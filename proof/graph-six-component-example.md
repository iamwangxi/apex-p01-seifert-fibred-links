# 39. The six-component example in full

[Overview](../README.md) · [Definitions](objects.md) · [Graph-manifold theorems](graph-theorems.md) · [References](../sources/bibliography.md)

**Theorem 39.1 (six-component example).** The oriented six-component Hopf-splice link below has $`X=Y`$ an infinite tree, with an infinite-valence vertex. Its ordinary vertices and exact class distances are the central demand-$`(2,2,1,1)`$ multiarc model, including parallel port annuli.

The actual $`S^3`$ construction and its two genuine JSJ tori are given below by meridian–longitude exchange of Hopf-fibre ports. Start with a negative Hopf four-fibre link, designating two components as ports and retaining two actual components. At each port splice a positive Hopf three-fibre link with one designated port and two retained actual fibres. The gluing is


```math
\mu_{U_i}\longmapsto\lambda_{V_i},\qquad
\lambda_{U_i}\longmapsto\mu_{V_i}.
```


All designated components are unknots. Each replacement is an unknot exterior, a solid torus whose meridian maps to the removed tube's meridian. The ambient manifold therefore remains $`S^3`$, and the other central port remains an unknot after the first replacement. There are six actual components.

The centre is a four-holed-sphere circle product and each leaf is a pair-of-pants circle product. Their boundary groups inject, and gluing gives irreducibility and incompressible internal tori. Neither side is a torus product, so neither torus is boundary-parallel. Adjacent fibre slopes have intersection two. The centre of each block group is its fibre factor; a common orientable Seifert fibering would restrict to those factors on both sides of an incompressible torus, contrary to the different slopes. A horizontal torus cannot occur in a Seifert piece with nonempty boundary. A nonorientable base is excluded by the embedded-Klein-bottle obstruction in $`S^3`$. Removing either cut would leave a piece neither Seifert nor atoroidal, so Hatcher's JSJ minimality criterion gives exactly these two genuine tori. The exterior is irreducible and the link is non-split.

For coherent actual sign sums $`(a_0,a_1,a_2)`$, the preferred-longitude relations give


```math
\Phi(\mu_{U_i})=a_i,\quad
\Phi(\lambda_{U_i})=-(a_0+a_j),\quad j\ne i,
```



```math
k_0=-(a_0+a_1+a_2),\quad
k_1=a_1-a_0-a_2,\quad k_2=a_2-a_0-a_1,
\qquad q_i=\gcd(|a_i|,|a_0+a_j|).
```


Coherent meridians of negatively oriented actual components have value minus one; their actual orientation meridians have value plus one. Auxiliary port meridians need not have value one. With $`d=\mu`$, $`h_0=\lambda-\mu`$, $`h_i=\lambda+\mu`$, each gluing matrix is the matrix displayed below. These relations also supply the relative-height example in Section 40.

The central block has two actual fibres of signs $`(+,-)`$; leaf 1 has $`(+,+)`$, leaf 2 has $`(-,-)`$. The covariance matrix and values are


```math
A=\begin{pmatrix}-1&1\\2&-1\end{pmatrix},\quad
(k_0,k_1,k_2)=(0,4,-4),\quad(q_1,q_2)=(2,2).
```


All efficient vertices have three central annuli and one degree-four leaf piece in each leaf. Both leaf pieces have $`\chi=-4`$, genus one, and four boundaries. Put $`x=1`$ if the two central actual ends are paired, otherwise $`x=0`$. Endpoint conservation gives


```math
\#(J\!-\!J)=1+x,\qquad
\#(\text{actual}\!-\!J)=2(1-x),\qquad
\#(\text{actual}\!-\!\text{actual})=x.
```


For $`x=1`$, the two port seams must be parallel: two disjoint nonparallel port seams separate the two actual holes, making their joining seam impossible. The resulting surface has a separate actual annulus and one genus-three component with four actual boundaries. Its central cut complement has a solid-torus chamber between the parallel annuli.

For $`x=0`$, the three arcs form a tree connecting all four ordinary circles. The cut base is a disk. The global surface is connected, of genus two with six actual boundaries. Both types have complexity eight. This classifies every genus and every component pattern, not only a selected family.

There is one zero block and two horizontal leaves. By Section 32 no relative integer remains. By Section 35,


```math
\delta_M(a,b)=\mathrm{osc}n_{a-b}
```


for the ordinary-normal central current, including all parallel copies. Thus Section 36 identifies the integer-demand carrier with the actual cyclic complex, and Section 38 contracts it.

## 39.1. In fact X is an infinite tree

A true cyclic simplex has a common reduced bipartite support on four boundary vertices. If the support is disconnected and feasible, its components must be the port pair and the actual pair; the other bipartite partition would have demands two and one in a component and is infeasible. The disconnected reduced support has only one edge for each pair: a second parallel-class coordinate would bound an empty rectangle on the side not containing the other component. It supports just the multiplicity vector $`(2,1)`$.

If the support is connected, it has $`V=4`$ and no empty digon, since arc coordinates are distinct ordinary classes. Every spherical face boundary walk has length at least four; a two-sided bridge face would require the whole component to be one edge. Euler's formula gives $`E\le2V-4=4`$. Its circulation dimension is at most $`E-V+1=1`$. The actual carrier therefore has dimension at most one. Hence the entire $`X`$ is a graph. It is connected and contractible by Section 38, so it is a tree.

Choose disjoint port and actual seams $`p,f`$, and let $`D`$ be the vertex $`2p+f`$. Complete them to a noncrossing four-cycle with the two cross-pair seams $`r,s`$. The other integral flow is $`p+r+s`$, a connected vertex $`C`$; their cycle difference has potential oscillation one. Twist the cross-pair seams by $`n`$ turns about the essential circle separating the port pair from the actual pair, keeping $`p,f`$ fixed. The resulting $`C_n`$ are distinct ordinary vertices, and every $`C_n`$ is adjacent to $`D`$ by the same four-cycle calculation. Distinctness follows from the nonzero twisting of a proper arc crossing that circle, or its ordinary peripheral path word. Thus $`D`$ has infinite valence and $`X`$ is infinite.

There is also an explicit global contraction for this example. Give every tree edge length one, fix root $`D`$, and let $`\ell(x)`$ be the length of the unique finite path from $`D`$ to $`x`$. Send $`x`$ at time $`t`$ to the point of that path at distance $`(1-t)\ell(x)`$ from $`D`$. On each closed edge cylinder the image lies in finitely many root-path edges and the formula is continuous. It agrees at endpoints. The CW cylinder criterion therefore makes it continuous on the ordinary product of the whole, non-locally-finite tree with $`I`$. This is a face-compatible contraction fixing $`D`$.

## 39.2. Here Y equals X

A geometric pair has a common reduced central graph by simultaneous efficient normalisation. A feasible disconnected graph gives one vertex. A feasible connected reduced graph has at most four edges and circulation dimension at most one. If it has a four-cycle, its flow interval has integer length at most one because the cycle meets a unit actual boundary. If its cycle is the two port edges, reducedness puts one actual vertex on each side of that cycle; otherwise the other side would be an empty digon. The two actual bridges therefore each consume one port demand, leaving total port-cycle flow one. Other two-edge cycles meet an actual unit demand and have the same bound. A tree has a single flow. Thus distinct geometric vertices have cyclic distance one.

Conversely $`X\subseteq Y`$ by Section 37. Since the graph $`X`$ is a tree, there is no three-vertex pairwise geometric clique and hence no geometric simplex of dimension two. Therefore $`Y=X`$, with the same CW realisation. Its strong deformation retraction is the identity. This proves Theorem 39.1.
