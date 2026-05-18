# Biostatistics — Vol 27  Issue 1  ·  2026-05-18

- 共 12 篇 · Biostatistics

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.1093/biostatistics/kxag004](https://doi.org/10.1093/biostatistics/kxag004) — A sensitivity analysis approach to principal stratification with a continuous longitudinal intermediate outcome: applications to a cohort stepped wedge trial
- **作者**: Lei Yang, Michael J Daniels, Fan Li
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在阶梯楔形集群随机试验（SW-CRT）设定下，本文研究具有连续型纵向中间变量的主分层因果效应（PCE）的识别与估计问题。传统主分层（PS）方法多局限于二值中间变量，本文通过利用 SW-CRT 中随时间变化的处理分配机制，引入敏感性参数对连续中间变量的不可识别部分进行校准。方法结合了纵向数据结构，在放宽假设的条件下实现了 PCE 的部分识别与点估计。实证分析基于中国男男性行为者（MSM）的 HIV 检测队列数据，将社会规范作为连续中间变量展示了所提方法的实际应用。对您有用：该工作推进了因果推断中主分层与敏感性分析在纵向连续中间变量下的方法学边界，且其流行病学队列 SW-CRT 数据对您在纵向因果与流行病学应用交叉方向的研究具有参考价值。
- **关键技术**: `principal stratification`, `sensitivity analysis`, `stepped wedge cluster randomized trials`, `principal causal effects`, `continuous intermediate variable`
- **为什么对您有用**: 直接连接您在因果推断中的 sensitivity analysis 与 longitudinal 设定，同时提供了流行病学队列 SW-CRT 数据集与应用范式，对主分层框架下连续中间变量的处理有方法学启发。

### 2. [10.1093/biostatistics/kxag001](https://doi.org/10.1093/biostatistics/kxag001) — A doubly robust framework for addressing outcome-dependent selection bias in multi-cohort EHR studies
- **作者**: Ritoban Kundu, Xu Shi, Michael Kleinsasser, Lars G Fritsche, Maxwell Salvatore, Bhramar Mukherjee
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在多队列 EHR 非概率样本中，针对结果依赖的选择偏差（outcome-dependent selection），目标是关联参数的 identification 与估计。本文提出 Joint Augmented IPW (JAIPW) 估计量，通过引入辅助得分模型（auxiliary score model）整合多队列个体数据与外部概率样本，实现双重稳健性（double robustness）。推导了 JAIPW 的渐近性质，证明其在选择模型或结果模型之一正确指定时具备相合性。模拟表明，在选择模型错定下，JAIPW 相较最优联合 IPW 方法的相对偏差和 RMSE 分别降低最高 6 倍与 5 倍。实证结合 MGI 生物库与国家概率样本估计了癌症-性别及 PRS 关联。对您有用：该文将 AIPW 扩展至多队列结果依赖选择偏差，其辅助得分构造思路可迁移至您关注的 causal inference 估计问题，并提供流行病学 EHR 数据集应用范例。
- **关键技术**: `Augmented Inverse Probability Weighting (AIPW)`, `double robustness`, `outcome-dependent selection bias`, `auxiliary score model`, `multi-cohort data integration`
- **为什么对您有用**: 直接关联您 primary interest 中的 causal inference 估计方法（AIPW 在复杂选择偏差下的扩展），同时契合 secondary interest 中流行病学（EHR 数据集、癌症关联应用）的需求，提供了处理非概率样本选择偏差的具体估计策略与数据集参考。

## 非参数 / 半参数  *(nonparam_semipara, 2 篇)*

### 1. [10.1093/biostatistics/kxag003](https://doi.org/10.1093/biostatistics/kxag003) — SAM-HC: a Bayesian nonparametric construction of hybrid control for randomized clinical trials using external data
- **作者**: Dehua Bi, Tianjian Zhou, Wei Zhong, Yuan Ji
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在随机对照临床试验中，当高质量外部数据可用或对照组招募困难时，目标是从外部数据借用信息以增强对照组，同时处理跨数据源的异质性子人群问题。核心方法是 Shared Atoms Model (SAM)，一种 Bayesian nonparametric 模型，通过 Dirichlet process 先验识别试验数据与外部数据之间的重叠与独特子人群，仅对共同子人群进行信息借用，形成 hybrid control (HC)。信息借用程度受样本量和结局相似度约束，避免过度借用导致的偏倚。模拟研究表明方法在异质性设定下稳健，特应性皮炎数据应用展示了更精确的处理效应估计。对您而言，该文提供了 Bayesian nonparametric 处理人群异质性的具体构造，可启发因果推断中 external validity / transportability 的非参数建模思路，但方法学 novelty 限于贝叶斯框架，与您关注的频率学派半参数效率理论距离较远。
- **关键技术**: `Bayesian nonparametric model`, `Shared Atoms Model`, `Dirichlet process prior`, `hybrid control construction`, `external data borrowing`, `subpopulation clustering`
- **为什么对您有用**: 与因果推断中 external validity / transportability 问题相关，Bayesian nonparametric 聚类识别共同子人群的思路可迁移至 proximal CI 或 IV 设定下处理异质性；但贝叶斯框架与您关注的 semiparametric efficiency / debiased ML 方向差异较大，收益主要在建模思路借鉴而非理论工具。

### 2. [10.1093/biostatistics/kxag006](https://doi.org/10.1093/biostatistics/kxag006) — Borrowing from historical control data in a Bayesian time-to-event model with flexible baseline hazard function
- **作者**: Darren A V Scott, Alex Lewin
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在贝叶斯动态借用历史对照数据的生存分析设定下，传统方法常对基线风险函数施加参数或分段约束以保证计算速度，本文在参数可交换性假设下研究基线风险无约束的半参数模型。提出一种基于集成平均（ensemble average）的半参数贝叶斯借用模型，允许基线风险取任意形式，并引入先验平滑后验基线风险的形状以改善估计与借用特性。针对先验-数据冲突（prior-data conflict），提出“lump-and-smear”借用先验，并基于历史与当前对数基线风险的容许差异给出了超参数选择的原则性方法。理论与模拟表明，当可交换性成立时，该半参数方法相比近似基线风险的方法提升了检验功效并降低了处理效应估计的偏差；在冲突下有效控制了I类错误膨胀。对您研究半参数理论在生存数据中的灵活建模，以及假设检验中先验-数据冲突下的I类错误控制有直接参考价值。
- **关键技术**: `Bayesian dynamic borrowing`, `semiparametric survival model`, `flexible baseline hazard`, `lump-and-smear prior`, `prior-data conflict`, `Type I error control`
- **为什么对您有用**: 连接到您的 semiparametric theory 兴趣（半参数生存模型中基线风险的灵活非参数建模）以及 hypothesis testing 兴趣（先验-数据冲突下的 I 类错误膨胀控制），同时提供了流行病学/临床试验场景的应用与 R 软件实现。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1093/biostatistics/kxag013](https://doi.org/10.1093/biostatistics/kxag013) — Statistical inference for high-dimensional generalized estimating equations
- **作者**: Lu Xia, Ali Shojaie
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在高维相关数据（如纵向组学数据）设定下，本文研究广义估计方程（GEE）中回归系数线性泛函的统计推断问题，目标是在 p 远大于 n 时实现有效的置信区间构建。作者通过构建投影估计方程得到去偏估计量，证明了该估计量在温和正则条件下具有渐近正态性（n^{-1/2}-CAN）。针对投影方向估计中的惩罚参数选择，本文提出了数据驱动的交叉验证方法，填补了现有高维 GEE 推断流程在调参上的空白。技术核心依赖高维惩罚估计与投影去偏思想，以消除正则化引入的估计偏差。模拟与 COVID-19 蛋白质组学真实数据表明，该方法在估计偏差和置信区间覆盖率上具有稳健的有限样本表现。该文将高维去偏推断从独立样本推广到相关数据，其投影估计方程的构造思路可直接迁移到您关注的 longitudinal causal inference 或高维效率理论（debiased ML）中。
- **关键技术**: `generalized estimating equations`, `projected estimating equations`, `high-dimensional debiased inference`, `asymptotic normality`, `cross-validation tuning`
- **为什么对您有用**: 直接关联您的高维统计与效率理论（debiased ML）兴趣：将高维去偏/投影推断推广至相关数据（GEE）设定，其投影估计方程构造与调参策略对处理 longitudinal 数据的高维因果推断或半参数有效估计具有直接迁移价值。

## 统计计算 / 算法  *(stat_computing, 3 篇)*

### 1. [10.1093/biostatistics/kxag010](https://doi.org/10.1093/biostatistics/kxag010) — Stochastic gradient descent estimation of generalized matrix factorization models with application to single-cell RNA sequencing data
- **作者**: Cristian Castiglione, Alexandre Segers, Lieven Clement, Davide Risso
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对单细胞RNA测序数据的高维降维问题，提出了一种基于指数散布族分布的广义矩阵分解（GMF）模型，将现有多种降维方法统一为该模型的特例。核心估计方法为自适应随机梯度下降（SGD）算法，通过随机近似与自适应步长实现了对超大规模低秩矩阵的快速求解。数值实验与真实数据分析表明，该算法在保持甚至提升矩阵重构精度与信号提取准确率的同时，显著降低了计算时间与内存消耗。方法已封装为开源R包sgdGMF，可无缝扩展至百万级细胞规模。对您在统计计算（数值方法与算法）方面的兴趣有直接参考价值，其针对大规模低秩矩阵设计的SGD优化策略与软件工程实现可迁移至其他高维统计计算场景。
- **关键技术**: `generalized matrix factorization`, `exponential dispersion family`, `adaptive stochastic gradient descent`, `low-rank model estimation`, `large-scale optimization`
- **为什么对您有用**: 直接契合您在统计计算（数值方法与算法）方面的核心兴趣，其针对大规模低秩矩阵设计的自适应SGD算法及R包实现，对处理高维数据的数值优化方法有迁移借鉴价值。

### 2. [10.1093/biostatistics/kxag007](https://doi.org/10.1093/biostatistics/kxag007) — Joint modeling of high-dimensional longitudinal data and survival using supervised low-rank tensor decomposition
- **作者**: Mohammad Samsul Alam, Rima Kaddurah-Daouk, Sheng Luo
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在高维纵向组学数据与生存结局的联合建模设定下，目标是解决复杂时间动态、特征间依赖及计算可行性问题，假设纵向过程可用低秩函数张量近似。提出一种基于监督低秩函数张量分解的联合建模框架，纵向过程由包含基线协变量监督的低秩张量表示，生存部分采用比例风险模型。估计采用基于似然的蒙特卡罗EM（MCEM）算法，实现连贯推断与个体化动态预测，通过张量低秩结构降维克服高维计算瓶颈。模拟显示在高删失和小样本下估计精度与预测性能显著优于两阶段法；在ADNI脂质组学应用中，4个成分解释了>99%的变异并识别出痴呆发病潜变量预测因子。对您而言，该文的低秩张量分解与MCEM算法设计对处理高维纵向数据的统计计算有参考价值，且ADNI数据集对流行病学应用有直接借鉴意义。
- **关键技术**: `low-rank tensor decomposition`, `Monte Carlo EM algorithm`, `joint modeling of longitudinal and survival`, `proportional hazards model`, `functional tensor approximation`, `dynamic prediction`
- **为什么对您有用**: 低秩张量分解与MCEM算法设计对您在统计计算与高维数据处理方面的兴趣有直接参考价值；同时ADNI脂质组学数据集对流行病学应用（secondary interest）具有数据集价值。

### 3. [10.1093/biostatistics/kxaf051](https://doi.org/10.1093/biostatistics/kxaf051) — Shortcomings of deep learning for distributional predictors: a note
- **作者**: Bonnie B Smith, Abhirup Datta, Brian Caffo
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 1/10 · novelty: `minor`
- **摘要**: 在生物医学高维同类型预测变量（如个体内分布）设定下，目标是学习对输入向量排列不变的映射，比较无结构深度网络与显式利用排列不变性的有序预测变量神经网络（OPNN）。无结构网络未引入不变性导致参数空间冗余，而OPNN通过显式约束简化学习任务。在neural Bayes estimation框架下，OPNN构造的点估计量精度显著优于无结构网络。模拟表明，无结构深度学习预测误差更高，而利用不变性可大幅提升估计与预测表现。对您可能有用：该文展示了在neural Bayes估计中通过显式引入排列不变性约束假设空间以提升估计效率的具体路径，直接关联您在efficiency theory与statistical computing上的兴趣。
- **关键技术**: `permutation invariance`, `neural Bayes estimation`, `ordered predictors neural network`, `unstructured deep learning`
- **为什么对您有用**: 关联您在efficiency theory与statistical computing的兴趣，展示了在neural Bayes估计中通过显式引入排列不变性约束假设空间，从而获得更精确（更高效）估计量的具体方法与实证。

## 流行病学  *(epidemiology, 3 篇)*

### 1. [10.1093/biostatistics/kxag002](https://doi.org/10.1093/biostatistics/kxag002) — Dynamic case-control sampling for rapid estimation of vaccine effectiveness against an emerging infectious disease variant
- **作者**: Taylor M Fortnam, Laura C Chambers, Alyssa Bilinski, Ewa King, Richard C Huard, Ellen Amore et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 4/10 · novelty: `application`
- **摘要**: 在公共卫生实时监测设定下，目标是估计新发传染病变异株的疫苗有效性（VE），关键假设为仅部分病例被测序且旧变异株的绝对VE已知。方法采用动态病例对照采样，将感染新变异株者作为“病例”、感染旧变异株者作为“对照”来估计相对VE。随后，将相对VE与旧变异株的已知绝对VE结合，推断新变异株的绝对VE。该估计策略本质上是 test-negative design 的扩展，处理了部分测序带来的选择偏倚，并允许随数据累积连续更新估计。在 Omicron BA.1/BA.2 数据上的实证表明，尽管样本量较小导致标准误增大，该方法估计的VE与传统方法可比。对您而言，该文提供了一个流行病学监测中应用因果推断（test-negative design 变体）的具体案例，适合关注流行病学应用因果方法的您参考其设计思路。
- **关键技术**: `dynamic case-control sampling`, `test-negative design`, `relative vaccine effectiveness`, `selection bias`, `sequential estimation`
- **为什么对您有用**: 匹配您的次要兴趣“流行病学（应用因果工作）”，展示了如何在部分测序的选择偏倚下利用 test-negative design 变体进行因果参数（VE）的动态估计，对您考虑流行病学监测数据的因果推断应用有参考价值。

### 2. [10.1093/biostatistics/kxaf052](https://doi.org/10.1093/biostatistics/kxaf052) — Risk functions with outcome measurement error
- **作者**: Jessie K Edwards, Stephen R Cole, Paul N Zivich, Benjamin Ackerman, Sonia Napravnik, Heather Henderson et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 3/10 · novelty: `minor`
- **摘要**: 在结局变量存在测量误差的设定下（如死亡登记链接不完整或错误导致的误分类与时间偏误），本文研究风险函数与生存函数的识别与估计问题，关键假设是存在内部或外部验证数据以估计灵敏度和特异度。核心方法将经典的 Rogan-Gladen 估计量推广至右删失生存数据场景，利用验证子研究中的误分类参数对风险估计进行校正，并可作为一种定量偏倚分析工具。模拟研究表明，即使验证子研究存在选择偏倚（入选者死亡风险更高），该方法仍表现良好。实证分析基于 2001–2022 年 UNC CFAR HIV 临床队列的死亡率估计，展示了死亡登记链接不完整时偏倚校正的实际效果。该方法学扩展对您在流行病学队列研究中处理结局测量误差有直接参考价值，但理论深度有限。
- **关键技术**: `Rogan-Gladen estimator`, `outcome measurement error`, `validation substudy`, `quantitative bias analysis`, `right censoring correction`
- **为什么对您有用**: 连接您在流行病学（secondary interest）中的应用因果工作：当队列研究依赖登记链接时结局误分类普遍存在，该方法提供了基于验证数据的偏倚校正框架，可直接迁移到类似 HIV 队列的因果效应估计场景。

### 3. [10.1093/biostatistics/kxag008](https://doi.org/10.1093/biostatistics/kxag008) — A flexible class of latent variable models for the analysis of antibody response data
- **作者**: Emanuele Giorgi, Jonas Wallin
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 在流行病学抗体浓度数据分析中，传统有限混合模型假设个体严格分为血清阴性和阳性两组，本文挑战此二分假设，提出连续潜变量框架，将免疫状态刻画为连续潜血清反应性。该框架兼容机制模型与回归模型，并将有限混合模型作为特例。为克服极大似然估计（MLE）的高计算成本，作者提出基于 L2 距离的估计量（minimum distance estimator）并证明其一致性。疟疾血清学案例表明，该连续潜变量模型能跨年龄段联合分析并适应传播模式变化。对您而言，该文提供了流行病学抗体数据集，其 L2 估计量的计算效率与一致性证明对统计计算与半参数估计有一定参考价值。
- **关键技术**: `latent variable model`, `L2-based estimation`, `minimum distance estimation`, `finite mixture model`, `serology data analysis`
- **为什么对您有用**: 属于流行病学（次要兴趣）应用，提供了疟疾抗体数据集；其替代 MLE 的 L2 估计量在计算效率与一致性上的探讨，对统计计算与半参数估计有参考价值。

## 其他  *(other, 1 篇)*

### 1. [10.1093/biostatistics/kxaf049](https://doi.org/10.1093/biostatistics/kxaf049) — A two-stage approach for segmenting spatial point patterns applied to multiplex imaging
- **作者**: Alvin Sheng, Brian J Reich, Ana-Maria Staicu, Santhoshi N Krishnan, Arvind Rao, Timothy L Frankel
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 本文在空间点模式框架下，针对多重成像数据的组织分割问题，提出两阶段方法：第一阶段对每张图像内细胞的空间点模式估计局部强度函数与对相关函数（pair correlation function），并通过协方差函数的谱分解对对相关函数进行降维。第二阶段将降维后的估计量输入贝叶斯层次模型进行聚类，聚类标签具有空间依赖性（如 Potts 先验），通过 MCMC 联合估计聚类分配与各聚类的空间特征并量化不确定性。模拟展示了方法的有限样本表现，实证应用于胰腺病变组织的多重免疫荧光图像分割。该方法对您主要兴趣方向的方法论重叠有限，但谱分解降维与空间依赖先验的贝叶斯计算思路可作参考。
- **关键技术**: `spatial point process`, `pair correlation function`, `spectral decomposition of covariance`, `Bayesian hierarchical clustering`, `spatially-dependent Potts prior`, `MCMC posterior sampling`
- **为什么对您有用**: 与您的主要兴趣（因果推断、高维RMT、半参数效率）重叠较少；谱分解降维与贝叶斯MCMC计算或对统计计算兴趣有边际参考价值，流行病学应用方向（肿瘤免疫组织分割）可提供空间数据集视角。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

