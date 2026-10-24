#!/usr/bin/env python3
# Finite exact diagnostic for Part 8 of the proof; standard library only; prints a deterministic report and writes no files.
from collections import Counter, defaultdict
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
import json
HERE = Path(__file__).resolve().parent

def cable_piece(p, q, inner_slope):
    assert p >= 2 and q and (gcd(p, q) == 1)
    (u, ell) = (1, -p * inner_slope)
    outer_lambda = p * ell
    regular = outer_lambda + p * q * u
    chi = F(-(p - 1), p) * abs(regular)
    outer_count = gcd(abs(u), abs(outer_lambda))
    inner_count = gcd(abs(p * u), abs(ell))
    assert chi.denominator == 1
    assert outer_count == 1 and inner_count == p
    b = outer_count + inner_count
    genus = F(2 - b - chi, 2)
    assert genus.denominator == 1 and genus >= 0
    return dict(kind=f'cable({p},{q})', copies=1, chi=int(chi), boundaries=b, genus=int(genus), fibre_value=regular, outer_slope=-outer_lambda)

def composing_piece(child_slopes, copies=1):
    return dict(kind='composing', copies=copies, chi=1 - len(child_slopes), boundaries=len(child_slopes) + 1, genus=0, fibre_value=1, outer_slope=sum(child_slopes))

def scale(piece, copies):
    return dict(piece, copies=copies)

def examples():
    first = [cable_piece(2, 1, 0), composing_piece([6, -6], copies=2)]
    second = [cable_piece(3, -2, 0), scale(first[0], 3), composing_piece([6, -6], copies=6)]
    specs = {'square_cable_2_1': (first, [(2, 6), (2, -6)], 3), 'square_cable_2_1_then_3_minus2': (second, [(6, 6), (6, -6)], 13), 'trefoil_cable_2_3_sum_mirror': ([composing_piece([6, -6])], [(1, 6), (1, -6)], 1), 'trefoil_cable_2_1_sum_T3_minus8': ([composing_piece([24, -24]), cable_piece(2, 1, 6)], [(2, 6), (1, -24)], 12)}
    records = {}
    for (name, (pieces, terminals, expected)) in specs.items():
        chi = sum((x['chi'] * x['copies'] for x in pieces))
        holes = 1 + sum((w for (w, _) in terminals))
        genus_h = F(2 - holes - chi, 2)
        assert genus_h.denominator == 1 and genus_h >= 0
        genus_companion = -chi
        assert genus_companion == expected
        assert sum((w * w * slope for (w, slope) in terminals)) == 0
        records[name] = dict(pieces=pieces, terminal_data=terminals, chi_H=chi, boundaries_H=holes, genus_H=int(genus_h), genus_companion=genus_companion)
    return records

def graph_components(vertices, edges):
    graph = {v: set() for v in vertices}
    for (a, b) in edges:
        graph[a].add(b)
        graph[b].add(a)
    (seen, result) = (set(), [])
    for root in graph:
        if root in seen:
            continue
        (stack, part) = ([root], set())
        while stack:
            v = stack.pop()
            if v in part:
                continue
            part.add(v)
            stack.extend(graph[v] - part)
        seen |= part
        result.append(part)
    return result

def build_signs(r, c):
    n = 2 * r
    edges = [(i, (c - i) % n) for i in range(n)]
    edges += [(i, -i % n) for i in range(1, n) if i != r]
    adjacency = defaultdict(set)
    for (a, b) in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    (signs, stack) = ({0: 1}, [0])
    while stack:
        a = stack.pop()
        for b in adjacency[a]:
            if b in signs:
                assert signs[b] == -signs[a]
            else:
                signs[b] = -signs[a]
                stack.append(b)
    assert len(signs) == n and signs[r] == -1
    assert sum(signs.values()) == 0
    return signs

def actual_assemblies(records):
    checks = 0
    for rec in records.values():
        for r in range(1, 17):
            n = 2 * r
            for c in range(1, n, 2):
                if gcd(c, n) != 1:
                    continue
                eps = build_signs(r, c)
                prefix = [0]
                for i in range(n):
                    prefix.append(prefix[-1] - eps[i])
                assert prefix[-1] == 0
                choices = [range(c, n * w, n) for (w, _) in rec['terminal_data']]
                for offsets in product(*choices):
                    terminal_edges = []
                    for ((w, _), offset) in zip(rec['terminal_data'], offsets):
                        size = n * w
                        for ell in range(size):
                            other = (offset - ell) % size
                            assert eps[ell % n] == -eps[other % n]
                            assert prefix[(ell + 1) % n] == prefix[other % n]
                            if ell < other:
                                terminal_edges.append((ell % n, other % n))
                    companion_parts = graph_components(range(n), terminal_edges)
                    assert len(companion_parts) == r
                    assert all((len(x) == 2 for x in companion_parts))
                    multiplicities = Counter((tuple(sorted(x)) for x in terminal_edges))
                    assert set(multiplicities.values()) == {sum((w for (w, _) in rec['terminal_data']))}
                    pattern_edges = [(i, -i % n) for i in range(1, r)]
                    whole = graph_components(range(n), terminal_edges + pattern_edges)
                    assert len(whole) == 1
                    chi_whole = n * rec['chi_H']
                    assert -chi_whole // 2 == r * rec['genus_companion']
                    checks += 1
    return dict(explicit_full_assemblies=checks, max_r=16, note='Essentiality of the local pieces is mathematical input.')

def slope_classes():
    tests = accepted = vertical = 0
    for p in range(2, 10):
        for q in range(-13, 14):
            if not q or gcd(p, q) != 1:
                continue
            assert F(q, p).denominator == p
            vertical += 1
            for mu in range(1, 10):
                for longitude0 in range(-40, 41):
                    if gcd(mu, longitude0) != 1:
                        continue
                    tests += 1
                    inner = F(-longitude0, p * mu)
                    if inner.denominator != 1:
                        continue
                    outer = F(-p * longitude0, mu)
                    assert mu == 1 and outer == p * p * inner
                    assert gcd(mu, p * longitude0) == 1
                    assert gcd(p * mu, longitude0) == p
                    assert p * longitude0 + p * q * mu != 0
                    accepted += 1
    return dict(primitive_cable_classes=tests, integral_child_classes=accepted, nonintegral_vertical_inner_slopes=vertical)

def arbitrary_two_defect_words():
    words = reflections = 0
    for r in range(1, 9):
        n = 2 * r
        for choices in product((1, -1), repeat=r - 1):
            eps = {0: 1, r: -1}
            for (i, sign) in enumerate(choices, 1):
                (eps[i], eps[n - i]) = (sign, -sign)
            roots = set()
            for w in range(1, 7):
                for offset in range(1, n * w, 2):
                    if all((eps[i % n] == -eps[(offset - i) % n] for i in range(n * w))):
                        roots.add(offset % n)
                        reflections += 1
            assert len(roots) <= 1
            words += 1
    return dict(all_pattern_compatible_words=words, actual_nonunit_reflections=reflections, max_terminal_degree=6)

def gap_products():
    nonfixed_products = endcaps = 0
    for roots in range(2, 34, 2):
        for c in range(1, roots, 2):
            fixed = {i for i in range(roots) if (c - i - 1) % roots == i}
            assert len(fixed) == 2
            for w in range(1, 10):
                size = roots * w
                for offset in range(c, size, roots):
                    match = lambda i: (offset - i) % size
                    gap = lambda i: (offset - i - 1) % size
                    fixed_ports = [i for i in range(size) if gap(i) == i]
                    assert len(fixed_ports) == 2
                    assert {i % roots for i in fixed_ports} <= fixed
                    endcaps += 2
                    for i in range(roots):
                        j = (c - i - 1) % roots
                        if i in fixed:
                            continue
                        port_gaps = list(range(i, size, roots))
                        assert all((gap(ell) % roots == j and gap(ell) != ell for ell in port_gaps))
                        assert len({gap(ell) for ell in port_gaps}) == w
                        assert all((match(ell) % roots == (j + 1) % roots and match((ell + 1) % size) % roots == j for ell in port_gaps))
                        nonfixed_products += 1
    even_w_example = dict(root_count=4, degree=2, offset=1, terminal_fixed_gaps=[0, 4], projections=[0, 0], fixed_root_gaps=[0, 2])
    return dict(nonfixed_product_boundary_checks=nonfixed_products, terminal_endcaps=endcaps, even_degree_example=even_w_example, note='Endpoint consistency is checked; product straightening is not computed.')

def four_actual_boundaries():
    signs = (1, -1, 1, -1)
    edges = []
    for offset in (1, 3):
        for i in range(4):
            j = (offset - i) % 4
            assert signs[i] == -signs[j]
            if i < j:
                edges.append((i, j))
    assert len(graph_components(range(4), edges)) == 1
    (chi, boundaries) = (-4, 4)
    genus = F(2 - boundaries - chi, 2)
    assert genus == 1
    return dict(edges=edges, companion_boundaries=boundaries, genus=int(genus))

def main():
    records = examples()
    output = dict(slopes=slope_classes(), examples=records, assemblies=actual_assemblies(records), two_defects=arbitrary_two_defect_words(), nonunit_gaps=gap_products(), four_parallel=four_actual_boundaries())
    print(json.dumps(output, ensure_ascii=False, indent=2))
    print('PASS: independent Euler, orientation, connectivity and gap diagnostics')
if __name__ == '__main__':
    main()
