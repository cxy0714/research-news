# Biostatistics — Vol 23  Issue 2  ·  2026-07-04

- 共 18 篇 · Biostatistics
- 目录核对 ⚠️ 疑似漏 1 篇（对照 OpenAlex 20 篇）：10.1093/biostatistics/kxaa029

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Biostatistics》第23卷第2期的18篇论文，整体上围绕**因果推断与效应修饰**、**高维与大规模数据计算**、以及**生物医学应用中的统计设计**三条主线展开。因果推断方向最为集中，涵盖工具变量、纵向治疗策略、效应修饰识别与中介分析；高维与计算方向聚焦于Cox模型、逻辑回归的快速算法及变量筛选；应用方向则涉及临床试验设计、诊断准确性评估和基因组学建模。

在因果推断主线中，多篇论文从不同角度推进了效应修饰与中介分析。**“An efficient and robust approach to Mendelian randomization”** 通过正则化处理高维工具变量下的多效性，提升因果估计效率；**“A sparse additive model for treatment effect-modifier selection”** 将加性非参数交互项与组Lasso结合，实现修饰因子筛选与非线性效应估计的联合。**“Evaluation of treatment effect modification by biomarkers”** 则针对非单调缺失数据，利用估计似然框架处理主分层分析。中介分析方面，**“The role of body mass index at diagnosis”** 提出密度回归中介方法，允许中介变量分布复杂变换，而**“Adaptive treatment strategies for chronic conditions”** 通过共享参数G估计提升纵向因果推断的效率。此外，**“Bayesian design of clinical trials”** 将联合模型与直接/间接效应分解结合，为临床试验设计提供因果推断视角。

高维与计算主线中，**“Fast Lasso method for large-scale and ultrahigh-dimensional Cox model”** 和 **“A divide-and-conquer method for sparse risk prediction”** 分别针对生存数据与二分类数据，提出分治与筛选结合的快速算法，适用于生物银行规模数据。**“Integrative functional linear model”** 将函数型数据分析与惩罚回归结合，用于多表型GWAS。假设检验方面，**“General tests of the Markov property”** 提出基于log-rank统计量的多状态模型检验。应用主线中，**“Surrogate-guided sampling designs”** 利用替代变量分层富集抽样提升罕见结局分类效率，**“Quantifying diagnostic accuracy improvement”** 将NRI/IDI扩展至竞争风险数据，**“Dose–response modeling”** 采用层次贝叶斯与深度神经网络建模药物筛选。

对于因果推断方向的研究者，建议优先阅读 **“An efficient and robust approach to Mendelian randomization”**（高维IV与多效性）、**“Adaptive treatment strategies for chronic conditions”**（纵向G估计与双稳健性）、**“A sparse additive model for treatment effect-modifier selection”**（修饰因子筛选与非线性交互）以及 **“Evaluation of treatment effect modification by biomarkers”**（非单调缺失下的主分层分析）。对于半参数效率与高维方向，**“Fast Lasso method”** 和 **“A divide-and-conquer method”** 提供了大规模数据下的计算框架，而 **“General tests of the Markov property”** 则涉及多状态模型的基础假设检验。

## 因果推断  *(causal_inference, 5 篇)*

### 1. [10.1093/biostatistics/kxaa045](https://doi.org/10.1093/biostatistics/kxaa045) · [arXiv](https://arxiv.org/abs/1911.00347) — An efficient and robust approach to Mendelian randomization with measured pleiotropic effects in a high-dimensional setting
- **作者**: Andrew J Grant, Stephen Burgess
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 609-625
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文在孟德尔随机化（MR）框架下，针对大量遗传变异作为工具变量时普遍存在的多效性问题，提出了一种正则化方法。标准的多变量MR需要将所有可能的多效性性状作为协变量纳入，但若某些协变量并非真正的多效性通路，会导致估计量效率低下。作者通过正则化（如Lasso）从一组候选协变量中自动筛选出需要调整的多效性通路，从而在控制偏倚的同时提高因果效应估计的效率。该方法仅需汇总统计量（summary-level data），无需个体数据，且允许候选协变量数量最多为遗传变异数减一。模拟研究展示了该方法在现实设定下的性能，并应用于尿酸浓度对冠心病因果效应的实证分析。对您而言，本文是工具变量（IV）方法在流行病学应用中的前沿案例，其正则化+汇总统计量的思路可迁移至您熟悉的因果推断设定中。
- **关键技术**: `Mendelian randomization`, `instrumental variables`, `regularization (Lasso)`, `summary-level data`, `pleiotropy adjustment`, `multivariable MR`
- **为什么对您有用**: 本文直接连接您的流行病学应用兴趣，展示了IV方法在高维多效性场景下的实际处理流程。您可以用very_familiar的因果推断估计理论（如正交评分）来审视其正则化选择是否最优，并考虑是否能用您熟悉的minimax bound分析其估计量的效率损失上界。中期可做：若想将类似方法推广到连续IV或非线性暴露，需先在moderately_familiar的identification theory上深入。

### 2. [10.1093/biostatistics/kxaa033](https://doi.org/10.1093/biostatistics/kxaa033) — Adaptive treatment strategies for chronic conditions: shared-parameter G-estimation with an application to rheumatoid arthritis
- **作者**: Shouao Wang, Erica Em Moodie, David A Stephens, Jagtar S Nijjar
- **期刊/来源**: Biostatistics
- **机构**: McGill University · GlaxoSmithKline (United Kingdom)
- **分类**: vol 23 · issue 2 · pp 430-448
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对慢性病中自适应治疗策略的估计问题，提出了一种共享参数G估计方法。传统方法假设各决策点的治疗规则参数独立，这在重复决策场景下不现实；共享参数可减少估计参数数量并简化临床实施。作者开发了一种新的计算算法，该算法在保持双稳健性的同时提高了效率，与未共享参数的序贯G估计相比具有优势。方法应用于苏格兰早期类风湿关节炎（SERA）队列数据，展示了实际可行性。理论部分证明了估计量的一致性和渐近正态性。对您而言，本文涉及纵向因果推断中的G估计和双稳健性，与您对因果推断（特别是纵向设定）和估计理论的兴趣直接相关。
- **关键技术**: `G-estimation`, `shared-parameter model`, `double robustness`, `adaptive treatment strategies`, `longitudinal causal inference`
- **为什么对您有用**: 本文直接连接您对因果推断中纵向设定和估计理论的兴趣，特别是G估计在重复决策场景下的扩展。您武器库中'因果推断中的估计理论'（very_familiar）可直接用于分析其双稳健性性质和渐近效率，而'识别理论'（moderately_familiar）可帮助评估共享参数假设的可检验性。中期可做：若想将共享参数思想推广到更复杂的识别设定（如proximal causal inference），需先在'识别理论'上加强。

### 3. [10.1093/biostatistics/kxaa032](https://doi.org/10.1093/biostatistics/kxaa032) · [arXiv](https://arxiv.org/abs/2006.00265) — A sparse additive model for treatment effect-modifier selection
- **作者**: Hyung Park, Eva Petkova, Thaddeus Tarpey, R Todd Ogden
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 412-429
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文针对随机试验中治疗效应修饰因子的识别与估计问题，提出了一种稀疏加性模型。模型将协变量与治疗的交互项（即治疗效应修饰项）参数化为加性非参数函数之和，而对协变量的主效应不做任何结构假设，从而将变量选择聚焦于真正影响治疗决策的修饰因子。估计采用带组Lasso惩罚的样条基展开，在惩罚框架下同时实现非线性交互函数的估计与修饰因子的筛选。理论部分证明了模型在特定正则条件下的变量选择一致性。模拟和真实临床试验数据（抗抑郁药治疗）展示了方法在识别非线性修饰因子上的优势。对您而言，本文属于应用导向的因果推断方法，其将变量选择与治疗效应异质性估计结合的设计，可启发您在proximal CI或IV设定下处理高维修饰因子的思路。
- **关键技术**: `sparse additive model`, `group Lasso`, `treatment effect modifier`, `nonparametric interaction`, `spline basis expansion`
- **为什么对您有用**: 本文直接对应您primary interest中的因果推断（治疗效应异质性）和高维统计（变量选择），且其将主效应与交互效应分离建模的策略，可迁移至您熟悉的nonparametric statistics框架下分析。武器库中'nonparametric statistics'和'high-dimensional asymptotics'可直接用于理解其理论保证，而'identification theory in causal inference'可帮助您评估该方法在观察性研究（如IV或proximal设定）中的扩展潜力。中期可做：若想将类似思路推广到IV设定下的修饰因子选择，需先在'moderately_familiar'的identification theory上补足工具。

### 4. [10.1093/biostatistics/kxaa040](https://doi.org/10.1093/biostatistics/kxaa040) · [arXiv](https://arxiv.org/abs/1710.09923) — Evaluation of treatment effect modification by biomarkers measured pre- and post-randomization in the presence of non-monotone missingness
- **作者**: Yingying Zhuang, Ying Huang, Peter B Gilbert
- **期刊/来源**: Biostatistics
- **机构**: University of Washington
- **分类**: vol 23 · issue 2 · pp 541-557
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文针对疫苗试验中治疗效应修饰（effect modification）的评估问题，提出在基线与随机后生物标志物存在非单调缺失（non-monotone missingness）时的分析方法。研究目标是基于中间生物标志物的主分层（principal strata）与基线生物标志物值进行双变量效应修饰分析。现有方法要求缺失模式为单调（即测量随机后标志物的参与者必测量基线标志物），但实际中如登革热疫苗试验中基线标志物仅部分可获取，违背该假设。作者基于估计似然（estimated likelihood）框架构建方法，通过EM算法处理非单调缺失下的联合分布估计。数值模拟表明新方法在偏差和效率上优于现有方法，并在两项III期登革热疫苗试验数据中展示了应用。该工作直接连接您对因果推断中识别与估计的兴趣，特别是主分层框架下处理缺失数据的实际挑战。
- **关键技术**: `estimated likelihood`, `EM algorithm`, `principal stratification`, `non-monotone missingness`, `bivariate effect modification`
- **为什么对您有用**: 本文直接对应您 primary interest 中的因果推断（主分层效应修饰）与纵向数据缺失问题，且属于流行病学应用（登革热疫苗试验）。您的武器库中 estimation theory in causal inference 和 identification theory 可直接用于理解其估计似然框架的识别假设与效率损失；缺失模式非单调性对现有方法（如单调缺失假设下的方法）的挑战，是您 moderately_familiar 的 HOIF 或 semiparametric theory 可尝试改进的方向（例如用 influence function 构造双稳健估计）。中期可做：需先在 moderately_familiar 的 semiparametric theory 上提升，以将当前基于似然的方法扩展为双稳健或 DML 版本。

### 5. [10.1093/biostatistics/kxaa044](https://doi.org/10.1093/biostatistics/kxaa044) — Bayesian design of clinical trials using joint models for longitudinal and time-to-event data
- **作者**: Jiawei Xu, Matthew A Psioda, Joseph G Ibrahim
- **期刊/来源**: Biostatistics
- **机构**: University of North Carolina at Chapel Hill
- **分类**: vol 23 · issue 2 · pp 591-608
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对临床试验中纵向数据与时间-事件终点联合建模的设计问题，提出贝叶斯框架下的样本量确定方法。采用灵活轨迹联合模型（flexible trajectory joint model），将纵向结局轨迹纳入风险模型，允许非比例风险（如风险比随时间递增）。时间-事件终点的推断基于时变风险比的均值，该均值可分解为治疗对终点的直接效应和通过纵向结局介导的间接效应。样本量确定基于贝叶斯视角定义的高功效和良好控制的I类错误率。通过乳腺癌临床试验设计示例展示方法。对您而言，该文将因果推断中的mediation分析（直接/间接效应分解）与临床试验设计结合，属于应用型因果推断工作。
- **关键技术**: `joint model for longitudinal and time-to-event`, `Bayesian sample size determination`, `mediation decomposition`, `non-proportional hazards`, `flexible trajectory model`
- **为什么对您有用**: 本文连接您的causal inference兴趣中的mediation和longitudinal方向，具体是临床试验中时间-事件终点的直接/间接效应分解。您的technical arsenal中'identification theory in causal inference'（moderately_familiar）可直接用于理解其mediation分解的识别假设；但本文是应用导向，方法学novelty有限（贝叶斯样本量公式为已知框架的扩展）。中期可做：若想在此方向深入，需先在moderately_familiar的semiparametric theory上加强，以评估其贝叶斯设计相对于频率学派DML方法的效率。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1093/biostatistics/kxaa030](https://doi.org/10.1093/biostatistics/kxaa030) — General tests of the Markov property in multi-state models
- **作者**: Andrew C Titman, Hein Putter
- **期刊/来源**: Biostatistics
- **机构**: Lancaster University · Leiden University Medical Center
- **分类**: vol 23 · issue 2 · pp 380-396
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对多状态模型中常见的 Markov 假设提出了一类通用检验方法。研究设定在事件史分析框架下，目标是对一般多状态过程检验 Markov 性，即未来转移率是否仅依赖于当前状态而非历史。作者首先考虑了两种现有方法：一是在 Cox 模型中纳入进入各状态的时间作为协变量，二是通过分层 Commenges-Andersen 检验检测共享脆弱性。核心创新在于基于 log-rank 统计量族构建新检验：将患者在初始时间 s 所处的状态分组，比较后续转移率，若 Markov 性成立则分组不应有影响。进一步推导了在给定协变量条件下 Markov 性的扩展检验形式。由于检验统计量的零分布复杂，采用 wild bootstrap 近似。模拟比较显示，Cox 基方法在多种偏离 Markov 的场景下保持良好功效，而 log-rank 基检验在非 Markov 行为不持续或不均匀时最为有效。本文对您可能有用：它直接关联您对假设检验的兴趣，且多状态模型在流行病学纵向数据中常见，可作为应用方向的方法学参考。
- **关键技术**: `log-rank test`, `wild bootstrap`, `Cox proportional hazards model`, `Commenges-Andersen test`, `multi-state model`, `Markov assumption test`
- **为什么对您有用**: 本文直接对应您 primary interest 中的假设检验，且多状态模型是流行病学纵向数据分析的核心工具。您武器库中的非参数统计和 M-估计理论可用于分析检验统计量的渐近性质，而 wild bootstrap 的数值实现可借助您统计计算的经验。中期可做：若想深入检验的局部功效或优化 bootstrap 计算，需先在 moderately_familiar 的 M-估计理论上加强。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1093/biostatistics/kxaa038](https://doi.org/10.1093/biostatistics/kxaa038) — Fast Lasso method for large-scale and ultrahigh-dimensional Cox model with applications to UK Biobank
- **作者**: Ruilin Li, Christopher Chang, Johanne M Justesen, Yosuke Tanigawa, Junyang Qian, Trevor Hastie et al.
- **期刊/来源**: Biostatistics
- **机构**: Stanford University · Grail (United States)
- **分类**: vol 23 · issue 2 · pp 522-540
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对大规模、超高维Cox比例风险模型，提出了一种基于Batch Screening Iterative Lasso (BASIL) 框架的快速Lasso求解算法。核心创新在于将变量筛选（screening）与迭代优化结合，使得算法能够处理内存无法容纳的基因型-生存时间数据。算法输出完整的Lasso路径（所有预定义正则化参数下的估计值），并通过C-index或验证偏差评估预测精度。在UK Biobank的306种疾病结局的大规模基因型-生存数据上展示了有效性。实现基于PLINK2包，开源为snpnet-Cox。该方法在计算效率上显著优于传统坐标下降法，特别适合生物银行级别的超大规模数据。对您而言，这是一篇统计计算与高维统计的实用结合，展示了如何将经典算法（Lasso）扩展到内存受限的超大规模场景，其screening+迭代的框架思路对您开发高效统计软件有直接参考价值。
- **关键技术**: `Batch Screening Iterative Lasso (BASIL)`, `Cox proportional hazard model`, `L1-regularized partial likelihood`, `screening and iterative optimization`, `concordance index (C-index)`
- **为什么对您有用**: 本文属于统计计算方向，直接连接您的primary interest中的'statistical computing (numerical methods, algorithm)'。技术武器库中'very_familiar'的'软件开发和high-dimensional asymptotics'可直接用于理解其算法设计（screening+迭代）和理论性质（Lasso路径的收敛性）。中期可做：若您想将类似screening思路推广到其他高维模型（如Cox模型与U-statistics结合），需先在'moderately_familiar'的'M-estimation theory'上加强，以处理非光滑损失函数的理论分析。

### 2. [10.1093/biostatistics/kxaa031](https://doi.org/10.1093/biostatistics/kxaa031) — A divide-and-conquer method for sparse risk prediction and evaluation
- **作者**: Chuan Hong, Yan Wang, Tianxi Cai
- **期刊/来源**: Biostatistics
- **机构**: Harvard University
- **分类**: vol 23 · issue 2 · pp 397-411
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对大规模数据下稀疏逻辑回归的拟合与预测精度推断问题，提出了一种融合筛选（screening）与一步线性化（one-step linearization）的分治（DAC）算法 SOLID。该方法先将数据分块，在各块内通过筛选减少候选变量维度，再对筛选后的协变量进行线性化近似，从而快速逼近全样本似然并完成惩罚估计。为评估预测模型的精度，作者进一步开发了修正交叉验证（MCV）方法，利用 SOLID 的副产品大幅降低计算负担，并首次在 DAC 框架下实现了对预测精度的推断（如区间估计）。模拟表明 SOLID 和 MCV 在计算速度上显著优于现有 DAC 方法，统计效率与全样本估计相当。该方法应用于 Partners HealthCare 电子病历数据，构建疾病诊断分类模型。对您而言，本文展示了如何将分治与线性化技巧结合以解决大规模数据下的计算瓶颈，其推断策略（MCV）对您在高维因果推断或统计计算中处理大规模数据时的效率问题有直接参考价值。
- **关键技术**: `divide-and-conquer`, `screening`, `one-step linearization`, `modified cross-validation`, `sparse logistic regression`, `massive data`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的 primary interest 中的 statistical computing。其 SOLID 算法中的分治与线性化策略可迁移至您在高维因果推断或 U-statistic 计算中处理大规模数据时的效率问题。您对软件开发和算法实现非常熟悉，因此可以立即动手复现或扩展其方法至其他模型（如 Cox 回归、线性 IV）。

## 流行病学  *(epidemiology, 5 篇)*

### 1. [10.1093/biostatistics/kxaa034](https://doi.org/10.1093/biostatistics/kxaa034) · [arXiv](https://arxiv.org/abs/1812.02829) — The role of body mass index at diagnosis of colorectal cancer on Black–White disparities in survival: a density regression mediation approach
- **作者**: Katrina L Devick, Linda Valeri, Jarvis Chen, Alejandro Jara, Marie-Abèle Bind, Brent A Coull
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 449-466
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文研究结直肠癌（CRC）患者中，非西班牙裔白人与黑人之间生存差异的机制，重点关注诊断时BMI作为中介变量的作用。作者提出一种新的密度回归中介分析方法，通过贝叶斯框架估计将黑人BMI分布干预为白人BMI分布后的自然直接效应和间接效应，从而量化BMI差异对种族生存差异的贡献。该方法不要求BMI分布仅发生均值平移，而是允许复杂分布形式的匹配，比传统均值移位中介分析更灵活。模拟研究表明，该方法与仅允许均值移位的方法表现相当或更优，且将BMI分类化会导致严重偏倚。应用于CanCORS数据时，发现该干预对老年和低收入黑人患者可能有益，但对年轻或高收入黑人群体可能有害。本文是流行病学中因果中介分析的应用，对您而言，其密度回归中介框架可启发在proximal CI或纵向设定中处理连续中介变量分布干预的方法学扩展。
- **关键技术**: `Bayesian density regression`, `causal mediation analysis`, `natural direct and indirect effects`, `Dirichlet process mixture`, `distributional intervention`
- **为什么对您有用**: 本文属于流行病学应用，使用因果中介分析处理种族健康差异问题，与您的secondary interest（流行病学数据集和因果推断应用）直接相关。技术上，其密度回归中介框架可视为对标准均值移位中介的推广，您武器库中的identification theory和semiparametric theory可用来评估该方法的识别假设是否可放松或转化为更高效的估计量（如DML）。作为应用论文，本文提供了真实数据集和分析流程，值得花时间阅读全文以获取流行病学中介分析的典型分析模式。

### 2. [10.1093/biostatistics/kxaa037](https://doi.org/10.1093/biostatistics/kxaa037) — Immune correlates analysis using vaccinees from test negative designs
- **作者**: Dean A Follmann, Lori Dodd
- **期刊/来源**: Biostatistics
- **机构**: National Institute of Allergy and Infectious Diseases
- **分类**: vol 23 · issue 2 · pp 507-521
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文研究在疫情暴发或罕见病场景下，如何利用 test-negative design (TND) 的疫苗接受者数据推断疫苗诱导的免疫应答与疾病风险之间的关联。传统前瞻性研究需对所有疫苗接受者测量免疫应答，成本高昂；TND 回顾性设计仅收集有症状就诊者的免疫应答，但存在感染后免疫应答可能被疾病状态污染的问题。作者提出对 TND 中的疫苗接受者同时测量针对相关病原体（如埃博拉）和无关蛋白（如载体）的免疫应答，利用后者作为前者在感染前的代理变量。方法上采用 logistic 回归，以插补的免疫应答作为协变量、病例状态为结局，并详细阐述了无偏推断所需的假设（如代理变量不受感染影响且与目标免疫应答相关）。通过模拟（包括恒定和衰减免疫应答场景）评估了方法表现，并分析了基于环状疫苗接种的埃博拉暴发模拟数据集。本文对您有用之处在于：它提供了一个流行病学中处理代理变量和缺失数据的因果推断案例，与您 causal inference 方向中的 IV 和 mediation 思路有技术交叉，且 TND 设计在疫苗有效性评估中应用广泛，值得作为应用型文献阅读。
- **关键技术**: `test-negative design`, `proxy variable`, `logistic regression with imputation`, `simulation-based evaluation`
- **为什么对您有用**: 本文属于流行病学应用，直接对应您的 secondary interest。它展示了在罕见病场景下利用代理变量进行因果推断的实用框架，与您 causal inference 方向中的 IV 和 mediation 思路有概念联系。武器库中 very_familiar 的 estimation theory in causal inference 足以理解其核心假设和估计方法，但本文是纯应用工作，无新方法学贡献，因此作为 gateway reading 了解 TND 设计即可，无需深入复现。

### 3. [10.1093/biostatistics/kxaa048](https://doi.org/10.1093/biostatistics/kxaa048) — Quantifying diagnostic accuracy improvement of new biomarkers for competing risk outcomes
- **作者**: Zheng Wang, Yu Cheng, Eric C Seaberg, James T Becker
- **期刊/来源**: Biostatistics
- **机构**: University of Pittsburgh · Johns Hopkins University
- **分类**: vol 23 · issue 2 · pp 666-682
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文针对竞争风险结局下新生物标志物诊断准确度提升的量化问题，将净重分类改善指数（NRI）和综合判别改善指数（IDI）从二分类及多分类结局扩展至竞争风险数据。通过累积发生函数量化竞争事件的累积风险，并采用逆概率加权处理独立删失导致的“缺失”类别。考虑了多种竞争风险模型，包括Fine-Gray模型、多状态模型和多项逻辑回归模型。NRI的推断基于估计量的渐近正态性，IDI则使用偏差校正加速Bootstrap。模拟表明所提推断方法表现良好，并应用于多中心艾滋病队列研究。对您而言，本文是流行病学中因果推断应用的一个实例，展示了在竞争风险设定下如何评估预测改善，其逆概率加权和累积风险建模思路可迁移至您关注的纵向因果推断中的敏感性分析问题。
- **关键技术**: `net reclassification improvement`, `integrated discrimination improvement`, `cumulative incidence function`, `inverse probability weighting`, `competing risks`, `Fine-Gray model`
- **为什么对您有用**: 本文属于流行病学应用，直接对应您的secondary interest。它展示了在竞争风险（如死亡）存在时如何评估新标志物的增量预测价值，其逆概率加权处理删失和累积风险建模的技术细节，对您从事纵向因果推断（如mediation analysis with competing events）有参考价值。武器库中'identification theory in causal inference'和'estimation theory in causal inference'足以理解其方法，但本文是应用导向，无新理论突破，属于中期可读的入门级流行病学方法论文。

### 4. [10.1093/biostatistics/kxaa047](https://doi.org/10.1093/biostatistics/kxaa047) · [arXiv](https://arxiv.org/abs/1812.05691) — Dose–response modeling in high-throughput cancer drug screenings: an end-to-end approach
- **作者**: Wesley Tansey, Kathy Li, Haoran Zhang, Scott W Linderman, Raul Rabadan, David M Blei et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 643-665
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对高通量癌症药物筛选中的剂量-反应建模问题，提出一个端到端的层次贝叶斯模型。模型将细胞系、药物及其分子特征（如基因表达、突变状态）作为协变量，通过一个深度神经网络参数化的非线性函数来刻画药物浓度-反应曲线。采用变分推断进行模型拟合，并利用条件随机化检验（CRT）来发现与药物反应相关的分子标志物。在真实数据案例中，模型成功捕捉到已知生物学关联（如TP53野生型与MDM2过表达共同预测对Nutlin-3(a)的敏感性），并在预测性能上比标准生物学方法（如四参数逻辑斯蒂模型）降低约20%的预测误差。该方法为药物基因组学中的关联发现提供了一个统计严谨的框架，其层次建模和条件随机化检验的思路对流行病学中高维暴露-反应研究具有参考价值。
- **关键技术**: `hierarchical Bayesian model`, `deep neural network`, `variational inference`, `conditional randomization test`, `dose-response curve`
- **为什么对您有用**: 本文属于流行病学应用（药物筛选），其层次贝叶斯模型和条件随机化检验（CRT）是处理高维协变量下暴露-反应关系的通用工具。研究者武器库中的非参数统计和因果推断估计理论可用于分析该模型的识别性和估计效率，而高维渐近工具可用于理解CRT在大量分子特征下的检验功效。本文作为流行病学应用论文，数据和分析流程清晰，适合作为入门读物，但核心方法学创新有限（主要贡献在应用层面），武器库足以支撑研究者理解并可能迁移其建模思路。

### 5. [10.1093/biostatistics/kxaa028](https://doi.org/10.1093/biostatistics/kxaa028) · [arXiv](https://arxiv.org/abs/1904.00412) — Surrogate-guided sampling designs for classification of rare outcomes from electronic medical records data
- **作者**: W Katherine Tan, Patrick J Heagerty
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 345-361
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对电子病历中罕见临床结局的分类问题，提出了一种基于替代变量（surrogate）分层的富集抽样设计。在资源受限（人工标注成本高）的设定下，目标是通过有策略地选择标注样本，提升分类模型的判别能力。方法核心是：利用与真实结局高度相关的辅助变量（如影像报告中的关键词）对未标注样本进行分层，然后按层不等概率抽样进行人工标注。作者给出了抽样设计如何影响预测模型性能（如AUC、校准度）的数学推导，并通过模拟验证了分层富集抽样相比简单随机抽样在相同标注成本下能显著提升模型判别力。最后，在腰椎影像报告数据（LIRE研究）上展示了该方法用于自然语言处理模型训练的实际效果。对您而言，这是一篇流行病学领域的应用方法论文，其核心思想——利用辅助变量优化标注成本与模型性能的权衡——与您在高维统计和因果推断中处理代理变量（proxies）或负对照（negative controls）的思路有潜在联系，可作为了解流行病学中实际数据收集策略的入门读物。
- **关键技术**: `enrichment sampling`, `stratified sampling`, `surrogate variables`, `outcome misclassification`, `natural language processing`
- **为什么对您有用**: 本文属于流行病学领域的应用方法论文，可作为gateway reading：它清晰阐述了在罕见结局下如何利用辅助变量（surrogate）设计高效抽样策略，数据结构和模型假设（如替代变量与真实结局的相关性）都交代得比较清楚，适合作为流行病学数据收集问题的入门。您的武器库中'非参数统计'和'因果推断中的估计理论'可以用于分析其抽样策略的偏差-方差权衡，但核心机器（如最优抽样比、成本函数建模）不在您当前非常熟悉的工具中，属于'暂不可做'——需要先补充survey sampling或active learning的相关理论。不过，本文值得花时间读全文，因为它提供了一个具体的流行病学应用场景，有助于您理解该领域的数据生成机制和实际约束。

## 其他  *(other, 5 篇)*

### 1. [10.1093/biostatistics/kxaa043](https://doi.org/10.1093/biostatistics/kxaa043) — Integrative functional linear model for genome-wide association studies with multiple traits
- **作者**: Yang Li, Fan Wang, Mengyun Wu, Shuangge Ma
- **期刊/来源**: Biostatistics
- **机构**: Renmin University of China · Shanghai University of Finance and Economics · Yale University
- **分类**: vol 23 · issue 2 · pp 574-590
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对全基因组关联研究（GWAS）中多个相关表型同时分析的问题，提出了一种整合性函数线性模型。该模型首次将单核苷酸多态性（SNP）数据近似为函数型对象，并采用惩罚技术（如LASSO或SCAD）进行变量选择，以处理SNP的高维性和多表型间的相关性。通过信息借用机制，模型能够同时识别与多个表型相关的遗传变异。模拟研究表明，与四种现有方法相比，该方法在识别和估计疾病相关遗传变异方面表现更优。对2型糖尿病数据的分析产生了生物学上有意义的发现，并具有良好的预测准确性和选择稳定性。该方法属于应用统计遗传学范畴，其核心贡献在于将函数型数据分析与惩罚回归结合用于GWAS，而非提出新的统计推断理论。
- **关键技术**: `functional linear model`, `penalized regression`, `genome-wide association studies`, `multi-trait analysis`, `variable selection`
- **为什么对您有用**: 本文属于流行病学/遗传学应用，与您的secondary interest（流行病学数据集和应用因果工作）相关。它展示了如何利用函数型数据表示和惩罚回归处理高维SNP数据，但方法学新颖性有限（主要是现有技术的组合应用）。从武器库角度看，您熟悉的非参数统计和高维渐近理论可用于理解其函数型建模的合理性，但本文不涉及因果推断或效率理论，因此暂不可做——核心机器（统计遗传学中的具体模型和惩罚方法）不在您的武器库中，不值得花时间精读全文。

### 2. [10.1093/biostatistics/kxaa041](https://doi.org/10.1093/biostatistics/kxaa041) — Bayesian analysis of longitudinal and multidimensional functional data
- **作者**: John Shamshoian, Damla Şentürk, Shafali Jeste, Donatello Telesca
- **期刊/来源**: Biostatistics
- **机构**: University of California, Los Angeles · Neurobehavioral Systems
- **分类**: vol 23 · issue 2 · pp 558-573
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文研究纵向功能数据（longitudinal functional data）的贝叶斯非参数建模，目标是在低维可解释特征提取的同时完成平滑、条件均值估计和协方差曲面估计。方法基于自适应分块Gibbs采样（adaptive blocked Gibbs sampling）从后验分布中抽取蒙特卡洛样本，计算效率较高。模拟实验评估了模型的操作特性，并在两个案例中应用：各国年龄别生育率随时间的变化，以及自闭症谱系障碍儿童的隐式学习实验。该方法学贡献在于将非参数贝叶斯框架系统性地适配到纵向功能数据场景，但未涉及因果推断、高维统计或效率理论等您的主要兴趣方向。对您而言，本文属于应用统计方法论文，与您的主要研究方向（因果推断、高维统计、U-统计量等）无直接关联。
- **关键技术**: `Bayesian nonparametrics`, `adaptive blocked Gibbs sampling`, `functional data analysis`, `longitudinal functional data`, `covariance surface estimation`
- **为什么对您有用**: 本文属于功能数据分析的应用方法论文，与您的主要兴趣（因果推断、高维统计、U-统计量、效率理论）无直接关联。武器库中的非参数统计和M估计理论虽可泛泛理解其方法，但缺乏具体可攻口子。暂不可做——核心机器（贝叶斯非参数、功能数据建模）不在武器库中，且无统计-计算权衡或U-统计量连接。

### 3. [10.1093/biostatistics/kxaa035](https://doi.org/10.1093/biostatistics/kxaa035) — Bayesian sparse heritability analysis with high-dimensional neuroimaging phenotypes
- **作者**: Yize Zhao, Tengfei Li, Hongtu Zhu
- **期刊/来源**: Biostatistics
- **机构**: Yale University · University of North Carolina at Chapel Hill
- **分类**: vol 23 · issue 2 · pp 467-484
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出一种贝叶斯稀疏遗传力分析方法，用于联合估计高维神经影像表型的遗传力。模型通过分层选择（基于脑结构网络和体素依赖）对区域和局部测量施加稀疏性，并利用非参数狄利克雷过程混合模型对SNP相关的表型变异进行分组，以增强生物学可解释性。模拟表明该方法在遗传力估计和可遗传性状选择上优于现有方法。应用于ADNI和UK Biobank两个大规模影像遗传学数据集，得到有生物学意义的结果。该方法属于应用统计遗传学方向，与您的主要兴趣（因果推断、高维统计、半参理论）无直接方法学关联，但展示了贝叶斯非参数在高维生物医学数据中的应用模式。
- **关键技术**: `Bayesian hierarchical model`, `Dirichlet process mixture`, `sparsity-inducing prior`, `heritability estimation`, `neuroimaging genetics`
- **为什么对您有用**: 本文属于应用统计遗传学，与您的主要兴趣方向（因果推断、高维RMT、半参效率理论）无直接方法学重叠。作为流行病学/遗传学应用，它展示了贝叶斯非参数在高维表型遗传力估计中的实践，但方法学新颖性有限（主要是现有贝叶斯工具的整合应用）。武器库中very_familiar的非参统计和high-dimensional asymptotics可帮助理解其模型设定，但核心机器（贝叶斯分层模型、DP混合）不在您的技术栈中，属于暂不可做方向。

### 4. [10.1093/biostatistics/kxaa046](https://doi.org/10.1093/biostatistics/kxaa046) — Principal curve approaches for inferring 3D chromatin architecture
- **作者**: Elena Tuzhilina, Trevor J Hastie, Mark R Segal
- **期刊/来源**: Biostatistics
- **机构**: University of California, San Francisco · Stanford University
- **分类**: vol 23 · issue 2 · pp 626-642
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对Hi-C染色质构象捕获数据，提出一种基于主曲线（principal curve）的三维基因组结构推断方法。传统方法通常将染色体建模为3D空间中的点云，再通过约束条件强制连续性，计算成本高且依赖细胞类型。作者将问题转化为度量缩放（metric scaling）框架，并引入主曲线方法直接拟合一条1D曲线，从而自然满足染色体的连续结构。该方法通过一个平滑度/自由度参数生成一系列候选解，并提出了模型选择策略。在IMR90细胞Hi-C数据上的应用表明，该方法能有效重建3D结构，且与正交成像数据对比验证了准确性。对您而言，本文属于生物统计应用，与您的主要兴趣方向（因果推断、高维统计等）无直接技术关联，但展示了统计方法（主曲线）在基因组学中的创新应用。
- **关键技术**: `principal curve`, `metric scaling`, `Hi-C data`, `3D genome reconstruction`, `smoothness parameter selection`
- **为什么对您有用**: 本文属于生物统计应用，与您的主要兴趣方向（因果推断、高维统计、半参理论等）无直接技术关联。作为gateway reading，本文对统计学家友好，清晰解释了Hi-C数据结构和重建问题，但核心方法（主曲线）并非您武器库中的常用工具。暂不可做：缺乏基因组学领域知识和Hi-C数据处理经验。

### 5. [10.1093/biostatistics/kxaa036](https://doi.org/10.1093/biostatistics/kxaa036) — Interim recruitment prediction for multi-center clinical trials
- **作者**: Szymon Urbas, Chris Sherlock, Paul Metcalfe
- **期刊/来源**: Biostatistics
- **机构**: Lancaster University · AstraZeneca (United Kingdom)
- **分类**: vol 23 · issue 2 · pp 485-506
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对多中心临床试验的招募预测问题，提出了一套通用框架，用于监测、建模和预测患者入组过程。研究动机是现有时间齐次招募模型产生的预测区间过于乐观且狭窄。首先，作者提出了两种检验招募率衰减的统计检验方法，并进行了功效分析。然后，引入了一个基于非齐次泊松过程的模型，其强度函数单调衰减，这一设定受肿瘤学试验中观察到的招募趋势启发。模型形式通用，可适配任意参数化曲线形状。作者还提供了一种构建合理参数先验的通用方法，并使用贝叶斯模型平均进行预测，以同时考虑参数和模型的不确定性。通过模拟数据集验证了方法的有效性和对模型误设的稳健性。最后，将新方法应用于肿瘤学试验数据，进行中期入组预测，并与现有方法比较，指出了入组模式发生意外变化的情况。
- **关键技术**: `inhomogeneous Poisson process`, `Bayesian model averaging`, `power study`, `parametric curve fitting`, `prior construction`
- **为什么对您有用**: 本文属于临床试验统计方法学，与您的流行病学（应用）次级兴趣相关，提供了一种处理入组率衰减的实用建模框架。您武器库中的非参数统计和M估计理论可用于分析其模型假设的稳健性，但核心方法（贝叶斯模型平均、泊松过程）与您的主要兴趣方向（因果推断、高维统计）交集有限。本文可作为流行病学应用领域的入门阅读，了解临床试验中一个具体的预测问题，但方法学新颖性一般，属于应用型工作。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

