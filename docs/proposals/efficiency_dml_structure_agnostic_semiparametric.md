# 选题提案 · 结构无关模型下的半参数效率与去偏

**战线范围**: 在不对 nuisance 函数施加具体结构（如光滑性、稀疏性）的设定下，推导半参数泛函的 minimax 下界、构造自适应去偏估计量并研究其渐近性质。  
**证据论文**: 30 篇（★ 收藏 11 篇）  
**提案条数**: 3  
**生成日期**: 2026-09-01  

> 每条提案的证据都点名来源论文 [k] 并引其原话。**不打分、不排名**——「证据 N 篇」是可数的事实，不是质量分。标了 ⚠️ 单点证据的条目只有一篇论文支撑，自己掂量。

---

### 提案 1：Structure-Agnostic Minimax Rates Under Asymmetric Nuisance Errors: Closing the Gap Between Upper and Lower Bounds

- **claim（一句话）**：在结构无关模型下，当倾向得分 \(\pi_0\) 和结果回归 \(\mu_0\) 的估计误差（近似误差 \(\delta_{\text{appr}}\) 与随机误差 \(\delta_{\text{stoc}}\)）不对称时，推导 minimax 风险 \(m(n, \bar{\delta}_\mu, \bar{\delta}_\pi)\) 的紧界，闭合 [1] Theorem A.1 中上下界之间的间隙，并推广 [3] 的混合光滑性下界至单一光滑情形。

- **最小内核**：先考虑最简特例：\(d=1\)，\(\mu_0\) 为常数（\(\delta_{\text{appr}}^\mu = 0\)，\(\delta_{\text{stoc}}^\mu = 0\)），\(\pi_0\) 需从数据估计且 \(\delta_{\text{appr}}^\pi, \delta_{\text{stoc}}^\pi \to 0\)。在此特例下，目标泛函退化为 ATE 的简单形式，minimax 风险退化为仅依赖 \(\bar{\delta}_\pi\) 的函数。需证明此时下界 \(n^{-1/2} + (\delta_{\text{appr}}^\pi + (\delta_{\text{stoc}}^\pi)^2)\) 与上界 \(\min\{n^{-1/2} + (\delta_{\text{stoc}}^\pi)^2, (\delta_{\text{appr}}^\pi + \delta_{\text{stoc}}^\pi)^2\}\) 是否匹配，并构造达到紧界的估计量。

- **证据**：
  - [1] 开放问题 1 扎根于 Theorem A.1：“上下界之间有间隙——扎根于 Theorem A.1 的陈述与作者对‘future studies’的提及”。具体地，上界为 \(\min\{n^{-1/2} + \delta_{\text{appr}} + (\delta_{\text{stoc}})^2, (\delta_{\text{appr}} + \delta_{\text{stoc}})(\delta_{\text{appr}}^\pi + \delta_{\text{stoc}}^\pi)\}\)，下界为 \(n^{-1/2} + (\delta_{\text{appr}} + (\delta_{\text{stoc}})^2) \cdot (\delta_{\text{appr}}^\pi + (\delta_{\text{stoc}}^\pi)^2) + (\delta_{\text{stoc}} \wedge \delta_{\text{stoc}}^\pi)^2\)，当 \(\pi_0\) 也可被黑盒估计时间隙存在。
  - [3] 开放问题 1 扎根于 Section 2.2：“a more structure-agnostic way ... would be to simply impose a rate condition ... We leave this refinement for future work”。该文的下界证明假设 \(f_\omega\) 和 \(f_\mu\) 都具有任意平滑性，但实际中可能只有一方平滑，需扩展下界到混合光滑性。

- **为什么现在**：[1] 和 [3] 分别独立给出了不对称误差下的上界和下界，但两者在率上不匹配。最近 [21] 的 TAME 框架在对称误差下实现了紧界，但其技术（局部编辑权重）可被改造用于不对称情形。此外，[5] 的 HOIF 分析揭示了单调偏置类泛函的偏差结构，为构造紧下界提供了新工具。

- **武器匹配**：使用 **very_familiar 中的“估计问题的 minimax 下界”** 技术，特别是 Le Cam 两点法和 Fano 不等式，针对不对称误差构造硬对（hard pair）分布，使下界中的混合项 \((\delta_{\text{appr}}^\pi + (\delta_{\text{stoc}}^\pi)^2)\) 与上界中的项对齐。同时利用 **高阶 U 统计量的计算（einsum）** 来高效计算下界证明中所需的矩。

- **风险与竞争**：该选题可能已被 [1] 或 [3] 的作者后续工作覆盖。需检查 [1] 的后续版本（如 arXiv 更新）或 [3] 作者（可能是 Balakrishnan 团队）的最新预印本。此外，若假设太强（如要求 \(\delta_{\text{appr}}^\pi\) 和 \(\delta_{\text{stoc}}^\pi\) 可分离），则紧界可能退化为平凡形式。需查阅 [21] 的附录是否已隐含不对称情形的结果。

- **交付形态**：`定理型`

- **第一周动作**：
  1. 读 [1] 的 Theorem A.1 及其证明，提取上下界表达式中的具体常数和条件。
  2. 读 [3] 的 Section 2.2 和 Proposition 2 的证明，理解混合光滑性下界的构造。
  3. 在最小内核（\(\mu_0\) 常数，\(\pi_0\) 需估计）下，写出下界证明的硬对构造草图。
  4. 检查 [21] 的 Theorem 2.1 和推论 2.2，看 TAME 的界在不对称误差下是否退化。
  5. 搜索 arXiv 上 [1] 和 [3] 作者的最新预印本，确认无重复。

---

### 提案 2：Debiased Estimation of Nonlinear Semiparametric Functionals Under Structure-Agnostic Models: Beyond Monotone Bias Class

- **claim（一句话）**：对于非单调偏置类的非线性半参数泛函（如期望条件协方差 ECC、二次泛函），在结构无关模型下构造一个渐近占优 DML 的估计量，并证明其 minimax 最优性，填补 [5] 中 ECC 互不占优的空白和 [21] 中仅限线性泛函的局限。

- **最小内核**：先考虑最简特例：\(d=1\)，目标泛函为 \(\theta = \mathbb{E}[Y - \mu_0(X)]^2\)（即条件方差泛函，属于二次泛函），且 \(\mu_0\) 和 \(\pi_0\) 均需从数据估计。在此特例下，DML 估计量的偏差为 \(\|\hat{\mu} - \mu_0\|^2\) 的乘积形式，而 HOIF 估计量需二阶修正。需证明是否存在一个估计量（如三阶 HOIF 或加权组合）能严格优于 DML，并给出其渐近分布。

- **证据**：
  - [5] 开放问题 2 扎根于 Section 4 和 Theorem 3：“对于期望条件协方差（以及 ATE, ATT 等），本文仅证明 HOIF 估计量与 DML 互不占优。是否存在其他估计量（如三阶 HOIF 或某种加权组合）能渐近占优 DML？需要进一步决策理论分析。”
  - [21] 开放问题 2 扎根于 Section 4：“TAME 的核心思想——局部编辑权重以满足对抗性矩约束——能否扩展到非线性泛函（如分位数处理效应、平均处理效应在子群上的投影）？这是作者明确留下的未来工作方向。”

- **为什么现在**：[5] 揭示了单调偏置类泛函的 HOIF 占优性，但 ECC 不属于此类，且 [21] 的 TAME 框架仅对线性泛函有效。最近 [4] 对二次泛函的 minimax 率给出了部分结果（Lemma 8 有 gap），[17] 的高维 AIPW 方差膨胀分析提供了非线性泛函偏差传播的新视角。这些进展使构造非线性泛函的紧界成为可能。

- **武器匹配**：使用 **moderately_familiar 中的“HOIF（高阶影响函数）”** 工具，推导 ECC 或二次泛函的二阶影响函数展开，并利用 **very_familiar 中的“高阶 U 统计量的计算（treewidth / tensor contraction / einsum）”** 来高效计算 HOIF 中的高阶矩项，避免组合爆炸。

- **风险与竞争**：该选题可能已被 [5] 或 [21] 的作者后续工作覆盖。需检查 [5] 的后续版本（如 arXiv 更新）或 [21] 作者（可能是 Gu 团队）的最新预印本。此外，若非线性泛函的偏差结构过于复杂（如涉及三阶乘积），则可能不存在多项式时间可计算的占优估计量，需考虑计算-统计权衡。需查阅 [4] 的 Lemma 8 是否已闭合二次泛函的 gap。

- **交付形态**：`方法+模拟型`

- **第一周动作**：
  1. 读 [5] 的 Section 4 和 Theorem 3，理解 ECC 的 HOIF 构造及互不占优的证明。
  2. 读 [21] 的 Section 4，理解 TAME 对线性泛函的扩展限制。
  3. 在最小内核（条件方差泛函）下，推导二阶影响函数表达式，并写出 HOIF 估计量的偏差-方差分解。
  4. 设计模拟：比较 DML、一阶 HOIF、二阶 HOIF 在 \(n=200, 500, 1000\) 下的 MSE 和覆盖概率。
  5. 搜索 arXiv 上 [5] 和 [21] 作者的最新预印本，确认无重复。

---

### 提案 3：Adaptive Hyperparameter Selection for Debiased Estimators in Structure-Agnostic Models: From Oracle to Data-Driven

- **claim（一句话）**：在结构无关模型下，为去偏估计量（如 SADE 的 under-smoothing 参数 \(\lambda\) 和 HOIF 的字典大小 \(k\)）设计数据自适应的选择准则，使得最终估计量在未知误差预算 \((\delta_{\text{appr}}, \delta_{\text{stoc}})\) 下达到 oracle 最优收敛率，并给出有限样本理论保证。

- **最小内核**：先考虑最简特例：\(d=1\)，目标泛函为 ATE，nuisance 函数 \(\mu_0\) 和 \(\pi_0\) 均用核回归估计（带宽 \(h\) 为唯一超参数）。在此特例下，SADE 的 under-smoothing 条件 \(\delta_{\text{appr}} \asymp (\delta_{\text{stoc}})^2\) 退化为带宽选择准则。需证明一个基于 Lepski 型自适应或交叉验证的带宽选择方法能自动达到该平衡，且不劣于 oracle 选择。

- **证据**：
  - [1] 开放问题 3 扎根于 Remark 2.1 与 Section 2.5：“理论建议 under-smoothing \(\delta_{\text{appr}} \asymp (\delta_{\text{stoc}})^2\)，但在实践中如何从黑盒 ML 的训练轨迹或超参数中量化 \(\delta_{\text{appr}}\) 与 \(\delta_{\text{stoc}}\)，以实现自动 under-smoothing？作者在 Remark 2.1 承认‘估计量本身 agnostic 到 \((\delta_{\text{appr}}, \delta_{\text{stoc}})\)，但族 \(\{\mathcal{G}_{\mu,s}\}\) 的最优选择需知晓预算’。”
  - [5] 开放问题 3 扎根于 Lemma 2-6 中关于 \(k\) 的上界条件：“HOIF 估计量需要选择字典大小 \(k\)，并涉及 Gram 矩阵估计。这带来计算成本（如 \(O(k^2)\) 或更高），可能与样本量 \(n\) 交互。论文给出 \(k = o(n)\) 条件，但未讨论如何最优选择 \(k\) 或自适应。”

- **为什么现在**：[1] 的 SADE 和 [5] 的 HOIF 都依赖 oracle 超参数选择，但 [21] 的 TAME 框架通过凸优化自动平衡偏差-方差，其思想可被借鉴用于自适应选择。此外，[17] 的高维 AIPW 方差膨胀分析提供了超参数与误差预算之间关系的定量刻画，[30] 的矩阵补全中样本门槛的 log 因子消除技术也可用于设计自适应准则。

- **武器匹配**：使用 **very_familiar 中的“非参数统计”** 中的 Lepski 自适应方法，结合 **very_familiar 中的“估计问题的 minimax 下界”** 来证明自适应选择的最优性。同时利用 **moderately_familiar 中的“HOIF”** 来推导字典大小 \(k\) 对偏差-方差的影响，并设计基于数据分裂的交叉验证准则。

- **风险与竞争**：该选题可能已被 [1] 或 [5] 的作者后续工作覆盖。需检查 [1] 的后续版本（如 arXiv 更新）或 [5] 作者（可能是 Balakrishnan 团队）的最新预印本。此外，若自适应选择需要估计 \(\delta_{\text{appr}}\) 和 \(\delta_{\text{stoc}}\)，而这两个量本身难以从数据中一致估计，则可能陷入循环。需查阅 [21] 的 TAME 是否已隐含自适应机制。

- **交付形态**：`方法+模拟型`

- **第一周动作**：
  1. 读 [1] 的 Remark 2.1 和 Section 2.5，理解 SADE 的 under-smoothing 条件及数值启发。
  2. 读 [5] 的 Lemma 2-6，提取 \(k\) 的上界条件及其对偏差-方差的影响。
  3. 在最小内核（ATE，核回归带宽）下，设计一个基于 Lepski 规则的带宽选择算法，并写出理论分析框架。
  4. 设计模拟：比较 oracle 选择、Lepski 自适应、交叉验证在 \(n=200, 500\) 下的 MSE 和覆盖概率。
  5. 搜索 arXiv 上 [1] 和 [5] 作者的最新预印本，确认无重复。

---

### 本页的证据论文

- [1] ★ [Optimally taming biases in black-box models for efficient semiparametric estimation](/research-news/deep_reads/2026-06-05-2606.06368/) — 2026-06-05
- [2] ★ [Binary regression and classification with covariates in metric spaces](/research-news/deep_reads/2026-06-19-10.1093_biomtc_ujaf123/) — Biometrics · 2026-06-19
- [3] ★ [Doubly-robust inference and optimality in structure-agnostic models with smoothness](/research-news/deep_reads/2026-06-19-2405.08525/) — 2026-06-19
- [4] ★ [Thin Sets Are Not Equally Thin: Minimax Learning of Submanifold Integrals](/research-news/deep_reads/2026-06-22-2507.12673/) — 2026-06-22
- [5] ★ [On the Asymptotic Inadmissibility of Double Machine Learning Estimators Under Structure-Agnostic Models](/research-news/deep_reads/2026-06-24-2606.22391/) — 2026-06-24
- [6] ★ [Direct and efficient estimation of bilinear forms in staggered tensor panels](/research-news/deep_reads/2026-07-09-2607.06330/) — 2026-07-09
- [7] ★ [On Rates Attainable under Random Design: A Negative Answer to a Problem of Robins](/research-news/deep_reads/2026-07-15-2607.13170/) — 2026-07-15
- [8] ★ [On the structural dimension of sliced inverse regression](/research-news/deep_reads/2026-05-26-10.1214_25-aos2505/) — Annals of Statistics · 2026-05-26
- [9] ★ [Group-Level Treatment Effect Heterogeneity in Difference-in-Differences: A Balanced Approach](/research-news/deep_reads/2026-06-25-2606.24785/) — 2026-06-25
- [10] ★ [Incremental effects for continuous exposures](/research-news/deep_reads/2026-08-31-2409.11967/) — 2026-08-31
- [11] ★ [Gradient-free stochastic optimization of derivatives under strong convexity](/research-news/deep_reads/2026-07-10-2607.07249/) — 2026-07-10
- [12] [Minimax rates for heterogeneous causal effect estimation](/research-news/deep_reads/2026-07-04-10.1214_24-aos2369/) — Annals of Statistics · 2026-07-04
- [13] [Targeted maximum likelihood estimation of vaccine effectiveness and immune correlates in test-negative design studies with missing data](/research-news/deep_reads/2026-05-22-2605.21793/) — 2026-05-22
- [14] [Average partial effect estimation using double machine learning](/research-news/deep_reads/2026-05-26-10.1214_25-aos2563/) — Annals of Statistics · 2026-05-26
- [15] [A Temporal Spatial Minimax Rate for Smoothly-Varying Distributions in Wasserstein Space](/research-news/deep_reads/2026-06-08-2606.07325/) — 2026-06-08
- [16] [Federated double machine learning for high-dimensional semiparametric models](/research-news/deep_reads/2026-06-19-10.1093_biomtc_ujaf150/) — Biometrics · 2026-06-19
- [17] [A new central limit theorem for the augmented IPW estimator: Variance inflation, cross-fit covariance and beyond](/research-news/deep_reads/2026-06-20-10.1214_24-aos2476/) — Annals of Statistics · 2026-06-20
- [18] [Semi-supervised U-statistics](/research-news/deep_reads/2026-06-20-10.1214_25-aos2550/) — Annals of Statistics · 2026-06-20
- [19] [Targeted estimation of state occupation probabilities for the non‐Markov illness‐death model](/research-news/deep_reads/2026-06-23-10.1111_sjos.12644/) — Scandinavian Journal of Statistics · 2026-06-23
- [20] [Towards a unified theory for semiparametric data fusion with individual-level data](/research-news/deep_reads/2026-07-04-10.1214_25-aos2609/) — Annals of Statistics · 2026-07-04
- [21] [Optimal use of a black-box learner in semiparametric estimation](/research-news/deep_reads/2026-07-27-2607.21541/) — 2026-07-27
- [22] [How Many Samples Are Needed to Determine Causal Direction? Sharp Minimax Bounds for Bivariate LiNGAM](/research-news/deep_reads/2026-08-18-2608.15840/) — 2026-08-18
- [23] [Minimax Limits of k-Fold Cross-Validation via Majority](/research-news/deep_reads/2026-05-26-2605.25859/) — 2026-05-26
- [24] [Near-optimal inference in adaptive linear regression](/research-news/deep_reads/2026-05-26-10.1214_24-aos2450/) — Annals of Statistics · 2026-05-26
- [25] [Minimax Private Estimation of Smooth Optimal-Transport Maps](/research-news/deep_reads/2026-06-04-2606.04683/) — 2026-06-04
- [26] [Nonparametric Riemannian Empirical Bayes, and Denoising Measurements on Manifolds](/research-news/deep_reads/2026-06-10-2606.11183/) — 2026-06-10
- [27] [Causal Sufficient Dimension Reduction for Multiple Continuous Exposures with an Application to Environmental Mixtures](/research-news/deep_reads/2026-06-17-2606.14840/) — 2026-06-17
- [28] [Minimax estimation of partially-observed vector autoregressions](/research-news/deep_reads/2026-06-18-10.1214_25-ejs2387/) — Electronic Journal of Statistics · 2026-06-18
- [29] [Nonparametric estimation of ordinary differential equations: Snake and stubble](/research-news/deep_reads/2026-06-18-10.3150_25-bej1936/) — Bernoulli · 2026-06-18
- [30] [Sharp bounds for multiple models in matrix completion](/research-news/deep_reads/2026-06-18-10.1214_26-ejs2503/) — Electronic Journal of Statistics · 2026-06-18

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

