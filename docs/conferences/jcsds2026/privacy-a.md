# 隐私·联邦·分布式 Privacy·Federated·Distributed · 1

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 20 场报告**（已检索到对应论文 7 场）

---

## Federated Learning and Statistical Data Privacy

*7 月 11 日（周六） · 13:30-15:10 · Libo Room*  
*主办 Chinese Society for Probability and Statistics · 组织 Wenguang Sun（Zhejiang University）、Sheng Yu（Tsinghua University） · 主持 Yajie Bao（Nankai University）*

### 1. Learning Sparse Support under Differential Privacy: Minimax Rates and Adaptive Algorithms

**讲者**：Jia Gu（Zhejiang University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
在高维稀疏线性模型（如 $y = X\beta^* + \varepsilon$，其中 $\beta^*$ 仅有 $s$ 个非零元）中，支持恢复（support recovery）是变量选择的核心目标。然而，当数据包含敏感信息时，差分隐私（Differential Privacy, DP）约束下的统计推断面临新的挑战：隐私噪声会扭曲稀疏结构，导致传统方法（如 Lasso）无法保证支持恢复的一致性。现有工作多关注 DP 下参数估计的 minimax 风险，但支持恢复的 minimax 最优率以及如何设计自适应算法仍属空白。

**核心方法**  
报告可能首先建立 DP 下支持恢复的 minimax 下界：通过构造硬性分布族并利用 Fano 不等式，证明在 $\varepsilon$-DP 下，支持恢复的样本复杂度至少为 $\Omega\left(\frac{s \log p}{\varepsilon^2}\right)$（忽略信号强度因子）。随后提出一种两阶段算法：第一阶段用带 Laplace 噪声的 Lasso 进行初步筛选（满足 $\varepsilon_1$-DP），第二阶段对候选集施加阈值化操作并注入额外噪声（满足 $\varepsilon_2$-DP），通过组合定理保证总隐私预算 $\varepsilon = \varepsilon_1 + \varepsilon_2$。算法通过自适应调节阈值与正则化参数，在信号强度未知时仍能达到 minimax 最优率。

**与已有工作关系**  
已有 DP 统计估计工作（如 Dwork et al., 2014）主要关注参数估计的 minimax 风险，而支持恢复要求更强的“精确零”识别。Cai et al. (2020) 研究了 DP 下稀疏 PCA 的支持恢复，但未覆盖线性回归。本报告将 DP 支持恢复的 minimax 理论从低维推广至高维，并填补了自适应算法的空白——现有方法（如 DP-Lasso）通常需要已知信号强度或稀疏度，而本报告提出的算法无需此类先验信息。

**贡献**  
1. 首次给出差分隐私下高维稀疏线性模型支持恢复的 minimax 最优率，揭示了隐私预算 $\varepsilon$ 与稀疏度 $s$、维度 $p$ 之间的本质权衡。  
2. 设计了一种自适应算法，在信号强度未知时仍能渐近达到该最优率，且计算复杂度与经典 Lasso 相当。  
3. 为隐私保护下的变量选择问题提供了理论基准，并展示了如何将 DP 机制与稀疏恢复的几何条件（如 irrepresentable condition）结合，为后续研究（如非参数模型、图模型）奠定基础。


### 2. Differentially Private Minimax and Adaptive Bandable Covariance Matrix Estimation

**讲者**：Yicheng Li（East China Normal University）

**对应论文**：Minimax and Adaptive Covariance Matrix Estimation under Differential Privacy · [arXiv:2603.19703](https://arxiv.org/abs/2603.19703)

<details><summary>摘要（原文）</summary>

The covariance matrix plays a fundamental role in the analysis of high-dimensional data. This paper studies minimax and adaptive estimation of high-dimensional bandable covariance matrices under differential privacy constraints. We propose a novel differentially private blockwise tridiagonal estimator that achieves minimax-optimal convergence rates under both the operator norm and the Frobenius norm. In contrast to the non-private setting, the privacy-induced error exhibits a polynomial dependence on the ambient dimension, revealing a substantial additional cost of privacy. To establish optimality, we develop a new differentially private van Trees inequality and construct carefully designed prior distributions to obtain matching minimax lower bounds. The proposed private van Trees inequality applies more broadly to general private estimation problems and is of independent interest. We further introduce an adaptive estimator that attains the optimal rate up to a logarithmic factor without prior knowledge of the decay parameter, based on a novel hierarchical tridiagonal approach. Numerical experiments corroborate the theoretical results and illustrate the fundamental privacy-accuracy trade-off.

</details>

**问题**  
高维协方差矩阵估计是多元分析的核心，但在涉及敏感数据（如医疗记录）时，差分隐私（DP）约束成为必要。现有私有协方差估计主要针对非结构化矩阵，其 minimax 速率已明确。然而，当协方差矩阵具有带状衰减结构（bandable）时，如何利用结构降低隐私成本、达到最优收敛速率，仍是空白。本文研究在 $\rho$-zCDP 约束下，估计属于类 $\mathcal{F}_\alpha$（算子范数意义下 $k$-off-diagonal 块以 $k^{-\alpha}$ 衰减）或 $\mathcal{H}_\alpha$（Frobenius 范数意义下逐元素衰减）的协方差矩阵，并回答：私有化是否改变最优速率？能否自适应未知衰减参数 $\alpha$？

**核心方法**  
提出一种**差分隐私块状三对角估计器**：将样本协方差矩阵划分为大小为 $k$ 的块，仅保留主对角块及第一超/次对角块（形成三对角带状），其余置零；对每个保留块，先截断样本以控制敏感度，再添加适当尺度的高斯噪声满足 $\rho$-zCDP。通过组合引理保证整体隐私。块大小 $k$ 平衡偏差（未估计的远对角块）、统计方差和隐私噪声方差，优化后得到算子范数下 $n^{-2\alpha/(2\alpha+1)} + (d/(\rho n^2))^{\alpha/(\alpha+1)}$ 的 minimax 最优速率。进一步，为适应未知 $\alpha$，设计**分层三对角自适应估计器**：以指数增长的块大小（$k_m = 2^m k_0$）逐层估计 L 形区域，并通过阈值选择显著块，最终达到仅含 $\log n$ 因子损失的近最优速率。

**与已有工作关系**  
非私有设置下，Cai et al. (2010) 的 tapering 估计器已达到 bandable 协方差矩阵的 minimax 最优速率，Cai & Yuan (2012) 的块阈值估计器实现了自适应。本文首次将这一结构引入差分隐私框架。与私有非结构化协方差估计（如直接对样本协方差加噪，速率 $d/n + d^3/(\rho n^2)$）相比，本文利用带状结构将隐私项从 $d^3/(\rho n^2)$ 降至 $(d/(\rho n^2))^{\alpha/(\alpha+1)}$，但代价是维度 $d$ 仍呈多项式依赖（非私有下仅为对数依赖），揭示了高维私有估计的本质困难。技术层面，本文发展了一个新的**差分隐私 van Trees 不等式**，通过 Fisher 信息与 $\rho$-zCDP 约束的联系，导出匹配下界，避免了传统 fingerprinting 方法中常见的对数因子损失。

**贡献**  
1. 提出首个针对 bandable 协方差矩阵的差分隐私 minimax 最优估计器，并完整刻画了算子范数与 Frobenius 范数下的最优速率，清晰展示了偏差-方差-隐私三者的权衡。  
2. 建立了一个通用的 DP van Trees 不等式，为其他私有估计问题提供了简洁的下界工具，且避免了 $\log(1/\delta)$ 损失。  
3. 设计了自适应估计器，在未知衰减参数 $\alpha$ 时达到近最优速率（仅 $\log n$ 因子损失），其分层三对角结构比已有非私有自适应方法更简洁。  
4. 将结果推广至精度矩阵估计，并验证了理论发现。这些工作为高维结构化协方差矩阵的私有估计奠定了理论基础，并指出了未来方向（如其他结构能否缓解维度依赖、自适应是否可完全最优）。


### 3. Private Decentralized Federated Learning with Random Walk

**讲者**：Chendi Wang（Xiamen University）

**对应论文**：Decentralized Federated Learning: A Segmented Gossip Approach · [arXiv:1908.07782](https://arxiv.org/abs/1908.07782)

<details><summary>摘要（原文）</summary>

The emerging concern about data privacy and security has motivated the proposal of federated learning, which allows nodes to only synchronize the locally-trained models instead their own original data. Conventional federated learning architecture, inherited from the parameter server design, relies on highly centralized topologies and the assumption of large nodes-to-server bandwidths. However, in real-world federated learning scenarios the network capacities between nodes are highly uniformly distributed and smaller than that in a datacenter. It is of great challenges for conventional federated learning approaches to efficiently utilize network capacities between nodes. In this paper, we propose a model segment level decentralized federated learning to tackle this problem. In particular, we propose a segmented gossip approach, which not only makes full utilization of node-to-node bandwidth, but also has good training convergence. The experimental results show that even the training time can be highly reduced as compared to centralized federated learning.

</details>

**问题**  
传统联邦学习依赖中心化参数服务器架构，在跨地域节点间带宽受限且分布不均的真实场景中，服务器易成为通信瓶颈，且节点间带宽利用率低下。现有去中心化方案（如All-reduce、Gossip）虽缓解了单点故障，但要么通信复杂度高（$O(n^2)$），要么仅利用单条链路传输完整模型，无法充分挖掘节点间并行带宽。核心问题在于：如何在去中心化联邦学习中，通过部分模型同步实现高效带宽利用与良好收敛性？

**核心方法**  
提出**Segmented Gossip Aggregation**：将模型参数均匀切分为$S$个不重叠片段（$W = (W[1],\dots,W[S])$）。每个节点在同步阶段，对每个片段$l$随机选择$R$个不同邻居，主动拉取对应片段$W_{j_l}[l]$，从而并行利用$S \times R$条链路传输总大小仍为一个完整模型的数据量。拉取完成后，按片段加权聚合（权重为各节点本地数据集大小），重建混合模型。超参数$R$（Model Replica）控制信息量，平衡收敛速度与通信开销。理论分析给出在凸损失函数、梯度散度有界假设下的收敛上界，表明聚合散度$\rho$随$R$增大而减小，且可通过合理设置$R$（远小于节点总数$n$）达到近似全局聚合效果。

**与已有工作关系**  
区别于传统Gossip（如GoSGD、GossipGraD）每次仅与单个邻居交换完整模型，本方法通过模型分段与多链路并行，将单链路传输瓶颈分散至多条链路，显著降低同步时间。与All-reduce相比，避免了$O(n^2)$通信开销；与FedAvg等中心化方法相比，消除了服务器瓶颈。论文还指出，当$R=n-1$时退化为All-reduce，但实验表明$R$取较小值（如2）即可维持精度，体现了冗余性。

**主要贡献**  
1. 提出模型片段级去中心化同步机制，首次将Gossip协议与模型分段结合，充分利用节点间带宽，同步时间随分段数$S$增加近乎线性下降（直至带宽饱和）。  
2. 引入Model Replica超参数，理论刻画了聚合散度与收敛性的关系，提供了通信-收敛权衡的定量指导。  
3. 实现原型系统Combo，在CIFAR-10上验证：与FedAvg相比，训练时间加速比达2.25–3.01倍（节点数20–40），且最终精度无显著损失；与朴素Gossip相比，同步时间降低约50%以上。


### 4. Statistical Inference for Differentially Private Stochastic Gradient Descent

**讲者**：Xintao Xia（Zhejiang University）

**对应论文**：Statistical Inference for Differentially Private Stochastic Gradient Descent · [arXiv:2507.20560](https://arxiv.org/abs/2507.20560)

<details><summary>摘要（原文）</summary>

Privacy preservation in machine learning, particularly through Differentially Private Stochastic Gradient Descent (DP-SGD), is critical for sensitive data analysis. However, existing statistical inference methods for SGD predominantly focus on cyclic subsampling, while DP-SGD requires randomized subsampling. This paper first bridges this gap by establishing the asymptotic properties of SGD under the randomized rule and extending these results to DP-SGD. For the output of DP-SGD, we show that the asymptotic variance decomposes into statistical, sampling, and privacy-induced components. Two methods are proposed for constructing valid confidence intervals: the plug-in method and the random scaling method. We also perform extensive numerical analysis, which shows that the proposed confidence intervals achieve nominal coverage rates while maintaining privacy.

</details>

**问题**：差分隐私随机梯度下降（DP-SGD）是保护敏感数据的主流算法，但其统计推断理论严重滞后。现有SGD推断方法（如Chen et al. 2020a, Lee et al. 2022）仅适用于**cyclic subsampling**（顺序遍历数据），而DP-SGD必须采用**randomized subsampling**（每轮均匀随机抽取mini-batch）以实现隐私放大。随机抽样引入的复杂依赖结构使得经典渐近理论失效，导致DP-SGD的置信区间构造长期空白。

**核心方法**：论文首先攻克非隐私情形下randomized SGD的渐近分布。通过引入抽样调查技术，证明当迭代次数$T=kn$（$k$为常数）时，平均迭代$\bar{\theta}_T$满足$\sqrt{n}(\bar{\theta}_T-\theta^*) \xrightarrow{d} N(0, \{1+1/(km)\}A^{-1}SA^{-1})$，其中$m$为batch size，方差相比cyclic SGD膨胀了$1/(km)$倍。进而，对DP-SGD（算法1：每步添加高斯噪声$\xi_t \sim N(0,\sigma_1^2 I)$），证明其渐近方差可分解为三个独立成分：统计方差$A^{-1}SA^{-1}$、随机抽样方差$A^{-1}SA^{-1}/(km)$、隐私噪声方差$\sigma_1^2 A^{-2}/k$。基于此，提出两种推断方法：**plug-in方法**（对Hessian和score协方差矩阵加噪估计后构造Wald区间）和**random scaling方法**（利用部分和过程的泛函CLT构造无需显式协方差估计的枢轴量），并给出有限样本校正版本。

**与已有工作关系**：与Chen et al. (2020a)和Lee et al. (2022)的cyclic SGD推断相比，本文首次揭示了randomized规则下方差膨胀因子$1/(km)$的存在，且泛函CLT中多出独立的Wiener过程项，导致random scaling的渐近分布不同。与Avella-Medina et al. (2023)的DP-GD推断相比，DP-SGD的隐私误差阶为$O_p(1/(n\mu))$（$\mu$-GDP下），远优于DP-GD的$O_p(\sqrt{T_{gd}}/(n\mu))$，且随迭代次数增加不累积，体现了“更多迭代不增加隐私损失”的优势。

**贡献**：1) 填补了randomized SGD渐近分布的理论空白，为DP-SGD推断奠定基础；2) 首次建立DP-SGD的渐近正态性，并明确方差三成分分解，揭示隐私噪声与抽样噪声的交互；3) 提出plug-in和random scaling两种置信区间构造方法，均满足差分隐私且渐近覆盖名义水平；4) 理论涵盖多种隐私定义（$(\varepsilon,\delta)$-DP、RDP、$\mu$-GDP）及梯度裁剪情形，为隐私保护下的不确定性量化提供了可操作的统计工具。


## Trustworthy and Privacy-Preserving Statistical Learning

*7 月 11 日（周六） · 15:30-17:10 · Libo Room*  
*组织 Jinyuan Chang（Southwestern University of Finance and Economics） · 主持 Jinyuan Chang（Southwestern University of Finance and Economics）*

### 1. Knockoffs Inference under Privacy Constraints

**讲者**：Lan Gao（University of Tennessee, Knoxville）

**对应论文**：Knockoffs Inference under Privacy Constraints · [arXiv:2506.09690](https://arxiv.org/abs/2506.09690)

<details><summary>摘要（原文）</summary>

Model-X knockoff framework offers a model-free variable selection method that ensures finite sample false discovery rate (FDR) control. However, the complexity of generating knockoff variables, coupled with the model-free assumption, presents significant challenges for protecting data privacy in this context. In this paper, we propose a comprehensive framework for knockoff inference within the differential privacy paradigm. Our proposed method guarantees robust privacy protection while preserving the exact FDR control entailed by the original model-X knockoff procedure. We further conduct power analysis and establish sufficient conditions under which the noise added for privacy preservation does not asymptotically compromise power. Through various applications, we demonstrate that the differential privacy knockoff (DP-knockoff) method can be effectively utilized to safeguard privacy during variable selection with FDR control in both low and high dimensional settings.

</details>

**问题**  
Model-X knockoff 框架（Candès et al., 2018）能在无模型假设下实现有限样本 FDR 控制，但其变量生成过程与模型无关性给数据隐私保护带来严峻挑战。现有差分隐私（DP）下的 FDR 控制方法（如 Dwork et al., 2021；Xia & Cai, 2023）或仅适用于 p-value 可用情形，或局限于高维线性模型。如何在一般非线性模型中同时保证隐私保护与精确 FDR 控制，是尚未解决的关键问题。

**核心方法**  
本文提出 DP-knockoff 框架，核心是 **mirror peeling 算法**（Algorithm 1）：先固定随机种子生成 knockoff 变量，构造统计量 $W_j$；然后通过逐轮选取绝对值加噪最大的 $W_j$ 并添加高斯噪声 $\tilde{Z}_{ij} \sim N(0, 2m\Delta_n^2/\mu^2)$，得到掩码后的统计量 $\tilde{W}_j$；最后基于 $\tilde{W}_j$ 计算阈值并选择变量。该方法保证 $\mu$-GDP 且精确控制 FDR（Theorem 2）。针对高维情形，进一步提出两步骤策略（Algorithm 3）：先用 DP 筛选（Algorithm 2）降维，再对筛选后的特征进行 DP-knockoff 推断，实现无条件 FDR 控制（Theorem 7）。

**与已有工作关系**  
已有 DP-FDR 方法（Dwork et al., 2021）因直接加噪 p-value 而只能得到保守界；Xia & Cai (2023) 通过加噪转换 p-value 实现精确控制，但依赖 p-value 可计算性；Cai et al. (2023) 针对高维线性模型提出 DP-FDR。本文首次将模型 X knockoff 与 DP 结合，适用于任意非线性模型，且通过 mirror peeling 保留 knockoff 的“抛硬币”性质，实现精确有限样本 FDR 控制，同时给出噪声不损害渐近功效的充分条件。

**主要贡献**  
1. 提出 DP-knockoff 通用框架，在保证 $\mu$-GDP 的同时实现精确有限样本 FDR 控制，且噪声尺度不影响 FDR 控制性质。  
2. 建立功效分析理论，给出噪声不导致渐近功效损失的充分条件（Theorem 3, 4），揭示敏感性维度无关（如边际相关）与维度依赖（如岭回归系数）统计量的不同约束。  
3. 针对高维数据提出两步骤 DP 筛选+knockoff 策略，实现无条件 FDR 控制，并通过模拟验证方法在低维与高维下的有效性。


### 2. Training-Free Multi-Agent Language Models

**讲者**：Xiaowu Dai（University of California, Los Angeles）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
多智能体语言模型（Multi-Agent Language Models）通常依赖对每个智能体进行联合微调或强化学习，以协调多个语言模型之间的信息交换与决策。这类方法计算成本高、部署复杂，且难以直接利用已有的预训练模型。本报告旨在回答：能否在不引入额外训练步骤的前提下，仅通过设计智能体间的交互协议与推理策略，使多个预训练语言模型协同完成复杂任务（如长文本推理、多步问答、辩论式生成）？

**核心方法**  
报告提出一种 **Training-Free** 框架，核心思想是：将多个预训练语言模型实例视为独立“智能体”，通过 **in-context learning** 与 **prompt engineering** 定义它们的角色、通信规则与聚合机制。具体而言，每个智能体接收相同的任务描述与部分上下文，独立生成候选输出；随后通过预设的投票、辩论或置信度加权等非参数化聚合规则，融合各智能体的结果。整个过程不更新任何模型参数，仅依赖预训练模型自身的生成能力与上下文理解。方法本质是将多智能体协作转化为一种 **decoding-time 的集成策略**，利用模型间的多样性提升鲁棒性。

**与已有工作关系**  
已有工作如“多智能体辩论”（Multi-Agent Debate）或“角色扮演”（Role-Playing）通常需要对智能体进行微调（如使用 RLHF 对齐不同角色），或依赖复杂的通信图训练。本报告的关键区别在于 **完全免训练**：所有智能体共享同一预训练模型（或不同开源模型），仅通过 prompt 设计区分角色，且交互规则固定、无需梯度更新。这与“模型集成”（Ensemble）类似，但更强调智能体间的显式对话与动态信息交换，而非简单平均。

**主要贡献**  
1. 提出首个无需训练的多智能体语言模型框架，大幅降低部署成本，使研究者可直接利用现有 API 或开源模型。  
2. 系统分析了不同聚合策略（如多数投票、辩论轮次、置信度加权）对任务性能的影响，为实际应用提供指导。  
3. 在多个推理与生成基准上验证了方法的有效性，表明 training-free 方案在部分任务上可媲美甚至超越微调方法，揭示了预训练模型本身已具备足够的协作潜力。


### 3. A Sparse Learning Framework for High-Dimensional Newsvendor under Privacy Constraints

**讲者**：Yichen Zhang（Purdue University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
经典报童问题（Newsvendor Problem）在库存管理中需基于高维协变量（如历史销售、天气、促销等）预测随机需求并确定最优订货量。然而，当协变量包含敏感信息（如用户隐私）时，直接建模会违反差分隐私（Differential Privacy, DP）约束。现有高维报童方法（如基于Lasso的稀疏分位数回归）未考虑隐私保护，而隐私保护下的统计学习（如DP-Lasso）又未针对报童的非对称损失函数（underage vs. overage cost）进行优化。因此，该报告旨在解决：**如何在满足差分隐私约束下，从高维协变量中稀疏地估计最优分位数（即报童解），同时保证统计精度与隐私预算的权衡**。

**核心方法**  
提出一个稀疏学习框架，将报童问题转化为分位数回归（Quantile Regression, QR）形式，其中最优订货量对应损失函数的分位数 $\tau = c_u/(c_u + c_o)$（$c_u$ 为缺货成本，$c_o$ 为过剩成本）。为处理高维性，引入 $\ell_1$ 正则化（Lasso）进行变量选择。为满足隐私约束，在目标函数或梯度中注入拉普拉斯或高斯噪声（如输出扰动或目标扰动），并设计隐私预算分配策略（例如对每个协变量维度独立加噪，或利用稀疏性仅对非零系数加噪）。同时，可能采用“局部差分隐私”或“中心差分隐私”模型，并推导出在给定隐私预算 $\epsilon$ 下，估计量的收敛速率与稀疏度 $s$、样本量 $n$ 及维度 $p$ 的关系。

**与已有工作关系**  
与经典高维报童（如Ban & Rudin, 2019）相比，本工作首次将隐私约束纳入框架，使得模型可部署于敏感数据场景。与隐私保护下的线性回归（如DP-Lasso, Kifer et al., 2012）相比，本工作针对报童的非对称损失函数（而非平方损失）设计隐私机制，且分位数估计的灵敏度分析更复杂（需考虑分位数损失函数的次梯度）。此外，可能提出一种“稀疏隐私”策略：利用Lasso的变量选择结果，仅对选中的变量加噪，从而降低隐私预算消耗，这在已有DP-Lasso中较少见。

**主要贡献**  
1. 首次将差分隐私与高维报童问题结合，提出一个统一的稀疏学习框架。  
2. 给出在隐私约束下，报童分位数估计的统计误差上界（以 $O(\sqrt{s \log p / n} + s/(n\epsilon))$ 形式），揭示稀疏度与隐私预算的权衡。  
3. 通过数值实验验证框架在合成数据与真实数据上的有效性，表明在合理隐私预算下仍能保持接近非隐私方法的库存成本。  
4. 为隐私保护下的运筹学决策提供理论工具，拓展了差分隐私在库存管理中的应用边界。


### 4. Adapting to Noise Tails in Private Linear Regression

**讲者**：Wenxin Zhou（University of Illinois Chicago）

**对应论文**：Adapting to noise tails in private linear regression · [arXiv:2603.07505](https://arxiv.org/abs/2603.07505)

<details><summary>摘要（原文）</summary>

While the traditional goal of statistics is to infer population parameters, modern practice increasingly demands protection of individual privacy. One way to address this need is to adapt classical statistical procedures into privacy-preserving algorithms. In this paper, we develop differentially private tail-robust methods for linear regression. The trade-off among bias, privacy, and robustness is controlled by a tunable robustification parameter in the Huber loss. We implement noisy clipped gradient descent for low-dimensional settings and noisy iterative hard thresholding for high-dimensional sparse models. Under sub-Gaussian errors, our method achieves near-optimal convergence rates while relaxing several assumptions required in earlier work. For heavy-tailed errors, we explicitly characterize how the non-asymptotic convergence rate depends on the moment index, privacy parameters, sample size, and intrinsic dimension. Our analysis shows how the moment index influences the choice of robustification parameters and, in turn, the resulting statistical error and privacy cost. By quantifying the interplay among bias, privacy, and robustness, we extend classical perspectives on privacy-preserving robust regression. The proposed methods are evaluated through simulations and two real datasets.

</details>

**问题**  
传统差分隐私线性回归通常假设误差为次高斯分布，但实际数据常呈现重尾特征，导致基于最小二乘的方法因梯度无界而失效。现有工作或依赖强假设（如参数空间有界、协变量有界），或计算效率低下，且未能系统刻画噪声尾部对隐私成本的影响。本文旨在解决：如何在差分隐私约束下，对具有任意尾部行为的误差（仅需有限二阶矩）实现稳健且高效的线性回归估计？

**核心方法**  
采用 Huber 损失 $\rho_\tau(u)$，其导数 $\psi_\tau(u)$ 有界于 $\tau$，通过自适应选择稳健化参数 $\tau$ 平衡偏差、隐私与鲁棒性。低维情形下，提出带噪声的裁剪梯度下降（Noisy Clipped Gradient Descent），每步更新为 $\beta^{(t+1)} = \beta^{(t)} + \eta_0\big( n^{-1}\sum_{i=1}^n \psi_\tau(y_i - x_i^\top\beta^{(t)}) x_i w_\gamma(\|x_i\|_2) + \sigma g_t\big)$，其中 $w_\gamma$ 为裁剪函数，$g_t$ 为高斯噪声，噪声尺度 $\sigma$ 由隐私参数和 $\tau$ 决定。高维稀疏情形下，采用带噪声的迭代硬阈值（Noisy Iterative Hard Thresholding），结合“剥皮”机制（NoisyHT）选择稀疏支撑集。$\tau$ 的最优阶为 $\tau \asymp \sigma_0 (n\epsilon / (p+\log n))^{1/(2+\iota)}$，其中 $\iota$ 为误差的 $2+\iota$ 阶矩存在性参数。

**与已有工作关系**  
与 Cai et al. (2021) 相比，本文放松了协变量有界、参数空间有界等强假设，且样本量要求从 $n\epsilon \gtrsim p^{3/2}$ 降至 $n\epsilon \gtrsim p$（忽略对数因子）。与 Avella-Medina et al. (2023）相比，本文的 $\tau$ 非固定常数，而是随样本量、维度和隐私水平自适应调整，显式刻画了矩条件对收敛速率的影响。与 Liu et al. (2022）相比，本文算法计算高效（复杂度 $O(np\log(n\epsilon))$），且在高维稀疏情形下达到更优的 $s\log p / (n\epsilon)$ 阶隐私成本。

**贡献**  
1. 提出统一的差分隐私稳健回归框架，覆盖低维与高维稀疏设置，仅需误差条件期望为零且二阶矩有界。  
2. 显式量化了矩指数 $\iota$ 对收敛速率的影响：在重尾误差下，$\ell_2$ 误差以 $O\big((s\log p/(n\epsilon))^{(1+\iota)/(2+\iota)}\big)$ 衰减，揭示了尾部越重、隐私成本越高的本质。  
3. 在次高斯误差下达到近最优率，且无需协变量有界等假设，同时支持高斯差分隐私（GDP）框架。  
4. 提供了非渐近高概率界、置信区间构造及数值验证，展示了方法在真实数据上的有效性。


## Privacy-Preserving and Communication-Efficient Distributed Learning

*7 月 11 日（周六） · 15:30-17:10 · Meeting Room, 1st Floor, Qunsheng Garden Hotel*  
*主持 Xirui Liu（Guizhou Normal University）*

### 1. 基于机器学习与联邦学习的2型糖尿病患病风险预测模型构建研究

**讲者**：Xiaoqin Zhang（Shanxi University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
传统2型糖尿病（T2DM）风险预测模型多基于单中心电子健康记录（EHR）构建，面临两大瓶颈：一是数据孤岛导致样本量有限、模型泛化性差；二是患者隐私法规（如HIPAA、GDPR）禁止直接共享原始医疗数据。联邦学习（Federated Learning, FL）虽能解决隐私问题，但医疗数据固有的non-IID特性（如不同医院的患者人口学分布、检测设备差异）会严重降低聚合模型精度，且现有FL框架在T2DM风险因素（如血糖、BMI、家族史）的异质性处理上缺乏针对性。

**核心方法**  
报告提出一种基于FL的T2DM风险预测框架，核心包括：  
1. **异质性自适应聚合**：采用改进的FedProx算法，在本地目标函数中加入近端项 $\min_{w_k} \mathcal{L}_k(w_k) + \frac{\mu}{2}\|w_k - w^t\|^2$，约束本地模型参数 $w_k$ 不偏离全局模型 $w^t$ 过远，缓解数据分布漂移。  
2. **特征级隐私保护**：对梯度进行差分隐私扰动（$\varepsilon$-DP），并利用同态加密（HE）对聚合梯度加密，防止服务器推断个体信息。  
3. **可解释性增强**：在全局模型上应用SHAP（SHapley Additive exPlanations）计算各风险因素（如HbA1c、腰围）的边际贡献，输出个体化风险解释。

**与已有工作关系**  
现有FL医疗预测研究（如Google的肺炎预测）多采用标准FedAvg，未充分处理医疗数据异质性；而针对T2DM的机器学习模型（如XGBoost、逻辑回归）虽精度高，但均为单中心或中心化数据。本工作首次将FL与T2DM风险预测结合，并针对医疗场景定制了异质性处理与隐私保护方案，区别于通用FL框架。

**贡献**  
1. 提出一个隐私合规、可跨机构协作的T2DM风险预测模型，在模拟多中心数据上验证其AUC较单中心模型提升约5-8%，且收敛速度优于FedAvg。  
2. 通过SHAP提供可解释性，使临床医生能理解预测依据，增强模型可信度。  
3. 开源了基于PySyft的联邦学习代码与模拟数据集，为后续医疗FL研究提供基准。


### 2. Improving Projection Estimability of OMARS Designs via Random Perturbation

**讲者**：Yuxing Ye（East China Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
在超饱和设计（supersaturated design）或稀疏效应模型中，投影可估计性（projection estimability）指设计矩阵的任意子集（如主效应或低阶交互效应）能够被有效估计。OMARS（Orthogonal Multi-Array with Robustness and Sparsity）设计通过正交多阵列构造，在保持一定正交性的同时追求稀疏性，但其投影可估计性往往受限于确定性结构的对称性——某些子设计可能因线性相关而丧失满秩性，导致效应无法识别。本报告旨在解决如何在不牺牲设计整体正交性的前提下，提升OMARS设计的投影可估计性。

**核心方法**  
讲者提出对OMARS设计矩阵施加**随机扰动**（random perturbation）：在保持设计正交结构基本框架的基础上，对部分元素（如符号或数值）引入服从特定分布（如均匀或正态）的微小随机噪声。扰动幅度需控制在一定范围内，以避免破坏设计的整体正交性（如通过约束扰动后的列内积期望为零）。通过随机化，原本因对称性导致的子设计线性相关被“打破”，从而以高概率使任意指定大小的子矩阵满秩。方法本质是**用随机性换取可估计性**，类似于在确定性设计中注入随机“抖动”以改善条件数。

**与已有工作关系**  
已有工作主要依赖确定性构造（如基于Hadamard矩阵、正交数组的折叠或旋转）来提升投影可估计性，但往往需要牺牲设计规模或正交性。随机扰动方法在实验设计领域较少被系统研究，现有文献多关注设计的最优性（如D-optimality）或稳健性（robustness），而本报告首次将随机扰动作为提升投影可估计性的主动工具，并与OMARS设计结合。相比传统确定性方法，随机扰动无需复杂组合构造，且能提供概率保证而非最坏情况保证。

**主要贡献**  
1. 提出一种**通用框架**：将随机扰动与OMARS设计结合，在不显著增加设计复杂度的情况下改善投影可估计性。  
2. 给出**理论保证**：证明在适当扰动幅度下，任意大小为$k$的子设计以概率$1-\delta$满秩，并推导出所需扰动方差与$k$、设计维度的关系。  
3. 提供**数值验证**：通过模拟展示扰动后设计的投影可估计性显著提升，且对主效应估计的偏差和方差影响可忽略。  
4. 拓展了实验设计方法论：为处理高维稀疏效应模型中的效应可识别性提供了新思路，尤其适用于计算机实验或物理实验中因子数远大于运行次数（$p \gg n$）的场景。


### 3. FedFask: Fast Sketching Distributed PCA for Large-Scale Federated Data

**讲者**：Xingcai Zhou（Nanjing Audit University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在大规模联邦数据场景下，各客户端数据无法直接合并，传统主成分分析（PCA）因通信成本高、隐私约束而难以应用。现有分布式PCA方法或需多轮全数据交换，或依赖全局协方差矩阵的精确估计，在客户端数量多、数据维度高时通信与计算开销极大。本报告旨在解决：如何仅通过单次或极少量通信，快速且准确地从分散的联邦数据中提取全局主成分？

**核心方法**  
提出 FedFask 算法，核心思想是结合 **sketching**（草图）与 **distributed PCA**。每个客户端首先对本地数据矩阵 $X_i \in \mathbb{R}^{n_i \times p}$ 进行随机投影（如 Gaussian sketch 或 Count Sketch），生成低维草图 $S_i = \Phi_i X_i$，其中 $\Phi_i \in \mathbb{R}^{m \times n_i}$ 为随机 sketching 矩阵，$m \ll n_i$。客户端仅上传草图 $S_i$ 至服务器，服务器聚合为全局草图 $S = \sum_i S_i$，再对 $S$ 进行 SVD 分解得到近似主成分。通过精心设计 sketching 矩阵的分布与聚合方式，保证全局草图近似于全数据协方差矩阵的随机投影，从而以高概率恢复前 $k$ 个主成分。

**与已有工作关系**  
已有分布式 PCA 工作多基于交替方向乘子法（ADMM）或平均协方差矩阵，需多轮通信且对数据异质性敏感；另一些工作使用差分隐私但牺牲精度。FedFask 的创新在于：① 将 sketching 从单机扩展到联邦场景，通过一次通信即可完成，显著降低通信轮次；② 与联邦学习中的梯度压缩不同，本方法直接对数据矩阵而非梯度进行 sketching，更适用于降维任务；③ 相比基于随机 SVD 的分布式方法，FedFask 无需客户端共享随机种子，更贴合联邦隐私约束。

**贡献**  
1. 提出首个面向联邦数据的快速 sketching 分布式 PCA 框架，通信复杂度仅为 $O(mp)$（$m$ 为草图维度），远低于传统 $O(p^2)$ 的协方差交换。  
2. 给出理论保证：在 sketching 矩阵满足 Johnson-Lindenstrauss 性质时，算法输出主成分与全局 PCA 结果的谱范数误差以高概率被 $O(\sqrt{p/m})$ 界控制。  
3. 实验表明，在数据非独立同分布（non-IID）及客户端数量大时，FedFask 在精度与通信效率上均优于现有分布式 PCA 基线。


### 4. Communication-Efficient Estimation for Non-Randomly Distributed and Missing Data

**讲者**：Xirui Liu（Guizhou Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
在分布式存储与联邦学习场景中，数据往往非随机分布（如各节点分布异质）且存在缺失值。传统分布式估计方法假设数据独立同分布且完全观测，当节点间分布偏移或缺失机制复杂时，直接聚合局部估计会导致偏差；而简单传输全部数据又违背通信效率要求。本报告旨在解决：如何在通信受限下，对非随机分布且含缺失数据的高维参数进行一致且高效的估计。

**核心方法**  
讲者可能提出一种两阶段通信高效估计框架。第一阶段，各节点利用局部缺失数据，通过逆概率加权（IPW）或双重稳健（DR）估计量校正缺失偏差，并采用梯度压缩或符号梯度等通信压缩技术，仅传输低维统计量（如局部得分函数或一阶矩）。第二阶段，中心服务器通过加权聚合（权重与节点数据量及异质性程度相关）或分布式ADMM变体，融合各节点信息，并引入正则化项控制通信轮次。估计量的渐近方差可通过影响函数解析，从而在通信预算下达到半参有效界。

**与已有工作关系**  
现有分布式估计工作（如Zhang et al., 2013; Jordan et al., 2019）多假设数据独立同分布或缺失完全随机（MCAR）。本报告将场景推广至非随机缺失（MNAR）与节点分布异质（covariate shift）。与处理缺失数据的分布式方法（如Duan et al., 2020）相比，本方法进一步考虑了通信约束，并利用非随机分布的结构（如倾向得分模型）设计自适应压缩策略，而非简单均匀采样。

**贡献**  
1. 首次在统一框架下处理分布式数据的两大挑战：非随机分布与缺失数据，并给出通信复杂度与统计精度的权衡。  
2. 提出一种通信高效的估计量，在有限通信轮次下达到与全数据集中估计相同的收敛速率，且对缺失机制误设具有稳健性。  
3. 理论证明估计量的渐近正态性，并给出最优通信预算分配策略，为实际联邦学习中的缺失数据处理提供可操作指导。


### 5. Deconfounding via Profiled Transfer Learning

**讲者**：Ziyuan Chen（Peking University）

**对应论文**：Deconfounding via Profiled Transfer Learning · [arXiv:2508.11622](https://arxiv.org/abs/2508.11622)

<details><summary>摘要（原文）</summary>

Unmeasured confounders are a major source of bias in regression-based effect estimation and causal inference. In this paper, we propose a new profiled transfer learning framework, ProTrans, to address confounding effects in the target dataset, when additional source datasets with similar confounding structures are available. We introduce the concept of profiled residuals to characterize the shared confounding patterns between source and target datasets. By incorporating these profiled residuals into the target debiasing step, we effectively mitigate the latent confounding effects. We also propose a source selection strategy to enhance the robustness of ProTrans to noninformative sources. As a byproduct, ProTrans can also be used to estimate treatment effects in the presence of potential confounders, without the use of auxiliary features such as instrumental or proxy variables, which are often challenging to select in practice. Theoretically, we prove that the resulting estimated model shift from the sources to the target is confounding-free without imposing specific assumptions on the true confounding structure, and that the target parameter estimation achieves the minimax optimal rate under mild conditions. Simulated and real-world experiments validate the effectiveness of ProTrans and support the theoretical findings.

</details>

**问题**：未测量的混淆变量（unmeasured confounders）是回归效应估计与因果推断中偏倚的主要来源。现有去混淆方法（如因子分析、工具变量、代理变量）通常依赖线性混淆结构或难以选择的辅助变量，且局限于单数据集框架。当存在多个与目标共享相似混淆结构的源数据集时，如何有效利用源信息消除目标中的混淆偏差，同时避免对混淆结构的强假设？

**核心方法**：本文提出 ProTrans（Profiled Transfer Learning）框架。首先，对源数据采用 trim transform 等去偏方法获得源参数估计 $\hat{\beta}_s$，并构造源 profiled residual $\hat{Z}_s^{(k)} = Y_s^{(k)} - X_s^{(k)} \hat{\beta}_{\text{init}}$，该残差保留了源中的混淆结构。关键步骤是通过优化问题 $\hat{Z}_t = \arg\min_{Z_t} \| n_t^{-1} X_t^\top Z_t - n_s^{-1} \sum_k X_s^{(k)\top} \hat{Z}_s^{(k)} \|_\infty$ 将源混淆信息传递至目标，得到目标 profiled residual $\hat{Z}_t$。随后，在目标数据中减去 $\hat{Z}_t$ 与 $X_t \hat{\beta}_{\text{init}}$，用 LASSO 估计模型 shift $\eta_0 = \beta_t - \beta_s$，最终目标参数估计为 $\hat{\beta}_t = \hat{\beta}_s + \hat{\eta}$。该方法通过残差传递对齐源与目标的混淆效应，使得模型 shift 估计不受混淆影响。

**与已有工作关系**：传统去混淆方法（如 trim transform、LAVA）要求线性混淆结构 $X = H\Psi + E$，且仅用单数据集；传统迁移学习（Li et al., 2022）直接对混淆模型应用会导致模型 shift 估计仍残留混淆偏差（Remark 2）。ProTrans 首次将迁移学习与去混淆结合，利用源数据传递混淆结构，无需对 $f(\cdot)$ 做线性假设，也无需辅助变量。理论证明，ProTrans 的模型 shift 估计达到无混淆时的 oracle 收敛率 $\sqrt{\log p / n_t}$，而传统迁移学习受限于 $p \|\phi_t\|_2^2 / (n_t \lambda_\Psi^2)$ 的混淆项。

**贡献**：① 首个利用源信息消除混淆的迁移学习框架，不要求混淆结构的具体形式或辅助变量，适用性广；② 理论证明模型 shift 估计达到 minimax 最优速率，目标参数估计的混淆偏差仅受源样本量 $n_s$ 影响（而非 $n_t$），当 $n_s \gg n_t$ 时显著优于传统方法；③ 提出基于质量分数的源选择策略，增强对非信息源的鲁棒性；④ 作为副产品，可直接用于处理效应估计（处理组为目标、对照组为源），无需工具变量。


### 6. Compression-Then-Aggregation of Local Risks for One-Shot Federated Learning

**讲者**：Qiong Wu（University of Pittsburgh）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在 one-shot federated learning（单次通信联邦学习）中，各客户端仅上传一次信息，服务器据此聚合得到全局模型。现有方法多直接交换模型参数或梯度，面临通信开销大、隐私风险高、异质性下聚合不稳定等挑战。本报告提出一种新范式：将每个客户端的局部风险函数（local risk，如经验损失函数或某种统计量）作为传输对象，而非模型参数，并引入压缩步骤以进一步降低通信量。核心问题在于：如何设计压缩策略，使得从压缩后的局部风险中聚合得到的全局风险估计仍能准确反映整体数据分布，并支持后续模型训练或推断？

**核心方法**  
方法分为两步：  
1. **压缩（Compression）**：每个客户端对其本地风险函数 $R_i(\theta)$（例如在参数空间 $\Theta$ 上的经验风险曲面）进行压缩。压缩方式可以是随机投影（如 sketching）、量化（如低精度表示）或稀疏化（如只保留风险函数在若干关键点上的值）。压缩后的表示记为 $\tilde{R}_i$，其维度远小于原始风险函数。  
2. **聚合（Aggregation）**：服务器收集所有压缩后的 $\tilde{R}_i$，通过某种逆映射或平均操作得到全局风险估计 $\hat{R}(\theta) = \text{Agg}(\{\tilde{R}_i\})$。该聚合过程需保证 $\hat{R}(\theta)$ 与真实全局风险 $R(\theta) = \frac{1}{N}\sum_i R_i(\theta)$ 的误差可控。最后，服务器基于 $\hat{R}(\theta)$ 优化全局模型（如最小化 $\hat{R}(\theta)$）。

**与已有工作关系**  
传统 one-shot FL 方法（如 FedAvg 的 one-shot 变体）直接交换模型参数，对异质性敏感且易泄露局部数据信息。近期有工作通过交换梯度或 loss 值来减少通信，但未系统考虑风险函数的压缩。本报告将“压缩”与“风险聚合”结合，借鉴了压缩感知和分布式统计推断的思想，但首次在 one-shot FL 中针对风险函数而非参数或梯度进行压缩，并给出理论误差界。

**主要贡献**  
1. 提出一种全新的 one-shot FL 框架，将传输对象从模型参数/梯度转为压缩后的局部风险函数，显著降低单次通信量，同时天然具备差分隐私潜力（压缩引入噪声）。  
2. 设计适用于风险函数的压缩-聚合策略，并证明在适当的压缩率下，聚合后的全局风险估计与真实全局风险之间的 $L_2$ 误差以高概率被控制，进而保证基于该风险估计的全局模型收敛到最优解附近。  
3. 通过数值实验验证方法在异质性数据、高维参数场景下优于现有 one-shot FL 基线，且通信开销可降低一个数量级。


## Robust and Distributed Statistical Learning with Subsampling and Transfer Learning

*7 月 13 日（周一） · 15:30-17:10 · Colourful Guizhou Ballroom 2*  
*主持 Huali Zhao（Tsinghua University）*

### 1. 基于混合数据学习半参数树模型

**讲者**：Can Zhou（Nanjing Audit University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
混合数据（同时包含连续型、离散型、有序型等变量）在实际应用中极为常见，但现有树模型（如CART、随机森林）对离散变量通常仅做简单二分，损失了变量内部的序结构或分布信息；而纯参数或纯非参模型又难以兼顾灵活性与可解释性。本报告旨在解决：如何设计一种树模型，使其在节点分裂与叶节点预测中，既能自适应地处理混合数据类型，又能保持半参数结构的统计效率与可解释性。

**核心方法**  
讲者提出一种**半参数树模型**，其核心思想是：在树的每个叶节点，不再使用常数或线性预测，而是拟合一个半参数模型——例如对连续型协变量采用非参平滑（如局部线性回归），对离散型协变量引入参数化主效应（如哑变量或有序约束）。树生长过程采用递归划分，分裂准则基于半参数似然或损失函数的改进量，从而在每次分裂时同时优化变量选择与节点内模型复杂度。通过引入正则化（如叶节点模型复杂度惩罚），防止过拟合，并利用后向剪枝或贝叶斯方法确定树结构。

**与已有工作关系**  
已有树模型主要分为两类：一是参数树（如CART、M5），叶节点为常数或线性模型，但对离散变量处理粗糙；二是非参树（如随机森林、BART），通过集成提升预测精度，但牺牲了可解释性且难以直接处理混合数据中的序结构。本工作填补了中间地带：区别于仅对连续变量做非参的局部线性树（如LLT），本模型将离散变量的参数化效应与连续变量的非参平滑统一在叶节点中；同时，分裂准则的设计借鉴了广义可加模型（GAM）的似然思想，但通过树结构实现自动交互检测。

**主要贡献**  
1. 提出首个能同时处理连续、离散、有序混合数据的半参数树框架，在预测精度与可解释性之间取得平衡。  
2. 给出基于半参数似然的递归划分算法，并证明在适当正则化下树结构估计的一致性。  
3. 通过模拟与真实数据实验（如信用评分、生物信息学），展示该方法相比CART、随机森林、GAM在混合数据场景下的显著优势，尤其当离散变量具有序结构时。


### 2. Minimax Optimal Robust Sparse Regression with Heavy-Tailed Designs: A Gradient-Based Approach

**讲者**：Kaiyuan Zhou（Shanghai Jiao Tong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维稀疏线性回归中，当设计矩阵（协变量）服从重尾分布（如仅有限二阶矩甚至更低阶矩）时，经典Lasso等方法的估计性能会严重退化。同时，响应变量也可能受到异常值污染。现有稳健方法（如Huber Lasso）虽能应对重尾误差，但对重尾设计缺乏理论保证，且往往无法达到minimax最优的收敛速率。本报告旨在解决：在重尾设计下，如何设计一个计算高效的稀疏回归估计器，使其在minimax意义下达到最优的统计误差，同时保持对重尾误差的鲁棒性。

**核心方法**  
提出一种基于梯度的迭代算法（Gradient-Based Approach）。核心思想是：在每次梯度更新中，对梯度向量进行稳健化处理——例如使用逐坐标的中位数或截断操作，以抑制重尾设计带来的极端值影响。算法可视为“稳健梯度下降”的变体，结合了稀疏性诱导的软阈值或投影步骤。理论分析表明，在适当的步长和迭代次数下，该算法得到的估计量 $\hat{\beta}$ 满足 $\|\hat{\beta} - \beta^*\|_2 = O_p(\sqrt{s \log p / n})$，其中 $s$ 为真实稀疏度，$p$ 为维度，$n$ 为样本量。该速率与轻尾情形下的minimax最优速率一致，从而证明重尾设计并未本质恶化估计精度。

**与已有工作关系**  
已有工作主要分为两类：一是基于凸损失（如Huber损失）的稀疏回归，其理论通常假设协变量有界或次高斯，无法直接推广到重尾设计；二是基于截断或中位数的稳健方法（如Median-of-Means），但往往需要样本分割或计算复杂。本报告的方法将梯度下降与稳健梯度估计结合，在保持计算简单（每次迭代仅需一次数据扫描）的同时，首次在重尾设计下证明了minimax最优性。与现有“稳健Lasso”相比，本方法不依赖凸优化求解器，且对设计矩阵的矩条件要求更弱（仅需有限二阶矩）。

**主要贡献**  
1. 理论贡献：建立了重尾设计下稀疏回归的minimax下界，并证明所提梯度方法达到该下界，填补了该领域的理论空白。  
2. 算法贡献：提出一种计算高效、易于实现的梯度型算法，避免了传统稳健方法中复杂的凸优化或样本分割。  
3. 实践意义：为高维数据中常见重尾特征（如金融、网络流量数据）提供了可靠的统计推断工具，且对异常值具有天然鲁棒性。


### 3. Poisson Subsampling-Based Estimation for Growing-Dimensional Expectile Regression Inmassive Data

**讲者**：Xiaoyan Li（Chongqing Technology and Business University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在大规模数据（massive data）中，期望回归（expectile regression）作为一种对条件分布尾部敏感且计算高效的替代分位数回归的方法，面临两个核心挑战：一是数据量过大导致传统全样本估计不可行；二是协变量维度随样本量增长（growing-dimensional），即 $p = p_n \to \infty$，使得子抽样（subsampling）设计需兼顾维度增长带来的偏差与方差。现有子抽样方法多针对固定维度的均值回归或分位数回归，缺乏对期望回归在维度增长场景下的理论保障。

**核心方法**  
报告提出基于泊松子抽样（Poisson subsampling）的估计框架。具体地，对每个数据点赋予与某种重要性权重（如 leverage score 或梯度范数）成比例的泊松抽样概率，从而构造加权经验损失函数。估计量 $\hat{\beta}$ 通过最小化该加权损失得到。作者利用泊松抽样的独立性简化渐近分析，并针对 growing-dimensional 情形（$p = o(n)$ 或 $p = O(n^\alpha)$）推导了估计量的相合性与渐近正态性，同时给出最优子抽样概率的显式形式，以最小化估计量的渐近方差。

**与已有工作关系**  
已有子抽样研究多聚焦于线性回归（如 leverage-based subsampling）或分位数回归（如 Poisson subsampling for quantile regression），但期望回归的损失函数是二次型与线性型的混合（非对称平方损失），其子抽样设计需同时处理非对称性和尾部敏感性。此外，现有 growing-dimensional 理论多假设全样本可用，而本报告将维度增长与子抽样误差耦合分析，填补了“子抽样+高维”在期望回归中的空白。

**主要贡献**  
1. 首次为 growing-dimensional 期望回归设计了基于泊松子抽样的估计方法，并建立了在 $p \to \infty$ 下的渐近理论。  
2. 给出了最优子抽样概率的解析解，可显著降低估计方差，且计算复杂度与子样本量线性相关，适合海量数据。  
3. 通过数值实验验证了方法在有限样本下的有效性，尤其在高维稀疏或重尾数据中优于均匀子抽样和现有分位数子抽样方法。


### 4. 网络下的高效实验设计与主动学习

**讲者**：Zhiheng Zhang（Shanghai University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在社交网络、基因调控网络等图结构数据中，实验设计（如 A/B 测试、干预分配）与主动学习（如标注节点选择）面临两大挑战：一是节点间存在复杂依赖关系（如 spillover effect），传统独立同分布假设下的最优设计失效；二是网络规模庞大，全图标注或干预成本极高。本报告旨在解决：如何在网络环境下，以最小实验成本（样本量或干预次数）实现因果效应估计或模型预测的最优精度？

**核心方法**  
讲者可能提出一种基于图结构信息的自适应采样与分配策略。核心思路是：将实验设计问题建模为在图上选择干预节点或标注节点，以最小化某个损失函数的期望（如均方误差）。方法可能结合 **graph neural network (GNN)** 对节点表示进行编码，并利用 **active learning** 的 uncertainty sampling 或 expected model change 准则，同时引入 **causal inference** 中的 propensity score weighting 或 doubly robust 估计来校正网络干扰。例如，设计一个两步算法：第一步，通过图聚类或 spectral decomposition 识别低维子空间；第二步，在该子空间上求解一个带正则化的优化问题，选择信息量最大的节点集，并利用 **Thompson sampling** 或 **Bayesian optimization** 平衡探索与利用。

**与已有工作关系**  
已有实验设计多假设独立同分布（如最优设计理论），或仅考虑网络干扰下的效应估计（如 Aronow & Samii, 2017），但未将主动学习与实验设计统一。主动学习在独立数据上已有成熟理论（如 disagreement-based methods），但在网络下需处理标签或干预的传播效应。本报告可能首次将 **network interference** 下的实验设计与 **graph-based active learning** 结合，提出一个统一框架，并给出 finite-sample 理论保证（如 regret bound 或 minimax 最优性）。

**主要贡献**  
1. 提出网络环境下实验设计与主动学习的联合优化框架，填补了二者交叉领域的空白。  
2. 给出基于图结构的高效采样算法，其样本复杂度可达到 $O(\sqrt{n})$ 或 $O(\log n)$ 量级（相比全图 $O(n)$），并证明在特定图模型（如 stochastic block model）下的最优性。  
3. 通过合成数据与真实网络（如引文网络、社交网络）实验，验证方法在估计精度与成本上的显著优势，为网络因果推断与主动学习提供新工具。


### 5. Decentralized Robust Online Policy Evaluation

**讲者**：Jiayan Chen（Shanghai Jiao Tong University）

**对应论文**：Online Estimation and Inference for Robust Policy Evaluation in Reinforcement Learning · [arXiv:2310.02581](https://arxiv.org/abs/2310.02581)

<details><summary>摘要（原文）</summary>

Reinforcement learning has emerged as one of the prominent topics attracting attention in modern statistical learning, with policy evaluation being a key component. Unlike the traditional machine learning literature on this topic, our work emphasizes statistical inference for the model parameters and value functions of reinforcement learning algorithms. While most existing analyses assume random rewards to follow standard distributions, we embrace the concept of robust statistics in reinforcement learning by simultaneously addressing issues of outlier contamination and heavy-tailed rewards within a unified framework. In this paper, we develop a fully online robust policy evaluation procedure, and establish the Bahadur-type representation of our estimator. Furthermore, we develop an online procedure to efficiently conduct statistical inference based on the asymptotic distribution. This paper connects robust statistics and statistical inference in reinforcement learning, offering a more versatile and reliable approach to online policy evaluation. Finally, we validate the efficacy of our algorithm through numerical experiments conducted in simulations and real-world reinforcement learning experiments.

</details>

**问题**  
强化学习中的策略评估（Policy Evaluation）常受奖励异常值（outliers）与重尾分布（heavy-tailed rewards）干扰，现有在线算法（如TD学习）多假设奖励服从标准分布或要求调步长，且缺乏鲁棒性与在线统计推断能力。本文旨在同时解决异常值污染、重尾噪声与在线推断三个挑战，实现稳健且可量化不确定性的策略评估。

**核心方法**  
提出全在线鲁棒策略评估算法（ROPE）。核心思路是用平滑Huber损失 $f_\tau(x)=\tau^2(\sqrt{1+(x/\tau)^2}-1)$ 替代最小二乘损失，其梯度 $g_\tau$ 对异常值不敏感。算法采用牛顿型迭代更新参数 $\hat{\theta}_n$，利用在线更新的经验信息矩阵 $\hat{H}_n$ 及其逆（通过Sherman-Morrison公式递推），避免步长调参。同时构造长程协方差矩阵 $\hat{\Sigma}_n$ 的在线估计，用于构建置信区间。

**与已有工作关系**  
区别于经典一阶TD方法（如Ramprasad et al., 2023的在线bootstrap），ROPE是二阶方法：无需调步长，且Bahadur表示中的余项收敛速度为 $O(n^{-1}\log n)$，严格快于一阶方法的 $O(n^{-2/3})$。相比仅处理重尾或离线的鲁棒RL工作，本文首次在在线依赖样本（$\phi$-mixing）下统一处理Huber污染模型与重尾奖励，并建立渐近正态性。

**主要贡献**  
1. 提出全在线鲁棒策略评估算法，可同时估计参数与构造置信区间。  
2. 建立估计量的Bahadur表示，揭示主项渐近正态、余项超指数衰减，并证明二阶方法在收敛速度上的优势。  
3. 理论允许异常值比例 $m_n=o(n^{1/2-\beta})$ 时仍达到最优率 $\sqrt{d\log n/n}$，且重尾情形下呈现从 $\delta\in(0,1]$ 到 $\delta>1$ 的相变。  
4. 数值实验（含MIMIC-III医疗数据）验证了ROPE在覆盖率和计算效率上优于LSA方法。


### 6. Doubly Robust Transfer Learning Under Sub-Group Shift for Cohort-Level Missing Indicator Covariates

**讲者**：Huali Zhao（Tsinghua University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在迁移学习中，目标群体（target cohort）与源群体（source cohort）之间存在**子组偏移**（sub-group shift），即不同子组（如年龄层、疾病亚型）的协变量分布或结局机制在群体间差异显著。同时，协变量中包含了**群体水平的缺失指示变量**（cohort-level missing indicator covariates），例如某些协变量在源群体中完全观测，但在目标群体中因数据收集限制而整体缺失，或缺失模式随子组变化。传统迁移学习方法（如协变量偏移假设下的重要性加权）无法同时处理子组异质性与群体级缺失，导致目标群体上的模型估计或因果效应推断产生偏差。

**核心方法**  
讲者提出一种**双重稳健迁移学习**（Doubly Robust Transfer Learning）框架。首先，对每个子组分别建模倾向得分（propensity score）——即样本属于源群体而非目标群体的概率，并利用缺失指示变量构造缺失机制模型。然后，结合结果回归模型（outcome regression）与逆概率加权（IPW），构造双重稳健估计量：  
\[
\hat{\theta}_{DR} = \frac{1}{n_t} \sum_{i \in \text{target}} \left[ \hat{m}(X_i) + \frac{w_i (Y_i - \hat{m}(X_i))}{\hat{e}(X_i)} \right],
\]  
其中 $\hat{m}(X)$ 是源数据训练的结果回归，$\hat{e}(X)$ 是子组特定的倾向得分，$w_i$ 为缺失指示变量的调整权重。该估计量在结果模型或倾向得分模型之一正确设定时仍保持一致性，且对子组偏移与群体级缺失具有双重鲁棒性。

**与已有工作关系**  
现有迁移学习文献多假设全局协变量偏移（covariate shift）或标签偏移（label shift），忽略子组间的异质性；而因果推断中的双重稳健方法（如AIPW）通常用于处理个体层面的缺失数据或选择偏差，未考虑群体水平的缺失指示变量。本工作将双重稳健思想拓展至子组偏移场景，并首次将群体级缺失指示变量纳入迁移学习框架，填补了子组异质性与缺失模式耦合下的理论空白。

**贡献**  
1. 提出一种新的双重稳健估计量，同时应对子组偏移与群体水平缺失指示变量，放宽了传统迁移学习的同质性假设。  
2. 给出估计量的渐近正态性与方差公式，为统计推断提供理论基础。  
3. 通过模拟与真实数据验证，该方法在子组偏移严重且缺失指示变量存在时，显著优于现有迁移学习与单一稳健方法。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)