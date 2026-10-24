#!/usr/bin/env python3
"""Exact, bounded algebraic diagnostics for the geometric-complex comparison.

Reads only repository-local proof files; prints deterministic JSON.
Does not traverse any subdirectory, import Seifert checker, or use third-party code; writes no files.
This does not certify the geometric system lemma or prove an infinite family.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
COUNTS = {}


def checked(key, n=1):
    COUNTS[key] = COUNTS.get(key, 0) + n


def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for a in range(total + 1):
        for rest in compositions(total - a, length - 1):
            yield (a,) + rest


class Graph:
    def __init__(self, name, edges):
        self.name, self.edges = name, tuple(edges)
        self.vertices = sorted({v for a, b, _, _ in edges for v in (a, b)})
        self.faces = sorted({f for _, _, l, r in edges for f in (l, r)})
        incident = {v: [] for v in self.vertices}
        for i, (a, b, _, _) in enumerate(edges):
            incident[a].append(i)
            incident[b].append(i)

        def recurse(remaining, chosen):
            if not remaining:
                yield frozenset(chosen)
                return
            v = min(remaining)
            for e in incident[v]:
                a, b, _, _ = edges[e]
                if a in remaining and b in remaining:
                    yield from recurse(remaining - {a, b}, chosen + [e])

        self.matchings = tuple(sorted(set(recurse(set(self.vertices), [])),
                                      key=lambda m: tuple(sorted(m))))
        assert self.matchings
        self.index = {m: i for i, m in enumerate(self.matchings)}
        self.all_edges = frozenset(range(len(edges)))
        self.potentials = [self.potential(self.vector(m), self.matchings[0])[0]
                           for m in self.matchings]
        self.adj = {i: set() for i in range(len(self.matchings))}
        for i, j in combinations(range(len(self.matchings)), 2):
            delta = [self.potentials[i][f] - self.potentials[j][f]
                     for f in self.faces]
            width = max(delta) - min(delta)
            assert width >= 1
            if width == 1:
                self.adj[i].add(j)
                self.adj[j].add(i)

    def vector(self, matching):
        return tuple(Q(e in matching) for e in range(len(self.edges)))

    def flow(self, bary):
        return tuple(sum((mass for i, mass in bary.items()
                          if e in self.matchings[i]), Q(0))
                     for e in range(len(self.edges)))

    def potential(self, w, reference, support=None, root=None):
        support = self.all_edges if support is None else support
        parent = {f: f for f in self.faces}

        def find(f):
            if parent[f] != f:
                parent[f] = find(parent[f])
            return parent[f]

        for e in self.all_edges - support:
            assert w[e] == 0 and e not in reference
            _, _, l, r = self.edges[e]
            a, b = find(l), find(r)
            parent[max(a, b)] = min(a, b)
        merge = {f: find(f) for f in self.faces}
        faces = sorted(set(merge.values()))
        root = faces[0] if root is None else merge[root]
        equations = []
        adjacent = {f: [] for f in faces}
        for e in support:
            _, _, l0, r0 = self.edges[e]
            l, r = merge[l0], merge[r0]
            d = w[e] - Q(e in reference)
            equations.append((l, r, d))
            adjacent[r].append((l, d))
            adjacent[l].append((r, -d))
        u, queue = {root: Q(0)}, [root]
        for f in queue:
            for g, change in adjacent[f]:
                value = u[f] + change
                if g in u:
                    assert u[g] == value
                else:
                    u[g] = value
                    queue.append(g)
        assert set(u) == set(faces), (self.name, faces, u)
        for l, r, d in equations:
            assert u[l] - u[r] == d
        return {f: u[merge[f]] for f in self.faces}, merge

    def decode(self, w, reference=None, support=None, root=None):
        reference = self.matchings[0] if reference is None else reference
        u, _ = self.potential(w, reference, support, root)
        cuts = sorted({Q(0), Q(1)} | {(-v) % 1 for v in u.values()})
        output = {}
        for low, high in zip(cuts, cuts[1:]):
            theta = (low + high) / 2
            q = {f: (v + theta).numerator // (v + theta).denominator
                 for f, v in u.items()}
            bits = []
            for e, (_, _, l, r) in enumerate(self.edges):
                bit = int(e in reference) + q[l] - q[r]
                assert bit in (0, 1)
                bits.append(bit)
            matching = frozenset(e for e, bit in enumerate(bits) if bit)
            assert matching in self.index
            assert all(w[e] > 0 for e in matching)
            i = self.index[matching]
            output[i] = output.get(i, Q(0)) + high - low
            checked('threshold_intervals')
        assert sum(output.values()) == 1
        assert self.flow(output) == tuple(w)
        assert self.is_true_simplex(output)
        checked('decoder_calls')
        return output

    def is_true_simplex(self, bary):
        return all(j in self.adj[i] for i, j in combinations(bary, 2))

    def maximal_cliques(self):
        def bronk(r, p, x):
            if not p and not x:
                yield tuple(sorted(r))
                return
            pivot = max(p | x, key=lambda a: len(p & self.adj[a])) if p | x else None
            candidates = p - self.adj[pivot] if pivot is not None else p.copy()
            for v in sorted(candidates):
                yield from bronk(r | {v}, p & self.adj[v], x & self.adj[v])
                p.remove(v)
                x.add(v)
        yield from bronk(set(), set(self.adj), set())


def grid(cols, rows):
    def face(x, y):
        if 0 < x < cols - 1 and 0 < y < rows - 1:
            return 1 + int(x // 1) + (cols - 1) * int(y // 1)
        return 0

    edges = []
    for y in range(rows):
        for x in range(cols):
            for nx, ny in ((x + 1, y), (x, y + 1)):
                if nx >= cols or ny >= rows:
                    continue
                a, b = (x, y), (nx, ny)
                if sum(a) % 2 == 0:
                    a, b = b, a
                dx, dy = b[0] - a[0], b[1] - a[1]
                mx, my = Q(a[0] + b[0], 2), Q(a[1] + b[1], 2)
                left = face(mx - Q(dy, 10), my + Q(dx, 10))
                right = face(mx + Q(dy, 10), my - Q(dx, 10))
                ai, bi = a[0] + cols * a[1], b[0] + cols * b[1]
                edges.append((ai, bi, left, right))
    return Graph(f'grid_{cols}x{rows}', edges)


def make_graphs():
    lens = [(2, 0, 1, 0), (2, 0, 0, 1),
            (3, 1, 2, 0), (3, 1, 0, 2)]
    cycle = []
    for i in range(6):
        j = (i + 1) % 6
        cycle.append((i, j, 1, 0) if i % 2 else (j, i, 0, 1))
    return [Graph('double_lens', lens),
            Graph('double_lens_forced_bridge', lens + [(5, 4, 0, 0)]),
            Graph('hexagon', cycle), grid(3, 2), grid(4, 2),
            grid(4, 3), grid(4, 4)]


def verify_graph(g):
    n = len(g.matchings)
    denominator = 4 if n <= 11 else 2
    samples = ({i: Q(a, denominator) for i, a in enumerate(c) if a}
               for c in compositions(denominator, n))
    sample_count = 0
    for serial, bary in enumerate(samples):
        sample_count += 1
        w = g.flow(bary)
        decoded = g.decode(w)
        if g.is_true_simplex(bary):
            assert decoded == bary
            checked('exact_recovery')
        positive = frozenset(e for e, mass in enumerate(w) if mass)
        supported = [m for m in g.matchings if m <= positive]
        assert supported
        assert g.decode(w, supported[-1], positive) == decoded
        checked('zero_face_mergers')
        if serial % 7 == 0:
            for ref in {g.matchings[0], g.matchings[n // 2], g.matchings[-1]}:
                assert g.decode(w, ref) == decoded
                checked('reference_comparisons')
            for root in g.faces:
                assert g.decode(w, root=root) == decoded
                checked('root_comparisons')
        for t in (Q(0), Q(1, 3), Q(1, 2), Q(1)):
            homotopy = {}
            for i in set(bary) | set(decoded):
                c = (1 - t) * bary.get(i, Q(0)) + t * decoded.get(i, Q(0))
                if c:
                    homotopy[i] = c
            assert sum(homotopy.values()) == 1
            assert g.flow(homotopy) == w
            assert g.decode(g.flow(homotopy)) == decoded
            if t == 0:
                assert homotopy == bary
            if t == 1:
                assert homotopy == decoded
            if g.is_true_simplex(bary):
                assert homotopy == bary
            checked('homotopy_parameter_checks')
        checked('rational_inputs')
    cliques = list(g.maximal_cliques())
    for clique in cliques:
        for weights in ([1] * len(clique), list(range(1, len(clique) + 1))):
            bary = {i: Q(a, sum(weights)) for i, a in zip(clique, weights)}
            assert g.decode(g.flow(bary)) == bary
            checked('maximal_simplex_recovery')
    # One additional input uses every matching with nonuniform positive mass.
    weights = [1 + (13 * i + 7) % 23 for i in range(n)]
    bary = {i: Q(a, sum(weights)) for i, a in enumerate(weights)}
    w = g.flow(bary)
    result = g.decode(w)
    assert g.flow(result) == w
    for ref in g.matchings:
        assert g.decode(w, ref) == result
        checked('full_support_reference_comparisons')
    return {'name': g.name, 'actual_vertices': len(g.vertices),
            'edges': len(g.edges), 'spherical_regions': len(g.faces),
            'matchings': n, 'cyclic_edges': sum(map(len, g.adj.values())) // 2,
            'maximal_cyclic_simplices': len(cliques),
            'rational_input_denominator': denominator,
            'composition_inputs': sample_count}


def double_lens_check(g):
    # Seifert labels M_ij choose e_i and f_j; edge indices are e0,e1,f0,f1.
    ids = {(i, j): g.index[frozenset((i, 2 + j))]
           for i in (0, 1) for j in (0, 1)}
    bad = {ids[0, 1]: Q(1, 2), ids[1, 0]: Q(1, 2)}
    good = {ids[0, 0]: Q(1, 2), ids[1, 1]: Q(1, 2)}
    assert not g.is_true_simplex(bad)
    assert g.is_true_simplex(good)
    assert g.flow(bad) == g.flow(good)
    assert g.decode(g.flow(bad)) == good
    a, b = ids[0, 1], ids[1, 0]
    delta = [g.potentials[a][f] - g.potentials[b][f] for f in g.faces]
    assert max(delta) - min(delta) == 2
    return {'illegal_cyclic_edge_width': 2,
            'geometric_carrier': 'tetrahedron on all four matching vertices',
            'cyclic_carrier': 'two triangles with diagonal M00--M11',
            'midpoint_retraction': '(M01+M10)/2 -> (M00+M11)/2',
            'preserved_edge_flow': [str(x) for x in g.flow(bad)]}


def main():
    graphs = make_graphs()
    profiles = [verify_graph(g) for g in graphs]
    special = double_lens_check(graphs[0])
    sources = sorted((HERE.parent/'proof').glob('*.md'))
    source_hashes = {str(p.relative_to(HERE.parent)): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in sources}
    report = {'status': 'PASS', 'arithmetic': 'fractions.Fraction; no tolerances',
              'counts': COUNTS, 'graphs': profiles, 'double_lens': special,
              'source_sha256': source_hashes,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'limits': ['Bounded algebraic diagnostics, not a proof by enumeration.',
                         'No test of 3D verticalisation or isotopy detection.',
                         'Repository-local sources only; no external dependencies.']}
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
