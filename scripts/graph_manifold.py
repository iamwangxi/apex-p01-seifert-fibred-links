#!/usr/bin/env python3
"""Offline standard-library diagnostic; original calculation functions retained."""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from math import ceil, floor, gcd
COUNTS = Counter()

def osc(v):
    return max(v) - min(v)

def canonical(v):
    return tuple((x - v[0] for x in v))

def decode(u, shift=Q(0), reference=None):
    if reference is None:
        reference = (0,) * len(u)
    values = tuple((x - r + shift for (x, r) in zip(u, reference)))
    breaks = {Q(0), Q(1)}
    for x in values:
        frac = x - floor(x)
        if frac:
            breaks.add(1 - frac)
    breaks = sorted(breaks)
    result = defaultdict(Q)
    for (low, high) in zip(breaks, breaks[1:]):
        theta = (low + high) / 2
        vertex = canonical(tuple((floor(x + theta) + r for (x, r) in zip(values, reference))))
        result[vertex] += high - low
    assert sum(result.values()) == 1
    return dict(result)

def flow(u, rows, ref):
    return tuple((m + u[left] - u[right] for (m, (left, right)) in zip(ref, rows)))

def bary(vertices, coefficients):
    return tuple((sum((c * v[j] for (c, v) in zip(coefficients, vertices))) for j in range(len(vertices[0]))))

def base_checks():
    for (a, b) in product(range(7), repeat=2):
        if a + b == 0:
            continue
        for a_positions in combinations(range(a + b), a):
            ap = set(a_positions)
            (h, old) = (0, [0])
            for i in range(a + b):
                h += 1 if i in ap else -1
                old.append(h)
            net = a - b
            new = list(range(net + 1)) if net >= 0 else list(range(0, net - 1, -1))
            assert min(old) <= min(new) <= max(new) <= max(old)
            COUNTS['packet_prefix_words'] += 1
    quotient = {(x + 2 - x, 1) for x in range(3)}
    assert quotient == {(2, 1)}
    COUNTS['unreduced_lens_quotient'] = 1
    for r in range(2, 13):
        a0 = 2 * (2 - r)
        ai = 2
        assert -(a0 + r * ai) == -4
        assert ai - a0 - (r - 1) * ai == 0
        assert gcd(ai, abs(a0 + (r - 1) * ai)) == 2
        n_centre = 2 if r == 2 else 2 * (r - 2)
        chi = 4 * (2 - n_centre - r)
        boundaries = n_centre + 2 * r
        genus = Q(2 - boundaries - chi, 2)
        assert genus.denominator == 1 and genus >= 0
        COUNTS['relative_rank_splice_examples'] += 1
    assert Q(2 - 4 + 8, 2) == 3
    assert Q(2 - 6 + 8, 2) == 2

def ribbon_checks():
    kinds = ((0, 1), (0, 3), (2, 1), (2, 3))
    demands = (2, 2, 1, 1)
    for multiplicity in product(range(5), repeat=4):
        edge_count = sum(multiplicity)
        if not 3 <= edge_count <= 6:
            continue
        edges = [kind for (kind, number) in zip(kinds, multiplicity) for _ in range(number)]
        incid = [[] for _ in range(4)]
        adjacent = [set() for _ in range(4)]
        for (e, (a, b)) in enumerate(edges):
            incid[a].append(2 * e)
            incid[b].append(2 * e + 1)
            adjacent[a].add(b)
            adjacent[b].add(a)
        if any((not d for d in incid)):
            continue
        (reached, todo) = ({0}, [0])
        while todo:
            for v in adjacent[todo.pop()] - reached:
                reached.add(v)
                todo.append(v)
        if len(reached) != 4:
            continue
        rotations = [[tuple(d[:1]) + p for p in permutations(d[1:])] for d in incid]
        for local in product(*rotations):
            rot = {d[i]: d[(i + 1) % len(d)] for d in local for i in range(len(d))}
            (unseen, faces) = (set(range(2 * edge_count)), [])
            while unseen:
                start = d = min(unseen)
                boundary = []
                while d in unseen:
                    unseen.remove(d)
                    boundary.append(d)
                    d = rot[d ^ 1]
                assert d == start
                faces.append(boundary)
            if 4 - edge_count + len(faces) != 2:
                continue
            COUNTS['planar_ribbon_systems'] += 1
            if min(map(len, faces)) < 4:
                continue
            COUNTS['no_empty_digon_systems'] += 1
            assert edge_count <= 4
            integral = []
            caps = [min(demands[a], demands[b]) for (a, b) in edges]
            for weights in product(*(range(c + 1) for c in caps)):
                if all((sum((weights[e] for (e, edge) in enumerate(edges) if v in edge)) == demands[v] for v in range(4))):
                    integral.append(weights)
            if not integral:
                continue
            if any((all((m[e] == 0 for m in integral)) for e in range(edge_count))):
                continue
            assert len(integral) <= 2
            COUNTS['positive_feasible_reduced_supports'] += 1

def quotient_decode(u, rows, ref):
    weights = flow(u, rows, ref)
    expected = decode(u)
    supported_reference = next(iter(expected))
    new_ref = flow(supported_reference, rows, ref)
    relative = tuple((x - y for (x, y) in zip(u, supported_reference)))
    parent = list(range(len(u)))

    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for (w, m, (left, right)) in zip(weights, new_ref, rows):
        if w == 0:
            assert m == 0 and relative[left] == relative[right]
            parent[find(left)] = find(right)
    roots = sorted({find(i) for i in range(len(u))})
    groups = {r: j for (j, r) in enumerate(roots)}
    reduced = [relative[r] for r in roots]
    result = defaultdict(Q)
    for (vertex, mass) in decode(tuple(reduced)).items():
        expanded = tuple((vertex[groups[find(i)]] + supported_reference[i] for i in range(len(u))))
        result[canonical(expanded)] += mass
    assert dict(result) == expected
    COUNTS['global_zero_face_comparisons'] += 1

def check_point(u, rows, ref, equalities=()):
    u = canonical(u)
    original = decode(u)
    assert bary(tuple(original), tuple(original.values())) == u
    for vertex in original:
        assert all((x >= 0 for x in flow(vertex, rows, ref)))
        assert all((vertex[a] == vertex[b] for (a, b) in equalities))
    for (a, b) in combinations(original, 2):
        assert osc(tuple((x - y for (x, y) in zip(a, b)))) <= 1
    for shift in (Q(0), Q(2, 7), Q(-7, 5)):
        for reference in ((0,) * len(u), tuple((i - i * i for i in range(len(u))))):
            assert decode(u, shift, reference) == original
            COUNTS['reference_and_global_root'] += 1
    if any((x == 0 for x in flow(u, rows, ref))):
        quotient_decode(u, rows, ref)
    COUNTS['potential_points'] += 1

def carrier_checks():
    square_rows = ((1, 0), (0, 1), (0, 1), (1, 0))
    square_ref = (1, 1, 1, 0)
    for n in range(17):
        check_point((Q(0), Q(n, 16)), square_rows, square_ref)
    rows = square_rows + tuple(((a + 2, b + 2) for (a, b) in square_rows))
    ref = square_ref + square_ref
    for (a, c, b) in product((Q(0), Q(1, 4), Q(1, 2), Q(1)), repeat=3):
        for level in (b - 2, b, b + 2):
            check_point((Q(0), a, level, level + c), rows, ref)
    for (a, c) in product((Q(0), Q(1, 4), Q(1, 2), Q(1)), repeat=2):
        check_point((Q(0), a, Q(0), c), rows, ref, ((0, 2),))
    vertices = tuple(((0, a, level, level + c) for (a, c, level) in product((0, 1), (0, 1), (-1, 0, 1))))
    for size in range(1, 5):
        for clique in combinations(vertices, size):
            if any((osc(tuple((x - y for (x, y) in zip(a, b)))) > 1 for (a, b) in combinations(clique, 2))):
                continue
            coeff = tuple((Q(i + 1, size * (size + 1) // 2) for i in range(size)))
            point = bary(clique, coeff)
            assert decode(point) == dict(zip(clique, coeff))
            COUNTS['global_true_simplex_recovery'] += 1
    for dimension in (1, 2, 3):
        for coordinates in product((Q(-3, 2), Q(-1, 3), Q(0), Q(1, 2), Q(5, 3)), repeat=dimension):
            check_point((Q(0),) + coordinates, (), ())
            COUNTS['pure_relative_level_points'] += 1
    theta_rows = ((0, 1), (1, 2), (2, 0), (1, 0), (2, 1), (0, 2))
    theta_ref = (1,) * 6
    theta_vertices = tuple(((0, 1 - a[0], a[2] - 1) for a in product(range(3), repeat=3) if sum(a) == 3))
    assert len(theta_vertices) == 7
    theta_points = set(theta_vertices)
    for pair in combinations(theta_vertices, 2):
        for t in (Q(1, 4), Q(1, 2), Q(3, 4)):
            theta_points.add(bary(pair, (t, 1 - t)))
    for triple in combinations(theta_vertices, 3):
        theta_points.add(bary(triple, (Q(1, 6), Q(2, 6), Q(3, 6))))
    for point in theta_points:
        check_point(point, theta_rows, theta_ref)
        for vertex in decode(point):
            m = flow(vertex, theta_rows, theta_ref)
            assert sum(m[:3]) == 3 and sum(m[3:]) == 3
            assert all((m[i] + m[i + 3] == 2 for i in range(3)))
        COUNTS['all_nonunit_port_flows'] += 1
    for size in range(1, 4):
        for clique in combinations(theta_vertices, size):
            if any((osc(tuple((x - y for (x, y) in zip(a, b)))) > 1 for (a, b) in combinations(clique, 2))):
                continue
            coeff = tuple((Q(i + 1, size * (size + 1) // 2) for i in range(size)))
            assert decode(bary(clique, coeff)) == dict(zip(clique, coeff))
            COUNTS['all_nonunit_simplex_recovery'] += 1
    assert flow((0, 0, 2, 2), rows, ref) == flow((0, 0, 0, 0), rows, ref)
    assert osc((0, 0, 2, 2)) == 2
    COUNTS['relative_level_negative_control'] = 1
    (a, b) = ((0, 1, 0, 0), (0, 0, 0, 1))
    assert osc(tuple((x - y for (x, y) in zip(a, b)))) == 2
    rounded = decode((Q(0), Q(1, 2), Q(0), Q(1, 2)))
    assert a not in rounded and b not in rounded
    COUNTS['independent_threshold_negative_control'] = 1

def horizontal_checks():
    values = tuple((Q(n, 3) for n in range(-5, 6)))
    arrays = []
    for q in (1, 2, 3):
        for a in product(values, repeat=q):
            if all((1 + a[(j + 1) % q] - a[j] > 0 for j in range(q))):
                arrays.append(a)
    for a in arrays:
        (low, high) = (floor(min(a)), ceil(max(a)))
        c = Q(low + high, 2)
        for chi in (Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)):
            for j in range(len(a)):
                v = c + chi * (a[j] - c)
                vr = c + chi * (a[(j + 1) % len(a)] - c)
                assert 1 + vr - v > 0
                for t in (Q(1, 5), Q(2, 5), Q(3, 5), Q(4, 5)):
                    phase = (1 - t) * v + t * (1 + vr)
                    assert low <= floor(phase) <= high
                    COUNTS['horizontal_no_new_index'] += 1
        COUNTS['coherent_boundary_arrays'] += 1
    (first, second) = ((Q(1, 3), Q(1, 3)), (Q(7, 3), Q(7, 3)))
    inherited_range = (min(floor(min(first)), floor(min(second))), max(ceil(max(first)), ceil(max(second))))
    assert inherited_range == (0, 3)
    assert (0, 1) != inherited_range
    COUNTS['independent_port_reset_negative_control'] = 1

def main():
    base_checks()
    ribbon_checks()
    carrier_checks()
    horizontal_checks()
    for (key, value) in sorted(COUNTS.items()):
        print(f'{key}: {value}')
    print('PASS: exact finite diagnostics; packet topology, isotopy and geometric carrier are proved in the manuscript.')

if __name__ == '__main__':
    import contextlib
    import io
    import json
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        main()
    print(json.dumps({'scope': 'Finite diagnostics; not a topology certificate.', 'output': captured.getvalue().splitlines()}, indent=2, sort_keys=True))
