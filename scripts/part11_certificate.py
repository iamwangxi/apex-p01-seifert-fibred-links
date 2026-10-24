from __future__ import annotations
#!/usr/bin/env python3
# Finite exact diagnostic for Part 11 of the proof; standard library only; prints a deterministic report and writes no files.
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from math import gcd
from pathlib import Path
import json
import runpy
import time
BASE = Path(__file__).resolve().parent
M = runpy.run_path(str(BASE / 'part11_star.py'))

@dataclass(frozen=True)
class GeneralVertex:
    r: int
    bmask: int
    d: int
    z: tuple

    @property
    def n(self):
        return 2 * self.r

    @property
    def axes(self):
        return (0,) + tuple((self.d if self.bmask & 1 << i else 0 for i in range(len(self.z))))

    @property
    def lifts(self):
        return (0,) + tuple((a + self.n * z for (a, z) in zip(self.axes[1:], self.z)))

    @property
    def signs(self):
        return M['sign_word'](self.r, self.axes)

def normal_types(ports, rmax):
    zz = (0,) * (ports - 1)
    yield GeneralVertex(1, 0, 0, zz)
    for r in range(2, rmax + 1):
        for d in range(1, 2 * r):
            if gcd(d, r) != 1 or (d + r) % 2 != 1:
                continue
            for b in range(1, 2 ** (ports - 1)):
                yield GeneralVertex(r, b, d, zz)

def geometric(u, v):
    for w in M['port0_orders']((u.r, v.r)):
        pos = {x: j for (j, x) in enumerate(w)}
        if all((M['fits_port']((u, v), pos, e) for e in range(1, len(u.axes)))):
            if u != v:
                assert M['oscillation']((u, v), w) == 1, (u, v, w)
            return True
    return False

def multiport_order_check(ports, rmax, all_phases):
    vv = list(normal_types(ports, rmax))
    phases = list(product((-1, 0, 1), repeat=ports - 1)) if all_phases else [(0,) * (ports - 1)]
    count = positive = 0
    for u in vv:
        assert u.signs is not None
        for v0 in vv:
            for z in phases:
                v = GeneralVertex(v0.r, v0.bmask, v0.d, z)
                predicted = all((abs(v.r * a - u.r * b) <= 1 for (a, b) in zip(u.lifts, v.lifts)))
                actual = geometric(u, v)
                assert actual == predicted, (u, v, actual, predicted)
                count += 1
                positive += actual
    return dict(ports=ports, rmax=rmax, phase_vectors=len(phases), normal_types=len(vv), pair_queries=count, disjoint_including_equal=positive)

def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    i = 0
    for j in range(len(a[0])):
        found = next((h for h in range(i, len(a)) if a[h][j]), None)
        if found is None:
            continue
        (a[i], a[found]) = (a[found], a[i])
        pivot = a[i][j]
        a[i] = [x / pivot for x in a[i]]
        for h in range(len(a)):
            if h != i and a[h][j]:
                c = a[h][j]
                a[h] = [x - c * y for (x, y) in zip(a[h], a[i])]
        i += 1
        if i == len(a):
            break
    return i

def central_certificates():
    count = 0
    examples = []
    for n in range(3, 11):
        for p in range(2, 17):
            for q in range(1, 25):
                if gcd(p, q) != 1:
                    continue
                linking = [[0 if i == j else p if 0 in (i, j) else 1 for j in range(n)] for i in range(n)]
                b = [[linking[i][j] if i != j else -sum(linking[i]) for j in range(n)] for i in range(n)]
                assert all((sum(row) == 0 for row in b))
                assert rank(b) == n - 1
                h = []
                for j in range(1, n):
                    row = [1] * n
                    row[j] -= p + n - 1
                    h.append(row)
                h.append([q] + [p] * (n - 1))
                assert rank(h) == n
                w = [[-(n - 1), 1], [p, 1]]
                assert rank(w) == 2
                assert p - q != 0
                a = (p + n - 1) * (n - 2) + (p - 1) * (q + n - 1)
                assert a > 0 and (a + 2 - n) % 2 == 0
                count += 1
                if (n, p, q) in ((3, 2, 1), (3, 2, 3), (4, 3, 2)):
                    examples.append(dict(n=n, p=p, q=q, chi_R=-a, genus_R=(a + 2 - n) // 2, boundaries=n, JSJ_blocks=n + 2))
    return dict(certificates=count, n_range=[3, 10], p_range=[2, 16], q_range=[1, 24], examples=examples)

def component_checks():
    count = 0
    for n in range(3, 8):
        for v in normal_types(n, 12):
            r = v.r
            seen = set()
            comps = []
            for j in range(v.n):
                if j in seen:
                    continue
                (stack, nodes, ends) = ([j], set(), [])
                while stack:
                    h = stack.pop()
                    if h in nodes:
                        continue
                    nodes.add(h)
                    for (e, a) in enumerate(v.axes):
                        if h == a:
                            assert v.signs[h] == 1
                            ends.append((e, 1))
                        elif h == (a + r) % v.n:
                            assert v.signs[h] == -1
                            ends.append((e, -1))
                        else:
                            k = (2 * a - h) % v.n
                            assert v.signs[k] == -v.signs[h]
                            stack.append(k)
                seen |= nodes
                assert ends
                comps.append((len(nodes), len(ends)))
            assert len(comps) == 2
            assert all((nodes == r for (nodes, _) in comps))
            if r % 2:
                assert sorted((b for (_, b) in comps)) == [n, n]
            else:
                k = bin(v.bmask).count('1')
                assert sorted((b for (_, b) in comps)) == sorted((2 * k, 2 * (n - k)))
            count += 1
    return dict(n_range=[3, 7], rmax=12, normal_types=count)

def pillowcase_coordinates(rmax=64):
    count = 0
    for r in range(1, rmax + 1):
        dd = [0] if r == 1 else [d for d in range(1, 2 * r) if gcd(d, r) == 1 and (d + r) % 2]
        for d in dd:
            for z in range(-2, 3):
                p = d + 2 * r * z
                (cx, cy) = (Fraction(1, 2), 0) if p % 2 == 0 else (0, Fraction(1, 2))
                points = []
                for k in range(r):
                    points.append(-p * (Fraction(k) + Fraction(1, 4)) / r % 1)
                    points.append((cx - p * (Fraction(k) + Fraction(1, 4) - cy) / r) % 1)
                points = sorted(points)
                assert len(set(points)) == 2 * r
                assert all(((points[(j + 1) % (2 * r)] - points[j]) % 1 == Fraction(1, 2 * r) for j in range(2 * r)))
                ep = -Fraction(p, 4 * r) % 1
                fp = Fraction(p, 4 * r) % 1
                assert (points.index(fp) - points.index(ep)) % (2 * r) == d
                assert (p + r) % 2
                count += 1
    return dict(rmax=rmax, relative_turns=[-2, 2], exact_rational_coordinate_checks=count)

def finite_graph(rmax, zmax):
    vv = [None] + M['vertices'](rmax, zmax)
    idx = {v: i for (i, v) in enumerate(vv)}
    uf = M['UnionFind'](len(vv))
    adj = [set() for _ in vv]
    for (j, v) in enumerate(vv[1:], 1):
        for w in set(M['finite_neighbors'](v, rmax)):
            i = idx.get(w)
            if i is None or i >= j:
                continue
            assert uf.join(i, j), (v, w)
            adj[i].add(j)
            adj[j].add(i)
    return (vv, idx, uf, adj)

def exchange_and_H0():
    (vv, _, _, adj) = finite_graph(16, 1)
    intervals = {}
    for (c, neighbors) in enumerate(adj):
        for (i, j) in combinations(sorted(neighbors), 2):
            assert j not in adj[i]
            if (i, j) in intervals:
                assert intervals[i, j] == c
            intervals[i, j] = c
            complexity = lambda k: 0 if vv[k] is None else 6 * vv[k].r
            assert complexity(c) < max(complexity(i), complexity(j))
    h0 = []
    for zmax in range(3):
        source = [None] + M['vertices'](16, zmax)
        (target, idx, uf, _) = finite_graph(16, zmax + 1)
        images = {uf.find(idx[v]) for v in source}
        assert len(images) == 1
        h0.append(dict(rmax=16, source_zmax=zmax, target_zmax=zmax + 1, source_vertices=len(source), target_vertices=len(target), target_components=uf.components, reduced_H0_image_rank=len(images) - 1))
    return dict(two_intervals=len(intervals), finite_vertices=len(vv), N1_N2_pass=True, reduced_H0_phase_inclusions=h0)

def constructive_parent_witnesses(rmax=64):
    count = width_checks = 0
    for r in range(2, rmax + 1):
        for v in M['types'](r):
            w = M['parent'](v)
            (tau, k, p) = M['sector'](v)
            s = w.r
            q = w.a2 + w.n * w.z2 if tau == 0 else w.a1 + w.n * w.z1
            assert abs(p * s - q * r) == 1
            points = []
            for (i, (a, n)) in enumerate(((p, r), (q, s))):
                points.extend((((-Fraction(a, 4 * n) + Fraction(j, 2 * n)) % 1, i, j) for j in range(2 * n)))
            points.sort()
            assert len({x for (x, _, _) in points}) == len(points)
            order = tuple(((i, j) for (_, i, j) in points))
            cut = next((t for (t, (i, j)) in enumerate(order) if j == 0 and order[(t + 1) % len(order)][1] == 0))
            order = order[cut:] + order[:cut]
            pos = {x: j for (j, x) in enumerate(order)}
            assert all((M['fits_port']((v, w), pos, e) for e in range(3))), (v, w, order)
            assert M['oscillation']((v, w), order) == 1
            count += 1
            width_checks += 1
    return dict(rmax=rmax, parent_edges=count, explicit_port_order_witnesses=count, original_Phi_width_one=width_checks, max_port_trace=2 * rmax)

def main():
    start = time.monotonic()
    out = dict(central_certificates=central_certificates(), components=component_checks(), pillowcase=pillowcase_coordinates(), exchange_and_H0=exchange_and_H0(), constructive_parents=constructive_parent_witnesses())
    print('linear certificates and component graphs checked', flush=True)
    out['multiport_orders'] = [multiport_order_check(4, 3, True), multiport_order_check(5, 3, False), multiport_order_check(6, 2, False)]
    print(json.dumps(out, indent=2))
if __name__ == '__main__':
    main()
