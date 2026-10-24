# Part 8. The square-knot cancellation tree and recursive graph-knot double parallels

[Overview](../README.md) · [Next page](part8-2.md) · Part 8, page 1 of 3

**Scope and status.** This part proves the case of the two oppositely oriented zero-framed parallels of the square knot, and a larger connected-sum family. Section 11 extends the same tree theorem to the recursively specified family obtained from nontrivial torus knots by arbitrary finite connected sums and nontrivial cablings. It does not prove contractibility for every graph-manifold link. Its conclusion for the square knot is stronger than contractibility: the complete ordinary all-incompressible complexes are the same simplicial tree. The annular vertex is a root, but is not a cone vertex. The ordinary-isotopy argument needed for the parent map is proved at the outer pattern torus. Section 10 additionally gives the square knot's reference-dependent ordinary coordinates, including its two remaining integral coordinates; signed sheet counts alone are not treated as a classification. A complete arithmetic coordinate catalogue for the larger recursive family is not supplied.

The tree proof below does not use Part 7, Theorem D, or an extension of the taut PS contraction. It uses the elementary essential-cut and Seifert arguments, a precisely specified ordinary product-region input, and, for the cyclic metric, the printed all-incompressible extension in Banks §10. No external novelty is claimed.

## 1. Statement and conventions

Use the ordinary reduced spanning conventions of [Section 1](objects.md). In particular, every labelled actual torus is used once, components are oriented and incompressible, closed components are excluded, boundary curves can slide, and ambient isotopies start at the identity. The cyclic cover uses the entire complement of the whole spanning system. Write $`X`$ for the flag complex of cyclic class distance one and $`Y`$ for the simultaneous geometric complex.

Let

```math
K=K_1\#\cdots\#K_m,\qquad K_i=T(p_i,q_i),\qquad
m\ge2,\quad p_i\ge2,\quad |q_i|\ge2,\quad \gcd(p_i,q_i)=1.
```

Set

```math
s_i=p_iq_i\ne0,\qquad g_i=\frac{(p_i-1)(|q_i|-1)}2.
```

Let $`L(K)`$ be the two oppositely oriented zero-framed parallels of $`K`$. Denote by $`a`$ the spanning annulus in the parallel pattern. Denote by $`v`$ the two oppositely oriented spanning fibres of $`E(K)`$, extended by the two pattern tethers.

**Theorem 1.1 (rooted-tree theorem).** For every such $`K`$:

1. $`X(L(K))=Y(L(K))`$, and this complex is a simplicial tree rooted at $`a`$.
2. The only disconnected vertex is $`v`$; it is a pendant vertex adjacent only to $`a`$.
3. Every other vertex is a connected surface. Apart from $`a`$, it has an efficient pattern consisting of two actual-to-companion annuli and $`r-1`$ essential companion-to-companion returning annuli, for a class-invariant integer $`r\ge1`$.
4. For $`r>1`$, surgery at the first pattern return, viewed from the positive actual torus, gives a well-defined ordinary parent $`p(s)`$. It satisfies $`r(p(s))\lt r(s)`$ and is adjacent to $`s`$. For $`r=1`$, put $`p(s)=a`$, and put $`p(v)=a`$.
5. The complete edge criterion is

```math
\{s,t\}\text{ is an edge}\quad\Longleftrightarrow\quad p(s)=t\text{ or }p(t)=s.
```

Consequently both complexes are contractible in the ordinary weak/CW topology. The root-path contraction is finite on every closed simplex cylinder.

The integer $`r`$ counts companion pieces, not the genus in the general statement. A normal form of a connected nonannular vertex has a nonempty subset

```math
V\subseteq\{1,\ldots,m\},\qquad \sum_{i\in V}s_i=0,
\qquad\text{(1.1)}
```

of vertical leaves. Necessarily $`|V|\ge2`$. Put $`H=\{1,\ldots,m\}\setminus V`$. Every companion piece has two oppositely oriented longitudinal boundaries and genus

```math
b(V)=|V|-1+2\sum_{i\in H}g_i>0.
\qquad\text{(1.2)}
```

The whole connected surface has genus $`r b(V)`$. Every subset satisfying (1.1) and every $`r\ge1`$ is realised. These are exhaustive **normal types**. We do not declare different choices of local twisting to be identical, nor do we use an unproved integer quotient to identify vertices.

**Corollary 1.2 (square knot).** For

```math
K=T(2,3)\#\overline{T(2,3)},
```

the only nonempty vertical subset is both leaves, and $`b(V)=1`$. Thus the parameter $`r`$ is exactly the genus of a connected nonannular vertex. The complete complexes are the same rooted tree. For the genus-$`r`$ vertices $`s_r`$ displayed in Part 7, Proposition C,

```math
\delta(a,s_r)=r.
\qquad\text{(1.3)}
```

In particular the tree has unbounded diameter, and $`a`$ is not a cone vertex.

**Corollary 1.3 (no cancellation subset).** If the nonzero integers $`s_i`$ have no nonempty zero-sum subset, the full vertex set is exactly $`\{a,v\}`$ and $`X=Y=\Delta^1`$. This includes connected sums of torus knots with all the $`s_i`$ of the same sign.

## 2. The exterior and efficient local pieces

Write

```math
M=E(L(K))=P\cup_{T_0}Q,\qquad
P=S^1_\lambda\times B_0,
```

where $`B_0`$ is a pair of pants with labelled actual holes $`b_+,b_-`$ and outer boundary $`b_0`$. Also

```math
Q=R\cup_{T_1\sqcup\cdots\sqcup T_m}\coprod_i Q_i,\qquad
R=S^1_\mu\times B_m,\qquad Q_i=E(K_i),
```

where $`B_m`$ is a sphere with $`m+1`$ holes. The coordinates satisfy

```math
\mu_i=\mu,\qquad \lambda=\lambda_1+\cdots+\lambda_m,
\qquad h_i=\lambda_i+s_i\mu.
\qquad\text{(2.1)}
```

The pattern fibre is $`\lambda`$, the composing fibre is $`\mu`$, and the leaf fibres are $`h_i`$. Adjacent fibre slopes intersect once. The pieces have incompressible boundary and are irreducible; the gluings are genuine JSJ gluings. This is the usual actual connected-sum and parallel construction in $`S^3`$, not an abstract graph of gluing matrices. Irreducibility under the incompressible gluings proves that $`L(K)`$ is non-split. The spanning class vanishes on all of $`Q`$.

### 2.1. Essential cuts, also for a disjoint finite family

Minimise intersection with the relevant torus collection. Inessential circles are removed by incompressibility and irreducibility. A boundary-parallel cut annulus with both ends on an internal torus gives an annular parallelism. Inside its solid torus, every intervening cut piece is an incompressible annulus with primitive longitudinal boundary. An innermost such annulus has an empty parallelism, removing two trace circles. Therefore it cannot occur at a minimum. A cut annulus using two boundaries on one actual torus cannot belong to a spanning vertex.

Thus all cut pieces are incompressible and boundary-incompressible: Hatcher Lemma 1.11 says the only boundary-compressible alternative, in this torus-boundary setting, is a boundary-parallel annulus. This argument applies to the embedded union of a finite disjoint family, keeping the labels of its constituent surfaces. It does not assume that separately minimised surfaces remain disjoint.

The same argument works first at $`T_0`$ alone, and then at the internal tori of $`Q`$ relative to its fixed outer trace. A parallel cut annulus with both ends on the original outer boundary of $`Q`$ would be a whole boundary-parallel component of the initial $`Q`$ cut, already excluded. No increase of the $`T_0`$ trace is required for the internal normalisation.

### 2.2. The pattern

Apply Hatcher Proposition 1.12 to the finite essential system. Its actual boundary slopes are the pattern fibre. A horizontal piece would meet those actual tori transversely to the fibre and is impossible. Hence the pattern pieces are vertical annuli.

If the two actual ends are paired, that annulus is already the whole spanning surface: any other component would be closed. This is $`a`$. Otherwise there are exactly two actual-to-outer tethers; all additional pattern pieces are essential outer-to-outer returns. A return arc in a pair of pants separates its two other holes. A disjoint return system is a parallel nested packet, linearly ordered from $`b_+`$ to $`b_-`$. In particular, its order does not use a chosen metric or a choice of phase origin.

If there are $`r-1`$ returns, the outer trace has $`2r`$ longitudinal circles. Number them cyclically, with the positive tether at $`0`$, in the positive $`\mu`$ direction. The negative tether is at $`r`$, and the return matching is

```math
P(i)=-i\pmod{2r},\qquad i\ne0,r.
\qquad\text{(2.2)}
```

The return nearest $`b_+`$ pairs $`1`$ with $`2r-1`$, the next pairs $`2`$ with $`2r-2`$, and so on.

### 2.3. The companion modes

Since the outer trace is longitudinal, it is transverse to the composing fibre $`\mu`$. All composing pieces are horizontal. A connected horizontal piece has primitive dual class $`\eta`$. Indeed its nonzero signed intersection with the oriented Seifert fibre makes it nonseparating; a loop crossing it once proves primitivity. Its complement is the horizontal product of Hatcher's argument. Every other disjoint horizontal component is a degree-one graph in that product: a finite covering's sheet order in an interval has no nontrivial monodromy. Thus the pieces are jointly parallel.

Orient $`\eta`$ so that

```math
\eta(\mu)=d>0,\qquad \eta(\lambda_i)=a_i,\qquad \sum_i a_i=0.
```

A horizontal piece in a torus-knot leaf has coherent boundary on its one boundary torus. Its boundary slope must be longitude. It is the primitive one-boundary spanning fibre. A vertical piece is an essential returning annulus of slope $`h_i`$. Therefore each leaf is of one of the following two types:

```math
i\in H:\ a_i=0;\qquad
i\in V:\ a_i=-s_i d.
```

Primitivity now forces $`d=1`$, and the sum condition gives (1.1). Each composing piece is a section of

```math
\eta_V(\mu)=1,\qquad
\eta_V(\lambda_i)=
\begin{cases}-s_i&i\in V,\\0&i\in H.
\end{cases}
\qquad\text{(2.3)}
```

Each horizontal leaf has one fibre attached to each section. Each vertical leaf has a parallel system of essential annuli separating its two exceptional fibres. The net class in $`Q`$ is zero, so the section signs contain equally many $`+`$ and $`-`$ signs.

If $`V`$ is empty, each section with its leaf fibres is a one-boundary spanning fibre of $`K`$. A pattern return would join the sole boundaries of two such pieces and create a forbidden closed component. Hence there are exactly two tethers and two oppositely oriented fibres. This gives $`v`$.

Its ordinary uniqueness follows by jointly putting the two companion fibres at bundle phases and following the actual path of the two outer tether endpoints by these phases. The two-tether pants system has one unmarked class; actual boundary motion absorbs actual collar turns, and a common bundle-phase circuit absorbs outer winding. This is the compatible-path argument for a fibre bundle, and does not require periodic monodromy. The fibre product and the usual all-incompressible fibred-point argument give the required fibre uniqueness.

The remaining case has $`V\ne\varnothing`$, hence $`|V|\ge2`$. It is treated next.

## 3. The signed matching rigidity

This finite lemma is the cancellation-specific step. No ordinary-isotopy classification is inferred merely from these numbers.

**Lemma 3.1 (two defects force one matching).** Let $`n=2r`$, with two actual tethers at $`0,r`$. Let $`P(i)=-i`$ for $`i\ne0,r`$. Suppose there is a sign function $`\epsilon_i\in\{+1,-1\}`$ with

```math
\epsilon_0=1,\quad \epsilon_r=-1,\quad
\epsilon_{P(i)}=-\epsilon_i\ (i\ne0,r).
\qquad\text{(3.1)}
```

For each of at least two vertical leaves let its perfect matching be

```math
L_j(i)=c_j-i\pmod n,\qquad c_j\text{ odd},\qquad
\epsilon_{L_j(i)}=-\epsilon_i.
\qquad\text{(3.2)}
```

Then all the $`c_j`$ are equal modulo $`n`$.

**Proof.** Two leaf reflections compose to translation by $`d=c_j-c_k`$. Their two sign reversals imply $`\epsilon_{i+d}=\epsilon_i`$. If $`d\notin\{0,r\}`$, then $`\epsilon_d=\epsilon_{-d}=\epsilon_0`$, contradicting the pattern relation at $`d`$. If $`d=r`$, periodicity contradicts $`\epsilon_r=-\epsilon_0`$. Thus $`d=0`$. ∎

The hypotheses follow geometrically. Essential return arcs in a twice-coned disk are parallel and separate its two cones. On cyclically numbered boundary positions their matching is a fixed-point-free reflection, necessarily with odd offset. Each annulus has oppositely oriented ends. The same is true of each pattern return. Since (2.3) has degree one at every port, each port reads the same section order, with its fixed peripheral orientation convention; matching pairs and section signs are consequently compared using the section labels themselves.

**Lemma 3.2 (the surface is a chain).** Write the common offset as $`c`$. A reduced spanning assembly in the nonempty-$`V`$ mode has

```math
\gcd(c,2r)=1.
\qquad\text{(3.3)}
```

Its companion intersection is a collection of $`r`$ connected pieces, each consisting of two sections, their horizontal leaf caps, and the $`|V|`$ annuli joining the same section pair at the vertical leaves. Every such piece has two outer boundaries of opposite longitude orientation and genus $`b(V)`$. The pattern returns join these pieces in one path from the positive actual boundary to the negative actual boundary. Every pattern return core separates those actual boundaries, and both sides of that cut have positive genus.

**Proof.** Each vertical leaf joins precisely the same section pairs by Lemma 3.1. This gives the stated two-section companion pieces. Two sections, each with genus $`\sum_{H}g_i`$ after capping the horizontal leaves, glued along $`|V|`$ annuli, have genus (1.2) and two outer boundaries.

Collapse each of these companion pieces to an edge $`L`$, retaining the pattern edges $`P`$. At every nonactual section endpoint there is one edge of each type. The two actual endpoints have just their $`L`$ edge. Thus the reduced incidence graph is a path between actual endpoints together with possible cycles. A cycle is a closed original surface component and is forbidden.

The orbit of $`0`$ under the two reflections is the subgroup of $`\mathbb Z/(2r)`$ generated by $`c`$. Since $`c`$ is odd, $`g=\gcd(c,2r)`$ is odd and divides $`r`$. Thus both actual endpoints belong to that orbit. All other orbits, if any, are closed components. Reducedness is therefore exactly (3.3). For a unit $`c`$, the path is explicitly

```math
0,\ c,\ -c,\ 2c,\ -2c,\ldots,(r-1)c,\ -(r-1)c,\ r
\quad\pmod{2r}.
\qquad\text{(3.4)}
```

Each pattern edge is a bridge of this path. Each side contains at least one companion piece, of genus $`b(V)>0`$. Opposite boundary orientations propagate along the path, giving the orientation statement at every cut. ∎

This also proves that every nonempty-$`V`$ spanning assembly is connected. In particular there are no additional disconnected vertices besides $`v`$.

Conversely, for any nonempty $`V`$ satisfying (1.1), any $`r\ge1`$, and any odd unit $`c`$ modulo $`2r`$, use the path (3.4) to assign alternating signs. These signs satisfy both the pattern and leaf matching conditions. Choose $`2r`$ parallel sections of (2.3), the indicated horizontal fibres, and nested vertical returns with this common reflection. The pattern has matching (2.2) and its two tethers. The graph is connected, so there is no closed component. Every local piece is essential. A compression disk minimised against the JSJ tori would give a piece compression or, by an outermost arc, a piece boundary compression. Both are excluded. Thus these are actual incompressible spanning surfaces, for all $`r`$.

## 4. The ordinary-isotopy interface at the outer torus

We need the return order and the surgery to be invariant under ordinary isotopy. We do **not** quotient the leaf parameters independently, and do not assume that an auxiliary horizontal phase is the global cyclic-cover coordinate.

**Lemma 4.1 (outer-torus comparison).** Suppose two ordinarily isotopic spanning surfaces are cut essentially by $`T_0`$, and their $`T_0`$ traces have the pattern-fibre slope $`\lambda`$ (empty traces are allowed). Then they are related by an ordinary isotopy preserving $`T_0`$ setwise. The same assertion holds for two isotopic labelled unions when their components are matched by that isotopy and all their cuts are essential.

**Proof.** Straighten their trace circles and arrange the two finite trace sets to be disjoint on $`T_0`$. Use the incompressible relative-product comparison: Banks Proposition 4.2, with the ordinary boundary motion permitted there, gives product-region pushes between isotopic essential surfaces. Repeat the usual product removal until the representatives coincide.

Here is why those pushes can preserve $`T_0`$. In a product region $`(W\times I)/\sim`$, the torus misses the collapsed face locus and the actual boundary. Because its boundary traces on the two horizontal faces are disjoint essential parallel circles, its intersection is a system of annuli, or contains a whole torus. A whole torus is impossible: the product retracts onto a surface with boundary and has free fundamental group, whereas $`\pi_1(T_0)=\mathbb Z^2`$ injects in $`M`$.

An intersection annulus returning to one horizontal face is parallel into that face. For completeness, its boundary curves are freely homotopic in $`W`$, hence cobound a face annulus. Their union with the returning annulus is a compressible torus in the handlebody. It cannot lie in a ball because its essential face core is nontrivial in $`\pi_1(W)`$. It therefore bounds the parallelism solid torus. A longitudinal degree greater than one would make an essential simple face curve a proper power in the orientable surface group $`\pi_1(W)`$, which is impossible. The degree is one, giving an annular product. Choose an innermost such product among the finite annulus system. Its face annulus has no other torus trace and is a whole cut piece parallel into $`T_0`$, contrary to essentiality.

All remaining torus annuli span the product. Straighten them jointly to $`\gamma\times I`$; this is the product-annulus straightening obtained by cutting the face into disks and using relative disk isotopy. The product push can now be performed tangent to these annuli. Conjugating back preserves the original $`T_0`$ and all boundary labels. Repeating the product comparison gives the required isotopy.

The cyclic-product exception is absent. A connected spanning fibre would have free kernel, whereas the spanning class kills $`\pi_1(Q)`$, which contains the injected $`\mathbb Z^2`$ of $`T_0`$. In the disconnected case a component uses only one actual torus and cannot be a whole fibre of $`M`$: a fibre of a connected surface bundle meets every boundary torus. The ordinary product comparison therefore applies componentwise there as well. ∎

Only the outer torus is used. Its trace slope is already known to be $`\lambda`$ on **both** representatives. In particular this proof does not presume equality of unknown signed trace slopes at all the internal JSJ tori.

**Consequences.** Every essential normal form described above attains the minimum $`T_0`$ count: compare it with a $`T_0`$-minimum representative, whose cuts are essential by §2.1, and apply Lemma 4.1. Hence $`r=\frac12\min\#(S\cap T_0)`$ is an ordinary invariant. For connected nonannular surfaces the companion pairing on the cyclically ordered $`T_0`$ circles is also intrinsic, so the offset $`c`$ of §3, with the positive tether as origin, is an ordinary invariant. These are not asserted to be a complete list of invariants.

The order of the pattern returns is preserved by a $`T_0`$-preserving isotopy: each return separates the two labelled actual tori in $`P`$, and the complementary regions give their linear order. This order is an intrinsic property of the embedded annuli, not a chosen base drawing.

## 5. A canonical annular parent

Let $`s`$ be a connected nonannular vertex with $`r>1`$. Choose an essential normal representative $`S`$. Let $`C`$ be its pattern return nearest the positive actual torus, and take a fibre core $`z\subset C`$. By Lemma 3.2, cutting $`S`$ at $`z`$ gives a positive side and a negative side. Let $`S_-`$ be the side containing the negative actual boundary.

In the part of $`P`$ between the positive actual torus and $`C`$, take a vertical annulus $`J`$ from that actual torus to $`z`$. Its interior misses $`S`$. It can be chosen in the disk left after cutting that annular base region by the positive tether. Attach $`J`$ to $`S_-`$ and take the small proper push-off on the side selected by $`J`$:

```math
P(S)=\mathrm{push}(S_-\cup_z J).
\qquad\text{(5.1)}
```

**Lemma 5.1 (parent properties).** The construction has the following properties.

1. $`P(S)`$ is connected, oriented, incompressible, and has the prescribed single boundary on each actual torus.
2. It has an essential normal form retaining a proper subset of the old companion pieces and of the old pattern returns. In particular $`1\le r(P(S))\lt r(S)`$.
3. It has a representative disjoint from $`S`$.
4. Its ordinary class depends only on $`s`$.
5. If $`S`$ belongs to a finite disjoint essential family and $`C`$ is the first return of the **whole family**, then $`P(S)`$ can be chosen disjoint from that entire family.

**Proof.** The negative side has two boundaries: the negative actual boundary and $`z`$. Lemma 3.2 gives the opposite longitude orientation at $`z`$, so the annular extension gives exactly the positive actual boundary orientation. It is a boundary-collar extension of a subsurface of $`S`$. Cutting an orientable surface along an essential circle injects each cut component's fundamental group; adjoining the collar adds no fundamental group. Since $`S`$ is incompressible, $`P(S)`$ is incompressible. There are no closed components. Hatcher Lemma 1.11 excludes a boundary compression, since a boundary-parallel annulus cannot use two different actual tori.

The deleted positive side and retained negative side each contain a companion piece. The new pattern merely replaces the retained half of $`C`$ by a positive tether; every other retained pattern piece is an old essential return or the old negative tether. All retained companion cuts are unchanged. This proves the normal-form and strict-decrease assertion.

The annulus $`J`$ approaches a definite side of $`S`$ at $`z`$. A sufficiently small regular-neighbourhood push of $`S_-\cup J`$ on that side is disjoint from $`S`$. For a disjoint family, choose the first return of the whole family. All positive tethers cut its positive-side annular base region into disks. The disk incident to that first return provides $`J`$ avoiding every tether and every other surface. The same small push avoids the entire family.

For uniqueness, first fix the essential representative. The positive tether cuts the relevant annular base region to a disk, so the joining arc for $`J`$, with its actual end free, is unique up to isotopy. The solid-torus version is the same primitive-annulus straightening; tangential motion along the full fibre circles gives no framing datum. Changing the core within $`C`$ or the small push-off does not change the ordinary class. Finally Lemma 4.1 carries two essential representatives through a $`T_0`$-preserving isotopy, preserving the first return and the negative side. Transporting $`J`$ and using this uniqueness proves (4). ∎

Define $`p(s)=[P(S)]`$. This is an ordinary-class operation, not a selection of one of several unspecified compressions. There is no compression step. Both the source and the new spanning surface retain their actual boundary orientations.

The local compatibility in (5) is sufficient below. We do not claim that an arbitrary vertex is globally dominated by its parent among all its neighbours.

## 6. Disjoint families have a common companion packet

**Lemma 6.1 (packet lemma).** In a finite disjoint essential family of connected nonannular spanning surfaces, all the companion pieces are jointly parallel copies of a single connected two-boundary surface $`F\subset Q`$, ignoring their orientation signs.

**Proof.** Simultaneously normalise the family at all JSJ tori using §2.1. In the composing block the entire horizontal system is parallel, by §2.3. Thus all its members use the same primitive auxiliary class and the same subset $`V`$. For each individual spanning surface, Lemmas 3.1–3.2 apply to its own subsequence of sections. Each of its companion components consists of a pair of sections joined at every vertical leaf. Consequently, on the section labels of the **whole union**, every vertical leaf has the same matching: each pair is already the pair of one companion component of one input surface.

At one vertical leaf the union of annuli is a parallel essential arc system in a twice-coned disk. Hence this common matching, on $`2N`$ cyclically ordered section positions, is one reflection $`i\mapsto c-i`$ with $`c`$ odd. No assertion that $`c`$ is a unit for this multi-vertex union is needed.

Number the gaps between sections by $`i`$. A vertical-leaf complementary product region joins gap $`i`$ to gap $`c-i-1`$. This gap involution has exactly two fixed gaps and $`N-1`$ paired gaps. The fixed gaps contain the two exceptional-fibre end regions, in whichever order the leaf realisation specifies. Every other region between successive leaf annuli is an annulus product. At a horizontal leaf, each gap has a fibre-product cap.

For each paired gap, glue its two composing section products, the vertical annulus products, and the horizontal fibre products. They give exactly a product between two neighbouring companion components. The interval directions agree with the two sides of these orientable surfaces. Collar reparametrisations and longitudinal tangential twists change the end identification, but do not change the fact that the region is a surface product. There are $`N-1`$ such intervening products and two end regions. Each companion component also has zero relative class in the knot exterior, since its two longitude boundaries have opposite signs; it is separating. Thus the $`N`$ companion components form one linear parallel packet, not a circular product. ∎

This is a statement about one actually disjoint family. It does not say that arbitrary intersecting surfaces have the same companion class.

## 7. The four-holed-sphere comparison and dimension one

**Lemma 7.1.** A simultaneous geometric simplex has at most two distinct vertices.

**Proof.** First consider a disjoint family containing a connected nonannular surface. Its normalisation cannot also contain $`v`$: in a vertical leaf of the connected surface the trace has slope $`h_i`$, whereas the capped vertex has longitudinal trace. Equivalently, the joint composing horizontal class cannot be both $`\eta_V`$ and $`\eta_\varnothing`$. Thus all members are connected, possibly including $`a`$.

By Lemma 6.1 all companion pieces of the nonannular members lie as slices in one product $`F\times I`$, where $`F`$ has two boundary circles. Its two vertical boundary annuli occupy disjoint longitudinal strips in $`T_0`$. Use a slightly larger product neighbourhood if necessary.

For an auxiliary two-dimensional model only, replace $`F`$ by an annulus with the same two labelled boundary circles. The product becomes a circle times a rectangle, attached to the outer boundary of the pattern pants along two sides. The resulting base $`B^*`$ is an orientable four-holed sphere: two holes are the actual holes, and two are auxiliary holes at the ends of the companion packet. Let $`d`$ be the rectangle's cocore, an arc joining the two auxiliary holes. Cutting $`B^*`$ along $`d`$ recovers the pattern pants with collars.

Each whole spanning surface becomes a proper simple arc $`\alpha`$ from the positive actual hole to the negative actual hole. Each companion slice is one crossing of $`d`$. The original pattern returns are essential in the cut pants, so $`\alpha`$ and $`d`$ have no bigon. There is no boundary half-bigon because their endpoints belong to disjoint pairs of boundary components. Thus all these arcs are in minimum position with $`d`$. The annulus $`a`$, if present, gives an arc disjoint from $`d`$.

Three disjoint arcs between the two actual holes in a four-holed sphere contain an isotopic pair. To see this, cap the actual holes to two vertices. Three such edges on the sphere cut it into three regions, while there are only two auxiliary holes. One region has neither auxiliary hole and gives the rectangular parallelism between two adjacent arcs. For a larger family the same argument finds an empty region. Denote the corresponding empty rectangle by $`D`$.

We must lift this parallelism back to the actual three-manifold; isotopy in the auxiliary model alone is insufficient. The arc $`d`$ has no endpoint inside $`D`$. Every component of $`d\cap D`$ spans from one of its parallel arc sides to the other. A returning component would give an innermost bigon with one of the two arcs, contrary to their minimum position with $`d`$. Parametrise $`D`$ as a rectangle with these spanning components as product crosscuts. Replace each annular crossing back by $`F`$. The crosscut product structure gives $`F\times I`$ there, and the remaining rectangles give the pattern annulus products. These products glue, with the same interval coordinate, to an actual product between the two original whole spanning surfaces. Their actual boundary orientations agree. They are therefore ordinarily isotopic.

Thus three distinct connected vertices cannot occur in a geometric simplex. A simplex containing $`v`$ can contain only $`a`$ besides it, by the preceding slope argument and the complete vertex types. The annulus and capped vertex do have disjoint representatives, using the two tethers and a third pants seam. ∎

The auxiliary four-holed sphere is used only for a given disjoint family. Its isotopy classes are not silently identified with the entire ordinary vertex set. The lifting of the empty rectangle, including minimum position with its cocore, is the necessary step in the proof.

## 8. Edges, the unique parent, and the tree

The vertex $`a`$ is geometrically adjacent to every $`r=1`$ connected vertex: its pattern has just the two tethers, and the remaining pants seam gives a disjoint annulus. If a connected vertex has $`r>1`$, no disjoint annulus representative exists. Indeed, simultaneously normalising such a disjoint pair makes the annular member the zero-trace pattern annulus, and an actual-to-actual seam must cross every essential pattern return. Thus

```math
\mathrm{Lk}_Y(a)=\{v\}\ \cup\ \{s:r(s)=1\}.
\qquad\text{(8.1)}
```

Set the parent of every vertex in (8.1) equal to $`a`$.

For any geometric edge between two connected nonannular vertices, if neither has a pattern return then adjoining $`a`$ would produce a three-vertex geometric simplex, contrary to Lemma 7.1. Otherwise normalise the disjoint pair and choose the first return of their whole pattern system. Suppose it belongs to $`S`$. Lemma 5.1 produces $`p(s)`$ disjoint from both endpoints. It differs from $`s`$, since its genus strictly decreases. Lemma 7.1 forces it to equal the other endpoint. This proves the edge criterion in Theorem 1.1.

Every parent path reaches $`r=1`$ after at most $`r-1`$ surgeries and then reaches $`a`$. Hence the graph is connected. Along every parent edge, the genus strictly decreases, until the final edge to the genus-zero annulus. The capped vertex is a separate pendant edge. A cycle would have a vertex of maximum genus on its nonpendant portion; its two cycle neighbours would both be lower-genus parents, contradicting the uniqueness of $`p`$. Thus the graph has no cycle. Together with Lemma 7.1 this proves that $`Y`$ is a simplicial tree.

### 8.1. Equality with the cyclic complex

Two disjoint connected spanning surfaces have representative cyclic width one. In the whole complement cut along one of them, the other is one connected proper wall. Its dual class vanishes there because both spanning surfaces represent the same global class. It separates that whole cut block into two chambers, with consecutive indices. Distinct ordinary vertices cannot have width zero: width zero would force every point of one whole surface into the other, and hence equality of the connected proper surfaces.

The pair $`a,v`$ also has width one. Cut the pattern along the two tethers and the companion along its two fibres. The whole $`v`$-block is the product solid torus from the cut pants together with the two fibre products. The $`a`$-annulus cuts it into exactly two connected chambers with consecutive indices. This keeps one common deck index for the disconnected spanning system.

Conversely, choose almost transverse simplified representatives attaining the cyclic class minimum, using Banks Proposition 4.10 and its explicit all-incompressible extension in §10. The difference potential near a transverse intersection has four chamber values $`h,h+1,h,h-1`$. Width one is therefore impossible at such an intersection. Separating any coincident components gives geometrically disjoint representatives. Thus the cyclic and geometric edge sets agree. Their common graph is the tree just proved, so its flag completion adds no higher simplex. Therefore $`X=Y`$.

### 8.2. An explicit contraction, including the topology at infinity

Give every tree edge length one. For a point $`x`$ let $`[a,x]`$ be its unique finite root path, and move $`x`$ along that path so that its remaining distance from $`a`$ is $`(1-t)d(a,x)`$. This fixes $`a`$ and ends at $`a`$. On each closed edge cylinder all images lie in the finite union of its two endpoint parent paths, and the map is continuous there. The ordinary CW cylinder criterion, with the compact interval factor, gives continuity on $`|X|\times I`$ in the weak/CW topology. Local finiteness is not required. This proves contractibility and the stronger explicit strong deformation retraction to the root.

[Overview](../README.md) · [Next page](part8-2.md)
