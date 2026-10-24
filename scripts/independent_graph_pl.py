#!/usr/bin/env python3
"""Offline standard-library diagnostic; original calculation functions retained."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from math import floor
from random import Random
(W, H) = (8, 6)
HOLES = {'A': (1, 2), 'B': (6, 2), 'P': (3, 1), 'Q': (4, 4)}
TRI = []
for (x, y) in product(range(W), range(H)):
    if (x, y) in HOLES.values():
        continue
    TRI.extend((((x, y), (x + 1, y), (x + 1, y + 1)), ((x, y), (x + 1, y + 1), (x, y + 1))))

def edge(a, b):
    return tuple(sorted((a, b)))
INCIDENCE = defaultdict(list)
for (i, tri) in enumerate(TRI):
    for (a, b) in zip(tri, tri[1:] + tri[:1]):
        INCIDENCE[edge(a, b)].append(i)
EDGES = sorted(INCIDENCE)
VERTICES = sorted({v for e in EDGES for v in e})
ROOT = VERTICES[0]
ADJ = defaultdict(list)
for (a, b) in EDGES:
    ADJ[a].append(b)
    ADJ[b].append(a)
DUAL = defaultdict(list)
for (e, incident) in INCIDENCE.items():
    if len(incident) == 2:
        (a, b) = incident
        DUAL[a].append((b, e))
        DUAL[b].append((a, e))

def boundary_label(e):
    if len(INCIDENCE[e]) == 2:
        return None
    (a, b) = e
    for (name, (x, y)) in HOLES.items():
        if a[0] == b[0] and a[0] in (x, x + 1) and (min(a[1], b[1]) == y):
            return name
        if a[1] == b[1] and a[1] in (y, y + 1) and (min(a[0], b[0]) == x):
            return name
    return 'outer'
START_EDGE = edge((2, 2), (2, 3))
END_EDGE = edge((6, 2), (6, 3))
START = INCIDENCE[START_EDGE][0]
END = INCIDENCE[END_EDGE][0]
CENTERS = [tuple((F(sum((v[j] for v in t)), 3) for j in (0, 1))) for t in TRI]
RNG = Random(613021)
N = Counter()

def oriented(k, a, b):
    return k[edge(a, b)] * (1 if a < b else -1)

def simple_dual_path():
    stack = [START]
    visited = {START}
    choices = {i: RNG.sample(DUAL[i], len(DUAL[i])) for i in range(len(TRI))}
    while stack[-1] != END:
        v = stack[-1]
        while choices[v] and choices[v][-1][0] in visited:
            choices[v].pop()
        if not choices[v]:
            stack.pop()
            assert stack
            continue
        (w, _) = choices[v].pop()
        visited.add(w)
        stack.append(w)
    return tuple(stack)

def path_cocycle(path):
    k = {e: 0 for e in EDGES}
    start_center = (F(3, 2), F(5, 2))
    end_center = (F(13, 2), F(5, 2))
    moves = [(START_EDGE, start_center, CENTERS[path[0]])]
    for (a, b) in zip(path, path[1:]):
        shared = next((e for (w, e) in DUAL[a] if w == b))
        moves.append((shared, CENTERS[a], CENTERS[b]))
    moves.append((END_EDGE, CENTERS[path[-1]], end_center))
    for (e, p, q) in moves:
        (a, b) = e
        det = (b[0] - a[0]) * (q[1] - p[1]) - (b[1] - a[1]) * (q[0] - p[0])
        assert det
        k[e] += 1 if det > 0 else -1
    for tri in TRI:
        assert sum((oriented(k, a, b) for (a, b) in zip(tri, tri[1:] + tri[:1]))) == 0
    assert all((k[e] == 0 for e in EDGES if boundary_label(e) in ('P', 'Q', 'outer')))
    return k

def potential(difference):
    u = {ROOT: 0}
    stack = [ROOT]
    while stack:
        a = stack.pop()
        for b in ADJ[a]:
            value = u[a] + oriented(difference, a, b)
            if b in u:
                assert u[b] == value
            else:
                u[b] = value
                stack.append(b)
    return u
PATHS = []
while len(PATHS) < 18:
    p = simple_dual_path()
    if p not in PATHS:
        PATHS.append(p)
MAPS = [path_cocycle(p) for p in PATHS]
KREF = MAPS[0]
U = [potential({e: k[e] - KREF[e] for e in EDGES}) for k in MAPS]

def point(node, u, r):
    (e, integer) = node
    (a, b) = e
    delta = KREF[e] + u[b] - u[a]
    t = (r + integer - u[a]) / delta
    assert 0 < t < 1
    return tuple((F(a[j]) + t * (b[j] - a[j]) for j in (0, 1)))

def reduced_word(points):
    word = []
    rays = [(name, F(x) + F(1, 2) + F(1, 10007), F(y)) for (name, (x, y)) in HOLES.items()]
    for (p, q) in zip(points, points[1:]):
        crossings = []
        for (name, xx, top) in rays:
            if p[0] < xx <= q[0] or q[0] < xx <= p[0]:
                t = (xx - p[0]) / (q[0] - p[0])
                yy = p[1] + t * (q[1] - p[1])
                if 0 < yy < top:
                    crossings.append((t, name, 1 if q[0] > p[0] else -1))
        for (_, name, sign) in sorted(crossings):
            if word and word[-1] == (name, -sign):
                word.pop()
            else:
                word.append((name, sign))
    while word and word[0][0] == 'A':
        word.pop(0)
    while word and word[-1][0] == 'B':
        word.pop()
    return tuple(word)

def extract(u, r):
    adjacency = defaultdict(list)
    for tri in TRI:
        (a, b, c) = tri
        integral = {a: 0, b: oriented(KREF, a, b), c: oriented(KREF, a, c)}
        heights = {v: integral[v] + u[v] for v in tri}
        (low, high) = (min(heights.values()), max(heights.values()))
        assert all(((x - r).denominator != 1 for x in heights.values()))
        for integer in range(floor(low - r) - 1, floor(high - r) + 2):
            level = r + integer
            hits = []
            for (v, w) in zip(tri, tri[1:] + tri[:1]):
                if min(heights[v], heights[w]) < level < max(heights[v], heights[w]):
                    e = edge(v, w)
                    hits.append((e, integer - integral[e[0]]))
            assert len(hits) in (0, 2)
            if hits:
                (v, w) = hits
                adjacency[v].append(w)
                adjacency[w].append(v)
    unseen = set(adjacency)
    components = []
    while unseen:
        first = next(iter(unseen))
        (component, stack) = ({first}, [first])
        unseen.remove(first)
        while stack:
            v = stack.pop()
            for w in adjacency[v]:
                if w not in component:
                    component.add(w)
                    unseen.remove(w)
                    stack.append(w)
        components.append(component)
    (arcs, circles) = ([], [])
    for comp in components:
        ends = [v for v in comp if len(adjacency[v]) == 1]
        assert all((len(adjacency[v]) in (1, 2) for v in comp))
        if ends:
            assert len(ends) == 2
            assert {boundary_label(v[0]) for v in ends} == {'A', 'B'}
            start = next((v for v in ends if boundary_label(v[0]) == 'A'))
            (ordered, previous, current) = ([], None, start)
            while True:
                ordered.append(current)
                nxt = [w for w in adjacency[current] if w != previous]
                if not nxt:
                    break
                assert len(nxt) == 1
                (previous, current) = (current, nxt[0])
            assert set(ordered) == comp
            arcs.append(ordered)
        else:
            circles.append(comp)
    assert len(arcs) == 1
    all_current = {e: 0 for e in EDGES}
    retained = {e: 0 for e in EDGES}
    for node in adjacency:
        (e, _) = node
        sign = 1 if KREF[e] + u[e[1]] - u[e[0]] > 0 else -1
        all_current[e] += sign
    for node in arcs[0]:
        (e, _) = node
        sign = 1 if KREF[e] + u[e[1]] - u[e[0]] > 0 else -1
        retained[e] += sign
    pre = {v: floor(u[v] - r) - floor(u[ROOT] - r) for v in VERTICES}
    assert all((all_current[e] == KREF[e] + pre[e[1]] - pre[e[0]] for e in EDGES))
    reread = potential({e: retained[e] - KREF[e] for e in EDGES})
    marks = []
    old_marks = []
    for name in ('P', 'Q'):
        boundary_vertices = {v for e in EDGES if boundary_label(e) == name for v in e}
        assert len({reread[v] for v in boundary_vertices}) == 1
        assert len({pre[v] for v in boundary_vertices}) == 1
        marks.append(reread[next(iter(boundary_vertices))])
        old_marks.append(pre[next(iter(boundary_vertices))])
    key = (reduced_word([point(v, u, r) for v in arcs[0]]), tuple(marks))
    return (key, len(circles), tuple(old_marks), tuple(marks))

def distribution(coefficients, collect=False):
    u = {v: sum((a * U[i][v] for (i, a) in coefficients.items())) for v in VERTICES}
    breaks = sorted({F(0), F(1)} | {x - floor(x) for x in u.values()})
    out = defaultdict(F)
    for (lo, hi) in zip(breaks, breaks[1:]):
        if lo == hi:
            continue
        r = (2 * lo + hi) / 3
        (key, circle_count, old, new) = extract(u, r)
        out[key] += hi - lo
        if collect:
            N['regular_PL_levels'] += 1
            N['circle_components_deleted'] += circle_count
            if old != new:
                N['old_phase_wrong_at_marks'] += 1
                global WITNESS
                if WITNESS is None:
                    WITNESS = (tuple(sorted(coefficients.items())), r, circle_count, old, new)
    assert sum(out.values()) == 1
    return (dict(out), u)
WITNESS = None

if __name__ == '__main__':
    import contextlib
    import io
    import json
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        states = set()
        for i in range(len(U)):
            (d, _) = distribution({i: F(1)}, True)
            assert len(d) == 1
            states.update(d)
            N['input_band_maps'] += 1
        for (i, j) in combinations(range(len(U)), 2):
            for a in (F(1, 3), F(1, 2), F(2, 3)):
                (d, _) = distribution({i: a, j: 1 - a}, True)
                states.update(d)
                N['pair_coefficient_points'] += 1
        for (i, j, k) in combinations(range(9), 3):
            (d, u0) = distribution({i: F(1, 3), j: F(1, 3), k: F(1, 3)}, True)
            states.update(d)
            critical = len({x - floor(x) for x in u0.values()})
            for epsilon in (F(1, 60), F(1, 600)):
                perturbed = {i: F(1, 3) + epsilon, j: F(1, 3) - epsilon, k: F(1, 3)}
                (de, ue) = distribution(perturbed)
                delta = max((abs(ue[v] - u0[v]) for v in VERTICES))
                l1 = sum((abs(de.get(s, 0) - d.get(s, 0)) for s in set(de) | set(d)))
                assert l1 <= 4 * critical * delta
                N['collision_continuity_checks'] += 1
            N['triple_coefficient_points'] += 1
        assert N['circle_components_deleted'] > 0
        assert N['old_phase_wrong_at_marks'] > 0
        N['finite_reduced_states_observed'] = len(states)
        for (key, value) in sorted(N.items()):
            print(f'{key}: {value}')
        print('Circle-deletion witness: (coefficients, phase, circles, old(P,Q), reread(P,Q))')
        print(WITNESS)
        print('PASS: deleting circles can change the relative potential; reread distributions pass the tested collisions.')
    print(json.dumps({'scope': 'Finite diagnostics; not a topology certificate.', 'output': captured.getvalue().splitlines()}, indent=2, sort_keys=True))
