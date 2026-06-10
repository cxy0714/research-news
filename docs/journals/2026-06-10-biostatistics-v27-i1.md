# Biostatistics — Vol 27  Issue 1  ·  2026-06-10

- 共 17 篇 · Biostatistics
- 目录核对 ✅ 17 篇全部抓到（对照 OpenAlex 18 篇）

## 因果推断  *(causal_inference, 4 篇)*

### 1. [10.1093/biostatistics/kxag009](https://doi.org/10.1093/biostatistics/kxag009) — IV-learner: learning conditional average treatment effects using instrumental variables
- **作者**: Stijn Vansteelandt, Stephen O’Neill, Richard Grieve, Karla Diaz-Ordaz
- **期刊/来源**: Biostatistics
- **机构**: University College Ghent · Ghent University · University of London · London School of Hygiene & Tropical Medicine · University College London
- **分类**: vol 27 · issue 1
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在存在未测量混杂的 IV 设定下，本文目标是估计条件平均处理效应（CATE），关键假设为标准 IV 独立性及排他性约束。直接将第一阶段回归的灵活预测代入 R-learner 会因数据自适应方法的正则化偏差传播导致 CATE 估计精度差；而现有 Neyman-orthogonal IV learner 在模拟中表现不佳。作者利用无限维 targeted learning（TMLE 思想）对第一阶段预测进行定向裁剪，构建 targeted Neyman-orthogonal IV-learner，以隔离正则化偏差并保证 CATE 估计的局部有效性。该方法可基于任意现成 learner 构建，支持连续/离散暴露及任意数量 IV 和协变量。模拟与 ICU 转运再分析显示该方法性能大幅提升。对您有用：直接推进了您关注的 IV 估计与 semiparametric efficiency / debiased ML 交叉方向，且提供了流行病学真实数据应用范例。
- **关键技术**: `conditional average treatment effects (CATE)`, `instrumental variables (IV)`, `Neyman-orthogonal learner`, `infinite-dimensional targeted learning`, `regularization bias mitigation`, `first-stage prediction tailoring`
- **为什么对您有用**: 直接连接到 causal inference 的 IV 估计子方向，以及 efficiency theory 中的 Neyman-orthogonality / targeted learning。您 moderately_familiar 的 HOIF (Higher-Order Influence Functions) 与 semiparametric theory 正是分析此类 infinite-dimensional targeted learner 的局部有效性与高阶偏差的理论工具——可以用来严格验证其声称的偏差隔离是否达到 semipara efficiency bound。**中期可做**：需先在 moderately_familiar 的 HOIF / semipara theory 上长肌肉，以推导该 IV-learner 的 influence function 与高阶余项界。

### 2. [10.1093/biostatistics/kxag005](https://doi.org/10.1093/biostatistics/kxag005) · [arXiv](https://arxiv.org/abs/2403.02539) — Addressing the influence of unmeasured confounding in observational studies with time-to-event outcomes: a semiparametric sensitivity analysis approach
- **作者**: Linda Amoafo, Shiyao Xu, Elizabeth Platz, Daniel Scharfstein
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在观测性研究中针对时间-事件结局下未测量混杂的敏感性分析问题，目标是竞争暴露下潜在结果边际分布的 identification 与 estimation。方法基于影响函数技术，先推导无删失数据的非参数影响函数（non-parametric IF），再通过映射将其转化为观测数据的影响函数，从而在半参数敏感性分析框架下处理未测量混杂与删失的联合影响。实证部分应用于前列腺癌研究中根治性前列腺切除术（RP）与外照射放疗+雄激素剥夺（EBRT+AD）的比较，仿真展示了估计量的有限样本性质。对您有用之处在于将半参数影响函数推导与因果敏感性分析结合，直接对接 causal inference 的 sensitivity analysis 子方向与 semiparametric efficiency theory。
- **关键技术**: `non-parametric influence function`, `influence function mapping (uncensored to observed data)`, `semiparametric sensitivity analysis`, `time-to-event outcomes with competing exposures`, `marginal potential outcome distributions`, `censoring adjustment via IF transformation`
- **为什么对您有用**: 直接连接 causal inference 的 sensitivity analysis 子方向（未测量混杂的半参数敏感性分析）与 semiparametric efficiency theory（非参数影响函数推导与映射）。用 very_familiar 的 estimation theory in causal inference 可以审视其 sensitivity model 的 identification 是否完备；用 moderately_familiar 的 semiparametric theory / influence function 技术可检查其 IF 是否达到 semiparametric efficiency bound。中期可做——需先在 moderately_familiar 的 semiparametric theory 上长肌肉（具体是 HOIF 在 censored data 下的扩展），才能判断其 IF 映射是否遗漏了 higher-order correction 以及 sensitivity 参数空间的效率界。

### 3. [10.1093/biostatistics/kxag001](https://doi.org/10.1093/biostatistics/kxag001) · [arXiv](https://arxiv.org/abs/2412.00228) — A doubly robust framework for addressing outcome-dependent selection bias in multi-cohort EHR studies
- **作者**: Ritoban Kundu, Xu Shi, Michael Kleinsasser, Lars G Fritsche, Maxwell Salvatore, Bhramar Mukherjee
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在多队列 EHR 非概率样本设定下，目标是估计 outcome-dependent selection bias 下的关联参数（如疾病-暴露 odds ratio），传统跨队列 IPW 易因选择模型异质与错配而失效。本文提出 Joint Augmented IPW (JAIPW) 估计量，融合多队列非概率样本与外部概率样本数据；通过引入灵活的 auxiliary score 模型构建 AIPW 形式，实现 double robustness（选择模型或辅助模型之一正确即一致）。推导了 JAIPW 的渐近性质，模拟显示在选择模型错配下相对偏差与 RMSE 较最优 joint IPW 降低 6 倍与 5 倍。实证应用于 MGI 多队列 EHR 生物银行与全国概率样本，校正了癌症-性别及 PRS 关联的 selection bias。对您有用：直接连接因果推断的 selection bias 估计理论与流行病学 EHR 大数据应用。
- **关键技术**: `outcome-dependent selection bias`, `Augmented IPW (AIPW)`, `double robustness`, `auxiliary score model`, `non-probability sample integration`, `multi-cohort EHR data`
- **为什么对您有用**: (1) 连接到因果推断的 outcome-dependent selection bias 估计，以及流行病学 EHR 多队列数据应用；(2) 用 `estimation theory in causal inference` (very_familiar) 和 `semiparametric theory` (moderately_familiar) 可以审视 JAIPW 是否达到该 non-probability sample 模型的 semiparametric efficiency bound，或探讨高维 nuisance 下的 debiased ML 扩展；(3) **立即可做**：用 very_familiar 的 CI estimation 推导其 influence function 并验证效率界，或将其 nuisance 估计替换为 DML cross-fitting 以改善有限样本表现。

### 4. [10.1093/biostatistics/kxag004](https://doi.org/10.1093/biostatistics/kxag004) · [arXiv](https://arxiv.org/abs/2412.00926) — A sensitivity analysis approach to principal stratification with a continuous longitudinal intermediate outcome: applications to a cohort stepped wedge trial
- **作者**: Lei Yang, Michael J Daniels, Fan Li
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在 principal stratification (PS) 框架下，本文研究连续型中间变量设定下 principal causal effects (PCE) 的 identification 与估计问题——传统 PS 方法主要处理二值中间变量，连续中间变量使 principal strata 无限细化、identification 更困难。作者提出一种 sensitivity analysis 方法，利用 stepped wedge cluster randomized trial (SW-CRT) 中时变处理分配的结构来校准 sensitivity 参数，在现实假设下实现 PCE 的部分 identification。核心机制是将 SW-CRT 的多期随机化结构转化为对 sensitivity 参数的约束条件，而非依赖强分布假设。实证部分将该方法应用于中国 MSM 人群 HIV 检测的 cohort SW-CRT 数据，以社会规范为连续中间变量。对您可能有用：本文将 PS 从二值中间变量推广到连续情形，与您 causal inference 中 sensitivity analysis 和 mediation 的兴趣直接相关。
- **关键技术**: `principal stratification`, `sensitivity analysis`, `principal causal effects`, `stepped wedge cluster randomized trial`, `continuous intermediate variable`, `partial identification`
- **为什么对您有用**: (1) 直接连接 causal inference 中 sensitivity analysis 与 mediation/intermediate variable 子方向——PS 框架下连续中间变量的 sensitivity 分析是您 sensitivity analysis 兴趣的具体场景；(2) 您 technical_arsenal 中 "identification theory in causal inference"（moderately_familiar）可以攻这篇 paper 的 identification 部分——PS 在连续中间变量下的 partial identification 与 sensitivity parameter 的 formal treatment 正是 identification theory 可以深入分析的口子；(3) **中期可做**：需先在 moderately_familiar 的 identification theory 上长肌肉（PS 的 partial identification 与 sensitivity parameter 的 formal treatment），然后可以考虑将 semiparametric efficiency bound 引入该设定。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1093/biostatistics/kxaf051](https://doi.org/10.1093/biostatistics/kxaf051) — Shortcomings of deep learning for distributional predictors: a note
- **作者**: Bonnie B Smith, Abhirup Datta, Brian Caffo
- **期刊/来源**: Biostatistics
- **机构**: Johns Hopkins University
- **分类**: vol 27 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究当预测变量向量满足置换不变性（即仅依赖其内分布）时，无结构神经网络与显式利用不变性的 ordered predictors neural network (OPNN) 的表现差异。设定为均值回归函数仅由预测变量的分布决定，或更一般地，目标映射在输入置换下不变。模拟与 neural Bayes estimation 实验表明，无结构深度学习方法预测误差更高、估计精度更差，而 OPNN 通过简化学习任务显著降低误差并提升估计效率。核心结论是：已知或怀疑置换不变性时，应采用显式利用不变性的模型而非无结构网络。对您有用之处在于，OPNN 在 neural Bayes estimation 中实现的效率提升直接关联 semiparametric efficiency 与估计理论。
- **关键技术**: `permutation-invariant neural network`, `ordered predictors neural network`, `neural Bayes estimation`, `distributional predictor`, `invariance-aware model design`
- **为什么对您有用**: 本文连接到 semiparametric efficiency 与 estimation theory 子方向：OPNN 在 neural Bayes estimation 中通过显式利用置换不变性获得更紧的估计精度，这触及 semiparametric efficiency bound 的讨论——当模型具有已知结构约束（不变性）时，如何设计 estimator 以逼近效率界。用您 very_familiar 的 minimax bounds 与 estimation theory 可以分析 OPNN 是否真正逼近了该不变性模型下的 minimax rate，或是否存在进一步的理论 gap。follow-up 判断：立即可做——用 minimax 理论框架验证 OPNN 的收敛率是否达到效率界。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1093/biostatistics/kxag013](https://doi.org/10.1093/biostatistics/kxag013) — Statistical inference for high-dimensional generalized estimating equations
- **作者**: Lu Xia, Ali Shojaie
- **期刊/来源**: Biostatistics
- **机构**: Michigan State University · University of Washington · Cancer Research And Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在高维纵向/聚类相关数据设定下，目标是广义估计方程(GEE)中回归系数线性泛函的置信区间构造，关键假设为系数稀疏性与温和regularity条件。核心方法通过构造投影估计方程(projected estimating equations)实现去偏推断，机制与debiased ML/orthogonal score一致——沿投影方向修正初始Lasso估计的偏差。证明了线性泛函估计量的n^{-1/2}-CAN性质与渐近正态性，并引入数据驱动交叉验证程序选择投影方向的调优参数，填补了现有高维GEE推断方法未处理该调参问题的空白。实证上在COVID-19纵向蛋白质组学数据中展示了置信区间覆盖的稳健性。对您在debiased inference框架与纵向因果推断交叉方向的工作有直接参考价值。
- **关键技术**: `projected estimating equations`, `high-dimensional debiased inference`, `generalized estimating equations`, `cross-validation tuning for projection direction`, `asymptotic normality for linear functionals`, `sparse regression with correlated outcomes`
- **为什么对您有用**: 本文将debiased ML的投影去偏机制从独立数据推广到GEE下的纵向相关数据，直接连接您primary interest中的效率理论(debiased inference)与纵向因果推断两个子方向。您very_familiar的高维渐近理论可直接审视其投影方向估计的收敛条件是否与已知minimax rate一致，moderately_familiar的semiparametric理论可用来验证其声称的渐近正态性是否达到semiparametric efficiency bound。follow-up判断：立即可做——用您熟悉的HOIF/高阶U-stat工具检查该投影估计方程是否可进一步做higher-order correction以改善有限样本偏差。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1093/biostatistics/kxag016](https://doi.org/10.1093/biostatistics/kxag016) — High-dimensional test for one-sided hypotheses
- **作者**: Rongrong Wang, Shrabanti Chowdhury, Hanwen Huang, Xiaoling Wang, Deepak N Ayyala, Santu Ghosh
- **期刊/来源**: Biostatistics
- **机构**: University of Pittsburgh · Icahn School of Medicine at Mount Sinai · Augusta University · Augusta University Health · Takeda (Japan)
- **分类**: vol 27 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在高维设定下（p≫n），针对均值向量的单侧假设检验问题，本文提出 Sum Max-Component（SMC）检验方法。现有高维均值检验多聚焦双侧，单侧检验在检测基因集上调/下调时更具科学意义但理论不足。SMC 统计量结合 sum-of-squares 与 max-component 两种构造，在 Gaussian 型与 Exponential 型尾部条件下推导了 p,n→∞ 时的渐近分布与 power 性质。有限样本模拟显示 SMC 在 type I error 控制与 power 上优于现有单侧方法。实证部分将 SMC 用于卵巢癌 CPTAC 蛋白质组数据的基因集富集分析。对您有用：本文直接推进高维单侧假设检验的渐近理论，与您的高维统计与 hypothesis testing 兴趣高度契合。
- **关键技术**: `high-dimensional one-sided mean test`, `Sum Max-Component statistic`, `Gaussian-type tails`, `Exponential-type tails`, `joint asymptotic regime (p,n→∞)`, `gene set enrichment analysis`
- **为什么对您有用**: 本文连接您的高维统计与 hypothesis testing 两个 primary interest 子方向，聚焦单侧均值检验这一相对空白问题。您 very_familiar 的高维渐近理论可直接审视其渐近分布推导与 power rate 是否达到 minimax optimal；moderately_familiar 的 M-estimation 理论可用来分析 SMC 统计量在更一般损失函数下的扩展。follow-up 判断：立即可做——用您的高维渐近与 minimax bound 工具验证其声称的 power rate 是否紧，并探索 SMC 在非 Gaussian/Exponential 尾部下的 robustness。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1093/biostatistics/kxag007](https://doi.org/10.1093/biostatistics/kxag007) — Joint modeling of high-dimensional longitudinal data and survival using supervised low-rank tensor decomposition
- **作者**: Mohammad Samsul Alam, Rima Kaddurah-Daouk, Sheng Luo
- **期刊/来源**: Biostatistics
- **机构**: Duke University · Clinical Research Institute
- **分类**: vol 27 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在高维纵向omics数据与生存结局的联合建模设定下，目标是同时估计多变量纵向轨迹的潜在结构与比例风险模型参数，关键假设为纵向过程的低秩可分结构及baseline协变量提供监督信息。方法核心是将纵向过程表示为多变量功能张量，通过supervised low-rank functional tensor decomposition提取latent structure，并在比例风险子模型中引入subject-level latent predictors关联两个过程；估计采用likelihood-based Monte Carlo EM算法实现coherent inference与动态预测。模拟显示在高删失率与小样本下相比两阶段方法有显著精度提升。在ADNI lipidomics数据上，4个成分解释>99%变异并识别出痴呆发病的显著潜在预测因子。对您可能有用之处在于张量分解的计算框架与您在higher-order U-statistics的tensor contraction/einsum工作有结构相似性，且AD流行病学队列数据可直接用于因果推断方法的二次开发。
- **关键技术**: `supervised low-rank tensor decomposition`, `Monte Carlo EM algorithm`, `proportional hazards joint model`, `functional tensor representation`, `dynamic prediction`
- **为什么对您有用**: 本文连接到stat_computing中的tensor decomposition框架以及epidemiology中的AD队列数据应用。研究者very_familiar中的'computation of higher-order U-statistics (treewidth / tensor contraction / einsum)'可以用来分析此方法中functional tensor低秩近似的计算复杂度，特别是contraction order optimization是否适用于此处的tensor分解结构。中期可做：需先在moderately_familiar的semiparametric theory上长肌肉，才能将此joint model的效率性质（是否达到semiparametric efficiency bound、influence function形式）做严格理论分析，当前论文本身未触及这些。

### 2. [10.1093/biostatistics/kxag010](https://doi.org/10.1093/biostatistics/kxag010) · [arXiv](https://arxiv.org/abs/2412.20509) — Stochastic gradient descent estimation of generalized matrix factorization models with application to single-cell RNA sequencing data
- **作者**: Cristian Castiglione, Alexandre Segers, Lieven Clement, Davide Risso
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文在单细胞 RNA 测序降维场景下提出广义矩阵因子分解（GMF）模型，假定响应服从指数散布族分布，并证明文献中多种降维方法（PCA、NMF 等）均为其特例。核心方法贡献是可扩展的自适应随机梯度下降（ASGD）算法，用于估计 GMF 的左/右因子矩阵，支持百万级细胞规模；算法在内存占用与执行时间上优于现有广义/非负 MF 方法，同时保持或提升矩阵重构精度与生物信号提取质量。理论层面未给出 ASGD 估计量的收敛速率或渐近分布，仅通过模拟与真实数据实证验证。所有方法封装为 R 包 sgdGMF（CRAN）。对您而言，本文的矩阵因子分解 + SGD 计算框架与 statistical computing 及高维统计的矩阵估计问题有方法论邻接，但缺乏您关心的效率界或 RMT 渐近理论。
- **关键技术**: `adaptive stochastic gradient descent`, `generalized matrix factorization`, `exponential dispersion family`, `single-cell dimensionality reduction`, `non-negative matrix factorization`
- **为什么对您有用**: 本文落在 statistical computing（数值方法与软件）这一 primary interest 上，但更偏向生物信息应用而非您关心的理论计算问题（U-statistic tensor contraction / einsum 复杂度）。您武器库中 high-dimensional asymptotics 与 M-estimation theory（moderately_familiar）可用来研究 ASGD 估计量的渐近性质与收敛速率——这正是本文缺失的理论部分。follow-up 判断：中期可做——需先在 M-estimation theory 的 SGD 渐近分析上长肌肉，才能对 GMF-ASGD 估计量给出 rigorous rate / influence function 结果；若仅关注软件实现与数据规模，则立即可做但与您核心理论方向偏离。

## 流行病学  *(epidemiology, 6 篇)*

### 1. [10.1093/biostatistics/kxag002](https://doi.org/10.1093/biostatistics/kxag002) — Dynamic case-control sampling for rapid estimation of vaccine effectiveness against an emerging infectious disease variant
- **作者**: Taylor M Fortnam, Laura C Chambers, Alyssa Bilinski, Ewa King, Richard C Huard, Ellen Amore et al.
- **期刊/来源**: Biostatistics
- **机构**: Brown University · Department of Health Services · Rhode Island Department of Health
- **分类**: vol 27 · issue 1
- 相关性 6/10 · novelty: `application`
- **摘要**: 在公共卫生监测设定下，目标是利用实时累积数据动态估计新发变异株的疫苗有效性（VE）。本文提出动态病例对照抽样方法：将感染新变异株者定义为“病例”、感染旧变异株者定义为“对照”，持续更新新旧变异株VE的相对比值，再结合已有旧变异株VE估计（来自传统大规模研究）推断新变异株VE。核心机制是嵌套抽样设计下的条件似然估计，仅需部分测序数据即可运行；理论性质表现为标准误增大但样本量远小于传统研究时仍可接受。实证以Omicron BA.1/BA.2子谱系展示，估计值与传统方法可比。对您可能有用：该方法为流行病学监测中的因果效应（VE）动态估计提供了可迁移的抽样-估计框架。
- **关键技术**: `dynamic case-control sampling`, `test-negative design`, `conditional likelihood estimation`, `relative vaccine effectiveness`, `real-time surveillance estimation`
- **为什么对您有用**: 直接连接流行病学因果推断应用（VE估计），属于secondary interest中的epidemiology方向。本文的动态病例对照抽样本质上是一种条件似然下的因果效应识别策略，与您very_familiar中的causal inference estimation theory有概念对接，但技术深度较浅（无semiparametric efficiency或higher-order分析）。作为gateway reading：入门性好，数据与模型设定清晰，适合了解公共卫生监测中VE估计的实际约束与抽样设计；武器库足以支撑进入此方向，但若要在此做方法学推进需先在moderately_familiar的semiparametric theory上长肌肉（例如推导该动态抽样下VE的efficient influence function与semiparametric efficiency bound）。是否值得读全文：若对流行病学因果推断应用场景感兴趣，值得快速浏览以了解实际数据结构与抽样约束；若寻求理论推进，则本文novelty有限。

### 2. [10.1093/biostatistics/kxag003](https://doi.org/10.1093/biostatistics/kxag003) — SAM-HC: a Bayesian nonparametric construction of hybrid control for randomized clinical trials using external data
- **作者**: Dehua Bi, Tianjian Zhou, Wei Zhong, Yuan Ji
- **期刊/来源**: Biostatistics
- **机构**: Chicago Department of Public Health · Colorado State University · Pfizer (United States)
- **分类**: vol 27 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在有高质量外部数据或对照组招募困难的RCT设定下，目标是借外部数据增强对照组以更精确估计处理效应，关键假设为外部与试验数据间存在潜在异质子群。采用Bayesian非参数模型Shared Atoms Model (SAM)识别跨数据集的重叠与独有子群，仅对共同子群借信息形成hybrid control (HC)；借信息程度受样本量与结局相似度双重约束，避免过度借用导致bias。模拟研究显示方法在异质设定下鲁棒，Atopic Dermatitis真实数据应用展示处理效应估计精度改善。对您而言，本文展示了外部数据借用的子群识别思路，但Bayesian非参数路线与您semiparametric efficiency / influence function技术栈差异较大。
- **关键技术**: `Bayesian nonparametric model`, `Shared Atoms Model`, `hybrid control`, `subpopulation clustering`, `treatment effect estimation`, `external data borrowing`
- **为什么对您有用**: (1) 连接到epidemiology secondary interest中RCT外部数据借用与处理效应估计，但非您primary的proximal CI / IV / mediation子方向；(2) Bayesian非参数SAM与您very_familiar的minimax bound / semiparametric efficiency工具不直接兼容，若要从您的技术栈切入，可考虑对HC设定下的ATE推导semiparametric efficiency bound并构造one-step / DR estimator作为对照方案；(3) 中期可做——需先在moderately_familiar的semiparametric theory上为HC借信息设定建立efficiency bound框架，再设计debiasing方案与SAM做理论-计算对比。

### 3. [10.1093/biostatistics/kxag011](https://doi.org/10.1093/biostatistics/kxag011) — Adaptive transfer learning for time-to-event modeling with applications in disease risk assessment
- **作者**: Yuying Lu, Tian Gu, Rui Duan
- **期刊/来源**: Biostatistics
- **机构**: Columbia Medical Practice · District of Columbia Public School · Harvard University Press
- **分类**: vol 27 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在小样本生存分析设定下，本文提出基于 Cox 比例风险模型的迁移学习方法 CoxTL，目标 estimand 为目标人群的条件风险率/生存函数，假设源与目标数据间存在 covariate shift 与 coefficient shift 两层异质性。核心机制组合 density ratio weighting 与 importance weighting 分别处理协变量分布偏移与系数偏移，并对潜在模型误设提供鲁棒性保证。模拟研究显示在多水平异质性场景下预测精度优于仅处理单一偏移的竞争方法，单一偏移场景下表现相当。在 All of Us Research Program 的 EHR 数据上预测 Hispanic 人群 ESRD 2 年风险，C-index 相比仅用目标数据提升 6.76%，相比现有 Cox 迁移方法提升 17.94%。对您可能有用：作为流行病学真实数据应用案例，density ratio weighting 与 importance weighting 的组合思路可类比因果推断中处理 positivity/selection bias 的加权修正策略。
- **关键技术**: `Cox proportional hazards model`, `density ratio weighting`, `importance weighting`, `covariate shift correction`, `concept shift correction`, `transfer learning under model misspecification`
- **为什么对您有用**: (1) 连接到流行病学应用子方向——ESRD 跨人群风险预测，涉及真实 EHR 数据集（All of Us），是典型的 minority population 小样本场景；(2) density ratio weighting 与 importance weighting 的组合可类比因果推断中处理 selection bias 的加权策略，但本文未触及 semiparametric efficiency bound 或 influence function，理论深度有限，用 very_familiar 的 estimation theory in causal inference 可审视其加权估计量的偏差-方差权衡是否可更严格刻画；(3) 中期可做——若想将迁移学习框架嵌入 semiparametric efficiency theory（推导迁移设定下的效率界或 debiased 版本），需先在 moderately_familiar 的 semiparametric theory 上长肌肉，本文本身不提供此理论入口。

### 4. [10.1093/biostatistics/kxaf052](https://doi.org/10.1093/biostatistics/kxaf052) — Risk functions with outcome measurement error
- **作者**: Jessie K Edwards, Stephen R Cole, Paul N Zivich, Benjamin Ackerman, Sonia Napravnik, Heather Henderson et al.
- **期刊/来源**: Biostatistics
- **机构**: University of North Carolina at Chapel Hill · Johnson & Johnson (United States) · Emory Healthcare · Emory University
- **分类**: vol 27 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在流行病学队列研究中，当结局（死亡）通过死亡登记 linkage 确认时，可能存在漏报、误报和时间错配三类结局测量误差，导致死亡风险和生存函数估计偏倚。本文将经典 Rogan-Gladen 估计量扩展到右删失生存数据设定下，通过灵敏度/特异度参数修正结局测量误差对风险函数的影响。方法可基于内部或外部验证数据参数化，也可作为定量偏倚分析工具；模拟显示即使在验证子样本有更高死亡风险的选择偏倚下，修正估计仍表现良好。对您可能有用：该文为流行病学结局测量误差提供了可操作的修正框架，直接连接到您在因果推断 sensitivity analysis 的兴趣。
- **关键技术**: `Rogan-Gladen estimator`, `outcome measurement error correction`, `sensitivity and specificity parameterization`, `quantitative bias analysis`, `right-censored survival data`
- **为什么对您有用**: 本文直接连接到流行病学应用中的因果推断/偏倚修正子方向，用 sensitivity/specificity 参数化做定量偏倚分析，与您在 causal sensitivity analysis 的兴趣一致。用您 very_familiar 的 estimation theory in causal inference 可以审视其修正估计量的 identifiability 条件和效率性质（是否达到 semiparametric efficiency bound）。follow-up 判断：立即可做——用 semiparametric theory 检查该修正估计量的 influence function 和效率界，或将其嵌入您熟悉的 sensitivity analysis 框架做扩展。

### 5. [10.1093/biostatistics/kxag008](https://doi.org/10.1093/biostatistics/kxag008) · [arXiv](https://arxiv.org/abs/2512.14504) — A flexible class of latent variable models for the analysis of antibody response data
- **作者**: Emanuele Giorgi, Jonas Wallin
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在流行病学血清学数据分析中，传统方法假设个体可二分为血清阴性与阳性，本文挑战此二分假设，提出连续潜变量模型刻画免疫状态。模型将免疫状态视为从最小到最强免疫激活的连续潜变量，可包容机制模型与回归模型，并将有限混合模型作为特例。为克服 MLE 计算代价，提出基于 L2 距离的估计量并证明其一致性，大幅降低计算成本。在疟疾血清学案例中展示了跨年龄联合分析及传播模式变化下的灵活性。对您有用：该文在流行病学数据集上展示了连续潜变量建模与 L2 估计，为 epi 数据的 latent exposure 与 causal misclassification 问题提供新视角。
- **关键技术**: `latent variable model`, `L2-based estimator`, `continuum seroreactivity`, `consistency proof`, `finite mixture model`
- **为什么对您有用**: (1) 点名连接到 epidemiology secondary interest 的血清学数据集与潜变量建模，这直接关联到流行病学中暴露变量测量误差与因果推断的设定。(2) 点名 technical_arsenal 中 moderately_familiar 的 M-estimation theory 可以攻这篇 paper 的 L2 估计量：目前作者只证明了 consistency，但未给出 asymptotic normality 或 semiparametric efficiency bound，可用 M-estimation 理论推导其极限分布并与 MLE 做效率比较。(3) 中期可做：需先在 moderately_familiar 的 M-estimation theory 上长肌肉，推导该 L2 估计量的 influence function 与效率界。

### 6. [10.1093/biostatistics/kxag006](https://doi.org/10.1093/biostatistics/kxag006) · [arXiv](https://arxiv.org/abs/2401.06082) — Borrowing from historical control data in a Bayesian time-to-event model with flexible baseline hazard function
- **作者**: Darren A V Scott, Alex Lewin
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在临床试验时间-事件数据设定下，目标是利用历史对照数据借力估计处理效应，传统贝叶斯借力方法通常约束基线风险函数形状以简化计算。本文提出一种贝叶斯借力半参数模型，通过 ensemble average 允许基线风险取任意形式，并引入先验对后验基线风险形状进行平滑。在参数可交换性假设下，准确建模基线风险而非近似其形式，提升了检验功效并降低了处理效应估计的偏差；在先验-数据冲突时，降低了 I 类错误膨胀。引入 lump-and-smear 借力先验，并基于历史与当前 log-baseline hazard 的容忍差异提出了超参数选择的准则。实证结果表明该方法在冲突下控制 I 类错误、在一致下提升功效方面优于传统方法，并提供了 R 软件实现。对您可能有用：本文将半参数基线风险建模与贝叶斯动态借力结合，为流行病学/临床试验中的处理效应估计提供了新视角，其半参数先验平滑机制可启发您在 semiparametric theory 下的进一步理论探索。
- **关键技术**: `Bayesian dynamic borrowing`, `semiparametric baseline hazard`, `ensemble average hazard`, `lump-and-smear prior`, `prior-data conflict`, `time-to-event model`
- **为什么对您有用**: 连接到流行病学临床试验的历史对照借力与处理效应估计，核心是 semiparametric baseline hazard 的灵活建模。您的 moderately_familiar 中的 semiparametric theory 可用来审视其 ensemble average hazard 的理论性质（如后验收敛率与 semiparametric efficiency bound 的关系），very_familiar 的 software development 可评估其 R 包的计算架构。中期可做：需先在 moderately_familiar 的 semiparametric theory 上长肌肉（特别是贝叶斯非/半参数后验收敛率），才能理论化其先验平滑对效率的影响。

## 其他  *(other, 2 篇)*

### 1. [10.1093/biostatistics/kxag012](https://doi.org/10.1093/biostatistics/kxag012) — NBSR: a Negative Binomial Softmax Regression model for microRNA-seq data analysis
- **作者**: Seong-Hwan Jun, Marc K Halushka, Matthew N McCall
- **期刊/来源**: Biostatistics
- **机构**: University of Rochester Medical Center · Cleveland Clinic
- **分类**: vol 27 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对 microRNA-seq 数据提出 Negative Binomial Softmax Regression (NBSR) 模型，estimand 为实验条件间的 log relative abundance ratio (log-RAR) 及绝对丰度 fold change。模型将 biological coefficient of variation 与 relative abundance 的关系纳入负二项参数化，并通过 softmax link 处理高度变异与稀疏表达的 microRNA。作者证明直接套用 mRNA-seq 方法（如负二项 GLM）会导致高 false discovery rate；NBSR 通过对 log-RAR 的 debiasing 实现对绝对丰度 fold change 的准确推断，尤其在仅少数 microRNA 差异表达时避免了 composition bias。模拟与真实数据表明 NBSR 在 power 与 CI 宽度上优于现有方法。对您而言，本文的 debiasing 思路与 composition bias 校正与 efficiency theory / debiased ML 中的 bias-correction 逻辑有形式上的相似，但属于生物统计应用，方法学 novelty 有限。
- **关键技术**: `negative binomial regression`, `softmax link function`, `log relative abundance ratio`, `debiasing composition bias`, `biological coefficient of variation modeling`
- **为什么对您有用**: 本文属于生物统计应用，与您 primary interest 的 causal inference / high-dim / efficiency theory 无直接交集。其 debiasing 步骤形式上类似 debiased ML 的 bias-correction，但场景是计数数据的 composition bias，而非 semiparametric efficiency bound 的 second-order bias。武器库中 semiparametric theory / M-estimation theory 可理解其推断框架，但无攻入新问题的口子。判断：**暂不可做**——核心场景（microRNA-seq composition bias）不在您研究范围，且缺乏与您 higher-order U / RMT / proximal CI 的技术连接，不值得展开读全文。

### 2. [10.1093/biostatistics/kxaf049](https://doi.org/10.1093/biostatistics/kxaf049) · [arXiv](https://arxiv.org/abs/2412.08828) — A two-stage approach for segmenting spatial point patterns applied to multiplex imaging
- **作者**: Alvin Sheng, Brian J Reich, Ana-Maria Staicu, Santhoshi N Krishnan, Arvind Rao, Timothy L Frankel
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对多重成像数据中的空间点模式分割问题，提出两阶段方法：第一阶段对每张图像估计局部强度函数与 pair correlation function，并通过协方差函数的谱分解对 pair correlation function 降维；第二阶段在 Bayesian 层次模型中对降维后的估计量做聚类，聚类标签具有空间依赖性（spatially-dependent cluster labels），通过 MCMC 联合估计聚类分配与各聚类的空间特征并量化不确定性。模拟验证了方法性能，并应用于胰腺病变组织的多重免疫荧光图像。该方法的核心 novelty 在于将非参数空间点过程特征提取与 Bayesian 空间聚类结合，但非参数估计部分（pair correlation function、谱分解）使用的是成熟工具，理论层面未给出收敛率或效率界。对您而言，仅谱分解降维与非参数函数估计的交叉有微弱方法学重叠，核心问题（空间点过程聚类）不在您的主线方向上。
- **关键技术**: `pair correlation function estimation`, `spectral decomposition of covariance function`, `Bayesian hierarchical clustering`, `spatially-dependent cluster labels`, `MCMC posterior sampling`, `spatial point pattern modeling`
- **为什么对您有用**: 本文与您的主线兴趣（因果推断、高维/RMT、效率理论、higher-order U）几乎没有直接交集；非参数函数估计（pair correlation function）与谱分解降维仅是您 very_familiar 中 nonparametric statistics 的边缘触碰。应用领域（肿瘤免疫学成像）也不在您指定的三个 secondary 方向（astrostats / econ / epi）之内。follow-up 判定：**暂不可做**——本文的核心机器（空间点过程、Bayesian 空间聚类）不在武器库中，且问题本身与您的研究议程不对接，不建议花时间深读全文。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

