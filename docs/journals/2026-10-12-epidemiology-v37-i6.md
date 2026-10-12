# Epidemiology — Vol 37  Issue 6  ·  2026-10-12

- 共 18 篇 · Epidemiology
- 目录核对 ⚠️ 疑似漏 5 篇（对照 OpenAlex 23 篇）：10.1097/ede.0000000000002017、10.1097/ede.0000000000002026、10.1097/ede.0000000000002036、10.1097/ede.0000000000002037、10.1097/ede.0000000000002035

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Epidemiology》的核心关切集中在因果推断的识别假设与估计目标界定上，尤其是随机试验与观察性研究中“效应”定义与选择偏误的纠缠。主线大致有三条：一是围绕随机试验中因果 estimand 的精细拆解（assignment 的作用、per-protocol 与 treatment strategy 的区分）；二是针对复杂暴露（混合物、纵向、时空）的非参数或半参数因果估计方法；三是流行病学应用中普遍性（external validity）与选择偏误的校正问题。此外，还有若干环境暴露与生殖/围产结局的实证研究，以及一篇网络传播动力学方法论文和一篇关于量子计算攻击的经济学评论，后者与统计主题关联较弱。

最突出的一条主线是因果 estimand 的识别条件与解释。`The Role of Assignment` 通过反例指出 per-protocol effect 可能混入 assignment 的直接效应，并给出二者等价的排除性限制条件，这是对随机试验中“依从性”分析框架的实质性澄清。`Vaccine Efficacy Against Naturally Asymptomatic Infections` 则用因果主分层框架将疫苗对无症状感染的效果从“症状转化效应”中分离出来，并给出不依赖跨世界假设的界，与前者形成互补——一个关注 assignment 的干扰，一个关注潜在结局类型的不可观测性。`Nonrandom Selection` 从 DAG 角度系统梳理了选择偏误何时不产生偏倚，强调 estimand 选择（ATE vs ATT）与选择机制结构的关系，为前两篇提供了更一般的识别视角。

第二条主线是暴露混合物与纵向因果效应的非参数估计。`Everything All at Once` 提出完全非参数的移位干预估计量，允许组分间交互与纵向设定，并利用机器学习拟合，直接回应了环境流行病学中“混合物整体效应”的估计需求。`Nesting a Target Study within a Target Trial` 则将目标试验框架扩展到健康差异的因果评估，通过分层抽样与组内随机化定义可解释的 estimand，并扩展了半参数 G-computation 以处理连续随机干预。这两篇在方法工具上共享“反事实移位”与“随机干预”的思想，但前者侧重暴露分布的全局移位，后者侧重组间差异的锚定与政策相关效应。

第三主线是普遍性与选择偏误的实证校正。`Can the All of Us Sample be Reweighted` 直接检验重加权能否使非概率样本逼近全国代表性，结果显示复杂模型仅部分缓解偏差，提示外部有效性校正的局限。`Long-term Effect of the Medicaid Expansion` 采用广义合成控制法处理州级面板的平行趋势违背，是政策评估中方法选择的典型示例。`Revisiting Severe Maternal Morbidity Recurrence` 则用逆概率加权校正选择性失访，量化偏倚小于 1%，展示了在队列研究中处理竞争事件与随访丢失的实操路径。

与因果推断最直接相关的优先阅读是 `The Role of Assignment`、`Vaccine Efficacy Against Naturally Asymptomatic Infections` 和 `Nonrandom Selection`，它们分别从 estimand 定义、主分层识别和选择偏误结构三个角度切入因果推断的核心。半参数效率方向可关注 `Nesting a Target Study within a Target Trial` 的 G-computation 扩展。高维或非参数方法兴趣者应看 `Everything All at Once` 的机器学习拟合与移位干预设计。

## 因果推断  *(causal_inference, 5 篇)*

### 1. [10.1097/ede.0000000000002034](https://doi.org/10.1097/ede.0000000000002034) · [arXiv](https://arxiv.org/abs/2408.14710) — The Role of Assignment in Defining and Identifying Causal Effects in Randomized Trials
- **作者**: Issa J. Dahabreh, Lawson Ung, Miguel A. Hernán, Yu-Han Chiu
- **期刊/来源**: Epidemiology
- **机构**: Beth Israel Deaconess Medical Center · Harvard University · Brown University
- **分类**: vol 37 · issue 6 · pp 885-892
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 本文在随机试验的框架下，聚焦于 per-protocol effect 与 treatment strategy effect 这两个因果 estimand 的概念区分与识别条件。作者通过构造反例，说明 per-protocol effect 不仅包含治疗策略本身的效果，还包含 assignment 不通过治疗而直接对结局产生的影响，因此不能简单等同于 treatment strategy effect。文中明确了二者相等的条件，即需要排除性限制假设（assignment 仅通过治疗影响结局）以及 assignment 不是治疗-结局关联的混杂因素。作者强调，即使 assignment 是随机化的，识别这些 estimand 通常仍需要利用 assignment 的信息，除非额外假设成立。这些假设在实际试验中可能不成立，尤其是当试验的分配过程与常规实践在结局相关方面存在差异（如盲法）时。文章通过因果图（DAG）等工具清晰展示了不同因果结构下的识别功能，对试验数据的统计分析和结果解释具有重要启示。
- **关键技术**: `causal diagrams (DAGs)`, `per-protocol effect`, `exclusion restriction`, `identification of causal estimands`, `randomized trials`
- **为什么对您有用**: 本文直接关联您的 primary interest 中 causal inference 的 identification 与 estimand 定义，特别是 per-protocol effect 与 treatment strategy effect 的区分，对您在流行病学应用中的因果推断工作有直接参考价值。您可以用 very_familiar 的 estimation theory in causal inference 来形式化这些 estimand 的识别条件，并进一步探讨在观察性数据中如何利用 assignment 信息进行估计。

### 2. [10.1097/ede.0000000000002022](https://doi.org/10.1097/ede.0000000000002022) · [arXiv](https://arxiv.org/abs/2605.23551) — Everything All at Once
- **作者**: Kara E. Rudolph, Shodai Inose, Nicholas T. Williams, Iván Díaz, Lucia Calderon, Jacqueline M. Torres et al.
- **期刊/来源**: Epidemiology
- **机构**: University of Oxford · McGill University · Institut national de recherche en sciences et technologies du numérique · Massachusetts Institute of Technology
- **分类**: vol 37 · issue 6 · pp 807-818
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文针对环境流行病学中常见的多元连续暴露混合物，提出一种非参数因果估计方法，目标是在单时点或纵向设定下估计暴露混合物整体移位（shift）对结局的影响。该估计量具有类似主效应回归系数的解释，可灵活定义移位方式（如同时移动多个组分、不同组分移动不同量），并支持组分间交互作用的考察。方法上，作者采用完全非参数的方式，利用机器学习拟合模型，避免了传统参数模型在复杂非随机化设定下的脆弱假设。为减少外推风险，文中还展示了如何基于观测数据评估外推程度并调整移位定义。作者将该方法应用于加州萨利纳斯母婴队列中纵向农药暴露与高血压风险的关系研究，并提供了逐步代码以促进复现和推广。对您而言，本文是纵向因果推断中处理多元连续暴露的实用范例，其非参数估计思路与您关注的 longitudinal causal inference 和 semiparametric theory 直接相关。
- **关键技术**: `nonparametric causal estimation`, `exposure mixture shift`, `longitudinal causal inference`, `machine learning for nuisance estimation`, `extrapolation assessment`
- **为什么对您有用**: 本文属于纵向因果推断中处理多元连续暴露的估计问题，直接对应您 primary interest 中的 longitudinal causal inference 和 semiparametric theory。您可以用 very_familiar 的 estimation theory in causal inference 来审视其估计量的渐近性质，或用 moderately_familiar 的 semiparametric theory 探讨其效率界。立即可做：基于本文的移位估计思路，结合您熟悉的非参数方法设计新的估计量；中期可做：若想深入理论，需在 semiparametric efficiency 方面加强；暂不可做：本文未涉及高维或计算复杂性，不涉及您的统计计算 tradeoff 兴趣。

### 3. [10.1097/ede.0000000000002021](https://doi.org/10.1097/ede.0000000000002021) — Vaccine Efficacy Against Naturally Asymptomatic Infections
- **作者**: Elizabeth T. Rogawski McQuade, Razieh Nabi, Allison Codi, Natalie Dean, Marc Lipsitch, David Benkeser
- **期刊/来源**: Epidemiology
- **机构**: Emory University · Harvard University · Stanford Medicine · Stanford University
- **分类**: vol 37 · issue 6 · pp 867-876
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对疫苗对自然无症状感染效果的估计问题，指出朴素比较接种与未接种者无症状感染风险的方法会产生误导，因为它混杂了疫苗预防无症状感染和将症状性感染转化为无症状感染两种效应。作者采用因果主分层框架，形式化定义了 estimand VE_NAI，即疫苗在那些自然（未接种时）会无症状的个体中预防无症状感染的效果，排除了症状转化效应，从而更接近通常的疫苗效力定义。文章给出了在随机和观察性研究中识别和估计该 estimand 所需的假设，并提出了不依赖跨世界独立假设的界以及围绕主要识别假设的敏感性分析。作者将该方法应用于 COVID-19 mRNA-1273 疫苗的随机试验，发现 VE_NAI 高于标准无症状感染效力估计，且与任何感染的效力相当。该工作为疫苗试验中报告多种效力指标提供了方法学支持，有助于理解疫苗对传播的影响和免疫机制。对您而言，本文是主分层因果推断在流行病学应用中的典型范例，其识别假设和敏感性分析思路可迁移至您的因果推断研究。
- **关键技术**: `principal stratification`, `causal estimand`, `identification assumptions`, `bounds`, `sensitivity analysis`, `randomized trial`
- **为什么对您有用**: 本文直接关联您的因果推断兴趣，特别是主分层框架下的 estimand 定义与识别，以及敏感性分析；您可运用 very_familiar 的估计理论（如 M-estimation）来审视其估计量的性质，或结合 moderately_familiar 的识别理论探讨其假设的可检验性。属于立即可做的范畴。

### 4. [10.1097/ede.0000000000002024](https://doi.org/10.1097/ede.0000000000002024) · [arXiv](https://arxiv.org/abs/2508.14690) — Nesting a Target Study within a Target Trial
- **作者**: Xinyi Sun, Theodore J. Iwashyna, Emmanuel F. Drabo, Deidra C. Crews, Kadija Ferryman, John W. Jackson
- **期刊/来源**: Epidemiology
- **机构**: Johns Hopkins University · Johns Hopkins Medicine · Erasmus University Rotterdam · Johns Hopkins Berman Institute of Bioethics
- **分类**: vol 37 · issue 6 · pp 727-737
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文提出 TS+TT 框架，将目标研究（TS）嵌套于目标试验（TT）中，用于评估干预对健康差异（disparities）的因果效应。TS 部分基于 allowability 的伦理假设，通过分层抽样使社会群体在允许的协变量上分布相似，从而锚定差异的测量。TT 部分在每组内随机化干预策略，确保组内可交换性，从而定义有意义的因果 estimand。作者扩展了半参数 G-computation 以处理连续随机干预，并估计时间-事件结局的反事实差异。通过脉搏血氧仪偏倚对治疗接受差异的假设干预实例展示了框架的应用。该框架为减少差异且避免加剧差异提供了伦理知情且政策相关的因果证据方法。
- **关键技术**: `target trial emulation`, `semiparametric G-computation`, `stochastic interventions`, `stratified sampling`, `counterfactual disparity measures`
- **为什么对您有用**: 该论文直接关联因果推断中的纵向与干预效应评估，特别是差异（disparity）的因果估计，属于您的主要兴趣方向。您可运用 identification theory 和 semiparametric theory 中的武器（如 efficient influence function、G-computation）来审视其 estimand 的定义和估计效率。中期可做：该框架涉及连续随机干预的 G-computation，您可在 moderately_familiar 的 semiparametric theory 上进一步巩固后，探索其效率界或敏感性分析。

### 5. [10.1097/ede.0000000000002018](https://doi.org/10.1097/ede.0000000000002018) — Nonrandom Selection With and Without Bias Due to Selecting on an Exposure
- **作者**: Chanelle J. Howe, Han-Chih T. Hsieh, Jason R. Gantenberg, Arman Oganisian, Charles B. Eaton, Haidong Lu
- **期刊/来源**: Epidemiology
- **机构**: Boston University · Brown University · Yale University
- **分类**: vol 37 · issue 6 · pp 877-884
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文在流行病学因果推断框架下，系统讨论非随机选择（selection）何时不会导致因果效应估计偏倚。作者强调，非随机选择是否产生偏倚取决于因果结构（DAG）和所关注的 estimand（如ATE、ATT等），而非选择本身。通过选取暴露水平（如仅纳入暴露者）的动机性例子，结合因果图和模拟，展示了多种选择不导致偏倚的场景，例如当选择由暴露或工具变量决定且目标 estimand 为条件效应时。文章提供了SAS和R代码以促进可复现性和深入理解。对您而言，该文可作为流行病学中 selection bias 的入门读物，其因果图与模拟结合的方式有助于您快速把握选择偏倚的识别条件。
- **关键技术**: `causal diagrams (DAGs)`, `selection bias`, `simulation`, `estimand-specific bias assessment`
- **为什么对您有用**: 本文属于流行病学应用中的因果推断，直接对应您的 secondary interest 中的流行病学应用方向。作为入门读物，它清晰展示了非随机选择何时不产生偏倚的识别条件，武器库中的 identification theory 足以支撑您理解并评估其因果图论证，值得花时间阅读全文以加深对选择偏倚机制的理解。

## 流行病学  *(epidemiology, 12 篇)*

### 1. [10.1097/ede.0000000000002016](https://doi.org/10.1097/ede.0000000000002016) — Can the All of Us Sample be Reweighted to Mirror a Nationally Representative Sample? A Comparison of Mortality Predictors
- **作者**: Jingxuan Wang, Peter Buto, Erin L. Ferguson, Ruijia Chen, Anna Pederson, Minhyuk Choi et al.
- **期刊/来源**: Epidemiology
- **机构**: Boston University · Harvard University · Massachusetts General Hospital · Mass General Brigham · University of California, San Francisco · Brown University · University of Southern California · University of California, Los Angeles
- **分类**: vol 37 · issue 6 · pp 854-866
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文针对 All of Us (AoU) 队列与全美代表性样本（NHANES）之间的选择偏差，评估重加权方法能否提升研究结果的普遍性。作者构建了四种选择权重模型，涵盖社会人口学、自报健康和临床特征及其交互项，并比较加权后 AoU 与 NHANES 中全因死亡率预测因子的风险比（HR），以风险比比值（RHR）衡量偏差。结果显示，加权改善了协变量平衡，最复杂的临床交互模型使高血压的 RHR 从 1.5 降至 1.2，但仍有 17/35 个 HR 偏离超过 20%。结论是重加权只能部分缓解选择偏差，无法完全实现普遍性。该研究对流行病学应用中的外部有效性评估和选择偏差校正具有直接参考价值。
- **关键技术**: `inverse probability weighting`, `selection bias`, `generalizability`, `Cox proportional hazards model`, `NHANES`
- **为什么对您有用**: 本文属于流行病学应用，直接关联您的 secondary interest 中流行病学队列研究的因果推断应用。它展示了重加权方法在真实队列中的实际效果和局限性，可作为您评估外部有效性方法的实证案例。

### 2. [10.1097/ede.0000000000002027](https://doi.org/10.1097/ede.0000000000002027) — Development and Validation of a Vacant Lot Care Condition Instrument for Longitudinal Evaluation of Place-based Interventions
- **作者**: Hiwot Y. Zewdie, Nicole Asa, Christina Brown, Rita Nelson, Hyden Terrell, Maggie Beverly et al.
- **期刊/来源**: Epidemiology
- **机构**: Harvard University · University of Washington · Drexel University · Columbia University · US Forest Service · United States Department of Agriculture
- **分类**: vol 37 · issue 6 · pp 738-746
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文开发并验证了一个用于纵向评估空地维护状况（vacant lot care condition）的标准化审计工具，目标是在场所干预（如空地绿化）的长期评估中量化“照护线索”（cues-to-care）。作者结合主题专家和社区专家制定审计协议，从费城2007至2023年的Google街景图像中对518块空地进行了5名评分者的3,419张图像审计，共6,315条评分。方法上，作者对一致且概念对齐的条目拟合双参数项目反应理论（IRT）模型，将可观测的照护线索合并为单一潜在得分，并检验该得分对随机对照绿化试验和当地维护计划的敏感性。结果显示，最终保留8个信度高于0.40的条目，IRT模型内部信度高达0.96，且得分对干预后条件改善敏感。结论是该IRT得分可准确测量空地照护状况随时间的变化，支持长期评估。对您而言，本文展示了IRT在纵向环境暴露测量中的应用，可作为流行病学中测量工具开发与验证的实例，但其方法学新颖性有限，主要是应用性质。
- **关键技术**: `item response theory (IRT)`, `two-parameter IRT model`, `Google Street View imagery audit`, `inter-rater reliability (Cohen's kappa)`, `longitudinal measurement`, `place-based intervention evaluation`
- **为什么对您有用**: 本文属于流行病学应用，涉及纵向数据下的测量工具开发，与您的secondary interest（流行病学应用因果工作）相关。作为gateway reading，它展示了如何将IRT用于环境暴露的纵向测量，但方法学深度一般。从武器库看，您对测量误差和纵向因果推断的熟悉度足以理解本文，但无需深入；若想跟进，可考虑用您的因果推断工具（如g-formula）评估测量误差对干预效应估计的影响，这属于中期可做，需在纵向因果推断方法上稍作巩固。

### 3. [10.1097/ede.0000000000002030](https://doi.org/10.1097/ede.0000000000002030) — Long-term Effect of the Medicaid Expansion Program on Cancer Mortality by US Region, Gender, and Race/Ethnicity
- **作者**: Mina Habib, Roshan Bastani, Beth Glenn, Zuo-Feng Zhang, Roch A. Nianogo
- **期刊/来源**: Epidemiology
- **机构**: University of California, Los Angeles · UCLA Jonsson Comprehensive Cancer Center · Kaiser Permanente
- **分类**: vol 37 · issue 6 · pp 747-755
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文利用美国 2005–2019 年州级面板数据，将 Medicaid 扩张视为自然实验，评估其对 25–64 岁成年人癌症死亡率（每 10 万人）的因果效应，并按地区、性别和种族/族裔进行亚组分析。数据来源包括美国人口普查、CDC WONDER、Kaiser Family Foundation 等，处理组为 27 个扩张州，对照组为 24 个非扩张州。方法上采用 person-time 加权的广义合成控制法（generalized synthetic control），调整人口、社会经济和医疗可及性变量，以缓解平行趋势假设的违背。结果显示扩张总体上与癌症死亡率降低相关（MD: –2.06; 95% CI: –4.24 to 0.11），但仅在女性、非西班牙裔白人和东北部州中达到统计显著。结论强调 Medicaid 扩张对癌症死亡率的影响存在异质性，对少数族裔和男性等群体的获益证据不足，可能反映医疗获取、质量及风险因素分布的不平等。对您而言，本文是流行病学中利用自然实验和合成控制法进行因果推断的应用范例，其亚组分析和敏感性思路可迁移至您关注的健康政策评估问题。
- **关键技术**: `generalized synthetic control`, `person-time weighting`, `natural experiment`, `state-level panel data`, `subgroup analysis`
- **为什么对您有用**: 本文属于流行病学应用，使用合成控制法评估政策因果效应，与您的 secondary interest 中流行病学应用方向直接相关。您可用 very_familiar 的估计理论（如双重差分、合成控制的偏差校正）来审视其识别假设和估计精度，中期可尝试用 moderately_familiar 的因果推断 identification 理论（如处理组异质性下的外推）来深化亚组分析的解释。总体而言，本文作为流行病学因果推断的入门级应用，值得快速阅读以了解数据和分析流程。

### 4. [10.1097/ede.0000000000002023](https://doi.org/10.1097/ede.0000000000002023) — Revisiting Severe Maternal Morbidity Recurrence
- **作者**: Rashida S. Smith-Webb, Martha M. Werler, Samantha E. Parker, Jennifer Weuve, Collette N. Ncube
- **期刊/来源**: Epidemiology
- **机构**: Boston University
- **分类**: vol 37 · issue 6 · pp 773-783
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文在流行病学队列中研究严重孕产妇发病（SMM）的复发风险，目标是估计首次分娩SMM对第二次分娩SMM风险的影响，并量化选择性失访（包括竞争事件和随访丢失）导致的偏倚。数据来自马萨诸塞州1998-2021年的571,862名初产妇，采用逆概率加权（IP of continuation weights）来校正失访偏倚，权重通过逻辑回归建模失访概率。效应估计使用修正泊松回归，分别用恒等连接和对数连接估计风险差（RD）和风险比（RR）。未加权分析显示SMM复发风险显著增加（RD=506.1/万，RR=5.39），加权后估计略有增加（RD=510.6，RR=5.42），偏倚小于1%，表明选择性失访影响很小。亚组分析显示黑人个体的复发风险最高（RD=1076.6，RR=6.24）。本文是典型的流行病学应用研究，方法学上使用IP加权和泊松回归，但未涉及新的统计理论；对您而言，可作为因果推断中失访偏倚校正的实例，但方法学新颖性有限。
- **关键技术**: `inverse probability of continuation weights`, `modified Poisson regression`, `risk difference`, `competing events`, `selective attrition bias`
- **为什么对您有用**: 本文属于流行病学应用研究，直接关联您的secondary interest中的流行病学队列因果推断。它展示了在纵向数据中处理失访偏倚的IP加权方法，但方法学较为常规。作为gateway reading，本文数据描述清晰，适合了解SMM复发风险的流行病学背景；您的武器库（如因果推断中的IPW、M-estimation）足以理解并复现其分析，但无需深入阅读全文，除非您关注失访偏倚的敏感性分析。

### 5. [10.1097/ede.0000000000002011](https://doi.org/10.1097/ede.0000000000002011) — Maternal Exposure to Air Pollution and Fetal Growth
- **作者**: Yana Luo, Ioar Rivas, Maria Foraster, Toni Galmés, Gustavo Arévalo, Lluís Barril et al.
- **期刊/来源**: Epidemiology
- **机构**: Universitat Pompeu Fabra · Barcelona Institute for Global Health · Centro de Investigación Biomédica en Red de Epidemiología y Salud Pública · Universitat Ramon Llull · University of California, Los Angeles · Institut Universitari d'Investigació en Atenció Primària Jordi Gol · Hospital Sant Joan de Déu Barcelona · Instituto de Salud Carlos III 等
- **分类**: vol 37 · issue 6 · pp 819-827
- 相关性 6/10 · novelty: `application`
- **摘要**: 该研究基于巴塞罗那生命研究队列（2018-2021年）的1024名孕妇数据，评估了母亲在家庭、工作场所和通勤路线等关键微环境中空气污染暴露（NO2、黑碳、PM2.5及其金属成分）与胎儿生长指标（出生体重和小于胎龄儿）的关联。暴露估计采用土地利用回归、扩散模型及两者的混合模型，并结合时间-活动数据计算总微环境暴露，同时使用被动采样器测量个人、室内和室外NO2浓度。关联分析使用线性和逻辑混合效应模型。结果显示，家庭和总微环境中的NO2和黑碳暴露与出生体重降低相关，工作场所黑碳、家庭及总微环境PM2.5及其金属成分的暴露也与出生体重降低相关，但部分结果在不同模型间不一致。个人和家庭室外NO2暴露也与出生体重降低相关，对小于胎龄儿的分析呈现类似模式。结论认为母亲空气污染暴露与胎儿生长受损相关，家庭暴露估计和短期NO2测量可作为实用的暴露代理。
- **关键技术**: `land-use regression`, `dispersion modeling`, `hybrid exposure models`, `time-activity data`, `mixed-effects models`, `passive sampling`
- **为什么对您有用**: 本文属于流行病学应用研究，直接对应您的secondary interest中的流行病学方向。它展示了在真实队列中结合多种暴露评估模型（LUR、扩散、混合）和混合效应模型进行因果关联推断的完整流程，其暴露测量设计和模型比较策略对您理解流行病学数据结构和分析实践有参考价值。作为入门读物，本文方法学清晰，但统计方法相对常规（混合效应模型），武器库足以支撑您理解其分析，但方法学迁移价值有限，可快速阅读以了解该领域的数据和分析模式。

### 6. [10.1097/ede.0000000000002033](https://doi.org/10.1097/ede.0000000000002033) — Air Pollution Exposure in Infancy and Incidence of Atopic Dermatitis in Preschool-Aged Children
- **作者**: Macarena Racciatti, Logan C. Dearborn, Joan A. Casey, Adam A. Szpiro, Kecia N. Carroll, Joel D. Kaufman et al.
- **期刊/来源**: Epidemiology
- **机构**: University of Washington · Icahn School of Medicine at Mount Sinai · University of California, San Francisco · University of Tennessee Health Science Center · Seattle Children's Research Institute
- **分类**: vol 37 · issue 6 · pp 828-836
- 相关性 5/10 · novelty: `application`
- **摘要**: 这是一项基于 ECHO-PATHWAYS 联盟六城市 1587 名儿童的纵向队列研究，目标是估计婴儿期（第一年）室外 PM2.5、NO2 和 O3 暴露对 4-6 岁特应性皮炎（AD）发病风险的影响。研究采用多变量 Poisson 回归估计 adjusted relative risk，并检验儿童性别与母亲教育程度作为潜在效应修饰因子。结果显示 O3 每增加 1 ppb 与当前 AD 的 adjusted RR=1.07（95% CI 1.01-1.13）相关，而 NO2 和 PM2.5 未见显著关联，且无性别修饰效应。值得注意的是，O3 与 AD 的关联仅在母亲教育程度较低的儿童中显著，提示环境暴露可能加剧健康不平等。该研究的主要方法学贡献在于利用验证过的国家尺度时空暴露模型进行个体水平暴露评估，并采用标准化问卷定义结局；但其因果推断强度受限于观察性设计、未控制的时变混杂以及结局测量依赖 caregiver 报告。对您而言，这是一篇典型的应用流行病学论文，其暴露-结局关联分析框架和效应修饰检验思路可迁移至您关注的因果推断应用场景，但方法学新颖性有限。
- **关键技术**: `multivariable Poisson regression`, `spatiotemporal exposure modeling`, `effect modification analysis`, `pooled longitudinal cohort`, `adjusted relative risk`
- **为什么对您有用**: (1) 属于流行病学应用方向，是您 secondary interest 中 epidemiology 的典型代表，展示了环境暴露与儿童健康结局的关联分析流程；(2) 可用您 very_familiar 的 estimation theory in causal inference 审视其混杂调整是否充分（如是否考虑时变混杂、是否有负对照检验），也可用 moderately_familiar 的 identification theory 评估其因果解释的边界；(3) 立即可做：作为应用论文，其分析模式（Poisson 回归 + 效应修饰）可直接复现或扩展，无需新武器；但若要深入做因果推断（如处理未测量混杂），则需在敏感性分析方法上补强。

### 7. [10.1097/ede.0000000000002031](https://doi.org/10.1097/ede.0000000000002031) — Associations Between Area-level Deprivation at the Census Tract Level and Preterm Birth in the Biosocial Impact of Black Births Study
- **作者**: Jazib Gohar, Carmen Giurgescu, Sue C. Grady, Zhehui Luo, Sarah Vaughan, Dawn P. Misra
- **期刊/来源**: Epidemiology
- **机构**: Michigan State University · University of Central Florida · Wayne State University
- **分类**: vol 37 · issue 6 · pp 788-795
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文利用 Biosocial Impact on Black Births 前瞻性队列中 1239 名黑人孕妇的数据，研究 Census tract 层面的区域剥夺指数与早产风险的关系，并检验母亲教育程度和家庭年收入的效应修饰作用。区域剥夺指数通过对 Census tract 层面特征进行主成分分析构建。采用广义估计方程（GEE）估计多水平广义线性模型，控制母亲年龄、教育和收入，最佳拟合模型包含教育与收入的两个两两交互项。结果显示，在无大学学历且年收入至少 3 万美元的女性中，高剥夺区域居住者的早产风险是低剥夺区域的 3 倍以上；教育（大学学历）在高剥夺区域中呈保护作用，而高收入反而有害。该研究为流行病学中邻里效应与健康差异的因果推断提供了观察性证据，但其识别策略依赖可忽略性假设，未涉及未测量混杂的敏感性分析。对您而言，本文可作为流行病学应用案例，其多水平建模与交互效应分析模式可迁移至您关注的因果推断与纵向数据研究。
- **关键技术**: `principal component analysis`, `generalized estimating equations`, `multilevel generalized linear models`, `effect modification`, `interaction terms`
- **为什么对您有用**: 本文属于流行病学应用研究，使用多水平模型和交互效应分析，与您的流行病学应用兴趣直接相关；其观察性设计中的混杂控制问题可连接您的因果推断敏感性分析工具；但方法学新颖性有限，主要价值在于数据集和分析流程。

### 8. [10.1097/ede.0000000000002029](https://doi.org/10.1097/ede.0000000000002029) — Impact of Abortion-limiting Legislation on Preterm and Early Term Birth in Atlanta, Georgia, 2020–2023
- **作者**: Stephanie M. Eick, Xiaping Zheng, Howard H. Chang, Suchitra Chandrasekaran, Anne L. Dunlop, Dana E. Goin
- **期刊/来源**: Epidemiology
- **机构**: Emory University · Columbia University
- **分类**: vol 37 · issue 6 · pp 765-772
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文利用 2020–2023 年亚特兰大 Emory 大学附属医院的出生数据，评估 Dobbs 判决（草案泄露、正式裁决）及佐治亚州 HB481 法案实施对早产（<37 周）和早期足月产（37–38 周）的影响。研究以受孕周为时间轴，计算每周受孕数及 PTB/ETB 比例，并估计与三个事件相关的风险比（HR）。结果显示，Dobbs 草案泄露后受孕数下降；HB481 实施后受孕的妊娠中，PTB 风险增加（HR=1.16, 95% CI: 1.03–1.29），ETB 风险也呈上升趋势（HR=1.05, 95% CI: 0.99–1.12）。结论认为堕胎限制相关法律变化可能影响生育模式及围产期结局。对您而言，这是一篇流行病学应用论文，其事件研究设计（interrupted time series 思路）和 HR 估计框架可迁移至您关注的因果推断中的纵向政策评估场景。
- **关键技术**: `event study design`, `hazard ratio estimation`, `interrupted time series`, `gestational-age-based conception timing`
- **为什么对您有用**: 本文属于流行病学应用论文，使用事件研究设计评估政策冲击对出生结局的影响，与您的 secondary interest 中流行病学应用因果推断方向直接相关。您可以用 very_familiar 的估计理论（如逆概率加权或 g-formula）来审视其 HR 估计的混杂控制是否充分，中期可做的是引入更精细的纵向因果模型（如 marginal structural model）来改进其分析。

### 9. [10.1097/ede.0000000000002025](https://doi.org/10.1097/ede.0000000000002025) — Neighborhood Deprivation and Hypertensive Disorders of Pregnancy
- **作者**: Meredith A. Dixon, Suchitra Chandrasekaran, Howard H. Chang, Michael R. Kramer, Tené T. Lewis, Penelope P. Howards
- **期刊/来源**: Epidemiology
- **机构**: Emory University · Georgia State University · Mercer University · Mercer University Health Sciences Center
- **分类**: vol 37 · issue 6 · pp 796-806
- 相关性 5/10 · novelty: `application`
- **摘要**: 本研究利用美国多中心前瞻性队列 nuMoM2b（2010-2013 年招募，n=7,349 名未产妇）评估社区剥夺指数（ADI）与妊娠期高血压疾病（HDP）的关联，并检验社会支持是否作为效应修饰因子。采用线性概率模型配合稳健标准误估计风险差（RD），按种族/族裔分层，并比较不同社会支持水平下的分层 RD 来评估效应修饰。结果显示，ADI 每增加 25 个百分点，非西班牙裔黑人中妊娠期高血压风险增加 2 例/100 人（RD=0.02, 95%CI: -0.01, 0.05），而西班牙裔和亚裔中呈负向关联；高社会支持与非西班牙裔白人和亚裔的子痫前期/子痫风险降低相关（RD=-0.03, 95%CI: -0.05, 0.00），但未发现社会支持对 ADI-HDP 关联的缓冲作用。该研究是流行病学应用论文，方法学上采用经典回归与分层分析，无新颖统计方法，但数据集（nuMoM2b 纵向队列）和效应修饰分析思路对您关注的应用因果推断（如纵向数据中的效应修饰）有参考价值。
- **关键技术**: `linear probability model`, `robust standard errors`, `effect measure modification`, `stratified analysis`, `area deprivation index`
- **为什么对您有用**: 本文属于流行病学应用论文，可作为 gateway reading 了解社区层面暴露与妊娠结局的因果关联研究设计；其效应修饰分析（按社会支持和种族分层）与您关注的纵向因果推断中的效应异质性分析相关。武器库中 very_familiar 的估计理论（如线性模型、稳健推断）足以理解本文方法，但方法学贡献有限，不值得深入精读；若需跟进，可考虑用更灵活的因果推断方法（如 g-computation 或 TMLE）改进效应修饰估计，这属于中期可做，需在 moderately_familiar 的 semiparametric theory 上加强。

### 10. [10.1097/ede.0000000000002020](https://doi.org/10.1097/ede.0000000000002020) — Indoor Radon Concentrations and Hematologic Traits in the Women’s Health Initiative
- **作者**: Cuiran Shi, Jason M. Collins, Ayesha Ekanayaka, James D. Stewart, Karen N. Conneely, David Y. Huang et al.
- **期刊/来源**: Epidemiology
- **机构**: University of North Carolina at Chapel Hill · Emory University · University of California, Los Angeles · UCLA Jonsson Comprehensive Cancer Center · Brigham and Women's Hospital · Harvard University · University of North Dakota · Fred Hutch Cancer Center 等
- **分类**: vol 37 · issue 6 · pp 837-847
- 相关性 5/10 · novelty: `application`
- **摘要**: 本研究在 Women's Health Initiative 前瞻性队列中，基于 154,630 名绝经后女性、5 次随访（19 年）的重复测量数据，评估室内氡浓度与血常规指标（白细胞、血小板、红细胞压积、血红蛋白及白细胞分类）的纵向关联。暴露变量为通过地理编码地址链接 USGS Radon Index 估计的时变室内氡浓度（pCi/L），按 EPA 行动水平分为 <2、2–4、>4 pCi/L 三档。方法上采用线性混合效应模型估计协变量调整的纵向关联，并在 6,313 人子集中用多元成分数据分析（compositional data analysis）评估白细胞分类的横断面关联。结果显示，与 <2 pCi/L 相比，>4 pCi/L 时白细胞计数显著降低（平均差 78 cells/μL），而血小板、红细胞压积和血红蛋白显著升高，且非线性样条模型结果一致；淋巴细胞百分比降低，其他细胞百分比升高。结论指出这些促血栓形成的髓系偏移对心血管风险的潜在影响尚不明确。对您而言，这是一篇典型的流行病学应用论文，其纵向混合模型和成分数据分析的建模思路可迁移至您关注的因果推断与纵向数据研究。
- **关键技术**: `linear mixed-effects models`, `compositional data analysis`, `repeated measures`, `geocoded exposure assessment`, `nonlinear spline models`
- **为什么对您有用**: 本文属于流行病学应用论文，直接对应您的 secondary interest 中的流行病学方向。其纵向重复测量设计和成分数据分析方法，与您熟悉的纵向因果推断和 semiparametric 理论有交集，可作为方法迁移的案例。武器库中的 very_familiar 工具（如纵向模型、M-estimation）足以支撑您理解并评估其分析策略，属于立即可读的入门级应用文献。

### 11. [10.1097/ede.0000000000002028](https://doi.org/10.1097/ede.0000000000002028) — Reproductive Health in an Era of Cascading Inequity
- **作者**: Samantha Schildroth, Erin Campbell, Mary D. Willis
- **期刊/来源**: Epidemiology
- **机构**: Boston University · University of New England
- **分类**: vol 37 · issue 6 · pp 784-787
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文是一篇评论性文章，在流行病学“双重危险”假说的基础上提出扩展：环境与社会压力源（如感知压力、经济困难、歧视）的联合暴露可能共同影响生殖健康，而加强社会安全网政策（如健康保险、食品安全、产科护理）可能缓解环境压力源的不良影响。作者利用美国公开数据（健康保险覆盖率、食品安全、医院产科护理，以及空气污染、铅、热浪等环境暴露）绘制了环境压力源与社会资源的地理重叠情况，以支持该扩展假说。文章最后为未来研究提供了建议，强调需严格评估这一扩展框架。作为评论文章，本文没有提出新的统计方法或实证因果推断，主要贡献在于概念框架的提出和基于公开数据的描述性展示。
- **关键技术**: `double jeopardy hypothesis`, `public data mapping`, `descriptive analysis`
- **为什么对您有用**: 本文属于流行病学领域的应用型评论，与您的次要兴趣“流行病学（应用、数据集、因果推断）”相关。作为入门读物，它清晰地阐述了环境与社会压力源联合效应的概念框架，但缺乏严格的统计方法。您的武器库（如因果推断中的敏感性分析、交互作用建模）足以支撑您理解并可能改进其提出的研究建议，但本文本身不提供可直接迁移的方法。因此，值得快速浏览以了解领域背景，但无需深入精读。

### 12. [10.1097/ede.0000000000002019](https://doi.org/10.1097/ede.0000000000002019) — Temporal Connectivity of Social Contact Networks in Urban and Rural India
- **作者**: Dehao Chen, Prasanna Samuel, Rajan Srinivasan, Adrien Le Guillou, Venkata Raghava Mohan, Saad B. Omer et al.
- **期刊/来源**: Epidemiology
- **机构**: Emory University · Christian Medical College, Vellore · The University of Texas Southwestern Medical Center
- **分类**: vol 37 · issue 6 · pp 756-764
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文利用印度泰米尔纳德邦城乡地区的实证社会接触数据，构建了接触-地点特定的网络统计量，并参数化动态网络模型，模拟一年内的每日网络，以计算前向可达路径（FRP）——即从指示病例通过直接或间接接触可到达的人群比例，用于量化急性呼吸道传播的时间连通性。结果显示，城乡网络中平均FRP在第1天急剧上升，随后在学校和工作场所持续增加，而在家庭和其他地点趋于平稳；到第365天，FRP按地点排序为家庭（农村0.06%，城市0.03%）<学校（11.96%，9.14%）<工作（12.55%，26.72%）<其他（40.54%，67.99%）。年龄分层分析显示，≥60岁人群家庭FRP最高，10-19岁人群学校FRP最高，40-59岁人群工作FRP最高。结论指出，尽管家庭FRP受家庭规模限制，但通过学校、工作和其他接触，可达性显著扩展，表明这些环境中急性呼吸道传播具有高时间连通性和显著流行潜力。对您而言，本文展示了动态网络模型与流行病学数据结合的应用范例，其网络模拟和FRP计算框架可能为您的流行病学因果推断研究提供数据生成机制的参考。
- **关键技术**: `dynamic network models`, `forward-reachable path (FRP)`, `contact-location-specific network statistics`, `agent-based simulation`
- **为什么对您有用**: 本文属于流行病学应用，使用动态网络模型量化接触网络的时间连通性，与您的流行病学应用兴趣直接相关；作为gateway reading，它清晰展示了从经验数据到网络参数化再到模拟的完整流程，适合入门；武器库中的软件开发和因果推断估计能力足以支撑理解其模拟框架，但若要深入扩展（如加入干预模拟），需在动态网络模型上稍作学习，属于中期可做。

## 其他  *(other, 1 篇)*

### 1. [10.1097/ede.0000000000002032](https://doi.org/10.1097/ede.0000000000002032) · [arXiv](https://arxiv.org/abs/2603.01091) — Harvest Now, Decrypt Later
- **作者**: Sarah F. Ackley, Michael D. Flanders, Jingxuan Wang
- **期刊/来源**: Epidemiology
- **机构**: Universidad Carlos III de Madrid
- **分类**: vol 37 · issue 6 · pp 848-853
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文从经济学角度重新审视'先收集后解密'（HN-DL）攻击，该攻击通过存档当前加密通信的密文，待未来量子计算机破解密钥交换后解密。作者构建了开源测试平台，模拟 TLS 1.2、TLS 1.3、QUIC 和 SSH 的完整攻击流程，量化了攻击者的存储与量子计算成本。核心发现是，存档截获流量对攻击者而言经济上微不足道，因此防御重点应从'能否存档'转向'解密成本多高'。文章评估了两种独立的防御策略：加密客户端问候（ECH）迫使攻击者进行无差别批量收集，从而膨胀其存档规模；而激进的重密钥和更大的密钥交换参数则增加所需的量子计算量。由于存储膨胀对双方都有代价，而量子成本膨胀仅针对攻击者，重密钥和密钥大小选择是最强的防御杠杆。本文属于网络安全领域的应用性研究，对统计方法无直接贡献，但可作为跨学科入门阅读。
- **关键技术**: `cost modeling`, `protocol analysis`, `open-source testbed`, `quantum workload estimation`
- **为什么对您有用**: 本文属于网络安全领域，与您的主要兴趣（因果推断、高维统计等）无直接关联，但可作为跨学科入门阅读。作为统计学家，您可能对其中'成本-收益'建模的框架感兴趣，但武器库中的统计工具（如 minimax 理论、U-统计量）在此并不适用。因此，本文不值得花时间精读，除非您对网络安全中的经济学建模有特别兴趣。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

