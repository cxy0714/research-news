# Biostatistics — Vol 25  Issue 4  ·  2026-05-21

- 共 19 篇 · Biostatistics

## 因果推断  *(causal_inference, 5 篇)*

### 1. [10.1093/biostatistics/kxae006](https://doi.org/10.1093/biostatistics/kxae006) — Mendelian randomization analysis using multiple biomarkers of an underlying common exposure
- **作者**: Jin Jin, Guanghao Qi, Zhi Yu, Nilanjan Chatterjee
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 1015-1033
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在孟德尔随机化(MR)框架下，针对潜在暴露（如系统性炎症）不可直接观测但存在多个共调节生物标志物的设定，目标是检验潜在暴露对疾病结局的因果效应方向与显著性。作者提出 MRLE 方法，基于结构方程模型(SEM)，利用可观测性状的 GWAS 汇总统计量的二阶矩构造估计函数。该方法允许遗传变异通过潜在暴露产生间接效应，同时允许对性状的直接效应（即多效性 pleiotropy）。相比单性状 MR 检验，MRLE 通过整合多个相关生物标志物的信息，在多种多效性设定下提升了检验效能并严格控制了第一类错误。实证分析整合五种炎症生物标志物，发现了炎症增加冠心病等疾病风险的因果证据，而标准单标志物 MR 无法一致检测。对您可能有用：该文将 IV 方法拓展至潜变量结构方程设定，利用二阶矩实现 identification，对您在因果推断（IV/潜变量）及流行病学应用方向有直接参考价值。
- **关键技术**: `Mendelian randomization`, `latent exposure`, `structural equation model`, `second-order moments`, `GWAS summary statistics`, `pleiotropy`
- **为什么对您有用**: 该文将 IV 方法拓展至潜在暴露的结构方程设定，利用二阶矩实现 identification，对您在因果推断（IV 方法与潜变量）及流行病学应用方向有直接参考价值；同时其基于汇总统计量的假设检验思路也可为高维/半参数推断提供启发。

### 2. [10.1093/biostatistics/kxae002](https://doi.org/10.1093/biostatistics/kxae002) — Estimation of optimal treatment regimes with electronic medical record data using the residual life value estimator
- **作者**: Grace Rhodes, Marie Davidian, Wenbin Lu
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 933-946
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在纵向电子病历(EMR)数据设定下，本文研究如何估计以累积受限剩余寿命(cumulative restricted residual life)为奖励函数的最优动态治疗策略(DTR)。核心估计量 ReLiVE 通过逆概率加权(IPW)结构估计给定策略下的期望累积受限剩余寿命，目标参数为 E[max(min(T−t,τ),0)]，其中 T 为生存时间、τ 为限制窗口。在此基础上，ReLiVE-Q 将 Q-learning 的反向归纳算法与 ReLiVE 结合，逐决策点拟合 Q 函数并选择最大化剩余寿命的治疗规则。模拟研究展示了 ReLiVE-Q 在有限样本下的表现，实证分析使用 MIMIC-III 数据库估计脓毒症 ICU 患者的最优序贯治疗策略。对您而言，本文将 DTR/Q-learning 框架扩展至剩余寿命这一生存型奖励，属于纵向因果推断的应用方法拓展，同时 MIMIC 数据集对流行病学因果应用有参考价值。
- **关键技术**: `Q-learning`, `dynamic treatment regime`, `inverse probability weighting`, `restricted residual life`, `backward induction`, `survival-reward estimation`
- **为什么对您有用**: 直接连接您 primary interest 中的纵向因果推断(DTR/序贯决策)与 secondary interest 中的流行病学应用，MIMIC 数据集及生存型奖励的 DTR 建模思路可迁移至其他重症医学因果问题。

### 3. [10.1093/biostatistics/kxad035](https://doi.org/10.1093/biostatistics/kxad035) — Bayesian semiparametric model for sequential treatment decisions with informative timing
- **作者**: Arman Oganisian, Kelly D Getz, Todd A Alonzo, Richard Aplenc, Jason A Roy
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 947-961
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在纵向因果推断设定下，本文研究动态治疗策略（DTR）对生存率的影响，需同时处理时间依赖性混杂、信息性治疗时间以及竞争性删失。提出基于 Gamma Process 先验的贝叶斯半参数生成模型，在连续时间尺度上刻画患者向下一治疗阶段或死亡的转移过程。利用 G-computation 计算调整时间依赖性混杂后的潜在生存概率后验分布，Gamma Process 的引入避免了对转移时间的强参数假设。在儿童急性髓系白血病临床试验数据中，评估了基于心脏功能动态调整蒽环类药物的假设规则疗效。对您有用：该文将贝叶斯半参数建模与纵向 G-computation 结合，处理了连续时间信息性观测时间这一棘手问题，对您在纵向因果推断及半参数理论方面的研究有直接的方法论借鉴价值。
- **关键技术**: `Bayesian semiparametric model`, `Gamma Process priors`, `G-computation`, `Dynamic treatment regimes`, `Time-varying confounding`, `Informative timing`
- **为什么对您有用**: 直接涉及您 primary interest 中的纵向因果推断与半参数理论，其处理连续时间信息性观测时间的方法及贝叶斯 G-computation 框架，为时间依赖性混杂下的 DTR 估计提供了新思路；同时作为流行病学/临床试验的应用因果工作，数据结构具有参考价值。

### 4. [10.1093/biostatistics/kxae012](https://doi.org/10.1093/biostatistics/kxae012) — Practical causal mediation analysis: extending nonparametric estimators to accommodate multiple mediators and multiple intermediate confounders
- **作者**: Kara E Rudolph, Nicholas T Williams, Ivan Diaz
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 997-1014
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在因果中介分析框架下，本文研究在存在多变量中介和多变量暴露后中间混杂因子时，interventional direct/indirect effects (IDE/IIE) 的非参数估计问题。传统 IDE/IIE 估计量无法同时处理多变量中介与中间混杂，而单独考察某子群中介时，其余中介即自然成为中间混杂。作者扩展了近期提出的非参数估计量，通过引入中介的联合分布建模及条件期望的嵌套估计，同时容纳多变量中介与中间混杂。该估计量基于 efficient influence function 构建，具备 n^{-1/2}-CAN 性质并在正则条件下达到半参数有效界。实证部分将该方法应用于 Section 8 住房券对青少年情绪障碍的间接效应分析，展示了拆解多中介子群时处理共发中间变量的策略。对您有用：该工作直接推进了您关注的 causal inference (mediation, longitudinal) 与 nonparametric theory 交叉方向，提供了一套处理多中介/中间混杂的实用非参数估计框架，可迁移至流行病学队列数据的因果中介分析。
- **关键技术**: `interventional indirect effects (IIE)`, `multiple mediators`, `intermediate confounders`, `efficient influence function`, `nonparametric estimation`
- **为什么对您有用**: 直接对应您 primary interest 中的 causal inference (mediation, longitudinal) 与 nonparametric theory，解决了多中介设定下中间混杂的识别与估计难题，且实证部分展示了流行病学数据的应用范式。

### 5. [10.1093/biostatistics/kxad018](https://doi.org/10.1093/biostatistics/kxad018) — Identifying predictors of resilience to stressors in single-arm studies of pre–post change
- **作者**: Ravi Varadhan, Jiafeng Zhu, Karen Bandeen-Roche
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 1094-1111
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在单臂前后测量研究中，识别影响韧性（resilience）的预测因子时，直接回归变化量与基线会因数学耦合和向均值回归（RTM）导致估计偏差。本文提出一种基于反事实对照组的校正方法，通过设定对照组参数进行敏感性分析来消除偏差，且仅需极少的分布假设。该方法将模型扩展至包含协变量，并允许利用外部数据约束敏感性分析的参数空间。模拟研究验证了方法的有效性；在全膝关节置换（TKR, N=7239）的真实数据应用中，校正后的分析揭示基线功能与恢复不再强相关，仅年龄和合并症数量与恢复负相关。对您有用：该文在缺乏对照组时的因果识别策略及配套的敏感性分析框架，可直接迁移至流行病学队列或纵向因果推断中处理基线偏差的问题。
- **关键技术**: `counterfactual control group`, `sensitivity analysis`, `regression to the mean correction`, `mathematical coupling`, `pre-post change estimation`
- **为什么对您有用**: 该文针对单臂研究提出的反事实对照组与敏感性分析框架，直接契合您在因果推断（敏感性分析）与流行病学应用中的兴趣，为处理纵向/观察性数据中的基线偏差提供了可迁移的识别策略。

## 非参数 / 半参数  *(nonparam_semipara, 4 篇)*

### 1. [10.1093/biostatistics/kxad033](https://doi.org/10.1093/biostatistics/kxad033) — Similarity-based multimodal regression
- **作者**: Andrew A Chen, Sarah M Weinstein, Azeez Adebimpe, Ruben C Gur, Raquel E Gur, Kathleen R Merikangas et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 1122-1139
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 在多模态数据（影像、移动健康、物理活动等）融合回归中，不同模态的维度与数据结构差异大，现有矩阵融合方法难以直接整合。本文将单模态 multivariate distance matrix regression (MDMR) 推广至多模态设定，提出 SiMMR，通过各模态的距离轮廓（distance profiles）同时回归临床变量。方法比较了多种 test statistic（似然比型、F 型等），采用 permutation test 进行推断；距离矩阵的构建本质上涉及 pairwise distance，与 U-statistics 有内在联系。模拟与影像/纵向移动健康实证表明，SiMMR 在有限样本下仍可检测多模态关联，并给出了不同场景下检验统计量的选择建议。对您有用：MDMR 的距离矩阵构造与 higher-order U-statistics 及非参数假设检验直接相关，多模态融合框架可迁移至流行病学多源数据的关联/因果分析。
- **关键技术**: `multivariate distance matrix regression`, `permutation-based inference`, `distance profile fusion`, `nonparametric association test`, `pairwise distance matrix`
- **为什么对您有用**: 距离矩阵回归的 pairwise distance 构造与您关注的 higher-order U-statistics 及非参数假设检验直接相连；多模态融合框架可迁移至流行病学多源数据的关联分析（secondary interest）。

### 2. [10.1093/biostatistics/kxae024](https://doi.org/10.1093/biostatistics/kxae024) — Neuroimaging meta regression for coordinate based meta analysis data with a spatial model
- **作者**: Yifan Yu, Rosario Pintos Lobo, Michael Cody Riedel, Katherine Bottenhorn, Angela R Laird, Thomas E Nichols
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 1210-1232
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在 coordinate-based meta-analysis (CBMA) 框架下，目标是估计脑激活空间强度函数并推断研究层面协变量（如发表年份、样本量）的效应，关键假设为激活焦点服从由平滑强度函数驱动的空间点过程。作者提出 generative CBMR 框架，以 spline 基展开参数化空间强度函数，纳入协变量回归，并比较四种焦点随机变异的随机模型（Poisson、负二项等）。方法基于 GLM 与空间点过程似然，sieve 式 spline 逼近实现非参数空间估计，计算效率优于 kernel-based 方法（ALE/MKDA）。在 20 个神经影像 meta-analytic 数据集上验证，进行 voxel 级空间齐性检验并与现有方法对比。对您而言，spline 参数化空间强度函数的 sieve 思路可迁移至其他空间点过程半参数估计，空间齐性检验的构造与 semiparametric 假设检验有方法论交叉。
- **关键技术**: `spline parameterization`, `spatial point process`, `coordinate-based meta-regression`, `generalized linear models`, `spatial homogeneity test`
- **为什么对您有用**: spline 参数化空间强度函数的 sieve 估计框架与 semiparametric theory 直接相关，空间齐性检验的构造对 hypothesis testing 方向有参考价值；但应用领域（神经影像）非您核心关注，方法论迁移需自行转化。

### 3. [10.1093/biostatistics/kxae010](https://doi.org/10.1093/biostatistics/kxae010) — Exponential family measurement error models for single-cell CRISPR screens
- **作者**: Timothy Barry, Kathryn Roeder, Eugene Katsevich
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 1254-1272
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在单细胞 CRISPR 筛选的设定下，目标是估计基因扰动对基因表达的因果效应，但标准 thresholded regression 因预测变量含测量误差而产生 attenuation bias，且偏差-方差权衡依赖一个难以选取的阈值参数。作者提出 GLM-EIV 方法，将经典 errors-in-variables 模型推广至响应与含噪预测变量均服从指数族分布、且可能受同一组混杂影响的情形。理论上证明了 thresholded regression 的 attenuation bias 机制，GLM-EIV 通过显式建模测量误差消除该偏差。计算方面开发了可在云端/高性能集群上跨数百处理器并行部署的基础设施，并应用于两个大规模单细胞 CRISPR 筛选数据集。EIV 框架与 proximal CI 中 negative control proxy 的测量误差结构高度同构，对您在 proximal CI 下研究 proxy 误差模型的 identification 与效率界有直接借鉴价值。
- **关键技术**: `errors-in-variables model`, `exponential family GLM`, `attenuation bias correction`, `confounding adjustment`, `parallel computing infrastructure`, `single-cell CRISPR screen`
- **为什么对您有用**: EIV 框架与 proximal CI 中 negative control proxy 的测量误差结构同构，GLM-EIV 对指数族响应的推广可为 proximal CI 下 proxy 误差模型的 identification 与估计提供新思路；并行计算基础设施对您统计计算方向也有参考价值。

### 4. [10.1093/biostatistics/kxae007](https://doi.org/10.1093/biostatistics/kxae007) — Functional support vector machine
- **作者**: Shanghong Xie, R Todd Ogden
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 1178-1194
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在 scalar-on-function 回归与分类设定下，传统线性模型对复杂非线性关系高度敏感，而标准 SVM 忽略了功能数据的高相关性且无法处理不规则观测。本文提出将功能主成分分析（FPCA）与 SVM 相结合的新方法：利用 FPCA 提取功能预测变量的连续特征以处理不规则观测与测量误差，再通过 SVM 捕捉标量响应与功能预测变量间的非线性关系。模拟与真实数据分析（EEG 信号分类、近红外光谱预测）表明，当功能预测变量测量误差较大时，该方法相比传统模型具有更优的预测表现。对您而言，该文展示了 FPCA 降维与核方法结合处理高维功能数据的计算策略，但缺乏半参数效率界或收敛率的深入理论，方法学新颖度有限。
- **关键技术**: `functional principal component analysis (FPCA)`, `support vector machine (SVM)`, `scalar-on-function regression`, `nonlinear classification`, `measurement error in functional predictors`
- **为什么对您有用**: 涉及非参数方法（SVM）与高维功能数据（FPCA）的结合，属于非参数理论的外围应用；但缺乏您关注的半参数效率或高维推断理论，主要价值在于了解功能数据下非参数建模的计算策略。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1093/biostatistics/kxae004](https://doi.org/10.1093/biostatistics/kxae004) — Projection-based two-sample inference for sparsely observed multivariate functional data
- **作者**: Salil Koner, Sheng Luo
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 1156-1177
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在稀疏纵向设计下，针对多变量函数型数据，本文研究两样本显著性检验问题，目标是检测多维度总体均值函数的组间差异，假设协方差结构属于非平稳的宽泛类别。方法基于多变量函数型主成分分析（MFPCA）进行投影降维，在保留各成分间动态相关性的同时将无限维问题转化为有限维。检验统计量基于投影后的均值差异构造，输出单一 p 值，避免了逐分量检验的多重比较校正问题。有限样本模拟表明该检验能控制第一类错误且功效优于现有方法。实证分析应用于阿尔茨海默病和帕金森病的纵向临床试验数据。对您有用：该文属于纵向数据的假设检验问题，其 MFPCA 投影构造检验统计量的思路可为您在纵向因果推断或高维半参数检验中的方法学开发提供参考，同时提供了流行病学队列的临床试验数据集。
- **关键技术**: `multivariate functional principal component analysis`, `projection-based two-sample test`, `sparse longitudinal functional data`, `non-stationary covariance structure`, `global testing`
- **为什么对您有用**: 直接契合您在数学统计（假设检验）和纵向数据方面的兴趣；MFPCA投影降维构造单一检验统计量的思路可迁移至高维/纵向因果推断的检验问题，且附带了流行病学（阿尔茨海默/帕金森）真实数据集。

### 2. [10.1093/biostatistics/kxad029](https://doi.org/10.1093/biostatistics/kxad029) — Signal detection statistics of adverse drug events in hierarchical structure for matched case–control data
- **作者**: Seok-Jae Heo, Sohee Jeong, Dagyeom Jung, Inkyung Jung
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 1112-1121
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在自发报告系统(SRS)的匹配病例-对照设计中，目标是检测药物不良反应信号；现有基于Bernoulli模型的树状扫描统计量未能考虑匹配对内的依赖性，导致I类错误膨胀。本文提出三种新统计量：基于McNemar检验、条件logistic回归的Wald检验、以及多项分布的似然比检验，在层级树状扫描框架下正确处理匹配对内相关性。模拟表明所提方法在I类错误率、功效、灵敏度和误检率上均优于现有Bernoulli方法。实证分析使用韩国不良反应报告系统数据库检测降压药相关的头晕不良事件信号。对您有用：将匹配病例-对照设计下的经典检验（McNemar / 条件logistic回归）与层级多重比较扫描框架结合，在流行病学药物安全监测场景中提供了可迁移的检验思路和真实数据集参考。
- **关键技术**: `tree-based scan statistic`, `McNemar's test`, `conditional logistic regression`, `multinomial likelihood ratio test`, `matched case-control design`, `signal detection in hierarchical data`
- **为什么对您有用**: 匹配病例-对照设计下的假设检验改进直接关联您的 hypothesis testing 兴趣，同时流行病学药物安全监测应用与您的 epidemiology secondary interest 对接，提供韩国不良反应报告系统真实数据集和分析流程参考。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1093/biostatistics/kxae016](https://doi.org/10.1093/biostatistics/kxae016) — Fast matrix completion in epigenetic methylation studies with informative covariates
- **作者**: Mélina Ribaud, Aurélie Labbe, Khaled Fouda, Karim Oualkacha
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 1062-1078
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在 DNA 甲基化 p ≫ n（位点数远大于样本数）的设定下，目标是利用少量高密度 WGBS 样本对大量低密度阵列样本进行矩阵补全。提出 LMCC (Linear Model of Coregionalisation with informative Covariates) 模型，将甲基化向量分解为固定效应（已知协变量）与潜在因子。核心机制是对固定和潜在系数向量在位点间分别施加高斯过程先验，以利用数据的功能性特征与空间相关性。模拟表明，当缺失机制与协变量相关时，引入协变量可显著提升补全精度，且算法在 p ≫ n 场景下计算高效。实证分析显示细胞类型、年龄等协变量有效改善了补全效果。对您可能有用：该文展示了 p ≫ n 设定下结合协变量的矩阵补全方法，对您的高维统计计算与算法设计方向有参考价值。
- **关键技术**: `matrix completion`, `Linear Model of Coregionalisation`, `Gaussian process prior`, `spatial correlation`, `fixed and latent factors`
- **为什么对您有用**: 论文处理 p ≫ n 下的矩阵补全问题，属于高维统计与统计计算交叉领域；虽然未涉及 RMT 或半参数效率，但其结合协变量与空间相关性的算法设计对您的高维/计算方向有一定参考价值。

### 2. [10.1093/biostatistics/kxae009](https://doi.org/10.1093/biostatistics/kxae009) — Bayesian joint modeling of multivariate longitudinal and survival outcomes using Gaussian copulas
- **作者**: Seoyoon Cho, Matthew A Psioda, Joseph G Ibrahim
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 962-977
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多元纵向与生存结局的联合建模中，传统随机效应模型实现困难且固定效应参数的解释条件化于随机效应。本文提出基于 Gaussian copula 的联合建模框架，允许直接指定边际模型，通过 copula 刻画纵向与生存结局间的依赖结构。核心创新是对 copula 中常见的无结构相关矩阵提出结构化分解（如自回归结构），在中小学本量下获得参数估计效率提升并显著降低计算复杂度。估计采用 MCMC 算法实现。模拟研究与乳腺癌临床试验（生活质量纵向数据+无病生存时间）的实证分析验证了方法有效性。对您而言，copula 框架下结构化相关矩阵的效率增益思路可迁移至 longitudinal causal inference 中的联合建模设定，且相关矩阵分解的降维策略对高维统计计算有参考价值。
- **关键技术**: `Gaussian copula`, `structured correlation decomposition`, `joint longitudinal-survival modeling`, `MCMC estimation`, `auto-regressive correlation structure`
- **为什么对您有用**: 结构化相关矩阵分解在中小学本下的效率提升与计算简化，可迁移至 longitudinal causal inference 的联合建模设定；乳腺癌流行病学数据集对 secondary interest 中的 epidemiology 应用有参考价值。

## 流行病学  *(epidemiology, 3 篇)*

### 1. [10.1093/biostatistics/kxae003](https://doi.org/10.1093/biostatistics/kxae003) — Dynamic models augmented by hierarchical data: an application of estimating HIV epidemics at sub-national level
- **作者**: Bao Le, Xiaoyue Niu, Tim Brown, Jeffrey W Imai-Eaton
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 1049-1061
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在 HIV 动态模型框架下，目标是在数据稀疏的亚国家层面同时估计患病率、发病率和死亡率，关键假设是同一国家内不同区域可通过层级结构共享信息。作者提出通过辅助数据（auxiliary data）将层级信息融入动态系统，而非直接在 HIV 动态模型中嵌入层级结构——后者因需联合估计多区域参数而计算复杂且耗时。该方法将层级信息借用与动态模型求解解耦，在保持原有计算效率的同时实现跨区域信息整合，改善了预测精度与不确定性评估。实证结果表明新模型在亚国家层面 HIV 估计中优于独立区域建模。对您而言，该文提供了层级动态模型计算简化的策略（统计计算方向），以及 HIV 亚国家估计的真实数据集与建模框架（流行病学应用方向）。
- **关键技术**: `dynamic epidemic model`, `hierarchical information borrowing`, `auxiliary data integration`, `sub-national prevalence estimation`, `uncertainty quantification`
- **为什么对您有用**: 连接到您的统计计算方向（层级动态模型的计算解耦与加速策略）和流行病学应用方向（HIV 亚国家估计的真实数据集），可借鉴其避免联合层级建模的计算简化思路。

### 2. [10.1093/biostatistics/kxae005](https://doi.org/10.1093/biostatistics/kxae005) — Tree-informed Bayesian multi-source domain adaptation: cross-population probabilistic cause-of-death assignment using verbal autopsy
- **作者**: Zhenke Wu, Zehang R Li, Irena Chen, Mengbing Li
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 1233-1253
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在口头尸检（VA）跨人群死因推断问题中，目标是估计特定死因死亡率分数（CSMF），假设各域症状条件分布存在异质性且相似性可由先验树结构编码。方法采用潜类别模型刻画多变量二元响应的条件分布，并引入沿预设根权树的 logistic stick-breaking 高斯扩散过程先验。通过节点特异的 spike-and-slab 先验实现数据驱动的域间信息自适应池化，后验推断采用可扩展的变分贝叶斯算法。模拟与验证数据集表明，该域适应方法提升了 CSMF 估计与个体死因分配的准确性。对您可能有用：该文属于流行病学死因推断应用，提供了真实数据集与贝叶斯域适应框架，其树结构先验与变分推断计算方案对处理异质性人群数据有参考价值，但理论深度不及您关注的半参数效率界。
- **关键技术**: `latent class model`, `logistic stick-breaking process`, `Gaussian diffusion tree prior`, `spike-and-slab prior`, `variational Bayes`, `domain adaptation`
- **为什么对您有用**: 属于流行病学应用方向，提供了跨人群死因推断的真实数据集与贝叶斯域适应方法；虽非您主攻的半参数/效率理论，但其处理异质性人群的树结构先验与变分计算方案可作应用参考。

### 3. [10.1093/biostatistics/kxae001](https://doi.org/10.1093/biostatistics/kxae001) — A Bayesian approach for investigating the pharmacogenetics of combination antiretroviral therapy in people with HIV
- **作者**: Wei Jin, Yang Ni, Amanda B Spence, Leah H Rubin, Yanxun Xu
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 1034-1048
- 相关性 2/10 · novelty: `application`
- **摘要**: 在 HIV 组合抗逆转录病毒疗法 (ART) 的纵向流行病学设定下，目标是估计药物组合与基因多态性对抑郁症状的交互效应，假设治疗历史可通过非参数核函数捕捉。提出一种贝叶斯方法，利用带复合核函数的高斯过程 (GP) 直接编码个体的纵向治疗历史，并结合贝叶斯加性回归树 (BART) 刻画个体异质性。该方法侧重于预测建模与交互效应探索，未涉及时变混杂的因果识别策略（如 g-formula 或 MSM）。仿真与 WIHS (Women's Interagency HIV Study) 真实数据应用展示了其在辅助个性化治疗决策上的临床效用。对您而言，该文提供了 HIV 纵向队列 (WIHS) 的真实数据结构参考，但在因果推断或半参数效率理论层面方法学借鉴有限。
- **关键技术**: `Gaussian process with composite kernel`, `Bayesian additive regression trees (BART)`, `longitudinal treatment history`, `pharmacogenetics interaction`
- **为什么对您有用**: 提供了流行病学纵向 HIV 队列 (WIHS) 的真实数据结构，但核心方法为贝叶斯非参数回归，与您关注的纵向因果推断（时变混杂调整）及半参数效率理论关联较弱。

## 其他  *(other, 3 篇)*

### 1. [10.1093/biostatistics/kxad031](https://doi.org/10.1093/biostatistics/kxad031) — Evaluating dynamic and predictive discrimination for recurrent event models: use of a time-dependent C-index
- **作者**: Jian Wang, Xinyang Jiang, Jing Ning
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 1140-1155
- 相关性 2/10 · novelty: `minor`
- **摘要**: 本文在复发事件数据（recurrent event）的风险预测模型设定下，目标是提出一种时间依赖的 C-index（concordance index）来局部评估模型在不同时间点的判别能力，而非仅给出全局判别指标。方法上，作者将 C-index 参数化为时间的函数，采用灵活参数模型（flexible parametric model）建模该函数，并构建基于 concordance 的似然进行估计与推断；方差估计采用 perturbation-resampling 过程。模拟研究考察了有限样本表现，并在结直肠癌患者再住院的真实数据上对三种回归模型的判别能力进行了比较。该方法学 novelty 有限（将已有 C-index 推广到时间依赖版本并套用 perturbation-resampling），对您主要关注的理论方向（因果推断、效率界、高维/半参数理论）直接关联较弱，但若您关注纵向/复发事件的预测评估问题，可作应用参考。
- **关键技术**: `time-dependent C-index`, `recurrent event model`, `concordance-based likelihood`, `perturbation-resampling`, `flexible parametric model`
- **为什么对您有用**: 复发事件设定与您 longitudinal causal inference 的兴趣有场景关联，但本文聚焦预测判别而非因果估计，理论深度较浅，主要收益在于了解复发事件数据的模型评估实践。

### 2. [10.1093/biostatistics/kxae017](https://doi.org/10.1093/biostatistics/kxae017) — <i>DifferentialRegulation</i> : a Bayesian hierarchical approach to identify differentially regulated genes
- **作者**: Simone Tiberi, Joël Meili, Peiying Cai, Charlotte Soneson, Dongze He, Hirak Sarkar et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 1079-1093
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在bulk与单细胞RNA-seq数据中，目标是识别不同实验条件下未剪接mRNA相对丰度的差异，核心挑战是多映射读段导致的高量化不确定性。提出DifferentialRegulation方法，采用贝叶斯层次模型，通过潜变量将读段分配至其基因/转录本来源及剪接版本，显式建模量化不确定性。该方法在基准测试中展现出良好的灵敏度与错误率控制，并作为Bioconductor R包实现。对您而言，该文展示了用潜变量建模处理观测不确定性的贝叶斯计算策略，但与您核心的半参数效率或因果推断理论关联较弱。
- **关键技术**: `Bayesian hierarchical model`, `latent variable approach`, `multi-mapping reads allocation`, `MCMC inference`, `RNA-seq quantification uncertainty`
- **为什么对您有用**: 该文属于计算生物学领域，使用贝叶斯潜变量处理测量不确定性，与您关注的半参数效率/因果推断理论距离较远，仅可作为处理观测不确定性（类似测量误差）的贝叶斯计算思路参考。

### 3. [10.1093/biostatistics/kxae008](https://doi.org/10.1093/biostatistics/kxae008) — Bayesian mixed model inference for genetic association under related samples with brain network phenotype
- **作者**: Xinyuan Tian, Yiting Wang, Selena Wang, Yi Zhao, Yize Zhao
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 1195-1209
- 相关性 0/10
- **摘要**: {
  "topic": "other",
  "summary_zh": "在影像遗传学设定下，目标是估计遗传变异对脑连接网络表型的效应，面临样本相关性（家系/未知亲缘）与网络拓扑结构双重挑战。作者提出 Bayesian network-response mixed-effect model，将群体结构（pedigree 与未知 relatedness）纳入随机效应，对遗传效应分量以"效应网络配置"建模，并施加 inter-network sparsity 与 intra-network shrinkage 先验以分离受风险变异影响的表型子网络。MCMC 算法用于后验推断与不确定性量化，模拟显示参数恢复良好；应用于 Human Connectome Project 数据得到可解释结果。该方法本质上是 network-variate outcome 的线性混合效应回归框架，对您在统计计算（MCMC 采样设计）与流行病学遗传关联数据集方面有一定参考价值，但与您核心的 semiparametric efficiency / causal inference 兴趣距离较远。",
  "key_techniques": [
    "Bayesian linear mixed-effect model",
    "network-variate response regression",


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

