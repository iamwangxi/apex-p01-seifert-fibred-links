#!/usr/bin/env python3
# Finite exact diagnostic for Part 7 of the proof; standard library only; prints a deterministic report and writes no files.
import argparse
from collections import defaultdict, deque
from fractions import Fraction
from hashlib import sha256
from math import gcd, prod
from pathlib import Path

def require(test, message):
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
        queue = [unseen.pop()]
        found = set(queue)
        while queue:
            for v in adjacency[queue.pop()]:
                if v in unseen:
                    unseen.remove(v)
                    found.add(v)
                    queue.append(v)
        result.append(found)
    return result

def polynomial_trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def polynomial_product(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for (i, x) in enumerate(a):
        for (j, y) in enumerate(b):
            result[i + j] += x * y
    return polynomial_trim(result)

def polynomial_quotient(a, b):
    remainder = a[:]
    result = [0] * (len(a) - len(b) + 1)
    while any(remainder) and len(remainder) >= len(b):
        degree = len(remainder) - len(b)
        require(remainder[-1] % b[-1] == 0, 'nonintegral quotient')
        coefficient = remainder[-1] // b[-1]
        result[degree] = coefficient
        for (i, value) in enumerate(b):
            remainder[degree + i] -= coefficient * value
        polynomial_trim(remainder)
    require(not any(remainder), 'nonzero polynomial remainder')
    return polynomial_trim(result)

def t_power_minus_one(n):
    return [-1] + [0] * (n - 1) + [1]

def torus_alexander(p, q):
    q = abs(q)
    require(p > 0 and q > 0 and (gcd(p, q) == 1), 'noncoprime torus data')
    numerator = polynomial_product(t_power_minus_one(p * q), [-1, 1])
    denominator = polynomial_product(t_power_minus_one(p), t_power_minus_one(q))
    return polynomial_quotient(numerator, denominator)

def substitute_power(a, p):
    result = [0] * (p * (len(a) - 1) + 1)
    for (i, x) in enumerate(a):
        result[p * i] = x
    return result

def cable_checks():
    primitive_tests = 0
    for p in range(2, 13):
        for q in range(-13, 14):
            if q == 0 or gcd(p, abs(q)) != 1:
                continue
            (mu_new, lambda_old) = ((1, 0), (0, 1))
            (mu_old, lambda_new) = ((p, 0), (0, p))
            h_from_new = (p * q, p)
            h_from_old = tuple((p * x + q * y for (x, y) in zip(lambda_old, mu_old)))
            require(h_from_new == h_from_old, 'fibre peripheral mismatch')
            possible = []
            for b in range(1, 17):
                for c in range(-16, 17):
                    if sum((x * y for (x, y) in zip((b, c), lambda_new))) == 0:
                        if gcd(b, abs(c)) == 1:
                            possible.append((b, c))
            require(possible == [(1, 0)], 'primitive class did not force one outer boundary')
            require(gcd(*mu_old) == p, 'inner boundary count')
            chi = abs(p * q) * (Fraction(1, p) - 1)
            genus = Fraction(2 - (p + 1) - chi, 2)
            require(genus == Fraction((p - 1) * (abs(q) - 1), 2), 'piece genus')
            require(genus.denominator == 1 and genus >= 0, 'invalid horizontal piece')
            primitive_tests += 1
    named = []
    for (name, a, b, p, q) in (('K_A', 2, 3, 2, 1), ('K_B', 2, 5, 3, 2)):
        base = torus_alexander(a, b)
        delta = polynomial_product(torus_alexander(p, q), substitute_power(base, p))
        genus = Fraction(len(delta) - 1, 2)
        base_chi = 1 - (len(base) - 1)
        piece_chi = -(p - 1) * abs(q)
        assembled_chi = piece_chi + p * base_chi
        require(assembled_chi == 1 - 2 * genus, 'Alexander degree / assembly disagreement')
        signs = sorted((((Fraction(k) + theta) / p, sign) for k in range(p) for (theta, sign) in ((Fraction(1, 5), 1), (Fraction(3, 5), -1))))
        require([s for (_, s) in signs] == [1, -1] * p, 'nonalternating leaf trace')
        require(abs(p * a * b - q) > 0, 'nongenuine cable / companion cut')
        expected = {'K_A': (2, 6, 4, 11, 2), 'K_B': (7, 26, 6, 28, 6)}[name]
        result = (int(genus), int(2 * (2 * genus - 1)), len(signs), abs(p * a * b - q), abs(p * q))
        require(result == expected, 'named example values')
        named.append({'name': name, 'genus': int(genus), 'complexity': result[1], 'leaf_trace': result[2], 'JSJ_determinants': result[3:], 'Alexander_coefficients_low_to_high': delta})
    print('cable primitive/peripheral parameter cases:', primitive_tests)
    for example in named:
        print(example)

def unique_tree_path(adjacency, start, finish):
    queue = deque([(start, [start])])
    while queue:
        (v, path) = queue.popleft()
        if v == finish:
            return path
        for w in adjacency[v]:
            if w not in path:
                queue.append((w, path + [w]))
    raise AssertionError('disconnected tree')

def anchored_splice_checks():
    sigma = {'C': -1, 'H': 1, 'A': -1, 'B': -1, 'D': 1, 'E': 1}
    edges = [('C', 'H'), ('H', 'A'), ('H', 'B'), ('C', 'D'), ('C', 'E')]
    adjacency = defaultdict(list)
    for (a, b) in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)
    actual = [(v, index) for v in 'ABDE' for index in range(2)]

    def probe_linking(v, w):
        return prod((sigma[x] for x in unique_tree_path(adjacency, v, w)))
    k = {v: sum((probe_linking(v, w) for (w, _) in actual)) for v in sigma}
    require(k == {'C': 0, 'H': -8, 'A': 4, 'B': 4, 'D': 4, 'E': 4}, 'probe linking k')
    x = {}
    for v in sigma:
        for w in adjacency[v]:
            x[v, w] = sum((probe_linking(w, target) for (target, _) in actual if v not in unique_tree_path(adjacency, w, target)))
    divisibility = {}
    for v in sigma:
        values = ([1, 1] if v in 'ABDE' else []) + [x[v, w] for w in adjacency[v]]
        divisor = 0
        for value in values:
            divisor = gcd(divisor, abs(value))
        divisibility[v] = divisor
        require(k[v] == sigma[v] * ((2 if v in 'ABDE' else 0) + sum((x[v, w] for w in adjacency[v]))), 'local H1 / linking mismatch')
    require(divisibility == {'C': 2, 'H': 2, 'A': 1, 'B': 1, 'D': 1, 'E': 1}, 'block div')
    q = [gcd(abs(x[v, w]), abs(x[w, v])) for (v, w) in edges]
    require(q == [4, 2, 2, 2, 2], 'port restrictions')
    require([x['C', w] for w in 'HDE'] == [-4, 2, 2], 'zero-block demands')
    require(all((abs(sigma[v] * sigma[w] - 1) == 2 for (v, w) in edges)), 'Hopf genuine cuts')
    horizontal = {v for v in sigma if k[v] != 0}
    clusters = components(horizontal, [(a, b) for (a, b) in edges if a in horizontal and b in horizontal])
    require(all((c & set('ABDE') for c in clusters)), 'missing anchor')
    require(len(components(['H0', 'H1', 'A', 'B'], [(h, v) for h in ('H0', 'H1') for v in ('A', 'B')])) == 1, 'horizontal cluster disconnected')
    norm = sum((abs(value) for value in k.values()))
    genus = (2 - len(actual) + norm) // 2
    require((norm, genus) == (24, 9), 'assembled six-block topology')
    print('six-block probe-linking result:', {'k': k, 'div': divisibility, 'q': q, 'norm': norm, 'genus': genus})

def disk_chord_faces(n, chords):
    edges = [(i, (i + 1) % n) for i in range(n)] + chords
    chord_at = {}
    for (edge_id, (a, b)) in enumerate(chords, n):
        require(a not in chord_at and b not in chord_at, 'not a matching')
        chord_at[a] = edge_id
        chord_at[b] = edge_id
    rotation = {}
    for v in range(n):
        rotation[v] = [v] + ([chord_at[v]] if v in chord_at else []) + [(v - 1) % n]
    face_of = {}
    faces = []
    for (edge_id, endpoints) in enumerate(edges):
        for start in endpoints:
            first = (edge_id, start)
            if first in face_of:
                continue
            current = first
            face = []
            while current not in face_of:
                (e, v) = current
                face_of[current] = len(faces)
                face.append(current)
                (a, b) = edges[e]
                w = b if v == a else a
                cyclic = rotation[w]
                next_edge = cyclic[(cyclic.index(e) - 1) % len(cyclic)]
                current = (next_edge, w)
            require(current == first, 'inconsistent face walk')
            faces.append(face)
    outside = {face_of[i, (i + 1) % n] for i in range(n)}
    require(len(outside) == 1, 'outer face split: crossing chord system')
    outside = outside.pop()
    inside = set(range(len(faces))) - {outside}
    require(len(inside) == len(chords) + 1, 'Euler planar disk-face count')
    dual_edges = [(face_of[e, a], face_of[e, b]) for (e, (a, b)) in enumerate(edges[n:], n)]
    require(all((a != b and a in inside and (b in inside) for (a, b) in dual_edges)), 'nonseparating return')
    require(len(components(inside, dual_edges)) == 1, 'disconnected dual')
    return (inside, dual_edges, face_of)

def each_dual_edge_separates(inside, dual_edges, cap_a, cap_b):
    require(cap_a in inside and cap_b in inside, 'missing cap')
    for i in range(len(dual_edges)):
        pieces = components(inside, dual_edges[:i] + dual_edges[i + 1:])
        require(len(pieces) == 2, 'return is not separating')
        require(any((cap_a in c and cap_b not in c for c in pieces)), 'return does not separate marks')

def square_knot_checks(max_r):
    annuli = 0
    for r in range(1, max_r + 1):
        n = 2 * r
        signs = [1 if i == 0 or i > r else -1 for i in range(n)]
        leaf = [(i, (1 - i) % n) for i in range(n) if i < (1 - i) % n]
        pattern = [(i, n - i) for i in range(1, r)]
        require(sum(signs) == 0 and signs[0] == 1 and (signs[r] == -1), 'section orientation')
        require(all((signs[a] + signs[b] == 0 for (a, b) in leaf + pattern)), 'annular orientation mismatch')
        (inside, dual, face_of) = disk_chord_faces(n, leaf)
        each_dual_edge_separates(inside, dual, face_of[0, 0], face_of[r, r])
        require(len(inside) == r + 1, 'leaf product-chamber count')
        (inside, dual, face_of) = disk_chord_faces(n, pattern)
        each_dual_edge_separates(inside, dual, face_of[0, 0], face_of[r, r])
        require(len(inside) == r, 'pattern region count')
        surface_edges = leaf + leaf + pattern + [(0, n), (r, n + 1)]
        require(len(components(range(n + 2), surface_edges)) == 1, 'closed/unreached component')
        require(len(surface_edges) - (n + 2) + 1 == r, 'surface graph first Betti number')
        chi = n * -1
        require((2 - 2 - chi) // 2 == r, 'surface genus')
        eta = (1, -6, 6)
        require(eta[1] + eta[2] == 0, 'outer longitude not killed')
        require(6 * eta[0] + eta[1] == 0 and -6 * eta[0] + eta[2] == 0, 'leaf fibre slope mismatch')
        require(all((sum((sign * value for sign in signs)) == 0 for value in eta)), 'nonzero total companion class')
        trace = (n, n, n)
        require(sum(trace) == 6 * r, 'trace arithmetic')
        annuli += len(surface_edges)
    print('square-knot disk-face / oriented assembly cases:', max_r, '; annulus occurrences including actual collars:', annuli)

def main():
    max_r = 128
    anchored_splice_checks()
    cable_checks()
    square_knot_checks(max_r)
    print('PASS: independent finite algebra / planar embedding diagnostics only')
if __name__ == '__main__':
    main()
