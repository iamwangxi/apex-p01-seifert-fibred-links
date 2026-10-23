# Contractibility of the cyclic complex for Seifert-fibred link exteriors via matching flows

The reduced incompressible **cyclic-distance flag complex** of every nonempty oriented non-split link in $`S^3`$ with Seifert-fibred exterior is contractible. For a chosen fibering with $`\phi(h)\ne0`$ it is a point. When $`\phi(h)=0`$, the proof gives an explicit unit-demand matching model on a planar base with marked unused cone holes, an exact class-distance formula, and compatible flow decoding for finite inclusion nullhomotopies.

This repository contains the proof and reproducible diagnostics for a **supplement / breakthrough contribution** to the Apex competition paper *Contractibility of the complex of incompressible Seifert surfaces: the knot case of Kakimizu's problem*, Apex Intelligence, 11 September 2026, 48 pages. Target PDF SHA-256:

```text
34f17d7d99780d3fd3626d9e5d7b35d6aa76661c404f191b6df341b300c0c06f
```

That paper proves the knot case and a link case under a connectedness-forcing condition; p. 2 identifies the untreated general-link extension. This manuscript permits disconnected spanning surfaces and uses complete-block cyclic distance. It does not claim contractibility of the original geometric-disjointness complex for every Seifert link. On the common connected-surface range the complexes agree.

## Reading the proof

1. [Objects and main theorem](proof/objects.md): prescribed total-link slopes, reduced surfaces and one whole complementary block.
2. [Classification and the point branch](proof/classification.md): the full filling classification, solid torus and nonzero fibre evaluation, and the exhaustive balanced list.
3. [Closed orbifolds and two boundaries](proof/two-boundaries.md): free-product infinite order, a genuine surface cover of the double, closed Proposition 25 and elementary point cases.
4. [Ordinary ambient-isotopy vertex bijection](proof/vertex-bijection.md): simultaneous verticalisation, the fibre quotient of the fundamental groupoid, joint arcs and effective codes.
5. [Exact class distance](proof/class-distance.md): cone/peripheral detection, all relative product-region cases, PS Proposition 3.2, connected-region potentials (Theorem 5.3) and the crossing obstruction (Lemma 5.4).
6. [Fixed matching-polytopes](proof/matching-carrier.md): spherical circulations, common floor rounding, continuity, zero faces and exact barycentric recovery.
7. [Contractibility](proof/contractibility.md): legal fibres (Lemma 7.2), finite height templates and phase collisions (Lemma 7.3), support gluing (Lemma 7.4) and the finite-inclusion/CW proof (Theorem 7.1).
8. [Double-cone example](proof/double-cone-example.md): four balanced regular $`(2,3)`$ fibres, an oriented $`T(8,12)`$, with geometrically disjoint vertices at class distance two.
9. [Scope and dependencies](proof/scope.md), [bibliography](sources/bibliography.md), and [exact finite diagnostics](scripts/README.md).

The proof uses PS journal Definition 2.1 and Proposition 3.2, including its declared §3 Sakuma interface. It uses no PS §§4–7 projection, order or contractibility result. Schultens' Proposition 25 is applied only to closed good aspherical orbifolds; Remark 35 is not an input. The fixed-graph and finite-family arguments are fully included here and require no companion manuscript.

## Reproducing the diagnostics

Python 3 and its standard library suffice:

```text
python3 -B scripts/run_all.py
```

The three checkers write deterministic JSON files beside themselves. The two independent checkers retain separate implementations and do not import or execute the author's checker. Their finite tests supplement the written proof; they do not certify the uniform theorem, PS class minimality or arbitrary ambient isotopy. The unrestricted PL preprocessing and parameter-family procedure are specified mathematically, rather than fully implemented.

The underlying proof underwent two separate adversarial reviews, covering topology/classification and carrier/contractibility. Both found no fatal or repairable mathematical issue. The present package incorporates the topology review's request to state the fibre quotient explicitly. A separate fresh-context package review checked proof coverage, source alignment, references and reproducibility; it did not repeat the mathematical reviews. No claim is made that the bare contractibility conclusion is new. Hatcher's circle-map mechanism and classical planar matching heights are credited in the bibliography.

## AI disclosure

GPT-6.1 Sol, in OpenAI Codex under human direction, developed the proof, ran the computations where applicable, and drafted this text; separate GPT-6.1 Sol sessions in fresh contexts performed adversarial reviews. Claude planned the work, checked key steps against the sources, and reviewed and edited the final text. GPT-6 Astra, also in OpenAI Codex, advised on research direction and submission scope. No human expert has certified the work.

## Licence and integrity

Original prose and documentation are licensed under CC BY 4.0. Code in `scripts/` is licensed under the MIT License; see [LICENSE](LICENSE). External publications retain their own rights and are not bundled. [MANIFEST.sha256](MANIFEST.sha256) records every other packaged file.

[中文说明](README.zh-CN.md)
