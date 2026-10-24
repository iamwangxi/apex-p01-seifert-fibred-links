# 17. The zero block with one coherent multiple port

[Overview](../README.md) · [Definitions](splice-objects.md) · [Block lemmas](splice-planar-blocks.md) · [References](../sources/bibliography.md)

### 17.1. Classification and the local whole complement

For the mixed case, ordinary diagrams in $`\mathcal A(P,\sigma,q)`$ are a full vertex model for the annular systems in $`P`$ with the prescribed actual curves and $`q`$ coherent fibre curves on $`T`$. All annuli connect different tori and have an actual end. In particular they are essential. Their complete complements are connected by the cut argument above; $`\phi_P`$ is primitive and every loop in a complement has zero $`\phi_P`$. The whole open complement therefore has one homeomorphic lift, up to one deck translation.

Put two diagrams in ordinary normal position: common classes coincide, other crossings are transverse, and ordinary bigons and free-endpoint half-bigons are removed. A fixed hyperbolic metric supplies canonical representatives. Form the connected signed region graph inside the entire $`b`$ complement, crossing only $`a\setminus b`$ with positive unit step. Do not cross $`b`$ or add an internal edge at a common arc. Its integral potential $`H_P`$ is unique up to one constant.

### 17.2. Class minimum despite a separating JSJ multicurve

For $`q>1`$ the local prescribed boundary multicurve separates the torus $`T`$. We therefore **do not** cite the standard PS setup for the local block without qualification. Instead use the following connected-complement version of its Section 3 proof.

**Lemma 17.1.** For the annular classes just specified, the local minimum complete-complement width is

```math
\Delta_P(a,b)=\mathrm{osc}(H_P)=\max H_P-\min H_P.
```

The minimum is over all local ambient representatives, with actual and JSJ curves allowed to slide as prescribed.

**Proof.** The normal annuli are almost transverse and have no relative product region. A noncommon product face is a fibre subannulus. Its projected path gives an empty ordinary bigon, an empty half-bigon at an actual circle or at $`J`$, or equality of two full proper arc classes. These are excluded by normal position. Each annulus has an actual end used only once in each system. Therefore a common annulus cannot be paired with a different component using both its ends, even though other components may use $`J`$. The usual coincident-face argument excludes two distinct product faces within the same common annulus: an uncollapsed side cannot use its one boundary circle twice, and all-collapsed frontiers force identical faces. There is no boundary product disk. This proves the same local simplified-intersection statement as Lemma A.2 in [the planar-block appendix](splice-planar-blocks.md), without requiring unit demand at $`J`$.

Now use PS's stated Sakuma Proposition 3.3 **directly** on closures of complete complementary blocks in the local cyclic cover. The ambient cover is orientable, irreducible and boundary-irreducible. Its frontiers are unions of lifts of essential annuli, hence incompressible and boundary-incompressible. They have the lifted almost-transverse, simplified position, as in the lifting observation in the proof of PS Proposition 3.2. That covering observation concerns essential frontiers and relative products, not the nonseparation of the original boundary multicurve. In the product case it can also be checked by lifting normal ordinary arcs: there are no geodesic bigons or half-bigons, noncommon full arcs cannot become properly homotopic, and a parallelism between distinct translates of a common arc would identify powers in the distinct endpoint peripheral subgroups. Those ordinary boundary subgroups are noncommensurable; only the same lift can be common.

Choose a representative $`b'`$ attaining the local integer minimum with $`a`$ fixed, with extreme indices $`m',r'`$. Fixing $`a`$ loses no minimum: transport any minimising pair by an ambient isotopy of its first member to this $`a`$. Its complete block is disjoint from every $`a`$ block outside this interval. Isotopy of $`b`$ to $`b'`$ gives an isotopy of the selected complete blocks. Proposition 3.3 forces the complete block of the normal $`b`$ to be disjoint from those same outside $`a`$ blocks. Its range is at most $`r'-m'`$; the reverse inequality is the definition of the minimum. This is precisely the Section 3 argument, using independently verified connected complete complements, not the failed local nonseparating-boundary hypothesis.

Finally, on the one complete $`b`$ lift, crossing a positive $`a`$ wall changes the $`a`$-block index by one. Connectedness gives exactly $`H_P`$. Every open region attains its index and every nonempty open-block intersection has a point in a region. Frontier contacts add none. This proves the formula. ∎

An A-only wall gives a unit jump. Thus the normal range is zero exactly when all arc classes are common, equivalently when the joint diagrams agree. Distinct diagram classes have $`\Delta_P\ge1`$, without assuming a local PS metric theorem for the separating boundary condition. The connected unit-step graph also attains every integer between its extremes.

The formula concerns the entire annular system, not independent shifts of its components. A common arc remains a cut frontier. No graph-distance identity or PS projection is used.
