# Biometrics — Vol 82  Issue 2  ·  2026-05-21

- 共 16 篇 · Biometrics

## 因果推断  *(causal_inference, 5 篇)*

### 1. [10.1093/biomtc/ujag057](https://doi.org/10.1093/biomtc/ujag057) — Measurement error-robust causal inference via constructed instrumental variables
- **作者**: Caleb H Miles, Linda Valeri, Brent Coull
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文研究混淆变量和暴露变量存在测量误差时的因果推断问题，目标参数为平均处理效应（ATE）和自然中介效应（NIE），关键假设是结果回归模型对误差变量呈线性。作者提出无需外部数据或测量误差分布先验知识的构造工具变量（constructed IV）法，利用仅含观测数据的函数构造 IV，在特定条件下恢复因果效应的一致估计。该方法避免了传统测量误差校正对外部验证数据的依赖，通过构造 IV 满足相关性和排他性约束。理论上证明了估计量在测量误差下的渐近一致性，并在孟加拉国产前队列数据中估计了铅暴露对出生身长的效应及蛋白质摄入的中介效应。对您有用：该文将 IV 方法创新性地用于解决测量误差下的因果识别与中介分析，直接契合您对因果推断（IV、中介）及流行病学应用的研究兴趣，提供了一种无需外部辅助数据的识别策略。
- **关键技术**: `constructed instrumental variables`, `measurement error correction`, `natural indirect effect`, `causal identification under error`, `linear outcome regression`
- **为什么对您有用**: 直接契合您对因果推断（IV、中介分析）及流行病学应用的研究兴趣；提供了一种无需外部辅助数据即可在测量误差下实现因果识别的新 IV 策略，对处理流行病学队列数据中的测量偏倚具有可迁移性。

### 2. [10.1093/biomtc/ujag056](https://doi.org/10.1093/biomtc/ujag056) — Personalized treatment design in the context of functional confounding
- **作者**: Zhixian Yang, Peijun Sang, Yixin Han, Bei Jiang, Linglong Kong, Xingcai Zhou
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在观察性研究中，当存在函数型混杂时，目标是利用临床与函数型协变量识别最优个体化治疗规则（ITR）。本文提出将 outcome-weighted learning (OWL) 与再生核希尔伯特空间（RKHS）结合，以估计包含函数型数据的最优治疗决策。针对传统支持向量机在 OWL 框架下的 data piling 问题，引入 distance-weighted discrimination (DWD) 分类器进行替代。理论上证明了决策泛函估计量的一致性并导出其风险界。模拟与 ADNI 阿尔茨海默病数据集分析显示该方法优于传统 OWL。对您有用：该工作将 RKHS 非参数理论引入因果 ITR 估计以处理函数型混杂，且其流行病学数据集（ADNI）分析对您在因果推断与流行病学交叉领域的应用有参考价值。
- **关键技术**: `outcome-weighted learning (OWL)`, `reproducing kernel Hilbert space (RKHS)`, `distance-weighted discrimination (DWD)`, `individualized treatment rule (ITR)`, `functional confounding`
- **为什么对您有用**: 将 RKHS 非参数理论引入因果推断的 ITR 估计以处理函数型混杂，且 ADNI 数据集分析对您在流行病学应用因果方法有参考价值。

### 3. [10.1093/biomtc/ujag063](https://doi.org/10.1093/biomtc/ujag063) — Bayesian adaptive randomization in the I-SPY2 sequential multiple assignment randomized trial
- **作者**: Peter Norwood, Christina Yau, Denise Wolf, Philip Beineke, Andrew Chapple, Anastasios Tsiatis et al.
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究I-SPY2乳腺癌平台试验转为序贯多重分配随机试验（SMART）设定下，旨在识别最优动态治疗策略（DTR）的响应自适应随机化（RAR）方案。核心提出一种贝叶斯RAR方法，依据治疗属于最优DTR的后验概率动态更新各阶段随机化分配概率，以最大化病理完全缓解（pCR）为目标。实证与模拟显示，相比均匀随机化，该方案在试验内提升了pCR率，且识别最优DTR的速率相当或更优。对您有用之处在于提供了SMART/DTR（纵向因果推断）在复杂平台试验中的实际落地案例，但方法学偏向贝叶斯实验设计而非半参数理论。
- **关键技术**: `Sequential Multiple Assignment Randomized Trial (SMART)`, `Dynamic Treatment Regime (DTR)`, `Response-Adaptive Randomization (RAR)`, `Bayesian posterior probability`, `platform trial design`
- **为什么对您有用**: 涉及纵向因果推断中的SMART和DTR（动态治疗策略），属于您primary interest中causal inference (longitudinal)的应用延伸；但方法核心为贝叶斯自适应设计，对半参数效率或高维理论的新意有限。

### 4. [10.1093/biomtc/ujag076](https://doi.org/10.1093/biomtc/ujag076) — Efficient collaborative learning of the average treatment effect
- **作者**: Sijia Li, Rui Duan
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多站点协作因果推断设定下（数据共享受限），目标是利用目标站点个体数据与源站点汇总统计量，估计目标人群的平均因果效应（ATE）。提出ECO-ATE方法，采用联邦框架且无需站点间迭代通信，降低了多站点协作的计算与基础设施门槛。该方法允许结果、处理和协变量的分布跨站点偏移，通过基于有效影响函数的构造，在适当正则条件下达到半参数有效界。模拟表明整合多源数据可显著提升效率，且对分布偏移和过度参数化具有鲁棒性；实证分析基于All of Us电子病历数据评估胰岛素对心衰的影响。对您有用：该工作将半参数效率理论拓展至联邦因果推断场景，其无迭代通信的估计器构造思路可直接迁移至您关注的多源/纵向因果推断及统计计算问题中。
- **关键技术**: `semiparametric efficiency bound`, `efficient influence function`, `federated learning`, `data integration`, `distributional shift`, `one-step estimation`
- **为什么对您有用**: 直接关联您 primary interest 中的因果推断与半参数效率理论，其无迭代通信的联邦估计器构造思路对多站点/纵向因果推断的统计计算有借鉴价值，同时提供了流行病学电子病历数据的应用范例。

### 5. [10.1093/biomtc/ujag054](https://doi.org/10.1093/biomtc/ujag054) — Bayesian shrinkage priors for penalized synthetic control estimators in the presence of spillovers
- **作者**: Esteban Fernández-Morales, Arman Oganisian, Youjin Lee
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在合成控制（SC）框架下，当控制单元因空间邻近而受到干预溢出效应污染时，传统 SC 估计量会产生偏差；本文目标是在存在 spillover 的设定下识别并估计干预的因果效应。作者提出贝叶斯 SC 框架，将 horseshoe 和 spike-and-slab 等收缩先验扩展为基于效用函数的收缩先验，该效用函数同时融合协变量相似性与空间距离，以此驱动数据驱动的控制单元选择——空间越近则溢出风险越高、权重越被收缩。方法不直接排除邻近单元，而是通过收缩其重要性来平衡偏差与方差。模拟显示在不同溢出水平下均能降低均方误差；实证应用于费城 2017 年含糖饮料税对销量的影响评估。对您而言，该文在因果推断的干扰/溢出设定下提供了一个识别策略思路，虽理论工具为贝叶斯收缩而非半参数效率，但溢出偏差的建模思路可迁移至您关注的因果识别与敏感性分析方向。
- **关键技术**: `synthetic control method`, `Bayesian shrinkage priors (horseshoe, spike-and-slab)`, `utility-based penalization`, `spillover/interference adjustment`, `spatial distance weighting`
- **为什么对您有用**: 直接涉及因果推断中干扰/溢出效应下的识别与估计问题（您 primary interest 的 causal inference 子方向），但方法路线为贝叶斯收缩而非半参数效率理论，理论深度与您关注的 efficiency bound / debiased ML 方向有距离；实证部分（饮料税政策评估）对经济理论应用有参考价值。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1093/biomtc/ujag077](https://doi.org/10.1093/biomtc/ujag077) — A mixed effect similarity matrix regression model (SMRmix) for integrating multiple microbiome datasets at the community level
- **作者**: Mengyu He, Ni Zhao
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多微生物组数据整合设定下，目标是识别与结局相关的群落水平微生物组转移，同时处理研究间异质性。提出混合效应相似性矩阵回归模型 (SMRmix)，将单研究下的微生物组核关联检验 (MiRKAT) 扩展至多研究整合。核心机制是在相似性矩阵（核矩阵）回归框架中引入随机效应以刻画异质性，并基于此构建关联性假设检验。模拟表明 SMRmix 控制了第一类错误且功效优于竞争方法；在 HIV 与结直肠癌多队列数据中展示了群落水平的一致性发现。该文将核方法与混合效应结合用于假设检验，对您在非参数假设检验及流行病学多队列数据整合方面的兴趣有参考价值。
- **关键技术**: `similarity matrix regression`, `kernel association test`, `mixed effect model`, `study heterogeneity`, `microbiome community-level testing`
- **为什么对您有用**: 将非参数核回归与混合效应结合用于假设检验，对您在非参数假设检验及流行病学多队列数据整合方面的兴趣有参考价值。

## 效率理论 / Debiased ML  *(efficiency_dml, 2 篇)*

### 1. [10.1093/biomtc/ujag062](https://doi.org/10.1093/biomtc/ujag062) — Borrowing information from an unidentifiable model: Guaranteed efficiency gain with a dichotomized outcome in the external data
- **作者**: Lu Wang, Yanyuan Ma, Jiwei Zhao
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在多源数据整合设定下，主数据含连续结局 Y，外部数据仅含其二值化版本 D=I(Y>c)，目标是在外部模型本身不可识别（unidentifiable）的条件下仍借信息提升回归参数的估计效率。提出两个估计器：第一个在误差分布误设定下仍保持渐近一致（misspecification-robust）；第二个保证比仅用主数据的加权最小二乘（WLS）有严格效率提升。理论证明基于 influence function 分解与信息正交投影，效率增益的保证不依赖外部模型的正确识别。模拟与 NHANES 实证验证了鲁棒性与效率提升。对您有用：该工作将 semiparametric efficiency bound 的思路拓展到'外部模型不可识别但仍可借信息'的场景，与您关注的 efficiency theory 及流行病学数据整合（NHANES）直接相关。
- **关键技术**: `semiparametric efficiency bound`, `guaranteed efficiency gain`, `misspecification-robust estimation`, `influence function decomposition`, `data integration with heterogeneous outcomes`, `weighted least squares`
- **为什么对您有用**: 直接推进 semiparametric efficiency theory——在不可识别外部模型下仍保证效率增益，这是对您 primary interest 中 efficiency bounds / debiased ML 的新理论补充；NHANES 实证也对接您 epidemiology secondary interest。

### 2. [10.1093/biomtc/ujag074](https://doi.org/10.1093/biomtc/ujag074) — Efficient interaction analysis in randomized controlled trials
- **作者**: Likun Zhang, Wei Ma
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在 RCT 的 covariate-adaptive randomization（包括简单随机化、分层随机化、minimization）设定下，本文定义了一个 model-free 的 treatment-covariate interaction 参数，避免对数据生成机制函数形式的假设。作者指出传统交互分析方法在该随机化机制下方差估计不一致，导致渐近保守或反保守推断，并给出了修正的一致方差估计量。进一步，利用处理分配由协变量自适应机制诱导的依赖结构，推导了该交互效应参数的半参数有效界，并提出了达到该界的半参数有效估计方法。该方法通过非参数/机器学习技术调整基线协变量，实现了 cross-fitting 框架下的 n^{-1/2}-CAN 且半参数有效推断。对您有用：该文将半参数有效界计算与 covariate-adaptive randomization 的依赖结构结合，直接推进了您在 efficiency theory 和 causal inference 交叉方向的理解，且其 model-free interaction 参数的思路可迁移至异质性处理效应的敏感性分析。
- **关键技术**: `semiparametric efficiency bound`, `covariate-adaptive randomization`, `efficient influence function`, `nonparametric covariate adjustment`, `model-free interaction parameter`, `cross-fitting`
- **为什么对您有用**: 直接推进您 primary interest 中 efficiency theory（半参数有效界计算）与 causal inference（处理效应异质性）的交叉方向；covariate-adaptive randomization 下的有效界推导是较新的理论场景，方法可迁移至纵向/中介分析中的交互效应推断。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1093/biomtc/ujag061](https://doi.org/10.1093/biomtc/ujag061) — A novel exact confidence interval for the difference of proportions in paired data using a restricted most probable statistic
- **作者**: Xingyun Cao, Weizhen Wang, Tianfa Xie
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在配对数据设定下，目标是构建两个比例之差的精确置信区间，以克服基于渐近正态性的近似方法在小样本下不可靠的问题。本文提出基于 restricted most probable (RMP) 统计量的精确区间，并进一步利用 h-function 方法进行优化，以保证推断的可靠性与精度。以 infimum coverage probability 和总区间长度为评价指标，与 score、Tang、Wald 等现有精确区间进行系统比较。理论与数值结果表明，所提方法在覆盖率和区间长度上均表现一致优越，并附有 R 代码实现。对您有用：该文属于有限样本精确推断，直接契合您在 mathematical statistics (hypothesis testing) 和 statistical computing 方向的兴趣，其 RMP 统计量构造与 h-function 优化思路可迁移至其他离散参数的精确检验问题。
- **关键技术**: `exact confidence interval`, `restricted most probable method`, `h-function optimization`, `infimum coverage probability`, `paired proportions`
- **为什么对您有用**: 直接契合您在 mathematical statistics (hypothesis testing) 和 statistical computing 方向的兴趣；其针对离散参数的 RMP 统计量构造与 h-function 优化算法可为有限样本精确推断提供思路借鉴。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1093/biomtc/ujag071](https://doi.org/10.1093/biomtc/ujag071) — Scalable Gaussian process regression via median posterior inference for estimating the health effects of an environmental mixture
- **作者**: Aaron Sonabend-W, Jiangshan Zhang, Edgar Castro, Joel Schwartz, Brent A Coull, Junwei Lu
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在贝叶斯半参数高斯过程回归框架下，目标是估计环境混合物（多污染物）对健康的暴露-响应函数，解决高维暴露变量间的复杂相关性与非线性关系。核心方法为 divide-and-conquer 策略：将数据分块后在各子集上并行计算 GP 后验分布，再通过 generalized median（median posterior）聚合子后验，避免全样本 MCMC 的计算瓶颈。该方法保留了 GP 回归的特征选择能力与半参数灵活性，同时将计算复杂度从 O(n³) 降至可并行水平。理论部分论证了 median posterior 在适当条件下的收敛性，但未给出 semiparametric efficiency bound 或 influence function 层面的结果。实证部分应用于马萨诸塞州 65 万新生儿体重与空气污染物混合物数据，发现交通污染标记物（元素碳、有机碳、PM₂.₅）与出生体重负相关。对您而言，该文的 divide-and-conquer + median posterior 聚合策略可作为大规模贝叶斯模型分布式计算的工具参考，但 semiparametric 理论深度有限。
- **关键技术**: `divide-and-conquer posterior`, `generalized median posterior`, `Gaussian process regression`, `Bayesian feature selection`, `distributed MCMC`, `exposure-response surface`
- **为什么对您有用**: 直接关联您 primary interest 中的 statistical computing（分布式贝叶斯计算算法），同时涉及 epidemiology 二级兴趣的真实数据集（65 万出生体重+空气污染）；但 semiparametric 效率理论层面贡献有限，收益主要在计算策略可迁移性。

## 流行病学  *(epidemiology, 2 篇)*

### 1. [10.1093/biomtc/ujag058](https://doi.org/10.1093/biomtc/ujag058) — Two-phase designs for cost-effective evaluation of cancer screening tests
- **作者**: Fangya Mao, Richard J Cook, Thomas Lorey, Nicolas Wentzensen, Li C Cheung
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在癌症筛查试验评价的 two-phase design 框架下，目标是高效估计 positive/negative predictive value（PPV/NPV），关键假设是 phase-1 筛查结果可用于分层 subsampling。本文提出一种新的 two-phase design，同时处理基线已有病例（prevalent cases）和随访新发病例（incident cases），通过优化 subsampling scheme 提升对筛查试验 risk-stratification utility 的估计效率。方法核心是在 phase-1 筛查结果分层下选择 phase-2 样本，构造 PPV/NPV 估计量；模拟显示相比简单随机抽样与传统 stratified 方案有显著效率提升。实证使用 Kaiser Permanente Northern California 的 HPV 阳性女性宫颈癌细胞学数据，评估 p16/ki-67 dual-stain test 的临床性能。对您而言，该文提供了流行病学筛查场景下 two-phase design 的完整分析流程与真实数据集，可关注其分层 subsampling 的效率优化思路是否可迁移至 semiparametric efficiency / influence function 框架下的最优设计问题。
- **关键技术**: `two-phase stratified sampling`, `predictive value estimation`, `optimal subsampling design`, `risk stratification`, `weighted estimation`
- **为什么对您有用**: 属于流行病学二级兴趣的真实数据应用（Kaiser Permanente 宫颈癌筛查队列），two-phase design 的效率优化与您 primary interest 中的 semiparametric efficiency theory 有概念连接，可借鉴其分层 subsampling 思路。

### 2. [10.1093/biomtc/ujag073](https://doi.org/10.1093/biomtc/ujag073) — Regression methods for cost-effectiveness analysis with different censoring times or terminating events for survival time and costs
- **作者**: Dingning Liu, Shuai Chen
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在成本-效果分析（CEA）中，当成本与效果分别面临不同删失时间或终止事件时，累积结局的诱导信息性删失使标准生存分析方法不可直接适用，而已有处理不同终止事件的 CEA 方法均不支持协变量调整。本文提出基于回归的 CEA 方法，目标参数为增量成本-效果比（ICER）与增量净效益（INB），通过在回归框架中纳入协变量实现协变量调整与亚组识别，从而提升效率并应对不完全随机化。模拟研究表明有限样本表现良好，两个心血管临床试验（MADIT-CRT / MADIT-II）的应用展示了方法在复杂删失机制下的实用性。对您而言，该文提供了心血管流行病学真实试验数据集，且协变量调整应对 imperfect randomization 的思路与因果推断中 treatment effect estimation 的协变量调整策略相通。
- **关键技术**: `incremental cost-effectiveness ratio`, `incremental net benefit`, `induced informative censoring`, `covariate adjustment under imperfect randomization`, `subgroup identification`, `regression-based CEA`
- **为什么对您有用**: 连接流行病学 secondary interest（MADIT-CRT / MADIT-II 心血管试验真实数据集）与因果推断 primary interest（imperfect randomization 下的协变量调整估计 treatment effect），数据集与分析流程可迁移至类似纵向因果分析场景。

## 其他  *(other, 4 篇)*

### 1. [10.1093/biomtc/ujag070](https://doi.org/10.1093/biomtc/ujag070) — Knowledge-guided Bayesian biclustering model for omics data with noisy graphs
- **作者**: Qiyiwen Zhang, Wenrui Li, Suprateek Kundu, Qi Long
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在高维异质组学数据的疾病亚型识别问题中，本文提出一种贝叶斯去噪知识引导的双聚类方法，设定观测生物图谱（如基因调控网络）为真实图谱的含噪变体。核心机制在于显式建模图谱中的误报（FP）和漏报（FN）边误差以实现图谱去噪，并将其整合入双聚类模型中。推断方面，开发了MCMC算法进行后验估计与双聚类提取。模拟研究与阿尔茨海默病基因表达及蛋白质组学真实数据验证了该方法在去噪与聚类上的优越性。对您而言，本文虽涉及高维数据，但方法论核心为贝叶斯图模型与MCMC计算，与您关注的高维RMT、半参数效率界及因果推断等理论工具距离较远，仅MCMC算法设计对统计计算兴趣有微弱参考价值。
- **关键技术**: `Bayesian biclustering`, `graph denoising`, `false positive/negative edge modeling`, `Markov chain Monte Carlo (MCMC)`, `omics data integration`
- **为什么对您有用**: 本文虽处理高维组学数据，但方法核心为贝叶斯图模型与MCMC，与您关注的高维RMT、半参数效率界及因果推断等理论重叠极少，仅MCMC算法设计对统计计算兴趣有微弱参考。

### 2. [10.1093/biomtc/ujag055](https://doi.org/10.1093/biomtc/ujag055) — A zero-inflated hierarchical generalized transformation model to address non-normality in spatially-informed cell-type deconvolution
- **作者**: Hunter J Melton, Jonathan R Bradley, Chong Wu
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在空间转录组学的细胞类型反卷积设定下，针对口腔鳞状细胞癌（OSCC）数据中严重的零膨胀现象与现有CARD方法正态假设的冲突，本文提出了零膨胀层次广义变换模型（ZI-HGT）。ZI-HGT作为辅助贝叶斯技术，通过广义变换将零膨胀数据映射至符合CARD正态假设的空间，结合条件自回归（CAR）先验进行空间信息整合。该ZI-HGT+CARD联合框架提升了细胞比例的反卷积精度，并提供了不确定性的贝叶斯量化。模拟与OSCC真实数据分析验证了其反卷积优越性，成功定位了肿瘤微环境中的成纤维细胞亚群。对您而言，若关注空间流行病学数据的零膨胀建模或贝叶斯计算，其变换策略可作参考，但与您核心的因果推断或效率理论距离较远。
- **关键技术**: `zero-inflated model`, `hierarchical generalized transformation`, `Conditional AutoRegressive (CAR) prior`, `Bayesian spatial deconvolution`, `cell-type deconvolution`
- **为什么对您有用**: 该文属于空间统计与生物统计交叉，虽然与您核心的因果推断或高维效率理论关联较弱，但其处理零膨胀的变换模型思路对空间流行病学数据建模有一定参考价值。

### 3. [10.1093/biomtc/ujag072](https://doi.org/10.1093/biomtc/ujag072) — Borrowing strength across exposures and outcomes via index models for multi-pollutant mixtures
- **作者**: Glen McGee, Joseph Antonelli
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 0/10
- **摘要**: ```json
{
  "topic": "nonparam_semipara",
  "summary_zh": "在多污染物混合暴露的环境流行病学设定下，目标是估计多个暴露与多个健康结局之间的非线性暴露-反应关系，核心假设是不同结局间共享相似的混合权重与暴露-反应曲线结构。提出多变量指数模型（multivariate index model）策略，通过跨结局、跨暴露"借力"提升检验功效，尤其在暴露高相关、效应微弱的典型场景下改善估计精度。在分布滞后模型特例中，联合鼓励滞后轮廓（lag profiles）与暴露-反应曲线的共聚类（co-clustering），以更高效识别关键易感窗口；进一步扩展至指数结构未知的多元指数模型，并引入变量重要性度量量化各组分贡献。方法基于贝叶斯框架，结合核机回归的灵活性与共享结构约束的效率增益。实证分析使用 NMMAPS 时间序列数据（3 种死亡结局 × 2 种空气污染指标，最大滞后 14 天）。对您而言，跨结局共享结构以提升效率的思路与 semiparametric efficiency 理论相通，同时该文提供了流行病学真实数据集与分析流程的参考价值。",
  "key_techniques": [
    "multiple index model",
    "Bayesian kernel machine regression",
    "

### 4. [10.1093/biomtc/ujag082](https://doi.org/10.1093/biomtc/ujag082) — Causal inference targeting a concentration index for studies of health inequalities
- **作者**: Mohammad Ghasempour, Xavier de Luna, Per E Gustafsson
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 0/10
- **摘要**: {
  "topic": "causal_inference",
  "summary_zh": "本文在因果推断框架下，定义了不同暴露水平下的反事实集中指数（counterfactual concentration index），以量化收入相关的健康不平等，目标估计量是健康变量与相对收入秩的标准化协方差。作者给出了该复杂估计量的识别条件，并推导了其有效影响函数（efficient influence function）。基于EIF，提出了正则渐近线性（RAL）估计量，证明了其 $\sqrt{n}$-相合性、渐近正态性及局部有效性。该估计量具有速率稳健性（rate robustness），允许部分干扰函数的收敛速率慢于 $\sqrt{n}$，这与 debiased ML 的正交性思想一致。模拟验证了有限样本表现，并在瑞典队列数据上考察了教育对收入相关健康不平等的因果效应。对您有用：该文将半参数效率理论（EIF推导与速率稳健性）应用于非标准因果估计量，对您在因果推断与效率理论交叉方向的研究具有直接的方法论借鉴意义。",
  "key_techniques": [
    "efficient influence function",
    "regular asymptotic linear estimator",
    "rate robustness",
    "count


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

