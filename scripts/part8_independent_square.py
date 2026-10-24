#!/usr/bin/env python3
# Finite exact diagnostic for Part 8 of the proof; standard library only; prints a deterministic report and writes no files.
import argparse
from collections import Counter, deque
from hashlib import sha256
from math import gcd
from pathlib import Path
import json

def insist(test, data):
    if not test:
        raise AssertionError(data)

def adjacency(size, pairs):
    graph = [set() for _ in range(size)]
    for (a, b) in pairs:
        insist(a != b, ('fixed point', a))
        graph[a].add(b)
        graph[b].add(a)
    return graph

def component(graph, start, omitted=None):
    seen = {start}
    queue = deque([start])
    while queue:
        here = queue.popleft()
        for nxt in graph[here]:
            if omitted is not None and frozenset((here, nxt)) == omitted:
                continue
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen

def colour(graph, positive, negative):
    labels = {positive: 1, negative: -1}
    queue = deque(labels)
    while True:
        while queue:
            here = queue.popleft()
            for nxt in graph[here]:
                if nxt in labels:
                    if labels[nxt] != -labels[here]:
                        return None
                else:
                    labels[nxt] = -labels[here]
                    queue.append(nxt)
        missing = next((i for i in range(len(graph)) if i not in labels), None)
        if missing is None:
            return tuple((labels[i] for i in range(len(graph))))
        labels[missing] = 1
        queue.append(missing)

def pieces(r, *offsets):
    n = 2 * r
    pattern = [(i, n - i) for i in range(1, r)]
    leaves = [(i, (c - i) % n) for c in offsets for i in range(n) if i < (c - i) % n]
    return (adjacency(n, pattern + leaves), pattern)

def width(word):
    height = low = high = 0
    for sign in word:
        height -= sign
        (low, high) = (min(low, height), max(high, height))
    insist(height == 0, ('nonzero period', word))
    return high - low

def graph_parent(r, c):
    (graph, _) = pieces(r, c)
    removed = frozenset((1, 2 * r - 1))
    kept = component(graph, r, removed)
    (start,) = kept & removed
    ordered = sorted(kept, key=lambda x: (x - start) % (2 * r))
    relabel = {x: i for (i, x) in enumerate(ordered)}
    target_r = len(ordered) // 2
    target_c = relabel[(c - start) % (2 * r)]
    insist(relabel[r] == target_r, (r, c, 'negative tether', ordered))
    insist(0 < target_r < r, (r, c, 'strict decrease'))
    insist(target_c % 2 == 1 and gcd(target_c, 2 * target_r) == 1, (r, c, 'target unit', target_r, target_c))
    for x in ordered:
        insist(relabel[(c - x) % (2 * r)] == (target_c - relabel[x]) % (2 * target_r), (r, c, 'induced reflection', x))
    signs = colour(graph, 0, r)
    target_signs = colour(pieces(target_r, target_c)[0], 0, target_r)
    insist(tuple((signs[x] for x in ordered)) == target_signs, (r, c, 'inherited orientation'))
    return (target_r, target_c)

def farey_lower_neighbours(r, c):
    result = []
    for s in range(1, r):
        for sign in (-1, 1):
            numerator = c * s + sign
            if numerator % r:
                continue
            d = numerator // r
            if 0 < d < 2 * s and d % 2 and (gcd(d, s) == 1):
                result.append((s, d))
    return result

def nodes(limit):
    return [(r, c) for r in range(1, limit + 1) for c in range(1, 2 * r, 2) if gcd(c, r) == 1]

def check_two_reflections(limit):
    counts = Counter()
    for r in range(1, limit + 1):
        for a in range(1, 2 * r, 2):
            for b in range(1, 2 * r, 2):
                counts['offset_pairs'] += 1
                (graph, _) = pieces(r, a, b)
                signs = colour(graph, 0, r)
                if signs is None:
                    continue
                counts['compatible'] += 1
                insist(a == b, (r, a, b, 'different reflections survived'))
                connected = len(component(graph, 0)) == 2 * r
                insist(connected == (gcd(a, 2 * r) == 1), (r, a, 'gcd versus no closed components'))
                counts['connected'] += connected
    return dict(counts)

def check_sign_defects(limit=12):
    counts = Counter()
    for r in range(1, limit + 1):
        n = 2 * r
        for bits in range(1 << r - 1):
            signs = [0] * n
            (signs[0], signs[r]) = (1, -1)
            for i in range(1, r):
                signs[i] = 1 if bits & 1 << i - 1 else -1
                signs[n - i] = -signs[i]
            counts['pattern_compatible_words'] += 1
            for shift in range(1, n):
                insist(any((signs[i] != signs[(i + shift) % n] for i in range(n))), (r, signs, 'nonzero signed period', shift))
                counts['nonzero_shifts_excluded'] += 1
            eligible = [c for c in range(1, n, 2) if all((signs[(c - i) % n] == -signs[i] for i in range(n)))]
            insist(len(eligible) <= 1, (r, signs, eligible))
    return dict(counts)

def check_parents(limit):
    (depths, parents) = ({}, {})
    counts = Counter()
    samples = []
    for (r, c) in nodes(limit):
        (graph, pattern) = pieces(r, c)
        insist(len(component(graph, 0)) == 2 * r, (r, c, 'not a path'))
        signs = colour(graph, 0, r)
        insist(signs is not None, (r, c, 'no orientation'))
        for edge in pattern:
            side = component(graph, 0, frozenset(edge))
            insist(r not in side and 2 <= len(side) <= 2 * r - 2, (r, c, edge, 'return not a positive-genus bridge'))
            counts['bridges'] += 1
        if r == 1:
            depths[r, c] = 1
        else:
            target = graph_parent(r, c)
            lower = farey_lower_neighbours(r, c)
            insist(lower == [target], (r, c, 'Farey parent mismatch', lower, target))
            inv = pow(c, -1, 2 * r)
            insist(target[0] == r - min(inv, 2 * r - inv), (r, c, 'inverse formula', target))
            parents[r, c] = target
            depths[r, c] = depths[target] + 1
            insist(width(signs) == width(colour(pieces(*target)[0], 0, target[0])) + 1, (r, c, 'potential width failed to decrease by one'))
            counts['parent_comparisons'] += 1
            if (r, c) in {(4, 3), (5, 3), (8, 3), (12, 5), (32, 17)}:
                samples.append({'source': [r, c], 'target': target, 'word': ''.join(('+' if x > 0 else '-' for x in signs)), 'width': width(signs)})
        insist(depths[r, c] == width(signs), (r, c, 'depth versus potential'))
        insist(1 <= width(signs) <= r and (width(signs) == 1) == (r == 1), (r, c, 'annular width bounds'))
        if c == 1:
            insist(width(signs) == r, (r, 'upstream s_r family'))
            counts['s_r_equalities'] += 1
        counts['unit_data'] += 1
    return (dict(counts, samples=samples), parents, depths)

def bfs(graph, source):
    distances = {source: 0}
    queue = deque([source])
    while queue:
        here = queue.popleft()
        for nxt in graph[here]:
            if nxt not in distances:
                distances[nxt] = distances[here] + 1
                queue.append(nxt)
    return distances

def check_metric(limit, parents, depths):
    data = nodes(limit)
    base_edges = [(x, y) for (i, x) in enumerate(data) for y in data[i + 1:] if abs(x[1] * y[0] - y[1] * x[0]) == 1]
    graph = {'a': set(), 'v': {'a'}}
    graph['a'].add('v')
    predecessor = {'v': 'a'}
    heights = {'a': 0, 'v': 1}
    for omega in (0, 1):
        for x in data:
            key = (omega, *x)
            graph[key] = set()
            predecessor[key] = 'a' if x == (1, 1) else (omega, *parents[x])
            heights[key] = depths[x]
        root = (omega, 1, 1)
        graph['a'].add(root)
        graph[root].add('a')
        for (x, y) in base_edges:
            graph[(omega, *x)].add((omega, *y))
            graph[(omega, *y)].add((omega, *x))
    comparisons = 0
    for source in graph:
        observed = bfs(graph, source)
        insist(len(observed) == len(graph), 'Farey sample disconnected')
        ancestors = set()
        x = source
        while True:
            ancestors.add(x)
            if x == 'a':
                break
            x = predecessor[x]
        for target in graph:
            x = target
            while x not in ancestors:
                x = predecessor[x]
            expected = heights[source] + heights[target] - 2 * heights[x]
            insist(observed[target] == expected, (source, target, 'LCA metric', expected, observed[target]))
            comparisons += 1
    return {'max_r': limit, 'arithmetic_vertices': len(data), 'determinant_edges_per_copy': len(base_edges), 'vertices_with_two_ancestor_labels_and_a_v': len(graph), 'ordered_BFS_distance_comparisons': comparisons}

def check_families(limit=32):
    counts = Counter()
    for k in range(2, 5):
        for total in range(k, limit + 1):
            n = 2 * total
            for c in range(1, n, 2):
                pairs = [(i, (k - 1 - i) % n) for i in range(k, total)]
                pairs += [(i, (c - i) % n) for i in range(n) if i < (c - i) % n]
                graph = adjacency(n, pairs)
                parts = [component(graph, a) for a in range(k)]
                valid = all((len(part & set(range(k))) == 1 and len(part & set(range(total, total + k))) == 1 for part in parts))
                valid = valid and len(set.union(*parts)) == n
                valid = valid and sum(map(len, parts)) == n
                if not valid:
                    continue
                strata = []
                for (start, part) in enumerate(parts):
                    cyclic = sorted(part, key=lambda x: (x - start) % n)
                    index = {x: i for (i, x) in enumerate(cyclic)}
                    r = len(part) // 2
                    offset = index[(c - start) % n]
                    insist(offset % 2 and gcd(offset, 2 * r) == 1, (k, total, c, start, 'individual unit'))
                    strata.append((r, offset))
                distinct = sorted(set(strata))
                insist(len(distinct) <= 2, (k, total, c, 'three arithmetic strata', strata))
                if len(distinct) == 2:
                    (low, high) = distinct
                    insist(low[0] < high[0] and graph_parent(*high) == low, (k, total, c, 'edge not arithmetic parent', strata))
                    counts['two_stratum_families'] += 1
                counts[f'valid_{k}_occurrence_families'] += 1
    return dict(counts)

def multiply(*words):
    out = []
    for word in words:
        for (factor, exponent) in word:
            if out and out[-1][0] == factor:
                exponent = (exponent + out.pop()[1]) % factor
            else:
                exponent %= factor
            if exponent:
                out.append((factor, exponent))
    return tuple(out)

def inverse(word):
    return tuple(((factor, -exponent % factor) for (factor, exponent) in reversed(word)))

def power(word, k):
    if k < 0:
        (word, k) = (inverse(word), -k)
    return multiply(*(word for _ in range(k)))

def check_leaf_quotient(limit=64):
    (x, y) = (((2, 1),), ((3, 1),))
    boundary = inverse(multiply(x, y))
    counts = Counter()
    for k in range(-limit, limit + 1):
        d = power(boundary, k)
        conjugate = multiply(d, x, inverse(d))
        insist((conjugate == x) == (k == 0), (k, 'boundary centralised order-two generator'))
        counts['conjugation_tests'] += 1
    return dict(counts)

def main():

    class args:
        (max_r, metric_r, reflection_r) = (128, 20, 32)
    insist(2 <= args.metric_r <= args.max_r, '2 <= metric-r <= max-r required')
    (arithmetic, parents, depths) = check_parents(args.max_r)
    result = {'two_reflection_rigidity': check_two_reflections(args.reflection_r), 'all_sign_words_with_two_defects': check_sign_defects(), 'graph_deletion_vs_Farey_parent': arithmetic, 'independent_determinant_graph_metric': check_metric(args.metric_r, parents, depths), 'common_packet_necessary_combinatorics': check_families(), 'C2_free_C3_normal_forms': check_leaf_quotient(), 'limits': ['No enumeration of ordinary surface-isotopy classes.', 'No computational proof of torus-preserving comparison, common products, or rectangle lifting.', 'Farey adjacency is an independent arithmetic cross-check, not an asserted replacement for the geometric proof.', 'The geometric identification of potential oscillation with cyclic class distance is reviewed in the report.']}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print('PASS: independent finite diagnostics for Part 8, sections 2-10')
if __name__ == '__main__':
    main()
