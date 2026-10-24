#!/usr/bin/env python3
"""Read-only exact adversarial diagnostics. Run with python3 -B.

No network, subprocess, third-party package, or file output. Geometry, dual
potentials, complete-B-complement widths and rounding are computed here rather
than importing the author's potential table. These are finite conditional tests,
not proofs of incompressibility, isotopy detection, PS, or contractibility.
"""
import hashlib
import json
from collections import Counter, defaultdict, deque
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE.parent
COUNTS = Counter()


def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for j in range(n + 1):
            for tail in compositions(n - j, k - 1):
                yield (j,) + tail


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def on_segment(a, b, p):
    return cross(a, b, p) == 0 and all(min(a[i], b[i]) <= p[i] <= max(a[i], b[i]) for i in (0, 1))


def meet(a, b, c, d):
    x, y, z, t = cross(a, b, c), cross(a, b, d), cross(c, d, a), cross(c, d, b)
    return ((x * y < 0 and z * t < 0) or on_segment(a, b, c) or on_segment(a, b, d)
            or on_segment(c, d, a) or on_segment(c, d, b))


def winding(p, polygon):
    value = 0
    for a, b in zip(polygon, polygon[1:]):
        assert not on_segment(a, b, p)
        if a[1] <= p[1] < b[1] and cross(a, b, p) > 0:
            value += 1
        if b[1] <= p[1] < a[1] and cross(a, b, p) < 0:
            value -= 1
    return value


class UF:
    def __init__(self, vertices):
        self.p = {v: v for v in vertices}

    def find(self, v):
        if self.p[v] != v:
            self.p[v] = self.find(self.p[v])
        return self.p[v]

    def join(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        self.p[a] = b
        return True


class Model:
    def __init__(self, name, vertices, edges, root):
        self.name = name
        self.vertices = vertices
        self.edges = [(a, b, tuple(tuple(map(F, p)) for p in points)) for a, b, points in edges]
        self.root = tuple(map(F, root))
        self.full = (1 << len(edges)) - 1
        self.cache = {}
        for a, b, points in self.edges:
            assert a in (3, 4) and b in (1, 2)
            assert points[0] == vertices[a] and points[-1] == vertices[b]
        # Verify embeddedness, including collinear-overlap exclusions.
        for ei, ej in combinations(range(len(edges)), 2):
            ai, bi, pi = self.edges[ei]
            aj, bj, pj = self.edges[ej]
            allowed = {vertices[v] for v in (ai, bi) if v in (aj, bj)}
            for a, b in zip(pi, pi[1:]):
                for c, d in zip(pj, pj[1:]):
                    if meet(a, b, c, d):
                        shared = set((a, b)) & set((c, d))
                        assert len(shared) == 1 and shared <= allowed
                        p = next(iter(shared))
                        other_i, other_j = (b if a == p else a), (d if c == p else c)
                        assert not on_segment(p, other_i, other_j)
                        assert not on_segment(p, other_j, other_i)
        self.matchings = []
        for mask in range(1 << len(edges)):
            if all(sum(bool(mask & (1 << e)) for e, (a, b, _) in enumerate(self.edges) if v in (a, b)) == 1
                   for v in vertices):
                self.matchings.append(tuple(int(bool(mask & (1 << e))) for e in range(len(edges))))
        self.lookup = {m: j for j, m in enumerate(self.matchings)}
        assert self.matchings
        self.feasible = [mask for mask in range(1 << len(edges))
                         if any(all(not x or mask & (1 << e) for e, x in enumerate(m)) for m in self.matchings)]
        for mask in self.feasible:
            self.geometry(mask)
        self.samples = sorted({tuple(sum(F(c[j], 4) * m[e] for j, m in enumerate(self.matchings))
                                     for e in range(len(edges)))
                               for c in compositions(4, len(self.matchings))})

    def geometry(self, mask):
        if mask in self.cache:
            return self.cache[mask]
        chosen = [e for e in range(len(self.edges)) if mask & (1 << e)]
        uf, tree, cycles = UF(self.vertices), defaultdict(list), []
        for e in chosen:
            a, b, points = self.edges[e]
            if uf.join(a, b):
                tree[a].append((b, e))
                tree[b].append((a, e))
                continue
            queue, previous = deque([b]), {b: None}
            while a not in previous:
                v = queue.popleft()
                for w, k in tree[v]:
                    if w not in previous:
                        previous[w] = (v, k)
                        queue.append(w)
            steps, v = [], a
            while v != b:
                w, k = previous[v]
                steps.append((w, v, k))
                v = w
            polygon = list(points)
            for start, end, k in reversed(steps):
                x, y, pp = self.edges[k]
                oriented = pp if (x, y) == (start, end) else tuple(reversed(pp))
                assert polygon[-1] == oriented[0]
                polygon.extend(oriented[1:])
            assert polygon[0] == polygon[-1]
            cycles.append(polygon)

        def signature(p):
            return tuple(winding(p, polygon) for polygon in cycles)

        lr, regions = {}, set()
        epsilon = F(1, 2 ** 20)
        for e in chosen:
            a, b = self.edges[e][2][:2]
            middle = tuple((a[k] + b[k]) / 2 for k in (0, 1))
            normal = (-(b[1] - a[1]), b[0] - a[0])
            probes = [tuple(middle[k] + sign * epsilon * normal[k] for k in (0, 1)) for sign in (1, -1)]
            for probe in probes:
                for other in chosen:
                    for c, d in zip(self.edges[other][2], self.edges[other][2][1:]):
                        if not (other == e and (c, d) == (a, b)):
                            assert not meet(middle, probe, c, d)
            lr[e] = tuple(signature(p) for p in probes)
            regions.update(lr[e])
        root = signature(self.root)
        regions.add(root)
        components = len({uf.find(v) for v in self.vertices})
        assert len(regions) == len(chosen) - len(self.vertices) + components + 1
        assert len(regions) == len(cycles) + 1
        out = (tuple(sorted(regions)), lr, root)
        self.cache[mask] = out
        COUNTS['geometrically_rebuilt_supports'] += 1
        return out

    def potential(self, w, reference, mask=None):
        if mask is None:
            mask = self.full
        regions, lr, root = self.geometry(mask)
        equations = [(l, r, w[e] - reference[e]) for e, (l, r) in lr.items()]
        return solve_potential(regions, root, equations)

    def complete_b(self, a, b):
        union = sum(1 << e for e in range(len(a)) if a[e] or b[e])
        regions, lr, root = self.geometry(union)
        # Only A-only walls are crossed; common and B-only walls remain cut.
        equations = [(l, r, F(1)) for e, (l, r) in lr.items() if a[e] and not b[e]]
        return solve_potential(regions, root, equations)


def solve_potential(regions, root, equations):
    adjacency = defaultdict(list)
    for l, r, delta in equations:
        adjacency[r].append((l, delta))
        adjacency[l].append((r, -delta))
    h, queue = {root: F(0)}, deque([root])
    while queue:
        v = queue.popleft()
        for w, delta in adjacency[v]:
            x = h[v] + delta
            if w in h:
                assert h[w] == x
            else:
                h[w] = x
                queue.append(w)
    assert set(h) == set(regions)
    return h


def models():
    vertices = {1: (0, 0), 2: (4, 4), 3: (4, 0), 4: (0, 4)}
    edges = [(3, 1, ((4, 0), (0, 0))), (3, 1, ((4, 0), (2, -2), (0, 0))),
             (4, 1, ((0, 4), (0, 0))), (3, 2, ((4, 0), (4, 4))),
             (4, 2, ((0, 4), (4, 4)))]
    five = Model('five_edge_JSJ_in_lens', vertices, edges, (2, -1))
    reflected = Model('reflected_five_edge', {v: (-p[0], p[1]) for v, p in vertices.items()},
                      [(a, b, [(-p[0], p[1]) for p in pp]) for a, b, pp in edges], (-2, -1))
    nested = Model('nested_disconnected', {1: (-4, 0), 2: (-1, 0), 3: (4, 0), 4: (1, 0)},
                   [(3, 1, ((4, 0), (0, 4), (-4, 0))),
                    (3, 1, ((4, 0), (0, -4), (-4, 0))),
                    (4, 2, ((1, 0), (0, 1), (-1, 0))),
                    (4, 2, ((1, 0), (0, -1), (-1, 0)))], (0, 0))
    square = Model('square_JSJ_inside', vertices, [edges[e] for e in (0, 2, 3, 4)], (2, 2))
    return [five, reflected, nested, square]


def floor(x):
    return x.numerator // x.denominator


def decode(pair, flows, reference, masks=None):
    if masks is None:
        masks = [g.full for g in pair]
    potentials = [g.potential(w, g.matchings[r], mask) for g, w, r, mask in zip(pair, flows, reference, masks)]
    bs = sorted({F(0), F(1)} | {(-x) % 1 for h in potentials for x in h.values()})

    def at(theta):
        result = []
        for g, ref, mask, h in zip(pair, reference, masks, potentials):
            regions, lr, root = g.geometry(mask)
            q = {f: floor(h[f] + theta) for f in regions}
            assert q[root] == 0
            output = list(g.matchings[ref])
            for e, (l, r) in lr.items():
                output[e] += q[l] - q[r]
            output = tuple(output)
            assert all(x in (0, 1) for x in output) and output in g.lookup
            for v in g.vertices:
                assert sum(output[e] for e, (a, b, _) in enumerate(g.edges) if v in (a, b)) == 1
            result.append(g.lookup[output])
        COUNTS['threshold_probes_including_collisions'] += 1
        return tuple(result)

    bary = defaultdict(F)
    outputs = set()
    for lo, hi in zip(bs, bs[1:]):
        vertex = at((lo + hi) / 2)
        bary[vertex] += hi - lo
        outputs.add(vertex)
    outputs.update(at(theta) for theta in bs[:-1])
    return dict(bary), outputs


def osc(values):
    return max(values) - min(values)


def cliques(vertices, distance):
    result = []

    def visit(prefix, candidates):
        if prefix:
            result.append(tuple(prefix))
        for j, v in enumerate(candidates):
            visit(prefix + [v], [w for w in candidates[j + 1:] if distance[v, w] <= 1])
    visit([], list(vertices))
    maximal = [s for s in result if not any(v not in s and all(distance[v, w] <= 1 for w in s) for v in vertices)]
    return result, maximal


def check_pair(pair):
    vertices = list(product(*(range(len(g.matchings)) for g in pair)))
    distance = {}
    for a, b in product(vertices, repeat=2):
        complete = [g.complete_b(g.matchings[a[i]], g.matchings[b[i]]) for i, g in enumerate(pair)]
        by_walls = osc([x for h in complete for x in h.values()])
        potentials = [g.potential(g.matchings[a[i]], g.matchings[b[i]]) for i, g in enumerate(pair)]
        by_circulation = osc([x for h in potentials for x in h.values()])
        assert by_walls == by_circulation
        distance[a, b] = by_walls
        COUNTS['complete_B_vs_full_circulation'] += 1
    assert all(distance[a, b] == distance[b, a] and (distance[a, b] == 0) == (a == b)
               for a, b in product(vertices, repeat=2))
    for flows in product(*(g.samples for g in pair)):
        bary, outputs = decode(pair, flows, (0, 0))
        assert sum(bary.values()) == 1
        assert all(distance[a, b] <= 1 for a, b in product(outputs, repeat=2))
        for reference in vertices:
            other, raw = decode(pair, flows, reference)
            assert other == bary and raw == outputs
            COUNTS['reference_pair_comparisons'] += 1
        for side, g in enumerate(pair):
            recovered = tuple(sum(weight * g.matchings[v[side]][e] for v, weight in bary.items())
                              for e in range(len(g.edges)))
            assert recovered == flows[side]
        masks = [sum(1 << e for e, x in enumerate(w) if x) for w in flows]
        supported_reference = next(iter(bary))
        reduced, _ = decode(pair, flows, supported_reference, masks)
        assert reduced == bary
        COUNTS['zero_support_rebuilds'] += 1
        COUNTS['rational_product_flows'] += 1
    simplices, maximal = cliques(vertices, distance)
    for simplex in maximal:
        for coeff in compositions(5, len(simplex)):
            weights = [F(x, 5) for x in coeff]
            flows = [tuple(sum(weights[j] * g.matchings[v[i]][e] for j, v in enumerate(simplex))
                           for e in range(len(g.edges))) for i, g in enumerate(pair)]
            bary, _ = decode(pair, flows, (0, 0))
            assert bary == {v: weights[j] for j, v in enumerate(simplex) if weights[j]}
            COUNTS['exact_simplex_recoveries'] += 1
    # Check shared-threshold distributions on every vertex-to-vertex segment,
    # with explicit near-collision probes. L1 <= 2 sum |delta u| by coupling theta.
    times = sorted({F(k, 8) for k in range(9)} | {F(1, 2) - F(1, 257), F(1, 2) + F(1, 257)})
    for a, b in combinations(vertices, 2):
        last = None
        for t in times:
            flows = [tuple((1 - t) * g.matchings[a[i]][e] + t * g.matchings[b[i]][e]
                           for e in range(len(g.edges))) for i, g in enumerate(pair)]
            bary, _ = decode(pair, flows, (0, 0))
            h = [g.potential(flows[i], g.matchings[0]) for i, g in enumerate(pair)]
            if last is not None:
                old_bary, old_h = last
                l1 = sum(abs(bary.get(v, 0) - old_bary.get(v, 0)) for v in vertices)
                bound = 2 * sum(abs(h[i][f] - old_h[i][f]) for i in range(2) for f in h[i])
                assert l1 <= bound
                COUNTS['collision_continuity_bounds'] += 1
            last = bary, h
    return {'blocks': [g.name for g in pair], 'vertices': len(vertices),
            'nonempty_simplices': len(simplices), 'maximal_simplices': len(maximal),
            'maximal_dimensions': sorted({len(s) - 1 for s in maximal})}


def check_offsets():
    # A connected four-chamber seam graph with a cycle, plus a leaf. Local
    # potentials use deliberately unrelated integer constants.
    edges = [(0, 1), (1, 2), (2, 0), (2, 3)]
    for seed in range(100):
        offsets = [(seed * (j + 2) + j * j) % 19 - 9 for j in range(4)]
        equations = []
        for e, (a, b) in enumerate(edges):
            global_value = seed - 2 * e
            ha, hb = global_value - offsets[a], global_value - offsets[b]
            equations.append((a, b, hb - ha))
        h = solve_potential(range(4), 0, equations)
        assert all(h[j] == offsets[j] - offsets[0] for j in range(4))
        broken = list(equations)
        a, b, delta = broken[2]
        broken[2] = (a, b, delta + 1)
        try:
            solve_potential(range(4), 0, broken)
        except AssertionError:
            pass
        else:
            raise AssertionError('A contradictory seam cycle was accepted')
        COUNTS['offset_cycle_and_inconsistency_pairs'] += 1


def check_linking():
    swap = ((0, 1), (1, 0))
    hp, hq, dq = (1, 1), (-1, 1), (1, 0)
    image_hp = tuple(sum(swap[i][j] * hp[j] for j in range(2)) for i in range(2))
    assert image_hp == tuple(hq[j] + 2 * dq[j] for j in range(2))
    assert abs(image_hp[0] * hq[1] - image_hp[1] * hq[0]) == 2
    # Derive cross coefficients by substituting the distinguished meridians
    # into each OLD actual preferred longitude; do not input a linking table.
    p_meridian, q_meridian = [0] * 4 + [-1] * 4, [1] * 4 + [0] * 4
    coherent = []
    for i in range(8):
        row = list(p_meridian if i < 4 else [-x for x in q_meridian])
        for j in range(8):
            if j != i and (j < 4) == (i < 4):
                row[j] += 1 if i < 4 else -1
        coherent.append(row)
    eps = [1, 1, -1, -1] * 2
    actual = [[eps[i] * eps[j] * coherent[i][j] for j in range(8)] for i in range(8)]
    assert all(actual[i][j] == actual[j][i] for i in range(8) for j in range(8))
    assert all(actual[i][j] != 0 for i in range(8) for j in range(8) if i != j)
    assert [sum(row) for row in actual] == [-1] * 4 + [1] * 4
    COUNTS['derived_linking_rows'] = 8
    return actual


def main():
    sources = sorted((TARGET / 'proof').glob('*.md')) + [HERE / 'empty_trace.py', Path(__file__)]
    hashes = {str(p.relative_to(TARGET)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    data = models()
    # Reproduce the author's coordinates without using them as input.
    original = data[0]
    by_edges = {m: j for j, m in enumerate(original.matchings)}
    a0, a1, b = [by_edges[m] for m in ((1, 0, 0, 0, 1), (0, 1, 0, 0, 1), (0, 0, 1, 1, 0))]
    r, s, u, v = (b, b), (a1, a0), (a1, b), (b, a0)
    profiles = [list(original.complete_b(original.matchings[s[i]], original.matchings[r[i]]).values()) for i in range(2)]
    assert [osc(h) for h in profiles] == [1, 1]
    assert osc(sum(profiles, [])) == 2
    midpoint = [tuple(F(original.matchings[r[i]][e] + original.matchings[s[i]][e], 2)
                      for e in range(len(original.edges))) for i in range(2)]
    bary, _ = decode([original, original], midpoint, r)
    assert bary == {u: F(1, 2), v: F(1, 2)}
    nested = data[2]
    upper = nested.lookup[(1, 0, 1, 0)]
    lower = nested.lookup[(0, 1, 0, 1)]
    nr, ns = (upper, lower), (lower, upper)
    nested_profiles = [list(nested.complete_b(nested.matchings[ns[i]], nested.matchings[nr[i]]).values())
                       for i in range(2)]
    assert [osc(h) for h in nested_profiles] == [2, 2]
    assert osc(sum(nested_profiles, [])) == 4
    cases = [check_pair(pair) for pair in product(data, repeat=2)]
    check_offsets()
    linking = check_linking()
    assert hashes == {str(p.relative_to(TARGET)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    result = {'status': 'all exact assertions passed', 'source_sha256': hashes,
              'independent_counts': dict(sorted(COUNTS.items())),
              'local_models': [{'name': g.name, 'matchings': len(g.matchings),
                                'feasible_supports': len(g.feasible), 'sample_flows': len(g.samples)} for g in data],
              'product_cases': cases, 'derived_linking_matrix': linking,
              'new_nested_counterexample_to_local_max': {'local_distances': [2, 2], 'global_distance': 4},
              'limits': ['Finite geometric and rational diagnostics only.',
                         'No proof of all-genus cut classification, arbitrary isotopy, or PS.',
                         'No proof of the infinite finite-template construction.',
                         'Writes no file, including no JSON or bytecode.']}
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
