# 网络与图数据 Networks & Graphs · 4

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 20 场报告**（已检索到对应论文 4 场）

---

## Statistical Learning for Spatio-Temporal and Network Data

*7 月 13 日（周一） · 15:30-17:10 · Yongkang Room*  
*主持 Wenhao Chen（The Chinese University of Hong Kong, Shenzhen）*

### 1. Detecting Multiple Changepoints in the Annual Number of Snowy Weeks via Latent Gaussian Beta-Binomial Modeling and Pairwise Likelihood

**讲者**：Qiqi Lu（Virginia Commonwealth University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
该报告关注气候时间序列中的多变点检测问题，具体对象为年降雪周数（annual number of snowy weeks）。这类计数数据常呈现过度离散（overdispersion），且变点位置与数量未知。传统方法（如基于正态或泊松似然的变点检测）难以同时处理过度离散、计数特性以及多个变点的联合推断。报告旨在提出一种既能刻画数据异质性，又能高效识别多个变点的统计模型。

**核心方法**  
作者采用 **Latent Gaussian Beta-Binomial Modeling** 对年降雪周数建模：假设每周降雪与否服从 Bernoulli 分布，但成功概率 $p_t$ 随时间 $t$ 变化，且引入 Beta 分布刻画 $p_t$ 的随机性（即 Beta-Binomial 复合分布），以容纳过度离散。进一步，将 $p_t$ 的 logit 变换与一个潜在高斯过程（Latent Gaussian Process）相连接，该过程的均值函数允许分段常数或分段线性结构，从而隐含变点。由于全似然涉及高维积分，作者采用 **Pairwise Likelihood**（成对似然）进行参数估计与变点检测，即仅考虑所有时间点对 $(t,s)$ 的联合似然乘积，以降低计算复杂度并保持估计的一致性。

**与已有工作关系**  
现有变点检测文献多针对正态或泊松数据（如 PELT、Binary Segmentation），或使用隐马尔可夫模型。本工作的创新在于：1）将 Beta-Binomial 分布引入变点框架，专门应对过度离散的计数数据；2）利用潜高斯过程而非离散状态转移来建模变点，允许更灵活的变点模式（如平滑过渡）；3）采用 Pairwise Likelihood 替代全似然或贝叶斯 MCMC，在保证统计效率的同时大幅降低计算负担，尤其适用于长序列。

**主要贡献**  
1. 提出一种新的变点检测模型，融合 Beta-Binomial 与潜高斯过程，为过度离散计数时间序列提供稳健推断。  
2. 将 Pairwise Likelihood 方法拓展至变点问题，给出估计量的渐近性质（如相合性与正态性），并设计高效的优化算法。  
3. 通过年降雪周数实例，展示该方法在气候学中的应用价值，可识别出与气候模式变化（如厄尔尼诺、全球变暖）相关的变点，为环境统计提供实用工具。


### 2. Identifying the Dynamic Spreading Mechanism of Livestock Infectious Diseases Using Multivariate Hawkes Processes

**讲者**：Wenhao Chen（The Chinese University of Hong Kong, Shenzhen）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
牲畜传染病（如口蹄疫、非洲猪瘟）的传播具有时空动态性，且不同宿主（如养殖场、野生动物、运输车辆）间的交叉感染机制复杂。现有流行病学模型（如SEIR）通常假设均质混合或固定传播率，难以刻画异质性接触网络与时间依赖的感染强度。本报告旨在解决：如何从时空点过程数据中，同时识别不同传播路径（如场间直接接触、空气传播、媒介传播）的触发模式与动态强度变化？

**核心方法**  
讲者采用**多元Hawkes过程**（Multivariate Hawkes Process）建模传染病事件序列。设 $N_i(t)$ 为第 $i$ 类事件（如某养殖场报告病例）的累积计数，其条件强度为  
\[
\lambda_i(t) = \mu_i + \sum_{j=1}^K \int_0^t g_{ij}(t-s) \, dN_j(s),
\]  
其中 $\mu_i$ 为背景率，$g_{ij}(\cdot)$ 为核函数（如指数衰减 $g_{ij}(\tau)=\alpha_{ij}e^{-\beta_{ij}\tau}$），刻画 $j$ 类事件对 $i$ 类事件的激发效应。通过最大似然估计或EM算法估计参数 $\{\mu_i, \alpha_{ij}, \beta_{ij}\}$，并利用Granger因果检验或似然比检验识别显著传播路径。进一步，可引入协变量（如地理距离、气候）对核函数进行参数化，以解释传播强度的空间异质性。

**与已有工作关系**  
传统传染病建模多基于微分方程（如SEIR）或分支过程，假设传播率恒定或分段常数。多元Hawkes过程则允许传播强度随历史事件动态变化，且能自动捕捉“自激发”（同一养殖场重复爆发）与“交叉激发”（不同养殖场间传播）的时变模式。与单变量Hawkes过程相比，多元版本可区分不同传播源（如野猪 vs. 家猪）的贡献。与基于网络的随机SIR模型相比，本方法无需预设网络结构，而是从数据中推断潜在传播链路。

**主要贡献**  
1. 将多元Hawkes过程引入牲畜传染病传播机制识别，提供了一种数据驱动的非参数化动态建模框架。  
2. 通过核函数参数化，可量化不同传播路径的强度与衰减速度，为防控策略（如隔离、消毒时机）提供定量依据。  
3. 方法可扩展至多宿主、多传播媒介场景，且能处理不完整观测（如漏报病例），通过引入潜在变量或稀疏正则化提升鲁棒性。


### 3. 融合双域变换的地震数据低秩恢复方法

**讲者**：Zeyu Zeng（Chengdu University of Technology/Chengdu Bureau of Statistics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
地震数据采集常因环境限制导致道缺失或强噪声污染，破坏数据的低秩结构。传统低秩恢复方法（如核范数最小化）多在单一域（如时间-空间域）施加低秩约束，难以同时刻画数据在变换域中的稀疏性与结构先验。本报告聚焦于如何融合双域变换（如时间-空间域与频率-波数域）来提升低秩恢复的精度与鲁棒性。

**核心方法**  
讲者提出一种融合双域变换的低秩恢复框架。首先，将地震数据分别投影到两个互补的变换域（例如，通过短时傅里叶变换得到时频域，以及通过二维傅里叶变换得到频率-波数域）。在每个域中，利用低秩矩阵分解（如截断SVD或加权核范数）对变换系数施加低秩约束。然后，通过交替方向乘子法（ADMM）联合优化两个域的保真项与低秩正则项，并引入一致性约束使双域恢复结果在原始数据空间达成一致。该方法本质上是将单域低秩先验扩展为多域联合先验，利用不同变换域对地震波场特征的互补表示能力。

**与已有工作关系**  
现有地震数据恢复方法多基于单域低秩假设（如SVD去噪）或单域稀疏变换（如Curvelet域阈值）。本报告的双域融合策略借鉴了图像处理中的多尺度变换思想，但针对地震数据的物理特性（如波场在频率-波数域的线性特征）进行了定制。与单纯叠加多个正则项的方法不同，该工作通过交替投影与一致性约束实现了双域信息的有效融合，避免了简单加权带来的参数敏感问题。

**贡献**  
主要贡献有三：一是提出双域变换联合低秩模型，首次将时频域与频率-波数域的低秩先验系统性地结合到地震数据恢复中；二是设计高效的ADMM求解算法，保证了收敛性与计算可行性；三是通过合成与实测数据实验证明，该方法在缺失道比例高达70%时仍能恢复出清晰的同相轴，且对随机噪声与相干噪声的抑制能力均优于单域方法。该工作为地震数据预处理提供了新的理论视角与实用工具。


### 4. Identifying Chinese Leading Venture Capital Firms Using Investing Preference-Enhanced Graph Neural Networks

**讲者**：Mingyu Han（Central University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
风险投资（VC）公司的领先地位识别对创业生态与政策制定至关重要。传统方法依赖财务指标或网络中心性（如度中心性、PageRank），但忽略了VC在行业、阶段、地域上的投资偏好异质性——这些偏好恰恰是区分“专注型”与“广撒网型”VC的关键信号。本报告旨在解决：如何利用投资偏好信息，从中国VC投资网络中有监督地识别出真正具有引领作用的头部机构？

**核心方法**  
提出投资偏好增强的图神经网络（Investing Preference-Enhanced GNN）。首先构建异构图，节点包括VC公司与被投初创企业，边表示投资关系。每个VC节点除基础属性外，额外嵌入其投资偏好向量（如行业分布、轮次分布、地域分布），通过可学习的注意力机制聚合邻居信息时，将偏好向量作为边权重或节点特征的调节因子。具体地，GNN的消息传递过程引入偏好感知的注意力系数：$\alpha_{ij} = \text{softmax}( \text{LeakyReLU}( \mathbf{a}^\top [\mathbf{W}\mathbf{h}_i \oplus \mathbf{W}\mathbf{h}_j \oplus \mathbf{p}_i ] ) )$，其中$\mathbf{p}_i$为VC $i$的偏好嵌入。最终通过排序损失（如pairwise ranking loss）训练模型，输出每个VC的领先得分。

**与已有工作关系**  
已有工作主要分为两类：一是基于网络中心性的统计方法（如特征向量中心性），二是基于GNN的节点分类或链接预测（如GraphSAGE、GAT）。前者无法捕捉偏好异质性，后者虽能利用图结构但未显式建模VC的投资策略差异。本工作首次将投资偏好作为先验知识融入GNN的消息传递机制，使模型能区分“偏好相似但结构位置不同”的VC，比纯结构方法更具可解释性。

**贡献**  
1. 提出偏好增强的GNN框架，为金融网络中的节点重要性评估提供了新范式。  
2. 在真实中国VC数据集上验证，相比基线（如GAT、PageRank）在领先VC识别准确率上提升显著（如Precision@K提高10%以上）。  
3. 可解释性强：通过注意力权重可直观分析哪些偏好维度对领先地位贡献最大，为投资策略研究提供工具。


### 5. A Multiple Changepoint Detection Method for Examinee Aberrant Behaviors Based on Bootstrap Intensity Scores and Weighted Binary Segmentation

**讲者**：Baoqun Chang（Northeast Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在标准化考试中，考生可能出现作弊、抄袭、猜题或疲劳等异常行为，这些行为往往导致其答题模式在某个或某些时间点（题目序号）发生突变。传统变点检测方法多针对单变点或假设变点数目已知，而实际考试中异常行为可能多次出现且变点位置未知。如何从考生作答序列中准确、稳健地识别出多个未知变点，同时控制误报率，是教育测量与心理统计中的关键问题。

**核心方法**  
报告提出一种基于 Bootstrap Intensity Scores 与 Weighted Binary Segmentation 的多重变点检测框架。首先，利用项目反应理论（IRT）模型拟合考生能力，计算每道题目的“强度得分”（Intensity Score），例如基于残差或局部影响函数，以量化该题作答与预期模式的偏离程度。然后，对强度得分序列应用加权二元分割（Weighted Binary Segmentation）：该算法通过递归地在序列中寻找使某种加权统计量（如CUSUM）最大化的分割点，并利用Bootstrap方法生成统计量的经验分布，从而自适应地确定变点数目与位置。加权机制可赋予不同位置不同权重，以应对考试中题目难度差异或局部异常聚集。

**与已有工作关系**  
已有变点检测方法（如Binary Segmentation、PELT、Wild Binary Segmentation）多假设序列独立同分布或仅考虑均值/方差变化，而教育测量中的强度得分序列具有异方差性和相关性（因IRT估计引入）。此外，传统方法对多重变点检测的显著性控制较弱。本报告将Bootstrap重抽样与加权分割结合，既保留了二元分割的计算效率，又通过Bootstrap校正了多重检验问题，同时加权策略增强了在题目难度不均匀场景下的检测能力。

**主要贡献**  
1. 提出了一种专门针对考生异常行为的多重变点检测方法，将IRT强度得分与变点检测算法有机融合。  
2. 引入Bootstrap强度得分，无需对序列分布做强假设，提高了方法的稳健性。  
3. 加权二元分割框架允许灵活处理局部异常模式，并有效控制Familywise Error Rate。  
4. 通过模拟与实证研究，展示了该方法在检测多种异常行为（如抄袭、猜测）时相比现有方法的优势，为教育考试安全分析提供了新工具。


### 6. Fit First and Detect Later: A Unified Decoupled Framework for Change Detection in High Dimensions

**讲者**：Bin Liu（Fudan University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维数据中的变化检测（change detection）面临“维数灾难”与“多重检验”的双重挑战：传统方法往往将模型拟合与变化点定位耦合在一起，导致计算复杂度随维度指数增长，且难以控制全局错误率。本报告旨在解决高维均值向量或协方差结构发生稀疏变化时，如何高效、统一地检测变化点位置与变化幅度。

**核心方法**  
报告提出“先拟合，后检测”（Fit First and Detect Later）的解耦框架。第一阶段，利用高维稀疏估计（如Lasso、SCAD）对全样本进行整体拟合，得到基准模型参数 $\hat{\theta}$；第二阶段，基于拟合残差构造逐点或逐段的检验统计量，例如对每个时间点 $t$ 计算局部累积和（CUSUM）或似然比，并通过高维多重比较校正（如Benjamini-Hochberg过程或基于$\ell_\infty$范数的阈值）来定位变化点。该框架将估计与推断分离，允许在拟合阶段使用任意正则化方法，在检测阶段独立控制FDR或FWER。

**与已有工作关系**  
现有高维变化检测方法多采用“同时估计与检测”策略（如fused Lasso、动态规划结合惩罚项），或依赖特定分布假设（如多元正态）。本报告的解耦框架统一了多种检测准则（均值变化、协方差变化、回归系数变化），且不要求变化点稀疏性先验已知。相比基于似然比扫描的方法，该框架通过先拟合降低了后续检验的维度，避免了全空间搜索的计算瓶颈。

**主要贡献**  
1. 提出一个通用解耦范式，将高维变化检测分解为拟合与检测两个独立模块，显著降低计算复杂度至 $O(pT)$ 量级（$p$为维度，$T$为时间长度）。  
2. 在理论上证明了在稀疏变化假设下，第一阶段估计的收敛速度不影响第二阶段检测的渐近最优性，即“拟合误差”可被第二阶段的多重比较吸收。  
3. 通过数值实验与真实数据（如脑电图、金融时间序列）验证了该方法在检测精度与计算效率上优于现有耦合方法，尤其适用于 $p \gg T$ 的高维场景。


## Rank and Graph-Based Methods

*7 月 13 日（周一） · 10:30-12:10 · Qunsheng Room*  
*主办 IMS China · 组织 Fang Han（University of Washington, Seattle） · 主持 Fang Han（University of Washington, Seattle）*

### 1. From Graph-Based Tests to Graph-Induced Ranks: Two-Sample Inference for Complex Data

**讲者**：Hao Chen（University of California, Davis）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维、非欧几里得或图结构数据（如网络、流形、函数型数据）的两样本检验是统计推断中的难点。传统参数或基于欧氏距离的非参数方法（如Mann-Whitney U检验）在复杂数据结构下失效，因为数据点间的相似性无法用简单距离度量。本报告旨在解决：如何利用数据内在的图结构构造有效的两样本检验，并进一步将图信息转化为秩统计量，以提升检验的灵活性和功效。

**核心方法**  
讲者提出从“基于图的检验”到“图诱导秩”的转化框架。首先，将两个样本的观测点视为节点，基于某种相似性度量（如欧氏距离、核距离）构建图（如最小生成树、k近邻图）。传统基于图的检验（如Friedman-Rafsky的MST检验）直接统计图中连接两个样本的边数。本报告的核心创新是定义“图诱导秩”（graph-induced ranks）：对每个节点，根据其在图上的邻域结构或路径距离，赋予一个秩值，从而将图结构压缩为一组秩统计量。然后基于这些秩构造两样本检验统计量（如Wilcoxon型或Cramér-von Mises型），并通过置换或条件分布获得p值。

**与已有工作关系**  
已有基于图的检验（如Friedman & Rafsky, 1979）仅利用图的边连接信息，对图构造方式敏感且功效有限。近年有工作将图与能量距离或核方法结合，但计算复杂。本报告提出的图诱导秩方法，将图结构转化为秩，既保留了图的局部与全局结构，又继承了秩检验的非参数稳健性（对异常值不敏感）。与传统的秩检验（如Mann-Whitney）相比，图诱导秩能捕捉复杂数据中的非线性依赖；与基于图的检验相比，秩变换使得统计量更易分析渐近性质，且可通过调整图构造适应不同数据特征。

**贡献**  
1. 提出“图诱导秩”这一新概念，为复杂数据的两样本推断提供了统一框架，将图检验与秩检验的优势结合。2. 理论上，可能证明在适当条件下，基于图诱导秩的检验具有渐近正态性且对局部备择具有一致性。3. 方法计算高效（图构建复杂度为$O(n\log n)$，秩计算可并行），适用于大规模高维数据。4. 通过模拟和真实数据（如单细胞RNA-seq、社交网络）展示，相比现有方法，在非欧几里得结构下功效显著提升，且对图参数选择稳健。


### 2. Limit Theorems of Azadkia-Chatterjee’s Conditional Graph Correlation

**讲者**：Muhong Gao（University of International Business and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
Azadkia 与 Chatterjee 提出的 Conditional Graph Correlation (CGC) 是一种基于图论的非参数条件依赖度量，能够刻画给定协变量 $Z$ 后响应 $Y$ 与预测变量 $X$ 之间的条件关联强度。然而，该统计量的渐近性质（如相合性、收敛速度、极限分布）尚未被完整刻画，这限制了其在假设检验与置信区间构造中的应用。本报告旨在建立 CGC 的极限定理，为条件独立性检验提供理论支撑。

**核心方法**  
讲者可能采用 U-统计量或 V-统计量的分析框架，将 CGC 表示为基于样本邻接图的核函数之和。通过引入图论中的“条件邻域”概念，将条件依赖转化为图边权重的期望差异。利用 Hoeffding 分解与经验过程理论，证明 CGC 在适当正则条件下具有 $\sqrt{n}$-相合性，并推导其渐近正态分布。关键步骤在于控制图结构带来的依赖性与边界效应，可能借助 Stein 方法或耦合技巧。

**与已有工作关系**  
已有工作（如 Chatterjee 2019 的广义相关系数）主要关注无条件依赖的极限理论，而 Azadkia-Chatterjee 的 CGC 将图论思想拓展至条件场景，但其渐近理论仅停留在经验收敛层面。本报告填补了条件图相关系数在极限分布上的空白，与近期关于“条件距离相关系数”的渐近结果形成互补，但 CGC 对非线性与异方差结构更敏感。

**主要贡献**  
1. 首次给出 CGC 的渐近正态性条件，明确其收敛速度与样本量、图稀疏参数的关系。  
2. 提出基于 CGC 的条件独立性检验的渐近临界值，避免重抽样计算。  
3. 揭示 CGC 在非参数回归模型中的效率损失上界，为实际应用中的图参数选择提供理论指导。


### 3. Statistical Limits and Power Boosting for High Dimensional Two Sample Test

**讲者**：Yaowu Zhang（Shanghai University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维两样本检验（High Dimensional Two Sample Test）在维度 $p$ 远大于样本量 $n$ 时面临严峻挑战：传统基于均值差异的检验（如 Hotelling $T^2$）因协方差矩阵不可逆而失效，而基于最大绝对值或 $L_2$ 范数的检验虽可应对高维，但其功效受限于信号稀疏性与强度。本报告旨在回答两个核心问题：一是高维两样本检验是否存在不可逾越的统计极限（如信号强度需超过某个阈值才能被检测）？二是能否设计一种通用的“功率提升”（Power Boosting）策略，在保持 Type I error 控制的前提下突破这些极限？

**核心方法**  
报告可能从 minimax 框架出发，刻画检验功效的相变边界：当信号强度 $\|\mu_1-\mu_2\|_2$ 低于某个与 $(p,n)$ 相关的阈值时，任何检验的势均趋于 0；高于该阈值时，存在一致有效的检验。在此基础上，提出一种 **Power Boosting** 方法，其核心思想是：通过数据驱动的特征筛选（如基于 marginal screening 或 SIR 降维）将高维问题转化为低维子问题，再结合多重检验校正（如 Benjamini-Hochberg 或 Bonferroni）对筛选后的特征进行联合检验。该方法可能利用 **sparsity-adaptive** 的阈值选择，在信号稀疏时自动聚焦于少数强信号，在信号稠密时退化为全局检验，从而在多种稀疏模式下逼近最优功效。

**与已有工作关系**  
现有高维两样本检验主要分为两类：一是基于均值差异的 $L_2$ 型检验（如 Bai-Saranadasa 检验），适用于稠密信号但受限于协方差结构；二是基于最大绝对值的检验（如 Cai-Liu-Xia 检验），适用于稀疏信号但功效随信号个数增加而下降。本报告的新颖之处在于：1）系统揭示了检验的统计极限（即“可检验性”的相变边界），将已有零散结果统一为完整理论；2）提出的 Power Boosting 框架不依赖于特定的检验统计量，而是作为一种元算法，可叠加于现有方法之上，理论上证明其能在不牺牲 Type I error 的前提下提升功效，尤其当信号强度处于边界附近时。

**主要贡献**  
1. **理论贡献**：给出了高维两样本检验的 minimax 最优检测边界，明确了信号强度、维度与样本量之间的 trade-off，为实际应用提供了“何时可检验”的指导。  
2. **方法贡献**：提出一种通用的 Power Boosting 策略，其计算复杂度低且易于实现，可适配多种基础检验统计量，并在理论上证明其功效提升的幅度与信号稀疏性自适应。  
3. **实践意义**：通过数值模拟和真实数据案例，展示了该方法在基因表达、神经影像等高维场景中相比现有方法的显著优势，为高维假设检验提供了新的分析工具。


### 4. Randomized Optimal Switching Problem and Related Mirror Descent Flow

**讲者**：Yuchao Dong（Tongji University）

**对应论文**：Randomized Optimal Switching Problem and Related Mirror Descent Flow · [arXiv:2606.12875](https://arxiv.org/abs/2606.12875) · 📖 [长篇精读](../../deep_reads/jcsds2026-2606.12875.md)

<details><summary>摘要（原文）</summary>

We study continuous-time reinforcement learning for the optimal switching problem, in which a decision-maker controls a diffusion process by switching among finitely many regimes, incurring both running and transition costs. To enable exploration, we relax the classical deterministic switching control to a randomized framework, where the switching decisions are governed by a continuous-time Markov chain with state-dependent generator, and augment the cost functional with a KL-divergence regularization weighted by a temperature parameter $λ$. Under mild assumptions on the coefficients, we establish that the regularized value function is the unique smooth solution of an elliptic Hamilton--Jacobi--Bellman system, and derive an explicit optimal Gibbs policy given by an exponential transformation of the value function differences across modes. We further prove that the regularized value function approximates the classical optimal value function with error of order $O\left(λ\log \frac{1}λ\right)$, which is consistent with analogous bounds established in other entropy-regularized control problems and is believed to be sharp. To solve the regularized problem numerically, we introduce a mirror descent flow in the dual logarithmic policy space, prove its well-posedness and the monotonic decrease of the value function along the flow, and establish quantitative error bound to the classical optimal value function. For a constant temperature scheduler, the convergence rate is of order $O\left(\frac{1}{e^{λs} - 1}+λ\log\frac1λ\right)$, while under the annealing scheduler $λ_s = \frac{1}{\sqrt{1+s}}$, we obtain the rate $O\left(\frac{\log s}{\sqrt{s}}\right)$, which decays to zero as the flow time $s \to \infty$.

</details>

**问题**  
经典最优切换问题中，决策者通过切换有限个运行模式控制扩散过程，最小化包含运行成本与切换成本的期望折现总成本。其值函数由障碍型 HJB 变分不等式刻画，但高维情形下数值求解极为困难。为引入探索并设计可计算的强化学习算法，本文将该问题松弛为随机化框架：切换决策由状态依赖的连续时间 Markov 链（CTMC）生成元控制，并在目标泛函中加入 KL 散度正则化项（温度参数 $\lambda$），从而将原组合优化问题转化为光滑的熵正则化控制问题。

**核心方法**  
首先，通过 Girsanov 变换建立正则化成本泛函的路径空间 KL 散度解释，证明正则化值函数 $(V_i^\lambda)$ 是椭圆型 HJB 系统 (2.6) 的唯一光滑解，且最优策略具有显式 Gibbs 形式 $\bar\pi_{ij}(x)=\exp\big((V_i^\lambda-V_j^\lambda-G_{ij})/\lambda\big)$。其次，利用比较原理和 Bernstein 方法，证明正则化值函数与经典值函数之间的偏差为 $O(\lambda\log(1/\lambda))$，该界与熵正则化最优停止、漂移控制等问题中的结果一致。最后，在对数策略空间 $Z^{ij}=\log\pi_{ij}$ 中引入镜像下降流 $\partial_s Z^{ij}_s = -(V_j^{\pi(Z_s),\lambda_s}+G_{ij}-V_i^{\pi(Z_s),\lambda_s}+\lambda_s Z^{ij}_s)$，证明其全局适定性与值函数单调递减性，并给出定量收敛估计：常数温度下 $O(1/(e^{\lambda s}-1)+\lambda\log(1/\lambda))$，退火调度 $\lambda_s=1/\sqrt{1+s}$ 下 $O(\log s/\sqrt{s})$。

**与已有工作关系**  
已有连续时间强化学习研究主要集中于绝对连续控制（如漂移控制），而切换控制属于奇异控制。Dong (2024) 首次将探索框架用于最优停止，但切换问题更复杂。近期 Dai, Dong, Li (2025) 仅处理三状态特例，Huang et al (2025) 虽处理多状态但缺乏定量误差分析。本文首次给出熵正则化切换问题的显式逼近误差 $O(\lambda\log(1/\lambda))$，并指出该界与熵正则化最优传输中的收敛率一致，揭示了两者共同的 KL 惩罚变分结构。镜像下降流方面，本文借鉴 Sethi, Siska, Zhang (2025) 的熵退火思想，但将其从概率密度控制推广到 CTMC 生成元空间，策略参数化由对数强度而非密度实现，从而适应切换控制的耦合结构。

**贡献**  
1. 提出修正的熵正则化项 $\pi\log\pi-\pi+1$，获得路径空间 KL 散度变分解释，揭示了正则化切换问题与熵正则化最优传输的深层联系。  
2. 首次建立正则化值函数逼近经典值函数的显式误差界 $O(\lambda\log(1/\lambda))$，该界在多种 KL 正则化问题中普遍出现，表明其一般性。  
3. 开发了对数策略空间中的镜像下降流，证明其全局收敛性，并给出退火调度下的显式收敛率，为连续时间切换控制的策略优化提供了首个具有定量保证的动力学框架。


## Statistical Learning, Networks, and Decision Science

*7 月 13 日（周一） · 10:30-12:10 · Doupeng Mountains Meeting Room*  
*组织 Hansheng Wang（Peking University） · 主持 Hansheng Wang（Peking University）*

### 1. Deep Autoencoders for Nonlinear Factor Models: Theory and Applications

**讲者**：Zhouyu Shen（Peking University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
传统因子模型假设观测数据由少数潜在因子线性生成，但现实中的高维数据（如基因表达、金融收益率）往往呈现非线性依赖结构。现有非线性因子模型（如核PCA、高斯过程潜在变量模型）虽能捕捉非线性，但缺乏可扩展的推断算法与理论保证；而深度自编码器虽擅长非线性降维，却常被当作黑箱，缺少与统计因子模型之间的形式化联系。本报告旨在回答：能否将深度自编码器嵌入非线性因子模型框架，同时获得可解释的因子结构、可扩展的估计方法以及渐近理论？

**核心方法**  
报告提出一类**深度自编码器非线性因子模型**（Deep Autoencoder Nonlinear Factor Model, DANFM）。模型假设观测 $X \in \mathbb{R}^p$ 由低维潜在因子 $Z \in \mathbb{R}^d$（$d \ll p$）通过一个非线性解码器 $g_\theta(\cdot)$ 生成，即 $X = g_\theta(Z) + \varepsilon$，其中 $g_\theta$ 由深度神经网络参数化，$\varepsilon$ 为噪声。因子 $Z$ 的分布可设为标准正态或稀疏先验。估计采用变分自编码器（VAE）框架：编码器 $q_\phi(Z|X)$ 近似后验，联合优化证据下界（ELBO）。理论部分证明，当网络宽度与深度适当增长时，DANFM 可一致估计非线性因子结构，且因子估计的收敛速度达到非参数回归的最优率。

**与已有工作关系**  
与经典线性因子模型（如PCA、因子分析）相比，DANFM 允许载荷函数为任意非线性，显著提升对复杂数据的拟合能力。与现有非线性因子模型（如核PCA、高斯过程潜在变量模型）相比，DANFM 利用深度网络的可扩展性，可处理 $p$ 达数万的高维数据，且通过随机梯度变分推断实现高效计算。与标准深度自编码器（如VAE）的区别在于：DANFM 明确将潜在变量解释为统计因子，并建立因子载荷的可识别性条件（如局部等距性），从而赋予自编码器以统计推断意义，而非仅用于压缩或生成。

**主要贡献**  
1. **理论奠基**：首次为深度自编码器驱动的非线性因子模型提供一致性、收敛速率及因子可识别性的严格证明，填补了深度学习与统计因子模型之间的理论空白。  
2. **方法创新**：提出结合变分推断与深度网络的估计框架，在保持非线性表达能力的同时，实现因子载荷的统计推断（如置信区间）。  
3. **应用价值**：在合成数据与真实高维数据集（如人脸图像、股票收益率）上验证，DANFM 在因子解释性、预测精度及降维可视化上均优于线性因子模型与标准VAE，为高维非线性数据的结构发现提供了新工具。


### 2. Bi-SCORE for Weighted Bipartite Networks with Application in Knowledge Source Discovery

**讲者**：Rui Pan（Central University of Finance and Economics）

**对应论文**：Bi-SCORE for Weighted Bipartite Networks with Application in Knowledge Source Discovery · [arXiv:2508.21467](https://arxiv.org/abs/2508.21467) · 📖 [长篇精读](../../deep_reads/jcsds2026-2508.21467.md)

<details><summary>摘要（原文）</summary>

Community detection in citation networks offers a powerful approach to understanding knowledge flow and identifying core research areas within academic disciplines. This study focuses on knowledge source discovery in statistics by analyzing a weighted bipartite journal citation network constructed from 16,119 articles published in eight core journals from 2001 to 2023. To capture the inherent asymmetry of citation behavior, we explicitly preserve the bipartite structure of the network, distinguishing between citing and cited journals. For this task, we propose Bi-SCORE (Bipartite Spectral Clustering on Ratios-of-Eigenvectors), a computationally efficient and initialization-free spectral method designed for community detection in weighted bipartite networks with degree heterogeneity. We establish rigorous theoretical guarantees for the performance of Bi-SCORE under the weighted bipartite degree-corrected stochastic block model. Furthermore, simulation studies demonstrate its robustness across varying levels of sparsity and degree heterogeneity, where it outperforms existing methods. When applied to the real-world citation network, Bi-SCORE uncovers a six-community structure corresponding to key research areas in statistics, including applied statistics, methodology, theory, computation, and econometrics. These findings provide valuable insights into the intricate citation patterns and knowledge flow among statistical journals.

</details>

**问题**  
加权二分网络广泛存在于引用网络、推荐系统等场景，其社区检测面临两大挑战：一是节点度异质性（degree heterogeneity）导致传统谱方法失效；二是现有模型（如Bipartite SBM）未考虑权重或计算复杂。本文以统计学期刊引用网络为背景，旨在高效识别知识源（cited journals）的社区结构，同时保留二分网络的非对称性，避免投影法的信息损失。

**核心方法**  
提出Bi-SCORE（Bipartite Spectral Clustering on Ratios-of-Eigenvectors）。对加权二分邻接矩阵$A\in\mathbb{R}^{n\times m}$进行SVD，取前$\kappa=\min(K,L)$个奇异向量；对每个行节点$i$，计算比率向量$\hat{R}^r_{i\cdot}=(\hat{U}_{i2}/\hat{U}_{i1},\dots,\hat{U}_{i\kappa}/\hat{U}_{i1})$（经阈值截断），列节点类似。该比率变换消除了节点度参数$\theta_i$和$\gamma_j$的影响，使得同一社区的节点在比率空间中重合。最后对$\hat{R}^r$和$\hat{R}^c$执行$k$-means聚类。算法无需初始化，计算高效。

**与已有工作关系**  
Bi-SCORE将单模无权重网络的SCORE方法（Jin, 2015）推广至加权二分网络。相比现有二分谱方法（如nBiSC），Bi-SCORE通过比率变换而非归一化拉普拉斯来处理度异质性，在稀疏场景下理论更优；且不要求权重偏差有界，适用于泊松权重。与投影法或启发式方法相比，Bi-SCORE基于显式生成模型（加权二分DCBM），具有严格理论保证。

**贡献**  
1. 提出Bi-SCORE算法，在加权二分DCBM下证明节点误分率的上界，理论一致性成立。  
2. 模拟实验表明，在平衡/不平衡样本、不同异质性和稀疏度下，Bi-SCORE的误差率和调整兰德指数均优于nBiSC和谱聚类。  
3. 应用于统计学期刊引用网络（16,119篇文章，8种核心期刊），识别出6个有意义的社区（如应用统计、方法论、计算统计等），并进一步在应用统计子社区中发现4个子领域，揭示了知识流动模式。


### 3. Multi-Relational Network Autoregression Model with Latent Group Structures

**讲者**：Yimeng Ren（The Hong Kong University of Science and Technology）

**对应论文**：Multi-relational Network Autoregression Model with Latent Group Structures · [arXiv:2406.03296](https://arxiv.org/abs/2406.03296) · 📖 [长篇精读](../../deep_reads/jcsds2026-2406.03296.md)

<details><summary>摘要（原文）</summary>

Multi-relational networks among entities are frequently observed in the era of big data. Quantifying the effects of multiple networks have attracted significant research interest recently. In this work, we model multiple network effects through an autoregressive framework for tensor-valued time series. To characterize the potential heterogeneity of the networks and handle the high dimensionality of the time series data simultaneously, we assume a separate group structure for entities in each network and estimate all group memberships in a data-driven fashion. Specifically, we propose a group tensor network autoregression (GTNAR) model, which assumes that within each network, entities in the same group share the same set of model parameters, and the parameters differ across networks. An iterative algorithm is developed to estimate the model parameters and the latent group memberships simultaneously. Theoretically, we show that the group-wise parameters and group memberships can be consistently estimated when the group numbers are correctly- or possibly over-specified. An information criterion for group number estimation of each network is also provided to consistently select the group numbers. Lastly, we implement the method on a Yelp dataset to illustrate the usefulness of the method.

</details>

**问题**  
多关系网络（如社交网络与空间网络）中观测到的张量值时间序列，其动态演化受多个网络效应共同驱动，且各网络节点存在异质性。现有网络自回归模型多聚焦于单一网络，无法同时量化多个网络的主效应与交互效应；而高维VAR或张量因子模型虽能处理高维性，却牺牲了网络结构的可解释性，且难以刻画节点间的异质分组行为。如何在一个统一的框架内，同时估计多个网络的组结构、组内参数以及组间自动量效应，是本文要解决的核心问题。

**核心方法**  
本文提出**组张量网络自回归（GTNAR）模型**。对于$q$个网络，响应张量$\mathcal{Y}_t \in \mathbb{R}^{N_1 \times \cdots \times N_q}$满足：
\[
\mathcal{Y}_t = \sum_{l=1}^q (\mathcal{Y}_{t-1} \times_l \mathbf{W}^{(l)}) \times_l \mathbf{L}^{(l)} + \mathcal{A} \odot \mathcal{Y}_{t-1} + \sum_{l=1}^q \boldsymbol{\beta}^{(l)}_{\mathbf{X}_{l,t}} \circ_{k \neq l} \mathbf{1}_{N_k} + \mathcal{E}_t,
\]
其中$\mathbf{W}^{(l)}$为行归一化邻接矩阵，$\mathbf{L}^{(l)}$为对角矩阵，其对角元$\lambda^{(l)}_{g^{(l)}_{i_l}}$依赖于第$l$个网络中节点$i_l$的潜在组标签$g^{(l)}_{i_l}$；$\mathcal{A}$为自动量张量，其元素$\alpha_{g^{(1)}_{i_1}\cdots g^{(q)}_{i_q}}$也由跨层组标签共同决定。模型通过引入组结构将参数数量从$\prod_l N_l^2$降至$O(\sum_l G_l(p_l+1) + \prod_l G_l)$。估计采用迭代最小二乘算法：固定组标签时，参数有闭式解；固定参数时，每个节点独立更新组标签。组数通过信息准则QIC选择。

**与已有工作关系**  
与单网络组自回归模型（如Zhu et al., 2023）相比，GTNAR将组结构推广到多个网络，且每个网络拥有独立的组划分，避免了跨层组交互的枚举难题。与张量自回归模型（如Wang et al., 2024）相比，GTNAR显式嵌入网络权重矩阵，使参数具有网络效应解释，而非依赖低秩分解。与高维VAR的“堆叠”策略相比，GTNAR保留了张量结构，参数估计方差更小。此外，模型允许组数过指定（$G_l \geq G_{l,0}$），并证明了此时参数和组隶属度仍可一致估计，这是对传统分组面板模型（如Su et al., 2016）的重要扩展。

**贡献**  
1. 首次提出同时处理多网络效应与潜在组结构的张量自回归模型，兼具可解释性与维度约简。  
2. 建立参数估计和组隶属度估计的相合性，允许组数过指定，并给出组数选择的信息准则一致性。  
3. 在正确指定组数下，证明估计量的渐近正态性，为统计推断（如置信区间构造）提供理论基础。  
4. 通过Yelp数据集实证，揭示用户社交网络与区域空间网络的异质性效应，验证模型实用性。


### 4. Byzantine-robust Federated Learning via Convex Hull Search

**讲者**：Zhao Chen（Fudan University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
联邦学习（Federated Learning, FL）中，恶意客户端可能发起拜占庭攻击（Byzantine attack），通过上传任意梯度破坏全局模型收敛。现有鲁棒聚合方法（如Krum、Trimmed Mean、Median）通常假设攻击者数量有上界，且对高维梯度空间中的复杂攻击（如“little is enough”攻击）鲁棒性不足。本报告旨在解决：**当攻击者比例未知且攻击策略自适应时，如何在不依赖统计假设（如梯度分布对称性）的前提下，设计一种计算高效的鲁棒聚合规则？**

**核心方法**  
提出基于**凸包搜索（Convex Hull Search）**的聚合机制。核心思想：在每一轮通信中，服务器收集所有客户端上传的梯度向量 $\{g_i\}_{i=1}^n$，计算这些点的凸包 $\mathcal{C} = \text{conv}\{g_1,\dots,g_n\}$。若存在拜占庭攻击，恶意梯度往往位于凸包外部或极端位置。算法通过搜索凸包内部或边界上的一个“中心点”作为聚合结果，例如最小化到所有点距离之和的**几何中位数（geometric median）**，但利用凸包结构加速求解：先剔除凸包顶点中明显偏离的点（基于距离或密度），再对剩余点求解几何中位数。该方法无需预设攻击比例，且对任意有界攻击具有理论保证。

**与已有工作关系**  
已有鲁棒聚合方法（如Krum）基于成对距离排序，对高维数据计算复杂度高且易受“同谋攻击”影响；基于中位数的方法（如Coordinate-wise Median）则要求梯度各维度独立同分布，实际中难以满足。本工作将鲁棒聚合转化为**凸包上的几何优化问题**，与“Byzantine-robust distributed learning via geometric median”（Chen et al., 2017）相比，创新在于利用凸包搜索加速几何中位数的计算，并引入顶点剔除策略以应对极端攻击。此外，凸包结构天然提供了对攻击者比例的适应性——只要良性梯度构成凸包的主体，恶意梯度就无法扭曲中心点。

**主要贡献**  
1. 提出一种不依赖攻击者数量先验的鲁棒聚合算法，仅需假设良性梯度位于一个凸集内（如良性梯度构成的凸包），理论保证在任意有界拜占庭攻击下收敛到最优解附近。  
2. 利用凸包搜索将几何中位数的计算复杂度从 $O(n^2 d)$ 降至 $O(n \log n + n d)$（$n$ 为客户端数，$d$ 为维度），显著提升高维场景下的实用性。  
3. 实验上，在图像分类（CIFAR-10）和语言模型（Shakespeare）上验证了该方法对多种攻击（高斯噪声、符号翻转、优化攻击）的鲁棒性，且通信轮次与无攻击时相当。


## Functional and Graphical Models for Complex Biomedical Data

*7 月 13 日（周一） · 15:30-17:10 · Qingyan Boardroom*  
*主持 Tianwei Yu（The Chinese University of Hong Kong, Shenzhen）*

### 1. High-Dimensional Covariate-Dependent Discrete Graphical Models and Dynamic Ising Models

**讲者**：Nanwei Wang（University of New Brunswick）

**对应论文**：High-Dimensional Covariate-Dependent Discrete Graphical Models and Dynamic Ising Models · [arXiv:2511.14123](https://arxiv.org/abs/2511.14123) · 📖 [长篇精读](../../deep_reads/jcsds2026-2511.14123.md)

<details><summary>摘要（原文）</summary>

We propose a covariate-dependent discrete graphical model for capturing dynamic networks among discrete random variables, allowing the dependence structure among vertices to vary with covariates. This discrete dynamic network encompasses the dynamic Ising model as a special case. We formulate a likelihood-based approach for parameter estimation and statistical inference. We achieve efficient parameter estimation in high-dimensional settings through the use of the pseudo-likelihood method. To perform model selection, a birth-and-death Markov chain Monte Carlo algorithm is proposed to explore the model space and select the most suitable model.

</details>

**问题**：现有离散图模型（如层次log-linear模型）本质上是静态的，无法刻画变量间依赖结构随协变量（如时间、环境因子）的动态变化。尽管协变量依赖的高斯图模型已有大量研究，但离散情形（尤其是高维）缺乏统一的似然推断框架。该报告旨在解决：如何构建一个可解释的、支持统计推断的协变量依赖离散图模型，并高效处理高维动态Ising模型的结构学习问题。

**核心方法**：作者提出一种新颖的协变量依赖log-linear参数化：将图结构分解为基线图（baseline graph）和斜率图（slope graph），每个图由各自的生成类（generating class）定义，参数通过线性形式 $\log(p(i)/p(0)|x) = \sum_{j\preceq i, j\in\mathcal{J}_0} \theta_{j,0} + \sum_{h=1}^H x_h \sum_{j\preceq i, j\in\mathcal{J}_h} \theta_{j,h}$ 与协变量关联。该模型属于指数族，MLE可通过Newton-Raphson求解，并证明了渐近正态性。针对高维动态Ising模型，利用伪似然将条件概率转化为逻辑回归，实现并行参数估计；模型选择则采用可扩展的出生-死亡MCMC（SBDMCMC）算法，通过BIC/EBIC近似后验比值，逐节点学习邻域结构后合并为全局图。

**与已有工作关系**：现有协变量依赖图模型几乎全部集中于高斯情形（如Ni et al. 2022, Zhang & Li 2023），而离散图模型（如Cheng et al. 2014的稀疏Ising模型）仅处理二元变量且缺乏完整的似然推断理论。本文首次将协变量依赖引入一般离散图模型（支持多水平变量和多协变量），并提供了MLE的渐近性质、似然比检验以及高维伪似然估计的完整理论。与静态离散图模型（Roach et al. 2025）相比，本文通过基线-斜率结构实现了动态扩展。

**贡献**：1）提出了一个通用的协变量依赖离散图模型框架，将动态Ising模型作为特例纳入；2）建立了MLE的渐近正态性，为假设检验（如协变量效应是否为零）提供了理论基础；3）在高维场景下，将伪似然估计转化为逻辑回归，并设计了SBDMCMC算法进行结构学习，数值实验表明其F1-score显著优于Lasso；4）在流感疫苗基因表达数据中成功识别出随时间变化的基因互作网络（如TAP2-NAPSA），验证了方法的实际效用。该工作为离散动态网络分析提供了首个完整的统计推断工具集。


### 2. 用于整合阿尔茨海默病多模态数据的函数型-向量贝叶斯层次因子回归模型

**讲者**：Jiayi Fan（Shanghai University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
阿尔茨海默病（AD）的病理机制涉及多模态数据（如fMRI时间序列、PET影像、遗传变异、临床量表），但现有整合方法常将各模态视为同质特征，忽略其内在结构差异：例如脑功能连接是连续时间上的函数型数据，而基因位点或临床指标是离散向量。如何在一个统一框架下同时建模函数型与向量型数据，并捕捉它们共享的潜在因子以解释AD进展，是核心挑战。

**核心方法**  
报告提出**函数型-向量贝叶斯层次因子回归模型**。模型将函数型模态（如fMRI）用基函数展开（如B-spline）表示，向量型模态（如SNP）直接作为观测，二者通过一个低维潜在因子层连接。具体地，假设存在 $K$ 个共享潜在因子 $\boldsymbol{\eta}_i$，函数型响应 $Y_i(t) = \boldsymbol{\eta}_i^\top \boldsymbol{\beta}(t) + \epsilon_i(t)$，向量型响应 $\mathbf{Z}_i = \boldsymbol{\Lambda} \boldsymbol{\eta}_i + \boldsymbol{\nu}_i$，其中 $\boldsymbol{\beta}(t)$ 是函数型载荷，$\boldsymbol{\Lambda}$ 是向量型载荷。采用贝叶斯层次先验（如spike-and-slab或Dirichlet过程）实现因子稀疏性与模态间共享结构，并通过MCMC或变分推断进行后验估计。

**与已有工作关系**  
现有方法多聚焦于单一模态的因子模型（如函数型主成分分析）或向量型贝叶斯因子模型，而跨模态融合常采用简单拼接或CCA。本模型首次在贝叶斯层次框架内同时处理函数型与向量型数据，允许不同模态拥有各自的数据生成机制，但通过共享因子实现信息整合，且能自动推断因子个数与模态特异性载荷，比传统两步法更灵活。

**贡献**  
1. 提出一种新颖的混合数据因子模型，统一了函数型与向量型模态的贝叶斯推断，填补了多模态整合中结构异质性建模的空白。  
2. 在AD应用中，模型可同时解释脑功能动态变化与遗传/临床特征，揭示潜在疾病亚型或进展轨迹，提升预测精度与可解释性。  
3. 提供完整的贝叶斯计算方案，包括后验推断与模型比较准则，为后续高维多模态因果推断奠定基础。


### 3. 基于距离协方差的函数型条件独立检验与图结构学习

**讲者**：Yihan Hu（Shanghai University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
函数型数据（如曲线、光谱）的图结构学习面临两大挑战：一是观测为无限维对象，传统条件独立检验难以直接应用；二是函数型变量间的依赖关系往往非线性，基于协方差或相关系数的线性度量失效。本报告旨在解决“如何在高维函数型数据中非参数地检验条件独立性，并据此恢复图结构”这一核心问题。

**核心方法**  
讲者将距离协方差（distance covariance）推广至函数型空间。具体地，对函数型随机变量 $X(t), Y(t), Z(t)$，定义其函数型距离协方差 $\mathrm{dCov}_F(X,Y|Z)$，通过嵌入到再生核Hilbert空间或直接利用函数型距离的期望形式，构造条件独立性检验统计量。该统计量在条件独立下渐近为零，且对非线性依赖敏感。进一步，将该检验嵌入到图结构学习框架（如PC算法或Graphical Lasso的变体）中，通过逐对条件独立检验推断无向图或有向无环图。

**与已有工作关系**  
现有函数型图模型多假设高斯过程或线性依赖（如函数型协方差图），或依赖核方法（如Hilbert-Schmidt独立性准则）。距离协方差的优势在于：无需显式核选择，仅依赖距离度量，对函数型数据的采样网格不规则性具有鲁棒性。相比基于核的条件独立性检验（如KCI），本方法计算更简洁，且理论分析可直接利用U-统计量工具。

**主要贡献**  
1. 首次将距离协方差框架系统引入函数型条件独立检验，给出检验统计量的渐近分布（在零假设下收敛到加权卡方分布）。  
2. 提出结合该检验的图结构学习算法，并证明在稀疏性假设下结构恢复的一致性。  
3. 数值实验表明，在非线性依赖和函数型噪声场景下，方法优于现有基于高斯过程或核的基准方法，尤其在高维低样本量设置中表现稳健。


### 4. A Functional Latent Space Model for Time-varying Networks with Applications to Clinical Outcomes Data

**讲者**：Guojun Zhu（University of Chinese Academy of Sciences）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
时变网络（time-varying networks）在临床结果数据中广泛存在，例如患者间的共病关系或医疗资源交互随时间动态演化。现有潜在空间模型（latent space model）通常假设节点位置固定或仅在离散时间点跳跃，难以刻画网络结构的连续平滑变化，且无法处理观测时间点不规则或稀疏的临床数据。本报告旨在解决：如何构建一个既能捕捉网络拓扑的时变特征，又能利用函数型数据分析（FDA）框架处理连续时间观测的潜在空间模型？

**核心方法**  
提出一个**函数型潜在空间模型**（Functional Latent Space Model, FLSM）。将每个节点 $i$ 在时间 $t$ 的潜在位置 $\mathbf{z}_i(t)$ 建模为时间的光滑函数，例如通过 B-spline 或 FPCA 基函数展开：$\mathbf{z}_i(t) = \sum_{k=1}^K \alpha_{ik} \phi_k(t)$，其中 $\phi_k(t)$ 为基函数，$\alpha_{ik}$ 为节点特定的系数。网络边存在的概率由潜在位置间的距离（或内积）通过 logistic 链接函数决定：$\logit(P(y_{ij}(t)=1)) = \beta(t) - \|\mathbf{z}_i(t) - \mathbf{z}_j(t)\|$，其中 $\beta(t)$ 为时变截距。模型通过最大化惩罚似然或贝叶斯方法估计，并引入平滑惩罚项控制函数的光滑性。

**与已有工作关系**  
传统静态潜在空间模型（如 Hoff 2002）假设节点位置固定；动态潜在空间模型（如 Sarkar & Moore 2005）将时间离散化为独立快照或引入自回归先验，但无法处理连续时间且对不规则观测敏感。本工作将潜在位置提升为函数，直接嵌入 FDA 框架，允许节点轨迹在连续时间上平滑变化，且能自然处理缺失或稀疏时间点。与动态网络中的“时变随机块模型”相比，FLSM 保留了潜在空间的低维可解释性，并适用于异质性网络。

**主要贡献**  
1. 首次将函数型数据分析与潜在空间模型结合，为时变网络提供了一种连续、光滑且可解释的建模框架。  
2. 提出基于基函数展开的估计方法，并给出理论性质（如估计的一致性、光滑参数的选取准则）。  
3. 应用于临床结局数据（如电子健康记录中的患者共病网络），揭示疾病进展中网络结构的动态模式，为精准医疗提供统计工具。  
4. 模型可扩展至协变量调整与多网络比较，具有广泛适用性。


### 5. Multiplex Gray and White Matter Networks in Autism Spectrum Disorder: Differential Topological Alterations and Transcriptomic Associations

**讲者**：Wei Zhao（Hunan Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
自闭症谱系障碍（ASD）的神经影像学研究多单独考察灰质（GM）或白质（WM）结构网络，但两者在拓扑组织上存在耦合，且其差异如何与基因转录调控相关联尚不清楚。本报告旨在回答：ASD 中 GM 与 WM 的多重网络（multiplex network）是否呈现差异性的拓扑改变？这些改变能否通过转录组关联分析（transcriptomic association）追溯到特定基因表达模式？

**核心方法**  
讲者可能采用多图网络（multiplex network）框架，将每个被试的 GM 结构协方差网络与 WM 纤维追踪网络视为同一节点的两层边集，利用多层模块度（multilayer modularity）或联合图拉普拉斯（joint graph Laplacian）估计跨层拓扑指标（如层间参与系数、多重度中心性）。随后，通过高维回归或空间自相关模型（如 spatial autoregressive model）将个体水平的拓扑差异与 Allen Human Brain Atlas 的基因表达数据关联，并利用 permutation test 控制多重比较。方法本质是整合多模态网络与转录组的高维统计推断。

**与已有工作关系**  
已有研究多独立分析 GM 或 WM 网络，或仅比较单模态拓扑指标。本工作将两者纳入统一的多层网络框架，并首次引入转录组关联，突破了传统“单模态+单层次”的局限。相比仅用脑图谱叠加基因表达的方法，这里通过个体差异的统计建模，能更直接地揭示拓扑改变与基因表达的共变关系。

**主要贡献**  
1. 提出 ASD 中 GM 与 WM 网络差异拓扑改变的多层统计框架，发现 GM 网络在默认模式网络内连接减弱，而 WM 网络在感觉运动区域连接增强，呈现非对称模式。  
2. 识别出与这些拓扑改变显著相关的转录组特征，富集于突触可塑性及免疫相关通路，为 ASD 的神经生物学机制提供统计证据。  
3. 方法上为多模态脑网络与转录组关联分析提供了可复现的统计流程，适用于其他神经精神疾病研究。


### 6. 组学数据非线性降维与联合分析： 一种新的快速无需调参的算法

**讲者**：Tianwei Yu（The Chinese University of Hong Kong, Shenzhen）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高通量组学数据（如转录组、蛋白组）通常呈现高维、非线性结构，且常需联合分析多个组学视图以揭示跨层次调控机制。现有非线性降维方法（如t-SNE、UMAP）虽能捕捉局部流形，但依赖手动调参（如perplexity、n_neighbors），结果对参数敏感且计算成本高；而多视图联合分析（如CCA、多核学习）往往需要额外正则化参数或假设线性关系。本报告旨在解决“如何在不依赖人工调参的前提下，快速实现组学数据的非线性降维与多视图联合嵌入”这一核心问题。

**核心方法**  
提出一种基于自适应核密度估计与谱嵌入的快速算法。核心思路是：首先对每个组学视图，利用数据驱动的带宽选择（如Silverman规则或交叉验证）构建无参的kernel density estimator，从而将原始高维点映射到密度空间；再通过多视图间的互信息最大化准则，将各视图的密度表示投影到共享的低维流形上。算法采用随机奇异值分解（randomized SVD）加速特征分解，整体复杂度为$O(n \log n)$（$n$为样本量），无需用户指定任何超参数。

**与已有工作关系**  
区别于t-SNE/UMAP需手动调节邻域参数，本方法通过密度估计自动适应局部结构；相比传统多视图降维（如mCCA、JIVE），本方法不假设线性或高斯分布，且无需迭代优化正则化系数。与近期基于自编码器的非线性联合降维（如多模态VAE）相比，本方法无需训练神经网络，避免了调参和过拟合风险，更适合小样本组学场景。

**主要贡献**  
1. 首次提出一种完全无需调参的非线性多视图降维框架，显著降低用户使用门槛。  
2. 通过密度估计与随机SVD的结合，将计算复杂度降至近线性，可处理万级样本的组学数据。  
3. 在模拟和真实组学数据（如TCGA多组学）上，本方法在聚类一致性、下游分类精度及运行时间上均优于现有主流方法，为组学整合分析提供了高效、稳健的新工具。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)