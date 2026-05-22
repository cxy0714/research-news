# Biostatistics — Vol 24  Issue 2  ·  2026-05-21

- 共 19 篇 · Biostatistics

## 因果推断  *(causal_inference, 4 篇)*

### 1. [10.1093/biostatistics/kxab036](https://doi.org/10.1093/biostatistics/kxab036) — Doubly robust nonparametric instrumental variable estimators for survival outcomes
- **作者**: Youjin Lee, Edward H Kennedy, Nandita Mitra
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 518-537
- 相关性 10/10 · novelty: `new_method`
- **摘要**: 本文在非参数工具变量（IV）框架下，针对删失生存结局，研究局部平均处理效应（LATE）在生存概率上的估计问题，考虑了协变量依赖和结局依赖的删失机制。作者基于有效影响函数（EIF）构建了双重稳健（DR）估计量，该估计量在 IV 为二值或连续时均适用，并能灵活结合机器学习工具进行非参数 nuisance 参数估计。理论上，所提估计量在 nuisance 参数估计满足适当收敛速度时可达半参数有效界；仿真验证了其在模型误设下的双重稳健性。实证分析将方法应用于 PLCO 癌症筛查试验，评估筛查对生存概率的因果效应。对您有用：该文将 IV 识别与 EIF/DR 估计结合拓展至生存数据，直接推进了您在因果推断（IV）与效率理论（EIF/DML）交叉方向的工作，且其流行病学队列数据的分析范式具有迁移价值。
- **关键技术**: `efficient influence function`, `doubly robust estimation`, `nonparametric instrumental variable`, `censored survival outcomes`, `local average treatment effect`
- **为什么对您有用**: 直接契合您在因果推断（IV）与效率理论（EIF、双重稳健/DML）上的核心兴趣，展示了如何在复杂删失结构下推导 EIF 并构建 DR 估计量；同时其流行病学队列数据（PLCO）的应用案例为您提供了 IV 方法在 epi 中实战的参考。

### 2. [10.1093/biostatistics/kxab043](https://doi.org/10.1093/biostatistics/kxab043) — Two-Stage TMLE to reduce bias and improve efficiency in cluster randomized trials
- **作者**: Laura B Balzer, Mark van der Laan, James Ayieko, Moses Kamya, Gabriel Chamie, Joshua Schwab et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 502-517
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在整群随机对照试验（CRT）设定下，目标是估计干预的因果效应，关键假设是控制基线及基线后缺失原因后结局缺失可忽略。提出两阶段目标最小损失估计量（Two-Stage TMLE）：第一阶段针对缺失机制进行目标更新以消除差异测量偏倚；第二阶段自适应调整基线协变量以优化精度。该方法利用TMLE的迭代更新与影响函数理论，在保证双鲁棒性的同时逼近半参数有效界。有限样本模拟表明，现有CRT估计量在缺失下严重有偏，而该方法可近乎消除偏倚。SEARCH社区试验实证展示了自适应协变量调整带来的显著效率提升。该文的两阶段TMLE构建策略直接关联您对效率理论（半参数有效界）和流行病学因果推断的兴趣，对处理复杂缺失与协变量调整有方法迁移价值。
- **关键技术**: `Two-Stage TMLE`, `cluster randomized trials`, `missing data mechanism`, `adaptive covariate adjustment`, `semiparametric efficiency bound`
- **为什么对您有用**: 直接关联您对效率理论（TMLE逼近半参数有效界）和流行病学因果推断的兴趣；两阶段TMLE的构建策略对处理复杂缺失和优化精度有方法论借鉴价值。

### 3. [10.1093/biostatistics/kxab029](https://doi.org/10.1093/biostatistics/kxab029) — A generalizability score for aggregate causal effect
- **作者**: Rui Chen, Guanhua Chen, Menggang Yu
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 309-326
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在因果推断的可推广性（transportability）框架下，目标是将源人群的 ATE 迁移到目标人群，核心挑战是协变量分布重叠不足（positivity violation）导致重加权或回归估计量方差过大。本文提出一种 generalizability score，作为筛选目标子人群以实现可靠因果效应推广的标尺。该方法通过权衡偏差与方差，利用条件平均处理效应（CATE）的异质性与参与概率来界定可推广的子集。其简化版本仅依赖协变量与处理分配信息，避免了接触结局变量可能引入的选择性偏差。模拟与真实数据表明该 score 能有效筛选出方差可控的目标子人群。对您有用：该工作直接处理因果推断中 transportability 的 identification 与 estimation 难题，其应对 positivity violation 与方差膨胀的思路对您在 generalizability 及 sensitivity analysis 方面的研究具有直接参考价值。
- **关键技术**: `transportability`, `generalizability score`, `positivity violation`, `variance-bias tradeoff`, `selection score`
- **为什么对您有用**: 直接对应您 primary interest 中的因果推断（identification 与 estimation），特别是处理 transportability 中协变量重叠不足导致的方差膨胀问题，为可推广性分析提供了新的子人群选择工具与偏差-方差权衡视角。

### 4. [10.1093/biostatistics/kxab012](https://doi.org/10.1093/biostatistics/kxab012) — A Bayesian semiparametric approach for inference on the population partly conditional mean from longitudinal data with dropout
- **作者**: Maria Josefsson, Michael J Daniels, Sara Pudas
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 372-387
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在纵向数据存在退出和练习效应的设定下，本文研究有限总体部分条件均值的估计问题，关键假设为目标总体的纵向辅助信息已知且缺失机制需满足特定条件。提出一种灵活的贝叶斯半参数预测估计器，利用半参数先验对结果模型进行建模，以捕捉复杂的纵向记忆轨迹。该方法通过贝叶斯预测框架自然整合辅助信息并进行不确定性量化，同时针对不可测试的缺失机制假设（如 MNAR）进行了系统的敏感性分析。模拟研究表明该方法在偏差和均方误差上优于传统方法，实证应用于 Betula 队列研究中的情景记忆轨迹估计。对您有用：该文的贝叶斯半参数框架及对不可测试假设的敏感性分析思路，可直接迁移至您关注的纵向因果推断与缺失数据问题中，且 Betula 队列数据对流行病学应用有参考价值。
- **关键技术**: `Bayesian semiparametric predictive estimator`, `sensitivity analysis for MNAR`, `longitudinal dropout modeling`, `finite population inference`, `generalizability with auxiliary information`
- **为什么对您有用**: 本文处理纵向数据退出下的总体推断与敏感性分析，属于纵向因果/缺失数据与半参数理论的交叉，且包含流行病学队列数据集（Betula），对您在纵向因果推断与敏感性分析方向的方法迁移及数据集获取均有价值。

## 非参数 / 半参数  *(nonparam_semipara, 2 篇)*

### 1. [10.1093/biostatistics/kxab031](https://doi.org/10.1093/biostatistics/kxab031) — Estimation for the bivariate quantile varying coefficient model with application to diffusion tensor imaging data analysis
- **作者**: Matthew Pietrosanu, Haoxu Shu, Bei Jiang, Linglong Kong, Giseon Heo, Qianchuan He et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 465-480
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 针对神经影像等多变量函数型响应的联合建模需求，本文提出双变量函数型响应的变系数分位数回归模型，estimand 为给定协变量下双变量响应的条件分位数变系数函数。估计过程结合交替方向乘子法（ADMM）与传播分离算法，利用 B-spline 基展开并施加 L2 平滑惩罚以保证系数函数的可解释性与光滑性。该框架本质上属于半参数变系数模型，允许刻画功能变量在定义域及临床协变量上的联合分布。模拟与 DTI 数据分析验证了方法有效性，揭示了各向异性分数与平均扩散率随胎龄与性别的联合演变模式。对您有用：此文的 B-spline 变系数估计与 ADMM 计算框架可迁移至您关注的 semiparametric theory 及 statistical computing 方向，但缺乏对效率界或高阶渐近性质的探讨。
- **关键技术**: `varying coefficient quantile regression`, `B-spline basis expansion`, `ADMM`, `L2 smoothness penalty`, `propagation separation algorithm`, `bivariate functional response`
- **为什么对您有用**: 涉及半参数变系数模型与 ADMM 优化计算，与您 primary interest 中的 semiparametric theory 及 statistical computing 有直接方法交叉，可借鉴其计算框架，但理论深度有限。

### 2. [10.1093/biostatistics/kxab024](https://doi.org/10.1093/biostatistics/kxab024) — Statistical modeling of longitudinal medical cost trajectory: renal cell cancer care cost analyses
- **作者**: Shikun Wang, Yu Shen, Ya-Chen Tina Shih, Ying Xu, Liang Li
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 244-261
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在纵向医疗成本与生存时间的联合建模设定下，本文目标是估计以生存时间为条件的平均成本轨迹（estimand），同时处理死亡终端事件与右删失。提出两阶段半参数方法，将不同生存时间对应的成本轨迹建模为三角区域上的双变量曲面。核心估计量采用离散测量时间与生存时间的张量积，并结合针对二维数组的有效岭惩罚进行正则化。该方法在模型灵活性、统计效率与计算可行性之间取得平衡，避免了强参数化假设。实证部分基于 SEER-Medicare 链接数据库分析了肾细胞癌患者的成本轨迹。对您有用：该文将半参数联合模型与张量积/岭惩罚计算结合，对您在纵向因果推断中的半参数效率理论及统计计算（张量方法）研究有方法迁移价值。
- **关键技术**: `semiparametric joint model`, `tensor product smoothing`, `ridge penalty`, `bivariate surface estimation`, `conditional mean trajectory`
- **为什么对您有用**: 论文结合半参数联合建模与张量积/岭惩罚计算处理纵向删失数据，对您在纵向因果推断的半参数理论及统计计算（张量方法）方向有方法迁移价值，同时提供了 SEER-Medicare 流行病学数据集的应用范例。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1093/biostatistics/kxab017](https://doi.org/10.1093/biostatistics/kxab017) — A meta-inference framework to integrate multiple external models into a current study
- **作者**: Tian Gu, Jeremy M G Taylor, Bhramar Mukherjee
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 406-424
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在内部个体数据与外部汇总模型共存且协变量集可能不完全一致的设定下，目标是构建改进的回归模型以提高估计精度。提出一种元分析框架，通过两个加权估计量将来自不同外部模型的估计进行组合，本质上是经验贝叶斯估计量的复合。该方法能够自动识别与内部数据最相关的外部信息并降低不兼容信息的影响，在偏差-方差权衡中取得平衡，从而保留最大的效率增益。理论证明所提估计量比仅用内部数据的朴素分析及朴素组合外部估计量更有效。对您有用：该框架在数据整合中的偏差-方差权衡与效率增益分析，与您在效率理论及流行病学应用中的兴趣直接相关，提供了多源数据融合的具体加权策略。
- **关键技术**: `empirical Bayes`, `meta-analysis`, `bias-variance trade-off`, `data integration`, `weighted estimator`
- **为什么对您有用**: 该文关注多源数据整合中的效率增益与偏差-方差权衡，与您的效率理论兴趣直接相关；其外部模型整合框架也可迁移至流行病学队列数据的因果推断应用中。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1093/biostatistics/kxab034](https://doi.org/10.1093/biostatistics/kxab034) — Quantifying uncertainty in spikes estimated from calcium imaging data
- **作者**: Yiqun T Chen, Sean W Jewell, Daniela M Witten
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 481-501
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在钙成像峰值估计问题中，目标是针对指数衰减与瞬时增加模型下估计出的峰值，检验某时间点无峰值的零假设。由于峰值估计与检验使用同一数据，经典检验会导致第一类错误膨胀，本文因此提出选择性推断（selective inference）方法。作者设计了高效算法计算有限样本 p 值以控制选择性第一类错误，并构造具有正确选择性覆盖率的置信区间。模拟与 spikefinder 数据验证了方法的有效性。对您有用之处在于，该工作直接呼应您对假设检验与统计算法的兴趣，其处理“选择后推断”的思路可迁移至高维变量筛选后的不确定性量化。
- **关键技术**: `selective inference`, `post-selection inference`, `finite-sample p-value`, `selective Type I error control`, `exponential decay model`
- **为什么对您有用**: 直接呼应您对假设检验与统计算法的兴趣；其处理“选择后推断”的思路可迁移至高维变量筛选后的不确定性量化问题。

### 2. [10.1093/biostatistics/kxaa055](https://doi.org/10.1093/biostatistics/kxaa055) — Developing a predictive signature for two trial endpoints using the cross-validated risk scores method
- **作者**: Svetlana Cherlin, James M S Wason
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 327-344
- 相关性 0/10 · novelty: `minor`
- **摘要**: 在高维基线协变量设定下，目标是识别并检验新疗法在双终点（如疗效与毒性）上同时获益的敏感亚组。本文将单终点交叉验证风险得分（CVRS）设计扩展至双终点（CVRS2），通过计算双变量风险得分并采用非参数聚类划分亚组。该方法利用交叉验证缓解高维特征选择带来的过拟合，并在选定亚组内进行疗效的假设检验。模拟与精神病学随机试验实证表明，CVRS2 能可靠识别双终点敏感组，且相比单终点方法减少了对协变量预筛选的依赖。对您而言，该文展示了高维协变量下多终点亚组检验的计算框架，对您关注的高维假设检验与流行病学试验应用有直接参考，但缺乏半参数效率等深层理论。
- **关键技术**: `cross-validated risk scores`, `bivariate risk scores`, `nonparametric clustering`, `subgroup treatment effect testing`, `high-dimensional covariates`
- **为什么对您有用**: 涉及高维协变量下的亚组疗效假设检验，与您的高维统计和假设检验兴趣相关；其实际应用于精神病试验数据，对流行病学/临床试验的因果推断应用有参考价值，但缺乏半参数效率等深层理论。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1093/biostatistics/kxab018](https://doi.org/10.1093/biostatistics/kxab018) — Interpretable principal component analysis for multilevel multivariate functional data
- **作者**: Jun Zhang, Greg J Siegle, Tao Sun, Wendy D’andrea, Robert T Krafty
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 227-243
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对多层级多变量函数数据（如 EEG 多频段×多电极×多受试者），提出可解释的主成分分析方法，将总变异分解为受试者间（subject-level）和受试者内电极间（replicate-within-subject）两层。核心估计量为带粗糙度惩罚的函数 PCA，通过求解 rank-one 凸优化问题实现跨变量（频段）的稀疏性（block Frobenius 惩罚）与时间域局部化（matrix L₁-norm 惩罚）的联合选择。算法层面，rank-one 结构使问题可逐分量交替求解，收敛性质依赖凸优化理论保证。实证分析创伤与解离症状的 EEG 数据，揭示了受试者层与电极层脑活动差异的神经生理关联。对您而言，该文的凸优化惩罚设计（block Frobenius + matrix L₁）可迁移至高维/函数数据的稀疏估计问题，且多层级变异分解思路对纵向因果推断中多水平混杂的结构化建模有参考价值。
- **关键技术**: `multilevel functional PCA`, `block Frobenius penalty`, `matrix L1-norm penalty`, `rank-one convex optimization`, `roughness penalty for smoothness`, `sparse localized functional components`
- **为什么对您有用**: 凸优化中 block Frobenius 与 matrix L₁ 联合惩罚的设计思路可直接迁移至您关注的统计计算与高维稀疏估计问题；多层级变异分解框架对纵向因果推断中多水平结构（subject/occasion）的建模有借鉴意义。

### 2. [10.1093/biostatistics/kxab022](https://doi.org/10.1093/biostatistics/kxab022) — Feature selection for support vector regression using a genetic algorithm
- **作者**: Shannon B McKearnan, David M Vock, G Elisabeta Marai, Guadalupe Canahuate, Clifton D Fuller, Julian Wolfson
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 295-308
- 相关性 1/10 · novelty: `minor`
- **摘要**: 在高维非线性回归设定下，针对支持向量回归（SVR）易过拟合的问题，本文提出基于遗传算法（GA）的特征选择方法。该方法通过迭代搜索协变量子集，优化用户定义的适应度函数以提升预测精度。模拟研究表明，GA-SVR在非线性关系下优于LASSO，在协变量相关时优于随机森林。实证部分使用UNOS国家登记处数据预测肾移植后供体肾功能。该方法主要提供预测性能的实证提升，缺乏高维统计理论（如收敛率、效率界）的严格刻画。对您的价值主要在于其流行病学数据应用模式，但方法学新颖度有限。
- **关键技术**: `support vector regression`, `genetic algorithm`, `feature selection`, `fitness function`, `nonlinear regression`
- **为什么对您有用**: 涉及高维特征选择与统计计算（遗传算法），并在流行病学/医学数据（器官移植）上应用，但缺乏您关注的高维理论（RMT/DML）或半参数效率界，方法学新颖度较低。

## 流行病学  *(epidemiology, 3 篇)*

### 1. [10.1093/biostatistics/kxab047](https://doi.org/10.1093/biostatistics/kxab047) — Integrated causal-predictive machine learning models for tropical cyclone epidemiology
- **作者**: Rachel C Nethery, Nina Katz-Christy, Marianthi-Anna Kioumourtzoglou, Robbie M Parks, Andrea Schumacher, G Brooke Anderson
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 449-464
- 相关性 6/10 · novelty: `application`
- **摘要**: 在热带气旋（TC）流行病学设定下，目标是量化历史TC对健康的急性因果效应并预测未来高风险社区。方法整合了因果推断组件（高空间分辨率下估计即时健康影响）与预测组件（关联TC气象特征及社区社会经济特征与健康影响）。技术核心为因果-预测集成机器学习框架，应用于Medicare人群的全因死亡与心肺住院数据。实证发现TC健康影响存在高度异质性，呼吸住院率平均显著增加，且持续风速是主要风险驱动因素。对您有用：该文是流行病学（secondary interest）中应用因果推断与ML整合的典型，提供了Medicare大规模队列数据的分析范式，适合关注流行病学因果应用的研究者借鉴。
- **关键技术**: `causal inference`, `predictive machine learning`, `heterogeneity analysis`, `spatial causal estimation`, `Medicare claims data`
- **为什么对您有用**: 属于流行病学（secondary interest）的应用因果工作，展示了因果推断与预测ML在高空间分辨率队列数据上的整合范式，对关注流行病学因果应用与数据集的研究者有参考价值。

### 2. [10.1093/biostatistics/kxab009](https://doi.org/10.1093/biostatistics/kxab009) — Prognosis of cancer survivors: estimation based on differential equations
- **作者**: Pål C Ryalen, Bjørn Møller, Christoffer H Laache, Mats J Stensrud, Kjetil Røysland
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 345-357
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在癌症生存分析框架下，目标是估计多种预后参数（如生存概率、条件生存概率等），关键假设是这些参数可由累积风险函数驱动的微分方程的解来表示。方法核心是将预后参数表达为微分方程的解，基于 Nelson-Aalen 型累积风险估计量代入微分方程，构造通用估计器，无需复杂数值优化即可用标准统计软件实现。文章显式给出了实践中常用预后参数的估计器，也提出了此前未被使用的预后参数估计。将方法应用于挪威五种常见癌症的预后评估，展示了新参数在区分长期预后方面的实用价值。对您而言，该文的流行病学数据集和生存分析中微分方程建模思路对 epidemiology 方向的因果应用有参考价值，但方法学深度与您 primary interest 的半参数效率理论距离较远。
- **关键技术**: `cumulative hazard estimation`, `Nelson-Aalen estimator`, `differential equation driven by cumulative hazards`, `survival prognosis parameters`, `martingale stochastic integrals`
- **为什么对您有用**: 该文提供了挪威五种常见癌症的流行病学数据集和预后分析流程，对您 epidemiology 方向的因果推断应用有数据集价值；微分方程驱动的估计框架与半参数 influence function 的 ODE 表述有概念联系，但理论深度有限。

### 3. [10.1093/biostatistics/kxab032](https://doi.org/10.1093/biostatistics/kxab032) — Predicting the onset of breast cancer using mammogram imaging data with irregular boundary
- **作者**: Shu Jiang, Jiguo Cao, Graham A Colditz, Bernard Rosner
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 358-371
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在乳腺癌流行病学队列中，目标是利用具有不规则边界的乳腺X光图像特征结合传统风险因子，提升对失效时间（发病时间）的预测精度。本文提出基于三角剖分的监督函数型主成分分析（sFPCA）方法，利用双变量样条（bivariate splines）灵活处理图像的不规则边界问题。与传统无监督FPCA不同，该方法依据与失效时间结局的关联强度对提取的特征进行排序，并提供了计算高效的特征值分解算法。模拟研究显示，该方法在Brier Score和AUC上均优于无监督FPCA。在Siteman癌症中心队列数据的实证中，该方法不仅取得了最佳预测表现，还揭示了图像中的重要风险模式。对您而言，该文展示了非参数函数数据分析与统计计算（三角剖分样条、特征值分解）在流行病学影像数据中的具体实现，提供了不规则边界数据处理的计算思路及真实队列数据参考。
- **关键技术**: `supervised functional principal component analysis`, `bivariate splines over triangulations`, `eigenvalue decomposition algorithm`, `failure time outcome`, `irregular boundary image data`
- **为什么对您有用**: 属于流行病学应用与方法结合的工作；虽然核心非因果推断，但其基于三角剖分的非参数样条计算和sFPCA降维方法，对您在统计计算和非参数理论方面的兴趣有参考价值，同时提供了乳腺癌队列的真实数据集范例。

## 其他  *(other, 5 篇)*

### 1. [10.1093/biostatistics/kxab038](https://doi.org/10.1093/biostatistics/kxab038) — Bayesian finite mixture of regression analysis for cancer based on histopathological imaging–environment interactions
- **作者**: Yunju Im, Yuan Huang, Aixin Tan, Shuangge Ma
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 425-442
- 相关性 2/10
- **摘要**: ```json
{
  "topic": "other",
  "summary_zh": "在有限混合回归(FMR)框架下，本文研究癌症异质性，estimand 为亚组特异的回归系数，假设存在有限个潜在亚组且高维影像特征具有稀疏性。方法采用贝叶斯框架，通过 spike-and-slab 型先验实现高维影像特征的变量选择与噪声剔除，并强制"主效应先于交互效应"的变量选择层级约束（hierarchy）。计算上开发了基于 MCMC 的采样算法处理混合模型的后验推断。模拟表明该方法在信号筛选和亚组识别上优于忽略层级结构的替代方法；TCGA 肺鳞状细胞癌数据分析揭示了与现有方法不同的异质性模式。对您而言，该文的理论深度有限（无收敛率/后验一致性结果），但贝叶斯层级变量选择机制与 TCGA 影像-环境交互建模思路可作应用参考。",
  "key_techniques": [
    "Bayesian finite mixture of regression",
    "spike-and-slab prior",
    "variable selection hierarchy",
    "high-dimensional imaging features",
    "MCMC posterior sampling"
  ],
  "why_relevant": "与您 prima

### 2. [10.1093/biostatistics/kxab040](https://doi.org/10.1093/biostatistics/kxab040) — Historical controls in clinical trials: a note on linking Pocock’s model with the robust mixture priors
- **作者**: Andrea Callegaro, Nicholas Galwey, Juan J Abellan
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 443-448
- 相关性 2/10
- **摘要**: {
  "topic": "other",
  "summary_zh": "在临床试验历史对照借用设定下，本文研究 Pocock 的 bias-variance 方法（与 commensurate prior 紧密相关）与 robust mixture prior (RMP) 之间的参数对应关系。核心发现是 RMP 的两个关键参数——先验概率 w（新试验与历史试验系统性不同的概率）和模糊分量方差 s_v^2——的不同组合可表达相同的先验信念，因此建议固定 s_v^2（例如使模糊分量"等价于一个受试者"），将对历史数据相关性的先验归结为单一可解释参数 w。本文为 Biostatistics 短文笔记，方法学 novelty 有限，主要贡献是澄清两种先验的联系并提供参数化实践建议。对您而言，历史对照借用与因果推断中 transportability/generalizability 有概念联系，但本文不涉及 identification 或 semiparametric 效率理论，直接收益有限。",
  "key_techniques": [
    "robust mixture priors",
    "commensurate prior",
    "Pocock bias-variance method",
    "historical control borrowin

### 3. [10.1093/biostatistics/kxab028](https://doi.org/10.1093/biostatistics/kxab028) — Bayesian adaptive model selection design for optimal biological dose finding in phase I/II clinical trials
- **作者**: Ruitao Lin, Guosheng Yin, Haolun Shi
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 277-294
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 本文研究I/II期临床试验中靶向及免疫治疗的最优生物剂量（OBD）寻找问题，设定为无参数假设与形状约束的剂量-反应曲线建模。作者将剂量寻找转化为贝叶斯模型选择问题，对毒性和疗效终点均采用无曲线（curve-free）模型以确定OBD。该方法通过整合所有剂量水平的观测数据实现自适应剂量分配，提升了锁定正确剂量的效率与准确性。理论上，该设计证明了剂量分配的连贯性（coherence）性质，并扩展至处理免疫治疗中常见的迟发效应。实证方面，模拟研究展示了其稳健性，并以慢性淋巴细胞白血病I/II期试验为例进行了说明。对您而言，本文虽涉及非参数建模（curve-free），但核心为贝叶斯自适应试验设计，缺乏频率学派的渐近效率或收敛率分析，与您关注的半参数效率理论及高维推断距离较远。
- **关键技术**: `Bayesian model selection`, `curve-free model`, `adaptive dose-finding`, `coherence property`, `late-onset outcomes`
- **为什么对您有用**: 本文属于贝叶斯临床试验设计，虽然使用了无曲线（curve-free）非参数模型，但缺乏您核心关注的频率学派半参数效率界或高维理论；对您可能仅有边缘参考价值，了解非参数约束在剂量寻找中的贝叶斯实现方式。

### 4. [10.1093/biostatistics/kxab027](https://doi.org/10.1093/biostatistics/kxab027) — Bayesian multiregional clinical trials using model averaging
- **作者**: Nathan W Bean, Joseph G Ibrahim, Matthew A Psioda
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 262-276
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 在多区域临床试验（MRCT）设定下，目标是估计区域特异性与全局处理效应，解决小样本区域估计质量差的问题。提出基于贝叶斯模型平均（BMA）的新方法，允许纳入协变量，并通过后验模型概率量化跨区域处理效应一致性的证据。模拟表明，相比固定效应线性回归，该方法具有更低的均方误差（MSE）；相比贝叶斯层次模型，具有更好的I类错误率控制。对您而言，该文展示了BMA在处理异质性与假设检验中的具体应用，但方法学深度偏向应用生物统计，与您关注的半参数效率或高维理论距离较远。
- **关键技术**: `Bayesian model averaging`, `multiregional clinical trials`, `posterior model probabilities`, `type I error control`, `treatment effect consistency`
- **为什么对您有用**: 涉及假设检验（I类错误控制）与异质性处理效应估计，但属于应用贝叶斯生物统计，理论深度与您关注的半参数效率或高维推断距离较远，仅作拓宽阅读。

### 5. [10.1093/biostatistics/kxab013](https://doi.org/10.1093/biostatistics/kxab013) — ACTOR: a latent Dirichlet model to compare expressed isoform proportions to a reference panel
- **作者**: Sean D McCabe, Andrew B Nobel, Michael I Love
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 388-405
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在RNA异构体相对比例比较的设定下，目标是利用大规模参考面板将目标数据集中的样本归类到预定义组（如组织来源或疾病状态）。作者提出ACTOR模型，采用带有Dirichlet-Multinomial观测的隐Dirichlet模型来刻画异构体比例的组间变异。估计方面，使用变分贝叶斯（variational Bayes）程序来近似样本组归属的后验分布。基于GTEx项目的参考数据，模型在模拟和真实RNA-seq数据上验证了组织类型分类的准确性。实证结果表明该方法能有效识别组织特异性剪接模式；然而，该工作主要面向基因组学应用，与您核心关注的因果推断、高维推断或半参数效率理论无直接交集，仅变分推断计算部分对统计计算子方向有微弱参考。
- **关键技术**: `latent Dirichlet model`, `Dirichlet-Multinomial observations`, `variational Bayes`, `isoform proportion estimation`
- **为什么对您有用**: 本文属于生物信息学领域的隐变量模型应用，与您的主要兴趣（因果推断、高维RMT、半参数理论）无直接关联，仅变分贝叶斯计算和R包实现可能对统计计算子方向有极微弱的参考价值。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

