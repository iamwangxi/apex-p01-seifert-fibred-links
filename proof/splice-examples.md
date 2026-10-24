# 22. Explicit witnesses and a nonunit fixed-support test

[Overview](../README.md) · [Definitions](splice-objects.md) · [Block lemmas](splice-planar-blocks.md) · [References](../sources/bibliography.md)

## 22.0. A balanced eight-component splice

### 22.0.1. The splice and its slope matrices

Let $`H_5^+`$ be five coherently oriented regular fibres of the Hopf action with weights $`(1,1)`$ on $`S^3`$. Let $`H_5^-`$ be five coherently oriented regular fibres of the action with weights $`(1,-1)`$. Pairwise coherent linking numbers are respectively $`+1`$ and $`-1`$. Choose a distinguished fibre $`K_P`$ and $`K_Q`$. Both are unknots. The complement of the distinguished fibre alone is a solid torus $`V_P`$ or $`V_Q`$.

Remove the other four fibre neighbourhoods in each solid torus. The resulting pieces are

```math
P=E(H_5^+)=S^1_{h_P}\times B_P,\qquad
Q=E(H_5^-)=S^1_{h_Q}\times B_Q,
\qquad B_P\cong B_Q\cong S^2\setminus5D^2.
```

Their distinguished boundaries are to be glued; their remaining eight tori are actual link boundaries. Let $`(\mu_P,\lambda_P)`$ and $`(\mu_Q,\lambda_Q)`$ be the coherent meridian/preferred-longitude bases of the distinguished unknots, in their original spheres. Glue by the orientation-reversing map

```math
g_*(\mu_P)=\lambda_Q,\qquad g_*(\lambda_P)=\mu_Q,\qquad
[g_*]_{(\mu_Q,\lambda_Q)\leftarrow(\mu_P,\lambda_P)}
=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
```

The meridian of $`V_Q`$ is $`\lambda_Q`$, so the corresponding filling slope on $`\partial V_P`$ is $`\mu_P`$. Thus $`V_P\cup_gV_Q`$ is ordinary meridional filling of the exterior of an unknot, hence $`S^3`$. The retained eight curves form $`L_8`$, and

```math
M=E(L_8)=P\cup_g Q,\qquad T=P\cap Q.
```

The regular fibre slopes and convenient section slopes on the two copies of $`T`$ are

```math
h_P=\lambda_P+\mu_P,\quad d_P=\mu_P,\qquad
h_Q=\lambda_Q-\mu_Q,\quad d_Q=\mu_Q.
```

Consequently

```math
g_*h_P=h_Q+2d_Q,\qquad g_*d_P=h_Q+d_Q,\qquad
[g_*]_{(h_Q,d_Q)\leftarrow(h_P,d_P)}
=\begin{pmatrix}1&1\\2&1\end{pmatrix},
\qquad \Delta(g_*h_P,h_Q)=2.
```

Both displayed matrices have determinant $`-1`$. The two regular fibre slopes do not match even as unoriented slopes.

### 22.0.2. Actual orientations and the global spanning class

Give the four retained fibres in each piece signs $`\epsilon=(+,+,-,-)`$ relative to its coherent Hopf orientations. Within $`P`$ coherent linking is $`+1`$, within $`Q`$ it is $`-1`$, and across the two sides it is $`-1`$.

One can verify the last sign directly without a splice formula. If the coherent actual meridians are $`u_i`$ in $`P`$ and $`v_j`$ in $`Q`$, then on the distinguished tori the old longitude relations are

```math
[\lambda_P]=\sum_i u_i,\qquad
[\lambda_Q]=-\sum_jv_j.
```

The gluing gives $`[\mu_P]=-\sum_jv_j`$ and $`[\mu_Q]=\sum_i u_i`$. Substitution into the old actual-longitude relations gives coefficient $`-1`$ for every cross-side meridian. The actual preferred longitudes retain their old zero framing: viewed from either solid torus the other torus supplies the original meridional filling.

For actual orientations, $`\mu_i=\epsilon_i u_i`$ or $`\epsilon_i v_i`$. The oriented linking row sums are

```math
s_i=\sum_{\ell\ne i}\mathrm{lk}(L_i,L_\ell)
=\begin{cases}-1&i\text{ on }P,\\+1&i\text{ on }Q.\end{cases}
```

The cross-side contribution vanishes because each other side is balanced. It follows that the forced total-link spanning slopes are

```math
\gamma_i^P=\lambda_i+\mu_i=\epsilon_i h_P,\qquad
\gamma_j^Q=\lambda_j-\mu_j=\epsilon_j h_Q.
```

Here $`\lambda_i`$ are the actual preferred longitudes, and the regular fibres on actual tori use their corresponding coherent orientations. The usual boundary homology equation $`\sum_i[\lambda_i+b_i\mu_i]=0`$ forces $`b_i=-s_i`$.

The global homomorphism satisfies

```math
\Phi(h_P)=\Phi(h_Q)=0,\qquad
\Phi(\mu_P)=\Phi(\lambda_P)=0,\qquad
\Phi|_{\pi_1(T)}=0.
```

On either ordinary base it has the four values $`(+,+,-,-)`$ and value zero on the unused fifth circle. Every pair of actual components has linking number $`+1`$ or $`-1`$ after orientation signs. In particular a separating sphere cannot partition the components, so $`L_8`$ is non-split.

### 22.0.3. Why this really is the two-block JSJ decomposition

Each product piece is irreducible and all its boundary tori inject into $`\mathbb Z\times F_4`$. Gluing along an incompressible torus gives an irreducible manifold, with injections of both piece groups and the torus group by amalgam normal form. The actual tori are incompressible as well. The torus $`T`$ is not boundary-parallel: each side has four actual boundary tori and cannot be $`T^2\times I`$.

It remains to exclude a single Seifert block. If $`M\subset S^3`$ had a Seifert fibering, its base would be orientable: an orientation-reversing base loop would give an embedded Klein bottle, impossible in $`S^3`$. Hatcher Proposition 1.12 makes the essential torus $`T`$ vertical or horizontal for that fibering. It cannot be horizontal, since a closed horizontal surface covers the whole base, whose boundary is nonempty. A vertical $`T`$ would induce a Seifert fibering on each side.

The centre of $`\mathbb Z\times F_4`$ is exactly the displayed fibre factor. A regular fibre of an orientable-base fibering on either side must be central and primitive on $`T`$. It is therefore $`\pm h_P`$ or $`\pm h_Q`$, respectively. A single fibering would identify their unoriented slopes, contradicting intersection number two. Thus $`M`$ is not Seifert, and it is not atoroidal because $`T`$ is essential. The one-torus collection cutting it into $`P,Q`$ is minimal. Hatcher Theorem 1.9 gives the canonical JSJ collection $`\{T\}`$. This is a genuine two-block exterior, rather than a redundant torus inside one Seifert piece.

Theorem 14.1 gives empty minimum trace and four vertical annuli for this example. The vertex set is the product of the two four-actual-boundary matching spaces, retaining the unused common boundary as a mark. The distance is the union of their rooted ranges (Theorem 18.1), and the contraction uses one common threshold (Theorem 19.1). Separate local distance-one changes can have global class distance two; separate contractions are not a gluing argument. The empty-trace checker and its independent implementation reproduce this rooted obstruction.


### 22.1. The smallest mixed Hopf witness

Splice positive and negative Hopf three-fibre links, each with one distinguished unknot removed, by

```math
g\mu_P=\lambda_Q,\qquad g\lambda_P=\mu_Q.
```

Retain the other two fibres on each side in their coherent orientations. Each side before deleting the retained curves is a solid torus, and the exchange gives meridional filling of an unknot exterior, hence $`S^3`$. The block bases are both pairs of pants; the fibre-section matrix is

```math
\begin{pmatrix}1&1\\2&1\end{pmatrix}.
```

For general coherent Hopf sign sums $`s_P,s_Q`$ the same meridian substitution gives

```math
k_P=s_P-s_Q,\qquad k_Q=-s_P-s_Q,\qquad
t_P=-s_Q,\quad t_Q=s_P,\qquad q=\gcd(|s_P|,|s_Q|).
```

Here $`s_P=s_Q=2`$, so $`(k_P,k_Q,q)=(0,-4,2)`$. The cut is two reaching annuli in $`P`$ and one degree-four horizontal surface in $`Q`$. Its Euler characteristic is -4 and it has four boundaries, hence genus one. Every spanning class has minimum trace two. This directly refutes the proposed universal empty-trace assertion.

The two pair-of-pants seams form one unmarked joint class, so this example has $`X`$ a point despite its nonempty trace. Within-side coherent linking is +1 on $`P`$, -1 on $`Q`$, and cross-side linking -1; all pairwise linkings are nonzero, so it is non-split. Fibre intersection two and the centre argument in Section 22.0 show that the common torus is the genuine two-block JSJ cut.

### 22.2. A six-vertex mixed support with demand two

For a nontrivial support take eight actual $`P`$ fibres, five positive and three negative, and two positive actual $`Q`$ fibres. Then $`s_P=s_Q=2`$, still $`(k_P,k_Q,q)=(0,-4,2)`$. The zero-side base has nine ordinary circles.

The following capped planar graph has one negative JSJ vertex $`J=(-2,0)`$ of demand two, one negative actual vertex $`N=(2,0)`$, and three positive actual vertices
$`p_1=(0,1),p_2=(0,0),p_3=(0,-1)`$. Join $`J`$ to each $`p_i`$ by edge $`a_i`$ and $`N`$ to each by $`b_i`$. Add an outer positive vertex $`A=(-5,0)`$ and negative vertex $`B=(5,0)`$, with directed edges $`e_0:B\to(0,4)\to A`$ and $`e_1:B\to(0,-4)\to A`$. Finally add a forced edge from negative $`(1,6)`$ to positive $`(-1,6)`$.

The outer lens contains the theta component, while the forced actual pair lies outside it. Thus the two outer edges are ordinarily nonisotopic. There are three graph components and four connected regions $`(O,L,U,D)`$; $`L`$ is a non-disk region between the outer lens and the theta component. In edge order
$`(e_0,e_1,a_1,a_2,a_3,b_1,b_2,b_3,f)`$ the face difference is

```math
Du=(u_L-u_O,\ u_O-u_L,\ u_L-u_U,\ u_U-u_D,\ u_D-u_L,\ 
u_U-u_L,\ u_D-u_U,\ u_L-u_D,\ 0).
```

The three theta matchings choose $`b_i`$ and all $`a_j`$ for $`j\ne i`$; denote them $`M_i`$. Each full matching chooses one outer edge and the forced edge. Use $`(e_1,M_3,f)`$ as reference and $`u_O=0`$. In order $`(O,L,U,D)`$ the six potentials are

```math
\begin{aligned}
(0,0,0,0),\quad &(0,0,0,1),\quad (0,0,1,1),\\ 
(0,1,1,1),\quad &(0,1,1,2),\quad (0,1,2,2).
\end{aligned}
```

Their global distances are their difference oscillations by Theorem 18.1. In particular the first and last are distance two, although their diagrams are geometrically disjoint on this one support. Even globally disjoint representatives exist: their JSJ-sector values lie in $`[1,2]`$; split the common reaching band inside that interval to obtain alternating traces, take parallel horizontal mates, and slightly separate the common forced annulus. The supported flow polytope is $`\Delta^1\times\Delta^2`$, triangulated into three tetrahedra by Theorem 19.1. The multiple demand, disconnected graph, non-disk region, forced bridge and a true nonedge are all present in one actual mixed-trace splice.

### 22.3. An arbitrary-order one-cone witness

Take two regular fibres of the weighted $`(1,r)`$ action, $`r\ge2`$, remove one distinguished unknot, and retain the other positively. The pattern side has an annular base with one retained cone of order $`r`$. Splice to a negative Hopf four-fibre link with one distinguished unknot removed; retain its three actual fibres with signs $`(+,+,-)`$. Use the same meridian–longitude exchange. Both distinguished curves are unknots, so the ambient manifold is again $`S^3`$.

Here

```math
h_P=\lambda_P+r\mu_P,\qquad h_Q=\lambda_Q-\mu_Q,\qquad
A_g=\begin{pmatrix}r&1\\r+1&1\end{pmatrix},
```

and

```math
k_P=0,\qquad k_Q=-(r+1),\qquad q=1,\qquad
\Delta(g h_P,h_Q)=r+1.
```

Cross-side coherent linking is $`-r`$ and all actual pairwise linkings are nonzero. The cut is the unique zero-side seam annulus and a horizontal piece in the other block of Euler characteristic $`-2(r+1)`$ with four boundaries. The resulting connected spanning surface has four boundary components and genus $`r`$, and $`X`$ is a point. This witnesses the low one-cone case for every allowed order, not merely a formal orbifold extension.
