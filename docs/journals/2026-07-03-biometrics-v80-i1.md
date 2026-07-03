# Biometrics — Vol 80  Issue 1  ·  2026-07-03

- 共 43 篇 · Biometrics
- 目录核对 ⚠️ 疑似漏 12 篇（对照 OpenAlex 60 篇）：10.1093/biomtc/ujad020、10.1093/biomtc/ujad015、10.1093/biomtc/ujad009、10.1093/biomtc/ujae007、10.1093/biomtc/ujad003 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Biometrics》第80卷第1辑共收录43篇论文，整体上可归纳为四条主线：**因果识别与估计**（约10篇，涉及工具变量中介分析、主分层、动态治疗方案、迁移学习等）、**半参数/非参数方法与效率理论**（约6篇，涵盖两阶段设计、纵向数据建模、非参数预测等）、**高维与结构化数据建模**（约8篇，包括降秩回归、图引导贝叶斯、稀疏vine copula等）、以及**假设检验与试验设计**（约5篇，涉及FDP不确定性、序贯监测、适应性设计等）。此外，还有若干流行病学应用与计算方法的独立工作。

在因果推断主线中，最突出的推进是**工具变量与中介分析的结合**。Using instrumental variables to address unmeasured confounding in causal mediation analysis 提出了双重依从者干预直接效应和间接效应，利用两个可能相关的IV分别处理暴露和中介的未观测混杂，填补了IV用于中介效应识别的空白，其非参数识别和高效影响函数估计与半参效率理论直接对接。另一篇Principal stratification analysis of noncompliance with time-to-event outcomes 则将主分层框架扩展到时间-事件结局，定义了complier平均因果效应并给出非参数识别条件。在动态治疗方案方面，Multiobjective tree-based reinforcement learning for estimating tolerant dynamic treatment regimes 引入了容忍率概念，通过多目标树强化学习输出多个可行决策规则集合，其半参数增广逆概率加权估计量兼顾了鲁棒性与可解释性。此外，Adaptive selection of the optimal strategy to improve precision and power in randomized trials 将TMLE与交叉验证结合，在大规模试验中自动选择最优协变量调整策略，实现了20%-43%的样本量缩减，其核心机制是估计影响曲线平方作为损失函数。

半参数/非参数方法主线中，**两阶段设计与效率提升**是反复出现的主题。Efficient designs and analysis of two-phase studies with longitudinal binary data 提出了残差依赖抽样设计，在半参数似然框架下开发了数值稳定的EM算法，相比简单随机抽样显著提升估计精度。Two-phase designs with failure time processes subject to nonsusceptibility 针对存在治愈分组的失效时间数据，提出了双变量残差依赖设计，在联合建模治愈概率和失效时间时实现高效子抽样。Robust data integration from multiple external sources for generalized linear models with binary outcomes 则通过自适应惩罚方法处理外部研究的人群异质性，利用遗漏变量偏差的显式形式构建惩罚项，自动对不兼容信息降权，实现了双重稳健整合。在纵向数据方面，Nonparametric predictive model for sparse and irregular longitudinal data 利用核方法基于预测变量轨迹的相似性构造权重，其乘性高斯核模型同时实现降维和函数协变量筛选，推导了渐近性质。

与因果推断/半参数效率/高维方向最贴合的论文包括：Using instrumental variables to address unmeasured confounding in causal mediation analysis（IV与中介分析）、Principal stratification analysis of noncompliance with time-to-event outcomes（主分层与时间-事件因果效应）、Adaptive selection of the optimal strategy to improve precision and power in randomized trials（TMLE与交叉验证效率提升）、Robust data integration from multiple external sources for generalized linear models with binary outcomes（双重稳健整合与自适应惩罚）、以及Multiple augmented reduced rank regression for pan-cancer analysis（结构化核范数与随机矩阵理论在高维回归中的应用）。

## 因果推断  *(causal_inference, 16 篇)*

### 1. [10.1093/biomtc/ujad037](https://doi.org/10.1093/biomtc/ujad037) — Using instrumental variables to address unmeasured confounding in causal mediation analysis
- **作者**: Kara E Rudolph, Nicholas Williams, Iván Díaz
- **期刊/来源**: Biometrics
- **机构**: Columbia University · New York University
- **分类**: vol 80 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在因果中介分析中处理未观测混杂问题，提出使用两个（可能相关的）工具变量分别针对暴露和中介变量，定义并非参数识别了新的 estimand——双重依从者干预直接效应和间接效应。该方法扩展了 IV 方法在总效应识别之外的用途，填补了 IV 用于中介效应识别的空白。估计量采用非参数、稳健且高效的框架，可能基于高效影响函数或类似 DML 的构造。应用部分使用住房券实验数据展示了方法的实用性。对您而言，本文直接连接您对因果推断中 IV 和中介分析的 interest，且其非参数识别和高效估计思路与您的 semiparametric theory 和 efficiency theory 高度相关。
- **关键技术**: `instrumental variables`, `mediation analysis`, `nonparametric identification`, `efficient estimation`, `complier interventional effects`
- **为什么对您有用**: 本文直接连接您 primary interest 中的 causal inference 子方向（IV 和中介分析），且其非参数识别和高效估计框架与您的 semiparametric theory 和 efficiency theory 高度相关。您可以用 very_familiar 的 nonparametric statistics 和 estimation theory in causal inference 来理解其识别策略，并进一步用 moderately_familiar 的 semiparametric theory 和 identification theory 来评估其效率界或提出改进。中期可做：若想深入推导其 semiparametric efficiency bound，需先在 moderately_familiar 的 semiparametric theory 上加强。

### 2. [10.1093/biomtc/ujad034](https://doi.org/10.1093/biomtc/ujad034) · [arXiv](https://arxiv.org/abs/2210.17453) — Adaptive selection of the optimal strategy to improve precision and power in randomized trials
- **作者**: Laura B Balzer, Erica Cai, Lucas Godoy Garraza, Pracheta Amaranath
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对随机对照试验中基线协变量调整的策略选择问题，目标是在控制第一类错误的前提下最大化估计精度。方法基于Balzer等人先前提出的Adaptive Pre-specification框架，将其扩展到大规模试验场景：使用V折交叉验证和估计影响曲线平方作为损失函数，从包含现代机器学习方法的扩展候选集中自动选择最优调整策略。核心机制是TMLE（Targeted Maximum Likelihood Estimation）与交叉验证的结合，通过影响函数实现效率增益的评估与选择。模拟研究表明，该方法在多种数据生成过程下均能保持第一类错误控制，并将精度提升转化为20%-43%的样本量缩减。在ACTG Study 175真实数据应用中，整体及亚组分析均观察到有意义的效率改进。对您而言，该工作直接关联因果推断中的估计效率提升问题，其交叉验证选择策略与您熟悉的非参数统计和因果推断估计理论高度契合。
- **关键技术**: `Targeted Maximum Likelihood Estimation (TMLE)`, `cross-validation`, `influence curve`, `adaptive pre-specification`, `covariate adjustment`
- **为什么对您有用**: 本文直接关联您primary interest中的因果推断估计效率问题，特别是随机试验中协变量调整的自动化选择。您very_familiar中的非参数统计和因果推断估计理论可直接用于理解其TMLE框架和影响函数机制，而moderately_familiar中的HOIF和半参数理论可进一步分析其选择策略的渐近性质。立即可做：基于您对非参数统计和因果推断估计的熟悉程度，可立即复现其模拟框架并探索更复杂的候选调整策略。

### 3. [10.1093/biomtc/ujad016](https://doi.org/10.1093/biomtc/ujad016) — Principal stratification analysis of noncompliance with time-to-event outcomes
- **作者**: Bo Liu, Lisa Wruck, Fan Li
- **期刊/来源**: Biometrics
- **机构**: Duke University · Clinical Research Institute
- **分类**: vol 80 · issue 1
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文针对临床试验中常见的不依从性问题（非依从性），在时间-事件结局（time-to-event）的设定下发展主分层分析（principal stratification）框架。目标 estimand 是 treatment 对 time-to-event outcome 的因果效应，在 principal strata（如 always-taker, complier, never-taker）上定义。作者给出了两个具体的因果 estimand（如 complier average causal effect on survival）及其非参数识别公式。估计方面采用潜变量混合模型（latent mixture modeling），具体使用 Bayesian 参数化 Weibull-Cox 比例风险模型作为 outcome 模型，并利用 Stan 编程语言实现自动后验采样。对于因果 estimand 作为模型参数的函数，提供了解析形式；当解析形式不可得时，给出数值计算方法。方法应用于 ADAPTABLE 试验，比较 81 mg 与 325 mg 阿司匹林对主要不良心血管事件风险的影响，并开发了 R 包 PStrata。对您而言，本文是主分层框架在生存分析中的系统化应用，其识别策略和 Bayesian 实现思路可迁移至您 causal inference 方向中的 longitudinal 或 mediation 设定。
- **关键技术**: `principal stratification`, `latent mixture modeling`, `Weibull-Cox proportional hazards model`, `Bayesian posterior sampling (Stan)`, `nonparametric identification`
- **为什么对您有用**: 本文直接对应您 primary interest 中 causal inference 的 longitudinal 子方向，具体处理 time-to-event 下的非依从性问题。您的 technical arsenal 中 'estimation theory in causal inference' 和 'identification theory in causal inference' 均属 very_familiar，可立即用于评估其识别假设的合理性及扩展至更复杂的 longitudinal 结构（如时变依从性）。中期可做：若想将本文的 Bayesian 混合模型与您 moderately_familiar 的 semiparametric theory 结合（如推导半参数效率界），需先在 'semiparametric theory' 上长肌肉。

### 4. [10.1093/biomtc/ujad026](https://doi.org/10.1093/biomtc/ujad026) — Bayesian nonparametric for causal inference and missing data by Michael J. Daniels, Antonio Linero, and Jason Roy, CRC Press, 2023 ISBN-13: 978-0367341008, https://www.routledge.com/Bayesian-Nonparametrics-for-Causal-Inference-and-Missing-Data/Daniels-Linero-Roy/p/book/9780367341008
- **作者**: Li-Pang Chen
- **期刊/来源**: Biometrics
- **机构**: National Chengchi University
- **分类**: vol 80 · issue 1
- 相关性 7/10 · novelty: `survey`
- **摘要**: 本文是对《Bayesian Nonparametrics for Causal Inference and Missing Data》一书的书评，该书系统介绍了利用贝叶斯非参数方法进行因果推断和缺失数据处理。全书15章分为三大主题：主题I（第1-4章）概述因果推断基础（g-formula、倾向性评分、边际结构模型、因果中介）、缺失数据机制（MCAR/MAR/MNAR及选择模型、模式混合模型、共享参数模型）和贝叶斯方法（MCMC、Gibbs采样、Hamiltonian Monte Carlo）及可识别性问题。主题II（第5-10章）聚焦贝叶斯非参数方法，包括狄利克雷过程混合模型、高斯过程先验、回归树（BART）等，并讨论其在因果效应估计和缺失数据插补中的应用。主题III（第11-15章）涵盖纵向数据、动态治疗方案的因果推断，以及敏感性分析和模型诊断。该书的一个关键优势是包含大量真实数据案例研究，帮助读者理解方法在实际数据集上的应用。对您而言，这是一本将贝叶斯非参数工具（如BART、狄利克雷过程）系统引入因果推断和缺失数据领域的专著，尤其适合您作为因果推断研究者了解贝叶斯视角下的识别与估计策略，但本书侧重综述而非新理论或新方法。
- **关键技术**: `Bayesian nonparametrics`, `Dirichlet process mixture`, `Gaussian process prior`, `BART (Bayesian Additive Regression Trees)`, `g-formula`, `propensity score`
- **为什么对您有用**: 本文是书评，直接对应您primary interest中的因果推断（identification、estimation）和缺失数据处理。本书系统介绍了贝叶斯非参数方法在因果推断中的应用，包括g-formula、倾向性评分、边际结构模型等经典框架的贝叶斯版本，以及BART、狄利克雷过程等工具。作为综述性专著，它适合作为您进入贝叶斯因果推断领域的入门读物，但方法学novelty程度较低。武器库方面：您对非参数统计和因果推断的估计理论非常熟悉，可以快速理解书中技术内容；但贝叶斯非参数的具体计算（如MCMC后验采样）属于moderately_familiar领域，需先熟悉狄利克雷过程和BART的算法细节才能动手复现案例。总体而言，这是一本值得通读的参考书，但非立即可做的前沿研究。

### 5. [10.1093/biomtc/ujae018](https://doi.org/10.1093/biomtc/ujae018) — Fitting the Cox proportional hazards model to big data
- **作者**: Jianqiao Wang, Donglin Zeng, Dan-Yu Lin
- **期刊/来源**: Biometrics
- **机构**: University of North Carolina at Chapel Hill
- **分类**: vol 80 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对大规模生存数据（百万级样本）下的Cox比例风险模型拟合问题，提出一种计算高效的估计方法。核心思路是：先在全数据的一个小子集上计算最大偏似然估计（MPLE）作为初始估计，然后利用剩余数据通过一步估计（one-step estimation）结合估计的有效得分函数（estimated efficient score function）来改进初始估计。该方法的关键在于，最终估计量在渐近分布上与基于全数据的传统MPLE等价，但计算时间仅为其一小部分。理论证明基于半参数效率理论，给出了估计量的渐近正态性和效率。模拟研究和UK Biobank数据应用验证了方法的实用性和计算优势。对您而言，该方法将半参数效率理论与大规模计算问题结合，其one-step框架可迁移至因果推断中的高效估计（如DML中的cross-fitting思想），且与您对软件开发和计算效率的兴趣直接相关。
- **关键技术**: `one-step estimation`, `efficient score function`, `Cox proportional hazards model`, `maximum partial likelihood estimation`, `subsampling`
- **为什么对您有用**: 本文连接您的primary interest中的效率理论（semiparametric efficiency bounds）和统计计算（大规模数据下的算法设计）。您武器库中'very_familiar'的'nonparametric statistics'和'estimation theory in causal inference'可直接用于理解其one-step估计的渐近理论；'moderately_familiar'的'semiparametric theory'可帮助您评估其efficient score的构造是否最优。**中期可做**：若想将类似框架推广到因果推断中的生存数据（如Cox模型下的ATE估计），需先在'semiparametric theory'上进一步熟练。

### 6. [10.1093/biomtc/ujad012](https://doi.org/10.1093/biomtc/ujad012) — Individualized treatment rule characterization via a value function surrogate
- **作者**: Nikki L B Freeman, Sydney E Browder, Katharine L McGinigle, Michael R Kosorok
- **期刊/来源**: Biometrics
- **机构**: University of North Carolina at Chapel Hill
- **分类**: vol 80 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对外周动脉疾病患者伤口管理中的部分依从性情境，提出了一种通过高斯过程代理价值函数来学习最优个体化治疗规则的方法。研究利用贝叶斯优化在价值函数上搜索最优策略，并进一步扩展至对个体化治疗规则类别的刻画，以增强临床可解释性。方法核心在于将价值函数视为黑箱目标，通过高斯过程建模其不确定性，并利用采集函数指导策略搜索。理论贡献在于展示了贝叶斯优化在有限样本下学习最优策略的可行性，同时提供了将复杂策略转化为临床可操作规则的系统框架。实证部分基于真实临床数据验证了方法的有效性。对您而言，本文的价值在于其将因果推断中的价值函数优化与贝叶斯非参数工具结合，属于您 moderately_familiar 的因果推断识别理论在临床决策中的具体应用，可作为中期可做的方向——需先在非参数贝叶斯优化上补充知识。
- **关键技术**: `Bayesian optimization`, `Gaussian process surrogate`, `value function`, `individualized treatment rule`, `precision medicine`
- **为什么对您有用**: 本文直接关联您 primary interest 中的因果推断（个体化治疗规则学习），并使用了您 very_familiar 的非参数统计工具（高斯过程）来代理价值函数。方法上，贝叶斯优化与您 moderately_familiar 的因果推断识别理论可结合，例如在部分依从性下利用工具变量识别价值函数。中期可做：需先熟悉贝叶斯优化的采集函数设计（如 EI、UCB），这是您武器库中目前缺失的一环。

### 7. [10.1093/biomtc/ujad028](https://doi.org/10.1093/biomtc/ujad028) · [arXiv](https://arxiv.org/abs/2101.09304) — The central role of the identifying assumption in population size estimation
- **作者**: Serge Aleshin-Guendel, Mauricio Sadinle, Jon Wakefield
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文重新审视了多系统估计（capture-recapture）中的识别假设问题。作者指出，在缺失数据框架下，未观测个体数（即总体大小）的估计完全依赖于一个不可检验的识别假设，而不同识别假设即使对观测数据拟合相同，也可能导致任意不同的总体大小估计。现有方法往往不明确指定识别假设，使得观测数据模型与识别假设难以解耦。本文提出一种新的框架，将观测数据模型与识别假设明确分离，并展示了常见模型如何纳入该框架。该方法可利用现有软件实现，并便于进行多种敏感性分析。通过科索沃战争平民伤亡人数的案例研究，作者展示了该方法的实际应用。对您而言，本文在识别假设的显式化与敏感性分析方面与proximal causal inference中的negative control假设检验思路高度相关，属于identification theory在缺失数据问题中的直接延伸。
- **关键技术**: `multiple-systems estimation`, `identifying assumption`, `sensitivity analysis`, `missing data framework`, `capture-recapture`
- **为什么对您有用**: 本文直接关联到primary interest中的identification theory in causal inference，特别是识别假设的显式化与敏感性分析。您可以用very_familiar的estimation theory in causal inference工具来审视其识别假设的合理性，并考虑将proximal CI中的negative control思路迁移到多系统估计的识别假设检验中。属于中期可做：需先在moderately_familiar的identification theory上进一步熟悉缺失数据框架下的识别策略。

### 8. [10.1093/biomtc/ujad039](https://doi.org/10.1093/biomtc/ujad039) — Inferring a directed acyclic graph of phenotypes from GWAS summary statistics
- **作者**: Rachel Zilinskas, Chunlin Li, Xiaotong Shen, Wei Pan, Tianzhong Yang
- **期刊/来源**: Biometrics
- **机构**: Iowa State University · University of Minnesota
- **分类**: vol 80 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文提出一种从GWAS汇总统计量推断表型有向无环图（DAG）的方法。在假设高斯线性结构方程模型嵌入DAG的设定下，利用遗传变异作为工具变量（IV），仅需GWAS汇总统计量和基因型参考面板即可进行估计。方法的核心是构建基于汇总统计量的似然比检验，用于检验有向边的存在性，这是区别于现有方法的独特特征。模拟研究验证了方法的有效性，并将该方法应用于29个心血管相关蛋白的因果网络估计，进一步将估计网络与阿尔茨海默病（AD）关联分析。作者提供了R包sumdag及Shiny应用，便于复现和应用。该方法为因果推断中IV与DAG的结合提供了实用工具，尤其适用于遗传流行病学中的表型网络分析。
- **关键技术**: `instrumental variables`, `directed acyclic graph (DAG)`, `Gaussian linear structural equation model`, `likelihood ratio test`, `GWAS summary statistics`, `R package sumdag`
- **为什么对您有用**: 本文直接连接您的primary interest中的因果推断（IV与DAG识别）和流行病学应用。技术层面，您可以用very_familiar的估计理论（如IV估计的渐近性质）和high-dimensional asymptotics来评估其估计量的统计性质，例如检验统计量的分布近似或高维基因变异下的相合性。中期可做：若想深入其似然比检验的semiparametric效率，需先在moderately_familiar的semiparametric theory上提升（如部分线性IV模型的半参效率界）。

### 9. [10.1093/biomtc/ujad007](https://doi.org/10.1093/biomtc/ujad007) · [arXiv](https://arxiv.org/abs/2212.02422) — Adaptive sequential surveillance with network and temporal dependence
- **作者**: Ivana Malenica, Jeremy R Coyle, Mark J van der Laan, Maya L Petersen
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文研究传染病监测中的自适应序贯检测分配问题，目标是在资源约束下最大化检测阳性结果。因果参数定义为在给定历史信息后，实施某种随机干预（stochastic intervention）所得到的潜在结果均值。核心挑战在于个体间存在网络依赖和时间依赖，使得数据退化为单一观测。方法的关键是不对网络和时间依赖结构做显式建模，而是使用短期性能在线超级学习器（Online Super Learner）在依赖模型和随机化方案之间进行选择。该策略能够随时间自适应地学习最优检测分配，并跨样本或跨时间进行学习。在模拟COVID-19疫情期间大学宿舍环境的基于智能体的仿真中，该方法展现出优越性能。对您而言，本文展示了在复杂依赖结构下进行因果推断和自适应设计的实际应用，与您对纵向因果推断和流行病学应用的兴趣直接相关。
- **关键技术**: `Online Super Learner`, `adaptive sequential design`, `stochastic intervention`, `network dependence`, `temporal dependence`, `agent-based simulation`
- **为什么对您有用**: 本文直接关联您的流行病学应用兴趣，展示了在具有网络和时间依赖的纵向数据中如何进行因果推断和自适应设计。您的武器库中'因果推断中的估计理论'和'软件工程'可直接用于复现或改进其在线学习器策略；'非参数统计'可用于分析其依赖模型选择的理论性质。中期可做：若先熟悉'纵向因果推断的识别理论'，可进一步研究其随机干预的识别条件。

### 10. [10.1093/biomtc/ujad010](https://doi.org/10.1093/biomtc/ujad010) — Efficient designs and analysis of two-phase studies with longitudinal binary data
- **作者**: Chiara Di Gravio, Jonathan S Schildcrout, Ran Tao
- **期刊/来源**: Biometrics
- **机构**: Imperial College London · Vanderbilt University Medical Center
- **分类**: vol 80 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对纵向二元结局与昂贵生物标志物暴露之间的关联估计问题，提出了一类新的残差依赖抽样（RDS）设计，作为两阶段研究的成本有效方案。在第一阶段，利用纵向结局和廉价协变量的数据，基于残差选择信息量大的个体进行暴露测量；第二阶段对选定子集测量昂贵暴露。分析方法上，作者开发了一个半参数似然框架，并设计了数值稳定且计算高效的EM算法来最大化该似然，从而有效整合两阶段数据。通过模拟研究，论文展示了RDS设计相比现有设计（如简单随机抽样、基于结局的抽样）在估计精度上的提升，并验证了所提分析方法的有限样本性能。最后，在肺健康研究中应用该方法，分析了遗传标记与肺功能不良的关联。对您而言，本文的核心价值在于其两阶段抽样设计结合半参数似然估计的思路，可直接迁移至您熟悉的因果推断中昂贵协变量或暴露的测量成本约束问题（如IV或mediation中的生物标志物），且其EM算法与您软件开发的技能点高度契合。
- **关键技术**: `residual-dependent sampling`, `two-phase study`, `semiparametric likelihood`, `EM algorithm`, `longitudinal binary data`
- **为什么对您有用**: 本文属于流行病学应用（secondary interest），其两阶段抽样设计（RDS）与半参数似然估计方法，直接对应您在因果推断中处理昂贵暴露测量成本的实际需求（如IV或mediation中的生物标志物）。您武器库中'非参数统计'和'估计理论'的功底可用来评估其RDS设计的最优性（例如，是否达到半参效率界），而'软件开发'技能可直接复现或扩展其EM算法。中期可做：若想将RDS推广至因果推断的ATE估计，需先在'moderately_familiar'的'identification theory'上加强，理解在纵向设定下如何将RDS与g-formula或IPW结合。

### 11. [10.1093/biomtc/ujad005](https://doi.org/10.1093/biomtc/ujad005) — Robust data integration from multiple external sources for generalized linear models with binary outcomes
- **作者**: Kyuseong Choi, Jeremy M G Taylor, Peisong Han
- **期刊/来源**: Biometrics
- **机构**: Cornell University · University of Michigan
- **分类**: vol 80 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究在内部研究（internal study）之外，有多个外部研究（external studies）提供基于不同协变量子集的GLM参数估计（summary information）时，如何高效且稳健地估计二值结局的GLM参数。核心挑战是外部研究可能与内部研究存在人群分布异质性（population heterogeneity），直接整合会引入偏差。作者提出一种自适应惩罚方法（adaptive penalization），利用GLM参数与遗漏协变量后参数之间的关系（即omitted-variable bias的显式形式）来构建惩罚项，自动对与内部数据不兼容的外部信息降权，从而实现稳健整合。该方法在计算上通过自适应权重和信息准则（如BIC）选择最优惩罚参数，避免了交叉验证的昂贵计算。理论分析证明了估计量的渐近正态性和效率增益。模拟显示，在多种异质性模式下，该方法均优于直接MLE，且接近理想情况下的最优效率。应用案例是整合两个外部模型的前列腺癌风险预测参数，改进内部logistic回归模型。该问题与您关注的因果推断中数据融合（data integration）和迁移学习（transfer learning）密切相关，其利用omitted-variable bias结构进行稳健估计的思路，对您处理proximal CI或IV中多源数据整合有直接参考价值。
- **关键技术**: `adaptive penalization`, `omitted-variable bias`, `summary-level data integration`, `information criterion tuning`, `generalized linear model`
- **为什么对您有用**: 本文属于因果推断中数据融合/迁移学习的应用方法，直接连接到您primary interest中的identification theory和estimation theory。技术上看，其利用omitted-variable bias的显式形式进行稳健整合，这一思路可迁移到您moderately_familiar的identification theory中处理unmeasured confounding时的多源数据场景（如proximal CI中的negative control）。中期可做：若您想将类似方法推广到proximal CI框架，需先在moderately_familiar的identification theory上深入理解proximal g-formula的识别条件，然后可尝试用类似惩罚思路处理多个proxy变量的整合。

### 12. [10.1093/biomtc/ujae002](https://doi.org/10.1093/biomtc/ujae002) — Semisupervised transfer learning for evaluation of model classification performance
- **作者**: Linshanshan Wang, Xuan Wang, Katherine P Liao, Tianxi Cai
- **期刊/来源**: Biometrics
- **机构**: Harvard University · University of Utah · Brigham and Women's Hospital
- **分类**: vol 80 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究在目标人群无标签、源人群有标签的迁移学习设定下，如何评估一个已训练二分类器的ROC性能（AUC、灵敏度、特异度等）。核心挑战是协变量分布在源和目标人群间漂移，且目标人群缺乏真实标签。作者提出STEAM三步估计法：第一步用双指标模型（double-index modeling）估计密度比权重，校准分布偏移；第二步用稳健插补（robust imputation）利用大量无标签目标数据提升效率；第三步结合交叉验证校正过拟合偏差。理论部分证明了估计量的相合性和渐近正态性，且只要密度比模型或结果模型之一正确指定，估计量即一致（双重稳健性）。模拟显示STEAM相比现有方法显著降低偏差并提升效率；实例应用于类风湿性关节炎表型模型在时间演变的EHR队列上的性能评估。对您而言，该文将迁移学习与因果推断中的双重稳健思想（类似DR估计）结合，且处理的是性能度量（而非模型参数）的迁移，与您的proximal CI和效率理论兴趣有直接技术交集。
- **关键技术**: `double-index modeling`, `density ratio weighting`, `robust imputation`, `double robustness`, `cross-fitting`, `ROC analysis`
- **为什么对您有用**: （1）直接连接到您的primary interest中的因果推断（迁移学习中的分布偏移可视为一种confounding by population，密度比权重类似IPW）和效率理论（双重稳健估计、交叉验证）。（2）武器库中very_familiar的'nonparametric statistics'和'estimation theory in causal inference'可直接用于分析其密度比模型的估计误差传播；moderately_familiar的'identification theory in causal inference'可用于思考其识别假设（如positivity、density ratio模型的可识别性）是否可放松。（3）中期可做：若想将STEAM扩展到proximal CI框架下处理未测量混淆，需先在moderately_familiar的'identification theory'上深入理解negative control假设。

### 13. [10.1093/biomtc/ujae020](https://doi.org/10.1093/biomtc/ujae020) — Conditional modeling of panel count data with partly interval-censored failure event
- **作者**: Xiangbin Hu, Wen Su, Zhisheng Ye, Xingqiu Zhao
- **期刊/来源**: Biometrics
- **机构**: Hong Kong Polytechnic University · City University of Hong Kong · National University of Singapore
- **分类**: vol 80 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究纵向随访中面板计数数据与部分区间删失失效事件的条件建模问题。失效事件对复发事件具有信息性，现有方法基于潜变量模型，对失效事件效应的解释间接。作者提出一个失效时间依赖的比例均值模型，通过未指定链接函数直接刻画失效事件对复发事件的影响。为处理部分区间删失，构造条件期望最小二乘函数，并采用两阶段估计：将失效时间分布视为函数型 nuisance 参数，用 B 样条逼近未知基线均值函数和链接函数。推导了有限维估计量的渐近正态性和无穷维估计量泛函的收敛速率。模拟验证了有限样本性质与理论一致，并在长寿纵向研究中得到应用。对您而言，本文的纵向因果推断设定（信息性删失、部分区间删失）与您的 causal inference（longitudinal）和 semiparametric theory 直接相关，其两阶段 B 样条估计与收敛率分析可视为非参数工具在复杂删失数据下的一个应用案例。
- **关键技术**: `conditional expectation least squares`, `B-spline approximation`, `two-stage estimation`, `partly interval-censored failure event`, `proportional mean model`, `functional nuisance parameter`
- **为什么对您有用**: 本文属于纵向因果推断中信息性删失问题的建模与估计，直接连接到 primary interest 的 causal inference（longitudinal）和 semiparametric & nonparametric theory。技术层面，其两阶段估计与 B 样条逼近可被 very_familiar 的 nonparametric statistics 和 estimation theory in causal inference 工具攻破——例如用 minimax bounds 验证其收敛率是否最优，或考虑用 higher-order U-statistics 的 treewidth 视角分析其估计量的计算成本。中期可做：若想将本文方法推广到更一般的因果 estimand（如动态 treatment 效应），需先在 moderately_familiar 的 identification theory in causal inference 上长肌肉。

### 14. [10.1093/biomtc/ujad011](https://doi.org/10.1093/biomtc/ujad011) — Proportional rates models for multivariate panel count data
- **作者**: Yangjianchen Xu, Donglin Zeng, Dan-Yu Lin
- **期刊/来源**: Biometrics
- **机构**: University of North Carolina at Chapel Hill
- **分类**: vol 80 · issue 1
- 相关性 5/10 · novelty: `application`
- **摘要**: 该文针对多变量面板计数数据（即每个受试者在两次检查之间记录多种类型复发事件的计数）提出比例率模型。协变量效应通过比例率模型刻画，而不同类型事件间的依赖结构完全非参数化，不指定参数形式。估计采用非参数最大伪似然法，在“各类型事件独立且每类事件为非齐次Poisson过程”的工作假设下进行，并开发了简单稳定的EM算法。理论上证明了回归参数估计的相合性和渐近正态性，协方差矩阵可通过sandwich估计量一致估计。还提出了一类图形和数值方法用于模型拟合优度检验。模拟和皮肤癌临床试验数据分析验证了方法性能。对您而言，该文的伪似然+EM框架与您熟悉的因果推断中纵向数据（如重复事件）的估计问题有直接关联，其sandwich方差估计思路也可迁移至您关注的proximal causal inference中的敏感性分析。
- **关键技术**: `nonparametric maximum pseudo-likelihood`, `EM algorithm`, `sandwich estimator`, `proportional rates model`, `multivariate panel count data`
- **为什么对您有用**: 本文属于流行病学应用（皮肤癌临床试验），与您的secondary interest（epidemiology）直接相关，且其处理多类型复发事件计数的方法可视为纵向因果推断中重复事件设定的一种建模策略。您的武器库中'nonparametric statistics'和'estimation theory in causal inference'可直接用于理解其伪似然估计的渐近性质，而'sandwich estimator'的稳健性分析思路可尝试用于您熟悉的proximal CI框架中的敏感性分析。中期可做：若想将本文方法推广至因果参数（如ATE）的识别，需先在'moderately_familiar'的'identification theory in causal inference'上长肌肉，理解其工作假设（独立Poisson）在因果解释下的局限性。

### 15. [10.1093/biomtc/ujad017](https://doi.org/10.1093/biomtc/ujad017) — Multiobjective tree-based reinforcement learning for estimating tolerant dynamic treatment regimes
- **作者**: Yao Song, Lu Wang
- **期刊/来源**: Biometrics
- **机构**: University of Michigan
- **分类**: vol 80 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出“容忍动态治疗方案”（tDTR）的概念，在预设容忍率下给出多个可行的个体化决策规则集合，以处理多目标优化中的权衡问题。方法上，作者开发了多目标树强化学习（MOT-RL），在每阶段通过半参数回归建模每个目标的反事实均值，并利用标量化增广逆概率加权估计量（SAIPWE）构造纯度度量来构建无监督决策树。算法采用向后归纳方式跨阶段运行，可同时输出最优DTR和tDTR，并允许决策者根据偏好调整。MOT-RL具有鲁棒、高效、易解释且灵活的优点。应用部分使用MD Anderson癌症中心的前列腺癌数据评估两阶段化疗方案，同时优化疾病负担和生存期。对您而言，本文在纵向因果推断中引入多目标容忍机制，其半参数回归与IPW估计器的结合思路可迁移至您的proximal CI或mediation分析中的多目标设定。
- **关键技术**: `semiparametric regression`, `augmented inverse probability weighted estimator (AIPW)`, `tree-based reinforcement learning`, `multiobjective optimization`, `dynamic treatment regime (DTR)`
- **为什么对您有用**: 本文直接关联您的primary interest中的纵向因果推断（dynamic treatment regime）和半参数理论（semiparametric regression + AIPW）。技术武器库中，您对非参数统计和因果推断估计理论非常熟悉，可立即用M-estimation框架分析其SAIPWE的渐近性质，或用higher-order U-statistics的树宽视角评估决策树分裂的计算成本。中期可做：若想将容忍机制扩展到proximal CI设定，需先在identification theory上长肌肉（moderately_familiar）。

### 16. [10.1093/biomtc/ujad004](https://doi.org/10.1093/biomtc/ujad004) · [arXiv](https://arxiv.org/abs/2210.16255) — Incorporating participants’ welfare into sequential multiple assignment randomized trials
- **作者**: Xinru Wang, Nina Deliu, Yusuke Narita, Bibhas Chakraborty
- **期刊/来源**: Biometrics
- **机构**: Duke-NUS Medical School · University of Cambridge · MRC Biostatistics Unit · Sapienza University of Rome · Yale University · National University of Singapore · Duke University
- **分类**: vol 80 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对动态治疗策略（DTR）的序贯多分配随机试验（SMART）中参与者福利被忽视的伦理问题，提出了一种基于“实验即市场”（EXAM）框架的新设计SMART-EXAM。传统SMART以固定等概率随机化分配治疗，可能导致大量参与者被分到经验上较差的或他们不喜欢的治疗组，从而降低招募率、增加脱落率，损害试验的内外部效度。SMART-EXAM的核心机制是在每个阶段的随机化过程中，同时纳入参与者的治疗偏好和预测的治疗效果（即个体化获益），从而动态调整分配概率，以提升参与者整体福利。作者详细描述了SMART-EXAM的实施步骤，并通过模拟研究将其与传统SMART在参与者福利和构建最优DTR的能力上进行对比。结果表明，当实验参数设置适当时，SMART-EXAM能在不显著牺牲构建最优DTR能力的前提下，有效改善试验参与者的福利。最后，文章利用一项针对注意力缺陷/多动障碍儿童的SMART数据进行了实例分析，展示了该设计的实际应用潜力。该设计为因果推断中涉及多阶段决策和个体化治疗的随机试验提供了一种兼顾伦理与效率的新思路，对您关注的纵向因果推断和试验设计方向有直接参考价值。
- **关键技术**: `Sequential Multiple Assignment Randomized Trial (SMART)`, `Experiment-as-Market (EXAM) framework`, `dynamic treatment regimes (DTR)`, `preference-based randomization`, `individualized treatment effect`
- **为什么对您有用**: 本文直接关联您primary interest中的“causal inference (longitudinal)”和“mediation”子方向，因为它处理的是多阶段治疗决策（DTR）的试验设计，这是纵向因果推断的核心应用场景。从技术武器库看，您“very_familiar”中的“estimation theory in causal inference”和“nonparametric statistics”可用于分析SMART-EXAM中基于偏好和预测效果的随机化机制对DTR估计量的识别与偏差影响，而“moderately_familiar”中的“identification theory in causal inference”则可用于严格刻画该设计下最优DTR的可识别性条件。**中期可做**：要深入分析SMART-EXAM的统计性质（如估计量的渐近效率、与标准SMART的方差比较），需先在“moderately_familiar”的“semiparametric theory”上加强，特别是处理非标准随机化机制下的影响函数推导。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1093/biomtc/ujad002](https://doi.org/10.1093/biomtc/ujad002) · [arXiv](https://arxiv.org/abs/2308.16333) — Multiple augmented reduced rank regression for pan-cancer analysis
- **作者**: Jiuzhou Wang, Eric F Lock
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文提出多重增强降秩回归（maRRR），用于整合多个队列的高维数据，同时学习协变量驱动的变异和辅助结构化变异。方法基于随机矩阵理论构造结构化核范数目标函数，回归或分解项可共享或特定于任意数量的队列。maRRR 框架统一了降秩回归和无监督多矩阵分解等方法，单数据集情形（aRRR）也是其特例。模拟表明，联合多个数据集并简约地考虑所有结构化变异能显著提升统计功效。在 TCGA 泛癌基因表达数据上，以体细胞突变为协变量，maRRR 在预测和插补上表现良好，并揭示了癌症类型间共享或特异的突变驱动变异。对您而言，该方法将高维回归与随机矩阵理论结合，其结构化核范数设计可直接迁移到您熟悉的高维统计和因果推断中的高维协变量调整问题。
- **关键技术**: `reduced rank regression`, `structured nuclear norm`, `random matrix theory`, `multi-cohort integration`, `matrix factorization`
- **为什么对您有用**: 本文直接连接您的高维统计和随机矩阵理论兴趣，其结构化核范数目标函数是 RMT 在高维回归中的典型应用。您可以用非常熟悉的 minimax 界工具分析其估计量的收敛速率，或用高维渐近理论验证其功效增益的紧性。中期可做：若将方法扩展到因果推断中的高维 IV 或 mediation 设定，需先在 moderately_familiar 的识别理论上长肌肉。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1093/biomtc/ujad023](https://doi.org/10.1093/biomtc/ujad023) — Nonparametric predictive model for sparse and irregular longitudinal data
- **作者**: Shixuan Wang, Seonjin Kim, Hyunkeun Ryan Cho, Won Chang
- **期刊/来源**: Biometrics
- **机构**: Miami University · University of Iowa · University of Cincinnati
- **分类**: vol 80 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对稀疏且不规则测量的纵向数据，提出一种基于核的均值响应轨迹预测方法。核心思想是利用预测变量轨迹在 L2 度量空间上的受试者间相似性来构造权重，假设预测变量轨迹随时间的变化模式相似会导致响应轨迹趋势相似。为应对多预测变量带来的维数灾难，作者引入了一个带多元高斯核的乘性模型，该模型能同时实现降维和筛选有预测意义的函数协变量。在温和正则条件下，推导了所提非参数估计量的渐近性质。通过大量模拟和 Framingham 心脏研究数据验证了方法的稳健性和灵活性。该工作与您的非参数统计和纵向因果推断兴趣直接相关，其基于相似性的加权思路可迁移至纵向数据中处理时变混杂的因果估计问题。
- **关键技术**: `kernel-based estimator`, `multiplicative model with multivariate Gaussian kernels`, `L2 metric space similarity`, `functional covariate selection`, `sparse and irregular longitudinal data`
- **为什么对您有用**: 本文直接关联您的非参数统计和纵向因果推断兴趣。其基于 L2 度量相似性的核加权方法，可视为纵向数据中处理时变混杂的一种非参数工具，您可以用非常熟悉的非参数统计和 minimax 界工具来评估该估计量的收敛速率是否最优。中期可做：若将该方法嵌入纵向因果推断的 g-computation 框架，需先在 moderately_familiar 的识别理论（如 sequential exchangeability 假设下的 g-formula）上补强。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1093/biomtc/ujae015](https://doi.org/10.1093/biomtc/ujae015) · [arXiv](https://arxiv.org/abs/2207.00926) — Asymptotic uncertainty of false discovery proportion
- **作者**: Meng Mei, Tao Yu, Yuan Jiang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究多重检验中错误发现比例（FDP）的不确定性量化问题。在检验统计量具有任意依赖结构的设定下，现有方法通常通过将任意依赖转化为弱依赖来建立FDP和FDR的强相合性，但FDP的渐近方差仍可能受依赖结构显著影响。作者假设检验统计量服从正态分布且满足弱依赖条件，推导了FDP的渐近展开式，并系统分析了不同依赖结构如何影响渐近方差。主要技术工具包括弱依赖条件下的极限定理和正态近似。理论结果表明，即使依赖程度很弱，FDP的变异性仍不可忽略，因此建议在多重检验报告中同时给出FDP的均值和方差估计，以更全面评估结果可靠性。该工作填补了FDP不确定性量化的文献空白，对您的高维假设检验兴趣有直接参考价值——其渐近方差分析框架可迁移至您熟悉的随机矩阵理论中特征值波动的研究设定。
- **关键技术**: `weak dependence`, `asymptotic expansion`, `false discovery proportion (FDP)`, `variance estimation`, `normal approximation`
- **为什么对您有用**: 直接连接您的高维假设检验兴趣——FDP的渐近方差分析是多重检验中依赖结构影响的核心问题。您武器库中'高维渐近理论'和'非参数统计'可直接用于验证其弱依赖假设的紧性，或推广至非正态设定。中期可做：需先在 moderately_familiar 的 'M估计理论' 上提升，以处理更一般的依赖结构下的方差估计。

### 2. [10.1093/biomtc/ujad013](https://doi.org/10.1093/biomtc/ujad013) — Randomized phase II selection design with order constrained strata
- **作者**: Yi Chen, Menggang Yu
- **期刊/来源**: Biometrics
- **机构**: University of Wisconsin–Madison
- **分类**: vol 80 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对随机化II期临床试验中的选择设计，提出利用分层人群的自然顺序约束（如疾病分期、风险等级）来提高统计效率。研究设定为二元或时间-事件结局，目标是在有限样本下最大化正确选择概率（PCS）。核心方法是将顺序约束纳入分层比较的统计推断中，通过约束似然或排序假设检验来减少参数空间，从而在不增加样本量的情况下提升检验效能。模拟和实例表明，与忽略顺序约束的标准方法相比，该方法在相同样本量下PCS提升5-15%，或可缩减样本量约20-30%。该方法可自然推广至随机化II期筛选设计。对您而言，该工作展示了如何将先验顺序信息（如单调性）融入假设检验框架以提升效率，这与您在高维统计和假设检验中的兴趣（如利用结构约束改善推断）直接相关，且其约束推断思路可迁移至因果推断中的敏感性分析或分层处理效应估计。
- **关键技术**: `order-constrained inference`, `randomized phase II selection design`, `stratified population`, `correct selection probability`, `time-to-event outcomes`
- **为什么对您有用**: 该论文直接关联您的假设检验兴趣，特别是利用顺序约束提升统计效率。您的技术武器库中的非参数统计和M估计理论可用于分析其约束似然估计的渐近性质，例如验证其PCS提升是否达到最优。中期可做：需先熟悉顺序约束推断的现有理论（如Barlow et al.的isotonic regression），但核心工具（M估计、渐近理论）已具备，属于立即可做的方向。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1093/biomtc/ujae016](https://doi.org/10.1093/biomtc/ujae016) · [arXiv](https://arxiv.org/abs/2305.08201) — Efficient computation of high-dimensional penalized generalized linear mixed models by latent factor modeling of the random effects
- **作者**: Hillary M Heiling, Naim U Rashid, Quefeng Li, Xianlu L Peng, Jen Jen Yeh, Joseph G Ibrahim
- **期刊/来源**: Biometrics
- **机构**: University of North Carolina at Chapel Hill
- **分类**: vol 80 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对高维广义线性混合模型（GLMM）的计算瓶颈，提出将随机效应分解为低维潜在因子（factor model decomposition），从而将高维随机效应的估计转化为少量潜在因子的估计，大幅降低计算复杂度。方法上，采用改进的 Monte Carlo Expectation Conditional Minimization（MCECM）算法进行参数估计，并同时实现固定效应和随机效应的变量选择（通过惩罚似然）。模拟实验表明，该方法在拟合速度上显著优于现有方法，并能扩展到现有方法无法处理的更高维度。理论贡献主要在于计算可扩展性，而非新的统计推断理论。对您而言，本文属于统计计算方向，展示了如何通过低维分解（类似降维或矩阵分解思想）解决高维混合模型的计算可扩展性问题，与您对统计计算（numerical methods, algorithm）的兴趣直接相关。
- **关键技术**: `factor model decomposition`, `Monte Carlo Expectation Conditional Minimization (MCECM)`, `penalized GLMM`, `latent factor modeling`, `variable selection for random effects`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的 primary interest 中的 statistical computing（numerical methods, algorithm）。核心武器是因子模型分解 + MCECM 算法，属于 moderately_familiar 的 M-estimation 和 high-dimensional asymptotics 范畴。**中期可做**：若想跟进，需先在 moderately_familiar 的 M-estimation theory 上长肌肉（特别是 MCECM 的收敛性分析），但当前武器库中的 high-dimensional asymptotics 和 software development 已足够理解其算法框架。

## 流行病学  *(epidemiology, 6 篇)*

### 1. [10.1093/biomtc/ujae008](https://doi.org/10.1093/biomtc/ujae008) · [arXiv](https://arxiv.org/abs/2302.02110) — A scalar-on-quantile-function approach for estimating short-term health effects of environmental exposures
- **作者**: Yuzi Zhang, Howard H Chang, Joshua L Warren, Stefanie T Ebelt
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文针对环境流行病学中短期暴露健康效应估计时，传统方法使用区域平均暴露量（如ZIP代码级日均值）无法捕捉个体暴露异质性的问题，提出了一种基于暴露分位数函数的标量回归方法。该方法将每个空间-时间单元内的暴露分布视为函数型协变量（分位数函数），通过标量-分位数函数回归模型（scalar-on-quantile-function regression）直接估计暴露分布不同分位点对健康结局（如急诊就诊次数）的效应。模型采用基函数展开（如B样条）对分位数函数进行降维，并利用惩罚似然估计实现参数估计与选择。在亚特兰大4年空气污染与急诊就诊数据分析中，利用SHEDS模型模拟的个人暴露分布，发现一氧化碳对呼吸和心血管疾病的影响在较低暴露分位数上更为显著。该方法提供了R包nbRegQF实现。对您而言，这是一篇应用导向的流行病学论文，其核心价值在于将暴露分布（而非均值）作为协变量，为因果推断中的暴露测量误差和个体异质性处理提供了新视角，与您对流行病学应用数据集的兴趣直接相关。
- **关键技术**: `scalar-on-function regression`, `quantile function covariate`, `B-spline basis expansion`, `penalized likelihood`, `exposure distribution modeling`
- **为什么对您有用**: 本文属于流行病学应用方向，直接使用真实数据集（亚特兰大空气污染与急诊就诊数据）并提供了R包，符合您对流行病学应用数据集的兴趣。方法学上，将暴露分布的分位数函数作为协变量，可视为对传统均值回归的推广，与您熟悉的非参数统计和因果推断中的暴露测量误差问题有潜在联系。作为入门读物，本文清晰展示了环境流行病学中从模拟暴露分布到健康效应建模的完整分析流程，值得花时间阅读全文以了解该领域的数据结构和分析范式。

### 2. [10.1093/biomtc/ujae014](https://doi.org/10.1093/biomtc/ujae014) — Bias correction models for electronic health records data in the presence of non-random sampling
- **作者**: Jiyu Kim, Rebecca Anthopolos, Judy Zhong
- **期刊/来源**: Biometrics
- **机构**: New York University
- **分类**: vol 80 · issue 1
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对电子健康记录（EHR）数据中因非随机纳入导致的 selection bias 问题，提出了一系列 Heckman 型偏倚校正方法。研究设定中，EHR 的纳入概率受人口学、社会经济地位、医疗转诊模式等不可观测因素影响，导致关联系数和结局均值的估计有偏。方法核心是将社会健康决定因素作为 selection covariates 纳入 Heckman 选择模型，以建模 EHR 非随机抽样概率。通过模拟研究验证了方法在多种设定下对偏倚的校正效果，并在纽约市 EHR 网络中估计了心血管疾病患病率及其与风险因素的关联。本文是应用导向的方法学工作，novelty 主要在于将 Heckman 模型适配到 EHR 选择偏倚场景，而非提出全新统计理论。对您而言，本文属于流行病学领域的应用型因果推断工作，展示了在真实数据缺失机制下的偏倚校正思路，可作为 gateway reading 了解 EHR 数据分析中的常见问题与解决框架。
- **关键技术**: `Heckman selection model`, `bias correction`, `selection bias`, `electronic health records`, `social determinants of health`
- **为什么对您有用**: 本文属于流行病学领域的应用型因果推断工作，直接对应您的 secondary interest 中的 epidemiology 方向。方法上使用了 Heckman 选择模型，与您 very_familiar 的 estimation theory in causal inference 有交叉，但核心机器（Heckman 模型及其识别假设）不在您的武器库中，属于暂不可做——需先熟悉样本选择模型的基本理论。本文可作为入门读物，帮助您了解 EHR 数据中 selection bias 的常见处理框架，但方法学深度有限，不值得投入全文精读。

### 3. [10.1093/biomtc/ujad027](https://doi.org/10.1093/biomtc/ujad027) — Estimating the effect of latent time-varying count exposures using multiple lists
- **作者**: Jung Yeon Won, Michael R Elliott, Emma V Sanchez-Vaznaugh, Brisa N Sánchez
- **期刊/来源**: Biometrics
- **机构**: University of Michigan · San Francisco State University · Drexel University
- **分类**: vol 80 · issue 1
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对纵向建成环境健康研究中商业数据库测量误差问题，提出一种联合建模方法以校正健康效应估计的偏倚。核心设定是：多个商业数据库提供同一时间点的计数暴露（如社区便利店数量），但各数据源质量不同且无金标准验证。方法上，构建一个贝叶斯非参数联合模型，同时刻画时变健康结局、观测计数暴露和潜在真实计数暴露；其中真实暴露采用泊松整数值一阶自回归过程（Poisson INAR(1)）建模时间依赖性，并通过狄利克雷过程混合先验灵活捕捉位置特异性暴露分布。该方法通过整合多个数据源的信息，估计每个数据源的时间特异性质量参数，从而解决数据源间的不一致性。在2001-2008年加州公立学校儿童肥胖数据与社区便利店暴露的实证分析中，该方法有效降低了纵向健康效应估计的偏倚。对您而言，本文提供了一个流行病学中处理多源测量误差的贝叶斯建模框架，其核心思想（利用多个有偏数据源校正估计）与因果推断中的负对照或工具变量思路有相通之处，可作为应用案例参考。
- **关键技术**: `Bayesian nonparametric modeling`, `Poisson INAR(1) process`, `Dirichlet process mixture`, `measurement error correction`, `multiple data sources integration`
- **为什么对您有用**: 本文属于流行病学应用，直接对应您的secondary interest。它处理的是纵向研究中多数据源测量误差问题，其建模思路（利用多个有偏来源推断真实暴露）与因果推断中的负对照或IV identification有概念联系，可作为应用案例。武器库方面，您对非参数统计和贝叶斯方法（moderately_familiar）足以理解其核心框架，但本文的贝叶斯非参数具体实现（DP混合）并非您当前主攻方向，因此属于**暂不可做**——核心机器（贝叶斯非参数建模与MCMC计算）不在武器库中，但作为入门读物了解流行病学数据结构和分析模式是有价值的。

### 4. [10.1093/biomtc/ujad008](https://doi.org/10.1093/biomtc/ujad008) — Efficient estimation for left-truncated competing risks regression for case-cohort studies
- **作者**: Xi Fang, Kwang Woo Ahn, Jianwen Cai, Soyoung Kim
- **期刊/来源**: Biometrics
- **机构**: Medical College of Wisconsin · University of North Carolina at Chapel Hill
- **分类**: vol 80 · issue 1
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对病例队列研究中的左截断竞争风险数据，提出了一种改进的逆概率加权估计方法。研究目标是在比例子分布风险模型下估计协变量对累积发生率的直接效应。现有方法未处理左截断且对完全观测协变量的参数估计效率较低。作者构建了增广逆概率加权估计方程，并进一步利用其他竞争原因的信息提出更高效的估计量。所提估计量具有一致性和渐近正态性，模拟研究验证了其无偏性和效率提升。该方法应用于动脉粥样硬化风险社区研究数据。对您而言，本文是流行病学中因果推断方法的应用实例，其增广加权思路与您熟悉的因果推断估计理论（如IPW、DR估计）直接相关，可作为中期可做的应用参考。
- **关键技术**: `augmented inverse probability weighting`, `proportional subdistribution hazards model`, `left truncation`, `competing risks`, `case-cohort design`
- **为什么对您有用**: 本文属于流行病学应用方向，与您的secondary interest（流行病学数据集、因果推断应用）直接匹配。您武器库中very_familiar的因果推断估计理论（IPW、DR估计）可直接用于理解其增广加权机制，但需注意其竞争风险设定与您熟悉的ATE框架略有差异。本文是中期可做的应用参考——您可先通过阅读本文熟悉竞争风险数据结构和左截断处理，再考虑将类似增广加权思路迁移到您关注的proximal CI或纵向因果推断中。

### 5. [10.1093/biomtc/ujad038](https://doi.org/10.1093/biomtc/ujad038) — Two-phase designs with failure time processes subject to nonsusceptibility
- **作者**: Fangya Mao, Li C Cheung, Richard J Cook
- **期刊/来源**: Biometrics
- **机构**: National Cancer Institute · Division of Cancer Epidemiology and Genetics · University of Waterloo
- **分类**: vol 80 · issue 1
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对存在不敏感（cure）分组的右删失失效时间数据，开发了两阶段设计的高效策略。研究设定中，部分个体为长期幸存者（不敏感），因此采用混合模型：逻辑回归建模治愈概率，比例风险模型建模敏感个体的失效时间，并进一步考虑联合建模两个参数。核心创新在于提出了一类新的双变量残差依赖设计，用于应对场景(c)中两个感兴趣参数同时存在时的子抽样挑战。通过模拟研究，该方法在估计效率上显著优于多种传统的第二阶段子抽样方案。文章还以前列腺、肺、结直肠和卵巢癌筛查试验数据为例进行了实证分析。对您而言，本文的两阶段设计思想与流行病学队列研究中的因果推断问题高度相关，其残差依赖抽样策略可迁移至您熟悉的逆概率加权或双重稳健估计框架中。
- **关键技术**: `two-phase design`, `mixture cure model`, `residual-dependent sampling`, `case-cohort design`, `proportional hazards model`
- **为什么对您有用**: 本文属于流行病学应用，直接对应您的secondary interest。其两阶段设计方法在大型队列中高效测量昂贵协变量，与您熟悉的因果推断中的逆概率加权和估计理论有直接接口。武器库中'非参数统计'和'因果推断中的估计理论'足以理解并评估其设计效率，属于'立即可做'的阅读范畴——可快速吸收其抽样策略，并思考如何将其与您关注的proximal causal inference或mediation分析中的子抽样问题结合。

### 6. [10.1093/biomtc/ujae013](https://doi.org/10.1093/biomtc/ujae013) — Soft classification and regression analysis of audiometric phenotypes of age-related hearing loss
- **作者**: Ce Yang, Benjamin Langworthy, Sharon Curhan, Kenneth I Vaden, Gary Curhan, Judy R Dubno et al.
- **期刊/来源**: Biometrics
- **机构**: Harvard University · Brigham and Women's Hospital · Medical University of South Carolina
- **分类**: vol 80 · issue 1
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对年龄相关性听力损失的复杂病因，提出了一种软分类与回归分析方法。研究首先利用二次判别分析（QDA）对听力图表型（老年正常型、代谢型、感觉型、代谢+感觉型）进行软分类，得到每个个体属于各表型的概率。随后，通过估计方程（estimating equations）建立暴露因素（如饮食模式）与这些软分类概率之间的关联模型。在合理假设下，估计方程无偏且估计量一致，模拟研究显示有限样本性能良好。应用部分利用护士健康研究II（Nurses' Health Study II）的数据，分析了DASH饮食依从性与听力表型的关系，发现更健康的饮食模式与较低的代谢+感觉型听力损失风险相关。该方法为流行病学中基于分类表型的因果关联分析提供了实用工具，尤其适用于结局为多类别软分类的场景。
- **关键技术**: `quadratic discriminant analysis (QDA)`, `estimating equations`, `soft classification`, `phenotype classification`
- **为什么对您有用**: 本文属于流行病学应用，直接关联您的secondary interest中的流行病学方向。方法上使用估计方程处理软分类概率，与您熟悉的因果推断中的估计方程方法有共通之处，可作为流行病学数据分析的入门参考。武器库中'identification theory in causal inference'和'M-estimation theory'可支撑理解其估计方程的无偏性论证，但本文方法学创新有限，属于标准技术应用。暂不可做：核心贡献在应用而非新方法，无需直接跟进。

## 其他  *(other, 16 篇)*

### 1. [10.1093/biomtc/ujad041](https://doi.org/10.1093/biomtc/ujad041) — Simultaneous variable selection and estimation in semiparametric regression of mixed panel count data
- **作者**: Lei Ge, Tao Hu, Yang Li
- **期刊/来源**: Biometrics
- **机构**: Northeast Normal University · Indiana University School of Medicine · Indiana University – Purdue University Indianapolis · Capital Normal University
- **分类**: vol 80 · issue 1
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对纵向调查中常见的混合面板计数数据（同时包含面板计数和面板二元成分），提出了一种在比例均值模型下的惩罚似然变量选择与估计方法。该方法通过EM算法实现高效计算，能够同时进行变量选择和参数估计，并保证稀疏解。理论证明所得估计量具有Oracle性质（即变量选择一致且估计量渐近有效）。模拟研究验证了有限样本下的良好表现，并应用于健康与退休研究（HRS）数据集。对您而言，该文属于应用统计方法论文，与您的主要兴趣（因果推断、高维统计、半参理论）无直接技术交集，但可作为纵向数据中变量选择方法的参考。
- **关键技术**: `penalized likelihood`, `EM algorithm`, `oracle property`, `proportional mean model`, `mixed panel count data`
- **为什么对您有用**: 本文属于纵向数据中变量选择的应用方法论文，与您的主要兴趣（因果推断、高维统计、半参理论）无直接技术交集。武器库中'非参数统计'和'高维渐近'可帮助理解其Oracle性质证明，但核心方法（惩罚似然+EM）并非您当前关注的前沿。暂不可做——缺乏与您核心兴趣的直接连接，不值得投入时间精读。

### 2. [10.1093/biomtc/ujae012](https://doi.org/10.1093/biomtc/ujae012) — Accounting for network noise in graph-guided Bayesian modeling of structured high-dimensional data
- **作者**: Wenrui Li, Changgee Chang, Suprateek Kundu, Qi Long
- **期刊/来源**: Biometrics
- **机构**: University of Pennsylvania · Indiana University School of Medicine · Indiana University – Purdue University Indianapolis · The University of Texas MD Anderson Cancer Center
- **分类**: vol 80 · issue 1
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对结构化高维数据（如基因组、转录组数据）的回归建模问题，提出一种图引导的贝叶斯框架，核心创新在于显式处理先验网络中的噪声（如数据库提取的图存在缺失边和假阳性边）。方法利用两个网络信息源：从现有数据库获得的含噪图，以及从观测数据中估计的图，通过潜在尺度建模框架对真实底层网络进行建模，并与自适应结构化收缩先验的贝叶斯回归模型耦合。开发了高效的MCMC算法进行后验采样。模拟和两个阿尔茨海默病组学数据集分析展示了方法相对于现有方法的优势。本文属于应用导向的方法学工作，方法学新颖性在于将网络噪声纳入贝叶斯先验建模，但核心工具（MCMC、收缩先验）较为经典。
- **关键技术**: `Bayesian shrinkage prior`, `graph-guided regularization`, `latent scale modeling`, `Markov chain Monte Carlo`, `structured high-dimensional regression`
- **为什么对您有用**: 本文属于高维统计与贝叶斯方法的交叉应用，与您的主要兴趣（高维统计、因果推断）关联较弱。方法学上未涉及您武器库中的核心工具（如U统计量、半参效率理论、随机矩阵理论）。作为流行病学应用（阿尔茨海默病组学数据）可作入门阅读，但方法学深度不足以支撑后续问题发现。暂不可做：核心机器（贝叶斯建模与MCMC）不在您当前武器库中，且方法学贡献偏应用，难以直接迁移到您的因果推断或高维统计工作。

### 3. [10.1093/biomtc/ujae001](https://doi.org/10.1093/biomtc/ujae001) · [arXiv](https://arxiv.org/abs/2203.01990) — From local to global gene co-expression estimation using single-cell RNA-seq data
- **作者**: Jinjin Tian, Jing Lei, Kathryn Roeder
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对单细胞RNA-seq数据中基因关系的局部性（随样本点变化、仅存在于子集、非线性或非单调）提出新的依赖度量。首先定义细胞特异性基因网络，然后通过平均得到一种新的单变量依赖度量——平均局部密度间隙（aLDG），该度量能累积局部依赖并检测任意非线性非单调关系。作者给出了aLDG的一致非参数估计量，并在总体和样本层面证明了其稳健性。进一步，利用外部结构信息（如空间或时间因子）对细胞进行小批量平均，可以更突出有意义的局部结构变化点。通过模拟和真实数据分析，aLDG在成对基因关系估计、细胞轨迹分叉点检测和空间转录组结构可视化等场景中优于现有方法。本文主要贡献在生物统计应用领域，与您的主要兴趣（因果推断、高维统计等）无直接技术重叠，但可作为流行病学或生物统计应用的一个参考案例。
- **关键技术**: `cell-specific gene networks`, `local density gap`, `nonparametric estimation`, `mini-batch averaging`, `spatial transcriptomics`
- **为什么对您有用**: 本文属于流行病学/生物统计的应用工作，与您的secondary interest（流行病学应用）相关。文中使用的非参数估计和局部依赖度量与您的very_familiar工具（非参数统计）有概念上的联系，但核心问题（基因网络估计）与您的主要兴趣方向（因果推断、高维RMT、U统计量等）距离较远。作为流行病学应用，本文展示了单细胞数据中依赖结构分析的统计思路，但方法学新颖性有限，属于应用型工作。暂不可做：核心机器（单细胞网络估计）不在您的武器库中，且缺乏与您主要兴趣的直接连接点。

### 4. [10.1093/biomtc/ujad042](https://doi.org/10.1093/biomtc/ujad042) · [arXiv](https://arxiv.org/abs/2208.12383) — High-dimensional sparse vine copula regression with application to genomic prediction
- **作者**: Özge Sahin, Claudia Czado
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对高维基因组预测中非线性与复杂依赖结构的问题，提出两种基于vine copula的稀疏回归方法。现有vine copula回归方法无法扩展到高维或超高维情形，本文通过引入稀疏性假设和变量选择机制解决了这一可扩展性瓶颈。方法的核心机制是定义相关、无关和冗余解释变量，并利用vine copula结构进行变量筛选与分位数回归。在计算复杂度上，作者证明了所提方法优于现有vine copula回归方法。通过模拟研究展示了变量选择能力和预测精度，并应用于玉米性状的基因组预测真实数据。与线性模型和分位数随机森林相比，本文方法在模拟和实际数据中均表现出优势。对您而言，本文属于应用导向的方法学工作，与您的主要兴趣方向（因果推断、高维统计、半参理论）关联较弱，但基因组预测中的变量选择与依赖结构建模思路可能对您在高维设定下的因果推断或预测问题有间接启发。
- **关键技术**: `vine copula regression`, `sparse variable selection`, `quantile regression`, `genomic prediction`
- **为什么对您有用**: 本文属于应用统计方法学，与您的主要兴趣方向（因果推断、高维统计、半参理论）关联较弱。方法核心是vine copula与稀疏回归的结合，未涉及您武器库中的具体工具（如U-statistics、efficiency theory、DML等）。作为gateway reading价值有限，因为基因组预测问题本身与您的统计计算-信息权衡兴趣方向距离较远。暂不可做——核心机器（vine copula理论、基因组数据特性）不在您的武器库中。

### 5. [10.1093/biomtc/ujad006](https://doi.org/10.1093/biomtc/ujad006) — Longitudinal varying coefficient single-index model with censored covariates
- **作者**: Shikun Wang, Jing Ning, Ying Xu, Ya-Chen Tina Shih, Yu Shen, Liang Li
- **期刊/来源**: Biometrics
- **机构**: Columbia University · The University of Texas MD Anderson Cancer Center · University of California, Los Angeles
- **分类**: vol 80 · issue 1
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对健康政策研究中癌症患者从诊断到死亡的纵向医疗费用轨迹估计问题，提出了一种纵向变系数单指标模型。该模型将多个患者特征压缩为一个单指标（代表医疗利用倾向），并通过双变量变系数函数灵活刻画该指标对费用轨迹不同区段的影响随时间和生存时间的变化。模型采用广义估计方程（GEE）估计，并扩展了边际均值结构以处理删失生存时间作为协变量的问题。作者建立了变系数的逐点置信区间和协变量效应的检验方法。模拟研究验证了方法的数值性能，并应用于SEER-Medicare数据库的前列腺癌患者医疗费用数据。该工作主要贡献在于提出一个针对特定应用场景的统计模型，方法学创新性有限，属于应用导向的方法开发。
- **关键技术**: `varying coefficient model`, `single-index model`, `generalized estimating equations (GEE)`, `censored covariates`, `longitudinal data`
- **为什么对您有用**: 本文属于流行病学应用（医疗费用数据），但方法学核心（变系数单指标模型+GEE）与您的主要兴趣方向（因果推断、半参理论）关联较弱。该文未涉及因果识别策略（如IV、proximal等），也未使用您武器库中的高阶U统计量或效率理论工具。作为流行病学应用，它展示了纵向删失数据建模的一个具体案例，但方法学深度不足以支撑您直接迁移或改进。暂不可做——核心机器（因果识别、半参效率界）在本文中未使用。

### 6. [10.1093/biomtc/ujae003](https://doi.org/10.1093/biomtc/ujae003) — Merging or ensembling: integrative analysis in multiple neuroimaging studies
- **作者**: Yue Shan, Chao Huang, Yun Li, Hongtu Zhu
- **期刊/来源**: Biometrics
- **机构**: University of North Carolina at Chapel Hill · Florida State University
- **分类**: vol 80 · issue 1
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文系统研究了多中心神经影像数据整合分析中的两种策略：合并（merging）与集成（ensembling）。设定为空间变系数混合效应模型（SVCMEM），目标是在存在研究间异质性的情况下比较两种方法的预测精度。合并策略将所有研究数据合并训练单一模型，集成策略则对各研究独立训练的模型进行加权平均。作者推导了在不同异质性程度下选择合并或集成策略的渐近准则，并给出了集成学习器的最优权重。通过大量模拟和三个大规模神经影像研究的实证分析验证了理论结果。该工作属于应用统计方法研究，方法学创新程度有限，主要贡献在于为多中心数据分析提供了实用的决策框架。
- **关键技术**: `spatially varying coefficient mixed effects models`, `ensemble learning`, `weighted averaging`, `asymptotic optimality`
- **为什么对您有用**: 本文属于流行病学/神经影像领域的应用工作，使用了混合效应模型和集成学习，但方法学深度有限，与您的主要兴趣（因果推断、高维统计、U-统计量）无直接交集。作为流行病学方向的gateway reading，它展示了多中心数据整合的实际问题，但武器库中的非参数统计和M-估计理论足以覆盖其技术内容，无需深入阅读全文。

### 7. [10.1093/biomtc/ujad024](https://doi.org/10.1093/biomtc/ujad024) · [arXiv](https://arxiv.org/abs/2303.05341) — Penalized deep partially linear cox models with application to CT scans of lung cancer patients
- **作者**: Yuming Sun, Jian Kang, Chinmay Haridas, Nicholas Mayne, Alexandra Potter, Chi-Fu Yang et al.
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对高维生存数据提出 Penalized Deep Partially Linear Cox Model (Penalized DPLC)，将部分线性 Cox 模型中的参数部分用 SCAD 惩罚进行变量选择（处理高维纹理特征），非参数部分用深度神经网络估计（缓解维数灾难）。模型假设 hazard 函数分解为线性组合（参数）与未知光滑函数（非参数）之和，属于半参数 Cox 框架。作者证明了估计量的收敛性与渐近性质（未给出具体率，但提及 consistency 与 oracle property）。模拟研究对比了多种方法（如 LASSO、DeepSurv）在风险预测与特征选择上的表现。实际应用在 NLST 肺癌 CT 纹理数据上，识别出关键临床与影像风险因素。对您而言，本文方法学 novelty 有限（SCAD + DNN 的组合在生存分析中已有类似工作），且未涉及您核心兴趣中的因果推断、U-统计量或效率理论；但若您关注高维生存数据中的半参数建模，可作为应用参考。
- **关键技术**: `SCAD penalty`, `deep neural network`, `partially linear Cox model`, `variable selection`, `survival analysis`
- **为什么对您有用**: 本文属于应用统计方法论文，与您的 primary interests（因果推断、高维 RMT、U-统计量、效率理论）无直接交集。方法上 SCAD + DNN 的组合在生存分析中并非全新，且未涉及您武器库中的具体工具（如 treewidth / einsum 或 minimax bound）。若您未来想进入高维生存数据方向，本文可作为入门应用案例，但当前暂不可做——核心机器（高维惩罚回归与 DNN 的渐近理论）不在您的武器库中。

### 8. [10.1093/biomtc/ujae010](https://doi.org/10.1093/biomtc/ujae010) — A boosting method to select the random effects in linear mixed models
- **作者**: Michela Battauz, Paolo Vidoni
- **期刊/来源**: Biometrics
- **机构**: University of Udine
- **分类**: vol 80 · issue 1
- 相关性 4/10 · novelty: `minor`
- **摘要**: 本文针对线性混合模型中随机效应的选择问题，提出了一种基于似然的boosting方法。由于目标函数（负剖面对数似然）非凸，标准梯度下降可能陷入鞍点或局部极小。为此，优化算法在牛顿方向之外同时使用负曲率方向，以更有效地探索非凸曲面。模拟和真实数据应用表明，该方法在随机效应选择上表现良好。对您而言，该文属于统计计算与模型选择交叉领域，但核心问题（随机效应选择）与您的主要兴趣（因果推断、高维统计）距离较远，且方法学创新程度有限。
- **关键技术**: `likelihood-based boosting`, `negative curvature direction`, `profile log-likelihood`, `random effects selection`, `linear mixed models`
- **为什么对您有用**: 本文涉及混合模型中的随机效应选择，属于统计计算与模型选择的交叉，但核心问题与您的主要兴趣（因果推断、高维统计、U统计量）关联较弱。方法上使用了负曲率方向处理非凸优化，这一技巧在您的武器库中并不突出。暂不可做：核心机器（混合模型随机效应选择）不在您的武器库里，且缺乏与您熟悉工具的直接连接。

### 9. [10.1093/biomtc/ujad021](https://doi.org/10.1093/biomtc/ujad021) · [arXiv](https://arxiv.org/abs/2210.08297) — Clustering blood donors via mixtures of product partition models with covariates
- **作者**: Raffaele Argiento, Riccardo Corradin, Alessandra Guglielmi, Ettore Lanzarone
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对献血间隔时间预测问题，提出了一类贝叶斯非参数聚类模型。模型通过引入协变量信息来改进随机划分的先验，使得具有相似协变量值的个体更倾向于被分到同一簇。该工作推广了已有的产品划分模型（PPMx），在凝聚函数上采用混合PPMx形式，相似函数则刻画簇的密度。在献血数据上的应用表明，纳入协变量信息能提升后验预测性能，并有助于用协变量解释估计出的簇结构。本文主要贡献在贝叶斯非参数聚类方法，与您关注的因果推断、高维统计、U-统计量等方向无直接交集。
- **关键技术**: `Bayesian nonparametric clustering`, `product partition models with covariates (PPMx)`, `random partition prior`, `cohesion and similarity functions`
- **为什么对您有用**: 本文属于贝叶斯非参数聚类应用，与您的主要兴趣方向（因果推断、高维统计、U-统计量等）无直接关联。武器库中的工具（如非参数统计、M估计理论）在此处不直接适用。暂不可做——核心机器（贝叶斯非参数先验设计、MCMC计算）不在武器库中。

### 10. [10.1093/biomtc/ujad014](https://doi.org/10.1093/biomtc/ujad014) — Incorporating graph information in Bayesian factor analysis with robust and adaptive shrinkage priors
- **作者**: Qiyiwen Zhang, Changgee Chang, Li Shen, Qi Long
- **期刊/来源**: Biometrics
- **机构**: University of Pennsylvania · Indiana University School of Medicine · Indiana University – Purdue University Indianapolis
- **分类**: vol 80 · issue 1
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出一种贝叶斯因子模型，用于高维多组学数据的低秩稀疏分解。核心创新在于设计了一种新的分层先验，能够将生物网络（如基因调控网络）的结构信息整合到因子载荷的稀疏性诱导中。该先验通过自适应收缩和额外层级将个体收缩参数与图信息关联，使得因子载荷的恢复更准确。与现有图整合方法相比，该先验克服了相变现象，对与真实稀疏结构不一致的噪声边具有鲁棒性。模型支持连续和离散数据类型。模拟和真实数据分析表明其优于若干现有因子分析方法。
- **关键技术**: `Bayesian factor model`, `sparsity-inducing prior`, `graph-incorporated shrinkage`, `adaptive shrinkage`, `phase transition`
- **为什么对您有用**: 本文属于贝叶斯高维统计方法，与您的主要兴趣（高维统计、非参数/半参数理论）关联较弱。其核心贡献在于先验设计而非您熟悉的 minimax 或效率理论框架。作为 gateway reading 价值有限，因为方法学 novelty 程度不高（主要是应用导向的改进）。暂不可做：核心机器（贝叶斯分层模型、MCMC 采样）不在您的武器库中。

### 11. [10.1093/biomtc/ujad001](https://doi.org/10.1093/biomtc/ujad001) — Homogeneity pursuit and variable selection in regression models for multivariate abundance data
- **作者**: Francis K C Hui, Luca Maestrini, Alan H Welsh
- **期刊/来源**: Biometrics
- **机构**: Australian National University
- **分类**: vol 80 · issue 1
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对生态学中多元丰度数据的回归建模问题，提出了一种同时进行同质性追踪（将响应系数相似的物种聚类）和变量选择的广义估计方程（GEE）方法。该方法通过（降秩）工作相关矩阵灵活处理物种间的相关性，并引入自适应融合Lasso和自适应Lasso惩罚，分别实现同一协变量下物种系数的聚类和不同协变量间的稀疏化。数值模拟表明，该方法在有限样本下优于现有方法。应用于澳大利亚大堡礁底栖生物的存在-缺失数据，揭示了物种-环境关系中的高度同质性和稀疏性，从而得到更简洁的模型，并提升了样本外预测性能。本文主要贡献在于将惩罚GEE框架扩展到生态学多元丰度数据的特定需求，属于应用导向的方法学改进。对您而言，本文与您的主要兴趣（因果推断、高维统计等）和方法库（非参数统计、M估计理论）的直接关联较弱，但可作为了解生态学中多元响应数据建模和惩罚GEE应用的参考。
- **关键技术**: `Generalized Estimating Equations (GEE)`, `adaptive fused lasso`, `adaptive lasso`, `reduced-rank working correlation matrix`, `homogeneity pursuit`, `variable selection`
- **为什么对您有用**: 本文属于应用统计方法学，与您的主要兴趣（因果推断、高维统计、半参理论等）和方法库（非参数统计、M估计理论）的直接关联较弱。它主要解决生态学中多元丰度数据的特定建模问题，而非您关注的统计推断或计算复杂性理论。作为gateway-reading，本文对生态学应用背景的统计学家可能有用，但您作为理论统计研究者，从中获得的方法学迁移机会有限。因此，本文暂不可做，核心机器（多元响应数据的GEE框架和生态学特定假设）不在您的武器库中。

### 12. [10.1093/biomtc/ujae011](https://doi.org/10.1093/biomtc/ujae011) — Bayesian two-stage modeling of longitudinal and time-to-event data with an integrated fractional Brownian motion covariance structure
- **作者**: Anushka Palipana, Seongho Song, Nishant Gupta, Rhonda Szczesniak
- **期刊/来源**: Biometrics
- **机构**: Duke University · University of Cincinnati · Veterans Health Administration · Cincinnati Children's Hospital Medical Center
- **分类**: vol 80 · issue 1
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文提出一种贝叶斯两阶段联合建模方法，用于纵向生物标志物轨迹与时间-事件数据。纵向子模型用标度积分分数布朗运动（IFBM）替代传统随机截距-斜率项，以更灵活地刻画生物过程的复杂变异；从IFBM模型导出实时预测概率作为疾病快速进展的风险监测函数。预测的纵向值作为Cox子模型的输入估计事件风险，两阶段通过贝叶斯后验计算与推断实现。在罕见病淋巴管平滑肌瘤病（LAM）的全国患者登记数据上，IFBM模型在预测肺病进展和死亡率方面优于积分Ornstein-Uhlenbeck和传统随机效应模型。该方法主要贡献在于用随机过程（IFBM）替代参数化随机效应，提升纵向轨迹的拟合与预测能力。对您而言，本文属于应用统计方法论文，与您的主要兴趣（因果推断、高维统计、U统计量等）无直接技术重叠，但可作为纵向数据建模的参考案例。
- **关键技术**: `integrated fractional Brownian motion`, `Bayesian posterior computation`, `joint modeling`, `Cox proportional hazards`, `predictive probability`
- **为什么对您有用**: 本文属于纵向数据与生存分析的联合建模应用，与您的主要兴趣方向（因果推断、高维统计、U统计量）无直接技术连接。武器库中无对应工具可直接攻其方法核心（IFBM随机过程与贝叶斯计算）。作为流行病学应用，可作入门阅读了解纵向数据建模的常见挑战，但方法学新颖性有限，不值得投入全文时间。

### 13. [10.1093/biomtc/ujad040](https://doi.org/10.1093/biomtc/ujad040) — Sparse ordinal discriminant analysis
- **作者**: Sangil Han, Minwoo Kim, Sungkyu Jung, Jeongyoun Ahn
- **期刊/来源**: Biometrics
- **机构**: Seoul National University · Korea Advanced Institute of Science and Technology
- **分类**: vol 80 · issue 1
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对分类问题中响应变量为有序类别（如癌症分级）的场景，提出了一种基于线性判别分析（LDA）的稀疏有序判别分析方法。现有方法通常只关注与有序标签边际相关的预测变量，而本文旨在选择那些共同贡献于有序标签的变量集合。方法核心是在最优评分（optimal scoring）框架下引入正则化：对最优评分施加有序性惩罚（ordinality penalty），同时对预测变量的系数施加稀疏性惩罚（如Lasso）。通过这种双重惩罚，模型能够同时实现变量选择和有序结构的利用。作者在胶质瘤基因表达数据集上验证了方法的有效性，并与多种现有方法进行了模拟比较，展示了其在分类性能和模型可解释性方面的优势。该方法属于监督学习中的降维与特征选择问题，与您的主要兴趣（因果推断、高维统计、半参数理论）无直接交集，但有序分类在流行病学等应用领域有潜在价值。
- **关键技术**: `optimal scoring`, `linear discriminant analysis`, `ordinality penalty`, `sparsity penalty`, `regularization framework`
- **为什么对您有用**: 本文属于应用统计方法论文，与您的主要兴趣方向（因果推断、高维统计、半参数理论）无直接技术交集。虽然有序分类在流行病学中有应用场景，但本文的方法论核心（LDA+正则化）并非您武器库中的核心工具，且未涉及您关注的识别、效率理论或计算复杂性等问题。作为gateway reading价值有限，不建议深入阅读。

### 14. [10.1093/biomtc/ujae006](https://doi.org/10.1093/biomtc/ujae006) — Changing interim monitoring in response to internal clinical trial data
- **作者**: Michael A Proschan, Martha Nason, Ana M Ortega-Villa, Jing Wang
- **期刊/来源**: Biometrics
- **机构**: National Institute of Allergy and Infectious Diseases
- **分类**: vol 80 · issue 1
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对新兴传染病（如COVID-19）临床试验中，因外部或内部数据驱动而临时修改中期分析计划的问题，研究如何在不预先设定适应性设计的情况下控制I类错误率。核心方法是Müller和Schäfer（2004）的条件错误率原则：在观察到内部数据后，若决定增加中期分析次数，则通过条件错误率函数确保最终检验的I类错误率不超过预设水平。文章详细分析了该方法的性质与局限性，包括对功效和停止边界的影响。提供了Shiny应用以辅助实践。主要结论是：即使仅基于内部数据（按分组）调整中期分析计划，条件错误率原则仍能严格控制I类错误，但可能损失部分功效。本文属于临床试验统计方法的应用性工作，对您而言，其方法论（条件错误率）与因果推断中的敏感性分析或序贯检验有间接联系，但技术深度和与您主要兴趣（高维统计、U统计量、半参效率理论）的直接关联较弱。
- **关键技术**: `conditional error principle`, `adaptive design`, `interim monitoring`, `type I error control`, `clinical trial design`
- **为什么对您有用**: 本文属于临床试验统计方法的应用性工作，与您的primary interests（因果推断、高维统计、U统计量、半参效率理论）的直接关联较弱。其核心方法（条件错误率原则）在序贯检验框架下控制I类错误，但未涉及您武器库中的具体工具（如higher-order U-statistics、minimax bound、semiparametric efficiency）。作为gateway reading，本文对流行病学或临床试验应用方向有一定参考价值，但技术新颖性和可迁移性有限。暂不可做：核心机器（序贯检验的条件错误率）不在您的武器库中，且与您当前研究路径的交叉点较少。

### 15. [10.1093/biomtc/ujad022](https://doi.org/10.1093/biomtc/ujad022) — A generalized phase 1-2-3 design integrating dose optimization with confirmatory treatment comparison
- **作者**: Yong Zang, Peter F Thall, Ying Yuan
- **期刊/来源**: Biometrics
- **机构**: Indiana University – Purdue University Indianapolis · The University of Texas MD Anderson Cancer Center
- **分类**: vol 80 · issue 1
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文提出一种广义的1-2-3期临床试验设计（Gen 1-2-3），将剂量优化与确证性治疗比较整合在一个统一框架中。设计从1-2期试验开始，利用剂量可接受性和最优性标准识别一组候选剂量（而非单一剂量）。在中间阶段（stage 2），将额外患者随机分配至候选剂量和活性对照组，并利用stage 1和stage 2患者的生存时间数据选择最优剂量。随后，基于所选最优剂量相对于对照在生存时间上提供实质性改善的预测概率，做出是否进入3期试验的Go/No Go决策。模拟研究表明，与Chapple和Thall (2019)的设计及两种传统设计相比，Gen 1-2-3具有更优的操作特征。该设计属于临床试验方法学，与您的主要研究兴趣（因果推断、高维统计等）无直接交集。
- **关键技术**: `phase 1-2-3 design`, `dose optimization`, `predictive probability`, `Go/No Go decision`, `survival time analysis`
- **为什么对您有用**: 本文属于临床试验设计方法学，与您的主要研究兴趣（因果推断、高维统计、半参理论等）无直接技术交集。武器库中的工具（如非参统计、U统计量）在此处无直接应用口子。作为应用领域文献，其方法学新颖性有限（novelty_flag: application），不推荐深入阅读。

### 16. [10.1093/biomtc/ujad019](https://doi.org/10.1093/biomtc/ujad019) — A flexible framework for spatial capture-recapture with unknown identities
- **作者**: Paul van Dam-Bates, Michail Papathomas, Ben C Stevenson, Rachel M Fewster, Daniel Turek, Frances E C Stewart et al.
- **期刊/来源**: Biometrics
- **机构**: University of St Andrews · University of Auckland · Williams College · Wilfrid Laurier University · University of Cape Town
- **分类**: vol 80 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文提出一个灵活的框架，将空间捕获-再捕获（SCR）模型推广到个体身份未知的情形。核心设定是将检测过程建模为标记泊松过程：一个计数过程描述所有动物的检测事件，一个标记分布描述观测到的信息（如身份、检测位置、性别等）。当个体无法唯一识别时，观测标记来自由动物活动中心和额外特征定义的混合分布。该方法统一了已有的潜在身份SCR模型和声学SCR模型，允许在身份缺失时仍能估计密度。通过渔貂相机陷阱调查和开普半岛苔蛙声学调查两个真实数据集验证，并辅以模拟研究。结果表明，加入性别或到达时间等额外标记的潜在身份SCR是估计动物密度的可靠方法。
- **关键技术**: `marked Poisson process`, `spatial capture-recapture`, `latent identity mixture model`, `acoustic SCR`
- **为什么对您有用**: 本文属于应用统计方法开发，与您的主要兴趣（因果推断、高维统计等）无直接技术重叠。但作为流行病学/生态学应用的一个例子，它展示了如何处理缺失标识符的计数数据，其混合模型框架对处理部分可观测的潜在变量问题有一定参考价值。武器库中非参数统计和M估计理论可用于分析此类模型的识别性和估计效率，但核心问题（空间点过程与身份缺失）不在您当前技术栈的焦点上，属于暂不可做的方向。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

