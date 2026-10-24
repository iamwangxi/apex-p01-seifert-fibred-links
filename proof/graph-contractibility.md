# 38. Face-compatible contractions and the infinite complex

[Overview](../README.md) · [Definitions](objects.md) · [Graph-manifold theorems](graph-theorems.md) · [References](../sources/bibliography.md)

Fix a vertex $`v_*`$ and a finite subcomplex $`K\subseteq X`$. Take finitely many canonical zero arc cores for its vertices and $`v_*`$, with one band per proper class and multiplicities in that band. Bands are chosen disjoint whenever their cores are disjoint.

For each vertex $`v`$, choose a global band phase map representing it. On a zero base it increases by the integral edge multiplicity and is zero modulo one off its bands, including unused cone collars. Its real face offsets encode the relative levels of Section 32. Extend into the horizontal clusters in that relative state, with strictly positive normalised fibre derivative in the interior and nonnegative derivative in outer collars. Flat boundary phases occur only among the finitely many zero-base corner phases. A regular phase in $`(0,1)`$ for this individual map represents $`v`$.

Choose real equivariant lifts $`h_v`$ with one common normalisation, and for coefficients on $`V(K)\cup\{v_*\}`$ put $`h_\mu=\sum_v\mu_v h_v`$. The equivariance is global $`\Phi`$; no local primitive-cover generator is used.

At a regular phase, zero-base fibres consist of proper arcs and possibly circles. Delete the circle components. Horizontal blocks still have positive fibre derivative at every remaining point and their actual primitive boundary. They supply their connected horizontal pieces. The surviving global surface is incompressible by essential-piece assembly, and every component has actual boundary. Different regular phases, even after deleting circles, are disjoint. Their finite set of distinct vertex classes therefore spans a simplex of $`Y`$.

There are genuinely only finitely many possible vertex classes in this coefficient family. Use one finite PL triangulation of the regular zero bases, record the deck changes, and bound all lifted corner values over the finite coefficient simplex. Only finitely many levels $`r+k`$ and normal arc templates occur. The cluster relative integers are bounded by the same finite boundary lift bounds; their connected fibre types are fixed. Away from equal corner phases the templates and boundary tracks are stable. At a collision the disappearing phase intervals have measure zero.

Let $`T(\mu)\in|Y|`$ be the sum of these regular reduced vertex classes weighted by their phase-interval lengths. This is continuous into a fixed finite geometric subcomplex. Importantly, after deleting circles its **actual class and relative levels** are recomputed; the old phase index is not reused.

On a true input simplex the zero bands are disjoint. There are no circle components. In an edge band the phase increase is $`c_e=\sum_v\lambda_v m_{v,e}`$, which can exceed one. Counting parallel occurrences over one phase period gives total measure $`c_e`$. The full relative face vector is the barycentric average of the input vectors. Thus Theorem 36.2's exact recovery gives $`T(\lambda)=\sum_v\lambda_v[v]`$. This uses integer multiplicities, not a zero-one incidence bound.

Consequently


```math
C_K(x,t)=R\!\left(
T\!\left((1-t)\lambda(x)+t\mathbf e_{v_*}\right)\right)
\qquad\text{(38.1)}
```


is a face-compatible nullhomotopy of the finite inclusion $`K\hookrightarrow X`$, with $`C_K(x,0)=x`$ and $`C_K(x,1)=v_*`$. The same phase maps and the same threshold are used on all faces. This is not a product of independently chosen block contractions.

One-point inputs give connectivity. Compact sphere images lie in finite CW subcomplexes and are killed by (38.1). Whitehead's theorem proves $`X`$ contractible, and Section 37 proves $`Y`$ contractible. The all-horizontal singleton case was handled in Section 30. This proves Theorems 29.1 and 29.2.
