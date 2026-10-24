# Part 12. Framed recursive parallels and weighted supports (continued)

[Overview](../README.md) · [Previous page](part12.md) · [Next page](part12-3.md) · Part 12, page 2 of 3

## 6. Proof of Theorem A and the one-port replacement interface

Let $`\mathcal A`$ be the pattern-annular subcomplex, with the companion port unused. It is contractible by the relative annular matching argument. It is nonempty exactly in the balanced case considered here.

Fix an ordinary $`F`$ from §5.3. It is essential, separating, of positive genus, with $`2k`$ boundaries on the single port. Every finite disjoint family in its class is jointly parallel, its complement incidence is linear, and its ordinary port-loop image is zero. Thus the **one-port** instance of Part 9, Theorem 11.2 applies. For $`v=1`$, its two-boundary instance Theorem 11.1 already suffices.

Here are the interfaces checked under the framing change.

| Packet proof input | Present framed setting |
|---|---|
| One actual pattern product | The $`n`$-hole disk product, with fibre $`\delta_f`$ |
| Actual unit boundary and pattern class | Values $`\varepsilon_i`$, independent of the chosen framing coordinates |
| Invisible one-port companion | $`\Phi\vert _Q=0`$ in the balanced case |
| Essential separating positive-genus fixed piece | §§4–5 |
| Joint linear packet | The point/gap proof (4.5), including $`v=1`$ |
| Ordinary zero port loops | Equation (5.1) and Lemma D |
| Known interface slope in ordinary comparison | $`\delta_f`$, of meridian intersection one |
| One original deck coordinate | The spanning $`\Phi`$-cover, with inherited absolute constants |

The parent uses a fixed end and one side of the original surface, resolves the corresponding chamber, and closes under enabled empty-disk repairs. Original chamber boundary-piece sets are disjoint. The barrier excludes other traces from every repair disk. Enabling is monotone, so the closure and its retained subpacket are ordinary. It changes only the original actual-bearing component containing the seed; whole closed components are deleted only at the end. Essential assembly proves the retained output incompressible.

None of these statements uses that $`\delta_f`$ is a preferred longitude. They use precisely the checked inputs in the table. The parent decreases the number of $`F`$-pieces and gives a cyclic edge by the shared-component argument. Its comparison retains one whole $`\Phi`$-block; it does not assign a separate deck shift to a terminal or to a negative sheet.

For finite cyclic simplices, the rooted component-wall construction orders restored coloured occurrences. Merge complete parent-event lists in that order. Each event is at an empty end of the current full family. The affine-height prism slabs therefore have genuine simultaneous geometric carriers and agree on common faces. The CW-cylinder argument gives the sector retraction. The component-wall retraction restricts to the sector; the bounded-count conclusion uses the coefficient-removal correction, not a false assertion that every phase output stays below the bound.

The full balanced $`Y`$ is the union of these sectors and $`\mathcal A`$. A nonannular simplex has only one ordinary $`F`$-label. Distinct sectors meet exactly in $`\mathcal A`$. Their contractions agree there, so the same CW sector-gluing argument as Part 9 contracts the full $`Y`$. This handles many modes without averaging maps from different auxiliary circles.

For $`f=0`$, Part 9, Theorem 1.9 applies directly. For $`s=1`$, the companion is one torus-knot exterior. If $`f=p_1q_1`$, the fibres match and the manifold is Seifert, covered by the Seifert result. If $`f\notin\{0,p_1q_1\}`$, neither horizontal longitude nor vertical fibre can meet the prescribed trace, so the companion is empty and the relative annular complex contracts. The $`f=0`$ case is already included in Part 9 or the rigid-cap theorem.

Finally let $`a=\sum\varepsilon_i\ne0`$. When $`f\ne0`$, the pattern fibre evaluation is $`fa`$; the composing and terminal fibre evaluations are respectively $`a`$ and $`s_i a`$. All are nonzero. The anchored horizontal classification therefore gives the single fibre vertex. The zero-framing case is Part 9, Theorem 1.9. This proves Theorem A in every orientation and framing case. The Part 7, Theorem D gives $`X`$ contractible and $` |Y|\searrow |X| `$. No general link theorem from the competition paper is invoked. ∎

### 6.1. Recursive graph knots and weighted frontier packets

The restriction to torus-sum companions can be removed. Define a recursive graph knot to be any knot obtained from nontrivial torus knots by finitely many connected sums and cables $`C_{p,q}`$, where $`p\ge2`$, $`q\ne0`$, and $`\gcd(p,q)=1`$. Signs and their order are unrestricted. Flatten adjacent composing nodes before using the genuine JSJ tree. All other interfaces in this recursive description are genuine: the cable-to-child fibre intersection cannot vanish by coprimality. This is an explicit class of actual knots, rather than a claim about arbitrary abstract splice matrices.

**Theorem G (framed recursive graph-knot parallels).** Theorem A holds with $`K`$ any recursive graph knot. In particular all actual counts, all orientations, all integer framings, arbitrarily nested sum/cable resonance modes, and their higher-degree invisible frontiers are included.

The reusable interface in its proof is the following.

**Lemma G′ (weighted rooted-cluster replacement).** Work in the actual decomposition $`M=P\cup_T Q`$, where all actual boundary lies in the disk-with-$`n`$-holes product $`P`$, its spanning slopes are its regular fibre, actual signs balance, and the one-port knot companion $`Q`$ is invisible to the original spanning class. Suppose $`Q`$ has the following efficient normal description at the fixed integral root slope:

1. Each nonvertical nonempty mode has a connected horizontal cluster $`C`$, fibred by a connected $`R`$ with $`\chi(R)\lt 0`$, exactly one root boundary, and primitive class $`\eta(\mu_{\rm root})=1`$.
2. Every cancellation mode has one or more frontier tori $`T_i`$, with positive degrees $`b_i`$, at its other boundaries. Each neighbour is a genuine Seifert block carrying only essential same-port vertical returns, and every finite efficient return system there is **jointly parallel**. Its other boundary tori, if any, are unused. Its ordinary peripheral family is malnormal modulo its central fibre. Joint parallelism is a separate geometric hypothesis; malnormality alone does not imply it.
3. A simultaneous efficient disjoint family has one such mode. Pure whole-companion fibres, if present, constitute a separate one-boundary fibre mode.

Then every cancellation family in a fixed ordinary connected companion class is a joint linear packet of essential separating positive-genus surfaces and has zero ordinary root-loop image. Consequently the **one-port** fixed-packet contraction applies to every such sector. Distinct ordinary companion sectors can be glued along their common pattern-annular subcomplex. No assumption $`b_i=1`$, no tether and no locally connected complement is needed.

**Proof: weighted point and gap orbits.** Put $`N`$ signed copies of $`R`$ around its phase circle. On $`T_i`$ the circular word is the $`b_i`$-fold repetition of their $`N`$ labels. A perfect essential-return matching in the adjacent block is
```math
j\longmapsto c_i-j\pmod{Nb_i},\qquad c_i\text{ odd}.
\qquad\text{(6.1)}
```
It pairs opposite signs and therefore makes $`N`$ even. Its action on sheet labels is the reflection $`c_i-j\bmod N`$, with $`b_i`$ parallel incidences for each paired sheet. Put
```math
g=\gcd\bigl(N,\{c_i-c_{i_0}\}_i\bigr),\qquad q_0=g/2,\quad k=N/g .
\qquad\text{(6.2)}
```
The sheet orbits give exactly $`q_0`$ connected pieces, each using $`2k`$ copies of $`R`$, with $`2k`$ root boundaries. The orbits are bipartite, and every piece has equally many positive and negative sheets. Its Euler characteristic and genus are
```math
\chi(F)=2k\chi(R),\qquad
g(F)=1-k(1+\chi(R))\ge1 .
\qquad\text{(6.3)}
```
Its dual class vanishes on the meridian generator of $`H_1(Q)`$; hence each connected $`F`$ is separating.

The local expanded gap reflection is $`c_i-1-j\bmod Nb_i`$; it descends to $`c_i-1-j\bmod N`$. Thus the global sheet/gap incidence is the quotient of an alternating cycle by these dihedral reflections. It is an interval, with $`q_0`$ sheet orbits and $`q_0+1`$ gap orbits. Every terminal end chamber maps to one of its two end gap orbits: a local fixed gap reduces to a fixed class for the common reflection modulo $`g`$. An interior gap orbit therefore uses only $`R\times I`$ pieces and vertical rectangles. They glue to an interval bundle with its two horizontal boundaries the two different complete adjacent $`F`$'s. It is their product. This proves joint parallelism and the linear complement incidence.

When $`b_i`$ is even, both terminal end chambers may project to the same global end. The other end region may have interval-bundle topology. We do **not** assert that the two ends contain terminal caps of the same kind, or use that assertion in the product proof. Only interior gaps must be actual products.

**Proof: the ordinary root-loop detector.** Work in the actual Bass–Serre tree of $`C`$ and its neighbouring vertical blocks, retaining their groups. Let $`H=\pi_1(F)`$. The induced graph of groups has sheet groups $`\pi_1(R)`$, annulus groups equal to the relevant central-fibre cyclic groups, and boundary-circle edge groups.

At a sheet vertex, the $`b_i`$ different boundary occurrences at $`T_i`$ represent distinct double cosets
```math
\ker\eta\backslash\pi_1(C)/\pi_1(T_i)
\ \cong\ \mathbb Z/b_i\mathbb Z .
\qquad\text{(6.4)}
```
Different occurrences cannot fold. Within one occurrence the injection follows from $`\pi_1(R)\cap\pi_1(T_i)`$ being exactly its primitive boundary-circle subgroup. At a return annulus, essentiality means its ends are distinct peripheral cosets, so there is no fold there either. Thus the induced Bass–Serre tree embeds in the ambient tree. It is the minimal $`H`$-tree: the sheet group is noncyclic and each boundary subgroup is proper; collapsing the degree-two annulus vertices gives the usual reduced graph of noncyclic surface groups. An annulus vertex has exactly two incident edges in this minimal tree.

Choose $`d=\mu_{\rm root}`$ in the reference cluster group, with $`\eta(d)=1`$. Suppose $`d^\ell`$ normalises $`H`$. It fixes the reference cluster vertex and preserves the minimal tree. A finite power preserves a chosen edge orbit in its finite quotient by $`H`$. Hence there are $`m>0`$ and $`h\in H\cap\pi_1(C)=\pi_1(R)`$ such that
```math
t=h^{-1}d^{m\ell}
```
fixes the chosen edge and its vertical endpoint. It normalises $`H`$, so the valence-two property makes it fix the other incident edge there. Peripheral malnormality modulo the central fibre implies that $`t`$ lies in that central fibre, which is the annulus subgroup of $`H`$. Consequently $`d^{m\ell}=ht`$ belongs to $`H\cap\pi_1(C)=\ker\eta`$. Applying $`\eta`$ gives $`\ell=0`$.

An ordinary loop, after a finite power, fixes a chosen boundary occurrence. Its boundary track is $`d^\ell`$ times a tangential power of the root slope, already in $`H`$. The preceding normaliser argument therefore gives zero transverse winding. Finite powers also eliminate permutations of the unmarked packet. This argument does not require $`d`$ itself to lie in a chosen frontier torus; that would fail when $`b_i>1`$.

The ordinary fixed-slope localisation, configuration quotient and whole-component test are now exactly those of §5.3. The hypotheses of Part 9, Theorem 11.2 with **one** companion port have all been checked. Its relative closure and coloured prisms therefore give the sector contraction, including the induced cyclic sector. Joint normalisation and the product conclusion show that a nonannular simplex has one ordinary connected companion label. Different labels meet only in the annular subcomplex, where their contractions agree. A pure one-boundary fibre sector, when present, contracts there by the cap-phase argument. This proves the lemma. ∎

### 6.2. Verification of the weighted interface under sum/cable recursion

The finite boundary-slope envelope of Part 10, Theorem 1.3 is
```math
\mathcal S(T(p,q))=\{0,pq\},\quad
\mathcal S(C_{p,q}(J))=\{pq\}\cup p^2\mathcal S(J),\quad
\mathcal S(\#J_i)=\sum_i\mathcal S(J_i).
\qquad\text{(6.5)}
```
It is a necessary finite envelope, not an assertion of exact spectra. In particular every finite essential boundary slope of a recursive graph knot is integral. This remains true for incoherently oriented boundary: the essential-cut proof of that theorem did not assume a sign-coherent whole system.

We prove the stronger root-cluster statement by induction. In a composing block, put $`\eta(\mu)=a>0`$. A child trace has finite integral slope $`t_i`$, so
```math
\eta(\lambda_i)=-t_i a,\qquad f=\sum_i t_i .
\qquad\text{(6.6)}
```
Primitivity forces $`a=1`$. The section has one root boundary and one boundary at each child. Attaching a horizontal child cluster with one root boundary does not join different sections. Vertical child roots become frontier caps.

In a horizontal cable block $`W=C_{p,q}(J)`$, use the integral homology basis $`(\mu_C,\lambda_J)`$. The peripheral relations and a finite inner slope $`t`$ give
```math
\mu_J=p\mu_C,\quad \lambda_C=p\lambda_J,\quad
\eta(\mu_C)=a,\quad\eta(\lambda_J)=-pt\,a,\quad f=p^2t.
\qquad\text{(6.7)}
```
Primitivity forces $`a=1`$. Thus its fibre has one root boundary, $`p`$ inner boundaries, and
```math
\chi(R_W)=-(p-1)|q-pt| .
\qquad\text{(6.8)}
```
The integer $`q-pt`$ is nonzero by coprimality. If the child is horizontal, attach its $`p`$ fibre copies to those $`p`$ boundaries. The resulting cluster remains connected with one root boundary, and its inherited frontier degrees are multiplied by $`p`$. If the child root is vertical, the new frontier has degree $`p`$.

A vertical cable root has outer slope $`pq`$, and inner fibre slope $`q/p`$. Since $`q/p`$ is not integral, (6.5) forbids any inner trace. Its cut pieces are therefore same-outer-port essential returns, with the entire child unused. A vertical torus-knot root has the familiar disk-with-two-cones returns. These are the only vertical roots: the composing fibre has meridional slope, excluded by the finite root slope.

There is no independent surface hidden below an unused edge, since it would be a whole closed component. Consequently each nonvertical mode consists of exactly the root horizontal cluster and these one-port vertical caps. Their orbifold bases are respectively a disk with two cones or an annulus with one cone. There are exactly two features away from the active port; an essential wave separates them, and disjoint such waves are parallel. Thus the required cap-return parallelism is proved here. Lemma B separately gives peripheral malnormality. Formulae (6.6)–(6.8) give one root boundary and arbitrary positive frontier degrees, often products of several cabling windings. Every genuine horizontal cluster has negative Euler characteristic. Simultaneous efficient normalisation forces a single mode: all horizontal sheets meet every incident port, and intersecting horizontal/vertical slopes cannot coexist there.

This proves every hypothesis of Lemma G′. It also proves there are finitely many normal modes, although the later ordinary labels retain all unbounded twist data rather than identifying them by these finite modes.

**Completion of Theorem G.** First $`n=1`$ is the graph knot itself; its spanning class is nonzero on every Seifert fibre, so actual unit usage forces the single whole fibre.

Suppose $`n>1`$ and the actual signed total is nonzero. For $`f\ne0`$, the pattern fibre and every companion block fibre have nonzero evaluation. The anchored argument gives a single global fibre vertex. For $`f=0`$, every companion cut is a one-boundary knot fibre, with signs individually retained. The cap-phase contraction applies to that restricted fibre class; no assertion of longitudinal rigidity against other zero-class modes is needed, because the nonzero companion class already excludes them.

For balanced signs, the pattern is vertical and $`\Phi|_Q=0`$. A nonempty root trace is the fixed finite slope $`f`$. If the root is horizontal, §§6.1–6.2 apply. The no-cap mode is precisely the whole graph-knot fibre, possible only at $`f=0`$; the cap-phase contraction handles it alongside the cancellation sectors. Distinct modes cannot coexist unless their connected ordinary cuts agree, in which case they already have the same ordinary sector label.

If the root is vertical, it is a torus-knot or cable root with matching framing. Amalgamate the pattern with that Seifert block. In the cable case its child is universally unused by the nonintegral inner-slope argument. The remaining actual-bearing Seifert core has nonzero class, zero fibre evaluation and any such unused boundary kept constant. Part 10, Lemma 10.1 contracts its relative $`Y`$; the empty-interface product adds no factor. The torus-knot case is the Seifert result. If no companion mode exists at all, only the pattern-annular complex remains.

All balanced sectors therefore glue along the same contractible annular subcomplex by their relative contractions. This proves $`Y`$ contractible in every case. Apply Part 7, Theorem D to the actual whole link to obtain $`X`$ contractible and $` |Y|\searrow |X| `$. No independent cyclic shift has been introduced at any cable frontier. ∎

### 6.3. One global separating packet seen at several actual patterns

There is a second replacement interface. Unlike the several-port branches of Part 9, Theorems 11.1–11.2, which are vacuous in $`S^3`$ by Part 9, Remark 11.3, it has actual $`S^3`$ examples. Its decomposition has **one invisible region with several boundary tori**, and a different actual pattern at each torus:
```math
M=Q\ \cup_{\bigsqcup_{j=1}^m T_j}\ \bigsqcup_{j=1}^m P_j,\qquad
P_j=S^1\times B_j .
\qquad\text{(6.9)}
```
Here $`B_j`$ is a disk with an even positive number of actual holes and one companion boundary. All actual spanning slopes are the displayed fibres, signs balance separately at each $`P_j`$, $`\Phi|_Q=0`$, and $`\partial Q=\bigsqcup_jT_j`$. The tori are incompressible and the whole is the stipulated actual non-split $`S^3`$ link exterior.

**Theorem I (common-packet contraction at several actual patterns).** Fix an essential connected separating $`F\subset Q`$ with $`\chi(F)\lt 0`$, and with $`2k_j>0`$ boundaries of the prescribed slope at every $`T_j`$. Suppose every finite disjoint system in its unoriented ordinary class is jointly parallel, and every ordinary loop of such a system has zero transverse configuration winding at every $`T_j`$.

Let $`Y_F`$ be the full geometric subcomplex whose $`Q`$ cuts are empty or arbitrary individually signed copies of $`F`$, and whose pattern cuts are essential vertical annuli. Then $`Y_F`$ is contractible relative to its pure pattern-annular subcomplex $`\mathcal A`$. Its induced cyclic subcomplex has the corresponding strong deformation retraction onto the annular cyclic subcomplex. Several such sectors can be glued along $`\mathcal A`$, provided a simultaneous nonempty family has only one ordinary connected $`Q`$-label.

The crucial hypothesis is **one common packet at all ports**. This is neither independent packets at different ports nor an arbitrary multiport horizontal cluster. Planar $`F`$'s with at least four boundaries are allowed; annuli are not included. The proof below uses negative Euler characteristic for the additive piece count, essentiality for assembly, and the stated packet and motion hypotheses. It does not use positive genus.

**Proof: global chambers and ordinary data.** Write the common packet $`F_0,\ldots,F_{q-1}`$ in a fixed reference order, with signs $`w_i`$. Its complementary regions in $`Q`$ form an interval. For a chosen normal side, the one-sided original chambers are the first end when its face has that side, the last end with that side, and an intervening product exactly when both its complete boundary faces have that side. Their sets of **whole $`F_i`$'s** are disjoint.

At $`T_j`$, each such global chamber has its collection of annular boundary caps. A chamber seen at two or more ports is selected **once**. Its operation removes its whole boundary pieces and applies all these caps at all ports together. The operations have disjoint endpoint sets and commute. Applying them on the chosen side gives the raw system disjoint from the original, with exactly its actual boundary. The retained $`Q`$ cuts are a subpacket of small push-offs. Pattern paths are composed separately inside each $`B_j`$; whole closed components with retained $`F`$-pieces are not deleted until closure stops.

Fixed-slope ordinary comparison applies to the complete $`T_j`$ collection. A component missing any actual torus cannot be a whole spanning fibre; a component carrying every actual boundary kills the injected $`Q`$ torus under the balanced class. Thus the usual spanning-bundle exception introduces no lost gluing. Zero loop images at all ports and the pattern peripheral detector retain the same ordered packet, cap matchings and transported configuration states during ordinary comparison. These statements do not assign independent deck coordinates to the ports.

For fixed local ordinary data, the transverse gluing states form a torsor over $`\mathbb Z^m`$: this is the fundamental group of the product of the unparametrised trace-configuration circles. Both side loop images are zero. In particular a sign-word period is not an additional quotient. Tangential motion in the common trace slope is absorbed by a pattern fibre collar and contributes no extra annular framing. These are ordinary boundary-motion integers; the original spanning cover still has just one common deck generator.

**Proof: every repair is a global chamber, and the closure is confluent.** A new inessential return at port $`j`$ cuts off an empty disk in $`B_j`$. No original essential pattern arc can enter that disk. Hence its two trace points lie in one gap of the original $`T_j`$ trace configuration. If that gap is inside one boundary-occurrence band of $`F`$, it lies between two consecutive original packet pieces. If it crosses between bands, it lies at an end of the packet. Its two negative or two positive pushed faces therefore identify exactly one unselected one-sided **global** product or end chamber.

This argument remains valid when the same chamber has another appearance at another port. Selecting it removes the same complete boundary pieces everywhere; all its local cap operations are part of that one selection. This identification is the step absent from an independent portwise argument.

Enabling is monotone. If chamber $`G`$ has an empty-return witness and another chamber $`G'`$ is selected, their whole boundary-piece sets are disjoint. The witness is a completed pattern path between surviving endpoints of $`G`$; caps at the other endpoints cannot alter it or its empty-disk class. Start with the fixed first end, on its actual normal side, and add enabled global chambers. The finite monotone process has a unique least closed result.

At its end there is no inessential pattern return. All retained cuts are essential copies of $`F`$ and essential vertical annuli. Essential assembly proves incompressibility. Delete the whole closed components now. Actual boundary was preserved and the number of $`F`$-pieces has strictly decreased. Only the original actual-bearing component containing the seed changes: each enabled product has a witnessing path joining its two pieces in that already changed component, and an unchanged original component still has essential unchanged pattern cuts. This is the same whole-component argument used for the one-port cyclic parent.

All tests and retained identities are ordinary invariants by the preceding comparison. The piece count is the component-additive ordinary integer $`q(S)=\chi(S)/\chi(F)`$, since all pattern pieces are annuli. It strictly decreases.

For completeness the cyclic-edge argument needs no genus hypothesis. Only one original connected actual-bearing component $`C`$ has been replaced. On the geometric edge to the output, Part 7's component-wall construction retains the common other components. A reduced generic output must choose either $`C`$, which already uses its entire actual subset, or all of its replacement components together. No mixed choice uses that actual subset once. Their phase measures are the two original coefficients, read on any of those actual meridians. Thus the Part 7 retraction is the identity on this edge, which already lies in $`X`$. We have an ordinary cyclic parent with a definite retained subpacket and a lower piece count, including planar negative-Euler companions.

**Proof: the relative family barrier uses all-port visibility.** Suppose the seed is first in the entire common packet of a simultaneous family. Its end chamber is empty of the others at every port. At a later repair, its empty disk at $`T_j`$ excludes every other family's essential pattern arc and port trace. Any other $`F`$-piece inside the proposed global product or end chamber would have a boundary occurrence in this same $`T_j`$ gap, because **every $`F`$ meets every port**. That is impossible. The whole repair chamber is therefore empty of the family, rather than only its local appearance at $`T_j`$. The parent is relatively compatible with the family, preserving the positions of retained pieces.

Pure annular family members have no $`Q`$-trace; their essential pattern arcs also miss the same empty disks. This covers the annular part of the relative statement.

**Proof: one order and one original cyclic cover give the prisms.** For a cyclic simplex, restore coloured occurrences by the Part 7 component-wall exact-recovery family, rooted in the chosen **global end chamber of $`Q`$**. Its restriction to the nested common $`F`$-packet gives a linear coloured order, compatible with all faces. At any occurrence its endpoints are
```math
\sum_i t_i n_i\pmod1,\qquad
\sum_i t_i(n_i+b_i)\pmod1,\qquad b_i\in\{0,1\},
\qquad\text{(6.10)}
```
with the same whole-wall membership and the same original lifted maps at every port. The order on another $`T_j`$ is the boundary restriction of this order; it is not independently chosen. Re-rooting adds one common constant. The zero-loop hypotheses retain the uncoloured reference end and order.

Merge complete parent trajectories in the order of their first retained coloured $`F`$-pieces. A parent's labels strictly increase and it retains a subpacket. Thus each event is first in the current whole family; the relative barrier just proved applies at all ports simultaneously. The vertical subdivisions and affine-height prism slabs have genuine simultaneous whole geometric carriers. Their restrictions to faces agree. These are precisely the one-sided closure and coloured-prism arguments of Part 9, §10, with global chamber names replacing separate local names; the new enabling and family-barrier assertions needed for that replacement have been proved above.

The component-wall construction stays in this sector: it recombines entire original actual-bearing components and hence retains only copies of the same $`F`$. It gives the initial $`Y_F`$-to-cyclic comparison. The prism contracts that cyclic sector to its annular part; the annular comparison and contraction are the relative planar ones. The finite-image CW-cylinder argument proves $`Y_F`$ contractible and gives the strong cyclic retraction. The initial component-wall comparison need not fix every geometric annular simplex. To obtain the relative geometric statement, use that $`\mathcal A\subseteq Y_F`$ is a nonempty CW subcomplex, both spaces are contractible, and this cofibration homotopy equivalence admits a strong deformation retraction. Choose it to fix $`\mathcal A`$. These relative choices glue by the CW criterion, proving the last assertion. ∎

### 6.4. A finite geometric certificate with several actual-facing ports

The weighted packet and normaliser proof also works when $`C`$ has several external ports. Suppose an actual support link $`K`$ is replaced, at each component, by a nonempty balanced integer-framed parallel pattern as in (6.9), with genuine support/pattern interfaces. Efficient support modes are enumerated by the finite auxiliary-cluster calculation, with the chosen pattern fibre slopes at the support boundaries. Discard algebraically impossible markings and markings whose nonempty pieces cannot reach an actual pattern through any slope-compatible active port. The latter would give whole closed components. This is a finite conservative reachability test, not an enumeration of all ordinary vertices. Lemma C supplies an additional oriented exclusion.

**Theorem J (all-visible horizontal cluster with return caps).** Assume every nonempty support mode has:

1. exactly one connected horizontal cluster $`C`$ containing every support boundary torus;
2. at least one vertical neighbour, each with one active port and a unique essential return type: a torus-knot block, a cable block with its other port unused, or a composing pants product with its other two ports unused; all other blocks lie beyond unused edges;
3. connected primitive cluster fibre $`R`$, with
```math
\chi(R)\lt 0.
\qquad\text{(6.11)}
```

Then $`Y`$ and $`X`$ are contractible, with $` |Y|\searrow |X| `$. There can be arbitrarily many actual patterns, arbitrarily many actual holes in each, several auxiliary modes, and nonunit degrees on either actual-facing or vertical frontiers. A mode excluded by Lemma C need not be checked further.

**Proof.** Every vertical cap has a single essential same-port return type. For $`N`$ cluster fibres the expanded matchings are (6.1), and the same point/gap orbits give a common parallel packet. Put $`B_{\rm ext}=\sum_j q_j`$, the external boundary count of $`R`$. Each component uses $`2k`$ copies of $`R`$, has $`2kq_j`$ boundaries at external port $`j`$, and
```math
g(F)=1-k\bigl(\chi(R)+B_{\rm ext}\bigr)
=1+k\bigl(2g(R)+B_{\rm cap}-2\bigr),\qquad
\chi(F)=2k\chi(R)\lt 0 ,
\qquad\text{(6.12)}
```
where $`B_{\rm cap}`$ counts boundary circles on the vertical frontier. Interior gap regions are actual products by the weighted proof; the possible asymmetric end regions are harmless. The composing-pants cap has the same parallel-wave and rectangular-complement description as the two-feature orbifold caps, with its two unused ports replacing the two features. Lemma B applies to it as well. Negative Euler characteristic suffices in Theorem I even when (6.12) gives genus zero.

Each component has balanced signed $`R`$-multiplicity. Its dual class vanishes on every support meridian at the external ports, which generate $`H_1(E(K))`$. Hence it is separating. The group-theoretic proof of Lemma G′ still embeds its surface tree and detects ordinary root motion. At port $`j`$, a transverse meridian has $`\eta(\mu_j)=\pm q_j\ne0`$ because its prescribed kernel is an integer-framed longitude. The normaliser argument gives $`m\ell\eta(\mu_j)=0`$, so every port winding is zero. The value need not be one.

In a simultaneous nonempty family the normal mode is common. Start at a support boundary, which belongs to every allowed cluster, and propagate across its horizontal subtree. A horizontal/vertical or horizontal/empty discrepancy at its first edge would give incompatible trace slopes or an omitted required trace. Thus the two markings cannot differ. Inside the one mode, the gap products make all connected support pieces ordinarily parallel. Different ordinary $`F`$-labels cannot occur in one disjoint family.

Theorem I now contracts each actual ordinary sector; their common annular subcomplex is contractible by the relative pattern product. Ordinary fixed-slope comparison at all support boundaries validates the sector labels without equating unknown internal twist markings. Glue the sectors and apply Part 7, Theorem D. All tests in the hypothesis concern finitely many connected JSJ subtrees, their primitive fibre classes and their off-cluster cap shapes. They do not replace ordinary labels by a finite numerical list. ∎

This certificate is a sufficient actual-graph subclass. It does not assert that an arbitrary zero-class region has one such all-visible cluster, or that a cluster without a vertical cap becomes separating.

### 6.5. A weighted distributed-pattern family realising the certificate

The certificate has an explicit family, not merely geometric conditional hypotheses.

**Theorem K (weighted replacements of several parallel supports).** Let $`K`$ be any recursive graph knot and $`m\ge2`$. Take $`m`$ zero-framed support parallels $`K_1,\ldots,K_m`$. Choose positive integers
```math
w_1,\ldots,w_m,\quad \gcd(w_1,\ldots,w_m)=1,\quad
S=\sum_iw_i,
```
and any nonzero integer $`t`$ satisfying $`w_i\mid St`$ for every $`i`$. At support $`K_i`$, take any positive even number of winding-one parallels of framing
```math
f_i=\frac{St}{w_i},
\qquad\text{(6.13)}
```
with equally many of each orientation. Then the resulting actual graph link has contractible $`X,Y`$, with $` |Y|\searrow|X| `$.

If exactly one balanced pair is used at every support and some $`w_i>1`$, $`X=Y`$ is a point. Higher-degree modes become active when enough actual boundaries are supplied. In particular the four-component example (8.2) is contractible.

**Proof.** Its support exterior is a composing product $`H=P_{m+1}\times S^1_\lambda`$ joined at its inner port to $`E(K)`$, with
```math
\lambda_i=\lambda_K=\lambda,\qquad
\mu_K=\sum_i\mu_i .
```
All $`\Phi`$-restrictions on the support vanish. Any nonempty support system must reach an actual pattern, hence meet $`H`$. It cannot be support-vertical, since $`f_i\ne0`$ differs from the fibre $`\lambda`$. Thus $`H`$ is horizontal and meets all support boundaries. Its primitive equations force, up to overall sign,
```math
\eta(\lambda)=St,\qquad \eta(\mu_i)=-w_i,\qquad
\eta(\mu_K)=-S.
\qquad\text{(6.14)}
```
Indeed the vector $`(St,-w_1,\ldots,-w_m)`$ is primitive. The actual-facing degrees are $`w_i`$, and the inner degree is $`S`$ with kernel $`\lambda_K+t\mu_K`$. The connected horizontal fibre $`R_H`$ has
```math
\chi(R_H)=-(m-1)S|t|,\quad
B_{\rm ext}=S,\quad B_{\rm inner}=S.
\qquad\text{(6.15)}
```

If no efficient $`E(K)`$ system has this finite slope, the support is universally empty. Otherwise apply the already proved recursive classification §6.2 at slope $`t`$. A vertical knot root is a torus-knot return cap or a cable return cap with its child unused. If the knot root is horizontal, attach its $`S`$ connected root fibres to the $`S`$ inner boundaries of $`R_H`$. This gives one connected primitive cluster fibre containing every actual-facing port. Its vertical frontier degrees are $`S`$ times the child's frontier degrees. No independent component beyond an unused cut can reach actual boundary.

Because $`t\ne0`$, the child mode cannot be a cap-free whole-knot fibre. At least one vertical cap is present. Moreover the resulting cluster $`R`$ satisfies
```math
\chi(R)\le -(m-1)S|t|,\qquad
\chi(R)+B_{\rm ext}\le S\bigl(1-(m-1)|t|\bigr)\le0.
\qquad\text{(6.16)}
```
This actually gives positive genus in (6.12), stronger than the negative Euler characteristic needed in Theorem J. Every nonempty candidate that can reach actual boundary therefore satisfies that theorem. The support/pattern fibre intersections are $`|f_i|>0`$; the composing-to-knot interface also has different fibres. Internal sum/cable cuts are genuine after flattening composing nodes. Hence the link is non-split by irreducible essential assembly, and Theorem J proves the conclusion.

If every pattern is a two-actual pants and some $`w_i>1`$, Lemma C excludes the only possible $`H`$ primitive class and therefore every nonempty support system. Each remaining pants seam is unique, so both complexes are a point. This last argument does not exclude the active higher-degree case with more actual boundaries. ∎

For example choose $`m=2`$, weights $`(1,2)`$, $`t=2`$, and $`K=C_{2,1}(T(2,3))`$. The framings are $`(6,3)`$. Use one balanced pair at the first support and two at the second. The actual link has six components. The $`H`$-fibre has external degrees $`1,2`$, vertical degree three, Euler characteristic $`-6`$, and genus one. Two opposite fibres and three cable returns form a connected genus-four spanning surface with six actual boundaries. The cable's inner trefoil port is unused, since its vertical inner slope is $`1/2`$. Thus an actual-facing degree-two mode and a tether-free cap are both active in a completely contracted distributed-pattern example.

All four branches (several auxiliary modes, nonunit port degree, a pattern branch with four actual holes, and untethered free returns) occur together by taking instead
```math
K=T(2,3)\#T(2,3)\#T(2,-3),\quad
m=2,\quad(w_1,w_2)=(1,2),\quad t=6.
\qquad\text{(6.17)}
```
The actual framings are $`18,9`$, with respectively two and four balanced actual components. The child has the three modes of (8.1). The singleton modes give $`\chi(R)=-30`$, external degrees $`1,2`$, cap degree three and a genus-28 connected spanning vertex. The three-terminal mode gives $`\chi(R)=-24`$, external degrees $`1,2`$, cap degrees $`3,3,3`$ and a genus-22 vertex. All caps have no actual tether. Several auxiliary phase circles, nonunit external degrees and a branch with four actual holes occur in this same six-component link. Theorem K contracts its entire $`X,Y`$.

**Corollary K1 (arbitrary nonzero framings with nonzero reciprocal sum).** In the same construction on $`m\ge2`$ zero-framed support parallels of any recursive graph knot, allow arbitrary nonzero integer framings $`f_i`$, with
```math
\sum_i\frac1{f_i}\ne0 .
\qquad\text{(6.17a)}
```
Balanced actual counts at every support are arbitrary. Then $`X,Y`$ are contractible. If $`t=(\sum_i1/f_i)^{-1}`$ is not an integer, the entire support is unused.

**Proof.** Put $`D=\mathrm{lcm}(|f_i|)`$, $`w_i=D/f_i`$, and $`S=\sum_iw_i\ne0`$. These signed $`w_i`$'s have gcd one. The primitive class on a nonempty $`H`$ is
$`\eta(\lambda)=D,\eta(\mu_i)=-w_i`$.
Its inner kernel has finite slope $`t=D/S`$. The recursive knot's finite boundary-slope envelope excludes nonintegral $`t`$; this gives the empty-support conclusion.

For integral $`t\ne0`$, the inner degree is $`|S|`$. Repeat the proof of Theorem K, attaching $`|S|`$ child fibres and multiplying their frontier degrees by $`|S|`$. All external degrees are now $`|w_i|>0`$. The horizontal cluster has negative Euler characteristic, and its child cannot be a cap-free whole-knot fibre because $`t\ne0`$. Theorem J applies. This use of signed weights is justified by the negative-Euler proof of Theorem I; no positive-genus inequality for signed weights is presumed. ∎

**Corollary L (a meridional composing cap).** Let $`K=J_1\#J_2`$, where each $`J_i`$ is a nontrivial torus knot followed by any finite sequence of nontrivial cables, without an intervening sum operation. Take two zero-framed support parallels of $`K`$, and replace them by arbitrary nonempty balanced patterns of framings $`(-d,d)`$, for any integer $`d\ne0`$. Then $`X,Y`$ are contractible. This includes a planar four-boundary companion at $`|d|=1`$.

**Proof.** These $`J_i`$'s have no essential meridional trace. In a torus knot neither its horizontal nor its vertical slope is meridional. In a cable space, a horizontal outer meridian would force an inner meridian by $`\mu_{\rm in}=p\mu_{\rm out}`$; a vertical outer slope is finite. Induction excludes it.

On the support composing block $`H`$, a nonempty mode has primitive class
```math
\eta(\lambda_K)=d,\quad\eta(\mu_1)=1,\quad
\eta(\mu_2)=-1,\quad \eta(\mu_K)=0 .
\qquad\text{(6.18)}
```
The inner trace is meridional of degree $`|d|`$. The root composing pants of $`K`$ must be vertical, since its fibre is $`\mu_K`$. Both child ports are unused by the preceding meridional exclusion. Its essential root returns have one ordinary type. Thus it is the third cap allowed in Theorem J.

The horizontal $`R`$ in $`H`$ is planar, with two external boundaries, $`|d|`$ cap boundaries and $`\chi(R)=-|d|\lt 0`$. Each connected support companion is two $`R`$'s joined by $`|d|`$ return annuli, with four external boundaries, genus $`|d|-1`$ and negative Euler characteristic $`-2|d|`$. Theorem J applies, including the planar case. All tori used here are genuine: their fibre intersections are $`|d|,|d|,1`$, and the child meridian-to-fibre intersections are nonzero. ∎

**Corollary L1 (the reciprocal-zero branch with one binary composing root).** Let $`K`$ be either an iterated cable of a nontrivial torus knot, or a finite cable sequence over $`J_1\#J_2`$ with $`J_i`$ as in Corollary L. For $`m\ge2`$ zero-framed support parallels of $`K`$, arbitrary nonzero integer framings $`f_i`$ and arbitrary balanced actual counts have contractible $`X,Y`$, including
$`\sum_i1/f_i=0`$.

For a nonzero reciprocal sum this is Corollary K1. For a zero sum, the forced inner slope on $`E(K)`$ is meridional. In the first knot family it is impossible, by the meridional induction just proved, so the support is empty. In the second family, every outer cable on a meridional trace is horizontal and forces the next trace meridional. At the binary composing root the pieces are vertical and both child ports are unused. There is therefore one horizontal cluster consisting of $`H`$ and that cable chain, incident to every actual pattern, and one composing-pants return cap. A primitive class is obtained by clearing the boundary-value denominators; it may increase actual-facing degrees, which Theorem J permits. Every actual nonempty mode has this description and has negative Euler characteristic. Theorem J proves the assertion. No composing root with three unused children is included.

Explicitly, let $`D=\mathrm{lcm}(|f_i|)`$, $`w_i=D/f_i`$, so $`\sum_iw_i=0`$. Let $`P`$ be the product of the outer cable windings, with $`P=1`$ if the root is already the binary composing block. Put
```math
g=\gcd(P,D),\qquad b=P/g,\qquad a=D/g .
\qquad\text{(6.19)}
```
The primitive cluster class restricts to $`b\eta_H`$ on $`H`$, and has value $`a`$ on the deepest preferred longitude. Its actual-facing degrees are $`b|w_i|`$, its single cap degree is $`a`$, and
```math
\chi(R)=-b(m-1)D-a(P-1)\lt 0 .
\qquad\text{(6.20)}
```
The cable contribution telescopes using $`\chi_{\rm cable}=-(p-1)|\eta(\lambda_{\rm in})|`$. Since $`\gcd(a,b)=1`$ and $`\gcd(w_i)=1`$, the displayed cluster class is primitive. These formulae justify the denominator-clearing and cover even the planar cases, without assuming unit actual-facing degree.

[Overview](../README.md) · [Previous page](part12.md) · [Next page](part12-3.md)
