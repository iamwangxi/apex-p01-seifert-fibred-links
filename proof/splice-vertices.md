# 16. Ordinary isotopy and the exact compatible vertex space

[Overview](../README.md) · [Definitions](splice-objects.md) · [Block lemmas](splice-planar-blocks.md) · [References](../sources/bibliography.md)

### 16.1. Localising efficient isotopies at the torus

We need an unrestricted-isotopy comparison, not just separate normal forms.

**Lemma 16.1.** In the mixed case, globally isotopic efficient representatives are related by an ambient isotopy preserving $`T`$ setwise.

**Proof.** The usual finite relative product-region simplification is available for incompressible, boundary-incompressible surfaces in the irreducible, boundary-irreducible link exterior. We explain why its pushes can preserve $`T`$. Arrange the two coherent traces disjoint on $`T`$. In a product region $`(W\times I)/\!\sim`$, the collapsed locus then misses $`T`$. Intersection with $`T`$ consists of proper annuli, since the trace cuts the torus into annuli. A whole $`T`$ cannot lie inside: $`W`$ has boundary, so the product-region group is free, whereas its injected torus group is $`\mathbb Z^2`$. Annulus cores are nontrivial for the same injection reason.

Here are the elementary product-annulus facts. In $`W\times I`$ an annulus returning to one horizontal face is parallel into that face. Its two curves cobound a face annulus; their union with the returning annulus gives a compressible torus in the handlebody. It cannot lie in a ball because its core is nontrivial. It bounds a solid torus whose annular slope has longitudinal degree one: a higher degree would make an essential simple curve a proper power in $`\pi_1(W)`$. The primitive-annulus disk argument then provides an innermost empty parallelism, with no other annulus trace in the face subannulus. If all annuli span, their lower and upper curve systems are isotopic; cut $`W`$ into disks, straighten the spanning intersections in the product disks, and apply relative disk isotopy in the remaining balls. This makes the annuli $`\Gamma\times I`$, including their matching permutation. Trim away collapsed boundary collars to apply the same argument to the relative product.

A returning $`T`$ annulus would yield a complete annular cut piece of one surface parallel into $`T`$, contradicting efficiency. All annuli therefore span. Straighten them in product coordinates, perform the usual push tangent to $`\Gamma\times I`$, and conjugate back. This gives a push preserving the original $`T`$, with the usual strict intersection reduction. It preserves efficiency, since it restricts to isotopies in the fixed pieces.

The fibre-bundle exception to the parallelism procedure cannot occur here. In the zero block the kernel contains $`\langle h,[d_1,d_2]\rangle\cong\mathbb Z^2`$, and this subgroup injects into $`\ker\Phi`$. A compact global fibre with actual boundary has free fundamental group. Thus $`M`$ does not fibre in this spanning class. Iterating the $`T`$-preserving product moves identifies corresponding isotopic components and finishes at the target. The product-annulus comparison uses the common slope and efficiency; it does not require balanced JSJ signs. ∎

### 16.2. The mixed vertex model and twist quotient

Let $`P`$ be the zero block. Let $`\mathcal A(P,\sigma,q)`$ consist of joint ordinary proper multiarc isotopy classes on $`B_P`$ with:

- one end on each actual circle, with its sign $`\sigma_j`$;
- $`q`$ ends, all of sign $`\sigma_J`$, on $`J`$;
- each arc joining opposite signs, and endpoints free on their own labelled circles.

There are no $`J`$-to-$`J`$ arcs. A class has $`q`$ reaching arcs and $`(n_P-q)/2`$ actual-to-actual arcs. Embedded joint diagrams are required; a mere list of endpoint counts or words is not a validity certificate.

**Theorem 16.2.** In the mixed case inverse image and horizontal assembly induce a bijection

```math
V(X(L))\cong\mathcal A(P,\sigma,q).
```

**Proof.** Verticalise the entire zero-side annulus system. Successively cut actual-to-actual arcs between unused circles and reaching arcs from an unused actual circle to the boundary containing $`J`$; each cut remains connected. Boundary-relative verticalisation fixes earlier cut faces. In a product, an arbitrary ambient annulus isotopy gives an equality of endpoint peripheral double cosets after quotienting its group by the fibre. This is ordinary proper-arc homotopy in $`\pi_1(B_P)`$. Ordinary homotopy-isotopy and joint straightening recover the joint unmarked diagram, including cyclic order at $`J`$.

For fixed collared trace $`\beta`$, the exact compatibility objects are a port-marked zero-side diagram and a horizontal piece in $`Q`$ with opposite cut boundary $`g\beta`$. Lemma 15.1 says the latter relative class is unique. Any boundary motion in a diagram isotopy extends to $`Q`$ in a collar, and its final horizontal piece is returned to the chosen relative class by Lemma 15.1. Conversely Lemma 16.1 restricts a global ordinary isotopy to compatible piece isotopies and common boundary motion. Thus taking the quotient by paths of compatible pairs is exactly ordinary unmarked diagram isotopy. The phase return described in Section 15 kills the port-rotation winding; no gluing parameter is being discarded without comparison.

Every allowed diagram actually assembles. Its annuli are essential and its horizontal mate is essential. Gluing essential pieces along an incompressible torus gives an incompressible surface: minimise a hypothetical compression disk's intersections with the torus; remove closed intersections, and use an outermost arc to contradict boundary-incompressibility or to decrease the intersection. Eventually the disk would compress a piece. Every component reaches actual boundary, since there are no returning $`J`$ arcs. This gives surjectivity and completes the comparison. ∎

In the double-zero case the vertex space is the product of the two unit matching spaces, with both $`J`$ circles unused. An arbitrary global annulus isotopy is detected by a spanning path whose two actual ends remain in the same factor of $`G_P*_{G_T}G_Q`$. Factor injection, then quotient by the fibre, recovers the ordinary local arc classes. Thus there is no extra global quotient, for all actual counts, using Lemma A.2 in [the planar-block appendix](splice-planar-blocks.md).

If both fibre values are nonzero, there is one vertex. To see this directly, make the coherent trace common and straight, and choose fibre-monotone circle maps for both block pieces, standardised to the same boundary phase map $`f_T`$ on the common collar. A monotone degree-$`q`$ function of the transverse $`\ell`$ coordinate has the required strict derivative sign for both fibres; it may be linear when the ports are equally spaced. The maps glue to a global fibration in class $`\Phi`$. For any two such maps their difference lifts to a real function on $`M`$, normalised to zero on that collar. Convex interpolation is strictly of sign $`k_i`$ along the fibre in each block, remains a submersion on $`T`$, and keeps the actual boundary restriction primitive. Its zero fibres are ambient isotopic. This proves the point statement without a general graph-manifold contractibility theorem.
