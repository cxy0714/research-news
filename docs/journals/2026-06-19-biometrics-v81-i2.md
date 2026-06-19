# Biometrics — Vol 81  Issue 2  ·  2026-06-19

- 共 38 篇 · Biometrics
- 目录核对 ⚠️ 疑似漏 2 篇（对照 OpenAlex 43 篇）：10.1093/biomtc/ujaf039、10.1093/biomtc/ujaf048

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

Biometrics Vol 81 Issue 2 的 38 篇论文围绕四条主线展开：**因果推断**（约 13 篇）集中在双稳健估计的方差与灵敏度、连续暴露的 lean 建模、中介分析、动态治疗方案、测量误差与空间混杂；**半参数 / 非参数方法**（约 6 篇）涉及充分降维、生存风险比非参数估计、联合建模和保序预测区间；**假设检验**（约 5 篇）关注适应性随机化试验（协变量自适应、响应自适应、平台试验对照切换）、高维组成分均值检验和局部错误发现率；**流行病学应用与方法**（约 8 篇）覆盖两阶段设计、半竞争风险、诊断荟萃分析、阶梯楔形设计样本量等，其余零散论文涉及高维筛选、半监督 Ising 模型、贝叶斯联合疗法设计等。

因果推断主线中，“双稳健”是一再出现的关键词：方差估计、敏感性分析、动态治疗规则、测量误差校正均在双稳健框架下推进。Double robust variance estimation 提出经验 Sandwich 和 bootstrap 在模型之一正确时仍保持方差一致性；Doubly robust omnibus sensitivity analysis 同时量化结局均值不可交换性与中间事件影响，给出半参数最优估计量。连续暴露效应有两篇形成互补：Towards efficient and interpretable assumption-lean GLM 通过去偏程序改善有限样本稳定性，Estimating weighted quantile treatment effects with missing outcome data by double sampling 处理 MNAR 缺失。中介分析（Continuous-time mediation analysis）和动态治疗方案（Optimal dynamic treatment regime estimation in the presence of nonadherence）分别延展至连续时间与依从性缺失场景。空间混杂（Regularized principal spline functions to mitigate spatial confounding）则与 exposure-measurement error 一脉相承，共同处理未观测混杂。

假设检验轴线中，几篇论文围绕临床试验设计中的推断困难：Statistical inference on the relative risk following covariate-adaptive randomization 揭示了 CAR 下传统 Wald 检验的保守性并给出修正；On the finite-sample and asymptotic error control of a randomization-probability test 为响应自适应试验提供有限样本 Type I error 控制；Design of platform trials with a change in the control treatment arm 解析了对照切换时信息保留对功效与条件 I 类错误的影响。高维检验方面，Power-enhanced two-sample mean tests 通过 P-value 组合策略提升微生物组成分数据检验功效，Inference with approximate local false discovery rates 利用邻域信息改进多重检验效率。

对于因果推断 / 半参数效率方向最贴近的论文包括：Double robust variance estimation、Towards efficient and interpretable assumption-lean GLM、Doubly robust omnibus sensitivity analysis、Optimal dynamic treatment regime estimation with nonadherence 和 Addressing confounding and continuous exposure measurement error；半监督效率方面可看 Robust and efficient semi-supervised learning for Ising model；高维方法可优先阅读 PDC-MAKES。

## 因果推断  *(causal_inference, 13 篇)*

### 1. [10.1093/biomtc/ujaf054](https://doi.org/10.1093/biomtc/ujaf054) · [arXiv](https://arxiv.org/abs/2404.16166) — Double robust variance estimation with parametric working models
- **作者**: Bonnie E Shook-Sa, Paul N Zivich, Chanhwa Lee, Keyi Xue, Rachael K Ross, Jessie K Edwards et al.
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文聚焦于因果推断中双重稳健估计量的方差估计问题。当暴露非随机时，基于影响函数的方差估计仅在结果模型和暴露模型都正确指定时才一致，这限制了其实际应用中的可靠性。作者提出经验sandwich方差估计量和非参数bootstrap在双稳健框架下具有方差双稳健性：只要其中一个工作模型正确，即可得到有效的方差估计和名义置信区间覆盖。通过仿真实验比较了影响函数法、经验sandwich和bootstrap三种方差估计量在参数工作模型下的有限样本表现。最后将该方法应用于改善妊娠结局项目中孕妇贫血对出生体重影响的因果效应估计。对您而言，本文涉及因果推断中双重稳健估计的方差稳健性这一关键实践问题，可与您非常熟悉的因果推断估计理论及非参数统计工具（如M估计、sandwich方差估计）直接对接，且经验sandwich估计器易于编程实现。
- **关键技术**: `doubly robust estimation`, `influence function`, `empirical sandwich variance estimator`, `nonparametric bootstrap`, `parametric working models`
- **为什么对您有用**: 本文属于因果推断中的估计理论子方向，具体是双重稳健估计量的方差估计在模型错误指定下的行为。研究者非常熟悉因果推断的估计理论（very_familiar），sandwich方差估计的分析工具已在武器库中，无需额外学习即可理解并评估该方法的实用性。**立即可做**：可直接将经验sandwich方差估计器应用于研究者自己的因果推断项目，或用非参数统计框架验证其渐近性质。

### 2. [10.1093/biomtc/ujaf071](https://doi.org/10.1093/biomtc/ujaf071) — Towards efficient and interpretable assumption-lean generalized linear modeling of continuous exposure effects
- **作者**: Stijn Vansteelandt
- **期刊/来源**: Biometrics
- **机构**: Ghent University
- **分类**: vol 81 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文关注连续暴露的因果效应估计，传统模型依赖方法易因模型误设而失效，基于modified treatment policies的shift干预虽提供无模型替代，但需评估多种shift幅度才能产生 actionable insights。作者引入参数化模型来描述不同幅度shift干预的效应，并采用assumption-lean估计策略，旨在模型误设下最小化平方偏差。尽管使用debiased machine learning (DML) 方法，但发现其在某些数据生成机制下表现不稳定，因此提出两大创新：一是开发一种广泛适用的去偏程序，显著改善有限样本性质；二是为具有更优效率界但模型误设时解释更微妙的estimand设计DML估计量。该方法避免逆暴露密度加权，无需针对positivity违规调整shift干预。通过Bangladesh Wash Benefits研究的模拟和再分析验证了方法的稳定性与实用性。这对您的因果推断（尤其连续暴露）、debiased ML和效率理论研究具有直接参考价值，其assumption-lean框架可迁移至proximal CI或纵向分析。
- **关键技术**: `debiased machine learning`, `assumption-lean estimation`, `modified treatment policies`, `shift interventions`, `efficient influence function`, `generalized linear models`
- **为什么对您有用**: 本文属于连续暴露因果效应与assumption-lean估计的交集，与您的primary interest（因果推断、debiased ML、效率理论）高度吻合。您武器库中的estimation theory in causal inference和semiparametric theory可直接用于评估其去偏程序的渐近性质；此外，您对higher-order U-statistics的熟悉度（树宽/张量收缩）可用于分析其estimand的高阶偏差。该工作立即可作为您拓展连续暴露因果推断（如IV或mediation）的参考方法。

### 3. [10.1093/biomtc/ujaf062](https://doi.org/10.1093/biomtc/ujaf062) · [arXiv](https://arxiv.org/abs/2403.11017) — Continuous-time mediation analysis for repeatedly measured mediators and outcomes
- **作者**: Kateline Le Bourdonnec, Linda Valeri, Cécile Proust-Lima
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对纵向研究中重复测量的中介变量和结局变量，提出了一种连续时间中介分析方法。传统方法将中介和结局离散化为固定时间点，而实际过程常定义在连续时间并以不规则的个体特异性时间点测量。作者在时间固定暴露X、随时间变化的中介过程M_t和结局过程Y_t以及时变混杂过程L_t的设定下，定义了自然效应和路径特定效应两类因果估计量。他们给出了可识别性假设，并采用基于微分方程的多元混合模型进行估计，该模型能灵活处理不规则访视时间。通过模拟实验评估了方法的性能，并在3C脑老化研究中以两个实例进行说明：教育水平通过抑郁症状和认知功能对功能依赖的影响，以及遗传因素通过血管脑损伤对认知功能的影响（以神经退行性变化为混杂）。该工作将经典中介分析从离散时间推广至真实的连续时间框架，对纵向因果推断具有重要价值。您的研究兴趣涵盖中介分析和纵向数据，文中基于微分方程的混合模型思路可与您的非参数/半参数因果推断方法形成互补，值得深入关注。
- **关键技术**: `multivariate mixed models`, `differential equations`, `path-specific effects`, `natural effects`, `continuous-time mediation`, `irregular longitudinal data`
- **为什么对您有用**: 本文直接切入您primary interest中的因果推断——纵向中介分析子方向，并针对不规则测量这一实际难题提出连续时间框架。您武器库中'非参数统计'和'因果推断的估计理论'可直接用于检验其识别假设在更弱条件下的稳健性。**中期可做**：若在'semiparametric theory'（moderately_familiar）上进一步精进，则可尝试推导该框架下半参数效率界或提出双稳健估计量。

### 4. [10.1093/biomtc/ujaf047](https://doi.org/10.1093/biomtc/ujaf047) · [arXiv](https://arxiv.org/abs/2503.06864) — Doubly robust omnibus sensitivity analysis of externally controlled trials with intercurrent events
- **作者**: Chenyin Gao, Xiang Zhang, Shu Yang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在外部对照试验（externally controlled trials）设定下，目标是估计处理效应，同时应对因缺乏随机化导致的基线不可比与结局均值不可交换性（outcome mean non-exchangeability），并处理不可避免的中间事件（intercurrent events）对效应的混杂干扰。本文建立了一个半参数框架，为主要分析和敏感性分析提供了 doubly robust 且局部最优的估计量。核心机制是提出一种 omnibus 敏感性分析，同时量化结局均值不可交换性与中间事件的影响，在指定条件下保证 root-n 一致性与渐近正态性。理论结果通过模拟与真实数据验证。对您有用：本文将 DR 与半参数局部最优性结合，直接连接到您 causal inference 中 sensitivity analysis 与 semiparametric efficiency 的核心兴趣。
- **关键技术**: `doubly robust estimation`, `semiparametric framework`, `omnibus sensitivity analysis`, `outcome mean non-exchangeability`, `intercurrent events`, `locally optimal estimator`
- **为什么对您有用**: 本文直接连接到您 causal inference 子方向中的 sensitivity analysis 与 semiparametric efficiency theory，特别是外部对照试验这一缺乏随机化的设定下如何做 robust inference。您武器库中的 semiparametric theory（moderately_familiar）与 estimation theory in causal inference（very_familiar）可以直接用来审视其声称的 locally optimal 与 DR 性质是否达到 semiparametric efficiency bound，甚至可以尝试用 HOIF 探索更高阶的改进。**立即可做**：用 very_familiar 的 causal estimation theory 检查其 influence function 构造与 DR 条件；若想推进 sharper rate 或 higher-order correction，需先在 moderately_familiar 的 HOIF 上长肌肉。

### 5. [10.1093/biomtc/ujaf041](https://doi.org/10.1093/biomtc/ujaf041) · [arXiv](https://arxiv.org/abs/2402.12555) — Optimal dynamic treatment regime estimation in the presence of nonadherence
- **作者**: Dylan Spicker, Michael P Wallace, Grace Y Yi
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究动态治疗方案（DTR）在患者非依从性（nonadherence）存在时的最优估计问题。非依从性指实际治疗与指定治疗不一致，忽略该问题将导致估计出次优的治疗规则。作者提出了一种基于双稳健（double robust）的估计方法，其估计量具有一致性和渐近正态性。具体地，通过调整非依从性对因果效应的影响，该方法可在倾向得分或结果模型之一正确时仍保持一致性。模拟实验表明，该方法性能稳健，与无依从性问题下的理想估计量表现相当。该工作将因果推断中的DTR估计推广到非依从性这一常见实际场景，对于纵向数据下的个性化治疗决策具有重要价值。
- **关键技术**: `dynamic treatment regimes`, `nonadherence adjustment`, `double robustness`, `consistent and asymptotically normal estimation`
- **为什么对您有用**: 直接对应您的核心兴趣——因果推断中的纵向DTR估计与非依从性处理。您非常熟悉的非参数统计（very_familiar）可用于估计倾向得分与结果模型中的nuisance参数，而您中等熟悉的identification theory（moderately_familiar）可用于检验本文对非依从性机制的可识别性假设。**中期可做**：先利用identification theory梳理该文未明确讨论的假设强度（如负对照或工具变量假设），再在您已有的DTR估计框架中实现其双稳健方法。

### 6. [10.1093/biomtc/ujaf045](https://doi.org/10.1093/biomtc/ujaf045) · [arXiv](https://arxiv.org/abs/2407.09443) — Addressing confounding and continuous exposure measurement error using corrected score functions
- **作者**: Brian D Richardson, Bryan S Blette, Peter B Gilbert, Michael G Hudgens
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究暴露变量存在经典加性测量误差且同时存在未观测混淆时，如何估计暴露对结局的边际因果效应。作者提出基于校正得分函数（corrected score function）的三种估计量：g-公式、逆概率加权（IPW）和双稳健（doubly-robust）估计量。双稳健估计量在倾向性评分模型或结果回归模型之一正确设定时仍保持一致，且所有估计量均为一致且渐近正态。方法依赖于经典测量误差假设和常规无混淆假设，核心工具是校正得分函数，它修正了测量误差导致的偏倚。模拟表明有限样本性能良好，并应用于 HVTN 505 疫苗试验，评估两种生物标志物对 HIV-1 感染风险的影响。该工作对您有用，因为它直接拓展了因果推断中混淆与测量误差联合处理的方法库，并提供了即用 R 包，特别适用于流行病学实际数据分析。
- **关键技术**: `corrected score functions`, `classical additive measurement error`, `doubly-robust estimation`, `g-formula`, `inverse probability weighting`, `R package mismex`
- **为什么对您有用**: 本文直接关联到您主要兴趣中的因果推断（混淆与测量误差联合处理），并提供了流行病学（HIV 疫苗试验）的实际应用案例。您的武器库中“因果推断估计”（very_familiar）和“半参数理论”（moderately_familiar）足以理解其双稳健构造和渐近理论；校正得分函数可作为一种新工具融入您已有的 IPW/g-formula 框架。评判：立即可做——您已掌握核心因果推断估计技术，可直接使用其 R 包或将其思路迁移至其他测量误差场景。

### 7. [10.1093/biomtc/ujaf068](https://doi.org/10.1093/biomtc/ujaf068) · [arXiv](https://arxiv.org/abs/2408.07560) — Variant specific treatment effects with applications in vaccine studies
- **作者**: Gellért Perényi, Mats Stensrud
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 在疫苗试验中病原体存在异质性变异株的设定下，本文目标是定义并识别变异株特异性治疗效应（variant-specific treatment effects）的因果 estimands。核心挑战在于：即使 RCT 数据中个体可视为 iid，疫苗在目标人群推广时必然存在干扰（interference），导致常规绝对尺度参数不再对应良定义因果效应。作者证明在特定干扰条件下，相对尺度上的疫苗效力参数（VE）仍可识别为良定义的因果效应，从而为报告相对效应而非绝对效应提供了新的因果推断依据。方法上依赖潜在结果框架与干扰下的 identification 条件推导，并在 HIV-1 疫苗试验数据上做了实证分析。对您有用：本文将干扰与变异株特异性效应结合的 identification 理论，直接连接到 causal inference 的 identification theory 子方向。
- **关键技术**: `variant-specific causal estimands`, `interference under population rollout`, `relative scale vaccine efficacy identification`, `potential outcomes framework`, `HIV-1 vaccine trial analysis`
- **为什么对您有用**: 本文直接推进 causal inference 中 identification theory 子方向——在干扰设定下重新定义变异株特异性 estimands，并证明相对尺度 VE 的 identification 条件，这对您在 identification theory（moderately_familiar）上的积累是很好的补充。用您 very_familiar 的 estimation theory in causal inference 可以直接构造该 estimands 的 estimator 并推导其效率界。立即可做：基于本文的 identification 结果，用 semiparametric efficiency bound 工具推导相对尺度 VE 的 efficient influence function 并构造 debiased estimator。

### 8. [10.1093/biomtc/ujaf076](https://doi.org/10.1093/biomtc/ujaf076) · [arXiv](https://arxiv.org/abs/2403.05373) — Regularized principal spline functions to mitigate spatial confounding
- **作者**: Carlo Zaccardi, Pasquale Valentini, Luigi Ippoliti, Alexandra M Schmidt
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在空间设计设定下研究未测量混杂导致的空间混杂（spatial confounding）问题，目标是恢复暴露对结局的因果效应。作者首先证明：非参数模型的混杂偏误与包含基矩阵表示未测量混杂（条件于暴露）的半参数模型的偏误之间存在一般关系，但半参数方法仅在暴露与混杂的空间结构、基展开类型及正则化机制满足特定条件时才能保证偏误缩减。为此提出贝叶斯半参数回归模型，用 principal spline basis functions 的展开矩阵逼近未观测因子，并对展开系数施加 spike-and-slab 先验以选择关键基函数。模拟显示该方法在偏误缩减与抗偏误放大（bias amplification）方面优于现有方法。对您有用：本文将空间混杂形式化为半参数基展开下的偏误分析，直接连接因果推断的 sensitivity / unmeasured confounding 与半参数理论。
- **关键技术**: `spatial confounding`, `semi-parametric basis expansion`, `principal spline basis functions`, `spike-and-slab prior`, `bias amplification`, `Bayesian semi-parametric regression`
- **为什么对您有用**: 本文直接连接因果推断的 unmeasured confounding / sensitivity 分析子方向，将空间混杂偏误形式化为半参数基展开下的条件偏误关系，属于因果推断与半参数理论的交叉。您武器库中 moderately_familiar 的 semiparametric theory 与 identification theory 可直接攻入其偏误缩减条件的理论分析口子，验证其声称的偏误缩减条件是否可进一步收紧或给出 minimax 视角。follow-up 粗判：中期可做——需先在 moderately_familiar 的 semiparametric theory 上长肌肉，具体是基展开偏误的 Frechet 导数与 influence function 分析，以将贝叶斯 spike-and-slab 选择机制转化为频率派的正则化收敛率。

### 9. [10.1093/biomtc/ujaf038](https://doi.org/10.1093/biomtc/ujaf038) — Estimating weighted quantile treatment effects with missing outcome data by double sampling
- **作者**: Shuo Sun, Sebastien Haneuse, Alexander W Levis, Catherine Lee, David E Arterburn, Heidi Fischer et al.
- **期刊/来源**: Biometrics
- **机构**: Harvard University · Carnegie Mellon University · Kaiser Permanente · Kaiser Permanente Washington Health Research Institute · University of Washington
- **分类**: vol 81 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在 EHR 等数据中结局常面临 missing-not-at-random (MNAR) 问题，本文研究如何利用 double sampling（对子样本补充采集缺失结局）来识别和估计因果加权分位数处理效应 (WQTE)。核心识别条件仅依赖 double sampling 的随机化假设，无需对原始缺失机制做 MNAR 假设；估计量为 inverse-probability weighted (IPW) estimator，允许倾向得分与 double-sampling 概率被非参估计。理论推导了估计量在单点分位与跨分位紧集上的逐点与均匀渐近性质，并配套 bootstrap 实现逐点与均匀推断；模拟与 EHR 减重手术数据实证验证了方法。对您可能有用：本文将 MNAR 缺失 + double sampling 的识别框架引入 WQTE，与您在因果推断 identification theory 及 semiparametric efficiency 的兴趣直接对接。
- **关键技术**: `weighted quantile treatment effects`, `missing-not-at-random`, `double sampling`, `inverse-probability weighting`, `uniform asymptotic inference`, `bootstrap uniform inference`
- **为什么对您有用**: 本文直接推进因果推断 identification theory 子方向：在 MNAR 缺失下用 double sampling 放弃原始缺失假设来识别 WQTE，这是非标准缺失机制下的 identification 新结果。用您 very_familiar 的 minimax bounds / high-dimensional asymptotics 武器可以审视其 IPW estimator 在非参倾向得分估计下的均匀收敛率是否达到 minimax optimal，或用 moderately_familiar 的 semiparametric theory 推导该 MNAR+double sampling 设定下的 semiparametric efficiency bound 并构造 one-step / DR estimator 以提升效率。Follow-up 判断：**中期可做**——需先在 moderately_familiar 的 semiparametric theory 上长肌肉（推导 MNAR+double sampling 模型的 efficient influence function），再构造 debiased / DR 版本。

### 10. [10.1093/biomtc/ujaf066](https://doi.org/10.1093/biomtc/ujaf066) · [arXiv](https://arxiv.org/abs/2402.11466) — Nonparametric assessment of regimen response curve estimators
- **作者**: Cuong T Pham, Benjamin R Baer, Ashkan Ertefaie
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文在动态边际结构模型框架下，提出用反事实风险（counterfactual risk）作为目标参数，非参数地评估治疗方案反应曲线（regimen-response curve）工作模型的拟合优度。现有方法缺乏对工作模型选择的诊断工具，本文填补了这一空白。作者推导了逆概率加权（IPW）和典范梯度（canonical gradient）两类估计量，将反事实风险映射到观测数据，并建立了渐近线性性与半参数效率理论。当权重函数通过sieve估计时，IPW估计量达到渐近有效且线性，无需参数模型假设。方法在帕金森病LS1研究数据上应用，展示了评估不同曲线模型的实际价值。对您而言，本文在因果推断中提出了一种不依赖参数模型的工作模型诊断思路，可直接运用您熟悉的非参数统计和因果推断估计理论来理解其渐近性质，并探索将其扩展到更复杂的纵向或高维设定。
- **关键技术**: `dynamic marginal structural models`, `inverse probability weighting`, `canonical gradient`, `sieve estimation`, `asymptotic linearity`, `counterfactual risk`, `regimen-response curve`
- **为什么对您有用**: 本文聚焦于动态边际结构模型中工作模型选择这一具体因果推断问题，提出了非参数拟合优度检验的新框架，直接关联您的主要兴趣方向（因果推断中的估计与诊断）。您非常熟悉的非参数统计和因果推断估计理论（inverse problems、sieve估计）可直接用于复现和扩展其渐近结果，例如推导更紧的minimax界或放松权重估计的正则性条件。根据武器库判断：**立即可做**——核心武器（非参数统计、估计理论）已覆盖，您可着手将方法推广到高维协变量或纵向数据场景，或与双重稳健估计结合。

### 11. [10.1093/biomtc/ujaf002](https://doi.org/10.1093/biomtc/ujaf002) · [arXiv](https://arxiv.org/abs/2403.13934) — Data integration methods for micro-randomized trials
- **作者**: E Huch, I Nahum-Shani, L Potter, C Lam, D W Wetter, W Dempsey
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对微随机试验（MRT）提出数据整合方法，目标是利用多个MRT的相似干预数据更有效地估计因果excursion效应。现有方法仅依赖单次MRT数据，本文通过加权组合多个试验的估计量来提升统计效率，并允许估计量之间存在相关性。方法基于多元精度加权的一般化形式，推导了渐近最优的meta估计量。理论证明了该估计量在最小化渐近方差意义下的最优性，且不损失无偏性和推断校准性。在吸烟戒断案例中，结合两项MRT数据可将标准误降低30%以上。仿真验证了方法在有限样本下的表现。对研究者而言，该工作直接关联因果推断中的纵向试验设计和效率理论，其多元精度加权框架可与您熟悉的因果推断估计理论结合，用于多源数据整合场景。
- **关键技术**: `micro-randomized trials`, `causal excursion effect`, `multivariate precision weighting`, `meta-analysis`, `data integration`, `asymptotic optimality`
- **为什么对您有用**: (1) 本文聚焦因果推断中微随机试验（MRT）的纵向数据设计，与您primary interests中的'causal inference (longitudinal)'直接对口；(2) 您very_familiar中的'estimation theory in causal inference'可快速解析其加权估计的渐近方差推导，而您moderately_familiar中的'identification theory in causal inference'可帮助评估其因果excursion效应在多个试验间的可移性假设；(3) 立即可做：该方法基于经典多元精度加权，无需新工具即可复现或扩展至其他MRT数据集。

### 12. [10.1093/biomtc/ujaf044](https://doi.org/10.1093/biomtc/ujaf044) — Multiple bias calibration for valid statistical inference under nonignorable nonresponse
- **作者**: Seonghun Cho, Jae Kwang Kim, Yumou Qiu
- **期刊/来源**: Biometrics
- **机构**: Inha University · Iowa State University · Peking University
- **分类**: vol 81 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 论文针对非随机缺失（nonignorable nonresponse）下的统计推断难题，提出多重偏倚校准方法。该方法利用多个候选倾向得分模型（PS）结合经验似然（empirical likelihood），通过将多个工作PS模型纳入内部偏倚校准约束，只要工作模型中包含真实模型且其期望等于真实缺失率，即可消除选择偏差。估计量通过经验似然的最大化获得，具有渐近正态性和有效性。模拟研究比较了现有方法，并展示了NHANES身体脂肪数据实例。本文方法本质上是多重鲁棒（multi-robust）估计，对您的因果推断兴趣中的缺失数据/选择偏差处理（如proximal CI中的negative control）有直接参考价值。
- **关键技术**: `Empirical likelihood`, `Multiple bias calibration`, `Propensity score model`, `Calibration constraint`, `Nonignorable nonresponse`
- **为什么对您有用**: 这篇论文直接处理非随机缺失带来的选择偏差，属于因果推断中缺失数据问题的核心子方向。您对estimation theory in causal inference非常熟悉，可以立即将多重偏倚校准思想（多个工作模型+经验似然约束）移植到proximal causal inference或纵向因果推断的选择偏差校正中，甚至可尝试用经验似然替换常用的IPW/TMLE框架。这是一个立即可做的方向：您已有的nonparametric statistics和软件工具能快速验证其有限样本表现。

### 13. [10.1093/biomtc/ujaf061](https://doi.org/10.1093/biomtc/ujaf061) · [arXiv](https://arxiv.org/abs/2307.06552) — Learn-As-you-GO (LAGO) trials: optimizing treatments and preventing trial failure through ongoing learning
- **作者**: Ante Bing, Donna Spiegelman, Daniel Nevo, Judith J Lok
- **期刊/来源**: Biometrics
- **机构**: Boston University · Yale University · Tel Aviv University
- **分类**: vol 81 · issue 2
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文关注在大型公共健康实施试验中，当干预包在试验进行中因效果不佳而被调整时的统计推断问题。传统方法在干预包改变后无法得到有效推断，作者提出Learn-As-you-GO (LAGO) 框架，并首次将其从二分类结局推广到连续结局，且不局限于logistic回归，允许灵活的条件均值模型。核心贡献在于：在动态调整干预包的情况下，仍能给出干预效果的点估计和区间估计，并保持假设检验的显著性水平。此外，还构建了关于最优干预包（在满足预指定均值条件下成本最小）的置信集，以及所有干预包组成下结局均值的置信带。理论部分基于全新的数学推导，而非直接套用二分类情形的结果。该工作为临床试验设计提供了一套“边学边改”的有效推断工具，对因果推断中动态治疗策略的估计与检验有直接参考价值。
- **关键技术**: `conditional mean models`, `confidence set for optimal intervention`, `hypothesis testing for overall effect`, `interval estimation in adaptive designs`, `point estimation under ongoing adaptation`
- **为什么对您有用**: 该论文直接对应您因果推断兴趣中的动态治疗策略/序贯设计方向，提供了一个在干预包可调整的试验中仍能进行有效估计和检验的完整框架。您完全可以运用在因果推断估计理论（very_familiar）中的工具，比如用非参数效率理论评估其估计量是否达到半参数有效界，或利用高维统计视角检查其置信集的覆盖精度。**中期可做**：需要先在identification theory in causal inference（moderately_familiar）上进一步熟悉LAGO的识别条件（如无未测量混淆假设如何随调整操作改变），但一旦突破，即可将该方法应用于流行病学队列研究或您感兴趣的适应性随机试验设计。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1093/biomtc/ujaf042](https://doi.org/10.1093/biomtc/ujaf042) — PDC-MAKES: a conditional screening method for controlling false discoveries in high-dimensional multi-response setting
- **作者**: Wei Xiong, Han Pan, Tong Shen
- **期刊/来源**: Biometrics
- **机构**: University of International Business and Economics · Peking University · Shandong University of Finance and Economics
- **分类**: vol 81 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对高维（超高维）多响应设定下的特征筛选问题，提出一种模型无关的条件筛选方法PDC-MAKES，目标是识别重要预测变量并同时控制错误发现率(FDR)。方法基于偏距离相关(partial distance correlation)度量预测变量向量与响应向量在给定其他变量条件下的条件依赖关系，该度量对重尾数据和高度相关具有稳健性，并能识别边际无关但条件相关的变量。与现有研究不同，该方法允许条件变量也高达维，利用偏距离相关的性质实现了高维条件变量的处理。为实现FDR控制，采用去随机化的knockoff-e值更稳定地设定筛选阈值，理论上证明了该方法在温和条件下具有sure screening性质并同时控制FDR且获得更高检验功效。仿真和实际数据应用验证了优越性能。您对高维统计和非参数方法的熟悉可直接用于评估该方法的渐近性质，且偏距离相关的U-统计量结构可以引入higher-order U-statistics的视角进一步分析其效率。
- **关键技术**: `partial distance correlation`, `feature screening`, `false discovery rate control`, `knockoff-e-values`, `sure screening property`, `high-dimensional multi-response`
- **为什么对您有用**: 本文连接您的高维统计和非参数假设检验兴趣：偏距离相关是一种非参数依赖性度量，其估计量具有U-统计量结构，您very_familiar的非参数统计工具（如minimax bound）可用于分析该方法的sure screening性质，且您对U-统计量的熟悉可以进一步探索高阶U-统计量在该问题中的效率提升。FDR控制是假设检验的核心问题，您的high-dimensional asymptotics知识可直接用于检验其阈值设定的理论性质。立即可做：使用您very_familiar的非参数统计和高维渐近工具即可复现并扩展其理论分析。

## 非参数 / 半参数  *(nonparam_semipara, 6 篇)*

### 1. [10.1093/biomtc/ujaf064](https://doi.org/10.1093/biomtc/ujaf064) — Semiparametric joint modeling for biomarker trajectory before disease onset
- **作者**: Yifei Sun, Xiwen Zhao, Kwun Chuen Gary Chan, Wanwan Xu, Heather Allore, Yize Zhao
- **期刊/来源**: Biometrics
- **机构**: Columbia University · Yale University · University of Washington
- **分类**: vol 81 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在纵向 biomarker 与疾病发病时间的联合建模设定下，目标是估计 biomarker 轨迹的回归系数与非参数 baseline 均值函数，轨迹同时依赖自然时间（如年龄）与距发病时间两个时间尺度。作者提出 semiparametric joint model，通过 profile kernel estimating equation 估计回归参数与 unspecified baseline 函数，并处理实践中自然时间与 study-time 不同导致的 left-truncation 偏倚。大样本理论证明了估计量的收敛性质（参数部分的一致性与渐近正态性，非参数部分的收敛速率）。模拟验证了有限样本表现，应用于 Alzheimer 前期脑 cortical thickness 轨迹，发现 APOE4 携带者在发病前水平更低。对您可能有用：该文的 profile kernel 估计与 left-truncation 处理可直接迁移到 longitudinal causal inference 中处理 right-censored / left-truncated mediator 轨迹的 semiparametric 估计问题。
- **关键技术**: `semiparametric joint model`, `profile kernel estimating equation`, `left-truncation adjustment`, `two time-scale trajectory`, `asymptotic normality`
- **为什么对您有用**: 直接连接到 longitudinal causal inference 与 semiparametric theory 子方向：profile kernel estimating equation 是您 moderately_familiar 的 M-estimation 与 semiparametric theory 的典型应用场景，left-truncation 偏倚修正在纵向因果 mediator 分析中常见。用您 very_familiar 的非参数统计与 moderately_familiar 的 semiparametric theory 即可展开读并尝试推导其 profile 步骤的 influence function——**立即可做**。

### 2. [10.1093/biomtc/ujaf072](https://doi.org/10.1093/biomtc/ujaf072) — Non-parametric estimators of hazard ratios for comparing two survival curves
- **作者**: Mihai Giurcanu, Theodore Karrison
- **期刊/来源**: Biometrics
- **机构**: Chicago Department of Public Health · University of Chicago
- **分类**: vol 81 · issue 2
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对两组生存曲线比较中的风险比，提出基于组别累积风险函数的估计方程，构造了非参数估计量。首先在常数风险比假设下推导估计量的渐近性质；随后将方法推广至时变风险比情形，利用局部常数近似将时间轴分段，并给出变化点选择准则。进一步，作者发展了分层估计量及跨层风险比异质性检验。模拟研究表明：在有限样本下，所提估计量在效率和覆盖概率准确性方面与Cox部分极大似然估计（MLE）竞争力相当，部分设定下表现更优。本文方法无需比例风险假设，适用于更灵活的生存数据建模。对您而言，该工作属于非参数统计在生物医学中的应用，您熟悉的非参数统计工具可直接用于理解其渐近推导，并可考虑将估计方程技术迁移至因果推断中的风险比估计问题。
- **关键技术**: `estimating equations`, `cumulative hazard function`, `local constant approximation`, `change point selection`, `stratified estimation`
- **为什么对您有用**: 本文直接对应您primary interest中的非参数统计理论，您非常熟悉的nonparametric statistics武器可帮助您快速理解其渐近论证与估计方程构造。立即可做：您可在因果推断框架下（例如处理效应的风险比）尝试采用类似估计方程方法，或检验其有限样本性能。此外，该文提出的分层风险比异质性检验也涉及假设检验主题，与您mathematical statistics兴趣一致。

### 3. [10.1093/biomtc/ujaf051](https://doi.org/10.1093/biomtc/ujaf051) — Distance weighted directional regression for Fréchet sufficient dimension reduction
- **作者**: Chao Ying, Zhou Yu, Xin Zhang
- **期刊/来源**: Biometrics
- **机构**: University of Wisconsin–Madison · East China Normal University · Florida State University
- **分类**: vol 81 · issue 2
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 针对非欧几里得响应变量的充分降维问题，本文提出距离加权方向回归（distance weighted directional regression）方法。该方法将经典的方向回归推广到Fréchet充分降维框架，同时处理线性与非线性降维。新公式通过距离加权统一了欧几里得与非欧几里得响应的处理，并进一步扩展到核化非线性降维。理论上，推导了线性Fréchet方向回归估计量的渐近正态性以及非线性估计量的收敛速率。模拟和两个真实数据应用（人类死亡率建模、糖尿病患病率分析）展示了方法在解释性和预测准确性上的优势。对于您而言，本文的非参数降维理论可与您熟悉的minimax界结合来评估其收敛率的最优性，并可能为因果推断中的高维协变量降维（例如中介分析或工具变量）提供新思路。
- **关键技术**: `Fréchet sufficient dimension reduction`, `distance weighted directional regression`, `kernel methods`, `asymptotic normality`, `convergence rate`, `non-Euclidean data`
- **为什么对您有用**: 直接连接到您的非参数/半参数理论兴趣，尤其是非欧几里得数据的充分降维这一新兴方向。您可以利用非常熟悉的非参数统计和minimax界工具来检验本文收敛率是否达到最优，并评估其在实际应用中的统计效率。此外，本文方法可迁移至因果推断中的高维协变量降维问题（例如构建倾向得分或替代指标），属于中期可做的扩展：需先掌握Fréchet度量空间和SDR框架，这对应技术武库中moderately_familiar的identification理论部分。

### 4. [10.1093/biomtc/ujaf065](https://doi.org/10.1093/biomtc/ujaf065) — Probabilistic exponential family inverse regression and its applications
- **作者**: Daolin Pang, Ruoqing Zhu, Hongyu Zhao, Tao Wang
- **期刊/来源**: Biometrics
- **机构**: Shanghai Jiao Tong University · University of Illinois Urbana-Champaign · Yale University
- **分类**: vol 81 · issue 2
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在高维回归与分类的充分降维设定下，针对离散型协变量（如物种有无记录、单细胞测序reads），本文提出 PrEFIR 方法，假设给定响应与潜在因子后协变量服从单参数指数族，从而识别并估计充分降维方向。核心机制在于引入潜在因子建模，使得降维方向不仅源于响应变量，也源于潜在因子；进一步通过双指数族引入散度参数处理过度/不足离散，并采用最大层次似然（maximum hierarchical likelihood）进行估计，配合高度可并行算法实现计算。理论层面给出了潜在因子框架下充分降维的 identification 条件与估计一致性，仿真与真实数据（生态/单细胞）验证了方法有效性。对您可能有用：该文的指数族潜在因子降维与层次似然估计，为处理混合型协变量的半参数模型提供了新视角。
- **关键技术**: `sufficient dimension reduction`, `exponential family inverse regression`, `latent factor modeling`, `double exponential family`, `maximum hierarchical likelihood`, `parallelizable EM-type algorithm`
- **为什么对您有用**: 本文连接到 semiparametric theory 中的充分降维子方向，特别是离散协变量下的 identification 与 estimation。您武器库中的 M-estimation theory（moderately_familiar）可以用来审视其 maximum hierarchical likelihood 的渐近性质与效率，而 software development（very_familiar）可直接评估其并行算法的实现复杂度。中期可做：需先在 M-estimation theory 上长肌肉以严格推导其估计量的 semiparametric efficiency bound。

### 5. [10.1093/biomtc/ujaf063](https://doi.org/10.1093/biomtc/ujaf063) — Conformal predictive intervals in survival analysis: a resampling approach
- **作者**: Jing Qin, Jin Piao, Jing Ning, Yu Shen
- **期刊/来源**: Biometrics
- **机构**: National Institute of Allergy and Infectious Diseases · University of Southern California · The University of Texas MD Anderson Cancer Center
- **分类**: vol 81 · issue 2
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在一般右删失生存数据设定下，目标是构建个体生存时间的分布无关 conformal prediction interval（PI），克服现有 Candès 等方法仅适用于 Type I 删失且只能估计下界的局限。核心机制是利用 bootstrap 重抽样来估计删失分布，进而对 conformal score 进行加权修正以处理协变量偏移，并在不同 working regression model（如 Cox AFT）下构建单侧与双侧 PI。方法在 working model 误设时仍保持有限样本覆盖率，模拟显示在中等删失比例下下界覆盖优良、双侧覆盖合理，并应用于乳腺癌生存预测。对您可能有用：本文将 conformal prediction 与生存分析删失机制结合，其 bootstrap 加权修正思路可类比因果推断中 IPW 处理 missing/at-risk 人群的协变量偏移问题。
- **关键技术**: `conformal prediction`, `right-censored survival data`, `bootstrap resampling`, `covariate shift weighting`, `distribution-free coverage`
- **为什么对您有用**: 本文直接连接因果推断与半参数理论中处理 missing data / selection bias 的 IPW 思路——用 bootstrap 估计删失概率做加权修正，与您熟悉的 inverse probability weighting 技术同源。用您 very_familiar 的 nonparametric statistics 与 software development 武器，可以复现其 bootstrap conformal 流程并探索将此 covariate-shift 修正迁移到 causal inference 的 sensitivity analysis 设定中。立即可做。

### 6. [10.1093/biomtc/ujaf053](https://doi.org/10.1093/biomtc/ujaf053) · [arXiv](https://arxiv.org/abs/2409.17404) — Bayesian covariate-dependent graph learning with a dual group spike-and-slab prior
- **作者**: Zijian Zeng, Meng Li, Marina Vannucci
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在协变量依赖的图模型设定下，目标是估计随协变量变化的精度矩阵（3维数组参数），以刻画异质数据中的条件依赖结构。本文提出 dual group spike-and-slab prior，沿节点方向与协变量方向实现双层分组选择，同时保留局部（元素级）稀疏性；采用嵌套策略分别处理不同分组方向带来的建模挑战。计算方面，开发了全参数 Gibbs sampler，避免了高维图模型常见的调参困难，提升了计算可行性。模拟显示图恢复精度优于现有方法；微生物组数据应用展示了微生物交互及协变量效应的推断。对您有用之处在于：该双层稀疏先验的结构化分组思想可迁移至高维因果推断中多干预变量的结构学习，且其 Gibbs sampler 的嵌套设计为统计计算武器库提供了可借鉴的矩阵/张量参数采样方案。
- **关键技术**: `dual group spike-and-slab prior`, `covariate-dependent graphical model`, `nested variable selection`, `Gibbs sampler`, `precision matrix estimation`, `3-dimensional array parameterization`
- **为什么对您有用**: 本文连接到您的高维统计与统计计算两个子方向：3维数组参数化与双层稀疏先验本质上是对张量/矩阵参数的结构化建模，其嵌套分组选择机制与您熟悉的 einsum / tensor contraction 视角有概念对接；全 Gibbs sampler 的设计直接落入统计计算（数值方法与软件）范畴。用您 very_familiar 的软件开发与高维渐近理论可以立即可做：复现其 Gibbs sampler 并在更高维设定下测试计算瓶颈，或用 minimax bound 检验其图恢复精度声称是否紧。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1093/biomtc/ujaf060](https://doi.org/10.1093/biomtc/ujaf060) · [arXiv](https://arxiv.org/abs/2311.15031) — Robust and efficient semi-supervised learning for Ising model
- **作者**: Daiqing Wu, Molei Liu
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究Ising模型在半监督设定下的参数推断问题，其中仅有少量标注结果（疾病表型）和大量未标注样本（辅助特征）。核心方法是：先对结果变量关于辅助特征建立条件模型，然后将监督估计的得分函数投影到辅助特征空间，利用未标注样本估计该投影，从而构造出无偏且方差更小的半监督估计量。这本质上等价于用Efficient Influence Function的投影部分自动进行方差缩减。针对条件模型可能误设带来的效率损失，作者进一步提出了内在高效更新和集成策略来稳健化估计。渐近理论证明该方法保持无偏性且方差小于监督估计。模拟与MIMIC-III ICU表型数据表明，在条件模型正确或轻度误设下均优于现有半监督方法。该方法将半参数效率框架与半监督学习结合，对因果推断中利用未标注数据提升ATE估计效率有直接借鉴价值。
- **关键技术**: `semi-supervised inference`, `Ising model`, `score function projection`, `efficient influence function`, `conditional model robustness`, `variance reduction via unlabeled data`
- **为什么对您有用**: 本文属于效率理论（semiparametric efficiency bounds/double ML）的具体应用，处理的是Ising模型参数而非因果效应，但投影得分函数的技术路径恰好与Efficient Influence Function/DML的orthogonal score思想同构。您可以用非常熟悉的非参统计与半参理论来分析其投影方法是否达到半参效率界，并可立即将同一框架移植到因果推断的ATE/ATT估计中，利用大量未标记个体的协变量提升效率。立即可做。

## 数理统计 / 假设检验  *(hypothesis_testing, 6 篇)*

### 1. [10.1093/biomtc/ujaf036](https://doi.org/10.1093/biomtc/ujaf036) — Statistical inference on the relative risk following covariate-adaptive randomization
- **作者**: Fengyu Zhao, Yang Liu, Feifang Hu
- **期刊/来源**: Biometrics
- **机构**: George Washington University · Renmin University of China
- **分类**: vol 81 · issue 2
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 在协变量适应性随机化（CAR）试验设定下，本文研究相对风险（relative risk, RR）的协变量调整估计量及其假设检验性质，关键假设涵盖广泛类别的 CAR 程序（如 stratified permuted block, minimization）。作者首先推导了该估计量的渐近分布，发现由于 CAR 引入的协变量平衡效应，传统标准误估计忽略了组间协变量相关性，导致常规 Wald 检验过于保守、Type I error 低于名义水平。为此，提出 model-based 与 model-robust 两种调整标准误的方法以修正保守偏差，并证明了调整后检验的渐近有效性。模拟实验验证了理论发现及调整方法在 Type I error 控制与 power 提升上的优势。对您可能有用：本文展示了 CAR 设计下检验统计量方差修正的具体推导，直接连接到您对假设检验与因果推断估计理论的兴趣。
- **关键技术**: `covariate-adaptive randomization`, `relative risk estimation`, `conservative Wald test correction`, `model-robust standard error`, `asymptotic variance derivation under CAR`
- **为什么对您有用**: 本文直接连接到您 primary interest 中的假设检验与因果推断估计理论：CAR 试验下 RR 估计量的方差修正本质上是一个 semiparametric inference 问题，与您熟悉的 efficiency theory 相关。您武器库中 M-estimation theory 与 semiparametric theory（moderately_familiar）可以直接用来审视其 model-robust variance estimator 是否达到 semiparametric efficiency bound，或推广到其他 estimand（如 odds ratio）。**中期可做**：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，以将本文的 CAR-variance-correction 框架系统化到更一般的 estimand 与高维协变量设定。

### 2. [10.1093/biomtc/ujaf069](https://doi.org/10.1093/biomtc/ujaf069) — On the finite-sample and asymptotic error control of a randomization-probability test for response-adaptive clinical trials
- **作者**: Nina Deliu, Sofia S Villar
- **期刊/来源**: Biometrics
- **机构**: University of Cambridge · MRC Biostatistics Unit · Sapienza University of Rome
- **分类**: vol 81 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在 response-adaptive randomized clinical trial 设定下，目标是解决 adaptive design 导致的 finite-sample type-I error 失控与 power 不足问题，estimand 为 treatment effect 的假设检验。作者提出基于 randomization-probability 的 novel test statistic，推导了其 finite-sample 与 asymptotic type-I error guarantee，并在 Thompson sampling 这一 Bayesian adaptive design 下验证了理论性质。核心机制利用 adaptive randomization probability 的已知分布结构绕过复杂 likelihood，实现 frequentist error control 同时保留 expected outcome optimality。实证通过 phase-II oncology trial 与模拟展示 power 优势。对您有用：该 paper 在 adaptive design 下用 randomization probability 构造 test statistic 并给出 finite-sample error bound，直接连接 hypothesis testing 与 sequential experiment 的 inferential challenge。
- **关键技术**: `randomization-probability test statistic`, `finite-sample type-I error control`, `response-adaptive randomization`, `Thompson sampling`, `asymptotic power efficiency`
- **为什么对您有用**: 直接连接 hypothesis testing 子方向：在 adaptive/sequential experiment 下构造有 finite-sample error guarantee 的 test statistic，是经典检验理论在非标准设计下的延伸。用您 very_familiar 的 minimax bounds 与 M-estimation theory（moderately_familiar）可以审视其 asymptotic power efficiency 是否达到某种 optimality，或探索该 randomization-probability statistic 的 influence function 结构。中期可做：需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以严格推导该 test statistic 在更一般 adaptive design 下的 semiparametric efficiency bound。

### 3. [10.1093/biomtc/ujaf050](https://doi.org/10.1093/biomtc/ujaf050) — A semiparametric quantile regression rank score test for zero-inflated data
- **作者**: Zirui Wang, Wodan Ling, Tianying Wang
- **期刊/来源**: Biometrics
- **机构**: Tsinghua University · Cornell University · Colorado State University
- **分类**: vol 81 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 零膨胀数据常见于经济学、医疗和环境科学等领域，传统参数模型（如ZIP、ZINB）因强分布假设在复杂非线性关联下失效。本文提出ZIQ-SIR检验，结合分位数单指标模型与秩得分检验，半参数地处理零膨胀与过离散，无需事先指定误差分布。方法核心是构造基于分位数回归的秩得分统计量，通过置换或渐近近似控制Type I错误，并利用单指标结构规避维度诅咒。模拟表明ZIQ-SIR在保持正确检验水平的同时，比现有参数/半参数方法显著提升对新关联的检测功效。在哥伦比亚肠道微生物组数据中，该方法发现了更多有意义的菌群-性状关联。该检验补充了零膨胀场景下的假设检验工具，您可基于非参数统计与秩检验的理论基础快速纳入研究。
- **关键技术**: `quantile single-index model`, `rank score test`, `semi-parametric regression`, `zero-inflated data testing`
- **为什么对您有用**: 直接对接您'假设检验'与'半参数理论'两大兴趣束，尤其是零膨胀这一实际数据常见而理论较少的检验设置。您已掌握的nonparametric statistics（very_familiar）可直接用于理解秩得分统计量的渐近性质，并可尝试将ZIQ-SIR与您熟悉的U-statistics视角或HOIF框架结合，拓展至更高阶的关联检测或因果推断中的处理效应检验。follow-up 粗判：立即可做——您对假设检验的渐近理论足够熟悉，只需补读分位数秩得分构造细节即可撰写方法评注或进行模拟比较。

### 4. [10.1093/biomtc/ujaf034](https://doi.org/10.1093/biomtc/ujaf034) · [arXiv](https://arxiv.org/abs/2405.02551) — Power-enhanced two-sample mean tests for high-dimensional microbiome compositional data
- **作者**: Danning Li, Lingzhou Xue, Haoyi Yang, Xiufan Yu
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在高维微生物组成分数据（单位 simplex 约束）的两样本均值检验设定下，目标是检测 $\mu_1 \neq \mu_2$，现有 maximum-type 与 quadratic-type 检验在不同稀疏/密集信号模式下各有盲区。本文基于 P-value 组合策略提出 power-enhanced 检验，将两种检验的优势整合以覆盖更广的 alternative space。理论上通过 Gaussian approximation 保证了 Type-I error 的精确控制，并证明组合检验在 maximum-type 与 quadratic-type 均失效的信号过渡区实现了 power 提升。模拟与真实微生物组数据实证显示，新方法在多种信号模式下较现有方法有显著 power 优势。对您可能有用：该文的高维 P-value 组合与 Gaussian approximation 技术可直接迁移到您关注的 hypothesis testing 与 high-dimensional asymptotics 交叉方向。
- **关键技术**: `P-value combination`, `power enhancement`, `Gaussian approximation for high-dimensional vectors`, `maximum-type test`, `quadratic-type test`, `compositional data constraint`
- **为什么对您有用**: 本文直接连接您 primary interest 中的 hypothesis testing 与 high-dimensional statistics 交叉方向，其 Gaussian approximation 与 P-value 组合框架是高维检验的经典工具。您武器库中 very_familiar 的 minimax bounds 与 high-dimensional asymptotics 可直接用于审视其声称的 power enhancement 是否在 minimax 意义下紧（例如过渡区的 rate 是否达到 optimal），或可将该组合策略推广至成分数据之外的更一般高维依赖结构。**立即可做**：用 very_familiar 的高维渐近理论验证其 Gaussian approximation 条件与 power 界的紧性。

### 5. [10.1093/biomtc/ujaf035](https://doi.org/10.1093/biomtc/ujaf035) · [arXiv](https://arxiv.org/abs/2212.08856) — Inference with approximate local false discovery rates
- **作者**: Rajesh Karmakar, Ruth Heller, Saharon Rosset
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 该论文在Efron两群组模型基础上，针对大规模多重检验中检验统计量存在依赖性的问题，提出了基于邻域信息的局部错误发现率(locFDR_N)方法。该方法利用每个假设的N-邻域内的检验统计量来估计该假设为原假设的后验概率，从而在控制边际错误发现率的同时提高检验功效。理论证明，在决策仅依赖N-邻域的限制下，基于locFDR_N的拒绝规则是最优的，且功效随N增大而单调递增。为了在计算复杂度和功效之间取得平衡，建议选择计算上可行的最大N。模拟表明，即使使用很小的N，该方法也显著优于现有实用方法。最后在身高GWAS数据中展示了如何利用局部依赖结构发现更多显著关联位点。对您而言，本文提供了处理大规模多重检验中依赖性的新视角，与您假设检验的兴趣方向直接相关，武器库中的非参数统计和minimax bound可用来刻画该方法在更复杂依赖结构下的最优性。
- **关键技术**: `local false discovery rate (locFDR)`, `neighborhood-based dependency modeling`, `large-scale multiple testing`, `optimal decision under restriction`
- **为什么对您有用**: 本文直接对应您primary interest中的hypothesis testing，特别是大规模多重检验中的依赖性问题。它提出了locFDR_N方法，将邻域信息纳入决策，理论上证明了最优性。您的武器库中'nonparametric statistics'和'minimax bounds for estimation problems'可用于分析该方法在更一般依赖结构下的最优性界或速率，属于中期可做——需先在'moderately_familiar'的HOIF或高阶U统计理论中熟悉局部依赖建模。

### 6. [10.1093/biomtc/ujaf073](https://doi.org/10.1093/biomtc/ujaf073) · [arXiv](https://arxiv.org/abs/2311.17467) — Design of platform trials with a change in the control treatment arm
- **作者**: Peter Greenstreet, Thomas Jaki, Alun Bedding, Pavel Mozgunov
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 在多臂多阶段（MAMS）平台试验设定下，当某处理被确证优于对照后成为新标准对照，剩余处理将针对新对照继续检验。核心 estimand 是总体功效（找到最优处理的概率）与条件功效/条件 I 类错误（针对当前对照的检验表现）。作者证明：在频率学派框架下，保留对照切换前收集的历史信息可能损害总体与条件功效，但同时也会降低条件 I 类错误；通过解析推导与数值模拟刻画了信息保留导致功效下降的具体条件。讨论了连续平台试验与利用同一基础设施启动全新试验的设计抉择。对您有用：本文对平台试验中多重检验功效与 I 类错误的解析刻画，为 longitudinal/sequential causal inference 中动态对照切换的 identification-estimation 稳定性提供了频率学派视角的参考。
- **关键技术**: `multi-arm multi-stage (MAMS) trial`, `conditional power analysis`, `conditional type I error control`, `platform trial design`, `group sequential testing`
- **为什么对您有用**: 本文直接涉及 hypothesis testing 在复杂序贯试验设计中的频率学派性质（条件功效 vs 条件 I 类错误），属于 primary interest 中数学统计/假设检验子方向。技术武器库中 minimax bounds 与 M-estimation theory 可用于审视其功效界是否紧、以及对照切换后 estimator 的 asymptotic 行为是否可进一步用 semiparametric efficiency 刻画。**中期可做**：需先在 moderately_familiar 的 identification theory 上长肌肉，以将频率学派条件检验框架转化为动态因果 identification 下的 debiased estimator 场景。

## 流行病学  *(epidemiology, 9 篇)*

### 1. [10.1093/biomtc/ujaf059](https://doi.org/10.1093/biomtc/ujaf059) — Improving estimation efficiency for case-cohort studies with a cure fraction
- **作者**: Qingning Zhou, Xu Cao
- **期刊/来源**: Biometrics
- **机构**: University of North Carolina at Charlotte · University of California, Riverside
- **分类**: vol 81 · issue 2
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文考虑存在治愈分数（不会经历事件）的病例-队列研究，采用两阶段抽样设计（广义病例-队列设计）以降低成本并提高检验效能。在 semiparametric transformation mixture cure models 下，提出两步估计程序：第一步基于完全观测数据（子队列 + 所有病例）使用 sieve maximum weighted likelihood 结合 EM 算法；第二步利用全数据中廉价协变量或辅助变量构建工作模型更新初始估计量。理论证明了更新估计量的一致性和渐近有效性（至少不差于第一步估计量），且工作模型可以错误指定。通过加权 bootstrap 进行方差估计，模拟和实际数据分析（National Wilms’ Tumor Study）验证了有限样本性能。与您的兴趣连接：该文使用了效率提升技巧（augmentation via working model），与 semiparametric efficiency theory 中的 one-step 或 double robust 思想相通，同时属于流行病学中两阶段设计的实际应用，可作为该领域方法实现的参考。
- **关键技术**: `two-stage sampling`, `semiparametric transformation mixture cure model`, `sieve M-estimation`, `EM algorithm`, `working model augmentation`, `weighted bootstrap`
- **为什么对您有用**: 本文属于流行病学中两阶段抽样设计的应用方法，利用了 semiparametric efficiency 的核心思路（通过工作模型提升估计效率），与您 'estimation theory in causal inference' 和 'semiparametric theory' 的 moderately_familiar 工具箱有直接接口。作为流行病学真实数据集（Wilms Tumor Study）的示例，适合作为该领域的入门阅读，武器库中的 nonparametric statistics 和 M-estimation 足以支撑理解其渐近论证。

### 2. [10.1093/biomtc/ujaf080](https://doi.org/10.1093/biomtc/ujaf080) · [arXiv](https://arxiv.org/abs/2503.16732) — Leveraging two-phase data for improved prediction of survival outcomes with application to nasopharyngeal cancer
- **作者**: Eun Jeong Oh, Seungjun Ahn, Tristan Tham, Min Qian
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对鼻咽癌研究中HPV状态大量缺失的两阶段数据，提出一种结合专家知识和预后指数的生存预测模型，目标为提升癌症患者生存预测的准确性。方法采用两阶段设计：第一阶段全样本拥有常规协变量，第二阶段子样本测量HPV；通过构建预后指数和临床重要性权重，充分利用所有数据而不丢弃HPV缺失样本。模型评估采用C指数、校准斜率和综合Brier评分，模拟和真实数据表明该方法一致优于对比方法。对您的用处：本文提供了流行病学纵向数据中缺失协变量处理的应用范例，其数据结构和分析框架可与您因果推断中的缺失数据方法（如proximal CI中的negative control）结合思考，延伸至处理混杂变量缺失的场景。
- **关键技术**: `Two-phase design`, `Prognostic index`, `Missing data`, `C-index`, `Integrated Brier score`, `Expert-guided method`
- **为什么对您有用**: 本文是流行病学中处理缺失协变量的实证研究，直接对接研究者对流行病学应用的数据集兴趣；研究者可利用estimation theory in causal inference（very_familiar）的工具评估该方法在因果推断问题中的适用性，例如考虑用influence function调整缺失导致的偏差。立即可做：阅读并复现其分析流程，作为流行病学案例理解。

### 3. [10.1093/biomtc/ujaf003](https://doi.org/10.1093/biomtc/ujaf003) — A semicompeting risks model with an application to UK Biobank data to identify risk factors for diabetes onset and progression
- **作者**: Md Tuhin Sheikh, Hongyu Zhao
- **期刊/来源**: Biometrics
- **机构**: Yale University
- **分类**: vol 81 · issue 2
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在流行病学半竞争风险设定下（两个非终止事件 T2D 与并发症、一个终止事件死亡），目标是识别不同疾病阶段风险因素的效应。作者提出基于共享 gamma frailty 的贝叶斯半竞争风险模型，通过 frailty 引入非终止与终止事件间的依赖结构以处理不可观测异质性。为利用入组时已患糖尿病的 prevalent cases，引入 power prior 方法整合历史信息，理论上改善了模型拟合与估计效率。模拟验证了框架的有效性，并在 UK Biobank 半百万数据上识别了 T2D 发病、进展至并发症及死亡各阶段的风险因素。对您可能有用：该文展示了 UKB 半竞争风险数据结构及贝叶斯 frailty 建模，可作为流行病学因果推断应用的数据集与模型参考。
- **关键技术**: `semicompeting risks model`, `shared gamma frailty`, `Bayesian hierarchical model`, `power prior`, `prevalent cases integration`, `UK Biobank`
- **为什么对您有用**: (1) 连接到流行病学因果推断应用子方向，提供了 UKB 半竞争风险数据集与多阶段疾病进展模型的具体案例；(2) 武器库中 semiparametric theory 与 identification theory 可用于审视其 frailty 识别假设与 power prior 效率增益的严格性，但本文核心是贝叶斯 frailty 框架而非 semiparametric efficiency；(3) **中期可做**：若想将 semiparametric efficiency / HOIF 工具引入半竞争风险多阶段效应估计以获得非贝叶斯的 n^{-1/2}-CAN efficient estimator，需先在 moderately_familiar 的 semiparametric theory 上长肌肉（特别是多阶段依赖结构下的 influence function 推导）。

### 4. [10.1093/biomtc/ujaf046](https://doi.org/10.1093/biomtc/ujaf046) · [arXiv](https://arxiv.org/abs/2405.11239) — Uncovering mortality patterns and hospital effects in COVID-19 heart failure patients: a novel multilevel logistic cluster-weighted modeling approach
- **作者**: Luca Caldera, Chiara Masci, Andrea Cappozzo, Marco Forlani, Barbara Antonelli, Olivia Leoni et al.
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在 Lombardy 地区 COVID-19 期间心衰患者住院的流行病学设定下，目标是评估医院对 45 天死亡率的影响并进行患者画像。本文提出 multilevel logistic cluster-weighted model，通过混合模型灵活处理连续与二值变量的依赖结构，同时捕捉不同患者子群的异质性及医院层面的随机效应。参数估计采用定制的 classification EM (CEM) 算法，模拟研究对比了其与竞争模型的表现。实证分析基于 Lombardy 行政数据，场景分析展示了模型在处理多重异质性来源时的有效性，为医疗决策提供患者特异性路径参考。对您可能有用：本文提供了流行病学队列中评估医院效应（类似 IV 或 cluster-level 因果效应）的半参数混合建模案例与真实数据集。
- **关键技术**: `multilevel logistic model`, `cluster-weighted model`, `classification EM algorithm`, `hospital profiling`, `scenario analysis`
- **为什么对您有用**: (1) 连接到 epidemiology secondary interest 中的 applied causal work 与 hospital effect 评估设定，提供了真实行政数据集；(2) 用 technical_arsenal 中 moderately_familiar 的 M-estimation theory 可以审视其 CEM 算法的收敛性与随机效应识别条件，或用 very_familiar 的 software development 复现其计算流程；(3) 中期可做——若想将 hospital effect 从纯预测提升到因果推断（如用 IV 或 proximal CI 消除医院选择偏倚），需先在 moderately_familiar 的 identification theory in causal inference 上长肌肉。

### 5. [10.1093/biomtc/ujaf040](https://doi.org/10.1093/biomtc/ujaf040) · [arXiv](https://arxiv.org/abs/2303.01186) — Discrete-time competing-risks regression with or without penalization
- **作者**: Tomer Meir, Malka Gorfine
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在离散时间竞争风险框架下，目标是在右删失与多类型终点共存时估计 cause-specific hazard / cumulative incidence，假设时间离散或分组测量。本文提出基于 Fine-Gray 型 logistic 回归的离散时间估计程序，核心优势是将惩罚回归（L1/L2 正则）与特征筛选直接嵌入 cause-specific hazard 拟合，避免了连续时间 subdistribution hazard 估计中正则化的技术障碍。理论层面给出参数估计的渐近性质，实证通过模拟比较无惩罚与惩罚版本在有限样本下的表现，并在 ICU 住院时长数据（三种竞争终点：出院、转院、死亡）上展示应用。对您可能有用：该文提供了流行病学队列离散竞争风险的完整建模与软件（PyDTS），可作为离散时间因果推断中 right-censoring 处理的参考案例。
- **关键技术**: `discrete-time competing risks`, `Fine-Gray logistic regression`, `regularized regression for subdistribution hazard`, `cause-specific hazard estimation`, `right censoring adjustment`
- **为什么对您有用**: 本文连接到流行病学因果推断的离散时间竞争风险设定，提供了可直接调用的 PyDTS 软件包与 ICU 真实数据集，适合作为离散生存分析的应用入门。武器库中的软件开发与 M-estimation 理论足以支撑对该方法渐近性质的深入审查与扩展，但若要将其嵌入 longitudinal causal inference 框架，需先在 moderately_familiar 的 identification theory 上长肌肉（处理竞争风险下的 counterfactual cumulative incidence identification）。**中期可做**。

### 6. [10.1093/biomtc/ujaf052](https://doi.org/10.1093/biomtc/ujaf052) · [arXiv](https://arxiv.org/abs/2405.00179) — A Bayesian joint longitudinal-survival model with a latent stochastic process for intensive longitudinal data
- **作者**: Madeline R Abbott, Walter H Dempsey, Inbal Nahum-Shani, Lindsey N Potter, David W Wetter, Cho Y Lam et al.
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 2/10 · novelty: `application`
- **摘要**: 在移动健康(mHealth)密集纵向数据(ILD)设定下，目标是联合建模多变量纵向轨迹与事件时间（首次吸烟复发），以捕捉快速波动对事件风险的即时影响。核心方法是将9维情绪强度降维为2个时变潜在因子，并用Ornstein-Uhlenbeck(OU)随机过程刻画其动态演化，再将其嵌入参数化hazard模型关联生存结局。采用Bayesian框架进行联合推断，模拟评估了估计性能。实证分析了戒烟mHealth数据，发现正/负情感潜在状态显著捕捉了首次复吸风险。对您可能有用：该文展示了ILD下joint longitudinal-survival模型的应用范式，OU过程提供了一种连续时间潜在因子的建模思路。
- **关键技术**: `joint longitudinal-survival model`, `Ornstein-Uhlenbeck process`, `latent factor model`, `parametric hazard model`, `Bayesian inference`, `intensive longitudinal data`
- **为什么对您有用**: 本文属于流行病学/行为医学的应用因果与建模工作，直接连接到您secondary interest中的epidemiology应用因果与数据集。(1) 作为ILD与joint model的入门读物，文章清晰展示了多变量纵向降维+连续时间随机过程的建模动机与数据结构，对统计学者较易读；(2) 您武器库中的very_familiar项（软件开发、高维纵向）足以支撑进入此类ILD计算与建模方向；(3) 值得花时间浏览全文的数据结构与OU过程设定部分，但方法学novelty有限（标准Bayesian joint model + OU），无需深读理论细节。

### 7. [10.1093/biomtc/ujaf074](https://doi.org/10.1093/biomtc/ujaf074) · [arXiv](https://arxiv.org/abs/2312.13097) — Power calculation for cross-sectional stepped wedge cluster randomized trials with a time-to-event endpoint
- **作者**: Mary Ryan Baumann, Denise Esserman, Monica Taljaard, Fan Li
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究横截面阶梯楔形集群随机试验（SW-CRT）在截断生存结局下的样本量与功效计算问题，目标参数为分层边际 Cox 模型下的干预效应，关键假设为集群内跨期与期内相关性参数恒定。核心方法提出分层边际 Cox 模型作为分析框架，并推导出 robust sandwich variance 的显式解析表达式，从而避免计算密集的模拟即可完成功效计算。基于 Wald 与 robust score 检验的功效公式在多种有限样本场景下通过模拟验证，并提供了 R Shiny 应用以实现样本量与功效的在线计算。对您可能有用：若未来在流行病学队列或集群试验设计中遇到生存结局与因果推断结合的问题，本文的 robust sandwich variance 解析推导可作为方法论参考。
- **关键技术**: `stepped wedge cluster randomized trial`, `stratified marginal Cox model`, `robust sandwich variance`, `Wald test power formula`, `robust score test`, `intra-cluster correlation`
- **为什么对您有用**: 本文属于流行病学集群试验设计，连接到 epidemiology secondary interest 的因果推断应用场景（SW-CRT 本身是干预效应识别的随机化设计）。从 technical_arsenal 看，本文的 robust sandwich variance 解析推导与您 moderately_familiar 的 M-estimation theory 有直接交集，可用 M-estimation 的 influence function 视角审视其方差公式是否可进一步泛化至更复杂的依赖结构。Follow-up 判断：**中期可做**——若想将此框架推广到更一般的 semiparametric efficiency bound 或处理非恒定相关性，需先在 moderately_familiar 的 semiparametric theory 上长肌肉（特别是生存数据下的 influence function 推导）。

### 8. [10.1093/biomtc/ujaf067](https://doi.org/10.1093/biomtc/ujaf067) · [arXiv](https://arxiv.org/abs/2405.11720) — Estimating optimally tailored active surveillance strategy under interval censoring
- **作者**: Muxuan Liang, Yingqi Zhao, Daniel W Lin, Matthew Cooperberg, Yingye Zheng
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在癌症主动监测（AS）设定下，目标是估计个体化活检策略的真阳性率（TPR）与真阴性率（TNR），关键难点在于疾病进展结局受区间删失（interval censoring）影响，且患者一旦活检阳性即退出研究（dependent dropout）。本文提出非参数核估计方法对 TPR/TNR 进行估计以处理区间删失与即时退出，并在此基础上构建加权分类框架来估计最优个体化 AS 策略，同时纳入成本-效益比。理论上，作者给出了所得 AS 策略的 uniform generalization error bound，覆盖 TPR 与 TNR 之间所有可能的权衡。模拟与前列腺癌队列数据应用验证了方法优势。对您而言，本文提供了一个将区间删失与 dependent dropout 纳入决策规则估计的流行病学应用案例。
- **关键技术**: `interval censoring`, `nonparametric kernel estimation`, `weighted classification framework`, `uniform generalization error bound`, `dependent dropout`, `cost-effectiveness analysis`
- **为什么对您有用**: 本文属于流行病学队列数据的应用因果/决策方法工作，直接涉及您 secondary interest 中 epidemiology 的 applied causal work 与数据集。从技术口子看，其 nonparametric kernel 估计与 uniform bound 的证明可尝试用您 very_familiar 的 minimax bounds 工具审视其收敛率是否紧；其 dependent dropout 结构与区间删失设定，可用 moderately_familiar 的 semiparametric theory 探索是否可构造 efficient influence function 以提升估计效率。Follow-up 判断：中期可做——需先在 moderately_familiar 的 semiparametric theory 上长肌肉，具体是推导此区间删失下 TPR/TNR 的 semiparametric efficiency bound，再考虑 debiased 改进。

### 9. [10.1093/biomtc/ujaf037](https://doi.org/10.1093/biomtc/ujaf037) — Vine copula mixed models for meta-analysis of diagnostic accuracy studies without a gold standard
- **作者**: Aristidis K Nikoloulopoulos
- **期刊/来源**: Biometrics
- **机构**: University of East Anglia
- **分类**: vol 81 · issue 2
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 在无完美金标准（imperfect reference standard）的诊断准确性荟萃分析设定下，目标是估计诊断试验的敏感度与特异度，关键假设是参考试验存在已知但非完美的误差结构。现有推荐方法为广义线性混合模型（GLMM），本文提出 vine copula mixed models 作为替代，允许随机效应服从任意单变量边际分布，并能刻画尾部依赖与不对称性，GLMM 仅为其特例。模拟与对宫颈新生物 Papanicolaou 试验数据的再分析表明，vine copula 模型在拟合与推断上可改进 GLMM。对您可能有用：若在流行病学队列中遇到无金标准的诊断偏倚问题，此模型提供了比 GLMM 更灵活的依赖结构刻画。
- **关键技术**: `vine copula mixed model`, `diagnostic accuracy meta-analysis`, `imperfect reference standard`, `tail dependence`, `generalized linear mixed model`
- **为什么对您有用**: 本文连接到流行病学因果推断中诊断试验偏倚的设定（无金标准下的 measurement error / misclassification）。武器库中的 semiparametric theory 与 M-estimation theory 可作为攻入此 paper 的口子——分析 vine copula 随机效应估计量的渐近性质与效率边界，当前 GLMM 的推断框架缺乏此层面的理论刻画。中期可做：需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以建立 copula 随机效应模型的一致性与渐近正态性。

## 其他  *(other, 2 篇)*

### 1. [10.1093/biomtc/ujaf077](https://doi.org/10.1093/biomtc/ujaf077) — COCA: a randomized Bayesian design integrating dose optimization and component contribution assessment for combination therapies
- **作者**: Xiaohan Chi, Ruitao Lin, Ying Yuan
- **期刊/来源**: Biometrics
- **机构**: The University of Texas MD Anderson Cancer Center
- **分类**: vol 81 · issue 2
- 相关性 2/10 · novelty: `application`
- **摘要**: 在癌症联合疗法早期试验设定下，目标是同时确定最优组合剂量（risk–benefit tradeoff）并评估各单药成分的贡献（component contribution）。本文提出两阶段随机化 II 期设计：第一阶段在多候选剂量中选最优组合，第二阶段启动多臂随机化评估各成分贡献。为提升试验效率与缩减样本量，两阶段疗效数据通过 spike-and-slab 先验的 Bayesian logistic regression 模型自适应合并。样本量与决策截断值由新校准程序系统确定以满足预设 operating characteristics；模拟显示该方法在达成双重目标的同时较竞争设计显著节省样本量。对您可能有用：该文虽属生物统计试验设计，但其 spike-and-slab 变量选择与 Bayesian adaptive combination 的思路可迁移至因果推断中多干预 arm 的 selection 与 sensitivity 分析。
- **关键技术**: `spike-and-slab prior`, `Bayesian logistic regression`, `adaptive data combination`, `risk-benefit tradeoff optimization`, `multi-arm randomized design`, `operating characteristics calibration`
- **为什么对您有用**: 本文核心是生物统计临床试验设计，与您 primary interest 的数学统计/高维/效率理论无直接交集。其 spike-and-slab 变量选择与 Bayesian adaptive pooling 的技术细节，在因果推断多处理 arm 的 selection 问题中有间接类比，但整体 novelty 偏应用设计而非理论推进。follow-up 判断：**暂不可做**——核心机器（Bayesian 临床试验设计、operating characteristics 校准）不在武器库中，且缺乏与您 very_familiar 的 minimax / U-stat / semiparametric efficiency 工具的直接接口。

### 2. [10.1093/biomtc/ujaf055](https://doi.org/10.1093/biomtc/ujaf055) — Continuous-space occupancy models
- **作者**: Wilson J Wright, Mevin B Hooten
- **期刊/来源**: Biometrics
- **机构**: Colorado State University · The University of Texas at Austin
- **分类**: vol 81 · issue 2
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文提出一类连续空间占用模型（continuous-space occupancy models），用于推断物种在大尺度空间上的分布同时修正检测不完全。现有方法无法处理连续空间上的物种发生过程与离散观测数据之间的空间支撑差异。作者将截断高斯过程（clipped Gaussian process）嵌入模型，刻画连续空间上的物种发生，从而能在更细分辨率上进行推断。模型采用贝叶斯方法拟合，并开发了高效MCMC算法：利用Vecchia近似实现空间高斯过程，设计替代数据（surrogate data）方法联合更新空间项和协方差参数。模拟和实例（新罕布什尔州的ovenbird数据）表明该模型相比已有空间占用模型具有更好的拟合与解释能力。对于统计计算方向，其MCMC加速策略（Vecchia近似和替代数据更新）值得借鉴；但本文主题与研究者核心兴趣方向距离较远，属于生态统计学入门阅读材料。
- **关键技术**: `clipped Gaussian process`, `change of spatial support`, `Vecchia approximation`, `surrogate data MCMC`, `spatial occupancy model`
- **为什么对您有用**: 本文属于生态统计应用，与研究者主要兴趣方向（因果推断、高维统计等）不直接关联。但其中使用的Vecchia近似和替代数据MCMC技术是高效空间统计计算的核心技巧，对统计计算领域的算法研究有参考价值。作为gateway阅读，本文清晰说明了连续空间模型与离散观测数据之间的支撑转换问题，但研究者当前武器库中缺乏空间统计背景，暂不可做直接扩展。若未来希望涉足空间因果推断或生态流行病学建模，本文是一个不错的入门点。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

