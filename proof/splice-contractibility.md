# 20. Finite height families and contractibility of the whole class

[Overview](../README.md) · [Definitions](splice-objects.md) · [Block lemmas](splice-planar-blocks.md) · [References](../sources/bibliography.md)

**Theorem 20.1.** The full complexes in the main theorem are contractible.

**Proof.** The nonzero/nonzero case is already a point. For a mixed case fix a base diagram $`A_*`$ and a finite global subcomplex $`K`$. By the isometric ordinary model and the crossing obstruction, canonical representatives of the finitely many diagram classes of $`K`$ and $`A_*`$ are disjoint on every input simplex. Choose common PL representatives and thin bands, with common copies of repeated edges.

Each input diagram gives a base circle map increasing once across each oriented arc band and zero off the bands. On each actual boundary its lift is monotone with degree $`\pm1`$; on $`J`$ it is monotone with degree $`\pm q`$. Choose a common lifted point outside all bands and normalise all real lifts there. Put $`\mathcal V=V(K)\cup\{A_*\}`$. For coefficients on this finite set, define on the common cover

```math
\mu_A\ge0,\qquad \sum_{A\in\mathcal V}\mu_A=1,\qquad
h_\mu=\sum_{A\in\mathcal V}\mu_A h_A.
```

This equivariant lift retains the prescribed boundary degrees and monotonicity.

Use one finite common triangulation and exclude its vertex phases. At a regular phase the base fibre has exactly one end on every actual circle and exactly $`q`$ ends of one sign on $`J`$. Its interval components join opposite signs; consequently no interval has both ends on $`J`$. Delete circle components. What remains is an allowed annular diagram. The decoder potential is recomputed from the retained arc flow; no assertion that deleting circles preserves the old phase height or its block indices is used.

The finite-template argument applies with this one multiple boundary. Bound all lifted triangle corner values over the finite coefficient simplex. Only finitely many levels $`r+k`$ occur in a chosen triangle. Triangle segment incidences, edge orders and fixed deck changes give finitely many normal templates and hence a genuinely finite set of ordinary arc coordinates. Hyperplanes for integer corner values and equal phases modulo one fix the templates and phase-interval lengths. At collisions, disappearing intervals have zero weight and every positive-length interval has a stable interior phase. For each regular phase interval $`I`$, let $`A_I(h_\mu)`$ be its retained arc system and put

```math
W_e(\mu)=\sum_I\lvert I\rvert\,\mathbf{1}_{\{e\in A_I(h_\mu)\}}.
```

Equal normal templates are related by order-preserving moves on edges, extended across triangles, so they determine the same ordinary arc classes. The retained averaged flow $`W`$ is therefore continuous in one fixed finite-dimensional space.

At each parameter its positive-weight arcs have simultaneous disjoint representatives, obtained from distinct regular fibres of that same circle map. They form an allowed support graph, with demand one at each actual circle and demand $`q`$ at $`J`$. There are finitely many supports. Theorem 19.1 pastes their decoders over common zero-coordinate faces and gives a continuous global map $`S(W(\mu))`$ with finite image.

On an initial true simplex its bands are disjoint. In an edge band the convex height has the form $`b_e+c_et_e`$ with
$`c_e=\sum_{A\ni e}\lambda_A\in[0,1]`$. A parallel copy of that edge occurs for total phase measure $`c_e`$. Outside bands there are only excluded phases. Thus
$`W=\sum_A\lambda_A\chi_A`$, and exact recovery in Theorem 19.1 gives the original global simplex point. Write $`F(\mu)=S(W(\mu))`$. For $`x=\sum_{A\in\sigma}\lambda_A[A]`$ in an input simplex, define

```math
C_K(x,t)=F\left((1-t)\sum_{A\in\sigma}\lambda_A\mathbf e_A
+t\mathbf e_{A_*}\right).
```

Here $`\mathbf e_A`$ is the standard coefficient vector for $`A\in\mathcal V`$. Exact recovery gives $`C_K(x,0)=x`$, and $`C_K(x,1)=[A_*]`$. The common lifts and the zero-face identities make this a face-compatible nullhomotopy of $`K\hookrightarrow X(L)`$.

There is no need to choose one continuously marked horizontal representative for every parameter. The proved ordinary vertex bijection and class-distance formula identify the diagram complex **simplicially** with the global complex, so the decoded homotopy is already a homotopy in $`X(L)`$. No gluing parameter is left outside that comparison.

In the double-zero case apply the same construction on both bases. Their JSJ collars are constant zero. The real lifts can be normalised on one common $`T_0`$, and convex combinations keep that value. Phase fibres avoid the torus; paired flow supports are decoded with one common threshold by Theorem 19.1. The same finite-template and exact-initial-identity proof gives finite inclusion nullhomotopies. Independent local contractions are not used.

Finally the realisation has its CW topology. One-point inputs give path connectedness; compact sphere images lie in finite subcomplexes and are killed by their finite inclusion homotopies. Whitehead's theorem gives contractibility. The argument does not assume local finiteness or contractibility of every finite image. ∎
