#!/usr/bin/env python3
# Finite exact diagnostic for Part 9 of the proof; standard library only; prints a deterministic report and writes no files.
from itertools import product
from math import gcd
import json

def components(vertices, edges):
    graph = {v: set() for v in vertices}
    for (a, b) in edges:
        graph[a].add(b)
        graph[b].add(a)
    out = []
    remaining = set(vertices)
    while remaining:
        root = min(remaining)
        seen = {root}
        todo = [root]
        while todo:
            a = todo.pop()
            for b in graph[a] - seen:
                seen.add(b)
                todo.append(b)
        remaining -= seen
        out.append(seen)
    return out

def canonical_edges(edges):
    return frozenset((frozenset((a, b)) for (a, b) in edges))

def resolve_pattern(edges, cap_pairs):
    graph = {}
    for (a, b) in list(edges) + list(cap_pairs):
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
    assert all((len(v) in (1, 2) for v in graph.values()))
    ends = sorted((v for v in graph if len(graph[v]) == 1))
    seen = set()
    out = []
    for start in ends:
        if start in seen:
            continue
        (current, previous) = (start, None)
        while True:
            seen.add(current)
            options = [x for x in graph[current] if x != previous]
            if previous is not None and len(graph[current]) == 1:
                out.append((start, current))
                break
            assert len(options) == 1
            (previous, current) = (current, options[0])
    closed = []
    unused = set(graph) - seen
    while unused:
        root = min(unused)
        comp = {root}
        todo = [root]
        while todo:
            a = todo.pop()
            assert len(graph[a]) == 2
            for b in graph[a]:
                if b not in comp:
                    comp.add(b)
                    todo.append(b)
        unused -= comp
        closed.append(comp)
    return (out, closed)

def reflection_checks(max_n=64):
    checked = 0
    for n in range(2, max_n + 1, 2):
        for cp in range(1, n, 2):
            for cm in range(1, n, 2):
                pairs = [(i, (cp - i) % n) for i in range(n)]
                pairs += [(i, (cm - i) % n) for i in range(n)]
                assert all((a != b and (a - b) % 2 for (a, b) in pairs))
                cc = components(range(n), pairs)
                g = gcd(n, cp - cm)
                assert len(cc) == g // 2
                assert {len(c) for c in cc} == {2 * n // g}
                for c in cc:
                    boundary = len(c)
                    chi = -len(c)
                    assert (2 - boundary - chi) // 2 == 1
                    assert sum(((-1) ** i for i in c)) == 0
                checked += 1
    return checked

def packet(k, word):
    q = len(word)
    (labels, signs) = ([], [])
    for root in range(2 * k):
        order = range(q) if root % 2 == 0 else range(q - 1, -1, -1)
        labels.extend(order)
        signs.extend((word[j] * (-1 if root % 2 else 1) for j in order))
    return (labels, signs)

def packet_checks():
    checked = 0
    for k in range(1, 9):
        for q in range(1, 7):
            n = 2 * k * q
            for w in product((1, -1), repeat=q):
                (labels, signs) = packet(k, w)
                for c in (2 * q - 1, 4 * q - 1):
                    for i in range(n):
                        j = (c - i) % n
                        assert labels[j] == labels[i]
                        assert signs[j] == -signs[i]
                checked += 1
    return checked

def family_checks(max_q=40):
    steps = 0
    for q in range(1, max_q + 1):
        a = lambda j: j
        b = lambda j: 2 * q - 1 - j
        c = lambda j: 2 * q + j
        d = lambda j: 4 * q - 1 - j
        actual = {a(q - 1), b(0), c(0), d(q - 1)}
        assert len(actual) == 4
        (labels, signs) = packet(2, (1,) * q)
        assert [signs[i] for i in sorted(actual)] == [1, -1, 1, -1]
        returns = [(a(j), b(j + 1)) for j in range(q - 1)]
        returns += [(c(j + 1), d(j)) for j in range(q - 1)]
        assert len(components(range(q), [(labels[x], labels[y]) for (x, y) in returns])) == 1
        assert (2 - 4 - -4 * q) // 2 == 2 * q - 1
        for (x, y) in returns:
            assert signs[x] == -signs[y]
            assert sum((min(x, y) < u < max(x, y) for u in actual)) in (1, 3)
        edges = [(('o', x), ('o', y)) for (x, y) in returns]
        edges += [(('o', i), ('a', i)) for i in actual]
        for j in range(q):
            if j:
                assert sum((b(j) < u < c(j) for u in actual)) == 2
            caps = [(('o', b(j)), ('o', c(j))), (('o', d(j)), ('o', a(j)))]
            (edges, closed) = resolve_pattern(edges, caps)
            assert len(closed) == (0 if j == 0 else 1)
            jj = j + 1
            expected = [(('a', b(0)), ('a', c(0)))]
            if jj == q:
                expected += [(('a', a(q - 1)), ('a', d(q - 1)))]
            else:
                expected += [(('o', b(jj)), ('o', c(jj)))]
                expected += [(('o', a(i)), ('o', b(i + 1))) for i in range(jj, q - 1)]
                expected += [(('o', c(i + 1)), ('o', d(i))) for i in range(jj, q - 1)]
                expected += [(('o', a(q - 1)), ('a', a(q - 1))), (('o', d(q - 1)), ('a', d(q - 1)))]
            assert canonical_edges(edges) == canonical_edges(expected)
            assert {e for pair in edges for e in pair if e[0] == 'a'} == {('a', i) for i in actual}
            steps += 1
    return dict(families=max_q, exact_resolution_steps=steps)

def retain_actual_components(edges, labels, surviving):
    qe = []
    anchored = set()
    for (x, y) in edges:
        if x[0] == y[0] == 'o':
            qe.append((labels[x[1]], labels[y[1]]))
        elif x[0] == 'o':
            anchored.add(labels[x[1]])
        elif y[0] == 'o':
            anchored.add(labels[y[1]])
    keep = set()
    for cc in components(surviving, qe):
        if cc & anchored:
            keep |= cc
    return [(x, y) for (x, y) in edges if x[0] == 'a' or y[0] == 'a' or labels[x[1]] in keep]

def obstruction_checks():
    (q, k) = (4, 2)
    w = (1, 1, -1, 1)
    (labels, signs) = packet(k, w)
    actual = {0, 2, 6, 9}
    returns = [(1, 15), (3, 14), (4, 13), (5, 12), (7, 11), (8, 10)]
    assert [sum((a < u < b for u in actual)) for (a, b) in returns] == [3, 2, 2, 2, 1, 1]
    assert all((signs[a] == -signs[b] for (a, b) in returns))
    assert sum((signs[i] for i in actual)) == 0
    qe = [(labels[a], labels[b]) for (a, b) in returns]
    assert len(components(range(q), qe)) == 1
    for j in range(len(qe)):
        assert len(components(range(q), qe[:j] + qe[j + 1:])) == 1
    assert (2 - 4 - -2 * k * q) // 2 == 7
    edges = [(('o', a), ('o', b)) for (a, b) in returns]
    edges += [(('o', i), ('a', i)) for i in actual]
    moves = [('first end', {0}, [(7, 8), (15, 0)], (10, 11)), ('last end', {3}, [(3, 4), (11, 12)], (13, 14)), ('pair (1,2)', {1, 2}, [(1, 2), (5, 6), (9, 10), (13, 14)], (3, 4)), ('pair (2,3)', {2, 3}, [(2, 3), (4, 5), (10, 11), (12, 13)], (7, 8))]
    report = []
    for (name, removed, caps, witness) in moves:
        cap_pairs = [(('o', a), ('o', b)) for (a, b) in caps]
        assert {e[1] for pair in cap_pairs for e in pair} == {i for (i, l) in enumerate(labels) if l in removed}
        (out, closed) = resolve_pattern(edges, cap_pairs)
        out = retain_actual_components(out, labels, set(range(q)) - removed)
        needed = frozenset((('o', witness[0]), ('o', witness[1])))
        assert needed in canonical_edges(out)
        assert sum((witness[0] < u < witness[1] for u in actual)) == 0
        assert witness[1] == witness[0] + 1
        assert {e for pair in out for e in pair if e[0] == 'a'} == {('a', i) for i in actual}
        report.append(dict(operation=name, surviving_empty_return=list(witness), copies=[labels[i] for i in witness], closed_annular_cycles=len(closed)))
    repairs = []
    for (name, cap_numbers, survivor) in [('first-end closure', [(7, 8), (15, 0), (2, 3), (4, 5), (10, 11), (12, 13)], 1), ('last-end closure', [(3, 4), (11, 12), (1, 2), (5, 6), (9, 10), (13, 14)], 0)]:
        (out, closed) = resolve_pattern(edges, [(('o', a), ('o', b)) for (a, b) in cap_numbers])
        out = retain_actual_components(out, labels, {survivor})
        assert len(out) == 4 and all(({a[0], b[0]} == {'o', 'a'} for (a, b) in out))
        assert {labels[e[1]] for pair in out for e in pair if e[0] == 'o'} == {survivor}
        assert {e[1] for pair in out for e in pair if e[0] == 'a'} == actual
        repairs.append(dict(operation=name, surviving_copy=survivor, companion_count=1, actual_tethers=4, genus=1, closed_annular_cycles=len(closed)))
    heights = [0]
    for sign in w:
        heights.append(heights[-1] + sign)
    assert max(heights) - min(heights) == 2
    return dict(raw_moves=report, same_side_repairs=repairs, original_height_range=2)

def main():
    result = dict(status='PASS — finite combinatorial assertions only', reflection_parameter_pairs=reflection_checks(), signed_reference_packets=packet_checks(), coherent_family=family_checks(), connected_genus_seven_obstruction=obstruction_checks(), topology_not_certified=['ordinary isotopy and zero-loop quotient', 'minimum cyclic width', 'compression existence or compatibility', 'relative annular carrier and contractibility'])
    print(json.dumps(result, ensure_ascii=False, indent=2))
if __name__ == '__main__':
    main()
