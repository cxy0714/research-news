# Biometrics — Vol 81  Issue 1  ·  2026-07-03

- 共 18 篇 · Biometrics
- 目录核对 ⚠️ 疑似漏 20 篇（对照 OpenAlex 38 篇）：10.1093/biomtc/ujaf010、10.1093/biomtc/ujaf013、10.1093/biomtc/ujaf020、10.1093/biomtc/ujae164、10.1093/biomtc/ujae163 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

Biometrics Vol 81 Issue 1 的 18 篇论文可归纳为三条主线：因果推断（7 篇）、假设检验（2 篇）、以及半参数/非参数方法与高维/网络建模（9 篇）。因果推断是本期最集中的主题，覆盖了从异质性效应、连续暴露、数据融合到主分层和动态治疗策略的多个方向；假设检验部分聚焦于复合零假设和依赖检验的组合；其余论文则分布在 Fréchet 回归、贝叶斯图形模型、生存分析伪观测、标量-网络回归及分布式空间计算等领域。

因果推断主线中，**The subtype-free average causal effect** 针对疾病亚型异质性提出 SF-ACE estimand，采用主分层框架并开发双重稳健估计与敏感性分析，是本期对因果识别假设最深入的讨论。**Multiply robust difference-in-differences** 将 DiD 扩展到连续暴露，通过正交得分和交叉拟合实现多重稳健估计，并给出半参数效率界。**Combining experimental and observational data** 用 power likelihood 融合 RCT 与观察性数据，以 ELPD 自适应选择学习率，在偏差-方差权衡中保持覆盖。**Individualized multi-treatment response curves** 用 RBF-net 共享神经元建模多治疗组 HTE，贝叶斯框架下量化不确定性。**Weighted Q-learning** 处理非随机缺失协变量下的最优动态治疗策略，提出逆概率加权估计量。**Bayesian nonparametric trees** 用 BCF 处理连续中介变量的主分层效应。**Estimating hypothetical estimands** 以糖尿病试验案例系统比较五种因果/缺失数据方法。假设检验方面，**Large-scale composite null hypothesis testing** 提出基于观测统计量计数的方法，提升中介分析中复合零假设检验的功效；**Unified combination framework for dependent tests** 推广 P 值组合方法处理依赖检验，并指出 Cauchy 组合的局限性。

半参数/非参与高维方向中，**Feature screening for metric space-valued responses** 基于 Fréchet 回归提出 SIS 方法，适用于分布或矩阵值响应的高维筛选。**Sparse Bernoulli mixture modeling** 用 NU 数据识别长新冠亚型，结合贝叶斯稀疏先验。**Network-based matrix-on-vector regression** 通过子图提取识别结构特征对功能连接网络的影响。**Robust Bayesian graphical regression** 用随机边际变换处理非正态性下的异质性图结构。**Regularized Bayesian Dirichlet-multinomial** 整合单细胞与临床数据。**Construct interpretable functions** 提出基于 Mallows Cp 的可解释函数骨架。**Pseudo-observations for bivariate survival** 推广伪观测至双变量生存数据。**Bayesian scalar-on-network** 在黎曼切空间建模脑功能连接。**Distributed model building** 用分治-整合策略处理超高维空间数据。

与因果推断方向最贴的优先看：**The subtype-free average causal effect**（主分层与敏感性分析）、**Multiply robust difference-in-differences**（连续暴露与半参效率）、**Combining experimental and observational data**（数据融合与偏差-方差权衡）、**Weighted Q-learning**（缺失数据与动态策略）。与半参数效率/高维方向相关的：**Multiply robust difference-in-differences**（正交得分与效率界）、**Feature screening for metric space-valued responses**（Fréchet 回归与高维筛选）、**Distributed model building**（分治-整合与计算效率）。

## 因果推断  *(causal_inference, 7 篇)*

### 1. [10.1093/biomtc/ujaf016](https://doi.org/10.1093/biomtc/ujaf016) — The subtype-free average causal effect for heterogeneous disease etiology
- **作者**: A Sasson, M Wang, S Ogino, D Nevo
- **期刊/来源**: Biometrics
- **机构**: Tel Aviv University · Brigham and Women's Hospital · Harvard University · Broad Institute
- **分类**: vol 81 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对疾病亚型异质性下的因果效应估计问题，提出了一种新的因果 estimand——无亚型平均因果效应（SF-ACE），定义为在所有暴露水平下都不会患其他亚型疾病的人群中，暴露对目标亚型的因果效应。研究以吸烟对结直肠癌微卫星不稳定性（MSI）亚型的异质性效应为应用背景，采用主分层（principal stratification）框架形式化该 estimand。作者系统研究了 SF-ACE 的非参数可识别性条件，讨论了比标准主分层更细致的单调性假设，并指出这些假设不可检验且可能过强。为此，开发了放松假设的敏感性分析方法。估计方面，提出了三种估计量，包括一个双重稳健（doubly robust）估计量。最后，在两个大型队列数据上应用该方法，分析吸烟对结直肠癌 MSI 亚型的异质性因果效应。该工作为流行病学中疾病亚型异质性分析提供了新的因果推断工具，直接连接您的 primary interest 中的因果推断（identification、sensitivity analysis）和 secondary interest 中的流行病学应用。
- **关键技术**: `principal stratification`, `subtype-free average causal effect`, `doubly robust estimation`, `sensitivity analysis`, `monotonicity assumptions`
- **为什么对您有用**: 本文直接连接您的 primary interest 中的因果推断子方向——主分层框架下的 identification 和 sensitivity analysis，以及 secondary interest 中的流行病学应用（结直肠癌亚型异质性）。从技术武器库看，您对 estimation theory in causal inference 非常熟悉，可以立即用 very_familiar 的 nonparametric statistics 和 minimax bounds 工具分析其 SF-ACE 估计量的收敛速率是否最优，以及其敏感性分析方法的识别假设是否可被更弱的条件替代（立即可做）。此外，其双重稳健估计量的 influence function 结构可进一步用您 moderately_familiar 的 semiparametric theory 工具进行效率界分析（中期可做）。

### 2. [10.1093/biomtc/ujaf015](https://doi.org/10.1093/biomtc/ujaf015) — Multiply robust difference-in-differences estimation of causal effect curves for continuous exposures
- **作者**: Gary Hettinger, Youjin Lee, Nandita Mitra
- **期刊/来源**: Biometrics
- **机构**: University of Pennsylvania · Brown University
- **分类**: vol 81 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在双重差分（DiD）框架下处理连续暴露（continuous exposure）的因果效应曲线估计问题。现有方法在处理与干预状态、暴露水平和结局趋势相关的混杂变量时存在严重局限。作者提出了一类多重稳健（multiply robust）估计量，允许干预模型、暴露模型和结局模型中的一部分被错误设定，同时不对效应曲线施加参数假设。估计量基于正交得分（orthogonal score）和交叉拟合（cross-fitting）构造，实现了n^{-1/2}-收敛和渐近正态性。理论部分给出了影响函数（influence function）和半参数效率界（semiparametric efficiency bound）。模拟和一项关于营养消费税对跨境购物行为异质性效应的实证研究展示了方法的实用性。对您而言，本文是连续暴露DiD中多重稳健估计的清晰范例，直接连接到您的因果推断（identification, estimation）和半参数效率理论兴趣。
- **关键技术**: `multiply robust estimation`, `difference-in-differences`, `continuous exposure`, `orthogonal score`, `cross-fitting`, `influence function`
- **为什么对您有用**: 本文直接对应您的primary interest中的因果推断（DiD设计下的连续暴露效应曲线）和效率理论（多重稳健估计量的影响函数与半参数效率界）。您的very_familiar武器（非参数统计、因果推断中的估计理论）可直接用于理解其正交得分构造和交叉拟合机制；moderately_familiar中的半参数理论可进一步验证其效率界是否紧。中期可做：若想将多重稳健思想推广到proximal CI或纵向设定，需先在HOIF（Higher-Order Influence Functions）上长肌肉。

### 3. [10.1093/biomtc/ujaf008](https://doi.org/10.1093/biomtc/ujaf008) — Combining experimental and observational data through a power likelihood
- **作者**: Xi Lin, Jens Magelund Tarp, Robin J Evans
- **期刊/来源**: Biometrics
- **机构**: University of Oxford · Novo Nordisk (United Kingdom)
- **分类**: vol 81 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文提出一种 power likelihood 方法，将随机对照试验（RCT）与观察性数据融合，以提升处理效应估计的效率。核心设定是：RCT 提供无偏但低效的估计，观察性数据样本量大但可能受未观测混杂偏倚。方法通过引入一个学习率参数（power parameter）来调控观察性数据在似然中的权重，从而在偏差与方差之间取得平衡。关键机制是：使用期望对数预测密度（ELPD）作为数据自适应选择学习率的标准，该标准可通过交叉验证或信息准则近似。理论部分证明了在正确指定学习率时，估计量具有相合性和渐近正态性，且覆盖率达到名义水平。模拟实验显示该方法在保持覆盖率的条件下显著提升统计功效。真实数据应用将 PIONEER 6 临床试验与美国健康索赔数据融合，验证了方法的实用性。对您而言，该工作直接关联因果推断中数据融合（data fusion）这一子方向，其 power likelihood 框架可与您熟悉的 semiparametric efficiency theory 结合，用于推导融合估计量的效率界。
- **关键技术**: `power likelihood`, `data fusion`, `expected log predictive density (ELPD)`, `learning rate selection`, `RCT augmentation`
- **为什么对您有用**: 本文属于因果推断中数据融合（data fusion）方向，直接连接您的 primary interest。您可以用 very_familiar 的 semiparametric efficiency theory 工具，推导该 power likelihood 估计量的效率界，并与现有融合方法（如 Bayesian 方法、逆概率加权）做比较。中期可做：若需将方法推广到更复杂的识别设定（如 proximal causal inference），需先在 moderately_familiar 的 identification theory 上长肌肉。

### 4. [10.1093/biomtc/ujaf019](https://doi.org/10.1093/biomtc/ujaf019) — Individualized multi-treatment response curves estimation using RBF-net with shared neurons
- **作者**: Peter Chang, Arkaprava Roy
- **期刊/来源**: Biometrics
- **机构**: University of Florida
- **分类**: vol 81 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究多治疗组异质性处理效应（HTE）的估计问题，目标是在给定协变量下估计不同治疗方案的个体化响应曲线。方法上，提出一种基于径向基函数网络（RBF-net）的非参数模型，通过共享隐藏神经元来刻画不同治疗结果之间的共性结构。估计与推断在贝叶斯框架下进行，利用阈值化最佳线性投影（thresholded best linear projections）实现，并通过高效的MCMC算法完成后验采样，同时量化不确定性。模拟实验验证了方法的数值性能。在MIMIC数据集上的应用分析了不同治疗策略对脓毒症患者ICU住院时长和12小时SOFA评分的影响。该工作对您可能有用：它涉及多治疗组因果推断中的非参数建模与不确定性量化，与您primary interest中的因果推断（尤其是异质性处理效应）直接相关。
- **关键技术**: `radial basis function network`, `shared hidden neurons`, `thresholded best linear projections`, `Bayesian MCMC`, `heterogeneous treatment effect`
- **为什么对您有用**: 本文直接关联您primary interest中的因果推断（多治疗组异质性处理效应估计）。技术层面，其非参数RBF-net建模与贝叶斯推断框架，您可以用very_familiar的非参数统计和因果推断估计理论来审视其模型假设与收敛性质。中期可做：若想将共享神经元结构推广到更一般的非参数模型或与double ML结合，需先在moderately_familiar的semiparametric theory上加强。

### 5. [10.1093/biomtc/ujae161](https://doi.org/10.1093/biomtc/ujae161) — Weighted Q-learning for optimal dynamic treatment regimes with nonignorable missing covariates
- **作者**: Jian Sun, Bo Fu, Li Su
- **期刊/来源**: Biometrics
- **机构**: Fudan University · University of Cambridge · MRC Biostatistics Unit
- **分类**: vol 81 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究在动态治疗策略（DTR）框架下，当协变量存在非随机缺失（nonignorable missing）时，如何估计最优治疗规则。目标是最优策略的Q函数，关键挑战在于后向归纳中早期阶段的伪结局（pseudo-outcome）因晚期协变量缺失而同样非随机缺失，即使纵向结局完全观测。作者提出两种加权Q-learning方法：通过估计方程构造逆概率权重，利用非应答工具变量（nonresponse instrumental variables）或敏感性分析来识别缺失机制。理论部分推导了加权Q-learning估计量的渐近性质（n^{-1/2}-CAN），并给出影响函数形式。模拟和MIMIC-III数据库的脓毒症液体管理实例验证了方法在有限样本下的表现。对您而言，本文是因果推断中缺失数据与DTR交叉的典型应用，其工具变量识别策略可与您的proximal CI知识对接，且加权估计的渐近理论可直接用您的semiparametric efficiency框架审视。
- **关键技术**: `weighted Q-learning`, `inverse probability weighting`, `nonignorable missing covariates`, `nonresponse instrumental variables`, `dynamic treatment regimes`, `estimating equations`
- **为什么对您有用**: 本文连接您的primary interest中causal inference的纵向DTR和缺失数据子方向。技术武器库中'identification theory in causal inference'（moderately_familiar）可直接用于理解其工具变量假设的合理性，而'estimation theory in causal inference'（very_familiar）可评估其加权估计的渐近效率。中期可做：若想将proximal CI的negative control思路引入DTR缺失数据，需先在moderately_familiar的identification theory上加强（具体是理解nonresponse IV与proximal IV的异同）。

### 6. [10.1093/biomtc/ujae167](https://doi.org/10.1093/biomtc/ujae167) — Estimating hypothetical estimands with causal inference and missing data estimators in a diabetes trial case study
- **作者**: Camila Olarte Parra, Rhian M Daniel, David Wright, Jonathan W Bartlett
- **期刊/来源**: Biometrics
- **机构**: Karolinska Institutet · Cardiff University · AstraZeneca (United Kingdom) · University of London · London School of Hygiene & Tropical Medicine
- **分类**: vol 81 · issue 1
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文以一项2型糖尿病临床试验为案例，系统展示了如何用因果推断和缺失数据处理方法估计ICH E9附录中定义的“假设策略”下的治疗效应。目标 estimand 是随机化治疗在假设无救援治疗和无停药情况下的效应，属于典型的 hypothetical estimand。作者实现了五种估计方法：混合模型重复测量（MMRM）、多重插补（MI）、逆概率加权（IPTW）、G-formula 和 G-estimation，并详细说明了每种方法的识别假设和R包实现细节。结果发现各估计量给出的点估计和标准误大致相似。文章还讨论了选择估计方法时的实际考量，包括计算时间、缺失数据处理方式、是否纳入事后事件数据、是否调整时变混杂、以及是否分别建模不同类型的并发事件。对您而言，这是一篇将因果推断方法（G-formula、G-estimation、IPTW）与临床试验中 estimand 框架紧密结合的应用论文，直接对应您的 primary interest 中 causal inference 的 estimation 子方向，且提供了可复现的R代码和数据集，适合作为方法学迁移的实证参考。
- **关键技术**: `G-formula`, `G-estimation`, `inverse probability of treatment weighting`, `multiple imputation`, `hypothetical estimand`, `mixed models for repeated measures`
- **为什么对您有用**: 本文直接对应您 causal inference 兴趣中的 estimation 子方向，特别是临床试验中 hypothetical estimand 的识别与估计。您的 technical arsenal 中 very_familiar 的 estimation theory in causal inference 足以理解并复现所有方法；若想进一步改进，可用 moderately_familiar 的 semiparametric theory 分析各估计量的效率损失。这是一篇应用论文，novelty 在于系统比较而非新方法，但数据集和R代码可作为您自己应用工作的模板。**中期可做**：若想将此类方法推广到更复杂的 longitudinal 设定（如时变混杂下的 G-estimation），需先在 moderately_familiar 的 identification theory in causal inference 上加强。

### 7. [10.1093/biomtc/ujaf024](https://doi.org/10.1093/biomtc/ujaf024) — Bayesian nonparametric trees for principal causal effects
- **作者**: Chanmin Kim, Corwin Zigler
- **期刊/来源**: Biometrics
- **机构**: Sungkyunkwan University · Brown University
- **分类**: vol 81 · issue 1
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对连续中介变量下的主分层分析（principal stratification）问题，提出了一种贝叶斯非参数方法。当中间变量连续时，基本主分层有无穷多个，传统的分层方法失效。作者采用贝叶斯因果森林（BCF）同时指定两个贝叶斯加性回归树（BART）模型：一个用于主分层成员关系，另一个用于条件于主分层的结果。该方法利用BCF捕捉处理效应异质性的能力，评估处理效应如何随连续主分层表面变化，并具有目标选择和正则化诱导混杂方面的优势。模拟研究验证了方法的有效性，并应用于评估电厂排放控制技术对颗粒物污染的因果效应如何随其对二氧化硫排放的影响而变化。该方法为连续中介变量下的因果效应异质性分析提供了灵活的非参数工具。
- **关键技术**: `Bayesian Causal Forests (BCF)`, `Bayesian Additive Regression Trees (BART)`, `principal stratification`, `continuous intermediate variable`, `regularization-induced confounding`
- **为什么对您有用**: 本文属于因果推断中主分层分析的应用，直接连接到您的primary interest中的causal inference（identification, estimation）。您的武器库中'nonparametric statistics'和'estimation theory in causal inference'非常熟悉，可以立即评估BART在此类问题中的理论性质（如后验收缩率）。中期可做：若想将HOIF（moderately_familiar）用于主分层估计的效率界推导，需先在该工具上积累经验。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1093/biomtc/ujaf007](https://doi.org/10.1093/biomtc/ujaf007) — Feature screening for metric space-valued responses based on Fréchet regression with its applications
- **作者**: Bing Tian, Jian Kang, Wei Zhong
- **期刊/来源**: Biometrics
- **机构**: Xiamen University · University of Michigan
- **分类**: vol 81 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对响应变量为一般度量空间值（如分布数据、矩阵值数据）的超高维预测变量筛选问题，提出了基于全局 Fréchet 回归的确定独立筛选（SIS）方法，称为 Fréchet-SIS。该方法利用边际广义残差平方和作为衡量预测变量重要性的边际效用，仅需数据对象之间的距离度量，无需显式定义响应变量的向量空间结构。理论上，在温和的正则条件下证明了 Fréchet-SIS 具有 sure screening 性质，即能以概率趋于1保留所有重要变量。模拟研究展示了良好的有限样本性能。在阿尔茨海默病神经影像研究中，该方法从582,591个候选SNP中筛选出与42个脑区体素强度分布相关的关键基因。此外，还包含一个经济学案例研究。该方法为处理复杂类型响应的高维变量选择提供了实用工具，尤其适用于非欧几里得空间数据。
- **关键技术**: `sure independence screening (SIS)`, `Fréchet regression`, `marginal general residual sum of squares`, `metric space-valued responses`, `ultrahigh-dimensional feature screening`
- **为什么对您有用**: 本文连接至非参数/半参数理论中的Fréchet回归框架，以及高维统计中的变量筛选问题。技术武器库中'非参数统计'和'高维渐近理论'可直接用于理解其sure screening性质的证明和边际效用的构造。中期可做：若想将Fréchet回归与因果推断中的倾向性得分筛选结合，需先在'半参数理论'上提升。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1093/biomtc/ujaf011](https://doi.org/10.1093/biomtc/ujaf011) — A simple and powerful method for large-scale composite null hypothesis testing with applications in mediation analysis
- **作者**: Yaowu Liu
- **期刊/来源**: Biometrics
- **机构**: Southwestern University of Finance and Economics · Statistical Research (United States)
- **分类**: vol 81 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对大规模中介分析中的复合零假设检验问题，提出了一种简单且有效的检验方法。传统 Sobel 检验和联合显著性检验在复合零假设下过于保守，导致检验功效低下。该方法的核心机制是仅需统计落在特定区域的观测检验统计量个数，无需复杂建模或估计。作者在弱假设下建立了非渐近理论，证明该方法能良好控制第一类错误并具有较高功效。大量模拟验证了理论结果，并在 DNA 甲基化数据上进行了实证分析。该方法直接适用于您在高维假设检验和因果中介分析中的实际需求，尤其是处理大规模多重比较时的功效提升问题。
- **关键技术**: `composite null hypothesis`, `large-scale multiple testing`, `non-asymptotic theory`, `mediation analysis`, `Sobel test`, `joint significance test`
- **为什么对您有用**: 本文直接关联您的 primary interest 中的 hypothesis testing 和 causal inference 的 mediation 子方向。您武器库中 very_familiar 的 nonparametric statistics 和 high-dimensional asymptotics 可以用于分析该方法的非渐近界是否紧致，或推广到更一般的复合零假设设定。**立即可做**：用 minimax bounds 验证其声称的 type I error 控制率是否最优。

### 2. [10.1093/biomtc/ujaf001](https://doi.org/10.1093/biomtc/ujaf001) — A unified combination framework for dependent tests with applications to microbiome association studies
- **作者**: Xiufan Yu, Linjun Zhang, Arun Srinivasan, Min-ge Xie, Lingzhou Xue
- **期刊/来源**: Biometrics
- **机构**: University of Notre Dame · Rutgers, The State University of New Jersey · GlaxoSmithKline (United States) · Pennsylvania State University
- **分类**: vol 81 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出一个统一的元分析框架，用于在一般设定下组合依赖的检验，并应用于微生物组关联研究。该框架基于经典P值组合方法和置信分布组合方法，但推广到处理检验间的依赖关系。作者证明广泛使用的Cauchy组合方法（称为vanilla Cauchy组合）是其特例，且框架能解决vanilla Cauchy组合分布假设被违反时的问题。数值结果表明忽略依赖会导致严重的尺寸失真。与现有方法相比，该框架能准确处理依赖并高效利用信息，构造出尺寸准确且功效增强的检验。应用上，通过组合同一数据集的多个微生物组关联检验，整合各检验在不同备择空间下的优势，实现更有效的微生物组关联发现。对您而言，本文的依赖检验组合方法可迁移到因果推断中的敏感性分析或多重中介检验场景，且其理论分析（如尺寸控制）与您熟悉的假设检验和M估计理论直接相关。
- **关键技术**: `P-value combination`, `Cauchy combination test`, `confidence distribution`, `dependent tests`, `meta-analysis`
- **为什么对您有用**: 本文属于假设检验方向，直接连接您的primary interest中的hypothesis testing。您武器库中very_familiar的非参数统计和minimax界可用于分析该组合检验的最优性，而moderately_familiar的M估计理论可用于处理检验统计量的依赖结构。中期可做：将框架推广到因果推断中的多重检验问题（如多个IV的联合检验），需先在M估计理论上进一步熟悉。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1093/biomtc/ujae159](https://doi.org/10.1093/biomtc/ujae159) — Distributed model building and recursive integration for big spatial data modeling
- **作者**: Emily C Hector, Brian J Reich, Ani Eloyan
- **期刊/来源**: Biometrics
- **机构**: North Carolina State University · Brown University
- **分类**: vol 81 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对神经影像学中超高维似然的高斯过程模型参数估计与推断，提出了一种分布式模型构建与递归整合框架。核心思路是将全局视角切换为局部数据视角，通过递归划分空间域，在分块内独立构建子模型，再通过一个计算与统计高效的整合过程同时纳入空间分辨率内部及之间的依赖性。理论部分分析了该分布式方法的统计与计算性质，包括估计一致性和计算复杂度。模拟实验验证了方法的有限样本表现。实际应用部分使用自闭症脑影像数据交换（ABIDE）数据集，提取了与自闭症谱系障碍相关的新空间模式。该方法对您可能有用：它展示了在超高维空间数据场景下如何通过分治-整合策略平衡计算可行性与统计效率，这与您在高维统计和统计计算方面的兴趣直接相关，尤其是分布式计算框架的设计思路可迁移至您熟悉的因果推断或高维推断中的大规模数据处理问题。
- **关键技术**: `distributed model building`, `recursive integration`, `Gaussian process`, `spatial partitioning`, `ultra-high-dimensional likelihood`
- **为什么对您有用**: 本文连接您在高维统计和统计计算方面的兴趣，特别是处理超高维似然时的计算-统计权衡问题。您的技术武器库中'非参数统计'和'高维渐近理论'可直接用于评估其分布式估计的收敛性质，而'软件开发'经验有助于理解其递归整合算法的实现细节。中期可做：若想将类似分治策略应用于因果推断中的大规模数据，需先在'半参数理论'上加强，以处理分布式估计中的影响函数整合问题。

## 流行病学  *(epidemiology, 1 篇)*

### 1. [10.1093/biomtc/ujaf021](https://doi.org/10.1093/biomtc/ujaf021) — Sparse Bernoulli mixture modeling with negative-unlabeled data: an approach to identify and characterize long COVID
- **作者**: Tingyi Cao, Harrison T Reeder, Andrea S Foulkes
- **期刊/来源**: Biometrics
- **机构**: Harvard University · Massachusetts General Hospital
- **分类**: vol 81 · issue 1
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对长新冠（long COVID）的亚型识别问题，提出了一种稀疏伯努利混合模型，专门处理“负-无标签”（negative-unlabeled, NU）数据——未感染者必然为阴性，但感染者的PASC状态未知。模型通过新颖的参数化将NU结构融入伯努利混合的似然，并引入贝叶斯稀疏先验实现特征选择，从而在识别亚型的同时筛选出最少的区分性症状。估计采用高效的EM算法，并通过网格搜索确定聚类数和稀疏度。模拟实验和RECOVER队列的真实数据分析验证了方法的有效性。该工作直接对应您流行病学应用兴趣中的“真实数据因果推断”方向，且其NU数据建模思路对proximal causal inference中negative control变量的处理有潜在借鉴。
- **关键技术**: `Bernoulli mixture model`, `negative-unlabeled data`, `sparse Bayesian prior`, `EM algorithm`, `grid search for model selection`
- **为什么对您有用**: 本文属于流行病学应用（长COVID亚型识别），直接命中您的secondary interest。其NU数据建模框架（负-无标签混合模型）与proximal causal inference中利用negative control处理未观测混杂的思路有结构相似性——您可以用very_familiar的“非参数统计”和“因果推断估计理论”来审视其识别假设是否可放松。中期可做：若想将NU混合模型与因果推断中的sensitivity analysis结合，需先在moderately_familiar的“identification theory in causal inference”上深入（如negative control的图模型条件）。

## 其他  *(other, 6 篇)*

### 1. [10.1093/biomtc/ujaf027](https://doi.org/10.1093/biomtc/ujaf027) — Evaluating the effects of high-throughput structural neuroimaging predictors on whole-brain functional connectome outcomes via network-based matrix-on-vector regression
- **作者**: Tong Lu, Yuan Zhang, Vince Lyzinski, Chuan Bi, Peter Kochunov, Elliot Hong et al.
- **期刊/来源**: Biometrics
- **机构**: University of Maryland, College Park · The Ohio State University · University of Maryland, Baltimore · Texas Health and Science University · The University of Texas Health Science Center · The University of Texas Health Science Center at Houston · Foundation for the National Institutes of Health
- **分类**: vol 81 · issue 1
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究多模态神经影像数据中结构特征（如白质微结构完整性、皮层厚度）对全脑功能连接网络的影响。作者提出了一种基于矩阵（网络）-on-向量回归模型的多层次子图提取方法（稠密二分图嵌套单分图），用于识别对功能连接子网络有系统性影响的结构特征子集，同时在大规模数据中有效控制假阳性。该方法本质上是一种高维回归与网络结构正则化的结合，通过子图结构降低参数空间维度。应用于UK Biobank 4242名参与者的数据，发现皮质脊髓束和小脑下脚的白质微结构完整性显著影响感觉运动、突显和执行功能子网络的功能连接（平均相关系数0.81，p<0.001）。本文属于应用导向的方法开发，方法学新颖性有限（主要贡献在于将现有网络回归框架适配到特定神经影像问题）。对您而言，本文涉及高维回归和网络结构分析，但与您的核心兴趣（因果推断、高维统计、U-统计量）无直接技术连接，可作为流行病学应用案例参考。
- **关键技术**: `network-on-vector regression`, `multi-level sub-graph extraction`, `dense bipartite with nested unipartite graph`, `false positive control in high dimensions`
- **为什么对您有用**: 本文属于流行病学/神经影像应用，使用高维回归方法分析结构-功能脑网络关联。您的武器库中'高维渐近理论'和'非参数统计'可帮助理解其子图提取方法的统计性质，但核心方法（网络回归、子图正则化）不在您的技术栈中。作为流行病学应用案例，本文展示了UK Biobank大规模数据的分析流程，值得作为入门读物了解该领域的数据结构和分析范式，但暂不可做——缺乏网络回归和子图选择的理论工具。

### 2. [10.1093/biomtc/ujae160](https://doi.org/10.1093/biomtc/ujae160) — Robust Bayesian graphical regression models for assessing tumor heterogeneity in proteomic networks
- **作者**: Tsung-Hung Yao, Yang Ni, Anindya Bhadra, Jian Kang, Veerabhadran Baladandayuthapani
- **期刊/来源**: Biometrics
- **机构**: University of Michigan · Texas A&M University · Purdue University West Lafayette
- **分类**: vol 81 · issue 1
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文提出了一种鲁棒贝叶斯图形回归模型（rBGR），用于估计非正态分布数据下的异质性图结构。传统图形模型通常假设同质图或正态性，这在癌症蛋白质组网络等应用中往往不成立。rBGR 通过随机边际变换处理非正态性，并利用图形回归技术构建协变量依赖的图以刻画异质性。文章提出了新的条件符号独立性概念（conditional sign independence with covariates）来刻画边依赖，并设计了高效的后验采样算法。模拟研究表明，rBGR 在非正态性数据下的边选择和协变量选择方面优于现有图形回归模型。该方法被应用于肺癌和卵巢癌的蛋白质组网络分析，揭示了与免疫细胞丰度差异相关的关键蛋白质-蛋白质相互作用。本文主要贡献在于方法学上的贝叶斯建模与计算，但未涉及因果推断、高维统计或效率理论等核心兴趣方向。
- **关键技术**: `Bayesian graphical regression`, `random marginal transformations`, `conditional sign independence`, `posterior sampling`, `heterogeneous graphical models`
- **为什么对您有用**: 本文属于生物统计应用，与您的主要兴趣（因果推断、高维统计、半参理论等）无直接交集。作为流行病学或癌症基因组学的应用阅读，它展示了如何用贝叶斯图形模型处理异质性和非正态数据，但方法学新颖性有限，且未涉及您武器库中的核心工具（如U统计量、minimax界、半参效率理论）。暂不可做：核心机器不在武器库里，缺乏贝叶斯图形模型和MCMC的深度积累。

### 3. [10.1093/biomtc/ujaf005](https://doi.org/10.1093/biomtc/ujaf005) — A regularized Bayesian Dirichlet-multinomial regression model for integrating single-cell-level omics and patient-level clinical study data
- **作者**: Yanghong Guo, Lei Yu, Lei Guo, Lin Xu, Qiwei Li
- **期刊/来源**: Biometrics
- **机构**: The University of Texas at Dallas · The University of Texas Southwestern Medical Center
- **分类**: vol 81 · issue 1
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出一个正则化贝叶斯 Dirichlet-multinomial 回归模型，用于整合单细胞 RNA 测序数据与患者层面的临床变量（如年龄、性别、生活方式）。模型通过层次树结构在不同细胞类型粒度上识别关联，并采用正则化处理高维参数。在肺纤维化、COVID-19 和非小细胞肺癌三个数据集上，模型成功发现了特定细胞类型与临床变量之间的显著关联。方法学上属于贝叶斯广义线性模型在组学数据上的应用，核心贡献在于整合分析框架而非统计理论创新。对您而言，本文属于生物统计应用方向，与您的主要兴趣（因果推断、高维统计、半参理论）无直接技术重叠，但可作为流行病学应用案例了解单细胞数据与临床变量的整合分析思路。
- **关键技术**: `Dirichlet-multinomial regression`, `Bayesian hierarchical model`, `regularization`, `single-cell RNA sequencing`
- **为什么对您有用**: 本文属于流行病学应用方向，与您的 secondary interest 中的 epidemiology 相关。但方法学上为贝叶斯回归框架，未涉及因果推断、半参效率或高维统计中的核心工具（如 influence function、minimax rate、RMT），武器库中 very_familiar 和 moderately_familiar 的工具均无直接对口。暂不可做：核心机器（贝叶斯层次模型与单细胞数据整合）不在您的武器库中，且无明确因果识别或效率理论问题可攻。

### 4. [10.1093/biomtc/ujaf014](https://doi.org/10.1093/biomtc/ujaf014) — A general, flexible, and harmonious framework to construct interpretable functions in regression analysis
- **作者**: Tianyu Zhan, Jian Kang
- **期刊/来源**: Biometrics
- **机构**: AbbVie (United States) · University of Michigan
- **分类**: vol 81 · issue 1
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出一个通用、灵活且和谐的框架，用于在回归分析中构建可解释函数，重点关注连续结局。作者首先根据用户对可解释性的期望定义了一个函数骨架（functional skeleton），然后基于Mallows的Cp统计量提出新的模型选择准则，以平衡近似精度、泛化能力和可解释性。该方法应用于自适应临床试验设计的样本量公式推导，以及贝叶斯Go/No-Go范式的操作特征解释，展示了使用有意义中间变量的优势。还通过Fisher精确检验的例子扩展到分类结局，并在NHANES真实数据分析中探究实验室测量指标间的关系。文章讨论了方法的若干扩展。整体上，本文更偏向应用导向的方法论框架，而非提出新的统计理论或效率界。
- **关键技术**: `Mallows's Cp`, `functional skeleton`, `model selection criterion`, `interpretable regression`
- **为什么对您有用**: 本文属于统计建模与可解释性的一般方法论，与您的主要兴趣（因果推断、高维统计、效率理论等）没有直接技术重叠。它不涉及您武器库中的具体工具（如U统计量、半参效率界、随机矩阵理论），因此暂不可做。如果您对可解释回归在流行病学或临床试验中的应用感兴趣，可作为入门阅读，但方法学新颖性有限。

### 5. [10.1093/biomtc/ujaf006](https://doi.org/10.1093/biomtc/ujaf006) — Pseudo-observations for bivariate survival data
- **作者**: Yael Travis-Lumer, Micha Mandel, Rebecca A Betensky
- **期刊/来源**: Biometrics
- **机构**: Hebrew University of Jerusalem · New York University
- **分类**: vol 81 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文提出将伪观测方法推广至双变量生存数据，以估计协变量对双变量失效时间联合分布的影响。在右删失下，先估计联合生存函数（采用Lin-Ying或Dabrowska非参数估计量），再基于此定义伪观测值，并将其作为响应变量拟合广义线性模型。证明了两种估计量下回归估计的相合性和渐近正态性。该方法可估计固定双变量时间点的联合生存概率，或同时多个时间点的联合生存概率，进而得到协变量调整的条件生存概率。通过模拟和两个真实数据集验证了方法的有效性。对您而言，本文属于生存分析领域的方法学扩展，与您的主要兴趣（因果推断、半参理论）关联较弱，但伪观测方法在纵向因果推断中可能有潜在应用。
- **关键技术**: `Pseudo-observations`, `Bivariate survival function`, `Dabrowska estimator`, `Lin-Ying estimator`, `Generalized linear model`, `Right censoring`
- **为什么对您有用**: 本文属于生存分析方法学，与您的主要兴趣（因果推断、高维统计、U统计量）直接关联较弱。伪观测方法在纵向因果推断中可能有应用，但本文聚焦于双变量生存数据的回归，而非因果识别或效率理论。武器库中的非参统计和M估计理论可帮助理解其渐近性质，但核心问题不直接对应您的技术强项。暂不可做——核心机器（双变量生存数据的伪观测框架）不在武器库中，且与您当前研究方向距离较远。

### 6. [10.1093/biomtc/ujaf023](https://doi.org/10.1093/biomtc/ujaf023) — Bayesian scalar-on-network regression with applications to brain functional connectivity
- **作者**: Xiaomeng Ju, Hyung G Park, Thaddeus Tarpey
- **期刊/来源**: Biometrics
- **机构**: New York University
- **分类**: vol 81 · issue 1
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文提出一种贝叶斯标量-网络回归模型，将标量结果与脑功能连接（以对称正定矩阵表示）关联起来。与直接向量化矩阵预测变量、忽略其几何结构的常见方法不同，该方法通过切空间建模尊重SPD矩阵的黎曼几何。在切空间中进行降维，将得到的低维表示与响应变量关联。降维矩阵以监督方式学习，并在Stiefel流形上施加稀疏诱导先验以防止过拟合。该方法产生一个简约的回归模型，允许对所有模型参数进行不确定性量化，并识别预测结果的关键脑区。通过模拟和人类连接组项目数据预测图片词汇得分的案例研究展示了性能。
- **关键技术**: `Bayesian regression`, `Riemannian geometry of SPD matrices`, `tangent space modeling`, `Stiefel manifold`, `sparsity-inducing prior`
- **为什么对您有用**: 本文属于生物统计应用，与您的主要兴趣（因果推断、高维统计等）无直接方法学关联。但作为流行病学/神经影像学应用，其处理矩阵值预测变量的几何感知方法（切空间建模、Stiefel流形先验）对您可能有一定参考价值，尤其是当您未来涉及脑连接数据或类似结构化预测变量的因果推断问题时。本文是应用导向，方法学新颖性有限（novelty_flag: application），可作为入门读物了解该领域的数据结构（SPD矩阵）和常见分析框架。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

