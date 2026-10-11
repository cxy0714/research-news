# Biometrics — Vol 82  Issue 4  ·  2026-10-10

- 共 8 篇 · Biometrics
- 目录核对 ✅ 8 篇全部抓到（对照 OpenAlex 8 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期共8篇论文，主线大致可归为三类：因果推断与可迁移性（2篇）、删失数据与生存/事件时间分析（2篇）、以及元分析推断（2篇），其余两篇分别落在化学信息学高斯过程建模和神经影像贝叶斯深度学习。因果与生存两条线在方法上共享对“分布偏移”和“数据粗化”的处理关切，而元分析两篇则聚焦于小样本异质性下的推断校准，整体呈现从个体级数据到汇总统计量推断的梯度。

因果推断主线最值得展开。Transportable inference一文将熵平衡引入可迁移性设定，处理目标总体仅有协变量矩时的效应外推，并进一步允许对协变量偏移做参数化建模，同时纳入汇总统计量不确定性，给出渐近正态性与方差估计。Causal decomposition framework则转向健康差异的分解，在无未测混杂假设下用机器学习估计多中介的联合与单独贡献，并给出未测混杂下可修改差异的sharp bounds。两篇虽问题不同，但都依赖半参数或非参数识别策略，且都强调对模型设定偏差的稳健性——前者通过偏移建模，后者通过敏感性边界。若您关注因果推断中的外部有效性或中介分解，这两篇提供了可对照的估计框架。

删失数据与生存分析线同样有方法交叉。Generative estimation of conditional survival function用条件生成器学习观测时间与删失指示的联合分布，再构造Kaplan-Meier与Nelson-Aalen估计量，将深度生成与经典非参数估计结合并给出收敛性质。Meta-analytical federated surveillance针对潜伏期估计，在区间与右删失下用随机变分推断实现联邦学习，各机构仅交换局部变分参数，精度接近集中分析。两篇都处理数据不完整性问题，但前者侧重非参数估计的生成式构造，后者侧重分布式推断中的似然近似，方法工具差异明显，可互为补充。元分析两篇（Pseudo-data augmentation与Prediction intervals）则聚焦小样本异质性，前者用伪数据增广在HGN模型下直接估计风险比，后者用置信分布与Edgington方法构建预测区间，均针对传统方法在稀疏数据下的覆盖不足。

若按主题优先阅读，因果推断两篇（Transportable inference、Causal decomposition framework）与半参数效率、敏感性分析最直接相关；删失数据两篇（Generative estimation、Fed-SVI）适合关注非参数估计与分布式推断的读者；元分析两篇则对应用统计中的小样本推断校准有参考价值。其余两篇（高斯过程化学信息学、贝叶斯深度学习神经影像）偏应用，理论贡献有限，可视兴趣选读。

## 因果推断  *(causal_inference, 3 篇)*

### 1. [10.1093/biomtc/ujag170](https://doi.org/10.1093/biomtc/ujag170) · [arXiv](https://arxiv.org/abs/2603.02474) — Transportable inference using target population summary statistics under covariate shift
- **作者**: Ying Sheng, Yifei Sun, Chiung-Yu Huang
- **期刊/来源**: Biometrics
- **机构**: Chinese Academy of Sciences · Academy of Mathematics and Systems Science · New York University · Columbia University · University of California, San Francisco
- **分类**: vol 82 · issue 4
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究在目标总体仅有协变量汇总统计量（如矩）而无法获得个体层面数据时的效应可迁移性（transportability）推断问题，目标估计量为源总体到目标总体的平均处理效应或结局均值。作者首先将熵平衡（EB）方法引入可迁移性设定，通过调整源个体权重使其协变量矩与目标汇总统计量匹配，并建立了EB估计量的渐近正态性，同时提出考虑汇总统计量不确定性的方差估计。其次，针对EB可能无法正确指定协变量偏移形式的情形，提出一种更灵活的建模方法，允许对协变量偏移进行参数化建模，并同时处理偏移和汇总统计量的不确定性。该估计量同样具有渐近正态性，且其渐近方差可一致估计。模拟研究评估了有限样本表现，并利用SEER乳腺癌数据进行了实证分析。对您而言，本文属于因果推断中外部效度（external validity）与协变量偏移下的传输推断，与您关注的proximal CI和纵向因果推断中的transportability问题直接相关。
- **关键技术**: `entropy balancing`, `covariate shift`, `transportability`, `asymptotic normality`, `variance estimation`, `summary statistics`
- **为什么对您有用**: 本文直接连接您primary interest中的causal inference子方向——在目标总体仅有汇总统计量时的效应传输推断，属于identification与estimation的交叉。您可以用very_familiar的estimation theory in causal inference来审视其估计量的渐近性质，特别是EB的权重估计与目标矩匹配的收敛速度；同时，您moderately_familiar的semiparametric theory可用于评估其方差估计是否达到半参数效率界。中期可做：若想将方法推广到proximal CI设定（如利用negative control变量），需先在identification theory in causal inference上加强（moderately_familiar），但总体而言，本文方法的核心（矩匹配与权重调整）与您的武器库高度兼容，立即可做的是复现其模拟并检验其在纵向设定下的表现。

### 2. [10.1093/biomtc/ujag171](https://doi.org/10.1093/biomtc/ujag171) — Causal decomposition framework for quantifying intervenable cancer health disparities
- **作者**: Fan Xia, Sang Kyu Lee, Seonjin Kim, Kelly Blum, Hyokyoung G Hong, Alison J Canchola et al.
- **期刊/来源**: Biometrics
- **机构**: University of California, San Francisco · Konkuk University · Konkuk University Medical Center · Miami University · UCSF Helen Diller Family Comprehensive Cancer Center · National Cancer Institute · Department of Health and Human Services · National Cancer Registry
- **分类**: vol 82 · issue 4
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文提出一个非参数分解框架，用于量化健康结果差异中多个可干预中介变量的贡献，目标 estimand 是可修改差异（modifiable disparity）。在无未测混杂（mediator-outcome）假设下，结合因果中介分析和机器学习估计各中介的联合与单独效应。针对种族等不可改变特征，采用反事实干预公式化假设干预。为缓解模型设定偏差，引入非参数敏感性分析，给出未测混杂下可修改差异估计的 sharp bounds。方法应用于结直肠癌生存差异数据，识别高影响的可干预因素。对您而言，该文将因果分解与敏感性分析结合，且用非参数方法处理多中介，与您的因果推断和半参数理论兴趣直接相关。
- **关键技术**: `causal mediation analysis`, `nonparametric decomposition`, `sensitivity analysis`, `sharp bounds`, `machine learning`
- **为什么对您有用**: (1) 直接连接 causal inference 的 mediation 与 sensitivity analysis 子方向，且是流行病学应用（结直肠癌差异）；(2) 可用 very_familiar 的 estimation theory in causal inference 和 nonparametric statistics 来审视其估计量的收敛性，或用 moderately_familiar 的 semiparametric theory 检查其 sharp bounds 是否达到效率界；(3) 立即可做：基于其框架，用现有工具推导多中介的联合效应估计的渐近性质。

### 3. [10.1093/biomtc/ujag172](https://doi.org/10.1093/biomtc/ujag172) — Meta-analytical federated surveillance for incubation period with interval- and right-censored data with stochastic variational inference
- **作者**: Daisuke Yoneoka, Takayuki Kawashima, Yuta Tanoue, Shuhei Nomura, Akifumi Eguchi
- **期刊/来源**: Biometrics
- **机构**: National Institute of Infectious Diseases · The University of Tokyo · Information and Mathematical Science and Bioinformatics (Japan) · Tokyo University of Marine Science and Technology · Tohoku University · Chiba University
- **分类**: vol 82 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对传染病监测中潜伏期估计问题，提出一种联邦贝叶斯推断框架 Fed-SVI，以应对两类挑战：观测数据粗化（区间删失和右删失）以及患者级数据因隐私限制无法集中分析。方法将传统元分析的汇总统计思想扩展为迭代的模型化联邦方法，拟合分层对数正态模型，显式建模异质性并估计全局分布。各机构仅交换局部变分参数（汇总统计），通过截断正态分布的期望严格纳入粗化数据的似然贡献，中央服务器利用随机自然梯度上升聚合参数，支持小批量更新。模拟研究表明 Fed-SVI 的精度与完全集中分析几乎一致，且显著优于丢弃删失信息的朴素联邦或元分析方法。应用于来自 177 个机构的 COVID-19 行列表，结果与集中估计一致。该方法为现代数据网络中的隐私保护监测提供了可扩展、准确且隐私保护的解决方案。对您而言，本文的联邦推断与删失数据处理思路可迁移至纵向因果推断中的隐私保护场景，且其分层模型与变分推断技术可借鉴于您的因果推断研究。
- **关键技术**: `federated learning`, `stochastic variational inference`, `natural gradient ascent`, `hierarchical lognormal model`, `interval censoring`, `truncated normal expectation`
- **为什么对您有用**: 本文属于因果推断与统计计算交叉领域，其联邦框架与删失数据处理方法可应用于纵向因果推断中的隐私保护场景。您可尝试用您熟悉的变分推断或分层模型技术评估其收敛性，或探索将联邦思想融入您的因果推断方法中。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1093/biomtc/ujag164](https://doi.org/10.1093/biomtc/ujag164) · [arXiv](https://arxiv.org/abs/2205.09633) — Generative estimation of conditional survival function
- **作者**: Xingyu Zhou, Wen Su, Changyu Liu, Yuling Jiao, Xingqiu Zhao, Jian Huang
- **期刊/来源**: Biometrics
- **机构**: University of Iowa · University of Hong Kong · Hong Kong Polytechnic University · Wuhan University
- **分类**: vol 82 · issue 4
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文提出一种深度生成式方法，用于在删失数据下非参数估计条件生存函数和风险函数。核心思路是先用条件生成器学习观测时间与删失指示变量在给定协变量下的联合条件分布，再基于该生成器构造 Kaplan-Meier 和 Nelson-Aalen 估计量，从而得到条件风险与生存函数的估计。该方法将深度生成学习与生存分析中的经典非参数估计相结合，并建立了生成式非参数估计量的收敛性质。数值研究验证了所提方法的有效性。对您而言，该工作将深度生成模型与经典非参数估计结合，其收敛性分析思路可能对您在非参数与半参数理论方面的研究有参考价值。
- **关键技术**: `deep generative model`, `conditional generator`, `Kaplan-Meier estimator`, `Nelson-Aalen estimator`, `censored data`, `nonparametric estimation`
- **为什么对您有用**: 该论文属于非参数与半参数理论方向，与您的 primary interest 中的非参数估计和生存分析相关。其将深度生成模型引入经典非参数估计的框架，可能提供新的估计思路。您可以用 very_familiar 的非参数统计和 minimax 理论来审视其收敛速度是否最优，或探讨其在高维协变量下的表现。中期可做：需先熟悉深度生成模型的理论性质（属于 moderately_familiar 之外的领域）。

## 其他  *(other, 4 篇)*

### 1. [10.1093/biomtc/ujag169](https://doi.org/10.1093/biomtc/ujag169) — Pseudo-data augmentation for exact conditional likelihood inference in meta-analysis
- **作者**: Hisashi Noma
- **期刊/来源**: Biometrics
- **机构**: The Graduate University for Advanced Studies, SOKENDAI · The Institute of Statistical Mathematics
- **分类**: vol 82 · issue 4
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对二元结局的 meta-analysis，提出一种基于伪数据增广的统一似然框架，在 hypergeometric-normal (HGN) 模型下直接估计风险比（risk ratio），而传统似然方法（如二项-正态 GLMM 和 HGN）仅限于比值比尺度。该方法通过伪数据增广保持 HGN 的条件似然结构，同时得到 log-risk-ratio 的无偏估计方程。为提高小样本或稀疏数据下的推断精度，采用 jackknife 偏差和方差修正实现高阶推断。模拟研究显示估计近似无偏、置信区间覆盖良好；应用于已发表的 meta-analysis 表明该方法可解释、连贯且计算可行。
- **关键技术**: `pseudo-data augmentation`, `conditional likelihood`, `hypergeometric-normal model`, `jackknife bias correction`, `risk-ratio estimation`
- **为什么对您有用**: 本文属于应用统计方法学，涉及条件似然和高阶推断（jackknife），与您对假设检验和效率理论的兴趣有间接关联，但并非核心方向。作为 Biometrics 的应用论文，其伪数据增广技巧可能对您处理离散数据的推断问题有启发，但整体相关性一般。

### 2. [10.1093/biomtc/ujag167](https://doi.org/10.1093/biomtc/ujag167) · [arXiv](https://arxiv.org/abs/2510.13216) — Prediction intervals for random-effects meta-analysis based on confidence distributions and Edgington’s method
- **作者**: David Kronthaler, Leonhard Held
- **期刊/来源**: Biometrics
- **机构**: Prevention Institute
- **分类**: vol 82 · issue 4
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文研究随机效应元分析中平均效应的预测区间构建问题，目标是在存在研究间异质性时提供对未来效应量的预测分布。作者基于 Edgington 的 p 值合并方法和广义异质性统计量构造置信分布，以纳入异质性估计的不确定性。模拟表明，当研究数超过 3 时，95% 预测区间通常能达到名义覆盖，且在 20 个或更少研究的场景下能有效反映效应估计的偏态。忽略异质性估计不确定性的公式往往覆盖不足，凸显了调整的必要性。该方法为元分析中的预测推断提供了一种新途径，但属于应用统计方法，理论新颖性有限。
- **关键技术**: `confidence distributions`, `Edgington's method`, `generalized heterogeneity statistic`, `prediction intervals`, `random-effects meta-analysis`
- **为什么对您有用**: 本文属于统计推断方法，但更偏向应用统计（元分析），与您的主要兴趣（因果推断、高维、半参数等）关联较弱。不过，其置信分布和不确定性调整的思想可能对您处理纵向或异质性数据时的推断有启发。作为 gateway reading，本文方法学深度一般，但可作为了解元分析预测推断的入门读物。武器库中的非参数和半参数工具足以理解其方法，但无需深入跟进。

### 3. [10.1093/biomtc/ujag168](https://doi.org/10.1093/biomtc/ujag168) · [arXiv](https://arxiv.org/abs/2405.09989) — A Gaussian process model for chemoinformatics with application to the hazard classification of organic solvents
- **作者**: Arron Gosnell, Evangelos Evangelou
- **期刊/来源**: Biometrics
- **机构**: University of Bath
- **分类**: vol 82 · issue 4
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对有机溶剂水污染危害分类问题，提出一种基于化学结构相似性的高斯过程模型。核心假设是化学结构相似的溶剂更可能属于同一危害类别，相似性由化学空间上的非欧几里得度量 Tanimoto 距离刻画。模型将核函数设为 Tanimoto 距离的函数，并创新性地引入尺度参数以控制化合物间相关强度，提供额外灵活性。实证表明，考虑化合物间相关性相比忽略相关性的模型显著提升预测性能，且优于文献中的其他模型。此外，作者提出一种遗传算法，基于模型的两个准则识别影响化合物效能的关键特征，以促进化学发现。模拟研究验证了所提方法的适用性。
- **关键技术**: `Gaussian process`, `Tanimoto distance`, `non-Euclidean kernel`, `genetic algorithm`, `feature selection`
- **为什么对您有用**: 本文属于化学信息学应用，与您的主要兴趣（因果推断、高维统计等）无直接交集，但作为 Biometrics 期刊的应用论文，其高斯过程建模和特征选择思路对您可能有一定参考价值。不过，其方法学新颖性有限，且不涉及您武器库中的具体工具，因此仅作为一般性阅读，不值得深入跟进。

### 4. [10.1093/biomtc/ujag174](https://doi.org/10.1093/biomtc/ujag174) — A Bayesian deep learning framework for brain dynamic functional connectivity linked with cognition
- **作者**: Xinyuan Tian, Yuanshuang Guo, Shengxian Ding, Yifei Zhang, Denise Esserman, Yize Zhao
- **期刊/来源**: Biometrics
- **机构**: Yale University
- **分类**: vol 82 · issue 4
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文提出一个贝叶斯深度学习框架，用于分析大脑动态功能连接（FC）与认知表现的关系。模型将 FC 分解为动态和静态成分，动态部分用阈值高斯过程建模以捕捉平滑时间变化并诱导稀疏性，静态部分用带阈值层的深度神经网络学习非线性关系。通过深度核学习，动态成分被表示为连续过程，避免了对时间模式的强假设。在模拟中，该方法在预测精度和特征选择上优于现有方法；在青少年大脑认知发展（ABCD）研究中，识别出与认知表现显著相关的动态脑信号。该工作属于神经影像统计应用，方法上结合了贝叶斯非参数和深度学习，但对统计理论贡献有限。
- **关键技术**: `Bayesian deep learning`, `thresholded Gaussian process`, `deep kernel learning`, `dynamic functional connectivity decomposition`, `sparsity-inducing thresholding`
- **为什么对您有用**: 本文属于应用统计（神经影像），与您的主要兴趣（因果推断、高维、半参数等）无直接重叠，但可作为流行病学或应用因果方向的入门读物，展示复杂纵向数据建模的实践。您的武器库（如非参数方法、贝叶斯计算）足以理解其方法，但无需深入；作为跨领域阅读，可了解动态网络建模的最新进展，但非优先阅读。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

