# 链环的不可压生成曲面复形：一般比较定理与大类图流形链环的可缩性

本仓库把比赛论文的主定理从纽结推广到生成曲面**可以不连通**的链环。比较同一顶点集上的两个复形：Kakimizu 原始的**几何不交复形** $`IS(L)=Y(L)`$（单形是可同时取不交代表的曲面族）与**循环距离旗复形** $`X(L)`$。顶点是全部约化、逐分量不可压的生成曲面（任意亏格），按普通环境同痕分类。

**定理 1（一般比较；[第 7 部分](proof/part7.md) Theorem D）。** 对 $`S^3`$ 中任意非空、定向、非分裂链环 $`L`$，顶点恒等给出 $`X(L)\subseteq Y(L)`$，且 $`|X(L)|`$ 是 $`|Y(L)|`$ 的强形变收缩核。因此 $`X(L)`$ 可缩当且仅当 $`IS(L)`$ 可缩。

**定理 2（可缩性）。** 对外部为图流形、属于下列任一类的 $`S^3`$ 中非空定向非分裂链环，$`X(L)`$ 与 $`Y(L)`$ 均可缩。

1. **Seifert 纤维外部**（Theorems 1.2、11.2）。
2. **每个 Seifert JSJ 块都触及链环**（Theorems 1.3、29.1），以及 Theorem 29.2 的横截叶块星形。
3. **锚定横截簇**（[第 7 部分](proof/part7.md) Theorem A）：生成类在每个 Seifert 块上非零，且纤维评价非零的块组成的森林的每个连通分支都含实际链环边界环面；允许不含链环边界的块。
4. **递归图结的平行簇**（[第 12 部分](proof/part12.md) Theorems A、G）：$`K`$ 由非平凡环面结经有限次连通和与 cable 得到；把 $`K`$ 换成任意正数条平行，框架为任意整数，取向任意。环面结连通和的零框架情形（含平方结平衡四平行）是 [第 9 部分](proof/part9.md) Theorem 1.9。两条反向零框架平行：迭代 cable 环面结时 $`X=Y`$ 是一条边（[第 6 部分](proof/part6.md)、第 7 部分 Theorem B）；递归图结时是有根树，平方结时直径无界（[第 8 部分](proof/part8.md)）。
5. **刚性帽与 Seifert 支撑**（[第 10 部分](proof/part10.md)）：带纵向刚性无边界结外部的锚定型核心，对环面结连通和给出精确判据，并给出递归斜率证书（Theorems 1.1、1.3 与 Proposition 1.2）；Seifert 纤维支撑的平衡零框架平行替换（Theorem 11.2、Corollaries 11.3–11.5）。
6. **共振 Hopf 星形**（[第 11 部分](proof/part11.md)）：$`n\ge3`$ 条正则 Hopf 纤维各换成一正一负、框架为 $`-(n-1)`$ 的平行。中央块无链环边界且生成类在其上为零，第 2、3 类不适用；$`X=Y`$ 是单纯树。有限证书可接纳更多中央簇。
7. **带权支撑与共同分离片序**（[第 12 部分](proof/part12.md) Theorems I、J、K，Corollaries K1、L、L1），以及 Theorem F 的合成类（对边界纤维装饰、单位纤维图案替换与空接口乘积封闭）。

**附注（[第 13 部分](proof/part13.md)）。** 比赛论文的纽结证明依赖一个组合交换判据（其 §2 Theorem B）。对链环，该判据在 $`Y`$ 上失效：十二条平衡正则 Hopf 纤维以及平衡六分量环面链环 $`T(12,18)`$ 中，有一对距离为二的顶点，其全部公共邻居恰成四点路径，无锥点，任何复杂度都无法补救；两个复形本身仍可缩。本仓库的证明是拓扑的，不使用论文的解析工具或交换定理。

目标是 Apex Intelligence 比赛版 *Contractibility of the complex of incompressible Seifert surfaces: the knot case of Kakimizu's problem*（2026-09-11，48 页），[公开 PDF](https://math.apexin.net/papers/seifert-surfaces.pdf)，SHA-256：

```text
34f17d7d99780d3fd3626d9e5d7b35d6aa76661c404f191b6df341b300c0c06f
```

论文 Theorems A、D（印刷第 2 页）覆盖纽结与 linking-indecomposable 链环，后者的生成曲面必连通；其第 6.3 节指出一般链环的障碍在于顶点的定义。定理 2 中的大多数链环（例如两两链接数为零的平行簇）是 linking-decomposable 的，有不连通的不可压生成曲面。本证明保留 Definition 4.1（印刷第 8 页）的同时几何不交单形，链环曲面约定依 Kakimizu 1992 印刷第 225 页；不连通链环两种复形的差异见 PS 期刊版印刷第 1490、1493 页。

## 阅读入口

[第 1 节](proof/objects.md) 给出共同的顶点约定、完整开补域与 Theorem 1.3。第 1–5 部分按第 2–40 节及附录 A 编号；第 6–13 部分各自局部编号，互相引用写作「Part n, Theorem x」。

1. **Seifert 循环证明，第 2–8 节：**[分类](proof/classification.md)、[闭轨形与两边界](proof/two-boundaries.md)、[普通同痕顶点](proof/vertex-bijection.md)、[精确类距离](proof/class-distance.md)、[匹配流取整](proof/matching-carrier.md)、[可缩性](proof/contractibility.md)、[双锥点例](proof/double-cone-example.md)。
2. **Seifert 几何比较，第 10–11 节：**[联合竖直化与同时复制](proof/geometric-realisation.md)、[强形变收缩](proof/geometric-retraction.md)。
3. **双块 splice，第 12–22 节：**[假设](proof/splice-objects.md)、[本质切片](proof/splice-minimal-cuts.md)、[水平片唯一性](proof/splice-horizontal-pieces.md)、[普通顶点](proof/splice-vertices.md)、[局部](proof/splice-local-distance.md)与[全局距离](proof/splice-global-distance.md)、[解码](proof/splice-matching-carrier.md)、[可缩性](proof/splice-contractibility.md)、[单锥点](proof/splice-one-cone.md)、[实际链环例](proof/splice-examples.md)、[附录 A](proof/splice-planar-blocks.md)。
4. **双块几何比较，第 23–28 节：**[同时最小切割](proof/splice-geometric-normalisation.md)、[水平片次序](proof/splice-horizontal-order.md)、[迹判据](proof/splice-trace-criterion.md)、[受限取整](proof/splice-trace-rounding.md)、[强形变收缩](proof/splice-geometric-retraction.md)、[无限制载体的反例](proof/splice-geometric-examples.md)。
5. **每块触及链环的图流形，第 29–40 节：**[定理与导览](proof/graph-theorems.md)、[本质切片](proof/graph-structure.md)、[普通环带](proof/graph-ordinary-annuli.md)、[多端口相位](proof/graph-horizontal-phases.md)、[平行束减幅](proof/graph-packet-comparison.md)、[横截填充](proof/graph-horizontal-filling.md)、[全局类最小](proof/graph-class-distance.md)、[势多面体](proof/graph-potential-carrier.md)、[几何回缩](proof/graph-geometric-retraction.md)、[有限高度收缩](proof/graph-contractibility.md)、[六分量树](proof/graph-six-component-example.md)、[整数直线例](proof/graph-relative-height-example.md)。
6. **[第 6 部分](proof/part6.md)：** 环面结的两条反向零框架平行；$`X`$ 是一条边，含不连通、非范数极小的顶点。
7. **[第 7 部分](proof/part7.md)**（两页）：锚定簇（Theorem A）、迭代 cable 双平行（Theorem B）、各亏格相消族（Proposition C）与一般比较（Theorem D，§9）。
8. **[第 8 部分](proof/part8.md)**（三页）：平方结相消树与递归图结双平行。
9. **[第 9 部分](proof/part9.md)**（四页）：环面结连通和的全部零框架平行簇。
10. **[第 10 部分](proof/part10.md)**（三页）：刚性帽、斜率包络与 Seifert 支撑平行。
11. **[第 11 部分](proof/part11.md)**（两页）：共振 Hopf 星形。
12. **[第 12 部分](proof/part12.md)**（三页）：任意框架递归平行、共同分离片序、带权支撑与合成类。
13. **[第 13 部分](proof/part13.md)：** 几何复形上交换公理 (N1) 的失效。

另有[范围与依赖](proof/scope.md)、[文献版本及印刷页码](sources/bibliography.md)、[诊断说明](scripts/README.md)。

## 机制与边界

Seifert 外部的普通顶点是平面匹配系统，完整块距离是区域势的振幅，同阈值取整译码全部匹配流。每块都触及链环时，用平行束前缀减幅、继承的端口实数提升与加权墙相位得到类最小与几何回缩。定理 1 的一般比较在同一个循环覆盖中平均整分量墙的 Thom 带映射；泛层是整张平行分量的并，不需要任何压缩选择。

超出这些范围后，无链环边界的块带有任意亏格的相消曲面（第 7 部分 Proposition C），逐点下降不足以收缩复形。第 8–12 部分改用对整个有限族都标准的结构代替全局压缩选择：唯一环带父顶点与共同平行片序（第 8、9 部分），有限同侧腔室闭包加棱柱同伦（第 9 部分），帽的纵向刚性（第 10 部分），辅助四孔球中的重复轴屏障与唯一 Farey 父顶点（第 11 部分），多端口可见的分离片序的单一全局腔室次序（第 12 部分）。

**并未覆盖全部非分裂图流形链环。** 第 12 部分 Proposition M 给出一个实际四分量链环，其某个顶点含互不平行的支撑片，共同片序约化失效；非分离的中央纤维簇、只在部分端口可见的片也仍未处理。这些是现有方法的障碍，不是不可缩反例。含双曲块的链环未处理。不主张裸可缩性结论首创，未做穷尽的新颖性检索。

## 复算与复核状态

在仓库根目录运行：

```text
python3 -B scripts/run_all.py
```

运行器执行全部诊断程序，捕获其确定性输出并与存档报告逐字节比对，默认不写文件；加 `--update` 才刷新报告。[诊断说明](scripts/README.md)列出全部程序，包括复核者独立编写的实现。有限计算不替代任意三维同痕、文献输入和无限复形定理。

每一部分都经过至少一路全新上下文对抗复核，均无致命问题；复核要求的修正均已落实：Lemma 31.2 的全零分支；第 7 部分五处澄清（含积区引文与连续性步骤的有限子复形措辞）；第 8 部分两处澄清；第 9 部分 Remark 11.3（其 Theorems 11.1–11.2 的多端口分支在 $`S^3`$ 中为空）；第 10 部分的 Hatcher 引文；第 11 部分端口符号重编码。第 6–13 部分由 Claude 依复核过的稿件编排，并完成最终编辑审阅。复核状态是证据记录，不是数学假设。全部 Markdown 页面已经 GitHub 官方渲染核对。

## AI 声明

GPT-6.1 Sol and GPT-6 Astra, in OpenAI Codex under human direction, developed the proofs and ran the computations; separate GPT-6.1 Sol sessions in fresh contexts performed the adversarial reviews and wrote independent diagnostic implementations. GPT-6 Astra also advised on research direction. Claude planned the work, checked key steps against the sources, assembled the package and edited the final text. No human expert has certified the work.

## 许可与完整性

原创文字、文档、诊断数据与编排采用 CC BY 4.0；`scripts/` 代码采用 MIT，见 [LICENSE](LICENSE)。不捆绑外部论文全文。[MANIFEST.sha256](MANIFEST.sha256) 覆盖其余全部文件。

[English overview](README.md)
