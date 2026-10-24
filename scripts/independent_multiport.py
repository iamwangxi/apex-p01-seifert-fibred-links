#!/usr/bin/env python3
"""Independent offline adversarial checks for two-block splices. Standard library; stdout only; no writes.

Explicit S3 splices A/B/C/D/E; boundary cycles are counted as permutation orbits.
The two mixed supports use rectilinear embedded arcs on a punctured sphere.
Integer indices are propagated through the ENTIRE cut-open B complement on
an exact cubical cell decomposition. A second computation integrates winding
numbers of the oriented A-B cycles. No author face/potential table is used.
The mixed horizontal extension is checked at its exact bilinear extrema.
Class minimality and ordinary isotopy are topological inputs, not numerical
consequences. The report is deterministic and contains only repository-relative paths.
"""
from collections import Counter, defaultdict, deque
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
COUNTS = Counter()
PROTECTED = sorted((PARENT / 'proof').glob('*.md')) + [HERE / 'multiport.py', Path(__file__)]


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def floor(x):
    return x.numerator // x.denominator


def osc(xs):
    return max(xs) - min(xs)


def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def compositions(n, k):
    if k == 1:
        yield (n,)
        return
    for j in range(n + 1):
        for rest in compositions(n - j, k - 1):
            yield (j,) + rest


def cycles(n, shift):
    todo = set(range(n))
    ans = []
    while todo:
        a = min(todo)
        out = []
        b = a
        while b in todo:
            todo.remove(b)
            out.append(b)
            b = (b + shift) % n
        assert b == a
        ans.append(out)
    return ans


def horizontal(k, actual, tj, cone=None):
    """Integer sheet permutations, including filling cone-boundary cycles."""
    degree = abs(k)
    assert degree
    cone_shift = 0 if cone is None else cone[1]
    assert sum(actual) + tj + cone_shift == 0
    all_steps = actual + [tj] + ([] if cone is None else [cone_shift])
    reached = {0}
    queue = deque([0])
    while queue:
        j = queue.popleft()
        for d in all_steps:
            v = (j + d) % degree
            if v not in reached:
                reached.add(v)
                queue.append(v)
    assert len(reached) == degree, "horizontal cover must be connected"
    ordinary = [cycles(degree, s) for s in actual]
    assert all(len(c) == 1 for c in ordinary), "unit actual boundary"
    trace = cycles(degree, tj)
    q = len(trace)
    assert q == gcd(degree, abs(tj))
    chi = degree * (1 - len(actual) - (cone is not None))
    if cone is not None:
        r, sx = cone
        assert r * sx + k == 0
        cc = cycles(degree, sx)
        assert all(len(c) == r for c in cc)
        chi += len(cc)
    boundary = len(actual) + q
    g2 = 2 - boundary - chi
    assert g2 >= 0 and g2 % 2 == 0
    COUNTS["horizontal_permutation_covers"] += 1
    return dict(degree=degree, trace_count=q,
                trace_cycle_lengths=[len(c) for c in trace],
                chi=chi, boundary=boundary, genus=g2 // 2)


def product_block(eta, m, signs):
    k = eta * (m + sum(signs))
    actual = list(signs)
    if actual:
        actual[0] -= eta * k
    assert m + sum(actual) == 0
    return k, actual


def splice(name, psigns, qsigns, weight=1, p_twist=0, q_twist=0):
    """Positive (1,weight) regular fibres spliced to negative Hopf fibres.

    On the designated unknot tori the (mu,lambda) matrix is
    [[p_twist,1],[p_twist*q_twist+1,q_twist]].
    Fill actual meridians first: both sides become solid tori, whose meridians
    lambda_P/lambda_Q are glued with intersection one. This is S3.
    """
    sp, sq = sum(psigns), sum(qsigns)
    aa, dd = p_twist, q_twist
    mp, mq = aa * weight * sp - sq, weight * sp + dd * sq
    if weight == 1:
        kp, pa = product_block(1, mp, psigns)
        cone = None
    else:
        kp = weight * (mp + sp)
        pa = list(psigns)
        cone = (weight, -(mp + sp))
    kq, qa = product_block(-1, mq, qsigns)
    a, b = weight * (aa * dd + 1) + dd, aa * dd + 1
    c, d = aa * weight + 1 + a, aa + b
    assert a * d - b * c == -1 and c != 0
    assert [[a, b], [c, d]] == mm(mm([[0, 1], [1, 1]],
               [[aa, 1], [aa*dd+1, dd]]), [[weight, 1], [1, 0]])
    assert (kp, mp) == (a * kq + c * mq, b * kq + d * mq)
    q = gcd(abs(kp), abs(mp))
    assert q == gcd(abs(kq), abs(mq))
    if q:
        vp, vq = (mp//q, -kp//q), (mq//q, -kq//q)
        assert gcd(*map(abs, vp)) == gcd(*map(abs, vq)) == 1
        assert (a*vp[0]+b*vp[1], c*vp[0]+d*vp[1]) == (-vq[0], -vq[1])
    np, nq = len(psigns), len(qsigns)
    assert np >= 2 and nq >= 2
    # Reconstruct the oriented linking matrix from the coherent entries.
    sg = psigns + qsigns
    lk = []
    for i in range(np + nq):
        row = []
        for j in range(np + nq):
            z = 0 if i == j else (weight * (aa * weight + 1) if i < np and j < np else
                                  -(dd+1) if i >= np and j >= np else -weight)
            row.append(z * sg[i] * sg[j])
        lk.append(row)
    assert all(lk[i][j] for i in range(len(sg)) for j in range(i))
    out = dict(name=name, n_P=np, n_Q=nq, signs_P=psigns, signs_Q=qsigns,
               meridian_longitude_matrix=[[aa, 1], [aa*dd+1, dd]],
               fibre_matrix=[[a, b], [c, d]], k_P=kp, k_Q=kq,
               t_P=mp, t_Q=mq, q=q, filling_meridian_intersection=1)
    if kp:
        out["P_cover"] = horizontal(kp, pa, mp, cone)
        assert out["P_cover"]["trace_count"] == q
    if kq:
        out["Q_cover"] = horizontal(kq, qa, mq)
        assert out["Q_cover"]["trace_count"] == q
    if kp == 0 and kq:
        assert q == abs(sum(psigns)) <= np and (np - q) % 2 == 0
        assert abs(kq) == c * q
        out.update(reaching_annuli=q, other_annuli=(np - q) // 2,
                   main_genus=out["Q_cover"]["genus"])
    elif kp and kq:
        chi = out["P_cover"]["chi"] + out["Q_cover"]["chi"]
        g = (2 - np - nq - chi) // 2
        assert 2 - 2 * g - np - nq == chi
        assert g == out["P_cover"]["genus"] + out["Q_cover"]["genus"] + q - 1
        out["global_genus"] = g
    COUNTS["actual_splices"] += 1
    return out


def winding(p, line):
    ans = 0
    x, y = p
    for (ax, ay), (bx, by) in zip(line, line[1:]):
        cross = (bx - ax) * (y - ay) - (by - ay) * (x - ax)
        if ay <= y < by and cross > 0:
            ans += 1
        if by <= y < ay and cross < 0:
            ans -= 1
    return ans


class Cubical:
    def __init__(self, name, holes, arcs, box):
        self.name, self.holes, self.arcs, self.box = name, holes, arcs, box
        self.demands = {v: h[4] for v, h in holes.items()}
        x0, x1, y0, y1 = box
        self.cells = {(x, y) for x in range(x0, x1) for y in range(y0, y1)
                      if not any(cx-r <= x < cx+r and cy-r <= y < cy+r
                                 for cx, cy, r, _, _ in holes.values())}
        self.root = (x0, y0)
        self.walls = []
        self.adj = defaultdict(list)
        occupied, endpoints = {}, {}
        for e, (u, v, path) in enumerate(arcs):
            assert holes[u][3] == -1 and holes[v][3] == 1
            for point, node in ((path[0], u), (path[-1], v)):
                cx, cy, r, _, _ = holes[node]
                assert max(abs(point[0]-cx), abs(point[1]-cy)) == r
            walls = []
            points = set()
            for (ax, ay), (bx, by) in zip(path, path[1:]):
                assert (ax == bx) != (ay == by)
                if ax == bx:
                    for y in range(min(ay, by), max(ay, by)):
                        west, east = (ax-1, y), (ax, y)
                        left, right = (west, east) if by > ay else (east, west)
                        walls.append((left, right))
                        points.update(((ax, y), (ax, y+1)))
                else:
                    for x in range(min(ax, bx), max(ax, bx)):
                        north, south = (x, ay), (x, ay-1)
                        left, right = (north, south) if bx > ax else (south, north)
                        walls.append((left, right))
                        points.update(((x, ay), (x+1, ay)))
            for l, r in walls:
                assert l in self.cells and r in self.cells
                key = frozenset((l, r))
                assert key not in occupied, "overlapping support arcs"
                occupied[key] = (e, l, r)
            for point in points:
                assert point not in endpoints, (name, e, endpoints.get(point), point)
                endpoints[point] = e
            self.walls.append(walls)
        self.occupied = occupied
        for c in self.cells:
            for dd in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                n = (c[0]+dd[0], c[1]+dd[1])
                if n in self.cells:
                    wall = occupied.get(frozenset((c, n)))
                    e = None if wall is None else wall[0]
                    sign = 0 if wall is None else (1 if c == wall[2] else -1)
                    self.adj[c].append((n, e, sign))
        self.matchings = [bits for bits in product((0, 1), repeat=len(arcs)) if self.legal(bits)]
        self.ids = {a: i for i, a in enumerate(self.matchings)}
        assert self.matchings
        self.full = (1 << len(arcs)) - 1
        self.geom_cache = {}
        self.widths = {}
        self.phase_examples = []

    def legal(self, bits):
        return all(sum(bits[e] for e, (a, b, _) in enumerate(self.arcs) if v in (a, b)) == d
                   for v, d in self.demands.items())

    def whole_complement(self, a, b):
        """Only B is a barrier. A-only crossings change the whole-block index."""
        h = {self.root: 0}
        queue = deque([self.root])
        while queue:
            c = queue.popleft()
            for n, e, sign in self.adj[c]:
                if e is not None and b[e]:
                    continue
                new = h[c] + (sign * a[e] if e is not None else 0)
                if n in h:
                    assert h[n] == new, "nonzero period in B complement"
                else:
                    h[n] = new
                    queue.append(n)
        assert len(h) == len(self.cells), "ENTIRE B complement must be connected"
        return h

    def cycles_of_difference(self, a, b):
        outgoing = defaultdict(list)
        for e, (u, v, path) in enumerate(self.arcs):
            if a[e] == b[e]:
                continue
            if b[e]:
                u, v, path = v, u, list(reversed(path))
            outgoing[u].append((v, path))
        lines = []
        while any(outgoing.values()):
            start = next(v for v in outgoing if outgoing[v])
            c = start
            line = [self.holes[c][:2]]
            while True:
                v, path = outgoing[c].pop()
                line.extend(path)
                line.append(self.holes[v][:2])
                c = v
                if c == start:
                    break
            lines.append(line)
        return lines

    def check_distances(self):
        for i, a in enumerate(self.matchings):
            for j, b in enumerate(self.matchings):
                h = self.whole_complement(a, b)
                polygons = self.cycles_of_difference(a, b)
                for (x, y), height in h.items():
                    direct = sum(winding((F(2*x+1, 2), F(2*y+1, 2)), p) for p in polygons)
                    assert direct == height
                    COUNTS["cubical_cell_vs_cycle_winding"] += 1
                width = osc(h.values())
                assert (width == 0) == (i == j)
                self.widths[i, j] = width
                if self.name == "B-q3-varying-reaching":
                    self.fill_horizontal(a, b, h)
                COUNTS["whole_complement_pair_widths"] += 1
        return [[self.widths[i, j] for j in range(len(self.matchings))]
                for i in range(len(self.matchings))]

    def fill_horizontal(self, a, b, h):
        aj = [e for e, (u, _, _) in enumerate(self.arcs) if u == "J"]
        if all(a[e] == b[e] for e in aj):
            # Full horizontal-bearing component can be common; adds this index.
            assert min(h.values()) <= h[(-7, -3)] <= max(h.values())
            COUNTS["common_horizontal_components"] += 1
            return
        lo, hi = min(h.values()), max(h.values())
        value = h[(-7, -3)]
        events = []
        for e in sorted(aj, key=lambda e: self.arcs[e][2][0][1]):
            if a[e] and b[e]:
                order = ("A", "B") if value + 1 <= hi else ("B", "A")
                assert value + (1 if order[0] == "A" else -1) >= lo
            else:
                order = (("A",) if a[e] else ("B",) if b[e] else ())
            for letter in order:
                value += 1 if letter == "A" else -1
                assert lo <= value <= hi
                events.append((letter, value))
        assert value == h[(-7, -3)]
        positions = [i for i, e in enumerate(events) if e[0] == "B"]
        q = len(positions)
        assert q == 3
        nu = [events[i][1] for i in positions]
        counts = []
        for j, p in enumerate(positions):
            nxt = positions[(j+1) % q]
            if nxt <= p:
                nxt += len(events)
            counts.append(sum(events[k % len(events)][0] == "A" for k in range(p+1, nxt)))
        assert sum(counts) == q
        assert all(nu[(j+1) % q] == nu[j]+counts[j]-1 for j in range(q))
        aa = []
        for j in range(q):
            age, u = 0, (j-1) % q
            while counts[u] == 0:
                age += 1
                u = (u-1) % q
                assert age < q
            aa.append(F(nu[j]) + F(age+1, q+1))
        assert all(1+aa[(j+1) % q]-aa[j] > 0 for j in range(q))
        center = aa[0]
        assert floor(min(aa)) >= lo and 1+floor(max(aa)) <= hi
        for chi in (F(0), F(1, 7), F(1, 2), F(1)):
            vv = [center+chi*(v-center) for v in aa]
            for j in range(q):
                derivative = 1+vv[(j+1) % q]-vv[j]
                assert derivative > 0
                for t in (F(0), F(1, 11), F(1, 2), F(10, 11), F(1)):
                    height = (1-t)*vv[j]+t*(1+vv[(j+1) % q])
                    assert lo <= floor(height) <= hi
                    COUNTS["horizontal_extension_index_samples"] += 1
        # Exact extrema occur at chi,t in {0,1}; the inequality thus certifies
        # the entire bilinear collar, not just the displayed sample points.
        self.phase_examples.append(dict(range_P=[lo, hi], counts=counts,
                                        a=[str(x) for x in aa],
                                        range_Q=[floor(min(aa)), 1+floor(max(aa))]))
        COUNTS["noncommon_horizontal_fillings"] += 1

    def geometry(self, mask):
        if mask in self.geom_cache:
            return self.geom_cache[mask]
        faces, samples = {}, []
        for seed in sorted(self.cells):
            if seed in faces:
                continue
            f = len(samples)
            samples.append(seed)
            faces[seed] = f
            queue = deque([seed])
            while queue:
                c = queue.popleft()
                for n, e, _ in self.adj[c]:
                    if e is not None and (mask >> e) & 1:
                        continue
                    if n not in faces:
                        faces[n] = f
                        queue.append(n)
        lr = {}
        for e, walls in enumerate(self.walls):
            if (mask >> e) & 1:
                pp = {(faces[l], faces[r]) for l, r in walls}
                assert len(pp) == 1
                lr[e] = pp.pop()
        out = (len(samples), faces[self.root], lr)
        self.geom_cache[mask] = out
        COUNTS["cubical_support_rebuilds"] += 1
        return out

    def potentials(self, flow, ref, mask, root=None):
        n, default_root, lr = self.geometry(mask)
        root = default_root if root is None else root
        adj = defaultdict(list)
        for e, (l, r) in lr.items():
            delta = flow[e]-ref[e]
            adj[r].append((l, delta))
            adj[l].append((r, -delta))
        pot = {root: F(0)}
        queue = deque([root])
        while queue:
            f = queue.popleft()
            for g, jump in adj[f]:
                z = pot[f]+jump
                if g in pot:
                    assert pot[g] == z
                else:
                    pot[g] = z
                    queue.append(g)
        assert len(pot) == n
        return pot

    def decode(self, flow, refid=0, mask=None, root=None):
        mask = self.full if mask is None else mask
        ref = self.matchings[refid]
        assert all(not ref[e] for e in range(len(ref)) if not (mask >> e) & 1)
        pot = self.potentials(flow, ref, mask, root)
        _, _, lr = self.geometry(mask)
        cuts = sorted({F(0), F(1)} | {(-v) % 1 for v in pot.values()})
        bary, raw = defaultdict(F), set()
        def at(theta):
            rr = {f: floor(v+theta) for f, v in pot.items()}
            bits = [0]*len(ref)
            for e, (l, r) in lr.items():
                bits[e] = ref[e]+rr[l]-rr[r]
            assert set(bits) <= {0, 1} and self.legal(bits)
            z = self.ids[tuple(bits)]
            raw.add(z)
            return z
        for x, y in zip(cuts, cuts[1:]):
            bary[at((x+y)/2)] += y-x
        for x in cuts[:-1]:
            at(x)
        assert all(self.widths[i, j] <= 1 for i, j in combinations(raw, 2))
        assert tuple(sum(w*self.matchings[i][e] for i, w in bary.items())
                     for e in range(len(ref))) == flow
        return dict(bary)

    def carrier(self):
        flows = set()
        for cc in compositions(4, len(self.matchings)):
            flows.add(tuple(sum(F(c, 4)*a[e] for c, a in zip(cc, self.matchings))
                            for e in range(len(self.arcs))))
        for flow in sorted(flows):
            base = self.decode(flow)
            for r in range(len(self.matchings)):
                for f in range(self.geometry(self.full)[0]):
                    assert self.decode(flow, r, root=f) == base
                    COUNTS["carrier_reference_root_checks"] += 1
            mask = sum(1 << e for e, x in enumerate(flow) if x)
            r = next(i for i, a in enumerate(self.matchings)
                     if all(not a[e] for e in range(len(a)) if not (mask >> e) & 1))
            assert self.decode(flow, r, mask) == base
            COUNTS["zero_face_reconstructions"] += 1
        simplices = []
        for mask in range(1, 1 << len(self.matchings)):
            s = tuple(i for i in range(len(self.matchings)) if (mask >> i) & 1)
            if all(self.widths[i, j] <= 1 for i, j in combinations(s, 2)):
                simplices.append(s)
        maximal = [s for s in simplices if not any(set(s) < set(t) for t in simplices)]
        for s in maximal:
            for cc in compositions(5, len(s)):
                weights = [F(c, 5) for c in cc]
                flow = tuple(sum(w*self.matchings[i][e] for w, i in zip(weights, s))
                             for e in range(len(self.arcs)))
                assert self.decode(flow) == {i: w for i, w in zip(s, weights) if w}
                COUNTS["true_simplex_exact_recovery"] += 1
        return dict(vertices=len(self.matchings), faces=self.geometry(self.full)[0],
                    rational_flows=len(flows), true_simplices=len(simplices),
                    maximal_simplices=len(maximal), maximal_sizes=sorted({len(s) for s in maximal}))


def nested_q1():
    # Each lens has a used boundary component on BOTH sides; neither pair of
    # parallel edges is an isotopic duplicate. The outer cap is not a mark.
    holes = {"L": (-12, 0, 1, -1, 1), "R": (12, 0, 1, 1, 1),
             "l": (-6, 0, 1, -1, 1), "r": (6, 0, 1, 1, 1),
             "n": (-2, 0, 1, -1, 1), "p": (2, 0, 1, 1, 1),
             "J": (0, 18, 2, -1, 1), "z": (0, 30, 1, 1, 1)}
    arcs = [("L", "R", [(-12, 1), (-12, 10), (12, 10), (12, 1)]),
            ("L", "R", [(-12, -1), (-12, -10), (12, -10), (12, -1)]),
            ("l", "r", [(-6, 1), (-6, 5), (6, 5), (6, 1)]),
            ("l", "r", [(-6, -1), (-6, -5), (6, -5), (6, -1)]),
            ("n", "p", [(-1, 0), (1, 0)]),
            ("J", "z", [(0, 20), (0, 29)])]
    return Cubical("A-q1-nested", holes, arcs, (-16, 16, -14, 34))


def varying_q3():
    holes = {"J": (-10, 0, 3, -1, 3), "N": (10, 0, 3, -1, 1),
             "L": (-18, 0, 1, -1, 1), "R": (18, 0, 1, 1, 1),
             "n": (-2, 22, 1, -1, 1), "p": (2, 22, 1, 1, 1)}
    arcs = [("L", "R", [(-18, 1), (-18, 15), (18, 15), (18, 1)]),
            ("L", "R", [(-18, -1), (-18, -15), (18, -15), (18, -1)])]
    for i, (y, z, turn) in enumerate(((9, 2, -6), (3, 1, -4), (-3, -1, -4), (-9, -2, -6))):
        node = "p"+str(i)
        holes[node] = (0, y, 1, 1, 1)
        arcs.append(("J", node, [(-7, z), (turn, z), (turn, y), (-1, y)]))
    for i, (y, z, turn) in enumerate(((9, 2, 6), (3, 1, 4), (-3, -1, 4), (-9, -2, 6))):
        arcs.append(("N", "p"+str(i), [(7, z), (turn, z), (turn, y), (1, y)]))
    arcs.append(("n", "p", [(-1, 22), (1, 22)]))
    return Cubical("B-q3-varying-reaching", holes, arcs, (-22, 22, -19, 26))


def main():
    initial = {str(p.relative_to(PARENT)): digest(p) for p in PROTECTED}
    cases = [splice("A", [1]*4+[-1]*3, [1, 1, -1]),
             splice("B", [1]*6+[-1]*3, [1]*4+[-1], q_twist=2),
             splice("C", [1, 1, 1, -1], [1, 1, 1]),
             splice("D-r5", [1, 1, -1], [1, 1, 1], weight=5),
             splice("E-r3-c6", [1, 1, -1], [1, 1, 1], weight=3, q_twist=2)]
    cone_orders = [splice("cone-r"+str(r), [1, 1, -1], [1, 1, 1], weight=r)
                   for r in range(2, 32)]
    assert cases[0]["q"] == 1 and cases[1]["q"] == 3
    assert cases[1]["fibre_matrix"] == [[3, 1], [4, 1]]
    assert cases[1]["Q_cover"]["genus"] == 21
    assert cases[2]["k_P"] and cases[2]["k_Q"]
    assert cases[3]["P_cover"]["genus"] == 13
    assert cases[4]["fibre_matrix"][1][0] == 6 and cases[4]["k_P"] == -6
    assert gcd(3, cases[4]["fibre_matrix"][1][0]) == 3
    negative_G = [[1, 2], [1, 1]]
    negative_A = mm(mm([[0, 1], [1, 1]], negative_G), [[1, 1], [1, 0]])
    assert negative_A == [[2, 1], [5, 2]]
    assert negative_A[0][0]*negative_A[1][1]-negative_A[1][0]*negative_A[0][1] == -1
    models = []
    for m in (nested_q1(), varying_q3()):
        widths = m.check_distances()
        carrier = m.carrier()
        assert max(map(max, widths)) == 2
        models.append(dict(name=m.name, cells=len(m.cells),
                           matchings=[list(a) for a in m.matchings],
                           pair_width_matrix=widths, carrier=carrier,
                           distinct_boundary_fillings=list({json.dumps(x, sort_keys=True): x
                                                           for x in m.phase_examples}.values())))
    assert initial == {str(p.relative_to(PARENT)): digest(p) for p in PROTECTED}
    print(json.dumps(dict(status="all independent exact checks passed", splices=cases,
                          cone_orders_checked=list(range(2, 32)),
                          determinant_alone_negative_control=dict(
                              meridian_longitude_matrix=negative_G,
                              fibre_matrix=negative_A, filled_H1_order=abs(negative_G[0][1]),
                              caveat="This fixes the pattern meridians; no assertion about alternative unmarked meridian systems."),
                          models=models, counts=dict(COUNTS),
                          source_sha256=initial,
                          limitations=["No finite test proves ordinary isotopy localization or PS 3.3/3.5.",
                                       "Computed global widths use the actual horizontal extension; class minimality uses the audited topological lower bound.",
                                       "Finite carriers do not prove the arbitrary finite-height nullhomotopy.",
                                       "No output file, cache, network, environment-secret read, Git or subprocess is used."]),
                     ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
