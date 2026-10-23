# 1. Objects and main theorem

[Overview](../README.md) · [Definitions](objects.md) · [References](../sources/bibliography.md)

Let $`L\subset S^3`$ be a nonempty tame oriented non-split link, $`E=E(L)`$ its exterior and $`T_i=\partial N(L_i)`$ its labelled boundary tori. Let

```math
\phi:\pi_1(E)\longrightarrow\mathbb Z,\qquad \phi(\mu_i)=1,
\qquad \alpha=\mathrm{PD}(\phi),
```

where each meridian is positive for the actual component orientation. A spanning surface is compact, properly embedded and oriented, has no closed components, and has exactly one oriented boundary curve on each $`T_i`$, extending to the given oriented link. Incompressibility is componentwise. Equivalence is ordinary ambient isotopy starting at the identity; boundary curves may slide on their own labelled tori. Disks are included in our incompressibility convention. These are the reduced link-spanning conventions, as opposed to adjoining null-homologous closed components.

If $`\lambda_i`$ is the individual preferred longitude, the boundary slope is forced:

```math
\gamma_i=\lambda_i-s_i\mu_i,\qquad
s_i=\sum_{j\ne i}\mathrm{lk}(L_i,L_j).
```

Indeed $`H_1(E;\mathbb Z)=\bigoplus_i\mathbb Z[\mu_i]`$ and $`[\lambda_i]=\sum_{j\ne i}\mathrm{lk}(L_i,L_j)[\mu_j]`$. The coefficient of $`[\mu_i]`$ in the zero class $`\sum_i(\lambda_i+b_i\mu_i)`$ is $`s_i+b_i`$, giving the formula. Also $`\phi(\gamma_i)=0`$, and $`\gamma_i`$ is the primitive kernel slope of $`\phi|_{T_i}`$. Intersection with the whole oriented surface represents $`\phi`$.

**Lemma 1.1 (one complete block).** The complement of a spanning surface is connected, and the cyclic cover associated to $`\ker\phi`$ is obtained by stacking copies of its whole cut-open complement, with one common level for every component.

**Proof.** At a boundary curve of any surface component, a meridian crosses that component once and misses every other component. Deleting its crossing segment joins the two local sides in the complement. In the connected dual graph of complementary regions, each surface-component edge is therefore a loop. Hence that graph has just one vertex. Stacking whole cut blocks gives a cover whose monodromy is intersection with the entire surface, namely $`\phi`$. A loop in the complement has zero intersection, so each complete block lifts homeomorphically. ∎

For representatives $`S,R`$, choose one connected lift $`V_R`$ of the **whole open** complement and let $`V_{S,j}=\tau^jV_{S,0}`$ be the complete open $`S`$ blocks. Set

```math
D(S,R)=\max\{j:V_{S,j}\cap V_R\ne\varnothing\}
       -\min\{j:V_{S,j}\cap V_R\ne\varnothing\},
\qquad
\delta([S],[R])=\min_{S'\in[S],\ R'\in[R]}D(S',R').
```

This is the open-block convention of Przytycki–Schultens (PS), Definition 2.1, pp. 1492–1493. Distinct vertices are adjacent exactly when $`\delta=1`$; $`X(L)`$ is the flag completion of this graph. Its realisation has the usual CW topology. There is no independent deck choice for separate surface components.

**Theorem 1.2.** If $`E(L)`$ is Seifert fibred, $`|X(L)|`$ is contractible. For a chosen fibering with oriented regular fibre $`h`$, put $`k=\phi(h)`$.

- If $`k\ne0`$, $`X(L)`$ is a point, including the solid-torus exterior.
- If $`k=0`$, the vertices are joint isotopy classes of positive-negative unit-demand matchings on a planar base with marked unused auxiliary holes. The classification, vertex bijection and exact class distance are given in §§2–5. Common-threshold decoding of the matching flows gives finite inclusion nullhomotopies in §§6–7.

The proof order is [classification](classification.md), [closed orbifolds and two boundaries](two-boundaries.md), [vertex bijection](vertex-bijection.md), [class distance](class-distance.md), [fixed-graph decoding](matching-carrier.md), and [contractibility](contractibility.md). The [double-cone example](double-cone-example.md) records a geometrically disjoint pair at class distance two.

The target competition paper proves the knot case and a link extension under a condition forcing spanning surfaces to be connected. Here spanning surfaces may be disconnected, and edges use cyclic class distance. On the common range where spanning surfaces are connected the two complexes agree; no identification is asserted for general disconnected surfaces. See [scope](scope.md).

The external geometric inputs are Hatcher's essential-surface and Seifert filling models; Schultens' **closed** good-aspherical-orbifold Proposition 25; PS Definition 2.1 and Proposition 3.2, with its stated §3 Sakuma interface; and Kakimizu's geometric connectivity Theorem A for the fibred point case. The contraction uses standard surface topology and the CW compact-image and Whitehead theorems. PS §§4–7 and Schultens' Remark 35 are not used. The [bibliography](../sources/bibliography.md) states the editions, printed pages and dependency boundaries.
