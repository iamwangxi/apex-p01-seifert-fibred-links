#!/usr/bin/env python3
"""Exact finite diagnostics for the new two-block rooted gluing interface.

Run with python3 -B. Reads this script and the local proof files; prints deterministic JSON.
It does not import another checker.
This finite model does not establish the topological inputs of the manuscript.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
COUNTS = defaultdict(int)

# Faces O,Q,C; C is the marked JSJ root.
ROOT = 2
LR = ((2, 1), (0, 2), (1, 0), (1, 0), (0, 1))
ENDPOINTS = ((3, 1), (3, 1), (4, 1), (3, 2), (4, 2))
NAMES = ("A0", "A1", "B")
MATCH = ((1, 0, 0, 0, 1), (0, 1, 0, 0, 1), (0, 0, 1, 1, 0))
POT = ((0, -1, 0), (1, 0, 0), (0, 0, 0))
INVERSE = {m: k for k, m in enumerate(MATCH)}
VERTICES = tuple(product(range(3), repeat=2))


def osc(xs):
    return max(xs) - min(xs)


def dv(v):
    return tuple(v[l] - v[r] for l, r in LR)


def floor(x):
    return x.numerator // x.denominator if isinstance(x, F) else x


def frac(x):
    return x - floor(x)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def local_flow(coeff):
    return tuple(sum((coeff[k] * MATCH[k][e] for k in range(3)), F(0)) for e in range(5))


def local_potential(coeff):
    return tuple(sum((coeff[k] * POT[k][f] for k in range(3)), F(0)) for f in range(3))


def distance(a, b):
    return osc([POT[a[i]][f] - POT[b[i]][f] for i in range(2) for f in range(3)])


def local_distance(a, b):
    return osc(sub(POT[a], POT[b]))


def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for j in range(n + 1):
            for tail in compositions(n - j, k - 1):
                yield (j,) + tail


def rooted_potentials(coeffs, reference):
    return tuple(sub(local_potential(coeffs[i]), POT[reference[i]]) for i in range(2))


def breaks(potentials):
    return sorted({F(0), F(1)} | {frac(-x) for u in potentials for x in u})


def rounded_at(potentials, reference, theta):
    out = []
    for i in range(2):
        q = tuple(floor(x + theta) for x in potentials[i])
        assert q[ROOT] == 0
        m = add(MATCH[reference[i]], dv(q))
        assert m in INVERSE, (reference, potentials, theta, m)
        # Independent degree check, not just lookup.
        for vertex in (1, 2, 3, 4):
            assert sum(m[e] for e, ends in enumerate(ENDPOINTS) if vertex in ends) == 1
        out.append(INVERSE[m])
    return tuple(out)


def decode(coeffs, reference=(2, 2), full_check=True):
    potentials = rooted_potentials(coeffs, reference)
    bs = breaks(potentials)
    bary = defaultdict(F)
    raw = []
    for lo, hi in zip(bs, bs[1:]):
        v = rounded_at(potentials, reference, (lo + hi) / 2)
        bary[v] += hi - lo
        raw.append(v)
        COUNTS["positive_threshold_intervals"] += 1
    for theta in bs[:-1]:
        raw.append(rounded_at(potentials, reference, theta))
        COUNTS["threshold_values_including_zero"] += 1
    assert sum(bary.values()) == 1
    if full_check:
        for a, b in combinations(set(raw), 2):
            assert distance(a, b) <= 1
            COUNTS["rounded_output_pair_checks"] += 1
        for side in range(2):
            expected = local_flow(coeffs[side])
            actual = tuple(sum((weight * MATCH[v[side]][e] for v, weight in bary.items()), F(0))
                           for e in range(5))
            assert actual == expected
        COUNTS["edge_expectation_checks"] += 2
    return dict(bary), tuple(raw)


def graph_masks():
    return tuple(mask for mask in range(1 << 5)
                 if any(all(not x or (mask >> e) & 1 for e, x in enumerate(m)) for m in MATCH))


class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def join(self, a, b):
        self.p[self.find(a)] = self.find(b)


def merged_faces(mask):
    u = UF(3)
    for e, (l, r) in enumerate(LR):
        if not (mask >> e) & 1:
            u.join(l, r)
    return tuple(u.find(f) for f in range(3))


def check_zero_faces(coeffs, bary):
    reference = next(iter(bary))
    potentials = rooted_potentials(coeffs, reference)
    candidates = []
    for i in range(2):
        w = local_flow(coeffs[i])
        choices = [mask for mask in MASKS
                   if all(not w[e] or (mask >> e) & 1 for e in range(5))]
        candidates.append(choices)
    # Check each individual quotient and all pairs of quotient supports.
    for i in range(2):
        for mask in candidates[i]:
            quotient = merged_faces(mask)
            u = potentials[i]
            for f, g in combinations(range(3), 2):
                if quotient[f] == quotient[g]:
                    assert u[f] == u[g]
            assert u[ROOT] == 0
            # All roundings descend through the actual region merger.
            for theta in breaks(potentials)[:-1]:
                q = tuple(floor(x + theta) for x in u)
                for f, g in combinations(range(3), 2):
                    if quotient[f] == quotient[g]:
                        assert q[f] == q[g]
                rounded = add(MATCH[reference[i]], dv(q))
                assert all(not rounded[e] for e in range(5) if not (mask >> e) & 1)
            COUNTS["zero_face_component_quotients"] += 1
    COUNTS["zero_face_support_pairs"] += len(candidates[0]) * len(candidates[1])


def det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def matvec(a, v):
    return tuple(sum(a[i][j] * v[j] for j in range(2)) for i in range(2))


def check_slope_and_linking_data():
    swap = ((0, 1), (1, 0))
    fibre_matrix = ((1, 1), (2, 1))
    assert det(swap) == det(fibre_matrix) == -1
    # In meridian,longitude coordinates.
    hp, hq, d = (1, 1), (-1, 1), (1, 0)
    assert matvec(swap, hp) == add(hq, (2, 0))
    assert matvec(swap, d) == add(hq, d)
    assert abs(det((matvec(swap, hp), hq))) == 2
    assert matvec(fibre_matrix, (1, 0)) == (1, 2)
    eps = (1, 1, -1, -1) * 2
    coherent = [[0 if i == j else (1 if i < 4 and j < 4 else -1)
                 for j in range(8)] for i in range(8)]
    actual = [[eps[i] * eps[j] * coherent[i][j] for j in range(8)]
              for i in range(8)]
    rows = [sum(row) for row in actual]
    assert rows == [-1] * 4 + [1] * 4
    assert sum(eps[:4]) == sum(eps[4:]) == 0
    assert all(actual[i][j] != 0 for i in range(8) for j in range(8) if i != j)
    COUNTS["gluing_matrix_checks"] = 5
    COUNTS["oriented_linking_rows"] = 8
    return {"meridian_longitude_matrix": swap, "fibre_section_matrix": fibre_matrix,
            "fibre_intersection": 2, "actual_linking_row_sums": rows}


def check_embedded_support_quotients():
    assert len(MASKS) == 17
    for mask in MASKS:
        u = UF(4)
        for e, ends in enumerate(ENDPOINTS):
            if (mask >> e) & 1:
                u.join(ends[0] - 1, ends[1] - 1)
        components = len({u.find(v) for v in range(4)})
        regions = len(set(merged_faces(mask)))
        assert regions == bin(mask).count("1") - 4 + components + 1
        COUNTS["spherical_region_euler_checks"] += 1
    for k in range(3):
        assert MATCH[k] == add(MATCH[2], dv(POT[k]))
        assert POT[k][ROOT] == 0
    for a, b in combinations(range(3), 2):
        assert local_distance(a, b) == 1


def check_grid():
    den = 8
    coeffs = [tuple(F(x, den) for x in c) for c in compositions(den, 3)]
    assert len(coeffs) == 45
    for cp, cq in product(coeffs, repeat=2):
        pair = (cp, cq)
        expected, raw = decode(pair)
        for reference in VERTICES:
            got, raw2 = decode(pair, reference)
            assert got == expected
            assert raw2 == raw
            COUNTS["reference_pair_comparisons"] += 1
        check_zero_faces(pair, expected)
        COUNTS["rational_product_flows"] += 1


def check_exact_simplex_recovery():
    simplices = []
    for mask in range(1, 1 << len(VERTICES)):
        s = tuple(VERTICES[j] for j in range(len(VERTICES)) if (mask >> j) & 1)
        if all(distance(a, b) <= 1 for a, b in combinations(s, 2)):
            simplices.append(s)
    maximal = [s for s in simplices
               if not any(v not in s and all(distance(v, a) <= 1 for a in s) for v in VERTICES)]
    assert len(maximal) == 6
    assert all(len(s) == 5 for s in maximal)
    COUNTS["nonempty_true_simplices"] = len(simplices)
    COUNTS["maximal_four_simplices"] = len(maximal)
    for s in maximal:
        for comp in compositions(8, len(s)):
            weights = tuple(F(x, 8) for x in comp)
            local_coeffs = tuple(tuple(sum((weights[j] for j, v in enumerate(s) if v[i] == k), F(0))
                                       for k in range(3)) for i in range(2))
            got, _ = decode(local_coeffs)
            expected = {v: weights[j] for j, v in enumerate(s) if weights[j]}
            assert got == expected, (s, weights, got)
            COUNTS["exact_simplex_recovery"] += 1


def check_shortcuts_fail():
    r, s, u, v = (2, 2), (1, 0), (1, 2), (2, 0)
    assert distance(r, s) == 2
    assert max(local_distance(r[i], s[i]) for i in range(2)) == 1
    assert all(distance(a, b) == 1 for a, b in combinations((r, s, u, v), 2) if {a, b} != {r, s})
    coeffs = ((F(0), F(1, 2), F(1, 2)), (F(1, 2), F(0), F(1, 2)))
    bary, _ = decode(coeffs)
    assert bary == {u: F(1, 2), v: F(1, 2)}
    independent = {r: F(1, 4), s: F(1, 4), u: F(1, 4), v: F(1, 4)}
    assert max(distance(a, b) for a, b in combinations(independent, 2)) == 2
    wrong_offsets = [x - POT[s[i]][0] for i in range(2) for x in POT[s[i]]]
    assert osc(wrong_offsets) == 1
    assert POT[s[0]][ROOT] - POT[s[0]][0] != POT[s[1]][ROOT] - POT[s[1]][0]
    return {"local_max_shortcut": 1, "correct_global_distance": 2,
            "independent_rounding_support_diameter": 2,
            "wrong_independent_root_shifts": 1,
            "common_threshold_midpoint_output": {"U": "1/2", "V": "1/2"}}


MASKS = graph_masks()
topological_data = check_slope_and_linking_data()
check_embedded_support_quotients()
check_grid()
check_exact_simplex_recovery()
counterexamples = check_shortcuts_fail()
report = {
    "status": "all exact finite assertions passed",
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "scope": "two copies of the five-edge marked-root planar support; exact fractions",
    "topological_coordinate_diagnostics": topological_data,
    "counts": dict(sorted(COUNTS.items())),
    "shortcut_counterexamples": counterexamples,
    "limits": [
        "Does not prove essentiality or simultaneous verticalisation of arbitrary surfaces.",
        "Does not prove the unrestricted isotopy comparison or PS simplified intersection.",
        "Does not verify the infinite finite-template argument or contractibility.",
        "No assertion about a nonempty JSJ-trace carrier."
    ]
}
report["proof_sha256"] = {str(p.relative_to(HERE.parent)): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in sorted((HERE.parent / "proof").glob("*.md"))}
print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
