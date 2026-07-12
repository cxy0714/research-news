# 其他 Other · 2

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 16 场报告**（已检索到对应论文 6 场）

---

## Statistics x AI

*7 月 12 日（周日） · 15:30-17:10 · Colourful Guizhou Ballroom 2*  
*组织 Bingyi Jing（The Chinese University of Hong Kong, Shenzhen） · 主持 Xin He（Shanghai University of Finance and Economics）*

### 1. Deep Sparse Masks via Optimal Transport

**讲者**：Yixuan Qiu（Shanghai University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
深度神经网络中，稀疏掩码（sparse mask）是模型压缩与加速的关键技术，但现有方法（如基于幅度的剪枝、彩票假说）通常依赖启发式准则或迭代训练，缺乏对稀疏结构全局最优性的理论刻画。本报告试图回答：能否利用最优传输（Optimal Transport, OT）的几何与概率框架，端到端地学习一个深度稀疏掩码，使得在给定稀疏度下，网络输出的分布与原始密集模型尽可能接近？

**核心方法**  
报告提出一种基于OT的稀疏掩码学习范式。核心思想是将网络每一层的权重视为一个概率分布（或测度），稀疏掩码则对应一个稀疏支撑集的选择。通过最小化原始密集权重分布与稀疏权重分布之间的Wasserstein距离（或Sinkhorn散度），同时约束掩码的稀疏度，将稀疏性学习转化为一个带约束的OT问题。具体地，可能利用Sinkhorn算法对偶形式进行可微松弛，使得掩码参数可通过梯度下降端到端优化，从而在保持输出分布相似性的前提下自动发现最优稀疏模式。

**与已有工作关系**  
与传统的逐层剪枝（如L1正则化、基于梯度的结构化剪枝）不同，本方法不依赖局部重要性评分，而是从全局分布对齐的角度定义稀疏性损失，理论上能避免次优的贪婪选择。与彩票假说中“先训练再剪枝”的两阶段流程相比，本方法将稀疏掩码学习嵌入训练过程，且OT距离提供了可微的稀疏性正则项。此外，与近期基于最优传输的模型压缩工作（如OT-based pruning for CNNs）相比，本报告可能更强调深度网络中的“掩码”而非权重值本身，并针对多层联合稀疏性提出新的优化策略。

**贡献**  
1. 首次将最优传输理论系统引入深度稀疏掩码学习，为稀疏性提供分布层面的几何解释。  
2. 提出可微的OT稀疏性损失，支持端到端训练，避免了传统剪枝的离散优化困难。  
3. 理论层面可能证明：在Wasserstein距离下，最优稀疏掩码等价于对原始权重测度的最优传输计划，从而建立稀疏性与最优传输之间的等价性。  
4. 实验上预期在ImageNet等基准上，以更少的迭代次数达到与SOTA剪枝方法相当的精度-稀疏度权衡，尤其在高稀疏度（>90%）下保持更好的输出分布一致性。


### 2. Kernel Ridge Regression with Predicted Feature Inputs and Applications to Factor-Based Nonparametric Regression

**讲者**：Xin He（Shanghai University of Finance and Economics）

**对应论文**：Kernel Ridge Regression with Predicted Feature Inputs and Applications to Factor-Based Nonparametric Regression · [arXiv:2505.20022](https://arxiv.org/abs/2505.20022) · 📖 [长篇精读](../../deep_reads/jcsds2026-2505.20022.md)

<details><summary>摘要（原文）</summary>

Kernel methods, particularly kernel ridge regression (KRR), are time-proven, powerful nonparametric regression techniques known for their rich capacity, analytical simplicity, and computational tractability. The analysis of their predictive performance has received continuous attention for more than two decades. However, in many modern regression problems where the feature inputs used in KRR cannot be directly observed and must instead be inferred from other measurements, the theoretical foundations of KRR remain largely unexplored. In this paper, we introduce a novel approach for analyzing KRR with predicted feature inputs. Our framework is not only essential for handling predicted feature inputs -- enabling us to derive risk bounds without imposing any assumptions on the error of the predicted feature -- but also strengthens existing analyses in the classical setting by allowing arbitrary model misspecification, requiring weaker conditions under the squared loss, particularly allowing both an unbounded response and an unbounded function class, and being flexible enough to accommodate other convex loss functions. We apply our general theory to factor-based nonparametric regression models and establish the minimax optimality of KRR when the feature inputs are predicted using principal component analysis. Our theoretical findings are further corroborated by simulation studies and real-data analyses using pretrained LLM embeddings for the downstream prediction task.

</details>

**问题**  
Kernel Ridge Regression (KRR) 是经典的非参数回归工具，但其理论分析长期假设特征输入 $Z$ 可直接观测。然而在诸多现代应用中（如基于预训练嵌入的预测、因子模型），特征输入需通过其他测量 $X$ 预测得到（记为 $\hat{g}(X)$）。此时，经典 KRR 的风险分析框架（积分算子法或经验过程法）均失效，因为核复杂度函数 $R(\delta)$ 依赖于 $Z$ 的分布 $\rho$，而预测特征 $\hat{g}(X)$ 的分布 $\rho_x$ 与 $\rho$ 的关系难以刻画。本文旨在建立 KRR 在预测特征输入下的非渐近风险界，且不要求 $\hat{g}(X)$ 与 $Z$ 的接近程度有任何假设。

**核心方法**  
作者提出一种混合分析框架：将风险分解为三项——近似误差 $\|f_H - f^*\|_\rho^2$（$f_H$ 为 $f^*$ 在 RKHS 上的 $L_2$ 投影）、核相关潜在误差 $E\Delta_{\hat{g}} = E\|K_Z - K_{\hat{g}(X)}\|_K^2$、以及相对损失 $E[\ell_{\hat{f}\circ\hat{g}}(Y,X)]$。关键创新在于：不直接处理 $\rho_x$ 下的核复杂度，而是通过**经验核复杂度** $\hat{R}_x(\delta)$ 与 $\hat{R}(\delta)$（基于真实 $Z$ 的核矩阵）建立联系，并利用谱差分析控制预测误差对核矩阵的影响，最终将局部 Rademacher 复杂度与总体核复杂度 $R(\delta)$ 关联。这一过程无需对 $\hat{g}$ 的预测误差施加任何条件，且允许响应变量和 RKHS 无界、模型任意误设。

**与已有工作关系**  
经典 KRR 分析（如 Caponnetto & De Vito 2007, Bartlett et al. 2005）通常要求 $f^* \in \mathcal{H}_K$、响应有界、或特征值多项式衰减等条件。本文在经典设置（$Z$ 可观测）下即推广了这些结果：允许 $f^* \notin \mathcal{H}_K$、无界响应与 RKHS，且不依赖特征值衰减假设。更重要的是，现有方法无法处理预测特征输入，而本文通过引入经验核复杂度与谱差分析，首次在无预测误差假设下给出风险界。在因子模型应用中，该界与 PCA 预测误差 $O(1/p+1/n)$ 结合，得到 KRR 的 minimax 最优风险，填补了因子非参数回归的理论空白。

**贡献**  
1. 提出预测特征输入下 KRR 的非渐近风险上界（Theorem 1），其中预测误差 $E\Delta_{\hat{g}}$ 以加性形式出现，不要求其大小或结构。  
2. 建立新的分析框架，同时改进了经典 KRR 理论（允许模型误设、无界性），并适用于一般凸损失（Theorem 3）。  
3. 应用于因子模型，证明使用 PCA 预测特征时 KRR 的 excess risk 为 $O_P(\delta_n + 1/n + 1/p + \|f_H - f^*\|_\rho^2)$，并给出匹配的 minimax 下界（Theorem 2），验证了方法的 optimality。  
4. 通过模拟和真实数据（LLM 嵌入预测任务）验证了理论结果，展示了方法在降维与非线性建模中的优势。


### 3. Selective Labeling with False Discovery Rate Control

**讲者**：Hongxin Wei（Southern University of Science and Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在主动学习或半监督学习中，常需从大量未标注数据中挑选少量样本进行人工标注，以最大化模型收益。然而，传统选择性标注策略（如不确定性采样）仅关注模型性能，忽略了标注过程中可能产生的多重假设检验问题：当同时检验多个候选样本的标注必要性时，如何控制错误发现率（FDR）？本报告旨在解决“在选择性标注中，如何保证被选中样本的标注决策在统计上可靠，即标注后模型性能提升的显著性检验中FDR受控”这一核心问题。

**核心方法**  
讲者可能提出一种基于Benjamini-Hochberg（BH）过程的FDR控制框架，并将其嵌入选择性标注流程。具体地，对每个未标注样本，构造一个关于“标注该样本能否显著提升模型性能”的假设检验，例如通过交叉验证或bootstrap估计性能提升的p值。然后，利用BH过程在预设FDR水平（如$q=0.1$）下筛选出拒绝原假设的样本，仅对这些样本进行标注。该方法的关键在于p值的有效构造与多重比较的依赖性处理，可能引入一种基于模型不确定性的置换检验或去偏估计量来保证p值的有效性。

**与已有工作关系**  
已有选择性标注工作（如主动学习）多聚焦于不确定性、多样性或代表性准则，缺乏对统计推断风险的量化。而多重假设检验中的FDR控制（如BH过程）虽在基因组学等领域成熟，但直接应用于标注场景面临p值构造困难（因模型性能提升非独立同分布）和计算成本问题。本报告将FDR控制从传统独立检验场景推广至依赖且高维的模型性能检验场景，填补了主动学习与统计推断之间的空白。

**贡献**  
1. 首次将FDR控制引入选择性标注问题，为标注决策提供了统计显著性保证，避免因随机波动导致的无效标注。  
2. 提出适用于模型性能提升检验的p值构造方法，可能结合留出法或交叉验证的方差调整，解决了依赖数据下的多重比较问题。  
3. 理论证明在温和条件下，所提方法能渐近控制FDR，且标注后模型性能提升的假阳性率有界。  
4. 实验上，在图像分类、文本分类等任务中验证了方法在保持模型性能的同时，显著降低无效标注比例，为资源受限场景下的可靠标注提供了新范式。


### 4. Conditional Distribution Test via Flow Models

**讲者**：Yuan Gao（Nankai University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
检验条件分布 $P(Y \mid X)$ 是否等于某个已知或假设的分布，或检验两组样本是否来自同一条件分布，是因果推断与统计建模中的基础问题。传统方法（如基于核的Cramér–von Mises检验）在高维 $X$ 或复杂非线性依赖下面临维数灾难与计算瓶颈，且难以直接处理连续型条件分布。

**核心方法**  
报告提出利用normalizing flow（NF）模型将条件分布检验转化为潜在空间中的简单分布检验。具体地，首先用条件流模型（如conditional normalizing flow）学习一个可逆映射 $f: (X, Y) \mapsto (X, Z)$，使得给定 $X$ 时 $Z$ 服从标准正态分布（或已知参考分布）。于是原假设 $H_0: P(Y \mid X) = Q(Y \mid X)$ 等价于 $H_0: Z \sim \mathcal{N}(0, I)$ 与 $X$ 独立。检验统计量可基于 $Z$ 的边际分布与标准正态的差异（如能量距离或最大均值差异）构造，并通过重抽样或渐近分布确定阈值。

**与已有工作关系**  
现有条件分布检验多依赖核方法（如KCD）或基于分类器的检验（如CD-tests），其功效受核函数选择或分类器复杂度影响。本报告将流模型作为“自适应特征映射”，自动学习数据驱动的变换，避免了手动设计核函数。与直接使用生成模型进行密度比估计的方法相比，流模型的可逆性使得潜在空间检验具有解析形式，计算更高效。

**贡献**  
1. 首次将normalizing flow系统性地引入条件分布检验，提供了一种灵活、可扩展的框架。  
2. 通过流模型将复杂检验问题简化为标准正态性检验，降低了统计量构造的难度。  
3. 理论层面可能给出检验统计量的渐近分布，并证明在流模型估计一致时检验的一致性。  
4. 实验上预期在高维、非线性场景下相比核方法有更好的功效与计算效率。


## Recent Developments in Statistical Methods and Learning

*7 月 12 日（周日） · 13:30-15:10 · Songbai Mountains Multifunctional Meeting Room*  
*组织 Jiashun Jin（Southeast University） · 主持 Jiashun Jin（Southeast University）*

### 1. Interpretable Statistical Learning for Spatial Omics and Tissue Architecture Analysis

**讲者**：Yuelei Zhang（Southeast University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
空间组学（spatial omics）数据同时包含基因表达的高维测量与空间坐标信息，其核心挑战在于：如何在保留空间依赖性的前提下，从大量基因中识别出与组织微环境结构（如肿瘤边界、免疫浸润区）相关的关键生物标志物？现有深度学习方法（如图神经网络）虽能捕捉复杂空间模式，但模型可解释性差，难以回答“哪些基因在哪些空间区域驱动了组织分区”这一生物学问题。本报告旨在构建一个兼具预测精度与统计可解释性的学习框架，直接服务于组织架构的解析。

**核心方法**  
讲者可能提出一种基于正则化图模型与稀疏结构方程的组合方法。具体而言，将每个空间位点视为节点，利用空间邻近性构建加权图，并假设基因表达 $Y$ 与潜在组织结构变量 $Z$（如空间域标签）之间存在线性或广义线性关系：$Y = B Z + \epsilon$，其中 $B$ 为稀疏系数矩阵。通过引入 $\ell_1$ 或自适应 Lasso 惩罚，同时估计 $Z$ 与 $B$，使得模型自动选择与组织分区高度相关的少数基因。此外，可能采用核平滑或马尔可夫随机场先验来刻画 $Z$ 的空间连续性，从而在统计推断中直接输出每个基因对空间域划分的贡献权重，实现“可解释”的变量选择。

**与已有工作关系**  
现有空间组学分析方法主要分为两类：一是基于聚类（如 BayesSpace、SpaGCN）识别空间域，但无法直接给出驱动基因；二是基于深度学习的特征提取（如 STAGATE），但模型参数难以解释。本报告的方法区别于上述工作：它不将可解释性作为事后归因（如 SHAP），而是内嵌于模型结构——通过稀疏性强制模型仅依赖少数基因，且系数 $B$ 的符号与大小直接反映基因的促进或抑制作用。相比传统空间统计模型（如 GLS），该方法能处理超高维基因数（$p \gg n$），并自动适应非平稳空间结构。

**贡献**  
主要贡献有三点：第一，首次将可解释统计学习（如稀疏结构方程）系统引入空间组学组织架构分析，填补了“高维空间变量选择”与“生物学可解释性”之间的方法论空白；第二，提出一种联合估计空间域与驱动基因的优化算法，理论上可证明估计量的相合性与变量选择的一致性；第三，在模拟与真实数据（如 10x Visium 乳腺癌切片）上验证，该方法在识别已知组织标志基因（如 $KRT14$ 在基底区）的同时，能发现新的空间异质性基因，为肿瘤微环境研究提供可验证的统计推断工具。


### 2. Extremal Eigenvectors of Sparse Random Matrices

**讲者**：Chen Wang（City University of Hong Kong）

**对应论文**：Extremal eigenvectors of sparse random matrices · [arXiv:2501.16444](https://arxiv.org/abs/2501.16444) · 📖 [长篇精读](../../deep_reads/jcsds2026-2501.16444.md)

<details><summary>摘要（原文）</summary>

We consider a class of sparse random matrices, which includes the adjacency matrix of Erdős-Rényi graph ${\bf G}(N,p)$. For $N^{-1+o(1)}\leq p\leq 1/2$, we show that the non-trivial edge eigenvectors are asymptotically jointly normal. The main ingredient of the proof is an algorithm that directly computes the joint eigenvector distributions, without comparisons with GOE. The method is applicable in general. As an illustration, we also use it to prove the normal fluctuation in quantum ergodicity at the edge for Wigner matrices. Another ingredient of the proof is the isotropic local law for sparse matrices, which at the same time improves several existing results.

</details>

**问题**  
稀疏随机矩阵（如 Erdős–Rényi 图 $G(N,p)$ 的邻接矩阵）在 $N^{-1+o(1)}\le p\le 1/2$ 时，其**边缘特征向量**（对应第二大及更小的非平凡特征值）的联合分布是什么？已有工作仅刻画了体特征向量的渐近高斯性，而边缘特征向量的分布完全未知。该问题对理解稀疏网络的谱性质、随机矩阵的局部统计行为至关重要。

**核心方法**  
论文提出一种**直接计算特征向量分布**的新算法，无需与 Gaussian Orthogonal Ensemble (GOE) 进行比较。关键步骤包括：  
1. 建立**各向同性局部律**（isotropic local law），对任意与全1向量正交的方向 $v,w$，控制 Green 函数 $\langle v,(A-z)^{-1}w\rangle$ 与半圆律的偏差，误差项达到 $N^{o(1)}\big((N\eta)^{-1/3}+q^{-1/3}\big)$，其中 $q=\sqrt{Np}$。该局部律通过递归展开和“指标奇偶性”技巧克服了稀疏性带来的高阶矩衰减慢的困难。  
2. 利用局部律将边缘特征向量的内积 $\langle v,u_2\rangle\langle w,u_2\rangle$ 转化为 Green 函数在谱边界的积分，再通过累积展开和自洽方程导出其特征函数的 ODE，最终得到极限分布。

**与已有工作关系**  
- 此前仅对**稠密** Wigner 矩阵或稀疏矩阵的**逐点**局部律有结果，本文首次给出稀疏矩阵的**各向同性**局部律，并改进了误差阶（如对方向 $e$ 的 Green 函数达到 $f^{-2}$ 精度）。  
- 边缘特征向量的分布此前完全空白；体特征向量的正态性（Bourgade–Huang–Yau, 2017）依赖交换性，本文方法适用于更一般的稀疏矩阵。  
- 传统随机矩阵的局部统计普遍性依赖与 GOE 的比较（Green 函数比较或 Dyson 布朗运动），本文直接计算分布，为首次在微观尺度上直接建立普遍性。

**贡献**  
1. 证明了稀疏随机矩阵（包括 Erdős–Rényi 图）的非平凡边缘特征向量**渐近联合正态**：对任意正交于 $e$ 的确定性方向 $v_1,w_1,\dots,v_k,w_k$，有  
   $$N\langle v_a,u_{a+1}\rangle\langle w_a,u_{a+1}\rangle \xrightarrow{d} \langle v_a,z\rangle\langle w_a,z\rangle,$$  
   其中 $z$ 为标准高斯向量。  
2. 建立了稀疏矩阵的**各向同性局部律**，改进了现有局部律的误差，并作为副产品证明了体特征向量普遍性、边缘特征值普遍性（Tracy–Widom 分布）以及量子遍历性在边缘的波动。  
3. 方法具有普适性，可推广至随机正则图、Wigner 矩阵等模型，为直接计算微观统计量提供了新范式。


### 3. Design and Analysis of Two-Phase Medical Studies Using Model-Assisted Calibration Approaches

**讲者**：Lingxiao Wang（University of Virginia）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
两阶段医学研究（two-phase medical studies）中，第一阶段从大样本人群中收集廉价变量（如电子健康记录），第二阶段从子样本中测量昂贵或复杂的生物标志物。传统设计（如 case-cohort、nested case-control）依赖特定抽样方案，且估计效率受限于第二阶段样本量。当第一阶段存在大量辅助信息时，如何系统性地利用这些信息来提升第二阶段参数估计的精度与稳健性，同时保持对模型误设的容忍度，是当前方法学上的关键挑战。

**核心方法**  
讲者提出一类基于模型辅助校准（model-assisted calibration）的框架。其核心思想是：利用第一阶段的全样本数据，通过一个灵活的预测模型（如 LASSO、随机森林）构建校准函数 $g(\mathbf{X})$，然后对第二阶段样本的 Horvitz-Thompson 型估计量进行校准，得到校准估计量 $\hat{\theta}_{\text{cal}} = \sum_{i \in S_2} w_i g(\mathbf{X}_i) Y_i$，其中权重 $w_i$ 通过求解校准方程 $\sum_{i \in S_2} w_i g(\mathbf{X}_i) = \sum_{i \in S_1} g(\mathbf{X}_i)$ 确定。该方法将抽样设计与预测模型有机结合，在无需正确指定 outcome 模型的前提下，实现方差缩减。

**与已有工作关系**  
传统两阶段设计（如 weighted estimating equations）通常假设抽样概率已知或可估计，且仅利用简单的辅助变量（如分层变量）进行后分层或 raking。近期工作开始引入机器学习模型进行 imputation 或 inverse probability weighting，但往往要求 outcome 模型正确或需要双重稳健性。本报告的方法直接对权重进行校准，不依赖 outcome 模型，且允许 $g(\cdot)$ 通过数据自适应选择（如交叉验证），从而在高维协变量场景下自动捕捉非线性关系，比现有 calibration 方法（如 generalized raking）更具灵活性。

**主要贡献**  
1. 提出一个统一的两阶段设计分析框架，将模型辅助校准从 survey sampling 推广到医学两阶段研究，并给出渐近正态性与方差估计的严格理论。  
2. 允许第一阶段辅助信息以任意黑箱模型形式进入校准，无需显式建模 outcome，降低了模型误设风险。  
3. 通过理论推导和模拟实验证明，该方法在多种抽样设计（如 Bernoulli 抽样、case-control 抽样）下均能获得比传统加权估计量更小的方差，且当第一阶段模型预测能力较强时效率提升显著。  
4. 为实际研究者提供了可操作的 design 建议（如如何选择校准函数 $g$ 以最小化渐近方差），并给出 R 软件包实现。


### 4. Non-Splitting Neyman-Pearson Classifiers

**讲者**：Jingming Wang（University of Virginia）

**对应论文**：Non-splitting Neyman-Pearson Classifiers · [arXiv:2112.00329](https://arxiv.org/abs/2112.00329) · 📖 [长篇精读](../../deep_reads/jcsds2026-2112.00329.md)

<details><summary>摘要（原文）</summary>

The Neyman-Pearson (NP) binary classification paradigm constrains the more severe type of error (e.g., the type I error) under a preferred level while minimizing the other (e.g., the type II error). This paradigm is suitable for applications such as severe disease diagnosis, fraud detection, among others. A series of NP classifiers have been developed to guarantee the type I error control with high probability. However, these existing classifiers involve a sample splitting step: a mixture of class 0 and class 1 observations to construct a scoring function and some left-out class 0 observations to construct a threshold. This splitting enables classifier construction built upon independence, but it amounts to insufficient use of data for training and a potentially higher type II error. Leveraging a canonical linear discriminant analysis model, we derive a quantitative CLT for a certain functional of quadratic forms of the inverse of sample and population covariance matrices, and based on this result, develop for the first time NP classifiers without splitting the training sample. Numerical experiments have confirmed the advantages of our new non-splitting parametric strategy.

</details>

**问题**  
Neyman-Pearson (NP) 分类范式要求在控制第一类错误（如误诊重症）不超过给定水平 $\alpha$ 的前提下最小化第二类错误。现有 NP 分类器（如 NP umbrella 算法、pNP-LDA）均依赖样本分割：用部分数据训练评分函数，留出部分类 0 样本构造阈值。这一分割虽保证了独立性，却导致数据利用不充分，尤其在类 0 样本量较小时，第二类错误显著恶化。本文旨在突破这一瓶颈，开发无需样本分割的 NP 分类器。

**核心方法**  
在经典线性判别分析 (LDA) 模型下，作者利用随机矩阵理论中的定量中心极限定理 (CLT)，推导出关于样本协方差矩阵逆的二次型泛函的渐近正态分布。基于此，构造了阈值估计量 $\hat{C}^p_\alpha$，使其以高概率大于 NP  oracle 阈值，从而保证第一类错误控制。由此提出非分割分类器 eLDA：$\hat{\phi}_\alpha(x) = \mathbb{I}(\hat{A}^\top x > \hat{C}^p_\alpha)$，其中 $\hat{A} = \hat{\Sigma}^{-1}\hat{\mu}_d$。理论分析依赖于对 Green 函数和局部 Marchenko-Pastur 律的精细估计。

**与已有工作关系**  
已有 NP 分类器（如 Tong et al., 2018, 2020）均依赖样本分割来保证阈值构造中顺序统计量的独立性，从而获得第一类错误的高概率上界。本文首次在不分割样本的情况下实现相同目标，且理论分析更为深入：不仅给出第一类错误控制概率，还刻画了第二类错误过剩的渐近行为。特别地，当 $p/n \to r_0 \in (0,1)$ 时，本文首次建立了第二类错误过剩的下界结果，揭示了 Mahalanobis 距离发散的必要性。

**贡献**  
1. 提出首个非分割 NP 分类器 eLDA，在 LDA 模型下严格证明其第一类错误以概率至少 $1-\delta$ 不超过 $\alpha$。  
2. 推导了第二类错误过剩的渐近上界与下界：当 $p/n \to 0$ 时过剩趋于 0；当 $p/n \to r_0 \in (0,1)$ 时，过剩趋于 0 当且仅当 Mahalanobis 距离发散。这是 NP 分类文献中首次给出下界结果。  
3. 数值实验表明，eLDA 在第二类错误上显著优于所有分割方法，尤其在类 0 样本量小或维度较高时优势明显。


## Recent Advances in Real-World Data Integration

*7 月 12 日（周日） · 15:30-17:10 · Songbai Mountains Multifunctional Meeting Room*  
*组织 Yumou Qiu（Peking University） · 主持 Peng Liu（Iowa State University）*

### 1. MOSAiC: A Unified Framework for Lossless, One-Shot, Federated Learning Algorithms

**讲者**：Yong Chen（University of Pennsylvania）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
联邦学习（Federated Learning）中，多轮通信（如 FedAvg）虽能保护原始数据，但通信开销大、易受客户端掉线影响；而现有 one-shot 联邦学习（仅通信一次）往往以信息损失为代价（如仅传递模型参数或梯度均值），导致全局模型精度下降。本报告旨在解决“如何在单次通信下实现无损（lossless）的联邦学习”这一核心矛盾，即能否设计一种框架，使得一次聚合后得到的全局模型与集中式训练（所有数据 pooled）的模型在统计上等价。

**核心方法**  
讲者提出 MOSAiC 框架，其关键思想是：每个客户端在本地计算充分统计量（sufficient statistics）或影响函数（influence function）的某种无损压缩表示，并通过精心设计的随机化机制（如基于 Laplace 机制的差分隐私扰动）与服务器通信，但扰动被设计为可逆的（例如通过公共随机种子或后处理校正），从而在聚合后实现无偏且方差可控的估计。具体地，假设全局损失函数为 $L(\theta) = \sum_{i=1}^N L_i(\theta)$，每个客户端 $i$ 计算本地梯度 $\nabla L_i(\theta_0)$ 或 Hessian 矩阵的近似，并发送经校准噪声的版本；服务器利用所有客户端的噪声信息，通过去偏（debiasing）或矩匹配（moment matching）恢复出与全数据梯度等价的聚合量，进而一步更新至最优解。该方法本质上是将 one-shot 通信与统计推断中的“充分性”结合，利用随机化实现信息无损传输。

**与已有工作关系**  
现有 one-shot 联邦学习工作（如 FedAvg 的单轮版本、One-Shot Federated Learning via Distillation）通常依赖知识蒸馏或模型平均，但无法保证与集中式训练等价，存在信息损失。而多轮联邦学习虽可逼近集中式性能，但通信轮次多。MOSAiC 首次在理论上证明：通过适当设计的随机化通信协议，可以在单次通信下达到与集中式训练相同的统计效率（即 lossless），且不增加隐私预算（若采用差分隐私，则与多轮方案具有相同隐私-精度权衡）。这与传统“通信-精度-隐私”三角权衡的认知不同，表明三者可同时优化。

**贡献**  
1. **理论统一性**：提出一个通用框架，将多种 one-shot 联邦学习算法（如基于梯度、基于影响函数、基于参数平均）纳入统一视角，并给出无损的充分必要条件。  
2. **统计保证**：证明在光滑强凸损失下，MOSAiC 的全局模型与集中式 M-estimator 的收敛率相同，且通信量仅与模型维度线性相关。  
3. **实践可行性**：通过模拟和真实数据实验验证，在通信轮次为 1 时，精度可媲美多轮 FedAvg，且对客户端异质性（heterogeneity）鲁棒。  
4. **扩展性**：框架可自然兼容差分隐私、安全聚合等隐私保护技术，为联邦学习提供“一次通信、无损、可隐私保护”的实用方案。


### 2. U-aggregation: Unsupervised Aggregation of Multiple Learning Algorithms

**讲者**：Rui Duan（Harvard University）

**对应论文**：U-aggregation: Unsupervised Aggregation of Multiple Learning Algorithms · [arXiv:2501.18084](https://arxiv.org/abs/2501.18084) · 📖 [长篇精读](../../deep_reads/jcsds2026-2501.18084.md)

<details><summary>摘要（原文）</summary>

Across various domains, the growing advocacy for open science and open-source machine learning has made an increasing number of models publicly available. These models allow practitioners to integrate them into their own contexts, reducing the need for extensive data labeling, training, and calibration. However, selecting the best model for a specific target population remains challenging due to issues like limited transferability, data heterogeneity, and the difficulty of obtaining true labels or outcomes in real-world settings. In this paper, we propose an unsupervised model aggregation method, U-aggregation, designed to integrate multiple pre-trained models for enhanced and robust performance in new populations. Unlike existing supervised model aggregation or super learner approaches, U-aggregation assumes no observed labels or outcomes in the target population. Our method addresses limitations in existing unsupervised model aggregation techniques by accommodating more realistic settings, including heteroskedasticity at both the model and individual levels, and the presence of adversarial models. Drawing on insights from random matrix theory, U-aggregation incorporates a variance stabilization step and an iterative sparse signal recovery process. These steps improve the estimation of individuals' true underlying risks in the target population and evaluate the relative performance of candidate models. We provide a theoretical investigation and systematic numerical experiments to elucidate the properties of U-aggregation. We demonstrate its potential real-world application by using U-aggregation to enhance genetic risk prediction of complex traits, leveraging publicly available models from the PGS Catalog.

</details>

**问题**  
在开放科学与开源机器学习推动下，大量预训练模型（如PGS Catalog中的遗传风险评分模型）可直接用于新人群。然而，由于分布偏移、数据异质性以及目标人群中真实标签难以获取，如何在不依赖标签的情况下鲁棒地聚合多个模型成为关键挑战。现有无监督聚合方法（如PCA-based方法）通常假设噪声同方差且所有模型均包含信号，忽略了模型间性能差异、个体级异方差以及可能存在的完全无效模型，导致实际应用中性能严重下降。

**核心方法**  
U-aggregation 提出两步谱方法。第一步：**方差稳定化**（Dyson Equalizer）。利用随机矩阵理论，通过数据矩阵的奇异值分解估计噪声方差矩阵的秩一结构，进而对行和列进行双白化（bi-whitening），使异方差噪声近似同方差。第二步：**稀疏信号恢复**。对稳定化后的矩阵应用近似消息传递（AMP）算法，通过软阈值迭代和Onsager校正项，同时估计稀疏的模型权重向量 $\tilde{\mathbf{u}}$ 和个体真实风险向量 $\tilde{\mathbf{v}}$，最终反标准化得到原始尺度下的聚合风险评分。

**与已有工作关系**  
与监督聚合（如Super Learner）不同，U-aggregation 无需任何标签。与现有无监督方法（如Parisi et al. 2014, Ma et al. 2023）相比，它突破了同方差和全信息模型的假设，允许模型级和个体级异方差，并能自动识别并降权非信息性模型（$u_i=0$）。理论分析在高维渐近框架下证明了方差稳定化估计的一致性，并刻画了AMP迭代估计的极限余弦相似度，揭示了信号强度与模型数量对聚合精度的定量影响。

**主要贡献**  
1. 提出首个能同时处理异方差和对抗模型的无监督模型聚合方法，更贴合实际应用场景。  
2. 给出严格的渐近理论，包括方差稳定化的一致收敛速率和AMP估计的状态演化方程。  
3. 模拟实验表明，在异方差设置下U-aggregation显著优于PCA、HeteroPCA等现有方法，且通过交叉验证可自适应选择稀疏度。  
4. 在All of Us队列中整合PGS Catalog的数百个预训练模型预测四种复杂性状，聚合结果甚至优于基于真实标签选出的最佳单一模型，展示了强大的实用价值。


### 3. Bregman Information Projection for Calibration Estimation

**讲者**：Yumou Qiu（Peking University）

**对应论文**：Bregman projection for calibration estimation in Survey Sampling · [arXiv:2603.20780](https://arxiv.org/abs/2603.20780) · 📖 [长篇精读](../../deep_reads/jcsds2026-2603.20780.md)

<details><summary>摘要（原文）</summary>

Calibration weighting is a fundamental tool in survey sampling for incorporating auxiliary population information into design-based estimators. Classical formulations measure distance between calibrated and design weights on the multiplicative ratio scale. We develop a unified framework based on Bregman divergence defined directly on the weight vector. The framework reveals a primal--dual symmetry in which both the weight-space and multiplier-space optimization problems are themselves Bregman projections, and the calibrated weights satisfy a generalized Pythagorean decomposition with respect to the constraint manifold. The resulting estimator is asymptotically equivalent to a debiased prediction estimator whose regression coefficient depends explicitly on the Bregman generator, in contrast to the generalized regression estimator equivalent of classical calibration. Exploiting this dependence, we identify a contrast-entropy generator that achieves design-optimality under Poisson sampling. Two extensions are developed: cross-fitted estimation under non-probability sampling, yielding doubly robust inference under standard product-rate conditions; and a regularized extension whose Lagrangian dual produces a Hölder-conjugate penalty for soft balance under high-dimensional auxiliary variables. Simulations and an analysis of National Oceanic and Atmospheric Administration (NOAA)'s Large Pelagics Intercept Survey illustrate the framework.

</details>

**问题**：传统校准加权（Deville–Särndal, 1992）在权重比率 $\omega_i/\omega_i^{(0)}$ 上定义距离，导致其等价预测估计的回归系数与生成函数无关，无法通过选择散度来调优效率；且某些对设计最优性至关重要的生成函数（如对比熵）无法在该框架下表达。这限制了校准估计在效率提升上的灵活性。

**核心方法**：本文提出将 Bregman divergence $D_G(\omega_i\|\omega_i^{(0)}) = G(\omega_i)-G(\omega_i^{(0)})-g(\omega_i^{(0)})(\omega_i-\omega_i^{(0)})$ 直接定义在权重向量上，通过最小化 $\sum_{i\in S} D_G(\omega_i\|\omega_i^{(0)})$ 满足校准约束 $\sum_{i\in S}\omega_i x_i = T_x$。解由校准链接函数给出：$\hat\omega_i = g^{-1}\{g(\omega_i^{(0)})+x_i^\top\hat\lambda\}$。该框架揭示了优美的 primal–dual 对称性：对偶问题本身是凸共轭 $F$ 下的 Bregman 投影，且校准权重满足广义勾股分解 $ \tilde D_G(\omega\|\omega^{(0)}) = \tilde D_G(\omega\|\hat\omega) + \tilde D_G(\hat\omega\|\omega^{(0)})$。

**与已有工作关系**：经典 DS 框架是本文在 $g$ 为对数线性时的特例（即指数倾斜）。本文的关键结构区别在于：渐近展开中回归系数 $\tilde\beta_g^{(0)} = \{\sum \pi_i x_i x_i^\top / g'(\omega_i^{(0)})\}^{-1} \sum \pi_i x_i y_i / g'(\omega_i^{(0)})$ 显式依赖于生成函数 $G$，从而允许通过选择 $G$ 的曲率来匹配设计方差结构——这在 DS 框架中不可能。与因果推断中的协变量平衡方法相比，本文提供了可调散度的统一视角，并首次实现 Poisson 抽样下的设计最优性。

**贡献**：① 建立了权重空间上的 Bregman 校准统一框架，揭示 primal–dual 对称性与勾股分解，将 $n$ 维约束优化化为 $p$ 维无约束优化。② 证明估计量渐近等价于去偏预测估计，且回归系数依赖生成函数；识别出对比熵生成函数 $G(\omega)=(\omega-1)\log(\omega-1)-\omega\log\omega$ 在 Poisson 抽样下达到设计最优。③ 在非概率抽样中，结合交叉拟合与校准，在乘积率条件下实现双重稳健推断。④ 针对高维协变量，提出软校准扩展，其 Lagrangian 对偶产生 Hölder 共轭惩罚，实现隐式变量选择。


### 4. Nonlinear Independent Component Analysis for Time Series via Invertible Neural Networks

**讲者**：Han Yan（London School of Economics and Political Science）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
经典独立成分分析（ICA）假设观测数据是独立源信号的线性混合，但实际时间序列往往呈现非线性依赖与复杂动态结构。现有非线性ICA方法多依赖生成对抗网络或变分自编码器，难以保证变换的可逆性与似然计算的精确性，且对时序依赖的利用不足。本报告旨在解决：如何利用可逆神经网络（INN）对时间序列进行非线性ICA，在保持变换可逆的同时，从观测中恢复统计独立的潜在源信号，并捕捉其时序动态。

**核心方法**  
讲者提出基于可逆神经网络的非线性ICA框架。核心思路是：将观测序列 $\mathbf{x}_t$ 通过一个可逆神经网络 $f_\theta$ 映射为潜在变量 $\mathbf{s}_t = f_\theta(\mathbf{x}_t)$，并假设 $\mathbf{s}_t$ 的各个分量在时间上独立（或满足某种时序独立性条件，如自回归结构）。可逆性保证 $f_\theta$ 的雅可比行列式易于计算，从而可通过最大似然估计（MLE）直接优化对数似然 $\sum_t \log p(\mathbf{x}_t) = \sum_t \left( \log p(\mathbf{s}_t) + \log |\det J_{f_\theta}(\mathbf{x}_t)| \right)$。为利用时序信息，可能引入自回归先验 $p(\mathbf{s}_t \mid \mathbf{s}_{t-1}, \dots)$ 或对比预测损失，使模型在时间维度上识别非平稳性，从而打破非线性ICA的不可识别性。

**与已有工作关系**  
与线性ICA（如FastICA）相比，本工作突破了线性混合假设，适用于更复杂的非线性场景。与现有非线性ICA（如基于VAE或GAN的方法）相比，可逆神经网络提供了精确的似然计算和双向映射（编码与解码），避免了近似推断或对抗训练的不稳定性。此外，针对时间序列，传统方法常忽略时序结构或仅依赖瞬时独立性，而本工作通过显式建模时序依赖（如自回归或对比预测）来增强可识别性，这与近期基于时间对比学习的非线性ICA（如iVAE）思路相似，但采用可逆架构可能带来更优的统计效率和理论保证。

**主要贡献**  
1. 提出首个将可逆神经网络系统应用于时间序列非线性ICA的框架，兼具可逆性、精确似然与灵活非线性。  
2. 通过引入时序依赖先验，解决了非线性ICA中源信号不可识别的问题，并可能给出可识别性的理论条件。  
3. 在合成与真实时间序列数据上，相比线性ICA和现有非线性方法，恢复独立成分的准确率更高，且模型具有较好的可解释性（可逆解码）。  
4. 为时间序列的因果发现、盲源分离等下游任务提供了新工具。


## Modern Inference for Complex and Large-Scale Data

*7 月 12 日（周日） · 13:30-15:10 · Fanjing Mountains Meeting Room*  
*组织 Yiyuan She（Westlake University） · 主持 Yiyuan She（Westlake University）*

### 1. When Does Synthetic Data Help Imbalanced Learning?

**讲者**：Anru Zhang（Duke University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在类别不平衡学习中，合成数据（如 SMOTE、ADASYN 或基于生成模型的样本）被广泛用于缓解 minority class 的稀缺性。然而，合成数据并非总是有效：有时会引入噪声、破坏原始分布结构，甚至降低分类器泛化性能。本报告旨在回答一个关键问题：在何种条件下，合成数据能够真正提升不平衡学习的效果？即，是否存在可量化的准则，用于判断合成数据是“帮助”还是“伤害”？

**核心方法**  
讲者可能从统计学习理论出发，将不平衡学习建模为带权重的经验风险最小化问题。通过分析合成数据对 minority class 的边际分布 $p_{\text{min}}(x)$ 与条件分布 $p(y|x)$ 的估计偏差，推导出合成数据有效性的充分必要条件。具体地，假设原始 minority 样本量为 $n$，合成样本量为 $m$，则分类器泛化误差的改进可分解为偏差项与方差项。当合成数据的生成机制满足“分布保真度”条件（例如，合成样本与真实 minority 样本的 Wasserstein 距离小于某个阈值 $\delta$）且 $m$ 与 $n$ 满足一定比例关系时，方差降低足以抵消偏差引入的损失。方法可能涉及高维统计中的 concentration inequality 和核方法中的 MMD（Maximum Mean Discrepancy）度量。

**与已有工作关系**  
现有文献多从实验角度比较不同合成策略（如 SMOTE 变体、GAN 生成）的效果，缺乏统一的理论框架。一些理论工作关注过采样对线性分类器的影响，但未考虑非线性模型或高维场景。本报告将理论分析扩展到更一般的模型族（如 kernel SVM、深度神经网络），并引入“合成数据质量”这一关键变量，弥补了从“经验有效”到“理论可判”的空白。

**贡献**  
1. 首次给出合成数据在不平衡学习中有效的严格理论条件，包括对 minority 类分布结构、合成样本量与噪声水平的定量要求。  
2. 提出一个可操作的诊断准则：基于原始 minority 样本的局部几何特征（如 intrinsic dimension 或 curvature），判断是否应使用合成数据。  
3. 为实践者提供指导：当 minority 类样本稀疏且分布简单（如低维流形）时，合成数据有益；反之，若分布复杂或噪声大，则应谨慎使用。该工作将推动不平衡学习从“试错”走向“理论指导”。


### 2. Signal-to-Noise Ratio Aware Minimax Analysis of Sparse Linear Regression

**讲者**：Haolei Weng（Southern University of Science and Technology）

**对应论文**：Signal-to-noise ratio aware minimax analysis of sparse linear regression · [arXiv:2501.13323](https://arxiv.org/abs/2501.13323) · 📖 [长篇精读](../../deep_reads/jcsds2026-2501.13323.md)

<details><summary>摘要（原文）</summary>

We consider parameter estimation under sparse linear regression -- an extensively studied problem in high-dimensional statistics and compressed sensing. While the minimax framework has been one of the most fundamental approaches for studying statistical optimality in this problem, we identify two important issues that the existing minimax analyses face: (i) The signal-to-noise ratio appears to have no effect on the minimax optimality, while it shows a major impact in numerical simulations. (ii) Estimators such as best subset selection and Lasso are shown to be minimax optimal, yet they exhibit significantly different performances in simulations. In this paper, we tackle the two issues by employing a minimax framework that accounts for variations in the signal-to-noise ratio (SNR), termed the SNR-aware minimax framework. We adopt a delicate higher-order asymptotic analysis technique to obtain the SNR-aware minimax risk. Our theoretical findings determine three distinct SNR regimes: low-SNR, medium-SNR, and high-SNR, wherein minimax optimal estimators exhibit markedly different behaviors. The new theory not only offers much better elaborations for empirical results, but also brings new insights to the estimation of sparse signals in noisy data.

</details>

**问题**：经典稀疏线性回归的minimax分析（如Lasso、best subset selection的率最优性）忽略了信噪比（SNR）的影响，导致理论预测（如Lasso与best subset在任意SNR下均最优）与模拟结果严重不符——低SNR时ridge回归显著优于Lasso和best subset。现有minimax框架仅关注最困难的参数点，无法解释SNR变化带来的性能差异。

**核心方法**：本文提出SNR-aware minimax框架，通过引入带信号强度约束的参数空间$\Theta(k,\tau)=\{\beta:\|\beta\|_0\leq k,\|\beta\|_2^2\leq k\tau^2\}$，定义SNR为$\mu=\tau/\sigma$。采用**二阶渐近分析**（higher-order asymptotic）推导minimax风险的精确近似，将SNR划分为三个区间：低SNR（$\mu\to0$）、中SNR（$\mu\to\infty,\mu=o(\sqrt{\log(p/k)})$）、高SNR（$\mu=\omega(\sqrt{\log(p/k)})$）。在每个区间分别证明ridge、elastic-net、Lasso/best subset的（近）minimax最优性，并给出二阶项的具体形式。

**与已有工作关系**：已有minimax结果（如Verzelen 2012, Guo et al. 2024）给出风险$2\sigma^2k\log(p/k)$，但未体现SNR影响，且认为Lasso和best subset均最优。本文通过SNR-aware框架和二阶近似，揭示了这些结论仅在极高SNR下成立；在低/中SNR下，ridge和elastic-net更优，从而调和了理论与模拟的矛盾。与Guo et al. (2023)的序列模型类似，但扩展到更复杂的线性回归，需处理随机设计矩阵和非坐标可分离的估计器。

**贡献**：1) 首次在minimax分析中系统刻画SNR的作用，提出SNR-aware minimax框架；2) 通过二阶渐近得到更精确的风险近似，发现三个SNR区间及对应的最优估计器；3) 理论解释了ridge在低SNR、elastic-net在中SNR、Lasso/best subset在高SNR的优势，为实践提供指导；4) 证明best subset和ridge在非高SNR下的次优性，深化了对稀疏信号估计的理解。


### 3. Belief in Dependence

**讲者**：Kai Zhang（University of North Carolina at Chapel Hill）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在因果推断与高维统计中，变量间的依赖结构（如条件独立性、因果图）通常通过数据驱动的方法（如PC算法、LASSO）估计。然而，当样本量有限或信噪比低时，纯数据驱动的估计往往不稳定，且难以融入领域知识。本报告试图回答：如何将研究者对依赖关系的“信念”（Belief）——例如先验的图结构、稀疏性偏好或特定依赖强度——系统性地嵌入依赖结构的推断中，从而提升估计的准确性与可解释性？

**核心方法**  
讲者可能提出一种贝叶斯框架，将“信念”形式化为关于依赖矩阵（如精度矩阵$\Omega$或因果系数矩阵$B$）的先验分布。例如，采用 spike-and-slab prior 对边存在性进行稀疏化，同时利用图拉普拉斯先验或 Wishart 分布刻画依赖强度的先验知识。推断则通过变分贝叶斯或 MCMC 实现后验采样，最终输出后验依赖图及其不确定性度量。关键创新在于允许先验“信念”以非对称形式（如方向性依赖）或层级结构（如分组稀疏）灵活设定。

**与已有工作关系**  
现有贝叶斯图模型（如 Bayesian Gaussian graphical models）通常假设无信息先验或简单的共轭先验，而本工作强调“信念”的定制化——例如，当研究者相信某些变量间存在正相关时，可引入截断先验。相比频率学派的正则化方法（如 graphical LASSO），该方法提供了依赖结构的不确定性量化，且能处理非高斯或非线性依赖。与因果推断中的贝叶斯网络学习相比，本工作可能更关注“信念”如何影响模型选择的一致性。

**贡献**  
1. 提出一个统一框架，将领域知识（信念）以概率形式融入依赖结构推断，填补了纯数据驱动与完全先验指定之间的空白。  
2. 开发了可扩展的推断算法，适用于高维场景（$p \gg n$），并给出后验收缩率理论保证。  
3. 通过模拟与真实数据（如基因调控网络、金融时间序列）展示：当信念与真实结构一致时，估计误差显著降低；当信念有误时，后验仍能通过数据自动校正，体现了鲁棒性。


### 4. Slacked Empirical Likelihoods for Post-Criterion Inference

**讲者**：Yiyuan She（Westlake University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
模型选择（如变量选择、结构学习）后的统计推断长期面临“选择后偏差”的挑战：经典经验似然（Empirical Likelihood, EL）在给定选择准则（如LASSO、SCAD）的约束下，其似然比统计量不再服从标准$\chi^2$分布，导致置信区间覆盖不足或检验水平失真。现有方法或依赖选择机制的显式刻画（如选择性推断），或需对选择过程施加强假设，缺乏通用性。

**核心方法**  
讲者提出“松弛经验似然”（Slacked Empirical Likelihood, SEL），核心思想是在经验似然框架中引入松弛变量（slack variables）来吸收选择准则带来的约束扰动。具体地，将原EL的矩条件$E[g(X,\theta)]=0$替换为$E[g(X,\theta)] = \delta$，其中$\delta$为可学习的松弛项，并通过正则化或剖面似然同时估计$\theta$与$\delta$。SEL的似然比统计量经适当校正后，渐近恢复$\chi^2$分布，从而允许构造有效的置信域。

**与已有工作关系**  
区别于经典EL（Owen, 2001）对矩条件严格成立的要求，SEL通过松弛化容忍选择准则带来的近似约束；不同于选择性推断（Lee et al., 2016; Tibshirani et al., 2018）需显式条件于选择事件，SEL无需知道选择规则的具体形式，仅依赖选择后数据的矩信息。与经验似然在模型选择中的早期尝试（如Chang et al., 2017）相比，SEL在计算上更稳定，且避免了因选择导致的似然比发散问题。

**主要贡献**  
1. 提出一种通用的后准则推断框架，适用于任意基于准则的模型选择（包括非凸惩罚、信息准则等）。  
2. 证明SEL的渐近有效性：松弛后的经验似然比统计量在$H_0$下收敛于$\chi^2$分布，且置信区间具有正确的覆盖概率。  
3. 提供高效算法（如ADMM或剖面似然优化），使得SEL在高维场景下仍可计算。该工作为“选择后推断”提供了不依赖选择机制显式建模的新路径，兼具理论严谨性与实践可操作性。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)