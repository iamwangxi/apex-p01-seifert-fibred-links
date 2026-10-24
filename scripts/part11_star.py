from __future__ import annotations
#!/usr/bin/env python3
# Finite exact diagnostic for Part 11 of the proof; standard library only; prints a deterministic report and writes no files.
from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations, permutations, product
from math import gcd
import argparse
import json
import time

@dataclass(frozen=True, order=True)
class Vertex:
    r: int
    a1: int = 0
    a2: int = 0
    z1: int = 0
    z2: int = 0

    @property
    def n(self):
        return 2 * self.r

    @property
    def axes(self):
        return (0, self.a1, self.a2)

    @property
    def lifts(self):
        return (0, self.a1 + self.n * self.z1, self.a2 + self.n * self.z2)

    @property
    def signs(self):
        return sign_word(self.r, self.axes)

@lru_cache(None)
def sign_word(r, axes):
    n = 2 * r
    signs = {}
    stack = []
    for a in set(axes):
        for (j, s) in ((a, 1), ((a + r) % n, -1)):
            if j in signs and signs[j] != s:
                return None
            if j not in signs:
                signs[j] = s
                stack.append(j)
    while stack:
        j = stack.pop()
        for a in set(axes):
            k = (2 * a - j) % n
            if k == j:
                continue
            s = -signs[j]
            if k in signs and signs[k] != s:
                return None
            if k not in signs:
                signs[k] = s
                stack.append(k)
    if len(signs) != n:
        return None
    return tuple((signs[j] for j in range(n)))

def types(r):
    if r == 1:
        return [Vertex(1)]
    ans = []
    for d in range(1, 2 * r):
        if gcd(d, r) != 1 or (d + r) % 2 != 1:
            continue
        for (a1, a2) in ((0, d), (d, 0), (d, d)):
            v = Vertex(r, a1, a2)
            assert v.signs is not None
            ans.append(v)
    return ans

def vertices(rmax, zmax=0):
    return [Vertex(v.r, v.a1, v.a2, z1, z2) for r in range(1, rmax + 1) for v in types(r) for (z1, z2) in product(range(-zmax, zmax + 1), repeat=2)]

def shuffles(lengths, prefix=()):
    if not any(lengths):
        yield prefix
        return
    for (i, k) in enumerate(lengths):
        if k:
            ll = list(lengths)
            ll[i] -= 1
            j = sum((1 for (h, _) in prefix if h == i)) + 1
            yield from shuffles(tuple(ll), prefix + ((i, j),))

@lru_cache(None)
def port0_orders(rs):
    k = len(rs)
    ans = []
    for pp in permutations(range(k)):
        p = tuple(((i, 0) for i in pp))
        for u in shuffles(tuple((r - 1 for r in rs))):
            v = tuple(((i, 2 * rs[i] - j) for (i, j) in reversed(u)))
            for qq in permutations(range(k)):
                q = tuple(((i, rs[i]) for i in qq))
                ans.append(p + u + q + v)
    return tuple(ans)

@lru_cache(None)
def port0_positions(rs):
    return tuple(((w, {x: j for (j, x) in enumerate(w)}) for w in port0_orders(rs)))

def fits_port_slow(vs, pos, e):
    total = len(pos)

    def lifted_pos(i, j):
        (q, j0) = divmod(j, vs[i].n)
        return pos[i, j0] + q * total
    packets = [[], [], [], []]
    for (i, v) in enumerate(vs):
        a = v.lifts[e]
        packets[0].append((lifted_pos(i, a), i, a))
        packets[1].extend(((lifted_pos(i, a + j), i, a + j) for j in range(1, v.r)))
        packets[2].append((lifted_pos(i, a + v.r), i, a + v.r))
        packets[3].extend(((lifted_pos(i, a + j), i, a + j) for j in range(v.r + 1, v.n)))
    nonempty = [sorted(x) for x in packets if x]
    if any((x[-1][0] >= y[0][0] for (x, y) in zip(nonempty, nonempty[1:]))):
        return False
    if nonempty[-1][-1][0] >= nonempty[0][0][0] + total:
        return False
    u = sorted(packets[1])
    target = [(i, 2 * vs[i].lifts[e] + vs[i].n - j) for (_, i, j) in reversed(u)]
    actual = [(i, j) for (_, i, j) in sorted(packets[3])]
    return target == actual

def fits_port(vs, pos, e):
    (total, k) = (len(pos), len(vs))
    (pp, qq) = ([], [])
    for (i, v) in enumerate(vs):
        for (j, target) in ((v.lifts[e], pp), (v.lifts[e] + v.r, qq)):
            (turn, j0) = divmod(j, v.n)
            target.append(pos[i, j0] + turn * total)
    if max(pp) - min(pp) != k - 1 or max(qq) - min(qq) != k - 1:
        return False
    if max(pp) >= min(qq) or max(qq) >= min(pp) + total:
        return False
    return fits_port_slow(vs, pos, e)

def position_bounds(rs, i, j):
    (r, other) = (rs[i], rs[1 - i])
    (turn, j0) = divmod(j, 2 * r)
    if j0 == 0:
        (lo, hi) = (0, 1)
    elif j0 < r:
        (lo, hi) = (j0 + 1, j0 + other)
    elif j0 == r:
        (lo, hi) = (r + other, r + other + 1)
    else:
        (lo, hi) = (other + j0 + 1, 2 * other + j0)
    return (lo + turn * 2 * sum(rs), hi + turn * 2 * sum(rs))

def port_interval_possible(vs, e):
    if len(vs) != 2:
        return True
    rs = tuple((v.r for v in vs))
    for negative in (False, True):
        bounds = [position_bounds(rs, i, v.lifts[e] + (v.r if negative else 0)) for (i, v) in enumerate(vs)]
        if bounds[0][0] > bounds[1][1] + 1 or bounds[1][0] > bounds[0][1] + 1:
            return False
    return True

@lru_cache(None)
def adjacent_packet_index(rs):
    found = {}
    for (h, (w, pos)) in enumerate(port0_positions(rs)):
        total = len(w)
        for (t, first) in enumerate(w):
            second = w[(t + 1) % total]
            if first[0] == second[0]:
                continue
            (aa, bb) = (first, second) if first[0] == 0 else (second, first)
            (x, y) = (pos[aa], pos[bb])
            delta = 1 if x == total - 1 and y == 0 else -1 if y == total - 1 and x == 0 else 0
            found.setdefault((aa[1], bb[1], delta), set()).add(h)
    return {key: frozenset(value) for (key, value) in found.items()}

@lru_cache(None)
def common_orders(vs):
    ports = []
    for e in (1, 2):
        (a, n) = (vs[0].lifts[e], vs[0].n)
        (turn, residue) = divmod(a, n)
        if residue == 0 and all((v.lifts[e] == turn * v.n for v in vs)):
            continue
        if not port_interval_possible(vs, e):
            return ()
        ports.append(e)
    rs = tuple((v.r for v in vs))
    indexed = port0_positions(rs)
    candidates = None
    if len(vs) == 2 and ports:
        lookup = adjacent_packet_index(rs)
        for e in ports:
            for negative in (False, True):
                (q0, a0) = divmod(vs[0].lifts[e] + (vs[0].r if negative else 0), vs[0].n)
                (q1, a1) = divmod(vs[1].lifts[e] + (vs[1].r if negative else 0), vs[1].n)
                ids = lookup.get((a0, a1, q1 - q0), frozenset())
                candidates = ids if candidates is None else candidates.intersection(ids)
                if not candidates:
                    return ()
    ans = []
    for h in range(len(indexed)) if candidates is None else sorted(candidates):
        (w, pos) = indexed[h]
        if all((fits_port(vs, pos, e) for e in ports)):
            ans.append(w)
    return tuple(ans)

def oscillation(vs, w):
    assert len(vs) == 2
    h = lo = hi = 0
    for (i, j) in w:
        h += (1 if i == 0 else -1) * vs[i].signs[j]
        lo = min(lo, h)
        hi = max(hi, h)
    assert h == 0
    return hi - lo

def pair_data(u, v):
    uu = Vertex(u.r, u.a1, u.a2)
    vv = Vertex(v.r, v.a1, v.a2, v.z1 - u.z1, v.z2 - u.z2)
    ww = common_orders((uu, vv))
    return dict(geometric=bool(ww), witnesses=len(ww), min_width=min((oscillation((u, v), w) for w in ww), default=None))

def edge(u, v):
    if u == v:
        return False
    if u is None or v is None:
        return (v if u is None else u).r == 1
    return all((abs(v.r * a - u.r * b) <= 1 for (a, b) in zip(u.lifts, v.lifts)))

def sector(v):
    assert v.r > 1
    if v.a1 == 0:
        return (0, v.z1, v.a2 + v.n * v.z2)
    if v.a2 == 0:
        return (1, v.z2, v.a1 + v.n * v.z1)
    assert v.a1 == v.a2
    return (2, v.z2 - v.z1, v.a1 + v.n * v.z1)

def from_sector(tau, k, p, r):
    if r == 1:
        assert p % 2 == 0
        m = p // 2
        return Vertex(1, 0, 0, k, m) if tau == 0 else Vertex(1, 0, 0, m, k) if tau == 1 else Vertex(1, 0, 0, m, m + k)
    (z, d) = divmod(p, 2 * r)
    assert d and gcd(d, r) == 1 and (d + r) % 2
    return Vertex(r, 0, d, k, z) if tau == 0 else Vertex(r, d, 0, z, k) if tau == 1 else Vertex(r, d, d, z, z + k)

@lru_cache(None)
def parent(v):
    if v is None or v.r == 1:
        return None
    (tau, k, p) = sector(v)
    r = v.r
    inv = pow(p, -1, r)
    choices = [((p * inv - 1) // r, inv), ((p * (r - inv) + 1) // r, r - inv)]
    good = [(q, s) for (q, s) in choices if (q + s) % 2]
    assert len(good) == 1, (v, choices)
    (q, s) = good[0]
    ans = from_sector(tau, k, q, s)
    assert edge(v, ans)
    assert ans.r < v.r
    return ans

@lru_cache(None)
def root_path(v):
    return (None,) if v is None else (v,) + root_path(parent(v))

def distance(u, v):
    (p, q) = (root_path(u), root_path(v))
    qi = {x: j for (j, x) in enumerate(q)}
    return next((i + qi[x] for (i, x) in enumerate(p) if x in qi))

def finite_neighbors(v, rmax):
    if v.r == 1:
        sectors = [(0, v.z1, 2 * v.z2), (1, v.z2, 2 * v.z1), (2, v.z2 - v.z1, 2 * v.z1)]
        yield None
    else:
        sectors = [sector(v)]
    for (tau, k, p) in sectors:
        for s in range(1, rmax + 1):
            for eps in (-1, 1):
                if (p * s + eps) % v.r:
                    continue
                q = (p * s + eps) // v.r
                if (q + s) % 2 == 0:
                    continue
                w = from_sector(tau, k, q, s)
                assert edge(v, w), (v, w)
                yield w

class UnionFind:

    def __init__(self, n):
        self.p = list(range(n))
        self.components = n

    def find(self, i):
        while self.p[i] != i:
            self.p[i] = self.p[self.p[i]]
            i = self.p[i]
        return i

    def join(self, i, j):
        (i, j) = (self.find(i), self.find(j))
        if i == j:
            return False
        self.p[i] = j
        self.components -= 1
        return True

def graph_homology(vs):
    vv = [None] + sorted((v for v in vs if v is not None))
    idx = {v: j for (j, v) in enumerate(vv)}
    rmax = max((v.r for v in vv if v is not None), default=0)
    uf = UnionFind(len(vv))
    ec = 0
    degree = [0] * len(vv)
    cycles = 0
    for (j, v) in enumerate(vv[1:], 1):
        for w in set(finite_neighbors(v, rmax)):
            i = idx.get(w)
            if i is None or i >= j:
                continue
            ec += 1
            degree[i] += 1
            degree[j] += 1
            cycles += not uf.join(i, j)
    rank1 = len(vv) - uf.components
    assert cycles == ec - rank1
    assert cycles == 0
    return dict(vertices=len(vv), edges=ec, rank_d1=rank1, betti_Z=[uf.components, ec - rank1, 0], max_degree=max(degree), triangles=0, phase_vertices=len(vv) - 1)

def exhaustive_signs(rmax):
    words = axis_words = reduced_pairs = 0
    for r in range(1, rmax + 1):
        n = 2 * r
        for plus in combinations(range(n), r):
            ss = [-1] * n
            for j in plus:
                ss[j] = 1
            words += 1
            aa = [a for a in range(n) if ss[a] == 1 and ss[(a + r) % n] == -1 and all((j in (a, (a + r) % n) or ss[(2 * a - j) % n] == -ss[j] for j in range(n)))]
            assert len(aa) <= 2
            axis_words += bool(aa)
            for (a, b) in combinations(aa, 2):
                d = (b - a) % n
                if gcd(d, r) == 1:
                    assert (d + r) % 2
                    expected = sign_word(r, (0, 0, d))
                    assert tuple((ss[(a + j) % n] for j in range(n))) == expected
                    reduced_pairs += 1
    return dict(rmax=rmax, balanced_words=words, words_with_axes=axis_words, reduced_axis_pairs=reduced_pairs)

def order_crosscheck(rmax, phase_range=1):
    base = vertices(rmax, 0)
    count = positives = witnesses = 0
    widths = {}
    by_shape = {}
    for u in base:
        for v0 in base:
            for (z1, z2) in product(range(-phase_range, phase_range + 1), repeat=2):
                v = Vertex(v0.r, v0.a1, v0.a2, z1, z2)
                q = pair_data(u, v)
                predicted = u == v or edge(u, v)
                assert q['geometric'] == predicted, (u, v, q, predicted)
                count += 1
                if q['geometric']:
                    positives += 1
                    witnesses += q['witnesses']
                    if u != v:
                        assert q['min_width'] == 1, (u, v, q)
                        widths[q['min_width']] = widths.get(q['min_width'], 0) + 1
                by_shape[u.r, v.r] = by_shape.get((u.r, v.r), 0) + 1
    return dict(rmax=rmax, relative_phase_bound=phase_range, pairs=count, disjoint_including_equal=positives, order_witnesses=witnesses, distinct_pair_min_widths=widths, shape_pairs=len(by_shape))

def optimization_crosscheck(rmax=4):
    base = vertices(rmax, 0)
    queries = port_tests = 0
    for u in base:
        for v0 in base:
            for (z1, z2) in product((-1, 0, 1), repeat=2):
                v = Vertex(v0.r, v0.a1, v0.a2, z1, z2)
                vs = (u, v)
                ref = []
                for (w, pos) in port0_positions((u.r, v.r)):
                    good = True
                    for e in (1, 2):
                        slow = fits_port_slow(vs, pos, e)
                        fast = fits_port(vs, pos, e)
                        assert slow == fast, (u, v, e, w)
                        port_tests += 1
                        good = good and slow
                    if good:
                        ref.append(w)
                assert tuple(ref) == common_orders(vs), (u, v)
                queries += 1
    return dict(rmax=rmax, phase_bound=1, full_witness_set_queries=queries, slow_fast_port_tests=port_tests, all_equal=True)

def height_checks(rmax):
    count = families = 0
    largest = 0
    for r in range(1, rmax + 1):
        for v in types(r):
            h = len(root_path(v)) - 1
            val = lo = hi = 0
            for s in v.signs:
                val += s
                lo = min(lo, val)
                hi = max(hi, val)
            assert val == 0 and hi - lo == h
            largest = max(largest, h)
            count += 1
        if r % 2 == 0:
            v = Vertex(r, 1, 0)
            assert distance(None, v) == 2
            assert parent(v) == Vertex(1)
            families += 1
    return dict(rmax=rmax, normal_types=count, max_height=largest, displayed_unbounded_family=families)

def truncations(rbounds, zbounds):
    ans = []
    previous = {}
    for zmax in zbounds:
        for rmax in rbounds:
            vv = set(vertices(rmax, zmax))
            raw = graph_homology(vv)
            closed = set(vv)
            for v in vv:
                closed.update(root_path(v))
            closure = graph_homology(closed)
            assert closure['betti_Z'] == [1, 0, 0]
            assert raw['betti_Z'][1:] == [0, 0]
            if zmax in previous:
                assert previous[zmax].issubset(vv)
            previous[zmax] = vv
            ans.append(dict(rmax=rmax, zmax=zmax, genus_max=3 * rmax // 2, complexity_max=6 * rmax, raw=raw, parent_closure=closure, added_parents=closure['vertices'] - raw['vertices'], H1_persistence_rank=0, H2_persistence_rank=0))
    return ans

def audit(args):
    started = time.monotonic()
    out = dict(status='finite checks of the proved catalogue; not a substitute for proof')
    out['packet_optimization'] = optimization_crosscheck()
    print('cached and unpruned packet predicates agree', flush=True)
    out['signs'] = exhaustive_signs(args.sign_rmax)
    print('signed diagrams checked', flush=True)
    out['orders'] = order_crosscheck(args.order_rmax, args.relative_phase)
    print('independent order/determinant comparison checked', flush=True)
    out['heights'] = height_checks(args.height_rmax)
    out['truncations'] = truncations(args.trunc_rmax, args.trunc_zmax)
    print(json.dumps(out, indent=2))
    return out

def exploratory(rmax, zmax):
    vv = vertices(rmax, zmax)
    edges = []
    for (i, j) in combinations(range(len(vv)), 2):
        q = pair_data(vv[i], vv[j])
        if q['geometric']:
            edges.append((i, j, q['min_width']))
    triangles = []
    adjacent = {(i, j) for (i, j, _) in edges}
    for (i, j, k) in combinations(range(len(vv)), 3):
        if all((tuple(sorted(p)) in adjacent for p in ((i, j), (i, k), (j, k)))):
            if common_orders((vv[i], vv[j], vv[k])):
                triangles.append((i, j, k))
    return dict(status='horizontal part of proved normal-form complex; root A omitted', rmax=rmax, zmax=zmax, vertices=len(vv), edges=len(edges), triangles=len(triangles), widths={w: sum((q == w for (_, _, q) in edges)) for w in sorted(set((q for (_, _, q) in edges)))}, edge_samples=[(vv[i].__dict__, vv[j].__dict__, w) for (i, j, w) in edges[:20]])

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--audit', action='store_true')
    p.add_argument('--orders-only', action='store_true')
    p.add_argument('--rmax', type=int, default=3)
    p.add_argument('--zmax', type=int, default=0)
    p.add_argument('--sign-rmax', type=int, default=9)
    p.add_argument('--order-rmax', type=int, default=6)
    p.add_argument('--relative-phase', type=int, default=1)
    p.add_argument('--height-rmax', type=int, default=256)
    p.add_argument('--trunc-rmax', type=int, nargs='+', default=[4, 8, 16, 32, 64])
    p.add_argument('--trunc-zmax', type=int, nargs='+', default=[0, 1, 2])
    p.add_argument('--output')
    args = p.parse_args(['--audit'])
    if args.orders_only:
        started = time.monotonic()
        out = order_crosscheck(args.order_rmax, args.relative_phase)
        out['elapsed_seconds'] = round(time.monotonic() - started, 3)
        if args.output:
            from pathlib import Path
            target = Path(args.output).resolve()
            assert target.parent == Path(__file__).resolve().parent
            target.write_text(json.dumps(out, indent=2) + '\n', encoding='utf-8')
        print(json.dumps(out, indent=2))
    elif args.audit:
        audit(args)
    else:
        print(json.dumps(exploratory(args.rmax, args.zmax), indent=2))
if __name__ == '__main__':
    main()
