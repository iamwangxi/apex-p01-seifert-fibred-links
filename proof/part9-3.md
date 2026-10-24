# Part 9. Parallel clusters of connected sums of torus knots (continued)

[Overview](../README.md) · [Previous page](part9-2.md) · [Next page](part9-4.md) · Part 9, page 3 of 4

## 9. A connected obstruction to the raw elementary packet moves

Use four copies of a four-boundary companion, in order $`0,1,2,3`$, with

```math
w=(+,+,-,+),\qquad N=16,\qquad c_+=7,\quad c_-=15.
\qquad\text{(9.1)}
```

The copy labels of the cyclic trace points and their signs are

```math
\begin{aligned}
r(i)&=(0,1,2,3,3,2,1,0,0,1,2,3,3,2,1,0),\\ 
\epsilon(i)&=(+,+,-,+,-,+,-,-,+,+,-,+,-,+,-,-).
\end{aligned}
\qquad\text{(9.2)}
```

Put the four actual tethers at

```math
U=\{0,2,6,9\},
\qquad\text{(9.3)}
```

with their displayed signs. The six pattern returns are

```math
(1,15),\ (3,14),\ (4,13),\ (5,12),\ (7,11),\ (8,10).
\qquad\text{(9.4)}
```

These are nested, opposite-sign chords. The numbers of actual tethers in their open index intervals are respectively $`3,2,2,2,1,1`$, so all are essential. Their graph on the four companion copies is connected and has no bridge. Thus every one of the six pattern returns is nonseparating on the resulting surface; the separating-return parent from the double-parallel argument cannot be used here. The vertex has Euler characteristic $`-16`$ and genus seven with four actual boundaries. No minimality of this obstruction's genus is asserted.

Consider exactly the following natural packet operations: resolve the first copy by the boundary annuli on the empty first end; resolve the last copy on the other empty end; or delete an adjacent opposite-sign pair and join corresponding boundary circles through its product region. Only pairs $`(1,2)`$ and $`(2,3)`$ are oppositely oriented.

Compose these cap matchings with (9.4), then delete **whole** closed components. The following returns remain in components carrying actual boundary:

| Operation | Empty-side return left in the output | Companion copies joined by that return |
|---|---|---|
| Resolve copy $`0`$ at the first end | $`(10,11)`$ | distinct copies $`2,3`$ |
| Resolve copy $`3`$ at the last end | $`(13,14)`$ | distinct copies $`2,1`$ |
| Cancel the product pair $`(1,2)`$ | $`(3,4)`$ | two boundaries of copy $`3`$ |
| Cancel the product pair $`(2,3)`$ | $`(7,8)`$ | two boundaries of copy $`0`$ |

Each listed interval contains no actual hole and no other retained trace point. Thus its pattern annulus is boundary-parallel into $`T_0`$. Push that annulus across $`T_0`$. In the first two rows it amalgamates two genus-one, four-boundary pieces into a genus-two, six-boundary companion piece. In the last two rows it tubes one such piece into a genus-two, two-boundary companion piece.

If the actual-bearing output component were incompressible, cutting it along the remaining longitudinal $`T_0`$ traces would give an incompressible piece of this stated topology. It is not a boundary-parallel annulus, hence is boundary-incompressible by Hatcher Lemma 1.11. But Section 2 classified all essential longitudinal companion pieces: they are genus-two one-boundary fibres or genus-one even-boundary cancellation pieces. Neither genus-two output is permitted. Therefore the actual-bearing output is compressible. This proves Proposition 1.4.

The exact finite calculation is reproduced by `scripts/part9_checks.py`.

## 10. One-sided packet normalisation and the complete contraction

The preceding arguments isolate the extra feature needed for mixed signs: repair all new empty pattern returns on the **same side of the original incompressible surface**. The original surface supplies a barrier. In a single parallel packet, that barrier leaves a finite set of mutually independent chamber operations. This is more restrictive than an arbitrary maximal compression procedure.

### 10.1. The finite one-sided chamber set

Fix a normal cancellation vertex $`S`$ and retain its original companion pieces $`F_0,\ldots,F_{q-1}`$ as barriers. Fix one of the two global normal sides of $`S`$, first called the negative side. A complementary region of $`Q\setminus S`$ is called negative if **all** its companion boundary faces are negative faces of $`S`$.

For the ordered word $`w`$, the negative regions are exactly:

* the first end region if $`w_0=+1`$;
* the product region between $`F_i,F_{i+1}`$ if $`(w_i,w_{i+1})=(-1,+1)`$;
* the last end region if $`w_{q-1}=-1`$.

Their sets of companion boundary pieces are pairwise disjoint. A piece cannot be used by two negative regions. The analogous positive list exchanges the signs. The **linear parallel packet** supplies this explicit list and, crucially, makes it exhaustive for the empty-return repairs in Lemma 10.1.

For any collection $`U`$ of negative regions, resolve all their boundary companion pieces by the annuli in their outer-torus boundaries. Retain one small negative push-off of every other original companion piece and of the pattern pieces. Denote the resulting raw surface by $`R_U`$. The annular cap operations have disjoint sets of endpoints and commute. They can all be made in the selected regions and in fixed small collars, so $`R_U`$ is disjoint from $`S`$ and has exactly the original actual boundaries.

Push the new boundary-parallel companion annuli into the pattern, in the empty annular gaps between the original trace circles. All these pattern moves can be taken fibre-invariant, so their annular path composition takes place literally in $`B`$. The remaining companion pieces of $`R_U`$ are precisely a subpacket of small negative push-offs of original pieces. Its pattern is an annular system, possibly with inessential returns and whole closed components. Ignore closed pattern circles, which are separate tori, but postpone deletion of components containing companion pieces until the normalisation is finished.

**Lemma 10.1 (the barrier identifies every bad return).** Every boundary-parallel pattern return of $`R_U`$ corresponds to a unique unselected negative region $`G`$ whose companion boundary pieces are still present. Resolving $`G`$ is a permitted further cap operation. No other kind of repair is required to make the cut pieces essential.

**Proof.** Let $`D\subset B`$ be the empty disk between the return and an interval of the companion boundary. It contains no actual hole. It also contains no trace point of the original $`S`$. Indeed an original pattern arc entering $`D`$ cannot cross the new return, and cannot end at an actual hole in $`D`$. It would therefore be a whole outer return lying in this empty disk, contradicting the essentiality of the original pattern cut.

The two new trace points consequently lie in one gap between consecutive original trace points. In such a gap there are at most two new trace points, one small negative push-off from either bordering original piece. Thus these are the only new trace points in the gap. If the gap lies within one root block, its two new ends belong to consecutive original copies with signs $`(-,+)`$ in the fixed **linear packet order**, and the gap is part of their negative product region. If it crosses from one root block to the next, the two ends belong to the same original end piece and lie on its negative end side. These are exactly the regions in the displayed list.

The identified region cannot already have been resolved, since its boundary pieces would then be absent. Replacing all those boundary pieces by that region's outer annuli is an oriented cap operation on the same negative side. It removes the witnessed empty return, possibly creating other ones. Every possible empty return has just been accounted for. ∎

### 10.2. A confluent finite closure

Say that an unselected negative region is enabled when it has a witness as in Lemma 10.1. Start from any specified negative end region and repeatedly add enabled regions to $`U`$.

**Lemma 10.2 (closure and ordinary parent).** The final selected set $`U^*`$ is independent of the order of additions. After deleting its whole closed components, $`R_{U^*}`$ is an incompressible spanning vertex. Starting at the fixed first end, and using the side on which that end lies, this defines an ordinary parent $`p(S)`$ with

```math
q(p(S))\lt q(S),\qquad \delta(S,p(S))=1.
\qquad\text{(10.1)}
```

The retained companion pieces are an intrinsically specified subpacket of the original packet. Put $`p(a)=a`$ on $`\mathcal A`$.

**Proof.** If $`G`$ is enabled and another region $`G'`$ is resolved, its witnessing pattern arc is unchanged. Its two endpoints are on the boundary pieces of $`G`$, which are disjoint from the boundary pieces of $`G'`$. In the annular path-composition description, resolving $`G'`$ changes only paths ending at those other endpoints; a complete path between the surviving endpoints of $`G`$ persists. Its empty-disk class persists too. Thus enabling is monotone under adding other regions.

This is a finite monotone closure process on the original chamber set, whose boundary-piece sets are disjoint. It has a unique least closed superset of the seed. Closed components containing companion pieces were deliberately not deleted during this process, so no change of the original chamber set or of this monotonicity is being hidden. Closed pattern circles have no endpoints and affect no enabling test. A first end on the positive side is treated by exactly this construction with the names of the two normal sides reversed.

At the terminal set there is no boundary-parallel pattern return, by Lemma 10.1. The retained companion pieces are essential copies of $`F_\gamma`$. All cut pieces are therefore essential, and the gluing disk argument makes every actual-bearing component incompressible. Delete the whole closed components now. Every actual boundary remains, and the seed removed at least one companion piece.

The seed operation changes just the connected component $`C`$ of $`S`$ containing its end piece. Every enabled product operation has a pattern arc joining its two boundary pieces, so both already lie in the same current component. No operation can join two previously separate original components. The unchanged original components have essential unchanged pattern cuts and never enable an operation. Thus only $`C`$ is replaced; the remaining components are common. Section 8.1's shared-component observation gives the cyclic edge in (10.1), even if the replacement of $`C`$ splits into several actual-bearing components.

Finally the ordinary efficient comparison preserves the ordered packet, its end, its normal-side chambers, and the pattern arc classes. The zero-loop lemma removes an unnoticed permutation of the companion boundary circles. Empty-disk tests and annular cap composition are invariant under these isotopies. The monotone closure and the final whole-component deletion are consequently ordinary invariants. The parent, including the identities in packet order of its retained pieces, is well-defined. ∎

There is no appeal here to uniqueness of maximal compression. The proof normalises an explicit same-side cap diagram by a finite ordinary closure.

**Lemma 10.3 (compatibility at an empty end).** Suppose $`S`$ belongs to a finite disjoint incompressible family in the same sector, and its first companion piece is first in the entire family's packet. Then $`p(S)`$ can be represented disjoint from that whole family. Its retained companion pieces can be kept in the same relative positions as before.

**Proof.** The seed end is empty of all other companion pieces. Use sufficiently small collars so that the first raw resolution avoids the family. At a subsequent enabled empty disk, the argument of Lemma 10.1 applies separately to every other member of the family: its essential pattern arcs cannot enter that empty disk. Hence no other trace point lies in its outer interval. In the common parallel packet, the repair product or end region is therefore empty of all other pieces. The cap move can be made there without meeting them. The same reasoning applies at every step, and deletion of whole closed components preserves disjointness. The small push-offs never cross a retained companion piece, so the remaining packet order is unchanged. ∎

For the genus-seven example, this repairs the failures explicitly. Starting at the first end selects that end and then the negative product region between copies $`2,3`$, leaving just copy $`1`$. Starting at the last end selects that end and then the positive product region between copies $`1,2`$, leaving just copy $`0`$. In each case the four actual boundaries tether to the surviving four-boundary piece, giving a genus-one parent. Thus that vertex has distance exactly two from the annular set: its companion height range is two and its parent has one piece.

### 10.3. Face-compatible coloured packet orders

The parent need not dominate every neighbour, and its single iteration need not be a simplicial map. We instead use complete parent trajectories and order their events within a cyclic simplex.

**Lemma 10.4 (ordinary coloured order).** For each cyclic simplex in a fixed sector there is a distinguished linear order of all its coloured companion occurrences, compatible with passage to a face. Occurrences shared by whole components are restored in an order specified by the rooted Part 7 component-wall construction. This order can be realised by simultaneous representatives.

**Proof.** Normalise the whole family and use the ordinary collapsed-component-wall convention of Part 7, Section 9. The simultaneous-union input here is precisely Sakuma Proposition 4.9(2), as used in Part 7, Section 9.1, together with its shared-component packet argument; no stronger labelled-union theorem is assumed. Root the integral difference potentials in the chosen end chamber of $`Q`$. They form a nested chain, so exact recovery orders the vertex phase intervals independently of positive weights.

More explicitly, let $`n_i`$ be the integral value of the $`i`$th lifted band map just below one component wall $`C`$, and let $`b_i\in\{0,1\}`$ indicate membership of $`C`$ in that vertex. The two band endpoints have phases

```math
\sum_i t_i n_i\pmod1,\qquad
\sum_i t_i(n_i+b_i)\pmod1.
\qquad\text{(10.1a)}
```

In chain order, the $`n_i`$ are nondecreasing and take at most two consecutive integer values; the same holds for $`n_i+b_i`$. Hence both phases are fixed partial-sum breakpoints of the ordered vertex intervals. The vertices containing $`C`$ occupy one cyclically consecutive set of these intervals, since its band has length $`w_C=\sum_i t_i b_i\le1`$. If every vertex contains $`C`$, its full-length band's start is still the specified breakpoint, so that case introduces no unchosen rotation.

On a positive companion occurrence of that wall the restored coloured copies follow this interval order; on a negative occurrence they follow its reverse. This fixes the coloured order at every occurrence. The order of the distinct collapsed companion occurrences themselves is preserved by the ordinary outer-torus comparison and the zero-loop packet detector. Thus the complete linear order is ordinary and realisable by choosing generic phases in the exact-recovery intervals.

When a vertex weight becomes zero, its phase interval disappears. All the remaining intervals keep their order, and unsupported wall bands disappear. Consequently the coloured companion order on a face is precisely the restricted order, with the deleted colour removed. Shared whole-component permutations cause no extra choice because they were collapsed before this construction. ∎

### 10.4. Multistep prisms contract every signed sector

For a nonannular vertex $`v`$, iterate its ordinary parent until it is annular:

```math
v=v^0,\ v^1=p(v),\ldots,\ v^{\ell(v)}=a(v),
\qquad \ell(v)\le q(v).
\qquad\text{(10.2)}
```

Each step retains a subpacket of the preceding one and removes its first piece. The successive first pieces, recorded in the initial packet of $`v`$, therefore occur in strictly increasing order. They label its successive events. All these data are ordinary invariants by Lemma 10.2. For an annular vertex use one stationary event with $`v^0=v^1=v`$.

Take a cyclic simplex $`\sigma`$. Merge the event lists of its vertices using the coloured companion order of Lemma 10.4; place stationary annular events afterwards in any fixed global order of annular vertices. At each genuine event its piece is first among all currently retained pieces: each vertex's next event is its own first retained piece. Lemma 10.3 therefore permits that parent step while preserving geometric compatibility with every other current vertex. By induction all intermediate states and each union of two consecutive states are geometric simplices. The final state consists entirely of annular vertices. If two state vertices become ordinarily equal, keep their labelled parallel occurrences for the geometric argument and identify their duplicate vertices only in the simplicial map; the barrier and packet arguments also apply to these finite repeated occurrences.

Here are explicit compatible prism subdivisions; there is no need to rescale time differently on different faces. On the vertical edge above $`v`$, put its trajectory vertices at heights $`j/\ell(v)`$, or at $`0,1`$ for a stationary annular event. Starting with the bottom state, process the merged events one at a time. A state defines the affine height function on $`\sigma`$ with those current heights at its vertices. Each event raises one of those heights. The slab between two consecutive affine graphs is the simplex spanned by the old state and the one new trajectory point. These slabs tile $`|\sigma|\times I`$ from height zero to height one. Deleting a vertex deletes its events, and their slabs have zero thickness on that face; all other heights and event orders remain unchanged. Thus the subdivisions agree on every face.

Map each trajectory point to its ordinary surface vertex. The geometric compatibility proved above makes this a simplicial map on every prism slab. It gives a homotopy

```math
H_\gamma:|X_\gamma|\times I\longrightarrow|Y_\gamma|
\qquad\text{(10.3)}
```

from the inclusion to the annular vertex map $`a`$. It fixes the annular cyclic subcomplex pointwise. On a closed simplex cylinder there are only finitely many events and finitely many carrier vertices. Hence the face-compatible construction is continuous in the ordinary CW product topology, without a uniform bound on $`q`$.

The Part 7 component-wall retraction restricts to $`Y_\gamma`$, since whole-component recombination retains the same companion class. Compose (10.3) with this retraction. The initial map is the identity on $`X_\gamma`$; the final map lands in the annular cyclic complex; and that complex is fixed throughout. We have proved

```math
|X_\gamma|\ \searrow\ |X_{\mathcal A}|,
\qquad\text{(10.4)}
```

a strong deformation retraction for every signed sector, including $`k\ge2`$. This is also compatible with bounded packet-count subcomplexes after the coefficient correction of Section 7.1. Along a parent trajectory every vertex count decreases, so the geometric prism above an input simplex with $`q\le n`$ has all its vertices at count at most $`n`$. After composition with Part 7, its PL count is still at most $`n`$. Applying $`D_n`$ keeps the homotopy in the induced cyclic subcomplex $`q\le n`$, fixes its annular part, and leaves the annular endpoint unchanged. Hence every such bounded cyclic subcomplex strongly deformation retracts onto the annular cyclic complex. The filtered comparison gives contractibility of its bounded geometric counterpart as well.

The annular cyclic complex is contractible. Thus $`X_\gamma`$ and, by the restricted Part 7 comparison, $`Y_\gamma`$ are contractible. The same construction restricts to either coherent coorientation, as used in Section 8.4.

Now use (6.1). The fibre sector is contractible, all cancellation sectors are contractible, and every intersection of different sectors is the contractible annular complex. Collapsing that common subcomplex yields a weak/CW wedge of contractible sector quotients. Therefore the full $`Y(L_4)`$ is contractible, and Part 7, Theorem D gives the full $`X(L_4)`$ conclusion. This proves the square-knot part of Theorem 1.9.

### 10.5. Mirror-torus composites and any number of parallels

For $`K=T(p,q)\#\overline{T(p,q)}`$, replace $`6,-6`$ by $`pq,-pq`$. The same two companion modes remain. In the cancellation mode every composing piece is still a pants section and every leaf piece is still an annulus, so a connected companion is still genus one with $`2k`$ boundaries. The quotient is the four-cone orbifold $`S^2(p,q,p,q)`$.

Its paired-cone construction gives a surface cover of degree $`pq`$ and genus $`(p-1)(q-1)\ge2`$. The peripheral cyclic subgroup in $`C_p*C_q`$ is malnormal: the primitive length-two boundary word has no axis reversal, since coprimality excludes $`p=q=2`$. Thus the ordinary curve detector, the zero outer-loop proof, and the single-packet catalogue remain valid. Disjoint essential curves on its underlying four-marked sphere remain parallel. All arguments in Sections 10.1--10.4 consequently apply with any balanced number of labelled actual holes. Neither the monotone chamber closure nor the multistep prism needs the four-hole component bound.

If the parallel orientations have nonzero signed total, the spanning class evaluates nontrivially on the composing and leaf fibres. Every efficient companion cut is then horizontal, so all companions are one-boundary spanning fibres. The entire complex is the capped-fibre partial-matching sector, contracted by the phase argument of Section 7. The one-parallel case is the fibred-point case. This proves the mirror-torus subfamily of Theorem 1.9.

### 10.6. The gap-orbit extension to connected sums of torus knots

We derive the additional packet facts needed for (1.5), rather than citing the extension in Part 8. A single torus-knot companion has only the longitudinal fibre mode, already covered, so assume $`s\ge2`$ in this calculation. Put $`s_i=p_iq_i`$ and let $`g_i`$ be the genus of the $`i`$th torus-knot fibre. The same root horizontal-piece calculation gives a subset of vertical terminal leaves

```math
V\subseteq\{1,\ldots,s\},\qquad \sum_{i\in V}s_i=0.
\qquad\text{(10.5)}
```

For $`V=\varnothing`$, the companion is the one-boundary spanning fibre. For $`V\ne\varnothing`$, let $`v=|V|\ge2`$ and $`g_H=\sum_{i\notin V}g_i`$. The horizontal cluster is a bundle with connected fibre $`H`$ of genus $`g_H`$, with one root boundary and one boundary at each vertical terminal. Its primitive phase has root meridian degree one. A simultaneous normal system consists of $`N`$ parallel $`H`$ sheets and reflection packets

```math
L_j(i)=c_j-i\pmod N,\qquad j\in V,
\qquad\text{(10.6)}
```

where $`N`$ is even and every $`c_j`$ is odd. The signs reverse across each reflection. Disjoint horizontal systems have one common primitive class, so a whole disjoint family has one such mode $`V`$.

**Lemma 10.5 (gap-orbit packet lemma).** Set

```math
g=\gcd\bigl(N,\{c_j-c_{j_0}:j\in V\}\bigr),
\qquad q=g/2,\qquad k=N/g.
\qquad\text{(10.7)}
```

The companion system has $`q`$ connected components, each with $`2k`$ root boundaries and genus

```math
1+k(v-2+2g_H).
\qquad\text{(10.8)}
```

All of them are jointly parallel. The complementary-region incidence is a linear path with two end regions and $`q-1`$ actual product regions.

**Proof.** The point action is generated by translations through the differences $`c_j-c_{j_0}`$ and one odd reflection. Modulo $`g`$, its orbits are the $`g/2`$ pairs of residues under that reflection. Each orbit has $`2N/g=2k`$ sheets. Since $`\chi(H)=1-v-2g_H`$, the Euler characteristic and the $`2k`$ root boundaries give (10.8).

Number the gaps between successive $`H`$ sheets by $`i\in\mathbb Z/N`$. The leaf gap reflection is

```math
G_j(i)=c_j-1-i\pmod N.
\qquad\text{(10.9)}
```

Modulo $`g`$, this is one even reflection. It has two fixed residue classes and $`(g-2)/2`$ paired classes, giving exactly $`q+1`$ gap orbits. Every terminal endcap projects to one of the two fixed classes. Both fixed classes actually contain endcaps: if $`k`$ is odd, the two endcaps of one leaf project to the two different fixed classes; if $`k`$ is even and only one class occurred, all differences $`(c_j-c_{j_0})/g`$ would be even, contradicting the defining gcd.

The quotient of the alternating cyclic point-gap incidence by these reflections is an interval: the $`q`$ point orbits are its edges and the $`q+1`$ gap orbits are its vertices. Every non-end gap orbit contains only horizontal products $`H\times I`$ and rectangular leaf regions, with no endcap. Their gluings are an interval bundle whose two horizontal boundary components are the two adjacent companion components. Such an interval bundle is their product. Thus all adjacent components, and hence all components, are parallel. This proves the asserted actual product regions, not just an equality of numerical profiles. ∎

It remains to check an ordinary port loop. Collapse the horizontal cluster by its bundle map to a circle $`E`$, and project each vertical terminal to its two-cone disk. The resulting group is a graph-of-groups amalgam with central group $`\langle d\rangle`$ and terminal groups

```math
C_{p_j}*C_{|q_j|},\qquad j\in V,
```

whose boundary cyclic groups are identified with $`\langle d\rangle`$. The root meridian maps to $`d`$ and the root longitude to the identity. The image of a connected companion's fundamental group is the free subgroup carried by its finite sheet-and-annulus incidence graph. To justify this assertion, give every sheet vertex trivial group. It has one incident edge of each terminal type. At a terminal vertex the essential annulus joins two different peripheral cosets. A reduced graph path is therefore reduced in the ambient graph of groups; no nontrivial such path belongs to a conjugate of the central cyclic group. This is an immersion of the incidence graph into the Bass--Serre tree quotient, so the image subgroup acts freely on its lifted subtree. The finite incidence graph has no vertex of valence one, since $`v\ge2`$, and is its own core.

If $`d^\ell`$ normalises this subgroup, it preserves its minimal invariant subtree and fixes its root central vertex. It induces an automorphism of the finite quotient core graph. Some power induces the identity; its lift fixing the root is then the identity on the whole subtree. At a terminal vertex this fixes two distinct incident edges. Their stabilisers have trivial intersection, because the primitive peripheral subgroup in $`C_{p_j}*C_{|q_j|}`$ is malnormal; coprimality excludes the only two-involution axis-reversal case. Hence that power of $`d^\ell`$ is the identity, and $`\ell=0`$.

Tracking an ordinary surface loop as in Lemma 4.1 proves zero outer configuration winding, including finite packet permutations. Notice that this is an ordinary group detector; no isotopy of the intermediate surfaces through horizontal normal forms is assumed.

Now any simultaneous nonempty cancellation family is one linear packet by Lemma 10.5. Its ordinary connected companion class supplies its sector label; a numerical profile is not substituted for that ordinary class. The one-sided closure, the relative empty-end property, and the coloured multistep prisms of Sections 10.1--10.4 apply unchanged. They use essentiality, parallel products, and the zero-loop detector, and do not require genus one or a four-marked-sphere coordinate. In a fixed sector use $`q(S)=\chi(S)/\chi(F)`$; this is again a component-additive ordinary count, so the filtered argument remains valid. Different ordinary companion classes cannot coexist in a disjoint family, while every sector contains the annular subcomplex. The same sector gluing proves contractibility for balanced parallel clusters of (1.5). For nonzero signed total, all cuts are horizontal and the capped-fibre argument applies as before. This completes Theorem 1.9.

[Overview](../README.md) · [Previous page](part9-2.md) · [Next page](part9-4.md)
