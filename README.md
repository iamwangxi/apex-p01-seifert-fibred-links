# Contractibility of incompressible spanning surface complexes for graph links whose JSJ pieces all meet the link

The original **geometric disjointness complex** $`IS(L)=Y(L)`$ is contractible for every nonempty oriented non-split $`S^3`$ link whose exterior is a graph manifold and **every Seifert JSJ piece has an actual link boundary torus**. Arbitrarily many pieces, retained exceptional fibres and disconnected spanning surfaces are allowed. The cyclic-distance flag complex $`X(L)`$ is a simplicial subcomplex and a **strong deformation retract** of $`Y(L)`$ in the ordinary weak/CW topology. No general geometric flagness is asserted.

Theorem 29.2 additionally handles a genuine Seifert star whose leaves all meet the link and have nonzero fibre evaluation; its central piece can have no actual boundary. The earlier Seifert and stipulated two-block splice proofs are retained as foundations and special cases. In their abstract gluing-matrix formulation an actual $`S^3`$ link exterior with the stated meridians remains an independent hypothesis; a determinant-minus-one matrix alone does not supply it.

This is a supplement / breakthrough contribution to Apex Intelligence, *Contractibility of the complex of incompressible Seifert surfaces: the knot case of Kakimizu's problem*, official competition version of 11 September 2026, 48 pages. [Target PDF](https://math.apexin.net/papers/seifert-surfaces.pdf), SHA-256:

```text
34f17d7d99780d3fd3626d9e5d7b35d6aa76661c404f191b6df341b300c0c06f
```

Theorems A and D, printed p. 2, cover knots and linking-indecomposable links. The discussion there identifies the shared-component obstruction to general links at Lemma 4.9. We retain Definition 4.1's simultaneous geometric simplices (printed p. 8) and Kakimizu 1992's link-spanning convention (printed p. 225). Competition p. 8 says geometric adjacency and cyclic adjacency agree **for knots**; the disconnected-link distinction is explicitly discussed in Przytycki–Schultens' journal edition, printed pp. 1490 and 1493. This package proves geometric contractibility for the stated graph-manifold range, while allowing the extra geometric edges that disconnected surfaces can create.

## Reading the proof

The [objects and combined theorem](proof/objects.md) give the common vertex convention, whole open complementary blocks and Theorem 1.3. Numbering continues through Sections 29–40 for the graph-manifold extension; the planar-block lemmas form Appendix A.

1. **Seifert cyclic proof, Sections 2–8:** [classification and point branches](proof/classification.md); [closed orbifolds and two boundaries](proof/two-boundaries.md); [ordinary-isotopy vertices](proof/vertex-bijection.md); [exact class distance](proof/class-distance.md); [matching-flow decoder](proof/matching-carrier.md); [finite inclusion nullhomotopies](proof/contractibility.md); [double-cone example](proof/double-cone-example.md).
2. **Seifert geometric comparison, Sections 10–11:** [joint verticalisation, copies and geometric flagness](proof/geometric-realisation.md); [strong deformation retraction, CW continuity and convex fibres](proof/geometric-retraction.md). Theorem 11.2 uses $`R=S_G\circ W`$ and $`H(x,t)=(1-t)x+tR(x)`$.
3. **Splice cyclic proof, Sections 12–22:** [hypotheses](proof/splice-objects.md); [essential cuts and all-genus minimum trace](proof/splice-minimal-cuts.md); [relative horizontal uniqueness](proof/splice-horizontal-pieces.md); [ordinary vertices and twist quotient](proof/splice-vertices.md); [local](proof/splice-local-distance.md) and [global distances](proof/splice-global-distance.md); [decoder](proof/splice-matching-carrier.md); [contractibility](proof/splice-contractibility.md); [one cone](proof/splice-one-cone.md); [actual link witnesses](proof/splice-examples.md). [Appendix A](proof/splice-planar-blocks.md) contains the full block inputs.
4. **Splice geometric comparison, Sections 23–28:** [simultaneous efficient cuts](proof/splice-geometric-normalisation.md); [ordered horizontal pieces](proof/splice-horizontal-order.md); [trace criterion](proof/splice-trace-criterion.md); [restricted rounding](proof/splice-trace-rounding.md); [strong deformation retraction](proof/splice-geometric-retraction.md); [obstructions to unrestricted matching carriers](proof/splice-geometric-examples.md). Theorem 27.1 is the splice comparison.

5. **Graph-manifold proof, Sections 29–40:** [theorems and guide](proof/graph-theorems.md); [essential cuts and all-genus structure](proof/graph-structure.md); [ordinary annuli and efficient comparison](proof/graph-ordinary-annuli.md); [multiport phases and the integer tree quotient](proof/graph-horizontal-phases.md); [packet range reduction](proof/graph-packet-comparison.md); [horizontal filling](proof/graph-horizontal-filling.md); [global class minimum](proof/graph-class-distance.md); [potential polyhedra and exact decoding](proof/graph-potential-carrier.md); [geometric carrier and retraction](proof/graph-geometric-retraction.md); [finite-height contraction](proof/graph-contractibility.md); [six-component infinite tree](proof/graph-six-component-example.md); [relative-height integer line](proof/graph-relative-height-example.md).

[Scope and verification boundary](proof/scope.md), [checked bibliography](sources/bibliography.md), and [diagnostics](scripts/README.md) complete the package. No companion proof is needed to supply an internal lemma.

## Mechanism and limits

For a balanced Seifert exterior, ordinary vertices are planar unit-demand matching systems with unused cone holes retained as marks. Complete-block distance is the oscillation of one region potential. Common-threshold rounding decodes every matching flow and recovers every true cyclic simplex point exactly. Joint verticalisation and parallel allocation make all matchings on a compatible graph one geometric simplex, which carries the straight-line deformation.

For two blocks, every class has all-genus minimum trace $`q=\mathrm{div}(\Phi|_T)`$. A mixed cut has coherent nonempty trace, one horizontal piece and annuli with actual unit ends. Nonempty trace imposes a further condition: the trace word is $`q`$ repetitions of one cyclic ordering of the surface labels. Equivalently the pairwise potential oscillation on JSJ sectors is at most one. Restricted potentials form a nested binary chain; the **existing full-region decoder** preserves that chain. Its smaller trace-constrained geometric carriers therefore carry the same deformation. All matchings on a common graph need not form a geometric simplex.

For many pieces, zero-side annuli can join two nonunit ports and their local complements can be disconnected. Packet prefix reduction and inherited real port lifts compare their normal potentials to the **global class minimum**. Horizontal clusters retain $`s-1`$ relative integer heights between $`s`$ zero regions. The actual carriers are potential polyhedra with these unbounded directions, not merely flow polytopes. A single common threshold decodes all coordinates. Weighted global wall phases realise input and output together, giving the geometric deformation without general flagness. Finite height families delete closed circles and then reread the actual surviving classes and relative heights before decoding.

PS journal Definition 2.1, Proposition 3.2 and their stated early Section 3 inputs remain explicit literature dependencies. The splice metric also retains PS Lemma 3.5 and Banks Proposition 4.2. No PS Sections 4–7 projection, order, dismantling or contractibility theorem is used. Schultens' Proposition 25 is used only for closed good aspherical orbifolds, after its hypotheses are proved; Remark 35 is not used. The bibliography credits Hatcher's circle-map method and classical planar matching heights.

Graph manifolds with pieces having no actual boundary remain untreated outside Theorem 29.2. Oppositely oriented zero-framed parallels of a nontrivial torus knot have a boundary-free companion piece and a spanning class with minimum companion-torus trace two although the restricted class has divisibility zero. This explains the actual-boundary hypothesis; it does not contradict the coherent-trace classification proved here. Links with hyperbolic JSJ pieces are untreated. No priority is claimed for bare contractibility and no exhaustive novelty search was undertaken.

## Reproduction and review status

From the repository root, with Python 3 and its standard library:

```text
python3 -B scripts/run_all.py
```

The sixteen diagnostic programs print deterministic JSON. The runner compares all reports byte for byte without writing; `--update` deliberately refreshes the reports. Ten programs retain independently developed review implementations. Tests cover the cyclic models, geometric copies, exact retraction, crossing supports on common faces, coherent trace orders and restricted carriers. They do not certify arbitrary three-dimensional isotopy, the literature inputs or the infinite-complex theorem. The general PL normaliser and complete parameter-family procedure are specified mathematically and are not fully implemented.

The Seifert cyclic proof and its geometric comparison each received two fresh-context adversarial reviews without fatal or repair-requiring findings. The splice cyclic proof received two review rounds and package corrections. An independent derivation agreed with the Seifert geometric comparison. The two-block geometric comparison also received a fresh-context review without fatal or repair-requiring findings. Its wording correction is incorporated: only a low cable block on the zero side forces a singleton; a low horizontal-side cable block remains subject to the trace-order proof. Claude completed the final editorial review of this graph-manifold expansion. Review status is evidence metadata, not a mathematical hypothesis. The graph-manifold proof received two separate fresh-context reviews, covering slicing/class distance and carriers/retraction. Neither found a fatal issue. The slicing review's repair extending efficient comparison to the all-zero branch and its weighted-crossing clarification are incorporated in Sections 31 and 33. Every repository Markdown page was checked through GitHub's official rendering.

## AI disclosure

GPT-6.1 Sol, in OpenAI Codex under human direction, developed the proofs, ran the computations, and drafted this text; separate GPT-6.1 Sol sessions in fresh contexts performed adversarial reviews, and an independent GPT-6 Astra session re-derived the geometric-complex comparison. GPT-6 Astra also advised on research direction and submission scope. Claude planned the work, checked key steps against the sources, and reviewed and edited the final text. No human expert has certified the work.

## Licence and integrity

Original prose, documentation, diagnostic data and arrangement are CC BY 4.0. Code in `scripts/` is MIT-licensed; see [LICENSE](LICENSE). External publications retain their own rights and are not bundled. [MANIFEST.sha256](MANIFEST.sha256) lists every other packaged file.

[中文说明](README.zh-CN.md)
