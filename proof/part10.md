# Part 10. Rigid caps, Seifert-support parallels and direct contractions of $`Y`$

[Overview](../README.md) · [Next page](part10-2.md) · Part 10, page 1 of 3

This part works directly on the geometric complex $`Y`$, through circle-valued maps.

**Status.** The full graph-manifold contractibility problem is not closed. This part proves a direct contraction of $`Y`$ for the capped-core class in Theorem 1.1, allowing several actual-boundary patterns, signed cap fibres, nonunit internal demands, and disconnected local complements. Proposition 1.2 supplies an exact rigidity criterion for connected-sum torus-knot caps, including mixed chirality; Theorem 1.3 gives a finite recursive cap certificate and includes all same-sign sum/cable constructions. Theorem 9.2 gives a strict complexity-decreasing geometric path from every vertex in the remaining nonempty-JSJ case to its coherent minimum layer, with an explicit neighbourhood-compatibility gap. Theorem 9.3 reduces all horizontal clusters to finitely many auxiliary primitive fibre types without anchoring. The single-Seifert case is covered by [Theorem 1.2](objects.md) and [Theorem 11.2](geometric-retraction.md) of Sections 1–11. Proposition 8.1 proves that single-pair annularisation followed only by closed-component deletion is not a vertex map: it can leave a compressible component with actual boundary.

A second complete class is proved in §11: balanced zero-framed parallel replacements of every non-split Seifert-exterior support other than the unknot, and graph supports passing a finite no-horizontal-mode certificate. Empty-interface products and fibre-matching amalgamation contract their $`Y`$ directly. In the nonlongitudinal-fibre case, opposite double replacement gives $`X=Y`$ a point, including explicit examples with several adjacent internal zero-restriction blocks. This class is not restricted to one-port caps.

The new contraction uses finite families of global circle maps and an explicit regular-level essentiality lemma. It does not use the first-return parent, the two-defect matching rigidity, or the rooted-tree conclusion of Part 8. Part 8, §13 is used as a test configuration; the local cancellation calculations are given independently.

The proof inputs are [Part 7](part7.md) and [Sections 29–40](graph-theorems.md). [Part 8](part8.md) is separate preceding work and is not an input.

## 1. Objects and the closed subclass

All spanning systems are the reduced, oriented, all-genus systems of Part 7: each labelled actual boundary torus is used once, closed components are excluded, and incompressibility is componentwise. Equivalence is ordinary ambient isotopy starting at the identity, with boundary curves allowed to slide. $`Y`$ is the complex defined by simultaneous whole disjoint representatives. $`X`$ is the cyclic-distance flag complex on the same vertices. We use the Part 7, Theorem D only after proving $`Y`$ contractible.

Let $`M=E(L)`$, with $`\Phi(\mu_i)=1`$. A **longitudinally rigid fibre cap** is a boundary-free submanifold $`Q\cong E(K)`$ with one attaching torus, where:

1. $`K`$ is a nontrivial fibred graph knot with connected one-boundary fibre $`R`$ and fixed bundle map $`p:Q\to\mathbb R/\mathbb Z`$;
2. every connected orientable essential surface in $`Q`$ with nonempty purely preferred-longitudinal boundary has exactly one boundary and is $`R`$, with either orientation;
3. a finite disjoint such system is jointly a parallel fibre system.

Here essential includes boundary-incompressible and excludes a boundary-parallel annulus. This is an exact geometric cap hypothesis, not a hypothesis about minimum genus. The Part 7, Lemma 5.1 verifies it for every nontrivial torus knot followed by any finite sequence of cables with winding $`p\ge2`$, nonzero coprime cabling parameter $`q`$, and either cabling sign. Thus the theorem below has an explicit infinite family of allowed caps without an unproved classification premise.

Choose disjoint such caps $`Q_1,\ldots,Q_s`$ and let the remaining **core** $`N`$ be a connected union of genuine Seifert JSJ blocks. Its other internal cuts are the core JSJ tori. All actual link boundary lies in the core. Assume:

```math
\qquad\text{(C1)}
\Phi|_{\pi_1M_v}\ne0\quad\text{for every core block }M_v;
```
```math
\qquad\text{(C2)}
\text{each component of }\{v\text{ in the core}:\Phi(h_v)\ne0\}
\text{ has actual boundary};
```
```math
\qquad\text{(C3)}
Q_j\text{ attaches to a zero core block, and }
\lambda_{K_j}\text{ is its regular-fibre slope on that torus}.
```

The core-plus-cap incidence graph is a tree. The core blocks are not solid tori or $`T^2\times I`$; unnecessary collars can first be removed. The elementary single-Seifert cases are covered by [Theorem 1.2](objects.md) and [Theorem 11.2](geometric-retraction.md) of Sections 1–11. The ambient manifold is the exterior of the stipulated actual $`S^3`$ link; no realisation theorem for arbitrary gluing matrices is asserted.

**Theorem 1.1 (capped anchored-core theorem).** Under these conditions, $`Y(L)`$ is contractible. Its proof supplies a nullhomotopy of the inclusion of every finite subcomplex, directly in $`Y`$, compatible on the faces of that finite subcomplex. Consequently $`X(L)`$ is contractible by Part 7, Theorem D, and $`|X|`$ remains a strong deformation retract of $`|Y|`$.

The signed cap restriction is $`d_j\psi_j`$, where $`\psi_j`$ is the knot class and $`d_j`$ may be zero. Cap fibres need not have coherent signs; their number is not set equal to $`|d_j|`$. Core blocks need not all have actual boundary. A vertical arc need not have an actual endpoint.

With no caps, the class contains Part 7, Theorem A. With one zero product pattern and one cap, it contains all orientations and all actual counts of the longitudinally rigid parallel families. More importantly it permits caps together with nonzero anchored clusters and several actual-boundary patterns. Section 6 gives an actual three-block example outside the all-blocks-meet-boundary range and outside the zero-framed parallel families.

The theorem does not include the cancelling square-knot companion cap: its essential longitudinal four-boundary pieces violate cap condition 2. This exclusion is visible in the counter-calculation of §8, rather than suppressed in the proof.

**Proposition 1.2 (nonresonant composing caps).** Let
```math
\qquad\text{(1.1)}
K=\mathop{\#}_{i=1}^{r}T(p_i,q_i),\qquad
p_i>1,\quad |q_i|>1,\quad \gcd(p_i,q_i)=1,
```
and put $`s_i=p_iq_i`$, in the convention that the torus-knot fibre slope is $`\lambda_i+s_i\mu_i`$. If
```math
\qquad\text{(1.2)}
\sum_{i\in V}s_i\ne0
\quad\text{for every nonempty }V\subseteq\{1,\ldots,r\},
```
then $`E(K)`$ is a longitudinally rigid fibre cap. For the connected sum $`K`$, condition (1.2) is also necessary. Under (1.2), rigidity persists after any finite sequence of nontrivial cables with winding at least two.

**Proof.** The one-summand case is the torus-knot case already cited. For $`r\ge2`$, cut a connected essential longitudinal surface along the composing tori. The composing block is $`P_{r+1}\times S^1`$, with $`h=\mu`$ and $`\lambda_{\rm out}=\sum_i\lambda_i`$. Its pieces are horizontal because the outer slope is longitude. Their primitive dual $`\eta`$, with orientation chosen so that $`b=\eta(\mu)>0`$, satisfies
```math
\qquad\text{(1.3)}
a_i=\eta(\lambda_i),\qquad \sum_i a_i=0.
```
Every horizontal piece meets every inner port. Essentiality in a torus-knot leaf leaves two possibilities: a horizontal one-boundary fibre of slope $`\lambda_i`$, or a vertical annulus of slope $`\lambda_i+s_i\mu_i`$. Consequently
```math
\qquad\text{(1.4)}
a_i=0\quad\text{or}\quad a_i=-s_i b.
```
The set of vertical leaves would be a nonempty zero-sum subset, contrary to (1.2). Hence all $`a_i=0`$. Primitivity gives $`b=1`$. Each composing piece is one section with one outer boundary, and its leaf fibres each have one boundary, so they cannot connect different sections. A connected whole surface therefore has exactly one outer boundary and is the connected-sum fibre. The connected-sum bundle can equivalently be obtained by matching these section and leaf phases. Finite systems are jointly parallel by cutting at one fibre and applying the relative product lemma.

Conversely, suppose a nonempty $`V`$ has zero framing sum. Use two oppositely oriented sections in the primitive class $`\eta(\mu)=1`$, $`a_i=-s_i`$ for $`i\in V`$ and $`a_i=0`$ otherwise. Such sections are graphs in the product composing block, since their outer longitude evaluation is zero. At each $`i\in V`$, join their ends by an essential vertical annulus in the torus-knot leaf. At every other leaf attach the two one-boundary fibres. All pieces are essential and the annuli make the assembly connected. It has two preferred-longitude outer boundaries with opposite signs and genus
```math
\qquad\text{(1.5)}
|V|-1+2\sum_{i\notin V}g(T(p_i,q_i))\ge1.
```
Essential assembly proves incompressibility and boundary-incompressibility. This contradicts longitudinal rigidity. The inequality uses $`|V|\ge2`$, since no $`s_i`$ is zero.

Under (1.2), the cabling argument of Part 7, Lemma 5.1 uses only the established one-boundary fibre conclusion for the preceding companion. Its peripheral identities force every new inner trace to be coherent longitude and each new outer piece to have one boundary. The same induction therefore applies with this connected-sum cap as its initial knot. ∎

All $`s_i`$ of the same sign satisfy (1.2), but the criterion also permits mixed signs. For example $`T(2,3)\#T(2,-5)`$ has framings $`6,-10`$ and is allowed. The square knot has framings $`6,-6`$ and is excluded for the exact zero-sum reason. This is a boundary-slope argument for caps, not a first-return or rooted-tree contraction. In particular it supplies caps with a boundary-free composing block internal to the actual JSJ tree.

**Theorem 1.3 (recursive cap certificate).** More generally use any finite construction from nontrivial torus knots by connected sums and nontrivial cables. Assign a finite slope envelope $`\mathcal S(K)`$, starting with
```math
\qquad\text{(1.6)}
\mathcal S(T(p,q))=\{0,pq\}.
```
At a cable and a connected sum put, respectively,
```math
\qquad\text{(1.7)}
\mathcal S(C_{p,q}(J))=\{pq\}\cup p^2\mathcal S(J),\qquad
\mathcal S(J_1\#\cdots\#J_r)=\mathcal S(J_1)+\cdots+\mathcal S(J_r).
```
Here $`p\ge2`$, $`q\ne0`$ is coprime to $`p`$, and the last operation is Minkowski addition. Certify a torus leaf, preserve certification at a cable, and certify a sum node if all its children are certified and
```math
\qquad\text{(1.8)}
r_i\in\mathcal S(J_i),\quad \sum_i r_i=0
\quad\Longrightarrow\quad r_1=\cdots=r_r=0.
```
Every certified knot is a longitudinally rigid fibre cap. In particular this includes arbitrary nesting of connected sums and cables whose torus and cabling signs are all positive, or all negative. It also permits certified mixed-sign constructions.

**Proof.** First every finite boundary slope of an orientable essential surface belongs to the assigned envelope. The slope convention is $`r\mu+\lambda`$, with rational $`r`$; meridional slope is excluded from this assertion.

For a torus knot, horizontal pieces have longitude slope and vertical pieces have fibre slope $`pq`$. In a cable space, a vertical piece has outer slope $`pq`$. Otherwise the pieces are horizontal. Using the peripheral identities
```math
\mu_J=p\mu_C,\qquad \lambda_C=p\lambda_J
\quad\text{in }H_1(W;\mathbb Q),
```
let $`\eta`$ be one horizontal primitive dual. A finite outer slope forces $`\eta(\mu_C)\ne0`$. The kernel slopes at the outer and inner tori consequently satisfy
```math
\qquad\text{(1.9)}
r_{\rm out}=-p\,\eta(\lambda_J)/\eta(\mu_C)
=p^2 r_{\rm in}.
```
Essential cutting makes $`r_{\rm in}`$ a finite essential boundary slope of $`J`$. This proves the cable envelope inclusion. In a composing block a finite outer slope again forces $`\eta(\mu)\ne0`$. The relation $`\lambda_{\rm out}=\sum_i\lambda_i`$ gives
```math
\qquad\text{(1.10)}
r_{\rm out}=\sum_i r_i,
```
where the $`r_i`$ are finite essential boundary slopes in its children. This proves the sum envelope inclusion. A vertical composing piece has meridional outer slope and so is not an omitted finite-slope case.

We now prove rigidity along the construction. At a cable, outer longitude is horizontal and (1.9) forces inner longitude; the one-boundary induction in Proposition 1.2 applies. At a sum node with outer longitude, (1.10) and (1.8) force every child slope to be longitude. Child rigidity then makes every child component a one-boundary fibre. The composing primitive class has all longitude evaluations zero and therefore $`\eta(\mu)=1`$; it is one section. A connected assembly has exactly one outer boundary and is the connected-sum fibre. Joint parallelism follows in its fibre product. This proves the inductive certification assertion.

For all-positive constructions the envelopes lie in $`[0,\infty)`$; for all-negative constructions they lie in $`(-\infty,0]`$. Thus (1.8) is automatic at every sum node. The argument does not require coherence of several cap components: their orientations remain independently retained. ∎

The envelopes are sufficient certificates, not asserted exact boundary-slope spectra in general; no necessity is claimed for the recursive test. The exact criterion of Proposition 1.2 is its torus-child special case.

## 2. Complete normal forms in this class

Use the coarse cut collection $`\mathcal U`$: the core JSJ tori and the outer cap tori. Minimise total intersection, also for the embedded union of a finite disjoint labelled family.

The essential-cut proof of Part 7, §2.1 applies. Inessential circles are removed by disk/ball moves; original components have actual boundary and cannot hide in a ball. A boundary-parallel cut annulus can only return to an internal torus. Its annular parallelism has an innermost empty primitive annulus, reducing the count. Thus all cut pieces are essential before any vertical/horizontal classification.

For a connected horizontal piece in an orientably based Seifert block, signed intersection with the regular fibre is nonzero. Its class is nonzero, hence nonseparating and primitive. Cutting along it gives its interval product. Other disjoint horizontal pieces are ordered degree-one graphs in that product, so are parallel, with individually retained signs. Their total class is

```math
\qquad\text{(2.1)}\Phi_v=(n_+-n_-)\eta_v .
```

This is Part 7, Lemma 2.1. In a zero core block, (C1) and (2.1) exclude horizontal pieces. Thus every zero core piece is a vertical annulus even without actual boundary in that block.

In the nonzero-fibre core forest, start at an actual block. Unit actual usage forces one horizontal piece and coherent trace. Every horizontal copy in the adjacent core block meets the incoming port, so this coherence forces all its signs to agree. Propagate along the tree. Each whole core horizontal cluster $`C`$ has one connected fibre $`H_C`$: every piece at the next block joins the already connected part. An actual meridian of value one makes $`\Phi_C`$ primitive.

The cluster has fibre-positive phase maps and need not have periodic monodromy. Its individual local total fibre can be disconnected. Its external port traces are coherent of size $`q_e=\mathrm{div}(\Phi|_{T_e})>0`$.

Between two zero core blocks, distinct genuine fibre slopes force empty trace. At a cap port, every nonempty trace has the core fibre slope, which is $`\lambda_{K_j}`$ by (C3). Longitudinal rigidity therefore makes every cap cut component a one-boundary fibre, with its sign retained. Empty cap trace means the cap has no surface.

**Lemma 2.1 (no cap-to-cap normal arc).** Every vertical annulus in an allowed normal spanning system joins distinct ordinary boundary circles, and at least one end is actual or is a port of an anchored horizontal cluster.

**Proof.** At an actual circle there is one endpoint. At an anchored port all endpoints have one sign, excluding a same-port return. Zero-to-zero ports are empty. If both ends are cap ports, including a return to the same cap port, attach the one-boundary fibres at its two ends. This already makes a whole closed component; it cannot join any other piece. Such a component is forbidden in a spanning vertex. These exhaust the endpoint types. ∎

This derives the restrictions from actual normal surfaces. It is not a local unit-end assumption. In particular a port-to-cap arc can have a nonunit anchored port at one end and a boundary-free cap at the other.

Every prescribed normal assembly of these essential pieces, with the indicated actual use and no cap-to-cap arcs, is incompressible: an innermost/outermost compression disk against $`\mathcal U`$ would give a piece compression or boundary compression. Every component has actual boundary, because it either has an actual end or contains an anchored $`H_C`$. No genus restriction is made.

One useful boundary of this subclass is already apparent. If $`N_j`$ is the number of cap fibres in a vertex, then

```math
\qquad\text{(2.2)}
N_j\le
\#\{\text{actual endpoints in its zero block}\}
+\sum_{\text{anchored ports of that block}}q_e .
```

All cap endpoints must join one of these noncap endpoints. Thus the subclass has bounded unsigned cap multiplicity; the unrestricted square-knot cancellation examples do not.

## 3. The ordinary-position and representative interfaces

These interfaces are necessary for a finite-family argument. Choosing unrelated representatives at vertices would not by itself give a homotopy on $`Y`$.

### 3.1. Fixed slopes suffice for torus-preserving comparison

**Lemma 3.1.** Two ordinarily isotopic efficient systems in this class are related by an isotopy preserving every torus of $`\mathcal U`$ setwise. The assertion also applies to two matched labelled disjoint unions.

**Proof.** On each torus both trace systems have the same known unoriented slope: kernel slope at an anchored interface, longitude at a cap interface, or empty trace at a zero-to-zero interface. Arrange the traces disjoint there. Orientation coherence at the cap port is not needed for this arrangement.

Apply the incompressible relative-product comparison, Banks Proposition 4.2. In a product $`(W\times I)/\sim`$, the torus collection gives annuli, or a whole torus. A whole torus would inject $`\mathbb Z^2`$ through the free group of a surface with boundary, impossible. A torus annulus returning to one horizontal face is parallel into that face: its essential simple face core is not a proper power, so its annular parallelism has longitudinal degree one. An innermost such return gives a whole boundary-parallel cut piece, contradicting essentiality. This applies to the entire disjoint torus collection.

All remaining annuli span the product and can be simultaneously straightened to products by cutting $`W`$ to disks. The push is then tangent to them. Iterate the product comparison. This is the fixed-slope argument of Lemma 31.2; it uses the already known common slopes, not a conjectural classification of arbitrary signed JSJ slopes.

A zero core block excludes the cyclic bundle exception for a connected spanning system: its infinite central fibre and an infinite-order element of the planar orbifold kernel inject a $`\mathbb Z^2`$ into $`\ker\Phi`$. A whole spanning fibre has free group. For a disconnected system, each component misses an actual boundary torus and so cannot be a whole fibre of the exterior. If no zero block exists there are no caps by (C3), and the all-horizontal point case of Sections 29–40 applies. ∎

Consequently the ordinary joint vertical-arc classes in the zero cores are intrinsic. The distinct-end detector of Section 31 applies to every one of them, including nonunit ends and retained cones. Choose a negative-curvature metric on each regular marked base. Its orthogeodesic cores are canonical; classes that coexist disjointly have disjoint cores. Parallel occurrences keep their multiplicity.

### 3.2. Caps have a boundary configuration, not an extra spin

For a fixed cap bundle $`p_j`$, each component is one fibre with one boundary. A finite disjoint system is a configuration of distinct phases, labelled by its attaching occurrences and signs. Its cyclic order is exactly the order of its boundary circles on the single attaching torus.

A path of that whole boundary configuration extends by moving the corresponding fibre phases. At fixed boundary circles two such systems are relatively isotopic: normalise one fibre and use the one-boundary product lemma on the remaining fibres in the cut product. A common phase circuit returns the unparameterised system. Thus the cap adds no relative multiport integer. One cannot choose its endpoint motions independently; the entire actual configuration path is extended.

This uses only the one-boundary rigidity and product statements of Part 7, Theorem B. No claim is made for a cap with a connected four-boundary component.

### 3.3. The remaining states are the anchored cluster states

For a connected anchored cluster with marked outer tori, positive phase maps give the relative state

```math
\qquad\text{(3.1)}\mathbb Z^{r_C}/\mathbb Z(1,\ldots,1).
```

Connected-fibre connectors detect the differences; positive interpolation proves sufficiency. Every zero-diagram boundary motion is carried into these states. A loop of a joint zero system has zero port-configuration winding: after a power fixes its occurrences, the distinct endpoint peripheral subgroups give $`d_i^{a}wd_j^{-b}=w`$, forcing $`a=b=0`$, exactly as in Lemma 31.1. That argument uses distinct ends, not coherent signs at a cap port.

Collapse empty zero-to-zero edges to regions $`\Lambda`$ and anchored subtrees to $`C`$. The core incidence graph is a tree, and its marked integer edge states have the form $`n_{\Lambda C}=t_\Lambda-s_C`$, unique up to one common additive integer. Empty interfaces identify the real constants. The one-port caps add no relation between two zero regions, by §3.2. In particular two normal maps for the same vertex with the same zero arc representatives have the same off-band face values and relative cluster data after one global normalisation. This is the precise use of the core tree from Part 7, §4.1.

It follows, by Lemma 3.1 and cap configuration uniqueness, that canonical zero diagrams plus these transported cluster states determine the ordinary global class. This is also sufficient: match the zero-diagram paths, extend each cap endpoint path by its fibre phases, and interpolate the anchored cluster maps in the prescribed relative states. Matching collar isotopies glue over the tree.

We need this sufficiency and intrinsic representative statement, not a closed integer catalogue or a new cyclic-distance formula.

## 4. Global maps and the essentiality of reduced levels

Fix a finite subcomplex $`K_0\subseteq Y`$ and a base vertex $`v_*`$. Use the finite set of canonical zero-core arc classes occurring in these vertices. Choose one finite PL band arrangement on each zero base, with bands disjoint whenever their cores are disjoint. Keep unused cone and empty-port collars constant.

Every allowed core arc has a fixed orientation across all vertices using it: it has a noncap end whose prescribed sign is fixed by an actual boundary or an anchored port. This permits one monotone transverse profile, with nonnegative multiplicity, for that arc class.

For each vertex $`v_i`$, construct a global circle map $`f_i`$ representing it:

* on a zero core it factors through the base, and increases with the appropriate sign through the bands of its annuli;
* on a cap it has the exact form

```math
\qquad\text{(4.1)}f_i|_{Q_j}=g_{ij}\circ p_j,\qquad \deg g_{ij}=d_j;
```

* on an anchored cluster it is fibre-positive in the interior and nonnegative at its banded outer boundary, in the relative state of $`v_i`$.

To construct the cap extension, identify its boundary circle coordinate with the quotient by $`\lambda_{K_j}`$. The boundary restriction of $`p_j`$ has degree one in that coordinate, so the zero-side boundary map is exactly a circle map $`g_{ij}`$ there and extends by (4.1). Its positive and negative bands record all the fibre occurrences.

The anchored extension is the relative positive-phase construction of Sections 29–40 and Part 7. Prescribe the real boundary differences, use fibre-constant collar cutoffs against a reference positive map, and retain the actual relative integers. It permits flat boundary phases and strictly positive interior derivative on each Seifert fibre after division by the fixed sign of $`k_v`$. It does not require periodic cluster monodromy.

Choose the individual band profiles so that every regular phase in $`(0,1)`$ represents $`v_i`$; flat exceptional phases are zero modulo one. One may insert flat plateaus at integer crossings of a multiplicity packet. All regions have one common global gluing, not independently normalised cap lifts.

On the single global $`\Phi`$-cover choose equivariant real lifts $`F_i,F_*`$. For
$`x=\sum_i\lambda_i[v_i]\in|K_0|`$ and $`t\in[0,1]`$ put

```math
\qquad\text{(4.2)}
F_{x,t}=(1-t)\sum_i\lambda_iF_i+tF_* .
```

Its deck displacement is one. It descends to a circle map in the original class $`\Phi`$. On each cap it still factors through the same $`p_j`$: differences between the $`g_{ij}`$ have periodic real lifts, with constants inherited from the global map. There is no additional cap deck generator.

**Lemma 4.1 (harmless deletion for the capped-core class).** A generic level of (4.2), after deleting its whole closed components, is an actual incompressible spanning system.

**Proof.** At a zero core the level is a collection of proper arcs and circles. At an anchored cluster it is blockwise horizontal and coherent: positivity is preserved by (4.2). Its primitive actual boundary forces one connected cluster fibre, by the same anchor propagation as §2. At a cap the level is a finite signed system of whole one-boundary fibres.

On every actual torus the boundary band maps have the same monotonicity and signed degree one. Thus a generic phase uses it exactly once. At an anchored zero-side port all endpoints have their prescribed one sign. An empty zero-to-zero port has a constant phase and is missed by a generic level.

A zero-base circle gives a whole closed vertical component. A zero arc with two cap ends joins the only boundaries of its two cap fibres and also gives a whole closed component. Delete these. A same-actual-boundary return is impossible by single usage; a same-anchored-port return is impossible by coherence. All remaining arcs therefore join distinct ordinary boundaries and have an actual or anchored end. They are essential vertical annuli.

Every retained component has actual boundary, either directly or through an anchored cluster. All its cut pieces are essential; the compression-disk outermost-arc argument proves global incompressibility. No compression choices were made. Deleting closed components does not change $`\Phi`$: in an $`S^3`$ link exterior a closed oriented surface has zero image in relative homology, equivalently zero intersection with the actual meridian basis. Actual usage and orientation are unchanged. ∎

The conclusion uses the one-boundary condition on an **entire cap component**. Replacing it by “algebraic cap demand zero” would be false, as §8 shows.

## 5. A direct finite contraction in $`Y`$

### 5.1. Phase averages and continuity

For each $`(x,t)`$, average the actual ordinary vertices of the reduced generic levels of (4.2), weighted by their phase-interval lengths. Denote the resulting point by $`Q(x,t)`$.

For fixed $`(x,t)`$, these levels are disjoint before and after closed-component deletion. Thus their distinct vertices form a genuine simplex of $`Y`$. No cyclic adjacency assertion is used.

There are only finitely many actual output classes over the finite parameter space. Use the fixed PL zero-base and cap-circle templates. Lifted corner values are affine and bounded; only finitely many integer-translated phase crossings and level templates occur. Anchored cluster fibre types are fixed, and their relative integers are bounded by the same finite boundary-lift ranges. Between critical phases the whole retained system is ordinarily isotopic. At a collision, the affected phase intervals have length tending to zero.

After deletion, read the **actual retained diagrams and relative cluster states**. Do not reuse face indices of deleted circles or closed cap-to-cap assemblies. The finite-template argument still bounds these retained states: it records their boundary tracks and actual retained paths, with only finitely many templates. This is the same necessary rereading step as in Part 7/Sections 29–40; no old potential is asserted unchanged by deletion.

It follows that $`Q`$ is continuous with finite image support on each closed simplex cylinder, including coefficient-zero faces.

### 5.2. The initial carrier is a genuine geometric carrier

At $`t=0`$ the vertices of a true input simplex have canonical zero cores that are disjoint or shared. Generic zero levels then stay in those same bands; none is a new cap-to-cap arc or a closed circle.

Compare with actual simultaneous disjoint normal representatives of that input simplex. Such a family exists by the definition of $`Y`$, and simultaneous efficient cutting plus Lemma 3.1 puts it in the same ordinary diagrams and relative states. Take disjoint whole-component band maps for this family.

Compressing a cooriented parallel arc packet changes neither endpoint lift value. For a generic phase $`r`$, the number of its selected annuli is

```math
\qquad\text{(5.1)}
\lfloor F_e^+-r\rfloor
-\lfloor F_e^--r\rfloor
```

where the transverse coorientation is chosen from $`F_e^-`$ to $`F_e^+`$. This is independent of internal packet profiles or their subdivision into input labels. The off-band integer face values, including their constants in all zero regions, are the same for the selected vertex maps and for the simultaneous normal family, after one common global normalisation. Their weighted values therefore agree.

The full selected states are read by composing the global weighted map with a degree-one band map about phase $`r`$. On an old face its lift is $`\lfloor F_{x,0}-r\rfloor+1`$. This reads the actual relative cluster integers as well as the arc counts in (5.1). There is no deletion at this initial disjoint-family stage, so no obsolete circle or cap-component index is being used.

On an anchored cluster, two such fillings have real difference zero at its marked interfaces and the same relative state. Positive interpolation, with a small interior positive smoothing if a band map has flat interior pieces, gives an isotopy of the selected connected fibres relative to those interfaces. On a cap, a selected boundary configuration determines its entire one-boundary fibre system by §3.2. Hence the selected whole ordinary classes, with their phase weights, are unchanged by this comparison.

For the simultaneous whole-component bands, a generic weighted level is a union of entire input component classes. Choosing phases away from their finitely many centre-wall values makes all output representatives disjoint from all input representatives as well as from one another. This is the geometric component-wall carrier of Part 7, §9.2; this part of its proof uses neither $`X`$ nor a class-minimum metric.

Thus the positive-weight vertices of $`Q(x,0)`$, together with the input vertices, have simultaneous whole disjoint representatives. In particular

```math
\qquad\text{(5.2)}J(x,u)=(1-u)x+uQ(x,0),\qquad0\le u\le1,
```

stays in $`Y`$. The same fixed maps were used on all faces of $`K_0`$, so these carriers agree there.

### 5.3. Endpoint and CW conclusion

At $`t=1`$, every reduced regular level is the base vertex, so $`Q(x,1)=[v_*]`$. Concatenating (5.2) with $`Q(x,t)`$ nullhomotopes the finite inclusion $`K_0\hookrightarrow Y`$.

One-point inputs give connectivity. Compact sphere images in the weak/CW realisation lie in finite subcomplexes, and are killed by these finite inclusion nullhomotopies. Whitehead gives contractibility of $`Y`$. The homotopies need not be a preselected compatible system as $`K_0`$ varies. Continuity on each finite cylinder is the proved finite-support continuity above. The general strong deformation retraction of Part 7, Theorem D, then gives $`X`$ contractible. This completes Theorem 1.1.

[Overview](../README.md) · [Next page](part10-2.md)
