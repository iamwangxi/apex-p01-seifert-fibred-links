# Part 9. Parallel clusters of connected sums of torus knots (continued)

[Overview](../README.md) · [Previous page](part9-3.md) · Part 9, page 4 of 4

## 11. Further replacement interfaces and what remains open

The complete parallel-cluster theorem uses three special facts: a single companion port, a common **linear** packet for every disjoint companion family in one sector, and a zero outer-loop detector. A general graph-manifold link can have a region incident to several different companion classes or to several ports. An empty return could then meet two negative faces of a region that also has positive faces; it would not identify a whole one-sided chamber that can be resolved. Uniformly one-sided chambers still have disjoint boundary-piece sets, but the exhaustive repair assertion of Lemma 10.1 is missing. A signed count alone does not supply that assertion.

### 11.1. More balanced square-knot parallels

The structural and core arguments are not specific to four actual holes. For $`2n`$ zero-framed square-knot parallels with $`n`$ signs of each kind, replace $`B`$ by the disk with $`2n`$ actual holes. The same companion catalogue and zero-loop proof apply. Pattern counts become $`(2n-t)/2`$ actual annuli and $`(2kq-t)/2`$ returns, with even $`t>0`$, and

```math
G=kq+c-n,\qquad c\le n.
\qquad\text{(11.1)}
```

The ordinary gluing coordinate is still the single signed-configuration integer. Each fixed two-boundary sector is the matching complex on a sphere with $`2n`$ actual holes and two unused auxiliary holes. The relative annular carrier, single-piece core, larger sectorwise core, and filtered cyclic comparison have the same proofs. Section 10 now contracts all the signed sectors, not only these cores.

The cyclic descent also extends, without assuming at most two spanning components. Here is a useful consequence of (7.1). If a geometric neighbour $`R`$ has strictly smaller additive complexity than $`S`$, apply the Part 7 retraction to $`x_t=(1-t)[S]+t[R]`$. For small $`t>0`$, its image has complexity strictly smaller than that of $`S`$ and still has positive barycentric coefficient at $`S`$: the image lies in one fixed finite carrier and tends to $`[S]`$. Some other support vertex has smaller complexity; since that support is a simplex of $`X`$, it is a cyclic neighbour of $`S`$. Every output is made from whole components of $`S`$ and $`R`$, so geometric compatibility with an additional fixed disjoint family is preserved.

Apply this observation with $`q=-\chi/(2k)`$ to the end-resolution and compression proof of Lemma 8.3. Thus every cancellation vertex has a lower-$`q`$ cyclic neighbour for arbitrary $`n`$, and (1.4) still holds. In particular, the distance to the annular set is exactly $`q`$ for every coherent packet. The subsequent chamber-closure proof gives the stronger ordinary parent and complete sector contraction.

### 11.2. An iterable two-boundary replacement lemma

The following states the precise reusable interface, including its ordinary-loop hypothesis.

**Theorem 11.1 (fixed two-boundary insertions at several ports).** Suppose an actual non-split $`S^3`$ link exterior has a decomposition

```math
M=(S^1\times B)\cup_{T_1\sqcup\cdots\sqcup T_r}
(Q_1\sqcup\cdots\sqcup Q_r),
\qquad\text{(11.2)}
```

where $`B`$ is planar with negative Euler characteristic, some boundary circles are labelled actual boundaries, the other $`r`$ circles are companion ports, all actual spanning slopes are the displayed fibre, and the spanning class vanishes on every $`Q_j`$. Assume the gluing tori are incompressible. No abstract gluing data are being asserted to realise a link in $`S^3`$.

At each port fix an essential separating positive-genus two-boundary companion $`F_j\subset Q_j`$ of the prescribed port slope. Require the following packet property: every finite disjoint system in its unoriented ordinary class is jointly parallel, and every ordinary loop of such a system has zero port-configuration winding. Let $`Y_{\mathbf F}`$ be the full subcomplex on the vertices whose $`Q_j`$ cuts are empty or parallel copies of $`F_j`$, with arbitrary individual orientations, and whose remaining cuts are essential vertical pattern annuli. Then $`Y_{\mathbf F}`$ is a planar oriented matching complex with two unused auxiliary holes for each companion port. It and its induced cyclic subcomplex are contractible.

**Proof.** The ordinary product comparison of Section 2.1 applies at the whole port collection: all the trace slopes are already fixed, an innermost returning torus annulus would be a forbidden same-port parallel cut piece, and the injected torus groups killed by the spanning class exclude the fibre exception. Replace $`Q_j`$ by a pair of pants $`V_j`$ and $`F_j`$ by its essential returning arc, independently at every port. The resulting surface $`B\cup_jV_j`$ is planar. Minimum position at the gluing circles gives exactly the efficient cut pieces, and the absence of closed components is exactly the absence of closed matching curves.

The local packet hypotheses give the same ordered signed packets and zero loop images as in Section 6.3. The pattern loop image is zero at every active port as well. For a distinct-end annulus this follows from the independent rational classes of its two boundary circles. For a returning annulus, close its base arc around a nonempty proper subset of the other boundary circles. Its word is not commensurable with the chosen port word in the planar free group; following an ordinary loop would make a nonzero port power centralise that word, which is impossible. Taking a power handles finite permutations. Thus the configuration bookkeeping (5.1), now over a product of active-port configuration circles, agrees on both sides of the replacement. The same argument with colours proves compatibility with restriction to finite subfamilies and to actual-bearing components.

Each companion packet has the same linear complementary-region incidences as its arc packet. Hence the geometric dictionary and whole component-wall data agree. The planar matching phase argument contracts the geometric complex. The Part 7 retraction stays within the specified class of components under recombination, so it restricts to the induced cyclic subcomplex, proving that subcomplex contractible too. ∎

The square-knot two-boundary sectors satisfy the packet hypotheses by Sections 3--4. This replacement dictionary does not extend by replacing a connected multi-boundary piece with several disconnected arcs. The chamber method does, however, give the following fixed-packet extension.

**Theorem 11.2 (several fixed one-port packets).** In the setting of (11.2), allow each $`F_j`$ to have any positive even number $`2k_j`$ of port boundaries, while retaining essentiality, separation, positive genus, joint parallelism and zero ordinary port-loop winding. Then the full subcomplex $`Y_{\mathbf F}`$ on these fixed companion classes, and its induced cyclic subcomplex, are contractible. The cyclic subcomplex strongly deformation retracts onto the pure pattern-annular cyclic subcomplex. The same conclusion holds with any fixed upper bound on the total number of companion pieces.

**Proof.** Fix an order of the companion ports and an end of each reference packet. For a vertex $`S`$, choose its first nonempty port and its first piece there. Use the normal side containing that end region. Form the finite collection of one-sided original chambers at **all** ports, and seed the closure at the chosen end. Their boundary-piece sets are disjoint, also across ports.

Every bad pattern return is at one port and bounds a disk containing no other boundary hole of $`B`$. The original essential pattern system cannot enter that disk. Lemma 10.1 therefore identifies a same-side original chamber at that port. The path-composition proof of monotone enabling and unique finite closure is unchanged. The final actual-bearing system has essential cuts at every torus. Only the original connected component containing the seed is changed, so the shared-component argument still gives a cyclic edge. The total piece count decreases, and each individual port packet is retained as a subpacket.

The ordinary product comparison preserves the port collection. The local zero-loop hypotheses preserve each reference end and the piece order. Hence this is an ordinary parent with a definite retained subpacket at every port. It remains compatible with a disjoint family whenever its seed is first in that family's packet at the chosen port: an enabled empty disk excludes traces of all other family members at that port, so its repair chamber is empty of them too.

A vertex's successive events are labelled by the seed port and the first retained piece there. These labels increase lexicographically: no port count can increase, and the parent always chooses the first active port. For a cyclic simplex use the ordinary coloured packet orders at all ports, and merge events lexicographically by port and then by the indicated piece order. The port orders are jointly realisable by one Part 7 component-wall phase family. Re-rooting its potentials only rotates all its phase intervals; the relative order of coloured copies within a band is unchanged. Their face restrictions are therefore compatible simultaneously at every port.

At each event the selected piece is first in the current family at its port, so the relative parent lemma applies. The fixed vertical subdivisions and affine-height slabs of Section 10.4 now give a face-compatible prism ending at an annular family. Compose with Part 7 to obtain the asserted strong deformation retraction. The total piece count is component-additive and decreases along every trajectory. Formula (7.2) therefore gives the same bounded-count conclusion. ∎

These theorems apply to fixed ordinary packet types at several **one-port** invisible companions on a zero-evaluation pattern block. They do not assert that every vertex of the surrounding link belongs to that fixed-type subcomplex, and they do not resolve an individual horizontal cluster with several independent external ports or several nonparallel cut classes in one companion. No ambient all-pair distance formula outside the specified sector is asserted for (11.2).

**Remark 11.3 (the port count in $`S^3`$).** In the actual $`S^3`$ setting of (11.2) the number $`r`$ of companion ports is at most one. On each actual boundary torus the fibre $`h`$ is the spanning slope, of the form $`\pm(\lambda_i+b_i\mu_i)`$, so it meets the meridian once. Meridional filling of every actual boundary torus therefore turns the product block into an oriented circle bundle over an $`r`$-holed sphere without new exceptional fibres. For $`r\ge2`$ its fundamental group is $`F_{r-1}\times\mathbb Z`$ and every port torus is $`\pi_1`$-injective. Each port torus is also injective in its companion piece, by the incompressibility hypothesis, and amalgamation along the ports preserves these injections. The filled manifold $`S^3`$ would contain an injected $`\mathbb Z^2`$, which is impossible. A companion piece cannot carry actual boundary instead, because the spanning class vanishes on it while an actual meridian has value one. Hence the branches of Theorems 11.1–11.2 with several ports are vacuous in $`S^3`$, and their content is the case $`r=1`$. Genuinely multi-port configurations, with one invisible support region and several actual pattern blocks, are treated in Part 12, Theorem I.

### 11.3. Open interfaces

The following issues remain open in this part:

* A class-minimum cyclic distance formula for arbitrary pairs of the data in Theorem 5.1. The special height lower bound and exact family do not supply that formula.
* A replacement for the linear single-packet chamber argument when several nonparallel companion classes occur together. The two-boundary replacement is a surface construction: replacing a connected four-or-more-boundary companion by several independent arcs would change connectivity and the no-closed-component test.
* A general ordinary normalisation compatible with finite families in those multi-class or multi-port configurations. Section 10 supplies one for the single-packet sectors and uses cyclic-simplex prisms to handle intersecting finite subcomplexes. It is not a general all-genus compression-choice theorem. The genus-seven example still proves that simply deleting whole closed components after one raw elementary move is insufficient.
* The analogous ordinary data and compatible reductions for multi-port unanchored horizontal clusters in a general graph-manifold link exterior, and their combination with Part 7, Theorem A and the Sections 29–40 interfaces.

For the parallel-cluster cases, the metric uncertainty is confined to fixed companion sectors. The annular isometry and excursion argument of Section 6.3 apply to every sector, even when its companion has more than two boundaries. Paths between different sectors pass through the annular part. The parent construction supplies finite paths and a contraction, but no geodesicity of arbitrary parent trajectories is asserted.

A compression disk for a raw output can be arranged to avoid a fixed disjoint incompressible family by innermost-circle removal. By itself this does not produce a single ordinary, family-compatible projection. Section 10 avoids that ambiguity by a finite same-side chamber closure whose independence relies on the linear packet. Hatcher's surface-cycle reduction and the taut PS projection theorem do not supply the missing extension to arbitrary graph-manifold assemblies.

More precisely, a general continuation needs three replacements for the present interfaces: an exhaustive description of what an empty return can meet when its region has more than two surface faces; an ordinary multi-port motion quotient with the port motions coupled rather than assigned separate deck constants; and a natural retained-piece or other well-founded event labelling that produces face-compatible schedules when one piece is seen at several external ports. A single-valued ordinary map without this last compatibility is not enough for the prism proof.

Contractibility for all graph-manifold links is therefore not proved here; Theorem 1.9 settles the four-parallel case and all parallel clusters of connected sums of nontrivial torus knots. No noncontractibility counterexample is claimed. Cabling recursion beyond the family stated in (1.5) is not silently included.

## 12. Sources and verification boundary

The topological inputs are the conventions of [Section 1](objects.md) and the ordinary product comparison of [Section 31](graph-ordinary-annuli.md); Hatcher's essential-surface and Seifert classification results (Lemma 1.11 and Proposition 1.12); Banks Proposition 4.2 and Propositions 2.4 and 4.10 together with their explicit all-incompressible extension in Banks' Section 10; Sakuma Proposition 4.9(1)–(2), printed p. 883, in the stated $`IS(L)`$ range; and the **closed** good-aspherical-orbifold statement of Schultens Proposition 25. The necessary orbifold hypotheses and the port-loop normaliser calculation are proved above. The partial-matching phase argument is given here rather than assuming a signed multi-boundary extension of Part 8. Part 7, Sections 2.3 and 9, supply the all-incompressible minimum-position input and the component-wall exact-recovery construction; [class distance](class-distance.md) supplies the planar metric.

The diagnostic `scripts/part9_checks.py` verifies 11,440 pairs of reflection offsets through $`N=64`$, 1,008 signed reference packets, the first 40 explicit distance-family diagrams with all 820 successive reductions, and all four failed raw operations in Section 9, including the absence of a bridge in its incidence graph. `scripts/part9_closure.py` checks 6,547 essential input diagrams, 13,094 end-seeded closures and all 20,880 reachable closure states in its stated ranges. It checks monotone enabling, uniqueness of the terminal selected chamber set, the same-side classification of every bad return, and strict packet decrease. Its hole-side tests use exact boundary-gap crossing parity, not a straight-chord assumption for the newly composed arc. `scripts/part9_gap_orbits.py` checks 28,743 gap-orbit parameter tuples with two to four terminal leaves and $`N\le20`$.

These finite checks do not certify ordinary isotopy, minimum cyclic width, the coloured-order interface, three-dimensional product regions, or the prism homotopy. Those are proved in the indicated sections.

[Overview](../README.md) · [Previous page](part9-3.md)
