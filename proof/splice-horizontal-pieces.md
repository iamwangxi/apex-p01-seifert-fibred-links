# 15. A horizontal piece with one marked JSJ boundary

[Overview](../README.md) · [Definitions](splice-objects.md) · [Block lemmas](splice-planar-blocks.md) · [References](../sources/bibliography.md)

**Lemma 15.1 (horizontal relative uniqueness).** Let $`Q=S^1_h\times B`$ have at least one actual torus, let $`\phi_Q`$ send every actual meridian to one, and let $`k=\phi_Q(h)\ne0`$. Fix a fibre-transverse embedded coherent JSJ trace $`\beta`$ representing $`\mathrm{PD}(\phi_Q|_T)`$, as for all the standard straight traces used below. Horizontal pieces in that class with this trace exist and have one relative ambient-isotopy class, fixing $`T`$ pointwise and allowing actual boundary curves to slide.

**Proof.** Start with a canonical map $`k\theta+f(x)`$ inducing $`\phi_Q`$, linear near its boundary tori. A fibre-transverse coherent trace supplies a boundary phase map with the same class, zero set $`\beta`$, and strict fibre derivative of sign $`k`$. The difference from the canonical boundary map lifts to a real function. A cutoff in a fibre-product collar interpolates to this phase map, preserving the strict fibre sign and leaving all actual boundary maps unchanged. This constructs a submersion in class $`\phi_Q`$ with connected horizontal zero fibre and prescribed trace; primitivity gives connectedness.

A connected cooriented horizontal piece is a global cross-section of the oriented periodic circle flow, with direction sign $`k`$. Flow boxes and positive parametrisation of the return intervals give a circle map $`f_H`$ with zero fibre exactly the piece, inducing $`\phi_Q`$ and with $`df_H(h)`$ strictly of sign $`k`$. Equivalently one assigns one positive phase turn to each successive interval between horizontal intersections on a circle fibre. The coherent ordering makes this assignment independent of a sheet label. This is also the interval-fibre construction of Hatcher's horizontal bundle complement.

Choose a fixed boundary circle map $`f_T`$ with this zero fibre and cohomology $`\phi_Q|_T`$, strictly monotone along the fibre in direction sign $`k`$. For instance use the restriction from the first horizontal piece. A linear map is possible after equally spacing a straight trace, but is not required for a fixed arbitrary trace. Take a fibre-product collar, with the maps constant in the normal collar coordinate near its boundary; the proper horizontal collar can first be flattened relative to $`\beta`$. The two restrictions have the same class. Their difference has a real lift on $`T`$, vanishing on every component of $`\beta`$: on each intervening annulus both phases run from zero to one with the same orientation. A cutoff constant along the fibres interpolates to $`f_T`$ near $`T`$. The fibre derivative is a convex combination of derivatives with the same strict sign. The zero surface moves by an isotopy fixing $`\beta`$; relative isotopy extension fixes the entire boundary torus.

For two resulting maps $`f_0,f_1`$, the difference has a global real lift $`u:Q\to\mathbb R`$ because both maps induce $`\phi_Q`$. On the connected torus collar it is an integer constant; subtract that integer so it is zero there. Now

```math
f_s=f_0+s u\pmod1
```

still has fibre derivative of the same strict sign and is fixed on that collar. Its zero fibres form a proper isotopy, with one curve on each actual torus because the restriction there is primitive. Isotopy extension gives the required ambient isotopy relative to $`T`$. ∎

A canonical choice is

```math
f_B(\theta,x)=k\theta+f(x)\pmod1,
```

where the base map supplies the remaining cohomology. It can be made linear on all boundary tori. Its zero fibre $`H`$ is connected by primitivity of $`\phi_Q`$. The return map of the flow $`h/k`$ is the finite-order map

```math
\rho=R_{1/k}|_H,\qquad \rho^{|k|}=\mathrm{id},
\qquad Q=(H\times[0,1])/((x,1)\sim(\rho x,0)).
```

It cyclically advances the $`q`$ JSJ boundary components by one. In coordinates
$`h=a\ell+b u`$ with $`\phi_Q(u)=q`$, one has $`k=bq`$ and the return translation has transverse component $`1/q`$. Thus the phase loop $`f_B^{-1}(s)`$ returns to the same unlabelled surface at $`s=1`$ and moves the trace through one cyclic port step.

This explicitly absorbs the integer winding of the unlabelled coherent trace configuration. A full transverse torus-translation loop gives $`q`$ such steps; translation tangent to $`\ell=h_P`$ fixes the vertical zero-side annuli as sets. Consequently no integer or finite cyclic gluing-twist parameter remains after the ordinary boundary-motion quotient. The actual-boundary sliding convention is essential in Lemma 15.1; a pointwise marking of all actual boundary curves would be a different problem.
