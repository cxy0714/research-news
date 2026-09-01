# 选题提案 · 双稳健估计与半参效率理论

**战线范围**: 发展双稳健（doubly robust）估计量及其影响函数（influence function），推导半参数效率界（semiparametric efficiency bound），并应用于ATE、CATE、分位数效应、剂量反应函数等因果参数的推断。  
**证据论文**: 30 篇（★ 收藏 18 篇）  
**提案条数**: 2  
**生成日期**: 2026-09-01  

> 每条提案的证据都点名来源论文 [k] 并引其原话。**不打分、不排名**——「证据 N 篇」是可数的事实，不是质量分。标了 ⚠️ 单点证据的条目只有一篇论文支撑，自己掂量。

---

### 提案 1：High-Dimensional Doubly Robust Variance Estimation: When Nuisance Functions Are Estimated via Machine Learning

- **claim（一句话）**：对于任意双稳健（DR）估计量，当结果回归和倾向性得分均用高维/非参数机器学习方法（如 Lasso、随机森林、深度神经网络）估计时，推导其渐近方差的一致估计量，并给出该方差估计量达到“推断双稳健”（即至少一个 nuisance 模型正确时方差估计一致）的充分条件。

- **最小内核**：单时点、二值处理、连续结局，协变量维度 \(p\) 固定但 nuisance 函数用 Lasso（惩罚线性回归）估计。在此特例下，命题退化为：给定结果模型用 Lasso 估计（可能错误指定），倾向性得分用逻辑回归估计（正确指定），经验 sandwich 方差估计是否仍一致？若否，需要何种修正（如交叉拟合、bootstrap 或高阶影响函数校正）？

- **证据**：
  - [4] Limitation section 明确写道：“Machine learning methods are typically not compatible with the estimating equations approach discussed in this paper”，并将“拓展到高维/自适应设定”列为第一开放问题。
  - [7] Web Appendix F 指出：“it is feasible to pursue double machine learning by estimating \(\pi_k\) with nonparametric estimators...”，但随后承认“未给出理论保证”，且定理 2 的证明依赖 \(n^{-1/4}\) 收敛速率，而高维/非参数设定下该速率可能不成立。
  - [22] 定理 3 的条件 (C2) 要求 nuisance 估计收敛速率 \(n^{-1/4}\)，并在开放问题 4 中明确问：“高维 \(X_0\) 下 \(\hat{\theta}_t\) 的渐近性质是否仍成立，或需更高阶修正（如 HOIF）？”

- **为什么现在**：最近 [5] 证明了 DML 在结构无关模型下的渐近不可容许性，并给出了 HOIF 估计量作为占优选择；HOIF 通过高阶偏差校正可以容忍更慢的 nuisance 收敛速率（如 \(n^{-1/3}\)），这为高维设定下方差推断提供了新的理论工具。同时 [4] 的模拟显示经验 sandwich 和 bootstrap 在有限样本下表现良好，但缺乏高维理论，HOIF 的引入可能填补这一缺口。

- **武器匹配**：用 **高阶 U 统计量的计算（treewidth / tensor contraction / einsum）** 来显式计算 HOIF 估计量的方差项。具体地，HOIF 的方差涉及多个 nuisance 函数估计的乘积的期望，可表示为高阶 U 统计量，通过 einsum 和张量缩并高效计算其渐近方差，从而构造出可操作的方差估计量。

- **风险与竞争**：
  - 可能已被抢先：Benkeser et al. (2017) 对 TMLE 的方差在高维下已有部分结果，但针对一般 DR 估计量（如 AIPW）的方差双稳健在高维下尚未解决。需查 Avagyan & Vansteelandt (2021) 以及近期关于“debiased machine learning”的方差估计工作。
  - 假设太强：HOIF 需要选择字典大小 \(k\) 且要求 \(k = o(n)\)，若真实 nuisance 函数稀疏性不足，HOIF 的方差可能爆炸。需在模拟中检验。
  - 反例存在：当两个 nuisance 模型都错误且偏差较大时，任何方差估计都可能失效，需明确边界条件。

- **交付形态**：`方法+模拟型`（产出可计算的方差估计量 + 模拟证据，尤其利用 einsum 实现 HOIF 方差的高效计算）。

- **第一周动作**：
  1. 读 [4] 的 Section 2-3，复现其模拟中“双模型正确”和“单模型正确”场景下的 sandwich 方差估计，记录有限样本偏差。
  2. 读 [5] 的 Lemma 2-6，写出 HOIF 估计量在单时点 ATE 下的二阶影响函数表达式，并推导其方差项作为 U 统计量的形式。
  3. 读 [22] 的定理 3 条件，确认高维下 \(n^{-1/4}\) 速率不成立的具体场景（如 Lasso 的收敛速率）。
  4. 用 Python 实现一个简单的高维模拟（\(p=50, n=200\)），比较 AIPW + sandwich、AIPW + bootstrap、AIPW + HOIF 方差估计的覆盖概率。
  5. 搜索 Avagyan & Vansteelandt (2021) 和 Benkeser et al. (2017)，确认其是否已处理高维 DR 方差问题。

---

### 提案 2：Computational-Statistical Tradeoffs in Bridge Function Estimation for Proximal Causal Inference

- **claim（一句话）**：在近端因果推断（proximal causal inference）中，当代理变量 \(Z, W\) 维度发散或连续时，桥函数 \(h\) 和 \(q\) 的估计面临不适定逆问题，其 minimax 最优收敛速率与计算复杂度（以张量网络树宽衡量）之间的权衡，并构造达到该权衡的自适应估计量。

- **最小内核**：单时点、二值处理、连续结局，代理变量 \(Z, W\) 均为低维连续（\(d_Z = d_W = 1\)），且桥函数满足线性积分方程 \(E[Y \mid Z, X] = E[h(W, X) \mid Z, X]\)。在此特例下，命题退化为：当积分算子为紧算子时，桥函数的收敛速率由算子谱衰减决定；若用截断奇异值分解（TSVD）估计，计算复杂度为 \(O(n^3)\)；能否用树宽为 \(O(\log n)\) 的张量网络近似该算子，从而将计算复杂度降至 \(O(n \log n)\) 而不损失统计效率？

- **证据**：
  - [8] Section 3.3 的 minimax 学习框架未讨论计算复杂度，开放问题 4 明确问：“桥函数估计的计算复杂度...对于高维 Z 和 W，求解 min-max 优化问题的计算成本可能很高。”
  - [10] 开放问题 2 指出：“当 Z 和 W 的维度很高，甚至大于样本量时，如何有效地估计桥函数 h 和 q，并使其满足本文所需的 \(L_2\) 收敛率条件？”
  - [23] 开放问题 1 提到：“若完备性条件失效或解不唯一，如何构造仍一致的估计量？是否可借鉴 Kallus et al. (2021) 的 minimax 学习框架，将 NDE/NIE 的嵌套 bridge 积分方程转化为 minimax 优化问题？” 该问题直接指向桥函数估计的计算可行性。
  - [20] 对近端反事实分位数过程的谱特征和相变分析（Assumption 4.4 的阈值饱和假设）提供了算子正则性的刻画，为理解桥函数估计的 ill-posedness 程度提供了新工具。

- **为什么现在**：[20] 首次给出了近端推断中算子谱衰减与相变边界的显式刻画，这使得我们可以将桥函数估计的 minimax 下界与计算复杂度（如张量网络的树宽）联系起来。同时 [11] 关于嵌套马尔可夫模型中 Verma 约束的切空间刻画，提供了另一种将积分方程转化为有限维逼近的几何视角，可能简化桥函数的计算。

- **武器匹配**：用 **高阶 U 统计量的计算（treewidth / tensor contraction / einsum）** 来参数化桥函数估计中的积分算子。具体地，将积分算子离散化为张量，其树宽对应计算复杂度；通过 einsum 实现张量缩并，从而在给定树宽下高效求解桥函数，并推导该近似下的统计收敛速率。

- **风险与竞争**：
  - 已被做过：Kallus et al. (2021) 的 minimax 学习框架已处理部分桥函数估计，但未讨论计算复杂度与树宽的关系。需查其是否涉及张量网络。
  - 假设太强：桥函数的存在性和唯一性依赖于完备性条件，该条件在高维下难以验证。若不完备，估计量可能不一致。
  - 算不出来：当算子谱衰减极慢（严重 ill-posed）时，即使最优算法也需要指数级样本，此时统计-计算权衡可能无实用解。

- **交付形态**：`定理型`（产出桥函数估计的 minimax 下界与计算复杂度下界，以及达到该下界的自适应估计量的存在性证明）。

- **第一周动作**：
  1. 读 [20] 的 Section 3-4，理解其谱特征和相变分析，特别是算子紧致性和阈值饱和假设。
  2. 读 [8] 的 Section 3.3，写出其 minimax 学习框架的优化目标，并识别出其中的积分算子。
  3. 读 [10] 的 Assumption A3（完备性条件），并查阅 Kress (1999) 关于紧算子谱分解的经典结果，写出桥函数估计的 minimax 下界形式。
  4. 用 Python 实现一个简单的一维连续代理变量模拟（\(n=500\)），用 TSVD 和用树宽为 2 的张量网络分别估计桥函数，比较 MSE 和运行时间。
  5. 搜索 Kallus et al. (2021) 和 Singh et al. (2024) 关于近端推断计算复杂度的文献，确认是否存在已有结果。

---

### 本页的证据论文

- [1] ★ [Calibrated sensitivity models](/research-news/deep_reads/2026-05-26-10.1093_biomet_asag001/) — Biometrika · 2026-05-26
- [2] ★ [Principal stratification with continuous post-treatment variables: nonparametric identification and semiparametric estimation](/research-news/deep_reads/2026-05-26-10.1093_jrsssb_qkaf049/) — Journal of the Royal Statistical Society Series B · 2026-05-26
- [3] ★ [Semiparametric Efficiency of Residual Correlation Testing under Gaussian Additive Noise Models](/research-news/deep_reads/2026-06-02-2606.01011/) — 2026-06-02
- [4] ★ [Double robust variance estimation with parametric working models](/research-news/deep_reads/2026-06-19-10.1093_biomtc_ujaf054/) — Biometrics · 2026-06-19
- [5] ★ [On the Asymptotic Inadmissibility of Double Machine Learning Estimators Under Structure-Agnostic Models](/research-news/deep_reads/2026-06-24-2606.22391/) — 2026-06-24
- [6] ★ [Semiparametric Efficiency Theory as Differential Calculus on a Space of Probability Distributions](/research-news/deep_reads/2026-06-24-2606.22784/) — 2026-06-24
- [7] ★ [Doubly robust estimation and sensitivity analysis for marginal structural quantile models](/research-news/deep_reads/2026-07-03-10.1093_biomtc_ujae045/) — Biometrics · 2026-07-03
- [8] ★ [Proximal Mediation Analysis with Unmeasured Treatment-Induced Confounding](/research-news/deep_reads/2026-07-07-2607.02901/) — 2026-07-07
- [9] ★ [Structural mean models for instrumented difference-in-differences](/research-news/deep_reads/2026-07-15-10.1214_24-ejs2313/) — Electronic Journal of Statistics · 2026-07-15
- [10] ★ [Debiased inference for proximal dose-response function](/research-news/deep_reads/2026-08-05-2608.00404/) — 2026-08-05
- [11] ★ [Toward a Semiparametric Efficiency Theory under Equality Constraints in Nested Markov Models](/research-news/deep_reads/2026-08-28-2608.24602/) — 2026-08-28
- [12] ★ [Group-Level Treatment Effect Heterogeneity in Difference-in-Differences: A Balanced Approach](/research-news/deep_reads/2026-06-25-2606.24785/) — 2026-06-25
- [13] ★ [An Instrumental Variable Approach to Account for Informative Treatment Switching in Real-world Evidence](/research-news/deep_reads/2026-07-03-2607.00980/) — 2026-07-03
- [14] ★ [Marginal Causal Effect Estimation with Continuous Instrumental Variables](/research-news/deep_reads/2026-07-10-2510.14368/) — 2026-07-10
- [15] ★ [A statistical test for the benefits of personalizing interventions](/research-news/deep_reads/2026-08-01-10.1126_science.aeb9506/) — Science · 2026-08-01
- [16] ★ [Incremental effects for continuous exposures](/research-news/deep_reads/2026-08-31-2409.11967/) — 2026-08-31
- [17] ★ [Towards a Unified Theory for Semiparametric Data Fusion with Individual-Level Data](/research-news/deep_reads/2026-09-01-2409.09973/) — 2026-09-01
- [18] ★ [Causal mediation analysis for stochastic interventions](/research-news/deep_reads/2026-08-31-1901.02776/) — 2026-08-31
- [19] [Proximal Path-Specific Inference](/research-news/deep_reads/2026-05-12-2605.09462/) — 2026-05-12
- [20] [Regularity, Phase Transitions, and Uniform Inference for Proximal Counterfactual Quantile Processes](/research-news/deep_reads/2026-05-12-2605.09257/) — 2026-05-12
- [21] [Semiparametric Mediation Analysis with Separately Observed Mediator and Outcome under Unmeasured Confounding](/research-news/deep_reads/2026-06-17-2606.17232/) — 2026-06-17
- [22] [Doubly robust nonparametric instrumental variable estimators for survival outcomes](/research-news/deep_reads/2026-06-20-10.1093_biostatistics_kxab036/) — Biostatistics · 2026-06-20
- [23] [Proximal mediation analysis](/research-news/deep_reads/2026-06-20-10.1093_biomet_asad015/) — Biometrika · 2026-06-20
- [24] [Improving the Efficiency of Subgroup Analysis in Randomized Controlled Trials with TMLE](/research-news/deep_reads/2026-05-18-2605.15483/) — 2026-05-18
- [25] [Targeted maximum likelihood estimation of vaccine effectiveness and immune correlates in test-negative design studies with missing data](/research-news/deep_reads/2026-05-22-2605.21793/) — 2026-05-22
- [26] [Average partial effect estimation using double machine learning](/research-news/deep_reads/2026-05-26-10.1214_25-aos2563/) — Annals of Statistics · 2026-05-26
- [27] [Doubly Robust Pointwise Confidence Intervals for a Monotonic Continuous Treatment Effect Curve](/research-news/deep_reads/2026-05-26-10.1080_01621459.2026.2639735/) — Journal of the American Statistical Association · 2026-05-26
- [28] [Identification and multiply robust estimation in causal mediation analysis across principal strata](/research-news/deep_reads/2026-05-26-10.1093_jrsssb_qkaf037/) — Journal of the Royal Statistical Society Series B · 2026-05-26
- [29] [On propensity score matching with a diverging number of matches](/research-news/deep_reads/2026-05-26-10.1093_biomet_asae026/) — Biometrika · 2026-05-26
- [30] [Semiparametric Efficient Fusion of Individual Data and Summary Statistics](/research-news/deep_reads/2026-05-26-10.1080_01621459.2026.2659379/) — Journal of the American Statistical Association · 2026-05-26

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

