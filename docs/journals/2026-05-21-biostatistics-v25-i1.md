# Biostatistics — Vol 25  Issue 1  ·  2026-05-21

- 共 14 篇 · Biostatistics

## 因果推断  *(causal_inference, 3 篇)*

### 1. [10.1093/biostatistics/kxad002](https://doi.org/10.1093/biostatistics/kxad002) — Assessing the causal effects of a stochastic intervention in time series data: are heat alerts effective in preventing deaths and hospitalizations?
- **作者**: Xiao Wu, Kate R Weinberger, Gregory A Wellenius, Francesca Dominici, Danielle Braun
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 1 · pp 57-79
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在时间序列因果推断设定下，目标是评估热浪警报对健康结局的因果效应，但传统因果推断所需的 overlap 假设（较冷天发布警报的概率近零）常被违反。本文提出基于增量时变倾向得分（ItvPS）的随机干预（stochastic intervention），通过将第 t 天发布警报的条件概率乘以优势比 δ_t 来定义新的因果 estimand。理论证明该 estimand 可在弱化版的 overlap 假设下被非参数地识别和估计，并给出了估计量的方差上界。方法进一步扩展至多站点时间序列的空间 Meta 分析，模拟显示估计量在偏差和 RMSE 上表现良好。实证利用 2837 个美国县区的 Medicare 数据评估了增加警报概率对死亡和住院的因果效应。对您有用：该文将 stochastic intervention 推广至时间序列并放松了 overlap 假设，对您在 longitudinal causal inference 的 estimand 构造与流行病学应用有直接参考价值。
- **关键技术**: `stochastic intervention`, `incremental time-varying propensity score`, `overlap assumption relaxation`, `nonparametric estimation`, `spatial meta-analysis`
- **为什么对您有用**: 直接推进了 longitudinal causal inference 中的 stochastic intervention 方法，通过 ItvPS 放松了 overlap 假设，且提供了大规模流行病学（Medicare）数据集的应用范例，对您在纵向因果推断的识别策略与流行病学应用有直接借鉴意义。

### 2. [10.1093/biostatistics/kxac053](https://doi.org/10.1093/biostatistics/kxac053) — Flexible evaluation of surrogacy in platform studies
- **作者**: Michael C Sachs, Erin E Gabriel, Alessio Crippa, Michael J Daniels
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 1 · pp 220-236
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究平台试验中试验水平替代指标的评估问题，目标是在存在人群、治疗和实施异质性的设定下，利用替代指标的处理效应预测临床结局的处理效应。作者提出一种分层贝叶斯半参数模型，采用基于 Dirichlet process mixtures 的非参数先验来刻画真实效应分布。该方法无需预设替代指标与结局效应的参数化关系，能够以数据驱动的方式识别替代指标价值存在差异的聚类。模拟结果表明，该半参数方法在效应预测上优于标准的参数化分层贝叶斯方法。文章通过基于 ProBio 试验的模拟示例展示了如何识别替代指标有效与无效的亚群。对您而言，该文将 Dirichlet process mixtures 引入因果替代指标评估，其处理异质性的非参数建模思路可为半参数理论及流行病学中的因果中介/替代指标分析提供方法借鉴。
- **关键技术**: `surrogate evaluation`, `hierarchical Bayesian model`, `Dirichlet process mixtures`, `nonparametric Bayes`, `platform trials`
- **为什么对您有用**: 涉及因果推断中的替代指标评估（与中介分析紧密相关）及非参数建模，且属于流行病学/临床试验应用场景，其处理异质性的非参数贝叶斯思路对您研究半参数理论与应用因果推断有参考价值。

### 3. [10.1093/biostatistics/kxac044](https://doi.org/10.1093/biostatistics/kxac044) — Time-to-event surrogate endpoint validation using mediation analysis and meta-analytic data
- **作者**: Quentin Le Coënt, Catherine Legrand, Virginie Rondeau
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 1 · pp 98-116
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在肿瘤学 meta-analytic 设定下，目标是在替代终点与最终终点均为删失生存时间时验证替代指标的有效性。方法上，提出基于中介分析的联合随机效应模型，将治疗对最终终点的总效应分解为直接效应与经替代终点的间接效应。利用试验层面随机效应刻画多中心异质性，由模型参数导出间接效应占总效应的比例作为替代性度量。实证将该框架应用于可切除胃癌数据，验证复发时间作为总生存期替代终点的合理性。对您有用：该文为纵向/生存数据的因果中介分析提供了具体的联合建模思路，且包含流行病学肿瘤队列的应用范例，可迁移至您关注的生存数据中介效应分解。
- **关键技术**: `mediation analysis`, `surrogate endpoint validation`, `joint frailty model`, `time-to-event data`, `meta-analytic random effects`, `indirect effect proportion`
- **为什么对您有用**: 直接关联您 primary interest 中的因果推断（中介分析、纵向/生存数据），同时提供了 secondary interest 中流行病学（肿瘤临床数据）的应用范例，可借鉴其多中心删失数据的中介建模框架。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1093/biostatistics/kxac032](https://doi.org/10.1093/biostatistics/kxac032) — CoCoA: conditional correlation models with association size
- **作者**: Danni Tu, Bridget Mahony, Tyler M Moore, Maxwell A Bertolero, Aaron F Alexander-Bloch, Ruben Gur et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 1 · pp 154-170
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在控制混杂变量的设定下，本文研究两个对称变量（如速度与精度）的条件相关性如何随第三变量变化，提出基于似然的 CoCoA 框架。引入了条件相关性尺度上的效应量指标“association size”，用于量化第三变量对对称关系的影响。核心机制是通过似然推断估计条件相关，并在模拟中与基因组研究中常用的半参数估计量对比，发现似然估计量在理想设定及模型误设下均具有更低的偏差和方差。实证分析使用费城神经发育队列（PNC），发现持续注意力增强会加强复杂推理任务中的速度-精度耦合。对您有用之处：该文提供了流行病学队列中条件相关与调节效应的建模实例，以及似然与半参数方法在有限样本下的效率与稳健性对比参考。
- **关键技术**: `conditional correlation model`, `likelihood-based estimation`, `semiparametric estimator comparison`, `association size`, `confounder adjustment`
- **为什么对您有用**: 文中对比了似然估计与半参数估计在有限样本下的偏差与方差表现，触及您对 semiparametric theory 的兴趣；同时应用了费城神经发育队列（PNC）数据，为流行病学应用场景中的条件相关与混杂调整提供了可迁移的分析范式。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1093/biostatistics/kxac036](https://doi.org/10.1093/biostatistics/kxac036) — Differences in set-based tests for sparse alternatives when testing sets of outcomes compared to sets of explanatory factors in genetic association studies
- **作者**: Ryan Sun, Andy Shi, Xihong Lin
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 1 · pp 171-187
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 本文研究高维稀疏替代假设下的集合检验问题，比较了多解释变量对单一表型与 单一解释变量对多表型在 rare/weak 信号框架下 Higher Criticism 和 Berk-Jones 等检验的差异性。核心发现是变量间的相关结构在两种设定下对检验势产生截然不同的影响，这解释了文献中关于 innovated 与 generalized 类型方法优劣的冲突结论。作者推导了新的势界以量化相关结构对检测边界的影响，为具体设定下统计量的选择提供了理论依据。理论与模拟表明，多解释变量设定下 generalized 方法通常更优，而多结果设定下 innovated 方法更有利，并在肺癌 eQTL 数据中得到验证。对您有用：本文直接推进了高维稀疏假设检验理论，其关于检测边界和势界的精细推导对您在 mathematical statistics (hypothesis testing) 和 high-dimensional statistics 方面的兴趣有直接参考价值。
- **关键技术**: `Higher Criticism statistic`, `Berk-Jones statistic`, `detection boundary`, `sparse alternatives`, `power bounds`, `innovated vs generalized tests`
- **为什么对您有用**: 直接关联您的 primary interest "mathematical statistics (hypothesis testing)" 与 "high-dimensional statistics"，本文对 rare/weak 信号下检测边界与势界的精细刻画，为高维稀疏假设检验提供了新的理论工具与视角。

### 2. [10.1093/biostatistics/kxac047](https://doi.org/10.1093/biostatistics/kxac047) — Inference after latent variable estimation for single-cell RNA sequencing data
- **作者**: Anna Neufeld, Lucy L Gao, Joshua Popp, Alexis Battle, Daniela Witten
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 1 · pp 270-287
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在单细胞 RNA 测序数据分析中，研究者常先估计潜在变量（如细胞类型或伪时间），再检验基因与该潜在变量的关联；若两步使用同一数据，标准假设检验方法将无法控制第一类错误。本文提出 count splitting 框架，在 Poisson 假设下将计数数据随机分配到两个独立子集中，分别用于潜在变量估计和后续假设检验。传统的样本分割在此场景不适用，而 count splitting 利用 Poisson 分布的可加性生成独立子集，避免了 data snooping 导致的推断失效。该方法不依赖特定的潜在变量估计或推断技术，具有高度灵活性，理论上在 Poisson 模型下能严格保证第一类错误控制。模拟和真实数据（多能干细胞向心肌细胞分化）验证了其 Type 1 error 控制和检验功效。对您有用：这是 post-selection inference 在高维计数数据中的巧妙应用，直接关联您对 hypothesis testing 和 statistical computing 的兴趣，count splitting 的算法思路可迁移到其他需避免数据重用偏差的推断场景。
- **关键技术**: `post-selection inference`, `count splitting`, `Type 1 error control`, `Poisson additivity`, `latent variable estimation`, `data snooping`
- **为什么对您有用**: 直接关联您对 hypothesis testing 的核心兴趣，提供了在“先估计后检验”这一常见 data snooping 场景下保证 Type 1 error 的计算框架，其 count splitting 思路可迁移至其他高维或潜在变量模型的 selective inference 问题。

### 3. [10.1093/biostatistics/kxac040](https://doi.org/10.1093/biostatistics/kxac040) — Adaptive clinical trial designs with blinded selection of binary composite endpoints and sample size reassessment
- **作者**: Marta Bofill Roig, Guadalupe Gómez Melis, Martin Posch, Franz Koenig
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 1 · pp 237-252
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在两臂随机对照试验中，针对二元复合终点（CE）样本量计算依赖成分间相关性且常未知的问题，提出一种基于盲态期中分析的适应性试验设计。核心机制是在期中分析时，根据盲态数据估计的事件概率、相关性及效应量，在 CE 与其最重要成分间选择所需样本量更低的终点作为主要终点，并同步重新评估样本量。模拟研究表明，该设计在严格保持 I 类错误的前提下，即使初始相关性设定错误也能达到目标功效，且功效等于或优于非适应性设计。对您在假设检验（适应性设计的 I 类错误控制）和流行病学 RCT 应用方面的兴趣有参考价值，但方法学偏向传统生物统计设计，缺乏半参数或高维理论深度。
- **关键技术**: `adaptive clinical trial design`, `blinded interim analysis`, `composite binary endpoints`, `sample size reassessment`, `type 1 error control`
- **为什么对您有用**: 涉及假设检验中的 I 类错误控制与功效分析（适应性设计），以及流行病学/临床试验的 RCT 设计应用，但缺乏您核心关注的深层数学统计或半参数效率理论。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1093/biostatistics/kxac035](https://doi.org/10.1093/biostatistics/kxac035) — A scalable and unbiased discordance metric with <i>H</i> +
- **作者**: Nathan Dyjack, Daniel N Baker, Vladimir Braverman, Ben Langmead, Stephanie C Hicks
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 1 · pp 188-202
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在无监督聚类设定下，当缺乏真实标签时，内部有效性指标常用于评估聚类质量，但不同相异度度量的量级差异导致跨尺度比较困难。现有尺度无关指标 G+ 存在两大缺陷：对大规模数据计算缓慢，且其值随组平衡（各簇样本比例）变化而产生偏倚。本文提出改进指标 H+，通过修正构造使其对组平衡具有不变性，从而消除该偏倚。同时，作者设计了基于排序和随机化的可扩展算法以高效估计 H+，并在 R 包 fasthplus 中实现。模拟与单细胞 RNA 测序数据验证了 H+ 的无偏性与算法的高效性。对您而言，该文在统计计算（可扩展算法设计）和指标无偏性构造上有一定参考价值，但与因果推断或半参数效率等核心方向关联较弱。
- **关键技术**: `internal validity metric`, `discordance metric`, `group balance invariance`, `scalable algorithm`, `unsupervised clustering`
- **为什么对您有用**: 涉及统计计算中的可扩展算法设计与无偏指标构造，但核心属于聚类评估，与您的主攻方向（因果/半参数/高维理论）距离较远，仅作计算方法参考。

### 2. [10.1093/biostatistics/kxac039](https://doi.org/10.1093/biostatistics/kxac039) — An online framework for survival analysis: reframing Cox proportional hazards model for large data sets and neural networks
- **作者**: Aliasghar Tarkhan, Noah Simon
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 1 · pp 134-153
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在大规模数据与神经网络设定下，传统 Cox 比例风险模型的部分似然(partial likelihood)因无法自然解耦，导致牛顿-拉夫森算法计算不稳定且不适用于随机梯度下降(SGD)。本文提出一种对 Cox 回归的简单重构，将目标函数转化为可加形式，使其天然适配 SGD 与在线学习。该方法避免了传统近似方法在大样本下的内存与计算瓶颈，并支持深度神经网络的端到端训练。理论与实验表明该框架在大规模数据集上计算高效且数值稳定。对您有用：直接契合您在统计计算（数值方法与算法）方向的兴趣，为大规模半参数生存模型提供了适配 SGD 的优化重构，思路可迁移至其他不可分解似然的半参数模型。
- **关键技术**: `Cox proportional hazards`, `stochastic gradient descent`, `partial likelihood reformulation`, `online learning`, `neural network survival model`
- **为什么对您有用**: 直接契合您在统计计算（数值方法与算法）方向的兴趣，为大规模半参数生存模型提供了适配 SGD 的优化重构，思路可迁移至其他不可分解似然的半参数模型。

## 流行病学  *(epidemiology, 5 篇)*

### 1. [10.1093/biostatistics/kxac034](https://doi.org/10.1093/biostatistics/kxac034) — A Bayesian framework for incorporating exposure uncertainty into health analyses with application to air pollution and stillbirth
- **作者**: Saskia Comess, Howard H Chang, Joshua L Warren
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 1 · pp 20-39
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在环境流行病学两阶段建模（先预测暴露再拟合健康结局）设定下，目标是纠正暴露预测不确定性对暴露-健康关联估计的影响。提出一种贝叶斯核密度估计（KDE）框架，利用第一阶段暴露模型的后验输出构建第二阶段的似然，避免信息损失。推导了Gibbs抽样所需的满条件分布以提升MCMC计算效率，并与忽略测量误差或简单近似的传统方法进行了理论联系与对比。模拟表明该KDE方法在多种设定及模型比较指标下表现更优。实证分析了新泽西州PM2.5滞后暴露与死胎的关联，发现分娩前3天高暴露显著增加风险。对您可能有用：提供了流行病学应用中处理两阶段测量误差的计算方案与R包，但缺乏半参数效率或因果识别等理论深度。
- **关键技术**: `Bayesian measurement error`, `kernel density estimation`, `two-stage inference`, `Gibbs sampling`, `full conditional distribution`
- **为什么对您有用**: 属于流行病学（secondary interest）应用关联分析，提供了处理两阶段暴露不确定性的贝叶斯计算方案和真实数据集，但缺乏半参数效率或因果识别等理论深度。

### 2. [10.1093/biostatistics/kxac049](https://doi.org/10.1093/biostatistics/kxac049) — An imputation approach for a time-to-event analysis subject to missing outcomes due to noncoverage in disease registries
- **作者**: Joanna H Shih, Paul S Albert, Jason Fine, Danping Liu
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 1 · pp 117-133
- 相关性 0/10 · novelty: `application`
- **摘要**: 在疾病登记库覆盖不全导致生存结局缺失的队列设定下，目标是利用纵向自报诊断数据对未覆盖区域的发病时间进行填补与估计。提出两步填补法：第一步使用 mover–stayer 模型，基于10年间隔问卷和死亡时点观测的覆盖状态，填补个体随时间变化的登记库覆盖轨迹。第二步在填补出的覆盖区域样本上拟合半参数工作模型，进而对未覆盖区域的登记库生存结局进行多重填补。相比仅删除缺失或简单替代的 ad hoc 方法，该框架显式刻画了覆盖状态的动态转移与缺失机制。模拟研究显示其有限样本性质优于替代方案，实证分析链接了美国放射技师队列与32州联合癌症登记库。对您有用：该文展示了半参数工作模型在复杂纵向缺失数据下的应用，其两步填补框架和流行病学真实队列数据可迁移至纵向因果推断中处理测量误差或不可忽略缺失的情境。
- **关键技术**: `mover-stayer model`, `semiparametric working model`, `multiple imputation`, `time-to-event analysis`, `missing data mechanism`
- **为什么对您有用**: 属于流行病学应用（secondary interest），使用半参数工作模型处理纵向缺失数据，其两步填补框架和真实队列数据对您在纵向因果推断中处理缺失/测量误差有方法迁移价值。

### 3. [10.1093/biostatistics/kxac046](https://doi.org/10.1093/biostatistics/kxac046) — Spatiotemporal varying coefficient model for respiratory disease mapping in Taiwan
- **作者**: Feifei Wang, Congyuan Duan, Yang Li, Hui Huang, Ben-Chang Shia
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 1 · pp 40-56
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文研究台湾地区PM2.5对呼吸系统疾病就诊率的影响，设定了具有空间变系数和参数化时间趋势的贝叶斯疾病制图模型。核心方法采用空间变系数模型捕捉暴露效应的空间异质性，并结合INLA（集成嵌套拉普拉斯近似）进行高效贝叶斯推断，避免了MCMC的计算瓶颈。模拟研究表明该方法在有限样本下的参数估计和预测精度上均有提升。实证分析覆盖台湾328个三级行政区，发现PM2.5与就诊率显著相关。对您而言，该文提供了流行病学空间数据的应用案例，INLA计算方法对大规模贝叶斯模型有参考价值，但方法学新颖度有限。
- **关键技术**: `spatially varying coefficient model`, `Bayesian disease mapping`, `INLA (integrated nested Laplace approximation)`, `spatiotemporal modeling`
- **为什么对您有用**: 属于流行病学应用方向，提供了空间流行病学数据集和分析范式；INLA计算方法对统计计算兴趣有微弱参考，但方法学新颖度较低。

### 4. [10.1093/biostatistics/kxac043](https://doi.org/10.1093/biostatistics/kxac043) — Joint modeling of longitudinal and competing-risk data using cumulative incidence functions for the failure submodels accounting for potential failure cause misclassification through double sampling
- **作者**: Christos Thomadakis, Loukia Meligkotsidou, Constantin T Yiannoutsos, Giota Touloumi
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 1 · pp 80-97
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在纵向与竞争风险数据的联合建模设定下，本文提出基于累积发生函数（CIF）的共享参数模型，以直接评估事件预后并处理潜在失效原因的错分类。方法采用广义优势率变换（含比例亚分布风险模型为特例），并正式约束全因 CIF 有界性为 1。通过双重抽样（double sampling）扩展模型以纠正失效原因错分类，并在贝叶斯框架下利用多状态表示推导状态占据与转移概率的后验样本。模拟与 HIV 真实数据展示了方法表现。对您而言，该文提供了流行病学队列中处理纵向测量误差与竞争风险错分类的贝叶斯联合建模思路，但缺乏半参数效率或高维理论。
- **关键技术**: `shared parameter model`, `cumulative incidence function`, `competing risks`, `generalized odds rate transformation`, `double sampling misclassification`, `Bayesian multistate model`
- **为什么对您有用**: 涉及纵向数据与竞争风险（与 causal inference 的 longitudinal 子方向相关），并在 HIV 流行病学数据上应用；但方法为贝叶斯参数模型，无半参数/效率理论，主要价值在于应用建模框架与数据集参考。

### 5. [10.1093/biostatistics/kxac038](https://doi.org/10.1093/biostatistics/kxac038) — Multiple exposure distributed lag models with variable selection
- **作者**: Joseph Antonelli, Ander Wilson, Brent A Coull
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 1 · pp 1-19
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在环境流行病学设定下，研究多暴露的分布式滞后模型（DLM），目标是在高维暴露时识别主效应、跨暴露交互作用及其各自的临界窗口，假设暴露-时间曲线为半参数形式。提出一种贝叶斯框架，利用 spike-and-slab 先验进行高维暴露及暴露间交互作用的变量选择；暴露的时间效应通过半参数分布式滞后曲线刻画，以识别不同暴露具有不同滞后效应的时间窗口。文中讨论了提升有害暴露检测功效的扩展，实证分析基于科罗拉多州出生记录数据评估孕期多种空气污染物对出生体重的影响。对您有用：该文将半参数曲线与高维变量选择结合的框架，可为流行病学队列研究中高维纵向暴露的建模提供真实数据集与方法借鉴，尽管其贝叶斯先验路径与您偏好的 debiased ML/效率理论路径不同。
- **关键技术**: `distributed lag models`, `spike-and-slab priors`, `semiparametric exposure-response curves`, `variable selection for interactions`, `critical window identification`
- **为什么对您有用**: 涉及高维变量选择与半参数曲线估计，且属于流行病学应用，提供了真实的高维纵向暴露数据集（科罗拉多州空气污染与出生体重），对您在流行病学因果推断或高维半参数建模的应用研究有数据集与建模思路的参考价值。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

