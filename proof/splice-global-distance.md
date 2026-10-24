# 18. Global distance: lower bound and a horizontal filling with no extra indices

[Overview](../README.md) · [Definitions](splice-objects.md) · [Block lemmas](splice-planar-blocks.md) · [References](../sources/bibliography.md)

**Theorem 18.1 (global class distance).** The class metric is as follows.

If both $`k`$ values vanish, take the two unit matching potentials with $`H_i(J_i)=0`$. Then

```math
\delta_M(a,b)=
\max\{\max H_P,\max H_Q\}
-\min\{\min H_P,\min H_Q\}.
```

In the mixed case, under Theorem 16.2,

```math
\delta_M(a,b)=\Delta_P(a,b)=\mathrm{osc}(H_P).
```

If both $`k`$ values are nonzero, $`X`$ has one vertex and its class metric is zero.

### 18.1. The mixed lower bound uses simultaneous simplification

Choose global representatives of $`a,b`$ and the essential torus $`T`$. **PS Lemma 3.5** puts these three surfaces in pairwise almost-transverse, pairwise simplified position. Move the resulting torus back to the fixed torus by a common ambient isotopy if necessary. The two spanning surfaces still have globally simplified intersection, so PS Proposition 3.2 gives their class-minimum width.

Their separate pairs with $`T`$ are simplified. The observation after Lemma 13.1 makes all cut pieces essential. Theorem 14.1 therefore gives the mixed annulus/horizontal pieces, each with connected complete complement. Lemma 16.1 identifies the zero-side classes with the fixed unmarked diagrams of $`a,b`$.

One whole global $`b`$ block restricts to exactly one lift of the whole connected $`P\setminus b_P`$; its $`a`$ indices are the corresponding local indices up to a single translation. Since $`\phi_P`$ sends an actual meridian to one, its deck generator is the global generator, with no factor of $`q`$ in this comparison. Thus

```math
\Delta_P(a,b)\le D_P(a_P,b_P)\le D_M(a,b)=\delta_M(a,b).
```

This argument does not assume that independent piece normalisations preserve a pre-existing global width. Simultaneous simplified intersection with $`T`$ is the extra interface that supplies the lower bound.

### 18.2. Removing partial coincidences for the upper bound

Let $`d=\Delta_P(a,b)`$ and choose normal local annuli attaining it by Lemma 17.1. Equal vertices have $`d=0`$ and are handled by coincident global representatives. For distinct vertices $`d\ge1`$.

If the complete reaching-arc subsystem is common to both diagrams, choose the whole horizontal-bearing global component common. The local difference potential is constant on all sectors adjacent to $`J`$: every incident current there is zero. The common horizontal side adds that one already attained index. The global representative width is exactly $`d`$.

Otherwise common reaching annuli are only **parts** of different global components and must not be left as partial coincidences. Separate each such common local annulus slightly. Its two old outside region values agree, say at $`r`$. The new strip can have value $`r+1`$ or $`r-1`$ by choosing the side of the push. Choose one inside the old interval $`[\min H_P,\max H_P]`$; this is possible because $`d\ge1`$. Disjoint thin bands allow the choices independently. Common actual-to-actual components may remain common. No local width is increased. Now both coherent JSJ traces are disjoint.

### 18.3. Boundary heights and the explicit horizontal extension

Arrange the $`b`$ ports equally spaced by a common boundary isotopy, preserving the local representative width. Choose adapted circle maps on the base with zero fibres the two annular systems. Such maps are obtained by cutting along a whole system, assigning its two cut frontiers phases zero and one, and extending into the connected cut surface with values strictly between them. The maps have actual boundary degrees $`\sigma_j`$ and JSJ degree $`\psi(d_J)`$. They can be strictly monotone at each used boundary.

Choose $`f_B`$ linear on $`T`$, and take the canonical horizontal fibration of Section 15 on $`Q`$ with this boundary map. Write its fibre $`H`$ and return map $`\rho`$ as there. Let $`C_1,\ldots,C_q`$ be the boundary circles of $`H`$ on $`T`$, with $`\rho C_j=C_{j+1}`$ cyclically.

For these adapted maps the zero fibre is the entire surface system, with no additional zero component. On one connected whole complementary lift the real phase avoids every integer, so its integer part is constant. Equivariance increases that integer by one on the next deck translate. Thus the floor of the real $`a`$ phase is **exactly** its complete-block index in a chosen whole $`b`$ block, up to one common translation. This is the index interpretation used in the filling below; a pointwise height is not being substituted for a whole-complement width.

The difference of the two local circle maps has a real lift. Its value on $`C_j`$, measured at the lower $`b`$ frontier, is a noninteger real number $`a_j`$, constant along that trace circle. On the intervening torus annulus the $`b`$ phase is $`t\in[0,1]`$. Linearise the other boundary phase there without changing port order or local width. It becomes

```math
a_j+t(1+a_{j+1}-a_j),\qquad
1+a_{j+1}-a_j>0,\qquad a_{q+1}=a_1.
```

Equivalently, if $`\nu_j=\lfloor a_j\rfloor`$ and $`m_j`$ is the number of $`a`$ ports in this $`b`$ sector, then

```math
\nu_{j+1}=\nu_j+m_j-1,\qquad m_j\ge0,\qquad \sum_jm_j=q.
```

These are cyclic boundary-height constraints. They replace the single constant root of the empty-trace case. They do not permit independent shifts on the $`q`$ sectors.

Let $`m=\min_j a_j`$ and $`M_0=\max_j a_j`$. Choose a noninteger $`c_0\in[m,M_0]`$, for example one of the $`a_j`$. Averaging a collar metric over the finite cyclic action gives equal, $`\rho`$-invariant collars of all $`C_j`$. With a common cutoff $`0\le\chi\le1`$ define on $`H`$

```math
v(x)=c_0+\chi(x)(a_j-c_0)\text{ in collar }C_j,\qquad
v(x)=c_0\text{ elsewhere}.
```

Then

```math
m\le v\le M_0,\qquad
1+v(\rho x)-v(x)>0.
```

The second inequality is $`1+\chi(a_{j+1}-a_j)>0`$ in a collar and is one elsewhere. In the mapping-torus coordinates of $`Q`$ define the lifted $`a`$ phase on one whole $`b`$ block by

```math
h_A(x,t)=(1-t)v(x)+t\bigl(1+v(\rho x)\bigr).
```

Subtracting $`t`$ gives a real function that descends under
$`(x,1)\sim(\rho x,0)`$. Thus the circle map induces exactly $`\phi_Q`$. It is strictly increasing along the flow $`h_Q/k_Q`$, agrees with the prescribed $`a`$ boundary phase on $`T`$, and its zero fibre is a connected horizontal piece. By Lemma 15.1 it is the required relative piece class. The actual boundary has a common nonintegral phase displacement $`c_0`$, so its curves are disjoint from the $`b`$ boundary.

Crucially,

```math
m\le h_A(x,t)\le 1+M_0.
```

The two extreme integer indices
$`\lfloor m\rfloor`$ and $`1+\lfloor M_0\rfloor`$ already occur near the ends of the open torus sectors on the $`P`$ side. Hence the horizontal block introduces **no new extreme complete-block index**. The maps and zero surfaces can be taken PL; positive corner smoothing, smaller than the finite margin from the extreme nonintegers to the integers, preserves this conclusion.

Glue the two maps and surfaces across $`T`$. Both maps induce the global $`\Phi`$. In one whole global $`b`$ block the horizontal-side index interval lies inside the vertical-side interval. The representative width is $`d`$. Therefore $`\delta_M(a,b)\le d`$, completing the mixed formula.

### 18.4. The double-zero formula

Here all annuli avoid $`T`$ and the two local complements glue across the entire torus. A whole global block contains one entire lift $`T_0`$, so the two local potentials must have the same value there. This gives the displayed union-of-ranges representative formula.

For the class minimum, normal local annuli have no global relative products. A proposed product with both faces in one block gives a relative path equality whose scaffold and actual endpoint motions lie in that factor of $`G_P*_{G_T}G_Q`$. Factor injection and quotient by the fibre force an ordinary empty bigon, half-bigon or common full arc. A product with faces in different blocks has no intersection frontier; its faces must be whole annuli and would need the same actual end tori, but the two actual label sets are disjoint. Common-annulus cases use unit actual usage. Uncollapsed product sides lie in the actual $`\partial M`$, not the internal torus. Thus the position is globally simplified and PS Proposition 3.2 supplies the class minimum. The unit-end argument works for every actual count. The complete local block proof, including coincident annuli, is Lemma A.2 in [the planar-block appendix](splice-planar-blocks.md).

The mixed proof above likewise minimises over all ordinary global representatives, including ones with nonminimal torus intersections. A restricted isotopy metric has not been substituted.
