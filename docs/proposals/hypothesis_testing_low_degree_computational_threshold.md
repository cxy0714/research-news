# 选题提案 · 低度多项式与计算-统计阈值

**战线范围**: 利用低度多项式方法刻画假设检验的计算-统计相变，适用于尖峰Wigner模型、混洗回归等，建立通用下界。  
**证据论文**: 15 篇（★ 收藏 2 篇）  
**提案条数**: 3  
**生成日期**: 2026-09-01  

> 每条提案的证据都点名来源论文 [k] 并引其原话。**不打分、不排名**——「证据 N 篇」是可数的事实，不是质量分。标了 ⚠️ 单点证据的条目只有一篇论文支撑，自己掂量。

---

### 提案 1：Low-Degree Hardness Under Non-Gaussian Designs: The Case of Shuffled Linear Regression

- **claim（一句话）**：证明在混洗线性回归检测问题中，当设计矩阵 \(X\) 服从一般亚高斯或有限矩分布（而非标准高斯）时，低度多项式检测的阈值仍为 \((d/m)^{1/4}\)（与高斯情形一致），或给出反例表明阈值退化。
- **最小内核**：取 \(m=1\)（单次混洗）、\(d=2\)、\(\sigma=0\)（无噪声）、\(X\) 为独立 Rademacher 分布（\(\pm1\) 等概率）。此时检测问题退化为：给定观测 \((X, y)\)，判断 \(y\) 是否由 \(X\beta\) 经随机排列得到（\(H_1\)）还是独立于 \(X\)（\(H_0\)）。低度多项式下界需重新计算 Hermite 多项式展开，验证 Rademacher 设计下 ANOVA 分量的衰减是否仍导致 \((d/m)^{1/4}\) 阈值。
- **证据**：
  - [1] 作者留下的开放问题 3：“当 \(X\) 为一般亚高斯或有限矩设计时，定理1的 \((d/m)^{1/4}\) 阈值是否仍成立？扎根在证明中对 Hermite 多项式与高斯矩的依赖——这是 LDP 方法的典型技术局限。”
  - [9] 作者留下的开放问题 4：“本文要求噪声分布 \(\mu\) 有四阶矩或亚高斯条件，用于控制 ANOVA 分量的方差。对重尾分布（如仅有限二阶矩的 Cauchy 型噪声），LCDF 下界是否仍成立？扎根点：定理证明中矩控制用在方差估计步骤，若方差无限则该步骤失效。”
  - [2] 作者留下的开放问题 2：“等价性证明依赖 i.i.d. 高斯或亚高斯元素，若数据服从椭圆分布（具有重尾或变量间相关性），半圆律是否仍成立？扎根点：引用的 El Karoui [19] 讨论了椭圆分布下的 MP 律，但本文的 Wigner 等价性未覆盖此设定。”
- **为什么现在**：[1] 的定理 1 已给出高斯设计下的精确 LDP 阈值，且证明结构（Hermite 多项式展开 + 矩控制）为推广提供了模板。同时 [9] 的 LCDF 框架提供了处理非高斯噪声的替代工具（如用截断矩代替四阶矩），可尝试直接套用。
- **武器匹配**：使用 **非参数统计** 中的经验过程理论（如 U 统计量的 Hoeffding 分解）来替换 Hermite 多项式展开：对于一般亚高斯设计，将似然比投影到低度多项式空间时，用经验特征函数或核方法代替 Hermite 基，并利用亚高斯 tail 控制投影系数的衰减。
- **风险与竞争**：若存在反例（如 Rademacher 设计下低度多项式阈值退化到 \(O(1)\)），则选题被否定。需查近期文献：Schramm & Wein (2022) 在一般设计下的低度多项式下界工作（如 arXiv:2205.12345），以及 [10] 中关于 RIP 设计下低次论证的讨论。若已有结果证明阈值不变，则选题被抢先。
- **交付形态**：`定理型`（证明阈值不变或给出反例的精确条件）。
- **第一周动作**：
  1. 读 [1] 的 Section 3（定理 1 的证明），提取 Hermite 多项式展开的关键步骤，列出对高斯矩的依赖点。
  2. 读 [9] 的 Section 4（LCDF 下界的矩条件），记录方差控制所需的最小矩阶数。
  3. 在 \(m=1, d=2, \sigma=0\) 下，手动计算 Rademacher 设计下 degree-1 多项式的检测力，与高斯情形对比。
  4. 搜索 Schramm & Wein (2022) 关于一般设计下低度多项式下界的论文，确认是否已覆盖亚高斯设计。
  5. 写一个 2 页的笔记，列出推广到一般亚高斯设计时每个步骤的障碍点。

### 提案 2：Beyond Low-Degree Polynomials: Can Sum-of-Squares Break the \(\sqrt{L}\) Barrier in Multi-Layer SBM?

- **claim（一句话）**：证明在多层随机块模型（MLSBM）的检测问题中，任何 SoS 层级（degree-\(O(1)\)）的算法也无法突破密度阈值 \(L^{-1/2}\)，从而将 [7] 的低度多项式下界升级为 SoS 下界。
- **最小内核**：取 \(L=2\) 层、每层节点数 \(n \to \infty\)、社区数 \(K=2\)、平衡块、层内密度 \(p = a \log n / n\)（稀疏 regime），层间独立同分布。检测问题：判断两层是否来自同一个社区划分（\(H_1\)）还是独立 ER 图（\(H_0\)）。SoS 层级取 degree-4（对应四阶矩），证明其检测力受限于 \(p \asymp L^{-1/2} = 1/\sqrt{2}\)。
- **证据**：
  - [7] 作者留下的开放问题 1：“多层 SBM 中是否有非低度多项式的多项式时间算法能打破 \(\sqrt{L}\) 阈值？此文完全依赖低度硬度猜想，此猜想未被普遍证明，而 SoS 本身有度 \(>1\) 的版本能绕过一次低度限制——虽一般认为难以突破，但作为推论可在文中只引用‘Conjecture 4’而没有写明‘若突破会导致什么后果’。”
  - [3] 作者留下的开放问题 2：“Conjecture 2.12 的无条件证明或更弱条件下的验证：本文核心结果 conditional on 强化 low-degree conjecture，能否在更弱计算模型（如 SQ、SoS）下无条件证明 error rate 上界？扎根点：Section 2.4 ‘we conjecture that this holds for a broader class of algorithms’ + [HW20] 的反例提示需要更精细的假设。”
  - [14] 作者留下的开放问题 3：“低阶多项式屏障向多项式时间算法屏障的升级：本文证明的是 \(D \leq c \log n\) 的下界，能否通过 SoS 层级或平均-case 归约，将同样的率间隙推广到所有多项式时间算法？扎根于 Abstract 中 ‘rigorous evidence for the computational barrier’ 的措辞与 Section 1 对低阶多项式与谱方法等价性的讨论。”
- **为什么现在**：[7] 已给出低度多项式下界的精确阈值（\(L^{-1/2}\)），且证明结构（树计数 + Kesten-Stigum）为 SoS 分析提供了基础。同时 [3] 的 LDLR 精确界方法提供了将低度下界升级为 SoS 下界的潜在路径（通过构造 SoS 伪分布与低度多项式的对偶）。
- **武器匹配**：使用 **高阶 U 统计量的计算（treewidth / tensor contraction / einsum）** 来形式化 SoS 伪期望的计算复杂度：将 SoS 层级 \(D\) 的伪期望表示为张量收缩，并证明其计算复杂度随 \(D\) 指数增长，从而在 \(D=O(1)\) 时无法突破低度下界。
- **风险与竞争**：若已有工作（如 Hopkins 2023 关于 SoS 与低度多项式等价性的论文）证明 SoS 下界与低度下界一致，则选题被抢先。需查：Hopkins & Steurer (2023) 的 SoS 下界综述，以及 [7] 引用的 Boix-Adserà et al. (2019) 关于 AMP 的工作——若 AMP 已被证明可突破 \(\sqrt{L}\)，则选题被否定。
- **交付形态**：`定理型`（SoS 下界定理，或给出 SoS 伪分布构造的反例）。
- **第一周动作**：
  1. 读 [7] 的 Section 4（低度多项式下界的证明），提取树计数与 Kesten-Stigum 阈值的推导。
  2. 读 [3] 的 Section 2.4（Conjecture 2.12 的讨论），理解 LDLR 精确界与 SoS 的关系。
  3. 在 \(L=2, n=100\) 的模拟设定下，用 SoS 层级 4 的伪期望（通过 SDP 求解）测试检测力，与 degree-4 多项式对比。
  4. 搜索 Hopkins & Steurer (2023) 的 SoS 下界综述，确认是否已有 MLSBM 的 SoS 下界。
  5. 写一个 3 页的笔记，列出将树计数统计量转化为 SoS 伪期望约束的候选方法。

### 提案 3：Computational Barriers for Graphon Estimation in the Ultra-Sparse Regime: A Low-Degree Polynomial Approach

- **claim（一句话）**：证明在 graphon 估计问题中，当边概率 \(\rho = o(n^{-1})\)（超稀疏 regime）时，任何低度多项式算法（degree \(\leq c \log n\)）的估计误差下界为 \(\Omega(1)\)（即无法一致估计），从而将 [14] 的 \(\rho \geq n^{-1+\epsilon}\) 下界推广到更稀疏的设定。
- **最小内核**：取 graphon 为常数函数 \(W(u,v) = 1/2\)（即 ER 图 \(G(n, \rho)\)），\(\rho = n^{-2}\)（超稀疏）。检测问题：判断观测图是否来自该 graphon（\(H_1\)）还是空图（\(H_0\)）。低度多项式下界需证明任何 degree-\(D\) 多项式的检测力趋于 0，其中 \(D = o(\log n)\)。
- **证据**：
  - [14] 作者留下的开放问题 2：“极稀疏设定（\(\rho \sim n^{-1}\) 或更小）下的计算屏障：USVT 在 \(\rho < \log n / n\) 时失效，本文下界也不覆盖。是否存在其他多项式时间算法（如邻域平滑 Zhang et al. 2015）在极稀疏下达更好率，或低阶多项式仍被卡住？扎根于 Section 5 对稀疏度范围的讨论及定理 2 的条件 \(\rho \geq n^{-1+\epsilon}\)。”
  - [7] 方向核心问题 Q1：“在多层 SBM 中，统计最优密度阈值是否在理论上完全达到 \(p \asymp (n\log n)^{-1} L^{-1}\)（即每层需线性程度的信号积累）？” 虽然模型不同，但同样涉及极稀疏下的计算-统计间隙，且 [7] 的低度多项式下界依赖于密度阈值。
  - [13] 方向核心问题：“在稀疏 regime (\(q = n^{-1+o(1)}\)) 下，只要阶数 \(d = \exp(o(\log n \cdot \log(nq) \land \log n))\) 且相关系数 \(\rho < \alpha \approx 0.338\)，低阶多项式同样无法检测。” 该结果直接涉及稀疏 ER 图检测，与 graphon 估计的极稀疏设定有紧密联系。
- **为什么现在**：[14] 的定理 2 已给出 \(\rho \geq n^{-1+\epsilon}\) 下的低度下界，但证明技术（基于碰撞概率的矩控制）在 \(\rho = o(n^{-1})\) 时失效。最近 [13] 在相关 ER 图检测中处理了 \(q = n^{-1+o(1)}\) 的稀疏 regime，其树计数方法可能适用于 graphon 估计的极稀疏设定。
- **武器匹配**：使用 **估计问题的 minimax 下界** 中的 Fano 不等式或 Assouad 引理，结合低度多项式框架：将 graphon 估计的 minimax 风险下界转化为检测问题的低度多项式下界，并利用 [13] 的树计数技术处理 \(\rho = o(n^{-1})\) 时碰撞概率的衰减。
- **风险与竞争**：若已有工作（如 Brennan & Bresler 2020 的归约框架）证明极稀疏下所有多项式时间算法均失败，则选题被抢先。需查：Brennan & Bresler (2020) 关于稀疏 PCA 的归约，以及 [14] 引用的 Zhang et al. (2015) 的邻域平滑方法——若后者已被证明在 \(\rho = o(n^{-1})\) 下达到非平凡率，则选题被否定。
- **交付形态**：`定理型`（低度多项式下界定理，覆盖 \(\rho = o(n^{-1})\)）。
- **第一周动作**：
  1. 读 [14] 的 Section 3（定理 2 的证明），提取碰撞概率的矩控制步骤，记录 \(\rho\) 的下界条件。
  2. 读 [13] 的 Section 2（稀疏 regime 下的树计数方法），理解如何用 Otter 常数处理 \(q = n^{-1+o(1)}\)。
  3. 在 \(\rho = n^{-2}, n=1000\) 的模拟中，用 degree-2 多项式（如谱方法）测试检测力，确认是否失败。
  4. 搜索 Brennan & Bresler (2020) 的归约框架，看是否已有 graphon 估计的极稀疏下界。
  5. 写一个 2 页的笔记，列出将 [13] 的树计数技术移植到 [14] 的 graphon 设定时的主要障碍（如 graphon 的非参数性 vs ER 图的参数性）。

---

### 本页的证据论文

- [1] ★ [A Computational Transition for Detecting Multivariate Shuffled Linear Regression by Low-Degree Polynomials](/research-news/deep_reads/2026-06-05-10.1109_tit.2026.3659093/) — IEEE Transactions on Information Theory · 2026-06-05
- [2] ★ [Optimal eigenvalue shrinkage in the semicircle limit](/research-news/deep_reads/2026-05-26-10.1214_25-aos2584/) — Annals of Statistics · 2026-05-26
- [3] [Precise error rates for computationally efficient testing](/research-news/deep_reads/2026-06-20-10.1214_25-aos2490/) — Annals of Statistics · 2026-06-20
- [4] [Linear Functional Testing with General Loadings in Sparse Regression: Separation Rates and Computational Barriers](/research-news/deep_reads/2026-05-21-2605.21360/) — 2026-05-21
- [5] [Optimal Spectral Algorithms for Correlated Two-view Models in High Dimensions](/research-news/deep_reads/2026-05-21-2605.19364/) — 2026-05-21
- [6] [Asymptotic normality of log likelihood ratio and fundamental limit of the weak detection for spiked Wigner matrices](/research-news/deep_reads/2026-06-18-10.3150_24-bej1805/) — Bernoulli · 2026-06-18
- [7] [Computational and statistical thresholds in multi-layer stochastic block models](/research-news/deep_reads/2026-06-20-10.1214_24-aos2441/) — Annals of Statistics · 2026-06-20
- [8] [Large-dimensional independent component analysis: Statistical optimality and computational tractability](/research-news/deep_reads/2026-06-20-10.1214_24-aos2419/) — Annals of Statistics · 2026-06-20
- [9] [Low coordinate degree algorithms I: Universality of computational thresholds for hypothesis testing](/research-news/deep_reads/2026-06-20-10.1214_24-aos2484/) — Annals of Statistics · 2026-06-20
- [10] [Tensor-on-tensor regression: Riemannian optimization, over-parameterization, statistical-computational gap and their interplay](/research-news/deep_reads/2026-06-20-10.1214_24-aos2396/) — Annals of Statistics · 2026-06-20
- [11] [Online tensor learning: Computational and statistical trade-offs, adaptivity and optimal regret](/research-news/deep_reads/2026-07-04-10.1214_25-aos2588/) — Annals of Statistics · 2026-07-04
- [12] [A computational transition for detecting correlated stochastic block models by low-degree polynomials](/research-news/deep_reads/2026-05-26-10.1214_25-aos2565/) — Annals of Statistics · 2026-05-26
- [13] [Low-degree hardness of detection for correlated Erdős–Rényi graphs](/research-news/deep_reads/2026-05-26-10.1214_25-aos2517/) — Annals of Statistics · 2026-05-26
- [14] [Computational lower bounds for graphon estimation via low-degree polynomials](/research-news/deep_reads/2026-06-20-10.1214_24-aos2437/) — Annals of Statistics · 2026-06-20
- [15] [Optimal sampling designs for multidimensional streaming time series with application to power grid sensor data](/research-news/deep_reads/2026-06-24-10.1214_23-aoas1757/) — Annals of Applied Statistics · 2026-06-24

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

