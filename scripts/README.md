# Exact offline diagnostics for the combined proof

[Overview](../README.md) · [Scope](../proof/scope.md)

Run from the repository root with Python 3 and its standard library:

```text
python3 -B scripts/run_all.py
```

All twelve child programs print deterministic JSON and write no files. The runner captures each report, normalises JSON key order and compares it byte for byte with the bundled file of the same basename. It exits nonzero on any failed assertion, child failure or differing report. The default run writes nothing. After an authorised package change, `python3 -B scripts/run_all.py --update` refreshes only those twelve reports. No network, third-party package, external working file or current timestamp is required.

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

The seven `independent_*` programs preserve separately developed review implementations and do not import or execute author checkers. Packaging changed only comments, paths, fingerprints and report conventions; redundant author re-execution was removed. The retained mathematical functions and assertions were not replaced by the author's implementations. Fingerprints are relative to this package; timestamps and private source names are absent. New geometric checks were adapted in the same way. The author splice geometric diagnostic and the independent splice geometric review implementation are both included. In the latter, one arbitrary graph-edge label was renamed to avoid a private-code collision; after reversing that label substitution, its calculation functions match the source AST.

Bounded finite diagnostics cannot certify joint three-dimensional normalisation, arbitrary ambient-isotopy detection, the noncompact Sakuma interface, the stated simultaneous simplification input, infinite CW continuity or uniform contractibility. They supplement the numbered proofs and declared literature inputs. The arbitrary-input PL normaliser and complete parameter subdivision remain mathematical specifications rather than complete software. Code is MIT-licensed; see [LICENSE](../LICENSE).
