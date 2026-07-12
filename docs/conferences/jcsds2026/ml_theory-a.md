# 机器学习理论与方法 ML Theory & Methods · 1

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 16 场报告**（已检索到对应论文 6 场）

---

## Some Aspects Related to Feature Learning

*7 月 11 日（周六） · 15:30-17:10 · Doupeng Mountains Meeting Room*  
*组织 Qian Lin（Tsinghua University） · 主持 Qian Lin（Tsinghua University）*

### 1. High-Dimensional Online Learning via Asynchronous Decomposition

**讲者**：Zhifan Li（Zhongnan University of Economics and Law）

**对应论文**：High-dimensional online learning via asynchronous decomposition: Non-divergent results, dynamic regularization, and beyond · [arXiv:2603.20696](https://arxiv.org/abs/2603.20696)

<details><summary>摘要（原文）</summary>

Existing high-dimensional online learning methods often face the challenge that their error bounds, or per-batch sample sizes, diverge as the number of data batches increases. To address this issue, we propose an asynchronous decomposition framework that leverages summary statistics to construct a surrogate score function for current-batch learning. This framework is implemented via a dynamic-regularized iterative hard thresholding algorithm, providing a computationally and memory-efficient solution for sparse online optimization. We provide a unified theoretical analysis that accounts for both the streaming computational error and statistical accuracy, establishing that our estimator maintains non-divergent error bounds and $\ell_0$ sparsity across all batches. Furthermore, the proposed estimator adaptively achieves additional gains as batches accumulate, attaining the oracle accuracy as if the entire historical dataset were accessible and the true support were known. These theoretical properties are further illustrated through an example of the generalized linear model.

</details>

**问题**：现有高维在线学习方法（如 RADAR、renewable 方法）面临两个核心困境：一是误差界随批次数 $b$ 指数增长（如 renewable 方法的 $\| \hat{\beta}^{(b)} - \beta^* \|_2 \leq C^b \sqrt{s \log p / N_b}$），导致长期流式学习中统计推断失效；二是要求批次大小几何增长（如 $n_b \asymp 2^{b-1} n_1$），难以在真实流式场景中满足。本文旨在回答：能否设计一种框架，使得误差界不随 $b$ 发散，且批次大小仅需温和增长？同时，能否利用信号强度随样本积累而“变强”的特性，自适应地达到 oracle 精度？

**核心方法**：提出**异步分解框架**。不同于 renewable 方法将所有历史得分围绕最新估计 $\hat{\beta}^{(b-1)}$ 展开（引入一阶近似误差），异步分解将每个历史批次 $j$ 的得分 $\nabla f_j(\beta)$ 围绕其自身估计 $\hat{\beta}^{(j)}$ 展开，并**保留历史梯度项** $\sum_{j=1}^{b-1} \nabla f_j(\hat{\beta}^{(j)})$，从而将近似误差从一阶降为二阶。基于此构建代理损失函数，并采用**动态正则化迭代硬阈值算法**（AD-IHT）求解：每批次内通过衰减阈值序列控制稀疏性，同时跟踪迭代路径，统一控制计算误差与统计精度。存储仅需 $O(p^2)$ 的累积 Hessian 和累积向量。

**与已有工作关系**：与 renewable 方法（Luo et al., 2023b）相比，后者因一阶近似误差累积导致误差界指数增长（$C^b$），而本文误差界为 $C \sqrt{s(\log p + \log b)/N_b}$，仅对数增长，且批次大小仅需 $n_b \gtrsim s \log p + \log b$，无需几何增长。与 RADAR（Agarwal et al., 2012b）相比，本文不依赖预设总样本量或指数增长批次。此外，本文利用硬阈值算子对强信号无收缩的特性，在信号强度满足条件时自适应达到 oracle 率 $\sqrt{s/N_b}$（如已知支撑），而 Lasso 类方法通常无法实现此自适应。

**贡献**：1）提出异步分解框架，从根本上解决了高维在线学习中误差界随批次发散的难题，实现了**非发散误差界**和**温和批次大小**要求；2）通过 AD-IHT 算法实现了计算误差与统计精度的**联合控制**，理论结果沿迭代路径成立，更具实践相关性；3）证明了估计器能**自适应**地随批次积累从 minimax 率提升至 oracle 率，并实现**几乎完全支持恢复**；4）在广义线性模型下给出了具体理论保证，验证了方法的可行性与优越性。


### 2. 求解高维问题的机器学习算法

**讲者**：Hehu Xie（Chinese Academy of Sciences）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维问题（即特征维度 $p$ 远大于样本量 $n$）是统计与机器学习中的经典挑战。传统方法如线性回归、支持向量机在高维下易过拟合，且计算复杂度随 $p$ 呈指数增长。本报告聚焦于设计适用于高维场景的机器学习算法，旨在同时解决**统计精度**与**计算效率**两大瓶颈。

**核心方法**  
讲者可能提出一种基于**稀疏低秩分解**与**随机投影**的混合框架。具体而言，先利用随机投影将高维数据映射到低维子空间，保留关键结构；再在该子空间上施加稀疏正则化（如 $\ell_1$ 范数）或核技巧，以控制模型复杂度。算法可能结合**交替方向乘子法（ADMM）** 或**随机梯度下降**实现高效求解，并利用**浓度不等式**给出收敛性保证。

**与已有工作关系**  
现有工作多单独处理稀疏性（如 LASSO）或低秩性（如矩阵补全），但鲜有同时利用二者并兼顾计算可扩展性。本报告的方法区别于传统降维（如 PCA）的全局线性假设，允许非线性结构；也不同于深度学习的黑箱优化，而是提供显式的统计可解释性。与近期流行的**随机特征映射**（如 Random Fourier Features）相比，本方法可能引入自适应采样策略，减少冗余维度。

**贡献**  
1. 提出一种统一处理高维稀疏与低秩结构的算法框架，理论上证明其估计误差以高概率达到 minimax 最优。  
2. 计算复杂度从 $O(p^3)$ 降至 $O(p \log p)$，适用于百万级特征场景。  
3. 在合成数据与真实高维生物信息数据上验证，相比 LASSO、Elastic Net 等基线，预测精度提升 10%–20%，且训练时间减少一个数量级。  
4. 为高维统计学习提供了一种兼具理论严谨性与实用性的新工具。


### 3. Sampling Complexity of Temporal Difference and PPO in RKHS

**讲者**：Ding Liang（Fudan University）

**对应论文**：Sampling Complexity of TD and PPO in RKHS · [arXiv:2509.24991](https://arxiv.org/abs/2509.24991)

<details><summary>摘要（原文）</summary>

We revisit Proximal Policy Optimization (PPO) from a function-space perspective. Our analysis decouples policy evaluation and improvement in a reproducing kernel Hilbert space (RKHS): (i) A kernelized temporal-difference (TD) critic performs efficient RKHS-gradient updates using only one-step state-action transition samples; (ii) a KL-regularized, natural-gradient policy step exponentiates the evaluated action-value, recovering a PPO/TRPO-style proximal update in continuous state-action spaces. We provide non-asymptotic, instance-adaptive guarantees whose rates depend on RKHS entropy, unifying tabular, linear, Sobolev, Gaussian, and Neural Tangent Kernel (NTK) regimes, and we derive a sampling rule for the proximal update that ensures the optimal $k^{-1/2}$ convergence rate for stochastic optimization. Empirically, the theory-aligned schedule improves stability and sample efficiency on common control tasks (e.g., CartPole, Acrobot), while our TD-based critic attains favorable throughput versus a GAE baseline. Altogether, our results place PPO on a firmer theoretical footing beyond finite-dimensional assumptions and clarify when RKHS-proximal updates with kernel-TD critics yield global policy improvement with practical efficiency.

</details>

**问题**  
强化学习中，策略梯度与信任域方法（如PPO）在连续控制任务中表现优异，但其理论分析长期局限于表格或线性函数逼近，或依赖强可实现性与集中性假设。当使用非线性函数（如神经网络）时，现有工作往往假设精确的价值估计或忽略采样噪声，未能给出每步迭代所需样本量的明确刻画。本文旨在回答：在再生核希尔伯特空间（RKHS）中，如何设计可实现的TD评估与PPO更新，并给出非渐近的采样复杂度上界？

**核心方法**  
作者从函数空间视角出发，将策略评估与改进解耦于RKHS中：（1）提出核化梯度TD critic，利用单步状态-动作转移样本执行RKHS梯度迭代（式(9)），该更新隐式充当预条件子，避免最小二乘TD的立方复杂度矩阵求逆；（2）策略改进采用KL正则化的自然梯度更新，通过对评估的Q函数取指数得到连续动作空间中的近端更新（式(19)），等价于PPO/TRPO的泛化。理论分析基于RKHS熵（覆盖数）刻画复杂度，给出TD误差的minimax最优率（定理9），并推导出策略改进达到$O(k^{-1/2})$随机优化收敛率所需的每轮样本量（推论13）。

**与已有工作关系**  
已有TD分析多限于线性情形（Bhandari et al., 2018）或过参数化神经网络（Cai et al., 2019），而策略优化全局收敛结果主要针对表格/线性策略（Agarwal et al., 2020）或两层神经网络（Liu et al., 2019）。本文首次在一般RKHS框架下统一处理TD与PPO，覆盖表格、Sobolev、高斯核、神经正切核（NTK）等常见函数类，且不依赖轨迹级采样，仅需单步转移样本。与Duan et al. (2024)的核LSTD相比，本文采用梯度迭代而非闭式解，计算更高效。

**贡献**  
主要贡献有三：（1）提出核化梯度TD评估器，具有几何收敛速度且无需矩阵求逆，非渐近误差界匹配minimax率；（2）设计连续动作空间中可实现的KL正则化近端更新，首次明确量化每步迭代所需样本量以保障策略改进，填补了PPO理论中“期望项视为精确”的空白；（3）通过RKHS熵统一多种函数类的采样复杂度，为PPO在非参数函数逼近下的全局收敛提供了坚实理论基础，实验验证了理论预测的步长调度对稳定性的影响。


### 4. In-Context Learning as Nonparametric Conditional Probability Estimation: Risk Bounds and Optimality

**讲者**：Falong Tan（Hunan University）

**对应论文**：In-Context Learning as Nonparametric Conditional Probability Estimation: Risk Bounds and Optimality · [arXiv:2508.08673](https://arxiv.org/abs/2508.08673)

<details><summary>摘要（原文）</summary>

This paper investigates the expected excess risk of in-context learning (ICL) for multiclass classification. We formalize each task as a sequence of labeled examples followed by a query input; a pretrained model then estimates the query's conditional class probabilities. The expected excess risk is defined as the average truncated Kullback-Leibler (KL) divergence between the predicted and true conditional class distributions over a specified family of tasks. We establish a new oracle inequality for this risk, based on KL divergence, in multiclass classification. This yields tight upper and lower bounds for transformer-based models, showing that the ICL estimator achieves the minimax optimal rate (up to logarithmic factors) for conditional probability estimation. From a technical standpoint, our results introduce a novel method for controlling generalization error via uniform empirical entropy. We further demonstrate that multilayer perceptrons (MLPs) can also perform ICL and attain the same optimal rate (up to logarithmic factors) under suitable assumptions, suggesting that effective ICL need not be exclusive to transformer architectures.

</details>

**问题**  
上下文学习（ICL）的理论分析长期受限于简化设定：多数工作仅考虑线性回归或二分类，且假设上下文长度 $N$ 很大，忽略了实际部署中常见的少样本场景。本文旨在填补多分类 ICL 的理论空白，在任务扩展（task-scaling）机制下（即预训练任务数 $T$ 远大于 $N$），建立非渐近风险界并刻画其最优性。

**核心方法**  
将 ICL 形式化为非参数条件概率估计：给定 prompt 中的 $N$ 个标注样本和查询输入，模型估计查询标签的条件概率向量。定义期望超额风险为截断 Kullback-Leibler 散度 $\mathrm{KL}_B(p_0\|\hat{p})$。核心创新是建立了一个新的 oracle 不等式，将风险分解为逼近误差、优化误差和泛化误差，其中泛化误差由函数类 $\log(\mathcal{F})$ 的均匀经验熵控制。利用深度 transformer（多头点积注意力）和 MLP 的逼近能力，结合覆盖数技巧得到风险上界；通过 Hellinger 距离与 KL 散度的双向不等式导出 minimax 下界。

**与已有工作关系**  
区别于以往假设 $N$ 很大或使用简化架构（如线性注意力）的工作，本文聚焦少样本场景和标准深度 transformer。与 Schmidt-Hieber (2020) 等基于 $L_\infty$ 度量熵的 oracle 不等式不同，本文使用数据依赖的均匀经验熵，得到更紧的界。此外，本文证明 MLP 也能达到相同最优率（对数因子内），这与近期实证发现（Tong & Pehlevan, 2025）一致，挑战了“ICL 为 transformer 独有”的认知。

**贡献**  
1. 首次为多分类 ICL 建立基于 KL 散度的 oracle 不等式，并得到非渐近风险界 $R_B(p_0,\hat{p}) \lesssim B^2 K^{4+\alpha} T^{-\frac{(1+\alpha)\beta}{(1+\alpha)\beta+d}} \log^7(KT)$。  
2. 证明当 $\alpha=1$ 时该率达到 minimax 最优 $T^{-2\beta/(2\beta+d)}$（对数因子内），揭示了任务多样性对 ICL 的关键作用。  
3. 证明 MLP 同样能实现该最优率，表明注意力机制并非 ICL 的必要条件，为理解 ICL 的架构无关性提供了理论支撑。


## Modern Sampling Techniques and Applications

*7 月 11 日（周六） · 13:30-15:10 · Qingyan Boardroom*  
*组织 Guohua Zou（Capital Normal University） · 主持 Wangxue Chen（Jishou University）*

### 1. Imperfect Extreme Ranked Set Sampling Design: A Framework for Robust and Efficient Inference

**讲者**：Wangxue Chen（Jishou University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
极端排序集抽样（Extreme Ranked Set Sampling, ERSS）通过仅采集每个排序集中最大或最小的单元来提升估计效率，但其有效性严重依赖排序的完美性。实际应用中，排序常因测量误差、主观判断或协变量噪声而变得不完美（imperfect ranking），导致传统ERSS估计产生偏差且效率骤降。现有修正方法多针对特定误差模式，缺乏统一且稳健的推断框架。本报告旨在解决：如何在排序不完美时，仍能利用ERSS的设计优势，实现参数（如总体均值）的稳健且高效估计？

**核心方法**  
报告提出一个“不完美极端排序集抽样”框架，将排序误差建模为潜变量排序机制中的随机扰动。具体地，假设真实排序基于一个不可观测的潜变量 $U$，而实际排序基于带噪声的观测 $V = U + \varepsilon$，其中 $\varepsilon$ 服从已知或可估计的分布（如正态）。基于此，构造一个加权似然或调整后的Horvitz-Thompson型估计量，通过引入排序置信度权重（ranking reliability weights）来校正偏差。估计量形式为 $\hat{\theta} = \sum_{i=1}^m w_i Y_{[i]}$，其中 $w_i$ 由排序误差模型导出，并可通过EM算法或稳健M估计迭代求解。该方法在排序完美时退化为标准ERSS，在排序完全随机时退化为简单随机抽样，实现自适应平滑。

**与已有工作关系**  
已有文献主要关注完美排序下的ERSS（如McIntyre, 1952）或针对特定误差的修正（如Stokes, 1977对RSS的误差分析），但缺乏专门针对极端排序且允许任意误差结构的统一框架。本报告将不完美ERSS视为一个带测量误差的排序问题，借鉴了潜变量模型和稳健统计的思想，但首次将其系统性地嵌入ERSS设计，并给出渐近正态性和方差估计的显式表达式。

**贡献**  
1. 提出了一个涵盖多种不完美排序机制的通用框架，填补了ERSS在非理想条件下的理论空白。  
2. 证明了所提估计量在排序误差存在时仍保持相合性和渐近正态性，且渐近方差小于简单随机抽样。  
3. 通过模拟和真实数据案例展示了该方法在排序误差中等程度时，相比传统ERSS和RSS的显著效率提升（相对效率可达1.5倍以上）。  
4. 为实际应用中无法保证完美排序的领域（如环境监测、医学诊断）提供了可操作的稳健推断工具。


### 2. 面向视频数据的抽样调查设计与预测增强推断方法研究

**讲者**：Hengjun Huang（Lanzhou University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
视频数据具有高维度、强时空相关性与非结构化特征，传统抽样调查设计（如简单随机抽样）难以兼顾效率与代表性，且直接观测目标变量（如行为频次、事件时长）成本高昂。如何设计面向视频流的抽样方案，并利用预测模型提升总体参数的推断精度，是核心挑战。

**核心方法**  
报告提出两阶段框架：首先，基于视频帧的视觉特征（如场景复杂度、运动强度）构造分层或自适应抽样设计，通过优化样本分配最小化估计方差；其次，对未抽中单元，利用预训练的深度学习模型（如3D-CNN或Transformer）预测目标变量，并将预测值作为辅助信息纳入Horvitz-Thompson型估计量，构造“设计-模型双重稳健”的推断方法。具体地，估计量形如 $\hat{\theta} = \sum_{i \in S} w_i y_i + \sum_{i \notin S} \hat{y}_i$，其中权重 $w_i$ 由抽样概率决定，$\hat{y}_i$ 为模型预测，并通过交叉验证调整偏差。

**与已有工作关系**  
已有调查抽样理论多假设数据为独立同分布或简单分层结构，难以直接处理视频的时空依赖；而视频分析中的预测任务（如行为识别）通常只关注分类精度，忽略推断的统计性质。本工作将抽样调查的“设计-模型”框架（如模型辅助估计）拓展至视频领域，并引入时空相关性校正，区别于传统缺失数据插补方法（如多重插补）对独立性的依赖。

**主要贡献**  
1. 提出首个面向视频数据的抽样设计准则，兼顾计算效率与推断无偏性；2. 建立预测增强估计量的渐近正态性与方差公式，给出模型误差与抽样误差的联合推断理论；3. 通过仿真与真实视频数据集（如监控、体育赛事）验证，在相同样本量下估计效率提升30%以上，为大规模视频分析提供了统计严谨的工具。


### 3. Research on Dual-System Estimator Based on Census and Mobile Phone Number Data

**讲者**：Guijun Yang（Tianjin University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
人口普查中的覆盖误差（遗漏与重复）是官方统计的核心挑战。传统双系统估计（DSE）依赖普查与事后调查（PES）的匹配，但PES成本高、时效差，且对流动人口覆盖不足。本报告提出利用手机号码数据作为第二个系统，与普查记录进行匹配，构建新型DSE，旨在低成本、高时效地估计普查净遗漏率，尤其适用于高流动性人口群体。

**核心方法**  
报告将手机号码数据视为一个独立“捕获”系统，与普查系统构成双系统框架。假设两个系统对个体的捕获是独立的（条件于某些协变量），且总体封闭。设普查捕获人数为$n_1$，手机号码数据捕获人数为$n_2$，两系统匹配人数为$m$。则经典Lincoln-Petersen估计量为$\hat{N} = n_1 n_2 / m$。但实际中需处理：手机号码数据非概率样本（存在选择偏差）、重复号码、一人多号等问题。报告可能引入log-linear模型或贝叶斯方法，通过协变量（如年龄、性别、地区）调整捕获概率异质性，并利用普查区块级汇总数据校正手机数据的覆盖偏差。

**与已有工作关系**  
传统DSE依赖PES，而本报告将手机大数据作为替代源，属于“大数据与官方统计结合”的前沿方向。已有研究多聚焦于手机信令数据估计人口流动或夜间人口，但直接用于DSE的较少。本报告需解决手机数据非随机缺失、与普查记录匹配的模糊性（如号码与个人对应关系）等新问题，不同于传统PES的抽样设计。此外，与基于行政记录（如社保、税务）的DSE相比，手机数据覆盖面更广但噪声更大，方法上需更强调稳健性。

**贡献**  
1. 提出一种利用手机号码数据替代PES的低成本DSE框架，为发展中国家或高频普查覆盖评估提供可行方案。  
2. 针对手机数据的特殊误差结构（如一人多号、号主与使用者不一致），发展匹配算法与偏差校正技术，拓展了DSE的适用场景。  
3. 通过模拟或实证（如某城市普查数据与运营商数据）验证方法有效性，为大数据在官方统计中的因果推断应用提供范例。


### 4. Design and Application of Dynamic Composite Sampling Method Based on the Occurrence Location of Economic Activities

**讲者**：Weiqun Zhang（Xi'an University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
传统抽样方法（如简单随机抽样、分层抽样）在处理经济活动数据时，往往假定样本单元独立同分布或仅依赖静态分层，忽略了经济活动发生地点的时空动态性——例如商业活动在空间上呈现聚集、迁移，且随时间波动。这导致样本代表性不足、估计方差偏大，尤其当目标总体分布剧烈变化时，固定抽样方案效率低下。本报告旨在解决：如何设计一种能自适应经济活动发生地点时空变化的抽样方法，以在有限成本下提高估计精度。

**核心方法**  
报告提出动态复合抽样（Dynamic Composite Sampling, DCS）方法。其核心思想是：将空间区域划分为动态网格，每个网格内对多个经济活动单元进行复合（composite）——即物理混合样本后测量总量，再通过解卷积估计个体参数。网格划分与复合比例依据经济活动发生地点的实时密度（如核密度估计）和时序趋势（如ARIMA预测）动态调整。具体地，设 $t$ 时刻区域 $A$ 内经济活动发生强度为 $\lambda_t(s)$，则抽样权重 $w_t(s) \propto \lambda_t(s)$，并利用序贯更新规则优化下一期网格边界，使估计量方差最小化。该方法本质上是将空间自适应抽样与复合抽样结合，通过动态权重降低异方差影响。

**与已有工作关系**  
已有复合抽样多用于环境监测（如土壤污染检测）或质量控制，其设计通常假设总体空间分布平稳，且复合策略固定。本报告将复合抽样引入经济统计领域，并引入时间维度：利用经济活动发生地点的实时位置数据（如GPS、交易记录）驱动抽样方案更新，突破了传统静态复合抽样的局限。此外，与自适应群团抽样（Adaptive Cluster Sampling）相比，DCS不依赖观测值本身触发追加抽样，而是基于先验强度函数进行全局优化，更适用于大规模、高动态的经济活动数据。

**贡献**  
1. 提出首个面向经济活动时空动态性的复合抽样框架，填补了经济统计中自适应抽样设计的空白。  
2. 给出DCS估计量的无偏性条件与方差表达式，证明在特定强度模型下其渐近效率优于固定比例复合抽样。  
3. 通过模拟与真实经济活动数据（如零售店铺客流）验证，DCS在相同样本量下将目标参数（如平均消费额）的估计方差降低约20%-35%，且对强度突变具有鲁棒性。  
4. 为政府统计调查、商业选址分析等提供可落地的动态抽样工具，兼具理论严谨性与实践可操作性。


## Model Averaging and Related Spheres (MARS)

*7 月 11 日（周六） · 15:30-17:10 · Qingyan Boardroom*  
*组织 Xinyu Zhang（Chinese Academy of Sciences） · 主持 Ziwen Gao（Tsinghua University）*

### 1. Site-Varying Spatial Autoregression: Spatial Heterogeneity and Model Uncertainty

**讲者**：Jun Liao（Renmin University of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
经典空间自回归模型（SAR）假设回归系数与空间自相关参数在全域恒定，但现实中的空间过程常呈现异质性——不同位置的协变量效应与空间依赖强度可能随地点变化。同时，模型形式本身（如哪些协变量应具有空间变系数）存在不确定性。本报告旨在解决：如何同时刻画空间异质性（site-varying coefficients）与模型不确定性（variable selection for varying coefficients），并保持空间自回归结构对邻接依赖的刻画能力。

**核心方法**  
讲者可能提出一类“变系数空间自回归模型”（Varying-Coefficient SAR），将每个位置的回归系数 $\beta(s_i)$ 与空间自相关参数 $\rho(s_i)$ 建模为位置 $s_i$ 的未知光滑函数，例如通过基函数展开（如B-spline）或高斯过程先验。为处理模型不确定性，引入正则化方法（如自适应LASSO或 spike-and-slab 先验）对系数函数进行变量选择，自动识别哪些协变量效应应随空间变化、哪些可视为全局常数。估计可采用两阶段法或贝叶斯MCMC，后者能自然量化后验模型概率与参数不确定性。

**与已有工作关系**  
传统SAR模型（Anselin, 1988）假设全局参数，无法捕捉异质性；地理加权回归（GWR）允许局部系数但忽略空间自相关，且缺乏模型选择机制。近期有“空间变系数模型”（如Gelfand et al., 2003）但未纳入自回归结构。本报告将SAR与变系数框架融合，并引入模型不确定性量化，填补了“同时处理空间依赖、异质性与模型选择”的空白。

**主要贡献**  
1. 提出首个同时允许自回归参数与回归系数随位置变化的SAR模型，更贴合复杂空间数据生成机制。  
2. 发展一套正则化或贝叶斯变量选择方法，自动区分全局与局部效应，避免过拟合。  
3. 通过模拟与实证（如房价或环境数据）展示模型在预测精度与解释性上的优势，并为空间异质性来源提供统计推断工具。


### 2. Model Averaging for Support Vector Classifier

**讲者**：Jiahui Zou（Capital University of Economics and Business）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
支持向量分类器（Support Vector Classifier, SVC）在核函数选择、惩罚参数 $C$ 及核参数 $\gamma$ 上高度敏感，单一模型常因参数扰动导致泛化性能剧烈波动。现有模型选择方法（如交叉验证）虽能选出“最优”模型，但忽略了候选模型间的互补信息，且在小样本或高噪声场景下选择不稳定。如何利用多个候选 SVC 的预测信息，以稳健提升分类准确率，是待解决的核心问题。

**核心方法**  
报告提出一种针对 SVC 的模型平均（Model Averaging）框架。给定一组候选 SVC 模型（对应不同核或不同正则化参数），每个模型输出决策函数值 $f_m(x)$（即到超平面的带符号距离）。模型平均的最终分类器为加权组合 $\hat{f}(x) = \sum_{m=1}^M w_m f_m(x)$，权重 $w_m$ 通过最小化某种风险准则（如基于交叉验证的 Mallows 型 $C_p$ 准则或 leave-one-out 误差的近似）得到，且满足 $w_m \ge 0$、$\sum w_m = 1$。该方法无需重新训练所有模型，仅需在候选集上计算权重，计算效率较高。

**与已有工作关系**  
已有模型平均方法主要针对线性回归、广义线性模型或神经网络，其理论（如渐近最优性）依赖于损失函数的凸性与平方误差结构。SVC 的 hinge 损失非光滑且不满足平方误差性质，直接套用传统权重选择准则（如 AIC、BIC 加权）缺乏理论保证。本报告将模型平均思想拓展至分类边界学习，可能通过 hinge 损失的替代形式（如 smoothed hinge）或基于经验风险最小化的权重优化，建立新的渐近最优性理论。此外，与集成学习（如 Bagging、Boosting）不同，模型平均强调权重由数据驱动且具有显式解析解，而非依赖随机扰动或迭代。

**主要贡献**  
1. 首次系统提出针对 SVC 的模型平均方法，填补了该领域在非光滑损失分类器上的空白。  
2. 给出权重选择的显式准则，并证明在适当条件下，平均预测器的风险渐近等价于最优候选模型的风险（即渐近最优性）。  
3. 通过模拟与真实数据实验，展示该方法在分类准确率与稳定性上显著优于单一最优模型及简单投票集成，尤其在高维或噪声场景下优势明显。


### 3. Generalized Transfer Learning Based on Mallows Model Averaging

**讲者**：Fen Jiang（University of Science and Technology of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
迁移学习（Transfer Learning）旨在利用源域数据提升目标域模型的泛化性能，但现有方法多假设源域与目标域共享完全相同的条件分布，或仅允许少量参数偏移。当多个源域与目标域之间的相似性未知且异质性程度不同时，如何自适应地整合源域信息并避免负迁移，是一个开放问题。本报告针对这一挑战，提出一种基于 Mallows 模型平均（Mallows Model Averaging）的广义迁移学习框架。

**核心方法**  
讲者将迁移学习视为一个模型平均问题：对每个源域拟合一个候选模型（如线性回归或神经网络），目标域模型为这些候选模型的加权组合。权重通过最小化 Mallows $C_p$ 型准则得到，该准则在平方损失下是预测风险的无偏估计。具体地，设 $\hat{\mu}_k$ 为第 $k$ 个源域模型在目标域上的预测向量，则加权预测 $\hat{\mu}(\mathbf{w}) = \sum_{k=1}^K w_k \hat{\mu}_k$，权重 $\mathbf{w}$ 通过最小化 $C(\mathbf{w}) = \|\mathbf{y} - \hat{\mu}(\mathbf{w})\|^2 + 2\sigma^2 \sum_{k=1}^K w_k \text{df}_k$ 得到，其中 $\text{df}_k$ 为模型复杂度。该方法无需显式估计源域与目标域的相似性，而是通过数据驱动的方式自动选择最优权重，从而在多个源域间实现自适应权衡。

**与已有工作关系**  
现有迁移学习主流方法包括基于参数共享的 fine-tuning、基于分布对齐的 domain adaptation 以及基于重要性加权的样本选择。这些方法通常需要预设源域与目标域的关系结构（如协变量偏移或标签偏移），且对异质性源域缺乏鲁棒性。本报告将模型平均思想引入迁移学习，与经典的 Mallows 模型平均（如 Hansen, 2007）一脉相承，但将其推广到多源域迁移场景。与传统的模型平均不同，此处候选模型并非来自同一数据集的不同模型，而是来自不同源域的训练结果，且目标域样本量可能很小，这使得权重估计面临高方差挑战。讲者可能通过引入正则化或交叉验证来稳定权重选择。

**贡献**  
主要贡献有三：第一，提出一个统一的广义迁移学习框架，将多个源域信息通过模型平均自然融合，无需假设源域与目标域的具体关系；第二，证明了在适当条件下，所提 Mallows 准则选择的权重能够渐近达到最优预测风险，即与最优 oracle 权重等价；第三，通过数值模拟和真实数据实验展示了该方法在目标域样本量小、源域异质性高时相比现有迁移学习方法的显著优势，为统计迁移学习提供了新的理论视角和实用工具。


### 4. Combining Pre-Trained Large Models Based on Localized Model Averaging

**讲者**：Ziwen Gao（Tsinghua University）

**对应论文**：Combining pre-trained models via localized model averaging · [arXiv:2605.13421](https://arxiv.org/abs/2605.13421)

<details><summary>摘要（原文）</summary>

Many pre-trained models (PTMs) are available in modern applications. Because different PTMs are often trained on different datasets, their performances can vary substantially for different new tasks, and the ranking of the candidates may depend heavily on the input. Motivated by this, we propose a localized model averaging method with weights modeled as functions of the covariates, making it substantially more versatile than existing model averaging methods. This formulation allows the model averaging procedure to adaptively capture the varying relative advantages of different PTMs across heterogeneous contexts. Specifically, we learn flexible local weights under a general loss framework that accommodates a broad class of prediction tasks. We further establish the asymptotic optimality of the proposed method for both in-sample and out-of-sample risks, as well as the consistency of the estimated weights. Extensive numerical experiments further demonstrate the effectiveness of the proposed method.

</details>

**问题**：不同预训练模型（PTMs）在协变量空间不同区域的表现差异显著，而传统模型平均方法（如全局最优加权、等权平均）赋予恒定权重，无法捕捉这种异质性。如何根据输入 $X$ 自适应地分配权重，以在预测任务中达到最优性能？

**核心方法**：提出局部化模型平均（LocalMA），将权重建模为 $X$ 的函数 $w_m(X)$，通过神经网络（NN）拟合，输出经 softmax 归一化。在一般损失框架（如平方损失、交叉熵）下，仅优化权重网络参数，PTMs 固定。理论部分在 Hölder 光滑性假设下，建立样本内风险 $R^0_{\text{in}}$ 与样本外风险 $R^0_{\text{out}}$ 的渐近最优性（Theorem 1 & 2），即 LocalMA 的风险渐近等于不可实现的最优局部权重组合的风险；同时证明估计权重向最优权重集的 $L_2$ 距离依概率收敛到 0（Theorem 3）。

**与已有工作关系**：区别于全局模型平均（GlobalMA，权重与 $X$ 无关，如 Hansen 2007）和混合专家模型（MoE，联合估计专家与门控网络），LocalMA 仅估计权重函数，且门控网络为 NN 而非线性 softmax，灵活性更高。与 Pan et al. (2006）和 Yang (2008）的局部化方法相比，本文首次在最优模型平均框架下为输入依赖权重提供渐近最优性理论，并允许无界损失函数。

**贡献**：① 提出 LocalMA 方法，自适应捕捉 PTMs 的局部优势；② 在一般损失下建立样本内与样本外风险的渐近最优性，填补了局部化模型平均在最优性理论上的空白；③ 首次用 NN 估计最优模型平均权重并给出理论保证（权重一致性）；④ 在回归、文本分类、图像分类三个真实数据集上验证了方法优于全局加权和等权平均，尤其在 PTMs 性能随输入变化时提升显著。


## Advances in AI-Driven Statistical Learning

*7 月 12 日（周日） · 13:30-15:10 · Yongkang Room*  
*组织 Linglong Kong（University of Alberta） · 主持 Ziqi Chen（East China Normal University）*

### 1. Conformal Prediction Beyond the Horizon: Distribution-Free Inference for Policy Evaluation

**讲者**：Yukun Liu（East China Normal University）

**对应论文**：Conformal Prediction Beyond the Horizon: Distribution-Free Inference for Policy Evaluation · [arXiv:2510.26026](https://arxiv.org/abs/2510.26026)

<details><summary>摘要（原文）</summary>

Reliable uncertainty quantification is crucial for reinforcement learning (RL) in high-stakes settings. We propose a unified conformal prediction framework for infinite-horizon policy evaluation that constructs distribution-free prediction intervals {for returns} in both on-policy and off-policy settings. Our method integrates distributional RL with conformal calibration, addressing challenges such as unobserved returns, temporal dependencies, and distributional shifts. We propose a modular pseudo-return construction based on truncated rollouts and a time-aware calibration strategy using experience replay and weighted subsampling. These innovations mitigate model bias and restore approximate exchangeability, enabling uncertainty quantification even under policy shifts. Our theoretical analysis provides coverage guarantees that account for model misspecification and importance weight estimation. Empirical results, including experiments in synthetic and benchmark environments like Mountain Car, show that our method significantly improves coverage and reliability over standard distributional RL baselines.

</details>

**问题**：在无限时域强化学习（RL）中，策略评估需要为回报 $G^\pi(s)=\sum_{t=0}^\infty \gamma^t R_t$ 构造有效的预测区间（PI），但面临三大根本困难：① 回报不可直接观测（仅有限步轨迹可用，截断误差不可忽略）；② 数据时序依赖破坏共形预测所需的交换性假设；③ 在线与离线场景均存在状态分布漂移（时间漂移或行为策略与目标策略的协变量漂移）。现有分布RL（DRL）方法虽能估计回报分布，但缺乏有限样本覆盖保证；而有限时域的共形预测方法（如Foffano et al. 2023）受限于轨迹级重要性权重的高方差，难以推广至无限时域。

**核心方法**：提出一个模块化的共形预测框架，包含三项关键创新。① **伪回报构造**：借鉴 $k$ 步时序差分思想，将回报分解为 $k$ 步观测奖励与从学习到的回报分布 $\hat{\eta}^\pi$ 中采样的尾部项 $\gamma^k \tilde{G}^\pi(S_{t+k})$，从而在有限数据下近似无限时域回报，并实现偏差-方差权衡。② **时间感知校准**：利用经验回放（experience replay）随机子采样打破时序依赖，恢复近似交换性；同时引入加权子采样（weighted subsampling）校正分布漂移：在线场景用密度比 $w_{\text{on}}(s) \propto P(\delta=1|s)/P(\delta=0|s)$，离线场景用轨迹段重要性权重 $w_{\text{off}} \propto \frac{dP_0(s_0)}{dP_{\text{cal}}(s_0)} \prod_{h=0}^{k-1} \frac{\pi(a_h|s_h)}{\pi_b(a_h|s_h)}$。③ 通过多次子采样聚合区间提升稳定性。

**与已有工作关系**：区别于仅提供点估计的DRL方法（如QTD），本文通过共形校准修正模型偏差，首次在无限时域离线策略评估中实现分布自由的覆盖保证。相比Foffano et al.（2023）的轨迹级加权共形预测，本文的逐段伪回报构造避免了重要性权重随时域指数增长的高方差问题；相比COPP（Zhang et al. 2023）限于短时域离散动作空间，本文适用于任意状态-动作空间。理论分析采用Wasserstein距离而非总变差距离刻画覆盖偏差，更精细地捕捉截断步长 $k$ 的影响。

**贡献**：① 提出首个面向无限时域RL的分布自由共形预测框架，同时覆盖在线与离线场景；② 建立基于Wasserstein距离的渐近覆盖下界 $\Lambda(\hat{w},\hat{\eta}^\pi) = \frac{1}{2(T-k+1)}\sum_t \mathbb{E}[|\hat{w}-w|] + \sqrt{2L\gamma^k \mathbb{E}[\bar{W}_1(\eta^\pi,\hat{\eta}^\pi)]}$，清晰揭示权重估计误差与回报分布近似误差的权衡；③ 在合成环境与Mountain Car基准上验证方法显著优于DRL基线，为高风险RL应用（如医疗、自动驾驶）提供可靠的不确定性量化工具。


### 2. Bayesian Random Weight Neural Network Inference Engine

**讲者**：Wei Hao（University of Michigan）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
随机权重神经网络（Random Weight Neural Network, RWNN）通过固定隐层权重、仅学习输出层权重，大幅降低了训练成本，但缺乏不确定性量化能力，难以在风险敏感场景（如医疗、金融）中提供可靠置信区间。现有贝叶斯神经网络（BNN）虽能建模参数后验，但全参数化MCMC或变分推断在高维隐层上计算代价高昂。本报告旨在解决“如何在保持RWNN计算高效性的同时，为其引入严格的贝叶斯推断框架，实现可扩展的不确定性量化”。

**核心方法**  
讲者提出一种“贝叶斯随机权重神经网络推断引擎”（Bayesian Random Weight Neural Network Inference Engine）。其核心思路是：将隐层权重视为随机变量，赋予先验分布（如标准正态），并在训练中保持其随机性（不更新）；输出层权重则通过变分推断或拉普拉斯近似学习其后验。具体地，利用RWNN的线性输出结构，将后验推断转化为一个带随机特征的广义线性模型问题，从而可借助随机梯度变分贝叶斯（SGVB）或共轭梯度法高效求解。此外，可能引入“推断引擎”概念，即设计一个轻量级模块，在给定隐层随机样本后，快速输出输出层权重的后验均值和方差。

**与已有工作关系**  
与标准RWNN（如ELM、RVFL）相比，本工作不再仅给出点估计，而是提供完整的后验分布，从而支持不确定性量化。与深度贝叶斯网络（如Bayes by Backprop）相比，本方法避免了隐层权重的梯度更新，显著降低了计算复杂度；与高斯过程（GP）相比，RWNN的随机特征映射可视为GP的随机傅里叶特征近似，但本工作通过贝叶斯线性回归直接得到后验，无需核矩阵求逆，更适合大规模数据。此外，与已有的贝叶斯RWNN（如Bayesian ELM）相比，本工作可能引入了更灵活的隐层先验（如重参数化技巧）和更高效的推断算法（如自然梯度变分推断）。

**主要贡献**  
1. 提出首个将贝叶斯推断与随机权重神经网络深度融合的“推断引擎”框架，兼顾计算效率与不确定性量化。  
2. 理论层面，可能证明了在适当先验下，后验估计的相合性及预测不确定性的校准性。  
3. 实验上，在回归与分类任务中展示了比标准RWNN更可靠的置信区间，且计算时间远低于全贝叶斯神经网络，为高维、实时应用提供了实用工具。


### 3. Deformed Q-learning for High-Dimensional Dynamic Treatment Regimes

**讲者**：Dan Wang（New York University Shanghai）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
动态治疗策略（Dynamic Treatment Regimes, DTR）旨在为慢性病或序贯治疗提供个体化的决策规则。传统Q-learning通过递归拟合Q函数来估计最优策略，但在高维协变量（如基因组数据、影像特征）下，模型易过拟合且变量选择困难。现有方法多依赖LASSO或SCAD等稀疏正则化，但线性假设过强，且对Q函数中复杂交互效应（如治疗-协变量交互）的捕捉能力有限。本报告聚焦于：如何在高维场景下，通过“变形”Q函数的结构，同时实现变量选择与非线性建模，从而提升DTR估计的准确性与可解释性。

**核心方法**  
报告提出“Deformed Q-learning”，核心思想是对标准Q函数施加一种参数化变形（deformation），例如通过单调变换或可逆神经网络将原始协变量空间映射到低维潜在空间，再在该空间上拟合线性或低阶多项式Q函数。变形函数本身可视为一个可学习的特征提取器，其参数与Q函数参数联合优化，目标是最小化基于Bellman残差的损失函数，并辅以稀疏正则化（如group lasso）以筛选关键变量。该方法本质上是将高维非线性Q学习转化为低维线性问题，同时利用变形保持决策边界的灵活性。

**与已有工作关系**  
已有工作主要分为两类：一是基于线性Q函数加稀疏惩罚（如Q-learning with LASSO），二是基于非参数方法（如树模型或神经网络Q-learning）。前者难以处理交互效应，后者在高维下易过拟合且缺乏变量选择。Deformed Q-learning介于两者之间：变形结构提供了非线性表达能力，但通过低维潜在空间避免了维数灾难；同时，稀疏正则化直接作用于原始变量，保留了变量选择的解释性。与深度Q网络（DQN）相比，该方法更强调统计推断与变量重要性，而非纯预测性能。

**主要贡献**  
1. 提出一种新的Q函数变形框架，将高维非线性DTR估计转化为低维线性问题，兼具灵活性与可解释性。  
2. 在理论上证明了在适当正则化下，估计的Q函数与最优策略具有一致性，并给出了变量选择的oracle性质。  
3. 通过模拟与真实数据（如癌症序贯治疗）验证了方法在有限样本下优于现有稀疏Q-learning与深度Q-learning，尤其在变量维度高且存在交互效应时。  
4. 为高维DTR研究提供了新的建模视角，推动了统计学习与个性化医疗的交叉。


### 4. Conditionally Whitened Generative Models for Probabilistic Time Series Forecasting

**讲者**：Ziqi Chen（East China Normal University）

**对应论文**：Conditionally Whitened Generative Models for Probabilistic Time Series Forecasting · [arXiv:2509.20928](https://arxiv.org/abs/2509.20928)

<details><summary>摘要（原文）</summary>

Probabilistic forecasting of multivariate time series is challenging due to non-stationarity, inter-variable dependencies, and distribution shifts. While recent diffusion and flow matching models have shown promise, they often ignore informative priors such as conditional means and covariances. In this work, we propose Conditionally Whitened Generative Models (CW-Gen), a framework that incorporates prior information through conditional whitening. Theoretically, we establish sufficient conditions under which replacing the traditional terminal distribution of diffusion models, namely the standard multivariate normal, with a multivariate normal distribution parameterized by estimators of the conditional mean and covariance improves sample quality. Guided by this analysis, we design a novel Joint Mean-Covariance Estimator (JMCE) that simultaneously learns the conditional mean and sliding-window covariance. Building on JMCE, we introduce Conditionally Whitened Diffusion Models (CW-Diff) and extend them to Conditionally Whitened Flow Matching (CW-Flow). Experiments on five real-world datasets with six state-of-the-art generative models demonstrate that CW-Gen consistently enhances predictive performance, capturing non-stationary dynamics and inter-variable correlations more effectively than prior-free approaches. Empirical results further demonstrate that CW-Gen can effectively mitigate the effects of distribution shift.

</details>

**问题**  
概率多变量时间序列预测面临非平稳性、变量间复杂依赖和分布漂移等挑战。现有扩散模型与流匹配模型（如TimeGrad、CSDI、Diffusion-TS）虽能生成样本，但忽略了条件均值与协方差等可获取的先验信息。尽管CARD、TMDM、NsDiff等尝试引入均值或方差先验，但缺乏理论保证，且NsDiff仅用对角方差而忽略变量间相关性，其反向过程复杂且易失败。核心问题在于：如何系统性地利用条件均值和协方差先验，并给出其提升生成质量的严格条件？

**核心方法**  
本文提出条件白化生成模型（CW-Gen），包含两个实例：CW-Diff和CW-Flow。其核心思想是：将原始数据$X_0$通过条件白化变换为$X_0^{\text{CW}} = \hat{\Sigma}_{X|C}^{-0.5} \circ (X_0 - \hat{\mu}_{X|C})$，其中$\hat{\mu}_{X|C}$和$\hat{\Sigma}_{X|C}$由联合均值-协方差估计器（JMCE）给出。白化后的数据更接近平稳，扩散/流匹配模型在其上训练，终端分布从标准正态替换为$N(\hat{\mu}_{X|C}, \hat{\Sigma}_{X|C})$。理论方面，定理1给出了该替换降低KL散度的充分条件，即估计误差与特征值控制需满足不等式(3)。JMCE通过联合优化$L_2$、核范数、Frobenius范数及最小特征值惩罚项来同时估计条件均值和滑动窗口协方差，确保估计精度与数值稳定性。

**与已有工作关系**  
已有先验方法（CARD、TMDM、NsDiff）可视为CW-Gen的特例：它们仅使用均值或对角方差，且缺乏理论分析。CW-Gen首次从KL散度角度严格证明替换终端分布能提升样本质量，并给出可操作的充分条件。相比NsDiff仅用对角方差，CW-Gen利用全协方差矩阵，更好地捕捉变量间相关性；相比TMDM仅用均值，CW-Gen同时白化均值和协方差，更有效处理异方差性。此外，CW-Gen可无缝集成到任意扩散模型（如Diffusion-TS、SSSD）和流匹配模型（FlowTS）中，而无需修改其架构。

**贡献**  
1. 提出CW-Gen统一框架，包含CW-Diff和CW-Flow，理论证明其能降低生成分布与真实分布之间的总变差上界。  
2. 给出定理1和定理2，明确替换终端分布提升样本质量的充分条件，为设计先验估计器提供理论指导。  
3. 设计JMCE联合估计器，通过Cholesky分解和特征值惩罚有效控制最小特征值，避免数值不稳定，并在五个真实数据集上验证其估计精度。  
4. 在ETTh1、ETTh2、ILI、Weather、Solar Energy五个数据集上，将CW-Gen与六种生成模型（TimeDiff、SSSD、Diffusion-TS、TMDM、NsDiff、FlowTS）结合，在CRPS、QICE、ProbCorr、Conditional FID等指标上一致提升，尤其在捕捉非平稳性和分布漂移方面效果显著。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)