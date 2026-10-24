# Part 7. Anchored clusters, iterated cables and the general comparison (continued)

[Overview](../README.md) · [Previous page](part7.md) · Part 7, page 2 of 2

## 8. A composing-space obstruction with unbounded genus

This proves Proposition C and gives a qualitatively different internal boundary-free example.

### 8.1. The tree and the two possible modes

For $`C=T(2,3)\#\overline{T(2,3)}`$,

```math
Q=R\cup_{T_+\sqcup T_-}(Q_+\sqcup Q_-),
\qquad R=S^1_\mu\times\Sigma_{0,3},
```

with $`\mu=\mu_+=\mu_-`$ and $`\lambda_C=\lambda_++\lambda_-`$ in composing-space homology. Leaf fibres are $`h_+=\lambda_++6\mu`$, $`h_-=\lambda_--6\mu`$. Add the double-parallel pattern $`P=S^1_{\lambda_C}\times\Sigma_{0,3}`$ along $`T_0`$. All three companion blocks are boundary-free and $`\Phi|_Q=0`$.

The four-block tree has three genuine cuts: the fibres at $`T_0`$ are $`\lambda_C,\mu`$, and at the leaves $`\mu,h_\pm`$, each pair intersecting once. All pieces have injected boundary and are irreducible. The actual construction is in $`S^3`$, and the link is non-split.

For a connected positive-genus spanning surface, the pattern cannot pair its actual ends, which would already give the annulus. Thus it reaches $`T_0`$ with slope $`\lambda_C`$. Composing pieces are horizontal. For a primitive positive piece write

```math
\eta(\mu)=d>0,\qquad \eta(\lambda_+)=a,\qquad
\eta(\lambda_-)=-a,\qquad \gcd(d,a)=1.
```

A horizontal torus-knot leaf component has coherent boundary on its sole torus. Its meridional homology coefficient must vanish, so its slope is longitude. A vertical piece has slope $`h_\pm`$.

If both leaves are horizontal then $`a=0,d=1`$. Each composing piece joins one fibre from each leaf and has one outer boundary: it is a square-knot spanning fibre. Pattern returns would make closed components, leaving only the disconnected capped vertex.

If both leaves are vertical their kernels require $`a+6d=0`$ and $`-a-6d=0`$. Thus $`d=1,a=-6`$. A mixed choice requires $`a=0=-6d`$, impossible. Every connected nonannular vertex consequently has sections of

```math
\qquad\text{(8.1)}\eta=(1,-6,+6)
\quad\text{on }(\mu,\lambda_+,\lambda_-).
```

Each is a pair of pants with one boundary on every port. Since total companion class vanishes, there are $`2r`$ sections with equal sign counts. All other pieces are annuli; thus $`\chi=-2r`$ and the connected two-boundary surface has genus $`r`$.

Every total-minimum representative therefore has vector (1.1) and total minimum $`6r`$. To minimise $`T_0`$ alone, first take its essential cuts and then put the companion pieces into internal essential form relative to their fixed $`T_0`$ boundary. The same two-mode argument does not change that boundary count; its capped mode is disconnected. Thus the individual outer minimum is $`2r`$. No assertion about independent minimisation of each other torus is needed.

### 8.2. Explicit essential assemblies for every $`r`$

Take $`2r`$ sections of (8.1), indexed in cyclic phase order by $`\mathbb Z/(2r)`$, with signs

```math
\qquad\text{(8.2)}\epsilon_i=
\begin{cases}
+1,&i=0\text{ or }r\lt i\lt 2r,\\ 
-1,&1\le i\le r.
\end{cases}
```

This is cyclic word $`+^r-^r`$, up to starting point. On a leaf port the auxiliary phase has degree one transverse to its fibre, so these are its marked fibre positions too.

At **each** leaf pair positions by

```math
\qquad\text{(8.3)}i\longleftrightarrow1-i\pmod{2r}.
```

These $`r`$ pairs are nested noncrossing return arcs in the disk with two cones. Put one cone in each endcap region. Every arc separates the cones, giving essential vertical annuli. Every pair has opposite signs.

In the pattern use $`r-1`$ returning annuli paired by

```math
\qquad\text{(8.4)}i\longleftrightarrow-i\pmod{2r},
\qquad1\le i\le r-1.
```

The two actual holes occupy opposite endcap regions. Positions $`0,r`$ reach the positive and negative actual holes. All pattern returns are essential and all signs match.

The leaf and pattern involutions give the chain

```math
0,\ 1,\ 2r-1,\ 2,\ 2r-2,\ 3,\ldots,\ r
```

through all section vertices, stopping when $`r`$ first appears. The second leaf adds the same edges. Every piece reaches the actual tethers, so the surface is connected and has no closed component.

All pieces are essential. For a leaf return, the two end regions contain the two cone points, of orders two and three; its fibre core is infinite and it cannot be a boundary-parallel annulus. For a pattern return, each end region contains an actual hole, so it too is not boundary-parallel. Hatcher Lemma 1.11 excludes boundary compressions of these incompressible annuli. The composing sections are bundle fibres.

Minimise a hypothetical compression disk against the incompressible JSJ tori. An outermost arc gives a piece boundary compression; a boundary-parallel surface arc is first pushed away. A disk missing all tori gives a piece compression. Neither is possible. This essential-assembly argument permits cycles in the surface incidence graph. The local complements are disconnected: the composing sections give $`2r`$ product chambers, and each leaf return system gives $`r+1`$ chambers. Only the whole spanning complement is connected, by the actual-meridian argument.

The $`2r`$ pants give $`\chi=-2r`$, proving genus $`r`$. Genus distinguishes the ordinary classes; §8.1 gives the efficient trace counts. Proposition C follows.

### 8.3. Precise failure of the net-demand extension

All companion restrictions and net port demands vanish, yet the fixed link has arbitrarily many positive/negative horizontal sections, arbitrarily many essential same-port returns, and connected essential assemblies with actual boundary. Ordinary isotopy preserves the genus and outer minimum trace.

The zero-block carrier of Sections 29–40 would assign capacity zero to these ports and discard every such piece. Keeping the primitive auxiliary class alone does not repair this: (8.1) is fixed for every $`r`$. In the capped vertex leaf slope is longitude; in these vertices it is $`h_\pm`$, with the same zero total class. Slope information is lost as well.

There is no global-$`\Phi`$ positive horizontal phase here: $`\Phi_R=0`$, while (8.1) is nonzero and the signed sheets use both flow signs. Applying Lemma 34.1 with that auxiliary class would change the covering class. Independent sheet deck constants violate the definition of $`D`$.

These are exact failures of the proposed reduction, not proof that a more elaborate signed carrier cannot exist.

### 8.4. Nonzero restrictions alone do not force coherence

There is a smaller independent obstruction to omitting (A2). Take three zero-framed parallels of a trefoil, oriented $`(+,+,-)`$. The four-holed product pattern has nonzero restriction and fibre evaluation zero. The boundary-free companion has restriction $`\psi`$, the primitive trefoil knot class, and fibre evaluation six. Thus (A1) holds at both blocks; its only horizontal cluster has no actual boundary.

Pair the first positive actual hole to the negative hole by one vertical annulus and attach the remaining positive hole to one companion fibre. This gives an incompressible spanning system of complexity one and two components. Alternatively attach all three actual holes to three companion fibres of signs $`(+,+,-)`$. This has complexity three and three components and is incompressible by the same collar/group-injection argument as §6.

Both have the same nonzero companion restriction $`\psi`$. The second has an extra positive-negative fibre pair and is not norm-minimising. Its minimum outer trace is three: each labelled one-actual-boundary component restricts to $`+\psi`$ or $`-\psi`$, hence must enter the companion, and the displayed longitudinal construction attains one curve per component. The first has minimum trace one. Yet $`\mathrm{div}(\Phi|_T)=1`$ throughout.

This proves that the role of (A2) is substantive even when no block has zero total restriction. It is not a counterexample to contractibility, nor is the complete complex of this three-parallel link classified here.

## 9. A component-wall retraction, independent of JSJ slices

This proves Theorem D. The unknot and the fibred case have one vertex by the product/connectivity argument of Lemma 2.4. Otherwise all spanning components are essential, the exterior is irreducible and boundary-incompressible, and the following printed inputs apply.

### 9.1. Source range and parallel packets

Sakuma's terminology on printed p.863 defines a Seifert surface as oriented, without closed components, with the given link boundary; it does not require connectedness. Equivalence is ordinary isotopy in the exterior. On printed p.883 Proposition 4.9(1) says that pairwise geometric edges give a simultaneous simplex for $`IS(L)`$, and (2) says that the unlabelled embedded union of disjoint representatives has isotopy type determined by that simplex. These are used as literature inputs in their stated all-incompressible, non-split range. No connectedness qualification is added or removed.

We cite Banks from arXiv:1109.0965v1, 5 September 2011. Its §10 explicitly extends Proposition 4.10 to all incompressible surfaces. In these citations Sakuma's geometric $`IS`$ is our $`Y`$, while Banks' Definition 10.1 is our cyclic $`X`$. We use the printed minimum-position extension as input 2.3, not a claimed new proof of the noncompact Sakuma interface behind PS.

A component of a spanning system uses a nonempty subset $`I`$ of actual tori. Its oriented relative class is determined by this subset: its meridian values are one on $`I`$ and zero elsewhere. In particular two ordinarily isotopic components have the same actual set and orientation.

**Packet lemma.** In a disjoint finite spanning family, the product between two isotopic component occurrences contains only occurrences of that same component class.

**Proof.** Such a proper product exists by the ordinary incompressible product-region theorem, Banks Proposition 4.2(1), printed p. 5; by Remark 4.4, p. 6, the second boundary-coincidence degeneration cannot occur for two distinct copies, whose boundaries are disjoint, and the first (self-coincidence) degeneration is the cyclic product; the exceptional cyclic product would make that component a whole bundle fibre and has already been separated as the fibred case. If $`C\times I`$ is the product, a different disjoint proper component entering its interior must lie entirely there, since its interior cannot exit through the horizontal faces or the actual boundary.

Its nonempty actual set $`J`$ is contained in $`I`$. Its boundary, projected to $`C`$, is the sum of the boundary circles indexed by $`J`$, with the prescribed orientations. In a connected orientable surface the only relation among all its boundary classes is their total sum. Thus this sum can vanish only if $`J=I`$. Equivalently, a vertical cut disk joining an included to an excluded boundary would have one boundary intersection, impossible.

An incompressible system in $`C\times I`$ using each vertical boundary annulus once is a horizontal slice: cut $`C`$ by proper arcs to a disk, remove innermost circle intersections with the product disks, and use their forced single spanning traces. The remaining surface in a ball is the one horizontal disk, by incompressibility. This is the product proof of Lemma 2.4, before its connectivity step. Therefore the component is isotopic to $`C`$. ∎

All occurrences of one component class consequently form a parallel packet with no other component class between them. The only cyclic packet would fill the exterior by a bundle with that fibre, already separated above. Successively collapse each packet to one cooriented wall, allowing coincident components; these moves avoid all walls of other classes. Restoring parallel copies preserves every input ordinary class. Each input contains at most one occurrence of a packet, since it uses its actual tori only once.

Sakuma's unlabelled-union uniqueness now suffices also for the weighted construction below. An ambient isotopy can permute occurrences only within one ordinary component class. Collapsing that packet assigns it the sum of their weights, which is independent of those permutations. No stronger labelled-union uniqueness is assumed.

### 9.2. The weighted wall construction

Let $`\sigma=\{v_0,\ldots,v_m\}`$ be a genuine geometric simplex. Choose its disjoint whole representatives and collapse the parallel packets. Denote the distinct component walls by $`C`$. For each $`v_i`$, take a Thom band map $`f_i:M\to\mathbb R/\mathbb Z`$, equal to zero off its wall bands, with jump one across each of its walls. Use the same transverse band profile on a shared wall. Thus, on the band of a wall $`C`$, every chosen real lift has the local form $`n_i+[C\subset v_i]\,\beta_C`$, with an integer constant $`n_i`$, the indicator of whether $`C`$ belongs to $`v_i`$, and one common transverse function $`\beta_C`$ increasing from 0 to 1; a level therefore never selects different fragments at different places along a wall. Each $`f_i`$ represents $`\Phi`$; its phase $`1/2`$ represents $`v_i`$.

On the one global $`\Phi`$-cover choose real equivariant lifts $`F_i`$. For $`x=\sum_i\lambda_i[v_i]`$ put

```math
\qquad\text{(9.1)}F_x=\sum_i\lambda_iF_i,\qquad
w_C(x)=\sum_{i:\ C\subset v_i}\lambda_i .
```

This still has deck displacement one. A wall band has total jump $`w_C\in[0,1]`$, and off the bands $`F_x`$ is constant on each chamber. A generic phase level is therefore a union of **entire parallel component walls**, not a cut-and-paste surface requiring compression.

On every actual torus the oriented bands are monotone in its meridian direction, and their total jump is $`\sum_i\lambda_i=1`$. A generic phase uses that torus exactly once. Every selected component is incompressible, has actual boundary and has the prescribed orientation. Thus each generic level is an actual reduced incompressible spanning surface.

Let $`v_r(x)`$ be its ordinary vertex, and define the finite phase average

```math
\qquad\text{(9.2)}\mathcal R_\sigma(x)=\int_{\mathbb R/\mathbb Z}[v_r(x)]\,dr .
```

There are only finitely many component subsets and exceptional chamber phases. The integral means their phase-interval lengths as barycentric coefficients. A change of lift adds one real constant to $`F_x`$, rotating the integration variable. Changing band profiles does not change these lengths: they are determined by the off-band chamber phases and the monotone jumps. Splitting or reordering a parallel packet changes only which isotopic copy is selected within the same phase interval; its total jump and the actual selected class are unchanged.

By §9.1, changing the simultaneous representatives does not change (9.2). Deleting an input with zero coefficient deletes its unsupported walls and merges equal-phase chambers. Thus the constructions agree on all common faces.

Two generic levels of the same map have cyclic distance at most one. In a complete block cut along one level, its real lift avoids that phase plus all integers and hence lies in a single interval of length one. The other level has at most one intermediate integer-translated phase there, giving at most two consecutive complete-block indices. Width zero would force one reduced whole surface into the other; actual usage once and absence of closed components then force equality. Distinct output vertices consequently form a clique of $`X`$. Thus $`\mathcal R_\sigma(x)\in|X|`$.

Choose the output phases also to avoid the finitely many values of $`F_x`$ on the original component walls. The outputs and all the input vertices then have simultaneous disjoint whole representatives, by restoring sufficiently close parallel input copies in their packets. This gives a genuine $`Y`$-carrier for the segment joining $`x`$ to $`\mathcal R_\sigma(x)`$.

### 9.3. Inclusion and exact recovery

For a cyclic edge choose almost transverse simplified minimum representatives by input 2.3. At a transverse intersection of noncoincident components, the difference potential has local values $`c,c+1,c,c-1`$, of range two. Width one therefore permits only coincident or disjoint components. Separating the coincident components gives a geometric edge. Sakuma Proposition 4.9(1) then makes every cyclic clique a simultaneous geometric simplex. Hence $`X\subseteq Y`$ simplicially.

For a cyclic simplex take its collapsed representative family. A product region between distinct disjoint components has empty collapsed locus; its horizontal faces have boundary only on the actual boundary and hence are whole components. Those would be parallel occurrences, already identified. A self-product on an identified component either makes that component a relative boundary, contradicting its actual meridian value one, or is the cyclic bundle exception already separated. Thus each almost disjoint pair has simplified intersection, and its width is its class minimum by input 2.3.

Fix one common chamber and integral reference lifts. On the finite common chamber set let $`u_i`$ be the integral potential of $`v_i-v_0`$, with all root values zero. Every pair satisfies

```math
\qquad\text{(9.3)}\mathrm{osc}(u_i-u_j)\le1.
```

The root-zero condition implies pointwise comparability. Relative to their pointwise minimum, the distinct vectors are nested zero-one vectors. For a generic level $`r\in(0,1)`$, band postcomposition as in §4.4 reads its full potential as

```math
\qquad\text{(9.4)}\left\lfloor\sum_i\lambda_i u_i+1-r\right\rfloor .
```

Common floor rounding of a nested zero-one chain returns each $`u_i`$ for exactly its barycentric weight. An integral vector determines the selected walls, since its jumps relative to the reference determine their oriented current; coincident packets have already been merged. Thus (9.2) returns exactly $`x`$, as an actual ordinary vertex combination. This proves exact recovery on every simplex of $`X`$, not just preservation of an average homology class.

### 9.4. Strong deformation and its limitation

The face-compatible maps (9.2) define $`\mathcal R:|Y|\to|X|`$. On a fixed closed simplex, finitely many chamber phases, affine in the coefficients, give continuous piecewise linear interval lengths and only finitely many output classes. Its carrier is actual by §9.2. Therefore

```math
\qquad\text{(9.5)}\mathcal H_D(x,t)=(1-t)x+t\mathcal R(x)
```

stays in $`Y`$, starts at the identity, ends in $`X`$, and fixes $`X`$ by §9.3. The image of every closed simplex cylinder lies in a fixed finite subcomplex, with continuous barycentric coordinates; the ordinary CW cylinder criterion gives continuity on $`|Y|\times I`$. This proves Theorem D.

This construction starts with one **geometric simplex** of disjoint inputs. It does not supply a contraction for an arbitrary finite subcomplex, whose vertex representatives can intersect. Convex band maps of such a family can have nonessential levels or closed components; §9 gives no canonical class-preserving reduction for them. In particular it does not contract the unbounded genus family of Proposition C.

## 10. What this part leaves open

Theorem A derives coherence from link conditions; Theorem B handles another noncoherent family by direct complete classification. Neither covers all graph links.

The remaining interfaces for a signed JSJ contraction are:

1. **Ordinary quotient:** a joint signed normal form with returning arcs, variable primitive auxiliary classes, phase words and boundary-motion stabilisers. Lemma 2.1 provides local types, not that global quotient.
2. **Canonical signed distance:** global simplified minimum position is supplied by the explicit Banks all-incompressible input. But no reduction of prescribed signed JSJ data through changing sheets and return packets has been proved to preserve that minimum and yield a canonical symbolic formula. No signed trace depth is asserted to equal $`\delta`$.
3. **Contraction carrier:** a carrier for arbitrary finite families must retain unbounded cancelled multiplicity, exclude closed/inessential assemblies and recover actual classes on input simplices. The positivity, finite capacities and circle deletion of Sections 29–40 do not establish this for Proposition C. The disjoint-simplex comparison with $`Y`$ is separately closed by Theorem D.

Theorem D shows that $`X`$ and $`Y`$ have the same homotopy type for every non-split link. Thus their general graph-manifold contractibility remains one problem, despite the completed strong deformation comparison. This part contains no noncontractible example. Parts 8–12 treat further cancelling families.

## 11. Dependencies and diagnostics

The diagnostic `scripts/part7_checks.py` verifies exact finite data:

| Check | Extent / result |
|---|---|
| Six-block splice | 5 gluing equations, genuine fibres, (A1)–(A2), local divisibility 2, norm 24, genus 9 |
| Boundary-free four-port support, demand 4 | 2,144 rational decoder points; 1,296 exact edge recoveries |
| Single-cable arithmetic, either sign | 1,760 parameter cases |
| Named cable links | genera 2,7; leaf traces 4,6 |
| Three cable stages | genus 20; deep trace 24 |
| Square-knot construction | $`1\le r\le256`$; 98,432 oriented internal annulus occurrences; signs, noncrossing, connectedness and Euler numbers |
| Unanchored three-parallel control | nonzero restriction, signed multiplicities 1 and 3, complexities 1 and 3 |
| Component-wall comparison on an actual $`Y`$-tetrahedron | 969 rational points; 2,907 global-root checks; 4,845 strong-deformation checks |

The cable vertex counts printed by the program refer to proved Theorem B, not computational surface enumeration. Likewise the interpretation of the square-knot trace as efficient uses §8.1, not a graph search.

The nonunit support is realised by a boundary-free negative Hopf centre with four positive Hopf leaves of actual sums $`(4,-4,4,-4)`$. Its central four-cycle flows are $`(x,4-x,x,4-x)`$, $`0\le x\le4`$. The decoder test is therefore attached to an actual anchored link. It checks a fixed support, not the whole vertex set.

The component-wall test uses the [balanced $`T(8,12)`$ two-lens example](double-cone-example.md). Its four whole surfaces form a geometric tetrahedron, while $`X`$ has the two triangles of the potential square. Direct phase-interval integration is compared with floor decoding from each of three global chamber roots. The component marginals, exact recovery on $`X`$, geometric containment, endpoints and constancy of the retraction along the deformation are checked with exact rational arithmetic. This finite example does not prove the printed union-uniqueness input or Theorem D. Independent review implementations are listed in the [diagnostic guide](../scripts/README.md).

| Input | Use and boundary |
|---|---|
| Hatcher Lemma 1.11, Proposition 1.12, horizontal product, printed pp.20–23 | essential cuts, signed Lemma 2.1, cable longitude induction |
| Sections 31–38, repaired Lemma 31.2 | only after §3 proves all structural/tautness hypotheses |
| Part 6, Lemmas 3.1, 3.3 and §§5–6 | longitudinal base, product lemma, compatible phases and direct whole-block distance |
| Lemma 2.4 / Kakimizu connectivity | spanning-fibre uniqueness in §5 |
| Banks arXiv:1109.0965v1 Proposition 4.2(1), Remark 4.4, Proposition 4.10 and explicit §10 extension | product regions; all-incompressible global minimum position, input 2.3 |
| Sakuma 1994 Proposition 4.9(1)–(2), printed p.883; definitions pp.863,871–872 | geometric flagness and unlabelled simultaneous-union uniqueness, used explicitly in §9 |
| Essential assembly and amalgam normal form | existence/incompressibility of displayed surfaces |
| CW finite-image criterion and Whitehead, as in Section 38 | Theorem A contraction and ordinary-product strong deformation |

Finite diagnostics do not replace the proofs or certify novelty.

[Overview](../README.md) · [Previous page](part7.md)
