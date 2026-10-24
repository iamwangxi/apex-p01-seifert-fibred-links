#!/usr/bin/env python3
"""Geometric geometry-side audit: exact PL examples, explicit parallel allocation, decoder.

Standard library only. Writes nothing, including no JSON or bytecode; run with -B.
The two examples are independently specified here. Regions are recovered from
polygonal winding signatures, not copied from the author's left/right tables.
Class distances use the already-established Seifert theorem; no finite computation
here proves 3D simultaneous verticalisation or detects arbitrary ambient isotopy.
No directory traversal, network, Git, .env access, or subprocess is used.
"""
from collections import Counter, deque
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import sys

COUNTS = Counter()


def pt(x, y):
    return Q(x), Q(y)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def scale(a, t):
    return a[0] * t, a[1] * t


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def side(a, b, c):
    return cross(sub(b, a), sub(c, a))


def on_segment(p, a, b):
    return (side(a, b, p) == 0 and
            all(min(a[i], b[i]) <= p[i] <= max(a[i], b[i]) for i in (0, 1)))


def intersect(a, b, c, d):
    s1, s2, s3, s4 = side(a, b, c), side(a, b, d), side(c, d, a), side(c, d, b)
    return (s1 * s2 < 0 and s3 * s4 < 0 or
            any((on_segment(p, r, s)) for p, r, s in
                ((a, c, d), (b, c, d), (c, a, b), (d, a, b))))


def meet_only_at(a, b, c, d, p):
    if not intersect(a, b, c, d):
        return True
    if not (p in (a, b) and p in (c, d)):
        return False
    if side(a, b, c) or side(a, b, d):
        return True
    other1 = b if a == p else a
    other2 = d if c == p else c
    return sum(sub(other1, p)[i] * sub(other2, p)[i] for i in (0, 1)) < 0


def winding(p, polygon):
    value = 0
    for a, b in zip(polygon, polygon[1:]):
        assert not on_segment(p, a, b), (p, a, b)
        if a[1] <= p[1] < b[1] and side(a, b, p) > 0:
            value += 1
        if b[1] <= p[1] < a[1] and side(a, b, p) < 0:
            value -= 1
    return value


def compositions(total, length):
    if length == 1:
        yield total,
    else:
        for a in range(total + 1):
            for rest in compositions(total - a, length - 1):
                yield (a,) + rest


class Model:
    def __init__(self, name, weights, vertices, edges, cones, parallel_pairs):
        self.name, self.weights = name, weights
        self.vertices = vertices  # label -> (position, sign)
        self.edges = edges  # name -> (negative label, positive label, PL points)
        self.cones, self.parallel_pairs = cones, parallel_pairs
        self.all_edges = tuple(sorted(edges))
        for e, (a, b, points) in edges.items():
            assert vertices[a][1] == -1 and vertices[b][1] == 1
            assert points[0] == vertices[a][0] and points[-1] == vertices[b][0]
        self.segments = [(e, i, a, b) for e, (_, _, points) in edges.items()
                         for i, (a, b) in enumerate(zip(points, points[1:]))]
        self.validate_embedding()

    def validate_embedding(self):
        for (e, i, a, b), (f, j, c, d) in combinations(self.segments, 2):
            if not intersect(a, b, c, d):
                continue
            allowed = set()
            if e == f and abs(i - j) == 1:
                allowed = {a, b} & {c, d}
            if e != f:
                for v in set(self.edges[e][:2]) & set(self.edges[f][:2]):
                    allowed.add(self.vertices[v][0])
            assert any(meet_only_at(a, b, c, d, p) for p in allowed), (e, f, i, j)
            COUNTS['embedded_segment_pairs'] += 1
        for _, p in self.cones:
            assert not any(on_segment(p, a, b) for _, _, a, b in self.segments)

    @lru_cache(None)
    def matchings(self, support):
        incident = {v: [] for v in self.vertices}
        for e in support:
            a, b, _ = self.edges[e]
            incident[a].append(e)
            incident[b].append(e)

        def visit(remaining, chosen):
            if not remaining:
                yield tuple(sorted(chosen))
                return
            v = min(remaining)
            for e in incident[v]:
                a, b, _ = self.edges[e]
                if a in remaining and b in remaining:
                    yield from visit(remaining - {a, b}, chosen + (e,))

        return tuple(sorted(set(visit(set(self.vertices), ()))))

    def tree_cycles(self, support):
        parent = {v: v for v in self.vertices}
        tree = {v: [] for v in self.vertices}
        cycles = []

        def root(v):
            while parent[v] != v:
                v = parent[v]
            return v

        for e in support:
            a, b, points = self.edges[e]
            if root(a) != root(b):
                parent[root(a)] = root(b)
                tree[a].append((b, e))
                tree[b].append((a, e))
                continue
            prev, queue = {b: None}, deque([b])
            while a not in prev:
                u = queue.popleft()
                for v, f in tree[u]:
                    if v not in prev:
                        prev[v] = (u, f)
                        queue.append(v)
            path, v = [], a
            while v != b:
                u, f = prev[v]
                path.append((u, v, f))
                v = u
            polygon = list(points)
            for u, v, f in reversed(path):
                x, y, route = self.edges[f]
                if x != u:
                    route = tuple(reversed(route))
                assert route[0] == polygon[-1]
                polygon.extend(route[1:])
            assert polygon[-1] == polygon[0]
            cycles.append(tuple(polygon))
        return cycles, len({root(v) for v in self.vertices})

    @lru_cache(None)
    def regions(self, support):
        cycles, components = self.tree_cycles(support)
        active_segments = [(e, i, a, b) for e, i, a, b in self.segments if e in support]

        def signature(p):
            return tuple(winding(p, polygon) for polygon in cycles)

        face_pairs = {}
        for e in support:
            pairs = set()
            for f, i, a, b in active_segments:
                if f != e:
                    continue
                mid, direction = scale(add(a, b), Q(1, 2)), sub(b, a)
                normal = (-direction[1], direction[0])
                eps = Q(1, 16)
                while True:
                    left, right = add(mid, scale(normal, eps)), sub(mid, scale(normal, eps))
                    clear = True
                    for g, j, c, d in active_segments:
                        if (g, j) == (f, i):
                            continue
                        if intersect(mid, left, c, d) or intersect(mid, right, c, d):
                            clear = False
                            break
                    if clear:
                        break
                    eps /= 2
                pairs.add((signature(left), signature(right)))
            assert len(pairs) == 1, (e, pairs)
            face_pairs[e] = pairs.pop()
        outer = (0,) * len(cycles)
        faces = {outer} | {f for pair in face_pairs.values() for f in pair}
        assert len(faces) == len(support) - len(self.vertices) + components + 1
        dual = {f: set() for f in faces}
        for left, right in face_pairs.values():
            dual[left].add(right)
            dual[right].add(left)
        reached, queue = {outer}, deque([outer])
        while queue:
            for f in dual[queue.popleft()]:
                if f not in reached:
                    reached.add(f)
                    queue.append(f)
        assert reached == faces
        return tuple(sorted(faces)), face_pairs, outer

    def flow(self, bary):
        return {e: sum((mass for m, mass in bary.items() if e in m), Q(0))
                for e in self.all_edges}

    def potential(self, support, flow, reference, root=None):
        faces, pairs, outer = self.regions(support)
        root = outer if root is None else root
        adjacency = {f: [] for f in faces}
        for e, (left, right) in pairs.items():
            jump = flow[e] - Q(e in reference)
            adjacency[right].append((left, jump))
            adjacency[left].append((right, -jump))
        u, queue = {root: Q(0)}, deque([root])
        while queue:
            f = queue.popleft()
            for g, jump in adjacency[f]:
                value = u[f] + jump
                if g in u:
                    assert u[g] == value
                else:
                    u[g] = value
                    queue.append(g)
        assert set(u) == set(faces)
        return u

    @lru_cache(None)
    def block_width(self, first, second):
        # Re-extract the union's regions; cross first-only walls, never second walls.
        support = tuple(sorted(set(first) | set(second)))
        faces, pairs, outer = self.regions(support)
        adjacency = {f: [] for f in faces}
        for e in set(first) - set(second):
            left, right = pairs[e]
            adjacency[right].append((left, 1))
            adjacency[left].append((right, -1))
        height, queue = {outer: 0}, deque([outer])
        while queue:
            f = queue.popleft()
            for g, jump in adjacency[f]:
                value = height[f] + jump
                if g in height:
                    assert height[g] == value
                else:
                    height[g] = value
                    queue.append(g)
        assert set(height) == set(faces), (first, second, height, faces)
        return max(height.values()) - min(height.values())

    def true_simplex(self, bary):
        return all(self.block_width(a, b) == 1 for a, b in combinations(bary, 2))

    def decode(self, support, flow, reference=None, root=None):
        matchings = self.matchings(support)
        reference = matchings[0] if reference is None else reference
        u = self.potential(support, flow, reference, root)
        _, pairs, _ = self.regions(support)
        cuts = sorted({Q(0), Q(1)} | {(-v) % 1 for v in u.values()})

        def at(theta):
            q = {f: (value + theta).__floor__() for f, value in u.items()}
            bits = {e: int(e in reference) + q[left] - q[right]
                    for e, (left, right) in pairs.items()}
            assert set(bits.values()) <= {0, 1}
            m = tuple(sorted(e for e, bit in bits.items() if bit))
            assert m in matchings
            assert all(flow[e] > 0 for e in m)
            return m

        result = Counter()
        for low, high in zip(cuts, cuts[1:]):
            result[at((low + high) / 2)] += high - low
            COUNTS['positive_threshold_intervals'] += 1
        for theta in cuts[:-1]:
            at(theta)
            COUNTS['exact_threshold_probes'] += 1
        result = dict(result)
        assert sum(result.values()) == 1
        assert self.flow(result) == flow
        assert self.true_simplex(result)
        COUNTS['decoder_calls'] += 1
        return result

    def parallel_feature_check(self):
        result = []
        for e, f in self.parallel_pairs:
            a, b, p = self.edges[e]
            c, d, q = self.edges[f]
            assert (a, b) == (c, d)
            polygon = tuple(p) + tuple(reversed(q))[1:]
            features = [(str(v), point) for v, (point, _) in self.vertices.items()
                        if v not in (a, b)]
            features += [('cone_' + str(order), point) for order, point in self.cones]
            inside = [name for name, point in features if winding(point, polygon)]
            outside = [name for name, point in features if not winding(point, polygon)]
            assert inside and outside, (e, f, inside, outside)
            result.append({'arcs': [e, f], 'features_on_sides': [inside, outside]})
        return result

    def allocated_copies(self):
        """Real rational PL copies, mitered then trimmed at small square holes."""
        matchings, copies = self.matchings(self.all_edges), []
        radius, epsilon = Q(1, 100), Q(1, 10**6)

        def clip(a, b, centre):
            assert all(abs(a[i] - centre[i]) < radius for i in (0, 1))
            direction = sub(b, a)
            times = [(centre[i] + (radius if direction[i] > 0 else -radius) - a[i]) /
                     direction[i] for i in (0, 1) if direction[i]]
            t = min(times)
            assert 0 < t < 1
            return add(a, scale(direction, t))

        for e in self.all_edges:
            a, b, path = self.edges[e]
            occurrences = [m for m in matchings if e in m]
            for rank, m in enumerate(occurrences):
                delta = (2 * rank + 1 - len(occurrences)) * epsilon
                directions = [sub(y, x) for x, y in zip(path, path[1:])]

                def endpoint(p, direction):
                    norm = sum(x * x for x in direction)
                    return add(p, scale((-direction[1], direction[0]), delta / norm))

                offset = [endpoint(path[0], directions[0])]
                for i in range(1, len(path) - 1):
                    x, y = directions[i - 1], directions[i]
                    det = cross(x, y)
                    assert det
                    # Solve cross(x,v)=delta=cross(y,v) at the original bend.
                    v = ((delta * y[0] - x[0] * delta) / det,
                         (delta * y[1] - x[1] * delta) / det)
                    assert cross(x, v) == delta == cross(y, v)
                    offset.append(add(path[i], v))
                offset.append(endpoint(path[-1], directions[-1]))
                old_first, old_last = offset[0], offset[-1]
                offset[0] = clip(old_first, offset[1], self.vertices[a][0])
                offset[-1] = clip(old_last, old_first if len(offset) == 2 else offset[-2],
                                  self.vertices[b][0])
                copies.append((m, e, tuple(offset)))
        segments = [(k, i, a, b) for k, (_, _, path) in enumerate(copies)
                    for i, (a, b) in enumerate(zip(path, path[1:]))]
        for (k, i, a, b), (l, j, c, d) in combinations(segments, 2):
            if k == l and abs(i - j) == 1:
                common = ({a, b} & {c, d}).pop()
                assert meet_only_at(a, b, c, d, common)
            else:
                assert not intersect(a, b, c, d), (k, l, i, j)
            COUNTS['allocated_segment_pair_checks'] += 1
        slots = {v: [] for v in self.vertices}
        for m, e, path in copies:
            a, b, _ = self.edges[e]
            slots[a].append(path[0])
            slots[b].append(path[-1])
        for v, endpoints in slots.items():
            assert len(endpoints) == len(matchings) == len(set(endpoints))
        return {'annular_occurrences': len(copies),
                'distinct_boundary_curves_per_actual_torus': len(matchings),
                'all_allocated_arcs_disjoint': True}


def models():
    avertices = {1: (pt(-6, 0), 1), 2: (pt(6, 0), -1),
                 3: (pt(-2, 0), 1), 4: (pt(2, 0), -1),
                 5: (pt(8, 0), 1), 6: (pt(10, 0), -1)}
    aedges = {
        'a0': (2, 1, (pt(6, 0), pt(0, 6), pt(-6, 0))),
        'a1': (2, 1, (pt(6, 0), pt(0, -6), pt(-6, 0))),
        'b0': (4, 3, (pt(2, 0), pt(0, 2), pt(-2, 0))),
        'b1': (4, 3, (pt(2, 0), pt(0, -2), pt(-2, 0))),
        'c': (6, 5, (pt(10, 0), pt(8, 0))),
    }
    ac = [(3, pt(0, 4)), (5, pt(0, 1))]
    positions = [(0, 0), (4, 0), (6, 2), (6, 6),
                 (4, 8), (0, 8), (-2, 6), (-2, 2)]
    bvertices = {i + 1: (pt(*p), 1 if i % 2 == 0 else -1)
                 for i, p in enumerate(positions)}

    def straight(a, b):
        return a, b, (bvertices[a][0], bvertices[b][0])

    bedges = {'a0': straight(2, 1), 'b0': straight(6, 5),
              'r': straight(4, 3), 'l': straight(8, 7),
              'd0': straight(2, 3), 'd1': straight(4, 5),
              'd2': straight(6, 7), 'd3': straight(8, 1),
              'a1': (2, 1, (pt(4, 0), pt(2, -2), pt(0, 0))),
              'b1': (6, 5, (pt(0, 8), pt(2, 10), pt(4, 8)))}
    bc = [(2, pt(2, Q(-1, 2))), (7, pt(2, Q(17, 2)))]
    return [Model('six_boundary_nested_T18_30', (3, 5), avertices, aedges, ac,
                  [('a0', 'a1'), ('b0', 'b1')]),
            Model('eight_boundary_connected_T16_56', (2, 7), bvertices, bedges, bc,
                  [('a0', 'a1'), ('b0', 'b1')])]


def verify(g):
    full = g.all_edges
    all_matchings = g.matchings(full)
    reference = all_matchings[0]
    full_faces, _, root = g.regions(full)
    potentials = {m: g.potential(full, g.flow({m: Q(1)}), reference) for m in all_matchings}
    for first, second in product(all_matchings, repeat=2):
        diff = [potentials[first][f] - potentials[second][f] for f in full_faces]
        assert max(diff) - min(diff) == g.block_width(first, second)
        COUNTS['independent_block_width_comparisons'] += 1
    feasible, sample_count = 0, 0
    for mask in range(1 << len(full)):
        support = tuple(e for i, e in enumerate(full) if mask & (1 << i))
        ms = g.matchings(support)
        if not ms:
            continue
        feasible += 1
        for amounts in compositions(4, len(ms)):
            sample_count += 1
            bary = {m: Q(a, 4) for m, a in zip(ms, amounts) if a}
            flow = g.flow(bary)
            decoded = g.decode(support, flow)
            if g.true_simplex(bary):
                assert decoded == bary
                COUNTS['exact_recovery_on_cyclic_simplices'] += 1
            positive = tuple(e for e in support if flow[e])
            assert g.decode(positive, flow) == decoded
            COUNTS['zero_edge_face_reextractions'] += 1
            if sample_count % 7 == 0:
                for ref in ms:
                    assert g.decode(support, flow, ref) == decoded
                    COUNTS['reference_changes'] += 1
                for f in g.regions(support)[0]:
                    assert g.decode(support, flow, root=f) == decoded
                    COUNTS['root_changes'] += 1
            for t in (Q(0), Q(1, 3), Q(1, 2), Q(1)):
                h = {m: (1 - t) * bary.get(m, 0) + t * decoded.get(m, 0)
                     for m in set(bary) | set(decoded)}
                h = {m: c for m, c in h.items() if c}
                assert set(h) <= set(ms) and sum(h.values()) == 1
                assert g.flow(h) == flow
                assert g.decode(support, g.flow(h)) == decoded
                if g.true_simplex(bary):
                    assert h == bary
                if t == 0:
                    assert h == bary
                if t == 1:
                    assert h == decoded
                COUNTS['homotopy_checks'] += 1
    labels = {}
    fixed = ('c',) if len(g.vertices) == 6 else ('l', 'r')
    for i, j in product(range(2), repeat=2):
        labels[str(i) + str(j)] = tuple(sorted(('a' + str(i), 'b' + str(j)) + fixed))
    if len(g.vertices) == 6:
        bad = {labels['00']: Q(1, 2), labels['11']: Q(1, 2)}
        expected = {labels['01']: Q(1, 2), labels['10']: Q(1, 2)}
    else:
        diagonal = ('d0', 'd1', 'd2', 'd3')
        bad = {labels['01']: Q(1, 3), labels['10']: Q(1, 3), diagonal: Q(1, 3)}
        expected = {labels['00']: Q(1, 3), labels['11']: Q(1, 3), diagonal: Q(1, 3)}
    assert not g.true_simplex(bad)
    assert g.decode(full, g.flow(bad)) == expected
    assert g.true_simplex(expected)
    COUNTS['explicit_noncyclic_geometric_simplices'] += 1
    return {'name': g.name, 'weights': g.weights, 'actual_tori': len(g.vertices),
            'retained_cone_orders': [q for q, _ in g.cones], 'edges': len(full),
            'connected_regions': len(full_faces), 'matchings': all_matchings,
            'block_width_matrix': [[g.block_width(a, b) for b in all_matchings] for a in all_matchings],
            'parallel_class_separation': g.parallel_feature_check(),
            'simultaneous_allocation': g.allocated_copies(),
            'feasible_deleted_edge_supports': feasible, 'rational_barycentric_inputs': sample_count,
            'noncyclic_input': {'+'.join(m): str(c) for m, c in bad.items()},
            'retracted_output': {'+'.join(m): str(c) for m, c in expected.items()}}


def negative_controls():
    g = models()[0]
    vertices, edges = dict(g.vertices), dict(g.edges)
    vertices[5], vertices[6] = (pt(Q(-1, 2), 3), 1), (pt(Q(1, 2), 3), -1)
    edges['c'] = (6, 5, (vertices[6][0], vertices[5][0]))
    bad = Model('deliberately_isotopic_outer_arcs', g.weights, vertices, edges,
                g.cones, g.parallel_pairs)
    rejected = False
    try:
        bad.parallel_feature_check()
    except AssertionError:
        rejected = True
    assert rejected
    slopes = []
    for h in models():
        p, q = h.weights
        signs = {v: sign for v, (_, sign) in h.vertices.items()}
        linking_sums = {i: sum(p * q * signs[i] * signs[j] for j in signs if j != i)
                        for i in signs}
        assert set(linking_sums.values()) == {-p * q}
        assert all(s + p * q == 0 for s in linking_sums.values())
        assert any(s != 0 for s in linking_sums.values())
        slopes.append({'link': h.name, 'total_link_meridian_coefficient': p * q,
                       'preferred_longitudes_fail_total_boundary_homology': True})
    return {'empty_side_parallel_pair_rejected': rejected, 'boundary_slope_checks': slopes}


def main():
    here = Path(__file__).resolve().parent
    root = here.parent
    sources = sorted((root/'proof').glob('*.md'))
    before = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sources}
    controls = negative_controls()
    COUNTS.clear()
    result = {'status': 'PASS', 'arithmetic': 'fractions.Fraction',
              'negative_controls': controls,
              'models': [verify(g) for g in models()], 'counts': dict(COUNTS)}
    after = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
             for p in sources}
    assert before == after
    result['input_sha256'] = after
    result['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['limitations'] = ['The PL copies certify these explicit finite arc families only.',
                             'Class widths invoke the established Seifert class-distance theorem.',
                             'No algorithm here proves the finite-system verticalisation lemma.',
                             'No output file is written.']
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
