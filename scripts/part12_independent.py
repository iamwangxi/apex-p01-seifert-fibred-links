#!/usr/bin/env python3
# Finite exact diagnostic for Part 12 of the proof; standard library only; prints a deterministic report and writes no files.
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from math import gcd, lcm
import json
import random
import time

def cc(n, edges):
    adj = [set() for _ in range(n)]
    for (a, b) in edges:
        adj[a].add(b)
        adj[b].add(a)
    unseen = set(range(n))
    out = []
    while unseen:
        todo = [min(unseen)]
        part = set()
        while todo:
            a = todo.pop()
            if a not in part:
                part.add(a)
                todo.extend(adj[a] - part)
        unseen -= part
        out.append(part)
    return out

def genus(chi, boundaries, components=1):
    a = 2 * components - boundaries - chi
    assert a >= 0 and a % 2 == 0, (chi, boundaries, components)
    return a // 2

def pants_degree():
    tested = survivors = 0
    for n in range(2, 15, 2):
        for plus in combinations(range(n), n // 2):
            word = [-1] * n
            for j in plus:
                word[j] = 1
            for degree in range(1, 7):
                total = n * degree
                for a in range(total):
                    tested += 1
                    b = (a + total // 2) % total
                    if word[a % n] != 1 or word[b % n] != -1:
                        continue
                    ok = all((j in (a, b) or word[j % n] + word[(2 * a - j) % n] == 0 for j in range(total)))
                    if ok:
                        survivors += 1
                        assert degree == 1, (word, degree, a)
    return dict(axis_conditions=tested, admissible_unit_axes=survivors, max_sheets=14, max_degree=6)

@lru_cache(None)
def matchings(points):
    if not points:
        return ((),)
    a = points[0]
    return tuple((((a, points[j]),) + left + right for j in range(1, len(points), 2) for left in matchings(points[1:j]) for right in matchings(points[j + 1:])))

def disk_faces(n, matching):
    edges = []
    for (a, b) in matching:
        edges += [((a - 1) % n, b), (a, (b - 1) % n)]
    faces = cc(n, edges)
    index = {j: i for (i, face) in enumerate(faces) for j in face}
    dual = [(index[a], index[(a - 1) % n]) for (a, b) in matching]
    assert all((a != b for (a, b) in dual))
    assert len(faces) == len(matching) + 1
    assert len(cc(len(faces), dual)) == 1
    return (faces, dual)

def two_feature_caps():
    total = path_cases = three_feature_cases = 0
    for n in range(2, 19, 2):
        for mat in matchings(tuple(range(n))):
            total += 1
            (faces, dual) = disk_faces(n, mat)
            degrees = Counter((v for edge in dual for v in edge))
            leaves = sum((degrees[j] == 1 for j in range(len(faces))))
            if leaves == 2:
                path_cases += 1
                offsets = {(a + b) % n for (a, b) in mat}
                assert len(offsets) == 1 and next(iter(offsets)) % 2 == 1
            if leaves == 3:
                three_feature_cases += 1
    assert three_feature_cases > 0
    return dict(all_noncrossing_matchings=total, two_feature_parallel_matchings=path_cases, three_feature_nonparallel_matchings=three_feature_cases, max_endpoints=18)

def weighted_packets():
    rng = random.Random(2410202601)
    tests = local_ends = same_end = 0
    for _ in range(5000):
        n = 2 * rng.randint(1, 50)
        weights = [rng.randint(1, 10) for _ in range(rng.randint(1, 7))]
        offsets = [rng.randrange(n * b // 2) * 2 + 1 for b in weights]
        (pe, ge, ends) = ([], [], [])
        for (b, c) in zip(weights, offsets):
            size = n * b
            mat = [(j, (c - j) % size) for j in range(size) if j < (c - j) % size]
            (faces, dual) = disk_faces(size, mat)
            degree = Counter((v for edge in dual for v in edge))
            for face in faces:
                projected = [j % n for j in face]
                ge.extend(((projected[0], j) for j in projected[1:]))
            this_ends = [next(iter(faces[j])) % n for j in range(len(faces)) if degree[j] == 1]
            assert len(this_ends) == 2
            ends.append(this_ends)
            pe.extend(((a % n, d % n) for (a, d) in mat))
        (points, gaps) = (cc(n, pe), cc(n, ge))
        g = n
        for c in offsets:
            g = gcd(g, c - offsets[0])
        assert len(points) == g // 2
        assert {len(part) for part in points} == {2 * n // g}
        assert len(gaps) == len(points) + 1
        region = {j: i for (i, part) in enumerate(gaps) for j in part}
        dual = []
        for part in points:
            incident = {tuple(sorted((region[j], region[(j - 1) % n]))) for j in part}
            assert len(incident) == 1
            dual.append(incident.pop())
        assert all((a != b for (a, b) in dual))
        assert len(set(dual)) == len(points)
        degree = Counter((v for edge in dual for v in edge))
        assert len(cc(len(gaps), dual)) == 1
        assert sorted(degree.values()) == [1, 1] + [2] * (len(gaps) - 2)
        for (b, pair) in zip(weights, ends):
            assert all((degree[region[j]] == 1 for j in pair))
            local_ends += 2
            if b % 2 == 0:
                assert region[pair[0]] == region[pair[1]]
                same_end += 1
        tests += 1
    return dict(configurations=tests, terminal_end_incidences=local_ends, even_degree_same_end_checks=same_end)

def reduce_word(word, orders):
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
        if e:
            out.append((i, e))
    return tuple(out)

def wpow(word, exponent, orders):
    if exponent < 0:
        word = tuple(((i, -e) for (i, e) in reversed(word)))
    return reduce_word(word * abs(exponent), orders)

def peripheral_equations():
    tested = words = 0
    for (orders, peripheral) in (((2, 3), (((0, 1), (1, 1)),)), ((2, 0), (((1, 1),), ((0, 1), (1, 1)))), ((3, 0), (((1, 1),), ((0, 1), (1, 1)))), ((0, 0), (((0, 1),), ((1, 1),), ((0, 1), (1, 1))))):
        exponents = [range(1, q) if q else (-2, -1, 1, 2) for q in orders]
        pool = {()}
        frontier = {()}
        for _ in range(3):
            frontier = {w + ((i, e),) for w in frontier for i in (0, 1) if not w or w[-1][0] != i for e in exponents[i]}
            pool |= frontier
        for w in pool:
            words += 1
            for (i, p) in enumerate(peripheral):
                if w in {wpow(p, k, orders) for k in range(-6, 7)}:
                    same_allowed = False
                else:
                    same_allowed = True
                for (j, q) in enumerate(peripheral):
                    if i == j and (not same_allowed):
                        continue
                    for (a, b) in product(range(-2, 3), repeat=2):
                        lhs = reduce_word(wpow(p, a, orders) + w + wpow(q, -b, orders), orders)
                        tested += 1
                        assert (lhs == w) == (a == b == 0), (orders, i, j, w, a, b)
    (d, w, orders) = (((0, 1), (1, 1)), ((0, 1),), (2, 2))
    assert reduce_word(d + w + d, orders) == w
    return dict(reduced_return_words=words, equations=tested, excluded_two_involution_negative_control=True)

def framing_lattices():
    values = (-8, -6, -4, -3, -2, -1, 1, 2, 3, 4, 6, 8)
    stats = Counter()
    for m in (2, 3, 4):
        for ff in product(values, repeat=m):
            stats['framing_lists'] += 1
            D = lcm(*(abs(f) for f in ff))
            w = [D // f for f in ff]
            S = sum(w)
            assert gcd(*w) == 1
            assert all((D - f * x == 0 for (f, x) in zip(ff, w)))
            q_inner = gcd(D, abs(S))
            ext = sum((abs(x) for x in w))
            genus(-(m - 1) * D, ext + q_inner)
            if S:
                t = Fraction(D, S)
                stats['integral_inner_slope' if t.denominator == 1 else 'nonintegral_inner_slope'] += 1
                if t.denominator == 1:
                    assert q_inner == abs(S)
                continue
            stats['reciprocal_zero'] += 1
            for P in (1, 2, 3, 4, 5, 6, 10, 12, 18, 30):
                common = gcd(D, P)
                (b, a) = (P // common, D // common)
                assert gcd(a, b) == 1 and b * D == a * P
                assert all((scale * D % P for scale in range(1, b)))
                assert all((b * D % divisor == 0 for divisor in range(1, P + 1) if P % divisor == 0))
                chi = -b * (m - 1) * D - a * (P - 1)
                genus(chi, b * ext + a)
                genus(2 * chi, 2 * b * ext)
                stats['meridional_primitive_lattices'] += 1
    return dict(stats)

def packet(word, k):
    q = len(word)
    (labels, signs, gap_names) = ([], [], [])
    for band in range(2 * k):
        line = list(range(q))
        if band % 2:
            line.reverse()
        labels.extend(line)
        signs.extend((word[j] * (-1 if band % 2 else 1) for j in line))
        gap_names.extend((('P', min(a, b)) for (a, b) in zip(line, line[1:])))
        gap_names.append(('R', q - 1) if band % 2 == 0 else ('L', 0))
    return (labels, signs, gap_names)

def random_pattern(word, rng):
    (k, holes) = (rng.randint(1, 3), rng.choice((2, 4, 6, 8)))
    (labels, signs, gaps) = packet(word, k)
    n = len(labels)
    nt = rng.choice(range(0, min(n, holes) + 1, 2))
    pos = [j for j in range(n) if signs[j] == 1]
    neg = [j for j in range(n) if signs[j] == -1]
    if len(pos) < nt // 2 or len(neg) < nt // 2:
        return None
    tethers = set(rng.sample(pos, nt // 2) + rng.sample(neg, nt // 2))
    marks = [2 * j for j in sorted(tethers)]
    for _ in range((holes - nt) // 2):
        marks.extend([2 * rng.randrange(n) + 1] * 2)
    masks = {}
    for a in range(n):
        for b in range(a + 1, n):
            masks[a, b] = sum((1 << h for (h, mark) in enumerate(marks) if 2 * a < mark < 2 * b))
    full = (1 << holes) - 1
    points = tuple((j for j in range(n) if j not in tethers))

    @lru_cache(None)
    def count(remaining):
        if not remaining:
            return 1
        a = remaining[0]
        return sum((count(remaining[1:z]) * count(remaining[z + 1:]) for z in range(1, len(remaining), 2) if signs[a] != signs[remaining[z]] and masks[a, remaining[z]] not in (0, full)))
    if not count(points):
        return None

    def draw(remaining):
        if not remaining:
            return []
        a = remaining[0]
        pick = rng.randrange(count(remaining))
        for z in range(1, len(remaining), 2):
            b = remaining[z]
            if signs[a] == signs[b] or masks[a, b] in (0, full):
                continue
            mass = count(remaining[1:z]) * count(remaining[z + 1:])
            if pick < mass:
                return [(a, b)] + draw(remaining[1:z]) + draw(remaining[z + 1:])
            pick -= mass
        raise AssertionError('unranking')
    return dict(n=n, k=k, holes=holes, labels=labels, signs=signs, gaps=gaps, tethers=tethers, marks=marks, matching=draw(points), masks=masks, full=full)

def trace_paths(pattern, selected):
    graph = defaultdict(list)

    def add(a, b, mask):
        graph[a].append((b, mask))
        graph[b].append((a, mask))
    for (a, b) in pattern['matching']:
        add(('p', a), ('p', b), pattern['masks'][a, b])
    for j in pattern['tethers']:
        add(('p', j), ('a', j), 0)
    for (j, chamber) in enumerate(pattern['gaps']):
        if chamber in selected:
            add(('p', j), ('p', (j + 1) % pattern['n']), 0)
    assert all((len(neighbours) in (1, 2) for neighbours in graph.values()))
    (seen, paths) = (set(), [])
    for start in sorted(graph):
        if start in seen or len(graph[start]) != 1:
            continue
        (current, previous, mask) = (start, None, 0)
        while True:
            seen.add(current)
            if previous is not None and len(graph[current]) == 1:
                paths.append((start, current, mask))
                break
            (nxt, edge_mask) = next(((v, m) for (v, m) in graph[current] if v != previous))
            mask ^= edge_mask
            (previous, current) = (current, nxt)
    return paths

def assembly(word, patterns, selected):
    removed = set()
    for (name, j) in selected:
        removed |= {j, j + 1} if name == 'P' else {j}
    remaining = set(range(len(word))) - removed
    (edges, actual, bad) = ([], defaultdict(set), set())
    for (port, p) in enumerate(patterns):
        cap_of_pair = {frozenset((j, (j + 1) % p['n'])): chamber for (j, chamber) in enumerate(p['gaps'])}
        for (a, b, mask) in trace_paths(p, selected):
            boundary = [p['labels'][e[1]] for e in (a, b) if e[0] == 'p']
            assert all((j in remaining for j in boundary))
            if len(boundary) == 2:
                edges.append(tuple(boundary))
                if mask in (0, p['full']):
                    key = frozenset((a[1], b[1]))
                    assert key in cap_of_pair, (word, p, selected, (a, b))
                    bad.add(cap_of_pair[key])
            elif len(boundary) == 1:
                other = b if a[0] == 'p' else a
                actual[boundary[0]].add((port, other[1]))
            else:
                assert a[0] == b[0] == 'a'
    parts = [part for part in cc(len(word), edges) if part <= remaining]
    records = [(part, set().union(*(actual[j] for j in part))) for part in parts]
    return (removed, bad, records)

def closure(word, patterns, seed):
    q = len(word)
    p = patterns[0]
    seed_pair = next(((p['signs'][j], p['signs'][(j + 1) % p['n']]) for (j, name) in enumerate(p['gaps']) if name == seed))
    eligible = {name for (j, name) in enumerate(p['gaps']) if (p['signs'][j], p['signs'][(j + 1) % p['n']]) == seed_pair}
    (_, _, original) = assembly(word, patterns, frozenset())
    seed_component = next((part for (part, actual) in original if seed[1] in part))
    (states, ends) = ({}, set())

    def visit(selected):
        if selected in states:
            return
        (removed, enabled, records) = assembly(word, patterns, selected)
        assert enabled <= eligible - selected
        states[selected] = enabled
        if not enabled:
            retained = set().union(*(part for (part, actual) in records if actual))
            assert len(retained) < q
            for (part, actual) in original:
                if part != seed_component:
                    assert (part, actual) in records
            ends.add((selected, tuple(sorted(retained))))
        for name in enabled:
            visit(selected | {name})
    visit(frozenset((seed,)))
    assert len(ends) == 1
    for (a, ea) in states.items():
        for (b, eb) in states.items():
            if a <= b:
                assert ea - b <= eb
    return len(states)

def multiport_closures():
    rng = random.Random(2410202602)
    stats = Counter()
    for _ in range(3000):
        q = rng.randint(1, 8)
        word = (1,) + tuple((rng.choice((-1, 1)) for _ in range(q - 1)))
        patterns = []
        for port in range(rng.randint(2, 5)):
            pattern = None
            for trial in range(12):
                pattern = random_pattern(word, rng)
                stats['pattern_trials'] += 1
                if pattern is not None:
                    break
            if pattern is None:
                break
            patterns.append(pattern)
        else:
            (_, bad, records) = assembly(word, patterns, frozenset())
            assert not bad
            if not all((actual for (part, actual) in records)):
                continue
            stats['reduced_inputs'] += 1
            stats['mixed_word_inputs'] += len(set(word)) > 1
            stats['zero_tether_port_occurrences'] += sum((not p['tethers'] for p in patterns))
            stats['degree_six_boundary_occurrences'] += sum((p['k'] == 3 for p in patterns))
            stats['eight_actual_hole_occurrences'] += sum((p['holes'] == 8 for p in patterns))
            for seed in (('L', 0), ('R', q - 1)):
                stats['closure_states'] += closure(word, patterns, seed)
                stats['seeded_closures'] += 1
    assert stats['reduced_inputs'] > 500
    assert stats['zero_tether_port_occurrences'] > 0
    return dict(stats)

def examples():
    data = {}
    data['cable_24'] = dict(blocks=3, chi_R=-11, genus_R=genus(-11, 3), chi_surface=2 * -11, genus_surface=genus(2 * -11, 2), intersections=[22, 11])
    assert data['cable_24']['genus_surface'] == 11
    data['two_trefoil_supports_12'] = dict(blocks=4, chi_R=12 * (2 - 3), genus_R=genus(-12, 1 + 1 + 2), first_genus=genus(-24, 4), intersections=[12, 12, 6])
    for r in range(1, 101):
        n = 2 * r
        eps = [1] + [-1] * r + [1] * (r - 1)
        returns = [(j, -j % n) for j in range(n) if j not in (0, r) and j < -j % n]
        cap = [(j % n, (1 - j) % (2 * n) % n) for j in range(2 * n) if j < (1 - j) % (2 * n)]
        assert all((eps[a] == -eps[b] for (a, b) in returns + cap))
        assert len(cc(n, returns + returns + cap)) == 1
        assert genus(-12 * n, 4) == 12 * r - 1
    data['weights_1_2_cable'] = dict(blocks=5, frames=[6, 3], external_degrees=[1, 2], cap_degrees=[3], chi_R=-6, genus_R=genus(-6, 1 + 2 + 3), genus_surface=genus(-12, 6))
    assert data['weights_1_2_cable']['genus_surface'] == 4
    mode_records = []
    weights = (6, 6, -6)
    for mask in range(1 << 3):
        vertical = [j for j in range(3) if mask & 1 << j]
        if sum((weights[j] for j in vertical)) != 6:
            continue
        chi_child = 1 - 3 - (3 - len(vertical))
        chi_cluster = -18 + 3 * chi_child
        cap_degrees = [3] * len(vertical)
        mode_records.append(dict(vertical=vertical, chi_R=chi_cluster, genus_R=genus(chi_cluster, 3 + sum(cap_degrees)), cap_degrees=cap_degrees, genus_surface=genus(2 * chi_cluster, 6)))
    assert sorted((x['genus_surface'] for x in mode_records)) == [22, 28, 28]
    data['sum_six_component_modes'] = mode_records
    B = ((-3, 1, 1), (1, -3, 1), (1, 1, -1))
    x = (1, 1, 2)
    assert all((sum((a * b for (a, b) in zip(row, x))) == 0 for row in B))
    assert B[0][0] * B[1][1] - B[0][1] * B[1][0] == 8
    q = [gcd(a, sum(x) - a) for a in x]
    assert q == [1, 1, 2]
    data['hopf_eight_higher_degree'] = dict(blocks=4, degrees=q, chi_R=-4, genus_R=genus(-4, sum(q)), surface_components=2, genus_each=genus(-4, 4), actual_boundaries_each=4, intersections=[4, 4, 2])
    eps = [1, 1, 1, -1, -1, -1]
    edges = []
    for a in (0, 2):
        edges += [(j, (2 * a - j) % 6) for j in range(6) if j < (2 * a - j) % 6]
    assert len(cc(6, edges)) == 2
    edges += [(2, 5)]
    assert all((eps[a] == -eps[b] for (a, b) in edges))
    assert cc(6, edges) == [set(range(6))]
    data['hopf_eight_joined_parities'] = dict(blocks=4, sheets=6, chi=-18, actual_boundaries=8, genus=genus(-18, 8), intersections=[3, 3, 3])
    assert data['hopf_eight_joined_parities']['genus'] == 6
    return data

def proposition_M():
    eps = [1, 1, -1, 1, -1, -1]
    mat = [(0, 5), (1, 2), (3, 4), (6, 11), (7, 10), (8, 9)]
    holes = (1.5, 3.5, 8.5)
    for (i, (a, b)) in enumerate(mat):
        assert eps[a % 6] == -eps[b % 6]
        assert 0 < sum((a < h < b for h in holes)) < 3
        assert all((not (a < c < b < d or c < a < d < b) for (c, d) in mat[i + 1:]))
    pieces = cc(6, [(a % 6, b % 6) for (a, b) in mat])
    assert pieces == [{0, 5}, {1, 2, 3, 4}]
    surfaces = []
    for part in pieces:
        s = len(part)
        assert sum((eps[j] for j in part)) == 0
        surfaces.append(dict(sheets=sorted(part), chi=-2 * s, external_boundaries=2 * s, genus=genus(-2 * s, 2 * s)))
    (faces, _) = disk_faces(12, mat)
    gap_edges = []
    for part in faces:
        reduced = [j % 6 for j in part]
        gap_edges += [(reduced[0], j) for j in reduced[1:]]
    gaps = cc(6, gap_edges)
    assert gaps == [{0, 2, 4}, {1, 3}, {5}]
    middle_faces = defaultdict(set)
    for j in range(6):
        surface = 'A' if j in pieces[0] else 'B'
        if j in gaps[0]:
            middle_faces[surface].add(eps[j])
        if (j - 1) % 6 in gaps[0]:
            middle_faces[surface].add(-eps[j])
    assert middle_faces == {'A': {1}, 'B': {-1}}
    returns = [(0, 2), (3, 5)]
    assert len(cc(6, [(a % 6, b % 6) for (a, b) in mat] + returns * 2)) == 1
    raw_path = [2, 0, 5, 3]
    assert all((tuple(sorted((a, b))) in set(returns + [(0, 5)]) for (a, b) in zip(raw_path, raw_path[1:])))
    assert not any((2 < tether < 3 for tether in (1, 4)))
    return dict(genuine_blocks=7, support_surfaces=surfaces, support_gap_regions=[sorted(g) for g in gaps], whole_chi=-12, whole_genus=genus(-12, 4), raw_chi=-8, raw_genus=genus(-8, 4), safe_end_genus=genus(-4, 4), interface_intersections=[2, 2, 1, 1, 1, 1])

def proposition_H_catalogue():
    stats = Counter()
    for n in range(2, 15, 2):
        r = n // 2
        for plus in combinations(range(n), r):
            pos = set(plus)
            eps = [1 if j in pos else -1 for j in range(n)]
            axes = [a for a in pos if eps[(a + r) % n] == -1 and all((j in (a, (a + r) % n) or eps[j] == -eps[(2 * a - j) % n] for j in range(n)))]
            offsets = [c for c in range(1, n, 2) if all((eps[j] == -eps[(c - j) % n] for j in range(n)))]
            for (ia, a) in enumerate(axes):
                for (b, c) in product(axes[ia:], offsets):
                    stats['signed_diagrams'] += 1
                    actual = {a, (a + r) % n, b, (b + r) % n}
                    edges = [(j, (2 * x - j) % n) for x in (a, b) for j in range(n) if j not in (x, (x + r) % n)]
                    edges += [(j, (c - j) % n) for j in range(n)]
                    parts = cc(n, edges)
                    reduced = all((part & actual for part in parts))
                    arithmetic = gcd(n, 2 * (b - a), c - 2 * a)
                    assert reduced == (arithmetic == 1)
                    if b != a:
                        assert (c - a - b - r) % n == 0
                    if reduced:
                        stats['reduced_diagrams'] += 1
                        stats['repeated_axis_reduced'] += a == b
                        assert len(parts) == 1
                        assert genus(-12 * n, 4) == 12 * r - 1
                    else:
                        stats['closed_component_rejections'] += 1
    return dict(stats)

def trajectory_prisms():
    rng = random.Random(2410202603)
    stats = Counter()
    for _ in range(300):
        colors = rng.randint(2, 5)
        labels = list(range(rng.randint(colors, 40)))
        coloring = list(range(colors)) + [rng.randrange(colors) for _ in labels[colors:]]
        rng.shuffle(coloring)
        alive = [{j for j in labels if coloring[j] == c} for c in range(colors)]
        trajectories = []
        for color in range(colors):
            remaining = set(alive[color])
            events = []
            while remaining:
                first = min(remaining)
                deleted = {first} | {j for j in remaining if rng.randrange(3) == 0}
                events.append((first, deleted))
                remaining -= deleted
            trajectories.append(events)
        order = sorted(((label, c, k) for (c, traj) in enumerate(trajectories) for (k, (label, deleted)) in enumerate(traj)))
        current = [set(a) for a in alive]
        for (label, c, k) in order:
            assert label == min(set().union(*current))
            current[c] -= trajectories[c][k][1]
            stats['empty_end_events'] += 1
        assert not set().union(*current)
        lengths = [len(traj) for traj in trajectories]

        def slabs(face):
            height = [Fraction(0)] * colors
            out = []
            for (label, c, k) in order:
                if c not in face:
                    continue
                old = tuple(height)
                height[c] += Fraction(1, lengths[c])
                out.append((c, old, tuple(height)))
            return out
        full_slabs = slabs(set(range(colors)))
        for size in range(1, colors + 1):
            for subset in combinations(range(colors), size):
                face = set(subset)
                local = slabs(face)
                restricted = [(c, tuple((h[i] if i in face else Fraction(0) for i in range(colors))), tuple((g[i] if i in face else Fraction(0) for i in range(colors)))) for (c, h, g) in full_slabs if c in face]
                assert local == restricted
                stats['nonempty_face_checks'] += 1
                mass = [rng.randint(1, 9) if i in face else 0 for i in range(colors)]
                x = [Fraction(a, sum(mass)) for a in mass]
                for numerator in range(8):
                    tau = Fraction(numerator, 7)
                    valid = 0
                    for (c, h, g) in local:
                        lower = sum((a * b for (a, b) in zip(x, h)))
                        upper = sum((a * b for (a, b) in zip(x, g)))
                        if not lower <= tau <= upper:
                            continue
                        new = (tau - lower) * lengths[c]
                        old = x[c] - new
                        assert 0 <= new <= x[c] and old >= 0
                        assert sum((x[i] for i in face - {c})) + old + new == 1
                        assert sum((x[i] * h[i] for i in face - {c})) + old * h[c] + new * g[c] == tau
                        valid += 1
                    assert valid >= 1
                    stats['rational_prism_probes'] += 1
        stats['families'] += 1
    return dict(stats)

def main():
    start = time.monotonic()
    tasks = [pants_degree, two_feature_caps, weighted_packets, peripheral_equations, framing_lattices, multiport_closures, examples, proposition_H_catalogue, proposition_M, trajectory_prisms]
    for task in tasks:
        result = task()
        print(json.dumps({task.__name__: result}, ensure_ascii=False), flush=True)
    print(json.dumps(dict(status='PASS'), ensure_ascii=False))
if __name__ == '__main__':
    main()
