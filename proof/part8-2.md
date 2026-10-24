# Part 8. The square-knot tree and recursive graph-knot double parallels (continued)

[Overview](../README.md) · [Previous page](part8.md) · [Next page](part8-3.md) · Part 8, page 2 of 3

## 9. Cyclic distance and a checkable parent calculation

The tree gives an exact ordinary-class metric description. Let $`h(s)`$ be the number of parent edges from $`s`$ to $`a`$. For any two vertices let $`w`$ be the first common vertex of their parent paths, viewed from the endpoints. Banks Proposition 2.4, with the corrected cyclic convention and its explicit §10 extension, identifies the cyclic class distance with graph distance. Therefore

```math
\delta(s,t)=h(s)+h(t)-2h(w).
\qquad\text{(9.1)}
```

This is an exact parent-tree formula. Recognising equality between two independently presented leaf/twist normal data is still a separate coordinate issue; (9.1) does not conceal a solved arithmetic quotient for that issue.

There is also a direct closed finite formula from any normal data for distance to $`a`$.

**Proposition 9.1 (annular distance).** Let $`s`$ be connected and nonannular, with data $`(r,c)`$ and sign word $`\epsilon_0,\ldots,\epsilon_{2r-1}`$. Put

```math
u_0=0,\qquad u_{j+1}=u_j-\epsilon_j\quad(0\le j\lt 2r).
```

Then

```math
\delta(a,s)=\max_j u_j-\min_j u_j.
\qquad\text{(9.2)}
```

In particular, $`1\le\delta(a,s)\le r`$, and equality with one occurs exactly when $`r=1`$.

**Proof.** Choose the annular pattern seam to miss the tethers and cross each pattern return once. All its intersection circles with $`S`$ are essential. No two such circles cobound an annulus in $`S`$, and none cobounds an annulus with an actual boundary: by Lemma 3.2, every intervening chain segment contains a positive-genus companion piece. A product region between $`A`$ and $`S`$ would have an annular face on $`A`$ and such an annular face on $`S`$, or a disk face bounded by an inessential intersection. Neither is possible. Thus the pair has simplified intersection and attains the class minimum by the printed Banks input.

The difference current $`A-S`$ has zero periods and defines one global integral chamber potential, up to one additive constant. In the composing block, where $`A`$ is absent, its successive values are precisely the $`u_j`$. Every leaf complementary component reaches its composing port: for vertical leaves these are the annular products and the two cone end regions; for horizontal leaves they are the fibre products. Thus no new value occurs in a leaf. Cutting the pattern pants along the annular seam gives an annulus. The tether pieces and the halves of the returns are $`2r`$ spanning arcs in this annulus, so every pattern chamber reaches $`T_0`$. No new value occurs there either.

The oscillation of this one potential is exactly the whole-complement representative width: in a whole lift of the $`S`$-complement its values are the indices of the open $`A`$-blocks, and every chamber has interior. This proves (9.2). Its upper bound is immediate from the $`r`$ signs of each type. The distance-one assertion also follows from (8.1). ∎

The sign word can be computed without solving a geometric isotopy problem: alternate signs along the path (3.4), beginning with $`+`$. For the construction of Part 7, §8, $`c=1`$, it is

```math
\epsilon_0=+1,\qquad \epsilon_i=-1\ (1\le i\le r),\qquad
\epsilon_i=+1\ (r\lt i\lt 2r).
```

Its prefix oscillation is $`r`$, proving (1.3).

For a further arithmetic check, let $`u`$ be the inverse of $`c`$ modulo $`2r`$, chosen in $`\{1,\ldots,2r-1\}`$, and put $`q=\min(u,2r-u)`$. If $`r>1`$, then $`1\le q\lt r`$. The first pattern return $`\{1,2r-1\}`$ occurs after $`q`$ companion edges in (3.4). The parent retains the suffix after it, and therefore

```math
r(p(s))=r-q.
\qquad\text{(9.3)}
```

To compute its new offset, retain the suffix section labels, cyclically reorder them starting at the new positive tether, and read the partner of that tether. This gives the new odd unit $`c'`$ modulo $`2(r-q)`$. The parent retains the corresponding actual companion pieces and boundary tracks; these tracks must not be thrown away when determining its ordinary class.

## 10. The square knot's ordinary quotient

For the square-knot model the complete topological alternatives are now:

* the unique annulus $`a`$;
* the unique disconnected capped-fibre vertex $`v`$;
* connected genus-$`r`$ vertices, $`r\ge1`$, assembled from $`2r`$ sections of $`(1,-6,+6)`$, with one common leaf reflection of odd unit offset $`c`$ modulo $`2r`$, and the pattern matching (2.2).

Neither the genus nor $`(r,c)`$ is a complete ordinary coordinate. The following describes the remaining quotient for this particular four-block exterior. It is not needed for the tree proof.

### 10.1. Fixed reference systems

Choose the representative $`c\in\{1,3,\ldots,2r-1\}`$, put $`n=2r`$, and use the sign word determined by (3.4). Fix the following reference objects once for every $`(r,c)`$.

* In the pattern, use the nested system (2.2), its labelled tethers, and outer phases $`i/n`$.
* In the composing block, use a fixed section map $`f_0`$ in class $`(1,-6,+6)`$ and the levels $`i/n`$ with their prescribed signs.
* At each leaf, the reflection $`i\mapsto c-i`$ has two endcap gaps, numbered

```math
j_0=(c-1)/2,\qquad j_0+r.
```

  For $`e\in\{0,1\}`$ choose one reference vertical packet with the order-two exceptional fibre in the endcap at gap $`j_0+er`$, and the order-three fibre at the other end. Its boundary circles are the same labelled phase circles $`i/n`$. Give its annuli the orientations prescribed by the section signs. Different choices of these fixed reference drawings only change the coordinate origin below.

For integers $`z_+,z_-`$, choose a real function $`u`$ on the composing base that is $`0`$ at its outer boundary and is $`z_+`$ and $`z_-`$ at the two leaf boundaries. Replace the composing levels by the levels $`i/n`$ of $`f_0-u`$. Their boundary circles have not changed, since these boundary values are integers. Glue to the fixed pattern and leaf packets. Denote the resulting vertex by

```math
s(r,c,e_+,e_-,z_+,z_-).
\qquad\text{(10.1)}
```

The choice of the real function with these boundary values does not matter: linear interpolation gives an isotopy through sections. All of these assemblies are essential and connected by §3.

**Proposition 10.1 (complete ordinary square-knot coordinates).** The map (10.1) is a bijection

```math
\coprod_{r\ge1}\left\{
c\in\{1,3,\ldots,2r-1\}:\gcd(c,2r)=1
\right\}\times\{0,1\}^2\times\mathbb Z^2
\ \longrightarrow\ \mathrm{Vert}(X)\setminus\{a,v\}.
\qquad\text{(10.2)}
```

The references are fixed before using this bijection. In particular, the two integer coordinates are not discarded by ordinary boundary motion.

### 10.2. Zero winding of the pattern and leaf packets

There is no nonzero period of the sign word. Indeed, if $`\epsilon_{i+d}=\epsilon_i`$ for a nonzero $`d\bmod n`$, then $`d=r`$ contradicts the two tether signs; otherwise applying the pattern sign relation at $`d`$ gives $`\epsilon_d=-\epsilon_{-d}`$, although both equal $`\epsilon_0`$. This also rules out a hidden rotation of indistinguishable signed section labels.

A loop of the pattern system has zero winding in the transverse configuration of its outer trace circles. Track the positive tether. Quotienting by its full fibre gives the ordinary pants group. The tracked spanning arc gives an equation

```math
d_+^{\ell}w d_0^{-k}=w.
```

The two peripheral classes $`[d_+]`$ and $`[d_0]`$ are independent in the pants abelianisation, so $`\ell=k=0`$. Tangential fibre motion changes no annulus image.

At a torus-knot leaf a loop of the labelled packet also has zero transverse boundary winding. The packet is linearly ordered between the order-two and order-three end regions. These regions cannot be interchanged by an ordinary isotopy: the fibre subgroup has indices two and three in their respective solid-torus core groups. The identity isotopy preserves the central fibre and these indices. Pick the annulus adjacent to the order-two end. In the fibre quotient

```math
\Gamma=C_2*C_3
```

let $`x`$ be the order-two generator and let $`d`$ be the ordinary boundary word, conjugate to $`(xy)^{-1}`$. A spanning path of the chosen annulus, closed through its endcap boundary interval, represents $`x`$ up to the fixed reference conjugacy. A loop of the boundary configuration with winding $`k`$ would give

```math
d^k x d^{-k}=x.
\qquad\text{(10.3)}
```

Any annular Dehn twist of the tracked spanning path is a fibre power and has already vanished in this quotient. In the free-product normal form the centraliser of $`x`$ is its finite factor $`C_2`$, whereas $`d`$ has infinite order and no nonzero power in that factor. Thus $`k=0`$.

The same argument applies to the mirror leaf and to arbitrary packet multiplicity. A loop cannot evade it by permuting endpoints: compatible composing-section labels have no nontrivial cyclic permutation, and the end regions fix the linear packet order.

### 10.3. Surjectivity and the two relative integers

Put a square-knot spanning surface in essential normal form. The values $`(r,c)`$ are already determined by the outer pairing. Straighten the pattern to its reference system, carrying its actual boundary motion into composing collars. At each leaf, its nested annuli cut the base into two singly marked end regions and rectangles. Matching these cut regions gives an isotopy, with boundary permitted to move, to a reference packet with the appropriate endcap choice $`e_\pm`$. A boundary twist of the twice-marked disk is absorbed by that boundary motion; its winding will be recorded, not forgotten. Extend the two leaf boundary motions into composing collars.

Now all three composing boundary configurations are the reference configurations, with the same individual section labels. Jointly straighten the composing pieces to sections relative to those configurations. The space of $`n`$ labelled points of a fixed cyclic order on a circle is a circle times a contractible open simplex. Accordingly a section system is a map from the composing pants into that configuration space. Its absolute homotopy class is fixed by the auxiliary section class. In the fixed section coordinate supplied by $`f_0`$, its circle-coordinate difference from the reference has zero absolute periods and therefore has a real lift. At each boundary this lift is an integer constant, common to all section labels by their cyclic ordering. Write these constants as $`(n_0,n_+,n_-)`$. Changing the lift adds one integer to all three, so the relative data are precisely

```math
z_+=n_+-n_0,\qquad z_-=n_--n_0.
\qquad\text{(10.4)}
```

Equivalently this is the connecting group

```math
H^0(\partial B_m;\mathbb Z)/H^0(B_m;\mathbb Z)\cong\mathbb Z^2
```

for the composing pants. The interval-gap coordinates in the configuration space are contractible. Thus (10.4) is the full relative section isotopy datum once the three boundary configurations are fixed. This proves surjectivity of (10.2).

### 10.4. Injectivity under ordinary isotopy

For the square knot all connected nonannular normal forms have the same three trace slopes: $`\lambda`$ at $`T_0`$ and $`h_\pm`$ at the two leaf tori. Apply the product-annulus proof of Lemma 4.1 to the union of these three tori. The boundary traces on each torus can be made disjoint because their slopes are known equal. An innermost returning torus annulus would make a complete cut piece parallel into that **same** torus. Spanning torus annuli straighten jointly. Hence an ordinary isotopy between two such normal forms can be chosen to preserve every one of the three tori. This is the full-torus comparison here; it is not applied to unknown slopes in the larger recursive family.

The positive tether fixes the origin of the section labels, and the cyclic order fixes all the other labels. A compatible local isotopy therefore returns each labelled boundary circle to its own reference circle. It preserves the labelled endcap gaps and the indices two and three just discussed, giving $`e_\pm'=e_\pm`$. The pattern and leaf pieces are now loops of their reference systems, and §10.2 gives zero transverse winding on all three composing boundaries.

The relative integers in (10.4) cannot change during such an ordinary composing isotopy. They may be detected by algebraic intersections of a tracked section with proper arcs between the outer reference chamber and each leaf reference chamber. The only possible change under moving boundary curves is the difference of their endpoint transverse windings, which is zero here. This detector does not require the intermediate surfaces to stay horizontal. Thus $`z_+'=z_+`$ and $`z_-'=z_-`$. Together with the already intrinsic $`(r,c)`$, this proves injectivity. ∎

The parent construction acts on these actual classes by retaining its companion suffix and recording the induced boundary tracks when returning to the fixed references. Equations (9.1) and (9.2) therefore give exact class distances, with ordinary equality now decided by (10.2). A single closed arithmetic formula for the changes of the particular fixed-reference tuple $`(e_+,e_-,z_+,z_-)`$ under the parent is not needed; the following ancestor coordinates eliminate those changes.

### 10.5. An arithmetic tree over the genus-one vertices

Let $`\Omega`$ be the genus-one vertex set, identified by (10.2) at $`(r,c)=(1,1)`$ with $`\{0,1\}^2\times\mathbb Z^2`$. Let $`\mathcal A`$ have vertices $`(r,c)`$ with $`r\ge1`$ and $`c`$ an odd unit in $`\{1,\ldots,2r-1\}`$. Its root is $`(1,1)`$; its parent is the suffix operation of (9.3) followed by the cyclic relabelling described after that equation. This is an entirely finite arithmetic operation on $`(r,c)`$, and it strictly decreases $`r`$.

**Proposition 10.2 (complete square-knot tree model).** The connected nonannular vertices are in bijection with

```math
\Omega\times\mathrm{Vert}(\mathcal A).
\qquad\text{(10.5)}
```

The first coordinate of $`s`$ is its genus-one ancestor, and the second is its outer data $`(r,c)`$. The full complex is obtained by attaching one copy of $`\mathcal A`$ for every $`\omega\in\Omega`$ to $`a`$ by the edge from its root, and attaching the additional pendant edge $`a v`$. There are no other edges or simplices.

**Proof.** Fix an outer stratum $`(r,c)`$ with $`r>1`$ and its arithmetic parent $`(r',c')`$. Under deletion of the companion prefix, the two cone end regions at each leaf remain distinct, since at least one annulus remains. Thus the map on its two endcap choices is a bijection; interchanging which end region contains the order-two fibre interchanges the target choice as well.

For fixed endcap choices, the two integral coordinates are a free transitive $`\mathbb Z^2`$ action by torus spins in the two leaf collars, as realised explicitly by the section translations in §10.1. These homeomorphisms fix the pattern pointwise. They therefore commute with the annular parent: the first return and the chosen negative side are carried to the corresponding first return and negative side. On the target stratum they act by the same unit translations of its two relative integers. Consequently the parent is an equivariant map between two free transitive $`\mathbb Z^2`$ sets. It is a bijection. Including the four endcap choices, it is a bijection from the whole $`(r,c)`$ stratum onto the whole $`(r',c')`$ stratum.

Induct down to $`(1,1)`$. In every $`(r,c)`$ stratum, the genus-one ancestor map is therefore a bijection onto $`\Omega`$. This proves (10.5). The edge statement is the already proved parent criterion. ∎

In particular the annular vertex has countably infinite valence. The tree is not locally finite, which is why §8.2 specifies the weak/CW topology explicitly.

This gives a finite arithmetic description of every pair distance in ancestor coordinates. Compute the depth $`d(r,c)`$ by (9.2), or by the parent loop. Different $`\Omega`$ coordinates have distance $`d(r,c)+d(r',c')`$. For equal $`\Omega`$ coordinates, find the first common arithmetic ancestor $`(r_0,c_0)`$ and subtract $`2d(r_0,c_0)`$ from that sum. The annular vertex has distance $`d(r,c)`$ from such a vertex, and $`v`$ has distance $`d(r,c)+1`$. Thus the ordinary quotient and all class distances in the square-knot model have a full description, without identifying distinct twists. Converting an arbitrary externally drawn surface to the chosen fixed-reference integers remains a normalisation task, not a new isotopy quotient assumption.

The two-integer conclusion of Proposition 10.1 is specific to the square-knot four-block model. An arithmetic enumeration of the end-region stabilisers and twisting coordinates in the larger recursive family remains open here. None is needed for its tree theorem.

## 11. Extension through arbitrary connected sums and cables

Define a recursive class $`\mathcal G`$ of knots as follows. Its initial members are nontrivial torus knots. It is closed under connected sums of at least two members and under $`(p,q)`$-cabling with winding number $`p\ge2`$, $`q\ne0`$, and $`\gcd(p,q)=1`$. Flatten adjacent connected-sum operations, and omit trivial summands. This specifies actual knots and their usual composing/cable/torus-knot decomposition. No classification theorem identifying every possible graph-knot description is required for the statement below.

**Theorem 11.1 (recursive extension).** For every $`K\in\mathcal G`$, the opposite zero-framed double parallel $`L(K)`$ has $`X=Y`$ equal to a rooted simplicial tree. The only disconnected vertex is the capped fibre pair $`v`$, pendant at the annulus $`a`$. The parent construction, the complete edge criterion, the root-prefix distance formula (9.2), and the parent-tree distance formula (9.1) remain valid. The integer $`r`$ is half the minimum outer trace; a connected nonannular vertex has genus $`r b`$ for a positive integer $`b`$ determined by its horizontal-cluster mode.

The necessary extension is local and is proved here. In particular one does not replace a nonunit terminal trace by a unit trace or forget its repeated sign word.

### 11.1. Finite slopes and horizontal root pieces

Measure a finite boundary slope by the rational number $`t`$ in $`\lambda+t\mu`$; the meridional slope is infinite. Consider an essential orientable surface system with nonempty boundary, no closed components, and a common finite outer slope in $`E(J)`$, for $`J\in\mathcal G`$. Put it in essential cut form recursively, relative to that fixed outer boundary.

**Lemma 11.2.** Every such finite outer slope is an integer. In a horizontal root block every connected horizontal piece has exactly one outer boundary. The possible finite-slope rules are:

```math
\begin{array}{ll}
\text{torus-knot leaf }T(a,b):&t=0\text{ (horizontal), or }t=ab\text{ (vertical)};\\ 
\text{composing block}:&t=t_1+\cdots+t_k;\\ 
\text{cable block }(p,q):&t=pq\text{ (vertical), or }t=p^2t_0\text{ (horizontal)}.
\end{array}
\qquad\text{(11.1)}
```

In the vertical cable case the inner port is empty; the outer returns separate the one cone from the unused inner hole.

**Proof.** Use induction on the recursive description. The induced system in a child knot exterior is essential, as required to apply induction. It is incompressible by essential cutting. A boundary-compressible component would be a boundary-parallel annulus by Hatcher Lemma 1.11. In the efficient block decomposition of such an annulus, every piece has nonpositive Euler characteristic. All genuine blocks here have negative base-orbifold Euler characteristic, so no piece could be horizontal. All pieces would be vertical annuli, which cannot cross a genuine JSJ torus with different fibre slopes on its two sides. The whole annulus would therefore lie in the child's root block. Its annular parallelism cannot contain an internal incompressible torus: that torus would inject a rank-two abelian group through the cyclic group of the parallelism solid torus. Since the parallelism boundary misses the internal tori, any torus meeting it would be wholly inside. Thus the parallelism lies in the root block too, making the annulus a forbidden boundary-parallel cut piece. This excludes the alternative.

The torus-knot base case is the one-boundary horizontal fibre/vertical-annulus dichotomy already proved in §2.3.

In a composing block, a finite outer slope is transverse to the meridional Seifert fibre. The entire root system is horizontal. Write the primitive class of one connected piece as $`\eta(\mu)=d>0`$ and $`\eta(\lambda_i)=a_i`$. Its child port has finite slope $`t_i=-a_i/d`$. The inductive hypothesis makes every $`t_i`$ integral. Thus every $`a_i`$ is divisible by $`d`$, and primitivity gives $`d=1`$. The outer slope is the sum of the child slopes and its boundary multiplicity is one. Every horizontal piece meets each child port, so no missing child trace is assumed here.

In a cable block use the integral homology identities

```math
[\mu_0]=p[\mu],\qquad[\lambda]=p[\lambda_0],\qquad
h|_{T_{\rm out}}=\lambda+pq\mu,
\qquad\text{(11.2)}
```

in the free basis $`\mu,\lambda_0`$. Suppose the outer slope is $`b/a`$, with $`a\ge1`$ and $`\gcd(a,b)=1`$. In the horizontal case, if a connected piece has $`k`$ outer boundary circles, coherent boundary orientation gives

```math
\eta(\mu)=ka,\qquad \eta(\lambda_0)=-kb/p.
```

Its inner slope is $`b/(p^2a)`$. It is finite and is integral by induction. Therefore $`a=1`$ and the outer slope is $`p^2t_0`$ for an integer $`t_0`$. The class is $`k(1,-pt_0)`$, so primitivity gives $`k=1`$.

In the vertical case the outer slope is $`pq`$. Any inner trace would have cable-fibre slope $`p\lambda_0+q\mu_0`$, namely the nonintegral finite slope $`q/p`$. This contradicts induction, since $`p\ge2`$ and $`\gcd(p,q)=1`$. Thus the inner port is empty. The remaining essential vertical annuli return to the outer port and separate the cone from the inner hole. Components behind the empty port would have no original outer boundary, hence would be forbidden closed components. This proves all assertions. ∎

Only finite slopes are classified in this lemma. Essential meridional annuli in composing spaces are not claimed absent. They cannot be entered by the horizontal finite-slope system under consideration.

### 11.2. A horizontal cluster with repeated terminal words

Return to the longitudinal boundary of the companion $`Q=E(K)`$ inside $`E(L(K))`$. A root vertical block is impossible: a torus-knot or cable fibre has nonzero finite slope, and a composing fibre has meridional slope. Start with the horizontal root and continue through horizontal blocks. Stop at a vertical torus-knot block or at a vertical cable block with empty inner port. All remaining subtrees behind empty ports contain no surface.

Call the resulting horizontal cluster $`C`$. By Lemma 11.2 each local horizontal component has one incoming boundary, though one parent piece may have several child boundaries. Hence the horizontal pieces of one root component attach down the tree to form one connected surface $`H`$ with one outer boundary. At a terminal port it has $`q_j\ge1`$ coherent boundary circles. A cable continuation multiplies these boundary counts by its winding $`p`$; a composing continuation does not change them. Thus $`q_j`$ is the product of the winding numbers on the path to terminal $`j`$.

The coherent local horizontal phase maps glue to a primitive circle map on $`C`$: their port degrees are exactly the matching $`q_j`$, and the outer meridian has value one. Its fibre is $`H`$, and cutting $`C`$ along it is $`H\times I`$. Consequently a whole normal system with $`N`$ root components is jointly a parallel system of $`N`$ copies of $`H`$. Its signs form the same outer word $`\epsilon_0,\ldots,\epsilon_{N-1}`$, and terminal $`j`$ reads that word repeated $`q_j`$ times. This circle map is auxiliary: the original spanning class still vanishes on $`Q`$, and no independent global cyclic-cover indices are assigned from this map.

One can also construct these cluster maps directly. For a primitive integral class on an orientably based Seifert block with nonzero fibre value, choose a closed one-form in that class and average it over the Seifert circle action. The averaged form has the same periods. Its evaluation on the action vector is constant and nonzero, so it integrates to a circle-valued submersion. Primitivity makes the fibre connected. Compatible boundary maps glue along the tree. This establishes existence of the local horizontal pieces used in a prescribed mode, rather than inferring existence from the surface-classification theorem alone.

If there is no vertical terminal, $`C=Q`$ and $`H`$ is the usual spanning fibre. Pattern returns would make closed components, as in §2.3. This is exactly the capped vertex $`v`$.

If there is a vertical terminal, in fact there are at least two. Propagating (11.1) to the longitudinal root writes its slope as

```math
0=\sum_{j\ {
m terminal}} w_j^2 s_j,
\qquad\text{(11.3)}
```

where $`w_j=q_j>0`$ and $`s_j`$ is the nonzero outer fibre slope of the terminal torus-knot or cable block. One nonzero summand cannot give zero. Put $`Q_C=\sum_j q_j\ge2`$ and $`g_H=g(H)`$. Then

```math
-\chi(H)=2g_H+Q_C-1>0.
\qquad\text{(11.4)}
```

### 11.3. Descending the terminal reflections to outer sheet labels

For a single spanning vertex the pattern has $`N=2r`$ outer circles and the two defects (3.1). At terminal $`j`$ the $`Nq_j`$ endpoints of its nested essential annuli have a reflection matching

```math
\ell\longmapsto c_j-\ell\pmod{Nq_j}.
\qquad\text{(11.5)}
```

The endpoint belongs to root copy $`\ell\bmod N`$. Opposite annular end orientations therefore give

```math
\epsilon_{c_j-i\bmod N}=-\epsilon_i.
\qquad\text{(11.6)}
```

An induced reflection with a fixed root label is impossible by (11.6). Since $`N`$ is even, its offset is odd. The proof of Lemma 3.1 now applies **modulo $`N`$**, so all the terminal reflections induce the same $`i\mapsto c-i`$ on root copies. The actual offsets modulo $`Nq_j`$ are retained; they are not equated or discarded.

It follows that every companion component consists of two copies of $`H`$, joined by $`q_j`$ annuli at terminal $`j`$. It has two opposite longitudinal outer boundaries and genus

```math
b=2g_H+Q_C-1=-\chi(H)>0.
\qquad\text{(11.7)}
```

The outer incidence graph is once again exactly the graph of §3: one matching $`L(i)=c-i`$, the partial pattern matching $`P(i)=-i`$, and two actual tethers. Reducedness is equivalent to $`\gcd(c,2r)=1`$. The surface is a path of $`r`$ companion pieces. Every pattern return separates its actual boundaries and has positive genus on each side.

Conversely, for any zero-slope mode with at least one terminal, construct $`H`$ as above, take $`2r`$ signed parallel copies, and at each terminal choose any odd reflection offset congruent to a chosen odd unit $`c`$ modulo $`2r`$. Its nested return annuli exist in the twice-featured base and pair opposite signs in the repeated word. Assemble the pattern as in §3. Essential assembly proves incompressibility; the unit condition excludes closed components. Thus every such mode has actual vertices for every $`r\ge1`$.

### 11.4. The common packet with nonunit terminal degree

For a disjoint family, simultaneous normalisation gives one common horizontal-cluster mode, by joint horizontal parallelism successively at every entered block. Each member's companion components are pairs of root copies by §11.3. Thus the terminal reflections, reduced to the root-copy labels of the entire family, give the same matching. Write its total number of root copies as $`N=2R`$ and its common offset as $`c`$; it need not be a unit for the union.

The cluster gaps are products $`H\times I`$ indexed by $`i\bmod N`$. At terminal $`j`$, a port gap has index $`\ell\bmod Nq_j`$, and its complementary-region matching is

```math
\ell\longmapsto c_j-\ell-1.
```

Its projection to cluster gaps is

```math
i\longmapsto c-i-1\pmod N.
\qquad\text{(11.8)}
```

This has two fixed cluster gaps and $`R-1`$ paired gaps. Only the containment of the end-region projections in the two fixed gaps is used: when a terminal multiplicity is even, both end regions of that terminal can project to the same fixed gap. For a nonfixed paired gap, none of its port gaps can be a terminal endcap: a terminal fixed gap would project to a fixed cluster gap. All its terminal regions are therefore annulus products, $`q_j`$ at terminal $`j`$. These products glue the two corresponding $`H\times I`$ pieces into a product between neighbouring whole companion components, exactly as in Lemma 6.1. The horizontal faces match the same two root-copy pairs throughout, so the interval direction cannot reverse around a cycle.

Terminal endcaps, and all unused subtrees behind a vertical cable's empty inner port, attach only in the two fixed cluster gaps. They add no intervening chamber. Hence the companion pieces of the entire disjoint family still form one linear parallel packet. This supplies the full nonunit replacement for Lemma 6.1.

All the hypotheses used in §§4–8 are now established. The outer trace slope is still $`\lambda`$, so Lemma 4.1 and the canonical annular parent apply without change. The common packet gives the same four-holed-sphere comparison, the lifted empty rectangle, and dimension one. The parent argument proves the tree. All chamber values outside the cluster reach its gaps, including unused subtrees through their empty ports, so the root-prefix calculation also remains unchanged. This proves Theorem 11.1.

### 11.5. Finite mode arithmetic and examples

A useful check on the cluster geometry records a mode as $`(t,g_H,Q_C)`$. A vertical stop is represented by a **formal boundary collar** profile $`(s,0,1)`$; its vertical block is not part of the horizontal cluster. A torus-knot horizontal mode is $`(0,g(K_i),0)`$. A composing operation adds the three coordinates. A horizontal $`(p,q)`$-cable continuation sends a child profile to

```math
\left(
p^2t,\quad
pg_H+\frac{(p-1)(|q-pt|-1)}2,\quad
pQ_C
\right),
\qquad\text{(11.9)}
```

and it has the additional vertical-stop profile $`(pq,0,1)`$. The horizontal cable piece has Euler characteristic $`-(p-1)|q-pt|`$, one outer boundary and $`p`$ inner boundaries, giving (11.9). The factor is nonzero because $`q\ne pt`$ by coprimality.

At the longitudinal root select $`t=0`$. The unique mode with $`Q_C=0`$ is the spanning fibre and gives $`v`$. Every mode with $`Q_C>0`$ satisfies $`Q_C\ge2`$ and has companion genus $`b=2g_H+Q_C-1`$. No equality of ordinary vertices is inferred from equality of these profile triples.

For example:

* the $`(2,1)`$-cable of the square knot has a cancellation mode with $`b=3`$;
* applying a further $`(3,-2)`$-cable gives $`b=13`$;
* the connected sum of the $`(2,3)`$-cable of a trefoil with a mirror trefoil has a mode with $`b=1`$: the cable block itself is vertical and its deeper companion is unused;
* the connected sum of the $`(2,1)`$-cable of a trefoil with $`T(3,-8)`$ has a cancellation mode with $`b=12`$.

Their connected vertices in each displayed mode have genus $`rb`$ for every $`r\ge1`$, and their full complexes are trees, including all other allowed modes.

[Overview](../README.md) · [Previous page](part8.md) · [Next page](part8-3.md)
