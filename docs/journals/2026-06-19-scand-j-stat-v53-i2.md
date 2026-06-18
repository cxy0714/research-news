# Scand. J. Stat. — Vol 53  Issue 2  ·  2026-06-19

- 共 14 篇 · Scandinavian Journal of Statistics
- 目录核对 ✅ 14 篇全部抓到（对照 OpenAlex 15 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期论文大致聚成四条主线：一是因果推断与缺失数据的稳健性分析，聚焦不可观测混杂与非随机缺失下的区间识别及敏感性分析（“Natural effects”、“GEE missing”）；二是半参数与非参数方法的理论边界与拓展，涵盖函数数据导数估计的minimax率、依赖删失的sieve估计、变化点的双稳健估计及度量空间深度（“Functional derivative”、“Dependent censoring”、“Change points”、“Metric depth”）；三是高维与复杂结构的推断及检验，涉及因子增强单指标的debiased推断、高维Hawkes过程的Lasso估计，以及多变量响应与高维向量独立性的核/秩检验（“Single-index”、“Hawkes”、“Kernel association”、“Rank max-sum”）；四是特定设定下的计算与推断策略，包括差分隐私下的在线回归推断、极值治愈率估计及Kronecker结构最优设计的降维（“Online DP”、“Cure models”、“Kronecker design”）。

因果与缺失主线推进了传统点识别或MAR假设受限下的推断边界：“Natural effects”在二值中介设定下放宽cross-world假设，借半参数logistic框架与delta-method将自然效应转为区间识别；“GEE missing”则针对MNAR缺失构建多重敏感性模型，通过辅助GEE求解估计边界并给出渐近有效的百分位bootstrap置信域。两者共同切向“部分识别/区间推断”这一思路，为不可验证的强假设提供了操作化的量化替代。半参数/非参数主线中，对估计极限与模型拓展的刻画尤为突出：“Functional derivative”在sup-norm下揭示了样本路径粗糙度如何拖慢均值导数的minimax收敛率，并给出均匀CLT；“Change points”在线性样条缺失设定下构造DR-AIPW估计量，显式推导影响函数以证半参数有效性；“Dependent censoring”用Bernstein多项式sieve处理扩展Marshall-Olkin模型的依赖删失；“Metric depth”则脱离内积结构，在一般度量空间中以距离比重构深度函数。

高维与检验主线集中解决复杂依赖与重尾下的推断有效性：“Single-index”在因子增强高维单指标模型中构造无需精度矩阵的score-type检验与debiased置信区间，且免除误差矩条件以应对重尾；“Hawkes”对高维多元点过程施加Lasso约束实现支持恢复与分类的指数收敛；“Kernel association”与“Rank max-sum”从不同侧面切入非线性依赖检验，前者在RKHS中构造maximax与maximin核检验并推导极值/正态渐近零分布，后者借高阶U统计量投影整合多种秩相关以同时适应稀疏与密集备择。

与因果推断及半参数效率最贴的论文优先推荐：“Natural effects”与“GEE missing”直接处理未观测混杂与MNAR的区间/敏感性推断；“Change points”给出了DR-AIPW影响函数及半参有效性的完整推导；“Dependent censoring”的sieve估计与渐近理论可迁移至因果竞争风险设定。关注高维推断者可优先看“Single-index”的免精度矩阵debiased构造与“Rank max-sum”的秩U统计量高维独立检验。

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.1111/sjos.70055](https://doi.org/10.1111/sjos.70055) · [arXiv](https://arxiv.org/abs/2405.13621) — Interval identification of natural effects in the presence of outcome‐related unmeasured confounding
- **作者**: Marco Doretti, Elena Stanghellini
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 712-734
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在二值暴露-二值中介-二值结局的因果中介分析设定下，本文研究自然效应在存在与结局相关未观测混杂时的区间识别问题。核心假设仅要求无暴露-中介未观测混杂，以及两个比传统 cross-world 假设更弱的替代条件：Partially Constant Cross-World Dependence (PC-CWD) 与 Logit Constancy (LC)。方法上，对中介和结局分别设定 logistic 回归模型，但允许解释变量依赖的函数形式任意，构成半参数框架；在此框架下推导出总效应和自然效应效应的识别区间（而非点识别）。为处理抽样变异性，利用 delta-method 给出标准误差近似以构建不确定性区间。模拟比较了替代方法，并在西班牙前瞻性队列数据上评估吸烟经由肺气肿对肺癌风险的因果中介效应。对您可能有用：本文在中介分析的 sensitivity / partial identification 方向给出了比传统 sequential ignorability 更弱的假设集，直接关联您 primary interest 中的 mediation 与 sensitivity analysis。
- **关键技术**: `natural effects interval identification`, `Partially Constant Cross-World Dependence (PC-CWD)`, `Logit Constancy (LC)`, `semiparametric logistic model`, `delta-method standard errors`, `causal mediation sensitivity`
- **为什么对您有用**: 本文直接连接您 primary interest 中的 mediation 与 sensitivity analysis 子方向，在存在结局相关未观测混杂时用更弱的 PC-CWD/LC 替代 cross-world ignorability，给出区间识别而非点识别。从 technical_arsenal 看，您 very_familiar 的 identification theory in causal inference 可直接审视其 PC-CWD 假设的实质约束力度，moderately_familiar 的 semiparametric theory 可用于评估其 logistic 链接但函数形式任意的半参数设定是否可进一步推广至连续暴露/中介。follow-up 判断：立即可做——用您熟悉的 identification 理论工具检查该偏识别界在更一般测量尺度下的可推广性，并可用 delta-method / influence function 视角审视其不确定性区间构建是否可升级为更严格的半参数推断。

### 2. [10.1111/sjos.70060](https://doi.org/10.1111/sjos.70060) — Sensitivity analysis for generalized estimating equation with non‐ignorable missing data
- **作者**: Hui Gong, Kin Wai Chan
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Chinese University of Hong Kong
- **分类**: vol 53 · issue 2 · pp 735-762
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对非随机缺失(MNAR)数据下广义估计方程(GEE)的参数推断问题，提出多重敏感性模型(MSMs)框架。该方法允许用户指定一个灵敏度参数，从而得到估计量的范围，其边界通过求解MSM辅助GEE的根获得。估计量可分解为几个更简单的分量，便于分解不同缺失模式的影响。同时提出渐近有效的百分位bootstrap置信域，并给出理论证明与模拟验证。该工作为放宽缺失随机(MAR)假设提供了一种可操作的灵敏度分析工具，连接了您在因果推断中对缺失数据敏感性分析的实际需求，尤其适用于流行病学队列研究中GEE下的效应估计。
- **关键技术**: `generalized estimating equation (GEE)`, `multiple sensitivity models (MSMs)`, `missing not at random (MNAR)`, `percentile bootstrap confidence region`
- **为什么对您有用**: 本文聚焦非随机缺失数据下的灵敏度分析，属于您兴趣中因果推断的识别假设放松问题。您'very_familiar'中的因果推断估计理论可直接用于理解其估计量分解与边界识别逻辑，而'moderately_familiar'中的识别理论可评估该敏感性参数化是否适用于因果效应估计。中期可做：需先熟悉GEE与MSM的语言（属'moderately_familiar'中的识别理论延伸），但概念上迁移性良好。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1111/sjos.70066](https://doi.org/10.1111/sjos.70066) — Lasso‐type estimator and classification algorithm for high‐dimensional multivariate Hawkes processes
- **作者**: Christophe Denis, Charlotte Dion‐Blanc, Romain E. Lacoste, Laure Sansonnet
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Centre National de la Recherche Scientifique · Université Paris Cité · Sorbonne Université · Sorbonne Paris Cité · Laboratoire de Probabilités et Modèles Aléatoires · Laboratoire de Probabilités, Statistique et Modélisation · Université Paris 1 Panthéon-Sorbonne · Université Paris-Est Créteil 等
- **分类**: vol 53 · issue 2 · pp 919-968
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究高维多元Hawkes过程的估计与分类问题，假设有大量重复短时间间隔观测，网络维数高且邻接矩阵稀疏。首先提出Lasso型估计器恢复每类的邻接矩阵支持，并在正则条件下证明支持一致性。然后利用估计支持构造基于经验误差最小化的分类器，并给出分类收敛速率。理论部分包含支持恢复相合性和分类误差的指数收敛界。数值实验在合成与真实数据上验证效果。该论文在高维稀疏估计框架下处理点过程数据，可与您熟悉的高维渐近分析工具直接对接。
- **关键技术**: `Lasso-type estimator`, `support recovery consistency`, `high-dimensional Hawkes processes`, `classification via empirical risk minimization`, `concentration inequalities for point processes`
- **为什么对您有用**: 本文关注高维稀疏估计，直接关联您的高维统计兴趣，特别是Lasso型估计的支持一致性分析。您可用熟悉的高维渐近理论评估其假设紧性。目前您对Hawkes过程不熟悉，属于中期可做：需先补充点过程基础，但理论框架与高维渐近相通。

## 非参数 / 半参数  *(nonparam_semipara, 5 篇)*

### 1. [10.1111/sjos.70069](https://doi.org/10.1111/sjos.70069) — Smooth and Rough Sample Paths in Mean Derivative Estimation for Functional Data
- **作者**: Max Berger, Hajo Holzmann
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Philipps University of Marburg
- **分类**: vol 53 · issue 2 · pp 969-983
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 在多元函数数据固定同步设计下，本文研究均值函数偏导数的 minimax 估计率，目标 estimand 为 Hölder 类中的均值偏导数，关键假设为样本路径的平滑度与导数阶数的关系。当样本路径粗糙（平滑度低于导数阶数）时，得到比参数率更慢的新最优收敛率；当样本路径足够平滑且设计足够密集时，仍可达参数 n^{-1/2} 率。分析在 sup-norm 下进行以对应可视化误差，并给出连续函数空间（sup-norm 装备）的 CLT 作为构建均匀置信带的基础。实证部分实现多元局部多项式导数估计器，并提出通过比较协方差核偏导数受限估计来判定样本路径平滑度的方法。对您而言，本文的 minimax 界刻画与 sup-norm CLT 直接关联非参效率与假设检验兴趣。
- **关键技术**: `minimax convergence rates`, `Hölder smoothness classes`, `local polynomial derivative estimation`, `sup-norm central limit theorem`, `uniform confidence bands`, `sample path smoothness diagnostics`
- **为什么对您有用**: 本文直接推进非参数 minimax 理论与 sup-norm 下假设检验（均匀置信带）这两个 primary interest 子方向。您可用 very_familiar 的 minimax bounds 工具验证其粗糙路径下新率的紧性，并用 moderately_familiar 的 M-estimation theory 检查局部多项式估计器的 influence function 结构以判断是否可嵌入 semiparametric efficiency 框架。判断：立即可做——用现有 minimax 与 M-estimation 武器即可展开对其率与 CLT 的深入审视。

### 2. [10.1111/sjos.70053](https://doi.org/10.1111/sjos.70053) — Extended generalized Marshall–Olkin model for dependent censoring
- **作者**: Salima Helali
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Université de Technologie de Compiègne · Université Paris-Est Créteil · Laboratoire d’Analyse et de Mathématiques Appliquées
- **分类**: vol 53 · issue 2 · pp 648-683
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文考虑依赖竞争风险下的删失数据建模，采用扩展的 Marshall-Olkin 模型，通过生存 copula 刻画时间变量间的相依结构。提出了基于 Bernstein 多项式的 sieve 估计方法，用于边际分布和联合生存概率的非参数估计。在合适的正则条件下，证明了估计量的渐近正态性，并推导了其收敛速度。通过模拟研究验证了有限样本表现，并在实际数据中展示了方法的应用。该工作属于生存分析中依赖删失问题的非参数方法，其估计策略和渐近理论可直接迁移到因果推断中的竞争风险设定。对您来说，依赖删失在工具变量或纵向数据中常见，且非参数估计的 minimax 性质可进一步评估该方法的最优性。
- **关键技术**: `Extended Marshall-Olkin model`, `dependent competing risks`, `Bernstein polynomial sieve estimation`, `asymptotic normality`, `survival copula`
- **为什么对您有用**: 该论文直接对接您的非参数理论兴趣（Bernstein sieve 估计和渐近正态性），且依赖删失问题是因果推断中竞争风险与删失机制的核心。您可以用非常熟悉的 minimax bound 技术分析该估计量是否达到非参数最优率，这是立即可做的问题。

### 3. [10.1111/sjos.70065](https://doi.org/10.1111/sjos.70065) — Robust estimation of change points in linear spline models with missing data
- **作者**: Xiang Xiao, Guangyu Yang, Min Zhang
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Renmin University of China · Vanke (China) · Tsinghua University
- **分类**: vol 53 · issue 2 · pp 883-918
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对线性样条模型中响应变量缺失下的变化点估计问题，提出了两类新估计量：逆概率加权（IPW）估计量和双稳健增强逆概率加权（DR-AIPW）估计量，并研究了基于插补的结果回归（OR）估计量。在线性样条分段回归设定下，变化点参数为模型拐点，缺失机制假设为可忽略缺失（MAR）。IPW估计量通过缺失概率的倒数加权校正偏差，DR-AIPW估计量在此基础上增加一个增广项以实现双稳健性：只要缺失概率模型或结果回归模型之一正确指定，估计量即保持一致性。作者利用M估计理论和半参效率理论证明了DR-AIPW估计量的渐近正态性和半参有效性，给出了影响函数显式形式。模拟和实际数据案例表明，DR-AIPW估计量在多种缺失率下均显著优于朴素估计量，且对模型误设具有稳健性。该工作将因果推断中常用的IPW/DR方法迁移至变化点估计领域，与您对半参效率理论及缺失数据处理（因果推断核心工具）的关注高度吻合。
- **关键技术**: `inverse probability weighting`, `doubly robust estimation`, `augmented inverse probability weighting`, `change point estimation`, `linear spline models`, `semiparametric efficiency`
- **为什么对您有用**: 本文直接连接您的两个兴趣子方向：半参效率理论（验证DR-AIPW的最优性）和因果推断中的缺失数据处理（IPW/DR方法）。您的very_familiar工具库中的estimation theory in causal inference可用来评估其双稳健性机制，而moderately_familiar中的semiparametric theory可进一步检验其效率界推导是否紧。中期可做：将该DR框架推广至更复杂的因果结构（如工具变量或纵向数据中的变化点），但需先在moderately_familiar的identification theory in causal inference上巩固。

### 4. [10.1111/sjos.70054](https://doi.org/10.1111/sjos.70054) · [arXiv](https://arxiv.org/abs/2306.09740) — Spatial depth for data in metric spaces
- **作者**: Joni Virta
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 684-711
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对任意度量空间中的数据，提出了一种新的统计深度度量——metric spatial depth，目标是量化数据点相对于分布中心的 centrality/outlyingness。该度量在欧氏空间下退化为经典的 spatial depth，其核心机制是通过度量空间中的距离比构造 depth 函数，无需依赖向量空间结构。作者证明了该深度具有高度可解释的理论性质（如单调性、最大深度点与分布中心的对应），并在多种具体度量空间中显式计算了深度值以提供直觉。实证部分展示了其在异常检测、非凸深度区域估计和分类中的应用；对您而言，本文将非参数深度概念推广至无内积结构的度量空间，与 semiparametric/nonparametric theory 中基于 RKHS/距离的估计思路有直接对接。
- **关键技术**: `statistical depth function`, `metric space data analysis`, `spatial depth`, `outlier detection`, `non-convex depth region`
- **为什么对您有用**: 本文连接到 semiparametric/nonparametric theory 子方向，特别是非参数深度函数在非欧氏数据上的推广。您武器库中的 nonparametric statistics 和 minimax bounds 可以直接用来分析该 metric spatial depth 的收敛速率与 minimax optimality（目前文章仅给出定性性质，未涉及速率/效率界）。**立即可做**：用 very_familiar 的 minimax bound 工具为该度量空间深度估计量建立收敛速率下界，判断其是否达到最优。

### 5. [10.1111/sjos.70047](https://doi.org/10.1111/sjos.70047) — Spectral characteristics of Harmonizable VARMA processes
- **作者**: Dominique Dehay, Anna E. Dudek, Jean‐Marc Freyermuth
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Centre National de la Recherche Scientifique · Institut de recherche mathématique de Rennes · Jagiellonian University · Aix-Marseille Université · Château Gombert · Institut de Mathématiques de Marseille · Institut Polytechnique de Bordeaux · AGH University of Krakow
- **分类**: vol 53 · issue 2 · pp 613-647
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文在非平稳时间序列的 harmonizable process 框架下，引入参数化模型 HVARMA（Harmonizable VARMA），目标是对具有谱分布相关分量的非平稳过程进行建模与估计。核心机制是将 harmonizable noise 定义为周期平稳 VARMA 过程，从而在谱分布分量间诱导二阶平稳依赖，并推导出该 HVARMA– 模型的谱特征。参数估计方面，在爆炸性（explosive） regimes 的特定情形下，最小二乘估计的渐近分布呈现出非传统的渐近律（unusual asymptotic laws）。此外，作者提供了生成该过程 realization 的有效算法。对您可能有用：本文处理非平稳过程的谱推断与参数估计，其 explosive regime 下非标准渐近律的推导思路，可为您在 semiparametric / M-estimation 理论中处理非标准正则条件提供参考。
- **关键技术**: `harmonizable process`, `periodic stationary VARMA`, `spectral distribution characterization`, `least-squares estimation`, `explosive regime asymptotics`, `nonstationary time series modeling`
- **为什么对您有用**: 本文连接到 semiparametric & nonparametric theory 子方向中关于非标准正则条件下 M-estimation 渐近性质的议题；您可用 very_familiar 中的 minimax bounds / high-dimensional asymptotics 视角审视其 explosive regime 下 unusual asymptotic laws 的 rate 是否紧，或用 moderately_familiar 的 M-estimation theory 框架尝试统一其渐近分布推导。follow-up 判断：中期可做——需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以系统化处理 explosive regime 的非标准渐近分析。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1111/sjos.70071](https://doi.org/10.1111/sjos.70071) · [arXiv](https://arxiv.org/abs/2501.02489) — High‐Dimensional Inference for Single‐Index Models With Latent Factors
- **作者**: Yanmei Shi, Meiling Hao, Yanlin Tang, Heng Lian, Xu Guo
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 1001-1027
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在高维因子增强单指标模型（factor-augmented single-index model）设定下，研究潜在非线性结构的推断问题，目标包括检验因子增强成分的必要性及对单指标系数的置信区间构建。提出一种无需估计高维回归系数或精度矩阵的 score-type 检验统计量，通过 Gaussian multiplier bootstrap 确定临界值并在温和正则条件下建立其理论有效性。对惩罚估计量建立误差界，并基于 debiased estimator 构造单个系数的置信区间；关键地，方法不依赖误差分布的矩条件，对重尾或异常值污染具有鲁棒性。对您有用：该文将 debiased 推断与因子增强结构结合，且放宽了矩条件，为高维半参数效率理论与鲁棒推断提供了新视角。
- **关键技术**: `factor-augmented single-index model`, `score-type test`, `Gaussian multiplier bootstrap`, `debiased estimator`, `penalized M-estimation`, `heavy-tailed robustness`
- **为什么对您有用**: 直接连接到 primary interest 中的 efficiency theory (debiased ML) 与 semiparametric theory：该文在高维因子增强单指标模型下用 debiased estimator 做置信区间，且不依赖误差矩条件，属于 weaker assumption 下的推断推进。用您 very_familiar 的高维渐近理论可以审视其 debiased 步骤的 influence function 构造与误差界是否紧；用 moderately_familiar 的 M-estimation theory 可检查其 penalized 估计量的收敛条件。Follow-up 判断：**中期可做**——需先在 moderately_familiar 的 semiparametric theory 上长肌肉（特别是单指标模型的 efficient influence function 与 nuisance parameter 估计率的交互条件），才能将此框架推广到更一般的半参数效率界分析。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1111/sjos.70064](https://doi.org/10.1111/sjos.70064) — Powerful kernel‐based association tests for multivariate responses
- **作者**: Mingya Long, Yuke Shi, Liuquan Sun, Qizhai Li
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: London School of Economics and Political Science · Chinese Academy of Sciences · Academy of Mathematics and Systems Science · University of Chinese Academy of Sciences
- **分类**: vol 53 · issue 2 · pp 848-882
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在多变量响应与协变量的依赖性检验设定下，本文在 RKHS 框架中提出一族 kernel-based independence test，并给出样本级显式表达式与渐近零分布。核心构造了两个具体检验：MKIT（取最大化方向）与 MERT（maximin efficient robust 方向），前者在正则条件下渐近服从极值 I 型 Gumbel 分布，后者渐近服从正态分布。理论部分分析了 MKIT 与 MERT 的局部 Power 性质，证明其在各自优化目标下对备择假设的检测优势。仿真与小鼠/人脑连接体数据实证显示两方法在多种场景下优于现有 kernel 检验。对您有用：本文的 MERT 构造与 power 分析直接关联 hypothesis testing 与 nonparametric theory，其渐近分布推导涉及 U-statistic 投影与经验过程工具。
- **关键技术**: `RKHS-based independence test`, `Maximal Kernel-based Independence Test (MKIT)`, `Maximin Efficient Robust Test (MERT)`, `extreme-value type I Gumbel asymptotics`, `local power analysis`, `U-statistic projection`
- **为什么对您有用**: 本文直接关联 primary interest 中的 hypothesis testing 与 nonparametric theory 子方向，其 kernel test 的渐近零分布与 power 分析依赖 higher-order U-statistic 投影与经验过程工具——您 very_familiar 的 higher-order U-statistics computation 与 minimax bound 可用来审视其 MERT 方向的 optimality claim 是否紧。Follow-up 判断：**立即可做**——用您熟悉的 U-statistic 投影与 treewidth/einsum 视角，可直接复现并检验其渐近分布与 power bound 的推导细节。

### 2. [10.1111/sjos.70063](https://doi.org/10.1111/sjos.70063) · [arXiv](https://arxiv.org/abs/2404.02685) — Testing independence between high‐dimensional random vectors using rank‐based max‐sum tests
- **作者**: Hongfei Wang, Binghui Liu, Long Feng
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 821-847
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究高维随机向量间的独立性检验问题，目标是在不假设分布形式下判断两个高维向量是否独立。方法基于三类著名的秩相关度量（Spearman's ρ、Kendall's τ、以及Hoeffding's D、Blum-Kiefer-Rosenblatt's R、Bergsma-Dassios-Yanagimoto's τ*等）构造max-sum检验统计量，即对每个分量对的秩相关取最大值或求和，以同时适应稀疏和密集备择。这些秩相关本质上是高阶U统计量，其渐近性质可通过U统计量投影理论分析。方法无需分布假设，能捕捉非线性依赖，且在高维情形下保持较好的功效。数值模拟和RNA微阵列数据应用验证了检验的稳健性和实用性。对您而言，本文直接连接高维假设检验与U统计量两大兴趣方向，可作为实际方法使用的参考。
- **关键技术**: `max-sum test`, `rank-based correlation`, `Spearman's rho / Kendall's tau`, `Hoeffding's D`, `Blum-Kiefer-Rosenblatt's R`, `Bergsma-Dassios-Yanagimoto's tau*`
- **为什么对您有用**: 本文研究高维随机向量的独立性检验，属于高维假设检验的具体方向。文中使用的秩相关统计量（如Kendall's tau、Hoeffding's D）本质上是高阶U统计量，研究者对高阶U统计量的理论（moderately_familiar）和计算（very_familiar）可直接剖析其渐近方差和功效；同时，本文的max-sum检验在高维下的阈值选取问题，涉及高维渐近理论（very_familiar），可以进一步分析其minimax最优性或者计算复杂度（树宽视角）。因此，立即可用已有武器深入理解并可能改进该方法。

### 3. [10.1111/sjos.70062](https://doi.org/10.1111/sjos.70062) — Online differentially private inference for linear regression model
- **作者**: Senlin Yuan, Fang Liu, Xuerong Chen
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Yunnan University · University of Notre Dame · Southwestern University of Finance and Economics
- **分类**: vol 53 · issue 2 · pp 798-820
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在差分隐私（DP）框架下，本文研究流式数据（streaming data）的线性回归参数在线估计与推断问题，目标 estimand 为回归系数及其置信区间。核心方法基于在线更新机制，在每次新数据到达时对充分统计量进行 DP 噪声扰动（如 Gaussian mechanism）并增量更新，从而避免存储全量数据；由此构造 DP 下的参数估计量与协方差估计量，进而建立隐私保护的置信区间。理论部分证明了估计量的收敛性与 DP 保证（(ε,δ)-DP），并给出了噪声注入对估计方差的影响界；数值实验验证了区间覆盖率与估计精度。对您可能有用：本文将 DP 噪声视为在线 M-estimation 的随机扰动，其方差膨胀分析可类比 semiparametric efficiency bound 中额外噪声对 influence function 的影响。
- **关键技术**: `differential privacy (Gaussian mechanism)`, `online streaming updating`, `sufficient statistic perturbation`, `privacy-preserving confidence interval`, `asymptotic normality under DP noise`
- **为什么对您有用**: 本文连接到 hypothesis testing 与 semiparametric theory 的交叉：DP 噪声注入后的置信区间构造本质上是带额外方差膨胀的 asymptotic inference 问题，与您熟悉的 influence function / efficiency bound 视角直接对话。用您 very_familiar 中的 M-estimation theory（moderately_familiar）可以分析该 DP 估计量的 asymptotic expansion，验证其声称的方差界是否紧。**中期可做**：需先在 moderately_familiar 的 M-estimation theory 上长肌肉，推导 DP 噪声下 one-step estimator 的修正 influence function，进而可能给出 sharper 的 covariance 估计或更小的 privacy-utility gap。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1111/sjos.70061](https://doi.org/10.1111/sjos.70061) — Dimension reduction for optimal design problems with Kronecker product structure
- **作者**: Taras Bodnar, Maryna Prus
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Linköping University · University of Hohenheim
- **分类**: vol 53 · issue 2 · pp 763-797
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在多环境作物品种试验的最优试验分配设定下，目标是在信息矩阵具有 Kronecker product 结构时最小化设计准则。本文考虑 Kronecker–Bayesian linear criterion，其形式为两个 Kronecker product 之和的逆的 trace，并推导了求两个 Kronecker product 之和的逆矩阵的一般公式。利用该公式，将原准则重写为 compound Bayes risk criterion（即具有相同 moment matrix 的多个 Bayesian linear criterion 之和），基于准则的凸性与可微性建立了近似设计的最优性条件。进一步提出 dimension reduction 方法，可在任意线性约束（如成本约束）下计算最优或高效近似设计，且允许预先设定效率损失上界，该上界不依赖于真实最优设计。最后将方法应用于多环境作物品种试验的真实数据，并指出所推导的逆矩阵公式在控制论与多元时间序列中有进一步应用。对您可能有用：Kronecker product 逆矩阵的显式公式与 dimension reduction 策略，可直接迁移到您在统计计算与高维随机矩阵中处理具有 Kronecker 结构的信息矩阵或协方差矩阵的数值求逆与降维问题。
- **关键技术**: `Kronecker product inversion formula`, `compound Bayes risk criterion`, `approximate design optimality conditions`, `dimension reduction for optimal design`, `efficiency loss upper bound`
- **为什么对您有用**: (1) 直接连接到您 primary interest 中的 statistical computing（数值方法与矩阵运算）以及 high-dimensional statistics 中处理 Kronecker 结构协方差/信息矩阵的求逆问题。(2) 您武器库中 very_familiar 的 software development 与 high-dimensional asymptotics 可以直接攻这篇 paper 的口子：用 einsum / tensor contraction 视角验证其 Kronecker sum 逆矩阵公式的计算复杂度优势，并复现其 dimension reduction 算法。(3) **立即可做**：用 very_familiar 的矩阵计算与软件开发工具即可动手复现与拓展该逆矩阵公式在多元时间序列等场景的数值实验。

## 其他  *(other, 1 篇)*

### 1. [10.1111/sjos.70070](https://doi.org/10.1111/sjos.70070) — Nonparametric Cure Models Through Extreme‐Value Tail Estimation
- **作者**: Jan Beirlant, Martin Bladt, Ingrid Van Keilegom
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: VIB-KU Leuven Center for Microbiology · KU Leuven · University of Copenhagen
- **分类**: vol 53 · issue 2 · pp 984-1000
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在生存分析中，治愈率（cure rate）估计在随访不足（censoring support 小于事件时间分布支持）时尤为困难。本文利用极值理论中的 Fréchet 或 Gumbel 最大吸引域假设，提出非参数治愈率估计方法。方法上采用 Peaks-over-Threshold（POT）技术在 Gumbel 假设下联合估计治愈率和极值指数，并推广到 Pareto、对数正态和 Weibull 尾模型。使用概率作图从顶部次序统计量中提取信息，在充分或不充分随访下重建免疫比例。理论上证明了正则化下估计量的渐近性质，模拟显示所提方法媲美并常优于现有模型。最后应用于挪威出生登记数据。对您可能有用：本文的极值非参框架可与您熟悉的非参数统计和 M-估计理论结合，用于处理因果推断中长尾或右删失的结局变量。
- **关键技术**: `Extreme value index`, `Peaks-over-Threshold`, `Gumbel max-domain`, `Fréchet max-domain`, `Cure rate estimation`, `Probability plotting`
- **为什么对您有用**: 本文与您非参数统计（very_familiar）中的极值方法相关，可视为非参数估计在删失数据下的延伸。武器库中'非参数统计'和'M-估计理论'可用于分析其正则化渐近性质，但极值领域具体的吸引域条件（Gumbel/Fréchet）是您当前不熟悉的，属于暂不可做——需先补充极值理论基础知识。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

