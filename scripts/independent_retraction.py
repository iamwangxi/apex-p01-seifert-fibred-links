#!/usr/bin/env python3
"""Geometric-comparison independent, offline diagnostics. Standard library only; no file writes.

Run with python3 -B. This script does not import any author checker or source.
It constructs a four-actual-boundary, two-cone example from rational PL paths,
extracts spherical regions by fundamental-cycle winding signatures, enumerates
matchings, and tests the proposed decoder/retraction. A second mother graph is
a sampled Dehn twist of the first, with a common non-cyclic geometric face.
All subsequent geometry and arithmetic are exact Fractions; the initial twist
is sampled numerically, then rounded to rational coordinates and validated as
an embedded PL graph. This is a bounded diagnostic, not a 3D proof.
"""

from collections import Counter, deque
from fractions import Fraction as F
from itertools import combinations, product
from math import atan2, cos, hypot, pi, sin
from random import Random
import json


COUNTS = Counter()
RNG = Random(20261024)


def point(x, y):
    return (F(x), F(y))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def mul(t, a):
    return (t * a[0], t * a[1])


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def orient(a, b, c):
    return cross(sub(b, a), sub(c, a))


def on_segment(p, a, b):
    return (orient(a, b, p) == 0
            and min(a[0], b[0]) <= p[0] <= max(a[0], b[0])
            and min(a[1], b[1]) <= p[1] <= max(a[1], b[1]))


def intersects(a, b, c, d):
    if (max(a[0], b[0]) < min(c[0], d[0])
            or max(c[0], d[0]) < min(a[0], b[0])
            or max(a[1], b[1]) < min(c[1], d[1])
            or max(c[1], d[1]) < min(a[1], b[1])):
        return False
    ab_c, ab_d = orient(a, b, c), orient(a, b, d)
    cd_a, cd_b = orient(c, d, a), orient(c, d, b)
    return ((ab_c * ab_d < 0 and cd_a * cd_b < 0)
            or on_segment(c, a, b) or on_segment(d, a, b)
            or on_segment(a, c, d) or on_segment(b, c, d))


def proper_crossing(a, b, c, d):
    return (orient(a, b, c) * orient(a, b, d) < 0
            and orient(c, d, a) * orient(c, d, b) < 0)


def winding(p, polygon):
    number = 0
    for a, b in zip(polygon, polygon[1:]):
        assert not on_segment(p, a, b), ('boundary probe', p)
        side = orient(a, b, p)
        if a[1] <= p[1] < b[1] and side > 0:
            number += 1
        elif b[1] <= p[1] < a[1] and side < 0:
            number -= 1
    return number


VERTICES = {0: point(-3, -2), 1: point(3, -2),
            2: point(3, 2), 3: point(-3, 2)}
NEGATIVE = {1, 3}
POSITIVE = {0, 2}
CONES = ((point(0, -3), 2), (point(0, 3), 3))


def edge(a, b, interior=()):
    assert a in NEGATIVE and b in POSITIVE
    return (a, b, (VERTICES[a],) + tuple(interior) + (VERTICES[b],))


CORE = {
    'e0': edge(1, 0),
    'e1': edge(1, 0, (point(2, -4), point(-2, -4))),
    'f0': edge(3, 2),
    'f1': edge(3, 2, (point(-2, 4), point(2, 4))),
}
PLAIN = dict(CORE, sl=edge(3, 0), sr=edge(1, 2))


def twist_path(record, steps=112):
    a, b, path = record
    assert len(path) == 2
    # Essential annulus about the lower lens: centre (0,-5/2),
    # radii 13/4 and 4. CORE misses the annulus. The endpoints are fixed.
    out = []
    for k in range(steps + 1):
        t = k / steps
        x = float(path[0][0]) * (1 - t) + float(path[1][0]) * t
        y = float(path[0][1]) * (1 - t) + float(path[1][1]) * t
        r = hypot(x, y + 2.5)
        amount = max(0.0, min(1.0, (r - 3.25) / .75))
        if amount in (0.0, 1.0):
            q = add(mul(F(steps - k, steps), path[0]),
                    mul(F(k, steps), path[1]))
        else:
            angle = atan2(y + 2.5, x) + 2 * pi * amount
            q = (F(round(r * cos(angle) * 10**9), 10**9),
                 F(round((r * sin(angle) - 2.5) * 10**9), 10**9))
        if not out or q != out[-1]:
            out.append(q)
    assert out[0] == path[0] and out[-1] == path[-1]
    return a, b, tuple(out)


TWISTED = dict(CORE, tl=twist_path(PLAIN['sl']),
               tr=twist_path(PLAIN['sr']))


class Graph:
    def __init__(self, name, records, check_embedding=False):
        self.name, self.records = name, dict(sorted(records.items()))
        self.names = tuple(self.records)
        self.segments = [(e, i, a, b)
                         for e, (_, _, p) in self.records.items()
                         for i, (a, b) in enumerate(zip(p, p[1:]))]
        if check_embedding:
            self.check_embedding()
        incident = {v: [] for v in VERTICES}
        for e, (a, b, _) in self.records.items():
            incident[a].append((b, e))
            incident[b].append((a, e))

        def enumerate_matchings(remaining):
            if not remaining:
                yield frozenset()
                return
            v = min(remaining)
            for other, e in incident[v]:
                if other in remaining:
                    for rest in enumerate_matchings(remaining - {v, other}):
                        yield rest | {e}

        self.matchings = tuple(sorted(set(enumerate_matchings(set(VERTICES))),
                                      key=lambda m: tuple(sorted(m))))
        assert self.matchings, (name, 'no perfect matching')
        self.cycles, components = self.fundamental_cycles()
        self.lr = {}
        for e in self.names:
            _, _, a, b = next(s for s in self.segments if s[0] == e)
            middle = mul(F(1, 2), add(a, b))
            dx, dy = sub(b, a)
            normal = (-dy, dx)
            epsilon = F(1, 64)
            for _ in range(100):
                left = add(middle, mul(epsilon, normal))
                right = sub(middle, mul(epsilon, normal))
                # The transverse probe may meet only its own segment.
                if all(not intersects(left, right, c, d)
                       for f, j, c, d in self.segments
                       if (f, j) != (e, 0)):
                    break
                epsilon /= 2
            else:
                raise AssertionError('unable to find a safe local probe')
            self.lr[e] = (self.signature(left), self.signature(right))
        self.faces = tuple(sorted({f for pair in self.lr.values() for f in pair}))
        assert len(self.faces) == len(self.names) - len(VERTICES) + components + 1
        self.root = (0,) * len(self.cycles)
        assert self.root in self.faces
        self.cone_faces = tuple(self.signature(p) for p, _ in CONES)
        assert all(f in self.faces for f in self.cone_faces)
        self.distance = {}
        ref = self.matchings[0]
        heights = {m: self.potential(self.vector(m), ref) for m in self.matchings}
        for a, b in combinations(self.matchings, 2):
            d = [heights[a][f] - heights[b][f] for f in self.faces]
            self.distance[a, b] = self.distance[b, a] = max(d) - min(d)
        self.height = heights

    def check_embedding(self):
        for (e, i, a, b), (f, j, c, d) in combinations(self.segments, 2):
            assert a != b and c != d
            if not intersects(a, b, c, d):
                continue
            common = set((a, b)) & set((c, d))
            if e == f and abs(i - j) == 1:
                assert len(common) == 1
            elif e != f and common <= set(VERTICES.values()) and len(common) == 1:
                pass
            else:
                raise AssertionError(('nonembedded PL input', self.name, e, i, f, j))
            # Shared-endpoint segments must not overlap along a ray.
            if common:
                p = next(iter(common))
                u = b if a == p else a
                v = d if c == p else c
                assert not on_segment(u, p, v) and not on_segment(v, p, u)
        COUNTS['embedded_mother_graphs'] += 1

    def fundamental_cycles(self):
        parent = {v: v for v in VERTICES}
        tree = {v: [] for v in VERTICES}

        def root(v):
            while parent[v] != v:
                v = parent[v]
            return v

        cycles = []
        for e, (a, b, path) in self.records.items():
            ra, rb = root(a), root(b)
            if ra != rb:
                parent[ra] = rb
                tree[a].append((b, path))
                tree[b].append((a, tuple(reversed(path))))
                continue
            pending = deque([(b, (b,), ())])
            while pending:
                v, visited, back = pending.popleft()
                if v == a:
                    polygon = path + back[1:]
                    assert polygon[0] == polygon[-1]
                    cycles.append(polygon)
                    break
                for w, p in tree[v]:
                    if w not in visited:
                        pending.append((w, visited + (w,), back + p if not back
                                        else back + p[1:]))
            else:
                raise AssertionError('forest path missing')
        return tuple(cycles), len({root(v) for v in VERTICES})

    def signature(self, p):
        return tuple(winding(p, c) for c in self.cycles)

    def vector(self, m):
        return {e: F(e in m) for e in self.names}

    def flow(self, bary):
        return {e: sum((mass for m, mass in bary.items() if e in m), F(0))
                for e in self.names}

    def potential(self, w, reference, root=None):
        root = self.root if root is None else root
        adjacent = {f: [] for f in self.faces}
        for e, (left, right) in self.lr.items():
            jump = w[e] - F(e in reference)
            adjacent[right].append((left, jump))
            adjacent[left].append((right, -jump))
        values = {root: F(0)}
        pending = deque([root])
        while pending:
            f = pending.popleft()
            for g, change in adjacent[f]:
                value = values[f] + change
                if g in values:
                    assert values[g] == value
                else:
                    values[g] = value
                    pending.append(g)
        assert set(values) == set(self.faces), 'more than one potential constant'
        return values

    def simplex(self, bary):
        return all(self.distance[a, b] == 1
                   for a, b in combinations(bary, 2))

    def decode(self, w, reference=None, root=None, critical=False):
        reference = self.matchings[0] if reference is None else reference
        assert all(0 <= w[e] <= 1 for e in self.names)
        for v in VERTICES:
            assert sum(w[e] for e, (a, b, _) in self.records.items()
                       if v in (a, b)) == 1
        u = self.potential(w, reference, root)
        cuts = sorted({F(0), F(1)} | {(-value) % 1 for value in u.values()})

        def rounded(theta):
            q = {f: (value + theta).__floor__() for f, value in u.items()}
            bits = {e: int(e in reference) + q[left] - q[right]
                    for e, (left, right) in self.lr.items()}
            assert set(bits.values()) <= {0, 1}
            m = frozenset(e for e, bit in bits.items() if bit)
            assert m in self.matchings
            assert all(w[e] > 0 for e in m)
            COUNTS['rounding_probes'] += 1
            return m

        out = {}
        for lo, hi in zip(cuts, cuts[1:]):
            m = rounded((lo + hi) / 2)
            out[m] = out.get(m, F(0)) + hi - lo
        if critical:
            for theta in cuts[:-1]:
                rounded(theta)
            COUNTS['critical_threshold_inputs'] += 1
        assert sum(out.values()) == 1
        assert self.simplex(out), ('not a true simplex', self.name, out)
        assert self.flow(out) == w
        COUNTS['decoder_calls'] += 1
        return out


def clean(bary):
    return {m: a for m, a in bary.items() if a}


def homotopy(bary, decoded, t):
    return clean({m: (1-t) * bary.get(m, F(0)) + t * decoded.get(m, F(0))
                  for m in set(bary) | set(decoded)})


def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for a in range(n + 1):
            for rest in compositions(n-a, k-1):
                yield (a,) + rest


def random_bary(matchings):
    values = [RNG.randrange(20) for _ in matchings]
    if not any(values):
        values[0] = 1
    return {m: F(a, sum(values)) for m, a in zip(matchings, values) if a}


def complete_block_width(records, a, b):
    # Rebuild A union B from scratch; cross A-only walls, never B walls.
    g = Graph('pair_union', {e: records[e] for e in a | b})
    adjacency = {f: [] for f in g.faces}
    for e in a - b:
        left, right = g.lr[e]
        adjacency[right].append((left, 1))
        adjacency[left].append((right, -1))
    height = {g.faces[0]: 0}
    queue = deque(height)
    while queue:
        f = queue.popleft()
        for h, step in adjacency[f]:
            expected = height[f] + step
            if h in height:
                assert height[h] == expected
            else:
                height[h] = expected
                queue.append(h)
    assert set(height) == set(g.faces), 'whole B-complement graph disconnected'
    return max(height.values()) - min(height.values())


M = {(i, j): frozenset((f'e{i}', f'f{j}'))
     for i, j in product(range(2), repeat=2)}


def analytical_retraction(bary, star=None):
    # Independent closed form for the square, or the square pyramid.
    s = min(bary.get(M[0, 1], F(0)), bary.get(M[1, 0], F(0)))
    result = {M[0, 0]: bary.get(M[0, 0], F(0)) + s,
              M[0, 1]: bary.get(M[0, 1], F(0)) - s,
              M[1, 0]: bary.get(M[1, 0], F(0)) - s,
              M[1, 1]: bary.get(M[1, 1], F(0)) + s}
    if star is not None:
        result[star] = bary.get(star, F(0))
    return clean(result)


def verify_graph(g, samples):
    for a, b in combinations(g.matchings, 2):
        assert complete_block_width(g.records, a, b) == g.distance[a, b]
        COUNTS['complete_block_pair_comparisons'] += 1
    for serial in range(samples):
        bary = random_bary(g.matchings)
        w = g.flow(bary)
        decoded = g.decode(w, critical=(serial % 31 == 0))
        if g.simplex(bary):
            assert decoded == bary
            COUNTS['random_true_simplex_recovery'] += 1
        if serial % 11 == 0:
            for ref in g.matchings:
                assert g.decode(w, reference=ref) == decoded
                COUNTS['reference_comparisons'] += 1
            for root in g.faces:
                assert g.decode(w, root=root) == decoded
                COUNTS['root_comparisons'] += 1
        for t in (F(0), F(1), F(1, 2), F(RNG.randrange(101), 100)):
            moved = homotopy(bary, decoded, t)
            assert all(m in g.matchings for m in moved)
            assert all(a >= 0 for a in moved.values()) and sum(moved.values()) == 1
            assert g.flow(moved) == w
            assert g.decode(g.flow(moved)) == decoded
            if t == 0:
                assert moved == bary
            if t == 1:
                assert moved == decoded
            if g.simplex(bary):
                assert moved == bary
            COUNTS['homotopy_checks'] += 1
        COUNTS['random_geometric_simplex_points'] += 1


def verify_all_cyclic_faces(g):
    max_faces = []
    for size in range(1, len(g.matchings) + 1):
        for face in combinations(g.matchings, size):
            if not g.simplex(face):
                continue
            COUNTS['cyclic_faces'] += 1
            if not any(g.simplex(face + (m,)) for m in g.matchings if m not in face):
                max_faces.append(face)
            for c in compositions(7, size):
                bary = {m: F(a, 7) for m, a in zip(face, c) if a}
                decoded = g.decode(g.flow(bary))
                assert decoded == bary
                assert homotopy(bary, decoded, F(13, 29)) == bary
                COUNTS['exhaustive_cyclic_face_recovery'] += 1
    return sorted(len(f) - 1 for f in max_faces)


def verify_deletions(mother):
    feasible = 0
    for bits in product((0, 1), repeat=len(mother.names)):
        support = {e for e, bit in zip(mother.names, bits) if bit}
        if not any(m <= support for m in mother.matchings):
            continue
        feasible += 1
        g = Graph('deleted_support', {e: mother.records[e] for e in support})
        for _ in range(9):
            bary = random_bary(g.matchings)
            w = g.flow(bary)
            result = g.decode(w)
            assert mother.decode(mother.flow(bary)) == result
            positive = {e for e in support if w[e] > 0}
            small = Graph('positive_support', {e: mother.records[e] for e in positive})
            sw = {e: w[e] for e in positive}
            assert small.decode(sw, reference=small.matchings[-1]) == result
            COUNTS['zero_deletion_comparisons'] += 1
    return feasible


def verify_analytical_fibres(g, samples=300):
    star = next(iter(set(g.matchings) - set(M.values())))
    for _ in range(samples):
        bary = random_bary(g.matchings)
        result = g.decode(g.flow(bary))
        assert result == analytical_retraction(bary, star)
        a = bary.get(M[0, 0], F(0)) + bary.get(M[0, 1], F(0))
        c = bary.get(M[0, 0], F(0)) + bary.get(M[1, 0], F(0))
        z = bary.get(star, F(0))
        lower, upper = max(F(0), a+c+z-1), min(a, c)
        assert lower <= upper
        for q in (F(0), F(1, 3), F(1), F(3, 4)):
            u = lower + q * (upper-lower)
            other = clean({M[0, 0]: u, M[0, 1]: a-u,
                           M[1, 0]: c-u, M[1, 1]: 1-z-a-c+u, star: z})
            assert min(other.values()) >= 0 and sum(other.values()) == 1
            assert g.flow(other) == g.flow(bary)
            assert g.decode(g.flow(other)) == result
            moved = homotopy(other, result, F(2, 5))
            assert moved.get(M[0, 0], F(0)) == F(3, 5)*u + F(2, 5)*upper
            COUNTS['convex_fibre_checks'] += 1
        COUNTS['closed_form_comparisons'] += 1


def verify_crossing_common_face(plain, twisted, core, samples=240):
    crossings = 0
    for e in ('sl', 'sr'):
        for f in ('tl', 'tr'):
            for en, _, a, b in plain.segments:
                if en != e:
                    continue
                for fn, _, c, d in twisted.segments:
                    if fn == f and proper_crossing(a, b, c, d):
                        crossings += 1
    assert crossings > 0, 'additional arcs of the two mother graphs must cross'
    nonidentity = 0
    for serial in range(samples):
        bary = ({M[0, 1]: F(1, 2), M[1, 0]: F(1, 2)}
                if serial == 0 else random_bary(core.matchings))
        expected = core.decode(core.flow(bary))
        assert expected == analytical_retraction(bary)
        assert plain.decode(plain.flow(bary)) == expected
        assert twisted.decode(twisted.flow(bary)) == expected
        if expected != bary:
            nonidentity += 1
        for t in (F(0), F(1, 7), F(2, 3), F(1)):
            a = homotopy(bary, plain.decode(plain.flow(bary)), t)
            b = homotopy(bary, twisted.decode(twisted.flow(bary)), t)
            assert a == b
            COUNTS['crossing_common_face_homotopies'] += 1
        COUNTS['crossing_common_face_decoders'] += 1
    assert nonidentity > 0
    return crossings, nonidentity


def main():
    core = Graph('two_cone_double_lens', CORE, check_embedding=True)
    plain = Graph('four_boundary_connected_graph', PLAIN, check_embedding=True)
    twisted = Graph('same_core_Dehn_twisted_connectors', TWISTED, check_embedding=True)
    assert len(core.matchings) == 4 and len(plain.matchings) == len(twisted.matchings) == 5
    # Distinct parallel classes: the two lens cycles contain different cones.
    assert core.cone_faces[0] != core.cone_faces[1]
    assert all(f != core.root for f in core.cone_faces)
    profiles = []
    for g, n in ((core, 400), (plain, 700), (twisted, 280)):
        verify_graph(g, n)
        maximal = verify_all_cyclic_faces(g)
        feasible = verify_deletions(g) if g is not twisted else None
        profiles.append({'name': g.name, 'matchings': len(g.matchings),
                         'regions': len(g.faces),
                         'maximal_cyclic_simplex_dimensions': maximal,
                         'feasible_deleted_supports': feasible})
    verify_analytical_fibres(plain)
    crossings, changed = verify_crossing_common_face(plain, twisted, core)
    bad = {M[0, 1]: F(1, 2), M[1, 0]: F(1, 2)}
    good = {M[0, 0]: F(1, 2), M[1, 1]: F(1, 2)}
    assert core.distance[M[0, 1], M[1, 0]] == 2
    assert core.decode(core.flow(bad)) == good
    print(json.dumps({'status': 'PASS', 'seed': 20261024,
                      'arithmetic': 'exact Fraction after rational PL construction',
                      'counts': dict(sorted(COUNTS.items())), 'graphs': profiles,
                      'extra_arc_transverse_crossings': crossings,
                      'nonidentity_common_face_samples': changed,
                      'analytic_decoder': 's=min(lambda01,lambda10); '
                        '(lambda00+s,lambda01-s,lambda10-s,lambda11+s,lambda_star)',
                      'fibre_interval': 'max(0,a+c+z-1) <= lambda00 <= min(a,c)',
                      'writes_files': False,
                      'limits': ['No proof of simultaneous 3D verticalisation.',
                                 'No numerical test proves CW product continuity.',
                                 'No import of author code, no network or source traversal.']},
                     ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
