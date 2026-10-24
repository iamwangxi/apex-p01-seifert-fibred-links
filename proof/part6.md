# Part 6. The two oppositely oriented zero-framed parallels of a torus knot

[Overview](../README.md) · Part 6, page 1 of 1

This part treats the full cyclic incompressible spanning-surface complex of the simplest link whose exterior has a JSJ piece without actual link boundary. Every genus is included. The theorem below does not use a norm-minimising projection, a deletion-of-tori certificate, or a contractibility theorem.

## 1. Statement and conventions

Let $`C=T(p,q)`$, where $`p,q\ge2`$ are coprime, and let $`V=N(C)`$ have the zero framing. Take two distinct parallel cores, with orientations $`+C,-C`$, and call the resulting oriented link $`L`$. Put

```math
M=E(L)=P\cup_T Q,\qquad
P=S^1_\lambda\times B,\qquad Q=E(C),\qquad T=\partial V,
```

where $`B`$ is a pair of pants. Its labelled inner boundaries are $`b_+,b_-`$, and its outer boundary is $`b_0`$. On $`T`$, $`\lambda`$ is the preferred companion longitude, and the transverse coordinate is its meridian $`\mu`$. On the actual link tori $`T_+,T_-`$, the prescribed boundary slopes are $`+\lambda,-\lambda`$. The pairwise linking number is zero.

A spanning surface is oriented, properly embedded, has one prescribed boundary curve on each labelled actual link torus, and has no closed components. It may be disconnected. Incompressibility is componentwise. Boundary curves may move in ambient isotopies starting at the identity.

Write $`\phi:\pi_1(M)\to\mathbb Z`$ for total oriented linking number. Thus on $`P`$ it is zero on $`\lambda`$, and has opposite unit values on the two inner meridians; on $`Q`$ it is identically zero, since the two parallels have opposite orientations. The cover and distance for $`M`$ are associated with this $`\phi`$, not the usual nonzero knot-fibration class on $`Q`$.

For surfaces $`S,F`$, let $`U_j=\tau^jU_0`$ be the lifts of the whole open complement $`M\setminus S`$, and let $`W`$ be one lift of the whole open complement $`M\setminus F`$. Set

```math
D(S,F)=\max\{j:W\cap U_j\ne\varnothing\}
-\min\{j:W\cap U_j\ne\varnothing\},\qquad
\delta([S],[F])=\min D(S',F').
```

The minimum ranges over representatives of the two isotopy classes. The complex $`X(L)=IS_{\mathrm{cyc}}(L)`$ is the flag complex with an edge between distinct classes at cyclic distance one.

Choose a seam $`\alpha\subset B`$ joining $`b_+`$ to $`b_-`$, and put $`A=S^1_\lambda\times\alpha`$. Choose disjoint seams $`\beta_+,\beta_-`$ joining $`b_+,b_-`$, respectively, to $`b_0`$. Attach a positive and a negative fibre of $`Q`$ along their outer ends; the resulting spanning system is denoted $`F`$. Let $`a=[A]`$, $`v=[F]`$, and

```math
g=\frac{(p-1)(q-1)}2.
```

**Theorem 1.1.** The full vertex set of $`X(L)`$ is exactly $`\{a,v\}`$. Minimum intersection with the fixed $`T`$, and the topology, are:

| Vertex | Minimum $`T`$-circles | Pattern part | Companion part | Components | Thurston complexity |
|---|---:|---|---|---:|---:|
| $`a`$ | 0 | one inner–inner vertical annulus | empty | 1, an annulus | 0 |
| $`v`$ | 2, of slopes $`+\lambda,-\lambda`$ | two inner–outer vertical annuli | two oppositely oriented fibres | 2, each of genus $`g`$ with one actual boundary | $`2(2g-1)>0`$ |

There is no residual gluing or torus-twisting parameter. Moreover,

```math
\delta(a,v)=1.
```

Consequently $`X(L)`$ is exactly one closed 1-simplex, with $`a`$ a cone vertex, and is contractible.

Let $`\mathcal C`$ be the class of links obtained by finitely many connected sums along specified components from factors each of which is a knot, a link all of whose incompressible spanning surfaces are connected, or a link all of whose incompressible spanning surfaces are norm-minimising.

**Theorem 1.2.** The link is non-split, its exterior is not Seifert fibred, and $`L\notin\mathcal C`$. In particular it has both disconnected and non-norm-minimising incompressible vertices.

For the right-handed trefoil, $`g=1`$ and the non-minimising vertex has complexity $`2`$. Mirroring gives the same assertions for negative torus knots. The argument applies to every nontrivial torus knot, not only $`T(2,3)`$.

## 2. Sources and exactly what is imported

Hatcher's notes (H) supply cutting and irreducibility, essential surfaces, the vertical/horizontal classification and the horizontal product complement: Lemma 1.11 (printed p. 20), Proposition 1.12 (printed pp. 20–22), the horizontal degree and Euler characteristic count (printed p. 22), the horizontal product complement (printed p. 23), and the circle-bundle construction for nonorientable bases (printed p. 32). Przytycki–Schultens' journal edition (PS J), §§2–3, printed pp. 1492–1495, supplies the whole open-complement definition and the disconnected-surface warning. Banks 2011, Proposition 2.2, fixes the product-region and companion-torus conventions; its Whitehead-double construction is not an input. Banks, arXiv:1109.0965v1 (B), supplies the product-region comparison (PDF pp. 5 and 15). Full bibliographic data are in the [bibliography](../sources/bibliography.md).

We use the Loop Theorem, isotopy extension, the amalgam normal-form theorem, the elementary disk-isotopy theorem in a ball, and elementary covering-space theory. We do not use PS Proposition 3.2 outside its stated minimum-norm domain: the upper and lower distance bounds are proved directly in §6. No PS §4–§8 projection result, competition Theorem A or D, or Banks product homeomorphism is needed for Theorem 1.1.

## 3. The companion-side theorem, including fibre uniqueness

Here “longitudinal essential component” has **nonempty boundary**, all of whose circles are preferred longitudes. Every companion component arising in this problem satisfies that condition. A vacuous assertion permitting a closed boundary-parallel torus would be false; that is not the cut-surface problem.

### 3.1. Seifert data and the boundary orientation

The standard circle action
```math
t\cdot(z_1,z_2)=(e^{ipt}z_1,e^{iqt}z_2)
```
on $`S^3`$ gives $`Q`$ a Seifert structure with base a disk and exceptional orders $`p,q`$. The deleted $`C`$ is a regular orbit. The regular fibre slope on $`\partial Q`$ is
```math
h=\lambda+pq\,\mu.
\qquad\text{(3.1)}
```
One way to verify the coefficient is to split along the standard Heegaard torus: van Kampen gives $`\langle x,y\mid x^p=y^q\rangle`$, with regular fibre $`h=x^p=y^q`$. Abelianisation sends $`x,y`$ to $`q\mu,p\mu`$, respectively. The peripheral fibre has longitudinal degree one, as a parallel of the deleted regular orbit, and has homology $`pq\,\mu`$. This proves (3.1).

**Lemma 3.1.** A connected oriented essential component $`S\subset Q`$ with nonempty longitudinal boundary has one boundary circle, is horizontal up to isotopy, represents the positive or negative generator of $`H_2(Q,\partial Q)`$, and is a spanning fibre.

**Proof.** H Proposition 1.12 applies. A vertical component with boundary is an annulus with fibre-slope boundary (H, printed p. 22); by (3.1) that slope is not $`\lambda`$. Hence $`S`$ is horizontal.

Orient the regular-fibre vector field $`Z`$. On a connected horizontal oriented surface the sign of its transverse intersection with $`Z`$ is constant. Equivalently, projection to the oriented base is either everywhere orientation-preserving or everywhere orientation-reversing, away from the cone points. Its boundary circles cover the one base-boundary circle with the same sign. Since all are longitudinal, their induced orientations are all the same longitude orientation. If there are $`b\ge1`$, then
```math
\partial[S]=\pm b[\lambda],\qquad [S]=\pm b\eta,
\qquad\text{(3.2)}
```
where $`\eta`$ is the Seifert relative generator. Indeed $`H_2(Q)=0`$, and the relative boundary map is an isomorphism onto the longitude kernel of $`H_1(\partial Q)\to H_1(Q)`$.

The class in (3.2) is nonzero. A separating connected oriented proper surface is the relative boundary of one side, so has zero relative class. Thus $`S`$ is nonseparating. Join the two ends of a small transverse crossing arc by a path in its connected cut complement. The resulting closed curve has algebraic intersection one with $`S`$. Therefore $`[S]`$ is primitive, and (3.2) forces $`b=1`$.

H's horizontal-complement argument now applies in its nonseparating case: $`Q\mathbin{\|}S=S\times I`$, so $`S`$ is a fibre (H, printed p. 23). Its fibration class is $`\pm\mathrm{PD}(\eta)`$, the ordinary knot class, not the zero restriction of the global $`\phi`$. ∎

The degree of the horizontal cover is $`pq`$: intersection with a regular fibre is $`pq`$, and all intersections have one sign. H's formula gives
```math
\chi(S)=pq\bigl(1-(1-1/p)-(1-1/q)\bigr)=p+q-pq=1-2g.
\qquad\text{(3.3)}
```
This argument covers every genus; it does not assume that $`S`$ was genus-minimising.

Existence is also accounted for. Choose an ordinary minimum-genus Seifert surface for $`C`$. It is incompressible, since a genuine compression, retaining the boundary-bearing descendant, would lower its genus. H Lemma 1.11 makes it boundary-incompressible, as its one boundary excludes the annulus exception. Lemma 3.1 therefore produces a horizontal spanning fibre $`R`$. The calculation (3.3) computes its genus. No prior uniqueness or analytic theorem is being used for this choice.

### 3.2. Uniqueness of the unmarked fibre

**Lemma 3.2.** Any two positive longitudinal horizontal fibres of $`Q`$ are ambient isotopic, with boundary allowed to move.

**Proof.** Let $`f_0,f_1:Q\to\mathbb R/\mathbb Z`$ be their bundle maps, each chosen to have the specified surface as its zero fibre. H's interval-bundle construction has interval directions along the original Seifert orbits and all its bundle fibres are horizontal (H, printed p. 23). Accordingly the maps can be chosen smooth with
```math
df_0(Z)>0,\qquad df_1(Z)>0.
```
To see the choice directly, parametrise the orbit intervals between consecutive intersections with the horizontal section monotonically, smooth in collars of the section, and glue the two ends. This produces a bundle map whose levels remain transverse to $`Z`$, including at the exceptional orbits.

The maps represent the same integral class, namely the primitive knot class in Lemma 3.1. Hence $`f_1-f_0`$ lifts to a smooth real function $`u:Q\to\mathbb R`$. Put
```math
f_t=f_0+t u\pmod{\mathbb Z}.
```
Then
```math
df_t(Z)=(1-t)df_0(Z)+t\,df_1(Z)>0.
```
The same assertion holds on the boundary, since $`Z`$ is tangent to it. The time-dependent vector field
```math
Y_t=-\frac{u}{df_t(Z)}\,Z
```
is smooth, tangent to $`\partial Q`$, and defined for all $`t`$ on the compact $`Q`$. Its flow $`\Psi_t`$ satisfies $`f_t\circ\Psi_t=f_0`$, and therefore carries $`f_0^{-1}(0)`$ to $`f_t^{-1}(0)`$. At $`t=1`$ it gives the required ambient isotopy. Negative orientation is handled by reversing the surface orientation. ∎

### 3.3. Two fibres must be normalised jointly

We need a fact about actual disjoint systems, rather than separate component classes.

**Lemma 3.3 (one-boundary surface in a product).** Let $`R`$ be a connected orientable surface with one boundary circle. An incompressible connected proper surface $`S\subset R\times I`$, with exactly one boundary circle in $`\partial R\times(0,1)`$ isotopic there to its core, is isotopic to $`R\times\{t\}`$, keeping the horizontal end faces fixed.

**Proof.** First straighten its boundary to $`\partial R\times\{t\}`$. Choose disjoint proper arcs cutting $`R`$ into a disk, and their product disks. Minimise total intersection with these disks relative to the boundary. A circle innermost on a product disk bounds a disk on $`S`$, by incompressibility. The intervening sphere bounds a ball in the product. Replacing the surface disk by a nearby copy of the innermost product-disk patch removes its intersections and creates none on the other disjoint product disks. No component of $`S`$ can be trapped in the ball, since $`S`$ has boundary. Thus there are no circles.

Each product disk has exactly two boundary intersections and hence one spanning trace arc. Straighten these trace arcs relative to their endpoints. After cutting along all product disks the ambient manifold is a ball. Each piece of $`S`$ is incompressible there: cutting along proper surface arcs preserves injection of each piece group into the original surface group. Consequently the pieces are disks. Their boundary pattern is the boundary of the one disk obtained by cutting $`R`$ along the chosen arcs: the straightened boundary and the one trace on each product disk specify this pattern completely. There is therefore one disk. The disk-isotopy theorem in a ball, fixing its boundary (H, printed p. 20), makes it the standard horizontal disk. Regluing gives the claimed isotopy. Every move is relative to the horizontal end faces. ∎

**Corollary 3.4.** Any disjoint system of two oppositely oriented longitudinal essential components in $`Q`$ can be isotoped jointly to $`R_{\theta_+}\sqcup(-R_{\theta_-})`$, with $`\theta_+\ne\theta_-`$, for one fixed knot fibration $`f`$. The labels and orientations are retained.

**Proof.** Normalise the positive component by Lemmas 3.1–3.2 and extend its isotopy ambiently, carrying the other component along. The remaining component lies in the cut product $`R\times I`$, with one core boundary on its vertical annulus. Apply Lemma 3.3 there, fixing the first component's two cut faces. ∎

A simultaneous movement of both phases through one full circuit is a loop of the two unparameterised fibre surfaces. Its two boundary circles make one common meridional circuit on $`T`$. It is valid even when the monodromy on parameterised fibres is nontrivial.

## 4. The uniform all-genus cut classification

### 4.1. Essential minimum intersection

The product $`P`$ is irreducible and all three of its boundary tori inject: their groups are $`\langle\lambda,c_i\rangle`$ in $`\mathbb Z\times\pi_1(B)`$. The nontrivial knot exterior $`Q`$ is irreducible and its boundary torus is incompressible. Amalgam normal form and the sphere-cutting argument (H, statement (4), printed pp. 14–15) show that $`M`$ is irreducible and that $`T,T_+,T_-`$ are incompressible. In particular $`L`$ is non-split.

No spanning component is a disk, since its boundary longitude is nontrivial in its injected actual boundary-torus group. H Lemma 1.11 makes every incompressible spanning component boundary-incompressible: its boundary-parallel-annulus alternative would use one actual torus twice.

For any full ambient-isotopy class, choose a transverse representative with the minimum number of $`T`$-circles. Every circle is essential on both surfaces. A trivial circle on one is trivial on the other by group injection; the innermost disk and irreducibility remove it. Whole surface components cannot obstruct the ball move because they all have boundary on $`\partial M`$.

Each cut piece is incompressible in its own piece of $`M`$, since cutting along essential surface circles injects the cut-piece group into the original surface group, which injects into $`M`$. No cut piece is a disk or a closed surface. A closed cut piece would already be a closed original component, and a disk would contradict essential intersection or a nontrivial actual longitude.

There is no boundary-parallel annular cut piece. Such an annulus can only have both ends on $`T`$. In its annular parallelism solid torus, every other cut piece has group injecting into the cyclic solid-torus group and hence, as an orientable nondisk surface with boundary, is an annulus. Its boundary has degree one in that solid torus. A meridian-disk cut straightens a finite such annulus system to products of disk arcs: each annulus has one trace on the meridian disk, and the cut pieces are disks in a ball. There is an innermost annulus with an empty parallelism to a subannulus of $`T`$. Push it across this empty product, removing two $`T`$-circles, a contradiction. Thus all cut pieces are boundary-incompressible by H Lemma 1.11.

This supplies H Proposition 1.12's full essentiality hypothesis in both pieces; it is not an application to merely incompressible surfaces.

### 4.2. The two cases

Every pattern piece meeting an actual torus has fibre-slope boundary and hence cannot be horizontal. It is a verticalisable annulus.

If the two actual boundaries are paired by an inner–inner annulus, that annulus is already a complete component of the spanning surface. Any remaining piece would assemble to components without actual boundary. Such components are forbidden. This is the zero-intersection case.

Otherwise both actual boundaries reach $`T`$ through inner–outer annuli. A reaching annulus has slope $`\lambda`$ on $`T`$. Disjoint essential circles on a torus all have the same unoriented slope, so every $`T`$-circle is longitudinal. This excludes horizontal pattern pieces even when they have only outer boundary; all pattern pieces are annuli. Lemma 3.1 makes every companion piece a single-boundary fibre.

An outer–outer pattern annulus would join the sole boundaries of two companion fibres and form a closed component of the assembled surface. It cannot reach any actual boundary, because those companion pieces have no other boundary. It is forbidden. Therefore there are precisely two inner–outer annuli and precisely two companion fibres. The induced boundary orientations give one positive and one negative fibre.

This proves that every minimum representative is of exactly one of the two types in Theorem 1.1, independently of genus.

The pattern annuli can be straightened simultaneously, relative to their already straight fibre boundary. Here is the needed relative statement. Choose a system of disjoint base arcs cutting $`B`$ to a disk, with endpoints avoiding all the finite annulus endpoints. Its product annuli meet the pattern system only in circles. Remove trivial circles by disk/ball moves minimising the total count. The remaining circles are essential cores on both annuli and can be straightened to fibres on the cutting faces. Cutting the product along them gives a solid torus and a finite annulus system with primitive longitudinal boundary. A meridian disk cuts each annulus into a disk; relative disk isotopies in the resulting ball straighten the whole system. The traces agree on the cut faces, so the isotopies glue. This is a simultaneous relative isotopy, not a choice of incompatible separate isotopies.

## 5. Actual vertices and elimination of all gluing parameters

### 5.1. The elementary pair-of-pants data

With endpoints allowed to move on their labelled boundary circles:

1. a seam from $`b_+`$ to $`b_-`$ has a unique isotopy class;
2. a disjoint pair of seams from $`b_+,b_-`$ to $`b_0`$ has a unique joint isotopy class.

For an elementary verification, complete either configuration to the usual three seams. They cut the pair of pants into two hexagons. Label-compatible maps of the hexagons glue to a label-preserving homeomorphism carrying one system to the other. Its possible seam-gluing discrepancies are twists in the three boundary collars. With boundary circles preserved setwise, each such twist is isotopic to the identity by rotating the corresponding boundary circle. The disk Alexander isotopy handles the hexagon interiors. Equivalently this is the ordinary seam/bigon proof for the pair of pants. No boundary labels are permuted.

For the two outer endpoints their cyclic order gives no extra choice: with two differently labelled points there is only one cyclic order, up to its starting point. During an isotopy they remain distinct.

### 5.2. Compatible paths, rather than independent local isotopies

The zero-intersection case is the unique vertex $`a`$, by simultaneous pattern straightening and the unique inner–inner seam.

In the nonzero case first apply Corollary 3.4 in $`Q`$. Its boundary motion on $`T`$ extends across a collar in $`P`$, so this is an isotopy of the assembled system preserving $`T`$ setwise. Fix the boundary coordinates once so the reference fibration restricts to the meridional projection: its fibres on $`T`$ are the straight preferred longitudes, and a meridian has phase degree one. To obtain these coordinates, choose a section of the boundary circle bundle over its phase circle and parametrise its longitude fibres. The section has homology $`\mu+k\lambda`$; changing it by $`-k`$ longitude turns makes the resulting torus chart induce the identity on homology. The chart is therefore isotopic to the identity on the torus. Extend that isotopy in a collar into $`P`$. The two fibres now have phases $`\theta_+,\theta_-`$. Straighten the two pattern annuli simultaneously relative to these fixed outer circles; their inner boundary curves may be straightened on the actual labelled tori.

They are now products of a pair of pants seam system. Choose an isotopy of that whole seam system to the fixed reference $`\beta_+,\beta_-`$. Write its outer endpoint phases as $`\theta_+(t),\theta_-(t)`$. These are an actual path of two distinct points on the outer meridian circle, not independently chosen integer lifts. At every time move the companion pair to
```math
R_{\theta_+(t)}\sqcup(-R_{\theta_-(t)}).
```
The piece boundary motions agree exactly throughout. Extend the common boundary motion in collars and apply relative isotopy extension in the two pieces. The compatible paths therefore glue to an ambient isotopy of the whole spanning system.

This proves that **every** nonzero-case assembly, including any relative winding, is isotopic to the one $`F`$. A full common outer winding is absorbed by the fibre loop in Corollary 3.4. Individual inner windings disappear because the actual boundary curves are allowed to move. A longitudinal reparametrisation contributes no parameter: the vertical annuli already contain the entire longitude circle, and the surfaces are unparameterised. There is no additional circle-gluing map datum for collared embedded surfaces with the same actual boundary circles.

Thus this is a complete ordinary-isotopy classification, not merely separate normalisation of individual surfaces. It needs no unproved extension of Banks's annular-decomposition comparison to tori. The compatible isotopies are explicitly supplied for this particular two-case model.

### 5.3. Existence, incompressibility and exact minimum

The annulus $`A`$ is incompressible: its core is the injected nontrivial $`\lambda`$ in $`P`$ and hence in $`M`$.

The two fibres used for $`F`$ are incompressible in $`Q`$; this follows also from their cut product and its mapping-torus group. Attaching an inner–outer annulus is just adding a boundary collar to each fibre. For completeness, the new component group injects: the surface group is unchanged by its annular collar, it injects into $`Q`$, and the amalgam normal form injects $`Q`$ into $`M`$. It therefore is incompressible. The assembled surfaces have exactly the prescribed orientations and no closed components.

The two classes are different because their numbers of components differ. Their Euler characteristics and complexities are precisely those in Theorem 1.1, by (3.3). Since $`A`$ has norm zero, $`F`$ is not norm-minimising.

The minimum intersection of $`v`$ is exactly two. A zero-intersection incompressible representative would be the one-annulus case of §4, whereas $`F`$ has two components. The explicit construction meets $`T`$ twice and attains the lower bound. The minimum for $`a`$ is zero.

## 6. Whole-complement cyclic distance, with both bounds

### 6.1. A complete block and its two chambers

Arrange $`\alpha,\beta_+,\beta_-`$ as the three pair-of-pants seams, with distinct boundary endpoints. Their interiors are disjoint, so $`A,F`$ are disjoint. We compute the block, rather than conclude adjacency from that fact.

Cutting $`P`$ along the two reaching annuli gives
```math
P\mathbin{\|}(S^1\times(\beta_+\cup\beta_-))=S^1_\lambda\times D,
```
where $`D`$ is a disk. Its original outer boundary is cut into two intervals $`J_0,J_1`$. Cutting $`Q`$ along the two fibre copies gives **two** product blocks $`K_0,K_1`$, each homeomorphic to $`R\times I`$. Each block's vertical annulus attaches to the corresponding $`S^1_\lambda\times J_i`$.

Consequently the **whole** cut complement is the connected manifold
```math
N_F=(S^1_\lambda\times D)\cup K_0\cup K_1,
\qquad\text{(6.1)}
```
with precisely these two annular attachments. Both companion blocks belong to this same complete block. The global $`\phi`$ vanishes on $`Q`$; it does not introduce a separate companion covering or a free phase-lift choice.

In the disk $`D`$, the remaining seam $`\alpha`$ is a proper arc separating $`D`$ into two disks $`D_0,D_1`$. Each contains precisely one of the intervals $`J_0,J_1`$, as seen by cutting the three seams into their two hexagons. Thus $`A`$ cuts (6.1) into exactly two connected chambers
```math
W_i=(S^1_\lambda\times D_i)\cup K_i,\qquad i=0,1.
\qquad\text{(6.2)}
```
They meet along the one connected annulus $`A`$, and both have nonempty interiors.

The complement of every spanning system is connected: the meridian at a boundary of each component crosses that component once and misses the rest; after deleting its crossing segment, it joins that component's two sides in the complement. The connected dual graph therefore has every edge a loop and has one vertex. Moreover all complement loops have $`\phi=0`$, by algebraic intersection with the whole surface. Thus the open complement lifts homeomorphically, and stacking complete blocks constructs the cyclic cover.

Take one lift $`\widetilde N_F`$ of (6.1). Because $`A`$ is connected and contained in the open complement of $`F`$, this lift contains exactly one entire lift of $`A`$; the other lifts lie in the other translates of the $`F`$-block. In the $`A`$-block indexing, its two chambers (6.2) have indices $`k,k+1`$, after choosing the coorientation. There is no other $`A`$-wall inside this block, and both chambers have interior points. The open $`F`$-block therefore intersects exactly these two consecutive open $`A`$-blocks:
```math
D(A,F)=(k+1)-k=1.
\qquad\text{(6.3)}
```
This proves $`\delta(a,v)\le1`$ using the complete complement of the disconnected system.

### 6.2. Why varying representatives cannot give width zero

Here is a direct elementary lower bound, avoiding a minimum-norm metric theorem.

If an open complete $`F'`$-block has index width zero against an $`A'`$-system, it cannot contain any point of any $`A'`$-wall. A small ball about such an interior point, contained in the open $`F'`$-block, would meet the two $`A'`$-blocks on its opposite sides, with consecutive indices. It would give width at least one.

But every interior point of $`A'\setminus F'`$ has a lift in that whole $`F'`$-block: the block maps homeomorphically onto $`M\setminus F'`$. Therefore width zero implies
```math
\mathrm{int}A'\subset F'.
\qquad\text{(6.4)}
```
Properness and closure give $`A'\subset F'`$. The connected interior of $`A'`$ must lie in one component of $`F'`$, and its closure still lies in that component. But $`A'`$ has boundary on both actual tori, whereas every component of $`F'`$ has boundary on only one of them. This is impossible. Thus every pair of representatives has positive integer width, and $`\delta(a,v)\ge1`$.

Together with (6.3) this proves the required equality. Since §5 classified the entire vertex set, flag completion gives exactly one edge and no higher simplex. Contraction of that closed edge to $`a`$ proves Theorem 1.1.

## 7. The exterior is not Seifert fibred, and the link is not in $`\mathcal C`$

### 7.1. The exterior is not Seifert fibred

Suppose $`M`$ were Seifert fibred. A Seifert base for a manifold embedded in $`S^3`$ is orientable: an orientation-reversing simple loop in a nonorientable base, avoiding cone points, would lift to an embedded Klein bottle (H, printed p. 32). A closed nonorientable surface cannot embed in $`S^3`$: its one-sided neighbourhood gives a closed transverse loop with mod-two intersection one, whereas its class in $`H_2(S^3;\mathbb Z/2)`$ is zero. Orient the regular fibre $`z`$ and put $`k=\phi(z)`$.

On each actual boundary torus the prescribed spanning slope generates the primitive kernel of $`\phi`$, while $`\phi`$ has value one on the oriented meridian. Thus its intersection with the fibre slope has magnitude $`|k|`$.

If $`k=0`$, that spanning slope is the fibre slope. H's classification then makes every boundary-bearing essential component vertical, hence an annulus. This contradicts the genus-$`g`$ components of $`F`$, since $`g\ge1`$.

If $`k\ne0`$, every such component must be horizontal. Projection of a connected horizontal component is onto the entire base (H, printed p. 23), so it meets every actual boundary torus. Two components would then use each torus at least twice. This contradicts the one-boundary-per-torus system $`F`$.

The solid-torus exception cannot occur: $`M`$ has two incompressible boundary tori. Hence $`M`$ is not Seifert fibred. This argument is the local Hatcher dichotomy, not a reliance on a guess from the name “satellite”.

Non-splitness was proved in §4.

### 7.2. No covered factors can produce this link by connected sums

In a finite specified-component sum of nonempty links $`J_1,\ldots,J_N`$,
```math
|L|-1=\sum_i(|J_i|-1).
\qquad\text{(7.1)}
```
For $`|L|=2`$, exactly one original factor $`J`$ has two components, and every other original factor is a knot. There cannot be two genuine multicomponent factors. Such a tree is a two-component factor with knots locally inserted along its components, allowing further knot connected sums.

An annular spanning surface prevents every nontrivial local knot factor. To verify this rather than infer it from the knot type, put the annulus in single-arc normal form with the meridional decomposing annuli. The normalisation uses only the following facts: a decomposing annulus core has $`\phi=\pm1`$; every surface loop has $`\phi=0`$; essential intersection circles are excluded; trivial circles are removed by incompressibility and irreducibility; the spanning boundary has one intersection with each meridional boundary circle. This is the single-arc normal form of Banks B (preprint p. 22), whose all-genus form uses only the facts just listed.

The cut knot pieces are connected single-boundary Seifert surfaces; the central $`J`$-piece is connected, since attaching knot pieces along one interval cannot join separate central components. Every piece is a subsurface of the original genus-zero annulus and therefore has genus zero. In particular each single-boundary knot piece is a disk. Every original knot factor is an unknot. Equivalently the interval-gluing genus formula is
```math
0=g(A)=g(A_J)+\sum_i g(R_{K_i}),
\qquad\text{(7.2)}
```
with all summands nonnegative. This argument can be applied to the whole decomposition tree. More explicitly, at a node with a two-component block and a knot block, the single trace cuts the annulus into a two-boundary genus-zero surface and a one-boundary disk, respectively. The knot block is an unknot. Cutting that disk along the knot block's remaining decomposition annuli produces one-boundary disks for its original knot leaves. Repeat on the two-component block. This proves the assertion for arbitrary bracketings and component choices, without a prime-knot assumption.

All knot factors are consequently trivial and the two-component factor $`J`$ is isotopic to $`L`$. But $`L`$ is neither a knot, nor a link with all incompressible spanning surfaces connected, nor one with all incompressible spanning surfaces norm-minimising: the two vertices in Theorem 1.1 explicitly rule out the latter two alternatives. Thus $`J`$ cannot be one of the factors allowed in $`\mathcal C`$. Equation (7.1) rules out every other route into $`\mathcal C`$. This proves Theorem 1.2.

## 8. Scope

The proof establishes the all-genus longitudinal companion theorem and fibre uniqueness (§3), the complete vertex and gluing classification (§§4–5), the whole-block distance-one equality and contraction (§6), and the exclusion from $`\mathcal C`$ (§7). The fibre uniqueness and simultaneous two-component isotopy are written separately because neither is supplied just by the primitive-class observation.

The only minimum used in the surface classification is the integer minimum of the number of $`T`$-intersection circles. It is not a genus, Euler-characteristic, norm or area minimum. No finite enumeration is part of the proof.

The proof is specific to two oppositely oriented zero-framed parallels of a torus knot. Part 7, Theorem B extends it to iterated cables, and Part 12, Theorems A and G, to arbitrary integer framings, numbers and orientations of parallels of recursive graph knots.

[Overview](../README.md)
