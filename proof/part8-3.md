# Part 8. The square-knot tree and recursive graph-knot double parallels (continued)

[Overview](../README.md) · [Previous page](part8-2.md) · Part 8, page 3 of 3

## 12. A further contraction for parallel families with capped fibres

The tree argument uses exactly two actual boundaries. There is a second extension that allows an arbitrary number of parallel actual components, provided every companion piece is a one-boundary fibre. Its reduction is different and is stated separately.

Let $`L_{\boldsymbol\varepsilon}(K)`$ be $`m\ge2`$ zero-framed parallels of $`K\in\mathcal G`$, with signs $`\varepsilon_j\in\{+1,-1\}`$, and put $`a_0=\sum_j\varepsilon_j`$. Its pattern is $`S^1_\lambda\times B`$, with $`B`$ a sphere with $`m+1`$ boundary circles; one is the companion port. As before it is an actual non-split graph-manifold link. Use the complete ordinary reduced all-incompressible vertex set.

**Theorem 12.1 (capped-fibre parallel families).** Suppose either

1. $`a_0\ne0`$; or
2. the finite mode recursion (11.1) for $`K`$ has no zero-slope mode containing a vertical terminal.

Then $`Y(L_{\boldsymbol\varepsilon}(K))`$ is contractible. With the general comparison of Part 7, Theorem D, $`X`$ is contractible as well. In particular this closes the full complex for the three trefoil parallels with signs $`(+,+,-)`$ from Part 7, §8.4. Case (2) also handles all orientations of parallel families of iterated cable torus knots, and of other companions having no cancellation mode.

The $`Y`$ assertion below is independent of Part 7, Theorem D. The invocation of D is confined to the last sentence about $`X`$; the tree theorems above do not acquire this dependency.

### 12.1. The exact partial-matching model

The global spanning class on $`Q=E(K)`$ is $`a_0\psi`$, where $`\psi`$ is the primitive knot class. Its value on the regular fibre of every composing, cable or torus-knot block is nonzero when $`a_0\ne0`$: the respective evaluations are a nonzero winding multiple of $`1`$, $`pq`$, or the torus-knot fibre product. Hence no efficient cut in $`Q`$ can be vertical. All companion pieces are jointly parallel one-boundary spanning fibres of $`K`$, with their individual signs retained. Under hypothesis (2), the longitudinal mode classification gives the same conclusion even when $`a_0=0`$.

Pattern pieces are vertical annuli. An outer-to-outer return would join two one-boundary companion fibres and make a forbidden closed component. Thus every pattern arc either joins two oppositely oriented actual holes, or joins one actual hole to the companion port. Every actual hole is used exactly once. Conversely every such oriented partial matching gives an incompressible spanning system: actual-to-actual annuli inject through the pattern fibre, and each tethered fibre is just a companion fibre with a boundary collar.

These ordinary multiarc classes give precisely the ordinary spanning classes. The outer-torus product comparison applies since all its traces have slope $`\lambda`$. The distinct-end vertical-annulus detector identifies the ordinary pattern multiarcs, with their joint endpoint order. Conversely, follow a whole multiarc isotopy's actual path of outer endpoints by the corresponding companion fibre phases. The matching collar motions give a whole isotopy, and a common full phase circuit absorbs outer winding. There is no extra relative torus-spin coordinate at this single port. This is the many-tether version of the compatible-path argument, not an assumption of fixed boundary curves.

Choose a negative-curvature metric with geodesic boundary on $`B`$. Each ordinary essential arc class with free boundary endpoints has its orthogeodesic representative. Disjoint classes have disjoint cores, and parallel occurrences have the same core. Two different orthogeodesics cannot have the same endpoint on a boundary circle, since the perpendicular initial direction would then be the same. Extend each companion endpoint to the fibre at that phase of a fixed bundle map $`f:Q\to\mathbb R/\mathbb Z`$. Thus a finite collection of vertices has canonical arc representatives, and every geometric simplex among them is represented by disjoint whole components after restoring parallel copies of shared cores.

### 12.2. Finite band maps with a harmless closed-component deletion

Fix a finite subcomplex $`K_0\subset Y`$ and a base vertex $`s_*`$. Take the finite arrangement of their orthogeodesic arc cores. Choose sufficiently narrow piecewise linear bands so that bands for disjoint distinct cores are disjoint, and use the same profile on a shared core. In $`Q`$ use the corresponding fibre-phase bands. For every vertex $`s_i`$ this gives a Thom map

```math
f_i:M\longrightarrow\mathbb R/\mathbb Z
```

representing the spanning class, with

```math
f_i|_Q=g_i\circ f,
\qquad \deg(g_i)=a_0.
\qquad\text{(12.1)}
```

The map on the pattern factors through $`B`$. Each actual boundary has one monotone band with its fixed sign. A component shared by two inputs has one common band profile. Choose real equivariant lifts $`F_i`$ on the single global spanning cover. For $`x=\sum_i\lambda_i[s_i]\in|K_0|`$ and $`t\in[0,1]`$, form

```math
F_{x,t}=(1-t)\sum_i\lambda_iF_i+tF_*.
\qquad\text{(12.2)}
```

It has the original deck displacement one. On $`Q`$ its descended map still factors through $`f`$ as a degree-$`a_0`$ circle map. Indeed the differences between the lifts in (12.1) are periodic real functions of the same fibre phase, with the constants inherited from the connected global construction. No separate deck constants are assigned to companion pieces.

A generic level has one boundary on every actual torus, since its boundary map there is a convex combination of monotone maps with total signed degree $`\varepsilon_j`$. Its pattern part consists of arcs and circles; its companion part consists of whole one-boundary fibres. Delete every closed component of the resulting level surface. The retained components are exactly:

* an actual-to-actual vertical annulus, with distinct actual ends; or
* one companion fibre extended by one actual-to-outer annulus.

An outer-to-outer arc only joins two one-boundary fibres to a **whole closed component**, so deleting it does not remove any actual boundary. A closed pattern circle also gives a whole closed component. No compression choices are involved. Every retained component is incompressible by the injections in §12.1, and their actual boundaries and orientations are unchanged.

For fixed $`(x,t)`$ choose one generic phase in every nonempty phase interval and average the ordinary vertices of these reduced levels by the interval lengths. The result, denoted $`Q(x,t)`$, is a point of $`|Y|`$: all these representatives are levels of the same map before the closed components are discarded, and remain simultaneously disjoint afterwards.

### 12.3. Continuity and the initial carrier

Use one finite PL template for the bands and their intersections on $`B`$, and one finite template on the fibre-phase circle. The lifted corner values in (12.2) are affine functions of the finitely many coefficients and remain bounded. Only finitely many integer-translated critical values and finitely many level patterns can occur. Between consecutive critical phases the reduced arc/fibre pattern has a fixed ordinary isotopy class. When two critical phases meet, the corresponding phase interval has length tending to zero. Thus the average $`Q`$ is continuous, with finite image support on each closed simplex cylinder, including coefficient-zero faces. Closed-component deletion changes the chosen class of a level, but does not change this finite-pattern and vanishing-interval argument.

At $`t=0`$, on a true input geometric simplex the bands are disjoint or shared whole-component bands. Every generic weighted level is consequently a union of entire input component classes. After choosing sufficiently close parallel copies, its representatives are disjoint from **all** input representatives as well as from each other. Therefore

```math
(1-u)x+uQ(x,0),\qquad 0\le u\le1,
\qquad\text{(12.3)}
```

stays in a genuine geometric carrier. These initial carriers agree on coefficient-zero faces, because the same finite set of maps $`f_i`$ was used throughout $`K_0`$. At $`t=1`$, all reduced levels are the base vertex, so $`Q(x,1)=[s_*]`$.

Concatenating (12.3) with $`Q(x,t)`$ nullhomotopes the inclusion of every finite subcomplex into $`Y`$. The same construction connects vertices to the base vertex. Compact sphere images lie in finite CW subcomplexes, so all homotopy groups vanish; the CW Whitehead theorem gives contractibility. The band widths, lift constants and PL templates need only agree on common faces inside one finite $`K_0`$; different finite subcomplexes need not use compatible choices, and no choice-independent global retraction formula is constructed. This proves the $`Y`$ assertion. Part 7, Theorem D, then gives the stated $`X`$ assertion.

This argument works because every outer return at a generic level closes up using two one-boundary fibres. For a cancellation companion with multi-boundary pieces, the same deletion would not be valid; no such extension is being asserted.

## 13. Relation to the full graph-manifold problem

The mechanism has three concrete ingredients:

1. every companion component in a connected spanning vertex has two outer boundaries;
2. the pattern returns are bridges separating the two actual boundaries;
3. every disjoint family has a common parallel companion packet, so the auxiliary arc model has only two unused holes.

These hold for the connected-sum family in Theorem 1.1 and, by the repeated-word argument of §11, for every opposite double parallel in the recursive class $`\mathcal G`$.

For a general graph link, this part does not establish a two-boundary companion classification, a separating-return property, or a two-ended common packet. These are precisely the inputs needed to reuse the tree proof. More general horizontal components, return networks and end-region configurations still require a compatible reduction; no such general reduction is proved here.

The simplest family beyond these inputs is already among parallel families; [Part 9](part9.md) proves its contractibility, together with all zero-framed parallel clusters of connected sums of torus knots. Take four zero-framed parallels of the square knot, with signs $`(+,-,+,-)`$ in their outer tether order. Use four composing sections with that sign word. At the positive trefoil leaf use the matching $`i\mapsto1-i`$ modulo four, and at the mirror leaf use $`i\mapsto3-i`$. Both reverse the alternating signs. Their union is the connected four-cycle with edges

```math
\{0,1\},\ \{2,3\},\ \{0,3\},\ \{1,2\}.
```

Attach one pattern tether from each section to its correspondingly signed actual component. All pieces are essential, so essential assembly gives a connected incompressible spanning surface. Its four pants have Euler characteristic $`-4`$; with four actual boundaries it has genus one. Its companion piece also has genus one and **four** longitudinal outer boundaries. This is an actual non-split graph link, and the construction uses the same genuine square-knot blocks, with the four-actual-hole pattern replacing the two-actual-hole pattern.

The period-two sign word allows the leaf offsets to differ by two. The two-defect contradiction of Lemma 3.1 is absent. Thus this surface cannot be treated as a path of two-boundary companion pieces. It also explains the limitation of §12: an outer return attached to a multi-boundary companion piece need not close up to a whole closed component, so the harmless deletion argument is unavailable. No noncontractible subcomplex or nonzero homology class is claimed for this four-parallel example.

The tree result and Theorem 12.1 can therefore be combined with the anchored-cluster theorem; they also contain the iterated-cable double-parallel theorem and the unanchored three-parallel control. There is no assertion that their union covers every graph link, and no asserted closure under arbitrary JSJ gluing of links with several independent actual-boundary patterns.

## 14. Sources, verification, and exact limits

| Source | Exact use |
|---|---|
| Hatcher, *Notes on Basic 3-Manifold Topology*, Lemma 1.11, Proposition 1.12 and the following horizontal-product discussion, printed pp.20–23 | Essential cut pieces; vertical/horizontal normal form; primitive horizontal product |
| Banks, arXiv:1109.0965v1, Proposition 4.2 and Remarks 4.3–4.4 | Ordinary incompressible product-region comparison in Lemma 4.1 |
| Banks, same paper, Proposition 4.10 and the explicit extension immediately following Definition 10.1 | Simplified all-incompressible representatives attain cyclic class width |
| Banks, same paper, Proposition 2.4 with the corrected cyclic convention and its explicit §10 extension | Equality of cyclic class distance and graph distance in (9.1) |
| Lemma 31.2 | Checked model for the product-annulus straightening; the actual outer-torus proof is written in §4, with its common-slope hypothesis explicit |
| Lemma 2.4 (fibred point and product) and the compatible-phase argument of Part 6 | Uniqueness of the capped pair; no theorem about all signed graph-manifold surfaces is inferred from it |

The square-knot mode calculation agrees with Part 7, §8. Its needed structural facts have been derived again here. Part 7, Theorem D, Sakuma Proposition 4.9's simultaneous-union uniqueness, a taut PS projection outside its range, and any all-genus compression-choice theorem are not dependencies of the tree proof. The final $`X`$ conclusion of Theorem 12.1 uses Part 7, Theorem D, explicitly; its $`Y`$ contraction does not. The ordinary distinct-end annulus detector used in §12 is the result of Section 31, now applied to a planar pattern with one companion hole.

The diagnostic `scripts/part8_checks.py` verifies finite matching rigidity, reduced connectivity, signs, the parent suffix and the root-distance arithmetic, as well as exact normal-data examples. These tests do not prove the ordinary product comparison, the lifted rectangle argument, or the general topological theorem. Those are the proof obligations in §§4–8.

[Overview](../README.md) · [Previous page](part8-2.md)
