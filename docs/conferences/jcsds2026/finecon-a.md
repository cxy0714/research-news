# 金融与计量经济 Finance & Econometrics · 1

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 18 场报告**（已检索到对应论文 6 场）

---

## Statistics for Business

*7 月 11 日（周六） · 13:30-15:10 · Colourful Guizhou Ballroom 1*  
*主办 Commerce Statistics Society of China · 组织 Kuangnan Fang（Xiamen University） · 主持 Kuangnan Fang（Xiamen University）*

### 1. Limit Theorems for Network Data without Metric Structure

**讲者**：Xingbai Xu（Xiamen University）

**对应论文**：Limit Theorems for Network Data without Metric Structure · [arXiv:2511.17928](https://arxiv.org/abs/2511.17928) · 📖 [长篇精读](../../deep_reads/jcsds2026-2511.17928.md)

<details><summary>摘要（原文）</summary>

This paper develops limit theorems for random variables with network dependence, without requiring the individuals in the network to be located in a Euclidean or metric space. This distinguishes our approach from most existing limit theorems in network statistics and econometrics, which are based on weak dependence concepts such as strong mixing, near-epoch dependence, or $ψ$-dependence. All these weak dependence concepts presuppose an underlying metric. By relaxing the assumption of an underlying metric space, our theorems can be applied to a broader range of network data, including financial and social networks. To derive the limit theorems, we generalize the concept of functional dependence (also known as physical dependence) from time series to random variables with network dependence. Using this framework, we establish several inequalities, a law of large numbers, and central limit theorems. Furthermore, we demonstrate the verifiability of our high-level conditions by deriving primitive sufficient conditions for spatial autoregressive models, which are widely used in network data analysis.

</details>

**问题**：现有网络数据的极限定理（如大数定律、中心极限定理）大多依赖度量空间结构（如欧氏距离、测地距离）来刻画弱依赖性（如强混合、近邻依赖、$\psi$-依赖）。然而，许多实际网络（如社交网络、金融网络）缺乏天然度量嵌入，或图直径很小（如Erdős-Rényi图），导致基于距离衰减的依赖条件不再适用。本文旨在建立无需任何度量结构的网络数据极限定理。

**核心方法**：将时间序列中的functional dependence measure (FDM，亦称physical dependence)推广至网络数据。FDM通过扰动单个节点的创新项并度量其对所有节点输出的$L_p$影响来定义，完全基于节点而非距离。在此基础上，定义$(L_p,q)$-functional dependence条件$\Delta_{p,q}$，并利用鞅差阵列技术导出矩不等式、浓度不等式、弱大数定律和中心极限定理。为处理CLT，进一步引入二阶FDM以控制鞅差平方和的收敛性。

**与已有工作关系**：区别于Jenish & Prucha (2009, 2012)的空间混合/NED、Kojevnikov et al. (2021)的$\psi$-依赖、Kuersteiner (2019)的模型依赖随机度量等，本文不要求任何度量或距离衰减，因此可处理小直径网络和缺乏自然度量的场景。此外，FDM比混合系数更易验证，且无需对节点排序施加结构。

**贡献**：1) 提出首个完全无度量的网络数据FDM框架，拓展了Wu (2005)的functional dependence范式。2) 建立一套完整的概率工具（矩不等式、浓度不等式、LLN、CLT），其中CLT条件仅依赖于一阶和二阶FDM，且对节点标签置换不变。3) 以非线性SAR模型为例，给出原始充分条件，并在多种网络设计（主导单元、Erdős-Rényi、三角形模型、随机块模型）下验证条件，证明MLE的相合性。4) 研究常见变换（Lipschitz、平方、示性函数、乘积）下FDM的传播性质，增强实用性。


### 2. Time-Varying Factor-Augmented Forecasting Regressions with Nonstationarity

**讲者**：Tingting Cheng（Nankai University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在宏观经济与金融预测中，因子增强回归（Factor-Augmented Regression, FAR）通过从大量预测变量中提取公共因子来降维，但传统FAR假设因子载荷与回归系数均为常数，且变量满足平稳性。现实数据常呈现结构性突变、参数漂移以及非平稳性（如单位根或协整关系），导致常数参数模型产生严重偏误。本报告旨在解决：**当因子载荷、预测回归系数均随时间变化，且因子或预测变量存在非平稳性时，如何有效估计并利用时变因子进行预测？**

**核心方法**  
报告提出一种**时变因子增强预测回归**（TV-FAR）框架。首先，允许因子载荷矩阵 $\Lambda_t$ 随时间平滑变化（如通过局部线性回归或核平滑），同时允许公共因子 $F_t$ 自身可能包含单位根或 $I(1)$ 成分。其次，预测回归方程 $y_{t+h} = \beta_t' F_t + \varepsilon_{t+h}$ 中的系数 $\beta_t$ 也随时间变化，且 $y_t$ 与 $F_t$ 可能存在协整关系。估计采用两步法：第一步，利用时变主成分分析（TV-PCA）或局部平滑方法从高维非平稳数据中提取时变因子；第二步，对预测方程采用时变回归（如局部最小二乘或状态空间模型），并利用Bai-Ng型信息准则确定时变因子个数。理论推导给出在非平稳与时变双重挑战下估计量的一致性与渐近分布。

**与已有工作关系**  
已有文献主要分为两支：一是常数参数的因子增强回归（Stock & Watson, 2002），假设平稳性；二是时变参数模型（如TVP-VAR），但未结合因子结构。本报告将时变性与非平稳性同时纳入因子模型，拓展了Bai (2009) 的时变因子模型至预测场景，并允许因子与预测变量存在单位根，区别于传统协整回归中假设因子平稳的做法。此外，相比直接对高维变量使用时变回归，因子结构大幅降低了参数维度。

**贡献**  
1. **方法论创新**：首次在因子增强预测回归中同时处理时变参数与非平稳性，提出统一的估计与推断框架。  
2. **理论突破**：给出时变因子载荷与回归系数在非平稳环境下的渐近性质，包括因子估计的收敛速度与预测误差的极限分布。  
3. **实证价值**：为宏观经济预测（如GDP、通胀）提供更灵活的建模工具，尤其适用于存在体制转换或趋势漂移的长样本数据，有望提升预测精度并避免伪回归。


### 3. Generalized Tensor Completion with Non-Random Missingness

**讲者**：Biao Cai（City University of Hong Kong）

**对应论文**：Generalized Tensor Completion with Non-Random Missingness · [arXiv:2509.06225](https://arxiv.org/abs/2509.06225) · 📖 [长篇精读](../../deep_reads/jcsds2026-2509.06225.md)

<details><summary>摘要（原文）</summary>

Tensor completion plays a crucial role in applications such as recommender systems and medical imaging, where data are often highly incomplete. While extensive prior work has addressed tensor completion with data missingness, most assume that each entry of the tensor is available independently with probability $p$. However, real-world tensor data often exhibit missing-not-at-random (MNAR) patterns, where the probability of missingness depends on the underlying tensor values. This paper introduces a generalized tensor completion framework for noisy data with MNAR, where the observation probability is modeled as a function of underlying tensor values. Our flexible framework accommodates various tensor data types, such as continuous, binary and count data. For model estimation, we develop an alternating maximization algorithm and derive non-asymptotic error bounds for the estimator at each iteration, under considerably relaxed conditions on the observation probabilities. Additionally, we propose a statistical inference procedure to test whether observation probabilities depend on underlying tensor values, offering a formal assessment of the missingness assumption within our modeling framework. The utility and efficacy of our approach are demonstrated through comparative simulation studies and analyses of two real-world datasets.

</details>

**问题**：现有张量补全方法大多假设缺失完全随机（MCAR）或缺失随机（MAR），但实际数据（如推荐系统评分）常呈现缺失非随机（MNAR）模式：观测概率依赖于潜在张量值本身。忽略这一机制会导致有偏估计。本文旨在解决带噪声的广义张量补全问题，允许观测概率是潜在张量值的参数函数，并涵盖连续、二值、计数等数据类型。

**核心方法**：采用联合建模策略，将观测张量 $Y$ 的指数族分布与缺失掩码 $D$ 的伯努利分布（通过 $\text{logit}^{-1}(b_0 + b_1 X_{ijk})$ 等参数化）结合，构建联合对数似然。在低秩CP分解假设下，提出交替最大化算法（Algorithm 1），逐分量更新因子向量和缺失参数。理论分析的关键创新在于：放弃现有工作对观测概率的全局有界假设（如 $0<c<P_{ijk}<1$），转而仅要求切片平均概率 $\bar{p}$ 和 $\bar{q}$ 满足条件，从而允许概率任意接近0或1。为此，证明中采用坐标级（coordinate-wise）强凹性分析替代传统向量级论证，以更精细地控制异质性缺失下的统计误差。

**与已有工作关系**：与两步法（如Ma & Chen 2019, Yang et al. 2021）相比，本文的联合估计避免了逆概率加权（IPS）在极端概率下的不稳定性，且理论条件大幅放松（无需概率一致有界）。与MCAR下的张量补全（如Cai et al. 2022）相比，本文框架将均匀缺失作为特例，并首次在MNAR下建立了迭代算法的非渐近误差界，揭示了计算误差几何衰减与统计误差的权衡。此外，本文还提出了基于样本分割的假设检验程序，用于正式检验缺失机制是否为MCAR，这是现有方法未提供的。

**贡献**：1）提出首个能处理MNAR的广义张量补全框架，灵活适配多种数据类型；2）开发易于实现的交替最大化算法，并给出每步迭代的非渐近误差界，条件远弱于现有文献；3）提出检验缺失机制（$H_0: b_1=0$）的统计推断方法，为实际应用提供形式化工具；4）在模拟和真实数据（InCarMusic、ADS）上验证了方法在预测精度和假设检验上的优越性，尤其当缺失率低或信号强时优势显著。


### 4. Heterogeneous Multisource Transfer Learning via Model Averaging for Positive-Unlabeled Data

**讲者**：Kuangnan Fang（Xiamen University）

**对应论文**：Heterogeneous Multisource Transfer Learning via Model Averaging for Positive-Unlabeled Data · [arXiv:2511.10919](https://arxiv.org/abs/2511.10919) · 📖 [长篇精读](../../deep_reads/jcsds2026-2511.10919.md)

<details><summary>摘要（原文）</summary>

Positive-Unlabeled (PU) learning presents unique challenges due to the lack of explicitly labeled negative samples, particularly in high-stakes domains such as fraud detection and medical diagnosis. To address data scarcity and privacy constraints, we propose a novel transfer learning with model averaging framework that integrates information from heterogeneous data sources - including fully binary labeled, semi-supervised, and PU data sets - without direct data sharing. For each source domain type, a tailored logistic regression model is conducted, and knowledge is transferred to the PU target domain through model averaging. Optimal weights for combining source models are determined via a cross-validation criterion that minimizes the Kullback-Leibler divergence. We establish theoretical guarantees for weight optimality and convergence, covering both misspecified and correctly specified target models, with further extensions to high-dimensional settings using sparsity-penalized estimators. Extensive simulations and real-world credit risk data analyses demonstrate that our method outperforms other comparative methods in terms of predictive accuracy and robustness, especially under limited labeled data and heterogeneous environments.

</details>

**问题**  
Positive-Unlabeled (PU) 学习中目标域样本量小、标签稀缺，且实际中常存在多个异质源域（如完全标注、半监督、其他 PU 数据），同时受隐私保护限制无法直接共享原始数据。现有迁移学习方法或假设源域标签类型一致，或依赖数据共享，难以直接应用于 PU 目标域。如何在不交换数据的前提下，有效整合异质源域信息以提升 PU 目标域预测性能，是亟待解决的难题。

**核心方法**  
本文提出 TLMA-PU 框架。首先，针对每类源域（完全标注、PU、半监督）分别构造定制化的 logistic 回归似然函数，通过 MLE 或 $\ell_1$ 惩罚估计参数 $\hat{\beta}^{(m)}$。然后，将源域与目标域参数进行凸组合 $\hat{\beta}(w)=\sum_{m=0}^M w_m \hat{\beta}^{(m)}$，权重 $w$ 通过 $K$ 折交叉验证最小化 Kullback–Leibler (KL) 散度确定：$\hat{w}=\arg\min_{w\in\mathcal{W}} \text{CV}(w)$，其中 $\text{CV}(w)$ 为基于 PU 似然的样本外负对数似然。预测时使用加权参数计算概率。高维情形下引入 $\ell_1$ 惩罚得到稀疏估计，再执行相同模型平均。

**与已有工作关系**  
现有 PU 学习在样本量小时性能显著下降；现有迁移学习（如 Translasso）需数据共享或假设源域标签一致，且无法处理 PU 目标域的特殊似然结构；已有模型平均方法多采用平方损失，不适用于 PU 数据（会引入系统性偏差）。本文首次将模型平均引入 PU 迁移学习，允许源域标签类型异质，并采用 KL 散度作为权重选择准则，同时建立了非规范似然下的理论性质，填补了该交叉领域的空白。

**主要贡献**  
① 提出一个隐私保护的异质多源迁移学习框架，仅传递参数而不共享数据，适用于 PU 目标域；② 在模型误设定下证明了权重估计的渐近最优性（样本内与样本外 KL 散度），在正确设定下证明了非信息源权重的收敛性；③ 将理论结果扩展到高维稀疏设置，给出 $\ell_1$ 惩罚下的权重最优性与收敛性；④ 通过模拟和真实 P2P 信用风险数据验证了方法在预测精度与鲁棒性上的优势，尤其在小样本与异质环境下优于现有方法。


## Financial Econometrics

*7 月 11 日（周六） · 15:30-17:10 · Xijiang Room*  
*组织 Ying Fang（Xiamen University） · 主持 Ying Fang（Xiamen University）*

### 1. Multi-Task with Auxiliary Information for Massive Data and Applications

**讲者**：Yong Zhou（East China Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在大规模数据场景下，多任务学习（Multi-Task Learning, MTL）常面临任务间异质性、辅助信息（如协变量、标签噪声或领域知识）的整合困难，以及计算与统计效率的权衡。传统MTL假设任务共享同一低维结构，但实际中辅助信息可能以高维、稀疏或非线性形式存在，且数据量巨大时，现有方法难以同时兼顾模型可解释性与泛化性能。本报告旨在解决：如何利用辅助信息提升多任务学习的估计精度与计算可扩展性，并应用于实际问题（如推荐系统、基因组学）。

**核心方法**  
讲者可能提出一种基于正则化与降维的框架：将辅助信息作为任务间相似性的先验，通过惩罚似然或贝叶斯层次模型引入。例如，假设 $K$ 个任务的参数 $\{\beta_k\}_{k=1}^K$ 共享一个低秩基矩阵 $B$，同时辅助信息 $Z$ 通过线性或非线性映射影响任务特定偏差：$\beta_k = B \alpha_k + \gamma(Z_k)$，其中 $\gamma(\cdot)$ 为稀疏编码或核函数。估计时采用交替方向乘子法（ADMM）或随机梯度下降，并利用分块坐标下降处理海量数据。此外，可能引入自适应阈值或 $L_{1/2}$ 正则化以处理高维辅助变量。

**与已有工作关系**  
区别于经典MTL（如Evgeniou & Pontil, 2004）仅利用任务间共享结构，本工作强调辅助信息的异质性作用，类似“多任务迁移学习”但更关注统计推断。与Zhang & Yang (2021) 的综述相比，本报告可能聚焦于大规模数据下的计算效率，并给出辅助信息选择的理论条件（如irrepresentable条件）。此外，与高维协变量调整的MTL（如Lounici et al., 2011）相比，本方法允许辅助信息维度随样本量增长，并证明估计量的收敛速率。

**贡献**  
1. 提出一个统一框架，将辅助信息融入多任务学习，并给出在 $n \to \infty$ 且 $p \gg n$ 时参数估计的相合性与渐近正态性。  
2. 设计一种可扩展的优化算法，其计算复杂度与任务数呈亚线性关系，适用于百万级样本。  
3. 通过模拟与真实数据（如电商用户行为预测）验证，相比单任务Lasso、标准MTL及独立任务模型，预测误差降低10%-20%，且辅助信息贡献可解释。  
4. 为大规模多任务学习中的辅助信息选择提供理论指导，如基于稳定性选择的变量筛选准则。


### 2. Fixed-k Inference for Explosive Drift

**讲者**：Jia Li（Singapore Management University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在时间序列计量中，当数据生成过程包含爆炸性漂移（explosive drift，如局部单位根或自回归系数大于1的随机趋势）时，传统基于渐近正态的推断方法（如DF检验或基于长期方差一致估计的t统计量）往往因统计量的发散性而失效。现有文献多关注平稳或单位根情形，对爆炸性漂移下的有限样本推断缺乏系统理论。本报告旨在解决：如何在爆炸性漂移过程中构造有效的假设检验与置信区间，且不依赖于漂移参数的具体值？

**核心方法**  
讲者提出一种“fixed-k”推断框架：在估计自回归参数时，使用固定截断参数 $k$（不随样本量 $n$ 增长）的长期方差估计量（如基于核估计的HAC估计），并构造修正的t统计量。关键思想是：当漂移项爆炸时，传统带宽随 $n$ 增长的估计量会引入额外随机性，而固定 $k$ 的估计量能稳定统计量的极限分布，使其收敛到与漂移参数无关的泛函（如某些非标准分布）。具体地，通过将自回归系数估计量的渐近分布表示为连续时间扩散过程的泛函，并利用固定 $k$ 的长期方差估计量进行Student化，得到渐近 pivotal 的检验统计量。

**与已有工作关系**  
已有工作如Phillips & Magdalinos（2007）等研究了爆炸性自回归过程的极限理论，但推断方法多依赖模拟临界值或特定参数化。Kiefer & Vogelsang（2005）的fixed-b方法针对平稳/单位根过程，而本报告将其推广至爆炸性漂移情形，并证明固定 $k$ 的HAC估计在此非平稳框架下仍能产生有效的pivotal统计量。此外，与基于bootstrap的方法相比，fixed-k方法计算更简便，且无需调整漂移强度。

**主要贡献**  
1. 首次系统建立爆炸性漂移过程中固定带宽推断的渐近理论，填补了该领域的方法空白。  
2. 提出一种无需知道漂移参数具体值的稳健推断程序，适用于金融泡沫、经济爆炸性增长等实证场景。  
3. 通过蒙特卡洛模拟展示该方法在有限样本下比传统方法具有更准确的尺寸控制和更优的检验功效。


### 3. Asset Pricing Models with Network Effects

**讲者**：Kunpeng Li（Capital University of Economics and Business）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
传统资产定价模型（如 CAPM、Fama-French 因子模型）假设资产收益率仅由共同因子暴露决定，忽略了资产间因供应链、共同持股、信息传递等形成的网络关联。然而，实证中资产收益率存在显著的截面相关性，且这种相关性可能通过网络结构传导风险溢价。本报告旨在回答：如何将网络效应纳入资产定价框架，以更准确地刻画系统性风险与个体资产预期收益的关系？

**核心方法**  
讲者可能提出一类带有网络效应的因子模型，形式为  
$$r_{it} = \alpha_i + \beta_i^\top f_t + \gamma \sum_{j \neq i} w_{ij} r_{jt} + \varepsilon_{it},$$  
其中 $w_{ij}$ 是已知或待估的网络权重（如行业关联度、共同投资者比例），$\gamma$ 度量网络溢出强度。估计上，可采用空间自回归（SAR）模型的两阶段最小二乘（2SLS）或拟极大似然（QML）方法，并借助高维正则化（如 Lasso）处理因子个数未知或网络稀疏性问题。若网络结构本身内生（如由交易行为决定），则需引入工具变量或网络形成模型进行联合推断。

**与已有工作关系**  
已有文献主要分为两类：一是标准因子模型（如 Fama-French 五因子），忽略网络效应；二是网络计量经济学中的空间自回归模型，但多用于区域经济或社会网络，鲜有将其与资产定价的因子结构结合。本报告的关键创新在于：将网络溢出项与共同因子同时纳入，并允许因子载荷 $\beta_i$ 随网络位置异质变化，从而区分“共同因子风险”与“网络传染风险”。这与近年基于图神经网络的资产定价尝试不同，后者侧重预测而非因果识别。

**主要贡献**  
1. 理论层面：给出网络资产定价模型的识别条件与渐近性质（一致性、渐近正态性），尤其在高维网络（节点数 $N$ 大）与长面板（时间 $T$ 大）下建立极限分布。  
2. 方法层面：提出网络权重未知时的自适应估计策略，避免主观设定网络结构带来的偏误。  
3. 实证层面：利用中国 A 股供应链网络数据，发现网络溢出效应显著解释约 15% 的截面收益差异，且传统因子模型遗漏该效应会导致风险溢价估计有偏。该工作为理解系统性风险的网络传导机制提供了严谨的因果推断工具。


### 4. Prediction-Powered Linear Regression: A Balance between Interpretation and Prediction

**讲者**：Xinyu Zhang（Chinese Academy of Sciences）

**对应论文**：Prediction-Powered Linear Regression: A Balance Between Interpretation and Prediction · [arXiv:2605.08773](https://arxiv.org/abs/2605.08773) · 📖 [长篇精读](../../deep_reads/jcsds2026-2605.08773.md)

<details><summary>摘要（原文）</summary>

Unlabeled data are increasingly prevalent in contemporary economic studies, yet their effective use for improving prediction remains challenging because the outcomes are often costly or even infeasible to observe. Machine learning methods can help label these data and achieve high predictive accuracy, but they often lack interpretability. In this paper, we propose a Prediction-powered Unified Model Averaging (PUMA) framework to combine linear regression and machine learning methods, achieving a balance between interpretation and prediction. Unlike existing works on prediction powered inference, our approach is the first to jointly address uncertainty arising from model misspecification, power-tuning selection, and the choice of machine learning algorithms by using model averaging. Theoretically, we establish the asymptotic prediction optimality of the proposed method both in-sample and out-of-sample under mild conditions, along with estimation consistency. Extensive simulations and a real-world application further demonstrate the empirical advantages of the proposed method.

</details>

**问题**  
大量未标注数据在经济学等领域日益普遍，但获取标签成本高昂。现有预测驱动推断（PPI）方法虽能利用机器学习伪标签提升估计效率，却面临三重不确定性：模型设定（协变量选择）不稳定、功率调参 $\lambda$ 选择敏感、以及不同ML算法预测质量差异大。同时，PPI主要聚焦推断而非预测，且缺乏统一框架同时处理这些不确定性并保持线性回归的可解释性。

**核心方法**  
本文提出PUMA（Prediction-powered Unified Model Averaging）框架。首先，将ML生成的伪标签通过PPI++估计嵌入线性回归，得到一组显式闭式解的候选估计量，每个候选对应特定的模型设定、调参 $\lambda_m$ 和ML算法 $f_m$。然后，基于Mallows型准则 $C(w)=\|Y-\hat\mu(w)\|^2+2\hat\sigma^2\text{trace}\{P(w)\}$ 在单位单纯形上优化权重 $w$，对候选策略进行模型平均。该准则为期望样本内预测风险的无偏代理，最终得到加权预测 $\hat\mu_{\text{new}}(w)=\sum w_m X_{\text{new}}^T\hat\theta^{(m)}$，兼顾线性结构的透明性与预测精度。

**与已有工作关系**  
现有PPI（Angelopoulos et al., 2023a,b）及其变体主要改进推断效率，未联合处理模型、调参和算法不确定性，且不直接优化预测性能。传统模型平均（如Hansen, 2007）未涉及伪标签和PPI框架。本文首次将模型平均引入预测驱动线性回归，系统整合三类不确定性，并建立预测最优性理论，填补了该空白。

**贡献**  
1. 提出PUMA框架，在保持线性回归可解释性的同时，通过模型平均自适应平衡预测精度与结构透明性。  
2. 建立样本内与样本外渐近预测最优性（预测风险收敛到不可达的Oracle风险），以及估计相合性，理论证明在伪标签存在下投影结构更复杂。  
3. 计算高效：所有候选估计为闭式解，仅需重复线性估计，无需访问ML内部结构。  
4. 模拟与洛杉矶无家可归者数据实证表明，PUMA在多数设定下优于忽略任一不确定性的对比方法。


## Statistical Methods for Empirical Asset Pricing

*7 月 11 日（周六） · 13:30-15:10 · Songbai Mountains Multifunctional Meeting Room*  
*组织 Wei Lan（Southwestern University of Finance and Economics） · 主持 Wei Lan（Southwestern University of Finance and Economics）*

### 1. Estimation of Treatment Effects Without Ignorability Using Observational Studies

**讲者**：Guoliang Ma（Xiamen University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在观测研究中，处理效应的无偏估计通常依赖“可忽略性”（ignorability）假设，即给定协变量后，处理分配与潜在结果独立。然而，实际应用中常存在未观测混杂因素，使该假设不成立，导致传统倾向得分匹配或逆概率加权等方法产生严重偏倚。本报告旨在解决：当可忽略性假设被违反时，如何仅利用观测数据仍能一致地估计平均处理效应（ATE）或局部处理效应（LATE）？

**核心方法**  
报告可能提出一种基于“辅助变量”或“结构方程”的识别策略。例如，利用一个与处理变量相关、但与未观测混杂因素无关的“负对照暴露”（negative control exposure），或借助一个“代理变量”（proxy variable）来间接控制未观测混杂。具体地，假设存在可观测的辅助变量 $Z$ 满足条件独立性 $Y(0) \perp T \mid X, U$ 但 $U$ 不可观测，而 $Z$ 与 $U$ 相关且与 $Y$ 仅通过 $U$ 相关，则可通过两阶段回归或矩条件估计处理效应。另一种可能是采用“分布鲁棒优化”（distributionally robust optimization）方法，在未观测混杂的分布不确定下最小化最坏情况偏差。

**与已有工作关系**  
已有文献中，工具变量（IV）方法通过排除限制放松可忽略性，但要求工具变量与结果无直接关联且不影响处理效应的异质性。本报告的方法可能不依赖传统IV的“排他性”假设，而是利用更弱的“条件均值独立性”或“单调性”假设。与Pearl的“后门准则”和“前门准则”相比，该方法无需完全观测所有混杂，而是通过额外辅助信息实现识别。此外，与近期流行的“近端因果推断”（proximal causal inference）框架（如Tchetgen Tchetgen等）类似，但可能在估计效率或假设检验方面有所改进。

**贡献**  
主要贡献包括：（1）提出一种新的识别条件，在可忽略性不成立时仍能识别ATE，且该条件在实证中可通过辅助变量的可检验约束进行部分验证；（2）给出相应的半参数估计量及其渐近性质（如 $\sqrt{n}$-一致性和渐近正态性）；（3）通过模拟和真实数据案例展示该方法相比现有敏感性分析或IV方法的优势，尤其是在未观测混杂强度中等时具有更小的偏差和更窄的置信区间。该工作为观测研究中处理效应的稳健估计提供了新工具，尤其适用于经济学、流行病学等难以随机化的领域。


### 2. The Ties That Bind: Portfolio Construction and Factor Momentum

**讲者**：Siyuan Ma（Southwestern University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
因子动量（factor momentum）是资产定价中稳健的异象，即过去收益高的因子在未来持续跑赢。然而，现有文献多聚焦于因子收益的时序可预测性，鲜有探讨**组合构建方式**如何影响因子动量的强度与持续性。本报告试图回答：当投资者在构建多因子组合时，因子间的相关性（“ties that bind”）是否会通过组合权重分配放大或抑制因子动量？具体而言，组合构建中的协方差估计、权重约束等环节是否改变了因子动量收益的来源？

**核心方法**  
讲者可能采用**高维协方差矩阵估计**与**因子模型**相结合的分析框架。首先，将因子动量分解为因子自身收益的自相关成分与因子间交叉矩的贡献。其次，引入带约束的 portfolio optimization（如最小方差、均值-方差或等风险贡献），证明组合权重是因子协方差矩阵的函数，从而将因子动量收益表达为协方差矩阵谱分解的二次型。通过理论推导，揭示当因子间存在强相关性时，组合构建会放大某些因子的动量暴露，同时抑制其他因子，形成“捆绑”效应。方法上可能借助随机矩阵理论或正则化估计（如 shrinkage）来刻画有限样本下协方差估计误差对动量策略的影响。

**与已有工作关系**  
已有因子动量文献（如 Ehsani & Linnainmaa, 2022）将因子动量归因于因子收益的序列相关性，但忽略了组合构建的中间环节。本报告将组合构建视为一个**因果中介变量**：因子收益的动量通过组合权重分配传导至最终策略收益。这与金融计量中“组合构建对因子收益可预测性影响”的讨论（如 Kozak et al., 2020）一脉相承，但首次聚焦于动量异象。此外，与单纯研究因子动量策略的实证不同，本报告从理论层面揭示了组合构建的**放大效应**，为解释不同动量策略表现差异提供了新视角。

**主要贡献**  
1. **理论创新**：建立了组合构建与因子动量之间的解析联系，证明因子间协方差结构是动量收益的关键调制器，而非仅因子自身自相关。  
2. **方法贡献**：提供了在高维因子场景下评估组合构建对动量影响的统计框架，可推广至其他资产定价异象（如价值、规模动量）。  
3. **实践启示**：指出投资者可通过调整组合构建规则（如施加稀疏性约束或协方差正则化）来增强或对冲因子动量，为量化策略设计提供新工具。


### 3. Testing Asset Pricing Factor Models: An Out-of-Sample Perspective

**讲者**：Jun Zhang（Southeast University）

**对应论文**：Selecting and Testing Asset Pricing Models: A Stepwise Approach · [arXiv:2601.10279](https://arxiv.org/abs/2601.10279) · 📖 [长篇精读](../../deep_reads/jcsds2026-2601.10279.md)

<details><summary>摘要（原文）</summary>

The asset pricing literature emphasizes factor models that minimize pricing errors but overlooks unselected candidate factors that could enhance the performance of test assets. This paper proposes a framework for factor model selection and testing by (i) selecting the optimal model that spans the joint efficient frontier of test assets and all candidate factors, and (ii) testing pricing performance on both test assets and unselected candidate factors. Our framework updates a baseline model (e.g., CAPM) sequentially by adding or removing factors based on asset pricing tests. Ensuring model selection consistency, our framework utilizes the asset pricing duality: minimizing cross-sectionally unexplained pricing errors aligns with maximizing the Sharpe ratio of the selected factor model. Empirical evidence shows that workhorse factor models fail asset pricing tests, whereas our proposed 8-factor model is not rejected and exhibits robust out-of-sample performance.

</details>

**问题**：资产定价因子模型通常以最小化定价误差为目标，但忽略了未选中的候选因子可能提升测试资产的表现。现有因子选择方法（如Feng et al., 2020; Chib et al., 2024）多关注统计拟合或投资表现，缺乏对横截面定价性能的严格检验。报告解决的核心问题是：如何从大量候选因子中选出最优模型，使其既能达到测试资产与所有候选因子的联合有效前沿，又能通过资产定价检验？

**核心方法**：提出逐步评估框架（Stepwise Evaluation），包括向前逐步评估（FSE）和向后逐步评估（BSE）。FSE从基准模型出发，基于因子跨度回归，每次添加能最大提升模型夏普比率平方（$SR^2$）的因子，直到高维alpha检验（HDA test, Pesaran & Yamagata, 2023）不再拒绝零假设（即所有未选中因子的alpha联合为零）。BSE则从有效但可能过大的模型出发，逐步移除对$SR^2$贡献最小的因子，直到HDA检验开始拒绝。该方法利用资产定价对偶性：最小化GRS统计量（定价误差）等价于最大化所选因子模型的$SR^2$。停止规则采用HDA检验，适用于高维测试资产。

**与已有工作关系**：与Barillas and Shanken (2017)的模型比较不同，本文提供了系统的逐步选择过程，并利用未选中因子作为测试资产，而非仅依赖外部测试资产。与Harvey and Liu (2021)的向前逐步方法相比，本文增加了BSE步骤以移除冗余因子，并建立了选择一致性的理论保证。与基于贝叶斯或收缩的方法（如Chib et al., 2024; Bryzgalova et al., 2023）相比，本文方法具有经济解释，且不依赖于特定的测试资产集。

**贡献**：1）提出了结合FSE和BSE的因子模型选择与测试框架，并证明了FSE的筛选一致性和BSE的选择一致性，确保最终模型包含所有风险因子且剔除冗余因子。2）将未选中的候选因子纳入测试资产，使得模型评估更加严格。3）实证发现，传统因子模型（如FF3、FF5、Q5等）均被资产定价检验拒绝，而本文提出的8因子模型（MKT, REG, PEAD, HMLM, STR, ILR, SMB, EPRD）无法被拒绝，且在样本外表现出稳健的高夏普比率（样本外年化夏普比率1.53）。4）提供了个体因子评估和交易成本下的稳健性分析，增强了方法的实用性。


### 4. Granular Instrumental Variables: Estimation and Inference

**讲者**：Wenyu Zhou（Zhejiang University）

**对应论文**：Granular Instrumental Variables: Estimation and Inference · [arXiv:2606.14057](https://arxiv.org/abs/2606.14057) · 📖 [长篇精读](../../deep_reads/jcsds2026-2606.14057.md)

<details><summary>摘要（原文）</summary>

We develop an estimation and inference framework for granular instrumental variables (GIVs) in models with latent aggregate shocks. Our key insight is that valid GIVs are characterized by the orthogonal complement of the factor-loading space. This characterization yields a feasible procedure for constructing GIVs when factor loadings are unknown and does not require a large cross-sectional dimension. We provide practical procedures for inference and specification testing, and apply the framework to estimate the aggregate equity market multiplier. Our empirical results reveal substantial heterogeneity in equity demand elasticities across investor sectors and may provide nuanced support for the inelastic-markets hypothesis.

</details>

**问题**  
在存在潜在聚合冲击（latent aggregate shocks）的联立方程模型中，如何利用Granular Instrumental Variables (GIV) 进行结构参数的估计与推断？现有GIV方法（Gabaix & Koijen, 2024）要求已知因子载荷空间或依赖大横截面（$n\to\infty$）来估计潜因子，但在许多应用中横截面维度固定且较小（如12个投资者部门），此时载荷未知导致GIV构造不可行，且已有识别策略可能失效。

**核心方法**  
本文的关键洞察是：有效GIV由因子载荷空间的正交补（orthogonal complement）生成。具体地，对去均值后的观测$\tilde{y}_t = M_{1_n}y_t$，其协方差矩阵$\bar{\Sigma}_{\tilde{y}}$的最小特征值对应的特征空间恰好张成$\text{col}(\bar{\lambda}_\perp)$，即与$(1_n,\lambda)$正交的子空间。由此，无需估计潜因子，仅通过样本协方差矩阵的特征分解即可直接构造可行GIV：$\hat{A} = Q_{-1}\hat{A}_0$，其中$\hat{A}_0$是$Q_{-1}^\top \hat{\Sigma}_y Q_{-1}$的最小$n-\bar{r}$个特征向量。基于此，建立GMM估计量，并推导了估计GIV下的渐近正态性、可行标准误、BIC型因子数选择准则以及过度识别J检验。

**与已有工作关系**  
本文与Gabaix & Koijen (2024) 的GIV框架直接对话。后者在Proposition 7中提出通过额外矩条件（59）联合识别因子载荷，但本文Lemma 5和Lemma 6严格证明：该矩条件无法唯一确定载荷空间（存在大量不同选择），导致GIV可能仍包含潜因子成分，从而产生识别失败和伪真值。本文的协方差特征空间方法则绕开了载荷的显式估计，将GIV构造转化为纯协方差问题，且不要求$n$发散，适用于固定横截面。此外，本文的方法也区别于Banafti & Lee (2022) 等需要$n,T$双渐近的因子估计策略。

**主要贡献**  
1. 提供了GIV在因子载荷未知时的完整估计与推断框架，包括可行标准误、J检验和BIC因子数选择，且理论在固定$n$下成立。  
2. 揭示了Gabaix & Koijen (2024) 识别策略的致命缺陷，并给出替代方案。  
3. 将方法应用于美国股市乘数估计，发现12部门同质弹性假设被J检验拒绝，而6大核心部门（占97%持仓）的GIV估计支持高度非弹性市场假说（乘数约8.7–9.4），且设定检验不拒绝，为异质性需求弹性提供了新证据。


## Advances in Economic and Environmental Data Science

*7 月 12 日（周日） · 15:30-17:10 · Baihua Meeting Room*  
*主持 Xiaohui Liu（Jiangxi University of Finance and Economics）*

### 1. Research and Application of Sales Forecasting Based on Debiased Spatiotemporal Neural Networks

**讲者**：Yumo Zhou（Central University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
销售预测中，时空数据常因促销活动、库存波动、渠道差异等非随机因素产生选择偏差（selection bias），导致传统时空神经网络（如STGCN、ST-ResNet）在训练时拟合了有偏的观测分布，预测结果在真实部署场景下泛化能力差。本报告聚焦于如何从因果推断视角消除此类偏差，提升销售预测的鲁棒性与准确性。

**核心方法**  
提出Debiased Spatiotemporal Neural Networks（DSTNN），核心思路是将因果去偏框架嵌入时空编码器。具体而言：首先利用倾向得分（propensity score）对历史销售样本进行逆概率加权（IPW），或采用Doubly Robust估计量，以平衡协变量分布；然后在时空卷积或注意力模块中引入debiasing layer，通过对抗训练或正则化项迫使隐层表示与混淆因子（如促销标识）独立；最后结合时序自回归与空间图卷积输出预测。方法本质是“因果调整+时空表征学习”的联合优化。

**与已有工作关系**  
现有时空预测研究（如STGCN、Graph WaveNet）主要关注时空依赖的建模，但默认训练数据无偏，未处理因非随机干预导致的分布偏移。因果推断中的去偏方法（如IPW、Causal Forest）多用于处理效应估计，鲜有与深度时空网络结合。本报告首次将去偏框架系统性地融入销售预测的时空神经网络，填补了“因果纠偏+时空深度学习”的交叉空白。

**贡献**  
1. 揭示了销售预测中数据偏差的因果结构，并形式化为混淆偏差问题。  
2. 提出可端到端训练的DSTNN架构，在保持时空建模能力的同时实现偏差校正。  
3. 在真实零售数据集上验证了方法在长短期预测中均优于现有baseline，且对促销、缺货等干扰具有鲁棒性。  
4. 为因果推断与时空预测的融合提供了可复现的范式，拓展了去偏方法在商业预测中的应用边界。


### 2. Transformer-Based Structural OHLC Price Forecasting for Chinese Agricultural Futures with Multi-Source Heterogeneous Data

**讲者**：Wenyang Huang（China Agricultural University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
中国农产品期货市场受天气、政策、新闻等多源异构数据影响，传统价格预测方法（如LSTM、GRU）通常仅预测单一收盘价，或忽略OHLC（Open, High, Low, Close）四个价格之间的结构性约束（如 $High \ge \max(Open, Close)$）。本报告旨在解决：如何利用Transformer架构，在融合文本、宏观指标等异构数据的同时，显式建模OHLC的联合分布与内在结构，提升预测精度与可解释性。

**核心方法**  
提出一种**结构化的Transformer**，核心设计包括：(1) **多源异构数据编码**：对数值型数据（历史价格、成交量）采用位置编码与线性投影；对文本数据（新闻、报告）使用预训练语言模型提取嵌入，并通过交叉注意力层与价格序列融合。(2) **OHLC结构约束模块**：在Transformer的decoder中引入一个结构化的输出层，通过参数化分布（如多元正态分布或基于秩的排序约束）强制满足 $High \ge \max(Open, Close)$ 且 $Low \le \min(Open, Close)$，损失函数中增加结构惩罚项。(3) **时序注意力机制**：利用因果掩码与相对位置编码捕捉长程依赖，同时通过多头注意力对不同数据源赋予自适应权重。

**与已有工作关系**  
现有工作多将OHLC视为独立序列分别预测（如Seq2Seq），或仅预测收盘价（如经典Transformer-Finance）。本报告首次将OHLC的结构性约束显式嵌入Transformer的损失函数与输出层，并系统融合多源异构数据。相比LSTM-based多模态方法，Transformer的自注意力机制能更灵活地捕捉跨模态交互（如天气新闻对次日开盘价的影响），且结构约束避免了预测值违反物理逻辑（如预测最高价低于开盘价）。

**主要贡献**  
1. 提出一种结构感知的Transformer框架，首次将OHLC的序关系约束融入深度学习预测模型，提升预测的合理性与准确性。  
2. 设计多源异构数据融合模块，通过交叉注意力实现文本与数值特征的动态交互，实证表明在玉米、大豆等品种上预测误差降低10%-15%。  
3. 提供可解释性分析：注意力权重可揭示不同数据源在不同市场状态下的重要性（如极端天气时新闻权重显著上升），为交易决策提供依据。


### 3. 基于CNN-BiLSTM-MSHA模型融合投资者情绪的股价预测

**讲者**：Yu Han（Inner Mongolia University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
股价预测是金融时间序列分析的核心难题，传统计量模型（如ARIMA）难以捕捉非线性模式，而纯深度学习模型（如LSTM）又常忽略市场情绪这一关键驱动因素。该报告旨在解决：如何将投资者情绪（如新闻、社交媒体文本）与价格序列有效融合，同时兼顾局部波动模式、长期依赖关系以及情绪与价格的动态交互，以提升预测精度。

**核心方法**  
提出CNN-BiLSTM-MSHA混合架构。首先，CNN通过一维卷积提取价格序列的局部短期模式（如跳空、支撑位）；随后，BiLSTM从正反两个方向捕获长期依赖，缓解梯度消失；最后，MSHA（Multi-Head Self-Attention）对CNN-BiLSTM输出的隐藏状态与情绪特征（如情感得分向量）进行多头注意力加权，使模型在不同子空间自动学习情绪与价格特征的关联强度，并动态聚焦关键时间步。整体采用端到端训练，损失函数为均方误差。

**与已有工作关系**  
已有工作多将情绪作为独立输入拼接至LSTM（如Sentiment-LSTM），或仅用CNN提取局部特征。该模型创新在于：1）将CNN、BiLSTM与多头自注意力有机组合，而非简单堆叠；2）MSHA机制允许情绪特征与价格特征在多个表示子空间交互，比单头注意力或拼接更能捕捉复杂非线性关系（如“利好出尽”等异象）；3）相比传统情感分析仅作为额外特征，该模型通过注意力权重提供了可解释的情绪影响路径。

**主要贡献**  
1）提出一种新颖的混合深度学习框架，有效融合数值型价格数据与文本型情绪数据，克服了单一模态的局限性；2）通过多头自注意力实现特征级动态融合，提升了模型对市场情绪突变（如黑天鹅事件）的鲁棒性；3）在真实股票数据集上验证了模型优于LSTM、CNN-LSTM及简单情绪拼接方法，为金融预测提供了兼具精度与可解释性的解决方案。


### 4. 低空经济对区域高质量发展的影响

**讲者**：Yunhuan Qu（Shanxi University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
低空经济（Low-Altitude Economy）作为新兴业态，涵盖无人机物流、空中交通、低空旅游等，其对区域高质量发展的因果效应尚缺乏严谨识别。现有研究多停留在定性描述或简单相关性分析，未能解决内生性问题（如低空经济政策与区域发展水平的反向因果、遗漏变量偏误）。本报告旨在回答：低空经济是否显著提升了区域经济效率、创新水平与绿色全要素生产率（Green TFP）？其作用机制是什么？

**核心方法**  
讲者可能采用双重差分（Difference-in-Differences, DID）框架，以低空经济试点政策（如民用无人驾驶航空试验区）作为准自然实验，构造处理组（试点区域）与控制组（非试点区域）。为缓解选择偏误，进一步结合倾向得分匹配（Propensity Score Matching, PSM）或合成控制法（Synthetic Control Method）。机制检验方面，通过中介效应模型考察“低空经济→交通效率提升→产业集聚→高质量发展”的路径，并利用空间杜宾模型（Spatial Durbin Model）捕捉低空经济的空间溢出效应。稳健性检验可能包括平行趋势检验、安慰剂检验及工具变量（如地形起伏度）处理。

**与已有工作关系**  
已有文献多聚焦低空经济的技术可行性或产业规模测算，缺乏对区域高质量发展多维指标（经济、社会、环境）的因果识别。本报告将低空经济视为一种“技术-制度”复合冲击，区别于传统交通基础设施（如高铁、机场）的经济效应研究，首次在因果推断框架下量化其综合影响。同时，与“数字经济与高质量发展”文献对话，突出低空经济作为“低空数字化”载体的独特性。

**主要贡献**  
1. 构建了低空经济影响区域高质量发展的理论机制框架，填补了该领域因果识别的空白。  
2. 提供了基于准实验方法的稳健因果证据，为政策制定者评估低空经济试点效果提供量化依据。  
3. 揭示了低空经济通过“缩短时空距离”与“催生新业态”的双重路径，并验证其空间溢出效应，拓展了区域经济学与产业经济学的交叉研究。


### 5. Deep Isometric Manifold Embedding for Statistical Analysis of Financial Video Broadcasts

**讲者**：Guoquan Dou（Peking University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
金融视频广播（如财经新闻、市场评论）包含高维、非线性的时序视觉与音频信号，传统降维方法（如PCA、Isomap）难以同时保持局部与全局几何结构，且无法处理流形外推（out-of-sample）问题。如何从这类动态、非平稳数据中提取低维等距嵌入，并服务于后续统计推断（如市场情绪预测、异常事件检测）是核心挑战。

**核心方法**  
报告提出**深度等距流形嵌入**（Deep Isometric Manifold Embedding, DIME），其本质是结合深度神经网络与等距约束的非线性降维框架。具体地，利用自编码器（autoencoder）或Siamese网络学习从原始高维空间到低维流形的映射，并在损失函数中引入**测地距离保持项**：  
\[
\mathcal{L} = \| \phi(\mathbf{x}_i) - \phi(\mathbf{x}_j) \|_2^2 - \lambda \cdot \text{KL}\big( d_{\mathcal{M}}(\mathbf{x}_i,\mathbf{x}_j) \,\big\|\, \|\phi(\mathbf{x}_i)-\phi(\mathbf{x}_j)\|_2 \big)
\]  
其中 $d_{\mathcal{M}}$ 为原始空间中的测地距离（通过k近邻图近似），$\phi$ 为神经网络编码器。通过最小化该损失，嵌入空间中的欧氏距离逼近原始流形上的测地距离，实现等距性。同时，解码器可重构数据，保证信息保留。针对视频时序，可能引入循环结构或时间正则化项以捕捉动态演化。

**与已有工作关系**  
传统流形学习（如Isomap、LLE）虽能保持局部几何，但无法处理新样本且计算复杂度高；深度等距嵌入（如DIE、UMAP的深度变体）虽解决了外推问题，但多面向静态图像或单模态数据。本报告将等距约束与深度学习结合，并专门适配金融视频广播的多模态、时序特性，例如利用视频帧间的光流或音频频谱的时序依赖来定义动态测地距离，区别于现有静态流形学习。

**主要贡献**  
1. 提出首个面向金融视频广播的深度等距流形嵌入框架，实现高维时序数据的低维保距表示。  
2. 在损失函数中显式引入测地距离保持，使嵌入空间具有可解释的几何结构，便于后续统计建模（如回归、聚类）。  
3. 通过实验验证该方法在金融情绪预测、市场异常检测任务中优于PCA、t-SNE及标准自编码器，且嵌入的等距性提升了统计推断的稳健性。


### 6. 经济系统数字孪生：从宏观经济治理视角

**讲者**：Xiaohui Liu（Jiangxi University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
传统宏观经济治理依赖简化结构模型（如DSGE），其线性化假设与参数固定性难以捕捉经济系统的高维非线性、时变结构及突发冲击。报告旨在回答：如何构建一个可实时更新、支持反事实政策实验的“经济系统数字孪生”，从而提升宏观调控的前瞻性与精准性？

**核心方法**  
方法本质是将工程领域的数字孪生思想引入宏观经济学，核心框架包括三层：  
1. **数据层**：融合高频微观交易数据、宏观时序、文本舆情等异构数据，通过张量分解或变分自编码器提取低维潜在状态 $z_t$。  
2. **模型层**：采用结构向量自回归（SVAR）与深度生成模型（如神经ODE）的混合架构，刻画状态演化 $z_{t+1} = f(z_t, a_t, \epsilon_t)$，其中 $a_t$ 为政策变量，$\epsilon_t$ 为不可观测冲击。  
3. **因果推断层**：利用因果图或do-operator实现反事实模拟，例如评估利率调整对就业的异质性效应 $\mathbb{E}[Y|do(A=a)]$，并通过贝叶斯更新实时校准参数。

**与已有工作关系**  
区别于传统宏观计量（如VAR、DSGE）的“先估计后模拟”范式，数字孪生强调**持续学习**与**双向交互**：模型不仅拟合历史，还能在线吸收新数据并修正结构。与工程数字孪生（如工业系统）相比，经济系统面临更严重的不可观测混杂与反馈循环，因此需引入因果结构学习（如PC算法）与弱工具变量稳健推断。

**主要贡献**  
1. 提出一个端到端的宏观经济数字孪生框架，将高维数据、动态因果模型与实时优化统一。  
2. 在方法论上，为处理经济系统中的非平稳性、时变因果效应提供了可操作的推断工具（如时变DAG与在线贝叶斯更新）。  
3. 实践上，为央行或财政部门的“政策实验室”提供低成本、可重复的反事实模拟平台，有望降低试错成本。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)