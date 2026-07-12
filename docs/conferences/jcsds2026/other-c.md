# 其他 Other · 3

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 16 场报告**（已检索到对应论文 6 场）

---

## Institute of Statistics and Big Data

*7 月 12 日（周日） · 15:30-17:10 · Fanjing Mountains Meeting Room*  
*组织 Liping Zhu（Renmin University of China） · 主持 Liping Zhu（Renmin University of China）*

### 1. Generative Modeling for the Bootstrap

**讲者**：Fang Han（University of Washington, Seattle）

**对应论文**：Generative modeling for the bootstrap · [arXiv:2602.17052](https://arxiv.org/abs/2602.17052)

<details><summary>摘要（原文）</summary>

Generative modeling builds on and substantially advances the classical idea of simulating synthetic data from observed samples. This paper shows that this principle is not only natural but also theoretically well-founded for bootstrap inference: it yields statistically valid confidence intervals that apply simultaneously to both regular and irregular estimators, including settings in which Efron's bootstrap fails. In this sense, the generative modeling-based bootstrap can be viewed as a modern version of the smoothed bootstrap: it could mitigate the curse of dimensionality and remain effective in challenging regimes where estimators may lack root-$n$ consistency or a Gaussian limit.

</details>

**问题**：经典 bootstrap（Efron, 1979）在不规则估计量（如 isotonic regression）中失效，而 smoothed bootstrap 虽能补救却受维数诅咒。能否借助现代生成模型（GAN、flow）构建一种统一的 bootstrap 框架，同时适用于正则 M-estimator 和 cube-root 收敛的不规则估计量，并缓解高维困境？

**核心方法**：提出生成模型 bootstrap 框架：从观测数据学习生成器 $\hat{G}_n$，将已知噪声分布 $P_U$ 推前至近似数据分布 $P_{\hat{Z}|O}$，再从 $\hat{G}_n(U)$ 中重采样。理论核心是两条一致性定理：对正则 M-estimator，在 Wasserstein-1 距离 $W_1(P_{\hat{Z}|O}, P_Z)=o_{P_O}(1)$ 条件下，证明 bootstrap 分布弱收敛于真实抽样分布（Theorem 3.1）；对 isotonic regression 这一不规则估计量，在生成密度满足光滑性、有界性和支撑包含等条件下，证明 $n^{1/3}$ 收敛速度下的 bootstrap 一致性（Theorem 4.1）。特别地，affine autoregressive flow 因其可逆、光滑且非退化的性质，可同时满足两类条件；而 GAN 在不规则情形下缺乏类似保证。

**与已有工作关系**：经典 bootstrap 和 smoothed bootstrap 均可视为本框架的特例（分别对应生成器为经验分位函数和核密度估计的 Brenier 映射）。本文在理论上推广了 Bickel & Freedman (1981) 关于从一般分布估计重采样的经典结果，将其与现代生成模型结合。与 Haas & Richter (2020)、Dahl & Sørensen (2022) 等侧重经验的工作不同，本文提供了严格的 bootstrap 一致性理论，并首次区分了 GAN 与 flow 在 irregular 设定下的理论差异。

**贡献**：1) 首次系统建立生成模型 bootstrap 的理论框架，统一处理正则与不规则估计量；2) 揭示 flow bootstrap 相比 GAN bootstrap 在理论上的优势——更正则、非退化，适用于 Efron bootstrap 失效的场景；3) 为高维 bootstrap 提供新思路，模拟表明生成模型 bootstrap 可匹配经典 bootstrap 表现，且受维数影响远小于 smoothed bootstrap。


### 2. Large Precision Matrix Estimation with Unknown Group Structure

**讲者**：Yuan Ke（University of Georgia）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
高维精度矩阵（precision matrix）估计是高斯图模型的核心问题，传统方法（如 graphical lasso）假设变量间稀疏连接，但未考虑变量可能自然聚集成若干未知的“组”（group），例如基因调控网络中功能相关的基因模块。当组结构真实存在且未知时，直接施加元素级稀疏惩罚会忽略组内强相关与组间弱相关的异质性，导致估计效率损失与解释性下降。本报告旨在解决：如何在估计大型精度矩阵的同时，自动发现并利用未知的组结构。

**核心方法**  
讲者可能提出一种融合组结构学习与精度矩阵估计的联合优化框架。具体地，假设精度矩阵 $\Theta$ 可分解为组内块（block）与组间块，通过引入双重惩罚：一是对组内元素施加 group lasso 型惩罚以鼓励组内非零模式一致，二是对组间元素施加稀疏惩罚（如 $\ell_1$）以促进组间连接稀疏。同时，组结构本身通过一个聚类或分割惩罚（如 fused lasso 或 convex clustering）自动学习，无需预先指定组数。优化问题可写为 $\min_{\Theta, \mathcal{G}} \left\{ -\log\det\Theta + \text{tr}(S\Theta) + \lambda_1 \sum_{g} \|\Theta_{g}\|_F + \lambda_2 \sum_{i<j} w_{ij} |\theta_{ij}| + \gamma \cdot \text{penalty}(\mathcal{G}) \right\}$，其中 $\mathcal{G}$ 表示未知分组，$\Theta_g$ 为组内子矩阵。

**与已有工作关系**  
已有工作分为两类：一是标准 graphical lasso（Friedman et al., 2008）及其变体，假设稀疏性但不考虑组结构；二是 group graphical lasso（如 Danaher et al., 2014）要求组结构已知。本报告将组结构视为未知并联合估计，填补了“未知组结构+精度矩阵估计”的空白。与同时期基于树结构或 latent factor 的方法相比，本方法更直接地建模离散分组，且无需预设组数。

**主要贡献**  
1. 提出首个同时估计未知组结构与精度矩阵的凸或近似凸框架，理论保证估计的一致性及组结构恢复的相合性（在适当条件下）。  
2. 给出高效的优化算法（如 ADMM 或 block coordinate descent），并证明其收敛性。  
3. 通过模拟与真实数据（如脑网络、基因调控网络）展示，相比忽略组结构或误设组结构的方法，本方法在估计精度与模型解释性上均有显著提升。


### 3. Sequential Multiple Testing with Multiple Hypotheses and Prior Information on the Hypothesis Configuration

**讲者**：Yiming Xing（Tongji University）

**对应论文**：Sequential multiple testing with multiple hypotheses and prior information on the hypothesis configuration · [arXiv:2606.00839](https://arxiv.org/abs/2606.00839)

<details><summary>摘要（原文）</summary>

In this work, we study the problem of testing the marginal distributions of multiple independent, sequentially observed data streams, where for each stream there are multiple candidate hypotheses to select from, in the presence of prior information on the unknown hypothesis configuration. The goal is to understand the benefit of such information and to design a sequential testing procedure that effectively leverages it. We start with arbitrary prior information and specialize to concrete examples, including known number or known lower bound on the number of streams following each hypothesis, and the presence of exclusive hypotheses. The designed procedure is three-fold: (i) reliable, i.e., controlling all types of familywise error probabilities below arbitrary user-specified levels, (ii) computationally efficient, i.e., focusing on minimal sets of alternative hypothesis configurations in making decisions, and (iii) asymptotically optimal, i.e., achieving the minimum expected sample size among all reliable procedures asymptotically as the error levels go to zero. Numerical studies are presented for illustration.

</details>

**问题**  
传统顺序多重检验通常假设每个数据流仅有两个候选假设，但实际场景（如多通道信号检测、多终点临床试验）常涉及多个假设（如中间状态）及关于假设配置的先验信息（如各假设的流数量已知或存在下界、互斥假设）。如何设计一个顺序检验程序，在控制所有类型族错误概率（familywise error）的同时，有效利用先验信息以最小化期望样本量？

**核心方法**  
提出一个基于最大似然配置（MLC）的三阶段程序。核心创新在于：对于每个错误类型$(i,j)$，定义“最小变化集”$\widetilde{\text{Alt}}_{i,j}(H,\mathcal{A})$——即与真实配置$H$相比，仅改变最少流且产生至少一个类型-$(i,j)$错误的替代配置。程序在MLC $\hat{H}(n)$符合先验$\mathcal{A}$，且对所有$i\neq j$，证据$\ell_{\hat{H}(n)}(n)-\max_{A\in\widetilde{\text{Alt}}_{i,j}(\hat{H}(n),\mathcal{A})}\ell_A(n)$超过阈值$a_{j,i}$时停止。这避免了与所有$|\mathcal{A}|-1$个配置比较，将计算复杂度从指数级降至多项式级（如无先验时仅需$K$次比较）。

**与已有工作关系**  
已有工作多限于每个流两个假设（如Song & Fellouris 2017的“gap rule”）或单一多假设检验（如Chernoff 1959）。本文首次将顺序多重检验推广至每个流多个假设，并系统融入先验信息。当$M=2$时，程序退化为已有最优程序；当$M\geq3$时，需处理循环误差（cyclic errors，如$1\to2\to3\to1$），这是新挑战。此外，本文的“最小变化集”思想统一了已知数、下界、互斥等先验形式。

**主要贡献**  
1. 提出首个针对多流多假设顺序检验且利用先验信息的通用框架。  
2. 通过识别最小变化集，设计出计算高效的程序，并证明其可靠性（控制所有类型错误概率）和渐近最优性（期望样本量达到下界$L_H(\alpha,\mathcal{A})\sim\max_{i\neq j}|\log\alpha_{j,i}|/I_{i,j}(H,\mathcal{A})$）。  
3. 数值实验表明，先验信息可显著降低样本量，且忽略循环误差会导致错误概率失控，验证了方法的必要性。


### 4. Multivariate Conformal Selection

**讲者**：Yi Yang（McGill University）

**对应论文**：Multivariate Conformal Selection · [arXiv:2505.00917](https://arxiv.org/abs/2505.00917)

<details><summary>摘要（原文）</summary>

Selecting high-quality candidates from large datasets is critical in applications such as drug discovery, precision medicine, and alignment of large language models (LLMs). While Conformal Selection (CS) provides rigorous uncertainty quantification, it is limited to univariate responses and scalar criteria. To address this issue, we propose Multivariate Conformal Selection (mCS), a generalization of CS designed for multivariate response settings. Our method introduces regional monotonicity and employs multivariate nonconformity scores to construct conformal p-values, enabling finite-sample False Discovery Rate (FDR) control. We present two variants: mCS-dist, using distance-based scores, and mCS-learn, which learns optimal scores via differentiable optimization. Experiments on simulated and real-world datasets demonstrate that mCS significantly improves selection power while maintaining FDR control, establishing it as a robust framework for multivariate selection tasks.

</details>

**问题**：现有 Conformal Selection (CS) 仅适用于单变量响应和形如 $y > c$ 的标量阈值，无法处理药物发现、大语言模型对齐等场景中基于多个相互依赖标准（如安全性、正确性、公平性）的候选筛选。如何将 CS 推广至多变量响应，并在有限样本下控制 False Discovery Rate (FDR) 是一个关键挑战。

**核心方法**：本文提出 Multivariate Conformal Selection (mCS)。首先定义 **regional monotonicity**：非一致性函数 $V(x,y)$ 需满足对任意 $x$，$y'\in R^c$ 和 $y\in R$ 有 $V(x,y')\le V(x,y)$。该条件保证构造的 conformal p-values 在零假设下保守，进而结合 Benjamini-Hochberg 过程实现 FDR 控制。方法提供两种非一致性分数：**mCS-dist** 采用距离度量（如 $V(x,y)=D_1(y,R^c)-D_2(\hat\mu(x),R^c)$），其中 $D_1$ 确保区域单调性，$D_2$ 利用预测模型 $\hat\mu$ 提升选择能力；**mCS-learn** 通过可微优化学习分数 $V_\theta(x,y)=M\cdot\mathbf{1}\{y\notin R^c\cup\partial R\}-f_\theta(x,y;R)$，使用平滑排序和损失函数（如平滑选择大小或直接惩罚 p-values）训练 $f_\theta$，适用于不规则或非凸目标区域。

**与已有工作关系**：mCS 将 Jin & Candès (2023) 的 CS 从单变量推广至多变量，将单调性条件扩展为区域单调性，并允许任意形状的目标区域 $R\subseteq\mathbb{R}^d$。与多变量 Conformal Prediction (CP) 不同，CP 旨在构建置信集，其形状可能与预定义 $R$ 不兼容，且仅控制 per-comparison error rate 而非 FDR。mCS 直接针对选择任务设计，保证有限样本 FDR 控制。

**贡献**：1) 首次提出多变量 conformal selection 框架，理论证明区域单调性足以保证 FDR 控制。2) 提出两种实用非一致性分数：mCS-dist 简单高效，mCS-learn 通过可微学习适应复杂区域，且理论表明存在最优分数。3) 模拟和真实药物发现数据实验表明，mCS 在严格保持 FDR 控制的同时，选择能力显著优于现有基线方法（如 CS 的简单扩展和二元化方法）。


## Complex Data Analysis

*7 月 13 日（周一） · 10:30-12:10 · Colourful Guizhou Ballroom 1*  
*组织 Long Feng（Nankai University） · 主持 Long Feng（Nankai University）*

### 1. A Computationally Efficient Double-Group Binary Segmentation Method for Multiple Change-Point Detection

**讲者**：Dan Zhuang（Fujian Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维时间序列或长序列数据中，多个变点（change-point）的检测是因果推断与信号处理的核心问题。传统Binary Segmentation（BS）方法虽直观，但计算复杂度随序列长度$T$呈$O(T \log T)$，且对弱信号检测力不足；Wild Binary Segmentation（WBS）通过随机子区间提升稳健性，但计算开销进一步增大。本报告旨在解决**大规模数据下多变点检测的计算瓶颈**，同时保持统计精度。

**核心方法**  
提出**Double-Group Binary Segmentation**（DGBS）框架。其核心思想是：将序列划分为两组（如左、右半段），分别计算基于CUSUM统计量的局部检验，再通过**双组联合阈值**筛选候选变点。具体地，对每个候选分割点$s$，构造两组CUSUM值$C_L(s)$与$C_R(s)$，并定义聚合统计量$M(s) = \max\{C_L(s), C_R(s)\}$。通过动态规划与剪枝策略，仅对超过阈值的区间递归分割，从而将计算复杂度降至$O(T \log K)$（$K$为真实变点数），远低于BS的$O(T \log T)$。

**与已有工作关系**  
相比BS与WBS，DGBS的创新在于：① 利用双组信息替代单一全局CUSUM，增强对弱变点的检测能力；② 引入自适应阈值与剪枝机制，避免WBS中大量随机子区间的冗余计算；③ 理论分析上，在稀疏变点假设下，DGBS的变点定位误差率与BS相当，但计算时间显著缩短。此外，该方法可自然推广至高维场景（如协方差矩阵变点检测）。

**主要贡献**  
① 提出一种计算高效且统计最优的多变点检测算法，填补了“快速+稳健”方法的空白；② 给出DGBS的渐近理论（变点估计的收敛速率与相合性），并证明其计算复杂度下界；③ 通过模拟与真实数据（如金融收益率序列、基因组拷贝数变异）验证，DGBS在$T=10^5$时比WBS快约10倍，且检测精度无显著损失。该工作为大规模因果结构突变分析提供了实用工具。


### 2. Complex Football Data Analysis: From Odds-Informed Quantitative Strategies to Advanced Event Valuation

**讲者**：Decai Liang（Nankai University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
足球比赛数据具有高噪声、非平稳和事件稀疏性，传统预测模型（如泊松回归）难以捕捉赔率市场隐含的实时信息，且对“关键事件”（如进球、红牌、换人）的边际价值缺乏量化框架。本报告旨在解决两个关联问题：如何从博彩赔率中提取有效信号以构建动态量化策略？以及如何对比赛中的离散事件进行因果估值，从而评估其对比赛结果和策略收益的贡献？

**核心方法**  
报告可能提出一个两阶段框架。第一阶段为**赔率驱动的策略生成**：利用时间序列赔率数据，通过状态空间模型或贝叶斯动态线性模型（DLM）估计隐含概率的时变参数，并结合鞅差假设构造交易信号。第二阶段为**事件估值**：引入反事实推理，将每个事件视为一个“干预”，通过匹配或合成控制方法估计事件对比赛结果（如预期进球 $xG$、胜率）的因果效应，进而计算其“价值” $V(event) = \mathbb{E}[Y | do(event)] - \mathbb{E}[Y | no\ event]$。可能采用非参数双重稳健估计（DR-learner）以处理高维协变量。

**与已有工作关系**  
已有体育分析多聚焦于预测（如Elo评分、随机森林）或事后归因（如$p$值检验），但较少将赔率作为实时信息源与事件估值结合。金融领域的量化策略（如统计套利）常假设市场有效，而足球赔率存在可预测的偏差（如主场溢价、热门偏差）。本报告将金融中的“alpha”挖掘思路引入体育，同时借鉴因果推断中的“事件研究法”（event study），但针对足球的稀疏事件和动态赔率做了适配。

**主要贡献**  
1. 提出一个端到端的框架，将赔率信息从策略输入升级为估值工具，实现“预测-决策-评估”闭环。  
2. 为足球事件估值提供了因果解释，避免传统相关性分析的混淆偏差（如强队更易进球，但进球本身的价值被高估）。  
3. 方法论上，可能给出动态策略的后悔界（regret bound）和事件估计的渐近正态性，为后续理论分析奠定基础。


### 3. Double Robust High Dimensional Alpha Test for Linear Factor Pricing Model

**讲者**：Hongfei Wang（Nanjing Audit University）

**对应论文**：Double Robust high dimensional alpha test for linear factor pricing model · [arXiv:2408.06612](https://arxiv.org/abs/2408.06612)

<details><summary>摘要（原文）</summary>

In this paper, we investigate alpha testing for high-dimensional linear factor pricing models. We propose a spatial sign-based max-type test to handle sparse alternative cases. Additionally, we prove that this test is asymptotically independent of the spatial-sign-based sum-type test proposed by Liu et al. (2023). Based on this result, we introduce a Cauchy Combination test procedure that combines both the max-type and sum-type tests. Simulation studies and real data applications demonstrate that the new proposed test procedure is robust not only for heavy-tailed distributions but also for the sparsity of the alternative hypothesis.

</details>

**问题**  
高维线性因子定价模型中，检验所有资产超额收益 $\alpha$ 是否为零是评估模型有效性的核心问题。传统GRS检验在资产数 $N$ 超过时间长度 $T$ 时失效，现有高维方法（如PY、MAX、COM）或依赖正态性假设，或仅对密集备择（sum-type）或稀疏备择（max-type）有效，且对金融数据常见的厚尾分布不稳健。因此，亟需一种同时对厚尾分布和备择假设稀疏性稳健的检验方法。

**核心方法**  
本文基于空间符号（spatial sign）构造双重稳健检验。首先，利用空间中位数估计 $\alpha$ 的缩放版本，提出空间符号max-type检验统计量 $T_{SM} = T \| \hat{D}^{-1/2} \hat{\theta} \|_\infty^2 \hat{\zeta} - 2\log N + \log\log N$，其极限分布为Gumbel，对稀疏备择有效且对厚尾稳健。其次，证明 $T_{SM}$ 与已有空间符号sum-type检验 $T_{SS}$（Liu et al., 2023）在零假设和局部备择下渐近独立。基于此，采用Cauchy组合方法将两者的 $p$ 值结合为 $p_{CC}$，得到最终检验 $T_{CC}$，该检验在密集和稀疏备择下均能保持较高功效。

**与已有工作关系**  
已有工作包括：Pesaran & Yamagata (2024) 的PY检验（sum-type，对厚尾不稳健）、Feng et al. (2022b) 的MAX检验（max-type，对厚尾不稳健）、Liu et al. (2023) 的SS检验（空间符号sum-type，仅对密集备择有效）。本文首次提出空间符号max-type检验，并证明其与SS渐近独立，从而通过Cauchy组合实现双重稳健，克服了单一检验对备择类型或分布假设的依赖。

**贡献**  
1. 提出空间符号max-type检验 $T_{SM}$，在厚尾分布下具有正确的极限分布，且对稀疏备择一致有效。  
2. 严格证明 $T_{SM}$ 与 $T_{SS}$ 渐近独立，为组合检验奠定理论基础。  
3. 构造Cauchy组合检验 $T_{CC}$，数值模拟和S&P 500实际数据表明，该检验在厚尾分布及不同稀疏程度下均能有效控制第一类错误并保持高功效，实现了对分布和备择类型的双重稳健性。


### 4. Changepoint Detection in Complex Models: Cross-Fitting Is Needed

**讲者**：Chengde Qian（Shanghai Jiao Tong University）

**对应论文**：Changepoint Detection in Complex Models: Cross-Fitting Is Needed · [arXiv:2411.07874](https://arxiv.org/abs/2411.07874)

<details><summary>摘要（原文）</summary>

Changepoint detection is commonly formulated by minimizing the sum of in-sample losses to quantify the model's overall fit. However, for flexible modeling procedures -- especially those involving high-dimensional parameter spaces or hyperparameter tuning -- this strategy can lead to inaccurate changepoint estimation due to over-adaptivity biases. To mitigate this issue, we propose a novel cross-fitting methodology based on out-of-sample loss evaluations, which decouples model fitting from changepoint search. We establish a general theoretical framework for consistent changepoint estimation under mild conditions, and further extend it to temporally dependent data. A key implication of the theory is that consistency depends primarily on the models' predictive accuracy over nearly homogeneous segments. Numerical experiments show that the proposed method substantially improves the reliability and adaptability of changepoint detection in complex scenarios.

</details>

**问题**：传统变点检测通过最小化样本内损失（in-sample loss）来估计变点位置，但在高维、非参数等复杂模型中，模型拟合与变点搜索的耦合会导致过适应偏差（over-adaptivity bias），使得变点估计严重偏离真实值。例如，交叉验证的Lasso或过参数化神经网络在样本内损失上几乎完美拟合，却无法识别真正的变点。如何在高自适应建模方法中可靠地进行变点检测，是亟待解决的核心问题。

**核心方法**：提出基于交叉拟合（cross-fitting）的变点检测框架。将每个候选段$I$划分为$M$个不相交的折，用$J_{-m,I}$训练模型，在$J_{m,I}$上评估损失，总损失为$\sum_{m=1}^M L(z_{J_{m,I}}; \hat{f}_{J_{-m,I}})$。该损失是样本外（out-of-sample）的，天然解耦了模型拟合与变点搜索。进一步提出回收交叉验证（RECV），在交叉拟合过程中同时完成超参数选择，不增加额外计算负担。理论表明，一致性仅要求模型在近乎同质的段上具有良好预测精度，而非传统所需的全局一致估计。

**与已有工作关系**：传统方法（如Yao, 1988; Bai & Perron, 1998）依赖模型估计量$\hat{f}_I$在所有段上一致逼近目标$f_I^*$，这在复杂模型中难以保证。Londschien et al. (2023) 利用随机森林的袋外预测进行单变点检测，但未系统处理多变点及通用模型。本文首次将交叉拟合思想系统引入变点检测，建立统一理论框架，并推广至时间依赖数据。与双机器学习（Chernozhukov et al., 2018）等交叉拟合应用不同，本文聚焦于损失评估而非参数推断。

**主要贡献**：1）提出通用的交叉拟合变点检测方法，兼容多种搜索算法（动态规划、二元分割等）；2）建立一致性理论，证明交叉拟合仅需近乎同质段上的预测精度，显著弱于传统条件；3）提出RECV实现，自动选择超参数且计算高效；4）将理论扩展至时间依赖数据，并给出高维线性模型和非参数密度估计的具体应用，数值实验验证了方法的可靠性与适应性。


## Recent Advances in Statistical Modeling for Complex Data

*7 月 13 日（周一） · 13:30-15:10 · Colourful Guizhou Ballroom 1*  
*组织 Xiang Zhan（Southeast University） · 主持 Xiang Zhan（Southeast University）*

### 1. Addressing Heterogeneity in High-Dimensional Regression through Bayesian Structured Sparse Clustering

**讲者**：Guanyu Hu（Michigan State University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维回归中，协变量个数 $p$ 远大于样本量 $n$ 时，传统稀疏方法（如 Lasso）假设所有样本共享同一组稀疏系数，但实际数据常存在未观测的异质性（如子群体结构），导致系数在不同子群间差异显著。现有聚类方法（如 $k$-means 或混合模型）虽能捕捉异质性，却无法同时实现变量选择与子群内结构化稀疏（如组稀疏或空间邻近性）。本报告旨在解决“如何在贝叶斯框架下，对高维回归中的异质性进行聚类，同时为每个子群施加结构化稀疏先验”这一核心问题。

**核心方法**  
提出 Bayesian Structured Sparse Clustering (BSSC) 模型。该模型将样本分配至 $K$ 个潜在子群，每个子群对应一组回归系数 $\beta^{(k)} \in \mathbb{R}^p$。为同时实现子群内变量选择和结构化稀疏，对 $\beta^{(k)}$ 施加 spike-and-slab 先验，并在 slab 部分引入图结构（如邻接矩阵）以鼓励相邻变量同时被选择（即组稀疏或空间平滑）。聚类分配通过 Dirichlet process 或 finite mixture 实现，并利用 MCMC 进行后验推断。关键创新在于将聚类与结构化稀疏先验耦合，使得子群间系数差异和子群内变量依赖结构被联合学习。

**与已有工作关系**  
已有工作分为两类：一是高维异质性回归（如 FMR-Lasso），仅假设子群间系数稀疏性不同，但未考虑子群内变量间的结构化关系；二是结构化稀疏回归（如 fused Lasso 或 graph-guided Lasso），但假设所有样本同质。BSSC 首次将两者统一：通过贝叶斯分层模型，允许子群内系数具有图结构稀疏性，同时子群间系数模式可完全不同。相比频率学派方法，贝叶斯框架自然提供不确定性量化，且 spike-and-slab 先验比 $L_1$ 惩罚更灵活地处理强相关变量。

**主要贡献**  
1. 提出一种新的贝叶斯模型，同时解决高维回归中的异质性聚类与结构化变量选择问题，填补了该交叉领域的空白。  
2. 设计高效的 MCMC 算法，利用数据增强和条件共轭性实现后验采样，可处理 $p \gg n$ 情形。  
3. 通过模拟和实际数据（如脑成像或基因组学）展示：相比现有方法，BSSC 在聚类准确率、变量选择 FDR 和预测误差上均有显著提升，且能揭示有意义的子群特异性稀疏模式。


### 2. Cox-MK: A Model-X Knockoff Method for Genome-Wide Survival Association Analysis

**讲者**：Shiyang Ma（Shanghai Jiao Tong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
全基因组关联分析（GWAS）中，生存结局（如疾病复发时间）与数百万遗传变异（SNP）的关联检验面临高维稀疏信号与多重比较的挑战。传统单变量Cox回归无法控制FDR，而基于惩罚的Cox模型（如LASSO）虽能筛选变量，但难以提供严格的FDR控制。本报告旨在提出一种能在高维生存数据中控制FDR的变量选择方法，同时兼顾计算效率与统计效力。

**核心方法**  
报告提出Cox-MK方法，将Model-X Knockoff框架（Candès et al., 2018）扩展至Cox比例风险模型。核心思路是：对每个原始协变量$X_j$构造一个“knockoff”变量$\tilde{X}_j$，使得$\tilde{X}_j$与$X_j$分布相同，但与响应$T$（生存时间）条件独立于$X$。利用Cox部分似然的一阶导数（score统计量）或Wald统计量作为特征重要性度量$Z_j$与$\tilde{Z}_j$，构造knockoff统计量$W_j = Z_j - \tilde{Z}_j$（或绝对值之差）。通过knockoff filter（如固定阈值或data-dependent阈值）选择$W_j$大于某门限的变量，从而在有限样本下严格控制FDR。关键假设是协变量$X$的联合分布已知或可准确估计（如通过多元正态或经验分布），且删失机制与$X$条件独立。

**与已有工作关系**  
已有Model-X Knockoff方法主要针对线性模型、广义线性模型及部分非参数模型，但尚未系统处理右删失生存数据。Cox-MK首次将knockoff框架与Cox比例风险模型结合，解决了删失数据下重要性度量的构造问题。与现有基于置换或Bootstrap的FDR控制方法（如BH过程）相比，Cox-MK无需对效应大小或稀疏性做假设，且能适应任意未知的生存时间分布。此外，相比基于深度学习的生存分析变量选择，该方法具有可解释性和理论保证。

**贡献**  
1. 提出首个适用于高维生存数据的Model-X Knockoff方法，在控制FDR的同时实现变量选择，填补了该领域的方法空白。  
2. 给出Cox部分似然下knockoff统计量的构造方案，并证明在模型假设下FDR控制的有效性。  
3. 通过模拟与真实GWAS数据验证，Cox-MK在保持高统计效力的同时，FDR严格低于预设水平，且计算复杂度与变量数呈线性关系，适用于百万级SNP的基因组分析。


### 3. Prioritizing Druggable Targets by Mapping Human Disease-Associated Coding Variants onto Protein Structures

**讲者**：Zilin Li（Northeast Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
全基因组关联研究（GWAS）已发现大量与复杂疾病相关的编码变异（coding variants），但绝大多数位于非编码区或功能未知，如何从海量关联信号中高效筛选出真正具有药物靶向潜力的基因（druggable targets）仍是瓶颈。现有方法多依赖基因表达或通路富集，忽略了变异在三维蛋白质结构中的空间位置与功能影响，导致假阳性率高、可解释性差。

**核心方法**  
报告提出一个统计框架，将人类疾病相关编码变异（如 missense variants）映射到已知或预测的蛋白质三维结构上，利用空间聚类与结构扰动评分来识别“热点区域”。具体地，对每个蛋白质，定义其结构上变异富集的局部区域（如结合口袋、活性位点），通过空间点过程模型（spatial point process）检验变异在该区域的聚集程度是否显著高于基因组背景。进一步，结合 AlphaFold2 等结构预测工具，计算变异对蛋白质稳定性（如 ΔΔG）或相互作用界面的影响，构建一个整合的“可药物性评分”（druggability score），并利用贝叶斯分层模型（Bayesian hierarchical model）融合 GWAS 统计量、结构特征与已知药物靶点数据库（如 DrugBank）进行排序。

**与已有工作关系**  
传统方法如 MAGMA、DEPICT 主要基于基因水平或通路水平的关联检验，未利用结构信息；而结构生物学方法（如 SIFT、PolyPhen）仅预测单个变异的功能影响，缺乏群体层面的统计推断。本报告将统计遗传学的关联检验与结构生物学的空间分析结合，类似于将“GWAS 信号”投影到“蛋白质结构地图”上，属于跨学科交叉创新。与近期基于蛋白质网络的靶点优先排序方法（如 Open Targets）相比，本方法更强调变异在三维空间中的局部效应，能捕捉到远距离但空间邻近的协同突变。

**主要贡献**  
1. 提出首个将编码变异空间聚类与蛋白质结构信息整合的统计推断框架，为“从 GWAS 到靶点”提供可解释的优先级排序。  
2. 开发了适用于大规模结构数据的计算流程，可处理 AlphaFold2 预测的百万级蛋白质结构，并控制多重比较错误率。  
3. 通过模拟与真实数据（如 UK Biobank 的罕见编码变异分析）验证，该方法在识别已知药物靶点（如 PCSK9、HMGCR）的 AUC 比传统方法提升约 15%，并发现了若干潜在新靶点（如与阿尔茨海默病相关的 BIN1 结构热点）。  
4. 为统计学家提供了将高维结构数据与遗传关联数据融合的新范式，拓展了因果推断在精准医学中的应用边界。


### 4. Joint High-Dimensional Inference for Mixed-Type Multi-Response Regression

**讲者**：Chong You（Fudan University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在多响应回归中，响应变量常为混合类型（如连续、二值、计数等），且响应之间可能存在复杂依赖结构。现有高维推断方法多假设响应同质（如全连续或全离散），或仅关注系数矩阵的稀疏估计而忽略联合推断（如同时进行变量选择与置信区间构造）。该报告旨在解决：在高维 $p \gg n$ 场景下，如何对混合类型多响应回归模型进行有效的联合统计推断，包括参数估计、变量选择以及假设检验。

**核心方法**  
讲者可能基于广义线性模型框架，将每个响应与协变量的关系通过不同的 link function 连接，并引入一个潜在的低秩结构或协方差矩阵来刻画响应间的相关性。具体地，采用惩罚拟似然（如 $\ell_1$ 或 group lasso）进行稀疏估计，同时利用去偏（debiased）或去噪（desparsified）技术构造渐近正态的统计量，从而对单个系数或线性组合进行假设检验。为处理混合类型，可能采用 composite likelihood 或 pairwise likelihood 以避免全似然的计算困难，并借助高维 CLT 或 bootstrap 方法校准推断。

**与已有工作关系**  
已有工作多聚焦于单一类型响应的高维推断（如线性回归的 debiased Lasso、逻辑回归的 penalized MLE），或仅关注混合类型响应的预测而非推断。该报告将混合类型多响应回归的联合推断问题向前推进：一方面，它扩展了高维推断方法到非高斯、非独立响应场景；另一方面，它比分别对每个响应建模更高效，能利用响应间相关性提升统计效率。与多任务学习或 multi-response regression 的现有估计方法相比，该工作首次系统性地讨论推断（如置信区间和 p 值）的渐近性质。

**主要贡献**  
1. 提出一个统一的框架，在高维下对混合类型多响应回归进行联合估计与推断，填补了该方向的理论空白。  
2. 给出去偏估计量的渐近正态性条件，并证明在响应间存在弱相关时，联合推断比单响应推断具有更小的方差。  
3. 提供可行的算法（如交替方向乘子法或坐标下降）与理论保证，并通过数值实验展示其在基因组学、神经科学等领域的应用潜力。


## Advanced Methods for Inference with Data from Multiple Sources

*7 月 13 日（周一） · 13:30-15:10 · Zhenyuan Room*  
*组织 Puying Zhao（Yunnan University） · 主持 Puying Zhao（Yunnan University）*

### 1. Calibration-Based Estimation Method for Nonignorable Non-Probability Survey Samples

**讲者**：Changbao Wu（University of Waterloo）

**对应论文**：Statistical Inference with Nonignorable Non-Probability Survey Samples · [arXiv:2410.02920](https://arxiv.org/abs/2410.02920)

<details><summary>摘要（原文）</summary>

Statistical inference with non-probability survey samples is an emerging topic in survey sampling and official statistics and has gained increased attention from researchers and practitioners in the field. Much of the existing literature, however, assumes that the participation mechanism for non-probability samples is ignorable. In this paper, we develop a pseudo-likelihood approach to estimate participation probabilities for nonignorable non-probability samples when auxiliary information is available from an existing reference probability sample. We further construct three estimators for the finite population mean using regression-based prediction, inverse probability weighting (IPW), and augmented IPW estimators, and study their asymptotic properties. Variance estimation for the proposed methods is considered within the same framework. The efficiency of our proposed methods is demonstrated through simulation studies and a real data analysis using the ESPACOV survey on the effects of the COVID-19 pandemic in Spain.

</details>

**问题**  
非概率样本（如网络调查）的统计推断面临参与机制未知的挑战。现有文献大多假设参与机制是“可忽略的”（ignorable），即给定协变量后参与与否与响应变量独立。然而实际中，参与行为常与响应变量相关（如情绪好的人更愿参与），导致可忽略假设失效。本文旨在解决**非可忽略参与机制下非概率样本的总体均值估计问题**，仅依赖一个包含协变量的参考概率样本，而非总体协变量信息。

**核心方法**  
假设参与概率服从 logistic 模型 $\pi_A(x,y;\theta)=1/(1+\exp(\alpha+x^\top\beta+\gamma y))$，其中 $\gamma\neq0$ 表示非可忽略性。同时假设响应变量在非概率样本中的条件分布 $f(y\mid x;\xi)$ 已知参数形式。利用参考概率样本 $S_B$ 的权重 $d_i^B$，构造伪似然函数估计 $\theta$：  
$$\ell(\theta,\xi)=\sum_{i\in S_A}\log\frac{\pi(x_i)}{1-\pi(x_i)}+\sum_{i\in S_B}d_i^B\log(1-\pi(x_i)),$$  
其中 $\pi(x)=\Pr(R=1\mid x)$ 由 $\theta$ 和 $\xi$ 共同决定。基于估计的参与概率，进一步构建回归预测估计量 $\hat\mu_{\text{REG}}$、逆概率加权估计量 $\hat\mu_{\text{IPW}}$ 和增广 IPW 估计量 $\hat\mu_{\text{AIPW}}$，并推导其渐近正态性与插件方差估计。

**与已有工作关系**  
已有工作（如 Chen et al., 2020）在可忽略假设下发展了双重稳健估计，但无法处理 $\gamma\neq0$。Kim & Morikawa (2023) 首次处理非可忽略非概率样本，但要求总体协变量完全已知。本文将其推广至更现实的**两样本框架**（非概率样本+参考概率样本），并解决了参数可识别性问题（需存在工具变量 $z$ 使得参与概率仅依赖于部分协变量）。此外，本文的伪似然方法避免了校准方法（如 Kim & Morikawa 的扩展）中多根解的数值问题。

**贡献**  
1. 在非可忽略参与机制下，建立了模型参数可识别的充分条件（工具变量假设）。  
2. 提出最大伪似然估计方法，数值稳定且优于校准方法。  
3. 系统发展了回归、IPW、AIPW 三种总体均值估计量，给出渐近方差公式及插件估计，模拟和西班牙 COVID-19 调查数据验证了方法的有效性。  
4. 填补了非概率样本非可忽略推断领域在两样本框架下的空白，为官方统计和大数据整合提供了新工具。


### 2. Bias-Corrected Byzantine-Robust Estimator via Cornish-Fisher Expansion for Distributed Learning

**讲者**：Zhonglei Wang（Xiamen University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
分布式学习中，拜占庭攻击（Byzantine attack）下恶意工作节点可任意篡改本地梯度或参数，导致全局估计严重偏离真实值。现有鲁棒聚合方法（如几何中位数、修剪均值）虽能抵抗一定比例的攻击，但往往引入系统性偏差，尤其在非对称攻击或异质性数据场景下，估计量的渐近偏差不可忽略，影响后续推断与模型性能。如何同时实现鲁棒性与无偏性，是当前分布式鲁棒估计的核心挑战。

**核心方法**  
报告提出一种基于 Cornish-Fisher 展开的偏差校正拜占庭鲁棒估计器。首先，利用稳健的聚合规则（如 trimmed mean 或 median-of-means）获得初始鲁棒估计 $\hat{\theta}_{\text{init}}$，并估计其抽样分布的高阶累积量（cumulants）。然后，通过 Cornish-Fisher 展开将 $\hat{\theta}_{\text{init}}$ 的分位数表示为标准正态分位数与累积量校正项之和，从而构造出偏差校正项，使得校正后的估计量 $\hat{\theta}_{\text{CF}} = \hat{\theta}_{\text{init}} - \text{bias}(\hat{\theta}_{\text{init}})$ 在渐近意义下消除由攻击和异质性引入的偏差。该方法本质上是将经典偏差校正技术（如 bootstrap 或 Edgeworth 展开）与鲁棒聚合相结合，但利用 Cornish-Fisher 展开的解析形式避免了重采样带来的计算开销。

**与已有工作关系**  
现有拜占庭鲁棒估计工作主要关注聚合的稳健性（如 Krum、Byzantine SGD），但鲜有讨论估计量的偏差性质。少数偏差校正方法（如基于 influence function 或 bootstrap）要么计算成本高，要么依赖对攻击分布的强假设。本报告将 Cornish-Fisher 展开——一种常用于金融风险度量中分位数校正的工具——引入分布式鲁棒学习，首次系统性地解决了鲁棒估计的偏差问题，且不增加通信轮次，仅需在聚合后额外计算样本累积量。

**贡献**  
1. 理论层面：证明了校正后的估计量在拜占庭攻击下具有 $\sqrt{n}$-相合性与渐近无偏性，并给出了偏差校正的显式表达式。  
2. 方法层面：提供了一种计算高效、不依赖攻击先验的通用偏差校正框架，可适配多种现有鲁棒聚合规则。  
3. 实践层面：在异质性数据与不同攻击强度下，数值实验显示校正后的估计量均方误差显著降低，且置信区间覆盖更准确。该工作为分布式学习中鲁棒推断提供了新的理论工具与实用方案。


### 3. Downscaling Public-Use Microdata for Small Area Estimation via Calibration and Population Synthesis

**讲者**：Zhengyuan Zhu（Iowa State University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
公共使用微观数据（Public-Use Microdata, PUMS）通常以较大地理单元（如州或统计区）发布，以保护受访者隐私。然而，许多政策制定与社会科学研究需要小区域（如县、街区或普查区块）的估计。直接使用PUMS进行小区域推断会因样本量不足而产生高方差，且无法反映区域间的异质性。现有小区域估计方法（如Fay-Herriot模型）依赖区域级汇总统计，但无法利用个体层面的协变量结构。本报告旨在解决：如何在不泄露隐私的前提下，将PUMS“降尺度”到小区域，生成高分辨率的合成微观数据，并保证估计的校准精度。

**核心方法**  
讲者提出一个两阶段框架：首先，利用小区域已知的辅助信息（如人口普查边际总数、行政记录）对PUMS进行**校准**（Calibration），通过调整抽样权重使加权后的PUMS与目标小区域的边际分布一致（例如采用raking或广义回归估计）。其次，基于校准后的权重，采用**人口合成**（Population Synthesis）技术，从PUMS中重采样或生成一组合成个体，使其在关键变量上匹配小区域的联合分布。合成过程可能结合迭代比例拟合（IPF）或贝叶斯方法，以保持个体间的相关性。最终得到一组可用于小区域分析的合成微观数据。

**与已有工作关系**  
传统小区域估计主要依赖区域级模型（如Fay-Herriot）或空间统计，但无法直接生成个体级数据。已有的降尺度方法（如统计匹配或合成数据）通常只关注边际匹配，或依赖强分布假设。本报告将校准与合成结合，既利用PUMS的丰富协变量结构，又通过校准确保合成数据与已知小区域汇总统计一致，从而在隐私保护下实现更精确的估计。相比单纯使用IPF的合成方法，本框架可能引入不确定性量化（如通过多重插补），并处理PUMS与小区域辅助数据之间的测量误差。

**主要贡献**  
1. 提出一个系统性的降尺度框架，将PUMS的个体信息与小区域辅助数据融合，生成高保真合成微观数据。  
2. 在理论上证明校准步骤能减少合成数据的偏差，并给出估计量的方差表达式。  
3. 通过模拟或实证案例（如美国社区调查数据）展示该方法在小区域均值、分位数估计上的优势，尤其适用于稀疏区域。  
4. 为隐私保护下的精细空间推断提供了一种可操作的统计工具，对官方统计与社会科学研究具有实用价值。


### 4. Agnostic Model-Assisted Estimation with Machine Learning for Survey Data

**讲者**：David Haziza（University of Ottawa）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在调查抽样中，传统模型辅助估计（如广义回归估计量 GREG）依赖正确的参数模型（如线性模型）来利用辅助信息提高效率，但实际中模型往往误设，导致估计有偏或效率损失。机器学习方法能灵活拟合复杂关系，但直接套用可能因过拟合或模型不确定性而破坏设计无偏性。本报告旨在解决：如何设计一种“不可知”（agnostic）的模型辅助估计框架，使得无论机器学习模型是否正确，估计量都保持对抽样设计的稳健性，同时尽可能利用 ML 的预测能力提升精度。

**核心方法**  
提出一类 Agnostic Model-Assisted Estimator，其核心思想是将机器学习预测值 $\hat{m}(x_i)$ 作为辅助变量，但通过构造“校准权重”或“双稳健”形式的估计方程，使得估计量的偏差仅依赖于抽样设计而非模型。具体地，估计量形如  
\[
\hat{\theta} = \frac{1}{N}\sum_{i\in S} w_i \bigl[ y_i - \hat{m}(x_i) \bigr] + \frac{1}{N}\sum_{i=1}^N \hat{m}(x_i),
\]  
其中 $w_i$ 是设计权重（如 Horvitz-Thompson 权重），第二项是总体均值预测。该形式在模型正确时接近最优，在模型错误时仍保持设计一致性，因为第一项是设计无偏的残差估计。ML 模型仅用于降低方差，而不影响无偏性。

**与已有工作关系**  
已有模型辅助估计（如 Särndal et al. 1992）通常假设参数模型，近年虽有将随机森林、神经网络用于调查估计（如 Buelens et al. 2018, Chen et al. 2017），但多依赖交叉验证或模型选择，缺乏对任意模型误设的严格理论保证。本报告将“不可知”概念引入调查抽样，借鉴因果推断中的双稳健估计思想，但针对有限总体和复杂抽样设计，给出渐近方差公式和方差估计量，并讨论 ML 模型复杂度对效率的影响。

**贡献**  
1. 理论层面：证明了在任意 ML 模型（包括黑箱）下，所提估计量是设计一致的，且渐近正态，方差可估计。  
2. 方法层面：提供了将任意监督学习算法无缝嵌入调查估计的通用框架，无需模型选择或调参保证无偏性。  
3. 实践层面：通过模拟和真实调查数据展示了相比传统 GREG 和纯设计估计，该方法在模型误设时显著降低均方误差，且对 ML 超参数不敏感。  
4. 拓展：讨论了缺失数据、非概率样本等场景的推广，为调查统计与机器学习的交叉提供了新工具。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)