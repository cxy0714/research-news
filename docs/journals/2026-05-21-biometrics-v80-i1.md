# Biometrics — Vol 80  Issue 1  ·  2026-05-21

- 共 19 篇 · Biometrics

## 因果推断  *(causal_inference, 5 篇)*

### 1. [10.1093/biomtc/ujae014](https://doi.org/10.1093/biomtc/ujae014) — Bias correction models for electronic health records data in the presence of non-random sampling
- **作者**: Jiyu Kim, Rebecca Anthopolos, Judy Zhong
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在电子健康记录(EHR)数据的非随机抽样设定下，目标是纠正选择偏差以获得总体关联系数和结局均值的相合估计。本文提出一系列 Heckman 型偏差校正方法，通过引入健康社会决定因素作为选择协变量来建模 EHR 非随机抽样概率。方法核心在于利用选择方程的建模修正结果方程的期望，属于经典样本选择框架在 EHR 场景的拓展。模拟表明该方法能有效校正关联系数与结局均值的偏差；实证分析估计了纽约市 EHR 网络中心血管疾病患病率及其与危险因素的关联。对您有用：提供了流行病学 EHR 数据集的选择偏差处理范式，且 Heckman 模型与您关注的因果推断中的选择偏差/IV 识别问题直接相关。
- **关键技术**: `Heckman selection model`, `selection bias correction`, `non-random sampling`, `social determinants of health`, `EHR data`
- **为什么对您有用**: 匹配您在流行病学（EHR数据集与应用因果）和因果推断（选择偏差识别）的兴趣；Heckman 模型是计量经济学与因果推断处理选择偏差的经典工具，本文展示了其在真实 EHR 数据中的适配与应用。

### 2. [10.1093/biomtc/ujad026](https://doi.org/10.1093/biomtc/ujad026) — Bayesian nonparametric for causal inference and missing data by Michael J. Daniels, Antonio Linero, and Jason Roy, CRC Press, 2023 ISBN-13: 978-0367341008, https://www.routledge.com/Bayesian-Nonparametrics-for-Causal-Inference-and-Missing-Data/Daniels-Linero-Roy/p/book/9780367341008
- **作者**: Li-Pang Chen
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 0/10 · novelty: `survey`
- **摘要**: 本文是对专著《Bayesian Nonparametrics for Causal Inference and Missing Data》的书评，系统梳理了在因果推断与缺失数据框架下使用贝叶斯非参数方法的设定与 identifiability 问题。书中涵盖 g-formula、倾向得分、边际结构模型及因果中介等因果 estimand 的贝叶斯估计，并详细讨论了 MCAR/MAR/MNAR 缺失机制下的选择模型、模式混合模型和共享参数模型。计算层面涉及 MCMC、Gibbs 采样、HMC 等后验推断算法，以及模型检验与数据增广策略。作为综述性书评，本文本身无新理论贡献，但为贝叶斯非参数因果推断提供了系统的文献与案例索引。对您而言，虽然您主要关注频率学派的半参数效率界与 debiased ML，但该书中关于 MNAR 缺失数据与不可识别性的讨论可为 proximal CI 及敏感性分析提供贝叶斯视角的对照与启发。
- **关键技术**: `Bayesian nonparametrics`, `missing not at random (MNAR)`, `marginal structural models`, `pattern mixture models`, `Hamiltonian Monte Carlo`, `causal mediation`
- **为什么对您有用**: 虽然您主攻频率学派的半参数效率理论，但该专著对 MNAR 缺失数据与不可识别性的贝叶斯建模讨论，可为您的 proximal CI 及敏感性分析研究提供不同推断范式下的参考与对照。

### 3. [10.1093/biomtc/ujad028](https://doi.org/10.1093/biomtc/ujad028) — The central role of the identifying assumption in population size estimation
- **作者**: Serge Aleshin-Guendel, Mauricio Sadinle, Jon Wakefield
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究多系统估计（capture-recapture）中的人口规模估计问题，将其视为缺失数据问题，核心在于不可检验的识别假设（identifying assumption）。作者指出传统方法常将观测数据模型与识别假设混为一谈，导致不同识别假设下即使拟合相同也会产生任意差异的总体规模估计。文章提出一种重新框架，将观测数据模型的设定与识别假设解耦，使得识别假设的论证更加透明且独立。该方法利用现有软件实现，并自然支持针对不同识别假设的敏感性分析。实证部分通过估计科索沃战争平民伤亡数量展示了该框架的应用。对您有用：该文对“识别假设”与“观测模型”解耦的框架及敏感性分析思路，可直接迁移至因果推断中处理不可检验的识别假设（如proximal CI或IV的敏感性分析）。
- **关键技术**: `multiple-systems estimation`, `identifying assumption`, `missing data framework`, `sensitivity analysis`, `model decoupling`
- **为什么对您有用**: 文章聚焦缺失数据与识别假设的解耦及敏感性分析，其形式化框架与因果推断中的识别与敏感性分析高度同构，可为proximal CI或IV设定下的敏感性分析提供方法论借鉴。

### 4. [10.1093/biomtc/ujad039](https://doi.org/10.1093/biomtc/ujad039) — Inferring a directed acyclic graph of phenotypes from GWAS summary statistics
- **作者**: Rachel Zilinskas, Chunlin Li, Xiaotong Shen, Wei Pan, Tianzhong Yang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在 GWAS 汇总统计数据设定下，目标是估计表型间的因果网络（DAG），假设高斯线性结构方程模型并以遗传变异作为工具变量（IV）。方法仅需 GWAS 汇总统计与基因型参考面板，通过 IV 策略实现有向边的识别与 DAG 估计。核心创新在于提出了基于汇总统计的似然比检验（LRT），用于推断有向边的存在性。仿真与 29 种心血管相关蛋白及阿尔茨海默病（AD）的真实数据分析验证了方法有效性，并提供了 R 包 sumdag。对您有用：直接关联因果推断（IV/DAG 估计）与假设检验（LRT），且提供流行病学 GWAS 数据集与计算工具，对 IV 因果图与统计计算方向有方法迁移与代码借鉴价值。
- **关键技术**: `instrumental variables`, `directed acyclic graph (DAG)`, `likelihood ratio test`, `GWAS summary statistics`, `Gaussian linear structural model`
- **为什么对您有用**: 直接关联因果推断（IV/DAG 估计）与假设检验（LRT），且提供流行病学 GWAS 数据集与 R 包，对您在 IV 因果图与统计计算方面的研究有方法迁移与工具借鉴价值。

### 5. [10.1093/biomtc/ujad037](https://doi.org/10.1093/biomtc/ujad037) — Using instrumental variables to address unmeasured confounding in causal mediation analysis
- **作者**: Kara E Rudolph, Nicholas Williams, Iván Díaz
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在因果中介分析中，暴露-结果、暴露-中介及中介-结果间的未观测混杂使得传统顺序可忽略性失效；本文在拥有两个（可能相关）工具变量（分别作用于暴露和中介）的设定下，定义并非参数识别了新的 estimand——双重依从者干预直接与间接效应。核心机制是利用两个 IV 的排他性假设，绕过不可观测混杂，推导出非参数识别公式。基于此，作者构造了非参数的、具有鲁棒性与半参数有效性的估计量（基于 efficient influence function），具备 n^{-1/2}-CAN 性质。实证部分将方法应用于住房券实验数据。对您有用：本文直接推进了您关注的因果推断中 IV 与 mediation 交叉方向，其非参数识别框架与 efficient estimator 构造对您的效率理论（semiparametric efficiency bounds）研究有直接参考价值。
- **关键技术**: `instrumental variables`, `causal mediation analysis`, `nonparametric identification`, `efficient influence function`, `interventional direct/indirect effects`
- **为什么对您有用**: 直接推进了您 primary interest 中的因果推断 IV 与 mediation 交叉方向；其非参数识别框架与半参数有效估计量的构造对您的效率理论（semiparametric efficiency bounds）研究具有直接参考价值。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 2 篇)*

### 1. [10.1093/biomtc/ujad001](https://doi.org/10.1093/biomtc/ujad001) — Homogeneity pursuit and variable selection in regression models for multivariate abundance data
- **作者**: Francis K C Hui, Luca Maestrini, Alan H Welsh
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在多变量丰度数据的回归设定下，目标是同时实现同质性追踪（将具有相似系数的物种分组）与变量选择，并处理物种间相关性。方法基于广义估计方程（GEE），通过降秩工作相关矩阵刻画响应变量间的相关性。引入 adaptive fused lasso 惩罚实现同质性聚类，adaptive lasso 惩罚实现跨协变量的稀疏性。数值模拟表明该方法具有优良的有限样本表现。实证分析（大堡礁数据）显示该方法能给出更简约的模型并提升样本外预测精度。对您有用：虽然应用在生态学，其将 fused lasso 与 GEE 结合处理多响应变量稀疏与聚类的计算框架，可迁移至高维统计中的多任务学习或流行病学多结局队列数据分析。
- **关键技术**: `generalized estimating equations`, `adaptive fused lasso`, `adaptive lasso`, `reduced-rank working correlation`, `homogeneity pursuit`, `multivariate regression`
- **为什么对您有用**: 涉及高维统计中的变量选择与稀疏建模，其基于 GEE 与 fused lasso 的同质性聚类计算框架可迁移至流行病学多结局数据或高维多任务回归设定。

### 2. [10.1093/biomtc/ujae012](https://doi.org/10.1093/biomtc/ujae012) — Accounting for network noise in graph-guided Bayesian modeling of structured high-dimensional data
- **作者**: Wenrui Li, Changgee Chang, Suprateek Kundu, Qi Long
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维结构化回归中，现有图引导方法常依赖含噪或不完整的外部网络先验。本文提出图引导贝叶斯建模框架，通过 latent scale modeling 融合含噪外部图与数据驱动估计图以推断真实潜在网络。该网络模型耦合了带自适应结构化收缩先验的贝叶斯高维回归，并开发了高效 MCMC 算法进行后验采样。模拟与阿尔茨海默病多组学数据分析表明，该方法在变量选择与预测上优于忽略网络噪声的现有方法。对您而言，虽然该文是贝叶斯框架而非 RMT 或 DML，但其处理先验图结构不确定性的 latent scale 建模思路及 MCMC 计算方案，对高维图推断与统计计算子方向仍有参考价值。
- **关键技术**: `graph-guided Bayesian regression`, `latent scale modeling`, `adaptive structured shrinkage prior`, `MCMC posterior sampling`, `network noise adjustment`
- **为什么对您有用**: 虽然该文属于贝叶斯高维统计而非您核心关注的 RMT 或 DML，但其处理先验图结构不确定性的 latent scale modeling 思路对高维图推断有启发，且 MCMC 计算方案对您的统计计算兴趣有参考价值。

## 非参数 / 半参数  *(nonparam_semipara, 2 篇)*

### 1. [10.1093/biomtc/ujad006](https://doi.org/10.1093/biomtc/ujad006) — Longitudinal varying coefficient single-index model with censored covariates
- **作者**: Shikun Wang, Jing Ning, Ying Xu, Ya-Chen Tina Shih, Yu Shen, Liang Li
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在纵向医疗成本分析中，针对具有偏态、零膨胀、异方差性及删失生存时间作为协变量的非线轨线估计问题，提出纵向变系数单指标模型。模型将多个患者特征压缩为单指标以表征医疗使用倾向，其对成本轨线的影响由双变量变系数函数（依赖时间与生存状态）灵活刻画。估计采用广义估计方程（GEE），通过扩展边际均值结构将删失生存时间纳入协变量。理论方面，建立了变系数函数的点置信区间及协变量效应的假设检验方法。模拟显示数值表现良好，并应用于 SEER-Medicare 前列腺癌数据。对您有用：该文将单指标与变系数结合处理纵向删失协变量的半参数建模思路，以及 GEE 框架下的假设检验理论，对您在纵向因果推断及半参数理论方面的研究有参考价值，同时提供了流行病学真实数据集的应用范例。
- **关键技术**: `varying coefficient model`, `single-index model`, `generalized estimating equations`, `censored covariate`, `pointwise confidence interval`
- **为什么对您有用**: 该文结合单指标与变系数的半参数建模策略及 GEE 框架下的假设检验，直接契合您在半参数理论与纵向因果推断方面的兴趣；同时 SEER-Medicare 数据集对流行病学应用有参考价值。

### 2. [10.1093/biomtc/ujad041](https://doi.org/10.1093/biomtc/ujad041) — Simultaneous variable selection and estimation in semiparametric regression of mixed panel count data
- **作者**: Lei Ge, Tao Hu, Yang Li
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在纵向混合面板计数数据（同时含面板计数与面板二分类成分）下，本文研究比例均值模型中的同时变量选择与估计问题。以往文献常忽略二分类成分将其视为缺失，本文提出惩罚似然方法以充分利用数据信息。计算上开发了高效的 EM 算法实现稀疏估计，理论上证明了所得估计量具有 oracle 性质（即渐近正态且变量选择相合）。仿真与 Health and Retirement Study 实际数据验证了方法的有限样本表现。对您有用：方法结合了半参数回归的 oracle 推断与纵向数据结构，且 HRS 数据集对经济理论/流行病学的应用因果工作有直接参考价值。
- **关键技术**: `penalized likelihood`, `proportional mean model`, `EM algorithm`, `oracle property`, `mixed panel count data`, `semiparametric regression`
- **为什么对您有用**: 涉及半参数回归的 oracle 推断与纵向数据结构，且 HRS 数据集对经济理论/流行病学的应用因果工作有直接参考价值。

## 效率理论 / Debiased ML  *(efficiency_dml, 2 篇)*

### 1. [10.1093/biomtc/ujad005](https://doi.org/10.1093/biomtc/ujad005) — Robust data integration from multiple external sources for generalized linear models with binary outcomes
- **作者**: Kyuseong Choi, Jeremy M G Taylor, Peisong Han
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在广义线性模型（GLM）框架下，研究如何利用内部原始数据与多个外部研究的汇总统计量（不同协变量子集下的参数估计）进行稳健的数据整合，以提升二值结局参数的估计效率。提出一种自适应惩罚方法，通过利用全模型与遗漏协变量模型参数间的理论关系，对与内部数据不兼容的外部信息进行降权惩罚，从而实现稳健性。计算方面，采用自适应权重与信息准则来选择最优惩罚调谐参数，避免了传统交叉验证的高昂计算负担。理论上，该方法在总体分布异质性下仍能保持一致性，并在外部模型兼容时相比直接极大似然估计（MLE）获得效率提升。模拟与前列腺癌高分级预测的真实数据应用验证了该估计器的稳健性与效率优势。对您有用：该文处理多源异质数据整合的降权/惩罚机制，对因果推断中外部有效性及数据融合的效率理论有直接借鉴意义，同时其调谐参数的快速计算策略也可迁移至您的统计计算工作中。
- **关键技术**: `adaptive penalization`, `data integration`, `omitted covariate GLM`, `information criterion`, `efficiency gain`
- **为什么对您有用**: 该文关注多源异质数据下的效率提升与稳健估计，其自适应惩罚与降权机制对因果推断中外部有效性与数据融合问题有直接借鉴意义；同时，其调谐参数的快速计算策略可迁移至您的统计计算兴趣中。

### 2. [10.1093/biomtc/ujad034](https://doi.org/10.1093/biomtc/ujad034) — Adaptive selection of the optimal strategy to improve precision and power in randomized trials
- **作者**: Laura B Balzer, Erica Cai, Lucas Godoy Garraza, Pracheta Amaranath
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在随机化试验中，目标是选择协变量调整策略（变量及函数形式）以最大化精度同时保持 I 类错误控制。作者扩展了 TMLE 框架下的 Adaptive Pre-specification 方法：从原先仅适用于小样本（N<40）的单协变量 GLM 候选集，推广为使用 V-fold cross-validation 并以估计的影响函数平方（influence curve-squared）作为损失函数，从包含多种机器学习算法的多协变量候选集中自适应选择。模拟研究表明，该方法在零假设下保持 I 类错误控制，精度提升等价于样本量减少 20%–43%；ACTG Study 175 实际数据亦显示整体及亚组效率改善。对您有用：以 influence function 为损失做 cross-validation 选择 TMLE 候选的思路，直接连接 efficiency theory 与 debiased ML 中的 orthogonal score 选择问题，且协变量调整的效率增益框架可迁移至观察性因果推断。
- **关键技术**: `TMLE`, `influence curve-squared loss`, `V-fold cross-validation`, `adaptive pre-specification`, `covariate adjustment in randomized trials`, `empirical efficiency`
- **为什么对您有用**: 以 influence function 平方作为 cross-validation 损失来选择 TMLE 候选估计器，直接连接您在 efficiency theory（semiparametric efficiency bounds / debiased ML）方面的兴趣；协变量调整的精度增益框架也可迁移至观察性因果推断中的协变量选择问题。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1093/biomtc/ujad013](https://doi.org/10.1093/biomtc/ujad013) — Randomized phase II selection design with order constrained strata
- **作者**: Yi Chen, Menggang Yu
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文在随机 II 期临床试验的选择设计（selection design）中，针对具有异质性预后亚群的分层总体，研究如何在存在自然序约束（order constraints）下提高统计效率。针对二分类和生存数据（time-to-event），作者提出利用参数空间的序约束（如各亚组响应率存在自然递增关系）来修正选择概率的计算。核心机制基于 order-restricted inference，通过引入约束极大似然估计或修正检验统计量，缩小参数空间从而提升检验的势（power）或正确选择概率。理论与模拟表明，相比无序约束的传统方法，该方法能显著提高正确选择概率或在同等功效下减少所需样本量。对您而言，本文展示了序约束推断在假设检验与选择设计中的效率提升机制，可作为受限参数空间下假设检验与效率优化的应用案例参考。
- **关键技术**: `order-restricted inference`, `randomized selection design`, `stratified analysis`, `isotonic regression / order constraints`, `time-to-event outcomes`
- **为什么对您有用**: 涉及假设检验与统计效率，展示了序约束（order constraints）如何缩小参数空间以提升检验势，对您在假设检验与效率理论方向有方法学借鉴意义。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1093/biomtc/ujae016](https://doi.org/10.1093/biomtc/ujae016) — Efficient computation of high-dimensional penalized generalized linear mixed models by latent factor modeling of the random effects
- **作者**: Hillary M Heiling, Naim U Rashid, Quefeng Li, Xianlu L Peng, Jen Jen Yeh, Joseph G Ibrahim
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维广义线性混合模型（GLMM）设定下，随着随机效应维度增加，模型设定与计算复杂度急剧上升。本文提出对随机效应进行因子模型分解，将高维潜空间降维至低维潜因子，从而实现高维 GLMM 的可扩展计算。参数估计采用改进的 Monte Carlo Expectation Conditional Minimization (MCECM) 算法，实现对固定效应与随机效应的同时惩罚变量选择。该降维策略避免了高维协方差矩阵的直接操作，大幅提升了计算效率。模拟结果显示该方法在速度与可扩展性上均优于现有方法。对您有用：直接契合您在统计计算（数值方法与算法）和高维统计方面的兴趣，提供了一种处理高维随机效应的降维计算与变量选择策略。
- **关键技术**: `factor model decomposition`, `Monte Carlo Expectation Conditional Minimization`, `penalized GLMM`, `variable selection`, `high-dimensional random effects`
- **为什么对您有用**: 契合您在统计计算（数值方法与算法）和高维统计方面的兴趣，提供了一种通过因子结构对高维随机效应降维并加速 MCECM 迭代的具体算法策略。

## 流行病学  *(epidemiology, 4 篇)*

### 1. [10.1093/biomtc/ujae013](https://doi.org/10.1093/biomtc/ujae013) — Soft classification and regression analysis of audiometric phenotypes of age-related hearing loss
- **作者**: Ce Yang, Benjamin Langworthy, Sharon Curhan, Kenneth I Vaden, Gary Curhan, Judy R Dubno et al.
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 3/10 · novelty: `application`
- **摘要**: 在流行病学队列研究中，目标是在年龄相关听力损失的软分类表型框架下，估计暴露（饮食模式）对表型分类概率的效应。方法首先利用二次判别分析（QDA）将连续听力数据映射为软分类概率，随后通过构建估计方程来推断暴露对这些概率的影响。在无偏性假设下，该估计方程产生一致估计量，且模拟研究显示其具有良好的有限样本表现。实证分析基于护士健康研究II（NHS II）的听力保护研究数据，发现健康饮食模式与代谢加感觉型表型概率降低相关。对您而言，该文提供了一个流行病学队列数据集的应用范例，但方法学核心（标准估计方程）对您主攻的半参数效率或高维因果推断理论创新有限。
- **关键技术**: `quadratic discriminant analysis`, `estimating equations`, `soft classification probability`, `audiometric phenotype`
- **为什么对您有用**: 属于流行病学（secondary interest）应用，使用了护士健康研究II（NHS II）真实队列数据；但方法学为标准估计方程，对您主攻的半参数效率/高维因果推断理论贡献较小，主要提供数据集和应用范式参考。

### 2. [10.1093/biomtc/ujad038](https://doi.org/10.1093/biomtc/ujad038) — Two-phase designs with failure time processes subject to nonsusceptibility
- **作者**: Fangya Mao, Li C Cheung, Richard J Cook
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在含不可治愈分数（nonsusceptibility）的右删失生存数据设定下，本文研究两阶段设计的有效抽样策略，目标是提升 cure model 及易感人群 PH 模型参数的估计效率。采用 mixture cure model 框架，文章考虑了三种回归设定：logistic cure 模型、易感人群 PH 模型，以及易感性与失效时间的联合回归。针对联合回归设定涉及双参数的挑战，作者提出了一类新的基于双变量残差的二阶段抽样设计（bivariate residual-dependent designs），通过依赖残差的子抽样规则优化信息矩阵。模拟研究表明该设计在估计效率上优于传统子抽样方案，并应用于 PLCO 癌症筛查试验数据。对您有用：该文将 semiparametric efficiency 理论应用于两阶段最优设计，且提供了流行病学队列（PLCO）的实际数据与 cure model 设定，对研究抽样效率与生存/因果推断的交叉有参考价值。
- **关键技术**: `two-phase design`, `mixture cure model`, `bivariate residual-dependent sampling`, `semiparametric efficiency`, `nonsusceptibility`
- **为什么对您有用**: 涉及两阶段设计的 semiparametric efficiency 优化，且提供了流行病学（PLCO 癌症筛查）真实数据集与 cure model 设定，对您在流行病学应用中的因果/生存推断及效率理论有直接参考价值。

### 3. [10.1093/biomtc/ujae011](https://doi.org/10.1093/biomtc/ujae011) — Bayesian two-stage modeling of longitudinal and time-to-event data with an integrated fractional Brownian motion covariance structure
- **作者**: Anushka Palipana, Seongho Song, Nishant Gupta, Rhonda Szczesniak
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在纵向与生存联合建模框架下，本文用 scaled integrated fractional Brownian motion (IFBM) 替代传统 random intercepts-and-slopes 刻画生物标志物轨迹的 within-patient 异质性，estimand 为动态疾病进展风险的实时预测概率。纵向 IFBM 子模型推导出新的 target functions 监测快速进展风险，其预测值作为 Cox 生存子模型的时变协变量输入。采用两阶段贝叶斯后验计算而非完全联合建模，降低了数值复杂性。在 LAM 罕见病国家登记队列数据上，IFBM 模型在预测性能上一致优于 integrated Ornstein-Uhlenbeck 及传统 random effects 方案。方法学 novelty 有限（将 integrated BM 推广为 fractional 版本），但对您在流行病学纵向队列中做因果推断或 mediation 分析时，IFBM 提供了一种灵活刻画纵向轨迹的非参数协方差结构替代方案。
- **关键技术**: `integrated fractional Brownian motion`, `joint longitudinal-survival model`, `two-stage Bayesian estimation`, `Cox proportional hazards`, `dynamic predictive probability`
- **为什么对您有用**: IFBM 作为非参数随机过程替代参数化 random effects，与您 semiparametric/nonparametric theory 兴趣相邻；LAM 罕见病登记队列数据及纵向-生存建模流程对流行病学应用有数据集与 pipeline 参考价值。

### 4. [10.1093/biomtc/ujae008](https://doi.org/10.1093/biomtc/ujae008) — A scalar-on-quantile-function approach for estimating short-term health effects of environmental exposures
- **作者**: Yuzi Zhang, Howard H Chang, Joshua L Warren, Stefanie T Ebelt
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 0/10 · novelty: `application`
- **摘要**: 在环境流行病学设定下，研究短期暴露对人群健康结局的影响，核心挑战是区域平均暴露无法捕捉时空单元内的个体暴露异质性。提出scalar-on-quantile-function回归模型，将暴露分布的分位函数作为泛函协变量纳入负二项回归，从而刻画不同分位数水平下的异质性健康效应。技术上通过对分位函数进行基展开或泛函主成分分析（FPCA）实现降维，结合函数系数灵活估计暴露-反应曲线。实证分析使用亚特兰大4年的急诊数据与SHEDS模拟的ZIP code级别暴露分布，发现一氧化碳对呼吸/心血管急诊的影响在暴露分布的低分位数段更显著。对您而言，该文提供了一个流行病学时空暴露数据结构范例，但方法学属于泛函回归的常规应用，理论深度有限。
- **关键技术**: `scalar-on-function regression`, `exposure quantile function`, `functional principal component analysis`, `negative binomial regression`, `spatiotemporal exposure modeling`
- **为什么对您有用**: 属于流行病学应用方向，提供了环境暴露异质性的时空数据集范例（SHEDS模拟暴露+急诊结局）；但方法学为泛函回归的常规应用，对您关注的半参数效率或因果推断理论借鉴有限。

## 其他  *(other, 2 篇)*

### 1. [10.1093/biomtc/ujad022](https://doi.org/10.1093/biomtc/ujad022) — A generalized phase 1-2-3 design integrating dose optimization with confirmatory treatment comparison
- **作者**: Yong Zang, Peter F Thall, Ying Yuan
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 本文提出一种整合剂量优化与确证性比较的广义I-II-III期临床试验设计（Gen 1-2-3），设定基于生存时间数据与活性对照。该方法扩展了Chapple和Thall (2019)的设计：第一阶段利用I-II期标准识别候选剂量集而非单一剂量；中间阶段在候选剂量与活性对照间进行随机化，并联合两阶段生存数据选择最优剂量；最后基于最优剂量优于对照的贝叶斯预测概率进行III期Go/No-Go决策。模拟研究表明，相较于传统设计及CT设计，Gen 1-2-3设计在试验运行特性上表现更优。对您而言，该文属于临床试验自适应设计，其基于预测概率的序贯假设检验与决策逻辑可为序贯因果推断或计算模拟提供间接思路，但与核心理论兴趣距离较远。
- **关键技术**: `adaptive clinical trial design`, `Bayesian predictive probability`, `dose optimization`, `Go/No-Go decision`, `sequential randomization`
- **为什么对您有用**: 与您的主要兴趣（因果推断、高维/半参数理论）直接关联较弱，但其基于预测概率的序贯假设检验与决策框架，可为序贯因果推断或统计计算中的模拟研究提供间接参考。

### 2. [10.1093/biomtc/ujad019](https://doi.org/10.1093/biomtc/ujad019) — A flexible framework for spatial capture-recapture with unknown identities
- **作者**: Paul van Dam-Bates, Michail Papathomas, Ben C Stevenson, Rachel M Fewster, Daniel Turek, Frances E C Stewart et al.
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 1
- 相关性 1/10 · novelty: `minor`
- **摘要**: 本文研究野生动物空间捕获-重捕获（SCR）中个体身份未知时的密度估计问题，将 SCR 建模为标记 Poisson 过程：一个计数过程描述所有检测事件，一个标记分布描述观测特征（身份、探测器位置等）。当个体无法唯一识别时，观测标记来自由活动中心和其他特征定义的混合标记分布，由此推广了现有 latent identity SCR 模型并统一了声学 SCR。方法通过 fisher 相机陷阱和 Cape Peninsula moss frog 声学调查数据验证，模拟显示加入性别或到达时间等额外标记可可靠估计密度。该方法学 novelty 有限，主要是框架统一与推广，对您的研究兴趣直接关联较弱。
- **关键技术**: `marked Poisson process`, `latent identity mixture model`, `spatial capture-recapture`, `acoustic SCR`
- **为什么对您有用**: 与您的主要兴趣（因果推断、高维/RMT、半参数效率、U-统计量）无直接重叠；标记 Poisson 过程的混合模型思路在理论上与您关注的方向关联极弱，阅读收益有限。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

