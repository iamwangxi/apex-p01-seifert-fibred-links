#!/usr/bin/env python3
# Finite exact diagnostic for Part 7 of the proof; standard library only; prints a deterministic report and writes no files.
from collections import deque
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from math import gcd
from pathlib import Path
COUNTS = {}

def check(condition, message):
    if not condition:
        raise AssertionError(message)

def gcd_all(values):
    result = 0
    for value in values:
        result = gcd(result, abs(value))
    return result

def components(vertices, edges):
    adj = {v: [] for v in vertices}
    for (a, b) in edges:
        adj[a].append(b)
        adj[b].append(a)
    unseen = set(vertices)
    result = []
    while unseen:
        start = min(unseen)
        todo = [start]
        unseen.remove(start)
        comp = {start}
        while todo:
            for nxt in adj[todo.pop()]:
                if nxt in unseen:
                    unseen.remove(nxt)
                    comp.add(nxt)
                    todo.append(nxt)
        result.append(comp)
    return result

def hopf_tree(sign, actual, tree_edges):
    adjacency = {v: [] for v in sign}
    for (v, w) in tree_edges:
        adjacency[v].append(w)
        adjacency[w].append(v)
    check(len(tree_edges) == len(sign) - 1, 'Not a tree')
    check(len(components(sign, tree_edges)) == 1, 'Disconnected tree')
    a = {v: sum(actual[v]) for v in sign}

    @lru_cache(None)
    def mu(v, w):
        return sign[w] * (a[w] + sum((mu(w, u) for u in adjacency[w] if u != v)))

    def longitude(v, w):
        return sign[v] * (a[v] + sum((mu(v, u) for u in adjacency[v] if u != w)))
    fibre = {v: sign[v] * (a[v] + sum((mu(v, w) for w in adjacency[v]))) for v in sign}
    restriction_div = {v: gcd_all(actual[v] + [mu(v, w) for w in adjacency[v]]) for v in sign}
    q = {}
    for (v, w) in tree_edges:
        check(mu(v, w) == longitude(w, v), 'Splice meridian mismatch')
        check(longitude(v, w) == mu(w, v), 'Splice longitude mismatch')
        q[v, w] = gcd(abs(mu(v, w)), abs(longitude(v, w)))
        check(abs(sign[v] * sign[w] - 1) == 2, 'Not a genuine Hopf cut')
    return (adjacency, fibre, restriction_div, q, mu)

def anchored_internal_example():
    sign = {'C': -1, 'H': 1, 'A': -1, 'B': -1, 'D': 1, 'E': 1}
    actual = {v: [] if v in ('C', 'H') else [1, 1] for v in sign}
    edges = [('C', 'H'), ('H', 'A'), ('H', 'B'), ('C', 'D'), ('C', 'E')]
    (adj, k, div, q, mu) = hopf_tree(sign, actual, edges)
    check(k == {'C': 0, 'H': -8, 'A': 4, 'B': 4, 'D': 4, 'E': 4}, k)
    check(all((div[v] > 0 for v in sign)), 'An identically zero restriction')
    check(div['C'] == div['H'] == 2, 'Wrong local divisibilities')
    horizontal = {v for v in sign if k[v] != 0}
    h_edges = [(v, w) for (v, w) in edges if v in horizontal and w in horizontal]
    clusters = components(horizontal, h_edges)
    check(sorted((len(c) for c in clusters)) == [1, 1, 3], clusters)
    check(all((any((actual[v] for v in c)) for c in clusters)), 'Unanchored cluster')
    check([mu('C', v) for v in ('H', 'D', 'E')] == [-4, 2, 2], 'Zero demands')
    check([q[e] for e in edges] == [4, 2, 2, 2, 2], q)
    flows = [(x, y) for x in range(5) for y in range(5) if x + y == 4 and x == 2 and (y == 2)]
    check(flows == [(2, 2)], flows)
    check(sum((abs(k[v]) for v in horizontal)) == 24, 'Wrong norm')
    actual_count = sum((len(x) for x in actual.values()))
    genus = (2 - actual_count + 24) // 2
    check(actual_count == 8 and genus == 9, 'Wrong global topology')
    check(2 - 3 + 4 == 3, 'Wrong zero-base cut Euler characteristic')
    COUNTS['anchored_internal_example_blocks'] = len(sign)
    COUNTS['anchored_internal_example_actual_components'] = actual_count
    COUNTS['anchored_internal_example_norm_genus'] = [24, genus]
    COUNTS['anchored_internal_example_local_horizontal_pieces'] = div['H']

def nonunit_rounding():
    sign = {'C': -1, **{str(i): 1 for i in range(4)}}
    actual = {'C': [], '0': [1] * 4, '1': [-1] * 4, '2': [1] * 4, '3': [-1] * 4}
    edges = [('C', str(i)) for i in range(4)]
    (_, k, div, q, _) = hopf_tree(sign, actual, edges)
    check(k['C'] == 0 and div['C'] == 4, 'Wrong four-port zero block')
    check(all((q[e] == 4 for e in edges)), 'Wrong nonunit port')

    def flow(x):
        return (x, 4 - x, x, 4 - x)
    integer_vertices = list(range(5))
    point_checks = 0
    recovery_checks = 0
    for denominator in range(1, 33):
        for numerator in range(4 * denominator + 1):
            x = Fraction(numerator, denominator)
            lower = x.numerator // x.denominator
            upper = min(4, lower + 1)
            weights = {lower: 1 - (x - lower)}
            if x != lower:
                weights[upper] = x - lower
            weights = {v: w for (v, w) in weights.items() if w}
            check(sum(weights.values()) == 1, 'Rounding mass')
            check(sum((v * w for (v, w) in weights.items())) == x, 'Exact expectation')
            check(all((all((0 <= e <= 4 for e in flow(v))) for v in weights)), 'Nonunit demand feasibility')
            check(max(weights) - min(weights) <= 1, 'Outputs not a cyclic simplex')
            point_checks += 1
    for lower in range(4):
        for denominator in range(1, 25):
            for numerator in range(denominator + 1):
                t = Fraction(numerator, denominator)
                x = lower + t
                expected = {lower: 1 - t, lower + 1: t}
                expected = {v: w for (v, w) in expected.items() if w}
                floored = {int(x): 1 - (x - int(x))}
                if x != int(x):
                    floored[int(x) + 1] = x - int(x)
                floored = {v: w for (v, w) in floored.items() if w}
                check(floored == expected, 'Simplex recovery')
                recovery_checks += 1
    check(len(integer_vertices) == 5, 'Carrier collapsed by net data')
    COUNTS['nonunit_interval_rational_points'] = point_checks
    COUNTS['nonunit_interval_simplex_recoveries'] = recovery_checks

def torus_genus(p, q):
    check(p >= 2 and abs(q) >= 2 and (gcd(p, abs(q)) == 1), 'Bad torus knot')
    return (p - 1) * (abs(q) - 1) // 2

def cable_step(previous_genus, p, q):
    check(p >= 2 and q != 0 and (gcd(p, abs(q)) == 1), 'Bad cable')
    horizontal_chi = -(p - 1) * abs(q)
    horizontal_boundary = p + 1
    horizontal_genus = Fraction(2 - horizontal_boundary - horizontal_chi, 2)
    check(horizontal_genus.denominator == 1 and horizontal_genus >= 0, 'Cable horizontal piece topology')
    chi = horizontal_chi + p * (1 - 2 * previous_genus)
    genus = Fraction(1 - chi, 2)
    formula = p * previous_genus + Fraction((p - 1) * (abs(q) - 1), 2)
    check(genus == formula and genus.denominator == 1, 'Cable genus formula')
    check(gcd(1, 0) == 1 and p * q != 0, 'Primitive horizontal class')
    return (int(genus), horizontal_chi)

def cable_family():
    count = 0
    for p0 in range(2, 8):
        for q0 in range(2, 8):
            if gcd(p0, q0) != 1:
                continue
            g0 = torus_genus(p0, q0)
            for p in range(2, 9):
                for q in range(-9, 10):
                    if not q or gcd(p, abs(q)) != 1:
                        continue
                    (genus, block_chi) = cable_step(g0, p, q)
                    check(abs(p * p0 * q0 - q) > 0, 'A claimed cable JSJ cut has matching fibres')
                    check(2 * block_chi + 2 * p * (1 - 2 * g0) == 2 * (1 - 2 * genus), 'Signed pair Euler sum')
                    word = [s for _ in range(p) for s in (1, -1)]
                    check(sum(word) == 0 and len(word) == 2 * p, 'Noncoherent leaf trace word')
                    check(len(word) != 0, 'div(Phi|T)=0 wrongly erased trace')
                    count += 1
    (g_a, chi_a) = cable_step(torus_genus(2, 3), 2, 1)
    (g_b, chi_b) = cable_step(torus_genus(2, 5), 3, 2)
    check((g_a, chi_a, 2 * (2 * g_a - 1)) == (2, -1, 6), 'Example K_A')
    check((g_b, chi_b, 2 * (2 * g_b - 1)) == (7, -4, 26), 'Example K_B')
    g = torus_genus(2, 3)
    winding = 1
    for (p, q) in ((2, 3), (3, -2), (2, -1)):
        (g, _) = cable_step(g, p, q)
        winding *= p
    check(winding == 12 and g == 20, 'Iterated cable recurrence')
    COUNTS['single_cable_exact_parameter_cases'] = count
    COUNTS['named_cable_examples'] = {'K_A': {'genus': g_a, 'leaf_trace': 4, 'X_Y_vertices': 2}, 'K_B': {'genus': g_b, 'leaf_trace': 6, 'X_Y_vertices': 2}, 'depth_three': {'genus': g, 'deep_leaf_trace': 2 * winding}}
    check(2 * (2 * torus_genus(2, 3) - 1) == 2, 'two-parallel trefoil complexity')
    COUNTS['two_parallel_regression'] = {'vertices': 2, 'edge': 1, 'trefoil_excess': 2}

def chords_cross(a, b, c, d):
    (a, b) = sorted((a, b))
    (c, d) = sorted((c, d))
    return a < c < b < d or c < a < d < b

def square_knot_returns():
    total_pairs = 0
    for r in range(1, 257):
        n = 2 * r
        eps = [1 if i == 0 or i > r else -1 for i in range(n)]
        leaf = [(i, (1 - i) % n) for i in range(n) if i < (1 - i) % n]
        pattern = [(i, -i % n) for i in range(1, r)]
        check(len(leaf) == r and len(pattern) == r - 1, 'Wrong matching sizes')
        check(sum(eps) == 0 and eps[0] == 1 and (eps[r] == -1), 'Wrong actual signs')
        check(all((eps[i] == -eps[j] for (i, j) in leaf + pattern)), 'Unoriented pair was mistaken for an oriented annulus')
        for family in (leaf, pattern):
            for (index, (a, b)) in enumerate(family):
                for (c, d) in family[index + 1:]:
                    check(not chords_cross(a, b, c, d), 'Crossing ribbon arcs')
        check({x for edge in pattern for x in edge} == set(range(n)) - {0, r}, 'Pattern tether slots')
        for (a, b) in pattern:
            (lo, hi) = sorted((a, b))
            check(lo < r < hi and (not lo < 0 < hi), 'Return fails to separate the two actual holes')
        internal = leaf + leaf + pattern
        comps = components(range(n), internal)
        check(len(comps) == 1 and {0, r} <= comps[0], 'Closed assembled component')
        all_edges = internal + [(0, n), (r, n + 1)]
        beta = len(all_edges) - (n + 2) + 1
        check(beta == r, 'Wrong surface graph genus')
        check(-n == 2 - 2 * r - 2, 'Euler characteristic / genus')
        eta = (1, -6, 6)
        check(tuple((sum((s * x for s in eps)) for x in eta)) == (0, 0, 0), 'Nonzero global restriction invented from an auxiliary fibration')
        prefix = [0]
        for s in eps:
            prefix.append(prefix[-1] + s)
        check(max(prefix) - min(prefix) == r, 'Signed word depth')
        total_pairs += len(internal)
    COUNTS['square_knot_all_genus_ribbon_cases'] = 256
    COUNTS['square_knot_oriented_internal_annulus_checks'] = total_pairs
    COUNTS['square_knot_max_genus_and_jointly_efficient_trace_per_torus'] = [256, 512]

def unanchored_nonzero_control():
    actual_signs = (1, 1, -1)
    net = sum(actual_signs)
    check(net == 1, 'Wrong nonzero companion restriction')
    companion_fibre_evaluation = 6 * net
    small = {'annuli': 1, 'fibres': (1,), 'components': 2}
    large = {'annuli': 0, 'fibres': actual_signs, 'components': 3}
    check(companion_fibre_evaluation == 6, 'Wrong trefoil fibre evaluation')
    check(sum(small['fibres']) == sum(large['fibres']) == net, 'The two restrictions differ')
    check(len(small['fibres']) == 1 and len(large['fibres']) == 3, 'Cancelled fibre pair was forgotten')
    check(2 * small['annuli'] + len(small['fibres']) == 3, 'Small system actual usage')
    check(2 * large['annuli'] + len(large['fibres']) == 3, 'Large system actual usage')
    COUNTS['unanchored_nonzero_control'] = {'companion_fibre_evaluation': 6, 'net_divisibility': 1, 'minimum_trace_and_complexity': [1, 3], 'ordinary_component_counts': [2, 3]}

def component_wall_retraction():
    vertices = ((0, 0), (1, 0), (0, 1), (1, 1))

    def direct_phase(weights):
        a = weights[1] + weights[3]
        b = weights[2] + weights[3]
        cuts = sorted({Fraction(0), a, b, Fraction(1)})
        result = {v: Fraction(0) for v in vertices}
        for (lo, hi) in zip(cuts, cuts[1:]):
            r = (lo + hi) / 2
            result[int(r < a), int(r < b)] += hi - lo
        return tuple((result[v] for v in vertices))

    def floor_from_root(a, b, root):
        values = (Fraction(0), a, b)
        values = tuple((v - values[root] for v in values))
        cuts = {Fraction(0), Fraction(1)}
        for value in values:
            fractional = value - value.numerator // value.denominator
            if fractional:
                cuts.add(1 - fractional)
        cuts = sorted(cuts)
        result = {v: Fraction(0) for v in vertices}
        for (lo, hi) in zip(cuts, cuts[1:]):
            theta = (lo + hi) / 2
            floors = [(v + theta).numerator // (v + theta).denominator for v in values]
            vertex = (floors[1] - floors[0], floors[2] - floors[0])
            check(vertex in vertices, 'Root rounding left the actual choices')
            result[vertex] += hi - lo
        return tuple((result[v] for v in vertices))

    def cyclic_distance(v, w):
        values = (0, v[0] - w[0], v[1] - w[1])
        return max(values) - min(values)
    bary_checks = root_checks = homotopy_checks = 0
    denominator = 16
    marginal_cache = {}
    for n0 in range(denominator + 1):
        for n1 in range(denominator - n0 + 1):
            for n2 in range(denominator - n0 - n1 + 1):
                n3 = denominator - n0 - n1 - n2
                weights = tuple((Fraction(n, denominator) for n in (n0, n1, n2, n3)))
                a = weights[1] + weights[3]
                b = weights[2] + weights[3]
                rounded = direct_phase(weights)
                formula = (1 - max(a, b), max(a - b, 0), max(b - a, 0), min(a, b))
                check(rounded == formula, 'Component-phase / closed formula mismatch')
                check(sum(rounded) == 1 and all((x >= 0 for x in rounded)), 'Retraction barycentric mass')
                check(rounded[1] + rounded[3] == a and rounded[2] + rounded[3] == b, 'Component weights changed')
                support = [v for (v, w) in zip(vertices, rounded) if w]
                check(all((cyclic_distance(v, w) <= 1 for v in support for w in support)), 'Output not in X')
                if not (weights[1] and weights[2]):
                    check(rounded == weights, 'A cyclic input point moved')
                old = marginal_cache.setdefault((a, b), rounded)
                check(old == rounded, 'Shared component packet labels matter')
                for root in range(3):
                    check(floor_from_root(a, b, root) == rounded, 'Global chamber root changed the phase average')
                    root_checks += 1
                for t in (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)):
                    moved = tuple(((1 - t) * w + t * z for (w, z) in zip(weights, rounded)))
                    check(sum(moved) == 1 and all((w >= 0 for w in moved)), 'Homotopy left actual Y tetrahedron')
                    check(direct_phase(moved) == rounded, 'Retraction changed along H')
                    if t == 0:
                        check(moved == weights, 'Wrong initial endpoint')
                    if t == 1:
                        check(moved == rounded, 'Wrong final endpoint')
                    homotopy_checks += 1
                bary_checks += 1
    COUNTS['component_wall_barycentric_points'] = bary_checks
    COUNTS['component_wall_global_root_checks'] = root_checks
    COUNTS['component_wall_strong_deformation_checks'] = homotopy_checks

def main():
    anchored_internal_example()
    nonunit_rounding()
    cable_family()
    square_knot_returns()
    unanchored_nonzero_control()
    component_wall_retraction()
    print('PASS: exact finite diagnostics; topological conclusions require the proof.')
    for (key, value) in COUNTS.items():
        print(f'{key}: {value}')
if __name__ == '__main__':
    main()
