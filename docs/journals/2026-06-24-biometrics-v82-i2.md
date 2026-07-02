# Biometrics — Vol 82  Issue 2  ·  2026-06-24

- 共 5 篇 · Biometrics
- 目录核对 ⚠️ 疑似漏 51 篇（对照 OpenAlex 61 篇）：10.1093/biomtc/ujag107、10.1093/biomtc/ujag071、10.1093/biomtc/ujag076、10.1093/biomtc/ujag105、10.1093/biomtc/ujag057 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期内容主要围绕**因果推断的可解释性与异质性分析**以及**纵向复杂数据建模**两条主线展开，同时包含一篇功能数据假设检验与一篇临床试验设计书评。因果推断主线集中探讨效应估计的稳健性与亚组发现，涉及 Meta 分析、纵向数据及内生性处理；纵向数据建模则侧重于解决测量误差、缺失值与未观测异质性带来的推断难题。

在**因果推断与异质性**主线上，本期重点推进了效应估计从“平均”向“特定总体”与“特定亚组”的精细化延伸。针对 Meta 分析中跨研究异质性问题，*Causally-interpretable random-effects meta-analysis* 指出现有方法常因忽略非分布差异来源而导致方差估计偏小，进而提出引入随机效应捕获额外变异性的整合估计量，以实现因果效应的准确推广与迁移。针对纵向临床试验中的处理效应异质性，*Subgroup identification via Interaction Tree...* 将交互树（ITree）与重复测量混合模型（MMRM）结合，在遵循监管指南的前提下利用树模型捕捉非线性交互效应，解决了传统方法难以识别长期治疗反应亚组的难题。此外，*Finite mixtures of linear quantile regressions...* 从内生性角度切入纵向因果，提出利用伴随变量的有限混合分位数回归，在不依赖工具变量的前提下控制未观测异质性，为分位数处理效应的识别提供了替代路径。

在**纵向与功能数据推断**方面，工作聚焦于非参数工具的开发与应用场景的拓展。*Statistical inference for mean function...* 针对部分观测功能时间序列，利用 B 样条估计量与高斯近似技术解决了均值函数的弱收敛与推断问题，构建了同时置信带与假设检验工具。书评 *Sample Sizes for Clinical Trials* 则系统梳理了各类试验设计下的样本量确定公式，作为方法应用的工具书补充。

对于关注**因果推断**与**半参数/非参数效率**的研究者，建议优先阅读前三篇：*Causally-interpretable random-effects meta-analysis* 讨论了因果框架下的方差估计效率问题；*Subgroup identification via Interaction Tree...* 展示了非参数树方法在纵向因果中的实际应用；*Finite mixtures of linear quantile regressions...* 则提供了处理纵向数据内生性与异质性的新思路。*Statistical inference for mean function...* 一文则适合关注高维渐近理论与非参数假设检验的读者参考。

## 因果推断  *(causal_inference, 3 篇)*

### 1. [10.1093/biomtc/ujag108](https://doi.org/10.1093/biomtc/ujag108) · [arXiv](https://arxiv.org/abs/2302.03544) — Causally-interpretable random-effects meta-analysis
- **作者**: Justin M Clark, Kollin W Rott, James S Hodges, Jared D Huling
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文在因果可解释的meta分析框架下，目标是将多个随机试验估计的处理效应推广（generalizability）或迁移（transportability）到一个目标总体。现有方法假设研究间异质性完全由效应修饰因子分布差异引起，但实际中异质性还可能来自其他来源（如研究设计差异），导致方差估计偏小。本文提出一种随机效应meta分析框架，通过引入随机效应来捕获跨研究间除可观测分布差异外的额外变异性，使得因果估计的方差更准确。在估计方面，采用逆概率加权或回归外推结合随机效应的整合估计量，并开发了相应的推断方法（包括标准误和置信区间）。理论结果展示了该估计量的一致性及其在有限样本下的表现。仿真和实例分析（如抗抑郁药试验）验证了方法有效。本文对您有具体帮助：它直接关联因果推断中的generalizability/transportability问题，且将随机效应模型与因果框架结合，是您primary interest中“因果推断识别与估计”的延伸应用。
- **关键技术**: `random-effects meta-analysis`, `generalizability and transportability`, `inverse probability weighting`, `outcome regression`, `effect modifier distribution`
- **为什么对您有用**: 本文直接针对causal inference中的treatment effect generalization/transportability，与您的primary interest “causal inference”紧密衔接。您very_familiar的“estimation theory in causal inference”可直接用于评估该文估计量的渐近性质；同时，其识别假设（如positivity、no unmeasured effect modifier）可用moderately_familiar的“identification theory in causal inference”进一步检验。follow-up判断：中期可做——需在identification theory上再熟悉一些以严格审视其假设的合理性。

### 2. [10.1093/biomtc/ujag104](https://doi.org/10.1093/biomtc/ujag104) — Subgroup identification via Interaction Tree and Mixed Model for Repeated Measures with application to Alzheimer’s disease
- **作者**: Zhichen Xu, Jimin Ding, Xiaogang Su, Guoqiao Wang, Ke Xie, Yining Zhao et al.
- **期刊/来源**: Biometrics
- **机构**: Washington University in St. Louis · The University of Texas at El Paso · University of Southern California
- **分类**: vol 82 · issue 2
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文旨在纵向临床试验中识别异质性处理效应的亚组，提出将交互树（ITree）与重复测量混合模型（MMRM）相结合的方法。ITree-MMRM保留树方法捕捉非线性处理交互的灵活性，同时遵循FDA指南使用MMRM评估终点总体处理效应。方法通过Bootstrap剪枝和参数调优降低过乐观风险。模拟实验表明ITree-MMRM优于现有亚组识别方法。将该方法应用于阿尔茨海默病临床试验，识别出具有长期治疗反应的亚组。本文对您有用：纵向因果推断中亚组异质性评估是您主要兴趣中因果推断（longitudinal）的直接应用，且树方法可借助非参数统计武器快速理解。
- **关键技术**: `Interaction Tree`, `Mixed Model for Repeated Measures (MMRM)`, `Bootstrap pruning`, `subgroup identification`, `tree-based methods`, `longitudinal clinical trials`
- **为什么对您有用**: 本文连接至因果推断中异质性处理效应（HTE）的纵向设定，具体为使用树方法结合MMRM进行亚组识别。研究者可用其非常熟悉的nonparametric statistics工具（递归划分树）解构方法的偏差-方差权衡与Bootstrap剪枝原理，并用estimation theory in causal inference评估其因果识别假设是否完备。立即可做：用very_familiar的非参数统计和因果估计理论可直接复现并检验其方法稳定性。

### 3. [10.1093/biomtc/ujag095](https://doi.org/10.1093/biomtc/ujag095) — Finite mixtures of linear quantile regressions with concomitant variables: a solution to endogeneity in longitudinal data modeling
- **作者**: Marco Alfó, Maria Francesca Marino, Francesca Martella
- **期刊/来源**: Biometrics
- **机构**: Sapienza University of Rome · University of Florence
- **分类**: vol 82 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对纵向数据中随机效应与协变量相关所导致的内生性问题，提出一类有限混合线性分位数回归模型。模型通过引入伴随变量（concomitant variables），将混合分布依赖于时间恒定协变量以及时间变异性协变量的时间恒定摘要，从而在分位数框架下控制未观测的异质性并缓解内生性。作者采用EM算法进行参数估计，并在大规模模拟研究中验证了该方法在有限样本下的偏误减少与效率提升。应用部分基于老年人MMSE评分纵向数据展示了模型的实际效果。该工作为纵向数据中的因果参数（如分位数处理效应）的识别提供了一条无需工具变量或传统IV假设的替代路径。对您而言，本文所讨论的内生性处理思路可迁移至您关注的纵向因果推断中敏感性分析或负对照设定的比较。
- **关键技术**: `finite mixture quantile regression`, `concomitant variables`, `endogeneity in longitudinal data`, `random effects dependence`, `EM algorithm`
- **为什么对您有用**: 本文直接连接您的因果推断（纵向数据）兴趣，其伴随变量框架相当于一种弱识别策略，可与proximal causal inference中的negative control设定做比较。您可以利用very_familiar中的因果推断估计理论（如正交条件）来检验该方法的识别假设，或将其与您的非参数方法（如 minimise bound）的视角结合。立即可做的 follow-up 是：用您熟悉的因果推断评估工具（如DML、双稳健估计）对该方法做敏感性分析，属于中期可做，需先熟悉分位数回归与有限混合模型的理论细节（moderately_familiar之外的技术）。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1093/biomtc/ujag111](https://doi.org/10.1093/biomtc/ujag111) — Statistical inference for mean function of partially observed functional time series
- **作者**: Shuang Sun, Leheng Cai, Qirui Hu
- **期刊/来源**: Biometrics
- **机构**: University of Pennsylvania · Tsinghua University · Shanghai University of Finance and Economics
- **分类**: vol 82 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究部分观测功能时间序列均值函数的统计推断问题。在理想情形下（曲线完整记录且无噪声），建立了基于理想估计量的Skorokhod空间弱收敛性，该估计量可能含有间断点。在实际有测量误差的场景中，提出B样条估计量，并通过高斯近似技术推导其最大偏差的渐近分布。基于supremum范数下的渐近结果，构建了同时置信带、两样本检验及相关假设检验等推断工具。实现上采用乘子bootstrap逼近极限分布，并证明了bootstrap程序的一致性。数值实验验证了理论有效性，并应用于一项视觉刺激脑电图数据集，发现了多个科学事实。本文对研究者熟悉的高维渐近与非参数假设检验方向有直接参考，其高斯近似与bootstrap技术可迁移至其他相依数据推断问题。
- **关键技术**: `B-spline estimator`, `Gaussian approximation`, `multiplier bootstrap`, `supremum norm inference`, `functional time series`, `Skorokhod space`
- **为什么对您有用**: 本文聚焦于相依功能数据的均值函数推断，与研究者对假设检验和非参数统计的兴趣高度契合。研究者very_familiar中的非参数统计工具可用于分析该B样条估计量的minimax收敛速率，而moderately_familiar中的M估计理论能帮助理解其渐近分布推导。不过，Skorokhod空间弱收敛和功能时间序列的依赖结构需要额外学习，属于中期可做方向，需先在moderately_familiar的semiparametric theory上加强。

### 2. [10.1093/biomtc/ujag005](https://doi.org/10.1093/biomtc/ujag005) — Sample Sizes for Clinical Trials (second edition)
- **作者**: Frank Bretz, Robin Ristl
- **期刊/来源**: Biometrics
- **机构**: Novartis (Switzerland) · Statistics Austria · Medical University of Vienna
- **分类**: vol 82 · issue 2
- 相关性 0/10 · novelty: `survey`
- **摘要**: 本文是 Steven Julious《Sample Sizes for Clinical Trials》第二版的书评，系统介绍了临床试验样本量确定的方法体系。全书覆盖正态、二值、有序和生存结局数据，在优效性、等效性、非劣效性和生物等效性设定下，针对平行组和交叉设计给出样本量公式。第二版新增多重性、整群随机试验、试点研究和单臂试验等章节，公式推导清晰并配有真实案例和参考表格。作为方法论综述，本书不涉及新的统计理论贡献，而是整合现有样本量计算工具供实践者参考。对您而言，可作为假设检验与试验设计的教学或应用参考。
- **关键技术**: `sample size determination`, `superiority and equivalence testing`, `non-inferiority trials`, `cluster-randomized trials`, `multiplicity adjustment`
- **为什么对您有用**: 连接到 hypothesis testing 与试验设计，但属于应用导向的工具书而非理论推进。您的 very_familiar 武器库（minimax bounds、estimation theory）远超本书所需，无需额外学习即可理解全部内容。follow-up 判定：暂不可做——本书是应用手册，没有可供理论挖掘的开放问题，仅适合作为教学参考或实际合作项目中的样本量计算查阅。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

