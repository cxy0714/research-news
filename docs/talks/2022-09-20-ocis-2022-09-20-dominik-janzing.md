# Formal framework for quantitative Root Cause Analysis

**讲者**: Dominik Janzing  
**讨论人**: Niklas Pfister  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2022-09-20  
**主题**: 因果推断  
**视频**: <https://youtu.be/MVEwsc4oCHg> · [幻灯片](https://drive.google.com/file/d/18ECQEnVUUzsU7B6P-kG9DtaXSj-EyU4X/view?usp=sharing)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

## 相关论文

- [1912.02724](https://arxiv.org/abs/1912.02724) *（尚未精读 — `talks read --id … --read-papers` 可补）*

---

### 一、这场报告在讲哪条工作线

这场报告的核心工作线是 **“基于因果结构的定量根因分析 (Root Cause Analysis, RCA)”**，它试图回答一个曾被大量工程文献使用、却缺乏数学定义的工程问题：**在一个由已知有向无环图 (DAG) 描述的复杂系统（如供应链、计算机网络）中，当某个目标变量出现异常（离群值，outlier）或整体分布发生改变时，如何将这种异常或变化定量地归因到系统的各个组件（即 DAG 中的节点）上？**

该工作的主要背景和当前前沿如下：

*   **核心追问**：区别于“因果效应”问题（问的是“若干预某变量，目标变量会如何变化”），根因分析追问的是“**当前这个异常中，哪个上游变量的行为‘不正常’，并且对目标变量的异常有实质贡献**”。关键在于，一个“表现正常”（即它的机制/噪声值符合历史分布）的中介变量，即使它对目标有很强的因果影响力，也不应被认定为根因。
*   **奠基与主流路线**：在 Janzing 等人的工作之前，大量工程文献中的 RCA 缺乏统一的数学框架。相关工作包括：用于解释黑箱模型预测的 **Shapley 值（针对特征归因）**、因果推断中的 **路径特定效应 (Path-Specific Effect, PSE)**、以及 **中介分析 (Mediation Analysis)**。但报告指出，这些工具并不能很好地满足根因分析的需求。
    *   **Causal Shapley values** (Heskes et al., 2020) 和 **Asymmetric Shapley values** (Frye et al., 2020)：对“纯传播节点”（如 `X -> Y -> Z` 中的 `Y`）也会赋予贡献，这不符合根因分析的直觉。
    *   **Information Flow** (Ay and Polani, 2008)：同样存在上述问题。
    *   **总效应 / 直接效应**：总效应会给传播节点贡献；直接效应则试图“剥离”上游影响，这恰恰与根因分析想要捕获的“上游传播”背道而驰。
    *   **稀疏机制迁移假设 (Sparse Mechanism Shift Hypothesis)** (Schölkopf et al., 2021)：为“分布变化”这一子问题提供了启发——小的分布变化通常只影响少数几个条件分布。这场报告将自己的工作放在了这个更宏大的假设背景下，但提供了定量归因的具体工具。
*   **这场报告的站位**：它站在“**从因果机制 (Causal Mechanism) 的视角进行归因**”这一新兴路线上，与主流“基于特征值”或“基于干预效应”的归因形成了鲜明对比。它提出的核心思想是：**贡献应归属于变量的“内在机制”（即 FCM 中的噪声项或条件分布），而非变量本身的值**。在这个框架下，一个纯“技术性节点”（如水管连接处、仅做加法的中间变量）如果机制本身没有变化，就不会被认为是根因。

**对应论文（已被幻灯片确认）**：
*   Janzing, D., Budhathoki, K., Minorics, L., & Blöbaum, P. (2022). *Causal structure based root cause analysis of outliers*. ICML 2022. (arXiv: 1912.02724) —— 本场报告的主要论文。
*   Budhathoki, K., Janzing, D., Blöbaum, P., & Ng, H. (2021). *Why did the distribution change?* AISTATS 2021.
*   Janzing, D., Blöbaum, P., Minorics, L., Faller, P., & Mastakouri, A. (2020). *Intrinsic Causal Contribution*. arXiv:2007.00714.

---

### 二、最小内核 / 一个最简例子

考虑一个最简单的逻辑 AND 门模型，来展示这个框架的核心思想。

**符号与模型 (AND 门例)**：

*   **DAG**: 目标变量 `Y` 由两个独立的原因变量 `X1` 和 `X2` 通过逻辑 AND 门决定。
*   **FCM**: `Y = f(X1,N1) ∧ f(X2,N2) = X1 ∧ X2`。此处函数 `f` 是恒等映射，而噪声项 `N1`, `N2` 是各自变量取值为 0 或 1 的随机性来源。为了简化，可以直接把 `X1`, `X2` 视为独立的伯努利随机变量，其参数即为 `P(X1=1)` 和 `P(X2=1)`。注意，这里 `X1` 和 `X2` 没有父节点，所以 Y 的父节点就是 X1 和 X2。
*   **可观测数据**：一次观测到 `(X1=1, X2=1, Y=1)`，这是一个罕见事件。
*   **估计目标 (Estimand)**：`P(Y=1) = P(X1=1) * P(X2=1) = p1 * p2`。我们需要将此事件的罕见性（用 outlier score 度量）归因给 `X1` 和 `X2`。

**核心思想展开**：

1.  **异常度量 (Outlier Score)**：`S(y) = -log P(Y >= y) = -log P(Y=1) = -log(p1 * p2) = -log(p1) - log(p2)`。异常分数可以分解为各输入异常分数的和。

2.  **贡献归因**：现在问题是，`-log(p1)` 和 `-log(p2)` 分别应该被归因为 X1 和 X2 的贡献吗？
    框架通过回答“如果我将一个变量的机制替换为‘正常’机制，目标异常会减少多少？”来定义贡献。
    *   **把 `X1` 的值替换为从它的正常分布 `P(X1)` 中随机抽取的一个值**，而不是将其固定为 1。假设 `X1` 是罕见的 (`p1=0.1`)，那么替换后，`X1` 很可能变成 0，从而 `Y` 由 1 变成 0 的概率极高。这个操作极大地改变了 `P(Y=1)`。
    *   **相比之下，如果 `X2` 是频繁事件 (`p2=0.9`)，将其值替换为从正常分布 `P(X2)` 中抽取的值，它大概率仍是 1，对 `P(Y=1)` 的改变很小。**
    *   因此，**贡献大小自然地与事件的罕见程度成正比**。在 SHApley 值对称化后，`X1` 的贡献是 `-log(p1)`，`X2` 的贡献是 `-log(p2)`。由于 `p1` 小（罕见），`X1` 贡献大（100% 的贡献归于 `X1` 的假设下）；由于 `p2` 大（频繁），`X2` 贡献小。

3.  **为什么不是直接根据因果效应归因？**
    *   **总效应**：干预 `do(X1=1)` 对 `Y` 的影响是巨大的，同样干预 `do(X2=1)` 也可能影响巨大（如果 `X2` 本来大概率是 1，则干预 `do(X2=1)` 影响很小，但这是特殊情况）。但这里的关键是，即使 `X2=1` 不是罕见事件，它在这次事件中仍是必不可少的，但我不该因此惩罚它。
    *   **直接效应**：`X1` 和 `X2` 都是 `Y` 的“直接”原因，所以直接效应也无法区分。
    *   **框架**：通过比较“真实值”和“正常分布下的随机值”对目标事件概率的影响，量化了“**在这个特定观测中，这些变量值偏离其常态的程度**”。这正是“根因”的要义：找到“行为异常”的源。

这个例子完美体现了框架的“不惩罚纯传播节点”性质，以及罕见事件更容易获得高贡献的特性。

---

### 三、报告主体：讲者讲了什么

此节按照讲者的叙述顺序，结合时间戳和幻灯片内容，复原其核心论点。

**0. 定位与动机 [0:03:00 - 0:07:00]**
*   **[0:03:00]** 讲者开场就声明：“this talk is not really about an algorithm ... it's more about a concept”。他明确将工作定位为提出“根因分析”的**形式化概念框架**，而非一个具体的、即插即用的算法。
*   **[0:04:05 - 0:05:05]** 展示了框架的三个应用领域：(1) RCA of outliers, (2) RCA of distribution change, (3) Intrinsic Causal Contribution (方差归因)。
*   **[0:05:05 - 0:05:58]** 引入**模块化视角**：因果贝叶斯网络分解为条件分布 `P(Xj|PAj)`，功能因果模型 (FCM) 分解为 `Xj = fj(PAj, Nj)`。这些“模块/机制”是独立的，可以被替换。

**1. 关键区分：RCA ≠ 治疗效应 [0:06:00 - 0:07:30]**
*   **[0:06:00]** 讲者通过“雷暴 -> 停电 -> 服务器宕机 -> 收入下降”例子，明确指出：**“treatment effect of do-interventions on server outage on revenue may be large, but server outage was not the root cause – it just showed its usual behaviour!”** 这是整个报告最重要的概念飞跃。
*   **[0:07:00]** 幻灯片第 5 页明确写着：“Root Cause Analysis is different from analyzing Treatment Effect”。

**2. 核心机制：替换机制而非替换值 [0:07:35 - 0:12:00]**
*   **[0:07:35]** 提出的核心流程：将节点 `j` 的**机制**（在 FCM 中是噪声 `Nj`，在CBN中是条件分布 `P(Xj|PAj)`）替换为“基线机制”，观察对目标量的影响。
*   **[0:08:00 - 0:08:45]** 基线定义：
    *   异常归因: 替换异常噪声 `nj` 为“正常”噪声（从历史分布中抽样）。
    *   分布变化归因：替换异常的条件分布 `P(Xj|PAj)` 为基线分布 `~P(Xj|PAj)`。
    *   方差归因：将随机噪声 `Nj` 设为常数（如0）。
*   **[0:09:00 - 0:10:30]** **为什么要替换机制，而不是替换值？**
    *   幻灯片第 9 页：“Replacing mechanism at a node changes the way it reacts to its parent nodes. Reveals role of a node better than replacing its value.”
    *   讲者强调，一个“纯传播节点”（如 `X -> Y = X`）其机制是恒等函数。如果它正常工作，替换其机制（如改为 `Y = X + 噪声`）会使其反应异常，从而被识别为有所贡献。而替换它的**值**则不会产生这种效果，因为如果它传播了一个异常值，替换它的值就会错误地移除这个异常。
    *   **关键洞察**：在 FCM 的“响应函数形式化”下，改变噪声本质上等同于改变函数 `fj` 本身。因此，**“是函数变了还是噪声变了？”的区分在概念上消失了** —— 任何导致 `Xj` 无法用 `fj(paj, 正常噪声)` 解释的行为都被认为是该节点机制的异常。

**3. RCA of Outliers 的详细实现 [0:12:05 - 0:18:00]**
*   **[0:12:05]** **异常量化**：采用 `S(x) := -log P{ g(X) ≥ g(x) }`，其中 `g` 是一个特征映射（如 `g(x)=x` 用于单侧极值，或 `g(x)=|x-μ|` 用于与均值的偏差）。这种评分满足量纲无关性。
*   **[0:12:35]** **贡献计算**：
    1.  将目标 `Xn` 递归地作为其所有祖先噪声的函数 `Xn = F(N1, ..., Nn)`。
    2.  对每个噪声 `Nj` 的贡献定义为 `log ( P{ g(Xn) >= g(xn) | (N1,...,Nj) adjusted to normal } / P{ g(Xn) >= g(xn) | (N1,...,N_{j-1}) adjusted to normal } )`。这个比值描述了将 `Nj` 调整为正常值后，该异常事件概率下降的倍数。取对数后，贡献量就具有可加性。
    3.  由于对噪音调整的顺序会影响结果，使用 **Shapley 值 (Shapley values)** 在所有可能的顺序上平均，以获得顺序无关的贡献分配。
*   **[0:13:50]** **AND门例子**：`Y = X1 AND X2`。`S(Y=1) = -log(P(X1=1)) - log(P(X2=1))`。框架自动得出每个输入的贡献等于其自身 outlier score。讲者强调：“only rare events can get high contribution ... this is not put in by hand but just results from the framework”。
*   **[0:14:00 - 0:15:00]** **二骰子例子** (`D4` 和 `D100` 掷出 (1,1))：`log(4*100) = log 4 + log 100`，贡献分别为 23% 和 77%，与直觉（`D100` 掷出1更罕见）吻合。
*   **[0:15:25 - 0:18:00]** **回应两个常见误解**：
    *   **误解 1**：框架假设异常都由噪声引起，但函数也可能异常。回应：在响应函数框架下，函数和噪声的区别不是根本性的。节点 `Xj` 为根因当且仅当它不能用“正常”噪声和原有函数解释。
    *   **误解 2**：框架依赖于对噪声的干预，这很不自然。回应：改变噪声 `nj -> ~nj` 等价于对**观测节点** `Xj` 进行**父节点依赖的干预** (`do(Xj = fj(paj, ~nj))`)。因此，不涉及对潜在变量的直接操作。

**4. RCA of Distribution Change [0:18:30 - 0:22:00]**
*   **[0:18:30]** 讲者简要提及该子问题。核心思想是当联合分布 `P` 变为 `~P` 时，将变化归因到各个条件分布 `P(Xj|PAj)` 的变化。
*   **[0:19:00]** **KL距离** 可以自然分解为条件 KL 距离之和（幻灯片第18页），这与“替换机制”的框架完美契合。但存在一个微小问题：条件 KL 距离权重中包含父节点分布 `P(paj)`，所以严格讲不是纯机制的属性。
*   **[0:19:40]** 对父节点分布的变化是**弱相关**的，但无法避免。
*   **[0:20:00]** **稀疏机制迁移假设**：讲者指出，本工作与 Schölkopf et al. (2021) 的精神一致——变化应是稀疏的。可以通过条件独立性检验 (`Xj ⟂ L | PAj`) 来识别哪些机制发生了改变（`L` 是标记数据集的标签）。

**5. 实验与实现问题 [0:23:45 - 0:30:00]**
*   **[0:23:45]** 展示了英格兰四条河流的水位数据实验。DAG 已知，假设结构系数均为1。
*   **[0:24:00]** **实验结果**：如图例27-28页所示，根因分析发现下游站点 (NJR) 没有贡献，而上游三个站点的贡献大致均等。讲者解释道：“如果多个机制同时异常，很可能是有共同混淆因素（如大面积降水）”，这与“稀疏机制迁移假设”一致——当机制变化不满足稀疏性时，暗示着存在未观测的共因。
*   **[0:27:00 - 0:30:00]** **坦承实践难点**：
    *   学习 FCM 在异常区域是**统计上不适定**的（因为异常数据点很少）。
    *   从过去数据生成“正常”噪声值受趋势、季节性的影响。
    *   方法的扩展性（scaling behavior）尚不明确。
    *   讲者反复强调：“**the main contribution is not the practical method and a specific algorithm, but defining a clear concept of RCA... despite tons of papers on RCA we didn't find a clear concept.**”

**6. 哲学层面与讨论 [0:30:00 - 结束]**
*   **[0:30:00]** **基线选择的主观性**：讲者认识到，根因分析不可避免地涉及**规范性 (normative aspects)**。例如“雷暴”是根因，还是“电网应耐雷性更强”？这取决于基线机制的选择：是“过去发生了什么”（统计视角）还是“我们希望发生什么”（伦理视角）。这个框架通过选择不同的基线机制来容纳不同的视角。
*   **[0:38:00 - 1:02:00]** **Q&A 和讨论者 (Niklas Pfister) 环节**：讨论集中在 **鲁棒性（模型设定错误）**、**CPDAG/等价类的处理**、**隐藏共因**、**大规模系统中 Shapley 值的计算问题**。讲者回应，这些是开放的研究问题。

**关键技术技巧摘要**：
1.  **Shapley 值的因果归因应用**：用于解决多顺序归因的不可加性与路径依赖问题。
2.  **对数概率比的分解**：将异常的计算从干预后概率的尺度转换为对数尺度，实现了可加性与量纲无关性。
3.  **响应函数形式化 (response function formulation)**：将 FCM 重新解释为父节点到子节点函数的分布，从而模糊了“噪声变化”与“机制变化”的界限，简化了理论。

---

### 四、对应论文与开放问题

**对应论文（基于幻灯片和转写）**：

1.  **（核心）** Janzing, D., Budhathoki, K., Minorics, L., & Blöbaum, P. (2022). *Causal structure based root cause analysis of outliers*. **ICML 2022**. arXiv:1912.02724.
2.  Budhathoki, K., Janzing, D., Blöbaum, P., & Ng, H. (2021). *Why did the distribution change?* **AISTATS 2021**.
3.  Janzing, D., Blöbaum, P., Minorics, L., Faller, P., & Mastakouri, P. (2020). *Intrinsic causal contribution*. **arXiv:2007.00714**.

**开放问题及依据（均来源于转写和 Q&A）**：

1.  **模型设定错误的鲁棒性/Robustness**：[[0:38:00]-[0:39:00], Q&A, Niklas Pfister 提问] 如果 DAG 或 FCM 的结构/函数被错误设定，归因结果如何变化？[讲者在 [0:39:00] 回应“we are doing experiments on that... too preliminary to comment”]。**明确留出的问题**：能否推导出归因结果的上下界？
2.  **未知图结构（CPDAG/等价类）**：[[0:38:50], Q&A] 如何将框架推广到图结构仅知等价类（CPDAG）的情况？`[讲者回应“I don't have an answer yet”]`
3.  **隐藏共因**：[[0:39:55], Q&A] 如何处理隐藏共因？`[讲者做了回应，但指出` “You just need to have the FCM and then you have dependent noise terms, but you intervene on the noise so that destroys the correlations”`，这暗示了其框架在隐藏共因下的有效性部分依赖于对正确 `FCM` 的假设，并非完全“自由”。]`。
4.  **函数学习在异常区域的不适定性**：[[0:28:57]] “learning the functions fj in the outlier region is statistically ill-posed”。这直接点出：在极端值区域进行非参数回归的统计难度，是该方法实际落地的核心障碍。
5.  **扩展性（Scaling）**：[[0:29:08], [0:34:00-0:35:00]] “scaling behavior of the method is currently unclear”；在 Q&A 中被问及“how large of a DAG can you handle”，讲者回应“很难说，高度依赖假设，如果是线性函数会好很多”。
6.  **基线选择的规范性问题**：[[0:30:00]-[0:31:00]] 当基线机制反映“期望”而非“历史”时，归因结果会发生质变。如何将这种规范性需求形式化地纳入框架？`[讲者将此作为开放问题进行讨论，并非提出解决方案]`
7.  **Shapley 值的计算复杂性**：[[0:35:05 - 0:36:00]] 在大数量节点下，Shapley 值的计算是组合爆炸的。`[讲者仅提及“there are approximations”，未给出具体策略]`。

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

