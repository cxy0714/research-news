# Biostatistics — Vol 23  Issue 3  ·  2026-05-21

- 共 20 篇 · Biostatistics

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1093/biostatistics/kxaa057](https://doi.org/10.1093/biostatistics/kxaa057) — Efficiently transporting causal direct and indirect effects to new populations under intermediate confounding and with multiple mediators
- **作者**: Kara E Rudolph, Iván Díaz
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 789-806
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文在因果中介分析框架下，研究将干预性直接和间接效应跨人群迁移的问题，设定中允许存在中间混杂以及多个/高维中介变量。作者基于迁移效应的 efficient influence function 构建了非参数 one-step 估计量，该估计量具有多重稳健性，在正则条件下达到半参数有效界且为 n^{-1/2}-CAN。方法支持通过 cross-fitting 结合数据自适应算法估计干扰参数，从而避免维数灾难。理论上证明了在多中介与中间混杂下的多重稳健与半参数有效性，实证上可解释不同站点间处理效应差异的机制。对您有用：直接推进了您关注的 causal inference (mediation) 与 efficiency theory 交叉方向，处理高维中介与中间混杂的半参数有效推断思路具有高度迁移性。
- **关键技术**: `transported interventional effects`, `efficient influence function`, `multiply robust estimation`, `cross-fitting`, `multiple mediators`
- **为什么对您有用**: 直接对应您 primary interest 中的 causal inference (mediation) 与 efficiency theory (semiparametric efficiency bounds)；其处理多中介与中间混杂下的多重稳健与有效估计方法，对您研究复杂因果结构下的半参数推断具有直接借鉴价值。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 2 篇)*

### 1. [10.1093/biostatistics/kxab006](https://doi.org/10.1093/biostatistics/kxab006) — Information enhanced model selection for Gaussian graphical model with application to metabolomic data
- **作者**: Jie Zhou, Anne G Hoen, Susan Mcritchie, Wimal Pathmasiri, Weston D Viles, Quang P Nguyen et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 926-948
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在高维 Gaussian graphical model (GGM) 的模型选择问题中，本文提出 structural BIC (sBIC)，将先验网络结构信息嵌入 BIC 惩罚项，并证明 extended BIC (eBIC) 是 sBIC 的特例。方法分两部分：一是 sBIC 准则，对先验结构建模并融入 BIC；二是两步 data-driven 算法，自动将先验结构嵌入候选模型池。在 mild regularity 条件下，证明了 sBIC 在高维 GGM 中的模型选择一致性（model selection consistency）。模拟显示对模型误设具有鲁棒性，且优于 eBIC 等现有方法。应用于婴儿粪便代谢组学队列数据，发现代谢通路关系是条件依赖的显著因子，并识别出传统通路分析无法发现的新代谢物关联。对您而言，高维 GGM 模型选择一致性结果与您的高维统计兴趣相邻，而代谢组学流行病学队列数据集对您的 epidemiology secondary interest 有直接参考价值。
- **关键技术**: `Gaussian graphical model`, `structural Bayesian information criterion`, `extended BIC`, `model selection consistency`, `high-dimensional penalty`, `prior structure embedding`
- **为什么对您有用**: 高维 GGM 的 BIC 型一致性结果与您的高维统计兴趣（虽非 RMT 核心）相邻；代谢组学分子流行病学队列数据及分析流程对您的 epidemiology secondary interest 有数据集和方法迁移价值。

### 2. [10.1093/biostatistics/kxab007](https://doi.org/10.1093/biostatistics/kxab007) — Simultaneous differential network analysis and classification for matrix-variate data with application to brain connectivity
- **作者**: Hao Chen, Ying Guo, Yong He, Jiadong Ji, Lei Liu, Yufeng Shi et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 967-989
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在矩阵变量数据设定下，本文目标是同时进行差异网络分析（识别组间差异交互模式）与疾病分类，假设协方差矩阵服从 Kronecker 乘积结构以分别刻画空间与时间相关性。方法将时间协方差视为冗余参数，通过集成学习过程联合估计空间协方差的组间差异并构建分类器。该过程避免了朴素向量化方法对矩阵结构信息的破坏，实现了差异网络检测与分类的同步优化。理论分析侧重于高维矩阵协方差估计与变量选择的一致性，但未涉及半参数效率界或 RMT 极限谱分布。在阿尔茨海默病 fMRI 数据应用中，识别出与已有实验一致的核心节点与差异连接，并取得良好分类表现。对您而言，该文展示了 Kronecker 结构在高维矩阵数据中的建模思路，且其神经影像数据分析流程对流行病学应用有参考价值。
- **关键技术**: `Kronecker product covariance`, `matrix-variate data`, `differential network analysis`, `ensemble learning`, `spatial-temporal correlation`
- **为什么对您有用**: 涉及高维矩阵数据的协方差结构估计（Kronecker 乘积），与您的高维统计与统计计算兴趣相邻；同时其阿尔茨海默病神经影像数据的应用分析对流行病学方向有数据集与方法借鉴价值。

## 非参数 / 半参数  *(nonparam_semipara, 3 篇)*

### 1. [10.1093/biostatistics/kxaa052](https://doi.org/10.1093/biostatistics/kxaa052) — Semiparametric regression on cumulative incidence function with interval-censored competing risks data and missing event types
- **作者**: Jun Park, Giorgos Bakoyannis, Ying Zhang, Constantin T Yiannoutsos
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 738-753
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究区间删失竞争风险数据且事件类型缺失情形下累积发生率（CIF）的半参数回归问题，目标参数为 CIF 回归系数，关键假设为包含辅助变量的弱 MAR 缺失机制。作者提出一种增强逆概率加权筛极大似然估计量（AIPW-SMLE），利用 sieve 空间逼近无穷维参数（基础风险），并通过 AIPW 结构处理事件类型缺失。该估计量具有双重稳健性（doubly robust）：当缺失概率模型或事件类型概率模型之一误设时仍保持一致。蒙特卡洛模拟表明该方法在缺失比例较高时仍表现良好，实证分析应用于撒哈拉以南非洲 HIV 队列数据，并提供了 R 包 intccr 的实现。对您有用：AIPW 与 sieve MLE 结合的双重稳健构造直接关联您对 semiparametric efficiency 与 DR 估计量的兴趣，且 HIV 队列竞争风险设定对流行病学因果推断应用有数据集与分析流程的借鉴价值。
- **关键技术**: `Augmented inverse probability weighting (AIPW)`, `Sieve maximum likelihood estimation`, `Double robustness`, `Competing risks regression`, `Interval censoring`
- **为什么对您有用**: AIPW 与 sieve MLE 的结合是半参数效率理论的典型应用，直接契合您对 semiparametric efficiency bounds 与 DR 估计量的兴趣；同时 HIV 队列的竞争风险与缺失数据设定对流行病学因果推断应用具有数据集与分析流程的借鉴价值。

### 2. [10.1093/biostatistics/kxaa051](https://doi.org/10.1093/biostatistics/kxaa051) — Treed distributed lag nonlinear models
- **作者**: Daniel Mork, Ander Wilson
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 754-771
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在空气污染暴露对健康影响的流行病学研究中，分布式滞后非线性模型（DLNM）常用于估计暴露-时间-响应函数，但传统样条基展开假设曲面全局光滑，在效应仅存在于特定时间窗口时不够灵活。本文提出基于贝叶斯加性回归树（BART）的 DLNM 框架，利用回归树在暴露-时间空间上构建分段常数关系，从而放松全局光滑假设。模拟表明，当真实暴露-时间曲面非光滑时，该树模型优于样条方法，方差更低且能更精确识别关键暴露窗口；在光滑设定下两者表现相当。实证分析将该方法应用于科罗拉多州出生队列的孕期 PM2.5 暴露与出生体重关联研究。对您而言，该文提供了流行病学纵向暴露设定的真实数据集与分析流程，并展示了非参数树方法在放松传统光滑假设时的应用潜力。
- **关键技术**: `distributed lag nonlinear model (DLNM)`, `Bayesian additive regression trees (BART)`, `piecewise constant estimation`, `critical window identification`, `bivariate basis expansion`
- **为什么对您有用**: 连接到您的 secondary interest 流行病学（应用与数据集）以及纵向暴露的因果/关联推断；展示了非参数树方法在放松全局光滑假设下的应用，对处理类似 epi 队列数据有方法迁移价值。

### 3. [10.1093/biostatistics/kxab005](https://doi.org/10.1093/biostatistics/kxab005) — Structure-preserving integrated analysis for risk stratification with application to cancer staging
- **作者**: Tianjie Wang, Rui Chen, Wenshuo Liu, Menggang Yu
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 990-1006
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究多研究个体患者数据下的风险分层（如癌症分期）问题，目标是在保留各研究异质性与非平衡数据结构的前提下，借力公共分组结构进行信息整合。方法上扩展了 Lin 等 (2013) 的 lasso-tree：该法以 lasso 惩罚生成比 CART 更灵活的分组模式，其参数化天然适配风险因子的有序约束（如肿瘤大小的单调性），本文进一步将其推广至多研究整合框架。理论贡献方面，为 lasso-tree 建立了原文献未涉及的性质（推测涉及分组选择一致性/oracle 性质及 lasso 惩罚下的收敛率）。模拟与多乳腺癌数据集分析验证了方法在异质性场景下的分组稳定性。对您而言，lasso-tree 的理论刻画（树结构+ℓ₁惩罚的 model selection 性质）与非参数/高维交叉区域相关，且癌症分期的流行病学应用场景可作为因果分层或 IV 分组的参考案例。
- **关键技术**: `lasso-tree`, `multi-study integration`, `ordered group lasso penalty`, `tree-structured model selection`, `oracle property`
- **为什么对您有用**: lasso-tree 的理论刻画（ℓ₁惩罚+树结构的 selection consistency）与您的高维统计/非参数理论兴趣交叉；癌症分期数据集与流行病学 secondary interest 对接，分组逻辑可迁移至因果推断中的 treatment effect heterogeneity 分层问题。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1093/biostatistics/kxaa060](https://doi.org/10.1093/biostatistics/kxaa060) — Assessing risk model calibration with missing covariates
- **作者**: Yei Eun Shin, Mitchell H Gail, Ruth M Pfeiffer
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 875-890
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在独立队列验证风险模型校准度时，部分协变量缺失（非计划或 case-cohort 等设计性缺失），目标是提高 O/E（观测/期望事件数）校准度量的估计效率。作者在逆概率权重（IPW）基础上引入 survey calibration 调整：要求完全数据子集中辅助统计量的加权和等于全队列总和，从而利用全队列可得信息提升效率。提出用仅依赖全队列可得变量的 pseudo-risk 近似真实风险值，作为估计 E 的高效辅助统计量，并推导了调整权重下 O/E 的解析方差公式。模拟表明 pseudo-risk 权重调整比 IPW 效率大幅提升，且即使 pseudo-risk 近似较差仍保持一致性；多重插补在模型误设时产生偏差。实证应用于第二原发甲状腺癌绝对风险模型的校准评估。该工作的 survey calibration 提升 IPW 效率路线与您在 efficiency theory（半参数效率、IPW 效率改进）及流行病学应用中的兴趣直接相关。
- **关键技术**: `inverse probability weighting`, `survey calibration`, `pseudo-risk auxiliary statistic`, `O/E calibration ratio`, `analytic variance formula`, `case-cohort missingness by design`
- **为什么对您有用**: survey calibration 提升 IPW 效率的技术路线直接对应您在 efficiency theory（半参数效率界、IPW 效率改进）方面的兴趣，且流行病学队列校准评估的应用场景可迁移至您关注的 epidemiology 因果应用。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1093/biostatistics/kxaa058](https://doi.org/10.1093/biostatistics/kxaa058) — Testing for similarity of binary efficacy–toxicity responses
- **作者**: Kathrin Möllenhoff, Holger Dette, Frank Bretz
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 949-966
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在含协变量（如剂量）的临床试验设定下，目标是检验两组患者（如不同地域或年龄层）在二元疗效-毒性响应曲线上的相似性（等价性），关键假设为响应曲线可用参数或Gumbel模型刻画。方法通过估计两组响应曲线间的最大偏差（supremum distance）构建检验统计量，并采用参数Bootstrap（parametric bootstrap）计算临界值。对于相关的二元疗效-毒性联合终点，引入二维Gumbel型模型刻画变量间依赖结构，将单终点相似性检验推广至双终点情形。模拟与案例研究表明该检验在有限样本下具有合理的水平与功效。对您有用：该文将极大偏差统计量与参数Bootstrap结合处理曲线等价检验，属于数学统计（假设检验）的经典拓展，其极值统计量与Bootstrap计算思路可迁移至其他非参数/半参数曲线比较问题。
- **关键技术**: `similarity testing (equivalence)`, `maximal deviation statistic`, `parametric bootstrap`, `Gumbel-type bivariate model`, `dose-response curves`
- **为什么对您有用**: 直接对应您primary interest中的数学统计（假设检验）方向；其基于极大偏差统计量与Bootstrap的曲线等价检验框架，对处理非参数/半参数曲线比较的假设检验问题具有方法学迁移价值。

### 2. [10.1093/biostatistics/kxab003](https://doi.org/10.1093/biostatistics/kxab003) — Testing calibration of phenotyping models using positive-only electronic health record data
- **作者**: Lingjiao Zhang, Yanyuan Ma, Daniel Herman, Jinbo Chen
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 844-859
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在 EHR 表型模型校准检验中，传统方法需要金标准病例与对照标签，但临床实践中常只能获得金标准病例与大量未标记患者（即 positive-only 数据）。本文在 labeled cases 代表全体病例的假设下，提出一种新的校准检验统计量：将风险子组中模型无关与模型依赖的病例数估计之差聚合，该统计量渐近服从卡方分布。此外，作者证明校准斜率亦可在 positive-only 设定下被估计，并提出判别度指标的一致估计量及其大样本性质。模拟与 Penn Medicine 原发性醛固酮增多症 EHR 数据验证了方法表现。对您而言，该文的 positive-only 框架本质上是一个部分标记/选择偏差下的半参数推断问题，校准检验的卡方渐近理论构造与您在 hypothesis testing 及 semiparametric efficiency 方向的兴趣直接相关。
- **关键技术**: `positive-only calibration test`, `chi-squared asymptotic distribution`, `calibration slope estimation under partial labeling`, `discrimination measure consistent estimation`, `model-free vs model-based case count comparison`
- **为什么对您有用**: 核心方法是在部分标记（positive-only）设定下构造校准检验统计量并推导渐近性质，直接关联您在 hypothesis testing 与 semiparametric theory 的 primary interests；EHR 表型验证场景也为流行病学应用提供了可迁移的分析模式与真实数据集参考。

### 3. [10.1093/biostatistics/kxab001](https://doi.org/10.1093/biostatistics/kxab001) — Dimension constraints improve hypothesis testing for large-scale, graph-associated, brain-image data
- **作者**: Tien Vo, Akshay Mishra, Vamsi Ithapu, Vikas Singh, Michael A Newton
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 860-874
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 针对具有图结构关联的大规模多重检验问题，本文提出一种基于经验贝叶斯混合模型的局部错误发现率评分方法。所提 GraphMM 方法通过在图邻接节点间对参数对比施加正则化约束，利用非零假设在图上形成连通子图的结构先验来提升检验功效。在局部 FDR 框架下，该正则化项等价于对相邻节点引入隐变量的相似性惩罚，从而在保持 FDR 控制的同时增强信号检测能力。模拟表明 GraphMM 在多种设定下能有效控制 FDR，但过度正则化可能导致 FDR 失控。在阿尔茨海默症脑影像数据的应用中，GraphMM 比传统忽略图结构的大规模检验方法产出更多显著结果。对您有用：该文将图结构约束引入多重检验的思路，可为您在假设检验方向的研究提供图正则化与 FDR 控制结合的参考范式。
- **关键技术**: `empirical Bayes mixture model`, `local false discovery rate`, `graph-structured regularization`, `large-scale multiple testing`
- **为什么对您有用**: 直接关联您在数学统计（假设检验）方向的兴趣，展示了如何在多重检验中利用图结构先验提升功效，其经验贝叶斯与正则化结合的思路对高维假设检验有参考价值。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1093/biostatistics/kxaa056](https://doi.org/10.1093/biostatistics/kxaa056) — Marginal modeling of cluster-period means and intraclass correlations in stepped wedge designs with binary outcomes
- **作者**: Fan Li, Hengshi Yu, Paul J Rathouz, Elizabeth L Turner, John S Preisser
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 772-788
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在阶梯楔形集群随机试验（SW-CRTs）的二值结局设定下，目标是干预效应和组内相关系数（ICC）的边际推断，传统基于个体水平观测的估计方程在大集群-时期样本量下计算量极大。本文提出基于集群-时期均值的估计方程方法，证明个体水平边际均值的 quasi-score 可等价重构为集群-时期均值的 quasi-score。同时，将个体水平 ICC 映射为集群-时期均值的相关系数，在广义线性模型框架下严格论证了该降维方法的合理性。进一步提出矩阵调整估计方程以改善 ICC 的有限样本推断性能。该方法在保证有效估计干预效应与相关系数的同时大幅提升计算速度，对您在纵向因果推断（集群随机试验设计）和统计计算（大规模相关数据降维算法）方面的研究具有直接的参考价值。
- **关键技术**: `estimating equations`, `quasi-score equivalence`, `intraclass correlation coefficient (ICC)`, `stepped wedge cluster randomized trials`, `matrix-adjusted estimating equations`, `marginal models`
- **为什么对您有用**: 本文直接处理纵向因果设计（SW-CRT）中大规模相关数据的计算瓶颈，通过 quasi-score 的代数重构实现降维加速，对您在统计计算（数值算法优化）和纵向因果推断（集群随机试验的干预效应估计）的交叉研究有直接的方法论借鉴意义。

## 流行病学  *(epidemiology, 2 篇)*

### 1. [10.1093/biostatistics/kxab010](https://doi.org/10.1093/biostatistics/kxab010) — A spatiotemporal recommendation engine for malaria control
- **作者**: Qian Guan, Brian J Reich, Eric B Laber
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 1023-1038
- 相关性 3/10 · novelty: `application`
- **摘要**: 在疟疾控制的时空资源分配问题中，目标是基于实时疾病信息寻找最大化长期累积收益的最优干预策略（policy）。作者将策略形式化为从疾病状态到连续资源分配的映射，并构建了兼顾可解释性与公平性的策略类。估计方法结合了层次贝叶斯时空模型（刻画疾病传播动态）与策略搜索算法（policy search），在预设策略类中求解最优策略。理论上未涉及半参数效率界或因果识别的新突破，主要侧重于贝叶斯时空建模与强化学习式策略优化的结合。在模拟与刚果民主共和国疟疾干预数据中，该框架的估计策略在长期结果上优于朴素分配方法。对您而言，该文提供了流行病学纵向因果干预（动态处理策略）的真实数据集与应用范式，策略搜索的设定与您关注的 longitudinal causal inference 有直接对接，但方法路径（贝叶斯 vs 半参数）差异较大。
- **关键技术**: `policy search`, `hierarchical Bayesian spatiotemporal model`, `optimal treatment regime`, `resource allocation`, `dynamic causal policy`
- **为什么对您有用**: 该文属于流行病学纵向因果干预的应用工作，提供了刚果疟疾时空数据集；其动态策略（optimal regime）设定与您关注的 longitudinal causal inference 直接相关，但方法路径为贝叶斯而非半参数效率理论，可作应用范式参考。

### 2. [10.1093/biostatistics/kxaa059](https://doi.org/10.1093/biostatistics/kxaa059) — Estimation of the generation interval using pairwise relative transmission probabilities
- **作者**: Sarah V Leavitt, Helen E Jenkins, Paola Sebastiani, Robyn S Lee, C Robert Horsburgh, Andrew M Tibbs et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 807-824
- 相关性 2/10 · novelty: `application`
- **摘要**: 在缺乏完整接触者追踪或全基因组测序的传染病监测设定下，本文目标是估计代际间隔（或序列间隔）的分布。核心方法提出一种基于配对相对传播概率的期望最大化（EM）算法，通过引入降噪技术来处理潜在传播对的不确定性，从而绕过对明确传播链的依赖。模拟研究表明，该方法在不同基本再生数、代际间隔和突变率设定下均能准确恢复间隔分布。实证部分将该方法应用于马萨诸塞州 2010–2016 年的结核病监测数据，成功估计了该地区的结核病序列间隔。对您而言，推断“谁传染谁”本质上是因果图的结构学习问题，该文提供的真实监测数据集及处理潜在传播对的 EM 框架，可为您在流行病学因果推断方向的应用工作提供 pipeline 和数据参考。
- **关键技术**: `expectation maximization (EM)`, `relative transmission probability`, `latent transmission pair`, `noise reduction`, `serial interval estimation`
- **为什么对您有用**: 属于流行病学（secondary interest）的应用因果推断工作，推断传播链本质是因果图结构学习；文中马萨诸塞州结核病真实监测数据及处理潜在传播对的 EM pipeline 对您在 epi 领域的因果推断应用有直接参考价值。

## 其他  *(other, 7 篇)*

### 1. [10.1093/biostatistics/kxaa049](https://doi.org/10.1093/biostatistics/kxaa049) — An optimal kernel-based multivariate U-statistic to test for associations with multiple phenotypes
- **作者**: Y Wen, Qing Lu
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 705-720
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在多表型关联检验设定下，目标是构建一个对表型分布和预测变量-结局关系形式鲁棒的检验统计量，以检测一组预测变量与多个结局之间的关联。本文提出基于核的多变量 U-统计量（KMU），采用基于秩的核函数处理结局变量以保证对分布的鲁棒性；检验统计量通过数据驱动方式融合多个核函数，从而捕捉未知的复杂非线性关系并避免单一核选择带来的功效损失。作者推导了该统计量的渐近性质（零假设下的渐近分布与局部替代假设下的功效），模拟表明 KMU 控制了 I 类错误且功效优于现有方法。在 ADNI 全基因组测序数据的影像表型分析中，KMU 识别出新的关联基因。对您有用：该文将多变量 U-统计量与核方法结合用于假设检验，直接契合您对 higher-order U-statistics 与 hypothesis testing 的理论兴趣，且其多核融合与渐近推导思路可迁移至高维或半参数设定下的检验问题。
- **关键技术**: `multivariate U-statistic`, `rank-based kernel`, `data-driven multiple kernel combination`, `asymptotic distribution`, `association testing`
- **为什么对您有用**: 直接契合您对 higher-order U-statistics 与 hypothesis testing 的理论兴趣；其多核融合与渐近性质推导思路对高维或半参数设定下的检验问题有方法学迁移价值。

### 2. [10.1093/biostatistics/kxab002](https://doi.org/10.1093/biostatistics/kxab002) — Bayesian biclustering for microbial metagenomic sequencing data via multinomial matrix factorization
- **作者**: Fangting Zhou, Kejun He, Qiwei Li, Robert S Chapkin, Yang Ni
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 891-909
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对微生物组高通量测序数据（组成性、稀疏、零膨胀计数矩阵），提出可识别的 Bayesian multinomial matrix factorization 模型，同时对微生物和宿主进行重叠双聚类。观测计数矩阵被建模为 Dirichlet-multinomial 混合，潜在聚类结构在其上分层构建；贝叶斯框架下聚类数自动确定，并利用微生物分类阶元树的先验信息提升可解释性。模拟中与替代方法比较展示了聚类恢复性能，应用于炎症性肠病（IBD）肠道微生物组数据，发现包含已知与 IBD 及其亚型相关菌科的聚类。该方法学核心为贝叶斯潜变量模型与矩阵分解，与您关注的 semiparametric efficiency、高维 inference 或因果推断方向重叠有限，但若您对 compositional data 的矩阵分解建模或流行病学微生物组数据集有兴趣，可作为应用参考。
- **关键技术**: `Bayesian multinomial matrix factorization`, `Dirichlet-multinomial mixture`, `biclustering with overlapping clusters`, `taxonomic tree prior`, `zero-inflated compositional count data`
- **为什么对您有用**: 与您 primary interests（causal inference、RMT、semiparametric efficiency）方法重叠很小；流行病学应用侧（IBD 微生物组数据集）有一定 secondary interest 价值，但方法本身为贝叶斯聚类而非因果推断或高维 inference，收益有限。

### 3. [10.1093/biostatistics/kxab004](https://doi.org/10.1093/biostatistics/kxab004) — A greedy approach for mutual exclusivity analysis in cancer study
- **作者**: Hongyan Fang, Zeyu Zhang, Yinsheng Zhou, Lishuai Jin, Yaning Yang
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 910-925
- 相关性 2/10 · novelty: `minor`
- **摘要**: 本文在癌症基因组学设定下，研究体细胞突变的互斥性（mutual exclusivity, ME）检测问题，目标是识别驱动基因或功能通路。作者提出一个 ME 的概率生成模型，并设计贪心算法（含预筛选与逐步前向步骤）来选择互斥基因集，显著降低计算时间。功效计算表明该方法在单个或多个重叠 ME 集合下均有较高检验功效。实证部分使用 TCGA 全外显子测序数据进行了验证。该方法学 novelty 有限——贪心启发式而非最优算法，概率模型较简单，未涉及效率理论或高维渐近分析。对您而言，仅在假设检验的计算加速思路上有微弱参考价值，与您核心兴趣方向（因果推断、半参数效率、RMT）关联不大。
- **关键技术**: `probabilistic generative model`, `greedy forward selection`, `pre-selection screening`, `power calculation`, `mutual exclusivity test`
- **为什么对您有用**: 与您 primary interests 重叠极弱：假设检验部分仅为功效模拟而非理论，计算部分为贪心启发式而非数值方法/矩阵算法；癌症基因组学也不在您 secondary interests（流行病学因果推断、经济理论、天文统计）范围内，收益有限。

### 4. [10.1093/biostatistics/kxaa061](https://doi.org/10.1093/biostatistics/kxaa061) — Penalized model-based clustering of fMRI data
- **作者**: Andrew Dilernia, Karina Quevedo, Jazmin Camchong, Kelvin Lim, Wei Pan, Lin Zhang
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 825-843
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对 fMRI 功能连接（FC）的异质性问题，提出随机协方差聚类模型（RCCM），在混合模型框架下同时进行被试聚类与个体/组水平协方差矩阵估计。RCCM 假设组内被试共享组水平 FC 网络特征，同时允许个体水平 FC 偏离组水平，通过 penalized likelihood 实现协方差矩阵的稀疏化估计，并使用 EM 算法进行求解。该方法将高维协方差矩阵的聚类与估计统一在基于模型的框架内，克服了传统方法先降维再聚类或忽略个体差异的缺陷。模拟显示 RCCM 在聚类准确度和 FC 估计误差上优于现有方法；在精神分裂症 fMRI 数据中展示了临床效用。对您而言，该文在 penalized covariance estimation 和 EM 算法实现上的计算细节有一定参考价值，但与您核心的因果推断或高维渐近理论关联较弱。
- **关键技术**: `model-based clustering`, `penalized likelihood`, `random covariance matrix`, `EM algorithm`, `functional connectivity estimation`
- **为什么对您有用**: 本文主要处理高维协方差矩阵的聚类与稀疏估计，涉及 penalized likelihood 与 EM 算法计算，与您在统计计算（矩阵估计与优化算法）方面的兴趣有微弱交叉，但核心理论（因果、RMT、效率）关联不大。

### 5. [10.1093/biostatistics/kxaa054](https://doi.org/10.1093/biostatistics/kxaa054) — A benchmark for dose-finding studies with unknown ordering
- **作者**: Pavel Mozgunov, Xavier Paoletti, Thomas Jaki
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 721-737
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究联合用药剂量寻找试验中剂量组合毒性排序未知时的非参数最优基准（benchmark）推广问题；原 benchmark 假定剂量可按毒性单调排序，而联合用药场景下部分组合无法排序，直接套用原 benchmark 会忽略排序不确定性导致上界过松。作者提出广义 benchmark：在给定每个患者完全信息下，评估每种可能排序的发生概率，据此对设计性能给出更紧的非参数上界。方法适用于任意数量的离散或连续终点，不限于二元毒性。通过 Phase I 联合试验（二元毒性）和 Phase I/II 联合试验（二元毒性+连续疗效）的数值示例说明改进幅度。该文对您直接价值有限——'最优基准上界'概念与 semiparametric efficiency bound 有类比性但技术路线差异大，且剂量寻找设计不在您核心兴趣内。
- **关键技术**: `nonparametric optimal benchmark`, `dose-finding design`, `ordering uncertainty`, `combination trials`, `upper bound on design performance`
- **为什么对您有用**: 与您 primary interest 的 semiparametric efficiency bound 仅在'性能上界'概念层面有弱类比，技术工具和设定差异大；剂量寻找设计非您关注领域，收益较低。

### 6. [10.1093/biostatistics/kxaa039](https://doi.org/10.1093/biostatistics/kxaa039) — Sine-skewed toroidal distributions and their application in protein bioinformatics
- **作者**: Jose Ameijeiras-Alonso, Christophe Ley
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 685-704
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在蛋白质生物信息学背景下，针对环面（torus）上的二面角数据通常呈现不对称模式但现有模型多为对称分布的问题，本文构建非对称环面分布。引入 sine-skewed 构造方法，从对称分布生成偏斜分布；该构造无需额外计算归一化常数，降低了模型复杂度。推导了形状与依赖性度量的显式表达式、随机数生成算法以及极大似然估计（MLE）的渐近性质。在蛋白质数据上验证了新模型优于对称前体模型。对您而言，该文属于方向统计学的参数建模，与您关注的半参数/高维/因果推断交集较小，仅 MLE 渐近理论有微弱关联。
- **关键技术**: `sine-skewed construction`, `toroidal distributions`, `maximum likelihood estimation`, `directional statistics`, `normalizing constant`
- **为什么对您有用**: 该文主要贡献在方向统计学的参数建模与 MLE 渐近性质，与您核心关注的半参数效率、高维推断或因果推断无直接交集，仅 MLE 渐近性有微弱理论关联，整体相关度较低。

### 7. [10.1093/biostatistics/kxab008](https://doi.org/10.1093/biostatistics/kxab008) — Bayesian adaptive design for concurrent trials involving biologically related diseases
- **作者**: Matthew A Psioda, H Amy Xia, Xun Jiang, Jiawei Xu, Joseph G Ibrahim
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 1007-1022
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究针对生物相关疾病的并发临床试验的贝叶斯自适应设计，目标是在每种疾病试验中验证试验药物优于对照。方法通过相关混合先验在疾病间借用治疗有效性的信息，其分析过程与贝叶斯模型平均密切相关。混合先验基于对每种疾病的悲观和乐观预测构建共轭先验，并对所有可能的先验配置组合设定混合权重。该框架允许在不同疾病终点具有不同数据类型时稳健地借用信息，克服了贝叶斯分层模型在此类异质数据设定下的局限。模拟研究表明，所提设计的操作特性优于基于贝叶斯分层模型的借用信息设计。对您而言，本文属于贝叶斯临床试验设计，与您关注的因果推断、半参数效率或高维推断等核心方向关联较弱。
- **关键技术**: `Bayesian adaptive design`, `correlated mixture priors`, `Bayesian model averaging`, `conjugate priors`, `operating characteristics`
- **为什么对您有用**: 本文属于贝叶斯临床试验设计，与您主要关注的因果推断、半参数理论及高维统计等方向关联较弱，仅在多重假设检验（试验操作特性控制）的宽泛意义下有极微弱的联系。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

