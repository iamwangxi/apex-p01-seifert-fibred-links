# 27. Strong deformation retraction for two-block splice exteriors

[Overview](../README.md) · [Geometric criterion](splice-trace-criterion.md) · [Restricted rounding](splice-trace-rounding.md) · [Cyclic contraction](splice-contractibility.md)

**Theorem 27.1.** In the two-block family of Section 12, including Corollary 21.1, the geometric complex $`Y=IS(L)`$ is flag, $`X\subseteq Y`$, and $`|X|`$ is a strong deformation retract of $`|Y|`$. Consequently $`Y`$ is contractible. The mixed branch uses trace-constrained carriers; the empty-trace branch uses matching-pair carriers with one common threshold; the double-horizontal case and the low cable case on the zero side are points.

## 27.1. Retraction, common faces and the weak topology

For $`x=\sum_{M\in\sigma}\lambda_M[M]\in|Y|`$ in the mixed branch, use the canonical common graph of the geometric simplex $`\sigma`$ and set

```math
W(x)=\sum_{M\in\sigma}\lambda_M\chi_M,\qquad
R(x)=S_G(W(x))\in|X|.
```

This is exactly the decoder of Theorem 19.1, now applied on the trace-constrained geometric simplices. By Theorem 25.2 and Lemma 26.1 it is legal.

All incidence vectors are nonnegative. A zero-flow edge is used by no positive-coefficient input vertex. Removing zero coefficients therefore deletes precisely these unused edges. Theorem 19.1 identifies the decoders on the resulting zero faces, independently of the matching reference and root. Two containing simplices both reduce to this same positive-support graph. Their extra deleted edges may cross; no common noncrossing supergraph is asserted. Ordinary joint straightening removes the drawing choice.

One can also see directly that the trace condition survives deletion. Choose a supported reference. The jump across a deleted edge is zero for every positive input potential. Any merged sectors therefore have the same values on the entire input chain; projecting to the new sector list preserves nesting and the decoder's restriction. There is still one common potential constant, not a free offset for every port or block.

On each closed simplex $`|\sigma|`$ the map $`W`$ is affine into a fixed finite polytope and $`S_G`$ is continuous into a finite cyclic subcomplex. The restrictions agree on faces, so the weak topology makes $`R:|Y|\to|X|`$ continuous. For $`x\in|X|`$, use its true $`X`$ simplex in the formula. Theorem 19.1's **exact simplex recovery** gives

```math
R(x)=x.
```

Identify $`|X|`$ with its simplicial-subcomplex image in $`|Y|`$ and define

```math
H(x,t)=(1-t)x+tR(x).
```

For a fixed input simplex, Lemma 26.1 puts the input vertices and all decoder vertices in the one finite geometric simplex $`\Delta(G,\mathcal C)`$. The displayed segment therefore stays in $`|Y|`$. It need not stay in the original input simplex or be carried by all matchings of $`G`$.

On every $`|\sigma|\times I`$ its finite barycentric coordinates are continuous. These cylinder restrictions agree on overlaps. The CW closed-cell-cylinder criterion in [Hatcher, Algebraic Topology](../sources/bibliography.md#hatcher-circle-map-method-and-cw-conclusion), printed p.523 (and Theorem A.6, p.524), makes $`H`$ continuous for the **ordinary product topology** on $`|Y|\times I`$. Subcomplexes have their induced CW topology, [Hatcher, Algebraic Topology](../sources/bibliography.md#hatcher-circle-map-method-and-cw-conclusion), p.520. No local finiteness, metrisability or countability is required. We obtain

```math
H(x,0)=x,\qquad H(x,1)=R(x),\qquad
H(a,t)=a\quad(a\in|X|).
```

This proves the strong deformation retraction in the mixed branch. The edge-expectation identity also gives

```math
W(H(x,t))=W(x),\qquad R(H(x,t))=R(x).
```

For a fixed image point $`p\in|X|`$, every point with flow $`w=W(p)`$ has the same positive-support graph. For any geometric decomposition of $`w`$, chain recovery on the restricted potentials says that its weighted distribution of reaching-edge patterns is exactly the distribution given by restricted common rounding. The latter depends only on $`w`$. Thus every such decomposition has the same set $`\mathcal C_w`$ of positive-weight trace patterns. All these decompositions belong to the single finite simplex $`\Delta(G_w,\mathcal C_w)`$. Since $`R(x)=p`$ is equivalent to $`W(x)=w`$ by edge expectation and exact recovery, the fibre is its convex matching-decomposition polytope, contracted linearly by $`H`$. This refinement is not needed for the main theorem.

## 27.2. Empty trace, double horizontal pieces and the cone extension

In the double-zero branch, Lemma 23.1 makes a whole geometric simplex miss $`T`$. Each block supplies a unit-demand noncrossing graph $`G_P,G_Q`$, with its JSJ circle unused. All pairs of matchings of these two graphs are simultaneously geometrically realisable: allocate one separate parallel copy of every edge occurrence in its own block. There is no horizontal trace condition to impose. Ordinary paired vertices and their assembly are those of Section 16.

Use Theorem 19.1 on $`P_{G_P}\times P_{G_Q}`$, with the two JSJ regions identified as one root and with **one common threshold**. True $`X`$ simplices have the common-graph property by the crossing obstruction, and hence lie in $`Y`$. The barycentric flow, zero-face argument and straight-line homotopy of Section 27.1 now apply in the geometric simplex of all matching pairs. Independent root shifts or independent rounding on the two sides are not used. This proves the same strong deformation retraction.

When both fibre values are nonzero, Section 16 proves that the **whole vertex set** is a singleton. The vertex definition is unchanged, so $`Y=X`$ is that point, even though its representatives have nonempty trace.

For a retained cone on the zero side, remove its fixed neighbourhood, keep the auxiliary circle unused, and apply the same graph and trace analysis at the ordinary JSJ boundary $`J`$. Section 21 supplies the ordinary-isotopy detection and carrier, including port order. All arcs still have an actual unit end. Cone capping is only for the circulation calculation and never identifies proper classes. The simultaneous block argument of Lemma 23.2 includes the local model. The low coned block with only one actual circle is the already established singleton with $`q=1`$ and needs no closing-curve argument.

For a cone on the horizontal side, the horizontal interval complement, primitive class and regular-fibre degree used in Lemma 24.1 are precisely those of Section 21. Ordered collar extension stays in the ordinary boundary charts and extends constantly toward the exceptional orbit. Thus the trace criterion and restricted rounding are unchanged. Local Seifert coefficients are denoted $`\beta`$ when needed, as distinct from the gluing-matrix entry $`c`$; no unintended coprimality between that matrix entry and the cone order is imposed.

Finally, in every branch compose the retraction with the established contraction of $`X`$. This proves contractibility of $`Y`$ throughout exactly the requested two-block and one-cone family.
