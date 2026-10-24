# Part 12. Framed recursive parallels, common separating packets and weighted supports

[Overview](../README.md) · [Next page](part12-2.md) · Part 12, page 1 of 3

**Scope.** The assertion for all non-split graph-manifold links is not proved here. Two new complete classes are proved: arbitrary integer-framed parallels of recursive sum/cable graph knots, and weighted balanced replacements at several parallel supports, with several actual pattern blocks. A common separating packet can be replaced simultaneously at all its visible ports. This handles several auxiliary modes, nonunit actual-facing and invisible frontier degrees, arbitrarily many actual holes, and free vertical returns in the same actual examples. One four-component free-return test is contracted. A different four-component example strictly obstructs a general common-packet reduction: one spanning vertex contains nonparallel four- and eight-boundary support pieces. Cap-free eight-component Hopf tests remain open as well.

Parts 9 and 10 are inputs. None of the new contractibility assertions below requires the tree theorem of Part 11. In particular, the $`S^3`$ filling restriction of Part 9, Remark 11.3, is respected: Part 9, Theorems 11.1–11.2, are invoked only with one invisible companion port. Theorem I proves a different actual decomposition, with one multi-boundary invisible region and several separate actual patterns, including the additional global-chamber argument that this needs.

## 1. Objects and the exact enlarged theorem

All vertices are ordinary ambient-isotopy classes of reduced oriented incompressible spanning systems. Each labelled actual torus is used once, whole closed components are excluded, and components need not be connected. Boundary is free to move on its labelled torus. $`Y`$ is defined by simultaneous disjoint whole representatives. $`X`$ is the cyclic-distance flag complex with the whole-open-complement convention. The original spanning class is $`\Phi`$; auxiliary fibre classes do not give extra deck normalisations.

For a nontrivial knot $`K`$ and $`f\in\mathbb Z`$, let $`L_f(K;\varepsilon_1,\ldots,\varepsilon_n)`$ consist of $`n\ge1`$ parallel regular curves of slope
```math
\delta_f=\lambda_K+f\mu_K
\qquad\text{(1.1)}
```
inside its actual tubular neighbourhood, with orientations $`\varepsilon_i=\pm1`$. These are winding-one parallels. The word “framed” refers to this actual construction in $`S^3`$. Distinct coherently referenced components have pairwise linking $`f`$.

**Theorem A (arbitrarily framed torus-sum parallels).** Suppose
```math
K=\mathop{\#}_{i=1}^{s}T(p_i,q_i),\qquad
s\ge1,\quad p_i\ge2,\quad |q_i|\ge2,\quad \gcd(p_i,q_i)=1 .
\qquad\text{(1.2)}
```
For every integer $`f`$, every $`n\ge1`$, and every orientation list, the actual non-split graph link $`L_f(K;\varepsilon)`$ has contractible $`X`$ and $`Y`$. The strong deformation retraction of $`|Y|`$ onto $`|X|`$ (Part 7, Theorem D) remains valid.

If $`f\ne0`$ and $`\sum\varepsilon_i\ne0`$, both complexes have one vertex. If the actual orientations are balanced, every fixed nonannular ordinary companion sector, including arbitrary signs within a packet, contracts to its pattern-annular subcomplex. Its bounded-packet cyclic subcomplex has the same strong deformation retraction.

This strictly extends Part 9, Theorem 1.9, whose framing is zero. The proof is in §§4–6. The extension is not obtained by dropping the word “zero”: the mode equation, longitude image in the detector, and singleton-terminal normaliser all require the changes proved below.

The main extensions are **Theorem G (§6.1)** for finite sum/cable recursive graph knots, and **Theorem K (§6.5)** for weighted replacements of several parallel supports. **Lemma G′** is the weighted rooted interface; **Theorem I** and the finite certificate **Theorem J** supply the common-packet multiport interface. **Theorem F (§9)** closes these classes together with anchored, capped-core and empty-interface families under the actual boundary operation of Theorem E.

## 2. Ordinary return loops without an actual tether

Let $`V`$ be a genuine Seifert piece embedded in $`S^3`$. Its orientable planar base orbifold has negative orbifold Euler characteristic. Write
```math
\Gamma=\pi_1^{\rm orb}(B)
= C_{\alpha_1}*\cdots*C_{\alpha_t}*F_{b-1},
\qquad\text{(2.1)}
```
where $`b\ge1`$ is the number of ordinary boundary circles. Let $`P_i=\langle d_i\rangle`$ be their primitive peripheral subgroups.

**Lemma B (peripheral family and free returns).** The $`P_i`$ form a malnormal family. Consequently every ordinary loop of an unmarked finite essential vertical-annulus system in $`V`$ has zero transverse configuration winding on every active port. This includes systems with only same-port returns and no actual tether.

**Proof.** The first assertion can be seen geometrically using a compact hyperbolic orbifold metric with geodesic ordinary boundary. In the universal convex domain, a nontrivial intersection of two conjugate peripheral groups identifies their geodesic axes. A deck transformation preserving such a boundary axis must preserve the side containing the convex domain. It cannot reverse the axis; discreteness and primitivity make its stabiliser exactly the peripheral group. Different ordinary boundaries have different axis orbits.

There is also a direct check in (2.1). Take all but one ordinary boundary as infinite cyclic free factors. The remaining boundary word traverses every ordinary and cone generator once. It is cyclically primitive and cannot be conjugate to its inverse. The sole two-involution boundary-word reversal is $`D^2(2,2)`$, of Euler characteristic zero, excluded here. The free-product axis normaliser is therefore its own primitive cyclic group, while different peripheral factors or the long boundary word have no conjugate nontrivial intersection.

Track a spanning path of a vertical annulus around a loop. After taking a finite power, both the annulus and its two boundary occurrences return individually. Quotienting by the Seifert fibre gives the necessary equation
```math
d_i^a\, w\,d_j^{-b}=w.
\qquad\text{(2.2)}
```
For distinct ends the peripheral-family assertion gives $`a=b=0`$. For a same-port essential return, $`w\notin P_i`$. This is the usual peripheral test for an essential return: a peripheral simple arc is parallel into that boundary; an essential wave cuts off a nonempty proper set of the other ordinary or cone features. Straightening such a simple wave by a boundary-preserving orbifold homeomorphism also verifies this test in the free-product normal form. Malnormality applied to $`P_i\cap wP_iw^{-1}`$ again gives $`a=b=0`$.

The integers are exactly the normal tracks of the trace circles; fibre-direction motion is tangent to the annuli. All circles in one parallel port configuration have the same configuration winding. Taking a finite power to remove permutations multiplies that winding, so its original value is zero too. No endpoint was required to be actual, and no connectedness of a local cut complement was used. ∎

This proves the port-loop part of branch (d). It is not a general normalisation or contraction theorem for networks crossing several invisible blocks.

## 3. An oriented obstruction at a balanced two-actual pants

Let a horizontal cluster have connected auxiliary fibre $`R`$, with $`q>0`$ boundary circles on a frontier torus. Suppose its neighbour is a genuine pants product with exactly two actual boundaries of opposite signs and no other port. Its nonempty pieces are vertical.

**Lemma C (balanced pants force unit frontier degree).** Any nonempty efficient spanning assembly at this frontier has $`q=1`$.

**Proof.** The two opposite actual demands make the total port trace class zero. Since one horizontal fibre has nonzero primitive port class, its positive and negative multiplicities are equal. Thus the horizontal collection consists of $`N=2r`$ parallel copies of $`R`$, with signs $`\epsilon_j`$, $`j\in\mathbb Z/N`$. Its trace word on the primitive circle quotient of this port is the $`q`$-fold repetition
```math
(\epsilon_0,\ldots,\epsilon_{N-1})^q .
\qquad\text{(3.1)}
```
Both actual boundaries must tether to the port. An actual-to-actual seam would cross every essential port return and leave no possible nonempty port assembly. The remaining essential pants returns are parallel. On the $`Nq`$ ordered positions their matching is the reflection $`j\mapsto2a-j`$, with actual ends $`a,a+Nq/2`$.

Choose $`a=0`$ at the actual end having positive central sign. All the positions $`kN`$ belong to the same $`R_0`$, and have sign $`+1`$. If $`q`$ is even, the negative actual end $`Nq/2`$ is one of those positions, a contradiction. If $`q>1`$ is odd, positions $`N,(q-1)N`$ are paired nonactual ends with the same sign, again impossible for an oriented annulus. Thus only $`q=1`$ remains. ∎

The lemma is about a balanced two-actual pants frontier. It does not prohibit higher degree at an actual-free return block or at a branch with more actual holes.

### 3.1. A strengthened finite empty-support certificate

Take an actual graph-link support $`K`$, and replace every component by one positive and one negative winding-one parallel of an integer-framed slope $`\ell_i`$. Assume its support-to-pattern and internal support tori are genuine. Every pattern is a two-actual pants product; the whole support restriction of $`\Phi`$ is zero.

Enumerate all connected horizontal support subtrees and their fixed frontier slopes: $`\ell_i`$ at a pattern frontier, the neighbouring Seifert fibre at a support-vertical frontier. Part 10, Theorem 9.3 supplies the unique possible primitive auxiliary class, if one exists with nonzero evaluation on all block fibres.

**Theorem C1 (oriented mode exclusion).** Suppose every candidate subtree either has no such horizontal class or has a balanced two-actual pants frontier where the primitive boundary degree exceeds one. Then every efficient spanning system misses the entire support. Hence $`X=Y`$ is a point.

**Proof.** A maximal horizontal cluster would give one of the enumerated classes. The first alternative excludes its existence and Lemma C excludes the second. All support pieces would therefore be vertical or empty. Genuine fibre mismatch makes every internal and outer support trace empty. Any remaining support piece would be a whole closed component, prohibited. Each relative pants factor then has its unique actual-to-actual seam. The empty-interface ordinary and simultaneous comparison of Part 10, Lemma 11.1 gives one global vertex. ∎

The test is finite and strictly strengthens the purely algebraic no-horizontal-mode certificate. It is sufficient, not necessary; its failure is not a noncontractibility result.

For example use three Hopf fibres and slopes $`\lambda_i-3\mu_i,\lambda_i-3\mu_i,\lambda_i-\mu_i`$. The matrix and primitive kernel are
```math
B=\begin{pmatrix}-3&1&1\\1&-3&1\\1&1&-1\end{pmatrix},
\qquad \ker B=\mathbb Q(1,1,2).
\qquad\text{(3.2)}
```
The central fibre evaluation is four, and its port degrees are $`1,1,2`$. Its genus-one four-boundary auxiliary fibre exists, but cannot enter the third balanced pants. Thus the actual six-component link has $`X=Y`$ a point despite algebraic resonance.

## 4. The framed companion modes

Put $`s_i=p_iq_i`$, and let $`g_i`$ be the genus of the $`i`$-th torus-knot fibre. For $`s\ge2`$, the companion $`Q=E(K)`$ has a composing product
```math
W=S^1_\mu\times P_{s+1},\qquad
\lambda=\sum_i\lambda_i,\qquad h_i=\lambda_i+s_i\mu .
\qquad\text{(4.1)}
```
The actual pattern $`P`$ is the disk with $`n`$ holes times a circle; its fibre is $`\delta_f`$. In the balanced case $`\Phi|_Q=0`$, while $`\Phi|_P\ne0`$ and $`\Phi(h_P)=0`$. Thus pattern pieces are essential vertical annuli. A nonempty companion trace has the fixed slope $`\delta_f`$. Since this is not the composing fibre $`\mu`$, all composing cut pieces are horizontal.

For a positive primitive local horizontal class write
```math
b=\eta(\mu)>0,\qquad a_i=\eta(\lambda_i).
```
A terminal is horizontal with $`a_i=0`$, or vertical with $`a_i=-s_i b`$. The outer boundary equation is
```math
\sum_i a_i+fb=0.
```
All $`a_i`$ are multiples of $`b`$, so primitivity in the composing block forces $`b=1`$. Consequently the exact normal mode equation is
```math
\boxed{\quad V\subseteq\{1,\ldots,s\},\qquad
\sum_{i\in V}s_i=f.\quad}
\qquad\text{(4.2)}
```
This is an unweighted subset equation, not an arbitrary integral combination.

For $`f\ne0`$, $`V`$ is nonempty. The horizontal cluster consists of one section and the fibres of the nonvertical terminals. Its connected fibre $`H_V`$ has
```math
v=|V|,\quad g_H=\sum_{i\notin V}g_i,\quad
\chi(H_V)=1-v-2g_H.
\qquad\text{(4.3)}
```
It has one root boundary and one boundary at each vertical terminal, all of primitive degree one. A normal system consists of $`N`$ parallel $`H_V`$ sheets. The vertical packets at its terminal ports have reflections
```math
j\longmapsto c_i-j\pmod N,\qquad c_i\text{ odd},
\qquad\text{(4.4)}
```
and pair opposite signs. Thus $`N`$ is even.

The joint normalisation in Part 9 applies to the labelled union: nonempty horizontal composing pieces hit every terminal port, so a single disjoint family has one such normal mode. We do not assert that $`V`$ itself is a complete ordinary invariant. The later sectors are labelled by actual ordinary connected companion classes.

### 4.1. Packet structure, including a singleton terminal

The gap-orbit calculation has no use of $`\sum s_i=0`$. With a fixed $`i_0\in V`$, set
```math
g=\gcd\bigl(N,\{c_i-c_{i_0}\}_{i\in V}\bigr),\quad
q=g/2,\quad k=N/g .
\qquad\text{(4.5)}
```
The point orbits give $`q`$ connected companion pieces, each with $`2k`$ root boundaries and genus
```math
g(F)=1+k(v-2+2g_H).
\qquad\text{(4.6)}
```
The gap reflections are $`j\mapsto c_i-1-j`$. Their $`q+1`$ orbits form an interval: two end regions and $`q-1`$ actual product regions. Its interior regions contain only $`H_V\times I`$ and terminal rectangles. They glue to products between the adjacent complete companion surfaces. Hence the whole collection is jointly parallel. This proves the geometric product, not just its Euler profile.

For $`v=1`$, (4.5) means $`g=N`$, $`k=1`$, $`q=N/2`$. Every component is exactly two $`H_V`$ sheets joined by one terminal annulus. Since $`s\ge2`$, there is at least one nonvertical nontrivial torus knot, so $`g_H>0`$. Thus
```math
g(F)=2g_H\ge2,\qquad |\partial F|=2.
\qquad\text{(4.7)}
```
The same gap interval proof works, and the terminal surface has positive genus. The only missing interface from the zero-framing argument is its ordinary outer-loop detector; it is proved next.

Every companion component is separating in $`Q`$. Indeed its reflections give equal numbers of positive and negative $`H_V`$ sheets. Its dual class vanishes on the meridian generator of $`H_1(Q)`$, so a connected such component is separating.

## 5. The ordinary outer loop, with the framing retained

### 5.1. At least two vertical terminals

For $`v\ge2`$, use the incidence-graph detector of Part 9, §10.6. Collapse the horizontal cluster by its primitive bundle map, and each vertical terminal by its Seifert fibre. The resulting group has central cyclic group $`\langle d\rangle`$ and terminal groups $`C_{p_i}*C_{|q_i|}`$, with their primitive peripheral groups identified with $`\langle d\rangle`$.

There is one framing correction:
```math
\mu\longmapsto d,\qquad
\lambda\longmapsto d^{-f},\qquad
\delta_f=\lambda+f\mu\longmapsto1.
\qquad\text{(5.1)}
```
Thus the transverse root motion still maps to $`d`$, and tangential motion to the trace still maps to the identity. The rest of the detector is unchanged. The image of a connected companion is the free subgroup carried by the sheet-and-annulus incidence graph. Reduced paths stay reduced, and $`v\ge2`$ makes that finite graph its own core. A nonzero $`d`$-power normalising it would preserve its minimal subtree. After a finite power it fixes two distinct terminal edges, contrary to peripheral malnormality. Therefore the normal exponent is zero.

This explicitly checks the longitude image; setting $`\lambda`$ to the identity when $`f\ne0`$ would be incorrect.

### 5.2. One vertical terminal

**Lemma D (singleton-terminal detector).** The two-boundary companion in (4.7) has zero ordinary root-configuration loop image.

**Proof.** Let $`C`$ be the horizontal cluster, $`J`$ its sole vertical terminal, and $`T`$ their interface. The cluster $`C`$ is a bundle with fibre $`H=H_V`$, of positive genus and two boundaries. The companion is
```math
F=H_0\ \cup A\ \cup H_1,
\qquad\text{(5.2)}
```
where $`A`$ is one essential vertical return in $`E(J)`$. In the Bass–Serre tree of $`C\cup_T E(J)`$, its induced graph of groups is a length-two path. The two end stabilisers are the noncyclic free groups $`\pi_1(H_0),\pi_1(H_1)`$; their intersections with the edge torus are the cyclic inner-boundary groups. The middle annulus group is cyclic.

This induced tree is minimal. Equivalently, collapse the middle annulus edge to obtain the amalgam of two noncyclic surface groups over their proper boundary cyclic subgroup. Both inclusions are proper. Its reduced Bass–Serre tree maps without a fold into the ambient tree, because $`A`$ joins distinct peripheral cosets. In particular the middle terminal vertex has exactly two incident edges in this minimal subtree.

Choose the reference base point at the first interface edge. A transverse root meridian $`d`$ is transported to the terminal meridian through the composing block; it lies in the interface torus and fixes that first edge and its terminal vertex. If $`d^\ell`$ normalises $`\pi_1(F)`$, it preserves its minimal subtree. The valence-two property makes it fix the other edge as well. In the terminal Seifert group the stabilisers of those two different peripheral cosets intersect only in the central fibre. Modulo that fibre the meridian is the infinite-order primitive peripheral word in $`C_p*C_{|q|}`$. Lemma B gives $`\ell=0`$.

An ordinary surface loop, after a finite power, returns a chosen boundary occurrence and base point. Its boundary track is a meridian power times a power of the trace $`\delta_f`$. The trace lies in $`\pi_1(F)`$ and can be removed from the normaliser equation. The preceding argument therefore excludes every nonzero normal exponent. Taking a finite power also handles unmarked packet permutations. ∎

The collapsed incidence graph alone would be a single edge when $`v=1`$, with trivial core. Retaining its noncyclic horizontal vertex groups is the necessary new step.

### 5.3. Ordinary sector labels and gluing states

The outer companion torus has a fixed slope $`\delta_f`$. The fixed-slope relative-product comparison localises ordinary isotopy there, without assuming anything about the unknown internal marking. The balanced original class kills its injected torus group, excluding the spanning-bundle exception. Thus a nonannular ordinary vertex has a definite ordinary connected companion class $`F`$, a complete ordered signed parallel packet, a joint pattern arc diagram, and their transported gluing state.

For fixed local ordinary data the state is the same single configuration-circle integer as in Part 9, §5. The pattern loop image is zero, and §§5.1–5.2 prove the companion loop image zero. No integer is divided out by a sign-word period. Tangential motion along $`\delta_f`$ adds no annular framing. The no-closed-component test is made on the whole assembly.

Different normal markings are not silently identified or declared distinct. The label is the ordinary surface $`F`$. A simultaneous nonannular family is one parallel packet by §4.1 and hence has just one such ordinary label. Therefore two different labels cannot occur together in a geometric simplex.

[Overview](../README.md) · [Next page](part12-2.md)
