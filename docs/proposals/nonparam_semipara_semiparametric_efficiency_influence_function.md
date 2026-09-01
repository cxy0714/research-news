# 选题提案 · 半参数效率与影响函数

**战线范围**: 推导半参数模型的效率界、有效影响函数、有效得分函数，并构造渐近正态/半参数BvM的估计量，涉及部分线性模型、分位数回归、逆问题等。  
**证据论文**: 30 篇（★ 收藏 10 篇）  
**提案条数**: 2  
**生成日期**: 2026-09-01  

> 每条提案的证据都点名来源论文 [k] 并引其原话。**不打分、不排名**——「证据 N 篇」是可数的事实，不是质量分。标了 ⚠️ 单点证据的条目只有一篇论文支撑，自己掂量。

---

### 提案 1：Higher-Order Influence Functions for Doubly Robust Estimation under Slow Nuisance Convergence

- **claim（一句话）**：构造 k 阶影响函数（HOIF）修正项，使得当 nuisance 函数的收敛速率慢于 \(n^{-1/4}\)（例如 \(n^{-1/3}\)）时，目标泛函的估计量仍达到 \(\sqrt{n}\)-一致渐近正态性与半参数效率界。
- **最小内核**：单时间点、二值处理 \(A \in \{0,1\}\)、连续结局 \(Y\)，nuisance 为倾向得分 \(\pi(X)\) 和条件均值 \(\mu(A,X)\)，假设两者均以 \(n^{-1/3}\) 速率收敛（例如通过高维 Lasso 或随机森林）。在此特例下，标准 DR 估计量的偏差为 \(O_p(n^{-2/3})\)，一阶 HOIF 将偏差降至 \(O_p(n^{-4/3})\)，从而 \(\sqrt{n}\) 收敛成立。
- **证据**：
  - [4] 开放问题 1：“当处理分配模型或结局分布模型用非参数方法估计时，收敛速率可能慢于 \(n^{-1/4}\)，此时双稳健性是否仍成立？”（扎根于 Web Appendix F 及定理 2 的 \(n^{-1/4}\) 条件）
  - [11] 开放问题 4：“高维 \(X_0\) 下 nuisance 估计的收敛速率保证：本文要求 nuisance 估计收敛速率 \(n^{-1/4}\)（定理 3），但在高维 \(X_0\) 下机器学习 nuisance 估计的收敛速率常未知或慢于 \(n^{-1/4}\)。”（扎根于定理 3 的条件 (C2)）
  - [15] 开放问题 4：“当前 EIF 给出了 \(\sqrt{n}\)-一致估计，若 nuisance 收敛极慢（如 \(n^{-1/4}\) 也不满足乘积条件），能否用 HOIF 构造更高阶的偏差修正？”（扎根于定理 3 的 rate robustness 边界）
  - [16] 开放问题 3：“本文要求 nuisance 收敛率 \(o(J^{-1/4})\)。若 nuisance 收敛更慢（如 \(J^{-1/3}\)），能否引入一阶或更高阶 HOIF 来修正偏差，达到 \(J^{-1/2}\) 收敛？”（扎根于定理 4 的速率条件）
  - [24] 开放问题 1：“能否构造一个不要求 \(o(n^{-1/4})\) 但仍保持 \(\sqrt{n}\) 率的 DR estimator？”（扎根于定理 2 后的技术条件）
- **为什么现在**：近期 [12] 的 resmoothing 方法通过位置-尺度模型简化了条件得分估计，但未解决慢收敛率下的偏差问题；[15] 和 [16] 明确将 HOIF 列为未来方向，且 [4]、[11]、[24] 独立指出了 \(n^{-1/4}\) 条件的脆弱性。同时，研究者武器库中的高阶 U 统计量计算（treewidth / tensor contraction / einsum）为显式构造 HOIF 提供了计算工具。
- **武器匹配**：用高阶 U 统计量的计算（treewidth / tensor contraction / einsum）将 HOIF 的 k 阶乘积项表示为张量缩并，从而高效实现偏差修正项的数值计算。具体地，将 EIF 的余项展开为 U 统计量之和，利用 einsum 自动推导各阶收缩路径。
- **风险与竞争**：Robins et al. (2008) 已提出高阶影响函数的一般理论，但主要针对完全参数模型；在非参数/半参数设定下，HOIF 的显式构造和有限样本表现尚未被系统研究。需查 Robins (2004)、van der Vaart (2014) 等是否已有类似结果。此外，当 nuisance 收敛极慢（如 \(n^{-1/6}\)）时，所需 HOIF 阶数可能过高导致计算爆炸，需在模拟中评估。
- **交付形态**：`方法+模拟型`
- **第一周动作**：
  1. 读 [4] 定理 2 的证明，提取标准 DR 估计量的二阶余项表达式。
  2. 读 [15] 定理 3 的 rate robustness 边界，明确 HOIF 需要修正的偏差阶数。
  3. 读 [16] 定理 4 的速率条件，确认 HOIF 在 CRT 设定下的适用性。
  4. 在最小内核设定下（\(n=500\)，\(\pi\) 和 \(\mu\) 以 \(n^{-1/3}\) 收敛），用 R 实现标准 DR 估计量，记录偏差和覆盖。
  5. 推导一阶 HOIF 的 U 统计量表达式（利用 einsum 表示），并在相同设定下模拟比较。

### 提案 2：Interventional Mediation Effects under Treatment-Induced Confounding: Identification and Semiparametric Estimation

- **claim（一句话）**：在存在受处理影响的中介-结局混杂（未观测 \(U\)）时，定义并识别干预直接效应（IDE）和干预间接效应（IIE），构造达到半参数效率界的双稳健估计量，且不依赖跨世界独立性假设。
- **最小内核**：单个中介 \(M\)、二值处理 \(A\)、连续结局 \(Y\)，存在未观测混杂 \(U\) 同时影响 \(M\) 和 \(Y\)（受处理混杂）。在此特例下，要证的是：干预间接效应 \(\psi_{\text{IIE}} = E[Y(1, M(1)) - Y(1, M(0))]\) 是可识别的，其 EIF 可显式写出，且估计量在倾向得分或结局模型之一正确时一致。
- **证据**：
  - [10] 开放问题 1：“受处理影响的中介-结局混杂：本文明确排除了这种情况。作者指出，点识别在此情况下‘通常不可能’，部分识别是活跃研究领域。”（扎根于 Remark 2 和 Section 7）
  - [16] 开放问题 2：“Interventional indirect effect 在 CRT 中的移植：Díaz et al. (2021) 用 interventional effect 绕过了跨世界联合分布的识别难题，无需 Copula 假设。能否在 CRT 溢出设定下定义 interventional spillover mediation effect，从而彻底避免 A5？”（扎根于作者引用 Díaz et al. (2021) 仅用于重参数化技巧，未讨论其 estimands 定义路线的替代性）
  - [23] 开放问题 1：“交叉世界独立假设（A3）的放宽或替代：作者在 intro 中指出 A3 是自然效应路线的必要假设且不可验证，但未提供在 A3 部分违反下的敏感度分析或识别界。”（扎根于 intro 中 “cross-world independence assumption... is untestable”）
- **为什么现在**：[5] 最近提出了近端中介分析处理处理诱导混杂，但只针对预处理混杂；[10] 提出了随机干预的中介分解，但排除了受处理混杂。结合 [5] 的代理变量思想和 [10] 的干预效应框架，现在有可能在受处理混杂下实现识别和有效估计。
- **武器匹配**：用因果推断中的估计理论（very_familiar）推导干预间接效应的 EIF，利用非参数统计中的 minimax 下界刻画部分识别边界。具体地，将受处理混杂 \(U\) 视为未观测变量，通过负对照变量（如代理变量）构造桥函数，再用双稳健估计量消除一阶偏差。
- **风险与竞争**：需确认 Díaz et al. (2021) 是否已隐含处理了受处理混杂（查其假设）；若已处理，则本提案无新意。此外，受处理混杂下的识别可能需要强完备性假设，可能不弱于跨世界独立性。需查 [5] 的 Assumption 4 是否可移植。
- **交付形态**：`定理型`（识别与效率界）+ `方法+模拟型`（估计量构造与模拟）
- **第一周动作**：
  1. 读 [10] 的定理 1-4，提取干预间接效应的定义和 EIF 推导步骤。
  2. 读 [5] 的 Section 3（识别部分），理解近端方法如何处理未观测混杂。
  3. 读 [16] 的 Theorem 1，确认 CRT 设定下干预效应的识别公式。
  4. 在最小内核设定下，写出干预间接效应在受处理混杂下的识别公式（利用负对照变量）。
  5. 推导该识别公式的一阶影响函数，并检查是否满足 Neyman 正交性。

---

### 本页的证据论文

- [1] ★ [Calibrated sensitivity models](/research-news/deep_reads/2026-05-26-10.1093_biomet_asag001/) — Biometrika · 2026-05-26
- [2] ★ [Principal stratification with continuous post-treatment variables: nonparametric identification and semiparametric estimation](/research-news/deep_reads/2026-05-26-10.1093_jrsssb_qkaf049/) — Journal of the Royal Statistical Society Series B · 2026-05-26
- [3] ★ [Semiparametric Efficiency of Residual Correlation Testing under Gaussian Additive Noise Models](/research-news/deep_reads/2026-06-02-2606.01011/) — 2026-06-02
- [4] ★ [Doubly robust estimation and sensitivity analysis for marginal structural quantile models](/research-news/deep_reads/2026-07-03-10.1093_biomtc_ujae045/) — Biometrics · 2026-07-03
- [5] ★ [Proximal Mediation Analysis with Unmeasured Treatment-Induced Confounding](/research-news/deep_reads/2026-07-07-2607.02901/) — 2026-07-07
- [6] ★ [An Instrumental Variable Approach to Account for Informative Treatment Switching in Real-world Evidence](/research-news/deep_reads/2026-07-03-2607.00980/) — 2026-07-03
- [7] ★ [A statistical test for the benefits of personalizing interventions](/research-news/deep_reads/2026-08-01-10.1126_science.aeb9506/) — Science · 2026-08-01
- [8] ★ [Incremental effects for continuous exposures](/research-news/deep_reads/2026-08-31-2409.11967/) — 2026-08-31
- [9] ★ [Towards a Unified Theory for Semiparametric Data Fusion with Individual-Level Data](/research-news/deep_reads/2026-09-01-2409.09973/) — 2026-09-01
- [10] ★ [Causal mediation analysis for stochastic interventions](/research-news/deep_reads/2026-08-31-1901.02776/) — 2026-08-31
- [11] [Doubly robust nonparametric instrumental variable estimators for survival outcomes](/research-news/deep_reads/2026-06-20-10.1093_biostatistics_kxab036/) — Biostatistics · 2026-06-20
- [12] [Average partial effect estimation using double machine learning](/research-news/deep_reads/2026-05-26-10.1214_25-aos2563/) — Annals of Statistics · 2026-05-26
- [13] [Doubly Robust Pointwise Confidence Intervals for a Monotonic Continuous Treatment Effect Curve](/research-news/deep_reads/2026-05-26-10.1080_01621459.2026.2639735/) — Journal of the American Statistical Association · 2026-05-26
- [14] [Semiparametric Inference for Causal Effects on Functional Outcomes](/research-news/deep_reads/2026-05-27-2605.26964/) — 2026-05-27
- [15] [Causal inference targeting a concentration index for studies of health inequalities](/research-news/deep_reads/2026-06-10-10.1093_biomtc_ujag082/) — Biometrics · 2026-06-10
- [16] [Semiparametric causal mediation analysis of cluster-randomized trials for indirect and spillover effects](/research-news/deep_reads/2026-06-10-10.1093_biomtc_ujag017/) — Biometrics · 2026-06-10
- [17] [Parametrization, prior independence, and the semiparametric Bernstein-von Mises theorem for the partially linear model](/research-news/deep_reads/2026-06-18-10.3150_25-bej1917/) — Bernoulli · 2026-06-18
- [18] [Semi-parametric Bernstein-von Mises theorem in linear inverse problems](/research-news/deep_reads/2026-06-18-10.1214_25-ejs2372/) — Electronic Journal of Statistics · 2026-06-18
- [19] [Estimating Effects of Longitudinal Modified Treatment Policies ( <scp>LMTPs</scp> ) on Rates of Change in Health Outcomes](/research-news/deep_reads/2026-06-19-10.1002_sim.70604/) — Statistics in Medicine · 2026-06-19
- [20] [Estimation of treatment effect among treatment responders with a time‐to‐event endpoint](/research-news/deep_reads/2026-06-19-10.1111_sjos.12706/) — Scandinavian Journal of Statistics · 2026-06-19
- [21] [Kernel-Profile Efficient Estimation in Generalized Partially Linear Models with Missing Outcomes in Longitudinal Studies](/research-news/deep_reads/2026-06-19-10.5705_ss.202024.0380/) — Statistica Sinica · 2026-06-19
- [22] [Semiparametric Efficient Estimation of Quantile Regression](/research-news/deep_reads/2026-06-19-10.5705_ss.202024.0378/) — Statistica Sinica · 2026-06-19
- [23] [Decomposition, identification and multiply robust estimation of natural mediation effects with multiple mediators](/research-news/deep_reads/2026-06-20-10.1093_biomet_asac004/) — Biometrika · 2026-06-20
- [24] [Doubly robust evaluation of high-dimensional surrogate markers](/research-news/deep_reads/2026-06-20-10.1093_biostatistics_kxac020/) — Biostatistics · 2026-06-20
- [25] [Efficient and multiply robust risk estimation under general forms of dataset shift](/research-news/deep_reads/2026-06-20-10.1214_24-aos2422/) — Annals of Statistics · 2026-06-20
- [26] [Efficient estimation under data fusion](/research-news/deep_reads/2026-06-20-10.1093_biomet_asad007/) — Biometrika · 2026-06-20
- [27] [Efficient semiparametric estimation of network treatment effects under partial interference](/research-news/deep_reads/2026-06-20-10.1093_biomet_asac009/) — Biometrika · 2026-06-20
- [28] [Model-assisted sensitivity analysis for treatment effects under unmeasured confounding via regularized calibrated estimation](/research-news/deep_reads/2026-06-20-10.1093_jrsssb_qkae034/) — Journal of the Royal Statistical Society Series B · 2026-06-20
- [29] [Nonparametric efficient estimation of marginal structural models with continuous time-varying treatments](/research-news/deep_reads/2026-06-20-10.1093_biomet_asag026/) — Biometrika · 2026-06-20
- [30] [Proximal survival analysis to handle dependent right censoring](/research-news/deep_reads/2026-06-20-10.1093_jrsssb_qkae037/) — Journal of the Royal Statistical Society Series B · 2026-06-20

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

