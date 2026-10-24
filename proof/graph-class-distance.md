# 35. The global class-minimum formula

[Overview](../README.md) · [Definitions](objects.md) · [Graph-manifold theorems](graph-theorems.md) · [References](../sources/bibliography.md)

Put the zero diagrams into ordinary normal position, keeping parallel counts. Align unused zero-to-zero port values. Transport the actual boundary tracks into the horizontal cluster states and solve the integer edge equations on $`\mathscr B`$. Fix one global zero chamber to level zero. Let $`n_z`$ be the resulting integral ordinary difference potential in zero block $`z`$, including its transported constant.

The tree equations and Lemma 31.1 make this decorated normal data unique up to one common constant. Normalising the zero diagrams without transporting those constants would define a different, incorrect quantity.

**Theorem 35.1 (class minimum with one deck displacement).** If zero blocks exist,


```math
\boxed{\quad
\delta_M(a,b)=
\max_{z,f}n_z(f)-\min_{z,f}n_z(f).
\quad}
\qquad\text{(35.1)}
```


For the one-zero-block horizontal-leaf star, this is just its ordinary central difference-current oscillation. If there is no zero block, the entire vertex set is a point.

**Lower bound and minimum comparison.** All incompressible vertices are norm-minimising by Section 30. Apply PS Lemma 3.5 to the **three surfaces** $`A,B,\mathcal T`$, where the disjoint torus union is the third surface. Return the torus union to the chosen one by a common ambient isotopy. The spanning pair is globally simplified, so PS Proposition 3.2 gives $`D_M(A,B)=\delta_M(a,b)`$. Simplified pairs with $`\mathcal T`$ give essential cuts.

Use Lemma 31.2 to identify their ordinary zero diagrams and cluster states with those of $`a,b`$. By Lemma 33.1 the global overlap range is exactly this minimum width. First put the reference surface $`B`$ in standard block forms, including geodesic zero cores, by one torus-preserving ambient isotopy carrying the whole pair. Normalise the other zero diagrams against this fixed reference by Lemma 33.2, with the two names interchanged if necessary; the range rule is unchanged by negating the difference potential. Keep the **absolute** range values and boundary tracks.

A common local ambient isotopy extends over neighbouring collars and carries both surfaces. A single-system disk, half-bigon, or packet move introduces only values already in the old range. At an unused port the old value is retained. At an active port, extend the recorded trace motion into the cluster and use Lemma 34.1 with the inherited boundary lifts; it gives the same relative cluster class and adds no value outside the old global interval. The horizontal representative $`A_*`$ in that lemma is only used to identify the relative class; its intermediate width is irrelevant. No assertion is made that all intermediate isotopy times have bounded width. The endpoint representative after refilling does, which is what class minimisation needs. The construction may be repeated at different ports of the same cluster; its relative integer data are carried, never renormalised.

After finitely many such moves the zero diagrams are normal and their relative constants are exactly the decorated normal data above. Therefore their union of ranges has width at most the original $`\delta_M(a,b)`$. This is the relative-product comparison. It does not assume that a disconnected local union is one complete local cyclic block, and does not apply local PS Proposition 3.3 to parallel packet frontiers.

**Upper bound.** Choose the normal zero representatives attaining those decorated ranges. Common copies may remain coincident; partial coincidences are allowed for computing the minimum over representatives. If transverse disjoint traces are preferred, separate each common port annulus in a disjoint thin band. Its two old values agree at an integer $`r`$; the new strip can have value $`r+1`$ or $`r-1`$. For distinct vertices the old global width is at least one, so choose a side staying inside the old interval. This preserves multiplicity and the ordinary diagram; record its boundary track.

Choose adapted zero-side circle maps, with each cut chamber taking values strictly between its two wall phases. Disconnected chambers cause no obstruction to this extension. Apply Lemma 34.1 to each horizontal cluster, with the same inherited real lift. On empty interfaces glue the already equal constant phases. The resulting whole representatives are in the required ordinary classes and have no new index outside the union of zero ranges. Their width is exactly that union, by Lemma 33.1. Hence (35.1) is attained.

If that width is zero, the zero currents coincide, so all diagrams agree; the transported constants agree globally, so all cluster states agree by the tree equations. The ordinary vertex theorem gives $`a=b`$. Thus distinct vertices have positive width. ∎

A normal crossing in any zero block forces three consecutive values by (33.2). Hence a cyclic simplex has canonical noncrossing zero arc cores. This is a **global class-distance** crossing obstruction.
