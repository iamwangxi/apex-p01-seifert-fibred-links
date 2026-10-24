# Part 10. Rigid caps and Seifert-support parallels (continued)

[Overview](../README.md) · [Previous page](part10-2.md) · Part 10, page 3 of 3

## 11. Empty-interface products and balanced Seifert-support parallels

This gives a second complete subclass, with a boundary-free zero-restriction block internal to the actual JSJ tree. Such a block is not a one-port cap.

### 11.1. A direct geometric product lemma

Let $`\mathcal Z`$ be a separating incompressible torus collection in the actual exterior. Suppose every finite simultaneous disjoint spanning family can be efficiently normalised disjoint from $`\mathcal Z`$. Write the resulting components containing actual boundary as $`M_1,\ldots,M_a`$. Define $`Y_i`$ using reduced incompressible systems in $`M_i`$ with the prescribed actual boundary and no boundary on the unused cut tori. All of their components must reach actual boundary. The inherited class vanishes on each unused torus.

**Lemma 11.1 (empty-interface product).** Under these conditions the ordinary vertices of $`Y`$ are tuples of ordinary vertices of the $`Y_i`$. A finite set of tuples is a geometric simplex exactly when each coordinate set is a simplex of its $`Y_i`$, allowing repeated coordinate vertices. If each $`Y_i`$ is contractible, then $`Y`$ is contractible by a direct finite-subcomplex homotopy. Hence $`X`$ is contractible by the retraction of Part 7, Theorem D.

**Proof.** A compression disk for a system missing $`\mathcal Z`$ can be made disjoint from those incompressible tori by innermost-circle disk exchanges. Thus the union is incompressible exactly when its pieces are incompressible. Pieces in an actual-free component would be whole closed components and are absent.

Ordinary comparison also localises. Both systems have empty trace on $`\mathcal Z`$. In a relative product region a torus of $`\mathcal Z`$ would therefore have no boundary traces; if it met the region it would be a whole torus. Its injected $`\mathbb Z^2`$ cannot factor through the free group of the product face. Hence the product pushes miss these tori. The bundle exception is excluded because each component class kills the injected $`\mathbb Z^2`$ of a missed torus; the case $`\mathcal Z=\varnothing`$ is just one factor. Conversely an isotopy of factor surfaces can be supported away from the unused tori: its compact surface track misses them, and relative isotopy extension fixes small collars there. These factor isotopies therefore glue without matching nonempty port motions. This proves the claimed ordinary factorisation.

The assumed simultaneous normalisation gives the forward simplex implication. Conversely choose simultaneous representatives in every factor. If several tuples have the same coordinate vertex, replace that representative by enough close whole parallel copies. Their unions then give simultaneous whole disjoint representatives of the tuples. This proves the reverse implication.

Here is the direct contraction argument; no infinite-product topology identification is needed. For a finite subcomplex $`K\subseteq Y`$, take its finite coordinate images $`K_i`$. For
$`x=\sum_v\lambda_v[v]`$, let $`p_i(x)`$ be its marginal probability distribution in coordinate $`i`$. Choose nullhomotopies $`h_i:|K_i|\times I\to|Y_i|`$ of the finite coordinate inclusions, each ending at a fixed vertex. Their images lie in finite subcomplexes, by compactness in the CW realisations.

Let $`Q(x,t)`$ be the product distribution with marginals $`h_i(p_i(x),t)`$:
```math
\qquad\text{(11.1)}
Q(x,t)_{(w_1,\ldots,w_a)}
=\prod_{i=1}^{a}h_i(p_i(x),t)_{w_i}.
```
At any parameter the support in each coordinate is a simplex. The full Cartesian product of these supports is therefore a simplex of $`Y`$. The coefficients in (11.1) are continuous and have finite total support on the finite cylinder. At $`t=0`$, its support together with the input support lies in the same product simplex. The straight segment from $`x`$ to $`Q(x,0)`$ is consequently carried by $`Y`$. At $`t=1`$ the distribution is one fixed tuple. This nullhomotopes the finite inclusion. The same finite-CW/Whitehead argument as §5 proves contractibility. ∎

This is a geometric coupling of factor homotopies. No cyclic-width comparison or independent deck normalisation for a whole spanning surface is asserted.

### 11.2. A nondegenerate Seifert support forces the centre empty

Let $`K=K_1\cup\cdots\cup K_n`$ be a non-split Seifert link whose exterior $`E_0`$ is a genuine Seifert piece with negative orbifold Euler characteristic. Use preferred meridians and longitudes, and put
```math
\qquad\text{(11.2)}
\Lambda_{ii}=0,\qquad \Lambda_{ij}=\mathrm{lk}(K_i,K_j)\ (i\ne j).
```
Assume $`\det\Lambda\ne0`$, and that the regular fibre of $`E_0`$ is not the preferred-longitude slope on any boundary torus.

Replace each $`K_i`$, inside its actual zero-framed tubular neighbourhood, by $`2m_i`$ zero-framed parallels, $`m_i`$ in each orientation, where $`m_i\ge1`$. Denote the resulting actual $`S^3`$ link by $`L`$. Its pattern block $`V_i`$ is $`P_{2m_i+1}\times S^1`$, with outer fibre slope $`\lambda_i`$. All these outer cuts are genuine by the fibre-slope assumption.

**Theorem 11.2 (balanced parallels of a nondegenerate Seifert support).** For every such $`L`$, $`Y(L)`$ is contractible, and hence so is $`X(L)`$, with the strong deformation retraction. If every $`m_i=1`$, both complexes consist of exactly one vertex.

**Proof.** The oriented winding sum of each pattern is zero. Hence $`\Phi|_{E_0}=0`$. On $`V_i`$, however, $`\Phi\ne0`$ because it takes values $`+1,-1`$ on the actual local meridians; its fibre evaluation is zero. The signed local lemma therefore forces all pieces in $`V_i`$ to be vertical. Every nonempty outer trace has slope $`\lambda_i`$.

If the central piece were horizontal, it would meet every boundary torus. A connected horizontal primitive dual $`\eta`$ would satisfy $`\eta(\lambda_i)=0`$ for all $`i`$. But
```math
\qquad\text{(11.3)}
[\lambda_i]=\sum_{j\ne i}\Lambda_{ij}[\mu_j]
\quad\text{in }H_1(E_0;\mathbb Q).
```
The meridians generate that homology. Nonsingularity of $`\Lambda`$ therefore forces $`\eta=0`$, contradicting horizontality. A central vertical piece would have the central regular-fibre slope at its boundary, incompatible with every $`\lambda_i`$. Thus the central piece has empty boundary trace. A surface remaining inside it would be a whole closed component, forbidden here, so the centre is empty.

This argument applies also to each member of any efficiently cut disjoint family. All outer interfaces are universally empty in the sense of Lemma 11.1. Irreducibility and injected boundary in the Seifert and pattern pieces also prove that the resulting actual link is non-split.

Each relative factor $`Y(V_i)`$ is contractible by the zero-core part of the direct circle-map proof: take canonical bands for the oriented actual-to-actual arc systems in $`P_{2m_i+1}`$, keep the unused outer boundary constant, use one common lift and average with a fixed base map. Every generic actual boundary has one endpoint. The unused outer boundary has none. After whole closed circles are deleted, every remaining level arc therefore joins two distinct actual boundaries and is essential. The initial carrier consists of the original disjoint arc bands, and finite templates give continuity exactly as in §§4–5. No horizontal or cap extension is needed in this factor. The class is primitive at its actual meridians; its restriction to the unused outer torus is zero by the balanced winding condition.

Lemma 11.1 now gives a direct contraction of the whole $`Y`$. If $`m_i=1`$, the factor base is a pants surface and its only possible system is its single actual-to-actual seam. Its ordinary class is unique with actual boundary allowed to move and the unused outer torus preserved. Thus every factor, and the whole $`Y`$, has one vertex. The same vertex set makes $`X`$ a point too. ∎

This result assumes neither coherent central traces nor an actual boundary in the centre. It derives empty trace from the homology calculation.

### 11.3. Explicit internal empty blocks and further gluing

Take $`K`$ to be $`n\ge3`$ regular Hopf fibres. Then
```math
\qquad\text{(11.4)}
\Lambda=J-I,\qquad \det\Lambda=(-1)^{n-1}(n-1)\ne0,
```
and the central fibre on the $`i`$-th boundary is $`\lambda_i+\mu_i`$. The centre has base an $`n`$-holed sphere. After balanced replacement it is a boundary-free, zero-restriction internal JSJ block, joined to $`n`$ actual pattern blocks. Theorem 11.2 applies for arbitrary $`m_i`$. With $`m_i=1`$, the actual $`2n`$-component link has $`X=Y`$ a point. This is outside Theorem 1.1: the central zero-restriction block has $`n`$ ports and cannot be a one-port cap.

More generally $`n\ge2`$ regular $`T(p,q)`$ fibres have common pairwise linking $`\ell=pq\ne0`$, giving
```math
\qquad\text{(11.5)}
\det\Lambda=\ell^n(-1)^{n-1}(n-1).
```
Their central fibre differs from each preferred longitude by $`\ell\mu_i`$, so the same conclusion holds. Another three-block example uses the axis and $`T(2,3)`$ braid in a solid torus, whose linking is two. The central exterior is an annulus-base Seifert piece with one cone; its two fibre-to-longitude intersections are two and six. Opposite two-parallel replacement on each component gives four actual components, an internal actual-free empty block, and $`X=Y`$ a point.

The product argument extends the class beyond parallel patterns. Suppose an actual $`S^3`$ graph link has the same central Seifert support with $`\Phi|_{E_0}=0`$, and each attached branch has an outer Seifert block with nonzero total restriction, zero fibre evaluation, and fibre slope $`\lambda_i`$. If its relative geometric complex, with the outer torus unused, is contractible, the proof of (11.3) still forces the centre empty and Lemma 11.1 contracts the whole $`Y`$.

In particular the branch can satisfy Lemma 10.1: allow additional unused zero-restriction boundary tori in its zero cores, keep their maps constant, and use the same hypotheses on its active core and rigid caps. Thus the capped-core class and empty-central-product operation can be iterated in actual realisations satisfying these hypotheses. No arbitrary splice-matrix realisation is being asserted.

The general gate is still unpassed. This additional complete class removes one kind of internal zero block; it does not essentialise the resonant multi-boundary cancellation modes of §8.

### 11.4. A finite exclusion certificate for multi-block supports

The same parallel-pattern conclusion has a finite sufficient test for arbitrary graph-link supports.

**Corollary 11.3 (no-horizontal-mode support certificate).** Let $`K`$ be a non-split graph link with genuine JSJ blocks. Assume the outer block fibre at each $`K_i`$ is not $`\lambda_i`$. For each nonempty connected subtree $`C`$ of its JSJ tree, form the boundary-value matrix of (9.9), prescribing $`\lambda_i`$ at every support boundary in $`C`$, and the neighbouring Seifert fibre at every cut frontier. If none of these matrices has a nowhere-zero kernel vector, then arbitrary balanced zero-framed parallel replacement of every $`K_i`$ has contractible $`Y`$ and $`X`$. If there is one positive and one negative parallel per $`K_i`$, both are a point.

**Proof.** Every pattern block is vertical by the same nonzero-restriction, zero-fibre-evaluation argument. If any support block were horizontal, take a connected component $`C`$ of the support horizontal forest. Its boundary values are exactly those used in the test, and Theorem 9.3 supplies a nowhere-zero kernel vector, a contradiction. Thus every support block is vertical or empty. At internal genuine support edges, two vertical fibre slopes differ; at every outer edge, the support fibre differs from $`\lambda_i`$. Every trace is therefore empty. Any surface left wholly in the support would be a closed component. The support is empty, and Lemma 11.1 and the relative pattern contractions from Theorem 11.2 prove the conclusion. ∎

This is a finite test over connected block subsets, using rational linear algebra. It is sufficient, not necessary: a rejected algebraic mode need not have a globally realisable return network. A singular tree matrix of nullity greater than one cannot have a nowhere-zero kernel vector by (9.10); a one-dimensional kernel can be checked directly. No enumeration of infinitely many unsigned multiplicities is hidden in this test.

For an explicit two-block support, cable one component of three regular Hopf fibres by any $`(p,q)`$, $`p\ge2`$, $`q\ne0`$, $`\gcd(p,q)=1`$. The support pieces are the remaining Hopf pants $`H`$ and the cable space $`W`$. Their fibre intersection is $`|p-q|\ne0`$; outer fibre-to-longitude intersections are $`pq\ne0`$ on the cable component and one on the other two. There are exactly three connected subsets to test:

* For $`C=H`$, write $`x=\eta(\mu_{\rm old}),y=\eta(\mu_2),z=\eta(\mu_3)`$. The two outer longitude conditions give $`y=z=-x`$. The cable-fibre frontier gives $`(q-2p)x=0`$, hence $`\eta=0`$, since coprimality excludes $`q=2p`$.
* For $`C=W`$, outer longitude gives $`\eta(\lambda_{\rm old})=0`$. The Hopf-fibre frontier is $`\lambda_{\rm old}+\mu_{\rm old}`$, with $`\mu_{\rm old}=p\mu_{\rm cable}`$. It forces $`\eta(\mu_{\rm cable})=0`$.
* For $`C=H\cup W`$, the support linking matrix has off-diagonal entries $`p,p,1`$, so its determinant is $`2p^2\ne0`$, and the three preferred-longitude conditions force the whole class to vanish.

Thus this whole two-block support family passes the certificate, for either cabling sign. Its balanced parallel replacements have two adjacent boundary-free, zero-restriction internal support blocks and three actual pattern branches. With one opposite pair at each branch, these are actual six-component, five-block $`S^3`$ graph links with $`X=Y`$ a point. Arbitrary larger balanced pattern counts still have the direct product contraction.

### 11.5. All Seifert supports

The explicit linking-matrix condition in Theorem 11.2 is automatic when no port fibre is a longitude. Together with fibre-matching amalgamation this removes the support restriction within the Seifert case.

**Corollary 11.4 (balanced parallel replacement of a Seifert link).** Let $`K`$ be a non-split link with Seifert-fibred exterior, other than the unknot. Replace every component by any positive even number of zero-framed parallels with equally many of each orientation. The resulting actual non-split graph link has contractible $`Y`$ and $`X`$, proved by the direct constructions above.

**Proof.** First suppose the Seifert exterior is genuine and $`n\ge2`$. Write its consistently oriented fibre in boundary and exterior homology as
```math
\qquad\text{(11.6)}
h|_{T_i}=r_i\mu_i+s_i\lambda_i,\qquad
[h]=\sum_j r_j[\mu_j].
```
The second formula follows from the first because $`\lambda_i`$ has no $`\mu_i`$ coefficient. For $`i\ne j`$ comparison gives
```math
\qquad\text{(11.7)}
r_j=s_i\Lambda_{ij}.
```
If no fibre is longitudinal, every $`r_i\ne0`$. Equation (11.7) forces every $`s_i\ne0`$, and symmetry of $`\Lambda`$ gives one common nonzero value $`c=r_is_i`$. Therefore
```math
\qquad\text{(11.8)}
\Lambda=c^{-1}\mathrm{diag}(r_i)(J-I)\mathrm{diag}(r_i),
\qquad
\det\Lambda=
\frac{\prod_i r_i^2}{c^n}(-1)^{n-1}(n-1)\ne0.
```
Theorem 11.2 applies.

If some $`r_i=0`$, its pattern fibre is the same unoriented slope as the support fibre. Merge every such pattern into the support Seifert block. The merged block now contains actual boundary, has nonzero total restriction and zero fibre evaluation. Every remaining pattern block also has actual boundary, nonzero restriction and zero fibre evaluation; their remaining interfaces have different fibre slopes. This is the no-cap, all-actual-block case of Theorem 1.1, with its direct $`Y`$ contraction. The merged base remains of negative orbifold Euler characteristic. No zero-restriction support block is left as an unproved piece.

For a one-component genuine Seifert support, the knot is a nontrivial torus knot. Its balanced parallel replacement is the rigid-cap case of Theorem 1.1. The Hopf-link exterior is a redundant $`T^2\times I`$ collar: remove it to obtain the two pattern blocks, both with actual boundary, and use the same no-cap case. The excluded unknot would instead give a split zero-parallel unlink. In all remaining cases irreducible pieces glued along injected genuine boundary show non-splittability. ∎

This corollary does not make the analogous assertion for every graph-link support: the resonant multi-boundary cluster networks in that larger class remain the outstanding case.

### 11.6. Nondegenerate general slopes, and a concrete resonant star

The empty-centre argument has a reusable slope form. Suppose an actual graph-link exterior is a Seifert support $`E_0`$, with $`\Phi|_{E_0}=0`$, and attached branches whose outer blocks are vertical because their restrictions are nonzero with zero fibre evaluation. Let their outer fibre slopes in support coordinates be
$`\ell_i=r_i\mu_i+s_i\lambda_i`$. Suppose each relative branch $`Y_i`$, with outer torus unused, is contractible, and no $`\ell_i`$ is the central fibre slope.

**Corollary 11.5 (nondegenerate Seifert gluing).** If
```math
\qquad\text{(11.9)}
\det B\ne0,\qquad B_{ij}=r_i\delta_{ij}+s_i\Lambda_{ij},
```
then the centre is universally empty and $`Y`$, hence $`X`$, is contractible.

**Proof.** A central horizontal dual would satisfy $`\eta(\ell_i)=0`$, or $`B(\eta(\mu_j))_j=0`$, contradicting (11.9). Central vertical traces cannot match the branch fibres. Thus all cuts are empty; Lemma 11.1 applies. The relative capped-core constructions described in §11.3 give one explicit family of allowed branches. This argument presupposes the stated actual $`S^3`$ realisation, not an arbitrary abstract gluing. ∎

The zero determinant is not merely a technical gap in this exclusion argument. It permits actual essential cancellation modes with unbounded genus in a small fixed link.

**Proposition 11.6 (a resonant six-component star).** Take three regular Hopf fibres as support. In each of their solid-torus neighbourhoods use two oppositely oriented parallel regular fibres of slope $`\lambda_i-2\mu_i`$, rather than zero-framed parallels. This is an actual non-split six-component $`S^3`$ graph link with four genuine JSJ blocks. Its central restriction is zero and all leaf restrictions are nonzero with fibre evaluation zero. It has infinitely many incompressible spanning vertices: for every $`t\ge1`$ one has two components of genera $`3t-1,3t`$, with four and two actual boundaries respectively.

**Proof.** Each leaf is a pants product, embedded as the two-fibre pattern with framing $`-2`$. Its outer fibre is $`\ell_i=\lambda_i-2\mu_i`$. The central fibre is $`\lambda_i+\mu_i`$, so each interface fibre intersection is three and is genuine. Opposite oriented winding makes $`\Phi=0`$ on the whole central block. Each leaf still has its two actual local meridians of values $`+1,-1`$. Irreducibility with injected boundary proves non-splittability.

Here $`\Lambda=J-I`$ and $`B=J-3I`$. It has kernel generated by $`(1,1,1)`$. The primitive central auxiliary class $`\eta(\mu_i)=1`$ has fibre evaluation three. Its connected fibre $`R`$ therefore has $`\chi(R)=-3`$. At each port its restriction is $`(\eta(\mu_i),\eta(\lambda_i))=(1,2)`$, so the port degree is one. It follows that $`R`$ has three boundary components and genus one. This is an auxiliary bundle only; the actual $`\Phi`$ is still zero there.

Put $`r=2t`$ and take $`2r`$ parallel copies of $`R`$, cyclically labelled $`j\in\mathbb Z/(2r)`$. At leaves zero and two take actual tethers at $`0,r`$ and return reflection $`P_0(j)=-j`$ on the other positions. At leaf one take actual tethers at $`1,r+1`$ and return reflection $`P_1(j)=2-j`$. These are the embedded pants return systems, with the two fixed positions as the actual ends.

The union of the $`P_0,P_1`$ edges has exactly two components, the even and odd positions. Indeed $`P_1P_0`$ is translation by two. Each parity component is a path with $`r`$ vertices: its only defects are $`0,r`$, or $`1,r+1`$, respectively. Its length $`r-1`$ is odd. Orient the fibre at positions $`0,1`$ positively, and propagate opposite signs across every return edge. This is consistent, makes positions $`r,r+1`$ negative, and also orients the third leaf system $`P_0`$ correctly.

Repeating the $`P_0`$ edges at the third leaf changes no connectivity. The even component has the four actual ends at leaves zero and two; the odd component has the two actual ends at leaf one. Neither is closed. Each contains $`r`$ copies of $`R`$, so each has Euler characteristic $`-3r`$. Their genera are
```math
\qquad\text{(11.10)}
\frac{3r-2}{2}=3t-1,\qquad \frac{3r}{2}=3t .
```
All horizontal fibres, actual-to-port seams and essential returning annuli are essential cut pieces. Essential assembly proves that these are actual incompressible spanning systems. Their distinct total complexities $`6r=12t`$ distinguish their ordinary vertices. ∎

Each leaf has $`r-1`$ port-to-itself returns with no actual end. With its two actual tethers these cut the pants base into $`r=2t`$ disks. Thus disconnected local complements and actual-free returning arcs occur in this same explicit family.

The same link also has the three-annulus spanning vertex. Theorem 9.2 gives pointwise descending paths from all the displayed vertices. No contraction of their full neighbourhoods is proved here. Proposition 11.6 is an explicit remaining test, not a noncontractibility counterexample. It shows that replacing the nondegeneracy condition by “the centre has total class zero” would discard actual multi-boundary cancellation modes.

The signed reflection data of this test admit a further complete finite statement.

**Lemma 11.7 (two positive tether axes).** Let $`\epsilon_j\in\{1,-1\}`$, $`j\in\mathbb Z/(2r)`$. Call $`a`$ a positive tether axis if
```math
\qquad\text{(11.11)}
\epsilon_a=1,\quad\epsilon_{a+r}=-1,\qquad
\epsilon_{2a-j}=-\epsilon_j\quad (j\ne a,a+r).
```
There are at most two such $`a`$. For a reduced horizontal normal diagram of the star in Proposition 11.6 with $`2r`$ central fibres:

* if $`r=1`$, all three leaves use the same positive axis;
* if $`r>1`$, after a common cyclic relabelling the three axes use exactly $`0,d`$, both occurring, with
```math
\qquad\text{(11.12)}
\gcd(d,r)=1,\qquad d+r\text{ odd}.
```
Conversely these choices give essential reduced diagrams with a unique compatible sign word. They have exactly two whole components. For odd $`r`$, both have three actual boundaries and genus $`(3r-1)/2`$. For even $`r`$, their actual boundary counts are four and two, and their genera are $`3r/2-1,3r/2`$.

These are normal-diagram statements; relative phase integers and the geometric adjacency of ordinary vertices are not classified by this lemma.

**Proof.** Put $`z=\exp(\pi i/r)`$ and $`E(z)=\sum_j\epsilon_jz^j`$. Equation (11.11) gives
```math
\qquad\text{(11.13)}
E(z)+z^{2a}\overline{E(z)}=4z^a,\qquad
\mathrm{Re}(z^{-a}E(z))=2.
```
The points $`z^a`$ are distinct on the unit circle. A line meets this circle in at most two points, proving the first assertion.

At each leaf of an actual diagram, both actual boundaries must be tethered to the centre: an actual-to-actual seam would intersect every essential port return, leaving no way to meet the nonempty horizontal trace. The remaining essential pants returns are parallel. Each has one end in each of the two port intervals between the actual tethers, so their reflection has fixed positions $`a_i,a_i+r`$, with opposite actual signs. Thus all three axes satisfy (11.11). If $`r>1`$ and they are all the same, every nonfixed reflection pair closes into a whole component with no actual boundary. Reducedness excludes this. Hence exactly two axes occur; set them equal to $`0,d`$.

If $`g=\gcd(d,r)>1`$, all actual defects have residue zero modulo $`g`$, and the reflection orbit of any nonzero residue cannot reach one. It gives a whole closed component. Thus $`g=1`$. The two reflections generate translation by $`2d`$, so their vertex orbits are the two parity classes, each with $`r`$ vertices. Their edge graphs are paths with $`r-1`$ edges and two defect endpoints. For even $`r`$, coprimality forces $`d`$ odd and both endpoints of either path are the positive and negative defects of one axis; the odd path length gives the required sign reversal. For odd $`r`$, the path length is even, so its endpoints must have the same sign. This is precisely $`d`$ even. These are (11.12).

Conversely the same path argument uniquely propagates compatible signs from the two positive defects whenever (11.12) holds. For even $`r`$ each path has equal numbers of signs; for odd $`r`$ the two oppositely seeded paths have cancelling imbalances. Thus the total signed multiplicity is zero as required by $`\Phi|_C=0`$. Repeating either reflection at the third leaf changes no connectivity. Every parity component reaches actual boundary. For odd $`r`$ each leaf contributes one actual boundary to each component; for even $`r`$, one reflection is used twice and the other once, giving four and two actual ends. Each component contains $`r`$ copies of the genus-one three-boundary fibre, hence has Euler characteristic $`-3r`$. The asserted genera follow. All the prescribed returns and tethers embed as essential pants systems, so essential assembly proves the converse realisation. The $`r=1`$ case is immediate. ∎

## 12. Sources, tests and exact limits

| Input | Use |
|---|---|
| Part 7, Theorems A, B and D | primitive signed local structure; longitudinally rigid caps; positive anchored cluster interfaces; the final implication from $`Y`$ to $`X`$ |
| Sections 31–38 | ordinary distinct-end arc detection; relative positive phases; absolute boundary constants; finite-template continuity with rereading after deletion |
| Banks arXiv:1109.0965v1 Proposition 4.2 and Remarks 4.3–4.4 | torus-preserving fixed-slope product comparison |
| Hatcher's three-manifold notes: Lemma 1.11 (boundary incompressibility), Proposition 1.12 (vertical/horizontal classification), the following horizontal-product discussion, and Proposition 1.14 (essentiality of horizontal and admissible vertical pieces) | essential cuts and classification; essential assembly across tori is proved in the text by the outermost-arc argument |
| Hatcher 2008, second proof, printed pp.5–6 | method of extending circle maps and reducing their levels; no three-dimensional incompressibility theorem is attributed to it |
| Kakimizu 1992, Theorem 2.1, Case 2; Przytycki–Schultens 2012, printed p.1492 | known all-incompressible connectivity and the exact essentialisation-choice limitation; neither is used as an all-genus contraction theorem |
| Part 8, §13 | actual four-parallel test configuration; not a dependency of Theorem 1.1 |

The tree and recursive-companion conclusions of Part 8 are not used in the new contraction.

The diagnostic `scripts/part10_checks.py` gives the following exact finite results:

| Diagnostic | Extent |
|---|---:|
| One-boundary cap endpoint grammar | 46,232 occurrence-labelled pairings |
| Signed cap-circle parameter choices / regular sectors | 455 / 1,398 |
| Composing-cap framing lists / nonresonant lists / mixed-chirality nonresonant lists | 11,110 / 5,706 / 4,146 |
| Resonant two-boundary witness modes | 7,366 |
| Positive recursive constructions / subsequent negative-cable certificates | 72 / 72 |
| Unbounded-family relabellings | $`1\le r\le256`$ |
| Balanced multi-component tests | $`1\le m\le128`$ |
| Horizontal excess identities / strict mixed-pair cases | 1,638 / 1,274 |
| Actual nonunit support, repeated-word simplex test | 11 nonempty simplices |
| Its barycentric points / common-root checks / contraction checks | 289 / 867 / 1,445 |
| Signed auxiliary-tree matrices / all-root cofactors | 1,449 / 7,389 |
| Nondegenerate Seifert support matrices / two-block cable certificates | 66 / 354 |
| Regular/exceptional support fibre-homology identities | 64 |
| Empty-interface product probability parameters | 495 |
| Resonant six-component-star parameters | $`1\le t\le64`$ |
| Balanced sign words for the two-axis lemma | 8,788, with $`1\le r\le8`$ |
| Coprime two-axis normal parameters | 3,388, with $`2\le r\le64`$ |

The actual nonunit-support check independently compares its degree-two port word condition with common rounding of $`(0,x,-y)`$. It retains the cap's signed zero demand and the multiplicity-two port-to-cap packet. It does not promote a common graph to an unrestricted geometric simplex.

Finite checks do not prove ordinary isotopy, compression-disk existence, parameter continuity, or contractibility; those are the arguments above. The checker is not a normal-surface enumerator and does not claim to cover arbitrary graph-link input. Contractibility for all graph-manifold links is not proved in this part.

[Overview](../README.md) · [Previous page](part10-2.md)
