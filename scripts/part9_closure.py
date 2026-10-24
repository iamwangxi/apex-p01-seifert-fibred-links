#!/usr/bin/env python3
# Finite exact diagnostic for Part 9 of the proof; standard library only; prints a deterministic report and writes no files.
from functools import lru_cache
from itertools import combinations, product
import json

def packet(k, w):
    q = len(w)
    labels = []
    signs = []
    for r in range(2 * k):
        order = range(q) if r % 2 == 0 else range(q - 1, -1, -1)
        labels.extend(order)
        signs.extend((w[j] * (-1 if r % 2 else 1) for j in order))
    return (labels, signs)

def matchings(n, u, signs, extra=None):

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
            holes = sum((a < i < b for i in u)) + (2 if extra is not None and a < extra < b else 0)
            if holes not in (1, 2, 3):
                continue
            for x in rec(tup[1:z]):
                for y in rec(tup[z + 1:]):
                    out.append(((a, b),) + x + y)
        return tuple(out)
    return rec(tuple((i for i in range(n) if i not in u)))

def all_actual(mm, u, labels, q):
    graph = [set() for _ in range(q)]
    for (a, b) in mm:
        graph[labels[a]].add(labels[b])
        graph[labels[b]].add(labels[a])
    seen = {labels[i] for i in u}
    todo = list(seen)
    while todo:
        a = todo.pop()
        for b in graph[a] - seen:
            seen.add(b)
            todo.append(b)
    return len(seen) == q

def chambers(k, w, side):
    q = len(w)
    n = 2 * k * q
    out = []
    if w[0] == -side:
        out.append(dict(name='L', copies={0}, caps=[(r * q + q - 1, (r + 1) * q % n) for r in range(1, 2 * k, 2)]))
    for j in range(q - 1):
        if (w[j], w[j + 1]) == (side, -side):
            caps = []
            for r in range(2 * k):
                positions = [r * q + (x if r % 2 == 0 else q - 1 - x) for x in (j, j + 1)]
                (a, b) = sorted(positions)
                assert b == a + 1
                caps.append((a, b))
            out.append(dict(name=f'P{j}', copies={j, j + 1}, caps=caps))
    if w[-1] == side:
        out.append(dict(name='R', copies={q - 1}, caps=[(r * q + q - 1, (r + 1) * q) for r in range(0, 2 * k, 2)]))
    used = set()
    for c in out:
        assert not used & c['copies']
        used |= c['copies']
    return out

def compose(mm, u, caps):
    graph = {}

    def add(a, b, tag):
        graph.setdefault(a, []).append((b, tag))
        graph.setdefault(b, []).append((a, tag))
    for (a, b) in mm:
        add(('o', a), ('o', b), None)
    for i in u:
        add(('o', i), ('a', i), None)
    for (j, (a, b)) in enumerate(caps):
        add(('o', a), ('o', b), j)
    assert all((len(v) in (1, 2) for v in graph.values()))
    ends = sorted((x for x in graph if len(graph[x]) == 1))
    seen = set()
    paths = []
    for start in ends:
        if start in seen:
            continue
        prev = None
        cur = start
        tags = []
        while True:
            seen.add(cur)
            if prev is not None and len(graph[cur]) == 1:
                paths.append((start, cur, tuple(tags)))
                break
            choices = [(x, t) for (x, t) in graph[cur] if x != prev]
            assert len(choices) == 1
            (nxt, tag) = choices[0]
            if tag is not None:
                tags.append(tag)
            (prev, cur) = (cur, nxt)
    return paths

def gap_contains(gap, x, n):
    (a, b) = gap
    assert b == (a + 1) % n
    return a < x < b if a < b else x > a or x < b

def bad_returns(paths, caps, u, extra, n):
    marks = list(u) + ([] if extra is None else [extra, extra])
    assert len(marks) == 4
    bad = []
    for (a, b, tags) in paths:
        if a[0] != b[0] or a[0] != 'o':
            continue
        (x, y) = sorted((a[1], b[1]))
        count = 0
        for mark in marks:
            bit = int(x < mark < y)
            for j in tags:
                bit ^= int(gap_contains(caps[j], mark, n))
            count += bit
        if count in (0, 4):
            bad.append((x, y, count))
    return bad

def surviving_actual_copies(paths, labels, removed, q):
    graph = {i: set() for i in range(q) if i not in removed}
    seen = set()
    for (a, b, _) in paths:
        if a[0] == b[0] == 'o':
            (x, y) = (labels[a[1]], labels[b[1]])
            graph[x].add(y)
            graph[y].add(x)
        elif a[0] == 'o':
            seen.add(labels[a[1]])
        elif b[0] == 'o':
            seen.add(labels[b[1]])
    todo = list(seen)
    while todo:
        a = todo.pop()
        for b in graph[a] - seen:
            seen.add(b)
            todo.append(b)
    return seen

def audit(k, w, mm, u, extra, seed_end):
    q = len(w)
    n = 2 * k * q
    (labels, _) = packet(k, w)
    side = -w[0] if seed_end == 'L' else w[-1]
    regs = chambers(k, w, side)
    seed = next((i for (i, r) in enumerate(regs) if r['name'] == seed_end))
    by_cap = {frozenset(pair): i for (i, r) in enumerate(regs) for pair in r['caps']}
    states = {}
    terminals = []

    def state(sel):
        caps = [cap for (i, r) in enumerate(regs) if i in sel for cap in r['caps']]
        removed = set().union(*(regs[i]['copies'] for i in sel))
        paths = compose(mm, u, caps)
        bad = bad_returns(paths, caps, u, extra, n)
        enabled = set()
        for (a, b, c) in bad:
            key = frozenset((a, b))
            assert key in by_cap, ('bad return not in same-side original chamber', k, w, mm, u, extra, seed_end, sel, bad)
            j = by_cap[key]
            assert j not in sel
            assert labels[a] not in removed and labels[b] not in removed
            enabled.add(j)
        assert {a[1] for p in paths for a in p[:2] if a[0] == 'a'} == set(u)
        return (enabled, paths, removed)

    def visit(sel):
        if sel in states:
            return
        (enabled, paths, removed) = state(sel)
        states[sel] = enabled
        if not enabled:
            kept = surviving_actual_copies(paths, labels, removed, q)
            assert len(kept) < q
            terminals.append((sel, kept))
            return
        for j in enabled:
            visit(sel | {j})
    visit(frozenset({seed}))
    assert len({s for (s, _) in terminals}) == 1, ('nonconfluent selected set', k, w, mm, u, extra, seed_end, terminals)
    for (a, ea) in states.items():
        for (b, eb) in states.items():
            if a <= b:
                assert ea - b <= eb, ('nonmonotone enabling', a, ea, b, eb)
    (selected, kept) = terminals[0]
    if all((x == w[0] for x in w)):
        assert len(kept) == q - 1, ('coherent count failure', k, w, mm, u, extra, seed_end, kept)
    return (len(states), len(selected), len(kept))

def main():
    cases = 0
    audits = 0
    states = 0
    max_selected = 0
    by_config = []
    configs = [(1, q) for q in range(1, 8)] + [(2, q) for q in range(1, 7)] + [(3, q) for q in range(1, 6)] + [(4, q) for q in range(1, 4)]
    for (k, q) in configs:
        count = 0
        n = 2 * k * q
        for ww in product((1, -1), repeat=q - 1):
            w = (1,) + ww
            (labels, signs) = packet(k, w)
            for t in (4, 2):
                if n < t:
                    continue
                for uu in combinations(range(n), t):
                    if sum((signs[i] for i in uu)):
                        continue
                    u = set(uu)
                    extras = [None] if t == 4 else [j + 0.5 for j in range(n)]
                    for extra in extras:
                        for mm in matchings(n, u, signs, extra):
                            if not all_actual(mm, u, labels, q):
                                continue
                            count += 1
                            cases += 1
                            for seed in ('L', 'R'):
                                (nstates, nsel, _) = audit(k, w, mm, u, extra, seed)
                                audits += 1
                                states += nstates
                                max_selected = max(max_selected, nsel)
        by_config.append(dict(k=k, q=q, input_diagrams=count))
    print(json.dumps(dict(status='PASS — finite diagrams only', input_diagrams=cases, seeded_closures=audits, reachable_closure_states=states, largest_selected_chamber_set=max_selected, configurations=by_config, not_certified=['ordinary invariance', 'Part 7 coloured-order interface', 'prism homotopy']), ensure_ascii=False, indent=2))
if __name__ == '__main__':
    main()
