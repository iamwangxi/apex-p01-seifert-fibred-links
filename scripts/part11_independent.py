from __future__ import annotations
#!/usr/bin/env python3
# Finite exact diagnostic for Part 11 of the proof; standard library only; prints a deterministic report and writes no files.
from collections import deque
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
from math import gcd
from pathlib import Path
import argparse
import json
import time
BASE = Path(__file__).resolve().parent.parent

def admissible(r, d):
    return 0 < d < 2 * r and gcd(r, d) == 1 and ((r + d) % 2 == 1)

@lru_cache(None)
def shape_data(r, ports=3):
    if r == 1:
        return ((0,) * ports,)
    return tuple(((0,) + tuple((d if mask & 1 << i else 0 for i in range(ports - 1))) for d in range(1, 2 * r) if admissible(r, d) for mask in range(1, 2 ** (ports - 1))))

@lru_cache(None)
def signs(r, axes):
    n = 2 * r
    result = [0] * n
    todo = []
    for a in axes:
        for (j, value) in ((a, 1), ((a + r) % n, -1)):
            assert result[j] in (0, value)
            result[j] = value
            todo.append(j)
    while todo:
        j = todo.pop()
        for a in axes:
            k = (2 * a - j) % n
            if k == j:
                continue
            if result[k]:
                assert result[k] == -result[j]
            else:
                result[k] = -result[j]
                todo.append(k)
    assert 0 not in result and sum(result) == 0
    return tuple(result)

def components(r, axes):
    unseen = set(range(2 * r))
    result = []
    while unseen:
        todo = [min(unseen)]
        (nodes, ends) = (set(), [])
        while todo:
            j = todo.pop()
            if j in nodes:
                continue
            nodes.add(j)
            for (i, a) in enumerate(axes):
                if j == a:
                    ends.append((i, 1))
                elif j == (a + r) % (2 * r):
                    ends.append((i, -1))
                else:
                    todo.append((2 * a - j) % (2 * r))
        unseen -= nodes
        result.append((nodes, ends))
    return result

def raw_signed_catalogue(rmax=9):
    words = reduced = checks = 0
    for r in range(1, rmax + 1):
        seen = {n: set() for n in (3, 4, 5)}
        for positive in combinations(range(2 * r), r):
            word = tuple((1 if j in positive else -1 for j in range(2 * r)))
            axes = [a for a in range(2 * r) if word[a] == 1 and word[(a + r) % (2 * r)] == -1 and all((j in (a, (a + r) % (2 * r)) or word[(2 * a - j) % (2 * r)] == -word[j] for j in range(2 * r)))]
            words += 1
            assert len(axes) <= 2, (r, word, axes)
            if 0 not in axes:
                continue
            for n in seen:
                for other in product(axes, repeat=n - 1):
                    aa = (0,) + other
                    cc = components(r, aa)
                    checks += 1
                    if any((not ends for (_, ends) in cc)):
                        continue
                    assert len(cc) == 2 and all((len(nodes) == r for (nodes, _) in cc))
                    assert signs(r, aa) == word
                    assert aa not in seen[n]
                    seen[n].add(aa)
                    reduced += 1
        for n in seen:
            assert seen[n] == set(shape_data(r, n)), (r, n, seen[n])
    return dict(rmax=rmax, balanced_words=words, raw_labelled_diagrams=checks, reduced_diagrams_3_to_5_ports=reduced)

def chord_test(order, rs, axes):
    pos = {label: j for (j, label) in enumerate(order)}
    N = len(order)
    plus = [pos[i, a % (2 * r)] for (i, (r, a)) in enumerate(zip(rs, axes))]
    minus = [pos[i, (a + r) % (2 * r)] for (i, (r, a)) in enumerate(zip(rs, axes))]
    marks = [kind for (_, kind) in sorted([(x, 1) for x in plus] + [(x, -1) for x in minus])]
    if sum((marks[j] != marks[(j + 1) % len(marks)] for j in range(len(marks)))) != 2:
        return False
    chords = []
    for (i, (r, a)) in enumerate(zip(rs, axes)):
        a %= 2 * r
        for j in range(2 * r):
            k = (2 * a - j) % (2 * r)
            if j >= k:
                continue
            (x, y) = sorted((pos[i, j], pos[i, k]))
            side_p = {x < t < y for t in plus}
            side_m = {x < t < y for t in minus}
            if len(side_p) != 1 or len(side_m) != 1 or side_p == side_m:
                return False
            chords.append((x, y))
    for ((a, b), (c, d)) in combinations(chords, 2):
        if (a < c < b) != (a < d < b):
            return False
    return True

def lift_window(order, rs, lifted_axes):
    pos = {label: j for (j, label) in enumerate(order)}
    N = len(order)
    lifted = []
    for (i, (r, a)) in enumerate(zip(rs, lifted_axes)):
        for j in range(a, a + 2 * r):
            (turn, residue) = divmod(j, 2 * r)
            lifted.append(pos[i, residue] + N * turn)
    return max(lifted) - min(lifted) < N

@lru_cache(None)
def all_port_zero_orders(r, s):
    N = 2 * (r + s)
    survivors = set()
    attempted = 0
    for remaining in combinations(range(1, N), 2 * r - 1):
        upos = (0,) + remaining
        holes = [j for j in range(N) if j not in upos]
        for offset in range(2 * s):
            raw = [None] * N
            for (j, t) in enumerate(upos):
                raw[t] = (0, j)
            for (j, t) in enumerate(holes):
                raw[t] = (1, (offset + j) % (2 * s))
            raw = tuple(raw)
            attempted += 1
            if not chord_test(raw, (r, s), (0, 0)):
                continue
            for cut in (raw.index((0, 0)), raw.index((1, 0))):
                order = raw[cut:] + raw[:cut]
                pos = {label: j for (j, label) in enumerate(order)}
                linear = all((pos[i, j] < pos[i, j + 1] for (i, size) in enumerate((2 * r, 2 * s)) for j in range(size - 1)))
                if linear and lift_window(order, (r, s), (0, 0)):
                    survivors.add(order)
    return (attempted, tuple(sorted(survivors)))

def edge_data(u, v):
    (r, *L) = u
    (s, *M) = v
    return u != v and all((abs(s * x - r * y) <= 1 for (x, y) in zip(L, M)))

def vertices(rmax, zmax=0, ports=3):
    return [(r,) + tuple((aa[i] + 2 * r * zz[i - 1] for i in range(1, ports))) for r in range(1, rmax + 1) for aa in shape_data(r, ports) for zz in product(range(-zmax, zmax + 1), repeat=ports - 1)]

def order_queries(rmax=4, ports=3, all_phases=True):
    base = vertices(rmax, 0, ports)
    phase_vectors = list(product((-1, 0, 1), repeat=ports - 1)) if all_phases else [(0,) * (ports - 1)]
    queries = positive = witnesses = distinct = 0
    for u in base:
        (r, *L) = u
        for v0 in base:
            (s, *M0) = v0
            for zz in phase_vectors:
                M = [m + 2 * s * z for (m, z) in zip(M0, zz)]
                v = (s,) + tuple(M)
                ok_orders = []
                for order in all_port_zero_orders(r, s)[1]:
                    if all((chord_test(order, (r, s), (a, b)) and lift_window(order, (r, s), (a, b)) for (a, b) in zip(L, M))):
                        ok_orders.append(order)
                predicted = u == v or edge_data(u, v)
                assert bool(ok_orders) == predicted, (u, v, ok_orders, predicted)
                queries += 1
                if ok_orders:
                    positive += 1
                    witnesses += len(ok_orders)
                    if u != v:
                        su = signs(r, (0,) + tuple((a % (2 * r) for a in L)))
                        sv = signs(s, (0,) + tuple((b % (2 * s) for b in M)))
                        widths = []
                        for order in ok_orders:
                            h = lo = hi = 0
                            for (member, j) in order:
                                h += su[j] if member == 0 else -sv[j]
                                (lo, hi) = (min(lo, h), max(hi, h))
                            assert h == 0
                            widths.append(hi - lo)
                        assert min(widths) == 1, (u, v, widths)
                        distinct += 1
    return dict(ports=ports, rmax=rmax, phase_vectors=len(phase_vectors), queries=queries, positive_including_equal=positive, full_order_witnesses=witnesses, distinct_min_width_one=distinct)

def decode(r, L):
    residues = tuple((x % (2 * r) for x in L))
    if r == 1:
        return all((x == 0 for x in residues))
    nonzero = set(residues) - {0}
    return len(nonzero) == 1 and admissible(r, next(iter(nonzero)))

@lru_cache(None)
def all_lower_neighbours(u):
    (r, *L) = u
    if r == 1:
        return (None,)
    result = []
    for s in range(1, r):
        intervals = []
        for x in L:
            lo = -(-(s * x - 1) // r)
            hi = (s * x + 1) // r
            if lo > hi:
                break
            intervals.append(range(lo, hi + 1))
        if len(intervals) != len(L):
            continue
        for M in product(*intervals):
            if decode(s, M):
                result.append((s,) + M)
    return tuple(result)

@lru_cache(None)
def path(u):
    if u is None:
        return (None,)
    lower = all_lower_neighbours(u)
    assert len(lower) == 1, (u, lower)
    return (u,) + path(lower[0])

def width_at_root(u):
    (r, *L) = u
    word = signs(r, (0,) + tuple((a % (2 * r) for a in L)))
    h = lo = hi = 0
    for eps in word:
        h += eps
        (lo, hi) = (min(lo, h), max(hi, h))
    return hi - lo

class UF:

    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def root(self, a):
        while a != self.parent[a]:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def join(self, a, b):
        (a, b) = (self.root(a), self.root(b))
        if a == b:
            return False
        self.parent[a] = b
        self.count -= 1
        return True

def induced_graph(vv, all_pairs=False):
    vv = [None] + sorted(set(vv) - {None})
    idx = {v: i for (i, v) in enumerate(vv)}
    adj = [set() for _ in vv]
    if all_pairs:
        for (i, j) in combinations(range(len(vv)), 2):
            (u, v) = (vv[i], vv[j])
            if v[0] == 1 if u is None else edge_data(u, v):
                adj[i].add(j)
                adj[j].add(i)
    else:
        for (j, v) in enumerate(vv[1:], 1):
            for u in all_lower_neighbours(v):
                i = idx.get(u)
                if i is not None:
                    adj[i].add(j)
                    adj[j].add(i)
    uf = UF(len(vv))
    E = 0
    for (j, nbr) in enumerate(adj):
        for i in nbr:
            if i < j:
                uf.join(i, j)
                E += 1
    b1 = E - len(vv) + uf.count
    triangles = sum((len(adj[i] & adj[j]) for j in range(len(vv)) for i in adj[j] if i < j)) // 3
    assert b1 == 0 and triangles == 0
    return (vv, adj, dict(vertices=len(vv), edges=E, betti_Z=[uf.count, b1, 0], rank_d1=len(vv) - uf.count, triangles=triangles))

def small_distance_check(rmax=6, zmax=1):
    raw = set(vertices(rmax, zmax))
    closed = {a for u in raw for a in path(u)}
    (vv, adj, stats) = induced_graph(closed, all_pairs=True)
    (_, other, _) = induced_graph(closed, all_pairs=False)
    assert adj == other
    pairs = 0
    for (i, u) in enumerate(vv):
        dist = {i: 0}
        q = deque([i])
        while q:
            j = q.popleft()
            for k in adj[j]:
                if k not in dist:
                    dist[k] = dist[j] + 1
                    q.append(k)
        assert len(dist) == len(vv)
        pu = path(u)
        for (j, v) in enumerate(vv):
            pv = path(v)
            pvpos = {a: k for (k, a) in enumerate(pv)}
            formula = next((k + pvpos[a] for (k, a) in enumerate(pu) if a in pvpos))
            assert formula == dist[j], (u, v, formula, dist[j])
            pairs += 1
        if u is not None:
            assert dist[0] == width_at_root(u)
    return dict(rmax=rmax, zmax=zmax, pair_distances=pairs, graph=stats)

def truncation_check(full=False):
    results = []
    for R in [4, 8, 16, 32, 64] if full else [4, 8, 16]:
        for Z in (0, 1, 2):
            vv = set(vertices(R, Z))
            (_, _, raw) = induced_graph(vv)
            closed = {a for u in vv for a in path(u)}
            (_, _, closure) = induced_graph(closed)
            assert closure['betti_Z'] == [1, 0, 0]
            results.append(dict(rmax=R, zmax=Z, raw=raw, closure=closure, added=len(closed) - len(vv) - 1))
    return results

def rank(a):
    a = [list(map(Fraction, row)) for row in a]
    k = 0
    for col in range(len(a[0])):
        pivot = next((j for j in range(k, len(a)) if a[j][col]), None)
        if pivot is None:
            continue
        (a[k], a[pivot]) = (a[pivot], a[k])
        scale = a[k][col]
        a[k] = [x / scale for x in a[k]]
        for j in range(len(a)):
            if j != k and a[j][col]:
                scale = a[j][col]
                a[j] = [x - scale * y for (x, y) in zip(a[j], a[k])]
        k += 1
        if k == len(a):
            break
    return k

def certificate_check():
    count = 0
    examples = []
    for n in range(3, 11):
        for p in range(2, 17):
            for q in range(1, 25):
                if gcd(p, q) != 1:
                    continue
                total = [[0, 1] + [-1] * (n - 1), [-p * (n - 1), p] + [0] * (n - 1)]
                for j in range(n - 1):
                    row = [p, 0] + [1] * (n - 1)
                    row[j + 2] -= p + n - 1
                    total.append(row)
                assert rank(total) == n
                eta = [1, n - 1] + [1] * (n - 1)
                assert all((sum((a * b for (a, b) in zip(row, eta))) == 0 for row in total))
                H = []
                for j in range(n - 1):
                    row = [1] + [1] * (n - 1)
                    row[j + 1] -= p + n - 1
                    H.append(row)
                H.append([q] + [p] * (n - 1))
                W = [[-p * (n - 1), p], [p, 1]]
                assert rank(H) == n and rank(W) == 2
                assert abs(p - q) > 0
                neg_chi = Fraction((p + n - 1) * (n - 2)) + Fraction(p * (q + n - 1) * (p - 1), p)
                genus = (neg_chi + 2 - n) / 2
                assert neg_chi > 0 and genus.denominator == 1
                if (n, p, q) == (3, 2, 1):
                    examples.append(dict(n=n, p=p, q=q, chi=-int(neg_chi), genus=int(genus)))
                count += 1
    negative_controls = 0
    for (n, p) in product(range(3, 9), range(2, 9)):
        H = []
        for j in range(n - 1):
            row = [1] * n
            row[j + 1] -= p + n - 1
            H.append(row)
        H.append([-(n - 1)] + [p] * (n - 1))
        assert rank(H) == n - 1
        negative_controls += 1
    return dict(positive_certificates=count, rejected_sign_controls=negative_controls, examples=examples)

def boundary_sign_check():
    signed_cases = 0
    for n in range(3, 9):
        for tail in product((-1, 1), repeat=n - 1):
            m = (1,) + tail
            M = sum(m)
            if M <= 0 or -1 not in m:
                continue
            B = [[1 - (M * m[i] if i == j else 0) for j in range(n)] for i in range(n)]
            assert rank(B) == n - 1
            assert all((sum((a * b for (a, b) in zip(row, m))) == 0 for row in B))
            framing = tuple((1 - M * x for x in m))
            assert all((abs(1 - f) == M for f in framing))
            assert all((gcd(abs(x), abs(M - x)) == 1 for x in m))
            assert (M - 1) * (n - 2) % 2 == 0
            signed_cases += 1
    m = (1, 1, -1)
    B = [[0, 1, 1], [1, 0, 1], [1, 1, 2]]
    assert rank(B) == 2
    rho = (0, 0, 1)
    vv = vertices(4, 1)
    for v in vv:
        (r, *L) = v
        word = signs(r, (0,) + tuple((x % (2 * r) for x in L)))
        actual_axes = tuple(((x + shift * r) % (2 * r) for (x, shift) in zip((0,) + tuple(L), rho)))
        assert tuple((word[a] for a in actual_axes)) == m
        assert all(((2 * a - j) % (2 * r) == (2 * b - j) % (2 * r) for (a, b) in zip(actual_axes, (0,) + tuple((x % (2 * r) for x in L))) for j in range(2 * r)))
    pairs = 0
    for (u, v) in combinations(vv, 2):
        (r, *L) = u
        (s, *N) = v
        actual_L = [x + shift * r for (x, shift) in zip(L, rho[1:])]
        actual_N = [x + shift * s for (x, shift) in zip(N, rho[1:])]
        assert [s * x - r * y for (x, y) in zip(L, N)] == [s * x - r * y for (x, y) in zip(actual_L, actual_N)]
        pairs += 1
    word = signs(2, (0, 1, 0))
    assert word == (1, 1, -1, -1)
    assert tuple((word[a] for a in (0, 1, 2))) == m
    assert all((ends for (_, ends) in components(2, (0, 1, 2))))
    return dict(mixed_signed_Hopf_certificates=signed_cases, explicit_example=dict(meridian_values=m, branch_framings=[0, 0, 2], boundary_matrix=B, fibre_degree=1, fibre_genus=0, r1_actual_positive_axes=[0, 0, 1], r2_actual_positive_axes=[0, 1, 2]), determinant_conjugacy_pairs=pairs, conclusion='literal actual-positive-axis catalogue needs fixed sign recoding')

def main():

    class args:
        full = False
    result = {'boundary': 'finite normal-data checks; no theorem about arbitrary embedded surfaces'}
    result['signed_catalogue'] = raw_signed_catalogue()
    print('raw signed catalogue passed', flush=True)
    result['planar_orders'] = [order_queries(), order_queries(3, 4), order_queries(3, 5, False), order_queries(2, 6, False)]
    result['cyclic_interleavings_examined'] = sum((all_port_zero_orders(r, s)[0] for (r, s) in product(range(1, 5), repeat=2)))
    print('independent chord planarity and integer lifts passed', flush=True)
    result['distances'] = small_distance_check()
    result['truncations'] = truncation_check(args.full)
    print('full determinant graphs, BFS distances and homology passed', flush=True)
    result['two_central_blocks'] = certificate_check()
    result['boundary_signs'] = boundary_sign_check()
    print(json.dumps(result, ensure_ascii=False, indent=2))
if __name__ == '__main__':
    main()
