#!/usr/bin/env python3
# Finite exact diagnostic for Part 13 of the proof; standard library only; prints a deterministic report and writes no files.
from fractions import Fraction as F
from functools import cmp_to_key, lru_cache
from collections import defaultdict, deque
import json
from itertools import product, combinations
N = 12
positive = {0, 1, 2, 6, 7, 8}
U = ((0, 5), (1, 4), (2, 3), (6, 11), (7, 10), (8, 9))
W = ((0, 11), (1, 10), (2, 9), (3, 8), (4, 7), (5, 6))
expected = (U, ((0, 11), (1, 4), (2, 3), (5, 6), (7, 10), (8, 9)), ((0, 11), (1, 10), (2, 3), (4, 7), (5, 6), (8, 9)), W)

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

def strict_cross(e, f):
    (a, b) = sorted(e)
    (c, d) = sorted(f)
    return a < c < b < d or c < a < d < b

def norm(m):
    return tuple(sorted((tuple(sorted(e)) for e in m)))

@lru_cache(None)
def matchings(v):
    if not v:
        return ((),)
    a = v[0]
    out = []
    for k in range(1, len(v), 2):
        b = v[k]
        if (a in positive) == (b in positive):
            continue
        for x in matchings(v[1:k]):
            for y in matchings(v[k + 1:]):
                out.append(((a, b),) + x + y)
    return tuple(out)

def main():
    pts = {i: (F(i), F(i * i)) for i in range(N)}
    raw = [(b, a, c) if a in positive else (a, b, c) for (c, mm) in [('u', U), ('w', W)] for (a, b) in mm]
    cuts = [[(F(0), a), (F(1), b)] for (a, b, c) in raw]
    intersection_pairs = []
    vertex_names = {i: str(i + 1) for i in range(N)}
    for (i, (a, b, c)) in enumerate(raw):
        for (j, (d, e, f)) in enumerate(raw[:i]):
            if c == f or {a, b} & {d, e}:
                continue
            v = sub(pts[b], pts[a])
            w = sub(pts[e], pts[d])
            den = cross(v, w)
            if not den:
                continue
            t = cross(sub(pts[d], pts[a]), w) / den
            s = cross(sub(pts[d], pts[a]), v) / den
            if 0 < t < 1 and 0 < s < 1:
                x = max(pts) + 1
                pt = (pts[a][0] + t * v[0], pts[a][1] + t * v[1])
                assert pt not in pts.values(), 'triple intersection'
                pts[x] = pt
                vertex_names[x] = f'U{j + 1}W{i - 5}'
                cuts[i].append((t, x))
                cuts[j].append((s, x))
                intersection_pairs.append((i, j))
    edges = []
    for ((a, b, c), cc) in zip(raw, cuts):
        vv = [x for (t, x) in sorted(cc)]
        edges.extend(((x, y, c) for (x, y) in zip(vv, vv[1:])))
    rot = defaultdict(list)
    for (i, (a, b, c)) in enumerate(edges):
        rot[a].append(2 * i)
        rot[b].append(2 * i + 1)

    def org(h):
        return edges[h // 2][h % 2]

    def half(v):
        return 0 if v[1] > 0 or (v[1] == 0 and v[0] > 0) else 1
    for (v, hh) in rot.items():

        def cmp(h, k):
            x = sub(pts[org(h ^ 1)], pts[v])
            y = sub(pts[org(k ^ 1)], pts[v])
            if half(x) != half(y):
                return -1 if half(x) < half(y) else 1
            z = cross(x, y)
            assert z or h == k, 'overlapping rays'
            return -1 if z > 0 else 1 if z < 0 else 0
        hh.sort(key=cmp_to_key(cmp))
    prev = {hs[j]: hs[j - 1] for hs in rot.values() for j in range(len(hs))}
    nxt = {h: prev[h ^ 1] for h in range(2 * len(edges))}
    faces = []
    face = {}
    for h in nxt:
        if h in face:
            continue
        cyc = []
        x = h
        while x not in face:
            face[x] = len(faces)
            cyc.append(x)
            x = nxt[x]
        assert x == h
        faces.append(cyc)
    assert len(pts) - len(edges) + len(faces) == 2
    actual = [[org(h) for h in hs if org(h) < N] for hs in faces]
    outer = next((i for (i, a) in enumerate(actual) if len(a) == N))
    inner_multi = sorted((tuple(sorted(a)) for (i, a) in enumerate(actual) if i != outer and len(a) >= 2))
    assert inner_multi == [(0, 11), (2, 3), (5, 6), (8, 9)], inner_multi
    assert all((len(a) <= 2 for (i, a) in enumerate(actual) if i != outer))
    for (i, a) in enumerate(actual):
        if i == outer or len(a) != 2:
            continue
        aa = set(a)
        assert any((set(edges[h // 2][:2]) == aa for h in faces[i]))
        assert tuple(sorted(a)) in norm(U) or tuple(sorted(a)) in norm(W)
        assert (a[0] - a[1]) % N in (1, N - 1)
    adj = defaultdict(list)
    for (i, (a, b, c)) in enumerate(edges):
        (l, r) = (face[2 * i], face[2 * i + 1])
        d = 1 if c == 'u' else -1
        adj[r].append((l, d))
        adj[l].append((r, -d))
    H = {outer: 0}
    q = deque([outer])
    while q:
        f = q.popleft()
        for (g, d) in adj[f]:
            val = H[f] + d
            if g in H:
                assert H[g] == val
            else:
                H[g] = val
                q.append(g)
    assert len(H) == len(faces)
    assert max(H.values()) - min(H.values()) == 3
    mm = tuple((norm(m) for m in matchings(tuple(range(N)))))
    assert set(mm) == {norm(m) for m in expected} and len(mm) == 4
    graph = []
    witnesses = {}
    for (i, a) in enumerate(expected):
        for (j, b) in enumerate(expected[:i]):
            cc = [(e, f) for e in a for f in b if strict_cross(e, f)]
            if not cc:
                graph.append((j, i))
            else:
                witnesses[f'{j}-{i}'] = [[x + 1 for x in cc[0][0]], [x + 1 for x in cc[0][1]]]
    assert graph == [(0, 1), (1, 2), (2, 3)], graph
    apices = [i for i in range(4) if all((i == j or tuple(sorted((i, j))) in graph for j in range(4)))]
    assert not apices
    name_to_vertex = {name: v for (v, name) in vertex_names.items()}
    vm = {i: (i + 6) % 12 for i in range(12)}
    for (v, name) in vertex_names.items():
        if v < 12:
            continue
        (ii, jj) = name[1:].split('W')
        (ii, jj) = (int(ii), int(jj))
        vm[v] = name_to_vertex[f'U{(ii + 2) % 6 + 1}W{7 - jj}']
    edge_lookup = {(a, b, c): i for (i, (a, b, c)) in enumerate(edges)}
    hm = {}
    for (i, (a, b, c)) in enumerate(edges):
        j = edge_lookup[vm[a], vm[b], c]
        hm[2 * i] = 2 * j
        hm[2 * i + 1] = 2 * j + 1

    def cyclic_equal(a, b):
        return len(a) == len(b) and any((a == b[k:] + b[:k] for k in range(len(b))))
    for (v, hs) in rot.items():
        assert cyclic_equal([hm[h] for h in hs], rot[vm[v]])
    fm = {}
    for (i, hs) in enumerate(faces):
        hh = [hm[h] for h in hs]
        fm[i] = next((j for (j, kk) in enumerate(faces) if cyclic_equal(hh, kk)))
    assert all((fm[fm[i]] == i and H[fm[i]] == H[i] for i in fm))
    fixed = [i for i in fm if fm[i] == i]
    assert len(fixed) == 2 and outer in fixed and any((H[i] == min(H.values()) for i in fixed))
    for m in expected:
        assert norm(m) == norm([((a + 6) % 12, (b + 6) % 12) for (a, b) in m])
    assert norm(U) == norm([((a + 6) % 12, (b + 6) % 12) for (a, b) in U])
    assert norm(W) == norm([((a + 6) % 12, (b + 6) % 12) for (a, b) in W])
    inner = [frozenset(range(a, 5 - a)) for a in range(3)]
    all_edges = frozenset(range(6))

    def disk_intervals(bits):
        return [all_edges - x if bit else x for (x, bit) in zip(inner, bits)]

    def laminar(ss):
        return all((not a & b or a <= b or b <= a for (a, b) in combinations(ss, 2)))
    astates = [bits for bits in product((0, 1), repeat=3) if laminar(disk_intervals(bits))]
    assert astates == [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1)]
    aedges = [(i, j) for (i, j) in combinations(range(4), 2) if laminar(disk_intervals(astates[i]) + disk_intervals(astates[j]))]
    assert aedges == [(0, 1), (1, 2), (2, 3)]
    out = {'status': 'PASS — exact finite certificate; topological exhaustion in manuscript', 'link': 'balanced 12-component regular Hopf-fibre link', 'sign_word': '+++---+++---', 'inside_U': [[a + 1, b + 1] for (a, b) in U], 'inside_W': [[a + 1, b + 1] for (a, b) in W], 'crossings': len(intersection_pairs), 'faces': len(faces), 'outer_actual_order': [x + 1 for x in actual[outer]], 'interior_faces_with_two_actual_corners': [[a + 1, b + 1] for (a, b) in inner_multi], 'interior_single_actual_corners': sorted((a[0] + 1 for (i, a) in enumerate(actual) if i != outer and len(a) == 1)), 'input_potential_by_face': {str(i): H[i] for i in range(len(faces))}, 'face_boundary_certificate': [{'face': i, 'height': H[i], 'boundary': [vertex_names[org(h)] for h in hs]} for (i, hs) in enumerate(faces)], 'input_cyclic_range': 3, 'full_geometric_interval_matchings_outside': [[[a + 1, b + 1] for (a, b) in m] for m in expected], 'interval_edges': graph, 'nonedge_single_crossing_witnesses': witnesses, 'apices': apices, 'half_turn_quotient': {'ribbon_automorphism': True, 'fixed_faces': fixed, 'actual_holes': 6, 'crossings': len(intersection_pairs) // 2, 'faces': (len(faces) + len(fixed)) // 2, 'sign_word': '+++---', 'two_fixed_face_marks_retained': True, 'all_four_interval_vertices_invariant': True, 'annular_states': astates, 'annular_interval_edges': aedges, 'realisation': 'balanced T(12,18) after assigning cone orders 2,3'}, 'not_claimed': ['N1 failure for X', 'noncontractibility', 'failure in either resonant test link']}
    print(json.dumps(out, ensure_ascii=False, indent=2))
if __name__ == '__main__':
    main()
