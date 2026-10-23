# 4. The ordinary ambient-isotopy vertex bijection

[Overview](../README.md) · [Definitions](objects.md) · [References](../sources/bibliography.md)

## 4.1. Surfaces and simultaneous verticalisation

All pairwise coherent linking numbers are the nonzero number $`pq`$; actual sign changes preserve their nonvanishing. Thus these links are non-split. Their exteriors are irreducible and their boundary tori incompressible, by Lemma 2.1. A prescribed fibre boundary cannot bound a disk, since $`h`$ has infinite order.

Every other incompressible spanning component is essential. Indeed Hatcher Lemma 1.11 leaves only a boundary-parallel annulus as a failure of boundary-incompressibility, and that annulus would use one boundary torus twice. Hatcher Proposition 1.12 then makes it vertical or horizontal. The prescribed fibre slope $`\gamma_i=\epsilon_i h_i`$ excludes horizontal boundary. Hence every component is a vertical annulus made of regular fibres, pairing opposite endpoint signs. There are exactly $`m`$ annuli.

They can be made vertical as one whole system. Verticalise one annulus and cut along it, carrying the others by isotopy extension. Its base arc joins two distinct actual circles; the cut base and cut exterior are connected and irreducible. The remaining annuli have fibre boundaries on distinct untouched tori, so are again essential. Hatcher's boundary-relative verticalisation fixes the earlier cut faces. Repeat and glue back. The argument neither deletes retained exceptional fibres nor asserts a product structure in their neighbourhoods.

Every compact regular base multiarc can be moved out of the fixed $`U_j`$ by radial isotopies fixing the cone points; these lift equivariantly in the local fibre-solid-torus models. Thus the following fixed model loses no vertex:

> An allowed system on $`P`$ consists of $`m`$ disjoint embedded proper arcs, each joining a positive actual circle to a negative actual circle, using every actual circle once and no auxiliary circle. Endpoints slide on their labelled actual circles. The auxiliary circles stay marked and unused.

Its inverse image gives incompressible spanning annuli: the core of each is $`h`$ of infinite order. The orientation is fixed by the prescribed $`\epsilon_i h_i`$ boundaries. These systems have norm zero, and conversely any reduced norm-zero spanning surface has only such incompressible annuli. In particular all vertices are norm-minimising; identifying the reduced $`X`$ with $`MS`$ does not invoke a contractibility theorem about $`MS`$.

The remaining issue is injectivity under arbitrary three-dimensional isotopy; it is proved below using §3.

## 4.2. The vertex theorem

**Theorem 4.1.** For every classified $`k=0`$ exterior, allowed **joint** arc-system isotopy classes on $`P`$ are in bijection with $`V(X)`$ under $`a\mapsto[F_a]`$, where $`F_a=p^{-1}(a)`$ for the Seifert projection $`p`$.

**Proof.** Surjectivity is simultaneous verticalisation in §4.1. An ambient isotopy between vertical annular systems preserves each labelled torus and the pairing of its ends. Track a spanning path in each annulus. Use the fibre quotient

```math
\pi_1(E)\longrightarrow\pi_1(E)/\langle h\rangle
\cong\pi_1^{\mathrm{orb}}(B)=\Gamma,
```

and its relative fundamental-groupoid version. Endpoint tracks on the labelled tori map to powers of the actual peripheral generators in $`\Gamma`$; changing the spanning path inside an annulus changes only a fibre power, killed by this quotient. This is not the homomorphism induced by the continuous map to the underlying base space, which would kill cone meridians as well. Thus the two base arcs have the same peripheral double coset, even if the isotopy crossed exceptional cores or left vertical position. Lemma 3.4 gives the corresponding ordinary arc classes whenever the model is not a point. The remaining cases are §3.5.

In every non-point case $`\chi(P)<0`$. Fix one ordinary hyperbolic metric with geodesic boundary on $`P`$. The unique orthogeodesics of the component proper classes straighten every disjoint multiarc simultaneously, with common classes represented once and boundary cyclic order retained. The individual classes therefore determine the joint system. Conversely a base-system isotopy can fix collars of all unused $`A_j`$. The circle bundle above $`P`$ is trivial, so lift that isotopy in a trivialisation and extend by the identity over every exceptional solid torus. This is an ordinary ambient isotopy of the exterior. ∎

Only embedded proper arcs with distinct actual ends are asserted to be detected by the orbifold double coset. No injectivity assertion is made for arbitrary words under the relations $`x_j^{q_j}=1`$.



## 4.3. Effective codes and decidable equality

**Lemma 4.2.** Matching vertices admit finite rational PL codes with decidable equality. No oracle for realisability of an arbitrary word list is needed.

**Proof.** Fix a marking of $`\pi_1(P)\cong F_{n+s-1}`$. A path from actual boundary $`C_i`$ to $`C_j`$ determines a peripheral double coset $`\langle d_i\rangle w\langle d_j\rangle`$ in this **ordinary** free group. Endpoint slides multiply by the peripheral powers on the two sides. Ordinary homotopy-isotopy and simultaneous straightening identify codes exactly when the pairing and those ordinary double cosets agree. The preceding fibre-quotient argument is what justifies using ordinary codes for unrestricted three-dimensional isotopy; no injectivity of the orbifold quotient on arbitrary words is asserted.

Choose a common basepoint and paths $`u_i`$ to the labelled boundaries. Closing an arc at its endpoints gives the word $`u_i a u_j^{-1}`$; changing the endpoint closures multiplies by $`d_i^r`$ and $`d_j^t`$. Write $`K_i=\langle d_i\rangle`$ for the resulting ordinary peripheral cyclic subgroup in this paragraph.

Choose once and for all a rational polygonal planar model of $`P`$: one outer polygon and $`n+s-1`$ disjoint inner polygons, labelled by all actual and auxiliary boundaries, together with a finite triangulation and a free-group marking. A code consists of $`m`$ finite rational PL polygonal arcs, their endpoint labels, and their coorientations. Exact segment-intersection and point-in-polygon tests decide whether the code is an allowed system. Every allowed system has such a code up to isotopy, by PL approximation and a small perturbation of vertices. An arc's word is obtained by pushing to the marked one-skeleton, or by recording crossings of fixed cuts reducing $`P`$ to a disk. The triangulation and marking are fixed background data, not a mapping-class-group quotient.

Two valid codes define the same vertex exactly when their pairings agree and all component double cosets agree. The latter is decidable by the following finite automaton construction.

For $`K_iwK_j`$, make an NFA with a left state bearing directed word loops $`d_i,d_i^{-1}`$, a directed stem spelling $`w`$ to a right state, and right loops $`d_j,d_j^{-1}`$. Add an epsilon edge for every path known to freely reduce to the empty word. Obtain all such edges by taking transitive closure and repeatedly adding


```math
p\longrightarrow_\varepsilon q
\quad\text{if}\quad
p\longrightarrow_z r\longrightarrow_\varepsilon s\longrightarrow_{z^{-1}}q.
```


There are finitely many state pairs, so saturation terminates. Every added edge has a freely trivial witness path. Conversely every freely trivial word admits nested inverse-pair cancellation, so induction on its length proves it is captured. A reduced candidate word $`v`$ is accepted by the saturated NFA exactly when some original accepted word reduces to $`v`$, i.e. exactly when $`v\in K_iwK_j`$. Testing the other representative word decides equality. This argument applies also to the final peripheral word, the inverse product of the other peripheral generators.

If canonical data are desired, enumerate reduced words in length-lexicographic order and choose the first accepted word for each coset. There is at least one, so this also terminates. Efficiency is not asserted. The vertex domain remains valid PL codes modulo this decidable equality, so deciding whether an arbitrary unrealised word list admits an embedding is unnecessary. This gives a countable, effective domain for the complete model.

∎
