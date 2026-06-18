# Average Causal Effect Estimation in DAGs with Hidden Variables: Beyond Back-Door and Front-Door Criteria

**讲者**: Young Researchers' Seminar  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2026-02-17  
**主题**: 因果推断  
**视频**: <https://youtu.be/GO1z9bECD2k> · [幻灯片](https://drive.google.com/file/d/1pyNTF31HmxdbiGp_6oS7flqBQbCjWl_O/view?usp=sharing)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

## 相关论文

- [2312.10234](https://arxiv.org/abs/2312.10234) *（尚未精读 — `talks read --id … --read-papers` 可补）*

---

### 一、这场报告在讲哪条工作线

这场报告本质上是在回答**一个有隐藏变量的因果图模型中，最优的（非参数有效、灵活、可自动化）估计方法是什么**——而且是针对一类*特殊但广泛*的、可以**被当前非参数识别算法“判定为可识别的”** 的因果参数。

**背景**：在有隐藏变量（unmeasured confounders）的 DAG 中，标准的 back-door 调整（g-formula）一般失效。现有文献给出了两条互补的路径：
- **识别（identification）路线**：Tian and Pearl (2002)、Shpitser and Pearl (2006) 等给出了在 acyclic directed mixed graphs（ADMGs）上**sound and complete** 的识别算法——对任意给定 ADMG，算法可以在多项式时间内判断某个因果参数（如 ATE）是否被非参数识别，并给出一个识别函数（若存在）。该方向已成熟，商业图模型因果推断软件（如 causaleffect R 包）均基于此。
- **估计（estimation）路线**：在识别函数已知后，如何灵活地给出一致且渐近有效的估计？这方向早先有 Bhattacharya et al. (2020) 针对特定图类的参数化估计；Jung et al. (2024) 和 Fulcher et al. (2020) 提供了一些具体图类（如 front-door）的估计方法。但**缺失**的是一个统一、可处理整个 primal fixability 类图（即 A 满足 `ch_G(A) ∩ dis_G(A) = ∅`）、同时允许使用任意机器学习方法（非参数速率）且保持根号 n 一致性与渐近有效性的估计框架。

**这场报告的位置**：讲者（Anna Guo）及其合作者（Nabi, Benkeser）试图**补上这个缺口**。报告核心工作线可分为两条：（1）对于**primal fixability 类**（“A 是 primal fixable”），给出一个通用的非参数有效估计框架（one-step + TMLE），并推导了充分条件（涉及多个 nuisances 的 L2 速率的乘积条件）以确保渐近线性；（2）对于**primal fixability 类之外**但 ATE 仍可识别的特例（如 “Napkin graph”，亦称“bow graph”），给出特殊处理，并引入一个凸组合加权影响函数来提升效率。两点均以 R 包 **flexCausal** 实现。

⚠ 注意：演讲中引用的文献标题有：
- Guo & Nabi, "Average Causal Effect Estimation in DAGs with Hidden Variables: Beyond Back-Door and Front-Door Criteria", **arXiv 2409.03962**.
- Guo, Benkeser, & Nabi, "Flexible Nonparametric Inference for Causal Effects under the Front-Door Model", **arXiv 2312.10234**.
- Guo, Benkeser, & Nabi, "Causal Inference with the 'Napkin' Graph", **arXiv 2512.19861**（字幕听成 "b2 b0"，实际是 2512.19861；slide 写的是 2512.19861）。

**重要背景引用**（对理解工作线必不可少）：
- Tian & Pearl (2002) "A general identification condition for causal effects" —— 提出 primal fixability 与识别条件。
- Bhattacharya, Nabi, & Shpitser (2020) "Semiparametric inference for causal effects in graphical models with hidden variables" —— 给出了 primal fixability 类下 ATE 的非参数影响函数（EIF）公式。Guo 等人的工作大量建立在该 EIF 上，但关键在于**重参数化** EIF 中涉及的密度比项，以便用灵活的回归方法而非直接密度估计来估计。

### 二、最小内核 / 一个最简例子

#### 2.1 符号、模型与可观测数据

令观测数据为 $O = (X, A, M, Y)$，其中：
- $A \in \{0,1\}$：二值处理变量。
- $Y \in \mathbb{R}$：结果变量。
- $X \in \mathbb{R}^d$：观测到的预处理混杂。
- $M$：一个可能的后处理变量（在前门 / front-door 情形下它落在 $A$ 的 district 中）。
- 存在未观测的混杂 $U$（不进入 $O$）。

图结构（ADMG 表示）：
```
A → M → Y
X → A, X → M, X → Y
A ↔ Y
```
（这里 `A ↔ Y` 的 bidirected edge 表示由隐藏变量引起的相依性。`A` 的 district `dis_G(A) = {A}`（只有 A 自身），children `ch_G(A) = {M}`；因为 `dis_G(A) ∩ ch_G(A) = ∅`，所以 A 是 primal fixable。）

**目标 estimand**：ATE = $\mathbb{E}[Y^{a=1} - Y^{a=0}]$，或更一般地期望潜在结果 $ψ_{a_0} = \mathbb{E}[Y^{a_0}]$, $a_0\in\{0,1\}$。

#### 2.2 识别函数（由幻灯片 [5/20] 的公式）

由 Tian-Pearl 算法可得识别函数：
$$ψ_{a_0}(P) = \iint y \,\mathrm{d}P(y|m, a_0, x) \, \mathrm{d}P(m|a_0, x) \, \mathrm{d}P(a|x) \, \mathrm{d}P(x)$$
（这里隐含了积分子 M、A、X；Y 是结果变量，最后一部分实际上是联合分布分解的一个因子。）

#### 2.3 重参数化：将识别函数写成迭代期望

关键技巧：将上述识别函数重新表达为（slide [7/20]）：

1. 将 $ψ_{a_0}$ 展开为：
   $$ψ_{a_0} = \mathbb{E}[I(A=a_0)Y] + \text{调整项}$$
   其中调整项 = 一个**嵌套的期望结构**：外层在 $X$ 上，中间层在 $(M, a_0, X)$ 上，最内层在 $(L, M, a_0, X)$ 上；在 front-door 模型中没有 $L$（$L$ 为空），因此退化为两个嵌套期望。

2. 具体地，对于这个单 M 的 front-door 模型，定义顺序回归函数：
   - $B_Y(m,x) = \mathbb{E}[Y \mid M=m, A=a_0, X=x]$（即先用观测数据 $Y \sim M,A,X$ 拟合，再在 $A:=a_0$ 下预测）
   - $B_M(x) = \mathbb{E}[B_Y(M,x) \mid A=a_0, X=x]$
   那么调整项 = $\mathbb{E}[B_M(X)]$。

所以 **plug-in estimator** 仅需两个顺序回归。

#### 2.4 为什么这种方法比直接估计密度更容易？

原始识别函数要求估计 $\mathrm{d}P(m|a_0,x)$——一个条件密度。而重参数化后的估计只需要**条件期望回归**（$B_Y$ 和 $B_M$），可以使用任何黑箱回归器（随机森林、神经网络、超学习器）。这是该方法灵活性的核心。

### 三、报告主体：讲者讲了什么

**[0:00 - 0:05]** 会议介绍：两场演讲；第一场 Anna Guo，Emory University，合作者 Razieh Nabi 和 David Benkeser。

**[0:05:21 - 0:06:31]** 设置框架：ATE 定义；没有未观测混杂时 back-door/g-formula 可识别；有未观测混杂则需要用其它方法（敏感性分析、边界、IV）。讲者强调本报告采用**图模型路径**：使用 ADMGs（将未观测变量投影出去），图模型识别算法（Tian-Pearl，Shpitser-Pearl）来判断目标是否可识别。

**[0:06:31 - 0:08:05]** ADMG 与 primal fixability：
- ADMG 的双向边（bidirected edges）表示未混杂，这些边将变量划分到不同**district**（双向边连通分量）。
- A 的 district：`dis_G(A)`，A 的 children：`ch_G(A)`。
- **Primal fixability**：`ch_G(A) ∩ dis_G(A) = ∅`。若成立，则整个 post-intervention 分布 `p(V\A | do(A=a_0))` 可识别。
- 若 primal fixability 不成立，整个分布不可识别，但某些边缘（如 ATE）可能仍然可识别（如 Napkin graph 示例）。

**[0:08:05 - 0:09:35]** 对于 primal fixability 类，识别函数的通用形式（slide [5/20]）：
- 将变量分为预处理 X、A 的 district 内的后处理变量 M、district 外的后处理变量 L。
- 再引入 **markov pillow（mp）**：对每个变量 V_i，mp(V_i) = 所有在 V_i 之前且落在 V_i 的 district 或该 district 的父母集中的变量。
- 通用识别函数是一个多层积分/求和，其中 M 组变量的条件密度中 A 被设为 $a_0$，L 组变量的条件密度中 A 被设为“随机”并在 A 层先验上积分（幻灯片 [5/20] 公式）。

**[0:09:35 - 0:12:03]** 估计目标：计算高效 + 灵活（允许 ML）+ 保持统计优良性质（根号 n 一致、渐近线性）+ 实现为统一 R 包。

**[0:12:03 - 0:13:14]** 重参数化与 plug-in 估计：
- 通过将识别函数拆成“基线项 + 迭代期望项”，将原本需要估计多个条件密度的问题转化为**一系列条件期望回归**。
- 对于 front-door 模型，仅需 2 个回归；对于双中介模型（slide [7/20]），需要 $K$ 个回归（$K$ 为 $A$ 与 $Y$ 之间的变量数）。
- 这些回归可以顺序进行（sequential regressions），依次形成 pseudo-outcomes。

**[0:13:14 - 0:16:45]** 基于影响函数（EIF，efficient influence function）的估计量：
- 单纯的 plug-in 估计量需要所有回归都正确指定才一致，且若用 ML 会有巨大一阶偏差。
- 利用 Bhattacharya et al. (2020) 给出的非参数有效影响函数，但他们的版本中涉及**密度比乘积**，直接用 ML 较难。
- 讲者给出的关键贡献：**重参数化 EIF**，使得密度比项也可用基于回归的方法（通过贝叶斯定理重新表达为倾向得分之比）来估计 → 整个 EIF 可以完全通过**回归** + **倾向得分** + **密度比回归** 来估计。

**[0:16:45 - 0:20:00]** 渐近线性条件与双重稳健性（slide [11/20] & [12/20]）：
- **状态条件的核心**：nuisances 之间的收敛速率需要满足**乘积条件**，例如对于某对 nuisance（回归 + 密度比），要求它们的 L2 收敛速度的倒数和 ≥ 1/2。这是典型的“慢速率 vs 慢速率 = 根号 n 整体”的逻辑。
- **双重稳健性**：两种方式达到一致 —— (a) 所有顺序回归一致且 | (b) 倾向得分 + 密度比估计一致。不需要两者同时。
- 注意：slide [12/20] 列出了不同的稳健性“路径”（基于条件密度的路径、基于顺序回归 vs 密度比直接估计的路径、基于顺序回归 vs 贝叶斯重参数化的路径）。这些路径在实际操作中提供灵活性。

**[0:20:00 - 0:24:00]** **flexCausal** R 包演示：以前门模型为例，通过 `make.graph()` 定义 ADMG，再调用 `flex_est(a=c(1,0), data, graph, treatment, outcome)` 即可得 ATE 的点估计和置信区间；输出会判断图是否非参数饱和（若饱和则报告所使用的估计量是有效估计量）。

**[0:24:00 - 0:27:32]** 假设检验（字幕听为 “testing”）：
- 具体针对 front-door 模型。该模型本身非参数饱和（对观测数据不施加约束），不可直接检验。
- 引入 **anchor variable** Z（预处理变量，与 A 和 M 有关，且不影响 Y），来产生一个**Verma 约束**（即干预 M 后的条件独立关系 `Z ⊥ Y | X`）。这个约束可被用于检验 front-door 的识别假设（无直接效应 + 各条件可忽略性）。
- 已有 Bhattacharya & Nabi (2022) 提出两个检验统计量；讲者的贡献：将这个检验变成**双重稳健检验**——不仅检验统计量本身要双重稳健，所使用的高方差估计量也要双重稳健，以允许 ML 估计 nuisance。

**[0:27:32 - 0:31:15]** **Napkin graph**（亦称 bow graph）：primal fixability 不成立的例子，但 ATE 仍可识别。识别函数呈现为**两个 g-formula 之比**。
- 第一个 g-formula 分子：在干预 Z=z* 下，$\mathbb{E}[I(A=a_0) Y]$。
- 第二个 g-formula 分母：在干预 Z=z* 下，$\mathbb{E}[I(A=a_0)]$。
- 有趣的性质：ATE 对 z* 的选择是不变的（z* 可在 Z 的全支撑上任取）。
- **效率提升**：由于不变性，对于不同的 z* 可得到不同的影响函数；讲者提出将一族影响函数线性组合（权重和为 1），再估计出最小方差权重，从而得到一个**加权影响函数估计量**，模拟显示方差减小。但严格推导 Verma 约束下的切空间（nuisance tangent space）是公开问题。

**[0:31:15 - 0:31:30]** 总结与未来工作。

**问答环节关键点**（第二场演讲的问题中对第一场的回应？实际上第二场是第二位的；第一场结束后主持人直接说 Razi 已回答完问题。据 slide 与转写，没有第一场的问答环节，但讲者 slide 上已有测试部分）——转写中第一场结束后即进入第二场闭合，无 QA。

### 四、对应论文与开放问题

#### 对应论文

1. **Guo, Benkeser, & Nabi** (2023). "Flexible Nonparametric Inference for Causal Effects under the Front-Door Model." **arXiv:2312.10234**. —— 对应报告中“front-door 模型下的估计 + 假设检验”部分。✅ 用户已在 Candidate papers 中给出。
2. **Guo & Nabi** (2024). "Average Causal Effect Estimation in DAGs with Hidden Variables: Beyond Back-Door and Front-Door Criteria." **arXiv:2409.03962**. —— 对应“primal fixability 类的统一估计框架”。✅ slide 明确标记，是主体。
3. **Guo, Benkeser, & Nabi** (2025? slide 写 2512.19861). "Causal Inference with the 'Napkin' Graph." **arXiv:2512.19861**. —— 对应 Napkin graph 部分。字幕听成 "b2 b0"，slide 明确写 **arXiv 2512.19861**。
4. （报告中提及的 works）Bhattacharya, Nabi, & Shpitser (2020) "Semiparametric inference for causal effects in graphical models with hidden variables." JMLR。—— 提供了最初始的 EIF。讲者的工作大量建立于此 EIF 并对之进行重参数化。
5. Bhattacharya & Nabi (2022) 关于 front-door 的假设检验（slide [14/20] 引用，anchor variable 方法）。

⚠ 注意：以上 arXiv 编号对 paper 1 和 2 是确定的（slide 与转写均验证）；paper 3 需从 slide 确认（编号 2512.19861，但 ASR 完全听错）。建议去 arXiv 核实。

#### 报告留下的开放问题

1. **Verma 约束下的半参数效率理论**（转写 [0:24:39-0:24:41]：“the nuisance tangent space under the Verma constraint... is still an open question” + slide 末尾）。目前只能用启发式方法（加权影响函数）来选最优 z*；完整的效率界推导尚未完成。
2. **超越 front-door 模型的假设检验**（转写 [0:25:59-0:26:04]：“propose testing methods and sensitivity analysis beyond the front-door model, but instead for the entire class of models” ）—— 对 primal fixability 类内一般的图，如何系统地检验图结构假设？
3. **Napkin graph 的最优 z* 选择的严格理论**（转写 [0:24:23-0:24:26]：“which C star gives us the most efficient estimator... in a rigorous way to answer this question is by deriving the nuisance tangent space”—— 在完整的半参数效率理论出来之前，加权组合的方差最小化是一个工程解，但未知是否已被完整刻画。
4. **flexCausal R 包在更复杂图（高维 X 或 K 个中介）上的计算可扩展性与渐近精度** —— 如何在保持理论上根号 n 一致性与实际计算成本之间平衡？是否适用于 high-dimensional settings？讲者未讨论。

---

**给研究者的建议**：如果你对**半参数效率理论 + 高阶 U 统计量**感兴趣，报告中的“影响函数重参数化”和“乘积 R2 条件”可能与你熟悉的 HOIF 方法产生共鸣——此处 EIF 中多乘积交互项（密度比 × 回归误差）的高阶偏置分析、以及“多个 nuisances 的收敛速率乘积”的根号 n 条件，与 You 正在读的 HOIF 理论有潜在联系。尤其是当 Z_k 个数 K 很大时，顺序回归与 EIF 的复杂度可能涉及类似 tensor contraction 的因子化形式，这正是你“统计计算”兴趣的切点。

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

