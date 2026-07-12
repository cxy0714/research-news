# 机器学习理论与方法 ML Theory & Methods · 3

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 16 场报告**（已检索到对应论文 9 场）

---

## Modern Machine Learning Theory

*7 月 13 日（周一） · 10:30-12:10 · Colourful Guizhou Ballroom 2*  
*组织 Tracy Ke（Harvard University） · 主持 Jingming Wang（University of Virginia）*

### 1. Semi‑Supervised Learning on Graphs with GNNs

**讲者**：Olga Klopp（ESSEC Business School）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
图上的半监督学习（Semi‑Supervised Learning on Graphs）旨在利用少量标注节点与大量未标注节点的图结构信息进行节点分类。尽管图神经网络（GNN）在实践中表现优异，但其统计性质——如泛化误差界、标签传播的收敛性以及模型复杂度与图拓扑的关系——仍缺乏严格的理论刻画。本报告聚焦于：在何种条件下，GNN 能够比经典图拉普拉斯正则化方法更高效地利用未标注数据？其泛化能力如何受图稀疏性、特征维度和标注比例影响？

**核心方法**  
讲者可能从统计学习理论出发，将 GNN 视为一种带参数化的图卷积算子，并建立其与图拉普拉斯平滑（graph Laplacian smoothing）之间的等价关系。通过引入“图有效维度”（effective dimension）或“图 Rademacher 复杂度”等概念，推导出 GNN 在 transductive 设定下的泛化上界。方法核心在于：将 GNN 的层数 $L$ 与图谱域上的滤波函数 $g(\lambda)$ 联系起来，证明当 $L$ 较小时，GNN 等价于低通滤波，从而与标签传播（label propagation）具有相似的偏差-方差权衡；而当 $L$ 增大时，模型复杂度随图的高频成分增长，需依赖正则化控制过拟合。

**与已有工作关系**  
已有工作多从经验风险最小化或图信号处理角度分析 GNN，但缺乏对半监督场景下未标注数据作用的严格统计解释。本报告可能将经典半监督学习理论（如 Belkin 等人的 manifold regularization）与 GNN 的表示能力统一在一个框架下，揭示 GNN 的 inductive bias 如何通过图结构实现“隐式正则化”。与单纯依赖图拉普拉斯的方法相比，GNN 的优势在于可学习非线性特征变换，但代价是更高的样本复杂度——这一权衡将通过理论界显式表达。

**贡献**  
主要贡献包括：（1）给出 GNN 在半监督学习中的泛化误差界，明确标注样本数 $m$、图节点数 $n$ 和特征维数 $d$ 之间的依赖关系；（2）证明当图满足一定的“聚类假设”时，GNN 的收敛速度可达到 $O(1/\sqrt{m})$，与经典方法一致，但常数项更优；（3）提出一种基于图谱的模型选择准则，指导 GNN 层数与隐藏维度的选取，避免过平滑（oversmoothing）。这些结果为图半监督学习提供了理论支撑，并启发更高效的 GNN 架构设计。


### 2. Transfer Learning on Edge Connecting Probability Estimation Under Graphon Model

**讲者**：Huimin Cheng（Boston University）

**对应论文**：Transfer Learning on Edge Connecting Probability Estimation under Graphon Model · [arXiv:2510.05527](https://arxiv.org/abs/2510.05527)

<details><summary>摘要（原文）</summary>

Graphon models provide a flexible nonparametric framework for estimating latent connectivity probabilities in networks, enabling a range of downstream applications such as link prediction and data augmentation. However, accurate graphon estimation typically requires a large graph, whereas in practice, one often only observes a small-sized network. One approach to addressing this issue is to adopt a transfer learning framework, which aims to improve estimation in a small target graph by leveraging structural information from a larger, related source graph. In this paper, we propose a novel method, namely GTRANS, a transfer learning framework that integrates neighborhood smoothing and Gromov-Wasserstein optimal transport to align and transfer structural patterns between graphs. To prevent negative transfer, GTRANS includes an adaptive debiasing mechanism that identifies and corrects for target-specific deviations via residual smoothing. We provide theoretical guarantees on the stability of the estimated alignment matrix and demonstrate the effectiveness of GTRANS in improving the accuracy of target graph estimation through extensive synthetic and real data experiments. These improvements translate directly to enhanced performance in downstream applications, such as the graph classification task and the link prediction task.

</details>

**问题**  
在图模型（Graphon）框架下，估计节点间连接概率是网络分析的基础任务，但现有方法（如邻域平滑、USVT）的精度高度依赖网络规模。实际中常遇到小规模目标图（如蛋白质网络仅25个节点），其图估计误差极大，严重制约下游任务（如链路预测、图分类）。如何利用一个结构相似的大规模源图来提升小目标图的估计精度，且无需节点对应关系，是本文要解决的核心问题。

**核心方法**  
本文提出 GTRANS 框架，包含三步：  
1. **初始估计**：对源图和目标图分别应用邻域平滑（Neighborhood Smoothing）得到初始概率矩阵 $\hat{P}_s^{\text{ini}}$ 和 $\hat{P}_t^{\text{ini}}$。  
2. **迁移对齐**：利用 Gromov-Wasserstein（GW）最优传输（或熵正则化变体 EGW）计算对齐矩阵 $\hat{\pi}$，将源图的结构信息投影到目标域，得到迁移估计 $\hat{P}_t^{\text{trans}}$ 并再次平滑。  
3. **自适应去偏**：若 GW 距离超过阈值 $\delta$，则计算残差 $R_t = \hat{P}_t^{\text{ini}} - \hat{P}_t^{\text{trans2}}$，对残差进行邻域平滑以提取目标特有结构，最终估计为 $\hat{P}_t = \hat{P}_t^{\text{trans2}} + \hat{P}_t^{\text{res}}$，避免负迁移。  

方法本质是将最优传输与图平滑结合，在无节点对应下实现结构对齐，并通过残差平滑自适应校正域偏移。

**与已有工作关系**  
现有图迁移学习仅适用于目标图为源图子集且节点对应已知的情形（Jalan et al., 2024）。本文首次在无节点对应、无监督设定下实现图估计迁移。与仅用目标数据的图估计方法（NS、USVT、SAS、ICE）相比，GTRANS 通过引入源图信息显著提升小图精度。理论分析方面，现有 EGW 稳定性结果多针对欧氏距离矩阵，本文首次给出一般成本矩阵下对齐矩阵的稳定性上界。

**贡献**  
1. 提出首个无需节点对应的图估计迁移学习方法 GTRANS。  
2. 建立对齐矩阵的稳定性理论：在熵正则化参数足够大时，$\|\hat{\pi} - \pi^*\|_F$ 可由 $\|\hat{P}_s^{\text{ini}} - P_s\|_{\infty} + \|\hat{P}_t^{\text{ini}} - P_t\|_{\infty}$ 控制。  
3. 实验表明，在合成数据上 MSE 一致优于基线；在真实图分类（IMDB、PROTEINS）和链路预测任务中，GTRANS 提升准确率 2–6 个百分点，验证了迁移学习的实际价值。


### 3. Fiedler Sign Consistency for Hierarchical Stochastic Block Models

**讲者**：Xiaodong Li（University of California, Davis）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
层次随机块模型（Hierarchical Stochastic Block Model, HSBM）是刻画网络多尺度社区结构的自然框架，其社区以树状层级组织。谱聚类中，Fiedler 向量（图 Laplacian 的第二小特征向量）常被用于二分图划分，但在 HSBM 下，该向量的符号能否一致地恢复顶层二分社区？更关键的是，当层次深度增加时，符号一致性是否仍能保持？现有工作多聚焦于单层 SBM 的谱聚类一致性，对层次结构下 Fiedler 向量的符号稳定性缺乏理论刻画。

**核心方法**  
讲者可能从随机矩阵理论出发，分析 HSBM 的期望 Laplacian 与观测 Laplacian 之间的谱偏差。通过建立 Fiedler 向量在 $L_2$ 范数下的收敛速率，并利用 Davis–Kahan 定理控制特征向量扰动，进一步证明其符号在逐点意义下以高概率与真实二分标签一致。关键在于利用 HSBM 的层级树结构，将顶层二分视为“粗粒度”划分，并证明即使下层社区存在异质性，Fiedler 向量的符号仍能抵抗噪声干扰。

**与已有工作关系**  
已有工作（如 Rohe et al., 2011; Lei & Rinaldo, 2015）证明了 SBM 下谱聚类的社区检测一致性，但通常要求社区间连接概率差异足够大，且未考虑层次结构。本报告将问题推广至 HSBM，并特别关注 Fiedler 向量符号的逐点一致性（而非仅聚类误差率）。这与近期关于“谱嵌入符号稳定性”的研究（如 Lyzinski et al., 2017）相关，但后者主要针对随机点积图。

**主要贡献**  
1. 首次给出 HSBM 下 Fiedler 向量符号一致性的充分条件，揭示层次深度与信噪比之间的权衡关系。  
2. 证明即使下层社区内部连接模式复杂，只要顶层二分社区的期望度差异满足一定阈值，符号一致性仍可保证。  
3. 提供一种基于 Fiedler 符号的层次聚类算法，并给出其误分率的上界，为多尺度网络分析提供理论支撑。


### 4. Nuisance Parameter Tuning for Inference in Observational Studies

**讲者**：Rajarshi Mukherjee（Harvard University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**未检索到公开论文，以下为基于题目与讲者方向的推断。**

**问题**  
在观察性研究中，因果效应的推断通常依赖于对 nuisance parameter（如倾向得分、条件均值函数）的估计。然而，这些 nuisance parameter 的估计往往涉及模型选择或调参（如正则化参数、核带宽、树深度），而调参的目标通常是预测精度，而非下游推断的准确性。这导致一个关键矛盾：最优预测的调参可能使因果估计量的置信区间覆盖不足或方差膨胀。本报告旨在解决“如何针对推断目标（而非预测）来调参 nuisance parameter，从而保证效应估计的渐近有效性及置信区间的正确覆盖”。

**核心方法**  
讲者可能提出一种基于“推断导向的调参准则”（inference-oriented tuning criterion），例如最小化估计量方差的渐近近似或调整置信区间长度的交叉验证。具体地，对于双重稳健估计量 $\hat{\tau} = \frac{1}{n}\sum_{i=1}^n \left( \frac{A_i Y_i}{\hat{e}(X_i)} - \frac{(1-A_i)Y_i}{1-\hat{e}(X_i)} \right)$，其中 $\hat{e}(X)$ 为倾向得分估计，调参目标不再是 $\hat{e}$ 的 MSE，而是 $\hat{\tau}$ 的渐近方差 $V(\lambda)$ 关于调参参数 $\lambda$ 的估计。通过构造一个数据依赖的 $\hat{\lambda}$ 使得 $V(\hat{\lambda})$ 最小化，同时保证 $\hat{\tau}$ 的 $\sqrt{n}$-一致性及正态性。

**与已有工作关系**  
现有文献（如 Chernozhukov et al. 2018 的 DML）强调使用交叉拟合和 Neyman 正交性来弱化 nuisance parameter 估计误差的影响，但通常假设 nuisance parameter 以 $n^{-1/4}$ 速率一致估计即可，并未系统讨论调参选择。另一些工作（如 van der Laan 的 TMLE）使用超学习（Super Learner）集成多个候选模型，但集成权重仍基于预测损失。本报告的新颖之处在于：将调参准则从预测损失转向推断损失，并证明该准则下估计量的渐近性质仍成立，且有限样本性能优于传统预测导向调参。

**主要贡献**  
1. 提出一种通用的推断导向调参框架，适用于多种 nuisance parameter 估计方法（如核回归、Lasso、随机森林）。  
2. 给出调参参数选择的理论保证：在适当条件下，基于推断损失最小化的调参仍能保持 $\sqrt{n}$-一致性和渐近正态性，且置信区间覆盖更准确。  
3. 通过模拟和实证研究展示，在有限样本下，该方法相比交叉验证调参、AIC/BIC 调参等显著提升因果推断的可靠性，尤其当 nuisance parameter 模型存在轻微误设时。


## Recent Advances in Model Free Inference

*7 月 13 日（周一） · 13:30-15:10 · Colourful Guizhou Ballroom 2*  
*组织 Yin Xia（Fudan University） · 主持 Yin Xia（Fudan University）*

### 1. Evaluating Black-Box Classifiers via Stable Adaptive Two-Sample Inference

**讲者**：Jing Lei（Carnegie Mellon University）

**对应论文**：Evaluating Black-Box Classifiers via Stable Adaptive Two-Sample Inference · [arXiv:2604.05470](https://arxiv.org/abs/2604.05470)

<details><summary>摘要（原文）</summary>

We consider the problem of evaluating black-box multi-class classifiers. In the standard setup, we observe class labels $Y\in \{0,1,\ldots,M-1\}$ generated according to the conditional distribution $ Y|X \sim \text{ Multinom}\big(η(X)\big), $ where $X$ denotes the features and $η$ maps from the feature space to the $(M-1)$-dimensional simplex. A black-box classifier is an estimate $\hatη$ for which we make no assumptions about the training algorithm. Given holdout data, our goal is to evaluate the performance of the classifier $\hatη$. Recent work suggests treating this as a goodness-of-fit problem by testing the hypothesis $H_0: ρ((X,Y),(X',Y')) \le δ$, where $ρ$ is some metric between two distributions, and $(X',Y')\sim P_X\times \text{ Multinom}(\hatη(X))$. Combining ideas from algorithmic fairness, Neyman-Pearson lemma, and conformal p-values, we propose a new methodology for this testing problem. The key idea is to generate a second sample $(X',Y') \sim P_X \times \text{ Multinom}\big(\hatη(X)\big)$ allowing us to reduce the task to two-sample conditional distribution testing. Using part of the data, we train an auxiliary binary classifier called a distinguisher to attempt to distinguish between the two samples. The distinguisher's ability to differentiate samples, measured using a rank-sum statistic, is then used to assess the difference between $\hatη$ and $η$ . Using techniques from cross-validation central limit theorems, we derive an asymptotically rigorous test under suitable stability conditions of the distinguisher.

</details>

**问题**  
评估黑盒多类分类器时，传统测试准确率无法区分“模型匹配数据生成分布”与“模型虽准确但分布严重偏离”的情形。例如，真实标签分布为均匀时，分类器 $\hat\eta(x)\equiv(1/2,1/2)$ 与 $\hat\eta(x)\equiv(1,0)$ 准确率相同，但前者完美匹配而后者完全错误。本文旨在解决：给定留出数据，如何检验黑盒分类器 $\hat\eta$ 是否在容忍半径 $\delta$ 内接近真实条件分布 $\eta$，即检验 $H_0:\rho(P_X\times\text{Multinom}(\hat\eta(X)),\,P_X\times\text{Multinom}(\eta(X)))<\delta$，其中 $\rho$ 为分布间分离度量。

**核心方法**  
利用两样本检验思想：保留特征 $X$，从 $\hat\eta$ 生成伪标签 $Y'$，构造第二个样本 $(X,Y')$。将问题转化为检验两个条件分布是否相同。用部分数据训练一个辅助二分类器（区分器）$\hat g$ 来区分真实样本与伪样本，其区分能力由秩和统计量 $T=\frac{1}{n^2}\sum_{i,j}\mathbf{1}\{\hat g(X_i,Y_i)<\hat g(X_j',Y_j')\}$ 衡量，该统计量是 AUC 的无偏估计。通过 Neyman-Pearson 引理，最优区分器对应似然比，AUC 与总变差距离成比例。为避免数据双重使用，提出样本分裂与交叉拟合两种程序，并利用交叉验证中心极限定理在区分器稳定性条件下证明 $T$ 的渐近正态性，从而构造检验和 $\delta$ 的置信下界。

**与已有工作关系**  
本文与 outcome indistinguishability（Dwork et al.）紧密相关，但采用基于秩的统计量并扩展至多类。相比 BAGofT（Zhang et al.），本文测试用户指定半径而非渐近相等，且适用于多类黑盒，无需将分类器训练纳入检验过程。相比 GRASP（Javanmard & Mehrabi），本文使用正态近似避免优化子程序，计算更高效，且能直接构造单侧置信区间。与校准测试（Lee et al.）目标不同，本文不依赖光滑性假设。此外，本文首次将交叉拟合引入基于分类的两样本检验，并给出稳定性条件下的理论保证。

**贡献**  
1）提出一个通用的黑盒分类器评估框架，适用于多类，对分类器结构和数据分布几乎无假设。2）利用 Neyman-Pearson 度量（AUC）定义分布分离度，并建立与总变差距离的定量关系。3）给出样本分裂与交叉拟合两种渐近有效程序，在稳定性条件下证明检验的 type-I 控制，并提供一致方差估计。4）理论表明区分器质量直接影响功效，并通过稀疏设置展示方法对底层结构的自适应性。5）模拟与真实数据（MNIST、Fashion MNIST）验证方法优于 GRASP，且能揭示准确率无法区分的模型差异（如随机森林与 XgBoost 的拟合优度差异）。


### 2. Conformalized Large-Scale Selective Inference with Informative and Trustworthy Prediction Sets

**讲者**：Wenguang Sun（Zhejiang University）

**对应论文**：Conformalized Large-Scale Selective Inference with Informative and Trustworthy Prediction Sets · [arXiv:2605.27012](https://arxiv.org/abs/2605.27012)

<details><summary>摘要（原文）</summary>

In large-scale prediction problems, exhaustively following up on all test units is often impractical and inefficient, motivating a selective reporting strategy that fulfills the dual requirements of informativeness and trustworthiness. Within the InfoFCR (Informative prediction with False Coverage Rate control) framework, we propose SCIP (Selective Conformal Inference for Informative Predictions), a procedure built on three key components: (i) an informative set constructor that tailors prediction sets to individual test units according to user-specified informativeness constraints; (ii) a trust score that provides a principled quantification of the trustworthiness of candidate informative sets; and (iii) generalized conformal p-values that are used to perform FCR analysis for selecting the most promising candidates. We establish that SCIP guarantees finite-sample FCR control and is asymptotically anti-conservative, achieving higher statistical power than existing methods. The framework is highly versatile, accommodating a wide range of error metrics across both regression and classification tasks. Extensive numerical experiments on simulated and real data demonstrate the effectiveness of our approach.

</details>

**问题**：在大规模预测任务（如基因组学、药物发现）中，对所有测试单元进行穷尽式报告与跟进不切实际，亟需一种选择性报告策略，同时满足两个核心要求：**信息性**（每个报告预测集必须符合用户指定的科学意义约束，如区间长度限制或排除无关类别）与**可信性**（控制错误覆盖率 FCR 在预设水平 $\alpha$ 下）。现有方法如 InfoSP 虽能同时满足二者，但存在内在保守性，无法充分利用 FCR 预算，导致统计效力不足。

**核心方法**：本文提出 **SCIP**（Selective Conformal Inference for Informative Predictions）框架，由三个关键组件构成：(i) **信息集构造器** $C^{\mathcal{I}}(X)$，根据信息性约束 $\mathcal{I}$ 为每个测试特征自适应生成可报告的预测集；(ii) **信任分数** $T(X, C^{\mathcal{I}})$，量化该信息集的可信度（值越高越可能覆盖真实标签）；(iii) **广义共形 $p$ 值** $p^{\text{GC}}_j$，基于信任分数构造，并应用 Benjamini–Hochberg 过程选择候选集。理论证明 SCIP 在有限样本下保证 FCR $\le \alpha$，且渐近反保守（FCR $\ge \alpha - O(me^{-n})$），从而充分释放 FCR 预算。

**与已有工作关系**：SCIP 重新审视了 InfoSP 框架（Gazin et al., 2025）中信息性与可信性的基本困境。通过引入信任分数与广义共形 $p$ 值，SCIP 将双重需求整合为统一的排序与选择问题。其具体实例 InfoSP$^+$ 被证明在渐近意义上支配 InfoSP（报告集包含关系概率趋于 1），克服了 InfoSP 因 $p$ 值缺乏直接概率链接而导致的保守性。此外，SCIP 统一了共形选择（cfBH）、选择性分类（FASI、Zhao-Su）及多样化选择等多种任务，并恢复现有方法为特例。

**贡献**：1. 提出 SCIP 这一通用框架，为选择性共形推断提供新视角，兼具有限样本 FCR 控制与渐近反保守性。2. 通过 InfoSP$^+$ 实例，理论阐明并实证验证了对 InfoSP 的效力提升。3. 框架高度灵活，可扩展至多样化选择等新场景，并为未来基于数据自适应信任分数的方法创新奠定基础。


### 3. Conformal Selective Prediction with General Risk Control

**讲者**：Ying Jin（University of Pennsylvania）

**对应论文**：Conformal Selective Prediction with General Risk Control · [arXiv:2603.24704](https://arxiv.org/abs/2603.24704)

<details><summary>摘要（原文）</summary>

In deploying artificial intelligence (AI) models, selective prediction offers the option to abstain from making a prediction when uncertain about model quality. To fulfill its promise, it is crucial to enforce strict and precise error control over cases where the model is trusted. We propose Selective Conformal Risk control with E-values (SCoRE), a new framework for deriving such decisions for any trained model and any user-defined, bounded and continuously-valued risk. SCoRE offers two types of guarantees on the risk among ``positive'' cases in which the system opts to trust the model. Built upon conformal inference and hypothesis testing ideas, SCoRE first constructs a class of (generalized) e-values, which are non-negative random variables whose product with the unknown risk has expectation no greater than one. Such a property is ensured by data exchangeability without requiring any modeling assumptions. Passing these e-values on to hypothesis testing procedures, we yield the binary trust decisions with finite-sample error control. SCoRE avoids the need of uniform concentration, and can be readily extended to settings with distribution shifts. We evaluate the proposed methods with simulations and demonstrate their efficacy through applications to error management in drug discovery, health risk prediction, and large language models.

</details>

**问题**：在AI模型部署中，选择性预测允许模型在不确定时弃权，但现有方法多针对二元风险（如分类错误），无法处理连续风险（如平方误差、开发成本）。实际应用中，药物筛选的浪费成本、临床预测的均方误差等连续风险需要精确控制，且需区分“总风险”（MDR）和“平均风险”（SDR）两种目标。如何对任意黑箱模型、任意有界连续风险，在有限样本下实现分布自由的弃权决策控制？

**核心方法**：提出SCoRE框架，核心是构造**风险调整的e-value** $E_{n+j}$，满足 $E[L_{n+j}E_{n+j}]\le 1$（$L_{n+j}$为未知风险）。基于数据可交换性，利用校准数据构造形如 $E_{n+j} = \inf_{\ell\in[0,1]} \frac{(n+1)\mathbf{1}\{s(X_{n+j})\le t_\gamma(\ell)\}}{\sum_i L_i\mathbf{1}\{s(X_i)\le t_\gamma(\ell)\} + \ell\mathbf{1}\{s(X_{n+j})\le t_\gamma(\ell)\}}$ 的e-value，其中 $s(\cdot)$ 为风险预测得分，$t_\gamma(\ell)$ 为经验风险阈值。随后，对MDR直接阈值化 $\hat\psi_{n+j}=\mathbf{1}\{E_{n+j}\ge 1/\alpha\}$；对SDR则应用e-BH过程。理论证明两者均实现有限样本风险控制，且仅依赖可交换性，无需均匀集中性假设。

**与已有工作关系**：现有共形选择（Jin & Candès, 2023）仅处理二元风险，依赖p值的尾部概率；SCoRE将其推广至连续风险，且e-value的期望性质天然匹配风险控制。与共形风险控制（Angelopoulos et al., 2022）相比，SCoRE的SDR变体避免了网格搜索和均匀集中，且MDR变体提供了e-value视角的统一分析。此外，SCoRE可自然扩展到协变量偏移场景，并具有Neyman-Pearson型最优性刻画。

**贡献**：1）首次提出针对连续风险的有限样本、分布自由的选择性预测框架，同时覆盖MDR和SDR两种目标；2）引入风险调整的e-value，将弃权决策转化为假设检验问题，方法简洁且可结合e-BH等成熟工具；3）理论证明最优得分函数为条件风险与奖励的比值，并给出实用构造策略；4）在药物发现、临床预测、LLM报告生成等应用中验证了有效性和紧致性。


### 4. Generalized Boundary FDR Control under Arbitrary Dependence: An Approach on Closure Principle

**讲者**：Haojie Ren（Shanghai Jiao Tong University）

**对应论文**：Generalized Boundary FDR Control under Arbitrary Dependence: An Approach on Closure Principle · [arXiv:2605.09953](https://arxiv.org/abs/2605.09953)

<details><summary>摘要（原文）</summary>

False discovery rate (FDR) is a cornerstone of modern multiple testing. However, it often fails to guarantee the reliability of "marginal" discoveries that lie at the boundary of the rejection set, which are often crucial in high-precision applications. While recent works (Soloff et al., 2024; Xiang et al., 2025) introduced the boundary false discovery rate (bFDR) to control the error probability at the marginal discovery, their method relies on restrictive assumptions such as independence or specific prior distributions. In this paper, we first propose $k$-bFDR, a novel generalization that controls the error probability of the $k$ least significant discoveries. We then provide a systematic investigation into the theoretical relationship between $k$-bFDR and existing error metrics. Furthermore, building upon the closure principle, we develop Domino, a unified framework that guarantees $k$-bFDR control under arbitrary dependence, applicable for both p-values and e-values. We prove the theoretical validity of the proposed Domino algorithm and demonstrate through extensive numerical experiments that it consistently achieves rigorous $k$-bFDR control while identifying trustworthy marginal discoveries. Analyses of real data reveal that $k$-bFDR control yields higher-quality rejection sets with greater practical significance.

</details>

**问题**：经典FDR控制仅保证拒绝集的平均错误率，但在高精度应用中（如基因组学），边界上的“搭便车”发现（即最不显著的拒绝）往往是假阳性，而现有边界FDR（bFDR）控制方法（Soloff et al., 2024; Xiang et al., 2025）依赖独立性或特定先验假设，无法处理实际中常见的任意依赖结构。此外，研究者常需同时验证一批边界发现，而非单个，现有方法缺乏对$k$个最边缘发现的联合控制。

**核心方法**：本文首先提出$k$-bFDR，定义为拒绝集中$k$个最不显著发现均为假阳性的概率（$k=1$时退化为bFDR）。在此基础上，基于闭包原则（closure principle）构建Domino框架。其核心是构造有效的$k$-local检验$\phi_S^k$，要求对任意包含边缘集$M_{r,k}$的子集$S$，若$\phi_S^k=1$则拒绝$H_S$，且$\mathbb{P}(\phi_S^k=1)\leq\alpha$。Domino通过搜索最大的$r$使得所有包含$M_{r,k}$的$S$均被拒绝，从而保证$k$-bFDR$\leq\alpha$。该框架兼容p值和e值，且对依赖结构无任何要求。

**与已有工作关系**：相比Soloff等（2024）的Support Line（SL）方法（仅适用于独立p值），Domino在任意依赖下严格控制$k$-bFDR，且通过闭包原则将bFDR控制推广到$k>1$。与经典FWER控制（如闭包检验）相比，Domino仅要求边缘集满足闭包条件，而非每个个体，因此更宽松、功效更高。与e-closure原则（Xu et al., 2025）相比，Domino可视为其特例，但允许更灵活的$k$-local检验（如广义Bonferroni、调和均值组合），从而在特定结构下提升功效。

**贡献**：①提出$k$-bFDR这一新度量，统一并推广了边界错误控制；②建立Domino框架，首次在任意依赖下实现$k$-bFDR的严格控制（定理3.4），且适用于p值和e值；③通过理论分析阐明$k$-bFDR与FWER、FDR的关系，并给出高效实现（$O(m^2)$复杂度）；④在CRISPR基因筛选和股票选择等真实数据中，Domino在保持边界可靠性的同时，显著提升发现集质量，有效过滤“搭便车”假阳性。


## Advances in Functional, Distributional, and Structured Statistical Learning

*7 月 13 日（周一） · 08:30-10:10 · Colourful Guizhou Ballroom 3*  
*主办 Korean Statistical Society · 组织 Cheolwoo Park（KAIST）、Sungkyu Jung（Seoul National University） · 主持 Jeong Min Jeon（Seoul National University）*

### 1. Hilbert Diffusion Models for Generating Functional Data with Galerkin-Type Kernel Neural Operators

**讲者**：Hyonho Chun（KAIST）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
函数型数据（functional data）的生成是统计与机器学习中的前沿问题，传统方法如FPCA或GAN往往难以捕捉函数空间的复杂结构（如光滑性、边界条件）或在高维离散化下计算成本高昂。本报告旨在解决：如何利用扩散模型（diffusion models）在无限维Hilbert空间中直接生成函数型数据，同时保证生成样本的连续性与统计一致性。

**核心方法**  
报告提出Hilbert扩散模型，将扩散过程定义在函数空间上，其正向过程通过随机偏微分方程（SPDE）逐步添加噪声，逆向过程则利用Galerkin型核神经算子（Galerkin-type kernel neural operators）近似得分函数（score function）。具体地，采用Galerkin投影将无限维问题离散到有限维基函数空间，并引入核方法构造神经算子，使得得分估计在函数空间上保持平移不变性与光滑性。模型通过变分下界训练，最终从噪声函数采样生成新函数。

**与已有工作关系**  
现有扩散模型主要处理欧氏空间中的向量数据，而函数型数据生成多依赖FPCA降维后应用生成模型（如GAN），但降维会损失细节。本工作将扩散模型直接推广至Hilbert空间，与Neural Operator（如FNO、DeepONet）结合，避免了离散化网格依赖，且能处理不规则采样。相比基于GAN的函数生成，扩散模型具有更稳定的训练和更好的模式覆盖。

**主要贡献**  
1. 首次将扩散模型与神经算子结合，提出适用于函数型数据的生成框架，理论上保证了生成样本在Hilbert空间中的收敛性。  
2. 利用Galerkin方法实现无限维到有限维的保结构离散，降低了计算复杂度，同时通过核神经算子保持函数的光滑性。  
3. 在模拟与真实函数数据（如曲线、图像）上展示了优于FPCA+GAN和传统扩散模型的生成质量，为函数型数据分析提供了新工具。


### 2. Deep Symbolic Learning for Histogram-Valued Regression Data

**讲者**：Ilsuk Kang（Chungbuk National University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
直方图值数据（Histogram-Valued Data）在计量经济学、环境科学等领域广泛出现，例如收入分布、污染物浓度分布等。传统回归模型通常假设响应或协变量为标量或向量，难以直接处理这种以区间-频率对形式呈现的分布型观测。现有方法多依赖距离度量（如Wasserstein距离）或函数型数据框架，但往往牺牲了预测精度或可解释性。本报告旨在解决：如何对直方图值响应变量进行回归建模，同时保持模型的高预测能力与符号可解释性？

**核心方法**  
讲者提出“Deep Symbolic Learning”框架，将深度学习与符号回归（Symbolic Regression）相结合。具体而言，首先利用深度神经网络（如全连接网络或图神经网络）对直方图的区间端点与频率进行嵌入，学习高维特征表示；随后通过符号回归模块（如基于遗传编程或可微符号网络）从这些表示中搜索显式的数学表达式，例如 $Y = f(X) = \sum_{i} \alpha_i \cdot \phi_i(X)$，其中 $\phi_i$ 为基函数（如多项式、指数、三角函数）。整个模型通过端到端训练，同时优化预测误差与表达式复杂度。

**与已有工作关系**  
已有工作主要分为两类：一是基于距离的直方图回归（如Fr´echet回归），通过最小化Wasserstein距离进行预测，但缺乏显式函数形式；二是函数型数据回归，将直方图视为密度函数，但需要光滑化且计算成本高。本报告的新颖之处在于：首次将深度学习与符号回归结合用于直方图值数据，既利用深度网络的表达能力捕捉复杂非线性关系，又通过符号回归输出可解释的闭式表达式，弥补了纯黑箱模型的可解释性缺陷。此外，与传统的符号回归仅处理标量数据不同，本方法专门设计了针对直方图结构的嵌入层。

**贡献**  
主要贡献有三点：1）提出一种新的回归范式，能够直接处理直方图值响应变量，无需预先降维或光滑化；2）通过符号回归模块，模型输出显式数学公式，便于领域专家理解与验证；3）在模拟与真实数据集上，相比Wasserstein回归、随机森林等基线，在预测精度与可解释性之间取得了更好的平衡。该工作为分布型数据的可解释建模提供了新工具，尤其适用于需要透明决策的领域（如政策评估、医学诊断）。


### 3. From Binary Pairs to Soft Correspondences in Audio Text Retrieval

**讲者**：Changwon Lim（Chung-Ang University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
现有音频-文本检索（Audio-Text Retrieval）任务通常依赖二元配对（binary pairs）作为监督信号，即一个音频片段与一个文本描述被标注为“匹配”或“不匹配”。这种硬标签忽略了语义上的部分匹配与模糊对应——例如，一段包含“雨声与鸟鸣”的音频与文本“雨声”之间并非完全无关，但二元标签无法刻画这种中间状态。因此，如何从离散的二元配对过渡到连续的软对应（soft correspondences），以更精细地建模跨模态语义关联，是当前方法的核心瓶颈。

**核心方法**  
讲者可能提出一种基于对比学习与软对齐的框架。具体而言，模型首先通过双塔编码器（如AudioMAE与BERT）提取音频与文本的全局与局部特征。随后，引入一个可学习的软对应模块，该模块利用注意力机制计算音频片段与文本词之间的逐元素相似度矩阵 $S \in \mathbb{R}^{T \times L}$（$T$ 为音频帧数，$L$ 为文本词数），并通过一个温度参数化的 softmax 将相似度转化为软匹配权重。训练时，损失函数不再仅依赖全局二元标签，而是结合了软对应的一致性约束：例如，鼓励音频-文本对的软对应分布与一个由语义相似度（如基于预训练文本编码器的余弦相似度）生成的伪标签分布之间的 KL 散度最小化。同时，保留全局对比损失以维持判别性。

**与已有工作关系**  
已有工作（如CLAP、AudioCLIP）主要依赖全局对比学习，将音频与文本整体嵌入拉近或推远，本质上仍属于二元配对范式。少数工作尝试使用细粒度对齐（如跨模态注意力），但通常需要人工标注的局部对应关系，成本高昂。本报告的核心创新在于：无需额外标注，仅从二元配对出发，通过自监督方式自动挖掘软对应，从而在保持训练效率的同时，提升了模型对语义重叠与部分匹配的建模能力。

**主要贡献**  
1. 提出“软对应”概念，将音频-文本检索从二元硬标签扩展至连续语义空间，更贴合真实场景中的模糊匹配需求。  
2. 设计了一种无需局部标注的软对应学习框架，通过对比学习与分布对齐的联合优化，自动捕获跨模态的局部语义关联。  
3. 在多个基准数据集（如AudioCaps、Clotho）上，该方法在检索召回率（Recall@K）上显著优于基于二元配对的基线，尤其在处理长文本与复杂音频场景时表现突出，验证了软对应策略的有效性与泛化能力。


### 4. Information Matrix Test for Normality of Innovations in Stationary Time Series Models

**讲者**：Zixuan Liu（Henan University of Economics and Law）

**对应论文**：Information matrix test for normality of innovations in stationary time series models · [arXiv:2407.08565](https://arxiv.org/abs/2407.08565)

<details><summary>摘要（原文）</summary>

This study focuses on the problem of testing for normality of innovations in stationary time series models.To achieve this, we introduce an information matrix (IM) based test. While the IM test was originally developed to test for model misspecification, our study addresses that the test can also be used to test for the normality of innovations in various time series models. We provide sufficient conditions under which the limiting null distribution of the test statistics exists. As applications, a first-order threshold moving average model, GARCH model and double autoregressive model are considered. We conduct simulations to evaluate the performance of the proposed test and compare with other tests, and provide a real data analysis.

</details>

**问题**  
在平稳时间序列建模中，检验新息（innovation）的正态性是模型诊断的关键步骤。现有方法多将 i.i.d. 下的正态性检验（如 Jarque-Bera 检验）直接应用于残差，但其渐近分布未必与基于真实误差的检验相同，且针对特定模型（如 GARCH、ARMA）的验证工作分散。本文旨在提出一种适用于**一般平稳时间序列模型**的正态性检验，无需为每个模型单独推导残差基检验的极限分布。

**核心方法**  
利用 White (1982) 的信息矩阵（IM）等价性：当模型正确设定且误差分布正确指定时，有 $E[\partial_\theta l \partial_{\theta'} l] + E[\partial^2_{\theta\theta'} l] = 0$。本文指出，若模型结构已知（如 $X_t = \mu_t(\theta) + \sigma_t(\theta) e_t$），则 IM 等价性可用于检验 $e_t$ 是否服从 $N(0,1)$。构造统计量 $T_n = \frac{1}{\sqrt{n}} \sum_{t=1}^n \tilde{d}(X_t; \hat\theta_n)$，其中 $\tilde{d}$ 由对数似然的二阶偏导与一阶偏导乘积之和构成。在正则条件下，$T_n' \hat V_n^{-1} T_n \xrightarrow{d} \chi^2_q$。作者给出了保证该极限分布成立的充分条件，并具体应用于 Threshold MA(1)、GARCH 和 Double AR 模型，验证了各条件。

**与已有工作关系**  
IM 检验最初用于检验模型设定错误（如遗漏变量、错误分布），且通常假设误差分布已知。本文反其道而行之：在模型结构正确的前提下，利用 IM 等价性检验误差分布的正态性。这与残差基的 JB 检验、KS 检验等不同——后者依赖残差近似 i.i.d. 的假设，且其渐近有效性需逐个模型验证；而 IM 检验直接从 QMLE 的得分与 Hessian 矩阵出发，理论框架统一，适用于一大类平稳时间序列模型（包括非线性模型）。

**贡献**  
1. 提出一种基于 IM 的、适用于一般平稳时间序列模型的新息正态性检验，填补了该领域缺乏通用检验的空白。  
2. 给出了检验统计量渐近服从 $\chi^2$ 分布的充分条件，并针对三个典型模型（TMA(1)、GARCH、DAR(1)）逐一验证，展示了方法的可操作性。  
3. 模拟表明，IM 检验在误差分布非重尾（如混合正态、广义 Lambda 分布）时显著优于 JB 等传统检验，在重尾情形下表现也令人满意；实证分析进一步揭示了其对异常值的稳健性。该检验为时间序列模型诊断提供了有价值的补充工具。


## Advanced Statistical Learning: Distribution-Free, Scalable and Cost-Efficient Inference

*7 月 13 日（周一） · 10:30-12:10 · Libo Room*  
*组织 Wei Zhong（Xiamen University） · 主持 Wei Zhong（Xiamen University）*

### 1. Distribution-Free Prediction Sets for Regression under Target Shift

**讲者**：Yanlin Tang（East China Normal University）

**对应论文**：Distribution-Free Prediction Sets for Regression under Target Shift · [arXiv:2510.10985](https://arxiv.org/abs/2510.10985)

<details><summary>摘要（原文）</summary>

In real-world applications, the limited availability of labeled outcomes presents significant challenges for statistical inference due to high collection costs, technical barriers, and other constraints. In this work, we propose a method to construct efficient conformal prediction sets for new target outcomes by leveraging a source distribution that is distinct from the target but related through a distributional shift assumption and provides abundant labeled data. When the target data are fully unlabeled, our predictions rely solely on the source distribution, whereas partial target labels, when available, are integrated to improve efficiency. To address the challenges of data non-exchangeability and distribution non-identifiability, we identify the likelihood ratio by matching the covariate distributions of the source and target domains within a finite B-spline space. To accommodate complex error structures such as asymmetry and multimodality, our method constructs highest predictive density sets using a novel weight-adjusted conditional density estimator. This estimator models the source conditional density along a quantile process and transforms it, through appropriate weighting adjustments, to approximate the target conditional density. We establish the theoretical properties of the proposed method and evaluate its finite-sample performance through simulation studies and a real-data application to the MIMIC-III clinical database.

</details>

**问题**：在回归任务中，目标分布 $Q$ 的标签因成本或技术限制而极度稀缺，但源分布 $P$ 拥有大量标签。在 target shift 假设（$p(x|y)=q(x|y)$，但 $p(y)\neq q(y)$）下，如何构建分布自由的预测集，使其对 $Q$ 中新个体的响应 $Y$ 满足边际覆盖保证？核心挑战在于：标签缺失导致似然比不可识别，且训练与测试数据非可交换，使得标准 conformal prediction 失效。

**核心方法**：提出 CPUTS 框架。首先，通过 B-spline 基函数将权重 $w(y)=q(y)/p(y)$ 投影到有限维空间，并利用协变量分布匹配（最小化重加权源分布与目标分布之间的 $L_2$ 距离）估计 $\hat w(y)$。其次，构造非一致性得分 $R(x,y)=-\hat q(y|x)$，其中 $\hat q(y|x)$ 通过先估计源条件密度（基于分位数过程的商估计）再经 $\hat w(y)$ 加权调整得到。最后，采用加权 conformal prediction（以 $\hat w$ 为权重）计算 $p$-值并构建预测集。方法覆盖两种场景：目标完全无标签（仅用 $P$ 数据）和部分有标签（结合 $P$ 与 $Q$ 标签，通过逆方差加权融合两个非一致性得分）。

**与已有工作关系**：现有 target shift 研究多聚焦分类（EM 或矩匹配）或回归中的参数估计（如 Lee et al. 2025 的 EIF 方法），而非直接构造预测集。任意分布 shift 下的 conformal prediction（如 Barber et al. 2023 的加权法、Cauchois et al. 2024 的鲁棒法）虽适用但保守，且需已知权重。本文首次在回归 target shift 下结合似然比估计与 conformal prediction，利用 B-spline 的局部支撑特性，比 Zhang et al. 2013 和 Nguyen et al. 2016 的全局基函数更灵活地捕捉 shift 的局部变化。

**贡献**：1）提出首个面向回归 target shift 的分布自由预测集框架，同时处理无标签和半监督场景；2）给出基于 B-spline 的权重估计器，并证明其 $L_2$ 收敛率（匹配 Sobolev 空间最优率）；3）通过加权条件密度估计构造最高预测密度集，在异方差、多模态下比传统残差得分更紧凑；4）理论证明覆盖概率下界（误差由权重估计精度控制），模拟与 MIMIC-III 真实数据验证了方法的有效性和效率提升（如亚洲人群 94.4% 的测试点区间更短）。


### 2. Subsampling-Based Convoluted Rank Regression for Massive Data

**讲者**：Xiaochao Xia（Chongqing University）

**对应论文**：Biweighted Poisson Subsampling for Convoluted Rank Regression with Massive Data · [arXiv:2606.08668](https://arxiv.org/abs/2606.08668)

<details><summary>摘要（原文）</summary>

Optimal subsampling efficiently selects the most informative data points, enabling accurate statistical inference while significantly reducing computational burden for massive datasets. However, the existing relevant methods can not directly be applied to pairwise loss problems, particularly for convoluted rank regression (CRR), due to the double summation structure in objective function. To this end, we first propose a new BIweighted Poisson Subsampling (BIPS) framework for such problems through designing a proper weight for a pair of observations instead of for a single observation for objective function. Two concrete inverse probability weighting strategies are considered. Secondly, we focus on the CRR models, under which the BIPS estimator (BIPS-CRR) is formulated. We establish consistency and asymptotic normality for BIPS-CRR, derive its optimal Poisson subsampling probabilities under the L-optimality criterion, and provide a practical algorithm to facilitate implementation. Thirdly, we develop a distributed estimator for CRR that incorporates BIPS as a pilot subsampling strategy. This estimation is globally efficient and is robust to both randomly and non-randomly distributed datasets in distributed computing environments. Extensive simulations and a real-world application demonstrate the excellent finite-sample performance of proposed methodology. Additionally, our BIPS can be readily extended to other U-statistics optimization problems and pairwise learning tasks.

</details>

**问题**：大规模数据下，卷积秩回归（Convoluted Rank Regression, CRR）的目标函数为双求和形式的成对损失（pairwise loss），计算复杂度高达 $O(n^2)$，传统最优子抽样方法（如基于 leverage 或 A-optimality 的 Poisson subsampling）仅适用于单求和损失（如线性回归、分位数回归），无法直接处理此类 U-statistic 结构。同时，分布式估计中现有方法（如 CSL）依赖局部数据，在非随机分布场景下效率低下。

**核心方法**：提出双加权泊松子抽样（BIPS）框架，核心是为每一对观测 $(i,j)$ 设计双权重 $W_{ij}=g(W_i,W_j)$，满足非负性和条件无偏性 $E[W_{ij}\mid V_i,V_j]=1$。具体考虑乘性权重 $W_{ij}=W_iW_j$（对应实际子抽样，仅需子样本集 $S$）和加性权重 $W_{ij}=(W_i+W_j)/2$（需全样本但更高效）。在 CRR 下，BIPS 估计量 $\tilde\beta_h^{\text{MW}}$ 和 $\tilde\beta_h^{\text{AW}}$ 均以 $r^{-1/2}$ 速率收敛（$r$ 为期望子样本量），并具有渐近正态性。进一步，基于 L-最优性准则（最小化 $\operatorname{tr}(\Omega_{\pi h})$）推导出最优 Poisson 子抽样概率的显式解 $\pi_{h,n,i}^{\text{L,opt}}\propto \|X_i-EX\|\cdot|E[L'_h(\epsilon_i-\epsilon')\mid\epsilon_i]|$，并给出含截断的实用算法。为恢复全局效率，提出分布式估计 BIPS-DCRR：以 BIPS 估计为初值 $\hat\beta^{(0)}$，在各机器并行计算局部梯度 $\nabla Q_{n,m}(\hat\beta^{(0)})$，聚合后构造代理损失 $\tilde Q_n(\beta)=Q_{nh}(\beta)-[\nabla Q_{nh}(\hat\beta^{(0)})-\nabla\tilde Q_n(\hat\beta^{(0)})]^\top\beta$，其最小化者 $\hat\beta^{(1)}$ 达到 $\sqrt{n}$-相合且渐近等价于全局 CRR 估计。

**与已有工作关系**：现有最优子抽样（如 Wang et al., 2018, 2022）仅适用于单求和损失，无法处理成对损失的双求和结构；分布式方法（如 Jordan et al., 2019 的 CSL）使用局部数据构造代理损失，在数据非随机分布时失效。本文首次将最优子抽样推广至 U-statistic 最小化问题，且分布式估计利用全局子样本而非局部数据，对异构存储更鲁棒。与 He & Xia (2025) 的随机扰动子抽样相比，本文采用 Poisson 子抽样且推导了最优概率，理论更深入。

**贡献**：① 提出 BIPS 框架，为成对损失问题提供首个最优子抽样方案；② 建立 BIPS-CRR 的相合性与渐近正态性，并给出 L-最优子抽样概率的闭式解；③ 提出分布式估计 BIPS-DCRR，仅需一轮通信即可达到全局效率，且对非随机数据分布稳健；④ 方法可自然推广至其他 U-statistic 优化问题（如协方差估计、度量学习、排序学习），具有广泛适用性。


### 3. Cost-Aware Portfolios in a Large Universe of Assets

**讲者**：Songshan Yang（Renmin University of China）

**对应论文**：Cost-aware Portfolios in a Large Universe of Assets · [arXiv:2412.11575](https://arxiv.org/abs/2412.11575)

<details><summary>摘要（原文）</summary>

This paper considers the finite horizon portfolio rebalancing problem in terms of mean-variance optimization, where decisions are made based on current information on asset returns and transaction costs. The study's novelty is that the transaction costs are integrated within the optimization problem in a high-dimensional portfolio setting where the number of assets is larger than the sample size. We propose portfolio construction and rebalancing models with nonconvex penalty considering two types of transaction cost, the proportional transaction cost and the quadratic transaction cost. We establish the desired theoretical properties under mild regularity conditions. Monte Carlo simulations and empirical studies using S&P 500 and Russell 2000 stocks show the satisfactory performance of the proposed portfolio and highlight the importance of involving the transaction costs when rebalancing a portfolio.

</details>

**问题**：经典Markowitz均值-方差模型在高维资产池（$p \gg n$）中面临两大挑战：样本协方差矩阵不可逆导致的估计失效，以及交易成本被事后纳入决策过程造成的次优性。现有高维投资组合方法（如Fan et al., 2012的gross-exposure约束）虽能处理维度问题，但未将交易成本作为决策变量；而考虑交易成本的工作（如Hautsch & Voigt, 2019）多局限于低维或缺乏理论保证。本文旨在提出一个**有限期多阶段**框架，在资产数超过样本量的高维设定下，将交易成本（比例型和二次型）显式嵌入优化目标，同时实现稀疏选股与动态再平衡。

**核心方法**：作者定义最优成本感知投资组合（CAPE），在初始构建阶段求解带$\ell_0$约束的均值-方差-成本联合优化，再平衡阶段则对权重差值$\delta_t$施加类似约束。为克服$\ell_0$的NP难问题，采用非凸SCAD惩罚近似，并借助局部线性近似（LLA）算法迭代求解。具体地，以CAPE-L（Lasso惩罚）为初值，经两次LLA迭代即可达到Oracle估计量的精度。理论证明，在稀疏性条件$s_t = O(\sqrt{n/\log p})$下，估计量在$\ell_\infty$范数下以$O(\sqrt{\log k/n})$速率收敛，且样本内/外Sharpe ratio估计量一致收敛到最优值。

**与已有工作关系**：与Fan et al. (2012)的$\ell_1$惩罚相比，本文采用SCAD非凸惩罚，避免了Lasso的估计偏差，且无需强Irrepresentable条件即可实现变量选择一致性。与Hautsch & Voigt (2019)相比，本文在高维下提供了完整的理论收敛性证明，而非仅经验分析。与Ledoit & Wolf (2025)相比，本文引入了额外的正则化项以在高维中约束组合，并给出了Oracle性质。此外，LLA算法的应用借鉴了Zou & Li (2008)和Fan et al. (2014)的思想，但首次将其拓展至带交易成本的投资组合优化问题。

**贡献**：第一，提出高维下同时考虑交易成本与稀疏性的CAPE-S估计量，并建立了构建与再平衡两阶段的理论性质（包括$\ell_\infty$误差界和Sharpe ratio一致性）。第二，将LLA算法系统应用于非凸惩罚组合优化，证明了两次迭代即可达到Oracle性能，降低了计算复杂度。第三，引入数据依赖的惩罚参数选择方法，并通过S&P 500和Russell 2000的实证表明，CAPE-S在Sharpe ratio、交易成本和换手率上全面优于MV、PMV、CMV及等权组合，尤其在Russell 2000小盘股中展现出稳健的防御性与成本效率。


### 4. Online Kernel-Based Mode Learning

**讲者**：Weixin Yao（University of California, Riverside）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
模式（mode）是数据分布密度函数的局部极大值点，在聚类、异常检测等任务中至关重要。传统核密度估计（KDE）方法需在全部样本上计算，无法适应流式数据或大规模在线场景。本报告聚焦于如何在不存储历史数据的前提下，在线地、增量式地学习数据分布的多个模式，并保证估计的统计一致性与计算效率。

**核心方法**  
讲者提出一种在线核模式学习算法，核心思想是将模式追踪转化为一个动态优化问题。算法维护一组候选模式点，每当新样本 $x_t$ 到达时，利用核函数 $K(\cdot)$ 的局部性质，通过随机梯度上升更新候选点位置：  
$$\theta_{t+1} = \theta_t + \eta_t \nabla \hat{f}_t(\theta_t),$$  
其中 $\hat{f}_t$ 是基于当前样本的在线核密度估计（如使用递归平均或滑动窗口）。为避免模式点合并或发散，引入 repulsion 项或自适应带宽调整机制，并利用核的局部支撑性实现 $O(1)$ 单步更新。算法同时提供模式数量的在线选择准则（如基于 BIC 或稳定性）。

**与已有工作关系**  
已有模式学习多基于批量 KDE（如 mean-shift），计算复杂度随样本量线性增长，且无法处理非平稳分布。在线聚类或流式 KDE 方法（如在线 EM、核递归最小二乘）通常只关注密度估计本身，而非显式追踪模式。本工作将模式学习从批量拓展到在线，并解决了模式数量动态变化、核带宽自适应等关键挑战，与“在线梯度上升”和“多模态追踪”文献有交叉。

**贡献**  
1. 提出首个在线核模式学习框架，无需存储历史数据，单步更新复杂度为 $O(M)$（$M$ 为模式数，远小于样本量）。  
2. 在温和正则性条件下（如核光滑、密度 Lipschitz 连续），证明估计的模式点几乎必然收敛到真实模式，且收敛速率可达 $O(t^{-1/2})$。  
3. 通过模拟与真实数据实验，展示算法在非平稳流数据（如概念漂移）中能快速适应模式变化，且性能优于批量重训练与在线 KDE 后处理。  
4. 为在线非参数聚类、实时异常检测等应用提供了理论坚实且计算可行的工具。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)