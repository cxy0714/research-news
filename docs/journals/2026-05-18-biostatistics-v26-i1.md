# Biostatistics — Vol 26  Issue 1  ·  2026-05-18

- 共 18 篇 · Biostatistics

## 因果推断  *(causal_inference, 5 篇)*

### 1. [10.1093/biostatistics/kxaf042](https://doi.org/10.1093/biostatistics/kxaf042) — Instrumental variable approach to estimating individual causal effects in N-of-1 trials: application to ISTOP study
- **作者**: Kexin Qu, Christopher H Schmid, Tao Liu
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在 N-of-1 试验（单一个体多次交叉）的纵向因果推断框架下，目标是在存在不依从性、二值处理/结局（非折叠性）和序列相关时估计个体因果效应。基于潜在处理与结果路径定义了连续暴露效应和观测行为效应两种 estimand。采用随机化分配作为工具变量（IV），构建两阶段参数贝叶斯 IV 模型系统进行估计。通过潜在结构模型建模混杂机制并结合贝叶斯后验推断，规避了 odds ratio 的非折叠性与非一致性问题，同时处理了重复测量的自相关。模拟显示相较于 ITT、PP 和 AT 方法，该贝叶斯 IV 方法大幅降低了偏差并提升了覆盖率。实证应用于 I-STOP-AFib 研究评估酒精对房颤的个体效应。对您有用：直接连接您感兴趣的纵向因果推断与 IV 方法，并提供了流行病学（房颤）数据集的应用范例。
- **关键技术**: `Bayesian instrumental variable`, `N-of-1 trial`, `non-collapsibility`, `latent structural model`, `longitudinal autocorrelation`, `potential outcome path`
- **为什么对您有用**: 直接连接您 primary interest 中的因果推断（IV、longitudinal）以及 secondary interest 中的流行病学应用与数据集，展示了在纵向 N-of-1 设计下处理非依从与非折叠性的贝叶斯 IV 实操方案。

### 2. [10.1093/biostatistics/kxaf031](https://doi.org/10.1093/biostatistics/kxaf031) — Identification and estimation of mediational effects of longitudinal modified treatment policies
- **作者**: Brian Gilbert, Katherine Hoffman, Nicholas Williams, Kara Rudolph, Edward J Schenck, Iván Díaz
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在纵向连续处理、时依混杂与中介的设定下，本文研究纵向修正处理策略（LMTP）中介效应的识别与估计。基于非参数结构方程模型（NPSEM）完成识别，提出基于双重稳健伪结果的交叉拟合序贯回归估计量。该方法无需限制性参数假设，所得估计量在半参数模型下达到有效界，具有 n^{-1/2}-CAN 性质。实证分析揭示了“不一致中介”现象（直接与间接效应方向相反），并在 COVID-19 机械通气与急性肾损伤的流行病学数据中验证方法。对您有用：该文将 longitudinal CI 与 mediation 结合，给出了 DR/Cross-fitting 下的半参数有效估计，直接推进您在纵向因果中介及效率理论的兴趣，同时其流行病学应用数据集具有参考价值。
- **关键技术**: `longitudinal modified treatment policies`, `causal mediation analysis`, `doubly robust pseudo-outcomes`, `cross-fitted sequential regression`, `semiparametric efficiency`, `nonparametric structural equation model`
- **为什么对您有用**: 直接推进您在纵向因果推断与中介分析（primary interest）的兴趣，提供了连续/纵向处理下 DR 伪结果与 cross-fitting 的半参数有效估计框架，且其 COVID-19 流行病学应用（secondary interest）具有数据集参考价值。

### 3. [10.1093/biostatistics/kxaf040](https://doi.org/10.1093/biostatistics/kxaf040) — Multi-study <i>R</i> -learner for estimating heterogeneous treatment effects across studies using statistical machine learning
- **作者**: Cathy Shyr, Boyu Ren, Prasad Patil, Giovanni Parmigiani
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在多研究设定下估计异质性处理效应(HTE/CATE)，目标是在允许研究间异质性（CATE、结果模型、倾向得分机制不同）的半参数框架下进行有效估计。提出多研究 R-learner，通过数据自适应目标函数结合跨研究的干扰参数估计与特定研究的 CATE 估计，利用成员概率实现跨研究信息借用。该方法基于 R-learner 的正交化思想，放松了传统多研究方法要求三个核心函数跨研究同质的假设。在序列估计框架下，证明了该估计量具有渐近正态性，且当处理分配机制存在研究间异质性时，比标准 R-learner 更有效。理论和癌症 RCT/观察性数据实证表明，该方法在异质性存在时表现更优。对您有用：该文将 R-learner 正交化框架扩展至多研究设定并推导了渐近正态性与效率提升，直接契合您在因果推断估计与效率理论方面的兴趣，且其处理多源数据异质性的思路可迁移至流行病学多队列因果分析。
- **关键技术**: `R-learner`, `heterogeneous treatment effect (CATE)`, `multi-study learning`, `orthogonalization`, `asymptotic normality`, `series estimation`
- **为什么对您有用**: 直接契合因果推断(CATE估计)与效率理论(渐近正态与效率提升)的核心兴趣；多研究异质性处理思路对流行病学多队列数据的因果推断应用有直接迁移价值。

### 4. [10.1093/biostatistics/kxaf043](https://doi.org/10.1093/biostatistics/kxaf043) — Stratification-based instrumental variable analysis framework for nonlinear effect analysis
- **作者**: Haodong Tian, Ashish Patel, Stephen Burgess
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在连续暴露的非线性因果效应设定下，针对传统 IV 回归或控制函数方法在未测混杂下功效低或结论误导的问题，本文提出基于分层的 IV 框架。该框架包含三个核心要素：分层法构造保持 IV 核心假设的子样本；标量-函数/标量-标量模型连接局部层特异性信息与全局效应估计；单效应求和法进行效应估计。此方法无需严格参数模型假设，支持因果效应函数识别及变点检测。模拟表明在弱工具变量下，该方法预测效应形状优于传统非线性 IV 方法。实证利用 UK Biobank 数据与孟德尔随机化评估饮酒对收缩压的非线性效应并检测到阈值。对您而言，该工作为 IV 设定下的非线性因果识别与变点检测提供了新思路，且 UK Biobank 的流行病学应用具有数据集参考价值。
- **关键技术**: `instrumental variable`, `stratification approach`, `scalar-on-function model`, `sum-of-single-effects`, `Mendelian randomization`, `change-point detection`
- **为什么对您有用**: 直接关联您 primary interest 中的因果推断（IV 方法），特别是处理非线性效应与弱工具变量问题；同时关联 secondary interest 中的流行病学（UK Biobank 数据集与孟德尔随机化应用）。

### 5. [10.1093/biostatistics/kxaf046](https://doi.org/10.1093/biostatistics/kxaf046) — Counterfactual fairness for small subgroups
- **作者**: Solvejg Wastvedt, Jared D Huling, Julian Wolfson
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在风险预测模型的算法公平性设定下，针对小规模受保护子群在存在治疗混杂时的反事实公平性评估问题。本文基于反事实公平框架，提出新的跨群借力估计量以利用更大样本量提升精度。同时引入一种新颖的数据借用方法，整合仅含协变量和群组信息而缺失结局与预测值的外部数据。实证表明该方法在小子群下相比现有技术显著降低了方差，并在 COVID-19 风险预测数据中验证了实用性。对您有用：该文将因果推断的反事实框架与外部数据整合结合，对您在因果推断（处理治疗混杂的反事实估计）和流行病学应用（COVID-19数据集）的交叉研究有方法迁移与数据集参考价值。
- **关键技术**: `counterfactual fairness`, `treatment confounding`, `cross-group estimation`, `data borrowing`, `external data integration`
- **为什么对您有用**: 将因果推断的反事实框架与外部数据整合结合，对您在因果推断（处理治疗混杂的反事实估计）和流行病学应用（COVID-19数据集）的交叉研究有方法迁移与数据集参考价值。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1093/biostatistics/kxaf047](https://doi.org/10.1093/biostatistics/kxaf047) — While-alive regression analysis of composite survival endpoints
- **作者**: Xi Fang, Hajime Uno, Fan Li
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在含终止事件的复合生存终点设定下，本文研究 exposure-weighted while-alive 度量的回归框架，目标是估计协变量对广义 while-alive 损失率的时变关联效应。方法采用 B-spline 建模协变量与广义 while-alive 损失率之间的时变关联，同时适用于独立数据与聚类相关数据。作者在两种数据设定下推导了回归估计量的渐近性质（一致性与渐近正态性），并通过模拟研究有限样本表现。实证分析应用于两个随机对照试验数据集，方法已实现为 R 包 WAreg。对您而言，该文的样条半参数回归框架与渐近理论推导与 semiparametric theory 兴趣有一定方法重叠，且临床终点回归的应用场景对 epidemiology 方向有数据集与模型参考价值。
- **关键技术**: `spline regression`, `while-alive cumulative frequency`, `asymptotic normality`, `cluster-correlated data`, `composite survival endpoint`
- **为什么对您有用**: 样条半参数回归的渐近理论推导与您的 semiparametric theory 兴趣有方法重叠；临床终点回归的应用场景对 epidemiology 方向提供数据集与模型参考，但方法学 novelty 偏增量式。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1093/biostatistics/kxae046](https://doi.org/10.1093/biostatistics/kxae046) — Testing for a difference in means of a single feature after clustering
- **作者**: Yiqun T Chen, Lucy L Gao
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在对观测数据进行聚类后检验两个估计簇在某特征上的均值差异时，经典假设检验因选择性偏差会导致第一类错误膨胀。本文针对层次聚类或k-means聚类得到的簇对，提出一种新的单特征均值差异检验方法。核心机制基于选择性推断框架，通过刻画聚类选择事件的截断分布来构建条件检验统计量。理论上，该检验在有限样本下严格控制选择性第一类错误率，且具备高效计算性。模拟和单细胞RNA测序数据验证了其有效性和功效。对您有用：该工作直接推进了您在数学统计（假设检验）方向的兴趣，展示了选择性推断如何修正数据窥探偏差，其有限样本保证和计算策略对后续研究有借鉴意义。
- **关键技术**: `selective inference`, `selective Type I error`, `post-selection inference`, `truncated distribution`, `hierarchical clustering`, `k-means clustering`
- **为什么对您有用**: 直接对应您在数学统计（假设检验）方向的兴趣；展示了选择性推断如何修正聚类后检验的偏差，其有限样本保证和计算策略对处理数据窥探问题具有方法学借鉴价值。

### 2. [10.1093/biostatistics/kxaf050](https://doi.org/10.1093/biostatistics/kxaf050) — High-dimensional inference for functional regression with an application to the Alzheimer’s disease magnetoencephalography study
- **作者**: Huaqing Jin, Fei Jiang
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在高维函数线性回归设定下，针对函数型协变量提出高维假设检验（HDHT）框架，旨在克服传统变量选择的不稳健性及特征提取的信息损失。核心方法构建了针对高维函数系数的检验统计量，通过去偏推断策略实现有效推断，并建立其渐近零分布与功效性质。理论分析涵盖了高维函数空间中的收敛率与检验水平控制，避免了传统选择方法对调参的过度敏感。模拟验证了检验的 size 和 power，应用于阿尔茨海默病（AD）脑磁图（MEG）数据，识别出19个关键脑区。对您有用：直接关联您的高维统计推断与假设检验兴趣，提供了函数型数据下高维检验的具体理论，且 AD MEG 数据集对流行病学应用方向有数据价值。
- **关键技术**: `high-dimensional hypothesis testing`, `functional linear regression`, `debiased inference`, `asymptotic null distribution`, `MEG data analysis`
- **为什么对您有用**: 直接关联您的高维统计推断与假设检验（hypothesis testing）兴趣，提供了函数型数据下高维检验的具体理论；同时其 AD MEG 数据集对流行病学（epidemiology）应用方向具有数据集价值。

### 3. [10.1093/biostatistics/kxaf045](https://doi.org/10.1093/biostatistics/kxaf045) — Determining vaccine responders in the presence of baseline immunity using single-cell assays and paired control samples
- **作者**: Zhe Chen, Siyu Heng, Asa Tapley, Stephen De Rosa, Bo Zhang
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 在疫苗免疫原性评估中，目标是在存在基线免疫与批次效应的设定下，利用 ICS 单细胞配对（接种前后）数据识别疫苗应答者。作者提出一种整合配对对照样本的统计框架，校正不同时间点实验批次效应，避免将批次变异误判为疫苗应答。核心方法是对未调整 p 值分别施加最保守和最宽松的校正：maximally adjusted p-value 在所有与对照数据一致的批次效应下保证 Type I error 有效性；minimally adjusted p-value 仅施加使调整后 p 值不被对照数据否定的最小校正，二者共同提供 Type I error 与功效的平衡。方法应用于 CoVPN 3008 研究，识别 Omicron 感染与疫苗诱导 T 细胞应答。对您而言，该文在假设检验（配对 p 值校正框架）和流行病学应用（疫苗队列数据集）两个方向均有参考价值，批次效应下检验有效性的思路可迁移至其他配对实验设计。
- **关键技术**: `paired p-value adjustment`, `batch effect correction via paired controls`, `maximally adjusted p-value`, `minimally adjusted p-value`, `Type I error validity under nuisance variation`, `intracellular cytokine staining (ICS) analysis`
- **为什么对您有用**: 直接关联您 primary interest 中的假设检验（配对 p 值校正框架处理批次效应）以及 secondary interest 中的流行病学应用（CoVPN 疫苗队列数据集）；批次效应下保证检验有效性的思路可迁移至其他配对因果/纵向设定。

## 统计计算 / 算法  *(stat_computing, 3 篇)*

### 1. [10.1093/biostatistics/kxaf039](https://doi.org/10.1093/biostatistics/kxaf039) — Network generalized estimating equations for complexly correlated data with applications to cluster randomized trials
- **作者**: Tom Chen, Fan Li, Rui Wang
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在整群随机试验（CRT）设定下，本文提出 network GEE 框架以估计均值参数与复杂关联结构，核心假设为观测在重叠分组内局部可交换。方法通过网络概念参数化工作相关矩阵，涵盖多重可交换、移动平均及指数衰减等结构。针对大集群下 GEE 的计算瓶颈，作者开发了 networkGEE R 包实现高效数值求解，突破了现有软件的局限。模拟与华盛顿州加速伴侣治疗（阶梯楔形 CRT）数据验证了方法有效性。对您而言，其大规模相关矩阵的计算方案与软件实现直接对应统计计算兴趣，阶梯楔形 CRT 应用也与流行病学因果推断场景契合。
- **关键技术**: `network GEE`, `working correlation structure`, `local exchangeability`, `cluster randomized trials`, `stepped-wedge design`
- **为什么对您有用**: 大规模相关数据下 GEE 的数值计算与 R 包开发对应您的统计计算兴趣，同时阶梯楔形 CRT 的流行病学应用契合您对流行病学因果推断应用的关注。

### 2. [10.1093/biostatistics/kxaf029](https://doi.org/10.1093/biostatistics/kxaf029) — Bayesian scalar-on-tensor regression using the Tucker decomposition for sparse spatial modeling
- **作者**: Daniel A Spencer, Rene Gutierrez, Rajarshi Guhaniyogi, Russell T Shinohara, Raquel Prado, Alzheimer’s Disease Neuroimaging Initiative et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在 scalar-on-tensor 回归设定下，tensor 协变量维度极高且系数具有空间稀疏性，目标是在保留空间结构的同时高效估计 tensor 系数。本文提出基于 Tucker 分解的贝叶斯方法，将 tensor 系数分解为核心张量与因子矩阵的乘积，大幅减少自由参数数量，同时通过先验分布实现稀疏正则化以刻画空间稀疏特征。模拟实验表明该方法在估计精度和变量选择上优于近期提出的 tensor 回归方法。ADNI 神经影像数据分析展示了其在实际高维空间数据中的推断优势。对您而言，Tucker 分解的参数降维策略和贝叶斯稀疏正则化方案可迁移至统计计算中 tensor 相关算法设计，尤其在高维 tensor 协变量场景下具有参考价值。
- **关键技术**: `Tucker tensor decomposition`, `Bayesian sparse regularization`, `scalar-on-tensor regression`, `low-rank parameter reduction`, `spatial sparsity modeling`
- **为什么对您有用**: 直接连接您 primary interest 中统计计算的 tensor 方向，Tucker 分解降维与稀疏正则化的结合策略可迁移至高维 tensor 推断算法设计；ADNI 数据集对流行病学应用也有参考价值。

### 3. [10.1093/biostatistics/kxaf038](https://doi.org/10.1093/biostatistics/kxaf038) — Assessing treatment efficacy for interval-censored endpoints using multistate semi-Markov models fit to multiple data streams
- **作者**: Raphaël Morsomme, C Jason Liang, Allyson Mateja, Dean A Follmann, Meagan P O’Brien, Chenguang Wang et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在多流区间删失数据设定下，本文研究多状态半马尔可夫模型的治疗效应评估，目标参数包括无症状感染保护效力及病毒脱落持续时间等。核心方法采用蒙特卡洛期望最大化（MCEM）算法结合重要性抽样，解决间歇性观测下边际似然不可解的计算难题。该算法相比现有方法实现了显著的计算效率提升，并允许在数据粗化复杂时拟合半参数模型。实证基于 REGEN-2069 新冠抗体预防试验，发现 REGEN-COV 降低了无症状感染风险与病毒脱落时间。对您而言，本文的 MCEM+重要性抽样计算方案可为复杂删失结构下的似然计算提供算法参考（统计计算），同时其流行病学多状态疗效评估框架对应用因果推断有借鉴价值。
- **关键技术**: `multistate semi-Markov model`, `Monte Carlo EM algorithm`, `importance sampling`, `interval censoring`, `semi-parametric model`
- **为什么对您有用**: 匹配您的统计计算兴趣（MCEM与重要性抽样解决不可解似然），同时提供流行病学临床试验数据集与多状态疗效评估的应用因果场景。

## 流行病学  *(epidemiology, 4 篇)*

### 1. [10.1093/biostatistics/kxaf037](https://doi.org/10.1093/biostatistics/kxaf037) — Meta-analysis models with group structure for pleiotropy detection at gene and variant level using summary statistics from multiple datasets
- **作者**: Pierre-Emmanuel Sugier, Yazdan Asgari, Mohammed Sedki, Thérèse Truong, Benoit Liquet
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在多表型 GWAS summary statistics 的 meta-analysis 设定下，目标是检测基因与变异水平的多效性（pleiotropy），并利用基因-变异的嵌套群组结构进行选择。本文提出 MPSG 方法，采用带群组结构惩罚（group penalty）的多变量 meta-analysis 模型，以同时选择相关变异与基因。算法层面使用 ADMM (Alternating Direction Method of Multipliers) 求解该惩罚优化问题。与 GCPBayes、PLACO、ASSET 等逐个检验的现有方法相比，MPSG 能同时利用全部遗传信息并保留层级结构；实证应用于乳腺癌与甲状腺癌的多效性基因识别。对您而言，该工作涉及高维惩罚回归与 ADMM 算法实现（统计计算），且多效性检测与因果推断中 IV 的 exclusion restriction 假设紧密相关，可作流行病学数据集与方法迁移的参考。
- **关键技术**: `penalized multivariate meta-analysis`, `group structure penalty`, `ADMM`, `GWAS summary statistics`, `pleiotropy detection`
- **为什么对您有用**: 涉及高维惩罚回归与 ADMM 算法（统计计算），且多效性检测与因果推断 IV 的 exclusion restriction 假设相关，可作流行病学数据集与方法迁移参考。

### 2. [10.1093/biostatistics/kxaf034](https://doi.org/10.1093/biostatistics/kxaf034) — Markov switching zero-inflated space-time multinomial models for comparing multiple infectious diseases
- **作者**: Dirk Douwes-Schultz, Alexandra M Schmidt, Laís Picinini Freitas, Marilia Sá Carvalho
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文针对多种传染病共循环的时空计数数据，提出马尔可夫转换零膨胀多项式模型，解决多疾病在空间、时间及疾病间的相关性及零膨胀问题。模型假设一种基线疾病始终存在，其他疾病通过耦合马尔可夫链在存在与缺失状态间切换，以捕捉长期缺失、疾病交互及空间传播特征。对于处于存在状态的疾病，采用自回归多项式模型刻画其传播强度差异及协变量（如温度）关联。推断采用基于联合采样所有未知存在指标的贝叶斯 MCMC 方法。实证分析了里约热内卢登革热、寨卡和基孔肯雅热的三重流行数据。对您而言，该文主要提供了一套多疾病时空流行病学数据集，但方法学上属于参数贝叶斯建模，与您关注的半参数/因果推断理论距离较远。
- **关键技术**: `Markov switching model`, `zero-inflated model`, `spatio-temporal autoregressive model`, `Bayesian MCMC`, `multinomial model`
- **为什么对您有用**: 该文属于流行病学应用，提供了里约热内卢三种蚊媒传染病时空数据集，但方法学为纯参数贝叶斯建模，对您核心的因果推断或效率理论贡献极小，仅作数据集参考。

### 3. [10.1093/biostatistics/kxaf028](https://doi.org/10.1093/biostatistics/kxaf028) — Bayesian mapping of mortality clusters
- **作者**: Andrea Sottosanti, Enrico Bovo, Pietro Belloni, Giovanna Boccuzzo
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 1/10 · novelty: `application`
- **摘要**: 本文针对多死因空间死亡率聚类问题，提出多变量贝叶斯模型 perla，旨在同时识别聚类的空间边界与驱动聚类的特定疾病。模型利用多项分布的 stick-breaking 构造将空间结构纳入聚类概率，并采用 global-local shrinkage prior 筛选死亡率显著变化的疾病、排除无信息疾病。后验推断采用 MCMC 算法，几乎所有参数均有闭式 Gibbs sampling 更新，避免了复杂调参。实证基于意大利 ULSS6 Euganea 地区和美国县级死亡率数据验证了方法有效性。对您而言，该文提供了流行病学空间数据集，且闭式 Gibbs 采样技巧对统计计算（MCMC 算法设计）有参考价值，但方法学理论新颖性有限。
- **关键技术**: `multivariate Bayesian model`, `stick-breaking formulation`, `global-local shrinkage prior`, `spatial clustering`, `Gibbs sampling`
- **为什么对您有用**: 提供了流行病学（多死因空间映射）的数据集与应用案例；其闭式 Gibbs 采样设计对您在统计计算（MCMC 算法）方面的兴趣有一定参考价值，但缺乏因果推断或高维渐近理论贡献。

### 4. [10.1093/biostatistics/kxaf048](https://doi.org/10.1093/biostatistics/kxaf048) — Assessing spatial disparities: a Bayesian linear regression approach
- **作者**: Kyle Wu, Sudipto Banerjee
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 本文在区域聚合空间流行病学数据的设定下，研究如何检测相邻区域间的空间健康差异，核心挑战在于空间差异的定义与稳健的概率推断。作者在贝叶斯线性回归框架中引入空间自回归，以实现基于模型的空间差异检测。方法的关键在于推导出可利用的解析易处理性（analytical tractability），从而大幅加速后验计算。模拟实验基于美国县级地图，实证分析采用 IHME 肺癌死亡率数据。对您而言，该文提供了流行病学空间数据集（IHME）及贝叶斯空间自回归的计算加速技巧，可作应用与计算参考。
- **关键技术**: `Bayesian linear regression`, `spatial autoregression`, `analytical tractability`, `probabilistic inference for disparities`
- **为什么对您有用**: 该文属于流行病学应用，提供了美国县级空间数据集（IHME）及贝叶斯空间自回归的解析加速计算技巧；虽然理论深度不及您关注的半参数/效率界，但其计算加速思路对统计计算子方向有一定参考价值。

## 其他  *(other, 2 篇)*

### 1. [10.1093/biostatistics/kxaf044](https://doi.org/10.1093/biostatistics/kxaf044) — Decomposition of longitudinal disparities: an application to the fetal growth-singletons study
- **作者**: Sang Kyu Lee, Seonjin Kim, Mi-Ok Kim, Katherine L Grantz, Hyokyoung G Hong
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 6/10
- **摘要**: {
  "topic": "epidemiology",
  "summary_zh": "本文将经典 Peters–Belson 分解扩展至纵向设定，目标是在给定 modifier 与协变量交互作用的框架下，将不同人群间的健康差异分解为三部分：(i) 协变量条件分布差异所致（在 modifier 共同分布下评估）；(ii) modifier 分布差异及其与协变量交互作用所致；(iii) 无法由观测协变量解释的残余差异。方法核心在于不将前两部分合并为单一"已解释差异"，而是分别刻画其随时间演变的模式，从而区分与 modifier 关联和无关的纵向差异路径。估计方面沿用回归拟合与反事实预测的 Oaxaca–Blainer/Peters–Belson 思路，在纵向重复测量下进行成分分解。实证分析基于胎儿生长纵向队列，展示不同种族/族裔群体在孕期胎儿发育轨迹上的差异分解。对您而言，该文的纵向差异分解框架与纵向因果推断（特别是 mediation / decomposition 型 identification）有方法学交叉，且提供了流行病学队列数据集的实证参考。",
  "key_techniques": [
    "Peters-Belson decomposition",
    "longitudinal disparity decomposition",
    "modifi

### 2. [10.1093/biostatistics/kxaf012](https://doi.org/10.1093/biostatistics/kxaf012) — Addressing the mean–variance relationship in spatially resolved transcriptomics data with <i>spoon</i>
- **作者**: Kinnary Shah, Boyi Guo, Stephanie C Hicks
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 1/10 · novelty: `application`
- **摘要**: 在空间转录组学 (SRT) 数据中，目标是识别空间变异基因 (SVGs)，现有方法多基于 P 值或空间方差比例排序，但忽略了 log 变换引入的技术偏差。本文指出 SRT 数据中存在均值-方差关系被 log 变换破坏的现象：高表达基因的计数方差大，但 log 变换后方差反而偏低。为此提出 spoon 框架，利用经验贝叶斯 (empirical Bayes) 技术校正此偏差，恢复合理的均值-方差趋势，从而更准确地优先排序 SVGs。仿真与真实 SRT 数据验证了该方法在偏差校正和 SVG 排序上的性能提升。对您而言，本文方法学 novelty 偏向应用，但经验贝叶斯校正计数数据方差稳定化的思路在处理其他高维计数数据时或可借鉴。
- **关键技术**: `empirical Bayes`, `mean-variance relationship`, `variance stabilization`, `log-transformation bias`, `spatially resolved transcriptomics`
- **为什么对您有用**: 本文主要针对空间转录组学应用，与您关注的因果推断、高维理论或效率理论等核心方向距离较远，但经验贝叶斯校正方差的技术在处理其他高维计数数据的方差稳定化时或可迁移借鉴。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

