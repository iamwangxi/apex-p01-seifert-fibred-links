#!/usr/bin/env python3
# Finite exact diagnostic for Part 9 of the proof; standard library only; prints a deterministic report and writes no files.
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, product
from math import gcd
from pathlib import Path
from hashlib import sha256
import json
import random
BASE = Path(__file__).resolve().parent.parent

def connected(vertices, edges):
    adj = {x: set() for x in vertices}
    for (x, y) in edges:
        adj[x].add(y)
        adj[y].add(x)
    rest = set(adj)
    cc = []
    while rest:
        todo = [min(rest)]
        seen = set(todo)
        while todo:
            for y in adj[todo.pop()] - seen:
                seen.add(y)
                todo.append(y)
        rest -= seen
        cc.append(seen)
    return cc

def trace(k, word):
    q = len(word)
    (copies, signs) = ([], [])
    for root in range(2 * k):
        js = list(range(q)) if root % 2 == 0 else list(reversed(range(q)))
        copies.extend(js)
        signs.extend((word[j] * (-1 if root % 2 else 1) for j in js))
    return (copies, signs)

def chamber_list(k, word, side):
    q = len(word)
    n = 2 * k * q
    pos = lambda r, j: r * q + (j if r % 2 == 0 else q - 1 - j)
    out = []
    if word[0] == -side:
        caps = [(pos(r, 0), pos((r + 1) % (2 * k), 0)) for r in range(1, 2 * k, 2)]
        out.append((frozenset({0}), tuple(caps)))
    for j in range(q - 1):
        if word[j] == side and word[j + 1] == -side:
            out.append((frozenset({j, j + 1}), tuple(((pos(r, j), pos(r, j + 1)) for r in range(2 * k)))))
    if word[-1] == side:
        out.append((frozenset({q - 1}), tuple(((pos(r, q - 1), pos(r + 1, q - 1)) for r in range(0, 2 * k, 2)))))
    normalized = []
    for (pieces, caps) in out:
        gaps = []
        for (a, b) in caps:
            if (b - a) % n != 1:
                (a, b) = (b, a)
            assert (b - a) % n == 1
            gaps.append((a, b))
        normalized.append((pieces, tuple(gaps)))
    used = set()
    for (pieces, _) in normalized:
        assert not used & pieces
        used |= pieces
    return normalized

def splice(returns, tethers, caps):
    edges = [(('o', a), ('o', b), None) for (a, b) in returns]
    edges += [(('o', a), ('a', a), None) for a in tethers]
    edges += [(('o', a), ('o', b), (a, b)) for (a, b) in caps]
    adj = {}
    for (eid, (a, b, _)) in enumerate(edges):
        adj.setdefault(a, []).append(eid)
        adj.setdefault(b, []).append(eid)
    assert all((len(ids) in (1, 2) for ids in adj.values()))
    used = set()
    paths = []
    for start in sorted((x for x in adj if len(adj[x]) == 1)):
        if adj[start][0] in used:
            continue
        (cur, tags) = (start, [])
        while True:
            options = [eid for eid in adj[cur] if eid not in used]
            if not options:
                paths.append((start, cur, tuple(tags)))
                break
            assert len(options) == 1
            eid = options[0]
            used.add(eid)
            (a, b, tag) = edges[eid]
            if tag is not None:
                tags.append(tag)
            cur = b if cur == a else a
    circles = 0
    for eid in range(len(edges)):
        if eid in used:
            continue
        circles += 1
        todo = [eid]
        while todo:
            e = todo.pop()
            if e in used:
                continue
            used.add(e)
            (a, b, _) = edges[e]
            todo.extend((x for v in (a, b) for x in adj[v] if x not in used))
    return (paths, circles)

def bad_paths(paths, marks, n):
    result = []
    for (x, y, caps) in paths:
        if x[0] != 'o' or y[0] != 'o':
            continue
        (a, b) = sorted((x[1], y[1]))
        enclosed = 0
        for h in marks:
            bit = int(2 * a < h < 2 * b)
            for (c, d) in caps:
                in_gap = 2 * c < h < 2 * d if c < d else h > 2 * c or h < 2 * d
                bit ^= int(in_gap)
            enclosed += bit
        if enclosed in (0, len(marks)):
            result.append(frozenset((a, b)))
    return result

def closure_audit(k, word, returns, tethers, pair_gaps, seed_last=False):
    (q, n) = (len(word), 2 * k * len(word))
    (labels, _) = trace(k, word)
    side = word[-1] if seed_last else -word[0]
    regs = chamber_list(k, word, side)
    end_piece = q - 1 if seed_last else 0
    seed = next((j for (j, (pp, _)) in enumerate(regs) if pp == {end_piece}))
    marks = [2 * i for i in tethers] + [2 * g + 1 for g in pair_gaps for _ in range(2)]
    original_cc = connected(range(q), [(labels[a], labels[b]) for (a, b) in returns])
    original_id = {x: j for (j, cc) in enumerate(original_cc) for x in cc}
    seed_component = original_cc[original_id[end_piece]]
    cap_id = {frozenset(cap): j for (j, (_, caps)) in enumerate(regs) for cap in caps}
    (cache, terminal) = ({}, [])

    def visit(selected):
        if selected in cache:
            return
        removed = set().union(*(regs[j][0] for j in selected))
        caps = [cap for j in selected for cap in regs[j][1]]
        (paths, _) = splice(returns, tethers, caps)
        bad = bad_paths(paths, marks, n)
        enabled = set()
        for witness in bad:
            assert witness in cap_id, (k, word, returns, tethers, pair_gaps, selected, witness)
            j = cap_id[witness]
            assert j not in selected
            assert not regs[j][0] & removed
            enabled.add(j)
        assert removed <= seed_component
        for (a, b, _) in paths:
            if a[0] == b[0] == 'o':
                assert original_id[labels[a[1]]] == original_id[labels[b[1]]]
        cache[selected] = enabled
        if not enabled:
            surviving = set(range(q)) - removed
            (ee, anchored) = ([], set())
            for (a, b, _) in paths:
                if a[0] == b[0] == 'o':
                    ee.append((labels[a[1]], labels[b[1]]))
                elif a[0] == 'o':
                    anchored.add(labels[a[1]])
                elif b[0] == 'o':
                    anchored.add(labels[b[1]])
            keep = set().union(*(cc for cc in connected(surviving, ee) if cc & anchored))
            assert len(keep) < q
            assert {x[1] for pp in paths for x in pp[:2] if x[0] == 'a'} == set(tethers)
            if len(set(word)) == 1:
                assert len(keep) == q - 1
            terminal.append(selected)
        else:
            for j in enabled:
                visit(selected | {j})
    visit(frozenset({seed}))
    assert len(set(terminal)) == 1
    for (a, ea) in cache.items():
        for (b, eb) in cache.items():
            if a <= b:
                assert ea - b <= eb
    return len(cache)

def random_closure_checks():
    rng = random.Random(20261024)
    (accepted, states, max_holes, mixed, two_tethers) = (0, 0, 0, 0, 0)
    for _ in range(24000):
        (k, q) = (rng.randint(1, 5), rng.randint(1, 10))
        n = 2 * k * q
        word = tuple((rng.choice((-1, 1)) for _ in range(q)))
        (labels, signs) = trace(k, word)
        holes = 2 * rng.randint(1, 6)
        t = 2 * rng.randint(1, min(holes, n) // 2)
        u = set(rng.sample(range(n), t))
        if sum((signs[i] for i in u)):
            continue
        gaps = [rng.randrange(n) for _ in range((holes - t) // 2)]
        marks = [2 * i for i in u] + [2 * g + 1 for g in gaps for _ in range(2)]

        @lru_cache(None)
        def count(xs):
            if not xs:
                return 1
            (a, total) = (xs[0], 0)
            for j in range(1, len(xs), 2):
                b = xs[j]
                if signs[a] == signs[b]:
                    continue
                inside = sum((2 * a < h < 2 * b for h in marks))
                if inside in (0, holes):
                    continue
                total += count(xs[1:j]) * count(xs[j + 1:])
            return total
        xs = tuple((i for i in range(n) if i not in u))
        if count(xs) == 0:
            continue

        def sample(xs):
            if not xs:
                return []
            a = xs[0]
            options = []
            for j in range(1, len(xs), 2):
                b = xs[j]
                if signs[a] == signs[b] or sum((2 * a < h < 2 * b for h in marks)) in (0, holes):
                    continue
                weight = count(xs[1:j]) * count(xs[j + 1:])
                if weight:
                    options.append((j, weight))
            pick = rng.randrange(sum((w for (_, w) in options)))
            for (j, w) in options:
                if pick < w:
                    return [(a, xs[j])] + sample(xs[1:j]) + sample(xs[j + 1:])
                pick -= w
            raise AssertionError('sampling failure')
        returns = sample(xs)
        anchored = {labels[i] for i in u}
        if any((not cc & anchored for cc in connected(range(q), [(labels[a], labels[b]) for (a, b) in returns]))):
            continue
        for seed_last in (False, True):
            states += closure_audit(k, word, returns, u, gaps, seed_last)
        accepted += 1
        max_holes = max(max_holes, holes)
        mixed += len(set(word)) > 1
        two_tethers += t == 2
    assert accepted > 300
    return dict(seed=20261024, candidates=24000, accepted=accepted, seeded_closures=2 * accepted, states=states, mixed_packets=mixed, two_tether_inputs=two_tethers, max_actual_boundaries=max_holes)

def numerical_examples():
    for q in range(1, 129):
        (a, b) = (lambda j: j, lambda j: 2 * q - 1 - j)
        (c, d) = (lambda j: 2 * q + j, lambda j: 4 * q - 1 - j)
        u = {a(q - 1), b(0), c(0), d(q - 1)}
        returns = [(a(j), b(j + 1)) for j in range(q - 1)]
        returns += [(c(j + 1), d(j)) for j in range(q - 1)]
        (labels, signs) = trace(2, (1,) * q)
        cc = connected(range(q), [(labels[x], labels[y]) for (x, y) in returns])
        assert len(cc) == 1
        assert sum((signs[x] for x in u)) == 0
        chi = -len(labels)
        assert F(2 - len(u) - chi, 2) == 2 * q - 1
        assert not bad_paths(splice(returns, u, [])[0], [2 * i for i in u], 4 * q)
        closure_audit(2, (1,) * q, returns, u, [])
    (labels, signs) = trace(2, (1, 1, -1, 1))
    returns = [(1, 15), (3, 14), (4, 13), (5, 12), (7, 11), (8, 10)]
    u = {0, 2, 6, 9}
    ee = [(labels[a], labels[b]) for (a, b) in returns]
    assert len(connected(range(4), ee)) == 1
    assert all((len(connected(range(4), ee[:i] + ee[i + 1:])) == 1 for i in range(6)))
    assert F(2 - 4 - -16, 2) == 7
    raw = [([(7, 8), (15, 0)], (10, 11)), ([(3, 4), (11, 12)], (13, 14)), ([(1, 2), (5, 6), (9, 10), (13, 14)], (3, 4)), ([(2, 3), (4, 5), (10, 11), (12, 13)], (7, 8))]
    for (caps, witness) in raw:
        (paths, _) = splice(returns, u, caps)
        assert frozenset(witness) in bad_paths(paths, [2 * i for i in u], 16)
    closure_audit(2, (1, 1, -1, 1), returns, u, [])
    closure_audit(2, (1, 1, -1, 1), returns, u, [], True)
    return dict(coherent_connected_families=128, genus_seven_raw_failures=4)

def orbit_checks():
    rng = random.Random(10105)
    checked = 0
    for _ in range(7000):
        n = 2 * rng.randint(1, 64)
        offsets = tuple((rng.randrange(1, n, 2) for _ in range(rng.randint(2, 7))))
        g = n
        for c in offsets:
            g = gcd(g, c - offsets[0])
        points = connected(range(n), [(i, (c - i) % n) for i in range(n) for c in offsets])
        gaps = connected(range(n), [(i, (c - 1 - i) % n) for i in range(n) for c in offsets])
        assert len(points) == g // 2
        assert {len(pp) for pp in points} == {2 * n // g}
        assert len(gaps) == g // 2 + 1
        gi = {i: j for (j, cc) in enumerate(gaps) for i in cc}
        end_gaps = {gi[((c - 1) // 2 + e * n // 2) % n] for c in offsets for e in (0, 1)}
        assert len(end_gaps) == 2
        degree = [0] * len(gaps)
        for pp in points:
            adjacent = {gi[i] for i in pp} | {gi[(i - 1) % n] for i in pp}
            assert len(adjacent) == 2
            for j in adjacent:
                degree[j] += 1
        assert all((x == (1 if j in end_gaps else 2) for (j, x) in enumerate(degree)))
        (v, k, gh) = (len(offsets), n // g, rng.randint(0, 5))
        chi_h = 1 - v - 2 * gh
        chi_f = 2 * k * chi_h
        assert F(2 - 2 * k - chi_f, 2) == 1 + k * (v - 2 + 2 * gh)
        checked += 1
    return dict(parameter_tuples=checked, max_N=128, terminal_leaf_counts='2..7')

def colour_order(n, b, weights):
    total = sum(weights)
    ts = [F(x, total) for x in weights]
    start = sum((x * t for (x, t) in zip(n, ts)))
    finish = start + sum((x * t for (x, t) in zip(b, ts)))
    suffix = [sum(ts[i:]) for i in range(len(ts) + 1)]
    active = []
    for (i, bit) in enumerate(b):
        if not bit:
            continue
        phase = (suffix[i] + suffix[i + 1]) / 2
        lifts = [phase + j for j in range(-2, 4) if start < phase + j < finish]
        assert len(lifts) == 1, (n, b, weights, i)
        active.append((lifts[0], i))
    return tuple((i for (_, i) in sorted(active)))

def coloured_order_checks():
    (cases, faces) = (0, 0)
    for m in range(1, 7):
        for cut in range(m + 1):
            n = tuple((int(i >= cut) for i in range(m)))
            for b in product((0, 1), repeat=m):
                if not any(b):
                    continue
                after = tuple((x + y for (x, y) in zip(n, b)))
                if sorted(after) != list(after) or max(after) - min(after) > 1:
                    continue
                reference = colour_order(n, b, [1] * m)
                for ww in ([i + 1 for i in range(m)], [m - i for i in range(m)], [1 + 3 * (i % 2) for i in range(m)]):
                    assert colour_order(n, b, ww) == reference
                for mask in range(1, 1 << m):
                    ids = [i for i in range(m) if mask >> i & 1]
                    (nn, bb) = (tuple((n[i] for i in ids)), tuple((b[i] for i in ids)))
                    if not any(bb):
                        continue
                    order = colour_order(nn, bb, [1] * len(ids))
                    assert tuple((ids[j] for j in order)) == tuple((i for i in reference if i in ids))
                    faces += 1
                cases += 1
    return dict(admissible_wall_chain_cases=cases, nonuniform_weight_tests=3 * cases, nonempty_wall_face_restrictions=faces)

def prism_checks():
    rng = random.Random(104)
    (slabs, probes, face_tests) = (0, 0, 0)

    def interpolate(events, lengths, ts, time, stationary):
        current = [0] * len(lengths)
        for i in events:
            low = sum((ts[j] * F(current[j], lengths[j]) for j in range(len(ts))))
            width = ts[i] / lengths[i]
            if width and low <= time <= low + width:
                new = (time - low) * lengths[i]
                out = {}
                for (j, weight) in enumerate(ts):
                    key = (j, 0 if j in stationary else current[j])
                    out[key] = out.get(key, F(0)) + weight - (new if j == i else 0)
                key = (i, 0 if i in stationary else current[i] + 1)
                out[key] = out.get(key, F(0)) + new
                return {v: t for (v, t) in out.items() if t}
            current[i] += 1
        raise AssertionError(('no slab', events, ts, time))
    for _ in range(500):
        m = rng.randint(1, 6)
        lengths = [rng.randint(1, 7) for _ in range(m)]
        (state, event_list) = ([0] * m, [])
        while state != lengths:
            i = rng.choice([j for j in range(m) if state[j] < lengths[j]])
            event_list.append(i)
            state[i] += 1
        weights = [rng.randint(1, 6) for _ in range(m)]
        ts = [F(w, sum(weights)) for w in weights]
        state = [0] * m
        for i in event_list:
            before = [F(state[j], lengths[j]) for j in range(m)]
            low = sum((t * h for (t, h) in zip(ts, before)))
            jump = F(1, lengths[i])
            high = low + ts[i] * jump
            for part in (F(0), F(1, 3), F(1, 2), F(1)):
                height = low + part * (high - low)
                new_coefficient = (height - low) / jump
                bary = list(ts)
                bary[i] -= new_coefficient
                assert min(bary) >= 0
                assert sum(bary) + new_coefficient == 1
                assert sum((bary[j] * before[j] for j in range(m))) + new_coefficient * (before[i] + jump) == height
                probes += 1
            state[i] += 1
            slabs += 1
        assert state == lengths
        for removed in range(m):
            if m == 1:
                continue
            face_weights = list(weights)
            face_weights[removed] = 0
            face_ts = [F(w, sum(face_weights)) for w in face_weights]
            restricted = [i for i in event_list if i != removed]
            for time in (F(0), F(1, 7), F(1, 2), F(6, 7), F(1)):
                for stationary in (set(), {j for j in range(m) if lengths[j] == 1}):
                    full = interpolate(event_list, lengths, face_ts, time, stationary)
                    face = interpolate(restricted, lengths, face_ts, time, stationary)
                    assert full == face
                    face_tests += 1
    return dict(slabs=slabs, rational_barycentric_probes=probes, exact_face_map_comparisons=face_tests)

def retained_event_checks():
    rng = random.Random(10104)
    (events_checked, faces) = (0, 0)
    for _ in range(4000):
        m = rng.randint(1, 8)
        colours = [i for i in range(m) for _ in range(rng.randint(0, 8))]
        rng.shuffle(colours)
        initial = [{j for (j, colour) in enumerate(colours) if colour == i} for i in range(m)]
        trajectories = []
        for i in range(m):
            remaining = set(initial[i])
            while remaining:
                seed = min(remaining)
                removed = {seed} | {p for p in remaining if rng.randrange(4) == 0}
                trajectories.append((seed, i, removed))
                remaining -= removed
        trajectories.sort(key=lambda event: event[0])
        remaining = [set(x) for x in initial]
        for (seed, colour, removed) in trajectories:
            assert seed == min(set().union(*remaining))
            assert seed == min(remaining[colour])
            assert removed <= remaining[colour]
            remaining[colour] -= removed
            events_checked += 1
        assert not set().union(*remaining)
        for deleted in range(m):
            face = [e for e in trajectories if e[1] != deleted]
            remaining = [set(x) if i != deleted else set() for (i, x) in enumerate(initial)]
            for (seed, colour, removed) in face:
                assert seed == min(set().union(*remaining))
                remaining[colour] -= removed
                faces += 1
    return dict(random_retained_subpacket_models=4000, empty_end_events=events_checked, face_schedule_events=faces)

def filtered_checks():
    rng = random.Random(107)
    cases = 0
    for _ in range(2500):
        weights = [rng.randint(1, 15) for _ in range(4)]
        ts = [F(w, sum(weights)) for w in weights]
        fwall = [rng.randint(-20, 20) for _ in range(4)]
        fv = [fwall[a] + fwall[2 + b] for a in range(2) for b in range(2)]
        aw = ts[0] + ts[1]
        bw = ts[0] + ts[2]
        cuts = sorted({F(0), aw, bw, F(1)})
        out = {}
        for (lo, hi) in zip(cuts, cuts[1:]):
            r = (lo + hi) / 2
            (a, b) = (int(r >= aw), int(r >= bw))
            j = 2 * a + b
            out[j] = out.get(j, F(0)) + hi - lo
        assert sum(out.values()) == 1
        fx = sum((t * f for (t, f) in zip(ts, fv)))
        assert sum((t * fv[j] for (j, t) in out.items())) == fx
        threshold = max(fv)
        for progress in (F(0), F(1, 3), F(1)):
            mix = {(0, j): (1 - progress) * t for (j, t) in enumerate(ts)}
            mix.update({(1, j): progress * t for (j, t) in out.items()})
            vals = {(kind, j): fv[j] for (kind, j) in mix}
            assert sum((mix[v] * vals[v] for v in mix)) == fx
            for a in (threshold, fx):
                keep = {v: t for (v, t) in mix.items() if vals[v] <= a and t}
                denom = sum(keep.values())
                assert denom > 0
                normalized = {v: t / denom for (v, t) in keep.items()}
                assert sum(normalized.values()) == 1
                assert all((vals[v] <= a for v in normalized))
        cases += 1
    corrected_edges = 0
    for numerator in range(1, 20):
        t = F(numerator, 20)
        initial = {1: t, 2: 1 - t}
        (a, b) = (t, 1 - t)
        output = {}
        cuts = sorted({F(0), a, b, F(1)})
        for (lo, hi) in zip(cuts, cuts[1:]):
            mid = (lo + hi) / 2
            j = 2 * int(mid >= a) + int(mid >= b)
            output[j] = output.get(j, F(0)) + hi - lo
        fv = (0, 2, 2, 4)
        assert output[3] > 0
        for progress in (F(0), F(1, 100), F(1, 2), F(1)):
            mixed = {j: (1 - progress) * initial.get(j, F(0)) + progress * output.get(j, F(0)) for j in range(4)}
            assert sum((mixed[j] * fv[j] for j in range(4))) == 2
            denom = sum((mixed[j] for j in range(3)))
            assert denom > 0
            corrected = {j: mixed[j] / denom for j in range(3) if mixed[j]}
            assert sum(corrected.values()) == 1
            assert all((fv[j] <= 2 for j in corrected))
            if progress == 0:
                assert corrected == initial
        corrected_edges += 1
    return dict(rational_weighted_wall_models=cases, deformation_and_sublevel_probes=cases * 3 * 2, edges_with_necessary_high_vertex_removal=corrected_edges)

def main():
    result = dict(numerical=numerical_examples(), closures=random_closure_checks(), gap_orbits=orbit_checks(), coloured_orders=coloured_order_checks(), retained_events=retained_event_checks(), affine_prisms=prism_checks(), filtered=filtered_checks())
    result['not_certified'] = ['ordinary isotopy / port loop quotients', 'incompressibility and 3D product regions', 'realizability of abstract diagrams as S3 link surfaces', 'global CW continuity / contractibility']
    result['status'] = 'PASS: independent finite diagnostics only'
    print(json.dumps(result, ensure_ascii=False, indent=2))
if __name__ == '__main__':
    main()
