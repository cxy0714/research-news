# 选题提案 · 条件独立性检验与因果推断

**战线范围**: 检验条件独立性或处理效应异质性，利用条件随机化检验、双稳健得分、影响函数、交叉拟合等方法。  
**证据论文**: 30 篇（★ 收藏 6 篇）  
**提案条数**: 2  
**生成日期**: 2026-09-01  

> 每条提案的证据都点名来源论文 [k] 并引其原话。**不打分、不排名**——「证据 N 篇」是可数的事实，不是质量分。标了 ⚠️ 单点证据的条目只有一篇论文支撑，自己掂量。

---

### 提案 1：Higher-Order Influence Function Correction for Riesz Representer Estimation Under Slow Nuisance Convergence

- **claim（一句话）**：构造一个基于二阶影响函数的去偏估计量，用于任意线性泛函（如 ATE、ATT）的 Riesz representer 估计，使得当 nuisance 函数的 \(L_2\) 收敛率慢至 \(n^{-1/3}\) 时，估计量仍达到 \(\sqrt{n}\)-一致且渐近正态，并给出有限样本 Berry-Esseen 界。

- **最小内核**：考虑最简单的线性泛函 \(\theta = E[m(Z; \gamma_0)]\)，其中 \(\gamma_0\) 是条件均值函数，Riesz representer \(\alpha_0\) 满足 \(E[m(Z; \gamma)] = E[\alpha_0(Z) \cdot \gamma(Z)]\)。在 \(d=1\) 的设定下（单个连续协变量），假设 \(\gamma_0\) 和 \(\alpha_0\) 均属于 Sobolev 球 \(S(s, L)\) 且光滑参数 \(s < d/4\)（导致收敛率慢于 \(n^{-1/4}\)）。此时一阶去偏失效，需要二阶影响函数修正。最小内核要证的命题是：当 \(\hat{\gamma}\) 和 \(\hat{\alpha}\) 的 \(L_2\) 误差均为 \(O_p(n^{-1/3})\) 时，二阶修正后的估计量 \(\hat{\theta} = \frac{1}{n}\sum_i m(Z_i; \hat{\gamma}) + \frac{1}{n}\sum_i \hat{\alpha}(Z_i)(Y_i - \hat{\gamma}(Z_i)) + \text{二阶项}\) 的偏差为 \(o_p(n^{-1/2})\)，且渐近方差等于半参数效率界。

- **证据**：
  - [7] 开放问题 4：“当 \(R(\hat{\gamma}_l)\) 和 \(R(\hat{\alpha}_l)\) 均慢于 \(n^{-1/4}\) 时，本文的二阶偏差控制失效，而 HOIF 正是处理此情形的理论。本文 intro 完全未提及 HOIF，这是一个理论缺口。”
  - [11] 开放问题 3：“Higher-order Influence Functions (HOIF) 加速：本文要求 nuisance 收敛率 \(o(J^{-1/4})\)。若 nuisance 收敛更慢（如 \(J^{-1/3}\)），能否引入一阶或更高阶 HOIF 来修正偏差，达到 \(J^{-1/2}\) 收敛？”
  - [19] 开放问题 1：“HOIF 修正能否进一步放宽平滑性条件？本文修正只用到一阶影响函数，要求 DR 交叉速率 \(o_P(1/\sqrt{n})\)。频率派 HOIF 理论已证明：用高阶影响函数可将条件放宽到 \(\beta_m + \beta_\pi > d/2\)。”

- **为什么现在**：近期 [7] 给出了通用去偏定理的有限样本保证，但明确将 HOIF 列为未覆盖情形；[11] 和 [19] 在各自设定下独立指出 HOIF 是自然扩展。同时，高阶 U 统计量的计算工具（treewidth / einsum）已成熟，使得二阶影响函数的显式表达式可高效实现，而无需手动推导复杂积分。

- **武器匹配**：使用 **高阶 U 统计量的计算（treewidth / tensor contraction / einsum）** 来构造二阶影响函数项。具体地，二阶项涉及 \(\hat{\alpha}\) 和 \(\hat{\gamma}\) 的乘积的期望，可表示为 U 统计量 \(U_n = \frac{1}{n(n-1)}\sum_{i\neq j} \phi(Z_i, Z_j)\)，其方差和偏差可通过 tensor contraction 在 \(O(n^2)\) 内计算，并利用 treewidth 分解加速至近线性。

- **风险与竞争**：主要风险是二阶影响函数的显式表达式可能依赖于具体泛函，通用性受限。需检查 [7] 的 Riesz representer 框架下二阶项是否总能写成 U 统计量形式（理论上成立，但需验证）。竞争：Robins et al. (2008, 2017) 已有 HOIF 理论，但未给出可计算实现；需确认是否有近期工作（如 Liu et al. 2025）已将 HOIF 与 Riesz representer 结合。建议搜索 “higher-order influence function Riesz representer” 及检查 [7] 的后续引用。

- **交付形态**：`方法+模拟型`

- **第一周动作**：
  1. 精读 [7] 的定理 1 证明，提取二阶偏差的显式表达式（Section 2.2 的余项展开）。
  2. 推导在 \(d=1\)、\(\gamma_0\) 和 \(\alpha_0\) 为 Sobolev 光滑时，二阶影响函数的具体形式（参考 Robins et al. 2008 的公式 (4.2)）。
  3. 用 einsum 实现 \(n=500\) 下二阶 U 统计量的计算，并与一阶去偏估计量对比 MSE。
  4. 阅读 [11] 的 Theorem 4 速率条件，确认其 \(J^{-1/4}\) 要求与本文设定的一致性。
  5. 搜索 arXiv 近半年 “higher-order influence function” 相关论文，确认无重复。

### 提案 2：Higher-Order Debiased Estimation of Bridge Functions in Proximal Causal Inference

- **claim（一句话）**：构造一个基于二阶影响函数的去偏估计量，用于近端因果推断中的桥函数 \(h(W, a, X)\) 和 \(q(Z, a, X)\) 的泛函（如剂量-反应函数 \(\theta(a)\)），使得当桥函数估计的 \(L_2\) 收敛率慢于 \(n^{-1/4}\)（例如 \(n^{-1/3}\)）时，估计量仍达到 \(\sqrt{n}\)-一致且渐近正态，并给出均匀置信带。

- **最小内核**：考虑连续处理 \(A\) 下的剂量-反应函数 \(\theta(a) = E[Y(a)]\)，在近端框架下可识别为 \(\theta(a) = E[h(W, a, X)]\)，其中 \(h\) 满足桥方程 \(E[Y - h(W, a, X) \mid Z, A=a, X] = 0\)。最小内核设定：\(X\) 为单变量，\(A\) 为二值（简化），\(Z\) 和 \(W\) 均为低维连续变量。假设桥函数 \(h\) 的估计 \(\hat{h}\) 来自 RKHS 且收敛率 \(O_p(n^{-1/3})\)（因 ill-posedness）。此时一阶去偏（如 [3] 的 Theorem 3）因 \(n^{-1/4}\) 条件不满足而失效。要证的命题：二阶修正后的估计量 \(\hat{\theta}(a) = \frac{1}{n}\sum_i \hat{h}(W_i, a, X_i) + \frac{1}{n}\sum_i \hat{q}(Z_i, a, X_i)(Y_i - \hat{h}(W_i, a, X_i)) + \text{二阶项}\) 的偏差为 \(o_p(n^{-1/2})\)，且渐近方差等于半参数效率界。

- **证据**：
  - [2] 结论比证明窄的地方：“Theorem 5 的收敛率条件 (iii) 要求第二阶项以 \(o_p(n^{-1/2})\) 收敛。作者声称‘当所有估计量以快于 \(n^{-1/4}\) 的速率收敛时，这个条件可满足’。但桥函数 \(h_a\) 和 \(q_a\) 的收敛率取决于积分方程 (3) 和 (4) 的 ill-posedness 程度，可能远慢于 \(n^{-1/4}\)。”
  - [3] 开放问题 2：“当 \(Z\) 和 \(W\) 的维度很高，甚至大于样本量时，如何有效地估计桥函数 \(h\) 和 \(q\)，并使其满足本文所需的 \(L_2\) 收敛率条件？”（该问题直接指出桥函数估计的收敛率条件可能不满足，与 [2] 的 gap 一致。）
  - [7] 开放问题 4 和 [11] 开放问题 3 也支持 HOIF 作为解决慢收敛的通用工具（见提案 1 证据），此处具体应用于桥函数。

- **为什么现在**：[2] 和 [3] 分别于 2026 年 7 月和 8 月发表，均将桥函数估计的收敛率条件视为关键瓶颈，但未提供解决方案。同时，[7] 的通用去偏定理和 [11] 的 HOIF 加速需求为二阶修正提供了理论动机。高阶 U 统计量的计算工具（einsum）可高效实现桥函数泛函的二阶项，因为桥方程本质上是 Fredholm 积分方程，其二阶影响函数可表示为 U 统计量。

- **武器匹配**：使用 **高阶 U 统计量的计算（treewidth / tensor contraction / einsum）** 来构造二阶项。具体地，桥函数 \(h\) 的二阶影响函数涉及 \(\hat{h}\) 和 \(\hat{q}\) 的乘积的期望，可写成 U 统计量 \(U_n = \frac{1}{n(n-1)}\sum_{i\neq j} \psi(Z_i, W_j, a, X_i, X_j)\)，其计算可通过 einsum 在 \(O(n^2)\) 内完成，并利用 treewidth 分解处理高维 \(X\)。

- **风险与竞争**：主要风险是桥函数估计的 ill-posedness 可能导致二阶项本身收敛慢，需验证在 \(n^{-1/3}\) 率下二阶项仍为 \(o_p(n^{-1/2})\)。竞争：可能存在未发表的 HOIF 应用于近端推断的工作（如 Tchetgen Tchetgen 组）。建议搜索 “proximal causal inference higher-order influence function” 及检查 [2][3] 的后续引用。另外，需确认 [28] 的连续 U 影响函数构造是否可替代 HOIF。

- **交付形态**：`方法+模拟型`

- **第一周动作**：
  1. 精读 [2] 的 Theorem 5 证明，提取桥函数估计收敛率对二阶项的影响（Appendix B 的余项展开）。
  2. 推导在 \(A\) 二值、\(X\) 单变量下，桥函数 \(h\) 的二阶影响函数显式表达式（参考 [3] 的 EIF 推导 Section 3.2）。
  3. 用 einsum 实现 \(n=500\) 下二阶 U 统计量的计算，并在 [3] 的模拟设定（Scenario 1，桥函数正确指定但收敛慢）下对比一阶与二阶去偏的 MSE 和覆盖。
  4. 阅读 [28] 的 Section 4.4.2，确认连续 U 的影响函数构造是否与 HOIF 互补。
  5. 搜索 arXiv 近半年 “bridge function higher-order” 相关论文，确认无重复。

---

### 本页的证据论文

- [1] ★ [Semiparametric Efficiency of Residual Correlation Testing under Gaussian Additive Noise Models](/research-news/deep_reads/2026-06-02-2606.01011/) — 2026-06-02
- [2] ★ [Proximal Mediation Analysis with Unmeasured Treatment-Induced Confounding](/research-news/deep_reads/2026-07-07-2607.02901/) — 2026-07-07
- [3] ★ [Debiased inference for proximal dose-response function](/research-news/deep_reads/2026-08-05-2608.00404/) — 2026-08-05
- [4] ★ [Group-Level Treatment Effect Heterogeneity in Difference-in-Differences: A Balanced Approach](/research-news/deep_reads/2026-06-25-2606.24785/) — 2026-06-25
- [5] ★ [A statistical test for the benefits of personalizing interventions](/research-news/deep_reads/2026-08-01-10.1126_science.aeb9506/) — Science · 2026-08-01
- [6] ★ [Causal mediation analysis for stochastic interventions](/research-news/deep_reads/2026-08-31-1901.02776/) — 2026-08-31
- [7] [A simple and general debiased machine learning theorem with finite-sample guarantees](/research-news/deep_reads/2026-06-20-10.1093_biomet_asac033/) — Biometrika · 2026-06-20
- [8] [Nonparametric tests of treatment effect homogeneity for policy-makers](/research-news/deep_reads/2026-05-26-10.1080_01621459.2026.2670746/) — Journal of the American Statistical Association · 2026-05-26
- [9] [Semiparametric Inference for Causal Effects on Functional Outcomes](/research-news/deep_reads/2026-05-27-2605.26964/) — 2026-05-27
- [10] [Empirical stratification for treatment effect heterogeneity with post-treatment variables](/research-news/deep_reads/2026-06-10-2606.11013/) — 2026-06-10
- [11] [Semiparametric causal mediation analysis of cluster-randomized trials for indirect and spillover effects](/research-news/deep_reads/2026-06-10-10.1093_biomtc_ujag017/) — Biometrics · 2026-06-10
- [12] [Double robust conditional independence test for novel biomarkers given established risk factors with survival data](/research-news/deep_reads/2026-06-19-10.1093_biomtc_ujaf133/) — Biometrics · 2026-06-19
- [13] [Estimating Effects of Longitudinal Modified Treatment Policies ( <scp>LMTPs</scp> ) on Rates of Change in Health Outcomes](/research-news/deep_reads/2026-06-19-10.1002_sim.70604/) — Statistics in Medicine · 2026-06-19
- [14] [Variable importance measures for heterogeneous treatment effects](/research-news/deep_reads/2026-06-19-10.1093_biomtc_ujaf140/) — Biometrics · 2026-06-19
- [15] [Efficient and multiply robust risk estimation under general forms of dataset shift](/research-news/deep_reads/2026-06-20-10.1214_24-aos2422/) — Annals of Statistics · 2026-06-20
- [16] [Nonparametric efficient estimation of marginal structural models with continuous time-varying treatments](/research-news/deep_reads/2026-06-20-10.1093_biomet_asag026/) — Biometrika · 2026-06-20
- [17] [Practical causal mediation analysis: extending nonparametric estimators to accommodate multiple mediators and multiple intermediate confounders](/research-news/deep_reads/2026-06-20-10.1093_biostatistics_kxae012/) — Biostatistics · 2026-06-20
- [18] [Semiparametric counterfactual density estimation](/research-news/deep_reads/2026-06-20-10.1093_biomet_asad017/) — Biometrika · 2026-06-20
- [19] [Double Robust Bayesian Inference on Average Treatment Effects](/research-news/deep_reads/2026-06-21-10.3982_ecta21442/) — Econometrica · 2026-06-21
- [20] [Efficient and Robust Estimation of the Generalized LATE Model](/research-news/deep_reads/2026-06-21-10.1080_07350015.2023.2282497/) — Journal of Business & Economic Statistics · 2026-06-21
- [21] [Constructing targeted minimum loss/maximum likelihood estimators: a simple illustration to build intuition](/research-news/deep_reads/2026-06-24-10.1093_aje_kwaf261/) — American Journal of Epidemiology · 2026-06-24
- [22] [Cross-Fitted Survey-Weighted TMLE with Design-Based Variance for Causal Machine Learning](/research-news/deep_reads/2026-06-30-2606.30918/) — 2026-06-30
- [23] [Causal inference on distribution functions](/research-news/deep_reads/2026-07-05-10.1093_jrsssb_qkad008/) — Journal of the Royal Statistical Society Series B · 2026-07-05
- [24] [Estimating heterogeneous treatment effects with right-censored data via causal survival forests](/research-news/deep_reads/2026-07-05-10.1093_jrsssb_qkac001/) — Journal of the Royal Statistical Society Series B · 2026-07-05
- [25] [A high-dimensional power analysis of the conditional randomization test and knockoffs](/research-news/deep_reads/2026-07-06-10.1093_biomet_asab052/) — Biometrika · 2026-07-06
- [26] [Fast and powerful conditional randomization testing via distillation](/research-news/deep_reads/2026-07-06-10.1093_biomet_asab039/) — Biometrika · 2026-07-06
- [27] [Nonparametric efficient causal mediation with intermediate confounders](/research-news/deep_reads/2026-07-06-10.1093_biomet_asaa085/) — Biometrika · 2026-07-06
- [28] [Proximal Identification and Estimation in Front-Door Causal Structures with Unobserved Confounding of the Mediator](/research-news/deep_reads/2026-07-15-2607.10515/) — 2026-07-15
- [29] [Targeted Deep Survival Contrasts: Valid Inference for Treatment-Specific Survival Benefit with Neural Networks](/research-news/deep_reads/2026-08-24-2608.20598/) — 2026-08-24
- [30] [Semiparametric localized principal stratification analysis with continuous strata](/research-news/deep_reads/2026-05-26-10.1093_jrsssb_qkaf034/) — Journal of the Royal Statistical Society Series B · 2026-05-26

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

