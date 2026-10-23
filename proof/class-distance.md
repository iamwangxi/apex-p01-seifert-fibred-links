# 5. Peripheral detection and exact class distance

[Overview](../README.md) · [Definitions](objects.md) · [References](../sources/bibliography.md)

## 5.1. Jordan curves and arbitrary peripheral powers

The detection lemma is uniform in the number and orders of the retained cones. Its proof uses the actual orbifold abelianisation; it does not replace all homotopy questions by homology.

**Lemma 5.1 (Jordan and peripheral detection).** Assume $`n\ge2`$ and all $`q_j\ge2`$. A regular embedded Jordan curve null in $`\Gamma`$ bounds a disk with no cone or actual boundary. If its conjugacy class belongs to $`\langle d_i\rangle`$, it either bounds such a disk or cobounds a cone-free annulus with $`C_i`$.

**Proof.** The abelianisation has generators $`d_1,\ldots,d_n,x_1,\ldots,x_s`$ and relations

```math
q_jx_j=0,\qquad \sum_i d_i+\sum_jx_j=0.
```

After capping the actual holes, take a disk side of the Jordan curve. Write $`a_i\in\{0,1\}`$ for whether it contains the $`i`$th actual hole and $`\eta_j\in\{0,1\}`$ for whether it contains the $`j`$th cone. Up to the common orientation sign, its class is

```math
v=\sum_i a_id_i+\sum_j\eta_jx_j.
```

If $`v=0`$, there is an integer $`t`$ such that $`a_i=t`$ for all $`i`$ and $`\eta_j\equiv t\pmod {q_j}`$ for all $`j`$. The actual coefficients force $`t=0`$ or $`1`$. Since $`q_j\ge2`$, the cone indicators must then equal $`t`$, not just be congruent to it. Either this side or the other side is an ordinary empty disk.

If $`v=rd_i`$, all actual coefficients away from $`i`$ must equal the same $`t`$; there is at least one such coefficient because $`n\ge2`$. Again $`t\in\{0,1\}`$ and every $`\eta_j=t`$. The remaining equation is $`r=a_i-t\in\{-1,0,1\}`$. Thus the chosen side is empty, contains just $`C_i`$ with no cone, or is the complementary version of one of these. These are exactly the disk and cone-free annulus alternatives. Conjugacy has no effect on the abelianisation. These are necessary consequences of a full group equality; no sufficiency assertion about arbitrary words has been made. ∎

This simultaneously handles two cones and every possible order, including order two. A disk containing either cone, or both cones, is not an empty bigon. The argument does not require their orders to be equal or a matching endpoint at a cone.

## 5.2. Normal position and relative product regions

Put two allowed systems in ordinary normal position on $`P`$: common proper classes coincide, other intersections are transverse, other boundary endpoints are disjoint, and there are no ordinary bigons or boundary half-bigons. In non-point cases $`\chi(P)\lt0`$. Fix a hyperbolic metric with geodesic boundary, constructed by gluing hyperbolic pairs of pants. In the universal cover a proper class between two specified boundary lifts has a unique common perpendicular. These orthogeodesics are embedded for simple classes, and disjoint classes have disjoint representatives, by the arc bigon and half-bigon criterion. An equal boundary endpoint and perpendicular tangent would force equality of the full geodesics; hence different classes have distinct boundary endpoints. Copy common classes once and take a sufficiently small simultaneous rational PL approximation. This gives the stated position, including endpoint-free half-bigons.

**Lemma 5.2 (simplified intersection).** The inverse-image vertical systems of such a normalised pair have simplified intersection in the relative PS §3 sense.

**Proof.** Transverse intersections are whole regular fibre circles. Distinct boundary fibres are disjoint, while a coincident boundary fibre cannot enclose an embedded boundary disk with itself. Thus there is no boundary product disk.

For a noncommon annular pair, the horizontal faces of a relative product region have frontier in whole intersection fibres and original boundary fibres. Each connected face is a fibre subannulus. Its interior cannot contain an additional transverse intersection: the other surface would then enter the product interior, contrary to its definition. Follow a spanning section of the face through the product and pass to $`\Gamma`$. With two interior ends the projected subarcs give a null Jordan curve, hence an ordinary empty bigon by Lemma 5.1. With one actual boundary end, the two subarcs give a return arc to some $`C_i`$. Closing it by a boundary interval gives a peripheral power, allowing arbitrary winding of the endpoint track. On the disk side excluding $`C_i`$ one has $`a_i=0`$. Lemma 5.1's equations force either no other feature on that side, or every other feature there. One of the two boundary intervals therefore gives an ordinary empty half-bigon. Both possibilities contradict normal position. With two boundary ends, the full arcs have the same two distinct actual ends and the same orbifold double coset. Theorem 4.1 identifies their ordinary classes, already common rather than noncommon.

A common annulus is disjoint from the other components, none of which uses its end tori. A product with one common face and one noncommon face would need the whole common annulus and the same two labelled tori on the other face, impossible. Two product faces within the same common annulus cannot have an uncollapsed side, since it would use the same single actual boundary circle as distinct product ends. If all sides collapse, their frontiers and original-boundary collar memberships agree. The mod-two difference of their characteristic functions is locally constant on the annulus and zero near its boundary, so the faces coincide, incompatible with an embedded product. This accounts for every common-component case, independently of $`m,s,q_j`$.

The uncollapsed vertical sides being in $`\partial E`$ is essential throughout. It is the relative convention explicitly stated by Oertel and used in PS §3; an arbitrary Seifert solid-torus chamber is not declared to be a product. ∎

All spanning annuli have minimal norm zero and are essential. The exterior is orientable, irreducible and boundary-irreducible. The prescribed curve on each torus is primitive and nonseparating there; $`\partial\alpha=[\gamma]`$, and the absolute-to-relative second-homology map is zero for a link exterior. Thus the PS setup and the actual position hypotheses of Proposition 3.2 hold. In the non-point cases,

```math
\delta([F_a],[F_b])=D(F_a,F_b).
```

For the two point cases of §3.5 choose coincident representatives; the class distance is zero. This supplies class minimality in all cases without appealing to PS's projection or contractibility conclusions.

## 5.3. Complete complementary blocks and the class-distance formula

**Theorem 5.3.** For two normalised allowed systems $`a,b`$, let the vertices of a signed graph be the connected open regions of $`P\setminus(a\cup b)`$. Across every segment of $`a\setminus b`$ put a unit edge in its positive coorientation. Do not cross $`b`$, and give a common arc no internal edge. There is a unique integral potential $`H`$ up to one global constant, and

```math
\delta([F_a],[F_b])=\max H-\min H.
```

**Proof.** Cut the entire base along the $`m`$ arcs of $`b`$. Each joins two different previously unused actual boundary circles, so every cut preserves connectedness. The ordinary filled cut base has $`m`$ boundary circles and Euler characteristic $`2-m`$, and retains all $`s`$ cones. The cut $`P`$ has $`m+s`$ boundary circles and Euler characteristic $`2-m-s`$. The whole three-dimensional complement is a connected Seifert space over that entire cut base. For $`m=1,s=1`$ its completion is a model solid torus; for $`m=1,s=2`$ it has disk base with two cones. Neither is incorrectly replaced by a circle product.

Every allowed matching represents the same $`\psi`$: its actual peripheral intersections are $`\epsilon_i`$ and its auxiliary peripheral intersections are zero, and these loops generate planar first homology. Every loop in the complete $`b`$ complement has zero $`\psi`$. The pullback description in §2.5 therefore gives a homeomorphic lift of the **entire connected** $`E\setminus F_b`$ into the cyclic cover. All choices differ by one common deck translation.

The signed region graph is connected, by paths in this complete base complement. Its loop step sums are intersections with $`a`$ of loops disjoint from $`b`$, hence zero $`\psi`$. Integrating the unit steps defines $`H`$ with just one constant. In the chosen whole $`b`$ block, crossing a positive $`a`$ wall changes the complete $`a`$-block index by one, so these indices are exactly $`H`$. Each region has nonempty interior and attains its index. Conversely every open-block intersection contains a point away from both surface systems and hence belongs to a listed region. Pure frontier contact gives no index.

Filling an auxiliary cone disk fills one hole of its one region, with no region merger. Its fibre preimage is connected and has zero $`\phi`$ monodromy; it introduces no fractional or extra block index. This applies separately or simultaneously to both cone disks. Hence Definition 2.1 gives representative width equal to the potential range, and Lemma 5.2 with PS Proposition 3.2 gives the class minimum. The point cases have one coincident normal system and constant potential zero. ∎

A noncommon arc segment has a unit jump, so width zero is precisely equality. Edges are exactly the distinct classes with potential range one. For ordinary effective PL codes the pair can be normalised by the terminating enumeration/bigon criterion below on $`P`$; finite region extraction and height propagation then decide the distance. This is a mathematical algorithm specification, not a claim that the entire classifier has been implemented.

## 5.4. Crossing obstruction and true simplices

**Lemma 5.4 (crossing obstruction).** A transverse crossing in normal position forces class distance at least two.

**Proof.** Work in a small regular disk about the crossing and an evenly covered lift. The local first-matching wall separates consecutive block indices $`k,k+1`$. On either side of the second-matching wall, both indices occur in nonempty quadrants. Those two sides lie in consecutive translates of the complete second-matching block. Bringing them into one chosen complete block translates one side by exactly one relative to the other, and translates its first-matching indices by the same amount. The chosen block therefore attains either $`\{k-1,k,k+1\}`$ or $`\{k,k+1,k+2\}`$. Its width is at least two; Theorem 5.3 makes this the class-distance bound. ∎

True simplices consequently have simultaneous noncrossing canonical ordinary representatives, copying common arc classes once. The converse from disjointness to adjacency is **not** used and can fail even with four actual holes when both cones are retained (§8).

## 5.5. A terminating normalisation procedure

Here is a deliberately inefficient algorithm that avoids requiring an exact numerical geodesic solver. Enumerate pairs of valid rational PL codes. Retain only pairs equivalent to the two input vertex codes by Lemma 4.2. Test that common arc classes coincide, the finite overlay is almost transverse with disjoint other boundary endpoints, and it has no bigons or half-bigons.

These are finite tests: enumerate subarcs between overlay intersections or endpoints; check whether their two-sided or boundary-three-sided union is an embedded Jordan curve bounding a disk in $`P`$. Polygon tests determine whether its disk contains a deleted hole. Common full-arc rectangles are handled by the double-coset test. A small rational approximation of the orthogeodesic pair supplies a successful code pair, so the enumeration terminates. Lemma 5.2 applies to every successful output. This is an actual algorithm, although no efficient or implemented preprocessing is claimed. Ordinary innermost-disk simplification can replace the search in implementations.
