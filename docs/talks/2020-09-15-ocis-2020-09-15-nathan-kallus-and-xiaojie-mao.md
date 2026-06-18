# Localized Debiased Machine Learning: Efficient Inference on Quantile Treatment Effects and Beyond

**讲者**: Nathan Kallus and Xiaojie Mao  
**讨论人**: Alex andre Belloni  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2020-09-15  
**主题**: 因果推断  
**视频**: <https://www.youtube.com/watch?v=ZhKfclG-eSQ> · [幻灯片](https://drive.google.com/file/d/1gR68Msb5ApyEtOfdFXYo2nxhdUuqnl_p/view?usp=sharing)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

## 相关论文

- [1912.12945](https://arxiv.org/abs/1912.12945) *（尚未精读 — `talks read --id … --read-papers` 可补）*

---

### 一、这场报告在讲哪条工作线

**核心问题**：如何在一个低维参数 \(\theta\) 由**包含高维干扰项（nuisance）的矩条件**定义、且干扰项又**依赖于参数本身**（estimand-dependent nuisances）的问题中，用灵活的机器学习方法进行高效估计和推断？典型例子是因果推断中的（局部）分位数处理效应（(L)QTE）估计。

**子方向背景**：
- **矩估计 + 干扰项处理**：经典 Z-估计中，当干扰项弱收敛速度慢于 \(\sqrt{n}\) 时，直接代入会污染目标参数的收敛。**去偏机器学习（DML）**（Chernozhukov et al. 2018）通过**Neyman 正交性** + **样本分割（cross-fitting）** 来解决：只要干扰项的估计误差乘积为 \(o_p(n^{-1/2})\)，目标参数就能达到 \(\sqrt{n}\)-收敛和渐近正态。
- **DML 的局限性——非线性参数依赖的干扰项**：DML 通常假设矩函数 \(\psi\) 线性于 \(\theta\)（如 ATE），此时干扰项不依赖 \(\theta\)。但当 \(\psi\) 非线性（如 QTE），干扰项 \(\eta_1(Z,\theta)\) 是 \(\theta\) 的连续函数（如条件 CDF），DML 要求先拟合**整个连续函数族** \(H = \{\eta_1(\cdot,\theta): \theta \in \Theta\}\)——这通常不适用于标准的监督学习回归（回归的标签是单个标量，而非一个函数）。
- **已有尝试**：
    - Belloni et al. (2017) 在 QTE 中用**连续族 Lasso**（需离散化 \(\theta\) 网格），分析高度特定于 Lasso，且计算量大。
    - Firpo (2007) 用极光滑的 sieve 估计器，要求较强光滑性，且仍无法对接现代 ML。

**这场报告的站位**：提出 **局部去偏机器学习（LDML）**，在不拟合整个连续函数族的前提下，复用正交性 + cross-fitting。核心洞察：**只需一个粗糙的初始估计 \(\hat{\theta}_{\text{init}}\)，然后在 \(\hat{\theta}_{\text{init}}\) 处局部估计依赖 \(\theta\) 的干扰项**（此时变成单个回归任务），即可恢复渐近效率和有效性。这实质上是将“连续族估计”简化为“单点估计”，极大放宽了对 ML 方法的要求。

**关键引用**：
- DML：Chernozhukov et al. (2018), "Double/debiased machine learning for treatment and structural parameters"（Econometrics Journal）.
- 连续族 Lasso：Belloni, Chernozhukov, Fernández-Val, Hansen (2017), "Program evaluation and causal inference with high-dimensional data"（Econometrica）.
- 高效 QTE 正交矩：Robins & Rotnitzky (1994), Tsiatis (2007) 的完全数据高效影响函数；Firpo (2007) 的 sieve 方法。

---

### 二、最小内核 / 一个最简例子

**符号设置**（特化为 QTE under ignorability）：

- **可观测数据**：\(Z = (X, T, Y)\)，i.i.d. 样本。
    - \(X \in \mathbb{R}^p\)：高维协变量（例如 \(p \gg n\) 或高维非参数）。
    - \(T \in \{0,1\}\)：处理变量。
    - \(Y \in \mathbb{R}\)：连续结果变量。
- **参数（estimand）**：\(\theta^*\) = 潜在结果 \(Y(1)\) 的 \(\gamma\)-分位数，即 \(P(Y(1) \le \theta^*) = \gamma\)（\(\gamma\) 给定，如 0.75）。
- **潜在不可观测量**：反事实 \(Y(1), Y(0)\)，只有 \(Y = TY(1) + (1-T)Y(0)\) 可观测。
- **可识别假设**：
    - 无混淆（ignorability）：\(Y(t) \perp T \mid X\)。
    - 重叠：\(0 < \pi^*(X) = P(T=1 \mid X) < 1\) 几乎必然。
- **干扰项**（nuisances）：
    - \(\pi^*(X) = P(T=1 \mid X)\)（倾向得分），**不依赖**参数。
    - \(\mu^*(X; \theta) = P(Y \le \theta \mid X, T=1)\)（条件 CDF 在处理组），**依赖**参数 \(\theta\)。
- **高效估计方程**（幻灯片 [Intro Method Theory]）：
    \[
    \psi(Z; \theta, \mu(X;\theta), \pi(X))
    = \frac{T}{\pi(X)} (I[Y \le \theta] - \mu(X;\theta)) + \mu(X;\theta) - \gamma.
    \]
    该矩满足 Neyman 正交性（对 \(\mu,\pi\) 的 Gâteaux 导数在真值处为 0）。

**最简例子（\(d=1\)，一个分位数，二值处理，\(X\) 可高维）**：
- 我们想估计“参加项目是否显著提升低收入人群的第 75 百分位收入”。
- 若直接使用 IPW 估计量 \(\hat{\theta}_{\text{IPW}}\)：只需估计倾向得分 \(\pi(x)\)，代入矩并解方程。但 \(\hat{\theta}_{\text{IPW}}\) 的收敛速度取决于 \(\hat{\pi}\) 的误差，通常慢于 \(\sqrt{n}\)。
- 若做标准 DML：需对**每一个可能的 \(\theta\) 值** 拟合条件 CDF \(\mu(x;\theta)\) —— 这要求学习一维的连续函数，典型 ML 方法无法直接输出一个函数族。
- **LDML 的解法**：
    1. 用 IPW 在数据子集 A 上估出**一个粗糙的初始估计** \(\hat{\theta}_{\text{init}}\)（可能收敛慢，\(n^{-1/4}\) 量级）。
    2. 在数据子集 B 上，**仅**在 \(\theta = \hat{\theta}_{\text{init}}\) 处拟合一个二值回归：\(\hat{\mu}(x) \approx P(Y \le \hat{\theta}_{\text{init}} \mid X=x, T=1)\)。这是一个标准的二值分类/回归任务。
    3. 将 \(\hat{\mu}(x)\) 和 \(\hat{\pi}(x)\)（从 B 估计）代入正交矩，在全集上解 \(\hat{\theta}\)。
    4. 最终 \(\hat{\theta}\) 达到与“知道真 \(\mu^*\) 和 \(\pi^*\) 的 oracle”相同的渐近表现，且是半参有效的。

---

### 三、报告主体：讲者讲了什么

#### 3.1 动机与问题（Nathan Kallus, [0:00:00–0:17:00]）

- **[0:01:18]** 用高中学电脑办公项目的例子说明：平均效应可能很小（0.1%），但第一四分位数效应可能很大（10%），因此分位数处理效应（QTE）在收入分布偏斜时比 ATE 更富信息。
- **[0:04:16]** 讲者用 CDF 图和水平距离直观定义 QTE：\(\theta^* = F_{Y(1)}^{-1}(\gamma)\)。
- **[0:06:39–0:12:00]** **IPW 估计及其问题**：
    - IPW 识别：\(E[ \frac{I[T=1]}{\pi(X)} I[Y \le \theta] - \gamma] =0\)。
    - 优点：只需估计倾向得分 \(\pi\)（标准二值回归）。
    - 缺点：\(\hat{\theta}_{\text{IPW}}\) 对 \(\hat{\pi}\) 的误差敏感——除非用极光滑的 sieve 估计器（Firpo 2007），否则 ML 估计的偏差（正则化/过参数化）和亚 \(\sqrt{n}\) 收敛会拖慢 QTE。
- **[0:11:54–0:16:00]** **正交性与 DML**：
    - 引出高效估计方程 \(\psi\)，满足 Neyman 正交性（在真值处对 \(\mu,\pi\) 的 Gâteaux 导数为零）。
    - DML：cross-fitting 替换干扰项估计，可达到 oracle 表现。
    - **但**：\(\mu^*(X;\theta) = P(Y \le \theta \mid X,T=1)\) 是 \(\theta\) 的**连续函数族**。拟合它对大多数 ML 不直接——要么用 kernel/kNN 权重做非参，要么用有限混合高斯等**参数化**方式。Belloni et al. (2017) 的“连续 Lasso”离散化 \(\theta\) 网格，理论分析与实践均复杂。
    - **[0:17:50–0:18:10]** 与 ATE 对比：ATE 的高效矩是 \(\theta\) 线性的，干扰项与 \(\theta\) 无关，故 DML 直接可用；非线性的 QTE 则“硬件上更难”。

#### 3.2 LDML 方法（Nathan Kallus, [0:18:47–0:33:30]）

- **[0:18:47]** **核心想法**：“如果我们**事先知道**一个粗糙的初始猜测 \(\hat{\theta}_{\text{init}}\)，就可以**只在那一个点**估计 \(\mu\)，避免连续族。” 这打破了 Catch-22——因为正交性意味着：只要 \(\hat{\theta}_{\text{init}}\) 与 \(\theta^*\) 足够接近，估计 \(\mu\) 时的错误不会通过正交矩放大。
- **[0:20:03]** **抽象框架**：数据 \(Z_i\) i.i.d.，参数 \(\theta^*\in \mathbb{R}^d\) 由矩条件 \(E[\psi(Z;\theta^*, \eta^*_1(Z,\theta^*), \eta^*_2(Z))] = 0\) 定义，其中 \(\eta_1\) 依赖 \(\theta\)（QTE 中的 \(\mu\)），\(\eta_2\) 不依赖（QTE 中的 \(\pi\)）。
- **[0:20:41–0:25:00]** **不变雅可比假设（Invariant Jacobian Assumption）**：
    - 若将 oracle 方程改为“将 \(\eta_1\) 中的参数固定在 \(\theta^*\)”后再解 \(\theta\)，其渐近线性表示中的雅可比 \(J^\diamond\) 与原始雅可比 \(J^*\) 相等。**讲者证明**（幻灯片 Proposition）：只要满足**Fréchet 正交性**（比 Gâteaux 更强的微分形式），该假设自动成立。而 Fréchet 正交性对 QTE、条件 VaR、IV 分位数等都成立（因为双鲁棒性——随机一个干扰正确时，矩不依赖另一个）。
- **[0:25:50–0:30:50]** **LDML 算法**（K-折，每折内三路分割）：
    1. 将数据随机均分 \(K\) 折。
    2. 对每折 \(k\)：
        - 在折 \(k\) 的补集 \(D_k^c\) 中，进一步分成两半 \(D_{k}^{c,1}\) 和 \(D_{k}^{c,2}\)。
        - 用 \(D_{k}^{c,1}\) 构建**初始估计** \(\hat{\theta}_{\text{init}}^{(k)}\)（如 IPW）。
        - 用 \(D_{k}^{c,2}\) 在 **固定** \(\hat{\theta}_{\text{init}}^{(k)}\) 下估计**依赖参数的干扰 \(\eta_1\)**（QTE中为 \(\mu\)，此时是单次回归）。
        - 用整个 \(D_k^c\) 估计不依赖参数的干扰 \(\eta_2\)（\(\pi\)）。
    3. 联合所有折，解矩方程或最小化 L2 范数得到 \(\hat{\theta}\)。
- **[0:30:50–0:33:00]** **方差估计与推断**：插件法估计渐近方差 \(\hat{\Sigma}\)（用 cross-fitted 干扰项），构造 Wald-型置信区间。谈到了**多重分割平均**（取中位数或 Winsorized 均值）以减少单次随机分割的噪声——但不影响一阶渐近。

#### 3.3 理论保证（Xiaojie Mao, [0:33:34–0:42:13]）

- **[0:35:48]** **QTE 下的具体干扰项收敛条件**：
    - \(\hat{\mu}\) 在 \(\hat{\theta}_{\text{init}}\) 处的误差 \(L_2\) 速率 \(\rho_{\mu,N} = o(1)\)。
    - \(\hat{\pi}\) 的误差速率 \(\rho_{\pi,N} = o(1)\)。
    - 初始估计误差 \(\rho_{\theta,N} = |\hat{\theta}_{\text{init}} - \theta^*| = o(1)\)。
    - 额外假定 \(1/\hat{\pi}\) 一致有界（保证逆概率权稳定）。
    - 对延续 CDF 的光滑条件（密度 a.e. 有正上下界，二阶导数有界）。
- **[0:38:09]** **主要定理**：若额外满足 **乘积率条件** \(\rho_{\pi,N}(\rho_{\mu,N} + \rho_{\theta,N}) = o(N^{-1/2})\)，则 LDML 分位数估计量 \(\hat{\theta}\) 渐近线性、正态，且达到半参有效界。
    - **讲者强调**：该乘积条件比 DML 标准分析所需的条件**更弱**——DML 对非线性矩通常需要每个干扰单独 \(o(N^{-1/4})\)，而这里允许个别速率慢、通过乘积调整。例如，若 \(\pi\) 估计很好（\(N^{-1/2}\)），\(\mu\) 可慢至 \(N^{-1/4}\) 甚至更慢，只要 \(\hat{\theta}_{\text{init}}\) 配合。
- **[0:39:49]** **延展至 QTE**：分别估计 \(Y(1)\) 和 \(Y(0)\) 的分位数后取差，保持效率。
- **[0:40:09]** **IPW 初始估计的特例**：若 \(\hat{\theta}_{\text{init}}\) 用 IPW，则 \(\rho_{\theta,N} = O(\rho_{\pi,N})\)。代入乘积率条件得 \(\rho_{\pi,N} = o(N^{-1/4})\)（即倾向得分估计需快于 \(n^{-1/4}\)）。讲者指出此时仍可通过 \(\mu\) 的慢速来补偿（若 \(\pi\) 快，\(\mu\) 可慢）。
- **[0:42:13]** 提到论文里还有对**均匀性**（uniform over classes）的更优结果，以及密度 \(J^*\) 的 IPW 核估计与自归一化稳定技巧。

#### 3.4 扩展与实证（Xiaojie Mao, [0:42:13–0:51:20]）

- **[0:42:13–0:45:08]** **局部 QTE（LQTE via IV）**：在二值工具变量 W、二值处理 T 的标准 IV 假设下，使用高效矩（含更多干扰项，如 complier 的条件分布），仍满足 Fréchet 正交性。LDML 可类似应用至 LQTE，渐近同样有效。
- **[0:46:36–0:49:30]** **实证示例**：401(k) 参与对净资产的 LQTE 影响（经典 IV 设置）。
    - 用 401(k) 资格作为 IV，协变量含高阶交互（20+ 个）。
    - 对比不同 ML 回归（Lasso、Boosting、神经网络）和不同折数 K=2,5,10，结果稳定。
    - 核心结论：LDML 实现简单，无需离散化网格，且结果与 Chernozhukov & Hansen 等低维/ Lasso 特定方法基本一致，但适用性更广。

#### 3.5 结论（Xiaojie Mao, [0:49:36–0:51:20]）

- 重申：对于分位数等**非平均**因果参数，DML 要求拟合连续函数族，不友好；LDML 用一个粗糙初始猜测 + 一次局部回归解决。
- 通用条件：Fréchet 正交性（比 Gâteaux 稍强但几乎所有双鲁棒模型满足）+ 干扰项估计的乘积率条件。

**讨论（Alexandre Belloni）与回应（[0:51:35–1:06:39]）**：
- Belloni 强调不变雅可比条件本质上是允许在干扰空间重新参数化的自由度；提出是否有**高阶渐近**的差异（即使用不同初始估计/干扰表示是否影响二阶行为）。讲者回应论文尚未涉及，但这确实是有趣的开放问题。
- 指出“连续 Lasso”在实际中只需 N 个网格点（非真连续），但 LDML 显然更简洁。
- 讲者确认 Eq.20 中的错误已在下个版本修复（用连续性而非二次上界）。

---

### 四、对应论文与开放问题

#### 4.1 对应论文

- **主论文**：arXiv 1912.12945, "Localized Debiased Machine Learning: Efficient Inference on Quantile Treatment Effects and Beyond", 作者 Nathan Kallus, Xiaojie Mao, Masatoshi Uehara.
    - 确认讲者即为该论文的作者（转写中 Masa 指 Masatoshi Uehara，已在报告开头提及）。
    - 幻灯片 URL 与 arXiv 一致。转写全程标题与方法名称吻合，未发现冲突信息。
- 幻灯片中提到代码仓库：https://github.com/CausalML/LocalizedDebiasedMachineLearning（尚未验证是否最新）。

#### 4.2 开放问题（每条扎根于转写）

1. **对概率质量（point mass）的鲁棒性**：Dominic 在 Q&A ([0:33:57]) 问若结果变量在分位数处有概率质量而非密度，LDML 的表现如何。讲者承认未在该场景模拟，是一个良好建议 —— 理论是否需要放松光滑性假设？哪些定理会断裂？
2. **初始估计的通用性**：Belloni 问题 ([0:51:35]) 问初始估计能有多“粗糙”？例如，若初始估计收敛慢于 \(n^{-1/4}\)，产品率条件是否还能通过 \(\mu\) 的慢速补偿满足？讲者未给出穷尽分类。
3. **更高阶渐近的影响**：Belloni 探讨 ([0:05:13] 讨论部分) 不同的干扰参数化/初始估计方式是否影响二阶项或有限样本表现？讲者承认未分析，指出这是一个很有前景的方向。
4. **方差估计器的稳定性**：密度 \(J^*\) 的 IPW 核估计（[0:40:50]）可能因极端逆概率权重而不稳，讲者提到自归一化或截断技巧，但未系统比较多种方差估计的敏感性。

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

