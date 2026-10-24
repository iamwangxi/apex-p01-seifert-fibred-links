# Part 9. Parallel clusters of connected sums of torus knots (continued)

[Overview](../README.md) · [Previous page](part9.md) · [Next page](part9-3.md) · Part 9, page 2 of 4

## 6. Geometric sectors and annular common links

### 6.1. Sectors

Let $`Y_\gamma`$ be the full subcomplex on $`\mathcal A`$ and the cancellation vertices with companion curve $`\gamma`$. Then

```math
Y=Y_{\rm fib}\ \cup\ \bigcup_\gamma Y_\gamma,
\qquad
Y_\gamma\cap Y_{\gamma'}=
Y_\gamma\cap Y_{\rm fib}=\mathcal A\quad(\gamma\ne\gamma').
\qquad\text{(6.1)}
```

Every simplex outside $`\mathcal A`$ belongs to exactly one of these sectors. To see this, normalise a whole disjoint union. Fibre and cancellation cuts have intersecting slopes on the leaf tori and cannot coexist. Cancellation cuts project to disjoint essential curves on the four-marked sphere and hence have the same $`\gamma`$.

The annular complex $`\mathcal A`$ is contractible by the planar matching-flow argument, with the companion hole retained as an unused marked boundary. The relative form needed next is proved explicitly.

### 6.2. The relative annular lemma

For a finite geometric simplex $`\sigma`$ define

```math
\mathcal A(\sigma)=
\{\tau\subseteq\mathcal A:\ \tau\cup\sigma\text{ is a simplex of }Y\}.
\qquad\text{(6.2)}
```

The definition allows shared vertices, so this is a closed common-star complex, not a link from which shared vertices have been removed.

**Lemma 6.1.** If $`\mathcal A(\sigma)`$ is nonempty, it is contractible.

**Proof.** Take essential simultaneous normal forms of $`\sigma`$, and a negative-curvature metric with geodesic boundary on $`B`$. Straighten their pattern arcs to orthogeodesic cores, retaining parallel multiplicities. An annular vertex compatible with $`\sigma`$ has every base arc disjoint from these cores, except that it may share a whole actual-to-actual annular core. Actual-to-outer and outer-return cores cannot be shared by an annular component. Thus all compatible annular vertices can be treated in one fixed planar complement of the core arrangement. Shared annular cores are restored as parallel packets; their occurrences can be put on an empty side of the fixed finite packet.

Here is a finite nullhomotopy inside this common star. Fix a finite subcomplex $`J\subseteq\mathcal A(\sigma)`$ and a base vertex $`a_*\in\mathcal A(\sigma)`$. Choose narrow PL bands for the finitely many arc cores involved. On a shared core use a common profile. The annular bands can be taken disjoint from the fixed $`\sigma`$ cores, using the packet push-offs just described. Their Thom maps

```math
f_i:B\longrightarrow\mathbb R/\mathbb Z
```

have the same integral cohomology class, actual boundary degrees $`+1,+1,-1,-1`$, and degree zero at the companion boundary. Each is constant on every fixed $`\sigma`$ core and on the companion boundary. Normalise real lifts $`u_i`$ of $`f_i-f_*`$ at a point of the companion boundary. For $`x=\sum_i t_i[a_i]`$ and $`s\in[0,1]`$ use

```math
f_{x,s}=f_*+(1-s)\sum_i t_i u_i\pmod1.
\qquad\text{(6.3)}
```

The actual boundary maps are still monotone maps of the prescribed unit degrees. The map remains constant on every obstacle core and on the companion boundary. At a generic phase, its level therefore avoids every obstacle and has one end on every actual hole and no companion ends. Delete its closed curve components. The remaining level is an oriented perfect matching, hence an annular vertex in $`\mathcal A(\sigma)`$.

Average the ordinary level vertices over the phase intervals. They are mutually disjoint levels of one map. A fixed finite PL template has only finitely many relevant critical values and level patterns. The lifted values are bounded affine functions of the coefficients. When critical phases meet, the corresponding interval has length tending to zero. Thus the phase average is continuous and has finite support on each closed simplex cylinder.

At $`s=0`$, on a true input simplex all weighted levels use whole input annular component classes, with parallel copies restored. They are jointly disjoint from the input simplex and from $`\sigma`$. The straight initial carrier homotopy is therefore in $`\mathcal A(\sigma)`$. At $`s=1`$ all reduced levels are the base matching. This nullhomotopes every finite inclusion in the common star. Compact sphere images lie in finite CW subcomplexes, and Whitehead's theorem proves contractibility. ∎

The same proof with no obstacle gives the asserted contractibility of $`\mathcal A`$. It never deletes part of an actual-bearing component: in this purely annular construction the deleted curves lift to whole closed tori.

### 6.3. Replacing a two-boundary companion by a returning arc

Fix $`\gamma`$ with $`i(\gamma,E)=2`$. Let $`V`$ be a pair of pants, with one gluing boundary and two labelled unused auxiliary boundaries, and put $`W=B\cup_{b_0}V`$. Thus $`W`$ is a sphere with four actual and two auxiliary holes. Replace every copy of $`F_\gamma`$ by an essential returning arc in $`V`$ separating its two auxiliary holes. A packet of such arcs has the same linear order and signed boundary word $`(w,-w^{\rm rev})`$ as the companion packet.

**Lemma 6.2 (replacement dictionary).** This replacement induces bijections of ordinary whole vertex classes and of ordinary actual-bearing component classes. It preserves precisely the simultaneous geometric simplices, and preserves the oriented complementary-region graph of every such finite union, including collapsed common components.

**Proof.** Put a proper matching on $`W`$ in minimum position with the gluing circle. Every cut segment is essential: a boundary-parallel cut return bounds an empty bigon with that circle. Every $`V`$ segment is therefore an essential return separating the two auxiliary holes, and all these segments form a parallel packet. The cut $`B`$ system has exactly the permitted pattern pieces. Conversely, gluing a reduced permitted diagram to the corresponding $`V`$ packet gives a proper matching; its absence of closed components is exactly the incidence condition of Theorem 5.1. Each actual-bearing component is an arc between two distinct opposite-sign actual boundaries. Essential cut pieces exclude any removable gluing-circle bigon.

An ordinary isotopy of minimum-position matchings can preserve the gluing circle. In a comparison rectangle, a returning circle arc gives a forbidden bigon, and a whole gluing circle cannot lie in an empty rectangle. All other circle arcs span the rectangle and straighten. This is the two-dimensional counterpart of Section 2.1.

For the local ordinary quotient in $`V`$, an essential returning arc has one endpoint-free unoriented class, and a packet retains its exact sign word. A loop has zero outer winding. For example, close a cross-arc around one auxiliary boundary and apply the same peripheral-track argument in the free group on the two auxiliary boundary words; a nonzero power of their product cannot normalise the subgroup generated by just one of them. Finite packet permutations are removed by taking a power, as in Lemma 4.1. Thus the two local loop images and the gluing integer in (5.1) are identical for $`Q`$ and $`V`$.

This correspondence is also valid for finite coloured unions. Use reference packets in one product neighbourhood of $`F_\gamma`$ and of the returning arc, with the same ordered boundary tracks. Restriction to a coloured subpacket commutes with replacement. The zero-loop statement makes this independent of straightening paths. Each actual-bearing component has its own actual tether, so the same pattern-loop argument applies to an individual component. This verifies the component-class assertion as well as the whole-vertex assertion; it is not inferred merely from a vertex count.

Finally, cutting $`Q`$ along $`q`$ parallel two-boundary companions gives $`q+1`$ connected regions, in linear order. The two end regions meet one outer annulus each; each intermediate product meets two. Cutting $`V`$ along $`q`$ parallel returns has exactly the corresponding end annuli and intermediate rectangles. The attachment incidences to the cut pattern, and every crossing coorientation, agree. Consequently the full oriented region graphs agree. The argument remains valid when a component carries several colours after common components have been identified. ∎

**Proof of Theorem 1.5.** Lemma 6.2 gives the geometric simplicial isomorphism. For a disjoint pair, collapse common whole component classes. The resulting almost disjoint pair is simplified, as in Part 7, Section 9.3; Banks' all-incompressible minimum-position statement makes its common-wall height width the class minimum. The dictionary preserves these component classes and the whole region graph, so it preserves cyclic edges too. Both cyclic complexes are flag completions, giving the asserted $`X_\gamma`$ isomorphism.

The planar geometric and cyclic matching complexes on $`W`$ are contractible by the matching theorem with marked unused auxiliary holes. Equivalently, one may fill the two auxiliary holes by the retained order-two and order-three cone disks: this is exactly the balanced four-regular-fibre Seifert matching model. Filling does not merge complementary regions or add a cyclic index.

For completeness, the global distance does not shorten by leaving the sector. Banks Proposition 2.4, explicitly included in its Section 10 all-incompressible extension, identifies cyclic class distance with graph distance in $`X`$. The annular subcomplex is isometric in the full $`X`$. Indeed, two annular systems miss $`T_0`$; any comparison product misses it as well, since its whole boundary misses $`T_0`$ and it cannot contain an injected torus. Their minimum width is the planar width in $`B`$, with the one companion boundary unused, and the planar matching metric supplies geodesics entirely in $`\mathcal A`$. Every edge outside a fixed sector must pass through $`\mathcal A`$, by (6.1) and $`X\subseteq Y`$. Replace each excursion outside $`X_\gamma`$ between annular vertices by such an annular geodesic. Hence $`X_\gamma`$ is isometric in $`X`$.

In particular, normalise the two replacement matchings $`a,b`$ on $`W`$ by common orthogeodesic cores and the ordinary bigon/half-bigon criterion. Cut along the whole matching $`b`$. On the connected graph of open regions of $`W\setminus(a\cup b)`$, cross each noncommon $`a`$ segment with its unit coorientation, never cross $`b`$, and put no edge across a common arc. There is one integral potential $`H`$, up to a single constant, and

```math
\delta_M(S,T)=\delta_{X_\gamma}(S,T)=\max H-\min H.
\qquad\text{(6.4)}
```

This is the planar class-distance formula transported by the dictionary. It is a finite computation on normal arc diagrams, not a minimisation over unknown surface representatives. ∎

Let $`\mathcal K_2=Y_{\rm fib}\cup\bigcup_{i(\gamma,E)=2}Y_\gamma`$. Both $`\mathcal K_2`$ and the induced cyclic subcomplex on its vertices are contractible. For the geometric assertion, glue the contractible sectors along $`\mathcal A`$. For the cyclic assertion, the component-wall retraction of Part 7 restricts to these sectors: recombining actual-bearing components of two-boundary packets still gives two-boundary packets in the same sector; recombining capped fibres and annuli stays in the capped-fibre sector. It therefore retracts $`\mathcal K_2`$ onto that induced cyclic subcomplex.

## 7. Contracting the single-companion layer

**Lemma 7.1 (annular neighbour of a single-piece simplex).** Every simplex $`\sigma\subset\mathcal C`$ has an annular common neighbour.

**Proof.** If every vertex is annular, any vertex of $`\sigma`$ suffices. Otherwise all companion pieces in a simultaneous normal form are parallel to the same $`F_\gamma`$, by Section 3. Choose a piece outermost in this whole packet. It belongs to a vertex $`S`$ having exactly one companion component.

On the empty end side of that piece, the outer torus meets the end region in $`k`$ annuli pairing consecutive boundary circles. Replace the chosen $`F_\gamma`$ by small push-offs of these boundary annuli on that side, and push the pattern pieces of $`S`$ consistently to that side. The result is disjoint from the entire original family. Since $`S`$ has no other companion component, every resulting actual-bearing component is a pure pattern annulus. Delete all whole closed components. Each remaining annulus joins distinct actual tori with opposite orientations and is incompressible. All actual boundaries remain. The resulting annular vertex is the required common neighbour. ∎

**Proof of Theorem 1.2 for $`\mathcal C`$.** On the barycentric subdivision, a simplex is a chain

```math
\sigma_0\subset\cdots\subset\sigma_m.
```

Assign it the carrier $`\mathcal A(\sigma_0)`$. Lemmas 6.1 and 7.1 make every carrier nonempty and contractible. On removing the smallest face, the new carrier is a subcomplex of the old one. The usual cellwise carrier extension therefore gives a map

```math
r:|\mathrm{sd}\mathcal C|\longrightarrow|\mathcal A|.
```

The identity map and the composite with the inclusion of $`\mathcal A`$ are both carried by the closed star of $`\sigma_0`$ in $`\mathcal C`$, which is contractible. Thus they are homotopic. On $`\mathcal A`$, the same argument compares $`r`$ with the identity using the carriers $`\mathcal A(\sigma_0)`$. Consequently $`\mathcal A\hookrightarrow\mathcal C`$ is a homotopy equivalence, and $`\mathcal C`$ is contractible. The constructions are cellwise in the weak/CW topology; no local finiteness is assumed. ∎

The capped-fibre sector $`Y_{\rm fib}`$ is also contractible. Its partial matching model in Section 5.3 admits the finite Thom-map proof with the companion maps factoring through the fixed square-knot bundle map. Convex real lifts still give generic levels consisting of pattern arcs and whole one-boundary fibres. A companion-to-companion return closes an entire component made from two one-boundary fibres; deleting all whole closed components leaves only tethered fibres and actual-to-actual annuli. These are incompressible. The finite phase-average and initial whole-component carrier argument is the same as in Lemma 6.1. This proof works for this **sector**, even though cancellation vertices exist elsewhere in $`Y`$.

The preceding carrier proof also applies separately to the single-piece subcomplex in each fixed $`\gamma`$ sector. Form $`\mathcal K`$ using the entire contractible sector when $`i(\gamma,E)=2`$, its contractible single-piece subcomplex when $`i(\gamma,E)\ge4`$, and the entire capped-fibre sector. Different pieces meet exactly in $`\mathcal A`$ and have no mixed nonannular simplex. Collapsing this contractible common subcomplex gives a weak/CW wedge of contractible sector quotients, which is contractible. This proves the asserted contractibility of $`\mathcal K`$ and completes Theorem 1.2.

### 7.1. A filtered version of the Part 7 comparison

Here is the extra step needed to transfer the larger core to $`X`$. The unmodified Part 7 retraction can introduce a recombination with more companion pieces, so its preservation of the vertex set must not be assumed.

Let $`f`$ be an additive function of ordinary whole component classes, extended linearly over $`Y`$. In the notation of Part 7, Section 9.2, a wall $`C`$ is selected for a phase interval of total length $`w_C=\sum_{i:C\subset S_i}t_i`$. Hence the Part 7 phase average $`\mathcal R`$ satisfies

```math
f(\mathcal R(x))=\sum_C f(C)w_C=f(x).
\qquad\text{(7.1)}
```

Its straight geometric homotopy preserves $`f`$ as well. Fix a threshold $`a`$ and let $`Z_a`$ be the full subcomplex on the vertices with $`f(v)\le a`$. On the larger PL sublevel set $`\{x:f(x)\le a\}`$ define

```math
D_a\left(\sum_v t_v[v]\right)=
\frac{\sum_{f(v)\le a}t_v[v]}{\sum_{f(v)\le a}t_v}.
\qquad\text{(7.2)}
```

The denominator is positive: a convex combination of values all strictly greater than $`a`$ cannot be at most $`a`$. The map is continuous on each closed simplex intersected with the sublevel, is face-compatible, stays in that simplex, and is the identity on $`Z_a`$. The PL sublevel is closed, so its subspace topology is weakly generated by these intersections with closed cells. This verifies continuity on the whole sublevel, not only on individual finite supports. The straight segment to $`D_a(x)`$ stays in the PL sublevel. The same statements hold on $`X`$.

For $`x\in|Z_a|`$, compose the Part 7 strong deformation with $`D_a`$. It starts at $`x`$, ends in the induced cyclic subcomplex, and fixes every point of that cyclic subcomplex throughout. The closed-simplex cylinder criterion gives continuity in the weak/CW topology. This proves Theorem 1.7. In particular it applies to $`f=-\chi`$ for every non-split link within the Part 7 conventions; no contractibility conclusion for those general sublevels is inferred.

In a fixed cancellation sector, $`q=-\chi/(2k)`$ is component-additive. Its phase averages therefore preserve $`q`$, including recombinations. The same is true for a function defined separately on the sectors, with value zero on their common annular part, provided its value is preserved in each sector. To transfer $`\mathcal C`$, work in the union of the cancellation sectors and set $`f=q`$ there, with threshold one. To transfer $`\mathcal K`$, set $`f=q`$ on the sectors with $`k\ge2`$ and $`f=0`$ on the fibre sector and the sectors with $`k=1`$, again with threshold one. The Part 7 construction stays in these sectors under whole-component recombination. Formula (7.2) consequently supplies a strong deformation retraction from each geometric core onto its induced cyclic core. Both induced cyclic cores are contractible, completing all assertions of Theorem 1.2.

## 8. A cyclic height obstruction and an exact family

### 8.1. Companion height

For a signed cancellation packet in $`Q`$, give the complementary regions integral heights, changing by the surface coorientation on crossing a piece. This is possible because the spanning class vanishes on $`Q`$. With the packet order and signs of (4.1), put

```math
H_0=0,\qquad H_j=\sum_{i=0}^{j-1}w_i,
\qquad
\kappa_Q(S)=\max_jH_j-\min_jH_j.
\qquad\text{(8.1)}
```

The range is independent of the additive choice and of reversal of the reference order. Section 2.1 makes it an ordinary invariant of the efficiently cut surface.

**Lemma 8.1.** For every cancellation vertex $`S`$ and every $`a\in\mathcal A^{(0)}`$,

```math
\delta(S,a)\ge\kappa_Q(S).
\qquad\text{(8.2)}
```

**Proof.** Choose an essential normal form of $`S`$ and a pure pattern representative of $`a`$. Simplify their intersections using the incompressible product-region comparison. Every comparison product is disjoint from $`T_0`$: its annular $`T_0`$ intersections would all return to the $`S`$ face because the $`a`$ face misses $`T_0`$, and an innermost return would give a boundary-parallel cut annulus of $`S`$. A whole $`T_0`$ in the product is again excluded by its injected torus group. Thus simplification leaves the companion packet unchanged.

Banks Proposition 4.10, with its explicit all-incompressible extension in Section 10, computes the ordinary minimum width in this simplified position. One complete open $`a`$ block contains a lift of the entire $`Q`$, since $`a`$ misses $`Q`$. The open $`S`$ blocks meeting its complementary packet regions have precisely the relative height differences (8.1). The width is therefore at least their range. This uses one common global block index, not separate choices for different companion pieces. ∎

**Lemma 8.2.** If one vertex is connected and two distinct whole spanning representatives are geometrically disjoint, their cyclic class distance is one.

**Proof.** Cut along the other whole spanning system. Its complement is connected. The connected first surface lies inside this cut block and separates it: every loop in the block has zero intersection with its homologous whole spanning class. There are two complementary regions, with consecutive heights. Hence the open-block width is one. ∎

We also need a small shared-component observation. Suppose $`S=C\sqcup A`$ and $`R=D\sqcup A`$ have disjoint representatives, where $`C`$ is connected, $`D`$ uses precisely the same oriented actual boundary set, and $`A`$ is a common system of whole components. The subsystem $`D`$ need not be connected. The two distinct vertices can be placed at cyclic distance one. In the whole cut block of $`R`$, the connected surface $`C`$ separates the block into heights zero and one, since its relative class equals the sum of the classes of $`D`$. Both boundary copies of each common component lie on the same side: a meridian at one of its actual boundaries joins them without meeting $`C`$. Put a parallel copy of that common component next to the appropriate boundary face so that its additional height stays within zero and one. Do this in disjoint product collars. This is a geometric choice of push-offs, not independent deck normalisation.

The separation assertion uses equality of the relevant relative classes. The dual class of an actual-bearing subsystem evaluates to one on the positive meridians of its actual boundary set and to zero on all other actual meridians. These meridians are a basis for the first homology of a link exterior. Thus a connected component and a replacement subsystem with precisely the same oriented actual boundary set have the same relative class.

### 8.2. Compression repair gives a cyclic descent, but not a parent map

**Lemma 8.3 (geometric descent relative to a simplex).** Let $`\sigma`$ be a finite geometric simplex with nonannular vertices in $`Y_\gamma`$. There are $`S\in\sigma`$ and a vertex $`R\in Y_\gamma`$, possibly annular, geometrically compatible with all of $`\sigma`$, such that $`q(R)\lt q(S)`$.

**Proof.** Put the whole family in simultaneous essential normal form. Choose an end piece of its entire companion packet, and let $`S`$ be its vertex. Resolve this one piece on the empty end side by the $`k`$ outer boundary annuli. Push the remaining pieces of $`S`$ to the consistent side and use sufficiently small collars. This gives an oriented raw spanning system $`R_0`$, disjoint from the whole family. It need not be incompressible.

First discard its whole closed components. Its pieces are retained companions and annuli, so those closed components have nonpositive Euler characteristic. Now compress the actual-bearing output components until they are incompressible, discarding every closed component subsequently produced. Every compression disk can be chosen disjoint from the fixed incompressible family: put it transverse to that family and remove its intersection circles by innermost disk exchange. An essential innermost circle would compress an original family component, which is impossible. This finite process preserves disjointness from $`\sigma`$ and all actual boundaries.

No actual disk can occur, since its longitudinal boundary is nontrivial in the exterior. An essential compression of an actual-bearing component cannot split off a sphere. Thus the retained Euler characteristic never decreases during these compressions and closed-component deletions. The initial end replacement increased it by $`2k`$, giving

```math
\chi(R)\ge\chi(S)+2k.
\qquad\text{(8.7)}
```

The final system is a reduced incompressible spanning vertex. Normalise it together with $`\sigma`$. The sector decomposition makes it annular or a cancellation vertex with the same $`\gamma`$; it cannot switch to the fibre mode while staying disjoint from $`S`$. Since $`\chi=-2kq`$ in this sector, (8.7) proves $`q(R)\le q(S)-1`$. ∎

**Lemma 8.4 (two-component recombination).** Suppose $`S,R\in Y_\gamma`$ are geometrically compatible and $`q(R)\lt q(S)`$. Then there is a cyclic neighbour $`T`$ of $`S`$, made from whole components of $`S`$ and $`R`$, with $`q(T)\lt q(S)`$. It remains geometrically compatible with every family compatible with the union of these representatives.

**Proof.** If one system is connected, Lemma 8.2 gives the edge to $`R`$. Otherwise each has two balanced actual-bearing components. If their actual-boundary pairings differ, their cyclic distance is one. To verify this directly, cut along $`R`$. Its connected whole cut block has only two $`S`$ walls. A width-two height graph would have to be a path with the two walls at distinct consecutive levels. Both boundary faces of one connected $`R`$ component must have the same ordered pair of height values at each of its actual ends, by the oriented meridian collars. Such a component cannot use an actual end at each of those two distinct walls. Different pairings require exactly that, so width two is impossible. The width is at most two and is nonzero for distinct classes; hence it is one.

If the pairings agree, write $`S=S_1\sqcup S_2`$ and $`R=R_1\sqcup R_2`$, with the same actual pair at corresponding indices. Both mixed systems

```math
U=S_1\sqcup R_2,\qquad V=R_1\sqcup S_2
```

are valid vertices, geometrically compatible with the whole union. The shared-component observation makes each distinct mixed system a cyclic neighbour of $`S`$. Companion count is additive, so

```math
q(U)+q(V)=q(S)+q(R)\lt 2q(S).
```

At least one mixed system has smaller count than $`S`$; choose it as $`T`$. It is automatically distinct from $`S`$. ∎

Apply Lemmas 8.3 and 8.4 to a singleton to obtain the strictly decreasing cyclic step in Theorem 1.6. Iterate the nonnegative integer $`q`$ to reach $`\mathcal A`$ in at most $`q(S)`$ steps. Apply them to a whole simplex for the relative assertion. Lemma 8.1 gives the other bound in (1.4), and a coherent word has height range $`q`$.

These lemmas use maximal compression only for existence. In particular, the relative assertion does not give a vertex cyclically adjacent to **every** member of the original simplex, much less one dominating all the mutually intersecting neighbours of $`S`$. No ordinary compression-choice theorem is hidden in the statement.

### 8.3. The explicit connected family

Choose $`\gamma`$ with $`i(\gamma,E)=4`$, and take $`q`$ coherently oriented parallel copies. Number the $`4q`$ outer trace points in four blocks, and write the four boundary points of copy $`j`$ as

```math
A_j=j,\quad B_j=2q-1-j,\quad
C_j=2q+j,\quad D_j=4q-1-j,
\qquad 0\le j\lt q.
\qquad\text{(8.3)}
```

The signs are $`(+^q,-^q,+^q,-^q)`$. Use four actual tethers at

```math
A_{q-1},\quad B_0,\quad C_0,\quad D_{q-1},
\qquad\text{(8.4)}
```

with signs $`+,-,+,-`$. The returns are

```math
A_jB_{j+1},\qquad C_{j+1}D_j,
\qquad 0\le j\lt q-1.
\qquad\text{(8.5)}
```

They are two nested stacks of disjoint chords. Each chord separates one actual tether from the other three, so it is essential. The companion incidence graph is a chain of $`q`$ vertices with two edges between successive vertices. Thus the resulting surface $`S_q`$ is connected and incompressible, and

```math
\chi(S_q)=-4q,\qquad g(S_q)=2q-1.
\qquad\text{(8.6)}
```

In leaf reflection coordinates these packets may be taken with $`c_+=2q-1`$ and $`c_-=4q-1`$. Formula (2.8) gives exactly $`q`$ four-boundary pieces.

Resolve the end copy $`0`$ using the annuli $`D_0A_0`$ and $`B_0C_0`$. For $`q>1`$, the latter joins the two indicated actual boundaries into a fixed annular component. The former splices (8.5) to a return $`B_1C_1`$ enclosing those same two actual holes. The remaining companion copies are $`1,\ldots,q-1`$. The new return is essential because the two actual holes on its enclosed side are still present, even though they now belong to the separate annular component.

Continue from that end. At each step the corresponding $`B_jC_j`$ return and end cap close a whole torus, which is deleted; the next $`B_{j+1}C_{j+1}`$ return encloses the same pair of actual holes. Every retained return remains essential. At the final step the remaining two actual boundaries are joined into a second annulus. No actual boundary is deleted. There are exactly $`q`$ steps.

The first edge has the connected representative $`S_q`$ on one side. Subsequent steps share the fixed annular component and change a single connected component, so the shared-component observation applies. For $`q=1`$, the initial connected surface resolves directly to the two annuli. Thus all $`q`$ steps are edges of $`X`$.

The packet is coherent, so $`\kappa_Q(S_q)=q`$. Lemma 8.1 bounds its distance from every annular vertex below by $`q`$, while the displayed $`q`$-edge path reaches an annular vertex. This proves (1.3). Lemma 8.2 gives the asserted lack of annular geometric neighbours for $`q\ge2`$, and completes Theorem 1.3.

The resolution just used is a special explicitly controlled family. It is not asserted to work for arbitrary signed packets.

### 8.4. Coherent end parents and an ordered contraction

Fix $`\gamma`$ and a reference end of its parallel packet. In this subsection all nonempty companion packets have the same coherent coorientation. Put $`p(a)=a`$ for $`a\in\mathcal A`$.

**Lemma 8.5 (coherent end parent).** End resolution at the chosen end of a coherent vertex, followed only by deletion of whole closed components, is already incompressible. It retains exactly $`q-1`$ companion pieces, still coherent, and defines an ordinary vertex $`p(S)`$ independent of the choices of collars and representatives.

**Proof.** Perform the end resolution on the component $`C`$ of $`S`$ containing that end piece; leave the other components unchanged. If necessary, compress the resulting actual-bearing subsystem of $`C`$, avoiding $`S`$, as in Lemma 8.3. The final system $`R`$ is in the same sector or is annular, and $`\chi(R)\ge\chi(S)+2k`$.

The shared-component observation in Section 8.1 gives $`\delta(S,R)=1`$: the one changed input component $`C`$ is connected, even if its eventual replacement splits. Coherence and Theorem 1.6 give

```math
q(S)=d(S,\mathcal A)\le1+d(R,\mathcal A)\le1+q(R).
```

Therefore $`q(R)=q(S)-1`$. An essential compression would have increased the retained Euler characteristic by at least two beyond the initial $`2k`$ increase. Deleting a closed component containing a companion piece would also have increased it further. Since the final Euler characteristic is exactly $`-2kq(R)`$, either event would force $`q(R)\le q(S)-2`$, a contradiction. Thus no essential compression was needed and no companion piece was lost to a discarded closed component. The only discarded components are tori.

For ordinary invariance, use the $`T_0`$-preserving comparison and the zero-loop packet identification. They preserve the chosen end and its consecutive boundary annuli. The replacement is uniquely specified in their collars; tangential longitudinal motion changes no embedded annulus. A whole closed component is deleted by its actual connectivity, not by an arbitrary choice. Hence the ordinary parent is well-defined. ∎

This establishes, in particular, the coherent peeling property that the preliminary finite experiments were testing. Its proof is the distance-and-Euler argument above, not an inference from those experiments.

**Coherent contraction.** Section 10 constructs one ordinary parent and one face-compatible multistep prism for all signed packets. Lemma 8.5 shows that its restriction to a coherent packet is just the unrepaired end resolution and preserves that coorientation. The Part 7 retraction also preserves this fixed-coorientation class under whole-component recombination. Consequently the contraction and its bounded-count version in Section 10.4 restrict to the positive or the negative coherent subcomplex. The filtered comparison of Section 7.1 gives the corresponding bounded geometric statements. This proves the fixed-coorientation assertions of Theorem 1.8 without a separate first-round construction.

For the final four-parallel assertion, let $`S`$ and $`T`$ have opposite coherent signs in the same sector. If they are geometrically disjoint, collapse common whole components and compute their difference potential. Along $`Q`$, every noncommon wall contributes with the same sign to $`S-T`$. Thus

```math
\delta(S,T)\ge q(S)+q(T).
\qquad\text{(8.8)}
```

On the other hand a disjoint pair has width at most the number of components of either member: the dual graph inside a whole cut block has one edge for each component of the other surface. Cancellation vertices of $`L_4`$ have at most two components. Consequently opposite coherent vertices have no cyclic edge, and their only possible geometric edges have $`q(S)=q(T)=1`$.

It follows that the full geometric coherent subcomplex in this sector is the union of the positive coherent subcomplex, the negative coherent subcomplex, and the already contracted single-piece subcomplex. The positive and negative pieces meet in $`\mathcal A`$; each intersects the single-piece subcomplex in its contractible $`q\le1`$ part. Successive homotopy pushouts show that the union is contractible. The cyclic coherent subcomplex is simply the union of its positive and negative parts along the annular cyclic complex, so it is contractible too.

Finally glue these coherent sectors for $`k\ge2`$ to the complete two-boundary sectors and the complete fibre sector. Different sectors meet only in the annular complex, in either convention. This proves the enlarged-core assertion of Theorem 1.8. It is still a proper core. The remaining mixed-sign vertices are handled by the full sector argument in Section 10.

[Overview](../README.md) · [Previous page](part9.md) · [Next page](part9-3.md)
