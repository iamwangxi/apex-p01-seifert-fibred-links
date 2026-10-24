# Bibliography, checked editions and actual dependencies

[Overview](../README.md) · [Scope](../proof/scope.md)

Page numbers below are **printed pages of the specified edition**, except where a preprint's own pagination is expressly stated. Source checks come from the supplied proofs and their source audits, together with the offline text checks made while assembling this package. This packaging step did not independently re-prove the cited theorems or newly inspect every page image. Public links identify recorded acquisition routes; they were not revisited during preparation. No external full text or PDF is bundled.

## Target competition paper

**Apex Intelligence.** *Contractibility of the complex of incompressible Seifert surfaces: the knot case of Kakimizu's problem*. Official competition version, 11 September 2026, 48 pages. Acquisition: [official competition PDF](https://math.apexin.net/papers/seifert-surfaces.pdf). PDF SHA-256, recomputed while packaging:

```text
34f17d7d99780d3fd3626d9e5d7b35d6aa76661c404f191b6df341b300c0c06f
```

Definition 4.1 and its following paragraph, p. 8: simultaneous geometric simplices and agreement with cyclic adjacency for knots. Introduction, p. 2: Theorems A and D, the connectedness role of linking-indecomposability, and the untreated general-link extension at Lemma 4.9 (the lemma itself is on pp. 11–12). Section 6.3, pp. 20–22, records the link slopes and connectedness interface. This package targets that competition version. Its proof does not assume the target's analytic exchange package or contractibility theorem. Section 2, Definition 2.1 (p. 3) and Theorem B (p. 4), the combinatorial exchange criterion, is quoted only in Part 11, §9 (where a tree satisfies it literally) and in Part 13 (where it fails for the geometric complex); no contractibility in this package depends on it.

For version distinction only, the subsequent author version is **G. Pan, C. You, J. Zhou and Y. Chen**, *Exchange complexes and contractibility of the complex of incompressible Seifert surfaces*, [arXiv:2609.09224v2](https://arxiv.org/abs/2609.09224v2), 12 September 2026. It is not substituted for the target competition edition or used as an additional proof input.

## Hatcher: essential surfaces, Seifert models and fillings

**Allen Hatcher.** *Notes on Basic 3-Manifold Topology*. Supplied author copy, using its internal printed pagination; no unchecked revision date is assigned. Acquisition route: [author PDF](https://pi.math.cornell.edu/~hatcher/3M/3M.pdf).

Checked Lemma 1.10, pp. 19–20 (solid-torus disks); Lemma 1.11, p. 20 (essentiality and the boundary-parallel-annulus exception); Proposition 1.12, pp. 20–22, including its boundary-relative verticalisation clause on p. 22 and its connected-surface convention on p. 12; horizontal covering and product complement, pp. 22–23; Proposition 1.13, pp. 23–24 (irreducibility); Corollary 1.15, p. 25 (solid-torus model fibering); nonorientable bases, sections, filling multiplicities and section twists, pp. 32–35; genus-one gluing and model solid tori, pp. 40–41. These support the explicit classification and point proof in §2, rather than an unquoted general classification of graph links. Parts 6–12 use the same Lemma 1.11, Proposition 1.12 and horizontal-product pages for their local cut pieces, statement (4) on pp. 14–15 (irreducibility after cutting along incompressible surfaces), and Proposition 1.14, p. 24 (essentiality of horizontal and admissible vertical pieces); essential assembly across tori is proved in those parts by the outermost-arc argument. Theorem 1.9, pp. 18–19, supplies the JSJ minimality/uniqueness criterion in the actual splice examples of §22. The finite-system extensions of the cut proof are proved explicitly in §§10, 23 and 30, rather than attributed to a printed disconnected-system theorem. The surface and filling pages were visually inspected in the supplied source audits.

## Schultens: closed-orbifold homotopy and isotopy

**Jennifer Schultens.** *Kakimizu complexes of Seifert fibered spaces*. *Algebraic & Geometric Topology* **18** (2018), 2897–2918. [DOI 10.2140/agt.2018.18.2897](https://doi.org/10.2140/agt.2018.18.2897). Acquisition: supplied journal PDF.

Checked §6: Definitions 21–24 on pp. 2906–2907 and Proposition 25 on p. 2907; its supporting lemmas run through pp. 2907–2911, and the proof of Proposition 25 is on pp. 2911–2912. The proposition concerns regular essential closed curves in a **closed good aspherical orbifold**. Sections 3 and 31 prove these hypotheses, including infinite order in the separating two-boundary case, before applying it. The regular-part fold is made into an orbifold-group retraction explicitly. Remark 35, p. 2912, is not used as a boundary-and-arc theorem. No automatic use of the paper's vertical-complex identification for this prescribed-boundary object is made.

## Przytycki–Schultens: early distance and simplified intersection

**Piotr Przytycki and Jennifer Schultens.** *Contractibility of the Kakimizu complex and symmetric Seifert surfaces*. *Transactions of the American Mathematical Society* **364** (2012), no. 3, 1489–1508. [DOI 10.1090/S0002-9947-2011-05465-6](https://doi.org/10.1090/S0002-9947-2011-05465-6). Acquisition: supplied **journal** PDF.

Checked setup on pp. 1489–1490, including the explicit disconnected-link distinction on p. 1490; p. 1493 reiterates that disjoint representatives can have cyclic distance greater than one; Definition 2.1, pp. 1492–1493 (whole **open** complementary lifts and class minimisation); §3, pp. 1494–1495, especially Proposition 3.2 (statement p. 1494, proof p. 1495), Proposition 3.3, Corollary 3.4 and Lemma 3.5 (p. 1495). Section 5 proves the actual simplified-intersection hypotheses for the normalised vertical systems. The §3 noncompact Sakuma interface is retained as a literature input, not independently reconstructed. In the splice metric, §17 checks connected complements and essential lifted frontiers before using Proposition 3.3 directly despite the separating JSJ multicurve. Section 18 uses the stated Lemma 3.5 to simplify the two spanning surfaces and the JSJ torus simultaneously. Its proof is left to the reader in the source; it remains a declared input. Section 35 also applies Lemma 3.5 to the whole oriented JSJ torus union as its third surface, after Section 30 proves norm minimality and essentiality. The packet comparison and real-lift filling in Sections 33–34 are proved here; they are not attributed to a local cyclic metric on disconnected complements. The geometric comparison proves finite-system normalisation directly and does not assume an extension of that lemma preserving a disjoint family. No conclusion from §§4–7 is used. Proposition 2.3 is not used, since its reverse inequality is deferred to §4. No further assessment of the paper's claims is made here.

## Sakuma: the declared product-region input

**Makoto Sakuma.** *Minimal genus Seifert surfaces for special arborescent links*. *Osaka Journal of Mathematics* **31** (1994), no. 4, 861–905. [DOI / institutional copy](https://doi.org/10.18910/9196). Acquisition: supplied journal PDF.

Checked the definitions of Seifert surfaces and their equivalence, pp. 863 and 871–872, which allow disconnected surfaces without closed components. Checked the blister definition and Proposition 4.8(2), p. 883: intersecting incompressible boundary-incompressible surfaces that can be isotoped apart admit the specified blister. Its uncollapsed side is in the ambient boundary. PS Proposition 3.3 is a stated possibly noncompact submanifold version, and that version is the actual input to PS Proposition 3.2. We have not independently certified that extension. Proposition 4.9(1), p. 883, supplies the standard flag convention for the geometric spanning-surface complex. Proposition 4.9(2), p. 883, states that the unlabelled embedded union of pairwise disjoint representatives of a simplex of $`IS(L)`$ is determined up to isotopy by the simplex. Both parts are used, in their stated all-incompressible non-split range, in the general comparison of Part 7, §9 (Theorem D) and in Part 9.

## Banks: relative product regions and parallelism

**Jessica E. Banks.** *The Kakimizu complex of a connected sum of links*. Checked edition: [arXiv:1109.0965v1](https://arxiv.org/abs/1109.0965v1), 5 September 2011. Acquisition: supplied preprint PDF; its own page numbers are used.

Checked Definition 4.1 and Proposition 4.2 on preprint p. 5, with Remarks 4.3–4.4 on p. 6: isotopic or isotopically disjoint incompressible boundary-incompressible surfaces admit the stated relative product regions. The uncollapsed vertical sides are in the ambient boundary. This supplies the finite simplification/parallelism input in Lemmas 16.1 and 31.2, including the explicit all-zero branch in the latter; the internal JSJ torus is not treated as an actual boundary side. Parts 6–13 also use Proposition 2.4, p. 2 (cyclic class distance equals graph distance), Proposition 4.10, p. 7 (simplified representatives attain the class distance), and the explicit extension of these statements to all incompressible spanning surfaces immediately after Definition 10.1, p. 22, together with the product-region statements above (Part 7, §9, applies Proposition 4.2(1) and Remark 4.4 to distinct whole components). The connected-sum product theorem is not used. The checked version is the 2011 v1 preprint, not a later edition with different pagination.

**Jessica E. Banks.** *On links with locally infinite Kakimizu complexes*. *Algebraic & Geometric Topology* **11** (2011), 1445–1454. Checked edition: [arXiv:1010.3831v2](https://arxiv.org/abs/1010.3831v2), 12 April 2011. Proposition 2.2, preprint p. 3, fixes the product-region and companion-torus conventions in Part 6; its Whitehead-double construction is not an input.

## Oertel: the relative convention

**Ulrich Oertel.** *Sums of incompressible surfaces*. *Proceedings of the American Mathematical Society* **102** (1988), no. 3, 711–719. Acquisition: supplied journal PDF; public route [AMS volume](https://www.ams.org/journals/proc/1988-102-03/).

Checked p. 712, especially the requirement that uncollapsed vertical boundary of a relative product region lie in the ambient boundary. This convention is used in Lemma 5.2; an arbitrary cone-fibred solid-torus chamber is not declared to be a product region.

## Kakimizu: all-incompressible geometric connectivity

**Osamu Kakimizu.** *Finding disjoint incompressible spanning surfaces for a link*. *Hiroshima Mathematical Journal* **22** (1992), no. 2, 225–236. [DOI 10.32917/hmj/1206392900](https://doi.org/10.32917/hmj/1206392900). Acquisition: supplied journal PDF.

Checked spanning conventions, p. 225; Theorem A and complete-complement construction, p. 226. Only **geometric connectivity** is used in Lemma 2.4 to upgrade the product-complement argument to the all-incompressible point conclusion. A disconnected-surface equality between geometric path distance and cyclic width is not an input. Part 10 cites the proof of Theorem 2.1 (Case 2, p. 230) only as the known all-incompressible connectivity argument, together with Przytycki–Schultens p. 1492 for the essentialisation-choice limitation; neither is used as a contraction theorem.

## Ordinary surface topology

**Benson Farb and Dan Margalit.** *A Primer on Mapping Class Groups*. Princeton University Press, 2012. Acquisition: supplied book PDF. Checked pp. 33–36, especially §1.2.7, pp. 35–36: ordinary curve/arc homotopy-isotopy, free boundary endpoints, bigons and boundary half-bigons, canonical simultaneous representatives and isotopy extension. These support §§3–5; no contraction of an ordinary arc complex is transferred to the matching domain.

**D. B. A. Epstein.** *Curves on 2-manifolds and isotopies*. *Acta Mathematica* **115** (1966), 83–107. Acquisition: supplied journal PDF. Checked Theorem 3.1, p. 89, for fixed-endpoint proper arcs. Free endpoint motion is handled with the boundary-circle convention above; no fixed-endpoint statement is silently substituted.

## Hatcher: circle-map method and CW conclusion

**Allen Hatcher.** *The cyclic cycle complex of a surface*. [arXiv:0806.0326v1](https://arxiv.org/abs/0806.0326v1), 2 June 2008, 7 pages. Acquisition: supplied arXiv copy. Checked the second proof, pp. 5–6: bicollars, based circle maps and regular-value preimages. It is the method source for the band-height family. Monotone prescribed boundaries, unused collars, arc-flow averaging, common-rounding decoding and parameter gluing are proved in §§6–7 and extended with actual relative-state rereading in §38. Hatcher's source/sink reduction is not used as a contraction of this complex.

**Allen Hatcher.** *Algebraic Topology*. Cambridge University Press, 2002. Acquisition: supplied author PDF, via the [author book page](https://pi.math.cornell.edu/~hatcher/AT/ATpage.html). Checked Proposition A.1, p. 520 (compact subsets of a CW complex lie in finite subcomplexes), and Whitehead Theorem 4.5, p. 346, including its subcomplex deformation-retraction consequence. These are the last two steps of Theorems 7.1, 20.1 and 29.1, after actual finite inclusion nullhomotopies have been constructed. The ordinary-product cellwise homotopy criterion on p. 523 and Theorem A.6 on p. 524 supply the closed-simplex-cylinder continuity in §§11, 27 and 37; the subcomplex topology is on p. 520. The criterion does not require local finiteness.

## Propp: planar matching heights

**James Propp.** *Lattice structure for orientations of graphs*. Checked edition: [arXiv:math/0209005v3](https://arxiv.org/abs/math/0209005v3), 19 March 2021. Acquisition: supplied arXiv PDF. The recorded later journal publication is *Electronic Journal of Combinatorics* **32**(4) (2025), #P4.26; the page references here refer to the checked v3, not to the journal.

Checked §3, Theorem 2 and its proof/face-height description, preprint pp. 21–22. This credits the classical planar bipartite matching-height framework. The printed connectedness and forced-edge restrictions are not assumed to cover disconnected supports or bridges. Section 6 independently proves every circulation, rounding and compatibility fact used here; Propp's theorem is attribution, not an unproved extension invoked as a proof input.

## Search and implementation boundary

No exhaustive novelty search was performed during packaging, and no assertion of priority for the bare conclusion is made. The finite programs are diagnostics, not implementations of every arbitrary-input normalisation and parameter-family operation. Exact editions and the stated mathematical inputs, rather than any absence-of-literature inference, determine the theorem's scope.
