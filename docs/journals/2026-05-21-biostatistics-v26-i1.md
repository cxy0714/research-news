# Biostatistics — Vol 26  Issue 1  ·  2026-05-21

- 共 18 篇 · Biostatistics

## 因果推断  *(causal_inference, 6 篇)*

### 1. [10.1093/biostatistics/kxaf031](https://doi.org/10.1093/biostatistics/kxaf031) — Identification and estimation of mediational effects of longitudinal modified treatment policies
- **作者**: Brian Gilbert, Katherine Hoffman, Nicholas Williams, Kara Rudolph, Edward J Schenck, Iván Díaz
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 10/10 · novelty: `new_method`
- **摘要**: 本文在纵向连续处理、时依混杂与中介的设定下，研究纵向修正处理策略（LMTP）中介效应的识别与估计。基于非参数结构方程模型（NPSEM）完成识别，并构造了基于双重稳健（DR）伪结果的交叉拟合序贯回归估计量。该估计量避免了限制性参数假设，达到了半参数有效界，且具有 n^{-1/2}-相合渐近正态（CAN）性质。实证分析探讨了 COVID-19 有创通气对生存率的影响，揭示了直接与间接效应方向相反的“不一致中介”现象。对您有用：直接推进了您关注的纵向因果中介与半参数效率理论，其 LMTP 下 DR 伪结果的构造思路可迁移至其他连续/纵向处理设定。
- **关键技术**: `longitudinal modified treatment policies`, `doubly robust pseudo-outcomes`, `cross-fitted sequential regression`, `nonparametric structural equation model`, `semiparametric efficiency bound`
- **为什么对您有用**: 直接对应您 primary interest 中的纵向因果中介与半参数效率理论，其针对连续/纵向处理的 DR 伪结果与 cross-fitting 构造为复杂纵向因果推断提供了可迁移的估计框架。

### 2. [10.1093/biostatistics/kxaf040](https://doi.org/10.1093/biostatistics/kxaf040) — Multi-study <i>R</i> -learner for estimating heterogeneous treatment effects across studies using statistical machine learning
- **作者**: Cathy Shyr, Boyu Ren, Prasad Patil, Giovanni Parmigiani
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在多研究（multi-study）设定下，目标是估计异质性处理效应（CATE），当研究间在 CATE 本身、条件期望结局 μ₀ 和处理分配机制上均存在异质性时，传统多研究方法的一致性假设不再成立。本文提出 multi-study R-learner，将 R-learner 推广至多研究场景，通过 data-adaptive objective function 以 membership probabilities 加权组合跨研究 nuisance 估计与研究特定 CATE。方法在 series estimation 框架下被证明渐近正态，且当处理分配机制存在跨研究异质性时，比标准 R-learner 更高效（效率增益来源于跨研究 nuisance 的信息借入）。实证部分使用癌症 RCT 与观察性数据验证了方法在异质性存在时的优势。对您有用：该工作直接连接 causal inference 的 CATE 估计与 efficiency theory（R-learner 本质基于 orthogonal score / Robinson 分解），多研究信息借入的效率提升思路可迁移至您关注的 proximal CI 或 IV 的多数据源融合问题。
- **关键技术**: `R-learner`, `multi-study learning`, `orthogonal score`, `membership probability weighting`, `series estimation`, `asymptotic normality`
- **为什么对您有用**: 直接推进 causal inference 中 CATE 估计的 efficiency theory（R-learner 基于 orthogonal score，多研究借信息提升效率），多研究异质性处理思路可迁移至您关注的 proximal CI / IV 的多数据源融合设定。

### 3. [10.1093/biostatistics/kxaf042](https://doi.org/10.1093/biostatistics/kxaf042) — Instrumental variable approach to estimating individual causal effects in N-of-1 trials: application to ISTOP study
- **作者**: Kexin Qu, Christopher H Schmid, Tao Liu
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在 N-of-1 试验（单一个体多次交叉）设定下，本文旨在估计个体因果效应，面临不完美依从性、二值变量导致的 OR 不可折叠性及序列自相关三大挑战。作者构建了基于潜在处理路径与结果路径的因果框架，定义了连续暴露效应与观测行为效应两种 estimand。方法上，以随机化分配为工具变量（IV），建立包含潜在结构模型的双参数贝叶斯 IV 系统。该模型通过显式建模混杂机制与贝叶斯后验推断，规避了非折叠性与非一致性问题，并引入自相关结构刻画纵向重复测量。模拟表明，相比 ITT、PP 和 AT 方法，该贝叶斯 IV 估计大幅降低偏差并提升覆盖率；实证应用于 I-STOP-AFib 数据评估酒精对房颤的个体效应。对您有用：提供了一个在纵向 N-of-1 设计下结合 IV 与贝叶斯结构方程处理依从性与非折叠性的具体范式，且附带流行病学真实数据集。
- **关键技术**: `Bayesian instrumental variable`, `N-of-1 trial causal framework`, `non-collapsibility adjustment`, `latent structural model`, `autocorrelated longitudinal data`
- **为什么对您有用**: 直接涉及您 primary interest 中的因果推断（IV、纵向数据），同时属于 secondary interest 流行病学领域的应用因果工作，提供了处理依从性与非折叠性的贝叶斯 IV 范式及真实数据集。

### 4. [10.1093/biostatistics/kxaf043](https://doi.org/10.1093/biostatistics/kxaf043) — Stratification-based instrumental variable analysis framework for nonlinear effect analysis
- **作者**: Haodong Tian, Ashish Patel, Stephen Burgess
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在连续暴露的非线性因果效应分析中，传统 IV 回归或控制函数方法在存在未测量混杂时面临统计功效低或结论误导的问题，本文提出基于分层（Stratification）的 IV 框架以放松强参数假设。该框架包含三个核心“S”要素：(i) 分层方法，在 IV 核心假设成立的总体子样本中构建层；(ii) Scalar-on-function 与 Scalar-on-scalar 模型，将局部层特异性信息连接至全局效应估计；(iii) Sum-of-single-effects 估计方法。此框架无需严格参数模型假设即可估计效应函数，并能识别因果效应的变点或阈值。仿真表明在弱工具变量设定下，该方法在预测效应形状上优于现有非线性 IV 方法，并能准确估计效应函数与变点。实证部分利用 UK Biobank 数据与孟德尔随机化分析了饮酒对收缩压的非线性因果效应，检测到阈值效应。对您有用：该文为非线性 IV 估计提供了避免强参数假设的半参数分层思路，且 UK Biobank 的 MR 应用对流行病学因果推断有直接参考价值。
- **关键技术**: `instrumental variable analysis`, `nonlinear causal effect`, `stratification approach`, `scalar-on-function model`, `sum-of-single-effects`, `Mendelian randomization`
- **为什么对您有用**: 直击您 primary interest 中的因果推断（IV 方法）与 secondary interest 中的流行病学（MR 应用与 UK Biobank 数据集）；其分层估计非线性效应的思路放松了传统 IV 的参数假设，为半参数/非参数 IV 估计提供了可迁移的新框架。

### 5. [10.1093/biostatistics/kxaf044](https://doi.org/10.1093/biostatistics/kxaf044) — Decomposition of longitudinal disparities: an application to the fetal growth-singletons study
- **作者**: Sang Kyu Lee, Seonjin Kim, Mi-Ok Kim, Katherine L Grantz, Hyokyoung G Hong
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文将经典 Peters–Belson (PB) 分解扩展至纵向设定，目标是在给定协变量与修饰变量 (modifier) 的框架下，识别并分解不同人群间健康差异的动态演变。提出的纵向分解方法将总差异划分为三个分量：(i) 协变量条件分布差异（在修饰变量共同分布下评估）；(ii) 修饰变量分布差异及其与协变量交互作用产生的差异；(iii) 未解释差异。区别于传统将前两项合并为“已解释差异”的做法，该分解通过分离修饰变量，实现了对与修饰变量相关和不相关的差异时间模式的独立刻画。实证部分将该方法应用于胎儿生长纵向研究，揭示了不同种族/族裔群体在孕期发育轨迹差异的来源。对您有用：该文的纵向差异分解框架与修饰变量交互机制，可为您在纵向因果推断与中介分析中的识别策略提供方法迁移，同时附有流行病学真实队列数据集。
- **关键技术**: `Peters-Belson decomposition`, `longitudinal disparity decomposition`, `modifier interaction`, `causal fairness decomposition`, `fetal growth trajectories`
- **为什么对您有用**: 该文将因果分解方法扩展至纵向设定并引入修饰变量交互，其方法论思路可迁移至您关注的纵向因果推断与中介分析；同时提供了流行病学（胎儿生长）真实数据集，符合您对应用因果工作的兴趣。

### 6. [10.1093/biostatistics/kxaf046](https://doi.org/10.1093/biostatistics/kxaf046) — Counterfactual fairness for small subgroups
- **作者**: Solvejg Wastvedt, Jared D Huling, Julian Wolfson
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在算法公平性设定下，针对小样本亚组的反事实公平性评估问题，目标是在 counterfactual fairness 框架下定义跨组可借信息的 estimands，关键假设为治疗混淆需被正确调整。提出三步法：首先定义利用跨组信息的新 estimands；其次通过扩大有效样本量进行估计；最后提出数据借用法（data borrowing），整合仅含协变量和组别信息但缺失结局与预测的外部数据。方法核心在于将外部无结局数据纳入反事实量的估计，提升小亚组的统计精度。应用于美国中西部医疗系统 COVID-19 风险预测模型的公平性评估。对您有用之处在于：counterfactual fairness 本质是因果 estimand 的识别与估计问题，其外部数据整合策略可迁移到 causal inference 中处理小亚组或缺失结局场景，且流行病学应用提供了真实数据集参考。
- **关键技术**: `counterfactual fairness`, `confounding adjustment by treatment`, `cross-group estimand`, `data borrowing with missing outcomes`, `external data integration`
- **为什么对您有用**: 直接连接 primary interest 中的 causal inference（反事实 estimand 定义与混淆调整）和 efficiency theory（小亚组精度提升的外部数据借用法），同时 secondary interest 的 epidemiology 应用提供了 COVID-19 风险预测的真实数据集与分析范式。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1093/biostatistics/kxaf047](https://doi.org/10.1093/biostatistics/kxaf047) — While-alive regression analysis of composite survival endpoints
- **作者**: Xi Fang, Hajime Uno, Fan Li
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在存在终止事件的复合生存终点设定下，本文研究暴露加权 while-alive 累积频率测度的回归问题，目标是估计协变量与广义 while-alive 损失率之间的时变关联。方法采用样条建模协变量与 while-alive 损失率的时变关联，适用于独立与聚类相关数据。理论上推导了回归估计量在两种数据设定下的渐近性质（n^{-1/2}-CAN），仿真验证了有限样本下估计量的无偏性与置信区间覆盖度。实证分析基于两个随机临床试验数据，方法已由 R 包 WAreg 实现。对您而言，本文的样条半参数回归与聚类数据渐近理论推导可作为生存分析/流行病学应用中的方法参考，但未涉及您核心关注的效率界或高维推断。
- **关键技术**: `spline regression`, `while-alive measure`, `composite survival endpoint`, `asymptotic properties`, `cluster-correlated data`
- **为什么对您有用**: 本文涉及半参数样条回归与渐近理论推导，可为您在流行病学/临床试验生存数据的应用提供回归工具，但未触及您核心关注的 semiparametric efficiency bounds 或高维推断。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1093/biostatistics/kxae046](https://doi.org/10.1093/biostatistics/kxae046) — Testing for a difference in means of a single feature after clustering
- **作者**: Yiqun T Chen, Lucy L Gao
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究在聚类（层次聚类或 k-means）后对单一特征均值差异进行假设检验的问题，目标 estimand 为两聚类间的特征均值差，关键假设是聚类算法的选择机制可被参数化刻画。传统检验因忽略选择偏差导致 Type I error 严重膨胀；作者提出一种新的选择性推断（selective inference）检验方法，通过条件推断框架修正选择偏差，在有限样本下精确控制 selective Type I error rate。该检验统计量具有计算高效性，无需重抽样或渐近近似。模拟与单细胞 RNA 测序数据验证了其有效性和功效。对您有用：直接推进您在 mathematical statistics (hypothesis testing) 方向的兴趣，展示了 post-selection inference 中有限样本精确检验的构造思路。
- **关键技术**: `selective inference`, `selective Type I error`, `post-selection inference`, `finite-sample exact test`, `k-means clustering`, `hierarchical clustering`
- **为什么对您有用**: 直接对应您在 mathematical statistics (hypothesis testing) 方向的兴趣，展示了 post-selection inference 中有限样本精确控制 Type I error 的检验构造；其单细胞数据应用对生物统计/流行病学队列的亚组分析有方法迁移价值。

### 2. [10.1093/biostatistics/kxaf045](https://doi.org/10.1093/biostatistics/kxaf045) — Determining vaccine responders in the presence of baseline immunity using single-cell assays and paired control samples
- **作者**: Zhe Chen, Siyu Heng, Asa Tapley, Stephen De Rosa, Bo Zhang
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在疫苗免疫原性研究中，目标是利用 ICS 单细胞检测的配对（接种前后）数据判定疫苗应答者，关键假设是配对对照样本可捕捉不同检测批次间的非预期变异（batch effects）。本文提出一种新的假设检验框架，通过配对对照数据计算两个调整 P 值：最大调整 P 值（对所有与对照数据相容的 batch effect 取最保守调整，保证 Type I error 有效性）和最小调整 P 值（仅施加使调整后 P 值不被对照数据证伪的最小调整）。这两个 P 值构成对 batch effect 的灵敏度带，在控制假阳性与保持检验功效之间取得平衡。方法应用于 CoVPN 3008 研究的 COVID-19 疫苗 ICS 数据，识别 Omicron 感染与疫苗诱导 T 细胞应答的参与者。对您有用之处：min/max P 值的 bounding 思路与 causal inference 中 sensitivity analysis 的逻辑同构，且假设检验框架直接关联您的 hypothesis testing 兴趣，流行病学数据集亦有参考价值。
- **关键技术**: `paired control P-value adjustment`, `maximally/minimally adjusted P-values`, `batch effect bounding`, `Type I error control under assay variation`, `ICS single-cell assay analysis`
- **为什么对您有用**: min/max 调整 P 值的 bounding 思路与您 primary interest 中 causal sensitivity analysis 的逻辑同构，假设检验框架直接关联 hypothesis testing 兴趣，CoVPN 3008 数据集对流行病学应用有参考价值。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1093/biostatistics/kxaf037](https://doi.org/10.1093/biostatistics/kxaf037) — Meta-analysis models with group structure for pleiotropy detection at gene and variant level using summary statistics from multiple datasets
- **作者**: Pierre-Emmanuel Sugier, Yazdan Asgari, Mohammed Sedki, Thérèse Truong, Benoit Liquet
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在多表型 GWAS 汇总数据的基因多效性（pleiotropy）检测问题中，现有方法通常在变异或基因单一尺度上逐一检验，无法同时利用变异嵌套于基因的层级组结构信息。本文提出 MPSG 方法，构建了带组结构惩罚（group-structured penalty）的多变量元分析模型，以在全基因组尺度上联合筛选多效性变异与基因。算法层面，作者实现了交替方向乘子法（ADMM）来高效求解该复合惩罚优化问题。仿真与乳腺癌-甲状腺癌真实 GWAS 数据表明，MPSG 在不同汇总统计量输入下相比 GCPBayes、PLACO 等方法具有更优的变量选择表现。对您而言，该文展示了 ADMM 在高维层级惩罚回归中的计算实现细节，且其基于汇总数据的多表型分析框架对流行病学中的高维因果推断与变量选择有参考价值。
- **关键技术**: `penalized multivariate meta-analysis`, `group-structured penalty`, `ADMM algorithm`, `pleiotropy detection`, `GWAS summary statistics`
- **为什么对您有用**: 展示了 ADMM 在高维层级惩罚优化中的统计计算实现（对应您的 statistical computing 兴趣），且其基于 GWAS 汇总数据的多效性分析框架可迁移至流行病学中的多表型因果推断与高维变量选择。

### 2. [10.1093/biostatistics/kxaf029](https://doi.org/10.1093/biostatistics/kxaf029) — Bayesian scalar-on-tensor regression using the Tucker decomposition for sparse spatial modeling
- **作者**: Daniel A Spencer, Rene Gutierrez, Rajarshi Guhaniyogi, Russell T Shinohara, Raquel Prado, Alzheimer’s Disease Neuroimaging Initiative et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在 scalar-on-tensor 回归设定下，tensor 协变量维度极高且系数具有内在空间稀疏性，目标是在保留空间结构的同时高效估计 tensor 系数。本文提出基于 Tucker 分解的贝叶斯方法，将 tensor 系数分解为核心 tensor 与各模态因子矩阵的乘积，大幅减少自由参数数量，并通过先验分布施加稀疏正则化。Tucker 分解相比 CP 分解允许各模态具有不同秩，灵活性更强。模拟实验与 ADNI 阿尔茨海默症神经影像数据分析均显示该方法在推断性能上优于现有 tensor 回归方法。对您而言，Tucker 分解的参数缩减机制与高维 tensor 运算策略可迁移至统计计算与高维统计的相关工作中。
- **关键技术**: `Tucker tensor decomposition`, `Bayesian scalar-on-tensor regression`, `sparsity-inducing priors`, `high-dimensional parameter reduction`, `neuroimaging spatial modeling`
- **为什么对您有用**: Tensor 分解的数值计算与参数缩减策略与您 statistical computing（tensor/matrix 数值方法）和 high-dimensional statistics 的兴趣有交叉；ADNI 数据集及分析流程对流行病学应用也有参考价值。

## 流行病学  *(epidemiology, 5 篇)*

### 1. [10.1093/biostatistics/kxaf038](https://doi.org/10.1093/biostatistics/kxaf038) — Assessing treatment efficacy for interval-censored endpoints using multistate semi-Markov models fit to multiple data streams
- **作者**: Raphaël Morsomme, C Jason Liang, Allyson Mateja, Dean A Follmann, Meagan P O’Brien, Chenguang Wang et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究区间删失多数据流下多状态 semi-Markov 模型的拟合与处理效应评估，目标参数为无症状感染的保护效力(PE)、感染后血清转换率及病毒脱落时长。核心方法为 Monte Carlo EM 算法配合 importance sampling，解决间歇观测下边际似然不可解析的难题，使半参数 semi-Markov 模型在复杂粗化数据下可拟合。算法相较现有方法有显著计算加速，并在 REGEN-COV 临床试验数据（症状、RT-qPCR、血清学三流）上给出 PE 估计：REGEN-COV 降低无症状感染风险、缩短病毒脱落时间、降低无症状感染者血清转换率。对您而言，该文的 MCEM+IS 计算框架对统计计算方向有参考价值，且流行病学试验数据及多状态因果效应（treatment efficacy on intermediate endpoints）的参数化思路可迁移至纵向因果推断场景。
- **关键技术**: `semi-Markov multistate model`, `Monte Carlo EM algorithm`, `importance sampling`, `interval censoring`, `protective efficacy estimation`, `semi-parametric likelihood`
- **为什么对您有用**: 流行病学真实数据集（REGEN-COV 试验）与多状态 semi-Markov 模型的半参数拟合方法，对您在纵向因果推断中处理区间删失中间终点有迁移价值；MCEM+IS 计算方案对统计计算方向亦具参考意义。

### 2. [10.1093/biostatistics/kxaf028](https://doi.org/10.1093/biostatistics/kxaf028) — Bayesian mapping of mortality clusters
- **作者**: Andrea Sottosanti, Enrico Bovo, Pietro Belloni, Giovanna Boccuzzo
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究多死因下的空间死亡率聚类问题，目标是在识别空间聚类边界的同时筛选出导致聚类形成的具体疾病。提出多元贝叶斯模型 perla，利用多项分布的 stick-breaking 构造将空间结构直接纳入聚类概率；引入 global-local shrinkage prior 排除无信息疾病，确保聚类仅依赖于死亡率有显著变化的疾病；推断采用 MCMC 算法，几乎所有参数均有闭式 Gibbs 采样更新，无需复杂调参。实证分析基于意大利 ULSS6 Euganea 地区及美国县级死亡率数据。对您而言，该文提供了一个流行病学空间数据集及贝叶斯聚类分析范式，但方法学与您关注的因果推断或半参数效率理论重叠有限。
- **关键技术**: `multivariate Bayesian spatial model`, `stick-breaking formulation`, `global-local shrinkage prior`, `Gibbs sampling`, `disease mapping`
- **为什么对您有用**: 属于流行病学（secondary interest）应用，提供了多死因空间聚类数据集和闭式 Gibbs 计算流程，但未涉及因果推断或半参数理论，方法可迁移性较弱，主要收益在于了解流行病学空间数据结构。

### 3. [10.1093/biostatistics/kxaf034](https://doi.org/10.1093/biostatistics/kxaf034) — Markov switching zero-inflated space-time multinomial models for comparing multiple infectious diseases
- **作者**: Dirk Douwes-Schultz, Alexandra M Schmidt, Laís Picinini Freitas, Marilia Sá Carvalho
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 2/10 · novelty: `application`
- **摘要**: 针对多种共循环传染病时空计数数据中存在大量零计数的问题，本文提出多元零膨胀时空多项式模型。模型假设一种基线疾病始终存在，其余疾病的存在/缺席状态由耦合马尔可夫链刻画，以捕捉长期缺席、疾病交互与空间扩散。在疾病存在时，各区域病例数服从自回归多项式分布，用于比较传播强度及协变量（如温度）的关联。推断采用贝叶斯 MCMC 方法，通过联合采样所有未知存在指标提升计算效率。实证分析了里约热内卢登革热、寨卡和基孔肯雅热的三重流行数据。对您而言，该文展示了贝叶斯层次模型在流行病学多疾病数据中的应用，但未涉及因果推断，主要价值在于了解时空流行病学数据结构及建模惯例。
- **关键技术**: `Markov switching model`, `zero-inflated model`, `spatio-temporal multinomial model`, `Bayesian MCMC`, `coupled Markov chains`
- **为什么对您有用**: 属于流行病学应用，提供了多疾病时空数据集的贝叶斯建模思路，但未涉及您关注的因果推断方法，仅作应用模式与数据结构参考。

### 4. [10.1093/biostatistics/kxaf048](https://doi.org/10.1093/biostatistics/kxaf048) — Assessing spatial disparities: a Bayesian linear regression approach
- **作者**: Kyle Wu, Sudipto Banerjee
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 0/10 · novelty: `application`
- **摘要**: 在区域聚合空间流行病学数据设定下，本文旨在检测相邻区域间的空间健康差异（如疾病死亡率边界划分），核心模型为带空间自回归的贝叶斯线性回归。方法在经典框架中引入空间自回归以实现基于模型的空间差异检测，并通过推导解析可处理性（通常涉及 GMRF 稀疏精度矩阵技巧）大幅加速后验计算。模拟在全美县级地图上验证了方法有效性，实证分析使用了 IHME 的美国县级肺癌年龄标准化死亡率数据。对您而言，本文主要价值在于提供了 IHME 县级流行病学数据集的获取与分析线索，但方法学属于贝叶斯空间统计，与因果推断或半参数效率理论关联较弱。
- **关键技术**: `Bayesian linear regression`, `spatial autoregression`, `analytical tractability`, `spatial disparities detection`, `IHME county-level mortality data`
- **为什么对您有用**: 提供了 IHME 美国县级肺癌死亡率数据集的应用案例，对您在流行病学方向寻找真实空间/区域层级数据集有参考价值，但方法学（贝叶斯空间自回归）与您的核心兴趣（因果/半参数/效率）重叠极低。

### 5. [10.1093/biostatistics/kxaf039](https://doi.org/10.1093/biostatistics/kxaf039) — Network generalized estimating equations for complexly correlated data with applications to cluster randomized trials
- **作者**: Tom Chen, Fan Li, Rui Wang
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在整群随机试验（CRT）设定下，针对具有复杂相关结构的均值与关联参数估计问题，本文提出基于网络概念的广义估计方程（GEE）框架。核心机制是将观测划分为可能重叠的局部可交换群组，利用网络图表示依赖结构，从而支持多重交换结构（简单、嵌套、块）、移动平均及指数衰减等复杂工作相关矩阵的建模。针对大整群规模下 GEE 计算的瓶颈，作者开发了 networkGEE R 包，通过特定数值算法突破了现有软件的计算限制。模拟研究验证了方法在有限样本下的表现，实证分析则基于华盛顿州加速伴侣疗法阶梯楔形 CRT 数据。对您有用：该文为阶梯楔形 CRT（纵向因果推断重要设计）提供了复杂相关结构建模思路与计算工具，其流行病学真实数据集和大规模矩阵计算方案对您的纵向因果推断与统计计算兴趣有直接参考价值。
- **关键技术**: `generalized estimating equations`, `network correlation structure`, `local exchangeability`, `stepped-wedge cluster randomized trial`, `large-scale matrix computation`
- **为什么对您有用**: 该文针对阶梯楔形 CRT（一种重要的纵向因果推断设计）提出网络 GEE 框架并解决大整群计算问题，其真实流行病学数据集和 R 包对您的纵向因果推断与统计计算兴趣有直接参考价值。

## 其他  *(other, 2 篇)*

### 1. [10.1093/biostatistics/kxaf012](https://doi.org/10.1093/biostatistics/kxaf012) — Addressing the mean–variance relationship in spatially resolved transcriptomics data with <i>spoon</i>
- **作者**: Kinnary Shah, Boyi Guo, Stephanie C Hicks
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对空间转录组学（SRT）数据中识别空间变异基因（SVG）的任务，指出对数转换会引入技术偏差，破坏基因计数的均值-方差关系（即高表达基因在对数转换后方差偏低）。为修正此偏差，作者提出 spoon 统计框架，利用经验贝叶斯（empirical Bayes）技术对均值-方差关系进行校准，从而更准确地优先排序 SVG。方法在模拟与真实 SRT 数据中验证了偏差修正的有效性。然而，该工作主要针对特定基因组学数据的预处理与排序问题，未涉及复杂的半参数理论或效率界计算。对您而言，此文仅在经验贝叶斯处理方差调制的应用层面有微弱参考价值，与您核心关注的因果推断、高维 RMT 或半参数效率理论无直接关联。
- **关键技术**: `empirical Bayes`, `mean-variance relationship`, `log-transformation bias correction`, `spatially variable genes`
- **为什么对您有用**: 本文属于生物信息学应用方法，使用经验贝叶斯处理特定数据的均值-方差关系，与您关注的半参数效率、高维随机矩阵或因果推断等理论方向重叠极低，仅作了解经验贝叶斯方差调制应用的微弱参考。

### 2. [10.1093/biostatistics/kxaf050](https://doi.org/10.1093/biostatistics/kxaf050) — High-dimensional inference for functional regression with an application to the Alzheimer’s disease magnetoencephalography study
- **作者**: Huaqing Jin, Fei Jiang
- **期刊/来源**: Biostatistics
- **分类**: vol 26 · issue 1
- 相关性 0/10
- **摘要**: {
  "topic": "hypothesis_testing",
  "summary_zh": "在高维函数线性回归设定下，本文提出针对函数型协变量的高维假设检验（HDHT）框架，旨在克服传统功率谱密度特征提取的信息损失与变量选择的不稳健性。核心方法通过构造去偏（debiased）或正交化的检验统计量，绕过了传统高维变量选择带来的选择后推断偏差。理论上严格建立了 HDHT 统计量的渐近分布与收敛性质，保证了检验的水平与功效。模拟验证了有限样本表现，并在阿尔茨海默病 MEG 数据中识别出 19 个关键脑区。对您有用：该工作直接结合了您关注的"高维假设检验"与"函数型/半非参理论"，且 AD-MEG 数据集对流行病学应用有参考价值。",
  "key_techniques": [
    "high-dimensional hypothesis testing",
    "functional linear regression",
    "debiased inference",
    "asymptotic distribution",
    "post-selection inference avoidance"
  ],
  "why_relevant": "直接切中您的主要兴趣"高维假设检验"与"半/非参理论"，同时其阿尔茨海默病 MEG 应用属于流行病学数据集


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

