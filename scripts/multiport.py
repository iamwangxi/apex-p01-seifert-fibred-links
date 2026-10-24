#!/usr/bin/env python3
"""Exact diagnostics for coherent multiple-port splices; no other checker is executed or imported.

Rebuilds planar faces from rational polylines and fundamental-cycle winding
signatures, including disconnected noncellular regions. Tests the new coherent
multiple-port carrier and the finite horizontal-filling inequalities.
Prints a deterministic JSON report; writes no file. This does not prove the topological lemmas.
"""
from collections import defaultdict, deque
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
COUNTS = defaultdict(int)


def floor(x):
    return x.numerator // x.denominator if isinstance(x, F) else x


def frac(x):
    return x - floor(x)


def osc(xs):
    return max(xs) - min(xs)


def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for j in range(n + 1):
            for tail in compositions(n - j, k - 1):
                yield (j,) + tail


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def minus(a, b):
    return (a[0] - b[0], a[1] - b[1])


def on_segment(p, a, b):
    return cross(minus(b, a), minus(p, a)) == 0 and all(
        min(a[i], b[i]) <= p[i] <= max(a[i], b[i]) for i in (0, 1))


def winding(p, polygon):
    w = 0
    for a, b in zip(polygon, polygon[1:]):
        assert not on_segment(p, a, b), (p, a, b)
        z = cross(minus(b, a), minus(p, a))
        if a[1] <= p[1] < b[1] and z > 0:
            w += 1
        if b[1] <= p[1] < a[1] and z < 0:
            w -= 1
    return w


class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, a):
        if self.p[a] != a:
            self.p[a] = self.find(self.p[a])
        return self.p[a]

    def join(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        self.p[a] = b
        return True


class Model:
    def __init__(self, name, vertices, edges, demands, outside, face_marks=None):
        self.name = name
        self.vertices = vertices
        self.edges = edges  # (negative, positive, polyline)
        self.demands = demands
        self.outside = outside
        self.face_marks = face_marks or {}
        self.n = len(edges)
        self.cache = {}
        self.matchings = []
        for bits in product((0, 1), repeat=self.n):
            if self.legal(bits):
                self.matchings.append(bits)
        assert self.matchings
        self.ids = {v: i for i, v in enumerate(self.matchings)}
        self.fullmask = (1 << self.n) - 1
        self.feasible = tuple(mask for mask in range(1 << self.n)
                              if any(all(not m[e] or (mask >> e) & 1 for e in range(self.n))
                                     for m in self.matchings))
        self.geom = self.geometry(self.fullmask)
        self.vertex_potentials = tuple(self.potential(
            self.geom, tuple(F(m[e] - self.matchings[0][e]) for e in range(self.n)), 0)
                                      for m in self.matchings)
        self.check_embedding()

    def legal(self, m):
        return all(sum(m[e] for e, (a, b, _) in enumerate(self.edges) if v in (a, b)) == d
                   for v, d in self.demands.items())

    def check_embedding(self):
        for i, (u, v, pts) in enumerate(self.edges):
            assert pts[0] == self.vertices[u] and pts[-1] == self.vertices[v]
            assert self.demands[u] > 0 and self.demands[v] == 1
            for j, (w, z, other) in enumerate(self.edges[:i]):
                allowed = {self.vertices[t] for t in (u, v) if t in (w, z)}
                for a, b in zip(pts, pts[1:]):
                    for c, d in zip(other, other[1:]):
                        s1 = cross(minus(b, a), minus(c, a))
                        s2 = cross(minus(b, a), minus(d, a))
                        t1 = cross(minus(d, c), minus(a, c))
                        t2 = cross(minus(d, c), minus(b, c))
                        assert not (s1 * s2 < 0 and t1 * t2 < 0)
                        for point in (a, b, c, d):
                            if on_segment(point, a, b) and on_segment(point, c, d):
                                assert point in allowed, (self.name, i, j, point)
        COUNTS["exact_polyline_embedding_models"] += 1

    def geometry(self, mask):
        if mask in self.cache:
            return self.cache[mask]
        keys = list(self.vertices)
        index = {v: i for i, v in enumerate(keys)}
        uf = UF(len(keys))
        tree = defaultdict(list)
        cycles = []
        for e, (u, v, line) in enumerate(self.edges):
            if not (mask >> e) & 1:
                continue
            if uf.join(index[u], index[v]):
                tree[u].append((v, e))
                tree[v].append((u, e))
            else:
                queue = deque([v])
                prev = {v: None}
                while u not in prev:
                    x = queue.popleft()
                    for y, f in tree[x]:
                        if y not in prev:
                            prev[y] = (x, f)
                            queue.append(y)
                back = []
                node = u
                while node != v:
                    before, f = prev[node]
                    back.append((before, node, f))
                    node = before
                route = list(reversed(back))
                polygon = list(line)  # u -> v
                for x, y, f in route:  # v -> u
                    a, b, pts = self.edges[f]
                    oriented = pts if (a, b) == (x, y) else tuple(reversed(pts))
                    assert polygon[-1] == oriented[0]
                    polygon.extend(oriented[1:])
                assert polygon[-1] == polygon[0]
                cycles.append(tuple(polygon))
        signature = lambda p: tuple(winding(p, c) for c in cycles)
        outside = signature(self.outside)
        signatures = {outside}
        raw_lr = {}
        for e, (_, _, line) in enumerate(self.edges):
            if not (mask >> e) & 1:
                continue
            candidates = []
            for a, b in zip(line, line[1:]):
                dx, dy = b[0] - a[0], b[1] - a[1]
                mid = ((F(a[0]) + b[0]) / 2, (F(a[1]) + b[1]) / 2)
                left = (mid[0] - F(dy, 1009), mid[1] + F(dx, 1009))
                right = (mid[0] + F(dy, 1009), mid[1] - F(dx, 1009))
                candidates.append((signature(left), signature(right)))
            assert all(x == candidates[0] for x in candidates), (self.name, mask, e)
            raw_lr[e] = candidates[0]
            signatures.update(candidates[0])
        order = [outside] + sorted(signatures - {outside})
        lookup = {s: i for i, s in enumerate(order)}
        lr = {e: (lookup[l], lookup[r]) for e, (l, r) in raw_lr.items()}
        components = len({uf.find(j) for j in range(len(keys))})
        expected_faces = bin(mask).count("1") - len(keys) + components + 1
        assert len(order) == expected_faces, (self.name, mask, len(order), expected_faces)
        marks = {name: lookup[signature(point)] for name, point in self.face_marks.items()}
        result = {"mask": mask, "faces": len(order), "lr": lr, "marks": marks}
        self.cache[mask] = result
        COUNTS["geometrically_rebuilt_supports"] += 1
        return result

    @staticmethod
    def potential(geom, current, root):
        adj = defaultdict(list)
        for e, (l, r) in geom["lr"].items():
            c = current[e]
            adj[r].append((l, c))
            adj[l].append((r, -c))
        values = {root: F(0)}
        queue = deque([root])
        while queue:
            f = queue.popleft()
            for g, step in adj[f]:
                nxt = values[f] + step
                if g in values:
                    assert values[g] == nxt
                else:
                    values[g] = nxt
                    queue.append(g)
        assert len(values) == geom["faces"]
        return tuple(values[j] for j in range(geom["faces"]))

    def distance(self, i, j):
        return osc([a - b for a, b in zip(self.vertex_potentials[i], self.vertex_potentials[j])])

    def decode(self, flow, mask=None, reference=0, root=0, check=True):
        mask = self.fullmask if mask is None else mask
        geom = self.geometry(mask)
        m = self.matchings[reference]
        assert all(not m[e] for e in range(self.n) if not (mask >> e) & 1)
        pot = self.potential(geom, tuple(flow[e] - m[e] for e in range(self.n)), root)
        thresholds = sorted({F(0), F(1)} | {frac(-x) for x in pot})

        def at(theta):
            q = tuple(floor(x + theta) for x in pot)
            out = [0] * self.n
            for e, (l, r) in geom["lr"].items():
                out[e] = m[e] + q[l] - q[r]
            out = tuple(out)
            assert all(x in (0, 1) for x in out)
            assert self.legal(out)
            COUNTS["legal_multiport_threshold_outputs"] += 1
            return self.ids[out]

        bary = defaultdict(F)
        raw = set()
        for lo, hi in zip(thresholds, thresholds[1:]):
            v = at((lo + hi) / 2)
            raw.add(v)
            bary[v] += hi - lo
        for theta in thresholds[:-1]:
            raw.add(at(theta))
        assert sum(bary.values()) == 1
        if check:
            for i, j in combinations(raw, 2):
                assert self.distance(i, j) <= 1
                COUNTS["true_global_output_pairs"] += 1
            expected = tuple(sum((mass * self.matchings[v][e] for v, mass in bary.items()), F(0))
                             for e in range(self.n))
            assert expected == tuple(flow)
            COUNTS["edge_expectations"] += 1
        return dict(bary)

    def run_carrier(self, denominator=6):
        flows = set()
        for counts in compositions(denominator, len(self.matchings)):
            flows.add(tuple(sum((F(counts[j], denominator) * m[e]
                                for j, m in enumerate(self.matchings)), F(0))
                            for e in range(self.n)))
        for flow in sorted(flows):
            expected = self.decode(flow)
            for reference in range(len(self.matchings)):
                for root in range(self.geom["faces"]):
                    assert self.decode(flow, reference=reference, root=root) == expected
                    COUNTS["reference_and_root_comparisons"] += 1
            for mask in self.feasible:
                if any(flow[e] and not (mask >> e) & 1 for e in range(self.n)):
                    continue
                ref = next(j for j, m in enumerate(self.matchings)
                           if all(not m[e] or (mask >> e) & 1 for e in range(self.n)))
                assert self.decode(flow, mask=mask, reference=ref) == expected
                COUNTS["zero_face_rebuilt_comparisons"] += 1
            COUNTS["distinct_rational_multiport_flows"] += 1

        simplices = []
        for bits in range(1, 1 << len(self.matchings)):
            s = tuple(j for j in range(len(self.matchings)) if (bits >> j) & 1)
            if all(self.distance(i, j) <= 1 for i, j in combinations(s, 2)):
                simplices.append(s)
        maximal = [s for s in simplices if not any(
            j not in s and all(self.distance(i, j) <= 1 for i in s)
            for j in range(len(self.matchings)))]
        for s in maximal:
            for counts in compositions(8, len(s)):
                weights = tuple(F(c, 8) for c in counts)
                flow = tuple(sum((weights[a] * self.matchings[j][e]
                                  for a, j in enumerate(s)), F(0)) for e in range(self.n))
                assert self.decode(flow) == {j: weights[a] for a, j in enumerate(s) if weights[a]}
                COUNTS["exact_true_simplex_recovery"] += 1
        return {"vertices": len(self.matchings), "feasible_supports": len(self.feasible),
                "faces": self.geom["faces"], "rational_flows": len(flows),
                "nonempty_true_simplices": len(simplices), "maximal_simplices": len(maximal),
                "maximal_dimensions": sorted(set(len(s) - 1 for s in maximal))}


def make_prism():
    v = {"J": (-2, 0), "N": (2, 0), "p1": (0, 1), "p2": (0, 0),
         "p3": (0, -1), "A": (-5, 0), "B": (5, 0), "C": (-1, 6), "D": (1, 6)}
    e = [("B", "A", (v["B"], (0, 4), v["A"])),
         ("B", "A", (v["B"], (0, -4), v["A"]))]
    e += [("J", f"p{i}", (v["J"], v[f"p{i}"])) for i in range(1, 4)]
    e += [("N", f"p{i}", (v["N"], v[f"p{i}"])) for i in range(1, 4)]
    e.append(("D", "C", (v["D"], v["C"])))
    demand = {k: (2 if k == "J" else 1) for k in v}
    return Model("demand-two nested prism", v, e, demand, (10, 10),
                 {"O": (10, 10), "L": (0, 3), "U": (0, F(1, 2)), "D": (0, F(-1, 2))})


def make_demand_three():
    v = {"J": (-3, 0), "N": (3, 0)}
    for i, y in enumerate((3, 1, -1, -3), 1):
        v[f"p{i}"] = (0, y)
    e = [("J", f"p{i}", (v["J"], v[f"p{i}"])) for i in range(1, 5)]
    e += [("N", f"p{i}", (v["N"], v[f"p{i}"])) for i in range(1, 5)]
    return Model("demand-three theta", v, e, {k: (3 if k == "J" else 1) for k in v}, (10, 10))


def check_matrix_covariance():
    for a, b, c, d in product(range(-4, 5), repeat=4):
        if a * d - b * c != -1 or not c:
            continue
        for kq, tq in product(range(-5, 6), repeat=2):
            kp, tp = a * kq + c * tq, b * kq + d * tq
            q = gcd(abs(kq), abs(tq))
            assert q == gcd(abs(kp), abs(tp))
            assert (q == 0) == (kp == 0 and kq == 0)
            if kp == 0 and kq != 0:
                assert abs(kq) == q * abs(c) and abs(tp) == q
            if kq == 0 and kp != 0:
                assert abs(kp) == q * abs(c) and abs(tq) == q
            COUNTS["unimodular_covector_cases"] += 1


def check_horizontal_fillings():
    for q in range(1, 7):
        for counts in compositions(q, q):
            nu = [0]
            for m in counts[:-1]:
                nu.append(nu[-1] + m - 1)
            assert nu[-1] + counts[-1] - 1 == 0
            ages = []
            for j in range(q):
                age = 0
                t = (j - 1) % q
                while counts[t] == 0:
                    age += 1
                    t = (t - 1) % q
                    assert age < q
                ages.append(age)
            base = [F(age + 1, q + 1) for age in ages]
            for scale, gauge in product((F(1), F(2, 3)), (-3, 2)):
                fractions = [F(1, 10) + scale * f * F(4, 5) for f in base]
                aa = [F(n) + f + gauge for n, f in zip(nu, fractions)]
                assert all(1 + aa[(j + 1) % q] - aa[j] > 0 for j in range(q))
                lo, hi = min(aa), max(aa)
                assert all(floor(aa[j]) == nu[j] + gauge for j in range(q))
                for center in (lo, hi, (lo + hi) / 2):
                    for cutoff in (F(0), F(1, 3), F(1)):
                        vv = [center + cutoff * (a - center) for a in aa]
                        assert all(lo <= z <= hi for z in vv)
                        for j in range(q):
                            derivative = 1 + vv[(j + 1) % q] - vv[j]
                            assert derivative > 0
                            for t in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1)):
                                height = (1 - t) * vv[j] + t * (1 + vv[(j + 1) % q])
                                assert lo <= height <= 1 + hi
                                assert floor(lo) <= floor(height) <= 1 + floor(hi)
                                COUNTS["horizontal_no_extra_index_values"] += 1
                            COUNTS["positive_fibre_derivatives"] += 1
                COUNTS["coherent_cyclic_boundary_arrays"] += 1
    # Genuine failures of omitted hypotheses in this finite analytic model.
    aa = (F(1, 10), F(17, 10), F(9, 10))
    assert all(1 + aa[(j + 1) % 3] - aa[j] > 0 for j in range(3))
    bad_v = (aa[0], aa[1], aa[0])  # different cutoffs on rho-related collars
    assert 1 + bad_v[2] - bad_v[1] < 0
    a = F(3, 10)
    wrong_center = F(23, 10)
    assert floor(wrong_center) > floor(a)
    return {"noninvariant_collar_cutoff_can_reverse_fibre_derivative": True,
            "center_outside_boundary_range_can_add_indices": True}


def check_examples():
    for np, nq in product(range(2, 9), repeat=2):
        for sp, sq in product(range(-np, np + 1, 2), range(-nq, nq + 1, 2)):
            kp, kq, tp, tq = sp - sq, -sp - sq, -sq, sp
            assert kp == kq + 2 * tq and tp == kq + tq
            q = gcd(abs(sp), abs(sq))
            assert q == gcd(abs(kp), abs(tp))
            if kp == 0 and kq:
                assert q == abs(sp) <= np and (np - q) % 2 == 0
                chi = abs(kq) * (1 - nq)
                genus_twice = 2 - nq - q - chi
                assert genus_twice >= 0 and genus_twice % 2 == 0
            COUNTS["Hopf_splice_sign_sum_cases"] += 1
    for r in range(2, 51):
        matrix = ((r, 1), (r + 1, 1))
        assert r - (r + 1) == -1
        kq, tq = -(r + 1), r
        assert matrix[0][0] * kq + matrix[1][0] * tq == 0
        assert matrix[0][1] * kq + matrix[1][1] * tq == -1
        assert gcd(abs(kq), abs(tq)) == 1
        assert (2 - 4 + 2 * (r + 1)) // 2 == r
        COUNTS["arbitrary_order_one_cone_witnesses"] += 1


check_matrix_covariance()
filling_controls = check_horizontal_fillings()
check_examples()
prism = make_prism()
theta = make_demand_three()
assert len(prism.matchings) == 6 and len(prism.feasible) == 57
assert len(theta.matchings) == 4
expected_lr = [("L", "O"), ("O", "L"), ("L", "U"), ("U", "D"), ("D", "L"),
               ("U", "L"), ("D", "U"), ("L", "D"), ("O", "O")]
for e, (l, r) in enumerate(expected_lr):
    assert prism.geom["lr"][e] == (prism.geom["marks"][l], prism.geom["marks"][r])
prism_results = prism.run_carrier()
theta_results = theta.run_carrier()
assert prism_results["nonempty_true_simplices"] == 31
assert prism_results["maximal_simplices"] == 3 and prism_results["maximal_dimensions"] == [3]
assert theta_results["nonempty_true_simplices"] == 15 and theta_results["maximal_simplices"] == 1
# The manuscript's first/last potential vertices and midpoint repair.
reference = (0, 1, 1, 1, 0, 0, 0, 1, 1)  # e1,M3,f
last = (1, 0, 0, 1, 1, 1, 0, 0, 1)       # e0,M1,f
first_id, last_id = prism.ids[reference], prism.ids[last]
assert prism.distance(first_id, last_id) == 2
mid = tuple(F(a + b, 2) for a, b in zip(reference, last))
middle_c = (0, 1, 0, 1, 1, 1, 0, 0, 1)   # e1,M1,f
middle_d = (1, 0, 1, 1, 0, 0, 0, 1, 1)   # e0,M3,f
assert prism.decode(mid) == {prism.ids[middle_c]: F(1, 2), prism.ids[middle_d]: F(1, 2)}
assert prism.distance(prism.ids[middle_c], prism.ids[middle_d]) == 1
report = {
    "status": "all exact finite assertions passed",
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "counts": dict(sorted(COUNTS.items())),
    "support_models": {prism.name: prism_results, theta.name: theta_results},
    "geometric_face_reconstruction": "fundamental-cycle winding signatures; no face or potential table supplied to the solver",
    "horizontal_filling_negative_controls": filling_controls,
    "mixed_distance_two_witness": {"q": 2, "supported_vertices": 6, "distance_first_last": 2,
                                    "midpoint_decoder": "half of e1,M1,f plus half of e0,M3,f"},
    "scope_limits": [
        "Matrix samples are algebraic covectors, not a claim that every sample is a realizable S3 link.",
        "Finite tests do not prove ordinary isotopy localization or horizontal relative uniqueness.",
        "Finite tests do not prove the direct Sakuma minimum lemma or PS Lemma 3.5.",
        "Finite tests do not prove the general finite-height or CW contractibility argument."
    ]
}
report["proof_sha256"] = {str(p.relative_to(HERE.parent)): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in sorted((HERE.parent / "proof").glob("*.md"))}
print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
