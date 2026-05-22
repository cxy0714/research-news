# Biometrics — Vol 81  Issue 2  ·  2026-05-21

- 共 38 篇 · Biometrics

## 因果推断  *(causal_inference, 14 篇)*

### 1. [10.1093/biomtc/ujaf071](https://doi.org/10.1093/biomtc/ujaf071) — Towards efficient and interpretable assumption-lean generalized linear modeling of continuous exposure effects
- **作者**: Stijn Vansteelandt
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文针对连续暴露的因果效应估计问题，在 modified treatment policies（shift interventions）框架下提出参数化不同 shift 幅度效应的模型，并发展 assumption-lean 估计策略。作者发现标准 debiased ML 在某些数据生成机制下表现不稳定，由此提出两项创新：一是更广泛适用的 debiasing procedure，显著改善有限样本性质；二是针对具有更优 semiparametric efficiency bound 的 estimand 构造 debiased ML 估计量，尽管模型误设时解释更微妙。与现有 projection estimator 不同，该方法避免逆暴露密度加权（无需估计倾向得分密度），也不需为处理 positivity 违反而定制 shift 方案。模拟与孟加拉 Wash Benefits 数据再分析验证了方法的有效性与稳定性。对您有用：本文将 debiased ML 与 efficiency bound 理论系统性地应用于连续暴露因果推断，其 debiasing 技巧和效率最优 estimand 的构造思路可直接迁移到您关注的 proximal CI 或纵向因果推断中的连续处理设定。
- **关键技术**: `debiased machine learning`, `modified treatment policies`, `shift interventions`, `semiparametric efficiency bound`, `assumption-lean estimation`, `projection estimator without inverse density weighting`
- **为什么对您有用**: 直接推进连续暴露因果推断中的 debiased ML 与效率理论，其 debiasing procedure 改进和更优效率界 estimand 构造思路可迁移至您关注的 proximal CI 及纵向因果推断中的连续处理场景。

### 2. [10.1093/biomtc/ujaf054](https://doi.org/10.1093/biomtc/ujaf054) — Double robust variance estimation with parametric working models
- **作者**: Bonnie E Shook-Sa, Paul N Zivich, Chanhwa Lee, Keyi Xue, Rachael K Ross, Jessie K Edwards et al.
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 9/10 · novelty: `new_theory`
- **摘要**: 在非随机化暴露下，ATE的双重稳健（DR）估计量常采用基于影响函数（IF）的方差估计，但该方差仅在结果与暴露模型均正确设定时一致。本文证明，在参数工作模型下，经验三明治方差估计量与非参数Bootstrap方差估计量同样具有双重稳健性。即仅需一个工作模型正确，它们即可提供有效的方差估计及名义置信区间覆盖率。核心机制在于IF方差包含因模型误判产生的非中心项而失效，而经验三明治与Bootstrap避开了该问题。模拟表明仅一个模型正确时，经验三明治与Bootstrap覆盖率接近名义水平，IF方差严重失真；实证应用于IPOP研究（HIV孕妇贫血对出生体重的影响）。对您有用：该文澄清了DR估计中方差估计的稳健性条件，直接关联因果推断与效率理论（影响函数、三明治方差）的兴趣，提示构造DR置信区间时应优先选用经验三明治或Bootstrap。
- **关键技术**: `doubly robust estimation`, `influence function based variance`, `empirical sandwich variance`, `nonparametric bootstrap`, `parametric working models`
- **为什么对您有用**: 直接关联因果推断的双重稳健估计与效率理论（影响函数 vs 经验三明治方差），澄清了方差估计稳健性的理论细节，对您在 DR/TMLE 估计中的方差构造与推断有直接指导意义。

### 3. [10.1093/biomtc/ujaf062](https://doi.org/10.1093/biomtc/ujaf062) — Continuous-time mediation analysis for repeatedly measured mediators and outcomes
- **作者**: Kateline Le Bourdonnec, Linda Valeri, Cécile Proust-Lima
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在纵向因果中介分析中，传统方法将时间离散化，本文针对暴露 $X$ 固定、中介过程 $\mathcal{M}_t$ 与结局过程 $\mathcal{Y}_t$ 在连续时间上不规则测量的设定，研究存在时依混杂 $\mathcal{L}_t$ 时的因果机制。定义了自然效应与路径特定效应两类因果 estimand，并给出了连续时间框架下的可识别性假设。估计方法采用基于微分方程的多变量混合模型，以参数化方式刻画连续时间下的轨迹演变与中介过程。模拟研究评估了有限样本表现，并在 3C 脑老化研究的两个实证中应用了该方法。实证揭示了教育水平通过抑郁与认知对功能依赖的中介路径，以及遗传因素通过血管性脑损伤影响认知的机制。对您有用：本文直接推进了您关注的 longitudinal mediation 方向，其基于微分方程混合模型的连续时间参数化方法对处理不规则纵向数据具有参考价值，同时提供了流行病学队列的真实数据集范例。
- **关键技术**: `longitudinal mediation analysis`, `path-specific effects`, `continuous-time multivariate mixed model`, `differential equations`, `time-dependent confounding`
- **为什么对您有用**: 直接推进您 primary interest 中的 longitudinal mediation 方向，且提供了 secondary interest 中流行病学（痴呆队列）的真实数据与因果分析范例；基于微分方程的连续时间混合模型对处理不规则纵向数据有方法学启发。

### 4. [10.1093/biomtc/ujaf066](https://doi.org/10.1093/biomtc/ujaf066) — Nonparametric assessment of regimen response curve estimators
- **作者**: Cuong T Pham, Benjamin R Baer, Ashkan Ertefaie
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在动态边际结构模型（dynamic MSM）框架下，regimen-response curve 描述平均结局与决策规则参数之间的函数关系，错误设定会导致最优治疗规则的因果估计有偏。本文以反事实风险（counterfactual risk）为目标参数，提出非参数 goodness-of-fit 方法来评估和比较 regimen-response curve 的工作模型。作者推导了逆概率加权（IPW）估计量和 canonical gradient（有效影响函数）将反事实风险映射到观测数据，并给出了固定与数据依赖目标参数下风险估计量的渐近性质。关键理论结果：当权重函数通过 sieve 估计时，IPW 估计量可以达到有效且渐近线性。实证部分在帕金森病 LS1 研究上估计 regimen-response curve。对您有用：该工作将 semiparametric efficiency theory（canonical gradient）与纵向因果推断中的 MSM 设定检验结合，sieve-IPW 达到有效性的证明思路可迁移到您关注的 proximal/longitudinal CI 中 nuisance function 估计的效率分析。
- **关键技术**: `inverse probability weighting`, `canonical gradient / efficient influence function`, `sieve estimation`, `dynamic marginal structural models`, `counterfactual risk`, `data-dependent target parameter`
- **为什么对您有用**: 直接连接您 primary interest 中的纵向因果推断（dynamic MSM）与 semiparametric efficiency theory（canonical gradient 推导、sieve-IPW 效率证明），设定检验的框架也可迁移到 proximal CI 中 working model 的诊断。

### 5. [10.1093/biomtc/ujaf047](https://doi.org/10.1093/biomtc/ujaf047) — Doubly robust omnibus sensitivity analysis of externally controlled trials with intercurrent events
- **作者**: Chenyin Gao, Xiang Zhang, Shu Yang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在外部对照试验（externally controlled trials）设定下，目标是在基线不可比性、结果均值非交换性（outcome mean non-exchangeability）及中间事件（intercurrent events）并存时识别并估计处理效应，关键假设包括条件可交换性与中间事件的因果结构假设。作者建立半参数框架，构造了双重稳健（doubly robust）且局部最优的估计量用于主分析和敏感性分析。核心创新是提出 omnibus sensitivity analysis，同时量化结果均值非交换性与中间事件对处理效应的联合影响，在指定敏感性参数下保持 n^{-1/2} 一致性与渐近正态性。技术工具涉及 efficient influence function 构造、DR 估计、以及针对两类假设违反的联合敏感性参数化。模拟与真实数据验证了方法表现。对您有用：该工作将敏感性分析从单一假设违反扩展到多源违反的联合框架，DR + 局部最优的性质直接关联您对 semiparametric efficiency 与 causal sensitivity analysis 的兴趣。
- **关键技术**: `doubly robust estimation`, `efficient influence function`, `omnibus sensitivity analysis`, `semiparametric framework`, `external control arm`, `intercurrent events`
- **为什么对您有用**: 直接推进 causal inference 中 sensitivity analysis 的理论：从单一假设违反到多源违反的联合框架，且 DR + 局部最优估计量涉及您关注的 semiparametric efficiency bound 与 influence function 技术，方法可迁移至其他非随机化因果推断场景。

### 6. [10.1093/biomtc/ujaf041](https://doi.org/10.1093/biomtc/ujaf041) — Optimal dynamic treatment regime estimation in the presence of nonadherence
- **作者**: Dylan Spicker, Michael P Wallace, Grace Y Yi
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在纵向因果推断的动态治疗策略（DTR）设定下，本文研究当存在非依从性（nonadherence，即分配处理与实际接受处理不一致）时最优 DTR 的估计问题。作者首先证明忽略非依从性会导致估计出次优策略，随后提出一种新的估计方法将非依从机制纳入考量。所提估计量具有双稳健（double robustness）性质，即在处理模型或依从机制模型之一正确指定时仍保持一致，且具备 $n^{-1/2}$-CAN（一致且渐近正态）的收敛性质。模拟表明，调整非依从性的新方法在策略最优性上可媲美基于无依从性理想数据的估计。该文将非依从性（类似 IV 设定中的分配与接受）引入纵向 DTR，其双稳健与 CAN 理论直接契合您对 longitudinal causal inference 与 efficiency theory 的兴趣。
- **关键技术**: `dynamic treatment regimes`, `nonadherence adjustment`, `double robustness`, `asymptotically normal estimation`, `longitudinal causal inference`
- **为什么对您有用**: 直接关联您 primary interest 中的 longitudinal causal inference 与 efficiency theory：非依从性设定类似 IV（分配 vs 实际处理），其双稳健与 CAN 估计量的推导对 DTR 下的半参数效率理论有直接参考价值。

### 7. [10.1093/biomtc/ujaf076](https://doi.org/10.1093/biomtc/ujaf076) — Regularized principal spline functions to mitigate spatial confounding
- **作者**: Carlo Zaccardi, Pasquale Valentini, Luigi Ippoliti, Alexandra M Schmidt
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究空间设计中未测量混杂导致的空间混杂问题，目标是在暴露与结局的半参数模型中消除混杂偏倚。作者首先揭示了非空间模型与包含基矩阵的半参数模型之间混杂偏倚的理论关系，证明半参数方法仅在特定条件下（依赖暴露与混杂的空间结构、基展开类型及正则化机制）才能减少偏倚。为此，提出一种贝叶斯半参数回归模型，利用主样条基函数展开矩阵逼近未观测混杂因子，并对展开系数施加 spike-and-slab 先验以实现基函数选择。模拟研究表明该方法较现有方法能更有效减少混杂偏倚，且对因果推断中常见的偏倚放大效应更具鲁棒性。该文将半参数基展开与因果混杂偏倚理论结合，为空间流行病学中的未测量混杂提供了新思路，契合您对因果推断（混杂/偏倚放大）与半参数理论的交叉兴趣。
- **关键技术**: `spatial confounding`, `semi-parametric regression`, `principal spline basis`, `spike-and-slab prior`, `bias amplification`, `basis expansion`
- **为什么对您有用**: 将半参数基展开与因果推断中的混杂偏倚/偏倚放大理论结合，为空间流行病学中的未测量混杂提供了新思路，契合您对因果推断（混杂/敏感性）与半参数理论的交叉兴趣。

### 8. [10.1093/biomtc/ujaf067](https://doi.org/10.1093/biomtc/ujaf067) — Estimating optimally tailored active surveillance strategy under interval censoring
- **作者**: Muxuan Liang, Yingqi Zhao, Daniel W Lin, Matthew Cooperberg, Yingye Zheng
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在癌症主动监测(AS)设定下，目标是基于生物标志物构建个体化活检决策规则以替代固定频率方案；关键挑战在于疾病进展状态受区间删失(interval censoring)，且阳性活检后患者立即退出导致非随机缺失。提出非参数核方法估计个体化AS策略的真阳性率(TPR)与真阴性率(TNR)，显式处理区间删失与即时退出；在此基础上构建加权分类框架估计最优AS策略，并纳入成本效益比进行决策优化。理论上给出所导出AS策略的一致泛化误差界，覆盖TPR与TNR之间所有可能的权衡。模拟与前列腺癌监测数据应用验证了方法优越性。该工作将动态治疗制度(DTR)思路扩展至区间删失下的监测策略优化，与您在因果推断中纵向/动态干预的兴趣相关，非参数核估计与泛化误差界的理论分析也可为半参数/非参数研究提供参考。
- **关键技术**: `nonparametric kernel estimation`, `interval censoring`, `weighted classification`, `dynamic treatment regime`, `uniform generalization error bound`, `cost-benefit optimization`
- **为什么对您有用**: 该文将DTR因果推断框架扩展至区间删失下的监测策略优化，与您在因果推断(longitudinal/dynamic intervention)的兴趣直接相关；非参数核估计与一致泛化误差界的理论工具也可为您的半参数/非参数理论研究提供方法借鉴。

### 9. [10.1093/biomtc/ujaf038](https://doi.org/10.1093/biomtc/ujaf038) — Estimating weighted quantile treatment effects with missing outcome data by double sampling
- **作者**: Shuo Sun, Sebastien Haneuse, Alexander W Levis, Catherine Lee, David E Arterburn, Heidi Fischer et al.
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在结局数据缺失非随机（MNAR）的设定下，本文研究因果加权分位数处理效应（WQTE）的识别与估计，利用双重抽样（double sampling）子样本获取缺失结局的真实值。借助双重抽样数据，作者提出了不需要原始数据缺失机制假设的识别条件，从而规避 MNAR 偏差。基于此，提出了一种逆概率加权（IPW）估计量，允许倾向得分和双重抽样概率被非参数或机器学习等方法估计。理论上推导了该估计量在特定分位点的逐点渐近性质，以及在 (0,1) 紧子集上的一致渐近性质，并开发了用于逐点和一致推断的自助法。实证部分将该方法应用于电子健康记录（EHR）数据，评估两种减肥手术对三年后 BMI 减少量的分布尾部效应。对您有用：该文处理 MNAR 结局的因果识别策略与一致推断理论，直接关联您关注的因果推断（MNAR 设定）与半非参理论（一致推断），且 EHR 数据集对流行病学应用有参考价值。
- **关键技术**: `weighted quantile treatment effects`, `missing not at random (MNAR)`, `double sampling`, `inverse-probability weighting (IPW)`, `uniform inference`, `bootstrap`
- **为什么对您有用**: 直接关联因果推断中的 MNAR 设定与半非参一致推断理论；同时其 EHR 流行病学应用与数据集对您的 secondary interest（流行病学应用因果）有直接参考价值。

### 10. [10.1093/biomtc/ujaf061](https://doi.org/10.1093/biomtc/ujaf061) — Learn-As-you-GO (LAGO) trials: optimizing treatments and preventing trial failure through ongoing learning
- **作者**: Ante Bing, Donna Spiegelman, Daniel Nevo, Judith J Lok
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究 LAGO（Learn-As-you-GO）试验：在试验进行中允许自适应调整干预方案时，如何保证因果效应估计与假设检验的有效性。设定为连续型结局下灵活条件均值模型（flexible conditional mean model），核心正则性条件涉及干预调整机制与结局模型的可识别性约束。方法上，作者推导了干预效应的 point/interval estimator，证明了在干预方案被中途修改时假设检验仍保持 valid type I error；进一步构造了最优干预方案（在达到预设均值下最小化成本）的 confidence set 以及所有干预组合下均值结局的 confidence bands。由于 binary outcome 下基于 logistic 模型的数学工具无法直接迁移到连续情形，理论推导完全重建。对您而言，该工作将 adaptive design 与 semiparametric 条件均值模型下的有效推断连接，可为 longitudinal causal inference 中 treatment adaptation 的 sensitivity 分析提供新思路。
- **关键技术**: `adaptive trial design`, `flexible conditional mean model`, `confidence set for optimal intervention`, `simultaneous confidence bands`, `valid inference under treatment adaptation`
- **为什么对您有用**: 与您 primary interest 中 causal inference (longitudinal, treatment adaptation) 及 semiparametric theory 相关；LAGO 框架下 flexible conditional mean model 的有效推断思路可迁移至 longitudinal causal setting 中处理方案随时间变化的 identification/estimation 问题。

### 11. [10.1093/biomtc/ujaf045](https://doi.org/10.1093/biomtc/ujaf045) — Addressing confounding and continuous exposure measurement error using corrected score functions
- **作者**: Brian D Richardson, Bryan S Blette, Peter B Gilbert, Michael G Hudgens
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在同时存在混杂和连续暴露变量经典加性测量误差的设定下，本文研究边际暴露效应的识别与估计问题。基于corrected score方法，作者提出了三种仅使用观测变量的估计器：g-formula、逆概率加权（IPW）和双重稳健（DR）估计器。理论上证明了这些估计器的一致性与渐近正态性（CAN），并验证了DR估计器在部分模型误指下的双重稳健性质。方法通过R包mismex实现，模拟研究展示了其在有限样本下对混杂与测量误差联合偏差的校正能力。实证分析应用于HVTN 505预防性疫苗试验，评估生物标志物对HIV-1感染的影响。对您有用：直接关联因果推断中混杂与测量误差同时处理的难题，其DR估计器的CAN性质与双重稳健性对您在效率理论与半参数因果推断方面的研究有直接参考价值，且提供了流行病学真实数据的应用范例。
- **关键技术**: `corrected score function`, `classical additive measurement error`, `doubly robust estimation`, `inverse probability weighting`, `g-formula`, `asymptotically normal`
- **为什么对您有用**: 直接关联因果推断中混杂与测量误差同时处理的难题，其DR估计器的CAN性质与双重稳健性对您在效率理论与半参数因果推断方面的研究有直接参考价值，且提供了流行病学（HIV疫苗试验）的真实数据应用范例。

### 12. [10.1093/biomtc/ujaf068](https://doi.org/10.1093/biomtc/ujaf068) — Variant specific treatment effects with applications in vaccine studies
- **作者**: Gellért Perényi, Mats Stensrud
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在存在多种病原体变异株的设定下，本文旨在识别和定义变异株特异性的因果处理效应，并显式考虑目标人群中的干扰（interference）问题。作者指出，即便随机试验中个体可视为独立，疫苗推广的目标人群中通常存在干扰。基于形式化因果推断框架，本文推导出了在干扰存在时，常用相对尺度疫苗效力参数仍可解释为明确定义因果效应的显式识别条件。此外，理论结果为在相对尺度而非绝对尺度上报告因果 estimand 提供了新的正当理由。实证部分通过大型 HIV-1 疫苗试验展示了如何区分疫苗对不同基因组序列病毒的效应。对您有用：本文在干扰假设下对变异株特异性 estimand 的 identification 推导，直接关联您对 causal inference 中 identification 与假设放松的兴趣，且 HIV 疫苗试验数据对流行病学因果推断应用有参考价值。
- **关键技术**: `causal identification under interference`, `variant-specific estimands`, `relative scale vaccine efficacy`, `target population interference`, `HIV-1 vaccine trial`
- **为什么对您有用**: 直接关联 causal inference 中的 identification 理论，特别是放松了无干扰假设下的 estimand 定义与识别；同时 HIV 疫苗试验的应用契合您对流行病学因果推断的兴趣。

### 13. [10.1093/biomtc/ujaf002](https://doi.org/10.1093/biomtc/ujaf002) — Data integration methods for micro-randomized trials
- **作者**: E Huch, I Nahum-Shani, L Potter, C Lam, D W Wetter, W Dempsey
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在微随机试验（MRT）的纵向因果推断设定下，目标是利用多个相似 MRT 的数据整合来估计因果游览效应，假设各试验干预相似但估计量间可能存在相关性。方法核心是推广多元精度加权以整合不同 MRT 的估计量，允许估计量间存在相关性，并证明所得元估计器具有渐近最优性。模拟与戒烟流行病学案例研究表明，该方法可降低标准误超 30% 且不牺牲渐近无偏性与推断校准。对您有用：该工作将精度加权与纵向因果推断结合，其渐近最优性证明和效率提升策略可直接迁移至您关注的 longitudinal causal inference 及 efficiency theory 子方向。
- **关键技术**: `micro-randomized trials`, `causal excursion effect`, `multivariate precision weighting`, `data integration`, `asymptotic optimality`
- **为什么对您有用**: 直接关联 primary interest 中的 longitudinal causal inference 与 efficiency theory，其推广的多元精度加权及渐近最优性证明为多源因果推断的效率界提供了新视角，且戒烟流行病学数据集对您的 secondary interest 有实证参考价值。

### 14. [10.1093/biomtc/ujaf044](https://doi.org/10.1093/biomtc/ujaf044) — Multiple bias calibration for valid statistical inference under nonignorable nonresponse
- **作者**: Seonghun Cho, Jae Kwang Kim, Yumou Qiu
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在非忽略缺失(nonignorable nonresponse)设定下，目标是对总体均值进行一致推断；关键假设是多个候选倾向得分(PS)模型中包含真实模型且其期望等于真实缺失率。提出multiple bias calibration方法：将多个working PS模型嵌入经验似然的内部偏差校准约束，从而消除选择偏差——只要候选集合包含真实PS模型，估计即一致，具有多重鲁棒性(multiple robustness)特征。研究了估计量的渐近性质（一致性、渐近正态性），并通过有限模拟与NHANES体脂数据实证分析对比现有方法。对您有用：经验似然+多working model的bias calibration思路可直接迁移到proximal CI或sensitivity analysis中处理模型误设的鲁棒性问题，同时该文在semiparametric框架下对nonignorable missing的identification策略值得借鉴。
- **关键技术**: `empirical likelihood`, `multiple bias calibration`, `nonignorable nonresponse`, `propensity score working models`, `multiple robustness`
- **为什么对您有用**: 直接关联causal inference中的missing data/selection bias问题；经验似然+多working PS模型的bias calibration为proximal CI和sensitivity analysis中模型误设鲁棒性提供了可迁移的思路。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 2 篇)*

### 1. [10.1093/biomtc/ujaf042](https://doi.org/10.1093/biomtc/ujaf042) — PDC-MAKES: a conditional screening method for controlling false discoveries in high-dimensional multi-response setting
- **作者**: Wei Xiong, Han Pan, Tong Shen
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在超高维多响应变量设定下，本文研究条件特征筛选中的 FDR 控制问题，目标 estimand 为与多响应向量条件相关的预测变量集。方法基于 partial distance correlation (PDC) 构建模型无关的条件筛选统计量，可在控制高维条件变量影响后度量预测变量与响应间的依赖，对重尾数据稳健且能识别边际无关但条件相关的预测变量。为控制 FDR，引入 derandomized knockoff-e-values 确定筛选阈值，相比传统 knockoff 更稳定。理论上在温和正则条件下证明了 sure screening property、FDR 控制及更高 power；PDC 的构造允许条件变量本身为高维向量，区别于现有条件独立性检验工作。该方法对您的高维统计与假设检验交叉研究有直接参考价值，特别是 knockoff-e-value 在多响应筛选中的 FDR 控制机制可迁移至其他高维 inference 场景。
- **关键技术**: `partial distance correlation`, `derandomized knockoff-e-values`, `sure screening property`, `FDR control`, `model-free conditional screening`, `multi-response ultrahigh-dimensional setting`
- **为什么对您有用**: 直接连接您的高维统计与假设检验两个 primary interest：PDC 提供了非参数条件依赖度量的新工具，knockoff-e-value 则为高维多重检验中的 FDR 控制提供了比传统 knockoff 更稳定的方案，可迁移至您关注的 semiparametric efficiency 或 debiased ML 场景中的变量筛选阶段。

### 2. [10.1093/biomtc/ujaf065](https://doi.org/10.1093/biomtc/ujaf065) — Probabilistic exponential family inverse regression and its applications
- **作者**: Daolin Pang, Ruoqing Zhu, Hongyu Zhao, Tao Wang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在高维回归与分类的充分降维设定下，针对现有方法难以处理离散型预测变量（如单细胞测序reads）的问题，本文提出概率指数族逆回归（PrEFIR）。PrEFIR 假设在给定响应与潜在因子条件下，预测变量服从单参数指数族分布，证明了低维降维空间不仅源于响应变量也源于潜在因子。进一步将模型扩展至双指数族以处理过度离散，并提出最大层次似然法进行估计，配合高度可并行化的计算算法。模拟与真实数据验证了方法有效性。该文处理高维离散数据的降维框架及可并行计算算法，对您在统计计算（算法设计）和高维统计（离散数据降维）方面的兴趣有直接参考价值。
- **关键技术**: `sufficient dimension reduction`, `exponential family inverse regression`, `latent factor model`, `double exponential family`, `maximum hierarchical likelihood`, `parallelizable algorithm`
- **为什么对您有用**: 涉及高维统计中的离散数据降维与潜在因子建模，其最大层次似然估计与可并行算法设计直接契合您在统计计算与高维统计方面的兴趣。

## 非参数 / 半参数  *(nonparam_semipara, 5 篇)*

### 1. [10.1093/biomtc/ujaf064](https://doi.org/10.1093/biomtc/ujaf064) — Semiparametric joint modeling for biomarker trajectory before disease onset
- **作者**: Yifei Sun, Xiwen Zhao, Kwun Chuen Gary Chan, Wanwan Xu, Heather Allore, Yize Zhao
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文在疾病发生前的生物标志物轨迹分析设定下，提出一个半参数联合模型，允许轨迹同时依赖自然时间尺度（如年龄）与距疾病发病时间，并处理了左截断偏差。估计方法采用 profile kernel estimating equation 来估计回归系数与未指定的基线均值轨迹函数。理论方面，建立了所提估计量的大样本性质（如 n^{-1/2} 收敛与渐近正态性）。实证应用于阿尔茨海默病临床前期的脑生物标志物轨迹，发现皮层厚度在发病前下降且 APOE4 携带者水平更低。该文对您有用，因为其 profile kernel estimating equation 与半参数联合模型的理论推导直接契合您的半参数理论兴趣，且阿尔茨海默病队列数据对您的流行病学应用方向有数据集参考价值。
- **关键技术**: `semiparametric joint model`, `profile kernel estimating equation`, `left-truncation bias correction`, `two time-scale trajectory`, `longitudinal-survival joint modeling`
- **为什么对您有用**: 直接契合您的半参数/非参数理论兴趣（profile kernel estimating equation 与大样本性质推导），同时阿尔茨海默病纵向队列数据对您的流行病学应用方向具有数据集参考价值。

### 2. [10.1093/biomtc/ujaf080](https://doi.org/10.1093/biomtc/ujaf080) — Leveraging two-phase data for improved prediction of survival outcomes with application to nasopharyngeal cancer
- **作者**: Eun Jeong Oh, Seungjun Ahn, Tristan Tham, Min Qian
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在两阶段抽样（two-phase design）生存数据设定下，核心 covariate（如 HPV 状态）在大部份样本中缺失，目标是利用全样本传统协变量与子样本完整信息提升生存预测精度。作者提出 expert-guided 方法：基于可观测协变量构建 prognostic index，并结合关键因子的临床重要性权重，对缺失协变量进行信息借补而非简单剔除。方法在 c-index、calibration slope 和 integrated Brier score 上通过模拟与 NPC 真实数据验证，一致优于仅用完整病例或简单插补的竞争方法。两阶段抽样是经典半参数效率问题，但本文侧重预测而非 identification / efficiency bound 推导，理论深度有限。对您而言，两阶段设计的效率利用思路可迁移至 semiparametric efficiency 与 epidemiology 应用场景，NPC 数据集也可作为因果/缺失数据方法的真实数据测试平台。
- **关键技术**: `two-phase sampling design`, `prognostic index`, `survival prediction with missing covariates`, `expert-guided imputation`, `concordance index evaluation`
- **为什么对您有用**: 两阶段抽样设计与 semiparametric efficiency theory（primary）直接相关，NPC 真实数据集对 epidemiology 应用（secondary）有数据集价值；但本文偏预测应用，理论贡献较浅，主要收益在于了解两阶段缺失协变量处理的工程思路和获取可用数据集。

### 3. [10.1093/biomtc/ujaf063](https://doi.org/10.1093/biomtc/ujaf063) — Conformal predictive intervals in survival analysis: a resampling approach
- **作者**: Jing Qin, Jin Piao, Jing Ning, Yu Shen
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在一般右删失生存数据（删失时间在发生失败时不可观测）设定下，目标是构建分布无关的保形预测区间（conformal predictive intervals）。针对 Candès 等人仅适用于 I 型删失且只能估计下界的方法，本文提出基于 Bootstrap 的重抽样方法，在多种工作回归模型下构建单侧与双侧保形预测区间。核心机制是通过 Bootstrap 重抽样弥补一般右删失结构中缺失的删失时间信息，并在保形框架下实现有限样本覆盖保证。理论性质上，该方法在工作回归模型误判时仍保持覆盖率的稳健性，模拟显示在中等删失比例下双侧区间覆盖率良好。实证应用于乳腺癌患者生存时间预测。对您有用：将 conformal prediction 拓展至一般右删失数据的思路，为流行病学队列研究中的分布无关稳健推断提供了新工具，且 Bootstrap 处理缺失删失时间的技巧对统计计算与半参数推断有参考价值。
- **关键技术**: `conformal prediction`, `bootstrap resampling`, `right-censored survival data`, `distribution-free inference`, `covariate shift`
- **为什么对您有用**: 将非参数保形预测拓展至一般右删失数据，为流行病学队列研究中的生存推断提供分布无关工具，Bootstrap 处理缺失删失时间的技巧对统计计算与半参数理论有参考价值。

### 4. [10.1093/biomtc/ujaf051](https://doi.org/10.1093/biomtc/ujaf051) — Distance weighted directional regression for Fréchet sufficient dimension reduction
- **作者**: Chao Ying, Zhou Yu, Xin Zhang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究非欧几里得响应变量与多维预测变量之间的 Fréchet 充分降维（SDR）问题，目标是在保持依赖结构的同时降低预测变量维度。作者提出了基于距离加权的方向回归方法，通过重新表述经典方向回归，统一了欧几里得与非欧几里得响应的线性 SDR，并将其扩展至非线性 Fréchet SDR。理论方面，对线性 Fréchet 方向回归估计量推导了渐近正态性，并对非线性估计量给出了收敛速率。模拟与实证分析基于人类死亡率与糖尿病患病率数据，验证了方法在解释性与样本外预测上的提升。对您有用：该文在非欧空间下推导了 SDR 估计量的渐近正态性与收敛速率，对您在半参数/非参数理论及流行病学数据应用方向有直接参考价值。
- **关键技术**: `Fréchet sufficient dimension reduction`, `distance weighted directional regression`, `asymptotic normality`, `nonlinear SDR`, `non-Euclidean data`
- **为什么对您有用**: 将经典 SDR 推广至非欧空间的半参数/非参数理论推导（渐近正态性与收敛速率），且应用了流行病学相关的死亡率与糖尿病数据集，对您在非参数理论及流行病学应用方向有参考价值。

### 5. [10.1093/biomtc/ujaf072](https://doi.org/10.1093/biomtc/ujaf072) — Non-parametric estimators of hazard ratios for comparing two survival curves
- **作者**: Mihai Giurcanu, Theodore Karrison
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在右删失生存数据设定下，基于组别特异累积风险函数的估计方程，提出比较两条生存曲线的风险比的非参数估计量。首先在常数风险比假设下推导估计量及其渐近正态性；随后将方法扩展至时间依赖且局部近似为常数的风险比，并提出变点选择方法。进一步构建分层估计量，提出跨层常数与时变风险比的异质性检验。模拟结果显示，在比例风险假设可能违背时，所提非参数估计量相比 Cox 偏最大似然估计在效率与覆盖率上更具稳健性。对您有用：该工作展示了如何绕开 Cox 模型直接用估计方程构建纯非参数风险比估计量并推导其渐近性质，对您在非参数/半参数理论及流行病学应用中的生存分析有直接参考价值。
- **关键技术**: `estimating equations`, `cumulative hazard function`, `asymptotic normality`, `change point selection`, `stratified heterogeneity test`
- **为什么对您有用**: 直接关联您的非参数/半参数理论兴趣（估计方程构建与渐近性质推导），同时风险比估计是流行病学因果推断与生存分析的核心工具，其在 PH 假设违背时的稳健性对应用有实际价值。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1093/biomtc/ujaf060](https://doi.org/10.1093/biomtc/ujaf060) — Robust and efficient semi-supervised learning for Ising model
- **作者**: Daiqing Wu, Molei Liu
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在电子病历(EHR)标签稀缺而辅助特征充足的半监督设定下，本文研究 Ising 模型交互参数的高效推断。方法核心是将监督估计量的 score function 投影到辅助 EHR 特征空间，利用无标签样本实现方差缩减且不引入偏差。针对条件模型误设可能导致的效率损失，提出 intrinsic efficient update 与 ensemble 策略，本质上是在逼近半监督效率边界。理论上证明了估计量的渐近正态性与方差缩减性质，模拟与 MIMIC-III ICU 数据分析显示其优于现有 SSL 方法。对您有用：score projection 与 intrinsic efficient update 直接关联您关注的 semiparametric efficiency bound 与 debiased ML 思想，且 EHR 流行病学应用提供了可迁移的分析范式。
- **关键技术**: `semi-supervised learning`, `score projection`, `intrinsic efficient update`, `Ising model`, `semiparametric efficiency bound`
- **为什么对您有用**: 直接关联您关注的 efficiency theory（semiparametric efficiency bound 与 variance reduction via projection），其 intrinsic efficient update 机制与 debiased ML 中的 orthogonal score 思想高度一致；同时 MIMIC-III 的流行病学应用具有数据集价值。

## 数理统计 / 假设检验  *(hypothesis_testing, 5 篇)*

### 1. [10.1093/biomtc/ujaf050](https://doi.org/10.1093/biomtc/ujaf050) — A semiparametric quantile regression rank score test for zero-inflated data
- **作者**: Zirui Wang, Wodan Ling, Tianying Wang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在零膨胀数据设定下，目标是检验零膨胀响应变量与协变量之间的关联，传统 ZIP/ZINB 模型依赖强参数假设（Poisson/Negative Binomial 分布族）可能失效。本文提出 ZIQ-SIR（zero-inflated quantile single-index rank-score test），将分位数回归、单指标模型与 rank-score 检验统计量结合，在半参数框架下同时处理零膨胀结构与非线性协变量效应，避免参数分布假设。方法的核心是构造针对零膨胀分位数单指标模型的 rank-score 检验统计量，在半参数正则条件下证明 Type I error 渐近控制。模拟显示 ZIQ-SIR 在 Type I error 控制和检验功效上均优于现有参数与半参数方法。应用于哥伦比亚肠道微生物组丰度数据，识别出更多显著关联。对您有用：该工作同时触及假设检验与半参数理论两个 primary interest，rank-score 检验在零膨胀/过度分散设定下的构造思路可迁移至其他半参数检验问题。
- **关键技术**: `rank-score test`, `quantile regression`, `single-index model`, `zero-inflated semiparametric model`, `asymptotic Type I error control`
- **为什么对您有用**: 直接连接假设检验与半参数理论两个 primary interest；rank-score 检验在零膨胀设定下的半参数构造思路可迁移至其他复杂分布假设下的检验问题，微生物组数据集对流行病学 secondary interest 也有参考价值。

### 2. [10.1093/biomtc/ujaf035](https://doi.org/10.1093/biomtc/ujaf035) — Inference with approximate local false discovery rates
- **作者**: Rajesh Karmakar, Ruth Heller, Saharon Rosset
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 在大规模多重检验的 Efron 2-group 模型下，研究相依检验统计量下的局部错误发现率（locFDR）推断问题。传统边际 locFDR 忽略依赖性导致功效损失，而全局条件 locFDR 的计算复杂度随假设数量指数增长，不可行。本文提出 locFDR_N，即给定其 N-邻域检验统计量下原假设为真的条件概率。作者证明了在仅依赖 N-邻域信息的决策类中，基于 locFDR_N 阈值的拒绝程序是最优的，且功效随 N 单调递增。模拟显示即使 N 很小，该方法也比现有实用方法有显著功效提升，并在身高 GWAS 数据中验证了实用性。对您有用：该工作将多重检验的 optimality 与计算可行性结合，直接推进您关注的 hypothesis testing 理论，其邻域条件概率的近似思路对高维相依结构下的统计计算也有启发。
- **关键技术**: `local false discovery rate`, `multiple testing optimality`, `2-group model`, `neighborhood conditioning`, `FDR control`
- **为什么对您有用**: 直接推进您 primary interest 中的 mathematical statistics (hypothesis testing) 方向，将最优性理论与计算可行性结合；GWAS 应用也契合您 epidemiology 的 secondary interest。

### 3. [10.1093/biomtc/ujaf073](https://doi.org/10.1093/biomtc/ujaf073) — Design of platform trials with a change in the control treatment arm
- **作者**: Peter Greenstreet, Thomas Jaki, Alun Bedding, Pavel Mozgunov
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 本文研究平台试验（platform trials）中对照组发生更替（即更优疗法成为新对照）时的设计问题，关注在频繁多臂多阶段（MAMS）设定下是否保留更替前的历史数据。作者通过解析推导和数值模拟证明，保留对照组更替前的信息可能对整体检验效能（overall power）和条件检验效能（conditional power）产生不利影响，即降低发现最优疗法或特定疗法优于当前对照的概率。同时，保留信息也会降低条件I类错误率（conditional type I error），即错误拒绝当前对照的概率。理论结果揭示了在连续平台试验与重新启动试验之间的权衡，为动态对照下的试验设计提供了决策依据。对您可能有用：虽然侧重临床试验设计，但其对动态干预下假设检验错误率与效能的解析分析，可为您的“假设检验”兴趣提供在自适应实验设定下的具体案例与理论参考。
- **关键技术**: `multi-arm multi-stage (MAMS) trials`, `conditional type I error`, `overall and conditional power`, `frequentist hypothesis testing`, `adaptive platform design`
- **为什么对您有用**: 核心是对动态对照更替下假设检验的I类错误与效能进行解析推导，直接关联您在“假设检验”方向的兴趣，展示了自适应实验设定下频率派性质的严谨分析。

### 4. [10.1093/biomtc/ujaf036](https://doi.org/10.1093/biomtc/ujaf036) — Statistical inference on the relative risk following covariate-adaptive randomization
- **作者**: Fengyu Zhao, Yang Liu, Feifang Hu
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文在协变量适应性随机化（CAR）实验设定下，研究相对风险（RR）的协变量调整估计及其假设检验的渐近性质。作者推导了广泛一类 CAR 程序下该估计量的理论性质，发现传统方差估计因忽略随机化导致的组内相关性而使检验过于保守（Type I error 低于名义水平）。为修正此问题，文章提出了基于模型和模型稳健两种标准误调整方法，以恢复正确的检验水平。理论证明与数值模拟均验证了调整后检验的有效性及优良有限样本性质。对您而言，该文展示了 CAR 设计下方差结构非标准导致检验保守的数学机制，直接关联您对假设检验与因果推断的兴趣，且 RR 是流行病学核心指标，方法可迁移至流行病学队列研究应用。
- **关键技术**: `covariate-adaptive randomization`, `relative risk estimation`, `model-robust standard error`, `conservative test correction`, `asymptotic variance derivation`
- **为什么对您有用**: 直接关联您对“假设检验”与“因果推断”的兴趣，展示了 CAR 设计下非标准方差结构导致检验保守的数学机制；同时相对风险是流行病学核心指标，其稳健标准误调整方法可迁移至流行病学应用。

### 5. [10.1093/biomtc/ujaf069](https://doi.org/10.1093/biomtc/ujaf069) — On the finite-sample and asymptotic error control of a randomization-probability test for response-adaptive clinical trials
- **作者**: Nina Deliu, Sofia S Villar
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在响应自适应随机化临床试验中，如何在保持期望结局最优性的同时保证频率学派I类错误控制是核心难题；本文提出基于随机化概率的新检验统计量，并在一般自适应设计下推导其有限样本与渐近误差保证。核心构造将检验统计量定义在分配机制的随机化概率上而非结局变量本身，从而在数据依赖分配下仍可获得有限样本I类错误控制——这突破了传统自适应推断仅依赖大样本渐近保证的局限。对Thompson采样这一贝叶斯响应自适应设计，作者具体刻画了所提检验的渐近性质与功效效率，证明其可同时保持期望结局最优性。实证部分通过一个II期肿瘤试验和模拟实验验证了方法的有效性。对您有用：该工作在假设检验方向提供了有限样本误差控制的新理论结果，且随机化概率检验统计量的构造思路可迁移至因果推断中自适应实验（如bandit-based RCT）的推断问题。
- **关键技术**: `randomization-probability test statistic`, `finite-sample type-I error control`, `Thompson sampling`, `response-adaptive randomization`, `asymptotic power efficiency`
- **为什么对您有用**: 直接关联您primary interest中的hypothesis testing——提供了自适应设计下有限样本I类错误控制的新理论；随机化概率检验统计量的构造思路也可迁移至因果推断中自适应实验的推断问题。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1093/biomtc/ujaf053](https://doi.org/10.1093/biomtc/ujaf053) — Bayesian covariate-dependent graph learning with a dual group spike-and-slab prior
- **作者**: Zijian Zeng, Meng Li, Marina Vannucci
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究协变量依赖的图学习问题，目标参数为精度矩阵随协变量变化的 3D 数组，在 node-level 和 covariate-level 双重分组结构下同时实现多层级与个体级稀疏选择。提出 dual group spike-and-slab prior，通过嵌套策略分别处理节点方向与协变量方向的分组选择挑战，实现 covariate-level、node-level 和 local-level 三层稀疏。计算方面开发了全 Gibbs sampler，避免了高维图模型中常见的调参困难，提升了 routine implementation 的可行性。模拟显示图恢复精度优于现有方法；微生物组数据应用展示了微生物互作及协变量效应的可解释性。对您而言，该工作的嵌套分组 spike-and-slab 结构与 Gibbs 采样方案可为高维结构稀疏问题中的贝叶斯计算提供思路，但与您核心的 RMT / semiparametric efficiency 方向距离较远。
- **关键技术**: `dual group spike-and-slab prior`, `covariate-dependent graphical model`, `multi-level structured sparsity`, `full Gibbs sampler`, `precision matrix estimation`
- **为什么对您有用**: 与您的高维统计和统计计算兴趣有方法学重叠——嵌套分组先验的结构化稀疏思路和免调参 Gibbs 采样方案可迁移至其他高维结构选择问题，但未涉及 RMT 或 semiparametric efficiency 核心理论。

### 2. [10.1093/biomtc/ujaf055](https://doi.org/10.1093/biomtc/ujaf055) — Continuous-space occupancy models
- **作者**: Wilson J Wright, Mevin B Hooten
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文在生态 occupancy model 框架下，解决观测数据离散空间支撑与物种发生过程连续空间支撑之间的 mismatch 问题，目标 estimand 为连续空间上的物种发生概率。核心方法是用 clipped Gaussian process 建模连续空间上的二元发生过程，从而允许在比观测分辨率更细的格点上做推断，并能刻画样地内部分发生与检测概率的关联。计算方面，采用 Vecchia 近似加速空间 GP 的似然计算，并发展 surrogate data 方法实现空间项与协方差参数的联合 MCMC 更新。模拟与 New Hampshire ovenbird 数据分析表明方法优于传统离散空间 occupancy model。对您而言，Vecchia 近似与 surrogate data MCMC 的计算方案可迁移至其他大规模空间 GP 推断场景，属于统计计算兴趣的边缘相关。
- **关键技术**: `clipped Gaussian process`, `Vecchia approximation`, `surrogate data MCMC`, `change of spatial support`, `spatial occupancy model`
- **为什么对您有用**: Vecchia 近似与 surrogate data 联合更新方案属于统计计算方向，可迁移至其他大规模空间 GP 推断问题；但整体偏生态应用，与您核心兴趣（causal inference / efficiency / RMT）距离较远。

## 流行病学  *(epidemiology, 6 篇)*

### 1. [10.1093/biomtc/ujaf037](https://doi.org/10.1093/biomtc/ujaf037) — Vine copula mixed models for meta-analysis of diagnostic accuracy studies without a gold standard
- **作者**: Aristidis K Nikoloulopoulos
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在无金标准参考试验的诊断准确性 Meta 分析设定下，现有推荐方法为 GLMM（广义线性混合模型），但其随机效应联合分布默认正态且无法捕捉尾部相依与不对称性。本文提出 vine copula mixed model，将 GLMM 嵌套为特例，允许随机效应取任意边缘分布，并通过 vine copula 结构灵活建模灵敏度与特异度之间的相依模式（含尾部相依与不对称）。模拟与实例（Papanicolaou 涂片诊断宫颈上皮内瘤变）表明，vine copula 随机效应模型在拟合与推断上可改进 GLMM。对您而言，该文展示了 copula 方法在流行病学诊断准确性研究中的半参数化建模思路，vine copula 的灵活相依结构可迁移至其他需放松联合分布假设的因果或半参数推断场景。
- **关键技术**: `vine copula mixed model`, `generalized linear mixed model`, `diagnostic accuracy meta-analysis`, `imperfect reference standard`, `tail dependence`, `copula random effects`
- **为什么对您有用**: 连接您 secondary interest 中的流行病学诊断准确性应用；vine copula 对随机效应联合分布的半参数化放松思路，可迁移至您 primary interest 中半参数理论里需放松多元隐变量分布假设的场景。

### 2. [10.1093/biomtc/ujaf046](https://doi.org/10.1093/biomtc/ujaf046) — Uncovering mortality patterns and hospital effects in COVID-19 heart failure patients: a novel multilevel logistic cluster-weighted modeling approach
- **作者**: Luca Caldera, Chiara Masci, Andrea Cappozzo, Marco Forlani, Barbara Antonelli, Olivia Leoni et al.
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 3/10 · novelty: `application`
- **摘要**: 在 COVID-19 期间意大利伦巴第地区心衰患者的医疗设定下，目标是预测住院后 45 天死亡率并刻画医院效应，采用多水平逻辑聚类加权模型（multilevel logistic cluster-weighted model）处理患者亚组异质性。方法将多水平逻辑回归与有限混合模型结合，以灵活刻画连续与二值变量的依赖结构及不同属性亚组的组特异性效应。参数估计采用定制的分类期望最大化（CEM）算法，并通过广泛模拟研究与竞争模型对比评估性能。实证分析基于伦巴第地区行政数据，对患者进行画像并调查医院水平对整体死亡率的影响。场景分析表明该方法能有效管理多重异质性来源，辅助医疗提供者与政策制定者识别患者特异性治疗路径。对您而言，该文提供了 COVID-19 心衰的流行病学真实数据集及多水平异质性建模案例，但缺乏您主要关注的因果推断或半参数效率理论深度。
- **关键技术**: `multilevel logistic regression`, `cluster-weighted model`, `finite mixture model`, `classification EM algorithm`, `hospital profiling`
- **为什么对您有用**: 提供了意大利 COVID-19 心衰的流行病学真实数据集和多水平异质性建模的实证案例，但方法学上偏向参数混合模型与 EM 算法，缺乏您关注的因果推断或半参数效率理论深度。

### 3. [10.1093/biomtc/ujaf074](https://doi.org/10.1093/biomtc/ujaf074) — Power calculation for cross-sectional stepped wedge cluster randomized trials with a time-to-event endpoint
- **作者**: Mary Ryan Baumann, Denise Esserman, Monica Taljaard, Fan Li
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在横断面阶梯楔形集群随机试验（SW-CRT）设定下，研究具有删失生存结局的统计检验功效计算问题，假设常数期内与期间相关参数。提出分层边际 Cox 模型进行分析，并推导了稳健三明治方差的显式表达式以避免计算密集的模拟。基于 Wald 和稳健得分检验推导了功效公式，并通过有限样本模拟验证其表现。实证以评估电子提醒系统对导管拔除时间的 SW-CRT 为例，并提供了 R Shiny 应用。对您可能有用：虽然理论深度偏向标准生物统计，但其对 SW-CRT 生存数据的功效计算框架和稳健方差推导，可为流行病学纵向干预研究的因果推断设计提供参考。
- **关键技术**: `stepped wedge cluster randomized trial`, `stratified marginal Cox model`, `robust sandwich variance`, `power calculation`, `Wald and score tests`
- **为什么对您有用**: 涉及假设检验（功效计算）与流行病学应用（SW-CRT干预研究），其稳健方差推导和试验设计框架对您在流行病学纵向因果推断或干预研究中的应用有参考价值，但理论深度相对常规。

### 4. [10.1093/biomtc/ujaf040](https://doi.org/10.1093/biomtc/ujaf040) — Discrete-time competing-risks regression with or without penalization
- **作者**: Tomer Meir, Malka Gorfine
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究离散时间竞争风险生存数据的回归估计问题，设定包含右删失与多种竞争事件。提出一种新的离散时间竞争风险估计程序，其核心优势在于能够无缝整合常用的正则化回归（如 Lasso/Ridge）与特征筛选方法，克服了现有连续时间方法在离散数据下难以直接正则化的局限。方法基于离散风险模型构造，支持高维协变量下的变量选择与参数估计，并提供了 Python 软件包 PyDTS 实现该算法及附加功能。模拟研究与 ICU 住院时长（含出院、转院、死亡三种竞争事件）的真实数据分析表明，该方法在离散竞争风险设定下结合惩罚回归具有良好的表现。对您而言，该工作在流行病学队列的竞争风险建模上有直接应用价值，且 PyDTS 包为您在统计计算与算法实现方面提供了可迁移的工具资源。
- **关键技术**: `discrete-time survival analysis`, `competing risks regression`, `regularized regression`, `feature screening`, `right censoring`
- **为什么对您有用**: 提供了流行病学（ICU 竞争风险）数据集与建模框架，且其 Python 包 PyDTS 对您的统计计算与算法兴趣有直接工具价值，方法可迁移至纵向/因果生存分析。

### 5. [10.1093/biomtc/ujaf052](https://doi.org/10.1093/biomtc/ujaf052) — A Bayesian joint longitudinal-survival model with a latent stochastic process for intensive longitudinal data
- **作者**: Madeline R Abbott, Walter H Dempsey, Inbal Nahum-Shani, Lindsey N Potter, David W Wetter, Cho Y Lam et al.
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在移动健康（mHealth）密集纵向数据（ILD）设定下，目标是建立多变量纵向结局与生存时间的联合模型，以捕捉快速波动对事件风险的影响。方法将多变量纵向结局降维为少数时变潜因子，并采用 Ornstein-Uhlenbeck（OU）随机过程对潜因子轨迹建模，随后将其纳入参数风险模型以关联生存结局。采用贝叶斯框架进行估计，规避了 ILD 下传统联合模型的高计算成本问题。模拟表明估计性能良好，实证分析将 9 种情绪降维为正/负情感潜因子，成功捕捉了戒烟后首次复吸的风险。对您有用：虽然本文采用贝叶斯参数化框架而非半参数效率理论，但其处理 ILD 的潜变量 OU 过程建模思路及戒烟实证数据集，对纵向因果推断中的时变混杂处理及流行病学应用有参考价值。
- **关键技术**: `joint longitudinal-survival model`, `Ornstein-Uhlenbeck process`, `latent factor model`, `Bayesian inference`, `intensive longitudinal data`
- **为什么对您有用**: 虽然本文为贝叶斯参数方法，但其针对密集纵向数据的联合建模框架和戒烟实证数据集，对您在纵向因果推断（时变混杂/生存结局）及流行病学应用方向有直接参考价值。

### 6. [10.1093/biomtc/ujaf003](https://doi.org/10.1093/biomtc/ujaf003) — A semicompeting risks model with an application to UK Biobank data to identify risk factors for diabetes onset and progression
- **作者**: Md Tuhin Sheikh, Hongyu Zhao
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在 UK Biobank 半竞争风险设定下（非终止事件 T2D 与并发症，终止事件死亡），目标是识别不同疾病阶段的风险因素并处理事件间依赖。核心方法为贝叶斯框架下的共享 gamma frailty 半竞争风险模型，用以刻画非终止与终止事件的关联结构。为利用入组时已患糖尿病的患病病例（prevalent cases），作者引入 power prior 机制整合这部分信息。模拟表明，power prior 的引入改善了模型拟合并提升了参数估计效率。UKB 实证分析揭示了遗传与非遗传因素在 T2D 进展各阶段的异质性作用。对您有用：本文展示了 UKB 数据的半竞争风险结构及整合患病病例的贝叶斯策略，对流行病学队列的多阶段进展分析有数据集参考价值，但未涉及半参数效率或形式化因果识别。
- **关键技术**: `semicompeting risks`, `shared gamma frailty model`, `Bayesian inference`, `power prior`, `prevalent cases`, `UK Biobank`
- **为什么对您有用**: 属于流行病学应用，使用了 UK Biobank 数据集和半竞争风险模型（与纵向/多阶段因果推断设定相关），对了解流行病学队列数据结构和进展分析有参考价值，但方法为参数贝叶斯框架，未触及您关注的半参数效率或形式化因果识别。

## 其他  *(other, 3 篇)*

### 1. [10.1093/biomtc/ujaf059](https://doi.org/10.1093/biomtc/ujaf059) — Improving estimation efficiency for case-cohort studies with a cure fraction
- **作者**: Qingning Zhou, Xu Cao
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 8/10
- **摘要**: {
  "topic": "nonparam_semipara",
  "summary_zh": "在广义 case-cohort 设计下研究含治愈分数的生存数据，目标是在半参数变换混合治愈模型（semiparametric transformation mixture cure model）下估计回归参数与治愈概率。提出两步估计：第一步基于完全数据构造 sieve maximum weighted likelihood 估计器，并用 EM 算法实现；第二步利用廉价协变量/辅助变量与结局的工作模型，以全样本信息更新估计器。理论证明更新后估计器一致且渐近效率不低于仅用完全数据的估计器，无论工作模型是否正确设定——这本质上是一种效率保证的 augmentation 策略。方差估计采用 weighted bootstrap。模拟与 Wilms 肿瘤数据展示了有限样本表现。对您有用：该文在半参数模型下实现了"工作模型误设亦不损失效率"的 augmentation，与您关注的 semiparametric efficiency bounds 及效率理论直接相关，sieve M-estimation 的技术路线也可迁移。",
  "key_techniques": ["sieve maximum weighted likelihood", "semiparametric transforma

### 2. [10.1093/biomtc/ujaf034](https://doi.org/10.1093/biomtc/ujaf034) — Power-enhanced two-sample mean tests for high-dimensional microbiome compositional data
- **作者**: Danning Li, Lingzhou Xue, Haoyi Yang, Xiufan Yu
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 7/10
- **摘要**: {
  "topic": "hypothesis_testing",
  "summary_zh": "在高维微生物组成分数据（单位和约束，$p \\gg n$）设定下，本文研究两样本均值向量的检验问题。提出基于P值组合的power-enhanced检验，融合maximum-type检验（捕捉稀疏信号）与quadratic-type检验（捕捉密集信号）的优势。理论部分利用高维Gaussian approximation与极值理论，证明该方法在较弱矩条件下可精确控制第一类错误率，并在更广的替代空间中提升检验功效。模拟与真实微生物组数据表明，该方法在不同信号稀疏度模式下均实现稳健且显著的功效提升。对您有用：直接推进您关注的"高维假设检验"方向，其power enhancement思想与Gaussian approximation技术可迁移至高维因果推断中的参数检验。",
  "key_techniques": [
    "high-dimensional hypothesis testing",
    "power enhancement",
    "P-value combination",
    "Gaussian approximation",
    "maximum-type test",
    "quadratic-type test"
  ],
  "why_r

### 3. [10.1093/biomtc/ujaf077](https://doi.org/10.1093/biomtc/ujaf077) — COCA: a randomized Bayesian design integrating dose optimization and component contribution assessment for combination therapies
- **作者**: Xiaohan Chi, Ruitao Lin, Ying Yuan
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 2
- 相关性 3/10
- **摘要**: {
  "topic": "other",
  "summary_zh": "在组合疗法早期试验中，需同时优化剂量并评估各组分贡献，传统设计样本量需求大。本文提出 COCA 两阶段随机化 II 期设计：第一阶段在多个候选组合剂量中通过最大化风险-收益权衡确定最优组合剂量；第二阶段启动多臂随机化评估各组分贡献。两阶段疗效数据通过带 spike-and-slab 先验的 Bayesian logistic 回归自适应合并以提升效率、缩减样本量。样本量与决策截断值通过新校准程序系统确定以保证期望的 operating characteristics。模拟表明 COCA 同时实现剂量优化与贡献评估双重目标，相比竞争设计节省大量样本量。对您而言，"组分贡献评估"与因果推断中 mediation/decomposition 有概念呼应，但本文为贝叶斯自适应试验设计，与您关注的 semiparametric efficiency 或 proximal CI 框架距离较远。",
  "key_techniques": [
    "spike-and-slab prior",
    "Bayesian adaptive design",
    "multi-arm randomization",
    "dose optimization",
    "calibration procedu


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

