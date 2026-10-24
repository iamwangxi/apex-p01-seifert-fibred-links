# 25. The finite trace criterion

Let $`G`$ be a finite noncrossing zero-side graph of distinct proper classes, with demand one at every actual circle, coherent demand $`q`$ at $`J`$, and no $`J`$-return edge. Each matching uses any edge at most once. Cap boundary circles only for the spherical circulation calculation, retaining all actual labels and unused cone marks.

Direct edges from negative to positive and set $`(D_Gv)_e=v_{\ell(e)}-v_{r(e)}`$ for the connected spherical regions. Repeated boundary walks are not assigned separate values.

Let $`\mathcal J_G`$ be the cyclic list of sectors between the incident edge bundles at $`J`$. A connected complementary region may occur several times in this list; it still has only one potential value. Choose one sector $`s_0`$ as root and a reference matching $`M_0`$. For any matching $`M`$ define its integral region potential by

```math
\chi_M-\chi_{M_0}=D_G n_M,\qquad n_M(s_0)=0.
```

Restrict $`n_M`$ to $`\mathcal J_G`$. Choose the direction around $`J`$ so its increments are the selected-edge counts of $`M`$ minus those of $`M_0`$. This is the direction dictated by the common port sign. In particular there is no factor $`q`$ and no independent shift on the $`q`$ sectors. Define

```math
\mathrm{osc}_J(v)=\max_{s\in\mathcal J_G}v_s
-\min_{s\in\mathcal J_G}v_s.
```

The root must be a sector at $`J`$ for the zero-one normalisation below. A spherical outside region need not meet $`J`$, for example when the reaching graph is nested inside another cycle. Theorem 19.1's decoder is root-independent, so moving its root to $`s_0`$ is permitted and uses only one common additive shift.

**Lemma 25.1 (trace criterion).** For a finite matching collection $`\mathcal B`$ the following conditions are equivalent:

(a) Parallel copies of its zero-side edges can be allocated so that its $`J`$ trace word is $`q`$ repetitions of one cyclic order of the matching labels.

(b) For every pair $`A,B\in\mathcal B`$,

```math
\mathrm{osc}_J(n_A-n_B)\le1.
```

(c) After choosing a member with minimal restricted potential as reference, the restricted potentials form a coordinatewise nested chain of zero-one vectors.

Coinciding restricted potentials are permitted, even for different global vertices.

**Proof.** For (a) to (b), read two labels in the repeated word, starting in $`s_0`$. Their cumulative count difference takes either just zero, zero and one, or zero and minus one. At the sectors between bundles this difference is exactly $`n_A-n_B`$. Parallel occurrences inside one bundle do not alter its values in those sectors.

For (b) to (c), all root values are zero and all potentials are integral. A difference of oscillation at most one containing zero is wholly in $`\{0,1\}`$ or wholly in $`\{-1,0\}`$. The finite restricted vectors are therefore totally ordered coordinatewise. Subtract a minimal one. Every resulting vector is zero-one and the vectors are nested. Changing the matching reference subtracts the same integral region potential, so this is precisely the permitted change of reference.

For (c) to (a), order the labels by this chain, breaking identical-vector ties once and for all. At each sector the labels whose cumulative count is one ahead of the reference are a suffix of the chain. As one passes a single edge bundle, every label contributes zero or one occurrence. If the reference does not use that edge, the suffix can only grow and the newly added consecutive labels occur there. If the reference does use it, the suffix can only shrink; the labels that occur are the complementary cyclic interval, including the reference. Thus the occurrences at that bundle can be put in the descending cyclic chain order, continuing the word from the preceding bundle. After the full turn every label has occurred exactly $`q`$ times and the cumulative differences return to zero. The word is exactly $`q`$ copies of one cyclic order.

Use those orders for the parallel copies in the rectangles around the $`J`$-incident edges. The other end is actual and its boundary curves are free, so it imposes no further order constraint. For actual-to-actual edges allocate arbitrary distinct parallel copies. This implements the word by disjoint zero-side annuli, without identifying shared components. Tied patterns have the same incident edges and can use the same fixed tie-breaking order at every occurrence. ∎

**Theorem 25.2 (geometric simplex criterion).** In the mixed branch, distinct global diagram vertices form a simplex of $`Y`$ exactly when their component proper classes have a common noncrossing graph $`G`$ and satisfy Lemma 25.1. In particular $`Y`$ is flag and $`X\subseteq Y`$.

**Proof.** Necessity: Lemmas 23.1–23.2 give the simultaneous block forms and common $`G`$. Lemma 24.1 gives the repeated trace word, and Lemma 25.1 gives the potential condition. Sufficiency: Lemma 25.1 allocates disjoint copies of every needed zero-side edge, with the repeated word on $`J`$. Lemma 24.1 fills the opposite side by disjoint horizontal mates. Glue across $`T`$. Theorem 16.2 and its incompressible assembly argument identify these as the required ordinary global vertices. This is an explicit simultaneous construction of whole surfaces.

For flagness, pairwise geometric edges give pairwise compatible component classes, so canonical ordinary representatives yield a common graph. They also give all pairwise restricted oscillation bounds. Lemma 25.1 then gives the whole repeated word and the sufficiency above gives the simplex. For a simplex of $`X`$, Section 19's crossing obstruction gives the common graph and its full pair potentials have oscillation at most one. Restriction to the $`J`$ sectors cannot increase oscillation. The same criterion puts that simplex in $`Y`$. ∎
