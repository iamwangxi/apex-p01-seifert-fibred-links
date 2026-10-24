#!/usr/bin/env python3
"""Independent exact splice-geometric diagnostics. Standard library; stdout only; run with -B.

Embedded straight edges, fundamental-cycle winding signatures and fresh deletion
models supply the face data. No author's face/potential table is imported.
Neither this diagnostic nor its horizontal collar probes prove 3D normalisation.
"""
from collections import Counter, deque
from dataclasses import dataclass
from fractions import Fraction as F
from functools import cmp_to_key
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json
import math
import random


COUNTS = Counter()
WORD_CACHE = {}


def cross(a, b):
    return a[0]*b[1] - a[1]*b[0]


def add(a, b):
    return (a[0]+b[0], a[1]+b[1])


def sub(a, b):
    return (a[0]-b[0], a[1]-b[1])


def scale(a, t):
    return (a[0]*t, a[1]*t)


def on_segment(p, a, b):
    return cross(sub(b, a), sub(p, a)) == 0 and all(
        min(a[i], b[i]) <= p[i] <= max(a[i], b[i]) for i in (0, 1))


def intersections(a, b, c, d):
    """None means a proper crossing; a set records endpoint/overlap contacts."""
    u, v = sub(b, a), sub(d, c)
    s1, s2 = cross(u, sub(c, a)), cross(u, sub(d, a))
    s3, s4 = cross(v, sub(a, c)), cross(v, sub(b, c))
    if s1*s2 < 0 and s3*s4 < 0:
        return None
    return {p for p in (a, b, c, d)
            if on_segment(p, a, b) and on_segment(p, c, d)}


def winding(poly, p):
    result = 0
    for a, b in zip(poly, poly[1:]):
        assert not on_segment(p, a, b), (poly, p)
        side = cross(sub(b, a), sub(p, a))
        if a[1] <= p[1] < b[1] and side > 0:
            result += 1
        elif b[1] <= p[1] < a[1] and side < 0:
            result -= 1
    return result


def osc(v):
    return max(v)-min(v)


def compositions(total, length):
    if length == 1:
        yield (total,)
    else:
        for a in range(total+1):
            for tail in compositions(total-a, length-1):
                yield (a,)+tail


def word_order(rows):
    """Exhaust cyclic label orders; does not use any potential/chain test."""
    key = tuple(rows)
    if key in WORD_CACHE:
        return WORD_CACHE[key]
    q, r = sum(rows[0]), len(rows)
    columns = list(zip(*rows))
    for order in permutations(range(r)):
        word, offset = order*q, 0
        for column in columns:
            wanted = {i for i, bit in enumerate(column) if bit}
            if set(word[offset:offset+len(wanted)]) != wanted:
                break
            offset += len(wanted)
        else:
            assert offset == q*r
            WORD_CACHE[key] = order
            return order
    WORD_CACHE[key] = None
    return None


def sector_test(rows):
    sums = []
    for row in rows:
        v = [0]
        for bit in row:
            v.append(v[-1]+bit)
        sums.append(v)
    return all(osc([a-b for a, b in zip(u, v)]) <= 1
               for u, v in combinations(sums, 2))


@dataclass(frozen=True)
class Edge:
    name: str
    tail: str
    head: str


def angle_compare(a, b):
    def half(v):
        return 0 if v[1] > 0 or (v[1] == 0 and v[0] >= 0) else 1
    ha, hb = half(a), half(b)
    if ha != hb:
        return -1 if ha < hb else 1
    c = cross(a, b)
    return -1 if c > 0 else 1 if c < 0 else 0


class Drawing:
    def __init__(self, name, coordinates, negative, edges, q):
        self.name, self.q = name, q
        self.xy = {v: tuple(map(F, p)) for v, p in coordinates.items()}
        self.negative = set(negative)
        self.edges = tuple(Edge(*e) for e in edges)
        self.demands = {v: q if v == 'J' else 1 for v in coordinates}
        self.all = frozenset(range(len(edges)))
        for e in self.edges:
            assert e.tail in self.negative and e.head not in self.negative
        for i, j in combinations(self.all, 2):
            e, f = self.edges[i], self.edges[j]
            hit = intersections(self.xy[e.tail], self.xy[e.head],
                                self.xy[f.tail], self.xy[f.head])
            expected = {self.xy[v] for v in (e.tail, e.head)
                        if v in (f.tail, f.head)}
            assert hit is not None and hit <= expected, (name, e, f, hit)
            COUNTS['embedded_edge_pairs'] += 1
        size = sum(self.demands.values())//2
        self.matchings = []
        for chosen in combinations(self.all, size):
            degrees = Counter(v for i in chosen for v in
                              (self.edges[i].tail, self.edges[i].head))
            if all(degrees[v] == d for v, d in self.demands.items()):
                self.matchings.append(frozenset(chosen))
        self.matchings = tuple(self.matchings)
        assert self.matchings
        self.indicators = tuple(tuple(F(i in m) for i in self.all)
                                for m in self.matchings)
        self.lookup = {v: i for i, v in enumerate(self.indicators)}

    def edge_id(self, name):
        return next(i for i, e in enumerate(self.edges) if e.name == name)

    def matching_id(self, names):
        m = frozenset(self.edge_id(n) for n in names)
        return self.matchings.index(m)

    def flow(self, bary):
        return tuple(sum((c*self.indicators[i][e] for i, c in bary.items()), F(0))
                     for e in self.all)


class Faces:
    """Rebuild connected spherical regions from the actual embedded subgraph."""
    def __init__(self, drawing, allowed=None):
        self.g = drawing
        self.allowed = drawing.all if allowed is None else frozenset(allowed)
        parent = {v: v for v in drawing.xy}

        def find(v):
            while parent[v] != v:
                parent[v] = parent[parent[v]]
                v = parent[v]
            return v

        tree = {v: [] for v in drawing.xy}
        extra = []
        for i in sorted(self.allowed):
            e = drawing.edges[i]
            a, b = find(e.tail), find(e.head)
            if a == b:
                extra.append(i)
            else:
                parent[a] = b
                tree[e.tail].append(e.head)
                tree[e.head].append(e.tail)
        cycles = []
        for i in extra:
            e = drawing.edges[i]
            paths, todo = {e.head: [e.head]}, deque([e.head])
            while todo and e.tail not in paths:
                a = todo.popleft()
                for b in tree[a]:
                    if b not in paths:
                        paths[b] = paths[a]+[b]
                        todo.append(b)
            cycles.append([drawing.xy[e.tail]]+
                          [drawing.xy[v] for v in paths[e.tail]])
        self.cycles = cycles

        def signature(p):
            return tuple(winding(c, p) for c in cycles)

        self.signature = signature
        raw = {}
        for i in self.allowed:
            e = drawing.edges[i]
            a, b = drawing.xy[e.tail], drawing.xy[e.head]
            v = sub(b, a)
            n = scale((-v[1], v[0]), F(1, 10000)/(abs(v[0])+abs(v[1])))
            mid = scale(add(a, b), F(1, 2))
            raw[i] = (signature(add(mid, n)), signature(sub(mid, n)))
        signatures = set(s for pair in raw.values() for s in pair)
        if not signatures:
            signatures.add(())
        self.faces = tuple(sorted(signatures))
        self.index = {s: i for i, s in enumerate(self.faces)}
        self.lr = {e: (self.index[l], self.index[r]) for e, (l, r) in raw.items()}
        components = len({find(v) for v in drawing.xy})
        assert len(self.faces) == len(self.allowed)-len(drawing.xy)+components+1
        self.outside = self.index[(0,)*len(cycles)]
        ports = [i for i in self.allowed if drawing.edges[i].tail == 'J']
        assert ports
        rays = {i: sub(drawing.xy[drawing.edges[i].head], drawing.xy['J'])
                for i in ports}
        self.ports = tuple(sorted(ports, key=cmp_to_key(
            lambda i, j: angle_compare(rays[i], rays[j]))))
        sectors = []
        for i, e in enumerate(self.ports):
            a, b = rays[self.ports[i-1]], rays[e]
            an = scale(a, F(1)/(abs(a[0])+abs(a[1])))
            bn = scale(b, F(1)/(abs(b[0])+abs(b[1])))
            c = cross(a, b)
            d = add(an, bn)
            if c < 0:
                d = scale(d, -1)
            elif c == 0:
                d = (-a[1], a[0])
            probe = add(drawing.xy['J'], scale(d, F(1, 10000)))
            sectors.append(self.index[signature(probe)])
        self.sectors = tuple(sectors)
        self.root = sectors[0]
        COUNTS['geometrically_rebuilt_supports'] += 1

    def potential(self, flow, reference=0, root=None):
        g = self.g
        root = self.root if root is None else root
        adjacent = {f: [] for f in range(len(self.faces))}
        for e, (l, r) in self.lr.items():
            d = flow[e]-g.indicators[reference][e]
            if l == r:
                assert d == 0
            adjacent[r].append((l, d))
            adjacent[l].append((r, -d))
        values, todo = {root: F(0)}, deque([root])
        while todo:
            f = todo.popleft()
            for h, d in adjacent[f]:
                v = values[f]+d
                if h in values:
                    assert values[h] == v
                else:
                    values[h] = v
                    todo.append(h)
        assert len(values) == len(self.faces)
        return tuple(values[f] for f in range(len(self.faces)))

    def decode(self, flow, reference=0, root=None):
        g = self.g
        u = self.potential(flow, reference, root)
        cuts = sorted({F(0), F(1)} | {(-v) % 1 for v in u})
        result = {}
        for a, b in zip(cuts, cuts[1:]):
            t = (a+b)/2
            floors = tuple((v+t).__floor__() for v in u)
            bits = [F(0)]*len(g.edges)
            for e, (l, r) in self.lr.items():
                bits[e] = g.indicators[reference][e]+floors[l]-floors[r]
            i = g.lookup[tuple(bits)]
            assert g.matchings[i] <= self.allowed
            assert all(flow[e] > 0 for e in g.matchings[i])
            result[i] = result.get(i, F(0))+b-a
            COUNTS['positive_threshold_intervals'] += 1
        # Probe all collision values too; this is distinct from interval masses.
        for t in cuts[:-1]:
            floors = tuple((v+t).__floor__() for v in u)
            bits = [F(0)]*len(g.edges)
            for e, (l, r) in self.lr.items():
                bits[e] = g.indicators[reference][e]+floors[l]-floors[r]
            assert tuple(bits) in g.lookup
            COUNTS['critical_threshold_probes'] += 1
        assert sum(result.values()) == 1 and g.flow(result) == tuple(flow)
        COUNTS['decoder_calls'] += 1
        return result

    def restricted(self, u):
        return tuple(u[f] for f in self.sectors)

    def rows(self, ids):
        return tuple(tuple(int(e in self.g.matchings[i]) for e in self.ports)
                     for i in ids)


def model_a():
    xy = {'J': (-3, 0), 'N': (3, 0), 'p1': (0, 3),
          'p2': (0, 0), 'p3': (0, -3),
          'c0': (-8, -6), 'c1': (8, -6), 'c2': (8, 6), 'c3': (-8, 6)}
    edges = [(f'a{i}', 'J', f'p{i}') for i in (1, 2, 3)]
    edges += [(f'b{i}', 'N', f'p{i}') for i in (1, 2, 3)]
    edges += [('z0', 'c0', 'c3'), ('z1', 'c2', 'c1'),
              ('Z0', 'c0', 'c1'), ('Z1', 'c2', 'c3')]
    return Drawing('A_nested_q2', xy, ('J', 'N', 'c0', 'c2'), edges, 2)


def model_b():
    xy = {'J': (0, 0), 'N': (6, 0), 'p1': (3, 3),
          'p2': (3, 0), 'p3': (3, -3), 'u': (-3, -3),
          'V': (-6, 0), 'w': (-3, 3),
          'c0': (10, -3), 'c1': (16, -3), 'c2': (16, 3), 'c3': (10, 3)}
    edges = [(f'a{i}', 'J', f'p{i}') for i in (1, 2, 3)]
    edges += [(f'b{i}', 'N', f'p{i}') for i in (1, 2, 3)]
    edges += [('s0', 'J', 'u'), ('s1', 'V', 'w'),
              ('S0', 'J', 'w'), ('Sx', 'V', 'u')]
    edges += [('z0', 'c0', 'c3'), ('z1', 'c2', 'c1'),
              ('Z0', 'c0', 'c1'), ('Z1', 'c2', 'c3')]
    return Drawing('B_theta_petal_q3', xy, ('J', 'N', 'V', 'c0', 'c2'), edges, 3)


def state_id(g, i, z, p=None):
    names = [f'b{i}']+[f'a{j}' for j in (1, 2, 3) if j != i]
    names += ['z0', 'z1'] if z == 0 else ['Z0', 'Z1']
    if p is not None:
        names += ['s0', 's1'] if p == 0 else ['S0', 'Sx']
    return g.matching_id(names)


def trimmed_copy(a, b, offset, radius=F(1, 10)):
    v = sub(b, a)
    n = scale((-v[1], v[0]), F(1)/(abs(v[0])+abs(v[1])))
    shift = scale(n, offset)
    ta = min((radius-(1 if v[k] > 0 else -1)*shift[k])/abs(v[k])
             for k in (0, 1) if v[k])
    tb = min((radius+(1 if v[k] > 0 else -1)*shift[k])/abs(v[k])
             for k in (0, 1) if v[k])
    assert ta+tb < 1
    return add(add(a, shift), scale(v, ta)), add(add(b, shift), scale(v, -tb))


def square_parameter(p, centre, radius=F(1, 10)):
    x, y = sub(p, centre)
    if y == -radius:
        t = x+radius
    elif x == radius:
        t = 2*radius+y+radius
    elif y == radius:
        t = 4*radius+radius-x
    else:
        assert x == -radius
        t = 6*radius+radius-y
    return (t/(8*radius)) % 1


def allocate_and_extend(faces, ids):
    """Actually allocate disjoint parallel arcs; then check horizontal collar gaps."""
    ids = tuple(sorted(ids))
    order = word_order(faces.rows(ids))
    assert order is not None
    g = faces.g
    repeated, cursor = order*g.q, 0
    port_order = {}
    for e in faces.ports:
        users = {j for j, i in enumerate(ids) if e in g.matchings[i]}
        chosen = repeated[cursor:cursor+len(users)]
        assert set(chosen) == users
        port_order[e] = [ids[j] for j in chosen]
        cursor += len(users)
    copies, events = [], []
    for e in g.all:
        users = port_order.get(e, [i for i in ids if e in g.matchings[i]])
        edge = g.edges[e]
        for rank, i in enumerate(users):
            shift = (F(rank)-F(len(users)-1, 2))/10000
            a, b = trimmed_copy(g.xy[edge.tail], g.xy[edge.head], shift)
            copies.append((i, e, a, b))
            if edge.tail == 'J':
                events.append((square_parameter(a, g.xy['J']), i))
    for a, b in combinations(copies, 2):
        assert intersections(a[2], a[3], b[2], b[3]) == set(), (g.name, a, b)
        COUNTS['parallel_copy_segment_pairs'] += 1
    events.sort()
    word = tuple(i for _, i in events)
    r = len(ids)
    assert len(word) == g.q*r and len(set(word[:r])) == r
    assert word == word[:r]*g.q
    # Every interval after a reference trace contains one copy of every other
    # label. Its actual boundary graph values need not be equal across intervals.
    ref = word[0]
    start = next(j for j, (_, i) in enumerate(events) if i == ref)
    rotated = events[start:]+[(t+1, i) for t, i in events[:start]]
    rotated += [(rotated[0][0]+1, ref)]
    reference_indices = [j for j, (_, i) in enumerate(rotated) if i == ref]
    expected = tuple(i for i in word[:r] if i != ref)
    boundary_gaps = []
    for left, right in zip(reference_indices, reference_indices[1:]):
        part = rotated[left+1:right]
        assert tuple(i for _, i in part) == expected
        lo, hi = rotated[left][0], rotated[right][0]
        values = [(t-lo)/(hi-lo) for t, _ in part]
        for chi in (F(0), F(1, 3), F(1, 2), F(1)):
            graphs = [(1-chi)*F(j+1, r)+chi*v for j, v in enumerate(values)]
            gaps = [b-a for a, b in zip([F(0)]+graphs, graphs+[F(1)])]
            assert min(gaps) > 0
            boundary_gaps += gaps
            COUNTS['horizontal_collar_gap_checks'] += len(gaps)
    COUNTS['allocated_whole_family_carriers'] += 1
    COUNTS['allocated_annulus_occurrences'] += len(copies)
    return {'vertices': len(ids), 'annuli': len(copies),
            'trace_word': word, 'minimum_tested_gap': str(min(boundary_gaps))}


def complement_width(g, a, b):
    """Rebuild A union B, keep B as barriers, cross A-only walls by +1."""
    f = Faces(g, g.matchings[a] | g.matchings[b])
    adjacent = {i: [] for i in range(len(f.faces))}
    for e in g.matchings[a]-g.matchings[b]:
        l, r = f.lr[e]
        adjacent[r].append((l, 1))
        adjacent[l].append((r, -1))
    values, todo = {f.root: 0}, deque([f.root])
    while todo:
        i = todo.popleft()
        for j, d in adjacent[i]:
            h = values[i]+d
            if j in values:
                assert values[j] == h
            else:
                values[j] = h
                todo.append(j)
    assert len(values) == len(f.faces)
    COUNTS['complete_complement_pairs'] += 1
    return osc(list(values.values()))


def verify_drawing(g, denominator):
    f = Faces(g)
    potentials = [f.potential(v) for v in g.indicators]
    trace = [f.restricted(v) for v in potentials]
    restricted_dist = [[osc([a-b for a, b in zip(u, v)]) for v in trace]
                       for u in trace]
    full_dist = [[osc([a-b for a, b in zip(u, v)]) for v in potentials]
                 for u in potentials]
    y_pair = [[word_order(f.rows((i, j))) is not None
               for j in range(len(g.matchings))] for i in range(len(g.matchings))]
    for i, j in product(range(len(g.matchings)), repeat=2):
        assert y_pair[i][j] == (restricted_dist[i][j] <= 1)
        assert complement_width(g, i, j) == full_dist[i][j]
    def geometric(ids):
        return all(y_pair[i][j] for i, j in combinations(ids, 2))
    def cyclic(ids):
        return all(full_dist[i][j] <= 1 for i, j in combinations(ids, 2))
    simplices, x_simplices = [], []
    for size in range(1, len(g.matchings)+1):
        for ids in combinations(range(len(g.matchings)), size):
            if size <= 4:
                assert (word_order(f.rows(ids)) is not None) == geometric(ids)
                COUNTS['whole_word_vs_pairwise_tests'] += 1
            if geometric(ids):
                simplices.append(frozenset(ids))
            if cyclic(ids):
                x_simplices.append(frozenset(ids))
    maximal_y = [s for s in simplices if not any(s < t for t in simplices)]
    maximal_x = [s for s in x_simplices if not any(s < t for t in x_simplices)]
    allocations = [allocate_and_extend(f, s) for s in maximal_y]
    accepted, rejected, recoveries = 0, 0, 0
    subfaces = {}
    carriers = set()
    for serial, coefficients in enumerate(compositions(denominator, len(g.matchings))):
        bary = {i: F(c, denominator) for i, c in enumerate(coefficients) if c}
        if not geometric(bary):
            rejected += 1
            continue
        accepted += 1
        flow = g.flow(bary)
        out = f.decode(flow)
        assert cyclic(out)
        reference = min(bary, key=lambda i: trace[i])
        patterns = {tuple(a-b for a, b in zip(trace[i], trace[reference])) for i in bary}
        assert all(set(p) <= {0, 1} for p in patterns)
        carrier = frozenset(i for i in range(len(g.matchings))
                            if tuple(a-b for a, b in zip(trace[i], trace[reference]))
                            in patterns)
        carriers.add(carrier)
        assert set(out) <= carrier and set(bary) <= carrier and geometric(carrier)
        assert word_order(f.rows(tuple(sorted(carrier)))) is not None
        def law(point):
            result = {}
            for i, mass in point.items():
                result[trace[i]] = result.get(trace[i], F(0))+mass
            return result
        assert law(out) == law(bary)
        positive = frozenset(e for e, value in enumerate(flow) if value)
        if positive not in subfaces:
            subfaces[positive] = Faces(g, positive)
        supported_reference = next(i for i, m in enumerate(g.matchings) if m <= positive)
        assert subfaces[positive].decode(flow, supported_reference) == out
        COUNTS['zero_face_reconstruction_comparisons'] += 1
        if serial % 7 == 0:
            for ref in range(len(g.matchings)):
                assert f.decode(flow, ref) == out
                COUNTS['reference_comparisons'] += 1
            for root in range(len(f.faces)):
                assert f.decode(flow, root=root) == out
                COUNTS['root_comparisons'] += 1
        if cyclic(bary):
            assert out == bary
            recoveries += 1
        for t in (F(0), F(1, 5), F(1, 2), F(4, 5), F(1)):
            h = {i: (1-t)*bary.get(i, F(0))+t*out.get(i, F(0))
                 for i in set(bary) | set(out)}
            h = {i: c for i, c in h.items() if c}
            assert geometric(h) and g.flow(h) == flow and f.decode(g.flow(h)) == out
            if t == 0:
                assert h == bary
            if t == 1:
                assert h == out
            if cyclic(bary):
                assert h == bary
            COUNTS['strong_homotopy_parameter_checks'] += 1
        COUNTS['restricted_carrier_and_trace_law_checks'] += 1
    # An asymmetric point in every cyclic face checks more than vertex fixing.
    for simplex in x_simplices:
        ids = sorted(simplex)
        bary = {i: F(j+1, len(ids)*(len(ids)+1)//2) for j, i in enumerate(ids)}
        assert f.decode(g.flow(bary)) == bary
        COUNTS['all_cyclic_faces_exact_recovery'] += 1
    for s in carriers:
        assert word_order(f.rows(tuple(sorted(s)))) is not None
    if g.name.startswith('A'):
        bad = (state_id(g, 3, 0), state_id(g, 1, 1))
        good = (state_id(g, 1, 0), state_id(g, 3, 1))
        base = state_id(g, 3, 0)
        state_ids = [(i, z, state_id(g, i, z)) for i in (3, 2, 1) for z in (0, 1)]
    else:
        bad = (state_id(g, 1, 0, 1), state_id(g, 3, 1, 0))
        good = (state_id(g, 3, 0, 0), state_id(g, 1, 1, 1))
        base = state_id(g, 3, 0, 0)
        state_ids = [(i, p, z, state_id(g, i, z, p))
                     for i in (3, 2, 1) for p in (0, 1) for z in (0, 1)]
        illegal = (state_id(g, 1, 0, 0), state_id(g, 3, 0, 1))
        assert not geometric(illegal) and word_order(f.rows(illegal)) is None
        COUNTS['illegal_nonempty_trace_pair_rejections'] += 1
    x = {i: F(1, 2) for i in bad}
    assert geometric(bad) and not cyclic(bad)
    assert f.decode(g.flow(x)) == {i: F(1, 2) for i in good}
    # Root at outside only for printing these independently recovered values.
    printed = []
    for state in state_ids:
        p = f.potential(g.indicators[state[-1]], base, f.outside)
        printed.append({'state': state[:-1], 'matching_id': state[-1],
                        'potential_in_signature_face_order': list(map(str, p))})
    return {'name': g.name, 'actual_zero_boundaries': len(g.xy)-1, 'q': g.q,
            'edges': len(g.edges), 'regions': len(f.faces),
            'matchings': len(g.matchings), 'faces': f.faces, 'J_sectors': f.sectors,
            'outside_meets_J': f.outside in f.sectors,
            'maximal_Y_carriers': len(maximal_y),
            'maximal_Y_vertices': sorted(map(len, maximal_y)),
            'maximal_X_simplices': len(maximal_x),
            'maximal_X_vertices': sorted(map(len, maximal_x)),
            'denominator': denominator, 'accepted_inputs': accepted,
            'rejected_inputs': rejected, 'X_inputs_recovered': recoveries,
            'different_positive_supports': len(subfaces),
            'carrier_sets_examined': len(carriers), 'allocations': allocations,
            'bad_geometric_edge_ids': bad, 'decoded_midpoint_edge_ids': good,
            'bad_edge_full_width': int(full_dist[bad[0]][bad[1]]),
            'bad_edge_trace_width': int(restricted_dist[bad[0]][bad[1]]),
            'state_potentials': printed}


def trace_word_attacks():
    rng = random.Random(20261024)
    # All distinct collections through four labels on six coherent bundles.
    for bundles, q in ((4, 2), (6, 2), (6, 3), (6, 4)):
        rows = [tuple(int(j in picked) for j in range(bundles))
                for picked in combinations(range(bundles), q)]
        for size in (2, 3, 4):
            for chosen in combinations(rows, size):
                assert sector_test(chosen) == (word_order(chosen) is not None)
                COUNTS['independent_trace_matrices'] += 1
    # Ties, empty bundles and six labels, beyond the author's four-label bound.
    for _ in range(1200):
        bundles = rng.randrange(4, 9)
        q = rng.randrange(1, bundles)
        size = rng.randrange(2, 7)
        rows = tuple(tuple(int(j in picked) for j in range(bundles))
                     for picked in (set(rng.sample(range(bundles), q))
                                    for _ in range(size)))
        assert sector_test(rows) == (word_order(rows) is not None)
        COUNTS['independent_trace_matrices'] += 1
    # If the unit actual end were dropped, one bundle could have two occurrences
    # of the same label. That case is deliberately outside the diagnostic domain.
    assert word_order(((1, 1, 0, 0), (0, 0, 1, 1))) is None


def cycles_of_translation(degree, shift):
    unseen, cycles = set(range(degree)), []
    while unseen:
        first = min(unseen)
        orbit, v = [], first
        while v in unseen:
            unseen.remove(v)
            orbit.append(v)
            v = (v+shift) % degree
        assert v == first
        cycles.append(orbit)
    assert len(cycles) == math.gcd(degree, shift)
    return cycles


def splice(p, r, d, Psigns, Qsigns):
    """Positive (1,p), negative (1,r), G_d; at most one retained cone."""
    assert p == 1 or r == 1
    sP, sQ = sum(Psigns), sum(Qsigns)
    A = ((p+d, 1), (1+r*(p+d), r))
    assert A[0][0]*A[1][1]-A[0][1]*A[1][0] == -1
    tP, tQ = -r*sQ, p*sP+d*r*sQ
    kP, kQ = p*(sP-r*sQ), -r*(p*sP+(d*r+1)*sQ)
    assert kP == kQ*A[0][0]+tQ*A[1][0]
    assert tP == kQ*A[0][1]+tQ*A[1][1]
    assert kP == 0 and kQ != 0
    q = math.gcd(abs(kP), abs(tP))
    assert q == math.gcd(abs(kQ), abs(tQ)) and abs(kQ) == q*A[1][0]
    # g(lambda_P)=mu_Q+d lambda_Q intersects the filled Q meridian once.
    assert abs(1*1-0*d) == 1
    # Pairwise linking, also independently checked against all fibre values.
    PP, QQ, PQ = p, -r*(1+d*r), -p*r
    assert all(v != 0 for v in (PP, QQ, PQ))
    assert PP*sP+PQ*sQ == kP and PQ*sP+QQ*sQ == kQ
    degree = abs(kQ)
    actual = [cycles_of_translation(degree, e) for e in Qsigns]
    ports = cycles_of_translation(degree, tQ)
    assert all(len(c) == 1 for c in actual) and len(ports) == q
    assert math.gcd(degree, *Qsigns, tQ) == 1
    chi = degree*(1-len(Qsigns))
    cone_cycles = []
    if r > 1:
        assert kQ % r == 0
        cone_shift = kQ//r
        assert (sum(Qsigns)+tQ+cone_shift) % degree == 0
        cone_cycles = cycles_of_translation(degree, cone_shift)
        assert all(len(c) == r for c in cone_cycles)
        chi = degree*(-len(Qsigns))+len(cone_cycles)
    else:
        assert (sum(Qsigns)+tQ) % degree == 0
    b = len(Qsigns)+q
    assert (2-b-chi) % 2 == 0
    genus = (2-b-chi)//2
    assert genus >= 0
    COUNTS['actual_S3_splice_and_cover_checks'] += 1
    return {'p': p, 'r': r, 'd': d, 'A': A,
            'P_sign_counts': (Psigns.count(1), Psigns.count(-1)),
            'Q_sign_counts': (Qsigns.count(1), Qsigns.count(-1)),
            'kP_kQ_tP_tQ_q': (kP, kQ, tP, tQ, q),
            'pairwise_coherent_linkings_PP_QQ_PQ': (PP, QQ, PQ),
            'Q_degree': degree, 'Q_JSJ_cycle_lengths': list(map(len, ports)),
            'Q_cone_cycle_lengths': list(map(len, cone_cycles)),
            'Q_chi_boundaries_genus': (chi, b, genus)}


def main():
    here = Path(__file__).resolve().parent
    root = here.parent
    sources = sorted((root/'proof').glob('*.md'))
    before = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    trace_word_attacks()
    cases = [splice(1, 1, 1, [1]*5+[-1]*3, [1]*3+[-1]),
             splice(1, 3, 1, [1]*7+[-1]*4, [1, 1, -1]),
             splice(5, 1, 1, [1]*5+[-1]*3, [1]*3+[-1]),
             splice(1, 3, 1, [1]*5+[-1]*2, [1])]
    # Same A graph remains legal on a zero cone of every tested order.
    for p in range(2, 18):
        splice(p, 1, 1, [1]*5+[-1]*3, [1]*3+[-1])
    # Additional horizontal-cone degree/count checks; these are not 3D isotopies.
    for r in range(2, 18):
        splice(1, r, 1, [1]*(r+2)+[-1]*2, [1, 1, -1])
    models = [verify_drawing(model_a(), 5), verify_drawing(model_b(), 4)]
    # A one-actual-boundary cone block on the HORIZONTAL side need not have
    # q=1 or a singleton global vertex set. The English proof limits its point
    # claim to the zero side; this negative control checks that distinction.
    b = model_b()
    low = Drawing('C_horizontal_low_cable',
                  {v: p for v, p in b.xy.items() if not v.startswith('c')},
                  ('J', 'N', 'V'),
                  [(e.name, e.tail, e.head) for e in b.edges[:10]], 3)
    low_faces = Faces(low)
    assert len(low.matchings) == 6 and low.q == cases[-1]['kP_kQ_tP_tQ_q'][-1] == 3
    low_check = {'q': low.q, 'distinct_supported_vertices': len(low.matchings),
                 'ordinary_zero_boundaries': len(low.xy)-1,
                 'ordinary_coned_horizontal_boundaries': 2,
                 'horizontal_chi_boundaries_genus': cases[-1]['Q_chi_boundaries_genus']}
    after = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    assert before == after
    print(json.dumps({'status': 'PASS', 'counts': dict(COUNTS), 'splices': cases,
                      'models': models, 'horizontal_low_cable_control': low_check,
                      'unchanged_source_sha256': before,
                      'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
                     ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
