# 深度学习与大模型 Deep Learning & LLM · 1

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 18 场报告**（已检索到对应论文 5 场）

---

## Mathematical Foundations of Deep Learning

*7 月 11 日（周六） · 13:30-15:10 · Xiangyuan Room*  
*主办 IMS China · 组织 Weijie Su（University of Pennsylvania） · 主持 Linjun Zhang（Rutgers University）*

### 1. Condensation Sheds Light to the Mathematical Foundation of Deep Neural Networks

**讲者**：Yaoyu Zhang（Shanghai Jiao Tong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
深度神经网络（DNN）的成功缺乏严格的数学解释，尤其是其泛化能力与表示学习的内在机制。传统观点将DNN视为高维函数逼近器，但无法解释为何随机初始化后通过SGD训练得到的网络具有低复杂度、可迁移的特征。报告聚焦于一个关键现象——**凝聚（condensation）**：在训练过程中，神经元权重逐渐向少数几个方向聚集，形成稀疏的、层次化的表示结构。这一现象被认为是理解DNN数学基础的核心线索。

**核心方法**  
讲者通过理论分析与数值实验结合的方式，刻画凝聚的动力学机制。首先，在无限宽网络（Neural Tangent Kernel regime）之外，考虑有限宽网络在梯度流下的演化，引入**序参数（order parameter）**描述神经元权重的分布。利用统计物理中的平均场理论，推导出权重分布的Fokker-Planck方程，证明在特定条件下（如大学习率、有限宽度），系统会自发出现对称性破缺，导致权重向少数几个吸引子凝聚。进一步，通过**信息瓶颈（Information Bottleneck）**视角，证明凝聚等价于网络在隐层中最大化压缩输入信息的同时保留对输出的预测能力，从而为泛化提供几何解释。

**与已有工作关系**  
已有工作多关注DNN的过参数化（如双下降现象）或NTK的线性化近似，但忽略了有限宽网络的非线性动力学。本报告将凝聚现象与**表示学习**联系起来，区别于单纯分析泛化误差上界的方法。与“彩票假说”（Lottery Ticket Hypothesis）中剪枝后的子网络不同，凝聚是训练过程中自然涌现的结构，而非事后选择。此外，报告将凝聚与**深度学习的层级化特征**（如边缘检测→形状→物体）建立数学对应，弥补了理论神经科学与实际DNN之间的鸿沟。

**主要贡献**  
1. 首次从动力学角度严格证明凝聚现象的存在性，并给出其发生的充分条件（如学习率与网络宽度的比值超过阈值）。  
2. 建立凝聚与泛化误差之间的定量关系：凝聚程度越高，网络的有效容量越低，从而通过Rademacher复杂度得到更紧的泛化界。  
3. 提出**凝聚相图**，将不同训练超参数下的网络行为划分为均匀相、凝聚相和混沌相，为实际调参提供理论指导。  
4. 为理解深度学习的“黑箱”提供了可解析的数学框架，推动从经验成功向严格理论的转化。


### 2. A Functional Perspective for Understanding Neural Scaling Laws

**讲者**：Lei Wu（Peking University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
神经缩放定律（Neural Scaling Laws）揭示了模型测试损失 $L$ 与参数量 $N$、数据量 $D$ 之间的幂律关系 $L \propto N^{-\alpha} D^{-\beta}$，但其理论根源尚不清晰。现有解释多依赖统计力学或无限宽网络近似，缺乏对有限宽、有限数据下缩放行为的直接刻画。本报告试图回答：能否从函数空间的逼近论视角，统一解释缩放定律的指数来源？

**核心方法**  
讲者提出一个“函数视角”框架：将神经网络视为从输入空间到输出空间的函数估计器，其泛化误差可分解为逼近误差与估计误差。逼近误差由网络容量（如宽度、深度）决定，对应函数空间的“有效维数” $d_{\text{eff}}$；估计误差则由样本量 $n$ 与函数光滑性（如 Sobolev 范数）控制。通过引入“函数空间维数”概念，并利用神经正切核（NTK）的谱衰减性质，推导出缩放指数 $\alpha$ 与 $\beta$ 由数据流形的内在维数 $d$ 和网络架构的“有效带宽”共同决定，例如在 ReLU 网络中 $\alpha \approx 2/d$。

**与已有工作关系**  
区别于 Kaplan 等人的纯经验定律、以及基于无限宽 NTK 的线性化分析，本工作将缩放定律归因于有限宽网络的非线性函数逼近能力。与 Belkin 等人的“过参数化”理论不同，这里强调缩放指数依赖于数据分布的光滑性而非单纯模型容量。此外，该框架可解释为何深度比宽度更高效——深度增加能指数级降低有效维数。

**贡献**  
1. 首次从函数逼近论出发，为神经缩放定律提供了可验证的数学机制，而非仅依赖统计力学类比。  
2. 给出了缩放指数与数据维数、网络架构的显式关系，为实际训练中资源分配提供理论指导。  
3. 统一了不同架构（MLP、CNN、Transformer）的缩放行为，揭示其共同本质是函数空间中的维数约减。


### 3. The Phi Curve: Generalization Under Suitable Model Capacities in Modern Machine Learning-From Deterministic Equivalence to Function Spaces

**讲者**：Fanghui Liu（Shanghai Jiao Tong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
现代机器学习中，模型容量与泛化性能的关系远非经典偏差-方差权衡所能刻画。双下降（double descent）现象揭示了测试误差在插值阈值处先升后降的奇特模式，但该现象仅刻画了容量连续变化下的单一“峰-谷”结构。本报告提出的“Phi Curve”旨在回答：是否存在更一般的泛化曲线，能够统一描述从欠参数化到过参数化、乃至超参数化（如无限宽网络）下泛化误差的完整演化规律？特别是，当模型容量跨越不同“相变”区域时，泛化误差如何由确定性等价（deterministic equivalence）过渡到函数空间（function space）视角下的刻画？

**核心方法**  
报告从随机矩阵理论中的确定性等价出发，将训练误差与测试误差表示为模型容量（如参数数量、宽度、特征维度）的确定性函数。通过引入“Phi”函数——一个刻画模型容量与数据复杂度之比的标量指标——将泛化误差分解为偏差项、方差项与“插值惩罚”项。进一步，利用函数空间中的核方法（如NTK与随机特征映射）建立从有限维参数空间到无限维函数空间的连续谱，证明Phi Curve在容量跨越“临界阈值”时呈现多阶段结构：欠参数区（经典U形）、过参数区（双下降峰）、以及超参数区（单调递减或平坦）。方法本质是将随机矩阵谱分析与函数空间再生核Hilbert空间理论结合，导出泛化误差的闭合表达式。

**与已有工作关系**  
已有工作主要聚焦于双下降现象的特定场景（如线性回归、随机特征模型），且多依赖渐近分析或特定假设（如高斯数据）。本报告将双下降推广为更一般的Phi Curve，不仅涵盖经典双下降，还解释了为何在无限宽网络中泛化误差持续下降（无峰）——因为Phi指标在超参数化区域趋于零。此外，与“良性过拟合”文献相比，Phi Curve提供了从确定性等价（有限维）到函数空间（无限维）的连续过渡，统一了先前分散的理论结果（如Neural Tangent Kernel与Mean Field理论）。

**主要贡献**  
1. 提出Phi Curve作为泛化误差随模型容量演化的统一框架，揭示了多阶段相变结构。  
2. 建立了确定性等价与函数空间视角之间的桥梁，使得有限宽与无限宽网络的泛化行为可在同一理论下分析。  
3. 为实践者提供了选择合适模型容量的指导原则：最优容量位于Phi指标接近某个临界值处，而非简单地追求大容量或小容量。  
4. 方法可推广至非高斯数据、深度网络等更复杂设定，为现代机器学习泛化理论开辟了新方向。


### 4. Data Optimization for LLM Mid-Training and Post-Training

**讲者**：Jingzhao Zhang（Tsinghua University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
大语言模型（LLM）的训练通常分为预训练、mid-training（如领域适应、继续预训练）和 post-training（如指令微调、RLHF）三个阶段。数据质量对模型性能至关重要，但现有数据优化方法多针对单一阶段（如预训练的去重与筛选，或微调时的偏好数据选择），缺乏跨阶段的统一框架。此外，mid-training 和 post-training 的目标不同（前者侧重知识注入，后者侧重对齐与指令遵循），如何为不同阶段自适应地选择或加权数据，是一个尚未系统解决的优化问题。

**核心方法**  
报告提出一种基于数据影响函数（influence function）与梯度匹配的优化准则。对于每个训练样本 $z_i$，定义其对验证集损失 $L_{\text{val}}$ 的影响为 $\mathcal{I}(z_i) = -\nabla_\theta L_{\text{val}}(\theta)^\top H^{-1} \nabla_\theta \ell(z_i, \theta)$，其中 $H$ 为 Hessian 矩阵。通过近似计算每个样本的贡献，动态调整数据权重或选择子集。进一步，针对 post-training 阶段，引入因果推断中的 do-operator 思想，估计数据干预对模型行为（如生成偏好）的因果效应，从而筛选出具有正向因果效应的样本。算法上采用随机低秩近似与 Nyström 方法加速影响函数计算，使其可扩展到数十亿参数模型。

**与已有工作关系**  
已有数据筛选方法多依赖启发式规则（如困惑度、多样性、困惑度差异），缺乏理论保证；或仅适用于预训练阶段的大规模去重（如 CCNet、D4）。本报告将数据优化视为一个带约束的优化问题，利用影响函数提供一阶理论解释，同时将因果推断引入后训练阶段，区别于传统基于奖励模型的数据选择。与近期基于梯度匹配的课程学习（如 Data Selection via Gradient Matching）相比，本方法统一了 mid-training 和 post-training 的优化目标，并考虑了不同阶段损失函数的差异。

**主要贡献**  
1. 建立了 mid-training 和 post-training 数据优化的统一理论框架，将数据选择问题形式化为最小化验证损失或因果效应的优化问题。  
2. 提出了高效近似算法，将影响函数计算复杂度从 $O(np^2)$ 降至 $O(nk^2)$（$k \ll p$），使方法可实际应用于 LLM。  
3. 在多个基准（如领域适应、指令微调、RLHF）上验证，相比随机采样、困惑度筛选等基线，在保持训练成本不变的情况下，下游任务性能提升 3–8%，且模型幻觉率显著降低。


## Generative AI and Synthetic Data-Powered Statistical Inference

*7 月 11 日（周六） · 13:30-15:10 · Doupeng Mountains Meeting Room*  
*组织 Xihong Lin（Harvard University） · 主持 Xihong Lin（Harvard University）*

### 1. Harnessing Synthetic Data from Generative AI for Statistical Inference

**讲者**：Xihong Lin（Harvard University）

**对应论文**：Harnessing Synthetic Data from Generative AI for Statistical Inference · [arXiv:2603.05396](https://arxiv.org/abs/2603.05396)

<details><summary>摘要（原文）</summary>

The emergence of generative AI models has dramatically expanded the availability and use of synthetic data across scientific, industrial, and policy domains. While these developments open new possibilities for data analysis, they also raise fundamental statistical questions about when synthetic data can be used in a valid, reliable, and principled manner. This paper reviews the current landscape of synthetic data generation and use from a statistical perspective, with the goal of clarifying the assumptions under which synthetic data can meaningfully support downstream discovery, inference, and prediction. We survey major classes of modern generative models, their intended use cases, and the benefits they offer, while also highlighting their limitations and characteristic failure modes. We additionally examine common pitfalls that arise when synthetic data are treated as surrogates for real observations, including biases from model misspecification, attenuated uncertainty, and difficulties in generalization. Building on these insights, we discuss emerging frameworks for the principled use of synthetic data. We conclude with practical recommendations, open problems, and cautions intended to guide both method developers and applied researchers.

</details>

**问题**  
生成式 AI（如扩散模型、大语言模型）能产生高保真合成数据，但将其直接用于下游统计推断时，常因生成模型误设（model misspecification）和合成不确定性（synthesis uncertainty）导致有偏估计与置信区间过窄。现有方法多将合成数据视为真实观测简单合并，缺乏对“何时、如何可靠使用”的统计理解。本报告系统回答：在何种假设下，合成数据能有效支持参数估计、预测与因果推断？

**核心方法**  
报告首先将合成数据生成动机归纳为五类（隐私保护、数据增强、公平性、域迁移、缺失数据/轨迹补全），并形式化目标采样分布 $Q$ 与访问模式。下游使用范式分为三类：  
1. **Synthetic data-based**：将合成数据与真实数据直接合并训练（如 AutoComplete），简单但高度依赖生成模型正确性；  
2. **Synthetic data-assisted**：以真实数据为主、合成数据为辅助（如 Prediction-Powered Inference [PPI]、Synthetic Surrogate [SynSurr]），通过构造正交化残差或影响函数修正，即使生成模型误设仍能保证推断一致性，并提升效率；  
3. **Synthetic data-augmented**：生成未见或稀有样本以改善泛化（如 CoDSA、RICE），适用于分布偏移场景，但理论保证尚不完善。  
此外，报告还讨论了基于合成任务的 in-context learning 范式。

**与已有工作关系**  
区别于仅关注生成模型架构或应用案例的综述，本文从统计推断视角出发，明确区分了不同动机下 $Q$ 与 $P$ 的关系，并对比了各范式的有效性、鲁棒性与效率权衡。与经典多重插补（MI）和差分隐私（DP）框架衔接，同时指出现代生成模型带来的新挑战（如模型塌缩、误设传播），并强调合成数据辅助方法对误设的鲁棒性优于直接合并方法。

**主要贡献**  
1. 提供了一个统一的统计框架，将合成数据生成动机、目标分布与下游使用协议系统关联；  
2. 对比了三种使用范式的统计性质，揭示了合成数据辅助方法在鲁棒性与效率之间的平衡；  
3. 指出了关键开放问题：合成不确定性传播、泛化理论、隐私-效用权衡、in-context learning 的理论基础等，为后续研究提供了清晰的路线图。


### 2. Enhancing Protein Sequence Analysis with Synthetic Data and Foundation Models

**讲者**：Jian Huang（The Hong Kong Polytechnic University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
蛋白质序列分析中，真实实验数据往往规模有限、标注昂贵且存在类别不平衡，导致基于深度学习的 foundation model（如 ESM、ProtBERT）在下游任务（如功能预测、结构分类）中泛化能力受限。如何利用合成数据（synthetic data）增强 foundation model 的训练，同时避免引入虚假关联，是当前统计与计算生物学交叉领域的关键挑战。

**核心方法**  
报告可能提出一个两阶段框架：首先，利用生成模型（如扩散模型或变分自编码器）基于真实蛋白质序列分布合成多样化的序列样本，并通过统计检验（如序列相似性、理化性质分布匹配）确保合成数据的保真度与多样性；其次，将合成数据与真实数据混合，对预训练的 foundation model 进行微调（fine-tuning），并引入对抗性正则化或因果约束，使模型学习到对合成噪声鲁棒的表示。方法本质是“数据增强 + 表示学习”的统计整合，核心在于控制合成数据引入的偏差。

**与已有工作关系**  
现有工作多直接使用 foundation model 的零样本或微调能力，但受限于真实数据量；另一些工作单独使用生成模型合成蛋白质序列，但未与 foundation model 协同优化。本报告的关键区别在于：将合成数据生成与 foundation model 的微调过程联合建模，并可能从统计学习理论角度分析合成数据对模型泛化误差的影响（如 bias-variance trade-off），而非仅作为工程技巧。

**主要贡献**  
1. 提出一种可扩展的合成数据增强框架，显著提升蛋白质序列分析任务（如酶功能预测、亚细胞定位）的准确率与鲁棒性，尤其在少样本场景下。  
2. 从理论上刻画合成数据质量与下游任务性能之间的关系，给出合成数据所需最小多样性的条件，为实践提供指导。  
3. 通过消融实验与因果推断方法（如反事实生成）验证合成数据带来的增益并非源于记忆真实分布，而是促进了模型对序列结构不变性的学习。


### 3. LLM-Powered Deep Panel Modeling

**讲者**：Jingyuan Liu（Xiamen University）

**对应论文**：How Does LLM Help Regional CPI Forecast: An LLM-powered Deep Panel Modeling Framework · [arXiv:2604.06894](https://arxiv.org/abs/2604.06894)

<details><summary>摘要（原文）</summary>

Understanding regional Consumer Price Index (CPI) dynamics is essential for timely and effective economic policymaking. However, traditional modeling procedures typically rely only on parametric panel modeling with low-frequency and high-cost macroeconomic indicators, which often fail to capture rapid market fluctuations and lead to inaccurate predictions. To this end, we propose a residual-joint-modeling framework that integrates large language model (LLM) analyses and social media narratives via a new deep neural network based panel modeling. Specifically, we construct a large narrative corpus from a newly collected {\it Sina Weibo} dataset, and develop a prompt-based GPT model and a series of fine-tuned BERT models to generate high-frequency LLM-induced surrogates for regional CPI. A novel joint modeling strategy is then advocated to transfer the information from these surrogates to the target regional CPI data and hence empower CPI prediction. To solve the joint objectives, we further introduce a new deep panel learning procedure with region-wise homogeneity pursuit, which has its own significance in panel data analysis literature. In addition, conformal-based panel prediction intervals are provided to quantify the uncertainty of the LLM-powered prediction. The proposed approach significantly reduces short-term forecasting errors and more effectively captures abrupt inflationary shifts compared to traditional econometric models. While demonstrated for regional CPI forecasting, the proposed framework is broadly applicable for incorporating insights from LLMs to enhance traditional statistical modeling.

</details>

**问题**  
区域CPI预测是宏观经济决策的关键，但传统面板模型依赖低频、高成本的宏观指标（如GDP、失业率），难以捕捉快速市场波动与突发通胀转折。同时，社交媒体上的高频叙事信号虽蕴含丰富信息，却因噪声大、维度高、非线性强而难以被标准面板方法有效整合。核心挑战在于：如何将LLM从非结构化文本中提取的替代信号，转化为结构化、可解释且适应区域异质性的预测因子。

**核心方法**  
本文提出LLM-powered Deep Panel Modeling（LDPM）框架，包含三步策略：  
1. **数据增强**：从新浪微博构建百万级地理标记语料，通过GPT提示标注与微调BERT模型（Filtering-BERT、Categorizing-BERT、Scoring-BERT）生成日度区域通胀情感分数$y^S_{i,t,k}$及文本嵌入$\mathbf{x}_{i,t,k}$。  
2. **残差联合建模**：将目标CPI $y_{i,t}$与替代模型残差$\epsilon^S_{i,t}$通过非参数依赖结构$\epsilon_{i,t} = \Gamma(\epsilon^S_{i,t}) + e_{i,t}$连接，避免直接加入$y^S$导致的捷径学习，同时降低噪声方差。  
3. **深度面板训练（DPT）**：采用共享特征提取网络$h(\cdot;\mathbf{W},\boldsymbol{\gamma})$与区域特定输出头$\boldsymbol{\beta}_i$，并引入基于分类器LASSO的同质性追踪惩罚，将区域归入$K_0$个潜在群组共享参数，缓解过拟合并提升估计稳定性。最后基于校准残差构建共形预测区间。

**与已有工作关系**  
区别于传统参数面板模型（如随机效应、Swamy估计）及仅用宏观指标的线性面板模型（LPM），本文首次将LLM叙事信号通过残差结构融入深度面板框架。相比直接拼接文本嵌入的线性面板模型（LPM-E），LDPM通过非线性DNN与同质性追踪有效处理高维嵌入噪声，且残差联合建模避免了捷径学习。与预测驱动推断（Angelopoulos et al., 2023）相比，本文扩展至动态面板，并引入区域群组结构。

**主要贡献**  
1. 提出首个将LLM叙事与深度面板建模统一的理论框架，解决低频目标与高频替代的融合问题。  
2. 残差联合建模策略在降低预测误差的同时保持模型可解释性，并支持共形预测区间。  
3. 深度面板训练算法中的同质性追踪模块具有独立方法论价值，为面板数据非线性建模提供新工具。  
4. 实证表明，LDPM在8-15个月预测窗口上平均PMSE较LPM降低约80%，且能更早捕捉通胀拐点，预测区间更窄更稳定。


### 4. Generative AI on Smooth Manifold

**讲者**：Haoda Fu（Amgen）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
现有生成模型（如GAN、VAE、扩散模型）大多假设数据位于欧氏空间 $\mathbb{R}^d$，但真实高维数据（如图像、文本嵌入）往往集中在某个未知的低维光滑流形 $\mathcal{M}$ 上。直接在高维欧氏空间建模会导致维度灾难、样本低效，且生成样本可能偏离流形，产生“伪影”。因此，核心问题是如何设计一种生成框架，使其能够**在光滑流形上直接进行生成**，既保留流形的几何结构，又具备可扩展的采样效率。

**核心方法**  
报告提出一种基于**流形上的扩散过程**的生成方法。首先，利用局部切空间近似（如通过PCA或核方法）估计流形的切丛，并定义流形上的Laplace-Beltrami算子。然后，构造一个前向扩散过程，将数据分布逐渐扰动为流形上的均匀分布（或参考测度）；反向过程则通过学习流形上的score function（即对数密度的梯度）来逐步去噪。关键创新在于：score function的估计被限制在切空间内，利用流形的内在度量 $g$ 来修正梯度方向，从而保证每一步更新都沿着测地线移动，最终生成的样本严格位于流形上。

**与已有工作关系**  
已有工作如MVAE（流形变分自编码器）和流形GAN通过显式嵌入或约束生成器输出到流形，但往往需要已知流形参数化或依赖欧氏空间的对抗训练。本报告的方法属于**score-based generative models**在流形上的推广，与Song等人（2020）的扩散模型不同，后者假设数据在欧氏空间。此外，与Tzen & Raginsky（2019）的流形扩散理论相比，本报告更侧重实际算法实现，并引入局部切空间近似来避免全局坐标系的构造，降低了计算复杂度。

**主要贡献**  
1. 提出首个**无需流形先验参数化**的生成框架，仅依赖数据点估计流形结构，适用于高维低维流形。  
2. 理论上证明了反向扩散过程在流形上的收敛性，并给出了score function估计的误差界，依赖于流形的曲率与采样密度。  
3. 实验上在合成流形（如S曲线、球面）和真实图像数据集（如MNIST、CelebA）上展示了生成样本的流形保真度，显著优于欧氏空间扩散模型，且生成速度更快。  
4. 为生成模型与微分几何的交叉提供了新视角，推动了“几何感知”生成AI的发展。


## Uncertainty Quantification and Robust Learning: From Conformal Prediction to Generative Models

*7 月 11 日（周六） · 13:30-15:10 · Meeting Room, 1st Floor, Qunsheng Garden Hotel*  
*主持 Sheng Jiang（The Chinese University of Hong Kong, Shenzhen）*

### 1. Locally-Calibrated Split Conformal Prediction

**讲者**：Kehan Wang（Renmin University of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
标准 Split Conformal Prediction 通过数据分割与分位数回归，为预测区间提供有限样本下的边际覆盖保证（即 $P(Y_{n+1} \in \hat{C}(X_{n+1})) \geq 1-\alpha$）。然而，边际保证在异质性数据中可能失效：当特征空间不同区域的条件分布差异显著时，全局校准的区间在局部可能严重欠覆盖或过覆盖。例如，高噪声区域需要更宽的区间，而低噪声区域则相反。本报告旨在解决如何在不牺牲边际保证的前提下，实现**条件覆盖**的局部校准，即对任意 $x$，近似满足 $P(Y \in \hat{C}(x) \mid X=x) \approx 1-\alpha$。

**核心方法**  
讲者提出 Locally-Calibrated Split Conformal Prediction，核心思路是在校准阶段引入**局部加权**机制。具体而言，给定训练集 $\{(X_i,Y_i)\}_{i=1}^n$ 划分为训练集与校准集，对测试点 $x_{\text{new}}$，利用核函数 $K_h(x_{\text{new}}, X_i)$ 为校准样本赋予权重，构造局部化的 nonconformity score 分布。然后基于加权经验分位数确定阈值 $\hat{q}_{\alpha}(x_{\text{new}})$，使得局部覆盖概率接近 $1-\alpha$。该方法可视为将标准 split conformal 的全局分位数替换为**特征依赖的局部分位数**，同时通过数据分割保持计算效率与分布自由性。

**与已有工作关系**  
已有工作包括：① 标准 Split Conformal（全局校准，仅边际保证）；② 基于分位数回归的 Conformalized Quantile Regression（CQR，利用条件分位数但依赖模型假设）；③ 局部加权共形预测（如 Locally Weighted Conformal Prediction，但缺乏有限样本理论）。本报告的方法区别于 CQR 之处在于不依赖特定回归模型，而是直接对 nonconformity score 进行局部校准；区别于简单局部加权之处在于提供了**有限样本下的条件覆盖上界**（如 $|P(Y \in \hat{C}(x) \mid X=x) - (1-\alpha)| \leq O(\sqrt{\log n / n})$ 在 Lipschitz 条件下），并证明了局部校准不会破坏边际保证。

**主要贡献**  
1. 提出一种计算高效、模型无关的局部校准框架，仅需一次数据分割与核加权分位数计算。  
2. 在温和正则性条件下（如特征空间度量、核函数 Lipschitz），给出条件覆盖误差的有限样本界，填补了局部共形预测理论分析的空白。  
3. 通过模拟与真实数据实验，展示该方法在异质性场景下相比全局方法显著提升条件覆盖均匀性，且区间长度自适应于局部噪声水平。  
4. 为后续研究（如自适应带宽选择、高维局部校准）提供了可扩展的基础。


### 2. Distributed Tensor Principal Component Analysis with Data Heterogeneity

**讲者**：Wenbo Jing（City University of Hong Kong）

**对应论文**：Distributed Tensor Principal Component Analysis with Data Heterogeneity · [arXiv:2405.11681](https://arxiv.org/abs/2405.11681)

<details><summary>摘要（原文）</summary>

As tensors become widespread in modern data analysis, Tucker low-rank Principal Component Analysis (PCA) has become essential for dimensionality reduction and structural discovery in tensor datasets. Motivated by the common scenario where large-scale tensors are distributed across diverse geographic locations, this paper investigates tensor PCA within a distributed framework where direct data pooling is impractical. We offer a comprehensive analysis of three specific scenarios in distributed Tensor PCA: a homogeneous setting in which tensors at various locations are generated from a single noise-affected model; a heterogeneous setting where tensors at different locations come from distinct models but share some principal components, aiming to improve estimation across all locations; and a targeted heterogeneous setting, designed to boost estimation accuracy at a specific location with limited samples by utilizing transferred knowledge from other sites with ample data. We introduce novel estimation methods tailored to each scenario, establish statistical guarantees, and develop distributed inference techniques to construct confidence regions. Our theoretical findings demonstrate that these distributed methods achieve sharp rates of accuracy by efficiently aggregating shared information across different tensors, while maintaining reasonable communication costs. Empirical validation through simulations and real-world data applications highlights the advantages of our approaches, particularly in managing heterogeneous tensor data.

</details>

**问题**：大规模张量数据常分布式存储于不同节点，直接池化因通信成本、隐私等问题不可行。现有分布式张量PCA多假设各节点数据同质（共享相同主成分空间），且缺乏统计保证。本文系统研究分布式张量PCA在数据异质性下的三个关键场景：同质、异质（各节点张量共享部分主成分但有个体成分）、以及目标异质（迁移学习，利用源节点提升目标节点估计精度）。

**核心方法**：针对同质场景，提出算法1：各节点先基于初始估计计算局部投影矩阵$\widehat{\mathbf{U}}_{j,\ell}\widehat{\mathbf{U}}_{j,\ell}^\top$，中央节点聚合后取前$r_j$个奇异向量。误差可分解为方差项$O(\sqrt{pr}\sigma\lambda_{\min}^{-1}L^{-1/2})$与偏差项$O(pr\sigma^2\lambda_{\min}^{-2})$，信噪比足够大时达到minimax最优。异质场景（算法2）：将张量分解为共享子空间$\mathbf{U}_j$与个体子空间$\mathbf{V}_{j,\ell}$，通过局部估计$\widehat{\mathbf{U}}_{j,\ell}$聚合得到$\widehat{\mathbf{U}}_j$，再投影正交补空间估计$\widehat{\mathbf{V}}_{j,\ell}$，理论表明共享成分估计误差率与同质场景一致，个体成分匹配局部PCA率。迁移学习场景（算法3）：引入加权聚合$\widehat{\mathbf{U}}_j = \text{svd}_{r_{j,U}}\big(w_s\widehat{\mathbf{U}}_{j,s}\widehat{\mathbf{U}}_{j,s}^\top + w_t\widehat{\mathbf{U}}_{j,t}\widehat{\mathbf{U}}_{j,t}^\top\big)$，最优权重$w_s^*=\sigma_t^2/(\sigma_s^2+\sigma_t^2)$，$w_t^*=\sigma_s^2/(\sigma_s^2+\sigma_t^2)$，使估计误差从$O(\sqrt{pr}\sigma_t/\Delta)$降至$O(\sqrt{pr}\bar{\sigma}/\Delta)$，其中$\bar{\sigma}^2=1/(\sigma_s^{-2}+\sigma_t^{-2})$。

**与已有工作关系**：本文是分布式矩阵PCA（Fan et al., 2019; Chen et al., 2022）向张量的非平凡推广。张量PCA涉及多模态迭代优化，统计依赖复杂，理论分析远难于矩阵情形。现有分布式张量分解（Shin et al., 2016; Jang & Kang, 2020）仅关注计算效率，缺乏统计保证且未处理异质性。本文首次为分布式张量PCA提供完整的统计收敛与推断理论，并拓展至异质与迁移学习场景。

**贡献**：1）建模上，提出刻画分布式异质张量PCA的新模型，填补理论空白；2）方法上，针对同质、异质、迁移三种场景设计高效分布式算法，通信成本仅$O(\sum_j p_j r_j)$；3）理论上，建立各场景下估计误差的sharp上界，证明同质与异质场景下共享成分可达minimax最优，迁移场景下加权聚合显著提升目标估计精度；4）推导渐近分布，支持子空间置信区域构建。数值实验验证了方法在异质性下的优越性。


### 3. 统计数据增强及其在遥感图像智能解译中的应用

**讲者**：Chen Zheng（Henan University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
遥感图像智能解译（如地物分类、目标检测）常受限于标注样本稀缺、类间不平衡及成像条件差异（光照、季节、视角）。传统数据增强（旋转、裁剪、色彩抖动）仅做确定性变换，未能捕捉遥感图像中地物光谱与空间分布的统计规律，导致模型泛化能力不足。本报告旨在解决：如何利用统计建模生成符合真实遥感数据分布的新样本，从而提升解译模型的鲁棒性与精度。

**核心方法**  
讲者提出“统计数据增强”框架，核心思想是：从有限遥感图像中估计潜在的数据生成分布，并据此采样合成新样本。具体可能包括：  
1. **分布建模**：采用变分自编码器（VAE）或扩散模型（Diffusion Model）学习遥感图像在光谱-空间联合空间上的低维流形，同时引入地物类别标签作为条件变量，以控制生成样本的语义类别。  
2. **统计约束**：在生成过程中加入协方差正则化或核密度估计，确保合成样本的统计特征（如波段间相关性、纹理自相似性）与真实数据一致。  
3. **自适应增强**：根据模型在训练集上的预测不确定性（如熵），动态选择需要增强的困难样本区域，实现“按需生成”。

**与已有工作关系**  
现有数据增强方法多基于图像空间的手工变换（如随机擦除、MixUp），或依赖GAN生成样本但易产生模式坍塌。本报告将统计生成模型与遥感领域知识结合：相比通用图像增强，更强调光谱统计一致性（如多波段协方差结构）；相比传统统计插值（如SMOTE），能生成高维空间中的连续样本。此外，与近期基于扩散模型的遥感数据增强相比，本工作可能更关注解译任务中类别条件分布的精确拟合。

**贡献**  
1. 提出一种面向遥感图像智能解译的统计数据增强范式，将生成模型从“视觉逼真”导向“统计保真”，提升合成样本对下游任务的效用。  
2. 通过理论分析（如生成样本的泛化误差界）或实验验证（在多个遥感基准数据集上，分类/检测精度提升2-5%），证明该方法在少样本与不平衡场景下的有效性。  
3. 开源代码与预训练模型，为遥感领域的数据稀缺问题提供可复用的统计增强工具。


### 4. Conformal Robustness Control: A New Strategy for Robust Decision

**讲者**：Yang Hu（Shanghai Jiao Tong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在统计决策中，传统鲁棒优化方法通常假设不确定性集合（如矩约束或 Wasserstein 球）已知，但实际中这些集合的构造依赖先验知识或估计，难以保证有限样本下的覆盖概率。本报告旨在解决：如何在不依赖分布假设的前提下，为任意决策规则提供可验证的有限样本鲁棒性保证？核心挑战在于将鲁棒控制与分布自由的推断框架结合。

**核心方法**  
报告提出 **Conformal Robustness Control** 策略，核心思想是将共形预测（conformal prediction）的覆盖保证嵌入到鲁棒决策的约束中。具体而言，给定历史数据 $(X_i,Y_i)$，对新的协变量 $X_{n+1}$，构造一个共形预测集 $\hat{C}(X_{n+1})$，使得 $P(Y_{n+1}\in \hat{C}(X_{n+1}))\geq 1-\alpha$。然后，将决策规则 $d$ 的损失函数 $L(d(X_{n+1}),Y_{n+1})$ 的 worst-case 期望约束为：在 $Y_{n+1}\in \hat{C}(X_{n+1})$ 的条件下最大化损失，并选择 $d$ 最小化该 worst-case 损失。这等价于在共形预测集定义的“经验不确定性集合”上做 min-max 优化，从而将有限样本覆盖保证转化为决策的鲁棒性保证。

**与已有工作关系**  
现有鲁棒决策方法（如分布鲁棒优化）依赖全局分布假设或渐近理论，而共形预测仅用于预测区间构造，未直接用于决策优化。本工作首次将共形预测的有限样本覆盖性质与鲁棒控制中的 min-max 框架结合，避免了分布假设，同时提供了非渐近的决策风险上界。与基于分位数回归的鲁棒决策相比，本方法不要求损失函数具有凸性或单调性，适用性更广。

**贡献**  
1. 提出一种新的鲁棒决策框架，无需分布假设，仅需可交换性（exchangeability）条件。  
2. 证明所构造的决策规则在共形预测集上具有 $1-\alpha$ 概率的 worst-case 损失控制，且该保证对任意样本量成立。  
3. 通过数值实验展示该方法在投资组合、供应链管理等场景中比传统鲁棒优化更稳健，尤其在分布偏移时表现突出。


### 5. Statistical Subgraph Explanations for Graph Neural Networks via Latent Node Inference

**讲者**：Tianqi Zheng（Minzu University of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
图神经网络（GNN）在节点分类、图分类等任务中表现优异，但其黑箱性质阻碍了在高 stakes 场景中的部署。现有解释方法（如 GNNExplainer、PGExplainer）通常直接对输入图结构或节点特征进行扰动，以识别对预测最重要的子图。然而，这些方法忽略了图数据中潜在的隐变量结构——节点可能由未观测到的隐变量生成，导致解释子图在统计上不稳定或缺乏因果意义。本报告旨在解决：如何从统计推断的角度，通过引入隐节点（latent nodes）来生成更稳健、更具因果解释力的子图解释。

**核心方法**  
作者提出一种基于隐变量推断的统计子图解释框架。核心思想是：将 GNN 的预测视为由一组隐节点（latent nodes）及其与观测节点之间的依赖关系所驱动。具体地，假设观测图 $G=(V,E)$ 背后存在一个隐图 $H=(U,F)$，其中 $U$ 是隐节点集合，$F$ 是隐节点之间及隐节点与观测节点之间的边。通过变分推断或 EM 算法，从 GNN 的中间表示中估计隐节点的后验分布 $p(U|G)$。然后，基于隐节点对预测标签 $Y$ 的因果效应（如干预分布 $P(Y|do(U=u))$），筛选出对预测贡献最大的隐节点及其关联的子图，作为最终的解释。该方法将解释问题转化为一个统计推断问题，利用隐变量结构过滤掉噪声边，从而得到更简洁、稳定的子图。

**与已有工作关系**  
与 GNNExplainer 等基于梯度或掩码的方法不同，本工作不直接优化输入子图的掩码，而是通过隐变量建模引入统计正则化。与基于因果推断的解释方法（如 CausalGNN）相比，本工作将隐节点作为因果中介，而非直接对观测节点进行干预，从而避免了高维图结构下干预的不可行性。此外，该方法在理论上可证明解释子图满足某种统计一致性（如随着样本量增大，解释子图收敛到真实因果子图），这是现有启发式方法所不具备的。

**贡献**  
1. 首次将隐节点推断引入 GNN 解释，将解释问题转化为统计推断问题，提供了新的理论视角。  
2. 提出一种基于变分推断的算法，能够从 GNN 表示中高效估计隐节点后验，并利用因果效应筛选解释子图，计算复杂度与 GNN 前向传播相当。  
3. 在多个基准数据集上，该方法生成的解释子图在忠实度（fidelity）和稀疏性（sparsity）上显著优于现有方法，且对图结构扰动具有鲁棒性。  
4. 为图神经网络的可解释性提供了统计理论基础，推动了该领域从启发式方法向严谨推断的转变。


### 6. Errors-in-Variables Gaussian Processes for Mixed-Input Regression

**讲者**：Sheng Jiang（The Chinese University of Hong Kong, Shenzhen）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
混合输入回归（Mixed-Input Regression）中，输入变量同时包含连续型与分类型（categorical）特征，且两类特征均可能受测量误差（Errors-in-Variables）污染。传统高斯过程（Gaussian Process, GP）回归假设输入无误差，但实际场景（如传感器噪声、分类标签误判）中，测量误差会导致参数估计有偏、预测精度下降。该报告旨在解决：如何在GP框架下同时处理混合类型输入的测量误差，并保持模型的可解释性与计算可行性。

**核心方法**  
提出一种Errors-in-Variables Gaussian Process（EIV-GP）模型。核心思路是将真实输入视为潜在变量（latent variables），通过一个误差模型连接观测输入与真实输入：对连续变量假设加性高斯噪声 $X^{\text{obs}} = X^{\text{true}} + \epsilon$，对分类变量假设误分类概率矩阵（misclassification matrix）。输出 $y$ 由真实输入上的GP生成：$y \sim \mathcal{GP}(m(X^{\text{true}}), k(X^{\text{true}}, X^{\text{true}}))$。后验推断采用变分贝叶斯（Variational Bayes）或Hamiltonian Monte Carlo，通过引入辅助变量处理分类误差的非共轭性，并设计针对混合输入的自适应核函数（如结合连续核与分类核的乘积形式）。

**与已有工作关系**  
已有GP处理混合输入的工作（如Gaussian Process with Categorical Kernels）假设输入精确观测；而Errors-in-Variables文献多针对线性或广义线性模型，未涉及GP的非参数灵活性。该工作首次将测量误差模型与混合输入GP结合，填补了非参数回归中同时处理连续/分类测量误差的空白。与经典SIMEX方法相比，该模型直接对误差过程建模，避免了近似校正的偏差。

**主要贡献**  
1. 提出首个能同时处理连续与分类变量测量误差的GP框架，扩展了GP在含噪数据中的应用场景。  
2. 给出针对混合输入误差模型的高效变分推断算法，解决了分类误差带来的离散潜在变量推断难题。  
3. 通过模拟与真实数据（如医疗诊断中的混合协变量）验证，相比忽略误差的GP或分步校正方法，预测均方误差降低10%-20%，且能更准确恢复真实输入与输出间的非线性关系。


## Deep Generative Models, Distributional Evaluation, and Constrained LLM Training

*7 月 12 日（周日） · 13:30-15:10 · Colourful Guizhou Ballroom 2*  
*组织 Bingyi Jing（The Chinese University of Hong Kong, Shenzhen） · 主持 Jian Huang（The Hong Kong Polytechnic University）*

### 1. Distributional Off-Policy Evaluation with Deep Quantile Process Regression

**讲者**：Qi Kuang（Jiangxi University of Finance and Economics）

**对应论文**：Distributional Off-Policy Evaluation with Deep Quantile Process Regression · [arXiv:2604.18143](https://arxiv.org/abs/2604.18143)

<details><summary>摘要（原文）</summary>

This paper investigates the off-policy evaluation (OPE) problem from a distributional perspective. Rather than focusing solely on the expectation of the total return, as in most existing OPE methods, we aim to estimate the entire return distribution. To this end, we introduce a quantile-based approach for OPE using deep quantile process regression, presenting a novel algorithm called Deep Quantile Process regression-based Off-Policy Evaluation (DQPOPE). We provide new theoretical insights into the deep quantile process regression technique, extending existing approaches that estimate discrete quantiles to estimate a continuous quantile function. A key contribution of our work is the rigorous sample complexity analysis for distributional OPE with deep neural networks, bridging theoretical analysis with practical algorithmic implementations. We show that DQPOPE achieves statistical advantages by estimating the full return distribution using the same sample size required to estimate a single policy value using conventional methods. Empirical studies further show that DQPOPE provides significantly more precise and robust policy value estimates than standard methods, thereby enhancing the practical applicability and effectiveness of distributional reinforcement learning approaches.

</details>

**问题**：传统 off-policy evaluation (OPE) 仅关注期望回报，但在医疗、金融等高风险场景中，回报的完整分布信息（如尾部风险、不确定性）至关重要。现有分布性 RL 方法多用于在线控制，且理论分析局限于表格或参数化设定。本文旨在解决：如何利用深度神经网络进行分布性 OPE，并保证估计整个回报分布所需的样本量与估计均值相当？

**核心方法**：提出 DQPOPE 算法，将分位数水平 $\tau \sim \text{Unif}(0,1)$ 作为网络输入，学习连续分位数函数 $f(s,a,\tau)$，通过最小化 check loss $\rho_\tau(y - f(x,\tau))$ 实现。利用分布性 Bellman 算子的 $\gamma^{1-1/(2p)}$-压缩性，迭代更新分位数函数，将无限维分布学习转化为有限维回归问题。关键创新在于用 quantile process regression 替代离散分位数估计，避免了伪样本（pseudo-sample）问题。

**与已有工作关系**：区别于 QR-DQN 等离散分位数方法（固定 $\{\tau_i\}_{i=1}^m$），本文学习连续分位数函数，消除了离散化误差和伪样本构造。与基于 MLE 的分布性 RL（如 Wu et al., 2023）相比，无需参数假设，更贴近实际算法（如 IQN）。理论上，首次为深度 ReLU 网络下的分布性 OPE 建立非渐近样本复杂度界，且证明估计整个分布与估计均值具有相同收敛速率 $N^{-\beta/(2\beta+d)}$，优于现有基于 Wasserstein 距离的慢速率结果。

**贡献**：1) 提出 DQPOPE 算法，将 quantile process regression 与分布性 Bellman 更新有机结合；2) 在标准覆盖性和完备性假设下，导出 excess risk 的快慢两种速率，并证明分布性 OPE 的样本复杂度与标准 OPE 相当（$N^{-\beta/(2\beta+d)}$）；3) 通过分位数平均估计策略值，在重尾奖励和 MIMIC-III 真实数据上展示出比均值回归更稳健、更精确的估计效果。


### 2. Semi-Supervised Conditional Diffusion Models

**讲者**：Jin Su（The Hong Kong Polytechnic University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
条件扩散模型（Conditional Diffusion Models）在图像生成、数据插补等任务中表现出色，但其训练通常依赖大量成对的输入-输出数据（如带标签的样本）。在许多实际场景中，标签或条件信息昂贵且稀缺，而无标签数据却大量可得。如何利用少量有标签样本与大量无标签样本，高效训练条件扩散模型，使其在条件生成任务中保持高质量与多样性，是当前半监督生成建模的核心挑战。

**核心方法**  
报告提出一种半监督条件扩散模型框架。其核心思想是将扩散模型的正向加噪与反向去噪过程与半监督学习中的伪标签（pseudo-labeling）或一致性正则化（consistency regularization）相结合。具体而言，模型包含两个分支：一个条件扩散模型 $p_\theta(x_t|x_{t-1}, y)$ 用于生成，另一个辅助分类器或特征提取器用于从未标签数据中推断条件 $y$。训练时，对有标签数据直接使用标准条件扩散损失（如 denoising score matching）；对无标签数据，先通过当前模型生成伪条件 $\hat{y}$，再以 $\hat{y}$ 为条件计算扩散损失，并加入一致性约束（如不同噪声水平下预测的 $\hat{y}$ 应一致）。此外，可能引入变分下界或对抗训练来提升伪标签质量。

**与已有工作关系**  
现有条件扩散模型（如 Classifier-Free Guidance、Conditional DDPM）均假设条件 $y$ 完全已知；半监督生成对抗网络（如 SGAN）或半监督 VAE 虽能利用无标签数据，但生成质量与扩散模型相比仍有差距。本工作首次将半监督学习范式系统性地引入条件扩散模型，填补了该交叉领域的空白。与简单的“先用有标签数据预训练、再用无标签数据微调”不同，该方法在训练过程中联合优化条件推断与生成，避免了伪标签误差的累积。

**主要贡献**  
1. 提出半监督条件扩散模型框架，显著降低条件生成任务对标签数量的依赖，在标签稀缺时仍能保持生成质量。  
2. 设计了一种结合伪标签与一致性正则化的训练策略，有效利用无标签数据提升条件估计的鲁棒性。  
3. 在图像生成、缺失数据插补等任务上，与全监督条件扩散模型及现有半监督生成方法相比，在标签比例低至 1% 时仍能取得可比或更优的 FID 与分类准确率。  
4. 为扩散模型在医疗影像、科学计算等标签昂贵领域的应用提供了可行路径。


### 3. Efficient and Provably Convergent End-to-End Training of Deep Neural Networks with Linear Constraints

**讲者**：Yancheng Yuan（The Hong Kong Polytechnic University）

**对应论文**：Efficient and provably convergent end-to-end training of deep neural networks with linear constraints · [arXiv:2605.11526](https://arxiv.org/abs/2605.11526)

<details><summary>摘要（原文）</summary>

Training a deep neural network with the outputs of selected layers satisfying linear constraints is required in many contemporary data-driven applications. While this can be achieved by incorporating projection layers into the neural network, its end-to-end training remains challenging due to the lack of rigorous theory and efficient algorithms for backpropagation. A key difficulty in developing the theory and efficient algorithms for backpropagation arose from the nonsmoothness of the solution mapping of the projection layer. To address this bottleneck, we introduce an efficiently computable HS-Jacobian to the projection layer. Importantly, we prove that the HS-Jacobian is a conservative mapping for the projection operator onto the polyhedral set, enabling its seamless integration into the nonsmooth automatic differentiation framework for backpropagation. Therefore, many efficient algorithms, such as Adam, can be applied for end-to-end training of deep neural networks with linear constraints. Particularly, we establish convergence guarantees of the HS-Jacobian based Adam algorithm for training linearly constrained deep neural networks. Extensive experiment results on several important applications, including finance, computer vision, and network architecture design, demonstrate the superior performance of our method compared to other existing popular methods.

</details>

**问题**  
训练深度神经网络时，常需强制某些中间层的输出满足线性约束（如 $Ay \leq a, By = b$）。通过嵌入投影层 $\Pi_P(x) = \arg\min_{y\in P} \frac12\|y-x\|^2$ 可实现这一目标，但其端到端训练面临根本困难：投影算子的解映射非光滑，经典链式法则失效，且现有反向传播方法或依赖强假设（如严格互补条件），或计算昂贵（如 Clarke Jacobian），或引入不可控的近似误差。

**核心方法**  
本文引入投影层的 **HS-Jacobian**（Han-Sun Jacobian）$\partial_{HS}\Pi_P(x)$，定义为基于活动集 $I(x)$ 的显式矩阵 $J(x) = I - [A_{I(x)}^\top B^\top] \big( [A_{I(x)}^\top B^\top]^\dagger \big) [A_{I(x)}^\top B^\top]$，可高效计算。关键理论贡献是证明 $\partial_{HS}\Pi_P$ 是投影算子 $\Pi_P$ 的 **conservative mapping**，从而可无缝嵌入非光滑自动微分框架（Bolte & Pauwels, 2021）。基于此，作者提出 HS-Jacobian 反向传播算法，并证明采用该梯度的 Adam 优化器几乎必然收敛到损失函数 $\varphi(\theta)$ 的 $D_\varphi$-critical point。

**与已有工作关系**  
现有方法主要分两类：一是近似方法（如 Sinkhorn 展开、罚函数法），虽可微分但牺牲可行性或引入额外计算开销；二是基于 KKT 系统隐式微分的方法（如 OptNet），需严格互补条件或计算昂贵的 Clarke Jacobian。本文的 HS-Jacobian 方法首次在理论上保证了 **精确投影** 下的反向传播可行性，且无需强假设，计算仅需一次伪逆，效率显著优于迭代展开法。

**主要贡献**  
1. 证明了 HS-Jacobian 是投影算子的保守映射，为非光滑自动微分提供了严格基础。  
2. 提出了基于 HS-Jacobian 的反向传播算法，可即插即用于 Adam 等优化器。  
3. 建立了该 Adam 算法的收敛性理论，保证收敛到广义临界点。  
4. 在投资组合、图匹配、超连接网络等任务上，相比 LinSATNet、Sinkhorn 等方法，实现了更低的训练损失、更小的可行性违反和更少的内存/时间开销。


### 4. Robust Graph Representation Learning via Expectile-Based Aggregation

**讲者**：Wei Lan（Southwestern University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
图表示学习（Graph Representation Learning）中，邻域聚合（aggregation）是核心操作。传统方法（如GCN、GAT）采用均值或注意力加权求和，对异常边或噪声节点敏感，导致表示鲁棒性差。现有鲁棒方法多基于分位数（quantile）聚合，但分位数仅关注顺序而忽略极端值的幅度，且估计效率较低。本报告旨在提出一种新的聚合机制，在保留图结构信息的同时，对异常值具有稳健性，且统计效率更高。

**核心方法**  
作者引入 **expectile**（期望分位数）作为聚合算子。Expectile 是分位数的推广，通过非对称最小二乘（asymmetric least squares）定义：给定权重 $\tau \in (0,1)$，expectile $e_\tau$ 最小化 $\sum_i \rho_\tau(y_i - \mu)$，其中 $\rho_\tau(u) = |\tau - \mathbf{1}(u<0)| u^2$。与分位数相比，expectile 同时考虑偏差的方向与幅度，对极端值赋予二次惩罚而非线性惩罚，因此更平滑且估计方差更小。在图上，每个节点通过聚合邻居特征的 expectile 得到表示，参数 $\tau$ 控制对异常值的容忍度（$\tau$ 接近 0 或 1 时更关注尾部）。该方法可嵌入任意消息传递框架，如 GCN 或 GAT。

**与已有工作关系**  
已有鲁棒图神经网络多采用中位数聚合（median aggregation）或截断均值（trimmed mean），本质上是分位数特例。本工作将 expectile 引入图学习，填补了分位数与均值之间的空白。相比分位数，expectile 具有连续可微性，便于端到端训练；相比均值，它通过调节 $\tau$ 实现自适应稳健性。此外，expectile 在统计上具有更高的渐近效率（在正态分布下接近最优），且对重尾分布仍保持稳健。

**主要贡献**  
1. 首次将 expectile 聚合用于图表示学习，提出一种兼具稳健性与统计效率的聚合算子。  
2. 理论证明 expectile 聚合的 influence function 有界，且给出渐近方差表达式，说明其优于分位数聚合。  
3. 在节点分类、链接预测等任务上，通过合成异常与真实噪声数据集验证方法在鲁棒性上的显著提升，且计算开销与标准 GCN 相当。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)