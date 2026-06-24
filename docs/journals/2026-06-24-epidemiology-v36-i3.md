# Epidemiology — Vol 36  Issue 3  ·  2026-06-24

- 共 15 篇 · Epidemiology
- 目录核对 ⚠️ 疑似漏 6 篇（对照 OpenAlex 22 篇）：10.1097/ede.0000000000001844、10.1097/ede.0000000000001845、10.1097/ede.0000000000001828、10.1097/ede.0000000000001829、10.1097/ede.0000000000001833 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期内容主要围绕因果推断方法在复杂流行病学问题中的应用展开，形成了三条明显的主线：一是因果识别策略与偏倚校正，涉及中间变量处理、死亡截断、外部数据校正及三角验证等；二是因果估计量的界定与理论性质，聚焦于传染病干预背景下的效应分解与界；三是数据整合与测量问题，涵盖潜变量测量、多源数据融合及种群规模估计。此外，还有多篇应用准实验设计、数学建模及传统流行病学设计的实证研究。

在因果识别策略方面，本期有多篇论文针对具体偏倚结构提出解决方案。关于中间混杂的处理，"Adjusting for Causal Intermediate Confounders" 一文在围产期悖论背景下，对比了将中间混杂视为暴露诱导混杂因子或多中介两种策略，并推导了干预效应的未测量混杂偏倚公式。针对死亡截断问题，"Effect Modification in Settings with Truncation by Death" 推导了存活者平均因果效应（SACE）的效应修饰条件，明确了主分层框架下权重的依赖结构。在混杂调整不一致问题上，"Adjusting Adjustments" 提出利用外部数据估计偏倚因子以校正已发表关联，而 "Hospital Delivery Volume" 则采用观察设计、兄弟姐妹比较与邻居比较三种设计进行三角验证，通过结果的不一致性揭示残余混杂。

在因果估计量界定与理论性质方面，"Causal Estimands for Analyses of Averted and Avertible Outcomes" 在传染病干预背景下形式化了"避免结果"与"可避免结果"的估计量，通过 SIRD 模型证明在参数时变情况下直接效应作为总体效应下界的假设可能失效。这一工作与上述因果识别研究相呼应，共同强调了在特定数据生成机制下明确估计量定义的重要性。此外，"Evaluating the Effect of Public Health and Social Measures" 通过数学建模分离了免疫动态变化对干预效果评估的影响，同样涉及对核心估计量 R(t) 的动态调整。

对于关注因果推断与半参数效率的研究者，建议优先阅读 "Effect Modification in Settings with Truncation by Death" 与 "Causal Estimands for Analyses of Averted and Avertible Outcomes"，前者涉及主分层框架下的识别问题，后者探讨了干扰背景下的效应界。关注高维数据整合与测量误差的读者可参考 "Latent Trait-based Measure" 与 "Estimating Prevalence of Opioid Misuse"，两者分别展示了潜变量模型与集成丰度模型在多源数据融合中的应用。

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.1097/ede.0000000000001848](https://doi.org/10.1097/ede.0000000000001848) — Does Adjusting for Causal Intermediate Confounders Resolve the Perinatal Crossover Paradox?
- **作者**: Wen Wei Loh, Cande V. Ananth
- **期刊/来源**: Epidemiology
- **机构**: Maastricht University · Rutgers, The State University of New Jersey · Johnson University · Environmental and Occupational Health Sciences Institute
- **分类**: vol 36 · issue 3 · pp 350-362
- 相关性 8/10 · novelty: `application`
- **摘要**: 这篇论文研究围产期流行病学中著名的“早产悖论”：先兆子痫患者早产时围产儿死亡率反而低于正常血压孕妇，中介分析通过早产（PTB）作为中介变量未能解释这一悖论。作者利用美国安全劳动联盟队列数据，采用interventional (in)direct effects框架，比较两种处理中间混杂（胎盘早剥、小于胎龄、绒毛膜羊膜炎）的策略：作为暴露诱导混杂因子或作为多个中介变量。核心方法是对比两种策略下的估计结果，并推导了针对interventional effects的未测量混杂偏倚公式（bias formulas）。结果显示，即使调整这些中间混杂，先兆子痫对围产儿死亡的保护性直接效应仍然存在（风险比0.60，95%CI 0.52-0.71），悖论未消除。敏感性分析表明，只有对结局影响很强且与PTB相关的未测量混杂才能解释该悖论。该研究为流行病学中介分析中中间混杂的处理和敏感性分析提供了具体范例，对您的中介分析与敏感性分析方法学兴趣有直接参考价值。
- **关键技术**: `interventional (in)direct effects`, `bias formulas for unmeasured confounding`, `causal mediation with intermediate confounders`, `Consortium on Safe Labor data`
- **为什么对您有用**: 论文直接呼应您的primary interest中的中介分析与敏感性分析方向，使用interventional effects处理中介路径中的暴露诱导混杂，这是您moderately_familiar中identification theory的具体应用。您可以用very_familiar的estimation theory in causal inference推导其bias formulas的finite-sample性质或开发更紧的敏感性分析边界——立即可做，因为工具都在武器库中。

### 2. [10.1097/ede.0000000000001834](https://doi.org/10.1097/ede.0000000000001834) — Effect Modification in Settings with “Truncation by Death”
- **作者**: Bronner P. Gonçalves, Etsuji Suzuki
- **期刊/来源**: Epidemiology
- **机构**: University of Surrey · Harvard University · Okayama University
- **分类**: vol 36 · issue 3 · pp 374-380
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 本研究探讨流行病学中因死亡截断（truncation by death）导致的效应修饰问题，即当结局（如生活质量）对死亡个体未定义时，目标估计量为存活者平均因果效应（SACE），定义在“永远存活”主层（always-survivors）上。使用潜在结果框架和主分层（principal stratification）推导出SACE被共同影响生存和结局的变量或仅影响生存的变量修饰的条件。进一步，将SACE表示为这些变量各层内因果效应的加权平均，权重不仅取决于总体中变量水平的相对频率，还依赖于“永远存活”主层本身。该工作为SACE的可迁移性（transportability）提供了理论基础，对流行病学中处理死亡截断的因果推断实践具有指导意义。本文框架清晰，适合作为流行病学因果推断应用的标准入门读物。
- **关键技术**: `Potential outcomes framework`, `Principal stratification`, `Survivor average causal effect (SACE)`, `Effect modification`, `Transportability of causal effects`, `Weighted average decomposition`
- **为什么对您有用**: 本文是流行病学中处理死亡截断问题的因果推断入门级读物，以潜在结果和主分层框架清晰地阐述了SACE的识别与效应修饰机制，对于您进入流行病学应用方向具有较好的引导作用。您的武器库中已有的因果推断识别理论和非参数统计功底足以支撑您理解本文方法，并可进一步将您熟悉的高阶U统计或张量收缩视角用于评估主分层加权估计的计算成本。值得花时间仔细阅读全文以掌握该领域的标准分析模式。

## 流行病学  *(epidemiology, 13 篇)*

### 1. [10.1097/ede.0000000000001840](https://doi.org/10.1097/ede.0000000000001840) — The Effects of Hospital Delivery Volume and Travel Time on Perinatal Mortality and Delivery in Transit: Causal Inference with Triangulation
- **作者**: Andreas Asheim, Sara Marie Nilsen, Signe Opdahl, Kari Risnes, Elisabeth Balstad Magnussen, Fredrik Carlsen et al.
- **期刊/来源**: Epidemiology
- **机构**: Norwegian University of Science and Technology · St Olav's University Hospital · The London College · University College London · Nord University
- **分类**: vol 36 · issue 3 · pp 425-435
- 相关性 8/10 · novelty: `application`
- **摘要**: 本研究利用挪威医疗出生登记数据（1999-2016），采用三种研究设计（观察混杂调整、兄弟姐妹比较、邻居比较）来三角化推断医院年分娩量与旅行时间对围产期死亡率和途中分娩的因果效应。观察设计显示高年分娩量（2000 vs 500例）与围产期死亡率升高相关（RR=1.81），但兄弟姐妹和邻居比较却提示降低关系（RR分别为0.64和0.61），说明混杂调整不足以消除选择偏倚。旅行时间增加在观察设计中与死亡率强相关，但另两种设计不支持此结论；而旅行时间与途中分娩风险的一致性关联则被三种设计共同验证。方法上，三种设计分别依赖不同的未观测混杂假设（无混杂、家户固定效应、邻近区域固定效应），通过结果的不一致性暴露了传统回归的局限性。对您而言，这篇流行病学应用论文展示了三角化推断在实际数据中识别混杂偏倚的威力，可作为您因果推断中敏感性分析教学或方法验证的案例。
- **关键技术**: `triangulation of multiple study designs`, `sibling comparison (within-family fixed effects)`, `neighbor comparison (spatial fixed effects)`, `observed confounder adjustment`, `perinatal mortality estimation`
- **为什么对您有用**: 论文属于流行病学领域的应用因果推断，是您的secondary interest之一。其核心是观察性研究中的混杂偏倚诊断，与您causal inference中identification theory和敏感性分析高度相关。三角化方法要求对不同设计背后的识别假设有清晰理解——您的very_familiar工具（估计理论）可用于定量评估各设计估计量的偏差方向，moderately_familiar的identification理论则可用于严格形式化各设计的识别条件。该文适合作为gateway reading切入流行病学数据中的因果推断实践，但方法学深度有限，属于应用案例而非理论突破，阅读后可尝试用您熟悉的minimax框架分析此类偏倚的bound。

### 2. [10.1097/ede.0000000000001839](https://doi.org/10.1097/ede.0000000000001839) — Causal Estimands for Analyses of Averted and Avertible Outcomes due to Infectious Disease Interventions
- **作者**: Katherine M. Jia, Christopher B. Boyer, Jacco Wallinga, Marc Lipsitch
- **期刊/来源**: Epidemiology
- **机构**: Center for Disease Dynamics, Economics & Policy · Leiden University Medical Center · National Institute for Public Health and the Environment · Harvard University
- **分类**: vol 36 · issue 3 · pp 363-373
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文在传染病干预（如疫苗接种）背景下，使用潜在结果框架形式化了“避免结果”（averted outcomes）和“可避免结果”（avertible outcomes）的因果估计量。作者将直接效应和总体效应调整后与标准直接、间接、总体因果效应（考虑干扰）联系起来。通过一个按接种状态分层的易感-感染-恢复-死亡（SIRD）模型，检验了“仅通过直接效应估计的避免/可避免结果是总体效应的下界”这一常见假设。发现当疫苗效力衰减、传播参数或病死率随时间变化时，该下界可能失效。只有在所有参数时间不变的最简单情景下，直接效应下界才成立。本文指出，实际数据分析中若未检查间接效应方向，直接计算直接效应作为下界可能不可靠。对您而言，该工作将因果推断中干扰下的估计量形式化与流行病学实用问题结合，是流行病学因果推断应用的有益参考。
- **关键技术**: `potential outcomes`, `interference`, `direct, indirect, total, and overall effects`, `SIRD model`, `lower bound assumption tests`
- **为什么对您有用**: 本文直接关联您的secondary interest中的流行病学因果推断应用，特别是干扰存在下的估计量定义和下界假设检验。您熟悉的因果推断identification理论与中介分析工具可用于评估其假设合理性（例如参数时变性对间接效应方向的影响），但本文主要为应用形式化，无需新方法介入，可作为流行病学因果推断应用案例阅读。

### 3. [10.1097/ede.0000000000001821](https://doi.org/10.1097/ede.0000000000001821) — Adjusting Adjustments: Using External Data to Estimate the Impact of Different Confounder Sets on Published Associations
- **作者**: Thomas P. Ahern, Lindsay J. Collin, Richard F. MacLehose, Benjamin Littenberg, Laura Haines, Michaela Bonnett et al.
- **期刊/来源**: Epidemiology
- **机构**: University of Vermont · U.S. National Science Foundation · University of Utah · Huntsman Cancer Institute · University of Minnesota · Vermont Department of Health · Emory University · Aarhus University
- **分类**: vol 36 · issue 3 · pp 381-390
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文针对观察性研究 meta-analysis 中各原始研究混杂调整不一致的问题，提出利用外部数据（NHANES III）进行"外部调整"的方法。核心 estimand 是暴露-结局关联（此处为超重 BMI 与全因死亡率的 risk ratio）在不同混杂调整集下的变化；关键假设是外部数据中暴露-混杂因子、混杂因子-结局的关联可迁移到目标研究人群。方法上，作者基于外部数据估计 bias factor，量化从原始调整集切换到"充分调整集"时 ratio measure 的位移，进而对原始效应估计进行校正。理论层面未涉及 formal identification 理论或 semiparametric efficiency，属于应用驱动的 sensitivity-type 调整；实证结果显示，对 33 项研究统一调整年龄、性别、吸烟后，汇总效应从 0.88 变为 0.90，异质性 I² 从 38.4% 降至 34.6%。对您而言，这是一个流行病学应用案例，展示了如何用外部数据校正混杂调整差异——方法学 novelty 有限，但数据集和操作流程可作为因果推断 sensitivity analysis 的实证参考。
- ⚠️ *摘要不完整，待重跑（`python -m research_news.rerun`）*
- **关键技术**: `external adjustment`, `bias factor`, `confounder selection`, `meta-analysis heterogeneity`, `transportability assumption`
- **为什么对您有用**: (1) 连接到流行病学队列研究的因果推断应用，展示了外部数据在混杂调整校正中的实际操作。(2) 本文方法本质上是 sensitivity analysis 的一个特例，但缺乏 formal identification 理论和 semiparametric efficiency 视角——您熟悉的 identification theory 和 semiparametric theory 可以用来严格刻画外部调整所需的 transportability 假设，并构造更高效的 estimator。(3) **中期可做**：需先在 moderately_familiar 的 identification theory 上长肌肉，将本文的 ad-hoc bias factor 方法嵌入到更严格的 sensitivity analysis 框架中（如 proximal CI 或 negative control 设定），形式化外部数据的使用条件。

### 4. [10.1097/ede.0000000000001841](https://doi.org/10.1097/ede.0000000000001841) — A Quasi-experimental Study of General Practices’ Referral to Mammography in the Posttrial Treatment Era
- **作者**: Mette Lise Lousdal, Timothy L. Lash, W. Dana Flanders, M. Alan Brookhart, Ivar Sønbø Kristiansen, Peter Vedsted et al.
- **期刊/来源**: Epidemiology
- **机构**: Aarhus University · Aarhus University Hospital · Emory University · Duke University · University of Southern Denmark · University of Oslo · Regionshospitalet Silkeborg · Steno Diabetes Centers
- **分类**: vol 36 · issue 3 · pp 401-407
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文在丹麦无组织筛查地区设计了一项准实验队列研究，评估乳腺X线摄影对50-66岁无症状女性乳腺癌死亡率的影响。研究以全科诊所（GP）为单位，首先基于患者个体风险因素预测各诊所的预期钼靶检查次数，然后计算实际与预期检查次数的比值，将该比值作为诊所层面的工具变量（IV）。每个女性被分配其所属诊所的IV值作为暴露状态，采用Cox比例风险模型估计风险比（HR=0.80, 95%CI: 0.68-0.95），发现高转诊率诊所的女性乳腺癌死亡风险更低。阴性对照分析（如非乳腺癌死亡）的关联接近零，提示未受不可观测混杂偏倚污染。该方法的核心创新在于利用诊所间转诊行为的差异作为准随机变异性，避免了传统观察性研究中因治疗改进等时间趋势带来的混杂。对于您而言，本文展示了如何在实际流行病学数据中构建工具变量并实施阴性对照检验，是因果推断方法在流行病学中的典型应用，可直接与您对IV和敏感性分析的已有知识对接。
- **关键技术**: `instrumental variable`, `negative control`, `quasi-experimental design`, `predicted-to-expected ratio`, `Cox proportional hazards`
- **为什么对您有用**: 本文直接关联您对流行病学应用因果推断的兴趣（secondary interest），特别展示了工具变量在非随机化环境中的实际构建方法。您武器库中"causal inference estimation theory"（very_familiar）可以立即用于理解其IV估计的识别假设和方差估计，而"identification theory"（moderately_familiar）则可用于分析该IV的排他性与相关性是否合理。立即可做：您无需额外工具即可评价其方法学合理性，并考虑将类似的诊所指派IV策略迁移到其他筛查或治疗效果的流行病学研究中。

### 5. [10.1097/ede.0000000000001832](https://doi.org/10.1097/ede.0000000000001832) — A Latent Trait-based Measure as a Data Harmonization and Missing Data Solution Applied to the Environmental Influences on Child Health Outcomes Cohort
- **作者**: Emily A. Knapp, Amii M. Kress, Ronel Ghidey, Tyler J. Gorham, Brendan Galdo, Stephen A. Petrill et al.
- **期刊/来源**: Epidemiology
- **机构**: Johns Hopkins University · Nationwide Children's Hospital · The Ohio State University · Harvard University · Harvard Pilgrim Health Care · University of Southern California · Massachusetts General Hospital · University of California, San Francisco 等
- **分类**: vol 36 · issue 3 · pp 413-424
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文在 ECHO 多队列协作联盟中应用 ROSETTA 潜变量方法，解决多队列数据一致化与缺失数据问题。目标是构建社会经济地位（SES）的通用测量指标。从 53 个队列的 39,372 名参与者中提取 52 个产前 SES 指标，通过因子分析提取三个潜在因子（收入与教育、保险与贫困、失业）。每个因子分数至少对 34,528 名参与者可用，且两因子同时可用的样本量超过任何单一指标。因子拟合良好，与替代 SES 测量相关性为 0.40–0.89。更高效的 SES（因子分数）与产前吸烟概率降低显著相关（OR=0.42）。相比多数缺失数据处理方法，ROSETTA 减少了缺失程度，仅略逊于多重插补。对您而言，本文是流行病学中多中心数据融合与缺失数据处理的一个扎实应用案例，其潜变量框架可用于您在因果推断中处理测量误差或代理变量的识别问题。
- **关键技术**: `latent variable model`, `factor analysis`, `data harmonization`, `missing data`, `ROSETTA`, `multiple imputation comparison`
- **为什么对您有用**: 本论文属于您的 secondary interest 流行病学中的真实数据分析，展示了如何在大规模多队列协作中整合不一致的测量并处理缺失数据。您熟悉的高维统计与因果推断中的测量误差思路可以与此潜变量方法交叉：例如用您的 higher-order U-statistics 或 semiparametric 工具来评估因子模型估计的精度。此外，本文作为 gateway reading 对流行病学领域的入门很有价值，数据描述和缺失数据处理细节清晰，值得花时间通读。

### 6. [10.1097/ede.0000000000001836](https://doi.org/10.1097/ede.0000000000001836) — Plant-Capture Methods for Estimating Homeless Population Size From Uncertain Plant Captures
- **作者**: Yiran Wang, Martin Lysy, Audrey Béliveau
- **期刊/来源**: Epidemiology
- **机构**: University of Waterloo
- **分类**: vol 36 · issue 3 · pp 319-326
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究植物捕获法（plant-capture）在估算无家可归人口规模中的应用，这是捕获-再捕获法的一个变体。传统方法通常忽略个体植物捕获状态的不确定性，作者提出三个层次复杂的层次模型来形式化地纳入这种不确定性，并允许不同调查站点之间存在异质性。模型使用贝叶斯或频率主义框架实现，通过MCMC或最大似然估计求解。文章将方法应用于美国人口普查局S-Night研究中25个大城市的无家可归人口数据，给出了点估计和区间估计。实证评估显示，考虑不确定性后估计的区间更长，更符合实际。本文为流行病学中种群规模估计提供了一种更严谨的不确定性量化框架。作为流行病学应用实例，其数据分析管道和模型构建思路对您从事卫生领域的应用研究有参考价值。
- **关键技术**: `plant-capture`, `hierarchical Bayesian modeling`, `capture-recapture`, `uncertainty quantification`, `Markov chain Monte Carlo`, `heterogeneity modeling`
- **为什么对您有用**: 本文属于流行病学中的种群估计应用，与您secondary interest中的epidemiology应用方向直接对接。可作为了解该领域常见数据结构和分析管道的入门材料。不过，核心方法（层次贝叶斯捕获模型）不在您当前技术武器库的直接射程内（缺贝叶斯分层建模和MCMC实现经验），因此适合作为中期可读的案例研究，不涉及主动的方法学攻击。

### 7. [10.1097/ede.0000000000001838](https://doi.org/10.1097/ede.0000000000001838) — Estimating Prevalence of Opioid Misuse in North Carolina Counties From 2016 to 2021: An Integrated Abundance Model Approach
- **作者**: David M. Kline, Brian N. White, Kathryn E. Lancaster, Kathleen L. Egan, Eva Murphy, William C. Miller et al.
- **期刊/来源**: Epidemiology
- **机构**: Wake Forest University · University of North Carolina at Chapel Hill
- **分类**: vol 36 · issue 3 · pp 310-318
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对北卡罗来纳州2016-2021年县级阿片类药物滥用流行率无法直接观测的问题，采用集成丰度模型（integrated abundance model）进行估计。该模型通过贝叶斯分层框架，整合了县级非法阿片类药物过量死亡人数、丁丙诺啡处方人数、治疗项目服务人数以及州级调查流行率估计，同时纳入县级社会与环境协变量。核心方法是利用多源数据构建状态空间模型，通过马尔可夫链蒙特卡洛采样得到流行率后验分布。结果显示，研究期间滥用流行率总体呈下降趋势，但西部和东南部县流行率高于均值；同时，滥用者中致命过量比例在2016-2021年间增长了8倍以上。该研究填补了地方层面阿片类药物滥用负担的空白，为资源分配提供了实证依据。对于您的流行病学应用兴趣，本文展示了如何将多种行政与调查数据通过贝叶斯模型进行融合，其数据整合策略和分析流程可直接迁移至其他疾病或地区的流行率估计问题。
- **关键技术**: `integrated abundance model`, `Bayesian hierarchical model`, `data integration`, `state-space model`, `Markov chain Monte Carlo`
- **为什么对您有用**: 本文直接对应您的secondary interest中的流行病学应用方向（阿片类药物滥用流行率的县级估计）。其核心价值在于提供了真实数据、模型设定与推断过程的完整范例——特别是如何利用贝叶斯分层模型融合多个不完整数据源（死亡、处方、治疗项目）来估计不可观测的流行率。若您对因果推断中的测量误差或数据融合问题感兴趣（属very_familiar的估计理论），可借鉴其多源数据整合的贝叶斯建模思路，例如在因果推断中处理缺失或误分类数据时采用类似的贝叶斯结构。整体而言，该文作为流行病学领域应用论文，方法学新颖性有限（属于成熟方法的迁移应用），但数据分析框架对您未来接触流行病学数据时有参考价值，值得花时间阅读全文以学习数据预处理和解构。

### 8. [10.1097/ede.0000000000001835](https://doi.org/10.1097/ede.0000000000001835) — Impact of Activity Participation on the Risk of Mortality and Hospitalizations in Danish Men and Women: Insights from REGLINK-SHAREDK
- **作者**: Linda Juel Ahrenfeldt, Jens Søndergaard, McKinsley Laro, Sören Möller, Tobias Anker Stripp
- **期刊/来源**: Epidemiology
- **机构**: University of Southern Denmark · Odense University Hospital · University of Copenhagen · Harvard University · Quantitative BioSciences
- **分类**: vol 36 · issue 3 · pp 297-305
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文基于SHARE调查中2004-2007年访谈的2987名40岁以上丹麦居民，将其与丹麦注册登记数据链接（REGLINK-SHAREDK），随访至2018年，旨在评估志愿工作、帮助他人、参加体育/社交俱乐部、宗教组织等多种活动参与及其频率对死亡率和住院风险的影响。采用泊松或负二项回归估计相对风险（RR）和风险差（RD），并调整多种潜在混杂因素。结果发现大多数活动参与与较低死亡率相关，尤其是女性；志愿工作、帮助他人和参加俱乐部活动的RR在0.85-0.89之间。住院次数减少主要体现在男性参与宗教组织或参与3项以上活动的人群中，而照顾病人仅在每周少于一次时与住院减少相关。该研究利用高质量丹麦注册数据，以流行病学标准方法（回归调整控制混杂）给出了详细的亚组和频次分析，对于关注活动干预与健康因果效应的应用研究者具有参考价值。
- **关键技术**: `cohort study`, `negative binomial regression`, `relative risk`, `risk difference`, `confounder adjustment`
- **为什么对您有用**: 本文是流行病学领域典型的观察性因果推断应用，直接对应研究者的secondary interest中的流行病学数据集和因果推断实践。研究采用的混杂调整回归方法是因果推断中基础的估计策略，研究者可从中理解注册数据链接的分析模式，并评估是否可与自身更复杂的因果方法（如IV、proximal CI）结合。作为应用论文，适合快速阅读以了解丹麦健康数据的分析流程，但不涉及新方法学贡献，因此属于‘中期可读’——需要先在流行病学数据理解上投入少许时间，但武器库中的估计理论足以支撑批判性评估。

### 9. [10.1097/ede.0000000000001843](https://doi.org/10.1097/ede.0000000000001843) — Long-term Economic Distress and Growing Educational Inequity in Life Expectancy
- **作者**: Arline T. Geronimus, Timothy A. Waidmann, John Bound, Vincent Pancini, Meifeng Yang
- **期刊/来源**: Epidemiology
- **机构**: University of Michigan · Michigan Medicine · Urban Institute · National Bureau of Economic Research
- **分类**: vol 36 · issue 3 · pp 287-296
- 相关性 5/10 · novelty: `application`
- **摘要**: 该论文研究美国长期经济困难（全球化与技术变革导致的劳动力市场恶化）是否加剧了不同教育水平群体间的预期寿命不平等。利用1990-2017年通勤区层面的时空变异，作者以基线产业组合构建宏观经济重组的外生度量（类似工具变量设计），估计其对死亡率趋势的因果效应。结果显示，长期经济停滞区域的死亡率恶化更严重，且教育最低四分之一人群受影响最大。通过中介分析发现，癌症、心血管与代谢疾病等应激相关内部疾病是主要中介路径，而自杀或物质滥用贡献很小。该文为流行病学中压力-健康因果关系提供了基于准实验设计的经验证据，对因果推断方法在群体健康领域的应用有直接示范作用。
- **关键技术**: `instrumental variable based on industrial mix`, `commuting zone analysis`, `difference-in-differences (spatiotemporal variation)`, `mediation analysis`, `mortality trend decomposition`
- **为什么对您有用**: 该论文是流行病学中因果推断的典型应用，使用工具变量识别长期经济条件对死亡率的教育不平等效应，直接关联到secondary interest中的流行病学应用。研究者熟悉的estimation theory in causal inference可用于评估其工具变量外生性假设与估计策略，identification theory则可帮助审视中介路径的分解逻辑。该方法框架与数据模式（通勤区面板、外生冲击）立即可为研究者复现或扩展分析所用。

### 10. [10.1097/ede.0000000000001831](https://doi.org/10.1097/ede.0000000000001831) — Helicobacter pylori Eradication Treatments and Risk of Alzheimer Disease: A Case–Control Study Nested in the Finnish Population
- **作者**: Emmi Keränen, Jaana Rysä, Miia Tiihonen, Sirpa Hartikainen, Anna-Maija Tolppanen
- **期刊/来源**: Epidemiology
- **机构**: University of Eastern Finland
- **分类**: vol 36 · issue 3 · pp 327-333
- 相关性 5/10 · novelty: `application`
- **摘要**: 本研究基于芬兰全国登记数据，开展了一项巢式病例对照研究，纳入70,520例阿尔茨海默病新发病例及281,233名按年龄、性别、居住地匹配的对照。暴露定义为AD诊断前至少5年开具的幽门螺杆菌根除治疗处方，结局为AD确诊。采用条件逻辑回归校正合并症与其他用药的混杂，结果显示粗OR为1.06（1.02, 1.11），校正后OR为1.03（0.99, 1.07），累计暴露次数与AD风险无关联。该结果不支持H. pylori感染作为AD独立危险因素的假说。先前报告的关联可能由反向因果与混杂解释。该研究设计严谨，利用国家处方登记避免回忆偏倚，并通过暴露滞后窗口处理前驱期混淆。对您而言，这是一篇流行病学应用论文，展示了如何利用注册数据与标准回归进行因果推断，尤其关注反向因果的处理策略。
- **关键技术**: `nested case-control design`, `conditional logistic regression`, `confounder adjustment using national registers`, `lagged exposure assessment to address reverse causation`
- **为什么对您有用**: 本文直接关联您在流行病学应用方向的兴趣，展示了利用全国注册数据开展因果推断的典型范例（巢式病例对照+条件逻辑回归），并专门处理了暴露与结局之间时间顺序的反向因果问题。您掌握的因果识别知识与非参数估计理论足以快速评价该研究的设计细节（如暴露滞后长度、混杂集选择），属于‘立即可做’的深入阅读材料。虽然方法学术新意不高，但作为真实数据应用，其数据结构与分析流程对您后续开展类似因果研究具有参考价值。

### 11. [10.1097/ede.0000000000001846](https://doi.org/10.1097/ede.0000000000001846) — Evaluating the Effect of Public Health and Social Measures Under Rapid Changes in Population-level Immunity Against SARS-CoV-2: A Mathematical Modeling Study
- **作者**: Sung-mok Jung, Jaehun Jung, Justin Lessler
- **期刊/来源**: Epidemiology
- **机构**: University of North Carolina at Chapel Hill · Jungheinrich (Germany) · Korea University · Johns Hopkins University
- **分类**: vol 36 · issue 3 · pp 334-343
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文研究在人群免疫快速变化背景下，如何准确评估公共卫生与社会措施（PHSM）对 SARS-CoV-2 传播的影响。核心 estimand 是时间变化的基本再生数 R(t)，关键假设包括感染诱导免疫与疫苗诱导免疫的动态变化及衰减。方法上构建了一个 compartmental 数学模型，将潜在免疫水平纳入 R(t) 的估计框架，从而分离 PHSM 的独立效应；通过反事实模拟讨论忽略免疫动态可能导致的偏倚方向与大小。实证分析使用韩国 2021 年 11 月至 2022 年 4 月的流行病学数据，发现 Omicron 期间 PHSM 的效果在调整免疫后显著减弱，且与人口流动模式相关。本文属于应用建模研究，方法学 novelty 有限，但提供了清晰的免疫-干预混杂结构示例。对您而言，这是一个展示如何将因果思维应用于流行病学动态模型的案例。
- **关键技术**: `compartmental mathematical model`, `time-varying reproduction number estimation`, `immunity dynamics modeling`, `counterfactual simulation`, `sensitivity to immunity misspecification`
- **为什么对您有用**: (1) 本文属于流行病学 secondary interest 的 gateway reading，展示了如何在干预评估中处理时变混杂（免疫水平）这一经典因果问题。(2) 武器库中的 identification theory in causal inference 足以理解本文的混杂结构，但模型设定属于 compartmental ODE 系统，非您熟悉的 semiparametric 框架。(3) 作为入门读物尚可，但方法学深度较浅，建议快速浏览图表与反事实分析部分即可，无需精读全文。

### 12. [10.1097/ede.0000000000001837](https://doi.org/10.1097/ede.0000000000001837) — Industrial Air Emissions and Breast Cancer Incidence in a United States-wide Prospective Cohort
- **作者**: Jennifer L. Ish, Jessica M. Madrigal, John L. Pearce, Alexander P. Keil, Jared A. Fisher, Rena R. Jones et al.
- **期刊/来源**: Epidemiology
- **机构**: National Institute of Environmental Health Sciences · National Cancer Institute · Division of Cancer Epidemiology and Genetics · Medical University of South Carolina
- **分类**: vol 36 · issue 3 · pp 391-400
- 相关性 4/10
- **摘要**: 本文研究工业空气排放物与乳腺癌发病率的关联，使用美国 EPA Toxics Release Inventory 数据量化 Sister Study 队列（n=46,150）参与者居住地 10 年内 28 种化合物的排放水平。主要方法包括 Cox 比例风险回归估计单个污染物的调整 HR，以及 Exposure Continuum Mapping (ECM) 框架分析污染物混合暴露，通过 joint-exposure response function 刻画联合暴露效应。随访中位数 13.4 年发现 4155 例乳腺癌病例，镍化合物和三氯乙烯在 3 km 范围内显示非单调但升高的关联（HR=1.3, 95% CI: 1.0-1.6）。ECM 识别出 25 种混合暴露模式解释 72% 的排放变异，高暴露罕见模式与较高乳腺癌发病率相关，但整体趋势无统计学意义（P=0.09）。作为应用性流行病学研究，本文的方法学 novelty 有限，但提供了大规模前瞻性队列的环境暴露数据和分析范例。
- **关键技术**: `Cox proportional hazards regression`, `Exposure Continuum Mapping`, `joint-exposure response function`, `pollutant mixture modeling`, `prospective cohort study`
- **为什么对您有用**: (1) 本文是典型的流行病学应用研究，属于 secondary interest 中的 epidemiology 方向，使用真实大规模队列数据（Sister Study）和环境暴露数据（EPA TRI）。(2) 从方法学角度，ECM 框架对混合暴露的处理方式可能与您熟悉的 semiparametric efficiency 或 high-dimensional 方法有潜在交叉，但本文未涉及因果推断框架（如 IV、sensitivity analysis、proximal CI），主要依赖传统 Cox 回归和描述性混合暴露分析。(3) 作为 gateway reading，本文适合了解环境流行病学的数据结构和常见分析方法，但方法学深度有限，不建议花时间精读全文——除非您对环境暴露的因果推断应用场景感兴趣，可考虑将 IV 或 sensitivity analysis 引入此类暴露混杂问题。

### 13. [10.1097/ede.0000000000001850](https://doi.org/10.1097/ede.0000000000001850) — Thanks to Our Reviewers
- **作者**: 
- **期刊/来源**: Epidemiology
- **分类**: vol 36 · issue 3 · pp 436-437
- 相关性 0/10 · novelty: `other`
- **摘要**: 本文是 Epidemiology 期刊 2024 年度的审稿人致谢名单，列举了 282 位参与同行评审的专家姓名及评审数量，并表彰了六位杰出审稿人。文章不涉及任何研究问题、方法或理论设定，纯为编辑部行政性致谢。无 estimand、无模型、无统计方法贡献。对您而言，本文仅作为流行病学期刊审稿人群体构成的参考信息，无方法学 novelty。
- **为什么对您有用**: 本文属于期刊行政性内容，与您的研究兴趣（因果推断、高维统计、效率理论等）无任何实质性关联。若您关注流行病学领域的研究动态或潜在合作者，可浏览名单中活跃审稿人（如部分作者在因果推断方法学有工作），但无需深入阅读。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

