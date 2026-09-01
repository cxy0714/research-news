# 选题提案 · 非参数回归的极小极大率刻画

**战线范围**: 在随机设计、流形、星形约束等不同函数类下，刻画非参数回归/估计的极小极大收敛率，使用度量熵、Fano不等式、Le Cam方法等工具。  
**证据论文**: 30 篇（★ 收藏 22 篇）  
**提案条数**: 2  
**生成日期**: 2026-09-01  

> 每条提案的证据都点名来源论文 [k] 并引其原话。**不打分、不排名**——「证据 N 篇」是可数的事实，不是质量分。标了 ⚠️ 单点证据的条目只有一篇论文支撑，自己掂量。

---

### 提案 1：High-Dimensional Minimax Rates for Nonparametric Causal Functionals under Smoothness Constraints

- **claim（一句话）**：刻画当协变量维数 \(d = d_n\) 随样本量增长时，条件平均处理效应（CATE）及平均处理效应（ATE）等非参数因果泛函的 minimax 收敛率，并构造达到该率的估计量。

- **最小内核**：先考虑 \(d = O(\log n)\) 且 CATE 为 Hölder 光滑（光滑度 \(\beta\)）的最简特例，此时倾向得分和结果回归均为 \(d\) 维 Hölder 类。在此特例下，要证的命题退化为：minimax 率是否为 \(n^{-2\beta/(2\beta+d)} + n^{-1/2}\) 的某种插值，且当 \(d\) 增长时是否出现“维数诅咒”的显式退化。

- **证据**：
  - [6] 开放问题 2：“如何扩展到更高维？” 扎根于 Introduction 中 “Our work is distinct from this stream of literature as we do not posit high dimensional models”，但同时又指出 “such models are allowed”，说明高维扩展是待解决问题。
  - [23] 开放问题 2：“当 \(d\) 随样本量增长时（例如 \(d = O(n^\alpha)\)），minimax 速率会如何变化？是否存在‘维数诅咒’之外的额外困难？” 扎根于 Section 5：“Extensions to high-dimensional settings are also of interest.”
  两篇独立论文均点名高维协变量下因果泛函 minimax 率刻画为开放问题。

- **为什么现在**：[23] 已建立固定 \(d\) 下 CATE 的 minimax 率（含手肘现象），[6] 已建立固定 \(d\) 下 ATE 的 structure-agnostic 最优率。这些固定维结果提供了高维扩展的基准，且近年高维非参数回归的局部熵技术（如 [29] 的星形约束框架）已成熟，使从固定维到增长维的推广成为可能。

- **武器匹配**：用 **高维渐近** 工具分析 \(d\) 增长时局部熵的临界方程，结合 **非参数统计** 中的度量熵下界技术（Fano 不等式、Le Cam 方法）推导下界；用 **因果推断中的估计理论**（如局部多项式 R-Learner）构造上界。

- **风险与竞争**：可能已被 Kato (2025) 或 Mukherjee & Sen (2026) 部分解决。需查 arXiv 上近一年关于“high-dimensional CATE minimax”或“nonparametric regression with diverging dimension”的预印本，以及 Belloni et al. (2017) 的高维条件矩估计工作。若假设过强（如要求倾向得分稀疏），则结果可能不具一般性。

- **交付形态**：`定理型`

- **第一周动作**：
  1. 读 [23] Section 2-3，摘出固定 \(d\) 下 CATE minimax 率的证明结构（下界构造与上界估计量）。
  2. 读 [6] Theorem A.1 及开放问题 2 的上下文，明确其高维扩展的具体困难（核平滑退化）。
  3. 读 [29] Section 3-4，学习局部熵临界方程在星形约束类上的应用，评估能否直接用于 Hölder 类。
  4. 写出当 \(d = \log n\) 时，CATE 下界的初步 Fano 构造（需将 [23] 的构造推广到高维）。
  5. 检查 [23] 的局部多项式 R-Learner 在 \(d\) 增长时的偏差-方差分解，看是否出现 \(d/n\) 项。

---

### 提案 2：Statistical-Computational Tradeoffs in Low-Rank Matrix/Tensor Estimation: A Low-Degree Polynomial Approach

- **claim（一句话）**：在共享子空间估计（[3]）和交错张量双线性形式估计（[8]）两个设定下，证明存在统计-计算间隙：信息论最优率需要指数时间算法才能达到，而多项式时间算法只能达到更慢的率，并用低度多项式障碍（low-degree polynomial barrier）刻画该间隙。

- **最小内核**：先考虑最简单的矩阵情形：两个矩阵共享一个 \(r\) 维左奇异子空间，噪声为同方差高斯，且谱分离条件恰好处于信息论可恢复但多项式时间困难的阈值。在此特例下，要证的命题退化为：低度多项式方法（如谱方法）的 SNR 阈值是否严格高于信息论阈值，且该间隙是否由 \(r\) 和矩阵维度的比值决定。

- **证据**：
  - [3] 开放问题 4：“验证 Conjecture 1：计算下界基于低度多项式猜想，是否可用 SQ 或 SoS 给出独立证据？” 扎根于 3.1 节 Conjecture 1 及 Theorem 4 的陈述。
  - [8] 开放问题 4：“计算-统计权衡：Algorithm 3（块状聚合）与 Algorithm 4（线性聚合）的权衡是否是本质的？是否存在一个算法能同时达到最优的统计效率和 \(O(o_k)\) 的计算复杂度？” 扎根于 Appendix B.1 中对两种算法的讨论及 Figure 5。
  两篇独立论文均明确点名计算-统计权衡为开放问题，且均涉及低秩结构。

- **为什么现在**：[3] 已提出低度多项式猜想作为计算下界的候选，[8] 已给出两种算法并展示权衡。近期低度多项式方法在 spiked Wigner 模型和 tensor PCA 上的成功（如 Kunisky et al., 2019）提供了现成的技术工具，使将 [3] 的猜想与 [8] 的权衡统一分析成为可能。

- **武器匹配**：用 **高阶 U 统计量的计算（treewidth / tensor contraction / einsum）** 来构造低度多项式检验统计量，并计算其矩；用 **估计问题的 minimax 下界** 技术（Fano 法）推导信息论下界，与低度多项式下界对比。

- **风险与竞争**：低度多项式方法在矩阵/张量问题上的应用已有大量工作（如 Perry et al., 2020; Brennan & Bresler, 2020），需确认 [3] 的共享子空间设定是否已被覆盖。需查 arXiv 上近一年关于“low-degree polynomial for subspace estimation”的论文。若 [3] 的 Conjecture 1 已被证明或证伪，则选题需调整。

- **交付形态**：`定理型`

- **第一周动作**：
  1. 读 [3] Section 3.1，理解 Conjecture 1 的精确陈述及 Theorem 4 的计算下界形式。
  2. 读 [8] Appendix B.1，摘出两种算法的计算复杂度与统计误差的显式表达式。
  3. 读 Kunisky et al. (2019) “Low-degree polynomials in high-dimensional statistics” 的 Section 2-3，掌握低度多项式下界的标准推导步骤。
  4. 针对 [3] 的共享子空间模型，写出低度多项式检验统计量的二阶矩表达式（用 tensor contraction 表示）。
  5. 针对 [8] 的双线性形式估计，写出信息论下界（用 Fano 法）与低度多项式下界的初步对比，看是否出现间隙。

---

### 本页的证据论文

- [1] ★ [Optimally taming biases in black-box models for efficient semiparametric estimation](/research-news/deep_reads/2026-06-05-2606.06368/) — 2026-06-05
- [2] ★ [Optimal Estimation of Shared Singular Subspaces Across Multiple Noisy Matrices](/research-news/deep_reads/2026-06-05-10.1109_tit.2026.3667733/) — IEEE Transactions on Information Theory · 2026-06-05
- [3] ★ [Statistically and Computationally Optimal Estimation and Inference of Common Subspaces](/research-news/deep_reads/2026-06-05-2606.06483/) — 2026-06-05
- [4] ★ [Adaptive Estimation of Aggregated Values of Conditional Linear Programs](/research-news/deep_reads/2026-06-09-2606.08359/) — 2026-06-09
- [5] ★ [Binary regression and classification with covariates in metric spaces](/research-news/deep_reads/2026-06-19-10.1093_biomtc_ujaf123/) — Biometrics · 2026-06-19
- [6] ★ [Doubly-robust inference and optimality in structure-agnostic models with smoothness](/research-news/deep_reads/2026-06-19-2405.08525/) — 2026-06-19
- [7] ★ [Thin Sets Are Not Equally Thin: Minimax Learning of Submanifold Integrals](/research-news/deep_reads/2026-06-22-2507.12673/) — 2026-06-22
- [8] ★ [Direct and efficient estimation of bilinear forms in staggered tensor panels](/research-news/deep_reads/2026-07-09-2607.06330/) — 2026-07-09
- [9] ★ [On Rates Attainable under Random Design: A Negative Answer to a Problem of Robins](/research-news/deep_reads/2026-07-15-2607.13170/) — 2026-07-15
- [10] ★ [Structural mean models for instrumented difference-in-differences](/research-news/deep_reads/2026-07-15-10.1214_24-ejs2313/) — Electronic Journal of Statistics · 2026-07-15
- [11] ★ [On the structural dimension of sliced inverse regression](/research-news/deep_reads/2026-05-26-10.1214_25-aos2505/) — Annals of Statistics · 2026-05-26
- [12] ★ [Symmetry: A general structure in nonparametric regression](/research-news/deep_reads/2026-05-26-10.1214_25-aos2529/) — Annals of Statistics · 2026-05-26
- [13] ★ [Fast Near-Optimal Estimation over Symmetric Norm Balls](/research-news/deep_reads/2026-06-02-2606.01554/) — 2026-06-02
- [14] ★ [Generalized nonparametric regression in reproducing kernel Hilbert spaces: Consistency and rates of convergence](/research-news/deep_reads/2026-06-24-2606.22993/) — 2026-06-24
- [15] ★ [A simple adaptive estimator of the integrated square of a density](/research-news/deep_reads/2026-07-17-0803.0847/) — 2026-07-17
- [16] ★ [Compound Selection Decisions: An Almost SURE Approach](/research-news/deep_reads/2026-07-30-2511.11862/) — 2026-07-30
- [17] ★ [Incremental effects for continuous exposures](/research-news/deep_reads/2026-08-31-2409.11967/) — 2026-08-31
- [18] ★ [On Estimation of $L_{r}$-Norms in Gaussian White Noise Models](/research-news/deep_reads/2026-07-17-1710.03863/) — 2026-07-17
- [19] ★ [A Tutorial on Bregman Projection in Statistics](/research-news/deep_reads/2026-07-07-2606.21714/) — 2026-07-07
- [20] ★ [Gradient-free stochastic optimization of derivatives under strong convexity](/research-news/deep_reads/2026-07-10-2607.07249/) — 2026-07-10
- [21] ★ [Nonparametric estimation of scalar diffusions based on low frequency data](/research-news/deep_reads/2026-08-31-math_0503680/) — 2026-08-31
- [22] ★ [Personalizing black-box models for nonparametric regression with minimax optimality](/research-news/deep_reads/2026-07-14-2601.01432/) — 2026-07-14
- [23] [Minimax rates for heterogeneous causal effect estimation](/research-news/deep_reads/2026-07-04-10.1214_24-aos2369/) — Annals of Statistics · 2026-07-04
- [24] [Dualizing Le Cam’s method for functional estimation I: General theory](/research-news/deep_reads/2026-05-26-10.1214_25-aos2498/) — Annals of Statistics · 2026-05-26
- [25] [Information theoretic limits of robust sub-Gaussian mean estimation under star-shaped constraints](/research-news/deep_reads/2026-05-26-10.1214_25-aos2576/) — Annals of Statistics · 2026-05-26
- [26] [The Distribution of Ridgeless Least Squares Interpolators](/research-news/deep_reads/2026-05-26-jmlr_v27_25-0458/) — JMLR · 2026-05-26
- [27] [Minimax rates of convergence for nonparametric location-Scale models](/research-news/deep_reads/2026-06-07-10.1016_j.jeconom.2026.106187/) — Journal of Econometrics · 2026-06-07
- [28] [A Temporal Spatial Minimax Rate for Smoothly-Varying Distributions in Wasserstein Space](/research-news/deep_reads/2026-06-08-2606.07325/) — 2026-06-08
- [29] [Characterizing the minimax rate of nonparametric regression under bounded star-shaped constraints](/research-news/deep_reads/2026-06-18-10.1214_25-ejs2419/) — Electronic Journal of Statistics · 2026-06-18
- [30] [Local goodness-of-fit testing for Hölder-continuous densities: Minimax rates](/research-news/deep_reads/2026-06-18-10.3150_24-bej1824/) — Bernoulli · 2026-06-18

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

