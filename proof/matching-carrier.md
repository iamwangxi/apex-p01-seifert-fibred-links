# 6. Compatible rounding on fixed matching polytopes

[Overview](../README.md) · [Definitions](objects.md) · [References](../sources/bibliography.md)

For a finite embedded multiarc $`G`$ on $`P`$, assume its edges are distinct positive-negative proper classes and it contains a matching of all actual circles. The auxiliary circles are marked but have no incident edges. Cap actual circles by radial stars and fill auxiliary circles **for the spherical circulation calculation only**. Connected regions before and after capping correspond: each star sector attaches to one old boundary interval, and each unused cap fills a hole of one existing region. The cone positions and proper arc identities remain part of the model. Distinct edges separated by a cone are not identified by filling it.

Direct edges negative to positive. For connected spherical regions set

```math
(D_Gu)_e=u_{\ell(e)}-u_{r(e)},\qquad
P_G=\{w\ge0:\ \sum_{e\ni i}w_e=1\text{ for each actual }i\}.
```

**Theorem 6.1.** The following six fixed-graph conclusions hold for every such $`G`$ in every classified $`k=0`$ exterior: one face-potential constant, legal common rounding, a true output simplex, continuous choice-independent decoding, zero-face agreement across graphs, and exact recovery of any true simplex. The matching subcomplex of $`G`$ triangulates $`P_G`$.

**Proof.** We prove all six conclusions directly.

**Lemma 6.2 (spherical circulation).** For a finite graph embedded in the oriented sphere, every real edge circulation $`c`$ is $`D_Gu`$ for a region function $`u`$. The kernel of $`D_G`$ consists of the common constants. If $`c`$ is integral, the root-normalised $`u`$ is integral.

**Proof.** Choose a spanning tree in each graph component. Each non-tree edge, together with the unique tree path between its ends, gives an oriented simple cycle. Parallel edges can give a simple two-edge cycle. These fundamental cycles span all circulations: subtract the multiple of each fundamental cycle needed to kill its non-tree edge, leaving a circulation supported on a forest. A forest circulation is zero, by successively removing leaves. This argument also shows directly that a bridge carries zero circulation.

By the Jordan curve theorem, an oriented simple cycle separates $`S^2`$ into two disks. Assign value one to every $`G`$ region on its left side and zero to every region on its right side. Every connected $`G`$ region lies wholly on one side. The resulting potential has difference one along a cycle edge traversed in its cycle direction, minus one if traversed oppositely, and zero along every other edge. Thus its difference vector is the cycle circulation. Taking the same linear combination as the cycle decomposition produces $`u`$. Subtract its root value. No region has been filled by a separate disk in this argument; a region with several boundary curves is assigned just one value.

For uniqueness, the region adjacency graph across **all** edges is connected. Indeed, a path on the sphere between two interior region points can be chosen to avoid finitely many vertices and cross edges transversely finitely often. If $`D_Gu=0`$, its value is unchanged at every such crossing, so it is constant on all regions. This is one global constant even when $`G`$ is disconnected. If $`c`$ is integral, following a path in this connected dual graph from the root shows every $`u_f`$ is an integer. ∎

For $`c=w-m`$, the unit incident sums make the difference a circulation, so a reference matching indicator $`m=\chi_M`$ gives $`w=m+D_Gu`$ with one root-normalised potential.

Write $`\mathrm{osc}(v)=\max v-\min v`$. For matching subgraphs $`A,B`$, write $`\chi_A-\chi_B=D_Gv`$. Delete unused edges. Their jumps are zero; the potential descends through every actual region merger with its full range unchanged. Each new region contains an old open region. Common arcs stay cut frontiers, not internal crossing edges. On the complete $`B`$-complement graph the descended $`v`$ satisfies exactly the unit equations across $`A`$-only walls. Theorem 5.3 therefore gives the essential new geometric interface

```math
\delta(A,B)=\mathrm{osc}(v).
```

No cone region, non-disk region or independent graph component has been discarded in this identification.

For $`0\le\theta\lt1`$ let

```math
q_f^\theta=\lfloor u_f+\theta\rfloor,\qquad
m_e^\theta=m_e+(D_Gq^\theta)_e.
```

The bounds $`0\le w_e\le1`$ mean $`-m_e\le u_\ell-u_r\le1-m_e`$. If $`L\le a-b\le U`$ with integral $`L,U`$, monotonicity gives $`L\le\lfloor a+\theta\rfloor-\lfloor b+\theta\rfloor\le U`$. A common floor shift therefore preserves the displayed integer-endpoint bounds, so $`m_e^\theta\in\{0,1\}`$, even at a threshold. Sector differences telescope at each actual vertex, preserving its unit sum. Thus every output is a legal matching vertex by Theorem 4.1. Between two ordered thresholds the floor difference is a face vector taking only zero and one. The displayed class-distance identity gives distance at most one between outputs, so their distinct vertices span a flag simplex. Define its finite barycentric average

```math
S_G(w)=\int_0^1[M_\theta]\,d\theta.
```

Writing $`u_f=k+a`$, $`0\le a\lt1`$, the floor is $`k`$ for length $`1-a`$ and $`k+1`$ for length $`a`$. Thus the identity $`\int_0^1\lfloor u_f+\theta\rfloor\,d\theta=u_f`$ gives the exact edge expectation $`\int_0^1\chi_{M_\theta}\,d\theta=w`$.

Changing reference subtracts an integral face potential and cancels pointwise in the floor formula. Changing root adds a common real constant, rotating the threshold circle and preserving the barycentric average. The decoder depends only on the embedded proper classes with all unused holes retained. With root and reference fixed, the potential is affine and uniformly bounded on $`P_G`$ (a simple dual path gives bound $`|\mathcal R_G|-1`$). Subdivide by the finitely relevant $`u_f=k`$ and $`u_f-u_g=k`$ hyperplanes. Threshold outputs are fixed and interval lengths affine on each cell. Colliding thresholds enclose intervals of vanishing length; every positive-length limiting interval retains the same output. Finitely many matching vertices make this ordinary continuity in a finite realisation, including lower-dimensional faces.

If $`w_e=0`$, its integral jump forces $`m_e^\theta=0`$ for every threshold. Switch to one of those supported matchings as reference. Now both indicators at the zero edge vanish, so its two face values agree. Delete it, descend through real region mergers and round the descended equal values. The retained output agrees pointwise. This covers an old reference using a zero edge, bridges and mergers containing one or both marked cones. Two graph rules on a common coordinate face both reduce to the same positive-support multiarc; ordinary joint straightening gives the same embedding and hence the same rule. Edges outside that support may cross.

Finally let $`\sigma=\{A_0,\ldots,A_k\}`$ be a true simplex of matchings in $`G`$. Their root-normalised integral potentials have pairwise oscillation at most one and root difference zero. Each difference is wholly in $`\{0,1\}`$ or wholly in $`\{-1,0\}`$, so the potentials form a coordinatewise chain. Use its minimum as reference. Every coordinate is now zero or one. In the potential for $`w=\sum_i\lambda_i\chi_{A_i}`$, a coordinate first turning on at index $`j`$ has value $`\sum_{i\ge j}\lambda_i`$. Common rounding therefore produces precisely $`A_i`$ for an interval of length $`\lambda_i`$. Thus

```math
S_G\left(\sum_i\lambda_i\chi_{A_i}\right)=\sum_i\lambda_i[A_i].
```

Zero coefficients remove zero-length intervals. This exact recovery and the edge expectation make the affine edge map and $`S_G`$ inverse homeomorphisms. Distinct matching subsets are distinct vertices by Theorem 4.1, so the claimed triangulation is genuine. ∎

This proof covers disconnected graphs, forced bridges and non-disk regions directly. It does not require extending Propp's printed connected/non-forced-edge hypotheses, and it uses no non-unit d-factor theorem. All actual demands stay one.
