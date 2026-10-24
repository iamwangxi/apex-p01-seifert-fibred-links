# 13. Essential cuts before any fibre classification

[Overview](../README.md) · [Definitions](splice-objects.md) · [Block lemmas](splice-planar-blocks.md) · [References](../sources/bibliography.md)

**Lemma 13.1.** A representative minimising the number $`|F\cap T|`$ has essential intersection circles and essential cut pieces, with no disk or closed piece.

**Proof.** Incompressibility and the irreducible-ball argument remove inessential intersection circles. No component is hidden in the ball, since every surface component has actual boundary. Cut pieces inject into the original surface along essential circles and then into $`M`$, and therefore into their own blocks. A disk would bound an essential cut circle or an essential actual curve; a closed piece would already be a forbidden closed component.

By Hatcher Lemma 1.11 the only possible boundary-compressible cut piece is a boundary-parallel annulus. Unit actual boundary usage forces both its ends onto $`T`$. Its annular parallelism is a solid torus $`R`$. Other pieces inside $`R`$ inject into its cyclic group and have no disks or closed components, so they too are annuli. Their boundaries are primitive longitudinal curves of $`R`$, since they lie on its torus-side annulus.

A meridian disk, followed by disk isotopies in the cut ball, simultaneously straightens this finite primitive annulus system. An innermost annulus has an empty parallelism to a torus-side subannulus. That subannulus has no other trace circle: its cut piece would enter the allegedly empty region. Push across a thin collar on the other side of $`T`$ to remove two circles, contradicting minimality. Thus every cut piece is boundary-incompressible and not boundary-parallel. ∎

The same essentiality conclusion holds if the pair $`(F,T)`$ is almost transverse with simplified intersection in the relative PS sense. Remark 3.1 excludes inessential circles. An innermost empty boundary-parallel cut annulus would itself give a relative product between $`F`$ and $`T`$, with its two boundary intervals collapsed. Simplified intersection excludes it.

We call either position **efficient** when its circles and all cut pieces are essential. Before this step, nonminimal representatives may have boundary-parallel JSJ annuli. No assertion below erases those representatives from the original ambient isotopy class.

## 14. The exhaustive three-case cut theorem

**Theorem 14.1.** Every incompressible spanning class has minimum intersection count $`q`$. The following list covers every efficient representative in every genus.

| Fibre values | Pieces | Common minimum trace | Global components |
|---|---|---|---|
| $`k_P=k_Q=0`$ | Vertical annuli in both blocks | Empty | $`n_P/2+n_Q/2`$ annuli |
| $`k_P=0\ne k_Q`$ | Vertical annuli in $`P`$; one horizontal $`H_Q`$ in $`Q`$ | $`q>0`$ copies of $`h_P`$, all coherent | One $`H_Q`$ with $`q`$ annular extensions, and $`(n_P-q)/2`$ annuli |
| $`k_Pk_Q\ne0`$ | One horizontal surface in each block | $`q>0`$ copies of $`\ell`$, all coherent | One connected surface |

The mixed row with $`P,Q`$ exchanged is included.

**Proof.** Start with Lemma 13.1 and apply Hatcher Proposition 1.12 to every essential piece. A horizontal piece covers the **whole** connected base, hence meets every actual boundary torus. This excludes horizontal pieces in a block with $`k_i=0`$, whose actual curves are fibres.

Suppose $`k_i\ne0`$. On each actual torus its prescribed curve is transverse to $`h_i`$. Also $`\ell`$ is transverse to $`h_i`$, because $`\Phi(h_i)\ne0`$. A vertical annulus therefore cannot have actual boundary or JSJ boundary. There are no closed cut pieces. Thus all pieces there are horizontal. Each connected horizontal piece meets every actual torus, and each such torus has only one curve. There is exactly one connected piece $`H_i`$.

The coorientation of this connected horizontal surface has constant sign on the oriented circle flow. Its JSJ boundary curves are consequently coherent, rather than an arbitrary balanced word. Its degree is $`|k_i|`$, read on an actual torus. Each JSJ boundary meets a regular fibre $`|k_i|/q`$ times, so its number of JSJ boundaries is exactly $`q`$.

If both fibre values vanish, the matrix calculation gives $`\Phi|_T=0`$. Both blocks have only vertical pieces. Any nonempty trace would have both fibre slopes, impossible since their intersection is nonzero. Hence it is empty.

In the mixed row the horizontal side forces the entire trace to consist of $`q`$ coherent curves of slope $`h_P`$. All pieces on $`P`$ are vertical annuli. An oriented annulus has opposite fibre signs at its ends. Therefore there is **no JSJ-to-JSJ annulus**: all JSJ ends have the same sign. Exactly $`q`$ annuli join JSJ to actual boundary, and the remaining $`n_P-q`$ actual ends form $`(n_P-q)/2`$ actual-to-actual annuli. They attach the single $`H_Q`$ to $`q`$ actual $`P`$ tori. The other annuli remain separate components.

In the last row both horizontal surfaces are connected; gluing their $`q`$ boundary pairs makes one connected global surface. The oriented restriction to $`T`$ is $`\mathrm{PD}(\Phi|_T)`$. Any representative has at least $`q`$ essential trace curves when $`q>0`$. The efficient representatives above attain that number, so they give the minimum in every class. ∎

For the zero side write the actual oriented fibre signs as $`\sigma_j=\pm1`$. The section presentation and $`k_P=0`$ give

```math
\psi(d_j)=\sigma_j,\qquad
\psi(d_J)=-\sum_{j=1}^{n_P}\sigma_j,\qquad
q=\left|\sum_j\sigma_j\right|.
```

Indeed an actual meridian $`d_j^{a_j}h_P^{b_j}`$ has value one, so $`a_j=\psi(d_j)=\pm1`$. Thus $`q\le n_P`$ and $`n_P-q`$ is even. All JSJ ports have sign $`\sigma_J=\mathrm{sign}(\psi(d_J))`$ and demand $`q`$. Actual ports have demand one. This is a coherent single multiple port, not a general two-sided return-arc problem.

Every block complement is connected. For a vertical zero-side system, each cut joins two previously unused actual circles, or an unused actual circle to the boundary already containing $`J`$. It never disconnects the base. For a horizontal piece the restriction $`\Phi_i`$ is primitive, because it sends an actual meridian to one; the connected nonzero relative class is nonseparating. Hatcher's horizontal-surface argument gives its complete complement $`H_i\times I`$. The two connected complements glue along the cut torus annuli, so the whole global complement is connected.

All vertices have the same norm

```math
N=|k_P|(n_P-1)+|k_Q|(n_Q-1).
```

Horizontal degree gives $`\chi(H_i)=|k_i|(1-n_i)`$; vertical pieces and circle gluings contribute zero. There are no disks. A reduced norm-minimiser can be compressed to an incompressible representative without increasing norm, retaining all actual boundaries and deleting closed components. Applying the classification to it shows its norm is $`N`$. Hence **all** our incompressible vertices are norm-minimising. This is proved before using PS's class-minimum theorem; no positive-genus incompressible vertex is omitted.
