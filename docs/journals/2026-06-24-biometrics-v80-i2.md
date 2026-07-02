# Biometrics — Vol 80  Issue 2  ·  2026-06-24

- 共 33 篇 · Biometrics
- 目录核对 ✅ 33 篇全部抓到（对照 OpenAlex 40 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

Biometrics Vol 80 Issue 2 的 33 篇论文中，因果推断占据绝对核心，覆盖了识别、估计、敏感性分析和实验设计的多个维度；此外，假设检验和流行病学应用也有重要贡献。整体可归纳为四条主线：其一，因果识别与估计的稳健性，聚焦双重稳健、近端控制与敏感性分析；其二，因果推断在时变/生存/纵向数据中的扩展，包括动态治疗策略、半竞争风险和治愈子群；其三，实验设计与随机化中的因果推断工具，涉及顺序分配、自适应随机化和基于随机化的置信区间；其四，高维中介分析与数据整合，少量但紧密关联因果推断。

因果推断的稳健性主线最为密集。*Doubly robust estimation and sensitivity analysis for marginal structural quantile models* 提出了边际结构分位数模型的双重稳健估计量，并引入混淆函数进行未测量混杂的敏感性分析。*Doubly robust proximal synthetic controls* 将近端因果推断引入合成控制，构造了双重稳健的GMM估计量，绕开了传统因子模型假设。*Single proxy control* 去除了秩保持假设，利用一个负对照结局实现非参数识别，并给出了双重稳健估计。*Differential recall bias in estimating treatment effects* 则在暴露误分类下推导了ATE的可识别界，并融合先验进行敏感性分析。这几篇共同推进了在模型误设或部分不可测混杂场景下，如何保持估计一致性或量化偏差边界。

时变与生存数据中的因果推断是另一突出主线。*Integrating randomized and observational studies to estimate optimal dynamic treatment regimes* 提出多阶段增强Q-learning估计量，利用观察性数据提升SMART的效率。*Causal inference for time-to-event data with a cured subpopulation* 基于主分层定义了always-uncured组的风险差和生存时间差，引入替代变量识别。*Direct and indirect treatment effects in the presence of semicompeting risks* 将中介分析拓展到存在终末事件的情形，定义了基于患病率和风险率的两种分解。*Regression models for average hazard* 提出用平均替代风险比，更易解释且对删失稳健。这些工作将因果推断的核心工具（效率增强、主分层、中介分解）推广到更贴合实际数据的生存和纵向结构。

此外，实验设计中的因果推断工具也值得注意。*On exact randomization-based covariate-adjusted confidence intervals* 在Fisher随机化检验框架下给出了ANCOVA型检验统计量的闭式置信区间；*Sequential covariate-adjusted randomization* 提出了逐患者最小化马氏距离与边际失衡的分配方法；*Robustness of response-adaptive randomization* 证明了双重自适应偏硬币设计对模型误设的稳健性。这三篇从精确推断和设计稳健性角度补充了实验因果推断的环节。

如果优先考虑与因果推断、半参数效率、高维方向最贴的论文，建议先读：*Doubly robust estimation and sensitivity analysis for marginal structural quantile models*（半参数效率+敏感性分析）、*Single proxy control*（非参数识别+双重稳健）、*Doubly robust proximal synthetic controls*（近端因果+双重稳健）、*Integrating randomized and observational studies to estimate optimal dynamic treatment regimes*（效率增强+纵向因果）、*Dissecting the colocalized GWAS and eQTLs with mediation analysis for high-dimensional exposures and confounders*（高维中介分析）、*On exact randomization-based covariate-adjusted confidence intervals*（精确推断+协变量调整）、以及*Efficient data integration under prior probability shift*（半参数似然+数据整合）。

## 因果推断  *(causal_inference, 15 篇)*

### 1. [10.1093/biomtc/ujae045](https://doi.org/10.1093/biomtc/ujae045) · [arXiv](https://arxiv.org/abs/2210.04100) — Doubly robust estimation and sensitivity analysis for marginal structural quantile models
- **作者**: Chao Cheng, Liangyuan Hu, Fan Li
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 该文在边际结构分位数模型（MSQM）框架下，估计时变治疗对潜在结果全分布的条件分位数处理效应，目标 estimand 为分位数差异。基于半参数模型，首先推导了 MSQM 的有效影响函数（EIF），并据此提出一类双重稳健（DR）估计量：当治疗分配模型或潜在结果分布模型中任一正确设定时，估计量一致；若两者均正确，则达到半参数有效界。为避免非光滑分位数目标函数带来的数值困难，采用平滑估计方程实现参数和方差的高效计算。在违反序贯可忽略性假设时，提出混淆函数方法进行敏感性分析，量化未测量混杂对估计的影响。模拟和 Yale 电子健康记录数据应用验证了方法的有限样本性能。对于专注因果推断的研究者，本文在边际结构模型和敏感性分析上提供了可直接迁移的双重稳健框架和半参数效率理论。
- **关键技术**: `doubly robust estimation`, `efficient influence function`, `marginal structural quantile model`, `smoothed estimating equation`, `confounding function for sensitivity analysis`, `semiparametric efficiency`
- **为什么对您有用**: 直接连接 primary interest 中的因果推断子方向——边际结构模型、敏感性分析。研究者武器库中 'estimation theory in causal inference'（very_familiar）和 'semiparametric theory'（moderately_familiar）可直接用于理解并复现该文的 DR 估计量与 EIF 推导；其平滑估计方程技巧也可与研究者熟悉的非参数统计和 M-估计（moderately_familiar）结合，用于处理类似非光滑 estimand。初步判断：立即可做——用 very_familiar 的因果推断估计理论和 moderately_familiar 的半参数理论即可分析此文并提出扩展（如纳入 proximal inference 或 higher-order U-statistic 视角下的分位数估计）。

### 2. [10.1093/biomtc/ujae046](https://doi.org/10.1093/biomtc/ujae046) — Integrating randomized and observational studies to estimate optimal dynamic treatment regimes
- **作者**: Anna Batorsky, Kevin J Anstrom, Donglin Zeng
- **期刊/来源**: Biometrics
- **机构**: University of North Carolina at Chapel Hill · University of Michigan
- **分类**: vol 80 · issue 2
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文旨在利用观察性数据提升随机试验（SMART）估计最优动态治疗策略（DTR）的效率。传统SMART成本高且需大样本，作者提出多阶段增强Q-learning估计量（MAQE），将SMART数据与观察性数据在多个时间点整合。方法扩展了已有的单阶段增强思路到多阶段Q-learning框架，通过利用共同表型、治疗和结局信息提高估计精度。模拟表明，MAQE比不加增广的Q-learning更准确估计最优DTR，且在不同样本量、噪声变量和效应大小下均稳健。该研究来自Back Pain Consortium，旨在为慢性腰痛定制个性化治疗。对您而言，本文直接衔接纵向因果推断中的DTR估计问题，您可用identification theory分析其识别假设是否合理，或用estimation theory评估其效率增益是否可达半参有效界。
- **关键技术**: `multi-stage augmented Q-learning`, `dynamic treatment regimes`, `SMART`, `observational study integration`, `augmented estimator`
- **为什么对您有用**: 1) 直接对应您primary interest中的纵向因果推断（DTR估计），且涉及结合RCT与观察性数据的识别与估计问题。2) 您的very_familiar武器库中“estimation theory in causal inference”可用于分析MAQE的渐近效率；moderately_familiar的“identification theory in causal inference”可用于审视其多阶段增广的识别条件（如无未测量混杂、一致性）。3) follow-up粗判：立即可做——用效率理论框架为该估计量推导半参有效界，或与现有DML方法做模拟对比。

### 3. [10.1093/biomtc/ujae027](https://doi.org/10.1093/biomtc/ujae027) · [arXiv](https://arxiv.org/abs/2302.06054) — Single proxy control
- **作者**: Chan Park, David B Richardson, Eric J Tchetgen Tchetgen
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文在潜在结果框架下，针对存在未观测混杂时的平均因果效应（ATT）识别问题，提出了单代理控制（single proxy control）的非参数方法。传统COCA方法依赖秩保持结构模型，假设个体因果效应恒定；本文去除了该假设，允许效应异质性，并建立了非参数识别条件。核心机制是利用一个负对照结局（NCO）作为治疗前反事实结局的误差代理，通过桥梁函数（bridge function）或扩展倾向得分实现识别。提出了三种估计策略：扩展倾向得分法、结局桥梁函数法以及双重稳健（doubly robust）法，后者结合了前两种的估计方程，具有效率优势。理论贡献在于证明了在单一代理下即可实现非参数识别，与近期近端因果推断（proximal causal inference）需要一对代理变量相比，显著降低了识别条件。应用部分以2015-2016年巴西Zika病毒爆发对出生率的影响为例，展示了方法的实用性。该方法与您的首要兴趣——因果推断中的近端因果推断和负对照变量设计——直接相关，尤其适用于流行病学研究中仅有一个可用代理的实际场景。
- **关键技术**: `negative control outcome`, `control outcome calibration approach (COCA)`, `outcome bridge function`, `doubly robust estimation`, `nonparametric identification`, `propensity score adjustment`
- **为什么对您有用**: 该文直接针对因果推断中proximal CI框架的代理数量限制，证明仅需单一负对照结局即可实现非参数识别，是对proximal CI（通常需一对代理）的重要补充与简化。您的武器库中'identification theory in causal inference'（中等熟悉）可用来评估其识别条件与proximal CI的优劣，而'doubly robust estimation'（属于estimation theory in causal inference，非常熟悉）可立即用于复现或扩展其双重稳健估计量。中期可做：在proximal CI框架下引入本文的桥梁函数思想，尝试统一理论。

### 4. [10.1093/biomtc/ujae054](https://doi.org/10.1093/biomtc/ujae054) · [arXiv](https://arxiv.org/abs/2310.18905) — Incorporating nonparametric methods for estimating causal excursion effects in mobile health with zero-inflated count outcomes
- **作者**: Xueqing Liu, Tianchen Qian, Lauren Bell, Bibhas Chakraborty
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在 micro-randomized trial (MRT) 框架下研究 causal excursion effect 的估计问题，目标 estimand 是干预对 zero-inflated count outcome 的边缘效应，识别依赖于 MRT 的随机化假设与 sequential ignorability。作者提出了结合非参数方法的估计策略，核心是利用 sieve / kernel 等非参数回归构建 outcome model 与 propensity score，并采用类似 one-step / AIPW 的构造获得 double robustness。理论贡献包括建立 bidirectional asymptotics（同时允许参数维数与样本量增长），证明了估计量的 √n-consistency 与渐近正态性。模拟与 Drink Less 试验数据分析验证了方法在 zero-inflation 设定下的实用性。对您而言，这是 longitudinal causal inference 与 semiparametric efficiency 理论在移动健康场景的具体应用。
- **关键技术**: `causal excursion effect`, `micro-randomized trial`, `zero-inflated count outcome`, `nonparametric sieve estimation`, `double robustness`, `bidirectional asymptotics`
- **为什么对您有用**: 直接连接到 primary interest 中的 longitudinal causal inference 与 semiparametric theory——causal excursion effect 是 MRT 场景下的核心 estimand，zero-inflated count outcome 扩展了现有 binary/continuous 的工作。您武器库中的 semiparametric theory（moderately familiar）与 nonparametric statistics（very familiar）可直接用于审视其 bidirectional asymptotics 证明与 sieve 估计的收敛率分析。**中期可做**：若想在此方向深入，需在 identification theory in causal inference（moderately familiar）上加强，特别是 MRT 的 sequential randomization 结构；技术层面，用您熟悉的 minimax bound 工具可验证其 sieve 估计的 rate 是否达到 optimal。

### 5. [10.1093/biomtc/ujae028](https://doi.org/10.1093/biomtc/ujae028) — Causal inference for time-to-event data with a cured subpopulation
- **作者**: Yi Wang, Yuhao Deng, Xiao-Hua Zhou
- **期刊/来源**: Biometrics
- **机构**: Peking University · Peking University International Hospital · Shanghai University of International Business and Economics · Guangzhou Experimental Station · Beijing Institute of Big Data Research
- **分类**: vol 80 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在 cure model 框架下，目标是在存在 cured subpopulation 时定义并识别 treatment effect on failure times。本文基于 principal stratification 提出两个因果 estimands：always-uncured 组的 timewise risk difference 和 mean survival time difference，作为对 treatment effect on cure rates 的补充。识别方面，作者引入 substitutional variable 代理潜在 cure status，在 ignorable treatment assignment 下证明了 identifiability。估计方法采用 mixture cure model 结合 substitutional variable 的建模，但未给出 semiparametric efficiency bound 或 influence function 形式的理论。实证分析应用于急性淋巴细胞白血病移植数据的 leukemia-free survival 比较。对您而言，这是 principal stratification 在 survival context 的具体应用，但方法学深度偏 identification 而非 efficiency theory。
- **关键技术**: `principal stratification`, `mixture cure model`, `substitutional variable for identification`, `time-to-event analysis`, `competing risks framework`
- **为什么对您有用**: 连接到 causal inference 的 principal stratification 和 identification theory 子方向。您 very_familiar 的 identification theory in causal inference 可以直接审视其 identifiability 条件的完备性，moderately_familiar 的 semiparametric theory 可用于补全其缺失的 efficiency bound 分析。**中期可做**：目前方法停留在 parametric/semiparametric estimation 层面，可用 semiparametric efficiency theory 推导 influence function 和 efficient estimator，或引入 DML 框架处理高维协变量。

### 6. [10.1093/biomtc/ujae032](https://doi.org/10.1093/biomtc/ujae032) — Direct and indirect treatment effects in the presence of semicompeting risks
- **作者**: Yuhao Deng, Yi Wang, Xiao-Hua Zhou
- **期刊/来源**: Biometrics
- **机构**: Peking University · Michigan United · Peking University International Hospital · Shanghai University of International Business and Economics · Beijing Institute of Big Data Research
- **分类**: vol 80 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 该文考虑半竞争风险（terminal event 可删失 nonterminal event）下的随机对照试验，目标是分解总治疗效应为直接效应（通过非终末事件路径以外）和间接效应（通过非终末事件）两部分。作者提出两种分解策略：一是调整非终末事件的患病率（prevalence），二是调整非终末事件的风险率（hazard），二者需要不同形式的跨世界（cross-world）假设才能识别。对于每一策略，定义了反事实累积发生率（counterfactual cumulative incidence）并建立了估计量的渐近性质。通过模拟和两个实际数据应用展示了两种分解的细微差别。该文将经典中介分析（mediation analysis）框架扩展至半竞争风险数据，对纵向因果推断和流行病学中的生存分析实际问题有直接参考价值。
- **关键技术**: `mediation analysis`, `semicompeting risks`, `counterfactual cumulative incidence`, `cross-world assumptions`, `decomposition of total effect`
- **为什么对您有用**: 该文直接对接到研究者 primary interest 中的 'causal inference (mediation, longitudinal)' 子方向，且与 secondary interest 中 epidemiology 的生存/竞争风险数据紧密相关。研究者使用武器库中 'estimation theory in causal inference' 和 'identification theory in causal inference' 可立即理解识别假设与推断方法，属'立即可做'的文献。该文提出的两种分解对比框架也可启发研究者思考在更复杂设定（如 proximal causal inference 或 high-dimensional covariates）下如何定义和估计直接/间接效应。

### 7. [10.1093/biomtc/ujae055](https://doi.org/10.1093/biomtc/ujae055) · [arXiv](https://arxiv.org/abs/2210.02014) — Doubly robust proximal synthetic controls
- **作者**: Hongxiang Qiu, Xu Shi, Wang Miao, Edgar Dobriban, Eric Tchetgen Tchetgen
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对面板数据中单个处理单元的因果效应推断问题，利用近端因果推断（proximal causal inference）框架，提出了两种新的非参数识别公式：一种基于加权，另一种融合了反事实结果模型和加权函数。作者引入协变量偏移（covariate shift）概念，在给定处理分配的条件下识别条件平均处理效应，不要求传统的完美处理前轨迹匹配。基于广义矩方法（GMM）构造了两个估计量，其中一个满足双重稳健性——只要结果模型或加权模型至少一个正确设定，该估计量即一致且渐近正态。该方法绕开了传统合成控制对线性因子模型的依赖，识别条件更为宽松。模拟实验和巴西肺炎疫苗效果的应用展示了方法的有限样本表现。对您而言，本文直接对接您的近端因果推断兴趣，并将识别与估计方法扩展到面板数据场景，与您非常熟悉的因果推断估计理论高度契合。
- **关键技术**: `proximal causal inference`, `synthetic control`, `double robustness`, `generalized method of moments`, `covariate shift`, `nonparametric identification`
- **为什么对您有用**: 本文直接服务于您对近端因果推断（proximal CI）的兴趣，将proximal idea创新性地应用到面板数据合成控制场景，提出了双重稳健估计。您非常熟悉的estimation theory in causal inference可直接用于分析该估计量的渐近性质（如效率界、敏感性），并且可进一步结合proximal CI的负控制设定进行拓展。基于现有武器库，此方法立即可做深入理解和扩展研究。

### 8. [10.1093/biomtc/ujae023](https://doi.org/10.1093/biomtc/ujae023) · [arXiv](https://arxiv.org/abs/2302.01246) — Behavioral carry-over effect and power consideration in crossover trials
- **作者**: Danni Shi, Ting Ye
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在潜在结果框架下研究交叉试验中行为性遗留效应对处理效应估计和检验功效的影响。定义基本估计量，证明当遗留效应满足符号条件时，该估计量低估真实处理效应但不膨胀单侧检验的第一类错误，而是降低检验功效。进一步推导出交叉设计比平行组设计更有效的条件，解决了存在遗留效应时的设计选择问题。同时提出基于协变量调整的方法以提升估计精度，并通过 MTN-034/REACH 研究数据验证了方法性能。对您而言，该论文的潜在结果识别框架直接关联因果推断中的 identification 问题，交叉试验的功效分析可衔接您的假设检验兴趣，协变量调整方法则与您熟悉的因果推断估计理论紧密相关。
- **关键技术**: `Potential outcomes framework`, `crossover design`, `basic estimator`, `sign condition`, `power analysis`, `covariate adjustment`
- **为什么对您有用**: 本文直接运用潜在结果框架（因果推断的核心）分析交叉试验的识别与估计问题，属于 causal inference 中 identification 的子方向。您非常熟悉的因果推断估计理论（如 IPW、Hájek 估计）可立即用于理解或扩展该文的估计器性质。同时，该类临床试验设计问题属于您的 secondary interest 流行病学，论文提供的数据和功率分析思路可作为实际应用案例。follow-up：立即可做——用已有因果推断武器（非常熟悉）可复现或延伸该文的条件推导。

### 9. [10.1093/biomtc/ujae058](https://doi.org/10.1093/biomtc/ujae058) · [arXiv](https://arxiv.org/abs/2307.02331) — Differential recall bias in estimating treatment effects in observational studies
- **作者**: Suhwan Bong, Kwonsang Lee, Francesca Dominici
- **期刊/来源**: Biometrics
- **机构**: Seoul National University · Harvard University
- **分类**: vol 80 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究观察性研究中因回顾性偏差（recall bias）导致的暴露误分类问题，特别关注 differential recall bias——即偏差方向与程度随结果状态变化。在没有验证性研究（validation study）的设定下，作者首先推导了平均处理效应（ATE）的可识别界（bounds），为因果推断提供了不依赖外部验证的保守范围。随后提出多种估计策略，分别基于差异化的假设（如非差异性、工具变量型假设等），并开发了融入先验信息的敏感性分析方法。通过广泛的模拟实验考察了模型误设下的稳健性，最后将方法应用于童年期身体虐待对成年期心理健康影响的实际数据分析。该工作为无法获取黄金标准暴露测量时的因果推断提供了系统性的分析框架。
- **关键技术**: `bounds for ATE under differential misclassification`, `sensitivity analysis with prior information`, `multiple estimation strategies under varying assumptions`
- **为什么对您有用**: 本文直接连接您的首要兴趣——因果推断中的识别与敏感性分析，具体针对 exposure misclassification 这一重要实际挑战。您可运用 technical_arsenal 中‘estimation theory in causal inference’来审视和推广该文提出的 bounds 至连续暴露或非线性模型，或用‘nonparametric statistics’推导更紧的非参界。Follow-up 粗判：立即可做，因为您对因果推断中的估计理论已很熟悉。

### 10. [10.1093/biomtc/ujae025](https://doi.org/10.1093/biomtc/ujae025) · [arXiv](https://arxiv.org/abs/2302.11656) — Confounder-dependent Bayesian mixture model: Characterizing heterogeneity of causal effects in air pollution epidemiology
- **作者**: Dafne Zorzetto, Falco J Bargagli-Stoffi, Antonio Canale, Francesca Dominici.
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文聚焦于空气污染流行病学中PM2.5长期暴露对死亡率因果效应的异质性识别问题。目标估计量是组平均处理效应（GATE），即条件平均处理效应在由协变量定义的子组上的聚合。作者提出Confounder-Dependent Bayesian Mixture Model (CDBMM)，利用依赖狄利克雷过程（dependent Dirichlet process）对潜在结果的条件分布进行灵活建模，从而在数据驱动下识别互斥且具有相似GATE的群体。该方法的核心机制是构建一个依赖于混杂变量和处理的无限混合模型，允许后验聚类自动捕捉异质性模式。通过仿真实验展示了方法在恢复异质性结构上的有效性，并应用于德克萨斯州Medicare保险索赔数据，识别出六个具有显著不同PM2.5因果效应的亚组。该工作为因果效应异质性分析提供了一种贝叶斯非参数工具，对流行病学中政策制定具有直接指导意义。对您而言，本文是因果推断在流行病学中的应用实例，尤其其GATE估计思路可迁移至您关注的纵向或中介分析中。
- **关键技术**: `Dependent Dirichlet process`, `Bayesian nonparametric mixture model`, `Group average treatment effect (GATE)`, `Confounder-dependent clustering`, `Causal effect heterogeneity`
- **为什么对您有用**: 本文连接您的secondary interest中流行病学应用，展示了贝叶斯非参数方法在因果推断异质性分析中的实际应用。您熟悉的非参数统计和因果推断估计论可帮助快速理解其GATE识别策略，但贝叶斯计算（dependent Dirichlet process）目前不在您的技术库中，属于中期可做的方向：若能掌握贝叶斯非参数基础，则可将类似聚类思路引入您的高阶U-统计或半参数效率框架。

### 11. [10.1093/biomtc/ujae050](https://doi.org/10.1093/biomtc/ujae050) — Dissecting the colocalized GWAS and eQTLs with mediation analysis for high-dimensional exposures and confounders
- **作者**: Qi Zhang, Zhikai Yang, Jinliang Yang
- **期刊/来源**: Biometrics
- **机构**: University of New Hampshire · University of Nebraska–Lincoln
- **分类**: vol 80 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文提出 MedDiC，一种针对高维暴露和混杂因素的中介效应估计程序。目标是在 GWAS 与 eQTL 共定位研究中，估计每个遗传变异对表型的总体间接效应 (Overall Indirect Effect, IE)。方法基于 difference-in-coefficients 思路，通过线性模型分解直接与间接效应，并利用高维正则化处理暴露和混杂的维度问题。模拟研究表明，MedDiC 在检验效能、置信区间长度和计算时间上优于现有方法。应用于玉米和小鼠两套真实数据集，结果与已知生物学机制一致，且在不同性状间具有良好的可重复性。该工作直接将因果推断中的中介分析推向高维场景，对您从事的 mediation 和 high-dimensional statistics 研究有直接参考价值。
- **关键技术**: `mediation analysis`, `difference-in-coefficients`, `high-dimensional exposures`, `confounders`, `GWAS-eQTL colocalization`
- **为什么对您有用**: 本文直接面向 primary interest 中的 mediation 方向，并在高维暴露和混杂设定下发展了新的推断程序。您可以利用对因果推断估计理论（very_familiar）和高维渐近（very_familiar）的熟悉程度，快速评估其方法在效率或假设强度上的改进空间。此外，若想将方法扩展至 semiparametric 效率框架（moderately_familiar 中的 semiparametric theory），可以中期着手——目前论文未使用 influence function 或 cross-fitting，但这是潜在的提升方向。总体判断：立即可做，因为核心技术已在武器库中。

### 12. [10.1093/biomtc/ujae033](https://doi.org/10.1093/biomtc/ujae033) — Identifying temporal pathways using biomarkers in the presence of latent non-Gaussian components
- **作者**: Shanghong Xie, Donglin Zeng, Yuanjia Wang
- **期刊/来源**: Biometrics
- **机构**: Southwestern University of Finance and Economics · University of Michigan · Columbia University
- **分类**: vol 80 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究时间序列生物标记物网络中潜在时间路径的识别问题，目标是在存在潜在非高斯成分（如伪迹、结构化噪声、遗传风险等）时，区分同期关系与时间关系。现有向量自回归（VAR）和动态因果模型未能处理隐藏的非高斯成分，导致估计有偏。作者提出一种新方法，先用独立成分分析（ICA）从多受试者时间序列数据中提取未观测的非高斯成分，然后在残差基础上基于矩估计分别估计同期网络和时序网络。算法计算快速且可扩展，并给出了网络结构的可识别性条件和渐近性质。通过大量模拟和ADHD脑区域生物标志物应用，证明了方法在恢复真实时序路径方面的优越性，发现时间边跨不同脑区，而同期边多集中在同一脑区的双侧连接。该方法为纵向因果推断中处理隐藏混杂信号提供了一个实用的工具，对您关注的因果推断中的时间序列识别方向有直接参考价值。
- **关键技术**: `independent component analysis (ICA)`, `vector autoregression (VAR)`, `method of moments`, `temporal network estimation`, `contemporaneous network separation`, `identifiability and asymptotic analysis`
- **为什么对您有用**: 本文直接对应您对纵向因果推断（longitudinal causal inference）的兴趣，特别是从多受试者时间序列生物标记物中识别时间依赖路径，与IV、中介分析等方向互补。您的技术武库中有非常熟悉的高维渐近和非参数估计，可用来验证文中渐近性质或设计更灵活的残差模型；但核心的ICA成分提取并非当前熟悉工具，属中期可做——需先在独立成分分析或因子模型上提升熟练度（moderately_familiar级别）方能深入复现或扩展该方法。总体来说，本文提供了一个干净的识别框架和实际数据分析案例，适合作为进入纵向因果推断的一个良好起点。

### 13. [10.1093/biomtc/ujae047](https://doi.org/10.1093/biomtc/ujae047) — Sequential covariate-adjusted randomization via hierarchically minimizing Mahalanobis distance and marginal imbalance
- **作者**: Haoyu Yang, Yichen Qin, Yang Li, Feifang Hu
- **期刊/来源**: Biometrics
- **机构**: Renmin University of China · University of Cincinnati · George Washington University
- **分类**: vol 80 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对比较研究中顺序随机化无法满足临床即时分配需求的问题，提出一种逐患者顺序分配方法。该方法将协变量不平衡度定义为修正马氏距离，并将边际不平衡（两组样本量差）分离，以显式优先级分层最小化这两个目标。与其他顺序随机化方法相比，该方法能在保持边际平衡（即两组样本量接近）的同时达到尽可能好的协变量平衡，从而更灵活地控制分配过程。理论部分证明了不平衡度量的收敛速度以及随后的处理效应估计（如均值差）的一致性。模拟和实际数据分析表明，该方法在平衡协变量方面显著优于现有顺序随机化方法（如Pocock-Simon方法）。对您而言，该工作涉及因果推断中实验设计的核心环节（随机化机制），其理论分析框架与您熟悉的estimation theory in causal inference直接相连。
- **关键技术**: `sequential randomization`, `modified Mahalanobis distance`, `covariate balance`, `marginal imbalance minimization`, `treatment effect estimation`
- **为什么对您有用**: 本文涉及比较研究中的顺序随机化设计，这是因果推断中处理效应估计的基础环节（实际实验设计）。其理论论证（不平衡度的收敛性和效应估计的一致性）可用您very_familiar中的estimation theory in causal inference武器（如非参数估计、minimax界）验证其最优性。立即可做：您可以直接评估该方法在ATE估计中的有效性，或者将其作为基准比较您自己工作中涉及随机化分配的场景。

### 14. [10.1093/biomtc/ujae037](https://doi.org/10.1093/biomtc/ujae037) — Regression models for average hazard
- **作者**: Hajime Uno, Lu Tian, Miki Horiguchi, Satoshi Hattori, Kenneth L Kehl
- **期刊/来源**: Biometrics
- **机构**: Dana-Farber Cancer Institute · Stanford University · The University of Osaka
- **分类**: vol 80 · issue 2
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对Cox比例风险模型中风险比（hazard ratio）作为治疗效应度量存在的局限，提出基于平均风险（Average Hazard, AH）的回归模型，以在给定截断时间τ内估计绝对差异和相对效应。该AH定义为删失无关的生存加权人时发病率，可在独立删失、组别特异性删失和协变量依赖删失三种假设下构建回归框架。方法核心是将AH回归与稳健Poisson回归紧密关联，但通过引入截断时间τ显式处理删失，从而比标准Poisson回归对删失更稳健。作者给出了三种删失设定下的估计方程和推断方法，并证明AH回归能同时提供治疗效应的绝对差和相对比，便于临床解释。仿真和实例分析表明，AH回归在非比例风险、交叠生存曲线等场景下比传统Cox模型更可靠。本文对您的主要兴趣领域“因果推断”直接相关，尤其为时间-事件结局的治疗效应量化提供了不依赖比例风险假设的替代工具，可与您熟悉的非参数统计和因果估计方法衔接。
- **关键技术**: `Average hazard regression`, `Robust Poisson regression`, `Censoring mechanisms`, `Treatment effect estimation for time-to-event outcomes`
- **为什么对您有用**: 本文属于因果推断中治疗效应估计的生存分析方法，直接对应您的primary interest“causal inference”（特别是与时间-事件结局相关的ATE度量）。您的武器库中“estimation theory in causal inference”和“nonparametric statistics”足以理解和评价其稳健Poisson回归与删除结构，属于“立即可做”的阅读范畴，无需额外工具即可跟进其方法细节及潜在扩展（如与逆概率删失加权结合）。

### 15. [10.1093/biomtc/ujae049](https://doi.org/10.1093/biomtc/ujae049) — Robustness of response-adaptive randomization
- **作者**: Xiaoqing Ye, Feifang Hu, Wei Ma
- **期刊/来源**: Biometrics
- **机构**: Renmin University of China · George Washington University
- **分类**: vol 80 · issue 2
- 相关性 5/10 · novelty: `weaker_assumption`
- **摘要**: 本文研究响应自适应随机化中双重自适应偏硬币设计（DBCD）对模型误设的稳健性。在临床试验中，DBCD根据累积响应调整分配概率以优先考虑伦理，但其理论性质通常假设响应模型正确设定。作者证明了即使设计模型误设（响应真实分布不同于设计模型），分配比例的一致性和渐近正态性仍可保持。进一步，针对三种常用线性回归模型（均值差、ANCOVA I、ANCOVA II）估计处理效应，允许模型任意误设，推导了估计量的渐近性质。结果表明，包含协变量-处理交互项的ANCOVA II模型提供最有效的估计量。这些结果为DBCD在模型不确定场景下的应用提供了理论支撑。对您有用：连接了因果推断中处理效应估计的稳健性分析，可使用您熟悉的 estimation theory in causal inference 深入检验其效率界。
- **关键技术**: `response-adaptive randomization`, `DBCD`, `model misspecification`, `ANCOVA`, `asymptotic normality`, `treatment effect estimation`
- **为什么对您有用**: 本文直接关联因果推断中处理效应估计的稳健性，特别是随机化设计下模型误设的渐近性质。您武器库中的'estimation theory in causal inference'可用于理解其估计量的效率与稳健性权衡。中期可做：若先在moderately_familiar的'semiparametric theory'上深入（特别是有效率界的概念），可进一步推导更一般的效率上界。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1093/biomtc/ujae021](https://doi.org/10.1093/biomtc/ujae021) — High-dimensional multisubject time series transition matrix inference with application to brain connectivity analysis
- **作者**: Xiang Lyu, Jian Kang, Lexin Li
- **期刊/来源**: Biometrics
- **机构**: University of California, Berkeley · University of Michigan
- **分类**: vol 80 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究高维 VAR 模型下带测量误差和多主体的 transition matrix 推断问题，目标是同时检验矩阵中的非零元素。方法核心是三个组件：修正的 EM 算法估计模型参数（处理测量误差和多主体异质性），基于张量回归构造偏差校正后的滞后自协方差估计量，并以此导出同时检验统计量。理论上证明了修正 EM 估计量的 uniform consistency，并证明了所提同时检验能够渐近控制 FDR 且功效趋近于 1。模拟和任务态 fMRI 数据实验验证了方法的有效性。本文对您在高维统计和假设检验方向的工作有直接借鉴：其处理 multi-subject 高维时间序列的推断框架可与您熟悉的 high-dimensional asymptotics 工具对接。
- **关键技术**: `high-dimensional VAR`, `measurement error correction`, `EM algorithm with bias correction`, `tensor regression`, `simultaneous hypothesis testing`, `false discovery rate control`
- **为什么对您有用**: 本文属于您 primary interest 中的高维统计和假设检验子方向，具体针对高维 VAR 模型的多重推断。技术武库中 very_familiar 的 'high-dimensional asymptotics' 可直接用于验证本文 uniform consistency 证明的严谨性。立即可做：您可以复现其 EM 估计的收敛性分析并探讨更紧的概率界。

## 非参数 / 半参数  *(nonparam_semipara, 2 篇)*

### 1. [10.1093/biomtc/ujae035](https://doi.org/10.1093/biomtc/ujae035) — Efficient data integration under prior probability shift
- **作者**: Ming-Yueh Huang, Jing Qin, Chiung-Yu Huang
- **期刊/来源**: Biometrics
- **机构**: Institute of Statistical Science, Academia Sinica · National Institutes of Health · National Institute of Allergy and Infectious Diseases · University of California, San Francisco
- **分类**: vol 80 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在 prior probability shift 设定下，目标是从多个异质数据源高效整合信息估计目标总体参数，核心假设是条件密度 P(X|Y) 跨数据源不变而边际 P(Y) 变化。本文提出基于经验似然的估计方法，通过 semiparametric likelihood 整合多源数据，支持连续和离散 outcome，突破了现有方法仅适用于离散 outcome 的限制。高维情形下引入 adaptive LASSO 进行变量选择，证明估计量具有 oracle property；同时提出基于 Neyman smooth alternatives 的 semiparametric likelihood ratio test 检验 prior probability shift 假设的成立性。模拟与实际数据分析验证了方法的有效性。对您在 semiparametric efficiency 和因果推断中数据整合问题有直接参考价值。
- **关键技术**: `empirical likelihood`, `semiparametric likelihood ratio test`, `Neyman smooth alternatives`, `adaptive LASSO`, `oracle property`, `prior probability shift`
- **为什么对您有用**: 直接连接到 semiparametric theory 这一 primary interest，涉及 semiparametric likelihood 构造与效率理论。technical_arsenal 中的 semiparametric theory（moderately_familiar）可直接用于审视其 likelihood 构造是否达到效率界，M-estimation theory 可用于分析 oracle property 的正则条件。立即可做：用您熟悉的 minimax bound 工具检验其声称的效率是否真正达到 semiparametric efficiency bound，或用 semiparametric theory 框架审视其 likelihood ratio test 的局部功效性质。

### 2. [10.1093/biomtc/ujae024](https://doi.org/10.1093/biomtc/ujae024) — Deep partially linear cox model for current status data
- **作者**: Qiang Wu, Xingwei Tong, Xingqiu Zhao
- **期刊/来源**: Biometrics
- **机构**: Beijing Normal University · Hong Kong Polytechnic University
- **分类**: vol 80 · issue 2
- 相关性 4/10 · novelty: `new_theory`
- **摘要**: 在 current status data（区间删失生存数据）的设定下，本文提出 deep partially linear Cox 模型，目标是对 treatment effect 的有限维参数进行 semiparametric efficient estimation。模型将线性部分（treatment covariates）与非线性部分（confounders，用 DNN 建模）分离，同时用 monotone splines 近似 baseline cumulative hazard。理论贡献包括：DNN 部分的 convergence rate（非参数速率）和有限维参数的 √n-consistency、asymptotic normality，并证明其达到 semiparametric efficiency bound。实证部分通过模拟和新闻流行度数据验证方法。对您在 semiparametric efficiency theory 和 DNN 非参数估计交叉方向有直接参考价值。
- **关键技术**: `deep partially linear model`, `current status data`, `semiparametric efficiency bound`, `monotone spline approximation`, `maximum likelihood estimation`, `DNN nonparametric regression`
- **为什么对您有用**: 直接连接到您 primary interest 中的 semiparametric efficiency theory——本文给出了 DNN nuisance参数估计下有限维参数仍能达到 efficiency bound 的完整证明。您熟悉的 minimax bounds 和 high-dimensional asymptotics 可用于审视其 DNN convergence rate 是否紧；semiparametric theory（moderately_familiar）是理解本文核心证明的必要工具。立即可做：用您 very_familiar 的 nonparametric statistics 和 estimation theory 验证其效率证明的严谨性，或将其与 HOIF 框架对比看是否有 higher-order bias correction 的空间。

## 数理统计 / 假设检验  *(hypothesis_testing, 4 篇)*

### 1. [10.1093/biomtc/ujae051](https://doi.org/10.1093/biomtc/ujae051) · [arXiv](https://arxiv.org/abs/2502.18666) — On exact randomization-based covariate-adjusted confidence intervals
- **作者**: Jacob Fiksel
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在 Fisher randomization test 框架下，目标是构造 covariate-adjusted 的 randomization-based confidence interval，关键假设是 randomization scheme（如 complete randomization）和 potential outcomes 的有限样本设定。本文扩展了 Zhu & Liu 的工作，针对 ANCOVA-type test statistic 推导出闭式表达的置信区间，避免了传统 test inversion 的计算负担。核心贡献包括：给出充分条件（可由观测数据检验）保证区间的正确覆盖率，以及证明该方法在非正态 outcome 下保持 robust。模拟显示计算时间与 Fisher-exact P-value 相当，并在 Phase I 临床试验数据上进行了实证分析。对您在假设检验与统计计算交叉方向有直接参考价值。
- **关键技术**: `Fisher randomization test`, `test inversion confidence interval`, `ANCOVA-type test statistic`, `closed-form confidence interval`, `exact randomization-based inference`, `covariate adjustment`
- **为什么对您有用**: 本文连接到您 primary interest 中的假设检验与统计计算方向，具体是 randomization-based inference 的计算效率问题。您的 technical_arsenal 中 software development 与 minimax bounds for estimation problems 可以用于评估该方法的计算复杂度与理论性质。**立即可做**：用 very_familiar 的 nonparametric statistics 和 software development 工具可以复现并扩展该方法，例如探索更复杂的 covariate-adjusted statistic 或其他 randomization design 下的闭式解。

### 2. [10.1093/biomtc/ujae036](https://doi.org/10.1093/biomtc/ujae036) — Testing conditional quantile independence with functional covariate
- **作者**: Yongzhen Feng, Jie Li, Xiaojun Song
- **期刊/来源**: Biometrics
- **机构**: Tsinghua University · Renmin University of China · Peking University
- **分类**: vol 80 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对标量响应与函数型协变量，在连续分位数水平上检验条件分位数独立性假设。作者构建了基于随机投影的Cramér–von Mises型检验统计量，通过将函数型协变量投影到有限维空间来规避维数诅咒，且投影后的假设几乎处处等价于原假设。利用经验过程理论，推导了检验统计量在零假设下的渐近分布。检验能够以参数速率探测一类局部备择假设，并给出全局与局部功效的渐近性质。通过乘子bootstrap方法估计临界值，模拟和EEG数据示例验证了有限样本表现。该工作为函数型数据中的条件独立性检验提供了非参数工具，与您熟悉的假设检验和非参数统计方向直接相关。
- **关键技术**: `Cramér–von Mises test`, `random projection`, `functional data`, `conditional quantile independence`, `empirical process`, `multiplier bootstrap`
- **为什么对您有用**: 连接到您的首要兴趣——假设检验与非参数理论中的函数型协变量条件独立性检验。您非常熟悉的非参数统计和高维渐近工具可直接用于评估该方法的随机投影策略能否扩展到其他检验问题（如条件均值独立性）。立即可做：无需额外学习即可基于该文思路开展后续研究（例如将投影方法与U-statistic结合）。

### 3. [10.1093/biomtc/ujae056](https://doi.org/10.1093/biomtc/ujae056) — Efficient testing of the biomarker positive and negative subgroups in a biomarker-stratified trial
- **作者**: Lang Li, Anastasia Ivanova
- **期刊/来源**: Biometrics
- **机构**: University of North Carolina at Chapel Hill
- **分类**: vol 80 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在 biomarker-stratified RCT 设定下，目标是同时检验 biomarker positive 和 negative 两个子群的 treatment effect，核心假设是 isotonic assumption（positive subgroup 的 treatment effect ≥ negative subgroup）。作者在 order-constrained 假设下构造了高效检验方法，利用 isotonic regression 的序约束结构提升检验功效，相比 Bonferroni 或 gatekeeping 等现有方法显著降低所需样本量。理论贡献在于证明在 prevalence < 0.5 时样本量节省尤为明显，使 pivotal trials 中同时评估两个子群变得可行。对您在 hypothesis testing 和 efficiency theory 方向的兴趣有直接参考价值。
- **关键技术**: `order-constrained hypothesis testing`, `isotonic regression`, `multiple testing with logical constraints`, `treatment effect heterogeneity`, `sample size efficiency`
- **为什么对您有用**: 直接连接到您 primary interest 中的 hypothesis testing 与 efficiency theory——这是在有序约束假设下的最优检验设计问题。您熟悉的 minimax bounds 和 nonparametric statistics 可用于分析该检验在更弱假设下的功效性质，属于**立即可做**：用 very_familiar 的 nonparametric statistics 工具即可审视其 isotonic assumption 是否可放松、效率提升是否达到理论下界。

### 4. [10.1093/biomtc/ujae022](https://doi.org/10.1093/biomtc/ujae022) — Flagging unusual clusters based on linear mixed models using weighted and self-calibrated predictors
- **作者**: Charles E McCulloch, John M Neuhaus, Ross D Boylan
- **期刊/来源**: Biometrics
- **机构**: University of California, San Francisco
- **分类**: vol 80 · issue 2
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在线性混合模型中，研究者常使用随机截距的预测值（如BLUP）来标记极端聚类（如表现差的医院）。该文指出，基于BLUP和固定效应预测的现有标记规则存在严重缺陷：错误标记率要么过高（极限接近0.5），要么过于保守（显著低于0.05），导致正确标记率极低。文章通过理论推导和大量数值模拟，系统评估了不同预测量和准确度指标的表现。作者提出了新的加权预测量和自校准预测量，能够有效控制错误标记率，同时显著提升正确标记率。新方法形式简单、易于实现。实际数据应用展示了其在儿童哮喘住院时长聚类分析中的优越性。该工作对纵向数据或分层结构中的异常点检测有直接参考价值，并与假设检验中的多重比较问题紧密相连。
- **关键技术**: `best linear unbiased predictor (BLUP)`, `fixed effects predictor`, `weighted predictor`, `self-calibrated predictor`, `linear mixed model`, `numerical evaluation via simulation`
- **为什么对您有用**: 直接连接到假设检验中的错误控制问题，尤其适用于流行病学中医院绩效评估或患者轨迹异常检测。您的武器库中的nonparametric statistics和minimax bounds可用来分析其预测量的最优性边界，但具体混合模型预测区间校准技术不在当前very_familiar列表中（缺线性混合模型推断经验），属于暂不可做——需要先在线性混合模型预测分布理论上补课。不过作为流行病学数据集和标记规则的应用型参考，值得一读。

## 统计计算 / 算法  *(stat_computing, 3 篇)*

### 1. [10.1093/biomtc/ujae031](https://doi.org/10.1093/biomtc/ujae031) · [arXiv](https://arxiv.org/abs/2402.15071) — High-dimensional covariate-augmented overdispersed poisson factor model
- **作者**: Wei Liu, Qingzhi Zhong
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对高维计数数据，提出协变量增强过离散泊松因子模型，同时进行因子分析和系数矩阵估计。模型在泊松因子分析基础上引入可观测协变量，并通过低秩约束捕捉响应变量与协变量的相互依赖关系。为处理非线性、两个高维潜变量矩阵及低秩约束带来的计算挑战，提出结合Laplace近似和Taylor近似的变分EM算法。理论上给出了可识别性条件，并基于奇异值比准则开发了确定因子数和系数矩阵秩的方法。模拟研究表明该方法在估计精度和计算效率上优于现有方法，并在CITE-seq数据上展示了实用性。方法已实现为R包COAP。该工作与您的高维统计和统计计算（变分推断、算法开发）兴趣直接相关，可利用您熟悉的软件工程经验快速复现和应用。
- **关键技术**: `variational EM`, `Laplace approximation`, `Taylor approximation`, `low-rank matrix`, `singular value ratio criterion`, `Poisson factor model`
- **为什么对您有用**: 本文连接您的高维统计和统计计算子方向，特别是变分推断在因子模型中的应用。您可运用'高维渐近理论'分析该变分估计的一致性，同时您的'软件开发'技能可轻松使用和扩展其R包。该R包立即可用于分析类似高维计数数据集（如单细胞测序数据），且中期可尝试将其变分框架推广至因果推断中的高维中介模型（需进一步熟悉识别理论）。

### 2. [10.1093/biomtc/ujae057](https://doi.org/10.1093/biomtc/ujae057) · [arXiv](https://arxiv.org/abs/2210.09560) — A Bayesian convolutional neural network-based generalized linear model
- **作者**: Yeseul Jeon, Won Chang, Seonghyun Jeong, Sanghoon Han, Jaewoo Park
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在广义线性模型（GLM）框架下嵌入卷积神经网络（CNN），目标是实现既有预测精度又有可解释性的回归系数推断与不确定性量化。核心方法是将 CNN 最后一层隐藏层的节点作为 GLM 的协变量，通过 Monte Carlo dropout 生成多个特征提取实现，进而拟合集成 GLM 以捕捉特征提取过程的不确定性。技术路线结合了 Bayesian GLM、MC dropout 近似后验采样、以及 CNN 特征迁移，避开了对整个深度网络做全 Bayesian 推断的计算难题。应用于疟疾发病率、脑肿瘤图像和 fMRI 数据，展示了在高维相关输入场景下的预测与推断性能。对您而言，这是将深度学习特征与 semiparametric/Bayesian 推断结合的计算方案，可作为 stat_computing 与流行病学数据分析的交叉阅读。
- **关键技术**: `Monte Carlo dropout`, `Bayesian generalized linear model`, `CNN feature extraction`, `ensemble GLM`, `uncertainty quantification`, `transfer learning for regression`
- **为什么对您有用**: 连接到 stat_computing（数值方法与算法）和流行病学应用两个方向。技术层面，本文的 MC dropout + ensemble GLM 是一种绕过深度网络全 Bayesian 推断计算瓶颈的近似方案，与您熟悉的 semiparametric theory 和 efficiency theory 有方法论对比价值——可以思考这种近似在理论上是否达到某种最优性或效率边界。follow-up 判断：**中期可做**——您可以用 very_familiar 的软件工程能力复现并扩展，但若要从理论角度分析其推断性质（如系数估计的渐近行为、效率损失），需要在 moderately_familiar 的 semiparametric theory 上进一步投入。

### 3. [10.1093/biomtc/ujae026](https://doi.org/10.1093/biomtc/ujae026) — Well-spread samples with dynamic sample sizes
- **作者**: Blair Robertson, Chris Price, Marco Reale
- **期刊/来源**: Biometrics
- **机构**: University of Canterbury
- **分类**: vol 80 · issue 2
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 本文提出一种新的空间抽样设计方法，能够在辅助空间上生成well-spread样本，并支持动态样本量调整，适用于主抽样（master sampling）场景。该方法仅需总体单元间的距离度量，无需模型假设。数值实验表明，该方法生成的样本具有良好的空间平衡性，与现有设计相比有竞争力。应用示例使用多个辅助变量估计巴西亚马逊东部的地上生物量总量，也展示了多目标调查（同时估计地上生物量、初级生产力和粘土含量三个响应变量）的效果。该方法作为一种通用的抽样算法，设计简洁且易于实现，为统计计算中的空间抽样提供了新工具。对您有用：该方法直接丰富了您统计计算兴趣中的算法工具箱，尤其适合在需要高效空间抽样的应用场景中参考。
- **关键技术**: `spatial sampling design`, `well-spread sampling`, `master sampling`, `distance measure`, `auxiliary space`, `multipurpose surveys`
- **为什么对您有用**: 本文直接对应您统计计算（numerical methods, algorithm）的兴趣，提出了一种新的抽样算法，设计简洁且可应用，是立即可做的glance-read。您的technical arsenal中的"software development"和"nonparametric statistics"足以理解其方法并进行数值比较。该文不涉及因果推断或高维统计，但作为算法设计论文，属于轻松阅读，无需额外工具。

## 流行病学  *(epidemiology, 5 篇)*

### 1. [10.1093/biomtc/ujae048](https://doi.org/10.1093/biomtc/ujae048) — A Bayesian semi-parametric model for learning biomarker trajectories and changepoints in the preclinical phase of Alzheimer’s disease
- **作者**: Kunbo Wang, William Hua, MeiCheng Wang, Yanxun Xu
- **期刊/来源**: Biometrics
- **机构**: Johns Hopkins University
- **分类**: vol 80 · issue 2
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文研究阿尔茨海默病（AD）临床前阶段生物标志物的纵向轨迹和变点，目标是建模生物标志物在症状出现前的转折点及其时间分布。作者提出贝叶斯半参数框架，联合建模生物标志物的纵向变化与症状发生时间的变点，其中症状时间受左截断和右删失，且人群中部分个体可能永不发病（治愈分数）。模型采用样条基函数刻画轨迹形状，并引入贝叶斯先验推断变点位置和个体易感性。通过模拟验证方法表现，并应用于BIOCARD研究中ptau181生物标志物数据，展示了在真实复杂纵向数据中的可行性。本文为流行病学中疾病进程建模提供了半参数贝叶斯工具，尤其适合处理删失、异质性和非渐近人群，对您的流行病学数据分析有直接参考价值。
- **关键技术**: `Bayesian semiparametric model`, `changepoint detection`, `left truncation and right censoring`, `cure fraction (susceptibility) model`, `joint longitudinal-survival model`, `MCMC inference`
- **为什么对您有用**: 本文连接您的二级兴趣流行病学（AD生物标志物数据应用），武器库中的semiparametric theory可理解其半参数部分，但贝叶斯推断（MCMC）需额外熟悉。中期可做：在semiparametric theory（moderately_familiar）上深入，可尝试将其变点估计移植到频率学派框架或改进瓶颈估计。

### 2. [10.1093/biomtc/ujae019](https://doi.org/10.1093/biomtc/ujae019) · [arXiv](https://arxiv.org/abs/2305.05913) — Case weighted power priors for hybrid control analyses with time-to-event data
- **作者**: Evan Kwiatkowski, Jiawen Zhu, Xiao Li, Herbert Pang, Grazyna Lieberman, Matthew A Psioda
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 该文提出在随机对照试验中利用外部对照数据增强内部对照组的方法，核心是扩展贝叶斯 power prior，使每个外部对照的折扣权重基于其与 RCT 数据的兼容性动态决定。兼容性通过从 RCT 后验预测分布中评估外部对照的似然来量化，模型采用分段常数基线风险的比例风险回归。模拟和真实数据（非小细胞肺癌试验）表明，该方法在外部对照与 RCT 人群存在系统性差异（如未测量混杂）时仍能提供稳健的推断。该方法为贝叶斯动态借用提供了新的个体加权框架，避免了传统全局借用方法的风险。对您而言，该文属于流行病学应用中的外部数据整合问题，与您在因果推断中处理未测量混杂的 sensitivity analysis 可形成互补——您熟悉的非参数统计和逆问题理论可用于分析其加权方案的稳健性条件。目前核心机器基于贝叶斯，您的武器库中贝叶斯工具不突出，属中期可做：需先掌握 power prior 和 dynamic borrowing 的贝叶斯推断框架。
- **关键技术**: `power prior`, `case-weighting`, `external control borrowing`, `piecewise constant baseline hazard`, `proportional hazards model`, `predictive distribution`
- **为什么对您有用**: 该文属于流行病学应用中的外部数据借用方向，与您对因果推断中未测量混杂和外部效度的兴趣直接相关。您可借鉴其个体兼容性评估思路来改进自己的 proximal causal inference 框架中的 negative control 选择，但需要先补贝叶斯动态借用的技术细节（因您的武器库主要侧重频率学派/半参方法），属中期可做。

### 3. [10.1093/biomtc/ujae038](https://doi.org/10.1093/biomtc/ujae038) · [arXiv](https://arxiv.org/abs/2304.01912) — Bayesian meta-analysis of penetrance for cancer risk
- **作者**: Thanthirige Lakshika M Ruberu, Danielle Braun, Giovanni Parmigiani, Swati Biswas
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出一种贝叶斯层次随机效应元分析方法，用于整合多项研究中的癌症遗传风险渗透率估计。多基因面板检测广泛使用后，需要准确的年龄特异性癌症风险来指导患者管理，而各研究报告的风险度量类型不同（渗透率、相对风险、比值比）。该方法通过贝叶斯层次模型统一融合不同度量，并利用MCMC算法估计参数后验分布，进而得到渗透率及其可信区间。模拟研究以ATM和PALB2两个中风险乳腺癌易感基因为例，结果显示新方法在覆盖概率和均方误差上显著优于现有方法。最后应用于ATM基因致病突变携带者的乳腺癌渗透率估计。本文的方法为流行病学中证据整合提供了实用工具，其贝叶斯框架也可推广到因果推断的敏感性分析或多种证据源的结合。
- **关键技术**: `Bayesian hierarchical random-effects model`, `meta-analysis`, `Markov chain Monte Carlo`, `penetrance estimation`, `credible interval`
- **为什么对您有用**: 本文属于流行病学应用，紧密连接研究者的次要兴趣——流行病学实际数据集和模型。研究者若关注因果推断中的证据整合（如多种研究设计的敏感性分析），本文的贝叶斯层次元分析方法可提供借鉴。武器库中的统计计算与软件开发经验能支撑复现其MCMC实现，但贝叶斯层次模型目前不在核心工具集中，需先熟悉MCMC和随机效应模型的细节。初步判断：暂不可做（需先补齐贝叶斯层次模型基础），但作为流行病学元分析的入门读物值得一读。

### 4. [10.1093/biomtc/ujae029](https://doi.org/10.1093/biomtc/ujae029) — Addressing age measurement errors in fish growth estimation from length-stratified samples
- **作者**: Nan Zheng, Atefeh Kheirollahi, Yildiz Yilmaz
- **期刊/来源**: Biometrics
- **机构**: Memorial University of Newfoundland
- **分类**: vol 80 · issue 2
- 相关性 1/10 · novelty: `application`
- **摘要**: 本文针对鱼类生长模型中年龄测量误差（ME）及长度分层年龄抽样（LSAS）的双重挑战，提出了一套统计方法。采用的工具包括：经验比例似然（empirical proportion likelihood）处理 LSAS 的选择性抽样，结构误差变量（structural errors-in-variables）处理年龄 ME，并用 continuation ratio-logit 模型刻画真实年龄分布。对年龄和长度分布实施离散化处理，大幅提升了计算效率。模拟表明，即使年龄 ME 较小，忽略它也会导致生长参数估计严重偏倚；而新方法在不同 ME 幅度下均表现稳健，且能准确估计标准误。真实数据分析和模型验证工具进一步展示了实用性。对您而言，本文虽非因果推断或高维方法，但测量误差与抽样偏差协整处理的技术思路可迁移至流行病学队列中的类似问题（如年龄误报、选择偏倚），且软件实现降低了门槛。
- **关键技术**: `empirical proportion likelihood`, `structural errors-in-variables`, `continuation ratio-logit model`, `response-selective sampling`, `two-phase sampling`
- **为什么对您有用**: 连接您的次要兴趣——流行病学的应用数据集和测量误差问题。武器库中'逆问题中的随机噪声'可类比本文的测量误差建模思路，'非参数统计'可用于扩展其模型假设的稳健性。中期可做：若想将本文方法迁移至因果推断中的测量误差体检验，需先熟悉 moderately_familiar 中的'因果推断识别理论'。

### 5. [10.1093/biomtc/ujae034](https://doi.org/10.1093/biomtc/ujae034) — Data science for infectious disease data analytics: an introduction with R, by Lily Wang, CRC Press, 2022 ISBN-13: 978-1032187426, https://www.routledge.com/Data-Science-for-Infectious-Disease-Data-Analytics-An-Introduction-with-R/Wang/p/book/9781032187426
- **作者**: Gillian Cheng, Andrei R Akhmetzhanov
- **期刊/来源**: Biometrics
- **机构**: National Taiwan University
- **分类**: vol 80 · issue 2
- 相关性 0/10 · novelty: `survey`
- **摘要**: 这是一篇书评，介绍 Lily Wang 2022 年出版的《Data Science for Infectious Disease Data Analytics: An Introduction with R》。该书面向传染病数据分析的入门读者，涵盖数据清洗、可视化、统计建模与机器学习方法，并配有 R 代码实现。内容涉及传播动力学模型、时空分析、聚类与分类等流行病学常用工具，适合作为应用统计学家进入传染病数据领域的入门读物。书评作者认为本书实用性强、代码可复现性高，但理论深度有限，不涉及前沿因果推断或高维统计方法。对您而言，本书可作为流行病学数据分析的 gateway reading，帮助了解该领域的数据结构与常见建模范式。
- **关键技术**: `R programming`, `infectious disease modeling`, `spatial-temporal analysis`, `data visualization`, `classification and clustering`
- **为什么对您有用**: (1) 本文属于流行病学方向的 gateway reading，书评明确指出该书适合入门、代码可复现，但缺乏理论深度；(2) 研究者的武器库（软件工程、因果推断估计理论）足以支撑进入该方向，但若想做方法学贡献需自行带入因果推断或高维工具；(3) 值得花时间浏览目录和代码示例，但不建议精读全书——更适合作为了解传染病数据结构的参考。

## 其他  *(other, 3 篇)*

### 1. [10.1093/biomtc/ujae017](https://doi.org/10.1093/biomtc/ujae017) · [arXiv](https://arxiv.org/abs/2106.03811) — Estimating the size of a closed population by modeling latent and observed heterogeneity
- **作者**: Francesco Bartolucci, Antonio Forcina
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文在 capture-recapture 闭群体规模估计问题中，将 Liu et al. 的经验似然方法扩展至允许潜在类别、协变量及序列依赖的灵活模型族。核心估计量通过 Fisher-scoring 算法实现 MLE，并提出一种比传统 EL 更高效的替代方法估计非参数成分，证明了协变量非参数分布与"从未被捕获概率"之间的映射是一对一且严格单调的。理论方面给出了渐近结果概述及 population size 的 profile likelihood 置信区间构造方法。模拟显示在估计整体漏计数时，该方法相比条件 MLE 有显著效率提升，尤其在小样本情形。对您而言，这是流行病学监测场景下的应用方法论文，技术核心是有限样本效率改进而非新理论框架。
- ⚠️ *摘要不完整，待重跑（`python -m research_news.rerun`）*
- **关键技术**: `empirical likelihood`, `latent class model`, `capture-recapture`, `profile likelihood confidence interval`, `Fisher-scoring algorithm`
- **为什么对您有用**: 本文属于流行病学监测数据的应用方法，涉及 capture-recapture 这一经典框架，但技术核心是有限样本效率改进而非 identification 或 semiparametric efficiency bound 的新理论。您武器库中的 semiparametric theory 和 M-estimation theory 足以理解全文技术细节，但论文未触及您 primary interest 的核心问题（如 efficiency bound 计算、debiasing、高维设定）。判断为**暂不可做**：没有明显的理论延伸口子，除非您想将 HOIF 或 sharper efficiency theory 引入 capture-recapture 的非参数成分估计——这需要先确认该领域是否已有类似工作。

### 2. [10.1093/biomtc/ujae030](https://doi.org/10.1093/biomtc/ujae030) · [arXiv](https://arxiv.org/abs/2212.14567) — Topical hidden genome: discovering latent cancer mutational topics using a Bayesian multilevel context-learning approach
- **作者**: Saptarshi Chakraborty, Zoe Guan, Colin B Begg, Ronglai Shen
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文研究癌症基因组学中超罕见体细胞突变的癌症类型特异性推断问题，目标是对数百万级别变异、数千肿瘤样本进行统计建模与预测。核心方法是贝叶斯多层 multilogistic 回归模型，结合 topic model（LDA 思想）对 mutation contexts 进行降维，生成可解释、去相关的 meta-feature topics。估计方面设计了高效的 MCMC 算法实现 full Bayesian inference，可处理数千万变异规模，远超现有高维多类回归方法的计算能力。理论层面未给出收敛率或后验一致性结果，主要贡献在于计算可扩展性与生物学发现。实证分析基于 Pan Cancer Analysis of Whole Genomes 数据集，揭示了与 UV 暴露、衰老、表观基因组组织相关的突变主题，预测性能与随机森林、深度学习方法相当。对您而言，这是生物统计应用类工作，方法学 novelty 有限。
- **关键技术**: `Bayesian multilevel multilogistic regression`, `topic model / LDA for dimension reduction`, `MCMC algorithm for high-dimensional posterior`, `mutation context meta-features`, `full Bayesian inference at scale`
- **为什么对您有用**: 本文属于生物统计应用，与您 primary interests（因果推断、高维 RMT、半参数效率、U-statistics）无直接方法学重叠。技术层面是 topic model + 高维贝叶斯回归，不涉及 semiparametric efficiency bound、debiasing、或 RMT 工具。武器库中 very_familiar 的 minimax bounds、higher-order U-statistics、semiparametric theory 均无法直接迁移至此问题。核心 MCMC / topic model 机器不在您的武器库中，属于暂不可做——若要进入此方向，需先补充贝叶斯计算与 topic model 理论基础。

### 3. [10.1093/biomtc/ujae053](https://doi.org/10.1093/biomtc/ujae053) — Introduction to statistical modelling and inference by Murray Aitkin, CRC Press, 2023, ISBN: 978-1032105710, https://www.routledge.com/Introduction-to-Statistical-Modelling-and-Inference/Aitkin/p/book/9781032105710
- **作者**: Chuhsing Kate Hsiao
- **期刊/来源**: Biometrics
- **机构**: National Taiwan University
- **分类**: vol 80 · issue 2
- 相关性 0/10 · novelty: `survey`
- **摘要**: 这是一本关于统计建模与推断的入门教材，由Murray Aitkin撰写，2023年由CRC Press出版。书中系统介绍了从概率模型到似然推断的核心内容，覆盖频率学派和贝叶斯方法。重点包括模型构建、假设检验、模型选择以及计算实现，并配有R代码示例。本书适合作为统计专业高年级本科生或研究生的教材，也可供实践者参考。对于已熟悉高等统计理论的研究者，本书可作为基础知识的快速回顾。
- **关键技术**: `likelihood inference`, `model selection (AIC/BIC)`, `Bayesian inference`
- **为什么对您有用**: 本书作为一本统计推断的综合性教材，与研究者'数学统计与假设检验'的基础兴趣间接相关，但内容较为初级，不会直接推进当前研究方向。立即可做的是快速浏览书中对似然推断和模型选择的讲解，以巩固基础，但无需投入大量时间。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

