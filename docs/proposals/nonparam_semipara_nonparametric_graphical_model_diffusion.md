# 选题提案 · 非参数图模型与扩散模型选择

**战线范围**: 利用扩散模型、得分匹配等工具进行非参数无向图模型选择，研究模型选择相合性、高维非参数估计。  
**证据论文**: 30 篇（★ 收藏 8 篇）  
**提案条数**: 2  
**生成日期**: 2026-09-01  

> 每条提案的证据都点名来源论文 [k] 并引其原话。**不打分、不排名**——「证据 N 篇」是可数的事实，不是质量分。标了 ⚠️ 单点证据的条目只有一篇论文支撑，自己掂量。

---

### 提案 1：Sparse-Graph-Adaptive Nonparametric Graphical Model Selection via Diffusion Models

- **claim（一句话）**：在无向图模型选择中，当真实精度矩阵的支撑图是稀疏的（即每个节点最多连接 \(s \ll D\) 个其他节点）时，证明基于扩散模型的条件协方差估计量（[4] 的 \(\widehat{\Sigma}_t\)）的图恢复相合性在高维 \(D \gg n\) 下仍成立，且所需信号强度条件可放松到与稀疏度 \(s\) 而非环境维度 \(D\) 相关。

- **最小内核**：\(D=3\)，真实图是一条链（1-2-3），即精度矩阵非零元仅在对角线和 \((1,2),(2,3)\) 位置。在该特例下，要证的命题退化为：当 \(n \to \infty\) 且 \(D\) 固定时，[4] Theorem 4.3 的相合性条件 \(C_\gamma \gtrsim n^{-\tilde{\beta}\beta/((\tilde{\beta}+4)(2\beta+d)) + \delta}\) 中的 \(d\) 可被替换为最大度 \(2\)（而非 \(D=3\)），且当 \(D\) 发散时该替换仍成立。

- **证据**：
  - [4] Section 8 第一段：“一个自然的下一步是将我们的分析扩展到高维设定，其中 \(D\) 随 \(n\) 发散。” 并指出常数 \(C_3\) 对 \(D\) 的依赖是当前瓶颈。
  - [24] Section 5（开放问题3）：“当 \(d\) 较大时速率极慢（维数灾难）。是否可以利用 \(f\) 的稀疏结构（例如 \(f\) 只依赖少量变量，即 ODE 中的相互作用图是稀疏的）来突破 \(d\) 出现在分母中的困境？” 该问题明确指向利用稀疏图结构缓解维数灾难，与图模型选择中的稀疏精度矩阵假设直接对应。

- **为什么现在**：[4] 的 Theorem 4.3 已给出固定 \(D\) 下的相合性，但证明中多处用到 \(D\) 的有限性（如 Lemma B.1 中的 \((DK)^{-1}\) 条件）。[24] 的速率表达式 \(n^{-\beta/(2(\beta+1)+d)}\) 展示了维数灾难的指数形式，并提出了稀疏结构作为突破路径。两者结合，使得“在稀疏图假设下将 [4] 的结论推广到高维”成为可操作的理论问题。

- **武器匹配**：用 **非参数统计** 中的 minimax 下界工具（如 Fano 引理、Assouad 引理）构造稀疏图模型下 Hessian 估计的 minimax 下界，并与 [4] 的上界匹配，证明稀疏度 \(s\) 替代 \(D\) 的最优性。

- **风险与竞争**：
  - 风险：该选题可能已被 [4] 的作者或后续工作（如 Gottwald et al. 2025 的扩展）部分解决。需查 [4] 的引用文献中是否有 2025-2026 年关于高维稀疏图选择的后续论文，以及 [24] 的引用中是否有将稀疏 ODE 图结构用于图模型的工作。
  - 竞争：SING/L-SING 方法（[4] 引用的竞争路线）也处理稀疏图，但依赖直接 Hessian 估计。需确认 SING 在高维下的理论是否已有稀疏度依赖的速率。
  - 假设风险：稀疏图假设（每个节点度 \(\le s\)）在真实高维图中可能不成立（如 hub 图）。需在提案中明确假设图的稀疏性，并讨论 hub 图下的扩展。

- **交付形态**：`定理型`

- **第一周动作**：
  1. 读 [4] 的 Lemma B.1 及其证明，精确提取常数 \(C_3\) 对 \(D\) 的依赖形式。
  2. 读 [24] 的 Section 5 关于稀疏结构的讨论，并查阅其引用的 Schmidt-Hieber (2017) 关于复合函数结构的速率。
  3. 用 Fano 引理推导 \(D\) 维稀疏精度矩阵（每个节点度 \(\le s\)）下 Hessian 估计的 minimax 下界，写出初步表达式。
  4. 在 \(D=3\) 链图设定下，手动验证 [4] 的证明中哪些步骤依赖 \(D\) 的有限性，并尝试用稀疏度 \(s=2\) 替换。
  5. 搜索 [4] 和 [24] 的引用文献中是否有 2025-2026 年关于高维稀疏图模型与扩散模型结合的工作。

### 提案 2：High-Dimensional Nonparametric Graph Recovery Using k-NN Azadkia-Chatterjee Correlations and Diffusion-Based Hessian Estimation

- **claim（一句话）**：将 Azadkia-Chatterjee 条件相关系数（[1]）的推断理论推广到基于 \(k\)-NN 图（\(k>1\)）的版本，并证明该系数与 [4] 的扩散模型估计的 Hessian 矩阵在条件独立图恢复中具有等价性，从而在高维 \(D \gg n\) 下建立基于 \(k\)-NN 相关系数的图选择相合性。

- **最小内核**：\(D=2\)，两个变量 \(X_1, X_2\)，真实图为空（即 \(X_1 \perp X_2\)）。在该特例下，要证的命题退化为：基于 \(k\)-NN 的 Azadkia-Chatterjee 条件相关系数 \(\xi_n^{(k)}(X_1, X_2)\) 在 \(H_0: X_1 \perp X_2\) 下的极限分布是否为标准正态（类似 [1] 中 \(k=1\) 的结果），且其检验功效是否高于 [1] 的 1-NN 版本。

- **证据**：
  - [1] Section 1.1 对 Lin and Han (2023) 的讨论：“Lin and Han (2023) 建议使用多个近邻 (multi-NN) 来提升 \(\xi_n\) 的统计功效。**本文的整套推断理论能否推广到基于 \(k\)-NN (\(k>1\)) 的 Azadkia-Chatterjee 条件相关系数上？其极限方差表达式和计算复杂度会如何变化？**”
  - [4] Section 8 第一段：“一个自然的下一步是将我们的分析扩展到高维设定。” 同时 [4] 的 Section 5 提到聚类方法依赖阈值选择，而 \(k\)-NN 相关系数可提供数据驱动的阈值。

- **为什么现在**：[1] 已给出 1-NN 下 \(T_n\) 的极限分布和方差估计，但明确承认 \(k>1\) 的理论是开放问题。[4] 的扩散模型方法在高维下需要自适应阈值，而 \(k\)-NN 相关系数天然提供一种基于近邻的依赖度量，且 [1] 的方差估计技术（Hájek 表示 + 协方差分解）可推广到 \(k\)-NN 图。两者结合使得“用 \(k\)-NN 相关系数替代 [4] 的启发式聚类”成为可操作的推断方案。

- **武器匹配**：用 **高阶 U 统计量的计算（treewidth / tensor contraction / einsum）** 来高效计算 \(k\)-NN 相关系数中的 U 统计量核（涉及 \(k\) 个近邻的指示函数），将 [1] 中 1-NN 的 \(O(n \log n)\) 算法推广到 \(k\)-NN 的 \(O(k n \log n)\) 并保持可计算性。

- **风险与竞争**：
  - 风险：Lin and Han (2023) 可能已有 \(k\)-NN 版本的初步结果，需查该文是否已给出极限分布。另外，[1] 的 Remark 4.2 指出 \(T_n\) 的检验 Pitman 效率为零，\(k>1\) 可能无法根本改善，需验证 \(k\) 增长是否改变这一性质。
  - 竞争：Huang et al. (2022) 的 KPC 度量也基于近邻，且已有部分理论。需确认 KPC 的 \(k\)-NN 版本是否已被研究。
  - 假设风险：\(k\)-NN 图在高维下近邻距离膨胀，可能导致相关系数退化。需在提案中假设协变量分布具有低维流形结构（如 [10] 的几何自适应），或使用 [4] 的扩散模型先降维。

- **交付形态**：`方法+模拟型`

- **第一周动作**：
  1. 读 [1] 的 Section 1.1 关于 multi-NN 的讨论，并找到 Lin and Han (2023) 的原文，确认其是否已有 \(k\)-NN 的极限理论。
  2. 读 [1] 的证明中 Hájek 表示和协方差分解部分（Section 3-4），尝试将 1-NN 的指示函数替换为 \(k\)-NN 的指示函数，写出 \(k\)-NN 下 U 统计量的核表达式。
  3. 在 \(D=2\) 独立高斯设定下，用 R 实现 \(k=2\) 的 Azadkia-Chatterjee 相关系数，并与 [1] 的 1-NN 版本比较经验分布。
  4. 读 [4] 的 Section 5 聚类方法，设计一个模拟：用 \(k\)-NN 相关系数矩阵替代 [4] 的启发式阈值，在 \(D=10\) 链图下比较图恢复的 F1 分数。
  5. 用 einsum 表示 \(k\)-NN 相关系数中的张量收缩（涉及近邻矩阵的乘积），评估计算复杂度是否仍为 \(O(n \log n)\) 量级。

---

### 本页的证据论文

- [1] ★ [Limit theorems of Azadkia-Chatterjee's conditional graph correlation](/research-news/deep_reads/2026-06-17-2606.15433/) — 2026-06-17
- [2] ★ [A new design for observational studies applied to the study of the effects of high school football on cognition late in life](/research-news/deep_reads/2026-06-19-10.1214_24-aoas1949/) — Annals of Applied Statistics · 2026-06-19
- [3] ★ [Multiply robust matching estimators of average and quantile treatment effects](/research-news/deep_reads/2026-06-23-10.1111_sjos.12585/) — Scandinavian Journal of Statistics · 2026-06-23
- [4] ★ [Nonparametric undirected graphical model selection using diffusion models](/research-news/deep_reads/2026-06-09-2606.08468/) — 2026-06-09
- [5] ★ [Generalized nonparametric regression in reproducing kernel Hilbert spaces: Consistency and rates of convergence](/research-news/deep_reads/2026-06-24-2606.22993/) — 2026-06-24
- [6] ★ [Stochastic interventions, sensitivity analysis, and optimal transport](/research-news/deep_reads/2026-08-31-2411.14285/) — 2026-08-31
- [7] ★ [Nonparametric Estimation of Optimal Stochastic Just-In-Time Adaptive Interventions for Distal Outcomes](/research-news/deep_reads/2026-06-25-2606.25107/) — 2026-06-25
- [8] ★ [Nonparametric estimation of scalar diffusions based on low frequency data](/research-news/deep_reads/2026-08-31-math_0503680/) — 2026-08-31
- [9] [Doubly robust nonparametric instrumental variable estimators for survival outcomes](/research-news/deep_reads/2026-06-20-10.1093_biostatistics_kxab036/) — Biostatistics · 2026-06-20
- [10] [Geometry Adaptive Counterfactual Distribution Learning with Diffusion-Guided Smoothing](/research-news/deep_reads/2026-05-26-2605.25811/) — 2026-05-26
- [11] [On propensity score matching with a diverging number of matches](/research-news/deep_reads/2026-05-26-10.1093_biomet_asae026/) — Biometrika · 2026-05-26
- [12] [Doubly Robust Uniform Confidence Bands for Group-Time Conditional Average Treatment Effects in Difference-in-Differences](/research-news/deep_reads/2026-06-07-10.1080_07350015.2025.2541719/) — Journal of Business & Economic Statistics · 2026-06-07
- [13] [Estimating Effects of Longitudinal Modified Treatment Policies ( <scp>LMTPs</scp> ) on Rates of Change in Health Outcomes](/research-news/deep_reads/2026-06-19-10.1002_sim.70604/) — Statistics in Medicine · 2026-06-19
- [14] [Nonparametric estimation of path‐specific effects in the presence of nonignorable missing covariates](/research-news/deep_reads/2026-06-19-10.1111_sjos.70002/) — Scandinavian Journal of Statistics · 2026-06-19
- [15] [Statistical inference for heterogeneous treatment effect with right-censored data from synthesizing randomized clinical trials and real-world data](/research-news/deep_reads/2026-06-19-10.1093_biomtc_ujaf131/) — Biometrics · 2026-06-19
- [16] [Variable importance measures for heterogeneous treatment effects](/research-news/deep_reads/2026-06-19-10.1093_biomtc_ujaf140/) — Biometrics · 2026-06-19
- [17] [A nonparametric doubly robust test for a continuous treatment effect](/research-news/deep_reads/2026-06-20-10.1214_24-aos2405/) — Annals of Statistics · 2026-06-20
- [18] [Assessing the causal effects of a stochastic intervention in time series data: are heat alerts effective in preventing deaths and hospitalizations?](/research-news/deep_reads/2026-06-20-10.1093_biostatistics_kxad002/) — Biostatistics · 2026-06-20
- [19] [Nonparametric estimation via partial derivatives](/research-news/deep_reads/2026-06-20-10.1093_jrsssb_qkae093/) — Journal of the Royal Statistical Society Series B · 2026-06-20
- [20] [Practical causal mediation analysis: extending nonparametric estimators to accommodate multiple mediators and multiple intermediate confounders](/research-news/deep_reads/2026-06-20-10.1093_biostatistics_kxae012/) — Biostatistics · 2026-06-20
- [21] [Instrumental variable estimation of distributional causal effects](/research-news/deep_reads/2026-06-23-10.1214_25-ejs2460/) — Electronic Journal of Statistics · 2026-06-23
- [22] [Asymptotics of AIC, BIC and Cp model selection rules in high-dimensional regression](/research-news/deep_reads/2026-07-14-10.3150_21-bej1422/) — Bernoulli · 2026-07-14
- [23] [Nonparametric estimation of the total treatment effect with multiple outcomes in the presence of terminal events](/research-news/deep_reads/2026-06-10-10.1093_biomtc_ujag053/) — Biometrics · 2026-06-10
- [24] [Nonparametric estimation of ordinary differential equations: Snake and stubble](/research-news/deep_reads/2026-06-18-10.3150_25-bej1936/) — Bernoulli · 2026-06-18
- [25] [Simultaneous semiparametric inference for single-index models](/research-news/deep_reads/2026-06-18-10.3150_24-bej1834/) — Bernoulli · 2026-06-18
- [26] [Antibiotics and Preterm Delivery: The Prevalent New-user Cohort Design to Resolve Immortal Time Bias](/research-news/deep_reads/2026-06-19-10.1097_ede.0000000000001947/) — Epidemiology · 2026-06-19
- [27] [Nonparametric estimation of densities on the hypersphere using a parametric guide](/research-news/deep_reads/2026-06-19-10.1111_sjos.12737/) — Scandinavian Journal of Statistics · 2026-06-19
- [28] [A Bayesian Nonparametric Approach to Mediation and Spillover Effects with Multiple Mediators in Cluster-Randomized Trials](/research-news/deep_reads/2026-06-20-10.1080_01621459.2025.2544366/) — Journal of the American Statistical Association · 2026-06-20
- [29] [Efficient nonparametric estimation of Toeplitz covariance matrices](/research-news/deep_reads/2026-06-20-10.1093_biomet_asae002/) — Biometrika · 2026-06-20
- [30] [Non-agency interventions for causal mediation in the presence of intermediate confounding](/research-news/deep_reads/2026-06-20-10.1093_jrsssb_qkad130/) — Journal of the Royal Statistical Society Series B · 2026-06-20

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

