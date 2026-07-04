# Biostatistics — Vol 22  Issue 4  ·  2026-07-04

- 共 15 篇 · Biostatistics
- 目录核对 ✅ 15 篇全部抓到（对照 OpenAlex 15 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Biostatistics》第22卷第4期共15篇论文，整体上围绕两条主线展开：**因果推断与测量误差**，以及**流行病学中的复杂数据建模与检验**。前者集中在随机化试验的推断方法、测量误差对因果参数的影响、以及利用外部数据的信息借用；后者则覆盖了归因危险度校正、遗传关联检验、群组检测回归、病例-对照稀疏估计、meta分析似然等价性等应用导向的方法。此外，还有若干篇涉及生存分析监测、高维正则化回归、篮子试验贝叶斯检验、疾病发病时间估计、成分数据降维和跨种族罕见变异荟萃分析，这些论文主题较为分散，但均属于生物统计方法学的常规拓展。

在因果推断主线中，最突出的工作是**随机化推断在集群随机试验中的推广**（Randomization-based confidence intervals for cluster randomized trials），它解决了传统随机化推断难以处理非连续和生存结局的痛点，通过个体水平数据反演构造置信区间，且不依赖大样本渐近理论，适用于匹配/分层等复杂设计。另一篇**Berkson误差的偏差分析**（Bias due to Berkson error）则挑战了经典结论，证明当存在未观测混杂时，用预测值替代观测值会导致推断系统性偏差，这对因果推断中测量误差的敏感性分析有直接警示。**动态借用与治疗效应异质性**（Dynamic borrowing in the presence of treatment effect heterogeneity）提出了协变量调整可交换性概念，在潜在结果框架下形式化信息借用条件，避免了因边际效应不同而导致的降权偏误。**贝叶斯迁移学习用于病因分布估计**（Regularized Bayesian transfer learning）则聚焦于目标人群的病因概率估计，通过收缩先验控制迁移误差，并理论证明集成模型倾向于选择最准确的基线分类器。

在流行病学方法主线中，**人群归因危险度的错误分类校正**（Estimation and inference for the population attributable risk in the presence of misclassification）填补了方法空白，其似然框架可处理主研究/验证研究设计，模拟显示校正后偏PAR估计值可增加317%。**肿瘤亚型异质性检验的混合效应模型**（A mixed-model approach for powerful testing of genetic associations）通过两阶段多分类模型得分检验降低自由度，并利用EM算法处理缺失数据。**群组检测数据的广义加性回归**（Generalized additive regression for group testing data）采用贝叶斯框架灵活捕捉非线性效应，同时处理分类错误。**病例-对照多亚型稀疏估计**（Sparse estimation for case–control studies with multiple disease subtypes）揭示了数据共享lasso与对称多项逻辑回归的形式化联系，指出非对称形式在亚型间同质性高时表现不佳。**双零研究在meta分析中的可忽略性**（The identity of two meta-analytic likelihoods）则从似然等价性角度证明双零研究不贡献信息，为实际应用提供理论依据。

对于因果推断方向的研究者，建议优先阅读：**Randomization-based confidence intervals for cluster randomized trials**（随机化推断CI的通用框架）、**Bias due to Berkson error**（测量误差与未观测混杂的交互）、**Dynamic borrowing in the presence of treatment effect heterogeneity**（协变量调整可交换性）。对于半参数效率或高维方向，**Regularized Bayesian transfer learning**（收缩先验与迁移学习）和**Adaptive group-regularized logistic elastic net regression**（分组正则化）可作参考，但后者更偏应用。

## 因果推断  *(causal_inference, 4 篇)*

### 1. [10.1093/biostatistics/kxaa007](https://doi.org/10.1093/biostatistics/kxaa007) — Randomization-based confidence intervals for cluster randomized trials
- **作者**: Dustin J Rabideau, Rui Wang
- **期刊/来源**: Biostatistics
- **机构**: Harvard University · Harvard Pilgrim Health Care
- **分类**: vol 22 · issue 4 · pp 913-927
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对集群随机试验（CRT）中置信区间构建问题，提出一种基于随机化推断的通用方法。现有参数和半参数方法依赖分布假设或大量集群数才能保证名义覆盖，而随机化推断虽无需分布假设，但通过反证法构造CI需检验非零原假设，对非连续和生存结局困难。作者利用个体水平数据，通过随机化检验反演构造CI，可处理多种结局类型（包括区间删失生存数据），并纳入匹配/分层等设计特征。方法采用计算高效的算法（无需穷举所有随机化分配），通过模拟验证覆盖率和区间长度，并在博茨瓦纳联合预防项目（HIV预防试验，区间删失生存结局）中展示应用。核心贡献在于将随机化推断CI推广到CRT常见复杂设定，且不依赖大样本渐近理论。对您而言，该方法属于因果推断中实验设计的实用工具，尤其适合纵向或生存结局的集群随机试验，与您的primary interest（causal inference, longitudinal）直接相关。
- **关键技术**: `randomization-based inference`, `inverting randomization tests`, `cluster randomized trials`, `interval-censored survival data`, `computationally efficient algorithm`
- **为什么对您有用**: 本文直接关联您的primary interest中的causal inference（cluster randomized trials）和longitudinal/生存结局。方法学上，它提供了一种不依赖大样本渐近的CI构造思路，您可以用very_familiar的estimation theory in causal inference和nonparametric statistics来理解其finite-sample性质。中期可做：若想将类似随机化推断思路推广到proximal causal inference或IV设定，需先在moderately_familiar的identification theory in causal inference上长肌肉（理解非零原假设下的识别条件）。

### 2. [10.1093/biostatistics/kxaa002](https://doi.org/10.1093/biostatistics/kxaa002) — Bias due to Berkson error: issues when using predicted values in place of observed covariates
- **作者**: Gregory Haber, Joshua Sampson, Barry Graubard
- **期刊/来源**: Biostatistics
- **机构**: National Cancer Institute · Division of Cancer Epidemiology and Genetics
- **分类**: vol 22 · issue 4 · pp 858-872
- 相关性 7/10 · novelty: `weaker_assumption`
- **摘要**: 本文研究在协变量存在 Berkson 测量误差时，用预测值替代观测值进行线性回归推断的偏差问题。经典结论认为，在标准假设下，Berkson 误差模型可得到一致或近似一致的推断。但本文证明，当结果模型中存在未观测混杂时，这一一致性不再成立——基于 Berkson 误差协变量的边际推断与基于真实观测协变量的推断存在系统性差异。由于未观测混杂在实际应用中普遍存在，这严重限制了预测值替代法的实用性。作者通过 NHANES 数据，以体脂百分比和 BMI 对 HbA1c 的联合关联为例，展示了使用预测体脂百分比替代观测值会导致推断结果显著不同，甚至出现方向相反的关联。本文对您有用：它直接关联您 causal inference 兴趣中的 sensitivity analysis 和 measurement error 问题，特别是 Berkson 误差与未观测混杂的交互效应，是您理解预测值替代法局限性的关键文献。
- **关键技术**: `Berkson error model`, `measurement error`, `unmeasured confounding`, `linear regression`, `predicted values substitution`
- **为什么对您有用**: 本文直接关联您 primary interest 中的 causal inference 子方向，特别是 measurement error 与 unmeasured confounding 的交互问题。您的 technical arsenal 中 'estimation theory in causal inference' 和 'identification theory in causal inference' 可直接用于分析本文的偏差机制——例如，用您熟悉的 nonparametric statistics 视角审视 Berkson 误差下的 identification 条件。中期可做：若想进一步拓展，需在 'semiparametric theory' 上长肌肉，以处理非线性 outcome 模型下的类似偏差。

### 3. [10.1093/biostatistics/kxz066](https://doi.org/10.1093/biostatistics/kxz066) — Dynamic borrowing in the presence of treatment effect heterogeneity
- **作者**: Ales Kotalik, David M Vock, Eric C Donny, Dorothy K Hatsukami, Joseph S Koopmeiners
- **期刊/来源**: Biostatistics
- **机构**: University of Minnesota · Wake Forest University
- **分类**: vol 22 · issue 4 · pp 789-804
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对随机对照试验中利用外部补充信息时存在的治疗效应异质性（treatment effect heterogeneity）问题，提出“协变量调整可交换性”（covariate-adjusted exchangeability）概念。传统方法通过比较边际治疗效应来判断数据源间的一致性，当边际效应因人群分布不同而不同时，会导致有偏或过度降权。作者在潜在结果框架下形式化定义协变量调整可交换性与边际可交换性，并利用线性模型与多源可交换性模型（multi-source exchangeability models, MEM）框架实现信息借用。模拟研究展示了方法在边际效应不同但协变量调整可交换性成立时的操作特性。实例分析使用两项极低尼古丁含量香烟临床试验数据。该方法扩展了在治疗效应异质性存在时借用外部信息的适用场景。
- **关键技术**: `covariate-adjusted exchangeability`, `multi-source exchangeability models (MEM)`, `potential outcomes framework`, `linear model for effect modification`
- **为什么对您有用**: 本文直接关联因果推断中的异质性处理效应与外部数据借用问题，属于 primary interest 的 causal inference 子方向。武器库中 very_familiar 的 estimation theory in causal inference 可直接用于理解其协变量调整可交换性假设的识别条件，而 moderately_familiar 的 identification theory 可用于评估该假设在更复杂设定（如 IV、proximal CI）下的可推广性。中期可做：若想将协变量调整可交换性推广到非参数或半参数模型，需先在 moderately_familiar 的 semiparametric theory 上提升。

### 4. [10.1093/biostatistics/kxaa001](https://doi.org/10.1093/biostatistics/kxaa001) · [arXiv](https://arxiv.org/abs/1810.10572) — Regularized Bayesian transfer learning for population-level etiological distributions
- **作者**: Abhirup Datta, Jacob Fiksel, Agbessi Amouzou, Scott L Zeger
- **期刊/来源**: Biostatistics
- **分类**: vol 22 · issue 4 · pp 836-857
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对计算机编码死因推断（CCVA）中的迁移学习问题，目标是估计目标人群的病因分布（population-level etiological distributions），而非个体分类。设定中，源域有大量标注数据训练基线分类器，目标域仅有少量标注数据，且两者分布可能不同。作者提出一种简约的层次贝叶斯迁移学习框架，直接估计目标域中各类别的概率。核心机制是引入一种新颖的收缩先验（shrinkage prior）作用于迁移误差率，保证当目标域无标注数据或基线分类器完全准确时，模型退化为直接聚合基线分类器预测的默认做法。进一步扩展为集成多个基线分类器的版本，理论证明集成模型倾向于选择最准确的基线分类器。实证分析展示了该方法在死因推断中的实用性。对您而言，本文是流行病学中因果推断与迁移学习结合的实例，其贝叶斯框架和收缩先验设计对您处理小样本目标域下的识别问题有参考价值。
- **关键技术**: `transfer learning`, `hierarchical Bayesian model`, `shrinkage prior`, `verbal autopsy`, `ensemble classifier`
- **为什么对您有用**: 本文直接关联您的流行病学（secondary interest）和因果推断（primary interest）中的迁移学习问题。您武器库中的非参数统计和估计理论可用于分析其收缩先验的渐近性质，但核心贝叶斯框架与您熟悉的频率学派工具差异较大，属于中期可做：需先在 moderately_familiar 的识别理论上补足贝叶斯迁移学习的 identification 条件。

## 流行病学  *(epidemiology, 5 篇)*

### 1. [10.1093/biostatistics/kxz067](https://doi.org/10.1093/biostatistics/kxz067) — Estimation and inference for the population attributable risk in the presence of misclassification
- **作者**: Benedict H W Wong, Jooyoung Lee, Donna Spiegelman, Molin Wang
- **期刊/来源**: Biostatistics
- **机构**: Harvard University · Cancer Research And Biostatistics · Brigham and Women's Hospital
- **分类**: vol 22 · issue 4 · pp 805-818
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文针对流行病学中人群归因危险度（PAR）在暴露变量存在分类错误时的估计与推断问题，填补了方法学空白。采用基于似然的参数估计方法，同时建模疾病风险模型和错误分类机制，支持主研究/内部验证研究和主研究/外部验证研究两种设计，并允许对可转移性（transportability）做出不同假设。通过模拟研究评估了有限样本性能，并应用于健康专业人员随访研究（HPFS）中高红肉摄入和酒精摄入与结直肠癌发病率的偏PAR估计。结果显示，校正错误分类偏倚后，两个风险因子的偏PAR估计值最多增加了317%，凸显了错误分类校正的重要性。对您而言，本文是流行病学中因果参数估计的经典应用，其似然框架和验证研究设计思路可迁移至您关注的因果推断中的测量误差问题。
- **关键技术**: `likelihood-based estimation`, `misclassification model`, `internal/external validation study`, `transportability assumptions`, `population attributable risk (PAR)`
- **为什么对您有用**: 本文属于流行病学应用，直接关联您的secondary interest中的流行病学数据与因果推断。方法上采用似然框架处理错误分类，与您非常熟悉的因果推断中的测量误差问题相通，可作为入门级阅读了解流行病学中PAR的估计实践。武器库中的非参数统计和因果推断估计理论足以理解本文方法，但本文偏应用，方法学新颖性有限，暂不构成直接的研究推进方向。

### 2. [10.1093/biostatistics/kxz065](https://doi.org/10.1093/biostatistics/kxz065) — A mixed-model approach for powerful testing of genetic associations with cancer risk incorporating tumor characteristics
- **作者**: Haoyu Zhang, Ni Zhao, Thomas U Ahearn, William Wheeler, Montserrat García-Closas, Nilanjan Chatterjee
- **期刊/来源**: Biostatistics
- **机构**: Bloomberg (United States) · National Cancer Institute · Division of Cancer Epidemiology and Genetics · Johns Hopkins University
- **分类**: vol 22 · issue 4 · pp 772-788
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对癌症遗传关联研究中肿瘤亚型异质性检验的问题，提出了一种混合效应两阶段多分类模型得分检验（MTOP）。第一阶段用标准多分类模型定义所有由肿瘤特征交叉分类得到的亚型；第二阶段对亚型特异性病例-对照优势比进行简约建模，包括基线亚型的固定效应和探索性标记的随机效应，以降低自由度。采用EM算法处理肿瘤标记的缺失数据。模拟和波兰乳腺癌研究（PBCS）数据表明，MTOP在识别风险位点与肿瘤亚型间的异质性关联方面优于现有方法。该方法已实现为R包TOP，便于应用。对您而言，本文是流行病学中因果推断（异质性效应检验）与缺失数据处理（EM算法）的实用案例，可作为应用导向的参考。
- **关键技术**: `polytomous logistic regression`, `score test`, `random effects model`, `EM algorithm`, `genome-wide association study`
- **为什么对您有用**: 本文属于流行病学应用，直接关联您的secondary interest中的流行病学因果推断。方法上使用了多分类模型和随机效应来检验异质性关联，与您熟悉的因果推断中的效应修饰概念相通。武器库中'identification theory in causal inference'和'M-estimation theory'可用于理解其检验统计量的构造，但核心是应用而非理论创新，属于'暂不可做'——缺乏直接可攻的理论口子，但可作为流行病学方法学的入门阅读。

### 3. [10.1093/biostatistics/kxaa003](https://doi.org/10.1093/biostatistics/kxaa003) — Generalized additive regression for group testing data
- **作者**: Yan Liu, Christopher S McMahan, Joshua M Tebbs, Colin M Gallagher, Christopher R Bilder
- **期刊/来源**: Biostatistics
- **机构**: University of Nevada, Reno · Clemson University · University of South Carolina · University of Nebraska–Lincoln
- **分类**: vol 22 · issue 4 · pp 873-889
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对低流行率疾病筛查中的群组检测数据，提出了一种贝叶斯广义加性回归方法。传统群组检测回归模型通常假设协变量效应为线性，但这一假设在应用中可能导致模型误设和推断偏倚。作者在个体患病概率模型中引入未知光滑函数，以灵活捕捉协变量的非线性效应，同时处理检测结果可能存在的分类错误。方法适用于任意群组检测协议，可同时估计多个协变量的光滑函数、线性效应以及检测准确率。通过爱荷华州衣原体感染群组检测数据展示了方法的实用性。对您而言，这是一篇流行病学领域的应用论文，展示了在复杂数据结构和分类错误下如何灵活建模，其分析模式对您从事因果推断中的测量误差或敏感性分析有参考价值。
- **关键技术**: `Bayesian generalized additive model`, `group testing`, `misclassification`, `smooth function estimation`
- **为什么对您有用**: 本文属于流行病学应用，直接对应您的secondary interest。其处理分类错误和协变量非线性效应的思路，对您从事因果推断中的测量误差问题有启发。武器库中'非参数统计'和'M估计理论'可用于理解其光滑函数估计的渐近性质，但本文是贝叶斯方法，与您熟悉的频率学派工具存在距离，属于'暂不可做'——核心机器（贝叶斯非参数后验计算）不在武器库里。

### 4. [10.1093/biostatistics/kxz063](https://doi.org/10.1093/biostatistics/kxz063) — Sparse estimation for case–control studies with multiple disease subtypes
- **作者**: Nadim Ballout, Cedric Garcia, Vivian Viallon
- **期刊/来源**: Biostatistics
- **机构**: Université Claude Bernard Lyon 1 · Unité Mixte de Recherche Epidémiologique et de Surveillance Transport Travail Environnement · Laboratoire Ville Mobilité Transport · Centre international de recherche sur le cancer
- **分类**: vol 22 · issue 4 · pp 738-755
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对病例-对照研究中存在多个疾病亚型（如乳腺癌亚型）的稀疏估计问题，提出了基于数据共享lasso（data shared lasso）的分层条件逻辑回归方法，用于匹配设计；对于非匹配设计，比较了两种基于L1惩罚的多项逻辑回归方法。核心贡献在于揭示了这两种方法之间的形式化联系：对称形式的多项逻辑回归实际上等价于数据共享lasso版本的非对称形式，因此当亚型间同质性中等或高时，以对照组为参照的非对称形式表现不佳。模拟实验验证了在匹配和非匹配设计下，适当利用亚型同质性可提升估计与预测精度、变量选择及异质性识别能力。初步应用于EPIC队列中乳腺癌亚型相关的代谢物识别。对您而言，本文是流行病学中应用因果推断与高维变量选择方法的典型案例，其数据共享lasso策略可迁移至您熟悉的因果推断中分层处理异质性效应的问题。
- **关键技术**: `data shared lasso`, `stratified conditional logistic regression`, `L1-penalized multinomial logistic regression`, `case-control study with subtypes`
- **为什么对您有用**: 本文直接关联您的流行病学次级兴趣，展示了在高维协变量下处理疾病亚型异质性的实用统计方法。您武器库中非常熟悉的高维渐近理论可用于分析其lasso估计量的选择一致性，而中等熟悉的M估计理论可用于推导其惩罚似然估计的渐近分布。中期可做：需先在中等熟悉的M估计理论上提升，以严格证明其估计量的Oracle性质。

### 5. [10.1093/biostatistics/kxaa004](https://doi.org/10.1093/biostatistics/kxaa004) — The identity of two meta-analytic likelihoods and the ignorability of double-zero studies
- **作者**: Dankmar Böhning, Patarawan Sangnawakij
- **期刊/来源**: Biostatistics
- **机构**: University of Southampton · Thammasat University
- **分类**: vol 22 · issue 4 · pp 890-896
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文研究 meta-analysis 中双零研究（两组均无事件）对似然推断的影响。在二分类结局的 meta-analysis 中，传统两阶段方法在存在大量零事件研究时会失效。作为替代，一阶段的 Poisson 回归模型和条件二项模型均能处理零事件研究，但条件二项模型会排除双零研究，而 Poisson 回归看似保留它们。作者证明两种模型在似然推断上等价，且双零研究（与单零研究不同）在两种模型中均不贡献似然信息。这一结果澄清了双零研究在 meta-analysis 中的可忽略性，为实际应用提供了理论依据。对您而言，本文是流行病学中 meta-analysis 方法学的清晰入门，展示了似然等价性这一基础但重要的理论结果，适合作为 gateway reading 理解零事件问题的统计处理。
- **关键技术**: `meta-analysis`, `Poisson regression`, `conditional binomial model`, `likelihood inference`, `double-zero studies`
- **为什么对您有用**: 本文属于流行病学应用方向，是 meta-analysis 中零事件问题的经典理论澄清。武器库中 'nonparametric statistics' 和 'estimation theory in causal inference' 的似然思维可帮助理解其等价性证明。作为 gateway reading，本文 exposition 清晰，适合快速掌握双零研究可忽略性的核心论点，值得花时间读全文。

## 其他  *(other, 6 篇)*

### 1. [10.1093/biostatistics/kxz064](https://doi.org/10.1093/biostatistics/kxz064) — Simultaneous monitoring for regression coefficients and baseline hazard profile in Cox modeling of time-to-event data
- **作者**: Yishu Xue, Jun Yan, Elizabeth D Schifano
- **期刊/来源**: Biostatistics
- **机构**: University of Connecticut
- **分类**: vol 22 · issue 4 · pp 756-771
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文在 Cox 比例风险模型框架下，提出了一种同时监测回归系数和累积基线风险函数的方法。该方法结合了用于回归系数的多元控制图和用于累积基线风险函数的轮廓控制图，能够处理不同删失率和样本大小的数据块。通过模拟研究验证了该方法在控制第一类错误的同时，对模型参数或非参数部分的变化具有较高的检测功效。在 SEER 项目淋巴瘤生存数据的应用中，该方法成功识别出存在结构模型变化的数据块。本文主要贡献在于将统计过程控制思想引入生存分析中的模型变化监测，但方法学创新程度有限，属于应用导向的拓展。
- **关键技术**: `Cox proportional hazards model`, `multivariate control chart`, `profile monitoring`, `cumulative baseline hazard`, `change point detection`
- **为什么对您有用**: 本文属于应用统计方法在流行病学/生存分析中的拓展，与您的流行病学（应用数据集、因果推断）次要兴趣有弱关联。但方法学核心（控制图+生存模型）不在您的技术武器库中，且缺乏与您主要兴趣（因果推断、高维统计、U-统计量）的直接连接。作为流行病学应用论文，其分析模式（SEER 数据的分块监测）对您可能有一定参考价值，但整体方法学新颖性不足，暂不可做。

### 2. [10.1093/biostatistics/kxz062](https://doi.org/10.1093/biostatistics/kxz062) · [arXiv](https://arxiv.org/abs/1805.00389) — Adaptive group-regularized logistic elastic net regression
- **作者**: Magnus M Münch, Carel F W Peeters, Aad W Van Der Vaart, Mark A Van De Wiel
- **期刊/来源**: Biostatistics
- **分类**: vol 22 · issue 4 · pp 723-737
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文提出一种自适应组正则化逻辑弹性网回归方法（gren），用于高维数据中特征具有外部分组信息（如先前研究的p值或组学注释）的场景。该方法将逻辑弹性网回归的贝叶斯形式与变分贝叶斯框架结合，通过近似经验变分贝叶斯估计同时优化模型参数和组级惩罚参数。每个特征组对应一个独立的惩罚参数，从而允许不同组具有不同的收缩强度。模拟和三项癌症基因组学及一项阿尔茨海默代谢组学研究表明，当分组信息有效时，gren能提升分类性能和特征选择。该方法本质上是带分组先验的正则化回归，不涉及因果推断、高维随机矩阵或U统计量等核心兴趣方向。对您而言，本文属于应用统计方法论文，与您的主要兴趣方向（因果推断、高维统计、U统计量等）无直接技术重叠，但可作为正则化方法在组学数据中应用的参考。
- **关键技术**: `group-regularized elastic net`, `empirical variational Bayes`, `logistic regression`, `high-dimensional feature selection`
- **为什么对您有用**: 本文与您的主要兴趣方向（因果推断、高维统计、U统计量、半参理论等）无直接技术连接。它属于高维正则化回归的应用方法，不涉及您武器库中的具体工具（如树宽/张量收缩、极小极大界、高阶影响函数等）。作为gateway阅读，本文对统计计算方向（变分贝叶斯）有一定参考价值，但整体相关性较低，暂不可做。

### 3. [10.1093/biostatistics/kxaa005](https://doi.org/10.1093/biostatistics/kxaa005) — RoBoT: a robust Bayesian hypothesis testing method for basket trials
- **作者**: Tianjian Zhou, Yuan Ji
- **期刊/来源**: Biostatistics
- **机构**: Chicago Department of Public Health · University of Chicago
- **分类**: vol 22 · issue 4 · pp 897-912
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对肿瘤学 II 期篮子试验（basket trial）提出一种稳健贝叶斯假设检验方法 RoBoT。篮子试验同时评估一种疗法在多种癌症类型中的疗效，核心挑战在于如何在篮子间自适应地借用信息（borrowing strength）以提升检验效能，同时控制多重比较下的 I 类错误膨胀。RoBoT 采用 Dirichlet 过程混合模型（DPMM）将篮子划分为若干潜在亚组，每个亚组内疗效相似，亚组数及归属由数据自动推断。与传统层次模型不同，该方法通过亚组结构避免过度收缩（excessive shrinkage）导致的假阳性。检验框架基于形式化的贝叶斯假设检验（Bayesian hypothesis testing），而非后验可信区间，提供可解释且稳健的决策准则。模拟实验表明 RoBoT 在控制 I 类错误和提升检验效能方面优于现有方法，并应用于伊马替尼和维莫非尼两项真实篮子试验数据。本文属于应用统计方法论文，方法学 novelty 程度有限（在已有 DPMM 和贝叶斯检验框架上做组合），但对您而言可作为流行病学或临床试验中多重比较与信息借用问题的入门参考。
- **关键技术**: `Bayesian hypothesis testing`, `Dirichlet process mixture model`, `basket trial`, `adaptive borrowing of strength`, `type I error control`
- **为什么对您有用**: 本文属于流行病学/临床试验领域的应用方法论文，可作为 gateway reading 了解篮子试验中信息借用与多重比较的统计挑战。您的武器库中非参数统计和 M-估计理论可用来分析其 DPMM 后验收缩性质，但核心机器（贝叶斯非参数、DPMM 后验收敛率）不在 very_familiar 中，属于**暂不可做**——缺少 Dirichlet 过程后验收缩理论工具。不过，若您未来想进入临床试验统计方向，本文是值得花时间读全文的入门材料。

### 4. [10.1093/biostatistics/kxz068](https://doi.org/10.1093/biostatistics/kxz068) — Estimating disease onset from change points of markers measured with error
- **作者**: Unkyung Lee, Raymond J Carroll, Karen Marder, Yuanjia Wang, Tanya P Garcia
- **期刊/来源**: Biostatistics
- **机构**: Texas A&M University · University of Technology Sydney · University of Minnesota · Columbia University
- **分类**: vol 22 · issue 4 · pp 819-835
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文研究亨廷顿病运动发病时间的客观估计问题。当前临床诊断依赖医生主观判断，存在误差。作者提出一个非线性位置偏移标记模型，刻画运动能力随时间的纵向衰退轨迹，并将运动发病定义为该轨迹的拐点。模型将拐点与其他疾病进展标记物（如认知、精神症状）关联。作者开发了两种估计方法：参数化的非线性混合效应模型和多阶段非参数方法。模拟研究表明，参数方法对均值结构设定敏感，而非参数方法在各种设定下均给出无偏估计。应用于大型观察性研究NPHD数据，非参数方法比临床主观判断更早预测运动发病。本文是应用导向的方法学工作，核心贡献在于将拐点估计问题与疾病发病时间推断结合。
- **关键技术**: `nonlinear mixed effects model`, `multi-stage nonparametric estimation`, `inflection point estimation`, `longitudinal data analysis`, `change point detection`
- **为什么对您有用**: 本文属于流行病学应用（亨廷顿病），与您的secondary interest 'epidemiology (application, data sets, causal inference)' 直接相关。方法上使用非参数估计处理纵向数据中的拐点，与您very_familiar的'nonparametric statistics'和'estimation theory in causal inference'有技术重叠，但问题设定（疾病发病时间推断）与您primary interests的因果推断（如mediation、longitudinal）有距离。本文是应用导向，方法学novelty有限，可作为流行病学纵向数据分析的入门读物，但无需深入阅读。

### 5. [10.1093/biostatistics/kxz060](https://doi.org/10.1093/biostatistics/kxz060) — Sufficient dimension reduction for compositional data
- **作者**: Diego Tomassi, Liliana Forzani, Sabrina Duarte, Ruth M Pfeiffer
- **期刊/来源**: Biostatistics
- **机构**: Université de Technologie de Troyes · Universidad Nacional del Litoral · Consejo Nacional de Investigaciones Científicas y Técnicas · National Cancer Institute
- **分类**: vol 22 · issue 4 · pp 687-705
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对成分数据（compositional data）提出基于似然的充分降维（SDR）方法，目标是找到成分向量的线性组合，使其包含关于结局变量的所有信息，即对建模和预测是充分的。作者考虑了逆回归的多种模型，包括正态、多项式和泊松图模型，以处理观测计数间的复杂依赖关系。这些模型能给出降维的有效估计，并适用于连续或分类结局。通过惩罚项纳入变量选择，并处理成分数据固有的不变性（invariance）问题。模拟和人类微生物组计划数据展示了所提方法与现有方法的比较。该方法在生物统计和微生物组分析中有应用价值，但核心是降维而非因果推断或高维统计理论。
- **关键技术**: `sufficient dimension reduction`, `inverse regression`, `graphical models`, `variable selection via penalties`, `compositional data invariance`
- **为什么对您有用**: 本文属于生物统计应用，与您的主要兴趣（因果推断、高维统计、U-统计等）无直接交集。作为流行病学/微生物组数据分析的入门读物，它展示了成分数据降维的似然框架，但方法学新颖性有限（主要是现有SDR方法的扩展）。武器库中非参数统计和估计理论可帮助理解其似然框架，但缺乏与您核心兴趣的深层连接。暂不可做——核心机器（成分数据特定模型、图模型似然）不在武器库中，且问题本身不直接导向您的研究方向。

### 6. [10.1093/biostatistics/kxz061](https://doi.org/10.1093/biostatistics/kxz061) — Trans-ethnic meta-analysis of rare variants in sequencing association studies
- **作者**: Jingchunzi Shi, Michael Boehnke, Seunggeun Lee
- **期刊/来源**: Biostatistics
- **分类**: vol 22 · issue 4 · pp 706-722
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对跨种族罕见变异关联研究的荟萃分析，提出了一种改进的基因/区域水平检验方法。现有方法未考虑不同人群间的遗传相似性，在异质性存在时功效不足。作者在核回归框架下构建修正随机效应模型，将人群间遗传相似性矩阵纳入效应系数的异质性结构建模。检验统计量采用基于重抽样的copula方法逼近其渐近分布，从而高效计算p值。模拟表明该方法在异质性下能控制I类错误率并提升检验功效。实际数据分析应用于T2D-GENES外显子测序数据，探索罕见变异与多个性状的关联。该方法对您作为统计学家而言，属于应用统计方法学论文，其核心贡献在于将遗传相似性信息融入随机效应模型，而非您主要关注的因果推断或高维统计理论。
- **关键技术**: `kernel regression framework`, `random effects model`, `resampling-based copula`, `score test`, `genetic similarity matrix`
- **为什么对您有用**: 本文属于流行病学/遗传学应用，与您的secondary interest（epidemiology）相关。但方法学核心是遗传关联检验，而非因果推断或您武器库中的非参/高维工具。作为入门级流行病学应用阅读，它清晰展示了罕见变异荟萃分析的数据结构和检验流程，但缺乏与您primary interests的直接技术连接。暂不可做——核心机器（遗传关联的随机效应模型与copula方法）不在您的武器库中，且该领域的方法学问题与您的统计计算权衡或U统计量方向距离较远。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

