# Epidemiology — Vol 37  Issue 2  ·  2026-06-19

- 共 11 篇 · Epidemiology
- 目录核对 ⚠️ 疑似漏 2 篇（对照 OpenAlex 13 篇）：10.1097/ede.0000000000001934、10.1097/ede.0000000000001932

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期论文围绕因果推断与流行病学应用交织展开，主要聚成三条主线：因果识别与estimand定义（涉及目标试验框架、信息性处理时间、test-negative设计偏倚修正、部分嵌套试验的通用性）；工具变量与准实验评估（比较区域密度与医生偏好IV、交错DID评估学校复课）；以及流行病学测量与结构性因素分析（贝叶斯back-calculation修正漏报、历史红线政策与结构性种族主义的长期效应、EHR与问卷数据一致性）。

因果识别与estimand主线在本期推进了对复杂设定下偏倚来源与识别条件的澄清。《Ideal Trial》指出目标试验框架下单纯对齐入排标准会偏离真实estimand，需平衡相关性与可行性以管理偏倚；《Informatively Timed Treatments》将纵向设定中相邻处理决策的等待时间视为time-varying confounder，修正g-methods的偏差；《Test-negative Designs》通过因果图识别多检测原因引入的选择偏倚，提出分层比值比估计量合并多原因数据以提升精度；《Partially Nested Trial》则针对仅部分中心/时段收集非随机化数据的嵌套设计，给出通用性分析的识别条件与估计量。

工具变量与准实验主线聚焦于药物安全与政策效应的实证评估，对比了不同策略的效度。《Area-level Patient Density and Physician Prescribing》在同一队列下直接比较区域处方密度与医生处方偏好两类IV对降糖药心血管效应的估计，显示IV调整均改善了协变量平衡；《School Reopenings》利用各县复课时间的交错实施构造staggered difference-in-differences，估计心理健康诊断率的下降效应。此外，测量与结构性因素主线中，《Back-calculation》以贝叶斯法将患病-报告比作为漏报乘数修正发病率；《Structural Racism》与《Historical Redlining》分别用复合指数/LCA与GEE探究社区结构性种族主义及历史红线政策对孕产期发病率与受孕概率的长期关联。

与因果推断及半参数效率方向最贴的论文适合优先看：关注estimand定义与识别条件的可看《Ideal Trial》与《Partially Nested Trial》；关注纵向g-methods调整集与偏差修正的可看《Informatively Timed Treatments》；关注选择偏倚分层修正及精度提升的可看《Test-negative Designs》；关注IV构造与效度比较的可看《Area-level Patient Density and Physician Prescribing》。

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.1097/ede.0000000000001933](https://doi.org/10.1097/ede.0000000000001933) · [arXiv](https://arxiv.org/abs/2405.10026) — The Ideal Trial: Defining Causal Estimands that Balance Relevance and Feasibility in Target Trial Emulations and Actual Randomized Trials
- **作者**: Margarita Moreno-Betancur, Rushani Wijesuriya, John B. Carlin
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 2 · pp 153-162
- 相关性 9/10 · novelty: `survey`
- **摘要**: 本文聚焦目标试验框架下因果 estimand 的定义问题，指出在观察性研究中常用 target trial 来逼近理想试验，但现有“对齐”方法（如使用相同入排标准）可能使 estimand 偏离实际感兴趣的目标。作者回顾了数学定义与理想试验两种定义 estimand 的等效途径，强调无论哪种方式都需平衡相关性与可行性。通过呼吸流行病学实例说明，若只注重可行性而忽略理想试验，会引入类似实际随机试验的偏倚来源。结论是必须明确理想试验与目标试验的差异，才能全面识别和管理偏倚。对您作为因果推断研究者，本文有助于澄清 target trial 框架中 estimand 定义的常见误区，并提供流行病学场景下 bias 讨论的实用视角。
- **关键技术**: `target trial emulation`, `causal estimand specification`, `ideal trial`, `bias analysis`, `feasibility-relevance tradeoff`
- **为什么对您有用**: 直接连接因果推断在流行病学中的应用（secondary interest），具体涉及 target trial 框架中 estimand 定义的偏差问题，与您武器库中“estimation theory in causal inference”直接相关——可以立即将本文的框架思路应用于您正在参与或合作的流行病学队列研究中，用以审视 estimand 定义的合理性。

### 2. [10.1097/ede.0000000000001943](https://doi.org/10.1097/ede.0000000000001943) · [arXiv](https://arxiv.org/abs/2508.21804) — Considerations for Estimating Causal Effects of Informatively Timed Treatments
- **作者**: Arman Oganisian
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 2 · pp 166-176
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在纵向因果推断设定下，本文研究处理时间跨个体异质且具有信息性（informatively timed）时，序列处理对生存结局效应的 identification 与估计问题。核心指出：相邻处理决策间的等待时间应被视为 time-varying confounder，忽略它将导致 g-methods（如 IPW、g-formula）产生偏差。方法上，将等待时间纳入 longitudinal g-methods 的调整集，在存在死亡与 censoring 的场景下构造相应的 estimators，并提供开源软件实现。理论贡献以 synthetic examples 展示偏差方向与修正机制，未给出 formal asymptotic efficiency 或 rate 结果。对您有用：本文将等待时间重新参数化为 time-varying confounder 的思路，直接连接 longitudinal causal inference 的 identification 理论，可作为该设定下构造 semiparametric efficient estimator 的起点。
- **关键技术**: `longitudinal g-methods`, `time-varying confounding`, `informatively timed treatment`, `waiting time as confounder`, `IPW estimation`, `survival outcome with censoring`
- **为什么对您有用**: 直接连接 longitudinal causal inference 中序列处理的 identification 与估计子方向。本文的核心 insight（等待时间即 time-varying confounder）为后续构造该设定下的 efficient influence function 与 semiparametric efficient estimator 提供了明确的 identification 前提——您可用 very_familiar 的 estimation theory in causal inference 与 moderately_familiar 的 semiparametric theory 直接切入，推导该结构下的 efficiency bound 与 debiased estimator。立即可做：用现有武器即可在本文 identification 框架上展开 efficiency theory 工作。

## 流行病学  *(epidemiology, 9 篇)*

### 1. [10.1097/ede.0000000000001940](https://doi.org/10.1097/ede.0000000000001940) · [arXiv](https://arxiv.org/abs/2312.03967) — Test-negative Designs with Various Reasons for Testing: Statistical Bias and Solution
- **作者**: Mengxin Yu, Tom Hongyi Liu, Kendrick Qijun Li, Nicholas Jewell, Eric Tchetgen Tchetgen, Dylan Small et al.
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 2 · pp 228-236
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在疫苗有效性评估的test-negative设计（TND）框架下，本文系统分析了纳入多种检测原因（症状、强制筛查、接触追踪）可能引入的选择偏倚。通过因果图和统计推导，作者识别了三种检测原因对应的偏倚来源，并分别定义了各estimand。基于此，提出一个分层比值比估计量（stratified odds ratio estimator），可在控制偏倚的同时合并多种原因数据以提升精度。理论部分给出了各estimand在何种条件下对应于同一疫苗有效性参数的充分条件。数值模拟和实际数据分析验证了分层估计量相对于标准估计量的偏倚校正效果和效率改进。该工作为实际疫情监测中灵活使用TND提供了严谨的统计框架。
- **关键技术**: `test-negative design`, `causal graph`, `stratified estimator`, `odds ratio`, `selection bias`
- **为什么对您有用**: 本文直接对应您 secondary interest 中的流行病学应用，同时深入使用了因果推断中的选择偏倚分析工具（causal graphs）；您的 technical arsenal 中的 'estimation theory in causal inference' 可直接适用于检验该分层估计量的半参效率，或扩展更复杂的分层方案；此为**立即可做**的 follow-up：您可以基于该框架开发标准软件包（R实现），或将该分层逻辑与您熟悉的高阶U-统计量结合以处理更复杂的依赖结构。

### 2. [10.1097/ede.0000000000001938](https://doi.org/10.1097/ede.0000000000001938) — Comparing Area-level Patient Density and Physician Prescribing Preference Instruments for the Effect of Antidiabetics on Adverse Cardiovascular Events Among Medicare Beneficiaries
- **作者**: Jack Cordes, Robert J. Glynn, Alexander M. Walker, Sebastian S. Schneeweiss
- **期刊/来源**: Epidemiology
- **机构**: Brigham and Women's Hospital · Harvard University
- **分类**: vol 37 · issue 2 · pp 207-219
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文在流行病学药物安全性评估中，比较了区域层面处方密度与医生处方偏好两类工具变量，用于估计DPP-4i抑制剂（西他列汀/沙格列汀）相较于磺脲类药物对老年Medicare人群主要不良心血管事件（MACE）的因果效应。研究基于两个模拟随机试验的队列，通过ZIP码级别的DPP-4i处方比例（0% vs 100% 及 <50% vs ≥50%）构造区域密度IV，并利用同一患者的医生历史处方构造医生偏好IV（含瞬时偏好IV）。两阶段IV回归模型均调整了倾向性评分五分位数。结果显示：传统未调整分析估计DPP-4i降低MACE风险（HR约0.68-0.86），但所有IV均强且改善了协变量平衡；区域密度IV分析未见有意义差异（西他列汀HR=1.1），医生偏好IV估计仍显示降低风险（HR=0.69），而瞬时偏好IV估计则无差异（HR=0.86-0.98），表明短期处方偏好IV具有潜力但效率不足。结论强调了IV选择对效应估计的敏感性。本文是流行病学中工具变量方法应用的具体案例，对您从事因果推断（特别是IV方法在真实数据中的表现）有参考价值，可以作为理解IV强度、排除限制假设及其实践局限的阅读材料。
- **关键技术**: `instrumental variable analysis`, `two-stage least squares`, `prescribing density`, `physician prescribing preference`, `propensity score adjustment`, `Medicare claims data`
- **为什么对您有用**: 本文直接关联到您的次要兴趣——流行病学中的应用因果推断，提供了IV方法在大型医保数据库中的实际构造、强度评估和灵敏度分析的完整范例。您对因果估计理论（very_familiar）的理解足以消化本文的IV设计与两阶段回归，但需注意本文强调的排除限制假设检验和IV选择对结论的影响。建议作为中期可读的实证案例，无需动手复现，但可加深对IV方法实际局限性的认识。

### 3. [10.1097/ede.0000000000001875](https://doi.org/10.1097/ede.0000000000001875) · [arXiv](https://arxiv.org/abs/2306.00855) — Generalizability Analyses with a Partially Nested Trial Design: The Necrotizing Enterocolitis Surgery Trial
- **作者**: Sarah E. Robertson, Matthew A. Rysavy, Martin L. Blakely, Jon A. Steingrimsson, Issa J. Dahabreh
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 2 · pp 177-186
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文针对部分嵌套试验设计（partially nested trial design）提出通用性分析（generalizability）方法。该设计常见于试验仅部分中心或部分时间段能收集非随机化个体数据，例如坏死性小肠结肠炎手术试验（NEC Surgery Trial）中前期同时收集随机化与非随机化个体，后期仅收集随机化个体。目标是在试验嵌套部分的数据中，利用整个试验的信息，估计全体符合条件个体（包括非随机化）的因果效应。作者给出了识别条件（identification conditions）并提出了相应的估计量，可能结合逆概率加权或结局回归。通过模拟研究评估估计量性能，并在NEC试验数据中进行了实证分析。该工作为流行病学中因实际操作限制导致的缺失非随机化数据提供了一种实用的推断框架。
- **关键技术**: `partially nested trial design`, `generalizability analysis`, `causal identification`, `weighted estimators`, `simulation study`
- **为什么对您有用**: 本文紧连接您流行病学应用的兴趣（secondary interest），并涉及因果推断中的通用性（generalizability）这一子方向。您非常熟悉的“estimation theory in causal inference”可直接用于理解和评估本文估计量的构造；若需进一步扩展至更复杂的嵌套结构（如多重时间段非随机化），可在“identification theory in causal inference”上稍加延伸即可上手。总体而言，该文提供了真实数据场景与可操作的方法，值得一读。

### 4. [10.1097/ede.0000000000001930](https://doi.org/10.1097/ede.0000000000001930) — Effect of School Reopenings on Children’s Mental Health During COVID-19: Quasi-experimental Evidence from California
- **作者**: Pelin Ozluk, Jeff Romine, Gosia Sylwestrzak, Rita Hamad
- **期刊/来源**: Epidemiology
- **机构**: Covance (United States) · Harvard University
- **分类**: vol 37 · issue 2 · pp 257-267
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文研究COVID-19疫情期间学校重新开放对儿童心理健康的因果效应，数据来自加州24个县185,735名儿童的健康保险理赔记录。采用交错实施的差异中差异（staggered difference-in-differences）设计，利用各县学校重新开放时间的外生变化作为准实验。估计结果表明，学校重新开放使每月心理健康诊断率下降1.2个百分点（95% CI: −1.59, −0.74），相关医疗支出下降10.6%（95% CI: −13.4%, −7.8%），效应在焦虑和抑郁诊断上最为显著，且女孩受影响更大。方法上应用了经典的双重差分框架，固定效应控制了不可观测的县和月间混杂，但未涉及更复杂的稳健估计（如将DID与倾向得分加权结合或使用合成控制）。该研究为理解公共卫生危机中的学校政策提供了因果证据，流行病学领域这种准实验设计的应用模式对您有直接参考价值：数据集结构和分析流水线（索赔数据、交错处理、事件研究图）可作为因果推断教学中展示DID实际应用的完整案例。
- **关键技术**: `difference-in-differences`, `staggered adoption design`, `quasi-experiment`, `administrative claims data`, `event study plots`
- **为什么对您有用**: 本文属于流行病学领域的应用因果推断研究，直接对应您secondary interest中的流行病学（数据集、应用因果）。您武器库中'causal inference estimation theory'（非常熟悉）可以立即用来评估DID的识别假设是否合理（如平行趋势、无预期效应），并思考是否可用更高效的估计量（如双重稳健DID）改善精度。立即可做：基于本文提供的处理时间和样本信息，您可以快速写一段代码复现平行趋势检验，或对比不同DID变种的结果。

### 5. [10.1097/ede.0000000000001936](https://doi.org/10.1097/ede.0000000000001936) — Adapting Back-calculation Methods to Estimate the Incidence of Tuberculosis
- **作者**: Anne N. Shapiro, Shariq Mohammed, C. Robert Horsburgh, Helen E. Jenkins, Laura F. White
- **期刊/来源**: Epidemiology
- **机构**: Boston University
- **分类**: vol 37 · issue 2 · pp 220-227
- 相关性 6/10 · novelty: `application`
- **摘要**: 在结核病（TB）流行病学设定下，目标是利用病例报告数据与疾病自然史参数估计真实发病率（incidence），核心假设为报告病例是发病率与疾病持续时间的卷积、且存在漏报偏倚。方法采用贝叶斯 back-calculation，将 prevalence-to-notification 比作为漏报乘数修正 Poisson 分布的报告计数，并通过 penalized-likelihood 保证平滑性，最终用 MCMC 求解越南、柬埔寨与菲律宾的性别分层发病率。实证结果显示估计发病率平均比报告数高 19%，男性发病率略高于女性。本文是流行病学应用，方法学 novelty 有限（标准贝叶斯 back-calculation 的领域适配），但对您可能有用：它展示了 back-calculation 在传染病因果/推断链条中如何处理 latency 与 underreporting 两个偏倚源。
- **关键技术**: `Bayesian back-calculation`, `Poisson convolution model`, `prevalence-to-notification ratio multiplier`, `penalized-likelihood smoothing`, `Markov chain Monte Carlo`
- **为什么对您有用**: 本文属于流行病学应用，方法学 novelty 有限（novelty_flag = application），但作为 gateway reading 有一定价值：(1) 它清晰展示了 back-calculation 如何将 latency（卷积结构）与 underreporting（乘数修正）显式建模，这对您在 causal inference 中处理 measurement error 与 latency 有概念启发；(2) 武器库（MCMC、penalized-likelihood）完全够用，但核心推断框架是标准贝叶斯而非 semiparametric / efficiency 理论，与您 primary interest 的技术连接较弱；(3) 值得花 10 分钟扫读 intro 与 model setup 以了解流行病学数据结构（报告延迟、漏报、性别分层），但不必深读方法细节。

### 6. [10.1097/ede.0000000000001935](https://doi.org/10.1097/ede.0000000000001935) — Longer-term Survival of UK People with Bleeding Disorders Infected by Human Immunodeficiency Virus and/or Hepatitis C Virus Through Contaminated Blood Transfusions
- **作者**: Matthew Gittins, Ben Palmer, Hua Xiang, Pratima Chowdary, Peter Collins, Sheila M. Bird
- **期刊/来源**: Epidemiology
- **机构**: Manchester Academic Health Science Centre · University of Manchester · Haemophilia Foundation Australia · Institute of Infection and Immunity · Cardiff University · University of Strathclyde · University of Cambridge · MRC Biostatistics Unit 等
- **分类**: vol 37 · issue 2 · pp 237-246
- 相关性 5/10 · novelty: `application`
- **摘要**: 本研究基于英国国家血友病数据库，分析了1970-1991年间因受污染血浆制品感染HIV和/或HCV的血友病患者的长期生存情况。队列纳入1992年1月1日仍存活的6282名血友病患者，其中15%为HIV/HCV合并感染，32%为HCV抗体阳性，28%为HCV抗体阴性。主要分析方法为Cox比例风险模型，分三个时期（1992-1999、2000-2009、2010-2019）估计不同感染组相对于HCV阴性组的全因死亡风险比，并利用UK一般人群生命表或参数生存模型估计各时期及感染组的寿命损失年。结果显示，即使在HCV血液筛查实施30年后，HCV阳性组在2010-2019年的死亡风险比仍为2.2（95%CI: 1.7-2.8），HIV/HCV合并感染组为4.2（2.9-6.0），寿命损失年依然显著。这对您有用：作为流行病学应用实例，其多时期Cox模型与寿命损失年估计的框架可迁移至其他慢性感染队列的长期预后分析，且数据集公开可用，适合练习因果推断中的时变混杂调整方法。
- **关键技术**: `Cox proportional hazards`, `parametric survival models`, `life table methods`, `epoch analysis`, `years of life lost estimation`
- **为什么对您有用**: 本文属于secondary interest中的流行病学方向，该研究使用经典的生存分析框架（Cox模型、寿命损失年）处理真实队列数据，分析模式清晰，数据集（National Haemophilia Database）有公开访问可能。您可以用moderately_familiar的因果识别工具（如时变混杂的IPW或g-formula）与本文的简单周期分析做对比，评估长期暴露的因果效应差异。本文适合作为流行病学应用的入门读物，武器库中的非参数统计和M估计理论足以支撑理解其方法学基础，值得花时间读全文以积累流行病学数据分析的实战经验。

### 7. [10.1097/ede.0000000000001941](https://doi.org/10.1097/ede.0000000000001941) — Neighborhood-level Measures of Structural Racism and Severe Maternal Morbidity Among Black Mothers in California
- **作者**: Elleni M. Hailu, Corinne A. Riddell, Mahader Tamene, Suzan L. Carmichael, Mahasin S. Mujahid
- **期刊/来源**: Epidemiology
- **机构**: Stanford University · Berkeley Public Health Division · University of California, Berkeley
- **分类**: vol 37 · issue 2 · pp 247-256
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文研究加州黑人母亲的重度孕产期发病率（SMM）与社区层面结构性种族主义的关联，estimand 为结构性种族主义指标对 SMM 风险的因果效应（以 OR 衡量），假设种族主义指标可视为外生暴露。方法上，作者从六个领域（房屋所有权、失业、贫困等）构建结构性种族主义度量：一是加法复合指数（四分位），二是潜在类别分析（LCA）提取四种类型学，再用混合效应 logistic 回归（社区随机截距）估计关联，调整母亲年龄、教育及保险。结果显示，高复合指数（Q4 vs Q1）的 SMM 风险增加 13%（95% CI: 1.04–1.24），LCA 高种族不平等类型的风险增加 12%（95% CI: 1.03–1.23）。作为流行病学应用，本文提供了大规模医院出生-普查关联数据（N≈555k）及结构性种族主义的多维测量框架，对您在流行病学因果推断方向理解结构性暴露的测量与建模有参考价值。
- **关键技术**: `latent class analysis`, `mixed-effects logistic regression`, `composite index construction`, `neighborhood random intercept`, `census-tract linkage`
- **为什么对您有用**: 本文属于流行病学因果推断的应用工作，提供了大规模关联数据集和结构性种族主义的多维测量方案，可作为理解流行病学中结构性暴露如何建模的入门案例。武器库中的 identification theory 和 M-estimation theory 可用于审视本文的混杂调整策略（仅调年龄/教育/保险是否足以 identification）及 LCA 测量误差对估计的影响。**中期可做**：需先在 moderately_familiar 的 identification theory 上长肌肉，才能对这类结构性暴露的因果 identification 做出实质性推进。

### 8. [10.1097/ede.0000000000001942](https://doi.org/10.1097/ede.0000000000001942) — Historical Neighborhood Redlining and Fertility in a Cohort of US Black Women
- **作者**: Mary D. Willis, Chen Sheng, Sharonda M. Lovett, Talia Feldscher, Kendra D. Sims, Brittney Francis et al.
- **期刊/来源**: Epidemiology
- **机构**: Boston University · Harvard University
- **分类**: vol 37 · issue 2 · pp 268-277
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文利用美国黑人女性健康研究（Black Women’s Health Study）队列数据，探究1930年代Home Owners’ Loan Corporation（HOLC）红线划界政策对当代生育能力（fecundability）的影响。暴露变量为居住社区的历史HOLC分级（A“最佳”至D“危险”，即redlined），结局为计划怀孕的每周期受孕概率。方法采用比例概率回归结合广义估计方程（GEE），估计受孕率比（fecundability ratio），并调整个体及社区层面的社会人口学混杂因素。地址通过地理编码与历史红线地图匹配。结果发现，相较于居住在A/B级区域的女性，居住在D级区域的女性受孕率降低18%（FR=0.82, 95%CI: 0.68-0.99），居住在C级的趋势类似但未达统计显著。结论支持历史结构性种族主义通过社区资源剥夺影响当代生殖健康。对您而言，这是一篇较好的流行病学应用入门读物，数据与设计清晰，可直接使用您very_familiar中的因果推断估计理论（混杂控制、敏感性分析）评估其证据强度，立即可读。
- **关键技术**: `Proportional probabilities regression`, `Generalized estimating equations (GEE)`, `Historical redlining exposure classification`, `Time-to-pregnancy analysis`, `Confounding adjustment for socioeconomic factors`
- **为什么对您有用**: 论文直接关联您的secondary interest中的流行病学方向，具体展示了队列研究中利用历史政策变量（HOLC分级）作为自然暴露，估计结构性种族主义对生殖健康影响的因果效应。您的very_familiar工具包中的“estimation theory in causal inference”和“nonparametric statistics”足以批判地审视其混杂调整是否充分（如是否引入DAG或进行敏感性分析），并考虑更稳健的估计方法（如G-computation或IPW）。本文方法门槛低，属于立即可读的流行病学应用，数据集和问题设计值得借鉴，可作为理解政策评估类因果实证研究的起点。

### 9. [10.1097/ede.0000000000001931](https://doi.org/10.1097/ede.0000000000001931) — Comparison of Lactation Information from Electronic Health Records with Survey Data Across Five US Health Systems
- **作者**: Gregory P. Jansen, Elisabeth M. Seburg, Gabriela Vazquez-Benitez, Kirsten Ehresmann, Hibo H. Mohamed, Lyndsay A. Avalos et al.
- **期刊/来源**: Epidemiology
- **机构**: University of Minnesota · Minnesota Department of Health · HealthPartners · Kaiser Permanente · Henry Ford Health System
- **分类**: vol 37 · issue 2 · pp 198-206
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文在流行病学设定下，比较了电子健康记录（EHR）中结构化哺乳数据与调查问卷数据的一致性，目标 estimand 为哺乳状态（ever 与 at survey）的 agreement 指标（kappa、sensitivity、PPV 等）。研究纳入五家美国医疗系统的 281 名产后抑郁个体，以 3-4 月后的调查数据为 reference，对比 EHR 中最多 10 月的记录。核心发现是两种数据源的一致性 ≥92%，kappa ≥0.77，EHR 对调查中"曾哺乳"与"当前哺乳"的 PPV 分别达 97.3% 与 98.0%，但记录数较少的个体一致性下降。该文为纯实证比较，无新方法学贡献，但提供了 EHR 哺乳数据可用性的量化证据。对您而言，若关注流行病学队列中 EHR 数据的 measurement error / misclassification 对因果估计的影响，此文的 descriptive 统计可作为背景参考。
- ⚠️ *摘要不完整，待重跑（`python -m research_news.rerun`）*
- **关键技术**: `Cohen's kappa`, `sensitivity / specificity / PPV / NPV`, `EHR structured data extraction`, `survey data as reference standard`, `measurement agreement study`
- **为什么对您有用**: 本文属于流行病学应用，连接到 epidemiology (datasets, applied causal work) 子方向，提供了多系统 EHR 哺乳数据与调查数据的 misclassification 量化指标。从武器库角度看，very_familiar 的 estimation theory in causal inference 可直接攻入：若后续要用此 EHR 数据做因果估计，可用 misclassification model 修正估计量的 bias。但本文本身无方法学 novelty（novelty_flag = application），仅提供 descriptive 数据。Follow-up 判断：**立即可做**——若您想研究 EHR misclassification 对 ATE 估计的 sensitivity，本文的 kappa/PPV 数据可直接作为 misclassification 参数输入您熟悉的 sensitivity analysis 框架。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

