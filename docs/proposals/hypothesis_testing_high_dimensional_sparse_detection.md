# 选题提案 · 高维稀疏信号检测与相变

**战线范围**: 研究高维稀疏信号（如子矩阵、图模型、Ising模型）的极小极大检测边界与计算-统计相变，常用Higher Criticism、似然比、二阶矩方法。  
**证据论文**: 30 篇（★ 收藏 9 篇）  
**提案条数**: 2  
**生成日期**: 2026-09-01  

> 每条提案的证据都点名来源论文 [k] 并引其原话。**不打分、不排名**——「证据 N 篇」是可数的事实，不是质量分。标了 ⚠️ 单点证据的条目只有一篇论文支撑，自己掂量。

---

### 提案 1：Low-Degree Polynomial Barriers for Sparse Signal Detection in the Curie-Weiss Ising Model

- **claim（一句话）**：证明在 Curie-Weiss Ising 模型下，当信号稀疏度 \(\alpha < 1/2\) 时，任何度数 \(D = o(\log n)\) 的低度多项式检验都无法达到信息论最优检测边界（即存在严格统计-计算间隙），并刻画间隙的精确阈值。

- **最小内核**：考虑最简单的 Curie-Weiss 模型（全连接，\(p=2\)，已知逆温度 \(\beta\)），检测是否存在稀疏非零磁场：\(H_0: \mu = 0\) vs \(H_1: \mu \in \Theta(s, B)\)，其中 \(s = n^{1-\alpha}\)，\(B\) 为信号强度。信息论检测边界由 [8] 给出：当 \(\beta \le 1\) 时，可检测条件为 \(B \gg \sqrt{2} n^{-1/2} s^{1/2}\)；当 \(\beta > 1\) 时，为 \(B \gg \sqrt{2\cosh(\beta m)} n^{-1/2} s^{1/2}\)。本提案要证：对于任何低度多项式检验（度数 \(D = o(\log n)\)），可检测所需信号强度至少为 \(B \gg n^{-1/2} s^{1/2} \cdot \omega(1)\)，即存在一个常数因子间隙。

- **证据**：
  - [7] 开放问题 4：“与计算复杂度的连接...是否存在统计-计算权衡？例如，在临界点，能否证明任何多项式时间算法都无法达到信息论最优的检测边界？” 扎根于本文完全未讨论计算问题。
  - [25] 开放问题 4：“统计-计算权衡...在 \(\theta_N \sim N^{-2/3}\) 或更稀疏时，达到 \(1/\sqrt{\theta_N}\) 估计率或 \(\sqrt{\theta_N}\) 检测率，是否需要超多项式时间？是否存在 low-degree polynomial barrier？” 扎根于 Intro 1.3 节提到 CS 领域的结构学习，但未讨论单样本推断的 stat-comp gap。
  - [15] 开放问题 4：“计算与统计的权衡...SST 若对一般 \(s\) 做穷举，计算复杂度是 \(\binom{p}{s}\)，不可行。能否设计计算可行的检验（如利用 einsum 树宽来降低计算张量收缩的复杂度）同时达到（或逼近）minimax 界？” 扎根于论文只讨论了 \(s\) 为小常数时的可行性。

- **为什么现在**：近期 [2] 在 shuffled linear regression 中建立了低度多项式下界（定理 1），[13] 在随机块模型中证明了 KS 界的紧性（定理 2），这些技术（低度多项式方法、树耦合、第二矩方法）已成熟到可以迁移到 Ising 模型。同时 [8] 给出了 Curie-Weiss 模型下信息论检测的尖锐常数（定理 1-2），为下界提供了精确基准。

- **武器匹配**：使用“高阶 U 统计量的计算（treewidth / tensor contraction / einsum）”来显式表示低度多项式检验统计量（其核为 \(\prod_{i \in S} X_i\)，是 \(D\) 阶 U 统计量），并利用“非参数统计”中的 minimax 下界技巧（如 Le Cam 引理、Fano 不等式）证明信息论下界。具体：用 einsum 计算低度多项式统计量在零假设和备择假设下的前两阶矩，证明其矩无法区分 \(H_0\) 和 \(H_1\) 当信号强度低于某个阈值。

- **风险与竞争**：可能已被 [7] 或 [25] 的作者后续工作处理。需检查 Bhattacharya & Mukherjee (2015) 之后是否有论文直接证明 Ising 模型下的低度多项式障碍。另外，Koehler & Mossel (2021) 在树上研究了低度多项式硬度，但 Curie-Weiss 模型是全连接，结果可能不同。建议搜索“low-degree polynomial Ising model detection”确认未被抢先。

- **交付形态**：`定理型`

- **第一周动作**：
  1. 读 [7] Section 2.2.2 关于临界温度的启发式论证，理解信息论下界结构。
  2. 读 [2] 定理 1 的证明（LDP 下界），掌握低度多项式方法的核心步骤（矩匹配、超可加性）。
  3. 读 [13] 的树耦合技术（Section 3），看能否用于 Curie-Weiss 模型（全连接图可视为树极限）。
  4. 写出 Curie-Weiss 模型下低度多项式检验的显式形式：统计量 \(T_D = \sum_{|S| \le D} w_S \prod_{i \in S} X_i\)，其中 \(w_S\) 为系数。
  5. 计算 \(T_D\) 在 \(H_0\) 和 \(H_1\) 下的前两阶矩（利用 Ising 模型的高斯逼近或鞍点近似），初步判断矩是否可区分。

---

### 提案 2：Adaptive Sparse Signal Detection Under Unknown Dependence in the Ising Model on a Cycle Graph

- **claim（一句话）**：构造一个对未知耦合强度 \(\beta\) 自适应的稀疏信号检测检验，在环图 Ising 模型下达到 minimax 最优检测边界（与已知 \(\beta\) 时相同），并证明其最优性。

- **最小内核**：考虑环图（cycle graph）上的 Ising 模型，已知图结构但未知耦合强度 \(\beta\)（铁磁，\(\beta > 0\)）。检测是否存在稀疏磁场：\(H_0: \mu = 0\) vs \(H_1: \mu \in \Theta(s, B)\)，其中 \(s = n^{1-\alpha}\)。已知 \(\beta\) 时，[8] 定理 6 给出检测边界：可检测条件为 \(B \gg \sqrt{2\chi(\beta)} n^{-1/2} s^{1/2}\)，其中 \(\chi(\beta) = (1 - \tanh \beta)/(1 + \tanh \beta)\) 是磁化率。本提案要构造一个检验，在 \(\beta\) 未知时仍达到该边界（至多常数因子）。

- **证据**：
  - [4] 开放问题 1：“未知 \(\lambda\) 时的检测阈值...对于 \(\alpha > 1/2\)，阈值不变；但对于 \(\alpha \le 1/2\)，可能需改用度方差检验。” 扎根于 Section 5。
  - [5] 开放问题 1：“未知依赖结构 \(Q\) 下的检验...能否构造对 \(Q\) 的估计误差鲁棒的检验？” 扎根于 Section 5。
  - [8] 开放问题 2：“格子模型下低温自由边界条件的严格证明...定理 6 在 \(\beta > \beta_c\) 时只对正边界条件成立。能否将结果推广到自由边界条件？” 扎根于 Section 3。虽然此条更偏向边界条件，但环图无相变，可视为自由边界条件的特例。

- **为什么现在**：[8] 给出了环图下已知 \(\beta\) 时的尖锐检测常数（定理 6 的证明依赖于 \(\chi(\beta)\) 的显式表达式），[4] 在 \(\beta\)-模型下讨论了未知 \(\lambda\) 时的检测阈值，[5] 在一般 Ising 模型下假设 \(Q\) 已知。这些工作为自适应检验提供了基准。此外，[7] 在高温区给出了自适应检验（Theorem 2.2），但环图无相变（\(\beta\) 任意大时仍可检测），因此需要覆盖全参数空间。

- **武器匹配**：使用“非参数统计”中的经验似然或交叉验证方法估计 \(\beta\)，结合“高维渐近”中的极值理论（如最大值收敛到 Gumbel 分布）。具体：用最大伪似然估计（MPLE）估计 \(\beta\)（计算复杂度 \(O(n)\)），然后代入已知 \(\beta\) 时的最优检验统计量（基于总和 \(S_n = \sum_i X_i\)），分析估计误差对检验势的影响，证明当 \(n\) 足够大时，估计误差可忽略。

- **风险与竞争**：可能已被 [8] 的自适应检验覆盖（[8] 定理 2 和 4 给出了自适应检验，但要求 \(\|\mu\|_\infty = O(1)\) 且只针对平均场和格子模型，未覆盖环图）。需检查 [8] 是否处理了环图（其 Section 3 只讨论了格子模型）。另外，[7] 的自适应检验只适用于高温区（\(\beta < \beta_c\)），而环图无相变，因此低温区是空白。建议搜索“adaptive testing Ising model cycle graph”确认。

- **交付形态**：`方法+模拟型`

- **第一周动作**：
  1. 读 [8] Section 3 关于自适应检验的构造（两阶段测试：先估计 \(\beta\) 是否大于 1，再使用相应检验）。
  2. 读 [4] Section 5 关于未知 \(\lambda\) 的讨论，特别是度方差检验的构造。
  3. 读 [5] Section 5 关于未知 \(Q\) 的讨论，理解鲁棒性要求。
  4. 在环图设定下，推导已知 \(\beta\) 时基于总和 \(S_n\) 的检验的检测边界（利用 [8] 的 \(\chi(\beta)\) 表达式）。
  5. 设计一个两阶段检验：第一阶段用 MPLE 估计 \(\hat{\beta}\)，第二阶段用 \(S_n\) 检验，阈值设为 \(\sqrt{2\chi(\hat{\beta})} n^{-1/2} s^{1/2} \cdot c\)，分析 Type I error 控制（需证明 \(\hat{\beta}\) 的收敛速率足够快）。

---

### 本页的证据论文

- [1] ★ [Sharp minimax risks and phase transitions in sparse submatrix detection](/research-news/deep_reads/2026-06-01-2605.31583/) — 2026-06-01
- [2] ★ [A Computational Transition for Detecting Multivariate Shuffled Linear Regression by Low-Degree Polynomials](/research-news/deep_reads/2026-06-05-10.1109_tit.2026.3659093/) — IEEE Transactions on Information Theory · 2026-06-05
- [3] ★ [Direct and efficient estimation of bilinear forms in staggered tensor panels](/research-news/deep_reads/2026-07-09-2607.06330/) — 2026-07-09
- [4] ★ [Detection Thresholds for the $β$-Model on Sparse Graphs](/research-news/deep_reads/2026-07-17-1608.01801/) — 2026-07-17
- [5] ★ [Global Testing Against Sparse Alternatives under Ising Models](/research-news/deep_reads/2026-07-17-1611.08293/) — 2026-07-17
- [6] ★ [Hypothesis testing for high-dimensional sparse binary regression](/research-news/deep_reads/2026-07-17-1308.0764/) — 2026-07-17
- [7] ★ [On Testing for Parameters in Ising Models](/research-news/deep_reads/2026-07-17-1906.00456/) — 2026-07-17
- [8] ★ [Sharp Signal Detection Under Ferromagnetic Ising Models](/research-news/deep_reads/2026-07-17-2110.02949/) — 2026-07-17
- [9] ★ [Double zero-inflated spatio-temporal modeling of daily precipitation under detection thresholds](/research-news/deep_reads/2026-07-07-2606.17717/) — 2026-07-07
- [10] [Regularity, Phase Transitions, and Uniform Inference for Proximal Counterfactual Quantile Processes](/research-news/deep_reads/2026-05-12-2605.09257/) — 2026-05-12
- [11] [Doubly Robust Pointwise Confidence Intervals for a Monotonic Continuous Treatment Effect Curve](/research-news/deep_reads/2026-05-26-10.1080_01621459.2026.2639735/) — Journal of the American Statistical Association · 2026-05-26
- [12] [Asymptotic limits of spiked eigenvalues and eigenvectors of signal-plus-noise matrices with weak signals and heteroskedastic noise](/research-news/deep_reads/2026-06-18-10.3150_24-bej1808/) — Bernoulli · 2026-06-18
- [13] [Exact phase transitions for stochastic block models and reconstruction on trees](/research-news/deep_reads/2026-06-18-10.1214_24-aop1723/) — Annals of Probability · 2026-06-18
- [14] [Semi-Parametric Estimation of Potential Outcome Distributions and General Causal Estimands by Borrowing Information from Both Treatments and Controls](/research-news/deep_reads/2026-06-19-10.5705_ss.202025.0267/) — Statistica Sinica · 2026-06-19
- [15] [Minimax detection boundary and sharp optimal test for Gaussian graphical models](/research-news/deep_reads/2026-06-20-10.1093_jrsssb_qkae029/) — Journal of the Royal Statistical Society Series B · 2026-06-20
- [16] [Power enhancement and phase transitions for global testing of the mixed membership stochastic block model](/research-news/deep_reads/2026-06-23-10.3150_22-bej1519/) — Bernoulli · 2026-06-23
- [17] [Sample canonical correlation coefficients of high-dimensional random vectors with finite rank correlations](/research-news/deep_reads/2026-06-23-10.3150_22-bej1525/) — Bernoulli · 2026-06-23
- [18] [Sparse signal detection in heteroscedastic Gaussian sequence models: Sharp minimax rates](/research-news/deep_reads/2026-06-23-10.3150_23-bej1667/) — Bernoulli · 2026-06-23
- [19] [Spiked eigenvalues of noncentral Fisher matrix with applications](/research-news/deep_reads/2026-06-23-10.3150_22-bej1579/) — Bernoulli · 2026-06-23
- [20] [A CLT for the LSS of large-dimensional sample covariance matrices with diverging spikes](/research-news/deep_reads/2026-07-04-10.1214_23-aos2333/) — Annals of Statistics · 2026-07-04
- [21] [Statistical inference in tensor completion: Optimal uncertainty quantification and statistical-to-computational gaps](/research-news/deep_reads/2026-07-04-10.1214_25-aos2617/) — Annals of Statistics · 2026-07-04
- [22] [On the phase transition of Wilks’ phenomenon](/research-news/deep_reads/2026-07-06-10.1093_biomet_asaa078/) — Biometrika · 2026-07-06
- [23] [Block-Independent Likelihood Ratio Testing for High-Dimensional Mean Vectors with Applications to Matrix-Variate Data](/research-news/deep_reads/2026-05-22-2605.21848/) — 2026-05-22
- [24] [Inference for possibly misspecified generalized linear models with nonpolynomial-dimensional nuisance parameters](/research-news/deep_reads/2026-05-26-10.1093_biomet_asae024/) — Biometrika · 2026-05-26
- [25] [Ising Models on Inhomogeneous Random Graphs: Inference, Local Asymptotic Minimaxity, and Limit of Experiments](/research-news/deep_reads/2026-06-08-2606.07065/) — 2026-06-08
- [26] [Phase transition of Schott's statistic for high-dimensional heavy-tailed data](/research-news/deep_reads/2026-06-13-2606.12943/) — 2026-06-13
- [27] [Detecting spectral breaks in spiked covariance models](/research-news/deep_reads/2026-06-18-10.3150_25-bej1900/) — Bernoulli · 2026-06-18
- [28] [Kernel two-sample tests for manifold data](/research-news/deep_reads/2026-06-18-10.3150_23-bej1685/) — Bernoulli · 2026-06-18
- [29] [Phase transitions of the maximum likelihood estimators in the p-spin Curie-Weiss model](/research-news/deep_reads/2026-06-18-10.3150_24-bej1779/) — Bernoulli · 2026-06-18
- [30] [Minimax rate of estimation for invariant densities associated to continuous stochastic differential equations over anisotropic Hölder classes](/research-news/deep_reads/2026-06-19-10.1111_sjos.12735/) — Scandinavian Journal of Statistics · 2026-06-19

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

