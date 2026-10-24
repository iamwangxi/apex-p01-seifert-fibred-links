# Part 13. The exchange axioms fail on the geometric complex

[Overview](../README.md) · Part 13, page 1 of 1

The competition paper proves its knot theorem through a combinatorial criterion (its §2, Definition 2.1 and Theorem B). A nonempty connected flag complex is contractible if it carries a well-ordered complexity $`c`$ such that, for every pair $`u,w`$ at edge-path distance two, the set $`I(u,w)=N(u)\cap N(w)`$ of common neighbours has an **apex** — a vertex equal or adjacent to every member of $`I(u,w)`$ — (N1), and some apex $`x`$ has $`c(x)\lt \max\{c(u),c(w)\}`$ (N2). Section 6.3 of the paper attributes the obstacle for general links to the definition of a vertex, since spanning surfaces may be disconnected. This part shows that the obstacle is real for Kakimizu's geometric complex $`Y=IS(L)`$: already for balanced Seifert links, (N1) fails, for **every** choice of complexity, although $`Y`$ is contractible. The contractibility theorems of this repository therefore use different methods.

## 1. Conventions

The vertices are the reduced ordinary spanning classes of [Section 1](objects.md): oriented, componentwise incompressible surfaces, with one boundary on each labelled actual torus and no closed component. Boundary circles slide on their own tori. The cyclic complex $`X`$ has edges of Banks/Sakuma class distance one and is flag. The geometric complex $`Y`$ uses simultaneous disjoint representatives of the entire spanning systems. Part 7, Theorem D gives $`X\subseteq Y`$ and a strong deformation retraction of $`|Y|`$ onto $`|X|`$.

For either graph, put $`I(u,w)=N(u)\cap N(w)`$ when $`d(u,w)=2`$. An apex must be a **vertex of this full interval** adjacent or equal to every vertex of it. A cone in a finite truncation is not enough, and the absence of a cone in a finite truncation is not by itself a counterexample. Similarly, a contractible interval need not be a cone.

## 2. A complete failure of (N1) for geometric disjointness

The obstruction already occurs in a Seifert exterior, without a cancellation companion.

**Theorem 2.1 (a four-vertex path as a full geometric two-interval).** Let $`H_{12}`$ be twelve regular Hopf fibres, with six of each orientation. Its full geometric spanning complex $`Y(H_{12})`$ does not satisfy (N1). Explicit vertices $`u,w`$ have $`d_Y(u,w)=2`$ and

```math
Y[I_Y(u,w)]\cong C_0-C_1-C_2-C_3.
\qquad\text{(2.1)}
```

In particular the full two-interval has no apex. This link is inside the already proved all-actual-boundary Seifert class; its $`X`$ and $`Y`$ are nevertheless contractible. For the displayed endpoints, the cyclic distance is three, so (2.1) is not an (N1) counterexample for $`X`$.

**Construction.** Use the Seifert matching description of Sections 2–8. The base is a sphere with twelve labelled actual holes and no auxiliary holes. On a circle separating two disks $`D_+,D_-`$ put the labels $`1,\ldots,12`$ in cyclic order, with signs

```math
+++---+++---.
```

Drill small holes at those points; the circle then serves only as a drawing seam, not an additional boundary of the base. In $`D_+`$ draw the following noncrossing chord systems:

```math
\begin{aligned}
U={}&\{(1,6),(2,5),(3,4),(7,12),(8,11),(9,10)\},\\ 
W={}&\{(1,12),(2,11),(3,10),(4,9),(5,8),(6,7)\}.
\end{aligned}
\qquad\text{(2.2)}
```

Each pair names the two labelled endpoint holes of a proper arc. Equivalently, $`U`$ consists of the two nested three-arc matchings on $`1,\ldots,6`$ and $`7,\ldots,12`$, while $`W`$ is the nested six-arc matching on all twelve labels. Let $`u,w`$ be their vertical annular inverse images. Every pair in (2.2) joins opposite signs.

Each pair of distinct-end chords crosses at most once. Chords sharing a hole do not cross elsewhere. Thus the displayed pair has no bigon or boundary half-bigon and is in ordinary minimum position. There are twelve transverse crossings. In particular $`u,w`$ are not geometrically adjacent.

**Exhaustion of the interval.** Any incompressible spanning surface for this balanced Hopf link is a six-annulus matching, by the Seifert classification of Section 2. If its ordinary vertex is geometrically compatible with both $`u,w`$, its base arcs can be represented disjoint from the fixed union $`U\cup W`$.

For completeness, simultaneous avoidance here is an elementary arc fact. Start with an arc system disjoint from $`U`$ and remove its intersections with $`W`$ by innermost empty bigons or half-bigons. If a reducing disk meets $`U`$, an outermost $`U`$ segment in that disk gives an empty bigon with $`W`$, or an empty half-bigon when the disk has an actual boundary side. This contradicts the minimum position of $`U,W`$. Thus the reductions can be made while retaining disjointness from $`U`$. The same statement also follows from canonical orthogeodesic representatives of proper arc classes. It is specific to the planar arc model; no analogous unproved assertion about arbitrary three-dimensional spanning systems is used.

Trace the faces of (2.2). The face on the $`D_-`$ side contains all twelve actual corners, in their cyclic order. Among the other thirteen faces, the only ones with two actual corners have the pairs

```math
\{3,4\},\quad\{9,10\},\quad\{1,12\},\quad\{6,7\}.
\qquad\text{(2.3)}
```

Four further faces have the single actual corners $`2,5,8,11`$, and all remaining faces have none. Each face in (2.3) has its direct boundary-ear chord in $`U`$ or $`W`$. A common arc in that face is isotopic across an empty rectangle to that ear, and then across the empty polygon cap to the same boundary ear in $`D_-`$. These rectangles contain no other member of the common matching: their only possible actual endpoints are already used by the moving arc, and closed components are forbidden. The moves can therefore be made on the whole matching. A face with zero or one actual corner cannot contain an arc using two distinct actual holes. It follows that **every common matching class** can be represented entirely in $`D_-`$. There is no missing winding parameter: the face is a disk, and the interior two-corner classes have just been identified with its boundary ears.

Conversely every oriented noncrossing perfect matching in $`D_-`$ gives a common neighbour. The positive-negative perfect matchings of this disk are exactly the following four:

| Vertex | Matching in $`D_-`$ |
|---|---|
| $`C_0`$ | $`(1,6),(2,5),(3,4),(7,12),(8,11),(9,10)`$ |
| $`C_1`$ | $`(1,12),(2,5),(3,4),(6,7),(8,11),(9,10)`$ |
| $`C_2`$ | $`(1,12),(2,11),(3,4),(5,8),(6,7),(9,10)`$ |
| $`C_3`$ | $`(1,12),(2,11),(3,10),(4,9),(5,8),(6,7)`$ |

One can check exhaustion by pairing hole one in turn with each opposite-sign hole. The two boundary intervals it cuts off must each have equally many signs; recurse inside those intervals. This finite Catalan recursion yields precisely the four displayed systems. Notice that $`C_0`$ is drawn in the other disk from $`U`$, and $`C_3`$ in the other disk from $`W`$; they are not identifications with the endpoints.

Consecutive rows have disjoint chord representatives. Nonconsecutive rows intersect essentially: for $`C_0,C_2`$ and $`C_0,C_3`$ the chords $`(1,6)`$ and $`(2,11)`$ have alternating ends, while for $`C_1,C_3`$ the chords $`(2,5)`$ and $`(3,10)`$ do. Each named pair crosses once and has four different endpoint holes, so it has no bigon or half-bigon and cannot be made disjoint on the punctured sphere. Thus the full induced interval is exactly the path (2.1). All four are distinct ordinary vertices, and none equals $`u`$ or $`w`$, since each is disjoint from both nonadjacent endpoints. The middle vertices have degree two in this four-vertex interval and the end vertices degree one; none has the required three neighbours. This proves failure of (N1), for every possible complexity.

**Cyclic check and limits.** Orient every input arc from negative to positive. The integral chamber potential of $`U-W`$, rooted at the outside face, has range three. An exact rational-coordinate ribbon certificate is provided by `scripts/part13_hopf12.py`: it places the twelve vertices on a convex parabola polygon, computes all intersections with rational arithmetic, verifies the fourteen face boundaries, and propagates the unit jumps. The attained heights are $`0,-1,-2,-3`$. The ordinary minimum-position formula of Section 5 therefore gives

```math
\delta(u,w)=3.
```

The same four matching patterns drawn in $`D_+`$ give a cyclic three-edge path: consecutive patterns change only the two annuli on four actual tori, with all other components common; their noncommon difference is one oriented cycle and has binary height. Thus the $`X`$ graph distance is also three. This explicitly distinguishes the geometric counterexample from a cyclic distance-two test. No noncontractibility or nonzero homology follows from (2.1). Indeed the full complexes in this example are contractible by [Theorem 1.2](objects.md) and [Theorem 11.2](geometric-retraction.md) of Sections 1–11.

The finite computation here has a different role from the exploratory searches: the face argument proves that the four listed classes are the **entire** geometric interval. The script checks that finite certificate; it is not a genus or winding cutoff.

**Consequence.** A theorem asserting that $`Y(L)`$ is an exchange complex for every link in Part 7, Theorem A, is false, since $`H_{12}`$ is already in that class. Hence a geometric exchange subclass cannot contain all of Part 7, Theorem A. The displayed $`u,w`$ are three steps apart in $`X`$, so this pair does not test the exchange axioms for $`X`$; that question is not decided here.


**Corollary 2.2 (a six-component Seifert counterexample).** The same failure occurs for six regular $`(2,3)`$ fibres in $`S^3`$, three positively and three negatively oriented: the balanced oriented torus link $`T(12,18)`$. Its geometric complex has a distance-two pair with full interval the path $`P_4`$. The displayed pair again has cyclic distance three. This is a different link from the six-component resonant Hopf star of Part 11.

**Proof.** Make the drawing (2.2) in a regular twelve-gon. The half-turn $`i\mapsto i+6`$ preserves its signs, both input chord systems, and each of the four outside systems $`C_j`$. On the sphere it has two fixed points, the centres of the two drawing disks, neither on an input arc. Quotient the marked picture by this half-turn. There are six actual holes, with cyclic signs $`+++---`$, and two marked fixed points. Retain both as forbidden marks for all proper arc isotopies.

The quotient input systems have three arcs each, with endpoint pairs $`(1,6),(2,5),(3,4)`$ but different ordinary paths. Their union has six crossings and eight faces. The outside face contains all six actual corners and one mark. The only other faces with two actual corners are the ears $`\{1,6\}`$ and $`\{3,4\}`$, whose arcs move to the outside boundary ears as before. The second mark is in a face with no actual corner. Empty bigons or half-bigons in the quotient would lift to empty ones in the original picture; hence the quotient pair is in minimum position.

Every common matching is consequently represented in the outside disk with its one retained mark. Filling that mark temporarily gives a disk with signs $`+++---`$, whose only noncrossing opposite-sign matching is the nested matching $`(1,6),(2,5),(3,4)`$. Its three arcs cut the disk into four regions. The retained mark can lie in any one of these four regions, and these are exactly the four ordinary matching classes in the marked disk. This is a complete classification: within a disk, the unmarked matching has one isotopy class, and retaining one point records only its complementary region.

One can also see their path adjacency directly. Label the nested arcs from outside to inside by $`a_0,a_1,a_2`$. For each arc, use class zero when its disk on the interval containing the inner endpoints excludes the mark, and class one when that disk contains the mark. The four states have bit words $`000,100,110,111`$. Consecutive states differ in one arc and are simultaneously disjoint. If two states differ in at least two successive arcs, the class-zero outer arc cuts off an unmarked disk containing the inner endpoints, whereas the class-one inner arc must leave that disk to put the mark on its specified side. It must cross the outer arc. Thus nonconsecutive states cannot be made disjoint.

The four quotients of $`C_0,\ldots,C_3`$ realise these four distinct classes. If two were isotopic downstairs while avoiding the marks, the identity-starting isotopy would lift upstairs and identify two of the distinct labelled matching classes in Theorem 2.1. Consecutive systems have half-turn-equivariant disjoint representatives, and their quotients are adjacent. A disjoint realisation of nonconsecutive quotients would lift to a disjoint realisation upstairs, contradicting the single-crossing witnesses in Theorem 2.1. Thus the full quotient interval is again $`P_4`$.

Now assign Seifert orders two and three to the two marked points. This step is a marked-base construction, **not** a claim about a branched covering of the eventual three-manifold. The ordinary annulus detector and matching classification of Sections 2–4 retain a cone of any order at least two as a forbidden mark; changing one mark's order to three changes none of these ordinary arc classes or simplices. The resulting marked base is realised by six regular fibres of the $`(2,3)`$ Seifert fibration of $`S^3`$, namely the stated balanced $`T(12,18)`$. It is non-split, and every incompressible spanning vertex is a three-annulus matching.

The input difference potential is invariant under the half-turn, so it descends with the same four attained integer levels $`0,-1,-2,-3`$. The ordinary minimum-position theorem for the marked base gives cyclic distance three. The inside quotients of the four consecutive patterns also give a three-edge cyclic path, changing one annulus at each step and retaining the other two. Thus its $`X`$ graph distance is three as well. No independent or fractional deck constant has been introduced. ∎

The counterexample therefore needs only three annular components per spanning vertex in this explicit Seifert realisation. No assertion that this component count or link is minimal is made. Capping away one of its demand pairs would not automatically preserve the interval: it can create a forbidden closed component and identify formerly different vertices.

### 2.3. Exact face certificate

For the drawing (2.2), let $`x_{i,j}`$ denote the crossing of the $`i`$th chord in the displayed list $`U`$ with the $`j`$th chord in the list $`W`$. The following cyclic face walks, with the potential of $`U-W`$, give a checkable finite certificate for the face inventory and the cyclic range. The outside face is numbered zero. Reversing every orientation reverses all heights and leaves the ranges unchanged.

| Face | Boundary walk | Height |
|---:|---|---:|
| 0 | $`6\; x_{1,5}\; 5\; x_{2,4}\; 4\; 3\; x_{2,3}\; 2\; x_{1,2}\; 1\; 12\; x_{4,2}\; 11\; x_{5,3}\; 10\; 9\; x_{5,4}\; 8\; x_{4,5}\; 7`$ | $`0`$ |
| 1 | $`x_{1,5}\; 6\; 7\; x_{4,5}`$ | $`-1`$ |
| 2 | $`x_{1,5}\; x_{1,4}\; x_{2,4}\; 5`$ | $`-1`$ |
| 3 | $`x_{1,4}\; x_{1,5}\; x_{4,5}\; x_{4,4}`$ | $`-2`$ |
| 4 | $`x_{1,4}\; x_{1,3}\; x_{2,3}\; x_{2,4}`$ | $`-2`$ |
| 5 | $`x_{1,3}\; x_{1,4}\; x_{4,4}\; x_{4,3}`$ | $`-3`$ |
| 6 | $`x_{1,3}\; x_{1,2}\; 2\; x_{2,3}`$ | $`-1`$ |
| 7 | $`x_{1,2}\; x_{1,3}\; x_{4,3}\; x_{4,2}`$ | $`-2`$ |
| 8 | $`1\; x_{1,2}\; x_{4,2}\; 12`$ | $`-1`$ |
| 9 | $`x_{2,4}\; x_{2,3}\; 3\; 4`$ | $`-1`$ |
| 10 | $`x_{4,2}\; x_{4,3}\; x_{5,3}\; 11`$ | $`-1`$ |
| 11 | $`x_{4,3}\; x_{4,4}\; x_{5,4}\; x_{5,3}`$ | $`-2`$ |
| 12 | $`x_{4,4}\; x_{4,5}\; 8\; x_{5,4}`$ | $`-1`$ |
| 13 | $`x_{5,3}\; x_{5,4}\; 9\; 10`$ | $`-1`$ |


### 2.4. Consequences for modified vertex sets

Every vertex of $`Y(H_{12})`$ consists of exactly six annuli, and every vertex in the Seifert example of Corollary 2.2 consists of exactly three. Passing to connected vertices gives the empty complex. Filtering only by component count, genus, Euler characteristic or JSJ trace either leaves the entire example or removes it entirely; those quantities are constant on its full vertex set. Such a filtration cannot repair (N1) while preserving a nonempty homotopy-equivalent model.

The natural cyclic complex $`X(H_{12})`$ is a strong deformation retract of $`Y(H_{12})`$ by Part 7, Theorem D. The pair in Theorem 2.1 is no longer a distance-two pair there. It is a homotopy-equivalent candidate which avoids **this** obstruction; its exchange axioms are not decided here. Nor may “the interval is a cone” be weakened to “the interval is contractible”: the path in (2.1) is contractible, and the proof of the competition paper's Theorem B uses an apex to keep witnesses in descending links.

[Overview](../README.md)
