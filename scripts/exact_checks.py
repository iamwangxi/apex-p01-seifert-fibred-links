#!/usr/bin/env python3
"""Exact bounded diagnostics for the Seifert-fibred link proof.

Uniform results are proved in proof/. Finite checks cover free products,
Jordan-feature equations and a two-cone support; no finite list proves the
family theorem. Writes only exact_checks.json beside this script.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import gcd, prod
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
PAIRS = [(2, 3), (2, 5), (3, 4), (3, 5), (4, 5)]


def normal(word, orders):
    stack = []
    for factor, exponent in word:
        q = orders[factor]
        if q:
            exponent %= q
        if not exponent:
            continue
        if stack and stack[-1][0] == factor:
            exponent += stack.pop()[1]
            if q:
                exponent %= q
        if exponent:
            stack.append((factor, exponent))
    return tuple(stack)


def inverse(word, orders):
    return normal(((f, -a) for f, a in reversed(word)), orders)


def cyclic_reduce(word, orders):
    w = normal(word, orders)
    while len(w) > 1 and w[0][0] == w[-1][0]:
        w = normal(w[1:] + w[:1], orders)
    return w


def short_conjugators(orders):
    alphabet = [(f, a) for f, q in enumerate(orders)
                for a in (range(1, q) if q else (-1, 1))]
    yield ()
    for x in alphabet:
        yield (x,)
    for x in alphabet:
        for y in alphabet:
            if x[0] != y[0]:
                yield (x, y)


def free_product_checks():
    count = 0
    profiles = []
    for a, b in PAIRS:
        assert gcd(a, b) == 1
        orders = (a, b, 0)  # C_a * C_b * Z
        words = list(short_conjugators(orders))
        local = 0
        for g, h in product(words, repeat=2):
            gi, hi = inverse(g, orders), inverse(h, orders)
            for r in range(1, a):
                for s in range(1, b):
                    w = normal(g + ((0, r),) + gi + h + ((1, s),) + hi, orders)
                    c = cyclic_reduce(w, orders)
                    assert len(c) >= 2 and c[0][0] != c[-1][0]
                    for power in (2, 3):
                        assert len(normal(c * power, orders)) == power * len(c)
                    local += 1
        count += local
        profiles.append({'orders': [a, b], 'conjugators': len(words),
                         'conjugated_products': local})
    return {'conjugated_products': count, 'profiles': profiles,
            'scope': 'conjugators of syllable length at most two; all nonzero cone powers'}


def abelian_checks():
    profiles = [(), (2,), (3,), (5,), (7,)] + [tuple(x) for x in PAIRS]
    partitions = peripheral = covers = 0
    genus_examples = []
    for n in (2, 4, 6, 8):
        for orders in profiles:
            s = len(orders)
            for actual in product((0, 1), repeat=n):
                for cones in product((0, 1), repeat=s):
                    t = actual[0]
                    null = all(x == t for x in actual) and all(
                        (x - t) % q == 0 for x, q in zip(cones, orders))
                    empty = not any(actual) and not any(cones)
                    full = all(actual) and all(cones)
                    assert null == (empty or full)
                    for i in range(n):
                        other = [actual[j] for j in range(n) if j != i]
                        t = other[0]
                        is_peripheral = all(x == t for x in other) and all(
                            (x - t) % q == 0 for x, q in zip(cones, orders))
                        only_i = actual[i] == 1 and sum(actual) == 1 and not any(cones)
                        complement_i = (actual[i] == 0 and sum(actual) == n - 1
                                        and all(cones))
                        assert is_peripheral == (empty or full or only_i or complement_i)
                        peripheral += 1
                    partitions += 1
            degree = prod(orders)
            g_double = n - 1
            chi = degree * (2 - 2 * g_double - 2 * sum(
                (Q(1) - Q(1, q) for q in orders), Q(0)))
            assert chi.denominator == 1 and chi % 2 == 0
            genus = 1 - chi / 2
            assert genus >= (1 if n == 2 and not orders else 2)
            for j, q in enumerate(orders):
                assert len({k % q for k in range(q)}) == q
            covers += 1
            if n in (2, 4) and orders in ((2,), (2, 3)):
                genus_examples.append({'actual_boundaries': n, 'orders': orders,
                                       'degree': degree, 'cover_genus': int(genus)})
    return {'feature_partitions': partitions, 'peripheral_membership_tests': peripheral,
            'double_cover_profiles': covers, 'genus_examples': genus_examples}


# Two disjoint lenses, containing two differently labelled cone points.
# Actual positives 1=(0,0),2=(5,0); negatives 3=(2,0),4=(7,0).
# Regions O=0 is one connected annular outside region, L=1, R=2.
EDGES = [(3, 1, 1, 0), (3, 1, 0, 1), (4, 2, 2, 0), (4, 2, 0, 2)]
LINES = [[(2, 0), (0, 0)], [(2, 0), (1, -1), (0, 0)],
         [(7, 0), (5, 0)], [(7, 0), (6, -1), (5, 0)]]
ALL = frozenset(range(4))


def winding(poly, point):
    px, py = point
    w = 0
    for a, b in zip(poly, poly[1:] + poly[:1]):
        ax, ay = a
        bx, by = b
        c = (bx - ax) * (py - ay) - (by - ay) * (px - ax)
        assert not (c == 0 and min(ax, bx) <= px <= max(ax, bx)
                    and min(ay, by) <= py <= max(ay, by))
        if ay <= py < by and c > 0:
            w += 1
        if by <= py < ay and c < 0:
            w -= 1
    return w


def drawing_checks():
    left = [(2, 0), (0, 0), (1, -1)]
    right = [(7, 0), (5, 0), (6, -1)]
    signs = {(0, 0): 0, (1, 0): 1, (0, 1): 2}

    def region(p):
        return signs[(winding(left, p), winding(right, p))]

    assert region((Q(1), Q(-1, 4))) == 1
    assert region((Q(6), Q(-1, 4))) == 2
    count = 0
    for e, line in enumerate(LINES):
        _, _, l, r = EDGES[e]
        for a, b in zip(line, line[1:]):
            dx, dy = b[0] - a[0], b[1] - a[1]
            mx, my = Q(a[0] + b[0], 2), Q(a[1] + b[1], 2)
            assert region((mx - Q(dy, 100), my + Q(dx, 100))) == l
            assert region((mx + Q(dy, 100), my - Q(dx, 100))) == r
            count += 2
    return count


def matchings(support):
    result = []
    for pair in combinations(sorted(support), 2):
        d = {i: 0 for i in range(1, 5)}
        for e in pair:
            a, b, _, _ = EDGES[e]
            d[a] += 1
            d[b] += 1
        if all(x == 1 for x in d.values()):
            result.append(frozenset(pair))
    return result


def faces(support):
    parent = list(range(3))

    def find(x):
        while x != parent[x]:
            x = parent[x]
        return x

    for e in ALL - support:
        _, _, l, r = EDGES[e]
        a, b = find(l), find(r)
        parent[max(a, b)] = min(a, b)
    image = tuple(find(x) for x in range(3))
    return sorted(set(image)), image


def solve(fs, equations, root):
    adj = {f: [] for f in fs}
    for l, r, c in equations:
        if l == r:
            assert c == 0
        else:
            adj[r].append((l, c))
            adj[l].append((r, -c))
    u = {root: Q(0)}
    queue = [root]
    for x in queue:
        for y, d in adj[x]:
            if y not in u:
                u[y] = u[x] + d
                queue.append(y)
            else:
                assert u[y] == u[x] + d
    assert set(u) == set(fs), 'one global height constant only'
    return u


def potential(support, w, ref, root=None):
    fs, image = faces(support)
    equations = [(image[EDGES[e][2]], image[EDGES[e][3]], w[e] - (e in ref))
                 for e in support]
    return solve(fs, equations, fs[0] if root is None else root), image


def block_width(a, b):
    fs, image = faces(a | b)
    equations = [(image[EDGES[e][2]], image[EDGES[e][3]], Q(1)) for e in a - b]
    u = solve(fs, equations, fs[0])
    return max(u.values()) - min(u.values())


def decode(support, w, ref=None, root=None):
    ms = matchings(support)
    assert ms
    ref = ms[0] if ref is None else ref
    u, image = potential(support, w, ref, root)
    cuts = sorted({Q(0), Q(1)} | {(-x) % 1 for x in u.values()})

    def rounded(t):
        q = {f: (x + t).__floor__() for f, x in u.items()}
        chosen = set()
        for e in support:
            _, _, l, r = EDGES[e]
            value = int(e in ref) + q[image[l]] - q[image[r]]
            assert value in (0, 1)
            if w[e] == 0:
                assert value == 0
            if value:
                chosen.add(e)
        m = frozenset(chosen)
        assert m in ms
        return m

    bary = {}
    probes = {t for t in cuts if t < 1}
    for a, b in zip(cuts, cuts[1:]):
        t = (a + b) / 2
        probes.add(t)
        m = rounded(t)
        bary[m] = bary.get(m, Q(0)) + b - a
    outputs = [rounded(t) for t in probes]
    for a, b in product(outputs, repeat=2):
        assert block_width(a, b) <= 1
    assert sum(bary.values()) == 1
    for e in ALL:
        assert sum(c for m, c in bary.items() if e in m) == w[e]
    return bary, len(probes)


def compositions(total, n):
    if n == 1:
        yield (total,)
    else:
        for a in range(total + 1):
            for tail in compositions(total - a, n - 1):
                yield (a,) + tail


def carrier_checks():
    counts = dict(feasible_graphs=0, ordered_matching_pairs=0, rational_flows=0,
                  threshold_probes=0, reference_comparisons=0, root_comparisons=0,
                  zero_support_comparisons=0, exact_simplex_recoveries=0)
    for mask in range(16):
        support = frozenset(e for e in ALL if mask & (1 << e))
        ms = matchings(support)
        if not ms:
            continue
        counts['feasible_graphs'] += 1
        for a, b in product(ms, repeat=2):
            u, _ = potential(support, [Q(e in a) for e in ALL], b)
            assert max(u.values()) - min(u.values()) == block_width(a, b)
            counts['ordered_matching_pairs'] += 1
        options = []
        for a, b in [(0, 1), (2, 3)]:
            options.append([Q(i, 8) for i in range(9)] if a in support and b in support
                           else [Q(int(a in support))])
        for x, y in product(*options):
            w = [x, 1 - x, y, 1 - y]
            bary, probes = decode(support, w)
            counts['rational_flows'] += 1
            counts['threshold_probes'] += probes
            for ref in ms:
                assert decode(support, w, ref=ref)[0] == bary
                counts['reference_comparisons'] += 1
            for root in faces(support)[0]:
                assert decode(support, w, root=root)[0] == bary
                counts['root_comparisons'] += 1
            positive = frozenset(e for e in support if w[e] > 0)
            assert decode(positive, w)[0] == bary
            counts['zero_support_comparisons'] += 1
        for size in range(1, len(ms) + 1):
            for simplex in combinations(ms, size):
                if not all(block_width(a, b) <= 1 for a, b in combinations(simplex, 2)):
                    continue
                for numbers in compositions(8, size):
                    coeffs = [Q(v, 8) for v in numbers]
                    w = [sum(c for m, c in zip(simplex, coeffs) if e in m) for e in ALL]
                    expected = {m: c for m, c in zip(simplex, coeffs) if c}
                    assert decode(support, w)[0] == expected
                    counts['exact_simplex_recoveries'] += 1
    full = matchings(ALL)
    assert full == [frozenset((0, 2)), frozenset((0, 3)),
                    frozenset((1, 2)), frozenset((1, 3))]
    assert block_width(full[1], full[2]) == 2
    assert block_width(full[0], full[3]) == 1
    midpoint = decode(ALL, [Q(1, 2)] * 4)[0]
    assert midpoint == {full[0]: Q(1, 2), full[3]: Q(1, 2)}
    assert counts['feasible_graphs'] == 9
    return {'counts': counts, 'drawing_side_probes': drawing_checks(),
            'matchings': [sorted(m) for m in full],
            'pair_widths': [[int(block_width(a, b)) for b in full] for a in full],
            'edge_incidence': EDGES, 'polylines': LINES,
            'cone_points': [['1', '-1/4'], ['6', '-1/4']],
            'nonadjacent_pair': [1, 2], 'decoded_midpoint': [0, 3]}


def main():
    result = {'status': 'finite diagnostics passed; uniform proof is in the manuscript',
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'free_product': free_product_checks(),
              'abelian_and_cover': abelian_checks(),
              'two_cone_carrier': carrier_checks(),
              'limitations': ['Only bounded conjugators and sampled orders/boundary counts are tested.',
                              'The two-cone graph is one example and its nine feasible subgraphs.',
                              'No arbitrary arc normalisation or parameter-family algorithm is implemented.',
                              'The family theorem and class minima require the written geometric proofs.']}
    (ROOT/'exact_checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'conjugated_products': result['free_product']['conjugated_products'],
                      'abelian_and_cover': result['abelian_and_cover'],
                      'carrier_counts': result['two_cone_carrier']['counts']},
                     ensure_ascii=False,sort_keys=True))


if __name__ == '__main__':
    main()
