#!/usr/bin/env python3
# Finite exact diagnostic for Part 7 of the proof; standard library only; prints a deterministic report and writes no files.
from collections import Counter, defaultdict
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations, permutations, product
from json import dumps
from pathlib import Path
COUNTS = Counter()

def floor(x):
    return x.numerator // x.denominator

def osc(v):
    return max(v) - min(v)

def delta(u, v):
    return osc(tuple((a - b for (a, b) in zip(u, v))))

def average(states, weights):
    return tuple((sum((w * u[j] for (u, w) in zip(states, weights))) for j in range(len(states[0]))))

def vector_decode(states, weights):
    f = average(states, weights)
    cuts = {Q(0), Q(1)}
    for value in f:
        frac = value - floor(value)
        if frac:
            cuts.add(1 - frac)
    cuts = sorted(cuts)
    ans = defaultdict(Q)
    for (a, b) in zip(cuts, cuts[1:]):
        theta = (a + b) / 2
        z = tuple((floor(value + theta) for value in f))
        z = tuple((v - z[0] for v in z))
        ans[z] += b - a
    assert sum(ans.values()) == 1
    return dict(ans)

def cochain(edges, p0, u):
    return tuple((p + u[b] - u[a] for ((a, b), p) in zip(edges, p0)))

def cochain_decode(edges, p0, states, weights):
    ans = defaultdict(Q)
    for (u, weight) in vector_decode(states, weights).items():
        p = cochain(edges, p0, u)
        assert set(p) <= {0, 1}
        ans[p] += weight
    return dict(ans)

def packet_decode(edges, p0, states, weights, order):
    f = average(states, weights)
    inputs = [cochain(edges, p0, u) for u in states]
    bands = []
    cuts = {Q(0), Q(1)}
    for (e, (a, b)) in enumerate(edges):
        start = f[a]
        local = []
        for i in order:
            if inputs[i][e] and weights[i]:
                end = start + weights[i]
                local.append((start, end, i))
                cuts.update((start - floor(start), end - floor(end)))
                start = end
        assert start - f[a] == p0[e] + f[b] - f[a]
        assert 0 <= start - f[a] <= 1
        bands.append(local)
    ans = defaultdict(Q)
    cuts = sorted(cuts)
    for (a, b) in zip(cuts, cuts[1:]):
        r = (a + b) / 2
        selected = tuple((sum((floor(end - r) - floor(start - r) for (start, end, _) in band)) for band in bands))
        assert set(selected) <= {0, 1}
        ans[selected] += b - a
    return dict(ans)

def positive_compositions(total, size):
    if size == 1:
        yield (total,)
    else:
        for first in range(1, total - size + 2):
            for tail in positive_compositions(total - first, size - 1):
                yield ((first,) + tail)

def chain_lemma():
    vectors = [(0,) + v for v in product(range(-2, 3), repeat=3)]
    adjacent = {(i, j): delta(vectors[i], vectors[j]) <= 1 for (i, j) in combinations(range(len(vectors)), 2)}
    for (i, j) in combinations(range(len(vectors)), 2):
        if not adjacent[i, j]:
            continue
        (a, b) = (vectors[i], vectors[j])
        assert all((x <= y for (x, y) in zip(a, b))) or all((x >= y for (x, y) in zip(a, b)))
        for nums in positive_compositions(5, 2):
            ws = tuple((Q(n, 5) for n in nums))
            assert vector_decode((a, b), ws) == dict(zip((a, b), ws))
            COUNTS['root_zero_chain_edge_recoveries'] += 1
    for ids in combinations(range(len(vectors)), 3):
        if not all((adjacent[i, j] for (i, j) in combinations(ids, 2))):
            continue
        states = tuple((vectors[i] for i in ids))
        bottom = tuple((min((u[j] for u in states)) for j in range(4)))
        ordered = sorted(states, key=sum)
        assert all((set((a - b for (a, b) in zip(u, bottom))) <= {0, 1} for u in states))
        assert all((all((a <= b for (a, b) in zip(u, v))) for (u, v) in zip(ordered, ordered[1:])))
        for nums in positive_compositions(5, 3):
            ws = tuple((Q(n, 5) for n in nums))
            assert vector_decode(states, ws) == dict(zip(states, ws))
            COUNTS['root_zero_chain_triangle_recoveries'] += 1
    COUNTS['integer_vectors_for_chain_lemma'] = len(vectors)
    (a, b) = ((0, 1, 0), (0, 0, 1))
    actual = vector_decode((a, b), (Q(1, 2), Q(1, 2)))
    assert delta(a, b) == 2
    assert actual == {(0, 0, 0): Q(1, 2), (0, 1, 1): Q(1, 2)}
    assert actual != {a: Q(1, 2), b: Q(1, 2)}
    COUNTS['noncyclic_edge_negative_control'] = 1

def bouquet(lengths, shared_loop=False):
    (edges, p0) = ([], [])
    next_vertex = 1
    for length in lengths:
        path = [0] + list(range(next_vertex, next_vertex + length - 1)) + [0]
        next_vertex += length - 1
        edges.extend(zip(path, path[1:]))
        p0.extend((1,) + (0,) * (length - 1))
    if shared_loop:
        edges.append((0, 0))
        p0.append(1)
    return (next_vertex, tuple(edges), tuple(p0), range(-1, 2))

def admissible_states(n, edges, p0, domain):
    return [(0,) + u for u in product(domain, repeat=n - 1) if set(cochain(edges, p0, (0,) + u)) <= {0, 1}]

def graph_case(name, spec):
    (n, edges, p0, domain) = spec
    states = admissible_states(n, edges, p0, domain)
    assert states
    by_cochain = {cochain(edges, p0, u): u for u in states}
    assert len(by_cochain) == len(states)
    COUNTS['models'] += 1
    COUNTS['admissible_model_vertices'] += len(states)
    COUNTS['models_with_negative_potentials'] += any((min(u) < 0 for u in states))

    def check_point(us, ws, deep=False):
        point = vector_decode(us, ws)
        for u in point:
            assert set(cochain(edges, p0, u)) <= {0, 1}
        assert all((delta(u, v) <= 1 for (u, v) in combinations(point, 2)))
        f = average(us, ws)
        assert average(tuple(point), tuple(point.values())) == f
        expected = tuple((sum((w * cochain(edges, p0, u)[e] for (u, w) in zip(us, ws))) for e in range(len(edges))))
        observed = tuple((sum((w * cochain(edges, p0, u)[e] for (u, w) in point.items())) for e in range(len(edges))))
        assert observed == expected
        COUNTS['weighted_points'] += 1
        COUNTS['wall_marginal_equalities'] += len(edges)
        if all((delta(u, v) <= 1 for (u, v) in combinations(us, 2))):
            assert point == {u: w for (u, w) in zip(us, ws) if w}
            COUNTS['cyclic_simplex_exact_recoveries'] += 1
        extra = states[-1]
        assert vector_decode(us + (extra,), ws + (Q(0),)) == point
        COUNTS['zero_face_checks'] += 1
        for t in (Q(0), Q(1, 2), Q(1)):
            mix_states = us + tuple(point)
            mix_weights = tuple(((1 - t) * w for w in ws)) + tuple((t * w for w in point.values()))
            assert vector_decode(mix_states, mix_weights) == point
            COUNTS['homotopy_retraction_constancy_checks'] += 1
        if deep:
            decoded = cochain_decode(edges, p0, us, ws)
            for root in range(n):
                rooted = tuple((tuple((x - u[root] for x in u)) for u in us))
                assert cochain_decode(edges, p0, rooted, ws) == decoded
                COUNTS['global_root_changes'] += 1
            for ref in us:
                new_base = cochain(edges, p0, ref)
                translated = tuple((tuple((a - b for (a, b) in zip(u, ref))) for u in us))
                assert cochain_decode(edges, new_base, translated, ws) == decoded
                COUNTS['reference_changes'] += 1
            orders = (tuple(range(len(us))), tuple(reversed(range(len(us)))))
            for order in orders:
                assert packet_decode(edges, p0, us, ws, order) == decoded
                COUNTS['labelled_packet_phase_integrations'] += 1
            if len(us) <= 3:
                for order in permutations(range(len(us))):
                    assert vector_decode(tuple((us[i] for i in order)), tuple((ws[i] for i in order))) == point
                    COUNTS['input_label_permutations'] += 1
    serial = 0
    for size in (1, 2, 3):
        for us in combinations(states, size):
            for nums in positive_compositions(3, size):
                ws = tuple((Q(num, 3) for num in nums))
                check_point(us, ws, serial % 23 == 0)
                serial += 1
    dense_weights = tuple((Q(i + 1, len(states) * (len(states) + 1) // 2) for i in range(len(states))))
    check_point(tuple(states), dense_weights, True)
    check_point(tuple(states), (Q(1, len(states)),) * len(states), True)
    for (a, b) in combinations(states, 2):
        for denominator in (1000, 1000000):
            eps = Q(1, denominator)
            wa = (Q(1, 2) - eps, Q(1, 2) + eps)
            wb = (Q(1, 2) + eps, Q(1, 2) - eps)
            (ra, rb) = (vector_decode((a, b), wa), vector_decode((a, b), wb))
            variation = sum((abs(ra.get(u, Q(0)) - rb.get(u, Q(0))) for u in ra.keys() | rb.keys()))
            (fa, fb) = (average((a, b), wa), average((a, b), wb))
            assert variation <= 2 * sum((abs(x - y) for (x, y) in zip(fa, fb)))
            COUNTS['near_phase_collision_continuity_checks'] += 1
    return {'name': name, 'chambers': n, 'walls': len(edges), 'vertices': len(states)}

def main():
    chain_lemma()
    cases = [('three_phase_cycle', bouquet((3,))), ('two_petal_2_by_3', bouquet((2, 3))), ('three_petal_cube', bouquet((2, 2, 2))), ('three_petal_3_by_3_by_3', bouquet((3, 3, 3))), ('two_petal_4_by_4', bouquet((4, 4))), ('shared_component_loop', bouquet((2, 2), shared_loop=True)), ('theta_graph', (4, ((0, 1), (1, 3), (0, 2), (2, 3), (3, 0)), (1, 0, 1, 0, 0), range(-3, 4))), ('crossed_chamber_graph', (5, ((0, 1), (1, 2), (2, 0), (0, 3), (3, 4), (4, 0), (2, 4), (1, 3)), (1, 0, 0, 0, 1, 0, 1, 0), range(-4, 5)))]
    inventory = [graph_case(name, spec) for (name, spec) in cases]
    print('PASS: exact algebra diagnostics; geometry and topology require the written audit.')
    print(dumps({'counts': dict(COUNTS), 'models': inventory}, ensure_ascii=False, indent=2))
if __name__ == '__main__':
    main()
