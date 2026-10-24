# 30. Essential cuts and the structural classification

[Overview](../README.md) · [Definitions](objects.md) · [Graph-manifold theorems](graph-theorems.md) · [References](../sources/bibliography.md)

Write $`h_v`$ for the regular fibre of a Seifert block $`M_v`$, and $`k_v=\Phi(h_v)`$. Call a block zero or horizontal according as $`k_v=0`$ or $`k_v\ne0`$. All local base and wall signs are fixed by the global surface coorientation; negative Hopf pieces do not have independently reversible height conventions.

Every embedded torus in $`S^3`$ separates. Consequently the JSJ dual graph is a tree. Seifert bases here are orientable and planar: a nonorientable base would produce an embedded Klein bottle; a nonseparating base curve in positive genus would produce a nonseparating vertical torus. Both contradict the $`S^3`$ embedding. Genuine multi-block pieces are neither solid tori nor $`T^2\times I`$. In the range of Theorem 29.1 each has at least two ordinary boundary circles.

Minimise the total number of circles of a surface with the whole JSJ collection $`\mathcal T`$. The essential-cut proof of [Lemma 13.1](splice-minimal-cuts.md) applies to the collection; the details for the whole collection are as follows. Inessential circles are removed by disk/ball moves. Cut pieces inject into the original surface and into their pieces. Disks and closed cut pieces are impossible. A boundary-parallel cut annulus must have its two ends on the same internal torus, since the surface uses an actual torus only once. An innermost empty annular parallelism removes two circles. The usual primitive annuli in that parallelism are straightened as a whole finite system. Thus every cut piece is essential before applying Hatcher.

The same conclusion follows from simplified intersection with $`\mathcal T`$: the innermost annular parallelism would be a relative product. It also holds simultaneously for a finite disjoint labelled family, by minimising the count of its embedded union, not by moving its members independently.

On an actual torus the prescribed spanning slope has intersection $`|k_v|`$ with $`h_v`$.

**Lemma 30.1 (all-genus structure).** Under Theorem 29.1:

- A zero block contains only vertical annuli.
- A horizontal block contains exactly one connected horizontal piece, of degree $`|k_v|`$.
- On an edge incident to a horizontal block, the entire trace is $`q_e=\mathrm{div}(\Phi|_{T_e})>0`$ parallel coherent curves, of the primitive kernel slope.
- On an edge between zero blocks the trace is empty.

**Proof.** Horizontal essential pieces cover the whole base. In a zero block they would meet an actual torus transversely to its prescribed fibre boundary, which is impossible. In a horizontal block an actual or internal kernel slope is transverse to its fibre, so no vertical annulus can end there. Each connected horizontal piece meets every actual torus; unit usage forces just one. Its coorientation has constant sign on the fibre flow, so every port trace is coherent and has exactly its divisibility count. Between two zero blocks a nonempty trace would have to have both fibre slopes. The slopes are different in a genuine JSJ decomposition, so that trace is empty. ∎

For a zero block, $`\Phi`$ kills both its regular fibre and its cone generators; it factors through the ordinary underlying planar base. At an actual circle its degree is $`\pm1`$, by applying $`\Phi`$ to the actual meridian $`d^a h^b`$. At an active port its degree is $`\pm q_e`$; at an empty port it is zero. Cone neighbourhoods are marked and unused. The signed degrees sum to zero. A vertical annulus pairs opposite signs, hence joins **distinct** ordinary boundary circles. It may join two ports and may be parallel to other such annuli.

All whole spanning complements are connected: at an actual boundary of each component a meridian joins its two sides while missing the rest. The dual chamber graph has all edges loops and hence one vertex. The complement lifts homeomorphically in the global $`\Phi`$-cover. This proves no local connectivity assertion.

Every efficient surface has complexity


```math
N=\sum_{v:k_v\ne0}|k_v|\,(-\chi^{\mathrm{orb}}(B_v)).
```


Vertical annuli and circle gluings contribute zero; there are no disks. Compress a norm minimiser and discard closed descendants. This retains its spanning class because $`H_2(M)\to H_2(M,\partial M)`$ is zero for a link exterior. Its incompressible descendant has the displayed complexity, while an assembled surface attains it. Thus the norm is $`N`$, and every incompressible vertex is norm-minimising.

For Theorem 29.2 with a boundary-free central zero block, the active leaf traces are fibre slopes on every central boundary, so horizontal central pieces are excluded even without a central actual torus. The same annular classification and norm argument apply. If its central evaluation is nonzero, all pieces are horizontal. Their union in the centre can be disconnected, but each component meets every port. The coherent leaf trace forces all those components to have the same flow sign. The resulting coherent phase map glues to the leaves to give a global submersion in primitive class $`\Phi`$. Convex interpolation of such maps proves the all-horizontal point case, by the positive-phase construction of [Section 15](splice-horizontal-pieces.md); central connectivity is not assumed.
