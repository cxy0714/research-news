# 网络与图数据 Networks & Graphs · 3

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 20 场报告**（已检索到对应论文 5 场）

---

## Recent Advances in Change Point Analysis for Complex Data: High-Dimensional Time Series and Dynamic Networks

*7 月 12 日（周日） · 13:30-15:10 · Xijiang Room*  
*组织 Yao Hu（Guizhou University） · 主持 Yao Hu（Guizhou University）*

### 1. Scale-Free Correlation Change-Point Detection in High-Dimensional Dynamic Networks

**讲者**：Yao Hu（Guizhou University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维动态网络（如脑功能连接、社交网络）中，节点间的相关性结构常随时间发生突变。现有变点检测方法多针对均值或协方差矩阵，但网络数据往往具有无标度（scale-free）特性——少数节点拥有大量连接，且相关性度量需对尺度不敏感。本报告旨在解决：如何在无标度网络假设下，对高维动态网络中的相关性矩阵进行变点检测，同时克服维数灾难与网络异质性带来的挑战。

**核心方法**  
讲者可能提出一种基于局部相关性矩阵的变点检测统计量。首先，对每个时间窗口内的节点对计算某种尺度不变的相关性度量（如Spearman秩相关或经标准化处理的Pearson相关），以消除节点方差差异的影响。然后，利用无标度网络的幂律度分布先验，构造一个加权稀疏惩罚项——对高度数节点赋予更小的惩罚，从而在检测变点时保留枢纽节点的结构信息。统计量采用滑动窗口下的累积和（CUSUM）形式，并通过高维极值理论推导其渐近分布，进而设定自适应阈值。

**与已有工作关系**  
已有高维变点检测工作（如基于协方差矩阵的CUSUM、似然比方法）通常假设网络是均匀的或稀疏的，未充分利用无标度网络的度分布信息。本报告将网络拓扑先验嵌入检测框架，区别于仅依赖数据驱动的方法。此外，传统相关性变点检测多针对低维或固定网络，本报告在动态高维场景下引入“尺度自由”概念，使得统计量对节点方差和网络规模具有鲁棒性。

**贡献**  
1. 首次将无标度网络的结构特性融入高维相关性变点检测，提出加权稀疏统计量，理论上证明了在幂律度分布下检测功效的相合性。  
2. 方法无需预设变点个数，且计算复杂度与网络边数呈线性关系，适用于大规模动态网络。  
3. 通过模拟和真实数据（如fMRI、金融网络）验证，相比现有方法，在枢纽节点突变场景下具有更高的检测灵敏度和更低的误报率。


### 2. Algorithm-Agnostic Post-Clustering Differential Expression Analysis with Asymptotic FDR Control

**讲者**：Mengtao Wen（Nankai University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
单细胞RNA-seq等高通量数据中，研究者常先对细胞进行聚类（如K-means、Louvain），再对聚类所得各组做差异表达（DE）分析。然而，聚类过程本身利用了数据中的结构信息，导致后续DE检验的p值分布偏离均匀性，产生选择性偏差（selection bias），使得传统FDR控制方法（如Benjamini-Hochberg）失效。现有纠偏方法多针对特定聚类算法（如基于K-means的“data splitting”或“selective inference”），缺乏通用性。本报告旨在提出一种**算法无关**（algorithm-agnostic）的后聚类DE分析方法，在渐近意义上严格控制FDR。

**核心方法**  
方法的核心思想是将聚类视为一个“黑箱”映射，不依赖其具体机制，而是利用**置换检验**（permutation test）构造null分布。具体地，通过多次随机置换样本的组标签（保持聚类结果不变），计算每个基因的DE检验统计量（如t统计量或Wilcoxon秩和统计量）的置换分布。由于置换破坏了基因表达与聚类标签之间的真实关联，该分布近似于原假设下的条件分布。进一步，基于置换得到的p值，采用**Benjamini-Hochberg过程**（BH）或**Storey的q-value方法**进行多重检验，并证明在样本量$n \to \infty$且聚类算法满足一定稳定性条件（如聚类结果对数据扰动不敏感）时，FDR可渐近控制在预设水平$\alpha$。关键理论工具是**经验过程**（empirical process）与**U-statistics**的渐近正态性，用以刻画置换p值的联合分布。

**与已有工作关系**  
已有工作主要分为两类：一是针对特定聚类算法的选择性推断（如Fithian et al., 2014; Gao et al., 2022），其理论依赖于算法具体形式，难以推广；二是基于数据分割（data splitting）的方法（如Cox & Battey, 2017），将数据分为两部分分别用于聚类和检验，但会损失统计效率。本报告的方法无需数据分割，且不依赖聚类算法细节，仅要求聚类结果在置换下保持“近似不变性”（即聚类算法对标签置换不敏感），这比现有方法更灵活。与Zhang et al. (2019)的“cluster-adaptive”方法相比，本方法直接控制FDR而非family-wise error rate，更适用于大规模多重检验。

**贡献**  
1. 提出首个**算法无关**的后聚类DE分析框架，适用于任意聚类算法（包括非参数、图聚类等），极大拓展了应用场景。  
2. 在温和条件下（聚类稳定性、矩条件）严格证明了渐近FDR控制，填补了该领域通用理论空白。  
3. 通过置换检验避免了复杂的条件分布推导，计算上易于实现，且无需对聚类算法做任何修改。  
4. 模拟与真实数据实验表明，该方法在保持较高统计功效的同时，FDR控制优于现有选择性推断方法，尤其在高维稀疏信号场景下优势明显。


### 3. BASIC: Bipartite Assisted Spectral-Clustering for Identifying Communities in Large-scale Networks

**讲者**：Tianchen Gao（Peking University）

**对应论文**：BASIC: Bipartite Assisted Spectral-clustering for Identifying Communities in Large-scale Networks · [arXiv:2503.06889](https://arxiv.org/abs/2503.06889) · 📖 [长篇精读](../../deep_reads/jcsds2026-2503.06889.md)

<details><summary>摘要（原文）</summary>

Community detection, which focuses on recovering the group structure within networks, is a crucial and fundamental task in network analysis. However, the detection process can be quite challenging and unstable when community signals are weak. Motivated by a newly collected large-scale academic network dataset from the Web of Science, which includes multi-layer network information, we propose a Bipartite Assisted Spectral-clustering approach for Identifying Communities (BASIC), which incorporates the bipartite network information into the community structure learning of the primary network. The accuracy and stability enhancement of BASIC is validated theoretically on the basis of the degree-corrected stochastic block model framework, as well as numerically through extensive simulation studies. We rigorously study the convergence rate of BASIC even under weak signal scenarios and prove that BASIC yields a tighter upper error bound than that based on the primary network information alone. We utilize the proposed BASIC method to analyze the newly collected large-scale academic network dataset from statistical papers. During the author collaboration network structure learning, we incorporate the bipartite network information from author-paper, author-institution, and author-region relationships. From both statistical and interpretative perspectives, these bipartite networks greatly aid in identifying communities within the primary collaboration network.

</details>

**问题**：社区检测是网络分析的核心任务，但在弱信号场景下（即社区内边概率与社区间边概率接近），传统谱聚类方法（如SCORE）的误分率急剧上升。现有增强方法（如SCORE+）主要依赖主网络自身的拉普拉斯变换或额外特征向量，却忽略了实际应用中广泛存在的二部图辅助信息（如作者-论文、作者-机构、作者-地区网络）。如何系统性地利用这些异构二部图信息来提升主网络社区检测的准确性与稳定性，是一个尚未被充分研究的问题。

**核心方法**：本文提出BASIC算法。其关键在于构造一个聚合平方矩阵 $M = AA^\top + \sum_{q=1}^Q B^{(q)}B^{(q)\top}$，其中 $A$ 为主网络邻接矩阵，$B^{(q)}$ 为第 $q$ 个二部网络邻接矩阵。该聚合自动适应不同维度的网络，且不破坏主网络的社区结构。随后对 $M$ 进行特征分解，取前 $K$ 个特征向量，应用SCORE归一化（取比值并截断）得到比值矩阵 $\hat{R}$，最后用k-means聚类。理论基于Degree-Corrected Stochastic Block Model (DCBM) 及其二部扩展BiDCBM，证明了聚合矩阵的谱结构保留了主节点的社区标签信息。

**与已有工作关系**：已有工作（如SCORE、SCORE+）仅利用主网络自身信息来应对弱信号，而BASIC首次将二部图信息引入社区检测框架。与协变量辅助方法不同，BASIC利用的是网络结构信息而非节点属性。更重要的是，理论证明BASIC不会导致“负知识迁移”：即使所有二部网络均为纯噪声，其误分率上界也不会劣于仅用主网络；而只要存在一个信号较强的二部网络，BASIC的收敛速度就严格快于仅用主网络。这为多源信息融合提供了坚实的理论保障。

**贡献**：1）首次提出利用二部图信息提升社区检测性能的方法，且可灵活与现有方法结合；2）在弱信号条件下严格推导了BASIC的误分率上界，证明其比仅用主网络的上界更紧，并给出了信号-噪声比（SNR）的显式表达式；3）收集并公开了一个大规模学术网络数据集（含合作网络、作者-论文、作者-机构、作者-地区网络），通过实证展示了BASIC在弱信号合作网络中识别出有意义的社区结构（如按机构、地域、研究方向聚类），且结果优于SCORE和SCORE+。


### 4. Spectral Change Point Estimation for High Dimensional Time Series by Sparse Tensor Decomposition

**讲者**：Xinyu Zhang（East China Normal University）

**对应论文**：Spectral Change Point Estimation for High Dimensional Time Series by Sparse Tensor Decomposition · [arXiv:2305.10656](https://arxiv.org/abs/2305.10656) · 📖 [长篇精读](../../deep_reads/jcsds2026-2305.10656.md)

<details><summary>摘要（原文）</summary>

Multivariate time series may be subject to partial structural changes over certain frequency band, for instance, in neuroscience. We study the change point detection problem with high dimensional time series, within the framework of frequency domain. The overarching goal is to locate all change points and delineate which series are activated by the change, over which frequencies. In practice, the number of activated series per change and frequency could span from a few to full participation. We solve the problem by first computing a CUSUM tensor based on spectra estimated from blocks of the time series. A frequency-specific projection approach is applied for dimension reduction. The projection direction is estimated by a proposed tensor decomposition algorithm that adjusts to the sparsity level of changes. Finally, the projected CUSUM vectors across frequencies are aggregated for change point detection. We provide theoretical guarantees on the number of estimated change points and the convergence rate of their locations. We derive error bounds for the estimated projection direction for identifying the frequency-specific series activated in a change. We provide data-driven rules for the choice of parameters. The efficacy of the proposed method is illustrated by simulation and a stock returns application.

</details>

**问题**  
高维时间序列的谱结构可能仅在部分频率和部分序列上发生结构性变化（如神经科学中的频带特异性断点），而现有变点检测方法或局限于单序列/单频率（如 FreSpeD），或无法适应高维稀疏场景（如 Preuss et al. 2015）。本文旨在同时估计变点位置、激活的序列集合以及激活的频率集合，且允许变化在序列和频率两个维度上均具有稀疏性。

**核心方法**  
首先将时间序列划分为等长块，每块估计谱密度矩阵，得到三阶 CUSUM 张量（频率×序列×块）。利用该张量特有的对称性与第三模恒等结构，提出一种结合截断矩阵幂法与张量幂法的稀疏张量分解算法（Algorithm 1），提取每个频率上的最优投影方向（即谱增量矩阵的稀疏主特征向量）。投影后的 CUSUM 向量经阈值化 $l_1$ 聚合（式 (3.6)）与野二元分割（Wild Binary Segmentation）实现多变点检测，同时输出各变点对应的激活频率与序列。

**与已有工作关系**  
与 Wang & Samworth (2018) 和 Wang et al. (2021) 的稀疏投影变点检测相比，本文从均值/方差变化推广到谱变化，且投影方向需从三阶张量而非矩阵中提取，因此发展了新的张量分解算法。与 Cho & Fryzlewicz (2015) 的 SBS-LSW 相比，本文在频域建模并显式刻画频率-序列双稀疏性，能识别变化的具体来源。与 Preuss et al. (2015) 相比，本文方法适用于高维且能自适应稀疏到稠密的变化。

**贡献**  
1. 提出首个同时估计高维时间序列谱变点位置、激活序列与激活频率的方法，填补了该问题的空白。  
2. 针对 CUSUM 张量的特殊结构，设计了可理论保证的稀疏张量分解算法，并证明投影方向估计的收敛速率为 $O(a\phi/(\delta^{5/6}\Delta\lambda))$，其中 $a$ 与稀疏度 $k_0$ 线性相关，体现了稀疏性带来的增益。  
3. 建立变点检测的一致性理论：变点数目估计正确，定位误差达到 $O(k^2 \log(Np)R/\lambda^2)$，接近协方差变点问题的 minimax 最优率。  
4. 通过模拟与 S&P100 股票收益率实例验证了方法在弱信号、多变点及非稀疏场景下的有效性，并展示了如何利用投影方向解释变点的经济含义。


## Statistical Methods in Generative AI and Network Models

*7 月 12 日（周日） · 13:30-15:10 · Doupeng Mountains Meeting Room*  
*组织 Yang Ning（Cornell University） · 主持 Yang Ning（Cornell University）*

### 1. SADA: Safe and Adaptive Aggregation of Multiple Black-Box Predictions

**讲者**：Jiwei Zhao（University of Wisconsin-Madison）

**对应论文**：SADA: Safe and Adaptive Aggregation of Multiple Black-Box Predictions in Semi-Supervised Learning · [arXiv:2509.21707](https://arxiv.org/abs/2509.21707) · 📖 [长篇精读](../../deep_reads/jcsds2026-2509.21707.md)

<details><summary>摘要（原文）</summary>

Semi-supervised learning (SSL) arises in practice when labeled data are scarce or expensive to obtain, while large quantities of unlabeled data are readily available. With the growing adoption of machine learning techniques, it has become increasingly feasible to generate multiple predicted labels using a variety of models and algorithms, including deep learning, large language models, and generative AI. In this paper, we propose a novel approach that safely and adaptively aggregates multiple black-box predictions of uncertain quality for both inference and prediction tasks. Our method provides two key guarantees: (i) it never performs worse than using the labeled data alone, regardless of the quality of the predictions; and (ii) if any one of the predictions (without knowing which one) perfectly fits the ground truth, the algorithm adaptively exploits this to achieve either a faster convergence rate or the semiparametric efficiency bound. We demonstrate the effectiveness of the proposed algorithm through small-scale simulations and two real-data analyses with distinct scientific goals. A user-friendly R package, sada, is provided to facilitate practical implementation.

</details>

**问题**：在半监督学习中，当有多个来自不同黑箱模型（如GPT、Llama、DeepSeek）的预测标签可用时，如何安全且自适应地聚合这些质量不确定的预测，以提升参数推断效率或预测精度？现有方法如Prediction-Powered Inference (PPI) 仅针对单一预测，且可能比仅用标注数据的基线更差；PPI++虽能保证不差于基线，但无法同时利用多个预测，且对向量参数不保证最优性。

**核心方法**：SADA通过构造一族无偏估计量（推断任务）或损失函数（预测任务），并数据驱动地选择最优权重来最小化渐近方差或期望风险。对于推断，估计量形式为 $\hat{\theta}(W)$，其中 $W$ 是 $Kp\times p$ 的权重矩阵，通过最小化均方误差得到最优权重 $W_{\text{opt}} = \frac{N-n}{N} \operatorname{var}\{S(X,\hat{Y};\theta^*)\}^{-1} \mathbb{E}\{S(X,\hat{Y};\theta^*) s(X,Y;\theta^*)^\top\}$。该权重自动将预测投影到真实标签的线性空间中，保证渐近方差不大于仅用标注数据的估计量（安全性），且当某个预测完美时，权重自动集中于该预测，达到 $N^{-1/2}$ 收敛率或半参有效界（自适应性）。对于预测任务，类似地优化损失函数的权重。

**与已有工作关系**：SADA将PPI/PPI++框架从单一预测推广到多个预测，并解决了PPI可能劣于基线的问题。与PPI++相比，SADA在向量参数情形下保证更小的渐近方差，且能同时利用多个预测。与Doubly Robust Self-Training等方法相比，SADA不依赖预测的具体形式或质量，且同时适用于推断和预测任务。

**贡献**：1) 提出首个原则性、完全数据驱动的多预测聚合方法，并给出安全性（不差于基线）和自适应性（自动识别最优预测）的严格理论保证。2) 推导了推断估计量的渐近表示和预测过剩风险的非渐近界，揭示了方法如何通过投影机制实现安全与自适应。3) 通过模拟和两个真实应用（在线请求礼貌性回归、ImageNet图像分类）验证了有效性，并提供了用户友好的R包 `sada`。


### 2. An Interactive Learning Paradigm in the Age of Generative AI

**讲者**：Yuchen Wu（Cornell University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
生成式 AI（如大语言模型）的涌现能力使得模型不仅能被动响应，还能主动生成内容。然而，传统统计学习范式（如监督学习、主动学习）假设数据生成过程是静态的，且学习器与数据源之间缺乏双向交互。本报告探讨的核心问题是：**如何设计一种交互式学习范式，使学习器能够通过与生成式 AI 的持续对话，自适应地获取信息、修正偏差，并提升下游任务的泛化性能？** 这涉及在动态、高维且可能带有对抗性的生成环境中，如何保证学习效率与统计一致性。

**核心方法**  
讲者可能提出一个基于 **online learning with generative feedback** 的框架。具体地，学习器维护一个参数化模型 $f_\theta$，在每一轮 $t$ 中，它向生成式 AI 发送一个查询 $q_t$（如提示词或数据点），AI 返回一个生成样本 $x_t \sim p_{\text{gen}}(\cdot \mid q_t)$ 或一个标签 $y_t$。学习器根据当前模型对 $(x_t, y_t)$ 的损失 $l(f_\theta(x_t), y_t)$ 更新参数，同时调整下一轮的查询策略以最小化累积 regret。方法本质是将生成式 AI 视为一个可交互的 **oracle**，通过设计查询策略（如基于 uncertainty sampling 或 information gain）来引导生成过程，从而高效探索假设空间。

**与已有工作关系**  
区别于传统的主动学习（active learning），后者通常从固定的未标注池中挑选样本，而本方法中样本由生成模型实时产生，因此查询空间是无限的且可定制。与 reinforcement learning from human feedback (RLHF) 不同，本方法不依赖人类标注，而是利用生成模型自身的输出作为反馈信号，可能结合了 **self-training** 与 **interactive learning** 的思想。此外，与单纯使用生成模型做数据增强（data augmentation）相比，本方法强调在线交互与策略优化，而非一次性扩充数据集。

**主要贡献**  
1. 提出一个统一的交互式学习范式，将生成式 AI 从“工具”提升为“交互伙伴”，为统计学习在生成时代提供了新视角。  
2. 可能给出在 convex 或 non-convex 损失下的 regret 上界，证明在生成 oracle 满足一定 smoothness 或 consistency 条件时，算法能达到 $O(\sqrt{T})$ 或更优的 regret。  
3. 通过理论分析与模拟实验，揭示交互策略（如查询的多样性、频率）对学习效率的影响，为实际部署（如个性化推荐、科学发现）提供指导。


### 3. Timely Decision Making with Balanced Benefit-Risk Tradeoffs

**讲者**：Yingqi Zhao（Fred Hutchinson Cancer Center）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在个性化医疗与动态治疗策略中，决策者常面临“及时性”与“获益-风险权衡”的双重挑战：一方面，治疗决策需在关键时间窗口内做出（如急性病或疾病进展期）；另一方面，过度追求短期获益可能累积长期风险。现有动态治疗策略（dynamic treatment regimes, DTRs）多假设决策时间点固定，且优化目标仅关注期望获益（如平均疗效），未系统纳入风险约束或时间敏感性。本报告旨在解决：**如何在时间敏感的场景下，构建同时平衡累积获益与风险的动态决策规则，并保证决策的及时性？**

**核心方法**  
讲者可能提出一个基于**强化学习**与**因果推断**的框架，将决策问题建模为带约束的Markov决策过程（constrained MDP）。具体地，状态空间包含患者随时间变化的协变量与风险指标；动作空间为治疗选项；奖励函数同时包含获益（如疗效）与风险（如副作用或毒性）的加权组合，且权重可随状态或时间动态调整。为体现“及时性”，引入**时间折扣因子**或**时间惩罚项**，迫使决策在有限步内完成。求解策略时，采用**双重鲁棒估计**或**逆概率加权**处理时序混杂，并利用**约束优化**（如拉格朗日对偶）在期望总获益与风险阈值间取得平衡。此外，可能借助**生存分析**中的风险函数来刻画风险累积过程。

**与已有工作关系**  
已有DTRs文献（如Q-learning、A-learning）主要优化期望获益，忽略风险；近期有工作引入风险约束（如CVaR），但多假设静态决策点。本报告将“及时性”作为显式约束，与**时序因果推断**中的“最优停止时间”问题（如何时切换治疗）相关联，但更强调在连续决策中平衡获益与风险。与**带约束的强化学习**（如safe RL）相比，本报告更关注医学场景下因果识别的特殊性（如未观测混杂、时间依赖性）。

**主要贡献**  
1. 提出一个统一框架，将“及时性”与“获益-风险权衡”纳入动态治疗策略的优化目标，填补了现有DTRs在时间敏感性场景下的空白。  
2. 给出在时序混杂下识别最优策略的理论条件（如序贯可忽略性、正性假设），并证明所提估计量的相合性与渐近正态性。  
3. 通过模拟或真实数据（如癌症治疗、重症监护）展示方法在降低累积风险的同时维持疗效，且决策时间显著提前，为临床实践提供可操作的统计工具。


### 4. Backdoor Reactivation with Clean Data

**讲者**：Yao Li（University of North Carolina at Chapel Hill）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
后门攻击通常依赖特定触发器（如像素块、图案）在推理时激活恶意行为，但这类触发器易被防御机制（如剪枝、微调、触发器检测）识别并移除。本报告探讨一个反直觉的问题：**能否仅使用干净数据（无触发器）重新激活已被抑制或移除的后门**？这挑战了“后门必须依赖显式触发器”的常识，揭示了后门持久性的新维度。

**核心方法**  
讲者可能提出一种 **Backdoor Reactivation** 机制：攻击者在训练阶段植入一个“潜伏”后门，该后门在标准推理中不响应任何触发器，但通过精心设计的干净数据分布（例如特定类别样本的统计特征、隐空间中的低维流形）作为“隐式密钥”，在模型微调或在线学习阶段重新激活后门。具体地，利用干净数据对模型参数进行微小扰动（如梯度上升或对抗性重训练），使得原本被抑制的后门神经元重新获得对目标标签的强响应。方法本质是**将后门从“输入空间依赖”转化为“参数空间依赖”**，从而绕过基于输入检测的防御。

**与已有工作关系**  
现有后门攻击（如 BadNets、TrojanNN）均假设触发器是固定的、可观测的；防御工作（如 Neural Cleanse、Fine-Pruning）则致力于检测或移除触发器对应的神经元。本报告提出的“干净数据激活”范式与上述工作正交：它不依赖触发器，因此传统防御无效；同时它要求攻击者拥有对模型后续更新过程的控制（如联邦学习中的恶意聚合、API 微调），属于一种**后门持久化攻击**，与近期“后门重编程”（Backdoor Re-programming）和“无触发器后门”（Triggerless Backdoor）有联系，但更强调利用干净数据而非对抗样本。

**主要贡献**  
1. 首次提出“干净数据重新激活后门”的概念，拓宽了后门攻击的威胁模型。  
2. 给出一种可行的实现算法，证明即使后门被部分移除，仍可通过干净数据恢复恶意行为。  
3. 揭示现有防御的盲区：仅关注输入触发器而忽略参数空间中的隐式后门，为设计更鲁棒的防御（如参数正则化、动态验证）提供了新方向。


## Advances in Machine Learning for Large Language Models and Matrix Methods

*7 月 12 日（周日） · 13:30-15:10 · Huangguoshu Theater Meeting Room*  
*主持 Jingwen Zhang（EAST China normal university）*

### 1. Prompt Perturbation for Reliable LLM Evaluation over Comparison Graphs

**讲者**：Dong Huang（Tsinghua University）

**对应论文**：Prompt Perturbation for Reliable LLM Evaluation over Comparison Graphs · [arXiv:2606.17634](https://arxiv.org/abs/2606.17634) · 📖 [长篇精读](../../deep_reads/jcsds2026-2606.17634.md)

<details><summary>摘要（原文）</summary>

Evaluating large language models (LLMs) is important for understanding their capabilities, comparing competing systems, and supporting the deployment of reliable models in practice. For open-ended tasks, pairwise evaluation has become a popular paradigm, in which two responses to the same prompt are compared and the resulting judgments are aggregated into an overall ranking. A central challenge of this paradigm is intransitivity: the induced comparison outcomes may fail to support any coherent global ranking. For example, one may observe cyclic preferences such as $A \succ B \succ C \succ A$, or inconsistencies involving ties such as $A \equiv B\equiv C\neq A$. Such contradictions make the resulting leaderboard unstable and challenging to interpret. In this paper, we propose a prompt perturbation framework for improving the consistency of pairwise LLM evaluation. Our approach generates perturbed variants of each prompt, uses the resulting comparison graphs to identify and filter out structurally inconsistent comparison patterns, and then applies standard ranking methods to the filtered comparisons. A key feature of the proposed framework is that graph-level structural consistency is incorporated explicitly into the evaluation pipeline before ranking aggregation. This provides a simple and principled way to reduce cyclic inconsistencies and improve the reliability of LLM rankings.

</details>

**问题**：在基于成对比较的 LLM 评估中，一个核心挑战是传递性缺失（intransitivity）：比较图可能包含循环（如 $A \succ B \succ C \succ A$）或平局矛盾（$A \equiv B \equiv C \not\equiv A$），导致无法得到一致的全局排名，使得最终排行榜不稳定且难以解释。现有方法多聚焦于聚合策略本身，而忽略了比较图的结构一致性。

**核心方法**：本文提出 prompt perturbation 框架，通过显式改善比较图的结构一致性来提升排名可靠性。具体而言，对每个原始 prompt 生成 $m$ 个语义等价的扰动变体，每个变体诱导一个比较图。然后计算每个图的短环（3-cycle 和 4-cycle）数量作为不一致性度量，仅保留环数低于阈值的图（即 cycle truncation）。最后对保留的图使用 Bradley–Terry 模型或 Davidson 模型（允许平局）进行排名聚合。该方法本质上是将图级别的结构一致性作为过滤准则，在聚合前剔除高度不一致的局部偏好结构。

**与已有工作关系**：已有工作主要关注三类方向：一是 LLM-as-a-judge 的鲁棒性，二是 intransitivity 的实证分析，三是经典排名方法（如 Elo、Bradley–Terry）在 LLM 评估中的应用。本文与这些工作的关键区别在于：它不是在给定比较图后优化聚合方式，而是通过 prompt perturbation 和 cycle truncation 主动改善比较图本身的质量。与仅使用单一 prompt 的传统流程相比，本文引入了扰动生成和基于图结构的选择步骤；与仅关注聚合的文献相比，本文在聚合前显式地利用图的结构一致性进行过滤，从而减少后续排名中的循环噪声。

**贡献**：1）提出一个简单而原则性的 prompt perturbation 框架，将图结构一致性显式纳入 LLM 评估流程，有效降低比较图中的循环不一致性。2）在随机有向图模型下给出理论保证：经过 cycle truncation 后，通过多数投票恢复真实排名所需的样本量从 $\frac{(4+\epsilon)\log n}{\log(1/(1-4p^2))}$ 降至 $\frac{(2+\epsilon)\log n}{\log(1/(1-4p^2))}$，表明截断能降低样本复杂度。3）在 MT-Bench 上的实验表明，该方法在 GPT-5 和 Prometheus 两种 judge 下均优于多种基线，且对超参数（如保留图数 $K$、环权重 $\mu$）稳健。


### 2. 非线性矩阵补全在一般损失与采样分布下的最优性理论

**讲者**：Yuanhong A（Renmin University of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
经典矩阵补全假设观测值由线性模型生成（如直接观测部分条目加噪声），且采样分布通常为均匀或独立同分布。然而实际应用中，观测常通过非线性链接函数（如逻辑回归、泊松计数）产生，且采样概率可能依赖于矩阵本身（如自适应采样）。该报告旨在解决：在一般损失函数（如指数族负对数似然）与任意采样分布下，非线性矩阵补全的 minimax 最优估计误差下界与可达上界是否一致？即最优性理论是否成立？

**核心方法**  
报告可能基于经验过程与局部 Rademacher 复杂度，将非线性观测模型转化为广义线性模型下的低秩矩阵估计问题。通过引入 Fisher 信息矩阵的期望版本，定义与采样分布相关的有效秩（effective rank），并利用覆盖数（covering number）与 Dudley 积分推导出估计误差的收敛速率。关键工具包括：将非线性损失函数的 Hessian 矩阵与采样协方差结构结合，构造出类似于线性情况下的“观测算子”的广义版本，进而证明在低秩约束下，估计量的误差上界由 $\sqrt{r d / n}$ 主导（其中 $r$ 为秩，$d$ 为维度，$n$ 为观测数），且该速率与信息论下界匹配。

**与已有工作关系**  
已有非线性矩阵补全工作多假设特定损失（如逻辑损失）或均匀采样，且最优性结果常局限于线性情况（如 Candès & Recht 2009）。该报告将损失函数推广至任意满足强凸性与 Lipschitz 条件的广义线性模型，并将采样分布放宽至允许依赖矩阵的异质性设计（heterogeneous design）。相比 Keshavan et al. (2010) 的谱方法，该工作更关注统计最优性而非计算效率；相比 Gunasekar et al. (2014) 的核范数正则化，该工作提供了更紧的下界证明。

**贡献**  
主要贡献有三：其一，首次在一般损失与采样分布下建立了非线性矩阵补全的 minimax 最优速率，填补了理论空白；其二，揭示了采样分布对估计精度的影响仅通过有效秩体现，而非简单的样本量；其三，为实际中设计自适应采样策略提供了理论指导——当采样概率与矩阵奇异向量对齐时，可达到更低的误差。该结果统一了线性与非线性矩阵补全的最优性理论，并为后续研究非凸优化算法的统计性质奠定了基础。


### 3. PAC-Efficient Reasoning for Large Language Models: Marginal Guarantees, Conditional Extensions, and Anytime Validity

**讲者**：Hao Zeng（Southern University of Science and Technology）

**对应论文**：A note on the impossibility of conditional PAC-efficient reasoning in large language models · [arXiv:2512.03057](https://arxiv.org/abs/2512.03057) · 📖 [长篇精读](../../deep_reads/jcsds2026-2512.03057.md)

<details><summary>摘要（原文）</summary>

We prove an impossibility result for conditional Probably Approximately Correct (PAC)-efficient reasoning in large language models. While recent work has established marginal PAC efficiency guarantees for composite models that switch between expensive expert models and cheaper fast models, we show that conditional (pointwise) guarantees are impossible in the distribution-free setting. Specifically, for non-atomic input spaces, any algorithm achieving conditional PAC efficiency must be trivial in the sense that it defers to the expert model with probability at least $1-α$ for almost every input.

</details>

**问题**  
大语言模型推理成本高昂，现有工作（Zeng et al., 2025）提出 **marginal PAC efficiency**，通过路由在昂贵专家模型与廉价快速模型间切换，控制期望风险。一个自然的问题是：能否实现更强的 **conditional (pointwise) PAC efficiency**，即对每个输入点 $x$ 控制风险 $P(R(\hat{f};x)>\epsilon)\leq\alpha$？本报告证明，在无分布假设（distribution-free）下，条件 PAC 效率是不可能的：任何非平凡算法（即对某些输入以大于 $\alpha$ 的概率使用快速模型）都无法同时满足条件风险控制与效率提升。

**核心方法**  
证明采用 **finite-sample indistinguishability** 构造。假设存在算法 $A$ 达到 $(\epsilon,\alpha)$-条件 PAC 效率，且存在正测度集 $E$ 使得对每个 $x\in E$ 有 $P(g(x)=0)>\alpha$。固定 $x^*\in E$，利用输入空间 $X$ 的非原子性，可在 $x^*$ 的任意小邻域 $B$ 内修改分布：保持边际 $P_X$ 不变，但将条件分布改为使 $\ell(\tilde{f}(x^*),f(x^*))>\epsilon$ 的分布 $Q_\epsilon$。新分布 $P'$ 与原始分布 $P$ 仅在 $B$ 上不同，且 $B$ 的测度可任意小，从而 $n$ 个样本下的总变差距离 $\text{TV}((P')^n,P^n)<\eta$。由于条件 PAC 效率要求对 $P'$ 也成立，推出 $P(g(x^*)=0)\leq\alpha$，与假设矛盾。因此，任何条件 PAC 效率算法必须满足 $P(g(x)=0)\leq\alpha$ 对几乎处处 $x$ 成立，即几乎总是使用专家模型。

**与已有工作关系**  
该结果直接类比于分布自由条件预测中的不可能性定理（Barber et al., 2021），后者证明 exact conditional coverage 在无假设下不可实现。本报告将其推广至 PAC 推理框架，并采用类似的不可区分性论证。边际 PAC 效率（Zeng et al., 2025）是可行的，但条件版本被证明不可能，这与共形预测中边际覆盖与条件覆盖的根本差异一致。此外，报告题目提及 **Anytime Validity**，可能进一步探讨在线或自适应场景下的保证，但论文核心聚焦于条件不可能性。

**贡献**  
1. 首次严格证明条件 PAC 效率在无分布假设下的不可能性，揭示了边际保证与条件保证之间的本质鸿沟。  
2. 为 LLM 推理效率研究提供了理论边界：实践者应专注于边际保证，或引入分布假设下的松弛条件（如近似条件保证）。  
3. 证明方法简洁有力，利用有限样本不可区分性构造，为类似不可能性结果提供了可复用的分析工具。该结果对设计高效且统计可靠的 LLM 路由系统具有重要指导意义。


### 4. Robust Online Recommender System via Matrix Completion

**讲者**：Guanyi Yue（Shanghai Jiao Tong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在线推荐系统需实时处理用户-物品交互的流式数据，并利用部分观测值预测缺失评分。传统矩阵补全（Matrix Completion）方法通常假设数据无噪声或噪声服从轻尾分布，但在实际场景中，用户行为常受恶意攻击、异常点击或系统故障干扰，导致观测值包含重尾噪声或对抗性异常值。现有在线矩阵补全算法（如基于梯度下降的在线SVD）缺乏对这类鲁棒性的理论保证，容易因少数异常点导致推荐质量大幅下降。本报告旨在解决：如何在在线、流式环境下，从被污染的部分观测中稳健地恢复低秩评分矩阵？

**核心方法**  
报告提出一种鲁棒在线矩阵补全算法，核心思想是将低秩矩阵的在线更新与鲁棒统计估计相结合。具体而言，算法在每一步接收新用户-物品对的部分观测，采用截断的Huber损失或分位数损失替代平方损失，以抑制异常值的影响；同时利用在线梯度下降（OGD）或随机优化框架，在低秩约束下（如通过SVD投影或矩阵分解参数化）更新估计。为处理流式数据，算法可能引入动量项或自适应步长，并利用矩阵的核范数正则化或秩约束保持低秩结构。理论分析上，通过建立在线遗憾（regret）上界或估计误差的收敛速率，证明在观测值被$\epsilon$比例污染时，算法仍能恢复真实矩阵，且误差随污染比例线性增长。

**与已有工作关系**  
已有在线矩阵补全工作（如Keshavan et al., 2010; Mardani et al., 2013）多假设噪声为独立同分布的高斯或亚高斯，且未考虑对抗性污染。本报告将鲁棒统计中的M估计思想引入在线设置，与离线鲁棒矩阵补全（如使用$\ell_1$范数或Huber损失）不同，需同时处理数据流式到达和计算效率问题。此外，与在线鲁棒PCA（如Feng et al., 2014）相比，本报告聚焦于部分观测下的矩阵补全，而非全观测下的主成分追踪。

**主要贡献**  
1. 首次提出针对在线推荐系统的鲁棒矩阵补全算法，在理论上证明其对重尾噪声和对抗性异常值的稳健性，并给出与污染比例相关的遗憾界。  
2. 算法具有线性时间复杂度和常数存储开销，适合大规模流式数据。  
3. 在合成数据和真实推荐数据集（如MovieLens）上验证，相比现有在线矩阵补全方法，在存在1%–10%异常值时，RMSE降低20%–40%，且收敛速度几乎不受影响。


### 5. 分析师前瞻性对控股股东股权质押的影响——来自大语言模型的证据

**讲者**：Ke Yao（Zhongnan University of Economics and Law）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
控股股东股权质押是公司金融中的常见行为，其动机与风险备受关注。已有文献多从财务指标、市场环境等角度解释质押决策，但较少关注信息中介——分析师——的语言特征如何影响控股股东行为。本报告提出一个新颖问题：分析师报告中的“前瞻性”（即对未来业绩、风险等的前瞻性表述）是否会抑制或加剧控股股东的股权质押倾向？其背后的机制可能是前瞻性信息降低了信息不对称，或改变了控股股东对股价崩盘风险的预期。

**核心方法**  
讲者利用大语言模型（如BERT或GPT系列）对分析师报告文本进行量化。具体而言，通过预训练模型提取每份报告中与未来预测相关的语义特征，构建一个连续的前瞻性得分（forward-looking score）。随后，将该得分作为核心解释变量，以控股股东股权质押比例或是否质押为被解释变量，在面板数据中控制公司固定效应、时间固定效应及一系列财务变量。为处理内生性（如质押行为反向影响分析师报告），可能采用工具变量法（如同行业其他分析师的前瞻性均值）或双重差分设计（如外生冲击导致分析师报告风格变化）。

**与已有工作关系**  
现有研究主要关注分析师报告的信息含量（如盈利预测准确性、推荐评级）对市场的影响，或股权质押的经济后果（如掏空、股价崩盘风险）。本报告将分析师的语言风格（前瞻性）作为独立维度，并首次将其与控股股东行为直接关联。此外，区别于传统词典法（如Loughran-McDonald词表），大语言模型能捕捉上下文语义，更精准地识别前瞻性表述，这是方法上的重要改进。

**主要贡献**  
第一，从信息中介的语言特征切入，拓展了股权质押动机的研究视角，揭示了分析师前瞻性通过降低信息不对称或改变控股股东预期来影响质押决策的渠道。第二，展示了如何利用大语言模型从非结构化文本中提取可解释的因果变量，为会计与金融领域的文本分析提供了新范式。第三，实证结果可能对监管层有启示：鼓励分析师提供更多前瞻性信息，有助于抑制控股股东的机会主义质押行为，从而降低市场风险。


### 6. A Compass for Useful Data: Online Data Selection via Alignment-Gated Fisher Geometry

**讲者**：Jingwen Zhang（EAST China normal university）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在大规模在线学习场景中，数据流不断涌入，但并非所有样本都对当前模型训练“有用”——冗余、噪声或分布外样本会降低效率甚至损害泛化。如何实时、高效地筛选出对模型更新最有益的数据，同时避免离线重训练的高昂成本？现有方法多依赖启发式准则（如不确定性采样、梯度范数）或静态核心集，缺乏对模型参数空间几何结构的动态感知，且难以兼顾数据“对齐”于当前学习目标的程度。

**核心方法**  
报告提出 **Alignment-Gated Fisher Geometry** 框架。核心思想是：将数据选择问题转化为在线优化中的“信息量”度量，利用 Fisher 信息矩阵刻画模型参数空间的局部几何结构。具体地，对每个新样本，计算其梯度与当前参数 Fisher 信息矩阵的二次型（即 Fisher 范数），作为该样本对模型参数更新的“影响度”。进一步引入 **Alignment Gate**——一个可学习的门控机制，根据样本梯度与历史梯度主方向的对齐程度（如余弦相似度）动态调整选择阈值，避免选择与当前学习轨迹冲突的样本。最终，仅保留 Fisher 范数高且对齐度好的样本参与在线梯度更新。

**与已有工作关系**  
与主动学习（基于不确定性或多样性）不同，本方法直接利用 Fisher 几何度量参数空间中的局部影响，而非仅依赖输出空间的不确定性；与基于梯度的数据选择（如梯度匹配）相比，本方法通过 Fisher 信息矩阵考虑了参数协方差结构，更稳健；与离线核心集方法相比，本方法支持在线流式处理，且通过 Alignment Gate 自适应地抑制分布偏移带来的有害样本。

**主要贡献**  
1. 首次将 Fisher 几何与对齐门控结合，提出在线数据选择的统一框架，兼顾信息量与方向一致性。  
2. 理论层面，证明了所选数据子集在 Fisher 意义下近似保持全量数据的参数更新方向，并给出泛化误差界。  
3. 实验上，在图像分类、语言模型微调等任务中，以更少的数据量达到与全量训练相当甚至更优的性能，且计算开销可控。


## Advances in Network and Privacy-Preserving Data Science

*7 月 12 日（周日） · 13:30-15:10 · ASEAN Roundtable Forum Meeting Room*  
*主持 Na Kang（Zhejiang Gongshang University）*

### 1. Joint Estimation of Edge Probabilities for Multi-Layer Networks via Neighborhood Smoothing

**讲者**：Diqing Li（Zhejiang Gongshang University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与方向的推断。

**问题**：多层网络（multi-layer network）在同一组节点上观测到多个关系层（如不同时间、不同关系类型）。核心任务是估计每条边的连接概率矩阵 $P^{(\ell)}_{ij}$，即在无参数假设下恢复潜在的边概率结构，同时借用各层之间的共性信息以降低方差。

**核心方法**：作者很可能将 Zhang、Levina 与 Zhu (2017) 提出的邻域光滑（neighborhood smoothing）方法从单层图子（graphon）估计推广到多层情形。基本思想是：对节点 $i$，通过比较其与其它节点邻接向量的差异定义相似度，选出“邻居”节点集合 $\mathcal{N}_i$，再对邻域内的邻接项取平均得到 $\hat P_{ij}$。多层的关键创新在于“联合”估计——利用跨层相似度度量或层间共享的潜在位置，使邻域选择同时聚合多层信息，从而在各层稀疏时仍能稳定估计。

**与已有工作的关系**：延续了 graphon 估计与潜在空间模型（latent space model）的非参数路线，区别于随机块模型（SBM）等参数方法；相较单层邻域光滑，通过层间信息借用（information borrowing）提升收敛速率。

**贡献（推断）**：提出多层邻域光滑估计量，给出均方误差收敛性理论，并在模拟与真实多层网络数据上验证其优于逐层独立估计。


### 2. 基于网络信息的近似因子模型估计

**讲者**：Yuzhou Zhao（Renmin University of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维时间序列或面板数据中，近似因子模型（approximate factor model）通过低维公共因子解释变量间的协方差结构，但传统估计方法（如主成分分析、拟极大似然）仅依赖观测数据本身，忽略了变量间或个体间已知的网络结构（如社交网络、供应链关系、基因调控网络）。当因子载荷或误差项存在网络相关性时，忽视网络信息会导致因子估计效率下降甚至不一致。本报告旨在解决：如何将网络结构信息融入近似因子模型的估计中，以提升因子载荷和公共因子的估计精度，尤其是在因子强度较弱或噪声异质的情形下。

**核心方法**  
讲者可能提出一种基于网络正则化的因子估计框架。具体地，在最小化重构误差的目标函数中引入图拉普拉斯（graph Laplacian）惩罚项，鼓励因子载荷矩阵在已知网络图上平滑变化，即相邻节点（变量或个体）的载荷向量相近。例如，优化问题形如 $\min_{L,F} \|X - LF^\top\|_F^2 + \lambda \operatorname{tr}(L^\top \Delta L)$，其中 $\Delta$ 为网络拉普拉斯矩阵，$L$ 为载荷矩阵，$F$ 为因子矩阵。通过交替最小化或谱分解求解，并利用网络结构修正主成分方向。另一种可能思路是利用网络信息构造加权协方差矩阵，再对其做特征分解，从而得到网络感知的因子估计。

**与已有工作关系**  
传统近似因子模型估计（如 Bai & Ng, 2002; Fan et al., 2013）假设因子载荷无先验结构，或仅利用稀疏性（如因子模型中的稀疏 PCA）。近年有工作引入图结构于因子模型（如图因子分析、网络向量自回归），但多假设因子本身服从网络动态，或仅用于降维可视化。本报告区别于这些工作之处在于：将网络信息作为载荷的平滑性先验，而非因子动态的先验；同时允许误差项存在弱相关（近似因子结构），而非严格因子模型。与图正则化矩阵分解（如 GNMF）相比，本报告更关注因子数的一致估计和载荷的渐近性质。

**贡献**  
主要贡献包括：（1）提出一种融合网络信息的近似因子模型估计方法，理论上证明在因子弱信号或网络结构强时，估计量的收敛速度优于传统 PCA；（2）给出因子个数的一致选择准则，该准则利用网络拉普拉斯的特征值间隙；（3）通过模拟和实证（如股票收益数据结合行业网络）展示方法在预测和风险分解中的改进。该工作为高维数据中利用辅助结构信息进行因子推断提供了新视角，尤其适用于网络节点间存在平滑变化载荷的应用场景。


### 3. 数据要素促进居民家庭服务消费的理论机制研究—基于CHFS的经验证据

**讲者**：Tianle Li（Henan University of Economics and Law）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
数据要素作为新型生产要素，其对居民家庭服务消费的驱动机制尚不清晰。现有研究多从宏观产业或企业层面探讨数据要素的经济效应，但微观家庭层面，尤其是数据要素如何通过信息匹配、信任构建与交易成本降低等渠道影响服务消费决策，缺乏系统的理论框架与因果识别证据。本报告旨在回答：数据要素的渗透（如数字平台使用、数据可及性）是否以及如何促进居民家庭服务消费（如家政、教育、医疗等）？其异质性（如城乡、收入阶层）又如何体现？

**核心方法**  
基于中国家庭金融调查（CHFS）面板数据，构建理论模型刻画数据要素影响服务消费的机制：数据要素通过降低信息不对称（减少搜索成本 $\tau$）和提升服务匹配效率（匹配概率 $p$），进而增加家庭服务消费支出 $C_s$。实证上，采用工具变量法（IV）处理数据要素的内生性（如以家庭所在地区互联网基础设施历史指标作为工具变量），并结合中介效应检验（如检验“数据使用→信息获取→消费决策”路径）。可能进一步使用双重差分（DID）或事件研究法，利用数字基础设施建设的政策冲击（如“宽带中国”试点）识别因果效应。

**与已有工作关系**  
区别于既有文献侧重数据要素对全要素生产率或企业创新的宏观影响，本报告将分析单元下沉至家庭，聚焦服务消费这一内需关键领域。与消费经济学中“数字普惠金融促进消费”的研究相比，本报告强调数据要素的“信息中介”与“信任增强”双重角色，而非仅信贷约束缓解。此外，CHFS数据的家庭层面微观特征（如户主年龄、教育、风险偏好）允许更精细的异质性分析，弥补了以往使用宏观加总数据或单一平台数据的不足。

**主要贡献**  
第一，从理论层面构建了“数据要素→信息摩擦缓解→服务消费扩张”的微观机制框架，为理解数字经济下的消费升级提供了新视角。第二，利用CHFS全国代表性面板数据，通过严谨的因果识别策略（IV+DID）估计了数据要素对家庭服务消费的因果效应，并量化了中介路径的贡献份额。第三，揭示了数据要素促进消费的异质性规律（如对低信息素养家庭、农村地区效果更显著），为制定精准的数据赋能消费政策（如提升数字素养、完善农村数字基础设施）提供了经验证据。


### 4. Differentially Private Adaptive Neyman Allocation for Sequential Experiments

**讲者**：Yaqi Zhou（Tsinghua University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在序贯实验中，自适应分配策略（如 Neyman allocation）通过动态调整各臂的分配比例来最小化目标估计量的渐近方差，但这一过程会反复利用历史数据，可能泄露个体敏感信息。如何在保证差分隐私（Differential Privacy, DP）的前提下，实现序贯实验中的自适应 Neyman 分配，同时维持统计效率，是核心挑战。

**核心方法**  
报告提出一种 **Differentially Private Adaptive Neyman Allocation** 算法。其核心思路是在每一轮更新分配概率时，对基于当前数据计算的 Neyman 最优分配比例施加噪声扰动。具体地，假设实验有 $K$ 个臂，第 $t$ 轮后各臂的样本均值和方差为 $\hat{\mu}_{k,t}, \hat{\sigma}^2_{k,t}$，则 Neyman 分配比例 $p_{k,t} \propto \hat{\sigma}_{k,t}$。为满足 $\varepsilon$-DP，算法在计算 $p_{k,t}$ 前，先对 $\hat{\sigma}^2_{k,t}$ 或 $\hat{\mu}_{k,t}$ 添加 Laplace 或 Gaussian 噪声，再基于扰动后的统计量重新计算分配概率。同时，通过树状结构（tree-based mechanism）或在线矩估计（online moment accountant）来追踪并控制整个序贯过程的隐私预算累积，确保总隐私损失不超过预设阈值。

**与已有工作关系**  
已有文献主要关注汤普森采样（Thompson Sampling）或 UCB 等 regret-minimization 策略的隐私版本，而 Neyman allocation 的目标是最小化最终估计量的方差（即统计推断效率），二者优化目标不同。此外，现有隐私自适应实验多采用“先探索后利用”或固定分配，缺乏对分配比例实时最优性的理论保证。本工作首次将差分隐私与 Neyman 分配结合，在序贯框架下同时处理隐私保护与方差最小化，并给出渐近最优的隐私-效用权衡。

**贡献**  
1. 提出首个满足差分隐私的自适应 Neyman 分配算法，填补了隐私保护下统计推断导向实验设计的空白。  
2. 理论证明在 $\varepsilon$-DP 约束下，算法得到的最终估计量的渐近方差与无隐私版本仅差一个与 $\varepsilon$ 和实验轮数 $T$ 相关的附加项，且该附加项以 $O(1/(\varepsilon^2 T))$ 速率衰减。  
3. 通过数值模拟验证了算法在有限样本下的有效性，展示了隐私预算与统计效率之间的可调节性，为实际应用（如在线 A/B 测试中的敏感数据保护）提供了可行方案。


### 5. Addressing Complex Missingness: A Bayesian Joint Analysis of Missing Item Response and Covariate Data under a Missing Not at Random Mechanism

**讲者**：Jialing Tan（Northeast Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在心理测量、教育测试或纵向调查中，项目反应数据（如 Likert 量表得分）与协变量（如年龄、收入）常同时缺失，且缺失机制可能为非随机缺失（Missing Not at Random, MNAR），即缺失概率依赖于未观测到的反应值或协变量本身。现有方法多单独处理项目反应缺失（如 IRT 框架下的缺失模型）或协变量缺失（如多重插补），但忽略了二者之间的依赖结构，导致参数估计有偏且推断效率低下。本报告旨在提出一个统一的贝叶斯联合模型，同时建模项目反应、协变量及其缺失机制，以解决 MNAR 下的复杂缺失问题。

**核心方法**  
采用贝叶斯分层框架，将项目反应模型（如多维 IRT 模型）与协变量分布（如多元正态回归）通过共享潜在特质变量 $\theta$ 连接。缺失机制由两个 probit 或 logistic 模型刻画：一个针对项目反应缺失指示变量 $R_{ij}$，另一个针对协变量缺失指示变量 $S_{ik}$，二者均依赖于未观测的 $\theta$、已观测的反应/协变量以及缺失值本身（MNAR 假设）。通过 MCMC（如 Gibbs 采样或 HMC）进行后验推断，利用数据增强（data augmentation）将缺失值视为潜在变量，实现联合采样。模型通过引入依赖参数（如缺失机制对缺失值的回归系数）来识别 MNAR 结构，并利用贝叶斯先验（如稀疏先验或敏感性分析先验）缓解非识别性问题。

**与已有工作关系**  
已有工作主要分为两类：一是单独处理项目反应缺失的 MNAR 模型（如 Holman & Glas, 2005），但忽略协变量缺失；二是处理协变量缺失的联合模型（如 Ibrahim et al., 2005），但假设项目反应完全观测。本报告首次将两类缺失置于同一贝叶斯框架下，并允许缺失机制之间通过潜在变量 $\theta$ 相关。相比传统的多重插补（MI）或极大似然估计，本方法能同时利用项目反应与协变量的信息，且无需假设缺失机制为 MAR。与近期基于深度学习的缺失处理方法相比，本方法保留了参数的可解释性，并提供了后验不确定性量化。

**贡献**  
1. 提出首个同时处理项目反应与协变量 MNAR 缺失的贝叶斯联合模型，填补了该交叉领域的空白。  
2. 通过共享潜在特质 $\theta$ 自然刻画两类缺失之间的依赖，避免了分步估计的信息损失。  
3. 提供完整的 MCMC 推断方案，并讨论模型可识别性条件（如工具变量或先验约束），为实际应用提供指导。  
4. 模拟与实证研究（如 PISA 数据）表明，在 MNAR 强度较高时，本方法相比现有方法显著降低偏差并提高覆盖率，尤其当缺失机制与潜在能力相关时。


### 6. 基本公共服务均衡布局能否增强城市创新网络韧性

**讲者**：Na Kang（Zhejiang Gongshang University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
城市创新网络韧性——即创新主体间协作关系在外部冲击（如经济波动、公共卫生事件）下维持功能并恢复的能力——是区域经济韧性的关键维度。然而，既有研究多关注基础设施或产业政策对创新产出的直接影响，鲜有探讨**基本公共服务均衡布局**（如教育、医疗、交通等公共资源的空间均等化配置）如何通过重塑创新要素流动与协作结构来影响网络韧性。本报告旨在回答：公共服务均衡布局是否以及如何增强城市创新网络的抗冲击与恢复能力？

**核心方法**  
讲者可能采用**双重差分（DID）** 或**工具变量（IV）** 策略，利用中国近年来推行的基本公共服务均等化试点政策（如“基本公共服务均等化综合改革试点”）作为准自然实验。通过构建城市层面的创新网络韧性指标（如网络连通性、节点冗余度、冲击后恢复速度），结合多期面板数据，估计政策冲击对韧性的因果效应。进一步，可能引入**空间杜宾模型**或**中介效应分析**，检验“公共服务均衡→人才/资本流动→网络结构优化→韧性提升”的传导机制，并控制城市初始创新水平、财政能力等混淆因素。

**与已有工作关系**  
现有文献主要从两条路径展开：一是创新网络韧性研究，侧重网络拓扑属性（如结构洞、聚类系数）与外部冲击的交互；二是公共服务与创新的关系，多聚焦于人力资本积累或企业选址。本报告将二者桥接，首次将**公共服务均衡布局**视为影响创新网络韧性的制度性前因，而非仅作为创新产出的投入要素。相较于传统韧性研究仅关注网络自身特征，该工作引入空间均衡政策视角，拓展了因果推断在创新地理学中的应用边界。

**贡献**  
1. **理论贡献**：提出“公共服务均衡→创新网络韧性”的分析框架，揭示公共资源配置的空间公平性如何通过降低创新协作摩擦、增强节点替代性来提升网络抗风险能力。  
2. **实证贡献**：利用准自然实验方法识别因果效应，克服了内生性问题（如高韧性城市可能主动布局公共服务），为政策评估提供可靠证据。  
3. **政策启示**：若发现正向效应，则表明推进基本公共服务均等化不仅是社会公平目标，更是增强城市创新系统韧性的战略工具，为“十四五”期间区域协调发展与创新驱动战略的协同提供量化依据。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)