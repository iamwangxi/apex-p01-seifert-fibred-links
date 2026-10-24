#!/usr/bin/env python3
"""Bounded exact diagnostics of the splice comparison's new trace condition and restricted carrier.

No import or execution of earlier checkers. No directory traversal. The only
output is deterministic JSON on stdout. This is not a 3D normalisation test.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
COUNTS = {}


def count(key, n=1):
    COUNTS[key] = COUNTS.get(key, 0) + n


def osc(values):
    return max(values) - min(values)


def cumulative(row):
    result = [0]
    for x in row:
        result.append(result[-1] + x)
    return result


def sector_criterion(rows):
    heights = list(map(cumulative, rows))
    return all(osc([a - b for a, b in zip(heights[i], heights[j])]) <= 1
               for i, j in combinations(range(len(rows)), 2))


def repeated_word_search(rows):
    """Independent brute force over cyclic colour orders, not a chain sort."""
    r, q = len(rows), sum(rows[0])
    columns = list(zip(*rows))
    for order in permutations(range(r)):
        word, position = order * q, 0
        for column in columns:
            labels = {i for i, bit in enumerate(column) if bit}
            part = word[position:position + len(labels)]
            if set(part) != labels:
                break
            position += len(labels)
        else:
            assert position == r * q
            return True
    return False


def word_checks():
    profiles = []
    for bundles in range(2, 6):
        for q in range(1, min(3, bundles - 1) + 1):
            rows = [tuple(int(i in selected) for i in range(bundles))
                    for selected in combinations(range(bundles), q)]
            for r in (2, 3, 4):
                accepted = rejected = 0
                for matrix in product(rows, repeat=r):
                    a, b = sector_criterion(matrix), repeated_word_search(matrix)
                    assert a == b, matrix
                    accepted += a
                    rejected += not a
                    count('independent_word_vs_sector_matrices')
                profiles.append({'bundles': bundles, 'q': q, 'labels': r,
                                 'accepted': accepted, 'rejected': rejected})
    # Explicit repeated pattern ties and q=2 obstruction.
    obstruction = ((1, 0, 0, 1), (0, 1, 1, 0))
    assert not sector_criterion(obstruction)
    assert not repeated_word_search(obstruction)
    return profiles


def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, length - 1):
            yield (first,) + rest


class Support:
    """Planar four-cycle petals at J, plus disjoint ordinary four-cycles.

    Every petal has two positive actual ends and one negative actual end.
    A petal uses two J edges as alternatives, contributing one J demand.
    Only petal faces, and outside 0, are read at J. An ordinary cycle face is
    not incident to J. Left/right tables follow the oriented square drawing.
    """
    def __init__(self, q, ordinary=1):
        self.q, self.ordinary, self.dimension = q, ordinary, q + ordinary
        self.name = f'coherent_q{q}_ordinary{ordinary}'
        self.edges = []  # negative, positive, left, right
        self.demands = {'J': q} if q else {}
        for i in range(self.dimension):
            a, b = f'p{i}a', f'p{i}b'
            if i < q:
                u, v = 'J', f'n{i}'
            else:
                u, v = f'n{i}a', f'n{i}b'
                self.demands[u] = 1
            self.demands[v] = self.demands[a] = self.demands[b] = 1
            f = i + 1
            self.edges.extend(((u, a, f, 0), (u, b, 0, f),
                               (v, a, 0, f), (v, b, f, 0)))
        self.faces = tuple(range(self.dimension + 1))
        self.states = tuple(product((0, 1), repeat=self.dimension))
        self.index = {s: i for i, s in enumerate(self.states)}
        self.vectors = tuple(tuple(x for b in s for x in (b, 1-b, 1-b, b))
                             for s in self.states)
        for vector in self.vectors:
            self.legal(vector)
        self.all_edges = frozenset(range(len(self.edges)))

    def legal(self, vector):
        assert all(bit in (0, 1) for bit in vector)
        for v, demand in self.demands.items():
            assert sum(vector[e] for e, (a, b, _, _) in enumerate(self.edges)
                       if v in (a, b)) == demand

    def flow(self, bary):
        return tuple(sum((mass * self.vectors[i][e] for i, mass in bary.items()), F(0))
                     for e in range(len(self.edges)))

    def potential(self, flow, reference, support=None, root=0):
        support = self.all_edges if support is None else support
        parent = list(self.faces)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        ref = self.vectors[reference]
        for e in self.all_edges - support:
            assert flow[e] == 0 and ref[e] == 0
            _, _, l, r = self.edges[e]
            l, r = find(l), find(r)
            parent[max(l, r)] = min(l, r)
        merge = {f: find(f) for f in self.faces}
        adjacent = {f: [] for f in set(merge.values())}
        for e in support:
            _, _, l, r = self.edges[e]
            l, r = merge[l], merge[r]
            difference = flow[e] - ref[e]
            adjacent[r].append((l, difference))
            adjacent[l].append((r, -difference))
        root = merge[root]
        values, queue = {root: F(0)}, [root]
        for f in queue:
            for g, d in adjacent[f]:
                target = values[f] + d
                if g in values:
                    assert values[g] == target
                else:
                    values[g] = target
                    queue.append(g)
        assert set(values) == set(adjacent)
        return {f: values[merge[f]] for f in self.faces}

    def decode(self, flow, reference=0, support=None, root=0):
        u = self.potential(flow, reference, support, root)
        cuts = sorted({F(0), F(1)} | {(-v) % 1 for v in u.values()})
        result = {}
        for a, b in zip(cuts, cuts[1:]):
            t = (a + b) / 2
            floor = {f: (v+t).numerator // (v+t).denominator for f, v in u.items()}
            vector = tuple(self.vectors[reference][e] + floor[l] - floor[r]
                           for e, (_, _, l, r) in enumerate(self.edges))
            self.legal(vector)
            bits = tuple(vector[4*i] for i in range(self.dimension))
            i = self.index[bits]
            assert vector == self.vectors[i]
            assert all(flow[e] > 0 for e, bit in enumerate(vector) if bit)
            result[i] = result.get(i, F(0)) + b - a
            count('threshold_intervals')
        assert sum(result.values()) == 1
        assert self.flow(result) == tuple(flow)
        assert self.cyclic(result)
        count('decoder_calls')
        return result

    def cyclic(self, bary):
        for i, j in combinations(bary, 2):
            d = [0] + [a-b for a, b in zip(self.states[i], self.states[j])]
            if osc(d) > 1:
                return False
        return True

    def geometric(self, bary):
        if not self.q:
            return True
        for i, j in combinations(bary, 2):
            d = [0] + [a-b for a, b in zip(self.states[i][:self.q],
                                         self.states[j][:self.q])]
            if osc(d) > 1:
                return False
        return True

    def port_law(self, bary):
        result = {}
        for i, mass in bary.items():
            ports = self.states[i][:self.q]
            result[ports] = result.get(ports, F(0)) + mass
        return result

    def realise_word(self, ids):
        if not self.q:
            return
        ids = sorted(ids, key=lambda i: (self.states[i][:self.q], i), reverse=True)
        word = []
        for petal in range(self.q):
            for chosen in (1, 0):
                word.extend(i for i in ids if self.states[i][petal] == chosen)
        assert word == ids * self.q
        count('explicit_whole_family_trace_words')

    def maximal_cyclic_simplices(self):
        for order in permutations(range(self.dimension)):
            s, ids = [0] * self.dimension, [self.index[(0,) * self.dimension]]
            for k in order:
                s[k] = 1
                ids.append(self.index[tuple(s)])
            yield tuple(ids)

    def maximal_geometric_simplices(self):
        if not self.q:
            yield tuple(range(len(self.states)))
            return
        for order in permutations(range(self.q)):
            s, ports = [0] * self.q, [(0,) * self.q]
            for k in order:
                s[k] = 1
                ports.append(tuple(s))
            yield tuple(i for i, state in enumerate(self.states)
                        if state[:self.q] in ports)


def verify_support(g, denominator):
    accepted = rejected = 0
    for serial, coefficients in enumerate(compositions(denominator, len(g.states))):
        bary = {i: F(a, denominator) for i, a in enumerate(coefficients) if a}
        if not g.geometric(bary):
            rejected += 1
            continue
        accepted += 1
        flow = g.flow(bary)
        output = g.decode(flow)
        assert g.port_law(output) == g.port_law(bary)
        assert g.geometric(set(bary) | set(output))
        g.realise_word(set(bary) | set(output))
        count('trace_law_preservation')
        if g.cyclic(bary):
            assert output == bary
            count('exact_X_recovery')
        positive = frozenset(e for e, w in enumerate(flow) if w)
        refs = [i for i, vector in enumerate(g.vectors)
                if all(not bit or e in positive for e, bit in enumerate(vector))]
        assert refs
        assert g.decode(flow, refs[-1], positive) == output
        count('zero_support_comparisons')
        if serial % 11 == 0:
            for ref in {0, len(g.states)//2, len(g.states)-1}:
                assert g.decode(flow, ref) == output
                count('reference_comparisons')
            for root in g.faces:
                assert g.decode(flow, root=root) == output
                count('root_comparisons')
        for t in (F(0), F(1, 3), F(1, 2), F(1)):
            point = {}
            for i in set(bary) | set(output):
                c = (1-t) * bary.get(i, F(0)) + t * output.get(i, F(0))
                if c:
                    point[i] = c
            assert sum(point.values()) == 1
            assert g.flow(point) == flow
            assert g.geometric(point)
            assert g.decode(g.flow(point)) == output
            if t == 0:
                assert point == bary
            if t == 1:
                assert point == output
            if g.cyclic(bary):
                assert point == bary
            count('strong_homotopy_parameter_checks')
    x_simplices = list(g.maximal_cyclic_simplices())
    y_carriers = list(g.maximal_geometric_simplices())
    for simplex in x_simplices:
        for weights in ([1] * len(simplex), list(range(1, len(simplex)+1))):
            bary = {i: F(a, sum(weights)) for i, a in zip(simplex, weights)}
            assert g.decode(g.flow(bary)) == bary
            count('maximal_X_simplex_recovery')
    for carrier in y_carriers:
        assert g.geometric(carrier)
        g.realise_word(carrier)
        for weights in ([1] * len(carrier), list(range(1, len(carrier)+1))):
            bary = {i: F(a, sum(weights)) for i, a in zip(carrier, weights)}
            decoded = g.decode(g.flow(bary))
            assert set(decoded) <= set(carrier)
            assert g.port_law(decoded) == g.port_law(bary)
            count('maximal_Y_carrier_preservation')
    return {'name': g.name, 'q': g.q, 'actual_ends': sum(v != 'J' for v in g.demands),
            'edges': len(g.edges), 'regions': len(g.faces),
            'matchings': len(g.states), 'denominator': denominator,
            'geometric_rational_inputs': accepted,
            'invalid_geometric_inputs_rejected': rejected,
            'maximal_X_simplices': len(x_simplices),
            'maximal_Y_carriers': len(y_carriers),
            'maximal_Y_vertices': max(map(len, y_carriers))}


def negative_controls():
    g = Support(2, 0)
    a, b = g.index[(1, 0)], g.index[(0, 1)]
    assert not g.geometric((a, b))
    assert not g.cyclic((a, b))
    h = Support(2, 1)
    c, d = h.index[(1, 1, 0)], h.index[(0, 0, 1)]
    bary = {c: F(1, 2), d: F(1, 2)}
    assert h.geometric(bary) and not h.cyclic(bary)
    decoded = h.decode(h.flow(bary))
    assert h.port_law(decoded) == h.port_law(bary)
    pair = Support(0, 2)
    x = {pair.index[(1, 0)]: F(1, 2), pair.index[(0, 1)]: F(1, 2)}
    good = {pair.index[(0, 0)]: F(1, 2), pair.index[(1, 1)]: F(1, 2)}
    assert pair.geometric(x) and not pair.cyclic(x)
    assert pair.decode(pair.flow(x)) == good
    return {'nonempty_trace_unrestricted_carrier': 'AABB rejected for q=2',
            'genuine_extra_geometric_edge': '110--001: J width 1, full width 2',
            'double_zero_common_threshold': '(10+01)/2 maps to (00+11)/2'}


def nested_root_checks():
    """A theta graph nested in an ordinary cycle: the outside misses J.

    Regions O,L,U,D. The three theta matchings have J-root potentials
    (L,U,D)=(0,0,0),(0,0,1),(0,1,1). Adding the outer cycle shifts all
    three by its bit z; O stays zero. This tests the necessary change of root.
    """
    edges = [('a', 'c', 1, 0), ('a', 'd', 0, 1),
             ('b', 'c', 0, 1), ('b', 'd', 1, 0),
             ('J', 'p1', 1, 2), ('J', 'p2', 2, 3), ('J', 'p3', 3, 1),
             ('N', 'p1', 2, 1), ('N', 'p2', 3, 2), ('N', 'p3', 1, 3)]
    demands = {v: 1 for v in ('a', 'b', 'c', 'd', 'N', 'p1', 'p2', 'p3')}
    demands['J'] = 2
    states = tuple((z, a, b) for z in (0, 1) for a, b in ((0, 0), (0, 1), (1, 1)))
    potentials = [(F(0), F(z), F(z+a), F(z+b)) for z, a, b in states]
    ref = (0, 1, 1, 0, 1, 1, 0, 0, 0, 1)
    vectors = [tuple(ref[e] + u[l] - u[r]
                     for e, (_, _, l, r) in enumerate(edges)) for u in potentials]
    for vector in vectors:
        assert all(x in (0, 1) for x in vector)
        for v, demand in demands.items():
            assert sum(vector[e] for e, (a, b, _, _) in enumerate(edges)
                       if v in (a, b)) == demand
    ids = {tuple(v): i for i, v in enumerate(vectors)}

    def flow(bary):
        return tuple(sum((mass*vectors[i][e] for i, mass in bary.items()), F(0))
                     for e in range(len(edges)))

    def decode(bary, root, reference=0):
        mean = [sum((mass*potentials[i][f] for i, mass in bary.items()), F(0))
                for f in range(4)]
        u = [mean[f] - potentials[reference][f] for f in range(4)]
        shift = u[root]
        u = [a-shift for a in u]
        cuts = sorted({F(0), F(1)} | {(-a) % 1 for a in u})
        result = {}
        for lo, hi in zip(cuts, cuts[1:]):
            t = (lo+hi)/2
            q = [(a+t).numerator // (a+t).denominator for a in u]
            vector = tuple(vectors[reference][e] + q[l]-q[r]
                           for e, (_, _, l, r) in enumerate(edges))
            assert vector in ids
            i = ids[vector]
            result[i] = result.get(i, F(0)) + hi-lo
        assert flow(result) == flow(bary)
        for i, j in combinations(result, 2):
            assert osc([a-b for a, b in zip(potentials[i], potentials[j])]) <= 1
        count('nested_decoder_calls')
        return result

    def law(bary):
        result = {}
        for i, mass in bary.items():
            p = states[i][1:]
            result[p] = result.get(p, F(0)) + mass
        return result

    # All six vertices are geometric, including full-width-two pairs.
    assert osc([a-b for a, b in zip(potentials[0], potentials[-1])]) == 2
    assert osc([potentials[-1][f] - potentials[0][f] for f in (1, 2, 3)]) == 1
    for coefficients in compositions(5, len(states)):
        bary = {i: F(a, 5) for i, a in enumerate(coefficients) if a}
        decoded = decode(bary, root=1)
        assert decode(bary, root=0) == decoded
        for reference in range(len(states)):
            assert decode(bary, root=1, reference=reference) == decoded
            count('nested_reference_comparisons')
        assert law(bary) == law(decoded)
        count('nested_trace_law_preservation')
        for t in (F(0), F(1, 2), F(1)):
            point = {i: (1-t)*bary.get(i, F(0)) + t*decoded.get(i, F(0))
                     for i in set(bary) | set(decoded)}
            point = {i: c for i, c in point.items() if c}
            assert flow(point) == flow(bary)
            assert decode(point, root=1) == decoded
            count('nested_homotopy_checks')
        count('nested_rational_inputs')
    return {'q': 2, 'actual_ends': 8, 'matchings': 6,
            'regions': ['O', 'L', 'U', 'D'],
            'J_sectors_use': ['L', 'U', 'D'], 'J_root': 'L',
            'outside_O_meets_J': False, 'denominator': 5,
            'geometric_carrier': 'one six-vertex simplex',
            'cyclic_polytope': 'triangular prism'}


def main():
    word_profiles = word_checks()
    profiles = [verify_support(Support(0, 2), 6),
                verify_support(Support(2, 1), 6),
                verify_support(Support(3, 1), 4),
                verify_support(Support(4, 1), 2)]
    negatives = negative_controls()
    nested = nested_root_checks()
    root = HERE.parent
    sources = sorted((root/'proof').glob('*.md'))
    source_hashes = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in sources}
    result = {'status': 'PASS', 'arithmetic': 'fractions.Fraction; no floating-point tolerance',
              'counts': COUNTS, 'word_profiles': word_profiles,
              'supports': profiles, 'negative_controls': negatives,
              'nested_root_case': nested,
              'source_sha256': source_hashes,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'limits': ['Finite diagnostics do not prove 3D simultaneous normalisation.',
                         'Known cyclic metric/isotopy inputs are not independently re-proved.',
                         'Repository-local sources only; stdout JSON; no file writes.']}
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
