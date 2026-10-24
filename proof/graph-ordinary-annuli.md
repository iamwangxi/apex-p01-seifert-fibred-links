# 31. Ordinary annuli, packets, and port motions

[Overview](../README.md) · [Definitions](objects.md) · [Graph-manifold theorems](graph-theorems.md) · [References](../sources/bibliography.md)

## 31.1. Distinct-end detection without a unit endpoint

Let a planar Seifert block have $`b\ge2`$ ordinary boundary circles and $`s`$ cones. Its fibre quotient is


```math
\Gamma=C_{q_1}*\cdots*C_{q_s}*F_{b-1}.
```


Track a path across an annulus during an arbitrary ambient isotopy. Quotienting by the fibre gives its endpoint peripheral double coset in $`\Gamma`$. The argument does not require either end to be actual.

For $`b\ge3`$, close a proper arc from $`C_i`$ to $`C_j`$ by the third boundary of a thin pair of pants. Its rational class $`d_i+d_j`$ is nonzero. Doubling along **all** ordinary circles injects the orbifold group, by the regular-part fold. The paired-cone finite cover makes this a closed good aspherical orbifold, by the closed-double construction in [Section 3](two-boundaries.md). Closed Schultens Proposition 25 recovers an isotopy of the closing curves avoiding the cones, and the labelled pants seam recovers the ordinary arc.

For $`b=2,s\ge2`$, cap one ordinary boundary by an ordinary disk. The closing curve maps to the remaining outer boundary of a disk with all $`s`$ cones, whose word is $`x_1\cdots x_s`$ in their free product. It is cyclically reduced of length at least two and has infinite order. The same closed-double argument applies. This extends the two-cone argument in [Section 3](two-boundaries.md) without requiring coprime orders or an actual endpoint. For $`b=2,s\le1`$, the ordinary annulus or pants seam has one unmarked class, directly.

It follows that **joint ordinary multiarc classes with multiplicities** detect ordinary vertical-annulus systems. A hyperbolic metric on the regular base gives the unique ordinary orthogeodesic cores. Parallel occurrences form a packet in a rectangle; their number is retained. Joint straightening retains cyclic endpoint order. Tangential fibre reparametrisations add no annular framing coordinate: the annulus contains the whole fibre circle.

Simultaneous verticalisation is valid even when cuts disconnect the base. Verticalise one incompressible annulus relative to already vertical cut faces and cut along it, carrying the remaining disjoint annuli. Work in every resulting Seifert component. A remaining annulus is essential or boundary-parallel; the latter is straightened in its boundary parallelism. All boundary slopes are fibres, so the horizontal alternative is excluded. This finite induction does not require previously unused endpoints or connected cuts.

The cone version of the empty-disk and peripheral test is also unchanged by multiplicity. For a regular Jordan loop let $`a_i,\eta_j\in\{0,1\}`$ record the ordinary holes and cones on one disk side after capping. Nullity in the abelianisation of $`\Gamma`$ forces $`a_i=t`$ for all ordinary holes and $`\eta_j\equiv t\pmod {q_j}`$. Thus $`t=0`$ or $`1`$, and one disk side has no feature. Equality to a power of one ordinary peripheral word gives the same equations at all other holes; the only nontrivial case is a once-around cone-free annulus at that boundary. These tests rule out a hidden relative-product disk through cone points. They do not assert injectivity for arbitrary orbifold words.

## 31.2. No unnoticed loop quotient at a zero block

**Lemma 31.1 (zero port winding).** For a genuine zero block, a loop of an unmarked joint annulus system has zero winding in the configuration of trace circles on each active port.

**Proof.** Take a finite power of the loop so each annulus and endpoint returns to itself. Its spanning path gives


```math
d_i^{\ell_i}w d_j^{-\ell_j}=w
```


in $`\Gamma`$, for its two distinct ends. The distinct boundary subgroups are noncommensurable. For $`b\ge3`$ this follows already from the independent rational boundary classes. For $`b=2,s\ge2`$, capping $`C_i`$ kills its subgroup and sends $`d_j`$ to an infinite-order product of all cone generators, so first $`\ell_j=0`$, then $`\ell_i=0`$. For $`b=2,s=1`$, the cyclic words of $`d_i`$ and $`d_j=(x d_i)^{-1}`$ in $`C_q*\mathbb Z`$ have different cyclically reduced syllable lengths under nonzero powers. For $`s=0,b=2`$ the block would be $`T^2\times I`$, excluded by genuine JSJ.

Thus every endpoint track has zero winding. A finite permutation of parallel copies cannot change this conclusion: taking a power multiplies the configuration winding by a positive integer. Its original winding was zero too. Actual endpoints were free throughout. ∎

## 31.3. Localising global isotopy at all tori

**Lemma 31.2 (ordinary efficient comparison).** If two efficient spanning systems with at least one zero block are ordinarily isotopic, they are related by an isotopy preserving every member of $`\mathcal T`$ setwise.

**Proof.** Arrange their parallel traces disjoint on each torus. Use the relative-product comparison of Banks Proposition 4.2, as in [Section 16](splice-vertices.md), and consider a product $`(W\times I)/\sim`$ between faces. Its intersection with $`\mathcal T`$ is a finite annulus system, or contains a whole torus. A whole torus is impossible: the product retracts to the surface $`W`$ with boundary and has free group, whereas that torus injects into $`M`$.

A returning annulus, with both ends on one horizontal face, is parallel into that face. Its two face curves cobound an annulus. The associated compressible torus in the handlebody bounds the annular parallelism solid torus; a higher longitudinal degree would make an essential simple face curve a proper power in $`\pi_1(W)`$. Straighten a finite nested system in that solid torus and choose an innermost empty parallelism. Its face annulus has no other torus trace. It is a complete cut piece parallel into the **same** JSJ torus, contradicting efficiency. This argument applies to the union of tori; it never mistakes a port-to-different-port annulus for a returning annulus.

All remaining torus annuli span the product. Straighten them simultaneously to $`\gamma\times I`$ by cutting the face into disks and using disk isotopy. Perform the product push tangent to these annuli and conjugate back. It preserves all the original tori, labels, and efficiency. Repetition gives the comparison.

The global fibred exception does not occur when a zero block is present. Its kernel contains a $`\mathbb Z^2`$: one factor is the infinite central fibre and the other is an infinite-order element of the orbifold kernel. For $`b\ge3`$ use a commutator of free boundary generators; for $`b=2,s\ge2`$ use $`x_1x_2`$; for $`b=2,s=1`$ use $`x d x d^{-1}`$. Their displayed free-product normal forms have infinite order and are killed by the zero-base homomorphism. This subgroup injects into $`\ker\Phi`$. A compact global spanning fibre would have free group, impossible.

If all blocks are zero, Lemma 30.1 makes both efficient surfaces disjoint from every JSJ torus. Take a Banks relative product region between their faces. Its horizontal faces lie in those surfaces and its uncollapsed sides lie in the actual boundary, so its whole boundary misses the JSJ collection. A connected JSJ torus meeting the product would therefore lie entirely inside it. The product retracts to a compact orientable surface with boundary and has free fundamental group. The JSJ torus group injects into the ambient manifold, so its inclusion through that free group would inject $`\mathbb Z^2`$ into a free group, impossible. Every such product region is consequently disjoint from the entire JSJ collection. Each product push fixes all those tori; finite product comparison gives the required torus-preserving ordinary isotopy. The zero-block kernel argument above excludes the global fibre exception in this branch as well. ∎

This proves an unrestricted ordinary-isotopy comparison, not just a fibred-isotopy equivalence. Parallel port packets satisfy efficiency because their ends are on different tori.
