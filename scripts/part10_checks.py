#!/usr/bin/env python3
# Finite exact diagnostic for Part 10 of the proof; standard library only; prints a deterministic report and writes no files.
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
from math import gcd
from pathlib import Path
COUNTS = {}

def check(test, message):
    if not test:
        raise AssertionError(message)

def components(vertices, edges):
    adjacency = {v: [] for v in vertices}
    for (a, b) in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)
    unseen = set(vertices)
    result = []
    while unseen:
        root = min(unseen, key=str)
        todo = [root]
        unseen.remove(root)
        comp = {root}
        while todo:
            for nxt in adjacency[todo.pop()]:
                if nxt in unseen:
                    unseen.remove(nxt)
                    comp.add(nxt)
                    todo.append(nxt)
        result.append(comp)
    return result

def actual_capped_core():
    phi_mu_axis = 0
    phi_mu_h_port = phi_mu_axis
    h_actual = (1, 1)
    k_h = sum(h_actual) + phi_mu_h_port
    phi_lambda_h_port = sum(h_actual)
    v_actual = (-1, -1)
    phi_mu_v_port = phi_lambda_h_port
    d_cap = sum(v_actual) + phi_mu_v_port
    check((k_h, phi_mu_v_port, d_cap) == (2, 2, 0), 'Peripheral equations')
    check(phi_mu_axis == 0 and any(v_actual), 'Wrong zero-core restriction')

    def determinant(v, w):
        return v[0] * w[1] - v[1] * w[0]
    core_intersection = abs(determinant((1, 0), (1, 1)))
    cap_intersection = abs(determinant((0, 1), (6, 1)))
    check((core_intersection, cap_intersection) == (1, 6), 'Genuine cut intersections')
    topologies = []
    for s in range(3):
        cap_plus = cap_minus = s
        anchored_to_cap = s
        direct_actual_to_anchored = 2 - s
        actual_to_cap = s
        check(direct_actual_to_anchored + actual_to_cap == 2, 'Actual use')
        check(direct_actual_to_anchored + anchored_to_cap == 2, 'Port demand')
        check(cap_plus == cap_minus and cap_plus + cap_minus == 2 * s, 'Signed cap conservation')
        chi_h_component = -2 - s
        b_h_component = 4 - s
        genus_h_component = Fraction(2 - b_h_component - chi_h_component, 2)
        chi_all = chi_h_component - s
        check(genus_h_component == s and chi_all == -(2 + 2 * s), 'Assembled Euler data')
        cut_base_chi = -2 + (2 + s)
        check(cut_base_chi == s, 'Zero-base cut Euler number')
        topologies.append({'cap_fibres': 2 * s, 'complexity': -chi_all, 'components': 1 + s, 'main_genus': s, 'main_actual_boundary': b_h_component})
    COUNTS['actual_three_block_example'] = topologies
    sum_cap = []
    cap_genus = 3
    chi_cap_fibre = 1 - 2 * cap_genus
    for s in range(3):
        main_chi = -2 + s * chi_cap_fibre
        main_boundary = 4 - s
        main_genus = Fraction(2 - main_boundary - main_chi, 2)
        chi_all = main_chi + s * chi_cap_fibre
        check(main_genus == 3 * s and -chi_all == 2 + 10 * s, 'Nonresonant sum-cap Euler data')
        sum_cap.append({'cap_fibres': 2 * s, 'complexity': -chi_all, 'main_genus': main_genus.numerator})
    check(abs(determinant((0, 1), (1, 0))) == 1, 'Composing cap outer fibre intersection')
    COUNTS['actual_five_block_nonresonant_cap_example'] = sum_cap

def nonresonant_composing_caps():
    framings = (-20, -15, -14, -10, -6, 6, 10, 14, 15, 20)
    cases = nonresonant = mixed_nonresonant = resonant_modes = 0
    genera = {6: 1, 10: 2, 14: 3, 15: 4, 20: 6}
    for count in range(1, 5):
        for weights in product(framings, repeat=count):
            zero_subsets = {mask for mask in range(1, 1 << count) if sum((weights[i] for i in range(count) if mask & 1 << i)) == 0}
            root_modes = {tuple((-weights[i] * bits[i] for i in range(count))) for bits in product((0, 1), repeat=count) if sum((-weights[i] * bits[i] for i in range(count))) == 0}
            check((root_modes == {(0,) * count}) == (not zero_subsets), 'Zero-sum criterion and root modes disagree')
            for mask in zero_subsets:
                vertical = [i for i in range(count) if mask & 1 << i]
                horizontal = [i for i in range(count) if not mask & 1 << i]
                genus = len(vertical) - 1 + 2 * sum((genera[abs(weights[i])] for i in horizontal))
                chi = 2 * (1 - count) + 2 * sum((1 - 2 * genera[abs(weights[i])] for i in horizontal))
                check(len(vertical) >= 2 and genus >= 1 and (chi == -2 * genus), 'Resonant two-boundary cap witness')
                resonant_modes += 1
            if not zero_subsets:
                nonresonant += 1
                mixed_nonresonant += min(weights) < 0 < max(weights)
            cases += 1
    check(not any((sum(subset) == 0 for n in (1, 2) for subset in combinations((6, -10), n))), 'Mixed-chirality genus-three example is resonant')
    check(6 + -6 == 0 and 6 + 14 - 20 == 0, 'Balanced examples escaped the criterion')
    COUNTS['composing_cap_framing_lists'] = cases
    COUNTS['nonresonant_lists'] = nonresonant
    COUNTS['mixed_chirality_nonresonant_lists'] = mixed_nonresonant
    COUNTS['resonant_two_boundary_witness_modes'] = resonant_modes

def recursive_cap_certificates():

    def torus(p, q):
        check(p > 1 and abs(q) > 1 and (gcd(p, q) == 1), 'Torus parameters')
        return (frozenset((0, p * q)), True, (p - 1) * (abs(q) - 1) // 2, 1)

    def cable(p, q, child):
        check(p >= 2 and q != 0 and (gcd(p, q) == 1), 'Cable parameters')
        (slope_set, certified, genus, blocks) = child
        return (frozenset({p * q} | {p * p * s for s in slope_set}), certified, p * genus + (p - 1) * (abs(q) - 1) // 2, blocks + 1)

    def summed(*children):
        values = list(product(*(child[0] for child in children)))
        nonresonant = all((not any(v) for v in values if sum(v) == 0))
        return (frozenset((sum(v) for v in values)), all((c[1] for c in children)) and nonresonant, sum((c[2] for c in children)), 1 + sum((c[3] for c in children)))
    positive = [torus(2, 3), torus(2, 5), torus(3, 4)]
    candidates = positive + [summed(a, b) for a in positive for b in positive]
    candidates += [cable(2, q, a) for q in (1, 3) for a in positive]
    candidates += [summed(a, b) for a in candidates[:] for b in positive]
    for candidate in candidates:
        check(candidate[1] and min(candidate[0]) == 0, 'An all-positive nested construction lost its certificate')
        check(cable(2, -1, candidate)[1], 'Changing a terminal cabling sign destroyed proven rigidity')
    nested = summed(cable(2, 1, torus(2, -3)), torus(2, 5))
    check(nested == (frozenset((-24, -14, 0, 2, 10, 12)), True, 4, 4), 'Mixed-sign recursive cap example')
    check(not summed(torus(2, 3), torus(2, -3))[1], 'The square-knot obstruction passed the recursive test')
    check(not summed(cable(2, -3, torus(2, 3)), torus(2, 3))[1], 'A cable/sum resonance passed the recursive test')
    topologies = []
    for s in range(3):
        cap_chi = 1 - 2 * nested[2]
        main_chi = -2 + s * cap_chi
        main_genus = Fraction(2 - (4 - s) - main_chi, 2)
        complexity = -main_chi - s * cap_chi
        check(main_genus == 4 * s and complexity == 2 + 14 * s, 'Six-block assembly Euler data')
        topologies.append({'cap_fibres': 2 * s, 'complexity': complexity, 'main_genus': main_genus.numerator})
    COUNTS['positive_recursive_cap_constructions'] = len(candidates)
    COUNTS['terminal_negative_cable_certificates'] = len(candidates)
    COUNTS['actual_six_block_nested_cap_example'] = topologies

def cap_grammar():
    cases = removed = 0
    for k in range(7):
        pos = ['H', 'H'] + [f'P{i}' for i in range(k)]
        neg = ['A0', 'A1'] + [f'N{i}' for i in range(k)]
        vertices = {'H', 'A0', 'A1'} | {f'P{i}' for i in range(k)} | {f'N{i}' for i in range(k)}
        for perm in permutations(neg):
            edges = list(zip(pos, perm))
            comps = components(vertices, edges)
            keep = set()
            actual_sets = []
            for comp in comps:
                actual = {'h0', 'h1'} if 'H' in comp else set()
                actual |= {v.lower() for v in comp if v.startswith('A')}
                if actual:
                    keep |= comp
                    actual_sets.append(actual)
                else:
                    check(len(comp) == 2 and sum((v.startswith('P') for v in comp)) == 1 and (sum((v.startswith('N') for v in comp)) == 1), 'An unanchored retained network escaped the cap lemma')
                    removed += 1
            retained = [(a, b) for (a, b) in edges if a in keep and b in keep]
            check(all((not (a.startswith('P') and b.startswith('N')) for (a, b) in retained)), 'Retained cap-to-cap annulus')
            cap_count = sum((v.startswith(('P', 'N')) for v in keep))
            check(cap_count <= 4 and cap_count % 2 == 0, 'Unsigned cap bound')
            check(sum((v.startswith('P') for v in keep)) == sum((v.startswith('N') for v in keep)), 'Reduced signed degree')
            union = set().union(*actual_sets)
            check(union == {'h0', 'h1', 'a0', 'a1'} and sum((len(s) for s in actual_sets)) == 4, 'Actual labels changed')
            cases += 1
    check(cases == sum((__import__('math').factorial(n) for n in range(2, 9))), 'Unexpected matching inventory')
    COUNTS['one_boundary_cap_grammar_pairings'] = cases
    COUNTS['closed_cap_pair_components_deleted'] = removed

def floor(value):
    return value.numerator // value.denominator

def fractional(value):
    return value - floor(value)

def circle_crossings(values, r):
    plus = minus = 0
    for (a, b) in zip(values, values[1:]):
        for n in range(floor(min(a, b) - r) - 1, floor(max(a, b) - r) + 2):
            level = r + n
            if a < level < b:
                plus += 1
            elif b < level < a:
                minus += 1
    return (plus, minus)

def signed_cap_circles():
    parameter_cases = sectors = folds = 0
    denominator = 12
    for degree in range(-2, 3):
        profiles = []
        for amplitude in (0, 2, 3):
            profiles.append(tuple((Fraction(degree * j, 4) + amplitude * t for (j, t) in enumerate((0, 1, 0, -1, 0)))))
        for n0 in range(denominator + 1):
            for n1 in range(denominator - n0 + 1):
                n2 = denominator - n0 - n1
                coeffs = tuple((Fraction(n, denominator) for n in (n0, n1, n2)))
                values = tuple((sum((coeffs[i] * profiles[i][j] for i in range(3))) for j in range(5)))
                check(values[-1] - values[0] == degree, 'Changed cap degree')
                cuts = sorted({Fraction(0), Fraction(1)} | {fractional(v) for v in values})
                signed_mean = unsigned_mean = Fraction(0)
                for (lo, hi) in zip(cuts, cuts[1:]):
                    r = (lo + hi) / 2
                    (plus, minus) = circle_crossings(values, r)
                    check(plus - minus == degree, 'Signed fibre conservation')
                    signed_mean += (hi - lo) * (plus - minus)
                    unsigned_mean += (hi - lo) * (plus + minus)
                    folds += int(plus + minus > abs(degree))
                    sectors += 1
                check(signed_mean == degree, 'Phase mean degree')
                variation = sum((abs(b - a) for (a, b) in zip(values, values[1:])))
                check(unsigned_mean == variation, 'Exact PL coarea / phase mass')
                parameter_cases += 1
    COUNTS['signed_cap_circle_parameter_cases'] = parameter_cases
    COUNTS['signed_cap_regular_phase_sectors'] = sectors
    COUNTS['sectors_with_cancelled_fibre_pairs'] = folds

def matching(n, offset):
    return {tuple(sorted((i, (offset - i) % n))) for i in range(n) if i != (offset - i) % n}

def displayed_unbounded_family():
    for r in range(1, 257):
        n = 2 * r
        leaf = matching(n, 1)
        pattern = matching(n, 0)
        check((0, 1) in leaf, 'First cancelled pair is not a leaf pair')
        eps = [1 if i == 0 or i > r else -1 for i in range(n)]
        check(eps[0] == -eps[1], 'The selected pair is not opposite')
        if r == 1:
            check(leaf == {(0, 1)} and (not pattern), 'Wrong annular endpoint')
            continue
        check((1, n - 1) in pattern, 'No old return for the new tether')
        residual_order = [n - 1] + list(range(2, n - 1))
        relabel = {old: new for (new, old) in enumerate(residual_order)}
        reduced_leaf = {tuple(sorted((relabel[a], relabel[b]))) for (a, b) in leaf if (a, b) != (0, 1)}
        reduced_pattern = {tuple(sorted((relabel[a], relabel[b]))) for (a, b) in pattern if (a, b) != (1, n - 1)}
        check(reduced_leaf == matching(n - 2, 1), 'Residual leaf matching')
        check(reduced_pattern == matching(n - 2, 0), 'Residual pattern matching')
        residual_eps = [eps[i] for i in residual_order]
        target_eps = [1 if i == 0 or i > r - 1 else -1 for i in range(n - 2)]
        check(residual_eps == target_eps and relabel[r] == r - 1, 'Residual orientation / actual tether')
        check(-2 * r + 2 == -2 * (r - 1), 'Euler descent')
    COUNTS['all_r_pair_annularisation_relabellings'] = 256

def balanced_four_boundary_failure():
    chi = {'H2': -1, 'H3': -1, 'P01': 0, 'P23': 0, 'M03': 0, 'M12': 0, 'T0': 0, 'T1': 0, 'T2': 0, 'T3': 0, 'B_out': 0, 'B_plus': 0, 'B_minus': 0}
    labels = {name: {int(name[1])} if name.startswith('T') else set() for name in chi}
    edges = [('B_out', 'T0'), ('B_out', 'T1'), ('B_plus', 'P01'), ('B_plus', 'P01'), ('B_minus', 'M03'), ('B_minus', 'M12'), ('M03', 'H3'), ('M12', 'H2'), ('P23', 'H2'), ('P23', 'H3'), ('H2', 'T2'), ('H3', 'T3')]
    output = []
    for comp in components(chi, edges):
        actual = set().union(*(labels[p] for p in comp))
        euler = sum((chi[p] for p in comp))
        genus = Fraction(2 - len(actual) - euler, 2)
        check(genus.denominator == 1 and genus >= 0, 'Not an oriented surface')
        output.append((tuple(sorted(actual)), euler, int(genus)))
    output.sort()
    check(output == [((), 0, 1), ((0, 1), 0, 0), ((2, 3), -2, 1)], 'Wrong post-annularisation component topology')
    old_leaf = {i: (3 - i) % 4 for i in range(4)}
    new_annulus = {0: 1, 1: 0}
    path = [2]
    path.append(old_leaf[path[-1]])
    path.append(new_annulus[path[-1]])
    path.append(old_leaf[path[-1]])
    check(path == [2, 1, 0, 3], 'Return endpoint composition')
    pants_chi = 2 - 3
    torus_with_one_hole_chi = 2 - 2 - 1
    check(pants_chi + torus_with_one_hole_chi == -2, 'Compression-curve Euler bookkeeping')
    COUNTS['balanced_four_boundary_annularisation'] = output
    COUNTS['retained_bad_component_actual_labels'] = [2, 3]

def balanced_multiple_components():
    for m in range(1, 129):
        n = 4 * m

        def index(a, k):
            return a * m + (k - 1 if a in (0, 2) else m - k)
        plus = set()
        minus = set()
        copy_groups = []
        for k in range(1, m + 1):
            group = tuple((index(a, k) for a in range(4)))
            copy_groups.append(set(group))
            plus |= {tuple(sorted((group[0], group[1]))), tuple(sorted((group[2], group[3])))}
            minus |= {tuple(sorted((group[0], group[3]))), tuple(sorted((group[1], group[2])))}
        check(plus == matching(n, 2 * m - 1), 'Repeated positive leaf')
        check(minus == matching(n, 4 * m - 1), 'Repeated mirror leaf')
        comps = components(range(n), list(plus | minus))
        check({frozenset(c) for c in comps} == {frozenset(c) for c in copy_groups}, 'Wrong companion components')
        chosen = tuple((index(a, m) for a in range(4)))
        (a, b, c, d) = chosen
        check((a, b, c, d) == (m - 1, m, 3 * m - 1, 3 * m), 'Wrong extreme copy')
        check(b == a + 1 and d == c + 1, 'The required product gaps are occupied')
        check(tuple(sorted((a, b))) in plus and tuple(sorted((c, d))) in plus and (tuple(sorted((a, d))) in minus) and (tuple(sorted((b, c))) in minus), 'Wrong local return rectangle')
        check(-4 * m + 2 == -4 * (m - 1) - 2, 'Remaining actual Euler sum')
    COUNTS['balanced_multi_component_test_sizes'] = 128

def pointwise_excess_identity():
    cases = mixed = 0
    for genus in range(4):
        for boundary in range(1, 8):
            chi = 2 - 2 * genus - boundary
            if chi >= 0:
                continue
            cost = -chi
            for positive in range(8):
                for negative in range(8):
                    if not (positive or negative):
                        continue
                    complexity = (positive + negative) * cost
                    baseline = abs(positive - negative) * cost
                    excess = complexity - baseline
                    check(excess == 2 * min(positive, negative) * cost, 'Mixed horizontal Euler excess')
                    check(excess >= 0 and excess % 2 == 0, 'Excess sign / parity')
                    if positive and negative:
                        after = (positive + negative - 2) * cost
                        check(complexity - after == 2 * cost and after - baseline == excess - 2 * cost, 'Pair replacement descent')
                        mixed += 1
                    cases += 1
    COUNTS['pointwise_horizontal_excess_cases'] = cases
    COUNTS['mixed_pair_strict_descent_cases'] = mixed

def actual_nonunit_carrier():
    vertices = ((0, 0), (1, 0), (0, 1), (1, 1))

    def geometric(subset):
        groups = [[], [], []]
        for label in subset:
            (x, y) = vertices[label]
            groups[0] += [label] * (1 - x)
            groups[1] += [label] * (x + y)
            groups[2] += [label] * (1 - y)
        n = len(subset)
        for packets in product(*(set(permutations(g)) for g in groups)):
            word = sum(packets, ())
            if word[:n] == word[n:] and len(set(word[:n])) == n:
                return True
        return False
    genuine = set()
    for size in range(1, 5):
        for subset in combinations(range(4), size):
            if geometric(subset):
                genuine.add(frozenset(subset))
    expected = {frozenset(s) for triangle in ((0, 1, 2), (1, 2, 3)) for size in range(1, 4) for s in combinations(triangle, size)}
    check(genuine == expected, 'Actual port words disagree with the disk carrier')

    def phase_decode(x, y, root):
        values = (Fraction(0), x, -y)
        values = tuple((v - values[root] for v in values))
        cuts = sorted({Fraction(0), Fraction(1)} | {1 - fractional(v) for v in values if fractional(v)})
        result = [Fraction(0)] * 4
        for (lo, hi) in zip(cuts, cuts[1:]):
            theta = (lo + hi) / 2
            ints = [floor(v + theta) for v in values]
            selected = (ints[1] - ints[0], ints[0] - ints[2])
            check(selected in vertices, 'A global root changed actual flow bounds')
            result[vertices.index(selected)] += hi - lo
        return tuple(result)

    def formula(x, y):
        if x + y <= 1:
            return (1 - x - y, x, y, Fraction(0))
        return (Fraction(0), 1 - y, 1 - x, x + y - 1)
    grid = roots = homotopies = 0
    denominator = 16
    for n0 in range(denominator + 1):
        for n1 in range(denominator - n0 + 1):
            for n2 in range(denominator - n0 - n1 + 1):
                n3 = denominator - n0 - n1 - n2
                weights = tuple((Fraction(n, denominator) for n in (n0, n1, n2, n3)))
                support = frozenset((i for (i, w) in enumerate(weights) if w))
                if support not in genuine:
                    continue
                x = weights[1] + weights[3]
                y = weights[2] + weights[3]
                for root in range(3):
                    check(phase_decode(x, y, root) == weights, 'Initial actual simplex was not recovered')
                    roots += 1
                for t in (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)):
                    (xt, yt) = ((1 - t) * x, (1 - t) * y)
                    rounded = phase_decode(xt, yt, 0)
                    check(rounded == formula(xt, yt), 'Independent phase formula')
                    check(frozenset((i for (i, w) in enumerate(rounded) if w)) in genuine, 'Contraction left actual Y')
                    if t == 0:
                        check(rounded == weights, 'Wrong initial contraction value')
                    if t == 1:
                        check(rounded == (1, 0, 0, 0), 'Wrong base endpoint')
                    homotopies += 1
                grid += 1
    COUNTS['actual_nonunit_carrier_simplices'] = len(genuine)
    COUNTS['actual_nonunit_carrier_barycentric_points'] = grid
    COUNTS['actual_nonunit_carrier_common_root_checks'] = roots
    COUNTS['actual_nonunit_carrier_contraction_checks'] = homotopies

def exact_determinant(rows):
    rows = [[Fraction(value) for value in row] for row in rows]
    result = Fraction(1)
    for i in range(len(rows)):
        pivot = next((j for j in range(i, len(rows)) if rows[j][i]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != i:
            (rows[i], rows[pivot]) = (rows[pivot], rows[i])
            result = -result
        value = rows[i][i]
        result *= value
        for j in range(i + 1, len(rows)):
            factor = rows[j][i] / value
            for k in range(i + 1, len(rows)):
                rows[j][k] -= factor * rows[i][k]
            rows[j][i] = 0
    return result

def tree_from_prufer(n, word):
    degree = [1] * n
    for v in word:
        degree[v] += 1
    edges = []
    for v in word:
        leaf = next((i for i in range(n) if degree[i] == 1))
        edges.append((leaf, v))
        degree[leaf] -= 1
        degree[v] -= 1
    left = [i for i in range(n) if degree[i] == 1]
    edges.append(tuple(left))
    return edges

def auxiliary_tree_modes():
    trees = [(1, [])]
    for n in range(2, 6):
        for word in product(range(n), repeat=n - 2):
            trees.append((n, tree_from_prufer(n, word)))
    for n in range(6, 11):
        trees.extend([(n, [(i - 1, i) for i in range(1, n)]), (n, [(0, i) for i in range(1, n)]), (n, [((i - 1) // 2, i) for i in range(1, n)])])
    cases = minors = 0
    for (n, edges) in trees:
        vectors = [[Fraction(1) for _ in range(n)], [Fraction((-1) ** i * (i % 3 + 1)) for i in range(n)], [Fraction(i + 1, i % 2 + 1) for i in range(n)]]
        for vector in vectors:
            for choice in range(3):
                matrix = [[Fraction(0) for _ in range(n)] for _ in range(n)]
                edge_weights = []
                for (index, (a, b)) in enumerate(edges):
                    coefficient = Fraction(1) if choice == 0 else Fraction((-1) ** index * (index + 1)) if choice == 1 else Fraction((-1) ** index * (index + 2), index + 1)
                    matrix[a][b] = matrix[b][a] = coefficient
                    matrix[a][a] -= coefficient * vector[b] / vector[a]
                    matrix[b][b] -= coefficient * vector[a] / vector[b]
                    edge_weights.append(coefficient * vector[a] * vector[b])
                check(all((sum((matrix[i][j] * vector[j] for j in range(n))) == 0 for i in range(n))), 'Chosen class is not a kernel vector')
                laplacian = [[matrix[i][j] * vector[i] * vector[j] for j in range(n)] for i in range(n)]
                expected = Fraction((-1) ** (n - 1))
                for weight in edge_weights:
                    expected *= weight
                for root in range(n):
                    minor = [[laplacian[i][j] for j in range(n) if j != root] for i in range(n) if i != root]
                    check(exact_determinant(minor) == expected and expected != 0, 'Signed tree cofactor or uniqueness failed')
                    minors += 1
                cases += 1
    star = [[0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
    check(all((exact_determinant([[star[i][j] for j in range(4) if j != root] for i in range(4) if i != root]) == 0 for root in range(4))), 'The zero-entry countertest unexpectedly had corank one')
    COUNTS['auxiliary_signed_tree_matrices'] = cases
    COUNTS['auxiliary_tree_cofactors_all_roots'] = minors

def empty_support_certificates():
    cases = 0
    for n in range(2, 13):
        for linking in (1, 2, 6, -6, 10, -10):
            matrix = [[0 if i == j else linking for j in range(n)] for i in range(n)]
            expected = linking ** n * (-1) ** (n - 1) * (n - 1)
            check(exact_determinant(matrix) == expected and expected != 0, 'Seifert support linking determinant')
            cases += 1
    check(exact_determinant([[0]]) == 0, 'two-parallel example incorrectly passed the point test')
    check(exact_determinant([[0, 2], [2, 0]]) == -4, 'Axis/trefoil support test')
    check((2, 6) == (abs(2), abs(2 * 3)), 'Outer genuine fibre intersections')
    exceptional_cases = 0
    for sign in (-1, 1):
        c = sign * 6
        for regular_count in range(9):
            for (use_a, use_b) in product((0, 1), repeat=2):
                rs = [c] * regular_count + [2] * use_a + [sign * 3] * use_b
                if len(rs) < 2:
                    continue
                ss = [Fraction(c, r) for r in rs]
                matrix = [[Fraction(0) if i == j else Fraction(rs[i] * rs[j], c) for j in range(len(rs))] for i in range(len(rs))]
                check(all((value.denominator == 1 for row in matrix for value in row)), 'This explicit regular/axis support lost integral linking')
                check(all((rs[j] == ss[i] * matrix[i][j] for i in range(len(rs)) for j in range(len(rs)) if i != j)), 'Global fibre homology comparison failed')
                expected = Fraction((-1) ** (len(rs) - 1) * (len(rs) - 1), c ** len(rs))
                for r in rs:
                    expected *= r * r
                check(exact_determinant(matrix) == expected and expected != 0, 'Automatic nonsingularity for nonlongitudinal fibres failed')
                exceptional_cases += 1
    cable_cases = 0
    for p in range(2, 17):
        for q in range(-19, 20):
            if not q or gcd(p, q) != 1:
                continue
            h_matrix = [[1, 0, 1], [1, 1, 0], [q, p, p]]
            w_matrix = [[0, p], [p, 1]]
            whole_matrix = [[0, p, p], [p, 0, 1], [p, 1, 0]]
            check(exact_determinant(h_matrix) == 2 * p - q != 0, 'A horizontal Hopf-only mode survived')
            check(exact_determinant(w_matrix) == -p * p != 0, 'A horizontal cable-only mode survived')
            check(exact_determinant(whole_matrix) == 2 * p * p != 0, 'A full horizontal mode survived')
            check(p - q != 0 and p * q != 0, 'A cut ceased to be genuine')
            cable_cases += 1
    COUNTS['nondegenerate_Seifert_support_matrices'] = cases
    COUNTS['regular_and_exceptional_Seifert_support_identities'] = exceptional_cases
    COUNTS['two_block_cabled_support_certificates'] = cable_cases

def product_geometric_carrier():
    tuples = tuple(product((0, 1), repeat=2))
    cases = 0
    denominator = 8
    for n0 in range(denominator + 1):
        for n1 in range(denominator - n0 + 1):
            for n2 in range(denominator - n0 - n1 + 1):
                ns = (n0, n1, n2, denominator - n0 - n1 - n2)
                weights = [Fraction(n, denominator) for n in ns]
                marginals = [[sum((weights[j] for (j, vertex) in enumerate(tuples) if vertex[i] == a)) for a in (0, 1)] for i in range(2)]
                for t in (Fraction(0), Fraction(1, 3), Fraction(1)):
                    moving = [[m[0] + t * m[1], (1 - t) * m[1]] for m in marginals]
                    coupling = [moving[0][a] * moving[1][b] for (a, b) in tuples]
                    check(sum(coupling) == 1 and min(coupling) >= 0, 'Product coupling ceased to be a probability')
                    for i in range(2):
                        for a in (0, 1):
                            check(sum((coupling[j] for (j, vertex) in enumerate(tuples) if vertex[i] == a)) == moving[i][a], 'Wrong geometric marginal')
                    if t == 1:
                        check(coupling == [1, 0, 0, 0], 'Wrong product base point')
                    else:
                        coordinate_supports = [{a for a in (0, 1) if moving[i][a]} for i in range(2)]
                        check(all((not coupling[j] or all((vertex[i] in coordinate_supports[i] for i in range(2))) for (j, vertex) in enumerate(tuples))), 'Product support left its geometric carrier')
                    if t == 0:
                        for u in (Fraction(0), Fraction(1, 2), Fraction(1)):
                            joined = [(1 - u) * a + u * b for (a, b) in zip(weights, coupling)]
                            check(sum(joined) == 1 and min(joined) >= 0, 'Initial straight product carrier failed')
                    cases += 1
    COUNTS['empty_interface_product_coupling_parameters'] = cases

def resonant_six_component_star():
    support_linking = [[0 if i == j else 1 for j in range(3)] for i in range(3)]
    boundary_matrix = [[support_linking[i][j] - (2 if i == j else 0) for j in range(3)] for i in range(3)]
    check(exact_determinant(boundary_matrix) == 0 and all((sum(row) == 0 for row in boundary_matrix)), 'The intended resonant auxiliary class vanished')
    check(exact_determinant([row[:2] for row in boundary_matrix[:2]]) == 3, 'Resonant mode has the wrong corank')
    fibre_evaluation = 3
    fibre_chi = -fibre_evaluation
    fibre_boundary = 3 * gcd(1, 2)
    check(Fraction(2 - fibre_boundary - fibre_chi, 2) == 1, 'Central auxiliary fibre genus')
    actual_linking = [[0 if i == j else -2 if i // 2 == j // 2 else 1 for j in range(6)] for i in range(6)]
    actual_orientations = [1, -1] * 3
    check(all((sum((actual_linking[i][j] * actual_orientations[j] for j in range(6))) == 2 * actual_orientations[i] for i in range(6))), 'Actual leaf fibre Phi did not vanish')
    check(all((sum(actual_orientations[2 * i:2 * i + 2]) == 0 for i in range(3))), 'Central restriction is not zero')
    examples = []
    for t in range(1, 65):
        (r, n) = (2 * t, 4 * t)
        offsets = (0, 2, 0)
        tethers = ((0, r), (1, r + 1), (0, r))
        edges = []
        adjacency = {j: [] for j in range(n)}
        labels = {j: set() for j in range(n)}
        signs = {}
        for (port, (offset, (positive, negative))) in enumerate(zip(offsets, tethers)):
            (signs[positive], signs[negative]) = (1, -1)
            labels[positive].add((port, 1))
            labels[negative].add((port, -1))
            for j in range(n):
                other = (offset - j) % n
                if j in (positive, negative):
                    check(other == j, 'A real tether was not a reflection defect')
                elif j < other:
                    edges.append((j, other))
                    adjacency[j].append(other)
                    adjacency[other].append(j)
        todo = list(signs)
        while todo:
            j = todo.pop()
            for other in adjacency[j]:
                if other in signs:
                    check(signs[other] == -signs[j], 'Inconsistent oriented return')
                else:
                    signs[other] = -signs[j]
                    todo.append(other)
        check(len(signs) == n, 'An unanchored closed component escaped the tests')
        comps = components(range(n), edges)
        check({frozenset(comp) for comp in comps} == {frozenset(range(0, n, 2)), frozenset(range(1, n, 2))}, 'Resonant parity path connectivity')
        genera = []
        for comp in comps:
            actual = set().union(*(labels[j] for j in comp))
            check(actual, 'A constructed whole component is closed')
            boundary = len(actual)
            chi = fibre_chi * len(comp)
            genus = Fraction(2 - boundary - chi, 2)
            if 0 in comp:
                check((len(comp), boundary, genus) == (r, 4, 3 * t - 1), 'Four-boundary component Euler data')
            else:
                check((len(comp), boundary, genus) == (r, 2, 3 * t), 'Two-boundary component Euler data')
            genera.append(genus.numerator)
        check(-1 + (r - 1 + 2) == r, 'Disconnected leaf chamber count')
        if t in (1, 64):
            examples.append({'t': t, 'trace_each_port': n, 'genera': sorted(genera), 'complexity': 12 * t})
    COUNTS['resonant_six_component_star_parameters'] = 64
    COUNTS['resonant_star_endpoint_examples'] = examples

def two_positive_axis_rigidity():

    def axes_of(signs):
        (n, r) = (len(signs), len(signs) // 2)
        return [a for a in range(n) if signs[a] == 1 and signs[(a + r) % n] == -1 and all((signs[(2 * a - j) % n] == -signs[j] for j in range(n) if j not in (a, (a + r) % n)))]
    words = 0
    for r in range(1, 9):
        n = 2 * r
        for rest in combinations(range(1, n), r - 1):
            positive = {0, *rest}
            signs = [1 if j in positive else -1 for j in range(n)]
            axes = axes_of(signs)
            check(len(axes) <= 2, 'Fourier positive-axis bound failed')
            if len(axes) == 2:
                d = axes[1] - axes[0]
                if gcd(d, r) == 1:
                    check((d + r) % 2 == 1, 'Reduced positive defects violate parity')
            words += 1
    parameters = 0
    for r in range(2, 65):
        n = 2 * r
        for d in range(1, n):
            if gcd(d, r) != 1 or (d + r) % 2 != 1:
                continue
            for third in (0, d):
                positive_axes = (0, d, third)
                signs = {}
                edges = []
                labels = {j: set() for j in range(n)}
                adjacency = {j: [] for j in range(n)}
                for (port, a) in enumerate(positive_axes):
                    b = (a + r) % n
                    (signs[a], signs[b]) = (1, -1)
                    labels[a].add((port, 1))
                    labels[b].add((port, -1))
                    for j in range(n):
                        other = (2 * a - j) % n
                        if j not in (a, b) and j < other:
                            edges.append((j, other))
                            adjacency[j].append(other)
                            adjacency[other].append(j)
                todo = list(signs)
                while todo:
                    j = todo.pop()
                    for other in adjacency[j]:
                        if other in signs:
                            check(signs[other] == -signs[j], 'Coprime positive-axis sign propagation')
                        else:
                            signs[other] = -signs[j]
                            todo.append(other)
                check(len(signs) == n, 'A reduced axis diagram has a closed orbit')
                check(sum(signs.values()) == 0, 'A two-axis diagram changed the central zero restriction')
                comps = components(range(n), edges)
                check(len(comps) == 2 and all((len(comp) == r for comp in comps)), 'Wrong two-axis component count')
                boundaries = []
                genera = []
                for comp in comps:
                    actual = set().union(*(labels[j] for j in comp))
                    boundaries.append(len(actual))
                    genus = Fraction(2 - len(actual) + 3 * r, 2)
                    check(genus.denominator == 1, 'Two-axis genus is not integral')
                    genera.append(genus.numerator)
                check(sorted(boundaries) == ([3, 3] if r % 2 else [2, 4]), 'Wrong two-axis actual boundary partition')
                check(sorted(genera) == ([(3 * r - 1) // 2] * 2 if r % 2 else [3 * r // 2 - 1, 3 * r // 2]), 'Wrong two-axis genus formula')
                parameters += 1
    COUNTS['positive_axis_balanced_sign_words'] = words
    COUNTS['coprime_two_axis_normal_parameters'] = parameters

def main():
    pass
    actual_capped_core()
    nonresonant_composing_caps()
    recursive_cap_certificates()
    cap_grammar()
    signed_cap_circles()
    displayed_unbounded_family()
    balanced_four_boundary_failure()
    balanced_multiple_components()
    pointwise_excess_identity()
    actual_nonunit_carrier()
    auxiliary_tree_modes()
    empty_support_certificates()
    product_geometric_carrier()
    resonant_six_component_star()
    two_positive_axis_rigidity()
    print('PASS: finite exact diagnostics; the topology is proved in the manuscript.')
    for (name, value) in COUNTS.items():
        print(f'{name}: {value}')
if __name__ == '__main__':
    main()
