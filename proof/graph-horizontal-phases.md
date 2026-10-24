# 32. Horizontal clusters and the full twist quotient

[Overview](../README.md) · [Definitions](objects.md) · [Graph-manifold theorems](graph-theorems.md) · [References](../sources/bibliography.md)

Join adjacent horizontal blocks into maximal connected clusters $`C`$. Each cluster is fibred in $`\Phi_C`$: glue fibre-monotone phase maps, affine on internal tori. Its spanning fibre $`H_C`$ is connected because it contains actual boundary of degree one. The return map of the **cluster** need not have finite order.

For $`r_C`$ outer active tori fixed pointwise with specified traces, the relative ordinary horizontal state space is


```math
\mathbb Z^{r_C}/\mathbb Z(1,\ldots,1).
\qquad\text{(32.1)}
```


To prove this, standardise the phase maps on the marked tori. Their difference has a real lift with integer boundary constants $`n_e`$. A connector in connected $`H_C`$ detects $`n_e-n_f`$ under any relative ambient isotopy. Equal differences give a relative isotopy by convex interpolation, which is strictly of sign $`k_v`$ on each block. Every vector is realised by real base functions near the external tori, constant along the local fibre, with zero boundary value on the other piece boundaries. This applies the positive-phase construction of [Section 15](splice-horizontal-pieces.md) to the whole cluster. No one-port uniqueness is asserted for a multiport cluster.

A common phase circuit of $`H_C`$ advances all outer traces by one port step and returns the unparameterised fibre to itself. Thus only the **diagonal** port motion is trivial in that cluster. Tangential motions of the kernel circles add no parameter on the vertical side. Lemma 31.1 shows there is no extra port-winding stabiliser from a zero block.

Between zero blocks the trace is empty; twisting in its unused collar fixes all normal surfaces. Join zero blocks across these empty edges into connected zero regions $`\Lambda`$. Contracting each zero region and each horizontal cluster gives a tree $`\mathscr B`$.

**Theorem 32.1 (ordinary vertex quotient).** Vertices are compatible joint zero-block multiarcs together with the cluster states (32.1), quotiented by the actual common boundary-motion paths. Noncanonically their extra integer rank is


```math
\#\{\Lambda\}-1
\qquad\text{(32.2)}
```


when zero blocks exist. There is no local unit-end or complement-connectivity condition.

**Proof.** For pointwise traces, use Section 31's joint annulus forms and (32.1). A diagram isotopy moves its actual trace circles by a definite path. Extend it in neighbouring cluster collars, and use the relative phase classification at the new traces. Lemma 31.2 gives the converse restriction of an arbitrary global isotopy. Lemma 31.1 ensures no unrecorded integer is lost in a diagram loop. Only a cluster's common phase loop kills its diagonal.

For completeness the integer quotient is explicit. After choosing marked representatives of the unmarked diagrams, assign an integer to every active edge. Divide by adding the same integer on all edges incident to one cluster. On the tree $`\mathscr B`$, every edge assignment has a unique expression


```math
n_{\Lambda C}=t_\Lambda-s_C
```


up to one common additive integer, by solving from a root. These integers use the positive global $`\Phi`$-phase direction: one phase turn advances one port step, so no factor $`q_e`$ is inserted. This leaves one integer level per zero region modulo one common level, proving (32.2). Empty zero edges require the neighbouring unused-torus levels to agree.

Every diagram actually assembles. Annular pieces are essential, all horizontal cluster pieces are fibres, and compression disks reduce across incompressible tori to a piece compression or boundary compression. No constructed component is closed: an annulus either reaches actual boundary directly or reaches a horizontal piece with actual boundary. All parallel occurrences and all cyclic endpoint identifications are retained before this quotient. ∎

In the six-component test there is one zero region and two horizontal leaf clusters, so (32.2) is zero. The vertex set is exactly the central joint multiarc set. This identifies the ordinary quotient for the example.
