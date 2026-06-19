# Epidemiology — Vol 37  Issue 3  ·  2026-06-19

- 共 18 篇 · Epidemiology
- 目录核对 ⚠️ 疑似漏 2 篇（对照 OpenAlex 20 篇）：10.1097/ede.0000000000001950、10.1097/ede.0000000000001957

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期《Epidemiology》第37卷第3期共18篇论文，可归纳为三条主线：**因果识别与推断方法**（目标试验框架、同胞比较设计、缺失数据处理、immortal time bias）、**测量偏差与算法验证**（报告差异、孕周估计算法、心理测量新指标）、**其他方法论**（时间离散化、公平性量化、化学物浓度标准化、计算优化）。因果推断是本期最密集的主题，覆盖从目标试验协议制定到具体偏倚来源的处理。

**因果识别与推断**方面，多篇论文聚焦于如何在不同设定下获得有效因果估计。《Where Do Target Trials Come From?》讨论了目标试验方案在观察数据中的迭代制定过程，强调透明记录与平衡研究问题与数据约束；《Applying the Target Study Conceptual Model》则直接应用该框架测量种族差异中的“允许协变量”效应，并用逆概率加权反转了粗估计方向。《Sibling Comparison Designs to Assess Social Exposures and Empirical Tools to Guide Interpretation》及其后续评论（《Re: Confounders, Mediators, or Colliders》）分别从实证工具和协变量角色判定切入，揭示同胞比较设计在控制共享混杂时的条件性与局限性。《Mind the Gap》与《Antibiotics and Preterm Delivery》分别处理缺失数据与immortal time bias，后者用prevalent new-user设计将虚假保护效应（HR=0.78）翻转为风险效应（HR=1.14），凸显偏倚处理方法对结论的剧烈影响。这组论文共同展现了目标试验框架从理论到实践、从模拟到真实数据的完整链路。

**测量偏差与算法验证**方面，本期涉及多种流行病学测量问题。《Differential Reporting of Severe Maternal Morbidity》揭示出生证明与索赔数据间的系统报告差异，且差异在少数族裔中更大，影响种族不平等评估。《Development and Validation of Gestational Age Estimation Algorithms》在非活产中比较四种算法，发现确定性方法外部泛化不劣于机器学习。《Novel Psychometric Indicator Assessments》提出相对超额相关矩阵，为多指标测量提供无模型描述工具。此外，《Understanding Algorithmic Fairness》将子群净获益纳入公平性量化，指出健康公平与系统目标之间的权衡。这些论文共同回应了数据质量、测量变异与算法选择对流行病学结论的威胁。

与**因果推断**方向最贴近的优先级论文：目标试验框架的两篇（Where Do Target Trials Come From?、Applying the Target Study Conceptual Model）、同胞比较设计及其评论、缺失数据处理的Mind the Gap与抗生素/早产一文。与**半参数效率**方向关联较弱，但《Discretizing Continuous Event Time Data》为离散时间设定下的效率损失提供实操指南；《An Improved Pooled Logistic Regression Implementation》则适用于加权生存分析的计算加速。

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1097/ede.0000000000001951](https://doi.org/10.1097/ede.0000000000001951) — Where Do Target Trials Come From? Specifying the Protocol of a Target Trial When Repurposing Data for Causal Inference
- **作者**: Miguel A. Hernán, Barbra A. Dickerman, Sonja A. Swanson, Issa J. Dahabreh
- **期刊/来源**: Epidemiology
- **机构**: Harvard University · University of Pittsburgh · Beth Israel Deaconess Medical Center · Deaconess Hospital
- **分类**: vol 37 · issue 3 · pp 282-286
- 相关性 8/10 · novelty: `survey`
- **摘要**: 本文讨论了在利用现有观察数据而非预设随机试验进行因果推断时，目标试验方案的制定过程。作者指出，研究者通常无法在数据检查前完全预先指定可模拟的目标试验方案，因为原始因果问题（index trial）必须根据数据的可得性、测量和缺失模式等因素迭代调整，从而形成最终的目标试验方案。这种自适应过程引出了重要问题：哪些数据检查是允许的，如何透明地记录每次调整及理由，以及是否可以预先指定调整规则。文章强调，目标试验框架的实际应用是迭代的，而非线性，需要平衡原始研究问题与数据约束。作者呼吁在方案调整过程中保持严谨性，并对调整进行明确记录。对于因果推断研究者和流行病学应用者而言，本文提供了实践指导，有助于理解在设计观察性研究时如何保持透明性和科学性。
- **关键技术**: `target trial framework`, `protocol specification`, `causal question adaptation`, `observational data repurposing`
- **为什么对您有用**: 本文直接关联到因果推断中的目标试验框架，这是流行病学因果推断的核心工具，也是研究者primary interest中的causal inference子方向。研究者moderately familiar的identification theory in causal inference可用于分析方案调整过程中识别假设的变化。后续可进一步探讨如何在数据适应过程中保证识别假设的合理性，属于立即可做的概念性思考。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1097/ede.0000000000001945](https://doi.org/10.1097/ede.0000000000001945) — An Improved Pooled Logistic Regression Implementation
- **作者**: Paul N. Zivich, Mark Klose, Justin B. DeMonte, Bonnie E. Shook-Sa, Stephen R. Cole, Jessie K. Edwards
- **期刊/来源**: Epidemiology
- **机构**: University of North Carolina Health Care · Department of Health
- **分类**: vol 37 · issue 3 · pp 311-314
- 相关性 7/10 · novelty: `minor`
- **摘要**: Pooled logistic 回归是流行病学生存分析中常用方法，但面对大型数据集时计算负担大，常需依赖放宽时间区间或参数化时间函数。本文提出一种改进实现：将长格式数据限制为只包含唯一事件时间的行，从而大幅减少数据维度。该技巧仅适用于时间使用不连续指示变量建模的灵活设定。在 SAS、R、Python 三种环境中使用公开数据集验证，点估计不变，但运行速度提升 6 到 68 倍。加速主要体现在避免了重复计算非事件风险集，尤其在使用 bootstrap 估计标准误时效果显著。该实现不改变模型假设或估计量性质，仅优化数据存储与循环逻辑。对您而言，这种计算技巧可直接复用在因果推断中的加权生存分析（如 g-formula 或 IPW），利用已熟练的软件开发能力快速集成。
- **关键技术**: `pooled logistic regression`, `data restriction to unique event times`, `bootstrap inference`, `survival analysis`, `computational optimization`
- **为什么对您有用**: 与您 secondary interest 中的流行病学应用直接相关：pooled logistic 回归是纵向因果推断的常见工具。您非常熟悉的 software development 技能可直接落地该算法加速，无需额外专业知识。立即可做：在自己的 R/Python 因果推断工具包中实现这一效率改进。

## 流行病学  *(epidemiology, 14 篇)*

### 1. [10.1097/ede.0000000000001958](https://doi.org/10.1097/ede.0000000000001958) — Mind the Gap: Addressing Missing Person Time When Estimating Outcome Incidence in Longitudinal Data
- **作者**: Jacqueline E. Rudolph, Rachael K. Ross, Lauren C. Zalla, Shruti H. Mehta, Gregory D. Kirk, Becky L. Genberg et al.
- **期刊/来源**: Epidemiology
- **机构**: Johns Hopkins University · Spencer Foundation · Johns Hopkins Medicine
- **分类**: vol 37 · issue 3 · pp 287-297
- 相关性 8/10 · novelty: `application`
- **摘要**: 该论文针对纵向数据中因缺失访视或退出导致的观测空白期（data gaps），探讨不同处理方法对结果发生率估计的偏倚和精度影响。作者通过模拟生成四种缺失机制（独立缺失、基线共同原因、时变共同原因、结局影响后续缺失），并评估了粗分析与两类加权方法（逆概率删失加权、逆概率观测加权）及多重插补在三种结局类型（短暂、重复、永久）下的表现。模拟结果显示：当允许缺失后个体重新进入分析时，即使缺失独立于结局，粗分析仍可能有偏；逆概率删失加权和多重插补在所有情景下相对无偏，且多重插补更精确。结论建议避免允许个体在数据间隙后返回的粗分析，而应采用删失或基于多重插补的策略。该论文为流行病学纵向研究中缺失数据的处理提供了实用的模拟证据，对您的流行病学应用兴趣有直接参考价值，尤其在因果推断中处理时变混杂和选择偏倚时，这些方法的比较能帮助选择稳健的估计策略。
- **关键技术**: `inverse probability of censoring weights`, `multiple imputation`, `inverse probability of observation weights`, `simulation study with data-generating mechanisms`, `handling intermittent missingness`
- **为什么对您有用**: 本文属于流行病学应用方法工作，直接对应您的 secondary interest 中的流行病学方向，尤其涉及纵向数据中缺失时间的处理方法，这与您 primary interest 中的 longitudinal causal inference 密切相关。您熟悉的非参数统计和因果推断估计理论（如 IPCW、多重插补）足以理解并批判该模拟比较的设计，可快速评估其结论在您自己的分析中的适用性，属于立即可做的范畴。该论文不涉及新理论，但作为方法选择参考，值得花时间阅读全文以了解不同缺失机制下各方法的表现细节。

### 2. [10.1097/ede.0000000000001937](https://doi.org/10.1097/ede.0000000000001937) — Sibling Comparison Designs to Assess Social Exposures and Empirical Tools to Guide Interpretation: An Illustrative Study of Childhood Income and Subsequent Mental Disorders
- **作者**: Linda Ejlskov, Buket Öztürk Esen, Tomáš Formánek, Christian Hakulinen, Nanna Weye, John J. McGrath et al.
- **期刊/来源**: Epidemiology
- **机构**: Aarhus University · Aarhus University Hospital · University of Cambridge · National Institute of Mental Health · University of Helsinki · Finnish Institute for Health and Welfare · Norwegian Institute of Public Health · The University of Queensland 等
- **分类**: vol 37 · issue 3 · pp 298-306
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文聚焦于兄弟姐妹比较设计在社会暴露（童年家庭收入）与精神障碍因果关系推断中的方法学挑战。利用丹麦全国队列数据（n=643,623；403,963个兄弟姐妹，出生1986–1996），开发了三套实证工具来辅助解读兄弟姐妹比较估计的可靠性。方法包括：负对照分析——通过构建伪兄弟姐妹（不相关但收入差异相似的个体）隔离暴露变异效应与共享家庭混杂效应；评估兄弟姐妹年龄结构、暴露相关性和变异模式，判断组内是否有意义对比；评估关键期假设——测量不同年龄的收入暴露。结果发现：总体分析显示家庭收入与精神障碍风险负相关（aHR=0.78），但兄弟姐妹比较设计无关联（aHR=1.02）；伪兄弟姐妹匹配收入后效应大幅衰减（aHR=0.93），未匹配收入则无衰减；收入效应在各个年龄测量时相似。结论认为，本例中兄弟姐妹比较设计估计值可能反映暴露变异有限和生命历程假设不满足，而非去除家庭混杂的效果。对您而言，本文是流行病学中因果推断方法的实例，展示了负对照设计在观察性研究中的应用，可与您的因果推断识别理论兴趣直接连接。
- **关键技术**: `sibling comparison design`, `negative control analysis`, `pseudo-sibling matching`, `shared familial confounding`, `critical period assumption`
- **为什么对您有用**: 本文直接关联您的secondary interest流行病学中的因果推断应用，具体展示了负对照和伪兄弟姐妹分析在评估社会暴露与健康结局中的实践。您非常熟悉的identification theory in causal inference可立即用来审视其识别假设（如无未测量共同混杂是否合理）。立即可做：利用您现有的因果推断识别理论和估计框架，即可复现或扩展这类负对照工具到其他流行病学队列中。

### 3. [10.1097/ede.0000000000001947](https://doi.org/10.1097/ede.0000000000001947) — Antibiotics and Preterm Delivery: The Prevalent New-user Cohort Design to Resolve Immortal Time Bias
- **作者**: Simon Galmiche, Eros Comin, Sophie Dell’Aniello, Jacques Balayla, Samy Suissa
- **期刊/来源**: Epidemiology
- **机构**: Jewish General Hospital · McGill University · University of Milano-Bicocca
- **分类**: vol 37 · issue 3 · pp 355-362
- 相关性 8/10 · novelty: `application`
- **摘要**: 在孕期抗生素使用与早产关联的流行病学队列研究中，目标 estimand 是第三孕期抗生素启动对早产/低出生体重的因果效应，关键问题是 immortal time bias 导致的时间固定暴露估计严重偏倚（HR=0.78，假保护效应）。本文采用 prevalent new-user 设计，在相同孕周日匹配抗生素启动者与未使用者，并使用 time-conditional propensity score 控制混杂。结果显示，正确处理 immortal time 后 HR 从 0.78 翻转为 1.14（95% CI: 1.04-1.24），而 time-varying 暴露方法给出 HR=1.23，证实 immortal time bias 是既往研究结论冲突的核心来源。对您可能有用：本文是流行病学中 immortal time bias 与 prevalent new-user 设计的典型应用案例，直接连接到因果推断中的 identification 与时间依赖混杂处理。
- **关键技术**: `prevalent new-user cohort design`, `immortal time bias correction`, `time-conditional propensity score matching`, `time-varying exposure analysis`, `target trial emulation`
- **为什么对您有用**: (1) 直接连接到流行病学因果推断中的 immortal time bias 问题与 prevalent new-user identification 策略，属于 secondary interest 中 epidemiology 的应用因果工作；(2) 用您 very_familiar 的因果推断 identification theory 可以审视其 time-conditional propensity score 是否完整阻断 backdoor path，或用 moderately_familiar 的 semiparametric theory 评估其 matching estimator 的效率损失；(3) **立即可做**：用 very_familiar 的因果推断 estimation theory 复现并比较其 HR 估计与 IPW / AIPW / one-step estimator 在此设定下的效率差异。

### 4. [10.1097/ede.0000000000001964](https://doi.org/10.1097/ede.0000000000001964) — Applying the Target Study Conceptual Model to Measure Racial and Ethnic Disparities in Hypertension Treatment Intensification
- **作者**: Aster Meche, Romsai T. Boonyasai, Yea-Jen Hsu, Raquel C. Greer, Hemalkumar B. Mehta, G. Caleb Alexander et al.
- **期刊/来源**: Epidemiology
- **机构**: Johns Hopkins University · Johns Hopkins Medicine · Agency for Healthcare Research and Quality
- **分类**: vol 37 · issue 3 · pp 376-385
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文在流行病学教程设定下，研究如何按照 IOM 定义（剔除准入、临床需求与偏好等“允许协变量”后的差异）测量高血压治疗强化中的种族差异。核心方法为“Target Study”概念模型，通过明确目标研究设计并使用逆概率加权（IPW）平衡允许协变量，从而估计非允许差异部分。实证使用 2018–2022 年 Mid-Atlantic 地区大型医疗系统电子病历数据，未调整时黑人患者治疗强化率高出白人 2–4 个百分点；IPW 调整允许协变量后，黑人患者反而低 3–4 个百分点（如 2020 年调整差异 −3%，95% CI −4%, −1%），揭示了 crude 与 adjusted 方向反转的 Simpson 现象。对您可能有用：该文展示了 IPW 在流行病学因果差异分解中的具体应用，可作为 epi 领域因果推断的入门案例阅读。
- **关键技术**: `inverse probability weighting`, `IOM disparity definition`, `allowable covariates adjustment`, `target study emulation`, `Simpson's paradox reversal`
- **为什么对您有用**: 本文属于流行病学因果推断的应用与教程，直接连接到 epidemiology secondary interest 的因果推断与数据集方向。技术层面仅使用标准 IPW，您武器库中 very_familiar 的“estimation theory in causal inference”完全覆盖其方法，无需额外长肌肉即可复现或扩展其分解框架。作为 gateway reading，本文对 IOM 差异定义与 IPW 实操的阐述清晰，适合快速了解 epi 领域如何将因果概念落地，但方法学 novelty 为 minor，不值得花时间深读全文。

### 5. [10.1097/ede.0000000000001954](https://doi.org/10.1097/ede.0000000000001954) — Differential Reporting of Severe Maternal Morbidity on US Birth Certificate and Claims Data by Race and Ethnicity
- **作者**: Beth L. Pineles, Anthony D. Harris, Lisa Pineles, Esa M. Davis, K. S. Joseph, Enrique Schisterman et al.
- **期刊/来源**: Epidemiology
- **机构**: University of Pennsylvania · University of Maryland, Baltimore · Foundation for the National Institutes of Health · Children's & Women's Health Centre of British Columbia · B.C. Women's Hospital & Health Centre
- **分类**: vol 37 · issue 3 · pp 345-354
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文比较了美国出生证明与医院索赔数据中严重孕产妇发病率（SMM）的报告差异，并评估了种族/民族分层的影响。研究利用2019年出生证明（约347万）和Premier Healthcare Database（约346万）数据，计算了输血、子宫切除、ICU入住等指标的发病率及发病率比（IRR）。结果显示，出生证明报告的SMM发病率普遍低于索赔数据，且这种差异在非西班牙裔黑人和西班牙裔患者中更为显著。例如，非西班牙裔白人输血的IRR为0.50，而其他种族/民族仅为0.29–0.39。进一步logistic回归表明，出生证明数据中种族/民族与SMM的关联强度被严重低估，调整后的优势比更接近零。本文揭示了出生证明数据在健康差异研究中的潜在偏倚，对流行病学中数据源选择与偏差校正研究具有重要参考价值。
- **关键技术**: `incidence rate ratio`, `logistic regression`, `claims data analysis`, `birth certificate data comparison`, `race/ethnicity stratification`, `data quality assessment`
- **为什么对您有用**: 本文属于流行病学领域的应用研究，直接回应了您对流行病学数据集的兴趣。其核心问题是数据源的系统性偏倚如何影响种族/民族健康差异的推断，这与您熟悉的因果推断中测量误差和选择偏差问题紧密相关。您可以使用非参数敏感性分析或偏差校正方法（如缺失数据或误分类模型）来进一步量化这种偏倚对效应估计的影响；但当前论文方法较简单，属于“中期可做”——需先熟悉流行病学数据质量评估的常规框架。

### 6. [10.1097/ede.0000000000001955](https://doi.org/10.1097/ede.0000000000001955) — State Minimum Wages and Food Insecurity Among Households Receiving Government Food Assistance
- **作者**: Krista Neumann, Barbara A. Laraia, Corinne A. Riddell
- **期刊/来源**: Epidemiology
- **机构**: University of Washington · Berkeley Public Health Division · University of California, Berkeley
- **分类**: vol 37 · issue 3 · pp 397-406
- 相关性 6/10 · novelty: `application`
- **摘要**: 在 SNAP 受助家庭中估计州最低工资对食物不安全的影响，estimand 为每增加 $1 最低工资的食物不安全患病率差异。利用 CPS-FSS 2002–2019 数据构建两年面板，采用 within-household 线性固定效应模型，调整时变经济混杂与同期安全网政策。整体估计提示微弱保护效应（PD/万人：−298，95% CI：−673, 77），亚组分析显示老年户、Hispanic 及部分大学教育家庭效应最强，Indigenous 家庭估计不精确且可能有害。本文为典型流行病学因果应用，方法学 novelty 有限，但数据结构与政策混杂控制策略对您有用。
- **关键技术**: `within-household linear fixed-effects model`, `2-year panel data linkage`, `time-varying confounding adjustment`, `concurrent policy adjustment`, `stratified subgroup analysis`
- **为什么对您有用**: 本文属于流行病学因果应用，连接到您 secondary interest 中的 epidemiology (applied causal work) 子方向；数据结构（两年面板+时变混杂+同期政策干预）与您 very_familiar 中的 estimation theory in causal inference 直接对应，可用 identification theory 视角审视其固定效应策略是否充分处理了时变混杂与政策交互。follow-up 粗判：立即可做——用您熟悉的因果 identification 框架即可评估其混杂控制假设的合理性，无需新武器。

### 7. [10.1097/ede.0000000000001946](https://doi.org/10.1097/ede.0000000000001946) — Discretizing Continuous Event Time Data
- **作者**: Rachael K. Ross, Jacqueline E. Rudolph, Lauren C. Zalla, Catherine R. Lesko
- **期刊/来源**: Epidemiology
- **机构**: Columbia University · Johns Hopkins University
- **分类**: vol 37 · issue 3 · pp 307-310
- 相关性 6/10 · novelty: `application`
- **摘要**: 在离散化连续事件时间数据的设定下，目标是确定如何将结局与失访（LTFU）事件分配到离散区间端点，以最小化与连续时间累积风险曲线的偏差。模拟与 20 个真实流行病学数据集的实证比较表明，结局应统一分配到区间末端。对于失访事件，将 LTFU 分配到离其连续事件时间最近的区间起点或末端（就近分配）的误差始终最小，优于固定分配到起点或末端的常规做法。本文为流行病学队列研究中时间离散化提供了明确的实操规则，对您在流行病学应用因果推断中处理离散时间 censoring 设定有直接参考价值。
- **关键技术**: `time discretization`, `cumulative risk estimation`, `loss to follow-up assignment`, `simulation comparison`
- **为什么对您有用**: 本文直接涉及流行病学队列研究中事件时间离散化的实操规则，属于您 secondary interest 中流行病学数据结构与因果推断设定的交叉点。就近分配 LTFU 的规则对您在离散时间下做 IPW / g-formula 估计时如何正确构造 censoring at-risk 集合有指导意义。本文是好的入门读物，武器库完全够支撑进入此方向，值得花时间读全文以掌握离散时间生存分析的数据处理细节。

### 8. [10.1097/ede.0000000000001949](https://doi.org/10.1097/ede.0000000000001949) · [arXiv](https://arxiv.org/abs/2412.07879) — Understanding Algorithmic Fairness for Clinical Prediction in Terms of Subgroup Net Benefit and Health Equity
- **作者**: Jose Benitez-Aurioles, Alice Joules, Irene Brusini, Niels Peek, Matthew Sperrin
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 3 · pp 386-396
- 相关性 6/10 · novelty: `application`
- **摘要**: 在临床预测模型的公平性设定下，目标 estimand 是各子群（按 protected attribute 划分）的 subgroup net benefit 及其对健康不平等的影响。本文扩展了决策曲线分析中的 net benefit 概念，将其作为量化不同子群临床获益差异的核心指标，而非仅依赖预测性能的 egalitarian 平等。方法上，通过 subgroup-specific net benefit 与 decision threshold 的联合分析，展示了资源约束下 health equity 与系统其他目标之间的必要 trade-off。实证部分构建了两个模型：2型糖尿病预防干预的预后模型与肺癌筛查分配算法，演示了该框架如何揭示模型在不同社会/临床语境下对公平性的影响。对您可能有用：本文将因果决策理论中的 net benefit 指标引入流行病学公平性评估，为 epi 应用中的 subgroup-specific decision-making 提供了结构化视角。
- **关键技术**: `subgroup net benefit`, `decision curve analysis`, `health equity quantification`, `clinical prediction model fairness`, `resource-constrained trade-off`
- **为什么对您有用**: (1) 本文属于流行病学应用，将 net benefit 这一决策分析指标用于 subgroup-level 的公平性评估，连接到 epi 领域的 applied causal/decision work；(2) 武器库中 estimation theory in causal inference 与 software development 可直接用于复现和扩展 subgroup net benefit 的估计与可视化工具；(3) **立即可做**：用 very_familiar 的因果估计与软件开发工具即可复现其 subgroup net benefit 计算框架，并探索在更复杂 longitudinal/IV 设定下的推广。

### 9. [10.1097/ede.0000000000001960](https://doi.org/10.1097/ede.0000000000001960) — Considerations for the Analysis of Urinary Environmental Chemical Concentrations During Pregnancy
- **作者**: Danielle R. Stevens, Kaleigh Hinton, Katie M. O’Brien, Jessie P. Buckley, Barrett M. Welch, Jason A. Watts et al.
- **期刊/来源**: Epidemiology
- **机构**: University of North Carolina at Chapel Hill · National Institute of Environmental Health Sciences · University of Nevada, Reno · Centers for Disease Control and Prevention · National Center for Environmental Health · Eastern Virginia Medical School
- **分类**: vol 37 · issue 3 · pp 325-335
- 相关性 6/10 · novelty: `application`
- **摘要**: 在孕期前瞻性队列研究中，目标是评估尿液水合指标（UFR/SG）的轨迹与预测因子，并比较不同标准化方法对环境化学生物标志物（MBP）暴露描述的影响。核心方法为广义可加混合模型（GAMM）刻画非线性轨迹与线性混合模型（LMM）筛选人口学/孕期预测因子，比较了四种浓度处理：未标准化、UFR标准化（排泄率）、SG标准化（Boeniger法）与协变量调整SG标准化（O'Brien法）。结果显示孕期SG线性下降而UFR非线性变化，种族等特征与水合指标显著关联；不同标准化方法间一致性良好（UFR与SG法一致性略低），但MBP的轨迹与预测因子在各方法下高度一致。对您有用：本文是流行病学队列中连续纵向测量与混杂调整的典型应用，展示了GAMM/LMM在纵向暴露评估中的实操范式。
- **关键技术**: `generalized additive mixed models`, `linear mixed effects models`, `urinary biomarker standardization`, `specific gravity adjustment`, `covariate-adjusted standardization`, `longitudinal trajectory analysis`
- **为什么对您有用**: 本文属于流行病学纵向队列的实证应用，连接到 epidemiology 的 applied causal work 与 longitudinal 设定，展示了 GAMM/LMM 处理孕期连续测量轨迹与混杂预测因子的完整 pipeline。武器库中 very_familiar 的软件开发与 moderately_familiar 的 semiparametric theory（GAMM 属半参数）足以支撑研究者进入此类纵向暴露评估的数据分析方向。作为 gateway reading，本文对孕期生理变化与水合调整的讨论清晰易懂，数据结构（8次纵向访视、303样本）与模型设定（GAMM/LMM）均有明确交代，值得花时间读全文以了解流行病学纵向暴露评估的典型范式与潜在方法学改进口子。

### 10. [10.1097/ede.0000000000001956](https://doi.org/10.1097/ede.0000000000001956) — Development and Validation of Gestational Age Estimation Algorithms for Nonlive Births in Administrative Healthcare Databases
- **作者**: Yongtai Cho, Eun-Young Choi, Hyesung Lee, Yunha Noh, Jung Yeol Han, Seung-Ah Choe et al.
- **期刊/来源**: Epidemiology
- **机构**: Sungkyunkwan University · Karolinska Institutet · Kangwon National University · Chonnam National University · Inje University Ilsan Paik Hospital · Mother Hospital · Korea University · Seoul National University 等
- **分类**: vol 37 · issue 3 · pp 336-344
- 相关性 6/10 · novelty: `application`
- **摘要**: 在韩国国家健康信息数据库的非活产（自然/人工流产、死胎）子集中，目标是估计孕周（GA），以疫苗接种登记数据作为参考标准。作者移植了美国数据库的四种算法：结果特异性赋值、超声记录调整、回归模型和随机森林，并在独立数据集上做了外部验证。核心发现是：在内部验证中随机森林表现最优（流产 MSE 1.68、死胎 MSE 0.97，2 周内准确率 >92%），但在外部验证中超声调整的确定性方法与随机森林表现相当（MSE 差距 <0.3）。结论是确定性方法因实现简单且外部泛化不劣于机器学习而更可取。对您可能有用：本文展示了流行病学行政数据中 phenotyping 算法的内部-外部验证范式，是理解 epi 数据清洗与测量误差问题的入门案例。
- **关键技术**: `gestational age phenotyping algorithm`, `external validation`, `random forest regression`, `deterministic rule-based assignment`, `mean squared error evaluation`, `administrative healthcare database linkage`
- **为什么对您有用**: 本文属于流行病学应用，连接到 epi secondary interest 的行政数据与因果推断前端的 phenotyping 问题。技术武器库中的软件开发经验可直接复现其算法比较流程，但本文无 semiparametric / efficiency / 高维理论贡献，方法学 novelty 有限。作为入门读物，本文清晰展示了 epi 数据的 linkage、参考标准构建与内外部验证范式，值得花时间读全文以了解韩国行政数据结构，但对您核心理论方向无直接推进。

### 11. [10.1097/ede.0000000000001939](https://doi.org/10.1097/ede.0000000000001939) — A Framework for Thinking About the Potential Public Health Impact of Epidemiologic Research
- **作者**: Catherine R. Lesko, Lauren C. Zalla, Rachael K. Ross, Jacqueline E. Rudolph, Emily R. Smith, Jessie K. Edwards
- **期刊/来源**: Epidemiology
- **机构**: Johns Hopkins University · Columbia University · Duke University · Duke Institute for Health Innovation · Duke University Health System · University of North Carolina at Chapel Hill
- **分类**: vol 37 · issue 3 · pp 363-370
- 相关性 4/10 · novelty: `survey`
- **摘要**: 本文在流行病学领域提出一个评估研究公共卫生影响的框架，包含疾病负担、干预潜力与背景因素三大维度。疾病负担维度考虑病例数量、疾病严重程度及人群分布。干预潜力维度涵盖暴露本身的可变性、其他原因的流行情况、自然病程下暴露与结局风险以及干预可行性。框架强调研究不须在所有维度上都表现突出，但维度越充实则潜在影响越大。该框架整合了已有知识，为流行病学研究的价值论证提供了结构化工具。对于您，框架中关于干预可行性与自然病程的讨论与因果推断中的干预识别和一致性假设相关，但本文不涉及具体估计方法，可作为流行病学方向的概念入门。
- **关键技术**: `impact evaluation framework`, `burden of disease assessment`, `intervention potential evaluation`, `natural course concept`, `feasibility of intervention`
- **为什么对您有用**: 本文属于流行病学领域的概念框架，连接您的次级兴趣（流行病学的应用与因果推断框架）。武器库中的因果推断理论（如干预、自然病程）可用于理解框架中的概念，但本文无具体统计方法或数据。由于缺乏流行病学领域知识和数据，您目前无法基于本文进行方法学跟进，仅适合作为背景阅读，因此暂不可做进一步研究。

### 12. [10.1097/ede.0000000000001963](https://doi.org/10.1097/ede.0000000000001963) — Novel Psychometric Indicator Assessments: The Relative Excess Correlation and Associated Matrices
- **作者**: Tyler J. VanderWeele, R. Noah Padgett
- **期刊/来源**: Epidemiology
- **机构**: Harvard University · Cancer Research And Biostatistics
- **分类**: vol 37 · issue 3 · pp 315-324
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对心理测量中多指标评估心理社会构念的场景，提出了两种新型相关矩阵：观察残差相关（ORC）矩阵和相对超额相关（REC）矩阵。ORC矩阵用于描述当某个指标高于个体所有指标的平均分时，其他指标是否也偏高；REC矩阵则度量每对指标的实际相关相对于基于其他指标预期值的偏离程度。即使原始相关系数全为正，这两种矩阵也常常出现负值，从而揭示指标间的相对模式。REC矩阵的正偏差有助于识别更紧密关联的指标聚类，可视为无需旋转或预设因子数的因子分析替代工具。推导了ORC、REC与协方差类似物之间的性质关系，方法纯粹描述性，不依赖模型假设。本文对您的作用在于：为流行病学中常见的多指标测量问题提供了一个直观、计算简便的描述工具，与您对流行病学数据应用的次要兴趣直接相关，且矩阵运算与您统计计算（矩阵操作）领域有技术交集。
- **关键技术**: `observed residual correlation (ORC) matrix`, `relative excess correlation (REC) matrix`, `clustering via positive deviations`, `descriptive correlation analysis`, `no need for rotation or factor number decisions`
- **为什么对您有用**: 本文连接您的次要兴趣——流行病学中多指标心理社会测量的描述性分析工具。您非常熟悉的统计计算与软件开发能力（例如使用 einsum 库高效实现矩阵运算）可立即可做：编写一个轻量级包计算 ORC 和 REC 矩阵，应用于流行病学队列数据（如抑郁量表条目分析），验证其与因子分析的互补性。武器库中的“非参数统计”视角也可用于研究这些矩阵的稳定性与样本量关系。整体上，这是一篇值得速读的方法论文献，但核心价值在于应用，而非理论突破。

### 13. [10.1097/ede.0000000000001959](https://doi.org/10.1097/ede.0000000000001959) — Re: Confounders, Mediators, or Colliders: What Types of Shared Covariates Does a Sibling Comparison Design Control For?
- **作者**: Alyssa Bilinski
- **期刊/来源**: Epidemiology
- **机构**: Brown University
- **分类**: vol 37 · issue 3 · pp e6-e7
- 相关性 4/10 · novelty: `minor`
- **摘要**: 本文是对 Sjölander 与 Zetterqvist 关于同胞比较设计方法论的评论，核心讨论共享协变量（如家庭环境）在因果图中的角色判定问题。作者指出，原文将共享家庭环境归类为中介变量忽略了科学问题对因果路径的依赖：当研究目标为父母年龄的生物学效应（如配子质量、胎盘功能等孕期机制）时，产后家庭环境应被视为混杂因素而非中介，此时同胞设计中的条件化恰好能剥离社会因素的混杂偏倚以隔离生物学效应。若研究总效应（生物学+社会路径），家庭环境才可能成为中介，但这对应的是将父母年龄视为社会标记而非生物学暴露的替代因果问题。效应修饰不改变混杂属性。该评论强调混杂/中介/碰撞器的判定取决于具体的因果 estimand 与假设，而非变量本身的固有属性。对您有用：此文以流行病学实例清晰展示了因果图变量角色随 estimand 切换而变化的逻辑，是因果识别理论在流行病学应用中辨析假设敏感性的简明范例。
- **关键技术**: `sibling comparison design`, `causal DAG role classification`, `confounder vs mediator distinction`, `estimand-dependent identification`, `effect modification vs mediation`
- **为什么对您有用**: 本文直接连接到因果推断中的 identification theory 子方向，以流行病学实例（同胞设计）具体展示了 estimand 如何决定 DAG 中变量的角色（混杂 vs 中介），这正是您在 identification theory 中关注的假设敏感性议题。您武器库中 very_familiar 的 identification theory in causal inference 完全足以剖析此文中的 DAG 角色切换逻辑并推广至更复杂的 longitudinal 或 mediation 设定。**立即可做**：用您熟悉的因果识别理论将此处的 estimand-dependent 角色判定形式化，推导在更一般设定下（如 longitudinal mediation）条件化策略对目标效应的偏倚方向。

### 14. [10.1097/ede.0000000000001962](https://doi.org/10.1097/ede.0000000000001962) — Thanks to Our Reviewers 2025
- **作者**: 
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 3 · pp 279-280
- 相关性 0/10 · novelty: `other`
- **摘要**: 本文是《Epidemiology》期刊2025年度的审稿人致谢名单，列举了263位审稿人及其审稿数量，并表彰了六位年度杰出审稿人。该名单本身不包含任何研究问题、estimand、模型设定或regularity假设，纯粹为编辑部的行政性致谢。文中未涉及任何估计方法、收敛性质、效率界或具体技术工具，亦无理论或实证结果。对您而言，这份名单可作为流行病学领域活跃研究者（尤其是因果推断方法方向）的快速索引，但无方法学novelty。
- **关键技术**: `peer review recognition`, `epidemiology researcher index`
- **为什么对您有用**: 本文点名了多位在流行病学因果推断方法领域活跃的研究者（如 Vanessa Didelez, Nima Hejazi, Oliver Dukes, Linbo Wang, Aaron Sarvet, Kara Rudolph 等），可作为您追踪 epidemiology 中 causal inference / semiparametric 方法应用前沿的线索。您的武器库（identification theory in causal inference, semiparametric theory）完全足以阅读这些审稿人近期发表的实质性方法论文，但本文本身无需展开阅读。

## 其他  *(other, 2 篇)*

### 1. [10.1097/ede.0000000000001961](https://doi.org/10.1097/ede.0000000000001961) — Jørn Olsen, 20 May 1946–5 January 2026
- **作者**: 
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 3 · pp 281-281
- 相关性 0/10 · novelty: `minor`
- **摘要**: 这是一篇悼念流行病学家Jørn Olsen的讣告，发表于《Epidemiology》期刊。Olsen是奥胡斯大学社会医学教授，丹麦流行病学研究的奠基人之一，在围产期流行病学方法、职业流行病学等领域做出了开创性贡献。他领导创建了丹麦国家出生队列，并坚持数据开放政策。他曾任国际流行病学协会主席，推动欧洲流行病学教育项目。本文主要回顾其学术生涯和人格风范，并无新的研究结果或方法论贡献。对您而言，这是一篇与secondary interest（流行病学应用）相关的人物介绍，但无技术内容可深入学习。
- **为什么对您有用**: 本文属于epidemiology（secondary interest）领域的纪念性文章，非研究论文，不涉及具体方法学或数据分析。无需进一步阅读。

### 2. [10.1097/ede.0000000000001948](https://doi.org/10.1097/ede.0000000000001948) — What Would You Do?
- **作者**: David A. Savitz
- **期刊/来源**: Epidemiology
- **机构**: Brown University
- **分类**: vol 37 · issue 3 · pp 374-375
- 相关性 0/10 · novelty: `minor`
- **摘要**: 该论文标题为《What Would You Do?》，作者David A. Savitz发表于《Epidemiology》期刊第37卷第3期第374-375页。提供的摘要内容与流行病学无关，而是关于儿童自理能力培养的教学材料，疑似元数据错误或占位符。实际文章很可能是一篇简短评论或伦理讨论，不具备方法学贡献。由于无法从摘要获取研究问题、技术方法或数据，无法进行有效评估。因此，该论文对您的研究领域（因果推断、高维统计、半参效率理论等）无直接关联。
- **为什么对您有用**: 该论文摘要与流行病学主题不符，无法判断是否与您的二级兴趣（流行病学应用、因果推断）相关。即使为真实评论，也缺乏具体统计方法或数据分析，不构成有价值的参考。您的技术武器库（非参、U统计量、因果推断理论）无法在此空壳摘要上应用。暂不可做——因为核心内容缺失。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

