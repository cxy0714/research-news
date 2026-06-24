# Epidemiology — Vol 36  Issue 4  ·  2026-06-24

- 共 19 篇 · Epidemiology
- 目录核对 ⚠️ 疑似漏 2 篇（对照 OpenAlex 24 篇）：10.1097/ede.0000000000001849、10.1097/ede.0000000000001851

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期内容主要围绕因果推断的方法论细节与应用挑战展开，形成了三条鲜明的主线：一是因果识别与推广中的结构性偏倚校正，涉及试验参与效应、选择偏倚、碰撞偏倚及缺失数据处理；二是纵向与重复测量数据的分析策略，聚焦时间尺度选择、交叉拟合稳定性及方差估计效率；三是经典流行病学设计的实证应用，涵盖政策评估、环境暴露与生存分析。此外，还有两篇侧重于半参数效率理论与高维预测工具的基础性文章。

在因果识别与推广主线中，多篇论文针对特定偏倚机制提出识别策略或量化其影响。*Generalizing and Transporting Causal Inferences* 与 *Revisiting the Population Attributable Fraction* 均关注因果效应的可迁移性，前者引入“试验参与效应”修正了随机试验结果的推广框架，后者利用逆概率加权实现了PAF从样本到目标总体的估计。*The Same but Different?* 与 *Liacine Bouaoun* 则分别通过系统综述和模拟实验，辨析了碰撞偏倚与选择偏倚的等价性争议、以及回忆偏倚与选择偏倚对剂量反应关系的联合影响。*Handling Multivariable Missing Data* 则具体考察了中介分析中多变量缺失机制对干预效应估计的影响，比较了多种插补策略的偏差表现。

纵向数据分析方法讨论中，交叉拟合的稳定性与时间尺度的选择成为焦点。关于机器学习因果推断中随机种子敏感性的争论（*Re: Don’t Let Your Analysis Go to Seed* 与 *The Authors Respond*）揭示了交叉拟合折数选择中的偏差-方差权衡：一方指出增加折数可消除种子波动，另一方则警示这会以方差膨胀为代价。*Approaches to Timescale Choice* 与 *Time and Age as Longitudinal Timescales* 深入讨论了认知老化研究中的时间尺度设定，指出“年龄”与“随访时间”尺度隐含不同的参数约束，错误选择将导致暴露效应估计偏倚。*Modeling Time-varying Dispersion* 则展示了通过辅助参数（离散度）的时变建模来提高时间序列回归的主效应估计精度。

对于关注因果推断与半参数理论的研究者，建议优先阅读 *Generalizing and Transporting Causal Inferences*（试验参与效应识别）、*Five Facts About Influence Functions*（影响函数与半参数效率入门）以及关于交叉拟合稳定性辩论的往来信件，这些文章直接触及了当前因果推断方法研究的前沿痛点与基础理论。

## 因果推断  *(causal_inference, 4 篇)*

### 1. [10.1097/ede.0000000000001863](https://doi.org/10.1097/ede.0000000000001863) · [arXiv](https://arxiv.org/abs/2407.14703) — Generalizing and Transporting Causal Inferences from Randomized Trials in the Presence of Trial Engagement Effects
- **作者**: Lawson Ung, Tyler J. VanderWeele, Issa J. Dahabreh
- **期刊/来源**: Epidemiology
- **分类**: vol 36 · issue 4 · pp 500-510
- 相关性 9/10 · novelty: `weaker_assumption`
- **摘要**: 该文针对随机试验结果向目标总体推广（generalizing/transporting）时常见的“试验参与效应”（trial engagement effects）问题，即被试因参与试验本身（而非所接受的干预）而对结局产生的影响。定义了考虑该效应下的新的因果估计量（如目标总体常规治疗下的平均处理效应）。在“试验参与与处理分配无绝对尺度或相对尺度交互作用”的假设下，证明了即使存在试验参与效应，仍可利用试验数据与目标总体协变量数据识别目标整体平均处理效应。关键的识别公式与先前无试验参与效应假设下采用的观察数据泛函完全相同，因此该结果为已有估计量提供了新的解释。对您可能有用：该工作属于流行病学领域的应用因果推断，直接涉及transportability与generalizability这一子方向，且其无交互作用假设的放松思路或许可迁移至您关注的proximal causal inference中的negative control设定。
- **关键技术**: `generalizability and transportability`, `trial engagement effects`, `no-interaction assumptions`, `identification via covariate adjustment`, `inverse probability weighting`
- **为什么对您有用**: 该文直接对应您在“流行病学（应用，数据集，因果推断）”上的兴趣，具体是RCT结果外推的方法论改进。您熟悉的非参数统计与因果推断估计理论（very_familiar中的“estimation theory in causal inference”）可直接用于理解其识别公式与估计量（如IPW或g-formula）。无交互作用假设的引入为后续实证应用提供了更宽松的假设，中期可做：若想将类似思路推广至更复杂设定（如纵向或Proximal CI），需在“identification theory in causal inference”（moderately_familiar）上进一步积累。

### 2. [10.1097/ede.0000000000001866](https://doi.org/10.1097/ede.0000000000001866) · [arXiv](https://arxiv.org/abs/2403.17396) — Handling Multivariable Missing Data in Causal Mediation Analysis Estimating Interventional Effects
- **作者**: S. Ghazaleh Dashti, Katherine J. Lee, Julie A. Simpson, John B. Carlin, Margarita Moreno-Betancur
- **期刊/来源**: Epidemiology
- **分类**: vol 36 · issue 4 · pp 487-499
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文聚焦于因果中介分析中估计干预效应（interventional effects）时的多变量缺失数据处理问题。通过基于维多利亚青少年健康队列研究的模拟，比较了完全病例分析、六种基于完全条件规范的多重插补方法以及一种“实质模型兼容”多重插补方法的性能。模拟涵盖了七种缺失机制，重点关注中间混杂变量、中介变量和结果变量对缺失的影响。结果显示，当缺失机制不涉及中间混杂、中介和结果时，所有较好的多重插补方法近似无偏；而当自身影响缺失时偏差最大。方差估计方面，BootMI（先Bootstrap后多重插补）的偏差小于MIBoot（先多重插补后Bootstrap）。本文为流行病学中的中介分析提供了实用的缺失数据处理指南，与您的因果推断中介分析兴趣及流行病学应用直接相关。
- **关键技术**: `multiple imputation`, `fully conditional specification`, `interventional effects`, `g-computation`, `MIBoot`, `BootMI`
- **为什么对您有用**: 本文直接关联您primary interest中的因果中介分析（mediation）方向，特别是干预效应的估计与缺失数据处理。您非常熟悉的因果推断估计理论和非参数统计可用于评估仿真设计中的估计性质；您的软件开发技能可复现或扩展其仿真框架。该工作提供的方法选择指南属于立即可做的范畴，可通过现有武器库直接切入。

### 3. [10.1097/ede.0000000000001860](https://doi.org/10.1097/ede.0000000000001860) — Re: Don’t Let Your Analysis Go to Seed: On the Impact of Random Seed on Machine Learning-based Causal Inference
- **作者**: Nicholas T. Williams, Anton Hung, Kara E. Rudolph
- **期刊/来源**: Epidemiology
- **机构**: Meredith College · Columbia University
- **分类**: vol 36 · issue 4 · pp e12-e13
- 相关性 5/10 · novelty: `application`
- **摘要**: 这篇Letter回应了Schader等人关于机器学习因果推断估计量随机种子依赖性的警告。作者指出，Schader等人的模拟仅使用2折交叉拟合，可能夸大了问题。基于相同的高维数据生成机制（n=100, 200个数据集），他们重复估计ATE 100次（不同种子），使用广义线性模型、多元自适应回归样条和随机森林的集成方法。比较2折与40折交叉拟合：2折时中位数内估计方差（×10^4）为0.398，而40折时为0.00813，降幅约98%。结论是简单地增加交叉拟合折数到适合数据集维度的水平，即可有效消除随机种子波动，无需多次运行平均。该结果表明交叉拟合折数的选择对估计稳定性至关重要，且实践中应更关注此参数而非依赖多轮平均。对您而言，这一结果直接关联因果推断中机器学习估计量的实际稳定性问题，且可通过现有因果推断软件（如您熟悉的软件开发能力）快速验证和应用于流行病学队列研究。
- **关键技术**: `cross-fitting`, `random seed dependence`, `ensemble of GLM/MARS/random forest`, `high-dimensional simulation`, `within-dataset estimate variance`
- **为什么对您有用**: 1) 直接联系流行病学中因果推断的应用，特别是机器学习估计量（如DML）在真实数据中的稳定性问题。2) 您的武器库中'causal inference estimation theory'和'software development'可直接用于复现和扩展（例如在其他DML方法中检验折数影响）。3) 立即可做：用您熟悉的R或Python因果推断包（如causalml、EconML）在不同折数下运行模拟，无需额外武器。

### 4. [10.1097/ede.0000000000001861](https://doi.org/10.1097/ede.0000000000001861) — The Authors Respond
- **作者**: Lindsey Schader, David Benkeser, Allison Codi
- **期刊/来源**: Epidemiology
- **机构**: Emory University · Orano (United States)
- **分类**: vol 36 · issue 4 · pp e13-e14
- 相关性 1/10 · novelty: `minor`
- **摘要**: 本文是对Williams等人建议的回应，该建议主张通过增加交叉拟合（cross-fitting）的折叠数来降低随机种子引起的变异性。作者在平均处理效应的模拟中重新检验了这一策略，发现随着折叠数从2倍增加到40倍，估计量的方差单调上升（从0.00049增至0.00118），增幅约2.4倍，而偏差变化很小。由于该模拟中方差远小于偏差，均方误差在各折叠数下大致相同，因此增加折叠数并未改善整体性能。作者指出交叉拟合存在偏差-方差权衡，单纯为降低随机种子敏感性而增加折叠数可能并非最优做法。他们建议分析人员应常规探索随机种子敏感性，特别是在小样本中，若发现明显变异性则可考虑对多个种子结果直接取平均作为一种快速无关策略。本文不提出新方法，而是对已有实践建议的实证检验与审慎提醒，对应用DML或交叉拟合的因果推断工作者具有直接的实践参考价值。
- **关键技术**: `cross-fitting`, `bias-variance tradeoff`, `random seed sensitivity`, `augmented inverse probability weighting`
- **为什么对您有用**: 该文直接涉及因果推断中交叉拟合（cross-fitting）核心实践问题——折叠数选择带来的偏差-方差权衡，属于DML/AIPW估计器实际应用中的关键细节。研究者当前对估计理论（very_familiar）和半参数理论（moderately_familiar）的掌握足以理解该模拟结果并判断其对自身田野应用的影响。参考价值：立即可做的是在其自身的因果推断模拟或数据分析中引入多折叠数敏感性分析作为标准诊断步骤，中期可关注是否需结合具体数据稀疏程度发展自适应折叠数选择准则（需进一步熟悉HOIF理论中交叉拟合的方差解析）。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1097/ede.0000000000001858](https://doi.org/10.1097/ede.0000000000001858) — Five Facts About Influence Functions
- **作者**: Stephen R. Cole, Alexander Breskin, Bonnie E. Shook-Sa, Paul N. Zivich, Michael G. Hudgens, Jessie K. Edwards
- **期刊/来源**: Epidemiology
- **机构**: Regeneron (United States)
- **分类**: vol 36 · issue 4 · pp 467-472
- 相关性 9/10 · novelty: `survey`
- **摘要**: 本文是一篇面向流行病学读者的 influence function 入门教程，设定为经典 semiparametric 框架，目标是解释 IF 在估计量构造与方差估计中的作用。核心机制包括：IF 定义为估计量在数据分布扰动下的 Gateaux 导数，用于刻画单个观测对估计量的影响；IF 可用于构造稳健方差估计，并提供 OLS、GEE、IPW 等方法的统一视角；IF 是推导 AIPW 和 TMLE 等双重稳健估计量的关键工具。文章通过两个简单例子（均值估计、线性回归系数）演示 IF 的计算与解释。对您有用：本文可作为 influence function 与 semiparametric efficiency 理论的入门读物，适合补充您在 efficiency theory 方面的技术储备。
- **关键技术**: `influence function`, `semiparametric efficiency`, `robust variance estimation`, `augmented inverse probability weighting`, `targeted maximum likelihood estimation`
- **为什么对您有用**: 本文直接连接到您 primary interest 中的 efficiency theory（semiparametric efficiency bounds, debiased ML），提供了 influence function 这一核心工具的直观入门。您在 `moderately_familiar` 中的 semiparametric theory 和 HOIF 都以 IF 为基础，本文可作为快速补齐概念缺口的 gateway reading。属于 gateway-reading 范畴：(1) 本文是很好的入门读物，解释清晰、不假设高深背景；(2) 武器库完全足够支撑阅读；(3) 建议快速浏览，若您已熟悉 IF 基本概念可跳过正文直接看例子。

## 流行病学  *(epidemiology, 14 篇)*

### 1. [10.1097/ede.0000000000001867](https://doi.org/10.1097/ede.0000000000001867) — Revisiting the Population Attributable Fraction
- **作者**: Mark Klose, Paul N. Zivich, Stephen R. Cole
- **期刊/来源**: Epidemiology
- **机构**: University of North Carolina at Chapel Hill · University of North Carolina Health Care · Department of Health
- **分类**: vol 36 · issue 4 · pp 482-486
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文研究 Population Attributable Fraction (PAF) 在样本与目标总体不一致时的识别与估计问题，核心设定是将研究样本的因果效应 transport 到目标总体。作者采用 inverse probability of treatment weighting (IPTW) 和 inverse odds of sampling weighting (IOSW) 实现风险估计的可迁移性，并使用非参数 bootstrap 和 M-estimation 的 sandwich variance estimator 进行方差估计。实证分析使用 Women's Interagency HIV Study (n=1164) 的数据，估计 2008 年美国 HIV 诊断女性 (n=11282) 中注射吸毒史对 AIDS 或死亡风险的 PAF，发现样本内估计 0.21 经 transport 后降至 0.13。本文是流行病学应用论文，方法学 novelty 有限，但清晰展示了 identification 条件和 transport 方法在 PAF 场景的应用。
- **关键技术**: `inverse probability of treatment weighting`, `inverse odds of sampling weighting`, `M-estimation`, `sandwich variance estimator`, `transportability`, `identification conditions`
- **为什么对您有用**: 本文连接到 epidemiology secondary interest，展示了因果推断中 transportability 和 identification 的实际应用场景。研究者熟悉的 identification theory in causal inference 和 semiparametric theory 足以完全理解本文方法，属于立即可读的 gateway reading。若研究者对流行病学数据集和 PAF 这一经典指标的应用场景感兴趣，本文提供了清晰的入门案例；但若寻求方法学创新或新的理论结果，本文价值有限。

### 2. [10.1097/ede.0000000000001854](https://doi.org/10.1097/ede.0000000000001854) — Quantifying the Health Burden of COVID-19 Using Individual Estimates of Years of Life Lost Based on Population-wide Administrative Level Data
- **作者**: Elena Milkovska, Bram Wouterse, Jawa Issa, Pieter van Baal
- **期刊/来源**: Epidemiology
- **机构**: Erasmus University Rotterdam
- **分类**: vol 36 · issue 4 · pp 520-530
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文基于荷兰50岁以上全人口（n≈610万）的管理数据，估计COVID-19死者个体水平的反事实预期寿命，计算寿命损失年（YLL）并考察其分布。研究使用Cox-LASSO和Cox-Elastic Net对大量潜在预测变量进行高维变量选择，建立生存模型预测个体预期寿命。利用预测值，按年龄和收入生成YLL分布，发现COVID-19死者的平均反事实预期寿命比一般人群低约28%，但存在显著异质性：20%死者的预期寿命超过年龄别群体均值。最富和最穷死者的平均YLL损失接近且离散程度相似。这一流行病学应用展示了高维变量选择与生存模型结合在真实大规模管理数据分析中的实际流程，其数据链接和反事实推理思路对您关注的流行病学应用与因果推断（反事实寿命损失）有参考价值。
- **关键技术**: `Cox-LASSO`, `Cox-Elastic Net`, `years of life lost (YLL)`, `counterfactual life expectancy`, `survival models`, `administrative data linkage`
- **为什么对您有用**: 本文属于您二级兴趣中的流行病学应用方向，使用了反事实寿命损失框架（与因果推断中的反事实概念相通）和高维变量选择方法。您对高维统计（very_familiar）和估计理论（very_familiar）非常熟悉，因此能轻松理解其Cox-LASSO基础；本文提供了一个大规模管理数据（610万人）进行流行病学分析的完整案例，涉及变量选择与生存预测的结合，可作为您未来进入流行病学数据分析的入门阅读。目前核心武器库缺更高级的因果识别方法（如IV、DML），但本文作为应用型工作可立即可读，无需额外学习。

### 3. [10.1097/ede.0000000000001865](https://doi.org/10.1097/ede.0000000000001865) — State-level Payday Loan Bans and Preterm Births in the US, 2000–2019
- **作者**: Samantha Gailey, Tim Bruckner, Rania Badran, Parvati Singh
- **期刊/来源**: Epidemiology
- **机构**: Department of Forestry · Michigan State University · University of California, Irvine · Department of Health · The Ohio State University
- **分类**: vol 36 · issue 4 · pp 541-550
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文利用2000–2019年美国10个州及哥伦比亚特区在发薪日贷款禁令实施上的时序变化，评估该政策对早产率的影响。研究方法采用交错差分法（staggered difference-in-differences），并纳入通过时间序列分析得到的州特异性早产时间倾向性作为控制变量。结果显示，禁令实施后的前3年内，每100例活产中的早产数下降约0.22（95% CI: -0.31, -0.13），相当于减少4512例预期外的早产。该结果支持发薪日贷款限制有助于降低早产率的假设。论文提供了一个清晰的因果识别策略，并讨论了政策冲击的异质性和潜在平行趋势假设。对于流行病学领域的政策评估研究，本文的分析框架和公开数据（CDC WONDER）可复现，对您而言，其交错DiD设计结合时间序列调整是验证因果推断假设的一个具体应用场景。
- **关键技术**: `staggered difference-in-differences`, `time-series propensity adjustment`, `preterm birth rate`, `parallel trends assumption`, `CDC WONDER database`
- **为什么对您有用**: （1）本文属于流行病学应用，直接对应您的secondary interest中的流行病学方向，且使用因果推断中的交错DiD设计，与您primary interest中的因果识别方法连接；（2）您可使用very_familiar的估计理论（尤其是平行趋势检验和标准误修正）来评估该文估计量的稳健性，或改进其时间序列倾向性调整的规范；（3）立即可做：核心方法（DiD+时间序列控制）是您武器库中非常熟悉的工具，无需额外学习即可直接审读或复现。

### 4. [10.1097/ede.0000000000001864](https://doi.org/10.1097/ede.0000000000001864) — The Same but Different?: A Systematic Review of the Impact of Selection and Collider Bias on Internal Validity
- **作者**: Natalie S. Levy, Katrina L. Kezios
- **期刊/来源**: Epidemiology
- **机构**: Aetion (United States) · Columbia University
- **分类**: vol 36 · issue 4 · pp 473-481
- 相关性 6/10 · novelty: `survey`
- **摘要**: 本文是一篇系统性综述，旨在比较选择偏倚与碰撞偏倚对内部效度的影响。作者系统检索了2000年至2024年间的同行评审方法论文章和流行病学教材，最终纳入33篇文章和12本教材。综述发现，尽管当前理论认为碰撞偏倚与选择偏倚在威胁内部效度上等价，但文献中对两者后果的结论存在分歧：碰撞偏倚被认为影响微小，而选择偏倚的效果可变。进一步分析发现，多数碰撞偏倚文献是在sharp null假设（暴露与结局无关联）下评估偏倚，且对交互作用（乘性vs.加性）的讨论与选择偏倚文献不同。作者建议未来研究应在非sharp null假设下考察碰撞偏倚，并同时考虑乘性和加性交互作用，以更好地预测和量化其对内部效度的影响。对于您而言，本文梳理了碰撞偏倚研究中的一个重要缺口——sharp null假设的普遍性，这直接关联到您因果推断中的敏感性分析兴趣，也属于流行病学应用方向的有价值入门读物。
- **关键技术**: `selection bias`, `collider bias`, `sharp null assumption`, `multiplicative interaction`, `additive interaction`
- **为什么对您有用**: 本文直接针对流行病学中的核心偏倚问题，属于您的secondary interest（流行病学应用）。它指出碰撞偏倚通常在sharp null假设下评估，这一定论可能过于局限，对您主要兴趣中的因果推断敏感性分析有启发：开发不依赖sharp null的碰撞偏倚敏感性方法是一个自然延伸。技术上，您武器库中'identification theory in causal inference'（moderately_familiar）可用来思考试验设计，但需要先熟悉碰撞偏倚的识别假设（如单调性、交互作用形式）才能动手改进——属于中期可做：需先在identification theory上加强。

### 5. [10.1097/ede.0000000000001857](https://doi.org/10.1097/ede.0000000000001857) — Alcohol Policy in Adolescence and Subsequent Alcohol-attributable Hospitalizations and Mortality at Ages 21−54 Years: A Register-based Cohort Study
- **作者**: Juha Luukkonen, Elina Einiö, Lasse Tarkiainen, Pekka Martikainen, Hanna Remes
- **期刊/来源**: Epidemiology
- **机构**: University of Helsinki
- **分类**: vol 36 · issue 4 · pp 580-589
- 相关性 5/10 · novelty: `application`
- **摘要**: 本研究利用芬兰1975—1977年实施的酒精广告禁令与税收上调作为自然实验，评估青春期暴露于严格酒精政策的年龄段对21—54岁酒精归因住院与死亡率的影响。采用芬兰注册数据库，覆盖1950—1964年出生队列（117.5万个体），以18岁（法定饮酒年龄）为参照组，计算各出生队列的时依风险比。结果显示，政策实施时年龄越小（如13岁或17岁），其后酒精归因住院风险越低（男性HR分别为0.85与0.91），且结果对外因死亡率一致，对女性方向相似但更不精确。该发现支持了青春期严格酒精政策可降低成年期酒精相关危害的假设。本文作为流行病学领域真实数据应用，展示了利用政策断点进行因果推断的经典队列设计，其识别策略与数据构造流程对研究者理解流行病学中自然实验的应用具有参考价值。
- **关键技术**: `register-based cohort study`, `natural experiment`, `Cox proportional hazards model`, `cohort-wise hazard ratio`, `alcohol-attributable hospitalization and mortality`
- **为什么对您有用**: 本文属于流行病学应用，直接匹配研究者的次要兴趣。它提供了一个清晰的流行病学因果推断入门案例：利用政策时间变化构造暴露分组，使用Cox模型估计风险比，数据源为芬兰全国注册数据库。研究者可借此熟悉流行病学常用分析框架（队列设计、率比估计），其因果识别策略（假定政策前后其他因素稳定）可与primary interest中的identification theory对照。武器库中'causal inference identification theory'足以支撑理解设计假设，但若要深入扩展流行病学专用方法（如竞争风险、多状态模型），则需要在'moderately_familiar'的semiparametric theory基础上进一步学习。总体而言，本文值得作为流行病学领域的gateway阅读，但无需deep read。

### 6. [10.1097/ede.0000000000001856](https://doi.org/10.1097/ede.0000000000001856) — Modeling Time-varying Dispersion to Improve Estimation of the Short-term Health Effect of Environmental Exposure in a Time-series Design
- **作者**: Danlu Zhang, Stefanie T. Ebelt, Noah C. Scovronick, Howard H. Chang
- **期刊/来源**: Epidemiology
- **机构**: Emory University
- **分类**: vol 36 · issue 4 · pp 450-457
- 相关性 5/10 · novelty: `application`
- **摘要**: 在时间序列计数数据中估计环境暴露对健康的短期效应时，标准做法假设离散参数恒定。该研究采用双广义线性模型（DGLM）框架，联合建模Poisson log-线性均值和离散参数，允许离散度随日历日期和气象等协变量时变。利用亚特兰大1999-2009年急诊就诊数据和日均臭氧浓度，发现离散度明显依赖日期和气象条件。与恒定离散模型相比，时变离散模型估计的相对风险（RR）从1.037降至1.029，但标准误减小26%，精度显著提高。模拟研究证实，若忽略时变离散，恒定离散假设会膨胀标准误。文章提供完整R代码，便于复现。作为流行病学应用，该工作展示了通过灵活建模辅助参数提升主效应估计精度的实践路径，值得一读。
- **关键技术**: `double generalized linear models`, `time-varying dispersion`, `Poisson log-linear model`, `covariate-dependent dispersion`, `overdispersion modeling`, `time-series count data`
- **为什么对您有用**: 本文作为流行病学入门读物质量高，写作清晰、DGLM框架解释充分，统计学家无需领域背景即可抓住核心；您已有的统计计算和GLM技能足以理解并复现其分析流程，武器库足够支撑您进入此应用方向；论文展示了时变离散建模对提高估计精度的实际价值并提供可复现代码，值得通读全文。

### 7. [10.1097/ede.0000000000001852](https://doi.org/10.1097/ede.0000000000001852) — Right Censoring and Mortality in the Multicenter AIDS Cohort Study and Women’s Interagency HIV Study
- **作者**: Jessie K. Edwards, Tiffany L. Breger, Stephen R. Cole, Paul N. Zivich, Bonnie E. Shook-Sa, Leah M. Sadinski et al.
- **期刊/来源**: Epidemiology
- **机构**: University of North Carolina at Chapel Hill · Emory University · Georgetown University · Johns Hopkins University · Johns Hopkins Medicine · University of Mississippi Medical Center · Northwestern University · Los Angeles LGBT Center 等
- **分类**: vol 36 · issue 4 · pp 511-519
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究队列研究中因参与者失访导致右删失对死亡率估计的偏倚问题，设定为 MACS 和 WIHS 两个 HIV 队列，关键假设是删失机制可能依赖于未观测的健康状态。核心方法是比较"金标准分析"（利用死亡登记数据获取全样本死亡率）与常规删失分析的结果差异，并应用 inverse probability of censoring weights (IPCW) 进行偏倚校正。实证结果显示，删失导致死亡率估计偏低 0-5%，IPCW 能部分校正这种衰减。本文属于应用方法学论文，展示了 IPCW 在真实队列数据中的实际效果，对您理解流行病学研究中缺失数据处理实践有参考价值。
- ⚠️ *摘要不完整，待重跑（`python -m research_news.rerun`）*
- **关键技术**: `inverse probability of censoring weights (IPCW)`, `right censoring`, `missing data mechanism`, `cohort study design`, `sensitivity to dropout`
- **为什么对您有用**: (1) 连接到流行病学队列研究的因果推断应用，具体是缺失数据/删失机制对估计量的影响评估。(2) IPCW 是您 very_familiar 的 estimation theory in causal inference 中的标准工具，可评估其文中 IPCW 实现是否正确使用了 stabilized weights、是否考虑了 time-varying confounding 等细节。(3) **立即可做**：用您熟悉的 semiparametric efficiency 理论可分析其 IPCW estimator 的效率性质，或考虑是否可用 TMLE 进一步改进。

### 8. [10.1097/ede.0000000000001853](https://doi.org/10.1097/ede.0000000000001853) — The Impact of Power Outages on Cardiovascular Hospitalizations Among Medicare Fee-for-service Enrollees in New York State, 2017–2018
- **作者**: Vivian Do, Heather Kathleen McBrien, Donald Edmondson, Marianthi-Anna Kioumourtzoglou, Joan Allison Casey
- **期刊/来源**: Epidemiology
- **机构**: Public Health Department · Columbia University · University of Washington
- **分类**: vol 36 · issue 4 · pp 458-466
- 相关性 5/10 · novelty: `application`
- **摘要**: 本研究利用2017-2018年纽约州245,452名Medicare受益人的数据，采用病例交叉设计（case-crossover design）评估停电对心血管疾病住院的影响。关键在于利用自身对照消除不随时间变化的混杂因素，并通过条件逻辑回归估计停电小时数与住院风险的率比。分析按城市性（纽约市、非纽约市城市、农村）和冷暖季分层，并考虑了年龄、性别和社区社会经济因素。主要结果几乎均为零关联（如纽约市停电后1天的率比1.05，95% CI 0.85-1.30），但暴露病例数量有限导致统计功效低，结论需谨慎解释。该研究展示了病例交叉设计在大规模行政数据中应用的实际挑战，包括暴露测量和功效不足问题。对您有用：它直接连接您流行病学应用兴趣，且案例可为您的因果推断课程提供实例，同时其数据分析流程（大数据清洗、分层回归、敏感度分析）也与您的统计计算兴趣相关。
- **关键技术**: `case-crossover design`, `conditional logistic regression`, `stratified analysis`, `Medicare claims data`, `power outage exposure measurement`
- **为什么对您有用**: 本文属于流行病学应用，采用病例交叉设计（自身对照）控制时间固定混杂，是环境流行病学因果推断的典型方法。您可以用非常熟悉的「estimation theory in causal inference」审视其条件逻辑回归的识别假设和效应估计性质（如偏差来源、功效分析）。此外，作为大规模行政数据的分析案例，它适合作为流行病学方向的入门读物，帮您熟悉真实数据分析的流程与陷阱，读完可快速判断是否值得深入复现或改进（立即可做）。

### 9. [10.1097/ede.0000000000001862](https://doi.org/10.1097/ede.0000000000001862) — Health Predictors of Neighborhood Selection: A Prospective Cohort Study of Residential Mobility in Ontario, Canada
- **作者**: Emmalin Buajitti, Laura C. Rosella
- **期刊/来源**: Epidemiology
- **机构**: University of Toronto · Public Health Ontario · McGill University · Trillium Health Centre
- **分类**: vol 36 · issue 4 · pp 440-449
- 相关性 5/10 · novelty: `application`
- **摘要**: 本研究聚焦健康对居住流动性的选择效应，即健康状况不佳的人群是否更倾向于搬入低收入社区，从而产生可能被误归因于邻里效应的社会经济梯度。采用加拿大安大略省2005至2014年间加拿大社区健康调查与人口行政数据的关联数据（n=93,235），以自评健康和多重慢性病作为基线健康指标，将居住流动结果分为六个类别（包括从不迁移和各类迁移），并拟合多项逻辑回归模型，调整了调查周期、年龄、性别、家庭收入、移民身份和居住不稳定性等协变量。结果显示，与自评健康很好/极好者相比，基线健康差/一般者从低收入社区迁至低收入社区、从高收入社区迁至低收入社区、从低收入社区迁至高收入社区以及不搬离低收入社区的优势比均显著升高，客观健康指标（≥4种慢性病 vs. ≤1种）结果一致。该研究利用大规模人口数据揭示了健康与居住流动之间的强关联，但其设计本质上是描述性/关联性分析，未使用因果推断方法（如工具变量或敏感性分析）控制未观测混杂。对于习惯因果推断框架的统计学者而言，本文可作为流行病学中“健康选择”问题的入门实证读物，其分析思路和公开可用的数据链接为深化方向（如探讨健康选择对邻里效应估计的偏倚大小）提供了基础。
- **关键技术**: `multinomial logistic regression`, `population-based cohort`, `self-reported health`, `multimorbidity`, `residential mobility categories`, `administrative data linkage`
- **为什么对您有用**: (1) 作为流行病学应用，本文以清晰的方法论呈现健康-邻里选择的实证分析，适合入门级阅读，无需天文学或复杂统计背景；(2) 研究者武器库中的因果推断工具（如 inverse probability weighting、instrumental variables）可直接用于诊断或纠正本文结论中可能存在的混杂偏倚，或扩展为更严谨的因果识别设计；(3) 该论文提供了真实的大型队列数据及其分析模式，对于想了解健康选择如何影响邻里效应估计的统计学者，值得花时间全文阅读，尤其可用于检验研究者自身在因果推断敏感性分析方面的方法。

### 10. [10.1097/ede.0000000000001868](https://doi.org/10.1097/ede.0000000000001868) — Effects of Prenatal Exposure to PM2.5 Chemical Components on Adverse Birth Outcomes and Under-5 Mortality in South Korea
- **作者**: Garam Byun, Yongsoo Choi, Jong-Tae Lee, Michelle L. Bell
- **期刊/来源**: Epidemiology
- **机构**: Yale University · Korea Institute of Drug Safety and Risk Management · Korea University
- **分类**: vol 36 · issue 4 · pp 531-540
- 相关性 4/10 · novelty: `application`
- **摘要**: 该研究基于韩国四个大城市的行政数据库，链接2013-2015年出生记录与5岁以下死亡记录，共324,566例出生，分析了孕期PM2.5及其10种化学成分暴露对早产、低出生体重、小于胎龄儿和5岁以下死亡率的影响。暴露变量采用各孕期及整个孕期的平均浓度，以逻辑回归估计优势比，仅调整了基础协变量（如母亲年龄、产次等），未采用倾向性评分或工具变量等因果推断方法。结果发现整个孕期PM2.5每增加一个四分位距(8.7 μg/m³)与早产风险升高17%相关（OR=1.17, 95%CI 1.11-1.23），而低出生体重、小于胎龄儿和死亡率未见显著关联。元素碳和二次无机气溶胶的效应估计高于其他成分。作为一篇流行病学应用论文，其优势在于大规模人群数据和多成分暴露刻画，但方法学上仅停留在传统回归关联分析，未处理未测量混杂或暴露测量误差。对您而言，这篇论文提供了一个真实数据场景：若使用工具变量（如风向）或负对照方法来识别PM2.5成分的因果效应，可极大提升证据质量，属于流行病学领域可供方法学改进的典型案例。
- **关键技术**: `logistic regression`, `fine particulate matter components`, `administrative birth-cohort data linkage`, `trimester-specific exposure assessment`, `meta-analysis of component-specific effects`
- **为什么对您有用**: 本文属于secondary interest中的流行病学应用，使用了大型行政链接数据（32万出生队列），暴露变量细分为10种PM2.5成分，分析模式对您接触真实数据集并思考因果识别方法有参考价值。尽管本文仅用传统回归，但暴露成分效应的异质性结果可启发您使用IV或负对照方法在类似数据上做更严格的因果推断（您熟悉causal inference估计理论）。技术武器库中'非常熟悉'的因果推断估计理论可以立即用于重新分析这类问题，例如设计基于监测站距离的工具变量或采用双稳健估计。总体而言，该文是应用参照物，值得快速浏览其数据结构和暴露赋值策略，但不需要深读方法细节。

### 11. [10.1097/ede.0000000000001855](https://doi.org/10.1097/ede.0000000000001855) — Nicotine–Cannabis Transitions and Nicotine Abstinence Among United States Adults
- **作者**: Dae-Hee Han, Adam M. Leventhal, Andrew C. Stokes, Janet E. Audrain-McGovern, Sandrah P. Eckel, Jessica Liu et al.
- **期刊/来源**: Epidemiology
- **机构**: University of Southern California · Boston University · University of Pennsylvania · Stanford University
- **分类**: vol 36 · issue 4 · pp 551-559
- 相关性 4/10 · novelty: `application`
- **摘要**: 本研究基于美国人口评估烟草与健康研究（PATH）六轮数据（2013-2021），探讨尼古丁使用向大麻使用的转换与一年后尼古丁戒断的关联。将基线时仅使用尼古丁的成年人按t+1时的四类暴露状态分组：仅大麻使用、尼古丁-大麻共使用、两者均不使用、继续仅尼古丁使用，调整混杂后比较t+2时的戒断率。采用log-binomial回归估计调整相对风险（aRR），发现共使用组戒断率显著低于继续仅尼古丁组（aRR=0.68），而转至仅大麻组戒断率显著更高（aRR=4.66），且与两者均不使用组戒断率相近。结论提示烟草戒断干预需区别对待不同大麻使用模式。该文是典型的流行病学纵向数据分析，其暴露分类策略和回归调整流程可供因果推断方法研究者评估识别假设。
- **关键技术**: `multinomial exposure classification`, `log-binomial regression`, `longitudinal cohort analysis`, `adjusted relative risk`, `Population Assessment of Tobacco and Health (PATH) dataset`
- **为什么对您有用**: 本文属于流行病学应用因果推断，直接连接您secondary interest中的流行病学实数据。其暴露转换定义和混杂调整方法可作为检验identification假设的实例——您的identification理论（moderately_familiar）可用于判断其调整集是否满足无混淆、非信息删失等假设。作为gateway reading，本文清晰呈现了PATH数据结构和分析范式，值得花时间了解这一公共健康数据集，但核心方法较常规，您若要在该数据上做更严谨的因果推断（如工具变量或proximal causal inference），需先在moderately_familiar的identification理论上深入学习。因此暂不可做直接复现改进，但可作中期可做的背景阅读。

### 12. [10.1097/ede.0000000000001859](https://doi.org/10.1097/ede.0000000000001859) — Approaches to Timescale Choice in Cognitive Aging Research and Potential Implications for Estimated Exposure Effects: Coordinated Analyses in 10 Cohorts of Older Adults
- **作者**: Eleanor Hayes-Larson, Ryan M. Andrews, Katrina L. Kezios, Ariane Bercu, Anaïs Rouanet, Catherine Helmer et al.
- **期刊/来源**: Epidemiology
- **机构**: University of Southern California · UCLA Health · Boston University · Columbia University · Université de Bordeaux · Inserm · Bordeaux Population Health · University of Washington 等
- **分类**: vol 36 · issue 4 · pp 560-571
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文关注认知老化研究中时间尺度选择（time on study vs. current age）对暴露效应估计的影响。研究采用协调分析方法，在10个老年队列中评估APOE ε4基因型（时间恒定暴露）和基线糖尿病状态（可能时变暴露）对记忆变化的影响。使用线性与非线性时间规格的混合效应模型，分别以time on study和current age为时间尺度估计暴露效应。结果发现APOE ε4效应估计在不同时间尺度下基本一致，但糖尿病效应在某些队列中方向相反，表明current age尺度可能因糖尿病测量年龄异质性而产生偏倚。研究展示了多队列协调分析中评估替代时间尺度的策略，并强调了时间尺度选择对估计结果的潜在影响。本研究为流行病学中老化与认知研究的暴露效应估计提供了实践指导，尤其适用于纵向因果推理中暴露时间变异性的敏感性分析。
- **关键技术**: `coordinated analysis across cohorts`, `mixed-effects models with linear/nonlinear time specifications`, `two timescale comparison (time on study vs. current age)`, `time-varying vs. time-invariant exposure handling`, `multi-cohort sensitivity analysis for timescale choice`
- **为什么对您有用**: 本文与您的secondary interest of epidemiology（应用因果工作）直接相关，核心问题——时间尺度选择对纵向暴露效应估计的影响——是流行病学中因果推断的设计敏感性议题。您的技术武器库中的estimation theory in causal inference（very_familiar）可用于审视不同时间尺度下混合效应模型估计的偏差来源，而identification theory（moderately_familiar）有助于理解暴露时变性与时间尺度选择的识别条件。这是一篇应用导向的论文，方法上不涉及新理论，但协调分析的设计和发现可作为您进入流行病学老化和认知方向的门径——值得精读以了解纵向队列数据的分析陷阱。

### 13. [10.1097/ede.0000000000001869](https://doi.org/10.1097/ede.0000000000001869) — Time and Age as Longitudinal Timescales: Multiple Useful Models are Illuminating
- **作者**: Michael E. Griswold, M. Maria Glymour
- **期刊/来源**: Epidemiology
- **机构**: University of Mississippi Medical Center
- **分类**: vol 36 · issue 4 · pp 572-579
- 相关性 3/10 · novelty: `survey`
- **摘要**: 本文评论纵向分析中“时间”与“年龄”作为时间尺度的选择争议，目标是通过偏差-方差权衡框架澄清两者关系。作者基于Hayes-Larson等人的多队列实证研究，指出“年龄”时间尺度隐含假设年龄0系数与时间系数相等，可能引入偏差；而“年龄0+时间”模型更为灵活，可分别估计个体内和个体间效应。通过三个队列的合并数据（约8万观测值），图示比较Age0、Time、Age三种模型下的认知衰退轨迹，发现Age模型因合并个体内与个体间信息而提高精度（标准误缩小21%），但若两效应不同则产生偏差。文章还扩展至非线性模型和随机效应，强调应同时考察两种时间尺度并诊断差异来源。对流行病学纵向因果推断中暴露效应估计的时间尺度选择具有直接指导意义，尤其适用于研究者关注的队列研究与因果推断设定。
- **关键技术**: `bias-variance tradeoff`, `mixed effects model`, `longitudinal timescales`, `within-person vs between-person contrasts`
- **为什么对您有用**: 本文直接连接研究者的次要兴趣——流行病学中的纵向数据分析和因果推断，具体涉及暴露对认知衰退效应的估计中时间尺度选择导致的偏差-方差权衡。研究者武器库中的“estimation theory in causal inference”可以立即用于形式化本文提到的系数等同假设检验，并评估其在因果框架下的敏感性。该问题立即可做，因为非参数统计和因果推断中的标准工具（如分层、逆概率加权）足以复现和扩展本文的对比分析。

### 14. [10.1097/ede.0000000000001870](https://doi.org/10.1097/ede.0000000000001870) — Liacine Bouaoun, Winner of the 2025 Rothman Prize
- **作者**: 
- **期刊/来源**: Epidemiology
- **分类**: vol 36 · issue 4 · pp 439-439
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文是一项案例对照模拟研究，旨在探讨手机使用与脑胶质瘤之间的J形关系是否可由回忆偏倚和选择偏倚的组合解释。研究基于Interphone Study数据，发现中度使用者的相对风险降低，而重度使用者（前10%）风险增加约40%的结果，可能完全由两类偏倚所致。本文通过蒙特卡洛模拟定量评估偏倚方向与幅度，并未使用复杂因果推断方法，而是直接对暴露误分类和选择过程建模。结论削弱了重度手机使用者患脑胶质瘤风险增加的因果证据。对于流行病学因果推断实践，本文展示了如何在观察性研究中使用模拟作为敏感性分析的工具，但方法学贡献有限，主要是应用性演示。作为获奖论文，其清晰度和对公共健康话题的重要性受到认可。
- **关键技术**: `simulation study`, `differential exposure misclassification`, `selection bias`, `case-control design`
- **为什么对您有用**: 该论文属于流行病学应用（secondary interest），展示模拟方法在评估观察性偏倚中的作用。武器库中的因果识别理论（偏倚方向分析）可用于理解其模拟设置，但本文不涉及新统计方法或效率理论，属于可理解但无直接技术延伸的阅读。立即可做：用现有非参数和因果推断知识即可读懂其偏倚逻辑。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

