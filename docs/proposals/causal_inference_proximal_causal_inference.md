# 选题提案 · 近端因果推断/负对照变量

**战线范围**: 利用负对照暴露和负对照结果（negative control variables）作为代理变量，在存在未测量混杂时识别和估计因果效应（如直接效应、路径效应、剂量反应函数），核心数学对象为桥函数（bridge function）和影响函数。  
**证据论文**: 30 篇（★ 收藏 15 篇）  
**提案条数**: 3  
**生成日期**: 2026-09-01  

> 每条提案的证据都点名来源论文 [k] 并引其原话。**不打分、不排名**——「证据 N 篇」是可数的事实，不是质量分。标了 ⚠️ 单点证据的条目只有一篇论文支撑，自己掂量。

---

### 提案 1：Longitudinal Proximal Mediation with Time-Varying Treatments and Mediators: Identification and Efficient Estimation

- **claim（一句话）**：在存在未测量时变混杂和受处理影响的中介-结局混杂时，识别并半参数有效估计时变处理 \(A_t\) 通过时变中介 \(M_t\) 对结局 \(Y\) 的路径特定干预效应（interventional direct and indirect effects），并构造达到半参数效率界的去偏估计量。

- **最小内核**：两个时间点 \(t=1,2\)，每个时间点有二元处理 \(A_t\)、连续中介 \(M_t\)、未测量混杂 \(U_t\)，以及代理变量 \(Z_t, W_t\)（满足近端条件）。在此特例下，要证的命题退化为：在给定 \(X\) 和代理变量下，桥函数 \(h_t\) 满足 Fredholm 积分方程 \(E[Y \mid A_{1:2}, M_{1:2}, X, Z_{1:2}] = \int h_t(m_t, a_{1:2}, x, w_{1:2}) \, dF_{W_t|...}\)，且干预间接效应 \(\theta_{\text{IE}} = E[E[Y \mid A_1=a, M_1=m_1, ...] - ...]\) 可表示为嵌套桥函数的期望。

- **证据**：
  - [6] 在 Discussion 中明确将“纵向设定下的扩展”列为未来方向（Section 6 第一段：“Extending our approach to longitudinal settings with time-varying treatments, mediators, and unmeasured treatment-induced confounding is a natural next step”）。
  - [20] 在开放问题 3 中提出：“能否将本文的嵌套 bridge 识别公式推广到时变处理与时变中介的 g-formula？”（扎根于 Ying et al. 2021 的引用与本文 Section 5 的未来方向暗示）。
  - [17] 在开放问题中写道：“如何将此框架拓展至纵向数据或多重中介场景”（原文：“open question: how to extend this framework to longitudinal data or multiple mediators”）。

- **为什么现在**：近端因果推断在单时间点设定下的识别与估计理论已成熟（[6]、[8]、[20]），且纵向半参数效率理论（如 [10] 的嵌套马尔可夫模型）提供了处理时变约束的工具。特别是 [10] 的 Verma 约束刻画方法可被用于处理纵向近端模型中的跨时间点条件独立性，使从“单时间点”到“纵向”的推广在理论上可行。

- **武器匹配**：使用 **高阶 U 统计量的计算（treewidth / tensor contraction / einsum）** 来高效计算纵向桥函数积分方程的解。纵向设定下桥函数涉及多个时间点的积分，其计算可表示为张量网络收缩，利用 treewidth 分解可降低计算复杂度，使原本指数级复杂度的积分变为多项式时间可解。

- **风险与竞争**：
  - 已被做过？需检查近期预印本（如 arXiv 2025-2026 上 Cui et al. 或 Ying et al. 的纵向近端工作）。建议搜索“proximal causal inference longitudinal mediation”。
  - 假设太强：纵向近端需要每个时间点的代理变量满足完备性条件，且跨时间点无反馈（或需额外假设），可能过于理想。
  - 反例存在：若代理变量随时间退化（如测量误差累积），桥函数可能不存在或解不唯一。
  - 算不出来：张量网络收缩的 treewidth 可能随时间点数量指数增长，需验证在有限时间点（如 3-5）下是否可行。

- **交付形态**：`方法+模拟型`

- **第一周动作**：
  1. 读 [6] Section 6 和 [20] Section 5，精确摘录纵向扩展的开放问题表述。
  2. 读 [10] 的 Theorem 1 和 Remark 5，理解 Verma 约束如何转化为加权条件矩限制，评估其是否适用于纵向近端模型。
  3. 写出两个时间点下桥函数积分方程的显式形式，并尝试用 einsum 表示其张量收缩结构。
  4. 在简单 DGP（线性结构、高斯噪声、两个时间点）下编写模拟代码，测试桥函数估计的有限样本性能（n=500, 1000）。

### 提案 2：Higher-Order Influence Functions for Proximal Causal Inference: Relaxing the \(n^{-1/4}\) Rate Condition

- **claim（一句话）**：针对近端因果推断中桥函数估计的 ill-posedness 导致收敛速率慢于 \(n^{-1/4}\) 的问题，构造基于二阶影响函数（HOIF）的偏差修正估计量，使得在 nuisance 估计仅以 \(n^{-1/3}\) 速率收敛时仍能达到 \(\sqrt{n}\)-一致性和渐近正态性。

- **最小内核**：单时间点、连续处理 \(A\)、连续代理变量 \(Z, W\)（均为标量），桥函数 \(h\) 满足 \(E[Y \mid A, X, Z] = \int h(w, a, x) \, dF_{W|A,X,Z}\)。在此特例下，要证的命题退化为：当 \(h\) 的估计量 \(\hat{h}\) 以 \(n^{-1/3}\) 收敛时，一阶影响函数修正后的估计量偏差为 \(O_p(n^{-2/3})\)，而二阶影响函数修正可将偏差降至 \(O_p(n^{-1})\)，从而允许 \(\sqrt{n}\) 推断。

- **证据**：
  - [4] 在 Section 9 结论中明确将高阶影响函数标记为当前框架之外：“Exploring these extensions would require a richer geometric framework and lies beyond the scope of this tutorial”（扎根于论文最后一句）。
  - [29] 在开放问题 3 中提出：“若 nuisance 收敛更慢（如 \(J^{-1/3}\)），能否引入一阶或更高阶 HOIF 来修正偏差，达到 \(J^{-1/2}\) 收敛？”（扎根于 Theorem 4 的速率条件与半参数效率界证明）。
  - [26] 在开放问题 4 中提出：“若 nuisance 收敛极慢（如 \(n^{-1/4}\) 也不满足乘积条件），能否用 HOIF 构造更高阶的偏差修正？”（扎根于本文定理 3 的 rate robustness 边界）。

- **为什么现在**：近端因果推断中桥函数估计是 ill-posed 逆问题，其收敛速率常慢于 \(n^{-1/4}\)（如 [8] 的模拟中桥函数估计使用 RKHS，但未提供理论保证）。同时，HOIF 理论在 [4] 中被系统介绍，且近期有计算 HOIF 的算法进展（如 Waterman & Lindsay, 1996; van der Vaart, 2014），使得将 HOIF 应用于近端设定成为可行。

- **武器匹配**：使用 **HOIF（高阶影响函数）**（moderately_familiar）来推导二阶影响函数的显式形式。具体地，对于近端剂量-反应函数 \(\theta(a) = E[h(W, a, X)]\)，其一阶影响函数已知（[8] Theorem 1），二阶影响函数可通过求解一个线性积分方程得到，该方程涉及桥函数估计的偏差的 Fréchet 导数。

- **风险与竞争**：
  - 已被做过？需检查 Robins et al. (2017) 或 Liu et al. (2021) 是否已将 HOIF 用于近端推断。建议搜索“higher-order influence function proximal causal inference”。
  - 假设太强：HOIF 要求 nuisance 估计的收敛速率已知且可分解为乘积形式，这在非参数设定下可能难以验证。
  - 反例存在：若桥函数估计的偏差不是平滑的（如存在跳跃），二阶展开可能失效。
  - 算不出来：二阶影响函数的计算涉及高阶矩和积分，可能计算成本高，需借助张量网络加速。

- **交付形态**：`定理型`

- **第一周动作**：
  1. 读 [4] Section 9 和 [8] Theorem 1，精确理解一阶影响函数的形式和 HOIF 的几何意义。
  2. 推导在标量 \(Z, W\) 设定下，\(\theta(a)\) 的二阶影响函数表达式（利用 [4] 的投影方法）。
  3. 读 [29] 的 Theorem 4 和 [26] 的 Theorem 3，摘录其速率条件，并对比 HOIF 修正后的条件。
  4. 在简单 DGP（线性桥函数、高斯噪声）下，用数值实验验证一阶和二阶修正的偏差缩减效果（n=200, 500, 1000）。

### 提案 3：Diagnosing Bridge Function Misspecification in Proximal Causal Inference: A Specification Test

- **claim（一句话）**：针对近端因果推断中桥函数模型误设导致估计失效的问题，构造一个基于过度识别限制的检验统计量，用于检测桥函数 \(h\) 或 \(q\) 是否被严重误设，并给出检验的渐近分布和局部功效。

- **最小内核**：单时间点、二元处理 \(A\)、连续结局 \(Y\)、低维代理变量 \(Z, W\)（均为标量）。桥函数 \(h\) 被参数化为线性形式 \(h(w, a, x; \beta) = \beta_0 + \beta_1 w + \beta_2 a + \beta_3 x\)。在此特例下，要证的命题退化为：若模型正确，则存在 \(\beta\) 使得 \(E[Y - h(W, A, X; \beta) \mid A, X, Z] = 0\) 几乎处处成立；若模型误设，则对任意 \(\beta\)，该条件期望非零。检验统计量基于样本矩 \(n^{-1/2} \sum_i (Y_i - h(W_i, A_i, X_i; \hat{\beta})) \cdot \phi(Z_i, A_i, X_i)\) 的二次型，其中 \(\phi\) 是工具函数。

- **证据**：
  - [8] 在开放问题 3 中提出：“能否开发一个检验统计量或诊断工具，来检测 \(h\) 或 \(q\) 的模型是否被严重误设？”（扎根于模拟中的 Scenario MM 导致估计和推断完全失效）。
  - [6] 在开放问题 3 中提出：“代理变量的选择依赖于主观判断，当 Assumption 4 被违反时，偏差有多大？需要开发敏感性分析方法。”（扎根于 Section 6 第三段）。
  - [20] 在开放问题 2 中提出：“由于完备性在中介设定下比 ATE 更难验证，一个自然的延伸是：量化秩条件偏离时 NDE/NIE 的最大偏移”（扎根于本文对 completeness 的强依赖与 Imai et al. 2010 的敏感性分析传统）。

- **为什么现在**：近端因果推断的模拟研究（如 [8] 的 Scenario MM）已明确展示桥函数误设会导致完全失效，但现有文献缺乏系统性的诊断工具。同时，条件矩限制的 specification test 在计量经济学中已有成熟理论（如 Newey, 1985; Bierens, 1990），可被直接移植到近端设定。

- **武器匹配**：使用 **非参数统计**（very_familiar）中的条件矩检验理论。具体地，将桥函数方程视为条件矩限制 \(E[\psi(O; h) \mid A, X, Z] = 0\)，构造基于核函数或级数基的检验统计量，并推导其渐近分布（如卡方分布或高斯过程极限）。

- **风险与竞争**：
  - 已被做过？需检查计量经济学中“近端 IV 的过度识别检验”相关文献（如 Belloni et al., 2012; Chen & Pouzo, 2012）。可能已有类似工作，但针对近端因果推断的桥函数误设检验尚未出现。
  - 假设太强：检验需要工具函数 \(\phi\) 的选择，不同选择可能导致不同功效，需提供数据驱动选择准则。
  - 反例存在：若桥函数误设但条件矩限制仍近似成立（如局部误设），检验可能缺乏功效。
  - 算不出来：检验统计量的临界值可能依赖 bootstrap，计算成本高。

- **交付形态**：`方法+模拟型`

- **第一周动作**：
  1. 读 [8] 的模拟部分（Scenario MM），精确记录桥函数误设导致估计失效的数值表现。
  2. 读 Newey (1985) 或 Bierens (1990) 关于条件矩检验的经典论文，摘录检验统计量的构造和渐近分布。
  3. 在 [8] 的模拟 DGP 基础上，实现一个基于核函数的条件矩检验，并评估其在正确模型和误设模型下的 size 和 power（n=500, 1000）。
  4. 写一个简短的模拟报告，对比不同工具函数 \(\phi\) 的选择对检验功效的影响。

---

### 本页的证据论文

- [1] ★ [Principal stratification with continuous post-treatment variables: nonparametric identification and semiparametric estimation](/research-news/deep_reads/2026-05-26-10.1093_jrsssb_qkaf049/) — Journal of the Royal Statistical Society Series B · 2026-05-26
- [2] ★ [Semiparametric Efficiency of Residual Correlation Testing under Gaussian Additive Noise Models](/research-news/deep_reads/2026-06-02-2606.01011/) — 2026-06-02
- [3] ★ [Multiply robust matching estimators of average and quantile treatment effects](/research-news/deep_reads/2026-06-23-10.1111_sjos.12585/) — Scandinavian Journal of Statistics · 2026-06-23
- [4] ★ [Semiparametric Efficiency Theory as Differential Calculus on a Space of Probability Distributions](/research-news/deep_reads/2026-06-24-2606.22784/) — 2026-06-24
- [5] ★ [Doubly robust estimation and sensitivity analysis for marginal structural quantile models](/research-news/deep_reads/2026-07-03-10.1093_biomtc_ujae045/) — Biometrics · 2026-07-03
- [6] ★ [Proximal Mediation Analysis with Unmeasured Treatment-Induced Confounding](/research-news/deep_reads/2026-07-07-2607.02901/) — 2026-07-07
- [7] ★ [Structural mean models for instrumented difference-in-differences](/research-news/deep_reads/2026-07-15-10.1214_24-ejs2313/) — Electronic Journal of Statistics · 2026-07-15
- [8] ★ [Debiased inference for proximal dose-response function](/research-news/deep_reads/2026-08-05-2608.00404/) — 2026-08-05
- [9] ★ [COMPACT: Spectral Adjustment Scores from a Complete and Irreducible Causal Criterion](/research-news/deep_reads/2026-08-13-2608.10305/) — 2026-08-13
- [10] ★ [Toward a Semiparametric Efficiency Theory under Equality Constraints in Nested Markov Models](/research-news/deep_reads/2026-08-28-2608.24602/) — 2026-08-28
- [11] ★ [Identification, Estimation, and Inference for Sequential Causally Ordered Mediation Pathways](/research-news/deep_reads/2026-06-03-2606.02833/) — 2026-06-03
- [12] ★ [A statistical test for the benefits of personalizing interventions](/research-news/deep_reads/2026-08-01-10.1126_science.aeb9506/) — Science · 2026-08-01
- [13] ★ [Incremental effects for continuous exposures](/research-news/deep_reads/2026-08-31-2409.11967/) — 2026-08-31
- [14] ★ [Towards a Unified Theory for Semiparametric Data Fusion with Individual-Level Data](/research-news/deep_reads/2026-09-01-2409.09973/) — 2026-09-01
- [15] ★ [Causal mediation analysis for stochastic interventions](/research-news/deep_reads/2026-08-31-1901.02776/) — 2026-08-31
- [16] [Proximal Causal Inference for Hidden Outcomes](/research-news/deep_reads/2026-05-12-2605.09849/) — 2026-05-12
- [17] [Proximal Path-Specific Inference](/research-news/deep_reads/2026-05-12-2605.09462/) — 2026-05-12
- [18] [Regularity, Phase Transitions, and Uniform Inference for Proximal Counterfactual Quantile Processes](/research-news/deep_reads/2026-05-12-2605.09257/) — 2026-05-12
- [19] [Doubly robust nonparametric instrumental variable estimators for survival outcomes](/research-news/deep_reads/2026-06-20-10.1093_biostatistics_kxab036/) — Biostatistics · 2026-06-20
- [20] [Proximal mediation analysis](/research-news/deep_reads/2026-06-20-10.1093_biomet_asad015/) — Biometrika · 2026-06-20
- [21] [Improving the Efficiency of Subgroup Analysis in Randomized Controlled Trials with TMLE](/research-news/deep_reads/2026-05-18-2605.15483/) — 2026-05-18
- [22] [Targeted maximum likelihood estimation of vaccine effectiveness and immune correlates in test-negative design studies with missing data](/research-news/deep_reads/2026-05-22-2605.21793/) — 2026-05-22
- [23] [Identification and multiply robust estimation in causal mediation analysis across principal strata](/research-news/deep_reads/2026-05-26-10.1093_jrsssb_qkaf037/) — Journal of the Royal Statistical Society Series B · 2026-05-26
- [24] [Semiparametric Inference for Causal Effects on Functional Outcomes](/research-news/deep_reads/2026-05-27-2605.26964/) — 2026-05-27
- [25] [Local Sensitivity Under Transport Restrictions](/research-news/deep_reads/2026-06-04-2606.04276/) — 2026-06-04
- [26] [Causal inference targeting a concentration index for studies of health inequalities](/research-news/deep_reads/2026-06-10-10.1093_biomtc_ujag082/) — Biometrics · 2026-06-10
- [27] [Empirical stratification for treatment effect heterogeneity with post-treatment variables](/research-news/deep_reads/2026-06-10-2606.11013/) — 2026-06-10
- [28] [Multiply robust estimation for causal survival analysis with treatment noncompliance](/research-news/deep_reads/2026-06-10-10.1214_25-aoas2117/) — Annals of Applied Statistics · 2026-06-10
- [29] [Semiparametric causal mediation analysis of cluster-randomized trials for indirect and spillover effects](/research-news/deep_reads/2026-06-10-10.1093_biomtc_ujag017/) — Biometrics · 2026-06-10
- [30] [Targeted maximum likelihood estimation for mediation analysis with multiple time-varying mediators](/research-news/deep_reads/2026-06-10-10.1093_biomtc_ujag102/) — Biometrics · 2026-06-10

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

