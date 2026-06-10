# Biostatistics — Vol 26  Issue 1  ·  2026-06-10

- 共 18 篇 · Biostatistics
- 目录核对 ⚠️ 疑似漏 67 篇（对照 OpenAlex 86 篇）：10.1093/biostatistics/kxae031、10.1093/biostatistics/kxae044、10.1093/biostatistics/kxae040、10.1093/biostatistics/kxae014、10.1093/biostatistics/kxae020 等

## 因果推断  *(causal_inference, 5 篇)*

### 1. [10.1093/biostatistics/kxaf031](https://doi.org/10.1093/biostatistics/kxaf031) · [arXiv](https://arxiv.org/abs/2403.09928) — Identification and estimation of mediational effects of longitudinal modified treatment policies
- **作者**: Brian Gilbert, Katherine Hoffman, Nicholas Williams, Kara Rudolph, Edward J Schenck, Iván Díaz
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 10/10 · novelty: `new_method`
- **摘要**: 在纵向连续处理（modified treatment policies, MTP）与非参数结构方程模型（NPSEM）设定下，研究因果中介效应的识别与估计，目标 estimand 为直接与间接效应。方法基于 doubly robust pseudo-outcomes 与 cross-fitted sequential regression，不依赖参数模型假设，得到 n^{-1/2}-CAN 且 semiparametric efficient 的估计量。识别策略利用 NPSEM 的纵向因子分解，处理了连续处理下的中介路径与混杂。实证应用于 COVID-19 机械通气对生存的影响（急性肾损伤为中介），揭示了“不一致中介”（direct 与 indirect 方向相反）现象。对您有用：直接推进了 causal inference 中 longitudinal mediation 与 MTP 的估计理论，且其 cross-fitted DR 框架与您的 efficiency theory / DML 兴趣高度契合。
- **关键技术**: `modified treatment policies`, `longitudinal mediation`, `NPSEM`, `doubly robust pseudo-outcomes`, `cross-fitted sequential regression`, `inconsistent mediation`
- **为什么对您有用**: 直接对应 causal inference 中的 longitudinal mediation 与 continuous treatment (MTP) 设定，以及 efficiency theory 中的 doubly robust / cross-fitting 估计。可用您 very_familiar 的 estimation theory in CI 与 software development 直接复现其 cross-fitted sequential regression 算法与渐近性质验证。立即可做：用现有 CI 估计与软件武器复现并验证其 DR estimator；若要拓展至 HOIF 或 proximal longitudinal mediation，则需先在 moderately_familiar 的 HOIF / identification theory 上长肌肉。

### 2. [10.1093/biostatistics/kxaf042](https://doi.org/10.1093/biostatistics/kxaf042) · [arXiv](https://arxiv.org/abs/2306.14019) — Instrumental variable approach to estimating individual causal effects in N-of-1 trials: application to ISTOP study
- **作者**: Kexin Qu, Christopher H Schmid, Tao Liu
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在 N-of-1 试验（单个体多次交叉）设定下，目标是定义并估计个体因果效应（连续暴露效应与个体观测行为效应）。核心挑战包括不完美依从性、二值处理与二值结局导致的 odds ratio non-collapsibility，以及纵向观测的序列自相关。作者采用随机化分配作为工具变量（IV），构建两方程参数贝叶斯 IV 模型，通过潜变量结构模型刻画混杂机制并以贝叶斯后验推断功能参数，绕过 non-collapsibility 与 non-consistency 问题，同时纳入自相关结构。模拟显示该方法相比 ITT/PP/AT 显著降低偏差并提升覆盖率。对您可能有用：该文将 IV 与贝叶斯潜变量结合处理个体层面依从性与 non-collapsibility，为纵向因果推断中 IV 方法的贝叶斯实现提供了一个具体案例。
- **关键技术**: `Bayesian instrumental variable`, `N-of-1 trial causal framework`, `non-collapsibility odds ratio`, `latent structural model`, `autocorrelation in longitudinal outcomes`, `potential treatment selection paths`
- **为什么对您有用**: 直接连接到因果推断中的 IV 方法与纵向设定，以及流行病学应用（房颤数据集）。您武器库中的 identification theory in causal inference（moderately_familiar）可以审视其潜变量结构模型的 identification 条件是否完备；贝叶斯 IV 的参数化设定限制了 semiparametric efficiency 的讨论空间，若想从效率理论角度切入需先补 semiparametric IV 理论。中期可做：需先在 semiparametric theory 上长肌肉，才能将此贝叶斯参数 IV 推广到 semiparametric/robust IV 估计。

### 3. [10.1093/biostatistics/kxaf043](https://doi.org/10.1093/biostatistics/kxaf043) · [arXiv](https://arxiv.org/abs/2507.07349) — Stratification-based instrumental variable analysis framework for nonlinear effect analysis
- **作者**: Haodong Tian, Ashish Patel, Stephen Burgess
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在连续暴露的非线性因果效应设定下，针对未测量混杂，本文提出基于分层 的工具变量 (IV) 框架，目标 estimand 为非线性效应函数及变点。框架由三个'S'要素构成：Stratification 构造保持 IV 核心假设的子样本层；Scalar-on-function/scalar-on-scalar 模型连接局部层特异性与全局效应估计；Sum-of-single-effects 方法实现效应估计。该方法规避了 IV regression 与 control-function 的强参数假设，在弱 IV 下具有更好的效应形状预测与变点识别能力。模拟与 UK Biobank 孟德尔随机化实证（酒精对血压）验证了方法的有效性及阈值效应。对您有用：本文拓展了非线性 IV 的 identification 与 estimation，且提供了流行病学 MR 的真实数据集范例。
- **关键技术**: `Stratification-based instrumental variable`, `Scalar-on-function model`, `Sum-of-single-effects estimation`, `Mendelian randomization`, `Nonlinear causal effect identification`, `Change point detection`
- **为什么对您有用**: (1) 本文属于 causal inference 的 IV 方法（非线性/弱IV设定）及 epidemiology 的 MR 应用，直接命中您的两个核心兴趣。(2) 您 very_familiar 的 'estimation theory in causal inference' 可用于审视该 Stratification-IV 框架的 semiparametric efficiency bound 是否可达，'software development' 能力可支撑其算法实现与拓展。(3) Follow-up：**立即可做**——用现有因果 identification 理论严格推导其分层假设下的 identification 逻辑，或评估其 estimator 的效率性质与弱IV下的收敛率。

### 4. [10.1093/biostatistics/kxaf040](https://doi.org/10.1093/biostatistics/kxaf040) · [arXiv](https://arxiv.org/abs/2306.01086) — Multi-study <i>R</i> -learner for estimating heterogeneous treatment effects across studies using statistical machine learning
- **作者**: Cathy Shyr, Boyu Ren, Prasad Patil, Giovanni Parmigiani
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 8/10
- **摘要**: 在多研究(multi-study)因果推断设定下，目标是估计异质性处理效应(CATE)并处理研究间异质性。现有方法常假设各研究的CATE、基线响应函数和倾向评分完全相同，本文放松了这三类假设，提出multi-study R-learner。该方法通过membership probability自适应地组合跨研究的nuisance function估计与研究内CATE估计，从而在研究间借用信息。在series estimation框架下证明了估计量的渐近正态性，并在倾向评分存在研究间异质性时比标准R-learner更有效。实证用癌症RCT与观察性数据展示了方法优势。对您有用：直接推进了因果推断中多研究设定下的CATE估计与效率理论。
- **关键技术**: `R-learner`, `multi-study learning`, `CATE estimation`, `membership probability`, `series estimation`, `asymptotic normality`
- **为什么对您有用**: 直接连接因果推断的CATE估计与效率理论(primary interest)。本文的渐近正态性与效率提升证明可用您熟悉的semiparametric efficiency bound工具审视其效率界是否紧。follow-up判断：立即可做——用very_familiar的estimation theory in causal inference验证其效率声称，或用moderately_familiar的semiparametric theory推导multi-study R-learner的influence function。

### 5. [10.1093/biostatistics/kxaf046](https://doi.org/10.1093/biostatistics/kxaf046) · [arXiv](https://arxiv.org/abs/2310.19988) — Counterfactual fairness for small subgroups
- **作者**: Solvejg Wastvedt, Jared D Huling, Julian Wolfson
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在 counterfactual fairness 框架下，本文针对小亚群（small subgroups）的公平性评估问题，提出新的 estimands 和估计策略。核心 estimands 跨群借信息以缓解小样本下的方差膨胀，并引入一种 novel data borrowing 方法，利用仅含协变量与群组信息但缺失结局和预测值的外部数据。估计采用基于 counterfactual framework 的因果推断方法（涉及 treatment confounding 的调整），理论性质聚焦于小样本下的方差–偏差权衡与数据增强效果。实证部分以 COVID-19 风险预测模型为例，展示在大型 Midwestern 医疗系统中的应用。对您有用：本文将 counterfactual fairness 与因果推断的 identification/estimation 结合，且涉及外部数据缺失结局的借信息问题，与您在 causal inference（identification, estimation）和 semiparametric theory 上的兴趣直接相关。
- **关键技术**: `counterfactual fairness`, `cross-group estimands`, `data borrowing with missing outcomes`, `treatment confounding adjustment`, `risk prediction fairness`
- **为什么对您有用**: 本文直接连接 causal inference 的 identification/estimation 子方向，特别是 counterfactual framework 下处理 treatment confounding 的 estimand 设计。您可以用 semiparametric efficiency theory（moderately_familiar）分析其跨群借信息 estimands 的效率界，或用 M-estimation theory 推导外部数据缺失结局情形下 estimator 的渐近性质。中期可做：需先在 semiparametric theory 上长肌肉以严格推导 efficiency bound 和 influence function。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1093/biostatistics/kxaf047](https://doi.org/10.1093/biostatistics/kxaf047) · [arXiv](https://arxiv.org/abs/2504.21710) — While-alive regression analysis of composite survival endpoints
- **作者**: Xi Fang, Hajime Uno, Fan Li
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在复合生存终点（含终止事件）设定下，本文针对 exposure-weighted while-alive 累积频率度量提出回归框架，目标是估计协变量对广义 while-alive 损失率的时间变化效应。核心估计量采用样条建模时变关联，结合逆概率加权处理终止事件的 censoring，并在独立与聚类数据两种设定下推导了估计量的渐近性质（一致性、n^{-1/2}-CAN）。模拟与两项随机临床试验数据验证了方法操作特性，配套 R 包 WAreg 已发布。对您可能有用：本文的样条 M-估计与聚类数据渐近理论可作为 semiparametric 回归框架的参考案例，尤其适合与您熟悉的 M-estimation theory 和 semiparametric theory 对接。
- **关键技术**: `exposure-weighted while-alive measure`, `spline M-estimation`, `inverse probability weighting`, `cluster-correlated data asymptotics`, `n^{-1/2}-CAN`
- **为什么对您有用**: 本文连接到 semiparametric & nonparametric theory 子方向，具体是样条 M-估计与聚类数据下的渐近理论。您武器库中 moderately_familiar 的 M-estimation theory 可直接攻这篇的估计量渐近推导口子，验证其 influence function 与效率性质是否可进一步优化。follow-up 粗判：立即可做——用 very_familiar 的非参统计与 moderately_familiar 的 M-estimation theory 即可展开阅读与复现。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1093/biostatistics/kxae046](https://doi.org/10.1093/biostatistics/kxae046) · [arXiv](https://arxiv.org/abs/2311.16375) — Testing for a difference in means of a single feature after clustering
- **作者**: Yiqun T Chen, Lucy L Gao
- **期刊/来源**: Biostatistics
- **机构**: Stanford University
- **分类**: vol 26 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在聚类后对单一特征均值差异进行假设检验的设定下，目标是检验两个估计聚类之间某特征的均值是否不同；经典检验因聚类选择依赖同一数据而导致 Type I error 膨胀。本文针对 hierarchical 或 k-means 聚类后的两聚类，提出一种基于 selective inference 框架的新检验：将聚类选择事件纳入条件推断，修正选择偏差，在有限样本下控制 selective Type I error rate，且计算高效。核心机制是对聚类选择事件进行精确刻画与条件化，从而在 selection-adjusted 的 null 分布下进行检验。模拟与单细胞 RNA-seq 数据实证验证了 Type I error 控制与 power。对您可能有用：本文将 selective inference 应用于聚类后检验，直接连接 hypothesis testing 与 post-selection inference 子方向。
- **关键技术**: `selective inference`, `selective Type I error`, `post-clustering hypothesis testing`, `finite-sample error control`, `selection event conditioning`, `hierarchical/k-means clustering selection region`
- **为什么对您有用**: (1) 直接连接 primary interest 中 hypothesis testing 的 selective/post-selection inference 子方向——聚类后检验是数据驱动选择后推断的典型场景；(2) 研究者的 minimax bounds（very_familiar）可用来分析该检验在高维多特征或多聚类设定下的 power 性质与最优性，M-estimation theory（moderately_familiar）可帮助将框架扩展到其他聚类算法或 semiparametric 模型；(3) **中期可做**：需先在 selective inference 的条件推断与选择事件刻画技术上长肌肉（moderately_familiar 的 M-estimation theory 可部分迁移，但 selective conditioning 的具体技术细节目前缺），之后可攻高维/多聚类扩展。

### 2. [10.1093/biostatistics/kxaf050](https://doi.org/10.1093/biostatistics/kxaf050) — High-dimensional inference for functional regression with an application to the Alzheimer’s disease magnetoencephalography study
- **作者**: Huaqing Jin, Fei Jiang
- **期刊/来源**: Biostatistics
- **机构**: Tsinghua University · University of California, San Francisco
- **分类**: vol 26 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在高维函数回归设定下，本文目标是针对函数型协变量构建高维假设检验（HDHT）框架，以克服传统基于功率谱密度特征提取的信息损失及函数回归变量选择的不稳健性。作者提出了一个针对函数型协变量的 HDHT 框架，并引入了严格的推断过程以支撑科学结论。理论方面，本文建立了该 HDHT 框架的渐近性质（摘要未详述具体收敛率与检验功效界，但声称有严格理论保证）。模拟验证了方法性能，并在阿尔茨海默病（AD）脑磁图（MEG）数据中应用，识别出19个与认知功能相关且符合AD病理生理学的关键脑区。对您可能有用：本文将高维假设检验拓展至函数型数据设定，直接连接了您的高维统计与假设检验兴趣，同时提供了临床神经科学数据的应用范式。
- **关键技术**: `high-dimensional hypothesis testing`, `functional linear regression`, `inference for functional covariates`, `MEG data analysis`, `robust alternative to variable selection`
- **为什么对您有用**: 本文直接连接到您的高维假设检验（primary interest）与流行病学/临床数据应用（secondary interest）的具体子方向。您可以用 `technical_arsenal` 中的 high-dimensional asymptotics (very_familiar) 来审视其 HDHT 框架的渐近理论是否紧致，或用 minimax bounds 验证其检验功效界。Follow-up 粗判：**中期可做**——需先在 moderately_familiar 的 M-estimation theory 或函数型数据推断上长肌肉，才能深入剖析其函数型高维检验的极限分布构造与功效分析。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1093/biostatistics/kxaf029](https://doi.org/10.1093/biostatistics/kxaf029) — Bayesian scalar-on-tensor regression using the Tucker decomposition for sparse spatial modeling
- **作者**: Daniel A Spencer, Rene Gutierrez, Rajarshi Guhaniyogi, Russell T Shinohara, Raquel Prado, Alzheimer’s Disease Neuroimaging Initiative et al.
- **期刊/来源**: Biostatistics
- **机构**: Winchester Hospital · The University of Texas at El Paso · Texas A&M University · University of Pennsylvania · University of California, Santa Cruz
- **分类**: vol 26 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在 scalar-on-tensor 回归设定下，目标是估计高维 tensor covariate 对 scalar response 的关联系数 tensor，同时保留空间结构并控制参数维度。本文提出 Bayesian Tucker 分解方法：将系数 tensor 分解为 core tensor 加因子矩阵乘积，大幅降低自由参数数量，并在 core tensor 上施加 sparsity-inducing regularization（如 spike-and-slab prior）。模拟实验对比了近期 tensor regression 方法（如 CP 分解 Bayesian 方法），ADNI 神经影像数据分析显示推断性能优于其他方法。理论贡献主要在模型设计层面，未给出 minimax rate 或 efficiency bound。对您而言，Tucker 分解的参数缩减机制与 tensor contraction 计算复杂度有间接关联，但核心 Bayesian modeling 路线与您的 U-statistic einsum 视角差异较大。
- **关键技术**: `Tucker tensor decomposition`, `Bayesian spike-and-slab regularization`, `scalar-on-tensor regression`, `core tensor sparsity prior`, `MCMC posterior inference`
- **为什么对您有用**: 本文属于 stat_computing / tensor 方向，但与您 primary interest 的具体子方向（U-statistic 的 einsum/treewidth 计算复杂度）交集有限——Tucker 分解在此是统计建模工具而非计算复杂度分析对象。technical_arsenal 中 tensor contraction / einsum 可用于分析 Tucker 分解系数估计的计算代价，但本文未触及此问题。follow-up 判断：**中期可做**——若想在 tensor regression 的计算复杂度上切入，需先在 moderately_familiar 的 M-estimation theory 上补充 Bayesian tensor 模型的 frequentist 对应，再用 very_familiar 的 einsum/treewidth 分析 Tucker 结构下估计量的计算瓶颈。

## 流行病学  *(epidemiology, 8 篇)*

### 1. [10.1093/biostatistics/kxaf044](https://doi.org/10.1093/biostatistics/kxaf044) · [arXiv](https://arxiv.org/abs/2404.11675) — Decomposition of longitudinal disparities: an application to the fetal growth-singletons study
- **作者**: Sang Kyu Lee, Seonjin Kim, Mi-Ok Kim, Katherine L Grantz, Hyokyoung G Hong
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文将经典 Peters–Belson 分解扩展至纵向设定，目标 estimand 是不同人口组间随时间演变的健康差异，关键假设是存在一个 modifier 变量与其它协变量交互。方法将差异分解为三部分：(i) 协变量条件分布差异在公共 modifier 分布下的贡献；(ii) modifier 分布差异及其与协变量交互的贡献；(iii) 未被观测协变量解释的残差。与传统将 (i)(ii) 合并为“已解释差异”的做法不同，本文允许分别刻画与 modifier 无关和有关的时间模式。实证分析基于胎儿生长纵向队列数据，展示种族/族裔群体间胎儿发育轨迹差异的动态分解。对您可能有用：该分解框架可视为纵向因果中介分析的变体，modifier 的角色类似中介变量，为纵向差异的 identification 与 estimation 提供了新视角。
- **关键技术**: `Peters-Belson decomposition`, `longitudinal disparity decomposition`, `modifier-interaction partitioning`, `conditional distribution weighting`, `fetal growth trajectory modeling`
- **为什么对您有用**: 本文连接到流行病学队列数据的因果分解方法，Peters–Belson 分解与因果中介分析在 identification 上有结构相似性（modifier ≈ mediator）。用您 very_familiar 的因果推断 identification theory 可以审视其分解的 identification 假设是否可进一步放松或与 longitudinal mediation 统一；moderately_familiar 的 semiparametric theory 可用于探讨三成分估计的 semiparametric efficiency bound。Follow-up 判断：中期可做——需先在 longitudinal causal mediation 的 identification 上长肌肉，再审视该分解框架的效率理论。

### 2. [10.1093/biostatistics/kxaf038](https://doi.org/10.1093/biostatistics/kxaf038) · [arXiv](https://arxiv.org/abs/2501.14097) — Assessing treatment efficacy for interval-censored endpoints using multistate semi-Markov models fit to multiple data streams
- **作者**: Raphaël Morsomme, C Jason Liang, Allyson Mateja, Dean A Follmann, Meagan P O’Brien, Chenguang Wang et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文在多状态半 Markov 模型框架下，利用多条可能存在区间删失的数据流（症状 onset、RT-qPCR、血清学）估计复杂生物医学终点的处理效应。目标 estimand 为 REGEN-COV 单抗组合对无症状感染的 protective efficacy (PE)、感染后血清转换率及病毒脱落持续时间。核心算法采用 Monte Carlo EM 结合 importance sampling 处理边际似然不可解析的问题，实现了对区间删失数据拟合半参数半 Markov 模型的计算可行性，相比现有方法有显著计算改进。实证结果显示 REGEN-COV 降低无症状感染风险与病毒脱落时长，并降低无症状感染者的血清转换率。对您可能有用：该文在流行病学试验中用半 Markov 模型处理区间删失多数据流，其 MCEM+IS 计算方案与您在统计计算和因果推断估计理论的兴趣有交叉。
- **关键技术**: `multistate semi-Markov model`, `Monte Carlo EM`, `importance sampling`, `interval-censored data`, `protective efficacy estimation`, `semi-parametric likelihood`
- **为什么对您有用**: 本文属于流行病学应用，用多状态半 Markov 模型处理区间删失多数据流估计 PE，与您 causal inference 中 longitudinal/mediation 设定有概念连接。技术层面，MCEM+IS 方案属于您 very_familiar 的统计计算范畴，可直接审视其计算效率声称；但半 Markov 模型的半参数推断理论（influence function / efficiency bound）本文未深入，您可用 moderately_familiar 的 semiparametric theory 攻其效率界缺口。Follow-up 判断：中期可做——需先在 moderately_familiar 的 semiparametric theory 上长肌肉，推导该半 Markov 区间删失设定的 semiparametric efficiency bound。

### 3. [10.1093/biostatistics/kxaf039](https://doi.org/10.1093/biostatistics/kxaf039) — Network generalized estimating equations for complexly correlated data with applications to cluster randomized trials
- **作者**: Tom Chen, Fan Li, Rui Wang
- **期刊/来源**: Biostatistics
- **机构**: Cancer Research And Biostatistics · Harvard Pilgrim Health Care · Yale University · Yale New Haven Health System
- **分类**: vol 26 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在 cluster randomized trials (CRTs) 设定下，目标是估计均值参数与复杂关联结构参数，传统 GEE 仅处理简单/嵌套交换结构。本文提出 network GEE 框架，将观测划分为可能重叠的局部交换群组以建模复杂相关（multiple exchangeable、moving average、exponential decay），并给出相应 working correlation matrix 的参数化。大簇场景下计算复杂度陡增，作者开发了 networkGEE R 包以实现现有软件无法拟合的模型。模拟验证了估计效率与稳健性，实证分析使用了 Washington State Expedited Partners Therapy stepped-wedge CRT 数据。对您而言，本文将网络拓扑引入 GEE working correlation 的思路，可为流行病学 CRT 数据的因果效应估计提供更灵活的方差–协方差建模工具。
- **关键技术**: `generalized estimating equations`, `network working correlation`, `locally exchangeable groups`, `stepped-wedge CRT`, `sandwich variance estimator`, `networkGEE R package`
- **为什么对您有用**: 本文连接到流行病学因果推断应用（stepped-wedge CRT 的效应估计），其 network working correlation 建模可提升 CRT 中 ATE 估计的效率与稳健性。您武器库中的 M-estimation theory 与 semiparametric theory 可直接审视其 GEE 求解器的收敛性质与 sandwich variance 的渐近有效性。follow-up 判断：立即可做——用 very_familiar 的软件开发能力复现/扩展 networkGEE，结合 moderately_familiar 的 M-estimation theory 探究其效率边界。

### 4. [10.1093/biostatistics/kxaf045](https://doi.org/10.1093/biostatistics/kxaf045) · [arXiv](https://arxiv.org/abs/2507.06451) — Determining vaccine responders in the presence of baseline immunity using single-cell assays and paired control samples
- **作者**: Zhe Chen, Siyu Heng, Asa Tapley, Stephen De Rosa, Bo Zhang
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在疫苗免疫原性评估设定下，目标是利用 ICS 单细胞数据识别疫苗应答者，同时处理基线免疫与批次效应导致的误分类问题。本文提出一个整合配对对照样本的新统计框架：通过最小与最大调整 P 值分别施加最保守与最宽松的批次效应校正，前者保证 Type I error 在所有与对照数据一致的批次效应下有效，后者仅做使调整后 P 值不被对照数据否证的最小修正。两个 P 值共同构成一个灵敏度分析区间，平衡了批次效应未知时的假阳性与假阴性。应用于 CoVPN 3008 COVID-19 疫苗试验数据，识别 Omicron 感染与 T 细胞应答。对您可能有用：该框架本质上是配对样本下对未观测批次效应的 partial identification / sensitivity analysis，与您在 causal inference sensitivity analysis 的兴趣直接相连。
- **关键技术**: `paired control sample adjustment`, `maximally adjusted p-value`, `minimally adjusted p-value`, `batch effect sensitivity analysis`, `single-cell ICS assay`, `vaccine responder classification`
- **为什么对您有用**: 本文直接连接到 epidemiology 应用中的 causal inference sensitivity analysis 子方向——配对对照样本下的批次效应校正本质上是对未观测混杂的 partial identification，与您在 proximal CI / sensitivity analysis 的 primary interest 对应。您可以用 very_familiar 的 minimax bounds 工具分析该框架的 maximally/minimally adjusted P 值区间是否紧，或用 moderately_familiar 的 identification theory 将其形式化为一个 formal sensitivity model。Follow-up 判断：中期可做——需先在 moderately_familiar 的 identification theory 上将批次效应模型形式化为 causal sensitivity model，再推导 sharper bounds。

### 5. [10.1093/biostatistics/kxaf037](https://doi.org/10.1093/biostatistics/kxaf037) — Meta-analysis models with group structure for pleiotropy detection at gene and variant level using summary statistics from multiple datasets
- **作者**: Pierre-Emmanuel Sugier, Yazdan Asgari, Mohammed Sedki, Thérèse Truong, Benoit Liquet
- **期刊/来源**: Biostatistics
- **机构**: Centre National de la Recherche Scientifique · Université de Pau et des Pays de l'Adour · Inserm · Université de Versailles Saint-Quentin-en-Yvelines · Université Paris Cité · Université Paris-Saclay · Institut Gustave Roussy · Sorbonne Paris Cité 等
- **分类**: vol 26 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文在多 GWAS summary statistics 的 meta-analysis 设定下，目标是检测基因/变异层面的 pleiotropy（一基因影响多表型）。现有方法逐个检验 pleiotropic association，无法同时利用所有遗传信息与嵌套的 group structure（variant → gene/pathway）。作者提出 MPSG 方法：penalized multivariate meta-analysis，引入 group-lasso 型惩罚以同时选择相关 variant 与 gene/pathway，并实现 ADMM 算法求解。模拟对比 GCPBayes、PLACO、ASSET 等基准方法，展示不同 summary statistics 输入下的性能差异；实证应用于乳腺癌与甲状腺癌的 pleiotropic gene 识别。对您可能有用：若关注流行病学多表型因果结构的联合推断，MPSG 的 group-penalized multivariate 框架提供了一种从 summary-level 数据做变量选择的计算方案。
- **关键技术**: `penalized multivariate meta-analysis`, `group-lasso penalty`, `ADMM algorithm`, `GWAS summary statistics`, `pleiotropy detection`
- **为什么对您有用**: 本文属于流行病学/遗传学应用，连接到您 secondary interest 中的 epidemiology 数据集与多表型因果推断。技术层面，MPSG 的 group-penalized multivariate meta-analysis 与 ADMM 算法属于您 very_familiar 的软件开发与 moderately_familiar 的 M-estimation 理论范畴，理论上可尝试用 semiparametric efficiency 或 HOIF 视角分析其选择一致性/收敛率。follow-up 判断：中期可做——需先在 moderately_familiar 的 M-estimation 理论上长肌肉，以推导 group-penalized multivariate estimator 的 oracle 性质与 post-selection inference。

### 6. [10.1093/biostatistics/kxaf028](https://doi.org/10.1093/biostatistics/kxaf028) · [arXiv](https://arxiv.org/abs/2407.19135) — Bayesian mapping of mortality clusters
- **作者**: Andrea Sottosanti, Enrico Bovo, Pietro Belloni, Giovanna Boccuzzo
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在空间疾病映射设定下，目标是识别多死因死亡率的空间聚类边界及驱动聚类的疾病组合，核心假设为相邻区域呈现相似死亡率水平且仅部分死因对聚类有贡献。提出 perla——多变量贝叶斯聚类模型，将空间邻接结构通过 stick-breaking 多项分布参数化嵌入聚类概率，并用 global-local shrinkage prior 自动筛选有信息量死因、压缩无信息死因的影响。MCMC 推断几乎全为闭式 Gibbs 步，无需复杂调参。实证基于意大利 ULSS6 Euganea 及美国 county 死亡率数据，模拟实验验证聚类检测的灵活性。对您而言，本文提供流行病学空间死亡率数据集，但方法（贝叶斯 stick-breaking 聚类 + shrinkage prior）与您主攻的因果推断/半参数效率理论无直接技术对接。
- **关键技术**: `stick-breaking multinomial construction`, `global-local shrinkage prior`, `Bayesian spatial cluster model`, `Gibbs sampling with closed-form updates`, `multivariate disease mapping`, `spatial adjacency prior`
- **为什么对您有用**: 本文落入流行病学（secondary interest）范畴，提供了意大利及美国 county 层级多死因死亡率空间数据集，但并非因果推断工作，无 IV / DML / semiparametric 方法成分。武器库中无直接攻此文的口子——stick-breaking 非参构造、global-local shrinkage prior、Bayesian spatial CAR 模型均不在 very_familiar 或 moderately_familiar 中。暂不可做：若要进入 Bayesian spatial clustering 方向需先补 Bayesian nonparametric 与 spatial prior 基础，与当前主攻方向偏离较大，建议仅浏览数据集部分。

### 7. [10.1093/biostatistics/kxaf034](https://doi.org/10.1093/biostatistics/kxaf034) · [arXiv](https://arxiv.org/abs/2410.16617) — Markov switching zero-inflated space-time multinomial models for comparing multiple infectious diseases
- **作者**: Dirk Douwes-Schultz, Alexandra M Schmidt, Laís Picinini Freitas, Marilia Sá Carvalho
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文提出 Markov switching zero-inflated space-time multinomial 模型，用于比较多种共循环传染病在不同区域与时段的传播动态；estimand 为各疾病相对传播强度及与协变量（如温度）的关联，regularity 假设包括基线疾病始终存在、其余疾病通过耦合 Markov chain 切换存在/缺席状态。核心机制：耦合 Markov chain 刻画长期零值、疾病交互与空间扩散；存在时计数服从自回归 multinomial；推断采用联合采样所有未知存在指标的 Bayesian MCMC。实证结果为里约热内卢登革/寨卡/基孔肯雅三重流行数据的时空模式比较。对您而言，本文是流行病学多疾病时空计数数据的完整建模案例，可作为 secondary interest 中流行病学数据集与应用因果工作的入门阅读。
- **关键技术**: `Markov switching model`, `zero-inflated spatio-temporal count model`, `autoregressive multinomial model`, `coupled Markov chains for presence indicators`, `Bayesian MCMC with joint sampling`
- **为什么对您有用**: 本文连接 secondary interest 中流行病学数据集与多疾病时空建模，提供了真实多结局计数数据结构与贝叶斯建模惯例的 gateway reading；武器库中软件开发与 M-estimation 理论可支撑理解其 MCMC 实现与模型拟合细节，但因果 identification/semiparametric efficiency 工具不直接适用于此贝叶斯设定。若想将多疾病相对传播强度问题转向因果 identification 与 semiparametric estimation，需中期积累——先在 moderately_familiar 的 identification theory 上结合多结局 longitudinal 设定做延伸；作为入门读物值得花时间读全文以熟悉数据结构与建模语言，但方法学迁移非立即可做。

### 8. [10.1093/biostatistics/kxaf048](https://doi.org/10.1093/biostatistics/kxaf048) · [arXiv](https://arxiv.org/abs/2407.19171) — Assessing spatial disparities: a Bayesian linear regression approach
- **作者**: Kyle Wu, Sudipto Banerjee
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在区域聚合空间流行病学数据设定下，研究目标是检测相邻区域间的空间健康差异（spatial disparity），即划定疾病死亡率地图上显著不同的邻域边界。作者在贝叶斯线性回归框架中引入空间自回归结构（spatial autoregression），提供模型驱动的空间差异检测与概率推断。核心方法贡献在于推导出可利用的分析 tractability（利用共轭结构避免全空间 MCMC 采样），大幅加速计算。模拟实验在全美县级地图上验证方法有效性，实证分析使用 IHME 美国县级肺癌年龄标准化死亡率数据。对您而言，本文提供了流行病学空间数据（IHME county-level dataset）的一个建模入口，但方法学 novelty 主要在贝叶斯空间模型的计算加速而非因果推断或半参数效率理论。
- **关键技术**: `Bayesian spatial autoregression`, `Womble boundary detection`, `analytical tractability via conjugacy`, `spatial disparity probabilistic inference`, `IHME county-level mortality data`
- **为什么对您有用**: 本文连接到流行病学 secondary interest 中的空间健康差异与县级死亡率数据集（IHME），提供了一个带真实数据的空间建模案例。方法学上，其'analytical tractability'加速计算属于 stat_computing 方向，但具体是贝叶斯共轭结构的利用而非您武器库中的 tensor contraction / einsum 复杂度分析，因此技术迁移口子不大。Follow-up 判断：**中期可做**——若想进入空间流行病学建模方向，需先补充空间统计基础（CAR/SAR 模型、Gaussian process on graphs），当前 very_familiar 武器库不直接覆盖空间自回归模型。

## 其他  *(other, 1 篇)*

### 1. [10.1093/biostatistics/kxaf012](https://doi.org/10.1093/biostatistics/kxaf012) — Addressing the mean–variance relationship in spatially resolved transcriptomics data with <i>spoon</i>
- **作者**: Kinnary Shah, Boyi Guo, Stephanie C Hicks
- **期刊/来源**: Biostatistics
- **机构**: Johns Hopkins University
- **分类**: vol 26 · issue 1
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文针对空间转录组学（SRT）数据中识别空间变异基因（SVG）的任务，指出log变换后存在技术偏差：高表达基因的原始计数方差大，但log变换后方差反而变小，破坏了均值-方差关系。作者在SRT数据中实证了这一偏差，并提出spoon框架，利用经验贝叶斯（empirical Bayes）技术校正该偏差，从而更准确地优先排序SVG。模拟与真实SRT数据均验证了spoon的有效性。对您而言，本文主要展示了经验贝叶斯在生物计数数据方差校正中的具体应用，但与因果推断、高维/半参数效率等核心方向无直接技术交叉。
- **关键技术**: `empirical Bayes shrinkage`, `mean-variance relationship correction`, `spatially variable gene detection`, `log-transformation bias`, `proportion of spatial variance`
- **为什么对您有用**: 本文属于生物统计应用，核心是经验贝叶斯方差校正，与您primary interest中的因果推断、高维RMT、半参数效率等无直接技术对接。若您对经验贝叶斯在计数数据中的具体实现感兴趣，可作为轻量阅读，但无需深入。follow-up判断：暂不可做——核心机器（经验贝叶斯先验构造、SRT空间模型）不在武器库，且与您当前研究方向无实质交叉。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

