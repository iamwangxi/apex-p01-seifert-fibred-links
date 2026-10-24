# Part 9. Parallel clusters of connected sums of torus knots

[Overview](../README.md) · [Next page](part9-2.md) · Part 9, page 1 of 4

**Scope.** The full graph-manifold-link contractibility problem is not closed here. The balanced four parallels of the square knot are handled by the single-packet contraction in Section 10. The gap-orbit extension there handles all zero-framed parallel clusters of connected sums of nontrivial torus knots. The results include an ordinary vertex catalogue for the square-knot case, exact distances on its two-boundary sectors and for specified unbounded families, and a one-sided ordinary parent for arbitrary signed packets. A connected genus-seven example shows why an unrepaired elementary packet move is insufficient. A closed formula for arbitrary mixed-packet pair distances and the genuinely multi-port graph-manifold induction remain open.

Part 8 is used only as a comparison. The proofs below re-establish the particular local facts they need. No external novelty is claimed. No finite enumeration is used as a substitute for a topological argument.

The main contraction is in Section 10, using the ordinary packet facts of Sections 2--4. Sections 5--9 give the square-knot catalogue, metric results, filtered comparison and the raw-surgery obstruction. Section 11 records fixed-packet replacement theorems (whose several-port branches are vacuous in $`S^3`$, Remark 11.3) and the general graph-manifold interface left open here.

## 1. Objects and statements

Let

```math
K=T(2,3)\#\overline{T(2,3)}
```

and let $`L_4`$ consist of four zero-framed parallels of $`K`$, two with each orientation. Actual boundary tori are labelled. Use the reduced ordinary conventions of [objects](objects.md): every actual torus is used once, surfaces are oriented and componentwise incompressible, closed components are excluded, and boundary curves may slide on their own tori. Isotopies start at the identity. The cyclic cover uses one common level for the whole cut-open complement.

Write $`Y`$ for simultaneous geometric disjointness and $`X`$ for the flag complex of cyclic class distance one. The Part 7, Theorem D identifies $`|X|`$ as a strong deformation retract of $`|Y|`$; it does not turn a proof about a proper subcomplex of $`Y`$ into a proof about all of $`Y`$.

There is a pattern-companion decomposition

```math
M=E(L_4)=P\cup_{T_0}Q,
\qquad P=S^1_\lambda\times B,
\qquad Q=E(K),
\qquad\text{(1.1)}
```

where $`B`$ is a disk with four actual holes and one outer companion boundary. Denote by $`\mathcal A`$ the subcomplex of pure pattern-annular vertices. Its vertices are the ordinary oriented perfect matchings of the four actual holes, with the companion hole retained as a marked unused hole.

Here are the principal results.

**Theorem 1.1 (ordinary catalogue).** Every vertex has exactly one of the following types: a pure pattern-annular system; a partial pattern matching capped by square-knot spanning fibres; or the cancellation data of Theorem 5.1. In the cancellation type, every connected companion piece has genus one and $`2k`$ longitudinal boundaries. Its unoriented ordinary companion class is a regular essential curve $`\gamma`$ on a four-marked sphere, not isotopic to its equator, with $`i(\gamma,E)=2k`$. A cancellation packet has $`q`$ parallel copies of this piece, with its complete ordered sign word retained. For fixed ordinary local pattern and companion data, the ordinary gluing classes form an explicitly described copy of $`\mathbb Z`$, restricted only by the no-closed-component condition. There is no further unnoticed port-loop quotient.

This is a path-coordinate catalogue. It does not identify distinct pattern arc classes, different rational curve slopes, different packet words, or different permitted integer gluings.

**Theorem 1.2 (contractible cores in both complexes).** Let $`\mathcal C`$ be the full subcomplex of $`Y`$ on the vertices in $`\mathcal A`$ and the cancellation vertices having exactly one companion component. Then $`\mathcal C`$ and the induced cyclic subcomplex on its vertices are contractible. The larger subcomplex

```math
\mathcal K=\mathcal C\cup Y_{\rm fib}\cup
\bigcup_{i(\gamma,E)=2}Y_\gamma,
\qquad\text{(1.2)}
```

where $`Y_{\rm fib}`$ is the entire capped-fibre sector and $`Y_\gamma`$ is the fixed-companion-class sector, each including $`\mathcal A`$, is contractible as well, as is the induced cyclic subcomplex on all its vertices. Thus every two-boundary companion packet is included, with arbitrary multiplicity and signs; multi-boundary companions are included when there is just one piece. In particular, the genus-one, four-boundary companion in the question lies in this core. The core contains vertices of arbitrarily large genus.

**Theorem 1.3 (unbounded exact distance from annuli).** For every $`q\ge1`$ there is a connected vertex $`S_q`$, of genus $`2q-1`$ and with four actual boundaries, such that

```math
\min_{a\in\mathcal A^{(0)}}\delta(S_q,a)=q.
\qquad\text{(1.3)}
```

Here $`S_1`$ is precisely a single genus-one, four-boundary cancellation companion with four tethers. For $`q\ge2`$, $`S_q`$ has no geometric annular neighbour. Thus neither $`X`$ nor $`Y`$ is a cone with any pure annular vertex as apex.

**Proposition 1.4 (failure of the elementary packet rule).** There is a connected genus-seven vertex with four parallel, four-boundary companion pieces, with ordered coorientations $`(+,+,-,+)`$, for which both end single-piece resolutions and both adjacent opposite-sign product cancellations leave a compressible component carrying actual boundary, even after every whole closed component is deleted. This only rules out these specified raw operations. It is not a noncontractibility result and does not rule out a different surgery or a surgery followed by a controlled compression procedure.

**Theorem 1.5 (two-boundary replacement).** For each $`\gamma`$ with $`i(\gamma,E)=2`$, the entire sector $`Y_\gamma`$ is simplicially isomorphic to the geometric oriented matching complex on a sphere with four actual holes and two unused auxiliary holes. The correspondence also identifies the induced cyclic complex $`X_\gamma`$ with the cyclic matching complex. Both are contractible. For two vertices in this sector, their distance in the full $`X`$ equals the planar minimum-height-range formula in (6.4). Thus ordinary classes, geometric simplices and all pair distances are determined for every such sector, including arbitrarily large mixed-sign packets.

**Theorem 1.6 (existential cyclic descent).** Every cancellation vertex with $`q>0`$ companion pieces has a cyclic neighbour in the same sector with fewer pieces; set $`q=0`$ on $`\mathcal A`$. Hence

```math
\kappa_Q(S)\le\min_{a\in\mathcal A^{(0)}}\delta(S,a)\le q(S).
\qquad\text{(1.4)}
```

The two bounds agree for every coherently cooriented packet. More generally, for every finite geometric simplex containing a cancellation vertex, one can choose one such vertex $`S`$ and a lower-$`q`$ cyclic neighbour of $`S`$ that remains geometrically compatible with the whole simplex. Section 8 first proves this by compression existence. Section 10 subsequently constructs an ordinary parent in the single-packet setting. Neighbourhood domination is not asserted; the contraction uses ordered prism subdivisions instead.

**Theorem 1.7 (filtered comparison).** The component-wall retraction in Part 7 preserves every additive ordinary component functional, in particular Euler characteristic. For any such functional $`f`$ and threshold $`a`$, the induced cyclic subcomplex on vertices with $`f\le a`$ is a strong deformation retract of the induced geometric subcomplex on the same vertices. The retraction is obtained by composing the Part 7 homotopy with removal and renormalisation of coefficients on vertices above the threshold; the unmodified Part 7 retraction need not preserve that induced subcomplex. The same argument applies to the sectorwise packet-count functions used here.

**Theorem 1.8 (coherent-packet sectors).** Fix any $`\gamma`$, including $`i(\gamma,E)\ge4`$, and fix one of its two reference coorientations. The full geometric subcomplex on $`\mathcal A`$ and all packets coherent in that coorientation is contractible, as is its induced cyclic subcomplex. For every $`n`$, the induced cyclic subcomplex with $`q\le n`$ strongly deformation retracts onto the annular cyclic subcomplex. For the four-parallel link, allowing either coherent coorientation still gives contractible induced geometric and cyclic subcomplexes. Consequently the core of Theorem 1.2 can be enlarged to include **every coherent multi-boundary packet of arbitrary size**, while retaining all mixed-sign two-boundary sectors and the fibre sector.

**Theorem 1.9 (complete parallel-cluster theorem).** The full complexes $`X(L_4)`$ and $`Y(L_4)`$ are contractible. More generally, this holds for every nonempty zero-framed parallel cluster, with arbitrary orientations, of

```math
K=\mathop{\#}_{i=1}^{s}T(p_i,q_i),\qquad
s\ge1,\quad p_i\ge2,\quad |q_i|\ge2,\quad\gcd(p_i,q_i)=1.
\qquad\text{(1.5)}
```

In the balanced case, each fixed cancellation-class cyclic sector, and every induced subcomplex with a fixed upper bound on its packet count, strongly deformation retracts onto its annular cyclic subcomplex. This theorem includes arbitrary signs inside each cancellation packet. The rational ordinary catalogue of Sections 3--5 is asserted for the square knot and its four-cone analogue, not for this entire larger family. The theorem does not assert contractibility for all graph-manifold links.

## 2. Efficient cuts and the two companion modes

Write

```math
Q=R\cup_{T_+\sqcup T_-}(Q_+\sqcup Q_-),
\qquad R=S^1_\mu\times B_2,
\qquad\text{(2.1)}
```

where $`B_2`$ is a pair of pants and $`Q_\pm`$ are the two trefoil exteriors. With consistent orientations,

```math
\lambda=\lambda_++\lambda_-,\qquad
h_+=\lambda_++6\mu,\qquad h_-=\lambda_--6\mu.
\qquad\text{(2.2)}
```

The spanning class vanishes on $`Q`$. The pattern fibre is $`\lambda`$, the composing fibre is $`\mu`$, and adjacent fibre slopes intersect once. These are the actual connected-sum and parallel constructions in $`S^3`$. All relevant tori are incompressible. In particular, the resulting exterior is irreducible and the link is non-split.

### 2.1. Essential-cut comparison

Minimise a surface's trace on the relevant torus collection. Inessential circles disappear by incompressibility and irreducibility. A boundary-parallel cut annulus returning to one torus has an annular parallelism. An innermost intervening annulus in that parallelism has an empty parallelism and removes two trace circles. Thus all cut pieces are essential. The same argument works for the embedded labelled union of a finite disjoint family. Hatcher's Lemma 1.11 excludes any other boundary-compressible cut piece in a manifold with torus boundary.

We will also use the following restricted ordinary comparison. If two efficiently cut spanning systems are ordinarily isotopic and their traces on $`T_0`$ have slope $`\lambda`$, they are isotopic preserving $`T_0`$ setwise. This is the product-region argument of Section 31, applied only at this one torus; it does not assume any unknown internal trace slope. In a Banks relative product region, the torus cuts into annuli, or lies wholly in the product. The latter would inject $`\mathbb Z^2`$ into the free group of a surface product. A returning torus annulus gives, by the annular-product argument, an innermost whole cut face annulus parallel into $`T_0`$, contradicting efficiency. The remaining torus annuli span the product and straighten jointly. All product pushes can therefore preserve $`T_0`$.

The fibre exception is absent. A connected spanning fibre would have free kernel, whereas the spanning class kills the injected torus group in $`Q`$. A component of a disconnected spanning system does not meet every actual boundary torus and cannot be a whole fibre of $`M`$.

Consequently the efficient outer trace, the number and topology of the companion components, and their ordinary local isotopy types are ordinary invariants. This assertion also applies to labelled unions when a particular isotopy matches their components.

### 2.2. Pattern pieces

The actual boundary slope is the pattern fibre. The Seifert classification makes every efficient pattern piece a vertical annulus. Its base is an actual-to-actual arc, an actual-to-outer tether, or an essential outer-to-outer return. An actual-to-actual arc joins opposite signs. Every actual hole occurs once. No pattern circle is retained, because its inverse image would be a whole closed component.

Port signs are always measured using one fixed transverse meridian on the ambient torus, equivalently the coorientation of the whole surface. The two blocks' opposite outward-boundary orientation conventions are converted to this common trace convention before their sign words are compared.

If the companion is nonempty, let $`t`$ be the number of tethers and $`N`$ the number of outer trace circles. In the cancellation mode,

```math
t\in\{2,4\},\qquad
\#\{\text{actual-to-actual annuli}\}=\frac{4-t}{2},\qquad
\#\{\text{returns}\}=\frac{N-t}{2}.
\qquad\text{(2.3)}
```

The exclusion of $`t=0`$ uses the no-closed-component condition. The balance restriction in (2.3) follows also from the companion classification below: each cancellation component has equally many positive and negative longitudinal ends.

### 2.3. Companion pieces

The longitudinal outer trace is transverse to $`\mu`$. Hence all composing pieces are horizontal. Cut along one connected horizontal piece. Its complement is its horizontal product; the interval order of other disjoint horizontal sheets prevents nontrivial covering monodromy. Thus the whole system is parallel to one primitive horizontal class

```math
\eta(\mu)=d>0,\quad \eta(\lambda_+)=a_+,\quad
\eta(\lambda_-)=a_-,\quad a_++a_-=0.
\qquad\text{(2.4)}
```

A horizontal piece in a trefoil leaf has longitudinal boundary and is its one-boundary spanning fibre. A vertical piece is a returning annulus of slope $`h_\pm`$. The available conditions are $`a_\pm=0`$ in a horizontal leaf, and $`a_\pm=\mp6d`$ in a vertical leaf. Exactly two modes remain:

```math
\eta_0=(1,0,0),\qquad \eta_c=(1,-6,+6).
\qquad\text{(2.5)}
```

Primitivity forces $`d=1`$. Mixed leaf modes do not satisfy $`a_++a_-=0`$.

The first mode gives parallel genus-two, one-boundary square-knot fibres. Every such fibre must have an actual tether: a return joining two one-boundary fibres would close an entire component. Thus $`N=t\in\{2,4\}`$ and there are no outer returns in the reduced fibre mode.

In the second mode, $`N`$ parallel pants sections are joined in each leaf by essential vertical annuli. Number the sections cyclically by $`\mathbb Z/N`$. A leaf packet is a reflection matching

```math
L_\pm(i)=c_\pm-i\pmod N.
\qquad\text{(2.6)}
```

There are no fixed points, so $`N`$ is even and $`c_\pm`$ are odd. Individual section signs $`\epsilon_i`$ satisfy

```math
\epsilon_{L_+(i)}=-\epsilon_i,
\qquad \epsilon_{L_-(i)}=-\epsilon_i.
\qquad\text{(2.7)}
```

Each connected component of the two-coloured matching graph is an alternating cycle, with double edges allowed. If it has $`2k`$ vertices, it has $`2k`$ pants and $`2k`$ gluing annuli, hence Euler characteristic $`-2k`$ and $`2k`$ outer boundaries. It therefore has genus one.

More explicitly, put

```math
g=\gcd(N,c_+-c_-),\qquad \gcd(N,0)=N.
```

The composition of the reflections is translation by $`c_+-c_-`$. Its orbits have size $`N/g`$. Since $`g`$ is even and each reflection exchanges the even and odd residue orbits, the full matching graph has

```math
q=\frac g2\quad\text{components},\qquad
2k=\frac{2N}{g}\quad\text{outer boundaries per component}.
\qquad\text{(2.8)}
```

Thus $`N=2kq`$. Every component has equally many signs of each kind. Different leaf offsets are permitted; setting them equal would delete the multi-boundary case from the problem.

If the complete spanning vertex has $`c`$ components and total genus $`G`$, then

```math
c\in\{1,2\},\qquad G=kq+c-2.
\qquad\text{(2.9)}
```

Indeed all actual-bearing components are balanced, so each uses at least two actual boundaries, and $`\chi(S)=-N=-2kq`$. When $`k=1`$, every companion vertex in the incidence graph has degree at most two; after closed cycles are excluded, its components are paths. Consequently $`c=2`$ in this case. A connected four-boundary cancellation vertex necessarily has $`k\ge2`$.

## 3. The four-marked sphere and the ordinary companion class

### 3.1. A fixed quotient map

Choose a circle map on $`R`$ representing $`\eta_c`$, with the prescribed linear boundary maps. Its levels are the pants sections. Glue the two leaf base orbifold disks along their common phase circle $`E`$. This gives

```math
\Sigma=S^2(2,3,2,3)=D_+\cup_E D_-
```

and a fixed continuous quotient map

```math
p:Q\longrightarrow\Sigma.
\qquad\text{(3.1)}
```

On a leaf this is the Seifert projection; on $`R`$ it is the $`\eta_c`$ circle map into $`E`$. These maps agree on the tori because $`\eta_c(h_\pm)=0`$. In particular,

```math
p_*(\mu)=d=[E],\qquad p_*(\lambda)=1.
\qquad\text{(3.2)}
```

We use cone points as marked points for regular curve isotopy. Their orders matter for the group detector below. The circle $`E`$ is an auxiliary horizontal phase; it is not the global spanning cyclic-cover coordinate, which is trivial on $`Q`$ in the balanced case.

A cancellation system maps to a regular multicurve $`\Gamma\subset\Sigma`$: each pants section maps to one point of $`E`$, and each leaf annulus maps to an arc separating its two cone points. Conversely, the inverse image of such a multicurve is exactly the corresponding pants-and-annulus system.

Every component of $`\Gamma`$ is in minimum position with $`E`$. An empty bigon would be an inessential returning leaf arc. A null, peripheral, or equator-parallel curve can avoid $`E`$, so no component has one of those types. On a four-marked sphere, two disjoint regular essential nonperipheral curves are isotopic. Consequently all companion components of any one disjoint family are parallel copies of a single $`F_\gamma=p^{-1}(\gamma)`$, and

```math
g(F_\gamma)=1,\qquad |\partial F_\gamma|=i(\gamma,E)=2k.
\qquad\text{(3.3)}
```

The parallelism is a real three-dimensional parallelism. The annulus between two curves $`\gamma`$ has no marked points. Every $`E`$-arc in it spans; a return would give a bigon, and a whole $`E`$ circle would make $`\gamma`$ equator-parallel. Its rectangles lift to leaf annulus products and its equator crosscuts to pants products. These glue to $`F_\gamma\times I`$.

### 3.2. Ordinary detection, including the orbifold hypotheses

The orbifold group is

```math
\Pi=(C_2*C_3)*_{\langle d\rangle}(C_2*C_3),
\qquad\text{(3.4)}
```

with the two boundary words identified in the orientation appropriate to the gluing. A curve meeting $`E`$ minimally and positively is cyclically reduced in this amalgam and has infinite order. Its inverse-image surface is a graph of pants and annuli whose incidence graph is that curve. Therefore

```math
p_*\pi_1(F_\gamma)=\langle\gamma\rangle,
\qquad\text{(3.5)}
```

with surjection onto this infinite cyclic group, not merely onto a non-specified power subgroup.

The orbifold is closed, good and aspherical. One explicit construction sends its paired order-two cone meridians to the nonzero element of $`C_2`$, its order-three meridians to opposite generators of $`C_3`$, and uses the six-sheeted punctured cover associated to $`C_2\times C_3`$. Filling the puncture lifts with their local degrees gives a genuine closed surface cover. Its Euler characteristic is $`6(-1/3)=-2`$, so its genus is two.

An ordinary isotopy between companion components makes the cyclic subgroups in (3.5) conjugate. Generators of equal infinite cyclic subgroups differ by inversion. Closed Schultens Proposition 25 therefore gives a regular unoriented isotopy of the curves in $`\Sigma`$. Its hypotheses have just been verified; no boundary-orbifold extension is used.

Conversely, isotopic curves in minimum position with $`E`$ admit an $`E`$-preserving isotopy. The usual bigon-removal proof works relative to the transverse $`E`$ arcs: an $`E`$ arc returning in a comparison bigon would contradict minimum position. At the disjoint stage the comparison annulus contains only spanning $`E`$ arcs. Lift the resulting disk-side arc isotopies through the leaf fibrations and the common phase motion through the pants bundle. Tangential motion along a full boundary fibre is absorbed in its collar. This produces an ordinary isotopy of the inverse-image surfaces in $`Q`$.

Thus the unoriented ordinary class of a connected cancellation companion is exactly $`\gamma`$. After fixing a pillowcase marking of the underlying four-marked sphere, these classes can be written as

```math
\gamma_{p/k},\qquad k\ge1,\quad p\in\mathbb Z,\quad \gcd(p,k)=1.
\qquad\text{(3.6)}
```

The equator has slope $`1/0`$, and the intersection number is $`2k`$. The pillowcase double cover here is the usual **topological** branched torus cover used to label curves; it is not claimed to be an orbifold cover of the order-three cone points.

## 4. Ordinary loops have zero outer winding

This section supplies the loop information missing from a catalogue based only on sheet counts.

**Lemma 4.1 (companion loop).** A loop of an unmarked cancellation companion system in $`Q`$ has zero winding in the configuration of its outer longitudinal trace circles. In particular it cannot cyclically permute those circles, permute the companion copies, or reverse a companion's coorientation while returning to the same unmarked system.

**Proof.** The peripheral subgroup $`\langle d\rangle`$ is malnormal in $`C_2*C_3`$. In reduced-word terms, $`d=xy`$ is primitive of syllable length two; its axis stabiliser has no reversal, since the order-three syllable is not its inverse. Thus its axis stabiliser is exactly $`\langle d\rangle`$, and different conjugates have trivial intersection.

It follows that the Bass--Serre tree of (3.4) has trivial stabilisers of two distinct edges incident at one vertex. If $`\gamma`$ crosses $`E`$, it acts hyperbolically on this tree. An element $`d^\ell`$ normalising $`\langle\gamma\rangle`$ preserves its axis, and also fixes the original amalgamation edge. Its action on the axis is therefore the identity or a reflection. Its square fixes the entire axis, including two adjacent edges. Hence $`d^{2\ell}=1`$, and $`\ell=0`$.

Now take a finite power of the given surface loop so that one companion component and each of its boundary circles return to themselves. Follow a basepoint on one boundary circle. After applying $`p_*`$ its track is $`d^\ell`$: tangential longitudinal motion vanishes by (3.2). Since the surface returns to itself, this track normalises its image subgroup (3.5). The preceding paragraph gives $`\ell=0`$. The configuration-circle winding of the original loop is zero too, since taking a power multiplies that integer. A zero-winding configuration loop induces no cyclic permutation. Each companion component has nonempty boundary, so the components cannot be permuted. An orientation reversal would reverse the induced orientation on a fixed longitudinal boundary circle, which an identity isotopy of the boundary torus cannot do. ∎

Fix, for each $`\gamma`$, one reference copy with a coorientation and a reference product neighbourhood. Use the same normal interval direction and the same chosen end for every packet multiplicity; deleting copies restricts this linear order. A signed $`q`$-packet is now classified by the exact word

```math
w=(w_0,\ldots,w_{q-1})\in\{+1,-1\}^q.
\qquad\text{(4.1)}
```

There is no further reversal or permutation quotient: an ambiguity between two identifications with the reference would be a loop prohibited by Lemma 4.1. The order is the linear order of parallel copies in the chosen product neighbourhood.

Starting at a positive root crossing of the reference curve, the outer sign word of this packet is

```math
\epsilon_Q=(w,-w^{\rm rev})^k,
\qquad\text{(4.2)}
```

up to the fixed reference cyclic origin. The order of copies reverses at the next root crossing.

**Lemma 4.2 (pattern loop).** For a pattern system with at least one actual-to-outer tether, a loop of its ordinary unmarked annulus system has zero outer trace winding.

**Proof.** Choose the tether at a specified actual hole; that hole is used once. After a finite power any finite packet permutation disappears. Project a path across this tether during the isotopy to $`B`$. If $`d_i`$ and $`d_0`$ are its two boundary words, their endpoint tracks give

```math
d_i^{\ell_i}u d_0^{-\ell_0}=u.
```

In the rational homology of the disk with four holes, $`[d_i]`$ and $`[d_0]=-[d_1]-\cdots-[d_4]`$ are independent. Hence $`\ell_0=\ell_i=0`$. Again the original configuration winding is zero because the powered winding is zero. ∎

Ordinary pattern annuli are detected by their joint ordinary multiarc classes. This includes returns: projection $`P\to B`$ sends a moving cross-arc of any annulus to a proper homotopy of its base arc. Proper homotopy of essential arcs on this ordinary surface gives endpoint-free isotopy. Joint straightening retains multiplicities and cyclic order. The annulus contains the full fibre circle, so there is no tangential framing coordinate.

## 5. The complete vertex catalogue and its gluing integer

We spell out what the integer means, rather than declaring arbitrary independently chosen local twists equivalent.

### 5.1. A configuration-space bookkeeping fact

Let $`\epsilon`$ be a fixed cyclic sign word of length $`N`$, and let $`C_\epsilon`$ be the space of $`N`$ distinct points on a circle carrying that cyclic sign pattern. If $`h`$ is the least positive period of $`\epsilon`$, then $`C_\epsilon`$ is homotopy equivalent to a circle. Its positive generator advances the reference indexing by $`h`$ positions. After $`N/h`$ such circuits each individual point has travelled once around the circle.

One model uses a starting angle and positive cyclic gaps with sum one, and quotients by the index shift $`h`$. Contracting the gaps equivariantly to equal gaps proves the assertion.

Suppose two path-connected local isotopy spaces have boundary evaluation to $`C_\epsilon`$. Boundary isotopy extension gives path and homotopy lifting: move the trace circles in a collar and extend the move to the local manifold. Components of their matching-boundary fibre product are then indexed by

```math
\mathrm{im}\pi_1(\mathcal E_P)\backslash
\pi_1(C_\epsilon)/
\mathrm{im}\pi_1(\mathcal E_Q).
\qquad\text{(5.1)}
```

For clarity, choose paths from a pair of fixed local references to a given matching pair. Their boundary paths have common endpoints, so their difference is a loop in $`C_\epsilon`$. Changing either local path changes its class by the corresponding loop image. Conversely, equality of these classes lets one adjust the paths to have the same boundary motion, by collar lifting. They then glue to a global isotopy. Tangential reparametrisations of full longitudinal circles are absorbed in the collars. This proves (5.1) without assuming that either local isotopy space is contractible.

### 5.2. Cancellation data

**Theorem 5.1 (precise cancellation catalogue).** Fix the reference choices just described. The cancellation vertices are exactly the following data, subject to the stated admissibility tests:

1. An ordinary oriented essential pattern multiarc class $`\alpha`$ in $`B`$, with every labelled actual hole used once. It has $`t=2`$ or $`4`$ tethers, $`N`$ outer ends, and the counts in (2.3).
2. A curve $`\gamma=\gamma_{p/k}`$ as in (3.6), and an integer $`q\ge1`$ with $`N=2kq`$.
3. An exact signed packet word $`w\in\{+1,-1\}^q`$.
4. An integer $`z\in\mathbb Z`$ in the configuration-circle coordinate (5.1).

First require the oriented outer trace word of $`\alpha`$ to agree cyclically with (4.2). Choose one reference alignment. If its least sign period is $`h`$, the integer $`z`$ changes that alignment by $`hz`$ positions modulo $`N`$, and also records all complete turns. Form the incidence graph by gluing the pattern annuli to the corresponding boundaries of the $`q`$ companion pieces. Every component of this graph must meet an actual boundary. This is the remaining admissibility test.

Two admissible data sets give the same ordinary vertex if and only if their ordinary $`\alpha`$, curve $`\gamma`$, word $`w`$, and integer $`z`$ agree in the fixed references. Different choices of references merely re-coordinate this statement.

**Proof.** Essential normalisation and Sections 2--3 prove exhaustiveness. All pieces specified in the construction are essential. The usual innermost-circle and outermost-arc argument for a compressing disk across the gluing torus makes their union incompressible. The sign test gives an orientation; the incidence test excludes whole closed components; all actual boundaries are used once.

An ordinary global isotopy can preserve $`T_0`$ by Section 2.1. Its restrictions preserve precisely the ordinary local data already detected in Sections 3--4. Conversely, matching local paths glue by the collar adjustment in Section 5.1. Both loop images in (5.1) vanish by Lemmas 4.1 and 4.2. Thus the remaining quotient is exactly $`\pi_1(C_\epsilon)=\mathbb Z`$. There is no additional identification of $`z`$. ∎

This is an effective topological encoding: ordinary multiarcs can be specified by any standard surface arc coordinates or finite curve diagrams; $`\gamma`$ has a rational slope; $`w`$ is finite; and $`z`$ is an integer measured by boundary tracks. The incidence test is finite. Reflection offsets alone are not a replacement for this catalogue.

### 5.3. The other two types

The pure annular vertices are exactly the ordinary oriented perfect matchings in $`B`$ with the companion boundary marked and unused.

In the fibre sector, every actual hole is either paired with an opposite actual hole or tethered to $`T_0`$. Cap each tether by a square-knot spanning fibre at the corresponding bundle phase. These partial matching classes are the complete ordinary vertices of this sector. There is no additional gluing integer. In (5.1), the signed fibre packet realises a generator of $`\pi_1(C_\epsilon)`$ by moving its phases around the bundle circle. Thus its loop image is the whole group and the quotient is a point. This argument uses whole phase paths, not independent deck choices for separate components.

For $`t=2`$ there are two genus-two one-boundary components and one annulus. For $`t=4`$ there are four genus-two one-boundary components. The $`t=0`$ case is already $`\mathcal A`$.

[Overview](../README.md) · [Next page](part9-2.md)
