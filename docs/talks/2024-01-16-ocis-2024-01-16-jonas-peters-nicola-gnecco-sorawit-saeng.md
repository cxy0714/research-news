# On Invariance-based Generalization and Extrapolation

**讲者**: Jonas Peters, Nicola Gnecco, Sorawit Saengkyongam  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2024-01-16  
**主题**: 因果推断  
**视频**: <https://youtu.be/9eAZ0mv1PxE> · [幻灯片](https://drive.google.com/file/d/1RoehZaE1293SyI55-7vLnwsQ4-lVfcZ7/view?usp=sharing)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

---

### 一、这场报告在讲哪条工作线

这场报告系统性地探讨了**基于不变性（invariance）的分布泛化（Distribution Generalization, DG）问题**，并提供了新的理论解析与具体方法。该方向追问的核心问题是：

> 当训练数据来自多个环境（environments），且测试时环境（E）可能**未观测到**（观测到的X、Y与新环境的关系未见过）或**观测到但需要外推**时，如何学习一个预测函数 \(f(X)\)，使得其在所有可能的目标环境上的最坏情况风险最小？（即 min-max 问题）

- **奠基与主流路线**：
  - **不变性作为泛化桥梁**：该领域的大量方法（如 Peters et al., 2016 "Causal inference by using invariant prediction"；Rojas-Carulla et al., 2018 "Invariant models for causal transfer learning"；Arjovsky et al., 2019 "Invariant risk minimization"）基于一个核心假设：存在一种函数 \(f\)（通常称为“因果函数”）使得其残差 \(Y – f(X)\) 与环境 E **条件独立**或**矩不变**。这些方法希望，学习到的这种“不变函数”能在新的未知环境上泛化良好。
  - **当前 Frontier 与核心困境**：尽管方法众多，但**何时这种不变性必然保证最坏情况风险最优**的理论理解仍不完整。一个关键困境是，许多方法假设 \(X\) 的分布可以外推（extrapolation in X），却忽略了环境 E 本身的变化可能改变**混淆程度**。报告用一张表格清晰总结了这一困境（[0:14:24]–[0:19:15]）：如果只能在 X 上外推，而在 E 上不能外推（即函数不能控制 E 对混淆的影响），则分布泛化**不可能**（counterexample from [4]）。

- **这场报告的位置**：
  报告由三位讲者（Jonas Peters、Nicola Gnecco、Sorawit Saengkyongam(James)）共同完成。它**不是提出一个单一方法**，而是：
  1. **提供理论诊断**（第一部分，Jonas）：给出分类表，阐明在**双外推性（double extrapolability）** 满足时，分布泛化才可能成立。即，函数 \(f\) 必须既能外推其形式（在 \(X\) 空间上外推），又能外推其抵抗环境 E 影响的能力（在 \(E\) 空间上外推）。
  2. **提出具体方法**（第二部分，Nicola）：**Boosted Control Functions (BCF)**。该方法在**非线性**、**因果函数不可识别**（under-identified）、**存在未观测混淆**（hidden confounders）的设定下，通过“控制函数 + 提升步骤”构造一个兼具**稳定损失（stable loss）**和**高预测性**的函数，从而填满了表格的“右下角”（双外推性成立、E未观测的情况）。
  3. **迈向高维 / 表示学习**（第三部分，James）：当 \(X\) 是**高维观测**（如图像/文本）且由底层潜变量 Z 映射而来时，报告给出一种**可识别性**方法，通过学习一个 **线性不变（linearly invariant）** 的编码器，将高维 \(X\) 映射回潜变量 \(Z\)，从而实现干预外推（Intervention Extrapolation，测试时 E 可观测）。
  4. **关键理论贡献**：把**不变性假定的强弱**（单函数不变 vs 多函数不变）与**外推能力**（X 外推 vs E 外推）做了一个清晰的 2×2 分类，为整个领域提供了统一的理论框架。研究者可借此判断当前方法到底需要什么假设才能工作。

### 二、最小内核 / 一个最简例子

为了理解核心思想，聚焦于报告第二部分（BCF）在**最简单特例**下的设定。

**数据生成与符号**：
- **可观测数据**（Training）：\((X_i, Y_i, E_i)_{i=1}^n\)，其中 X = p 维预测变量，Y = 响应变量，E = 环境变量（离散或连续，视为外生变量）。
- **模型结构**（Additive Int-On-E Model）：
  - \(E = \epsilon_E\) （外生，独立于所有噪音）
  - \(Z = M E + V\) （Z = 潜变量，M 是 p × d_E 矩阵，V 是均值为0的噪音，独立于 E）
  - \(X = g(Z, \epsilon_X)\) （非线性混合函数 g，这里为了最简，假设 \(X = Z\) 即 g 为恒等映射 → 这实际上回到经典的 Control Function 线性情形）
  - \(Y = f^*(X) + h(V, \epsilon_Y)\) （加性模型，这里为了最简，假设 h 线性，即 \(h(V, \epsilon_Y) = \gamma^\top V + U\)，其中 U 是均值为0的噪音，且与 E、V 独立）
  - 注意：**\(U\) 与 \(X\) 相关**（通过 \(V\)），因此 \(X\) 和 \(Y\) 是**混淆的**（confounded）。直接回归 \(Y \sim X\) 会有偏差。

- **目标**：学习一个预测函数 \(\hat{f}(x)\)，使其在所有可能的 **do-interventions on E**（即改变 E 的分布，尤其外推至训练未见的 E 值）下，最坏均方误差最小。测试时 E 未观测。

**最简特例：** \(d_X = d_E = 1\)，单变量。
- 模型变成：
  - \(X = m E + V\) (m 是标量系数)
  - \(Y = f^*(X) + \gamma V + U\) （其中 \(\gamma\) 是标量，U 是噪音）
- **控制函数 (Control Function) 方法**：
  1. **Step 1**：用 \(E\) 对 \(X\) 做回归，得到残差 \(\hat{V} = X - \hat{m} E\) （即控制变量，分离出由 E 解释部分和与 E 独立的混淆部分）。
  2. **Step 2**：对 \(Y\) 关于 \(X\) 和 \(\hat{V}\) 做回归：
     \[
     \mathbb{E}[Y | X, \hat{V}] = f^*(X) + \gamma \hat{V}.
     \]
     这一步**识别了因果函数 \(f^*\)**，因为 \(\mathbb{E}[U | X, \hat{V}] = 0\)（由于 U 与 E 独立，条件独立性成立）。但经典的 Control Function 只输出 \(f^*(X)\)。

- **BCF 的关键提升**：
  在 Step 2 得到 \(f^*(x)\) 后，BCF 还考虑**剩下的 \(\gamma \hat{V}\) 部分**。由于 \(\hat{V}\) 部分地包含 \(X\) 的信息（因为 \(X = mE + V\) 中，V 是 X 中与 E 无关的“不变方向”），BCF 进一步用一个函数（例如非线性）从整个 \(X\) 中预测 \(\gamma \hat{V}\)：
  \[
  g_{\text{boost}} = \mathbb{E}_{\text{Ptr}}[\gamma \hat{V} | R_X = R_x],
  \]
  其中 \(R\) 是与 \(M\) 正交的方向（即 X 中不被 E 改变的部分）。最终输出：
  \[
  f_{\text{BCF}}(x) = f^*(x) + g_{\text{boost}}(x).
  \]
  **直觉**：\(f^*\) 已经保证了损失在所有 E 上稳定（constant loss）；而 \(g_{\text{boost}}\) 则利用 \(X\) 的“不变部分”来进一步提高预测精度（更有效），同时不破坏稳定性——因为 \(g_{\text{boost}}\) 属于“不变动量”（即其条件分布不随 E 变化的量）。BCF 是**兼具稳定性和预测性**的折中。

**核心结论**：在这个最简例子中，如果 \(f^*\) 是加性可分的，且噪声 U/V 支持有界或为高斯，则 BCF 是最小最坏风险最优的。

### 三、报告主体：讲者讲了什么

**第一部分：Jonas Peters——理论框架与核心困境（[0:01:05]–[0:21:30]）**

- **[0:01:05]–[0:05:00] 问题设置**：
  - 定义了 Deterministic Model vs Random Model，指出需要指定马尔可夫核 (Markov kernel) 以说清楚“对未见环境的手动干预”（do-operator）。
  - 提出两个场景：A) 测试时 E 可观测 → Intervention Extrapolation；B) E 不可观测 → Distribution Generalization，是本场重点。
  - 数学化 min-max 问题：\(\min_f \sup_{e \in \mathcal{E}} \mathbb{E}_e[(Y - f(X))^2]\)。

- **[0:05:00]–[0:10:30] 泛化的两条路线**：
  - 一条路线：找到**不变函数** (invariant function) → 推断其具有**稳定损失** (stable loss) → 若存在强的干预 E 则函数损失最小 → 实现泛化。
  - 强调：不唯一的立脚点是直接假设 \(f\) 求解 min-max；而是希望从训练集可验证的原则（不变性）推导出最坏情况风险最优。

- **[0:10:30]–[0:14:30] 不变性的含义与分类**：
  - 给出了4种训练集上的不变性定义：(a) \(Y – f(X) \perp\!\!\!\perp E\) (强不变); (b) \(\mathbb{E}[Y – f(X) | E] = 0\); (c) \(\mathbb{E}[(Y – f(X))E] = 0\); (d) 风险在E上常数。
  - 核心点：**并非所有不变性都能推出稳定损失**；需要更受限的模型（如 Additive Int-On-E 模型）。

- **[0:14:30]–[0:19:15] 关键分类表与双外推性**：
  - 引入两类不变性：**单不变函数** vs **多不变函数**。若只有一个不变函数（如因果函数），则问题退化为识别问题（如 IV）；若有很多不变函数，则需要外加“预测性最好”准则。
  - 2×2 表格 (slide "When do we have a chance of a stable loss?"):
    - 左上 (E=\(E_{tr}\), P_X dominated): 恒成立（λ = 单不变函数可 IV；多不变函数可通过 HSIC-X 等）。
    - 右上 (X 可外推, E 不可外推): 单不变函数 ✅ (如线性 IV)；多不变函数 **❌** (存在反例 [4])。
    - 左下 (E 可外推, X 不可外推): 单不变函数 ✅；多不变函数 ❌（类似反例）。
    - 右下（双外推）：**✅**：方法包括 subset searches（无隐藏）、anchor regression（线性）、BCF（非线性，有隐藏）。
  - **take-home**：依赖不变性进行泛化时，需要**双外推性**：函数既能外推其在 X 上的形式，又能外推其在 E 上的抗混淆能力（即能控制 E 对混淆程度的影响）。这个诊断非常清晰：不是所有不变性方法在X外推假设下都会工作。

**第二部分：Nicola Gnecco——Boosted Control Functions (BCF) ([0:21:35]–[0:41:10])**

- **[0:22:00]–[0:27:38] 模型与目标**：
  - 采用 Additive Int-On-E 模型，且 E 对 X 的影响是**线性**（X = M E + V），但 \(f^*\) 可以是非线性。V 和 U 在给定条件下相关，导致混淆。
  - 强调：该模型包含**协变量偏移**（E shift X 的边缘分布）和**概念偏移**（E 影响 V，从而改变 Y|X 条件分布）。
  - min-max 目标：\(\min_{f \in \mathcal{F}} \sup_{P \in \mathcal{P}} \mathbb{E}_P[(Y – f(X))^2]\)。

- **[0:27:38]–[0:32:14] BCF 三步法**：
  1. **控制变量**：从训练数据中，对每个观测计算残差 \(V = X – M E\)（M 可通过回归 X~E 得到）。这剥离了 X 中受 E 影响的部分。
  2. **控制函数方程**：运行加性回归：\(\mathbb{E}_{\text{Ptr}}[Y | X, V] = f^*(X) + \gamma(V)\)（关键：由于条件独立性 \(U \perp (X, V) | V\)，\( \mathbb{E}[U|X,V] = \mathbb{E}[U|V] \)，记作 γ(V)）。这直接识别了因果函数 f^*，但仅使用 f^* 会丢失预测力。
  3. **提升 (Boost)**：利用 X 中不被 E 影响的部分（正交于 M 的方向）预测 γ(V)。计算 \(\mathbb{E}_{\text{Ptr}}[\gamma(V) | RX = Rx]\)，其中 R 是 M 的正交补投影。最终：\(f_{\text{BCF}}(x) = f^*(x) + \mathbb{E}_{\text{Ptr}}[\gamma(V) | RX = Rx]\)。
  - **代码示例**：基于 scikit-learn 接口，可指定 \(f^*\) 和 γ 的学习器（如 RandomForest）。

- **[0:32:14]–[0:36:03] 可识别性与泛化保证**：
  - **可识别性定理**：BCF 从训练分布 \(\text{Ptr}\) 上可识别，条件为 (a) f^*, γ 可微 & 存在联合密度；或 (b) γ 线性 & E 分类。若 BCF 本身（作为函数）能外推（如线性），则在测试支持上也可识别。
  - **泛化定理**：若噪声 (U,V) 支持有界或为高斯；存在强手段使 E 的方差可以任意大（部分环境遍历所有 E 方向）；且函数类 \(\mathcal{F}\) 能外推（如决策树外推为常数）；则 BCF 的 **sup-risk 等于** 最小可能风险。并且，BCF 的残差分布独立于 E，且它**是所有具有稳定损失的函数中预测性最强**。

- **[0:36:03]–[0:41:10] 数值实验与总结**：
  - 实验：d_X=10, E 维度从1→10, E 方差增大。对比 Plain regression（退化） vs BCF（接近理论最优）。
  - 总结：BCF 填满了 Jonas 表格中右下角的情况：全非线性、不可识别因果函数、存在隐藏混淆；需要 X 和 E 都能外推。

**第三部分：Sorawit Saengkyongam (James)——干预外推的可识别表示 ([0:41:20]–[0:57:11])**

- **[0:41:20]–[0:44:21] 动机**：连接因果表示学习与分布泛化。提出能识别潜变量的**表示**，用于**干预外推**（E 在测试时可观测但外推），并给出可能的实用框架。

- **[0:41:50]–[0:48:30] 模型**：类似于 BCF，但 X 是**高维观测**（隐性变量模型），由潜变量 Z 通过非线性可逆映射 Q 生成：\(X = Q(Z, \epsilon_X)\)。Z 满足 \(Z = M E + V\)（线性效应）。目标为计算 \(\mathbb{E}[Y | do(E=e^*)]\) 当 \(e^*\) 在训练外。

- **[0:48:30]–[0:56:00] 可识别性与方法**：
  - 引入**线性不变 (linearly invariant)** 条件：对于编码器 \(\phi\)，要求 \(\mathbb{E}[\phi(X) – \mathbb{E}[\phi(X)|E] \mid E] = 0\)（即残差均值为0）。
  - 定理：在线性、可逆、Latent 为全支撑假设下，上述条件与编码器 β 的双射性共同保证 \(\phi\) 能识别 Q 的逆（可逆变换），从而识别潜变量 Z。
  - 实际操作：用正则化自编码器（重建损失 + MMD 惩罚实现线性不变条件）来训练 \(\phi\)。得到 \(\phi\) 后，用控制函数法构建估计量 \(\hat{\mathbb{E}}[Y | do(E=e^*)]\)。

- **时间限制，略去了数值实验**。

### 四、对应论文与开放问题

**对应论文**：

1. **Boosted Control Function (BCF)** 方法：
   - 报告引用：Nicola Gnecco, Jonas Peters, Sebastian Engelke, Niklas Pfister. "Guarantees for Invariance-based Generalization"（或类似标题，待查 arXiv）。其中引文的数字[7,15,23]对应 Control Function 的经典文章（如 Heckman, Newey, etc.）。  
   - 幻灯片末尾代码库提到 GitHub 仓库（待核实）。  
   - 状态：Abstract 提到 16. Jan 2024 报告，论文可能已投稿或即将公开。

2. **Identifiable Representation for Intervention Extrapolation**：
   - 报告引用：Sorawit Saengkyongam, Elan Rosenfeld, Jonas Peters. “Identifying Representations for Intervention Extrapolation”（待查）。可能已有一篇论文或工作论文。

3. **Theoretical Classification Table**：
   - 第一部分的理论框架（尤其是不变性→稳定损失的条件）目前是工作进展（work in progress），且涉及与 Niklas Pfister 的讨论，尚未有正式论文，但附有文献列表：[1,3,20,21,22,25,6]等 —— 可作为该领域的经典引用索引。

**开放问题（扎根于转写）**：

1. **如何将分类表扩展到非加性损失（如分类）？**  
   [0:19:00–0:20:25]：Jonas 提到（非同行评审）他们认为类似的反例在分类中同样存在。当前结论尚缺严格证明，开放: “不同损失函数下，双外推性是否仍是必要条件？”

2. **当 E 是分类变量时，如何放松“强干预”假设？**  
   [0:20:35–0:20:40]：Jonas 直接问：“if E is categorical, when is double extrapolation ever satisfied?” 这是方法 BCF 的天然局限：若 E 维度小于 X 维度，部分 X 变化方向无法被 E 触发，因此可能永远无法实现“对所有 X 方向稳定”。开放: 发展无需遍历所有方向干预的泛化保证。

3. **高维非线性表示学习的适用性与计算代价**  
   [0:41:20–0:56:00] 中，James 的方法假设 Q 是单射的，这在高维现实问题（如图像生成）中很可能被违反。开放问题：当 Q 不为单射（如 X 是压缩感知下采样），是否还能构造可靠的干预外推估计器？此外，MMD 惩罚 + Autoencoder 的双重目标是计算敏感的，目前没有给出一种有效的理论误差界。

4. **不变性条件的计算复杂性**  
   报告中提到“许多方法存在”，研究者可以从**统计-计算权衡**角度追问：给定很少的环境（小样本 E），能否有效检验哪些函数满足强不变性？是否存在低次多项式阻碍（低度多项式屏障）？这引出一个开放问题：**在训练环境数量小于特征维度时，不变性检验的计算复杂度是否为指数级？**（特别在高维 X 与小 n_E 时，EIV-like 问题）。如果用户对信息-计算差距（information-computation gap）熟悉，这是极具潜力的交叉点。

5. **“提升”步骤的计算代价**  
   BCF 的第三阶段需要将潜变量 γ(V) 与 X 通过 R_x 匹配，这涉及训练多个回归器。在高维情况下，是否存在类似 “树宽/张量收缩计算模型”（用户熟悉的 HOIF / U-stat 计算复杂度）可以刻画这个步骤的计算瓶颈？开放：BCF 中“提升”部分的最优统计-计算 tradeoff。

6. **双外推性假设中的结构假设**  
   报告的表依赖“双外推性=外推 X + 外推 E”。一个更深的问题：**在何种半参数假设下，这种双外推性可以降低为“单外推性”（例如用很少的环境就够）？** 例如，若 f^* 是稀疏的线性，是否只需 X 方向的有限外推就能识别？这里与用户熟悉的高维统计（随机矩阵、稀疏性、最小-最大边界）高度契合。

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

