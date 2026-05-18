# Biometrics — Vol 82  Issue 2  ·  2026-05-18

- 共 14 篇 · Biometrics

## 因果推断  *(causal_inference, 5 篇)*

### 1. [10.1093/biomtc/ujag057](https://doi.org/10.1093/biomtc/ujag057) — Measurement error-robust causal inference via constructed instrumental variables
- **作者**: Caleb H Miles, Linda Valeri, Brent Coull
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在混杂变量和/或暴露存在测量误差的设定下，本文研究平均处理效应（ATE）和自然间接效应（NIE）的因果识别与估计问题，无需外部数据或测量误差分布的先验知识。核心方法是构造工具变量，即仅利用观测数据的函数作为误差变量的 IV。在结果回归模型关于误差变量为线性的假设下，证明这些构造的 IV 满足相关性和排他性约束，从而恢复因果效应的一致估计。理论上给出了估计的一致性，并在孟加拉国母婴队列数据中进行了实证分析，估计了铅暴露对出生身长的直接/间接效应。该文将 IV 方法创新性地应用于测量误差下的因果中介分析，直接契合您对因果推断（IV、中介）及流行病学应用的研究兴趣，且放松了传统测量误差校正需外部数据的假设。
- **关键技术**: `constructed instrumental variables`, `measurement error correction`, `causal mediation analysis`, `natural indirect effect`, `outcome regression linearity`
- **为什么对您有用**: 直接契合您对因果推断中 IV 和中介分析的兴趣，且放松了传统测量误差校正需外部数据的假设；同时提供了流行病学队列数据的因果应用案例。

### 2. [10.1093/biomtc/ujag076](https://doi.org/10.1093/biomtc/ujag076) — Efficient collaborative learning of the average treatment effect
- **作者**: Sijia Li, Rui Duan
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在多站点协作因果推断设定下，针对数据共享受限问题，目标是估计目标人群的平均因果效应（ATE），允许结局、处理和协变量的分布跨站点偏移。提出 ECO-ATE 估计器，采用联邦框架，仅需目标站点的个体数据与源站点的汇总统计量，无需站点间迭代通信。通过构建基于 efficient influence function 的 one-step 估计器，在适当正则条件下达到半参数效率界。模拟表明整合多源数据可显著提升效率，且对分布偏移与过度参数化具有鲁棒性。实证基于 All of Us 电子病历评估胰岛素对 II 型糖尿病患者心衰的影响。该工作将半参数效率界理论拓展至联邦因果推断场景，为您在多站点数据整合下的 efficient estimation 提供了计算友好的非迭代方案。
- **关键技术**: `semiparametric efficiency bound`, `efficient influence function`, `federated learning`, `distributional shift`, `one-step estimation`
- **为什么对您有用**: 直接结合了您 primary interest 中的因果推断与半参数效率界理论，并在统计计算（联邦/非迭代）层面提供了实用方案，同时涉及流行病学电子病历数据应用。

### 3. [10.1093/biomtc/ujag056](https://doi.org/10.1093/biomtc/ujag056) — Personalized treatment design in the context of functional confounding
- **作者**: Zhixian Yang, Peijun Sang, Yixin Han, Bei Jiang, Linglong Kong, Xingcai Zhou
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在观察性研究存在功能性混淆的设定下，本文研究个性化治疗规则（ITR）的估计问题，目标是寻找基于临床预测变量的最优决策函数。方法上，作者将结果加权学习（OWL）与再生核希尔伯特空间（RKHS）结合以处理功能性数据，并引入距离加权判别（DWD）分类器替代传统SVM以解决数据堆积问题。理论上，文章建立了决策泛函估计量的一致性并推导了其风险界。仿真与阿尔茨海默病神经影像学计划（ADNI）数据集的分析验证了该方法相较于传统OWL的优越性。对您有用：该文将功能性混淆纳入因果推断ITR框架，其RKHS与DWD结合的非参数方法可为您在纵向/功能性数据的因果推断及非参数理论研究中提供方法学借鉴。
- **关键技术**: `outcome-weighted learning`, `reproducing kernel Hilbert space`, `distance-weighted discrimination`, `individualized treatment rule`, `functional confounding`, `risk bound`
- **为什么对您有用**: 涉及因果推断中的个性化治疗规则（ITR）与功能性混淆，结合了RKHS非参数方法，对您在纵向/功能性数据的因果推断及非参数理论方向有参考价值。

### 4. [10.1093/biomtc/ujag063](https://doi.org/10.1093/biomtc/ujag063) — Bayesian adaptive randomization in the I-SPY2 sequential multiple assignment randomized trial
- **作者**: Peter Norwood, Christina Yau, Denise Wolf, Philip Beineke, Andrew Chapple, Anastasios Tsiatis et al.
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 4/10 · novelty: `application`
- **摘要**: 在 I-SPY2 乳腺癌新辅助治疗平台试验的 SMART（序贯多重分配随机试验）设定下，目标是识别最大化病理完全缓解（pCR）的最优动态治疗策略（DTR）。核心方法是提出一种贝叶斯响应自适应随机化（RAR）方案，根据当前累积数据计算某治疗属于最优策略的后验概率，并以此动态更新后续患者的随机化分配权重。该设计支持最多三阶段的序贯治疗决策，属于纵向因果推断中 DTR 的试验设计范畴。实证结果表明，相比均匀随机化，该贝叶斯 RAR 机制能提升试验内总体 pCR 率，并以相当或更快的速度识别出最优 DTR。对您而言，本文侧重临床试验的贝叶斯自适应设计而非半参数理论，但 SMART 框架下动态策略的识别与您关注的纵向因果推断紧密相关，可作为 DTR 实际应用与设计思路的参考。
- **关键技术**: `Sequential Multiple Assignment Randomized Trial (SMART)`, `Dynamic Treatment Regimes (DTR)`, `Bayesian response-adaptive randomization`, `Posterior probability of optimal regime`, `Platform trial design`
- **为什么对您有用**: SMART 和 DTR 属于纵向因果推断的重要分支；本文虽为贝叶斯自适应设计的应用，缺乏半参数效率界等理论深度，但提供了 SMART 框架下动态策略识别的实际数据与设计思路，对您关注纵向因果推断的应用有参考价值。

### 5. [10.1093/biomtc/ujag054](https://doi.org/10.1093/biomtc/ujag054) — Bayesian shrinkage priors for penalized synthetic control estimators in the presence of spillovers
- **作者**: Esteban Fernández-Morales, Arman Oganisian, Youjin Lee
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在合成控制（SC）框架下，当空间邻近的控制单元存在干预溢出效应时，目标是估计政策干预的因果效应并控制由溢出导致的偏差。本文提出一种基于效用函数的贝叶斯收缩先验框架，扩展了传统的 horseshoe 和 spike-and-slab 惩罚方法。该效用函数融合了协变量相似性与空间距离，通过数据驱动机制降低潜在受污染控制单元的权重，从而在偏差（溢出风险）与方差（拟合优度）之间进行权衡。该方法避免了直接剔除邻近单元造成的方差膨胀，而是通过先验收缩实现软性选择。模拟研究显示其在不同溢出水平下均能有效降低估计偏差，实证应用于费城 2017 年饮料税对含糖饮料销量的影响评估。对您而言，该文为因果推断中处理溢出/干扰（interference）设定提供了贝叶斯惩罚的新思路，且实证场景契合经济政策评估。
- **关键技术**: `synthetic control`, `Bayesian shrinkage priors`, `horseshoe prior`, `spike-and-slab`, `spillover effects`, `spatial utility function`
- **为什么对您有用**: 涉及因果推断中合成控制方法在溢出效应（干扰）下的识别与估计问题，属于您 primary interest 中因果推断的干扰/溢出设定，且实证部分与经济政策评估（secondary interest）相关。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1093/biomtc/ujag074](https://doi.org/10.1093/biomtc/ujag074) — Efficient interaction analysis in randomized controlled trials
- **作者**: Likun Zhang, Wei Ma
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 在协变量自适应随机化（CAR，含简单/分层随机化与最小化法）的 RCT 设定下，本文提出无模型（model-free）的处理-协变量交互作用目标参数，避免了对数据生成机制函数形式的假设。作者指出传统交互作用分析方法在 CAR 下方差估计不一致（渐近保守或反保守），并给出了修正的一致方差估计量。通过刻画 CAR 诱导的处理分配依赖结构，本文推导了该交互作用参数的半参数有效界，并提出了新的半参数有效估计方法。该推断过程结合非参数与机器学习技术调整基线协变量，实现了渐近有效性。对您有用：本文完整展示了在复杂随机化机制下推导半参数有效界并构造有效估计量的流程，直接契合您对效率理论和因果推断的兴趣，且对实验经济学/流行病学 RCT 应用有方法迁移价值。
- **关键技术**: `covariate-adaptive randomization`, `semiparametric efficiency bound`, `model-free interaction`, `consistent variance estimator`, `machine learning adjustment`
- **为什么对您有用**: 直接展示了在复杂随机化机制下推导半参数有效界并构造有效估计量的完整流程，契合您对效率理论和因果推断的核心兴趣，且对实验经济学/流行病学 RCT 应用有方法迁移价值。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1093/biomtc/ujag077](https://doi.org/10.1093/biomtc/ujag077) — A mixed effect similarity matrix regression model (SMRmix) for integrating multiple microbiome datasets at the community level
- **作者**: Mengyu He, Ni Zhao
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 在多微生物组数据整合设定下，目标是识别与结局相关的群落水平微生物偏移，同时控制研究间异质性。提出混合效应相似性矩阵回归模型（SMRmix），将单研究的微生物核关联检验扩展至多研究混合效应框架。该方法通过相似性矩阵（核函数）刻画群落结构，并引入随机效应捕捉异质性。模拟表明 SMRmix 具有良好的第一类错误控制且功效优于现有方法；在 17 个 HIV 和 11 个结直肠癌真实数据集上验证了其一致性。对您有用之处：展示了核回归/相似性矩阵在假设检验中的扩展思路，且包含丰富的流行病学多队列数据集，可作方法迁移或实证参考。
- **关键技术**: `similarity matrix regression`, `kernel association test`, `mixed effect model`, `study heterogeneity integration`, `microbiome community-level shift`
- **为什么对您有用**: 涉及半参数核回归与假设检验的扩展框架，同时提供了HIV与结直肠癌的流行病学多队列数据集，对假设检验方法迁移或流行病学实证研究有参考价值。

### 2. [10.1093/biomtc/ujag061](https://doi.org/10.1093/biomtc/ujag061) — A novel exact confidence interval for the difference of proportions in paired data using a restricted most probable statistic
- **作者**: Xingyun Cao, Weizhen Wang, Tianfa Xie
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在配对数据设定下，研究两个比例之差的精确置信区间构造问题，旨在克服基于渐近正态性的近似方法在小样本下覆盖率不可靠的缺陷。提出基于受限最可能统计量（restricted most probable statistic）的新区间，并进一步利用 h-function 方法进行优化，得到既保证覆盖概率又提高精度的最优精确区间。通过下确界覆盖概率（infimum coverage probability）和区间总长度作为评价指标，与 score 方法、Tang 方法、Wang 方法等现有精确区间进行系统比较，证明所提区间具有一致更优的表现。文章附带 R 代码以支持实际应用。对您有用：该文属于经典的精确假设检验与区间估计，其 h-function 优化算法及 R 代码实现可为您在统计计算与假设检验方向的工具箱提供直接参考。
- **关键技术**: `exact confidence interval`, `restricted most probable method`, `h-function optimization`, `infimum coverage probability`, `paired proportions difference`
- **为什么对您有用**: 直接对应您 primary interest 中的假设检验与统计计算方向；其针对小样本精确推断的 h-function 优化算法及提供的 R 代码，对处理类似离散参数精确检验问题具有方法学和计算上的参考价值。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1093/biomtc/ujag071](https://doi.org/10.1093/biomtc/ujag071) — Scalable Gaussian process regression via median posterior inference for estimating the health effects of an environmental mixture
- **作者**: Aaron Sonabend-W, Jiangshan Zhang, Edgar Castro, Joel Schwartz, Brent A Coull, Junwei Lu
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在环境混合物暴露-反应的半参数高斯过程回归框架下，针对全样本 MCMC 在大规模数据下计算不可行的问题，本文提出一种分布式计算策略。核心方法为 divide-and-conquer：将数据分块并行计算子集后验，再通过 generalized median 组合得到 median posterior。该组合策略可推广至其他计算昂贵的贝叶斯模型，有效解决了高斯过程模型在大样本下的可扩展性瓶颈。实证部分将该方法应用于马萨诸塞州 65 万新生儿体重与空气污染物的流行病学数据，发现交通污染标记物与出生体重呈负相关。对您而言，该文提供了半参数 GP 模型的可扩展计算方案（stat computing），同时包含大型流行病学数据集的应用案例（epidemiology datasets）。
- **关键技术**: `divide-and-conquer`, `generalized median posterior`, `Gaussian process regression`, `parallel MCMC`, `Bayesian semi-parametric`
- **为什么对您有用**: 提供了半参数贝叶斯模型在大规模数据下的 divide-and-conquer 计算方案（stat computing），并包含 65 万样本的流行病学空气污染与出生体重数据集（epidemiology datasets）。

## 流行病学  *(epidemiology, 3 篇)*

### 1. [10.1093/biomtc/ujag072](https://doi.org/10.1093/biomtc/ujag072) — Borrowing strength across exposures and outcomes via index models for multi-pollutant mixtures
- **作者**: Glen McGee, Joseph Antonelli
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在环境流行病学多污染物混合暴露设定下，传统非参数模型（如 BKMR）在暴露高相关且效应微弱时检验效能低下。本文提出多指标模型（multivariate index model）策略，通过共享混合物成分权重与暴露-反应曲线，跨暴露与结局借力以提升估计效能。在分布滞后模型中，该方法联合鼓励滞后轮廓与暴露-反应曲线的共聚类，更高效地识别关键易感窗口。进一步将框架扩展至指标结构未知的多元指标模型，并引入变量重要性度量量化成分贡献。实证基于 NMMAPS 数据联合建模死亡率与空气污染。该借力策略对您在流行病学队列研究中处理高相关暴露与微弱效应的半参数建模与效率提升有直接参考价值。
- **关键技术**: `multiple index models`, `distributed lag models`, `co-clustering`, `Bayesian kernel machine regression`, `variable importance measures`
- **为什么对您有用**: 契合您在流行病学（环境健康）的应用兴趣，其跨结局借力以提升半参数模型检验效能的策略，对处理高相关暴露与微弱因果效应的流行病学应用具有方法迁移价值。

### 2. [10.1093/biomtc/ujag058](https://doi.org/10.1093/biomtc/ujag058) — Two-phase designs for cost-effective evaluation of cancer screening tests
- **作者**: Fangya Mao, Richard J Cook, Thomas Lorey, Nicolas Wentzensen, Li C Cheung
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究癌症筛查试验临床性能（PPV、NPV）的成本效益评价问题，设定为两阶段设计（two-phase design）下的缺失数据结构，目标是在仅对精心选取的子样本进行昂贵标记物测量时，高效估计风险分层指标。核心方法是将传统以标记物-结局关联为目标的二阶段设计扩展至预测值估计，提出一种新型子抽样方案，同时容纳初筛时已有病例（prevalent cases）与随访中新发病例（incident cases），并通过逆概率加权（IPW）或增强逆概率加权（AIPW）类估计量实现半参数有效推断。模拟显示所提设计相较其他子抽样策略具有显著的效率提升；实证分析基于 Kaiser Permanente Northern California 的 HPV 阳性女性宫颈癌筛查数据评估 p16/ki-67 双染试验。对您而言，两阶段设计的效率理论（影响函数、最优抽样权重）与半参数效率界直接相关，同时该文提供了流行病学筛查场景的完整数据集与方法迁移参考。
- **关键技术**: `two-phase design`, `inverse probability weighting`, `augmented IPW`, `semiparametric efficiency`, `predictive value estimation`, `optimal subsampling`
- **为什么对您有用**: 两阶段设计本质是缺失数据下的半参数效率问题，与您 primary interest 中的 semiparametric efficiency bounds 和 efficiency theory 直接相通；同时该文提供了流行病学筛查场景的完整数据集，对您 secondary interest 中的 epidemiology 应用有参考价值。

### 3. [10.1093/biomtc/ujag073](https://doi.org/10.1093/biomtc/ujag073) — Regression methods for cost-effectiveness analysis with different censoring times or terminating events for survival time and costs
- **作者**: Dingning Liu, Shuai Chen
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究成本-效果分析（CEA）中，当成本与效果指标面临不同删失时间或不同终止事件时的回归估计问题，目标参数为增量成本效果比（ICER）和增量净效益（INB）。核心挑战在于累积成本因诱导信息性删失无法直接套用标准生存分析方法，且成本与效果的删失结构可能不同。作者在回归框架中引入协变量调整，提出处理异质删失机制的估计方法，同时实现协变量调整以提高效率与亚组识别。模拟研究显示有限样本表现良好，并应用于 MADIT-CRT 和 MADIT-II 两项心血管临床试验数据。该方法对您在流行病学队列研究中处理复杂删失下的因果/效果评价有直接应用价值，但理论深度（如影响函数、半参数效率界）有限。
- **关键技术**: `cost-effectiveness analysis with informative censoring`, `incremental cost-effectiveness ratio estimation`, `covariate adjustment under heterogeneous censoring`, `subgroup identification via regression`, `survival analysis with different terminating events`
- **为什么对您有用**: 直接连接您 secondary interest 中流行病学应用与数据集（MADIT-CRT/II 心血管试验），提供复杂删失下 CEA 的可迁移方法；但缺乏半参数效率理论或高维推断的新贡献，方法学 novelty 偏应用层面。

## 其他  *(other, 2 篇)*

### 1. [10.1093/biomtc/ujag062](https://doi.org/10.1093/biomtc/ujag062) — Borrowing information from an unidentifiable model: Guaranteed efficiency gain with a dichotomized outcome in the external data
- **作者**: Lu Wang, Yanyuan Ma, Jiwei Zhao
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 8/10
- **摘要**: {
  "topic": "efficiency_dml",
  "summary_zh": "在数据整合设定下，主数据包含连续结局 Y，外部数据仅含其二值化版本 D=I(Y>c)，目标是在外部模型因二值化而不可识别的情况下仍借信息提升回归系数的估计效率。提出两个新估计量：第一个在误差分布可能误判时仍保持渐近一致；第二个基于 influence function 推导，保证比仅用主数据的加权最小二乘估计有严格的效率提升（asymptotic variance 更小）。核心技术工具包括 semiparametric efficiency bound 分析与 misspecified sub-model 下的信息借取机制，证明即使外部数据信息不完整，仍可实现有保证的效率增益。模拟验证了误判场景下的稳健性与效率提升；NHANES 数据展示了实际应用。对您有用：该工作为 semiparametric efficiency theory 提供了"从不可识别外部模型借信息仍保证效率提升"的新理论结果，对数据整合下的 efficiency bound 研究有直接参考价值。",
  "key_techniques": [
    "semiparametric efficiency bound",
    "influence function",
    "guaranteed efficien

### 2. [10.1093/biomtc/ujag055](https://doi.org/10.1093/biomtc/ujag055) — A zero-inflated hierarchical generalized transformation model to address non-normality in spatially-informed cell-type deconvolution
- **作者**: Hunter J Melton, Jonathan R Bradley, Chong Wu
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 在空间转录组学的细胞类型反卷积设定下，针对口腔鳞状细胞癌(OSCC)数据的高零膨胀特征，本文提出零膨胀层级广义转换模型(ZI-HGT)以放松条件自回归反卷积(CARD)的正态性假设。ZI-HGT 作为辅助贝叶斯技术，通过转换函数将高度零膨胀的计数数据映射至符合正态假设的隐空间，从而协调数据特征与模型假设。结合后的 ZI-HGT + CARD 框架在贝叶斯层级下量化细胞类型比例的不确定性，并在模拟与 OSCC 实证分析中展示了更高的反卷积精度。实证结果成功定位了肿瘤微环境中成纤维细胞的分布，对理解肿瘤生长与免疫抑制有重要意义。对您而言，广义转换模型放松分布假设的思路与半参数理论有一定交集，但本文核心偏向贝叶斯空间统计与生物信息学应用，方法学直接迁移价值有限。
- **关键技术**: `zero-inflated model`, `hierarchical generalized transformation model`, `Conditional AutoRegressive Deconvolution`, `spatial transcriptomics`, `Bayesian auxiliary technique`
- **为什么对您有用**: 广义转换模型（HGT）放松参数分布假设的思路与半参数理论有微弱交集，但本文核心为贝叶斯空间统计在基因组学的应用，对您主要兴趣的直接启发性较弱，仅作应用视角参考。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

