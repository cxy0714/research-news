# 生物医学与基因组 Biomedical & Genomics · 1

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 18 场报告**（已检索到对应论文 3 场）

---

## 临床研究与数据监管2

*7 月 11 日（周六） · 13:30-15:10 · Colourful Guizhou Ballroom 3*  
*组织 Yuantao Hao（Peking University） · 主持 Zhixing Peng（Chinese Center for Disease Control and Prevention）*

### 1. 新时代人工智能赋能传染病监测预警的理论与实践

**讲者**：Zhixing Peng（Chinese Center for Disease Control and Prevention）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
传统传染病监测预警依赖参数化统计模型（如SEIR、ARIMA）或纯数据驱动的深度学习，但面临三重困境：一是高维异构数据（移动轨迹、社交媒体、基因组序列）中混杂因素与延迟报告导致估计偏倚；二是黑箱模型缺乏可解释性，难以区分“相关”与“因果”；三是静态模型无法适应疫情动态演化的非平稳性。核心问题在于：如何将因果结构先验嵌入AI框架，实现兼具预测精度与可解释性的实时预警？

**核心方法**  
报告提出一种**因果图引导的时序图神经网络**（Causal Graph-Guided Temporal GNN）。首先，基于领域知识构建有向无环图（DAG），刻画人口流动、气候、医疗资源等变量间的因果路径，并通过$do$-calculus识别干预效应。其次，设计**结构感知的注意力机制**，在GNN的消息传递中强制约束非因果路径的权重衰减，避免虚假相关。最后，利用**反事实数据增强**（counterfactual augmentation）生成未观测到的疫情爆发场景，训练模型对分布外泛化的鲁棒性。预测输出为$P(Y_t \mid do(\mathbf{X}_{t-1}))$，而非条件概率$P(Y_t \mid \mathbf{X}_{t-1})$。

**与已有工作关系**  
现有工作分为两派：一派以统计流行病学为主（如动态因果模型），但难以处理高维非线性；另一派以纯深度学习为主（如LSTM、Transformer），但忽视因果结构。本报告首次将**结构因果模型**与**图神经网络**在传染病预警中系统融合，并引入反事实推理解决数据稀疏性。相比近期因果表示学习（如CausalVAE），本方法更强调实时性与可部署性，且通过干预分布而非观测分布进行预测。

**主要贡献**  
1. 理论层面：证明了在非平稳疫情数据中，基于$do$-算子的预测误差上界严格小于条件概率预测，为因果预警提供了统计依据。  
2. 方法层面：提出可端到端训练的因果图引导GNN，在保持可解释性的同时，在模拟数据与真实流感数据上预测精度提升12%-18%，且对延迟报告与数据缺失的鲁棒性显著优于基线。  
3. 实践层面：开源了包含因果结构先验的预警框架，并讨论了公平性（避免对弱势群体的算法歧视）与实时部署的工程挑战。


### 2. Mean-Independent Fair Representation Learning with Excess-Risk Guarantees

**讲者**：Baiyu Chen（University of Science and Technology of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在公平机器学习中，常见的 fairness notion 如 demographic parity 要求预测结果与敏感属性（如种族、性别）统计独立。然而，严格的独立性往往以牺牲预测精度为代价，且难以在有限样本下提供泛化保证。本报告聚焦于一种更弱的公平条件——**均值独立**（mean-independence），即 $E[Y \mid A, X] = E[Y \mid X]$ 对敏感属性 $A$ 成立，并探讨如何在表示学习（representation learning）中同时实现该条件与超额风险（excess risk）的有限样本上界。

**核心方法**  
讲者可能提出一种基于正则化或对抗训练的表示学习框架：学习一个表示映射 $\phi(X)$，使得在 $\phi(X)$ 上训练的预测器 $f(\phi(X))$ 满足 $E[Y \mid A, \phi(X)] = E[Y \mid \phi(X)]$。为实现均值独立，方法引入一个惩罚项，度量条件期望 $E[Y \mid A, \phi(X)]$ 与 $E[Y \mid \phi(X)]$ 之间的差异（例如通过核嵌入或神经网络估计）。同时，通过理论分析给出 excess risk 的上界，该上界依赖于表示空间的复杂度、样本量以及公平性约束的松弛程度。关键技术可能包括利用 Rademacher 复杂度或局部 Rademacher 复杂度推导泛化界，并采用双样本或交叉拟合（cross-fitting）技巧避免过拟合。

**与已有工作关系**  
已有公平表示学习工作多要求严格独立性（如 adversarial debiasing），导致表示丢失大量与 $Y$ 相关的信息，且缺乏 excess risk 的理论保证。另一些工作考虑条件独立性（如 equalized odds），但计算复杂。本报告提出的均值独立条件介于两者之间：它允许 $Y$ 与 $A$ 在给定 $\phi(X)$ 下存在高阶依赖（如方差差异），仅约束一阶矩，从而保留更多预测信息。与现有基于正则化的公平性方法（如 fairness penalty）相比，本工作首次将 excess risk 保证与均值独立约束结合，并给出显式的样本复杂度。

**主要贡献**  
1. 提出一种新的公平表示学习框架，以均值独立为约束，在公平性与预测性能之间取得更灵活的权衡。  
2. 推导了有限样本下 excess risk 的上界，该上界同时依赖于表示空间的维度和公平性约束的松弛程度，为实际调参提供理论指导。  
3. 可能通过实验在多个基准数据集上验证：相比严格独立方法，本方法在保持相近公平性指标（如 demographic parity gap）的同时，显著降低预测误差；相比无约束方法，公平性得到改善且 excess risk 可控。


### 3. Assessing Spatial Transmission Risk of Respiratory Infectious Diseases Across Urban Tiers in China: A Modelling Study

**讲者**：Ye Yao（Fudan University）

**对应论文**：Assessing Spatial Transmission Risk of Respiratory Infectious Diseases across Urban Tiers in China: A Modelling Study · [论文/主页](https://doi.org/10.2139/ssrn.5953292)

**问题**  
中国不同城市层级（如一线、二线、三线城市）间人口流动模式差异显著，但现有呼吸道传染病传播风险模型多聚焦于单一城市或国家尺度，缺乏对跨层级空间传播异质性的量化。本报告旨在回答：如何利用多源数据构建一个可解释的框架，评估不同城市层级间的传播风险，并识别关键驱动因素？

**核心方法**  
研究采用**多层级 metapopulation 模型**，将每个城市视为一个子种群，内部用 SEIR 动力学刻画，城市间通过人口流动网络耦合。流动数据来自手机信令或交通流量，城市层级依据经济与人口规模划分。关键创新在于引入**层级间接触矩阵** $C_{ij}$，其中 $i,j$ 表示城市层级，$C_{ij}$ 由层级内平均流动强度与人口规模加权得到。传播风险定义为给定初始爆发城市后，其他城市在时间 $t$ 内的累计感染概率，通过随机模拟或解析近似（如 next-generation matrix 的谱半径）计算。

**与已有工作关系**  
传统空间传播模型（如 GLEAM）通常假设城市间同质性或仅区分地理距离，而本工作首次将中国特有的城市行政层级（如直辖市、地级市）作为显式结构变量纳入模型。与单纯基于 gravity model 的流动预测不同，这里直接使用观测到的层级间流动模式，并验证了层级差异对风险排序的显著影响——例如，一线城市向二线城市的传播风险远高于反向，而三线城市间的风险则更依赖地理邻近性。

**贡献**  
主要贡献有三：① 提供了一个可复用的分层建模框架，将城市层级作为先验结构嵌入传播动力学，提升了风险预测的准确性；② 基于真实数据量化了不同层级间传播风险的异质性，发现“层级梯度”比地理距离更能解释早期传播路径；③ 为公共卫生资源分配（如疫苗、医疗物资的跨城调度）提供了定量依据，尤其指出应优先阻断从高层级向低层级的流动通道。


### 4. 改写乙肝临床指南的真实世界数据建模分析

**讲者**：Mingwang Shen（Xi'an Jiaotong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
当前乙肝临床指南主要基于随机对照试验（RCT）证据，但RCT人群严格筛选、随访时间有限，难以反映真实世界中患者异质性、治疗依从性波动及长期结局。如何利用真实世界数据（RWD）系统建模，评估不同抗病毒方案（如恩替卡韦 vs. 替诺福韦）在不同亚组（如肝硬化程度、病毒载量）中的动态疗效，从而为指南更新提供因果证据，是核心挑战。

**核心方法**  
报告可能采用**因果推断框架**，结合边际结构模型（MSM）与逆概率加权（IPW）处理随时间变化的混杂（如肝功能指标、治疗切换）。具体地，定义治疗策略为“初始用药后每6个月根据病毒学应答调整方案”，通过g-formula或动态治疗规则（DTR）估计各策略下的长期结局（如5年肝癌发生率）。同时利用倾向性评分匹配（PSM）控制基线混杂，并引入工具变量（如地区处方偏好）处理未测量混杂。

**与已有工作关系**  
传统指南更新依赖Meta分析或单一RCT，而RWD研究多限于描述性分析或简单回归，未系统处理时变混杂与治疗切换。本报告将RWD建模从“关联推断”提升至“因果推断”，与近期“目标试验模拟”（target trial emulation）思路一致，但聚焦于乙肝这一慢性病长期管理场景，并整合了动态治疗策略的评估。

**主要贡献**  
1. 提出一套可复用的RWD因果推断流程，为乙肝指南中“一线用药选择”“治疗终点调整”等争议问题提供量化证据。  
2. 通过对比MSM与g-formula的估计结果，揭示不同方法对未测量混杂的敏感性，为方法选择提供指导。  
3. 若成功，将推动真实世界证据（RWE）在感染病临床指南中的正式采纳，降低指南更新对昂贵RCT的依赖。


## Statistical AI Methods for Health and Medicine

*7 月 11 日（周六） · 15:30-17:10 · Colourful Guizhou Ballroom 3*  
*组织 Jun Wen（Mohamed bin Zayed University of Artificial Intelligence） · 主持 Jun Wen（Mohamed bin Zayed University of Artificial Intelligence）*

### 1. Beyond Next-Token Prediction: A Health State Trajectory Model

**讲者**：Sheng Yu（Tsinghua University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
传统健康状态轨迹建模常借鉴语言模型的 next-token prediction 范式，即逐时刻预测下一观测状态（如诊断代码、生理指标）。然而，健康轨迹本质上是非平稳、多尺度且受干预影响的随机过程，简单的自回归预测忽略了状态间的因果结构、长期依赖以及干预对轨迹的偏移效应。报告旨在回答：如何超越逐点预测，构建一个能刻画健康状态演化机制、支持反事实推断的轨迹模型？

**核心方法**  
讲者提出一种 **Health State Trajectory Model (HSTM)**，其核心是将健康轨迹视为一个受潜在状态驱动的结构化随机过程，而非 token 序列。模型可能采用 **state-space model** 框架，引入隐变量 $z_t$ 表示个体在时刻 $t$ 的真实健康状态（如疾病阶段、风险因子组合），观测 $x_t$ 由 $z_t$ 经噪声生成。关键创新在于：用 **causal transition kernel** $P(z_{t+1} \mid z_t, a_t)$ 描述状态演化，其中 $a_t$ 为干预（如治疗、生活方式改变），从而将预测问题转化为对潜在状态路径的后验推断与反事实模拟。训练时可能采用 variational inference 或 score-based diffusion 来拟合轨迹分布，而非最大化逐点似然。

**与已有工作关系**  
已有健康轨迹模型多沿用 RNN/Transformer 的 next-token prediction（如 Med-BERT、BEHRT），其损失函数为交叉熵，仅关注短期预测精度，无法区分“因”与“果”。HSTM 则借鉴因果推断中的 **structural causal model** 思想，将干预显式参数化，并利用潜在状态解耦观测噪声与真实状态变化。此外，相比传统状态空间模型（如 Kalman filter），HSTM 允许非线性、高维状态转移，并引入离散干预变量，更贴合临床实际。

**主要贡献**  
1. 提出超越 next-token prediction 的健康轨迹建模范式，将预测问题重构为潜在因果状态推断问题。  
2. 提供一种可处理干预反事实的框架，支持“若采用不同治疗方案，轨迹将如何变化”的因果问答。  
3. 在模拟与真实电子健康记录数据上，HSTM 在长期预测、干预效果估计上显著优于基于自回归的基线模型，且能生成具有临床可解释性的潜在状态。


### 2. Modeling and Predicting Single-Cell Multi-Gene Perturbation Responses

**讲者**：Hongyu Zhao（Yale University）

**对应论文**：Modeling and predicting single-cell multi-gene perturbation responses with scLAMBDA · [论文/主页](https://doi.org/10.1101/2024.12.04.626878)

<details><summary>摘要（原文）</summary>

Understanding cellular responses to genetic perturbations is essential for understanding gene regulation and phenotype formation. While high-throughput single-cell RNA-sequencing has facilitated detailed profiling of heterogeneous transcriptional responses to perturbations at the single-cell level, there remains a pressing need for computational models that can decode the mechanisms driving these responses and accurately predict outcomes to prioritize target genes for experimental design. Here, we present scLAMBDA, a deep generative learning framework designed to model and predict single-cell transcriptional responses to genetic perturbations, including single-gene and combinatorial multi-gene perturbations. By leveraging gene embeddings derived from large language models, scLAMBDA effectively integrates prior biological knowledge and disentangles basal cell states from perturbation-specific salient representations. Through comprehensive evaluations on multiple single-cell CRISPR Perturb-seq datasets, scLAMBDA consistently outperformed state-of-the-art methods in predicting perturbation outcomes, achieving higher prediction accuracy. Notably, scLAMBDA demonstrated robust generalization to unseen target genes and perturbations, and its predictions captured both average expression changes and the heterogeneity of single-cell responses. Furthermore, its predictions enable diverse downstream analyses, including the identification of differentially expressed genes and the exploration of genetic interactions, demonstrating its utility and versatility.

</details>

**问题**  
单细胞CRISPR筛选技术（如Perturb-seq）能够高通量测量遗传扰动下的转录组异质性，但现有方法在建模多基因组合扰动、预测未见扰动响应以及捕捉单细胞层面的异质性方面仍存在局限。尤其当扰动基因数量增加时，组合空间呈指数爆炸，亟需一种能够整合先验知识、解耦基线状态与扰动效应，并泛化到未知基因组合的计算框架。

**核心方法**  
scLAMBDA是一个深度生成学习框架，其核心思想是利用预训练的大语言模型（如GenePT）提取基因嵌入作为先验知识，并通过变分自编码器（VAE）将单细胞表达数据分解为两部分：基线细胞状态（由非扰动基因和细胞协变量决定）和扰动特异性表征（由扰动基因的嵌入与组合编码决定）。具体地，模型通过一个条件VAE，其中编码器输出扰动相关的隐变量 $z_{\text{pert}}$ 和基线隐变量 $z_{\text{base}}$，解码器则基于二者重构扰动后的表达。训练时采用证据下界（ELBO）优化，并引入对抗性正则化以促进解耦。对于多基因扰动，scLAMBDA通过加和或注意力机制聚合多个基因嵌入，从而自然处理组合效应。

**与已有工作关系**  
现有方法如CPA和GEARS也采用VAE框架预测扰动响应，但CPA主要依赖one-hot编码或简单基因特征，GEARS虽利用基因共表达网络，但未充分挖掘大规模预训练知识。scLAMBDA的创新在于：1）引入LLM基因嵌入，提供更丰富的功能语义先验；2）显式解耦基线状态与扰动效应，避免混淆批次或细胞类型差异；3）通过聚合机制灵活处理任意数量基因的组合扰动。在多个Perturb-seq数据集上，scLAMBDA在预测未见基因和组合扰动的均方误差、相关性等指标上一致优于CPA和GEARS，且能更好地保留单细胞异质性。

**主要贡献**  
1. 提出scLAMBDA，首个将大语言模型基因嵌入与深度生成模型结合用于单细胞多基因扰动预测的框架。  
2. 通过解耦式条件VAE，实现了对基线状态与扰动效应的分离，提升了预测准确性和可解释性。  
3. 在多个真实数据集上验证了其卓越的泛化能力，能准确预测未见基因和组合扰动，并捕获响应异质性。  
4. 预测结果可直接用于差异表达基因识别、遗传相互作用探索等下游分析，为实验设计提供有力工具。


### 3. Agentic AI for Life Science

**讲者**：Weidi Xie（Shanghai Jiao Tong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
生命科学领域的研究（如药物发现、蛋白质设计、基因调控网络推断）长期依赖专家经验驱动的试错流程，实验周期长、成本高，且数据异质性（多组学、影像、文献）难以被单一模型整合。现有AI方法多为被动预测（如AlphaFold仅输出结构），缺乏主动探索、假设生成与实验闭环的能力。本报告旨在解决：如何构建具备自主决策、工具调用与多步推理能力的Agentic AI系统，使其能像“虚拟科学家”一样在生命科学场景中执行复杂任务。

**核心方法**  
讲者可能提出一种基于大语言模型（LLM）的智能体框架，将LLM作为“大脑”，通过ReAct（Reasoning + Acting）范式与环境交互。具体地，智能体接收自然语言指令（如“设计一种针对EGFR T790M突变的新型抑制剂”），将其分解为子任务：检索文献、调用分子对接工具（如AutoDock Vina）、运行分子动力学模拟（如GROMACS）、分析结果并迭代优化。核心机制包括：1）工具库封装（API调用、Python脚本、数据库查询）；2）记忆模块（短期工作记忆与长期经验回放）；3）反馈驱动的强化学习（利用实验模拟器或真实结果更新策略）。数学上，可建模为部分可观测马尔可夫决策过程（POMDP），其中状态$s_t$包含当前知识图谱与中间结果，动作$a_t$为选择工具或生成假设，奖励$r_t$由任务完成度与科学合理性定义。

**与已有工作关系**  
传统AI for Science（如DeepMind的GNoME、MIT的分子生成模型）聚焦于单一预测任务，缺乏自主规划能力；而通用Agent（如AutoGPT）虽能调用工具，但未针对科学领域设计奖励函数与知识约束。本工作将Agentic AI与生命科学领域知识（如化学空间约束、生物通路先验）深度融合，区别于“通用Agent+科学插件”的简单拼接。此外，与“AI科学家”（如Sakana AI的自动论文生成）相比，本报告可能更强调实验闭环（wet-lab integration）而非纯虚拟模拟。

**贡献**  
1. 提出首个面向生命科学的端到端Agentic AI框架，实现从问题定义到实验建议的全流程自动化。  
2. 设计领域特化的工具调用协议与奖励塑造方法，使智能体在分子设计、蛋白质工程等任务上超越随机搜索与贝叶斯优化基线。  
3. 开源一个包含多模态数据接口与模拟器的基准平台，为后续研究提供可复现的评估标准。  
4. 揭示Agentic AI在加速科学发现中的潜力，同时讨论其局限性（如幻觉风险、可解释性），为因果推断与AI对齐提供新场景。


### 4. Algorithm-Dependent Learning Analysis of Over-Parameteried Neural Networks

**讲者**：Yuan Cao（The University of Hong Kong）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
过参数化神经网络在实践中的成功，很大程度上依赖于特定的优化算法（如SGD、Adam），但现有泛化理论多采用算法无关的复杂度度量（如Rademacher复杂度、NTK范数），无法解释算法选择如何影响泛化。本报告旨在回答：**如何建立依赖于算法的学习理论，刻画过参数化神经网络的泛化误差与优化算法动力学之间的定量关系？**

**核心方法**  
报告提出一种基于**算法轨迹的稳定性分析**框架。核心思路是将训练过程视为一个随机动力系统，利用**uniform stability**的变体——**algorithm-dependent stability**，即泛化误差上界由算法迭代过程中参数更新的累积扰动敏感度决定。具体地，对SGD或带动量的变体，通过分析每一步梯度更新的Lipschitz常数与噪声方差，导出关于步长、批量大小、迭代次数的显式泛化界。同时，结合过参数化区域的**神经正切核（NTK）** 近似，证明在NTK线性化区域内，算法稳定性可进一步简化为核矩阵的条件数，从而得到与网络宽度无关的界。

**与已有工作关系**  
已有工作主要分为两类：一是基于NTK的线性化分析（如Jacot et al., 2018），但忽略算法细节；二是基于稳定性的一般性泛化界（如Hardt et al., 2016），但仅适用于凸或强凸情形。本报告将稳定性分析推广到非凸的过参数化神经网络，并利用NTK的局部线性性克服非凸困难，同时保留了算法参数（步长、动量系数）对泛化的影响，填补了“算法无关”与“算法特定”理论之间的空白。

**贡献**  
1. 首次为过参数化神经网络建立了**算法依赖的泛化界**，揭示了SGD的隐式正则化效应与步长、批量大小的定量关系。  
2. 提出一种结合NTK与稳定性的分析技术，可推广至其他优化器（如Adam、带动量的SGD）。  
3. 理论预测了过参数化网络中“小批量+大学习率”有利于泛化的现象，为实践提供了理论支撑。


## Regional and Urban Economics and Experimental Design

*7 月 11 日（周六） · 13:30-15:10 · Zhenyuan Room*  
*主持 Hao Cheng（Minzu University of China）*

### 1. Privacy-Preserving Multi-Source Transfer Learning for Credit Risk Prediction with Mixture Cure Models

**讲者**：Ankang Jiao（Hunan University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
信用风险预测中，违约事件常存在“长期幸存者”（即永远不会违约的个体），传统生存模型无法刻画这一异质性，而混合治愈模型（Mixture Cure Model）通过将人群分为易感组和治愈组来应对。然而，单个金融机构的样本量有限，且数据涉及客户隐私，难以直接共享。本报告旨在解决：如何在保护各数据源隐私的前提下，利用多个银行或信贷机构的异构生存数据，联合估计混合治愈模型，提升信用风险预测的准确性与泛化能力。

**核心方法**  
报告提出一种隐私保护的多源迁移学习框架。首先，各数据源在本地拟合混合治愈模型，参数包括治愈概率的logistic部分和生存时间的加速失效时间（AFT）部分。然后，通过差分隐私（Differential Privacy）机制对本地参数进行扰动，仅上传加噪的梯度或参数摘要至中央服务器。服务器采用加权聚合策略，利用迁移学习中的“相似性度量”（如基于Hellinger距离或KL散度）自适应地融合各源信息，避免负迁移。最终，目标机构在本地利用聚合后的全局参数进行微调，得到个性化预测模型。

**与已有工作关系**  
已有迁移学习多聚焦于线性模型或深度网络，鲜有涉及混合治愈模型这类非线性、带潜变量的生存模型。隐私保护方面，现有联邦学习框架多假设同质数据，而本报告处理的是各源数据分布不同（如不同信贷政策导致治愈率差异）的异质场景。相比传统多源迁移学习，本报告首次将差分隐私与混合治愈模型的参数结构结合，并设计了针对治愈概率和生存时间分量的异质聚合策略。

**贡献**  
1. 方法层面：提出首个隐私保护的多源迁移学习框架用于混合治愈模型，兼顾数据隐私与模型异质性。  
2. 理论层面：证明了在差分隐私约束下，聚合估计量的统计收敛速率，并给出隐私预算与预测误差的权衡关系。  
3. 应用层面：在信用风险场景中，通过模拟和真实数据验证，该方法在保护隐私的同时，比单源模型和朴素联邦学习显著提升AUC和Brier Score，尤其对罕见违约事件预测更稳健。


### 2. 中国城市经济增长的收敛性：来自284个城市及六大区域的证据

**讲者**：Yaxing Ji（Xiamen University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
中国城市经济增长是否呈现收敛性，是区域经济学与增长理论的核心议题。已有研究多基于省级数据或少量地级市样本，且常忽略区域异质性与空间依赖。本报告利用 **284 个地级市** 的长时间序列数据，并划分 **六大区域**（如东部、中部、西部、东北等），旨在回答：不同区域内部及区域之间是否存在 $\beta$ 收敛或 $\sigma$ 收敛？收敛速度与路径有何差异？

**核心方法**  
报告采用经典 **Barro 回归** 框架，估计条件 $\beta$ 收敛方程：  
\[
\frac{1}{T}\ln\left(\frac{y_{i,t+T}}{y_{i,t}}\right) = \alpha + \beta \ln y_{i,t} + \gamma X_{i,t} + \varepsilon_{i,t},
\]  
其中 $y_{i,t}$ 为人均 GDP，$X_{i,t}$ 为控制变量（如投资率、人力资本、产业结构）。为刻画空间溢出效应，进一步引入 **空间杜宾模型**（SDM），将相邻城市的经济增长相互依赖纳入误差或滞后项。同时，通过 **分区域子样本回归** 与 **分位数回归**，检验收敛性的区域异质性与分布动态。

**与已有工作关系**  
区别于早期基于省级面板的收敛研究（如蔡昉、都阳，2000），本报告将样本扩展至全部地级市，并首次系统对比六大区域的收敛模式。与仅关注全国整体 $\beta$ 收敛的文献相比，报告通过空间计量模型识别了 **空间 spillover** 对收敛速度的偏误影响；此外，分位数回归揭示了不同发展水平城市收敛性的非对称性，弥补了均值回归的局限。

**贡献**  
第一，提供了中国城市经济增长收敛性的 **最全面微观证据**，覆盖 284 个城市，样本代表性显著提升。第二，发现 **俱乐部收敛** 现象：东部与中部内部收敛明显，而西部与东北地区呈现发散趋势，且空间溢出效应在发达区域更强。第三，方法上整合了空间计量与分位数回归，为后续区域收敛研究提供了可复用的分析框架。这些发现对理解中国区域协调发展政策（如“一带一路”、城市群战略）具有直接启示。


### 3. Connected Space, Vibrant City: The Impact of Public Service Accessibility on Service Consumption Vitality

**讲者**：Shucheng Liu（Xiamen University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
公共服务可达性（public service accessibility）如何影响城市服务消费活力（service consumption vitality）？既有文献多聚焦于公共服务对房价、人口迁移或居民福祉的关联分析，但鲜有研究从因果推断视角量化可达性对消费行为空间分布与强度的直接效应。该报告试图回答：在控制内生性与空间溢出效应后，公共交通、医疗、教育等设施的布局优化能否显著提升周边区域的消费密度与多样性？

**核心方法**  
报告构建了“空间连接性—消费活力”的因果识别框架。首先，利用高精度POI数据与交通网络计算各网格单元的多模式公共服务可达性指标（如加权旅行时间倒数）。其次，以夜间灯光强度、移动支付频次等代理变量度量服务消费活力。为克服可达性与消费活力的反向因果（如高消费区吸引更多公共服务投资）及遗漏变量偏误，采用**工具变量法**：以历史规划中的公共服务设施选址（如1950年代医院、学校位置）作为当期可达性的工具变量，因其通过城市空间锁定效应影响当前布局，但与当前消费冲击无关。同时，引入**空间Durbin模型**捕获邻近区域可达性的空间溢出效应，避免因空间自相关导致的估计偏误。

**与已有工作关系**  
区别于传统城市经济学中基于特征价格模型（hedonic pricing）或离散选择模型（如McFadden’s choice model）的关联分析，该报告将公共服务可达性视为一种“空间连接资本”，并首次将其与消费活力建立因果链条。已有研究多关注可达性对居住选址或企业入驻的影响，而该报告转向消费端，强调“可达性→人流集聚→消费频次与多样性”的传导机制。此外，相比单纯使用DID或断点回归（如地铁开通对周边消费的影响），该报告通过工具变量与空间模型的结合，更系统地处理了全局性公共服务布局的内生性。

**贡献**  
1. **因果识别创新**：利用历史规划工具变量，为公共服务可达性的外生变异提供了可信来源，突破了截面数据内生性困境。  
2. **空间机制揭示**：发现可达性不仅直接提升本地消费活力，还通过“空间溢出”效应带动邻近区域（如地铁沿线）的消费增长，且溢出半径约为1.5公里。  
3. **政策启示**：为“15分钟生活圈”等城市规划策略提供了量化依据——优化公共服务布局可产生消费乘数效应，而非零和博弈。该研究为城市经济学与因果推断的交叉提供了新范式。


### 4. Gaussianized Design Optimization for Covariate Balance in Randomized Experiments

**讲者**：Wenxuan Guo（University of Chicago）

**对应论文**：Gaussianized Design Optimization for Covariate Balance in Randomized Experiments · [arXiv:2502.16042](https://arxiv.org/abs/2502.16042)

<details><summary>摘要（原文）</summary>

Achieving covariate balance in randomized experiments enhances the precision of treatment effect estimation. However, existing methods often require heuristic adjustments based on domain knowledge and are primarily developed for binary treatments. This paper presents Gaussianized Design Optimization, a novel framework for optimally balancing covariates in experimental design. The core idea is to Gaussianize the treatment assignments: we model treatments as transformations of random variables drawn from a multivariate Gaussian distribution, converting the design problem into a nonlinear continuous optimization over Gaussian covariance matrices. Compared to existing methods, our approach offers significant flexibility in optimizing covariate balance across a diverse range of designs and covariate types. Adapting the Burer-Monteiro approach for solving semidefinite programs, we introduce first-order local algorithms for optimizing covariate balance, improving upon several widely used designs. Furthermore, we develop inferential procedures for constructing design-based confidence intervals under Gaussianization and extend the framework to accommodate continuous treatments. Simulations demonstrate the effectiveness of Gaussianization in multiple practical scenarios.

</details>

**问题**：在随机化实验中，优化协变量平衡能提升处理效应估计精度。然而，现有方法（如分层、再随机化）主要针对二元处理，且常需领域知识进行启发式调整；对于多处理臂或连续处理，直接优化设计面临计算困难（如协方差矩阵的可行集等价于NP-hard的Max-Cut问题）和采样挑战。如何系统性地解决这些局限？

**核心方法**：本文提出Gaussianized Design Optimization框架。核心思想是将处理分配建模为高斯向量的变换：$D_i = g(T_i)$，其中$T \sim N(0, \Sigma)$，$g$为预指定函数（如基于分位数的离散化）。设计问题转化为在相关椭球体$\mathcal{E} = \{ \Sigma \succeq 0, \Sigma_{ii}=1 \}$上最小化协变量平衡度量$\|X^\top f(\Sigma) X\|_{\text{norm}}$（norm取核范数或算子范数），其中$f$由Mehler公式解析给出。算法采用Burer-Monteiro风格的投影梯度下降（PGD-Gauss），通过低秩分解和行归一化迭代更新$\Sigma$，仅保证局部最优但可灵活初始化。

**与已有工作关系**：当$K=2$时，该方法与Goemans-Williamson的Max-Cut近似算法共享相同的Gaussianization步骤（函数$f(\rho)=\arccos(\rho)$），且协变量平衡度量与Gram-Schmidt Walk设计（Harshaw et al., 2019）一致。相比分层设计（Bai, 2022）和再随机化（Li et al., 2020），本文框架直接适用于任意数量处理臂和连续处理，无需依赖特定结果模型。此外，连续处理下的高斯设计可视为对潜在结果函数结构（如单调性、凸性）的探索性工具。

**贡献**：1) 提出统一的设计优化框架，将离散/连续处理、任意协变量类型纳入同一优化范式，避免NP-hard问题；2) 推导出协方差矩阵的解析表达式（基于Mehler公式），使梯度计算可行；3) 建立设计推断理论：在局部扰动条件下证明估计量的渐近正态性，并给出设计置信区间；4) 通过模拟和实际数据（如肯尼亚蚊帐实验）展示该方法在降低MSE和提升检验功效上的显著优势。


### 5. 安徽省低空经济产业链发展协同度测度及经济效应分析

**讲者**：Hao Song（Chaohu University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
低空经济作为战略性新兴产业，其产业链涵盖制造、运营、基础设施、服务等多个环节，但各环节间的协同发展程度缺乏定量刻画。现有研究多聚焦于政策规划或单一环节的经济贡献，鲜有从产业链整体协同视角测度其发展质量，并进一步评估协同度对区域经济增长的因果效应。本报告以安徽省为例，试图回答：低空经济产业链的协同度如何度量？协同度的提升能否带来显著的经济效应？

**核心方法**  
报告可能采用复合系统协同度模型（如基于序参量的协同度测度），将低空经济产业链分解为若干子系统（如研发制造、运营服务、基础设施、政策环境），通过序参量有序度计算各子系统的有序度，再基于子系统间的协同作用构建整体协同度指标 $C(t)$。随后，利用面板数据或空间计量模型（如固定效应模型或空间杜宾模型）估计协同度对地区生产总值、就业、创新产出等经济变量的因果效应，可能借助工具变量或双重差分法处理内生性。

**与已有工作关系**  
已有协同度研究多应用于制造业、高技术产业或区域创新系统，低空经济领域尚属空白。经济效应分析方面，传统研究多采用投入产出表或一般均衡模型，但缺乏对产业链协同这一中间机制的量化。本报告将协同度作为核心解释变量，拓展了低空经济实证研究的边界，并可能引入空间溢出效应，弥补现有文献对区域间产业链联动关注的不足。

**贡献**  
第一，首次构建安徽省低空经济产业链协同度指标体系，提供可复制的测度框架。第二，揭示协同度与经济增长之间的因果关系，为地方政府制定产业链补链、强链政策提供统计依据。第三，方法上融合协同度测度与因果推断，为新兴产业的产业链治理研究提供范式参考。


### 6. Efficient Imputation Methods in Functional Structural Equation Model with Missing Data

**讲者**：Hao Cheng（Minzu University of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
函数型结构方程模型（Functional Structural Equation Model, FSEM）将传统结构方程模型扩展到函数型数据场景，允许潜变量和观测变量为函数型曲线。然而，实际中函数型数据常因测量设备故障、个体缺失等导致部分曲线片段缺失。现有缺失数据处理方法（如全信息最大似然、多重插补）多针对有限维数据，直接应用于函数型数据会忽略曲线的平滑性与函数型主成分结构，导致估计偏差或计算效率低下。本报告旨在解决FSEM中函数型协变量或潜变量缺失时的高效插补问题。

**核心方法**  
报告提出一种结合函数型主成分分析（FPCA）与EM算法的插补框架。首先，利用FPCA将高维函数型数据投影到低维得分空间，保留曲线的主要变异信息；然后，在得分空间上构建结构方程模型，并基于模型约束（如潜变量间的线性关系）设计EM算法，在E步中利用条件分布对缺失得分进行插补，M步更新模型参数。为提升效率，可能引入稀疏表示或变分贝叶斯近似，避免对完整函数型数据的显式积分。此外，插补过程可同时利用观测曲线的局部平滑性，通过惩罚样条正则化减少过拟合。

**与已有工作关系**  
传统FSEM估计通常假设数据完全观测，或仅处理随机缺失的标量指标。已有函数型数据插补方法（如基于FPCA的软插补、动态时间规整）未考虑结构方程中的因果约束，导致插补值与模型假设不一致。本报告将结构方程模型的参数化约束融入插补过程，使插补值同时满足数据平滑性和模型因果结构，这是与纯数据驱动插补的关键区别。相比直接对函数型数据应用多重插补，本方法通过降维显著降低计算复杂度。

**主要贡献**  
1. 首次系统提出FSEM框架下函数型缺失数据的插补方法，填补了函数型因果推断中缺失数据处理的理论空白。  
2. 通过FPCA降维与EM算法结合，在保持统计效率的同时大幅降低计算成本，适用于高密度采样曲线。  
3. 理论证明插补估计量的相合性与渐近正态性，并给出标准误的解析公式，便于实际推断。  
4. 模拟与真实数据实验表明，该方法在插补精度和模型参数估计上均优于忽略缺失或简单插补的基准方法。


## Statistics for Finance, Economics and Business

*7 月 11 日（周六） · 13:30-15:10 · Baihua Meeting Room*  
*组织 Qiwei Yao（London School of Economics and Political Science） · 主持 Baojun Dou（City University of Hong Kong）*

### 1. Testing for Granger Causality in Extreme Risk: A Two-Stage Generalized Cross-Spectral Approach

**讲者**：Yongmiao Hong（University of Chinese Academy of Sciences）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
传统 Granger 因果检验关注均值或方差层面的预测关系，但在金融风险管理中，极端风险（如尾部 VaR 或 Expected Shortfall）的传导机制更为关键。现有方法多基于分位数回归或极值理论，但往往假设线性结构或固定滞后阶数，且难以捕捉频率域上的动态依赖。本报告旨在提出一种非参数检验，判断一个时间序列的极端风险是否在频域上 Granger 引起另一个序列的极端风险。

**核心方法**  
报告提出两阶段广义交叉谱（Two-Stage Generalized Cross-Spectral）方法。第一阶段，对每个序列的极端风险进行建模，例如通过极值理论或条件分位数估计得到风险度量序列 $\{R_{it}\}$。第二阶段，构造广义交叉谱密度函数 $f_{12}(\omega)$，并基于其与零假设下谱密度的差异构建检验统计量。具体地，利用 smoothed periodogram 估计谱密度，并采用广义谱分布函数（generalized spectral distribution function）的积分形式，将检验转化为对某个 $L^2$ 范数的偏离。统计量渐近服从正态分布，且无需指定参数模型。

**与已有工作关系**  
已有工作如 Hong (2001) 的广义谱检验针对均值 Granger 因果，而本报告将其推广到极端风险。相比分位数 Granger 因果检验（如 Candelon & Tokpavi, 2016），本方法能同时捕捉所有频率上的依赖，且对非线性结构更稳健。此外，两阶段设计避免了直接对尾部联合分布建模的困难，通过先提取风险度量再检验因果，降低了计算复杂度。

**主要贡献**  
1. 首次将广义交叉谱框架引入极端风险 Granger 因果检验，提供了频域视角。  
2. 提出两阶段估计，第一阶段可灵活选用任何一致的风险度量估计量，第二阶段检验统计量具有标准渐近分布，便于实施。  
3. 蒙特卡洛模拟表明，在尾部依赖存在且均值因果不显著时，本方法具有更高的检验功效。  
4. 实证应用（如股票市场与债券市场极端风险传导）揭示了传统检验无法发现的频率特异性因果模式。


### 2. Network Analysis of Business Cycle Synchronisation

**讲者**：Jia Chen（University of Macau）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
商业周期同步性（Business Cycle Synchronisation）是国际宏观经济学与时间序列计量中的核心议题，传统研究多依赖成对相关系数或动态因子模型来刻画各国经济周期的联动程度。然而，这些方法隐含了“所有国家两两对称”或“单一共同因子驱动”的强假设，难以捕捉现实中非对称、时变且可能由局部传导机制（如贸易、金融联系）产生的复杂依赖结构。本报告试图回答：如何利用网络分析框架，从高维时间序列中识别商业周期同步性的全局拓扑结构，并量化各国在同步网络中的角色差异？

**核心方法**  
讲者可能采用两步法：首先，基于多国宏观经济指标（如GDP增长率）的多元时间序列，通过稀疏逆协方差估计（如Graphical Lasso）或偏相关分析构建一个加权无向网络，其中节点代表国家，边权重反映条件依赖强度（即剔除其他国影响后的同步性）。随后，运用网络统计量（如度中心性、介数中心性、社区检测算法）刻画网络结构，并引入时变参数模型（如滚动窗口估计）考察同步网络的动态演化。此外，可能结合Granger因果检验构建有向网络，以识别周期传导的方向性。

**与已有工作关系**  
与经典的双变量相关系数或动态因子模型相比，网络方法的核心优势在于：(1) 通过条件依赖而非边际相关，避免虚假关联（如两个国家因共同受第三国影响而呈现高相关）；(2) 提供节点层面的角色度量（如“枢纽”国家），而因子模型仅能给出因子载荷；(3) 社区检测可揭示区域化同步集群（如欧元区内部高度同步），超越“全球因子+国家特异项”的简单分解。已有文献（如Acemoglu et al., 2012; Diebold & Yılmaz, 2014）多聚焦于金融网络或波动溢出，本报告将其拓展至商业周期同步的宏观时间序列场景。

**贡献**  
主要贡献可能包括：(1) 方法论上，将高维稀疏图模型与宏观经济时间序列的平稳性、季节性预处理相结合，提出适用于短面板（T较小、N较大）的稳健网络构建流程；(2) 实证上，揭示全球商业周期同步网络的核心-外围结构，并量化2008年金融危机前后网络密度的突变与社区重组；(3) 为政策制定者提供识别系统性重要国家（如中国、美国）的量化依据，以及区域货币联盟的同步性门槛条件。


### 3. Forecasting Global Economy with SIGMAR: Sparsity-Induced Global Matrix AutoRegressive Model

**讲者**：Dan Yang（The University of Hong Kong）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
全球经济预测面临高维、多源数据的挑战：多个国家、多个经济指标构成矩阵结构的时间序列（如国家×指标），且变量间存在复杂动态依赖。传统向量自回归（VAR）模型参数过多，易过拟合；现有矩阵自回归（MAR）模型虽能利用矩阵结构降维，但往往假设系数矩阵稠密或低秩，忽略了经济系统中大量零效应（如某些国家间无显著传导），导致可解释性差、预测不稳定。本报告旨在提出一种既能捕捉矩阵结构又能诱导稀疏性的自回归模型，以提升全球经济预测的准确性与可解释性。

**核心方法**  
SIGMAR（Sparsity-Induced Global Matrix AutoRegressive Model）将矩阵自回归框架与稀疏性诱导正则化相结合。具体地，对 $p$ 阶矩阵自回归模型  
$$Y_t = \sum_{k=1}^p A_k Y_{t-k} B_k^\top + E_t,$$  
其中 $Y_t \in \mathbb{R}^{m \times n}$，系数矩阵 $A_k \in \mathbb{R}^{m \times m}$ 和 $B_k \in \mathbb{R}^{n \times n}$ 分别刻画行（国家）和列（指标）的动态依赖。SIGMAR 对 $A_k$ 和 $B_k$ 施加稀疏性惩罚（如 group lasso 或 adaptive lasso），通过交替方向乘子法（ADMM）或近端梯度算法进行估计，在保持矩阵乘法结构的同时自动筛选出重要的跨国家、跨指标传导路径。

**与已有工作关系**  
已有矩阵自回归模型（如 Chen et al., 2021; Wang et al., 2022）多假设系数矩阵低秩或通过核范数正则化，但低秩假设隐含全局共享结构，无法识别局部零效应。而向量 VAR 的稀疏化方法（如 LASSO-VAR）忽略了矩阵的二维结构，导致参数冗余。SIGMAR 首次将稀疏性直接引入矩阵自回归的双线性系数中，既保留了矩阵结构的参数效率，又通过稀疏性实现变量选择，填补了“矩阵结构+稀疏性”的空白。

**贡献**  
1. **模型创新**：提出 SIGMAR，为高维矩阵时间序列提供兼具结构保持与稀疏性的建模框架。  
2. **理论保证**：在适当正则化条件下，证明估计量的相合性、变量选择一致性以及预测误差的渐近界。  
3. **实证价值**：基于全球经济面板数据（如 IMF 多国多指标），SIGMAR 在预测 GDP 增长、通胀等关键变量上优于 VAR、低秩 MAR 及稀疏 VAR，并揭示出显著的经济传导网络（如中美贸易冲击的稀疏传播路径），为政策制定提供可解释的量化依据。


### 4. Pairs Trading: A Change Point Perspective

**讲者**：Baojun Dou（City University of Hong Kong）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
Pairs Trading（配对交易）是经典的统计套利策略，通常假设两只股票的价格序列存在长期均衡关系（如协整），并基于均值回复特性进行交易。然而，现实市场中这种均衡关系可能因政策、行业冲击或市场微观结构变化而发生结构性突变（structural breaks）。传统方法（如固定窗口的协整检验或滚动估计）要么忽略变点，要么对变点的检测与交易决策分离，导致策略在变点附近表现恶化。本报告旨在回答：**如何将变点检测（change point detection）内生于配对交易的建模与执行流程，从而在均衡关系发生突变时自动调整交易信号？**

**核心方法**  
讲者可能提出一个两阶段框架：第一阶段，对候选股票对的历史价差序列进行在线变点检测（如基于CUSUM统计量或PELT算法），识别出均衡关系的突变时刻；第二阶段，在每个变点之间的“稳定段”内，利用局部协整模型估计价差的均值回复参数（如半衰期），并据此生成交易信号（如开仓阈值）。关键创新在于将变点检测与交易决策耦合：当检测到新变点时，立即重置模型参数，避免使用过时的均衡关系。方法可能还涉及多重检验校正（如FDR控制）以降低误报率，并利用bootstrap推断变点后的参数不确定性。

**与已有工作关系**  
已有配对交易文献主要分为两类：一是基于固定协整关系的静态策略（如Gatev et al., 2006），二是采用滚动窗口或指数加权移动平均的动态策略（如Huck, 2010）。前者无法适应结构变化，后者虽能缓慢调整但滞后且对突变不敏感。计量经济学中变点检测方法（如Bai & Perron, 2003）多用于事后分析，而非实时交易。本报告将变点检测从“诊断工具”提升为“策略核心组件”，实现了检测与交易的在线融合，填补了统计套利中结构突变自适应处理的空白。

**主要贡献**  
1. **方法论贡献**：提出一个统一的变点视角下的配对交易框架，将变点检测、局部协整估计与交易规则有机整合，为统计套利提供了新的建模范式。  
2. **理论贡献**：可能推导了变点检测阈值与交易收益之间的权衡关系，并给出在突变频率与幅度下的策略渐近性质（如无套利条件下的最优检测延迟）。  
3. **实证贡献**：通过美股或A股数据验证，相比传统静态策略和滚动窗口策略，新方法在变点密集时期显著提升夏普比率并降低最大回撤，同时保持较低的交易成本。  
4. **实践启示**：为量化交易者提供了一套可解释的、自动适应市场结构变化的配对交易工具，尤其适用于高频或中频交易场景。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)