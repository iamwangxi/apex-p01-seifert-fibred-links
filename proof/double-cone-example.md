# 8. Two retained cones and a disjoint pair at class distance two

[Overview](../README.md) · [Definitions](objects.md) · [References](../sources/bibliography.md)

The order-independent model must still use true cyclic edges. A concrete example occurs already on four actual holes with two retained cones. It is realised, for example, by four regular $`(2,3)`$ fibres with balanced signs, an oriented $`T(8,12)`$.

In a capped sphere picture put positives $`1=(0,0),2=(5,0)`$ and negatives $`3=(2,0),4=(7,0)`$. The directed edges are

```math
\begin{aligned}
e_0&:(2,0),(0,0), & e_1&:(2,0),(1,-1),(0,0),\\ 
f_0&:(7,0),(5,0), & f_1&:(7,0),(6,-1),(5,0).
\end{aligned}
```

Place the order-two cone at $`(1,-1/4)`$ in the left lens and the order-three cone at $`(6,-1/4)`$ in the right lens. Drill small neighbourhoods of the labelled vertices and cones. Each pair of same-end arcs is ordinarily nonisotopic: its lens contains one marked cone and its other side contains the other features. Theorem 4.1 keeps their annuli distinct under ordinary ambient isotopy.

There are three connected regions: the annular outside region $`O`$ and lens regions $`L,R`$. They are **not** four separate boundary walks. Their directed face differences are

```math
D_Gu=(u_L-u_O,\ u_O-u_L,\ u_R-u_O,\ u_O-u_R).
```

The four matchings $`M_{ij}=\{e_i,f_j\}`$ are all geometrically disjoint as subcollections of this one graph. With $`M_{11}`$ as reference and $`u_O=0`$, their potentials in the order $`(O,L,R)`$ are

```math
n_{00}=(0,1,1),\quad n_{01}=(0,1,0),\quad
n_{10}=(0,0,1),\quad n_{11}=(0,0,0).
```

Hence

```math
\delta(M_{01},M_{10})=2,
```

and every other distinct pair has distance one. The carrier is the square polytope triangulated by the true diagonal $`M_{00}M_{11}`$. At its midpoint, the illegal formal vertex average $`([M_{01}]+[M_{10}])/2`$ has the same edge flow as the decoder's valid output $`([M_{00}]+[M_{11}])/2`$. The four matchings even have the same endpoint pairing; their distinction uses actual arc classes, not merely different labels.

This example verifies that extending the proof by a geometric-disjointness shortcut would fail. It is a fixed-support certificate, not a claim that a particular pair of interpolated height functions realises that old vertex average.
