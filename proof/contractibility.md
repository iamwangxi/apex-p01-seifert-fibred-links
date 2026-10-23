# 7. Finite inclusion nullhomotopies and contractibility

[Overview](../README.md) · [Definitions](objects.md) · [References](../sources/bibliography.md)

**Theorem 7.1.** The entire $`k=0`$ complex of each classified exterior is contractible.

## Common finite height family

In a non-point case, fix a matching $`M_*`$ and a finite subcomplex $`K\subset X`$. Choose the finitely many proper arc classes of their vertices, with a common copy of each repeated class. The crossing obstruction in Lemma 5.4 makes canonical ordinary representatives simultaneous and disjoint on every input simplex. Make a common rational PL approximation and choose thin bands, disjoint for each noncrossing pair and away from collars of **every** $`A_j`$. Only incompatible classes need cross.

For each input matching, define a circle map by $`t_e\pmod1`$ in the transverse coordinate of each of its disjoint arc bands and by zero outside. Both sides of a band have circle value zero, so this is continuous; crossing the band has degree one. It induces the same $`\psi`$, has monotone actual boundary lifts of increment $`\epsilon_i`$, and is constant on every unused collar. Extend it constantly across all cone disks in the underlying base. Normalise the real lifts at one common lifted point outside all bands. For convex coefficients on this finite set of matchings,

```math
h_\mu=\sum_M\mu_M h_M,\qquad
\sum_M\mu_M=1,\quad \mu_M\ge0,\qquad
h_\mu(\tau z)=h_\mu(z)+1.
```

An individual normalised lift is constant with an integer value on a chosen lift of each $`A_j`$. That integer may differ between inputs **and between cones**. Their convex combination is still separately constant on every such circle and disk. It is not forced to be integer or to have one common value at different cones.

**Lemma 7.2 (legal fibres and arc-indicator flow).** For the fixed height family, deleting circle components from each regular fibre gives a legal matching. Averaging its arc indicators gives a nonnegative unit-demand flow $`W`$.

**Proof.** Take one finite common PL triangulation including all band boundaries, crossings, outside-chamber vertices and unused collars. Exclude all triangulation-vertex phases modulo one. At a remaining regular phase, the fibre is an embedded compact PL one-manifold: it has one endpoint on every actual boundary by monotonicity of degree $`\pm1`$, and none on any auxiliary boundary by constancy. Interval components join opposite signs. Removing all circle components leaves a legal $`m`$-arc matching $`A_r(h_\mu)`$. Neither cone disk contributes a fibre piece at a regular phase. Deletion is used for legality alone, not to preserve complementary blocks or the old height potential.

For intervals $`J`$ between vertex phases, with an additional cut at zero, average arc indicators:

```math
W_e(\mu)=\sum_J |J|\,\mathbf1_{\{e\in A_{r_J}(h_\mu)\}},\qquad r_J\in J.
```

The phase intervals have total length one, so each actual boundary has total demand one. This remains an edge flow, not an average of vertices that might be nonadjacent. ∎

**Lemma 7.3 (finite templates and phase collisions).** For the fixed finite height family, all regular-fibre arc classes lie in one finite set $`\mathcal E`$, and the arc-indicator flow $`W`$ is continuous on the whole coefficient simplex, including coefficient faces and simultaneous auxiliary-collar phase collisions.

**Proof.** Choose triangle lifts and retain all corner lifts and integer deck changes. An integer $`L`$ bounds all input corner heights and hence all convex combinations. Only levels $`r+k`$ with $`-L-1\le k\le L+1`$ can occur in a chosen triangle. Recording all triangle segment incidences, edge-intersection orders and gluing translations gives finitely many normal templates. Equal templates are related by order-preserving edge moves extended over triangles, so they determine actual joint proper classes, including winding about either cone. This gives one finite arc-coordinate set $`\mathcal E`$ for the whole coefficient simplex.

The finitely relevant hyperplanes $`a_v=k`$, $`a_v-a_w=k`$ and all coefficient faces fix the integer parts and cyclic order of vertex phases. On each relative open cell every positive-length interval has one fixed template and affine length, so $`W`$ is affine in the common finite space $`\mathbb R^{\mathcal E}`$. At a collision, shrinking intervals have zero limiting weight, and each positive-length interval has a persistent template, seen at an interior phase away from all limiting vertex values. This includes simultaneous collisions of the two cone-collar values, flat triangles and phases crossing zero. Thus $`W`$ is continuous before it is interpreted in $`|X|`$. ∎

**Lemma 7.4 (embedded supports and zero-face gluing).** Each positive support of $`W`$ is embedded. The fixed-graph decoders glue on the finite union of its support polytopes to a continuous decoder $`S`$ with image in a finite subcomplex.

**Proof.** At each parameter the positive-weight arcs have simultaneous disjoint representatives: choose them in the different regular fibres of that same circle map. Delete circles, identify repeated proper classes and straighten. They form an allowed graph $`G_\mu`$ with

```math
W_e(\mu)\ge0,\qquad \sum_{e\ni i}W_e(\mu)=1
\quad\text{for every actual }i.
```

Every phase matching supplies a matching witness. There are only finitely many support graphs, and support can only shrink on a parameter-cell face. Their polytopes are compact subsets of the one finite coordinate space. Intersections are common zero-coordinate faces, where Theorem 6.1 identifies their decoders. Finite closed-set pasting gives a continuous $`S`$ on their union, with image in a finite subcomplex (each graph has finitely many matchings). ∎

## Proof of Theorem 7.1

**Proof.** The two point cases are already complete. Otherwise Lemmas 7.2–7.4 give the continuous map $`F(\mu)=S(W(\mu))`$ in the common height family above.

At an initial input simplex $`\sigma`$ its bands are disjoint. In edge band $`e`$ the height is $`b_e+c_et_e`$, with the actual global offset and

```math
c_e=\sum_{M\ni e}\lambda_M\in[0,1].
```

Outside the bands it is constant at excluded phases. A full parallel copy of $`e`$ therefore occurs for total phase measure exactly $`c_e`$, at most once per regular phase. Hence

```math
W(\lambda)=\sum_{M\in\sigma}\lambda_M\chi_M,
\qquad F(\lambda)=\sum_{M\in\sigma}\lambda_M[M]
```

by exact recovery. At the single base matching every regular fibre is that matching, so $`F(\mathbf e_{M_*})=[M_*]`$. For $`x=\sum_{M\in\sigma}\lambda_M[M]`$ use

```math
C_K(x,t)=F\left((1-t)\sum_{M\in\sigma}\lambda_M\mathbf e_M
                    +t\mathbf e_{M_*}\right).
```

The same functions, normalisations, triangulation and arc-coordinate set are used on every input face. Zero coefficients delete whole summands, including offsets. Thus this is a face-compatible continuous homotopy of the finite inclusion to the fixed vertex, carried by a genuinely finite subcomplex. Critical values at unused boundaries and both cone orders have introduced no additional interface.

Finally the realisation has its CW topology. One-vertex inputs prove path connectedness. A sphere map has compact image contained in a finite subcomplex (Hatcher Proposition A.1); composing with its finite inclusion nullhomotopy makes the sphere map null. All homotopy groups vanish. Whitehead's Theorem 4.5 then makes $`|X|`$ contractible, indeed a point subcomplex is a deformation retract. No assertion that each finite image is itself contractible is needed. ∎

The band/circle-map mechanism follows Hatcher's 2008 second proof, pp. 5–6; the prescribed-boundary flow and decoder are proved here. The decoding potential is recomputed from the retained arc flow after circle deletion; it is not the pre-deletion height. At general interpolation parameters no barycentric average of possibly nonadjacent phase-matching vertices is used.

## Terminating mathematical specification

For every finite PL input this is terminating: the double-coset test of Lemma 4.2 and rational representative enumeration of §5.5 produces the simultaneous representatives; finite rational band refinements give $`T`$; a finite height bound gives the finite hyperplane arrangement; finite templates identify interval components and their arc classes; each finite graph's potential is solved linearly and its threshold cells are finite. The existence of orthogeodesic representatives and small rational approximations proves termination of the initial enumeration. The procedure need not be efficient. The accompanying diagnostic is not claimed to implement this entire arbitrary-input construction.

The constructions in §§3–7 use no theorem asserting contractibility of the complex being studied. Combining Theorem 7.1 with Lemmas 2.1, 2.3 and 2.4 proves Theorem 1.2 for every link in its statement.
