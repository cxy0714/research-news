# 选题提案 · 去偏机器学习与正交分数理论

**战线范围**: 基于 Neyman 正交分数和 Riesz 表示子的去偏机器学习框架，包括交叉拟合、有限样本推断、自动去偏（AutoDML）以及在高维/非参数设定下的效率理论。  
**证据论文**: 30 篇（★ 收藏 15 篇）  
**提案条数**: 3  
**生成日期**: 2026-09-01  

> 每条提案的证据都点名来源论文 [k] 并引其原话。**不打分、不排名**——「证据 N 篇」是可数的事实，不是质量分。标了 ⚠️ 单点证据的条目只有一篇论文支撑，自己掂量。

---

### 提案 1：Semiparametric Efficiency Bounds for Proximal Dose-Response Functions and Distal Causal Excursion Effects

- **claim（一句话）**：推导 [4] 中近端剂量反应函数 \(\theta(a)\) 和 [1] 中远端因果 excursion 效应 (DCEE) 的半参数效率界，并证明现有去偏估计量是否达到该界。

- **最小内核**：考虑最简单的设定：二元处理 \(A \in \{0,1\}\)，单个低维代理变量 \(Z, W\)，无协变量 \(X\)。此时 [4] 的剂量反应函数退化为 \(E[Y(a)]\)，桥函数方程简化为 \(E[Y|A=a,W] = E[h(W)|A=a,W]\)，效率界可通过计算有效影响函数 (EIF) 得到。对于 [1] 的 DCEE，考虑两个时间点 (\(T=2\))，处理 \(A_1, A_2\)，远端结果 \(Y\)，无时变混杂。此时 DCEE 退化为标准 ATE 的推广，其效率界未知。在这个特例下，要证的命题是：DCEE 的 EIF 方差是否等于 [1] 中给出的渐近方差表达式。

- **证据**：
  - [1] 开放问题 1：“DCEE 的半参数效率界：本文两个估计器都是 \(\sqrt{n}\)-一致且渐近正态的，但它们的渐近方差是否达到了半参数效率界？……这是一个明确的 open problem——参考 Cheng et al. (2023) 对 CEE 的效率界推导，对 DCEE 做类似分析将是一个直接且重要的后续工作。”
  - [4] 开放问题 1：“经验协方差估计的理论证明……但更根本的是，本文未推导剂量反应函数的半参数效率界。作者在正文中未提及效率界，仅在补充材料中声称是 RAL 估计量。”
  - [2] 开放问题 1：“半参效率界问题：作者称在补充材料中展示了 \(\hat{\tau}_{CV}\) 是某个半参模型下的 RAL 估计量，但正文未给出该半参模型的效率界，也未证明 \(\hat{\tau}_{CV}\) 能达到该效率界。”

- **为什么现在**：[1] 和 [4] 分别于 2026 年 6 月和 8 月发表，明确指出了效率界的缺失。[2] 也提出了类似问题。同时，[1] 引用了 Cheng et al. (2023) 的 CEE 效率界作为模板，使得 DCEE 的效率界推导有直接路径。研究者武器库中的 minimax 下界技术可以直接应用于这些设定。

- **武器匹配**：使用**估计问题的 minimax 下界**方法，通过计算半参数模型的切空间和有效影响函数 (EIF)，得到效率界。具体地，对于 DCEE，利用 [1] 中给出的渐近方差表达式，验证其是否等于 EIF 的方差。对于 [4] 的剂量反应函数，利用其桥函数方程构造参数子模型，计算信息算子。

- **风险与竞争**：需要确认是否有其他团队正在做类似工作。建议检查 Cheng et al. (2023) 的作者组是否已发表 DCEE 效率界的工作。另外，[4] 的作者在 Remark 2 中提到了经验协方差的理论证明是开放问题，但效率界本身可能已被其他工作解决（如 Kennedy 2020 的框架）。需查阅 Kennedy (2020) 是否覆盖了近端设定。

- **交付形态**：`定理型`

- **第一周动作**：
  1. 读 [1] 的 Theorem 1 和渐近方差表达式，以及 Cheng et al. (2023) 的 CEE 效率界推导。
  2. 读 [4] 的 Section 3 和补充材料，理解其桥函数识别和估计量构造。
  3. 推导 DCEE 在 \(T=2\)、无协变量下的 EIF，计算其方差，与 [1] 的方差对比。
  4. 推导 [4] 中剂量反应函数在二元处理下的 EIF，验证是否与现有 ATE 的 EIF 一致。
  5. 搜索 Cheng et al. (2023) 和 Kennedy (2020) 的最新引用，确认是否有后续工作。

### 提案 2：Higher-Order Influence Functions for Robust Debiased Machine Learning under Slow Nuisance Convergence

- **claim（一句话）**：构造一个基于高阶影响函数 (HOIF) 的去偏机器学习估计量，使得当一阶 nuisance 估计量收敛率慢于 \(n^{-1/4}\) 时，仍能实现 \(\sqrt{n}\) 一致估计和有效推断。

- **最小内核**：考虑最简单的设定：单个连续处理变量 \(A\)，结果 \(Y\)，协变量 \(X\)，目标参数为平均处理效应 (ATE)。假设倾向性得分 \(\pi(A|X)\) 和结果回归 \(\mu(A,X)\) 的估计量收敛率均为 \(n^{-1/3}\)（慢于 \(n^{-1/4}\)）。此时一阶 DML 失效。HOIF 通过引入二阶影响函数项来吸收二阶偏差。在这个特例下，需要推导二阶影响函数的显式表达式，并证明其偏差项为三个误差的乘积（如 [12] Theorem 1 的结构），从而在更慢收敛率下仍可控制。

- **证据**：
  - [17] 开放问题 4：“当 \(R(\hat{\gamma}_l)\) 和 \(R(\hat{\alpha}_l)\) 均慢于 \(n^{-1/4}\) 时，本文的二阶偏差控制失效，而 HOIF 正是处理此情形的理论。本文 intro 完全未提及 HOIF，这是一个理论缺口。”
  - [25] 开放问题 1：“是否可用 HOIF 构造更高阶的 DR 矩，将吸收条件放宽至 \(\|\hat{\pi}-\pi\|=o_p(n^{-1/4})\) 甚至更弱？”
  - [27] 开放问题 3：“若 nuisance 收敛更慢（如 \(J^{-1/3}\)），能否引入一阶或更高阶 HOIF 来修正偏差，达到 \(J^{-1/2}\) 收敛？”

- **为什么现在**：[17] 给出了有限样本 DML 定理，但明确承认了 HOIF 的缺失；[25] 和 [27] 分别从连续处理和中介分析角度提出了 HOIF 的需求。同时，研究者武器库中的高阶 U 统计量计算（einsum/treewidth）使得 HOIF 的显式表达式可以高效计算，这在以前是计算瓶颈。

- **武器匹配**：使用**高阶 U 统计量的计算（treewidth / tensor contraction / einsum）**，将 HOIF 的期望项表示为张量网络，通过 einsum 实现 \(O(n^{\text{treewidth}})\) 的计算复杂度，避免指数级展开。具体地，对于 ATE 的二阶影响函数，其期望涉及三个 nuisance 函数的乘积积分，可转化为一个三阶张量收缩。

- **风险与竞争**：需要确认 HOIF 在非参数设定下的理论是否已被 Robins et al. (2008) 或 Liu et al. (2017) 等解决。需查阅 Robins (2004) 关于高阶影响函数的系列工作，以及 van der Laan (2014) 的 TMLE 高阶扩展。如果已有完整理论，则选题被抢先。另外，HOIF 的方差可能发散，需要检查二阶影响函数的方差是否有限。

- **交付形态**：`方法+模拟型`

- **第一周动作**：
  1. 读 [17] 的 Theorem 1 和假设 1，明确一阶 DML 的偏差结构。
  2. 读 [25] 的 Section 2，理解连续处理下 DR 矩的构造。
  3. 推导 ATE 设定下二阶影响函数的 U 统计量表达式（参考 Robins et al. 2008 的公式）。
  4. 用 einsum 实现 \(n=500\) 模拟中二阶影响函数的计算，对比一阶 DML 在慢 nuisance 下的表现。
  5. 检查 [27] 中关于 CRT 中介的 HOIF 加速是否与 ATE 设定兼容。

### 提案 3：High-Dimensional Bridge Function Estimation for Proximal Causal Inference via Regularized Spectral Methods

- **claim（一句话）**：提出一种基于谱正则化（Tikhonov 或谱截断）的桥函数估计方法，适用于高维代理变量（\(Z, W\) 维度远大于样本量），并证明其收敛率以及用于下游因果效应估计时的 \(\sqrt{n}\) 推断条件。

- **最小内核**：考虑最简单的设定：二元处理 \(A\)，结果 \(Y\)，代理变量 \(Z\) 和 \(W\) 均为高维（\(d \gg n\)），但假设桥函数 \(h(W)\) 是稀疏的（只有少数 \(W\) 分量相关）或具有低维结构（如加法模型）。此时，Fredholm 积分方程 \(E[Y|A=a,W] = E[h(W)|A=a,W]\) 在高维下是严重不适定的。特例：假设 \(W\) 的每个分量独立，且 \(h(W) = \beta^T W\)（线性），则问题退化为高维线性 IV，可用 Lasso 等。但更一般的非参数设定下，需要谱方法。

- **证据**：
  - [4] 开放问题 2：“高维代理变量下的桥函数估计：本文的桥函数估计（GMM, 指数校准）是针对低维代理变量的。当 \(Z\) 和 \(W\) 的维度很高，甚至大于样本量时，如何有效地估计桥函数 \(h\) 和 \(q\)，并使其满足本文所需的 \(L_2\) 收敛率条件？”
  - [16] 开放问题：“高维代理变量下桥函数估计的最优数值算法设计。”
  - [3] 开放问题 4：“桥函数估计的计算复杂度：本文使用最小最大学习估计桥函数，但未讨论其计算复杂度。对于高维 \(Z\) 和 \(W\)，求解 min-max 优化问题的计算成本可能很高。”

- **为什么现在**：[4] 和 [16] 都是 2026 年发表的最新工作，明确指出了高维桥函数估计的缺失。同时，研究者武器库中的“带随机噪声的反问题”和“高维渐近”可以直接应用于此。此外，[3] 中使用的 minimax 学习框架在高维下计算昂贵，而谱方法（如核方法结合随机特征）可能更高效。

- **武器匹配**：使用**带随机噪声的反问题**理论，将桥函数估计视为一个线性逆问题，并利用谱截断或 Tikhonov 正则化。结合**高维渐近**，推导在代理变量维度发散时估计量的收敛率。同时，利用**高阶 U 统计量的计算**中的 einsum 技巧，实现核矩阵的特征分解（如 Nyström 近似）以降低计算复杂度。

- **风险与竞争**：需要确认是否存在已有的高维桥函数估计工作，如 Singh et al. (2024) 或 Xu et al. (2025)。另外，谱方法在非参数逆问题中的收敛率依赖于源条件和 ill-posedness 程度，在高维下可能更差。需要检查是否已有反例表明高维桥函数估计不可行。

- **交付形态**：`方法+模拟型`

- **第一周动作**：
  1. 读 [4] 的 Section 3.2 和 3.3，理解其 GMM 和指数校准方法。
  2. 读 [16] 的桥函数识别部分，明确积分方程形式。
  3. 推导线性桥函数（\(h(W)=\beta^T W\)）在高维下的 Lasso 估计理论，作为基准。
  4. 实现一个基于核谱截断的桥函数估计器，在 \(d=50, n=200\) 的模拟中测试性能。
  5. 搜索“high-dimensional bridge function”或“proximal causal inference high-dimensional”看是否有预印本。

---

### 本页的证据论文

- [1] ★ [Distal causal excursion effects: modeling long-term effects of time-varying treatments in micro-randomized trials](/research-news/deep_reads/2026-06-19-10.1093_biomtc_ujaf134/) — Biometrics · 2026-06-19
- [2] ★ [Flexible and efficient estimation of causal effects with error-prone exposures: a control variates approach for measurement error](/research-news/deep_reads/2026-06-19-10.1093_biomtc_ujaf151/) — Biometrics · 2026-06-19
- [3] ★ [Proximal Mediation Analysis with Unmeasured Treatment-Induced Confounding](/research-news/deep_reads/2026-07-07-2607.02901/) — 2026-07-07
- [4] ★ [Debiased inference for proximal dose-response function](/research-news/deep_reads/2026-08-05-2608.00404/) — 2026-08-05
- [5] ★ [Causal Inference for Functional Treatments with Stochastic Policies](/research-news/deep_reads/2026-06-25-2606.27518/) — 2026-06-25
- [6] ★ [An Instrumental Variable Approach to Account for Informative Treatment Switching in Real-world Evidence](/research-news/deep_reads/2026-07-03-2607.00980/) — 2026-07-03
- [7] ★ [Outcome-adapted Automatic Debiased Machine Learning](/research-news/deep_reads/2026-07-07-2607.03351/) — 2026-07-07
- [8] ★ [Marginal Causal Effect Estimation with Continuous Instrumental Variables](/research-news/deep_reads/2026-07-10-2510.14368/) — 2026-07-10
- [9] ★ [A statistical test for the benefits of personalizing interventions](/research-news/deep_reads/2026-08-01-10.1126_science.aeb9506/) — Science · 2026-08-01
- [10] ★ [Towards a Unified Theory for Semiparametric Data Fusion with Individual-Level Data](/research-news/deep_reads/2026-09-01-2409.09973/) — 2026-09-01
- [11] ★ [A kernelization-based approach to nonparametric binary choice models](/research-news/deep_reads/2026-06-07-10.1016_j.jeconom.2026.106264/) — Journal of Econometrics · 2026-06-07
- [12] ★ [Private Rate-Double-Robust Inference](/research-news/deep_reads/2026-06-22-2606.20427/) — 2026-06-22
- [13] ★ [Causal mediation analysis for stochastic interventions](/research-news/deep_reads/2026-08-31-1901.02776/) — 2026-08-31
- [14] ★ [Semi-nonparametric models of multidimensional matching: An optimal transport approach](/research-news/deep_reads/2026-06-07-10.1016_j.jeconom.2026.106242/) — Journal of Econometrics · 2026-06-07
- [15] ★ [Localized Debiased Machine Learning: Efficient Inference on Quantile Treatment Effects and Beyond](/research-news/deep_reads/2026-07-14-1912.12945/) — 2026-07-14
- [16] [Proximal Path-Specific Inference](/research-news/deep_reads/2026-05-12-2605.09462/) — 2026-05-12
- [17] [A simple and general debiased machine learning theorem with finite-sample guarantees](/research-news/deep_reads/2026-06-20-10.1093_biomet_asac033/) — Biometrika · 2026-06-20
- [18] [Nonparametric inference for sublevel-set probabilities of conditional average treatment effect functions](/research-news/deep_reads/2026-05-18-2605.15373/) — 2026-05-18
- [19] [Double/Debiased Machine Learning for Continuous Treatment Effects in Panel Data with Endogeneity](/research-news/deep_reads/2026-05-19-2605.17910/) — 2026-05-19
- [20] [Average partial effect estimation using double machine learning](/research-news/deep_reads/2026-05-26-10.1214_25-aos2563/) — Annals of Statistics · 2026-05-26
- [21] [Doubly Robust Pointwise Confidence Intervals for a Monotonic Continuous Treatment Effect Curve](/research-news/deep_reads/2026-05-26-10.1080_01621459.2026.2639735/) — Journal of the American Statistical Association · 2026-05-26
- [22] [Identification and multiply robust estimation in causal mediation analysis across principal strata](/research-news/deep_reads/2026-05-26-10.1093_jrsssb_qkaf037/) — Journal of the Royal Statistical Society Series B · 2026-05-26
- [23] [Semiparametric Inference for Causal Effects on Functional Outcomes](/research-news/deep_reads/2026-05-27-2605.26964/) — 2026-05-27
- [24] [Design-based edge-level causal inference with machine learning assisted covariate adjustment](/research-news/deep_reads/2026-06-02-2606.00965/) — 2026-06-02
- [25] [Double Debiased Machine Learning Nonparametric Inference with Continuous Treatments](/research-news/deep_reads/2026-06-07-10.1080_07350015.2025.2505487/) — Journal of Business & Economic Statistics · 2026-06-07
- [26] [Sharp Bounds and Inference in Sample Selection Models with Treatment Endogeneity](/research-news/deep_reads/2026-06-09-2606.09223/) — 2026-06-09
- [27] [Semiparametric causal mediation analysis of cluster-randomized trials for indirect and spillover effects](/research-news/deep_reads/2026-06-10-10.1093_biomtc_ujag017/) — Biometrics · 2026-06-10
- [28] [HSCI: Neyman-Orthogonal Causal Inference under High-Dimensional Proportional Hazards](/research-news/deep_reads/2026-06-12-2606.14132/) — 2026-06-12
- [29] [Semiparametric Local Projections](/research-news/deep_reads/2026-06-13-2606.13519/) — 2026-06-13
- [30] [Bias-Aware External-Model-Assisted Inference in High-Dimensional Regression](/research-news/deep_reads/2026-06-17-2606.15602/) — 2026-06-17

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

