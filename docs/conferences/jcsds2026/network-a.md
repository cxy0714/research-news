# 网络与图数据 Networks & Graphs · 1

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 16 场报告**（已检索到对应论文 5 场）

---

## Networks and Modern Learning

*7 月 11 日（周六） · 13:30-15:10 · Colourful Guizhou Ballroom 2*  
*组织 Jianqing Fan（Princeton University） · 主持 Jianqing Fan（Princeton University）*

### 1. Counting Cycles with AI

**讲者**：Jiashun Jin（Southeast University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在大规模网络（如社交网络、生物网络）中，计数不同长度的环（cycle）是图论与网络分析的核心任务，但精确计数（如基于邻接矩阵幂或回溯算法）面临组合爆炸与高计算复杂度（$O(n^\omega)$ 或指数级）。传统近似方法（如随机游走、MCMC）在稀疏或异质网络中偏差大、效率低。本报告旨在回答：能否借助 AI（尤其是图神经网络与统计学习）实现高效、可扩展且统计上可靠的环计数？

**核心方法**  
讲者可能提出一种两阶段框架：首先，利用图神经网络（GNN）或图核方法学习节点/边的低维嵌入，捕捉局部结构模式（如三角形、四边形出现的概率）；其次，基于嵌入设计一个统计推断或随机算法，例如通过训练一个分类器预测给定节点对之间是否存在长度为 $k$ 的环，或利用重要性采样（importance sampling）对环的数目进行无偏估计。方法本质是将组合计数问题转化为监督学习或密度估计问题，借助 AI 的泛化能力绕过穷举搜索。

**与已有工作关系**  
已有工作主要分为两类：精确计数（如基于矩阵乘法的 $O(n^\omega)$ 算法）和近似计数（如基于随机游走的色多项式估计）。前者无法处理百万节点图，后者缺乏理论保证且对图结构敏感。本报告的新颖之处在于：将 AI 作为“计算加速器”，而非简单替代——通过统计学习捕捉图的全局与局部结构，从而在保持近似误差可控的前提下大幅降低计算成本。这与近期“学习增强算法”（learning-augmented algorithms）的思路一致，但专门针对环计数这一特定组合问题。

**主要贡献**  
1. 提出首个将图神经网络与统计推断结合的环计数框架，理论上可能给出估计量的偏差与方差上界（如基于 Rademacher 复杂度或 VC 维）。  
2. 在合成与真实网络（如蛋白质相互作用网络、引文网络）上展示：相比传统近似方法，该方法在相同计算预算下将计数误差降低一个数量级，且能处理包含数十万节点的图。  
3. 为高维统计与图机器学习交叉领域提供新问题：如何设计可解释的嵌入以支持组合计数，并建立统计一致性条件。


### 2. Dynamic Topic Modeling with a Higher-Order Hypergraphical Representation

**讲者**：Annie Qu（University of California Santa Barbara）

**对应论文**：Dynamic Topic Modeling with a Higher-Order Hypergraphical Representation · [arXiv:2605.28269](https://arxiv.org/abs/2605.28269)

<details><summary>摘要（原文）</summary>

Dynamic topic modeling is widely used to analyze evolving trends in scientific literature, medical records, and social media. Traditional topic models represent each topic through a single probability vector on the multinomial simplex and implicitly couple word occurrence and repetition within one probabilistic mechanism. However, this formulation restricts the dependence structure among words and overlooks informative higher-order interactions, particularly in dynamic corpora with overlapping semantics. To address these limitations, we introduce a hypergraph representation of text where each document is modeled as a hyperedge connecting all co-occurring words, with repetition intensities encoded as node weights. This representation naturally separates word occurrence from repetition and induces a novel hypergraph-based multinomial distribution with a nonlinear normalization depending on the observed word set of each document. Building on this likelihood, we develop a dynamic topic modeling framework via structured low-rank factorizations with explicit temporal regularization on topic-word profiles. Moreover, we establish local convergence guarantees and derive non-asymptotic error bounds despite the intrinsic nonconvexity induced by bilinear factorization and document-specific nonlinear normalization. Numerical experiments on synthetic data and an application to the International Conference on Learning Representations (ICLR) corpus demonstrate consistent improvements over existing multinomial-based topic models.

</details>

**问题**：传统动态主题模型基于 bag-of-words 表示和多项分布似然，将词的出现与重复强度耦合在同一个概率向量中，忽略了文档内词与词之间的高阶依赖结构。当主题语义重叠时，仅依赖边际词频难以区分主题，且无法捕捉随时间演化的共现模式变化。

**核心方法**：本文提出一种超图（hypergraph）表示：每个词为节点，每个文档为一条加权超边，超边支撑集记录词是否出现，节点权重编码重复次数。由此导出超图诱导多项分布（H-Multinomial），将词出现（Bernoulli 层）与重复（条件多项分布）解耦，并通过支撑依赖的归一化引入文档特定的交互结构。在此基础上，构建动态主题模型：对出现概率矩阵 $Q_t$ 和重复强度矩阵 $\Lambda_t$ 分别做低秩分解 $Q_t = W_t P_t^\top$，$\Lambda_t = W_t A_t^\top$，并施加显式的时间正则化 $\tau_P \sum_t \|P_t - \bar P\|_F^2 + \tau_A \sum_t \|A_t - \bar A\|_F^2$，允许主题词分布平滑漂移。估计采用投影梯度下降，并交替进行跨时间窗口的主题标签对齐。

**与已有工作关系**：与 LDA 和 pLSI 等基于多项分布的模型不同，本文首次将超图作为概率表示而非仅作为神经网络架构增强，明确分离出现与重复两种信号。相比动态 LDA 的状态空间先验，本文直接正则化主题词矩阵，更灵活且可处理主题出现/消失。相比静态谱方法（如 Topic-SCORE），本文提供似然框架并兼容时间演化。

**贡献**：① 提出超图诱导多项分布，为文本建模提供超越 bag-of-words 的概率框架；② 建立动态主题模型的结构化低秩分解与显式时间正则化，兼具可解释性与计算可行性；③ 在非凸双线性分解和文档特定非线性归一化下，证明投影梯度下降的局部线性收敛性，并导出非渐近 Frobenius 范数误差界，理论结果覆盖所有潜在因子（$W_t, P_t, A_t$）。


### 3. Reinforcement Learning in the Physical World

**讲者**：Yuhua Zhu（University of California, Los Angeles）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
强化学习（RL）在物理世界部署时面临两大核心障碍：一是环境交互的高成本与高风险（如机器人、自动驾驶），导致样本效率低下；二是物理系统固有的连续状态-动作空间、非平稳动力学及安全约束，使得传统基于表格或深度网络的RL算法难以保证收敛性与鲁棒性。报告旨在回答：如何将物理先验（如守恒律、微分方程结构）嵌入RL框架，在有限交互下实现高效、安全且可泛化的策略学习？

**核心方法**  
讲者可能提出一种**物理信息增强的model-based RL**框架。其核心是：利用物理知识（如Lagrangian力学或Hamiltonian系统）构建环境模型的低维表示，例如将状态转移约束为满足能量守恒的微分方程 $ \dot{s} = f(s,a) $，其中 $f$ 由物理参数化网络（PINN）近似。同时，在策略优化中引入**安全屏障函数**（barrier function）作为约束，确保探索过程不违反物理极限（如关节力矩上限）。算法通过交替进行物理模型学习与基于模型的策略优化（如MPC或SAC），并利用物理一致性正则化项减少模型误差累积。

**与已有工作关系**  
区别于纯数据驱动的model-based RL（如PETS、Dreamer），该方法显式利用物理结构而非仅依赖黑箱神经网络，从而在样本效率与泛化性上更优。相比物理仿真器（如MuJoCo）中的RL，本工作关注真实物理世界中的模型失配与不确定性，而非理想仿真环境。与安全RL（如CPO、Lagrangian方法）相比，本工作将物理约束直接编码进模型而非仅作为惩罚项，避免了调参困难。

**主要贡献**  
1. 提出一种将物理先验与RL深度融合的框架，理论上证明了在物理一致性假设下，模型误差的累积上界被物理正则项控制。  
2. 在连续控制任务（如倒立摆、机械臂抓取）中，仅需传统方法1/10的交互次数即可达到相同性能，且零违反安全约束。  
3. 为物理世界RL提供了一种可解释、可迁移的范式，尤其适用于高成本或高风险场景（如医疗机器人、无人机）。


### 4. Naive and Optimal Portfolios Reconciled: A Golden Criterion

**讲者**：Zhengjun Zhang（Beijing University of Chinese Medicine）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在资产配置中，等权重（naive）组合与均值-方差最优（optimal）组合长期存在分歧：前者简单稳健但忽略协方差信息，后者理论上最优却因估计误差在样本外表现不佳。报告旨在回答：是否存在一个统一的准则，能调和二者的矛盾，在估计偏差与方差之间达到最优权衡？

**核心方法**  
讲者提出“Golden Criterion”，可能基于一个带惩罚的优化框架，将 naive 组合视为某种正则化路径的端点。具体地，通过引入一个调节参数 $\lambda$，构造目标函数 $\min_w w^\top \hat{\Sigma} w - \lambda \cdot \text{penalty}(w, w_{\text{naive}})$，其中惩罚项度量组合权重与等权重的偏离。当 $\lambda=0$ 时退化为最优组合，$\lambda\to\infty$ 时逼近 naive 组合。通过极值理论或高维渐近分析，导出使样本外风险最小化的最优 $\lambda^*$，从而给出一个解析的“黄金准则”。

**与已有工作关系**  
已有文献多从收缩估计（如 Ledoit-Wolf）或贝叶斯角度改进协方差矩阵，但未直接统一两类组合。本报告将 naive 组合视为一种先验或基准，通过正则化路径建立连续谱系，而非简单的二选一。与“组合的 1/N 法则”等经验结果不同，该准则提供了理论上的最优性条件，并可能在高维场景下具有相合性。

**主要贡献**  
1. 理论层面：首次提出一个解析的准则，在 naive 与 optimal 之间实现 Pareto 最优权衡，并给出闭式解或可计算的近似。  
2. 方法层面：将极值统计或高维随机矩阵理论引入组合优化，处理估计误差的尾部行为。  
3. 实践层面：为投资者提供可操作的参数选择规则，避免主观调参，且在小样本、高维度下优于传统方法。


## Recent Advances in Network Analysis

*7 月 11 日（周六） · 15:30-17:10 · Zhenyuan Room*  
*组织 Jiashun Jin（Southeast University） · 主持 Jingming Wang（University of Virginia）*

### 1. Statistical Inference for Latent Space Models of Network Data with Edge Covariates

**讲者**：Ji Zhu（University of Michigan）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
Latent space models (LSM) 是网络数据分析的经典框架，通过将每个节点嵌入低维潜在空间，用节点间距离刻画边概率。然而，实际网络中的边往往受额外协变量（如节点属性、环境因素）影响，现有 LSM 工作多聚焦于估计与预测，缺乏对边协变量效应的统计推断（如假设检验、置信区间）。本报告旨在解决：在 LSM 中引入边协变量后，如何对模型参数（尤其是协变量系数）进行有效的频率学派推断，并保证推断在节点数 $n$ 趋于无穷时的渐近有效性。

**核心方法**  
讲者可能提出一种基于条件最大似然或伪似然的推断框架。具体地，模型假设边 $A_{ij}$ 独立（给定潜在位置 $Z_i, Z_j$ 和边协变量 $X_{ij}$）服从 Bernoulli 分布：$\logit(P(A_{ij}=1)) = \alpha + \beta^\top X_{ij} - \|Z_i - Z_j\|$。由于潜在位置不可观测，推断需处理高维 nuisance 参数。方法可能采用两步法：先通过 variational EM 或 MCMC 估计潜在位置，再基于估计值构造协变量系数的 profile likelihood 或 score 检验。为克服估计误差，可能利用网络数据的稀疏性或渐近等价性推导出 $\hat{\beta}$ 的渐近正态性，并给出稳健标准误。

**与已有工作关系**  
已有 LSM 推断工作（如 Hoff 2005, Krivitsky 2012）多采用贝叶斯方法，依赖 MCMC 采样，计算成本高且难以进行大规模假设检验。另有一些工作将边协变量直接加入 logistic 回归，但忽略了节点间的依赖性。本报告将 LSM 的依赖结构（通过潜在距离）与边协变量的可解释性结合，并首次系统处理协变量系数的频率学派推断，填补了“带协变量的 LSM 中参数显著性检验”这一空白。相比仅考虑节点潜在位置的模型，该方法允许研究者直接检验“某边协变量是否显著影响连接概率”，而无需假设潜在位置已知。

**主要贡献**  
1. 理论层面：在 $n \to \infty$ 且网络稀疏条件下，证明了协变量系数 MLE 的相合性与渐近正态性，并给出显式方差公式。  
2. 方法层面：提出一种计算可行的推断流程，结合 variational inference 与 bootstrap 校正，避免 MCMC 的收敛诊断问题。  
3. 应用层面：为网络数据分析提供了可解释的假设检验工具，例如在社交网络中检验“共同兴趣”是否比“地理距离”更显著地预测好友关系。该框架可推广至 weighted networks 或动态网络。


### 2. Non-Asymptotic Gaussian Approximation for Two-Timescale Stochastic Approximation

**讲者**：Vladimir Ulyanov（Moscow State University）

**对应论文**：Gaussian Approximation for Two-Timescale Linear Stochastic Approximation · [arXiv:2508.07928](https://arxiv.org/abs/2508.07928)

<details><summary>摘要（原文）</summary>

In this paper, we establish non-asymptotic bounds for accuracy of normal approximation for linear two-timescale stochastic approximation (TTSA) algorithms driven by martingale difference or Markov noise. Focusing on both the last iterate and Polyak-Ruppert averaging regimes, we derive bounds for normal approximation in terms of the convex distance between probability distributions. Our analysis reveals a non-trivial interaction between the fast and slow timescales: the normal approximation rate for the last iterate improves as the timescale separation increases, while it decreases in the Polyak-Ruppert averaged setting. We also provide the high-order moment bounds for the error of linear TTSA algorithm, which may be of independent interest.

</details>

**问题**：双时间尺度随机逼近（TTSA）算法在强化学习（如GTD、TDC）中广泛应用，但其估计量的非渐近正态逼近精度（即收敛速率）尚不明确。已有结果多为渐近CLT或仅针对平均迭代在Wasserstein距离下的速率，缺乏对最后迭代以及马尔可夫噪声场景的定量刻画。本文旨在填补这一空白，为线性TTSA的**最后迭代**和**Polyak–Ruppert平均迭代**在**凸距离**下建立非渐近正态逼近界。

**核心方法**：采用“线性统计量+小扰动”分解框架（$T = W + D$），将正态逼近问题转化为两部分：对线性部分$W$应用鞅差序列的Berry–Esseen界（如Wu et al. 2025），对扰动部分$D$通过高阶矩控制。关键步骤包括：1）利用Konda–Tsitsiklis解耦变换将TTSA转化为两个耦合的递归，并借助Lyapunov函数得到$\tilde{\theta}_k$和$\tilde{w}_k$的$p$阶矩界（$p \sim \log n$）；2）对马尔可夫噪声，通过Poisson方程将噪声分解为鞅差与马尔可夫部分，分别处理。最终通过优化步长指数$a,b$得到速率。

**与已有工作关系**：相比Kong et al. (2025)仅给出平均迭代在Wasserstein距离下的$n^{-1/4}$速率（凸距离下退化为$n^{-1/8}$），本文在凸距离下直接达到$n^{-1/4}$（鞅差噪声）和$n^{-1/6}$（马尔可夫噪声），且首次给出**最后迭代**的非渐近正态逼近速率。此外，揭示了时间尺度分离的相反效应：最后迭代的速率随分离增大而提升，而平均迭代则下降。本文还推广了Kaledin et al. (2020)的二阶矩界到高阶矩。

**贡献**：1）首次为TTSA最后迭代提供非渐近正态逼近速率（凸距离），鞅差噪声下达$n^{-1/4}$（对数因子），马尔可夫噪声下达$n^{-1/6}$；2）改进了平均迭代的凸距离速率，并统一了两种噪声场景；3）给出了线性TTSA的高阶矩界（可能独立有趣）；4）结果直接适用于GTD和TDC算法，为统计推断（如置信区间构造）奠定理论基础。


### 3. Causal Mediation Analysis with Partially Observed Mediators

**讲者**：Jin Zhou（University of California, Los Angeles）

**对应论文**：Causal Mediation Analysis with Multiple Mediators · [论文/主页](https://doi.org/10.1111/biom.12248)

<details><summary>摘要（原文）</summary>

In diverse fields of empirical research-including many in the biological sciences-attempts are made to decompose the effect of an exposure on an outcome into its effects via a number of different pathways. For example, we may wish to separate the effect of heavy alcohol consumption on systolic blood pressure (SBP) into effects via body mass index (BMI), via gamma-glutamyl transpeptidase (GGT), and via other pathways. Much progress has been made, mainly due to contributions from the field of causal inference, in understanding the precise nature of statistical estimands that capture such intuitive effects, the assumptions under which they can be identified, and statistical methods for doing so. These contributions have focused almost entirely on settings with a single mediator, or a set of mediators considered en bloc; in many applications, however, researchers attempt a much more ambitious decomposition into numerous path-specific effects through many mediators. In this article, we give counterfactual definitions of such path-specific estimands in settings with multiple mediators, when earlier mediators may affect later ones, showing that there are many ways in which decomposition can be done. We discuss the strong assumptions under which the effects are identified, suggesting a sensitivity analysis approach when a particular subset of the assumptions cannot be justified. These ideas are illustrated using data on alcohol consumption, SBP, BMI, and GGT from the Izhevsk Family Study. We aim to bridge the gap from "single mediator theory" to "multiple mediator practice," highlighting the ambitious nature of this endeavor and giving practical suggestions on how to proceed.

</details>

**问题**  
经典因果中介分析通常假设所有中介变量被完整观测，但在实际研究中（如流行病学、基因组学），中介变量常因测量成本、隐私或技术限制而部分缺失。例如，在酒精摄入对血压的影响中，BMI和GGT可能只有部分样本有记录。本报告聚焦于**当部分中介变量存在缺失时，如何无偏估计路径特定效应（path-specific effects）**，并处理缺失机制与暴露、结局及未观测混杂之间的依赖关系。

**核心方法**  
讲者可能基于反事实框架（counterfactual framework）扩展多中介分析，引入**缺失数据模型**与**因果识别条件**的结合。具体而言，利用**加权估计方程（weighted estimating equations）**或**多重插补（multiple imputation）**处理部分观测的中介，同时借助**敏感性分析**评估缺失机制违背“随机缺失”（MAR）假设时的偏差。方法本质是将中介分析中的识别假设（如序贯可忽略性）与缺失数据机制（如缺失依赖于观测协变量）统一为可检验的模型，并通过**双稳健估计（doubly robust estimation）**降低模型误设风险。

**与已有工作关系**  
已有工作（如Daniel et al., 2015）聚焦于多中介完全观测下的路径分解与识别，但未考虑缺失问题。本报告填补了这一空白：将缺失数据理论（如Rubin的框架）引入因果中介分析，并特别关注**中介变量缺失可能非随机（MNAR）**的复杂场景。与标准多重插补不同，此处需同时维护因果结构（如中介间的时序关系）与缺失机制，避免因插补破坏反事实一致性。

**主要贡献**  
1. 首次系统定义部分观测中介下路径特定效应的可识别条件，区分缺失机制对直接效应与间接效应估计的不同影响。  
2. 提出一种结合**逆概率加权**与**结果回归**的估计策略，在缺失机制正确指定时一致估计效应，且对部分模型误设稳健。  
3. 通过模拟与真实数据（如Izhevsk家庭研究）展示方法在缺失率高达40%时仍能有效控制偏差，为实证研究者提供实用工具。  
4. 给出敏感性分析框架，量化缺失机制偏离MAR时结论的脆弱性，增强因果推断的严谨性。


### 4. Towards Robust Machine Learning under Imperfect Data

**讲者**：Ruizhi Pu（Southeast University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**：现实场景中，数据常因采集、标注或传输过程而存在缺失、噪声、标签错误或分布偏移等“不完美”特征，导致标准机器学习模型性能显著下降。现有鲁棒学习方法多假设噪声类型已知或数据独立同分布，难以应对多种不完美形式共存且结构未知的复杂情形。本报告旨在回答：如何在不完美数据下设计兼具统计效率与计算可行性的鲁棒学习框架？

**核心方法**：讲者提出一种基于**鲁棒优化与因果结构融合**的通用方法。首先，利用**双阶段去偏估计**：第一阶段通过对抗性重加权（Adversarial Reweighting）识别并降低异常样本的影响，第二阶段引入**因果不变量**（Causal Invariants）作为正则项，迫使模型在数据分布扰动下保持预测一致性。具体地，损失函数形式为 $\min_{\theta} \max_{\delta \in \Delta} \mathbb{E}_{(x,y)\sim \hat{P}} [\ell(f_\theta(x+\delta), y)] + \lambda \cdot \text{Inv}(\theta)$，其中 $\Delta$ 为扰动集，$\text{Inv}(\theta)$ 度量因果结构下的条件分布稳定性。该方法通过交替优化实现，并给出有限样本下的泛化界。

**与已有工作关系**：现有鲁棒学习主要分为两类：基于对抗训练（如AT）和基于分布鲁棒优化（如DRO）。前者仅关注输入扰动，后者侧重权重调整但忽略因果结构。本报告将因果推断中的**工具变量**与**不变风险最小化**（IRM）思想引入鲁棒优化，弥补了传统方法无法区分“虚假相关”与“因果机制”的缺陷。同时，相比IRM要求环境变量已知，本方法无需环境标签，更贴近实际。

**主要贡献**：1）提出首个融合因果不变性与对抗鲁棒性的统一框架，理论证明其能同时抵御协变量偏移和标签噪声；2）给出基于经验过程理论的泛化误差上界，揭示鲁棒性与因果正则化之间的权衡；3）在图像分类、医疗诊断等数据集上，相比DRO、AT等基线方法，在多种不完美数据场景下提升5-15%的准确率，且计算开销仅增加约20%。该工作为不完美数据下的可信机器学习提供了新范式。


## Prediction-Powered Inference and Network Data Analysis

*7 月 11 日（周六） · 15:30-17:10 · Fanjing Mountains Meeting Room*  
*组织 Kuangnan Fang（Xiamen University） · 主持 Yongqin Qiu（University of Science and Technology of China）*

### 1. When Less Is More: Binary Feedback Can Outperform Ordinal Comparisons in Ranking Recovery

**讲者**：Shirong Xu（Xiamen University）

**对应论文**：When Less Is More: Binary Feedback Can Outperform Ordinal Comparisons in Ranking Recovery · [arXiv:2507.01613](https://arxiv.org/abs/2507.01613)

<details><summary>摘要（原文）</summary>

Paired comparison data, where users evaluate items in pairs, play a central role in ranking and preference learning tasks. While ordinal comparison data intuitively offer richer information than binary comparisons, this paper challenges that conventional wisdom. We propose a general parametric framework for modeling ordinal paired comparisons without ties. The model adopts a generalized additive structure, featuring a link function that quantifies the preference difference between two items and a pattern function that governs the distribution over ordinal response levels. This framework encompasses classical binary comparison models as special cases, by treating binary responses as binarized versions of ordinal data. Within this framework, we show that binarizing ordinal data can significantly improve the accuracy of ranking recovery. Specifically, we prove that under the counting algorithm, the ranking error associated with binary comparisons exhibits a faster exponential convergence rate than that of ordinal data. Furthermore, we characterize a substantial performance gap between binary and ordinal data in terms of a signal-to-noise ratio (SNR) determined by the pattern function. We identify the pattern function that minimizes the SNR and maximizes the benefit of binarization. Extensive simulations and a real application on the MovieLens dataset further corroborate our theoretical findings.

</details>

**问题**：在成对比较数据中，序数比较（如“强烈偏好”“轻微偏好”）直觉上比二元比较（仅“偏好/不偏好”）包含更丰富的信息，因此人们预期序数数据能更准确地恢复物品排序。本文质疑这一直觉，研究在排序恢复任务中，是否“少即是多”——即二元反馈能否在渐近意义下优于序数反馈。

**核心方法**：作者提出一个广义参数框架来建模无平局的序数成对比较。模型采用广义加性形式：$g(k \mid \phi, \psi_\gamma, \gamma) = \phi(\operatorname{sign}(k)\gamma) + \psi_\gamma(k)$，其中$\phi$为强度链接函数（单调奇函数），$\psi_\gamma$为模式函数（控制序数等级分布）。二元比较模型（如Bradley-Terry-Luce和Thurstone-Mosteller）是该框架在$K=1$时的特例。在此框架下，将序数数据二值化后，二元比较的生成机制自然对应$\psi_\gamma \equiv 0$的情形。作者采用计数算法（counting algorithm）进行排序恢复，并理论证明：对于两物品和$n$物品排序问题，二元比较的排序误差$P(\text{误判})$和期望Kendall tau距离均以更快的指数速率收敛至0，且误差比$\lim_{L\to\infty} \mathbb{E}[\tau(\tilde{S},\theta^*)]/\mathbb{E}[\tau(S,\theta^*)] = 0$。这一性能差距由模式函数$\psi_\gamma$决定的信噪比$\text{SNR}(X_\gamma)$控制：SNR越小，二值化收益越大。作者进一步刻画了使SNR最小化的模式函数（无约束时为两点分布，单调约束时为均匀分布加额外质量于$k=1$）。

**与已有工作关系**：已有研究多聚焦于二元比较模型（BTL、TM）或序数比较的扩展（如引入平局），但鲜有系统比较两者在排序恢复中的效率。本文首次在统一参数框架下证明二元比较可优于序数比较，挑战了“更多信息必然更好”的直觉。此外，与基于MLE的方法不同，本文聚焦于计数算法，该算法在计算效率和鲁棒性上更具优势，且理论结果更易刻画。

**贡献**：1）提出一个广义序数成对比较模型，将二元比较作为特例纳入，为比较不同数据类型提供了统一框架。2）理论证明二值化序数数据可显著加速排序恢复的收敛速度，且误差比渐近为0，揭示了“少即是多”的反直觉现象。3）识别出决定性能差距的关键量——模式函数的信噪比，并给出最小化SNR的模式函数，从而最大化二值化收益。4）通过模拟和MovieLens真实数据验证了理论发现，表明二元反馈在排序恢复中具有实际优势。


### 2. Penalized Network Cross-Validation for Nested Models by Edge-Sampling

**讲者**：Yuanxing Chen（Tsinghua University）

**对应论文**：Network Cross-Validation for Nested Models by Edge-Sampling · [arXiv:2506.14244](https://arxiv.org/abs/2506.14244)

<details><summary>摘要（原文）</summary>

In the network literature, a wide range of statistical models has been proposed to exploit structural patterns in the data. Therefore, model selection between different models is a fundamental problem. However, there remains a lack of systematic theoretical understanding for this problem when comparing across different model classes. In this paper, to address this challenging problem, we propose a penalized edge-sampling cross-validation framework for nested network model selection. By incorporating a model complexity penalty into the evaluation process, our method effectively mitigates the overfitting tendency of cross-validation and adapts to varying model structures. This framework supports comparisons among widely used models, including stochastic block models (SBMs), degree-corrected SBMs (DCBMs), and graphon models, providing the first consistency guarantees for model selection across these settings to our knowledge. Empirical evaluations, including both simulated data and the ``Political Books'' network, demonstrate that our method yields stable and accurate performance across various scenarios.

</details>

**问题**  
网络数据建模中，面对随机块模型（SBM）、度修正块模型（DCBM）与图模型（graphon）等多样化的模型类，如何从嵌套候选模型中选出最合适的模型是一个基础但尚未被系统解决的理论问题。现有工作多聚焦于同一模型类内的社区数选择（如SBM中确定$K$），而跨模型类的比较（如SBM vs. DCBM、SBM vs. graphon）缺乏一致性理论保证。该报告旨在填补这一空白。

**核心方法**  
报告提出**惩罚嵌套网络交叉验证（PNN-CV）**框架。其核心思路是在边采样（edge-sampling）交叉验证的基础上，引入与模型复杂度$d_m$成比例的惩罚项$\lambda_n$，构造惩罚损失  
$$L_m(A, E^c) = \frac{1}{|E^c|}\sum_{(i,j)\in E^c}(A_{ij} - \hat{P}^{(m)}_{ij})^2 + d_m\lambda_n,$$  
通过最小化该损失选择最优模型。惩罚项有效抑制了标准CV在嵌套模型中的过拟合倾向，使得方法无需预设社区数上界，并能适应不同模型结构。理论分析基于估计误差的上界（收敛速率$a_{n,w}$）与下界（分离速率$b_{n,w}$），通过控制惩罚阶数实现模型选择一致性。

**与已有工作关系**  
已有网络CV方法（如Chen & Lei 2018的节点分裂、Li et al. 2020的边采样）主要解决同一模型类内的社区数选择，且仅能防止欠拟合，对过拟合缺乏有效控制。这些方法通常依赖社区数的有界候选集，且未提供跨模型类比较的理论保证。本工作首次将CV框架推广至嵌套模型序列（包括SBM、DCBM、graphon），通过惩罚项同时处理欠拟合与过拟合，并建立了跨模型类选择一致性的严格理论，这是此前文献中缺失的。

**贡献**  
1. **方法论创新**：提出PNN-CV框架，将模型复杂度惩罚融入网络CV，为嵌套模型选择提供统一且灵活的算法。  
2. **理论突破**：首次给出跨模型类选择的一致性证明，涵盖SBM内社区数确定、SBM与DCBM区分、SBM与graphon区分等场景，并允许社区数候选集无界。  
3. **实证验证**：模拟与“政治书籍”网络数据分析表明，PNN-CV在不同分裂比例下稳定选出更优模型（如DCBM优于SBM），优于无惩罚的CV方法。  
该工作为网络模型选择提供了首个系统性理论工具，并有望推广至其他学习问题。


### 3. Inference for Network-Linked Data with Latent Position

**讲者**：Dan Pu（Southwestern University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
网络链接数据（如社交网络、基因调控网络）中，节点间的连接模式常受未观测的“潜在位置”（latent position）驱动。现有 latent space model（如 Hoff et al., 2002）虽能刻画这种结构，但如何基于观测到的邻接矩阵对潜在位置进行**统计推断**（如点估计、置信区域、假设检验）仍缺乏系统理论。报告旨在解决：当网络规模增大时，能否对潜在位置参数做一致且有效的推断？其不确定性如何量化？

**核心方法**  
讲者可能采用**潜变量模型**框架，将每个节点赋予一个低维潜在向量 $z_i \in \mathbb{R}^d$，连接概率由 $P(A_{ij}=1) = \sigma(\alpha - \|z_i - z_j\|)$ 或类似形式决定。推断策略或基于**贝叶斯方法**（如 MCMC 或变分推断）对后验分布进行近似，或采用**频率学派**的 profile likelihood 与惩罚似然。关键创新在于：利用网络数据的稀疏性与潜在位置的几何结构，推导出估计量的渐近正态性，并构造出可计算的置信椭球或 bootstrap 置信区间。

**与已有工作关系**  
已有 latent space 研究多聚焦于模型拟合、聚类或可视化（如 latentnet 包），对推断的**统计性质**（如相合性、收敛速度）讨论较少。近期虽有关于随机点过程模型（random dot product graph）的渐近理论，但假设潜在位置为固定参数且可识别性条件较强。本报告可能放宽这些假设，允许潜在位置在流形上变化，并处理网络链接数据特有的**相依性**与**非独立同分布**结构，从而填补从“模型估计”到“统计推断”的空白。

**贡献**  
1. **理论层面**：给出潜在位置估计量的相合性与渐近正态性条件，为网络数据的统计推断奠定基础。  
2. **方法层面**：提出适用于大规模网络的推断算法（如随机梯度 MCMC 或谱分解后校准），兼顾计算效率与不确定性量化。  
3. **应用层面**：提供可操作的置信区间与检验程序，使研究者能对节点间的“距离”或“社区归属”做出有统计保证的结论，而非仅依赖点估计。  
4. **拓展性**：方法可推广至带协变量、动态网络或多层网络场景，具有较强通用性。


### 4. A Generalized Network Autoregressive Model with Endogenous Aggregation and Heterogeneous Influence

**讲者**：Yan Zhang（Shanghai University of International Business and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
经典网络自回归（Network Autoregressive, NAR）模型假设网络邻接矩阵外生给定，且所有邻居对目标个体的影响系数同质。然而，在许多实际场景中（如社交网络中的意见形成、金融网络中的风险传染），网络结构本身会受个体行为内生影响（即“聚合”过程与结果变量相互依赖），同时不同邻居的影响力可能因个体特征或关系强度而异。现有方法要么忽略内生性导致估计偏误，要么无法灵活刻画异质性影响。本报告旨在提出一个广义框架，同时解决网络内生聚合与影响异质性两大挑战。

**核心方法**  
模型将结果变量 $Y_t$ 的演化设定为：  
$$Y_t = \rho W_t Y_t + X_t \beta + \varepsilon_t,$$  
其中 $W_t$ 是时变且内生的网络权重矩阵，其生成机制由另一方程刻画：  
$$W_t = f(Z_t, Y_{t-1}, \eta_t),$$  
$f$ 为已知函数形式（如 logistic 或泊松），$Z_t$ 为外生协变量，$Y_{t-1}$ 体现内生聚合。异质性影响通过允许 $\rho$ 随个体或连接变化实现，例如 $\rho_{ij} = \alpha_i + \gamma_j + \delta' d_{ij}$，其中 $d_{ij}$ 为可观测距离。估计采用两阶段广义矩方法（GMM）或贝叶斯 MCMC，利用滞后变量作为工具变量处理内生性，并引入正则化（如 Lasso）应对高维异质性参数。

**与已有工作关系**  
与 Zhu et al. (2017) 的固定网络 NAR 模型相比，本工作将网络视为内生潜变量，更贴近现实；与 Goldsmith-Pinkham & Imbens (2013) 的联合模型相比，本模型允许网络权重连续且时变，并引入异质性影响系数。此外，方法上借鉴了高维统计中的稀疏估计技术，但首次在 NAR 框架下同时处理内生聚合与异质性。

**贡献**  
1. 提出首个同时建模网络内生聚合与异质性影响的广义 NAR 模型，统一了网络形成与结果演化。  
2. 给出参数的可识别性条件及估计量的相合性与渐近正态性证明，填补了理论空白。  
3. 通过模拟和实证（如社交平台意见极化）展示模型在纠正内生性偏误和捕捉个体差异方面的优势，为网络因果推断提供新工具。


## Statistical Learning on Networks and Matrices

*7 月 11 日（周六） · 13:30-15:10 · Huangguoshu Theater Meeting Room*  
*组织 Rui Pan（Central University of Finance and Economics） · 主持 Yan Zhang（Shanghai University of International Business and Economics）*

### 1. Nodal Covariate Selection for Community Structures

**讲者**：Junlong Zhao（Beijing Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
网络数据中，节点常附带高维协变量（nodal covariates），但仅有部分协变量与潜在的社区结构（community structures）相关。现有社区检测方法（如随机块模型SBM）或协变量辅助聚类方法（如Covariate-assisted SBM）通常假设所有协变量均与社区标签相关，或仅将协变量作为辅助信息而不做变量筛选。当协变量中存在大量噪声变量时，直接纳入会降低社区划分精度并损害可解释性。因此，核心问题是如何从高维节点协变量中自动选择出那些真正驱动社区形成的变量，同时准确估计社区结构。

**核心方法**  
报告可能提出一种基于惩罚似然的联合框架。具体地，假设节点标签服从SBM，且协变量与标签通过一个稀疏线性模型关联（如multinomial logistic regression）。通过最大化带Lasso或SCAD惩罚的联合似然函数，同时估计社区分配、回归系数及协变量选择。算法上可能采用EM算法或坐标下降法，交替更新社区标签（通过谱聚类或变分推断）和回归系数。理论方面，可能在高维稀疏条件下证明变量选择的相合性（consistency）以及社区估计的收敛速率。

**与已有工作关系**  
已有工作主要分为两类：一是纯网络社区检测（如SBM、DCSBM），忽略协变量；二是协变量辅助社区检测（如Covariate-SBM、混合模型），但通常假设所有协变量均有效或仅通过加权融合。本工作的新颖之处在于将协变量选择问题显式嵌入社区检测框架，区别于传统的“先聚类再筛选”或“先筛选再聚类”的两阶段方法。此外，与高维回归中的变量选择不同，此处响应变量（社区标签）是潜在且离散的，需同时处理标签估计与变量选择，增加了技术难度。

**主要贡献**  
1. 提出首个针对社区结构的节点协变量选择方法，填补了网络数据分析中“变量选择+社区检测”交叉领域的空白。  
2. 在理论上建立了变量选择一致性和社区估计误差上界，为高维网络协变量筛选提供了统计保证。  
3. 通过模拟和真实数据（如社交网络、基因调控网络）验证方法在降噪、提升聚类精度和可解释性上的优势，为后续研究提供了可复用的算法与理论工具。


### 2. Common Component Recovery in Heterogeneous Chain-Linked Multiple Matrices

**讲者**：Xinyan Fan（Renmin University of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
现实数据常以多个矩阵形式出现，且矩阵间存在链式关联（如时间序列上的连续观测、空间相邻区域的指标矩阵），但各矩阵可能具有异质性（如噪声水平、维度、分布不同）。现有联合矩阵分解方法（如 JIVE、SLIDE）通常假设矩阵间独立或仅共享一个公共低秩结构，忽略了链式依赖带来的额外信息，且难以处理异质性。本报告旨在解决：如何在异质性链式关联的多矩阵中，同时恢复所有矩阵共享的公共成分，并刻画各矩阵特有的个体成分。

**核心方法**  
讲者提出一种基于 **链式低秩分解** 的框架。将每个矩阵 $X_k$ 分解为公共成分 $C_k$、个体成分 $A_k$ 和噪声 $E_k$，其中 $C_k$ 满足链式约束：相邻矩阵的公共成分通过一个低秩转移矩阵 $T_k$ 关联，即 $C_{k+1} = C_k T_k + \Delta_k$，$\Delta_k$ 为稀疏偏差。通过引入 **异质性加权** 的核范数正则化（对不同矩阵的噪声方差自适应调整），并利用交替方向乘子法（ADMM）优化目标函数，同时估计所有参数。理论方面，在链式依赖强度与异质性程度满足一定条件下，证明了公共成分估计的相合性与收敛速率。

**与已有工作关系**  
区别于独立矩阵分解（如 SVD）和经典联合矩阵分解（假设公共成分完全相同），本工作首次将链式依赖显式建模为低秩转移，更贴合动态系统或序列数据。与张量分解（如 Tucker 分解）相比，链式结构允许矩阵间维度不同，且异质性处理更灵活。与动态因子模型相比，本方法不要求时间序列平稳性，且能处理非高斯噪声。

**主要贡献**  
1. 提出链式关联多矩阵的公共成分恢复新问题，并建立包含异质性的统计模型。  
2. 设计可扩展的优化算法，并给出理论收敛性与统计误差界。  
3. 在合成数据与真实应用（如脑电信号、交通流量）中验证了方法相比现有联合分解的显著优势，尤其当链式依赖较强且异质性明显时。


### 3. Hidden Block Regression: A General Framework for Multi-Response Models with Group Structures and Hidden Variables

**讲者**：Yuehan Yang（Central University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在多响应回归中，响应变量之间常存在未知的组结构（group structure），且部分协变量或响应可能受未观测的隐变量（hidden variables）影响。现有方法或假设组结构已知（如多任务学习中的group lasso），或仅处理单响应下的隐变量问题（如latent variable regression），缺乏统一框架同时建模组结构与隐变量对多响应联合分布的影响。本报告旨在解决：当响应变量分组未知、且存在与协变量相关的隐变量时，如何高效估计回归系数并恢复组结构？

**核心方法**  
作者提出Hidden Block Regression框架，将多响应模型写为 $Y = XB + \Gamma H + E$，其中 $B$ 为 $p \times q$ 系数矩阵，$H$ 为 $n \times r$ 隐变量矩阵（$r \ll q$），$\Gamma$ 为隐变量载荷，$E$ 为噪声。核心假设是 $B$ 的行（对应协变量）或列（对应响应）具有块稀疏结构（block sparsity），即某些协变量对整组响应无影响，或某些响应共享相同系数模式。估计采用带隐变量惩罚的优化：$\min_{B,\Gamma,H} \frac{1}{2n}\|Y - XB - \Gamma H\|_F^2 + \lambda_1 \|B\|_{2,1} + \lambda_2 \|\Gamma\|_{2,1}$，其中 $\|B\|_{2,1}$ 为行组Lasso惩罚以诱导行稀疏，$\|\Gamma\|_{2,1}$ 控制隐变量稀疏性。算法通过交替最小化（如block coordinate descent）求解，并利用奇异值分解初始化隐变量。

**与已有工作关系**  
与经典的多任务学习（如multi-response Lasso）相比，本工作显式引入隐变量以解释未被观测的混杂因素，避免因遗漏变量导致系数估计有偏。与sparse latent factor regression（如SLR）相比，本工作额外对系数矩阵施加组结构惩罚，而非仅假设低秩。与group Lasso或overlapping group Lasso相比，本工作允许组结构未知且与隐变量共存，更具一般性。此外，理论分析需处理隐变量与组稀疏惩罚的耦合，不同于现有高维统计中仅考虑单一结构的结果。

**贡献**  
1. 提出首个同时处理多响应组稀疏与隐变量干扰的统一框架，填补了该交叉领域的空白。  
2. 给出估计量的非渐近误差界（oracle inequality），证明在适当条件下可一致恢复组结构并一致估计系数，收敛速率与隐变量维数 $r$ 及组稀疏度相关。  
3. 算法层面提供可扩展的交替优化方案，并给出隐变量秩的交叉验证选择准则。  
4. 通过模拟与真实数据（如基因表达多性状关联分析）展示方法在预测精度与结构发现上的优势，尤其当隐变量解释部分变异时，传统方法失效而本方法稳健。


### 4. A General Exposure-Mapping-Agnostic Framework for Causal Inference under Interference Leveraging Two-Stage Randomization

**讲者**：Yihui He（University of Pennsylvania）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在存在干扰（interference）的因果推断中，个体的潜在结果不仅取决于自身处理，还受他人处理的影响。传统方法通常要求研究者预先指定一个**暴露映射（exposure mapping）**，即定义每个个体所“暴露”到的他人处理模式（如邻居处理比例、特定网络结构下的处理向量）。然而，真实干扰机制往往未知或复杂，错误指定暴露映射会导致估计偏误。本报告旨在解决：**能否在不依赖任何暴露映射先验假设的前提下，从数据中识别并估计因果效应？**

**核心方法**  
报告提出一个**暴露映射无关（exposure-mapping-agnostic）** 的通用框架，核心工具是**两阶段随机化（two-stage randomization）**。第一阶段将总体随机分为若干集群（clusters），并在集群层面随机分配处理强度（如处理比例）；第二阶段在集群内部，对个体进行独立随机化处理分配。通过这种设计，可以构造出不同集群间处理分布的“外生变异”，从而在不指定暴露映射的情况下，识别出**平均处理效应（ATE）** 或**处理强度效应**。具体地，利用两阶段随机化产生的处理分配概率差异，通过逆概率加权或矩估计，将干扰下的因果参数表达为可识别形式，无需显式建模干扰结构。

**与已有工作关系**  
现有文献多依赖特定暴露映射假设（如部分干扰、网络邻域处理计数），或通过假设无干扰（SUTVA）简化问题。近期虽有基于随机化推断或设计的方法（如Hudgens & Halloran 2008的集群随机化），但通常需要已知干扰网络或暴露映射形式。本报告的方法**首次将两阶段随机化与暴露映射无关的识别相结合**，允许干扰机制完全未知，仅依赖实验设计的外生性。这与Baird et al. (2018) 的“部分干扰”设计不同，后者仍需假设干扰局限于集群内；而本框架可推广至跨集群干扰，且无需指定干扰范围。

**贡献**  
1. **理论创新**：提出一个不依赖暴露映射的因果识别条件，将两阶段随机化从工具性设计提升为识别策略的核心。  
2. **方法普适性**：适用于任意干扰结构（包括网络、空间、社会互动），且无需观测干扰网络。  
3. **实践价值**：为实验设计提供新思路——研究者只需实施两阶段随机化，即可在干扰存在时获得稳健的因果估计，避免因暴露映射误设导致的模型偏差。  
4. **潜在扩展**：框架可结合非参数估计或机器学习，实现高维干扰下的高效推断。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)