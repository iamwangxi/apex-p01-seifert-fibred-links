# 19. Exact compatibility complexes and the fixed-support carrier

[Overview](../README.md) · [Definitions](splice-objects.md) · [Block lemmas](splice-planar-blocks.md) · [References](../sources/bibliography.md)

Theorem 16.2 and Theorem 18.1 specify a full compatibility **complex**, not just a vertex space. In the mixed case take $`\mathcal A(P,\sigma,q)`$, join distinct vertices when $`\mathrm{osc}(H_P)=1`$, and flag-complete. This complex is simplicially and metrically isomorphic to $`X(L)`$. The double-zero case uses the product vertex set and the common-root union formula. The nonzero/nonzero case is a point.

A local normal crossing forces width at least two. Cap all used boundary circles by radial stars and treat crossings as graph vertices. The $`a-b`$ current is conserved at actual vertices and also at $`J`$, since both systems have the same integer demand $`q`$ there. Its spherical face potential has jumps +1 on $`a`$ and -1 on $`b`$, and restricts to the complete-$`b`$ potential by connectedness. At a crossing the four sector values give three consecutive indices. Thus true global simplices have noncrossing canonical ordinary arc representatives in the zero block.

For the mixed case let $`G`$ be a finite allowed embedded bipartite multiarc graph containing an allowed system. Actual vertices have demand one; $`J`$ has demand $`q`$ and its fixed sign. Edges are distinct ordinary proper classes. There is no $`J`$-to-$`J`$ edge, and **every edge has a unit-demand actual endpoint**. Set

```math
P_G=\{w\ge0:\ \sum_{e\ni j}w_e=1\text{ at every actual }j,\quad
\sum_{e\ni J}w_e=q\}.
```

In particular $`0\le w_e\le1`$, despite the nonunit demand at $`J`$. Direct edges negative to positive. For connected spherical regions use
$`(Du)_e=u_{\ell(e)}-u_{r(e)}`$. Radial capping does not merge old open regions; an unused auxiliary cap only fills a hole of its own region. All unused cone/JSJ marks are retained in ordinary arc identity.

**Theorem 19.1 (compatible flow decoder).** In the mixed case the supported global subcomplex triangulates $`P_G`$. Its decoder is

```math
w=m+Du,\qquad
m^\theta=m+D\lfloor u+\theta\rfloor,\qquad
S_G(w)=\int_0^1[M_\theta]\,d\theta,\qquad 0\le\theta\lt1.
```

It is continuous, reference- and root-independent, commutes with deleting zero edges, and exactly recovers every true simplex. In the double-zero case the corresponding supported subcomplex triangulates $`P_{G_P}\times P_{G_Q}`$, using the two JSJ root regions as one root and **the same** threshold on both blocks.

**Proof.** Every circulation on a spherical embedded graph is $`Du`$: fundamental cycles of a spanning forest have Jordan left-side potentials. The dual graph across all edges is connected even if the primal graph is disconnected or regions are not disks. The kernel is one common constant, and integral circulations have integral root-zero potentials. Demand equality makes $`w-m`$ a circulation, including at the multiple vertex.

The integer-endpoint bounds

```math
-m_e\le u_\ell-u_r\le1-m_e
```

are preserved by a common floor shift. Thus every rounded edge is zero or one. Sector telescoping preserves each prescribed incident sum, including the integer $`q`$ at $`J`$. The outputs are legal annular diagrams, with no returning arc. Between two ordered thresholds the difference potential takes only zero and one. Theorem 18.1 gives global class distance at most one. In the double-zero case the joint root-zero difference is binary on both blocks, and its union range is at most one. Flagness gives a true output simplex.

Changing reference subtracts an integral potential and cancels pointwise in the floor formula. In the mixed case changing root adds one real constant, rotating the threshold circle and preserving the barycentric integral. In the double-zero case only a **common** shift of the two roots is allowed.

Potentials are affine and bounded on the compact flow polytope. The finitely relevant hyperplanes $`u_f=k`$ and $`u_f-u_g=k`$ fix floor outputs and cyclic threshold order. Interval lengths are affine on their cells; colliding intervals have vanishing weight. This proves continuity into a finite realisation.

If $`w_e=0`$, every threshold output omits the edge. Change to a supported rounded reference; its potential jump on that edge is zero. Deleting it merges only equal-potential regions, with the full range unchanged, so decoding agrees. Distinct graphs agree on their common positive-support coordinate face, even when deleted edges cross. Bridges, disconnected graphs and non-disk regions cause no extra constant.

For a true simplex the integral root-zero potentials have pairwise oscillation at most one. Every difference is entirely in $`\{0,1\}`$ or entirely in $`\{-1,0\}`$, so they form a coordinatewise chain. Use its minimum as reference: all potentials are nested zero-one vectors. A coordinate first appearing at index $`j`$ has value $`\sum_{i\ge j}\lambda_i`$ in the averaged flow. Common rounding outputs vertex $`j`$ for exactly length $`\lambda_j`$. Hence

```math
S_G\left(\sum_j\lambda_j\chi_{A_j}\right)=\sum_j\lambda_j[A_j].
```

The identity $`\int_0^1\lfloor u+\theta\rfloor\,d\theta=u`$ gives the inverse edge expectation. Thus the affine edge map and the decoder are inverse homeomorphisms. The ordinary vertex bijection ensures that distinct supported indicators are distinct global vertices. ∎

This proof is not a general theorem for arbitrary nonunit graph factors. Its capacity bound comes from the unit actual end of **every** edge. Coherent trace is what excluded $`J`$-to-$`J`$ edges and made this extension possible.
