# 21. One retained cone on either side

[Overview](../README.md) · [Definitions](splice-objects.md) · [Block lemmas](splice-planar-blocks.md) · [References](../sources/bibliography.md)

**Corollary 21.1.** The same classification, metric and contractibility conclusions hold if one block has one cone point of arbitrary order $`r\ge2`$ and the other is a planar product, with a genuine common JSJ torus and actual unit spanning boundaries. Replace each horizontal Euler characteristic by its orbifold value. The possible annular one-cone base with one actual and one JSJ boundary is included.

Here are the additional checks, rather than an appeal to an unspecified orbifold extension.

## Cut classification

Hatcher's theorem already includes exceptional fibres. Actual fibre boundary excludes every horizontal zero-side piece, and a nonzero-side horizontal piece still covers every actual boundary. Coherence and trace count $`q`$ are read at the ordinary torus exactly as before. If the cone is on a nonzero side, $`r\mid k`$ follows from $`r\phi(x)+\beta k=0`$ and $`\gcd(r,\beta)=1`$. Here $`\beta`$ is the local Seifert coefficient, independent of the gluing-matrix entry $`c`$. Its Euler contribution is

```math
\chi(H)=|k|\bigl(\chi(B)-(1-1/r)\bigr).
```

## Canonical horizontal fibration and finite return

For $`k\ne0`$, use the locally free circle action of period one on regular fibres, obtained by equivariantly filling the ordinary circle bundle with the Seifert solid-torus model. For any circle map $`f`$ inducing $`\phi`$, lift
$`f(R_tz)-f(z)`$ to $`F(z,t)`$ with $`F(z,0)=0`$. Then $`F(z,t+1)=F(z,t)+k`$. Put

```math
u(z)=\int_0^1\bigl(F(z,t)-kt\bigr)\,dt,\qquad
f_{\rm eq}=f+u\pmod1.
```

The identity $`u(R_sz)=u(z)+ks-F(z,s)`$ proves
$`f_{\rm eq}(R_sz)=f_{\rm eq}(z)+ks`$. This is a smooth representative of the same class, with derivative $`k`$ along the nonzero circle vector field, including the exceptional orbit. Primitivity makes its fibre connected. Boundary corrections constant along the fibre make its torus maps linear. Its return is still $`R_{1/k}`$ of finite order, so the horizontal filling of Section 18.3 works unchanged. The invariant collar construction stays away from the exceptional orbit, with constant $`v`$ near its preimages. Relative horizontal uniqueness uses the same positive flow-box phase construction and interpolation.

## Zero-side ordinary isotopy

Remove a fixed cone disk and keep it marked and unused. Every vertical arc here joins distinct ordinary boundaries: no coherent minimum trace allows a $`J`$-return arc. For at least three ordinary boundaries Lemma A.2's closed-double argument in [the planar-block appendix](splice-planar-blocks.md) detects each arc under arbitrary three-dimensional isotopy. Its closing curve has nonzero rational class $`d_i+d_j`$; the closed double has genus at least two, is good by the paired-cone finite cover, and Schultens’ closed Proposition 25 applies. The group fold, not a continuous ordinary projection through the cone, recovers ordinary arc isotopy. Multiple use of $`J`$ changes none of these distinct-end arguments; actual ends remain unit, and joint straightening retains the port order. Jordan/peripheral detection at the cone excludes the same local products.

## The low case

If the zero block has only one actual circle and one JSJ circle, balance gives $`q=1`$. Its regular base is a pair of pants with the cone boundary unused, and the actual-to-JSJ seam has one free-endpoint class. Relative horizontal uniqueness on the other side gives one global vertex. No torsion closing curve is fed to Schultens’ Proposition 25. In the double-zero case this low block cannot occur, since its single actual sign could not balance with zero JSJ degree.

## Local minimum and carrier

For the other zero-side cases all annuli still have an actual end and connected complement. The direct Proposition 3.3 argument in Lemma 17.1 applies; cone Jordan/peripheral detection substitutes for the ordinary empty-disk check. Graph capping fills the unused cone disk only for circulation. In finite height families every input is constant on its cone collar; convex combinations remain constant there, and the collar phase is among the excluded vertex phases. Deleting circle fibres and recomputing the flow gives the same legal multiport diagrams. All zero-face and exact-recovery arguments remain valid.

In using Lemma 16.1 on a coned zero side with at least two actual boundaries, a nontrivial commutator in the free boundary factor still supplies the kernel $`\mathbb Z^2`$. The low zero-side case is a point directly. Thus no unanalysed nonfibred-isotopy exception is needed.

This does not solve arbitrary coned returning-arc systems. The structural coherence theorem has excluded those systems from the present minimum cuts.
