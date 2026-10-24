#!/usr/bin/env python3
# Finite exact diagnostic for Part 8 of the proof; standard library only; prints a deterministic report and writes no files.
from collections import Counter, deque
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from math import gcd
from pathlib import Path
HERE = Path(__file__).resolve().parent

def require(condition, detail):
    if not condition:
        raise AssertionError(detail)

def edges(r, offsets):
    n = 2 * r
    out = [(i, -i % n) for i in range(1, r)]
    for c in offsets:
        out.extend(((i, (c - i) % n) for i in range(n) if i < (c - i) % n))
    return out

def colouring(r, offsets):
    n = 2 * r
    adj = [[] for _ in range(n)]
    for (i, j) in edges(r, offsets):
        adj[i].append(j)
        adj[j].append(i)
    colours = {0: 1, r: -1}
    reached_from_zero = set()
    queue = deque([0])
    while queue:
        i = queue.popleft()
        if i in reached_from_zero:
            continue
        reached_from_zero.add(i)
        queue.extend(adj[i])
    queue = deque([0, r])
    while True:
        while queue:
            i = queue.popleft()
            for j in adj[i]:
                if j in colours:
                    if colours[j] != -colours[i]:
                        return (None, len(reached_from_zero))
                else:
                    colours[j] = -colours[i]
                    queue.append(j)
        missing = next((i for i in range(n) if i not in colours), None)
        if missing is None:
            break
        colours[missing] = 1
        queue.append(missing)
    return (colours, len(reached_from_zero))

def unit_path(r, c):
    n = 2 * r
    require(gcd(c, n) == 1 and c % 2, (r, c, 'unit'))
    path = [0]
    for k in range(1, r):
        path.extend([k * c % n, -k * c % n])
    path.append(r)
    require(len(path) == n and len(set(path)) == n, (r, c, 'path'))
    return path

def sign_word(r, c):
    path = unit_path(r, c)
    signs = {node: 1 if j % 2 == 0 else -1 for (j, node) in enumerate(path)}
    return [signs[i] for i in range(2 * r)]

def oscillation(word):
    heights = [0]
    for sign in word:
        heights.append(heights[-1] - sign)
    require(heights[-1] == 0, (word, 'unbalanced'))
    return max(heights) - min(heights)

def parent_data(r, c):
    require(r > 1, 'annular root has no signed parent data')
    n = 2 * r
    path = unit_path(r, c)
    cut = next((j for j in range(1, n - 1, 2) if {path[j], path[j + 1]} == {1, n - 1}))
    suffix = path[cut + 1:]
    rp = len(suffix) // 2
    origin = suffix[0]
    cyclic = sorted(suffix, key=lambda i: (i - origin) % n)
    index = {old: new for (new, old) in enumerate(cyclic)}
    cp = index[(c - origin) % n]
    require(index[r] == rp, (r, c, 'new negative tether'))
    require(0 < rp < r and cp % 2 and (gcd(cp, 2 * rp) == 1), (r, c, rp, cp, 'parent unit'))
    for i in suffix:
        require(index[(c - i) % n] == (cp - index[i]) % (2 * rp), (r, c, i, 'retained leaf reflection'))
    for j in range(1, len(suffix) - 1, 2):
        (x, y) = (suffix[j], suffix[j + 1])
        require((x + y) % n == 0, 'old pattern edge retained')
        require((index[x] + index[y]) % (2 * rp) == 0, (r, c, 'new pattern reflection'))
    old_word = sign_word(r, c)
    require([old_word[i] for i in cyclic] == sign_word(rp, cp), (r, c, 'inherited signs'))
    inverse = pow(c, -1, n)
    q = min(inverse, n - inverse)
    require(rp == r - q, (r, c, 'inverse suffix formula'))
    return (rp, cp)

def check_rigidity(limit=48):
    cases = compatible = reduced = 0
    for r in range(1, limit + 1):
        n = 2 * r
        for cp in range(1, n, 2):
            for cm in range(1, n, 2):
                cases += 1
                (signs, reach) = colouring(r, (cp, cm))
                if signs is None:
                    continue
                compatible += 1
                require(cp == cm, (r, cp, cm, 'different leaf matchings'))
                require((reach == n) == (gcd(cp, n) == 1), (r, cp, 'reducedness versus gcd'))
                if reach == n:
                    reduced += 1
                    require([signs[i] for i in range(n)] == sign_word(r, cp), (r, cp, 'unique reduced signs'))
    return dict(offset_pairs=cases, compatible=compatible, reduced=reduced)

def check_parents(limit=256):
    cases = parent_cases = 0
    depths = {}
    examples = {}
    for r in range(1, limit + 1):
        for c in range(1, 2 * r, 2):
            if gcd(c, 2 * r) != 1:
                continue
            cases += 1
            word = sign_word(r, c)
            require(word.count(1) == word.count(-1) == r, (r, c, 'signs'))
            for (x, y) in edges(r, (c, c)):
                require(word[x] == -word[y], (r, c, x, y))
            distance = oscillation(word)
            require(1 <= distance <= r and (distance == 1) == (r == 1), (r, c, distance, 'root width bounds'))
            if r == 1:
                depths[r, c] = 1
            else:
                (rp, cp) = parent_data(r, c)
                parent_cases += 1
                depths[r, c] = 1 + depths[rp, cp]
                require(distance == 1 + oscillation(sign_word(rp, cp)), (r, c, 'root distance did not drop one'))
            require(depths[r, c] == distance, (r, c, 'depth versus direct chamber width'))
            if c == 1:
                require(distance == r, (r, 'Part 7 unbounded family'))
            if (r, c) in {(4, 3), (5, 3), (8, 3), (12, 5)}:
                examples[f'r={r},c={c}'] = dict(word=''.join(('+' if x == 1 else '-' for x in word)), root_width=distance, parent=parent_data(r, c))
    return dict(unit_normal_data=cases, parent_checks=parent_cases, examples=examples)

def family_paths(k, total, c):
    n = 2 * total
    leaf = {i: (c - i) % n for i in range(n)}
    pattern = {i: (k - 1 - i) % n for i in range(k, total)}
    pattern.update({j: i for (i, j) in list(pattern.items())})
    (paths, used) = ([], set())
    for start in range(k):
        path = [start]
        current = start
        while True:
            nxt = leaf[current]
            if nxt in path:
                return None
            path.append(nxt)
            if nxt not in pattern:
                break
            current = pattern[nxt]
            if current in path:
                return None
            path.append(current)
        if not total <= path[-1] < total + k or set(path) & used:
            return None
        used.update(path)
        paths.append(tuple(path))
    if len(used) != n:
        return None
    return paths

def return_events(paths, k, total):
    current = list(paths)
    events = []
    while True:
        candidates = []
        for (label, path) in enumerate(current):
            for j in range(1, len(path) - 1, 2):
                (a, b) = path[j:j + 2]
                rank = a if k <= a < total else b
                require(k <= rank < total, (path, 'return rank'))
                candidates.append((rank, label, j))
        if not candidates:
            return (events, current)
        (_, label, j) = min(candidates)
        old = current[label]
        new = old[j + 1:]
        require(len(new) >= 2 and len(new) < len(old), 'strict suffix')
        events.append((label, old, new))
        current[label] = new

def timed_state(paths, events, weights, time):
    current = list(paths)
    bary = Counter()
    clock = Fraction(0)
    for (label, old, new) in events:
        duration = weights[label]
        require(current[label] == old, 'event state mismatch')
        if duration and time < clock + duration:
            for (i, path) in enumerate(current):
                bary[i, path] += weights[i]
            moved = max(Fraction(0), time - clock)
            bary[label, old] -= moved
            bary[label, new] += moved
            return {key: value for (key, value) in bary.items() if value}
        current[label] = new
        clock += duration
    return {(i, path): weights[i] for (i, path) in enumerate(current) if weights[i]}

def check_families(limit=36):
    counts = Counter()
    face_checks = timing_checks = 0
    for k in range(1, 7):
        for total in range(k, limit + 1):
            for c in range(1, 2 * total, 2):
                paths = family_paths(k, total, c)
                if paths is None:
                    continue
                counts[k] += 1
                genera = [len(path) // 2 for path in paths]
                require(len(set(genera)) <= 2, (k, total, c, 'three different genera in a common packet'))
                (events, terminal) = return_events(paths, k, total)
                require(all((len(path) == 2 for path in terminal)), 'terminal tether state')
                require(len(events) <= total - k, 'return-count termination')
                for omit in range(k):
                    reduced_paths = [path for (i, path) in enumerate(paths) if i != omit]
                    (reduced_events, _) = return_events(reduced_paths, k, total)
                    relabel = {i: i if i < omit else i - 1 for i in range(k) if i != omit}
                    projected = [(relabel[i], old, new) for (i, old, new) in events if i != omit]
                    require(projected == reduced_events, (k, total, c, omit, 'face event order'))
                    face_checks += 1
                if k == 2 and total <= 12:
                    for a in range(5):
                        weights = [Fraction(a, 4), Fraction(4 - a, 4)]
                        duration = sum((weights[i] for (i, _, _) in events))
                        for j in range(9):
                            time = duration * Fraction(j, 8)
                            state = timed_state(paths, events, weights, time)
                            require(sum(state.values()) == 1 and min(state.values()) > 0, 'barycentric interpolation')
                            timing_checks += 1
    return dict(common_packet_families=dict(sorted(counts.items())), deletion_checks=face_checks, weighted_checks=timing_checks, note='Includes parallel occurrences; not counts of distinct simplices.')

def check_modes():
    knots = [(2, 3), (2, -3), (2, 5), (2, -5), (3, 10), (2, -15)]
    mode_count = 0
    named = {}
    for size in range(2, 6):
        for chosen in combinations(knots, size):
            framings = [p * q for (p, q) in chosen]
            genera = [(p - 1) * (abs(q) - 1) // 2 for (p, q) in chosen]
            for mask in range(1, 1 << size):
                vertical = [i for i in range(size) if mask & 1 << i]
                if sum((framings[i] for i in vertical)):
                    continue
                mode_count += 1
                horizontal = [i for i in range(size) if i not in vertical]
                b = len(vertical) - 1 + 2 * sum((genera[i] for i in horizontal))
                require(len(vertical) >= 2 and b > 0, 'positive companion genus')
                eta = [1] + [-framings[i] if i in vertical else 0 for i in range(size)]
                require(sum(eta[1:]) == 0, 'outer longitude kernel')
                for i in vertical:
                    require(eta[i + 1] + framings[i] * eta[0] == 0, 'vertical kernel')
                for r in (1, 2, 7, 31):
                    chi = 2 * r * (1 - size)
                    chi += sum((2 * r * (1 - 2 * genera[i]) for i in horizontal))
                    require(chi == -2 * r * b, 'Euler genus formula')
    for (name, chosen) in {'square': [(2, 3), (2, -3)], 'granny': [(2, 3), (2, 3)], 'square_plus_trefoil': [(2, 3), (2, -3), (2, 3)], 'different_torus_knots_same_opposite_framing': [(3, 10), (2, -15)]}.items():
        ss = [p * q for (p, q) in chosen]
        gg = [(p - 1) * (abs(q) - 1) // 2 for (p, q) in chosen]
        vv = []
        for mask in range(1, 1 << len(chosen)):
            v = [i for i in range(len(chosen)) if mask & 1 << i]
            if sum((ss[i] for i in v)) == 0:
                b = len(v) - 1 + 2 * sum((gg[i] for i in range(len(chosen)) if i not in v))
                vv.append(dict(vertical=[i + 1 for i in v], companion_genus=b))
        named[name] = vv
    return dict(zero_sum_modes=mode_count, named=named)

def recursive_profiles(tree):
    kind = tree[0]
    if kind == 'torus':
        (_, p, q) = tree
        g = (p - 1) * (abs(q) - 1) // 2
        return [(0, g, 0, ()), (p * q, 0, 1, ((1, p * q),))]
    if kind == 'sum':
        result = []
        for choices in product(*(recursive_profiles(child) for child in tree[1:])):
            result.append((sum((x[0] for x in choices)), sum((x[1] for x in choices)), sum((x[2] for x in choices)), tuple((term for x in choices for term in x[3]))))
        return result
    if kind == 'cable':
        (_, p, q, child) = tree
        require(p >= 2 and q and (gcd(p, q) == 1), 'genuine cable parameters')
        result = [(p * q, 0, 1, ((1, p * q),))]
        for (t, g, boundary_count, terminals) in recursive_profiles(child):
            numerator = (p - 1) * (abs(q - p * t) - 1)
            require(numerator >= 0 and numerator % 2 == 0, 'horizontal cable genus')
            gp = p * g + numerator // 2
            qp = p * boundary_count
            chip = -(p - 1) * abs(q - p * t) + p * (1 - 2 * g - boundary_count)
            require(chip == 1 - 2 * gp - qp, 'horizontal cable Euler characteristic')
            result.append((p * p * t, gp, qp, tuple(((p * w, slope) for (w, slope) in terminals))))
        return result
    raise AssertionError(tree)

def check_recursive_modes():
    trefoil = ('torus', 2, 3)
    mirror = ('torus', 2, -3)
    square = ('sum', trefoil, mirror)
    examples = {'cable_2_1_square': ('cable', 2, 1, square), 'cable_3_minus2_cable_2_1_square': ('cable', 3, -2, ('cable', 2, 1, square)), 'vertical_cable_terminal': ('sum', ('cable', 2, 3, trefoil), mirror), 'horizontal_cable_cancellation': ('sum', ('cable', 2, 1, trefoil), ('torus', 3, -8)), 'no_cancellation': ('sum', ('cable', 2, 1, trefoil), mirror)}
    expected = {'cable_2_1_square': [3], 'cable_3_minus2_cable_2_1_square': [13], 'vertical_cable_terminal': [1], 'horizontal_cable_cancellation': [12], 'no_cancellation': []}
    records = {}
    profile_checks = 0
    for (name, tree) in examples.items():
        profiles = recursive_profiles(tree)
        zero = []
        fibred = 0
        for (t, g, terminal_count, terminals) in profiles:
            profile_checks += 1
            require(t == sum((w * w * slope for (w, slope) in terminals)), (name, 'weighted terminal slope'))
            require(terminal_count == sum((w for (w, _) in terminals)), (name, 'terminal phase degree'))
            if t == 0:
                if not terminals:
                    fibred += 1
                else:
                    require(len(terminals) >= 2 and terminal_count >= 2, 'one terminal cannot cancel')
                    zero.append(2 * g + terminal_count - 1)
        require(fibred == 1, (name, 'unique horizontal fibre mode'))
        require(sorted(zero) == expected[name], (name, zero, 'named cancellation genus'))
        records[name] = dict(profiles=len(profiles), cancellation_companion_genera=zero)
    for p in range(2, 8):
        for q in range(-9, 10):
            if not q or gcd(p, q) != 1:
                continue
            profiles = recursive_profiles(('cable', p, q, square))
            zero = [(g, b) for (t, g, b, _) in profiles if t == 0 and b]
            require(len(zero) == 1, 'cabled square cancellation mode')
            (g, b) = zero[0]
            require(2 * g + b - 1 == p + (p - 1) * abs(q), 'cabled genus recursion')
            profile_checks += len(profiles)
    return dict(profile_checks=profile_checks, examples=records)

def check_repeated_words():
    checks = gap_checks = 0
    for r in range(1, 25):
        n = 2 * r
        for c in range(1, n, 2):
            if gcd(c, n) != 1:
                continue
            signs = sign_word(r, c)
            for degree in range(1, 9):
                size = n * degree
                for offset in range(c, size, n):
                    checks += 1
                    pairs = Counter()
                    for i in range(size):
                        j = (offset - i) % size
                        require(signs[i % n] == -signs[j % n], 'repeated-word opposite ends')
                        require(j % n == (c - i) % n, 'induced root reflection')
                        if i < j:
                            pairs[tuple(sorted((i % n, j % n)))] += 1
                    require(set(pairs.values()) == {degree}, 'degree annuli per root pair')
                    for i in range(size):
                        j = (offset - i - 1) % size
                        require(j % n == (c - i - 1) % n, 'projected gap involution')
                        if i == j:
                            require(i % n == (c - i - 1) % n, 'terminal endcap escaped a fixed root gap')
                        gap_checks += 1
    return dict(repeated_terminal_reflections=checks, projected_gaps=gap_checks)

def check_arithmetic_tree(limit=16):
    omega = ((0, 0, 0, 0), (1, 0, 0, 0), (0, 0, 1, 0))
    arithmetic = [(r, c) for r in range(1, limit + 1) for c in range(1, 2 * r, 2) if gcd(c, 2 * r) == 1]
    (root, capped) = (('a',), ('v',))
    graph = {root: {capped}, capped: {root}}
    parent = {capped: root}
    for label in omega:
        for (r, c) in arithmetic:
            node = (label, r, c)
            p = root if r == 1 else (label, *parent_data(r, c))
            parent[node] = p
            graph.setdefault(node, set()).add(p)
            graph.setdefault(p, set()).add(node)
    require(sum(map(len, graph.values())) // 2 == len(graph) - 1, 'tree edge count')
    chains = {root: [root]}
    for node in graph:
        chain = [node]
        while chain[-1] != root:
            chain.append(parent[chain[-1]])
        chains[node] = chain
    comparisons = 0
    for source in graph:
        dist = {source: 0}
        queue = deque([source])
        while queue:
            node = queue.popleft()
            for other in graph[node]:
                if other not in dist:
                    dist[other] = dist[node] + 1
                    queue.append(other)
        require(len(dist) == len(graph), 'finite arithmetic tree connectedness')
        for (target, breadth_first) in dist.items():
            common = next((x for x in chains[source] if x in set(chains[target])))
            formula = len(chains[source]) - 1 + (len(chains[target]) - 1)
            formula -= 2 * (len(chains[common]) - 1)
            require(formula == breadth_first, 'ancestor formula versus independent BFS')
            comparisons += 1
    for label in omega:
        for (r, c) in arithmetic:
            node = (label, r, c)
            require(len(chains[node]) - 1 == oscillation(sign_word(r, c)), 'arithmetic copy root width')
    return dict(sample_ancestor_labels=len(omega), arithmetic_nodes=len(arithmetic), total_vertices=len(graph), distance_comparisons=comparisons, note='Verifies the stated arithmetic model, not its geometric identification.')

def check_leaf_loop_words():
    orders = (2, 3)

    def multiply(a, b):
        result = list(a)
        for (factor, power) in b:
            if result and result[-1][0] == factor:
                power = (result.pop()[1] + power) % orders[factor]
            if power:
                result.append((factor, power))
        return tuple(result)

    def inverse(a):
        return tuple(((factor, -power % orders[factor]) for (factor, power) in reversed(a)))

    def power(a, k):
        if k < 0:
            return power(inverse(a), -k)
        result = ()
        for _ in range(k):
            result = multiply(result, a)
        return result
    (x, y) = (((0, 1),), ((1, 1),))
    d = inverse(multiply(x, y))
    cases = 0
    for k in range(-64, 65):
        conjugate = multiply(multiply(power(d, k), x), power(d, -k))
        require((conjugate == x) == (k == 0), (k, 'leaf centraliser word'))
        cases += 1
    return dict(boundary_conjugation_cases=cases, note='Finite free-product checks; the no-winding proof is §10.2.')

def check_one_boundary_caps():
    cases = closed_removed = 0
    for actual_count in range(2, 7):
        for signs in product((1, -1), repeat=actual_count):
            total_sign = sum(signs)
            for positive_outer in range(4):
                negative_outer = positive_outer + total_sign
                if negative_outer < 0 or positive_outer + negative_outer > 6:
                    continue
                positive = [('actual', i) for (i, s) in enumerate(signs) if s > 0]
                negative = [('actual', i) for (i, s) in enumerate(signs) if s < 0]
                positive += [('outer', i) for i in range(positive_outer)]
                negative += [('outer', positive_outer + i) for i in range(negative_outer)]
                require(len(positive) == len(negative), 'oriented arc-end balance')
                for target in permutations(negative):
                    actual_uses = Counter()
                    retained_fibre_degree = 0
                    for (x, y) in zip(positive, target):
                        if x[0] == y[0] == 'outer':
                            closed_removed += 1
                            continue
                        for node in (x, y):
                            if node[0] == 'actual':
                                actual_uses[node[1]] += 1
                        if x[0] != y[0]:
                            actual = x if x[0] == 'actual' else y
                            retained_fibre_degree += signs[actual[1]]
                    require(actual_uses == Counter({i: 1 for i in range(actual_count)}), 'closed deletion lost an actual boundary')
                    require(retained_fibre_degree == total_sign, 'closed deletion changed degree')
                    cases += 1
    return dict(oriented_arc_pairings=cases, closed_cap_pairs_deleted=closed_removed, note='Graph diagnostic includes nonplanar pairings; no surface-isotopy enumeration.')

def check_four_parallel_obstruction():
    signs = (1, -1, 1, -1)
    offsets = (1, 3)
    graph = [set() for _ in range(4)]
    for c in offsets:
        for i in range(4):
            j = (c - i) % 4
            require(signs[i] == -signs[j], 'four-parallel orientation')
            graph[i].add(j)
    (seen, queue) = (set(), deque([0]))
    while queue:
        i = queue.popleft()
        if i not in seen:
            seen.add(i)
            queue.extend(graph[i])
    require(len(seen) == 4 and all((len(x) == 2 for x in graph)), 'connected four-cycle')
    (chi, boundary) = (-4, 4)
    genus = (2 - boundary - chi) // 2
    require(genus == 1 and offsets[0] != offsets[1], 'four-boundary companion')
    return dict(section_word='+-+-', leaf_offsets=offsets, companion_boundaries=boundary, genus=genus, note='Obstructs the two-boundary proof mechanism, not contractibility.')

def main():
    results = {'matching_rigidity': check_rigidity(), 'parent_and_distance': check_parents(), 'common_packet_diagnostics': check_families(), 'torus_sum_modes': check_modes(), 'recursive_sum_cable_modes': check_recursive_modes(), 'nonunit_terminal_words': check_repeated_words(), 'square_arithmetic_tree': check_arithmetic_tree(), 'leaf_loop_free_product': check_leaf_loop_words(), 'one_boundary_fibre_deletion': check_one_boundary_caps(), 'four_balanced_parallel_control': check_four_parallel_obstruction(), 'limits': ['No enumeration of ordinary isotopy classes or leaf twisting stabilisers.', 'No computational proof of the outer-torus product comparison.', 'No computational proof of the lifted empty-rectangle argument.', 'No claim about all graph-manifold links.']}
    print(json.dumps(results, ensure_ascii=False, indent=2))
    print('PASS: all stated finite arithmetic/combinatorial diagnostics')
if __name__ == '__main__':
    main()
