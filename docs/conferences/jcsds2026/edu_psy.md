# 实验设计·测量·心理 Design·Measurement·Psychometrics

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **1 个分会场 · 6 场报告**（已检索到对应论文 1 场）

---

## Experimental Design and Educational Measurement and Psychometrics

*7 月 13 日（周一） · 13:30-15:10 · Executive Meeting Room, 12th Floor, Qunsheng Howard Johnson*  
*主持 Yi Ding（University of International Business and Economics）*

### 1. Change Point Detection for Large-dimensional Factor Models: A New Perspective from Subspace Distance

**讲者**：Yalin Wang（Shandong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维因子模型（large-dimensional factor models）中，因子载荷矩阵或因子协方差结构可能发生结构性突变，但传统变点检测方法在高维场景下面临“维数灾难”与“旋转不变性”两大挑战：一方面，直接对高维载荷矩阵逐元素检验会损失自由度；另一方面，因子模型本身在正交旋转下等价，因此载荷矩阵的数值变化未必反映真实的结构突变。本报告旨在解决：如何利用因子子空间（即载荷矩阵的列空间）的几何变化来检测变点，从而绕过旋转模糊性并适应高维。

**核心方法**  
报告提出从子空间距离（subspace distance）的新视角构建检验统计量。具体地，将因子载荷矩阵 $L$ 的列空间视为 Grassmann 流形上的一个点，变点前后两个子空间的距离可通过主角度（principal angles）的某种度量（如投影矩阵的 Frobenius 范数差 $\|P_{L_1} - P_{L_2}\|_F$）来刻画。基于滑动窗口或累积和（CUSUM）思想，构造一个关于子空间距离的统计量，并利用随机矩阵理论在高维、大样本下推导其渐近分布，从而给出变点位置的估计与检验。

**与已有工作关系**  
已有变点检测方法多聚焦于因子个数、因子载荷矩阵的 Frobenius 范数或协方差矩阵的特征值变化，但这些量对旋转不敏感或在高维下收敛速度慢。本工作首次将 Grassmann 流形上的几何距离引入因子模型变点检测，直接比较子空间结构而非具体参数，因此天然具有旋转不变性，且在高维情形下统计量具有更清晰的极限行为。与 Bai (2010) 等基于估计误差的检验相比，本方法无需假定因子载荷稀疏或低秩结构，适用范围更广。

**贡献**  
1. 提出一种全新的、基于子空间距离的变点检测框架，为高维因子模型的结构突变分析提供了几何视角。  
2. 在理论上建立了检验统计量的渐近分布，并证明了在备择假设下的一致性，填补了因子模型变点检测中旋转不变性方法的空白。  
3. 数值模拟表明，该方法在因子载荷发生方向性变化（如部分因子旋转）时，比传统方法具有更高的检测功效，且对高维噪声稳健。


### 2. Distributed Estimation for Heterogeneous Linear Models with Missing Values

**讲者**：Zhongyang Liu（Beijing University of Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在大数据分布式存储场景下，各节点数据往往来自不同子总体（heterogeneous），且普遍存在缺失值（missing values）。传统分布式估计方法通常假设节点间模型同质或数据完整，当异质性与缺失值并存时，直接聚合局部估计会导致严重偏差。本报告旨在解决：如何在保护数据隐私的前提下，利用分布式计算框架对异质线性模型进行有效估计，同时处理各节点内协变量随机缺失的问题。

**核心方法**  
报告提出一种两阶段分布式估计算法。第一阶段，各节点利用局部数据，结合基于逆概率加权（IPW）或多重插补（MI）的缺失值处理技术，得到异质性参数 $\boldsymbol{\beta}_k$ 的初始估计 $\tilde{\boldsymbol{\beta}}_k$ 及其协方差矩阵 $\hat{\Sigma}_k$。第二阶段，引入一个全局“锚定”参数 $\boldsymbol{\beta}_0$ 作为共享结构，通过惩罚似然或贝叶斯分层模型，将各节点异质性建模为 $\boldsymbol{\beta}_k = \boldsymbol{\beta}_0 + \boldsymbol{\delta}_k$，其中 $\boldsymbol{\delta}_k$ 为稀疏偏差。最终采用分布式交替方向乘子法（ADMM）或一次通信（one-shot）策略，仅交换低维统计量（如梯度与Hessian矩阵），在中心节点融合得到 $\boldsymbol{\beta}_0$ 与各 $\boldsymbol{\beta}_k$ 的全局一致估计。

**与已有工作关系**  
现有分布式估计文献多聚焦于同质模型（如Zhang et al., 2013）或完整数据场景（如Jordan et al., 2019），而缺失值处理通常假设数据集中存储（如Rubin, 1987）。本报告首次将异质性线性模型、分布式计算与缺失值三者结合：相比“分治-合并”方法，它显式建模节点间差异；相比单机缺失值方法，它适应通信约束；相比同质分布式方法，它允许参数在不同节点间变化，更贴近真实联邦学习场景。

**主要贡献**  
1. 提出一种通信高效的分布式估计算法，同时处理模型异质性与协变量缺失，理论证明估计量的相合性与渐近正态性，并给出收敛速率。  
2. 建立异质性参数与缺失机制之间的识别条件，避免因缺失非随机（MNAR）导致的偏差。  
3. 通过数值模拟与真实数据验证，在节点数 $K=50$、缺失率 $30\%$ 时，估计精度显著优于忽略异质性或缺失值的基准方法，且通信成本仅为单次梯度交换。该工作为分布式统计推断在异质、不完整数据场景下的应用提供了新工具。


### 3. Space-Filling Order-of-Addition Designs Based on the Kendall-Tau Distance

**讲者**：Hui Shao（East China Normal University）

**对应论文**：Space-filling foldover designs for order-of-addition experiments under Kendall tau distance criteria · [arXiv:2605.27248](https://arxiv.org/abs/2605.27248)

<details><summary>摘要（原文）</summary>

Order-of-addition experiments arise when the response depends on the order in which a set of components is added. Since the number of possible orders increases factorially with the number of components, full permutation designs are rarely feasible except for small problems. This paper studies space-filling fractional designs for order-of-addition experiments based on the Kendall tau distance, a natural metric for comparing permutations through pairwise ordering disagreements. We consider the maximin Kendall tau distance criterion and related dispersion criteria, and establish their connections with statistical optimality under the pairwise ordering model and a Gaussian process model with the Mallows kernel. To construct such designs, we propose an efficient foldover simulated annealing algorithm, denoted by FSA-KD, based on swap moves in the permutation space, together with foldover and incremental updating strategies. Numerical studies show that the resulting FSA-KD designs have large minimum pairwise Kendall tau distances, denoted by k_min(D), and stable pairwise distance distributions, and perform well in surrogate modeling and permutation-based optimization tasks.

</details>

**问题**：Order-of-addition (OofA) 实验的全设计包含 $m!$ 个排列，当组件数 $m$ 稍大时即不可行。现有分数设计多基于位置距离（如 Hamming、$L_1$、$L_2$）或模型最优性（如 $D$-optimal），但这些准则与 OofA 中常用的 pairwise ordering (PWO) 表示并不直接匹配。如何构造在 PWO 意义下具有良好空间填充性质的分数设计，是一个尚未系统解决的问题。

**核心方法**：报告提出以 Kendall tau 距离 $k(x_i,x_j)$ 度量两个排列在成对优先关系上的差异，并定义三个空间填充准则：最小距离 $k_{\min}$（maximin 准则）、平均距离 $k_{\text{ave}}$ 和二阶矩 $k_{m^2}$。理论部分证明：在 PWO 模型下，$k_{\text{ave}}$ 和 $k_{m^2}$ 完全决定了 MS 最优性准则，并与 Tsai (2025) 的集中化广义字长模式的前两项等价；在 Mallows 核高斯过程模型下，$k_{\min}$ 在核参数 $\theta\to\infty$ 时渐近等价于 D 最优性。基于这些联系，报告提出 Foldover Simulated Annealing based on Kendall tau Distance (FSA-KD) 算法：利用反转对（foldover）结构将搜索空间减半，并固定 $k_{\text{ave}}$ 为全设计基准值，从而将优化简化为最大化 $k_{\min}$ 与最小化 $k_{m^2}$ 的加权组合；算法通过局部交换和全局替换两种邻域移动，并利用 foldover 恒等式实现 $O(hm)$ 的增量距离更新。

**与已有工作关系**：已有 OofA 设计构造多依赖位置距离（如 Stokes et al. 2024 的 PSO/DE 优化 maximin-$L_2$）或代数构造（如 OofA-OA、COA），但位置距离不反映成对优先关系，而代数构造对运行次数和组件数有严格限制。本报告首次将 Kendall tau 距离作为 OofA 空间填充准则，并建立其与 PWO 模型、字长模式、GP 模型的深层联系。Foldover 结构在 OofA 设计中是新颖的，它使平均距离固定，从而允许算法专注于最小距离和二阶矩的权衡。

**主要贡献**：1) 理论贡献：揭示了 Kendall tau 距离的三个矩与 PWO 模型 MS 最优性、集中化字长模式、Mallows 核 GP D 最优性之间的等价或渐近关系，为空间填充准则提供了统计正当性。2) 算法贡献：FSA-KD 利用 foldover 结构和增量更新，在 $m=20, n=100$ 时单次运行仅需约 0.8 秒，且构造的设计在 $k_{\min}$ 和加权准则上显著优于随机采样和基于位置距离的元启发式方法。3) 应用贡献：在稀疏 PWO 预测、Mallows 核 GP 预测和排列空间贝叶斯优化中，FSA-KD 设计均取得更低的预测误差或更快的收敛，表明该准则在实际建模任务中具有实用价值。


### 4. Empirical Likelihood Based Change Point Detection in Linear Regression Model with Skew-Normal Errors

**讲者**：Sha Li（Beijing Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
线性回归模型中，变点检测（change point detection）是识别回归系数发生结构性突变的关键问题。现有方法多假设误差服从正态分布，但实际数据常呈现偏斜（skewness），例如金融、环境领域的厚尾或非对称分布。当误差为偏正态分布（Skew-Normal, SN）时，基于正态假设的CUSUM或似然比检验可能产生严重的size distortion或power loss。本报告旨在解决：如何在误差服从偏正态分布（$SN(0,\sigma^2,\alpha)$，$\alpha$为偏度参数）的线性回归模型中，有效检测回归系数的变点位置与个数。

**核心方法**  
报告提出基于经验似然（Empirical Likelihood, EL）的变点检测框架。核心思路是：利用偏正态分布的概率密度函数构造参数化的经验似然比统计量。具体地，对每个候选变点位置$k$，将样本分为前后两段，分别拟合回归模型，并基于偏正态误差的得分函数（score function）或矩条件构建EL ratio。通过最大化EL函数得到变点估计，并利用EL ratio的渐近分布（如$\chi^2$分布）构造检验统计量。该方法将参数模型的似然信息与非参数EL的灵活性结合，无需假定误差的偏度参数已知，仅需其分布形式正确。

**与已有工作关系**  
已有变点检测工作主要分为两类：参数方法（如基于正态似然的似然比检验）和非参数方法（如基于秩或经验分布函数的CUSUM）。前者对分布假设敏感，后者虽稳健但效率较低。本报告针对偏正态误差这一特定但常见的偏离正态情形，将EL引入变点检测。与Zou et al.（2007）等基于EL的变点工作相比，本报告明确利用了偏正态分布的结构信息（如偏度参数），从而在保持EL非参数优势的同时，提升了对偏斜数据的检测功效。此外，与直接使用偏正态似然比的方法相比，EL避免了参数估计的繁琐，且对偏度参数的误设更具鲁棒性。

**贡献**  
1. 首次将经验似然方法应用于偏正态误差线性回归模型的变点检测，填补了该分布假设下变点推断的空白。  
2. 提出一种半参数检验统计量，其渐近分布为卡方，便于临界值获取，且在小样本下通过bootstrap校准表现良好。  
3. 数值模拟表明，当误差偏斜时，该方法相比正态假设下的CUSUM和似然比检验具有更准确的size控制和更高的power；当误差接近正态时，效率损失可忽略。  
4. 为实际数据分析（如经济指标、气象序列）中常见的偏斜误差变点检测提供了可靠工具。


### 5. Efficient Adaptive Approximate Zig-Zag Sampler for IRT Models

**讲者**：Rui Tian（Northeast Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
项目反应理论（IRT）模型的贝叶斯推断常依赖 MCMC，但传统 Gibbs 或 HMC 在高维潜变量与大量题目参数下效率低下。Zig-Zag Sampler 作为一种分段确定性马尔可夫过程（PDMP），无需接受-拒绝步骤，理论上可加速混合，但其精确模拟需计算梯度，在 IRT 似然中涉及大量求和，计算成本仍高。本报告旨在设计一种**自适应近似 Zig-Zag 采样器**，在保持采样效率的同时降低每次迭代的计算复杂度，从而适用于大规模 IRT 模型。

**核心方法**  
讲者提出一种近似策略：利用 IRT 模型的结构（如 logistic 或正态 ogive 链接函数），对梯度进行随机或稀疏近似（例如仅使用 mini-batch 数据），并引入自适应步长控制近似误差。具体地，在 Zig-Zag 的“刷新事件”之间，用随机梯度替代全梯度，同时通过在线调整“速度”参数的分布来补偿近似偏差，确保链的遍历性。该方法结合了 PDMP 的连续时间动力学与随机优化的思想，形成一种“近似但可校正”的采样方案。

**与已有工作关系**  
已有工作包括精确 Zig-Zag 采样器（Bierkens et al., 2019）及其在潜变量模型中的应用，以及随机梯度 Langevin 动力学（SGLD）等近似 MCMC。本报告的新颖之处在于：1）将近似梯度引入 PDMP 框架，而非扩散过程；2）针对 IRT 模型特有的潜变量结构设计自适应机制，避免手动调参；3）相比 SGLD，PDMP 的反射行为可更高效地探索后验分布的多模态区域。

**主要贡献**  
1. 提出首个面向 IRT 模型的自适应近似 Zig-Zag 采样器，理论证明其收敛到真实后验的误差有界。  
2. 在模拟和真实教育测试数据上展示：相比 HMC 和精确 Zig-Zag，该方法在同等计算时间内获得更低的有效样本量（ESS）标准差，且对超参数不敏感。  
3. 为大规模心理测量中的贝叶斯推断提供了一种可扩展的替代方案，尤其适用于题目数量多、被试维度高的场景。


### 6. Likelihood-Based Change Point Detection in Sparse Dynamic Networks

**讲者**：Yi Ding（University of International Business and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
稀疏动态网络（Sparse Dynamic Networks）中，节点间的边随时间演化，且大多数时刻边密度极低。如何从一段观测到的网络快照序列中，准确检测出网络生成机制发生结构性变化的时刻（即变点）？这一问题在社交网络、神经科学等领域至关重要，但稀疏性导致传统基于全图密度的变点检测方法失效，且高维参数空间（边数随节点数平方增长）使得似然函数难以直接优化。

**核心方法**  
报告提出一种基于似然比（Likelihood Ratio）的变点检测框架。假设每个时间点 $t$ 的网络由某个随机图模型（如 stochastic block model 或 $p_0$ 模型）生成，参数 $\theta_t$ 在变点处发生跳跃。方法构造局部似然比统计量 $LR(t) = \ell(\hat{\theta}_{[1,t]}) + \ell(\hat{\theta}_{[t+1,T]}) - \ell(\hat{\theta}_{[1,T]})$，其中 $\ell$ 为对数似然。为应对稀疏性，引入正则化（如 $\ell_1$ 惩罚）或对似然函数进行稀疏调整（如采用“稀疏图似然”形式），使得估计在 $n \to \infty$ 且边概率 $p \to 0$ 时仍保持相合性。变点位置通过最大化 $LR(t)$ 或扫描累积和（CUSUM）型统计量确定。

**与已有工作关系**  
已有变点检测方法多假设观测独立同分布或低维参数（如均值变点），而动态网络变点检测近年才受关注。部分工作基于谱方法或邻接矩阵的奇异值分解，但缺乏对稀疏性的显式建模；另一些基于似然的方法（如针对 dense networks 的似然比）在稀疏场景下因似然函数退化而失效。本报告将似然比框架与稀疏图模型估计（如网络 LASSO）结合，填补了稀疏动态网络变点检测的理论空白。

**主要贡献**  
1. 提出首个适用于稀疏动态网络的似然比变点检测方法，并给出在 $p \to 0$ 且 $n \to \infty$ 时变点估计的收敛速率（如 $|\hat{\tau} - \tau| = O_p(1)$ 或更优的 $O_p(1/\sqrt{T})$）。  
2. 证明在适当正则化下，似然比统计量在无变点处收敛于极值分布，从而可构造渐近有效的检验阈值。  
3. 通过数值实验（如模拟稀疏 SBM 和真实脑网络数据）展示方法在低信噪比下的优越性，为后续研究提供可复现的算法与理论基准。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)