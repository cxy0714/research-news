# 时间序列与时空 Time Series & Spatio-Temporal

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 20 场报告**（已检索到对应论文 6 场）

---

## Learning for Voice, Adversarials, Digital Twin and Changepoints

*7 月 11 日（周六） · 15:30-17:10 · Baihua Meeting Room*  
*组织 Songxi Chen（Tsinghua University） · 主持 Songxi Chen（Tsinghua University）*

### 1. Accent Matters: Communication Costs and Information Content in Analyst-Manager Dialogue

**讲者**：Feng Li（Peking University）

**对应论文**：Accent Matters: Communication Costs and Information Content in Analyst-Manager Dialogue · [论文/主页](https://doi.org/10.2139/ssrn.6087646)

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在分析师与公司管理层的电话会议对话中，口音（accent）是否以及如何影响信息传递效率？具体而言，管理层的口音会带来额外的“沟通成本”（communication costs），从而降低分析师从对话中提取的信息含量，并可能扭曲市场反应。现有文献多关注语言内容（如语调、模糊性）或非语言特征（如语速、停顿），但口音作为语音特征中不可忽视的异质性来源，其对信息经济后果的因果识别尚属空白。

**核心方法**  
讲者可能采用多模态计量框架：首先，利用语音识别与声学分析技术，从电话会议录音中提取管理层的口音特征（如元音空间、韵律偏差），构建口音强度指标（accent intensity）。其次，通过自然语言处理（NLP）度量分析师提问与经理回答之间的信息不对称程度，例如使用文本相似度或问答相关性得分。最后，将口音强度作为关键解释变量，在控制会议主题、公司基本面、分析师特征等固定效应后，估计口音对信息含量（如股价同步性、盈余预测修正幅度）的因果效应。为处理内生性，可能采用工具变量（如经理出生地或教育背景的方言距离）或准实验设计（如跨地区分析师与经理的配对差异）。

**与已有工作关系**  
已有研究（如Hobson et al., 2012; Mayew & Venkatachalam, 2012）关注语音情绪、语调对信息传递的影响，但均假设语音内容可被无成本解码。本报告将沟通成本从语义层面拓展至声学层面，引入“口音”这一被忽视的摩擦因素。此外，与语言学中“口音歧视”文献不同，本报告聚焦于信息经济学视角，量化口音如何通过增加认知负荷（cognitive load）降低信息提取效率，而非社会偏见。

**贡献**  
第一，首次系统识别口音在专业对话中的信息成本，为“软信息”传递的微观机制提供新证据。第二，方法上融合语音信号处理与因果推断，为会计与金融领域的语音分析研究提供可复现的范式。第三，实践上提示投资者和监管者：口音差异可能导致信息解读偏差，需在信息披露质量评估中纳入语音特征维度。


### 2. USAD: Uncertainty-Aware Statistical Adversarial Detection

**讲者**：Liuhua Peng（University of Melbourne）

**对应论文**：USAD: Uncertainty-aware Statistical Adversarial Detection · [arXiv:2606.27832](https://arxiv.org/abs/2606.27832) · 📖 [长篇精读](../../deep_reads/jcsds2026-2606.27832.md)

<details><summary>摘要（原文）</summary>

Statistical adversarial detection (SAD) treats detection as a two-sample test. Given a reference set of clean examples (CEs) and a batch of queries, potentially containing an unknown mixture of CEs and adversarial examples (AEs), SAD decides whether the query distribution drifts away from the CE distribution while controlling the false-alarm rate. Existing SAD-based methods mainly use maximum mean discrepancy (MMD) to measure the distributional discrepancy. However, MMD's distributional properties limit its ability to capture characteristic uncertainty patterns of AEs that are crucial for detection: AEs typically exhibit abnormal feature spread (i.e., global uncertainty) and instability under perturbations (i.e., local uncertainty). To close the gap, we propose Uncertainty-aware Statistical Adversarial Detection (USAD), which explicitly captures these uncertainty patterns with two new statistics: (1) Variance Discrepancy (VD), which measures the difference in feature spread between AEs and CEs to capture global uncertainty differences. (2) Perturbation-based Covariance Discrepancy (PCD), which compares feature covariance under Gaussian perturbations to capture local uncertainty differences. By aggregating VD and PCD, USAD achieves superior detection performances over baseline methods against various adversarial attacks, highlighting the importance of considering characteristic behaviors of AEs for effective SAD. Our code is available at: https://anonymous.4open.science/r/USAD.

</details>

**问题**  
现有统计对抗检测（SAD）将检测视为两样本假设检验：给定干净样本参考集 $X$ 与查询批 $Y$，检验 $H_0: P=Q$ 是否成立。主流方法采用最大均值差异（MMD）作为检验统计量。然而，MMD 主要捕捉分布间的均值嵌入差异（一阶矩），对对抗样本（AE）特有的不确定性模式——全局不确定性（特征分布离散度异常）与局部不确定性（对微扰动的敏感性）——不敏感。这导致 MMD 在查询批较小时检验功效急剧下降，限制了实际部署。

**核心方法**  
本文提出 USAD，显式构造两个新统计量：  
1. **方差差异（VD）**：比较干净样本与查询样本在语义特征空间中的方差 $V_P$ 与 $V_Q$，即 $\text{VD}(P,Q;\ell) = (V_P - V_Q)^2$，捕捉全局不确定性差异。  
2. **扰动协方差差异（PCD）**：对每个样本施加高斯扰动 $\delta \sim \mathcal{N}(0,\sigma^2 I)$，计算特征协方差矩阵 $\Sigma_x$，再比较两类样本的协方差分布均值嵌入，即 $\text{PCD}(P,Q,\rho) = \|\mu_{\Sigma_P} - \mu_{\Sigma_Q}\|^2_{\mathcal{H}_\rho}$，捕捉局部不确定性差异。  
两者通过相关性感知加权（基于干净校准集估计协方差结构 $\hat{\Sigma}_A$）聚合为单一检验统计量 $T^A$，再经置换检验控制第一类错误。

**与已有工作关系**  
现有 SAD 方法（如 SAMMD）依赖 MMD，本质是检验均值嵌入相等。本文指出 MMD 对二阶结构（方差、局部协方差）不敏感，而对抗攻击恰恰在这些几何特征上留下显著痕迹。USAD 直接针对这些特征设计统计量，弥补了 MMD 在捕捉不确定性模式上的根本缺陷，从而在小样本和混合场景下显著提升功效。

**贡献**  
1. 识别出 MMD 对 AE 不确定性模式不敏感是现有 SAD 样本效率低下的关键原因。  
2. 提出 VD 与 PCD 两个新统计量，分别刻画全局与局部不确定性差异，并通过相关性感知聚合实现自适应检测。  
3. 理论上证明 USAD 在置换检验下严格控制第一类错误（Theorem 1），且 VD、PCD 及 USAD 的检验功效随样本量趋于 1（Theorems 2–3, Corollary 4）。  
4. 实验表明，在 CIFAR-10 和 ImageNet 上，USAD 在查询批仅含 10 个样本时仍能达到近乎完美的检测功效，远超 MMD 基线，且对自适应攻击鲁棒。


### 3. Digital Twin for Behavior Change Interventions: A Case Study on HeartSteps Trials

**讲者**：Hang Zhou（UNC Chapel-Hill）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**：移动健康干预（如 HeartSteps 试验）中，行为干预的时机与内容需根据用户实时状态动态调整，但传统因果推断方法（如微随机试验 MRT 的边际结构模型）仅能估计平均处理效应，无法为每个用户提供实时、个性化的最优决策。如何利用用户历史数据与实时传感器信息构建“数字孪生”，以模拟不同干预策略下的潜在结果，并在线优化干预策略？

**核心方法**：讲者可能提出一个基于强化学习与因果推断的数字孪生框架。具体而言，利用 HeartSteps 试验的微随机数据，为每个用户训练一个个体化的状态转移模型（如隐马尔可夫模型或递归神经网络），该模型捕捉用户行为、环境特征与干预之间的动态因果关系。数字孪生体通过在线贝叶斯更新，实时拟合用户当前状态，并利用离线学习的因果效应估计（如基于 G-computation 或 doubly robust 估计）模拟“如果施加某干预，未来行为轨迹如何变化”。在此基础上，采用 Thompson 采样或上置信界算法选择当前最优干预，平衡探索与利用。

**与已有工作关系**：已有 MRT 分析主要关注事后因果推断（如加权估计方程），缺乏实时决策能力；而传统的数字孪生多用于工程系统（如数字孪生电网），较少涉及人类行为中的因果混淆与个体异质性。本工作将数字孪生引入行为干预，首次在 MRT 框架下结合在线学习与离线因果推断，并利用 HeartSteps 真实数据验证。相比单纯强化学习（如 contextual bandit），该方法显式建模干预的因果效应，避免混淆偏差，且能利用历史试验数据加速学习。

**贡献**：1）提出行为干预数字孪生的通用框架，将因果推断与在线学习无缝衔接；2）在 HeartSteps 数据上展示该方法可显著提升干预效果（如步数增加），同时降低用户负担；3）为移动健康领域提供一种可解释、可验证的个性化干预设计工具，推动因果推断从“事后分析”走向“实时决策”。


### 4. Spatial-Sign Based High Dimensional Change Point Inference

**讲者**：Long Feng（Nankai University）

**对应论文**：Spatial-Sign based High dimensional Change Point Inference · [arXiv:2504.19306](https://arxiv.org/abs/2504.19306) · 📖 [长篇精读](../../deep_reads/jcsds2026-2504.19306.md)

<details><summary>摘要（原文）</summary>

High-dimensional changepoint inference, adaptable to diverse alternative scenarios, has attracted significant attention in recent years. In this paper, we propose an adaptive and robust approach to changepoint testing. Specifically, by generalizing the classical mean-based cumulative sum (CUSUM) statistic, we construct CUSUM statistics based on spatial medians and spatial signs. We introduce test statistics that consider the maximum and summation of the CUSUM statistics across different dimensions, respectively, and take the maximum across all potential changepoint locations. The asymptotic distributions of test statistics under the null hypothesis are derived. Furthermore, the test statistics exhibit asymptotic independence under mild conditions. Building on these results, we propose an adaptive testing procedure that combines the max-$L_\infty$-type and max-$L_2$-type statistics to achieve high power under both sparse and dense alternatives. Through numerical experiments and theoretical analysis, the proposed method demonstrates strong performance and exhibits robustness across a wide range of signal sparsity levels and heavy-tailed distributions.

</details>

**问题**  
高维均值变点检测中，现有方法多基于样本均值构造CUSUM统计量，对重尾分布敏感，且难以同时适应稀疏强信号与密集弱信号两种备择模式。本文旨在提出一种对重尾数据鲁棒、且能自适应不同信号稀疏性的变点检验方法。

**核心方法**  
将经典均值CUSUM推广至基于空间符号（spatial sign）和空间中位数（spatial median）的版本。具体地，利用空间中位数构造 max‑L∞ 型统计量 $M_{n,p}$ 与 $M^\dagger_{n,p}$，对稀疏信号敏感；利用空间符号构造 max‑L2 型统计量 $S_{n,p}$ 与 $S^\dagger_{n,p}$，对密集信号有效。在推导出两类统计量的渐近零分布（均为Gumbel型）并证明其渐近独立性的基础上，采用Fisher方法组合对应p值，得到自适应检验 $p_{M,S}$ 与 $p_{M^\dagger,S^\dagger}$。

**与已有工作关系**  
已有自适应方法（如Wang & Feng, 2023）基于样本均值，在重尾分布下失效。本文将其框架推广至空间符号与空间中位数，首次将空间符号技术引入高维变点推断。此外，现有文献多研究Gumbel分布与正态分布之间的渐近独立性，本文首次建立了两个Gumbel型极限分布之间的渐近独立性，填补了理论空白。

**贡献**  
(1) 提出对重尾分布鲁棒的高维变点检验，同时保持对正态数据的可比效率；(2) 通过组合max‑L∞与max‑L2型统计量，实现对稀疏与密集信号的自适应，数值实验表明在多种分布下优于现有方法；(3) 理论上推导了统计量的渐近零分布、局部备择下的一致性，并建立了两个Gumbel型极限的渐近独立性，为高维极值理论提供了新工具。


## Time Series and Longitudinal Data and Bayesian Methods

*7 月 12 日（周日） · 15:30-17:10 · Executive Meeting Room, 12th Floor, Qunsheng Howard Johnson*  
*主持 Yiping Hong（Beijing Institute of Technology）*

### 1. On Ignorability of Preferential Sampling in Geostatistics

**讲者**：Ganggang Xu（University of Miami）

**对应论文**：On Ignorability of Preferential Sampling in Geostatistics · [arXiv:2511.03158](https://arxiv.org/abs/2511.03158) · 📖 [长篇精读](../../deep_reads/jcsds2026-2511.03158.md)

<details><summary>摘要（原文）</summary>

Preferential sampling has attracted considerable attention in geostatistics since the pioneering work of Diggle et al. (2010). A variety of likelihood-based approaches have been developed to correct estimation bias by explicitly modelling the sampling mechanism. While effective in many applications, these methods are often computationally expensive and can be susceptible to model misspecification. In this paper, we present a surprising finding: some existing non-likelihood-based methods that ignore preferential sampling can still produce unbiased and consistent estimators under the widely used framework of Diggle et al. (2010) and its extensions. We investigate the conditions under which preferential sampling can be ignored and develop relevant estimators for both regression and covariance parameters without specifying the sampling mechanism parametrically. Simulation studies demonstrate clear advantages of our approach, including reduced estimation error, improved confidence interval coverage, and substantially lower computational cost. To show the practical utility, we further apply it to a tropical forest data set.

</details>

**问题**：在地统计模型中，当采样位置与空间过程存在依赖（即 preferential sampling）时，传统似然方法（如 Diggle et al., 2010）需显式建模采样机制（如 log-Gaussian Cox process），但这类方法计算昂贵且易因模型误设而失效。本文核心问题是：在何种条件下，可以完全忽略采样机制，仍获得回归系数和协方差参数的一致估计？

**核心方法**：作者在 Diggle et al. (2010) 的框架下，允许潜在强度场 $X(s)$ 与标记过程 $Y(s)$ 具有任意各向同性交叉协方差 $C_{XY}(\|s-t\|)$，而非限制为比例关系 $X(s)=\gamma Y(s)$。主要发现：最小二乘估计 $\hat{\beta}$ 除截距项外仍无偏（截距偏差 $C_{XY}(0)$ 可校正），且其渐近正态性成立（Theorem 1）。对于协方差参数，基于残差的矩估计（sill $\omega$）和核平滑估计（半变异函数 $V_Y(r)$、交叉协方差 $C_{XY}(r)$）均保持相合（Theorem 2）。进一步，通过最小对比或复合似然目标函数，可对参数化协方差函数（如 Matérn）进行相合估计（Theorem 3），无需指定采样机制。

**与已有工作关系**：已有工作（如 Diggle et al., 2010; Pati et al., 2011）依赖对采样机制的完整参数化，且计算复杂度高（如 TMB 方法）。本文首次证明，在更一般的交叉协方差结构下，经典的非似然方法（最小二乘、矩估计）仍有效，从而避免了模型误设风险，并大幅降低计算成本（模拟中速度提升数百倍）。

**贡献**：1) 理论刻画了 preferential sampling 可被忽略的充分条件，即仅需交叉协方差函数存在且满足正则性；2) 提出一套无需参数化采样机制的估计流程，覆盖回归系数和协方差参数，并给出渐近推断；3) 通过模拟和热带森林数据验证了方法在偏差、覆盖率和计算效率上的优势，为实际应用提供了稳健且高效的替代方案。


### 2. Spherically Embedded Time Series with Unknown Trend and Periodic Components

**讲者**：Jiazhen Xu（Macquarie University）

**对应论文**：Spherically Embedded Time Series with Unknown Trend and Periodic Components · [arXiv:2604.03574](https://arxiv.org/abs/2604.03574) · 📖 [长篇精读](../../deep_reads/jcsds2026-2604.03574.md)

<details><summary>摘要（原文）</summary>

Spherically embedded time series are time series with values naturally residing on or can be equivalently mapped to the sphere. Despite their ubiquity in diverse scientific fields, these data frequently exhibit complex non-stationarity driven by latent trend and periodic components. Traditional Euclidean time series methods fail to account for the intrinsic non-Euclidean geometry of the sphere, leaving a critical gap in rigorous methodologies for modelling and forecasting nonstationary spherically embedded time series. To address this methodological gap, we propose a unified geometric framework to analyse nonstationary spherically embedded time series. Central to our approach is a novel nonparametric spherical trend-periodicity decomposition model that uses an optimal-transport-based removal operation to sequentially extract the smooth trend and periodic components while preserving spherical topology. The resulting de-trended and de-seasonalised stationary residuals can be further modelled using a spherical autoregressive model, formalising a novel trend-periodic spherical autoregressive model. Theoretical foundations for the modelling procedure are established on the consistency under temporal dependence. Extensive simulations corroborate these theoretical guarantees and demonstrate the superior finite-sample predictive performance of the trend-periodic spherical autoregressive model. Finally, we validate the practical utility of our methodology through applications to electricity generation compositions and bike trip volume profiles, yielding significantly enhanced forecasting accuracy while providing interpretable insights into the underlying structural dynamics.

</details>

**问题**：球面嵌入时间序列（如方向数据、成分数据、分布数据）广泛存在于能源经济、城市信息学等领域，但常受未知趋势和周期成分驱动而呈现非平稳性。现有球面自回归模型（Zhu & Müller, 2024）假设平稳性，无法识别或解耦这些潜在结构；而欧氏空间中的加减法在球面上无定义，导致传统分解方法失效。因此，亟需一个能同时处理非平稳趋势和周期成分的球面时间序列建模框架。

**核心方法**：提出球面趋势-周期分解（STPD）模型。核心创新在于利用最优传输定义球面“移除”操作 $M_{\nu_2 \to \nu_1}(\nu_3)$，该操作将 $\nu_2$ 移至 $\nu_1$ 所需的旋转速度施加于参考点 $\nu_3$，从而在保持球面拓扑的前提下实现成分分离。具体分两步：① 用局部 Fréchet 回归估计光滑趋势 $\hat{f}(t/T)$，并通过移除操作得到去趋势序列；② 对去趋势序列，用全局 Fréchet 回归和惩罚残差平方和（含信息准则）估计未知周期 $\hat{\vartheta}$ 及周期成分 $\hat{g}(t)$，再次移除得到平稳残差。最后对残差拟合球面 AR 模型（TPSAR），实现预测。

**与已有工作关系**：本文是首个处理球面嵌入时间序列中未知趋势与周期成分的统一框架。相比 Zhu & Müller (2024) 的球面 AR 模型，本文通过 STPD 分解将非平稳序列转化为平稳残差，从而扩展了球面 AR 的适用范围；相比 Wasserstein AR 模型（仅适用于分布数据），本文方法可同时处理方向、成分和分布数据。理论方面，将局部 Fréchet 回归和周期量化的相合性结果从独立情形推广到 $\alpha$-混合时间依赖情形，填补了非欧时间序列非平稳建模的理论空白。

**贡献**：① 提出 STPD 模型，首次系统解耦球面时间序列的趋势、周期与随机成分；② 建立 TPSAR 半参数模型，兼具可解释性与预测能力；③ 证明趋势、周期及 AR 系数估计量的相合性，给出收敛速率；④ 模拟与实证（美国电力成分、纽约自行车流量分布）表明，TPSAR 在预测精度上显著优于现有球面 AR 及差分球面 AR 模型，并揭示出有意义的潜在结构动态。


### 3. The Empirical Bayes Estimators of the Variance Parameter of the Normal Distribution with a Normal-Inverse-Gamma Prior Under Stein's Loss Function

**讲者**：Yingying Zhang（Yunnan University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在正态分布 $N(\mu, \sigma^2)$ 中，方差参数 $\sigma^2$ 的估计是经典问题，但传统估计（如样本方差）在 Stein 损失函数 $L(\hat{\sigma}^2, \sigma^2) = \hat{\sigma}^2/\sigma^2 - \log(\hat{\sigma}^2/\sigma^2) - 1$ 下并非最优。该损失函数对低估惩罚更重，且与似然比检验、信息几何有深刻联系。当先验信息存在时，Bayes 估计可改善性能，但先验超参数未知时需借助 Empirical Bayes (EB) 方法。本报告聚焦于在 Normal-Inverse-Gamma (NIG) 先验 $\sigma^2 \sim \text{IG}(a, b), \mu|\sigma^2 \sim N(\mu_0, \sigma^2/\kappa)$ 下，如何构造 $\sigma^2$ 的 EB 估计量并研究其在 Stein 损失下的风险性质。

**核心方法**  
首先推导在 NIG 先验下 $\sigma^2$ 的 Bayes 估计量（后验均值或后验众数）在 Stein 损失下的闭式解。由于超参数 $(a, b, \mu_0, \kappa)$ 未知，利用边际似然（即观测数据 $X_1,\dots,X_n$ 的分布）通过矩估计或极大似然估计得到超参数的估计值，代入 Bayes 估计量得到 EB 估计量。关键步骤是分析 EB 估计量的风险函数，可能借助 Stein 的无偏风险估计 (SURE) 或数值模拟，并与经典估计（如样本方差、最小方差无偏估计）及完全 Bayes 估计（固定超参数）进行比较。此外，可能推导出 EB 估计量在特定条件下（如 $n$ 较大时）的渐近最优性。

**与已有工作关系**  
已有文献对正态均值的 EB 估计研究充分（如 James-Stein 估计），但对方差参数的 EB 估计关注较少。经典方差估计在 Stein 损失下的 minimax 估计已有结果（如 Strawderman 1974），但多采用倒 Gamma 先验的 Bayes 方法。本报告将 EB 思想引入方差参数，并采用更灵活的 NIG 先验（同时建模均值和方差的不确定性），拓展了应用场景。与完全 Bayes 方法相比，EB 避免了主观选择超参数的困难；与频率学派方法相比，EB 可能获得更小的风险。

**贡献**  
1. 首次系统研究 NIG 先验下 $\sigma^2$ 在 Stein 损失下的 EB 估计，给出显式或近似表达式。  
2. 理论证明 EB 估计量的风险优于经典样本方差估计，并在一定条件下达到渐近最优。  
3. 通过数值模拟展示 EB 估计在有限样本下的稳健性和效率提升，尤其当均值 $\mu$ 也未知时。  
4. 为高维或分层模型中方差分量的估计提供新工具，推动 Empirical Bayes 在方差推断中的应用。


### 4. 二元Marshall-Olkin瑞利分布的参数估计

**讲者**：Xiang Xiao（Shanghai University of Engineering Science）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
Marshall-Olkin 型分布是刻画多元寿命数据相依性的经典模型，其核心特征是通过“冲击”机制同时诱发多个变量的失效，导致联合分布包含奇异部分。现有工作多聚焦于指数或 Weibull 分布，而瑞利分布（Rayleigh distribution）作为 Weibull 分布形状参数固定为 2 的特例，在可靠性工程中广泛用于描述磨损失效。然而，二元 Marshall-Olkin 瑞利分布的参数估计尚未得到系统研究，主要困难在于：似然函数因奇异部分而复杂，且瑞利分布尺度参数与冲击参数耦合，传统 MLE 的显式解难以获得。

**核心方法**  
报告拟提出一种基于 EM 算法的极大似然估计方案。将冲击发生与否视为潜在变量，构造完整数据似然函数，使得 E 步中可解析计算冲击指示的条件期望；M 步则转化为两个独立的瑞利分布尺度参数估计问题，从而得到迭代更新的闭式表达式。此外，可能利用瑞利分布与卡方分布的关系，推导出矩估计作为初始值，以加速 EM 收敛。对于小样本情形，或许引入 Bootstrap 偏差校正。

**与已有工作关系**  
已有文献对 Marshall-Olkin 指数分布（Marshall & Olkin, 1967）及 Weibull 分布（Kundu & Dey, 2009）的估计已有成熟结果，但瑞利分布的特殊性（形状参数已知）使得似然函数结构更简单，却也导致冲击参数与尺度参数的可识别性条件发生变化。本报告填补了这一特例的空白，并可能证明在形状参数固定时，EM 算法具有比一般 Weibull 情形更快的收敛速度。

**贡献**  
1. 首次给出二元 Marshall-Olkin 瑞利分布参数 MLE 的 EM 算法，并证明其收敛性。  
2. 推导出参数估计的渐近正态性及协方差矩阵的显式表达式，便于区间估计。  
3. 通过数值模拟验证算法在有限样本下的优良表现，并与基于 copula 的伪似然方法对比，展示所提方法在相依性较强时的效率优势。  
4. 为实际工程中二元磨损寿命数据的建模提供一套完整的推断工具。


### 5. Statistical Inference for Coefficients and Trend Function in Time-Varying GARCH Model

**讲者**：Ziyi Zou（Fuzhou University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
经典 GARCH 模型假设条件方差方程中的系数为常数，但金融时间序列常呈现结构突变或缓慢漂移，此时常系数设定会带来模型误设。本报告关注 **Time-Varying GARCH (TV-GARCH)** 模型，允许自回归系数与波动率趋势函数随时间平滑变化，并聚焦于如何对时变系数和趋势函数进行有效的统计推断（如置信区间、假设检验），而非仅做点估计。

**核心方法**  
报告采用 **局部平稳性 (local stationarity)** 框架，将 TV-GARCH 视为一类局部平稳过程。通过 **核加权局部拟似然 (kernel-weighted local quasi-likelihood)** 估计时变参数，即在每个时间点 $t/T$ 附近使用核函数对观测值加权，最大化局部拟似然函数得到系数 $\alpha(u), \beta(u)$ 与趋势函数 $c(u)$ 的估计 $\hat{\alpha}(u), \hat{\beta}(u), \hat{c}(u)$，其中 $u \in [0,1]$ 为标准化时间。在此基础上，推导估计量的联合渐近正态性，并构造逐点置信区间与同时置信带 (simultaneous confidence band)。为处理边界偏差，可能采用边界核或局部线性修正。

**与已有工作关系**  
现有文献对时变 GARCH 的研究多集中于参数化时变（如分段常数、线性趋势）或非参数估计但缺乏推断理论。本报告区别于：1) 常系数 GARCH 的推断方法（如 Bollerslev & Wooldridge 1992）；2) 仅关注波动率趋势函数而非系数的非参数模型（如 Fan & Yao 2003）；3) 参数时变 GARCH 的似然比检验。报告将非参数时变系数与趋势函数的联合推断纳入统一框架，填补了 TV-GARCH 模型统计推断的理论空白。

**主要贡献**  
1) 首次为 TV-GARCH 模型中的时变系数和趋势函数提供完整的渐近推断理论，包括估计量的收敛速率与渐近分布。  
2) 提出同时置信带的构造方法，可检验系数是否随时间恒定（如 $H_0: \alpha(u)=\alpha$），或趋势函数是否具有特定形状。  
3) 通过模拟与实证（如股票指数日收益率）展示方法在有限样本下的表现，揭示金融波动率中显著的时变特征，为风险管理和波动率预测提供更可靠的统计工具。


### 6. Fisher Scoring for Exact Matérn Covariance Estimation through Stable Smoothness Optimization

**讲者**：Yiping Hong（Beijing Institute of Technology）

**对应论文**：Fisher Scoring for Exact Matérn Covariance Estimation through Stable Smoothness Optimization · [arXiv:2601.11437](https://arxiv.org/abs/2601.11437) · 📖 [长篇精读](../../deep_reads/jcsds2026-2601.11437.md)

<details><summary>摘要（原文）</summary>

Gaussian Random Fields (GRFs) with Matérn covariance functions have emerged as a powerful framework for modeling spatial processes due to their flexibility in capturing different features of the spatial field. However, the smoothness parameter is challenging to estimate using maximum likelihood estimation (MLE), which involves evaluating the likelihood based on the full covariance matrix of the GRF, due to numerical instability. Moreover, MLE remains computationally prohibitive for large spatial datasets. To address this challenge, we propose the Fisher-BackTracking (Fisher-BT) method, which integrates the Fisher scoring algorithm with a backtracking line search strategy and adopts a series approximation for the modified Bessel function. This method enables an efficient MLE estimation for spatial datasets using the ExaGeoStat high-performance computing framework. Our proposed method not only reduces the number of iterations and accelerates convergence compared to derivative-free optimization methods but also improves the numerical stability of the smoothness parameter estimation. Through simulations and real-data analysis using a soil moisture dataset covering the Mississippi River Basin, we show that the proposed Fisher-BT method achieves accuracy comparable to existing approaches while significantly outperforming derivative-free algorithms such as BOBYQA and Nelder-Mead in terms of computational efficiency and numerical stability.

</details>

**问题**  
空间统计中，Matérn 协方差函数的平滑参数 $\nu$ 的精确极大似然估计（MLE）长期面临数值不稳定与计算瓶颈：似然面在 $\nu$ 方向近乎平坦，且 $\nu$ 的梯度涉及修正 Bessel 函数 $\mathcal{K}_\nu$ 的导数，有限差分易引入舍入误差；同时，精确 MLE 需对 $n\times n$ 协方差矩阵求逆，$O(n^3)$ 复杂度使大规模数据难以处理。现有软件多采用 BOBYQA、Nelder–Mead 等无导数优化，虽规避了导数计算，却忽略了似然的可微结构，导致迭代次数多、收敛慢，且对极端 $\nu$ 值（如 $\nu<0.1$ 或 $\nu>1$）估计不稳定。

**核心方法**  
本文提出 **Fisher-BackTracking (Fisher-BT)** 算法，将 Fisher scoring 与回溯线搜索（Armijo 条件）结合，并引入 Nelder–Mead 回退机制。Fisher scoring 利用期望 Fisher 信息矩阵 $I(\theta)$ 构造更新方向 $\phi^{(t)} = I(\theta^{(t)})^{-1}\nabla\ell(\theta^{(t)})$，充分利用似然的二阶统计结构以加速收敛。为稳定 $\nu$ 的导数计算，采用 Geoga et al. (2023) 的级数近似算法计算 $\partial_\nu \mathcal{K}_\nu$，避免有限差分。回溯线搜索在每一步动态调整步长，防止大 $\nu$ 时更新过冲；当 Fisher scoring 因数值问题无法收敛时（如 $\nu$ 极值），自动切换至 Nelder–Mead 作为安全网。算法集成于 ExaGeoStat 高性能计算框架，通过并行稠密线性代数库实现 $O(n^2)$ 内存与 $O(n^3)$ 运算的加速。

**与已有工作关系**  
已有精确 MLE 软件（如 fields、ExaGeoStat）依赖 BOBYQA 或 Nelder–Mead 等无导数方法，未利用似然可微性；BFGS 虽用梯度，但不涉及 $\nu$ 的 MLE 且忽略 Fisher 信息结构。Fisher scoring 此前仅用于近似 MLE（如 Vecchia 近似），因 $\nu$ 导数不稳定而未用于精确 MLE。本文首次将 Fisher scoring 与稳定级数近似结合，并针对大 $\nu$ 的数值不稳定性设计回溯与回退策略，填补了精确 MLE 中导数优化方法的空白。

**贡献**  
1. 提出首个用于 Matérn 精确 MLE 的 Fisher scoring 算法，通过级数近似稳定 $\nu$ 导数，显著减少似然函数调用次数（相比 BOBYQA 降低 50%–80%），计算时间大幅缩短。  
2. 回溯线搜索与 Nelder–Mead 回退机制使算法在 $\nu\in[0.05,1.3]$ 宽范围内保持数值稳定，估计方差小于无导数方法，且避免极端离群值。  
3. 借助 ExaGeoStat 框架，方法可处理 $n$ 达数万至百万的观测，在密西西比河流域土壤湿度数据上验证了精度与效率的优越性。


## Advances in Bayesian Methods and State-Space Models

*7 月 12 日（周日） · 13:30-15:10 · Meeting Room, 1st Floor, Qunsheng Garden Hotel*  
*主持 Changqing Lu（Central South University）*

### 1. A General Weighted Block Ensemble Kalman Filter with Data-Driven Optimal Block-Width Selection

**讲者**：Lei Qian（Peking University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维非线性状态空间模型中的状态估计是数据同化与信号处理的核心挑战。传统 Ensemble Kalman Filter (EnKF) 通过蒙特卡洛样本近似协方差，但在高维或非平稳场景下，样本协方差噪声大、局部相关性难以捕捉，且固定块结构（如分块对角）缺乏适应性。本报告旨在解决：如何通过数据驱动方式自适应选择块宽度，并引入加权机制以提升 EnKF 在高维、非高斯或稀疏观测下的估计精度与计算效率。

**核心方法**  
提出一种 **General Weighted Block Ensemble Kalman Filter (GW-BEnKF)**。其核心思想是：将状态变量划分为若干块，每块内采用局部 EnKF 更新，块间通过加权融合实现全局一致性。块宽度（即每块包含的变量数）不再由先验知识固定，而是基于数据驱动准则（如交叉验证、最小化预测误差或贝叶斯信息准则）自动选择。具体地，对每个候选块宽度，计算局部 EnKF 的更新后验，再以加权平均（权重与局部似然或后验方差成反比）整合全局估计。该方法可视为对标准 EnKF 的“分而治之”扩展，同时避免了传统分块方法中块边界处的不连续性。

**与已有工作关系**  
已有工作包括：标准 EnKF（Evensen, 1994）、局部化 EnKF（Houtekamer & Mitchell, 1998）以及分块 EnKF（如 Block EnKF, 2010）。局部化 EnKF 通过距离衰减函数截断协方差，但需预设半径；分块 EnKF 固定块结构，无法适应异质性。本报告的新颖之处在于：① 将块宽度视为超参数，通过数据驱动自动选择，而非人工设定；② 引入加权机制，允许不同块对最终估计的贡献随局部数据质量动态调整，从而提升鲁棒性；③ 理论上可能证明加权平均可降低均方误差，且计算复杂度与块数线性相关，适合大规模问题。

**贡献**  
主要贡献有三点：第一，提出一种自适应块宽度选择方法，将模型选择思想融入 EnKF 框架，解决了传统分块方法中块大小依赖先验的痛点；第二，加权融合策略使得算法对非平稳性和异常观测具有韧性，拓展了 EnKF 在非高斯场景下的适用性；第三，通过数值实验（如 Lorenz 96 模型或大气数据同化）展示，GW-BEnKF 在估计精度和计算时间上优于标准 EnKF 和固定块 EnKF，尤其在高维稀疏观测下优势显著。该工作为高维状态估计提供了一种灵活、自动化的工具，并启发了数据同化与机器学习交叉的新方向。


### 2. Data Integration of Non-Probability and Probability Samples Using Deep Generative Model

**讲者**：Tongxin Wang（Shanxi University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在调查统计中，概率样本（probability sample）具有严格随机性、可做无偏推断，但成本高、样本量有限；非概率样本（non-probability sample，如网络爬取数据）量大但存在未知选择偏差。如何有效整合两类样本，在控制偏差的同时提升估计精度，是当前数据融合的核心挑战。传统方法（如逆概率加权、倾向得分校准）依赖对选择机制的显式建模，当协变量维度高、关系非线性时易出现模型误设。

**核心方法**  
报告提出利用深度生成模型（Deep Generative Model, DGM）来联合建模概率样本与非概率样本的生成过程。具体而言，假设存在潜在变量 $Z$ 控制观测协变量 $X$ 与样本选择指示 $S$（$S=1$ 表示概率样本，$S=0$ 表示非概率样本），DGM（如变分自编码器或生成对抗网络）学习 $p(X, S)$ 的联合分布，并通过对抗性训练或重要性加权使非概率样本的 $X$ 分布向概率样本的 $X$ 分布对齐。最终利用对齐后的非概率样本扩充有效样本量，对目标量（如总体均值 $\mu$）进行加权估计，权重由 DGM 隐式推断的选择概率 $P(S=1|X)$ 给出。

**与已有工作关系**  
现有数据整合方法多基于参数化倾向得分模型（如 logistic regression）或核方法，对高维、非线性协变量适应性弱。深度生成模型在此场景的应用尚处早期：部分工作使用 GAN 进行分布匹配但未显式建模选择机制，或仅用于缺失数据填补。本报告将 DGM 同时用于选择机制学习与分布对齐，并利用概率样本的“黄金标准”特性进行校准，是对传统加权方法的非参数化扩展。

**主要贡献**  
1. 提出一个端到端的深度生成框架，无需预设选择模型形式，自动从数据中学习复杂选择偏差。  
2. 通过潜在变量结构，可自然处理协变量缺失或测量误差问题，提升实际应用鲁棒性。  
3. 在模拟与真实数据上展示相比现有方法（如 IPW、calibration weighting）更低的均方误差，尤其在样本量差异大或协变量维度高时优势显著。  
4. 为因果推断中非概率样本的整合提供了新工具，拓展了深度生成模型在 survey sampling 领域的应用边界。


### 3. Predicting Average Daily Liveweight Gain in Grazing Cattle from Accelerometer-Derived Behaviour and Activity

**讲者**：Shuwen Hu（Royal Melbourne Institute of Technology,RMIT）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
放牧牛的日均增重（Average Daily Liveweight Gain, ADG）是衡量养殖效益的关键指标，传统上依赖定期称重，成本高、应激大且难以高频监测。本报告旨在利用佩戴于牛颈或腿部的加速度计（accelerometer）所采集的连续行为与活动数据，构建统计模型以预测ADG，从而为精准畜牧业提供非侵入式的替代方案。

**核心方法**  
报告可能采用两阶段建模策略。第一阶段，从加速度计原始三轴信号中提取行为分类特征（如站立、行走、采食、反刍的时间占比）及活动量指标（如步数、加速度幅值的均值与方差、频域能量）。第二阶段，将这些高维特征作为预测变量，以ADG为响应变量，建立回归模型。考虑到数据具有个体重复测量和时序相关性，方法可能包括：  
- 使用**随机森林**或**梯度提升机**处理非线性关系与特征交互；  
- 引入**线性混合模型**（LMM）或**广义加性模型**（GAM）以刻画个体随机截距与时间趋势；  
- 通过**交叉验证**与**正则化**（如Lasso）进行变量选择，避免过拟合。  
关键假设是行为模式与能量收支直接关联，从而间接反映增重。

**与已有工作关系**  
已有研究多聚焦于利用加速度计识别牛的行为类别（如采食、反刍），或单独分析活动量与能量消耗的关系，但鲜有直接预测ADG的端到端模型。本报告将行为识别与增重预测整合，填补了从传感器信号到经济性状的预测链路。相较于传统基于饲料摄入量或代谢体重的方法，本方法无需人工观测或侵入式设备，且可提供连续、实时的增重估计。

**贡献**  
1. **方法论创新**：提出一套从加速度计特征到ADG的统计预测框架，融合行为分类与活动量指标，可能揭示不同行为对增重的差异化贡献（如采食时间比步数更具预测力）。  
2. **实践价值**：为放牧场景下的个体增重监测提供低成本、高频率的解决方案，助力精准饲养与早期健康预警。  
3. **统计启示**：通过对比不同模型（如线性 vs. 树集成）的预测性能，可评估行为-增重关系的线性假设是否合理，并为高维时序数据的降维与建模提供案例。


### 4. Equilibrium Joining Strategies in a Two-Stage Service System with Priority Customers and Feedback

**讲者**：Jia Xu（Chaohu University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在具有优先顾客（Priority Customers）与反馈（Feedback）的两阶段服务系统中，顾客需决定是否加入系统，且加入后可能因服务不满意而重复排队（反馈）。优先顾客享有插队权，这改变了普通顾客的等待成本与收益权衡。报告旨在刻画两类顾客（优先与普通）在非合作博弈下的均衡加入策略，即每个顾客基于对系统状态的理性预期，选择“加入”或“放弃”的阈值策略，并求解该阈值在稳态下的纳什均衡。

**核心方法**  
采用连续时间马尔可夫链（CTMC）建模系统状态（各阶段队列长度），将顾客的决策建模为基于个人收益的博弈。利用“收益-成本”框架：顾客加入的期望净收益 = 服务价值 \(R\) - 期望等待时间成本（与队列长度和优先权相关）。通过求解稳态概率分布，推导出普通顾客与优先顾客的均衡阈值 \(n^*\) 与 \(m^*\)，使得当队列长度低于阈值时加入，否则放弃。方法本质是固定点方程：给定对方策略，个体最优策略与系统稳态分布自洽。

**与已有工作关系**  
经典排队博弈（如Naor模型）仅考虑单阶段、无优先权或简单反馈。已有两阶段模型（如串联队列）多假设顾客一次性通过，未考虑反馈与优先插队。本报告将优先权与反馈同时引入两阶段系统，扩展了“Join-or-Balk”博弈的适用范围。此外，与仅考虑社会最优的文献不同，本报告聚焦个体理性下的纳什均衡，并比较其与社会最优的差异。

**主要贡献**  
1. 首次给出含优先顾客与反馈的两阶段服务系统中均衡加入策略的显式或半显式解，揭示优先权如何扭曲普通顾客的加入阈值。  
2. 证明均衡存在唯一性条件，并分析系统参数（如服务率、反馈概率）对均衡阈值与系统吞吐量的影响。  
3. 为服务系统设计（如是否允许优先插队）提供博弈论视角的定量指导，例如发现优先权可能降低总社会福利，但提升优先顾客的个体效用。


### 5. Modified Cholesky Decomposition-Based Localization in Ensemble Kalman Filter

**讲者**：HaoXuan Sun（Harbin Institute of Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
Ensemble Kalman Filter (EnKF) 在高维数据同化中面临样本协方差矩阵的虚假远距离相关，导致滤波发散或精度下降。传统 localization 方法（如距离截断、Gaspari–Cohn 函数）通过乘性 Schur product 强制稀疏化，但依赖预设的截断半径，且可能破坏协方差矩阵的正定性或引入结构偏差。本报告旨在解决：能否利用 Modified Cholesky Decomposition (MCD) 实现一种数据驱动的、自适应的 localization 策略，在保持正定性的同时更精准地抑制虚假相关？

**核心方法**  
报告提出基于 MCD 的 EnKF 局地化方案。MCD 通过对样本协方差矩阵进行 Cholesky 分解，并对 Cholesky 因子施加稀疏约束（如 $\ell_1$ 惩罚或顺序条件回归），得到稀疏的下三角矩阵 $L$，使得 $\hat{\Sigma} = L L^\top$ 为稀疏且正定的协方差估计。在 EnKF 分析步中，用该稀疏协方差替代原始样本协方差，从而自然实现 localization：仅保留 Cholesky 因子中非零元素对应的变量间条件依赖关系，远距离变量因条件独立而被自动截断。该方法无需预设距离阈值，而是通过数据自适应地选择稀疏模式。

**与已有工作关系**  
传统 EnKF localization 多采用乘性方法（如 Schur product with a correlation function），其稀疏结构由距离函数硬性决定，无法适应非各向同性的相关结构。另有一些基于正则化协方差估计的方法（如 graphical lasso），但计算成本高且难以保证 Cholesky 分解的序贯性。MCD 方法本质上是将协方差估计的稀疏化与 Cholesky 分解的序贯性结合，既保留了 EnKF 的序贯更新框架，又通过条件回归的稀疏性实现了自适应 localization，在计算效率与灵活性之间取得平衡。

**主要贡献**  
1. 提出一种新的 EnKF localization 框架，将 MCD 的稀疏协方差估计直接嵌入滤波更新，避免了传统乘性 localization 对正定性的破坏。  
2. 通过数据驱动的方式自动确定局地化范围，无需手动调参，尤其适用于非平稳或各向异性的空间场。  
3. 理论分析了 MCD 稀疏因子在 EnKF 中的误差传播性质，并给出计算复杂度（$O(np^2)$ 可降至 $O(n \log p)$ 在稀疏假设下），为高维应用提供了可行性保障。


### 6. Bayesian Inference for Independent Cluster Point Processes

**讲者**：Changqing Lu（Central South University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
独立簇点过程（Independent Cluster Point Processes）是一类重要的点过程模型，其中事件点由相互独立的簇中心及其附属子点构成，广泛应用于空间统计、流行病学与神经科学等领域。然而，其似然函数通常涉及对不可观测的簇中心与簇结构的积分，导致计算困难；现有推断方法多依赖频率学派或近似贝叶斯计算，难以在保持统计效率的同时处理大规模数据或复杂簇结构。本报告旨在解决：如何为独立簇点过程设计一种计算可行且理论严谨的贝叶斯推断框架，以同时估计簇参数与潜在簇分配。

**核心方法**  
讲者可能采用数据增广（data augmentation）策略，将未观测的簇中心与簇标签视为潜在变量，构建完整的层次贝叶斯模型。通过引入共轭先验或条件共轭结构（如对簇内子点强度使用Gamma先验，对簇中心位置使用Dirichlet过程先验），推导出易于采样的全条件分布，进而利用Gibbs采样或Hamiltonian Monte Carlo进行后验推断。为应对高维或大规模数据，可能进一步结合分治策略（divide-and-conquer）或变分贝叶斯近似，将全局推断分解为独立簇的局部更新，从而降低计算复杂度。

**与已有工作关系**  
已有工作多聚焦于特定子类，如Neyman-Scott过程或泊松簇过程，且推断方法常依赖矩估计或EM算法，难以量化不确定性。本报告将独立簇点过程推广至更一般的簇结构（如允许簇内点分布非泊松、簇大小随机），并首次系统性地提出贝叶斯框架。与基于MCMC的通用点过程推断（如Møller & Waagepetersen, 2004）相比，本方法利用簇间独立性简化了联合后验的采样，避免了全局点过程似然的昂贵计算；与近年来的变分推断方法（如Lloyd et al., 2015）相比，本报告可能更注重后验分布的精确性而非近似速度。

**贡献**  
主要贡献包括：（1）为独立簇点过程建立了一个灵活的贝叶斯建模框架，可容纳多种簇内点分布与先验设定；（2）开发了高效的计算算法，通过条件独立结构实现线性时间复杂度的后验采样，适用于大规模空间数据；（3）在模拟与真实数据上验证了方法在参数估计与簇恢复方面的优越性，尤其在高噪声或簇重叠场景下优于现有频率学派方法；（4）提供了后验一致性理论结果，为贝叶斯推断的可靠性提供了理论支撑。


## Recent Advances in Statistical Inference for Complex Dynamic Data

*7 月 13 日（周一） · 15:30-17:10 · Baihua Meeting Room*  
*组织 Yao Hu（Guizhou University） · 主持 Yao Hu（Guizhou University）*

### 1. A Class of Threshold Autoregressive Interval Model with a Dynamic Threshold Driven by Explanatory Variables

**讲者**：Kai Yang（Changchun University of Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
经典阈值自回归（TAR）模型假设阈值为常数或仅由滞后内生变量决定，难以刻画外部经济、气候等解释变量对机制切换的时变影响。同时，现有区间时间序列模型（如区间ARIMA）通常将区间上下界视为独立序列或直接对区间中点与半径建模，忽略了区间内部结构可能存在的非线性阈值效应。本报告旨在提出一类**动态阈值驱动的区间自回归模型**，允许阈值本身随外生解释变量线性或非线性变化，从而更灵活地捕捉区间值数据中的机制转换行为。

**核心方法**  
模型设定为：  
\[
Y_t = \begin{cases} 
\phi_1' X_t + \varepsilon_{1t}, & \text{if } Z_t \leq \gamma(W_t) \\
\phi_2' X_t + \varepsilon_{2t}, & \text{if } Z_t > \gamma(W_t)
\end{cases}
\]  
其中 $Y_t$ 为区间值响应（如 $[L_t, U_t]$），$X_t$ 包含自回归项与外生变量，$Z_t$ 为阈值变量，$\gamma(W_t)$ 为动态阈值函数（例如 $\gamma(W_t)=W_t'\theta$），$W_t$ 为驱动解释变量。估计可采用拟极大似然或贝叶斯方法，并利用网格搜索或MCMC处理阈值参数的非光滑性。模型允许区间上下界共享同一阈值机制，也可分别设定不同阈值。

**与已有工作关系**  
相比 Tong (1978) 的经典 TAR 模型，本工作将常数阈值推广为解释变量的线性/非线性函数，类似 Chan & Tong (1986) 的平滑转移自回归（STAR）但保留离散跳跃结构。与区间时间序列文献（如 Maia et al., 2008）相比，首次将阈值非线性引入区间建模，而非仅对均值或方差建模。此外，动态阈值设计借鉴了“阈值变量外生化”的思想（如 Hansen, 2000），但针对区间数据提出了新的估计与推断框架。

**贡献**  
1. 提出一类兼具区间数据特征与动态阈值非线性的新模型，拓展了阈值自回归的适用范围。  
2. 给出模型的可识别性条件与参数估计方法，并证明估计量的相合性与渐近正态性（在合理正则条件下）。  
3. 通过模拟与实证（如金融区间波动、气象区间预测）展示模型在拟合与预测上的优势，为区间值时间序列分析提供了新的非线性工具。


### 2. Parameter Estimation for High-Dimensional State-Space Model via Ensemble Kalman Filter

**讲者**：Yang Sun（Peking University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维状态空间模型（State-Space Model, SSM）的参数估计是时间序列分析与动态系统建模的核心难题。当状态维度 $p$ 远大于观测长度 $T$ 时，传统极大似然估计（如EM算法）或贝叶斯方法（如粒子MCMC）面临“维数灾难”：高维状态的后验采样需要指数级粒子数，且参数似然面崎岖不平，导致计算成本不可承受。本报告聚焦于如何利用Ensemble Kalman Filter（EnKF）这一高效状态滤波工具，同时实现未知参数（如转移矩阵、噪声协方差）的在线或离线估计。

**核心方法**  
报告提出一种基于EnKF的联合状态-参数估计框架。核心思路是将参数 $\theta$ 视为“伪状态”，通过增广状态向量 $\mathbf{z}_t = (\mathbf{x}_t, \theta_t)$ 将参数估计转化为状态滤波问题。具体地，利用EnKF的集合传播机制：在预测步，对参数施加人工动态（如随机游走 $\theta_t = \theta_{t-1} + \eta_t$）以保持多样性；在更新步，利用观测 $\mathbf{y}_t$ 同时校正状态与参数。为避免参数集合退化，可能引入协方差膨胀（covariance inflation）或局部化（localization）技术，并采用迭代更新策略（如Iterated EnKF）以处理参数与状态的非线性耦合。

**与已有工作关系**  
现有参数估计方法主要分为两类：一是基于粒子滤波的SMC²（粒子MCMC），虽理论精确但高维下粒子数指数增长；二是基于变分贝叶斯或EM的近似推断，但需解析梯度且对模型形式敏感。本报告的方法属于“集成卡尔曼平滑”家族，与Stroud & Bengtsson (2007) 的EnKF参数估计一脉相承，但针对高维场景做了关键改进：通过自适应协方差膨胀和分块局部化，缓解了增广状态维度升高带来的集合协方差估计偏差。相比近期流行的“可微分EnKF”（DEnKF），本方法无需自动微分，更适用于黑箱模型。

**主要贡献**  
1. 提出一种计算高效的在线参数估计算法，单步复杂度为 $O(N p)$（$N$ 为集合大小），远低于粒子滤波的 $O(N^p)$，使高维SSM的参数估计成为可能。  
2. 理论分析了增广EnKF的渐近偏差，并给出保证参数一致性的充分条件（如参数动态噪声的衰减率）。  
3. 在数值实验中（如气候模型、神经信号解码），展示了该方法在 $p \sim 10^3$ 量级下仍能准确恢复参数，且对模型误设定具有鲁棒性。  
4. 为后续研究提供了开源实现与基准测试，推动了EnKF从纯状态滤波向参数推断的实用化转型。


### 3. Hierarchical Gaussian Markov Random Field Modeling of Finite Element Models with Boundary Conditions

**讲者**：Yan Wang（Beijing University of Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
有限元模型（Finite Element Model, FEM）广泛应用于工程与物理系统的数值模拟，但其确定性求解无法刻画材料参数、载荷及边界条件（Boundary Conditions）的不确定性。同时，FEM 的高维离散化网格导致直接进行贝叶斯推断计算量极大。本报告旨在解决：如何构建一个层次化高斯马尔可夫随机场（Hierarchical GMRF）模型，在保留 FEM 结构信息的前提下，高效地融入边界条件约束，并实现后验不确定性量化。

**核心方法**  
报告提出将 FEM 的刚度矩阵与质量矩阵视为 GMRF 的精度矩阵（precision matrix）的线性组合，通过引入潜变量（latent field）表示位移场，并利用边界条件构造线性约束（如 Dirichlet 边界 $u|_{\partial \Omega}=g$）。层次结构体现在：第一层为物理驱动的 GMRF 先验（精度矩阵由 FEM 离散化导出），第二层为观测模型（如应变或位移测量），第三层为边界条件参数的超先验。推断采用集成嵌套拉普拉斯近似（INLA）或稀疏 Cholesky 分解，利用 GMRF 的稀疏性实现高效计算。

**与已有工作关系**  
已有工作（如 Lindgren et al., 2011 的 SPDE 方法）用 GMRF 近似连续偏微分方程的解，但通常针对简单边界（如齐次 Neumann 或 Dirichlet），且未显式利用 FEM 的离散结构。本报告将 FEM 的单元刚度矩阵直接作为 GMRF 的局部依赖结构，并系统处理非齐次、混合边界条件，相当于在统计模型与数值分析之间架起更直接的桥梁。此外，层次化框架允许对边界条件本身进行贝叶斯学习，而传统 FEM 将其视为已知或通过正则化处理。

**主要贡献**  
1. 提出一种新的概率化 FEM 框架，将确定性有限元离散与 GMRF 层次模型统一，实现物理信息与数据驱动的不确定性量化。  
2. 给出边界条件在 GMRF 精度矩阵中的显式嵌入方式（如通过线性约束或惩罚项），避免传统“硬约束”导致的数值不稳定。  
3. 利用稀疏矩阵算法，使后验推断的计算复杂度与 FEM 求解相当，可扩展至大规模网格。  
4. 为工程中涉及边界条件不确定性的问题（如接触力学、流固耦合）提供统计推断工具。


### 4. Robust Selection of the Number of Change-Points via FDR Control

**讲者**：Hui Chen（Jiangsu Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
变点检测中，选择变点个数（即模型阶数）是核心难题。传统方法如BIC、交叉验证或基于似然比检验的序列过程，在高维或噪声异质场景下易过度选择或漏检，且缺乏对错误发现率的显式控制。该报告旨在解决：如何在保证变点位置推断的FDR（False Discovery Rate）不超过预设水平的前提下，稳健地估计变点个数，尤其适用于数据存在异常值或分布偏移的鲁棒场景。

**核心方法**  
讲者可能提出一种两步框架：首先，利用稳健的局部检验统计量（如基于分位数回归或Huber损失的得分统计量）对每个候选位置计算p值，并通过Benjamini-Hochberg（BH）过程或更保守的BY过程控制FDR；其次，将FDR控制与模型选择准则（如改进的mBIC）结合，通过自适应阈值筛选出显著变点，同时利用bootstrap或置换方法校准检验统计量的空分布，以应对非参数或厚尾误差。方法本质是将多重假设检验框架嵌入变点选择，用FDR替代传统的族系错误率（FWER），从而在保证发现能力的同时控制错误发现比例。

**与已有工作关系**  
现有变点选择方法多依赖信息准则（如BIC、MDL）或惩罚似然（如PELT），但缺乏对错误发现率的直接控制；而基于FDR的变点检测（如CUSUM + BH）通常假设误差正态且方差已知，对异常值敏感。该报告的工作可能将稳健统计（如M估计）与FDR控制结合，提出对模型误设和重尾误差具有鲁棒性的变点个数选择方法，填补了“稳健性”与“多重比较控制”之间的空白。

**主要贡献**  
1. 首次将FDR控制框架系统引入变点个数的稳健选择，提供理论保证（如FDR渐近控制、选择一致性）。  
2. 提出适用于非高斯、异方差数据的稳健检验统计量，避免传统方法因异常点导致的虚假变点。  
3. 通过模拟和实证（如金融时间序列、基因组数据）展示该方法在变点检测的准确性和鲁棒性上优于BIC、PELT及非稳健FDR方法。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)