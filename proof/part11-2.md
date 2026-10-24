# Part 11. The resonant Hopf star (continued)

[Overview](../README.md) · [Previous page](part11.md) · Part 11, page 2 of 2

## 10. Multiport extension and its scope

The repeated-axis argument is not specific to three leaves.

**Theorem 10 (balanced resonant Hopf stars).** For any $`n\ge3`$, take $`n`$ regular Hopf fibres and replace each by one positive and one negative parallel of framing $`-(n-1)`$. For this actual $`2n`$-component non-split graph link, $`X=Y`$ is a simplicial tree, with root the $`n`$-annulus system. For $`r>1`$, the catalogue and parent algorithm above hold with:

- $`B`$ any nonempty subset of $`\{1,\ldots,n-1\}`$;
- $`z\in\mathbb Z^{n-1}`$;
- $`L_i=d\,1_{i\in B}+2rz_i`$, $`L_0=0`$;
- the edge condition $`|sL_i-rM_i|\le1`$ for every port.

For $`r=1`$ there is no $`B,d`$ choice and all axes are zero.

**Proof.** The central equations are $`(J-nI)x=0`$, with primitive solution $`\eta(\mu_i)=1`$. Its fibre has one boundary at each port and
```math
\chi(R)=n(2-n),\qquad
g(R)=(n-1)(n-2)/2.
```
The fibre intersections are $`n`$, so all interfaces are genuine. The signed classification, the two-axis proof, the primitive relative phase quotient, and essential assembly are unchanged. Every horizontal reduced vertex with $`r>1`$ uses exactly two axes, partitioning the leaves into two nonempty groups.

For any pair in one group, the formal four-hole diagram contains $`r-1`$ parallel essential closed curves. Thus a neighbour with sheet number greater than one preserves that pair and its relative integer. Since both partitions have exactly two nonempty groups, preserving all same-group pairs forces preservation of the whole partition. It also fixes all within-group phase differences.

Choose $`0\notin B`$ and $`b\in B`$. A sector fixes $`z_i`$ for $`i\notin B,i\ne0`$, and fixes $`z_i-z_b`$ for $`i\in B,i\ne b`$. Its remaining slope is
```math
p/r=(d+2rz_b)/r.
```
The four-hole matching at ports $`0,b`$ gives its Farey edges; all other leaves are duplicates with fixed relative phases. The lifting argument gives sufficiency simultaneously at every port. A horizontal vertex with $`r>1`$ belongs to just one sector, and has the unique lower parent (7.1). A vertex with $`r=1`$ has parent $`A`$. The same maximum-denominator argument proves the global tree and the same global potential proves $`X=Y`$. ∎

More generally the proof gives the following usable substitution lemma.

**Bundle-port lemma.** In an actual non-split exterior, replace the central block by a connected, actual-free fibre cluster $`C`$ with $`n\ge3`$ labelled ports and $`\Phi|_C=0`$. Assume: (i) every efficient nonempty cut of a spanning system in $`C`$ is a balanced collection of parallel fibres of one fixed primitive bundle; (ii) its connected fibre has negative Euler characteristic and exactly one boundary on each port, of the attached leaf-fibre slope; (iii) positive phase maps in this class have the relative boundary quotient $`\mathbb Z^n/\mathbb Z`$, with the fixed-slope ordinary comparison and simultaneous positive boundary extension; and (iv) every attached branch is the two-actual pants product used above. Empty cuts are allowed. Then the same catalogue, sectors, tree, distance and contraction hold.

**Port signs.** By (ii) the connected positive fibre meets port $`i`$ with a sign $`\sigma_i\in\{1,-1\}`$ relative to the actual positive tether of leaf $`i`$. Orient the class so that $`\sigma_0=1`$, and put $`\rho_i=(1-\sigma_i)/2`$. At a leaf with $`\sigma_i=-1`$ the defect condition (3.2) reads $`\epsilon_{a_i}=\sigma_i`$ and $`\epsilon_{a_i+r}=-\sigma_i`$, and its term in the Fourier identity is $`4\sigma_iz^{a_i}`$. The catalogue, the two-axis argument, the allowed parity classes of the four-hole diagrams and the parent algorithm are therefore used in the re-encoded coordinates
```math
\widetilde a_i=a_i-\rho_ir\pmod{2r},\qquad
\widetilde L_i=L_i-\rho_ir .
```
That is, a leaf with $`\sigma_i=-1`$ uses its actual negative tether as the reference for the central positive axis, while retaining the identity of every actual boundary. All defects are then positive, and
```math
P_{\widetilde a_i}=P_{a_i},\qquad
s\widetilde L_i-r\widetilde M_i=sL_i-rM_i .
```
Carries from the integer lift are absorbed into the original phase integers. The ordinary quotient is still $`\mathbb Z^{n-1}`$; $`\rho`$ is fixed data of the cluster and its class, not a vertex state. The reflections, joint disjointness, actual orientations and the original $`\Phi`$ are unchanged, so the tree and width arguments apply verbatim. Without this re-encoding the literal axis catalogue can fail. For three Hopf support fibres with framings $`(0,0,2)`$, each replaced by one positive and one negative parallel, the class $`\eta(\mu_i)=(1,1,-1)`$ gives port signs $`(+,+,-)`$; at $`r=2`$ with central word $`(+,+,-,-)`$ the actual positive tethers sit at three different positions. In Theorem 10 and in §10.2 every $`\sigma_i=1`$.

The proof just given, read in these coordinates, uses exactly these four properties and hence proves the lemma. It can be applied after replacing a central block by another cluster for which (i)–(iii) have been proved; the other blocks need not be a single Seifert piece. It is not a claim that arbitrary graph clusters satisfy (i). The explicit Hopf stars prove an unbounded multiport family without any such extra premise.

### 10.1. A finite central-tree certificate

Here is a sufficient test for such substitution, including partial horizontal clusters. Let $`C`$ be an actual-free tree of genuine Seifert blocks with negative orbifold Euler characteristic, with the same two-actual pants leaves at its outer ports and $`\Phi|_C=0`$. For every nonempty connected central subtree $`D`$, form the rational vector space $`W_D\subset H^1(D;\mathbb Q)`$ of classes killing:

- the attached leaf fibre on an outer port of $`C`$ lying in $`D`$;
- the neighbouring central Seifert fibre on an internal frontier of $`D`$.

Require that every proper $`D`$ has no member evaluating nontrivially on all its block fibres. Require that $`W_C`$ is one-dimensional, generated by an integral primitive $`\eta`$ nonzero on every block fibre, whose restriction to each outer torus is primitive. These are finite rational linear tests over the connected subtrees. The port signs $`\sigma_i`$ are the signs of the restrictions of $`\eta`$ at the outer tori relative to the actual positive tethers, and the re-encoding above is used whenever they are not all positive.

These conditions imply the bundle-port hypotheses. Indeed a maximal horizontal cluster in an efficient system gives a member of $`W_D`$ nonzero on every block fibre. Choose a local positive primitive horizontal class at a root and propagate its sign across the horizontal interfaces. Since the block graph is a tree, there is no sign holonomy. In a connected subassembly every visited local horizontal piece consequently has the same propagated sign. A horizontal piece meets every port, so the subassembly visits all of $`D`$; its primitive dual is nonzero on every block fibre. This argument does not use the possibly zero total local class. A frontier is adjacent to a vertical block, whose fibre supplies its slope. Thus no proper $`D`$ is possible.

If any horizontal piece exists, the entire central tree is horizontal, in the unique primitive class $`\eta`$ up to sign. Local Seifert submersions with this class exist by averaging a closed integral representative over the locally free circle action: its contraction with the fibre vector is the nonzero period $`\eta(h_v)`$. Straighten their boundary maps to the identical linear torus restrictions; their real collar differences and the global class $`\eta`$ let these maps glue to a bundle. Its fibre is connected by primitivity and has one boundary on each outer port. Its Euler characteristic is the sum of negative local covering Euler characteristics. The actual total central class zero forces balanced signs. If no horizontal piece exists, genuine fibre mismatch at every central and outer edge forces every trace empty; closed remaining components are excluded. This proves (i)–(ii).

Positive maps in the fixed class differ by global real functions. The local positive derivative conditions, with the signs of the block fibres chosen using $`\eta`$, are convex; matching torus collars use the same primitive quotient maps. Prescribed outer boundary constants extend by base functions constant on the internal collars. Thus the relative boundary components are $`\mathbb Z^n/\mathbb Z`$, and arbitrary increasing port maps extend by the positive collar construction of §5. Fixed-slope ordinary comparison applies to the internal tori as well. The absolute boundary-torus detector (4.4) applies to this whole connected cluster, since its boundary fundamental-class sequence again has only the one diagonal relation; the attached tether loops again have zero winding. Hence these components remain distinct under arbitrary ordinary isotopy. This proves (iii), and proves the certificate.

The proper-subtree test is necessary for this sufficient argument. The fact that the whole boundary-value kernel has dimension one alone would not exclude a smaller balanced horizontal cluster returning through vertical central blocks.

### 10.2. An actual two-central-block family

The certificate is not confined to a one-block centre. Start with $`n\ge3`$ regular Hopf fibres and cable the zeroth one by $`(p,q)`$, with winding $`p\ge2`$, $`q\ge1`$, and $`\gcd(p,q)=1`$. Denote the cabled support by $`K`$. Replace each component of $`K`$ by one positive and one negative parallel, with framing minus its support linking row sum. Thus the cable component has framing $`-p(n-1)`$, and the other components have framing $`-(p+n-2)`$.

The centre consists of a Hopf $`n`$-pants block $`H`$ and a cable block $`W`$. Their fibre intersection is $`|p-q|\ne0`$. Put $`\eta(\mu_j)=1`$ at every support component. This is an auxiliary class; the actual six- or $`2n`$-component link class still restricts to zero on the centre. With old coordinates at the cabled port,
```math
\mu_{\rm old}=p\mu_{\rm cable},\qquad
\lambda_{\rm cable}=p\lambda_{\rm old}.
```
The fibre evaluations in $`H,W`$ are respectively
```math
p+n-1,\qquad p(q+n-1),
```
and all outer interfaces are genuine. The central linking matrix has positive off-diagonal entries $`p`$ at the cable and one elsewhere. Its row-sum boundary equations are a connected weighted Laplacian, with kernel exactly the constant vector. Thus $`W_C=\mathbb Q\eta`$.

There are just two proper connected central subtrees to check. In $`H`$, write $`x`$ at $`\mu_{\rm old}`$ and $`y_j`$ at the other meridians. The outer equations give
```math
x+\sum y_j-(p+n-1)y_i=0.
```
Hence all $`y_i=y`$ and $`x=py`$. The cable-fibre frontier then gives $`p(q+n-1)y=0`$, so the class is zero. In $`W`$, the outer cable equation gives $`\eta'(\lambda_{\rm old})=(n-1)\eta'(\mu_{\rm cable})`$; the Hopf-fibre frontier gives $`(p+n-1)\eta'(\mu_{\rm cable})=0`$, again zero. The certificate applies.

The connected auxiliary fibre has $`n`$ boundaries and
```math
-\chi(R)=(p+n-1)(n-2)+(p-1)(q+n-1).
```
For $`n=3,p=2,q=1`$, it has genus three and three boundaries. The resulting six-component link has five genuine JSJ blocks, two of them central and actual-free. Its $`X=Y`$ is the same explicitly classified tree, with $`\chi_-(S)=2r[-\chi(R)]`$.

This gives a concrete central-cluster substitution beyond the original Hopf star. Further substitutions can be certified by the same finite subtree test; unrestricted gluing of two resonant clusters is not asserted.

What prevents unrestricted iteration is now identifiable. Multiple auxiliary modes, including a proper horizontal subcluster returning through vertical central blocks, need not share one circle and one outer phase quotient. If a fibre has several boundaries on a port, the formal projection is no longer a two-arc matching. If a branch has more actual boundaries, its defect sum replaces the single term $`4z^a`$ in the two-axis equation, and the line-circle argument no longer bounds the number of axes by two. An actual-free vertical return packet can also lack the tether that froze its port loop in §4. No repeated-axis barrier or unique lower parent has been proved for these configurations.

The finite certificate is sufficient only: failing it is not a noncontractibility result, and a permitted algebraic mode need not have a reduced global realisation. These remaining cases, and hence all graph links, remain open here. Neither disconnected local complements nor noncoherent signed traces are additional assumptions or outstanding gaps in the family proved above.

## 11. Computational cross-checks and negative tests

The accompanying standard-library script checks the signed order model independently against the determinant criterion. The former retains a common central cyclic order at all three ports and both relative integer phases; it does not identify a cyclic clique with a geometric simplex by definition.

For a family with sheet numbers $`2r_i`$, a port-zero order has four consecutive packets: positive tethers, the first return ends, negative tethers, and the reverse matching of the first return ends. At another port its integer lifted axes specify the same four packets in the lifted common order. Its return partners are
```math
j\longmapsto 2L_i+2r_i-j.
```
The $`+2r_i`$ is necessary: matching only residues would lose a full twist. Exhausting packet shuffles is a finite disjointness test. Its necessity and sufficiency are also the normal-form construction in §§3–5. For a pair it is cross-checked against (6.1); a witness yields the signed central potential and its width.

The diagnostics `scripts/part11_star.py` and `scripts/part11_certificate.py` reproduce the following checks. The default packaged run performs the baseline order comparison for $`r,s\le6`$ (21,609 queries); the enlarged rows for $`r,s\le8`$ come from a separate call of the same function `order_crosscheck(8,1)` in `scripts/part11_star.py`, which can be made by importing that file without running its main routine.

The first checks all normal types with $`r,s\le6`$, and both relative phase integers between $`-1`$ and $`1`$. This contains every possible relative phase of an edge: a relative turn of absolute value at least two separates its positive packet lifts by more than one whole common circle. The test includes nonedges and equal classes, not just predicted neighbours.

| Check | Exact extent / result |
|---|---|
| Balanced sign words and all positive axes | 66,196 words, $`r\le9`$ |
| Independent packet-order / determinant queries | 21,609, all equal |
| Enlarged packet-order / determinant queries, $`r,s\le8`$ | 74,529, all equal |
| Enlarged distinct positive pair queries / minimum witness width | 180 / always one |
| Distinct positive pair queries / minimum witness width | 96 / always one |
| Parent depth / signed prefix oscillation | 79,993 types, $`r\le256`$, all equal |
| Original unbounded-genus family | 128 parameters, all at distance two |
| Finite phase-and-complexity truncations | 15, all $`H_1=H_2=0`$ |
| Exact pillowcase coordinates, including five full-turn values | 8,475, $`r\le64`$ |
| Explicit lattice construction of parent-edge port orders | 5,082, $`r\le64`$, all width one |
| Multiport component graphs | 7,383, three to seven ports |
| Four-to-six-port order queries | 30,397, all equal to the arithmetic predicate |
| Two-central-block rational certificates | 1,720 |
| Finite two-interval exchange tests | 11,869 |

The five largest-phase-box truncations have the following integer homology. The phase box is $`|z_1|,|z_2|\le2`$; the root is included.

| $`r_{\max}`$ | vertices | edges | $`(b_0,b_1,b_2)`$ | vertices after parent closure |
|---:|---:|---:|---:|---:|
| 4 | 626 | 587 | (39,0,0) | 637 |
| 8 | 2,276 | 2,199 | (77,0,0) | 2,287 |
| 16 | 8,276 | 8,123 | (153,0,0) | 8,287 |
| 32 | 32,576 | 32,271 | (305,0,0) | 32,587 |
| 64 | 127,076 | 126,467 | (609,0,0) | 127,087 |

Each parent closure has one fewer edge than vertices and homology $`(1,0,0)`$. Its extra vertices are the eleven phase-boundary ancestors omitted by the finite box. The boundary map $`C_1\to C_0`$ is computed by the full determinant-neighbour list, independently of the parent list; its rank is vertices minus connected components. The resulting forests have zero integral $`H_1`$, as well as zero $`H_1`$ over every field. There are no triangles or higher simplices, hence $`C_2=0`$ and $`H_2=0`$.

All $`H_1,H_2`$ persistence maps are consequently zero. The additional explicit $`r\le16`$ checks for phase inclusions $`Z=0\to1`$, $`1\to2`$, and $`2\to3`$ show that their reduced $`H_0`$ maps are also zero, even though the larger box has new peripheral components. Thus the observed disconnectedness is a phase-truncation effect.

There is no four-cycle in these finite graphs; the theorem excludes one in the entire complex. Vertex links can be disconnected, as they are in any branching tree. Such a link is not a noncontractibility certificate for the ambient complex.

The enlarged run has 544 complete common-order witnesses, including 91 equal-class queries; the other 180 positive queries are between distinct vertices. Witnesses count labelled order presentations, not isotopy classes of their embedded unions. Its search uses a cached index of necessary consecutive endpoint packets, retaining their integer lift differences. The unpruned four-packet predicate remains in the checker. Complete witness sets agree for 5,625 queries, with 392,328 individual slow/fast port comparisons; the entire original $`r,s\le6`$ numerical baseline, including all witnesses and homology outputs, is unchanged. The arithmetic determinant criterion is not used to prefilter the independent order search.

Finite tests do not prove the ordinary comparison, the geometric lifting, or contractibility; those are the arguments above.

## 12. Inputs

- [Part 10, §11.6–11.7](part10-3.md) for the actual link and signed diagrams; the needed calculations have been re-proved here.
- [Part 7](part7.md), signed local classification and Theorem D; no general contractibility conclusion is imported.
- [Part 8](part8.md), ordinary phase and tree arguments as a comparison; the new step here is the multiport repeated-axis barrier.
- The repaired fixed-slope product comparison [Lemma 31.2](graph-ordinary-annuli.md), with the explicit restriction in §4 that its old empty-zero-block inference is not used.
- Banks, arXiv:1109.0965v1, Proposition 2.4, Proposition 4.10 and the explicit §10 extension, for the cyclic convention and class minimum.
- The competition paper, §2, only for the literal exchange axiom in §9; its knot minimal-surface argument is not applied to disconnected link surfaces.

The repeated-axis barrier resolves the multiport resonant cancellation for this star and the families of §10.

[Overview](../README.md) · [Previous page](part11.md)
