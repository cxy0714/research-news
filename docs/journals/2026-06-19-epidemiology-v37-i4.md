# Epidemiology — Vol 37  Issue 4  ·  2026-06-19

- 共 19 篇 · Epidemiology
- 目录核对 ⚠️ 疑似漏 3 篇（对照 OpenAlex 24 篇）：10.1097/ede.0000000000001944、10.1097/ede.0000000000001986、10.1097/ede.0000000000001988

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期以因果推断方法在流行病学应用中的识别挑战与工具改进为核心，可归纳为三条主线：① 因果识别偏倚的批判与诊断（碰撞变量、知情存在、无混杂性评估、多重版本治疗、可迁移性假设）；② 生存分析与加权方法在时间事件研究中的新应用（疫苗效力的PWP-GT frailty模型、分布式滞后模型、逆强度加权、事后分层）；③ 传统流行病学设计的合理性检验（病例交叉、空间贝叶斯、合成队列、目标试验模拟）。其中前两条篇幅最集中，且直接涉及因果推断的基本假设与估计量构建。

第一条主线聚焦因果效应识别中易被忽视的偏倚来源及其检验策略。Improving Inference in Air Pollution Epidemiology 用有向无环图系统论证了多污染物调整中碰撞变量偏倚的机制与规模，强调变量选择需理论指导。Informed Presence in Electronic Health Record Data 将知情存在偏倚纳入数据缺失框架，展示了逆强度加权与多重删失在纵向数据中的纠偏效果。Empirically Assessing the Plausibility of Unconfoundedness 提出一种仅基于协变量与结局条件关联的经验诊断，用于评估无混杂性假设是否被数据违反。Latent Variation in Pathogen Strain-specific Effects 在多重版本治疗框架下形式化菌株异质性对效应可迁移性的约束，揭示标准风险比依赖于菌株流行频率。Re: Generalizing and Transporting Causal Inferences 讨论了试验参与效应缺失时识别公式的简化条件，与Defining and Estimating Outcomes Directly Averted 一文对疫苗直接避免结局的定义和偏倚分析（风险差估计量在易感者耗竭下的系统性高估）共同构成对因果估计量定义与跨场景迁移的严谨审视。此外，The Illusion of the “Self-correcting” Nature of Science 以一个失败方法（残差非线性孟德尔随机化）为例，警示因果推断中假设检验与撤销机制的不完善。

第二条主线是时间事件框架与重加权方法的结合。Improving Assessment of Vaccine Effectiveness 将检验阴性设计重构为队列生存分析，引入PWP-GT frailty模型处理重复感染与时变疫苗状态，优于常规logistic回归。Temporal Variation in PM2.5 and Mortality 采用病例交叉设计配合非线性时间模型，刻画短期效应的时间趋势及其亚组异质性。The Association Between Outdoor Temperature and Fluid Homeostasis 使用分布式非线性滞后模型分离冷/热温度在不同滞后期的效应曲线。Illustrating Poststratification Methods 系统比较事后分层、raking、MRP与逆概率加权在非概率样本中的校正效果。Informed Presence 也归属于此主线（逆强度加权）。

与因果推断方向最贴、适合优先阅读的论文包括：Improving Inference in Air Pollution Epidemiology（变量选择与碰撞偏倚）、Informed Presence in Electronic Health Record Data（知情存在与加权）、Empirically Assessing the Plausibility of Unconfoundedness（无混杂性检验）、Latent Variation in Pathogen Strain-specific Effects（多重版本治疗的可迁移性）、Defining and Estimating Outcomes Directly Averted（疫苗直接效应的定义与偏倚）、Re: Generalizing and Transporting Causal Inferences（试验参与效应下的识别）。此外，Improving Assessment of Vaccine Effectiveness 将TND识别与生存分析结合，也值得关注。

## 因果推断  *(causal_inference, 3 篇)*

### 1. [10.1097/ede.0000000000001985](https://doi.org/10.1097/ede.0000000000001985) · [arXiv](https://arxiv.org/abs/2402.10156) — Empirically Assessing the Plausibility of Unconfoundedness in Observational Studies
- **作者**: Fernando Pires Hartwig, Kate Tilling, George Davey Smith
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 4 · pp 515-522
- 相关性 8/10 · novelty: `weaker_assumption`
- **摘要**: 本文针对观察性研究中无混杂性（unconfoundedness）假设因不可观测混杂而易失效的问题，提出一种简单策略来经验性评估条件无混杂性（conditional unconfoundedness）的合理性。该方法不要求对混杂结构做显式假设，仅依赖暴露、结局与协变量之间的时间顺序及研究选择机制（可由设计保证）。核心步骤是检验调整集中与暴露相关的协变量子集（给定其他协变量）与结局的条件关联；若关联显著，则暗示无混杂性可能不成立。作者给出理论证明，通过模拟验证了方法的有限样本表现，并利用1982年Pelotas出生队列数据演示了分娩方式对智商因果效应的评估。论文还讨论了测量误差的影响及方法的主要局限。该工作直接连接因果推断中的敏感性分析传统，提供一个无需先验混杂知识的实用工具。
- **关键技术**: `conditional unconfoundedness`, `temporal ordering assumption`, `covariate-outcome association test`, `simulation-based validation`, `sensitivity analysis`
- **为什么对您有用**: 本文属于因果推断中不可观测混杂评估的应用方法，直接对应您在敏感性分析方向的兴趣。您可以利用very_familiar中的estimation theory in causal inference快速理解并扩展此方法，例如将其与proximal causal inference中的negative control概念结合以强化检验力。该方法假设弱、操作简单，立即可做：可直接复现模拟或应用于您手头的观察性研究数据。

### 2. [10.1097/ede.0000000000001953](https://doi.org/10.1097/ede.0000000000001953) · [arXiv](https://arxiv.org/abs/2509.05508) — Defining and Estimating Outcomes Directly Averted by a Vaccination Program when Rollout Occurs Over Time
- **作者**: Katherine M. Jia, Christopher B. Boyer, Alyssa Bilinski, Marc Lipsitch
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 4 · pp 408-416
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文聚焦COVID-19疫苗推广背景下如何定义和估计“直接避免结局”——即固定疫苗覆盖率下疫苗接种对接种者自身的因果效应。作者首先形式化了该因果估计量，指出它是总避免结局（包含间接效应）的下限。在单阶段随机对照试验中，他们推导了一个无偏估计量。接着，他们系统分析了流行病学研究中常用的风险差估计量（hazard difference estimator）的偏倚，证明即使在RCT中，若疫苗有效，该估计量也会因未接种人群易感者更快耗竭而产生系统性高估。仿真显示，当感染病死率较低时（如COVID-19），对死亡的高估较小；但对感染终点且基本再生数高、疫苗效力高时，高估可很严重。论文还定义了“可避免结局”及其估计量，并指出未来可探讨观测研究中的可识别性。这为疫苗效果评估的因果推断提供了明确概念框架和偏倚诊断工具。
- **关键技术**: `causal estimand definition`, `hazard difference estimator`, `depletion of susceptibles`, `direct effect vs total effect`, `bias analysis`, `simulation calibration`
- **为什么对您有用**: 本文直接对接您在流行病学中应用因果推断的二级兴趣，尤其是疫苗效果评估中估计量的识别与偏倚分析。您可以用非常熟悉的“estimation theory in causal inference”来评估其无偏估计量的方差、推广至观测研究下的半参数估计；也可用“identification theory”讨论混杂调整下该估计量的可识别性条件。这是一个立即可做的工作——论文核心概念简单，您完全有能力将其中思路扩展到更复杂的纵向接种方案或工具变量设定中。

### 3. [10.1097/ede.0000000000001969](https://doi.org/10.1097/ede.0000000000001969) · [arXiv](https://arxiv.org/abs/2407.14703) — Re: Generalizing and Transporting Causal Inferences from Randomized Trials in the Presence of Trial Engagement Effects
- **作者**: Rachael K. Ross, Kara E. Rudolph, Daniel Malinsky
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 4 · pp e10-e11
- 相关性 7/10 · novelty: `minor`
- **摘要**: 本文是对 Ung 等人关于在存在试验参与效应时跨人群迁移因果推断的回复与补充，聚焦于试验参与效应（S→Y）不存在时的识别问题。在无 S→Y 边的 DAG 与 SWIG 下，目标 estimand E(Y^a) 的识别仅需标准可交换性与一致性假设，通过 g-formula 退化为 E(E(Y|X,A=a,S=1))。核心机制是利用 S=1 条件下的可交换性，将潜在结果期望链式分解为可观测量的条件期望，无需额外调节试验参与变量。该识别公式实质上是标准 transportability / generalizability 在无参与效应特例下的简化。对您可能有用：此文清晰展示了 trial engagement 效应存在与否对 identification formula 的结构性影响，是理解 transportability 识别条件变体的简明参考。
- **关键技术**: `transportability`, `generalizability`, `trial engagement effects`, `identification via g-formula`, `SWIG (Single World Intervention Graph)`
- **为什么对您有用**: 直接连接因果推断中的 identification theory 与 transportability 子方向，展示了 trial engagement 效应这一结构性假设如何改变目标 estimand 的识别公式。用您 very_familiar 的 identification theory in causal inference 即可完全解析其 DAG 与 SWIG 的识别链，判断其逻辑完备性。属于**立即可做**：无需额外工具即可将此无参与效应的识别条件与您熟悉的 semiparametric efficiency bound / HOIF 框架对接，思考在更复杂 longitudinal 设定下参与效应的识别与估计。

## 流行病学  *(epidemiology, 16 篇)*

### 1. [10.1097/ede.0000000000001972](https://doi.org/10.1097/ede.0000000000001972) — Improving Assessment of Vaccine Effectiveness by Coupling Test-negative Design Studies with Survival Models
- **作者**: Shangchen Song, Matt D. T. Hitchings, Yang Yang, Ira M. Longini, on behalf of the N3C consortium
- **期刊/来源**: Epidemiology
- **机构**: University of Florida · University of Georgia · Franklin College
- **分类**: vol 37 · issue 4 · pp 417-426
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在疫苗有效性评估的检验阴性设计（TND）框架下，指出传统的病例-对照视角可重新表述为队列研究的特例，从而允许使用生存分析模型。作者引入Prentice-Williams-Peterson gap-time（PWP-GT）frailty模型，该模型能够同时考虑重复感染事件和时变疫苗接种状态，比常规logistic回归更贴合实际流行病学过程。通过大量模拟研究，文章展示了所提模型在估计有效性时的优势。最后，作者利用美国国家COVID队列协作组织（N3C）的真实数据，估计了辉瑞疫苗在奥密克戎流行期间对初次感染和再感染的有效性。对于您而言，这是一篇将因果推断概念（TND的识别）与生存分析技术结合的应用论文，直接对应您对流行病学中因果推断方法的应用兴趣。
- **关键技术**: `Test-negative design`, `Cohort study re-framing`, `Prentice-Williams-Peterson gap-time (PWP-GT) frailty model`, `Recurrent event survival analysis`, `Time-dependent vaccination status`
- **为什么对您有用**: 该论文直接属于您的二级兴趣方向：流行病学中的因果推断应用，特别关注TND设计在疫苗有效性估计中的新方法。您可以将非常熟悉的'estimation theory in causal inference'用于分析该PWP-GT模型与传统logistic TND的偏差-方差权衡，此项工作可立即跟进（立即可做）：形式化该队列重构下的识别条件或扩展至时变混杂。

### 2. [10.1097/ede.0000000000001967](https://doi.org/10.1097/ede.0000000000001967) — Improving Inference in Air Pollution Epidemiology: The Case for Rethinking Multipollutant Adjustment
- **作者**: Hong Chen, Matthew Quick, Jay S. Kaufman, Chen Chen, Jeffrey C. Kwong, Juwel Rana et al.
- **期刊/来源**: Epidemiology
- **机构**: Health Canada · University of Ottawa · University of Toronto · Public Health Ontario · Statistics Canada · McGill University · Scripps Institution of Oceanography · University of California San Diego 等
- **分类**: vol 37 · issue 4 · pp 427-436
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文指出空气污染流行病学中常用的多污染物调整方法存在严重偏倚风险。当回归模型同时调整多个共污染物时，若其中某些共污染物是暴露和结局的共同原因（混杂）或受暴露影响的中介/碰撞变量，则调整碰撞变量会人为打开非因果路径，导致效应估计失真。作者通过一个有良好特征的加拿大全国队列数据与模拟研究，展示了这种偏倚在实际规模上如何影响污染物-健康关系的推断。他们进一步讨论了基于有向无环图的变量选择策略以及敏感性分析等缓解方法。本文是对流行病学实践中常见做法的批判性审视，强调因果推断的变量选择需要理论指导而非统计拟合。作为流行病学应用文章，它清楚展示了因果推断中碰撞变量偏倚的机制和影响，对您理解实际数据中的识别问题有直接帮助。
- **关键技术**: `collider bias`, `multipollutant adjustment`, `directed acyclic graphs`, `simulation-based bias quantification`, `sensitivity analysis`
- **为什么对您有用**: 本文属于次级兴趣（流行病学）中的因果推断应用，核心是碰撞变量偏倚的识别与缓解，直接连接到您主要兴趣中的因果推断identification理论。您武器库中的'estimation theory in causal inference'足以理解其偏倚机制和模拟设计，'identification theory in causal inference'可用于评估其提出的策略是否充分。这是一篇优秀的入门读物：不需要领域先验即可理解其论证结构，且问题（多污染物调整）在流行病学中普遍存在，值得花时间全文阅读以掌握此类偏倚的典型模式。

### 3. [10.1097/ede.0000000000001987](https://doi.org/10.1097/ede.0000000000001987) — The Illusion of the “Self-correcting” Nature of Science
- **作者**: George Davey Smith
- **期刊/来源**: Epidemiology
- **机构**: University of Bristol
- **分类**: vol 37 · issue 4 · pp e8-e8
- 相关性 7/10 · novelty: `minor`
- **摘要**: 本文以残差非线性孟德尔随机化方法为例，批判了科学“自我纠正”的幻觉。该方法最初发表于Epidemiology，旨在通过遗传工具变量估计非线性因果效应，但后续研究发现其可能产生违背逻辑的结果，甚至重现观测关联而非因果效应。尽管部分明显错误的论文已被撤稿，但多数问题论文未被纠正，新论文仍持续引用该方法。作者呼吁期刊对问题方法增加警示标识，以减缓错误结论的扩散。本文是一篇评论文章，不提出新方法，但对流行病学中心方法论误用提供了重要警示。对于关注因果推断的统计学家，本文展示了孟德尔随机化中识别假设失败的具体案例。
- **关键技术**: `Mendelian randomization`, `residual nonlinear method`, `self-refuting findings`, `retraction and correction policy`
- **为什么对您有用**: 本文是流行病学方法误用的典型案例，与研究者的secondary interest（流行病学应用）直接相关。研究者已有的因果推断识别理论与估计理论（very_familiar工具箱中的estimation theory in causal inference）足以理解该方法的谬误根源。作为入门读物很合适，清晰阐述了工具变量法中非线性估计的潜在陷阱，值得通读全文。

### 4. [10.1097/ede.0000000000001975](https://doi.org/10.1097/ede.0000000000001975) · [arXiv](https://arxiv.org/abs/2602.06262) — Latent Variation in Pathogen Strain-specific Effects Under Multiple-Versions-of-Treatment Theory
- **作者**: Bronner P. Gonçalves
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 4 · pp 490-493
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文在多重版本治疗框架下探讨病原体菌株特异性效应对感染结局的因果解释。当研究者缺乏菌株亚型信息时，报告中常用的效应估计量（如菌株特异性风险比）的因果含义依赖于感染菌株在目标人群中的流行频率。作者使用潜在结果形式化推导，指出治疗变异无关假设通常被违反，导致此类效应不具有普遍可迁移性，必须额外考虑菌株分布的可移植条件。文章核心是概念澄清而非新估计量推导，但揭示了忽略菌株异质性时标准因果推断的潜在偏误。对流行病学研究者而言，本文提供了一种简洁的理论透镜，可用于评估现有感染病研究结论的稳健性，并凸显收集病原体亚型数据的方法学价值。由于该领域实证数据丰富，本文的框架可直接应用于疫苗有效性或疾病严重性的比较研究。
- **关键技术**: `potential outcomes`, `multiple versions of treatment`, `treatment-variation-irrelevance assumption`, `transportability`, `strain-specific effects`
- **为什么对您有用**: 本文是流行病学中应用因果推断的入门级概念阐释，清晰连接了你对因果识别理论的兴趣（moderate_familiar 中的 identification theory in causal inference）。全文逻辑不依赖高深技术，现有武器库中的非参因果推断工具足以立即理解，可作为与流行病学家交流时的背景知识，但本身不提供新的方法论推进，故仅作快速阅读即可。

### 5. [10.1097/ede.0000000000001974](https://doi.org/10.1097/ede.0000000000001974) — Informed Presence in Electronic Health Record Data: Illustrating Bias and Bias Reduction Approaches in Longitudinal Analyses
- **作者**: Daniel T. Vader, Di Shu, Rebecca A. Hubbard, Craig L. K. Boge, Anna Sharova, Kevin Downes et al.
- **期刊/来源**: Epidemiology
- **机构**: Drexel University · University of Pennsylvania · Brown University · Children's Hospital of Philadelphia
- **分类**: vol 37 · issue 4 · pp 523-531
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文聚焦电子健康记录数据中「知情存在偏倚」对纵向关联估计的影响，该偏倚源于数据采集与患病状态相关，使得观测过程成为暴露和结局的共同因，从而产生 collider bias。作者给出了一个概念性框架，将知情存在偏倚视为数据缺失机制依赖于暴露和结局时，传统的完全随机缺失假设被违反。方法上，本文采用逆强度加权（inverse intensity weighting）和多重删失（multiple outputation）两种重加权/重采样策略，以恢复观测过程与结局的条件独立性。通过一项儿科实体器官移植受者（N=271）的真实数据，展示糖皮质激素与巨细胞病毒血症关联的估计：朴素分析的发病率比（IRR）为1.83（1.02, 3.28），经逆强度加权校正后降至1.37（0.73, 2.57），自举逆强度加权和多重删结果类似。作者建议研究者基于有向无环图识别观测过程的依赖结构，并在分析中明确处理结局依赖的访问模式。本文对您有用在于：它展示了一个流行病学中常见但鲜有系统讨论的偏倚来源，以及如何用加权方法进行敏感性分析，直接对应您 secondary interest 中流行病学的纵向因果推断应用场景。
- **关键技术**: `inverse intensity weighting`, `multiple outputation`, `bootstrapped inverse intensity weighting`, `collider bias framework`, `conditional independence assumption`, `directed acyclic graph (DAG) for visit process`
- **为什么对您有用**: 本文属于流行病学应用，直接连接您的 secondary interest 中「纵向因果推断的应用数据集」子方向。您 technical arsenal 中 very_familiar 的「estimation theory in causal inference」可立即理解逆强度加权的权重构造与 IPW 思想，且您对「非参数统计」和「高维渐近」的熟悉度足以评估该方法的假设合理性。本文给出的是概念性框架而非新理论，作为 gateway reading 值得快速浏览，以了解 EHR 数据中偏倚来源的 DAG 表述和实际衰减效应。follow-up 粗判：立即可做——您无需新工具就能消化并评估该方法是否可移植到您接触的纵向数据中。

### 6. [10.1097/ede.0000000000001980](https://doi.org/10.1097/ede.0000000000001980) — Illustrating Poststratification Methods in Medical Claims Data: A Korean Example
- **作者**: Yeon Woo Oh
- **期刊/来源**: Epidemiology
- **机构**: Yonsei University
- **分类**: vol 37 · issue 4 · pp 494-503
- 相关性 7/10 · novelty: `application`
- **摘要**: 在非概率样本（韩国 NHIS 健康检查数据）存在自愿参与导致的抽样偏差设定下，目标是校正肥胖患病率与自报疾病敏感度的 population-level 估计。本文实证比较了四种重加权方法：simple poststratification、raking、multilevel regression with poststratification (MRP) 以及 inverse probability sampling weights，以 KNHANES 调查为参考标准。核心机制是利用辅助变量（年龄、性别、吸烟、饮酒、区域）的边缘或联合分布对样本重加权，MRP 通过 multilevel model 在小区域子群中平滑估计后再 poststratification。结果显示 crude 肥胖率 36.3% 经各方法校正后降至 33.9%–34.7%，更接近参考值 31.4%，但仍有残余偏差；IPW 与 simple poststratification 结果相近。对您而言，本文展示了流行病学行政数据中 generalizability / transportability 校正的典型流程，可作为了解 epi 应用数据集与重加权策略的入门阅读。
- **关键技术**: `poststratification`, `raking`, `multilevel regression with poststratification (MRP)`, `inverse probability sampling weights`, `generalizability of nonprobability samples`
- **为什么对您有用**: 本文属于流行病学应用方向，展示了行政数据中非概率样本 generalizability 校正的实证流程，是了解 epi 数据结构与重加权实践的入门读物。研究者武器库中的 identification theory in causal inference 与 semiparametric theory 可以直接审视本文 IPW 与 poststratification 的理论基础（如 transportability identification 条件、效率界），但本文本身方法学 novelty 较低，仅是已有方法的实证比较。判断：立即可做——用 very_familiar 的 estimation theory in causal inference 可以分析这些重加权估计量的 semiparametric efficiency bound 与残余偏差来源，但本文仅值得快速浏览数据部分，无需深读全文。

### 7. [10.1097/ede.0000000000001991](https://doi.org/10.1097/ede.0000000000001991) — Electrical Power Outages and Asthma-related Emergency Department Visits in New York City, 2018–2022
- **作者**: Nina M. Flores, Kara E. Rudolph, Ariel Spira-Cohen, Sarah Walters, Vivian Do, Alexander J. Northrop et al.
- **期刊/来源**: Epidemiology
- **机构**: Columbia University · New York City Department of Health and Mental Hygiene · Global Policy Institute · University of Washington
- **分类**: vol 37 · issue 4 · pp 544-552
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文研究纽约市2018–2022年停电对哮喘急诊就诊的影响，estimand为停电暴露对哮喘ED visit的因果效应。作者整合了纽约州公共服务部（区域级）与NYCHA（建筑级）两套停电数据与行政急诊数据，分别采用augmented synthetic control方法评估四次大规模停电的关联效应，以及case-crossover设计评估建筑级当日停电暴露的OR。结果显示2019年7月21日局部大停电与当晚哮喘急诊率增加0.20/1000相关；NYCHA居民夏季停电日哮喘急诊OR为2.23（95% CI 0.92–5.37），儿童及滞后0–1天效应更突出。对您而言，本文展示了流行病学因果研究中augmented synthetic control与case-crossover的具体应用场景，可作为secondary interest中epidemiology应用因果方法的实证参考。
- **关键技术**: `augmented synthetic control`, `case-crossover design`, `sub-daily time-series analysis`, `lagged exposure modeling`, `administrative health data linkage`
- **为什么对您有用**: 本文直接连接到secondary interest中epidemiology的因果推断应用，展示了augmented synthetic control与case-crossover在环境健康因果效应估计中的实操流程。从technical_arsenal看，您对identification theory in causal inference（very_familiar）足以理解其identification策略，但augmented synthetic control的具体理论细节需在moderately_familiar的semiparametric theory上稍作补充。作为epidemiology因果应用的入门实证案例，值得花时间浏览方法与数据链接部分，但理论novelty有限，无需深读全文。

### 8. [10.1097/ede.0000000000001984](https://doi.org/10.1097/ede.0000000000001984) — Association of Maternal Gestational Diabetes Mellitus with Infant Visual Acuity Development
- **作者**: Xue You, Hui Zhu, Mengting Jiang, Yonghui Gu, Yangqian Jiang, Tao Jiang et al.
- **期刊/来源**: Epidemiology
- **机构**: Nantong University · Taizhou People's Hospital · Nanjing Medical University · Suzhou Municipal Hospital · Third Affiliated Hospital of Zhengzhou University
- **分类**: vol 37 · issue 4 · pp 479-489
- 相关性 6/10 · novelty: `application`
- **摘要**: 本研究基于江苏出生队列（2014–2018年，2041名母亲、2139名婴儿），探讨母体妊娠期糖尿病（GDM）及其糖耐量亚型对婴儿1岁格栅视力发育的影响。暴露按OGTT结果分为单纯空腹血糖受损、单纯糖耐量受损及两者合并三组；结局为Teller视力卡测量的异常视力。采用广义估计方程（GEE）估计相对风险（RR），并控制双胎观测的组内依赖性；辅以代谢组学分析探索中介通路。结果显示GDM暴露使婴儿视力异常风险增加70%（RR=1.7；95% CI 1.2–2.3），合并亚型风险最高（RR=3.2）；代谢组学提示甘氨酸/丝氨酸/苏氨酸代谢通路及肌酸可能参与该关联。对您而言，本文提供了流行病学队列中GEE处理双胎依赖及代谢组学中介探索的具体应用范例。
- **关键技术**: `generalized estimating equation (GEE)`, `birth cohort design`, `relative risk estimation`, `metabolomics pathway enrichment`, `oral glucose tolerance test (OGTT) subtyping`
- **为什么对您有用**: 本文属于流行病学队列应用，直接对应您 secondary interest 中 epidemiology 的 causal inference 应用与数据集。文中GEE处理双胎依赖性及代谢组学中介探索，可作为您 identification theory 与 semiparametric theory 武器切入的口子——例如用 semiparametric efficiency bound 评估GEE在该依赖结构下的效率，或用 HOIF / higher-order U-statistics 建立代谢物-结局中介的更精细检验。Follow-up 判断：**中期可做**——需先在 moderately_familiar 的 semiparametric theory / identification theory 上长肌肉，才能将队列中的依赖结构与中介识别问题形式化。

### 9. [10.1097/ede.0000000000001952](https://doi.org/10.1097/ede.0000000000001952) — Long-term Cardiovascular Outcomes Following Bariatric Surgery: Reconciling Seemingly Conflicting Evidence
- **作者**: Sebastien Haneuse, Luke Benz, Valerie A. Smith, David Arterburn, Matthew L. Maceijewski
- **期刊/来源**: Epidemiology
- **机构**: Harvard University · Duke University · Durham VA Health Care System · Kaiser Permanente Washington Health Research Institute
- **分类**: vol 37 · issue 4 · pp 467-475
- 相关性 6/10 · novelty: `application`
- **摘要**: 在减重手术对糖尿病患者心血管疾病（CVD）风险的因果效应设定下，近期两项基于VA和Optum数据的研究声称无CVD获益，而既往观察性证据普遍支持风险降低。本文使用Kaiser Permanente数据，通过目标试验模拟（target trial emulation）复现VA研究的设计与分析流程，所得结果仍支持CVD风险降低，与既往证据一致。核心机制在于剖析结果冲突的来源：小样本下的统计有效性问题、可迁移性（transportability）理论提示不同人群本不应期望结果一致，以及“临床试验思维”带来的保守性。本文无新方法学贡献，主要是因果推断设计原则在流行病学实证中的应用与反思。对您可能有用：本文展示了 target trial emulation 与 transportability 在真实流行病学冲突证据中的具体应用，可作为因果推断 identification 与可迁移性理论的实证案例。
- **关键技术**: `target trial emulation`, `transportability`, `evidence triangulation`, `observational causal inference`
- **为什么对您有用**: (1) 直接连接到因果推断的 identification 理论与可迁移性（transportability）子方向，以及流行病学实证应用；(2) 用您 very_familiar 的 identification theory in causal inference 可以直接审视本文 target trial emulation 的设计假设是否完备，用 moderately_familiar 的 transportability 理论可进一步分析人群差异导致的效应异质性；(3) **立即可做**：用现有武器即可复现或扩展其 target trial emulation 设计逻辑，评估其 sensitivity 分析的完备性。

### 10. [10.1097/ede.0000000000001978](https://doi.org/10.1097/ede.0000000000001978) — An Expedited Chart Review Process for Large Database Studies Using Natural Language Processing and Multiwave Adaptive Sampling
- **作者**: Shirley V. Wang, Georg Hahn, Sreedhara Sushama Kattinakere, Mufaddal Mahesri, Haritha S. Pillai, Rajendra Aldis et al.
- **期刊/来源**: Epidemiology
- **机构**: Brigham and Women's Hospital · Harvard University · Center for Drug Evaluation and Research · Harvard Pilgrim Health Care
- **分类**: vol 37 · issue 4 · pp 504-514
- 相关性 5/10 · novelty: `application`
- **摘要**: 在大型医疗索赔数据库与电子健康记录（EHR）链接的设定下，目标是验证基于编码的算法（用于识别健康结局等关键参数）的测量特性，以支持后续的定量偏倚分析（quantitative bias analysis）处理结局误分类问题。核心方法引入两种加速机制：(1) 利用自然语言处理（NLP）辅助标注，减少人工审阅每份图表的时间；(2) 多波次自适应抽样（multiwave adaptive sampling），在性能指标达到预设精度时通过停止规则提前终止验证。实证案例为肥胖患者故意自伤的索赔算法验证，结果显示NLP辅助使单图表审阅时间减少40%，自适应停止规则避免了77%的图表审阅且对性能指标的精度损失有限。对您可能有用：该文展示了流行病学数据库研究中偏倚敏感性分析的上游数据验证流程，是了解定量偏倚分析应用场景的入门读物。
- **关键技术**: `quantitative bias analysis`, `outcome misclassification`, `multiwave adaptive sampling`, `NLP-assisted annotation`, `claims-based algorithm validation`, `stopping rule for precision`
- **为什么对您有用**: (1) 本文连接到流行病学应用因果推断中的定量偏倚分析（quantitative bias analysis）与结局误分类问题，属于您 secondary interest 中 epi 的应用场景；(2) 武器库中 estimation theory in causal inference 与 moderately_familiar 的 identification theory 可以直接切入该文上游的误分类偏倚校正理论部分，但多波次自适应抽样设计涉及 sequential estimation / group sequential 方法，目前不在武器库内；(3) 作为 gateway reading，本文对 EHR 数据结构与验证流程的展示清晰易懂，值得花时间读全文以了解偏倚敏感性分析在流行病学中的实际数据需求与操作范式。

### 11. [10.1097/ede.0000000000001979](https://doi.org/10.1097/ede.0000000000001979) — Income Volatility During Early to Mid-adulthood and 10-year Memory Decline in a Longitudinal Synthetic Cohort
- **作者**: Katrina L. Kezios, Scott C. Zimmerman, Peter T. Buto, Maria Glymour, Adina Zeki Al Hazzouri
- **期刊/来源**: Epidemiology
- **机构**: Columbia University · University of California, San Francisco
- **分类**: vol 37 · issue 4 · pp 532-543
- 相关性 5/10 · novelty: `application`
- **摘要**: 研究利用合成队列探讨成年早期到中期的收入波动对十年记忆衰退的影响。通过链接两个美国队列NLSY79和HRS，将HRS参与者匹配到NLSY79中20个最相似的个体并赋予收入波动史。采用含混杂调整的线性混合模型估计收入波动对基线记忆功能和10年衰退的效应。结果发现高收入波动与较低的基线记忆功能相关（如经历≥3次收入下降≥25%者记忆分数低0.60分），但与记忆衰退速率无关。结论表明收入波动可能影响中年记忆功能，但因果解释受限于队列链接假设和未测量混杂。本文对流行病学纵向数据匹配和合成队列构建提供了详细案例分析，适合作为流行病学因果推断应用实践的入门阅读材料。
- **关键技术**: `synthetic cohort construction`, `nearest neighbor matching on linking variables`, `longitudinal linear mixed models`, `confounder adjustment`, `income volatility measurement`
- **为什么对您有用**: 本文是流行病学应用，使用合成队列设计研究收入波动与认知衰退的关系，数据构建部分清晰，可作为流行病学纵向因果推断实践的入门读物。武器库中‘identification theory in causal inference’可帮助理解其匹配策略的识别假设（如可交换性、一致性），无需新工具即可理解全文。虽然方法学贡献有限，但数据链接和分析思路值得阅读，有助于扩展流行病学实证经验。

### 12. [10.1097/ede.0000000000001983](https://doi.org/10.1097/ede.0000000000001983) — Validity of Military Service as Reported on U.S. Death Certificates
- **作者**: Candice Y. Johnson, Lucy Akushevich, Heather R. Batchelder, Ashley E. Price, Katelyn M. Holliday, Elliot D. Hill et al.
- **期刊/来源**: Epidemiology
- **机构**: Duke University Health System · Michigan State University
- **分类**: vol 37 · issue 4 · pp 553-558
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文评估美国死亡证书上军人服役身份报告的效度，目标参数为 misclassification 的 sensitivity、specificity 及预测值，以支持后续军事人群死亡率研究的定量偏倚分析。数据来自 2014–2021 年五州 467,075 份死亡证书，与国防部人力数据中心记录通过 SSN 链接。核心发现：军人服役的 sensitivity 为 81.5%（女性仅 72.3%，未服现役者仅 63.5%），specificity 为 99.5%，存在系统性 underreporting。方法上仅做分层描述性统计与 CI 估计，未涉及建模或因果推断框架。对您有用之处在于：该文提供了具体的 misclassification bias 参数，可直接作为流行病学因果研究中 sensitivity analysis 的输入。
- **关键技术**: `record linkage`, `misclassification bias parameters`, `quantitative bias analysis`, `sensitivity and specificity estimation`
- **为什么对您有用**: 本文属于流行病学应用，直接连接您 secondary interest 中 epidemiology 的 causal inference 与 sensitivity analysis 子方向——它给出了 exposure misclassification 的具体参数，正是您做 quantitative bias analysis 时需要的输入。从 technical_arsenal 看，您用 identification theory in causal inference 的武器即可对这类 misclassification 做更系统的 correction framework，属于**立即可做**的延伸。但本文本身方法学 novelty 极低（纯描述性频率统计），作为了解死亡证书数据偏倚结构的入门读物尚可，不值得花时间深读全文。

### 13. [10.1097/ede.0000000000001977](https://doi.org/10.1097/ede.0000000000001977) — Temporal Variation in the Association Between Short-term Exposure to Fine Particulate Matter and Mortality Across Subpopulations in North Carolina and Michigan, U.S.
- **作者**: Rory K. Stewart, Honghyok Kim, Yimeng Song, Hayon Michelle Choi, Chen Chen, Yongsoo Choi et al.
- **期刊/来源**: Epidemiology
- **机构**: Yale University · University of Illinois Chicago · Harvard University · Scripps Institution of Oceanography · University of California San Diego
- **分类**: vol 37 · issue 4 · pp 456-466
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文利用病例交叉设计（case-crossover design）分析2001–2016年间美国北卡罗来纳州和密歇根州65岁以上老年人短期PM2.5暴露与死亡风险的关联随时间的变化趋势。采用条件逻辑回归（conditional logistic regression）估计每10 μg/m³ PM2.5增加的死亡比值比（OR），并引入非线性时间模型（如样条或分段线性）刻画OR的逐年变化。进一步按年龄、性别、种族/族裔、教育程度、城乡和州内区域进行亚组分析，以探索时间趋势在不同亚群中的异质性。结果显示：北卡罗来纳的PM2.5-死亡OR从前期（2001–2008）到后期（2009–2016）下降了约0.77%，而密歇根上升了0.28%；非线性模型表明北卡罗来纳的关联随时间波动，密歇根则持续上升。还发现环境健康不平等可能随时间加剧：密歇根非西班牙裔黑人亚群的OR增幅（+1.71%）显著高于非西班牙裔白人（+0.14%）。该研究对您作为流行病学应用（secondary interest）的入门读物很有价值，可帮助熟悉环境健康领域常用的病例交叉设计及其亚组分析实践。
- **关键技术**: `case-crossover design`, `conditional logistic regression`, `time-varying effect modification`, `nonlinear temporal model`, `subgroup analysis`
- **为什么对您有用**: 本文是环境流行病学应用论文，属于研究者secondary interest中的流行病学领域。研究者已有的因果推断估计理论（very_familiar中的estimation theory in causal inference）足以理解病例交叉设计的逻辑和条件逻辑回归的估计原理，因而可作为理解环境健康实证研究的入门读物。该论文展示了亚组分析在揭示健康不平等时间趋势中的应用，值得花时间读全文以了解环境流行病学数据集结构和分析流程。

### 14. [10.1097/ede.0000000000001970](https://doi.org/10.1097/ede.0000000000001970) — Spatial Heterogeneity in Synergistic Effects of Extreme Heat and NO2 Exposures on Cardiorespiratory Hospitalizations in California
- **作者**: Yiqun Ma, Chen Chen, Rosana Aguilera, Alexander Gershunov, Michael Jerrett, Rachel Connolly et al.
- **期刊/来源**: Epidemiology
- **机构**: Scripps Institution of Oceanography · University of California San Diego · Los Angeles County Department of Public Health · University of California, Los Angeles · Inserm · École des Hautes Études en Santé Publique · Institut de Recherche en Santé, Environnement et Travail · Université de Rennes
- **分类**: vol 37 · issue 4 · pp 437-446
- 相关性 4/10 · novelty: `application`
- **摘要**: 在2000–2019年加州ZCTA层面队列中，研究极端高温与NO₂暴露对心肺住院的协同效应（RERI）及其空间异质性。方法上，先做state-level case-crossover分析，再通过within-community matched设计结合spatial Bayesian hierarchical model估计ZCTA-specific RERI，最后用meta-regression探索社区特征对效应的修饰作用。全州层面协同效应微弱（RERI=0.005, 95% CI含0），但ZCTA层面RERI范围从-1.08到2.22，呈现巨大空间异质性；低SES、高人口密度、少绿地及高历史温度社区的RERI更高。对您可能有用：本文是流行病学中评估exposure interaction（RERI）与空间异质性的典型应用，展示了matched design与Bayesian hierarchical model在多暴露协同因果效应估计中的实际用法。
- **关键技术**: `case-crossover design`, `relative excess risk due to interaction (RERI)`, `spatial Bayesian hierarchical model`, `within-community matched design`, `meta-regression for effect modification`
- **为什么对您有用**: (1) 连接到流行病学secondary interest中的因果推断应用，具体是多暴露协同效应的RERI估计与空间异质性刻画。(2) 武器库中moderately_familiar的identification theory in causal inference可以用来审视RERI的identification条件（如是否需要no-unmeasured-confounding for joint exposure），very_familiar的high-dimensional asymptotics与software development可切入其spatial Bayesian hierarchical model的估计与计算瓶颈。(3) **中期可做**：若想在此类流行病学数据上做方法学改进（如用DML/semiparametric效率界替代Bayesian hierarchical model估计RERI），需先在moderately_familiar的semiparametric theory上长肌肉，特别是多暴露交互效应的efficient influence function推导。

### 15. [10.1097/ede.0000000000001973](https://doi.org/10.1097/ede.0000000000001973) — Validation of Body Mass Index-For-Age Percentile Curves in Older Adults Using Data From the Canadian Longitudinal Study on Aging
- **作者**: Christopher D. Kim, Claire E. Cook, Hailey R. Banack
- **期刊/来源**: Epidemiology
- **机构**: 3M (United States) · University of Toronto
- **分类**: vol 37 · issue 4 · pp 559-564
- 相关性 3/10 · novelty: `application`
- **摘要**: 该文利用加拿大老龄化纵向研究（CLSA）数据（n=28,764），验证了年龄别BMI百分位数曲线在老年人中作为肥胖筛查工具的有效性。将BMI≥85th百分位数定义为肥胖，与DXA测得的总体脂百分比（BF%）≥40%的金标准比较，计算了灵敏度、特异度、阳性预测值和阴性预测值。结果显示女性中灵敏度仅0.32、特异度0.98、PPV 0.94、NPV 0.61；男性中灵敏度0.85、特异度0.86、PPV 0.14、NPV 1.00。表明年龄别BMI百分位数特异度高但灵敏度因性别而异，尤其女性中漏诊率较高。研究提示现有肥胖判别标准对老年人可能不够准确，但年龄别百分位数作为筛查工具仍有潜力。对统计研究者的价值在于，这是一例经典的诊断测试评估典范，可学习流行病学中分类性能指标的计算与解释，并思考如何用更先进的统计方法（如bootstrap置信区间、AUC比较）改进分析。
- **关键技术**: `sensitivity and specificity analysis`, `positive predictive value`, `negative predictive value`, `BMI-for-age percentiles`, `binary classification with gold standard`
- **为什么对您有用**: 作为流行病学应用的入门读物，本文方法简单、数据规模大，适合快速了解队列研究中诊断测试评估的设计与报告范式。研究者武器库中的非参数统计、估计理论和软件技术完全足以理解并复现此类分析，但方法学贡献有限，不涉及因果推断或高维统计。如果希望进入流行病学领域，这篇全文值得一读以建立直观；如果只想了解分析模式，读摘要和图表即可。

### 16. [10.1097/ede.0000000000001968](https://doi.org/10.1097/ede.0000000000001968) — The Association Between Outdoor Temperature During the Past Weeks and Current Fluid Homeostasis
- **作者**: Sofia Enhörning, Olle Melander, Sölve Elmståhl, Gunnar Engström, Mats Pihlsgård, Simon Timpka
- **期刊/来源**: Epidemiology
- **机构**: Malmö University · Skåne University Hospital · Lund University
- **分类**: vol 37 · issue 4 · pp 447-455
- 相关性 3/10 · novelty: `application`
- **摘要**: 在瑞典五个人群队列（n=29,755）的纵向设定下，研究过去21天户外温度对当前体液稳态（copeptin、尿渗透压、总水摄入）的非线性关联，核心estimand是温度-体液指标的滞后因果曲线。方法上采用分布式非线性滞后模型（distributed nonlinear lag models），刻画冷/热温度在不同滞后窗口对copeptin和尿渗透压的异质性效应；结果显示持续0°C 21天使copeptin升高14.9%（95% CI: 11.5%–18.3%），而高温效应仅持续24小时内。本文为流行病学观察性研究，方法学novelty有限，但提供了温度-体液-健康的潜在因果链假说与大规模队列数据。对您可能有用：若将温度视为连续处理、体液指标为中介，该数据结构可作为 longitudinal mediation / sensitivity analysis 的实证场景。
- **关键技术**: `distributed lag nonlinear model`, `longitudinal cohort analysis`, `vasopressin biomarker (copeptin)`, `nonlinear exposure-response curve`, `lag structure estimation`
- **为什么对您有用**: 本文属于流行病学应用，连接到您 secondary interest 的 epidemiology (datasets, applied causal work)：提供了大规模纵向队列数据与连续暴露（温度）-中介（体液稳态）-结局的因果链假说。从 technical_arsenal 看，您 very_familiar 的 causal inference estimation theory 与 moderately_familiar 的 identification theory in causal inference 可以直接攻这篇 paper 的方法缺口——它目前仅做 association，未做 longitudinal mediation identification 或 sensitivity analysis，这是您可切入的具体口子。Follow-up 判断：**立即可做**——用 very_familiar 的因果推断工具（mediation identification + sensitivity）对该数据结构重新建模，将温度-体液-健康的 association 升格为 formal causal mediation 分析。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

