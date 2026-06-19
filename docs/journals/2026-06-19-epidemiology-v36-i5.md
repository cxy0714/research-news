# Epidemiology — Vol 36  Issue 5  ·  2026-06-19

- 共 15 篇 · Epidemiology
- 目录核对 ⚠️ 疑似漏 1 篇（对照 OpenAlex 18 篇）：10.1097/ede.0000000000001886

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

Epidemiology Vol 36 Issue 5 围绕两条主线展开：一是因果识别与中介分析的方法论推进，二是因果估计框架在实际流行病学研究中的落地应用。方法线包括三篇聚焦中介分析的论文——将可分离效应扩展至多有序中介（Definition and Interpretation of Separable Path-specific Effects With Multiple Ordered Mediators）及一篇评论（L or M 1—Critical Challenges in Mediation Analysis），以及一篇针对右删失生存数据的回归式proximal causal inference（Regression-based Proximal Causal Inference for Right-censored Time-to-event Data），后者利用负对照变量处理未测量混杂。应用线则覆盖principal stratification（Vaccine Effects on In-hospital COVID-19 Outcomes）、目标试验框架（Estimating the Effects of Lifestyle Interventions on Mortality Among Cancer Survivors）、靶向最大似然估计（Racial and Ethnic Differences …With Perinatal Health）以及一篇辅助模拟验证的蒙特卡洛积分方法（Computing True Parameter Values in Simulation Studies）。此外，本期还包含多篇流行病学方法创新与数据驱动研究，如当前状态数据非参数分析（Investigating Symptom Duration Using Current Status Data）、经验贝叶斯风险汇总（Beta Approach for Risk Summarization）、社交接触模型扩展（Improving the Use of Social Contact Studies）等。

在因果识别与中介分析这一主线上，本期显著推进了中介机制的可解释性与识别条件。多有序中介的可分离效应论文将传统依赖 cross-world 反事实的路径特定效应重新解释为若干分离组件的因果效应，并在FFRCISTG模型下将个体级隔离假设弱化为总体级隔离，使识别假设有可能在未来实验中得到验证；同时，该框架提供了检测中介间混杂与因果序错设的工具。伴随的评论文章则横向对比了natural/interventional/separable三种estimand在识别假设不可检验性上的差异，强调中介分析的实质挑战在于 cross-world 独立性假设而非估计效率。proximal causal inference文章则将未测量混杂的代理变量方法推广至加法风险模型下的右删失结局，分别处理连续、计数和右删失三种负对照结局类型，给出识别条件与一致性证明，并在SUPPORT数据中实证展示其对右心导管置入效应的校正效果。这些工作共同围绕着如何在不依赖不可验证假设的前提下，从观察数据中分离更可靠的因果解释。

在因果估计框架的应用主线中，几个实例展示了不同识别策略在具体问题中的操作化。principal stratification论文证明，仅对“无论是否接种都会住院”的子群才能定义疫苗因果效应，并给出可操作的敏感性分析流程。目标试验框架论文则系统化地将观察性数据仿制为指定干预方案，并在癌症幸存者中估计生活方式干预的死亡率效应，同时提供修改方案以探索未测量混杂的敏感性。TMLE应用在围产期健康数据中评估了SARS-CoV-2感染和疫情时期对不同种族/族裔群体的边际风险差异。蒙特卡洛积分方法则为模拟研究中解析困难的真值计算提供了通用方案，并附有R代码，特别适用于时变混杂等复杂场景。这些文章不引入新理论，但为因果推断在流行病学中的落地提供了稳健的范例。

若从因果推断与半参数效率角度优先阅读，建议重点关注Regression-based Proximal Causal Inference for Right-censored Time-to-event Data、Definition and Interpretation of Separable Path-specific Effects With Multiple Ordered Mediators、L or M 1—Critical Challenges in Mediation Analysis，以及Vaccine Effects on In-hospital COVID-19 Outcomes和Computing True Parameter Values in Simulation Studies。

## 因果推断  *(causal_inference, 3 篇)*

### 1. [10.1097/ede.0000000000001884](https://doi.org/10.1097/ede.0000000000001884) · [arXiv](https://arxiv.org/abs/2409.08924) — Regression-based Proximal Causal Inference for Right-censored Time-to-event Data
- **作者**: Kendrick Qijun Li, George C. Linderman, Xu Shi, Eric J. Tchetgen Tchetgen
- **期刊/来源**: Epidemiology
- **分类**: vol 36 · issue 5 · pp 694-704
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在proximal causal inference框架下，针对右删失time-to-event数据提出了回归-based的两阶段估计方法，目标是在加法风险结构模型下估计因果效应，并利用一对负对照变量（处理混杂代理和结果混杂代理）控制未测量混杂。方法的核心是第一阶段通过结果混杂代理和不同类型的负对照结果（连续、计数、右删失）构造未测量混杂的替代变量，第二阶段将其作为协变量纳入加法风险模型进行回归估计。作者为每种负对照类型给出了识别条件和估计量的一致性证明，并通过模拟验证了有限样本性能。实证部分基于SUPPORT数据评估了右心导管置入对危重症患者生存的影响，结果表明该方法能有效校正未测量混杂偏倚。方法已实现为开源R包pci2s，便于实际应用。对您的价值：填补了proximal CI在生存数据上的方法空白，直接连接您对因果推断（特别是负对照和敏感性分析）和流行病学应用的核心兴趣，且R包可复现或扩展。
- **关键技术**: `Proximal causal inference`, `Negative control exposure and outcome`, `Additive hazard model`, `Two-stage regression`, `Right-censored survival data`, `pci2s R package`
- **为什么对您有用**: 本文是proximal causal inference在右删失生存数据上的直接扩展，属于您primary interest中causal inference的子方向（proximal CI的负对照设定）。您very_familiar的'estimation theory in causal inference'可直接理解其两阶段估计量和识别条件，'software development'可支持审计或扩展pci2s R包。依据武器库，这是**立即可做**的题材：您可以复现结果、将其框架推广至更复杂的纵向生存模型或多状态模型。

### 2. [10.1097/ede.0000000000001887](https://doi.org/10.1097/ede.0000000000001887) — Definition and Interpretation of Separable Path-specific Effects With Multiple Ordered Mediators
- **作者**: Yan-Lin Chen, Sheng-Hsuan Lin
- **期刊/来源**: Epidemiology
- **机构**: National Yang Ming Chiao Tung University · National Dong Hwa University · Ta Solutions (China)
- **分类**: vol 36 · issue 5 · pp 677-685
- 相关性 9/10 · novelty: `new_theory`
- **摘要**: 在多有序中介的因果中介分析设定下，传统路径特定效应因依赖 cross-world 反事实定义而难以解释且识别假设不可验证。本文将可分离效应方法扩展至多有序中介情形，提出可分离路径特定效应框架，将其解释为若干分离组件对结果的因果效应，从而提供更直观的机制理解。核心机制在于证明：在个体级隔离假设下，可分离与传统路径特定效应等价；而在 FFRCISTG 模型下将个体级隔离弱化为总体级隔离假设时，可分离效应仍可识别，且其识别假设可在未来实验中验证，避开了传统方法不可验证的 cross-world 假设。文中还讨论了该框架如何检测中介间混杂与因果序错设等假设违背。对您可能有用：为 longitudinal / mediation 的 identification 理论提供了避开 cross-world 假设的新路径，直接连接您对因果识别理论的兴趣。
- **关键技术**: `separable path-specific effects`, `FFRCISTG model`, `population-level isolation assumptions`, `cross-world counterfactual avoidance`, `multiple ordered mediators identification`
- **为什么对您有用**: 本文直接连接您 primary interest 中因果推断的 mediation 与 identification 理论子方向，用 FFRCISTG + 总体级隔离假设替代传统 cross-world 假设，是 identification 理论的一个具体推进。您武器库中 moderately_familiar 的 identification theory in causal inference 可直接用来审视其总体级隔离假设的实质含义与 FFRCISTG 模型的限制。Follow-up 判断：**中期可做**——需先在 moderately_familiar 的 identification theory 上长肌肉，深入理解 FFRCISTG 与 NPSEM 的细微差别后，可探讨该总体级隔离假设在 longitudinal 设定下的推广与估计理论。

### 3. [10.1097/ede.0000000000001888](https://doi.org/10.1097/ede.0000000000001888) — L or M 1—Critical Challenges in Mediation Analysis
- **作者**: Etsuji Suzuki
- **期刊/来源**: Epidemiology
- **机构**: Okayama University
- **分类**: vol 36 · issue 5 · pp 686-689
- 相关性 8/10 · novelty: `survey`
- **摘要**: 本文是一篇流行病学期刊上的评论/短评，聚焦因果中介分析中不同 estimand 的选择与挑战。设定涉及多有序中介情形下 Chen & Lin 提出的 separable path-specific effects，并与经典的 natural / interventional / separable direct/indirect effects 进行对比讨论。核心机制不涉及新 estimator 或收敛率推导，而是从 identification 假设（如 cross-world independence 的不可检验性）角度审视各 estimand 的因果解释力与适用边界。主要结论是强调中介分析 estimand 的选择需紧密结合流行病学实质问题，而非纯数学便利。对您而言，此文梳理了多中介下 separable effects 的 identification 逻辑，可作为中介理论文献的快速定位导图。
- **关键技术**: `separable path-specific effects`, `natural direct/indirect effects`, `interventional effects`, `cross-world independence assumption`, `multiple ordered mediators`
- **为什么对您有用**: 直接连接因果推断的中介分析子方向，特别是多有序中介下 separable path-specific effects 的 identification 假设梳理。您武器库中 moderately_familiar 的 identification theory in causal inference 可直接用来审视此文提及的 cross-world independence 假设的放宽可能，或推导相应 estimand 的 semiparametric efficiency bound。属于 gateway-reading：好入门，梳理了 estimand 族谱，值得花一小时扫读全文以把握流行病学视角对 identification 假设的质疑，但方法学 novelty 极低。

## 流行病学  *(epidemiology, 12 篇)*

### 1. [10.1097/ede.0000000000001877](https://doi.org/10.1097/ede.0000000000001877) — Vaccine Effects on In-hospital COVID-19 Outcomes
- **作者**: Bronner P. Gonçalves, Piero L. Olliaro, Peter Horby, Benjamin J. Cowling
- **期刊/来源**: Epidemiology
- **机构**: University of Surrey · University of Oxford · Department of Health · University of Hong Kong
- **分类**: vol 36 · issue 5 · pp 646-649
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文探讨住院 COVID-19 患者按疫苗接种状态分组的比较研究，指出此类条件于住院状态的常规分析因选择偏差（collider bias）而无法给出总体因果效应。在 principal stratification 框架下，作者证明仅对“无论是否接种都会住院”的子群（principal stratum）才能识别因果疫苗效应。方法上，本文采用 principal stratification 识别策略，并给出针对该子群效应的 sensitivity analysis 操作流程。实证表明，引入该框架可改变仅做常规条件分析的研究结论。对您而言，这是将 principal stratification 与 sensitivity analysis 应用于流行病学真实数据场景的典型案例。
- **关键技术**: `principal stratification`, `collider bias / selection bias`, `sensitivity analysis`, `causal identification`, `conditional analysis post-selection`
- **为什么对您有用**: 本文直接连接流行病学（secondary interest）中的因果推断应用，核心是 principal stratification 解决 collider/selection bias 的 identification 问题。您武器库中的 identification theory in causal inference（moderately_familiar）可直接切入本文的 stratum 识别与 sensitivity analysis 设定。**中期可做**：若想在此类流行病学选择偏差问题上做理论推进，需先在 moderately_familiar 的 identification theory 上长肌肉，特别是 principal stratum 的半参数效率界与 debiased 估计。

### 2. [10.1097/ede.0000000000001889](https://doi.org/10.1097/ede.0000000000001889) — Estimating the Effects of Lifestyle Interventions on Mortality Among Cancer Survivors: A Methodologic Framework
- **作者**: Emma E. McGee, Miguel A. Hernán, Edward Giovannucci, Lorelei A. Mucci, Yu-Han Chiu, A. Heather Eliassen et al.
- **期刊/来源**: Epidemiology
- **机构**: Broad Institute · Brigham and Women's Hospital · Harvard University · October 6 University · Massachusetts Institute of Technology · Pennsylvania State University
- **分类**: vol 36 · issue 5 · pp 705-718
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文聚焦于癌症幸存者中生活方式干预对死亡率影响的因果效应估计，采用目标试验（target trial）框架来提升观察性研究估计的可解释性。作者提出三步骤程序：首先明确规定目标试验的方案（干预、结局、对照、时间零点等），然后在大型前瞻性队列数据中仿制这些试验，最后通过修改目标试验方案来探索未测量混杂或阳性违反假设的敏感性。以乳腺癌和前列腺癌幸存者为例，估计了遵循七项身体活动与饮食建议以及戒酒对20年死亡率的效应，风险差从-4.8%到-13.0%不等。该方法框架本质上是一个系统化的因果推断应用流程，并未引入新的估计量或理论，但提供了可复现的范式。对您而言，本文可作为流行病学中因果推断应用（secondary interest）的典型案例，您完全可以用自己熟悉的因果推断估计理论（如IPW、g-computation）来评析其分析背后的识别假设和估计策略。
- **关键技术**: `target trial emulation`, `per-protocol effect`, `positivity violations`, `unmeasured confounding sensitivity analysis`, `causal risk difference estimation`
- **为什么对您有用**: 本文连接您对流行病学应用和因果推断的双重兴趣，具体展示了目标试验框架如何在真实大型队列中落地。打开的口子是：您可以用非常熟悉的`estimation theory in causal inference` 去审视其估计方法（如风险差的标准化或IPW估计）是否最优，以及用 `identification theory in causal inference` 评估其目标试验规范是否足以保证内部有效性。判定为**立即可做**：无需学习新工具，阅读全文即可剖析其方法学逻辑，并可能在您的软件项目中复现或扩展其分析。

### 3. [10.1097/ede.0000000000001878](https://doi.org/10.1097/ede.0000000000001878) — Racial and Ethnic Differences in the Relationship of SARS-CoV-2 Infection and the COVID-19 Pandemic Period With Perinatal Health in California
- **作者**: Emily F. Liu, Shelley Jung, Kara E. Rudolph, Mahasin S. Mujahid, William H. Dow, Dana E. Goin et al.
- **期刊/来源**: Epidemiology
- **机构**: University of California, Berkeley · Columbia University · Berkeley Public Health Division
- **分类**: vol 36 · issue 5 · pp 668-676
- 相关性 7/10 · novelty: `application`
- **摘要**: 本研究利用2019-2021年加州出生证明和医院数据（849,401例分娩），采用靶向最大似然估计（TMLE）估计SARS-CoV-2感染和COVID-19大流行期对围产期结局的边际风险差异。目标是通过比较亚裔、黑人、西班牙裔、多种族和白人孕妇的差异，检验感染和大流行期对边缘化种族/族裔群体围产期结局的负面影响是否更强。结果显示西班牙裔孕妇感染率最高，而亚裔和黑人孕妇在多个结局上边际风险差异最大，尤其体现在这些群体已不成比例承受的不良结局上。研究证实了感染和大流行期风险在不同种族/族裔群体中的不平等分布。该应用展示了TMLE在真实流行病学队列中的使用，对研究者熟悉因果推断估计方法在流行病学数据上的实践有直接参考价值。
- **关键技术**: `Targeted maximum likelihood estimation (TMLE)`, `Marginal risk difference`, `Causal inference with observational data`, `Perinatal epidemiology`
- **为什么对您有用**: 本文属于流行病学应用（你列为次级兴趣），且使用了因果推断中的TMLE方法，与你的主要兴趣中「因果推断（估计理论）」直接相关。你武器库中的「estimation theory in causal inference」已足够理解论文方法细节，能立即迁移至类似流行病学数据的因果效应估计（立即可做）。

### 4. [10.1097/ede.0000000000001873](https://doi.org/10.1097/ede.0000000000001873) — Computing True Parameter Values in Simulation Studies Using Monte Carlo Integration
- **作者**: Ashley I. Naimi, David Benkeser, Jacqueline E. Rudolph
- **期刊/来源**: Epidemiology
- **机构**: Emory University · Johns Hopkins University
- **分类**: vol 36 · issue 5 · pp 690-693
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对模拟研究中需要已知真实参数值但解析计算困难的问题，提出使用蒙特卡洛积分通过数值方式近似真实值。作者在两种因果推断场景中演示该方法：一是简单的三变量系统，估计边际调整优势比；二是更复杂的中介分析，估计存在暴露影响的中介-结果混杂因素时的控制直接效应。文章给出了通用伪代码和R代码，并讨论了如何控制蒙特卡洛误差（如增大样本量、使用公共随机数）以及通过交叉验证模拟程序来避免编码错误。该方法对流行病学模拟研究特别实用，因为复杂因果模型（如具有时变混杂的纵向数据）的真实参数值往往难以解析推导。对于您（陈星宇）的因果推断和流行病学应用兴趣，本文提供了一种可靠且易于实现的模拟验证工具，可以直接用于您自己设计的模拟实验，以检验估计量的一致性。
- **关键技术**: `Monte Carlo integration`, `simulation-based estimand calculation`, `causal mediation analysis`, `controlled direct effect`, `marginal adjusted odds ratio`
- **为什么对您有用**: 本文直接服务于流行病学模拟研究中的参数计算问题，与您的次要兴趣流行病学（应用数据集、因果推断）高度吻合，特别是其中关于因果中介分析的控制直接效应场景。您武器库中非常熟悉的因果推断估计理论和软件发展技能可以立即用于复现或扩展本文的模拟框架（例如，将其应用于您感兴趣的proximal causal inference或纵向数据设定）。本文属于方法学入门级应用，立即可做——无需学习新工具，即可吸收其伪代码和R代码用于您的模拟研究。

### 5. [10.1097/ede.0000000000001882](https://doi.org/10.1097/ede.0000000000001882) · [arXiv](https://arxiv.org/abs/2407.04214) — Investigating Symptom Duration Using Current Status Data: A Case Study of Postacute COVID-19 Syndrome
- **作者**: Charles J. Wolock, Susan Jacob, Julia C. Bennett, Anna Elias-Warren, Jessica O’Hanlon, Avi Kenny et al.
- **期刊/来源**: Epidemiology
- **分类**: vol 36 · issue 5 · pp 650-659
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文以大学新冠检测项目为背景，研究长新冠（postacute COVID-19 syndrome）症状持续时间的分布。数据为当前状态数据（current status data），即在至少28天后调查受访者症状是否已消退，仅记录调查时间和二值症状状态。与传统方法相比，文章采用现代非参数技术，在更弱的假设下进行估计，并允许使用灵活的机器学习工具处理协变量，同时通过逆概率加权处理调查无应答。方法的核心是假设调查响应时间在观测协变量层内条件独立于症状消退时间，并构建了针对该条件独立性偏离的敏感性分析程序。结果显示，30天时约19%的参与者仍有症状，90天时降至7%；女性、急性期疲劳和高病毒载量与症状消退较慢相关。对您而言，本文展示了流行病学中当前状态数据的非参数处理框架，其中条件独立性假设的敏感性分析方法可迁移到因果推断中的无混淆性假设检验，且其逆概率加权技术可结合您的估计理论工具进行效率分析。
- **关键技术**: `current status data`, `nonparametric estimation`, `machine learning (flexible)`, `sensitivity analysis`, `inverse probability weighting`
- **为什么对您有用**: 本文是流行病学领域的实数据应用，但其非参数估计和敏感性分析方法直接连接到您的主要兴趣——非参数与半参数理论以及因果推断中的无混淆性假设评估。武器库中的'nonparametric statistics'和'estimation theory in causal inference'可用于复现或扩展该敏感性分析框架（例如推导条件独立性假设检验的渐近性质）。中期可做：若您希望进一步研究当前状态数据下的半参数效率界，需先在'semiparametric theory'上增强能力（当前为moderately_familiar）。整体上，这是一篇值得精读的流行病学方法应用文章。

### 6. [10.1097/ede.0000000000001880](https://doi.org/10.1097/ede.0000000000001880) — Beta Approach for Risk Summarization: An Empirical Bayes Method for Summarizing Pregnancy History to Predict Later Health Outcomes
- **作者**: Mary V. Díaz-Santana, Molly Rogers, Clarice R. Weinberg
- **期刊/来源**: Epidemiology
- **机构**: National Institutes of Health · National Institute of Environmental Health Sciences
- **分类**: vol 36 · issue 5 · pp 591-598
- 相关性 4/10 · novelty: `application`
- **摘要**: 本研究针对妊娠并发症（如妊娠糖尿病）的复发风险预测问题，提出了一种基于经验贝叶斯的简单方法——Beta Approach for Risk Summarization (BARS)。关键在于如何利用女性多次妊娠历史（包含发生与未发生事件）来量化个体内在风险倾向性，传统方法难以处理个体间妊娠次数差异。BARS假定个体风险倾向服从Beta分布，通过已有的妊娠结局更新后验分布，得到个体化的风险估计，并用于预测后续妊娠结局或远期健康结局。应用上，基于Sister Study队列的回顾性数据，BARS在预测妊娠糖尿病复发方面校准良好。进一步，将其用于前瞻性分析妊娠糖尿病与乳腺癌风险的关联，验证了方法在更新暴露历史后的稳健性。本文方法简单实用，展示了在流行病学纵向数据中利用经验贝叶斯综合历史信息的一种可行策略，其思路可迁移至因果推断中时变暴露或重复测量的设置。
- **关键技术**: `empirical Bayes`, `Beta-Binomial model`, `risk prediction`, `recurrence risks`, `retrospective cohort`
- **为什么对您有用**: 本文是流行病学中应用经验贝叶斯总结纵向历史数据的典型案例，直接对应研究者的secondary interest（流行病学应用）。研究者武器库中的minimax估计理论和非参数统计可用于分析该模型的收缩性质与预测误差。中期可探索将该方法迁移至因果推断中的时变暴露总结（如用单调指数或倾向性得分更新），需先在identification theory上进一步熟悉。对于对流行病学应用感兴趣的统计学者，本文是理解妊娠史作为风险因素处理的良好入门阅读。

### 7. [10.1097/ede.0000000000001876](https://doi.org/10.1097/ede.0000000000001876) · [arXiv](https://arxiv.org/abs/2408.07298) — Improving the Use of Social Contact Studies in Epidemic Modeling
- **作者**: Tom Britton, Frank Ball
- **期刊/来源**: Epidemiology
- **分类**: vol 36 · issue 5 · pp 660-667
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文关注社交接触研究在传染病建模中的应用。传统方法使用接触矩阵（age-specific contact matrix）表示各年龄组间的平均接触次数，但忽略了年龄组内个体社交活动强度的巨大变异。作者提出将每个年龄组划分为“高社交活跃”和“低社交活跃”两个亚群，构造扩展接触矩阵。基于该扩展矩阵的传染病模型显示，考虑社交活动变异对基本再生数 R0 和最终感染比例（final epidemic size）有显著影响，其重要性甚至超过年龄分组本身。然而，社交接触研究通常缺乏关于社交活跃个体是否倾向于与其他活跃个体接触（即按活动强度的类聚性混合，assortative mixing）的信息。分析表明，无论类聚性如何，考虑变异都能改善模型预测的准确性，但不同类聚假设下 R0 和最终感染比例差异明显。因此，作者呼吁未来社交接触研究应同时收集关于活动强度类聚性的数据。本文是流行病学中数据驱动建模的典型应用，方法学创新有限，属于“改进已有数据使用方法”的实证工作。
- **关键技术**: `contact matrix`, `social activity variation`, `assortative mixing`, `basic reproduction number R0`, `final epidemic size`, `compartmental epidemic model`
- **为什么对您有用**: 本文属于流行病学中数据驱动建模的入门级读物，清晰展示了如何利用社交接触调查数据构建和改进传染病模型。研究者若想进入流行病学应用方向，本文可帮助快速理解该领域的数据结构（分层接触矩阵、个体变异）和关注指标（R0、流行规模）。武器库中“非参数统计”和“M估计”可用来处理接触矩阵中各组内变异的不确定性，但无需立即开展；本文更适合作为方向导引而非直接方法迁移。若研究者对传染病建模与因果推断的交集（如干预效果的外推）感兴趣，则值得通读全文作为背景。

### 8. [10.1097/ede.0000000000001890](https://doi.org/10.1097/ede.0000000000001890) — Use of Health Administrative Data to Identify Migraine in Individuals With a Recognized Pregnancy: A Validation Study in Ontario, Canada
- **作者**: Carmela Melina Albanese, Susan J. Bondy, Christine Lay, Zhiyin Li, Jun Guan, Hilary K. Brown
- **期刊/来源**: Epidemiology
- **机构**: University of Toronto · Public Health Ontario · Institute for Clinical Evaluative Sciences · Women's College Hospital · The Scarborough Hospital
- **分类**: vol 36 · issue 5 · pp 599-605
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文在加拿大安大略省的孕妇队列中，验证了利用健康行政数据识别偏头痛的算法，目标 estimand 是以人群代表性自我报告为金标准的算法灵敏度/特异度/PPV/NPV。研究纳入 N=8824 名在 2005-2021 年间有记录妊娠且在受孕前 5 年内完成 CCHS 问卷的女性，构建了基于 ICD-9 346 / ICD-10 G43 诊断码与偏头痛特异性药物索赔的不同组合及不同回溯窗口的算法。核心发现是所有算法特异度均高（81.7%–98.9%），但灵敏度差异大（6.1%–53.2%）；要求 ≥2 次医生就诊或 ≥1 次急诊/住院且终身回溯的算法在特异度（94.0%）与灵敏度（30.4%）间取得较好折衷，kappa 一致性为 0.29。对您可能有用：若在流行病学队列中用行政数据做因果推断（如偏头痛对围产期结局的 IV 或 DML 估计），此类验证研究提供了测量误差（misclassification）特性的定量参考。
- **关键技术**: `validation study of administrative data algorithms`, `ICD diagnostic code algorithms`, `sensitivity-specificity-PPV-NPV evaluation`, `self-report gold standard comparison`, `lookback period variation`
- **为什么对您有用**: 本文连接到流行病学因果推断子方向：当用行政数据做 treatment（如偏头痛）的因果效应估计时，算法的低灵敏度意味着 treatment 有大量 false-negative misclassification，直接导致 attenuation bias 或 selection bias。研究者可用 semiparametric efficiency bound / debiased ML 的武器库定量分析 misclassification 对 ATE estimator 的影响，甚至推导 correction estimator。follow-up 判断：**中期可做**——需先在 moderately_familiar 的 identification theory 上长肌肉，具体是 misclassification 下的 causal identification 修正条件，再结合 very_familiar 的 estimation theory 构造 robust estimator。

### 9. [10.1097/ede.0000000000001874](https://doi.org/10.1097/ede.0000000000001874) — Early Detection of Dengue Outbreaks: Transmission Model Analysis of a Dengue Outbreak in a Remote Setting in Ecuador
- **作者**: Hannah Van Wyk, Andrew F. Brouwer, Gwenyth O. Lee, Sully Márquez, Paulina Andrade, Edward L. Ionides et al.
- **期刊/来源**: Epidemiology
- **机构**: University of Michigan · Rutgers, The State University of New Jersey · Universidad San Francisco de Quito · University of California, Berkeley
- **分类**: vol 36 · issue 5 · pp 636-645
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文利用2019年厄瓜多尔偏远河岸城镇的登革热爆发数据，探讨在监测系统正式识别爆发前是否已存在未被检测的病毒传播。研究对象是爆发前4例报告病例（2月9日、2月13日、3月28日、5月2日），目标是通过隐马尔可夫模型估计首发病例（无论是否被检测到）的最可能日期。模型假设不同的病例报告比例，并基于状态转移和观测概率推断未检测到的传播链。结果显示，在所有假定的报告比例下，最可能的首发病例日期均在2月7日至2月12日之间，即距主要爆发约2个多月；个体模拟表明更早或更晚的首发病例也存在可能。结论认为登革病毒在社区中已循环约3个月才进入爆发阶段。对您而言，这是一篇流行病学应用实例，展示了如何将状态空间模型用于传染病早期预警，但方法学新颖性有限，可作为流行病学数据驱动的入门读物。
- **关键技术**: `Hidden Markov Model`, `transmission modeling`, `case reporting fraction`, `simulation-based inference`
- **为什么对您有用**: 本文属于流行病学领域的真实数据应用，与您的二级兴趣方向（流行病学数据集和应用因果工作）直接相关。但方法上仅使用经典的隐马尔可夫模型，未涉及您的技术武器库中的高阶U统计、因果推断识别或半参效率理论，因此属于入门级阅读。当前武器库无法直接迁移——因核心建模依赖传染病动力学的SEIR型假设而非统计因果结构，暂不可做。

### 10. [10.1097/ede.0000000000001879](https://doi.org/10.1097/ede.0000000000001879) — Spatial Variability and Clustering of Life Expectancy in the United States: 1990–2019
- **作者**: Isabel P. De Ramos, Tara P. McAlexander, Usama Bilal
- **期刊/来源**: Epidemiology
- **机构**: Drexel University
- **分类**: vol 36 · issue 5 · pp 616-624
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文研究 1990–2019 年间美国通勤区（commuting zone）层面按性别划分的出生预期寿命的空间异质性与聚类模式。核心 estimand 为各通勤区在六个 5 年窗口下的 sex-specific life expectancy 及其跨期变化量。方法上，作者计算了 sex-specific life expectancy，并采用空间自相关与聚类方法（如 Moran's I 与 LISA）识别基线水平与变化趋势的地理聚集区。主要发现：总体预期寿命先升后停滞，女性空间方差扩大；低基线且持续恶化的区域集中在 Appalachia 与 Deep South，高基线且改善最显著的区域散布于 Midwest/Northwest/West。对您而言，本文提供了流行病学空间因果推断的典型数据结构与区域异质性场景，可作为理解地理单元上因果驱动因素（contextual drivers）识别的入门实证案例。
- **关键技术**: `life expectancy estimation`, `spatial autocorrelation (Moran's I)`, `LISA clustering`, `commuting zone spatial unit`, `spatial heterogeneity decomposition`
- **为什么对您有用**: 本文属于流行病学实证研究，连接到 epidemiology 的空间异质性与因果驱动因素子方向。(1) 作为 gateway reading，本文清晰展示了空间单元（commuting zone）上的寿命估计与聚类分析，数据结构（区域面板、空间自相关）对考虑空间因果推断（如区域层面 IV / contextual effect identification）的研究者有参考价值。(2) 武器库中 estimation theory in causal inference 与 moderately_familiar 的 identification theory 可用于后续探索本文提到的 contextual drivers 的因果识别问题，但空间计量与流行病学死因分解的具体工具暂不在库中。(3) 判断：**中期可做**——若想在此类空间流行病学数据上做因果驱动因素识别，需先在 moderately_familiar 的 identification theory 上补充空间混淆与区域层面 IV 的文献；作为入门读物值得花时间读全文以了解数据结构。

### 11. [10.1097/ede.0000000000001883](https://doi.org/10.1097/ede.0000000000001883) — Potential Impact of Maternal Nighttime Light Exposure and Its Interaction With Sociodemographic Characteristics on the Risk of Various Congenital Heart Diseases
- **作者**: Shanidewuhaxi Tuohetasen, Yanji Qu, Philip K. Hopke, Kai Zhang, Yang Liu, Shao Lin et al.
- **期刊/来源**: Epidemiology
- **机构**: Sun Yat-sen University · Guangdong Academy of Medical Sciences · Clarkson University · University of Rochester Medical Center · Albany State University · New York State Department of Health · University at Albany, State University of New York · Emory University 等
- **分类**: vol 36 · issue 5 · pp 625-635
- 相关性 1/10 · novelty: `application`
- **摘要**: 本研究在南方中国 21 市的病例-对照设定下，探究孕期母体夜间人工光照（ALAN）暴露与后代先天性心脏病（CHD）风险的关联，estimand 为条件 OR 及其与社会经济人口学变量的乘法/加法交互效应。方法上，采用卫星遥感数据估算居住地址的年度 ALAN 暴露量，并使用边际结构 Logistic 模型（MSM）处理混杂，辅以四分位数的单调剂量-反应关系验证。核心结果显示，ALAN 每增加 1 单位，总 CHD 风险 OR 为 1.2（95% CI: 1.2-1.3），且在低教育、低收入及常住人群中交互效应更显著（OR 达 1.3）。作为流行病学应用，本文提供了大尺度环境暴露-出生缺陷数据集及 MSM 分析管线，对您在流行病学因果推断方向理解交互效应估计与混杂调整有参考价值。
- **关键技术**: `marginal structural model`, `multiplicative and additive interaction`, `satellite-derived exposure assessment`, `dose-response analysis`, `logistic regression`
- **为什么对您有用**: 本文属于流行病学因果推断的应用工作，直接连接到您 secondary interest 中流行病学数据集与因果推断应用的方向；数据集涉及大尺度地理暴露与多亚型疾病分层，适合作为检验交互效应估计方法（如您 moderately_familiar 中的 M-estimation theory）的实证场景。作为 gateway reading，本文清晰展示了 MSM 在环境流行病学中处理混杂与交互的管线，武器库完全足够支撑阅读与复现，值得花时间读全文以了解该领域的数据结构与建模惯例。

### 12. [10.1097/ede.0000000000001881](https://doi.org/10.1097/ede.0000000000001881) — Medium-term Exposure to Wildfire Smoke PM2.5 and Cardiorespiratory Hospitalization Risks
- **作者**: Yaguang Wei, Edgar Castro, Kanhua Yin, Alexandra Shtein, Bryan N. Vu, Mahdieh Danesh Yazdi et al.
- **期刊/来源**: Epidemiology
- **机构**: Harvard University · Icahn School of Medicine at Mount Sinai · University of Missouri–Kansas City · Stony Brook School · Stony Brook University · Emory University · Brigham and Women's Hospital
- **分类**: vol 36 · issue 5 · pp 606-615
- 相关性 1/10 · novelty: `application`
- **摘要**: 本文利用2006-2016年美国15个州的住院数据，研究了野火烟雾PM2.5的中期暴露（3个月平均）与多种心肺疾病住院风险的关系。方法上，作者将传统的病例-交叉设计（case-crossover design）从急性效应扩展至中期暴露分析，将空间分辨率为10-km²的每日烟雾PM2.5估计聚合至ZIP码水平，并与住院记录匹配。采用条件逻辑回归或泊松回归估计相对风险，并控制个体固定效应（通过自对照设计）和时空趋势。结果显示，3个月平均暴露与多数心肺疾病（尤其是高血压）呈正相关，相对风险（每0.1 μg/m³增加）为1.0051（95%CI: 1.0035-1.0067），且滞后分析表明效应可持续至暴露后3个月。亚组分析发现，在高贫困度、高植被覆盖区域以及曾吸烟者中效应更强。对临床或流行病学研究者而言，本文提供了一个将短期因果推断设计（病例-交叉）应用于中期暴露的实证范例，并展示了时空暴露数据与健康结局对接的实操经验；对统计学者，可借此思考该设计下的识别假设（如可交换性、对照选择）及潜在测量误差对估计的影响。
- **关键技术**: `case-crossover design`, `spatiotemporal exposure modeling`, `self-controlled design`, `conditional logistic regression`, `subgroup analysis`
- **为什么对您有用**: 直接对应流行病学应用方向（secondary interest），展示了利用病例-交叉设计进行中期暴露因果效应估计的完整分析流程。研究者武器库中的因果推断估计理论（very_familiar）可用于审视其识别假设（如无时间趋势混杂、暴露测量误差）和结果稳健性。中期可做：若想深入该领域，需补充空间流行病学建模（如暴露插值、多水平模型）知识，但本文作为入门案例值得精读。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

