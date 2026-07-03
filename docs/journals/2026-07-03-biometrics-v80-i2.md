# Biometrics — Vol 80  Issue 2  ·  2026-07-03

- 共 33 篇 · Biometrics
- 目录核对 ✅ 33 篇全部抓到（对照 OpenAlex 40 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Biometrics》第80卷第2号共收录33篇论文，主题高度集中于**因果推断**，尤其是纵向数据、生存数据和随机化试验中的识别与效率问题，同时穿插了**假设检验**、**高维因子模型**和**半参数整合**等方向。因果推断主线可细分为三条：一是**边际结构模型与双稳健估计**的扩展（如分位数、生存数据、零膨胀计数结局）；二是**主分层与中介分析**在复杂生存数据和高维暴露中的应用；三是**随机化试验设计**中的协变量调整、自适应分配和交叉设计效应。此外，**高维假设检验**（函数型分位数独立性检验）和**数据整合**（prior probability shift下的半参数估计）构成次要但突出的方法线。

在因果推断主线中，**双稳健估计**的推广最为密集。Doubly robust estimation and sensitivity analysis for marginal structural quantile models将双稳健思想从均值推广到分位数因果效应，并引入平滑估计方程和混淆函数敏感性分析。Doubly robust proximal synthetic controls则在合成控制框架下，利用proximal因果推断实现双稳健估计，适用于单一处理单元的panel数据。Single proxy control放宽了秩保持假设，仅需单个负对照结局即可非参数识别ATT，与proximal方法形成对比。Integrating randomized and observational studies to estimate optimal dynamic treatment regimes将增强Q学习扩展到多阶段，整合随机试验与观察性数据以实现双稳健最优DTR估计。**主分层与中介分析**方面，Causal inference for time-to-event data with a cured subpopulation利用替代变量识别治愈亚组，估计始终未治愈者的生存效应；Direct and indirect treatment effects in the presence of semicompeting risks将中介分解引入半竞争风险生存数据，依赖跨世界假设。**随机化试验设计**中，On exact randomization-based covariate-adjusted confidence intervals给出了协变量调整后均值差统计量的闭合形式精确置信区间，消除计算瓶颈；Behavioral carry-over effect and power consideration in crossover trials在潜在结果框架下推导了行为性carry-over对功效的影响边界；Robustness of response-adaptive randomization证明DBCD在模型误设下仍保持相合性；Sequential covariate-adjusted randomization via hierarchically minimizing Mahalanobis distance and marginal imbalance实现了逐个体分配的自适应随机化。

其他方向中，**假设检验**有Testing conditional quantile independence with functional covariate，通过随机投影构造Cramér–von Mises型检验，能检测参数速率的局部备择；Efficient testing of the biomarker positive and negative subgroups in a biomarker-stratified trial利用等渗约束提升联合检验效能。**高维与半参数**方面，High-dimensional covariate-augmented overdispersed poisson factor model提出协变量增强的泊松因子模型，结合变分推断与低秩分解；Efficient data integration under prior probability shift在半参数框架下用自适应LASSO处理高维协变量选择；Deep partially linear cox model for current status data将DNN与单调样条结合，达到半参数有效界。

对于因果推断方向的研究者，优先关注：Doubly robust estimation and sensitivity analysis for marginal structural quantile models（双稳健分位数因果效应）、Doubly robust proximal synthetic controls（合成控制中的双稳健估计）、Single proxy control（单负对照的非参数识别）、Causal inference for time-to-event data with a cured subpopulation（主分层与治愈模型）、Direct and indirect treatment effects in the presence of semicompeting risks（半竞争风险中介分析）、Integrating randomized and observational studies to estimate optimal dynamic treatment regimes（多阶段增强Q学习）。对于半参数效率理论，Deep partially linear cox model for current status data和Efficient data integration under prior probability shift值得一读。对于高维假设检验，Testing conditional quantile independence with functional covariate和Efficient testing of the biomarker positive and negative subgroups in a biomarker-stratified trial提供了新视角。

## 因果推断  *(causal_inference, 18 篇)*

### 1. [10.1093/biomtc/ujae045](https://doi.org/10.1093/biomtc/ujae045) · [arXiv](https://arxiv.org/abs/2210.04100) — Doubly robust estimation and sensitivity analysis for marginal structural quantile models
- **作者**: Chao Cheng, Liangyuan Hu, Fan Li
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文在边际结构分位数模型（MSQM）框架下，研究时变处理对潜在结果全分布的条件分位数因果效应。在序贯可忽略性假设下，推导了MSQM的有效影响函数，并基于此提出一个新的双稳健估计量：若处理分配模型或潜在结果分布模型之一正确设定，该估计量一致；若两者均正确，则达到半参数有效。为便于计算，作者引入平滑估计方程求解点估计和方差估计。此外，提出混淆函数方法进行敏感性分析，评估序贯可忽略性违反时估计量的稳健性。模拟和Yale New Haven电子健康记录数据的实证分析验证了方法性能。该工作将双稳健思想从均值因果效应推广到分位数因果效应，对您从事的因果推断（纵向数据）和半参数效率理论方向有直接参考价值。
- **关键技术**: `efficient influence function`, `doubly robust estimation`, `marginal structural quantile model`, `smoothed estimating equation`, `confounding function sensitivity analysis`
- **为什么对您有用**: 直接连接到您primary interest中的因果推断（纵向数据）和效率理论（半参数有效界）。您的very_familiar工具（非参统计、因果推断估计理论）可直接用于理解其双稳健构造和影响函数推导；moderately_familiar的HOIF和半参数理论可进一步分析其高阶性质。中期可做：将本文的平滑估计方程技巧与您熟悉的higher-order U-statistics计算（treewidth/einsum）结合，探索分位数估计的计算效率改进。

### 2. [10.1093/biomtc/ujae025](https://doi.org/10.1093/biomtc/ujae025) · [arXiv](https://arxiv.org/abs/2302.11656) — Confounder-dependent Bayesian mixture model: Characterizing heterogeneity of causal effects in air pollution epidemiology
- **作者**: Dafne Zorzetto, Falco J Bargagli-Stoffi, Antonio Canale, Francesca Dominici.
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文针对空气污染流行病学中因果效应异质性刻画问题，提出了一种新的Confounder-Dependent Bayesian Mixture Model (CDBMM)。该方法利用dependent Dirichlet process对潜在结果的条件分布进行灵活建模，从而在数据驱动下识别出具有相似Group Average Treatment Effect (GATE)的互斥人群子组，并估计各组内的因果效应。通过模拟研究验证了方法在揭示处理效应异质性方面的有效性，并应用于德克萨斯州Medicare参保者数据，发现PM2.5对死亡率因果效应存在六个异质性组。该方法的核心贡献在于将贝叶斯非参数混合模型与因果推断中的GATE估计相结合，为识别脆弱人群提供了新工具。对您而言，本文是流行病学中因果推断的典型应用，展示了如何利用贝叶斯方法处理效应异质性，与您的因果推断和流行病学应用兴趣直接相关。
- **关键技术**: `Bayesian nonparametric mixture model`, `dependent Dirichlet process`, `Group Average Treatment Effect (GATE)`, `causal effect heterogeneity`, `potential outcomes`
- **为什么对您有用**: 本文直接关联您的流行病学应用兴趣，展示了在空气污染研究中利用贝叶斯非参数方法识别异质性因果效应的完整分析流程。您武器库中的'identification theory in causal inference'和'nonparametric statistics'可直接用于理解其模型假设和估计策略，但核心的贝叶斯非参数工具（dependent Dirichlet process）不在您的武器库中，属于'暂不可做'——若想跟进，需先熟悉贝叶斯非参数建模。

### 3. [10.1093/biomtc/ujae028](https://doi.org/10.1093/biomtc/ujae028) — Causal inference for time-to-event data with a cured subpopulation
- **作者**: Yi Wang, Yuhao Deng, Xiao-Hua Zhou
- **期刊/来源**: Biometrics
- **机构**: Peking University · Peking University International Hospital · Shanghai University of International Business and Economics · Guangzhou Experimental Station · Beijing Institute of Big Data Research
- **分类**: vol 80 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对存在治愈亚组的生存数据，提出基于主分层（principal stratification）的因果估计量：始终未治愈亚组中的时点风险差和平均生存时间差，作为治愈率治疗效应的补充。在可忽略的治疗分配机制下，利用替代变量（substitutional variable）识别潜在治愈状态，证明了两个估计量的可识别性。估计方法采用混合治愈模型（mixture cure model），并通过交叉验证或似然比检验选择模型。应用于急性淋巴细胞白血病移植类型比较的观察性研究，分析无白血病生存率。对您而言，该文将主分层框架与生存数据治愈模型结合，是因果推断在流行病学纵向数据中的具体应用，且识别策略（替代变量）与您的proximal causal inference兴趣有技术交集。
- **关键技术**: `principal stratification`, `mixture cure model`, `substitutional variable`, `time-varying risk difference`, `survival analysis`
- **为什么对您有用**: 连接您的primary interest中causal inference的纵向/生存数据子方向，以及secondary interest中流行病学应用。技术层面，主分层识别策略与proximal CI的negative control思路有可比性，可用您very_familiar的nonparametric statistics和estimation theory in causal inference工具检验其识别假设的稳健性（如替代变量有效性）。中期可做：若想深入，需先在moderately_familiar的identification theory in causal inference上巩固主分层与工具变量的联系。

### 4. [10.1093/biomtc/ujae032](https://doi.org/10.1093/biomtc/ujae032) — Direct and indirect treatment effects in the presence of semicompeting risks
- **作者**: Yuhao Deng, Yi Wang, Xiao-Hua Zhou
- **期刊/来源**: Biometrics
- **机构**: Peking University · Michigan United · Peking University International Hospital · Shanghai University of International Business and Economics · Beijing Institute of Big Data Research
- **分类**: vol 80 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在完全随机化实验的框架下，针对半竞争风险（非终端事件可被终端事件删失，反之不成立）场景，提出两种将总处理效应分解为直接效应和间接效应的策略。第一种策略通过调整非终端事件的患病率来分解，第二种策略通过调整非终端事件的风险函数来分解。两种策略均需引入跨世界（cross-world）假设以实现可识别性，但假设条件略有不同。作者建立了反事实累积发生率和分解处理效应的渐近性质，并通过模拟和两个真实数据应用展示了两种分解的细微差异。该工作将经典中介分析框架扩展到生存数据中的半竞争风险设定，为理解治疗如何通过非终端事件（如疾病进展）影响终端事件（如死亡）提供了形式化工具。
- **关键技术**: `mediation analysis`, `semicompeting risks`, `counterfactual cumulative incidence`, `cross-world assumptions`, `asymptotic theory`
- **为什么对您有用**: 本文直接连接您的主要兴趣——因果推断中的中介分析，并处理了生存数据特有的半竞争风险结构，这是纵向因果推断中一个现实且重要的设定。您武器库中'very_familiar'的'非参数统计'和'因果推断中的估计理论'可直接用于理解其识别策略和渐近性质，而'moderately_familiar'的'因果推断中的识别理论'则是评估其cross-world假设合理性的关键。**中期可做**：若想在此方向上做出方法学贡献（如放松假设或引入高维协变量），需先在'moderately_familiar'的'半参数理论'上加强，以处理更复杂的估计方程和效率界。

### 5. [10.1093/biomtc/ujae046](https://doi.org/10.1093/biomtc/ujae046) — Integrating randomized and observational studies to estimate optimal dynamic treatment regimes
- **作者**: Anna Batorsky, Kevin J Anstrom, Donglin Zeng
- **期刊/来源**: Biometrics
- **机构**: University of North Carolina at Chapel Hill · University of Michigan
- **分类**: vol 80 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对动态治疗策略（DTR）的估计问题，提出多阶段增强Q学习估计量（MAQE），将SMART随机试验数据与观察性研究数据整合，以提高估计效率。MAQE在Q-learning框架下，通过augmentation方法利用观察性数据中的额外信息，对每个阶段的Q函数进行修正，从而减少对随机试验样本量的依赖。该方法扩展了已有的单阶段augmentation方法到多阶段设定，核心机制是构造一个augmented estimating equation，结合倾向得分和结果回归的估计，实现双重稳健性。模拟研究表明，MAQE在估计最优DTR的准确性和平均价值上优于未增强的Q-learning，且对试验与观察性研究的样本量比例、噪声变量和效应大小均稳健。本文对您的主要兴趣——因果推断中的纵向设定和估计理论——有直接连接，尤其是augmentation方法在整合不同数据源时的双重稳健性机制，与您熟悉的非参数统计和因果推断中的估计理论（如DR估计）高度相关。
- **关键技术**: `Q-learning`, `augmented estimation`, `dynamic treatment regimes`, `data integration`, `double robustness`
- **为什么对您有用**: 本文直接连接您的主要兴趣——因果推断中的纵向设定和估计理论，尤其是augmentation方法在整合随机试验与观察性数据时的双重稳健性机制。您熟悉的非参数统计和因果推断估计理论（如DR估计）可直接用于分析该方法的效率增益和稳健性条件。中期可做：将MAQE与您moderately_familiar的HOIF理论结合，推导其高阶影响函数，以刻画更精细的偏差-方差权衡。

### 6. [10.1093/biomtc/ujae055](https://doi.org/10.1093/biomtc/ujae055) · [arXiv](https://arxiv.org/abs/2210.02014) — Doubly robust proximal synthetic controls
- **作者**: Hongxiang Qiu, Xu Shi, Wang Miao, Edgar Dobriban, Eric Tchetgen Tchetgen
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在合成控制（SC）框架下，针对单一处理单元的panel数据，引入proximal causal inference的思想，提出了双重稳健的估计量。研究目标是在处理单元仅有一个的情况下，利用控制单元的线性组合来反事实地估计处理效应。现有SC方法通常要求处理前轨迹的近乎完美匹配，且依赖于对反事实结果生成机制的正确建模。作者通过引入协变量偏移（covariate shift）概念，在给定处理分配的条件下，得到了两个非参数识别公式：一个基于加权，另一个结合了反事实结果模型和加权函数。基于这两个公式和广义矩方法（GMM），作者开发了两个估计量，其中一个是双重稳健的——只要结果模型或加权模型中至少有一个正确设定，该估计量就是一致且渐近正态的。模拟和巴西肺炎球菌结合疫苗对全因肺炎风险影响的实证分析验证了方法的有效性。该工作将proximal CI的识别策略与SC的panel数据设定结合，对您关注的因果推断（特别是纵向数据中的处理效应估计）有直接的方法学启发。
- **关键技术**: `proximal causal inference`, `synthetic control`, `doubly robust estimation`, `generalized method of moments`, `covariate shift`, `nonparametric identification`
- **为什么对您有用**: 直接连接到您primary interest中的causal inference（特别是纵向/panel数据中的处理效应估计）和proximal CI方向。本文的识别策略（利用negative control变量处理未观测混杂）与您technical arsenal中very_familiar的estimation theory in causal inference高度契合，可立即用您熟悉的非参数统计和minimax bound工具分析其估计量的最优性（如是否达到半参效率界）。中期可做：若想将本文的proximal SC框架推广到更一般的多重处理或动态处理设定，需先在moderately_familiar的identification theory in causal inference上加强（特别是proximal g-formula的扩展）。

### 7. [10.1093/biomtc/ujae027](https://doi.org/10.1093/biomtc/ujae027) · [arXiv](https://arxiv.org/abs/2302.06054) — Single proxy control
- **作者**: Chan Park, David B Richardson, Eric J Tchetgen Tchetgen
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在负对照结局（NCO）框架下，研究平均处理效应（ATT）的非参数识别与估计。作者放宽了Tchetgen Tchetgen (2013) 提出的COCA方法中关键的秩保持（rank-preservation）假设，允许个体处理效应存在异质性，从而在仅需单个代理变量（NCO）的条件下实现非参数识别。这一结果与近期需要一对混淆代理变量的proximal causal inference形成对比，显著降低了代理变量的数据要求。估计方面，作者提出了三种策略：扩展倾向得分法、结果桥函数法以及双重稳健法，后者结合了前两者的优势。理论部分建立了桥函数的非参数识别条件，并给出了估计量的渐近性质。实证部分以巴西Zika病毒爆发对出生率的影响为例，展示了方法的应用。对您而言，本文在proximal CI框架下用单一代理变量替代一对代理变量的识别策略，直接关联您的因果推断兴趣，且其双重稳健估计器与您熟悉的debiased ML思想相通。
- **关键技术**: `negative control outcome`, `control outcome calibration approach`, `bridge function`, `doubly robust estimation`, `nonparametric identification`, `average causal effect for the treated`
- **为什么对您有用**: 本文直接关联您的primary interest中的proximal causal inference方向，提出了用单一代理变量（NCO）替代一对代理变量的非参数识别策略，降低了数据要求。您可以用very_familiar中的非参数统计和因果推断估计理论来审视其桥函数识别条件的紧性，或用moderately_familiar中的HOIF思想分析其双重稳健估计量的高阶性质。中期可做：若想将本文的单一代理框架推广到纵向设定，需先在moderately_familiar的identification theory in causal inference上长肌肉。

### 8. [10.1093/biomtc/ujae054](https://doi.org/10.1093/biomtc/ujae054) · [arXiv](https://arxiv.org/abs/2310.18905) — Incorporating nonparametric methods for estimating causal excursion effects in mobile health with zero-inflated count outcomes
- **作者**: Xueqing Liu, Tianchen Qian, Lauren Bell, Bibhas Chakraborty
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文在移动健康微随机试验（MRT）的框架下，针对零膨胀计数结局（如Drink Less试验中干预后一小时的屏幕浏览次数）定义并估计因果瞬时效应（causal excursion effect）。现有MRT因果推断方法主要处理连续或二元结局，本文首次将零膨胀计数结局纳入该框架。估计方法采用非参数技术（如核平滑或样条）对时间趋势和协变量进行建模，并结合加权和估计方程。作者建立了双向渐近理论（bidirectional asymptotics），即同时考虑个体数和时间点趋于无穷时的估计量一致性及正态性。模拟研究验证了有限样本性能，并在Drink Less试验数据上展示了方法的应用。对您而言，该文将因果推断中的瞬时效应估计与零膨胀计数数据结合，属于纵向因果推断与半参数估计的交叉问题，且其双向渐近框架可能对您熟悉的非参数统计和M估计理论有直接参考价值。
- **关键技术**: `causal excursion effect`, `micro-randomized trial`, `zero-inflated count`, `bidirectional asymptotics`, `kernel smoothing`, `weighted estimating equations`
- **为什么对您有用**: 该文直接连接您的primary interest中的纵向因果推断（micro-randomized trial）和计数数据估计问题。您的技术武器库中'非参数统计'和'M估计理论'（moderately_familiar）可直接用于理解其双向渐近证明和加权估计方程的核心机制。中期可做：若想将您熟悉的higher-order U-statistics的树宽/张量收缩视角用于分析其估计量的计算复杂度，需先在'HOIF'（moderately_familiar）上长肌肉，因为该文的非参数部分可能涉及高阶影响函数。

### 9. [10.1093/biomtc/ujae050](https://doi.org/10.1093/biomtc/ujae050) — Dissecting the colocalized GWAS and eQTLs with mediation analysis for high-dimensional exposures and confounders
- **作者**: Qi Zhang, Zhikai Yang, Jinliang Yang
- **期刊/来源**: Biometrics
- **机构**: University of New Hampshire · University of Nebraska–Lincoln
- **分类**: vol 80 · issue 2
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文针对GWAS与eQTL共定位分析中的因果推断问题，提出MedDiC方法。研究设定为高维暴露、混杂和中介变量下的中介分析，目标是对每个暴露估计总体间接效应（IE）。方法基于difference-in-coefficients思路，通过两阶段回归分离直接与间接效应，并利用高维正则化（如Lasso）处理维度问题。模拟表明MedDiC在检验功效、置信区间长度和计算速度上优于现有方法。应用于玉米和小鼠两个真实数据集，结果与外部生物学证据一致。对您而言，本文连接了因果推断中的高维中介分析与实际基因组学应用，其估计策略可借鉴于您熟悉的high-dimensional asymptotics和estimation theory in causal inference。
- **关键技术**: `difference-in-coefficients`, `high-dimensional mediation analysis`, `Lasso regularization`, `overall indirect effect estimation`, `colocalization analysis`
- **为什么对您有用**: 本文直接连接您的primary interest中的causal inference（mediation）和high-dimensional statistics，属于应用型方法论文。您的very_familiar武器库中的high-dimensional asymptotics和estimation theory in causal inference可直接用于理解其估计量的收敛性质，moderately_familiar的identification theory in causal inference可用于评估其识别假设的合理性。中期可做：若想改进其inference（如debiased Lasso或bootstrap），需先在moderately_familiar的semiparametric theory上长肌肉。

### 10. [10.1093/biomtc/ujae058](https://doi.org/10.1093/biomtc/ujae058) · [arXiv](https://arxiv.org/abs/2307.02331) — Differential recall bias in estimating treatment effects in observational studies
- **作者**: Suhwan Bong, Kwonsang Lee, Francesca Dominici
- **期刊/来源**: Biometrics
- **机构**: Seoul National University · Harvard University
- **分类**: vol 80 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文聚焦于观察性研究中自报告二元暴露的差分回忆偏倚（differential recall bias）对处理效应估计的影响。在回顾性队列设计中，回忆偏倚可能是有方向性的且随结局状态变化，导致暴露测量误差非随机缺失。作者在无验证数据可用的设定下，推导了平均处理效应（ATE）的可识别边界。提出了多种估计策略，分别依赖于不同的假设（如非差分回忆偏倚、工具变量、负对照等），并给出了一种结合先验知识的敏感性分析方法。通过模拟研究考察了多种模型误设场景下各方法的稳健性。最后将方法应用于童年身体虐待对成年心理健康影响的实证分析。该工作对您可能有用：它直接连接了因果推断中测量误差与识别假设的交叉点，您可以用非参数统计和M估计理论来审视其边界推导的紧致性，或考虑用高阶U统计量处理更复杂的偏倚结构。
- **关键技术**: `differential recall bias`, `partial identification`, `sensitivity analysis`, `non-differential misclassification`, `negative control`
- **为什么对您有用**: 本文属于因果推断中测量误差与识别假设的交叉方向，直接连接您的primary interest中的identification theory和sensitivity analysis。您可以用very_familiar的nonparametric statistics和minimax bounds工具来检验其ATE边界是否可被收紧，或用moderately_familiar的identification theory来评估其假设（如非差分回忆偏倚）在实证中的可检验性。中期可做：若想将方法推广到连续暴露或纵向设定，需先在semiparametric theory上长肌肉。

### 11. [10.1093/biomtc/ujae019](https://doi.org/10.1093/biomtc/ujae019) · [arXiv](https://arxiv.org/abs/2305.05913) — Case weighted power priors for hybrid control analyses with time-to-event data
- **作者**: Evan Kwiatkowski, Jiawen Zhu, Xiao Li, Herbert Pang, Grazyna Lieberman, Matthew A Psioda
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对随机对照试验（RCT）中利用外部对照数据增强内部对照组的混合分析问题，提出了一种基于病例加权的power prior方法。该方法的核心创新在于：每个外部对照患者的折扣权重并非全局统一，而是根据其与RCT对照数据的相容性单独计算，从而系统性地调整因未测量混杂等造成的差异。权重通过RCT数据估计的生存参数后验分布推导出的外部对照预测分布来确定，具体实现采用分段常数基线风险的Cox比例风险模型。模拟研究和基于非小细胞肺癌真实数据的分析表明，该方法在外部对照与RCT人群存在多种形式的不相容时仍能提供稳健的推断。该工作本质上是在生存分析框架下处理数据融合中的选择偏差问题，与因果推断中利用外部数据（如历史对照、真实世界证据）进行敏感性分析和稳健估计的子方向高度相关。
- **关键技术**: `power prior`, `case-weighting`, `piecewise constant baseline hazard`, `predictive distribution`, `hybrid control analysis`, `time-to-event data`
- **为什么对您有用**: 直接连接到primary interest中的causal inference子方向——利用外部数据增强RCT的识别与估计，是proximal causal inference和sensitivity analysis的典型应用场景。武器库中'identification theory in causal inference'（moderately_familiar）可直接用于分析其权重构造的识别假设（如未测量混杂的强弱程度），而'nonparametric statistics'（very_familiar）可用于评估其分段常数基线风险假设的敏感性。中期可做：若想将权重构造推广到更灵活的生存模型（如加性风险、加速失效时间），需先在'semiparametric theory'（moderately_familiar）上提升对生存数据半参效率界的理解。

### 12. [10.1093/biomtc/ujae021](https://doi.org/10.1093/biomtc/ujae021) — High-dimensional multisubject time series transition matrix inference with application to brain connectivity analysis
- **作者**: Xiang Lyu, Jian Kang, Lexin Li
- **期刊/来源**: Biometrics
- **机构**: University of California, Berkeley · University of Michigan
- **分类**: vol 80 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究高维多受试者时间序列中VAR模型转移矩阵的推断问题，特别关注测量误差和受试者条件变化对有效连接模式的影响。核心目标是同时检验多个受试者间转移矩阵的差异，而非单个矩阵的估计。方法包含三个关键组件：修正的EM算法处理测量误差，基于张量回归的检验统计量（利用偏差校正后的滞后自协方差对协变量回归），以及适当阈值化的同时检验。理论贡献包括：证明修正EM估计量的相合性，并证明所提检验能一致控制错误发现率且功效渐近趋于1。模拟和任务态fMRI脑连接数据分析验证了方法有效性。对您而言，该工作将高维VAR、测量误差和多受试者推断结合，其张量回归框架与您熟悉的higher-order U-statistics（树宽/张量收缩）有潜在技术交叉点，值得关注。
- **关键技术**: `high-dimensional VAR`, `measurement error`, `EM algorithm`, `tensor regression`, `simultaneous testing`, `false discovery control`
- **为什么对您有用**: 本文连接您的主要兴趣：高维时间序列因果推断（VAR转移矩阵）和假设检验。技术层面，其张量回归检验统计量可尝试用您熟悉的higher-order U-statistics树宽/张量收缩视角分析计算成本或构造更紧的界——这是**中期可做**的，需先在moderately_familiar的higher-order U-statistics理论上进一步熟悉。

### 13. [10.1093/biomtc/ujae051](https://doi.org/10.1093/biomtc/ujae051) · [arXiv](https://arxiv.org/abs/2502.18666) — On exact randomization-based covariate-adjusted confidence intervals
- **作者**: Jacob Fiksel
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文在随机化推断框架下，针对小样本随机实验中的协变量调整问题，提出了一种精确的置信区间构造方法。传统Fisher随机化检验的置信区间需通过反演检验（test inversion）在效应量网格上搜索，计算成本高昂，限制了实际应用。作者将Zhu和Liu（2023）关于均值差统计量的闭合形式置信区间结果，推广到协变量调整后的均值差统计量（ANCOVA型）。核心贡献是给出了一个基于观测数据即可检验的充分条件，保证该闭合形式置信区间具有正确的覆盖概率。模拟表明，该方法对非正态结果稳健，且计算时间与Fisher精确p值相当，消除了协变量调整下随机化推断的计算瓶颈。方法本身不依赖渐近近似，适用于小样本和有限总体推断。对您而言，该工作直接关联因果推断中实验设计的精确推断方法，其闭合形式推导思路可迁移至更复杂的因果估计量（如IV或proximal CI）的随机化推断。
- **关键技术**: `Fisher randomization test`, `test inversion`, `covariate adjustment via ANCOVA`, `closed-form confidence interval`, `finite-sample exact inference`
- **为什么对您有用**: 直接关联primary interest中的因果推断（实验设计下的精确推断），且其闭合形式推导思路可迁移至您熟悉的proximal CI或IV设定下的随机化推断。武器库中'非参数统计'和'因果推断估计理论'（very_familiar）足以理解并评估该方法的推广潜力——立即可做：尝试将闭合形式推广到更一般的treatment effect estimand（如分位数效应）。

### 14. [10.1093/biomtc/ujae023](https://doi.org/10.1093/biomtc/ujae023) · [arXiv](https://arxiv.org/abs/2302.01246) — Behavioral carry-over effect and power consideration in crossover trials
- **作者**: Danni Shi, Ting Ye
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文在潜在结果框架下系统研究交叉设计中的行为性 carry-over 效应。当 washout 期无法消除 carry-over 效应时（如比较有效性研究中行为性而非生物性 carry-over），基本估计量在 carry-over 满足符号条件时低估处理效应，这不会膨胀单侧检验的 I 类错误，但会降低检验功效。作者推导了交叉设计相比平行组设计仍更优的条件，即功效权衡的解析边界。同时发展了协变量调整方法以提升效率。通过 MTN-034/REACH 研究数据验证了理论结果。对您而言，本文是因果推断中纵向/交叉设计的一个干净识别与检验问题，其符号条件与功效分析思路可直接迁移至您熟悉的 IV 或 mediation 设定下的敏感性分析。
- **关键技术**: `potential outcomes framework`, `carry-over effect`, `sign condition`, `power trade-off`, `covariate adjustment`
- **为什么对您有用**: 直接连接 primary interest 中的因果推断（纵向/交叉设计）和假设检验。本文的符号条件+功效权衡分析是您 very_familiar 的 minimax bound 和 estimation theory 可以攻的口子——例如，能否将 carry-over 的符号条件推广为更一般的部分识别界，并用您熟悉的非参数下界工具刻画功效损失的最优性。中期可做：需先在 moderately_familiar 的 identification theory 上长肌肉（具体为部分识别下的检验问题）。

### 15. [10.1093/biomtc/ujae049](https://doi.org/10.1093/biomtc/ujae049) — Robustness of response-adaptive randomization
- **作者**: Xiaoqing Ye, Feifang Hu, Wei Ma
- **期刊/来源**: Biometrics
- **机构**: Renmin University of China · George Washington University
- **分类**: vol 80 · issue 2
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 本文研究响应自适应随机化（DBCD）在模型误设下的稳健性。DBCD 根据累积响应调整分配概率以平衡伦理，但现有理论多假设响应模型正确指定。作者证明，即使响应真实分布偏离设计模型，DBCD 的分配比例仍保持相合性和渐近正态性。进一步，针对三种常用线性回归模型（均值差、ANCOVA I、ANCOVA II）估计处理效应，允许模型任意误设，推导了估计量的相合性和渐近正态性。结果显示，包含协变量-处理交互项的 ANCOVA II 模型给出最有效的估计量。这些结果为 DBCD 在模型误设场景下的应用提供了理论支撑，对因果推断中自适应试验的设计与分析有直接参考价值。
- **关键技术**: `response-adaptive randomization`, `doubly adaptive biased coin design`, `model misspecification`, `ANCOVA`, `asymptotic normality`, `treatment effect estimation`
- **为什么对您有用**: 本文直接关联因果推断中自适应试验的估计问题，特别是处理效应估计在模型误设下的稳健性。您的武器库中'因果推断的估计理论'和'非参数统计'可用于分析其渐近性质，而'软件工具开发'可复现其模拟验证。中期可做：将 ANCOVA II 的稳健性结果推广到更复杂的纵向或中介分析设定，需先在'因果推断的识别理论'上加强。

### 16. [10.1093/biomtc/ujae047](https://doi.org/10.1093/biomtc/ujae047) — Sequential covariate-adjusted randomization via hierarchically minimizing Mahalanobis distance and marginal imbalance
- **作者**: Haoyu Yang, Yichen Qin, Yang Li, Feifang Hu
- **期刊/来源**: Biometrics
- **机构**: Renmin University of China · University of Cincinnati · George Washington University
- **分类**: vol 80 · issue 2
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对比较性临床试验中的序贯分配问题，提出了一种新的自适应随机化方法。该方法在每次单个患者入组时，通过分层最小化新定义的修正马氏距离（衡量协变量整体平衡）和边际不平衡（两组样本量差异）来实现分配，且明确指定了优化优先级。与现有需要成对或分组分配的方法不同，该方法实现了逐个体分配，更贴合临床实际。理论上证明了不平衡测度的收敛性以及后续处理效应估计的无偏性。模拟和真实数据分析表明，该方法在协变量平衡和边际平衡上均优于现有序贯随机化方法。对您而言，该方法为因果推断中的随机化试验设计提供了更精细的控制工具，尤其适用于纵向或序贯入组的临床试验场景。
- **关键技术**: `adaptive randomization`, `Mahalanobis distance`, `covariate balance`, `sequential allocation`, `treatment effect estimation`
- **为什么对您有用**: 本文直接关联您的因果推断兴趣中的随机化试验设计，特别是序贯分配下的协变量平衡问题。您武器库中'因果推断的估计理论'和'非参数统计'可用于分析该方法的渐近性质或扩展到更复杂的处理效应估计。中期可做：若想将此法与您熟悉的'高阶U统计量'结合分析其平衡性，需先熟悉'HOIF'工具。

### 17. [10.1093/biomtc/ujae037](https://doi.org/10.1093/biomtc/ujae037) — Regression models for average hazard
- **作者**: Hajime Uno, Lu Tian, Miki Horiguchi, Satoshi Hattori, Kenneth L Kehl
- **期刊/来源**: Biometrics
- **机构**: Dana-Farber Cancer Institute · Stanford University · The University of Osaka
- **分类**: vol 80 · issue 2
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对时间-事件结局的治疗效应度量，提出了一种基于平均风险（AH）的回归分析方法。传统Cox比例风险模型的风险比存在可解释性局限，而AH定义为给定时间窗口内无删失的人时发病率，具有直观的流行病学解释。作者考虑了三种删失机制：独立删失、组别特异性删失和协变量依赖删失，并建立了相应的AH回归模型。该方法与稳健Poisson回归紧密相关，但在存在删失时比Poisson回归更稳健。AH回归可以同时提供绝对差和相对比的治疗效应总结，并允许调整协变量，从而提升效应量解释的正确性。该方法为Cox风险比提供了一种有用的替代方案，尤其适用于需要明确时间窗口的临床试验或流行病学研究。对您而言，本文的AH回归框架与您的因果推断（特别是纵向数据中的治疗效应度量）和流行病学应用兴趣直接相关，其稳健Poisson回归的链接也为您熟悉的M估计理论提供了分析切入点。
- **关键技术**: `Average hazard with survival weight`, `Robust Poisson regression`, `Censoring mechanisms`, `Truncation time τ`, `Absolute risk difference`, `Relative risk`
- **为什么对您有用**: 本文直接关联您的因果推断兴趣中的纵向数据治疗效应度量，以及流行病学应用兴趣。AH回归作为Cox风险比的替代，其稳健Poisson回归框架与您非常熟悉的M估计理论高度契合，您可以用非参数统计和估计理论工具分析其渐近性质。中期可做：若想深入其半参数效率，需先在 moderately_familiar 的 semiparametric theory 上提升。

### 18. [10.1093/biomtc/ujae033](https://doi.org/10.1093/biomtc/ujae033) — Identifying temporal pathways using biomarkers in the presence of latent non-Gaussian components
- **作者**: Shanghong Xie, Donglin Zeng, Yuanjia Wang
- **期刊/来源**: Biometrics
- **机构**: Southwestern University of Finance and Economics · University of Michigan · Columbia University
- **分类**: vol 80 · issue 2
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对多主体时间序列生物标志物数据，提出一种识别潜在时间路径的方法。模型假设观测数据包含高斯信号和非高斯噪声（如伪迹、遗传风险因素等），现有VAR和动态因果建模未考虑后者。方法核心是先用独立成分分析（ICA）提取未观测的非高斯成分，再对残差用矩估计法分别估计节点间的同期网络和时间网络。作者证明了模型的可识别性，并推导了网络估计量的渐近性质。算法计算快速、可扩展。模拟和ADHD脑区生物标志物数据应用表明，时间网络连接不同脑区，同期网络多为同区域双侧连接。对您有用：该方法将ICA与矩估计结合处理潜变量，其识别策略和渐近理论可迁移至proximal CI或mediation分析中的unobserved confounder设定。
- **关键技术**: `independent component analysis (ICA)`, `method of moments`, `vector autoregression (VAR)`, `contemporaneous vs temporal network separation`, `identifiability under non-Gaussian components`
- **为什么对您有用**: 连接primary interest的因果推断子方向：处理未观测混杂的时间序列因果识别。技术武器库中'非参数统计'和'因果推断估计理论'可直接用于分析其ICA+矩估计的识别条件是否可推广至proximal g-formula框架。中期可做：需先在moderately_familiar的'identification theory in causal inference'上长肌肉，以严格检验其可识别性假设在更一般因果图下的充分性。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1093/biomtc/ujae031](https://doi.org/10.1093/biomtc/ujae031) · [arXiv](https://arxiv.org/abs/2402.15071) — High-dimensional covariate-augmented overdispersed poisson factor model
- **作者**: Wei Liu, Qingzhi Zhong
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对高维过离散计数数据，提出协变量增强的泊松因子模型（COAP），联合进行因子分析与大系数矩阵估计。模型假设响应变量和协变量均存在潜在因子结构，并通过低秩约束刻画系数矩阵，以捕捉变量间的相互依赖。为处理非线性、双潜在矩阵及低秩约束带来的计算挑战，作者提出结合Laplace近似和Taylor近似的变分估计方案。同时，基于奇异值比值准则开发了因子数和系数矩阵秩的确定方法。理论方面，给出了确保计算可识别性的可识别条件。模拟表明COAP在估计精度和计算效率上优于现有方法，并应用于CITE-seq数据集。该工作对您在高维统计和统计计算方面的兴趣有直接参考价值，特别是其变分推断与低秩分解的结合策略。
- **关键技术**: `variational inference`, `Laplace approximation`, `Taylor approximation`, `low-rank matrix estimation`, `singular value ratio criterion`, `Poisson factor model`
- **为什么对您有用**: 连接高维统计（因子模型与低秩估计）和统计计算（变分推断的数值方法）。武器库中'高维渐近理论'和'软件工程'可直接用于复现或改进其变分EM算法；'逆问题'视角可用于分析Laplace近似的偏差。中期可做：若先熟悉'半参数理论'中的profile似然，可推导该变分估计的渐近效率。

## 非参数 / 半参数  *(nonparam_semipara, 2 篇)*

### 1. [10.1093/biomtc/ujae035](https://doi.org/10.1093/biomtc/ujae035) — Efficient data integration under prior probability shift
- **作者**: Ming-Yueh Huang, Jing Qin, Chiung-Yu Huang
- **期刊/来源**: Biometrics
- **机构**: Institute of Statistical Science, Academia Sinica · National Institutes of Health · National Institute of Allergy and Infectious Diseases · University of California, San Francisco
- **分类**: vol 80 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究在 prior probability shift（即不同数据集的 Y 分布不同，但 P(X|Y) 相同）下的高效数据整合问题。目标是在该假设下，利用多个源数据集提高目标数据集的估计效率。方法上，作者提出了一种半参数估计框架，通过经验似然或加权似然构造估计方程，并引入自适应 LASSO 惩罚进行高维协变量选择，所得估计量具有 oracle 性质（即变量选择一致性且渐近正态）。对于连续或离散结局均适用，突破了现有方法仅限离散结局的限制。此外，作者提出了一种新颖的半参数似然比检验，将原假设下的条件密度嵌入 Neyman 平滑备择，检验 prior probability shift 假设是否成立。模拟和实际数据验证了方法的有效性。该工作对您可能有用：它连接了您的 semiparametric theory 和 high-dimensional statistics 兴趣，且检验部分涉及 hypothesis testing 工具，可作为数据融合场景下假设检验与估计的参考。
- **关键技术**: `semiparametric likelihood ratio test`, `adaptive LASSO`, `oracle property`, `Neyman's smooth alternatives`, `empirical likelihood`
- **为什么对您有用**: 本文直接关联您的 semiparametric & nonparametric theory 和 high-dimensional statistics 兴趣，特别是半参数似然比检验与自适应 LASSO 的结合。您可以用 very_familiar 的 minimax bounds 工具分析其估计量的最优性，或用 moderately_familiar 的 semiparametric theory 验证其效率界。中期可做：若想将检验推广到更一般的 shift 设定，需先在 moderately_familiar 的 identification theory 上加强。

### 2. [10.1093/biomtc/ujae024](https://doi.org/10.1093/biomtc/ujae024) — Deep partially linear cox model for current status data
- **作者**: Qiang Wu, Xingwei Tong, Xingqiu Zhao
- **期刊/来源**: Biometrics
- **机构**: Beijing Normal University · Hong Kong Polytechnic University
- **分类**: vol 80 · issue 2
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 针对当前状态数据（current status data），提出深度部分线性Cox模型，以缓解维数灾难。模型用深度神经网络（DNN）拟合非线性协变量效应，用单调样条逼近基线累积风险函数，兼具灵活性与可解释性。建立了最大似然估计的收敛速率，并证明治疗协变量效应的有限维估计量是√n-相合、渐近正态且达到半参数有效界。通过模拟和新闻流行度真实数据验证了方法性能。该工作将深度学习和半参数效率理论结合到区间删失生存数据中，对您在半参数理论和非参数统计方面的兴趣有直接参考价值。
- **关键技术**: `deep neural networks`, `monotone splines`, `semiparametric efficiency bound`, `current status data`, `partially linear Cox model`
- **为什么对您有用**: 本文直接连接您的非参数与半参数理论兴趣，具体在区间删失数据（current status data）这一设定下，展示了如何用DNN+单调样条实现半参数有效估计。您的技术武器库中'非参数统计'和'半参数理论'（moderately_familiar）可直接用于分析其估计量的收敛速率是否最优，以及能否将类似框架推广到其他删失类型。中期可做：需先在HOIF（Higher-Order Influence Functions）上长肌肉，以检验其效率界推导的紧性。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1093/biomtc/ujae036](https://doi.org/10.1093/biomtc/ujae036) — Testing conditional quantile independence with functional covariate
- **作者**: Yongzhen Feng, Jie Li, Xiaojun Song
- **期刊/来源**: Biometrics
- **机构**: Tsinghua University · Renmin University of China · Peking University
- **分类**: vol 80 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文提出一种新的非参数条件分位数独立性检验，用于检验标量响应变量与函数型协变量在连续分位数水平上的条件独立性。检验统计量基于随机投影的函数型协变量构建的Cramér–von Mises型经验过程，通过投影假设（与原假设几乎必然等价）有效避免了函数型数据的“维数灾难”。在温和假设下推导了检验统计量的渐近零分布，并研究了其全局和局部渐近功效性质，特别证明了该统计量能以参数速率检测趋近于零假设的广泛局部备择假设。推荐使用简单的乘子bootstrap方法估计临界值。通过蒙特卡洛模拟和EEG数据集分析验证了有限样本性能。该工作对您在高维假设检验方向有直接参考价值，尤其是其处理函数型数据时采用的随机投影降维策略，与您熟悉的非参数统计和高维渐近工具高度契合。
- **关键技术**: `Cramér–von Mises test statistic`, `empirical process indexed by random projections`, `multiplier bootstrap`, `functional data analysis`, `conditional quantile independence`
- **为什么对您有用**: 本文直接对应您primary interest中的“hypothesis testing”和“high-dimensional statistics”子方向，具体是函数型数据下的条件独立性检验。您武器库中“非参数统计”和“高维渐近”工具可直接用于理解其经验过程投影降维的核心机制，且其随机投影策略与您熟悉的“inverse problems with random noise”有技术共鸣。**中期可做**：若想将类似投影检验推广到您的higher-order U-statistics设定（如检验高阶交互效应），需先在moderately_familiar的“higher-order U-statistics理论”上加强，特别是理解投影后的U-statistic渐近分布。

### 2. [10.1093/biomtc/ujae056](https://doi.org/10.1093/biomtc/ujae056) — Efficient testing of the biomarker positive and negative subgroups in a biomarker-stratified trial
- **作者**: Lang Li, Anastasia Ivanova
- **期刊/来源**: Biometrics
- **机构**: University of North Carolina at Chapel Hill
- **分类**: vol 80 · issue 2
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对生物标志物分层随机对照试验中，标志物阳性与阴性亚组的治疗效应检验问题。传统方法通常只检验阳性亚组或总人群的效应，但可能掩盖阴性亚组无效而总人群显著的情况。作者利用两个亚组治疗效应单调非递减（阳性≥阴性）的等渗假设，构造了一种高效的联合检验方法。该方法通过等渗回归对两个亚组的效应进行约束估计，并基于此构建检验统计量，在控制族系错误率的同时提高了检验效能。与现有方法相比，该方法在标志物阳性率低于0.5时能大幅减少所需样本量，使在关键试验中同时评估两个亚组的效应变得可行。理论分析证明了该检验在等渗假设下的渐近有效性，模拟研究验证了其有限样本性能。对您而言，本文的等渗约束检验思路可迁移至因果推断中的敏感性分析或异质性处理效应检验，且其样本量节省的量化结果对设计实际临床试验有直接参考价值。
- **关键技术**: `isotonic regression`, `multiple testing`, `biomarker-stratified trial`, `constrained likelihood ratio test`, `sample size calculation`
- **为什么对您有用**: 本文属于假设检验方向，直接连接您的primary interest中的hypothesis testing。其等渗约束检验的渐近有效性分析可用您very_familiar的minimax bounds工具来验证是否达到最优检验效能。中期可做：若将等渗假设放松为部分单调或允许非参数形式，需先提升moderately_familiar的semiparametric theory能力。

## 流行病学  *(epidemiology, 2 篇)*

### 1. [10.1093/biomtc/ujae038](https://doi.org/10.1093/biomtc/ujae038) · [arXiv](https://arxiv.org/abs/2304.01912) — Bayesian meta-analysis of penetrance for cancer risk
- **作者**: Thanthirige Lakshika M Ruberu, Danielle Braun, Giovanni Parmigiani, Swati Biswas
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对多基因面板检测中癌症易感基因的外显率估计问题，提出了一种贝叶斯分层随机效应元分析方法。该方法能够整合报告不同风险度量（如外显率、相对风险、比值比）的研究，并考虑相关不确定性。通过马尔可夫链蒙特卡洛算法估计参数的后验分布，进而得到外显率及其可信区间。模拟研究基于两个中等风险乳腺癌易感基因ATM和PALB2的数据，结果表明所提方法在可信区间覆盖率和均方误差方面显著优于现有方法。最后，作者将方法应用于ATM基因致病突变携带者乳腺癌外显率的估计。本文是流行病学中因果推断（外显率估计）的典型应用，其贝叶斯元分析框架对整合异质性研究具有参考价值。
- **关键技术**: `Bayesian hierarchical random-effects model`, `Markov chain Monte Carlo`, `meta-analysis`, `penetrance estimation`
- **为什么对您有用**: 本文属于流行病学应用，直接对应您的secondary interest。其贝叶斯元分析框架整合不同风险度量的思路，对您关注的因果推断中异质性研究整合（如IV或敏感性分析中的多源证据）有借鉴意义。武器库中'identification theory in causal inference'和'M-estimation theory'可帮助您理解其模型假设与估计策略，但核心方法（贝叶斯分层模型）并非您的主要工具，因此属于'暂不可做'——需补充贝叶斯建模经验。

### 2. [10.1093/biomtc/ujae034](https://doi.org/10.1093/biomtc/ujae034) — Data science for infectious disease data analytics: an introduction with R, by Lily Wang, CRC Press, 2022 ISBN-13: 978-1032187426, https://www.routledge.com/Data-Science-for-Infectious-Disease-Data-Analytics-An-Introduction-with-R/Wang/p/book/9781032187426
- **作者**: Gillian Cheng, Andrei R Akhmetzhanov
- **期刊/来源**: Biometrics
- **机构**: National Taiwan University
- **分类**: vol 80 · issue 2
- 相关性 1/10 · novelty: `survey`
- **摘要**: 本文是对Lily Wang所著《Data Science for Infectious Disease Data Analytics: an Introduction with R》一书的书评，发表于Biometrics期刊。该书旨在为传染病数据分析提供入门级的数据科学方法介绍，涵盖数据清洗、可视化、统计建模（如时间序列、空间分析）以及机器学习在疫情监测中的应用。书评指出，该书以R语言为工具，强调实际数据集的操作和代码示例，适合公共卫生和流行病学领域的初学者。然而，书评也批评该书在因果推断方法（如工具变量、G-computation）和高级统计理论（如半参数效率界）方面覆盖不足，且对现代数据科学工具（如深度学习、贝叶斯非参数方法）的讨论较为浅显。总体而言，该书是一本实用的入门教材，但方法学深度有限，不适合寻求前沿统计方法的研究者。对于您而言，该书可作为流行病学应用领域的快速入门读物，但您更关注的方法学创新（如proximal causal inference、debiased ML）在其中几乎未被涉及，因此阅读价值主要在于了解传染病数据分析的常见数据结构和R实现流程。
- **关键技术**: `R programming`, `time series analysis`, `spatial statistics`, `machine learning for epidemiology`
- **为什么对您有用**: 本文属于流行病学应用领域的书评，连接您的secondary interest中的流行病学数据集和实际分析流程。您的technical arsenal中'软件发展'（very_familiar）可用于评估书中R代码的效率和可扩展性，但核心方法学（如因果推断、半参数理论）在书中缺失，因此无法直接攻入。作为gateway reading，该书适合快速了解传染病数据的基本结构（如病例计数、接触追踪数据），但方法学深度不足以支撑您的研究方向。建议仅作为背景阅读，不投入全文精读。

## 其他  *(other, 8 篇)*

### 1. [10.1093/biomtc/ujae048](https://doi.org/10.1093/biomtc/ujae048) — A Bayesian semi-parametric model for learning biomarker trajectories and changepoints in the preclinical phase of Alzheimer’s disease
- **作者**: Kunbo Wang, William Hua, MeiCheng Wang, Yanxun Xu
- **期刊/来源**: Biometrics
- **机构**: Johns Hopkins University
- **分类**: vol 80 · issue 2
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对阿尔茨海默病（AD）临床前阶段生物标志物的纵向轨迹与变点问题，提出一个贝叶斯半参数框架。研究目标是联合建模生物标志物（如ptau181）的纵向变化与相对于症状发作时间的变点，同时处理左截断和右删失数据。核心创新在于允许部分个体可能永远不会进展到MCI或AD，而非假设所有个体最终都会发病。方法上采用贝叶斯半参数模型，通过Dirichlet过程混合对异质性人群进行建模，并利用MCMC进行后验推断。模拟研究验证了方法的有效性，并在BIOCARD队列数据上展示了ptau181生物标志物的临床轨迹。该工作主要贡献在于统计建模与流行病学应用，而非因果推断或高维理论。
- **关键技术**: `Bayesian semiparametric model`, `Dirichlet process mixture`, `changepoint model`, `left truncation and right censoring`, `MCMC`
- **为什么对您有用**: 本文属于流行病学应用，与您的secondary interest（流行病学数据集与因果推断应用）相关。但方法学核心是贝叶斯半参数纵向建模，与您primary interests中的因果推断、高维统计、U统计量等方向无直接技术交集。武器库中very_familiar的非参数统计和M估计理论可帮助理解模型框架，但无直接可攻问题。作为流行病学应用，可读全文了解AD生物标志物数据分析的典型挑战（左截断、异质性、治愈率），但方法学novelty有限。

### 2. [10.1093/biomtc/ujae017](https://doi.org/10.1093/biomtc/ujae017) · [arXiv](https://arxiv.org/abs/2106.03811) — Estimating the size of a closed population by modeling latent and observed heterogeneity
- **作者**: Francesco Bartolucci, Antonio Forcina
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文在 capture-recapture 框架下，针对封闭种群大小估计问题，提出了一种新的潜类模型，允许捕获概率依赖于未观测的潜类型、协变量以及之前的捕获历史（即序列依赖）。方法核心是将 Liu 等人的经验似然（EL）思路扩展至更灵活的设定，直接估计总体大小而非通过协变量配置的条件估计求和。作者引入了一种比传统 EL 更有效的非参数分量估计方法，并证明了协变量的非参数分布与从未被捕获概率之间的映射是严格单调的一一对应。采用 Fisher-scoring 算法进行极大似然估计，并给出了构造总体大小的 profile 似然置信区间的程序。渐近理论结果被简要勾勒。基于两个真实数据集的例示和模拟研究表明，在估计总体漏计数时，所提方法在效率上显著优于条件极大似然估计，尤其在样本量不够大时。对您而言，本文属于应用统计方法论文，与您的主要兴趣（因果推断、高维统计等）无直接技术交集，但 capture-recapture 与流行病学中的队列漏报问题有概念联系，可作为流行病学应用方向的入门阅读。
- **关键技术**: `empirical likelihood`, `latent class model`, `capture-recapture`, `Fisher-scoring algorithm`, `profile likelihood confidence interval`
- **为什么对您有用**: 本文属于 capture-recapture 方法的应用统计论文，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接技术连接。作为流行病学方向的 gateway reading，它清晰展示了种群大小估计在队列漏报问题中的建模思路（潜类+序列依赖），但方法学 novelty 有限（主要是 EL 的扩展）。武器库中无直接可攻工具，暂不可做。

### 3. [10.1093/biomtc/ujae057](https://doi.org/10.1093/biomtc/ujae057) · [arXiv](https://arxiv.org/abs/2210.09560) — A Bayesian convolutional neural network-based generalized linear model
- **作者**: Yeseul Jeon, Won Chang, Seonghyun Jeong, Sanghoon Han, Jaewoo Park
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出一种贝叶斯卷积神经网络广义线性模型（Bayesian CNN-GLM），旨在解决CNN在图像/空间数据回归中难以进行统计推断（如协变量效应估计、不确定性量化）的问题。方法核心是将CNN最后一个隐藏层的节点（经MC dropout多次实现）作为GLM的协变量，从而在保留CNN预测灵活性的同时获得可解释的回归系数和不确定性度量。通过集成多个MC dropout实现下的GLM拟合，该方法能够吸收特征提取过程中的不确定性。作者将方法应用于疟疾发病率数据、脑肿瘤图像数据和fMRI数据，展示了其在处理高维相关输入与向量协变量共存场景下的实用性。该方法本质上是一种两阶段策略：先用CNN提取特征，再用GLM做推断，其统计效率依赖于dropout近似后验的准确性。对您而言，本文属于应用导向的方法开发，与您的主要兴趣（因果推断、高维统计、半参理论）无直接技术交集，但若您未来涉足图像型协变量的因果推断或空间流行病学应用，其将CNN嵌入GLM的框架思路可作为入门参考。
- **关键技术**: `Monte Carlo dropout`, `generalized linear model`, `convolutional neural network`, `uncertainty quantification`, `ensemble GLM`
- **为什么对您有用**: 本文属于应用统计方法开发，与您的主要兴趣（因果推断、高维统计、半参理论）无直接技术交集。其核心贡献在于为CNN提供推断能力，而非您关注的identification、efficiency或minimax理论。作为gateway reading，本文对流行病学应用（疟疾、脑肿瘤）有数据和分析流程展示，但方法学深度有限。武器库中'非参数统计'和'因果推断估计理论'可帮助您理解其两阶段策略的局限性（如dropout近似后验的偏差），但并无直接可攻的问题。暂不可做：核心机器不在武器库里，缺贝叶斯深度学习与变分推断的专门知识。

### 4. [10.1093/biomtc/ujae022](https://doi.org/10.1093/biomtc/ujae022) — Flagging unusual clusters based on linear mixed models using weighted and self-calibrated predictors
- **作者**: Charles E McCulloch, John M Neuhaus, Ross D Boylan
- **期刊/来源**: Biometrics
- **机构**: University of California, San Francisco
- **分类**: vol 80 · issue 2
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文研究基于线性混合模型（LMM）中随机截距的预测值来识别极端或异常聚类（如表现差的医院或健康快速下降的患者）的问题。传统上，常用的最佳线性无偏预测（BLUP）和固定效应预测（FEP）被用于标记极端聚类，但理论分析和数值评估表明，这两种方法的错误标记率要么高得不可接受（极限下接近0.5），要么过于保守（远低于0.05），导致正确标记率极低。作者提出了新的标记方法，包括加权预测器和一种称为“自校准”的简单易用版本，能够有效控制错误标记率。新方法在控制错误标记率的同时，显著提高了正确标记率。通过儿童哮喘住院时长的儿科医院数据进行了应用演示。本文主要贡献在于提出了一种实用的统计工具，用于在层次数据中识别异常聚类，但方法学上属于应用导向的改进，而非理论突破。
- **关键技术**: `best linear unbiased predictor (BLUP)`, `fixed effects predictor (FEP)`, `linear mixed model (LMM)`, `self-calibrated predictor`, `weighted predictor`, `cluster-specific intercepts`
- **为什么对您有用**: 本文属于应用统计方法论文，与您的主要兴趣（因果推断、高维统计等）无直接交集。但如果您在流行病学或卫生服务研究中遇到类似的分层数据异常检测问题（如医院绩效评估），本文提供的自校准方法可能是一个实用的工具。不过，从方法学角度看，本文并未引入您武器库中的核心工具（如U统计量、半参效率理论等），因此作为gateway reading的价值有限，不值得花时间精读全文。

### 5. [10.1093/biomtc/ujae030](https://doi.org/10.1093/biomtc/ujae030) · [arXiv](https://arxiv.org/abs/2212.14567) — Topical hidden genome: discovering latent cancer mutational topics using a Bayesian multilevel context-learning approach
- **作者**: Saptarshi Chakraborty, Zoe Guan, Colin B Begg, Ronglai Shen
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对癌症基因组超罕见体细胞突变的高维稀疏数据，提出一种贝叶斯多层上下文学习框架。传统统计方法无法处理数百万变异位点与数千肿瘤样本的极端稀疏数据，作者在前期“隐藏基因组”模型基础上，引入主题模型（topic model）对突变上下文进行降维，生成可解释的去相关元特征主题。采用高效MCMC算法实现全贝叶斯推断，规模远超现有高维多分类回归方法。在全基因组泛癌分析数据集上，发现与紫外线暴露、衰老及表观基因组组织相关的突变主题，交叉验证预测性能媲美随机森林和深度学习黑箱模型。对您而言，本文属于生物统计应用，与您的主要兴趣方向（因果推断、高维统计、U统计量等）无直接技术连接，但主题模型降维思路在流行病学罕见变异分析中可能有参考价值。
- **关键技术**: `topic model`, `Bayesian multilevel model`, `MCMC`, `dimension reduction`, `ultra-high-dimensional sparse data`
- **为什么对您有用**: 本文属于流行病学/生物统计应用，与您的主要兴趣方向（因果推断、高维RMT、U统计量、半参效率理论）无直接技术重叠。武器库中无贝叶斯主题模型或MCMC核心工具，暂不可做。作为流行病学应用，可作入门阅读了解罕见变异分析的数据结构，但方法学迁移价值有限。

### 6. [10.1093/biomtc/ujae029](https://doi.org/10.1093/biomtc/ujae029) — Addressing age measurement errors in fish growth estimation from length-stratified samples
- **作者**: Nan Zheng, Atefeh Kheirollahi, Yildiz Yilmaz
- **期刊/来源**: Biometrics
- **机构**: Memorial University of Newfoundland
- **分类**: vol 80 · issue 2
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文针对鱼类生长模型中的年龄测量误差（MEs）和长度分层年龄抽样（LSAS）的联合问题，提出了一种新的估计方法。目标是在LSAS这种两阶段响应选择性抽样设计下，利用长度-年龄数据估计生长曲线参数，同时纠正年龄MEs带来的偏差。方法核心是结合经验比例似然（empirical proportion likelihood）处理LSAS的抽样偏差，以及结构误差变量（structural errors-in-variables）方法处理年龄MEs。为建模年龄分布，采用了continuation ratio-logit模型，该模型与真实年龄分布的随机性一致。通过离散化年龄和长度分布，显著提升了计算效率，并契合实际数据中离散化的特点。模拟研究表明，即使年龄MEs很小，忽略它也会导致生长估计的显著偏差，而新方法在不同MEs幅度下均表现良好，且能准确估计参数标准误。真实数据分析验证了模型诊断工具的有效性。本文对您作为统计计算和软件开发者有一定参考价值，其离散化策略和提供的R代码可视为处理复杂抽样与测量误差的实用案例，但方法学创新性有限，属于应用领域的方法改进。
- **关键技术**: `empirical proportion likelihood`, `structural errors-in-variables`, `continuation ratio-logit model`, `length-stratified age sampling`, `discretization approach`
- **为什么对您有用**: 本文属于应用统计（渔业生物学）的方法论文，与您的primary interests（因果推断、高维、U统计等）无直接交集。但作为统计计算和软件开发的兴趣点，其离散化策略提升计算效率的思路以及提供的完整R代码，对您开发统计软件有微弱的参考价值。武器库中'软件发展'一项可直接用于复现或扩展其代码。本文不值得投入全文阅读，除非您对渔业数据或测量误差校正有特定兴趣。

### 7. [10.1093/biomtc/ujae026](https://doi.org/10.1093/biomtc/ujae026) — Well-spread samples with dynamic sample sizes
- **作者**: Blair Robertson, Chris Price, Marco Reale
- **期刊/来源**: Biometrics
- **机构**: University of Canterbury
- **分类**: vol 80 · issue 2
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文提出一种新的空间抽样设计方法，用于在任意辅助空间上生成空间平衡（well-spread）样本，并支持动态样本量调整，适用于主抽样（master sampling）场景。方法仅需种群单元间的距离度量，不依赖空间坐标，通过数值实验与现有设计（如广义随机分块、局部枢轴法）对比，证明其在空间平衡性和估计精度上的竞争力。核心机制基于距离驱动的样本选择算法，可灵活适应不同样本量需求，无需重新设计。应用实例使用多个辅助变量（如植被指数、地形）估计巴西亚马逊东部地上生物量总量，并扩展到多目标调查（同时估计生物量、初级生产力和黏土含量）。对您而言，本文属于应用导向的空间统计方法，与您的主要兴趣（因果推断、高维统计等）无直接技术重叠，但多目标抽样设计的思想可能对流行病学或环境科学中的因果推断数据收集有间接启发。
- **关键技术**: `spatial sampling design`, `well-spread sample`, `master sampling`, `distance-based sampling`
- **为什么对您有用**: 本文属于应用统计方法，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接技术连接。武器库中无对应工具可攻其核心问题（空间抽样设计）。作为流行病学或环境科学的数据收集方法，可作入门了解，但非优先阅读。

### 8. [10.1093/biomtc/ujae053](https://doi.org/10.1093/biomtc/ujae053) — Introduction to statistical modelling and inference by Murray Aitkin, CRC Press, 2023, ISBN: 978-1032105710, https://www.routledge.com/Introduction-to-Statistical-Modelling-and-Inference/Aitkin/p/book/9781032105710
- **作者**: Chuhsing Kate Hsiao
- **期刊/来源**: Biometrics
- **机构**: National Taiwan University
- **分类**: vol 80 · issue 2
- 相关性 1/10 · novelty: `survey`
- **摘要**: 这是一篇书评，介绍Murray Aitkin的《Introduction to Statistical Modelling and Inference》一书。该书评简要概述了教材的内容，包括统计建模、似然推断、贝叶斯方法等核心主题。书评指出该书适合作为研究生统计推断课程的参考读物，强调其通过实际例子讲解统计概念的教学风格。书评作者认为该书在统计建模与推断的教学上有一定价值，但未提供深入的方法学评价或与前沿研究的对比。对于您而言，这是一本教科书而非研究论文，不涉及您主要兴趣中的任何具体理论或方法进展。
- **关键技术**: `statistical modelling`, `likelihood inference`, `Bayesian methods`
- **为什么对您有用**: 这是一篇书评，属于教学资源介绍，不涉及您主要兴趣中的因果推断、高维统计、U-统计量或计算复杂度等任何具体子方向。它既不是入门读物（因为您已远超教材水平），也不提供可迁移的方法学工具。无需阅读全文。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

