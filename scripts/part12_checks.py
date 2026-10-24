#!/usr/bin/env python3
# Finite exact diagnostic for Part 12 of the proof; standard library only; prints a deterministic report and writes no files.
from fractions import Fraction
from itertools import combinations, product
from math import gcd, lcm
from pathlib import Path
import json
import hashlib
import random
import time
BASE = Path(__file__).resolve().parent

def rank(a):
    a = [[Fraction(x) for x in row] for row in a]
    i = 0
    for j in range(len(a[0])):
        h = next((h for h in range(i, len(a)) if a[h][j]), None)
        if h is None:
            continue
        (a[i], a[h]) = (a[h], a[i])
        t = a[i][j]
        a[i] = [x / t for x in a[i]]
        for h in range(len(a)):
            if h != i and a[h][j]:
                t = a[h][j]
                a[h] = [x - t * y for (x, y) in zip(a[h], a[i])]
        i += 1
        if i == len(a):
            break
    return i

def components(n, edges):
    adj = [[] for _ in range(n)]
    for (i, j) in edges:
        adj[i].append(j)
        adj[j].append(i)
    (seen, out) = (set(), [])
    for i in range(n):
        if i in seen:
            continue
        (cc, todo) = (set(), [i])
        while todo:
            j = todo.pop()
            if j in cc:
                continue
            cc.add(j)
            todo.extend(adj[j])
        seen |= cc
        out.append(cc)
    return out

def pants_degree_test(rmax=6, qmax=5):
    count = forbidden = axes = 0
    for r in range(1, rmax + 1):
        n = 2 * r
        for plus in combinations(range(n), r):
            eps = [-1] * n
            for j in plus:
                eps[j] = 1
            for q in range(1, qmax + 1):
                nn = n * q
                found = []
                for a in range(nn):
                    count += 1
                    ok = eps[a % n] == 1 and eps[(a + nn // 2) % n] == -1
                    if ok:
                        ok = all((j in (a, (a + nn // 2) % nn) or eps[(2 * a - j) % n] == -eps[j % n] for j in range(nn)))
                    if ok:
                        found.append(a)
                if q > 1:
                    assert not found, (r, q, eps, found)
                    forbidden += 1
                axes += len(found)
    return dict(rmax=rmax, qmax=qmax, expanded_axis_tests=count, forbidden_periodic_words=forbidden, surviving_axes=axes)

def normal(word, orders):
    out = []
    for (i, e) in word:
        if orders[i]:
            e %= orders[i]
        if not e:
            continue
        if out and out[-1][0] == i:
            e += out.pop()[1]
            if orders[i]:
                e %= orders[i]
            if not e:
                continue
        out.append((i, e))
    return tuple(out)

def multiply(a, b, orders):
    return normal(a + b, orders)

def inverse(a, orders):
    return normal(tuple(((i, -e) for (i, e) in reversed(a))), orders)

def power(a, n, orders):
    if n < 0:
        (a, n) = (inverse(a, orders), -n)
    out = ()
    for _ in range(n):
        out = multiply(out, a, orders)
    return out

def peripheral_tests():
    count = 0
    for p in range(2, 8):
        for q in range(2, 9):
            if gcd(p, q) != 1:
                continue
            orders = (p, q)
            d = ((0, 1), (1, 1))
            for w in (((0, 1),), ((1, 1),), ((0, 1), (1, 1), (0, 1))):
                w = normal(w, orders)
                for (a, b) in product(range(-6, 7), repeat=2):
                    left = multiply(multiply(power(d, a, orders), w, orders), power(d, -b, orders), orders)
                    assert (left == w) == (a == b == 0), (p, q, w, a, b)
                    count += 1
    old_count = count
    for orders in ((2, 0), (3, 0), (0, 0)):
        d = ((0, 1), (1, 1))
        for w in (((0, 1),), ((1, 1),), ((0, 1), (1, 1), (0, 1))):
            w = normal(w, orders)
            for (a, b) in product(range(-6, 7), repeat=2):
                left = multiply(multiply(power(d, a, orders), w, orders), power(d, -b, orders), orders)
                assert (left == w) == (a == b == 0), (orders, w, a, b)
                count += 1
    orders = (2, 2)
    d = ((0, 1), (1, 1))
    w = ((0, 1),)
    assert multiply(multiply(d, w, orders), d, orders) == w
    return dict(exponent_bound=6, free_product_equations=count, torus_cap_equations=old_count, cable_and_composing_equations=count - old_count, all_nonzero_return_windings_excluded=True, excluded_zero_Euler_orbifold_has_nonzero_solution=True)

def packet_gap_tests():
    rng = random.Random(6006)
    count = singles = 0
    for n in range(2, 66, 2):
        for v in range(1, 7):
            for _ in range(15):
                cc = [rng.randrange(n // 2) * 2 + 1 for _ in range(v)]
                g = n
                for c in cc:
                    g = gcd(g, c - cc[0])
                (q, k) = (g // 2, n // g)
                edges = [(i, (c - i) % n) for c in cc for i in range(n)]
                point = components(n, edges)
                gaps = components(n, [(i, (c - 1 - i) % n) for c in cc for i in range(n)])
                assert len(point) == q
                assert all((len(a) == 2 * k for a in point))
                assert len(gaps) == q + 1
                adj = [[] for _ in range(n)]
                for (i, j) in edges:
                    adj[i].append(j)
                colors = {}
                for a in point:
                    start = next(iter(a))
                    colors[start] = 1
                    todo = [start]
                    while todo:
                        h = todo.pop()
                        for j in adj[h]:
                            if j in colors:
                                assert colors[j] == -colors[h]
                            else:
                                colors[j] = -colors[h]
                                todo.append(j)
                    assert sum((colors[j] for j in a)) == 0
                if v == 1:
                    assert k == 1 and q == n // 2
                    singles += 1
                count += 1
    return dict(Nmax=64, terminal_range=[1, 6], configurations=count, singleton_terminal_configurations=singles)

def framed_modes():
    genus = {6: 1, -6: 1, 10: 2, -10: 2, 12: 3, -12: 3}
    count = singleton = signatures = 0
    examples = []
    for length in range(2, 6):
        for weights in product((6, -6, 10), repeat=length):
            signatures += 1
            for mask in range(1, 2 ** length):
                vv = [i for i in range(length) if mask & 1 << i]
                f = sum((weights[i] for i in vv))
                v = len(vv)
                gh = sum((genus[s] for (i, s) in enumerate(weights) if i not in vv))
                chi_h = 1 - v - 2 * gh
                assert chi_h < 0
                if v == 1:
                    assert gh > 0
                    assert 1 + (v - 2 + 2 * gh) == 2 * gh
                    singleton += 1
                for k in (1, 2, 3):
                    if v == 1 and k > 1:
                        continue
                    chi_f = 2 * k * chi_h
                    b = 2 * k
                    gf = (2 - b - chi_f) // 2
                    assert gf == 1 + k * (v - 2 + 2 * gh)
                    assert gf > 0
                    assert sum((-weights[i] for i in vv)) == -f
                    count += 1
            if weights == (6, 6, -6):
                modes = []
                for mask in range(1, 2 ** length):
                    vv = [i for i in range(length) if mask & 1 << i]
                    if sum((weights[i] for i in vv)) == 6:
                        gh = sum((genus[s] for (i, s) in enumerate(weights) if i not in vv))
                        modes.append(dict(V=vv, v=len(vv), genus_H=gh, genus_F_k1=1 + len(vv) - 2 + 2 * gh))
                examples.append(dict(weights=list(weights), framing=6, modes=modes))
    return dict(weight_signatures=signatures, Euler_mode_checks=count, singleton_mode_checks=singleton, examples=examples)

def weighted_packet_tests():
    rng = random.Random(62026)
    count = endpoint_checks = even_ends = 0
    for n in range(2, 50, 2):
        for v in range(1, 6):
            for _ in range(20):
                bb = [rng.randrange(1, 9) for _ in range(v)]
                cc = [2 * rng.randrange(n * b // 2) + 1 for b in bb]
                (edges, gap_edges, local_ends) = ([], [], [])
                for (b, c) in zip(bb, cc):
                    nn = n * b
                    for j in range(nn):
                        edges.append((j % n, (c - j) % nn % n))
                        gap_edges.append((j % n, (c - 1 - j) % nn % n))
                        if (c - 1 - j) % nn == j:
                            local_ends.append(j % n)
                    assert sorted({j % b for j in range(b)}) == list(range(b))
                points = components(n, edges)
                gaps = components(n, gap_edges)
                g = n
                for c in cc:
                    g = gcd(g, c - cc[0])
                assert len(points) == g // 2
                assert len(gaps) == g // 2 + 1
                assert all((len(a) == 2 * n // g for a in points))
                glabel = {j: i for (i, a) in enumerate(gaps) for j in a}
                dual_edges = []
                for a in points:
                    endpoints = {tuple(sorted((glabel[j], glabel[(j - 1) % n]))) for j in a}
                    assert len(endpoints) == 1
                    edge = endpoints.pop()
                    assert edge[0] != edge[1]
                    dual_edges.append(edge)
                assert len(set(dual_edges)) == len(dual_edges)
                assert len(components(len(gaps), dual_edges)) == 1
                deg = [0] * len(gaps)
                for (a, b) in dual_edges:
                    deg[a] += 1
                    deg[b] += 1
                assert sorted(deg).count(1) == 2
                assert max(deg) <= 2
                for j in local_ends:
                    assert deg[glabel[j]] == 1
                    endpoint_checks += 1
                for (b, c) in zip(bb, cc):
                    nn = n * b
                    ee = [j for j in range(nn) if (c - 1 - j) % nn == j]
                    assert len(ee) == 2
                    if b % 2 == 0:
                        assert glabel[ee[0] % n] == glabel[ee[1] % n]
                        even_ends += 1
                count += 1
    return dict(Nmax=48, degrees=[1, 8], terminal_range=[1, 5], configurations=count, local_end_checks=endpoint_checks, even_degree_same_end_cases=even_ends, interior_dual_regions_are_linear=True)

def recursive_modes(knot):
    tag = knot[0]
    if tag == 'T':
        (_, p, q) = knot
        assert p >= 2 and abs(q) >= 2 and (gcd(p, q) == 1)
        genus = (p - 1) * (abs(q) - 1) // 2
        return [dict(slope=0, chi=1 - 2 * genus, b=(), vertical=False), dict(slope=p * q, chi=None, b=(), vertical=True)]
    if tag == 'C':
        (_, p, q, child) = knot
        assert p >= 2 and q != 0 and (gcd(p, q) == 1)
        out = [dict(slope=p * q, chi=None, b=(), vertical=True)]
        for mode in recursive_modes(child):
            t = mode['slope']
            cw = -(p - 1) * abs(q - p * t)
            if mode['vertical']:
                (chi, bb) = (cw, (p,))
            else:
                chi = cw + p * mode['chi']
                bb = tuple((p * b for b in mode['b']))
            out.append(dict(slope=p * p * t, chi=chi, b=bb, vertical=False))
        return out
    assert tag == 'S' and len(knot) >= 3
    out = []
    for modes in product(*(recursive_modes(x) for x in knot[1:])):
        chi = 2 - len(knot)
        bb = []
        for m in modes:
            if m['vertical']:
                bb.append(1)
            else:
                chi += m['chi']
                bb.extend(m['b'])
        out.append(dict(slope=sum((m['slope'] for m in modes)), chi=chi, b=tuple(bb), vertical=False))
    return out

def recursive_mode_tests():
    torus = [('T', 2, 3), ('T', 2, -3), ('T', 2, 5), ('T', 3, -4)]
    knots = list(torus)
    for (x, y) in product(torus, repeat=2):
        knots.append(('S', x, y))
    first = list(knots)
    for x in first:
        for (p, q) in ((2, 1), (2, -3), (3, 2), (3, -5)):
            knots.append(('C', p, q, x))
    for (i, x) in enumerate(first):
        y = ('C', 2, -1, torus[i % len(torus)])
        knots.append(('S', x, y))
        knots.append(('C', 3, 1, ('S', x, y)))
    count = high = cap = 0
    degree_max = 0
    for knot in knots:
        for m in recursive_modes(knot):
            count += 1
            assert isinstance(m['slope'], int)
            if m['vertical']:
                cap += 1
                continue
            (chi, bb) = (m['chi'], m['b'])
            assert chi < 0
            numerator = 1 - sum(bb) - chi
            assert numerator >= 0 and numerator % 2 == 0
            if bb:
                degree_max = max(degree_max, max(bb))
                high += any((b > 1 for b in bb))
                for k in (1, 2, 3, 7):
                    (chi_f, nbd) = (2 * k * chi, 2 * k)
                    gf = (2 - nbd - chi_f) // 2
                    assert gf == 1 - k * (1 + chi) and gf >= 1
            else:
                assert m['slope'] == 0
    base = ('S', torus[0], torus[0], torus[1])
    cable = ('C', 2, 1, base)
    special = [m for m in recursive_modes(cable) if m['slope'] == 24]
    assert sorted(((m['chi'], m['b']) for m in special)) == [(-19, (2,)), (-19, (2,)), (-15, (2, 2, 2))]
    smallest = [m for m in recursive_modes(('C', 2, 1, torus[0])) if m['slope'] == 24]
    assert len(smallest) == 1
    assert smallest[0]['chi'] == -11 and smallest[0]['b'] == (2,)
    return dict(recursive_constructions=len(knots), mode_markings=count, vertical_roots=cap, higher_degree_horizontal_modes=high, largest_frontier_degree=degree_max, multimode_cable_example=special, two_actual_cable_example=smallest[0])

def distributed_return_tests(rmax=8):
    count = reduced = repeated = rejected = 0
    for r in range(1, rmax + 1):
        n = 2 * r
        for plus in combinations([j for j in range(1, n) if j != r], r - 1):
            pos = set(plus) | {0}
            eps = [1 if j in pos else -1 for j in range(n)]
            axes = [a for a in range(n) if eps[a] == 1 and eps[(a + r) % n] == -1 and all((j in (a, (a + r) % n) or eps[(2 * a - j) % n] == -eps[j] for j in range(n)))]
            if 0 not in axes:
                continue
            offsets = [c for c in range(1, n, 2) if all((eps[(c - j) % n] == -eps[j] for j in range(n)))]
            for (b, c) in product(axes, offsets):
                count += 1
                gg = gcd(gcd(n, 2 * b), c)
                ed = [(j, -j % n) for j in range(n)]
                ed += [(j, (2 * b - j) % n) for j in range(n)]
                ed += [(j, (c - j) % n) for j in range(2 * n)]
                ed = [(i % n, j % n) for (i, j) in ed]
                cc = components(n, ed)
                defects = {0, r, b, (b + r) % n}
                is_reduced = all((a & defects for a in cc))
                assert is_reduced == (gg == 1)
                if b != 0:
                    assert c == (b + r) % n
                if is_reduced:
                    assert len(cc) == 1
                    genus = (2 - 4 + 12 * n) // 2
                    assert genus == 12 * r - 1
                    reduced += 1
                    repeated += b == 0
                else:
                    rejected += 1
        eps = [1] + [-1] * r + [1] * (r - 1)
        assert all((eps[(1 - j) % n] == -eps[j] for j in range(n)))
        assert all((j in (0, r) or eps[-j % n] == -eps[j] for j in range(n)))
    return dict(rmax=rmax, signed_axis_return_choices=count, reduced_choices=reduced, repeated_axis_reduced_choices=repeated, excluded_closed_component_choices=rejected, every_reduced_surface_connected=True)

def weighted_support_tests():
    counts = dict(primitive_weight_lists=0, framing_choices=0, child_mode_extensions=0, higher_actual_degree_extensions=0)
    child_knots = [('T', 2, 3), ('C', 2, 1, ('T', 2, 3)), ('S', ('T', 2, 3), ('T', 2, 3), ('T', 2, -3)), ('C', 2, -1, ('S', ('T', 2, 3), ('T', 2, -3)))]
    for m in range(2, 5):
        for weights in product(range(1, 5), repeat=m):
            gg = 0
            for w in weights:
                gg = gcd(gg, w)
            if gg != 1:
                continue
            counts['primitive_weight_lists'] += 1
            S = sum(weights)
            for t in range(-12, 13):
                if t == 0 or any((S * t % w for w in weights)):
                    continue
                counts['framing_choices'] += 1
                framing = [S * t // w for w in weights]
                assert all((f * w == S * t for (f, w) in zip(framing, weights)))
                assert [gcd(S * abs(t), w) for w in weights] == list(weights)
                assert gcd(S, S * abs(t)) == S
                chi_h = -(m - 1) * S * abs(t)
                gh_numerator = 2 - 2 * S - chi_h
                assert gh_numerator >= 0 and gh_numerator % 2 == 0
                for child in child_knots:
                    for mode in recursive_modes(child):
                        if mode['slope'] != t:
                            continue
                        if mode['vertical']:
                            (chi, bb) = (chi_h, (S,))
                        else:
                            assert mode['b']
                            chi = chi_h + S * mode['chi']
                            bb = tuple((S * b for b in mode['b']))
                        assert chi + S <= 0
                        gR_numerator = 2 - S - sum(bb) - chi
                        assert gR_numerator >= 0 and gR_numerator % 2 == 0
                        for k in (1, 2, 5):
                            gf = (2 - 2 * k * S - 2 * k * chi) // 2
                            assert gf == 1 - k * (chi + S) and gf > 0
                        counts['child_mode_extensions'] += 1
                        counts['higher_actual_degree_extensions'] += max(weights) > 1
    small = dict(weights=[1, 2], t=2, frames=[6, 3], child='C(2,1;T(2,3))', chi_R=-6, external_degrees=[1, 2], cap_degrees=[3], actual_counts=[2, 4], chi_F=-12, genus_F=4)
    assert (2 - 6 - small['chi_F']) // 2 == small['genus_F']
    multi = dict(weights=[1, 2], t=6, frames=[18, 9], child='T(2,3)#T(2,3)#T(2,-3)', chi_R=[-30, -30, -24], cap_degrees=[[3], [3], [3, 3, 3]], actual_counts=[2, 4], genera_F=[28, 28, 22])
    for (chi, gf) in zip(multi['chi_R'], multi['genera_F']):
        assert (2 - 6 - 2 * chi) // 2 == gf
    return dict(**counts, active_actual_degree_two_example=small, distributed_four_branch_example=multi)

def signed_framing_tests():
    vals = (-6, -4, -3, -2, -1, 1, 2, 3, 4, 6)
    counts = dict(framing_lists=0, nonzero_reciprocal=0, nonintegral_inner_slope=0, integral_inner_slope=0, zero_reciprocal=0, child_modes=0, planar_support_modes=0, meridional_cable_checks=0)
    children = [('T', 2, 3), ('C', 2, 1, ('T', 2, 3)), ('S', ('T', 2, 3), ('T', 2, 3), ('T', 2, -3))]
    for m in (2, 3, 4):
        for ff in product(vals, repeat=m):
            counts['framing_lists'] += 1
            D = lcm(*(abs(f) for f in ff))
            ww = [D // f for f in ff]
            S = sum(ww)
            W = sum((abs(w) for w in ww))
            gg = 0
            for w in ww:
                gg = gcd(gg, w)
            assert gg == 1
            qroot = gcd(abs(S), D)
            chi_h = -(m - 1) * D
            gh2 = 2 - W - qroot - chi_h
            assert gh2 >= 0 and gh2 % 2 == 0
            if S:
                counts['nonzero_reciprocal'] += 1
                t = Fraction(D, S)
                if t.denominator != 1:
                    counts['nonintegral_inner_slope'] += 1
                    continue
                counts['integral_inner_slope'] += 1
                assert qroot == abs(S)
                for child in children:
                    for mode in recursive_modes(child):
                        if mode['slope'] != t:
                            continue
                        if mode['vertical']:
                            chi = chi_h
                            caps = (abs(S),)
                        else:
                            assert mode['b']
                            chi = chi_h + abs(S) * mode['chi']
                            caps = tuple((abs(S) * x for x in mode['b']))
                        assert chi < 0
                        gr2 = 2 - W - sum(caps) - chi
                        assert gr2 >= 0 and gr2 % 2 == 0
                        ks = (1,) if len(caps) == 1 else (1, 2, 3)
                        for k in ks:
                            gf = 1 - k * (chi + W)
                            assert gf >= 0
                        counts['planar_support_modes'] += chi + W == 1
                        counts['child_modes'] += 1
            else:
                counts['zero_reciprocal'] += 1
                for P in (1, 2, 3, 4, 6, 12):
                    g = gcd(P, D)
                    b = P // g
                    a = D // g
                    assert gcd(a, b) == 1 and b * D == a * P
                    chi = -b * (m - 1) * D - a * (P - 1)
                    ext = b * W
                    gr2 = 2 - ext - a - chi
                    assert gr2 >= 0 and gr2 % 2 == 0
                    assert 1 - ext - chi >= 0
                    counts['meridional_cable_checks'] += 1
    assert counts['planar_support_modes'] > 0
    return counts

def actual_examples():
    b = [[-3, 1, 1], [1, -3, 1], [1, 1, -1]]
    x = [1, 1, 2]
    assert rank(b) == 2
    assert [sum((a * y for (a, y) in zip(row, x))) for row in b] == [0, 0, 0]
    S = sum(x)
    qq = [gcd(a, S - a) for a in x]
    assert qq == [1, 1, 2]
    chi_R = -S
    genus_R = (2 - sum(qq) - chi_R) // 2
    assert genus_R == 1
    high_port = dict(actual_components=8, framings=[-3, -3, -1], actual_pair_counts=[1, 1, 2], q=qq, chi_R=chi_R, genus_R=genus_R, vertex_components=2, actual_boundaries_each=4, genera=[1, 1])
    n = 6
    eps = [1, 1, 1, -1, -1, -1]
    edges = []
    tethers = []
    for a in (0, 2):
        tethers += [(a, 1), ((a + 3) % n, -1)]
        for j in range(n):
            k = (2 * a - j) % n
            if k != j and j < k:
                assert eps[k] == -eps[j]
                edges.append((j, k))
    tethers += [(0, 1), (1, 1), (3, -1), (4, -1)]
    edges.append((2, 5))
    assert len(components(n, edges)) == 1
    assert len(tethers) == 8
    chi = -3 * n
    genus = (2 - 8 - chi) // 2
    assert genus == 6
    many_actual = dict(actual_components=8, framings=[-2, -2, -2], actual_pair_counts=[1, 1, 2], q=[1, 1, 1], central_sheets=6, connected=True, chi=chi, genus=genus)
    s = 6
    a = 2 * s
    root_q = gcd(2, 2 * s)
    assert root_q == 2
    chi = -2 * a
    genus = (2 - 4 - chi) // 2
    assert genus == 11
    free_return = dict(actual_components=4, knot='T(2,3)', support='two zero-framed parallels', pair_framings=[12, 12], central_q=[1, 1, 2], genus_R=5, companion_vertical_annuli=2, connected_vertex_genus=genus, chi=chi, actual_boundaries=4, conclusion='X=Y contractible by Theorem K and Proposition H')
    cable_degree_two = dict(actual_components=2, knot='C(2,1;T(2,3))', framing=24, chi_R=-11, genus_R=5, frontier_degree=2, chi_F=-22, genus_F=11, conclusion='contractible by Theorem G')
    return dict(oriented_pants_exclusion=dict(actual_components=6, framings=[-3, -3, -1], kernel=x, q=qq, conclusion='point'), higher_port=high_port, many_actual=many_actual, active_free_return=free_return, solved_cable_degree_two=cable_degree_two)

def main():
    start = time.monotonic()
    out = dict(pants=pants_degree_test(), peripheral=peripheral_tests(), packets=packet_gap_tests(), framed_modes=framed_modes(), weighted_packets=weighted_packet_tests(), recursive_modes=recursive_mode_tests(), distributed_free_return=distributed_return_tests(), weighted_supports=weighted_support_tests(), arbitrary_signed_framings=signed_framing_tests(), actual_examples=actual_examples())
    print(json.dumps(out, ensure_ascii=False, indent=2))
if __name__ == '__main__':
    main()
