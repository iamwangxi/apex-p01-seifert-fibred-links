#!/usr/bin/env python3
"""Offline standard-library diagnostic; original calculation functions retained."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from math import floor, gcd
N = Counter()

def osc(u):
    return max(u) - min(u)

def norm(u):
    return tuple((x - u[0] for x in u))

def bary(dist):
    size = len(next(iter(dist)))
    return tuple((sum((c * v[i] for (v, c) in dist.items())) for i in range(size)))

def decode(u):
    u = norm(u)
    cuts = {F(0), F(1)}
    for x in u:
        frac = x - floor(x)
        if frac:
            cuts.add(1 - frac)
    cuts = sorted(cuts)
    out = defaultdict(F)
    for (left, right) in zip(cuts, cuts[1:]):
        theta = (left + right) / 2
        out[tuple((floor(x + theta) for x in u))] += right - left
    return dict(out)

def rows_flow(u, rows):
    return tuple((m + u[l] - u[r] for (l, r, m, cap) in rows))

def compositions(total, length):
    if length == 1:
        yield (total,)
    else:
        for a in range(total + 1):
            for tail in compositions(total - a, length - 1):
                yield ((a,) + tail)

def cliques(vertices):
    for size in range(1, len(vertices) + 1):
        for vv in combinations(vertices, size):
            if all((osc(tuple((a - b for (a, b) in zip(v, w)))) <= 1 for (v, w) in combinations(vv, 2))):
                yield vv

def verify_point(u, rows, check_demands):
    d = decode(u)
    assert sum(d.values()) == 1
    assert bary(d) == norm(u)
    for v in d:
        w = rows_flow(v, rows)
        assert all((0 <= a <= row[3] for (a, row) in zip(w, rows)))
        check_demands(w)
    assert all((osc(tuple((a - b for (a, b) in zip(v, w)))) <= 1 for (v, w) in combinations(d, 2)))
    for shift in (F(-11, 7), F(2, 3), F(3)):
        assert decode(tuple((x + shift for x in u))) == d
    shift = (0, -3, 2)
    translated = decode(tuple((x - a for (x, a) in zip(norm(u), shift))))
    restored = {norm(tuple((x + a for (x, a) in zip(v, shift)))): c for (v, c) in translated.items()}
    assert restored == d
    N['rational_points'] += 1

def strip_test():
    rows = ((1, 0, 0, 1), (0, 1, 1, 1), (1, 0, 0, 1), (0, 1, 1, 1), (0, 0, 1, 1), (2, 2, 1, 1), (2, 2, 1, 1))

    def demands(w):
        (ja, da, dc, jc, jb, e, f) = w
        assert ja + da == dc + jc == jb == e == f == 1
        assert ja + jc + jb == 2 and da + dc == 1
    vertices = tuple(((0, x, t) for x in (0, 1) for t in range(-2, 3)))
    assert len({rows_flow(v, rows) for v in vertices}) == 2
    assert len(vertices) == 10
    edges = [(v, w) for (v, w) in combinations(vertices, 2) if osc(tuple((a - b for (a, b) in zip(v, w)))) == 1]
    simplexes = list(cliques(vertices))
    assert Counter(map(len, simplexes)) == {1: 10, 2: 17, 3: 8}
    assert 10 - 17 + 8 == 1
    for x in (0, 1):
        for (n, m) in combinations(range(-2, 3), 2):
            assert osc((0, 0, n - m)) == abs(n - m)
    for vv in simplexes:
        for denominator in (3, 5):
            for numerators in compositions(denominator, len(vv)):
                d = {v: F(a, denominator) for (v, a) in zip(vv, numerators) if a}
                assert decode(bary(d)) == d
                N['strip_exact_simplex_recovery'] += 1
    for (a, b) in product(range(9), range(-16, 17)):
        u = (F(0), F(a, 8), F(b, 8))
        verify_point(u, rows, demands)
        if a in (0, 8):
            small = decode((F(0), F(b, 8)))
            expanded = {(0, a // 8, v[1]): c for (v, c) in small.items()}
            assert decode(u) == expanded
            N['strip_zero_faces'] += 1
        for t in (F(0), F(1, 3), F(1)):
            c = tuple(((1 - t) * z for z in u))
            verify_point(c, rows, demands)
            if t == 1:
                assert decode(c) == {(0, 0, 0): F(1)}
            N['strip_supported_contraction'] += 1
    (bad_left, bad_right) = ((0, 1, 0), (0, 0, 1))
    assert osc(tuple((a - b for (a, b) in zip(bad_left, bad_right)))) == 2
    assert decode((F(0), F(1, 2), F(1, 2))) == {(0, 0, 0): F(1, 2), (0, 1, 1): F(1, 2)}
    N['strip_vertices'] = len(vertices)
    N['strip_edges'] = len(edges)
    N['strip_triangles'] = sum((len(s) == 3 for s in simplexes))

def band_level_read(u):
    (_, a, b) = u
    cuts = sorted({F(0), F(1), a, b})
    out = defaultdict(F)
    for (lo, hi) in zip(cuts, cuts[1:]):
        if lo == hi:
            continue
        r = (lo + hi) / 2
        ma = sum((0 < r + k < a for k in range(-2, 3)))
        mb = sum((0 < r + k < b for k in range(-2, 3)))
        na = sum((a < r + k < 1 for k in range(-2, 3)))
        nb = sum((b < r + k < 1 for k in range(-2, 3)))
        assert ma + na == mb + nb == 1
        out[0, ma, mb] += hi - lo
    return dict(out)

def cone_test():
    assert 6 * (2 - 2) == 0 and 6 * 2 - 2 == 10
    assert gcd(2, 12) == 2 and abs(6 - 1) == 5
    rows = ((1, 0, 0, 1), (0, 1, 1, 1), (2, 0, 0, 1), (0, 2, 1, 1), (0, 0, 1, 1), (0, 0, 1, 1))

    def demands(w):
        assert w[0] + w[1] == w[2] + w[3] == w[4] == w[5] == 1
        assert w[4] + w[5] == 2
    vertices = tuple(((0, a, b) for (a, b) in product((0, 1), repeat=2)))
    simplexes = list(cliques(vertices))
    assert Counter(map(len, simplexes)) == {1: 4, 2: 5, 3: 2}
    for (a, b) in product(range(13), repeat=2):
        u = (F(0), F(a, 12), F(b, 12))
        verify_point(u, rows, demands)
        assert band_level_read(u) == decode(u)
        N['cone_band_level_decode'] += 1
        if a in (0, 12) or b in (0, 12):
            if a in (0, 12):
                expected = {(0, a // 12, v[1]): c for (v, c) in decode((F(0), F(b, 12))).items()}
            else:
                expected = {(0, v[1], b // 12): c for (v, c) in decode((F(0), F(a, 12))).items()}
            assert decode(u) == expected
            N['cone_zero_faces'] += 1
    for nn in compositions(8, 4):
        d = {v: F(n, 8) for (v, n) in zip(vertices, nn) if n}
        u = bary(d)
        rd = decode(u)
        assert decode(bary(rd)) == rd
        on_x = all((osc(tuple((a - b for (a, b) in zip(v, w)))) <= 1 for (v, w) in combinations(d, 2)))
        assert (rd == d) == on_x
        for t in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1)):
            hd = defaultdict(F)
            for (v, c) in d.items():
                hd[v] += (1 - t) * c
            for (v, c) in rd.items():
                hd[v] += t * c
            hd = {v: c for (v, c) in hd.items() if c}
            assert set(hd) <= set(vertices)
            assert sum(hd.values()) == 1 and bary(hd) == u
            assert decode(bary(hd)) == rd
            if on_x:
                assert hd == d
            N['cone_SDR_checks'] += 1
        N['cone_Y_grid_points'] += 1
    anti = {(0, 0, 1): F(1, 2), (0, 1, 0): F(1, 2)}
    assert decode(bary(anti)) == {(0, 0, 0): F(1, 2), (0, 1, 1): F(1, 2)}
    assert {tuple((w[0] + w[1], w[2] + w[3])) for w in (rows_flow(v, rows) for v in vertices)} == {(1, 1)}
    N['cone_vertices'] = len(vertices)
    N['cone_X_edges'] = sum((len(s) == 2 for s in simplexes))
    N['cone_X_triangles'] = sum((len(s) == 3 for s in simplexes))
    N['cone_Y_tetrahedra'] = 1

def hopf_line_test():
    (a0, a1, a2) = (0, 2, 2)
    k = (-(a0 + a1 + a2), a1 - a0 - a2, a2 - a0 - a1)
    assert k == (-4, 0, 0)
    assert gcd(a1, a0 + a2) == gcd(a2, a0 + a1) == 2
    for (n, m) in product(range(-5, 6), repeat=2):
        assert osc((0, n - m)) == abs(n - m)
        if n != m:
            assert (osc((0, n - m)) == 1) == (abs(n - m) == 1)
        N['Hopf_line_pairs'] += 1
    for a in range(-60, 61):
        x = F(a, 12)
        d = decode((F(0), x))
        assert sum(d.values()) == 1 and bary(d) == (0, x)
        assert set(d) <= {(0, floor(x)), (0, floor(x) + 1)}
        N['Hopf_line_rounding'] += 1

def collar_test():
    for q in (1, 2, 3):
        for aa in product((F(-1, 2), F(0), F(1, 3), F(1)), repeat=q):
            if not all((1 + aa[(j + 1) % q] - aa[j] > 0 for j in range(q))):
                continue
            (lo, hi) = (floor(min(aa)), -floor(-max(aa)))
            c = F(lo + hi, 2)
            for chi in (F(0), F(1, 3), F(1)):
                vv = tuple((c + chi * (a - c) for a in aa))
                assert all((1 + vv[(j + 1) % q] - vv[j] > 0 for j in range(q)))
                for (j, t) in product(range(q), (F(1, 4), F(1, 2), F(3, 4))):
                    g = (1 - t) * vv[j] + t * (1 + vv[(j + 1) % q])
                    assert lo <= floor(g) <= hi
                    N['collar_index_checks'] += 1

def tree_quotient_test():
    for size in range(2, 7):
        for code in product(range(size), repeat=size - 2):
            degree = [1] * size
            for v in code:
                degree[v] += 1
            edges = []
            for v in code:
                leaf = next((i for i in range(size) if degree[i] == 1))
                edges.append((leaf, v))
                degree[leaf] -= 1
                degree[v] -= 1
            last = [i for i in range(size) if degree[i] == 1]
            edges.append(tuple(last))
            adjacency = [[] for _ in range(size)]
            for (a, b) in edges:
                adjacency[a].append(b)
                adjacency[b].append(a)
            color = {0: 0}
            todo = [0]
            while todo:
                v = todo.pop()
                for w in adjacency[v]:
                    if w not in color:
                        color[w] = 1 - color[v]
                        todo.append(w)
            for zero_color in (0, 1):
                zeros = [i for i in range(size) if color[i] == zero_color]
                clusters = [i for i in range(size) if i not in zeros]
                directed = [(a, b) if a in zeros else (b, a) for (a, b) in edges]
                assignments = {edge: 3 * i - 2 * size for (i, edge) in enumerate(directed)}

                def solve(values):
                    height = {zeros[0]: 0}
                    while len(height) < size:
                        for ((a, b), n) in values.items():
                            if a in height and b not in height:
                                height[b] = height[a] - n
                            elif b in height and a not in height:
                                height[a] = height[b] + n
                    assert all((height[a] - height[b] == n for ((a, b), n) in values.items()))
                    return height
                original = solve(assignments)
                changed = {edge: n + (edge[1] + 1) * 7 for (edge, n) in assignments.items()}
                other = solve(changed)
                assert all((original[z] == other[z] for z in zeros))
                stars = [{i for (i, e) in enumerate(directed) if e[1] == c} for c in clusters]
                assert all(stars) and sum(map(len, stars)) == len(edges)
                assert all((not a & b for (a, b) in combinations(stars, 2)))
                assert len(edges) - len(clusters) == len(zeros) - 1
                N['bipartite_tree_quotients'] += 1

if __name__ == '__main__':
    import contextlib
    import io
    import json
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        tree_quotient_test()
        hopf_line_test()
        strip_test()
        cone_test()
        collar_test()
        for (key, value) in sorted(N.items()):
            print(f'{key}: {value}')
        print('PASS: finite support and band-level arithmetic; topology and template stability require the written proofs.')
    print(json.dumps({'scope': 'Finite diagnostics; not a topology certificate.', 'output': captured.getvalue().splitlines()}, indent=2, sort_keys=True))
