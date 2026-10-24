# Incompressible spanning surface complexes of links: a general comparison theorem and contractibility for large classes of graph links

This package extends the main theorem of the competition paper from knots to links whose spanning surfaces may be **disconnected**. Two complexes on the same vertex set are compared: Kakimizu's original **geometric disjointness complex** $`IS(L)=Y(L)`$, whose simplices are families with simultaneously disjoint representatives, and the **cyclic-distance flag complex** $`X(L)`$. Vertices are all reduced, componentwise incompressible spanning surfaces, of every genus, up to ordinary ambient isotopy.

**Theorem 1 (general comparison; [Part 7](proof/part7.md), Theorem D).** For every nonempty oriented non-split link $`L\subset S^3`$, the identity on vertices gives $`X(L)\subseteq Y(L)`$, and $`|X(L)|`$ is a strong deformation retract of $`|Y(L)|`$. Consequently $`X(L)`$ is contractible if and only if $`IS(L)`$ is.

**Theorem 2 (contractibility).** $`X(L)`$ and $`Y(L)`$ are contractible for every nonempty oriented non-split link $`L\subset S^3`$ whose exterior is a graph manifold in any of the following classes.

1. **Seifert-fibred exteriors** (Theorems 1.2 and 11.2).
2. **Every Seifert JSJ piece meets the link** (Theorems 1.3 and 29.1), and the horizontal-leaf stars of Theorem 29.2.
3. **Anchored transverse clusters** ([Part 7](proof/part7.md), Theorem A): the spanning class is nonzero on every Seifert piece, and every component of the forest of pieces with nonzero fibre evaluation contains an actual link boundary torus. Pieces without link boundary are allowed.
4. **Parallel families of recursive graph knots** ([Part 12](proof/part12.md), Theorems A and G). Let $`K`$ be obtained from nontrivial torus knots by finitely many connected sums and cables. Replace $`K`$ by any positive number of parallel copies, with any integer framing and any orientations. The zero-framed case for connected sums of torus knots, including the balanced four parallels of the square knot, is [Part 9](proof/part9.md), Theorem 1.9. Two opposite zero-framed parallels have $`X=Y`$ an edge for iterated cables of torus knots ([Part 6](proof/part6.md); Part 7, Theorem B) and a rooted tree for every recursive graph knot, of unbounded diameter for the square knot ([Part 8](proof/part8.md)).
5. **Rigid caps and Seifert supports** ([Part 10](proof/part10.md)): cores of the anchored type carrying boundary-free knot exteriors that are longitudinally rigid, with an exact criterion for connected sums of torus knots and a recursive slope certificate (Theorems 1.1 and 1.3, Proposition 1.2); balanced zero-framed parallel replacements of Seifert-fibred supports (Theorem 11.2 and Corollaries 11.3–11.5).
6. **Resonant Hopf stars** ([Part 11](proof/part11.md)): for $`n\ge3`$, replace each of $`n`$ regular Hopf fibres by one positive and one negative parallel of framing $`-(n-1)`$. The central piece has no link boundary and the spanning class vanishes on it, so classes 2 and 3 do not apply; $`X=Y`$ is a simplicial tree. A finite certificate admits further central clusters.
7. **Weighted supports and common separating packets** ([Part 12](proof/part12.md), Theorems I, J, K, Corollaries K1, L, L1), and the composition class of Theorem F, which is closed under boundary fibre decorations, unit fibre-pattern substitutions and empty-interface products.

**Remark ([Part 13](proof/part13.md)).** The competition paper's knot proof rests on a combinatorial exchange criterion (its §2, Theorem B). For links that criterion fails on $`Y`$: for twelve balanced regular Hopf fibres, and for the balanced six-component torus link $`T(12,18)`$, an explicit pair of vertices at distance two has full common neighbourhood a four-vertex path, which has no apex, whatever the complexity. Both complexes are nevertheless contractible. The proofs here are topological and do not use the paper's analytic package or its exchange theorem.

This is a supplement / breakthrough contribution to Apex Intelligence, *Contractibility of the complex of incompressible Seifert surfaces: the knot case of Kakimizu's problem*, official competition version of 11 September 2026, 48 pages. [Target PDF](https://math.apexin.net/papers/seifert-surfaces.pdf), SHA-256:

```text
34f17d7d99780d3fd3626d9e5d7b35d6aa76661c404f191b6df341b300c0c06f
```

Theorems A and D of the paper, printed p. 2, cover knots and linking-indecomposable links, where every spanning surface is connected. Its Section 6.3 states that the obstacle for general links is the definition of a vertex. Most links in Theorem 2, for example all parallel families with zero pairwise linking, are linking-decomposable and have disconnected incompressible spanning surfaces. We retain Definition 4.1's simultaneous geometric simplices (printed p. 8) and Kakimizu 1992's link-spanning convention (printed p. 225); the disconnected-link distinction between the two complexes is discussed in Przytycki–Schultens' journal edition, printed pp. 1490 and 1493.

## Reading the proof

[Section 1](proof/objects.md) fixes the common vertex convention, the whole open complementary blocks and Theorem 1.3. Parts 1–5 are numbered as Sections 2–40 with Appendix A; Parts 6–13 number their results locally and cite one another as “Part n, Theorem x”.

1. **Seifert cyclic proof, Sections 2–8:** [classification and point branches](proof/classification.md); [closed orbifolds and two boundaries](proof/two-boundaries.md); [ordinary-isotopy vertices](proof/vertex-bijection.md); [exact class distance](proof/class-distance.md); [matching-flow decoder](proof/matching-carrier.md); [finite inclusion nullhomotopies](proof/contractibility.md); [double-cone example](proof/double-cone-example.md).
2. **Seifert geometric comparison, Sections 10–11:** [joint verticalisation, copies and geometric flagness](proof/geometric-realisation.md); [strong deformation retraction](proof/geometric-retraction.md).
3. **Two-block splices, Sections 12–22:** [hypotheses](proof/splice-objects.md); [essential cuts](proof/splice-minimal-cuts.md); [horizontal uniqueness](proof/splice-horizontal-pieces.md); [ordinary vertices](proof/splice-vertices.md); [local](proof/splice-local-distance.md) and [global distances](proof/splice-global-distance.md); [decoder](proof/splice-matching-carrier.md); [contractibility](proof/splice-contractibility.md); [one cone](proof/splice-one-cone.md); [actual link witnesses](proof/splice-examples.md); [Appendix A](proof/splice-planar-blocks.md).
4. **Splice geometric comparison, Sections 23–28:** [simultaneous efficient cuts](proof/splice-geometric-normalisation.md); [ordered horizontal pieces](proof/splice-horizontal-order.md); [trace criterion](proof/splice-trace-criterion.md); [restricted rounding](proof/splice-trace-rounding.md); [strong deformation retraction](proof/splice-geometric-retraction.md); [obstructions to unrestricted carriers](proof/splice-geometric-examples.md).
5. **Graph manifolds whose pieces meet the link, Sections 29–40:** [theorems and guide](proof/graph-theorems.md); [essential cuts](proof/graph-structure.md); [ordinary annuli](proof/graph-ordinary-annuli.md); [multiport phases](proof/graph-horizontal-phases.md); [packet range reduction](proof/graph-packet-comparison.md); [horizontal filling](proof/graph-horizontal-filling.md); [global class minimum](proof/graph-class-distance.md); [potential polyhedra](proof/graph-potential-carrier.md); [geometric retraction](proof/graph-geometric-retraction.md); [finite-height contraction](proof/graph-contractibility.md); [six-component tree](proof/graph-six-component-example.md); [integer line](proof/graph-relative-height-example.md).
6. **[Part 6](proof/part6.md):** two oppositely oriented zero-framed parallels of a torus knot; $`X`$ is one edge, with a disconnected non-norm-minimising vertex.
7. **[Part 7](proof/part7.md)** (two pages): anchored clusters (Theorem A), iterated-cable double parallels (Theorem B), a cancelling family of every genus (Proposition C) and the general comparison (Theorem D, §9).
8. **[Part 8](proof/part8.md)** (three pages): the square-knot cancellation tree and recursive graph-knot double parallels.
9. **[Part 9](proof/part9.md)** (four pages): all zero-framed parallel clusters of connected sums of torus knots.
10. **[Part 10](proof/part10.md)** (three pages): rigid caps, slope envelopes and Seifert-support parallels.
11. **[Part 11](proof/part11.md)** (two pages): the resonant Hopf stars.
12. **[Part 12](proof/part12.md)** (three pages): framed recursive parallels, common separating packets, weighted supports and the composition class.
13. **[Part 13](proof/part13.md):** failure of the exchange axiom (N1) on the geometric complex.

[Scope and verification boundary](proof/scope.md), [checked bibliography](sources/bibliography.md), and [diagnostics](scripts/README.md) complete the package. No companion proof is needed to supply an internal lemma.

## Mechanism and limits

For Seifert exteriors, ordinary vertices are planar matching systems; complete-block distance is the oscillation of one region potential, and common-threshold rounding decodes every matching flow. When every piece meets the link, packet prefix reduction, inherited real port lifts and weighted wall phases give the class minimum and the geometric deformation. The general comparison of Theorem 1 averages Thom band maps of whole component walls in one global cyclic cover; a generic level is a union of entire parallel components, so no compression choice is needed.

Beyond these ranges, pieces without link boundary carry cancelling surfaces of unbounded genus (Part 7, Proposition C), and a pointwise descent alone does not contract the complex. Parts 8–12 replace a global compression choice by structures that are canonical on whole finite families: a unique annular parent and a common parallel packet (Parts 8 and 9), a finite same-side chamber closure with prism homotopies (Part 9), longitudinal rigidity of caps (Part 10), a repeated-axis barrier in an auxiliary four-holed sphere giving unique Farey parents (Part 11), and one global chamber order for a separating packet seen at several ports (Part 12).

All non-split graph links are **not** covered. Part 12, Proposition M, gives an actual four-component link in which one spanning vertex contains nonparallel support pieces, so the common-packet reduction fails; non-separating central fibre clusters and pieces visible at only some ports also remain. These are obstructions to the present methods, not counterexamples to contractibility. Links with hyperbolic JSJ pieces are untreated. No priority is claimed for bare contractibility conclusions, and no exhaustive novelty search was undertaken.

## Reproduction and review status

From the repository root, with Python 3 and its standard library:

```text
python3 -B scripts/run_all.py
```

The runner executes every diagnostic program, captures its deterministic output and compares it byte for byte with the stored report, without writing; `--update` deliberately refreshes the reports. The [diagnostic guide](scripts/README.md) lists the programs, including independent implementations written by the reviewers. Finite tests do not certify arbitrary three-dimensional isotopy, the literature inputs or the infinite-complex theorems.

Every part received at least one fresh-context adversarial review; none found a fatal issue. The corrections they requested are incorporated: the all-zero branch of Lemma 31.2; five clarifications in Part 7, including the product-region citations and the finite-subcomplex wording of the continuity step; two clarifications in Part 8; Remark 11.3 of Part 9, which shows that the several-port branches of its Theorems 11.1–11.2 are vacuous in $`S^3`$; the Hatcher citation in Part 10; the port-sign re-encoding of the bundle-port lemma and certificate in Part 11. Claude assembled Parts 6–13 from the reviewed manuscripts and completed the final editorial review. Review status is evidence metadata, not a mathematical hypothesis. Every repository Markdown page was checked through GitHub's official rendering.

## AI disclosure

GPT-6.1 Sol and GPT-6 Astra, in OpenAI Codex under human direction, developed the proofs and ran the computations; separate GPT-6.1 Sol sessions in fresh contexts performed the adversarial reviews and wrote independent diagnostic implementations. GPT-6 Astra also advised on research direction. Claude planned the work, checked key steps against the sources, assembled the package and edited the final text. No human expert has certified the work.

## Licence and integrity

Original prose, documentation, diagnostic data and arrangement are CC BY 4.0. Code in `scripts/` is MIT-licensed; see [LICENSE](LICENSE). External publications retain their own rights and are not bundled. [MANIFEST.sha256](MANIFEST.sha256) lists every other packaged file.

[中文说明](README.zh-CN.md)
