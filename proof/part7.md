# Part 7. Anchored clusters, iterated cable parallels, an unbounded cancelling family, and the general comparison

[Overview](../README.md) · [Next page](part7-2.md) · Part 7, page 1 of 2

**Summary.** Theorem A proves contractibility of $`X`$ and $`Y`$ for graph-manifold links whose Seifert pieces satisfy the anchoring conditions (A1)–(A2), which allow pieces without actual boundary. Theorem B treats oppositely oriented zero-framed parallels of iterated cables of torus knots. Proposition C exhibits connected incompressible spanning vertices of every positive genus with zero total companion class; it shows that the net-demand contraction of Sections 29–40 cannot be extended unchanged. Theorem D proves $`X\subseteq Y`$ and a strong deformation retraction of $`|Y|`$ onto $`|X|`$ for **every** non-split link in $`S^3`$, using a component-wall carrier and precisely identified printed all-incompressible inputs. Thus $`X`$ is contractible if and only if $`Y`$ is.

The inputs are Sections 29–40 ([theorems](graph-theorems.md)), including the repaired [Lemma 31.2](graph-ordinary-annuli.md), and [Part 6](part6.md), Sections 3–6. Their conclusions are used only within the ranges checked below. Neither Theorem 29.1 nor PS Proposition 3.2 is applied to the non-taut vertices of Theorem B or Proposition C.

## 1. Objects and statements

Use the ordinary, reduced, all-genus spanning conventions of [Section 1](objects.md). Every labelled actual boundary torus is used exactly once, closed components are forbidden, components are incompressible, and boundary curves may slide during ambient isotopies starting at the identity. The complete complement is connected. Its entire lift, rather than a componentwise choice, defines the cyclic block. Write

```math
\Phi(\mu_i)=1,\qquad
D(A,B)=\max\{j:U_{A,j}\cap U_B\ne\varnothing\}
-\min\{j:U_{A,j}\cap U_B\ne\varnothing\},
\qquad
\delta(a,b)=\min_{A\in a,\ B\in b}D(A,B).
```

The vertices of $`X`$ are all these ordinary classes; $`X`$ is the flag completion of distinct pairs with $`\delta=1`$. A simplex of $`Y`$ means simultaneous whole disjoint representatives. There is no flag completion in the definition of $`Y`$.

Let $`\mathscr T`$ be the genuine Seifert JSJ tree, $`M_v`$ a block, $`\Phi_v=\Phi|_{\pi_1M_v}`$, and $`h_v`$ an oriented regular fibre. Set $`k_v=\Phi_v(h_v)`$. “Nonzero restriction” means $`\Phi_v\ne0`$, not necessarily $`k_v\ne0`$.

Call the link **horizontally anchored** if

```math
\qquad\text{(A1)}\Phi_v\ne0\quad\hbox{for every block }v,
```
```math
\qquad\text{(A2)}
\text{every connected component of the induced forest } \{v:k_v\ne0\}
\text{ contains an actual boundary torus.}
```

These are conditions on the oriented link and finite homomorphisms. They do not assume anything about its surfaces or their traces. Evaluation on a finite Seifert generating set checks (A1); the finite JSJ tree checks (A2).

**Theorem A (anchored-cluster extension).** For every nonempty oriented non-split graph-manifold link in $`S^3`$ satisfying (A1)–(A2), both $`X`$ and $`Y`$ are contractible, and the identity on vertices gives $`X\subseteq Y`$ with $`|X|`$ a strong deformation retract of $`|Y|`$.

Boundary-free zero blocks may be adjacent. Boundary-free nonzero-fibre blocks may be adjacent. The total fibre of a block in a non-primitive restricted class $`\Phi_v`$ may be disconnected; each connected horizontal piece is still a connected fibre of the primitive class. Every incompressible spanning vertex is norm-minimising. Active traces are coherent of size $`\mathrm{div}(\Phi|_T)`$, zero-to-zero traces are empty, and the full ordinary quotient and distance/carrier formulas of Sections 29–40 hold at the level of connected horizontal clusters.

This includes Theorem 29.1 and the whole horizontal-leaf star Theorem 29.2. The six-block example in §7.1 belongs to neither of those previously stated graph-manifold ranges.

For the second extension, start with a nontrivial torus knot $`C_0=T(a,b)`$, where $`a,|b|\ge2`$ are coprime. Inductively let

```math
C_j=(p_j,q_j)\text{-cable of }C_{j-1},
\qquad p_j\ge2,\quad q_j\ne0,\quad \gcd(p_j,q_j)=1.
```

The convention is winding number $`p_j`$, hence cable slope $`p_j\lambda_{j-1}+q_j\mu_{j-1}`$. Allow any finite depth, including zero, and either sign of $`b,q_j`$. No composing-space/connected-sum operation is included in this definition.

**Theorem B (iterated-cable double parallels).** Let $`L(C_n)`$ be two oppositely oriented zero-framed parallels of $`C_n`$. Its complete ordinary vertex set consists of exactly two classes:

* $`a`$, the annulus between the actual components;
* $`v`$, two oppositely oriented spanning fibres of $`E(C_n)`$, extended to the two actual tori by annular collars.

They satisfy $`\delta(a,v)=1`$, have disjoint whole representatives, and

```math
X(L(C_n))=Y(L(C_n))=\Delta^1.
```

Both are contractible and their strong deformation retraction is the identity. If $`g_j=g(C_j)`$, then

```math
g_0=\frac{(a-1)(|b|-1)}2,\qquad
g_j=p_jg_{j-1}+\frac{(p_j-1)(|q_j|-1)}2.
```

The complexity of $`a`$ is zero and that of $`v`$ is $`2(2g_n-1)`$. The global $`\Phi`$ vanishes on the entire companion exterior, including all its internal blocks. This theorem is not an instance of Theorem A.

Depth zero is exactly Part 6, with the additional explicit conclusion for $`Y`$. At positive depth the cable blocks have no actual boundary; the outermost one is internal in the JSJ tree.

The torus chain is genuine. At the pattern port the fibre intersection is $`|p_nq_n|>0`$ (or $`|ab|>0`$ at depth zero). At an inner cable port compare $`p_j\lambda+q_j\mu`$ with the companion boundary fibre $`\lambda+s\mu`$, where $`s=ab`$ or the preceding cable product. Their intersection is $`|p_js-q_j|\ne0`$: equality would contradict $`\gcd(p_j,q_j)=1`$. None of the cable spaces is $`T^2\times I`$.

**Proposition C (unbounded cancellation on one fixed graph link).** Let

```math
C=T(2,3)\#\overline{T(2,3)},\qquad L=L(C).
```

For every integer $`r\ge1`$, $`L`$ has a connected incompressible spanning vertex $`s_r`$ of genus $`r`$, hence complexity $`2r`$. The vertices are pairwise distinct. Write $`T_0`$ for the pattern/companion torus and $`T_+,T_-`$ for the two composing/torus-knot tori. Every representative minimising total intersection with this three-torus collection has trace vector

```math
\qquad\text{(1.1)}(\#T_0,\#T_+,\#T_-)=(2r,2r,2r).
```

Also $`\min_{S\in s_r}\#(S\cap T_0)=2r`$, even when only $`T_0`$ is minimised. All three companion block restrictions $`\Phi_v`$, and all three $`\Phi|_{T_e}`$, vanish. The composing block contains $`2r`$ horizontal sections of an auxiliary primitive class with $`r`$ signs of each type. The leaves contain same-port returning vertical annuli. The annular vertex has complexity and trace zero.

Neither slopes nor unsigned multiplicities nor connected topology are determined by the total local classes. This proposition does not assert noncontractibility of $`X(L)`$ or $`Y(L)`$.

**Theorem D (component-wall comparison).** For every nonempty oriented non-split link in $`S^3`$, on the full reduced all-incompressible vertex set, the identity gives $`X\subseteq Y`$ and $`|X|`$ is a strong deformation retract of $`|Y|`$. This comparison does not require a graph-manifold hypothesis or tautness. It does not assert either space contractible.

The printed inputs for Theorem D are Sakuma 1994 Proposition 4.9(1)–(2), including its stated $`IS(L)`$ range, and Banks, arXiv:1109.0965v1, Proposition 4.10 with its explicit extension in §10. Their definitions and exact ranges are checked in §9. No general all-genus version is inferred merely from the taut statement of PS Proposition 3.2.

## 2. The general local signed dichotomy

The following facts do not assume (A1)–(A2), local complement connectivity, actual endpoints on local arcs, or coherent traces.

### 2.1. Efficient cuts

Minimise total intersection with the complete JSJ collection. The essential-cut argument of Section 30 applies without an actual torus in each individual block. Actual boundary is used globally: an original surface component cannot hide in a ball, and a closed cut component would be a closed original component. Inessential circles are removed by disk/ball moves. A boundary-parallel cut annulus has its two ends on one internal torus; an annulus using two curves on one actual torus is forbidden. In its annular parallelism, all other pieces are primitive annuli; an innermost empty one removes two trace circles. Every cut piece is therefore essential before Hatcher Proposition 1.12 is applied.

The same argument works for the embedded union of a finite disjoint labelled family. Independently efficient representatives are not assumed to remain disjoint.

### 2.2. Horizontal multiplicity and signed words

**Lemma 2.1.** A nonempty efficient cut system in a Seifert block has one of two types:

1. vertical annuli, possibly parallel and possibly returning to the same port;
2. $`N\ge1`$ parallel copies of a connected horizontal fibre of a primitive class $`\eta_v`$, carrying a cyclic word of signs $`\epsilon_1,\ldots,\epsilon_N`$.

In the second case, after orienting $`\eta_v`$ once,

```math
\qquad\text{(2.1)}\Phi_v=d_v\eta_v,\qquad d_v=\sum_{\ell=1}^N\epsilon_\ell.
```

If a port has $`q_{\eta,e}=\mathrm{div}(\eta_v|_{T_e})`$, its unsigned trace is $`Nq_{\eta,e}`$, whereas its algebraic trace is $`d_vq_{\eta,e}`$. In a fibration coordinate the port word is the sheet-sign word repeated $`q_{\eta,e}`$ times, up to cyclic starting point and the fixed peripheral orientation convention.

**Proof.** Apply the finite-system proof of Hatcher Proposition 1.12 to the disjoint essential union. Its vertical pieces with boundary are annuli. A horizontal component covers the whole base, so meets every ordinary boundary torus. It cannot coexist with a vertical annulus: on an endpoint torus their slopes would intersect. Closed vertical pieces cannot occur in a cut of a reduced spanning surface.

For a connected horizontal component $`H`$, transverse intersection with the oriented regular fibre has constant nonzero sign. Thus $`\mathrm{PD}[H](h_v)\ne0`$. Its relative class is nonzero, so $`H`$ is nonseparating. A loop closing a single crossing through its connected complement shows that this class is primitive. Hatcher's horizontal-product argument gives $`M_v\mathbin{\|}H=H\times I`$.

After simultaneous horizontalisation, another component is transverse to the interval direction in this product. Projection to $`H`$ is a finite covering; its sheets have a linear order in each interval. Monodromy preserves that order, so a connected component has degree one. It is a graph, isotopic to a horizontal slice. This gives joint parallelism. Proportionality of the classes also follows from their common boundary slopes: rational first homology of a planar Seifert block is generated by the fibre and ordinary boundary loops, with cone loops rational multiples of the fibre.

Adding the oriented classes gives (2.1). In a primitive bundle coordinate the copies are distinct phases. A transverse port circuit reads those phases $`q_{\eta,e}`$ times. ∎

In the vertical case $`\Phi_v`$ kills the fibre and cone generators and descends to a signed ordinary-base class. Each annulus has opposite oriented fibre ends. A same-port return contributes opposite ends at that port. Nonzero unsigned traces with net demand zero are allowed. Ordinary arc classes, cone marks, multiplicities and endpoint tracks remain part of the data; net homology is not a local isotopy classification.

**Corollary 2.2.** If $`k_v=0`$ but $`\Phi_v\ne0`$, every efficient piece in $`M_v`$ is vertical.

Indeed a horizontal system would have $`d_v\eta_v(h_v)=0`$, hence $`d_v=0`$ and $`\Phi_v=0`$. This replaces the actual-boundary argument in this case.

For $`k_v\ne0`$, let $`g_v>0`$ be the divisibility of $`\Phi_v`$. Orient $`\eta_v=\Phi_v/g_v`$. Lemma 2.1 allows

```math
\qquad\text{(2.2)}N=g_v+2t,\qquad t\ge0.
```

One coherent port forces $`t=0`$. Without one, balanced copies cannot be dismissed. If $`\Phi_v=0`$, an entirely different nonzero auxiliary $`\eta_v`$ can occur with $`N=2t`$. Its auxiliary phase direction is not a generator of the global $`\Phi`$-cover.

### 2.3. What remains universally true about width

For arbitrary whole spanning representatives $`A,B`$, the difference current has zero periods: both represent $`\Phi`$. Crossing $`A`$ increases an integral chamber potential $`H`$ by one and crossing $`B`$ decreases it by one; common oriented walls cancel. There is exactly one additive constant on the connected global chamber adjacency graph.

As in Lemma 33.1,

```math
\qquad\text{(2.3)}D(A,B)=\mathrm{osc}H.
```

One whole open $`B`$-block maps homeomorphically onto $`M\setminus B`$. In that lift the values of $`H`$, up to one constant, are the indices of the open $`A`$-blocks. Every chamber has interior and every nonempty block intersection contains a chamber point. This proves (2.3).

This is a representative formula, not a proof that a prescribed signed JSJ normal form attains the ordinary class minimum. Independent constants cannot be assigned on the two sides of a boundary-free block.

**Literature input 2.3 (all-incompressible minimum position).** Almost transverse representatives with simplified intersection attain $`\delta`$, also for non-taut incompressible spanning surfaces. Banks Proposition 4.10 states the minimum-width result, and §10, immediately after Definition 10.1, explicitly extends that proposition and the simultaneous-position Lemma 4.9 to incompressible surfaces. Proposition 2.4 there uses lifts of the whole open complement, and Definition 10.1 is the cyclic flag convention used for $`X`$ here. This is a printed input, not a new extension claimed by this manuscript.

The distinction is important: global simplified minimum position is available. What remains unproved for general signed JSJ data is that a specified ordinary normal-data reduction preserves that attained width and yields an explicit canonical formula.

## 3. Forced coherence under the anchoring conditions

The single Seifert-block cases, including the unknot and Hopf exterior, are covered by the Seifert theorems ([Theorem 1.2](objects.md) and [Theorem 11.2](geometric-retraction.md) of Sections 1–11). For the rest of this proof the genuine JSJ collection is nonempty, so the incompressible-boundary and genuine-block hypotheses used below hold.

Assume (A1)–(A2). No block can have empty cut: intersection with the spanning surface represents $`\Phi_v`$, which is nonzero. In an actual block the original unit-boundary argument applies: if $`k_v=0`$, its pieces are vertical; if $`k_v\ne0`$, it has one connected horizontal piece and coherent trace. At every other zero block, Corollary 2.2 gives vertical pieces. Thus **all** zero blocks are vertical before any edge-trace conclusion.

A maximal $`k_v\ne0`$ subtree has an actual anchor by (A2). Across an edge its nonempty coherent trace is transverse to the next block's fibre, whose evaluation is nonzero. The next block has no vertical piece. Every horizontal copy meets that port, so coherence forces all copies to have the same sign. Its other ports are consequently coherent. Propagate over the finite subtree.

A boundary-free horizontal block may have $`g_v>1`$ pieces. It is the **cluster** that is connected: the anchor starts connected, and every horizontal component of the next block joins the incoming connected union. Induction gives one connected fibre $`H_C`$.

Coherent fibre-monotone phase maps glue across internal tori in class $`\Phi_C`$. An actual meridian of value one makes this class primitive. Thus the cluster is a bundle with connected fibre, regardless of the number of local slices. Cluster monodromy need not have finite order.

At a zero-to-zero edge the two vertical fibre slopes differ, so trace is empty. At an edge with a horizontal side, its coherent trace forces zero-side fibre slope and nonzero signed cardinality. Every active edge has exactly $`q_e=\mathrm{div}(\Phi|_{T_e})>0`$ coherent curves.

A same-port return would have opposite ends. It cannot end on a coherent active port, an empty port, or an actual torus used once. It is excluded by the proof, not removed from the initial classification.

Zero-base degrees balance: $`\pm1`$ at actual boundaries, $`\pm q_e`$ at active ports, zero at cones/empty ports. A boundary-free zero block has nonzero base class by (A1); it therefore has at least two ordinary boundaries. The distinct-end annulus detector of Section 31 applies, including its two-boundary coned cases. Genuine $`T^2\times I`$ blocks are excluded.

Every normal global component has actual boundary: a zero annulus reaches an actual torus or a connected horizontal cluster with actual boundary. No annulus ends at an empty interface. This verifies the reduced convention in both directions of assembly.

All vertices have complexity

```math
\qquad\text{(3.1)}N_\Phi=\sum_{v:k_v\ne0}|k_v|(-\chi^{\mathrm{orb}}(B_v)).
```

Coherence gives that total degree even with multiple local pieces. Compress a norm minimiser and remove closed descendants; this preserves the relative class since $`H_2(M)\to H_2(M,\partial M)`$ is zero for a link exterior. Its incompressible descendant and every other incompressible surface have complexity (3.1). Thus all vertices are norm-minimising, independently of the later minimum-width comparison.

For comparison with Theorems 29.1–29.2: if every block has actual boundary then (A1) and (A2) are automatic. In a horizontal-leaf star with boundary-free centre, each leaf's nonzero fibre evaluation makes its port restriction nonzero, so the central restriction is nonzero too. If the centre is horizontal, it joins the actual leaves in one anchored cluster; if it is zero, every leaf is its own anchored cluster. Thus the entirety of the star Theorem 29.2 is recovered.

## 4. Ordinary quotient, distance, carriers and geometric retraction for Theorem A

This is a transfer of the proofs of Sections 29–40 after checking their local hypotheses, not an invocation of Theorem 29.1 outside its stated range.

### 4.1. Ordinary isotopy

All zero annuli have distinct ordinary ends. Integrated Lemma 31.1 detects their joint ordinary classes and multiplicities by peripheral double cosets in

```math
\pi_1(M_z)/\langle h_z\rangle
\cong C_{a_1}*\cdots*C_{a_s}*F_{b_z-1}.
```

Its proof already permits nonunit port-to-port packets, disconnected cut complements and unused cone/ordinary marks. It gives zero port-configuration winding for a loop of such a system. Tangential fibre motion gives no framing.

The repaired Lemma 31.2 restricts arbitrary ambient isotopies to the JSJ collection using relative product regions and efficient cuts. Its hypotheses here are unchanged: incompressible boundary, essential pieces, coherent traces and no closed original component. A whole incompressible torus cannot lie in a surface product region, whose group is free. A returning torus annulus there gives an innermost boundary-parallel cut annulus, contrary to efficiency. Spanning annuli straighten simultaneously. In the all-zero case the surfaces miss the tori, and the free-group obstruction makes all product pushes avoid them. This is the incorporated R1 repair.

A zero block excludes the global fibre exception by its injected $`\mathbb Z^2`$ in $`\ker\Phi`$, as in Section 31. Its nonzero planar-base class and genuine-block condition, rather than actual endpoints, supply the infinite-order kernel element. If there are no zero blocks the whole surface is a connected bundle fibre and the space is a point.

For a connected horizontal cluster $`C`$ with $`r_C`$ marked outer tori the relative state is

```math
\qquad\text{(4.1)}\mathbb Z^{r_C}/\mathbb Z(1,\ldots,1).
```

Connected $`H_C`$ supplies connectors detecting differences of real boundary-lift constants. Positive-phase convex interpolation gives the converse isotopy, including cone collars. Local disconnectedness causes no change.

Contract empty zero edges to regions $`\Lambda`$ and horizontal subtrees to clusters $`C`$. The incidence graph is a tree. Integer edge states have the unique form

```math
\qquad\text{(4.2)}n_{\Lambda C}=t_\Lambda-s_C
```

modulo one common integer. The extra height rank is $`\#\Lambda-1`$ when zero regions exist. Every annulus boundary track is carried into (4.1). Constants cannot be reset across a boundary-free block. These are exactly the ordinary quotient assertions of Theorem 32.1.

### 4.2. Attained class minimum with one deck displacement

Put the zero diagrams into the ordinary packet normal form of Sections 31 and 33, with their absolute transported constants. Let $`n_z(f)`$ be their difference potentials, with empty-interface values identified. Then

```math
\qquad\text{(4.3)}\delta(a,b)=\max_{z,f}n_z(f)-\min_{z,f}n_z(f).
```

All vertices are taut by §3. Apply PS Lemma 3.5 to $`A,B,\bigcup\mathcal T`$, return the third surface by a common ambient isotopy, and apply PS Proposition 3.2 to the simplified spanning pair. Its width is the class minimum.

The packet comparison normalises the zero diagrams without new global extrema. It retains aligned common copies geometrically and treats every cut component separately. At a boundary-free zero block the same empty bigon, half-bigon, disk and packet moves apply: they use distinct ordinary ends and inherited heights, not actual ends. Every boundary motion is recorded.

Refill a connected cluster using Lemma 34.1. If inherited boundary indices lie in $`[m,M]`$, its formula

```math
g(x,t)=(1-t)v(x)+t(1+v(\rho x))
```

has $`m\lt g\lt M+1`$ for $`0\lt t\lt 1`$, preserves the relative state and adds no index. Only the external return collars need be periodic; $`\rho`$ need not be. The product is $`H_C\times[0,1]`$, so multiple local slices cause no problem.

The resulting normal width is at most the original class minimum. Conversely inherited-lift filling realises the normal data with no extra extreme. This proves both inequalities and attainment of (4.3). A disconnected local complement is never treated as a complete local cyclic block.

### 4.3. Actual potential polyhedra

Choose finite reduced noncrossing zero graphs $`G_z`$, a supported reference vertex $`R`$, and all ordinary/cone marks. Orient edges from negative to positive demand. Let $`D_zu`$ be left-minus-right face differences, $`b_i`$ positive endpoint demands, and $`U_e=\min(b_{\partial_-e},b_{\partial_+e})`$. The actual carrier is

```math
\qquad\text{(4.4)}
\mathcal P_G=\{u:\ u_{f_*}=0,\quad
u_{\rho_{z,e}}=u_{\rho_{z',e}}\text{ on empty interfaces},\quad
0\le m_{R,z}+D_zu\le U\}.
```

Every demand of a zero graph may be nonunit. Integral points make multiplicity band maps, with real face constants extending over the primitive connected clusters in the prescribed states. Every component reaches actual boundary by §3, and essential assembly gives incompressibility. Conversely the ordinary quotient and (4.2) recover exactly one integral point. There is no extra integer or finite quotient.

For supported vertices,

```math
\qquad\text{(4.5)}\delta(v_u,v_w)=\mathrm{osc}(u-w).
```

Common floor rounding preserves the integral-endpoint inequalities and empty-face equalities. Hence

```math
\qquad\text{(4.6)}S_G(u)=\int_0^1[v_{\lfloor u+\theta\rfloor}]\,d\theta
```

is a true cyclic simplex. One threshold is shared by all blocks and heights. Exact expectation and the nested zero-one description of cyclic simplices give exact recovery. A zero-weight edge merges equal faces; root/reference changes preserve the decoder. Unbounded relative directions are retained.

Use real band increments $`m_R+Du\ge0`$, extend real boundary differences into clusters, and choose generic phases. They have proper distinct-end zero arcs, connected cluster fibres and actual boundary on every component. The outputs of (4.6) are thus simultaneously disjoint whole surfaces. In particular $`X\subseteq Y`$.

### 4.4. Strong deformation retraction and contraction

For a geometric simplex choose simultaneous efficient forms and integral coordinates $`u_i`$ on its common zero graphs. Put

```math
\qquad\text{(4.7)}
R\!\left(\sum_i\lambda_i[v_{u_i}]\right)
=S_G\!\left(\sum_i\lambda_i u_i\right).
```

The weighted-wall proof of Lemma 37.1 uses disjoint zero bands and ordered **connected cluster fibres**. Generic weighted levels avoid the whole input family. Band postcomposition reads their actual relative vector as

```math
\left\lfloor\sum_i\lambda_i u_i+1-r\right\rfloor,
```

including transported constants. Inputs and outputs therefore form a genuine geometric carrier. The segment

```math
\qquad\text{(4.8)}\mathcal H(x,t)=(1-t)x+tR(x)
```

stays in $`Y`$ and fixes $`X`$ pointwise.

For contraction apply Section 38's finite-height construction to a finite subcomplex and a base vertex, combining global equivariant band lifts. Delete closed zero-base circles at generic levels and recompute the surviving actual classes and heights. Every remaining zero arc reaches actual boundary or an anchored cluster, even in a boundary-free zero block. Cluster levels keep their actual unit boundary. All outputs are essential reduced spanning surfaces.

A finite PL template and bounded lifted corner values give finitely many actual outputs. Vanishing phase intervals give continuity at collisions. True input simplices have disjoint bands, no circles, and exact recovery. Composing this finite phase-average family with $`R`$ nullhomotopes each finite inclusion into $`X`$, compatibly on its faces. Compact sphere images lie in finite CW subcomplexes; Whitehead gives contractibility.

The image of every closed simplex cylinder of (4.8) is contained in a fixed finite subcomplex, its barycentric functions are continuous, with common-face agreement. The ordinary CW cylinder criterion gives continuity on $`|Y|\times I`$, without local finiteness. This completes Theorem A.

## 5. Longitudinal rigidity for iterated cables

An essential surface here has nonempty boundary, no closed component, and is boundary-incompressible. A boundary-parallel annulus is not essential. Boundary circles are preferred longitudes, with no initial coherence assumption.

**Lemma 5.1.** In $`E(C_j)`$, every connected essential surface with nonempty purely longitudinal boundary has one boundary and is a spanning fibre, with either orientation. Every finite disjoint such system is jointly a parallel fibre system.

**Proof.** For $`j=0`$ use Part 6, Lemma 3.1: horizontalness, coherence on the single torus, primitive class, one boundary and product complement were proved without a genus assumption.

Inductively write

```math
E(C_j)=W_j\cup_{T_{j-1}}E(C_{j-1}),
```

where $`W_j`$ has annular base with one cone of order $`p=p_j`$. Its homology is freely generated by $`\mu_j,\lambda_{j-1}`$, and

```math
\qquad\text{(5.1)}
[\mu_{j-1}]=p[\mu_j],\quad
[\lambda_j]=p[\lambda_{j-1}],\quad
h_j|_{T_j}=\lambda_j+pq\mu_j .
```

The first is winding number. The torus cable has class $`p\lambda_{j-1}+q\mu_{j-1}`$, and torus framing differs from preferred longitude by $`pq\mu_j`$. Substitution proves the second equality.

Minimise with $`T_{j-1}`$. Internal parallel annuli reduce the count; a parallel annulus using only original outer boundary would already be a forbidden boundary-parallel whole component. Thus all cuts are essential.

Outer longitude is transverse to $`h_j`$, since $`pq\ne0`$. The cable-space union is horizontal. Every component meets the outer torus. For one such component, let $`\eta`$ be its primitive dual and $`b>0`$ its number of outer longitudes. Those signs are coherent, so after orientation choice

```math
\eta(\mu_j)=b,\qquad \eta(\lambda_j)=0.
```

Equation (5.1) gives $`\eta(\lambda_{j-1})=0`$, hence $`\eta=b(1,0)`$ in that free basis. Primitivity gives $`b=1`$. On the companion port the restriction is $`(\mu_{j-1},\lambda_{j-1})=(p,0)`$, so its boundary is exactly $`p`$ coherent preferred longitudes.

By induction every companion cut component has one boundary and is a fibre. It joins only one cable-space piece. Each whole component therefore has one outer boundary.

Existence of the cable horizontal piece follows by applying the preceding argument to any incompressible one-boundary Seifert surface of the cable knot. Glue its phase in class $`(1,0)`$ to $`p`$ times the companion knot phase. Boundary degrees agree; fibre-monotone collar interpolation gives a bundle in the primitive knot class. Its fibre is this assembly, with

```math
\qquad\text{(5.2)}\chi(R_j)=-(p-1)|q|+p\chi(R_{j-1}).
```

Uniqueness of a spanning fibre is Lemma 2.4, the all-incompressible fibred-point lemma. For a finite disjoint system normalise one fibre, cut to $`R_j\times I`$, and apply Part 6, Lemma 3.3 successively relative to the end faces. This gives joint parallelism with all orientation labels retained. Equation (5.2) gives the genus formula. ∎

The absence of composing spaces matters: one outer longitude in a cable space forces zero evaluation on its only independent companion longitude; in a composing space it only forces the sum of such evaluations to vanish.

## 6. Ordinary vertices, class minimum and $`Y`$ for Theorem B

Write

```math
E(L(C_n))=(S^1_\lambda\times B)\cup_{T_0}Q,\qquad Q=E(C_n),
```

with $`B`$ a pair of pants having two actual holes and one outer port. Actual slopes are $`+\lambda,-\lambda`$, and $`\Phi|_Q=0`$.

Minimise with $`T_0`$. Pattern pieces are vertical: a horizontal component would meet the actual fibre-slope boundaries. If the actual ends pair, that annulus is the whole surface. Otherwise both actual ends reach $`T_0`$, and all its traces have slope $`\lambda`$. Lemma 5.1 makes every companion piece a one-boundary fibre.

An outer-to-outer pattern return would join the only boundaries of two such fibres and make a forbidden closed component. Thus only two reaching annuli and one positive/one negative fibre occur. This is the complete all-genus topological classification.

For the ordinary quotient, the actual-to-actual pants seam is unique and the two actual-to-outer seams have one joint unmarked class. Jointly normalise the companion pair to phases $`\theta_+,\theta_-`$. During an isotopy of the seam system, follow its **actual path** of outer endpoints by those fibre phases. Matching collar motions glue to an ambient isotopy of the whole system. A common full phase circuit absorbs outer winding; actual boundary motion absorbs inner collar turns. Longitudinal tangential motion is contained in the annuli. There is no relative torus-twist parameter. This is the compatible-path proof of Part 6, §5, with Lemma 5.1 in place of its companion lemma.

The annulus is incompressible by its injected pattern longitude. Each other component is a companion fibre with an annular collar, and injects by amalgam normal form. The classes differ by component count. Their complexities follow from (5.2).

For distance choose the three pants seams disjoint, giving representatives $`A\in a,F\in v`$. Cutting the two reaching annuli leaves $`S^1\times D^2`$. Cutting $`Q`$ along its two fibres leaves two products $`R_n\times I`$, attached along the two outer intervals. Both occur in the **same whole** $`F`$-block; $`\Phi|_Q=0`$, so no independent companion deck indexing is used. The $`A`$-annulus cuts this block into exactly two nonempty connected chambers with consecutive indices. Thus $`D(A,F)=1`$.

Width zero for any representatives would force the connected annulus into the disconnected $`v`$-surface: otherwise a ball about an annulus point in the whole open $`v`$-block meets consecutive annulus blocks. Properness would put its two actual boundaries in one component of $`v`$, impossible. Hence $`\delta(a,v)\ge1`$, without a norm-minimum theorem.

The two vertices have simultaneous disjoint representatives and there are no others. Thus $`X=Y=\Delta^1`$. The identity is the strong deformation retraction, and linear edge contraction to $`a`$ contracts both.

## 7. Actual links and programmed checks

These are links constructed inside $`S^3`$, not merely gluing matrices.

### 7.1. Six blocks, two boundary-free internal vertices

Take Hopf-fibre link pieces of signs

```math
\sigma_C=-1,\quad \sigma_H=+1,\quad
\sigma_A=\sigma_B=-1,\quad \sigma_D=\sigma_E=+1,
```

with tree edges $`CH,HA,HB,CD,CE`$. Pieces $`C,H`$ have three ports and no actual components. Each leaf has one port and two actual regular fibres, both positive in its local orientation. Splice ports by meridian–longitude exchange.

Each newly attached piece has an unknotted port. The unknot exterior is a solid torus with meridian equal to its removed port's preferred longitude; the exchanged gluing therefore fills the other exterior meridionally. Successive splices preserve $`S^3`$, carrying the remaining components. Each block is a product pants piece with injected boundary. Opposite adjacent Hopf signs give fibre intersection two, so these are genuine cuts. Irreducibility and boundary injection under gluing prove non-splitness.

Let $`a_v`$ be the sum of local actual signs and $`x_{v,w}=\Phi(\mu_{v,w})`$. Tree recursion gives

```math
\qquad\text{(7.1)}
x_{v,w}=\sigma_w\left(a_w+\sum_{u\sim w,\ u\ne v}x_{w,u}\right),
\qquad k_v=\sigma_v\left(a_v+\sum_{w\sim v}x_{v,w}\right).
```

| Block | Actual count | $`k_v`$ | $`\mathrm{div}\Phi_v`$ |
|---|---:|---:|---:|
| $`C`$ | 0 | 0 | 2 |
| $`H`$ | 0 | −8 | 2 |
| $`A,B,D,E`$ | 2 each | 4 each | 1 each |

At $`C`$ the signed demands are $`(-4,2,2)`$. Every restriction is nonzero. The horizontal clusters are $`\{H,A,B\},\{D\},\{E\}`$, all anchored. Theorem A applies outside both previously stated graph-manifold ranges.

The zero pants system is unique: two parallel seams to each positive port. Cutting four arcs gives three disk components, so the local complement is disconnected. The $`H`$ block has two horizontal pieces, while its cluster is connected. There are no relative zero-region heights or zero flow cycles, so $`X=Y`$ is a point. The connected spanning surface has

```math
-\chi=8+4+4+4+4=24,\qquad b=8,\qquad g=9.
```

### 7.2. An internal boundary-free cable block

Let $`K_A`$ be the $`(2,1)`$-cable of $`T(2,3)`$, and take $`L(K_A)`$. Its tree is the actual two-hole pattern, then a boundary-free cable space, then a boundary-free trefoil exterior. The cable block is internal. Its fibre on the companion port has longitude coefficient two and is distinct from the trefoil fibre; the pattern and cable fibres are also distinct.

Each whole $`v`$-component has genus two, total complexity is six, and the deep leaf trace is $`(+,-,+,-)`$, size four despite $`\Phi|_T=0`$. Theorem B gives $`X=Y=\Delta^1`$.

### 7.3. A separate noncoherent leaf example

Let $`K_B`$ be the $`(3,2)`$-cable of $`T(2,5)`$, and take $`L(K_B)`$. Its boundary-free leaf trace is $`(+,-)^3`$, size six. Each $`v`$-component has genus seven and total complexity is twenty-six. Again $`X=Y=\Delta^1`$.

At the boundary of a depth-$`j`$ companion in $`L(C_n)`$, the $`v`$-trace has $`2\prod_{\ell=j+1}^n p_\ell`$ curves. The two top phases under $`(\prod p_\ell)f_j`$ give alternating signs on a meridional circuit. The total class is zero. Section 6's direct distance calculation keeps one common deck displacement through the entire chain.

[Overview](../README.md) · [Next page](part7-2.md)
