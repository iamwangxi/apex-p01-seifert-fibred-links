#!/usr/bin/env python3
# Finite exact diagnostic for Part 9 of the proof; standard library only; prints a deterministic report and writes no files.
from itertools import product
from math import gcd
import json

def orbits(n, offsets):
    left = set(range(n))
    out = []
    while left:
        todo = [min(left)]
        seen = set(todo)
        while todo:
            x = todo.pop()
            for c in offsets:
                y = (c - x) % n
                if y not in seen:
                    seen.add(y)
                    todo.append(y)
        left -= seen
        out.append(seen)
    return out

def main():
    checked = 0
    for n in range(2, 21, 2):
        for leaves in range(2, 5):
            for cs in product(range(1, n, 2), repeat=leaves):
                g = n
                for c in cs:
                    g = gcd(g, c - cs[0])
                q = g // 2
                k = n // g
                points = orbits(n, cs)
                gaps = orbits(n, tuple((c - 1 for c in cs)))
                assert len(points) == q and {len(x) for x in points} == {2 * k}
                assert len(gaps) == q + 1
                point_id = {x: i for (i, o) in enumerate(points) for x in o}
                gap_id = {x: i for (i, o) in enumerate(gaps) for x in o}
                endcaps = {(c - 1) // 2 % n for c in cs} | {((c - 1) // 2 + n // 2) % n for c in cs}
                end_regions = {gap_id[x] for x in endcaps}
                assert len(end_regions) == 2
                incidence = {i: set() for i in range(q + 1)}
                for (i, piece) in enumerate(points):
                    neighbours = {gap_id[(x - 1) % n] for x in piece} | {gap_id[x] for x in piece}
                    assert len(neighbours) == 2
                    (a, b) = neighbours
                    incidence[a].add(i)
                    incidence[b].add(i)
                assert {i for (i, e) in incidence.items() if len(e) == 1} == end_regions
                assert all((len(e) == (1 if i in end_regions else 2) for (i, e) in incidence.items()))
                seen_regions = set()
                seen_pieces = set()
                todo = [0]
                while todo:
                    a = todo.pop()
                    seen_regions.add(a)
                    for p in incidence[a] - seen_pieces:
                        seen_pieces.add(p)
                        todo.extend((b for (b, es) in incidence.items() if p in es and b not in seen_regions))
                assert len(seen_regions) == q + 1 and len(seen_pieces) == q
                checked += 1
    print(json.dumps(dict(status='PASS — finite orbit incidences only', parameter_tuples=checked, largest_N=20, terminal_leaf_counts=[2, 3, 4], not_certified=['horizontal bundle models', 'three-dimensional product regions', 'ordinary loop normaliser', 'contractibility']), ensure_ascii=False, indent=2))
if __name__ == '__main__':
    main()
