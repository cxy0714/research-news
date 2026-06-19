# Biostatistics — Vol 25  Issue 1  ·  2026-06-20

- 共 14 篇 · Biostatistics
- 目录核对 ⚠️ 疑似漏 2 篇（对照 OpenAlex 16 篇）：10.1093/biostatistics/kxac041、10.1093/biostatistics/kxac042

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期论文大致聚为三条主线：一是因果推断与替代终点评估，涉及时间序列随机干预、中介分析及平台试验半参数建模；二是流行病学中的时空与缺失数据建模，聚焦多重暴露滞后效应、暴露不确定性量化、结局非随机缺失插补及时空变系数；三是假设检验与计算方法，涵盖高维稀疏信号检验、单细胞数据选择性推断、盲态自适应设计、Cox模型在线化及聚类指标修正。

因果推断与替代终点主线推进了不同设定下的效应识别与异质性刻画。时间序列因果方面，热浪警报干预一文针对冷天处理概率近零导致的positivity失效，提出incremental time-varying propensity score (ItvPS)定义随机干预estimand，在弱化overlap下实现非参数识别与方差上界推导；替代终点方面，两篇论文从不同切面处理异质性：肿瘤meta-analysis一文用联合frailty模型分解中介间接效应占比以量化surrogacy，平台试验一文则用Dirichlet过程混合先验构建分层贝叶斯半参数模型，自动识别替代效果异质子群。

流行病学建模主线集中处理环境健康研究中的复杂结构与测量缺陷。多重暴露一文以spike-and-slab先验与半参数样条基解决高维暴露-滞后效应的变量选择与交互识别；暴露不确定性一文通过核密度估计（KDE）将第一阶段暴露后验完整传递至第二阶段健康模型；结局缺失一文针对登记非覆盖导致的非随机缺失，用mover–stayer模型结合半参数工作模型进行两步多重插补；时空变系数一文则以INLA推断贝叶斯空间变系数，刻画PM2.5效应的空间异质。

假设检验与计算主线针对特定数据结构修正推断逻辑与计算瓶颈。稀疏信号检验一文对比variant set与phenotype set两类set-based检验，推导不同相关性结构下的power bounds；单细胞推断一文利用count splitting将泊松计数随机分割，解决隐变量估计与关联检验的数据重复使用导致的FDR失控；Cox在线化一文将偏似然改写为可分解目标函数以兼容SGD与神经网络；聚类指标一文修正无监督discordance指标对group balance的依赖并给出近似抽样加速算法。

与因果推断方向最贴的是热浪警报ItvPS随机干预与平台试验Dirichlet过程半参数替代评估两篇；与半参数效率/非参数建模相关的是多重暴露滞后样条建模与时空变系数INLA推断；关注高维与假设检验逻辑的读者可优先看稀疏信号set-based检验与单细胞count splitting选择性推断。

## 因果推断  *(causal_inference, 3 篇)*

### 1. [10.1093/biostatistics/kxad002](https://doi.org/10.1093/biostatistics/kxad002) · [arXiv](https://arxiv.org/abs/2102.10478) — Assessing the causal effects of a stochastic intervention in time series data: are heat alerts effective in preventing deaths and hospitalizations?
- **作者**: Xiao Wu, Kate R Weinberger, Gregory A Wellenius, Francesca Dominici, Danielle Braun
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 1 · pp 57-79
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在时间序列因果推断设定下，目标是评估热浪警报对死亡与住院的干预效应，核心难点是冷天发出警报的概率近零导致经典 positivity/overlap 假设失效。作者提出 incremental time-varying propensity score (ItvPS) 随机干预：将第 t 天基于历史信息的处理概率乘以 odds ratio δ_t，定义新类因果 estimand。理论证明该 estimand 在弱化 overlap 下可识别，并提出基于 ItvPS 的非参数估计量并导出其方差上界。方法进一步通过空间 meta-analysis 扩展至多站点时间序列，模拟显示估计量在 bias 与 RMSE 上表现良好。实证应用于 2837 个美国县域 Medicare 数据，评估增加热浪警报概率的因果效应。对您有用：此文的 ItvPS 随机干预与弱化 overlap 思路可直接迁移至 longitudinal causal inference 中处理 positivity 违反的设定。
- **关键技术**: `incremental propensity score intervention`, `time-varying propensity score`, `stochastic intervention`, `weak overlap assumption`, `nonparametric estimation`, `spatial meta-analysis`
- **为什么对您有用**: 直接连接 longitudinal causal inference 子方向，用 ItvPS 随机干预绕过经典 positivity 假设的思路对处理时间序列/纵向数据中 overlap 违反有明确方法论价值。可用 very_familiar 的 estimation theory in causal inference 分析其非参数估计量的效率性质（是否达到 semiparametric efficiency bound），或用 moderately_familiar 的 semiparametric theory 探索该 estimand 的 influence function 与更优估计量构造。**中期可做**：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，以推导该随机干预 estimand 的有效影响函数与可能的双稳健/交叉拟合估计量。

### 2. [10.1093/biostatistics/kxac044](https://doi.org/10.1093/biostatistics/kxac044) — Time-to-event surrogate endpoint validation using mediation analysis and meta-analytic data
- **作者**: Quentin Le Coënt, Catherine Legrand, Virginie Rondeau
- **期刊/来源**: Biostatistics
- **机构**: Inserm · Bordeaux Population Health · UCLouvain
- **分类**: vol 25 · issue 1 · pp 98-116
- 相关性 8/10 · novelty: `application`
- **摘要**: 在肿瘤学 meta-analytic 数据设定下，本文研究如何验证 censored time-to-event 替代终点（surrogate endpoint），核心 estimand 为治疗对最终终点（如 OS）的总效应中经由替代终点（如 TTR）传递的间接效应占比。方法采用 mediation 分析将总效应分解为直接与间接效应，并通过 trial-level random effects 的联合模型（joint frailty model）刻画 meta-analytic 层级的异质性；从模型参数直接计算间接效应占比作为 surrogacy 指标。理论层面依赖 frailty 模型的参数估计一致性，但未给出 semiparametric efficiency bound 或 influence function 分析；实证应用于可切除胃癌数据，验证 TTR 作为 OS 替代终点的可行性。对您有用：本文将 mediation 与 surrogate validation 结合，是 longitudinal/mediation 因果推断在流行病学应用的一个具体实例。
- **关键技术**: `mediation analysis`, `time-to-event surrogate validation`, `joint frailty model`, `meta-analytic random effects`, `indirect effect proportion`
- **为什么对您有用**: 本文连接 causal inference 的 mediation 子方向与 epidemiology 的 oncology 队列数据应用，属于具体应用场景下的参数化建模。您可用 semiparametric theory / efficiency bound 的武器库审视其 frailty 模型：当前方法依赖参数化 joint model，一个自然的 follow-up 是为 censored mediation 的间接效应占比构造 semiparametric efficient estimator 或 influence function，这属于立即可做——用 very_familiar 的 nonparametric statistics 与 moderately_familiar 的 semiparametric theory 即可动手。

### 3. [10.1093/biostatistics/kxac053](https://doi.org/10.1093/biostatistics/kxac053) · [arXiv](https://arxiv.org/abs/2208.09869) — Flexible evaluation of surrogacy in platform studies
- **作者**: Michael C Sachs, Erin E Gabriel, Alessio Crippa, Michael J Daniels
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 1 · pp 220-236
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在平台试验（platform studies）中，评估替代终点（surrogate）的预测价值是一个因果推断问题，但现有方法未针对平台试验特有的异质性（人群、治疗、实施质量）进行设计。该文提出一个分层贝叶斯半参数模型，以Dirichlet过程混合分布作为非参数先验来刻画处理对替代终点效应与对临床结局效应之间的联合分布。模型自动识别替代效果不同的子群（clusters），允许在不同治疗环境中灵活预测。模拟显示该方法在均方误差和覆盖概率上优于标准分层贝叶斯方法。作者以ProBio试验为原型构造示例，展示了发现替代终点有用和无用子群的能力。该工作对关注因果推断中替代指标评估、特别是希望将半参数非参数工具用于实际试验设计的统计学家有参考价值。
- **关键技术**: `Dirichlet process mixture`, `hierarchical Bayesian semiparametric model`, `platform studies`, `trial-level surrogate evaluation`, `cluster identification`, `treatment effect prediction`
- **为什么对您有用**: 本文属于流行病学与因果推断的交叉领域，直接连接您对替代指标（surrogacy）评估和平台试验设计的方法学兴趣。它采用非参数贝叶斯（DP mixture）建模，与您非常熟悉的非参数统计和因果推断中的估计理论形成互补——您可以借助自己的极熟武器（如 minimax bound 检验其潜在识别条件是否紧、用 HOIF 分析其效率损失）来评估该方法是否可进一步推导出半参数效率界。随访建议：这是一个中期可做的方向——需要先在 moderately_familiar 的因果识别理论中理清平台试验下替代指标的可识别条件，再结合 DML 或正交得分提升效率。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1093/biostatistics/kxac036](https://doi.org/10.1093/biostatistics/kxac036) — Differences in set-based tests for sparse alternatives when testing sets of outcomes compared to sets of explanatory factors in genetic association studies
- **作者**: Ryan Sun, Andy Shi, Xihong Lin
- **期刊/来源**: Biostatistics
- **机构**: The University of Texas MD Anderson Cancer Center · Harvard University
- **分类**: vol 25 · issue 1 · pp 171-187
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 本文系统比较了高维遗传关联研究中两类 set-based 检验的相对表现：一类将多个遗传变异作为解释变量集检验单个表型（variant set → phenotype），另一类将单个变异作为解释变量检验多个表型集（variant → phenotype set）。核心问题是：在稀有弱信号（sparse alternatives）设定下，Higher Criticism、Berk-Jones 等基于检测边界（detection boundary）的检验方法，其操作特征如何受协变量和结果之间相关性结构的影响？作者推导了新的 power bounds，能直接刻画不同设定下检验的相对效能，并揭示了两类 setting 中相关结构对判别能力的相反作用。通过肺癌 eQTL 的真实数据实例和模拟研究，验证了理论发现对实际研究设计的指导意义。该工作将检测边界理论从传统的 single-test 情境拓展到多变量 group-test 比较，为高维假设检验中信号稀疏性下的检验选择提供了理论支撑，与您的高维统计和假设检验兴趣直接相关。
- **关键技术**: `Higher Criticism`, `Berk-Jones test`, `detection boundary`, `set-based association tests`, `power bounds`, `rare weak signals`
- **为什么对您有用**: 该论文直接关联您 primary interest 中的高维假设检验子方向——稀疏信号检测的边界性能分析。您 very_familiar 武器库中的 minimax bounds 和 high-dimensional asymptotics 可直接用于验证这些 power bounds 是否紧致，或将其推广至更一般的协方差结构。立即可做：利用您已有的 minimax 分析技术，可以复现并拓展本文的功率界限，检验其在不同稀疏程度下的最优性。

### 2. [10.1093/biostatistics/kxac047](https://doi.org/10.1093/biostatistics/kxac047) · [arXiv](https://arxiv.org/abs/2207.00554) — Inference after latent variable estimation for single-cell RNA sequencing data
- **作者**: Anna Neufeld, Lucy L Gao, Joshua Popp, Alexis Battle, Daniela Witten
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 1 · pp 270-287
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在单细胞RNA测序数据分析中，研究人员常常先估计表征细胞状态的隐变量（如细胞类型或伪时间），然后用同一数据对每个基因与估计得到的隐变量之间的关联进行假设检验。标准p值方法因数据重复使用而无法保证FDR控制或Type1误差率。作者提出count splitting框架，在泊松数据假设下，将每个基因的计数随机分割成独立的两部分：一部分用于隐变量估计，另一部分用于推断，从而适用于任意隐变量估计技术和推断方法。通过模拟实验和真实分化干细胞数据，展示了该方法在保持检验功效的同时有效控制Type1误差。由于单细胞RNA-seq数据的Poisson结构，该方法在选择性推断领域开辟了新思路，对您的假设检验兴趣（特别是多重比较和后选择推断）有直接参考价值。
- **关键技术**: `count splitting`, `data splitting for inference`, `Poisson assumption`, `latent variable estimation`, `Type 1 error control`, `single-cell RNA-seq`
- **为什么对您有用**: 本文属于 hypothesis testing 的后选择推断子方向，与您 primary interest 中的数学统计与假设检验高度吻合。您熟悉的 nonparametric statistics 和 high-dimensional asymptotics 可直接用于分析 count splitting 在非泊松分布下的渐近性质或稳健性扩展，属于**立即可做**的范围：用非参数工具研究该方法对泊松假设偏离的敏感性。

### 3. [10.1093/biostatistics/kxac040](https://doi.org/10.1093/biostatistics/kxac040) · [arXiv](https://arxiv.org/abs/2206.09639) — Adaptive clinical trial designs with blinded selection of binary composite endpoints and sample size reassessment
- **作者**: Marta Bofill Roig, Guadalupe Gómez Melis, Martin Posch, Franz Koenig
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 1 · pp 237-252
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在两臂随机对照试验中，当单一二元终点所需样本量过大时常用复合终点（CE），但 CE 的样本量计算依赖各成分效应量、事件概率及成分间相关性，而相关性在文献中常缺失。本文提出一种自适应设计：在期中分析时基于盲态数据选择 CE 或其最重要成分作为主要终点（选择规则为估计所需样本量更小者），并同时重估样本量。方法通过模拟验证：自适应设计在功效上不低于非自适应设计，且在规划阶段相关性误设时仍能达到目标功效并保持 type 1 error。所有计算在 R 中实现并以腹膜透析试验示例。对您可能有用：该设计本质上是一个带盲态数据重估的 adaptive hypothesis testing 问题，展示了如何在保持 type 1 error 下做终点选择。
- **关键技术**: `adaptive clinical trial design`, `blinded sample size reassessment`, `composite binary endpoint`, `type 1 error control`, `interim analysis`
- **为什么对您有用**: 本文连接到 hypothesis testing 子方向中的 adaptive design 与 type 1 error 控制问题。研究者武器库中的 M-estimation theory 与 nonparametric statistics 可用于分析该盲态选择规则的渐近性质（如选择后 estimator 的 influence function 与条件 type 1 error 界），这是攻入本文理论缺口的具体口子。Follow-up 判断：中期可做——需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以严格推导 adaptive selection + sample size reassessment 下 estimator 的渐近分布与精确 type 1 error 界。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1093/biostatistics/kxac039](https://doi.org/10.1093/biostatistics/kxac039) — An online framework for survival analysis: reframing Cox proportional hazards model for large data sets and neural networks
- **作者**: Aliasghar Tarkhan, Noah Simon
- **期刊/来源**: Biostatistics
- **机构**: University of Washington
- **分类**: vol 25 · issue 1 · pp 134-153
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 针对大规模生存数据及神经网络模型，传统Cox比例风险模型的偏似然函数不具备可分性，无法直接应用随机梯度下降（SGD），且在内存受限时计算不稳定。本文提出一种重新公式化Cox模型的新框架，通过将偏似然改写为可分解的在线目标函数，使其天然兼容SGD与小批量优化。新目标函数在统计上等价于原偏似然，但允许逐样本或分批更新，从而支持流式数据和超出内存的训练集。该框架还自然扩展到深度神经网络，将生存层嵌入端到端学习管线，避免了对完整协方差矩阵的存储和求逆。实验表明，在大型队列数据上，该方法在保持预测精度的同时显著降低了计算开销，且对缺失值和不均匀事件时间具有鲁棒性。对您而言，这一在线化技巧可以移植到因果推断中的纵向生存终点分析，尤其是您熟悉的M估计和逆问题框架下，可能实现高效的大规模拟合。
- **关键技术**: `stochastic gradient descent (SGD)`, `reformulated partial likelihood`, `online survival learning`, `neural survival models`, `large-scale Cox regression`
- **为什么对您有用**: 本文直接回应统计计算中大规模数据拟合的痛点，与您熟悉的高维渐近和软件工程经验高度契合。您可以用M估计和逆问题方法分析该在线框架的收敛性，或将其嵌入因果推断中的生存终点处理，为流行病学队列研究提供高效工具。立即可做：您已有的软件开发能力足以复现并扩展该算法，且其思路对因果中介分析中的时间-事件终点亦有直接参考价值。

### 2. [10.1093/biostatistics/kxac035](https://doi.org/10.1093/biostatistics/kxac035) — A scalable and unbiased discordance metric with <i>H</i> +
- **作者**: Nathan Dyjack, Daniel N Baker, Vladimir Braverman, Ben Langmead, Stephanie C Hicks
- **期刊/来源**: Biostatistics
- **机构**: Johns Hopkins University
- **分类**: vol 25 · issue 1 · pp 188-202
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在无监督聚类设定下，当缺乏外部真实标签时，常依赖内部有效性指标（如紧密度/分离度）评估聚类质量，但不同 dissimilarity 量纲差异导致指标不可比。此前提出的 scale-agnostic discordance 指标 $G_+$ 虽消除量纲依赖，但其计算在大规模数据上极慢，且本文证明 $G_+$ 的值会随各组样本比例（group balance）变化而偏移，这是不理想的性质。作者提出修正指标 $H_+$，通过调整 $G_+$ 的构造使其不再依赖 group balance，并在模拟与单细胞 RNA-seq 数据上验证了 $H_+$ 的稳定性。为解决计算瓶颈，作者基于近似/抽样方法给出 scalable 算法，并发布 R 包 fasthplus。对您可能有用：本文将高阶 U-statistic/two-sample statistic 的计算瓶颈与 scalable 算法设计直接关联，是统计计算与 U-stat 实际求值交叉的典型案例。
- **关键技术**: `discordance metric`, `group balance correction`, `scalable U-statistic computation`, `nearest-neighbor approximation`, `internal cluster validity`
- **为什么对您有用**: 本文核心落在统计计算与 U-stat 求值的可扩展性上：$G_+$ 本质上是基于 pairwise dissimilarity 的高阶统计量，其精确求值成本为 $O(n^2)$，作者提供的 scalable 近似算法直接触及您 very_familiar 中的 computation of higher-order U-statistics。您可以用 treewidth / tensor contraction / einsum 视角重新审视 $H_+$ 的计算图，看是否能给出比 fasthplus 更优的 contraction order 或复杂度下界。**立即可做**：用 very_familiar 的 U-stat einsum 框架分析 $H_+$ 的精确求值复杂度，并与作者的近似算法做对比验证。

## 流行病学  *(epidemiology, 5 篇)*

### 1. [10.1093/biostatistics/kxac038](https://doi.org/10.1093/biostatistics/kxac038) · [arXiv](https://arxiv.org/abs/2107.14567) — Multiple exposure distributed lag models with variable selection
- **作者**: Joseph Antonelli, Ander Wilson, Brent A Coull
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 1 · pp 1-19
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在环境流行病学中，多重暴露分布式滞后模型旨在同时估计多个环境暴露的时间滞后效应（关键窗口）并筛选重要暴露及其交互。本文提出一种贝叶斯方法，以 spike-and-slab 先验对暴露系数进行变量选择，并用半参数分布式滞后曲线（如样条基）刻画暴露-时间效应。模型中还引入交互项先验，以识别不同暴露在不同关键窗口间的协同或拮抗作用。通过贝叶斯 MCMC 进行后验推断，并引入改进策略以提高检测有害暴露的效能。将方法应用于科罗拉多州出生体重数据，评估孕期多种空气污染物（如 PM2.5、O3）对出生体重的滞后效应，识别出不同污染物的关键窗口及若干交互。对您而言，本文是流行病学中高维暴露-滞后建模的实用方法范本，其数据集和变量选择框架可作为您关注的因果推断应用中暴露混杂筛选的参考。
- **关键技术**: `distributed lag models`, `spike-and-slab priors`, `semiparametric curves`, `variable selection`, `interaction detection`, `Bayesian MCMC`
- **为什么对您有用**: 本文属于流行病学应用方向，直接连接到您secondary interest中的流行病学数据集与因果推断应用。具体而言，它展示了在高维暴露-滞后设定下使用贝叶斯变量选择识别关键窗口，但其核心工具（贝叶斯 MCMC、spike-and-slab）不在您当前武器库中（缺少贝叶斯建模经验），因此直接复刻或改进难度较大，属于暂不可做范畴。不过，问题本身（多重暴露滞后效应、交互检测）与您熟悉的高维统计和因果推断有天然联系，可作为入门读物了解环境流行病学数据结构和问题设定，为未来可能的方法学交叉（如使用非参数或去偏机器学习替代贝叶斯部分）埋下伏笔。全文值得快速浏览，重点看数据格式和模型结构。

### 2. [10.1093/biostatistics/kxac043](https://doi.org/10.1093/biostatistics/kxac043) — Joint modeling of longitudinal and competing-risk data using cumulative incidence functions for the failure submodels accounting for potential failure cause misclassification through double sampling
- **作者**: Christos Thomadakis, Loukia Meligkotsidou, Constantin T Yiannoutsos, Giota Touloumi
- **期刊/来源**: Biostatistics
- **机构**: National and Kapodistrian University of Athens · Indiana University – Purdue University Indianapolis
- **分类**: vol 25 · issue 1 · pp 80-97
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对纵向标记物和竞争风险数据的联合建模问题，提出一类灵活的共享参数模型。生存子模型直接使用累积发病函数（CIF），假设CIF依赖于去除测量误差的标记物真实轨迹，并采用广义odds率变换（包含比例子分布风险模型为特例）。同时，模型通过双重抽样（随机子样本已知真实失败原因）来校正潜在的失败原因错误分类。为获得可解释的临床预后信息，论文还定义了基于标记物值和竞争风险的互斥状态，并在贝叶斯框架下推导了状态占据和转移概率的后验样本。模拟研究验证了方法的有限样本表现，HIV感染者实际数据的应用展示了其可行性。该工作虽非因果推断，但其处理测量误差和错误分类的共享参数框架可迁移至纵向因果中介分析或时变混淆校正；HIV数据集也为评估因果方法的敏感度提供了现实场景。
- **关键技术**: `shared random effects model`, `cumulative incidence function`, `generalized odds-rate transformation`, `double sampling for misclassification`, `Bayesian posterior sampling`
- **为什么对您有用**: 本文属于流行病学领域（secondary interest）的纵向竞争风险数据分析，其处理测量误差和原因错误分类的方法与因果推断中的时变混淆校正及中介分析有相通之处。武器库中'very_familiar'的纵向数据估计经验和'moderately_familiar'的因果推断识别理论可直接用于批判该模型的识别假设（如无交互的测量误差结构）。作为流行病学应用，本文提供了明确的HIV数据集和分析流程，适合作为入门读物理解该领域的数据结构，值得花时间深入阅读以获取可迁移的分析模板。

### 3. [10.1093/biostatistics/kxac034](https://doi.org/10.1093/biostatistics/kxac034) · [arXiv](https://arxiv.org/abs/2203.16627) — A Bayesian framework for incorporating exposure uncertainty into health analyses with application to air pollution and stillbirth
- **作者**: Saskia Comess, Howard H Chang, Joshua L Warren
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 1 · pp 20-39
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 该论文针对环境暴露与健康关联分析中两阶段建模忽视暴露预测不确定性的问题，在贝叶斯框架下提出了一种灵活的核密度估计（KDE）方法。该方法利用第一阶段暴露模型的后验样本，通过KDE逼近暴露分布的完整后验，并将其作为输入纳入第二阶段的健康结果模型，从而更准确地量化关联。作者推导了高效模型拟合所需的完全条件分布，并与现有方法（如多重插补、贝叶斯后验预测）建立了理论联系。模拟研究表明，该方法在多种设定和模型比较指标上普遍优于忽略不确定性或简单处理不确定性的方法。实证应用分析了2011–2015年新泽西州逐日细颗粒物（PM2.5）滞后暴露与死产数的关联，发现分娩前3天的高暴露与风险升高相关。论文附带了R包KDExp，便于方法复现和推广。对于研究者的流行病学secondary interest，本文提供了一个完整的暴露-健康分析pipeline，并展示了真实数据（滞后回归）的应用范式，其非参数后验传播策略也可迁移到其他因果推断中涉及预测误差的设定。
- **关键技术**: `Bayesian kernel density estimation`, `two-stage modeling with exposure uncertainty`, `posterior propagation`, `full conditional distributions`, `R package KDExp`
- **为什么对您有用**: 本文属于流行病学应用，是研究者secondary interest的具体方向（空气污染与围产期健康）。作为统计学出身的研究者，本文的贝叶斯KDE方法和后验传播策略可以连接到very_familiar中的“非参数统计”与“软件工具开发”经验，值得细读其R包实现。整体上，本文是流行病学暴露-反应分析的优秀入门读物，研究者已具备理解该方法所需的核心统计知识（贝叶斯计算、核密度估计、层次模型），可以快速抓住方法要点和实证分析流程。

### 4. [10.1093/biostatistics/kxac049](https://doi.org/10.1093/biostatistics/kxac049) — An imputation approach for a time-to-event analysis subject to missing outcomes due to noncoverage in disease registries
- **作者**: Joanna H Shih, Paul S Albert, Jason Fine, Danping Liu
- **期刊/来源**: Biostatistics
- **机构**: National Cancer Institute · Division of Cancer Epidemiology and Genetics
- **分类**: vol 25 · issue 1 · pp 117-133
- 相关性 4/10 · novelty: `application`
- **摘要**: 本研究针对美国缺少全国性癌症登记导致队列研究中部分参与者结局缺失的问题，提出了一种基于多重插补的时间-事件分析方法。核心设定是：患者癌症诊断结果依靠各州登记数据，但只有部分州参与，因此未覆盖州的参与者结果缺失且非随机。方法分两步：第一步用 mover–stayer 模型借助纵向问卷上的自报诊断插补参与者的登记覆盖状态；第二步基于第一步识别的覆盖样本，拟合一个半参数工作模型（含基线风险函数和协变量），插补缺失的登记结果。模拟表明该方法比直接删除未覆盖者或简单插补等方法在偏倚和均方误差上均有改善。论文将方法应用于美国放射技术人员队列与32州联合登记数据的链接分析，验证了实际可行性。对您而言，这是一个流行病学真实数据缺失问题的应用案例，其中半参数插补策略与您的非参数和半参数估计知识可直接对接。
- **关键技术**: `mover–stayer model`, `semiparametric working model`, `multiple imputation`, `time-to-event analysis`, `disease registry noncoverage`
- **为什么对您有用**: 该论文属于流行病学应用，对您而言是 gateway reading：(1) 问题背景和数据结构清晰，不依赖流行病学专有名词，适合作为入门读物；(2) 您熟悉的非参数统计和 M-估计理论足以理解其半参数工作模型和插补逻辑，无需额外学习新工具；(3) 值得花时间快速阅读全文，积累疾病登记数据缺失的典型处理思路，后续若涉及类似选择偏差的因果推断研究（如基于登记的队列），该策略可直接迁移。

### 5. [10.1093/biostatistics/kxac046](https://doi.org/10.1093/biostatistics/kxac046) — Spatiotemporal varying coefficient model for respiratory disease mapping in Taiwan
- **作者**: Feifei Wang, Congyuan Duan, Yang Li, Hui Huang, Ben-Chang Shia
- **期刊/来源**: Biostatistics
- **机构**: Renmin University of China · Sun Yat-sen University · Fu Jen Catholic University
- **分类**: vol 25 · issue 1 · pp 40-56
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文旨在研究PM2.5对台湾地区呼吸疾病就诊率的影响。利用328个行政区的面板数据，构建了一个贝叶斯时空变系数模型：空间部分通过条件自回归先验刻画区域随机效应，时间趋势采用参数形式（如线性或二次项），PM2.5的效应允许随空间变化。模型使用集成嵌套拉普拉斯近似（INLA）进行高效推断，无需MCMC采样。模拟研究表明，相比忽略时空异质性的模型，本文方法在参数估计和预测性能上均有提升。实证结果显示，PM2.5与就诊率存在显著正向关联，且效应强度在台湾北部和西部工业区更为突出。该工作展示了空间变系数模型在流行病学制图中的实际应用流程，对于研究空气污染健康效应的统计学家是一份易读的应用参考。
- **关键技术**: `Bayesian hierarchical model`, `spatially varying coefficient`, `integrated nested Laplace approximation (INLA)`, `conditional autoregressive prior`, `disease mapping`
- **为什么对您有用**: （1）该论文属于流行病学应用方向，使用空间统计方法分析空气污染对健康的关联，贴合您的 secondary interest——流行病学。（2）论文中的空间变系数模型本质上是一种非参数平滑（随空间变化的系数），可用您非常熟悉的 nonparametric statistics 视角理解其偏置-方差权衡和光滑度选择。（3）作为流行病学入门应用，该文清楚呈现了数据结构和贝叶斯建模流程，适合快速了解空间疾病制图领域；但若要深入改进模型（如引入因果推断中的混杂调整），需先补充空间统计和 INLA 的专门知识，目前属于“暂不可做”方向。

## 其他  *(other, 1 篇)*

### 1. [10.1093/biostatistics/kxac032](https://doi.org/10.1093/biostatistics/kxac032) — CoCoA: conditional correlation models with association size
- **作者**: Danni Tu, Bridget Mahony, Tyler M Moore, Maxwell A Bertolero, Aaron F Alexander-Bloch, Ruben Gur et al.
- **期刊/来源**: Biostatistics
- **机构**: Penn Center for AIDS Research · University of Pennsylvania · National Institute of Mental Health · Lifespan
- **分类**: vol 25 · issue 1 · pp 154-170
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文提出 CoCoA（条件相关模型与关联大小框架），旨在解决如速度-准确性权衡条件于第三变量（如持续性注意力）时的统计推断问题。传统回归或相关分析无法直接建模对称关系的条件依赖性，因此作者构建基于似然的参数模型来估计条件相关系数作为协变量的函数。同时引入关联大小度量（association size），在控制混杂后量化相关强度，效果量与相关系数尺度对应。在模拟中，似然法相比改编自基因组研究的半参数估计量，在理想设定和模型误设下均表现出更低的偏差与方差。应用Philadelphia神经发育队列的神经认知数据，发现持续性注意力越高，复杂推理任务中速度-准确性耦合越强（控制年龄后）。该框架为条件相关提供了互补于回归建模的视角，且似然推断的稳健性对非统计专业人员友好，适合队列研究中相关结构的假设检验。该方法在流行病学或神经科学队列的条件相关分析中有直接应用价值。
- **关键技术**: `conditional correlation model`, `likelihood-based estimation`, `association size measure`, `semiparametric estimator comparison`, `model misspecification robustness`
- **为什么对您有用**: 该论文直接对应您secondary interest中的流行病学应用领域（神经队列数据集），其条件相关建模思路可迁移至因果推断中的条件独立性检验或效应修饰分析。您对非参数统计和估计理论的熟悉程度可快速验证似然法在小样本下的渐近性质，并能用高维渐近工具扩展至多变量调整场景。立即可做：利用您very_familiar中的非参数统计和估计理论，可直接复现并对比其半参数估计量的效率损失。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

