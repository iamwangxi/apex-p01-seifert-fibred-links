# 3. Closed orbifolds, infinite order and two actual boundaries

[Overview](../README.md) · [Definitions](objects.md) · [References](../sources/bibliography.md)

## 3.1. A free-product lemma

**Lemma 3.1.** In a free product with two distinct nontrivial cyclic factors $`A,B`$, the product of a nonidentity conjugate of an element of $`A`$ and a nonidentity conjugate of an element of $`B`$ has infinite order.

**Proof.** After conjugating the product, it is $`a t b t^{-1}`$, with $`1\ne a\in A`$, $`1\ne b\in B`$. Choose $`t`$ of minimal reduced syllable length in its $`A`$–$`B`$ double coset. Removing a leading $`A`$ syllable changes the displayed element by conjugacy; removing a trailing $`B`$ syllable does not change the middle conjugate. The cyclic factors commute with their own elements, so these operations preserve $`a,b`$. If $`t`$ is empty, $`ab`$ is cyclically reduced of length two. Otherwise its first syllable is not in $`A`$ and its last is not in $`B`$. Therefore $`a t b t^{-1}`$ is cyclically reduced of length $`2+2\lvert t\rvert`$. Its positive powers have those lengths multiplied by the exponent and cannot be the identity. ∎

## 3.2. Closed doubles and an injective fold on orbifold groups

Double $`B`$ along all $`n`$ actual boundary circles, obtaining a closed orientable orbifold $`D B`$ of underlying genus

```math
g_D=n-1.
```

It has two cones of each order $`q_j`$, one in each half. On regular parts the fold retraction

```math
r:(D B)\setminus\{o_1,o_1',\ldots,o_s,o_s'\}
 \longrightarrow B\setminus\{o_1,\ldots,o_s\}
```

is identity on the original half and reflection on the mirror. Its induced homomorphism on ordinary fundamental groups sends a cone meridian in either half to the corresponding original cone meridian, up to inversion and conjugacy. It therefore sends every cone-order relation to a cone-order relation. Passing to their quotients gives a **retraction of orbifold groups** $`\Gamma_D\to\Gamma`$. Consequently $`\Gamma\to\Gamma_D`$ is injective. This uses the fold only on regular parts and elementary group quotients; it does not require an unproved boundary orbifold homotopy theorem.

**Lemma 3.2.** The double is good and aspherical in every case where the closed theorem is used.

**Proof.** For $`s\ge1`$, let $`N=\prod_j q_j`$ and $`A=\prod_j\mathbb Z/q_j`$. In the usual punctured closed-surface presentation, send the two meridians of the $`j`$th pair to $`+e_j,-e_j`$, and all handle generators to zero. The relator maps to zero and the map is onto. The associated cover of the ordinary punctured surface has full order $`q_j`$ at each cone. Fill its boundary cycles by disks with local degree $`q_j`$. This constructs a connected, genuine orbifold cover by a closed surface, rather than presupposing goodness. Its Euler characteristic is

```math
\chi(\Sigma)=N\left(2-2g_D-2\sum_j(1-1/q_j)\right),
\qquad
g(\Sigma)=1+N\left(g_D-1+\sum_j(1-1/q_j)\right)\ge2.
```

For $`s=0,n\ge4`$ the double itself is a genus-$`n-1`$ surface. Thus all non-point cases considered below satisfy precisely the closed good-aspherical hypotheses of Schultens Proposition 25. ∎

## 3.3. Closing arcs without assuming nonseparation

For an embedded regular arc $`a`$ joining distinct actual circles $`C_i,C_j`$, let $`c(a)`$ be the third boundary of a thin regular neighbourhood of $`C_i\cup a\cup C_j`$. It is a regular simple closed curve bounding a cone-free pair of pants on that side. Its conjugacy word is, with a consistent orientation convention,

```math
d_i w_a d_j w_a^{-1},
```

where $`w_a`$ is its relative path word. Equal $`\Gamma`$ peripheral double cosets $`\langle d_i\rangle w_a\langle d_j\rangle`$ therefore make the corresponding $`c(a)`$ conjugate.

**Lemma 3.3.** The closing curve has infinite order when $`n\ge4`$ or $`n=2,s=2`$.

**Proof.** We verify essentiality before invoking the closed theorem.

* If $`n\ge4`$, its image in $`\Gamma_{\rm ab}\otimes\mathbb Q=\mathbb Q^n/\langle(1,\ldots,1)\rangle`$ is $`d_i+d_j`$, which is nonzero. Its order in $`\Gamma`$, and then in $`\Gamma_D`$ by the fold injection, is infinite. It is also nonseparating in the closed double, though only infinite order is needed here.
* If $`n=2,s=2`$, the other side of $`c(a)`$ in $`B`$ is a disk containing exactly the two cones. Its boundary word is the product of two once-around cone meridians, conjugated by paths to the cones. In $`\Gamma=C_{q_1}*C_{q_2}*\mathbb Z`$ these are nontrivial elements conjugate into **different** finite factors. Lemma 3.1 makes their product infinite-order. The fold injection again preserves this. The closing curve can be separating in $`D B`$; infinite order is the needed condition, and no nonseparating assertion is made for it. ∎

## 3.4. Recovering regular arc classes

**Lemma 3.4 (regular arcs).** In either of those cases, equality of peripheral double cosets in $`\Gamma`$ for two embedded arcs with the same two actual ends implies endpoint-free ordinary isotopy in $`P`$.

**Proof.** Their closing curves are conjugate in $`\Gamma_D`$ and are regular essential simple closed curves there, by the preceding infinite-order argument. In a good aspherical orbifold, conjugacy supplies the orbifold free homotopy: homotope one fundamental interval of the equivariant universal-cover lifts and extend by the common deck element. Apply **closed** Schultens Proposition 25 to obtain an isotopy avoiding every cone in both halves. Fold that isotopy on regular parts. It becomes an ordinary free homotopy between the closing curves in $`B\setminus\{o_j\}`$, equivalently in the compact surface $`P`$ by the puncture collars. Ordinary curve homotopy-isotopy and isotopy extension identify their labelled pair-of-pants sides. The seam joining the specified two boundaries in a pair of pants is unique up to endpoint-free isotopy. This recovers the original arc class. ∎

## 3.5. The two elementary point cases

For $`n=2,s=0`$, $`P`$ is an annulus and its boundary-to-boundary arc has one endpoint-free isotopy class. For $`n=2,s=1`$, $`P`$ is a pair of pants and its seam joining the two actual boundaries likewise has one class, regardless of the cone order. One elementary seam proof cuts along a chosen seam to obtain an annulus; innermost return arcs remove any other seam's intersections by ordinary bigons and free-endpoint half-bigons. Once the seams are disjoint, one side of the two-edge circle is an empty rectangle, giving their isotopy. The same argument without the third hole handles the annulus. This proves **Lemma 3.5**, uniqueness in the zero- and one-cone two-boundary cases.

The simultaneous verticalisation proved in §4.1 then proves $`X`$ has one vertex in both cases. Its class distance is zero and its carrier is a point. In the one-cone case the closing curve would be cone-peripheral; we have not applied Proposition 25 to that torsion class. This is an explicit treatment, not an excluded case.
