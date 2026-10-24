# Exact offline diagnostics for the combined proof

[Overview](../README.md) · [Scope](../proof/scope.md)

Run from the repository root with Python 3 and its standard library:

```text
python3 -B scripts/run_all.py
```

All thirty-eight child programs print deterministic output and write no files. The runner captures each report, normalises JSON key order (a program whose output is plain text, or text followed by JSON, is stored as its list of output lines) and compares it byte for byte with the bundled file of the same basename. Child processes run with a fixed hash seed. It exits nonzero on any failed assertion, child failure or differing report. The default run writes nothing. After an authorised package change, `python3 -B scripts/run_all.py --update` refreshes only those thirty-eight reports. No network, third-party package, external working file or current timestamp is required.

## Cyclic models

- `exact_checks.py`: bounded free-product infinite-order checks, Jordan/peripheral feature equations, closed-double genera, and exact decoding on a double-cone support and its feasible subgraphs.
- `independent_topology.py`: independently generated braid arcs, an arbitrary-word quotient negative control, separate abelian elimination and double-cover calculations.
- `independent_carrier.py`: exact PL embeddings, connected regions rebuilt from forest-cycle winding, rational potentials, separate whole-complement indices, zero faces, true-simplex recovery and auxiliary-collar phase collisions.
- `empty_trace.py`: the actual balanced eight-component splice, shared-root product ranges, common thresholds, deleted supports and negative controls for independent roots/thresholds.
- `multiport.py`: matrix/covector checks, coherent cyclic boundary arrays, the explicit horizontal filling bounds, demand-two and demand-three planar supports, zero faces and exact simplex recovery.
- `independent_empty_trace.py`: separately reconstructed local models and paired supports, including a nested example with local width two and global width four.
- `independent_multiport.py`: peripheral substitution for actual splices, horizontal monodromy, separate cubical/winding indices, cone orders and the fixed-peripheral determinant-only negative control.

## Geometric comparison

- `geometric_comparison.py`: common-threshold decoding on explicit compatible supports, full-simplex recovery, zero support, deformation identities, and the distance-two midpoint moving across a geometric tetrahedron.
- `independent_geometry.py`: independently specified six- and eight-boundary two-cone examples; exact PL parallel-copy allocation, slopes, face reconstruction and geometric/cyclic comparisons. It does not execute an author's checker.
- `independent_retraction.py`: a separate decoder, a closed-form retraction and convex-fibre interval, and two mother graphs whose extra arcs cross while the common noncyclic face has the same retraction. A Dehn-twisted PL example is initially sampled numerically, rationalised and checked for embedding; subsequent comparisons use exact fractions. The random seed is fixed.
- `splice_geometric_comparison.py`: exhaustive bounded repeated-word versus sector-oscillation comparisons, coherent-port supports, chain-pattern preservation under the full decoder, zero faces, strong-deformation identities and negative controls. It includes a JSJ root sector inside a surrounding cycle, so the spherical outside region cannot incorrectly serve as the trace root.

- `independent_splice_geometry.py`: a fresh independent trace-order implementation, actual splice monodromy, exact region reconstruction, all parallel occurrences, ordered horizontal boundary extension, restricted retraction paths and a horizontal-side low-cable negative control with demand three and six supported vertices. It never imports or executes an author checker.

## Graph-manifold diagnostics

- `graph_manifold.py`: the author's packet-prefix, reduced-ribbon, integral-potential, relative-height, common-root, zero-face, true-simplex and horizontal-collar arithmetic tests.
- `independent_graph_slicing.py`: independent preferred-longitude splice equations, the all-zero branch, retained-cone and empty-interface examples, a bounded free-group tree model, and exact open-sector index bounds.
- `independent_graph_carrier.py`: independent bipartite-tree integer quotients, a strip with a free relative-height direction, a two-cone geometric tetrahedron, direct band-level rereading and exact strong-deformation identities.
- `independent_graph_pl.py`: independently constructs PL regular layers, deletes actual circle components, rereads the surviving arc classes and potentials, and checks bounded collision continuity. Its explicit witness shows that retaining the pre-deletion potential can be wrong.

These four programs preserve their source calculations. Their original text reports are captured as deterministic JSON output arrays; packaging removes private comments/docstrings and translates report labels. The three independent implementations do not import or execute the author's checker. A normalised AST comparison records that calculation code is retained, with only docstrings, print labels and the output envelope adjusted.

The ten `independent_*` programs preserve separately developed review implementations and do not import or execute author checkers. Packaging changed only comments, paths, fingerprints and report conventions; redundant author re-execution was removed. The retained mathematical functions and assertions were not replaced by the author's implementations. Fingerprints are relative to this package; timestamps and private source names are absent. New geometric checks were adapted in the same way. The author splice geometric diagnostic and the independent splice geometric review implementation are both included. In the latter, one arbitrary graph-edge label was renamed to avoid a private-code collision; after reversing that label substitution, its calculation functions match the source AST.


## Parts 6–13 diagnostics

Programs named `partN_checks.py` and the other `partN_*` programs without `independent` in their names were written with the corresponding part; programs named `partN_independent*.py` were written by the fresh-context reviewers and do not import or execute the author programs. Part 6 has no program.

- `part7_checks.py`: the six-block splice equations and genuine fibres, the boundary-free four-port support decoder, single-cable arithmetic and cable genera, the square-knot construction for $`r\le256`$, the unanchored control and the component-wall comparison on an actual geometric tetrahedron.
- `part7_independent_ab.py`: independent anchored-splice, cable and square-knot checks for Theorems A–C.
- `part7_independent_wall_phase.py` and `part7_independent_potential.py`: independent component-wall phase, boundary-subset homology and common-potential checks for Theorem D.
- `part8_checks.py`: matching rigidity, parents and distances, common packets, torus-sum and recursive modes, nonunit terminal words, the arithmetic tree, leaf-loop free products, one-boundary caps and the four-parallel control.
- `part8_independent_square.py`, `part8_independent_extension.py`, `part8_independent_pl.py`: two-reflection rigidity, sign defects, Farey parents against graph deletion, the determinant metric and $`C_2*C_3`$ normal forms; slopes, Euler numbers, orientations and gap products of the recursive family; PL level averaging and collision continuity for capped-fibre families.
- `part9_checks.py`, `part9_closure.py`, `part9_gap_orbits.py`: reflection offsets, signed packets, the explicit distance family and the failed raw operations; one-sided closure (monotone enabling, confluence, same-side bad returns, strict decrease); gap-orbit parameters for connected sums.
- `part9_independent.py`: the $`S_q`$ family, the genus-seven example, planar closures, gap orbits, coloured orders, retained-event and prism-slab models, and the filtered comparison.
- `part10_checks.py` and `part10_independent.py`: cap grammar, composing-cap framing lists, recursive certificates, balanced multi-component tests, the nonunit support simplex test, auxiliary trees, Seifert support matrices, empty-interface products, the six-component star and the two-axis lemma; independent degree-$`n`$ port supports, word criteria and contraction checks.
- `part11_star.py`, `part11_certificate.py`, `part11_independent.py`: signed diagrams, order/determinant comparison for $`r,s\le6`$, parent depth against prefix oscillation and truncation homology (the enlarged comparison for $`r,s\le8`$ quoted in Part 11 is the function `order_crosscheck(8,1)` of `part11_star.py`, run separately after importing the file without its main routine); central-cluster certificates, component graphs, pillowcase coordinates and multiport orders; an independent signed catalogue, chord planarity, BFS distances, truncation homology and mixed-sign certificates.
- `part12_checks.py`, `part12_common_packet.py`, `part12_free_returns.py`, `part12_independent.py`: pants degree, peripheral equations, framed and weighted modes, recursive constructions and signed framings; common-packet closures, including a sample of four-hole patterns with the fixed seed 60662026; the Proposition M witness and two-feature Euler cases; an independent reconstruction of all of these and of the trajectory prisms.
- `part13_hopf12.py`: the exact rational face certificate for the twelve-fibre two-interval: its fourteen faces, the four common matchings, their path adjacency and the attained heights.

For packaging, documentation strings and comments were removed through the Python abstract syntax tree, self-checks that hashed private working files and the writing of report files were removed, wall-clock timings were dropped, and a few report labels were renamed. The resulting programs were run and their outputs compared with those of the unmodified calculations; apart from the renamed labels and the removed hashes and timings, they agree.

Bounded finite diagnostics cannot certify joint three-dimensional normalisation, arbitrary ambient-isotopy detection, the noncompact Sakuma interface, the stated simultaneous simplification input, infinite CW continuity or uniform contractibility. They supplement the numbered proofs and declared literature inputs. The arbitrary-input PL normaliser and complete parameter subdivision remain mathematical specifications rather than complete software. Code is MIT-licensed; see [LICENSE](../LICENSE).
