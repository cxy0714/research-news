# Biometrics — Vol 82  Issue 2  ·  2026-07-03

- 共 6 篇 · Biometrics
- 目录核对 ⚠️ 疑似漏 51 篇（对照 OpenAlex 67 篇）：10.1093/biomtc/ujag107、10.1093/biomtc/ujag071、10.1093/biomtc/ujag076、10.1093/biomtc/ujag105、10.1093/biomtc/ujag057 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Biometrics》第82卷第2期的6篇论文，主题分布较为分散，但可归纳为三条主线：**因果推断与异质性处理效应**（3篇）、**函数型数据与纵向数据统计推断**（2篇）、以及**方法整合与实用工具**（1篇书评）。因果推断主线最为突出，覆盖了从meta分析外推、纵向数据内生性处理到亚组识别的不同场景；函数型数据主线则聚焦于部分观测时间序列的推断和跨来源数据整合。

在因果推断主线中，三篇论文从不同角度处理异质性和外推问题。**Causally-interpretable random-effects meta-analysis** 将随机效应引入meta分析框架，将异质性分解为可解释（effect modifier分布差异）与不可解释（研究间差异）两部分，通过加权回归和g-computation实现外推，理论贡献在于明确了treatment effect外推的识别条件。**Finite mixtures of linear quantile regressions with concomitant variables** 针对纵向数据中随机效应与协变量相关导致的内生性，提出基于有限混合分位数回归的工具变量思路，利用伴随变量实现条件外生性，计算简单且能纠正偏误。**Subgroup identification via Interaction Tree and Mixed Model for Repeated Measures** 将交互树与重复测量混合模型结合，通过递归分割捕捉非线性交互，再以MMRM进行边际推断，适用于纵向临床试验中亚组识别，Bootstrap剪枝策略降低了过拟合风险。这三篇分别对应了因果外推、纵向数据内生性、亚组发现三个子问题，方法工具上均依赖混合模型或树模型与参数推断的结合。

函数型数据主线包含两篇。**Statistical inference for mean function of partially observed functional time series** 在Skorokhod空间上建立弱收敛性，处理部分观测和测量误差，利用B样条估计和高斯逼近导出supremum范数下的同时置信带与两样本检验，bootstrap一致性得到证明，适用于脑电图等高频数据。**INTACT** 则聚焦于纵向身体活动数据的跨来源整合，通过共享特征值和特征函数建模共同信息，允许来源特定的尺度和旋转调整，本质是函数型数据分析的整合工具，不涉及因果推断。此外，**Sample Sizes for Clinical Trials** 的书评系统整理了各类试验设计的样本量计算方法，属于教学参考。

对于因果推断方向的研究者，优先关注 **Causally-interpretable random-effects meta-analysis**（外推与异质性分解）、**Finite mixtures of linear quantile regressions with concomitant variables**（纵向数据内生性处理）和 **Subgroup identification via Interaction Tree and Mixed Model for Repeated Measures**（亚组识别与纵向因果推断）。对于函数型数据与高维推断方向，**Statistical inference for mean function of partially observed functional time series** 提供了部分观测场景下的渐近理论工具。

## 因果推断  *(causal_inference, 3 篇)*

### 1. [10.1093/biomtc/ujag108](https://doi.org/10.1093/biomtc/ujag108) — Causally-interpretable random-effects meta-analysis
- **作者**: Justin M Clark, Kollin W Rott, James S Hodges, Jared D Huling
- **期刊/来源**: Biometrics
- **机构**: University of Minnesota · Oregon State University
- **分类**: vol 82 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在 causally-interpretable meta-analysis 框架下，目标是将多个随机试验的 treatment effect 外推至目标人群。现有方法假设研究间异质性仅来自 effect modifier 分布差异，但实际中异质性可能源于未测量的研究特征。作者提出一个概念框架，将异质性分解为可解释部分（由 effect modifier 分布差异导致）和不可解释部分（由研究间差异导致），并引入随机效应模型来刻画后者。估计方法采用加权回归和 g-computation 的变体，结合 bootstrap 或 delta method 进行推断。理论贡献在于明确了哪些 treatment effect 类型（如 ATE、ATT）适合 generalizability 和 transportability 技术，以及异质性对因果估计的影响。实证部分通过模拟和真实数据（如心血管试验）展示了方法在存在不可解释异质性时的表现。对您而言，本文连接了 causal inference 中的 transportability 与 meta-analysis 的随机效应框架，是您 primary interest 中“identification and estimation”在纵向/多研究场景下的延伸，且其异质性分解思路可能启发您在高维 U-statistics 中处理跨群体差异的建模。
- **关键技术**: `random-effects meta-analysis`, `generalizability and transportability`, `g-computation`, `weighted regression`, `bootstrap inference`
- **为什么对您有用**: 本文直接连接 primary interest 中的 causal inference 子方向——transportability 和 generalizability，且其随机效应框架处理研究间异质性的思路，可视为您 moderately_familiar 的 identification theory 在 meta-analysis 场景下的拓展。从武器库看，您 very_familiar 的 nonparametric statistics 和 estimation theory in causal inference 可直接用于理解其加权估计和 g-computation 步骤；中期可做的是，用您 moderately_familiar 的 semiparametric theory 检验其估计量的效率界是否最优（本文未给出 semiparametric efficiency bound，这是一个可攻的口子）。暂不可做的部分：本文未涉及高维或计算复杂性，因此无需额外工具。总体而言，这是一篇方法学论文，适合作为 causal inference 在 meta-analysis 应用中的入门阅读，值得花时间读全文以获取异质性建模的视角。

### 2. [10.1093/biomtc/ujag095](https://doi.org/10.1093/biomtc/ujag095) — Finite mixtures of linear quantile regressions with concomitant variables: a solution to endogeneity in longitudinal data modeling
- **作者**: Marco Alfó, Maria Francesca Marino, Francesca Martella
- **期刊/来源**: Biometrics
- **机构**: Sapienza University of Rome · University of Florence
- **分类**: vol 82 · issue 2
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对纵向数据中随机效应与协变量相关导致的内生性问题，提出了一种基于有限混合分位数回归的解决方案。模型假设混合分布依赖于时间恒定协变量以及时变协变量的时间恒定汇总统计量（即伴随变量），从而在分位数回归框架下处理内生性。该方法本质上是一种基于混合模型的工具变量思路，通过伴随变量实现条件外生性。模拟研究表明该方法能有效纠正内生性偏误，且计算简单。实证部分应用于老年人群简易精神状态检查（MMSE）评分的纵向数据分析。对您而言，本文展示了在纵向数据分位数回归中处理内生性的一个实用策略，与您的因果推断（纵向数据、IV）和流行病学应用兴趣直接相关。
- **关键技术**: `finite mixture quantile regression`, `concomitant variables`, `random effects endogeneity`, `longitudinal data`
- **为什么对您有用**: 本文直接关联您的因果推断兴趣中的纵向数据与工具变量子方向，提供了一个在分位数回归框架下处理内生性的具体建模策略。您的技术武器库中'identification theory in causal inference'和'estimation theory in causal inference'可以直接用于评估该方法的识别假设和估计性质。中期可做：若想将本文方法与更现代的debiased ML或正交化方法结合，需先在'semiparametric theory'上加强。

### 3. [10.1093/biomtc/ujag104](https://doi.org/10.1093/biomtc/ujag104) — Subgroup identification via Interaction Tree and Mixed Model for Repeated Measures with application to Alzheimer’s disease
- **作者**: Zhichen Xu, Jimin Ding, Xiaogang Su, Guoqiao Wang, Ke Xie, Yining Zhao et al.
- **期刊/来源**: Biometrics
- **机构**: Washington University in St. Louis · The University of Texas at El Paso · University of Southern California
- **分类**: vol 82 · issue 2
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对纵向临床试验中的异质性处理效应，提出将交互树（Interaction Tree, ITree）与重复测量混合模型（MMRM）结合的ITree-MMRM方法，用于识别对治疗有长期响应的亚组。ITree通过递归分割捕捉非线性处理-协变量交互，MMRM则遵循FDA指南对纵向终点进行边际处理效应推断。方法采用Bootstrap剪枝和调参策略以降低过拟合风险。模拟研究表明ITree-MMRM在亚组识别性能上优于现有方法。应用于阿尔茨海默病临床试验，识别出具有长期治疗反应的亚组。对您而言，该方法将树模型的可解释性与纵向因果推断的规范性结合，可作为您纵向因果推断方向的一个实用工具参考。
- **关键技术**: `Interaction Tree`, `Mixed Model for Repeated Measures`, `bootstrap pruning`, `subgroup identification`, `longitudinal clinical trial`
- **为什么对您有用**: 本文直接关联您的纵向因果推断兴趣，特别是处理效应异质性的识别问题。您武器库中'因果推断中的估计理论'和'非参数统计'可用于分析ITree的分割准则与MMRM的边际效应估计的统计性质。中期可做：若您先在'识别理论'上深入，可进一步探讨该方法在proximal causal inference框架下的扩展。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1093/biomtc/ujag111](https://doi.org/10.1093/biomtc/ujag111) — Statistical inference for mean function of partially observed functional time series
- **作者**: Shuang Sun, Leheng Cai, Qirui Hu
- **期刊/来源**: Biometrics
- **机构**: University of Pennsylvania · Tsinghua University · Shanghai University of Finance and Economics
- **分类**: vol 82 · issue 2
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对部分观测的函数型时间序列，研究均值函数的统计推断问题。在理想情形（曲线完全观测、无噪声）下，建立了 Skorokhod 空间上的弱收敛性，允许估计量存在间断点。在实际情形（数据含测量误差）中，提出了 B 样条估计量，并利用高斯逼近技术导出了其最大偏差的渐近分布。基于这些渐近结果，发展了 supremum 范数下的多种推断工具：同时置信带、两样本检验和相关假设检验。实现上采用 multiplier bootstrap 逼近极限分布，并证明了 bootstrap 程序的一致性。数值实验验证了理论结果，并将方法应用于视觉刺激实验的脑电图数据集，发现了多个科学事实。对您而言，本文的 Gaussian approximation + bootstrap 框架与您在高维假设检验和函数型数据分析方面的兴趣高度相关，其处理部分观测和测量误差的思路可迁移至您关注的纵向因果推断中的缺失数据问题。
- **关键技术**: `B-spline estimation`, `Gaussian approximation`, `multiplier bootstrap`, `supremum norm inference`, `Skorokhod space weak convergence`
- **为什么对您有用**: 本文直接连接您在高维假设检验和函数型数据分析方面的兴趣，其 Gaussian approximation 和 multiplier bootstrap 技术是您 very_familiar 的非参数统计和 minimax 界工具箱中的核心武器，可立即用于分析部分观测数据下的推断问题。中期可做：将本文的 supremum 范数推断框架与您 moderately_familiar 的 HOIF 理论结合，发展针对函数型因果效应的同时置信带。

## 其他  *(other, 2 篇)*

### 1. [10.1093/biomtc/ujag112](https://doi.org/10.1093/biomtc/ujag112) — INTACT: a method for integration of longitudinal physical activity data from multiple sources
- **作者**: Jingru Zhang, Erjia Cui, Hongzhe Li, Haochang Shou
- **期刊/来源**: Biometrics
- **机构**: Fudan University · University of Minnesota · University of Pennsylvania
- **分类**: vol 82 · issue 2
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出 INTACT 方法，用于整合来自不同设备、协议和预处理流程的纵向身体活动强度数据。核心挑战是去除设备/研究特异性效应，同时保留有意义的生物信号，并处理高分辨率时间序列中的纵向和日内相关性。INTACT 通过共享特征值和特征函数建模跨来源的共同信息，同时允许来源特定的尺度和旋转调整。方法应用于 NHANES 两波加速度计数据整合，以及 NHANES 与商用设备数据的整合，在减轻来源效应方面优于现有方法。该方法本质上是函数型数据分析的整合工具，不涉及因果推断或高维统计的核心理论。对您而言，本文属于应用统计方法，与您的主要兴趣（因果推断、高维统计等）无直接技术关联，但可作为流行病学数据整合的参考案例。
- **关键技术**: `functional data analysis`, `eigenvalue decomposition`, `data harmonization`, `accelerometry`
- **为什么对您有用**: 本文属于流行病学领域的应用方法，与您的 secondary interest 中的 epidemiology 相关，但方法学上为函数型数据整合，不涉及因果推断或高维统计。作为流行病学数据整合的入门读物，可了解设备效应去除的实际挑战，但武器库中的工具（如非参统计、U-统计量）无法直接攻入其核心机制。暂不可做——核心机器（函数型数据分析的整合框架）不在武器库中。

### 2. [10.1093/biomtc/ujag005](https://doi.org/10.1093/biomtc/ujag005) — Sample Sizes for Clinical Trials (second edition)
- **作者**: Frank Bretz, Robin Ristl
- **期刊/来源**: Biometrics
- **机构**: Novartis (Switzerland) · Statistics Austria · Medical University of Vienna
- **分类**: vol 82 · issue 2
- 相关性 1/10 · novelty: `survey`
- **摘要**: 本文是对Julious《临床试验样本量》（第二版）的书评。该书系统覆盖了正态、二分类、有序及生存结局在优效性、等效性、非劣效性和生物等效性设计下的样本量计算方法，包括平行组和交叉设计。第二版新增了多重性、整群随机试验、预试验和单臂试验等章节，并对原有内容进行了全面更新。书中提供了大量基于真实场景的实例和参考表格，并清晰解释了基本公式的理论推导。对于复杂方法（如有序数据分析），则引用了原始文献。全书强调试验目标如何影响设计选择和样本量需求。作为一本面向临床试验研究者的实用参考书，其方法论贡献在于系统整理和教学，而非提出新理论或新方法。
- **关键技术**: `sample size calculation`, `superiority/non-inferiority/equivalence designs`, `cluster-randomized trials`, `multiplicity adjustment`
- **为什么对您有用**: 本文是书评，不涉及新方法或理论，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接关联。若您未来涉足临床试验设计或流行病学应用，本书可作为实用参考，但当前武器库中的工具（如非参统计、minimax界）无需用于攻读书评内容。暂不可做：核心内容为教学参考，非研究前沿。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

