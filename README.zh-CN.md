# 每个 JSJ 块均触及链环的图流形链环：不可压生成曲面复形可缩

对 $`S^3`$ 中非空、定向、非分裂，外部为图流形且**每个 Seifert JSJ 块至少有一个实际链环边界环面**的链环，原始几何不交复形 $`IS(L)=Y(L)`$ 可缩。允许任意多块、保留锥点和不连通生成曲面；单形按整族曲面的同时不交定义。循环距离旗复形 $`X(L)`$ 是其单纯子复形和**强形变收缩核**。一般范围不另行断言 $`Y`$ 为旗复形。

另一个已证延伸允许 Seifert 星形分解的中央块没有实际边界，只要所有叶块都有实际边界且纤维评价非零。原 Seifert 和双块 splice 证明保留为基础与特例；抽象双块矩阵叙述中的 $`S^3`$ 外部假设仍独立于矩阵条件。

目标是 Apex Intelligence 的比赛版 *Contractibility of the complex of incompressible Seifert surfaces: the knot case of Kakimizu's problem*（2026-09-11，48 页），[公开 PDF](https://math.apexin.net/papers/seifert-surfaces.pdf)，SHA-256：

```text
34f17d7d99780d3fd3626d9e5d7b35d6aa76661c404f191b6df341b300c0c06f
```

Theorems A、D 位于印刷第 2 页，覆盖纽结和 linking-indecomposable 链环；同页把一般链环及 Lemma 4.9 的共享分量障碍列为未处理扩展。本证明保留 Definition 4.1（印刷第 8 页）的同时几何不交单形，链环曲面约定依 Kakimizu 1992 印刷第 225 页。比赛第 8 页只说明纽结的两种邻接约定一致；不连通链环的差异归于 PS 期刊版印刷第 1490、1493 页。

## 阅读入口

- [共同对象与总定理 1.3](proof/objects.md)。
- Seifert 循环证明：第 2–8 节，[分类](proof/classification.md)、[闭轨形与两边界](proof/two-boundaries.md)、[普通同痕顶点](proof/vertex-bijection.md)、[精确类距离](proof/class-distance.md)、[匹配流取整](proof/matching-carrier.md)、[可缩性](proof/contractibility.md)、[双锥点距离二例](proof/double-cone-example.md)。
- Seifert 几何比较：第 10–11 节，[有限系统联合竖直化与同时复制](proof/geometric-realisation.md)、[强形变收缩与 CW 连续性](proof/geometric-retraction.md)。
- 双块循环证明：第 12–22 节，[独立假设](proof/splice-objects.md)、[全属最小切片](proof/splice-minimal-cuts.md)、[水平片唯一性](proof/splice-horizontal-pieces.md)、[普通顶点与扭转商](proof/splice-vertices.md)、[局部](proof/splice-local-distance.md)与[全局距离](proof/splice-global-distance.md)、[解码](proof/splice-matching-carrier.md)、[可缩性](proof/splice-contractibility.md)、[单锥点](proof/splice-one-cone.md)、[实际链环例子](proof/splice-examples.md)；[附录 A](proof/splice-planar-blocks.md)完整证明块级输入。
- 双块几何比较：第 23–28 节，[同时最小切割](proof/splice-geometric-normalisation.md)、[水平片的统一次序](proof/splice-horizontal-order.md)、[迹判据](proof/splice-trace-criterion.md)、[受限取整](proof/splice-trace-rounding.md)、[强形变收缩](proof/splice-geometric-retraction.md)、[无限制载体的反例](proof/splice-geometric-examples.md)。
- 任意多块证明：第 29–40 节，[定理与证明导览](proof/graph-theorems.md)、[高效切片](proof/graph-structure.md)、[普通环带与全零比较](proof/graph-ordinary-annuli.md)、[多端口相位与整数商](proof/graph-horizontal-phases.md)、[平行束减幅](proof/graph-packet-comparison.md)、[横截填充](proof/graph-horizontal-filling.md)、[全局类最小](proof/graph-class-distance.md)、[带非有界方向的势载体](proof/graph-potential-carrier.md)、[几何回缩](proof/graph-geometric-retraction.md)、[有限高度族与可缩性](proof/graph-contractibility.md)、[六分量无限树](proof/graph-six-component-example.md)、[整数直线例](proof/graph-relative-height-example.md)。
- [范围与依赖](proof/scope.md)、[文献版本及印刷页码](sources/bibliography.md)、[十六项诊断](scripts/README.md)。

原单块与双块证明的核心机制为 $`R=S_G\circ W`$ 和 $`H(x,t)=(1-t)x+tR(x)`$。Seifert 情形的相容图上，全部匹配有同时几何代表。双块非空迹情形还需迹循环词由同一标签次序重复 $`q`$ 次；JSJ 扇区上的限制势组成嵌套二值链，全区域同阈值取整保持这条链，故同伦留在合法的受限几何载体内。不能直接沿用全部匹配构成单形的断言。

多块证明保留零区域之间的 $`s-1`$ 个相对整数高度。相容支撑上的实际载体因此可有非有界方向，不能只保留边流。平行端口束的前缀势减幅与保留实数提升的横截填充，把代表宽度落实为普通类最小。全局加权墙相位同时实现输入与译码输出，给出几何回缩；有限高度族删圆后重新读取实际类和相对高度，再接公共阈值译码。

## 复算、依赖和边界

在仓库根目录运行：

```text
python3 -B scripts/run_all.py
```

十六项标准库程序输出确定性 JSON，默认逐字节比对且不写文件；加 `--update` 才刷新报告。十份独立复核实现保留各自计算函数。有限计算不替代任意三维同痕、文献输入和无限复形定理；通用 PL 规范化与完整参数族程序未全部实现。

保留 PS Definition 2.1、Proposition 3.2 及其第 3 节所述 Sakuma 非紧接口；双块距离另用 PS Lemma 3.5 和 Banks Proposition 4.2。不调用 PS 第 4–7 节的投影、序、拆解或可缩性结果，不对其作超出本证明的评价。Schultens Proposition 25 只用于满足条件的闭 good aspherical 轨形，不用 Remark 35。Hatcher 圆映射与经典匹配势方法按实际用途注明来源。

Seifert 循环证明和几何比较各有两路独立对抗复核，均无致命或需补证问题；双块循环证明有两轮复核及投稿包修订。Seifert 几何比较另有独立再推导。双块几何比较的全新上下文复核亦已完成：致命 0、需补证 0、表述 1。已将低 cable 一点结论明确限定于零侧；水平侧低 cable 继续按迹序论证处理。本次图流形扩展已由 Claude 完成最终编辑审阅。图流形部分有切片／类距离与载体／回缩两路独立复核，均无致命问题；切片侧要求的全零比较补法和加权交点措辞已落实于第 31、33 节。全部 Markdown 页面已经 GitHub 官方渲染核对。

含无实际边界块且不属于横截叶块星形延伸的图流形未处理；含双曲块的一般链环亦未处理。非平凡环面结的反向零框架两平行已给出受限类可除度为零、某顶点最小伴随环面迹却为二的情形，故双块切片定理不能直接沿 JSJ 树归纳。不主张裸可缩性结论首创，不声称经过人类专家认证或 Lean 形式化。

## AI 声明

GPT-6.1 Sol, in OpenAI Codex under human direction, developed the proofs, ran the computations, and drafted this text; separate GPT-6.1 Sol sessions in fresh contexts performed adversarial reviews, and an independent GPT-6 Astra session re-derived the geometric-complex comparison. GPT-6 Astra also advised on research direction and submission scope. Claude planned the work, checked key steps against the sources, and reviewed and edited the final text. No human expert has certified the work.

## 许可与完整性

原创文字、文档、诊断数据与编排采用 CC BY 4.0；`scripts/` 代码采用 MIT，见 [LICENSE](LICENSE)。不捆绑外部论文全文。[MANIFEST.sha256](MANIFEST.sha256)覆盖其余全部文件。

[English overview](README.md)
