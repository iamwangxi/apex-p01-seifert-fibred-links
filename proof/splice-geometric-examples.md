# 28. A genuine-family obstruction to the unrestricted carrier

Take the positive/negative Hopf splice construction of Section 22.1, with meridian–longitude exchange. On the zero side retain six actual fibres with signs four positive and two negative; on the other side retain two positively oriented actual fibres. The sign sums are both two. Section 22.1's calculation gives

```math
(k_P,k_Q,q)=(0,-4,2),\qquad
A_g=\begin{pmatrix}1&1\\2&1\end{pmatrix}.
```

This is an actual $`S^3`$ splice with two genuine product JSJ blocks and non-split underlying link by the same construction, not a purely formal matrix. Fibre intersection is two.

On the capped zero-side base draw two disjoint square-shaped petals meeting only at the negative vertex $`J`$ of demand two. Each petal is a four-cycle with two positive actual vertices and one negative actual vertex. In each petal a matching chooses one $`J`$ edge and the opposite actual-negative edge. There are four matching vertices $`M_{ab}`$, $`a,b\in\{0,1\}`$. They all have one common noncrossing graph.

Choose the edge order around $`J`$ as the two edges of the first petal followed by the two of the second. With reference $`M_{00}`$ the potentials on the outside and two petal interiors are

```math
n_{ab}=(0,a,b).
```

All three regions occur in the $`J`$ sector list. Therefore

```math
\mathrm{osc}_J(n_{10}-n_{01})=2.
```

The selected-port word of these two diagrams is $`AABB`$ up to cyclic order, rather than $`ABAB`$. Lemma 24.1 and the simultaneous efficient-cut lemma rule out disjoint global representatives even if one first allows nonminimal intersections with $`T`$. Thus these two matching vertices are **not a geometric edge**. The unrestricted four-vertex simplex on this graph is invalid.

The two three-vertex chains

```math
\{M_{00},M_{10},M_{11}\},\qquad
\{M_{00},M_{01},M_{11}\}
```

are valid trace carriers. In this example every face is incident to $`J`$, so the supported geometric and cyclic complexes actually agree. This is a strict counterexample to the unrestricted-matching step, not to the comparison theorem.

For $`q=1`$ the extra obstruction vanishes: every label occurs just once around $`J`$, so every allocated finite word is one cyclic order. Thus all matchings on a common graph are geometrically realisable in that special mixed case. The distinction begins with $`q\ge2`$.

For a test containing genuine extra geometric edges, add a disjoint actual four-cycle in the outside region. This adds two positive and two negative actual circles, preserving sign sum and $`q=2`$. Its independent bit $`z`$ gives potentials

```math
n_{abz}=(0,a,b,z).
```

Only $`(0,a,b)`$ is read at $`J`$. The supported geometric complex consists of two six-vertex simplices (one for each chain of the $`a,b`$ square), whereas the cyclic complex triangulates the full three-cube by its six ordinary chain tetrahedra. For instance $`(a,b,z)=(1,1,0)`$ and $`(0,0,1)`$ satisfy the trace condition but have full oscillation two. They are a geometric edge and not a cyclic edge. The restricted decoder and the homotopy above handle that edge inside a legal six-vertex carrier.
