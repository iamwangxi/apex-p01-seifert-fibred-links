# 24. What nonempty trace requires on the horizontal side

Choose the sign of the periodic fibre flow so that the horizontal pieces have positive transverse orientation. Every horizontal piece has regular-fibre degree $`|k_Q|`$, belongs to the fixed primitive class $`\Phi|_Q`$ and has $`q`$ boundary circles on $`T`$.

**Lemma 24.1 (ordered horizontal pieces).** A disjoint family of such connected horizontal pieces has, on $`T`$, a cyclic word consisting of $`q`$ repetitions of one cyclic ordering of the surface labels. Conversely any disjoint straight trace family of that form can be filled by simultaneously disjoint horizontal pieces in the required relative classes.

**Proof of necessity.** Cut $`Q`$ along one member $`H_0`$. By the horizontal bundle complement, this is $`H_0\times I`$ with interval direction the positive periodic flow. A different connected horizontal member projects along those intervals locally diffeomorphically and properly to $`H_0`$, including at its boundary; hence it is a finite covering of $`H_0`$. If its degree were $`d`$, a regular circle fibre of $`Q`$ would meet it $`d|k_Q|`$ times. Its actual degree is $`|k_Q|`$, so $`d=1`$. It is therefore the graph of a function $`v:H_0\to(0,1)`$.

For a disjoint family the graph functions have one strict order throughout the connected $`H_0`$. On each of its $`q`$ JSJ boundary circles the same order holds. Reading across the $`q`$ successive $`H_0`$ traces on $`T`$ yields precisely $`q`$ repetitions of that order, with $`H_0`$ closing each cycle. This uses geometric degree, with no cancelling intersections.

**Proof of sufficiency.** Choose one trace family as $`H_0\cap T`$ and a horizontal mate $`H_0`$ by Lemma 15.1. The prescribed traces of the other labels become ordered boundary graph values

```math
0<a_{1j}<\cdots<a_{sj}<1
```

on every JSJ boundary component $`C_j\subset\partial H_0`$, with the same label order for every $`j`$. Choose constants $`0<c_1<\cdots<c_s<1`$. In disjoint collars of the $`C_j`$, using a common cutoff $`0\le\chi\le1`$, set

```math
v_i=(1-\chi)c_i+\chi a_{ij},\qquad
v_i=c_i\text{ off the JSJ collars}.
```

If boundary graph values vary along a collar circle, use the same formula pointwise. Strict inequalities remain strict under the common convex interpolation. The graphs $`t=v_i(x)`$ in $`H_0\times(0,1)`$ are thus simultaneously disjoint connected horizontal pieces, with the prescribed JSJ boundary and free actual boundary. They represent the correct primitive class. Lemma 15.1 identifies each with the required mate; its twist quotient is the ordinary global vertex quotient. No matching between two independently labelled sets of sheets remains to be chosen.

This argument also works with a cone on $`Q`$. The cut horizontal complement is still the interval product from Section 21; degree is checked on a regular orbit. The collars are ordinary boundary collars, and the constant extension covers the points lying above the exceptional orbit. ∎

In particular two families must alternate at $`T`$, but pairwise alternation alone needs an argument before being used for several families. The next lemma provides that argument and its precise link to the decoder.
