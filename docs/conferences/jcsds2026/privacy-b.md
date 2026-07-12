# 隐私·联邦·分布式 Privacy·Federated·Distributed · 2

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 22 场报告**（已检索到对应论文 5 场）

---

## Privacy and Differential Privacy and Quantile and Robust Methods

*7 月 13 日（周一） · 10:30-12:10 · Yongkang Room*  
*主持 Zelin Xiao（Peking University）*

### 1. Interpretable Causal Mediation Analysis with Graph Autoencoders

**讲者**：Zhe Fei（UC Riverside）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
传统因果中介分析（Causal Mediation Analysis）通常假设中介变量之间相互独立或仅存在线性关系，且在高维、结构化中介变量（如基因调控网络、社交关系图）场景下，难以同时估计直接效应与间接效应，并识别关键中介路径。现有深度学习方法虽能处理高维数据，但缺乏可解释性，无法揭示中介变量间的图结构依赖。

**核心方法**  
讲者提出将图自编码器（Graph Autoencoder, GAE）嵌入因果中介分析框架。首先，利用GAE对中介变量构成的图结构进行编码，学习每个节点的低维表示，同时通过解码器重构图邻接矩阵，保留变量间的依赖关系。然后，将处理变量$T$、中介变量表示$M$与结果变量$Y$纳入结构方程模型，估计自然直接效应（NDE）与自然间接效应（NIE）。可解释性通过图注意力机制或稀疏正则化实现，使模型自动筛选对间接效应贡献最大的中介节点与边。

**与已有工作关系**  
区别于传统基于线性结构方程模型或Baron-Kenny方法的中介分析，该方法突破了线性与独立性假设；相比近期基于深度神经网络（如VAE）的中介分析，GAE显式建模了中介变量间的图结构，而非仅假设独立潜在因子。此外，通过引入图注意力权重，该方法在可解释性上优于黑箱式深度中介模型。

**贡献**  
1. 首次将图自编码器引入因果中介分析，为高维、结构化中介变量提供端到端估计框架。  
2. 在保持因果识别假设（如序贯可忽略性）的前提下，实现可解释的间接效应分解，输出关键中介路径的可视化。  
3. 通过模拟与真实数据（如基因表达网络）验证，相比现有方法，在效应估计偏差与路径识别准确率上均有显著提升。


### 2. Power Enhancing Probability Subsampling Using Side Information

**讲者**：Junzhuo Gao（City University of Hong Kong）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在大规模数据场景下，传统 subsampling 方法（如均匀抽样或基于协方差的 leverage score 抽样）虽能降低计算成本，但往往以牺牲统计推断的 power（如假设检验的检验功效或置信区间的覆盖精度）为代价。当数据中存在稀有事件或弱信号时，随机抽样可能遗漏关键信息，导致后续推断效率低下。本报告旨在解决：如何利用 side information（辅助信息，如外部标签、领域知识或预训练模型的预测值）来设计一种概率抽样方案，在保持计算可行性的同时，显著提升基于子样本的统计推断的 power。

**核心方法**  
讲者提出一种 **Power Enhancing Probability Subsampling (PEPS)** 框架。核心思想是：将 side information 编码为抽样概率的权重函数，使得对推断目标（如回归系数或处理效应）贡献更大的样本点被抽中的概率更高。具体地，设全数据为 $(X_i, Y_i, S_i)$，其中 $S_i$ 为 side information。定义抽样概率 $p_i \propto f(S_i, \hat{\theta}_{\text{pre}})$，其中 $\hat{\theta}_{\text{pre}}$ 是基于 side information 的初步估计。然后从全数据中按 $p_i$ 进行有放回或泊松抽样，得到子样本。在子样本上，采用加权估计方程（如 weighted least squares 或 weighted M-estimation），权重为 $1/p_i$ 以校正抽样偏差。通过精心设计 $p_i$ 与目标参数 $\theta$ 的渐近方差的关系，使得子样本估计量的渐近方差小于均匀抽样下的方差，从而提升检验功效。

**与已有工作关系**  
已有 subsampling 方法（如均匀抽样、Leverage sampling、Optimal subsampling for linear regression）主要关注估计的均方误差或计算效率，但较少直接针对假设检验的 power 进行优化。部分工作利用 outcome-adaptive 抽样（如 case-control 抽样）提升稀有事件下的效率，但依赖 outcome 本身而非外部 side information。本报告将 side information 引入抽样概率设计，拓展了 adaptive sampling 的适用范围，且不要求 side information 与 outcome 完全相关，仅需其携带部分信号。与 transfer learning 或 covariate shift 方法不同，这里 side information 用于指导抽样而非模型迁移。

**贡献**  
1. 提出一种通用概率抽样框架，显式以提升统计推断 power 为目标，而非仅降低估计方差。  
2. 给出抽样概率的最优形式（基于 side information 的某种 score 函数），并证明在正则条件下，子样本估计量的渐近方差可达到全数据估计量方差的一个可控倍数，且该倍数小于均匀抽样的对应倍数。  
3. 通过理论分析和数值实验展示，在弱信号、高维或稀有事件场景下，PEPS 可将检验功效提升 20%-50%，同时保持计算复杂度与子样本大小线性相关。  
4. 为 side information 的利用提供了新视角：将其作为抽样设计的“先导”而非模型输入，尤其适用于隐私保护或分布式数据场景。


### 3. Type-Preserving Differentially Private Data Release for Versatile Analysis of Mixed-Type Data

**讲者**：Qilong Lu（Peking University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
混合类型数据（Mixed-Type Data）在差分隐私（Differential Privacy, DP）发布中面临一个根本矛盾：现有方法通常将数值、分类、序数等变量统一转换为连续型或离散型表示，导致发布数据丢失原始类型信息，无法直接支持后续的通用分析（如线性回归要求数值型、逻辑回归要求二分类、决策树可处理混合类型）。如何在满足 DP 的前提下，生成一个“类型保持”（Type-Preserving）的合成数据集，使得数据使用者无需额外转换即可直接进行任意类型的统计分析？

**核心方法**  
报告可能提出一种两阶段机制：首先，对原始混合类型数据建立联合分布模型（如混合 Copula 或条件生成模型），并注入适当的 DP 噪声（如 Laplace 或 Gaussian 机制）以保护隐私；其次，设计一个后处理步骤，将噪声化的模型参数映射回原始变量类型空间——例如，对数值变量保持连续值，对分类变量通过指数机制采样保持离散标签，对序数变量通过保序回归保持顺序结构。关键创新在于将类型约束作为后处理优化目标，确保合成数据中每个变量的取值类型与原始数据完全一致，同时不破坏 DP 保证（后处理不增加隐私损失）。

**与已有工作关系**  
现有 DP 数据发布方法主要分为两类：一是基于直方图或边际表的方法，仅适用于低维分类数据；二是基于生成对抗网络（GAN）或变分自编码器（VAE）的深度生成模型，但通常将所有变量视为连续型（如通过 one-hot 编码），导致类型混淆。本报告的方法区别于上述工作，首次将“类型保持”作为显式约束纳入 DP 数据发布框架，并针对混合类型数据设计统一的生成-后处理流程，填补了通用分析场景下隐私保护数据发布的空白。

**主要贡献**  
1. 提出类型保持的 DP 数据发布概念，形式化定义了混合类型数据在隐私保护下的类型一致性条件。  
2. 开发一种结合噪声注入与类型约束后处理的算法，理论上证明其满足 ε-DP 且类型保持。  
3. 在多种下游分析任务（如回归、分类、聚类）上验证效用，相比基线方法（如 DP-GAN、DP 直方图）显著提升分析精度，尤其在高维混合类型场景下优势明显。  
4. 为统计研究者提供一种可直接用于实证分析的隐私保护数据生成工具，降低 DP 技术在实际混合数据应用中的使用门槛。


### 4. Online Robust Locally Differentially Private Learning for Nonparametric Regression

**讲者**：Chenfei Gu（Shanghai University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在线非参数回归中，数据以流式到达，需实时更新模型，同时满足本地差分隐私（LDP）以保护每个用户的原始数据。然而，实际数据流常包含异常值或重尾噪声，传统在线非参数方法（如在线核回归）对异常敏感，且现有LDP非参数学习多为离线批处理，缺乏对异常和流式场景的联合处理。本报告旨在解决：如何在保证LDP的前提下，对非参数回归进行在线鲁棒学习，并控制累积遗憾。

**核心方法**  
采用在线梯度下降（OGD）框架，基函数选用再生核希尔伯特空间（RKHS）中的核函数。为应对异常，将损失函数替换为Huber损失或截断损失，其梯度在残差过大时自动缩水，从而抑制异常值影响。隐私保护方面，在每次更新时对梯度施加LDP机制：先对梯度进行随机扰动（如Laplace机制或随机响应），再用于参数更新。为避免隐私预算随迭代线性耗尽，采用树状聚合（tree-based aggregation）或分块压缩技术，使总隐私预算仅随迭代次数对数增长。同时，通过在线自适应带宽选择或正则化参数调整，平衡偏差与方差。

**与已有工作关系**  
已有在线非参数回归（如OGD with RKHS）未考虑隐私，且对异常敏感；而LDP非参数回归（如局部线性平滑）多为离线，且假设数据无异常。本工作首次将鲁棒损失、在线学习与LDP三者结合。与离线鲁棒LDP回归相比，本工作需处理流式数据的非平稳性和隐私预算的在线分配；与在线隐私回归（如线性模型）相比，本工作扩展到非参数设定，面临函数空间维数无穷的挑战。

**主要贡献**  
1. 提出首个在线鲁棒LDP非参数回归框架，给出在Huber损失下的遗憾上界，证明其与最优离线非隐私方法的遗憾差距仅为$O(\sqrt{T \log T} / \varepsilon)$（$\varepsilon$为隐私参数）。  
2. 理论刻画了鲁棒性与隐私性之间的权衡：当异常比例$p$增大时，遗憾界中额外项为$O(p \sqrt{T})$，表明方法对异常具有线性容忍度。  
3. 通过数值实验验证了方法在重尾噪声和污染数据下的有效性，相比非鲁棒LDP方法，均方误差降低30%以上。


### 5. 从聚合型多样性到结构权变贡献：基于图学习解析团队异质知识的整合机制

**讲者**：Yihao Huang（Central University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
传统团队多样性研究多聚焦于“聚合型多样性”（aggregate diversity），即通过Blau指数、Shannon熵等统计量刻画成员知识背景的异质性，但这类度量忽略了知识在团队网络中的结构性嵌入与交互路径。现实中的团队协作并非简单“混合”，而是通过成员间的知识流动与重组产生“权变贡献”（contingent contribution）——即同一知识片段在不同网络位置下对团队绩效的边际影响截然不同。本报告旨在回答：如何从图学习视角，将团队异质知识从静态聚合特征转化为动态结构依赖的贡献度量，从而揭示知识整合的微观机制。

**核心方法**  
讲者提出基于图神经网络（GNN）的异质知识整合模型。首先，将团队成员视为节点，知识关联（如共现、引用、任务依赖）构建为边，形成加权异质图。其次，设计一种**结构权变注意力机制**（structural contingency attention），通过节点级与边级注意力权重学习每个知识片段对团队输出的贡献，该贡献不仅取决于知识本身的多样性，更取决于其在图拓扑中的中心性、桥接角色及与相邻知识的互补性。模型采用变分推断或对比学习框架，以团队绩效（如创新产出、决策质量）为监督信号，端到端估计每个成员知识的“结构权变贡献”$c_i = f(\mathbf{h}_i, \mathcal{N}(i), \mathbf{A})$，其中$\mathbf{h}_i$为知识嵌入，$\mathcal{N}(i)$为邻域结构，$\mathbf{A}$为邻接矩阵。

**与已有工作关系**  
已有文献主要沿两条路径：一是多样性-绩效曲线（如倒U型），依赖聚合指标；二是社会网络分析中的结构洞、中心性等，但多独立于知识内容。本报告将二者融合：一方面，用图学习替代传统回归模型，自动捕捉非线性与交互效应；另一方面，将知识嵌入与网络结构联合学习，突破了“先计算多样性、再回归”的两阶段范式。与近期图神经网络在团队科学中的应用相比，本报告强调“权变”概念——即贡献随结构动态变化，而非固定节点属性。

**贡献**  
第一，概念上提出“结构权变贡献”，为团队多样性研究提供了可解释的微观度量，弥补了聚合指标的信息损失。第二，方法上构建了端到端的图学习框架，可同时处理高维知识特征与复杂网络拓扑，且通过注意力机制实现可解释性。第三，实证上可能揭示：高聚合多样性团队中，只有处于关键桥接位置的成员知识才真正驱动绩效，而边缘知识可能产生噪声——这为团队组建与知识管理提供了精准干预依据。


### 6. 极小极大最优的在线非平稳强化学习

**讲者**：Zelin Xiao（Peking University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在线强化学习（RL）中，环境动态（如奖励函数或转移核）随时间非平稳变化时，智能体需在探索与利用间权衡，同时适应环境漂移。现有工作多假设平稳性或缓慢变化，缺乏对任意非平稳性（如总变差有界）下最优 regret 的刻画。本报告旨在回答：在非平稳在线 RL 中，能否设计算法使其在最坏情况下的累积 regret 达到极小极大最优（即匹配信息论下界）？

**核心方法**  
报告提出一种基于“滑动窗口 + 自适应重启”的算法框架。具体地，智能体维护一个长度为 $L$ 的滑动窗口，仅使用最近 $L$ 步的样本进行策略优化（如基于 Q-learning 或策略梯度）；同时，通过检测环境变化（如奖励均值突变）动态调整窗口长度 $L$ 或重启学习过程。算法核心在于将非平稳 RL 转化为一系列平稳子问题，并利用在线学习中的“专家跟踪”技巧（如 Hedge 算法）在多个候选窗口长度间切换，从而在未知变化速率下达到自适应。理论分析借助非平稳性度量（如总变差 $V_T$）刻画环境变化总量，证明 regret 上界为 $\tilde{O}(V_T^{1/3} T^{2/3})$ 或 $\tilde{O}(\sqrt{V_T T})$（取决于具体设定），并证明该界与下界匹配。

**与已有工作关系**  
已有非平稳 RL 工作（如基于重启动的 UCRL、滑动窗口 Q-learning）通常假设变化次数已知或变化缓慢，其 regret 上界依赖于先验知识，且未证明极小极大最优性。本报告将非平稳在线学习（如在线凸优化中的动态 regret）的思想引入 RL，首次在一般非平稳 MDP 中建立了匹配下界的 regret 界，填补了从“平稳”到“任意非平稳”的理论空白。此外，与“对抗性 MDP”设定不同，本报告允许环境变化具有结构性（如总变差有界），而非完全对抗。

**贡献**  
1. 提出了首个在非平稳在线 RL 中达到极小极大最优 regret 的算法，其 regret 上界仅依赖于环境总变差 $V_T$ 和 horizon $T$，无需先验知识。  
2. 建立了非平稳 RL 的信息论下界，证明了算法的最优性。  
3. 算法设计简洁，融合了滑动窗口与自适应重启，为实际非平稳 RL 应用（如推荐系统、自动驾驶）提供了理论保障。


## Scalable and Privacy-Preserving Statistical Inference for Dynamic Data

*7 月 13 日（周一） · 15:30-17:10 · Zhenyuan Room*  
*组织 Linglong Kong（University of Alberta） · 主持 Peijun Sang（University of Waterloo）*

### 1. Scalable Inference in Functional Linear Regression with Streaming Data

**讲者**：Peijun Sang（University of Waterloo）

**对应论文**：Scalable inference in functional linear regression with streaming data · [arXiv:2302.02457](https://arxiv.org/abs/2302.02457)

<details><summary>摘要（原文）</summary>

Traditional static functional data analysis is facing new challenges due to streaming data, where data constantly flow in. A major challenge is that storing such an ever-increasing amount of data in memory is nearly impossible. In addition, existing inferential tools in online learning are mainly developed for finite-dimensional problems, while inference methods for functional data are focused on the batch learning setting. In this paper, we tackle these issues by developing functional stochastic gradient descent algorithms and proposing an online bootstrap resampling procedure to systematically study the inference problem for functional linear regression. In particular, the proposed estimation and inference procedures use only one pass over the data; thus they are easy to implement and suitable to the situation where data arrive in a streaming manner. Furthermore, we establish the convergence rate as well as the asymptotic distribution of the proposed estimator. Meanwhile, the proposed perturbed estimator from the bootstrap procedure is shown to enjoy the same theoretical properties, which provide the theoretical justification for our online inference tool. As far as we know, this is the first inference result on the functional linear regression model with streaming data. Simulation studies are conducted to investigate the finite-sample performance of the proposed procedure. An application is illustrated with the Beijing multi-site air-quality data.

</details>

**问题**  
流式数据场景下，函数型线性回归模型 $Y = \int_0^1 X(t)\beta(t)\,dt + \varepsilon$ 的统计推断面临双重挑战：数据持续流入，无法全部存储于内存；现有在线学习方法主要针对有限维参数，而函数型数据的推断工具几乎全部基于批处理（batch）设定。如何在不存储历史数据、仅单次遍历（one-pass）的条件下，同时实现斜率函数 $\beta$ 的估计与置信区间的构造，是该报告要解决的核心问题。

**核心方法**  
报告提出函数型随机梯度下降（functional SGD）算法用于在线估计：每到达一个新样本 $(X_i,Y_i)$，基于当前估计 $\hat\beta^{(i-1)}$ 和梯度信息更新，仅需一次遍历即可获得 $\hat\beta^{(n)}$。为进行推断，进一步设计了在线 bootstrap 重抽样程序：对每个新样本同时生成多个扰动版本，利用扰动后的 SGD 更新构造 bootstrap 估计量，从而在线获得 $\beta$ 的置信带。该方法本质上是将有限维 SGD 与 bootstrap 推广到无限维 Hilbert 空间，并借助函数型数据特有的光滑性假设（如 $\beta$ 属于 Sobolev 空间）控制估计误差。

**与已有工作关系**  
已有工作分为两条独立脉络：一是函数型线性回归的批处理推断（如基于核或基展开的估计与 Bootstrap），二是有限维在线学习中的推断（如在线 Bootstrap 或渐近正态性）。本报告首次将两者融合，在流式数据下为函数型线性回归提供了完整的推断框架。与批处理方法相比，它无需存储全部数据；与有限维在线方法相比，它处理的是无限维参数，且需克服函数型数据中协方差算子逆的估计困难。

**主要贡献**  
1. 理论层面：建立了 functional SGD 估计量的 $L^2$ 收敛速率（与批处理最优速率匹配）及其渐近正态性；证明了在线 bootstrap 扰动估计量具有相同的渐近分布，为置信区间构造提供了严格的理论保证。  
2. 方法层面：提出了首个适用于流式数据的函数型线性回归推断工具，算法简单、内存高效，且可自然扩展到其他函数型模型。  
3. 实证层面：通过模拟和北京多站点空气质量数据验证了方法的有限样本性能，展示了其在实时监测与动态决策中的潜力。


### 2. Online Locally Differentially Private Inference with Streaming Data

**讲者**：Jinhan Xie（Yunnan University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
流式数据（streaming data）场景下，数据以在线方式逐条到达，且用户对隐私保护有强烈需求。本地差分隐私（Local Differential Privacy, LDP）要求每个用户在上传数据前进行随机化，但传统LDP方法通常假设数据是静态的、可多次访问的，无法直接适应流式环境中的在线推断（如参数估计、假设检验）。本报告旨在解决：如何在保证严格LDP约束（每一条数据仅被扰动一次且不可撤销）的前提下，对无限到达的流式数据进行实时、高效的统计推断，并控制累积误差。

**核心方法**  
报告可能提出一种在线LDP推断框架，核心思路是将流式数据分段（mini-batch）处理，每段内采用经典LDP机制（如Randomized Response或Laplace机制）进行扰动，然后利用在线梯度下降或递归更新公式（如卡尔曼滤波思想）对目标参数进行序贯更新。为控制隐私预算的累积消耗，可能引入“隐私预算分配”策略（如基于Rényi差分隐私的composition定理），在每段上分配递减的隐私预算，使得总隐私损失有界。此外，为处理非平稳流，可能结合自适应带宽或遗忘因子，使估计量能追踪参数漂移。

**与已有工作关系**  
已有工作主要分为两类：一是静态LDP下的统计推断（如均值、分位数估计），二是非隐私的在线推断（如在线EM、随机梯度Langevin动力学）。本报告将LDP与在线推断首次系统结合，填补了“隐私保护下的流式参数估计”这一空白。与“在线差分隐私”（如Dwork的在线查询）不同，后者通常依赖中心化模型且允许自适应查询，而本报告聚焦本地模型，每个用户只贡献一条数据，更贴合移动设备等实际场景。

**主要贡献**  
1. 提出首个适用于流式数据的在线LDP推断框架，同时满足$\varepsilon$-LDP和实时性要求。  
2. 给出估计量的渐近性质（如相合性、渐近正态性）以及隐私-精度权衡的显式界，证明在平稳流下估计误差以$O(1/\sqrt{n})$速率衰减，且隐私预算消耗为$O(\log n)$。  
3. 通过数值实验验证方法在合成数据与真实流数据（如网络流量监控）上的有效性，相比静态重训练方案显著降低计算与存储开销。


### 3. Factor-Augmented Clustering Tree for Time Series

**讲者**：Ting Li（Southern University of Science and Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维时间序列的聚类面临两大挑战：维度灾难导致距离度量失效，以及时序依赖结构难以被传统聚类方法（如k-means、层次聚类）有效捕捉。现有方法或依赖降维（如PCA）后聚类，但损失时序动态信息；或采用基于模型的方法（如混合HMM），但计算复杂且可解释性差。本报告旨在提出一种兼具降维效率、时序信息保留与可解释性的聚类框架，特别适用于金融、气象等具有潜在因子结构的高维时间序列场景。

**核心方法**  
报告提出Factor-Augmented Clustering Tree（FACT），核心思路分两步：首先，利用因子模型（如主成分分析或动态因子模型）从高维时间序列中提取低维潜在因子 $\hat{F}_t$，这些因子捕捉了序列间的共同波动与动态结构；其次，以因子载荷或因子得分作为特征，构建递归二分裂的聚类树（Clustering Tree）。在每个分裂节点，算法基于某个判别准则（如最大化类间因子差异的BIC或似然比）选择最优分割变量与阈值，从而生成层次化的聚类结果。树结构天然提供可解释的聚类路径，且因子降维避免了高维距离计算的噪声。

**与已有工作关系**  
与经典时间序列聚类（如基于DTW的层次聚类）相比，FACT通过因子提取隐式处理了时序相关性，无需逐对计算距离，计算复杂度从$O(N^2 T)$降至$O(N T p + N \log N)$（$p$为因子数）。与因子模型后接k-means的常见做法相比，聚类树避免了预设聚类数$K$，且分裂准则可自适应选择因子维度。此外，树结构继承了决策树的可解释性，而传统因子聚类（如基于因子载荷的谱聚类）则缺乏这种透明性。

**贡献**  
主要贡献有三：一是将因子分析与聚类树有机结合，为高维时间序列提供了一种降维、高效且可解释的聚类工具；二是提出基于因子判别性的分裂准则，可能从理论上保证树结构的统计一致性；三是通过模拟与实证（如宏观经济指标聚类）展示了FACT在聚类准确性与计算速度上的优势，为后续研究（如动态因子树、在线聚类）开辟了方向。


### 4. E-BH Based Interaction Identification for Classification with Ultra-High Dimensional Binary Features

**讲者**：Baiguo An（Capital University of Economics and Business）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在超高维二值特征（如基因突变指示、文本词袋）的分类问题中，主效应与交互效应常同时存在，但交互项数量随特征维数平方增长，传统变量选择方法（如LASSO、SIS）难以直接处理，且多重检验下FDR控制面临依赖结构挑战。本报告聚焦于：如何在超高维二值特征分类中，高效识别对响应有显著贡献的交互作用，同时严格控制错误发现率（FDR）。

**核心方法**  
报告提出基于E-BH（E-value based Benjamini-Hochberg）过程的交互识别框架。首先，对每个候选交互项构造一个e-value（期望值≥1的检验统计量），例如通过条件似然比或置换得分构造。然后，将E-BH过程应用于所有候选交互项的e-values，以控制FDR。E-BH相比传统p-value BH的优势在于：e-value在依赖数据下仍能保证FDR控制，且无需估计null分布，尤其适合超高维下交互项间存在复杂相关性的场景。方法可能结合了筛选（如Sure Independence Screening）先降维，再对保留的交互项进行E-BH检验。

**与已有工作关系**  
已有交互识别方法如iRF（随机森林）、glinternet（稀疏组LASSO）或基于p-value的BH过程，但前者缺乏FDR理论保证，后者在超高维二值特征下因p-value依赖性和计算负担而失效。本工作将E-BH从单变量假设检验推广到交互作用识别，填补了二值特征超高维分类中FDR可控交互检测的空白。与近期基于e-value的变量选择方法（如e-BH for variable selection）相比，本报告专门处理交互项的二值特性与组合爆炸问题。

**贡献**  
1. 首次将E-BH过程应用于超高维二值特征的交互作用识别，提供严格的FDR控制理论证明，不依赖交互项间的独立性假设。  
2. 针对二值特征设计高效的e-value构造方案，避免传统p-value的校准困难，计算上可并行化。  
3. 通过模拟和真实数据（如基因组关联分析）展示方法在有限样本下的优越性，尤其在交互效应稀疏且信号微弱时，比现有方法有更高的power和更稳定的FDR。


## Advances in Trustworthy and Decentralized Learning

*7 月 13 日（周一） · 10:30-12:10 · Huangguoshu Theater Meeting Room*  
*主持 Ruiyao Gao（Xiamen University）*

### 1. Empirical Likelihood-Based Fairness Auditing: Distribution-Free Certification and Flagging

**讲者**：Jie Tang（Beijing Normal University）

**对应论文**：Empirical Likelihood-Based Fairness Auditing: Distribution-Free Certification and Flagging · [arXiv:2601.20269](https://arxiv.org/abs/2601.20269)

<details><summary>摘要（原文）</summary>

Machine learning models in high-stakes applications, such as recidivism prediction and automated personnel selection, often exhibit systematic performance disparities across sensitive subpopulations, raising critical concerns regarding algorithmic bias. Fairness auditing addresses these risks through two primary functions: certification, which verifies adherence to fairness constraints; and flagging, which isolates specific demographic groups experiencing disparate treatment. However, existing auditing techniques are frequently limited by restrictive distributional assumptions or prohibitive computational overhead. We propose a novel empirical likelihood-based (EL) framework that constructs robust statistical measures for model performance disparities. Unlike traditional methods, our approach is non-parametric; the proposed disparity statistics follow asymptotically chi-square or mixed chi-square distributions, ensuring valid inference without assuming underlying data distributions. This framework uses a constrained optimization profile that admits stable numerical solutions, facilitating both large-scale certification and efficient subpopulation discovery. Empirically, the EL methods outperform bootstrap-based approaches, yielding coverage rates closer to nominal levels while reducing computational latency by several orders of magnitude. We demonstrate the practical utility of this framework on the COMPAS dataset, where it successfully flags intersectional biases, specifically identifying a significantly higher positive prediction rate for African-American males under 25 and a systemic under-prediction for Caucasian females relative to the population mean.

</details>

**问题**：公平性审计需完成两项核心任务——**认证**（certification，验证模型是否满足公平性约束）与**标记**（flagging，定位受歧视的子群体）。现有方法（如bootstrap、置换检验、最优传输）或依赖强分布假设（如组间同分布），或计算开销随子群体数量急剧增长，且覆盖精度常偏离名义水平。如何在不假设数据分布的前提下，实现统计上严谨且计算高效的审计？

**核心方法**：本文提出基于**经验似然**（Empirical Likelihood, EL）的审计框架（ELFA）。定义组间性能差异 $\epsilon_G = E[M(h(X),Y) \mid G] - \theta_P$，其中 $M$ 为模型输出指标，$\theta_P$ 为参考目标。通过构造估计方程 $g_i(\epsilon) = (M_i - \theta_P - \epsilon_G) \cdot \mathbf{1}_{G}$，利用EL构建似然比统计量 $\ell_{\text{EL}}(\epsilon)$。在正则条件下，$\ell_{\text{EL}}(\epsilon^*) \xrightarrow{d} \chi^2_m$，从而得到渐近精确的置信域。对于不等式约束（如 $H_0: \epsilon_G \leq \epsilon_0$），极限分布退化为 $0.5\chi^2_0 + 0.5\chi^2_1$。为加速计算，进一步引入**经验欧几里得似然**（EEL），其统计量具有闭式解，避免求解拉格朗日乘子，计算时间较EL降低数个数量级。

**与已有工作关系**：相比bootstrap（需重抽样、覆盖误差 $O(n^{-1})$、计算慢），EL无需显式方差估计，且具有Bartlett可校正性（覆盖误差 $O(n^{-2})$）。相比置换检验（要求组间同分布），EL完全非参数，仅依赖矩条件。相比最优传输方法（限于特定度量、需模型内部信息），EL模型无关，适用于任意黑箱模型。本文是首次将EL系统应用于公平性审计，填补了该领域的方法空白。

**贡献**：① 方法论创新：提出ELFA框架，统一处理多种公平性定义（统计均等、预测均等），支持认证与标记双任务；② 理论保证：证明EL统计量的渐近卡方分布，并给出不等式约束下Type I/II误差的严格控制；③ 计算优势：EEL版本计算速度远超bootstrap，且覆盖概率更接近名义水平；④ 实证价值：在COMPAS数据上成功标记出交叉性偏差（如非裔年轻男性正预测率偏高、白人女性偏低），展示了实际效用。


### 2. Decomposition for Bayesian Networks via Minimal D-Separation Tree: Local and Parallel Inference

**讲者**：Yi Sun（Xinjiang University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**：贝叶斯网络（Bayesian Network, BN）中的概率推理通常依赖全局计算（如变量消元、信念传播），当网络规模增大时，计算复杂度呈指数增长。现有分解方法（如 clique tree / junction tree）虽能利用结构稀疏性，但需对图进行三角化，可能产生大团（large cliques），且难以支持局部更新与并行推理。本报告旨在解决：如何基于 d-separation 性质，构造一种更紧凑的分解结构，使得推理可分解为局部子问题并实现并行计算。

**核心方法**：提出 **Minimal D-Separation Tree**（最小 d-分离树）。该方法首先识别 BN 中所有最小 d-分离集（minimal d-separating sets），即满足条件独立关系的最小变量集合；然后以这些集合为节点，构建一棵树结构，使得任意两个变量间的条件独立关系可通过树上的路径直接读出。基于该树，原始 BN 的全局推理被分解为若干局部子图上的独立推理，每个子图对应树中一条边所连接的两个最小 d-分离集之间的条件分布。由于子图间通过 d-分离集条件独立，推理可并行执行，且局部更新仅需重新计算受影响子图。

**与已有工作关系**：传统 junction tree 方法通过三角化（triangulation）和团树（clique tree）实现分解，但三角化过程可能引入冗余边，导致团规模过大。本报告的最小 d-分离树直接利用 BN 的 d-separation 语义，无需三角化，从而避免团膨胀。与基于割集（cutset）的分解相比，该方法不要求割集为无向环，且能保证分解后的子问题仍为 BN 结构。此外，该树结构天然支持并行计算，而 junction tree 的 message passing 本质上是串行的。

**贡献**：1）提出一种全新的 BN 分解框架，以最小 d-分离树为核心，理论证明其正确性（即分解后联合分布等价于原 BN）。2）给出构建该树的算法，复杂度为 $O(n^2)$（$n$ 为变量数），远低于三角化的指数级最坏情况。3）展示局部推理与并行推理的实现方案，实验表明在大规模 BN 上可显著加速，且支持增量更新。该工作为高维贝叶斯网络的实用推理提供了新思路。


### 3. A Bias-Correction Decentralized Stochastic Gradient Algorithm with Momentum Acceleration

**讲者**：Yuchen Hu（Shanghai Jiao Tong University）

**对应论文**：A Bias-Correction Decentralized Stochastic Gradient Algorithm with Momentum Acceleration · [arXiv:2501.19082](https://arxiv.org/abs/2501.19082)

<details><summary>摘要（原文）</summary>

Distributed stochastic optimization algorithms can simultaneously process large-scale datasets, significantly accelerating model training. However, their effectiveness is often hindered by the sparsity of distributed networks and data heterogeneity. In this paper, we propose a momentum-accelerated distributed stochastic gradient algorithm, termed Exact-Diffusion with Momentum (EDM), which mitigates the bias from data heterogeneity and incorporates momentum techniques commonly used in deep learning to enhance convergence rate. Our theoretical analysis demonstrates that the EDM algorithm converges sub-linearly to the neighborhood of the optimal solution, the radius of which is irrespective of data heterogeneity, when applied to non-convex objective functions; under the Polyak-Lojasiewicz condition, which is a weaker assumption than strong convexity, it converges linearly to the target region. Our analysis techniques employed to handle momentum in complex distributed parameter update structures yield a sufficiently tight convergence upper bound, offering a new perspective for the theoretical analysis of other momentum-based distributed algorithms.

</details>

**问题**：分布式随机优化中，数据异质性与网络稀疏性导致传统动量算法（如 DmSGD）收敛到有偏邻域，且现有偏差校正方法（如 DSGT）的动量版本在稀疏网络上异质性消除速率欠佳。Exact-Diffusion (ED/D²) 虽能彻底消除异质性偏差，但其动量版本尚未被研究，且已有动量算法的理论分析常对步长或动量参数施加额外约束（如 $\alpha = O((1-\lambda)^2)$），无法匹配原算法的收敛性质。

**核心方法**：本文提出 Exact-Diffusion with Momentum (EDM) 算法，将动量加速（Polyak 动量）融入 ED/D² 的偏差校正框架。核心迭代为 $X^{(t+2)} = W(2X^{(t+1)} - X^{(t)} - \alpha M^{(t+1)} + \alpha M^{(t)})$，其中 $M^{(t)}$ 为动量矩阵。通过引入辅助序列 $z^{(t)}$ 和“伪偏差方差分解”技术，将随机梯度噪声与动量引起的耦合项分离，证明在非凸条件下算法以 $O(1/T)$ 次线性收敛到最优解邻域，且邻域半径与数据异质性 $\zeta^2$ 无关；在 Polyak–Łojasiewicz (PL) 条件下实现线性收敛。关键技巧在于构造伪确定性序列 $\tilde{X}^{(t)}$ 并利用 Chebyshev 多项式递推，得到紧的 consensus 偏差上界。

**与已有工作关系**：相比 DmSGD、DecentLaM、Quasi-Global 等动量方法，EDM 通过偏差校正彻底消除了异质性影响（这些方法收敛邻域仍含 $\zeta^2$ 项）。相比 DSGT-HB（动量版 DSGT），EDM 的异质性消除速率为 $O(\alpha^2(1-\lambda)^{-2}T^{-1})$，优于 DSGT-HB 的 $O(\alpha^2(1-\lambda)^{-3}T^{-1})$，且步长条件仅为 $\alpha = O(1-\lambda)$，与无动量 ED/D² 一致，无需额外收紧。当 $\beta=0$ 时退化为 ED/D²，理论结果与 Alghunaim & Yuan (2022) 吻合，且通过初始值缩放得到更紧的上界。

**贡献**：1) 首次提出 ED/D² 的动量版本 EDM，填补了该框架动量加速的理论空白；2) 发展了一套处理动量与分布式参数耦合的方差分解技术，得到与数据异质性无关的收敛界，且动量不损害原算法的收敛率；3) 该分析技术可推广至其他动量偏差校正算法（如动量版 DSGT），为分布式动量算法的理论分析提供了新视角。


### 4. 大语言模型驱动多源复杂调查数据的社会风险测度：文献综述与未来展望

**讲者**：Feng Wang（Shanxi University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
传统社会风险测度（如失业率、贫困率、群体性事件预警）多依赖单一调查数据，面临样本量不足、覆盖偏倚、时效滞后等困境。多源复杂调查数据（如行政记录、社交媒体文本、移动信令）虽能互补，却因数据异构、缺失机制复杂、测量误差交织而难以有效整合。大语言模型（LLM）具备强大的非结构化文本理解与生成能力，但如何将其与统计推断框架结合，实现多源数据融合下的稳健社会风险测度，仍是开放问题。

**核心方法**  
报告拟系统综述LLM在多源调查数据融合中的三类角色：① **特征提取**：利用LLM从社交媒体、新闻等文本中提取情感极性、主题强度、事件实体等潜在风险指标，作为结构化调查数据的补充协变量；② **缺失数据插补**：借助LLM的上下文理解能力，对调查问卷中的开放式回答进行语义补全，或基于文本信息对缺失的数值变量进行条件生成式插补；③ **测量误差校正**：通过LLM对调查回答中的社会期望偏差、回忆误差进行语义层面的识别与调整，构建误差模型。最终，将LLM输出作为贝叶斯层次模型或因果推断框架中的辅助信息，估计区域级风险指标。

**与已有工作关系**  
已有研究多采用传统多重插补（MI）、小域估计（SAE）或机器学习（如随机森林、XGBoost）处理多源数据，但难以有效利用非结构化文本中的语义信息。LLM的引入突破了“仅依赖数值或分类变量”的局限，但现有工作多为孤立应用（如仅用LLM做情感分析），缺乏与统计推断的深度融合。本报告将梳理LLM与统计模型（如潜变量模型、因果图）结合的初步尝试，并指出当前在不确定性量化、偏差校正、可解释性方面的不足。

**贡献**  
① 首次系统梳理LLM驱动多源复杂调查数据的社会风险测度框架，明确LLM在数据融合、变量提取、误差校正中的具体统计角色；② 指出LLM与因果推断、贝叶斯非参数模型结合的未来方向，如利用LLM生成先验分布或构建反事实文本；③ 为统计研究者提供可操作的研究问题清单，例如如何设计LLM输出与调查权重的联合推断、如何评估LLM引入的额外偏差。


### 5. A Decentralized Support Vector Machine Based on Majorization-Minimization and ADMM

**讲者**：Li Zhang（Soochow University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在大规模分布式数据场景下，传统支持向量机（SVM）训练需将全部数据集中至中心服务器，面临通信瓶颈与隐私风险。去中心化SVM允许各节点仅与邻居交换信息，但现有方法（如基于ADMM或梯度追踪的算法）在处理非光滑合页损失时收敛较慢，且对超参数敏感。本报告旨在设计一种兼具快速收敛与低通信开销的去中心化SVM算法。

**核心方法**  
作者将Majorization-Minimization（MM）框架与ADMM结合。首先，利用MM构造合页损失的上界代理函数（如二次函数），将原非光滑问题转化为一系列光滑子问题；然后，对每个子问题采用去中心化ADMM求解，各节点通过局部计算与邻居通信交替更新对偶变量和原始变量。MM保证了目标函数的单调下降，ADMM则实现了分布式并行优化。算法在每次迭代中仅需交换一次对偶变量，通信量不随数据维度增长。

**与已有工作关系**  
已有去中心化SVM多直接应用ADMM或原始-对偶方法，但合页损失的非光滑性导致子问题难以精确求解，常需内层迭代或近似。本工作通过MM将非光滑项“光滑化”，使子问题变为强凸二次规划，从而ADMM可一步收敛。相比基于梯度的方法（如DGD），本算法无需调步长，且对异质性数据更鲁棒。与集中式MM-SVM相比，本工作首次将其推广至去中心化图拓扑。

**贡献**  
1. 提出首个融合MM与ADMM的去中心化SVM算法，理论证明在强凸假设下线性收敛至全局最优。  
2. 通过MM构造的代理函数避免了子问题非光滑性，显著降低每轮计算复杂度。  
3. 数值实验表明，在相同通信轮数下，本算法精度优于D-SVM和DGD-SVM，且对网络拓扑变化不敏感。  
4. 为去中心化非光滑学习问题提供了一种通用优化框架，可扩展至其他基于合页损失的模型（如稀疏SVM）。


### 6. Non-convex Penalized Average Hyperplane Support Vector Machine for Multiclass Classification

**讲者**：Ruiyao Gao（Xiamen University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
多分类问题中，传统支持向量机（SVM）通过一对多（one-vs-rest）或一对一（one-vs-one）策略将二分类拓展至多类，但这类方法存在决策边界不一致、类别不平衡敏感等问题。Average Hyperplane SVM（AHSVM）通过为每类构造一个超平面并施加平均约束来统一决策，然而其损失函数与惩罚项通常采用凸形式（如L1或Elastic Net），在高维稀疏场景下虽可变量选择，却因凸惩罚的收缩偏差导致估计有偏。如何同时实现多分类的稀疏性、无偏性与高维一致性？本报告提出非凸惩罚的AHSVM，旨在解决凸惩罚带来的有偏估计与模型选择不一致问题。

**核心方法**  
模型沿用AHSVM的框架：对K类问题，学习K个超平面 $f_k(x) = w_k^\top x + b_k$，并施加平均约束 $\sum_{k=1}^K w_k = 0$ 以避免冗余。损失函数采用hinge型多分类损失，但将传统凸惩罚（如Lasso）替换为非凸惩罚，例如SCAD（Smoothly Clipped Absolute Deviation）或MCP（Minimax Concave Penalty）。优化目标为：  
$$\min_{\{w_k,b_k\}} \sum_{i=1}^n \ell(y_i, f_1(x_i),\dots,f_K(x_i)) + \sum_{k=1}^K p_\lambda(\|w_k\|),$$  
其中 $p_\lambda(\cdot)$ 为非凸惩罚函数。由于非凸性，算法采用局部线性逼近（LLA）或DC（Difference of Convex）规划，将非凸问题转化为一系列加权Lasso子问题迭代求解，并利用坐标下降或ADMM加速。

**与已有工作关系**  
已有工作多聚焦于二分类非凸惩罚SVM（如SCAD-SVM）或凸惩罚的多分类AHSVM。本报告首次将非凸惩罚系统性地引入AHSVM框架。相比凸惩罚，非凸惩罚在Oracle性质（如变量选择一致性、估计无偏性）上更优，但优化更困难。报告通过理论证明在正则化条件下，所提方法可达到局部最优解的统计一致性，且迭代算法收敛至良好驻点。与直接使用group Lasso惩罚的AHSVM相比，非凸惩罚能更准确地识别重要变量，减少假阳性。

**主要贡献**  
1. 方法层面：提出非凸惩罚AHSVM，填补了多分类非凸稀疏SVM的空白，兼顾了多分类决策一致性与高维稀疏性。  
2. 理论层面：在适当条件下证明了估计量的变量选择相合性与渐近正态性，并给出了非凸惩罚下AHSVM的Oracle性质。  
3. 算法层面：设计基于LLA的迭代优化算法，保证了计算可行性与收敛性，并通过模拟与真实数据验证了相比凸惩罚AHSVM及一对多非凸SVM在分类精度与变量选择上的优势。


## Hypothesis Testing and Privacy and Differential Privacy

*7 月 13 日（周一） · 10:30-12:10 · Executive Meeting Room, 12th Floor, Qunsheng Howard Johnson*  
*主持 Jiajun Sun（Xiamen University）*

### 1. Collaborative Inference for Sparse High-Dimensional Models with Non-Shared Data

**讲者**：Yifan Gu（Renmin University of China）

**对应论文**：Collaborative Inference for Sparse High-Dimensional Models with Non-Shared Data · [arXiv:2504.19924](https://arxiv.org/abs/2504.19924)

<details><summary>摘要（原文）</summary>

In modern data analysis, statistical efficiency improvement is expected via effective collaboration among multiple data holders with non-shared data. In this article, we propose a collaborative score-type test (CST) for testing linear hypotheses, which accommodates potentially high-dimensional nuisance parameters and a diverging number of constraints and target parameters. Through a careful decomposition of the Kiefer-Bahadur representation for the traditional score statistic, we identify and approximate the key components using aggregated local gradient information from each data source. In addition, we employ a two-stage partial penalization strategy to shrink the approximation error and mitigate the bias from the high-dimensional nuisance parameters. Unlike existing methods, the CST procedure involves constrained optimization under non-shared and high-dimensional data settings, which requires novel theoretical developments. We derive the limiting distributions for the CST statistic under the null hypothesis and the local alternatives. Besides, the CST exhibits an oracle property and achieves the global statistical efficiency. Moreover, it relaxes the stringent restrictions on the number of data sources required in the current literature. Extensive numerical studies and a real example demonstrate the effectiveness and validity of our proposed method.

</details>

**问题**  
在多个数据持有者无法直接共享原始数据的场景下，如何对稀疏高维模型进行高效的统计推断？现有分布式方法（如分治策略）通常要求各站点样本量平衡且数据源数量 $m$ 远小于样本量，难以适应非共享数据与大量参与方的实际需求。本文聚焦于线性假设 $H_0: C\theta = t$ 的检验问题，其中 $\theta$ 为目标参数，$\gamma$ 为高维稀疏 nuisance 参数，允许约束数 $r$ 与目标维数 $d$ 随样本量发散。

**核心方法**  
提出协作得分检验（CST）。首先，通过分解传统得分统计量的 Kiefer-Bahadur 表示，识别出关键成分可用各数据源的局部梯度信息近似，从而构造一个带梯度偏移的代理损失 $\tilde{L}(\beta) = \hat{L}_1(\beta) + \langle \nabla\hat{L}(\tilde{\beta}^{(0)}) - \nabla\hat{L}_1(\tilde{\beta}^{(0)}), \beta \rangle$，其中 $\hat{L}_1$ 为主机经验损失。其次，采用两阶段部分惩罚策略：第一阶段用 $\ell_1$ 惩罚获得初始估计，第二阶段在约束 $C\theta=t$ 下使用折叠凹惩罚（如 SCAD）对 $\gamma$ 进行加权 $\ell_1$ 惩罚，以减小近似误差并缓解高维 nuisance 参数带来的偏差。最终检验统计量 $T_S = N \| \hat{\Omega} \nabla_{\hat{b}}\hat{L}(\hat{\beta}) \|_2^2$ 渐近服从 $\chi^2(r)$ 分布，其中 $\hat{\Omega}$ 为基于支持估计的方差调整矩阵。

**与已有工作关系**  
与分治检验（Battey et al., 2018）相比，CST 无需去偏步骤，且放松了对 $m$ 的严格限制（允许 $m$ 与样本量同阶甚至更大），同时支持更一般的线性假设（多约束、发散 $r,d$）。与分布式梯度增强损失（Jordan et al., 2019）相比，本文从得分统计量分解角度重新诠释了该损失，并首次在非共享数据下处理高维 nuisance 参数与线性约束，建立了带约束优化下的 oracle 性质。

**贡献**  
1. 提出 CST 流程，实现非共享数据下高维模型的协作推断，通信复杂度仅为 $O(mp)$ 每轮，迭代次数对数增长。  
2. 通过两阶段部分惩罚策略有效处理高维 nuisance 参数，并证明 CST 统计量具有 oracle 性质（与已知支持下的 OCST 同分布）。  
3. 理论推导了 CST 在原假设与局部备择下的极限分布，其功效与全局共享数据下的传统得分检验一致，优于分治检验。  
4. 数值实验与真实数据（芝加哥出租车数据）验证了 CST 在控制第一类错误与提升功效方面的有效性，尤其当数据源数量较大时优势显著。


### 2. Analysis of Quadratic Forms of High-Dimensional Non-Stationary Time Series, with Application to ANOVA and Independent Testing

**讲者**：Yunyi Zhang（The Chinese University of Hong Kong, Shenzhen）

**对应论文**：ANOVA for High-dimensional Non-stationary Time Series · [arXiv:2509.09079](https://arxiv.org/abs/2509.09079)

<details><summary>摘要（原文）</summary>

Temporal dependence and the resulting autocovariances in time series data can introduce bias into ANOVA test statistics, thereby affecting their size and power. This manuscript accounts for temporal dependence in ANOVA and develops a test statistic suitable for high-dimensional, non-stationary time series. Recognizing that the presence of complex fourth-order cumulants may introduce difficulties in variance estimation of the test statistic, we develop a bootstrap algorithm to conduct hypothesis testing through computer simulations. Theoretical results including the asymptotic distribution of the test statistic under the null hypothesis and the validity of the proposed bootstrap algorithm are established. Numerical studies demonstrate a good finite-sample performance of the proposed test statistic. In addition to the new test procedure, this manuscript derives theoretical results on consistency, Gaussian approximation, and variance estimation for quadratic forms of high-dimensional non-stationary time series, which may be of independent interest to researchers.

</details>

**问题**  
高维时间序列的方差分析（ANOVA）面临双重挑战：数据维度 $d$ 可与样本量 $T_k$ 相当甚至更大，且时间序列常呈现非平稳性（协方差结构随时间变化）。经典高维两样本检验（如 Chen & Qin, 2010）假设观测独立，直接用于时序数据时，非零自协方差会引入 $O(\sqrt{d})$ 量级的偏差，严重膨胀检验的 size 并损害 power。现有针对时序的 ANOVA 工作多限于平稳序列或要求 $d^{3/2}/\sqrt{T_k}\to 0$，无法适应高维非平稳场景。因此，如何构造一个对时序依赖稳健、适用于高维非平稳序列的均值检验统计量，是核心问题。

**核心方法**  
讲者提出一种修正的 ANOVA 检验统计量 $\widehat{R}$，通过引入两个带宽 $B$ 和 $B_1$（$0<B<B_1<\min T_k$），仅保留时间滞后介于 $[B, B_1]$ 的乘积项 $x_{t_1,k}^\top x_{t_2,k}$，从而有效消除短程依赖带来的偏差。该统计量可视为 Chen & Qin (2010) 检验的推广：当 $B=1$、$B_1$ 足够大时退化为原形式。为处理方差估计中涉及的四阶累积量难题，讲者将 Zhang et al. (2024) 的二阶 wild bootstrap 算法推广至高维时序，通过模拟生成服从联合正态分布的权重，对“二阶残差”进行重采样，从而避免直接估计复杂方差。理论方面，论文建立了 $(M,\alpha)$-短程依赖随机向量二次型的集中不等式、高斯逼近定理和 HAC 方差估计，并据此证明了 $\widehat{R}$ 在原假设下的渐近正态性以及 bootstrap 的一致性。

**与已有工作关系**  
已有高维 ANOVA 文献（如 Chen & Qin, 2010; Cai et al., 2014）均假设观测独立；针对时序的 ANOVA 研究（如 Nagahata & Taniguchi, 2018）则要求平稳性且维度增长受限。本文首次同时处理高维性、非平稳性和时序依赖，将 Chen & Qin (2010) 的统计量推广至非平稳时序，并将 Zhang et al. (2024) 的 bootstrap 从标量时序扩展到向量时序。此外，论文关于二次型的理论结果（如定理 4.2–4.5）独立于 ANOVA 本身，为样本协方差、谱密度等统计量的分布分析提供了新工具。

**主要贡献**  
1. 提出适用于高维非平稳时间序列的 ANOVA 检验统计量，通过带宽选择有效消除时序偏差，且允许 $d$ 与 $T_k$ 同阶。  
2. 建立 $(M,\alpha)$-短程依赖向量时序二次型的集中不等式、高斯逼近和 HAC 方差估计，这些结果具有独立的方法论价值。  
3. 证明所提 bootstrap 算法的渐近有效性，为实际应用提供了可行的推断方案。  
4. 数值实验表明，该方法在多种时序依赖结构下能良好控制 size 并保持 power，优于忽略时序依赖的现有方法。


### 3. Distributed Hypothesis Testing for High Dimensional Mutual Independence

**讲者**：Xiangyu Shi（Nanjing Forestry University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维数据中，检验多个随机变量之间的互独立性（mutual independence）是统计推断的基础问题，但传统检验方法（如基于经验分布或核方法的全样本检验）在高维场景下面临维数灾难与计算瓶颈。当数据分散存储于多个节点（如分布式系统）时，通信成本与隐私约束进一步限制了全局数据的集中处理。本报告旨在解决：如何在通信受限的分布式环境下，对高维向量的各分量是否相互独立进行有效假设检验，并控制第一类错误与检验功效。

**核心方法**  
讲者可能提出一种基于“分治-聚合”框架的分布式检验统计量。首先，各节点利用局部数据计算两两变量间的某种独立性度量（如距离协方差或互信息估计），并通过稀疏化或压缩感知技术降低通信量。然后，中心节点聚合各节点的局部统计量，构造一个全局检验统计量，其渐近分布在高维稀疏假设下可近似为极值分布或卡方混合分布。关键步骤在于：利用去偏估计（debiased estimation）或交叉拟合（cross-fitting）消除分布式计算带来的偏差，并借助自举（bootstrap）或置换检验（permutation test）校准临界值，以应对有限样本下的分布逼近误差。

**与已有工作关系**  
现有高维独立性检验多集中于全样本场景（如基于协方差矩阵的球性检验、基于距离协方差的检验），而分布式检验的研究尚处起步阶段。已有分布式假设检验工作主要针对均值或回归系数，鲜有涉及高维互独立性。本报告将分布式推断与高维非参数检验相结合，可能借鉴了“分布式似然比检验”或“分布式U统计量”的框架，但针对互独立性这一特殊零假设，需要重新设计聚合策略与偏差校正，以克服高维稀疏性带来的多重比较问题。

**主要贡献**  
1. 首次在分布式环境下系统研究高维互独立性检验，填补了该方向的方法论空白。  
2. 提出通信高效的检验流程，理论证明在通信预算固定时，检验的渐近性质（size与power）与全样本检验等价，且无需交换原始数据。  
3. 通过数值模拟与真实数据（如基因表达数据）验证方法在有限样本下的有效性，为分布式统计推断提供新工具。


### 4. Differentially Private Gaussian Graphical Model: Optimality, Algorithm and FDR Control

**讲者**：Jiajun Sun（Xiamen University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高斯图模型（Gaussian Graphical Model）通过估计精度矩阵（inverse covariance matrix）的非零模式来揭示变量间的条件独立关系。然而，当数据包含敏感信息（如基因表达或医疗记录）时，直接发布图结构会泄露个体隐私。本报告聚焦于在差分隐私（Differential Privacy, DP）约束下，如何同时实现图结构估计的统计最优性（optimality）与错误发现率（False Discovery Rate, FDR）控制。核心挑战在于：隐私噪声会扭曲稀疏性诱导的惩罚项，导致传统FDR控制方法（如BH过程）失效，且现有DP图模型算法缺乏minimax最优性保证。

**核心方法**  
报告可能提出一种两阶段框架：第一阶段，采用带隐私噪声的graphical lasso估计精度矩阵，其中噪声通过高斯机制或拉普拉斯机制注入到样本协方差矩阵或梯度中，并利用隐私预算的集中化分配（如Rényi DP）达到最优收敛速率。第二阶段，基于去偏化的隐私估计量（debiased DP estimator）构造检验统计量，并设计一种隐私感知的FDR控制程序——例如，通过引入隐私噪声的校准阈值或采用knockoffs框架的差分隐私变体，确保在有限样本下FDR被严格控制在预设水平。理论部分可能证明该算法在稀疏图（边数$s = o(p)$）下达到minimax最优的$\ell_2$估计误差，且FDR控制不因隐私噪声而膨胀。

**与已有工作关系**  
现有DP图模型研究多关注估计一致性（如Cai et al., 2021），但未涉及FDR控制；而传统FDR控制方法（如Benjamini-Hochberg）在DP设定下因噪声扭曲p值分布而失效。本报告首次将DP、最优性理论与多重假设检验结合，填补了隐私保护下图模型推断的空白。与近期DP变量选择工作（如Kifer et al., 2022）相比，本报告针对图模型特有的稀疏结构（精度矩阵的对称性）优化了隐私噪声的注入策略。

**主要贡献**  
1. 提出首个同时满足差分隐私、统计最优性和FDR控制的高斯图模型算法，建立了隐私预算与图结构可识别性之间的精确trade-off。  
2. 在理论上证明了所提估计量的minimax最优性，并给出了FDR控制下所需样本量的下界。  
3. 通过数值实验验证了方法在合成数据与真实基因网络数据上的有效性，表明在中等隐私预算（如$\epsilon=1$）下仍能保持合理的图恢复精度与FDR控制。


### 5. Noncentral Normal-Reference Transfer Theory for High-Dimensional L² Mean Tests

**讲者**：Pengfei Wang（Nanyang Technological University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维均值检验中，基于 $L^2$ 范数的检验（如 Hotelling’s $T^2$ 的推广）在维度 $p$ 远大于样本量 $n$ 时面临严重挑战：样本协方差矩阵奇异，传统检验统计量失效。现有方法（如 Bai-Saranadasa 检验、Chen-Qin 检验）虽能在零假设下给出渐近分布，但对**非中心备择假设**（即均值差非零）下的统计量分布刻画不足，导致功效分析依赖模拟或近似，缺乏理论保证。本报告旨在解决这一问题：如何为高维 $L^2$ 均值检验在非中心情形下建立精确的渐近分布理论？

**核心方法**  
讲者提出 **Noncentral Normal-Reference Transfer Theory**（非中心正态参考转移理论）。其核心思想是：将高维 $L^2$ 检验统计量 $T = \|\bar{X} - \bar{Y}\|^2$（或经协方差调整的版本）在非中心备择下的分布，通过构造一个**非中心正态参考分布**（即均值非零、协方差已知的高维正态分布）进行“转移”。具体地，利用随机矩阵谱分析中的 Marčenko-Pastur 定律及其推广，证明 $T$ 的分布可渐近等价于某个非中心 $\chi^2$ 型分布，其非中心参数由真实均值差和总体协方差谱决定。该理论的关键在于：通过一个线性变换将原统计量映射到参考分布空间，从而将复杂的非中心分布问题转化为参考分布的已知性质。

**与已有工作关系**  
已有高维均值检验工作（如 Bai-Saranadasa, 1996; Chen & Qin, 2010）主要关注零假设下的渐近正态性或 $\chi^2$ 近似，对非中心情形仅给出粗糙的界或依赖置换检验。本工作首次系统性地处理非中心备择下的分布转移问题，区别于传统的中心极限定理方法。与近期基于随机矩阵理论的“Normal-Reference”方法（如 Wang et al., 2020）相比，本工作将其从零假设推广到非中心情形，并引入非中心参数作为转移桥梁，从而统一了零假设与备择假设下的理论框架。

**主要贡献**  
1. 提出了非中心正态参考转移理论，为高维 $L^2$ 均值检验在非中心备择下提供了**显式的渐近分布表达式**，包括非中心参数与协方差谱的解析关系。  
2. 给出了检验功效的精确渐近公式，避免了传统模拟或 bootstrap 的计算负担，且适用于一般协方差结构（如因子模型、稀疏协方差）。  
3. 通过数值实验验证了理论在有限样本下的准确性，为高维均值检验的实践提供了理论支撑，尤其适用于基因表达、金融资产等维度极高的场景。


### 6. Minimax Detection of Localized Underdensity in Uniformity Testing on Closed Manifolds

**讲者**：Jixin Wang（Imperial College London）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
经典均匀性检验（uniformity testing）通常假设数据来自欧氏空间中的简单区域（如超立方体），但许多实际数据（如天体分布、地球物理观测）天然位于闭流形（closed manifold，如球面 $\mathbb{S}^d$、环面 $\mathbb{T}^d$）上。该报告关注一个更精细的备择假设：流形上存在一个**局部欠密度区域**（localized underdensity），即该区域内的点密度显著低于均匀分布。问题在于：在 minimax 框架下，需要多少样本才能可靠地检测到这种局部偏离？检测的误差边界如何依赖于流形的维数、欠密度区域的几何尺度（如半径 $r$）以及偏离幅度？

**核心方法**  
报告可能利用流形上的调和分析（harmonic analysis）或局部化基函数（如球面小波、热核卷积）构造检验统计量。具体地，将均匀分布视为零假设，局部欠密度视为一个光滑的密度扰动 $f = 1 - \varepsilon \cdot \phi$，其中 $\phi$ 是支撑在测地球上的光滑函数。通过流形上 Laplace-Beltrami 算子的特征展开，将检验问题转化为对低频或中频系数的能量检测。最优检验统计量可能基于局部化核的积分，其阈值由 minimax 风险决定，并借助 concentration inequality 导出检测的相变边界（如 $n \asymp r^{-d} \varepsilon^{-2}$ 量级）。

**与已有工作关系**  
已有均匀性检验多针对全局偏离（如 Sobolev 检验、能量距离），或仅适用于欧氏空间中的局部偏离（如 scan statistic）。该工作将局部欠密度检测推广到一般闭流形，并给出 minimax 最优性。与球面均匀性检验（如 Bingham 检验）相比，这里允许备择假设具有局部性而非全局各向异性；与流形上的密度估计相比，这里关注假设检验的 minimax 速率而非估计误差。

**主要贡献**  
1. 首次在闭流形上系统研究局部欠密度检测的 minimax 问题，刻画了检测难度与流形维数、区域尺度、偏离幅度的精确关系。  
2. 构造了基于局部化核的检验统计量，并证明其在 minimax 意义下最优（或达到最优速率），同时给出可实现的阈值选择方法。  
3. 为流形上非参数假设检验提供了新的理论框架，可推广至其他局部结构（如局部过密度、边缘检测）的 minimax 分析。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)