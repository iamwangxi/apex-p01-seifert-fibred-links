#!/usr/bin/env python3
# Finite exact diagnostic for Part 12 of the proof; standard library only; prints a deterministic report and writes no files.
from itertools import product
from itertools import combinations
from functools import lru_cache
from pathlib import Path
import json
import random
BASE = Path(__file__).resolve().parent

def packet(w):
    q = len(w)
    return (list(range(q)) + list(range(q - 1, -1, -1)), list(w) + [-s for s in w[::-1]])

def pants(w):
    (labels, signs) = packet(w)
    (q, n) = (len(w), 2 * len(w))
    out = []
    for a in range(n):
        u = {a, (a + q) % n}
        if signs[a] != 1 or signs[(a + q) % n] != -1:
            continue
        if any((j not in u and signs[(2 * a - j) % n] == signs[j] for j in range(n))):
            continue
        mm = [(j, (2 * a - j) % n) for j in range(n) if j not in u and j < (2 * a - j) % n]
        assert len(mm) == q - 1
        assert all((sum((x < i < y for i in u)) == 1 for (x, y) in mm))
        out.append((mm, u))
    return out

def chambers(w, side):
    (q, n) = (len(w), 2 * len(w))
    out = []
    if w[0] == -side:
        out.append(('L', {0}, [(n - 1, 0)]))
    for j in range(q - 1):
        if (w[j], w[j + 1]) == (side, -side):
            out.append((str(j), {j, j + 1}, [(j, j + 1), (n - 2 - j, n - 1 - j)]))
    if w[-1] == side:
        out.append(('R', {q - 1}, [(q - 1, q)]))
    seen = set()
    for (_, pieces, _) in out:
        assert not seen & pieces
        seen |= pieces
    return out

def compose(mm, u, caps):
    graph = {}

    def add(a, b, tag):
        graph.setdefault(a, []).append((b, tag))
        graph.setdefault(b, []).append((a, tag))
    for (a, b) in mm:
        add(('o', a), ('o', b), None)
    for j in u:
        add(('o', j), ('a', j), None)
    for (j, (a, b)) in enumerate(caps):
        add(('o', a), ('o', b), j)
    ends = sorted((x for x in graph if len(graph[x]) == 1))
    assert all((len(a) in (1, 2) for a in graph.values()))
    (seen, paths) = (set(), [])
    for start in ends:
        if start in seen:
            continue
        (prev, cur, tags) = (None, start, [])
        while True:
            seen.add(cur)
            if prev is not None and len(graph[cur]) == 1:
                paths.append((start, cur, tuple(tags)))
                break
            (nxt, tag) = next(((a, t) for (a, t) in graph[cur] if a != prev))
            if tag is not None:
                tags.append(tag)
            (prev, cur) = (cur, nxt)
    return paths

def bad(paths, caps, u, n):
    out = []
    for (a, b, tags) in paths:
        if a[0] != 'o' or b[0] != 'o':
            continue
        (x, y) = sorted((a[1], b[1]))
        count = 0
        for mark in u:
            bit = x < mark < y
            for tag in tags:
                (lo, hi) = caps[tag]
                inside = lo < mark < hi if lo < hi else mark > lo or mark < hi
                bit ^= inside
            count += bit
        if count in (0, len(u)):
            out.append((x, y))
    return out

def actual_reachable(path_lists, labels, available):
    adj = {j: set() for j in available}
    seen = set()
    for paths in path_lists:
        for (a, b, _) in paths:
            if a[0] == b[0] == 'o':
                (x, y) = (labels[a[1]], labels[b[1]])
                assert x in adj and y in adj
                adj[x].add(y)
                adj[y].add(x)
            elif a[0] == 'o':
                seen.add(labels[a[1]])
            elif b[0] == 'o':
                seen.add(labels[b[1]])
    todo = list(seen)
    while todo:
        j = todo.pop()
        for k in adj[j] - seen:
            seen.add(k)
            todo.append(k)
    return seen

def audit(w, diagrams, seed_end):
    (q, n) = (len(w), 2 * len(w))
    (labels, _) = packet(w)
    side = -w[0] if seed_end == 'L' else w[-1]
    regs = chambers(w, side)
    seed = next((j for (j, r) in enumerate(regs) if r[0] == seed_end))
    by_cap = {frozenset(cap): j for (j, r) in enumerate(regs) for cap in r[2]}
    (states, terminal) = ({}, [])

    def visit(sel):
        if sel in states:
            return
        caps = [cap for (j, r) in enumerate(regs) if j in sel for cap in r[2]]
        removed = set().union(*(regs[j][1] for j in sel))
        (path_lists, enabled) = ([], set())
        for (mm, u) in diagrams:
            paths = compose(mm, u, caps)
            path_lists.append(paths)
            for (x, y) in bad(paths, caps, u, n):
                key = frozenset((x, y))
                assert key in by_cap, ('missing global chamber', w, diagrams, sel, (x, y))
                j = by_cap[key]
                assert j not in sel
                assert not regs[j][1] & removed
                enabled.add(j)
        states[sel] = enabled
        if not enabled:
            kept = actual_reachable(path_lists, labels, set(range(q)) - removed)
            assert len(kept) < q
            terminal.append((sel, tuple(sorted(kept))))
        for j in enabled:
            visit(sel | {j})
    visit(frozenset({seed}))
    assert len(set(terminal)) == 1, ('nonconfluent', w, diagrams, terminal)
    for (a, ea) in states.items():
        for (b, eb) in states.items():
            if a <= b:
                assert ea - b <= eb
    return (len(states), len(terminal[0][0]))

def packet_k(k, w):
    q = len(w)
    (labels, signs) = ([], [])
    for r in range(2 * k):
        order = range(q) if r % 2 == 0 else range(q - 1, -1, -1)
        labels.extend(order)
        signs.extend((w[j] * (-1 if r % 2 else 1) for j in order))
    return (labels, signs)

def chambers_k(k, w, side):
    q = len(w)
    n = 2 * k * q
    out = []
    if w[0] == -side:
        out.append(('L', {0}, [(r * q + q - 1, (r + 1) * q % n) for r in range(1, 2 * k, 2)]))
    for j in range(q - 1):
        if (w[j], w[j + 1]) == (side, -side):
            caps = []
            for r in range(2 * k):
                aa = [r * q + (x if r % 2 == 0 else q - 1 - x) for x in (j, j + 1)]
                caps.append(tuple(sorted(aa)))
            out.append((str(j), {j, j + 1}, caps))
    if w[-1] == side:
        out.append(('R', {q - 1}, [(r * q + q - 1, (r + 1) * q) for r in range(0, 2 * k, 2)]))
    return out

def local_four_hole_pool(k, w, rng):
    (labels, signs) = packet_k(k, w)
    n = len(labels)
    pool = []
    for nt in (0, 2, 4):
        if nt > n:
            continue
        choices = list(combinations(range(n), nt))
        rng.shuffle(choices)
        found = 0
        for uu in choices:
            if sum((signs[j] for j in uu)):
                continue
            if nt == 4:
                extras = [()]
            elif nt == 2:
                extras = [(j + 0.5, j + 0.5) for j in range(n)]
            else:
                extras = [(a + 0.5, a + 0.5, b + 0.5, b + 0.5) for (a, b) in combinations(range(n), 2)]
            rng.shuffle(extras)
            for extra in extras:
                marks = list(uu) + list(extra)

                @lru_cache(None)
                def rec(tup):
                    if not tup:
                        return ((),)
                    a = tup[0]
                    out = []
                    for z in range(1, len(tup), 2):
                        b = tup[z]
                        if signs[a] == signs[b]:
                            continue
                        holes = sum((a < i < b for i in marks))
                        if not 0 < holes < 4:
                            continue
                        for x in rec(tup[1:z]):
                            for y in rec(tup[z + 1:]):
                                out.append(((a, b),) + x + y)
                                if len(out) >= 48:
                                    return tuple(out)
                    return tuple(out)
                for mm in rec(tuple((j for j in range(n) if j not in uu))):
                    pool.append(dict(k=k, mm=mm, u=set(uu), marks=marks, labels=labels, tethers=nt))
                    found += 1
                    if found >= 48:
                        break
                if found >= 48:
                    break
            if found >= 48:
                break
    return pool

def converted_paths(paths, labels):

    def conv(a):
        return ('o', labels[a[1]]) if a[0] == 'o' else a
    return [(conv(a), conv(b), tags) for (a, b, tags) in paths]

def audit_general(w, diagrams, seed_end):
    q = len(w)
    side = -w[0] if seed_end == 'L' else w[-1]
    ref = chambers_k(1, w, side)
    all_regs = [chambers_k(d['k'], w, side) for d in diagrams]
    assert all(([(r[0], r[1]) for r in rr] == [(r[0], r[1]) for r in ref] for rr in all_regs))
    seed = next((j for (j, r) in enumerate(ref) if r[0] == seed_end))
    states = {}
    terminal = []

    def visit(sel):
        if sel in states:
            return
        removed = set().union(*(ref[j][1] for j in sel))
        enabled = set()
        converted = []
        for (d, regs) in zip(diagrams, all_regs):
            caps = [cap for (j, r) in enumerate(regs) if j in sel for cap in r[2]]
            bycap = {frozenset(cap): j for (j, r) in enumerate(regs) for cap in r[2]}
            paths = compose(d['mm'], d['u'], caps)
            assert {a[1] for p in paths for a in p[:2] if a[0] == 'a'} == d['u']
            converted.append(converted_paths(paths, d['labels']))
            for (x, y) in bad(paths, caps, d['marks'], 2 * d['k'] * q):
                key = frozenset((x, y))
                assert key in bycap, ('unclassified global repair', w, d, sel, (x, y))
                j = bycap[key]
                assert j not in sel and (not ref[j][1] & removed)
                enabled.add(j)
        states[sel] = enabled
        if not enabled:
            kept = actual_reachable(converted, list(range(q)), set(range(q)) - removed)
            assert len(kept) < q
            terminal.append((sel, tuple(sorted(kept))))
        for j in enabled:
            visit(sel | {j})
    visit(frozenset({seed}))
    assert len(set(terminal)) == 1, ('nonconfluent global closure', w, terminal)
    for (a, ea) in states.items():
        for (b, eb) in states.items():
            if a <= b:
                assert ea - b <= eb
    return (len(states), len(terminal[0][0]))

def wider_checks():
    rng = random.Random(60662026)
    inputs = audits = states = zero_tether_ports = mixed = 0
    all_pools = local_options = 0
    for q in range(1, 6):
        for tail in product((1, -1), repeat=q - 1):
            w = (1,) + tail
            pools = [local_four_hole_pool(k, w, rng) for k in (1, 2)]
            all_pools += 2
            local_options += sum(map(len, pools))
            available = [p for p in pools if p]
            if not available:
                continue
            for _ in range(100):
                diagrams = [rng.choice(rng.choice(available)) for j in range(rng.choice((2, 3, 4)))]
                raw = [converted_paths(compose(d['mm'], d['u'], []), d['labels']) for d in diagrams]
                if actual_reachable(raw, list(range(q)), set(range(q))) != set(range(q)):
                    continue
                inputs += 1
                zero_tether_ports += sum((d['tethers'] == 0 for d in diagrams))
                mixed += len(set(w)) > 1
                for end in ('L', 'R'):
                    (ns, _) = audit_general(w, diagrams, end)
                    audits += 1
                    states += ns
    return dict(sample_seed=60662026, packet_count_max=5, boundary_counts_per_port=[2, 4], actual_holes_per_pattern=4, bounded_local_pools=all_pools, local_diagram_options=local_options, reduced_sampled_inputs=inputs, seeded_closures=audits, reachable_states=states, zero_tether_port_occurrences=zero_tether_ports, mixed_sign_inputs=mixed)

def main():
    counts = dict(input_families=0, seeded_closures=0, reachable_states=0, mixed_sign_inputs=0, largest_chamber_closure=0)
    for q in range(1, 11):
        for tail in product((1, -1), repeat=q - 1):
            w = (1,) + tail
            local = pants(w)
            for m in (2, 3, 4):
                for diagrams in product(local, repeat=m):
                    (labels, _) = packet(w)
                    raw = [compose(mm, u, []) for (mm, u) in diagrams]
                    if actual_reachable(raw, labels, set(range(q))) != set(range(q)):
                        continue
                    counts['input_families'] += 1
                    counts['mixed_sign_inputs'] += len(set(w)) > 1
                    for end in ('L', 'R'):
                        (ns, nc) = audit(w, diagrams, end)
                        counts['seeded_closures'] += 1
                        counts['reachable_states'] += ns
                        counts['largest_chamber_closure'] = max(counts['largest_chamber_closure'], nc)
    out = dict(status='PASS: finite path diagrams only', packet_count_max=10, actual_pants_ports=[2, 3, 4], **counts, sampled_four_actual_hole_checks=wider_checks(), not_certified=['ordinary quotient', 'three-dimensional products', 'coloured prism compatibility'])
    print(json.dumps(out, ensure_ascii=False, indent=2))
if __name__ == '__main__':
    main()
