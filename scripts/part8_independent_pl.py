#!/usr/bin/env python3
# Finite exact diagnostic for Part 8 of the proof; standard library only; prints a deterministic report and writes no files.
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations
from math import atan2, floor, pi
import json

def frac(x):
    return x - floor(x)

class Pattern:

    def __init__(self, signs):
        self.signs = signs
        (nx, ny) = (8, 6)
        hole_cells = [(1, 1), (5, 1), (3, 4), (6, 4)][:len(signs)]
        self.points = [(x, y) for y in range(ny + 1) for x in range(nx + 1)]
        ids = {p: i for (i, p) in enumerate(self.points)}
        self.triangles = []
        for x in range(nx):
            for y in range(ny):
                if (x, y) in hole_cells:
                    continue
                (a, b, c, d) = [ids[p] for p in [(x, y), (x + 1, y), (x + 1, y + 1), (x, y + 1)]]
                self.triangles += [(a, b, c), (a, c, d)]
        self.boundaries = []
        for (x, y) in hole_cells:
            self.boundaries.append([ids[p] for p in [(x, y), (x + 1, y), (x + 1, y + 1), (x, y + 1)]])
        outer = [(x, 0) for x in range(nx + 1)]
        outer += [(nx, y) for y in range(1, ny + 1)]
        outer += [(x, ny) for x in range(nx - 1, -1, -1)]
        outer += [(0, y) for y in range(ny - 1, 0, -1)]
        self.boundaries.append([ids[p] for p in outer])
        self.outer = len(signs)
        self.edge_boundary = {}
        for (label, loop) in enumerate(self.boundaries):
            for (a, b) in zip(loop, loop[1:] + loop[:1]):
                self.edge_boundary[tuple(sorted((a, b)))] = label
        centres = [(x + 0.5, y + 0.5) for (x, y) in hole_cells]
        angles = [[atan2(y - cy, x - cx) / (2 * pi) for (cx, cy) in centres] for (x, y) in self.points]
        self.base = [sum((F(round(v * 10 ** 6), 10 ** 6) * s for (v, s) in zip(row, signs))) for row in angles]
        self.cocycle = {}
        for tri in self.triangles:
            for (a, b) in combinations(tri, 2):
                (a, b) = sorted((a, b))
                self.cocycle[a, b] = -sum((s * floor(vb - va + 0.5) for (va, vb, s) in zip(angles[a], angles[b], signs)))
        for (a, b, c) in self.triangles:
            assert self.edge(a, b) + self.edge(b, c) + self.edge(c, a) == 0
        for (label, loop) in enumerate(self.boundaries):
            degree = sum((self.edge(a, b) for (a, b) in zip(loop, loop[1:] + loop[:1])))
            assert degree == (sum(signs) if label == self.outer else signs[label])

    def edge(self, a, b):
        return self.cocycle[a, b] if a < b else -self.cocycle[b, a]

    def potential(self, seed, amplitude):
        u = [F((i * 37 + seed * 19) % 11 - 5, 3) for i in range(len(self.points))]
        for (label, loop) in enumerate(self.boundaries):
            degree = sum(self.signs) if label == self.outer else self.signs[label]
            winding = 0
            for (k, v) in enumerate(loop):
                if k:
                    winding += self.edge(loop[k - 1], v)
                t = F(k, len(loop))
                target = degree * t
                if label == self.outer:
                    target += amplitude * (2 * t if t <= F(1, 2) else 2 - 2 * t)
                u[v] = target - self.base[v] - winding
        return u

    def level(self, u, phase):
        values = [a + b for (a, b) in zip(self.base, u)]
        assert all((frac(x) != phase for x in values))
        graph = defaultdict(list)
        for tri in self.triangles:
            (a, b, c) = tri
            v = {a: values[a], b: values[b] + self.edge(a, b), c: values[c] + self.edge(a, c)}
            for integer in range(floor(min(v.values()) - phase) + 1, floor(max(v.values()) - phase) + 1):
                height = phase + integer
                if not min(v.values()) < height < max(v.values()):
                    continue
                crossings = []
                for (x, y) in ((a, b), (b, c), (c, a)):
                    if min(v[x], v[y]) < height < max(v[x], v[y]):
                        (low, high) = sorted((x, y))
                        shift = v[low] - values[low]
                        assert shift.denominator == 1
                        crossings.append((low, high, integer - int(shift)))
                assert len(crossings) == 2
                (x, y) = crossings
                graph[x].append(y)
                graph[y].append(x)
        assert all((len(neighbours) in (1, 2) for neighbours in graph.values()))
        (seen, arcs, circles) = (set(), [], 0)
        for start in graph:
            if start in seen:
                continue
            (stack, part) = ([start], set())
            while stack:
                vertex = stack.pop()
                if vertex in part:
                    continue
                part.add(vertex)
                stack.extend(graph[vertex])
            seen |= part
            ends = [v for v in part if len(graph[v]) == 1]
            if not ends:
                circles += 1
                continue
            assert len(ends) == 2
            labels = tuple(sorted((self.edge_boundary[v[:2]] for v in ends)))
            arcs.append(labels)
        actual_uses = Counter((i for arc in arcs for i in arc if i != self.outer))
        assert actual_uses == Counter(range(self.outer))
        (closed_caps, retained) = (0, [])
        for (a, b) in arcs:
            if a == b == self.outer:
                closed_caps += 1
                continue
            assert a != b
            if b != self.outer:
                assert self.signs[a] == -self.signs[b]
            retained.append((a, b))
        tether_sign = sum((self.signs[a] for (a, b) in retained if b == self.outer))
        assert tether_sign == sum(self.signs)
        return (tuple(sorted(retained)), circles, closed_caps)

    def average(self, u):
        critical = sorted({F(0), F(1)} | {frac(a + b) for (a, b) in zip(self.base, u)})
        (weights, diagnostics) = (defaultdict(F), Counter())
        for (a, b) in zip(critical, critical[1:]):
            if a == b:
                continue
            (signature, circles, caps) = self.level(u, (a + b) / 2)
            weights[signature] += b - a
            diagnostics['regular_intervals'] += 1
            diagnostics['pattern_circles_deleted'] += circles
            diagnostics['two_fibre_closed_components_deleted'] += caps
        assert sum(weights.values()) == 1
        return (weights, diagnostics)

def blend(u, v, s):
    return [(1 - s) * a + s * b for (a, b) in zip(u, v)]

def main():
    output = []
    for signs in ((1, 1, -1), (1, -1), (1, -1, 1, -1)):
        p = Pattern(signs)
        end_amplitude = F(-2) if not sum(signs) else F(3)
        (u, v) = (p.potential(1, F(2)), p.potential(7, end_amplitude))
        stats = Counter()
        sample_parameters = [F(k, 8) for k in range(9)]
        collisions = set()
        for (i, j) in combinations(range(len(u)), 2):
            velocity = v[i] - u[i] - (v[j] - u[j])
            if not velocity:
                continue
            initial = p.base[i] + u[i] - (p.base[j] + u[j])
            for integer in range(-3, 4):
                s = (integer - initial) / velocity
                if F(1, 5) < s < F(4, 5):
                    collisions.add(s)
        chosen = sorted(collisions)[::max(1, len(collisions) // 3)][:3]
        if not sum(signs):
            chosen.append(F(1, 2))
        samples = {}
        for s in sample_parameters + chosen:
            (w, d) = p.average(blend(u, v, s))
            stats.update(d)
            samples[s] = w
        velocity_bound = max((abs(b - a) for (a, b) in zip(u, v)))
        checks = 0
        for centre in chosen:
            reference = samples[centre]
            for denominator in (1000, 10000):
                for sign in (-1, 1):
                    step = F(sign, denominator)
                    (weights, d) = p.average(blend(u, v, centre + step))
                    stats.update(d)
                    keys = set(reference) | set(weights)
                    l1 = sum((abs(reference.get(k, 0) - weights.get(k, 0)) for k in keys))
                    bound = 2 * len(u) * velocity_bound * abs(step)
                    assert l1 <= bound
                    checks += 1
        assert stats['two_fibre_closed_components_deleted'] > 0
        output.append(dict(signs=signs, vertices=len(u), triangles=len(p.triangles), exact_collision_continuity_checks=checks, includes_constant_companion_profile=not sum(signs), **stats))
    print(json.dumps(output, ensure_ascii=False, indent=2))
    print('PASS: exact PL tracing, closed-cap deletion and pairing-average continuity')
    print('LIMIT: pairing signatures do not classify ordinary arc isotopy.')
if __name__ == '__main__':
    main()
