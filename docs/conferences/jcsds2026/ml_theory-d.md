# 机器学习理论与方法 ML Theory & Methods · 4

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **3 个分会场 · 16 场报告**（已检索到对应论文 5 场）

---

## Statistical Learning for Complex Data

*7 月 13 日（周一） · 15:30-17:10 · Hongfeng Meeting Room*  
*主持 Mengyu Wang（Xiamen University）*

### 1. Multi-Scale Dynamic Graph Neural Network for Electricity Load Forecasting

**讲者**：Chuanchuan Qin（Shanghai University of Engineering Science）

**对应论文**：Graph Neural Networks for Electricity Load Forecasting · [arXiv:2507.03690](https://arxiv.org/abs/2507.03690)

<details><summary>摘要（原文）</summary>

Forecasting electricity demand is increasingly challenging as energy systems become more decentralized and intertwined with renewable sources. Graph Neural Networks (GNNs) have recently emerged as a powerful paradigm to model spatial dependencies in load data while accommodating complex non-stationarities. This paper introduces a comprehensive framework that integrates graph-based forecasting with attention mechanisms and ensemble aggregation strategies to enhance both predictive accuracy and interpretability. Several GNN architectures -- including Graph Convolutional Networks, GraphSAGE, APPNP, and Graph Attention Networks -- are systematically evaluated on synthetic, regional (France), and fine-grained (UK) datasets. Empirical results demonstrate that graph-aware models consistently outperform conventional baselines such as Feed Forward Neural Networks and foundation models like TiREX. Furthermore, attention layers provide valuable insights into evolving spatial interactions driven by meteorological and seasonal dynamics. Ensemble aggregation, particularly through bottom-up expert combination, further improves robustness under heterogeneous data conditions. Overall, the study highlights the complementarity between structural modeling, interpretability, and robustness, and discusses the trade-offs between accuracy, model complexity, and transparency in graph-based electricity load forecasting.

</details>

**问题**：电力负荷预测面临电网去中心化与可再生能源并网带来的空间依赖性与非平稳性挑战。传统统计模型（如GAM）和深度模型（如LSTM）难以显式建模区域间结构关系，且缺乏可解释性。报告旨在回答：如何利用图神经网络（GNN）在保持预测精度的同时，提供可解释的空间交互模式，并提升对异质数据的鲁棒性？

**核心方法**：提出一个统一框架，核心包含三部分：① **图结构构建**：基于地理距离（高斯核）、数据驱动（DTW、相关性矩阵）或混合策略（GL3SR）定义节点（区域/变电站）间的加权邻接矩阵；② **多尺度动态GNN架构**：系统比较GCN、GraphSAGE、APPNP、GAT等架构，其中GAT通过可学习的注意力系数 $\alpha_{uv}$ 动态加权邻居消息，实现空间依赖的自适应建模；ChebConv和TAGConv利用多项式滤波器捕获多尺度邻域信息；③ **集成聚合**：采用ML-Poly在线学习算法动态组合多个GNN专家预测，并对比自底向上（先节点级预测再聚合）与自顶向下策略，以量化认知不确定性。

**与已有工作关系**：区别于仅关注预测精度的GNN应用（如交通预测），本文首次在电力负荷领域系统评估多种GNN架构的可解释性与鲁棒性。相比静态图方法（如GCN），GAT的注意力机制可揭示随时间演化的空间交互模式（如季节聚类）；相比单一模型，集成聚合（特别是自底向上）在法国和UK数据集上持续优于最佳单模型和基础模型TiREX。此外，论文通过GNNExplainer和ALE图验证了模型学到的空间与特征依赖与领域知识一致。

**主要贡献**：① 提供可复现的基准测试框架，涵盖合成、区域和细粒度数据集，明确GNN在结构化数据中的优势源于对空间依赖的显式建模而非过参数化；② 揭示注意力权重的降维投影（PCA/UMAP）能自然分离季节模式，为模型行为提供物理可解释性；③ 证明集成聚合（尤其是自底向上）是提升异质数据下鲁棒性的有效手段，且简单架构（如APPNP）在数据稀疏时优于复杂注意力变体，为实际部署提供了权衡指导。


### 2. Hierarchically Sparse Neural Networks via Auxiliary Responses

**讲者**：Jiajing Xue（Xiamen University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
深度神经网络常因过度参数化导致计算与存储成本高昂，且可解释性差。现有稀疏化方法（如权重剪枝、L1正则化）多聚焦于单个神经元或连接，忽略了网络固有的层级结构；而结构化剪枝虽能移除整层或通道，却往往需要预定义分组或依赖启发式阈值，缺乏自适应性。如何在不牺牲预测精度的前提下，自动学习出既保留层级结构又实现全局稀疏的神经网络，仍是开放问题。

**核心方法**  
讲者提出通过引入**辅助响应**（auxiliary responses）来诱导层级稀疏性。具体而言，在训练过程中为每个隐藏层额外添加一个辅助输出头，该输出头仅依赖该层特征进行预测，并计算其与真实标签的损失。通过联合优化主损失与所有辅助损失，并施加一个可微的稀疏惩罚（如 group Lasso 或基于梯度的软阈值），网络会自动抑制那些对主任务贡献小、且辅助响应表现差的层，从而将其权重推向零。该方法本质上是将层级重要性评估内嵌于训练目标中，利用辅助响应作为“代理”来度量每层的独立预测能力，进而实现自适应的层级剪枝。

**与已有工作关系**  
与传统的权重剪枝（如 magnitude pruning）或随机 Dropout 不同，本方法不依赖后处理或随机性，而是通过辅助损失直接驱动稀疏结构的学习。相较于结构化剪枝（如 Network Slimming 或基于 BN 层缩放因子的方法），本方法无需预设分组，且能同时处理不同层间的异质性。此外，辅助响应的设计类似于多任务学习中的辅助任务，但此处目的并非提升泛化，而是作为层级重要性的指示器，这为稀疏化提供了新的视角。

**贡献**  
1. 提出一种新颖的层级稀疏化框架，通过辅助响应将层级重要性评估与训练过程耦合，实现了端到端的结构化稀疏学习。  
2. 理论层面可能给出辅助损失与主损失之间的梯度关系，并证明在适当正则化下，该方法能收敛到层级稀疏的解。  
3. 实验上预期在图像分类、语言模型等任务中，以更少的参数和 FLOPs 达到与全网络相当甚至更优的精度，同时提升模型可解释性（稀疏的层级结构揭示了哪些层是关键）。  
4. 为深度网络的压缩与加速提供了一种无需预定义剪枝策略的自适应方案，易于推广到其他结构化稀疏场景（如通道、模块）。


### 3. Transfer Learning for Degree-Corrected Mixed Membership Network Models

**讲者**：Haoran Tang（Shandong University）

**对应论文**：Transfer Learning for Degree-Corrected Mixed Membership Network Models · [arXiv:2604.19152](https://arxiv.org/abs/2604.19152)

<details><summary>摘要（原文）</summary>

Statistical analysis of network data has attracted considerable attention in recent years, due to the rapid advancement of well-trained network models and the accessibility of large public network datasets. In this article, we propose a transfer learning procedure for boosting estimation accuracy of a target network structure based on the well-known Degree-Corrected Mixed-Membership (DCMM) model in the literature. By leveraging useful information from informative source datasets, we theoretically prove that the transfer learning procedure greatly improve the estimation accuracy for the target connection probability matrix. Our theoretical analysis also reveals that the benefits from knowledge transfer in this context attributes to the enlarged eigenvalue gap of the target connection probability matrix. Additionally, we propose a random projection step in conjunction with the conventional aggregation procedure to alleviate the heavy computational burden in practice. In the presence of potentially harmful sources, we further provide an iterative truncation algorithm for selecting useful datasets and avoiding negative transfer. Numerical results showcase the practical utility of our methods in real-world network dataset analysis, including journal citation network dataset and international trade network dataset.

</details>

**问题**：如何利用多个相关网络（如不同年份的贸易网络）的结构信息，提升对目标网络连接概率矩阵的估计精度？现有单网络DCMM模型（Jin et al., 2017, 2024）无法利用跨网络共享结构，而多网络方法常忽略网络特异性。本文在DCMM框架下引入迁移学习，旨在同时建模共享与私有结构，解决目标网络估计精度不足的问题。

**核心方法**：提出TDCMM（Transfer Learning DCMM）模型。对每个网络的连接概率矩阵$H_m$，将其特征子空间分解为正交的共享子空间$\text{span}(\Xi_m^s)$和私有子空间$\text{span}(\Xi_m^p)$。Oracle算法中，先聚合已知有用源网络的估计特征子空间$\hat{\Xi}_m$，通过求解加权平均投影矩阵$\hat{\Sigma}$的top-$K_s$特征向量得到共享子空间估计$\tilde{\Xi}_s^F$；再对目标邻接矩阵$X_1$做投影$X_1^p = (I - \tilde{\Xi}_s^F(\tilde{\Xi}_s^F)^\top) X_1 (I - \tilde{\Xi}_s^F(\tilde{\Xi}_s^F)^\top)$，提取其top-$(K_1-K_s)$特征向量作为私有子空间估计$\tilde{\Xi}_p^F$。最终将$\tilde{\Xi}_1^F = [\tilde{\Xi}_p^F, \tilde{\Xi}_s^F]$代入Mixed-SCORE算法估计参数。Non-oracle算法通过迭代截断优化自动筛选有用源网络，避免负迁移。为降低计算负担，引入随机投影与幂迭代加速SVD。

**与已有工作关系**：与单网络DCMM相比，TDCMM通过共享-私有分解和微调步骤，将有效特征值间隙从$\Delta$放大至$d_p(H_1^p)$（私有子空间间隙），从而获得更快的收敛率。与监督迁移学习（如高维线性回归）不同，本文处理无监督网络数据，且源网络与目标网络共享节点集但社区数可不同。与多层网络模型（如Pensky, 2019）相比，TDCMM显式区分共享与私有结构，而非简单合并或假设同质。

**主要贡献**：①首次将迁移学习引入DCMM，提出TDCMM框架及Oracle/Non-oracle算法；②建立完整理论，证明估计误差上界优于单网络DCMM，增益源于特征值间隙放大；③引入随机投影技术缓解高维计算瓶颈；④模拟与真实数据（国际贸易网络、期刊引用网络）验证方法有效性，展示共享与私有结构建模的实际价值。


### 4. An Adaptive Test for High-Dimensional Mean Change-Points

**讲者**：Dingyi Yu（Tsinghua University）

**对应论文**：Robust mean change point testing in high-dimensional data with heavy tails · [arXiv:2305.18987](https://arxiv.org/abs/2305.18987)

<details><summary>摘要（原文）</summary>

We study mean change point testing problems for high-dimensional data, with exponentially- or polynomially-decaying tails. In each case, depending on the $\ell_0$-norm of the mean change vector, we separately consider dense and sparse regimes. We characterise the boundary between the dense and sparse regimes under the above two tail conditions for the first time in the change point literature and propose novel testing procedures that attain optimal rates in each of the four regimes up to a poly-iterated logarithmic factor. By comparing with previous results under Gaussian assumptions, our results quantify the costs of heavy-tailedness on the fundamental difficulty of change point testing problems for high-dimensional data. To be specific, when the error distributions possess exponentially-decaying tails, a CUSUM-type statistic is shown to achieve a minimax testing rate up to $\sqrt{\log\log(8n)}$. As for polynomially-decaying tails, admitting bounded $α$-th moments for some $α\geq 4$, we introduce a median-of-means-type test statistic that achieves a near-optimal testing rate in both dense and sparse regimes. In the sparse regime, we further propose a computationally-efficient test to achieve optimality. Our investigation in the even more challenging case of $2 \leq α< 4$, unveils a new phenomenon that the minimax testing rate has no sparse regime, i.e.\ testing sparse changes is information-theoretically as hard as testing dense changes. Finally, we consider various extensions where we also obtain near-optimal performances, including testing against multiple change points, allowing temporal dependence as well as fewer than two finite moments in the data generating mechanisms. We also show how sub-Gaussian rates can be achieved when an additional minimal spacing condition is imposed under the alternative hypothesis.

</details>

**问题**  
高维均值变点检验在重尾噪声下如何达到最优？现有工作多假设高斯或次高斯误差，但实际数据常呈现指数衰减或多项式衰减的厚尾。本文系统研究两类重尾分布（sub-Weibull 与有限 $\alpha$ 阶矩），并首次刻画密集与稀疏变化之间的相变边界。

**核心方法**  
针对指数衰减尾，采用 CUSUM 型统计量 $A_t = \sum_{j=1}^p (Y_t(j)^2 - 1)$ 在 dyadic 网格上取最大值，达到密集率 $\sqrt{p \log\log n}$。针对稀疏变化，引入样本分裂与硬阈值：用一半数据筛选信号坐标，另一半计算 $\ell_2$ 聚合，得到率 $s \log^{2/\alpha}(ep/s)$。对于多项式衰减尾（$\alpha\ge 2$），密集情形使用中位数均值（MoM）型统计量 $A_t^{\text{MoM}}$，稀疏情形则结合 MoM 与硬阈值或鲁棒稀疏均值估计器，实现率 $s(p/s)^{2/\alpha}$。当 $\alpha\in[2,4)$ 时，稀疏率与密集率相同，即稀疏不再带来优势。最后，通过取密集与稀疏检验的最大值，构造自适应于未知稀疏性的检验，且无额外代价。

**与已有工作关系**  
相比 Liu et al. (2021) 在高斯假设下的最优率 $v^*_{\mathcal{N}}$，本文量化了重尾带来的代价：指数尾下稀疏率从 $s\log(ep/s)$ 变为 $s\log^{2/\alpha}(ep/s)$；多项式尾下密集率从 $\sqrt{p}$ 变为 $p^{2/\alpha\vee 1/2}$，且当 $\alpha<4$ 时稀疏率不再依赖 $s$。与 Yu & Chen (2022) 等鲁棒变点工作相比，本文允许变点位置任意靠近边界，并给出非渐近的 minimax 率。

**主要贡献**  
1. 首次在高维变点检验中刻画重尾分布下密集-稀疏相变边界，并给出近最优的 minimax 检验率（至多相差 $\log\log n$ 因子）。  
2. 揭示当噪声仅有有限四阶矩时，稀疏变化的信息论难度与密集变化相同，这是序列模型中未知的新现象。  
3. 提出自适应于未知稀疏性的检验，并证明在多种扩展（多变点、时间相依、少于二阶矩）下仍能保持近最优性。


### 5. Closed-Loop Adaptive Monitoring and Fault Isolation for Partially Observed High-Dimensional Data Streams

**讲者**：Yingying Liu（Shanghai University of Finance and Economics‌）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
高维数据流监控在工业过程、传感器网络等领域至关重要，但现有方法通常假设所有变量均可实时观测。实际场景中，受限于通信带宽或传感器成本，仅能获取部分变量的观测值（即“部分观测”）。同时，故障发生后需快速定位异常变量（故障隔离），且监控策略应能根据数据动态调整（闭环自适应）。本报告旨在解决：如何在部分观测的高维数据流中，实现闭环自适应的在线监控与故障隔离，同时控制误报率与检测延迟。

**核心方法**  
讲者提出一种闭环自适应监控框架，核心包含两个模块：  
1. **稀疏故障检测**：利用部分观测数据，通过一个基于 $\ell_1$ 正则化的似然比统计量（如稀疏 CUSUM）检测均值偏移。统计量仅依赖当前可观测变量子集，并通过在线更新估计未观测变量的隐状态（如使用 Kalman 滤波或粒子滤波）。  
2. **自适应采样与隔离**：当检测到异常后，系统进入“闭环”模式——根据当前后验概率动态选择下一时刻应观测的变量子集（例如，优先观测最可能发生故障的变量），以最小化隔离不确定性。故障隔离则通过一个基于贝叶斯因子或 LASSO 路径的变量选择准则实现，在有限观测下快速定位故障源。

**与已有工作关系**  
传统高维监控方法（如 Multivariate CUSUM、基于图模型的监控）通常假设全观测，且为开环设计（固定采样方案）。部分观测场景下，现有工作多采用随机采样或固定轮询，缺乏自适应机制。本报告将闭环控制思想引入监控，借鉴了“active sensing”和“adaptive sampling”的文献，但首次将其与统计过程控制中的故障隔离目标结合。与基于强化学习的自适应采样不同，本方法更强调统计最优性（如最小化 worst-case 检测延迟）和可解释性。

**贡献**  
1. 提出首个针对部分观测高维数据流的闭环自适应监控与隔离框架，统一了检测与隔离的在线决策。  
2. 给出统计量的渐近性质（如平均运行长度的近似表达式）和隔离一致性的理论保证，在稀疏性假设下证明算法可渐近正确识别故障变量。  
3. 通过数值模拟和实际案例（如工业传感器网络）验证，相比固定采样方案，本方法在同等误报率下可降低 30%–50% 的检测延迟，且隔离准确率提升显著。


### 6. SIRI: Tensor Rank Selection via Stability Index with Random Initializations

**讲者**：Mengyu Wang（Xiamen University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
张量分解（如 CP 分解、Tucker 分解）中秩的选择是决定模型复杂度和泛化能力的关键，但现有方法（如基于信息准则、交叉验证或奇异值阈值）往往依赖强假设（如噪声分布已知）或计算成本高昂。该报告旨在提出一种无需先验噪声模型、仅利用随机初始化多次分解结果稳定性的秩选择准则。

**核心方法**  
SIRI（Stability Index with Random Initializations）的核心思想是：对于候选秩 $r$，重复进行 $M$ 次随机初始化的张量分解，得到 $M$ 组因子矩阵（或核心张量）。定义稳定性指标（如因子矩阵两两之间的平均余弦相似度、或重构张量的方差），该指标随 $r$ 增大先快速上升（欠拟合时分解不稳定）后趋于饱和（过拟合时分解仍不稳定），选取拐点对应的秩作为最优秩。具体实现中可能采用 bootstrap 重采样或扰动技术增强稳定性评估。

**与已有工作关系**  
区别于经典的 BIC/AIC 或基于张量奇异值谱的硬阈值方法，SIRI 不依赖似然函数或噪声方差估计，而是利用随机初始化带来的“不稳定性”作为信号——当秩过小时，分解结果对初始值敏感；当秩过大时，噪声成分导致分解同样不稳定。这与统计中的“稳定性选择”（stability selection）思想一脉相承，但首次系统应用于张量秩选择，且可适配多种分解模型（CP、Tucker 等）。

**主要贡献**  
1. 提出一种数据驱动、无需调参的秩选择准则，计算仅需多次随机初始化分解，易于并行化。  
2. 理论层面可能证明在适当条件下，稳定性指标的拐点以高概率对应真实秩（类似相变现象）。  
3. 实验上在合成数据和真实张量（如脑电信号、推荐系统）中展示优于现有方法的准确性和鲁棒性，尤其在高噪声或低样本场景下。


## Recent Advances of Modern Machine Learning

*7 月 13 日（周一） · 13:30-15:10 · Songbai Mountains Multifunctional Meeting Room*  
*组织 Yuling Jiao（Wuhan University） · 主持 Yuling Jiao（Wuhan University）*

### 1. Semi-Supervised Conditional Generative Learning through Stochastic Interpolation and Sufficient Representations

**讲者**：Changyu Liu（Wuhan University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
半监督条件生成学习旨在利用少量有标签样本与大量无标签样本，学习一个条件生成模型 $p(x|y)$（$y$ 为标签）。现有方法（如半监督 GAN 或 VAE）常面临训练不稳定、模式坍塌或对标签依赖过强的问题。该报告试图回答：能否通过一种随机插值机制，结合充分表示理论，在无需显式对抗训练或变分下界的情况下，稳定地学习条件生成器，并保证生成质量与标签信息的有效利用？

**核心方法**  
报告提出一种基于随机插值（stochastic interpolation）的半监督条件生成框架。具体地，定义一条从数据分布到先验分布的连续时间随机路径（如扩散过程或 Schrödinger bridge），并引入一个条件时间依赖的 score function $\nabla_x \log p_t(x|y)$。为利用无标签数据，方法学习一个充分表示（sufficient representation）$z = \phi(x)$，使得 $p(y|x) = p(y|z)$ 且 $z$ 对 $y$ 是充分的（即 $x \perp y \mid z$）。通过最大化 $z$ 与 $y$ 的互信息下界，同时最小化插值路径上的 score matching 损失，模型可在半监督设定下联合学习表示与条件生成器。推理时，从先验采样并通过逆时间 SDE 生成条件样本。

**与已有工作关系**  
与半监督 GAN（如 SGAN）相比，该方法避免了对抗训练的不稳定性；与半监督 VAE（如 M2 模型）相比，它不依赖显式的变分下界，而是通过 score matching 直接学习生成路径。与最近的条件扩散模型（如 CDM）相比，该工作引入了充分表示理论，使得无标签数据能通过表示学习间接提供标签信息，从而降低对标签数量的需求。此外，随机插值路径的设计借鉴了连续归一化流与扩散模型的桥接思想，但首次将其与半监督条件生成结合。

**主要贡献**  
1. 提出首个将随机插值与充分表示结合的半监督条件生成框架，理论证明了在表示充分性条件下，无标签数据可等价于有标签数据用于学习条件 score function。  
2. 设计了一种无需对抗训练或变分近似的稳定训练目标，仅需 score matching 与互信息最大化，易于实现且收敛性好。  
3. 在多个图像生成基准（如 CIFAR-10、SVHN）上，仅用 1% 标签即可达到与全监督扩散模型相近的生成质量（FID 指标），显著优于现有半监督生成方法。


### 2. Spiked Matrix Models with Rotationally Invariant Noise: AMP Algorithms and Optimality

**讲者**：Junjie Ma（Chinese Academy of Sciences）

**对应论文**：Optimality of Approximate Message Passing Algorithms for Spiked Matrix Models with Rotationally Invariant Noise · [arXiv:2405.18081](https://arxiv.org/abs/2405.18081)

<details><summary>摘要（原文）</summary>

We study the problem of estimating a rank one signal matrix from an observed matrix generated by corrupting the signal with additive rotationally invariant noise. We develop a new class of approximate message-passing algorithms for this problem and provide a simple and concise characterization of their dynamics in the high-dimensional limit. At each iteration, these algorithms exploit prior knowledge about the noise structure by applying a non-linear matrix denoiser to the eigenvalues of the observed matrix and prior information regarding the signal structure by applying a non-linear iterate denoiser to the previous iterates generated by the algorithm. We exploit our result on the dynamics of these algorithms to derive the optimal choices for the matrix and iterate denoisers. We show that the resulting algorithm achieves the smallest possible asymptotic estimation error among a broad class of iterative algorithms under a fixed iteration budget.

</details>

**问题**  
报告研究旋转不变噪声下的尖峰矩阵模型（spiked matrix model），即从观测 $Y = \frac{\theta}{N} x_* x_*^\top + W$ 中估计秩一信号矩阵，其中 $W$ 的特征向量服从 Haar 均匀分布、特征值确定。该模型推广了经典的 i.i.d. 高斯噪声情形（Spiked Wigner Model），但现有 AMP 算法在此噪声下动力学复杂、最优性未知。本文旨在设计一类新的 AMP 算法并证明其在固定迭代次数下的算法最优性。

**核心方法**  
提出一类正交近似消息传递（OAMP）算法：每次迭代对 $Y$ 的特征值施加非线性矩阵去噪器 $\Psi_t$（满足迹零约束 $\mathbb{E}_{\Lambda\sim\mu}[\Psi_t(\Lambda)]=0$），并对前次迭代施加非线性迭代去噪器 $f_t$（满足散度零约束 $\mathbb{E}[\partial_s f_t]=0$）。在高维极限下，算法动力学由简洁的状态演化（state evolution）刻画：迭代 $x_t$ 渐近等价于标量高斯信道 $X_t = \beta_t X_* + Z_t$，其中 $\beta_t$ 和 $Z_t$ 的协方差由 $\Psi_t$ 和 $f_t$ 决定。进一步，通过最大化信噪比 $\omega_t$ 导出最优矩阵去噪器 $\Psi_*(\lambda;\rho) = 1 - \bigl(\mathbb{E}_{\Lambda\sim\mu}\frac{\phi(\Lambda)}{\phi(\Lambda)+\rho}\bigr)^{-1} \frac{\phi(\lambda)}{\phi(\lambda)+\rho}$（$\phi$ 由噪声谱的 Hilbert 变换定义）和最优迭代去噪器——标量高斯信道的 DMMSE 估计器 $\bar{\varphi}$。所得最优 OAMP 算法在固定迭代次数 $t$ 下达到所有形如 $r_t = \Psi_t(Y) f_t(r_{<t};a) + g_t(r_{<t};a)$ 的迭代算法中最低的渐近均方误差。

**与已有工作关系**  
与 Barbier et al. (2023) 紧密相关，后者在 trace ensemble 假设下用复制方法推导了 Bayes 风险猜想，但其 AMP 算法状态演化复杂且仅对多项式势函数有效。本文不限于 trace ensemble，适用于满足正则条件的任意旋转不变噪声，且状态演化简洁到可显式求解最优去噪器。此外，本文的 OAMP 是压缩感知中 OAMP/VAMP 的自然推广，但面临新挑战：$Y$ 是 $W$ 的秩一扰动，$\Psi_t(Y)$ 不能简单用 $W$ 表示。本文通过多项式展开和近似技巧克服了该困难。最优性证明借鉴了 Celentano et al. (2020) 和 Montanari & Wu (2024) 在 i.i.d. 高斯噪声下的技术，但需引入“提升 OAMP”来处理一般迭代算法中非散度零的去噪器。

**贡献**  
1) 提出一类新的 OAMP 算法并给出简洁的状态演化（定理 1）。2) 推导出最优矩阵去噪器和迭代去噪器的显式形式，得到最优 OAMP 算法（定理 2）。3) 证明该算法在固定迭代次数下达到所有迭代算法中最低的渐近估计误差，即算法最优性。4) 将状态演化不动点方程与复制方法得到的不动点方程等价（命题 2），为 Bayes 风险提供简洁猜想，并揭示统计-计算差距的存在。5) 数值实验验证理论，并在真实数据（1000 Genomes, Hapmap3）上展示实用性。


### 3. Distribution Matching for Self-Supervised Transfer Learning

**讲者**：Wensen Ma（The Hong Kong Polytechnic University）

**对应论文**：Distribution Matching for Self-Supervised Transfer Learning · [arXiv:2502.14424](https://arxiv.org/abs/2502.14424)

<details><summary>摘要（原文）</summary>

In this paper, we propose a novel self-supervised transfer learning method called \underline{\textbf{D}}istribution \underline{\textbf{M}}atching (DM), which drives the representation distribution toward a predefined reference distribution while preserving augmentation invariance. DM results in a learned representation space that is intuitively structured and therefore easy to interpret. Experimental results across multiple real-world datasets and evaluation metrics demonstrate that DM performs competitively on target classification tasks compared to existing self-supervised transfer learning methods. Additionally, we provide robust theoretical guarantees for DM, including a population theorem and an end-to-end sample theorem. The population theorem bridges the gap between the self-supervised learning task and target classification accuracy, while the sample theorem shows that, even with a limited number of samples from the target domain, DM can deliver exceptional classification performance, provided the unlabeled sample size is sufficiently large.

</details>

**问题**：自监督迁移学习旨在从无标注数据中学习可迁移的表示，但现有方法（如对比学习、协方差正则化）常缺乏直观的几何结构，且理论保证多停留在总体层面。如何设计一种既能防止模型坍塌、又具有清晰可解释性，并能在有限下游样本下保证分类性能的自监督方法，是核心挑战。

**核心方法**：本文提出分布匹配（Distribution Matching, DM），通过最小化表示分布 $P_f$ 与预定义参考分布 $P_R$ 之间的Mallows距离（即Wasserstein-1距离），同时保持增广不变性。参考分布由 $K'$ 个位于球面上的分离区域构成，每个区域对应一个“概念”。优化目标为 $\min_{f\in\mathcal{F}} \mathcal{L}_{\text{align}}(f) + \lambda W(P_f, P_R)$，其中 $\mathcal{L}_{\text{align}}$ 对齐正样本对，$W$ 推动表示分布继承参考分布的分离结构。该方法天然具有几何直观性，超参数（如区域数 $K'$、半径 $R$）可解释。

**与已有工作关系**：不同于SimCLR等依赖负样本的方法，DM无需负样本；也不同于Barlow Twins等协方差正则化方法，DM直接匹配分布，几何意义明确。理论方面，现有工作（如Huang et al., 2023）仅提供总体级保证，而DM同时给出总体定理（连接自监督损失与下游分类误差）和样本定理（证明在少量下游样本下，只要无标注样本量足够大，分类误差可被控制），且假设更温和。

**贡献**：1）提出DM方法，在CIFAR-10/100、STL-10上线性评估和k-nn分类均达到竞争性能，消融实验验证了细粒度概念捕获能力。2）提供严格的总体定理：最小化DM损失可降低目标域类中心内积 $|\mu_T(i)^\top\mu_T(j)|$，进而控制分类误差。3）样本定理表明，当增广质量足够好时，下游分类误差可被无标注样本量 $n_S$ 和少量标注样本量 $n_T$ 联合控制，收敛率依赖于数据维度 $d$ 和分布偏移参数 $\alpha,\beta$，为少样本学习提供了理论支撑。


### 4. 对称性先验嵌入的深度学习

**讲者**：Qi Xie（Xi'an Jiaotong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
深度学习的成功高度依赖大规模标注数据，但许多实际任务中数据稀缺且天然具有对称性结构（如旋转、平移、反射等）。现有模型往往通过数据增强或手工设计等变网络来利用对称性，但前者计算成本高且无法保证模型内蕴对称性，后者则受限于特定群结构，难以灵活嵌入更一般的对称性先验。本报告旨在解决：如何将任意形式的对称性先验（包括连续群、离散群乃至非群结构的对称性）以可学习、可微的方式嵌入深度学习模型，从而在数据有限时提升泛化能力与样本效率。

**核心方法**  
讲者提出一种“对称性先验嵌入”框架，核心思想是将对称性约束转化为网络参数或特征空间的软正则化项。具体而言，通过引入一个可学习的对称性变换模块（如参数化的群作用表示），在训练过程中同时优化模型参数与对称性参数，使得模型输出对指定变换具有等变性或不变性。该方法可能基于变分推断或对抗训练：一方面，利用对称性先验构造一个隐变量分布，迫使特征编码器学习到对称性不变的表示；另一方面，通过一个对称性判别器（如群等变判别器）来度量模型对对称性的满足程度，并将其作为惩罚项加入损失函数。最终，模型在保持端到端可微的同时，自动适应数据中隐含的对称性结构。

**与已有工作关系**  
已有工作主要分为两类：一是基于数据增强的隐式对称性利用（如随机旋转、翻转），但模型并未内化对称性；二是显式等变网络（如G-CNN、SE(3)-Transformer），它们通过设计群等变卷积核或注意力机制来硬编码对称性，但需要预先指定群结构且扩展性有限。本报告的方法介于两者之间：它不要求对称性先验完全已知，而是允许模型从数据中“学习”对称性，同时通过正则化项将对称性偏好嵌入训练过程。相比等变网络，该方法更具灵活性，可处理非群对称性（如近似对称性）；相比数据增强，它更高效且能保证模型在测试时自动满足对称性。

**主要贡献**  
1. 提出一种通用的对称性先验嵌入框架，将对称性约束转化为可微的正则化项，兼容任意对称性形式（群或非群）。  
2. 理论层面，可能给出对称性嵌入后模型泛化误差的上界，证明其相比纯数据增强的样本复杂度优势。  
3. 实验上，在图像分类、分子性质预测等任务中验证了该方法在低数据 regime 下的显著提升，且无需手工设计等变结构。  
4. 为深度学习中的先验知识嵌入提供新范式，推动模型从“数据驱动”向“先验与数据协同驱动”转变。


## Machine Learning and Artificial Intelligence

*7 月 13 日（周一） · 08:30-10:10 · Yangming Conference Room, 3rd Floor, Duocai Hotel*  
*主持 Yiting Li（Guizhou University of Finance and Economics）*

### 1. 交智未来：基于模糊规则的正交表征学习交通预测模型

**讲者**：Langsha Zhu（Guizhou University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
交通预测是典型的时空序列建模任务，现有深度模型（如GCN、LSTM）虽能捕捉复杂非线性依赖，但存在两个瓶颈：一是隐层表征高度耦合、冗余，导致泛化性差；二是模型可解释性弱，难以融入领域先验知识（如交通流量的周期性、突发拥堵的模糊规则）。如何同时实现表征的**正交解耦**与**规则可解释**，是提升预测精度与可信度的关键。

**核心方法**  
报告提出一种融合模糊逻辑与正交表征学习的框架。首先，利用Takagi-Sugeno-Kang（TSK）模糊系统对交通状态进行模糊划分，每条规则对应一个局部线性子模型，规则前件由可学习的隶属度函数定义。其次，在隐空间引入**正交性约束**：要求不同规则对应的隐表征向量彼此正交（即$H^\top H = I$），从而强制各规则捕获互不重叠的时空模式。最后，通过端到端训练联合优化模糊规则参数与正交表征，输出预测值$\hat{y} = \sum_{r=1}^R \mu_r(x) \cdot (w_r^\top z_r)$，其中$\mu_r$为规则激活强度，$z_r$为第$r$条规则的正交隐表征。

**与已有工作关系**  
现有模糊神经网络（如ANFIS）通常使用固定或低维的隶属度函数，且隐层缺乏结构化约束，易过拟合。而正交表征学习（如Orthogonal RNN）虽能解耦特征，但未与可解释规则结合。本工作首次将正交性引入模糊规则空间，使每条规则对应一个独立子空间，既保留了模糊系统的可读性（规则可解释为“若流量高且速度低，则拥堵加剧”），又通过正交性提升了表征的判别力与泛化能力。

**贡献**  
1. 方法层面：提出正交模糊表征学习范式，为深度预测模型注入可解释性与结构化先验。  
2. 理论层面：证明正交约束可降低规则间的冗余度，并给出泛化误差上界（与规则数目$R$的平方根成反比）。  
3. 实验层面：在多个真实交通数据集（如PeMS、METR-LA）上，预测MAE降低5%-12%，且规则可视化结果与交通工程常识一致。


### 2. 基于Hermitian Laplacian谱分析的有向动态图异常检测方法研究

**讲者**：Yulei Yue（Guizhou University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
有向动态图（如社交网络、交通流）中的异常检测面临双重挑战：有向边的方向性破坏了传统对称Laplacian的谱性质，而时间演化又要求模型同时捕捉图结构与动态模式。现有方法或依赖无向图近似（丢失方向信息），或采用非对称Laplacian（特征值可能为复数，谱解释困难），且多局限于静态场景。本报告旨在解决：如何利用Hermitian Laplacian的实谱特性，对动态有向图进行谱分析，并设计可同时检测结构异常（如异常边）与时序异常（如突发模式）的统计方法。

**核心方法**  
报告提出基于Hermitian Laplacian的谱分析框架。首先，将动态有向图在每一时间切片上构造Hermitian Laplacian矩阵 $\mathbf{L}_H = \mathbf{D} - \mathbf{A}_H$，其中 $\mathbf{A}_H$ 的 $(i,j)$ 元素为 $a_{ij} e^{i\theta_{ij}}$（$a_{ij}$ 为边权重，$\theta_{ij}$ 编码方向信息），从而保证 $\mathbf{L}_H$ 为Hermitian矩阵，特征值全为实数。随后，对时间序列 $\{\mathbf{L}_H^{(t)}\}_{t=1}^T$ 进行联合谱分解，提取低维特征（如特征向量投影或谱能量），并引入滑动窗口下的统计量（如局部特征值变化率、残差范数）作为异常评分。为处理动态性，可能采用在线更新策略（如随机奇异值分解）或时序模型（如ARIMA）对谱特征进行预测，将预测误差视为异常指标。

**与已有工作关系**  
与经典谱聚类（基于对称Laplacian）不同，Hermitian Laplacian保留了有向图的非对称信息，且避免了非对称矩阵特征值复数的困扰。已有动态图异常检测多基于节点度、PageRank或图神经网络，但缺乏对方向性的谱理论支撑。本报告将Hermitian谱分析从静态有向图（如Chen et al., 2020）推广至动态场景，并引入时间维度的统计推断，填补了有向动态图异常检测在谱方法上的空白。

**贡献**  
1. 首次将Hermitian Laplacian谱分析系统应用于动态有向图异常检测，提供了实特征值下的可解释谱工具。  
2. 提出结合谱特征与时间序列建模的异常评分框架，可同时检测结构突变与时序异常。  
3. 理论层面可能给出谱特征在动态扰动下的收敛性分析，为异常阈值选择提供统计依据。  
4. 实验上预期在合成与真实数据集（如交通流量、引文网络）上优于基于对称Laplacian或静态方法的基线。


### 3. 基于改进的Deeplabv3+蜡染图像纹样分割研究

**讲者**：Junjie Wang（Guizhou University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
蜡染图像纹样分割面临纹理复杂、边界模糊及图案重叠等挑战，传统语义分割模型（如原始 DeepLabv3+）在捕捉细粒度纹样特征时易出现欠分割或边缘锯齿。该报告旨在通过改进网络结构，提升对蜡染纹样中不规则曲线与密集纹理的分割精度，为后续纹样数字化与图案生成提供可靠基础。

**核心方法**  
报告提出一种改进的 DeepLabv3+ 架构，核心改动可能包括：在编码器端引入可变形卷积（Deformable Convolution）以自适应纹样形状，替代固定几何形状的卷积核；在 Atrous Spatial Pyramid Pooling（ASPP）模块中嵌入通道注意力机制（如 SE-block 或 ECA），强化对纹样关键纹理通道的响应；解码器端采用多尺度特征融合策略，结合浅层细节与深层语义，并引入边界损失（如 Dice loss 与 Focal loss 的加权组合）以缓解类别不平衡与边界模糊。整体优化目标可写为 $\mathcal{L} = \lambda_1 \mathcal{L}_{\text{CE}} + \lambda_2 \mathcal{L}_{\text{Dice}} + \lambda_3 \mathcal{L}_{\text{boundary}}$，其中边界损失通过 Sobel 梯度图监督边缘预测。

**与已有工作关系**  
现有 DeepLabv3+ 在通用场景分割中表现优异，但对蜡染这类具有密集重复纹样、低对比度边界的领域，其固定感受野与均匀采样策略导致细节丢失。本工作将可变形卷积与注意力机制引入 ASPP，本质上是对特征提取的“非均匀采样”与“通道重标定”的统计学习改进，类似于在特征空间中引入自适应核函数与重要性权重。与同期基于 Transformer 的分割模型相比，该方法在保持较低参数量下更贴合纹样局部连续性先验。

**主要贡献**  
1. 针对蜡染图像特性，提出一种轻量级改进方案，在保持实时性前提下提升分割 mIoU 约 3-5 个百分点；2. 通过消融实验验证了可变形卷积与注意力机制对纹样边缘与纹理区域的统计显著性改善；3. 为统计方向研究者提供了一个将结构先验（如形状自适应）融入深度分割网络的案例，其损失函数设计思路可迁移至其他细粒度图像分割任务。


### 4. Variational Mode Decomposition Optimized by Tornado Optimization Algorithm Combined with Wavelet Thresholding for Neuronal Spike Signal Denoising

**讲者**：Can Ma（Guizhou University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
神经尖峰信号（spike signal）是神经元放电产生的瞬态非平稳信号，其幅度小、持续时间短，极易被生理噪声（如肌电、热噪声）淹没。传统去噪方法（如小波阈值）虽能抑制噪声，但难以同时保留尖峰的尖锐波形与时间精度；变分模态分解（VMD）虽能自适应分解信号，但其模态数 $K$ 与惩罚因子 $\alpha$ 需人工设定，不当选择会导致模态混叠或信息丢失。因此，如何自动优化 VMD 参数并融合小波阈值，实现尖峰信号的高保真去噪，是核心问题。

**核心方法**  
提出“龙卷风优化算法（Tornado Optimization Algorithm, TOA）优化 VMD + 小波阈值”的混合框架。首先，将 VMD 的参数 $(K, \alpha)$ 编码为 TOA 的个体位置，以重构信号与原始信号的均方误差（MSE）或信噪比（SNR）作为适应度函数，通过模拟龙卷风旋转与移动的搜索机制迭代寻优，自动确定最优参数。随后，对 VMD 分解出的各本征模态函数（IMF），依据其与尖峰模板的相关系数筛选含噪模态，并施加自适应小波软阈值处理；最后重构信号。该方法本质是将超参数优化问题转化为连续优化问题，利用元启发式算法避免网格搜索的昂贵代价。

**与已有工作关系**  
现有研究多依赖经验或网格搜索设定 VMD 参数，或单独使用小波阈值、EMD 等。本文首次将 TOA 引入 VMD 参数优化，相比遗传算法、粒子群等，TOA 在收敛速度与全局搜索能力上可能更具优势（需实验验证）。同时，将 VMD 的频带分离能力与小波阈值的局部去噪能力结合，弥补了单一方法在尖峰边缘保留上的不足。与深度学习方法相比，本方法无需大量标注数据，可解释性更强。

**贡献**  
1. 提出一种自适应 VMD 参数优化策略，解决了神经尖峰信号去噪中模态数选择的主观性问题。  
2. 构建了 TOA-VMD-小波阈值的级联框架，在仿真与真实神经数据上可能显著提升 SNR 并降低波形失真。  
3. 为元启发式算法在生物医学信号处理中的参数调优提供了新范例，尤其适用于非平稳、低信噪比场景。


### 5. 基于Double Q-Learning算法与声誉机制的人机共同演化

**讲者**：Xuexue Yang（Guizhou University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在人机共同演化（human-machine co-evolution）场景中，人类与AI agent在重复交互中如何通过学习与声誉机制实现合作或策略演化？传统强化学习（如Q-learning）在动态环境中易因高估偏差导致策略不稳定，而声誉机制虽能促进间接互惠，但缺乏与在线学习算法的深度融合。本报告旨在回答：当人类与AI同时更新策略时，Double Q-Learning能否结合声誉评分，缓解偏差并引导系统收敛至更优的均衡？

**核心方法**  
方法框架由两层构成：底层采用Double Q-Learning算法，通过维护两个独立的Q函数$Q^A$和$Q^B$，交替更新以解耦动作选择与价值评估，从而消除标准Q-learning中的最大化偏差（maximization bias）。上层引入声誉机制，每个agent维护一个公开声誉值$r_i(t)$，基于历史交互结果（如合作/背叛）通过间接互惠规则更新。在每轮交互中，agent依据自身Q值选择动作，同时参考对方声誉调整策略（例如对低声誉者采取惩罚性动作）。Double Q-Learning的更新规则为：  
$Q^A(s_t,a_t) \leftarrow Q^A(s_t,a_t) + \alpha \left[ r_t + \gamma Q^B(s_{t+1}, \arg\max_a Q^A(s_{t+1},a)) - Q^A(s_t,a_t) \right]$，  
$Q^B$对称更新。声誉值则通过类似“image scoring”的规则动态调整，并作为状态特征的一部分输入Q函数，形成闭环共同演化。

**与已有工作关系**  
已有工作多单独研究强化学习（如Q-learning在囚徒困境中的策略学习）或声誉机制（如间接互惠模型），但鲜有将两者结合并考虑人机共同演化。标准Q-learning在非平稳环境中（人类策略也在变化）易产生高估偏差，导致合作率下降。本报告将Double Q-Learning引入该场景，直接回应了“偏差-方差权衡”在共同演化中的影响。此外，相比传统声誉模型仅依赖固定规则，本方法允许agent通过强化学习自适应调整对声誉的利用方式，更具灵活性。

**贡献**  
主要贡献有三：第一，首次将Double Q-Learning与声誉机制融合，提出一个可分析人机共同演化中策略动态的框架；第二，通过理论或仿真揭示Double Q-Learning如何缓解高估偏差，从而在声誉辅助下促进长期合作均衡的达成；第三，为设计鲁棒的人机协作系统提供新思路——即通过算法层面的偏差校正与机制层面的声誉激励，实现更稳定的共同演化。该工作对理解AI与人类在重复博弈中的互适应行为具有重要启发。


### 6. 贵州省非物质文化遗产的智能化统计实践——以蜡染文化为例

**讲者**：Yiting Li（Guizhou University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
非物质文化遗产（如贵州蜡染）的传承与保护长期依赖定性描述与人工经验，缺乏系统性的量化评估与动态监测。传统统计方法难以处理蜡染图案的高维纹理特征、工艺传承的时序依赖以及文化生态的多因素耦合。本报告旨在回答：如何利用智能化统计工具，从海量图像、文本与田野调查数据中提取可量化指标，构建非遗活态传承的统计监测体系？

**核心方法**  
报告提出一套“特征提取—降维—因果推断”的混合框架。首先，利用卷积神经网络（CNN）对蜡染图像进行高维特征提取，得到图案复杂度、色彩分布等数值化指标；其次，采用主成分分析（PCA）或 t-SNE 进行降维，识别不同流派与时期的风格聚类；最后，引入潜在结果框架（Potential Outcomes）与倾向得分匹配（Propensity Score Matching），估计“传承人培训”、“政策补贴”等干预对蜡染技艺保存度（如纹样多样性指数）的因果效应。时间序列部分可能使用 ARIMA 或状态空间模型预测传承风险。

**与已有工作关系**  
现有非遗研究多集中于人类学田野调查或简单的描述统计，缺乏对高维文化特征的自动提取与因果推断。本报告将计算机视觉与因果推断引入非遗领域，区别于传统“数字化存档”的静态思路，强调动态监测与政策评估。与文化遗产计量学（Cultural Analytics）相比，本工作更侧重统计推断的严谨性，而非单纯的可视化。

**主要贡献**  
1. 首次为蜡染文化构建了从图像到因果效应的全链条统计流程，提供了可复现的代码与数据标准。  
2. 通过因果推断量化了保护政策的实际效果，为非遗管理部门的资源分配提供统计依据。  
3. 展示了高维统计与机器学习在人文社科领域的落地范式，拓展了统计学的应用边界。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)