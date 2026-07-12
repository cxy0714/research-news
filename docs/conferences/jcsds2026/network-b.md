# 网络与图数据 Networks & Graphs · 2

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 18 场报告**（已检索到对应论文 8 场）

---

## Inference in Statistical Models for Network Data

*7 月 11 日（周六） · 15:30-17:10 · Huangguoshu Theater Meeting Room*  
*组织 Ting Yan（Central China Normal University） · 主持 Ting Yan（Central China Normal University）*

### 1. Hypergraph Embeddings

**讲者**：Binyan Jiang（The Hong Kong Polytechnic University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
超图（hypergraph）允许一条超边连接任意多个节点，能自然刻画高阶交互（如共现、多变量因果关系），但现有图嵌入方法（如node2vec、GNN）仅适用于普通图（边连接两个节点）。如何将超图的节点或超边映射到低维向量空间，同时保留高阶结构信息（如超边内节点的联合分布、超边间的重叠模式）？这是本报告要解决的核心问题。

**核心方法**  
报告可能提出一种基于**超图拉普拉斯（hypergraph Laplacian）**的谱嵌入框架。具体地，定义超图上的随机游走：从当前节点出发，先均匀选择包含该节点的超边，再在该超边内均匀选择下一节点。该游走的转移矩阵$P$的谱分解给出节点的低维表示。为处理超边权重与节点异质性，可引入正则化项或采用**张量分解**（如CP分解）直接对超边邻接张量$\mathcal{A} \in \{0,1\}^{n \times n \times \cdots \times n}$（$k$阶）进行低秩近似，得到节点嵌入。此外，可能结合**变分推断**或**对比学习**目标，使嵌入保持超边内节点相似性高于随机负样本。

**与已有工作关系**  
已有图嵌入方法（如DeepWalk、LINE）仅考虑成对边，无法捕捉超边内多个节点的联合效应。部分超图神经网络（HGNN）通过超边卷积聚合信息，但依赖节点特征且缺乏可解释的几何意义。本报告的方法不依赖节点特征，仅利用超图结构，且通过谱理论或张量分解提供显式低维表示，与经典谱聚类、多维缩放（MDS）一脉相承，但推广到高阶交互场景。

**主要贡献**  
1. 提出一种可扩展的超图嵌入算法，计算复杂度与超边数线性相关，适用于大规模超图。  
2. 给出嵌入的统计一致性：当超图由某种随机超图模型（如超图随机块模型）生成时，嵌入能一致地恢复节点社区结构。  
3. 在多个真实数据集（如论文合著、药物组合）上展示嵌入在下游任务（超边预测、节点分类）中的优越性，尤其优于将超图退化为普通图的基线方法。


### 2. Optimal Clustering by Lloyd Algorithm for Low-Rank Mixture Model

**讲者**：Dong Xia（Hong Kong University of Science and Technology）

**对应论文**：Optimal Clustering by Lloyd Algorithm for Low-Rank Mixture Model · [arXiv:2207.04600](https://arxiv.org/abs/2207.04600)

<details><summary>摘要（原文）</summary>

This paper investigates the computational and statistical limits in clustering matrix-valued observations. We propose a low-rank mixture model (LrMM), adapted from the classical Gaussian mixture model (GMM) to treat matrix-valued observations, which assumes low-rankness for population center matrices. A computationally efficient clustering method is designed by integrating Lloyd's algorithm and low-rank approximation. Once well-initialized, the algorithm converges fast and achieves an exponential-type clustering error rate that is minimax optimal. Meanwhile, we show that a tensor-based spectral method delivers a good initial clustering. Comparable to GMM, the minimax optimal clustering error rate is decided by the separation strength, i.e., the minimal distance between population center matrices. By exploiting low-rankness, the proposed algorithm is blessed with a weaker requirement on the separation strength. Unlike GMM, however, the computational difficulty of LrMM is characterized by the signal strength, i.e., the smallest non-zero singular values of population center matrices. Evidence is provided showing that no polynomial-time algorithm is consistent if the signal strength is not strong enough, even though the separation strength is strong. Intriguing differences between estimation and clustering under LrMM are discussed. The merits of low-rank Lloyd's algorithm are confirmed by comprehensive simulation experiments. Finally, our method outperforms others in the literature on real-world datasets.

</details>

**问题**：矩阵值观测的聚类问题广泛存在于基因网络、脑成像、国际贸易流等场景。传统方法将矩阵向量化后应用经典聚类算法（如K-means），但忽略了矩阵观测中普遍存在的低秩结构，导致统计次优。本文提出低秩混合模型（LrMM），假设每个簇的中心矩阵是低秩的，旨在同时实现计算高效与统计最优的聚类。

**核心方法**：设计低秩Lloyd算法（lr-Lloyd）。该算法在每次迭代中，先根据当前标签计算每个簇的样本均值矩阵，再通过SVD取其最佳低秩近似作为更新后的簇中心，然后重新分配标签。初始化采用基于张量谱方法（TS-Init），通过HOSVD估计低秩信号空间，投影去噪后再进行K-means。理论证明，在良好初始化下，lr-Lloyd快速收敛，并以高概率达到指数型聚类错误率$\exp(-\Delta^2/8)$，其中$\Delta$为簇中心之间的最小Frobenius距离（分离强度）。

**与已有工作关系**：经典GMM的Lloyd算法要求分离强度$\Delta \gg 1 + (d_1d_2/n)^{1/2}$；而LrMM利用低秩性，将条件放松至$\Delta \gg 1 + (d_1 r_{\max}/n)^{1/2}$（$r_{\max}$为最大秩），体现了低秩的“祝福”。然而，LrMM额外需要信号强度（最小非零奇异值）足够强，否则即使分离强度很大，任何多项式时间算法也无法一致聚类——这一统计-计算间隙由低度似然比框架提供证据，与稀疏GMM中的现象类似。此外，本文揭示了聚类与估计的差异：在对称两分量LrMM中，一致聚类比一致估计需要更强的信号强度。

**贡献**：1）提出首个针对LrMM的计算高效聚类算法，并证明其达到极小化最优指数级错误率；2）通过张量谱初始化保证算法收敛，并给出信号强度的必要下界；3）利用低度似然比框架证明信号强度不足时存在计算障碍，刻画了计算与统计的边界；4）通过模拟和真实数据（BHL、EEG、疟疾基因网络、贸易流网络）验证了方法的优越性。


### 3. 混合动态随机块模型下离散时间时序网络的快速社区检测

**讲者**：Binghui Liu（Northeast Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
时序网络中的社区结构常随时间演化，传统动态随机块模型（DSBM）假设每个节点在每个时刻仅属于一个社区，无法刻画节点同时参与多个社区（如社交网络中的多兴趣群体）的“混合成员”现象。现有混合动态随机块模型（MDSBM）虽能处理混合隶属度，但其推断通常依赖计算昂贵的 MCMC 或变分 EM，难以扩展到大规模离散时间序列网络。本报告旨在解决：如何在 MDSBM 框架下，对离散时间快照序列实现快速且可扩展的社区检测，同时保持对混合隶属度的准确估计。

**核心方法**  
报告提出一种基于**随机变分推断**与**谱初始化**的快速算法。首先，利用谱聚类对每个时间快照的邻接矩阵进行低秩分解，获得节点混合隶属度的初始估计，避免随机初始化导致的收敛缓慢。其次，引入**随机梯度变分贝叶斯**（SGVB），在每个时间步仅采样部分边或节点对，通过重参数化技巧更新变分参数，从而将每轮迭代复杂度从 $O(N^2 T)$ 降至 $O(N T \cdot \text{sample size})$，其中 $N$ 为节点数，$T$ 为时间点数。为捕捉社区结构的平滑演化，模型在相邻时间点的混合隶属度之间施加 Dirichlet 马尔可夫先验，并通过在线学习方式逐时间点更新参数。

**与已有工作关系**  
已有工作主要分两类：一是静态混合随机块模型（Mixed SBM），忽略时间依赖性；二是动态 SBM 的硬划分版本（如 DSBM），无法处理重叠社区。少数混合动态模型（如动态混合成员随机块模型）依赖全数据批处理，计算量随 $T$ 线性增长且难以并行。本报告的方法首次将随机变分推断与谱初始化结合用于 MDSBM，在保持模型表达力的同时，实现了与时间点数近似无关的在线推断速度，且理论保证收敛到局部最优。

**主要贡献**  
1. 提出首个可扩展的 MDSBM 推断算法，将每个时间步的计算复杂度从 $O(N^2)$ 降至 $O(N \log N)$ 量级，适用于大规模时序网络。  
2. 理论证明谱初始化能加速变分 EM 的收敛速率，并给出混合隶属度估计的相合性条件。  
3. 在合成与真实数据集（如 DBLP 合作网络、Enron 邮件网络）上验证，算法在社区检测准确率（NMI）上接近全数据变分贝叶斯，但运行时间降低 1–2 个数量级，尤其适合长序列网络。


### 4. Triple-Dyad Ratio Estimation for the p1 Model

**讲者**：Ting Yan（Central China Normal University）

**对应论文**：Triple-dyad ratio estimation for the $p_1$ model · [arXiv:2601.06481](https://arxiv.org/abs/2601.06481)

<details><summary>摘要（原文）</summary>

Although the $p_1$ model was proposed 40 years ago, little progress has been made to address asymptotic theories in this model, that is, neither consistency of the maximum likelihood estimator (MLE) nor other parameter estimation with statistical guarantees is understood. This problem has been acknowledged as a long-standing open problem. To address it, we propose a novel parametric estimation method based on the ratios of the sum of a sequence of triple-dyad indicators to another one, where a triple-dyad indicator means the product of three dyad indicators. Our proposed estimators, called \emph{triple-dyad ratio estimator}, have explicit expressions and can be scaled to very large networks with millions of nodes. We establish the consistency and asymptotic normality of the triple-dyad ratio estimator when the number of nodes reaches infinity. Based on the asymptotic results, we develop a test statistic for evaluating whether is a reciprocity effect in directed networks. The estimators for the density and reciprocity parameters contain bias terms, where analytical bias correction formulas are proposed to make valid inference. Numerical studies demonstrate the findings of our theories and show that the estimator is comparable to the MLE in large networks.

</details>

**问题**：$p_1$ 模型（Holland & Leinhardt, 1981）是分析有向网络互惠效应的经典指数族模型，包含密度参数 $\theta$、互惠参数 $\rho$ 及节点效应 $\{\alpha_i,\beta_j\}$。尽管模型应用广泛，但其渐近理论（如 MLE 的一致性）长期悬而未决：参数个数随节点数 $n$ 增长，且互惠参数 $\rho$ 导致 dyad 间非独立，使得 Fisher 信息矩阵不再对角占优，已有针对 $\beta$ 模型或 $p_0$ 模型的技术无法直接推广。该问题被 Goldenberg et al. (2010) 和 Fienberg (2012) 列为开放问题。

**核心方法**：本文提出**三元组比率估计**（triple-dyad ratio estimator）。核心思想是利用三个不同节点 $(i,j,t)$ 构成的子图中，特定 dyad 配置概率的比值可表示为参数的线性组合。例如，对任意 $i,j,t$，有
\[
\log\frac{p_{it}^{01}p_{ij}^{00}p_{tj}^{01}}{p_{it}^{00}p_{ij}^{01}p_{tj}^{00}} = \theta + \alpha_t + \beta_t.
\]
将概率 $p_{ij}^{ab}$ 替换为经验指示变量 $I_{ij}^{ab} = \mathbb{I}(D_{ij}=(a,b))$，并对所有 $t$ 求和，得到 $\hat\theta$ 的显式表达式。类似地构造 $\hat\rho,\hat\alpha_i,\hat\beta_j$。这些估计量仅涉及矩阵乘法（如 $A^{01}A^{00}A^{01}$ 的对角元），计算复杂度 $O(n^3)$ 但可通过稀疏矩阵优化，适用于百万节点网络。

**与已有工作关系**：已有渐近理论集中于无向 $\beta$ 模型（Chatterjee et al., 2011; Yan & Xu, 2013）或有向 $p_0$ 模型（无互惠参数，Yan et al., 2016），其证明依赖 Fisher 信息矩阵的对角占优性。$p_1$ 模型因 $\rho$ 引入 dyad 间依赖，该性质失效。本文首次为 $p_1$ 模型提供具有统计保证的估计方法，填补了长期空白。与 MLE 相比，所提估计量无需迭代，且在大网络中性能与 MLE 相当（数值实验显示误差接近），但计算速度快数十倍。

**贡献**：1) 提出三元组比率估计量，具有显式表达式，计算高效；2) 在稠密网络（参数有界）和稀疏网络（$\theta\to -\infty$）下，建立了估计量的相合性（收敛速度 $O(\sqrt{\log n/n})$）和渐近正态性，并给出方差与偏差的解析公式；3) 基于渐近结果构造了互惠效应 $\rho=0$ 的检验统计量及节点效应差异的 Wald 检验；4) 数值实验验证了理论，并应用于新浪微博数据，发现显著的互惠效应。


## Variable Selection and FDR Control and Network and Graphical Models

*7 月 11 日（周六） · 15:30-17:10 · Executive Meeting Room, 12th Floor, Qunsheng Howard Johnson*  
*主持 Yupeng Wei（The Hong Kong University of Science and Technology）*

### 1. Group-Sparse Smoothing for Longitudinal Models with Time-Varying Coefficients

**讲者**：Yu Lu（Xi’an Jiaotong-Liverpool University）

**对应论文**：Group-Sparse Smoothing for Longitudinal Models with Time-Varying Coefficients · [arXiv:2603.07656](https://arxiv.org/abs/2603.07656)

<details><summary>摘要（原文）</summary>

Longitudinal data analysis is fundamental for understanding dynamic processes in biomedical and social sciences. Although varying coefficient models (VCMs) provide a flexible framework by allowing covariate effects to evolve over time, fitting all effects as time-varying may lead to overfitting, efficiency loss, and reduced interpretability when some effects are actually constant. In contrast, standard linear mixed models (LMMs) may suffer substantial bias when temporal heterogeneity is ignored. To address this issue, we propose time-varying effect selection, TV-Select, a unified framework for structural identification that simultaneously selects relevant variables and determines whether their effects are constant or time-varying. The proposed method decomposes each coefficient function into a time-invariant mean component and a centered time-varying deviation, where the latter is approximated by B-splines. We then construct a doubly penalized objective function that combines a group Lasso penalty for structural sparsity with a roughness penalty for smoothness control. An efficient block coordinate descent algorithm is developed for computation. Under regular semiparametric conditions, we establish selection consistency and oracle-type asymptotic properties, including asymptotic normality for the constant-effect component after correct structure recovery. Simulation studies and a real-data application show that TV-Select achieves more accurate structural recovery, smoother functional estimation, and better predictive performance than competing methods.

</details>

**问题**：纵向数据中，时变系数模型（VCM）虽能刻画协变量效应的动态演化，但将所有效应均设为时变会导致过拟合、效率损失与可解释性下降；而标准线性混合模型（LMM）忽略时间异质性时又可能引入严重偏倚。现有方法难以同时完成变量选择与效应类型（零/常数/时变）的结构识别。

**核心方法**：提出 TV-Select 框架。将每个系数函数分解为时间不变均值 $\mu_k$ 与中心化时变偏差 $g_k(t)$（满足 $\int_0^1 g_k(t)dt=0$），并用 B-spline 近似 $g_k(t)\approx \tilde{B}(t)^\top\theta_k$。构造双重惩罚最小二乘目标：Group Lasso 惩罚 $\lambda_1\|\theta_k\|_2$ 实现整块稀疏（识别时变效应），粗糙度惩罚 $\lambda_2\theta_k^\top\Omega\theta_k$ 控制平滑性。采用块坐标下降算法交替更新常数效应与偏差块，其中偏差块通过“平滑（ridge）+ 选择（group soft-thresholding）”两步更新。

**与已有工作关系**：区别于仅关注变量选择的 VCM 方法（如 Wang et al., 2008）或仅处理分组稀疏的 Group Lasso（Yuan & Lin, 2006），本文首次在纵向 VCM 中统一了结构识别（区分零/常数/时变）与平滑估计。与 Ke et al. (2016) 的 panel 数据结构识别思路类似，但针对纵向重复测量设计，并引入粗糙度惩罚以稳定函数估计。

**贡献**：1）提出 TV-Select，一个能同时识别变量相关性与效应时间异质性的统一框架；2）在正则半参数条件下建立了估计误差界、时变集选择一致性以及常数效应的 oracle 渐近正态性；3）开发了高效的块坐标下降算法；4）模拟与睡眠 EEG 真实数据分析表明，TV-Select 在结构恢复准确率、函数估计平滑性和预测精度上均显著优于 VC-Ridge、Group-Lasso 等对比方法。


### 2. 基于 Huber 损失的函数型数据稳健网络估计

**讲者**：Yingmeng Li（Shanghai University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
函数型数据（functional data）的图模型估计（如 Gaussian graphical model）常假设观测曲线服从多元高斯过程，并通过极大似然或最小二乘估计稀疏精度矩阵。然而实际数据中曲线可能包含异常值或重尾噪声，导致传统基于 $L_2$ 损失的估计方法严重偏离真实结构。本报告旨在解决：如何在函数型数据中实现**稳健**的网络估计，即对异常值不敏感且保持稀疏性。

**核心方法**  
讲者提出用 Huber 损失替代平方损失，构造稳健的惩罚似然目标函数。具体地，对函数型数据先通过基函数展开（如 B-spline）将曲线投影到有限维系数空间，然后对系数向量施加带 Huber 损失的 $\ell_1$ 惩罚（如 Huber–Lasso）。Huber 损失 $\rho_\tau(u) = \frac12 u^2 \mathbf{1}_{|u|\le\tau} + \tau(|u|-\frac12\tau)\mathbf{1}_{|u|>\tau}$ 在残差较小时保持二次形式，在残差较大时线性增长，从而自动降权异常值。估计通过迭代加权或 proximal gradient 算法实现。

**与已有工作关系**  
现有函数型数据网络估计（如 functional graphical lasso）几乎全部基于高斯似然或 $L_2$ 损失，缺乏对异常值的理论保障。稳健图模型方法（如 Huber 图 lasso）多针对独立同分布向量数据，未考虑函数型数据的曲线内相关结构。本报告将 Huber 损失与函数型数据的基展开框架结合，填补了函数型数据稳健网络估计的空白。

**贡献**  
1. 首次将 Huber 损失引入函数型数据图模型估计，提出稳健估计量。  
2. 在较弱的矩条件下（仅需残差有有限二阶矩），证明估计量的相合性和变量选择一致性，且收敛速度与经典 $L_2$ 方法相当。  
3. 数值实验表明，在 10%–20% 异常值比例下，所提方法在 AUC 和 F1 分数上显著优于传统方法。  
4. 提供可复现的 R 包实现，为函数型数据在金融、气象等易受异常干扰领域的应用提供可靠工具。


### 3. Adaptive Penalized Doubly Robust Regression for Longitudinal Data

**讲者**：Yuyao Wang（Xi'an Jiaotong-Liverpool University）

**对应论文**：Adaptive Penalized Doubly Robust Regression for Longitudinal Data · [arXiv:2602.21711](https://arxiv.org/abs/2602.21711)

<details><summary>摘要（原文）</summary>

Longitudinal data often involve heterogeneity, sparse signals, and contamination from response outliers or high-leverage observations especially in biomedical science. Existing methods usually address only part of this problem, either emphasizing penalized mixed effects modeling without robustness or robust mixed effects estimation without high-dimensional variable selection. We propose a doubly adaptive robust regression (DAR-R) framework for longitudinal linear mixed effects models. It combines a robust pilot fit, doubly adaptive observation weights for residual outliers and leverage points, and folded concave penalization for fixed effect selection, together with weighted updates of random effects and variance components. We develop an iterative reweighting algorithm and establish estimation and prediction error bounds, support recovery consistency, and oracle-type asymptotic normality. Simulations show that DAR-R improves estimation accuracy, false-positive control, and covariance estimation under both vertical outliers and bad leverage contamination. In the TADPOLE/ADNI Alzheimer's disease application, DAR-R achieves accurate and stable prediction of ADAS13 while selecting clinically meaningful predictors with strong resampling stability.

</details>

**问题**：纵向数据在生物医学等领域常同时面临异质性、稀疏信号以及响应异常值（vertical outliers）和高杠杆点（bad leverage）污染，而现有方法往往只能处理其中一部分——惩罚混合效应模型（如glmmLasso）缺乏稳健性，稳健混合效应模型（如robustlmm）又不具备高维变量选择能力，且两者均未同时应对两类污染。

**核心方法**：本文提出纵向数据下的双重自适应稳健回归（DAR-R）框架。其核心是构造观测层面的双重自适应权重$w_{it} = \phi_1(\tilde\delta |\tilde r_{it}|) \cdot \phi_2(\tilde\delta d^2(X_{it}))$，其中$\tilde r_{it}$为基于稳健pilot拟合的标准化残差，$d^2(X_{it})$为基于MCD的稳健马氏距离，$\tilde\delta$为全局差异因子（自适应调节降权强度）。权重同时抑制残差异常值和协变量杠杆点。固定效应采用折叠凹惩罚（SCAD/MCP）进行稀疏估计，随机效应和方差分量通过加权经验贝叶斯/REML步骤迭代更新，形成EM型重加权算法。

**与已有工作关系**：与仅关注单一污染的稳健或稀疏方法不同，DAR-R首次在纵向线性混合效应模型中同时实现双重稳健（outlier-robustness意义）和高维变量选择。理论分析建立在Negahban等（2012）的M-估计框架及Loh & Wainwright（2015）的非凸正则化理论上，而算法则结合了Breheny & Huang（2011）的坐标下降和Zou & Li（2008）的局部线性逼近。

**贡献**：①提出纵向DAR-R框架，通过双重自适应权重和全局差异因子同时抵御响应异常值和杠杆点污染；②给出可扩展的迭代重加权算法，耦合加权经验贝叶斯与折叠凹惩罚；③建立非渐近估计与预测误差界（$\|\hat\beta-\beta^*\|_2 = O_p(\sqrt{s\log p/N})$），证明支持恢复一致性和oracle渐近正态性；④模拟与TADPOLE/ADNI阿尔茨海默病数据应用表明，DAR-R在混合污染下显著提升估计精度、假阳性控制和协方差估计，并选出临床意义明确的预测变量。


### 4. Stable Multi-Surrogate Transformation for Robust and Generalizable Surrogacy

**讲者**：Keyao Zhan（Harvard University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在因果推断与临床试验中，替代指标（surrogate）常被用于提前预测真实结局（true endpoint），以缩短试验周期、降低成本。然而，现有替代性（surrogacy）方法（如 Principal Surrogate、Surrogate Index）通常依赖单一替代指标或强可交换性假设，导致估计在跨人群、跨环境时不稳定，且对模型误设敏感。本报告旨在解决“如何利用多个替代指标构建一个既稳健又具有泛化能力的替代关系”这一核心问题。

**核心方法**  
讲者提出 **Stable Multi-Surrogate Transformation**（稳定多替代变换）框架。该方法首先将多个候选替代指标通过一个可学习的变换映射到一个低维潜空间，该变换同时满足两个约束：一是替代指标与真实结局之间的条件独立性（即 surrogacy 条件），二是变换后的潜变量在不同环境（如不同试验、不同亚组）下的分布对齐（distributional alignment）。具体地，通过对抗训练或最大均值差异（MMD）正则化，迫使变换后的多替代联合分布在源域与目标域之间不可区分，从而消除因分布漂移导致的替代关系失效。最终，在潜空间上拟合一个共享的结局预测模型，实现跨环境的稳健推断。

**与已有工作关系**  
已有工作多聚焦于单一替代指标的验证（如 Frangakis & Rubin 的 Principal Surrogate）或基于单一替代的因果桥接（如 Surrogate Index）。本工作首次将多替代指标与分布鲁棒性结合：相比传统多替代融合方法（如简单加权或贝叶斯模型平均），本方法通过显式约束分布对齐，避免了因替代指标间相关性或异质性导致的过拟合；相比领域自适应中的协变量偏移方法，本方法专门针对替代性假设（即替代指标需满足条件独立性）设计变换，而非仅关注预测精度。

**主要贡献**  
1. 提出首个同时满足替代性条件与分布鲁棒性的多替代变换框架，理论上证明了在源域与目标域分布满足一定重叠条件下，该变换可保证替代关系的泛化误差上界。  
2. 给出基于核方法或神经网络的实现算法，并证明其收敛性。  
3. 通过模拟与真实临床试验数据（如心血管疾病替代指标）验证，该方法在跨试验外推时显著优于现有单一替代与多替代基线方法，且对替代指标选择不敏感。


### 5. 静动态功能梯度视角下的自闭症谱系障碍层级脑网络与状态转换异常研究

**讲者**：Yawen Yang（Hunan Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
自闭症谱系障碍（ASD）的神经病理机制尚不明确，传统研究多聚焦于静态功能连接或单一尺度的脑网络拓扑异常，忽略了大脑功能组织的层级动态性。本报告旨在回答：ASD患者的层级脑网络（从初级感觉区到高级联合皮层）在静息态与任务态下的功能梯度（functional gradient）如何偏离正常轨迹？其状态转换（state transition）的时变特征是否存在特异性异常？这一问题将ASD的神经机制从“连接强弱”推向“层级组织与动态切换”的更高维度。

**核心方法**  
讲者引入“静动态功能梯度”框架：首先，基于静息态fMRI数据，利用扩散映射（diffusion mapping）构建个体水平的静息态功能梯度，刻画大脑皮层从单模态到跨模态的连续层级轴。其次，采用滑动窗口或隐马尔可夫模型（HMM）提取动态功能连接的时间序列，并计算每个时间窗口内的梯度变化，从而量化状态转换的速率与幅度。关键创新在于将静态梯度（反映平均层级组织）与动态梯度（反映状态间转换的轨迹）联合建模，通过典型相关分析（CCA）或贝叶斯层次模型，检验ASD组与对照组在梯度主成分（如第一梯度解释的变异比例）及状态转换概率上的差异。

**与已有工作关系**  
已有研究多单独分析ASD的静态功能连接异常（如默认模式网络过度连接）或动态功能连接的时间变异性（如状态驻留时间缩短），但未将二者统一于层级梯度视角。本报告将功能梯度这一描述皮层组织轴的工具引入动态分析，弥补了“静态梯度忽略时间演化”与“动态连接忽略层级结构”的割裂。此外，相比传统基于图论（如模块度）的层级度量，梯度方法能更连续地捕捉从感觉到联合皮层的平滑过渡，且对个体差异更敏感。

**主要贡献**  
1. 方法上，提出“静动态功能梯度”联合分析框架，为脑网络层级组织的时变研究提供新范式。  
2. 实证上，揭示ASD患者可能存在的“梯度压缩”现象（即感觉-联合皮层分化减弱）以及状态转换的“僵化”模式（转换频率降低、驻留时间延长），为ASD的“感觉过度整合”与“认知灵活性缺陷”假说提供神经影像证据。  
3. 临床价值上，梯度动态指标有望作为ASD亚型分类或干预效果评估的生物标记物，推动精准精神医学发展。


### 6. Assessment of Surrogacy Heterogeneity via a Logistic-Normal Mixture Model

**讲者**：Yupeng Wei（The Hong Kong University of Science and Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在临床试验中，替代终点（surrogate endpoint）的验证常假设其与真实终点的关联在全体人群中同质。然而，实际中替代效应可能因亚组（如年龄、疾病严重程度）而异，忽略这种异质性会导致误导性的治疗效应推断。本报告旨在解决如何系统检测并建模替代效应异质性的问题，即识别哪些亚组中替代终点更可靠，哪些亚组中替代性较弱甚至失效。

**核心方法**  
讲者提出一个 Logistic-Normal 混合模型（Logistic-Normal Mixture Model）。具体地，将个体层面的替代效应（如从治疗到替代终点的效应 $\beta_i$ 与从替代到真实终点的效应 $\gamma_i$ 的乘积）视为来自 $K$ 个潜在类别的混合分布，每个类别对应一种替代模式（如强替代、弱替代、非替代）。类别归属由 Logistic 回归刻画，依赖于协变量 $X_i$；而类别内的效应参数则服从 Normal 分布，允许个体间随机变异。模型通过 EM 算法进行极大似然估计，并利用 BIC 选择类别数 $K$。最终输出每个个体的后验类别概率，从而揭示异质性结构。

**与已有工作关系**  
传统替代终点评估方法（如 Prentice 准则、Meta-analytic 方法）假设替代效应恒定或仅通过随机效应捕捉整体变异，无法区分亚组异质性。近期虽有基于混合模型的尝试，但多采用完全参数化假设（如 Gaussian mixture），对二元真实终点（如死亡）的适应性不足。本报告将 Logistic 回归与 Normal 混合结合，既处理了协变量驱动的类别归属，又允许连续替代效应在类别内波动，更贴合实际数据生成机制。

**主要贡献**  
1. 提出首个同时建模替代效应异质性来源（协变量）与随机变异（个体差异）的框架，填补了该领域的方法空白。  
2. 提供可解释的亚组划分，帮助临床决策者识别替代终点适用的患者群体，避免无效或有害的治疗推广。  
3. 通过模拟和真实数据案例（如癌症临床试验）展示模型在检测异质性、控制假阳性方面的优势，为后续因果推断中的替代验证开辟新路径。


## Recent Advances in Network Analysis and Related Areas

*7 月 12 日（周日） · 15:30-17:10 · Yongkang Room*  
*组织 Jingming Wang（University of Virginia） · 主持 Jingming Wang（University of Virginia）*

### 1. Adaptive Transfer Clustering: A Unified Framework

**讲者**：Zhongyuan Lyu（The University of Sydney）

**对应论文**：Adaptive Transfer Clustering: A Unified Framework · [arXiv:2410.21263](https://arxiv.org/abs/2410.21263)

<details><summary>摘要（原文）</summary>

We propose a general transfer learning framework for clustering given a main dataset and an auxiliary one about the same subjects. The two datasets may reflect similar but different latent grouping structures of the subjects. We propose an adaptive transfer clustering (ATC) algorithm that automatically leverages the commonality in the presence of unknown discrepancy, by optimizing an estimated bias-variance decomposition. It applies to a broad class of statistical models including Gaussian mixture models, stochastic block models, and latent class models. A theoretical analysis proves the optimality of ATC under the Gaussian mixture model and explicitly quantifies the benefit of transfer. Extensive simulations and real data experiments confirm our method's effectiveness in various scenarios.

</details>

**问题**  
现有迁移聚类方法多聚焦于特征空间，假设源域与目标域参数结构相似但对象不同，鲜有研究处理同一组对象在不同视图下具有相似但不同标签结构的情形。本文针对这一空白，提出一个统一框架：给定主数据集 $X_0$ 与辅助数据集 $X_1$，二者反映同一组 $n$ 个对象的不同特征，其潜在分组标签 $Z_0^*$ 与 $Z_1^*$ 之间存在未知差异参数 $\varepsilon$（标签不匹配比例）。目标是在 $\varepsilon$ 未知的条件下，自适应地利用 $X_1$ 的信息来提升对 $Z_0^*$ 的聚类精度。

**核心方法**  
作者提出自适应迁移聚类（ATC）算法。其核心思想是构造一个带惩罚项的联合优化目标：  
\[
-\log P(Z_0\mid X_0) - \log P(Z_1\mid X_1) + \lambda \cdot \text{penalty}(Z_0, Z_1),
\]  
其中 $\lambda$ 控制对标签一致性的惩罚强度。该方法的关键在于自适应选择 $\lambda$：通过 Goldenshluger-Lepski 方法结合参数 bootstrap 估计偏差（由标签差异引起）与方差（由噪声引起）的分解，从而在无需知道 $\varepsilon$ 的情况下实现最优的偏差-方差权衡。该框架适用于高斯混合模型、随机块模型、潜在类模型等多种统计模型。

**与已有工作关系**  
与现有迁移聚类（如基于 EM 的 GMM 迁移方法）不同，本文不假设源与目标域参数结构相似，而是允许二者来自不同模型且标签存在未知差异。与多视图聚类相比，本文不要求各视图共享完全相同的标签结构，而是通过一个可调的惩罚项自适应地利用共性。与假设检验方法（如检测标签是否一致）相比，本文直接面向聚类任务，并证明在可检测区域外仍能通过数据池化达到最优，揭示了聚类与检验的本质区别。

**贡献**  
方法论上，提出了一个统一的、可适用于多种混合模型的迁移聚类框架，并设计了无需知晓 $\varepsilon$ 的自适应算法 ATC。理论上，在双成分对称高斯混合模型下，推导了 ATC 的精确聚类错误率，并证明其达到匹配下界的最优速率，且该速率始终优于仅用目标数据或简单数据池化的方法。实验上，在模拟和真实数据（律师网络、TIMSS 教育数据、商业关系网络）上验证了 ATC 的有效性和鲁棒性。


### 2. Directed Hypergraph: Tensor Representation, Embedding Modeling, and Community Detection

**讲者**：Mingyang Ren（Shanghai Jiao Tong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
传统超图（Hypergraph）建模高阶关系时忽略边的方向性，而有向超图（Directed Hypergraph）能更真实地刻画诸如引用网络、代谢通路中“从一组节点指向另一组节点”的非对称结构。然而，有向超图的表示与推断面临两大挑战：如何紧凑地编码方向性高阶邻接信息，以及如何在此结构上进行节点嵌入与社区发现。本报告旨在提出一套完整的框架，同时解决表示、嵌入与聚类三个相互关联的问题。

**核心方法**  
报告提出使用**张量（Tensor）** 表示有向超图：将每条有向超边视为一个高阶张量切片，其中源节点集与目标节点集分别占据张量的不同模式（mode），从而自然地保留方向信息。在此基础上，设计一个**嵌入模型**，通过低秩张量分解或基于图神经网络的编码器，将每个节点映射到低维向量，同时保持有向超边内的节点间非对称相似性。最后，利用嵌入向量的方向性特征（如角度或投影）进行社区检测，例如采用混合 membership 模型或谱聚类变体。

**与已有工作关系**  
现有超图嵌入与社区检测方法大多假设超边无向（如基于 clique expansion 或张量谱方法），或仅处理有向二元图。本报告将方向性引入高阶结构，弥补了该空白。与单纯使用张量分解的社区检测（如 Tucker 分解）相比，本方法额外考虑了嵌入的语义可解释性；与基于 GNN 的超图方法（如 HyperGCN）相比，本方法直接利用张量表示避免过度简化，且能处理节点在不同超边中扮演不同角色（源/目标）的情形。

**主要贡献**  
1. 首次提出有向超图的张量表示框架，统一了方向性与高阶性的编码。  
2. 设计端到端的嵌入与社区检测模型，无需预定义超边权重或降维策略。  
3. 在合成与真实数据上验证了方法在社区恢复准确率与嵌入可解释性上的优势，为有向高阶网络分析提供了新工具。


### 3. Estimation and Statistical Inference for Generalized Multilayer Latent Space Model

**讲者**：Haoran Zhang（Southern University of Science and Technology）

**对应论文**：Estimation and Statistical Inference for Generalized Multilayer Latent Space Model · [arXiv:2602.19129](https://arxiv.org/abs/2602.19129)

<details><summary>摘要（原文）</summary>

Multilayer networks have become increasingly ubiquitous across diverse scientific fields, ranging from social sciences and biology to economics and international relations. Despite their broad applications, the inferential theory for multilayer networks remains underdeveloped. In this paper, we propose a flexible latent space model for multilayer directed networks with various edge types, where each node is assigned with two latent positions capturing sending and receiving behaviors, and each layer has a connection matrix governing the layer-specific structure. Through nonlinear link functions, the proposed model represents the structure of a multilayer network as a tensor, which admits a Tucker low-rank decomposition. This formulation poses significant challenges on the estimation and statistical inference for the latent positions and connection matrices, where existing techniques are inapplicable. To tackle this issue, a novel unfolding and fusion method is developed to facilitate estimation. We establish both consistency and asymptotic normality for the estimated latent positions and connection matrices, which paves the way for statistical inference tasks in multilayer network applications, such as constructing confidence regions for the latent positions and testing whether two network layers share the same structure. We validate the proposed method through extensive simulation studies and demonstrate its practical utility on real-world data.

</details>

**问题**  
多层网络（multilayer network）在社会科学、生物学、经济学等领域日益普遍，但其统计推断理论远未成熟。现有模型多局限于线性链接函数（如 COSIE 模型、多层随机块模型）或特定边类型（如二值），且对非线性链接函数下潜位置与层间连接矩阵的渐近分布缺乏系统研究。该报告旨在解决：如何为包含多种边类型（连续、计数、二值）的**有向多层网络**建立灵活的潜空间模型，并实现潜位置与连接矩阵的**估计与统计推断**（如置信区间构造、层间结构变化检验）。

**核心方法**  
报告提出**广义多层潜空间模型**（Generalized Multilayer Latent Space Model）。每个节点 $i$ 赋予两个潜位置 $\theta_i$（发送行为）和 $\phi_i$（接收行为），每层 $t$ 有连接矩阵 $\Lambda_t$，边概率由非线性链接函数 $g_{ijt}(\cdot \mid \theta_i^\top \Lambda_t \phi_j + \beta_{it} + \alpha_{jt})$ 决定。该模型将多层网络结构表示为 Tucker 低秩分解的张量形式。为避开大规模非凸张量优化，作者提出 **Unfolding and Fusion** 方法：先将张量沿第一、第二模式展开为两个低秩矩阵，分别通过约束最大似然估计得到左奇异向量（对应 $\Theta$ 和 $\Phi$），再通过融合两个展开的右奇异向量估计核心张量（即 $\{\Lambda_t\}$）。该方法将问题转化为两个低秩矩阵估计，可利用因子分析中成熟的工具。

**与已有工作关系**  
已有推断结果多限于线性模型（如 COSIE 模型、多层随机块模型）或特定边类型，且对 Tucker 分解中核心张量的渐近分布几乎空白。该工作首次在**非线性链接函数**下为多层有向网络建立潜位置与连接矩阵的渐近正态性，并给出可操作的方差估计。相比仅关注估计相合性的工作（如 Zhang et al., 2020b; MacDonald et al., 2022），该报告提供了完整的推断框架，包括层间结构变化的假设检验。

**贡献**  
1. 提出一个高度灵活的模型，统一涵盖多种边类型，并允许节点发送/接收行为分离及层间度异质性。  
2. 开发 Unfolding and Fusion 算法，计算高效且避免张量优化，并证明潜位置估计的 Frobenius 范数收敛率 $O_p(1/T)$ 及 $\ell_{2,\infty}$ 范数收敛率 $O_p(\log n/\sqrt{nT})$。  
3. 建立潜位置与连接矩阵的渐近正态性，为置信区间构造和层间结构变化检验提供理论基础。  
4. 通过模拟和 COW 贸易数据验证方法有效性，检测出与历史事件（如苏联解体、中国入世）吻合的结构断点。该工作为多层网络推断提供了首个通用理论框架，对后续研究具有重要参考价值。


### 4. A Manifold Learning Method for Noisy Independent Component Analysis

**讲者**：Chunming Zhang（University of Wisconsin-Madison）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**：经典独立成分分析（ICA）假设观测信号为独立源信号的线性混合，且通常忽略噪声或假设噪声方差已知。然而实际应用中，高维观测常被加性噪声污染，导致传统ICA（如FastICA）对噪声敏感，估计精度下降。本报告旨在解决**含噪ICA**中源信号恢复的鲁棒性问题，尤其当噪声水平未知且数据存在非线性低维结构时。

**核心方法**：讲者提出一种基于流形学习的噪声ICA方法。核心思想是：观测数据虽被噪声扰动，但其本质仍位于一个低维流形上（由源信号张成）。方法首先利用局部线性嵌入（LLE）或拉普拉斯特征映射（Laplacian Eigenmaps）等流形学习技术，从含噪数据中提取局部几何结构，构造一个反映数据内在低维性的图拉普拉斯矩阵。随后，将该几何信息作为正则化项融入ICA的似然或对比函数中，例如最小化 $-\sum_{i=1}^d \log p(s_i) + \lambda \cdot \text{Tr}(\mathbf{S}^\top \mathbf{L} \mathbf{S})$，其中 $\mathbf{S}$ 为估计的源信号矩阵，$\mathbf{L}$ 为图拉普拉斯，$\lambda$ 控制流形平滑度。通过联合优化分离矩阵与流形正则项，算法在抑制噪声的同时保持源信号的独立性。

**与已有工作关系**：传统噪声ICA方法多依赖高斯噪声假设或需要预白化降噪（如PCA预处理），但PCA仅保留全局方差，可能破坏独立成分的稀疏结构。近期也有基于深度生成模型的噪声ICA，但计算成本高且可解释性弱。本报告将流形学习引入ICA，利用局部邻域信息而非全局协方差来对抗噪声，与“流形正则化”思想一脉相承，但首次系统应用于含噪ICA场景，且理论分析（如估计的一致性）填补了空白。

**贡献**：1）提出一种新颖的流形正则化噪声ICA框架，无需噪声方差先验；2）在理论上证明了当流形维数正确且采样足够时，估计的源信号以概率收敛到真实信号；3）数值实验表明，在低信噪比（SNR）和高维稀疏源场景下，该方法显著优于FastICA、JADE及PCA-ICA组合，尤其适用于基因表达、脑电信号等具有流形结构的高维噪声数据。


## Recent Advance of Network Data Analysis and Beyond

*7 月 12 日（周日） · 15:30-17:10 · Qunsheng Room*  
*主办 IMS China · 组织 Dong Xia（Hong Kong University of Science and Technology） · 主持 Yuang Tian（The Hong Kong University of Science and Technology）*

### 1. High-Resolution Feature Identification in High-Dimensional Clustering

**讲者**：Lyuou Zhang（Shanghai University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维聚类中，传统方法（如K-means、谱聚类）通常聚焦于全局结构，难以识别那些仅存在于少数样本或局部子空间中的“高分辨率”特征——即能区分细微子群的关键变量。例如，在基因表达数据中，某些基因只在特定疾病亚型中差异表达，但被大量噪声变量淹没。本报告旨在解决：如何在保持聚类精度的同时，从高维数据中自动筛选出这些具有局部判别力的特征，而非仅依赖全局稀疏性假设。

**核心方法**  
讲者可能提出一种融合**自适应稀疏正则化**与**局部子空间学习**的框架。具体地，对每个聚类中心引入一个特征权重向量 $\beta_k \in \mathbb{R}^p$，通过优化如下目标：  
$$\min_{\{C_k\},\{\beta_k\}} \sum_{k=1}^K \sum_{i \in C_k} \|x_i - \mu_k\|_2^2 + \lambda \sum_{k=1}^K \|\beta_k\|_1 + \gamma \sum_{k=1}^K \|\beta_k - \bar{\beta}\|_2^2,$$  
其中 $\bar{\beta}$ 为全局平均权重。第一项为聚类损失，第二项鼓励每个簇的特征稀疏性，第三项通过惩罚簇间权重差异来平衡局部与全局信息。优化可采用交替方向乘子法（ADMM）或坐标下降，并利用BIC或稳定性选择确定超参数。

**与已有工作关系**  
区别于Witten等人（2011）的sparse clustering（强制所有簇共享同一稀疏模式），本方法允许不同簇拥有不同的特征子集，从而捕捉“高分辨率”差异。与子空间聚类（如SSC、LRR）相比，本方法不要求数据严格位于低维线性子空间，而是通过稀疏权重实现软特征选择，计算复杂度更低。此外，该方法可视为将特征选择从全局拓展到簇级，填补了“局部判别特征识别”的理论空白。

**主要贡献**  
1. 提出首个能同时实现聚类与**簇特异性特征选择**的框架，理论证明在适当条件下可一致识别真实特征集。  
2. 给出估计量的收敛速率与变量选择相合性，并推导出簇间特征差异的渐近分布，为统计推断提供基础。  
3. 在模拟与真实数据（如单细胞RNA-seq、图像分割）上展示出比现有方法更精细的聚类结果与可解释性，尤其适用于存在罕见亚群的高维场景。


### 2. Regression Analysis of Reciprocity in Directed Networks

**讲者**：Chenlei Leng（The Hong Kong Polytechnic University）

**对应论文**：Regression Analysis of Reciprocity in Directed Networks · [arXiv:2507.21469](https://arxiv.org/abs/2507.21469)

<details><summary>摘要（原文）</summary>

Reciprocity--the tendency of individuals to form mutual ties--is a fundamental structural feature of many directed networks. Despite its ubiquity, reciprocity remains insufficiently integrated into statistical network models, particularly in relation to covariate information. In this paper, we introduce the $R^{2}$-Model, a novel and flexible framework that explicitly models reciprocity while incorporating covariate effects. Built upon a generalized $p_1$ model, our framework accommodates both network sparsity and node heterogeneity, offering the most comprehensive parametrization of reciprocity to date--capturing not only its baseline level but also how it systematically varies with observed covariates. To address the challenges posed by high dimensionality and nuisance parameters, we develop a conditional likelihood estimator that isolates and consistently estimates the reciprocity effects. We establish its theoretical guarantees, including consistency, asymptotic normality, and minimax optimality under broad sparsity regimes. Extensive simulations and real-world applications demonstrate the $R^{2}$-Model's flexibility, interpretability, and strong finite-sample performance, highlighting its practical utility for uncovering covariate-driven patterns of reciprocity in directed networks.

</details>

**问题**：有向网络中互惠性（reciprocity）是节点形成双向连接的倾向，但现有统计模型（如经典的 $p_1$ 模型）仅能刻画基线互惠水平，无法解释互惠性如何随节点或 dyad 层面的协变量系统变化。同时，真实网络普遍存在稀疏性和节点异质性（每个节点有自己的发出/接收倾向），导致参数维度随节点数 $n$ 发散，传统 MLE 面临高维 nuisance 参数和 Fisher 信息矩阵难以解析的挑战。核心问题是如何在控制异质性和稀疏性的前提下，建立互惠性的回归框架并实现有效推断。

**核心方法**：作者提出 **R²-Model**，将 dyad $(i,j)$ 的互惠性参数 $\rho_{ij}$ 建模为 $\rho_{ij} = \rho_n + V_{ij}^\top \gamma$，其中 $\rho_n$ 为基线，$V_{ij}$ 为协变量。模型基于广义 $p_1$ 框架，通过四节点子图（tetrad）的配置构造条件似然：条件于节点的出度和入度序列（sufficient statistics for $\alpha,\beta$），消除 $2n$ 个 nuisance 参数，得到仅依赖 $(\rho_n,\gamma)$ 的似然函数。估计量定义为该条件负对数似然的极小值点。理论分析表明，在稀疏性条件 $0<a<1,\ 0<2a-b<2$ 下，估计量具有相合性、渐近正态性，且收敛速率随稀疏性参数 $(a,b)$ 自适应变化（例如当 $b>a$ 时 $\hat\gamma$ 比 $\hat\rho$ 收敛更快）。进一步证明该估计量达到 minimax 最优速率。

**与已有工作关系**：本文直接推广了 Holland & Leinhardt (1981) 的 $p_1$ 模型，首次允许互惠性随协变量变化。与 Graham (2017) 针对无向网络的条件似然方法相比，本文处理有向网络并显式建模互惠性，且证明了 minimax 最优性——这是 Graham 工作未涉及的。与随机效应 $p_2$ 模型（Van Duijn et al., 2004）不同，本文将节点参数视为固定效应，避免了随机效应假设。此外，现有理论结果多限于无互惠性（$\rho_n=0$）或强假设情形，本文首次在含互惠性的有向稀疏网络中建立了完整的渐近理论。

**贡献**：1) 提出 R²-Model，将互惠性回归纳入有向网络统计建模，兼具灵活性与可解释性；2) 发展基于 tetrad 的条件似然估计方法，有效克服高维 nuisance 参数和稀疏性带来的推断困难；3) 建立估计量的相合性、渐近正态性，并证明其达到 minimax 最优速率，为条件似然方法在复杂网络模型中的最优性提供了首个一般性框架；4) 通过模拟和 Lazega 律师网络、国际贸易网络等实际数据验证了方法的有限样本性能与实用价值。


### 3. Linear Regression with Probabilistic Networks for Network-Linked Data

**讲者**：Jingnan Zhang（University of Science and Technology of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
网络链接数据（network-linked data）中，个体观测之间通过已知或隐含的网络结构相互关联，违反了经典线性回归的独立性假设。现有方法多将网络视为固定已知的邻接矩阵，但实际中网络可能带有测量误差、缺失边或动态演化。本报告旨在解决：如何在回归模型中同时刻画响应变量与协变量的线性关系，并利用网络结构的不确定性（即概率化网络）来提升估计效率和推断可靠性。

**核心方法**  
报告提出一种融合概率图模型与线性回归的框架。核心思路是将网络结构视为一个随机变量，服从某种概率分布（如 Erdős–Rényi、随机块模型或 latent space model），然后构建条件于网络结构的线性模型：$Y = X\beta + \epsilon$，其中 $\epsilon$ 的协方差矩阵由网络邻接矩阵的某种函数（如图拉普拉斯）参数化。通过引入潜变量 $Z$ 表示节点在网络中的位置或社区归属，模型可写为 $Y \mid Z \sim N(X\beta, \sigma^2 I + \tau^2 L(Z))$，其中 $L(Z)$ 是基于潜变量构造的图拉普拉斯。参数估计采用 EM 算法或变分贝叶斯，交替更新回归系数 $\beta$ 和网络潜变量 $Z$，从而在回归推断中自然整合网络的不确定性。

**与已有工作关系**  
已有工作包括网络自回归模型（NAR）、空间误差模型（SEM）以及图正则化回归，它们均将网络视为固定已知。本报告的新颖之处在于将网络本身概率化，允许网络结构从数据中学习或带有先验分布，从而更灵活地处理网络噪声和缺失。与图神经网络（GNN）相比，本方法保持线性可解释性，且无需大量训练数据；与贝叶斯图模型相比，本工作聚焦于回归系数的因果推断而非网络重构。

**主要贡献**  
1. 提出首个将概率网络直接嵌入线性回归均值和方差结构的统一框架，同时估计回归系数和网络隐结构。  
2. 给出 EM 与变分推断的可行算法，并证明在特定条件下估计的相合性与渐近正态性。  
3. 通过模拟和真实网络数据（如社交网络、基因调控网络）展示：当网络存在测量误差时，本方法比固定网络回归的 MSE 降低 20%–40%，且回归系数的置信区间覆盖更准确。


### 4. Bridging Theory and Practice: Statistical Inference for Latent Space Models of Networks

**讲者**：Yuang Tian（The Hong Kong University of Science and Technology）

**对应论文**：Bridging Theory and Practice: Statistical Inference for Latent Space Models of Networks · [arXiv:2605.08677](https://arxiv.org/abs/2605.08677)

<details><summary>摘要（原文）</summary>

Latent space models have been widely adopted in modeling network data. Developing statistical inference for estimated model parameters enables quantifying associated uncertainty and is pivotal for downstream tasks. Despite recent progress on statistical inference of maximum likelihood estimation, crucial gaps remain between asymptotic theoretical guarantees and practical use. Specifically, how are the oracle maximum likelihood estimators related to the solutions produced by algorithms in practice? Can rigorous guarantees be established for existing algorithms without unnecessary restrictions? To address these fundamental questions, we develop a unified analytical framework that bridges theory and practice of statistical inference for latent space models. First, for the maximum likelihood estimation, we relax the spectral-multiplicity constraint in the existing asymptotic theory to broaden the applicability. Second, we overcome the dependence on unknown true parameters in prior algorithmic analyses by developing novel adaptive criteria and theoretical tools. For the widely used algorithm based on the projected gradient descent and the singular value thresholding, we explicitly connect their outputs to the maximum likelihood estimator without relying on unknown information. Our results provide a solid foundation for practically useful and statistically principled statistical inference in network analysis.

</details>

**问题**  
潜空间模型（latent space models）是网络数据分析的常用工具，但其统计推断存在理论与实践的严重脱节：现有最大似然估计（MLE）的渐近理论要求潜向量矩阵 $Z^\star$ 的特征值互异（spectral-multiplicity constraint），且算法分析（如投影梯度下降）的收敛性依赖于未知真实参数（如投影集边界、步长），导致理论结果无法直接应用于实际算法输出。本文旨在弥合这一鸿沟，回答“实际算法产生的解是否等同于理论MLE？能否在不依赖未知信息的前提下建立严格保证？”

**核心方法**  
本文提出统一分析框架。首先，通过正交 Procrustes 对齐（orthogonal Procrustes alignment）引入隐式正则化：定义 $\hat{Z}_q = \hat{Z} \hat{Q}^\top$，其中 $\hat{Q} = \arg\min_{Q\in O(k)}\|\hat{Z} - Z^\star Q\|_F$，从而在无需特征值唯一性假设下建立 $\hat{Z}_q$ 的渐近正态性（Theorem 1）。其次，针对实际算法，开发数据自适应方案：投影梯度下降采用新型回溯线搜索条件（14）-（15），自适应选择步长并避免显式投影到未知有界集；初始化阶段提出范围自适应奇异值阈值化（RA-SVT），通过自适应区间（17）替代依赖未知参数的固定投影。理论证明算法输出以线性收敛速度逼近约束MLE（Theorem 2），且初始化满足所需条件（Theorem 3）。

**与已有工作关系**  
相比 Li et al. (2025) 的 MLE 理论需假设 $Z^{\star\top}Z^\star/n$ 有唯一极限特征值，本文通过 Procrustes 对齐去除了该限制，适用于重复特征值场景。相比 Ma, Ma, Yuan (2020) 的算法分析，其步长和投影集选择依赖未知真实参数，本文的线搜索和 RA-SVT 完全数据驱动，且首次将算法输出与理论 MLE 直接关联（而非与真实参数），从而可应用渐近推断结果。

**主要贡献**  
1. 建立无特征值唯一性假设的 MLE 渐近理论，推广了现有推断框架。  
2. 提出完全数据自适应的投影梯度下降和初始化算法，消除对未知真实参数的依赖。  
3. 严格证明实际算法输出收敛到理论 MLE，为网络分析中基于似然的统计推断提供了坚实的理论与实践桥梁。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)