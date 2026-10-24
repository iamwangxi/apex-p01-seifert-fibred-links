#!/usr/bin/env python3
# Finite exact diagnostic for Part 10 of the proof; standard library only; prints a deterministic report and writes no files.
from collections import Counter, deque
from fractions import Fraction as Q
from itertools import combinations, product
from math import gcd
COUNTS = Counter()

def require(value, label):
    if not value:
        raise AssertionError(label)

def rref(matrix):
    rows = [list(map(Q, row)) for row in matrix]
    columns = len(rows[0]) if rows else 0
    pivots = []
    r = 0
    for c in range(columns):
        p = next((i for i in range(r, len(rows)) if rows[i][c]), None)
        if p is None:
            continue
        (rows[r], rows[p]) = (rows[p], rows[r])
        leading = rows[r][c]
        rows[r] = [x / leading for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                a = rows[i][c]
                rows[i] = [x - a * y for (x, y) in zip(rows[i], rows[r])]
        pivots.append(c)
        r += 1
        if r == len(rows):
            break
    return (rows, pivots)

def nullspace(matrix):
    (rows, pivots) = rref(matrix)
    basis = []
    for free in range(len(matrix[0])):
        if free in pivots:
            continue
        v = [Q(0)] * len(matrix[0])
        v[free] = Q(1)
        for (i, p) in enumerate(pivots):
            v[p] = -rows[i][free]
        basis.append(v)
    return basis

def determinant(matrix):
    rows = [list(map(Q, row)) for row in matrix]
    value = Q(1)
    for c in range(len(rows)):
        p = next((i for i in range(c, len(rows)) if rows[i][c]), None)
        if p is None:
            return Q(0)
        if p != c:
            (rows[c], rows[p]) = (rows[p], rows[c])
            value = -value
        leading = rows[c][c]
        value *= leading
        for i in range(c + 1, len(rows)):
            a = rows[i][c] / leading
            rows[i] = [x - a * y for (x, y) in zip(rows[i], rows[c])]
    return value

def slope(covector):
    (a, b) = covector
    return -Q(b, a) if a else None

def peripheral_slices():
    for p in range(2, 10):
        for (a, b) in product(range(-7, 8), repeat=2):
            if not (a or b):
                continue
            outer = (a, p * b)
            inner = (p * a, b)
            if a:
                require(slope(outer) == p * p * slope(inner), 'Cable scaling')
                COUNTS['cable_finite_covectors'] += 1
            else:
                require(slope(outer) is None and slope(inner) is None, 'Meridional traces must stay excluded')
                COUNTS['cable_meridional_negative_controls'] += 1
            if not b and gcd(abs(a), abs(b)) == 1:
                require(gcd(abs(outer[0]), abs(outer[1])) == 1, 'One cable outer longitude')
                require(gcd(abs(inner[0]), abs(inner[1])) == p, 'Exactly p companion longitudes')
    for count in range(2, 5):
        for b in range(1, 5):
            for a in product(range(-3, 4), repeat=count):
                outer = slope((b, sum(a)))
                children = [slope((b, x)) for x in a]
                require(outer == sum(children), 'Composing sum of slopes')
                COUNTS['composing_finite_covectors'] += 1

class Assembly:

    def __init__(self):
        self.pieces = {}
        self.edges = []

    def add(self, name, chi, boundary, actual=()):
        require(name not in self.pieces, 'Distinct piece names')
        self.pieces[name] = (chi, boundary, frozenset(actual))

    def join(self, a, b):
        require(a in self.pieces and b in self.pieces, 'Valid gluing endpoints')
        self.edges.append((a, b))

    def components(self):
        adjacency = {v: [] for v in self.pieces}
        for (a, b) in self.edges:
            adjacency[a].append(b)
            adjacency[b].append(a)
        unseen = set(self.pieces)
        result = []
        while unseen:
            root = next(iter(unseen))
            (todo, component) = ([root], set())
            unseen.remove(root)
            while todo:
                v = todo.pop()
                component.add(v)
                for w in adjacency[v]:
                    if w in unseen:
                        unseen.remove(w)
                        todo.append(w)
            chi = sum((self.pieces[v][0] for v in component))
            boundary = sum((self.pieces[v][1] for v in component))
            boundary -= 2 * sum((a in component for (a, b) in self.edges))
            actual = frozenset().union(*(self.pieces[v][2] for v in component))
            require(boundary == len(actual), 'All unglued boundaries are actual')
            genus = Q(2 - boundary - chi, 2)
            require(genus.denominator == 1 and genus >= 0, 'Orientable component Euler data')
            result.append((component, chi, boundary, int(genus), actual))
        return result

def composing_cap_witnesses():
    knots = ((2, 3), (2, -3), (2, 5), (2, -5), (3, 4), (3, -4))
    for count in range(1, 6):
        for choices in product(knots, repeat=count):
            framings = tuple((p * q for (p, q) in choices))
            genera = tuple(((p - 1) * (abs(q) - 1) // 2 for (p, q) in choices))
            resonances = [mask for mask in range(1, 1 << count) if sum((framings[i] for i in range(count) if mask >> i & 1)) == 0]
            for b in (1, 2, 3):
                for mask in range(1 << count):
                    values = [-b * framings[i] if mask >> i & 1 else 0 for i in range(count)]
                    if sum(values):
                        continue
                    divisor = gcd(b, *map(abs, values))
                    require(divisor == b, 'Primitive composing class forces b=1')
                    require(mask == 0 or mask in resonances, 'Subset criterion')
            COUNTS['composing_cap_framing_lists'] += 1
            for mask in resonances:
                a = Assembly()
                a.add('section+', 1 - count, count + 1, ('outer+',))
                a.add('section-', 1 - count, count + 1, ('outer-',))
                for (i, g) in enumerate(genera):
                    if mask >> i & 1:
                        a.add((i, 'annulus'), 0, 2)
                        a.join('section+', (i, 'annulus'))
                        a.join('section-', (i, 'annulus'))
                    else:
                        for sign in ('+', '-'):
                            a.add((i, sign), 1 - 2 * g, 1)
                            a.join('section' + sign, (i, sign))
                components = a.components()
                require(len(components) == 1, 'Zero-sum witness is connected')
                (_, chi, boundaries, genus, _) = components[0]
                expected = bin(mask).count('1') - 1 + 2 * sum((g for (i, g) in enumerate(genera) if not mask >> i & 1))
                require(boundaries == 2 and genus == expected and (genus >= 1), 'Zero-sum witness genus and boundary count')
                require(chi == -2 * genus, 'Two-boundary witness Euler sum')
                COUNTS['connected_two_boundary_witnesses'] += 1

def tree_matrices():
    trees = {1: [()], 2: [((0, 1),)], 3: [((0, 1), (1, 2)), ((0, 1), (0, 2))], 4: [((0, 1), (1, 2), (2, 3)), ((0, 1), (0, 2), (0, 3))]}
    for (n, shapes) in trees.items():
        for edges in shapes:
            for weights in product((-2, -1, 1, 2), repeat=len(edges)):
                if n == 4 and any((abs(w) != 1 for w in weights)):
                    continue
                for diagonal in product(range(-2, 3), repeat=n):
                    matrix = [[Q(0)] * n for _ in range(n)]
                    for (i, d) in enumerate(diagonal):
                        matrix[i][i] = Q(d)
                    for ((a, b), w) in zip(edges, weights):
                        matrix[a][b] = matrix[b][a] = Q(w)
                    kernel = nullspace(matrix)
                    has_nowhere_zero = bool(kernel) and all((any((v[i] for v in kernel)) for i in range(n)))
                    if has_nowhere_zero:
                        require(len(kernel) == 1, 'Tree nullity must be one')
                        k = kernel[0]
                        lap = [[matrix[i][j] * k[i] * k[j] for j in range(n)] for i in range(n)]
                        require(all((sum(row) == 0 for row in lap)), 'Zero row sums')
                        predicted = Q((-1) ** (n - 1))
                        for (a, b) in edges:
                            predicted *= matrix[a][b] * k[a] * k[b]
                        for root in range(n):
                            minor = [[lap[i][j] for j in range(n) if j != root] for i in range(n) if i != root]
                            require(determinant(minor) == predicted != 0, 'Every signed tree cofactor')
                            COUNTS['arbitrary_tree_cofactors'] += 1
                        COUNTS['arbitrary_trees_with_horizontal_line'] += 1
                    COUNTS['arbitrary_integer_tree_matrices'] += 1
    star = [[0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
    kernel = nullspace(star)
    require(len(kernel) == 2 and all((v[0] == 0 for v in kernel)), 'Higher nullity is excluded only with the nowhere-zero condition')

def port_word_simplex(vertices, degree):
    m = len(vertices)
    sizes = [sum(map(sum, vertices))]
    sizes += [sum((v[i] == 0 for v in vertices)) for i in range(degree)]
    observed = [[0] * (degree + 1) for _ in range(m)]
    start = 0
    for (group, size) in enumerate(sizes):
        for position in range(start, start + size):
            observed[position % m][group] += 1
        start += size
    require(start == degree * m, 'One label per fibre, degree repeats')
    wanted = Counter(((sum(v),) + tuple((1 - x for x in v)) for v in vertices))
    return wanted == Counter(map(tuple, observed))

def threshold_distribution(mean, root):
    values = [Q(0)]
    for value in mean:
        values.append(values[-1] + value)
    values = [x - values[root] for x in values]
    cuts = sorted({Q(0), Q(1)} | {-x % 1 for x in values})
    output = Counter()
    for (lo, hi) in zip(cuts, cuts[1:]):
        phase = (lo + hi) / 2
        floors = [(value + phase).__floor__() for value in values]
        selected = tuple((floors[i + 1] - floors[i] for i in range(len(mean))))
        require(set(selected) <= {0, 1}, 'Actual endpoint capacity')
        output[selected] += hi - lo
    return output

def nonunit_carriers():
    for n in range(2, 5):
        vertices = [tuple((v >> i & 1 for i in range(n))) for v in range(1 << n)]
        accepted = 0
        for size in range(1, len(vertices) + 1):
            for simplex in combinations(vertices, size):
                COUNTS['nonunit_candidate_subsets'] += 1
                if not port_word_simplex(simplex, n):
                    continue
                accepted += 1
                weight_options = [tuple((Q(1, size) for _ in simplex)), tuple((Q(i + 1, size * (size + 1) // 2) for i in range(size))), tuple((Q(size - i, size * (size + 1) // 2) for i in range(size)))]
                for weights in weight_options:
                    mean = tuple((sum((w * v[i] for (w, v) in zip(weights, simplex))) for i in range(n)))
                    desired = Counter(dict(zip(simplex, weights)))
                    for root in range(n + 1):
                        require(threshold_distribution(mean, root) == desired, 'True geometric simplex start/root recovery')
                        COUNTS['nonunit_start_and_root_checks'] += 1
                    for time in (Q(0), Q(1, 5), Q(1, 2), Q(4, 5), Q(1)):
                        point = tuple(((1 - time) * x for x in mean))
                        out = threshold_distribution(point, 0)
                        require(port_word_simplex(tuple(out), n), 'The whole output support is geometric')
                        require(sum(out.values()) == 1, 'Phase measure one')
                        if time == 1:
                            require(out == Counter({(0,) * n: Q(1)}), 'Common base vertex endpoint')
                        COUNTS['nonunit_contraction_checks'] += 1
        COUNTS[f'degree_{n}_genuine_simplices'] = accepted
    require(not port_word_simplex(((0, 0), (1, 1)), 2), 'Common arc support alone must not imply a geometric edge')

def four_boundary_assembly(m, cancel):
    a = Assembly()
    n = 4 * m

    def index(part, copy):
        return part * m + (copy if part % 2 == 0 else m - 1 - copy)
    selected = (m - 1, m)
    replacement = {}
    for j in range(n):
        a.add(('actual', j), 0, 2, (j,))
        if not cancel or j not in selected:
            a.add(('pants', j), -1, 3)
            a.join(('actual', j), ('pants', j))
    if cancel:
        for kind in ('outer', 'positive', 'negative'):
            a.add(('new', kind), 0, 2)
        for j in selected:
            a.join(('actual', j), ('new', 'outer'))
            replacement[j, 'positive'] = ('new', 'positive')
            replacement[j, 'negative'] = ('new', 'negative')
    for copy in range(m):
        j = [index(part, copy) for part in range(4)]
        for (kind, pairs) in (('positive', ((j[0], j[1]), (j[2], j[3]))), ('negative', ((j[0], j[3]), (j[1], j[2])))):
            for pair in pairs:
                node = (kind, copy, pair)
                a.add(node, 0, 2)
                for endpoint in pair:
                    target = replacement.get((endpoint, kind), ('pants', endpoint))
                    a.join(node, target)
    return a.components()

def cancellation_examples():
    for m in range(1, 97):
        before = four_boundary_assembly(m, False)
        after = four_boundary_assembly(m, True)
        require(len(before) == m and all(((b, g, chi) == (4, 1, -4) for (_, chi, b, g, _) in before)), 'Parallel four-boundary components')
        types = Counter(((chi, b, g) for (_, chi, b, g, _) in after))
        expected = Counter({(0, 0, 1): 1, (0, 2, 0): 1, (-2, 2, 1): 1})
        if m > 1:
            expected[-4, 4, 1] = m - 1
        require(types == expected, 'Closed torus + actual annulus + bad genus-one component')
        COUNTS['annularisation_and_multicomponent_assemblies'] += 1

def support_matrices():
    for n in range(2, 11):
        for linking in (-10, -6, -1, 1, 6, 10):
            matrix = [[0 if i == j else linking for j in range(n)] for i in range(n)]
            require(determinant(matrix) == linking ** n * (-1) ** (n - 1) * (n - 1), 'Seifert regular fibre support determinant')
            COUNTS['regular_fibre_support_determinants'] += 1
    for p in range(2, 15):
        for q in range(-30, 31):
            if not q or gcd(p, q) != 1:
                continue
            h_only = [[1, 0, 1], [1, 1, 0], [q, p, p]]
            w_only = [[0, p], [p, 1]]
            whole = [[0, p, p], [p, 0, 1], [p, 1, 0]]
            require(determinant(h_only) == 2 * p - q != 0, 'H-only exclusion')
            require(determinant(w_only) == -p * p != 0, 'W-only exclusion')
            require(determinant(whole) == 2 * p * p != 0, 'Whole-support exclusion')
            require(p != q, 'Genuine support interface')
            COUNTS['cabled_hopf_three_subtree_certificates'] += 1
    require(determinant([[1, 0, 1], [1, 1, 0], [4, 2, 2]]) == 0, 'Noncoprime q=2p must fail H-only exclusion')
    resonance = [[-2, 1, 1], [1, -2, 1], [1, 1, -2]]
    basis = nullspace(resonance)
    require(basis == [[Q(1), Q(1), Q(1)]], 'Resonant central line')

def resonant_star():
    for t in range(1, 193):
        (r, n) = (2 * t, 4 * t)
        a = Assembly()
        adjacency = {j: [] for j in range(n)}
        actual_sign = {}
        for j in range(n):
            a.add(('R', j), -3, 3)
        for (port, axis) in enumerate((0, 1, 0)):
            for (j, sign) in ((axis, 1), (axis + r, -1)):
                actual = (port, sign)
                node = ('tether', port, j)
                a.add(node, 0, 2, (actual,))
                a.join(node, ('R', j))
                require(j not in actual_sign or actual_sign[j] == sign, 'Actual sign consistency')
                actual_sign[j] = sign
            pairs = []
            for j in range(n):
                other = (2 * axis - j) % n
                if j == other or j > other:
                    continue
                pairs.append((j, other))
                node = ('return', port, j)
                a.add(node, 0, 2)
                a.join(node, ('R', j))
                a.join(node, ('R', other))
                adjacency[j].append(other)
                adjacency[other].append(j)
            require(len(pairs) == r - 1, 'Return count')
            for ((x, y), (z, w)) in combinations(pairs, 2):
                require(not (x < z < y < w or z < x < w < y), 'A pants return pairing must be noncrossing')
        signs = dict(actual_sign)
        todo = deque(signs)
        while todo:
            j = todo.popleft()
            for other in adjacency[j]:
                if other in signs:
                    require(signs[other] == -signs[j], 'Oriented return gluing')
                else:
                    signs[other] = -signs[j]
                    todo.append(other)
        require(len(signs) == n and sum(signs.values()) == 0, 'Balanced central zero class')
        components = a.components()
        require(len(components) == 2, 'Exactly two spanning components')
        require(sorted(((b, g) for (_, _, b, g, _) in components)) == [(2, 3 * t), (4, 3 * t - 1)], 'Resonant star genera and boundaries')
        require(sum((-chi for (_, chi, _, _, _) in components)) == 12 * t, 'Unbounded distinct complexities')
        COUNTS['resonant_star_orientable_assemblies'] += 1

def descent_and_products():
    for g in range(6):
        for boundary in range(1, 10):
            chi = 2 - 2 * g - boundary
            if chi >= 0:
                continue
            for (positive, negative) in product(range(10), repeat=2):
                if not (positive or negative):
                    continue
                full = -(positive + negative) * chi
                baseline = -abs(positive - negative) * chi
                require(full - baseline == -2 * min(positive, negative) * chi, 'Even nonnegative excess')
                if positive and negative:
                    require(full + 2 * chi <= full - 2, 'Strict annular descent')
                COUNTS['horizontal_excess_identities'] += 1
    for numerator in range(14):
        weights = [Q(numerator, 13), 1 - Q(numerator, 13)]
        inputs = ((0, 0), (1, 2))
        marginal0 = [weights[0], weights[1]]
        marginal1 = [weights[0], Q(0), weights[1]]
        output = {(i, j): marginal0[i] * marginal1[j] for i in range(2) for j in range(3)}
        require(sum(output.values()) == 1, 'Product probability total')
        for i in range(2):
            require(sum((output[i, j] for j in range(3))) == marginal0[i], 'First product marginal')
        for j in range(3):
            require(sum((output[i, j] for i in range(2))) == marginal1[j], 'Second product marginal')
        for time in (Q(0), Q(1, 3), Q(1)):
            joint = {v: time * output[v] for v in output}
            for (v, weight) in zip(inputs, weights):
                joint[v] += (1 - time) * weight
            require(sum(joint.values()) == 1, 'Initial carrier segment')
            COUNTS['product_probability_segments'] += 1

def main():
    peripheral_slices()
    composing_cap_witnesses()
    tree_matrices()
    nonunit_carriers()
    cancellation_examples()
    support_matrices()
    resonant_star()
    descent_and_products()
    print('PASS: independent exact finite diagnostics; topology is assessed in the report.')
    for (name, count) in sorted(COUNTS.items()):
        print(f'{name}: {count}')
if __name__ == '__main__':
    main()
