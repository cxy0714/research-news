# Biometrics — Vol 80  Issue 4  ·  2026-05-21

- 共 52 篇 · Biometrics

## 因果推断  *(causal_inference, 17 篇)*

### 1. [10.1093/biomtc/ujae106](https://doi.org/10.1093/biomtc/ujae106) — Semiparametric sensitivity analysis: unmeasured confounding in observational studies
- **作者**: Razieh Nabi, Matteo Bonvini, Edward H Kennedy, Ming-Yueh Huang, Marcela Smid, Daniel O Scharfstein
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 10/10 · novelty: `new_method`
- **摘要**: 在观测研究中评估平均因果效应（ACE）时，本文针对不可检验的无未测量混杂假设，提出了一种半参数敏感性分析框架。该方法推广了 Robins 等人的工作，在固定敏感性参数下，利用半参数理论推导了 ACE 的非参数有效影响函数（EIF）。基于此 EIF，作者构建了一个 one-step、split-sample 且带有截断的估计量，其依赖的观测数据半参数模型不对敏感性参数施加限制。理论上给出了保证该估计量具有 √n-CAN（一致渐近正态）收敛性的充分条件。实证部分将该方法应用于评估孕期吸烟对出生体重的因果效应。对您有用：本文将 EIF 与 one-step cross-fitting 结合用于敏感性分析，直接契合您在因果推断（敏感性分析）和效率理论（半参数效率界）方面的核心兴趣，并附带流行病学因果应用的实证范例。
- **关键技术**: `semiparametric sensitivity analysis`, `efficient influence function`, `one-step estimation`, `sample splitting`, `root-n consistent asymptotically normal`
- **为什么对您有用**: 直接推进了您在因果推断（敏感性分析）和效率理论（非参数有效影响函数、one-step 估计）方面的核心兴趣，同时提供了流行病学因果应用的实证范例与数据集参考。

### 2. [10.1093/biomtc/ujae095](https://doi.org/10.1093/biomtc/ujae095) — A causal inference framework for leveraging external controls in hybrid trials
- **作者**: Michael Valancius, Herbert Pang, Jiawen Zhu, Stephen R Cole, Michele Jonsson Funk, Michael R Kosorok
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在混合试验（内部RCT结合外部历史对照）设定下，目标是识别和估计ATE，核心识别假设为内部与外部对照之间的可交换性。本文将此设定形式化为因果推断框架，并提出新的图准则来刻画识别条件。推导了该设定下的半参数效率界，并构建了双重稳健（DR）估计量。当未知干扰函数由灵活机器学习方法估计时，通过交叉拟合保证了估计量的 n^{-1/2}-CAN 性质与半参数有效性。提出了针对模型误设的诊断方法，模拟与SUNFISH试验实证均表明外部对照可显著提升估计效率。对您有用：该文将因果识别（图准则）与效率理论（半参数效率界、DR-ML）紧密结合，并在流行病学试验数据中落地，直接契合您对因果推断识别/估计、效率界及流行病学应用的兴趣。
- **关键技术**: `doubly robust estimation`, `semiparametric efficiency bounds`, `graphical criteria`, `cross-fitting`, `exchangeability assumption`
- **为什么对您有用**: 直接契合您对因果推断（识别与估计）和效率理论（半参数效率界、DR-ML）的核心兴趣；同时提供了流行病学（SMA试验）的真实数据应用范例，展示了外部对照设计下DR-ML的具体操作与诊断方法。

### 3. [10.1093/biomtc/ujae110](https://doi.org/10.1093/biomtc/ujae110) — Causal effect estimation in survival analysis with high dimensional confounders
- **作者**: Fei Jiang, Ge Zhao, Rosa Rodriguez-Monguio, Yanyuan Ma
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在高维混杂生存数据设定下，本文目标是估计不同处理下的限制平均生存时间（RMST）差异这一因果 estimand，假设混杂结构可通过因子模型降维。方法结合因子模型与充分降维（SDR）技术构造倾向得分与预后得分，基于此提出核加权双重稳健（DR）估计量。理论证明了该估计量与匹配方法的内在联系，并建立了其一致性与渐近正态性。实证部分通过弥漫大B细胞淋巴瘤数据集展示了方法应用。对您有用：该工作结合了高维因子模型降维与因果推断 DR 估计，直接契合您在因果推断（生存数据处理效应）与高维统计的交叉兴趣，且 DR 估计的渐近正态性推导对 semiparametric efficiency 理论有参考价值。
- **关键技术**: `restricted mean survival time (RMST)`, `factor model`, `sufficient dimension reduction`, `doubly robust estimation`, `kernel matching`, `asymptotic normality`
- **为什么对您有用**: 直接契合您在因果推断（生存数据处理效应）与高维统计（因子模型降维）的交叉兴趣；其 DR 估计量的渐近正态性推导对 semiparametric efficiency 理论有参考价值，且流行病学数据应用可作 pipeline 借鉴。

### 4. [10.1093/biomtc/ujae154](https://doi.org/10.1093/biomtc/ujae154) — Semi-parametric sensitivity analysis for trials with irregular and informative assessment times
- **作者**: Bonnie B Smith, Yujing Gao, Shu Yang, Ravi Varadhan, Andrea J Apter, Daniel O Scharfstein
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在纵向随机试验中，当受试者评估时间不规则且具信息性时，目标是估计处理效应；关键正则假设为 explainable assessment (EA)——评估时间与当前结局仅通过历史数据关联。作者提出基于 exponential tilting 的敏感性分析框架，用敏感性参数刻画对 EA 假设的偏离程度。推断策略基于新构造的 influence function-based augmented inverse intensity-weighted (AIIW) estimator，实现 n^{-1/2}-CAN 估计。观测数据的半参数工作模型与敏感性参数设定完全解耦，允许灵活建模而不影响敏感性分析的透明性。理论上给出了 efficient influence function 及相应的渐近正态性结果，实证应用于低收入哮喘患者 RCT 数据并详述实现步骤。对您有用：直接推进了 longitudinal causal inference 中 sensitivity analysis 的方法论，且 influence function-based AIIW estimator 的构造思路可迁移到其他 irregular/informative observation 设定（如 proximal CI 中的 negative control 时间结构）。
- **关键技术**: `exponential tilting sensitivity model`, `augmented inverse intensity-weighted estimation`, `efficient influence function`, `explainable assessment assumption`, `semiparametric modeling`, `longitudinal point process`
- **为什么对您有用**: 直接推进您 primary interest 中 longitudinal causal inference 的 sensitivity analysis 方法论；influence function-based AIIW estimator 构造与 semiparametric efficiency theory 紧密相关，思路可迁移至 proximal CI 等其他含 informative observation 的因果推断设定。

### 5. [10.1093/biomtc/ujae143](https://doi.org/10.1093/biomtc/ujae143) — A Bayesian joint model for mediation analysis with matrix-valued mediators
- **作者**: Zijin Liu, Zhihui (Amy) Liu, Ali Hosni, John Kim, Bei Jiang, Olli Saarela
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文在因果中介分析框架下，研究高维矩阵值中介变量（如放疗中的剂量-体积直方图矩阵）对处理与结局之间因果效应的中介机制。提出一种贝叶斯联合中介模型，通过概率化多线性主成分分析（MPCA）提取矩阵数据的潜在特征，保留其固有的矩阵结构。推导并实现了 Gibbs 采样算法进行参数联合估计，并引入 Varimax 旋转以识别矩阵数据中的活跃中介指标。模拟表明，相较于两步法，该联合模型在估计因果分解效应时具有更高的效率。实证分析揭示了肛管癌放疗中处方剂量通过危及器官剂量分布对治疗中断的中介效应，且效应可在矩阵形式下可视化。对您而言，该文将中介分析扩展至矩阵值数据结构，其联合建模思路对处理高维/张量中介变量的因果推断问题具有参考价值。
- **关键技术**: `Bayesian joint mediation model`, `probabilistic multilinear PCA`, `Gibbs sampling`, `Varimax rotation`, `causal decomposition effects`
- **为什么对您有用**: 直接涉及因果推断中的中介分析，并拓展至高维矩阵/张量数据结构；同时包含流行病学（癌症放疗）的实际数据应用，对研究复杂结构数据的中介效应及流行病学因果应用有参考价值。

### 6. [10.1093/biomtc/ujae140](https://doi.org/10.1093/biomtc/ujae140) — Optimal adaptive SMART designs with binary outcomes
- **作者**: Rik Ghosh, Bibhas Chakraborty, Inbal Nahum-Shani, Megan E Patrick, Palash Ghosh
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究序贯多重随机化试验（SMART）中的最优自适应随机化设计，目标是在二值结局下寻找使总期望治疗失败人数最小的分配概率，同时约束预设目标函数的渐近方差固定。作者将自适应分配建模为约束优化问题，在保证动态治疗策略（DTR）价值函数估计量渐近方差达到预设界的前提下，通过响应自适应随机化最小化伦理代价。理论上探讨了最优自适应分配的渐近性质与方差约束的交互影响，模拟与 M-bridge（大学生酒精风险干预）真实 SMART 数据验证了方法在降低失败率与保持估计效率间的权衡。对您有用：该工作将纵向因果推断（SMART/DTR）中的设计优化与渐近效率约束结合，其约束优化框架和自适应随机化理论可迁移至您关注的纵向因果推断与效率理论研究中。
- **关键技术**: `sequential multiple-assignment randomized trial (SMART)`, `dynamic treatment regimes (DTRs)`, `response-adaptive randomization`, `constrained optimization`, `asymptotic variance constraint`
- **为什么对您有用**: SMART/DTR 属于您 primary interest 中的纵向因果推断（longitudinal CI）；本文在固定渐近方差的约束下优化分配概率，直接涉及效率理论（efficiency theory）与统计计算（约束优化），且应用部分契合流行病学因果推断。

### 7. [10.1093/biomtc/ujae148](https://doi.org/10.1093/biomtc/ujae148) — Estimation of a genetic Gaussian network using GWAS summary data
- **作者**: Yihe Yang, Noah Lorincz-Comi, Xiaofeng Zhu
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在 GWAS 汇总数据下，目标是估计多表型的遗传高斯网络（基于遗传相关矩阵的逆矩阵），但现有估计受估计误差和特异性多效性（idiosyncratic pleiotropy）偏差干扰。本文提出 EGG (estimation of genetic graph) 方法，利用多变量孟德尔随机化（MVMR）的技术同时消除上述两种偏差。EGG 估计的遗传网络可解释为在给定其他表型下表型间的共享生物学贡献，本质上是对精度矩阵（precision matrix）的去偏估计。模拟与真实数据分析表明，相比传统网络估计器，EGG 能有效消除偏差并恢复真实的条件依赖结构。对您有用：将 IV/MR 的偏差校正思想引入高维精度矩阵估计，对您在因果推断（IV/MR）与高维统计（网络/精度矩阵）交叉领域的方法论拓展有直接参考价值。
- **关键技术**: `multivariable Mendelian randomization`, `precision matrix estimation`, `pleiotropy bias correction`, `genetic Gaussian network`, `GWAS summary statistics`
- **为什么对您有用**: 将 IV/MR 的偏差校正机制引入高维精度矩阵（网络）估计，直接契合您在因果推断（IV/MR）与高维统计交叉方向的兴趣，且提供了流行病学 GWAS 数据的应用范式。

### 8. [10.1093/biomtc/ujae112](https://doi.org/10.1093/biomtc/ujae112) — On network deconvolution for undirected graphs
- **作者**: Zhaotong Lin, Isaac Pan, Wei Pan
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `new_theory`
- **摘要**: 本文研究无向图上 Network Deconvolution (ND) 的理论依据：给定描述总效应（边际关联）的网络，ND 旨在重构描述直接效应（条件关联）的网络。作者首先揭示 ND 隐含的线性模型假设，随后证明一个简洁等价结果——在无向图设定下 ND 与精度矩阵（precision matrix）的使用等价，从而为 ND 在无向图上的应用提供了严格的理论解释。此外，文章形式化刻画了对总效应图做缩放的效应。实证部分利用大规模 GWAS 数据，将 ND 用于对比身高与冠心病风险之间的边际遗传相关与条件遗传相关，结果与 ND 推断的因果有向图一致。对您而言，该文将直接/间接效应分解与精度矩阵联系起来的等价结果，可为 mediation 分析和条件独立性检验提供新的视角，且 GWAS 应用展示了流行病学数据中因果推断的一种可行路径。
- **关键技术**: `network deconvolution`, `precision matrix equivalence`, `direct vs indirect effect decomposition`, `linear structural model`, `GWAS genetic correlation`
- **为什么对您有用**: 直接/间接效应分解是 mediation 与因果图推断的核心问题，精度矩阵等价结果将图方法与高斯图模型/条件独立性联系起来，对您在因果推断（mediation、条件效应识别）和流行病学应用（GWAS 遗传相关）均有参考价值。

### 9. [10.1093/biomtc/ujae152](https://doi.org/10.1093/biomtc/ujae152) — Adaptive randomization methods for sequential multiple assignment randomized trials (smarts) via thompson sampling
- **作者**: Peter Norwood, Marie Davidian, Eric Laber
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在序贯多重分配随机试验（SMART）设定下，研究目标是多阶段动态治疗策略（DTR）的比较与最优嵌入策略的估计，关键挑战是响应自适应随机化（RAR）导致的非标准极限行为。本文提出基于Thompson Sampling（TS）的RAR算法，将随机化概率与处理最优的估计概率对齐。针对RAR引起的渐近非正态性，构建了有效的试验后推断程序，这是首个在多阶段试验中修正RAR非标准渐近性质的推断方法。实证基于真实SMART数据，表明TS能在提升受试者收益的同时不牺牲试验后比较的统计效率。对您有用：该文处理的多阶段DTR属于纵向因果推断范畴，其针对自适应随机化下非标准渐近行为的推断理论对理解复杂设计下的效率与假设检验有直接参考价值。
- **关键技术**: `Thompson Sampling`, `response-adaptive randomization`, `dynamic treatment regimes`, `non-normal asymptotic behavior`, `sequential multiple assignment randomized trials`
- **为什么对您有用**: 直接涉及纵向因果推断中的动态治疗策略（DTR）评估，且其针对自适应随机化导致的非标准渐近行为（渐近非正态）所提出的推断方法，对您在复杂实验设计下的数学统计与假设检验研究有理论参考价值。

### 10. [10.1093/biomtc/ujae141](https://doi.org/10.1093/biomtc/ujae141) — An adaptive enrichment design using Bayesian model averaging for selection and threshold-identification of predictive variables
- **作者**: Lara Maleyeff, Shirin Golchi, Erica E M Moodie, Marie Hudson
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文在精准医学临床试验的 adaptive enrichment 设计框架下，目标是从候选生物标志物中识别具有增强处理效应的亚群，并允许中期分析时限制入组。方法上，连续型生物标志物的处理效应修饰作用通过 free knot B-splines 灵活建模，关键参数通过 Bayesian model averaging (BMA) 在所有变量组合上边际化估计，避免预先指定标志物或假设线性关系。中期决策规则评估亚群处理效应的增强或减弱，支持 early termination for efficacy/futility 及入组限制。模拟比较了与现有方法的 operating characteristics。该设计虽为贝叶斯框架，但其处理效应异质性识别与非线性建模思路对您在 causal inference 中处理 treatment effect heterogeneity 及 nonparametric 建模有参考价值，但理论深度（如效率界、influence function）有限。
- **关键技术**: `Bayesian model averaging`, `free knot B-splines`, `adaptive enrichment design`, `subgroup identification`, `interim analysis decision rules`
- **为什么对您有用**: 与您 primary interest 中 causal inference 的 treatment effect heterogeneity 识别相关，非线性 B-spline 建模也触及 nonparametric theory；但整体为贝叶斯试验设计，缺乏频率派效率理论，对您核心理论兴趣的直接增益较弱，主要提供应用层面的设计思路借鉴。

### 11. [10.1093/biomtc/ujae132](https://doi.org/10.1093/biomtc/ujae132) — Bayesian pathway analysis over brain network mediators for survival data
- **作者**: Xinyuan Tian, Fan Li, Li Shen, Denise Esserman, Yize Zhao
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在遗传暴露→脑网络连接（矩阵型中介）→疾病发病时间（生存结局）的因果通路设定下，目标是量化脑网络的中介效应并保留全网络信息。方法核心包括：对生存结局建立对称矩阵变量加速失效时间（AFT）模型，对网络中介建立对称矩阵响应回归；通过 within-graph sparsity 与 between-graph shrinkage 的贝叶斯先验实现网络结构选择与去噪。模拟显示该方法优于将网络拆解为边向量的传统做法；ADNI 实证揭示了阿尔茨海默病的神经生物学可信通路。对您而言，该文将 mediation 分析拓展至矩阵型中介变量，其矩阵变量建模与稀疏先验设计可迁移至您关注的 mediation 理论与统计计算（矩阵算法）交叉方向。
- **关键技术**: `matrix-variate AFT model`, `symmetric matrix response regression`, `Bayesian mediation analysis`, `within-graph sparsity prior`, `between-graph shrinkage prior`, `accelerated failure time model`
- **为什么对您有用**: 直接关联您 primary interest 中的 causal mediation，将中介变量从标量/向量推广至对称矩阵，其矩阵变量建模思路与统计计算中的矩阵/张量方法相通，可作为 mediation 理论向高维结构化中介拓展的参考起点。

### 12. [10.1093/biomtc/ujae145](https://doi.org/10.1093/biomtc/ujae145) — A Bayesian framework for causal analysis of recurrent events with timing misalignment
- **作者**: Arman Oganisian, Anthony Girard, Jon A Steingrimsson, Patience Moyo
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在观察性重复事件研究中，当资格认定与治疗时间不一致（timing misalignment）且存在终止事件（如死亡）时，目标是识别和估计特定随访窗口内的平均因果效应。本文将时间错位问题转化为时变治疗框架：部分患者在资格认定时已接受治疗，另一部分则未接受但可能在后续存活期间切换治疗。在右删失下定义并识别了因果 estimand，估计采用 g-computation 程序，结合死亡与重复事件过程的联合半参数贝叶斯模型。实证分析基于 Medicare 理赔数据比较不同阿片类药物治疗下的住院率，避免了 ad hoc 方法导致的偏倚。对您有用：该文将时间错位转化为时变治疗问题的 identification 策略，以及联合半参数贝叶斯 g-computation 的估计思路，对纵向因果推断和流行病学应用有直接参考价值。
- **关键技术**: `g-computation`, `time-varying treatment`, `joint semiparametric Bayesian model`, `recurrent event process`, `timing misalignment`
- **为什么对您有用**: 直接涉及因果推断中的纵向/时变治疗设定，解决了资格与治疗时间错位的 identification 问题；同时提供了流行病学（Medicare 数据）的因果应用范例，对您在纵向因果推断和流行病学应用方向的思考有迁移价值。

### 13. [10.1093/biomtc/ujae129](https://doi.org/10.1093/biomtc/ujae129) — Sensitivity analysis for studies transporting prediction models
- **作者**: Jon A Steingrimsson, Sarah E Robertson, Sarah Voter, Issa J Dahabreh
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究预测模型从源人群向目标人群的迁移问题，设定为目标人群仅有协变量数据而结局缺失，识别依赖于结局与人群给定协变量条件独立的不可验证假设。针对该假设可能不成立的情况，作者提出了指数倾斜（exponential tilt）敏感性分析模型，以量化假设违背对模型表现度量推断的影响。在指数倾斜模型下，推导了目标人群风险的识别公式，并构建了相应的估计量。理论方面，研究了估计量的大样本性质（渐近正态性），实证方面将方法应用于肺癌筛查数据。对您有用：直接对应您 primary interest 中的因果推断敏感性分析，指数倾斜框架在处理 transportability/选择偏倚时具有方法可迁移性，且应用部分契合您对流行病学数据集的 secondary interest。
- **关键技术**: `transportability`, `exponential tilt model`, `sensitivity analysis`, `identification under missing data`, `asymptotic properties`
- **为什么对您有用**: 直接对应 primary interest 中的因果推断敏感性分析，指数倾斜模型为处理 transportability 假设违背提供了具体框架；肺癌筛查应用契合 secondary interest 中的流行病学数据集。

### 14. [10.1093/biomtc/ujae139](https://doi.org/10.1093/biomtc/ujae139) — A generalized logrank-type test for comparison of treatment regimes in sequential multiple assignment randomized trials
- **作者**: Anastasios A Tsiatis, Marie Davidian
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在 SMART（序贯多重赋值随机试验）框架下，目标是基于右删失生存数据比较不同动态干预策略（embedded regimes）的生存分布，核心假设为顺序随机化与无信息删失。本文提出一种广义 logrank 型检验，通过在加权函数中纳入基线及随时间变化的协变量来提升检验效率。该检验统计量基于各 regime 下期望风险集的估计构建，将标准 logrank 检验推广至多阶段决策情境，并明确澄清了从观察性数据做因果推断所需的可识别性假设。理论上，该方法包络并改进了现有 SMART 下的生存比较方法，其协变量调整机制与半参数效率理论紧密相关。模拟与急性早幼粒细胞白血病（APL）真实数据验证了其功效提升与实用性。对您有用：直接关联 longitudinal causal inference 与 hypothesis testing，展示了如何在复杂纵向因果设定下通过协变量调整构建更有效的检验统计量。
- **关键技术**: `dynamic treatment regimes`, `SMART design`, `logrank test`, `covariate adjustment for efficiency`, `sequential randomization assumption`, `survival analysis`
- **为什么对您有用**: 直接关联您 primary interest 中的 longitudinal causal inference 与 hypothesis testing；展示了在多阶段纵向因果设定下如何通过协变量调整提升检验效率并澄清因果假设，对研究动态干预的半参数检验有直接借鉴价值。

### 15. [10.1093/biomtc/ujae155](https://doi.org/10.1093/biomtc/ujae155) — De-biasing the bias: methods for improving disparity assessments with noisy group measurements
- **作者**: Solvejg Wastvedt, Joshua Snoke, Denis Agniel, Julie Lai, Marc N Elliott, Steven C Martino
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在算法公平性/健康差异评估中，种族/民族分组变量常以 imputed probabilities（如 BISG 算法输出）而非真实标签测量，本文研究该测量误差如何导致差异度量的统计偏差，并提出校正与敏感性分析方法。核心方法包括：(1) 对常用公平性指标（如 FPR/FNR 差异等）证明统计偏差的理论上界，刻画误差对 disparity estimate 的影响范围；(2) 提出敏感性分析框架，允许从业者在一系列假定的组概率误差水平下评估差异度量的偏倚方向与幅度。在骨质疏松临床决策支持算法的案例中，使用 BISG 推算的种族信息展示了方法实操流程。对您有用：本文的敏感性分析思路可直接迁移到因果推断中处理变量/分组变量 misclassification 的设定，且提供了流行病学应用中的真实数据管道与 BISG 数据集参考。
- **关键技术**: `sensitivity analysis for measurement error`, `theoretical bias bounds for fairness metrics`, `BISG (Bayesian Improved Surname Geocoding)`, `disparity assessment with probabilistic group membership`, `misclassification bias correction`
- **为什么对您有用**: 敏感性分析是您 primary interest 中因果推断的核心子方向，本文将敏感性分析从 unmeasured confounding 迁移到分组变量测量误差设定，思路可迁移；同时是流行病学（secondary）中带真实数据管道的应用。

### 16. [10.1093/biomtc/ujae123](https://doi.org/10.1093/biomtc/ujae123) — How to achieve model-robust inference in stepped wedge trials with model-based methods?
- **作者**: Bingkai Wang, Xueqi Wang, Fan Li
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在阶梯楔形（stepped wedge）集群随机试验中，目标是边际处理效应的非参数 estimand（基于潜在结果定义，可为日历时间/暴露时间的函数），研究在模型误设下基于模型的方法（线性混合模型、GEE with independence/exchangeable/nested exchangeable working correlation）何时仍能给出一致估计。核心理论结果：一致性通常仅要求处理效应结构正确设定，而工作模型的其余部分（协变量函数形式、随机效应、误差分布）可误设，sandwich variance estimator 提供有效推断；在非恒等链接函数或 ratio estimand 下，需额外 g-computation 步骤才能实现模型稳健推断。模拟与一项已完成的阶梯楔形试验再分析验证了理论。对您有用：该工作将 semiparametric model-robustness 思路引入纵向集群试验的因果 estimand，g-computation + sandwich 的组合对您在 longitudinal causal inference 与 semiparametric efficiency 方向的研究有直接参考价值。
- **关键技术**: `g-computation`, `sandwich variance estimator`, `linear mixed models`, `GEE with working correlation`, `model-robust inference`, `potential outcomes estimands`
- **为什么对您有用**: 直接连接您 primary interest 中的 longitudinal causal inference 与 semiparametric theory：证明了对非参数边际 estimand 仅需处理效应结构正确即可一致估计，放松了对工作模型其余部分的假设，且 g-computation 步骤在非恒等链接下的必要性是新的理论洞见，可迁移到其他纵向因果设定。

### 17. [10.1093/biomtc/ujae135](https://doi.org/10.1093/biomtc/ujae135) — Estimating marginal treatment effect in cluster randomized trials with multi-level missing outcomes
- **作者**: Chia-Rui Chang, Rui Wang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在整群随机试验（CRT）的多层结构（个体嵌套于子群、子群嵌套于群）下，针对个体与群组层面的信息性缺失，目标是边际处理效应的识别与估计。现有 IPW-GEE 方法仅处理个体缺失，忽略群组整体脱落会导致偏误；本文提出基于加权广义估计方程（WGEE）的新估计量，构建了多层乘法稳健估计量。理论证明只要每个聚类层级上多个倾向得分模型中至少有一个被正确设定，该估计量即具有一致性与渐近正态性。模拟研究评估了有限样本表现，并应用于马达加斯加疟疾干预的 CRT 数据。对您有用：该文将缺失数据框架下的多重稳健性扩展至多层因果推断设定，其 WGEE 与倾向得分建模策略可直接迁移至流行病学群组随机化试验的因果分析中。
- **关键技术**: `weighted generalized estimating equations`, `multiply robust estimation`, `multi-level propensity score`, `inverse probability weighting`, `informative missingness`
- **为什么对您有用**: 直接关联 primary interest 中的因果推断（缺失数据下的处理效应估计）与半参数/效率理论（多重稳健性），同时提供了 secondary interest 流行病学（疟疾干预 CRT）的真实数据应用范例。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 3 篇)*

### 1. [10.1093/biomtc/ujae153](https://doi.org/10.1093/biomtc/ujae153) — Debiased high-dimensional regression calibration for errors-in-variables log-contrast models
- **作者**: Huali Zhao, Tianying Wang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在微生物组高维组成型协变量（compositional covariates）存在测量误差的设定下，本文针对线性 log-contrast 模型提出去偏回归校准（debiased regression calibration）方法，目标是对误差污染后的高维系数进行有效统计推断。核心机制是先用校准方程修正测量误差带来的偏差，再通过去偏（debiasding）步骤构造 one-step 修正估计量，在相对宽松的稀疏度条件下建立估计量的渐近正态性，从而支持置信区间构造。关键技术工具包括 Lasso 类惩罚估计、误差-in-变量校准、以及去偏 Lasso 的 low-dimensional projection 思想。数值实验和微生物组真实数据应用表明，该方法有效消除偏差并达到名义覆盖概率。对您有用之处：这是高维去偏推断在测量误差设定下的扩展，与您关注的 debiased ML / 高维推断效率理论直接相关，且宽松稀疏条件下的渐近正态性结果可为您的高维假设检验工作提供参考。
- **关键技术**: `debiased Lasso`, `regression calibration`, `errors-in-variables`, `log-contrast model`, `compositional data`, `asymptotic normality under relaxed sparsity`
- **为什么对您有用**: 直接关联您的高维统计与效率理论（debiased ML）方向：将去偏推断从标准高维线性模型推广到测量误差+组成型约束设定，且在更弱稀疏条件下获得渐近正态性，对您研究高维假设检验的放松假设有借鉴价值。

### 2. [10.1093/biomtc/ujae109](https://doi.org/10.1093/biomtc/ujae109) — Heterogeneity-aware integrative regression for ancestry-specific association studies
- **作者**: Aaron J Molstad, Yanwei Cai, Alexander P Reiner, Charles Kooperberg, Wei Sun, Li Hsu
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在多祖先基因组研究中，目标是构建 ancestry-specific 的 pQTL 模型以预测蛋白表达，允许不同群体的回归系数与误差方差异质。提出一种跨群体信息借用的惩罚极大似然估计量，通过替代参数化使目标函数凸且惩罚尺度不变。为提升计算效率，提出近似算法并研究其理论性质。实证表明该方法显著提升非洲裔人群的蛋白表达预测精度，并在下游 PWAS 中发现多个与血脂性状的关联。对您有用：该文在高维惩罚回归中的凸优化重构与计算加速策略，对您在统计计算与高维统计方面的研究有直接借鉴价值；其流行病学基因组应用也契合您的次级兴趣。
- **关键技术**: `penalized maximum likelihood`, `convex optimization`, `scale-invariant penalty`, `approximate algorithm`, `multi-ancestry regression`, `pQTL modeling`
- **为什么对您有用**: 涉及高维惩罚回归的凸优化重构与计算加速（契合您的高维统计与统计计算兴趣），并在流行病学基因组数据中展示了异质性建模的应用（契合您的流行病学应用兴趣）。

### 3. [10.1093/biomtc/ujae158](https://doi.org/10.1093/biomtc/ujae158) — Structured feature ranking for genomic marker identification accommodating multiple types of networks
- **作者**: Yeheng Ge, Tao Li, Xingdong Feng, Mengyun Wu, Hailong Liu
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 3/10 · novelty: `sharper_rate`
- **摘要**: 在高维基因组标记筛选设定下，目标是识别与复杂疾病表型相关的特征，同时克服传统边际特征排序忽略预测变量间网络依赖结构的局限。本文提出一种基于 Laplacian 正则化的结构化特征排序方法，创新性地处理了多种网络场景（先验已知网络与数据驱动估计网络），并通过调节参数控制网络中的噪声与不确定性。理论上严格证明了相较于原始边际度量，所提网络结构化度量在温和条件下具有更快的收敛速率，并满足 sure screening 性质。模拟与 TCGA 黑色素瘤数据分析验证了其有限样本性能与实用性。该文在高维特征筛选中引入网络结构并给出更快的收敛速率，对您研究高维统计理论（特别是 feature screening 与 Laplacian regularization 结合的收敛性质）有直接参考价值。
- **关键技术**: `feature screening`, `Laplacian regularization`, `sure screening property`, `network-structured ranking`, `convergence rate`
- **为什么对您有用**: 直接涉及高维统计中的特征筛选理论，并在温和条件下给出了比边际方法更快的收敛速率与 sure screening 保证，对您关注的高维统计理论（feature screening 与收敛率改进）有参考价值。

## 非参数 / 半参数  *(nonparam_semipara, 8 篇)*

### 1. [10.1093/biomtc/ujae138](https://doi.org/10.1093/biomtc/ujae138) — Large-scale survival analysis with a cure fraction
- **作者**: Bo Han, Xiaoguang Wang, Liuquan Sun
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在含治愈分数的大规模生存数据设定下，目标是半参数治愈回归模型中回归参数的估计与推断，假设潜伏期服从半参数比例风险模型而发病率无需参数设定。提出以易感概率（susceptible probability）为权重的加权估计方程方法，通过非参数估计权重实现回归参数的稳定估计。进一步提出基于数据块的递归概率加权估计方法，在大规模或在线场景下实现计算与内存效率。建立了所提估计量的渐近正态性等渐近性质。模拟与真实数据应用验证了方法的有限样本表现。对您有用之处在于：其半参数治愈模型的加权估计方程构造与渐近理论可直接迁移至其他 semiparametric inference 问题，递归分块计算策略对大规模统计计算有参考价值。
- **关键技术**: `mixture cure model`, `probability-weighted estimating equation`, `semiparametric proportional hazards`, `recursive block estimation`, `nonparametric weight estimation`
- **为什么对您有用**: 半参数治愈模型的加权估计方程与渐近理论直接关联您的 semiparametric theory 兴趣，递归分块计算策略对 statistical computing 方向有参考价值，且流行病学生存数据应用提供了真实数据集参考。

### 2. [10.1093/biomtc/ujae121](https://doi.org/10.1093/biomtc/ujae121) — Modeling longitudinal skewed functional data
- **作者**: Mohammad Samsul Alam, Ana-Maria Staicu
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出一种针对纵向函数数据的建模框架，旨在处理逐点偏斜性，通过 copula 方法将边际逐点变异与复杂的纵向及函数依赖解耦。边际变异由参数分布函数描述，以捕捉随时间和函数参数平滑变化的偏斜性；联合依赖则通过基于低秩近似的协方差的高斯 copula 来量化。该模型为逐点分位数估计和新时间点的完整轨迹预测提供了统一框架。数值模拟和多发性硬化症患者的扩散张量成像（DTI）数据应用验证了方法的有效性，并提供了 R 包 sLFDA。对您而言，其 copula 解耦与低秩协方差近似的技术思路在 semiparametric theory 和 statistical computing 方面有一定参考价值，尽管核心应用场景偏离因果推断与高维理论。
- **关键技术**: `Gaussian copula`, `low-rank covariance approximation`, `functional data analysis`, `pointwise quantile estimation`, `skewness modeling`
- **为什么对您有用**: 涉及 copula 解耦与低秩协方差近似，与您关注的 semiparametric theory 和 statistical computing 有方法交集，但核心是函数数据建模而非因果或高维效率理论。

### 3. [10.1093/biomtc/ujae150](https://doi.org/10.1093/biomtc/ujae150) — Time-dependent prognostic accuracy measures for recurrent event data
- **作者**: R Dey, D E Schaubel, J A Hanley, P Saha-Chaudhuri
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `new_theory`
- **摘要**: 在复发事件数据设定下，本文旨在刻画基线生物标志物的时变预测精度，基于半参数脆弱模型同时处理标志物信息性与未观测异质性。作者提出了新的预测精度度量，并在半参数框架下构建了相应的估计量。理论上，利用经验过程等工具严格推导了该估计量的渐近性质（一致性与渐近正态性），模拟显示有限样本下偏差极小且覆盖率合适。实证部分将方法应用于囊性纤维化患者基线肺活量（FEV）对反复肺病急性发作的预测评估。对您有用之处：该文的半参数脆弱模型渐近理论推导对您在半参数/效率理论方面的研究有直接参考价值，且复发事件建模与流行病学应用契合您的次级兴趣。
- **关键技术**: `semiparametric frailty model`, `prognostic accuracy measures`, `recurrent event data`, `asymptotic properties`, `time-dependent accuracy`
- **为什么对您有用**: 半参数脆弱模型的渐近性质推导与您在半参数理论及效率理论的兴趣直接相关；同时，复发事件数据的建模与流行病学应用契合您的次级兴趣，提供了可迁移的纵向数据分析范式。

### 4. [10.1093/biomtc/ujae128](https://doi.org/10.1093/biomtc/ujae128) — Robust model averaging approach by Mallows-type criterion
- **作者**: Miaomiao Wang, Kang You, Lixing Zhu, Guohua Zou
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在均值回归的模型平均框架下，针对现有基于 OLS 或 MLE 的方法对异常值高度敏感的问题，目标是构建具有有界影响函数的稳健模型平均估计量。对每个候选模型构建广义 M (GM) 估计量，并基于 GM 型损失函数对最终预测误差进行渐近展开，由此建立稳健的 Mallows 型权重选择准则。理论上证明了权重估计量向理论最优权重向量的相合性，并严格推导了所提估计量的渐近性质。通过证明该估计量具有有界影响函数来刻画其稳健性，并定义了经验预测影响函数以量化评估稳健程度。模拟与实证表明该方法在响应变量和/或协变量被污染时仍优于传统模型选择与平均方法。对您有用：影响函数的推导与渐近展开技术直接关联您关注的半参数效率理论与数理统计基础，且模型平均为处理模型不确定性提供了不同于单一模型 DML 的视角。
- **关键技术**: `Mallows-type criterion`, `Generalized M-estimator`, `influence function`, `asymptotic expansion`, `robust model averaging`
- **为什么对您有用**: 影响函数的推导与渐近展开技术直接关联您关注的半参数效率理论与数理统计基础；模型平均权重准则的构建为处理模型不确定性提供了不同于单一模型 DML 的视角。

### 5. [10.1093/biomtc/ujae136](https://doi.org/10.1093/biomtc/ujae136) — A multivariate Polya tree model for meta-analysis with event-time distributions
- **作者**: Giovanni Poli, Elena Fountzilas, Apostolia-Maria Tsimeridou, Peter Müller
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在 meta-analysis 设定下，本文针对多组 event-time 分布 $G_1,\dots,G_n$ 提出了一种多元 Polya tree (PT) 非参数贝叶斯先验。核心机制是将标准 PT 构造中独立的 Beta 分裂概率替换为基于研究协变量索引的高斯过程（GP）先验（作用在 logit 尺度上），从而在相似研究间引入更强的先验相关性。该构造保留了条件共轭的后验更新性质，简化了 event-time 数据的贝叶斯计算。实证部分将该模型应用于癌症免疫治疗研究的 meta-analysis。对您而言，虽然本文属于贝叶斯非参数路线，与您关注的频率派半参数效率界及 DML 路线不同，但其利用 GP 诱导多元非参数分布相关性的思路在流行病学队列/生存分析的非参数建模中仍有边缘参考价值。
- **关键技术**: `multivariate Polya tree`, `Gaussian process prior`, `conditionally conjugate updating`, `meta-analysis of event-time data`, `logit splitting probabilities`
- **为什么对您有用**: 涉及非参数理论（多元 Polya tree）与流行病学应用（癌症免疫治疗 meta-analysis），但属于贝叶斯非参数路线，与您关注的频率派半参数效率界及 DML 方法差异较大，仅作非参数建模思路的边缘参考。

### 6. [10.1093/biomtc/ujae111](https://doi.org/10.1093/biomtc/ujae111) — Bayesian network-guided sparse regression with flexible varying effects
- **作者**: Yangfan Ren, Christine B Peterson, Marina Vannucci
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维回归的特征选择设定下，本文提出 VERGE 方法，利用预测变量间的网络结构并结合半参数变系数模型刻画个体协变量对预测效应的调节作用。方法采用贝叶斯框架，区分用于预测结局的特征变量与调节效应的个体协变量；通过 spike-and-slab 先验实现网络连接特征与调节协变量的同时选择；网络结构通过图估计融入特征选择过程，鼓励相关预测变量被共同选中。模拟显示其在特征选择和预测精度上优于现有方法；在肠道微生物-肥胖流行病学应用中识别了关键类群及生态依赖。对您可能有用：变系数框架的半参数思想与您关注的半参数理论相关，且高维贝叶斯图结构选择可作对比参考。
- **关键技术**: `varying coefficient model`, `spike-and-slab prior`, `Bayesian graph estimation`, `high-dimensional feature selection`, `network-structured shrinkage`
- **为什么对您有用**: 变系数模型属于半参数建模范畴，与您关注的半参数理论相关；高维特征选择与图结构推断的贝叶斯方法可为您在效率理论或频率派高维推断中的研究提供对比视角；流行病学应用（微生物组-肥胖）提供了真实数据集参考。

### 7. [10.1093/biomtc/ujae131](https://doi.org/10.1093/biomtc/ujae131) — Dynamic factor analysis with dependent Gaussian processes for high-dimensional gene expression trajectories
- **作者**: Jiachen Cai, Robert J B Goudie, Colin Starr, Brian D M Tom
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维纵向基因表达数据设定下，本文提出贝叶斯稀疏因子分析将观测轨迹映射到低维通路表达轨迹，并用依赖高斯过程(DGP)刻画不同通路间的相关性，从而放松了纵向因子分析中经典的因子独立性假设。方法核心是将因子载荷的稀疏结构（对应基因-通路归属）与因子轨迹的DGP先验结合，通过Monte Carlo EM (MCEM) 算法拟合：E步用标准MCMC采样，M步调用GPFDA包做DGP超参数的MLE。模拟与真实数据分析表明，相比独立因子模型，DGP因子模型在恢复通路轨迹形状、揭示基因-通路关系及预测基因表达（更近的点估计与更窄的预测区间）上表现更优。MCEM的模块化结构使其可推广到其他含DGP组件的复杂模型，配套R包DGP4LCF已上线CRAN。对您而言，该文的因子降维思路与高维统计中spiked covariance / factor model的频率学派理论形成贝叶斯对照，MCEM计算方案及GP先验的模块化设计也可为纵向因果推断中的潜变量建模提供计算参考。
- **关键技术**: `Bayesian sparse factor analysis`, `dependent Gaussian processes`, `Monte Carlo EM`, `MCMC sampling`, `longitudinal factor model`, `GPFDA`
- **为什么对您有用**: 因子降维与高维统计中spiked covariance / factor model的频率学派理论形成贝叶斯对照；MCEM模块化计算方案及GP先验设计可为纵向因果推断中的潜变量建模提供可迁移的计算思路。

### 8. [10.1093/biomtc/ujae113](https://doi.org/10.1093/biomtc/ujae113) — Functional generalized canonical correlation analysis for studying multiple longitudinal variables
- **作者**: Lucas Sort, Laurent Le Brusquet, Arthur Tenenhaus
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文提出功能广义典型相关分析（FGCCA）框架，旨在探索多个联合观测的随机过程（纵向函数数据）之间的关联，核心设定为多块正则化广义典型相关分析模型，对稀疏和不规则观测具有鲁棒性。方法层面，作者证明了求解算法的单调收敛性质，并引入贝叶斯方法来估计典型成分。进一步，框架被扩展以整合单变量或多变量响应变量，从而支持预测性任务。模拟研究与真实纵向数据集验证了方法的有限样本表现。对您而言，尽管本文侧重关联探索而非因果识别，但其处理稀疏不规则纵向数据的算法收敛性分析与多块降维思路，可为纵向因果推断中高维时变变量的降维与计算提供方法借鉴。
- **关键技术**: `functional generalized canonical correlation analysis`, `multiblock regularized GCCA`, `monotonic convergence algorithm`, `Bayesian canonical component estimation`, `sparse irregular longitudinal data`
- **为什么对您有用**: 本文处理纵向函数数据的降维与关联分析，虽然非因果推断，但其针对稀疏不规则纵向数据的算法收敛性证明和多块整合扩展，对您在纵向因果推断（如时变混杂/中介）中的高维变量降维与统计计算有参考价值。

## 数理统计 / 假设检验  *(hypothesis_testing, 6 篇)*

### 1. [10.1093/biomtc/ujae142](https://doi.org/10.1093/biomtc/ujae142) — Joint mirror procedure: controlling false discovery rate for identifying simultaneous signals
- **作者**: Linsui Deng, Kejun He, Xianyang Zhang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在中介分析或可重复性分析等需要联合检验多个假设以识别“同时显著信号”的场景下，本文研究如何在有限样本下控制错误发现率（FDR）。提出联合镜像（JM）程序，通过迭代方法基于逐步揭示的信息缩小拒绝域，直至错误发现比例的保守估计低于目标FDR水平。引入复合FDR（cFDR）这一更严格的误差度量，根据零假设成分的数量对错误发现进行加权。利用留一法（leave-one-out）技术证明了JM程序在有限样本下对cFDR的控制，并提出可融入偏序信息的高效算法。模拟与实证表明，该方法在特征间相依的情况下仍能有效控制cFDR并提升统计功效，且成功应用于真实中介分析与可重复性分析。对您有用：该文将多重检验的前沿方法（镜像过程、有限样本FDR控制）与因果推断中的中介分析结合，为您在中介效应筛选中的假设检验问题提供了直接可用的方法与理论保证。
- **关键技术**: `joint mirror procedure`, `composite FDR (cFDR)`, `leave-one-out technique`, `finite-sample FDR control`, `partial ordering information`
- **为什么对您有用**: 直接关联您在因果推断（中介分析）与假设检验方向的交叉兴趣；提供了在中介效应筛选中控制cFDR的新方法与有限样本理论保证，可迁移至高维中介分析场景。

### 2. [10.1093/biomtc/ujae114](https://doi.org/10.1093/biomtc/ujae114) — Changepoint detection on daily home activity pattern: a sliced Poisson process method
- **作者**: Israel Martínez-Hernández, Rebecca Killick
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在日常居家活动监测场景下，目标是在非齐次 Poisson 过程（IPP）序列中检测跨天的行为模式变点，假设每天内事件时间服从 rate function 随时刻变化的 IPP，每天为一次独立观测。作者提出 sliced Poisson process 方法，将一天内事件时间切片建模，利用局部变点信息汇总检测跨天变化；rate function 的刻画方式未明确给出非参数/半参数的收敛率或效率界。方法通过模拟数据评估，并提供可视化与可解释的变点及趋势追踪，但缺乏变点估计的渐近理论（如收敛率、检验 size/power 的极限分布）。主要贡献在于建模框架与应用可解释性，理论深度有限；对您而言，若关注变点检测的假设检验理论（似然比统计量极限分布）或非参数 rate function 估计的效率界，本文提供应用场景但理论收益不大。
- **关键技术**: `inhomogeneous Poisson process`, `changepoint detection`, `sliced Poisson process`, `daily activity modeling`, `likelihood-based detection`
- **为什么对您有用**: 与您 hypothesis testing 兴趣中的变点检测方向相邻，但本文偏应用建模，缺乏渐近理论与效率分析，理论迁移价值有限；居家活动监测数据结构对流行病学应用有参考价值。

### 3. [10.1093/biomtc/ujae119](https://doi.org/10.1093/biomtc/ujae119) — A formal goodness-of-fit test for spatial binary Markov random field models
- **作者**: Eva Biswas, Andee Kaplan, Mark S Kaiser, Daniel J Nordman
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 针对空间二值 Markov 随机场 (MRF) 模型，本文提出一种正式的拟合优度 (GOF) 检验，以解决空间二值数据中邻域结构难以评估且缺乏模型诊断工具的问题。检验统计量基于拟合条件概率构造了一种条件 Moran's I，用于检测模型形式（特别是邻域结构设定）的偏离。该方法通过条件概率残差捕捉空间依赖性偏离，并在数值模拟中展示了在检测零模型偏离时的检验功效。实证分析使用了 Besag 的 endive 数据和爱荷华州草雀繁殖模式数据。对您而言，本文展示了如何针对复杂依赖结构（如空间/网络）构建假设检验，其条件 Moran's I 的构造思路可为您在因果推断或高维假设检验中处理依赖结构提供参考。
- **关键技术**: `goodness-of-fit test`, `Markov random field`, `conditional Moran's I`, `spatial binary data`, `model diagnostics`
- **为什么对您有用**: 直接关联您在 mathematical statistics (hypothesis testing) 的兴趣；虽然聚焦空间统计，但针对复杂依赖结构构造 GOF 检验统计量（条件 Moran's I）的思路，对处理因果推断或网络/空间依赖下的假设检验有方法学借鉴价值。

### 4. [10.1093/biomtc/ujae108](https://doi.org/10.1093/biomtc/ujae108) — Group sequential testing of a treatment effect using a surrogate marker
- **作者**: Layla Parast, Jay Bartroff
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在使用替代标志物（surrogate marker）进行因果效应检验的设定下，本文研究如何利用纵向重复测量的替代标志物信息进行成组序贯检验（group sequential testing），以实现试验的提前停止。基于先验研究中替代标志物与主要结局的联合分布，作者采用非参数框架构建当前仅含替代标志物信息的检验统计量。核心机制在于推导多个时间点上此类非参数检验统计量的相关性性质，并据此计算控制总体I类错误率的有效性与无效性停止边界（stopping boundaries）。模拟研究与两个AIDS临床试验数据验证了该序贯检验的有限样本表现。对您有用：该文将非参数替代标志物检验与成组序贯设计结合，直接连接了您对因果推断（替代标志物/中介）与假设检验（序贯检验）的双重兴趣，且提供了流行病学临床试验的应用范例。
- **关键技术**: `group sequential testing`, `surrogate marker`, `nonparametric test`, `stopping boundaries`, `correlated test statistics`
- **为什么对您有用**: 直接连接因果推断（替代标志物/中介分析）与假设检验（成组序贯设计）两个核心兴趣，并在流行病学（AIDS临床试验）数据上展示了应用。

### 5. [10.1093/biomtc/ujae157](https://doi.org/10.1093/biomtc/ujae157) — Spatially adaptive variable screening in presurgical functional magnetic resonance imaging data analysis
- **作者**: Yifei Hu, Xinge Jessie Jeng
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在术前 fMRI 体素级多重检验设定下，目标是控制假阴性（漏检功能脑区）而非传统假阳性，基于 voxel-specific mixture model 提出新度量 Bayesian missed discovery rate (BMDR)。核心方法是在 BMDR 框架下构建 variable screening 程序，利用 fMRI 数据的空间相关结构提升边界信号体素的保留率；该程序完全 data-driven，无需手动阈值。与现有 FDR/FNR 控制方法的关键区别在于直接在体素水平调控假阴性并融入空间信息。数值实验表明，相比 state-of-the-art 方法，新方法在保留边界微弱信号体素方面更优，同时更干净地分离功能区域与背景噪声。对您而言，该文在多重检验中翻转错误类型优先级（假阴性优先）的思路，以及空间结构辅助高维 screening 的策略，可迁移至您关注的 hypothesis testing 与高维 variable screening 子方向。
- **关键技术**: `Bayesian missed discovery rate`, `voxel-specific mixture model`, `spatial variable screening`, `false negative control`, `multiple testing with spatial structure`
- **为什么对您有用**: 该文将多重检验的错误控制从 FDR 翻转为假阴性优先，并提出空间结构辅助的高维 screening 程序，思路可迁移至您 primary interest 中的 hypothesis testing（错误率重新定义）与高维 variable screening 子方向。

### 6. [10.1093/biomtc/ujae125](https://doi.org/10.1093/biomtc/ujae125) — A new robust approach for the polytomous logistic regression model based on Rényi’s pseudodistances
- **作者**: Elena Castilla
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多项逻辑回归模型下，针对误分类误差导致的最大似然估计(MLE)不稳健问题，本文提出基于 Rényi 伪距离(RP)的最小 RP 估计族。该估计族由调节参数 α≥0 控制，当 α=0 时退化为经典 MLE；同时基于此距离构建了稳健的 Wald 型检验统计量。其稳健机制在于通过 α 调整概率分布间的伪距离度量，降低异常或误分类样本对目标函数的贡献权重。理论与模拟表明，在存在误分类误差时，RP 估计相比 MLE 具有更小的偏差，且 Wald 型检验能更好地维持名义水平。对您可能有用：虽然属于参数稳健推断，但其对 Wald 型检验稳健性的构造思路可为您的假设检验兴趣提供参考，尤其在分类结局存在测量误差时。
- **关键技术**: `Rényi pseudodistance`, `polytomous logistic regression`, `robust estimation`, `Wald-type test`, `misclassification error`
- **为什么对您有用**: 涉及假设检验（Wald-type test）的稳健性构造，属于数理统计范畴；虽然未触及半参数效率或高维，但对分类数据测量误差下的稳健推断提供了一种参数化思路，可作假设检验方向的边缘参考。

## 统计计算 / 算法  *(stat_computing, 7 篇)*

### 1. [10.1093/biomtc/ujae146](https://doi.org/10.1093/biomtc/ujae146) — Unlocking the power of multi-institutional data: Integrating and harmonizing genomic data across institutions
- **作者**: Yuan Chen, Ronglai Shen, Xiwen Feng, Katherine Panageas
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在多中心基因组数据（GENIE BPC）整合设定下，目标是克服基因面板差异与患者异质性，提取降噪的低维潜变量以捕捉真实突变模式。提出 Bridge 模型，采用分位数匹配潜变量方法推导整合特征，保留非共有基因信息并最大化数据利用率。该方法通过跨面板信息共享提升学习效率与泛化能力，解决高维稀疏突变与弱信号问题。仿真验证了参数估计性质，在六种癌症真实数据中提取的潜特征在生存预测上持续表现优异。对您而言，该文的高维稀疏数据整合策略与分位数匹配潜变量方法，可为多源异质数据的降维计算提供参考，且 GENIE BPC 数据集具有流行病学应用价值。
- **关键技术**: `quantile-matched latent variable model`, `multi-institutional data harmonization`, `high-dimensional sparse data integration`, `information sharing across panels`, `survival prediction`
- **为什么对您有用**: 涉及高维稀疏数据的降维与多源异质数据整合计算，其分位数匹配潜变量思路对处理高维统计中的信息损失有参考价值，同时 GENIE BPC 临床数据集对流行病学应用有数据集价值。

### 2. [10.1093/biomtc/ujae107](https://doi.org/10.1093/biomtc/ujae107) — Composite dyadic models for spatio-temporal data
- **作者**: Michael R Schwob, Mevin B Hooten, Vagheesh Narasimhan
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 在景观遗传学等时空数据设定下，目标是推断控制基因流的空间机制，但现有方法常忽略时间依赖且计算不可行。本文提出贝叶斯层次二元（dyadic）模型，通过构建全连接网络容纳时空依赖，并引入归一化复合似然（normalized composite likelihoods）处理时空相关性，从而在大数据集下实现计算可扩展性。该模型还整合了物理统计模型中常见的物理机制。方法应用于青铜时代欧洲古人类DNA数据，推断影响人类迁徙的机制。对您而言，若关注统计计算中复合似然的近似推断与可扩展性，或对群体遗传学时空数据建模感兴趣，本文的计算方案与数据集具有参考价值。
- **关键技术**: `composite likelihood`, `Bayesian hierarchical model`, `dyadic data`, `spatio-temporal dependence`, `normalized composite likelihoods`
- **为什么对您有用**: 涉及统计计算中复合似然近似推断与可扩展性算法，且包含古人类DNA的时空数据应用，对关注计算方法或群体遗传学数据的研究者有一定参考价值。

### 3. [10.1093/biomtc/ujae130](https://doi.org/10.1093/biomtc/ujae130) — A hierarchical random effects state-space model for modeling brain activities from electroencephalogram data
- **作者**: Xingche Guo, Bin Yang, Ji Meng Loh, Qinxia Wang, Yuanjia Wang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多通道静息态 EEG 信号分析中，目标是估计脑区连接的时空动态模式，同时处理组间与个体间异质性。本文提出随机效应状态空间模型 (RESSM)，对时间动态矩阵和空间映射矩阵引入多层随机效应，允许脑连接模式随时间变化以刻画非平稳性。模型在贝叶斯层次框架下通过 Gibbs sampler 拟合，直接对高维随机效应矩阵建模而不施加低秩或稀疏等结构约束，并讨论了可识别性问题的处理。模拟表明参数估计与推断有效；应用于 MDD 多中心临床试验数据，发现患者与健康对照在静息态脑时间动态上存在显著差异，且 RESSM 提取的个体水平特征对异质性处理效应 (HTE) 的预测优于传统频带功率。对您而言，高维随机效应矩阵的无约束估计与 Gibbs 计算方案可参考于统计计算方向，MDD 临床试验数据集对流行病学应用方向有数据价值。
- **关键技术**: `Bayesian hierarchical model`, `state-space model`, `Gibbs sampler`, `high-dimensional random effects matrices`, `non-stationarity modeling`, `identifiability`
- **为什么对您有用**: 高维随机效应矩阵无约束估计与 Gibbs 计算方案对统计计算方向有参考价值；MDD 多中心临床试验数据集对流行病学应用方向有数据集价值，HTE 预测部分与因果推断中的异质性处理效应估计有松散关联。

### 4. [10.1093/biomtc/ujae115](https://doi.org/10.1093/biomtc/ujae115) — Temporal generative models for learning heterogeneous group dynamics of ecological momentary assessment data
- **作者**: Soohyun Kim, Young-geun Kim, Yuanjia Wang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在生态瞬时评估（EMA）纵向数据设定下，目标是刻画异质性群体动态，现有 mixed-effect model 需对固定/随机效应及相关结构做强假设，而 RTRBM 未利用协变量捕捉群体异质性。作者提出 HDRBM，在 recurrent temporal restricted Boltzmann machine 框架中引入协变量调制隐层动态，使不同协变量子群体拥有差异化的转移参数。方法上采用 contrastive divergence 与 Gibbs 采样的变体进行训练，生成模型可模拟多维度、相关、层级结构的高频纵向响应。模拟与真实 EMA 数据表明 HDRBM 在重构精度和可解释性上优于无协变量 RTRBM，并能识别驱动群体动态差异的协变量。对您而言，该文提供了一种纵向高维相关数据的生成式建模思路，可辅助后续 longitudinal causal inference 中的潜在结果生成或敏感性分析，但其本身不涉及 semiparametric efficiency 或 identification 理论。
- **关键技术**: `recurrent temporal restricted Boltzmann machine`, `contrastive divergence`, `heterogeneous group dynamics`, `covariate-modulated hidden units`, `Gibbs sampling`, `ecological momentary assessment`
- **为什么对您有用**: 与您 primary interest 中的 longitudinal causal inference 间接相关——HDRBM 可作为纵向高维相关数据的生成模型，为后续因果推断（如 g-methods / marginal structural models）提供更灵活的潜在数据生成机制参考；同时 EMA 数据集对 epidemiology 方向有实际数据价值。

### 5. [10.1093/biomtc/ujae134](https://doi.org/10.1093/biomtc/ujae134) — An exploratory penalized regression to identify combined effects of temporal variables—application to agri-environmental issues
- **作者**: Bénedicte Fontez, Patrice Loisel, Thierry Simonneau, Nadine Hilgert
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在双时间序列协变量对标量输出的联合效应设定下，目标是识别并估计具有解释性的联合时间区间对响应变量的影响。提出SpiceFP方法，将两个时间变量离散化为联合模态（类别区间），以各区间的观测频率作为回归子构建多重回归模型。利用广义融合Lasso（generalized fused lasso）同时进行区间划分与系数估计，实现系数的稀疏性与相邻区间的结构化平滑。模拟表明该方法能灵活筛选出非零/有影响力的模态，并在葡萄品质的农业环境数据中进行了应用展示。对您而言，其广义融合Lasso在多维频率表上的算法构建思路可作统计计算参考，但缺乏您关注的半参数效率或高维推断理论。
- **关键技术**: `generalized fused lasso`, `temporal variable discretization`, `joint modalities frequency regression`, `penalized regression`, `sparsity and structure`
- **为什么对您有用**: 涉及高维惩罚回归（广义融合Lasso）的算法设计与统计计算，但缺乏您核心关注的高维推断理论（如RMT/debiasing）或半参数效率，仅作计算方法参考。

### 6. [10.1093/biomtc/ujae116](https://doi.org/10.1093/biomtc/ujae116) — Bayesian inference for group-level cortical surface image-on-scalar regression with Gaussian process priors
- **作者**: Andrew S Whiteman, Timothy D Johnson, Jian Kang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在群体水平神经影像的 image-on-scalar 回归设定下，本文旨在估计空间变系数函数并改善传统预处理平滑导致的推断校准问题。方法上，对空间变系数施加高斯过程先验以诱导正则化，并结合非平稳误差过程实现数据自适应平滑。针对高分辨率影像带来的计算瓶颈，引入 Vecchia 型近似对先验进行近似，该近似保留全空间秩且适用于广泛的空间相关函数类，显著提升了计算可行性。模拟与 ABCD 研究 fMRI 数据分析表明，该方法比标准顶点分析具有更好的校准和功效。对您可能有用：Vecchia 近似作为处理大规模空间相关数据的数值方法，属于您关注的 statistical computing 领域，可为高维/大规模矩阵计算提供算法借鉴。
- **关键技术**: `Gaussian process priors`, `Vecchia approximation`, `image-on-scalar regression`, `non-stationary error process`, `spatial regularization`
- **为什么对您有用**: 虽然应用场景为神经影像，但其核心的 Vecchia 近似计算方法属于您关注的 statistical computing 领域，可为处理大规模空间/矩阵数据的数值算法设计提供可迁移的思路。

### 7. [10.1093/biomtc/ujae151](https://doi.org/10.1093/biomtc/ujae151) — Graphical model inference with external network data
- **作者**: Jack Jewson, Li Li, Laura Battaglia, Stephen Hansen, David Rossell, Piotr Zwiernik
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维图模型设定下（样本量相对参数量受限），研究如何利用变量间的外部网络数据改善参数推断与模型可解释性。提出一种 spike-and-slab 先验框架，将偏相关的边缘存在概率、均值及方差回归到外部网络上，以刻画网络结构对图模型参数的依赖。该方法旨在检测外部网络是否与图模型相关并解释其影响机制，计算上基于 R 及概率编程语言实现了相应算法。在美国 COVID-19 疫情与社交媒体协同演化的应用中，表明引入网络数据可提升统计精度与样本外预测。对您而言，该文虽非半参数或效率理论，但其高维图模型外部信息整合思路及流行病学数据集，对您关注的高维推断与流行病学应用有一定参考价值。
- **关键技术**: `spike-and-slab prior`, `graphical model`, `partial correlation regression`, `probabilistic programming`, `external network data integration`
- **为什么对您有用**: 该文处理高维图模型外部信息整合的计算思路，以及 COVID-19 时空流行病学应用数据集，对您关注的高维统计计算与流行病学应用有参考价值。

## 流行病学  *(epidemiology, 4 篇)*

### 1. [10.1093/biomtc/ujae122](https://doi.org/10.1093/biomtc/ujae122) — Derivation of outcome-dependent dietary patterns for low-income women obtained from survey data using a supervised weighted overfitted latent class analysis
- **作者**: Stephanie M Wu, Matthew R Williams, Terrance D Savitsky, Briana J K Stephenson
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在复杂抽样调查数据下，本文目标是识别与高血压结局相关的饮食模式，克服信息性抽样导致的选择偏差。作者提出监督加权过拟合潜类分析（SWOLCA），基于贝叶斯伪似然将抽样权重整合到离散数据的暴露-结局模型中。该方法通过MCMC Gibbs采样算法，在潜类模型内调整分层、聚类及信息性抽样，并允许交互项处理效应修饰。模拟研究表明SWOLCA在偏差、精度和覆盖度上优于忽略抽样设计的传统方法。实证部分利用NHANES（2015-2018）数据刻画了美国低收入女性的饮食-高血压关联模式。对您而言，该文提供了NHANES复杂数据集的贝叶斯伪似然加权框架，对在流行病学调查数据中处理信息性抽样和进行因果推断具有参考价值。
- **关键技术**: `Bayesian pseudo-likelihood`, `supervised latent class analysis`, `informative sampling`, `complex survey weighting`, `MCMC Gibbs sampling`
- **为什么对您有用**: 属于流行病学应用，使用经典NHANES复杂数据集；虽然核心是贝叶斯潜类模型而非您主攻的半参数/因果理论，但其处理信息性抽样和调查权重的贝叶斯伪似然方法，对您在流行病学调查数据中开展因果推断或加权估计具有数据集和方法参考价值。

### 2. [10.1093/biomtc/ujae117](https://doi.org/10.1093/biomtc/ujae117) — Case-crossover designs and overdispersion with application to air pollution epidemiology
- **作者**: Samuel Perreault, Gracia Y Dong, Alex Stringer, Hwashin Shin, Patrick E Brown
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在空气污染流行病学的 case-crossover 设计下，传统条件逻辑模型假设个体独立，无法处理过度分散。本文放松了个体间独立性假设，在条件逻辑模型中显式引入过度分散，并证明所得的过度分散条件逻辑模型与过度分散条件泊松模型在似然上完全等价。作者进一步给出了该模型的贝叶斯计算实现，大规模模拟表明标准模型会严重低估覆盖率，而所提模型则不会。多伦多空气污染与发病率的实证分析显示，新模型对公共假期等异常值更具鲁棒性。对您有用：若您关注流行病学时间序列的因果推断应用，此文提供了 case-crossover 设计下处理过度分散的似然等价转换与贝叶斯计算方案。
- **关键技术**: `case-crossover design`, `conditional logistic model`, `overdispersion`, `conditional Poisson model`, `Bayesian implementation`
- **为什么对您有用**: 连接到您的流行病学应用与因果推断兴趣，提供了 case-crossover 设计（流行病学常用因果推断设计）下处理过度分散的似然等价理论与贝叶斯计算方案，对空气污染时间序列因果效应估计有直接参考价值。

### 3. [10.1093/biomtc/ujae120](https://doi.org/10.1093/biomtc/ujae120) — Likelihood adaptively incorporated external aggregate information with uncertainty for survival data
- **作者**: Ziqi Chen, Yu Shen, Jing Qin, Jing Ning
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在生存数据设定下，研究如何将外部癌症登记库的聚合生存信息（如生存率统计量）与主队列数据整合，以提升治疗效果评估与生存预测的精度。核心挑战在于：罕见癌种的外部聚合统计量本身样本量有限，其变异不可忽略，传统忽略外部不确定性的整合方法会导致过度自信的推断。作者提出 externally informed likelihood 方法，在似然框架中将聚合统计量的抽样变异显式纳入，实现主队列与外部数据的自适应链接。理论上建立了估计量的渐近性质（一致性、渐近正态性），模拟显示有限样本下覆盖率与效率均优于忽略外部不确定性的方法。实证部分将 MD Anderson 炎性乳腺癌队列与 NCDB 聚合数据整合，评估三模态治疗在不同亚型上的生存效应。对您有用之处：该文在似然框架下处理外部数据不确定性的思路可迁移至因果推断中多源数据整合（如 IV/proximal CI 中借用外部 negative control 统计量），且流行病学队列数据集与分析流程具有参考价值。
- **关键技术**: `externally informed likelihood`, `aggregate data integration`, `survival analysis`, `asymptotic normality`, `uncertainty propagation`, `empirical likelihood-type calibration`
- **为什么对您有用**: 直接对应流行病学（secondary interest）中的真实数据应用，且似然框架下显式处理外部聚合统计量不确定性的思路可迁移至因果推断中多源数据整合场景（如 proximal CI 借用外部 negative control 信息），方法学思路有借鉴价值。

### 4. [10.1093/biomtc/ujae147](https://doi.org/10.1093/biomtc/ujae147) — A likelihood approach to incorporating self-report data in HIV recency classification
- **作者**: Wenlong Yang, Danping Liu, Le Bao, Runze Li
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `application`
- **摘要**: 在 HIV 近期感染分类问题中，目标是在自我报告检测史和生物标志物可用的设定下估计感染状态，其中感染状态因自我报告信息而部分可观测。本文提出一种基于似然的概率模型，将已知感染状态的个体与状态未知个体结合，联合建模生物标志物对感染状态的影响，以及感染状态与最近检测时间对检测结果的影响。在马拉维 PHIA 数据和模拟中，相比逻辑回归和二叉树，该模型参数估计更有效且偏差更小，对报告误差和模型误设具有一定鲁棒性。对您有用：此为流行病学应用，其处理部分可观测结果的似然建模思路可迁移至流行病学队列研究中的测量误差或潜在类别分析。
- **关键技术**: `likelihood-based probabilistic model`, `partially observed outcome`, `latent class modeling`, `measurement error robustness`, `bio-behavioral survey data`
- **为什么对您有用**: 属于流行病学（secondary interest）应用，提供了 PHIA 真实数据集和部分可观测变量的似然建模框架，对处理流行病学队列研究中的测量误差与缺失数据有参考价值。

## 其他  *(other, 7 篇)*

### 1. [10.1093/biomtc/ujae144](https://doi.org/10.1093/biomtc/ujae144) — Robust and flexible learning of a high-dimensional classification rule using auxiliary outcomes
- **作者**: Muxuan Liang, Jaeyoung Park, Qing Lu, Xiang Zhong
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 6/10
- **摘要**: ```json
{
  "topic": "high_dim_rmt",
  "summary_zh": "在高维线性分类设定下，目标是利用目标结局与辅助结局联合估计分类规则；传统多任务学习(MTL)在模型误设时会对目标结局引入偏差。作者将估计偏差分解为"子空间内"(within-subspace)与"逆子空间"(against-subspace)两类，提出两步法：先以MTL利用所有结局提升效率，再以仅含目标结局的校准步同时修正两类偏差。理论上证明最终估计量的估计误差严格低于仅用目标结局的single-task估计量，且偏差分解框架给出了MTL误设下偏差来源的精确刻画。模拟与真实数据分析验证了方法优势。对您有用：高维设定下"先借信息再校准偏差"的两步机制与debiased ML的orthogonal score思路相通，偏差分解框架可迁移至因果推断中利用辅助变量(如negative control)提升效率同时保证鲁棒性的问题。",
  "key_techniques": [
    "multi-task learning bias decomposition",
    "within-subspace and against-subspace bias",
    "high-dimensional linear classification",
    "two-step

### 2. [10.1093/biomtc/ujae105](https://doi.org/10.1093/biomtc/ujae105) — ROMI: a randomized two-stage basket trial design to optimize doses for multiple indications
- **作者**: Shuqi Wang, Peter F Thall, Kentaro Takeda, Ying Yuan
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文提出一种用于多适应症剂量优化的两阶段随机篮式试验设计（ROMI），目标是在允许不同适应症最优生物学剂量（OBD）异质性的前提下跨组借用信息。第一阶段评估高剂量并剔除不安全或无效的适应症；第二阶段对保留的适应症在高低剂量间进行随机分配。方法采用潜在聚类贝叶斯分层模型跨适应症借用信息，结合适应症特异性效用函数量化响应-毒性权衡，并以最高后验均值效用选择最优剂量。模拟显示该设计在操作特性上优于忽略适应症差异或独立优化的设计。对您而言，该文属于临床试验自适应设计，与您关注的半参数/效率理论或因果推断关联较弱，但其中处理异质性的贝叶斯借用信息机制可作一般参考。
- **关键技术**: `basket trial design`, `Bayesian hierarchical model`, `latent cluster model`, `posterior mean utility`, `dose optimization`
- **为什么对您有用**: 该文属于临床试验自适应设计，与您核心关注的半参数效率、高维RMT或因果推断理论关联较弱，但其中处理异质性的贝叶斯借用信息机制在多源数据建模时有一般性参考价值。

### 3. [10.1093/biomtc/ujae118](https://doi.org/10.1093/biomtc/ujae118) — Leveraging information from secondary endpoints to enhance dynamic borrowing across subpopulations
- **作者**: Jack M Wolf, David M Vock, Xianghua Luo, Dorothy K Hatsukami, F Joseph McClernon, Joseph S Koopmeiners
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10
- **摘要**: ```json
{
  "topic": "other",
  "summary_zh": "在随机试验的多个亚群（如 basket trial）设定下，目标是借跨亚群信息提高亚群处理效应（subpopulation treatment effect）的估计精度。作者提出扩展 multisource exchangeability model（MEM），将次要终点（secondary endpoints）纳入亚群可交换性（exchangeability）的判断，从而更智能地决定借强度量。模拟显示：当亚群处理效应同质时，新方法通过增强借力降低 MSE；当亚群异质时，因次要终点提供更准确的不可交换信号而减小偏倚幅度。在极低尼古丁香烟戒烟试验数据上，有效样本量相比标准 MEM 提升 2–4 倍。该方法属于贝叶斯动态借力框架，与您关注的 semiparametric efficiency / debiased ML 路线不同，但"利用辅助变量提升主终点精度"的思路与 proximal CI 中 negative control 辅助信息的思想有概念呼应。",
  "key_techniques": [
    "multisource exchangeability model",
    "dynamic borrowing",
    "Bayesian model averaging

### 4. [10.1093/biomtc/ujae124](https://doi.org/10.1093/biomtc/ujae124) — Clustering computer mouse tracking data with informed hierarchical shrinkage partition priors
- **作者**: Ziyi Song, Weining Shen, Marina Vannucci, Alexandria Baldizon, Paul M Cinciripini, Francesco Versace et al.
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在贝叶斯框架下提出层次收缩划分（HSP）先验，用于对鼠标轨迹汇总统计量进行聚类，以识别具有相似神经行为反应的总体子群。HSP模型将受试者簇定义为在实验条件下产生相似（而非完全相同）嵌套划分的集合，允许组内嵌套划分存在偏差，并可在划分中融入先验信息。这区别于要求条件嵌套划分完全相同的传统双聚类方法，也不同于基于采样模型公共参数定义簇的现有嵌套聚类。实证与模拟结果表明该框架能有效揭示不同受试者组的行为模式。该文属于贝叶斯层次模型与认知神经科学的应用交叉，与您关注的因果推断、半参数效率或高维推断等核心方向关联较弱。
- **关键技术**: `hierarchical shrinkage partition prior`, `Bayesian nested clustering`, `bi-clustering deviation`, `mouse-tracking trajectories`
- **为什么对您有用**: 本文属于贝叶斯聚类与认知神经科学的应用交叉，与您关注的因果推断、半参数理论或高维统计等核心方向关联较弱，仅作了解特定数据结构（轨迹汇总统计）的参考。

### 5. [10.1093/biomtc/ujae137](https://doi.org/10.1093/biomtc/ujae137) — Cumulative link mixed-effects models in the service of remote sensing crop progress monitoring
- **作者**: Ioannis Oikonomidis, Samis Trevezas
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文在遥感作物进度监测场景下提出累积链接模型（CLM）方法，estimand 为作物发育阶段的有序类别概率及关键农学参数，假设年度间存在随机效应以刻画季节间变异。方法上构建了固定效应与混合效应两种 CLM，推断基于偏似然，并对比了基于多项分布的标准 CLM 与基于乘积二项分布的新变体。模型利用日历时间、热时间和归一化植被指数作为预测变量，在 Nebraska 八种作物 20 年数据上验证了广泛适用性。配套开发了 R 包生态系统 Ages of Man 以保证可复现性。该方法学 novelty 有限——累积链接混合模型与偏似然推断均为成熟工具，主要贡献在应用层面；对您而言，若关注有序类别数据的半参数建模或混合效应推断的计算实现，R 包可作为参考，但与核心研究方向（causal inference / efficiency theory / RMT）关联较弱。
- **关键技术**: `cumulative link model`, `mixed-effects ordinal regression`, `partial likelihood`, `product binomial distribution`, `proportional odds assumption`
- **为什么对您有用**: 与您的主要研究方向（causal inference、efficiency theory、RMT）关联较弱；累积链接模型属有序数据的半参数建模范畴，但本文未推进效率理论或识别理论，仅提供应用与软件实现，收益有限。

### 6. [10.1093/biomtc/ujae127](https://doi.org/10.1093/biomtc/ujae127) — Wasserstein regression with empirical measures and density estimation for sparse data
- **作者**: Yidong Zhou, Hans-Georg Müller
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10
- **摘要**: {
  "topic": "nonparam_semipara",
  "summary_zh": "在分布回归（distribution-response regression）设定下，目标是将一元分布作为响应变量与协变量建模，传统方法需先对每个个体分布做密度估计再回归，但当某些分布仅有稀疏观测时个体密度估计不可一致。本文提出基于经验测度（empirical measures）的 Wasserstein 回归方法，跳过个体密度恢复的预处理步骤，直接在 Wasserstein 空间中对经验分布做 Fréchet 回归。核心机制是利用全体分布样本的协变量信息跨个体借力（borrow strength），使得即使某分布仅有极少观测点也能获得一致估计，同时规避了带宽选择与密度估计偏差问题。理论上证明了在样本量异质（部分稀疏、部分稠密）情形下估计的一致性，模拟与 ECHO 环境儿童健康数据表明优于现有方法。对您有用：该工作在非参数分布回归中放松了对每个个体需充足观测的假设，其"跨个体借力"思路与 semiparametric efficiency 中跨方程借力的思想相通，且稀疏分布回归在流行病学队列数据中有直接应用价值。",
  "key_techniques": [
    "Wasserstein regression",
    "empirical measures",
    "

### 7. [10.1093/biomtc/ujae149](https://doi.org/10.1093/biomtc/ujae149) — An efficient joint model for high dimensional longitudinal and survival data via generic association features
- **作者**: Van Tuan Nguyen, Adeline Fermanian, Antoine Barbieri, Sarah Zohar, Anne-Sophie Jannot, Simon Bussy et al.
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 0/10
- **摘要**: {
  "topic": "stat_computing",
  "summary_zh": "在高维纵向与生存数据联合建模设定下，目标是同时进行预后预测与显著特征选择。本文提出 FLASH 方法，融合共享随机效应与联合潜在类别模型的思想，通过正则化技术在高维下自动识别显著的纵向与时间独立特征。估计方法基于 EM 算法，并提供了计算高效的实现。模拟与公开医疗数据集的实证表明，该方法在"实时"预测的 C-index 上显著优于现有联合模型，且计算速度提升数个数量级，同时具备可解释性。对您在统计计算（EM 算法的高效实现与优化）方面的兴趣有直接参考价值，其公开医疗数据集也可作为流行病学应用研究的测试平台。",
  "key_techniques": [
    "joint modeling",
    "EM algorithm",
    "shared random effects",
    "latent class model",
    "high-dimensional regularization",
    "C-index"
  ],
  "why_relevant": "论文的核心贡献在于高维联合模型的 EM 算法高效实现，直接契合您在统计计算与数值方法上的兴趣；此外，公开医疗数据集对您在流行病学应用与因果推断方向具有数据集价值。",
  "novelty_fl


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

