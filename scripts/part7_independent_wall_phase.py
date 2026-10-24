#!/usr/bin/env python3
# Finite exact diagnostic for Part 7 of the proof; standard library only; prints a deterministic report and writes no files.
from collections import deque
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import permutations, product
from math import comb

@dataclass(frozen=True)
class Wall:
    name: str
    tail: str
    head: str
    actual: tuple
    minus_chi: int
    packet: str

@dataclass(frozen=True)
class Support:
    chambers: tuple
    walls: tuple
    tori: tuple
    meridians: tuple

def check(condition, message):
    if not condition:
        raise AssertionError(message)

def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for first in range(n + 1):
            for tail in compositions(n - first, k - 1):
                yield ((first,) + tail)

def actual_counts(support, vertex):
    return tuple((sum((t in w.actual for w in support.walls if w.name in vertex)) for t in support.tori))

def check_support(support, vertices):
    walls = {w.name: w for w in support.walls}
    for w in support.walls:
        check(w.actual, 'A selected wall must have actual boundary')
        check(len(set(w.actual)) == len(w.actual), 'Repeated actual torus')
    for vertex in vertices:
        check(actual_counts(support, vertex) == (1,) * len(support.tori), 'An input is not a reduced spanning surface')
    for (torus, cycle) in zip(support.tori, support.meridians):
        check(all((torus in walls[e].actual for e in cycle)), 'Wrong meridian')
        check(set(cycle) == {w.name for w in support.walls if torus in w.actual}, 'Meridian misses a torus wall')
        check(all((walls[a].head == walls[b].tail for (a, b) in zip(cycle, cycle[1:] + cycle[:1]))), 'A positive meridian is not a closed directed path')
        for vertex in vertices:
            check(sum((e in vertex for e in cycle)) == 1, 'An input has torus degree different from one')

def potential(support, vertex, reference, root=None):
    root = root or support.chambers[0]
    adj = {c: [] for c in support.chambers}
    for w in support.walls:
        d = int(w.name in vertex) - int(w.name in reference)
        adj[w.tail].append((w.head, d))
        adj[w.head].append((w.tail, -d))
    values = {root: 0}
    queue = deque([root])
    while queue:
        c = queue.popleft()
        for (nxt, d) in adj[c]:
            if nxt in values:
                check(values[nxt] == values[c] + d, 'Difference cochain has a nonzero period')
            else:
                values[nxt] = values[c] + d
                queue.append(nxt)
    check(len(values) == len(support.chambers), 'Disconnected chamber graph')
    return values

def width(support, a, b):
    u = potential(support, a, b)
    return max(u.values()) - min(u.values())

def fractional(x):
    return x - x.numerator // x.denominator

def phase_average(support, vertices, weights, root=None, illegal_shift=None):
    check(sum(weights) == 1 and min(weights) >= 0, 'Bad barycentric weights')
    us = [potential(support, v, vertices[0], root) for v in vertices]
    chamber = {c: sum((lam * u[c] for (lam, u) in zip(weights, us))) for c in support.chambers}
    bands = []
    cuts = {Q(0), Q(1)}
    for w in support.walls:
        jump = sum((lam for (lam, v) in zip(weights, vertices) if w.name in v))
        check(0 <= jump <= 1, 'A packet jump is outside [0,1]')
        start = chamber[w.tail]
        if illegal_shift:
            start += illegal_shift.get(w.name, Q(0))
        bands.append((w, start, jump))
        cuts.update((fractional(start), fractional(start + jump)))
    result = {}
    cuts = sorted(cuts)
    for (lo, hi) in zip(cuts, cuts[1:]):
        if lo == hi:
            continue
        r = (lo + hi) / 2
        selected = set()
        for (w, start, jump) in bands:
            n = (start - r).numerator // (start - r).denominator + 1
            if start < r + n < start + jump:
                selected.add(w.name)
        selected = frozenset(selected)
        result[selected] = result.get(selected, Q(0)) + hi - lo
    return result

def packet_projection(support, distribution):
    packets = {w.name: w.packet for w in support.walls}
    result = {}
    for (vertex, weight) in distribution.items():
        image = frozenset((packets[e] for e in vertex))
        check(len(image) == len(vertex), 'One level selected two parallel copies')
        result[image] = result.get(image, Q(0)) + weight
    return result

def split_packets(support, vertices, orders):
    chambers = list(support.chambers)
    walls = []
    expanded = [set() for _ in vertices]
    replacements = {}
    for w in support.walls:
        uses = orders[w.name]
        check(set(uses) == {i for (i, v) in enumerate(vertices) if w.name in v}, 'Packet order changed its input membership')
        ends = [w.tail]
        for j in range(len(uses) - 1):
            c = 'inside:' + w.name + ':' + str(j)
            chambers.append(c)
            ends.append(c)
        ends.append(w.head)
        replacements[w.name] = []
        for (j, i) in enumerate(uses):
            name = w.name + '@' + str(i)
            walls.append(Wall(name, ends[j], ends[j + 1], w.actual, w.minus_chi, w.packet))
            expanded[i].add(name)
            replacements[w.name].append(name)
    meridians = tuple((tuple((n for e in cycle for n in replacements[e])) for cycle in support.meridians))
    return (Support(tuple(chambers), tuple(walls), support.tori, meridians), tuple((frozenset(v) for v in expanded)))

def validate_distribution(support, distribution):
    check(sum(distribution.values()) == 1, 'Lost phase length')
    for vertex in distribution:
        check(actual_counts(support, vertex) == (1,) * len(support.tori), 'A generic layer has wrong actual boundary')
    out = tuple(distribution)
    for (a, b) in product(out, repeat=2):
        check(width(support, a, b) <= 1, 'Output layers have width over one')

def two_bridge_parallel():
    support = Support(('O', 'P', 'N'), (Wall('p0', 'O', 'P', ('+',), 1, 'p0'), Wall('p1', 'P', 'O', ('+',), 1, 'p1'), Wall('n0', 'O', 'N', ('-',), 1, 'n0'), Wall('n1', 'N', 'O', ('-',), 1, 'n1')), ('+', '-'), (('p0', 'p1'), ('n0', 'n1')))
    vertices = tuple((frozenset(('p' + str(a), 'n' + str(b))) for (a, b) in ((0, 0), (1, 0), (0, 1), (1, 1))))
    check_support(support, vertices)
    check(width(support, vertices[1], vertices[2]) == 2, 'Lost distance-two pair')
    check(width(support, vertices[0], vertices[3]) == 1, 'Wrong true diagonal')
    mid = phase_average(support, vertices, (Q(0), Q(1, 2), Q(1, 2), Q(0)))
    check(mid == {vertices[0]: Q(1, 2), vertices[3]: Q(1, 2)}, 'The geometric-edge midpoint decoded incorrectly')
    count = packet_count = root_count = 0
    all_orders = [tuple(permutations((i for (i, v) in enumerate(vertices) if w.name in v))) for w in support.walls]
    for nums in compositions(10, 4):
        weights = tuple((Q(n, 10) for n in nums))
        answer = phase_average(support, vertices, weights)
        validate_distribution(support, answer)
        if not (weights[1] and weights[2]):
            check(answer == {v: w for (v, w) in zip(vertices, weights) if w}, 'A true cyclic simplex was not fixed')
        for root in support.chambers:
            check(phase_average(support, vertices, weights, root) == answer, 'Global chamber-root choice changed the phase average')
            root_count += 1
        for choices in product(*all_orders):
            orders = {w.name: order for (w, order) in zip(support.walls, choices)}
            (expanded, inputs) = split_packets(support, vertices, orders)
            check_support(expanded, inputs)
            raw = phase_average(expanded, inputs, weights)
            for layer in raw:
                check(actual_counts(expanded, layer) == (1, 1), 'An expanded-packet level used a torus more than once')
            check(packet_projection(expanded, raw) == answer, 'Parallel-copy order changed the actual selected class')
            packet_count += 1
        count += 1
    check(count == comb(13, 3), 'Wrong tetrahedron enumeration')
    bad = phase_average(support, vertices, (Q(0), Q(1, 2), Q(1, 2), Q(0)), illegal_shift={'p0': Q(1, 4)})
    check(any((actual_counts(support, layer) != (1, 1) for layer in bad)), 'Negative control failed to detect a forbidden independent phase')
    return {'barycentric_points': count, 'global_roots': root_count, 'packet_permutations': packet_count, 'distance_matrix': [[width(support, a, b) for b in vertices] for a in vertices], 'forbidden_independent_phase_detected': True}

def three_parallel_figure_eight():
    support = Support(('U', 'V'), (Wall('a13', 'V', 'U', (1, 3), 0, 'a13'), Wall('f2', 'U', 'U', (2,), 1, 'f2'), Wall('f1', 'U', 'V', (1,), 1, 'f1'), Wall('f3', 'U', 'V', (3,), 1, 'f3')), (1, 2, 3), (('f1', 'a13'), ('f2',), ('f3', 'a13')))
    vertices = (frozenset(('a13', 'f2')), frozenset(('f1', 'f2', 'f3')))
    check_support(support, vertices)
    check(width(support, *vertices) == 1, 'The two triple-parallel vertices are not adjacent')
    chi = [sum((w.minus_chi for w in support.walls if w.name in v)) for v in vertices]
    check(chi == [1, 3], 'The higher-complexity input was silently made taut')
    count = 0
    for n in range(25):
        weights = (Q(n, 24), Q(24 - n, 24))
        answer = phase_average(support, vertices, weights)
        validate_distribution(support, answer)
        check(answer == {v: w for (v, w) in zip(vertices, weights) if w}, 'The all-incompressible edge was not fixed')
        for order in ((0, 1), (1, 0)):
            orders = {'a13': (0,), 'f2': order, 'f1': (1,), 'f3': (1,)}
            (expanded, inputs) = split_packets(support, vertices, orders)
            check_support(expanded, inputs)
            check(packet_projection(expanded, phase_average(expanded, inputs, weights)) == answer, 'The shared one-boundary component changed under collapse')
            count += 1
    return {'barycentric_points': 25, 'shared_packet_orders': count, 'minus_chi': chi, 'ordinary_component_counts': [2, 3], 'width': 1}

def boundary_subset_homology():
    count = 0
    for b in range(1, 13):
        ds = [tuple((int(i == j) for j in range(b - 1))) for i in range(b - 1)]
        ds.append((-1,) * (b - 1))
        for included in product((0, 1), repeat=b):
            image = tuple((sum((a * d[j] for (a, d) in zip(included, ds))) for j in range(b - 1)))
            check((not any(image)) == (not any(included) or all(included)), 'A nonempty proper boundary subset has zero homology')
            count += 1
    return {'boundary_counts': '1..12', 'all_subsets': count}

def double_cone_control():
    support = Support(('O', 'L', 'R'), (Wall('e0', 'O', 'L', (1, 3), 0, 'e0'), Wall('e1', 'L', 'O', (1, 3), 0, 'e1'), Wall('f0', 'O', 'R', (2, 4), 0, 'f0'), Wall('f1', 'R', 'O', (2, 4), 0, 'f1')), (1, 2, 3, 4), (('e0', 'e1'), ('f0', 'f1'), ('e0', 'e1'), ('f0', 'f1')))
    vertices = tuple((frozenset(('e' + str(a), 'f' + str(b))) for (a, b) in ((0, 0), (1, 0), (0, 1), (1, 1))))
    check_support(support, vertices)
    check(width(support, vertices[1], vertices[2]) == 2, 'Cone-lens width collapsed')
    for nums in compositions(6, 4):
        weights = tuple((Q(n, 6) for n in nums))
        validate_distribution(support, phase_average(support, vertices, weights))
    return {'link': 'balanced T(8,20)', 'retained_cones': [2, 5], 'barycentric_points': comb(9, 3), 'extra_geometric_edge_width': 2}

def main():
    import json
    result = {'boundary_subset_homology': boundary_subset_homology(), 'double_parallel_7_4': two_bridge_parallel(), 'three_parallel_figure_eight': three_parallel_figure_eight(), 'double_cone_control': double_cone_control()}
    print('PASS: exact geometric diagnostics; topological inputs remain separate.')
    print(json.dumps(result, ensure_ascii=False, indent=2))
if __name__ == '__main__':
    main()
