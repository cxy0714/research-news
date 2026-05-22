# Biostatistics — Vol 27  Issue 1  ·  2026-05-21

- 共 12 篇 · Biostatistics

## 因果推断  *(causal_inference, 3 篇)*

### 1. [10.1093/biostatistics/kxag003](https://doi.org/10.1093/biostatistics/kxag003) — SAM-HC: a Bayesian nonparametric construction of hybrid control for randomized clinical trials using external data
- **作者**: Dehua Bi, Tianjian Zhou, Wei Zhong, Yuan Ji
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在利用外部数据构建随机对照试验混合对照组(Hybrid Control)的设定下，目标是处理试验与外部数据间存在异质性亚群时的处理效应估计。本文提出基于 Shared Atoms Model (SAM) 的贝叶斯非参数构造，通过识别跨数据集的重叠与唯一亚群，将信息借用限制在共同亚群中。借用的程度受样本量与结局相似度约束，从而在保证稳健性的同时提高估计精度。模拟表明该方法对异质性稳健，特应性皮炎数据集的应用展示了更优的处理效应估计。该文展示了贝叶斯非参数方法在因果推断数据融合中处理未观测异质性的机制，对您在因果推断中考虑外部数据借用及非参数建模有参考价值。
- **关键技术**: `Bayesian nonparametrics`, `Shared Atoms Model`, `hybrid control`, `data fusion`, `subpopulation heterogeneity`
- **为什么对您有用**: 涉及因果推断中RCT外部数据借用与异质性处理，采用贝叶斯非参数方法，对您在因果推断的数据融合及非参数理论方向有参考价值。

### 2. [10.1093/biostatistics/kxag001](https://doi.org/10.1093/biostatistics/kxag001) — A doubly robust framework for addressing outcome-dependent selection bias in multi-cohort EHR studies
- **作者**: Ritoban Kundu, Xu Shi, Michael Kleinsasser, Lars G Fritsche, Maxwell Salvatore, Bhramar Mukherjee
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多队列电子病历(EHR)非概率抽样研究中，针对结局依赖的选择偏倚问题，目标是估计二值疾病风险模型中的关联参数。本文提出 Joint Augmented IPW (JAIPW) 估计量，通过整合多队列个体数据与外部概率样本数据实现双重稳健性。该估计量引入灵活的辅助得分模型，以应对不同队列选择机制异质性导致的模型误设问题。理论上给出了 JAIPW 的渐近性质；在选择模型误设下，模拟显示其相对偏倚和 RMSE 分别降低至传统联合 IPW 方法的 1/6 和 1/5。实证分析将 MGI 多临床 EHR 生物库与国家概率样本结合，估计癌症-性别及癌症-多基因风险评分(PRS)关联。对您有用：该框架将 AIPW 双重稳健理论拓展至多队列结局依赖选择偏倚设定，且 EHR 实证分析对流行病学队列研究的因果推断与缺失数据方法有直接迁移价值。
- **关键技术**: `double robustness`, `Augmented Inverse Probability Weighting (AIPW)`, `outcome-dependent selection bias`, `non-probability sampling`, `auxiliary score model`, `multi-cohort integration`
- **为什么对您有用**: 将 AIPW 双重稳健与半参数效率理论拓展至多队列 EHR 的结局依赖选择偏倚设定，对您在因果推断（选择偏倚/缺失数据）和流行病学应用（EHR 队列数据集）方面的兴趣有直接参考价值。

### 3. [10.1093/biostatistics/kxag004](https://doi.org/10.1093/biostatistics/kxag004) — A sensitivity analysis approach to principal stratification with a continuous longitudinal intermediate outcome: applications to a cohort stepped wedge trial
- **作者**: Lei Yang, Michael J Daniels, Fan Li
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在阶梯楔形集群随机试验（SW-CRT）设定下，本文研究以连续型纵向中间变量为分层依据的主分层因果效应（PCE）的识别与估计问题，突破了现有主分层方法仅处理二元中间变量的限制。核心方法利用 SW-CRT 中处理分配随时间变化的结构，校准敏感性参数并在现实假设下实现 PCE 的识别；估计策略结合了纵向建模与敏感性分析框架，无需对连续中间变量的潜在结果做不可验证的强分布假设。技术工具涉及主分层框架下的非参数识别缺失、敏感性参数的校准机制、以及 SW-CRT 交叉设计带来的内部有效性增益。实证部分将方法应用于中国男男性行为者 HIV 检测的队列 SW-CRT，以社会规范为连续中间变量展示 PCE 估计。对您有用：该文将敏感性分析嵌入主分层/中介框架并处理连续纵向中间变量，与您关注的 causal inference 中 sensitivity analysis、mediation 及 longitudinal 设定直接对接，敏感性参数校准思路可迁移至其他连续中介场景。
- **关键技术**: `principal stratification`, `principal causal effects`, `sensitivity analysis`, `stepped wedge cluster randomized trial`, `continuous intermediate variable`, `longitudinal treatment assignment`
- **为什么对您有用**: 直接对应您 primary interest 中 causal inference 的 sensitivity analysis、mediation 与 longitudinal 子方向；将主分层从二元扩展到连续中间变量的敏感性分析思路，可迁移至您关心的 proximal CI 或 IV 场景中处理连续型 unmeasured confounder 的识别问题。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1093/biostatistics/kxag013](https://doi.org/10.1093/biostatistics/kxag013) — Statistical inference for high-dimensional generalized estimating equations
- **作者**: Lu Xia, Ali Shojaie
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在高维广义估计方程（GEE）框架下，目标是对相关数据（如纵向）回归系数的线性泛函进行推断，假设协变量维度 p 远大于样本量 n 且工作相关结构已知或可估。核心方法通过构造投影估计方程（projected estimating equations）获得线性泛函的 debiased 估计量，在温和正则条件下证明其渐近正态性（n^{-1/2}-CAN）；同时提出数据驱动的交叉验证程序选择投影方向的调优参数，弥补了现有高维 GEE 推断方法中调优参数选取的理论空白。模拟表明该估计量在有限样本下偏差更小、置信区间覆盖更准。该方法可迁移至您关注的纵向因果推断中高维协变量调整后的 debiased 推断场景，投影估计方程的构造思路也与 semiparametric efficiency / orthogonal score 方法论相通。
- **关键技术**: `projected estimating equations`, `high-dimensional GEE`, `debiased inference for linear functionals`, `cross-validation tuning parameter selection`, `asymptotic normality under high dimensions`, `longitudinal correlated data`
- **为什么对您有用**: 直接推进高维推断（primary interest），投影估计方程的构造与 debiased ML / orthogonal score 思路一致，且 GEE 纵向设定可迁移至您关注的 longitudinal causal inference 中高维协变量调整场景；COVID-19 蛋白质组学应用提供流行病学数据集参考。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1093/biostatistics/kxag006](https://doi.org/10.1093/biostatistics/kxag006) — Borrowing from historical control data in a Bayesian time-to-event model with flexible baseline hazard function
- **作者**: Darren A V Scott, Alex Lewin
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在单历史数据集的贝叶斯生存分析框架下，研究如何在放松基线风险函数形状约束时进行动态借据，目标是准确估计处理效应并控制先验-数据冲突导致的 I 类错误膨胀。提出一种半参数贝叶斯借据模型，通过集成平均使基线风险函数具有完全灵活性，并引入先验平滑后验基线风险形状以改善估计与借据特性。相比传统约束基线风险以换取计算速度的方法，该模型在参数可交换性成立时降低了处理效应偏差并提升了功效。针对先验-数据冲突，引入 lump-and-smear 借据先验，有效抑制了 I 类错误膨胀。提出基于历史与当前对数基线风险容忍差异的超参数选择原则，并提供了 R 语言软件实现。对您可能有用：虽然侧重贝叶斯借据，但其对半参数基线风险的建模策略及先验-数据冲突下的稳健性分析，可为生存分析中的半参数理论及流行病学临床试验应用提供参考。
- **关键技术**: `Bayesian dynamic borrowing`, `semiparametric baseline hazard`, `lump-and-smear prior`, `prior-data conflict`, `time-to-event model`, `ensemble average`
- **为什么对您有用**: 涉及半参数模型（灵活基线风险）的设定与计算，且属于流行病学/临床试验的应用场景；虽然核心是贝叶斯借据而非您关注的频率学派效率理论，但其处理先验-数据冲突的思路及半参数生存模型的计算实现仍有参考价值。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1093/biostatistics/kxag007](https://doi.org/10.1093/biostatistics/kxag007) — Joint modeling of high-dimensional longitudinal data and survival using supervised low-rank tensor decomposition
- **作者**: Mohammad Samsul Alam, Rima Kaddurah-Daouk, Sheng Luo
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对高维纵向组学数据与生存结局的联合建模问题，设定纵向过程为多变量函数张量，生存结局采用比例风险模型。提出一种基于监督低秩函数张量分解的联合建模框架，通过低秩近似提取纵向数据的潜在结构并引入基线协变量的监督信息。估计方面采用基于似然的蒙特卡洛期望最大化（MCEM）算法，实现纵向轨迹与生存概率的联合推断与动态预测。模拟显示在高删失和小样本下，相比两阶段方法，估计精度和预测性能显著提升；在 ADNI 脂质组学数据中，4 个成分即可解释 99% 以上的变异并识别痴呆发病的潜在预测因子。对您而言，该文展示了张量分解与 MCEM 算法在高维纵向数据中的计算实现，且 ADNI 数据集对流行病学应用有参考价值。
- **关键技术**: `supervised low-rank tensor decomposition`, `Monte Carlo Expectation-Maximization (MCEM)`, `joint modeling of longitudinal and survival`, `proportional hazards model`, `dynamic prediction`
- **为什么对您有用**: 直接契合您在 statistical computing (tensor, numerical algorithm) 和 high-dimensional statistics 的兴趣；同时 ADNI 脂质组学数据集及纵向建模框架对您在 epidemiology (datasets) 和 causal inference (longitudinal) 的研究提供了数据与模型基础。

### 2. [10.1093/biostatistics/kxag010](https://doi.org/10.1093/biostatistics/kxag010) — Stochastic gradient descent estimation of generalized matrix factorization models with application to single-cell RNA sequencing data
- **作者**: Cristian Castiglione, Alexandre Segers, Lieven Clement, Davide Risso
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文针对单细胞RNA测序数据的高维降维问题，提出在指数分散族（exponential dispersion family）假设下的广义矩阵分解（GMF）模型，将现有多种降维方法统一为该模型的特例。核心估计方法为自适应随机梯度下降（SGD）算法，通过随机近似与自适应步长实现大规模矩阵的快速求解，显著降低内存消耗。算法层面实现了对百万级细胞数据的可扩展计算，并在矩阵重构保真度和生物信号提取精度上优于非负矩阵分解等现有方法。数值实验与真实数据表明该算法在执行时间与内存占用上具有显著优势，并提供了开源R包sgdGMF。对您有用：该工作直接契合您在统计计算（数值方法与算法）方面的兴趣，其自适应SGD在广义矩阵分解中的实现细节及大规模矩阵运算的内存优化策略，对高维数据计算具有迁移价值。
- **关键技术**: `generalized matrix factorization`, `adaptive stochastic gradient descent`, `exponential dispersion family`, `large-scale matrix computation`, `single-cell RNA-seq dimensionality reduction`
- **为什么对您有用**: 直接契合您在统计计算（数值方法与算法）方面的兴趣，其自适应SGD算法在广义矩阵分解中的实现细节及大规模矩阵运算的内存优化策略，对高维数据计算具有迁移价值。

## 流行病学  *(epidemiology, 4 篇)*

### 1. [10.1093/biostatistics/kxag008](https://doi.org/10.1093/biostatistics/kxag008) — A flexible class of latent variable models for the analysis of antibody response data
- **作者**: Emanuele Giorgi, Jonas Wallin
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在抗体浓度数据分析中，传统方法基于有限混合模型将个体二分为血清阴性/阳性；本文提出连续潜变量框架，将免疫状态表示为从最小到最强免疫激活的连续潜血清反应性（latent seroreactivity），放松了二分假设。该框架可容纳机制型与回归型模型设定，有限混合模型为其特例。作为计算贡献，作者提出基于L₂距离的估计量替代MLE，大幅降低计算成本，并建立其一致性。疟疾血清学案例展示了框架跨年龄联合分析并适应传播模式变化的能力。L₂估计量的计算效率与一致性证明对统计计算方向有参考价值；连续潜变量建模思路可迁移至流行病学因果推断中处理潜混杂与测量误差的设定。
- **关键技术**: `L2 minimum distance estimation`, `latent variable model`, `finite mixture model`, `consistency proof`, `serology data modeling`
- **为什么对您有用**: L₂估计量作为MLE的高效替代连接统计计算方向；连续潜变量框架可迁移至流行病学因果推断中处理潜混杂/测量误差的设定，对您epidemiology secondary interest中的applied causal work有方法借鉴价值。

### 2. [10.1093/biostatistics/kxaf049](https://doi.org/10.1093/biostatistics/kxaf049) — A two-stage approach for segmenting spatial point patterns applied to multiplex imaging
- **作者**: Alvin Sheng, Brian J Reich, Ana-Maria Staicu, Santhoshi N Krishnan, Arvind Rao, Timothy L Frankel
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 在多重成像的空间点模式分割问题中，目标是将组织图像按肿瘤免疫学中的不同空间排列模式（regime）进行分区，假设同一 regime 内细胞空间依赖结构同质。方法分两阶段：第一阶段估计局部强度和配对相关函数，并通过协方差函数的谱分解对配对相关函数降维；第二阶段在贝叶斯层次模型中对降维后的估计量进行聚类，聚类标签具有空间依赖性（Potts 模型先验），通过 MCMC 联合估计聚类分配及各聚类的空间特征并量化不确定性。模拟和胰腺组织多重免疫荧光图像应用展示了方法性能。谱分解降维与随机矩阵理论有微弱联系，但整体方法（空间点模式、贝叶斯聚类）与您的核心兴趣重叠有限；对流行病学空间数据建模有参考价值。
- **关键技术**: `spatial point pattern`, `pair correlation function`, `spectral decomposition of covariance`, `Bayesian hierarchical clustering`, `Potts model prior`, `MCMC`
- **为什么对您有用**: 谱分解降维与 RMT 有微弱联系；胰腺肿瘤组织的空间点模式应用属于流行病学二次兴趣，但方法核心（贝叶斯空间聚类）与您的因果推断/半参数/效率理论方向重叠有限，阅读收益偏低。

### 3. [10.1093/biostatistics/kxag002](https://doi.org/10.1093/biostatistics/kxag002) — Dynamic case-control sampling for rapid estimation of vaccine effectiveness against an emerging infectious disease variant
- **作者**: Taylor M Fortnam, Laura C Chambers, Alyssa Bilinski, Ewa King, Richard C Huard, Ellen Amore et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 0/10 · novelty: `application`
- **摘要**: 在新发传染病变异株快速出现的流行病学监测设定下，目标是利用动态累积的实时数据估计疫苗有效性（VE）。方法采用动态病例对照采样（dynamic case-control sampling），将新变异株感染者作为“病例”，旧变异株感染者作为“对照”，估计相对VE。随后结合旧变异株的已知VE（通常来自大型传统研究），通过桥接假设推断新变异株的绝对VE。该方法仅需部分病例的测序数据，在 Omicron BA.1/BA.2 数据上的实证结果显示其估计值与传统方法可比，但标准误因样本量较小而有所增加。对您可能有用：作为流行病学因果推断的应用案例，展示了如何在部分测序（选择偏倚/missing data）下利用桥接假设进行VE估计，可为相关监测数据集的分析提供应用参考。
- **关键技术**: `dynamic case-control sampling`, `test-negative design`, `vaccine effectiveness estimation`, `bridging assumption`
- **为什么对您有用**: 属于流行病学因果推断的应用工作，展示了在部分测序（选择偏倚）下利用桥接假设估计VE的实用策略，可为处理类似监测数据集提供应用参考。

### 4. [10.1093/biostatistics/kxaf052](https://doi.org/10.1093/biostatistics/kxaf052) — Risk functions with outcome measurement error
- **作者**: Jessie K Edwards, Stephen R Cole, Paul N Zivich, Benjamin Ackerman, Sonia Napravnik, Heather Henderson et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在右删失生存设定下，目标估计量为存在结局测量误差（漏报、误报、时间错位）时的死亡率风险与生存函数，关键假设为可获取内部或外部验证数据以估计误差参数。本文将经典 Rogan-Gladen 估计量扩展至右删失场景，通过验证子研究估计灵敏度与特异度，对风险函数进行校正；当验证子研究存在选择偏倚（高死亡风险者更易入组）时，模拟显示方法仍表现稳健。实证分析基于 2001–2022 年 UNC CFAR HIV 临床队列，校正死亡登记链接不完整/不正确导致的结局误差。该方法亦可作为定量偏倚分析工具使用。对您而言，该文提供了流行病学队列中结局测量误差的校正框架，与您对 sensitivity analysis 和流行病学应用因果方法的兴趣直接相关，且 HIV 队列数据结构具有参考价值。
- **关键技术**: `Rogan-Gladen estimator`, `outcome measurement error correction`, `validation substudy design`, `quantitative bias analysis`, `right-censored survival data`
- **为什么对您有用**: 结局测量误差的校正与您 primary interest 中的 sensitivity analysis 直接相关，同时 HIV 队列实证属于 epidemiology secondary interest；方法虽非高阶理论，但验证数据框架可迁移至您关注的因果推断设定中。

## 其他  *(other, 1 篇)*

### 1. [10.1093/biostatistics/kxaf051](https://doi.org/10.1093/biostatistics/kxaf051) — Shortcomings of deep learning for distributional predictors: a note
- **作者**: Bonnie B Smith, Abhirup Datta, Brian Caffo
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 3/10
- **摘要**: {
  "topic": "nonparam_semipara",
  "summary_zh": "在高维同类型预测变量（如个体内重复测量）的回归设定下，目标是学习在输入向量置换不变性假设下结果与预测变量的映射关系。作者比较了无结构深度神经网络与显式嵌入置换不变性的"有序预测变量神经网络"（ordered predictors neural network），后者通过排序或聚合将不变性结构化入网络架构。模拟结果表明，无结构方法预测误差更高，而利用不变性的方法一致更优。在神经贝叶斯估计（neural Bayes estimation）框架中，有序预测变量网络可产生显著更精确（lower MSE）的点估计量。核心建议是：当置换不变性已知或可疑时，应采用能利用该不变性的模型而非无结构深度学习。对您有用：该文展示了利用已知结构不变性提升估计效率的思路，与您在 semiparametric efficiency 和 statistical computing 上的兴趣相关——在神经贝叶斯估计中通过不变性约束获得更精确估计量的逻辑，可迁移到其他有结构约束的半参数/非参数问题。",
  "key_techniques": [
    "permutation-invariant neural network",
    "neural Bayes estimation",
    "order


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

