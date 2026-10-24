# Part 10. Rigid caps and Seifert-support parallels (continued)

[Overview](../README.md) · [Previous page](part10.md) · [Next page](part10-3.md) · Part 10, page 2 of 3

## 6. An actual signed-cap example outside the previous named ranges

As a consistency check, the opposite two-parallel torus-knot link has a pants core and one rigid cap. Lemma 2.1 leaves exactly the actual-to-actual annulus or the two actual-to-cap seams with two opposite cap fibres. The ordinary pants systems and the one-port cap state are unique; the two whole systems have disjoint representatives, as in the construction of Part 6. Thus $`Y=X=\Delta^1`$, recovering Part 6 and the cable extension of Part 7, Theorem B. With no caps Theorem 1.1 contains Part 7, Theorem A, so the horizontal-leaf star Theorem 29.2 is also retained.

Take a positive Hopf-fibre piece $`H`$ with two positive actual regular components and one port. Take a keychain piece $`V`$ with its axis as a cap port, two negative actual regular components, and one further regular port. Splice the latter port to the Hopf port by meridian–longitude exchange. Attach a trefoil exterior to the axis port by the same exchange. The core consists of $`V,H`$; the cap is $`E(T(2,3))`$.

This is an actual $`S^3`$ link. The initial Hopf port and the keychain regular port are unknotted. Their splice preserves $`S^3`$; the keychain axis becomes a standard parallel core of the removed Hopf port and remains an unknot. Splicing the trefoil exterior to that axis replaces its unknot neighbourhood in the usual satellite construction and again gives $`S^3`$.

Write $`h_V=\mu_A`$, where $`A`$ is the keychain axis. In keychain homology,

```math
\lambda_A=\mu_1+\mu_2+\mu_P,\qquad
\lambda_1=\lambda_2=\lambda_P=\mu_A.
```

The cap attachment kills the total value on $`\mu_A`$. On the Hopf side $`\Phi(\mu_{\mathrm{port}})=0`$, hence $`k_H=2`$ and $`\Phi(\lambda_{\mathrm{port}})=2`$. Thus

```math
\qquad\text{(6.1)}
k_V=0,\quad \Phi(\mu_1)=\Phi(\mu_2)=-1,\quad
\Phi(\mu_P)=2,\quad
\Phi|_Q=(-1-1+2)\psi=0.
```

The anchored port has demand two and the cap port has net demand zero. All core restrictions are nonzero, and $`H`$ is an actual anchor. The fibre intersections are one on $`VH`$ and six on the cap edge, so both cuts are genuine. All pieces are irreducible with injected boundary; the link is non-split.

The four actual components are winding-one copies of the trefoil. Their linking matrix has the Hopf actual pair of linking $`+1`$ and all other pairwise linkings zero, with the prescribed component orientations. Thus this is not a zero-framed parallel family; actual boundary also lies in two different genuine blocks. It is outside Part 7, Theorem A because the cap restriction is zero, and outside the Part 8 one-pattern parallel families. No claim of exclusion from every possible previously known connected-sum closure is needed for the theorem.

Let $`s\in\{0,1,2\}`$ be the number of negative actual zero-core endpoints sent to the cap instead of directly to $`H`$. The cap has $`s`$ fibres of each sign and $`s`$ anchored-port-to-cap annuli. The other $`2-s`$ actual endpoints go directly to $`H`$.

For the trefoil cap,

```math
\qquad\text{(6.2)}
N_{\mathrm{cap}}=2s,\qquad
-\chi=2+2s,\qquad
\#\text{global components}=1+s.
```

The component containing $`H`$ has genus $`s`$ and $`4-s`$ actual boundaries; the other $`s`$ components have genus one and one actual boundary each. These are incompressible assemblies. The complexity varies from two to six, so the theorem is not merely a taut-surface contraction.

At $`s=2`$, the two anchored-to-cap annuli are parallel and have no actual end. The four-holed zero base cut along its four arc occurrences has two disk chambers. Both the nonunit endpoint and the disconnected local complement are therefore present in an actual example of Theorem 1.1.

For a precise fixed-support check, denote the two negative actual holes by $`A,B`$, the anchored port by $`P`$, and the cap port by $`C`$. Choose the planar five-edge support
```math
\qquad\text{(6.3)}AP,\ BP,\ AC,\ BC,\ CP .
```
With $`x,y\in\{0,1\}`$, its four vertices have multiplicities
```math
\qquad\text{(6.4)}(1-x,\,1-y,\,x,\,y,\,x+y).
```
The two triangular circulation faces have opposite orientation, so their complete potentials are $`(0,x,-y)`$, not $`(0,x,y)`$.

At $`P`$ the endpoint groups, in cyclic order, are the $`AP`$, $`CP`$, $`BP`$ packets. A simultaneous family of $`n`$ connected anchored fibres must read one common input-label order twice, since the port degree is two. Enumerating these packet orders, or directly checking the repeated words, gives exactly the five edges other than $`v_{00}v_{11}`$, and the two triangles
```math
\qquad\text{(6.5)}\{v_{00},v_{10},v_{01}\},\qquad
\{v_{10},v_{01},v_{11}\}.
```
The other endpoints impose no further obstruction: actual circles use each input once, and the one-boundary cap fibres follow their actual endpoint phases.

Common rounding of $`(0,x,-y)`$ has barycentric output
```math
\qquad\text{(6.6)}
\begin{cases}
(1-x-y)[v_{00}]+x[v_{10}]+y[v_{01}],&x+y\le1,\\ 
(1-y)[v_{10}]+(1-x)[v_{01}]+(x+y-1)[v_{11}],&x+y\ge1.
\end{cases}
```
It fixes every actual simplex in (6.5), preserves mean multiplicities, and realises the linear contraction of the square to $`(0,0)`$ inside this geometric disk. The checker compares the repeated-word criterion independently with the common-threshold outputs, including all three choices of global face root. This is a fixed-support test, not an enumeration of the entire infinite complex.

Replace the trefoil cap by $`K=T(2,3)\#T(2,-5)`$. Proposition 1.2 applies since $`6-10\ne0`$, and the same actual satellite construction gives a five-block example. The cap's composing block is boundary-free and internal, and the restriction of $`\Phi`$ to all three cap blocks is zero. The cap fibre has genus three. Formula (6.2) becomes
```math
\qquad\text{(6.7)}
-\chi=2+10s,\qquad
g(\text{component containing }H)=3s,\qquad s=0,1,2.
```
The other $`s`$ actual components have genus three. The core-to-cap fibre intersection is now one; the two internal composing-to-torus-knot intersections are also one, so the five blocks are genuine. The same geometric two-triangle support and nonunit port remain. This example allows mixed chirality and multiple internal zero-restriction blocks while retaining a complete direct contraction.

For a nested mixed-sign certificate, take
```math
\qquad\text{(6.8)}
K=C_{2,1}(T(2,-3))\#T(2,5).
```
The two child envelopes are $`\{0,2,-24\}`$ and $`\{0,10\}`$; their only zero sum is $`0+0`$. Theorem 1.3 certifies this genus-four cap. Its four genuine blocks give a six-block version of the same actual construction, with complexity $`2,16,30`$ for $`s=0,1,2`$. This uses a cable followed by a sum and is not confined to one composing level followed only by cables.

## 7. The unbounded family of Part 7, Proposition C

The following direct local calculation treats the normal diagrams of every genus in Part 7, Proposition C. Choose their embedded representatives coherently by the reverse insertion described below. It is not a claim to have classified every ordinary twisting state or contracted all neighbours of these vertices.

Let $`n=2r`$. The composing sections have signs

```math
\epsilon_0=+,\qquad
\epsilon_i=-\ (1\le i\le r),\qquad
\epsilon_i=+\ (r\lt i\lt n).
```

Both trefoil leaves pair by $`L(i)=1-i\pmod n`$. The two-actual-hole pattern has return pairing $`P(i)=-i\pmod n`$, with actual tethers at $`0,r`$.

Annularise the adjacent positive/negative sections $`0,1`$ across their product slab: replace its two horizontal pants by the three vertical boundary annuli. At each leaf, the existing $`L`$-annulus $`0\leftrightarrow1`$ closes with the new boundary annulus to a whole torus. Delete these two closed tori.

For $`r>1`$, the new outer annulus takes the positive actual tether through the old pattern return $`1\leftrightarrow n-1`$. It becomes the positive tether at $`n-1`$. Relabel the remaining cyclic section order as

```math
\qquad\text{(7.1)}[\,n-1,2,3,\ldots,n-2\,].
```

The residual leaf matching is again $`L(i)=1-i`$ modulo $`2(r-1)`$, the residual pattern matching is $`P(i)=-i`$, and its negative tether is at $`r-1`$. Its signs are precisely the $`r-1`$ word. The retained surface is therefore of the $`r-1`$ normal type and is incompressible by essential assembly. At $`r=1`$ the outer annulus is the actual-to-actual spanning annulus.

To obtain an actual ordinary-class path, fix all collars and section coordinates once and define the displayed family recursively by reversing this operation: insert the first adjacent section pair in the indicated slab, extend the two leaf endcap packets and the first pattern return, and apply no additional collar circuit. Its cancellation then literally recovers the preceding embedded representative with its inherited boundary tracks. Equality of ordinary vertices is not inferred from the permutations alone.

The replacement can be pushed to the appropriate frontier of the product slab and its incident collars, avoiding the original complete surface. This gives a genuine geometric edge from $`s_r`$ to the displayed lower surface. The removed pants raise Euler characteristic by two, so the genus drops by one.

This supplies paths for the entire unbounded displayed family without bounding $`r`$, using no tree classification. It does not prove that one such replacement is dominated by the closed star of its target. Nor does it address every ordinary twisting state. Those are separate finite-neighbourhood requirements, and are not inferred from pointwise descent.

## 8. Balanced four-boundary cancellation: a strict local failure

Use the actual graph link in Part 8, §13: four zero-framed parallels of the square knot, signs $`(+,-,+,-)`$. Its four composing pants sections are $`H_0,H_1,H_2,H_3`$, with these signs in cyclic order. The positive trefoil leaf pairs

```math
\qquad\text{(8.1)}L_+=\{(0,1),(2,3)\},
```

and the mirror leaf pairs

```math
\qquad\text{(8.2)}L_-=\{(0,3),(1,2)\}.
```

The pattern attaches each section to its own actual component. Essential assembly gives the connected genus-one, four-boundary incompressible surface $`S`$, with $`\chi(S)=-4`$.

**Proposition 8.1 (single-pair annularisation is not an essential reduction).** Annularising just the adjacent opposite sections $`H_0,H_1`$, followed only by deleting whole closed components, leaves a compressible actual spanning component. In particular this rule is not a map on vertices of $`Y`$.

**Proof.** Let $`B_{01}`$ be the product slab between these sections. Replace $`H_0,H_1`$ by the three annuli in $`\partial_{\mathrm v}B_{01}`$.

At the outer port, the new annulus joins actual tethers $`0,1`$, giving an actual annular component $`A_{01}`$.

At the positive leaf, the new annulus closes the existing leaf annulus $`0\leftrightarrow1`$ into a whole torus. Delete it.

At the mirror leaf, the new annulus joins the old returns $`0\leftrightarrow3`$ and $`1\leftrightarrow2`$, producing an annulus $`B_{23}`$. This annulus is boundary-parallel. Indeed the two old nested arcs and the port intervals $`0\!-\!1`$, $`2\!-\!3`$ bound the middle rectangle between their essential returns; it contains neither cone. The concatenation along $`0\!-\!1`$ is therefore parallel to $`2\!-\!3`$.

The remaining actual component $`W`$ consists of $`H_2,H_3`$, the essential positive-leaf return $`2\leftrightarrow3`$, and this boundary-parallel mirror annulus, plus actual tethers $`2,3`$. It has $`\chi=-2`$, two actual boundaries and genus one.

Choose a proper arc $`\alpha`$ in the pants $`H`$, from its mirror cuff to itself, separating its outer cuff from its positive cuff. In the adjacent slab between $`H_2,H_3`$, the rectangle $`\alpha\times I`$, extended through the parallelism of $`B_{23}`$, is a compression disk for $`W`$. Its boundary is essential: cutting $`W`$ along it gives a pants side containing the two actual boundaries and a once-punctured-torus side containing no actual boundary. Thus it cannot bound a disk in $`W`$.

After deletion of the one closed torus, $`A_{01}\sqcup W`$ still has the required actual boundaries, but is not incompressible. This proves the assertion. ∎

Compressing $`W`$ along the displayed disk gives an actual annulus and a closed torus; deleting the latter repairs this individual output. Thus the calculation obstructs the proposed vertex rule, not the existence of a lower actual vertex.

The bad retained system is itself an oriented spanning level of a Thom map in the original class $`\Phi`$. Boundary degree and global cohomology therefore do not exclude it. Its whole complement is connected by the actual-meridian argument, which does not use incompressibility. Its global complementary-region graph has one vertex and loop edges, hence no sources or sinks. The source/sink deletion in the surface cycle-complex proof would leave this graph unchanged while the actual component remains compressible.

Thus arbitrary circle-map extension plus whole closed/null-region deletion is insufficient in dimension three. This is not a proof that a carefully chosen affine family must encounter this particular system.

This calculation also identifies why the capped-core lemma works and cannot be silently enlarged. Here a leaf component is an annulus with two port boundaries, rather than a one-boundary fibre. Joining its one end to the new boundary annulus can leave its other end available to connect to another section. The result need not be a whole closed component. A boundary-parallel return can then attach to multi-boundary horizontal pieces and create the compression disk above.

The naive operation works on every $`s_r`$ in §7 and fails on this four-actual-boundary example. Thus neither “the number of horizontal sheets decreases” nor “all closed components are deleted” is a sufficient replacement for a finite-neighbourhood/parameter essentiality proof.

**Corollary 8.2 (balanced multi-component test).** The failure persists for a system with arbitrarily many balanced four-boundary companion components.

Take $`m`$ parallel copies of the four-boundary companion piece and $`4m`$ actual zero-framed parallels, each attached to its corresponding outer boundary. The whole spanning system has $`m`$ connected genus-one, four-actual-boundary components. For section types $`a=0,1,2,3`$ and copy $`k=1,\ldots,m`$, use cyclic indices

```math
\qquad\text{(8.3)}
I(a,k)=
\begin{cases}
am+k-1,&a=0,2,\\ 
am+m-k,&a=1,3.
\end{cases}
```

The signs are $`+^m-^m+^m-^m`$. The two leaf systems are the noncrossing reflections with offsets $`2m-1`$ and $`4m-1`$, respectively. Their component groups are exactly the four sections of each $`k`$.

For copy $`k=m`$, its indices are $`m-1,m,3m-1,3m`$. The first two and last two are adjacent in the whole system. The mirror-return rectangle between its two annuli has these adjacent empty port intervals as its other sides. Thus the annularisation and compression disk of Proposition 8.1 avoid all the other copies. They leave one compressible two-actual-boundary component, one actual annulus, and the other $`m-1`$ original components, after the one closed torus is deleted.

All pieces before the operation are essential; the actual link is the specified $`4m`$-parallel square-knot link in $`S^3`$. This supplies a uniform multi-component, multi-boundary instance, not just an abstract signed matching. ∎

## 9. General pointwise descent and the remaining compatibility gap

### 9.1. Compression relative to an incompressible barrier

**Lemma 9.1 (barrier compression).** Let $`\mathcal B`$ be a finite embedded disjoint union of incompressible proper surfaces in a non-split nontrivial link exterior. Let $`A`$ be a reduced oriented spanning surface disjoint from $`\mathcal B`$, not necessarily incompressible. There is an incompressible reduced spanning surface $`A_{\mathrm{ess}}`$, disjoint from $`\mathcal B`$, obtained by compressions and deletion of closed descendants. Its complexity does not exceed that of $`A`$.

**Proof.** A compression disk for $`A`$ has boundary disjoint from $`\mathcal B`$, so its intersection with the barrier is a union of circles. Every such circle is nullhomotopic in the ambient manifold and hence bounds a disk in its incompressible barrier component. Choose an innermost such disk on the barrier, whose interior misses the compression disk. Replacing the disk it bounds on the compression disk by a nearby copy of this barrier disk gives an embedded compression disk with the same boundary and fewer barrier intersections. Its interior still misses $`A`$, because the barrier misses $`A`$. Repetition gives a compression disk avoiding the barrier entirely.

Compress there and discard closed descendants. Actual boundaries and orientations persist and complexity cannot increase. Repeat if needed. The usual integer
```math
\qquad\text{(9.1)}
\sum_D g(D)+n-b_0(A)
```
for a reduced spanning system, where $`n`$ is the fixed actual boundary count, decreases under a compression after closed descendants are discarded. This proves termination. The final system is globally incompressible, since any further global compression disk could again be made barrier-disjoint. ∎

### 9.2. A strict geometric descent for every graph link

For the genuine Seifert blocks put
```math
\qquad\text{(9.2)}
B_\Phi=\sum_v |\Phi(h_v)|(-\chi^{\mathrm{orb}}(B_v)).
```
The elementary one-Seifert cases are already known. In a nonempty genuine $`S^3`$ JSJ collection each $`\chi^{\mathrm{orb}}(B_v)\lt 0`$. Indeed the nonnegative planar-base cases are a solid torus, $`T^2\times I`$, or a disk with two order-two cones. The first two are not genuine blocks. The last contains a Klein bottle: join the two exceptional-fibre Möbius bands by a vertical annulus. It cannot embed in $`S^3`$.

Write $`c(S)=\chi_-(S)=-\chi(S)`$ for a spanning vertex in this nontrivial boundary-incompressible setting.

**Theorem 9.2 (global pointwise annular descent).** Let a non-split graph-manifold link have a nonempty genuine JSJ collection. For every vertex $`s=[S]`$:

1. $`E(s)=c(S)-B_\Phi`$ is a nonnegative even integer.
2. $`E(s)=0`$ exactly when its efficient horizontal systems have one sign in each entered block.
3. If $`E(s)>0`$, there is a vertex $`s'`$ geometrically adjacent in $`Y`$, with
```math
\qquad\text{(9.3)}c(s')\le c(s)-2 .
```
4. Consequently there is a finite strictly decreasing geometric path to the coherent minimum-complexity layer, of length at most $`E(s)/2`$. The minimum complexity among spanning surfaces is $`B_\Phi`$.

No canonical parent or link domination is asserted.

**Proof.** In an efficient block with horizontal primitive fibre $`H_v`$, let its positive and negative multiplicities be $`a_v,b_v`$, with $`m_v=|\eta_v(h_v)|>0`$. Then
```math
\qquad\text{(9.4)}
-\chi(H_v)=m_v(-\chi^{\mathrm{orb}}(B_v)),\qquad
|\Phi(h_v)|=|a_v-b_v|m_v.
```
Vertical annuli and circle gluings contribute zero. Hence
```math
\qquad\text{(9.5)}
c(S)-B_\Phi
=\sum_{v\text{ horizontal}}
2\min(a_v,b_v)(-\chi(H_v)).
```
This proves (1)–(2), including integrality. Every term is positive when both signs occur.

Choose adjacent opposite horizontal copies $`H_0,H_1`$ in such a block. They bound a product slab $`P=H_v\times I`$ with interior disjoint from the original surface. The block has no actual boundary: an actual torus could not be used by both horizontal copies.

Annularise this pair by replacing the two horizontal faces by $`\partial H_v\times I`$, and round the corners with the incident old pieces. The two opposite coorientations face either into the slab or out of it. Thus the replacement is the other frontier of the corresponding one-sided neighbourhood of $`S\cup P`$, and has an embedded representative disjoint from the whole original $`S`$. Its actual boundary is unchanged.

Call it $`A_0`$. It need not be incompressible; Proposition 8.1 is an explicit example. Nonetheless all its pieces are old essential cut pieces or new annuli, so each assembled component has nonpositive Euler characteristic, and
```math
\qquad\text{(9.6)}
\chi_-(A_0)=c(S)+2\chi(H_v)\lt c(S).
```
Delete its whole closed components to obtain $`A`$; this does not increase complexity or remove actual boundary. Apply Lemma 9.1 with the entire incompressible original $`S`$ as barrier. The resulting $`S'`$ is an actual incompressible spanning system disjoint from $`S`$, with
```math
c(S')\le c(S)+2\chi(H_v)\le c(S)-2.
```
Its ordinary vertex differs from $`s`$ by complexity, so it gives a genuine geometric edge of $`Y`$. There is no assertion of cyclic distance one for disconnected endpoints.

Repeat. Nonnegative even $`E`$ drops by at least two; if it is positive another mixed horizontal pair exists by (9.5). The process therefore reaches $`E=0`$. The same formula bounds every incompressible vertex below by $`B_\Phi`$; compressing an arbitrary spanning surface cannot increase complexity, so the reached value is the minimum spanning complexity. This proves (4). ∎

The proof applies to the arbitrarily high-genus Part 7 family and to every balanced multi-component example of Corollary 8.2. It does not assume two boundary circles per companion component.

There is a useful conditional compatibility statement. If the chosen slab and its neighbourhood avoid an entire finite disjoint family of incompressible neighbours, then Lemma 9.1 can use that family together with $`S`$ as barrier. The lower output can be chosen disjoint from all of them. This proves compatibility **once that common slab exists**; it neither chooses such a slab simultaneously over the whole link nor makes the compression result an ordinary-class function.

### 9.3. Finitely many auxiliary fibre modes, without an anchoring assumption

There is a useful general structural reduction. It neither bounds multiplicities nor solves the essentialisation-choice problem.

**Theorem 9.3 (finite auxiliary cluster types).** Fix the genuine JSJ tree and actual boundary slopes of a non-split graph link in $`S^3`$. For an efficient essential normal representative, mark every block as horizontal, vertical, or empty. For each connected component $`C`$ of its horizontal forest:

1. its frontier slopes are prescribed by the marking: actual slopes at actual tori, and the neighbouring vertical-block fibre slopes elsewhere;
2. the compatible rational classes nonzero on every Seifert fibre lie in one one-dimensional rational cohomology subspace, with a primitive class unique up to sign;
3. this subspace has a primitive integral bundle class $`\eta_C`$, and every connected component of the cut surface in $`C`$ is a fibre $`R_C`$, with either orientation; the entire cut system is jointly parallel;
4. in particular only finitely many auxiliary primitive cluster types occur over all efficient normal representatives of all vertices.

The number of positive and negative copies of $`R_C`$, their boundary multiplicities, and their vertical return networks can still be unbounded. A marking here is a normal-form label, not a claimed complete ordinary-isotopy invariant.

**Proof.** A horizontal piece meets every torus of its block. Its neighbouring nonhorizontal block is therefore nonempty and vertical, giving the asserted fixed frontier slope. All pieces in a horizontal block have one primitive unoriented local fibre class. Across an internal horizontal edge, their nonzero boundary covectors are proportional. Rescale and orient these local classes so that their boundary restrictions agree. The horizontal incidence graph is a tree, so this constructs a compatible rational class on the whole cluster.

We prove its uniqueness, including uniqueness across different representatives with this marking. The bases of Seifert pieces embedded in $`S^3`$ are planar: positive genus would give a nonseparating embedded vertical torus, and a nonorientable base would give an embedded Klein bottle. Neither is possible in $`S^3`$. Choose an oriented fibre $`h_v`$ and boundary sections $`s_{ve}`$, with bases $`(h_v,s_{ve})`$ positive in the outward torus orientation, and rational charge $`e_v`$ such that
```math
\qquad\text{(9.7)}
\sum_e[s_{ve}]=e_v[h_v]\quad\text{in }H_1(M_v;\mathbb Q).
```
These fibre and boundary classes generate rational homology. At an internal horizontal edge $`vw`$, write
```math
\qquad\text{(9.8)}
h_w=\alpha_{ve}h_v+\beta_e s_{ve},\qquad \beta_e\ne0.
```
The reverse formula has the same coefficient $`\beta_e`$: the torus gluing reverses boundary orientation and its matrix has determinant $`-1`$. If $`k_v=\eta(h_v)`$, it follows that
```math
\eta(s_{ve})=(k_w-\alpha_{ve}k_v)/\beta_e.
```
At a frontier with prescribed slope $`u_eh_v+v_es_{ve}`$, horizontality gives $`v_e\ne0`$ and $`\eta(s_{ve})=-u_ek_v/v_e`$. Applying (9.7) yields
```math
\qquad\text{(9.9)}
A k=0,\qquad
A_{vw}=1/\beta_e,\qquad
A_{vv}=-e_v-\sum_{e\ {\rm internal}}\alpha_{ve}/\beta_e
-\sum_{e\ {\rm frontier}}u_e/v_e .
```
Thus $`A`$ is symmetric with nonzero off-diagonal entries exactly on the horizontal tree. The coefficient vector of any horizontal class is nowhere zero.

For completeness, if such a tree matrix has a nowhere-zero kernel vector $`k`$, set $`D=\mathrm{diag}(k_v)`$. Then $`DAD`$ has zero row sums and nonzero edge weights $`w_{vw}=A_{vw}k_vk_w`$. Every principal cofactor is
```math
\qquad\text{(9.10)}
(-1)^{|C|-1}\prod_{vw\in E(C)}w_{vw}\ne0.
```
One can compute this by deleting the root row of the tree incidence matrix; its determinant is $`\pm1`$. Hence $`\dim\ker A=1`$. The conclusion remains valid for one vertex, with the empty cofactor equal to one. Rational block homology and tree gluing then determine the whole rational cohomology line, proving (2).

Orient local pieces relative to the compatible class already constructed. Across every horizontal-to-horizontal trace, relative sign is preserved. A connected component $`R`$ of the cut system therefore has one sign throughout, visits every block of $`C`$, and gives a nonzero class on every $`h_v`$. Its connected dual class is primitive. The one-dimensional conclusion forces that class to be $`\eta_C`$ or $`-\eta_C`$.

The local fibre maps can be chosen with zero set exactly $`R`$ in each block. Their torus restrictions have the same nonzero degrees and coherently oriented trace circles, so monotone collar interpolation matches the maps. They give a bundle $`C\to S^1`$ with connected fibre $`R`$. Equivalently, cutting along $`R`$ glues the local interval products along spanning annuli; interval coordinates can be straightened to a global product. Two such maps in the same primitive class have a global real difference; positive interpolation along the signed Seifert fibres identifies their fibres by isotopy, with boundary allowed to move. Cutting at one fibre and using the relative product lemma gives joint parallelism of a finite disjoint system. This proves (3).

There are finitely many block markings and horizontal components. The actual slopes and adjacent vertical fibre slopes are fixed for each marking, and (2) gives at most one primitive class up to sign for each component. This proves (4). ∎

Thus the general normal data reduce to finitely many possible connected multi-boundary fibre types, signed parallel multiplicities, and embedded vertical arc systems. For the actual global class,
```math
\qquad\text{(9.11)}
\Phi|_C=(n_C^+-n_C^-)\eta_C.
```
When this restriction vanishes, arbitrary balanced multiplicities remain possible. The square-knot four-boundary example uses the same finite auxiliary mode as its two-boundary examples; the new difficulty is the gluing and essentialisation of its boundary network, rather than infinitely many new primitive fibre slopes. Relative phase integers and ordinary isotopy across different markings have not been discarded.

These auxiliary bundles classify cut pieces only. They introduce no independent deck constants into the original $`\Phi`$-cover, and they are not being substituted for that cover in a cyclic-distance or contraction argument.

**Corollary 9.4 (ordinary localisation within a fixed mode).** If two ordinarily isotopic efficient representatives have the same horizontal/vertical/empty marking, their isotopy can be chosen to preserve every JSJ torus setwise.

**Proof.** At a horizontal–horizontal edge Theorem 9.3 fixes the kernel slope. At a horizontal–vertical edge the vertical fibre fixes it. At a vertical–vertical edge the different genuine fibre slopes force empty trace; an empty block also forces empty trace at its edges. Thus all interface slopes are already the same on the two representatives. The fixed-slope product comparison of Lemma 3.1 applies to this whole collection, without a cap or anchoring premise. Its returning annuli would give forbidden boundary-parallel cut pieces, and its spanning annuli can be straightened jointly.

The bundle exception causes no additional case. If some block is vertical or empty, the class of every whole spanning component kills a $`\mathbb Z^2`$ in that block: in the vertical case choose the fibre and an infinite-order element of the planar orbifold kernel; in the empty case use a boundary torus. Such a component cannot be a whole connected spanning fibre, whose kernel is free. If every block is horizontal, actual unit usage and connectedness of the JSJ tree force the single fibre vertex of Sections 29–40. ∎

This is a localisation statement, not a complete quotient. It does not prove that two different markings cannot represent the same ordinary vertex, or erase return-endpoint stabilisers and their transported phase states. Those local boundary-motion and cross-mode questions remain part of a general carrier construction.

### 9.4. What is still missing for a contraction

No noncontractible example has been found. Theorem 1.1 is a complete enlarged subclass, not a solution for all graph links. Theorem 9.2 supplies global geometric descent, but not a finite-subcomplex deformation.

The unresolved case permits an unanchored horizontal cluster with multi-boundary pieces and vertical return networks at several ports. Adjacent opposite sheets can be annularised in more than one way, but:

1. the retained system may remain compressible, as in Proposition 8.1; Lemma 9.1 repairs an individual output but does not make its compression choices canonical;
2. different input vertices of a geometric simplex can interleave in a horizontal cluster, so a chosen adjacent pair of one vertex need not have its slab disjoint from all the others;
3. pointwise lower surfaces and the conditional barrier statement do not supply closed-star containment or a proved contractible reduction carrier over arbitrary finite links;
4. different horizontal modes can meet through empty pieces, and a sector-gluing proof needs the actual intersection complexes, not only contractibility of isolated modes.

A complete proof along this route would need either a simultaneous essentialisation theorem for these signed multi-boundary diagrams or a finite reduction carrier whose choice spaces are proved contractible. Neither is supplied here. In particular no general compression-choice theorem is assumed.

The auxiliary bundle class from Theorem 9.3 does not itself provide the missing family. In an unanchored zero-restriction cluster, different vertices can use different positive phase maps $`p_i`$ in the same auxiliary class, with transported relative port states, and signed profiles $`g_i`$. A weighted sum of $`g_i\circ p_i`$ is not proved to remain horizontal or to admit a continuous essentialisation. The one-port caps avoid this interface because their whole endpoint configuration extends in one fixed bundle. The multiport resonant star in §11.6 keeps the interface present even after its signed reflection types are classified.

The obstruction is now stronger than unbounded unsigned trace alone: even a four-sheet, genus-one balanced input has a local cancellation producing a compressible component that still carries actual boundary. The graph-manifold geometry is essential to repairing that operation; the cycle-complex reduction in a surface does not by itself do so.

For comparison, Kakimizu 1992, Theorem 2.1, already proves connectedness of the all-incompressible geometric complex for every non-split link. Its Case 2 essentialises a cut-and-paste output by McMillan moves relative to incompressible barriers. Theorem 9.2 is not a claim of new connectedness: it gives a graph-manifold complexity formula and a strictly complexity-decreasing geometric path. Przytycki–Schultens, journal version, printed p.1492, explicitly identify ordinary-class independence of the extra essentialisation as the obstacle to extending their taut-complex contraction. That statement is consistent with, and does not fill, the missing interface here.

## 10. The relative geometric complex with unused boundary tori

The branch operation below needs a relative statement about $`Y`$, not a cyclic metric on a new auxiliary manifold.

**Lemma 10.1 (unused boundary version).** Let $`N\subset S^3`$ be a compact connected union of genuine Seifert blocks and rigid fibre caps, with incompressible torus boundary divided into a nonempty actual set and an unused set $`\mathcal U`$. Prescribe the inherited primitive class $`\Phi_N`$, with actual meridian values one and $`\Phi_N|_U=0`$ for every $`U\in\mathcal U`$. Assume the capped-core conditions (C1)–(C3) with respect to its actual boundaries. If there is a reduced incompressible spanning system with these actual boundaries, class $`\Phi_N`$, and no boundary on $`\mathcal U`$, its relative geometric complex $`Y_N`$ is contractible by the same direct finite-subcomplex construction.

**Proof.** A block adjacent to an unused torus cannot be in the nonzero-fibre forest, since its fibre evaluation there would be nonzero. Its core pieces are therefore vertical by (C1), and its unused ordinary base circles have no endpoints. The anchored horizontal clusters and one-boundary cap pieces are exactly those of §2. No cap-to-cap assembly can be retained, and every retained arc still has distinct endpoints with an actual or anchored end. The unused circles are marked holes, not filled disks.

The ordinary comparison and distinct-end detectors retain these unused holes. All maps are chosen constant in their collars. Hence every generic averaged level misses the unused tori. The finite zero-core band templates, positive cluster maps and cap factor maps are constructed as in §4, using one $`\Phi_N`$-cover. Its deck group is $`\mathbb Z`$ because of an actual meridian of value one.

Closed-component deletion remains harmless for homology without using a complete actual-meridian basis: every closed oriented surface in the interior of $`N\subset S^3`$ separates $`N`$, so its relative class is zero. Essential assembly proves incompressibility of every retained level. The unused zero-degree collars add only finitely many exceptional phase values. Initial disjoint-family carriers, retained-state rereading and finite-support continuity are precisely the proofs of §5. They nullhomotope every finite inclusion and give contractibility of $`Y_N`$. ∎

Only this relative geometric conclusion is asserted. The $`X\subseteq Y`$ retraction is used for the eventual whole $`S^3`$ link exterior, not presumed for a partial factor.

[Overview](../README.md) · [Previous page](part10.md) · [Next page](part10-3.md)
