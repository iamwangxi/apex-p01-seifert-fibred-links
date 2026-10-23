# Seifert 纤维链环外部的循环距离复形可缩性

对 $`S^3`$ 中每个非空、定向、非分裂且外部为 Seifert 纤维空间的链环，约化不可压**循环距离旗复形**均可缩。选定纤维化后，若 $`k=\phi(h)\ne0`$，复形为一点；若 $`k=0`$，顶点对应带标记、未使用锥点孔的平面单位需求匹配，类距离由完整补块的区域势振幅精确给出，匹配流的相容取整提供有限包含的零伦。

本仓库保存 Apex 比赛论文 *Contractibility of the complex of incompressible Seifert surfaces: the knot case of Kakimizu's problem*（Apex Intelligence，2026 年 9 月 11 日，48 页）突破贡献投稿的证明与复算材料。目标 PDF 的 SHA-256 为：

```text
34f17d7d99780d3fd3626d9e5d7b35d6aa76661c404f191b6df341b300c0c06f
```

目标论文在印刷第 2 页给出纽结定理与迫使生成曲面连通的链环推广，并列出尚未处理的一般链环扩展。本证明允许不连通生成曲面，研究循环距离复形；在生成曲面连通的共同范围内，两种复形一致。本证明没有宣称一般不连通情形下原始几何不交复形的全族结论。

## 阅读入口

- [定义与主定理](proof/objects.md)：总链环边界斜率、约化约定和完整开补块。
- [分类与一点情形](proof/classification.md)：填充分类、实心环面、非零纤维求值和平衡定向清单。
- [闭轨形与两条实际边界](proof/two-boundaries.md)：自由积无限阶、闭双倍曲面覆盖、闭 Proposition 25 及基本点情形。
- [普通环境同痕顶点双射](proof/vertex-bijection.md)与[精确类距离](proof/class-distance.md)：纤维商基本群胚、外围检测、相对乘积区和 PS 类最小值，含类距离公式（Theorem 5.3）与交叉阻碍（Lemma 5.4）。
- [固定图匹配流取整](proof/matching-carrier.md)与[可缩性](proof/contractibility.md)：合法输出单形与零坐标面，以及合法纤维（Lemma 7.2）、有限模板与相位碰撞（Lemma 7.3）、支撑粘合（Lemma 7.4）和有限包含/CW 证明（Theorem 7.1）。
- [双锥点例子](proof/double-cone-example.md)：平衡定向的四条正则 $`(2,3)`$ 纤维构成 $`T(8,12)`$，其中一对几何不交顶点的类距离为二。
- [范围与依赖](proof/scope.md)、[参考文献](sources/bibliography.md)、[核验脚本说明](scripts/README.md)。英文证明在本目录内自足。

文献输入保留 PS 期刊版 Definition 2.1、Proposition 3.2 及其明确声明的第 3 节 Sakuma 接口；不调用 PS 第 4–7 节的投影、序和可缩性结果。Schultens Proposition 25 只用于已证明满足条件的闭 good aspherical 轨形，不调用 Remark 35。Hatcher 圆映射方法与经典平面匹配势方法均按实际用途注明归属，不主张裸结论在文献中从未出现。

## 复算与证据边界

用 Python 3 标准库运行：

```text
python3 -B scripts/run_all.py
```

三个程序生成确定性的 JSON。两份独立程序保留各自实现，不导入或运行作者核验程序。有限样本不能替代全族符号证明，也不独立证明三维同痕或 PS 类最小值。任意输入的 PL 规范化与完整参数族过程已有终止性证明，尚无完整软件实现。

底层证明已完成拓扑分类、载体与可缩性两路独立对抗复核，均未发现致命或可修补数学问题；本目录落实了将同痕轨迹明确写成纤维商基本群胚映射的表述意见。另一次全新上下文的投稿包复核检查了证明覆盖、来源对齐、引用与可复现性；该复核没有重复两路数学复核。材料没有经过人类专家认证，也没有声称 Lean 形式化验证。

## AI 声明

GPT-6.1 Sol, in OpenAI Codex under human direction, developed the proof, ran the computations where applicable, and drafted this text; separate GPT-6.1 Sol sessions in fresh contexts performed adversarial reviews. Claude planned the work, checked key steps against the sources, and reviewed and edited the final text. GPT-6 Astra, also in OpenAI Codex, advised on research direction and submission scope. No human expert has certified the work.

## 许可与完整性

原创文字与文档采用 CC BY 4.0；`scripts/` 代码采用 MIT License，全文见 [LICENSE](LICENSE)。外部论文保留各自权利，本目录不捆绑其全文或 PDF。[MANIFEST.sha256](MANIFEST.sha256) 列出其余全部文件的哈希。

[English overview](README.md)
