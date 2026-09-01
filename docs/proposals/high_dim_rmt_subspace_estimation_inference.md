# 选题提案 · 共享奇异子空间与公共子空间的最优估计与推断

**战线范围**: 针对多矩阵共享奇异子空间或公共子空间，研究minimax最优估计（如Stack-SVD、投影梯度下降）、sinΘ距离收敛率、自适应置信区间及渐近正态性，涉及计算-统计最优性权衡。  
**证据论文**: 30 篇（★ 收藏 13 篇）  
**提案条数**: 2  
**生成日期**: 2026-09-01  

> 每条提案的证据都点名来源论文 [k] 并引其原话。**不打分、不排名**——「证据 N 篇」是可数的事实，不是质量分。标了 ⚠️ 单点证据的条目只有一篇论文支撑，自己掂量。

---

### 提案 1：Optimal Estimation of Shared Singular Subspaces under Heteroskedastic and Correlated Noise

- **claim（一句话）**：要证：在噪声为异方差（如 Bernoulli）或行/列相关（如时间序列）时，共享奇异子空间估计的 minimax 最优收敛率，并构造达到该率的可计算估计量（以 sinΘ 距离度量）。

- **最小内核**：先打两个特例：  
  1. 两个矩阵（K=2），噪声独立但异方差（方差分别为 σ₁², σ₂²），共享奇异值强度 λ 相同，私有奇异值为 0。此时命题退化为：估计量在 sinΘ 距离下的收敛率是否仍为 n^{-1/2}（若 λ 足够大）？若否，率由 σ₁²/σ₂² 的比值如何决定？  
  2. 两个矩阵，噪声为行间一阶自相关 AR(1)（相关系数 ρ），列独立。此时命题退化为：相变阈值 λ_c 是否随 ρ 增大而增大？收敛率是否仍为 n^{-1/2} 或退化？

- **证据**：  
  - [2] 开放问题 2：“若噪声行间相关或列间相关（如时间序列矩阵），Stack-SVD 的相变阈值与新估计量的 minimax 性质如何变化？”（扎根于假设 2 的噪声条件）。  
  - [3] 开放问题 2：“当前模型要求同方差 Wigner 噪声，真实网络数据多为 Bernoulli 异方差。Extending our analysis to this setting may require additional modifications that explicitly account for heteroskedasticity。”（扎根于 Discussion 第二段）。  
  两篇独立论文点名了同一类 gap：现有理论局限于独立同分布噪声，需要推广到更一般的噪声结构。

- **为什么现在**：[2] 和 [3] 分别建立了同方差独立噪声下的 minimax 最优估计和相变理论，为推广提供了基准。[3] 的 Discussion 明确指出了异方差噪声的挑战，[2] 的假设 2 限制了噪声结构。最近 [3] 的 Conjecture 1（低度多项式猜想）暗示了计算下界，但尚未处理噪声推广。因此，现在可以结合 [2] 的 Stack-SVD 框架和 [3] 的相变分析，将噪声结构推广作为自然下一步。

- **武器匹配**：使用 **非参数统计** 中的 minimax 下界技术（Fano 不等式、Assouad 引理）推导下界；使用 **高阶 U 统计量的计算（treewidth / tensor contraction / einsum）** 来构造可计算的估计量——当噪声相关时，似然或矩条件可能涉及高阶张量，需要高效收缩（例如将协方差矩阵的逆表示为张量网络，用 einsum 优化收缩顺序）。

- **风险与竞争**：  
  - 可能已被 [2] 或 [3] 的作者后续工作覆盖：需检查 arXiv 上 2026 年 6 月之后的预印本（如搜索 “shared subspace heteroskedastic” 或 “correlated noise”）。  
  - 假设太强：若噪声相关结构未知（如 AR(1) 的 ρ 需估计），估计量可能不稳定。需查阅 [2] 的参考文献中关于时间序列矩阵谱分析的早期工作（如 Bai & Silverstein, 2010）。  
  - 反例：若噪声相关导致信息矩阵奇异（如完全共线），估计可能不可识别。需在最小内核中先验证可识别性条件。

- **交付形态**：`方法+模拟型`（需要构造可计算估计量并验证有限样本性能）。

- **第一周动作**：  
  1. 读 [2] 的 Section 2（模型设定）和 Theorem 3（谱分离假设），确认噪声假设的具体形式（假设 2 的原文）。  
  2. 读 [3] 的 Discussion 第二段，摘录异方差噪声的原文。  
  3. 推导两个矩阵异方差噪声下 sinΘ 距离的 minimax 下界（使用 Fano 不等式，假设共享奇异值强度 λ 已知，噪声方差比 σ₁²/σ₂² 固定）。  
  4. 设计模拟设定：K=2, n=100, p=50, λ=2, 噪声方差分别为 1 和 2（异方差），比较 Stack-SVD 与本文提出的新估计量（如加权 Stack-SVD）。  
  5. 查阅 [2] 和 [3] 的引用文献中是否有处理相关噪声的已有工作（如时间序列矩阵的谱方法，例如 “Spectral analysis of large dimensional random matrices” by Bai & Silverstein）。

---

### 提案 2：Shared Subspace Estimation without Spectral Gap: Minimax Rates under Continuous Singular Value Decay

- **claim（一句话）**：要证：当共享奇异值与私有奇异值之间不存在正间隙（即奇异值连续衰减）时，共享奇异子空间估计的 minimax 最优收敛率（以 sinΘ 距离度量），并构造达到该率的估计量（依赖奇异值衰减速度 α）。

- **最小内核**：先打一个特例：两个矩阵（K=2），共享奇异值序列为 λ_k = k^{-α}（α>0），私有奇异值为 0（即无私有成分）。此时谱分离条件不成立（间隙趋于 0）。命题退化为：估计量在 sinΘ 距离下的收敛率由 α 和矩阵维度 p 决定，可能为 n^{-α/(2α+1)} 或更慢。

- **证据**：⚠️ 单点证据。  
  - [2] 开放问题 1：“当前新估计量的 minimax 最优性依赖共享与私有奇异值之间的谱分离条件（间隙足够大）。若奇异值连续衰减或无间隙，能否构造仍达 minimax rate 的估计量？”（扎根于定理 3 的谱分离假设与 limitation 讨论）。仅此一篇论文明确点名此 gap。

- **为什么现在**：[2] 建立了有间隙下的 minimax 最优估计，但明确将无间隙情形列为开放问题。[3] 的相变理论也依赖于谱分离（虽然未明确讨论无间隙），但 [3] 的 Discussion 提到“精确依赖”可能涉及谱分离的量化。因此，现在可以基于 [2] 的框架，引入奇异值衰减速度 α 作为参数，推导新的 minimax 率。

- **武器匹配**：使用 **非参数统计** 中的 minimax 下界技术（通过构造一个参数族使得谱间隙随 n 变化，利用 Fano 引理或 Assouad 引理）；使用 **高阶 U 统计量的计算（treewidth / tensor contraction / einsum）** 来构造估计量——当奇异值连续时，可能需要截断或正则化，涉及张量收缩（例如将截断后的 SVD 表示为张量网络，用 einsum 优化计算）。

- **风险与竞争**：  
  - 可能已有工作处理无间隙情形（如低秩矩阵恢复中的 “incoherence” 条件）。需检查 [2] 的参考文献中是否引用了相关文献（如 Candès & Recht, 2009 的 “Exact matrix completion via convex optimization”）。  
  - 无间隙情形下估计可能根本不可行（信息论下界为常数），需要确认是否存在非平凡率。需查阅 [2] 的 limitation 讨论中是否提及。  
  - 若 α 很小（奇异值衰减慢），率可能极慢，需在最小内核中先验证是否可识别。

- **交付形态**：`定理型`（主要产出 minimax 下界和上界，可能附带简单模拟验证）。

- **第一周动作**：  
  1. 读 [2] 的 Theorem 3 及其证明，理解谱分离假设的具体数值条件（如 λ_min(shared) - λ_max(private) ≥ δ）。  
  2. 读 [2] 的 limitation 讨论段落，摘录原文。  
  3. 推导两个矩阵在奇异值连续衰减（λ_k = k^{-α}）下的 minimax 下界：构造两个参数族，使得它们的共享子空间相差一个小的旋转，但观测矩阵的分布难以区分（使用 Fano 引理，计算 KL 散度）。  
  4. 查阅 [2] 的参考文献中关于“无间隙”或“连续谱”的已有工作（如随机矩阵理论中的 Bai-Yin 律，或 “Spiked covariance model” 中无间隙情形的处理）。  
  5. 设计一个简单模拟：K=2, n=100, p=50, 共享奇异值按幂律衰减（α=1, 2），比较 Stack-SVD 与截断估计量（如保留前 r 个奇异值，r 由阈值选择）的 sinΘ 误差。

---

### 本页的证据论文

- [1] ★ [Calibrated sensitivity models](/research-news/deep_reads/2026-05-26-10.1093_biomet_asag001/) — Biometrika · 2026-05-26
- [2] ★ [Optimal Estimation of Shared Singular Subspaces Across Multiple Noisy Matrices](/research-news/deep_reads/2026-06-05-10.1109_tit.2026.3667733/) — IEEE Transactions on Information Theory · 2026-06-05
- [3] ★ [Statistically and Computationally Optimal Estimation and Inference of Common Subspaces](/research-news/deep_reads/2026-06-05-2606.06483/) — 2026-06-05
- [4] ★ [Adaptive Estimation of Aggregated Values of Conditional Linear Programs](/research-news/deep_reads/2026-06-09-2606.08359/) — 2026-06-09
- [5] ★ [Limit theorems of Azadkia-Chatterjee's conditional graph correlation](/research-news/deep_reads/2026-06-17-2606.15433/) — 2026-06-17
- [6] ★ [Fast Near-Optimal Estimation over Symmetric Norm Balls](/research-news/deep_reads/2026-06-02-2606.01554/) — 2026-06-02
- [7] ★ [Causal Inference for Functional Treatments with Stochastic Policies](/research-news/deep_reads/2026-06-25-2606.27518/) — 2026-06-25
- [8] ★ [Group-Level Treatment Effect Heterogeneity in Difference-in-Differences: A Balanced Approach](/research-news/deep_reads/2026-06-25-2606.24785/) — 2026-06-25
- [9] ★ [A simple adaptive estimator of the integrated square of a density](/research-news/deep_reads/2026-07-17-0803.0847/) — 2026-07-17
- [10] ★ [A statistical test for the benefits of personalizing interventions](/research-news/deep_reads/2026-08-01-10.1126_science.aeb9506/) — Science · 2026-08-01
- [11] ★ [A kernelization-based approach to nonparametric binary choice models](/research-news/deep_reads/2026-06-07-10.1016_j.jeconom.2026.106264/) — Journal of Econometrics · 2026-06-07
- [12] ★ [A Nonparametric Test for Cross-Unit Spillovers](/research-news/deep_reads/2026-08-05-2608.00136/) — 2026-08-05
- [13] ★ [Nonparametric estimation of scalar diffusions based on low frequency data](/research-news/deep_reads/2026-08-31-math_0503680/) — 2026-08-31
- [14] [Minimax rates for heterogeneous causal effect estimation](/research-news/deep_reads/2026-07-04-10.1214_24-aos2369/) — Annals of Statistics · 2026-07-04
- [15] [Statistical Inference for Smoothed Support Vector Machines in High Dimensions: From Offline to Online Data](/research-news/deep_reads/2026-05-18-2605.15911/) — 2026-05-18
- [16] [An Online Meta-Level Adaptive Design Framework with Targeted Learning Inference: Applications to Evaluating and Utilizing Surrogate Outcomes in Adaptive Designs](/research-news/deep_reads/2026-05-26-10.1080_01621459.2026.2657052/) — Journal of the American Statistical Association · 2026-05-26
- [17] [Decorrelated Local Linear Estimator: Inference for Non-linear Effects in High-dimensional Additive Models](/research-news/deep_reads/2026-05-26-jmlr_v27_22-1436/) — JMLR · 2026-05-26
- [18] [Generalized linear spectral statistics of high-dimensional sample covariance matrices and its applications](/research-news/deep_reads/2026-05-26-10.1214_25-aos2601/) — Annals of Statistics · 2026-05-26
- [19] [Information theoretic limits of robust sub-Gaussian mean estimation under star-shaped constraints](/research-news/deep_reads/2026-05-26-10.1214_25-aos2576/) — Annals of Statistics · 2026-05-26
- [20] [On propensity score matching with a diverging number of matches](/research-news/deep_reads/2026-05-26-10.1093_biomet_asae026/) — Biometrika · 2026-05-26
- [21] [Minimax rates of convergence for nonparametric location-Scale models](/research-news/deep_reads/2026-06-07-10.1016_j.jeconom.2026.106187/) — Journal of Econometrics · 2026-06-07
- [22] [Nonparametric Causal Inference with Functional Covariates](/research-news/deep_reads/2026-06-07-10.1080_07350015.2025.2501563/) — Journal of Business & Economic Statistics · 2026-06-07
- [23] [A Temporal Spatial Minimax Rate for Smoothly-Varying Distributions in Wasserstein Space](/research-news/deep_reads/2026-06-08-2606.07325/) — 2026-06-08
- [24] [HSCI: Neyman-Orthogonal Causal Inference under High-Dimensional Proportional Hazards](/research-news/deep_reads/2026-06-12-2606.14132/) — 2026-06-12
- [25] [Paired Sample Tests for High-dimensional Uncorrelatedness via Random Integration](/research-news/deep_reads/2026-06-17-2606.15636/) — 2026-06-17
- [26] [Asymptotic normality of log likelihood ratio and fundamental limit of the weak detection for spiked Wigner matrices](/research-news/deep_reads/2026-06-18-10.3150_24-bej1805/) — Bernoulli · 2026-06-18
- [27] [Characterizing the minimax rate of nonparametric regression under bounded star-shaped constraints](/research-news/deep_reads/2026-06-18-10.1214_25-ejs2419/) — Electronic Journal of Statistics · 2026-06-18
- [28] [Hoeffding-type decomposition for U-statistics on bipartite networks](/research-news/deep_reads/2026-06-18-10.1214_25-ejs2402/) — Electronic Journal of Statistics · 2026-06-18
- [29] [Local goodness-of-fit testing for Hölder-continuous densities: Minimax rates](/research-news/deep_reads/2026-06-18-10.3150_24-bej1824/) — Bernoulli · 2026-06-18
- [30] [Assessing spillover effects: Handling missing outcomes in network-based studies](/research-news/deep_reads/2026-06-19-10.1177_09622802251382586/) — Statistical Methods in Medical Research · 2026-06-19

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

