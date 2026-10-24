# 12. Two-block splice exteriors and the cyclic-distance complex

**Main theorem.** Let $`L\subset S^3`$ be an oriented non-split link whose exterior has exactly two JSJ blocks $`M=P\cup_g Q`$, each an orientable circle product over a planar surface. There is one common JSJ torus $`T`$; all other boundary tori are actual labelled link boundaries. Assume the regular fibre slopes have nonzero intersection on $`T`$. Each product block has at least two actual boundary tori. Then the reduced all-incompressible cyclic-distance flag complex $`X(L)`$ defined below is contractible. The extension with one cone point on one side is Corollary 21.1.

The assumption that this is an $`S^3`$ link exterior with its prescribed meridians is independent of the matrix conditions. No claim that arbitrary determinant-minus-one gluings give $`S^3`$ exteriors is made.

The cyclic proof is [Sections 13–14](splice-minimal-cuts.md), [15](splice-horizontal-pieces.md), [16](splice-vertices.md), [17](splice-local-distance.md), [18](splice-global-distance.md), [19](splice-matching-carrier.md) and [20](splice-contractibility.md), with [21](splice-one-cone.md) and [22](splice-examples.md) for the extension and witnesses. [Appendix A](splice-planar-blocks.md) proves the planar block inputs inside this repository. The named external inputs are listed in [the bibliography](../sources/bibliography.md).

Surfaces may be disconnected. “Reduced” means that closed components are excluded; it does not impose a genus bound or identify distinct proper arc classes. The prescribed actual spanning slope is the total-link longitude $`\gamma_j=\lambda_j-(\sum_{s\ne j}\mathrm{lk}(L_j,L_s))\mu_j`$, with $`\lambda_j`$ the individual preferred longitude.


## 12.1. Boundary convention and matrix data

Write

```math
P=S^1_{h_P}\times B_P,\qquad Q=S^1_{h_Q}\times B_Q,\qquad
B_i\cong S^2\setminus(n_i+1)D^2,\qquad n_i\ge2.
```

The distinguished base circle $`J_i`$ gives the copy of $`T`$; the other $`n_i`$ circles give actual labelled tori. A genuine JSJ torus cannot have a solid torus or $`T^2\times I`$ product side, so the displayed lower bound includes every product block in this one-edge family.

A surface is oriented, has one prescribed oriented spanning curve on every actual torus, has no closed components, and is componentwise incompressible. Isotopies start at the identity and may slide actual boundary curves. They need not preserve $`T`$ or the Seifert fibering. No genus or norm restriction is imposed in the initial vertex definition.

All wall signs use the global surface coorientation. Orient each zero-side base so a right-to-left crossing of an arc directed negative-to-positive is a positive crossing of its oriented annulus. This fixes the relative sign between the blocks; the negative Hopf side has no independently reversible height convention.

Set

```math
\Phi(\mu_j)=1,\qquad \alpha=\mathrm{PD}(\Phi),\qquad
k_i=\Phi(h_i),\qquad t_i=\Phi(d_i),
```

where $`d_i`$ is a section slope on the common torus. The actual spanning curve $`\gamma_j`$ is the primitive kernel of $`\Phi|_{T_j}`$ with actual longitude coefficient one. Thus

```math
\Delta(\gamma_j,h_i)=|k_i|
\quad\text{on every actual torus of block }i.
```

This follows by writing $`h_i=u\mu_j+v\gamma_j`$ and applying $`\Phi`$. In particular $`k_i=0`$ forces the actual boundary curve to be an oriented fibre. No assumption about a preferred longitude being itself the spanning slope is made.

Use the fibre/section convention

```math
g_*h_P=a h_Q+c d_Q,\qquad g_*d_P=b h_Q+d d_Q,\qquad
A_g=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad ad-bc=-1,\quad c\ne0.
```

The covectors satisfy

```math
(k_P,t_P)=(k_Q,t_Q)A_g,\qquad
q=\gcd(|k_P|,|t_P|)=\gcd(|k_Q|,|t_Q|).
```

Take $`q=0`$ if the restricted covector is zero. The matrix is unimodular, and
$`\Delta(g_*h_P,h_Q)=|c|`$. Consequently

```math
q=0\quad\Longleftrightarrow\quad k_P=k_Q=0.
```

If $`q>0`$, let $`\ell`$ be the primitive kernel slope of $`\Phi|_T`$ and choose a transverse coordinate $`u`$ with $`\Phi(u)=q`$. Reading ports positively below means in this transverse direction. In the mixed case $`k_P=0\ne k_Q`$,

```math
\ell=h_P\text{ as an unoriented slope},\qquad
|k_Q|=q\,\Delta(g_*h_P,h_Q)=q|c|.
```

All matrix entries are allowed when their construction is a link exterior as stipulated. An arbitrary determinant-minus-one gluing of two pieces is not being declared to give an $`S^3`$ link exterior.

We retain the open whole-complement definition of distance. In the $`\Phi`$ cover, choose one lift $`V_B`$ of the entire connected open complement of $`B`$ and the complete $`A`$ blocks $`V_{A,j}=\tau^jV_{A,0}`$. Then

```math
D_M(A,B)=\max\{j:V_{A,j}\cap V_B\ne\varnothing\}
-\min\{j:V_{A,j}\cap V_B\ne\varnothing\},\qquad
\delta_M([A],[B])=\min_{A',B'}D_M(A',B').
```

Only one common deck translation is allowed. All complements used below are proved connected; their loops have zero $`\Phi`$ and hence they lift homeomorphically.

**Definition 12.1.** The vertices of $`X(L)`$ are ambient-isotopy classes of the reduced, oriented, componentwise incompressible spanning surfaces specified above, representing $`\alpha`$. Distinct vertices are joined by an edge exactly when $`\delta_M=1`$. The complex $`X(L)`$ is the flag completion of this graph, and its realisation is given the CW topology.

The geometric complex uses exactly the same vertex convention as [Section 1](objects.md). Its simultaneous realisation and strong deformation retraction are proved in [Sections 23–27](splice-geometric-normalisation.md); the trace-order obstruction is illustrated in [Section 28](splice-geometric-examples.md).
