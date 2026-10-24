# 34. Horizontal filling with tracked boundary levels

[Overview](../README.md) · [Definitions](objects.md) · [Graph-manifold theorems](graph-theorems.md) · [References](../sources/bibliography.md)

Let $`A,B`$ be the two cluster fibre classes to be assembled, with given collared traces and their **real lifted** boundary differences. Their integer relative state is as in Section 32. The lemma replaces the cluster interior in those relative classes; it does not assume the original intersecting cluster representatives were already jointly horizontal.

Fix $`B`$ in standard horizontal form. For $`A`$, first take a blockwise horizontal representative $`A_*`$ of its prescribed ordinary relative class, with the same outer traces and boundary lift; this existence is supplied by Section 32 and relative Hatcher straightening. No width bound is claimed for that intermediate choice. Choose a vector field $`Z`$ positive for the phase maps of $`A_*`$ and $`B`$, tangent to the internal tori. In a Seifert block use $`h_v/k_v`$; on an internal torus the two phase differentials are positive multiples of the same covector. Partition and collar interpolation therefore give a common positive field. This works for any finite disjoint family as well. Make the $`B`$ boundary phase affine by a common boundary reparametrisation. Near an outer port choose the standard local fibre flow and its product collar. Its return has invariant collar coordinates on the finitely permuted outer boundary components, although the return in the interior of the cluster can have infinite order.

Cut along $`B`$, with coordinates $`(x,t)\in H_C\times[0,1]`$ and monodromy $`\rho`$. This $`\rho`$ can have infinite order. At a port, let $`C_j`$ be its $`q_e`$ boundary circles, ordered by $`\rho C_j=C_{j+1}`$. On its $`j`$-th open sector the lifted $`A`$-phase can be made


```math
g_j(t)=(1-t)a_j+t(1+a_{j+1}),\qquad
1+a_{j+1}-a_j>0.
\qquad\text{(34.1)}
```


Linearisation retains the zero order and the recorded relative lift. Coincident traces are allowed, so the $`a_j`$ may be integers. If a band phase has flat intervals, replace it by a strictly monotone boundary phase with the same zero curves before this linearisation. Its complementary intervals still avoid the integers, so this changes no overlap index.

**Lemma 34.1 (no extra global index).** Suppose all zero-side overlap indices lie in $`[m,M]`$, with the same global normalisation, on every port of $`C`$. The prescribed relative state and trace can be filled in $`C`$ without introducing an index outside $`[m,M]`$.

**Proof.** At each $`B`$-frontier, the two adjacent open sectors in (34.1) show


```math
m\le a_j\le M.
\qquad\text{(34.2)}
```


The upper bound follows by approaching the other end of the preceding sector, whose lifted value is $`1+a_j`$; the lower bound follows at the lower end of the next sector. These are bounds on the **inherited real lifts**, not independently chosen integers at different ports.

Choose $`c\in[m,M]`$. In collars of all outer $`C_j`$, choose cutoffs $`\chi`$ invariant under their return permutation, and set


```math
v(x)=c+\chi(x)(a_j-c),\qquad v=c\ \text{elsewhere}.
```


Then $`m\le v\le M`$ and $`1+v(\rho x)-v(x)>0`$; in a collar the latter is $`1+\chi(a_{j+1}-a_j)>0`$. Define


```math
g(x,t)=(1-t)v(x)+t(1+v(\rho x)).
\qquad\text{(34.3)}
```


Its difference from $`t`$ descends to a real function on $`C`$. It represents $`\Phi_C`$, has positive derivative along $`Z`$, and has exactly the required real boundary differences. For $`0\lt t<1`$,


```math
m\lt g(x,t)\lt M+1.
```


Thus all its integer indices belong to $`[m,M]`$.

To check the ordinary **relative** class, start with a blockwise horizontal representative of the prescribed state, standardised to the same boundary phases. It and $`B`$ admit the common positive field just used. The difference from the new phase map has a real lift zero on every marked outer collar. Convex interpolation along that field gives a relative ambient isotopy. Thus filling has not changed a cluster twist. No finite-order assertion about the cluster monodromy was used. ∎

For Seifert blocks with cones, the positive phase maps are obtained by the accepted circle-action averaging construction: if $`R_t`$ has regular period one and $`F(z,t)`$ lifts $`f(R_tz)-f(z)`$, put


```math
u(z)=\int_0^1(F(z,t)-k_vt)\,dt,\qquad f_{\rm eq}=f+u.
```


Then $`f_{\rm eq}(R_tz)=f_{\rm eq}(z)+k_vt`$. Collar corrections preserve the strict sign. Cone orders divide $`k_v`$, as follows from the Seifert relations. The outer collar argument above is entirely in the regular part.
