# Appendix A. Planar block lemmas used in the splice proof

[Overview](../README.md) · [Local distance](splice-local-distance.md) · [References](../sources/bibliography.md)

The lemmas here supply the unit-boundary, ordinary-isotopy and cone-detection inputs. The multiple coherent JSJ port is treated separately in Sections 16–18; a separating JSJ multicurve is not silently substituted into the unit-boundary hypothesis.

## A.1. Planar unit-boundary data

Let $`W`$ be an orientable irreducible Seifert block with orientable planar base orbifold $`B`$, with $`b\ge3`$ ordinary boundary circles $`C_1,\ldots,C_b`$ and finitely many cone points of orders $`q_j\ge2`$. All boundary tori are incompressible. Let $`h`$ be the regular fibre.

Some ordinary tori are actual and the rest are designated JSJ tori. An actual torus has one prescribed oriented fibre curve. For the **unit sector**, a JSJ torus is either unused or has one prescribed oriented fibre curve. Write $`I`$ for the active ordinary boundaries and give them signs $`\sigma_i\in\{+1,-1\}`$; the others have demand zero. Assume

```math
I\ne\varnothing,\qquad \sum_{i\in I}\sigma_i=0.
```

We assume at least one actual boundary. Thus the prescribed actual slope is vertical. This is the zero-fibre-degree sector. It is not a lemma for horizontal actual boundary conditions. If a unit JSJ condition instead prescribes a nonfibre slope, its system space is empty: horizontal components are excluded by the actual boundary, vertical components have fibre slope, and a boundary-parallel annulus would require two curves on the same torus.

An unmarked prescribed JSJ trace records its slope, multiplicity and orientation. For comparing pieces during gluing one must additionally use an embedded collared trace and compatible boundary motion. With multiplicity one, the boundary circle may slide on its own torus. For a fixed embedded fibre trace with several components, mark the corresponding base endpoints, including their cyclic order and signs.

Remove fixed small cone disks to form the ordinary planar surface $`P`$. Cone circles are always marked and unused. They are filled only when doing a spherical circulation calculation.

## A.2. Classification, ordinary isotopy and class distance

**Lemma A.2 (unit-boundary planar Seifert block).** For the unit data above:

1. Every incompressible spanning system with no closed components is simultaneously isotopic to the inverse image of a disjoint proper multiarc on $`P`$. Each arc joins two distinct active ordinary circles of opposite signs, and each active circle is used once. No inactive or cone circle is used.
2. These **joint ordinary multiarc isotopy classes**, with free endpoints on their labelled active circles, are in bijection with ordinary ambient-isotopy classes of the systems in $`W`$. The isotopy need not preserve the Seifert fibering.
3. The whole complement of every system is connected. For two ordinary normal systems $`a,b`$, the local class distance is the oscillation of the integer region potential obtained by crossing only $`a\setminus b`$ walls inside the complete $`b`$ complement. Common arcs remain cut frontiers, with no internal crossing edge.
4. If a designated JSJ boundary $`J`$ is unused, its region fixes the potential at $`H(J)=0`$. The **rooted profile**
   $`[\min H,\max H]`$ is the data needed at this one empty-trace gluing interface. Replacing it by its length loses information. With several unused JSJ boundaries, retain their individual values $`H(J_\ell)`$ as well as the range; they cannot all be independently set to zero.

Here normal means that common arc classes coincide, other crossings are transverse, boundary endpoints of distinct classes are distinct, and no ordinary bigon or free-endpoint half-bigon remains. Fixing an ordinary hyperbolic metric on $`P`$, and then straightening, supplies simultaneous canonical representatives.

**Proof.** We give the interfaces that change when actual boundaries are replaced by JSJ boundaries; no assertion depends on an actual link filling. The Seifert presentation is

```math
G_W=\left\langle h,x_1,\ldots,x_s,d_1,\ldots,d_b\ \middle|\ 
h\text{ central},\ x_j^{q_j}h^{c_j}=1,\ 
x_1\cdots x_s d_1\cdots d_b=1\right\rangle.
```

The fibre has infinite order: send $`h`$ to $`N=\prod_jq_j`$ (take $`N=1`$ if there are no cones), send $`x_j`$ to $`-c_jN/q_j`$, and choose the last boundary value to satisfy the final relation. Consequently a prescribed fibre cannot bound a disk. A boundary-parallel annulus would use one boundary torus twice, contrary to unit demand. Hatcher Lemma 1.11 makes every component essential. A horizontal component covers the whole base and would have nonfibre boundary on every ordinary torus, including an actual torus. Its actual fibre boundary is impossible. Hatcher Proposition 1.12 therefore makes each component a vertical annulus.

Verticalise the annuli successively. Cutting along an arc joining two distinct previously unused boundary circles preserves connectedness, irreducibility and the inherited Seifert structure. The boundary-relative clause in Hatcher's proof fixes earlier cut faces. The remaining boundary labels still occur once. Induction gives simultaneous verticalisation, including systems near exceptional fibres. Move the arcs out of fixed cone disks by local radial isotopies that lift in the fibre-solid-torus models. The sign convention is the one in which an oriented annulus pairs opposite signs.

Here is the ordinary-isotopy injection, which cannot be replaced by a homology calculation. The quotient by the central fibre is

```math
\Gamma=G_W/\langle h\rangle
=\left\langle x_j,d_i\ \middle|\ x_j^{q_j}=1,\ 
x_1\cdots x_s d_1\cdots d_b=1\right\rangle.
```

Tracking a spanning path through any ambient annulus isotopy gives equality of the endpoint peripheral double cosets in $`\Gamma`$. This is a **group quotient**, not a continuous projection of the isotopy through a cone to an ordinary base homotopy.

Close an arc with ends $`C_i,C_j`$ by the third boundary of a thin neighbourhood of $`C_i\cup a\cup C_j`$. Its conjugacy class is $`d_iw_ad_jw_a^{-1}`$. Its rational abelianisation $`d_i+d_j`$ is nonzero in $`\mathbb Q^b/\langle\sum d_i\rangle`$ because $`b\ge3`$. Double the orbifold along **all** ordinary boundaries. The double has genus $`b-1\ge2`$ and two cones of each order. Folding regular parts and then passing to cone-order quotients gives a group retraction, hence an injection of $`\Gamma`$ into the double's orbifold group. Goodness can be checked explicitly: map the paired cone meridians to $`+e_j,-e_j`$ in $`\prod_j\mathbb Z/q_j`$ and handles to zero, and fill the resulting ordinary punctured cover. The resulting genuine surface cover has genus at least two.

The two closing curves are thus regular essential homotopic curves in a closed good aspherical orbifold. Schultens’ closed Proposition 25 isotopes them away from the cones. Fold the regular isotopy to get ordinary free homotopy in the original punctured base. Ordinary homotopy-isotopy, followed by uniqueness of the seam in the labelled pair of pants, recovers the arc. Individual arc classes determine the joint system by simultaneous straightening. A base isotopy can fix unused collars and lifts over the ordinary circle bundle, extending by identity over exceptional solid tori. This proves assertion 2 for arbitrary cone orders and any number of inactive ordinary circles. No return-arc assertion with two ends on the same ordinary torus is hidden in this argument.

For completeness the local class minimum has the following direct detection proof. In the abelianisation of $`\Gamma`$,

```math
q_jx_j=0,\qquad \sum_i d_i+\sum_jx_j=0.
```

For a regular Jordan curve take one disk side after capping the ordinary holes. Its ordinary-hole and cone indicators are $`a_i,\eta_j\in\{0,1\}`$. Nullity implies

```math
a_i=t\text{ for all }i,\qquad \eta_j\equiv t\pmod {q_j}.
```

Thus the curve has an empty disk side. If it is peripheral at $`C_k`$, the equations at every $`i\ne k`$ give a common $`t=0`$ or $`1`$, and every cone indicator equals $`t`$. The curve is either trivial or cobounds a cone-free annulus with $`C_k`$. It follows that a relative product between noncommon annular faces would give an empty ordinary bigon, an empty half-bigon, or equality of the two full arc classes. These are excluded by normal position. The relative uncollapsed sides lie in $`\partial W`$, as required by Oertel and PS Section 3. Common-annulus faces have the usual coincident-component convention: no other component uses their two end tori; two distinct product faces within one common annulus cannot have an uncollapsed side, and with all sides collapsed their frontiers and collar memberships force them to coincide. There is also no boundary product disk between disjoint or coincident fibre curves.

All these surfaces have Thurston norm zero. The PS homology hypothesis holds for this block: the presentation gives $`b_1(W)=b`$, Euler characteristic zero gives $`b_2(W)=b-1`$, and the boundary-torus image in $`H_2(W)`$ has rank $`b-1`$ by the relative fundamental class sequence. Hence $`H_2(W)\to H_2(W,\partial W)`$ is rationally zero and is zero integrally because the target is free. The unit multicurve does not separate any boundary torus; an empty condition does not separate an unused torus either. PS Proposition 3.2 applies and makes the normal representative attain the class minimum.

The homomorphism dual to the system kills $`h,x_j`$ and sends each active $`d_i`$ to $`\sigma_i`$, all others to zero. It factors through the ordinary planar base. The full complement of a matching is connected, since each successive cut joins two previously unused circles. Loops there have zero intersection with the entire system, so the whole complement lifts homeomorphically. Its signed region graph is connected, and integrating the unit wall crossings gives a single integer potential up to one constant. Every open region attains its complete-block index and every open-block intersection contains such a region. This proves assertion 3; the unused-circle region proves assertion 4. ∎

The lemma is stated with $`b\ge3`$. The two-ordinary-boundary case actually needed for the one-cone extension is Lemma A.3 below.

## A.3. Two ordinary boundaries and one cone

**Lemma A.3 (the low seam case).** Suppose the base has exactly two ordinary boundary circles and at most one cone, both ordinary circles are used once with opposite signs, and the prescribed curves are regular fibres. There is exactly one spanning annulus class under the boundary-motion convention.

**Proof.** The fibre is infinite-order by the integer homomorphism in Lemma A.2. A disk is impossible; a boundary-parallel annulus would use the same torus twice. Hatcher's classification therefore gives a vertical annulus. With no cone the ordinary base is an annulus; after deleting a cone neighbourhood it is a pair of pants. The proper arc between the two specified ordinary boundaries has one free-endpoint isotopy class in either case. To see the latter directly, cut along a chosen seam to obtain an annulus. Innermost return arcs remove the intersections of another seam by bigons and free-endpoint half-bigons. Once the seams are disjoint, an empty rectangle identifies them. These base moves lift over the regular circle bundle and extend by the identity over the cone solid torus. Thus every surface is in the same class. No cone-peripheral torsion closing curve is used in the closed-orbifold theorem. ∎

## A.4. Detection when an ordinary boundary is used repeatedly

**Lemma A.4 (distinct-end detection with a coherent port).** In a planar block with at least three ordinary boundaries, the ordinary-isotopy detection and Jordan/peripheral tests in Lemma A.2 apply to an embedded multiarc whose arcs have distinct ordinary ends, even if several ends lie on one distinguished boundary, provided every arc has a unit actual end. With two ordinary boundaries and one cone, the only coherent unit-actual case is Lemma A.3.

**Proof.** An arbitrary ambient annulus isotopy gives endpoint peripheral double cosets via the fibre quotient and its relative fundamental-groupoid version. It need not project continuously to the punctured base. For a given pair of distinct ordinary ends, the closing curve used in Lemma A.2 has rational class $`d_i+d_j\ne0`$ because there are at least three ordinary boundaries. The closed-double, finite-cover, regular-isotopy and seam argument there therefore recovers each individual proper arc class. A negative-curvature metric on the ordinary surface with all cone holes retained gives simultaneous orthogeodesic straightening; its unique representatives recover the joint diagram and cyclic order at the repeated boundary. Coincident arcs are copied once. The Jordan and peripheral equations in Lemma A.2 count boundary features, not incident endpoints, so are unchanged. Each common annulus still has its actual end used once: no other component can share both its labelled ends. The coincident-face argument in Lemma A.2 therefore remains valid. In the low case, coherence and the single actual end force one distinguished end, reducing to Lemma A.3. This assertion includes no arc returning to its own boundary and no arbitrary-word injectivity claim for an orbifold quotient. ∎
