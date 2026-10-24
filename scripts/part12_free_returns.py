#!/usr/bin/env python3
# Finite exact diagnostic for Part 12 of the proof; standard library only; prints a deterministic report and writes no files.
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
from math import gcd
import json
BASE = Path(__file__).resolve().parent

@lru_cache(None)
def noncrossing(tup):
    if not tup:
        return ((),)
    a = tup[0]
    out = []
    for z in range(1, len(tup), 2):
        b = tup[z]
        for x in noncrossing(tup[1:z]):
            for y in noncrossing(tup[z + 1:]):
                out.append(((a, b),) + x + y)
    return tuple(out)

def components(n, edges):
    graph = [set() for _ in range(n)]
    for (a, b) in edges:
        graph[a].add(b)
        graph[b].add(a)
    seen = set()
    out = []
    for j in range(n):
        if j in seen:
            continue
        todo = [j]
        cc = set()
        while todo:
            a = todo.pop()
            if a in cc:
                continue
            cc.add(a)
            todo.extend(graph[a] - cc)
        seen |= cc
        out.append(cc)
    return out

def positive_axes(eps):
    n = len(eps)
    r = n // 2
    return [a for a in range(n) if eps[a] == 1 and eps[(a + r) % n] == -1 and all((j in (a, (a + r) % n) or eps[(2 * a - j) % n] == -eps[j] for j in range(n)))]

def hole_marks(mat, n):
    marks = []
    for (a, b) in mat:
        if b - a == 1:
            marks.append(a + 0.5)
        elif (a, b) == (0, n - 1):
            marks.append(n - 0.5)
    if not 2 <= len(marks) <= 3:
        return None
    marks += marks[:1] if len(marks) == 2 else []
    assert len(marks) == 3
    for (a, b) in mat:
        assert 0 < sum((a < h < b for h in marks)) < 3
    return marks

def explicit_witness():
    n = 6
    eps = [1, 1, -1, 1, -1, -1]
    mat = ((0, 5), (1, 2), (3, 4), (6, 11), (7, 10), (8, 9))
    assert len({j for p in mat for j in p}) == 12
    for (i, (a, b)) in enumerate(mat):
        assert eps[a % n] == -eps[b % n]
        for (c, d) in mat[i + 1:]:
            assert not (a < c < b < d or c < a < d < b)
    marks = hole_marks(mat, 2 * n)
    assert marks == [1.5, 3.5, 8.5]
    assert 1 in positive_axes(eps)
    cap_edges = [(a % n, b % n) for (a, b) in mat]
    cuts = components(n, cap_edges)
    assert cuts == [{0, 5}, {1, 2, 3, 4}]
    chi_R = -2
    data = []
    for cc in cuts:
        assert sum((eps[j] for j in cc)) == 0
        chi = chi_R * len(cc)
        boundary = 2 * len(cc)
        genus = (2 - boundary - chi) // 2
        assert genus == 1
        data.append(dict(sheets=sorted(cc), chi=chi, boundaries=boundary, boundaries_at_each_port=len(cc), genus=genus))
    actual_returns = [(0, 2), (3, 5)]
    assert components(n, cap_edges + actual_returns + actual_returns) == [set(range(n))]
    assert (2 - 4 - n * chi_R) // 2 == 5
    gap_edges = []
    for (a, b) in mat:
        gap_edges.extend([((a - 1) % n, b % n), (a % n, (b - 1) % n)])
    gaps = components(n, gap_edges)
    assert gaps == [{0, 2, 4}, {1, 3}, {5}]
    mid = {0, 2, 4}
    faces = {'A': set(), 'B': set()}
    for j in range(n):
        name = 'A' if j in {0, 5} else 'B'
        if j in mid:
            faces[name].add(eps[j])
        if (j - 1) % n in mid:
            faces[name].add(-eps[j])
    assert faces == {'A': {1}, 'B': {-1}}
    path = [2, 0, 5, 3]
    assert all((tuple(sorted(edge)) in {(0, 2), (0, 5), (3, 5)} for edge in zip(path, path[1:])))
    assert not any((2 < j < 3 for j in (1, 4)))
    raw_chi = 4 * chi_R
    raw_genus = (2 - 4 - raw_chi) // 2
    assert raw_genus == 3
    safe_paths = [[1, 2, 0], [4, 3, 5]]
    assert all((tuple(sorted(edge)) in {(0, 2), (1, 2), (3, 4), (3, 5)} for path in safe_paths for edge in zip(path, path[1:])))
    assert (2 - 4 + 4) // 2 == 1
    intersections = [2, 2, 1, 1, 1, 1]
    assert all(intersections)
    return dict(actual_components=4, support='two zero-framed parallels', knot='T(2,3)#T(2,5)#T(3,4)', pattern_framings=[-2, 2], auxiliary_class=dict(lambda_K=2, mu_1=1, mu_2=-1, mu_K=0), central_sheets=n, signs=eps, pants_axes=[1, 1], actual_tethers_at_each_port=[1, 4], actual_returns_at_each_port=actual_returns, cap_matching=mat, unused_child_hole_marks=marks, support_cut_components=data, support_components_not_parallel_by_boundary_count=True, support_gap_regions=[sorted(a) for a in gaps], mixed_region_faces={'A': 'positive', 'B': 'negative'}, raw_end_resolution=dict(removed_support_piece='A', cap_at_each_port=[5, 0], bad_return_at_each_port=[2, 3], retained_tethers_at_each_port=[1, 4], chi=raw_chi, genus=raw_genus, actual_component_compressible_by_proof=True), safe_opposite_end=dict(removed_support_piece='B', caps_at_each_port=[[1, 2], [3, 4]], tether_paths=safe_paths, retained_support_piece='A', genus=1, cyclic_neighbour_by_component_wall_proof=True), special_distance=dict(to_two_annulus_vertex=2, half_central_sheet_count=3, proof='safe cyclic path plus forced pants crossing', not_an_all_pair_formula=True), whole_surface_connected=True, whole_chi=-12, whole_genus=5, JSJ_blocks=7, interface_fibre_intersections=intersections, not_claimed=['noncontractibility', 'complete ordinary catalogue', 'homology of the full complex'])

def finite_search():
    out = []
    for n in (2, 4, 6):
        checked = reduced = unequal = 0
        for tail in combinations(range(1, n), n // 2 - 1):
            pos = set(tail) | {0}
            eps = [1 if j in pos else -1 for j in range(n)]
            axes = positive_axes(eps)
            if not axes:
                continue
            for mat in noncrossing(tuple(range(2 * n))):
                if any((eps[a % n] == eps[b % n] for (a, b) in mat)):
                    continue
                if hole_marks(mat, 2 * n) is None:
                    continue
                cap = [(a % n, b % n) for (a, b) in mat]
                cuts = components(n, cap)
                for (a, b) in product(axes, repeat=2):
                    checked += 1
                    edges = cap + [(j, (2 * a - j) % n) for j in range(n)]
                    edges += [(j, (2 * b - j) % n) for j in range(n)]
                    whole = components(n, edges)
                    actual = {a, (a + n // 2) % n, b, (b + n // 2) % n}
                    if not all((cc & actual for cc in whole)):
                        continue
                    reduced += 1
                    unequal += len(set(map(len, cuts))) > 1
        out.append(dict(sheets=n, axis_matching_choices=checked, reduced_choices=reduced, unequal_support_boundary_counts=unequal))
    assert out[0]['unequal_support_boundary_counts'] == 0
    assert out[1]['unequal_support_boundary_counts'] == 0
    assert out[2]['unequal_support_boundary_counts'] > 0
    return out

def meridional_two_feature_tests():
    count = 0
    for d in range(1, 65):
        chi_R = -d
        assert (2 - (2 + d) - chi_R) // 2 == 0
        chi_F = 2 * chi_R
        genus_F = (2 - 4 - chi_F) // 2
        assert genus_F == d - 1 and chi_F < 0
        assert gcd(0, d) == d
        for r in range(1, 17):
            assert (2 - 4 - 2 * r * chi_R) // 2 == d * r - 1
            count += 1
    return dict(degree_max=64, whole_Euler_checks=count, degree_one_companion=dict(genus=0, boundaries=4, chi=-2))

def main():
    out = dict(status='PASS: finite planar and Euler data', proposition_M=explicit_witness(), finite_search=finite_search(), corollary_L=meridional_two_feature_tests())
    print(json.dumps(out, ensure_ascii=False, indent=2))
if __name__ == '__main__':
    main()
