# Biometrics — Vol 80  Issue 1  ·  2026-06-24

- 共 43 篇 · Biometrics
- 目录核对 ⚠️ 疑似漏 12 篇（对照 OpenAlex 60 篇）：10.1093/biomtc/ujad020、10.1093/biomtc/ujad015、10.1093/biomtc/ujad009、10.1093/biomtc/ujae007、10.1093/biomtc/ujad003 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

Biometrics Vol 80 Issue 1 围绕因果识别与推断、半参数效率与稳健估计、高维与结构化建模、非参数回归与变量选择四条主线展开。因果方向集中在工具变量中介分析、主分层分析、DAG 学习与动态治疗策略，多篇推进非参数识别和贝叶斯/半参数估计；半参数效率方向聚焦于自适应协变量调整、一步估计应用于大规模 Cox 模型、以及两阶段抽样设计中的 AIPW 与残差依赖抽样；高维方法涵盖随机矩阵理论驱动的降秩回归、vine copula 回归、贝叶斯因子分析与网络引导先验，以及多重检验中 FDP 的渐近不确定性；非参数/半参数主线涉及纵向变系数单指数模型、稀疏不规则数据预测、混合面板计数数据的变量选择等。

因果推断主线进展最为密集：使用工具变量的因果中介分析提出 double complier 效应并通过 influence function 一步估计实现双稳健性与半参效率；主分层分析在时间-事件结局下处理非依从性，采用贝叶斯 Weibull-Cox 模型与 Stan 实现；从 GWAS 汇总统计推断表型 DAG 的方法利用工具变量与高斯结构方程模型，支持边显著性检验；动态治疗策略方向同时出现多目标树增强学习（MOT-RL，结合标量化增广 IPW 与后向归纳）与 SMART‑EXAM 设计（动态随机化概率提升参与者福利），均涉及反事实均值的半参数估计。半参数效率方面，自适应选择最优调整策略（TMLE + V‑fold CV，基于影响曲线平方损失）在随机试验中实现精度提升，Cox 比例风险模型的一步估计（有效得分函数 + 子集 MLE）将半参效率思想落地到百万级数据，两阶段设计中的 AIPW 估计方程同时处理 left truncation 与竞争风险，与残差依赖抽样（RDS）共同展示了效率理论在流行病学设计中的系统应用。高维与结构化建模中，multiple augmented reduced rank regression (maRRR) 以随机矩阵理论核范数联合多数据集分解，high‑dimensional sparse vine copula 回归处理高维非线性依赖，而图信息贝叶斯因子分析通过自适应收缩先验整合生物学网络，均为高维变量选择与结构发现提供了新工具。

对因果推断方向最相关的论文包括：工具变量中介分析、主分层分析、GWAS 汇总统计 DAG、多目标树增强动态治疗策略、SMART‑EXAM 设计、ITR 表征（高斯过程代理模型）。对半参数效率方向最相关的论文包括：自适应策略选择、Cox 一步估计、AIPW 两阶段设计（left‑truncated competing risks）、残余依赖抽样设计。对高维统计方向最相关的论文包括：maRRR、vine copula 回归、图信息贝叶斯因子分析、高维惩罚 GLMM（因子模型降维）。

## 因果推断  *(causal_inference, 10 篇)*

### 1. [10.1093/biomtc/ujad037](https://doi.org/10.1093/biomtc/ujad037) — Using instrumental variables to address unmeasured confounding in causal mediation analysis
- **作者**: Kara E Rudolph, Nicholas Williams, Iván Díaz
- **期刊/来源**: Biometrics
- **机构**: Columbia University · New York University
- **分类**: vol 80 · issue 1
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在因果中介分析框架下，研究存在未观测混杂时的间接效应识别问题，设定需要两个（可能相关的）工具变量分别作用于暴露和中介。提出 novel estimands——double complier interventional direct and indirect effects——在两个 IV 存在时实现非参数识别。估计方法采用 influence function-based one-step estimator，具有 double robustness 和 semiparametric efficiency 性质。理论贡献在于将 IV 方法从 total effect 推广到 mediation setting，解决了 exposure-mediator-confounder 三重混杂的识别难题。实证部分应用于住房券实验数据。对您在 mediation 和 IV 交叉方向的研究有直接参考价值。
- **关键技术**: `instrumental variables`, `causal mediation analysis`, `interventional effects`, `influence function`, `double robustness`, `semiparametric efficiency`
- **为什么对您有用**: 直接连接到您 primary interest 中的 mediation 和 IV 两个子方向，且涉及 semiparametric efficiency theory。您 very_familiar 的 estimation theory in causal inference 和 moderately_familiar 的 identification theory / semiparametric theory 正好可以用来审视其 identification strategy 的完备性和 estimator 的效率性质。立即可做：用您熟悉的 semiparametric efficiency bound 工具验证其 estimator 是否达到效率下界，或探索 single IV 情形下的 identification possibility。

### 2. [10.1093/biomtc/ujad026](https://doi.org/10.1093/biomtc/ujad026) — Bayesian nonparametric for causal inference and missing data by Michael J. Daniels, Antonio Linero, and Jason Roy, CRC Press, 2023 ISBN-13: 978-0367341008, https://www.routledge.com/Bayesian-Nonparametrics-for-Causal-Inference-and-Missing-Data/Daniels-Linero-Roy/p/book/9780367341008
- **作者**: Li-Pang Chen
- **期刊/来源**: Biometrics
- **机构**: National Chengchi University
- **分类**: vol 80 · issue 1
- 相关性 8/10 · novelty: `survey`
- **摘要**: 本文是对《Bayesian Nonparametrics for Causal Inference and Missing Data》一书的书评。该书由Michael J. Daniels, Antonio Linero和Jason Roy合著，2023年由CRC Press出版，共15章，分为三个主题。主题一（第1-4章）概述因果推断基础（因果效应、g-formula、倾向得分、边际结构模型、因果中介）、缺失数据机制（MCAR/MAR/MNAR，可忽略与不可忽略缺失，选择模型、模式混合模型、共享参数模型）以及贝叶斯方法（先验、后验、MCMC、Gibbs采样、Hamiltonian Monte Carlo等）和可识别性问题。主题二（第5-10章）聚焦贝叶斯非参数方法，包括Dirichlet过程混合模型、高斯过程、贝叶斯可加回归树（BART）和贝叶斯因果森林等，应用于因果估计和缺失数据插补。主题三（第11-15章）展示实际案例研究。该书以频率学派为主的因果推断文献中填补了贝叶斯视角的空白，特别强调贝叶斯非参数方法的灵活性及其在处理复杂缺失模式和因果推断中的优势。对于研究者而言，本书可作为系统学习贝叶斯非参数因果推断方法的入门参考，尤其适合已有非参数统计和因果推断基础但希望拓展贝叶斯工具的学者。
- **关键技术**: `Bayesian nonparametrics`, `Dirichlet process mixture models`, `Gaussian processes`, `Bayesian additive regression trees (BART)`, `propensity score methods`, `g-formula`
- **为什么对您有用**: 本文直接关联您的主要兴趣方向——因果推断的识别与估计，特别提供了贝叶斯非参数视角（如BART、高斯过程）的综述，与您熟悉的非参数统计和因果推断理论形成互补。您现有的非参数统计和因果推断工具（如M-estimation、识别理论）可以用于理解书中贝叶斯方法的频率学性质；本书适合作为gateway reading，帮助您从频率学派转向贝叶斯非参数因果推断，中期可在“非参数统计”武器基础上拓展贝叶斯计算能力（如MCMC）。这是一本值得花时间阅读全文的书评，以决定是否购入原书。

### 3. [10.1093/biomtc/ujad016](https://doi.org/10.1093/biomtc/ujad016) — Principal stratification analysis of noncompliance with time-to-event outcomes
- **作者**: Bo Liu, Lisa Wruck, Fan Li
- **期刊/来源**: Biometrics
- **机构**: Duke University · Clinical Research Institute
- **分类**: vol 80 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文关注临床试验中时间-事件结局下的治疗非依从性（非依从性）导致的因果推断问题，在principal stratification框架下定义了两个因果估计量（如处理组平均因果效应等）。作者给出了非参数识别条件，并采用潜变量混合模型进行估计，具体使用贝叶斯参数Weibull-Cox比例风险模型对潜层结局建模。通过Stan编程语言实现自动后验抽样，并推导了因果估计量关于模型参数的解析形式（若无解析解则提供数值方法）。该方法应用于ADAPTABLE试验，评估81mg与325mg阿司匹林对主要不良心血管事件风险的因果效应，并开发了R包PStrata。对于您而言，本文是principal stratification在时间-事件结局上的直接应用，其识别策略和贝叶斯估计框架可迁移到您的因果推断工作中。
- **关键技术**: `principal stratification`, `noncompliance`, `time-to-event outcomes`, `Bayesian Weibull-Cox model`, `latent mixture model`, `Stan`
- **为什么对您有用**: 本文直接切入您primary interests中的因果推断子方向——principal stratification在非依从性下的识别与估计，且处理了时间-事件结局这一常见但文献中缺乏实用方法的场景。您的technical_arsenal中identification theory in causal inference（moderately_familiar）恰好可用来评估其非参数识别条件是否严密；若您希望扩展至更灵活的semiparametric估计或引入cross-fitting，则需先补足semiparametric theory（moderately_familiar）——因此该论文属于中期可做：先用其R包复现结果，再探索改进为semiparametric版本。

### 4. [10.1093/biomtc/ujae014](https://doi.org/10.1093/biomtc/ujae014) — Bias correction models for electronic health records data in the presence of non-random sampling
- **作者**: Jiyu Kim, Rebecca Anthopolos, Judy Zhong
- **期刊/来源**: Biometrics
- **机构**: New York University
- **分类**: vol 80 · issue 1
- 相关性 7/10 · novelty: `application`
- **摘要**: 电子健康记录(EHR)数据常因非随机纳入而产生选择偏差，导致关联估计和结果均值有偏。本文提出一类Heckman型偏差校正方法，通过纳入多重社会健康决定因素（如人口学、社会经济地位、医疗转诊模式）作为选择协变量，对EHR非随机抽样概率进行建模。方法采用两阶段估计：第一阶段用Probit模型估计选择概率，第二阶段将逆米尔斯比率作为校正项纳入结果回归。数值模拟在多种偏差机制下验证了校正效果；纽约市EHR网络数据中，用于估计心血管疾病患病率及其与风险因素的关联。该工作将Heckman校正框架系统引入EHR环境，为观察性健康数据中的选择偏差提供了实用工具。与您关注的因果推断中的识别问题及流行病学应用直接相关，Heckman模型方法与您熟悉的非参数统计和逆问题技术有方法论衔接，可进一步探讨非参数Heckman扩展或结合交叉拟合的稳健估计。
- **关键技术**: `Heckman selection model`, `Non-random sampling`, `Bias correction`, `Inverse Mills ratio`, `Social determinants of health`, `Selection bias`
- **为什么对您有用**: 本文针对EHR数据选择偏差问题提出Heckman型校正方法，属于因果推断中样本选择模型的直接应用，与您的因果推断兴趣（identification, sensitivity analysis）高度相关。您武器库中的非参数统计和逆问题方法可以用于分析该方法的非参数化扩展，例如放松参数分布假设。核心方法（Heckman两阶段）和识别假设对您而言属于very_familiar领域，因此可以立即评估其识别条件及有限样本表现，并考虑引入交叉拟合或更高阶影响函数提升稳健性。

### 5. [10.1093/biomtc/ujad039](https://doi.org/10.1093/biomtc/ujad039) — Inferring a directed acyclic graph of phenotypes from GWAS summary statistics
- **作者**: Rachel Zilinskas, Chunlin Li, Xiaotong Shen, Wei Pan, Tianzhong Yang
- **期刊/来源**: Biometrics
- **机构**: Iowa State University · University of Minnesota
- **分类**: vol 80 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究如何从GWAS汇总统计量推断表型间的有向无环图（DAG）。假设表型服从高斯线性结构方程模型，利用遗传变异作为工具变量，方法仅需GWAS汇总统计量和外部基因型参考面板即可实现DAG的估计。核心步骤包括：通过工具变量识别有向边，估计结构方程参数；并基于汇总统计量构造有向边的似然比检验。与现有方法不同，该方法不依赖个体-level数据，且支持边显著性的统计推断。作者将方法应用于29个心血管相关蛋白的因果网络估计，并发现该网络与阿尔茨海默病存在关联。模拟研究验证了方法的有效性。对您有用：本文直接连接因果推断中的工具变量和DAG学习，且是流行病学实际应用，您可用熟悉的因果推断估计理论分析其识别和估计性质。
- **关键技术**: `Instrumental variables (genetic variants)`, `Gaussian linear structural equation model`, `Directed acyclic graph (DAG) estimation`, `Likelihood ratio test for directed edges`, `GWAS summary statistics`
- **为什么对您有用**: 本文连接您的两个主要子方向：因果推断中的工具变量（IV）和DAG结构学习，以及流行病学应用（心血管蛋白与阿尔茨海默病）。具体而言，您非常熟悉的estimation theory in causal inference可直接用于分析该方法的IV估计偏差和渐近性质；同时，您中等熟悉的identification theory in causal inference可用于评估遗传变异作为IV的有效性假设和DAG的因果充分性。此为中期可做的follow-up——立即可用estimation theory分析估计表现，但全面理解识别基础需先在identification理论上巩固。该文提供了可直接操作的R包sumdag，适合作为实证分析的起点。

### 6. [10.1093/biomtc/ujad017](https://doi.org/10.1093/biomtc/ujad017) — Multiobjective tree-based reinforcement learning for estimating tolerant dynamic treatment regimes
- **作者**: Yao Song, Lu Wang
- **期刊/来源**: Biometrics
- **机构**: University of Michigan
- **分类**: vol 80 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文在动态治疗策略（DTR）框架下，提出“容忍治疗策略”（tDTR）概念，允许决策者在预设容忍度内接受多个可行决策规则，以权衡多目标冲突。方法上，开发了多目标树增强学习（MOT-RL），在每一阶段通过半参数回归建模反事实均值，并利用标量化的增广逆概率加权估计量（SAIPWE）构造节点纯度度量，构建无监督决策树。算法采用后向归纳递推，输出一组帕累托最优的决策规则，兼顾多个疗效指标。应用部分分析了MD Anderson癌症中心的前列腺癌两阶段化疗数据，同时降低肿瘤负荷并延长生存。该方法将树的可解释性与多目标优化结合，计算效率高，适合实际临床决策支持。对您而言，这篇论文在因果推断的动态治疗子方向提供了可操作的树方法框架，半参数回归和AIPW估计均与您的武器库直接匹配，可进一步推导该估计量的效率界或扩展至连续治疗情形。
- **关键技术**: `Tree-based reinforcement learning`, `Augmented inverse probability weighted estimator (AIPW)`, `Scalarized augmented inverse probability weighted estimator (SAIPWE)`, `Semiparametric regression (counterfactual mean modeling)`, `Multiobjective optimization`, `Dynamic treatment regime (DTR)`
- **为什么对您有用**: 本文聚焦因果推断中的动态治疗策略（DTR）子方向，结合多目标优化与树方法，直接可接入您熟悉的非参数/半参数估计和IPW估计工具。由于您对因果推断估计理论非常熟悉，且具备软件开发能力，该框架下的效率界推导或扩展到连续治疗场景属于“立即可做”的工作——只需在现有AIPW和半参回归基础上做理论延伸。

### 7. [10.1093/biomtc/ujad004](https://doi.org/10.1093/biomtc/ujad004) · [arXiv](https://arxiv.org/abs/2210.16255) — Incorporating participants’ welfare into sequential multiple assignment randomized trials
- **作者**: Xinru Wang, Nina Deliu, Yusuke Narita, Bibhas Chakraborty
- **期刊/来源**: Biometrics
- **机构**: Duke-NUS Medical School · University of Cambridge · MRC Biostatistics Unit · Sapienza University of Rome · Yale University · National University of Singapore · Duke University
- **分类**: vol 80 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 这篇论文关注动态治疗策略（DTR）的序贯多分配随机试验（SMART）设计，核心问题是如何在试验过程中提升参与者福利。传统的SMART使用固定随机化概率分配治疗，可能导致较多参与者接受经验上较差或患者不喜的治疗，从而引发伦理问题和招募、保留困难。作者提出SMART-EXAM框架，将参与者偏好和基于历史数据的个体化预测治疗效果纳入随机化概率的调整中，以此提高参与者整体福利。该设计通过“市场实验”思想，使随机化概率随累积数据动态变化，同时保持对最优DTR的统计识别能力。模拟结果表明，在参数适当设定下，SMART-EXAM能在不显著降低构建最优DTR能力的前提下改善参与者福利。最后，作者利用ADHD儿童SMART数据展示该设计的实际应用潜力。对您而言，该论文将因果推断中的序贯治疗分配与实验设计伦理问题结合，与您主要兴趣中的因果推断（特别是时序/动态干预）直接相关，同时其方法学也可迁移至流行病学领域的临床试验设计。
- **关键技术**: `Experiment-as-Market framework`, `adaptive randomization`, `sequential multiple assignment randomized trial`, `dynamic treatment regimes`, `participant welfare optimization`
- **为什么对您有用**: （1）该论文直接涉及因果推断中的序贯治疗策略（DTR）设计，属于您主要兴趣中因果推断的纵向/动态干预子方向；同时流行病学（临床试验）是您的次级兴趣。（2）您的技术武器库中“因果推断的估计理论”（very_familiar）可用于分析这种自适应随机化设计下DTR估计的无偏性/方差，而“因果推断的识别理论”（moderately_familiar）则对理解福利优化是否扭曲识别至关重要。（3）**中期可做**：您需要先在“因果推断的识别理论”上补充对非平稳随机化偏差的理论理解，方可针对SMART-EXAM设计推导出正确的IPW或AIPW估计量并分析其效率。

### 8. [10.1093/biomtc/ujad012](https://doi.org/10.1093/biomtc/ujad012) — Individualized treatment rule characterization via a value function surrogate
- **作者**: Nikki L B Freeman, Sydney E Browder, Katharine L McGinigle, Michael R Kosorok
- **期刊/来源**: Biometrics
- **机构**: University of North Carolina at Chapel Hill
- **分类**: vol 80 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对外周动脉疾病患者伤口管理的部分依从性临床背景，研究个体化治疗规则（ITR）的优化与表征。核心目标是学习最优ITR，即根据患者特征给出能使期望临床结局最大化的治疗决策规则。方法上，采用高斯过程（GP）代理模型对值函数进行非参数建模，并利用贝叶斯优化（BO）在规则空间内高效搜索全局最优解，避免了直接估计高维值函数的计算负担。进一步，作者扩展了传统ITR学习任务，提出对ITR类别进行描述性表征（characterization），将统计最优规则转化为临床可操作的决策框架。通过模拟和真实数据实例，验证了该方法在有限样本下的可行性与稳健性。对您而言，本文展示了非参数代理模型与贝叶斯优化在因果推断政策学习问题中的实用结合，直接连接您对因果推断（ITR学习）和非参数统计的兴趣，可作为实证参考。
- **关键技术**: `Gaussian process surrogate`, `Bayesian optimization`, `value function`, `individualized treatment rule`, `characterization of rule classes`
- **为什么对您有用**: 本文直接对应您primary interest中的因果推断子方向——个体化治疗规则（ITR）学习，属于政策学习范畴。所用高斯过程代理是非参数统计（您very_familiar）的典型工具，值函数估计框架则依赖因果推断中的估计理论（您very_familiar），因此您可以立即可用现有武器库理解并复现其核心逻辑。后续可进一步探索用higher-order U-statistics改进值函数估计的效率，或用HOIF框架推导ITR表征的渐近性质。

### 9. [10.1093/biomtc/ujad028](https://doi.org/10.1093/biomtc/ujad028) · [arXiv](https://arxiv.org/abs/2101.09304) — The central role of the identifying assumption in population size estimation
- **作者**: Serge Aleshin-Guendel, Mauricio Sadinle, Jon Wakefield
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对多系统估计（capture-recapture）中的人口规模估计问题，将其视为缺失数据问题，核心是需要一个不可检验的识别假设来从观测数据估计未观测个体数。作者指出，不同识别假设即使得到相同的观测数据拟合，也可能产生任意不同的总体规模估计，因此明确识别假设至关重要。现有方法常隐含假设而不显式声明，难以将观测数据模型与识别假设分离。本文提出一个重新框架，通过解耦观测数据模型与识别假设，允许在给定观测数据模型下灵活选择识别假设，并利用现有软件（如R包）进行多种敏感性分析。在科索沃战争平民伤亡案例中展示了该方法的实用性。该框架本质上是一种敏感性分析方法，与因果推断中基于识别假设的敏感性分析（如E-value、proximal causal inference中的negative control）思路相通，可为您的识别假设验证和软件工具开发提供直接借鉴。
- **关键技术**: `multiple-systems estimation`, `capture-recapture`, `identifying assumption`, `sensitivity analysis`, `missing data`, `log-linear models`
- **为什么对您有用**: 本文直接链接您对causal inference中identification和sensitivity analysis的兴趣，特别是识别假设的显式化与解耦策略，与proximal CI中negative control假设的运用同源。您的very_familiar武器库中的software development可立即用于实现类似敏感性分析工具，而moderately_familiar的identification theory则有助于深入理解其识别框架，属于**中期可做**方向（需先在identification theory上进一步积累）。

### 10. [10.1093/biomtc/ujad007](https://doi.org/10.1093/biomtc/ujad007) · [arXiv](https://arxiv.org/abs/2212.02422) — Adaptive sequential surveillance with network and temporal dependence
- **作者**: Ivana Malenica, Jeremy R Coyle, Mark J van der Laan, Maya L Petersen
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究传染病监测中的适应性序贯检测分配问题，目标是在资源和网络/时间依赖的约束下最大化识别病例的公共卫生效果。核心设定是潜在感染状态为隐变量，且个体间依赖结构（网络）和时间依赖均未指定，将数据视为单一观测。作者将因果参数定义为：在给定历史观测下，若实施最大化期望阳性数（受资源限制）的随机干预，所得到的潜在结果均值。方法上不建模依赖结构，而是使用在线超级学习器（Online Super Learner）实时从候选依赖模型和随机化方案中动态选择最优策略，从而适应疫情演变并跨样本学习。模拟实验在COVID-19大学宿舍环境中验证了该方法相比固定策略的优越性能。该工作连接了因果推断中的序贯设计（longitudinal causal inference）与流行病学实际监测问题，其在线选择依赖模型的思路对您处理复杂依赖下的因果估计具有借鉴意义。
- **关键技术**: `Online Super Learner`, `adaptive sequential design`, `stochastic intervention`, `resource constraint`, `agent-based simulation`
- **为什么对您有用**: 该论文直接对应您流行病学（secondary interest）和纵向因果推断（primary interest）的交汇点：利用序贯随机干预定义因果参数并在线优化检测策略。您武器库中的因果推断估计理论和软件技能（very_familiar）足以理解该方法，但若要深入评估或扩展其识别假设（如序贯可忽略性），需要在中等熟悉的因果识别理论上进一步巩固。中期可做：可针对该框架的识别条件进行敏感性分析或采用交叉拟合（cross-fitting）改进估计性能。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 3 篇)*

### 1. [10.1093/biomtc/ujad002](https://doi.org/10.1093/biomtc/ujad002) · [arXiv](https://arxiv.org/abs/2308.16333) — Multiple augmented reduced rank regression for pan-cancer analysis
- **作者**: Jiuzhou Wang, Eric F Lock
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文提出 multiple augmented reduced rank regression (maRRR)，一种结合多个数据集进行联合矩阵回归与分解的灵活方法。目标是在多队列高维数据中同时学习协变量驱动的低秩结构以及各队列特有或共享的辅助变异结构。目标函数采用由随机矩阵理论启发的结构化核范数，同时惩罚回归系数矩阵与残差低秩成分。该方法将现有的降秩回归和无监督多矩阵分解统一在同一个框架下，并引入了针对单数据集的‘增广降秩回归’新变体。模拟实验显示整合多个队列显著提升统计功效，且更加节俭地解释全部结构变异。应用于 TCGA 的泛癌基因表达数据（以体细胞突变为协变量），在预测和填补任务上表现良好，并揭示了跨癌种共享或特有的变异模式。对您而言，其核心工具——结构化核范数与随机矩阵理论动机——直接连接您的高维随机矩阵理论兴趣；您可用擅长的极小极大下界技术分析其估计量的相变阈值或收敛速度。
- **关键技术**: `structured nuclear norm`, `random matrix theory`, `reduced rank regression`, `multi-cohort matrix factorization`, `augmented regression`
- **为什么对您有用**: 本文直接连接您的高维统计——随机矩阵理论兴趣（摘要明确以RMT驱动核范数目标）。您可用非常熟悉的高维渐近理论与极小极大界分析该方法的相变行为或估计误差（属于立即可做，因为现有武器库中的‘高维渐近’与‘极小极大界’直接适用）。此外，若您对统计学在癌症基因组学中的应用感兴趣，本文提供了真实数据集与分析流程，可作为流行病学/应用方向的入门参照。

### 2. [10.1093/biomtc/ujad042](https://doi.org/10.1093/biomtc/ujad042) · [arXiv](https://arxiv.org/abs/2208.12383) — High-dimensional sparse vine copula regression with application to genomic prediction
- **作者**: Özge Sahin, Claudia Czado
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 该论文针对高维基因组预测数据中存在的非线性关系和复杂依赖结构，提出两种基于vine copula的稀疏回归方法。现有vine copula回归无法扩展至高维，该文首先证明新方法在计算复杂度上的优势。方法通过定义分位数回归中相关、无关及冗余自变量，实现变量选择与预测。模拟研究表明，在稀疏高维设定下，方法能有效识别相关变量并提升预测精度。实际数据应用基于玉米性状的基因组预测，并与线性模型、分位数随机森林比较，展示优越性。该文为高维非线性依赖下的变量选择提供了新工具，与您关注的高维统计变量选择方向直接相关。
- **关键技术**: `vine copula regression`, `quantile regression`, `variable selection`, `sparsity`, `high-dimensional regression`
- **为什么对您有用**: 本文属于高维统计中的稀疏变量选择问题，与您对高维渐近理论（very_familiar）的兴趣对口。vine copula引入非线性依赖，其理论分析可能需要您补充copula基础知识，属于中期可做：需先在nonparametric statistics（very_familiar）中熟悉vine copula的建模框架。

### 3. [10.1093/biomtc/ujad014](https://doi.org/10.1093/biomtc/ujad014) — Incorporating graph information in Bayesian factor analysis with robust and adaptive shrinkage priors
- **作者**: Qiyiwen Zhang, Changgee Chang, Li Shen, Qi Long
- **期刊/来源**: Biometrics
- **机构**: University of Pennsylvania · Indiana University School of Medicine · Indiana University – Purdue University Indianapolis
- **分类**: vol 80 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究高维多组学数据分解为低秩稀疏矩阵的问题，提出一种结合生物学图信息的贝叶斯因子分析模型。现有贝叶斯因子模型很少有效整合基因网络等图结构，作者设计了一个新颖的分层先验，通过图信息识别协同工作的基因群，实现网络内稀疏性。该先验还引入额外层次将个体收缩参数与图信息关联，并克服了相位转变现象，对不一致的噪声边具有鲁棒性。模型可同时处理连续和离散数据类型，模拟实验和真实数据分析表明其优于若干现有因子分析方法。文中使用的自适应收缩先验和图引导稀疏化策略，为高维结构化变量选择提供了新思路。对您而言，该研究展示了图信息在高维贝叶斯推断中的有效整合方式，可拓展您在 high-dimensional statistics 方向上的工具箱。
- **关键技术**: `Bayesian factor analysis`, `graph-guided sparsity`, `adaptive shrinkage priors`, `hierarchical priors`, `phase transition robustness`
- **为什么对您有用**: 本文属于 high-dimensional statistics 中因子模型的图正则化方法，与您的高维统计兴趣直接相关。您可以运用 very_familiar 中的 high-dimensional asymptotics 分析其先验的收缩性质，或评估其 minimax 最优性。但由于核心方法是贝叶斯分层先验与 MCMC 计算，而您的武器库以频率学派方法为主，目前暂不可直接复现其计算；若未来您对贝叶斯计算产生兴趣，则可通过 moderate_familiar 的 semiparametric theory 对比其与频率学派正则化的异同。

## 非参数 / 半参数  *(nonparam_semipara, 10 篇)*

### 1. [10.1093/biomtc/ujad006](https://doi.org/10.1093/biomtc/ujad006) — Longitudinal varying coefficient single-index model with censored covariates
- **作者**: Shikun Wang, Jing Ning, Ying Xu, Ya-Chen Tina Shih, Yu Shen, Liang Li
- **期刊/来源**: Biometrics
- **机构**: Columbia University · The University of Texas MD Anderson Cancer Center · University of California, Los Angeles
- **分类**: vol 80 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在纵向医疗成本数据分析中，目标是估计从癌症诊断到死亡期间的人群平均成本轨迹，同时刻画患者特征对轨迹的影响。核心挑战包括：成本数据的偏态、零膨胀和异方差性，轨迹的非线性，以及生存时间的删失导致轨迹长度和形状依赖生存时间。作者提出纵向变系数单指数模型（longitudinal varying coefficient single-index model），将多个患者特征压缩为单指数以表示医疗使用倾向，该指数对成本轨迹的影响通过二元变系数函数灵活建模，同时依赖时间和生存状态。估计方法采用广义估计方程（GEE）并扩展边际均值结构以将删失生存时间作为协变量处理。理论贡献包括建立变系数函数的逐点置信区间和协变量效应的假设检验，估计量具有 n^{-1/2}-CAN 性质。模拟研究验证了有限样本表现，并应用于 SEER-Medicare 前列腺癌患者的医疗成本数据。对您而言，这篇论文展示了半参数单指数模型在复杂数据结构下的扩展应用，涉及 GEE 估计和逐点推断，属于应用导向的方法学工作。
- **关键技术**: `varying coefficient model`, `single-index model`, `generalized estimating equations`, `pointwise confidence interval`, `censored covariate`, `bivariate smoothing`
- **为什么对您有用**: (1) 连接到 semiparametric theory 的单指数模型设定，以及 longitudinal data 的边际建模框架。(2) 您的 very_familiar 武器库中 nonparametric statistics 和 estimation theory in causal inference 可以直接审视其估计策略；moderately_familiar 的 semiparametric theory 可用于分析其效率性质——本文未涉及 semiparametric efficiency bound，这是一个可切入的理论口子。(3) **中期可做**：若想在此方向深入，需先在 semiparametric theory 上长肌肉，特别是单指数模型的效率理论和最优估计；当前论文是应用导向，理论深度有限，但作为 longitudinal semiparametric model 的实例可快速浏览。

### 2. [10.1093/biomtc/ujad023](https://doi.org/10.1093/biomtc/ujad023) — Nonparametric predictive model for sparse and irregular longitudinal data
- **作者**: Shixuan Wang, Seonjin Kim, Hyunkeun Ryan Cho, Won Chang
- **期刊/来源**: Biometrics
- **机构**: Miami University · University of Iowa · University of Cincinnati
- **分类**: vol 80 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在稀疏不规则纵向数据设定下，目标是预测响应变量的均值轨迹，假设预测变量轨迹与响应轨迹在 L2 空间中具有相似性模式。作者提出基于核的估计器，通过 L2 距离度量被试间预测轨迹相似性来构建权重，并采用乘积型多元高斯核模型处理多预测变量的维数灾难问题。该方法同时实现降维与功能性协变量筛选，在 mild regularity conditions 下建立了估计量的渐近性质（一致性、收敛速度）。模拟与 Framingham Heart Study 数据展示了方法的稳健性与灵活性。对您在非参数理论与纵向数据因果推断方向的兴趣有直接参考价值。
- **关键技术**: `kernel-based estimation`, `L2 metric space similarity`, `multiplicative Gaussian kernel model`, `functional covariate selection`, `sparse longitudinal data`, `nonparametric asymptotic theory`
- **为什么对您有用**: 直接连接到您 primary interest 中的非参数理论与纵向数据设定。您 very_familiar 的 nonparametric statistics 与 minimax bounds 工具可用来审视其收敛速度是否达到最优率，moderately_familiar 的 semiparametric theory 可用于探讨是否可构造更高效的 one-step estimator。**中期可做**：若想在此方向深入，需先在 semiparametric theory 上长肌肉，将核估计与 influence function 方法结合以提升效率。

### 3. [10.1093/biomtc/ujad041](https://doi.org/10.1093/biomtc/ujad041) — Simultaneous variable selection and estimation in semiparametric regression of mixed panel count data
- **作者**: Lei Ge, Tao Hu, Yang Li
- **期刊/来源**: Biometrics
- **机构**: Northeast Normal University · Indiana University School of Medicine · Indiana University – Purdue University Indianapolis · Capital Normal University
- **分类**: vol 80 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究混合面板计数数据（mixed panel count data）下的变量选择与估计问题，目标是在比例均值模型（proportional mean model）下同时实现协变量筛选与回归系数估计。作者提出基于惩罚似然的 SCAD/MCP 正则化方法，针对面板计数与面板二值成分的混合结构构建部分似然，并开发 EM 算法实现稀疏估计。理论证明估计量具有 oracle property，即在真实模型已知时的渐近分布与变量选择一致性。模拟与 HRS 数据应用验证了有限样本表现。对您而言，这是半参数回归框架下正则化估计与 M-估计理论的直接应用案例。
- **关键技术**: `penalized likelihood`, `SCAD/MCP regularization`, `EM algorithm`, `oracle property`, `proportional mean model`, `panel count data`
- **为什么对您有用**: 本文属于半参数回归与变量选择的交叉领域，与您 primary interest 中的 semiparametric theory 和 M-estimation theory 直接相关。从 technical_arsenal 角度，您对 M-估计理论的 moderately_familiar 程度足以验证其 oracle property 证明的严谨性，但论文核心是方法学与实证应用，理论 novelty 相对有限。follow-up 判断：**中期可做**——若想深入，需在 semiparametric efficiency 方向长肌肉，考察当前惩罚似然方法是否达到半参数有效界，或是否存在效率损失。

### 4. [10.1093/biomtc/ujad024](https://doi.org/10.1093/biomtc/ujad024) · [arXiv](https://arxiv.org/abs/2303.05341) — Penalized deep partially linear cox models with application to CT scans of lung cancer patients
- **作者**: Yuming Sun, Jian Kang, Chinmay Haridas, Nicholas Mayne, Alexandra Potter, Chi-Fu Yang et al.
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对肺癌患者CT扫描纹理特征与生存风险的关系，提出了惩罚深度部分线性Cox模型（Penalized DPLC）。该模型将风险函数分解为参数部分（处理高维纹理特征）和非参数部分（通过深度神经网络估计）。参数部分采用SCAD惩罚进行变量选择，以应对高维情形；非参数部分用DNN拟合，缓解维数诅咒。作者证明了估计量的收敛性和渐近性质，并通过模拟研究比较了风险预测和变量选择性能。最后应用于NLST数据集，揭示了关键临床和影像风险因素对患者生存的影响。该工作将高维惩罚回归与深度学习结合到半参数Cox模型中，为生存分析中的高维影像数据提供了一种可行的分析框架。
- **关键技术**: `SCAD penalized variable selection`, `deep neural network`, `partial linear Cox model`, `high-dimensional survival analysis`, `asymptotic properties of penalized DNN estimators`
- **为什么对您有用**: 本研究直接关联到您对高维统计和半参数模型的兴趣。从技术层面看，您可以用非常熟悉的高维渐近理论来审读其SCAD惩罚部分的oracle性质，并用非参数统计的minimax观点评估其DNN部分的估计效率——这些工具您已熟练掌握。不过，本文涉及深度神经网络的理论分析（如收敛率）并非您目前武器库的核心，因此建议列为中期可做：您需要先在deep learning理论（nonparametric neural network approximation）上适度拓展，即可完整评判该方法的优势和局限。

### 5. [10.1093/biomtc/ujae001](https://doi.org/10.1093/biomtc/ujae001) · [arXiv](https://arxiv.org/abs/2203.01990) — From local to global gene co-expression estimation using single-cell RNA-seq data
- **作者**: Jinjin Tian, Jing Lei, Kathryn Roeder
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文关注单细胞 RNA-seq 数据中基因关系的局部依赖性估计问题。传统的全局依赖度量无法捕捉随样本点变化、可能仅存在于子集且非线性的基因关系。作者提出 averaged Local Density Gap (aLDG)，通过对细胞特异基因网络（每个细胞一个局部密度比）进行总体平均，得到一个能累积局部依赖性且可检测任意非线性非单调关系的单变量依赖度量。他们还给出了 aLDG 的一致非参数估计量，并在总体和经验层面证明了其稳健性。进一步，他们引入 mini-batch 变体，按外部结构（如空间或时间因子）将细胞分组后平均，以更好地突出有意义的局部结构变化点。通过模拟和真实数据分析（包括成对基因关系估计、细胞轨迹分叉点检测、空间转录组结构可视化），aLDG 在检测能力上优于现有方法。该工作对您有价值：它提供了一个非参数依赖度量的新视角，可以推广到其他需要局部依赖检测的场景，例如因果推断中的条件独立性测试。
- **关键技术**: `Local Density Gap`, `averaged Local Density Gap (aLDG)`, `cell-specific gene networks`, `nonparametric dependence measure`, `mini-batch averaging`, `kernel density estimation`
- **为什么对您有用**: 本论文直接连接您的 primary interest 中的非参数理论，尤其是局部依赖度量及其一致估计。您 very_familiar 的非参数统计工具（核密度估计、收敛速率）可以直接用于检验 aLDG 估计量的理论性质。目前可以直接动手复现其模拟和数据分析，中期可尝试将其与 higher-order U-statistics 结合，推导 aLDG 的 U-statistic 表示与高阶影响函数，从而改善计算效率。

### 6. [10.1093/biomtc/ujae012](https://doi.org/10.1093/biomtc/ujae012) — Accounting for network noise in graph-guided Bayesian modeling of structured high-dimensional data
- **作者**: Wenrui Li, Changgee Chang, Suprateek Kundu, Qi Long
- **期刊/来源**: Biometrics
- **机构**: University of Pennsylvania · Indiana University School of Medicine · Indiana University – Purdue University Indianapolis · The University of Texas MD Anderson Cancer Center
- **分类**: vol 80 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在高维回归设定下，目标是估计回归系数同时进行变量选择，关键假设是预测变量的真实网络结构未知且现有数据库网络存在噪声（缺失边和伪边）。方法提出 graph-guided Bayesian 框架，融合数据库 noisy graph 与数据驱动估计图两源信息，通过 latent scale modeling 对真实网络建模，配合 adaptive structured shrinkage prior 实现结构化收缩。后验推断采用 MCMC 采样，理论贡献主要是贝叶斯框架下的网络噪声校正机制，而非频率派的收敛率或效率界。模拟与阿尔茨海默病基因组/蛋白质组数据分析显示，相比忽略网络噪声的现有方法，在变量选择和预测精度上有提升。对您而言，这是贝叶斯结构化高维回归的应用案例，可作为 semiparametric theory 与贝叶斯方法交叉视角的参考阅读。
- **关键技术**: `graph-guided Bayesian regression`, `latent scale modeling`, `adaptive structured shrinkage prior`, `MCMC posterior sampling`, `network uncertainty quantification`, `high-dimensional variable selection`
- **为什么对您有用**: 本文属于贝叶斯高维回归在基因组学中的应用，与您 primary interest 中的 semiparametric theory 和 high-dimensional statistics 有交叉，但核心是贝叶斯建模而非频率派效率理论或 minimax rate。您的 very_familiar 武器库中 minimax bounds 和 high-dimensional asymptotics 可用于审视其收缩先验的理论性质（如后验收缩率），但本文未提供此类理论结果。follow-up 判定：**暂不可做**——若想深入此方向，需先在 moderately_familiar 的 semiparametric theory 基础上补充贝叶斯非参数理论（后验收缩率、变分近似理论），当前武器库不直接支撑贝叶斯高维推断的理论分析。

### 7. [10.1093/biomtc/ujae010](https://doi.org/10.1093/biomtc/ujae010) — A boosting method to select the random effects in linear mixed models
- **作者**: Michela Battauz, Paolo Vidoni
- **期刊/来源**: Biometrics
- **机构**: University of Udine
- **分类**: vol 80 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在线性混合模型（LMM）框架下，研究目标是随机效应结构的选择问题，即识别哪些随机效应系数方差为零。作者提出基于 profile negative log-likelihood 的 boosting 方法进行变量选择，核心难点在于目标函数的非凸性。为处理非凸优化，算法同时利用 Newton 方向和负曲率方向进行迭代更新，以避免陷入局部极小值。理论部分未给出选择一致性证明或渐近分布结果，主要通过模拟和实例展示方法在有限样本下的表现。对您而言，这是 M-estimation 与非凸优化在经典模型选择场景的一个具体应用实例。
- **关键技术**: `likelihood-based boosting`, `linear mixed models`, `nonconvex optimization`, `negative curvature direction`, `profile likelihood`, `random effects selection`
- **为什么对您有用**: (1) 连接到 primary interest 中的 semiparametric theory 与 M-estimation theory——随机效应选择本质上是方差成分的边界检验问题，涉及 non-regular asymptotics。(2) 您武器库中的 M-estimation theory（moderately_familiar）可用于分析该 estimator 的渐近性质，目前文章缺乏选择一致性或 oracle property 的理论保证，这是一个可切入的理论口子。(3) follow-up 判断：**中期可做**——需先在 semiparametric theory / M-estimation 的边界检验理论上长肌肉，才能处理非凸目标函数下变量选择的一致性问题。

### 8. [10.1093/biomtc/ujae020](https://doi.org/10.1093/biomtc/ujae020) — Conditional modeling of panel count data with partly interval-censored failure event
- **作者**: Xiangbin Hu, Wen Su, Zhisheng Ye, Xingqiu Zhao
- **期刊/来源**: Biometrics
- **机构**: Hong Kong Polytechnic University · City University of Hong Kong · National University of Singapore
- **分类**: vol 80 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究纵向随访中 panel count data 与部分区间删失失效事件的联合建模问题，目标是在失效事件信息性地影响复发事件的设定下估计回归参数。作者提出 failure-time-dependent proportional mean model，通过未指定的 link function 实现对失效事件效应的直接解释，避免了 latent variable model 的间接性。估计方法采用条件期望最小二乘函数处理部分区间删失，发展了两阶段估计程序：第一阶段用 B-spline 逼近未知 baseline mean 和 link function，第二阶段将失效时间分布视为 functional nuisance parameter。理论贡献包括建立估计量的整体收敛速率、有限维参数估计的渐近正态性以及无穷维估计泛函的渐近性质。该方法应用于健康长寿纵向研究数据，对您在纵向因果推断与半参数理论方向有参考价值。
- **关键技术**: `panel count data`, `partly interval-censoring`, `B-spline approximation`, `two-stage estimation`, `proportional mean model`, `semiparametric efficiency`
- **为什么对您有用**: 本文直接关联您 primary interest 中的 semiparametric theory 和 longitudinal causal inference——其两阶段估计程序、B-spline 逼近无穷维参数、以及渐近正态性推导都是典型的半参数方法。您可以用 very_familiar 的 nonparametric statistics 和 moderately_familiar 的 semiparametric theory 来审视其收敛速率是否可达 semiparametric efficiency bound，以及 nuisance parameter 估计精度对最终推断的影响。立即可做：用您熟悉的 minimax bound 工具验证其收敛速率是否紧，或探索在 causal longitudinal setting 下类似条件期望策略的适用性。

### 9. [10.1093/biomtc/ujad011](https://doi.org/10.1093/biomtc/ujad011) — Proportional rates models for multivariate panel count data
- **作者**: Yangjianchen Xu, Donglin Zeng, Dan-Yu Lin
- **期刊/来源**: Biometrics
- **机构**: University of North Carolina at Chapel Hill
- **分类**: vol 80 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究多变量面板计数数据下多种复发事件类型的回归效应估计，目标参数是比例速率模型中的回归系数，关键假设是各事件类型的边际速率模型正确设定，而对事件间依赖结构不做任何参数假设。采用非参数极大伪似然估计，在工作独立性假设下构造似然函数，发展了简单稳定的 EM 型算法进行计算。证明了回归参数估计量具有相合性与渐近正态性，协方差矩阵可通过三明治估计量相合估计，渐近性质不依赖于工作独立性假设的正确性。提出了模型检验的图形与数值方法，并通过皮肤癌临床试验数据进行了实证分析。对您在 semiparametric theory 方向的工作有参考价值，展示了伪似然方法在复杂依赖结构下的稳健性。
- **关键技术**: `nonparametric maximum pseudo-likelihood`, `EM algorithm`, `sandwich variance estimator`, `proportional rates model`, `panel count data`, `model diagnostics`
- **为什么对您有用**: 本文属于 semiparametric theory 的应用，展示了在依赖结构完全未设定时伪似然估计仍能获得有效推断，与您 moderately_familiar 的 semiparametric theory 直接相关。技术核心是 sandwich variance 的构造与渐近正态性证明，用您 very_familiar 的 minimax bounds 和 estimation theory 武器可以验证其效率性质或考虑更优估计量。立即可做：用 semiparametric efficiency 理论分析该估计量是否达到效率下界，或考虑 higher-order influence function 改进。

### 10. [10.1093/biomtc/ujad021](https://doi.org/10.1093/biomtc/ujad021) · [arXiv](https://arxiv.org/abs/2210.08297) — Clustering blood donors via mixtures of product partition models with covariates
- **作者**: Raffaele Argiento, Riccardo Corradin, Alessandra Guglielmi, Ettore Lanzarone
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在 Bayesian nonparametric 框架下，目标是利用献血者协变量信息改进聚类预测，estimand 为 successive blood donation gap times 的后验预测分布。作者提出 mixtures of product partition models with covariates (PPMx)，通过 cohesion function 的混合和基于 cluster denseness 的 similarity function 构建随机划分先验。核心机制是让协变量相似的个体更可能被聚到同一类，从而在先验层面融入协变量信息而非仅在似然中建模。理论贡献包括证明后验一致性性质，实证显示在意大利献血数据上预测性能优于标准 PPMx。对您在 semiparametric theory 和 efficiency 方面的兴趣而言，这是一个 Bayesian nonparametric clustering 的应用实例。
- **关键技术**: `product partition models`, `Bayesian nonparametric clustering`, `covariate-dependent partition prior`, `posterior predictive inference`, `mixture models`
- **为什么对您有用**: 本文属于 Bayesian nonparametric 方法的应用拓展，与您 primary interest 中的 semiparametric theory 有一定距离——它从 Bayesian 角度处理聚类与预测，而非 frequentist semiparametric efficiency 或 influence function 理论。技术武器库中的 nonparametric statistics 和 M-estimation theory 可用于理解其理论性质，但核心 Bayesian nonparametric 工具（如 random partition prior、Dirichlet process 相关理论）不在您的 very_familiar 或 moderately_familiar 列表中。**暂不可做**：若想深入此类方向，需先补充 Bayesian nonparametric 的基础（如 Dirichlet process、random partition model 的 asymptotic theory）。

## 效率理论 / Debiased ML  *(efficiency_dml, 2 篇)*

### 1. [10.1093/biomtc/ujad034](https://doi.org/10.1093/biomtc/ujad034) · [arXiv](https://arxiv.org/abs/2210.17453) — Adaptive selection of the optimal strategy to improve precision and power in randomized trials
- **作者**: Laura B Balzer, Erica Cai, Lucas Godoy Garraza, Pracheta Amaranath
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在随机化试验的协变量调整设定下，目标是选择最优调整策略（变量及其函数形式）以最大化精度同时保持 Type-I error 控制。核心方法是 Adaptive Pre-specification 框架下的 TMLE，使用 V-fold cross-validation 和 estimated influence curve-squared 作为 loss function，从候选集（包括 GLM 和 ML 方法）中选择最优调整。理论保证包括 Type-I error 控制和一致性；模拟显示精度提升相当于样本量减少 20%-43%。对您在效率理论和 semiparametric efficiency bounds 方面的兴趣有直接参考价值。
- **关键技术**: `TMLE`, `influence function`, `cross-validation`, `adaptive pre-specification`, `covariate adjustment`, `precision gain`
- **为什么对您有用**: 直接连接到您 primary interest 中的 efficiency theory（semiparametric efficiency bounds）和 semiparametric theory。您 very_familiar 的 estimation theory in causal inference 和 moderately_familiar 的 semiparametric theory / HOIF 可以直接用来分析其 influence-function-based selection 的理论性质（如是否达到 efficiency bound）。立即可做：用您的 semiparametric efficiency 知识验证其声称的 efficiency gain 是否最优，或扩展到 longitudinal setting。

### 2. [10.1093/biomtc/ujae018](https://doi.org/10.1093/biomtc/ujae018) — Fitting the Cox proportional hazards model to big data
- **作者**: Jianqiao Wang, Donglin Zeng, Dan-Yu Lin
- **期刊/来源**: Biometrics
- **机构**: University of North Carolina at Chapel Hill
- **分类**: vol 80 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对Cox比例风险模型在百万级样本大数据下的拟合计算问题。作者提出先对随机抽取的小子集做最大部分似然估计，然后利用全数据估计的有效得分函数（efficient score function）进行一步校正（one-step estimation），从而整合剩余数据。最终估计量的渐近分布与基于全数据的标准MLE等价，但计算时间仅为其一小部分。该方法本质上是将半参数效率理论中的一步估计思想应用于大规模数据场景，以计算成本换取统计效率的保留。模拟实验及UK Biobank数据分析验证了方法的实用性与精度。对您而言，该工作展示了有效得分函数与一步估计在真实大数据场景下的成功落地，与debiased ML及半参数效率方向直接相关。
- **关键技术**: `one-step estimation`, `efficient score function`, `Cox proportional hazards model`, `subset estimation`, `asymptotic equivalence`
- **为什么对您有用**: 连接点：本文直接应用半参数效率理论中的有效得分函数和一步估计，与您对debiased ML和半参数效率bounds的兴趣高度重合。技术武器库中'因果推断中的估计理论'和'软件开发'可立即用于理解、复现该方法，并可考虑将其迁移至因果推断中其他半参数模型（如带时变处理的Cox模型）以应对大数据场景。评估：立即可做——该方法是经典一步估计的直接应用，现有软件工具足够支撑扩展。

## 数理统计 / 假设检验  *(hypothesis_testing, 4 篇)*

### 1. [10.1093/biomtc/ujae015](https://doi.org/10.1093/biomtc/ujae015) · [arXiv](https://arxiv.org/abs/2207.00926) — Asymptotic uncertainty of false discovery proportion
- **作者**: Meng Mei, Tao Yu, Yuan Jiang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文在多重检验的弱依赖假设下，研究假发现比例（FDP）的渐近不确定性。已有工作表明FDP在弱依赖下强相合于同一极限，但作者发现即使弱依赖，FDP的渐近方差仍显著受依赖结构影响。在检验统计量服从多元正态且弱相关的设定下，推导了FDP的渐近展开，并系统分析了不同协方差模式对方差表达式的定量影响。技术手段主要基于delta方法和对弱依赖协方差矩阵的谱分析。基于理论结果，建议在多重检验报告中同时汇报FDP的均值与方差估计，以更准确评估研究结论的可靠性。本文直接切合您在假设检验方向的实际关切，尤其您熟悉的高维渐近工具可用于进一步放松正态或弱依赖假设。
- **关键技术**: `FDP asymptotic expansion`, `weak dependence`, `asymptotic variance decomposition`, `delta method`, `multiple testing`
- **为什么对您有用**: 本文专注假设检验中的核心问题——多重比较下错误发现率的变异性，属于您 primary interest 中的 hypothesis testing 子方向。您 very_familiar 武器中的「高维渐近」可以用于分析文中弱依赖协方差谱对方差的影响，甚至拓展到非正态或高维稀疏设定；而您对统计计算的熟悉程度也方便为建议的方差估计方法编写软件库。这是一个中期可做的方向：先通过本文掌握弱依赖FDP方差的数学结构，再结合 moderately_familiar 中的 semiparametric 技术（如局部经验过程）处理更一般的依赖模式。

### 2. [10.1093/biomtc/ujad040](https://doi.org/10.1093/biomtc/ujad040) — Sparse ordinal discriminant analysis
- **作者**: Sangil Han, Minwoo Kim, Sungkyu Jung, Jeongyoun Ahn
- **期刊/来源**: Biometrics
- **机构**: Seoul National University · Korea Advanced Institute of Science and Technology
- **分类**: vol 80 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在有序多分类（ordinal classification）设定下，目标是构建一个稀疏、低维的判别子空间，使得投影方向能反映类别间的自然有序结构。作者基于线性判别分析（LDA）的最优得分（optimal scoring）框架，同时施加两类惩罚：对最优得分施加有序性惩罚以编码类别顺序，对预测变量系数施加稀疏惩罚以实现变量选择。方法的核心是变量选择不再基于边际关联，而是基于变量集体对有序标签的贡献，通过 penalized LDA 框架实现。理论部分证明了估计的一致性，模拟和胶质瘤基因表达数据的实证表明分类性能有竞争力且估计结果对有序标签具有更好的可解释性。对您在高维统计与 M-estimation 理论方面的兴趣有参考价值。
- **关键技术**: `optimal scoring for LDA`, `ordinality penalty`, `sparse discriminant analysis`, `coordinate descent optimization`, `penalized M-estimation`
- **为什么对您有用**: 本文连接到您 primary interest 中的高维统计与 M-estimation 理论：它本质上是一个带结构约束的 penalized M-estimation 问题，有序性惩罚可以视为对参数空间的 shape constraint。您可以用 very_familiar 的 minimax bounds 工具分析该方法在有序设定下的 rate optimality，或用 moderately_familiar 的 M-estimation 理论分析其 asymptotic properties（如 oracle property 是否成立）。Follow-up 判定：**中期可做**——需先在 moderately_familiar 的 M-estimation 理论上确认 penalized LDA 的理论工具是否完备，再切入有序结构带来的新理论问题。

### 3. [10.1093/biomtc/ujae006](https://doi.org/10.1093/biomtc/ujae006) — Changing interim monitoring in response to internal clinical trial data
- **作者**: Michael A Proschan, Martha Nason, Ana M Ortega-Villa, Jing Wang
- **期刊/来源**: Biometrics
- **机构**: National Institute of Allergy and Infectious Diseases
- **分类**: vol 80 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究在未预设适应性设计的临床试验中，如何根据内部期中数据动态增加 interim analysis 而不膨胀 type I error。核心设定是 two-arm trial，estimand 为 treatment effect，关键假设是 conditional error principle 可在无预先规划时保护 type I error。方法基于 Müller and Schäfer (2004) 的 conditional error principle，允许在观察到外部或内部数据后修改监控计划，通过条件概率重新计算 stopping boundary，确保 overall type I error rate 不变。理论结果表明该方法在任意 post-hoc 修改下保持 valid type I error control，但 power 和 expected sample size 的优化受限于修改时机和信息量。对您在 hypothesis testing 和 clinical trial design 方面的兴趣有直接参考价值。
- **关键技术**: `conditional error principle`, `type I error control`, `interim analysis`, `adaptive design`, `alpha spending`, `stopping boundary`
- **为什么对您有用**: 直接连接到您 primary interest 中的 hypothesis testing，特别是临床试验多重检验与 error control 的理论框架。conditional error principle 是一个 elegant 的概率工具，用您 very_familiar 的非参数统计和估计理论可以深入分析其 power property 和 optimal modification strategy。**立即可做**：用您熟悉的 minimax bound 和估计理论工具，可以分析在什么条件下动态修改 interim analysis 能达到 near-optimal power-sample size tradeoff，或研究 multiple post-hoc modifications 的累积效应。

### 4. [10.1093/biomtc/ujad013](https://doi.org/10.1093/biomtc/ujad013) — Randomized phase II selection design with order constrained strata
- **作者**: Yi Chen, Menggang Yu
- **期刊/来源**: Biometrics
- **机构**: University of Wisconsin–Madison
- **分类**: vol 80 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究随机化 II 期临床试验中的 selection design，在存在分层（strata）且各层响应率有自然序约束（order constraint）的设定下，目标是提高正确选择最优治疗方案的概率。核心方法是利用序约束构造 restricted maximum likelihood estimator，并在 binary 和 time-to-event 两种结局下推导了正确选择概率（probability of correct selection）的样本量公式。理论贡献在于证明序约束可带来效率增益，模拟和实例显示样本量可减少或选择正确率提升。对您在 hypothesis testing 与效率理论方面的兴趣有直接参考价值。
- **关键技术**: `order-constrained inference`, `restricted maximum likelihood`, `probability of correct selection`, `stratified clinical trial design`, `sample size calculation`
- **为什么对您有用**: 本文连接到您 primary interest 中的 hypothesis testing 与 efficiency theory——序约束下的 restricted MLE 本质上是利用参数空间的先验结构来提升估计/检验效率，与 semiparametric efficiency 的思想有相通之处。您武器库中的 very_familiar 项目（nonparametric statistics, minimax bounds）足以理解本文的理论框架，属于**立即可做**的阅读范围。不过本文 novelty 属于应用导向的方法改进，理论深度有限，可作为 constrained inference 的入门案例。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1093/biomtc/ujae016](https://doi.org/10.1093/biomtc/ujae016) · [arXiv](https://arxiv.org/abs/2305.08201) — Efficient computation of high-dimensional penalized generalized linear mixed models by latent factor modeling of the random effects
- **作者**: Hillary M Heiling, Naim U Rashid, Quefeng Li, Xianlu L Peng, Jen Jen Yeh, Joseph G Ibrahim
- **期刊/来源**: Biometrics
- **机构**: University of North Carolina at Chapel Hill
- **分类**: vol 80 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对高维广义线性混合模型（GLMM）中固定效应与随机效应同时变量选择的计算瓶颈，提出一种基于因子模型分解的快速计算方法。通过将大量随机效应分解为少量潜在因子，大幅降低潜空间维度，从而缓解高维随机效应带来的计算复杂度。在参数估计方面，采用改进的蒙特卡洛期望条件最大化（MCECM）算法，可同时进行固定效应和随机效应的惩罚变量选择。模拟研究表明，该方法在拟合高维惩罚GLMM时速度显著优于现有方法，且能扩展到更大维度。对您可能有用：本文的因子分解降维思路可启发您在高维因果推断或U统计量计算中处理随机效应时的算法设计。
- **关键技术**: `factor model decomposition`, `Monte Carlo Expectation Conditional Maximization (MCECM)`, `penalized GLMM`, `high-dimensional variable selection`, `latent factor modeling`
- **为什么对您有用**: 本文直接关联您 primary interests 中的统计计算方向，特别是高维模型的可扩展算法。您非常熟悉的软件开发能力可用于复现和扩展该方法；文中因子分解策略或可借鉴到您的高阶U统计量计算中，通过类似降维优化张量收缩成本。此工作立即可做：您具备实现MCECM和惩罚GLMM的软件工程基础，可尝试将该方法应用于因果推断中的纵向数据混合模型。

## 流行病学  *(epidemiology, 7 篇)*

### 1. [10.1093/biomtc/ujae008](https://doi.org/10.1093/biomtc/ujae008) · [arXiv](https://arxiv.org/abs/2302.02110) — A scalar-on-quantile-function approach for estimating short-term health effects of environmental exposures
- **作者**: Yuzi Zhang, Howard H Chang, Joshua L Warren, Stefanie T Ebelt
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在环境流行病学设定下，目标是估计短期暴露（如日均值）对人群健康结局的因果效应，核心难点在于空间单元内暴露分布的异质性无法被区域平均捕捉。本文提出 scalar-on-quantile-function 回归，将暴露分布的 quantile function 作为函数型协变量纳入广义线性模型，从而同时刻画 within-unit 异质性与不同分位水平的效应差异。估计采用函数型数据分析的 spline basis 展开，结合 penalized likelihood 实现正则化，理论层面给出估计的一致性与渐近正态性。实证分析 Atlanta 地区 4 年的空气污染与急诊数据，发现 CO 对呼吸/心血管疾病的影响在暴露分布低分位变化时更为显著。对您而言，这是流行病学应用中处理 exposure misclassification 的函数型方法案例，R 包 nbRegQF 可直接复用。
- **关键技术**: `functional covariate regression`, `quantile function representation`, `penalized spline basis`, `generalized linear model`, `exposure heterogeneity modeling`
- **为什么对您有用**: 本文属于流行病学应用，核心贡献是将暴露分布的 quantile function 作为函数型协变量建模，属于您 secondary interest 中 epidemiology 的应用案例。技术上涉及函数型数据分析与 penalized estimation，与您 very_familiar 的 nonparametric statistics 和 M-estimation theory 有直接连接，可验证其 spline 展开的正则化条件是否满足您熟悉的 M-estimation 收敛理论。follow-up 判断：立即可做——用 very_familiar 的 nonparametric statistics 工具可检验其函数型协变量估计的 minimax rate 是否紧，或用您熟悉的软件能力扩展 nbRegQF 的数值稳定性。

### 2. [10.1093/biomtc/ujad027](https://doi.org/10.1093/biomtc/ujad027) — Estimating the effect of latent time-varying count exposures using multiple lists
- **作者**: Jung Yeon Won, Michael R Elliott, Emma V Sanchez-Vaznaugh, Brisa N Sánchez
- **期刊/来源**: Biometrics
- **机构**: University of Michigan · San Francisco State University · Drexel University
- **分类**: vol 80 · issue 1
- 相关性 7/10 · novelty: `application`
- **摘要**: 在纵向 built-environment 健康研究中，目标是估计 latent time-varying count exposure（如便利店数量）对健康结局（儿童肥胖）的因果效应，核心挑战是多个商业数据库对同一暴露的测量存在不一致和误差。作者提出联合模型，将观测的 count exposure、潜在真实 exposure 和纵向健康结局同时建模，真实 exposure 采用 Poisson INAR(1) 过程刻画时间依赖，并引入 Bayesian nonparametric 方法灵活捕捉 location-specific 异质性。通过估计各数据源的时间特异性质量（sensitivity/specificity 类似思路），方法校正了测量误差导致的效应估计偏差。实证分析使用 2001-2008 年加州公立学校数据，展示了多源数据融合对减少偏差的效果。对您而言，这是一个将 measurement error 校正与纵向因果推断结合的应用案例。
- **关键技术**: `Bayesian nonparametric`, `Poisson INAR(1) process`, `latent variable model`, `measurement error correction`, `longitudinal joint model`
- **为什么对您有用**: 本文属于流行病学应用，核心是纵向设定下的 latent exposure measurement error 校正——与您 primary interest 中的 longitudinal causal inference 和 semiparametric theory 有方法论连接。技术上，本文的 Bayesian nonparametric + INAR(1) 框架可视为一种 identification 策略，但未触及 semiparametric efficiency 或 influence function 层面。从武器库角度，您 very_familiar 的 estimation theory in causal inference 和 moderately_familiar 的 identification theory 足以理解并批判本文的 identification 假设；若要 follow-up，需在 Bayesian computation 上补课（moderately_familiar 之外）。判断：**中期可做**——若想将此问题纳入 semiparametric efficiency 框架，需先在 semiparametric theory 上长肌肉，推导 latent exposure 下 ATE 的 efficient influence function。

### 3. [10.1093/biomtc/ujad010](https://doi.org/10.1093/biomtc/ujad010) — Efficient designs and analysis of two-phase studies with longitudinal binary data
- **作者**: Chiara Di Gravio, Jonathan S Schildcrout, Ran Tao
- **期刊/来源**: Biometrics
- **机构**: Imperial College London · Vanderbilt University Medical Center
- **分类**: vol 80 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在两阶段抽样设计框架下，目标是估计纵向二值结局与昂贵生物标志物暴露之间的关联参数，关键假设是给定第一阶段信息下第二阶段抽样的条件独立性。提出 residual-dependent sampling (RDS) 设计，利用纵向结局和廉价协变量构造残差型筛选统计量，优先抽取信息量大的个体进行暴露测量。分析方法采用半参数似然，通过 EM 算法最大化 profile likelihood，实现第一阶段全样本信息的高效利用。理论推导了估计量的渐近正态性，模拟显示 RDS 设计在时变暴露系数估计上相比现有方法有显著的效率增益。实证分析使用 Lung Health Study 数据，研究遗传标记与肺功能恶化的纵向关联。对您可能有用：这是流行病学纵向数据中两阶段设计的应用范例，展示了半参数效率理论在复杂抽样场景的具体实现。
- **关键技术**: `two-phase sampling design`, `semiparametric likelihood`, `EM algorithm`, `residual-dependent sampling`, `longitudinal binary outcome`, `efficient influence function`
- **为什么对您有用**: (1) 连接到流行病学队列研究的两阶段抽样设计，涉及纵向二值结局的半参数效率问题。(2) 您的 semiparametric theory（moderately_familiar）可以直接用于审视其效率界推导是否达到 semiparametric efficiency bound，以及 EM 算法的数值稳定性是否可从 M-estimation 理论角度改进。(3) **中期可做**：需先在 semiparametric theory 上长肌肉，才能深入评估其效率声明是否紧；若只关注应用层面，现有武器库足够理解设计逻辑。

### 4. [10.1093/biomtc/ujad038](https://doi.org/10.1093/biomtc/ujad038) — Two-phase designs with failure time processes subject to nonsusceptibility
- **作者**: Fangya Mao, Li C Cheung, Richard J Cook
- **期刊/来源**: Biometrics
- **机构**: National Cancer Institute · Division of Cancer Epidemiology and Genetics · University of Waterloo
- **分类**: vol 80 · issue 1
- 相关性 6/10 · novelty: `application`
- **摘要**: 在两阶段抽样设计框架下，研究右删失数据中存在"非易感"亚群（长期生存者/cure fraction）时的回归估计问题，目标参数包括治愈概率和易感者生存时间分布。采用 mixture cure model 设定，考虑三种回归框架：logistic cure model、易感者的 PH model、以及同时建模易感性与失败时间的联合回归。核心贡献是针对双参数场景提出了一类新的 bivariate residual-dependent sampling designs，通过依赖两残差变量的最优抽样策略提升估计效率。模拟显示该方法优于现有 phase II 抽样方案，并应用于 PLCO 癌症筛查试验数据。对您而言，这是流行病学队列研究中两阶段设计的应用范例，涉及 semiparametric efficiency 与最优抽样策略。
- ⚠️ *摘要不完整，待重跑（`python -m research_news.rerun`）*
- **关键技术**: `two-phase sampling design`, `mixture cure model`, `residual-dependent sampling`, `semiparametric efficiency`, `right-censored survival data`, `weighted estimation`
- **为什么对您有用**: 本文属于流行病学应用论文，连接到您 secondary interest 中的 epidemiology 数据集与因果/生存分析方法。技术上涉及 semiparametric efficiency theory（您 moderately_familiar），可作为一个具体案例理解两阶段设计下的最优抽样与效率界问题。作为 gateway reading：本文方法学 novelty 有限（novelty_flag = application），但数据集（PLCO）和分析流程对进入流行病学应用有参考价值，建议快速浏览方法部分后决定是否深入。

### 5. [10.1093/biomtc/ujad008](https://doi.org/10.1093/biomtc/ujad008) — Efficient estimation for left-truncated competing risks regression for case-cohort studies
- **作者**: Xi Fang, Kwang Woo Ahn, Jianwen Cai, Soyoung Kim
- **期刊/来源**: Biometrics
- **机构**: Medical College of Wisconsin · University of North Carolina at Chapel Hill
- **分类**: vol 80 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在 case-cohort 研究设计下，目标是估计 competing risks 场景中 proportional subdistribution hazards 模型的回归参数，同时处理 left truncation 带来的额外挑战。现有 inverse probability weighting (IPW) 方法未处理 left truncation 且对完全观测协变量效率不足，本文提出 augmented inverse probability-weighted (AIPW) estimating equation 以同时解决这两个问题。当有来自其他风险原因的额外信息时，进一步提出利用该信息的更高效估计量。所提估计量具有一致性和渐近正态性，模拟研究显示在回归参数估计上有 unbiased 性质和效率提升。本文将 AIPW 技术从标准生存分析扩展到 left-truncated competing risks 的 case-cohort 设计，对您在流行病学队列研究中处理复杂截断机制的因果推断工作有直接参考价值。
- **关键技术**: `augmented inverse probability weighting (AIPW)`, `proportional subdistribution hazards model`, `competing risks`, `left truncation`, `case-cohort design`, `Fine-Gray model`
- **为什么对您有用**: (1) 本文属于流行病学应用因果工作，涉及复杂截断机制下的回归参数估计，与您 secondary interest 中的 epidemiology (application, causal inference) 直接相关。(2) AIPW 的效率提升机制与您 very_familiar 的 estimation theory in causal inference 和 moderately_familiar 的 semiparametric theory 完全对接，可用 semiparametric efficiency bound 视角验证其声称的效率增益是否达到 optimal。(3) **立即可做**：用您熟悉的 semiparametric efficiency theory 推导该估计量的 influence function，验证是否达到 semiparametric efficiency bound，并可探索是否可用 cross-fitting 进一步提升有限样本表现。

### 6. [10.1093/biomtc/ujae011](https://doi.org/10.1093/biomtc/ujae011) — Bayesian two-stage modeling of longitudinal and time-to-event data with an integrated fractional Brownian motion covariance structure
- **作者**: Anushka Palipana, Seongho Song, Nishant Gupta, Rhonda Szczesniak
- **期刊/来源**: Biometrics
- **机构**: Duke University · University of Cincinnati · Veterans Health Administration · Cincinnati Children's Hospital Medical Center
- **分类**: vol 80 · issue 1
- 相关性 4/10 · novelty: `application`
- **摘要**: 在纵向数据与生存数据的联合建模框架下，目标是预测疾病进展与死亡风险，关键假设是生物标志物轨迹可用积分分数布朗运动（IFBM）刻画。方法上，用 IFBM 替代传统随机截距-斜率模型，通过贝叶斯后验计算拟合纵向子模型，再以预测值作为 Cox 子模型的时变协变量。IFBM 是积分布朗运动的推广，其 Hurst 指数可刻画更丰富的轨迹粗糙度与长期依赖结构。两阶段估计避免了联合似然的计算复杂性，同时导出了实时预测概率的目标函数。实证分析基于淋巴管平滑肌增多症（LAM）国家登记数据，IFBM 模型在预测性能上优于积分 Ornstein-Uhlenbeck 与传统随机效应模型。对您而言，这是一个将非参数随机过程引入纵向因果推断/生存分析的实例，可作为应用导向的 gateway reading。
- **关键技术**: `joint modeling of longitudinal and survival data`, `integrated fractional Brownian motion`, `Bayesian two-stage estimation`, `Cox proportional hazards with time-varying covariates`, `dynamic predictive probabilities`
- **为什么对您有用**: (1) 本文属于流行病学纵向数据分析的应用论文，展示了如何用非参数随机过程（IFBM）刻画生物标志物轨迹的复杂变异，与您 secondary interest 中的 epidemiology 应用场景直接相关。(2) 技术上，IFBM 的 Hurst 指数与轨迹粗糙度的关系涉及非参数统计中的样本路径性质，您 very_familiar 的 nonparametric statistics 可用于理解其理论性质，但本文是贝叶斯计算导向，不涉及 minimax 界或效率理论。(3) 作为 gateway reading：本文对 LAM 疾病登记数据的结构和预测目标有清晰描述，适合作为了解纵向-生存联合建模在流行病学中应用的入门材料；若您想探索纵向因果推断中处理复杂轨迹变异的方法，值得花时间读全文。

### 7. [10.1093/biomtc/ujae013](https://doi.org/10.1093/biomtc/ujae013) — Soft classification and regression analysis of audiometric phenotypes of age-related hearing loss
- **作者**: Ce Yang, Benjamin Langworthy, Sharon Curhan, Kenneth I Vaden, Gary Curhan, Judy R Dubno et al.
- **期刊/来源**: Biometrics
- **机构**: Harvard University · Brigham and Women's Hospital · Medical University of South Carolina
- **分类**: vol 80 · issue 1
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文以年龄相关性听力损失的听力学表型分类为背景，目标是通过二次判别分析（QDA）对表型进行软分类，并利用估计方程分析饮食模式对软分类概率的影响。在合理假设下，估计方程无偏且得到一致估计量，有限样本模拟表现良好。应用数据来自护士健康研究II听力保护研究，分析DASH饮食模式与代谢+感官表型的关联，发现更健康的饮食降低该表型发生风险。该方法提供了一种将分类结果作为连续响应进行回归分析的框架，适用于流行病学中的多类别结局分析。对于您的流行病学应用兴趣，本文展示了一个真实队列中软分类与暴露分析的完整流程，数据结构和分析管道值得借鉴。
- **关键技术**: `Quadratic discriminant analysis`, `Estimating equations`, `Soft classification probabilities`, `Cohort study`
- **为什么对您有用**: 本文属于流行病学应用，使用真实大型队列数据（Nurses' Health Study II）分析饮食与听力损失表型的关联，可直接作为流行病学数据分析的入门案例。您非常熟悉的estimation theory in causal inference中的估计方程工具可用来审视其无偏性条件是否可推广至存在混杂的情形。目前暂不可做：核心因果识别框架未包含在分析中，若需引入因果解释需先加强identification theory (moderately familiar) 中的工具。

## 其他  *(other, 6 篇)*

### 1. [10.1093/biomtc/ujad005](https://doi.org/10.1093/biomtc/ujad005) — Robust data integration from multiple external sources for generalized linear models with binary outcomes
- **作者**: Kyuseong Choi, Jeremy M G Taylor, Peisong Han
- **期刊/来源**: Biometrics
- **机构**: Cornell University · University of Michigan
- **分类**: vol 80 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在广义线性模型（GLM）框架下，目标是利用内部研究的个体数据和多源外部研究的 summary statistics（参数估计）来提高二分类结局回归系数的估计效率。外部模型仅包含内部协变量的子集，作者提出一种 adaptive penalization 方法，通过利用 GLM 全模型与省略协变量子模型参数间的理论关系，对与内部数据兼容性差的外部信息进行降权惩罚。该方法在保持计算效率的同时实现了 robustness：当外部数据与内部数据存在总体异质性时，估计量仍保持一致性；当外部数据兼容时获得效率提升。理论部分未给出显式的渐近分布或 semiparametric efficiency bound，但通过信息准则和 adaptive weights 避免了传统 cross-validation 的计算负担。模拟显示该方法在多种总体异质性设定下优于直接 MLE，实证分析将其应用于前列腺癌高风险预测的 logistic 回归模型。对您在 efficiency theory 和 semiparametric theory 方面的兴趣有直接参考价值，尤其是在多源数据融合的效率界与 robustness 权衡问题上。
- **关键技术**: `data integration from multiple external sources`, `adaptive penalization`, `GLM omitted covariate relationship`, `information criterion for tuning`, `robustness to population heterogeneity`
- **为什么对您有用**: （1）直接连接到您 primary interest 中的 efficiency theory 和 semiparametric theory——多源数据融合下的效率界是一个值得深挖的理论问题，本文的 penalization 方法可视为一种 empirical likelihood / GMM 类型的约束整合，但缺乏显式的 efficiency bound 分析。（2）您 very_familiar 的 estimation theory in causal inference 和 moderately_familiar 的 semiparametric theory 可以用来攻这篇 paper 的理论缺口：例如，用 semiparametric efficiency bound 刻画多源 summary data 融合的最优效率，或用 influence function 分析 penalization 对 asymptotic variance 的影响。（3）**中期可做**：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，特别是多源约束下的 efficiency bound 推导；目前 paper 缺乏显式的渐近理论，这正是可以切入的理论贡献点。

### 2. [10.1093/biomtc/ujae003](https://doi.org/10.1093/biomtc/ujae003) — Merging or ensembling: integrative analysis in multiple neuroimaging studies
- **作者**: Yue Shan, Chao Huang, Yun Li, Hongtu Zhu
- **期刊/来源**: Biometrics
- **机构**: University of North Carolina at Chapel Hill · Florida State University
- **分类**: vol 80 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文系统研究了在多个神经影像研究中对空间变系数混合效应模型（SVCMEM）进行整合学习的合并（merging）与集成（ensembling）方法。合并方法将全部研究数据合并训练一个全局模型，集成方法则分别训练各研究模型后加权平均。作者在有异质性的设定下，渐近地比较了两类学习器的预测精度，并给出了选择策略与集成最优权重的理论指导。模拟实验和三个大规模神经影像数据集验证了理论。对您而言，多研究整合框架与流行病学中合并队列的分析需求相通，但本方法基于 SVCMEM 而非您更熟悉的因果推断或半参数工具，因此属于认知拓展性阅读。
- **关键技术**: `Spatially Varying Coefficient Mixed Effects Models (SVCMEM)`, `Merged learner`, `Ensemble learner`, `Optimal weight asymptotics`, `Multi-study integration`
- **为什么对您有用**: 论文属于流行病学方向的多研究数据整合主题，对应您的 secondary interest。您技术武器库中的非参数统计理论可用于分析 SVCMEM 的收敛性，但混合效应与空间相关性的细节需要额外学习。这属于中期可做领域：需先补充线性混合模型和空间统计的渐近理论，再考虑迁移至因果推断中的多中心合并分析。

### 3. [10.1093/biomtc/ujad001](https://doi.org/10.1093/biomtc/ujad001) — Homogeneity pursuit and variable selection in regression models for multivariate abundance data
- **作者**: Francis K C Hui, Luca Maestrini, Alan H Welsh
- **期刊/来源**: Biometrics
- **机构**: Australian National University
- **分类**: vol 80 · issue 1
- 相关性 4/10 · novelty: `application`
- **摘要**: 该论文针对生态学多变量丰度数据的回归建模问题，提出了一种基于广义估计方程（GEE）的同时同质性追踪与变量选择方法。目标是在物种-环境关系中对每个协变量上的物种系数进行聚类（同质性），并实现不同协变量的稀疏性选择。方法上，在GEE框架中引入自适应fused lasso惩罚以实现系数聚类，同时使用自适应lasso惩罚来鼓励跨协变量的不同稀疏水平，并通过（降秩）工作相关矩阵处理物种间的相关性。数值模拟表明，该方法在有限样本下优于几种现有方法。将该方法应用于澳大利亚大堡礁的海底生物存在-缺失数据，揭示了物种-环境关系中明显的同质性和稀疏性，从而得到更简洁且具有更强预测性能的模型。该方法属于高维变量选择与聚类分析的交叉应用，与您在高维统计和惩罚估计方向的兴趣有一定关联，但并非因果推断或半参效率理论的核心问题。
- **关键技术**: `generalized estimating equations`, `adaptive fused lasso`, `adaptive lasso`, `variable selection`, `homogeneity pursuit`, `working correlation matrix`
- **为什么对您有用**: 本文涉及高维变量选择与系数聚类，可连接您在高维统计中变量选择方法的兴趣；您非常熟悉的高维渐近性工具可用于分析惩罚GEE估计量的收敛速率及oracle性质。不过，核心方法基于GEE和fused lasso优化，当前武器库对这方面的算法与理论覆盖不足，属于暂不可做——需要先掌握惩罚估计的优化理论和fused lasso的渐近性质，才能对该方法进行深入分析或改进。

### 4. [10.1093/biomtc/ujad022](https://doi.org/10.1093/biomtc/ujad022) — A generalized phase 1-2-3 design integrating dose optimization with confirmatory treatment comparison
- **作者**: Yong Zang, Peter F Thall, Ying Yuan
- **期刊/来源**: Biometrics
- **机构**: Indiana University – Purdue University Indianapolis · The University of Texas MD Anderson Cancer Center
- **分类**: vol 80 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文提出一种广义的Phase 1-2-3临床试验设计（Gen 1-2-3），整合剂量优化与验证性治疗比较。设计从Phase 1-2试验开始，使用剂量可接受性和最优性标准识别一组候选剂量（而非单个剂量），然后在中间阶段将额外患者随机分配至候选剂量和活性对照治疗组，利用两阶段生存数据选择最优剂量。随后基于所选最优剂量对比对照的预测概率做出是否进入Phase 3的Go/No Go决策。模拟研究表明，与CT设计及两种传统设计相比，Gen 1-2-3设计具有更优的操作特征。该设计主要针对临床试验中的序贯决策问题，方法学贡献在于阶段间信息整合与预测概率驱动的决策机制。
- **关键技术**: `Bayesian predictive probability`, `dose optimization`, `phase 1-2-3 design`, `survival analysis`, `randomized allocation`
- **为什么对您有用**: 本文属于临床试验设计方法学，与您的主要兴趣（因果推断、高维统计、半参数效率等）直接关联较弱。但作为Biometrics上的应用方法论文，其设计思路（多阶段信息整合、基于预测概率的决策）可能对您关注的流行病学或应用因果工作中的序贯随机化设计有间接参考价值。从武器库看，您当前的工具（非参数统计、因果推断估计）无法直接攻入该问题核心，因为该方法高度依赖贝叶斯预测概率和生存模型，而您对此不熟悉（暂不可做）。因此本文不值得全文精读，快速浏览设计框架即可。

### 5. [10.1093/biomtc/ujad019](https://doi.org/10.1093/biomtc/ujad019) — A flexible framework for spatial capture-recapture with unknown identities
- **作者**: Paul van Dam-Bates, Michail Papathomas, Ben C Stevenson, Rachel M Fewster, Daniel Turek, Frances E C Stewart et al.
- **期刊/来源**: Biometrics
- **机构**: University of St Andrews · University of Auckland · Williams College · Wilfrid Laurier University · University of Cape Town
- **分类**: vol 80 · issue 1
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文在空间捕获-重捕获（SCR）框架下，解决野生动物个体无法唯一识别时的种群密度估计问题。核心设定是将 SCR 建模为 marked Poisson process，包含一个计数过程（所有动物的检测）和一个 mark 分布（观测到的标记，如身份、性别、到达时间）。当个体身份未知时，观测到的 mark 来自由活动中心和其他特征定义的 mark 分布的混合分布，通过 latent identity 模型进行推断。方法统一了现有 latent identity SCR 模型和声学 SCR，在贝叶斯框架下使用 MCMC 进行计算。应用于 fisher 相机陷阱数据和 Cape Peninsula moss frog 声学调查数据，模拟显示加入额外 mark（如性别、到达时间）可提高密度估计的可靠性。对您而言，这是生态学领域的应用统计论文，方法学 novelty 有限。
- **关键技术**: `spatial capture-recapture`, `marked Poisson process`, `latent identity model`, `mixture mark distribution`, `Bayesian MCMC inference`
- **为什么对您有用**: 本文属于生态学应用统计，与您 primary interests（因果推断、高维统计、效率理论等）无直接方法学连接。技术核心是 marked Poisson process 和 latent identity mixture model，属于经典空间点过程与分层贝叶斯模型，不涉及 semiparametric efficiency、high-dimensional theory 或 causal identification 等您熟悉的工具。novelty_flag 为 application，主要是框架整合与实证应用。follow-up 判定：暂不可做——核心机器不在武器库内，且与您当前研究议程无交叉点。

### 6. [10.1093/biomtc/ujae002](https://doi.org/10.1093/biomtc/ujae002) — Semisupervised transfer learning for evaluation of model classification performance
- **作者**: Linshanshan Wang, Xuan Wang, Katherine P Liao, Tianxi Cai
- **期刊/来源**: Biometrics
- **机构**: Harvard University · University of Utah · Brigham and Women's Hospital
- **分类**: vol 80 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在协变量分布发生 shift 且目标人群缺乏标签的设定下，本文研究如何将已训练二分类器的 ROC 曲线参数从源人群迁移到目标人群。核心 estimand 是目标人群上的 TPR/FPR 及 ROC 曲线，关键假设是 covariate shift（条件结局分布 P(Y|X) 不变）与源-目标数据的可识别性。提出的 STEAM 方法采用三步估计：double-index 密度比建模构造校准权重、robust imputation 利用无标签数据提升效率、cross-fitting 校正有限样本过拟合偏差。理论证明在密度比模型或结局模型任一正确设定下，估计量具有 consistency 与 n^{-1/2}-CAN 性质，达到 semiparametric efficiency 的双稳健性。模拟显示相较现有方法有 bias 降低与效率提升，RA 表型模型的 EHR 时序队列实证展示了方法实用性。对您而言，这是 semiparametric efficiency 理论在迁移学习场景的具体应用，双稳健估计与 influence function 技术可直接迁移。
- **关键技术**: `double robust estimation`, `density ratio estimation`, `semiparametric efficiency bound`, `influence function`, `covariate shift adaptation`, `cross-fitting`
- **为什么对您有用**: 直接连接 semiparametric efficiency 理论（primary interest），展示了 influence function 与 double robustness 在迁移学习/协变量偏移场景的具体实现。您可以用 very_familiar 的 semiparametric theory 和 minimax bound 工具审视其效率声称是否紧、双稳健条件是否可进一步放松；moderately_familiar 的 HOIF 理论可能用于探索更高阶效率改进。**立即可做**：用现有 semiparametric 武器验证其 efficiency bound 推导、考察 influence function 构造的完备性。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

