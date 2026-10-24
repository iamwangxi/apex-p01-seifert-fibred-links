# 33. The overlap potential and the new packet comparison

[Overview](../README.md) · [Definitions](objects.md) · [Graph-manifold theorems](graph-theorems.md) · [References](../sources/bibliography.md)

## 33.1. Whole-complement width as a difference current

For two cooriented homologous surfaces $`A,B`$, form the dual graph crossing **both** currents, with jump $`+1`$ across $`A`$ and $`-1`$ across $`B`$. Common faces cancel as currents. Its cycles have weight $`\Phi-\Phi=0`$. It has a single integer potential $`h_{A-B}`$, up to one constant. This construction is on all chambers, not on a chosen connected local complement.

**Lemma 33.1.** For whole spanning surfaces,


```math
D_M(A,B)=\mathrm{osc}h_{A-B}.
\qquad\text{(33.1)}
```


**Proof.** Make an adapted circle map $`f_F`$ dual to each surface: in its whole cut complement its lifted value lies strictly between two consecutive integers, and the two faces have values zero and one. Such a map is constructed by collar extension into the cut manifold. Lift the whole $`B`$-complement once. Its $`B`$-phase has integer part zero. The integer part of the $`A`$-phase is exactly the complete $`A`$-block index. On projection this is the difference-current potential, including its $`-1`$ jump when the selected $`B`$-block is continued across a projected $`B`$-face. Every open chamber attains its index and every open block intersection contains such a point. This gives (33.1).

Equivalently use the two real phase lifts on the global cover and their real difference. There is one common deck normalisation, even if a local restriction has many chambers or nonprimitive image. ∎

The restriction to a zero block is the corresponding local difference-current potential. Its normalisation is inherited from the global one. It is **not** a local complete-block metric.

## 33.2. A range-reduction rule

Here is the elementary replacement for applying Sakuma to nonparallel local frontiers.

**Lemma 33.2 (tracked blister and packet reduction).** Let $`P`$ be a genuine planar Seifert block. Consider two oriented incompressible annulus systems with equal coherent signed boundary demands, every annulus joining distinct ordinary boundary components. Arbitrary integer demands are allowed. Ordinary normalise their joint regular-base arc classes, while carrying their actual boundary-motion paths. Then their local difference-current range does not increase. Values at untouched boundary collars remain unchanged. The only remaining relative products in normal position are products inside a common parallel packet; their reduced range is already the endpoint range.

**Proof.** We give the moves and their range checks; this is not a claim that local PS simplified intersection holds.

First verticalise the first system, carrying the second. This common ambient isotopy preserves the range. Hold any already coincident annuli fixed and work in all components obtained by cutting them; no other annulus of either system crosses a common annulus. Straighten boundary curves of the second against the fibre curves of the first by empty boundary bigons. The curves are coherent on each boundary torus. Extend the moves in a common collar of the pair.

For an empty bigon or half-bigon, the old crossing has four sectors of values


```math
(c,c+1,c,c-1)\quad\hbox{or}\quad(c,c+1,c+2,c+1),
\qquad\text{(33.2)}
```


up to an overall integer, sign, and cyclic order. After the disk push every newly occurring value is one of those old values. The regions outside the push keep their values. The collar version has the same sector check. Thus a free-end half-bigon at a multiple port is legitimate; it is not silently discarded as a rel-boundary isotopy. Its endpoint path is recorded for Section 34.

Now intersections in the interior are circles. A trivial one is trivial on both annuli, by their group injections. Use an innermost disk of the first system and the corresponding disk of the second. Their sphere bounds a ball. Its interior contains no component of the moving system: its disk is one boundary face, the other disk is disjoint from that system, and a whole proper component cannot be hidden in a ball. Other pieces of the fixed system can be present. Each of their complementary chambers in this ball meets the moving disk face; the chamber adjacent to the other disk also meets that face near its circular edge. Removing the moving disk changes its value by one to the value already on the other side of that old disk face. Thin separation at the edge uses (33.2). Hence the ball move introduces no new extreme. Nested disks are cleaned first, and the trivial-circle count decreases.

All remaining circles are essential cores on both systems. Straighten them on the fixed vertical annuli to fibres by an isotopy preserving those annuli. Cut along the fixed annuli, in **every** resulting component. The second system cuts into incompressible annuli with fibre boundary. Each is essential or boundary-parallel. Hatcher's relative theorem verticalises the former; the latter is straightened in its boundary parallelism. Induct by cutting along one straightened annulus at a time, fixing all previous faces. This includes components with exceptional fibres and disconnected cuts. It is an ambient isotopy fixing the first system, so the difference-current range is unchanged. Gluing gives two vertical multiarcs.

Remove ordinary bigons and free-end half-bigons in the regular base. Their products with a fibre are precisely the disk/blister moves just checked; the ordinary bigon criterion terminates at the normal representatives. A cone or unused boundary inside the proposed disk prevents an empty bigon and is never filled for this step. The ordinary annulus detector in Section 31 excludes an additional three-dimensional product between different ordinary proper classes.

Finally handle common classes as packets. A parallel rectangle between two such arcs can contain only parallel strands: it has no cone or boundary hole, and coherent endpoint signs prohibit a returning strand. Read a transverse packet word. Its prefix heights add $`+1`$ for an $`A`$ copy and $`-1`$ for a $`B`$ copy. If the counts are $`a,b`$, cancel $`\min(a,b)`$ pairs by aligning copies in their existing order, leaving the residual monotone word of sign $`a-b`$. Its height range is


```math
[\min(r,r+a-b),\max(r,r+a-b)].
\qquad\text{(33.3)}
```


Both endpoints already occurred in the old prefix word, so no new extreme is introduced. No two components of the same system are identified. The coincident pairs remain present geometrically and cancel only in the **difference current**.

Noncommon normal products would give an empty bigon, a half-bigon, or equality of full proper classes, all already handled. A product pairing an extra strand with a common strand can remain inside a packet; (33.3), rather than the old unit-end coincident-face argument, proves that it cannot reduce the endpoint range. Thus no assertion of local PS simplified intersection is needed.

Every move has a specified collar track. In particular one does not reset the potential constant after moving a port. Relative integers may be transported from a zero diagram into its adjacent cluster; they are not erased. ∎

The ordinary geodesic normal form is independent of the chosen bigon sequence. With multiplicities, the only extra choices are the orders of identical strands in a packet, whose range is (33.3). Collapsing a packet to a weighted core preserves its extrema. After expanding multiplicities, each single-copy crossing has three consecutive integer values by (33.2), even when the local cut complement is disconnected. If the two compressed noncommon cores have multiplicities $`a,b>0`$, their outer-sector value set is $`\{c,c+a,c-b,c+a-b\}`$, with range $`a+b\ge2`$. Compression preserves extrema only after the packet reduction just proved. Thus a noncommon normal crossing cannot occur in a distance-one ordinary class pair.
