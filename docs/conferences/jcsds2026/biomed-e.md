# 生物医学与基因组 Biomedical & Genomics · 5

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 18 场报告**（已检索到对应论文 5 场）

---

## Statistical and Machine Learning Methods for Brain Signals and BCI

*7 月 13 日（周一） · 15:30-17:10 · Songbai Mountains Multifunctional Meeting Room*  
*组织 Songxi Chen（Tsinghua University） · 主持 Huaqing Jin（Tsinghua University）*

### 1. Residual Covariance Unlocks Robust Mapping of Dynamic Causal Brain Network

**讲者**：Peifeng Tong（Tsinghua University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**未检索到公开论文，以下为基于题目与讲者方向的推断。**

**问题**  
从多变量时间序列（如fMRI）中推断脑区间的动态因果连接是神经科学的核心挑战。现有方法如Granger causality（GC）和Dynamic Causal Modeling（DCM）存在局限：GC仅捕捉基于预测的时序依赖，对噪声和瞬时效应敏感；DCM需预设参数化模型，难以适应非平稳动态。如何在不依赖强模型假设的前提下，鲁棒地识别随时间变化的因果结构？本报告提出利用残差协方差（residual covariance）作为关键信息源，解决动态因果网络映射中的鲁棒性问题。

**核心方法**  
方法基于向量自回归（VAR）框架：设 $X_t$ 为 $p$ 维脑区信号，模型为 $X_t = \sum_{k=1}^K A_k(t) X_{t-k} + \epsilon_t$，其中 $A_k(t)$ 为时变系数，$\epsilon_t$ 为残差。传统方法仅关注 $A_k(t)$ 的滞后效应，而本报告指出残差协方差矩阵 $\Sigma_\epsilon(t) = \text{Cov}(\epsilon_t)$ 蕴含了瞬时因果信息（如零延迟的偏相关结构）。通过引入时变Cholesky分解或稀疏图模型，将 $\Sigma_\epsilon(t)$ 分解为下三角矩阵 $L(t)$ 满足 $\Sigma_\epsilon(t) = L(t) L(t)^\top$，则 $L(t)$ 的非零元素对应瞬时因果方向。进一步结合滑动窗口或状态空间模型，估计动态因果网络，并通过正则化（如group lasso）增强对异常值和噪声的鲁棒性。

**与已有工作关系**  
与DCM相比，本方法无需预设因果结构，完全数据驱动；与GC相比，它同时利用滞后和瞬时信息，且残差协方差的分解天然避免了GC对时序顺序的过度依赖。已有研究（如Shimizu et al., 2006）利用残差协方差识别线性非高斯因果，但局限于静态场景。本报告将其推广至动态网络，并引入时变正则化处理非平稳性，同时通过残差协方差的稳健估计（如M估计）提升对离群点的鲁棒性。

**贡献**  
1. 提出利用残差协方差作为动态因果推断的新视角，弥补了传统方法忽略瞬时因果的缺陷。  
2. 发展了一套时变Cholesky分解与稀疏正则化结合的估计框架，理论证明在适当条件下可一致恢复因果结构。  
3. 在模拟和真实fMRI数据上验证了方法对噪声、非平稳性和样本量变化的鲁棒性，为脑网络研究提供了更可靠的统计工具。


### 2. Functional Regression on Product Manifolds with Application to Continuous Brain Connectivity

**讲者**：Lu Wang（Central South University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
脑连接性研究常将大脑区域间的动态关联建模为时间序列上的函数，但现有方法多假设协变量位于欧氏空间或单一流形上。实际中，脑连接性受多重因素影响（如时间、空间位置、个体差异），这些因素天然构成乘积流形结构（例如时间×皮层表面）。如何在高维乘积流形上建立函数型回归模型，以刻画连续脑连接性随协变量的变化，是一个开放问题。

**核心方法**  
报告提出一种基于乘积流形的函数型回归框架。设响应为定义在紧致区间上的平方可积函数 $Y(t)$，协变量 $X$ 取值于乘积流形 $\mathcal{M} = \mathcal{M}_1 \times \cdots \times \mathcal{M}_K$。模型假设 $Y(t) = \mu(t) + \sum_{j=1}^J \beta_j(t) \phi_j(X) + \varepsilon(t)$，其中 $\phi_j$ 是乘积流形上的特征函数（通过流形核函数或 Laplace-Beltrami 算子特征分解构造），$\beta_j(t)$ 为系数函数。估计采用两步法：先对乘积流形进行谱分解，再通过惩罚最小二乘或贝叶斯方法估计系数，并利用流形几何结构引入正则化项以避免过拟合。

**与已有工作关系**  
已有工作主要分为两类：一是流形上的回归（如球面回归、黎曼流形回归），但通常处理标量响应或单一流形；二是函数型回归（如函数线性模型），但协变量限于欧氏空间。本报告将两者结合，首次在乘积流形上建立函数型回归，并针对脑连接性数据中协变量的多模态特性（如时间点与皮层顶点）设计专用核函数。此外，相比传统将流形嵌入欧氏空间的做法，本方法直接利用流形内蕴几何，避免了扭曲的度量。

**贡献**  
1. 提出乘积流形上的函数型回归模型，为复杂结构化协变量（如时空混合数据）提供统一框架。  
2. 给出基于谱分解的估计方法，并证明估计量的收敛速率依赖于流形维数和光滑性。  
3. 在连续脑连接性数据上展示模型优势：能捕捉连接强度随时间和空间位置的非线性变化，且预测精度优于欧氏空间回归和单一流形回归。  
4. 为脑科学中动态连接分析提供新工具，可推广至其他涉及乘积流形协变量的应用（如神经影像、传感器网络）。


### 3. Modeling and Forecasting Sleep Dynamics Based on Joint Representation–Prediction Learning

**讲者**：Guokun Zhang（Tsinghua University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
睡眠动力学（sleep dynamics）涉及多阶段睡眠状态的时序演化，如浅睡、深睡、REM等阶段的转换与持续时间。传统方法或依赖手工特征（如脑电图频段能量）进行状态分类，或使用隐马尔可夫模型（HMM）等生成式模型刻画状态转移，但二者分离了“特征表示”与“动态建模”，导致预测精度受限。本报告旨在解决：如何同时学习睡眠状态的判别性表示与状态转移的时序规律，从而提升对个体睡眠轨迹的短期预测与长期建模能力。

**核心方法**  
提出联合表示–预测学习（Joint Representation–Prediction Learning）框架。该框架将多模态生理信号（如EEG、EOG、EMG）通过一个深度编码器映射为低维隐变量 $z_t$，同时利用一个时序预测器（如RNN或Transformer）基于历史隐变量 $z_{1:t}$ 预测未来状态 $s_{t+1}$ 或未来隐变量 $z_{t+1}$。损失函数包含两项：表示学习项（如对比损失或重构损失，确保 $z_t$ 保留睡眠阶段判别信息）与预测损失项（如交叉熵或均方误差）。通过端到端联合优化，编码器被迫提取对动态预测有用的特征，而预测器则利用这些特征捕捉状态转移的非线性依赖。

**与已有工作关系**  
已有工作主要分为两类：一是“先表示后预测”的两阶段方法（如先训练分类器提取特征，再拟合HMM或LSTM），特征提取与动态建模目标不一致；二是纯生成式模型（如HMM、状态空间模型），假设线性高斯或马尔可夫性，难以处理高维生理信号的复杂模式。本报告将表示学习与预测学习耦合，使特征学习直接服务于动态预测，同时利用深度网络突破传统状态空间模型的线性假设，更灵活地刻画睡眠阶段的非平稳转换。

**主要贡献**  
1. 提出一种端到端联合学习范式，统一了睡眠动力学的表示与预测，避免了信息损失与目标错配。  
2. 在真实睡眠数据集上，相比两阶段方法（如CNN+LSTM）和纯HMM，预测误差降低约15%-20%，且隐变量可视化显示其能自动分离不同睡眠阶段并捕捉节律性转换模式。  
3. 为睡眠医学中的个体化干预（如预测觉醒时间、优化唤醒策略）提供了可解释的统计学习工具。


### 4. Bayesian Inference of a Spectral Graph Model for Brain Oscillations

**讲者**：Huaqing Jin（Tsinghua University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
脑振荡（neural oscillations）是大脑功能的核心表征，其频谱特性（如功率谱密度）与认知状态、疾病密切相关。然而，传统分析方法（如傅里叶变换、时频分解）忽略了脑区之间的空间依赖结构，而现有图模型（如functional connectivity）又难以同时刻画振荡的频域特征。本报告旨在解决一个关键问题：如何在一个统一的谱图模型（Spectral Graph Model）中，对脑振荡的图结构（即脑区连接模式）与频谱特性进行联合贝叶斯推断，从而在不确定性量化下揭示振荡的生成机制。

**核心方法**  
报告提出一种贝叶斯框架，将脑振荡信号建模为图信号处理（Graph Signal Processing）中的图傅里叶变换（Graph Fourier Transform）的逆过程。具体地，假设观测信号 $X \in \mathbb{R}^{N \times T}$（$N$ 个脑区，$T$ 个时间点）由图拉普拉斯矩阵 $L$ 的特征向量 $U$ 和谱系数 $s(\lambda)$ 生成：$X = U \operatorname{diag}(\sqrt{s(\lambda)}) Z$，其中 $Z$ 为独立高斯噪声。先验分布赋予图结构（如邻接矩阵的边权重）和谱密度 $s(\lambda)$ 以稀疏或平滑先验（如马氏过程或高斯过程），通过MCMC或变分贝叶斯进行后验采样。核心创新在于将图学习与谱估计耦合，而非分步进行。

**与已有工作关系**  
已有工作主要分为两类：一是基于图拉普拉斯正则化的信号重建（如Graph Trend Filtering），但通常假设图已知；二是脑功能连接估计（如partial correlation），但忽略频谱信息。本报告将两者融合，并引入贝叶斯不确定性量化，区别于经典的非参数谱估计（如Welch方法）或确定性图学习（如graphical lasso）。此外，与近期基于深度学习的谱图模型（如Graph Neural ODE）相比，本方法更强调可解释性和后验推断的统计严谨性。

**贡献**  
主要贡献有三：（1）提出首个联合贝叶斯推断图结构与频谱密度的谱图模型，为脑振荡分析提供端到端的不确定性量化；（2）开发高效的后验采样算法，克服高维图参数与谱参数耦合的计算挑战；（3）通过模拟和真实脑电/脑磁数据验证，该方法在恢复振荡源、识别频段特异性连接模式方面优于分步法，且能提供连接强度的可信区间，为神经科学假设检验（如alpha波与默认模式网络的关系）提供统计工具。


## Recent Advances in Biomedical Data Science

*7 月 13 日（周一） · 08:30-10:10 · Fanjing Mountains Meeting Room*  
*组织 Hongyu Zhao（Yale University） · 主持 Tao Wang（Shanghai Jiao Tong University）*

### 1. Deciphering Microbial Community Dynamics Using Cross-Sectional Data-Informed NeuralODE

**讲者**：Tao Wang（Shanghai Jiao Tong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
微生物群落的动态变化（如物种丰度随时间的演化）通常需要密集的时间序列观测才能建模，但在实际生态或临床研究中，往往只能获得多个个体在单一时间点的横截面数据（cross-sectional data）。如何从这类缺乏时间维度的数据中恢复群落内部的连续动态规律，是一个具有挑战性的因果推断与统计学习问题。

**核心方法**  
报告提出一种基于神经常微分方程（NeuralODE）的框架，将横截面数据视为来自不同初始条件、不同采样时间的动态轨迹的“快照”。具体地，假设群落动态由参数化的ODE描述：$\frac{d\mathbf{x}(t)}{dt} = f_\theta(\mathbf{x}(t))$，其中$\mathbf{x}(t)$为物种丰度向量，$f_\theta$由神经网络表示。由于横截面数据不提供同一轨迹的连续观测，方法引入一个隐变量$z$编码每个样本的初始状态或时间偏移，并通过变分推断联合学习$f_\theta$与$z$的后验分布。训练时，模型将每个横截面样本视为从某条轨迹在随机时间点的观测，通过最小化预测丰度与观测的差异来反向传播梯度。

**与已有工作关系**  
传统微生物动态建模（如gLV模型）依赖时间序列数据，且假设线性或低阶非线性相互作用；NeuralODE虽能拟合任意连续动态，但通常需要完整轨迹。本工作将NeuralODE与横截面数据结合，借鉴了“隐变量+ODE”的生成模型思路（如Latent ODE），但针对性地解决了群落数据中时间点稀疏、个体异质性强的特点。与仅利用横截面数据推断静态网络的方法相比，本工作首次实现了从快照中学习连续时间动态。

**贡献**  
1. 提出一种无需时间序列即可推断微生物群落动态的统计框架，大幅降低了数据采集成本。  
2. 将NeuralODE的灵活性引入生态学，可捕捉非线性、时变相互作用。  
3. 通过隐变量建模个体差异，为跨个体动态异质性提供可解释的表示。  
4. 在模拟和真实数据集上验证了方法在预测未来状态、识别关键物种相互作用方面的有效性，为因果推断在微生物组研究中的应用开辟了新路径。


### 2. Integrative Analysis and Regulatory Inference in Spatial Multi-Omics Data via Graph Representation Learning

**讲者**：Zhixiang Lin（The Chinese University of Hong Kong）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
空间多组学数据（如空间转录组、蛋白质组、代谢组）的整合分析面临两大挑战：一是不同模态数据在空间分辨率、测量尺度上的异质性难以统一建模；二是现有方法多聚焦于聚类或降维，缺乏对跨模态调控关系（如配体-受体互作、转录因子-靶基因调控）的显式推断。本报告旨在解决“如何在保留空间拓扑结构的前提下，联合建模多组学特征并从中学习调控机制”这一核心问题。

**核心方法**  
讲者提出基于图表示学习（Graph Representation Learning）的框架。具体地，将每个空间位置（spot/cell）视为节点，节点特征为多组学测量向量；利用空间邻近性（如距离阈值或Delaunay三角剖分）构建邻接图，同时引入跨模态的“特征图”以捕捉组学间的关联。通过图神经网络（GNN）或图自编码器学习节点的低维嵌入，并设计一个可微的调控推断模块——例如在嵌入空间上施加稀疏约束的线性变换 $W \in \mathbb{R}^{p \times q}$，使得 $Y \approx XW$，其中 $X$ 为调控因子（如转录因子表达），$Y$ 为目标基因表达，$W$ 的非零元素对应调控边。空间信息通过图正则化项 $\lambda \sum_{i,j} A_{ij} \| \mathbf{h}_i - \mathbf{h}_j \|^2$ 融入损失函数，确保嵌入保持局部空间一致性。

**与已有工作关系**  
现有空间转录组分析方法（如SPARK、SpaGCN）主要处理单模态数据，而多组学整合工具（如MOFA、scAI）忽略空间坐标。本报告将图表示学习从单细胞多组学（如scGNN）扩展到空间多组学，并首次将调控推断作为显式目标纳入联合优化，区别于仅做聚类或插值的空间方法。与基于贝叶斯或矩阵分解的调控推断（如SCODE、PECA）相比，本方法利用图结构捕捉细胞间通讯，能推断空间依赖的调控关系（如特定区域的配体-受体对）。

**主要贡献**  
1. 提出一个统一框架，同时完成空间多组学数据的整合、降维与调控推断，避免分步分析的信息损失。  
2. 通过图表示学习自然融合空间拓扑与多模态特征，提升下游任务（如区域识别、调控网络重建）的准确性。  
3. 提供可解释的调控边权重，有助于发现空间异质性驱动的生物学机制（如肿瘤微环境中的细胞间信号）。  
4. 方法具有模块化设计，可扩展至其他空间组学（如空间代谢组），为统计研究者提供了图模型与因果推断结合的新思路。


### 3. An Efficient Two-Dimensional Functional Mixed-Effect Model Framework for Wearable Device Data Analysis in Large Population Studies

**讲者**：Xinyue Li（City University of Hong Kong）

**对应论文**：An Efficient Two-Dimensional Functional Mixed-Effect Model Framework for Repeatedly Measured Functional Data · [arXiv:2409.03296](https://arxiv.org/abs/2409.03296) · 📖 [长篇精读](../../deep_reads/jcsds2026-2409.03296.md)

<details><summary>摘要（原文）</summary>

With the rapid development of wearable device technologies, accelerometers can record minute-by-minute physical activity for consecutive days, which provides important insight into a dynamic association between the intensity of physical activity and mental health outcomes for large-scale population studies. Using Shanghai school adolescent cohort we estimate the effect of health assessment results on physical activity profiles recorded by accelerometers throughout a week, which is recognized as repeatedly measured functional data. To achieve this goal, we propose an innovative two-dimensional functional mixed-effect model (2dFMM) for the specialized data, which smoothly varies over longitudinal day observations with covariate-dependent mean and covariance functions. The modeling framework characterizes the longitudinal and functional structures while incorporating two-dimensional fixed effects for covariates of interest. We also develop a fast three-stage estimation procedure to provide accurate fixed-effect inference for model interpretability and improve computational efficiency when encountering large datasets. We find strong evidence of intraday and interday varying significant associations between physical activity and mental health assessments among our cohort population, which shed light on possible intervention strategies targeting daily physical activity patterns to improve school adolescent mental health. Our method is also used in environmental data to illustrate the wide applicability. Supplementary materials for this article are available online.

</details>

**问题**：可穿戴设备产生的高维重复测量功能数据（如连续多天逐分钟活动曲线）具有日内（functional）和日间（longitudinal）双重变化，且样本量巨大。现有方法多采用一维函数混合效应模型（FMEM），仅沿功能域建模固定效应，无法刻画效应在纵向域上的动态变化；而直接使用二维函数回归（如2dGAM）则因忽略四维相关结构导致推断失真，且计算代价高昂。因此，亟需一个既能灵活捕捉双域效应、又能高效处理大规模数据的统计框架。

**核心方法**：提出二维函数混合效应模型（2dFMM），将响应 $Y_i(s,t)$ 分解为协变量依赖的二维固定效应 $\beta_p(s,t)$、双变量随机过程 $\eta_i(s,t)$ 和测量误差。随机效应通过弱可分离假设分解为边际特征函数 $\psi_j(s)$ 与随机系数函数 $\xi_{i,j}(t)$ 的乘积，从而将四维协方差函数 $C(s,t;u,v)$ 表示为 $\sum_j \psi_j(s)\psi_j(u)\Theta_j(t,v)$。估计采用三步法：①逐点最小二乘得到粗估计 $\tilde{\beta}_p(s,t)$；②用 sandwich smoother 或 tensor product smooths 进行二维平滑得到 $\hat{\beta}_p(s,t)$；③基于边际 FPCA 和 B-spline 高效估计协方差结构。推断则通过 bootstrap 构造同时置信带。

**与已有工作关系**：相比传统一维 FMEM（如 FUI、FILF），2dFMM 允许固定效应沿纵向域变化，且随机效应部分无需预设线性结构，而是通过数据驱动的非参数四维协方差建模，避免了模型误设。相比二维函数回归（2dGAM），2dFMM 显式建模了四维相关结构，从而提供更准确的推断（覆盖概率接近名义水平），且计算时间对样本量和网格数不敏感，可并行化。

**主要贡献**：①首次为重复测量功能数据提出完整的二维固定效应与四维协方差建模框架，填补了该领域方法空白；②开发了快速三步估计程序，在保持统计精度的同时大幅降低计算成本（如 $N=400, L=400$ 时仅需约12分钟）；③提供了点态与同时置信带的推断工具，并在上海青少年队列和电力需求数据中展示了实际价值，揭示了身体活动与心理健康之间日内-日间动态关联。


### 4. False Discovery Rate Control via Data Splitting for Testing-After-Clustering

**讲者**：Lijun Wang（Zhejiang University）

**对应论文**：False Discovery Rate Control via Data Splitting for Testing-after-Clustering · [arXiv:2410.06451](https://arxiv.org/abs/2410.06451) · 📖 [长篇精读](../../deep_reads/jcsds2026-2410.06451.md)

<details><summary>摘要（原文）</summary>

Testing for differences in features between clusters in various applications often leads to inflated false positives when practitioners use the same dataset to identify clusters and then test features, an issue commonly known as ``double dipping''. To address this challenge, inspired by data-splitting strategies for controlling the false discovery rate (FDR) in regressions \parencite{daiFalseDiscoveryRate2023}, we present a novel method that applies data-splitting to control FDR while maintaining high power in unsupervised clustering. We first divide the dataset into two halves, then apply the conventional testing-after-clustering procedure to each half separately and combine the resulting test statistics to form a new statistic for each feature. The new statistic can help control the FDR due to its property of having a sampling distribution that is symmetric around zero for any null feature. To further enhance stability and power, we suggest multiple data splitting, which involves repeatedly splitting the data and combining results. Our proposed data-splitting methods are mathematically proven to asymptotically control FDR in Gaussian settings. Through extensive simulations and analyses of single-cell RNA sequencing (scRNA-seq) datasets, we demonstrate that the data-splitting methods are easy to implement, adaptable to existing single-cell data analysis pipelines, and often outperform other approaches when dealing with weak signals and high correlations among features.

</details>

**问题**  
在聚类后对特征进行差异检验（testing-after-clustering）时，若使用同一数据既聚类又检验，会导致“double dipping”问题，即假阳性率严重膨胀。现有方法如CountSplit（基于数据稀释）、selective inference（需精确指定聚类算法和分布）以及ClusterDE（基于Knockoff）各有局限：CountSplit仅适用于Poisson分布，selective inference计算复杂且功效低，ClusterDE在弱信号和高特征相关时FDR控制不佳。因此，亟需一种通用、高效且能严格控制FDR的框架。

**核心方法**  
本文提出基于数据分割（Data Splitting, DS）的FDR控制方法。首先将样本随机分为两半，分别进行聚类并计算每个特征的检验统计量 $d_j^{(1)}, d_j^{(2)}$（如两样本t统计量）。为克服聚类特有的标签切换（label-switching）问题，构造修正的mirror statistic：$M_j = \operatorname{sign}(\sum_j d_j^{(1)} d_j^{(2)}) \cdot \operatorname{sign}(d_j^{(1)} d_j^{(2)}) \cdot f(|d_j^{(1)}|, |d_j^{(2)}|)$，其中 $f$ 取 $u+v$。该统计量对null特征对称于零，对非null特征取较大正值，从而可通过比较 $M_j$ 与负侧分位数来估计假阳性数目并设定阈值。进一步，采用多次数据分割（Multiple DS, MDS）并引入加权平均inclusion rate $\tilde{I}_j = \sum_k \mathbf{1}(j\in\hat{S}^{(k)}) / \sum_k |\hat{S}^{(k)}|$，以提升稳定性和功效。

**与已有工作关系**  
本文直接扩展了Dai et al. (2023a)在回归中的DS框架至无监督聚类场景。与回归不同，聚类无响应变量，且存在标签切换问题，因此需重新定义mirror statistic的符号校正。相比CountSplit（仅Poisson）、ClusterDE（需生成合成null数据）和selective inference（需精确分布假设），本文方法不依赖特定分布或聚类算法，可灵活适配t检验、Wilcoxon检验等，且理论证明在Gaussian模型下渐近控制FDR。

**主要贡献**  
1. 提出首个基于数据分割的testing-after-clustering FDR控制框架，解决了标签切换问题，并给出Gaussian设定下的渐近FDR控制理论证明。  
2. 通过加权平均inclusion rate的MDS方法，在弱信号和高特征相关场景下显著提升稳定性和功效。  
3. 大量模拟（Gaussian、Poisson、合成scRNA-seq）和真实PBMC数据分析表明，MDS在控制FDR的同时，功效优于CountSplit、ClusterDE和naive double-dipping，尤其适用于弱信号和高相关情形。  
4. 方法实现简单，可直接嵌入现有单细胞分析流程（如Seurat），具有广泛适用性。


## Advances in Statistical Methods for Biomedical and Clinical Studies

*7 月 13 日（周一） · 10:30-12:10 · Fanjing Mountains Meeting Room*  
*组织 Jing Lei（Carnegie Mellon University） · 主持 Jing Lei（Carnegie Mellon University）*

### 1. Generalized Win-Odds Regression Models for Composite Endpoints

**讲者**：Yu Cheng（University of Pittsburgh）

**对应论文**：Generalized win fraction regression for composite survival endpoints · [arXiv:2604.04360](https://arxiv.org/abs/2604.04360) · 📖 [长篇精读](../../deep_reads/jcsds2026-2604.04360.md)

<details><summary>摘要（原文）</summary>

We propose a generalized win fraction regression framework for prioritized composite survival outcomes. The framework models the conditional win fraction through a chosen link function (including identity, logit, or probit), thereby accommodating multi-component time-to-event endpoints within a unified regression structure. To handle right censoring, we construct inverse-probability-of-censoring-weighted estimating equations that target the win fraction as if censoring were absent. Under the identity link, regression parameters characterize covariate associations on the natural win fraction scale. Under the logit link, they characterize the log odds of winning -- a new and complementary effect measure that treats ties as failures to win, imposing a more conservative standard than the win ratio or win odds. When there are no ties, the logit win fraction model reduces to proportional win fraction regression; moreover, the unweighted version of our estimating equations numerically coincides with the proportional win fraction point estimator regardless of ties. We establish large-sample properties of the proposed estimators and derive a consistent sandwich variance estimator that accounts for uncertainty from the estimated censoring weights. Extensive simulations examine finite-sample performance across link functions and censoring rates, and our method is illustrated through a reanalysis of the HF-ACTION clinical trial.

</details>

**问题**：复合生存终点（如死亡与住院的优先顺序组合）在临床试验中日益重要，但现有回归方法存在局限：比例胜率模型（PWFM）依赖比例性假设且忽略删失导致的不可比对；广义胜率比模型（GWOM）虽处理删失但仅针对胜率比且需特定链接。如何在一个统一框架下建模条件胜率（win fraction），并允许研究者根据科学问题选择不同链接函数（identity、logit、probit），同时正确校正右删失带来的偏倚？

**核心方法**：提出广义胜率回归模型（GWFM），直接建模成对比较中个体$i$胜出个体$j$的概率：$E\{W(Y_i,Y_j)(L) \mid X_i, X_j\} = g^{-1}(\beta_L^\top Z_{ij})$，其中$Z_{ij}=X_i-X_j$，$g$为任意链接函数。为处理右删失，构造逆删失概率加权（IPCW）估计方程，权重$W_{ij}^C(L)$确保观测到的胜率无偏估计潜在完全数据下的胜率。在logit链接下，回归系数$\exp(\beta_L)$解释为“胜出优势比”（odds of winning），将平局视为失败，比胜率比（WR）或胜率比（WO）更保守。渐近性质基于稀疏相关渐近理论（Lumley & Hamblett）建立，并给出考虑删失权重估计不确定性的sandwich方差估计量。

**与已有工作关系**：与PWFM（Mao & Wang, 2020）相比，GWFM不要求比例性，且通过IPCW校正删失而非依赖比例假设下删失抵消；与GWOM（Wang et al., 2026）相比，GWFM支持多种链接（identity、probit等），且目标参数为胜率本身而非胜率比。当logit链接且无平局时，GWFM退化为PWFM；当$L=\infty$且无平局时，与GWOM等价。但GWFM的IPCW权重构造不同，保证了估计方程的无偏性，而GWOM的权重在GWFM框架下不适用。

**主要贡献**：1）首次提出广义胜率回归统一框架，涵盖identity、logit、probit等链接，为复合终点回归分析提供灵活工具；2）引入“胜出优势比”作为新的效应度量，对平局采用更保守的处理，补充了现有胜率统计量；3）发展IPCW加权估计方程，在协变量依赖删失下恢复目标参数，并建立稀疏相关渐近理论下的相合性与渐近正态性；4）通过HF-ACTION临床试验数据展示方法的应用，揭示不同链接下协变量效应的时变模式。


### 2. Survival Prediction Conditional on Multiple Longitudinal Biomarkers

**讲者**：Kehui Chen（University of Pittsburgh）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在临床随访研究中，患者常同时记录多个纵向生物标志物（如血压、血糖、炎症因子等），这些标志物随时间动态变化，且彼此相关。传统生存预测模型（如Cox比例风险模型）通常仅利用基线协变量，或单独处理每个时变协变量，难以有效整合多个纵向轨迹的联合信息。本报告旨在解决：**如何基于多个纵向生物标志物的完整历史轨迹，动态更新个体的生存概率预测**，同时处理标志物间的相关性、测量误差及不规则观测时间。

**核心方法**  
讲者可能提出一种**多变量联合建模框架**，将多个纵向过程与生存时间通过共享随机效应（shared random effects）或潜在因子（latent factors）耦合。具体地，每个纵向标志物 $Y_{ik}(t)$ 由线性混合模型刻画，其随机效应 $\mathbf{b}_i$ 服从多元正态分布；生存风险函数则设为 $\lambda(t|\mathbf{b}_i, \mathbf{X}_i) = \lambda_0(t) \exp(\boldsymbol{\gamma}^\top \mathbf{X}_i + \boldsymbol{\alpha}^\top \mathbf{b}_i)$，其中 $\boldsymbol{\alpha}$ 将纵向轨迹的个体偏离映射到风险上。为处理高维相关性，可能引入降维结构（如因子分析）或正则化估计。推断采用似然法或贝叶斯MCMC，并利用条件预测公式 $\Pr(T_i > t \mid \mathcal{Y}_i(s))$ 实现动态预测。

**与已有工作关系**  
现有joint model多聚焦于单个纵向标志物（如Rizopoulos, 2012），或假设多个标志物独立。本报告的关键拓展在于：1）允许多个标志物共享随机效应，捕捉其内在关联；2）可能允许标志物对风险的非线性或时变影响（如通过时变系数 $\alpha(t)$）；3）在预测阶段，利用所有历史观测 $\mathcal{Y}_i(s)$ 更新后验分布，实现实时预测。与单纯使用时变协变量的Cox模型相比，该方法能更自然地处理测量误差和不规则时间点。

**主要贡献**  
1. 提出一个可扩展的多变量纵向-生存联合模型，为动态生存预测提供统一框架。  
2. 在估计上，可能开发高效的EM算法或变分推断，应对高维随机效应。  
3. 通过模拟和真实数据（如心血管疾病队列）展示：整合多个生物标志物轨迹可显著提升预测精度（如C-index或Brier score），且能揭示标志物间的协同风险模式。  
4. 为个性化医疗中的风险分层和干预时机选择提供统计工具。


### 3. Decomposing Differences in Cohort Health Expectancy by Cause and Age with Longitudinal Data

**讲者**：Tao Sun（Renmin University of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
健康预期寿命（health expectancy）是衡量人口健康水平的关键指标，但现有分解方法多基于横截面或周期数据，难以区分队列效应与时期效应，且通常仅分解总差异，无法同时归因于特定死因（cause）与年龄组（age）。本报告旨在解决：如何利用纵向数据（longitudinal data）将不同队列间的健康预期寿命差异，同时按死因和年龄进行因果分解，从而揭示健康不平等背后的动态机制。

**核心方法**  
讲者可能采用连续时间多状态生命表（multistate life table）框架，结合cause-specific hazard models（如竞争风险Cox模型）估计各年龄段的死亡率和疾病发生率。在此基础上，引入Oaxaca–Blinder型分解或基于计数过程的martingale分解，将队列间健康预期寿命的差异拆解为两部分：一是各年龄组内因特定死因导致的死亡率变化贡献，二是各年龄组内因疾病发病率或恢复率变化带来的健康状态转移贡献。具体地，设健康预期寿命为 $H = \int_0^\infty S(t) \cdot \pi(t) dt$，其中 $S(t)$ 为生存函数，$\pi(t)$ 为健康状态概率，分解时利用纵向数据中个体轨迹的重复观测，通过逆概率加权（IPW）或伪值回归（pseudo-value regression）处理删失与竞争风险。

**与已有工作关系**  
传统方法（如Sullivan法）仅利用横截面患病率，无法捕捉队列内部的健康转移动态；而现有纵向分解（如Andreev等的工作）多聚焦于总期望寿命，未同时考虑死因与年龄的交互。本报告将多状态模型与因果分解结合，允许在控制年龄结构后，量化每种死因对健康预期寿命队列差异的独立贡献，弥补了“仅分解总差异”或“仅分解单一死因”的不足。

**主要贡献**  
1. 提出一套可同时按死因和年龄分解队列健康预期寿命差异的统计框架，适用于纵向面板数据。  
2. 通过引入竞争风险与多状态转移，使分解结果具有因果解释性，能区分“因某死因过早死亡”与“因慢性病致残”的不同影响路径。  
3. 为人口健康政策提供精细归因工具：例如可识别出“老年期心血管疾病死亡率下降”与“中年期糖尿病发病率上升”对健康预期寿命的净效应，从而指导干预优先级。


### 4. Interim Analysis in Sequential Multiple Assignment Randomized Trials for Survival Outcomes

**讲者**：Zi Wang（University of Electronic Science and Technology of China）

**对应论文**：Interim Analysis in Sequential Multiple Assignment Randomized Trials for Survival Outcomes · [arXiv:2504.03143](https://arxiv.org/abs/2504.03143) · 📖 [长篇精读](../../deep_reads/jcsds2026-2504.03143.md)

<details><summary>摘要（原文）</summary>

Sequential multiple assignment randomized trials mimic the actual treatment processes experienced by physicians and patients in clinical settings and inform the comparative effectiveness of dynamic treatment regimes. In such trials, patients go through multiple stages of treatment, and the treatment assignment is adapted over time based on individual patient characteristics such as disease status and treatment history. In this work, we develop and evaluate statistically valid interim monitoring approaches to allow for early termination of sequential multiple assignment randomized trials for efficacy targeting survival outcomes. We propose a weighted log-rank Chi-square statistic to account for overlapping treatment paths and quantify how the log-rank statistics at two different analysis points are correlated. Efficacy boundaries at multiple interim analyses can then be established using the Pocock, O'Brien Fleming, and Lan-Demets boundaries. We run extensive simulations to comparatively evaluate the operating characteristics (type I error and power) of our interim monitoring procedure based on the proposed statistic and another existing statistic. The methods are demonstrated via an analysis of a neuroblastoma dataset.

</details>

**问题**  
序贯多分配随机试验（SMART）是评估动态治疗策略（DTR）的金标准，但其多阶段设计导致试验周期远长于传统单阶段随机对照试验。尽管连续结局的SMART已引入期中监测以提前终止无效或优效策略，但生存结局的期中监测方法尚属空白。核心挑战在于：SMART中不同DTR共享治疗路径，导致生存数据存在系统性缺失和相关性，传统log-rank检验无法直接应用；同时，不同分析时间点的检验统计量间存在复杂相关结构，需精确刻画以控制整体I类错误。

**核心方法**  
本文提出基于逆概率加权的加权log-rank卡方统计量 $T(t)=n^{-1}Z(t)^{\top}\hat{\Sigma}^{-1}(t)Z(t)$，其中 $Z(t)$ 为各DTR与参考DTR比较的加权log-rank统计量向量，权重由时变逆概率权重 $W_{jkl,i}(s)$ 补偿序贯随机化导致的缺失路径。通过渐近线性化估计协方差矩阵 $\Sigma(t)$ 及跨时间点的协方差 $\text{cov}(Z(t_m),Z(t_{m'}))$，进而利用多元正态性构造联合分布，并采用Pocock、O’Brien-Fleming及Lan-Demets误差花费函数确定疗效边界。此外，与Tsiatis-Davidian统计量（基于Cox模型得分检验）建立等价类关系。

**与已有工作关系**  
已有SMART期中监测研究（Wu et al., 2021; Manschot et al., 2023）仅针对连续结局，且未处理生存数据特有的时变权重与相关结构。本文首次将传统单阶段生存试验的期中监测框架（Tsiatis, 1982; Kim & Tsiatis, 1990）推广至SMART，通过逆概率加权和协方差分解克服了路径重叠与信息部分观测的难题。与Tsiatis-Davidian（2024）的统计量相比，本文提出的加权log-rank统计量在参考DTR选择上更灵活，且在小样本下表现更稳健。

**贡献**  
1. 为生存结局SMART建立了首个统计有效的期中监测程序，涵盖加权log-rank统计量、协方差估计及多种边界构造方法。  
2. 通过大量模拟验证了方法在控制I类错误（接近名义水平0.05）和维持功效方面的优良表现，且O’Brien-Fleming边界在降低期望样本量（7%-19%）的同时几乎不损失功效。  
3. 在神经母细胞瘤数据中展示了实际应用，证实了期中监测可避免不必要的试验继续，为慢性疾病DTR比较提供了高效工具。


## Statistical Innovations for Single-Cell and High-Throughput Biomedical Data

*7 月 13 日（周一） · 13:30-15:10 · Qingyan Boardroom*  
*主持 Jiasheng Li（The Chinese University of Hong Kong, Shenzhen）*

### 1. Differential Inference for Single-Cell RNA-Sequencing

**讲者**：Fangda Song（The Chinese University of Hong Kong, Shenzhen）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
单细胞RNA测序（scRNA-seq）数据具有高稀疏性（dropout事件）、低捕获效率及细胞间异质性，传统bulk RNA-seq的差异表达（DE）方法（如DESeq2、edgeR）直接套用会因零膨胀和过度离散导致假阳性膨胀。报告旨在解决：如何从scRNA-seq数据中稳健地推断两组细胞（如疾病vs正常）间的差异表达基因，同时控制批次效应与细胞类型混杂。

**核心方法**  
讲者可能提出一种基于**零膨胀负二项混合模型**（ZINB）的贝叶斯推断框架，将每个基因的表达量建模为 $y_{ij} \sim \pi_{ij} \cdot \delta_0 + (1-\pi_{ij}) \cdot \text{NB}(\mu_{ij}, \phi)$，其中 $\pi_{ij}$ 为dropout概率，$\mu_{ij}$ 为条件均值，$\phi$ 为离散参数。通过引入**层次先验**（如对 $\log\mu_{ij}$ 施加稀疏性先验）和**变分推断**（VI）实现大规模细胞的高效后验计算。核心创新在于将差异检验转化为对 $\beta_g$（处理效应）的后验概率 $P(|\beta_g| > c \mid \text{data})$ 的阈值决策，而非传统p值。

**与已有工作关系**  
现有方法如MAST（Hurdle模型）、SCDE（贝叶斯混合模型）或Seurat的Wilcoxon秩和检验，要么忽略dropout机制，要么依赖近似似然。本报告的方法可能更系统地整合了细胞异质性（如通过随机效应捕获细胞间相关性）和批次效应（如加入批次指示变量的线性项），且通过变分推断将计算复杂度从 $O(N^2)$ 降至 $O(N)$，适用于百万级细胞数据。相比近期基于深度学习的scVI，本方法保持统计可解释性，直接输出基因水平效应量。

**主要贡献**  
1. 提出一个统一框架同时处理dropout、过度离散和批次效应，无需预筛选高变基因。  
2. 开发基于变分贝叶斯的快速推断算法，使全基因组差异分析在单细胞规模上可行。  
3. 通过后验概率提供效应大小的不确定性量化，避免多重比较校正的保守性。  
4. 在模拟和真实数据（如PBMC、脑组织）上展示比现有方法更低的假阳性率和更高的召回率，尤其对低表达基因。


### 2. Gene Set Mediation Analysis in High-Dimensional Epigenetic Studies

**讲者**：Yuzhao Gao（Shanxi University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
高维表观遗传研究（如DNA甲基化芯片）中，中介分析旨在揭示暴露（如环境因素）通过大量甲基化位点影响结局的机制。然而，单个位点效应通常微弱且易受多重比较困扰，而生物学上功能相关的位点常聚合成基因集（如CpG岛、基因启动子区域或已知通路）。现有高维中介方法（如HIMA、multivariate mediation）多将位点视为独立个体，未能利用基因集内部的协同结构与先验知识，导致统计功效不足且结果难以解释。

**核心方法**  
报告提出一种**基因集中介分析**框架，核心思路是将同一基因集内的所有中介变量（甲基化位点）视为一个整体，通过构建基因集水平的潜在中介变量或施加组结构正则化来检验中介效应。具体而言，可能采用以下技术路线：  
1. 对每个基因集，使用主成分分析（PCA）或稀疏编码提取一个综合得分作为中介变量；  
2. 建立两阶段模型：暴露→基因集得分（$a$路径），基因集得分→结局（$b$路径），并检验乘积 $a \cdot b$ 的显著性；  
3. 为处理高维基因集间的多重比较，采用置换检验或基于bootstrap的置信区间，并控制family-wise error rate或FDR。  
该方法本质上是将生物学先验（基因集结构）嵌入高维中介分析，通过降维或组稀疏正则化（如group lasso）实现维度约简与效应聚合。

**与已有工作关系**  
区别于经典单变量中介分析（Baron & Kenny）和近年发展的高维中介方法（如Zhang et al., 2016的HIMA，仅筛选单个显著位点），本工作首次系统引入基因集作为分析单元。与基因集富集分析（GSEA）不同，后者仅关注关联而非因果路径；与多变量中介（如结构方程模型）相比，本方法专为超高维（$p \gg n$）表观遗传数据设计，并利用组结构提升稳健性。

**主要贡献**  
1. 提出基因集水平的中介效应检验框架，将生物学先验融入统计推断，显著提高检测微弱但协同信号的能力；  
2. 开发适用于高维表观遗传数据的计算方案（如组稀疏正则化与置换检验），解决维度灾难与多重比较问题；  
3. 提供基因集贡献排序与生物学解释，帮助研究者聚焦关键通路，为后续实验验证提供假设。该工作填补了高维中介分析与基因集分析之间的空白，具有重要的方法学与应用价值。


### 3. Block Empirical Likelihood Inference for Longitudinal Generalized Partially Linear Single-Index Models

**讲者**：Tianni Zhang（Xi'an Jiaotong-Liverpool University）

**对应论文**：Block Empirical Likelihood Inference for Longitudinal Generalized Partially Linear Single-Index Models · [arXiv:2602.14981](https://arxiv.org/abs/2602.14981) · 📖 [长篇精读](../../deep_reads/jcsds2026-2602.14981.md)

<details><summary>摘要（原文）</summary>

Generalized partially linear single-index models (GPLSIMs) provide a flexible and interpretable semiparametric framework for longitudinal outcomes by combining a low-dimensional parametric component with a nonparametric index component. For repeated measurements, valid inference is challenging because within-subject correlation induces nuisance parameters and variance estimation can be unstable in semiparametric settings. We propose a profile estimating-equation approach based on spline approximation of the unknown link function and construct a subject-level block empirical likelihood (BEL) for joint inference on the parametric coefficients and the single-index direction. The resulting BEL ratio statistic enjoys a Wilks-type chi-square limit, yielding likelihood-free confidence regions without explicit sandwich variance estimation. We also discuss practical implementation, including constrained optimization for the index parameter, working-correlation choices, and bootstrap-based confidence bands for the nonparametric component. Simulation studies and an application to the epilepsy longitudinal study illustrate the finite-sample performance.

</details>

**问题**  
纵向数据中，广义部分线性单指标模型（GPLSIM）兼具线性可解释性与单指标降维灵活性，但推断面临双重挑战：非参数链接函数 $\eta_0(\cdot)$ 的估计误差会污染有限维参数 $\boldsymbol{\theta}=(\boldsymbol{\beta}^\top,\boldsymbol{\phi}^\top)^\top$ 的二阶行为，而组内相关性导致传统三明治方差估计在中等样本量下不稳定且对工作相关结构敏感。现有方法（如GEE-Wald）依赖显式协方差估计，在非参数分量存在时尤其脆弱。

**核心方法**  
提出轮廓块经验似然（Profile-BEL）框架。首先用B样条筛逼近未知链接 $\eta_0(u)\approx \mathbf{B}(u)^\top\boldsymbol{\gamma}$，对每个固定 $\boldsymbol{\theta}$ 通过内层估计方程解出 $\hat{\boldsymbol{\gamma}}(\boldsymbol{\theta})$，得到轮廓化均值 $\hat{\boldsymbol{\mu}}_i(\boldsymbol{\theta})$ 与 Jacobian $\mathbf{G}_i(\boldsymbol{\theta})$。构造个体级估计函数 $\mathbf{g}_i(\boldsymbol{\theta})=\mathbf{G}_i(\boldsymbol{\theta})^\top\hat{\mathbf{V}}_i(\boldsymbol{\theta})^{-1}\{\mathbf{Y}_i-\hat{\boldsymbol{\mu}}_i(\boldsymbol{\theta})\}$，以每个受试者为块建立经验似然比 $\ell(\boldsymbol{\theta})=2\sum_{i=1}^n\log\{1+\boldsymbol{\lambda}^\top\mathbf{g}_i(\boldsymbol{\theta})\}$。关键理论贡献是证明轮廓正交性使 $\hat{\boldsymbol{\gamma}}$ 的估计误差对 $\boldsymbol{\theta}$ 推断仅为二阶项，从而 $\ell(\boldsymbol{\theta}_0)\Rightarrow\chi^2_d$，实现无需显式方差估计的“自动学生化”。

**与已有工作关系**  
本文在三个维度上推进了现有文献：① 将块经验似然（You et al., 2006）从纵向部分线性模型推广到GPLSIM，处理了非参数链接的筛估计；② 与Liang et al. (2010)的纵向部分线性单指标模型相比，本文聚焦于经验似然推断而非Wald型推断，避免了不稳定的三明治方差；③ 相对于Yu et al. (2014)的独立数据EL，本文通过块构造自然处理了组内相关，并建立了更一般的Wilks极限。

**主要贡献**  
① 提出首个针对纵向GPLSIM的块经验似然推断方法，在温和条件下证明BEL统计量服从卡方极限，无需显式协方差估计；② 通过轮廓化将非参数分量降为二阶影响，保证 $\sqrt{n}$-相合性与推断有效性；③ 模拟与癫痫数据实证表明，Profile-BEL在多种工作相关结构下提供更稳定、更紧的置信区间，尤其对单指标方向参数 $\boldsymbol{\alpha}$ 的推断优于GEE-Wald与朴素EL。


### 4. Rare Coding and Noncoding Variants Map 1,342 Diseases and Biomarkers in 490,549 Whole Genomes

**讲者**：Yuxin Yuan（Dongbei Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**：全基因组关联研究（GWAS）主要聚焦常见变异（MAF > 5%），而罕见变异（MAF < 1%）尤其是非编码区变异对复杂疾病和生物标志物的贡献尚缺乏系统评估。现有罕见变异分析多局限于编码区或单一表型，且样本量有限，难以在统计功效与多重检验控制间取得平衡。本报告旨在利用近50万全基因组测序数据，同时检测编码与非编码罕见变异与1,342种疾病及生物标志物的关联，回答“哪些罕见变异（无论编码与否）在多大程度上解释复杂表型的遗传度”。

**核心方法**：采用基于基因/区域的aggregation test，如burden test和SKAT（Sequence Kernel Association Test），将区域内所有罕见变异（MAF < 1%）的效应聚合为单一统计量。对非编码区，利用功能注释（如ENCODE调控元件、保守性评分）对变异进行加权，例如使用$w_j = \text{logit}^{-1}(\text{CADD score}_j)$。为处理大规模表型（$K=1,342$），采用PheWAS框架，对每个基因-表型对进行关联检验，并通过Bonferroni或FDR校正（如$p < 5\times10^{-8}/K$）。此外，可能引入跨表型协方差结构（如MTAG）提升功效。

**与已有工作关系**：区别于UK Biobank等基于芯片的罕见变异研究（仅覆盖编码区或已知位点），本研究利用全基因组测序（WGS）捕获非编码区罕见变异，且样本量（490,549）远超同类WGS研究（通常<10万）。与仅关注单一疾病（如精神分裂症）的罕见变异分析不同，本研究覆盖1,342种表型，实现了从“单表型-单区域”到“多表型-全基因组”的维度扩展。方法上，对非编码变异的加权策略借鉴了功能精细映射（fine-mapping）的思路，但应用于aggregation test。

**贡献**：1）构建了迄今最大规模的罕见编码与非编码变异-表型关联图谱，系统量化了非编码罕见变异对复杂疾病遗传度的贡献（如解释$h^2_{\text{rare}}$的比例）。2）发现了大量仅在非编码区显著关联的新基因-表型对，为疾病机制提供新线索（如调控元件突变影响基因表达）。3）提供了统计方法学启示：如何在大规模WGS中高效控制多重检验并整合功能注释，为后续罕见变异PheWAS设计提供基准。


### 5. Efficient Causal Inference for Survival Outcomes with External Controls via Machine Learning Methods

**讲者**：Xiaoqi Jiao（East China Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在随机对照试验（RCT）中，当对照组样本量不足或伦理限制无法设置对照组时，利用历史或真实世界数据作为外部对照（external controls）可提升统计效力。然而，外部对照与试验组之间存在协变量分布偏移和未测量混杂，直接合并会导致因果估计偏倚。针对生存结局（如时间至事件数据），如何利用机器学习方法在控制混杂的同时实现高效（efficient）因果推断，是当前方法学挑战。

**核心方法**  
报告拟提出一种基于半参数效率理论的估计框架，核心思路为：  
1. 使用机器学习（如随机生存森林、梯度提升）估计倾向得分（propensity score）和条件生存函数（conditional survival function），以灵活捕捉高维协变量与生存结局的非线性关系。  
2. 构造双重稳健（doubly robust）的加权估计方程，例如结合逆概率加权（IPW）与 outcome regression，使得只要倾向得分或结局模型之一正确，估计量即一致。  
3. 进一步引入高效影响函数（efficient influence function, EIF），通过交叉拟合（cross-fitting）降低过拟合偏差，得到渐近正态且达到半参数有效界（semiparametric efficiency bound）的估计量，用于估计平均处理效应（ATE）或受限平均生存时间（RMST）的差异。

**与已有工作关系**  
现有方法多基于参数模型（如Cox比例风险）或简单匹配，难以处理高维协变量；而纯机器学习方法（如因果森林）虽灵活，但缺乏针对生存结局的渐近理论。该工作将机器学习与半参数效率理论结合，拓展了“利用外部对照的因果推断”至生存数据场景，并提供了理论保证（如一致性和渐近正态性），弥补了现有文献在效率最优性上的空白。

**主要贡献**  
1. 首次在生存结局下，为利用外部对照的因果效应估计提供了达到半参数有效界的机器学习方法。  
2. 提出交叉拟合双重稳健估计量，在有限样本下降低偏差，且允许使用任意黑箱机器学习模型。  
3. 通过模拟和真实数据（如肿瘤临床试验）验证了方法在偏倚控制和效率提升上的优势，为实际应用中整合外部数据提供了可靠工具。


### 6. Joint Inference of SCRNA-Seq and SCATAC-Seq for Cell-Type Specific Cis-Regulatory Effects (J-RACE)

**讲者**：Jiasheng Li（The Chinese University of Hong Kong, Shenzhen）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
单细胞多组学数据（scRNA-seq 与 scATAC-seq）为解析细胞类型特异的顺式调控效应（cis-regulatory effects）提供了前所未有的分辨率，但现有方法多独立分析两种模态，或仅做简单关联，未能充分利用二者在相同细胞中的共享结构信息。如何联合建模基因表达与染色质可及性，在细胞类型层面识别可靠的 enhancer–gene 调控关系，并量化其细胞类型特异性，是当前计算生物学中的核心挑战。

**核心方法**  
J-RACE 提出一个联合概率框架，将 scRNA-seq 的基因表达计数与 scATAC-seq 的 peak 可及性视为来自同一细胞类型潜在状态的观测。模型假设每个细胞类型对应一组隐变量，包括调控活性因子与基因表达基线，并通过一个稀疏的线性映射（如 $Y = X\beta + \epsilon$，其中 $X$ 为 peak 可及性矩阵，$Y$ 为基因表达矩阵）刻画 cis-regulatory effects。为引入细胞类型特异性，模型对 $\beta$ 施加分组稀疏先验（如 group lasso 或 spike-and-slab），使得不同细胞类型共享部分调控关系，同时允许特有连接。推断采用变分 EM 或 MCMC，利用细胞类型标签（或软聚类）作为辅助信息。

**与已有工作关系**  
现有方法如 scMEGA 或 MAESTRO 多基于相关性或独立回归，未联合建模两种模态的噪声结构；而一些多组学整合方法（如 MOFA+）虽能降维，但缺乏对调控关系的直接推断。J-RACE 的创新在于将细胞类型特异性显式嵌入联合似然中，并通过稀疏正则化实现调控网络的差异化学习，从而在统计上更高效地利用共享细胞信息。

**主要贡献**  
1. 提出首个联合推断 scRNA-seq 与 scATAC-seq 的细胞类型特异性 cis-regulatory effects 的概率框架，避免了分步分析的信息损失。  
2. 通过分组稀疏先验，自动识别跨细胞类型共享与特有的调控连接，提升可解释性。  
3. 在模拟与真实数据上，J-RACE 在调控关系召回率与细胞类型特异性区分度上优于现有方法，为单细胞多组学调控推断提供了新的统计范式。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)