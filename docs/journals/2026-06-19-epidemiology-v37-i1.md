# Epidemiology — Vol 37  Issue 1  ·  2026-06-19

- 共 17 篇 · Epidemiology
- 目录核对 ⚠️ 疑似漏 4 篇（对照 OpenAlex 23 篇）：10.1097/ede.0000000000001910、10.1097/ede.0000000000001909、10.1097/ede.0000000000001928、10.1097/ede.0000000000001929

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期内容主要围绕因果推断的识别与稳健估计、偏倚校正与敏感性分析两条方法论主线，以及流行病学应用中的测量误差与数据链接问题展开。因果主线涵盖了中介分析、未控制混杂与正定性违反、试验外推、检验阴性设计及空间双重差分等六篇论文；偏倚与敏感性主线聚焦于选择偏倚、未测量混杂界与依从性中介；应用主线则处理了测量误差参数迁移、时间聚合数据纠偏及数据链接验证等具体场景。

因果识别与稳健估计主线在本期推进了多个复杂设定下的效应定义与双重稳健（DR）估计。针对受暴露影响的中间混杂，广义自然间接效应一文引入中介解释判据，在比非参数SEM更弱的假设下实现了等价于干预间接效应的识别；针对未控制混杂，双重稳健COCA一文将负对照设计扩展至条件效应与异质性刻画，在暴露与焦点结果模型同时正确时保持一致；在检验阴性设计（TND）中，疫苗效果一文提出优势比等混杂假设以提供因果理论依据，并给出DR半参数估计量及偏离时的敏感性分析；空间双重差分一文则结合贝叶斯疾病映射与双向Mundlak机制，通过INLA计算在小区域评估中纳入时空随机效应。

偏倚校正与敏感性分析主线集中处理了观察性研究中不可识别部分的参数化与界收紧。选择偏倚G-computation一文将识别结果转化为stacked estimating equations以统一推导与实现；未测量混杂边际界一文将条件E-value扩展至边际效应，仅需指定敏感性参数最大值以降低维度并收紧界；试验外推一文针对参与影响依从性的不可识别问题，引入相对依从性差异参数构建了基于influence function的DR one-step估计器；抗菌药物间接效应一文系统梳理了干扰设定下的因果框架，厘清了抗生素与疫苗在干扰结构上的差异。

关注因果推断与半参数效率的读者，建议优先看广义自然间接效应、双重稳健COCA、TND疫苗效果及试验外推四篇，它们均涉及复杂识别假设下的DR或半参数估计量推导；关注高维与计算方法的读者可留意空间双重差分中的INLA实现；关注偏倚与敏感性分析的读者则可直接参阅边际界与选择偏倚G-computation。

## 因果推断  *(causal_inference, 7 篇)*

### 1. [10.1097/ede.0000000000001922](https://doi.org/10.1097/ede.0000000000001922) — Causal Mediation Analysis with Mediator-outcome Confounders Affected by Exposure: On Definition and Identification of Generalized Natural Indirect Effect
- **作者**: Yan-Lin Chen, Tsung Yu, Sheng-Hsuan Lin
- **期刊/来源**: Epidemiology
- **机构**: National Yang Ming Chiao Tung University · National Cheng Kung University · National Dong Hwa University
- **分类**: vol 37 · issue 1 · pp 21-29
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在因果中介分析中，当存在受暴露影响的中介-结局混杂（intermediate confounders）时，传统自然间接效应（NIE）在非参数结构方程模型（SEM）下不可识别。本文引入一类广义自然间接效应（generalized NIE），其中一种通过随机干预定义的特例与非参数SEM下的interventional indirect effect（IIE）等价，但识别假设更弱。作者提出新的间接效应判据（mediator interpretability criteria），确保在中间混杂存在时仍能维持有效的中介解释；IIE不满足该判据，而所有广义NIE均满足。在额外无异质性假设下，NIE等于该广义NIE从而变得可识别，为流行病学研究中不可避免中间混杂的场景提供了更实用的替代度量。本文的方法贡献在于放宽了识别条件并给出新的定义框架，拓展了中介分析的理论基础。对您而言，本文是因果推断中中介分析的重要进展，直接适用于流行病学队列研究中的效应分解问题。
- **关键技术**: `causal mediation analysis`, `generalized natural indirect effect`, `interventional indirect effect`, `cross-world assumptions`, `intermediate confounders`, `identification theory`
- **为什么对您有用**: 本文直接关联因果推断中的中介分析子方向，特别是受暴露影响的中间混杂下的效应分解问题。您非常熟悉的identification theory可用于评估本文识别假设的完整性与可放松性；非参数统计知识则可用于构造相应估计量。这是立即可做的问题：您可直接基于本文定义推导半参数效率界，或将其整合进现有的中介分析研究框架。

### 2. [10.1097/ede.0000000000001907](https://doi.org/10.1097/ede.0000000000001907) — Doubly Robust Control Outcome Calibration Approach Estimation of Conditional Effects with Uncontrolled Confounding
- **作者**: Wen Wei Loh
- **期刊/来源**: Epidemiology
- **机构**: Maastricht University
- **分类**: vol 37 · issue 1 · pp 98-106
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文在存在未控制混淆的条件下，针对条件因果效应（包括效应修饰）的估计问题，提出了一种双重稳健的控制结果校准（Doubly Robust COCA）估计量。现有COCA方法依赖负对照结果模型的正确设定，而新方法通过同时正确指定暴露模型和焦点结果模型，即可在负对照模型误设时仍得到一致估计。该估计量具有闭式解，计算简便，且允许协变量与暴露的交互项进入模型以刻画异质性效应。通过数值模拟验证了有限样本下的无偏性与推断准确性，并利用公开数据集评估了志愿服务对心理健康的影响。对于您的proximal CI研究中涉及的负对照假设与敏感性分析，该方法提供了可直接实现的双重稳健扩展，尤其适用于流行病学或经济学中利用负对照结果的因果识别场景。
- **关键技术**: `doubly robust estimation`, `control outcome calibration approach (COCA)`, `negative control outcomes`, `effect modification`, `uncontrolled confounding`
- **为什么对您有用**: 本文直接涉及您primary interest中的proximal causal inference方向——利用负对照结果（negative control outcomes）在未控制混淆下识别因果效应，是敏感性分析的具体工具。您非常熟悉的causal inference估计理论（特别是双重稳健框架）足以支撑您快速理解其假设与识别策略，并可进一步尝试将其推广至更复杂的纵向或工具变量设定。立即可做：您现有的估计理论工具可直接验证该方法的双稳健性条件，或将其与您熟悉的交叉拟合、高效影响函数结合以提升效率。

### 3. [10.1097/ede.0000000000001924](https://doi.org/10.1097/ede.0000000000001924) — Causal Identification Conditions for the Effect of Treatment in the Treated: Illustration Using the Northwest Germany Stroke Registry
- **作者**: Catherine Wiener, Paul N. Zivich, Tobias Kurth, Michele Jonsson-Funk, Alexander Breskin, Klaus Berger et al.
- **期刊/来源**: Epidemiology
- **机构**: University of North Carolina at Chapel Hill · House of Representatives · Charité - Universitätsmedizin Berlin · Regeneron (United States) · University of Münster
- **分类**: vol 37 · issue 1 · pp 57-66
- 相关性 8/10 · novelty: `application`
- **摘要**: 比较平均处理效应(ATE)与处理组平均处理效应(ATT)在观察性研究中的识别条件。ATE需满足正定性（positivity）在两组均成立，而ATT只需处理组满足正定性，放松了对对照组的对称性要求。方法上，分别用逆概率加权（IPTW）估计ATE、用标准化死亡比加权（SMR weighting）估计ATT，并在德国西北中风登记数据（2020-2021）中应用，评估组织型纤溶酶原激活剂(tPA)对院内死亡率的影响。模拟研究（5000次，6000例）设定均质与非均质处理效应，并构造对照组正定性违反和两组均满足两种场景。结果表明：当对照组存在正定性违反时，ATE估计的log尺度偏差随违反程度增大（均质：0.2–1.1，非均质：0.2–0.9），而ATT估计仍保持无偏。实际数据中ATE风险比为1.70（95%CI: 0.80–3.64，暗示有害），而ATT风险比为0.82（0.59–1.14，暗示保护）。该文清晰展示了在正定性违反的常见场景下，ATT识别条件的优越性。对您而言，这与因果推断中识别条件的研究直接相关，尤其关于弱化假设时的估计稳健性，是sensitivity analysis和IV方法中值得关注的实证案例。
- **关键技术**: `Inverse probability of treatment weighting (IPTW)`, `Standardized mortality ratio (SMR) weighting`, `Positivity assumption`, `Average treatment effect in the treated (ATT)`, `Simulation-based bias assessment`
- **为什么对您有用**: 直接关联primary interest中的因果推断识别理论，特别是ATT相比于ATE的弱识别条件及其在正定性违反中的稳健性。研究者对estimation theory in causal inference非常熟悉，因此可以立即理解并评估该文的加权估计逻辑与偏倚模拟设计。属于立即可做的阅读与借鉴——可将类似的识别条件对比延伸到proximal causal inference或IV中的对照依从性问题上。

### 4. [10.1097/ede.0000000000001919](https://doi.org/10.1097/ede.0000000000001919) — Bounds and E-values for Marginal Causal Effects
- **作者**: Arvid Sjölander, Iuliana Ciocănea-Teodorescu, Erin E. Gabriel
- **期刊/来源**: Epidemiology
- **机构**: Karolinska Institutet · Carol Davila University of Medicine and Pharmacy · Institutul National Victor Babes · University of Copenhagen
- **分类**: vol 37 · issue 1 · pp 5-15
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 该文关注观察性研究中未测量混杂对边际因果效应的影响。现有 Ding-VanderWeele 界适用于条件因果效应，扩展至边际效应时需在每个测量混杂水平上指定敏感性参数，维度高且保守性强。本文提出新界，仅需指定所有测量混杂水平上敏感性参数的最大值，大幅降低维度，且界通常更窄。新界自然转化为边际因果效应的 E-value，使研究者能更直接地评估未测量混杂对边际因果结论的威胁。作者基于标准回归技术给出估计量，并通过公开数据演示，提供完整 R 代码。对于流行病学应用中常见的边际因果问题，该工具比旧有方法更易实现且更灵敏，适合作为敏感性分析的常规输出。
- **关键技术**: `E-value`, `Ding-VanderWeele bounds`, `marginal causal effect`, `sensitivity analysis`, `regression-based estimation`
- **为什么对您有用**: 本文直接服务于流行病学中的因果推断敏感性分析，与您二级兴趣 'epidemiology' 及一级兴趣 'causal inference (sensitivity analysis)' 高度吻合。方法上，您 'very_familiar' 的 'estimation theory in causal inference' 和 'minimax bounds for estimation problems' 可立即用于评估该界的紧致性（是否可进一步收紧），或将其思想推广至更复杂的 estimand（如 mediation）。**立即可做**：用您熟知的非参数估计或正交化技巧改进该界在有限样本下的偏差-方差权衡。

### 5. [10.1097/ede.0000000000001925](https://doi.org/10.1097/ede.0000000000001925) · [arXiv](https://arxiv.org/abs/2506.00157) — Transporting Results from a Trial to an External Target Population When Trial Participation Impacts Adherence
- **作者**: Rachael K. Ross, Iván Díaz, Amy J. Pitts, Elizabeth A. Stuart, Kara E. Rudolph
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1 · pp 39-49
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在试验结果向外部目标人群外推（transportability）的设定下，当试验参与本身通过依从性（adherence）中介影响结局时，目标人群的潜在结局均值（estimand）因缺乏真实世界的治疗与依从性数据而不可识别。本文提出一种敏感性分析框架，引入刻画试验与目标人群间依从性相对差异（可条件于协变量）的敏感性参数，并讨论基于外部知识设定参数范围或 Monte Carlo 抽样的策略。作者构造了两个估计器：plug-in 估计器与基于 influence function 的 one-step 估计器，后者具有双重稳健性并支持用机器学习估计 nuisance 函数。在阿片类药物使用障碍治疗的真实数据应用中，将两种用药下的复发风险从试验外推至真实人群。对您可能有用：本文将中介差异纳入外推敏感性分析的思路，可补充 proximal CI 或 longitudinal mediation 中处理 unmeasured mediator 的工具箱。
- **关键技术**: `transportability / generalizability`, `sensitivity analysis for unmeasured mediator`, `one-step estimator`, `double robustness`, `Monte Carlo sensitivity parameter sampling`
- **为什么对您有用**: 直接连接因果推断中的 transportability 与 sensitivity analysis 子方向，处理 trial participation 通过 adherence 产生中介效应的不可识别问题；one-step / DR 估计器与您 efficiency theory 武器库中的 influence function 构造直接对接，可用 semiparametric efficiency bound 验证其 DR 估计器是否达到局部效率。立即可做：用 very_familiar 的 estimation theory in causal inference 与 moderately_familiar 的 semiparametric theory 推导该 estimand 的效率界并检查 one-step 估计器的效率性质。

### 6. [10.1097/ede.0000000000001926](https://doi.org/10.1097/ede.0000000000001926) · [arXiv](https://arxiv.org/abs/2504.20360) — Identification and Estimation of Vaccine Effectiveness in the Test-Negative Design Under Equi-confounding
- **作者**: Christopher B. Boyer, Kendrick Qijun Li, Xu Shi, Eric J. Tchetgen Tchetgen
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1 · pp 77-87
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文聚焦于检验阴性设计（TND）中疫苗效果的识别与估计问题。传统上TND被认为能减少未测量健康寻求行为的混杂，但缺乏基于潜在结果的严格形式化。作者提出优势比等混杂（odds ratio equi-confounding）假设，在该假设下，未测量混杂对检测阳性和阴性个体的影响在优势比尺度上等价，从而为TND的因果解释提供了理论依据。在识别基础上，给出了在等混杂假设下接种者边际风险比的估计量，包括结果模型、逆概率加权以及双稳健半参数估计量，并证明了后者的双重稳健性质。当等混杂不成立时，设计了参数化偏离程度的敏感性分析方法。模拟研究在多种场景下验证了所提估计量的有限样本表现。该工作为流行病学疫苗效果评估提供了更严格的因果推断框架，连接了研究者对因果推断识别理论与流行病学应用的兴趣。
- **关键技术**: `test-negative design`, `odds ratio equi-confounding`, `doubly robust estimator`, `inverse probability weighting`, `semiparametric estimator`, `sensitivity analysis`
- **为什么对您有用**: 本文直接回应了研究者对流行病学中因果推断（尤其是疫苗效果估计）的应用兴趣，其核心识别条件与估计框架属于identification theory in causal inference的典型范例。研究者可用very_familiar中的estimation theory in causal inference对双稳健估计量的效率进行深入评估，也可借助moderately_familiar中的semiparametric theory进一步拓展至更复杂的纵向或IV设定。基于现有武器库，本文所涉方法的理解与改进可立即可做（无需额外工具）。

### 7. [10.1097/ede.0000000000001912](https://doi.org/10.1097/ede.0000000000001912) — Spatial Difference-in-Differences with Bayesian Disease Mapping Models
- **作者**: Carl Bonander, Marta Blangiardo, Ulf Strömberg
- **期刊/来源**: Epidemiology
- **机构**: Karlstad University · University of Gothenburg · Imperial College London
- **分类**: vol 37 · issue 1 · pp 30-38
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本研究将贝叶斯疾病映射模型与双重差分（DID）方法结合，旨在解决小区域流行病学评估中空间相关性被忽视的问题。方法上采用基于插补的DID框架，利用双向Mundlak估计实现与固定效应DID等价的因果识别，同时通过时空随机效应捕捉空间与时间结构。使用集成嵌套拉普拉斯近似（INLA）进行高效贝叶斯计算，可灵活指定空间和时间效应。模拟结果表明，在时空结构正确设定的情况下，该方法在参数估计精度和区间覆盖率上均优于标准DID方法。文章以瑞典市镇冰爪分发项目为例展示了实际应用。对您而言，该工作直接连接了次级兴趣中的流行病学因果推断应用，您可以用estimation theory in causal inference分析其识别假设的合理性，并利用software development经验复现或扩展其计算实现。
- **关键技术**: `Difference-in-Differences`, `Bayesian disease mapping`, `Integrated Nested Laplace Approximation`, `imputation-based DID`, `two-way Mundlak estimation`, `spatiotemporal random effects`
- **为什么对您有用**: 该论文属于流行病学中因果推断的应用，与您的secondary interest（流行病学、因果推断DID方法）高度相关。您武器库中的estimation theory in causal inference可以直接分析其识别假设（如平行趋势在空间平滑下的含义），而software development技能可用来复现INLA实现并结合自己的因果推断软件包扩展。整体而言，立即可做：您已掌握理解其方法论所需的核心工具。

## 流行病学  *(epidemiology, 10 篇)*

### 1. [10.1097/ede.0000000000001916](https://doi.org/10.1097/ede.0000000000001916) · [arXiv](https://arxiv.org/abs/2506.03347) — Constructing G-computation Estimators: Two Case Studies in Selection Bias
- **作者**: Paul N Zivich, Haidong Lu
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1 · pp 50-56
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文在流行病学选择偏倚框架下，针对 treatment-induced selection 与缺乏联合调整集的共发偏倚两种复杂因果结构，探讨如何将 identification 结果转化为 G-computation 估计量。核心机制是将 G-computation 参数化为 stacked estimating equations，从而统一理论推导与软件实现，并通过模拟展示有限样本性质。该方法本质上利用了参数化 g-formula 的 M-estimation 结构，便于推导 influence function 与进行 sandwich variance 估计。主要结果为两种偏倚场景下提供了具体的参数化估计策略与模拟验证。对您可能有用：本文展示了从 DAG identification 到 M-estimation 实现的完整路径，可直接迁移到您因果推断 identification theory 的研究流程中。
- **关键技术**: `G-computation`, `stacked estimating equations`, `M-estimation`, `selection bias`, `treatment-induced selection`
- **为什么对您有用**: (1) 连接到流行病学因果推断的应用场景（选择偏倚的 identification 与 estimation），属于 secondary interest 中的 epidemiology；(2) 本文的 stacked estimating equations 视角与您 moderately_familiar 中的 M-estimation theory 直接对接，可用 M-estimation 理论分析其 estimator 的渐近性质与效率；(3) **立即可做**：用 very_familiar 的软件开发能力将 stacked estimating equations 实现为开源 Python/R 包，并用 moderately_familiar 的 semiparametric theory 探讨这些参数化估计量的 semiparametric efficiency bound 是否可达。

### 2. [10.1097/ede.0000000000001921](https://doi.org/10.1097/ede.0000000000001921) — How Should We Study the Indirect Effects of Antimicrobial Treatment Strategies?: A Causal Perspective
- **作者**: Juan Gago, Christopher Boyer, Marc Lipsitch
- **期刊/来源**: Epidemiology
- **机构**: Harvard University · Cleveland Clinic · Case Western Reserve University
- **分类**: vol 37 · issue 1 · pp 88-97
- 相关性 8/10 · novelty: `survey`
- **摘要**: 本文研究抗菌药物管理策略中直接效应与间接效应（如耐药菌传播导致的个体间干扰）的因果评估问题，目标 estimand 为不同治疗策略下的直接与间接因果效应对比。核心难点在于抗生素干预的间接危害具有扩散性且难以测量，而现有处理干扰的因果框架（如疫苗研究中的两阶段随机化设计）因干预机制本质差异无法直接移植。作者系统回顾了适用于干扰设定的因果识别框架与实验设计，并针对抗菌药物特性提出了适配的替代方案与设计调整。主要贡献在于将流行病学中抗菌耐药的权衡评估明确纳入潜在结果框架，厘清了疫苗与抗生素在干扰结构上的关键差异。对您可能有用：本文为流行病学因果推断中的干扰（interference）设定提供了系统梳理，可直接连接到您因果推断中的 identification theory 与 longitudinal / mediation 视角。
- **关键技术**: `potential outcomes framework`, `interference and indirect effects`, `two-stage randomized design`, `causal identification under interference`, `antimicrobial stewardship trade-offs`
- **为什么对您有用**: 本文直接连接到您 secondary interest 中流行病学因果推断的应用场景，聚焦于干扰（interference）下的因果 identification 问题，这是您 moderately_familiar 中 identification theory in causal inference 的自然延伸。您可以用 very_familiar 的 estimation theory in causal inference 工具审视文中提出的识别策略是否具备可估的 semiparametric efficient estimator，或用 minimax bounds 评估间接效应估计的统计难度。**中期可做**：需先在 moderately_familiar 的 identification theory 上补充干扰设定下的 g-formula / IPW 识别条件，再切入 estimator 构造。

### 3. [10.1097/ede.0000000000001917](https://doi.org/10.1097/ede.0000000000001917) — Using Measurement Error Parameters From Validation Data
- **作者**: Rachael K. Ross, Matthew P. Fox, Catherine R. Lesko, Jacqueline E. Rudolph, Lauren C. Zalla, Jessie K. Edwards
- **期刊/来源**: Epidemiology
- **机构**: Columbia University · Boston University · Johns Hopkins University · University of North Carolina at Chapel Hill
- **分类**: vol 37 · issue 1 · pp 67-72
- 相关性 7/10 · novelty: `survey`
- **摘要**: 在流行病学测量误差校正中，目标是利用验证数据中的测量误差参数（如二分类情形下的灵敏度/特异度）将其迁移至目标样本以消除信息偏倚。本文系统梳理了迁移这些参数所需的独立性假设，并指出所需假设因参数形式不同（真实值条件于测量值 vs. 测量值条件于真实值）而异。核心机制是通过 DAG（有向无环图）来可视化并澄清迁移假设成立的条件，从而确定哪些参数可被有效迁移。该工作属于方法学框架梳理，未提出新 estimator 或收敛率理论，但为应用研究者提供了实用的 DAG 工具。对您可能有用：本文将测量误差参数的迁移问题形式化为条件独立性假设，这与因果推断中 transportability / identification 的 DAG 逻辑高度同源。
- **关键技术**: `measurement error correction`, `validation data transportability`, `conditional independence assumptions`, `DAG-based identification`, `sensitivity and specificity parameters`
- **为什么对您有用**: 本文直接连接到流行病学（secondary interest）中的测量误差与因果推断 identification 理论（primary interest）的交叉：它用 DAG 形式化测量误差参数的 transportability，逻辑上与您熟悉的 causal identification theory 完全同构。从 technical_arsenal 看，您 very_familiar 的 identification theory in causal inference 可直接攻入此文：将测量误差参数迁移视为一个 identification + transportability 问题，用您已有的 DAG 识别工具即可严格化甚至推广其假设框架。**立即可做**：用因果 identification 的形式语言重写其 transportability 条件，或将其嵌入更一般的 semiparametric measurement-error correction estimator 中推导效率界。

### 4. [10.1097/ede.0000000000001927](https://doi.org/10.1097/ede.0000000000001927) — Obesity from Childhood to Mid-adulthood in the United States: A Synthetic Cohort Approach to Measuring Health Trajectories
- **作者**: Natalia E. Poveda, Michael R. Elliott, Neil K. Mehta, Solveig A. Cunningham
- **期刊/来源**: Epidemiology
- **机构**: Pontificia Universidad Javeriana · University of Michigan · The University of Texas Medical Branch at Galveston · Emory University · Netherlands Interdisciplinary Demographic Institute
- **分类**: vol 37 · issue 1 · pp 121-131
- 相关性 5/10 · novelty: `application`
- **摘要**: 本研究利用合成队列方法，结合美国两项全国代表性纵向数据（ECLS-K 1998–1999 和 NLSY97），通过线性混合模型估计个体 BMI 轨迹，并基于轨迹匹配将年轻队列的肥胖轨迹外推至 41 岁。结果显示肥胖患病率从 4 岁时的 10.0% 上升至 41 岁时的 56.3%，在 8 岁、26 岁和 38 岁出现发病率高峰。方法学通过最大化短生命周期片段的信息来刻画长期健康动态，为缺乏长程跟踪数据的问题提供了一个实用框架。该文对您的启示：作为流行病学纵向数据分析的应用，它展示了如何融合多源数据并建模轨迹；其匹配和预测思路可与因果推断中的 g-formula 或敏感性分析结合。整体上是一篇清晰易读的入门级流行病学论文。
- **关键技术**: `Synthetic cohort`, `Linear mixed model`, `Trajectory matching`, `Longitudinal data integration`, `Body mass index projection`
- **为什么对您有用**: 本文连接研究者的 secondary interest in epidemiology，特别是纵向数据整合与肥胖轨迹建模。研究者可运用 nonparametric statistics 中的匹配偏差分析和 inverse problems 中的平滑假设检验来审视合成队列方法的外推有效性（具体口子：线性混合模型假设的检验与轨迹匹配的稳定性）。follow-up 粗判：立即可做——凭借熟练的非参数统计和因果推断训练，研究者可以立即评估其匹配策略的识别假设和预测不确定性，无需新工具。作为入门阅读，数据结构和模型清晰，值得全文阅读。

### 5. [10.1097/ede.0000000000001923](https://doi.org/10.1097/ede.0000000000001923) — Unbiased Estimates Using Temporally Aggregated Outcome Data in Time Series Analysis: Generalization to Different Outcomes, Exposures, and Types of Aggregation
- **作者**: Xavier Basagaña, Joan Ballester
- **期刊/来源**: Epidemiology
- **机构**: Universitat Pompeu Fabra · Barcelona Institute for Global Health · Centro de Investigación Biomédica en Red de Epidemiología y Salud Pública
- **分类**: vol 37 · issue 1 · pp 16-20
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究在时间序列分析中，如何利用时间聚合（temporally aggregated）的结局数据对底层 disaggregated 关联进行无偏估计，设定为环境流行病学中暴露-结局的延迟非线性模型（distributed lag nonlinear model）。核心方法基于先前提出的纠偏框架，通过构造特定聚合权重矩阵将 disaggregated 模型参数映射至聚合尺度，从而在仅观测聚合数据时恢复原始关联。模拟实验覆盖死亡率与住院结局、温度与NO2暴露、以及连续/非连续日期的三种聚合方案，结果显示在样本量充足时估计无偏，偏差与方差随聚合程度上升、随样本量下降，且在周聚合及星期混杂的空气污染模型中仍保持无偏。对您可能有用：本文提供了环境流行病学中处理聚合数据的具体纠偏策略与模拟数据集，可作为流行病学因果/关联分析中数据结构问题的入门案例。
- **关键技术**: `temporally aggregated outcome correction`, `distributed lag nonlinear model`, `aggregation weight matrix mapping`, `simulation-based bias assessment`, `time series confounding adjustment`
- **为什么对您有用**: (1) 本文属于流行病学（secondary interest）的应用方法论文，聚焦环境健康时间序列中聚合数据的纠偏估计，而非您主攻的因果 identification 或 semiparametric efficiency 理论。(2) 武器库中 minimax bounds / semiparametric theory 可用于审视该方法在强聚合下的理论极限——当前论文仅靠模拟验证无偏性，缺乏正式的 asymptotic variance 或 efficiency bound 分析，这是一个潜在的理论切入点。(3) **中期可做**：若想在此方向深入，需先在 moderately_familiar 的 semiparametric theory 上长肌肉，为聚合观测下的 partial identification / efficiency bound 建立正式框架；但作为流行病学数据结构与模型的 gateway reading，本文值得花时间读全文以了解该领域常见数据痛点。

### 6. [10.1097/ede.0000000000001908](https://doi.org/10.1097/ede.0000000000001908) — OpenSAFELY: Effectiveness of COVID-19 Vaccination in Children and Adolescents
- **作者**: Colm D. Andrews, Edward P. K. Parker, Elsie Horne, Venexia Walker, Tom Palmer, Andrea L. Schaffer et al.
- **期刊/来源**: Epidemiology
- **机构**: University of Oxford · Nuffield Health · University of London · London School of Hygiene & Tropical Medicine · University of Bristol · WPP (United Kingdom) · Harvard University
- **分类**: vol 37 · issue 1 · pp 141-151
- 相关性 5/10 · novelty: `application`
- **摘要**: 该研究利用英国OpenSAFELY-TPP电子健康记录数据，评估了BNT162b2疫苗在儿童（5-11岁）和青少年（12-15岁）中的安全性与有效性。研究采用匹配队列设计，将接种第一剂的个体与未接种对照按年龄、性别等特征匹配，以及将接种第二剂的个体与仅接种一剂的对照匹配。主要结局包括SARS-CoV-2阳性检测、COVID-19急诊就诊、住院、重症监护和死亡；安全性结局包括心包炎和心肌炎。在82万余名青少年中，第一剂疫苗在20周内将阳性检测风险降低26%（IRR=0.74），COVID-19急诊和住院风险分别降低40%和42%。第二剂进一步降低阳性检测风险33%，但对急诊就诊无额外效果；所有COVID-19相关死亡为零，重症事件极少。值得注意的是，心包炎和心肌炎仅出现在接种组，第一剂发生率为27/百万，第二剂为10/百万。研究展示了大规模真实世界观察性数据在疫苗效果评估中的应用，其匹配和分层分析策略对因果推断中的confounding控制具有借鉴意义。对您来说，这篇论文可作为流行病学领域应用因果推断的范本，其数据结构和分析管道值得关注，便于您了解该领域对ATE估计的实际操作。
- **关键技术**: `matched cohort design`, `incidence rate ratio (IRR)`, `propensity-score matching`, `electronic health record analysis`, `observational study with negative control? (not explicit)`
- **为什么对您有用**: 连接您的二级兴趣——流行病学中的应用因果推断，特别是大规模观察性疫苗效果评估。您very_familiar的causal inference estimation theory可直接用于批判其匹配和IRR估计是否达到最优（例如未使用双稳健估计），可思考是否需引入更先进的加权或IV方法。该论文安利了OpenSAFELY数据平台和分析模式，可作为流行病学数据工作的入门参考。中期可做出发点：若想深入，需在流行病学背景知识（如监测偏差、SARS-CoV-2检测策略变化）上加强，但武器库中的M-estimation和semiparametric theory已足够审读其核心分析。

### 7. [10.1097/ede.0000000000001918](https://doi.org/10.1097/ede.0000000000001918) — Pregnancy Length Measurement Error: A Comparison of Last Menstrual Period and Ultrasonography with Ovulation-based Estimation
- **作者**: Ginna L. Doss, Julie L. Daniels, Sunni L. Mumford, Charles Poole, Anne Z. Steiner, Enrique F. Schisterman et al.
- **期刊/来源**: Epidemiology
- **机构**: University of North Carolina at Chapel Hill · National Institute of Environmental Health Sciences · National Institute of Health Sciences · University of Pennsylvania · University of Utah
- **分类**: vol 37 · issue 1 · pp 107-114
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文在流行病学队列中比较了末次月经（LMP）与超声测量妊娠时长的方法学误差，以排卵日（误差≤24小时）作为金标准。基于EAGeR试验的392名单胎活产样本，同时具备前瞻性记录的LMP、排卵监测与早孕期头臀长数据，估计了不同测量方式下的妊娠时长、早产发生率及小于胎龄儿比例。核心发现：LMP倾向于高估妊娠时长（早产率0.07，灵敏度0.76），超声倾向于低估（早产率0.10，灵敏度0.94但特异度0.97），排卵金标准下早产率为0.08。作者指出这种测量误差导致的结局错分可指导未来的偏倚分析。对您可能有用：本文提供了经典测量误差导致因果结局错分的流行病学真实数据案例，适合作为偏倚分析（sensitivity analysis）方法研究的动机数据集。
- **关键技术**: `measurement error modeling`, `outcome misclassification`, `sensitivity-specificity analysis`, `gold-standard validation`, `bias analysis`
- **为什么对您有用**: 本文直接连接到流行病学因果推断中的测量误差与结局错分问题，提供了LMP/超声/排卵三种测量对比的真实数据集。您武器库中的因果推断敏感性分析（sensitivity analysis）与M-estimation理论可以直接攻入本文指出的'future bias analyses'口子——将经验性的灵敏度/特异度转化为formal的bias-model或corrected estimator。**立即可做**：用very_familiar的因果推断估计理论与sensitivity analysis框架，在该数据集上构建measurement-error-corrected的早产效应估计器。

### 8. [10.1097/ede.0000000000001915](https://doi.org/10.1097/ede.0000000000001915) — Use of Routinely Collected Data to Classify Planned Mode of Delivery Among Pregnancies With a Previous Cesarean Delivery: A Validation Study
- **作者**: Mary M. Brown, Ya-Hui Yu, Jennifer A. Hutcheon, Christy G. Woolcott, Victoria M. Allen, John Fahey et al.
- **期刊/来源**: Epidemiology
- **机构**: University of New Brunswick · Emory University · University of British Columbia · Dalhousie University · Cancer Care Nova Scotia
- **分类**: vol 37 · issue 1 · pp 115-120
- 相关性 4/10 · novelty: `application`
- **摘要**: 该研究旨在验证基于行政数据的算法是否能准确分类有剖宫产史孕妇的计划分娩方式（计划阴道分娩 vs. 计划再次剖宫产）。以加拿大新斯科舍省围产期数据库2017-2019年的记录为研究对象，对符合试产条件的既往剖宫产者应用诊断和手术编码算法，并以随机抽样的200份病历图表审查作为金标准进行比较。估算灵敏度、特异度、阳性预测值和阴性预测值，并计算95%置信区间。结果显示，算法识别计划阴道分娩的灵敏度达99%，特异度96%，阳性预测值94%，阴性预测值99%，表明基于常规收集数据的算法能够准确分类计划分娩方式。该研究为依赖类似算法的观察性研究提供了偏倚程度低的证据，对您作为统计学研究者关注流行病学实际数据分析中的测量误差和分类偏倚有直接参考价值。
- **关键技术**: `algorithm validation`, `sensitivity and specificity`, `positive/negative predictive values`, `chart review gold standard`, `administrative data classification`
- **为什么对您有用**: 本文属于流行病学应用方向的典型校准研究，验证了简单编码规则的准确性，可作为您了解流行病学中常见数据质量问题的入门读物。您的武器库中非参数统计和估计理论足以理解其逻辑，无需额外储备工具。此类研究虽方法简单，但展示了如何系统评估观察性研究中的关键变量测量误差，值得花时间阅读全文以熟悉流行病学常用验证设计。

### 9. [10.1097/ede.0000000000001914](https://doi.org/10.1097/ede.0000000000001914) — Comparative Risks of Opioid Overdose in Patients on Oxycodone Initiating Selective Serotonin Reuptake Inhibitors
- **作者**: Katsiaryna Bykov, C. Andrew Basham, Nazleen F. Khan, Robert J. Glynn, Shruti Belitkar, Seanna M. Vine et al.
- **期刊/来源**: Epidemiology
- **机构**: Brigham and Women's Hospital · Harvard University · Stanford University
- **分类**: vol 37 · issue 1 · pp 132-140
- 相关性 4/10 · novelty: `application`
- **摘要**: 本研究在已使用oxycodone的患者中，比较不同SSRI类药物引发opioid overdose的风险。基于2004-2020年美国商业和公共医疗保险索赔数据，纳入753,263名成年人，以sertraline为参照，采用倾向得分匹配权重平衡可测混杂，进而通过加权Cox比例风险模型估计风险比。结果显示citalopram、escitalopram、fluoxetine、paroxetine相比sertraline的overdose风险约高24-26%（HR 1.24-1.26），但绝对发生率较低（10.8-15.2/千人年）。本文是流行病学中标准因果推断方法的典型应用，可作为药物比较效果研究的入门范例。
- **关键技术**: `propensity score matching weights`, `weighted Cox proportional hazards model`, `large-scale claims data analysis`
- **为什么对您有用**: 本文属于secondary interest流行病学中的应用因果工作，方法标准（PS加权Cox）、数据来源和协变量描述清晰，适合作为统计学研究者进入药物比较有效性领域的入门读物。武器库中的因果推断估计理论和软件工程能力足以理解全文，无需额外工具。若有意熟悉真实世界数据下删失分析流程和倾向得分加权实践，值得花时间阅读；若仅关心方法论创新，则不必深读。

### 10. [10.1097/ede.0000000000001913](https://doi.org/10.1097/ede.0000000000001913) — Sensitivity of Cancer Registry Linkage with Missing or Incomplete Social Security Number and Implications for Cancer Cohorts
- **作者**: Lauren E. McCullough, Anusila Deka, Christina Newton, Peter Briggs, Erin Gardner, Kevin C. Ward et al.
- **期刊/来源**: Epidemiology
- **机构**: American Cancer Society · Emory University · Texas Department of State Health Services
- **分类**: vol 37 · issue 1 · pp 73-76
- 相关性 4/10 · novelty: `application`
- **摘要**: 本研究评估了社会安全号码（SSN）缺失或不完整对癌症登记链接敏感性的影响。基于癌症预防研究-3的284,361名参与者数据，使用Match*Pro软件进行概率链接，比较了完整SSN、部分SSN（后四位）和缺失SSN三种情况下的链接敏感性，并在手动审查前后分别评估。结果显示，手动审查前缺失/部分SSN的敏感性为92.5%，手动审查后分别提升至98.6%和98.8%，且按性别、年龄、种族分组的亚组敏感性均超过87%，未发现显著异质性。研究表明，在其他个人识别信息（如姓名、出生日期、地址）充分时，即使缺少完整SSN也能实现高敏感性链接。该方法学评估对设计包容性队列研究及确保数据链接质量具有重要意义，为流行病学中链接偏倚的量化提供了实证基础。
- **关键技术**: `Probabilistic record linkage`, `Match*Pro software`, `Sensitivity analysis`, `Manual review`, `Missing data`
- **为什么对您有用**: 本文是流行病学数据链接质量的应用研究，直接关联您对流行病学数据集的次要兴趣。武器库中的“estimation theory in causal inference”可用于分析链接偏误对因果效应估计的影响，但概率链接本身（如Match*Pro算法）并非您的熟悉领域。建议暂不可做，因核心记录链接工具的底层匹配规则和决策阈值需专门学习。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

