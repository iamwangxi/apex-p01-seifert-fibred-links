#!/usr/bin/env python3
"""Offline standard-library diagnostic; original calculation functions retained."""
from collections import Counter, deque
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from math import ceil, floor, gcd
COUNTS = Counter()

def linear_solve(matrix, rhs):
    a = [[Q(x) for x in row] + [Q(b)] for (row, b) in zip(matrix, rhs)]
    n = len(rhs)
    assert all((len(row) == n + 1 for row in a))
    for col in range(n):
        pivot = next((i for i in range(col, n) if a[i][col]))
        (a[col], a[pivot]) = (a[pivot], a[col])
        c = a[col][col]
        a[col] = [x / c for x in a[col]]
        for i in range(n):
            if i != col and a[i][col]:
                c = a[i][col]
                a[i] = [x - c * y for (x, y) in zip(a[i], a[col])]
    return tuple((row[-1] for row in a))

@dataclass(frozen=True)
class SeifertNode:
    p: int
    q: int
    actual: tuple
    ports: tuple
    retained: tuple = ()

    def linking(self, first, second):
        if first == second == 'R':
            return self.p * self.q
        if {first, second} == {'R', 'X'}:
            return self.q
        raise ValueError((first, second))

    def fibre_linking(self, kind):
        return self.p * self.q if kind == 'R' else self.q

    def fibre_slope(self, kind):
        return (self.p * self.q, 1) if kind == 'R' else (self.q, self.p)

    def orbifold_chi(self):
        return Q(2 - len(self.actual) - len(self.ports)) - sum((1 - Q(1, c) for c in self.retained), Q(0))

def splice_tree(nodes, edges):
    keys = tuple(((v, i) for (v, node) in enumerate(nodes) for i in range(len(node.ports))))
    index = {key: i for (i, key) in enumerate(keys)}
    mate = {}
    for (a, b) in edges:
        assert a not in mate and b not in mate
        (mate[a], mate[b]) = (b, a)
    assert set(mate) == set(keys)
    (matrix, rhs) = ([], [])
    for key in keys:
        (w, j) = mate[key]
        node = nodes[w]
        row = [0] * len(keys)
        row[index[key]] = 1
        for (k, kind) in enumerate(node.ports):
            if k != j:
                row[index[w, k]] -= node.linking(node.ports[j], kind)
        matrix.append(row)
        rhs.append(node.linking(node.ports[j], 'R') * sum(node.actual))
    solution = linear_solve(matrix, rhs)
    mu = dict(zip(keys, solution))
    assert all((x.denominator == 1 for x in solution))
    k_values = []
    for (v, node) in enumerate(nodes):
        value = node.fibre_linking('R') * sum(node.actual)
        value += sum((node.fibre_linking(kind) * mu[v, i] for (i, kind) in enumerate(node.ports)))
        assert value.denominator == 1
        k_values.append(int(value))
        assert node.actual
        assert all((value % order == 0 for order in node.retained))
    port_data = []
    for (a, b) in edges:
        (v, i) = a
        (w, j) = b
        (av, bv) = nodes[v].fibre_slope(nodes[v].ports[i])
        (aw, bw) = nodes[w].fibre_slope(nodes[w].ports[j])
        delta = abs(av * aw - bv * bw)
        assert delta > 0
        assert av * mu[a] + bv * mu[b] == k_values[v]
        assert aw * mu[b] + bw * mu[a] == k_values[w]
        div = gcd(abs(int(mu[a])), abs(int(mu[b])))
        if k_values[v] == k_values[w] == 0:
            assert div == 0
        else:
            assert div > 0
        port_data.append((div, delta, int(mu[a]), int(mu[b])))
    norm = sum((abs(k) * -node.orbifold_chi() for (k, node) in zip(k_values, nodes) if k))
    assert norm.denominator == 1
    return (tuple(k_values), tuple(port_data), int(norm))

def link_examples():
    six = (SeifertNode(1, -1, (1, -1), ('R', 'R')), SeifertNode(1, 1, (1, 1), ('R',)), SeifertNode(1, 1, (-1, -1), ('R',)))
    path = (((0, 0), (1, 0)), ((0, 1), (2, 0)))
    (k, data, norm) = splice_tree(six, path)
    assert k == (0, 4, -4) and norm == 8
    assert tuple((x[0] for x in data)) == (2, 2)
    assert Q(2 - 4 + 8, 2) == 3
    assert Q(2 - 6 + 8, 2) == 2
    print('six-component:', k, '(div, fibre-intersection, mu_v, mu_w)=', data, 'norm=', norm)
    all_zero = (six[0], SeifertNode(1, 1, (1, -1), ('R',)), SeifertNode(1, 1, (1, -1), ('R',)))
    (kz, dz, nz) = splice_tree(all_zero, path)
    assert kz == (0, 0, 0) and nz == 0
    assert tuple((x[:2] for x in dz)) == ((0, 2), (0, 2))
    print('all-zero:', kz, 'port-data=', dz, 'norm=', nz)
    four = (SeifertNode(1, -1, (1, 1, 1), ('R', 'R', 'R')), SeifertNode(1, 1, (1, 1), ('R',)), SeifertNode(1, 1, (1, 1), ('R',)), SeifertNode(2, 3, (-1,), ('X',), (3,)))
    star = path + (((0, 2), (3, 0)),)
    (k4, data4, norm4) = splice_tree(four, star)
    assert k4 == (-4, 0, 0, -27) and norm4 == 34
    assert tuple((x[0] for x in data4)) == (2, 2, 1)
    assert tuple((x[1] for x in data4)) == (2, 2, 5)
    assert Q(2 - 8 + norm4, 2) == 14
    print('four-block:', k4, 'port-data=', data4, 'norm=', norm4, 'global genus=14')
    five = (four[0], SeifertNode(1, 1, (1, 1), ('R', 'R')), four[2], four[3], SeifertNode(1, -1, (1, -1), ('R',)))
    tree = star + (((1, 1), (4, 0)),)
    (k5, data5, norm5) = splice_tree(five, tree)
    assert k5 == (-4, 0, 0, -27, 0) and norm5 == 34
    assert tuple((x[0] for x in data5)) == (2, 2, 1, 0)
    assert tuple((x[1] for x in data5)) == (2, 2, 5, 2)
    print('five-block:', k5, 'port-data=', data5, 'norm=', norm5, 'components=(genus14,b8)+(annulus)')
    COUNTS['new_S3_examples'] = 3
INVERSE = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}

def reduce_word(word):
    out = []
    for c in word:
        if out and out[-1] == INVERSE[c]:
            out.pop()
        else:
            out.append(c)
    return ''.join(out)

def inverse_word(word):
    return ''.join((INVERSE[c] for c in reversed(word)))

def coset(word):
    return word.rstrip('aA')

def cost(word):
    (result, in_a) = (0, False)
    for c in word:
        if c in 'aA':
            if not in_a:
                result += 2
            in_a = True
        else:
            result += 1
            in_a = False
    return result

def exact_six_distance(first, second):
    (kind1, g) = first
    (kind2, h) = second
    w = reduce_word(inverse_word(g) + h)
    if kind1 == kind2 == 'C':
        return cost(w)
    if kind1 == 'C' and kind2 == 'D':
        return cost(coset(w)) + 1
    if kind1 == 'D' and kind2 == 'C':
        return exact_six_distance(second, first)
    w = w.lstrip('aA').rstrip('aA')
    return 0 if not w else cost(w) + 2

def words(radius):
    (all_words, frontier) = ({''}, {''})
    for _ in range(radius):
        frontier = {w + c for w in frontier for c in INVERSE if not w or INVERSE[c] != w[-1]}
        all_words.update(frontier)
    return all_words

def six_group_graph():
    group = words(6)
    graph = {}

    def add_edge(x, y):
        graph.setdefault(x, set()).add(y)
        graph.setdefault(y, set()).add(x)
    for g in group:
        add_edge(('C', g), ('D', coset(g)))
        for b in 'bB':
            h = reduce_word(g + b)
            if h in group:
                add_edge(('C', g), ('C', h))
    edge_count = sum(map(len, graph.values())) // 2
    (todo, seen) = ([next(iter(graph))], set())
    while todo:
        x = todo.pop()
        if x not in seen:
            seen.add(x)
            todo.extend(graph[x] - seen)
    assert len(seen) == len(graph) and edge_count == len(graph) - 1
    assert len(graph['D', '']) == 13
    assert all((len(graph['C', g]) == 3 for g in words(5)))
    small = [('C', w) for w in sorted(words(3))]
    small += [('D', w) for w in sorted({coset(w) for w in words(3)})]
    for first in small:
        (distances, todo) = ({first: 0}, deque([first]))
        while todo:
            x = todo.popleft()
            for y in graph[x]:
                if y not in distances:
                    distances[y] = distances[x] + 1
                    todo.append(y)
        for second in small:
            assert distances[second] == exact_six_distance(first, second)
            COUNTS['six_exact_distance_comparisons'] += 1
    COUNTS['six_C_vertices_in_window'] = len(group)
    COUNTS['six_D_vertices_in_window'] = len(graph) - len(group)
    COUNTS['six_edges_in_window'] = edge_count
    print('six group graph:', len(graph), 'vertices,', edge_count, 'edges; connected, acyclic')

def packet_and_filling():
    for (a, b) in product(range(1, 9), repeat=2):
        outer = (0, a, -b, a - b)
        assert max(outer) - min(outer) == a + b
        COUNTS['weighted_crossing_outer_sectors'] += 1
    assert set((0, 2, -2, 0)) == {-2, 0, 2}
    for length in range(1, 14):
        for word in product((1, -1), repeat=length):
            (heights, level) = ([0], 0)
            for sign in word:
                level += sign
                heights.append(level)
            for initial in (-3, 0, 5):
                (low, high) = (initial + min(heights), initial + max(heights))
                endpoints = (initial, initial + level)
                assert low <= min(endpoints) <= max(endpoints) <= high
            COUNTS['packet_words'] += 1
    values = tuple((Q(i, 3) for i in range(-6, 7)))
    for q in range(1, 5):
        for a in product(values, repeat=q):
            if not all((1 + a[(j + 1) % q] - a[j] > 0 for j in range(q))):
                continue
            m = min((floor(a[j]) for j in range(q)))
            M = max((ceil(1 + a[(j + 1) % q]) - 1 for j in range(q)))
            assert all((m <= x <= M for x in a))
            for c in {Q(m), Q(M), Q(m + M, 2)}:
                for cutoff in (Q(0), Q(1, 3), Q(1, 2), Q(1)):
                    v = tuple((c + cutoff * (x - c) for x in a))
                    for j in range(q):
                        (start, end) = (v[j], 1 + v[(j + 1) % q])
                        assert end > start
                        assert floor(start) >= m
                        assert ceil(end) - 1 <= M
                        COUNTS['whole_open_filling_sectors'] += 1
            COUNTS['coherent_cyclic_arrays'] += 1

def decode(u):
    points = {Q(0), Q(1)}
    for x in u:
        frac = x - floor(x)
        if frac:
            points.add(1 - frac)
    result = Counter()
    points = sorted(points)
    for (low, high) in zip(points, points[1:]):
        theta = (low + high) / 2
        v = tuple((floor(x + theta) for x in u))
        root = v[0]
        result[tuple((x - root for x in v))] += high - low
    return result

def two_zero_region_strips():
    for t in (Q(i, 7) for i in range(-28, 29)):
        result = decode((Q(0), t))
        assert sum(result.values()) == 1
        assert set((v[1] for v in result)) <= {floor(t), ceil(t)}
        assert sum((mass * v[1] for (v, mass) in result.items())) == t
        COUNTS['relative_height_line_points'] += 1
    for direction in (-1, 1):
        for (a, t) in product((Q(i, 7) for i in range(8)), (Q(j, 5) for j in range(-15, 16))):
            u = (Q(0), direction * a, t)
            output = decode(u)
            assert sum(output.values()) == 1
            assert all((v[1] in (0, direction) for v in output))
            assert all((sum((mass * v[i] for (v, mass) in output.items())) == u[i] for i in range(3)))
            for (x, y) in product(output, repeat=2):
                diff = [a - b for (a, b) in zip(x, y)]
                assert max(diff) - min(diff) <= 1
            COUNTS['relative_height_strip_points'] += 1
    tree = words(4)
    edge_number = sum((1 for w in tree if w))
    intervals = 6
    vertices = len(tree) * (intervals + 1)
    edges = len(tree) * intervals + edge_number * (intervals + 1) + edge_number * intervals
    triangles = edge_number * intervals * 2
    assert edge_number == len(tree) - 1
    assert vertices - edges + triangles == 1
    COUNTS['tree_interval_product_vertices'] = vertices
    COUNTS['tree_interval_product_edges'] = edges
    COUNTS['tree_interval_product_triangles'] = triangles

def main():
    link_examples()
    six_group_graph()
    packet_and_filling()
    two_zero_region_strips()
    for (key, value) in sorted(COUNTS.items()):
        print(f'{key}: {value}')
    print('PASS: finite diagnostics only; topology and class minimality require the written proofs.')

if __name__ == '__main__':
    import contextlib
    import io
    import json
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        main()
    print(json.dumps({'scope': 'Finite diagnostics; not a topology certificate.', 'output': captured.getvalue().splitlines()}, indent=2, sort_keys=True))
