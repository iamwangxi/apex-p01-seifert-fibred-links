# 36. The actual compatible carrier, with relative level directions

[Overview](../README.md) · [Definitions](objects.md) · [Graph-manifold theorems](graph-theorems.md) · [References](../sources/bibliography.md)

Choose finite noncrossing graphs $`G_z`$ of distinct ordinary arc classes in every zero base, containing an allowed global vertex $`R`$. Include all unused cone and empty-port marks in proper arc identity. Direct arcs negative to positive. A zero graph need not be connected or have disk regions. Let $`\mathcal F_z`$ be its connected spherical face set after radial capping solely for circulation. Define


```math
(D_z u)_e=u_{\ell(e)}-u_{r(e)},\qquad
U_e=\min(b_{\partial_-e},b_{\partial_+e}).
```


For every empty edge identify the values of its two unused-port faces. Set one global face value to zero. Write $`m_{R,z}`$ for the reference integral multiplicity flow and put


```math
\mathcal P_G=
\left\{u:\ u_{f_*}=0,\quad
u_{\rho_{z,e}}=u_{\rho_{z',e}}\ \text{on empty edges},\quad
0\le m_{R,z}+D_zu\le U\right\}.
\qquad\text{(36.1)}
```


This is a polyhedron, not necessarily a bounded polytope. Its unrestricted level dimension is $`\#\Lambda-1`$.

**Lemma 36.1 (integral states are precisely global vertices).** Integral points of (36.1) are in bijection with the ordinary vertices whose zero arc classes are supported on the $`G_z`$.

**Proof.** For an integral flow $`m_z`$, make its band phase map: it is zero modulo one off the arc rectangles and increases by $`m_{z,e}`$ across edge $`e`$. A generic phase, say $`1/2`$, is exactly the multiarc with those multiplicities. Relative to the reference, the real difference on a face is $`u_f`$. The empty-face identifications give the required real gluing there. Prescribe these real boundary differences on every horizontal cluster and extend them in its outer collars; the phase classification of Section 32 realises them. Band maps may be flat at phase zero; choose the extension strictly fibre-positive in the cluster interior and nonnegative on the outer boundary. Phase $`1/2`$ remains regular. A strict boundary phase with this same selected fibre gives the same ordinary relative class. This constructs the global class.

Conversely put a supported vertex into these band representatives, carrying its boundary tracks. Its cluster relative phases give integer edge data. The tree equation in Section 32 has a unique solution in the face constants, modulo one common integer. This gives exactly an integral vector (36.1). Lemma 31.1 excludes a further loop identification. Two integral vectors with the same edge flows can still be different vertices, because their relative zero-region levels may differ. ∎

For two band representatives, their lifted phase difference across an edge rectangle is linear between the two **integral** face differences. Each individual phase is monotone across that rectangle. Integer-endpoint inequalities therefore put their floor difference between those same face values; all intermediate packet strips add no extreme. Face values themselves are attained off the rectangles. Their transported cluster states are those used in Lemma 36.1. Consequently Theorem 35.1 reads simply


```math
\delta_M(v_u,v_{u'})=\mathrm{osc}_{\bigsqcup\mathcal F_z}(u-u').
\qquad\text{(36.2)}
```


**Theorem 36.2 (global potential carrier).** The supported actual subcomplex $`X_G`$ triangulates $`\mathcal P_G`$. Its decoder is


```math
u^\theta=\lfloor u+\theta\rfloor,\qquad
S_G(u)=\int_0^1[v_{u^\theta}]\,d\theta,\qquad 0\le\theta<1.
\qquad\text{(36.3)}
```


There is one threshold and one common additive normalisation across **all** zero blocks and all relative level directions.

**Proof.** Integer-endpoint inequalities in (36.1) are preserved by common floor rounding. The demand equations telescope, so every rounded edge count is a nonnegative integer with the required demands. Empty-face equalities are preserved too. Thus Lemma 36.1 makes every output an actual global vertex. Differences between ordered threshold vectors take only the values zero and one; (36.2) makes the output a true cyclic simplex.

Exact expectation follows from $`\int_0^1\lfloor t+\theta\rfloor d\theta=t`$. For a true simplex the integral root-zero potential vectors have pairwise oscillation at most one. They are coordinatewise comparable, and relative to their minimum are nested zero-one vectors. Common rounding of a barycentric average returns every vertex for exactly its barycentric weight. Thus the potential map and decoder are inverse.

Reference change subtracts an integral potential vector and cancels in the floor. Root change rotates the one threshold circle. On bounded pieces only finitely many floor hyperplanes occur, giving continuity. If an edge weight is zero, every positive-measure output omits it. Choose a supported integral reference output; the potential jump there is zero, so deletion merges equal-valued faces, including any empty-port root faces. The state correspondence preserves all relative constants. This proves compatibility on common positive-support faces, including graphs whose other, deleted edges cross. The local circulation argument works for disconnected graphs, bridges and non-disk regions by the spanning-forest and connected-dual argument of [Section 6](matching-carrier.md): each fundamental planar cycle bounds a Jordan potential, these span all circulations, and the region dual has only the common-constant kernel. Radial caps are used only for this calculation and do not erase ordinary arc marks. ∎

When there is one zero region, (36.1) is the ordinary product of integer-demand flow polytopes with their empty-root identifications. For the six-component test there is just one central base, so this proves the identification of the common-threshold construction with its **actual** $`X`$, on reduced supports.

**Lemma 36.3 (geometric realisation of the cyclic carrier).** The positive-weight outputs of $`S_G(u)`$, for any real $`u\in\mathcal P_G`$, have simultaneous disjoint representatives. In particular $`X`$ is a simplicial subcomplex of $`Y`$, without using a geometric-simplex hypothesis on the input.

**Proof.** On a zero face take the reference band phase lift plus the real constant $`u_f`$. Extend that real difference across an edge rectangle linearly between its two face values. The transverse phase increment is


```math
w_e=m_{R,e}+u_\ell-u_r\ge0.
```


Around every ordinary boundary the total increment is its prescribed integer demand, so this is a circle map in the same class, not just a collection of unrelated rectangle maps. At unused cone circles it extends constantly. Empty-face equalities glue it across empty interfaces.

On each cluster extend the prescribed real boundary difference from the reference phase map using outer-collar cutoffs constant along the Seifert fibres. Its normalised fibre derivative is a convex combination of the nonnegative prescribed boundary derivative and the positive reference interior derivative. Thus it is strictly positive in the interior and has only the excluded flat boundary phases at the outer interface. The real difference extends over the cluster, so the map has exactly the relative state specified by $`u`$. The JSJ tree gives the global class $`\Phi`$.

Exclude the finitely many zero-face phases. A regular level has only proper zero arcs in the edge rectangles and connected horizontal pieces in the clusters. It has no closed component and is an incompressible spanning surface. Distinct regular levels are disjoint. At a reference face of integer height $`j`$, the level $`r\in(0,1)`$ has relative integral coordinate


```math
\lfloor j+u_f-r\rfloor-\lfloor j-1/2\rfloor
=\lfloor u_f+1-r\rfloor.
```


Thus these are precisely the decoder outputs, with their relative levels as well as their edge counts. For a true $`X`$ simplex take an interior barycentric average. Exact simplex recovery in Theorem 36.2 makes every input vertex one of these positive-weight outputs. Choosing one regular level for each gives the required whole geometric simplex. ∎
