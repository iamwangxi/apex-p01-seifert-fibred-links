# 37. The geometric complex and a strong deformation retraction

[Overview](../README.md) · [Definitions](objects.md) · [Graph-manifold theorems](graph-theorems.md) · [References](../sources/bibliography.md)

Simultaneously minimise the total $`\mathcal T`$-trace of a finite disjoint labelled family. The essential-cut proof of Section 30 works for its embedded union, by the finite-family argument in [Section 23](splice-geometric-normalisation.md). No component hidden in a ball can be proper with actual boundary. Innermost empty annular parallelisms remove trace without meeting another member. Thus the family has simultaneous efficient forms. Finite-system Hatcher straightening makes all its zero annuli vertical and its horizontal pieces horizontal while retaining labels and disjointness, including nested packets and cone models.

It follows that a geometric simplex has a canonical common reduced graph $`G_z`$ at every zero block. Its actual vertices have the integral coordinates of Section 36, including the relative levels. For


```math
x=\sum_{i\in\sigma}\lambda_i[v_{u_i}]\in|Y|,\qquad
R(x)=S_G\left(\sum_i\lambda_i u_i\right),
\qquad\text{(37.1)}
```


the decoder is independent of reference, root and representative.

The required geometric carrier is proved directly; it is not the unrestricted assertion that all flows on a common graph are geometrically compatible.

**Lemma 37.1 (weighted-wall carrier).** Every positive-weight output of (37.1), together with the input vertices, is simultaneously geometrically realisable.

**Proof.** Keep actual disjoint efficient representatives of the input simplex and choose thin disjoint bands around all their occurrences. A band phase for each input increases by one across each of its component walls and is zero modulo one off its bands. Its class is $`\Phi`$, and phase $`1/2`$ is the input surface. On the global cover normalise their real lifts once. The weighted phase


```math
h_\lambda=\sum_i\lambda_i h_i
```


still shifts by $`\Phi(\gamma)`$ under every deck element $`\gamma`$, so it descends to a circle map.

In a zero block a regular level consists entirely of arcs in its edge bands. There are no closed circle levels off those bands, because there the phase is constant and excluded. Its signed endpoint demands are unchanged. In a horizontal cluster the disjoint connected fibre pieces have one common cyclic order: cut along one, and every other degree-one piece is a graph in its interval product. Weighting their successive bands gives the same total phase increment one per period. A regular level is one connected fibre graph in that product. Its boundary words match the zero-side levels because the map was global.

Thus every regular global level is an allowed incompressible spanning surface, with no closed components, and distinct levels are disjoint. Choose phases also avoiding the finitely many values of $`h_\lambda`$ on the original component walls. The levels are then disjoint from the whole input family as well.

Off the zero bands, $`h_i-h_R=u_i`$ is the integral face potential. For a level $`r\in(0,1)`$, its relative face vector is


```math
\left\lfloor\sum_i\lambda_i u_i+1-r\right\rfloor.
```


Here the reference is its regular phase $`1/2`$: at a face with integer reference height $`j`$, $`\lfloor j-1/2\rfloor=j-1`$. To read the actual state of a selected level, postcompose the weighted circle map with a degree-one band map supported near $`r`$, avoiding all the finitely many face phases. Its phase $`1/2`$ is exactly that whole level surface, and its lifted value on an old face is $`\lfloor h_\lambda-r\rfloor+1`$. This is a global band map for the selected surface, so it reads its actual relative cluster levels, not just its edge counts. Hence these levels are exactly the vertices in (36.3), with $`\theta=1-r`$. They supply all positive-weight outputs. This proves the carrier simultaneously at both ends of every port-to-port band; no independent endpoint ordering is imposed. ∎

The inclusion $`X\subseteq Y`$ was proved independently in Lemma 36.3. Equation (37.1) fixes $`X`$ pointwise by Theorem 36.2's exact recovery.

Define


```math
\mathcal H(x,t)=(1-t)x+tR(x).
\qquad\text{(37.2)}
```


Lemma 37.1 puts the positive-coefficient vertices of this segment in a geometric simplex, so it remains in $`Y`$. On each closed input simplex there are finitely many possible floor outputs; their barycentric coordinates are continuous. The resulting finite image may be a union of geometric simplices and need not be one full unrestricted simplex. This suffices for continuity on each closed simplex cylinder. Zero-face compatibility makes the restrictions agree. The CW closed-cell-cylinder criterion gives continuity on the ordinary product $`|Y|\times I`$. Thus


```math
\mathcal H(x,0)=x,\quad \mathcal H(x,1)=R(x),\quad
\mathcal H(a,t)=a\quad(a\in|X|).
```


This proves the strong deformation retraction. Flagness of $`Y`$ is not assumed or needed for this argument.
