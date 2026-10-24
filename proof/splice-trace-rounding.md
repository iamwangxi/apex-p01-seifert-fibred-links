# 26. The trace condition is preserved by common rounding

Let $`\mathcal C`$ be a nonempty chain of restricted potentials of matching vertices of $`G`$ satisfying Lemma 25.1(c), with a minimal matching reference fixed. Define

```math
\mathcal D(G,\mathcal C)
=\{M\in\mathcal M(G):n_M|_{\mathcal J_G}\in\mathcal C\}.
```

It is finite. Every pair in this set satisfies the trace condition, so Theorem 25.2 makes **all** its vertices one genuine geometric simplex $`\Delta(G,\mathcal C)`$. This assertion is for the restricted set, not for all of $`\mathcal M(G)`$.

Write the affine region potential of a flow in the reference coordinates as

```math
w=\chi_{M_0}+D_Gu(w),\qquad u(w)(s_0)=0,
```

where explicitly

```math
P_G=\left\{w\in[0,1]^{E(G)}:\quad
\sum_{e\ni a}w_e=1\text{ at every actual }a,\quad
\sum_{e\ni J}w_e=q\right\}.
```

The capacity-one bound follows from the unit actual end of every edge. The existing full-region decoder is

```math
m^\theta=\chi_{M_0}+D_G\lfloor u(w)+\theta\rfloor,
\qquad S_G(w)=\int_0^1[M_\theta]\,d\theta,
\qquad 0\le\theta\lt1.
```

The integral is the finite barycentric sum over positive-length threshold intervals. Put

```math
P_{G,\mathcal C}
=\{w\in P_G:u(w)|_{\mathcal J_G}\in\mathrm{conv}(\mathcal C)\}.
```

**Lemma 26.1 (restricted rounding).** The decoder of Theorem 19.1 sends $`P_{G,\mathcal C}`$ into the cyclic subcomplex on $`\mathcal D(G,\mathcal C)`$. Its edge map identifies that subcomplex with $`P_{G,\mathcal C}`$. Equivalently,

```math
P_{G,\mathcal C}
=\mathrm{conv}\{\chi_M:M\in\mathcal D(G,\mathcal C)\}.
```

**Proof.** Write $`u|_J=\sum_i\lambda_i c_i`$ with the $`c_i`$ nested zero-one vectors of $`\mathcal C`$. Common threshold rounding of this vector can take only those same chain values. Explicitly, a coordinate first turning on at index $`j`$ has value $`\sum_{i\ge j}\lambda_i`$. Between its finitely many thresholds the rounded restricted vector is one of the $`c_i`$; zero weights give intervals of zero length. The root remains zero for $`0\le\theta\lt1`$.

Theorem 19.1 rounds the **whole** region vector with this same $`\theta`$. It gives legal matching indicators and a true global cyclic simplex. The jumps at the incident edges of $`J`$ are determined by the restricted sector values, including the fixed reference indicators. Thus every positive-weight output matching has restricted potential in $`\mathcal C`$. No new reaching-edge pattern is introduced, although its actual-to-actual edges may change.

Exact edge expectation gives the displayed inclusion of every flow into the convex hull of those matching indicators. The reverse inclusion follows from the affine potential equation. Theorem 19.1's exact recovery on true simplices, together with continuity, proves the claimed identification and triangulation. This uses the full-region decoder; rounding the trace sectors independently would not suffice. ∎

In particular, for an input geometric simplex one may take $`\mathcal C`$ to be its own restricted potentials. Every output of its barycentric-flow decoder and every input vertex then belong to $`\Delta(G,\mathcal C)`$. This is the replacement for Section 10's unrestricted all-matching carrier.
