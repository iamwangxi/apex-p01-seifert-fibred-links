# Part 12. Framed recursive parallels and weighted supports (continued)

[Overview](../README.md) · [Previous page](part12-2.md) · Part 12, page 3 of 3

## 7. An anchored leaf operation that can actually be iterated

For this anchored operation one needs only a **single** outer boundary, rather than full longitudinal rigidity against all cancellation pieces. Every recursive graph knot has the following property: an orientable connected essential surface with exactly one preferred-longitudinal boundary is its fibre, with either orientation. Indeed its nonzero spanning class has nonzero evaluation on every block fibre, as follows inductively from the meridian, sum and cable homology relations. All cuts are horizontal, and unit outer usage propagates the single whole fibre. Alternatively (6.1) forbids a vertical cap on a lone signed root sheet. Finite such fibre systems are jointly parallel. This includes the square knot, whose many-boundary longitudinal rigidity fails.

**Theorem E (boundary fibre decoration).** Let $`L`$ be a non-split graph link and $`J`$ any recursive graph knot (or any of the longitudinally rigid fibre caps). Replace any actual component $`L_i`$ by its connected sum with $`J`$, formed in a small ball meeting only that component. Then the full geometric complexes before and after the operation are simplicially isomorphic. Consequently contractibility of both $`X,Y`$, with the strong comparison, is preserved. The operation can be repeated at any actual components.

**Proof.** If the old link is the unknot, both complexes before the operation are points, as are those of $`J`$, so deal with that case separately. Otherwise the old boundary is incompressible. The new exterior has a composing pants block with the new actual boundary and two ports, one to the old exterior and one to $`E(J)`$. Its Seifert fibre is the actual meridian, of spanning evaluation one after orienting that meridian. Unit usage at that actual torus forces exactly one connected horizontal section; it has one boundary at each port. At the knot port its slope is the preferred longitude. The preceding single-boundary property gives one $`J`$-fibre; no other component can be hidden there because a detached component would be whole closed. Thus restriction gives a reduced incompressible system in the old exterior with exactly the original boundary usage. A compression disk there would remain a compression disk of the new system; a whole closed old component could not attach to the new blocks and is forbidden.

Conversely attach the section and $`J`$-fibre to any old system. Their essential cuts give an incompressible new system. The genus of the component containing the decorated actual boundary increases by $`g(J)`$; other components are retained.

There is no extra ordinary integer. With pointwise fixed traces the section has $`\mathbb Z^3/\mathbb Z`$ boundary phase states. Fix the old port lift. Motion of the new actual boundary removes its integer, and a full one-port bundle circuit of the $`J`$-fibre removes the other. Configurations, rather than independently parameterised boundary points, are used. The fixed-slope product comparison gives the converse restriction of arbitrary ordinary isotopy at the two ports. The fibred exception is harmless: when the old graph class is fibred, the whole anchored horizontal construction on both sides gives a single vertex. Otherwise a zero-evaluation graph block gives the injected $`\mathbb Z^2`$ in the original kernel, also excluding the exception after the operation.

For a finite disjoint old family, its old-port configuration extends by parallel sections and one common $`J`$-fibre configuration; positive phase interpolation matches the boundary paths. They give simultaneous whole extensions. Restriction of a simultaneous new family is the simultaneous old family. This proves the ordinary vertex bijection and the exact geometric simplex criterion, hence the simplicial isomorphism of $`Y`$. Part 7, Theorem D then transfers contractibility to $`X`$, without requiring an unproved all-pair cyclic isometry. ∎

This two-port operation is anchored: its actual meridian has value one and its knot restriction is nonzero. It is not the zero-class several-invisible-port setting ruled out by Part 9, Remark 11.3.

**Corollary E′ (unit fibre-pattern substitution).** The same simplicial $`Y`$-isomorphism holds when the single actual boundary is replaced by any stipulated actual graph pattern with one outer port, provided its inherited class has nonzero evaluation on every block fibre, its connected bundle fibre has exactly one outer boundary, and the outer restricted class and slope agree with those of the old actual torus. Every new actual boundary still has unit usage.

Indeed actual unit usage and horizontal propagation force exactly that one fibre in the added pattern. Its full bundle circuit has degree one at the outer port and removes the last relative gluing integer. Restriction, essential extension, fixed-slope ordinary comparison and simultaneous positive phases are exactly the proof of Theorem E. For the old unknot, cap the single outer fibre boundary by the meridian disks of its solid-torus exterior. This extends the bundle; the graph classification gives the single whole fibre on both sides. These assertions are about the actual pattern, not a proposed arbitrary splice matrix.

An explicit operation is to add $`2r`$ small meridians of one actual component, $`r`$ of each orientation. The old component remains. Their total effect on the class in the old exterior is zero. The added composing product has fibre the old meridian, of evaluation one, and connected planar fibre with one outer boundary and $`2r+1`$ actual boundaries. It satisfies the corollary. Thus balanced meridian additions, as well as recursive graph-knot decorations, preserve the entire geometric complex.

## 8. Actual examples for all four branches

Every construction below is in $`S^3`$; the stated Seifert blocks are genuine unless a separately handled fibre-matching case is specified. Non-splittability follows from their irreducible pieces with injected boundary, or from the nonzero linking in the framed two-component examples. Essential assembly proves the displayed vertices; a finite incidence graph by itself would not do so.

### (a) Several auxiliary modes, already with two actual components

Let
```math
K=T(2,3)\#T(2,3)\#T(2,-3),\qquad f=6,
\qquad\text{(8.1)}
```
and take one positive and one negative $`f`$-parallel. The mode weights are $`(6,6,-6)`$. Equation (4.2) has $`V=\{1\},\{2\},\{1,2,3\}`$. The first two have $`g_H=2`$ and a two-boundary companion of genus four; the third has $`g_H=0,v=3`$ and one of genus two. At least the genus-two and genus-four ordinary companion classes differ. Their horizontal clusters do not share one auxiliary fibre circle.

Theorem A contracts this entire complex by ordinary-sector gluing. These actual components have linking number of absolute value six, so this is not a zero-framed parallel cluster disguised by a change of name.

### (b) A genuine higher-degree frontier

Here is a solved example with only two actual components. Let
```math
K=C_{2,1}(T(2,3)),\qquad f=24,
\qquad\text{(8.1a)}
```
and take opposite $`f`$-parallels. The companion cable block has horizontal primitive class
$`\eta(\mu_K)=1,\eta(\lambda_J)=-12,\eta(\mu_J)=2`$.
Its root degree is one, its trefoil frontier degree is two, and
```math
\chi(R)=-11,\qquad |\partial R|=3,\qquad g(R)=5.
```
Two oppositely signed copies of $`R`$, joined by two essential trefoil returns, give a connected companion with two actual-facing boundaries, Euler characteristic $`-22`$ and genus eleven. Tether them to the two actual boundaries. The interface fibre intersections are $`22`$ and $`11`$; both tori are genuine. Theorem G contracts the entire complex, not only this vertex's normal-data model. This is minimal in actual count for a balanced nonempty parallel cluster.

There is a different, still unresolved, higher-degree example whose central cluster has no vertical cap:

Use three Hopf support fibres with framings $`(-3,-3,-1)`$, as in (3.2). Use one balanced pair at each of the first two supports and **two** positive and two negative parallels at the third. There are eight actual components. The central primitive fibre has degree four over the pants, port multiplicities $`(1,1,2)`$, genus one and four boundaries.

Take one copy with each sign. At the first two patterns use their two tethers. At the third, a five-holed-sphere pattern, tether all four port circles to its two positive and two negative actual boundaries. The whole system has two components, each of genus one with four actual boundaries. All tethers are essential, so this is a genuine incompressible spanning vertex. Lemma C does not apply to the third pattern.

This exhibits an active higher-degree mode, not merely an algebraically possible kernel. Theorem G is not applied to this distributed-pattern link.

### (c) More actual holes can join the two parity components of Part 11

Use the original Hopf support with framing $`-2`$ at all three leaves, but use two balanced pairs at leaf two. Again there are eight actual boundaries. Take six central fibres with sign word $`+++---`$. At leaves zero and one use the usual pants axes $`0,2`$. At leaf two use actual tethers at positions $`0,1,3,4`$, and the return joining $`2`$ to $`5`$.

The return separates the two actual holes tethered at $`3,4`$ from those tethered at $`0,1`$, so it is essential. The other tethers are disjoint in their two sides. The first two reflections alone have the two parity components; the $`2`$-to-$`5`$ return joins them. Thus the whole surface is connected, has eight actual boundaries and Euler characteristic $`-18`$, hence genus six. The two-orbit/Farey-tree conclusion of Part 11 is not available for this diagram.

For a completely solved more-actual-hole example, take four balanced $`f=6`$ parallels of (8.1). Theorem A permits any actual count and contracts its several modes. The eight-component construction shows the additional difficulty when the extra holes are in a different actual branch of a multiport cluster.

All four phenomena also coexist in one solved example: cable (8.1) by $`C_{2,1}`$, use framing $`24`$, and take four balanced parallels. The singleton vertical-subtree modes have $`\chi(R)=-19`$, frontier degree two and a genus-nineteen two-boundary cancellation companion. The three-terminal mode has $`\chi(R)=-15`$, frontier degrees $`(2,2,2)`$ and a genus-fifteen two-boundary companion. The genus distinction detects different ordinary sectors; all their return caps lack actual tethers. Theorem G handles the full link with four actual holes in its single pattern.

### (d) Free vertical returns and a four-component multiport closure

For a solved two-component example, take $`K=T(2,3)\#T(2,3)`$ and framing $`f=6`$, with opposite orientations. Either singleton vertical mode has a horizontal cluster of genus one with two boundaries, joined by a vertical return in the other torus-knot block. That vertical block has no actual tether. Lemmas B and D and Theorem A apply.

The more stringent test has four actual components. Take two zero-framed support parallels $`J_1,J_2`$ of $`J=T(2,3)`$. Inside each use one positive and one negative parallel of framing $`12=2pq`$. The actual exterior has:

- an actual-free composing pants $`H`$ of the two support parallels;
- two actual pants patterns with outer slope $`\lambda_i+12\mu_i`$;
- the actual-free torus-knot block $`E(J)`$.

On $`H`$ choose the primitive auxiliary class
```math
\eta(\lambda_J)=12,\qquad
\eta(\mu_1)=\eta(\mu_2)=-1,\qquad
\mu_J=\mu_1+\mu_2.
\qquad\text{(8.2)}
```
The root restriction is $`(\eta(\mu_J),\eta(\lambda_J))=(-2,12)`$, of degree two and kernel $`6\mu_J+\lambda_J`$, exactly the trefoil Seifert fibre. At the two actual patterns the primitive degrees are one. The central fibre has
```math
\chi(R)=-12,\quad |\partial R|=4,\quad g(R)=5.
```
Take $`R`$ with each sign. Their four root trace circles have word $`+-+-`$. Two parallel essential vertical annuli in the trefoil block pair opposite signs. The actual patterns use only tethers. The resulting system is connected, has four actual boundaries, Euler characteristic $`-24`$, and genus eleven.

The three interface fibre intersections are $`12,12,6`$, so all are genuine. There is no actual tether in the trefoil return block. This is an actual active degree-two port of an unanchored horizontal cluster with another two external ports. It is the $`m=2,w_1=w_2=1,t=6`$ instance of Theorem K and is therefore completely contracted. Its support cuts are parallel copies of one genus-eleven four-boundary class, seen at both actual patterns; Theorem I uses their common order.

Its pairwise linking matrix has nonzero entries of absolute value twelve within the two chosen pairs and zero cross entries. Thus it is neither a uniform framed parallel cluster nor a zero-framed cluster; its unanchored zero-class central block also violates the capped-core hypothesis. The construction is minimal in actual count within the “two balanced pants branches and one free torus-knot return” setting: both actual branches require two actual boundaries.

### 8.1. Exact component obstruction in the four-component test

The last example admits a stronger conclusion than existence of one high-genus vertex.

**Proposition H (the four-component closure and repeated-axis failure).** In the four-component link (8.2), $`X=Y`$ and this complex is contractible. There is exactly one vertex with empty support, the two-annulus vertex $`A`$. Every other vertex is connected, uses $`N=2r`$ central fibres, and has genus $`12r-1`$. In a normal diagram let $`a,b`$ be its positive tether axes at the two actual pants, and let the free trefoil-return reflection have offset $`c\bmod 2N`$, necessarily odd. Reducedness implies
```math
\gcd(N,2(b-a),c-2a)=1 .
\qquad\text{(8.3)}
```
When $`a\ne b`$, the signed equations further imply
```math
c\equiv a+b+r\pmod N .
\qquad\text{(8.4)}
```
Repeated actual axes $`a=b`$ are possible for arbitrarily large $`r`$. Thus the repeated-axis exclusion of a tether-only star fails as soon as the degree-two free-return cap is present.

**Proof.** Any nonempty support trace meets both actual patterns. Their two degree-one frontier equations give
$`\eta(\lambda_J)+12\eta(\mu_i)=0`$.
Primitivity gives exactly the class (8.2), up to sign. Its inner trace is the trefoil fibre, so that block is vertical. A horizontal trefoil restriction would instead force $`\eta(\lambda_J)=0`$, making the entire horizontal class zero. A support-vertical trace cannot meet the two mismatched actual pattern fibres. Thus these and the empty-support mode exhaust all efficient vertices.

For a nonempty diagram, the two actual pants give the reflections
$`j\mapsto2a-j,2b-j`$ on $`\mathbb Z/N`$, with their fixed positions as actual tethers. The free cap has expanded word of length $`2N`$ and reflection $`j\mapsto c-j`$; it induces the latter reflection modulo $`N`$, with two incidences per sheet. Actual signs balance, so $`N=2r`$, and the perfect cap matching makes $`c`$ odd.

Put $`g=\gcd(N,2(b-a),c-2a)`$. It is odd. It divides $`b-a`$ and $`r`$, so all four actual defects $`a,a+r,b,b+r`$ have residue $`a\bmod g`$. If $`g>1`$, a different dihedral residue orbit gives a complete surface component without actual boundary. Reducedness forbids it. Hence $`g=1`$, the reflection action is transitive, and the whole surface is connected. Its Euler characteristic is $`-12N=-24r`$; four actual boundaries give genus $`12r-1`$.

For (8.4) write $`z=e^{2\pi i/N}`$, $`E=\sum_j\epsilon_jz^j`$. The two tether equations and the perfect-return equation are
```math
E+z^{2a}\overline E=4z^a,\quad
E+z^{2b}\overline E=4z^b,\quad
E+z^c\overline E=0.
\qquad\text{(8.5)}
```
When $`a\ne b`$, their difference gives
$`(z^a+z^b)\overline E=4`$. The sum cannot vanish, and substitution in the third equation gives $`z^c=-z^{a+b}`$, exactly (8.4).

For repeated axes set $`a=b=0,c=1`$. Take $`\epsilon_0=+1`$, $`\epsilon_1,\ldots,\epsilon_r=-1`$, and $`\epsilon_{r+1},\ldots,\epsilon_{2r-1}=+1`$. Both pants tether at $`0,r`$; both their returns and the expanded free-cap reflection pair opposite signs. Equation (8.3) holds. Essential assembly gives a connected actual vertex for every $`r\ge1`$. The case $`r=1`$ is the displayed genus-eleven vertex.

With empty support, each actual pants has its unique actual-to-actual seam. Empty-interface ordinary comparison gives exactly $`A`$.

For $`X=Y`$, apply the Part 7 component-wall retraction to any geometric simplex. Its generic output recombines whole input components. Every input other than $`A`$ is connected and already uses all four actual tori; if no such component is chosen, both components of $`A`$ must be chosen together. Hence every output is an input vertex. The phase measure of the output at a vertex equals its input coefficient, read on any actual meridian (on either annular component for $`A`$). Thus the component-wall map is the identity on this geometric simplex. Its image lies in $`X`$, so the simplex already lies in $`X`$. Contractibility follows from Theorem K. This proves the proposition. ∎

No two distinct vertices of this example share an ordinary connected-component class. That fact alone would not prove the exchange axiom or contractibility. The complete proof here instead uses the common separating packet and the global same-side closure of Theorem I. No tree conclusion or all-pair metric formula is asserted.

### 8.2. A four-component obstruction with several free return types

**Proposition M (the common-packet hypothesis fails in an actual four-component link).** Put
```math
K=J_1\#J_2\#J_3,\qquad
(J_1,J_2,J_3)=(T(2,3),T(2,5),T(3,4)).
\qquad\text{(8.6)}
```
Take two zero-framed support parallels of $`K`$. Replace the first by one balanced pair of framing $`-2`$, and the second by one balanced pair of framing $`+2`$. This is a non-split four-component graph link with seven genuine Seifert blocks. It has a connected genus-five incompressible spanning vertex whose support cuts include **two disjoint nonparallel essential separating surfaces**, both of genus one: one has two boundaries at each actual-facing support port, the other has four at each. Thus a common separating packet does not follow from a single auxiliary horizontal mode, zero support class, unit actual-facing degrees, or all-port visibility. Resolving one of its support end pieces also gives a compressible actual-bearing output; the new empty return lies in an originally mixed-side chamber.

**Proof.** Its support consists of $`H=P_3\times S^1_\lambda`$, the outer composing product of the two support parallels, and $`E(K)`$. The root block $`V=P_4\times S^1_\mu`$ of $`E(K)`$ has three child torus-knot ports. All support restrictions of the original $`\Phi`$ vanish. On $`H`$ use
```math
\eta(\lambda)=2,\quad\eta(\mu_1)=1,\quad
\eta(\mu_2)=-1,\quad\eta(\mu_K)=0 .
\qquad\text{(8.7)}
```
Its primitive connected fibre $`R`$ is a four-holed sphere: $`\chi(R)=-2`$, actual-facing degrees $`1,1`$, inner meridional degree two. The block $`V`$ is vertical and all three child ports are unused; a torus-knot child has no meridional essential trace.

Take six $`R`$'s, indexed $`0,\ldots,5`$, with signs
```math
(\epsilon_0,\ldots,\epsilon_5)=(+,+,-,+,-,-).
```
At **each** actual pants use central-positive axis $`1`$ in the $`\eta`$-oriented endpoint convention: actual tethers are at $`1,4`$, and the two returns are $`(0,2),(3,5)`$. Choose the labelled actual orientations accordingly; each pattern has one of each sign. The returns pair opposite signs and each separates the two actual holes.

The meridional trace in $`V`$ is this word repeated twice, on positions $`0,\ldots,11`$. Use the six noncrossing returns
```math
(0,5),\ (1,2),\ (3,4),\ (6,11),\ (7,10),\ (8,9).
\qquad\text{(8.8)}
```
They pair opposite signs. To realise their essential isotopy types, place the unused child holes $`J_1,J_2,J_3`$ in the leaf regions at $`(1,2),(3,4),(8,9)`$, respectively. Every arc separates a nonempty proper subset of these three holes. The other complementary regions are rectangles or the central three-sided region. Thus all six vertical annuli are essential and disjoint. This is an actual arc system in the four-holed base, not just an abstract graph matching.

Reducing (8.8) modulo six, the support component graph has exactly the cycles
```math
\{0,5\},\qquad \{1,2,3,4\}.
```
The first component has two $`R`$'s and two annuli, Euler characteristic $`-4`$, four external boundaries and genus one. The second has four $`R`$'s and four annuli, Euler characteristic $`-8`$, eight external boundaries and genus one. Both have equally many signed $`R`$'s, so their dual classes vanish on the two support meridians; hence both separate the support. Their different boundary counts prove they are not ordinarily parallel.

Their ordinary port-loop image is still zero. The normaliser proof in Lemma G′ only needs the distinct degree-two boundary double cosets at a sheet and the essentiality of each returning annulus at its other vertex; it does not need the annuli to be parallel for this group calculation. Both surface trees still embed and have noncyclic sheet groups and degree-two annulus vertices. Apply the same argument at either actual-facing meridian, whose $`\eta`$-value is $`1`$ or $`-1`$. Thus nonparallel support geometry remains even after this ordinary-loop issue is removed.

The actual returns $`(0,2),(3,5)`$ join these two components. The whole surface is connected, has four actual boundaries and Euler characteristic $`-12`$, so its genus is five. Essential assembly proves its incompressibility, as well as essentiality of the two support pieces.

All interfaces are genuine: the actual pattern-to-$`H`$ fibre intersections are two, the $`H`$-to-$`V`$ intersection is one, and each $`V`$-to-$`J_i`$ intersection is one. Irreducibility with injected boundaries proves non-splittability. The horizontal/vertical/empty marking is forced in every nonempty efficient representative by (8.7) and the meridional exclusion at the children. In any such representative $`\chi(S)=-2N`$; this vertex therefore has $`N=6`$. Its trace counts are forced to be $`6,6,12`$ at the two actual-facing and the meridional interfaces, and zero at the children. The constructed representative has exactly these counts and is efficient. The ordinary fixed-slope comparison therefore cannot remove the exhibited two different support topologies by an alternative efficient marking.

Here is the explicit repair failure. Label the six $`H`$-phase gaps by $`j`$ after sheet $`j`$. The three connected support-complement regions have gap sets
```math
\{5\},\qquad \{0,2,4\},\qquad \{1,3\}.
\qquad\text{(8.9)}
```
This follows directly by gluing the boundary-gap regions of (8.8) through the degree-two port. Write $`F_A`$ for the $`\{0,5\}`$ support piece and $`F_B`$ for the other piece. The middle region has the **positive** face of $`F_A`$ and the **negative** face of $`F_B`$. Gap $`2`$, however, has two negative $`F_B`$ boundary occurrences. It is a local same-side gap in a globally mixed-side region.

Resolve the negative end piece $`F_A`$, using its boundary cap $`(5,0)`$ at both actual ports. The path
```math
2\longleftrightarrow0\longleftrightarrow5\longleftrightarrow3
```
leaves the new pattern return $`(2,3)`$ at each port, with tethers $`1,4`$ unchanged. Both returns bound empty disks. Their original support region is the mixed region in (8.9), not an unselected one-sided chamber with disjoint boundary-piece set.

The raw actual-bearing system is connected, has Euler characteristic $`-8`$, four actual boundaries and genus three. Pushing its two inessential returns into $`Q`$ gives a connected genus-three, four-boundary support piece. But every essential connected support piece in this link has genus one: if it uses $`s`$ horizontal $`R`$'s, it has Euler characteristic $`-2s`$ and $`2s`$ external boundaries, since all other cut pieces are vertical annuli. These data force genus one. The current two curves at each support port are already the least possible nonempty zero-class trace. Thus if the raw whole component were incompressible, essential cutting would give the impossible genus-three support piece. It is compressible. No whole closed component was responsible for this failure. ∎

The other end does give an individual descent. Resolving the positive end $`F_B`$ uses caps $`(1,2),(3,4)`$ at each actual port. The old tethers at $`1,4`$ then extend along $`1\!-\!2\!-\!0`$ and $`4\!-\!3\!-\!5`$. Only $`F_A`$ remains, with essential tethers and no return; it is a genus-one cyclic neighbour $`T`$ of the original genus-five vertex $`S`$.

In fact this vertex satisfies
```math
\delta(A,S)=2,\qquad N(S)/2=3 ,
\qquad\text{(8.10)}
```
where $`A`$ is the unique two-annulus vertex. The three pants seams realise $`T`$ disjoint from $`A`$; the whole-component argument makes this a cyclic edge. Hence $`S,T,A`$ gives the upper bound two, in the original $`\Phi`$-cover. For the lower bound, any simultaneous efficient family containing $`A`$ keeps $`A`$ outside the support: a nonempty essential support piece has negative Euler characteristic, whereas $`A`$ has Euler characteristic zero and its pattern pieces are annuli. But $`S`$'s six central sheets force two essential port returns at each actual pants. Each crosses its actual-to-actual seam of $`A`$. Thus $`A,S`$ are not geometrically adjacent; by $`X\subseteq Y`$ their cyclic distance is not one. This proves (8.10).

This is a special exact distance, not an all-pair minimum-width formula. It shows directly why bare half-sheet count is not a general depth. The example does **not** obstruct individual lower neighbours. The missing statement is an ordinary, whole-family-compatible choice or exchange carrier across these different support types.

The single-active-port block $`V`$ in this example has **three** unused features, in contrast to every return cap in Theorem J. Its essential waves need not be parallel. The support-complement region between the two displayed separating pieces is not a product, so Theorem I has no common packet to use. The example is minimal in actual count within two nonempty balanced pants replacements, each of which needs two actual components. It is an obstruction to the proposed replacement hypothesis and to the unrestricted original-chamber closure, **not** a proof that its $`X`$ or $`Y`$ is noncontractible.

## 9. The proved composition class and the obstruction to full induction

Start with any link in one of the following proved families:

1. the anchored horizontal class of Part 7, Theorem A;
2. the capped anchored-core class of Part 10, Theorem 1.1;
3. the Seifert-support balanced zero-framed families of Part 10, Theorem 11.2 and its stated extensions;
4. the integer-framed recursive graph-knot parallel families of Theorem G;
5. supports certified empty by Theorem C1;
6. distributed-pattern supports passing Theorem J, including Theorem K and Corollaries K1, L and L1.

Permit finitely many boundary fibre decorations from Theorem E or unit fibre-pattern substitutions from Corollary E′, including balanced meridian additions. Also permit the universal-empty-interface product operation whenever its factors are in the **relative** versions for which contractibility has been proved; whole-link results are not automatically promoted to relative results with new unused tori.

**Theorem F (certified composition class).** Every actual non-split graph link obtained by these operations has contractible $`Y`$, and hence contractible $`X`$ with the strong deformation comparison.

**Proof.** Items 1–3 are proved in Parts 7 and 10; 4 is Theorem G, 5 is Theorem C1, and 6 is Theorem J. Theorem E and Corollary E′ are simplicial $`Y`$-isomorphisms at the anchored pattern operations. At a universally empty torus the ordinary tuple and simultaneous product criteria apply, and the finite marginal-product homotopy contracts the union from the relative factor contractions. Induct on the finite list of certified operations. Part 7, Theorem D is applied only to the eventual actual whole link. ∎

This is a strict enlargement of each listed class in the sense of a common proved class containing it. For example (8.1) with nonzero framing and its genus-two/genus-four companions is outside the zero-framed Part 9 family, is not longitudinally rigid at the relevant companion slope, has an unanchored zero-class horizontal cluster, and is not a balanced zero-framed replacement of a Seifert support. Decorations can give its actual components different prescribed recursive graph-knot types, including nonrigid resonant ones such as the square knot, while retaining its geometric complex. The theorem does not claim closure under an arbitrary active splice.

The four-component edge in (8.2) is now closed. Theorem I identifies its repeated local chamber appearances globally and supplies its whole-family barrier. The explicit six-component family (6.17) also closes all four branches together with distributed actual patterns. Proposition M gives a different, still unresolved four-component link: several return types in a free composing block produce nonparallel support pieces inside one actual vertex. Even separation and all-port visibility therefore do not suffice without the common-packet hypothesis.

The induction stops when the invisible region does not reduce to one all-visible **separating** packet. In the eight-component examples of (b)–(c), the central cuts are parallel copies of a nonseparating fibre of the Hopf support. Their complement incidence is circular. There is no end chamber to seed Theorem I; removing one fibre would also violate its nonzero port class. Cancelling an opposite pair requires a choice of an adjacent product whose emptiness is compatible with the whole family, which the present proof does not supply.

There is an exact ordinary-loop distinction as well. In a cap-free bundle the fibre subgroup is normal, and its full bundle circuit gives nonzero simultaneous port configuration winding. Theorem I's zero-loop hypothesis is therefore false there, rather than an assumption one may quietly retain. At the four-actual-hole leaf, the signed tether equation has several defect terms, and the two-axis Fourier restriction used in Part 11 is not available. The example in (c) explicitly joins its two parity components.

These eight-component tests are minimal within the fixed three-Hopf-leaf balanced pattern setting for adding a branch with more than two actual boundaries: the six-component baseline has one balanced pair at each leaf, and one additional balanced pair raises the count to eight. No global smallest counterexample is claimed. A higher-degree test is likewise given in (b) with degrees $`(1,1,2)`$; Lemma C forces its degree-two pattern to have at least four actual holes.

More generally different horizontal clusters may meet different actual-facing port subsets. A local empty disk then need not exclude a whole other companion piece from the proposed global repair region; the all-port-visibility step in Theorem I fails. Several nonparallel companion labels can coexist, so their sector intersections are not identified by the common annular subcomplex. This is the precise missing replacement for a general JSJ induction. No noncontractible full complex has been found.

## 10. Computational record and inputs

The diagnostics enumerate finite normal-data and group equations. They do not enumerate all ordinary vertices of the remaining examples and do not identify a proxy graph with their actual $`X`$ or $`Y`$. Finite calculations only cross-check the arguments above.

`scripts/part12_checks.py` tests 214,740 expanded pants-axis conditions, 14,196 peripheral equations (including 1,521 cable/composing cases), 2,880 unweighted and 2,400 weighted packet configurations, 14,400 weighted end incidences, 892 mode markings of 140 recursive constructions, and 1,472 child-mode extensions of 2,904 admissible weighted support framings. Its signed extension checks 11,100 framing lists, including 6,898 nonintegral finite slopes, 3,756 integral finite slopes and 446 reciprocal-zero cases, with 2,676 meridional cable denominator checks.

`scripts/part12_common_packet.py` tests 1,238 end-seeded closures for several actual pants, followed by 5,444 closures on a sample of four-hole patterns, drawn with the fixed seed 60662026, with two or four boundaries per companion at each port. The latter sample includes 537 zero-tether port occurrences. `scripts/part12_free_returns.py` independently verifies Proposition M's planar arcs, support pieces, mixed gap region and bad end resolution, and 1,024 two-feature meridional Euler cases. Its small exact search checks 66 signed axis/matching choices through six $`R`$'s, of which 54 are reduced and 12 have unequal support boundary counts. These are diagrams, not ordinary vertices. The four-hole sample is explicitly bounded; none of these counts is a count of all ordinary vertices. The common-chamber path audit adapts the argument of Part 9, §10 and its finite path-composition test, with one global chamber selection applied at every port.

| Input | Exact use |
|---|---|
| [Part 7](part7.md), especially Theorems A and D | horizontal unit propagation; the whole-component comparison in the original spanning cover |
| [Part 8](part8.md) | recursive double-parallel range, used only for comparison of scope |
| [Part 10](part10.md), §§9.3, 10–11 | finite auxiliary classes, ordinary localisation, relative unused boundary and empty-interface products |
| [Part 9](part9.md), §§10–11 and Remark 11.3 | one-port packet result; same-side closure and whole-trajectory coloured prism arguments; the $`r\le1`$ filling restriction |
| [Part 11](part11.md) | motivating star and the four extensions; no theorem here assumes its tree conclusion |
| Banks, arXiv:1109.0965v1, Proposition 2.4 and §10 | cyclic-distance convention where used |

[Overview](../README.md) · [Previous page](part12-2.md)
