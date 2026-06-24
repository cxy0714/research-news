# Epidemiology — Vol 36  Issue 1  ·  2026-06-24

- 共 16 篇 · Epidemiology
- 目录核对 ⚠️ 疑似漏 1 篇（对照 OpenAlex 17 篇）：10.1097/ede.0000000000001790

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期内容围绕**因果推断框架的应用与拓展**、**流行病学经典偏倚与数据质量**、以及**环境与遗传因素的效应识别**三条主线展开。因果推断主线汇集了多篇方法论导向的文章，涵盖目标试验模拟、工具变量、中介分析及部分识别；偏倚与数据主线集中讨论了 immortal time bias、地理数据链接错误及 EHR 数据提取；效应识别主线则关注环境交互、基因-环境交互及剂量-响应决策。

因果推断主线在本期分量最重，集中展示了从框架规范到具体工具的推进。**Target trial emulation** 方面，降压药与痴呆关系的文章通过阳性对照检验揭示了残余混杂问题，另一篇则从结构视角剖析了 immortal time bias 的成因，指出其源于事后信息导致的选择或错分偏倚。**中介分析与纵向数据**方面，一篇针对时间-事件中介与竞争风险提出了基于多状态模型的 R 实现命令，另一篇利用纵向 g-computation 分解抑郁症对死亡率的路径效应。**识别策略与决策**方面，教育政策的自然实验文章应用工具变量估计认知轨迹，剂量选择文章则在单调性假设下将部分识别框架引入 minimax regret 决策。

其余两条主线提供了具体场景下的方法细节。**偏倚与数据质量**方面，ZIP Code 与 ZCTA 链接的文章量化了地理编码不匹配带来的选择偏倚，哮喘表型研究对比了结构化数据与 AI 文本提取在构建 RWE 时的效度差异。**效应识别**方面，结直肠癌研究强调了加法尺度交互指标（RERI）相对于乘法交互的独立性，空气污染与新冠研究利用 Cox 模型量化了污染物交互的额外病例数，预期寿命研究则验证了不同空间聚合方法的一致性。

对于因果推断方向的研究者，建议优先关注**降压药与痴呆**、**Immortal time bias 结构描述**及**剂量选择的部分识别**三篇，分别对应目标试验框架的诊断应用、偏倚结构剖析与决策理论前沿；关注纵向因果中介分析者可参考**多状态模型 R 命令**与**抑郁症-死亡率路径分解**两文。

## 因果推断  *(causal_inference, 3 篇)*

### 1. [10.1097/ede.0000000000001791](https://doi.org/10.1097/ede.0000000000001791) — Multistate approach for stochastic interventions on a time-to-event mediator in the presence of competing risks: A new R command within the CMAverse R package
- **作者**: Ziqing Wang, Baoyi Shi, Cécile Proust-Lima, Hélène Jacqmin-Gadda, Linda Valeri
- **期刊/来源**: Epidemiology
- **机构**: Columbia University
- **分类**: vol 36 · issue 1 · pp 139-140
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文在因果中介分析框架下，考虑中介变量和结局均为时间-事件且存在竞争风险的情形，提出一个新的R命令cmest_multistate，扩展了CMAverse包。采用多状态模型（multistate modeling）刻画从基线到中介事件、基线到结局事件、以及中介事件到结局事件的三条转换路径。定义两个因果估计量：残差异（RD）和转移分布效应（SD），分别对应固定中介时间分布到未暴露组或暴露组下的生存概率差异。模型使用半参数Cox比例风险模型拟合各转换的基线风险，通过非参数bootstrap获得置信区间。模拟验证显示估计偏差小且覆盖率达到理论值。该工作对流行病学健康差异研究中涉及时间-事件中介和竞争风险的实际数据分析有直接工具价值；研究者已有的因果推断估计理论可帮助评估其识别假设，而软件开发者技能则有助于理解和贡献此类R包。
- **关键技术**: `multistate modeling`, `Cox proportional hazards`, `stochastic intervention`, `causal mediation analysis with time-to-event`, `competing risks`, `nonparametric bootstrap confidence intervals`
- **为什么对您有用**: 直接连接因果推断中的中介分析和纵向数据方向（time-to-event mediator & outcome with competing risks），是流行病学应用中常用的设定。研究者可用其非常熟悉的因果推断估计理论评估该方法的识别假设与渐近性质，同时该R包扩展也对接其软件开发者技能，可复现或扩展应用于新数据集。评估为立即可做：核心方法（半参数Cox、bootstrap）已在武器库中，可直接使用或改编。

### 2. [10.1097/ede.0000000000001799](https://doi.org/10.1097/ede.0000000000001799) — State Schooling Policies and Cognitive Performance Trajectories: A Natural Experiment in a National US Cohort of Black and White Adults
- **作者**: Min Hee Kim, Sze Yan Liu, Willa D. Brenowitz, Audrey R. Murchland, Thu T. Nguyen, Jennifer J. Manly et al.
- **期刊/来源**: Epidemiology
- **机构**: Lee University · University of California, San Francisco · Montclair State University · Kaiser Permanente Center for Health Research · Harvard University · University of Maryland, College Park · Columbia University · University of Alabama at Birmingham 等
- **分类**: vol 36 · issue 1 · pp 79-87
- 相关性 7/10
- **摘要**: 利用历史州级教育政策变化（义务教育法、学期长度、出勤率、师生比）作为自然实验，构造工具变量预测教育年限（PPYEd），进而估计教育对中老年认知水平及10年变化轨迹的因果效应。研究对象为REGARDS队列中20,248名45岁以上非西班牙裔黑人和白人，采用随机截距-斜率模型估计PPYEd对记忆、语言流畅性和综合认知得分的效应，并允许按种族/性别分组。结果显示每增加一年PPYEd，基线综合认知提高0.11个标准差（95%CI: 0.07–0.15），记忆效应最为明显，但PPYEd与认知变化率无显著关联。效应在白人和黑人、男性和女性之间基本一致。该研究属于工具变量在流行病学纵向数据中的真实应用，方法设计清晰（政策IV + 混合效应模型），但未评估工具变量的排除限制有效性或使用更灵活的异质性处理方法。对您而言，这是一个了解IV在非传染性疾病流行病学中典型应用的案例，您的因果推断理论（特别是IV识别假设和纵向数据估计理论）可直接用于评估该分析的假设强度与稳健性。
- **关键技术**: `instrumental variables (policy-based instruments)`, `natural experiment`, `random intercept and slope models`, `state-level compulsory schooling laws`
- **为什么对您有用**: (1) 本文属于您 primary interest 中 instrumental variables 在流行病学纵向队列中的具体应用，直接连接“IV in longitudinal settings”子方向；(2) 您非常熟悉的 estimation theory in causal inference 可立即用于评估其工具变量假设（如 exclusion restriction 在认知轨迹中的合理性）及估计量的识别偏差；(3) 立即可做：您可用 own very_familiar 的软件开发和因果推断估计理论，尝试复现其 IV 估计或进行敏感性分析（如放宽政策外生性假设）。

### 3. [10.1097/ede.0000000000001793](https://doi.org/10.1097/ede.0000000000001793) · [arXiv](https://arxiv.org/abs/2305.17206) — Using Limited Trial Evidence to Credibly Choose Treatment Dosage when Efficacy and Adverse Effects Weakly Increase with Dose
- **作者**: Charles F. Manski
- **期刊/来源**: Epidemiology
- **分类**: vol 36 · issue 1 · pp 60-65
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在剂量选择问题中，目标是基于有限 RCT 证据选择最优剂量，假设疗效与不良反应随剂量单调递增。核心设定是剂量空间为离散整数 t ∈ {0,1,...,T}，但试验仅观测 K < T+1 个剂量水平的结局，导致剂量-响应分布部分识别。作者证明在单调性假设下，识别区域为凸多边形，并给出其显式刻画。决策准则采用 minimax regret，在 T=2 时有解析解，更大 T 时计算仍可行。本文将部分识别框架引入剂量决策，对因果推断中的 partial identification 与决策理论有方法论启发。
- **关键技术**: `partial identification`, `monotone dose-response`, `minimax regret`, `convex identification region`, `dose-finding under ambiguity`
- **为什么对您有用**: 连接到因果推断中的 partial identification 与决策理论，与您熟悉的 identification theory 和 minimax bounds 直接相关。用您 very_familiar 的 minimax bounds 工具可以立即分析其 regret 界的紧性，moderately_familiar 的 identification theory 足以跟进其识别区域的推导。**立即可做**：用 minimax 视角审视其 regret 准则是否可改进，或推广到连续剂量空间。

## 流行病学  *(epidemiology, 13 篇)*

### 1. [10.1097/ede.0000000000001802](https://doi.org/10.1097/ede.0000000000001802) — Target Trial Emulation Using Cohort Studies: Estimating the Effect of Antihypertensive Medication Initiation on Incident Dementia
- **作者**: Erin E. Bennett, Chelsea Liu, Emma K. Stapp, Kan Z. Gianattasio, Scott C. Zimmerman, Jingkai Wei et al.
- **期刊/来源**: Epidemiology
- **机构**: Milken Institute · George Washington University · University of Chicago · University of California, San Francisco · University of South Carolina · University of Mississippi Medical Center · University of Washington · National Institute of Neurological Disorders and Stroke 等
- **分类**: vol 36 · issue 1 · pp 48-59
- 相关性 9/10 · novelty: `application`
- **摘要**: 本文采用 target trial emulation 框架，利用三个队列研究（ARIC、CHS、HRS）估计中年启动降压药对痴呆发病的因果效应，estimand 为 intention-to-treat 风险比。方法上通过 propensity score overlap 限制样本、构造 positivity 限制，并引入 positive control outcome（冠心病）检验 exchangeability 假设是否成立。核心发现是 positive control 分析在三个队列中均显示降压药启动与冠心病风险增加相关——这与临床先验矛盾，提示存在严重 residual confounding。作者据此强调：在 target trial emulation 中，仅靠 propensity score trimming 无法保证无混淆，positive control outcome 是诊断假设违反的重要工具。对您而言，这是流行病学应用中因果识别假设诊断的典型案例，展示了如何在真实数据中检验 positivity 和 exchangeability。
- **关键技术**: `target trial emulation`, `propensity score overlap`, `positive control outcome`, `exchangeability assumption`, `intention-to-treat analysis`
- **为什么对您有用**: (1) 本文是流行病学因果推断应用的 gateway reading，展示了 target trial emulation 框架下如何用 positive control outcome 诊断 exchangeability 假设违反——这与您 primary interest 中 causal inference 的 sensitivity analysis 方向直接相关。(2) 武器库中 identification theory in causal inference（moderately_familiar）足以理解本文的识别策略和假设检验逻辑；若要深入，可在 sensitivity analysis 的形式化方法上补课。(3) 作为应用论文，方法学 novelty 有限，但 positive control outcome 作为诊断工具的思路值得借鉴——**立即可做**：用您熟悉的 identification theory 审视其假设检验逻辑是否严谨。

### 2. [10.1097/ede.0000000000001808](https://doi.org/10.1097/ede.0000000000001808) — A Structural Description of Biases That Generate Immortal Time
- **作者**: Miguel A. Hernán, Jonathan A. C. Sterne, Julian P. T. Higgins, Ian Shrier, Sonia Hernández-Díaz
- **期刊/来源**: Epidemiology
- **机构**: Harvard University · University of Bristol · NIHR Bristol Biomedical Research Centre · Health Data Research UK · Jewish General Hospital · McGill University
- **分类**: vol 36 · issue 1 · pp 107-114
- 相关性 8/10 · novelty: `survey`
- **摘要**: 本文系统地描述了生存分析中 immortal time bias 的结构性成因，指出该偏倚并非由 immortal time 本身产生，而是源于基于事后信息分配治疗组或基于事后资格选择样本所导致的 selection 或 misclassification。作者通过 target trial emulation 框架要求明确指定资格标准、治疗分配与随访起点，三者在时间上必须同步，从而消除 immortal time 的出现。当有重复测量纵向数据时，文章总结了多种分析策略，均以模拟目标试验为纲，避免常见的偏倚陷阱。最后强调“immortal time bias”这一术语有误导性，正确理解其来源有助于研究者设计更可靠的观察性研究。该文是流行病学因果推断的经典方法学总结，与您的 secondary 兴趣（流行病学应用中的因果推断）直接相关，可作为实践指南和教学材料。
- **关键技术**: `target trial emulation`, `immortal time bias`, `selection bias`, `misclassification`, `survival analysis design`, `observational study validity`
- **为什么对您有用**: 本文直接对接到您在流行病学应用中的因果推断兴趣，尤其适用于队列研究的生存分析设计。您 moderately familiar 的 identification theory（如 target trial 框架）是本文的核心概念，可帮助您评估现有研究或改进自己的纵向数据分析。立即可做：通读本文可快速掌握 immortal time bias 的识别与规避方法，并迁移至您可能参与的流行病学合作或教学工作中。

### 3. [10.1097/ede.0000000000001804](https://doi.org/10.1097/ede.0000000000001804) — The Contribution of Noncommunicable and Infectious Diseases to the Effect of Depression on Mortality: A Longitudinal Causal Mediation Analysis
- **作者**: Christiane Didden, Matthias Egger, Naomi Folb, Gary Maartens, Eliane Rohner, Reshma Kassanjee et al.
- **期刊/来源**: Epidemiology
- **机构**: University of Bern · LMU Klinikum · Institute of Social and Preventive Medicine · Ludwig-Maximilians-Universität München · University of Cape Town · University of Bristol · South African Medical Research Council · Stellenbosch University
- **分类**: vol 36 · issue 1 · pp 88-98
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文基于南非医疗保险公司2011-2020年约98万人的纵向数据，采用interventional effects approach和Monte Carlo模拟的g-computation，估计重度抑郁症(MDD)对8年死亡率的总体效应，并量化非传染性疾病和传染病作为中介变量的贡献。研究设定为纵向因果中介分析，目标是将MDD-死亡率总效应分解为通过不同疾病路径的间接效应。方法上，通过反事实定义干预风险的中介效应，利用蒙特卡洛模拟实现g-computation估计，避免了参数模型对高维中介的严格线性假设。结果发现MDD组死亡风险比无MDD组高23%（RR=1.23），其中43.4%的差异可由躯体合并症解释：心血管疾病贡献最大(17.8%)，其次为慢性呼吸疾病(8.6%)、癌症(7.5%)、糖尿病/慢性肾病(5.8%)、结核(4.3%)、HIV(2.7%)。结论指出非传染性疾病而非传染病是主要中介路径。对于您而言，这是一项流行病学中纵向因果中介的完整应用实例，其多重中介分解策略和g-computation实现可直接迁移至您感兴趣的其他纵向因果问题（如proximal CI中的中介分析）。
- **关键技术**: `interventional effects approach`, `Monte Carlo simulation-based g-computation`, `longitudinal causal mediation analysis`, `multiple mediator decomposition`
- **为什么对您有用**: 本文属于流行病学领域的因果推断应用，与您的次级兴趣流行病学（应用数据集、因果工作）高度契合。您可以用 moderately_familiar 中的 identification theory in causal inference 严格审视其 interventional effects 的识别假设（如顺序交换性、一致性、无未测量混杂）在观测数据中的可信度，这是评估结论效度的关键。中期可做：先加强 identification theory in causal inference 工具，即可对类似纵向中介研究提出假设敏感性分析或替代识别策略。

### 4. [10.1097/ede.0000000000001796](https://doi.org/10.1097/ede.0000000000001796) — Long-term Associations Between Time-varying Exposure to Ambient PM2.5 and Mortality: An Analysis of the UK Biobank
- **作者**: Jacopo Vanoli, Arturo de la Cruz Libardi, Francesco Sera, Massimo Stafoggia, Pierre Masselot, Malcolm N. Mistry et al.
- **期刊/来源**: Epidemiology
- **机构**: London School of Hygiene & Tropical Medicine · University of Florence · ASL Roma · Azienda Sanitaria Locale Roma 3 · Ca' Foscari University of Venice · University Hospitals of Cleveland · Case Western Reserve University · Imperial College London 等
- **分类**: vol 36 · issue 1 · pp 1-10
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文研究长期 PM2.5 暴露与全因及特定原因死亡率的关联，使用 UK Biobank 队列中 498,090 名受试者的详细个体数据。核心 estimand 是 Cox 比例风险模型下的 hazard ratio，关键假设包括 time-varying exposure 的正确指定和无混杂假设。方法上，通过高分辨率时空机器学习模型重建 8 年滞后窗口内的年度暴露历史，采用 distributed lag models 检验滞后结构，并控制个体和区域层面的混杂因素。主要发现：PM2.5 每增加 10 μg/m³，全因死亡 HR=1.27 (95% CI: 1.06-1.53)，呼吸系统死亡 HR=2.07 (1.04-4.10)，但与心血管死亡无显著关联。敏感性分析表明更精细的暴露度量带来更高的风险估计。作为流行病学应用研究，本文展示了 time-varying exposure 和 distributed lag 结构在队列分析中的具体实现，对您理解 longitudinal CI 在实际数据中的应用场景有参考价值。
- **关键技术**: `Cox proportional hazards model`, `time-varying exposure`, `distributed lag models`, `spatiotemporal exposure modeling`, `confounding adjustment`
- **为什么对您有用**: (1) 连接到 secondary interest 中流行病学队列研究的因果分析，展示了 time-varying exposure 和 distributed lag 结构如何在实际中处理纵向暴露数据；(2) 本文是典型的应用研究，方法学 novelty 有限，但数据集和分析流程可作为 longitudinal CI 方法的实证参考；(3) **暂不可做**：本文核心是标准 Cox 模型应用，不涉及 identification theory 或 semiparametric efficiency 等您 primary interest 中的技术口子，若要 follow-up 需将更复杂的 longitudinal CI 方法（如 g-methods、marginal structural models）引入此类暴露数据分析。

### 5. [10.1097/ede.0000000000001803](https://doi.org/10.1097/ede.0000000000001803) — Advanced Approaches to Generating High-validity Real-world Evidence in Asthma
- **作者**: Karynsa Kilpatrick, Katherine Cahill, Urmila Chandran, Daniel Riskin
- **期刊/来源**: Epidemiology
- **机构**: Amgen (United States) · Vanderbilt University Medical Center · Versar (United States)
- **分类**: vol 36 · issue 1 · pp 20-27
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究哮喘表型特征的 EHR 数据质量问题，目标是在真实世界证据（RWE）框架下比较传统结构化数据提取与 AI 驱动的非结构化临床文本提取的准确性。研究从 3481 名患者的 6037 次医疗就诊中提取 18 个协议定义的特征（包括哮喘严重程度亚型、合并症、症状等），以人工图表审查作为参考标准，使用 Cohen's kappa 评估标注者间信度，以 F1-score 评估提取准确率。传统方法（仅使用结构化数据）的平均 F1-score 为 52.2%，而 AI 方法（处理非结构化文本）达到 94.7%，相对提升 81.4%。主要结论是 AI 技术可显著提升 EHR 数据质量，从而支持高有效性真实世界证据的生成。对您而言，这是一篇流行病学应用论文，展示了数据质量评估的具体流程，但方法学 novelty 有限。
- **关键技术**: `electronic health record data`, `natural language processing`, `chart abstraction`, `Cohen's kappa`, `F1-score`, `real-world evidence`
- **为什么对您有用**: 本文属于流行病学应用研究，与您的 secondary interest（epidemiology: datasets, applied causal work）相关，但核心是 NLP 数据提取而非因果推断或统计方法创新。您的 technical_arsenal（如 semiparametric theory 或 minimax bounds）无法直接应用于本文的数据质量评估问题。本文可作为了解 EHR 数据质量评估流程的入门读物，但若您希望探索 EHR 数据在因果推断中的应用，需要先了解该领域的测量误差与缺失数据处理方法。

### 6. [10.1097/ede.0000000000001797](https://doi.org/10.1097/ede.0000000000001797) — Geospatial Data Aggregation Methods for Novel Geographies: Validating Congressional District Life Expectancy Estimates
- **作者**: Alina Schnake-Mahl, Giancarlo Anfuso, Stephanie M. Hernandez, Usama Bilal
- **期刊/来源**: Epidemiology
- **分类**: vol 36 · issue 1 · pp 119-125
- 相关性 5/10 · novelty: `application`
- **摘要**: 该研究验证了两种聚合方法在估算美国国会选区预期寿命上的一致性。一种方法利用 US Small-area Life Expectancy Estimates Project 的人口普查区级预期寿命估计，通过 dasymetric 方法（人口加权）聚合到国会选区；另一种方法直接使用地理参考的生命统计数据，将年龄别死亡和人口计数汇总后计算简略生命表。通过绝对差异、Pearson 相关和 Bland-Altman 图进行一致性评估。结果显示出生时预期寿命两种方法高度一致，但75岁及以上年龄组相关性较弱。该验证性研究为新型政治地理单元（国会选区）的健康指标聚合提供了方法学支持。对于您而言，本文是流行病学应用中数据聚合与验证的实例，可快速了解小区域估计聚合的实操流程与效度评估思路。
- **关键技术**: `dasymetric mapping`, `population-weighted aggregation`, `abridged life table`, `Bland-Altman plot`
- **为什么对您有用**: 本文属于流行病学领域的应用验证研究，直接对应您的 secondary interest 中的流行病学方向。尽管方法本身较为常规，但其中的聚合策略与验证流程可作为您未来处理地理编码健康数据时的参考。由于技术门槛低，您可以立即评估其分析合理性，并思考如何将更严格的因果推断（如聚合层面的混杂控制）融入类似设定。

### 7. [10.1097/ede.0000000000001795](https://doi.org/10.1097/ede.0000000000001795) — Characterization of Additive Gene–environment Interactions For Colorectal Cancer Risk
- **作者**: Claire E. Thomas, Yi Lin, Michelle Kim, Eric S. Kawaguchi, Conghui Qu, Caroline Y. Um et al.
- **期刊/来源**: Epidemiology
- **机构**: Fred Hutch Cancer Center · University of Southern California · American Cancer Society · The University of Melbourne · Cancer Council Victoria · Umeå University · University of Ioannina · Imperial College London 等
- **分类**: vol 36 · issue 1 · pp 126-138
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究结直肠癌（CRC）中遗传风险评分（GRS）与环境因素的基因-环境交互作用，目标估计量是加法尺度上的交互作用指标 RERI（Relative Excess Risk due to Interaction），在标准 logistic 回归框架下进行识别与推断。数据来自 CRC 联盟汇总的 45,247 例病例与 52,671 例对照，涵盖 13 个环境因素与 141 个遗传变异构成的 GRS。方法上，作者同时报告乘法交互（logistic 回归系数的交互项）与加法交互（RERI），后者通过 logistic 模型参数的线性组合构造估计量与置信区间。主要发现是：乘法交互均不显著，但加法交互显示高遗传风险人群在重度饮酒、吸烟、高 BMI、高红肉摄入上有显著正 RERI（超额风险），而在阿司匹林/NSAIDs 使用及水果、纤维、钙摄入上有显著负 RERI（保护作用更强）。这是典型的流行病学大队列应用研究，方法学 novelty 有限，但数据规模与交互作用指标的公共卫生解读对您理解 epidemiology 应用场景有参考价值。
- **关键技术**: `additive interaction`, `RERI`, `logistic regression`, `genetic risk score`, `multiplicative interaction`, `consortium-level meta-analysis`
- **为什么对您有用**: (1) 本文属于流行病学应用，展示了加法交互 RERI 在公共卫生意义上的识别与估计，与您 secondary interest 中 epidemiology 的应用因果工作直接相关。(2) 方法层面使用的是您 very_familiar 的 logistic 回归与标准推断，技术门槛低；但若想深入 RERI 的 semiparametric efficiency 或 sensitivity analysis，需要您在 moderately_familiar 的 identification theory 上稍作延伸。(3) follow-up 判断：**立即可读**——作为 epidemiology 领域 G×E 交互作用的入门案例，数据规模大、结果解读清晰，适合了解该领域常用的交互作用指标与报告规范。

### 8. [10.1097/ede.0000000000001798](https://doi.org/10.1097/ede.0000000000001798) — Progressing “Positive Epidemiology”: A Cross-national Analysis of Adolescents’ Positive Mental Health and Outcomes During the COVID-19 Pandemic
- **作者**: Meredith O’Connor, Craig A. Olsson, Katherine Lange, Marnie Downes, Margarita Moreno-Betancur, Lisa Mundy et al.
- **期刊/来源**: Epidemiology
- **机构**: The University of Melbourne · Murdoch Children's Research Institute · Deakin University · Australian Psychological Society · Great Ormond Street Hospital · University College London · Imperial College London
- **分类**: vol 36 · issue 1 · pp 28-39
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文以“积极流行病学”为框架，利用澳大利亚（CATS、LSAC两个队列）和英国（MCS）四个长期纵向队列，评估COVID-19大流行前青少年积极心理健康（情绪调节、同伴交往、关爱他人）对疫情期间心理困扰、生活满意度、睡眠和酒精使用等结果的影响。方法采用两阶段meta分析：各队列先通过回归控制潜在混杂，估计风险比（RR）与置信区间，再随机效应合并。积极心理健康由家长报告测量，结果变量在2020年（青少年16–21岁）收集。主要发现：积极心理健康显著降低心理困扰风险（RR=0.83, 95%CI 0.71–0.97），提高生活满意度（RR=1.1, 95%CI 1.0–1.2），但对健康行为的影响较微弱且不显著。该研究展示了如何利用现有大型纵向数据检验资产性保护因素；对您而言，其分析框架可作为流行病学因果推断应用的切入点，启发您用更严格的因果方法（如G公式、双重稳健估计）改进混杂控制或进行敏感性分析。
- **关键技术**: `two-stage meta-analysis`, `longitudinal cohort study`, `confounder adjustment via regression`, `risk ratio estimation`, `positive mental health measurement`, `multi-cohort harmonization`
- **为什么对您有用**: 本文属于流行病学应用方向，直接对应您的secondary interest中“epidemiology (datasets, applied causal work)”。您可以用“estimation theory in causal inference”（very_familiar）评估其混杂控制是否充分、RR估计的可靠性，并尝试替换为双重稳健估计或TMLE以提升鲁棒性。这是一个中期可做的follow-up：需要先加强“identification theory in causal inference”（moderately_familiar），例如引入阴性对照或工具变量处理未观测混杂，从而提出更严格的识别策略。

### 9. [10.1097/ede.0000000000001789](https://doi.org/10.1097/ede.0000000000001789) — Doubly Marginalized: The Interplay of Racism and Disability in Outcomes for Minoritized People With Down Syndrome
- **作者**: Salina Tewolde, Ashley Scott, Alianna Higgins, Jasmine Blake, Amy Michals, Matthew P. Fox et al.
- **期刊/来源**: Epidemiology
- **机构**: Boston University · Mount Sinai Hospital
- **分类**: vol 36 · issue 1 · pp 66-75
- 相关性 4/10 · novelty: `application`
- **摘要**: 本研究在流行病学交叉性框架下，探讨种族/民族和唐氏综合征对成人死亡率与住院率的交互影响。目标是比较非裔、亚裔、原住民等少数族裔唐氏综合征患者与白人患者在健康结局上的差异，并评估种族与唐氏综合征之间的加性交互作用。数据来源为2011-2019年美国Medicare数据库，涵盖119,325名唐氏综合征成人和320万无智力残疾成人。主要采用年龄调整率（率比及95%置信区间）和加性交互作用分析（交互作用超额风险），未使用倾向评分或工具变量等因果推断方法。结果显示，唐氏综合征人群中非裔与白人死亡率无显著差异（率比0.96, 95% CI: 0.92-1.01），但所有少数族裔的住院率均高于白人。加性交互分析表明，非裔、原住民和混血群体在死亡率上呈负加性交互，而所有群体（除原住民外）在住院率上呈正加性交互。该文章是流行病学中交叉性量化的应用实例，对您可能有用：它展示了常规队列数据中加性交互的实践，但方法学较基础，未深入因果推断中的混淆或选择偏差问题，而您更熟悉的高维因果推断工具或可为此类研究提供更严谨的识别策略。
- **关键技术**: `additive interaction`, `age-adjusted rates`, `Medicare data analysis`
- **为什么对您有用**: 本文属于流行病学领域的应用研究，是您的 secondary interest。方法上使用标准的年龄调整和加性交互分析，未涉及您熟悉的因果推断工具（如IV、DML等），因此方法学 novelty 较低。但作为流行病学实证论文，它可以帮助您了解交叉性量化在真实数据中的实施方式和常见挑战（如混杂、选择偏倚）。从您的武器库看，您能用 very_familiar 的因果推断理论（如识别假设、敏感性分析）来评估该研究的识别有效性，但本文本身不提供可直接迁移的新方法。建议作为背景阅读，不值得全文精读。

### 10. [10.1097/ede.0000000000001792](https://doi.org/10.1097/ede.0000000000001792) — Interactive Effects of Long-term Exposure to Air Pollutants on SARS-CoV-2 Infection and Severity: A Northern Italian Population-based Cohort Study
- **作者**: Giovanni Veronesi, Sara De Matteis, Camillo Silibello, Emanuele M. Giusti, Walter Ageno, Marco M. Ferrario
- **期刊/来源**: Epidemiology
- **机构**: University of Insubria · University of Milan
- **分类**: vol 36 · issue 1 · pp 11-19
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文利用意大利北部瓦雷泽省 709,864 名成年居民的前瞻性队列数据，探讨长期暴露于 PM10、NO2 和 O3 对 SARS-CoV-2 感染和严重性（住院、死亡）的交互效应。研究方法采用 Cox 比例风险模型估计单个污染物及交互项的风险比（HR），同时结合 Poisson 模型量化因交互效应导致的额外病例数。结果显示，PM10 和 NO2 与感染及死亡率呈正相关，且在城市区域及高 NO2 共暴露区域效应更强；在高 PM10 共暴露下，O3 原本的保护性关联逆转，每增加 1 µg/m³ 导致额外 278 例感染。模型调整了社会人口因素和合并症，暴露评估则综合化学传输模型和随机森林模型。本文是环境流行病学中多污染物交互效应分析的典型应用，其暴露-效应建模思路和交互效应量化方法可与研究者关注的因果推断（尤其是效应修饰和多暴露联合效应）相结合，为实际数据分析提供直接参考。
- **关键技术**: `Cox proportional hazards model`, `interaction analysis (additive & multiplicative)`, `Poisson regression for excess cases`, `environmental exposure modeling (chemical transport + random forest)`, `population-based cohort study`
- **为什么对您有用**: 本文属于流行病学应用，直接连接研究者 secondary interest 中的流行病学数据集和因果推断应用。研究者武器库中的「estimation theory in causal inference」和「nonparametric statistics」可用于评估暴露-响应曲线的函数形式或进行敏感性分析，例如用平滑项替代线性假设、引入倾向性评分加权以改进混杂调整。立即可做：本文方法传统（Cox 回归），研究者无需学习新工具即可理解其统计假设，并批判性地检验比例风险假定和暴露线性性，进而尝试更灵活的估计方法（如时变暴露、双稳健估计）进行后续分析。

### 11. [10.1097/ede.0000000000001801](https://doi.org/10.1097/ede.0000000000001801) — Multilevel Resilience and Appointment Attendance Among African American/Black Adults with HIV: A Prospective Multisite Cohort Study
- **作者**: Marta G. Wilson-Barthes, Jee Won Park, Michael J. Mugavero, Sonia Napravnik, Michael P. Carey, Joseph L. Fava et al.
- **期刊/来源**: Epidemiology
- **机构**: Brown University · University of Delaware · University of Alabama at Birmingham · University of North Carolina at Chapel Hill · Miriam Hospital · University of Miami · Rhode Island Department of Health
- **分类**: vol 36 · issue 1 · pp 99-106
- 相关性 3/10 · novelty: `application`
- **摘要**: 本研究在291名非洲裔/黑人HIV感染者队列中，前瞻性评估多层面韧性资源与门诊就诊依从性的关联。韧性采用多层面韧性资源度量表（Multilevel Resilience Resource Measure）测量；两个二分类结局分别为12个月内≥87.5%预约就诊率（visit adherence）和两个6个月窗口内的重复就诊指标（clinic attendance）。采用修正Poisson模型估计调整风险比（aRR），对可能的混杂因素（如年龄、性别、社会经济地位）进行控制。结果显示，韧性资源较高组与较低组相比，clinic attendance的aRR为0.95（95% CI: 0.88, 1.0），visit adherence的aRR为1.2（0.95, 1.4），均未达到统计显著性。作者认为这是首批探讨韧性资源与就诊依从性关系的研究之一，但需在更大样本中验证。对您而言，该文展示了流行病学中纵向队列数据、二分类结局的修正Poisson建模实践，与您在流行病学（应用、数据集、因果推断）中的次要兴趣直接相关，但方法学相对常规（标准回归+稳健方差估计），并无新统计技术引入。
- **关键技术**: `Modified Poisson models`, `risk ratio estimation`, `longitudinal cohort study`, `multilevel resilience measurement`
- **为什么对您有用**: 该文属于流行病学领域的应用研究，连接您的次要兴趣（流行病学数据集、应用因果推断）。论文使用的修正Poisson模型是队列研究中处理二分类结局的常用方法（稳健方差估计直接估计风险比），武器库中'estimation theory in causal inference'可支撑对此类模型假设（如对数线性模型正确指定）的诊读。可做判断：暂不可做——论文本身无新统计方法，仅是常规应用，不值得投入时间展开读；但若您想熟悉流行病学队列数据分析的常见结构与变量编码（如韧性量表、重复结局指标），可作为快速浏览的入门材料。

### 12. [10.1097/ede.0000000000001794](https://doi.org/10.1097/ede.0000000000001794) — Potential of a Second Screening Test for Alloimmunization in Pregnancies of Rhesus-positive Women: A Swedish Population-based Cohort Study
- **作者**: Nishan Lamichhane, Shengxin Liu, Agneta Wikman, Marie Reilly
- **期刊/来源**: Epidemiology
- **机构**: Karolinska Institutet · Karolinska University Hospital
- **分类**: vol 36 · issue 1 · pp 40-47
- 相关性 3/10 · novelty: `application`
- **摘要**: 该研究针对Rh阳性孕妇是否应进行第二次抗体筛查这一争议问题，利用瑞典国家登记数据（2003-2012年，682,126次妊娠）开展基于人群的队列分析。在提供二次筛查的县建立logistic回归模型预测阳性结果，并验证其准确性，然后将模型外推至仅提供一次筛查的县，估计漏检的同种免疫病例数。通过区间删失生存分析确定二次筛查的最佳时机为孕28周。结果显示，二次筛查可使同种免疫检出率从0.19%提升至0.25%，即发现当前25%的漏诊病例，而额外筛查和监测成本仅约为不良妊娠结局花费的10%。该论文方法上虽未引入新颖统计技术，但完整展示了预测建模、生存分析与成本效益评估的整合路径，其数据清洗与模型验证过程为流行病学观察性研究提供了可复用的分析范式。对您而言，这是一篇扎实的流行病学应用文献，其分析流程和数据集处理方式可作为您进入流行病学因果推断应用方向的入门范例。
- **关键技术**: `logistic regression for risk prediction`, `interval-censored survival analysis`, `population-based cohort study`, `cost-effectiveness comparison`, `model validation with internal data`
- **为什么对您有用**: 本文属于流行病学应用方向，是您secondary interests中的明确子类别。论文虽未涉及因果推断方法，但完整呈现了大规模登记数据从预测建模到政策建议的常规分析链路，是很好的入门读物。您武器库中的非参数统计和M-估计理论可直接用于评估其模型假设稳健性及推导成本效益估计的置信区间，无需额外学习成本，因此立即可做并值得花时间精读其数据与模型细节。

### 13. [10.1097/ede.0000000000001800](https://doi.org/10.1097/ede.0000000000001800) — ZIP Code and ZIP Code Tabulation Area Linkage: Implications for Bias in Epidemiologic Research
- **作者**: Futu Chen, Beau MacDonald, Yan Xu, Wilma Franco, Alberto Campos, Lawrence A. Palinkas et al.
- **期刊/来源**: Epidemiology
- **机构**: University of Southern California · Collaborative Neuroscience Network · University of California San Diego · Human Longevity (United States)
- **分类**: vol 36 · issue 1 · pp 115-118
- 相关性 2/10 · novelty: `application`
- **摘要**: 该论文旨在比较美国人口普查ZCTA（ZIP Code Tabulation Areas）与美国邮政服务ZIP码的两种链接方法——非交叉映射（一对一）和交叉映射（一对多）——对流行病学研究中选择偏倚的影响。研究利用全国数据及加州死亡率和健康保险数据，采用广义可加模型（GAM）分析ZCTA是否包含不匹配ZIP码与社会人口学特征的关系。全国数据显示15%的ZCTA存在不匹配ZIP码，非交叉映射会系统性地排除更多位于大都市核心、社会经济地位较低、非白人居民的区域。然而，在加州的实际应用中，受影响的ZIP码占比虽达25%-34%，但对应的人口占总样本比例极小（死亡率0.03%，健康保险0.44%）。作者推荐使用交叉映射链接，并提示非交叉映射可能引入偏倚，但幅度有限。该研究为流行病学中地理编码链接的偏误评估提供了清晰的实证框架，有助于识别数据整合中的选择偏倚来源。
- **关键技术**: `crosswalk linkage`, `generalized additive models`, `selection bias analysis`, `spatial data linkage`, `ZIP code/ZCTA concordance`
- **为什么对您有用**: 该论文直接关联流行病学应用（secondary interest）中的数据链接偏倚问题，是理解实际数据源选择偏倚的优良入门案例。您武器库中的'estimation theory in causal inference'可迁移用于量化链接偏倚对因果估计（如逆概率加权）的敏感性。此文门槛低、结构清晰，无需额外工具即可快速读懂，属于立即可做的流行病学应用阅读。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

