# Biometrics — Vol 80  Issue 4  ·  2026-07-03

- 共 52 篇 · Biometrics
- 目录核对 ⚠️ 疑似漏 2 篇（对照 OpenAlex 55 篇）：10.1093/biomtc/ujae126、10.1093/biomtc/ujae133

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Biometrics》第80卷第4期共收录52篇论文，主题分布广泛，但可归纳为几条主线。最突出的是**因果推断**，占据约三分之一篇幅，涵盖从经典平均处理效应（ATE）估计到复杂试验设计、敏感性分析、中介分析、生存因果推断等多个子方向。其次是**假设检验与高维推断**，包括FDR控制、稳健检验、变量筛选等。此外，**半参数/非参数方法**、**贝叶斯建模**、**临床试验设计**、**流行病学应用**以及**高维降维与图模型**也有集中出现。整体上，本期在因果推断领域呈现“方法工具化”趋势：大量工作聚焦于将因果框架与具体数据挑战（如测量误差、缺失数据、高维混杂、复发事件、访视时间不规则）结合，并给出可操作的估计量与推断程序。

在因果推断主线中，**未测量混杂与敏感性分析**是反复出现的主题。多篇论文从不同角度处理这一核心难题：`Semiparametric sensitivity analysis: unmeasured confounding in observational studies` 将Robins等人的敏感性分析推广到半参数设定，推导了非参数有效影响函数并构造一步估计量；`Sensitivity analysis for studies transporting prediction models` 针对预测模型外推问题，提出指数倾斜敏感性分析模型，刻画可忽略性假设的违背程度；`Semi-parametric sensitivity analysis for trials with irregular and informative assessment times` 则在访视时间信息性场景下，通过指数倾斜引入敏感性参数，构建增广逆强度加权估计量。这三篇论文共享“半参数框架+敏感性参数”的技术路线，但分别应用于观察性研究、预测模型外推和试验访视机制，体现了敏感性分析方法的横向扩展。

另一条因果推断子主线是**高维/复杂数据下的因果估计**。`Causal effect estimation in survival analysis with high dimensional confounders` 将因子模型与充分降维结合，把高维协变量压缩为两个低维得分，再构造双重稳健的核估计量，用于生存数据中的RMST效应估计。`Debiased high-dimensional regression calibration for errors-in-variables log-contrast models` 处理高维组成型协变量的测量误差问题，将测量误差视为内生性，通过校准步骤实现渐近正态推断，其思路可迁移至proximal causal inference。`A Bayesian framework for causal analysis of recurrent events with timing misalignment` 则针对复发事件中治疗分配与资格时间点的错位，通过g-computation和联合半参数贝叶斯模型估计因果效应。这三篇论文分别应对高维混杂、测量误差和时序错位，共同展示了因果推断在高维和复杂纵向数据中的方法学进展。

此外，**序贯多阶段试验（SMART）与动态治疗策略**在本期也有集中讨论。`A generalized logrank-type test for comparison of treatment regimes in sequential multiple assignment randomized trials` 提出广义对数秩检验，用于比较SMART中嵌入的治疗策略的生存分布；`Adaptive randomization methods for sequential multiple assignment randomized trials (smarts) via thompson sampling` 首次将Thompson Sampling引入SMART自适应随机化，并处理由此导致的非标准渐近行为；`Optimal adaptive SMART designs with binary outcomes` 则通过约束优化框架，在固定渐近方差下最小化期望治疗失败数。这三篇论文从检验、随机化和优化三个角度推进了SMART设计的方法学。

对于因果推断方向的研究者，建议优先关注以下论文：`Semiparametric sensitivity analysis: unmeasured confounding in observational studies`（半参数效率与敏感性分析）、`Causal effect estimation in survival analysis with high dimensional confounders`（高维降维与生存因果推断）、`Debiased high-dimensional regression calibration for errors-in-variables log-contrast models`（高维测量误差与校准）、以及`A Bayesian framework for causal analysis of recurrent events with timing misalignment`（复发事件与时序错位）。对于半参数效率理论感兴趣的读者，`Semiparametric sensitivity analysis` 和 `How to achieve model-robust inference in stepped wedge trials with model-based methods?` 提供了影响函数和模型稳健推断的典型范例。高维方向则可关注 `Joint mirror procedure: controlling false discovery rate for identifying simultaneous signals`（FDR控制）和 `Robust and flexible learning of a high-dimensional classification rule using auxiliary outcomes`（迁移学习与偏差分解）。

## 因果推断  *(causal_inference, 20 篇)*

### 1. [10.1093/biomtc/ujae095](https://doi.org/10.1093/biomtc/ujae095) — A causal inference framework for leveraging external controls in hybrid trials
- **作者**: Michael Valancius, Herbert Pang, Jiawen Zhu, Stephen R Cole, Michele Jonsson Funk, Michael R Kosorok
- **期刊/来源**: Biometrics
- **机构**: University of North Carolina at Chapel Hill
- **分类**: vol 80 · issue 4
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在混合试验（hybrid trial）框架下，将随机试验的内部数据与外部历史对照数据结合，以提升平均处理效应（ATE）的估计效率。研究动机来自SUNFISH试验（risdiplam对脊髓性肌萎缩症患者运动功能的影响），原始分析仅使用试验内部数据，本文探索加入历史试验安慰剂组作为外部对照。作者将问题形式化为因果推断框架，指出此类设计缺乏完全随机化，对模型假设依赖更强。文章给出了内部与外部对照可交换性的充分因果假设以识别ATE，并与新的图准则建立联系。提出了估计量，回顾了效率界，并发展了在未知 nuisance 模型用灵活机器学习估计时的有效双稳健估计方法，同时建议了模型诊断手段。模拟和SUNFISH实例表明，外部对照可提升处理效应估计的效率。对您而言，本文是因果推断中利用外部数据（如历史对照、真实世界证据）提升效率的典型应用，与您的primary interest（因果推断中的identification与estimation）直接相关，且涉及双稳健估计与效率界等您熟悉的工具。
- **关键技术**: `doubly robust estimation`, `efficient influence function`, `cross-fitting`, `exchangeability assumptions`, `graphical criteria for external validity`, `machine learning nuisance estimation`
- **为什么对您有用**: 直接连接到primary interest中的因果推断（identification与estimation），特别是利用外部数据（历史对照）提升效率的设定。武器库中very_familiar的'nonparametric statistics'和'estimation theory in causal inference'可直接用于理解其双稳健估计与效率界推导；moderately_familiar的'identification theory in causal inference'可用于审视其交换性假设的充分性。中期可做：若想进一步拓展其图准则或效率界，需在moderately_familiar的'semiparametric theory'上加强。

### 2. [10.1093/biomtc/ujae153](https://doi.org/10.1093/biomtc/ujae153) — Debiased high-dimensional regression calibration for errors-in-variables log-contrast models
- **作者**: Huali Zhao, Tianying Wang
- **期刊/来源**: Biometrics
- **机构**: Tsinghua University · Colorado State University
- **分类**: vol 80 · issue 4
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对高维组成型协变量（如微生物组数据）存在测量误差的问题，首次在log-contrast线性模型下进行统计推断。提出了一种校准方法，在参数稀疏性条件相对宽松下，建立了估计量的渐近正态性，从而支持假设检验和置信区间构造。方法核心是将测量误差视为一种特殊的endogeneity，通过校准步骤修正偏差，类似于instrumental variable或measurement error模型中的纠偏思路。数值实验和微生物组数据应用表明，该方法能有效降低偏差并达到名义覆盖概率。该工作对您可能有用：它连接了高维统计推断与因果推断中的测量误差问题，且其校准思路可迁移至proximal causal inference中的negative control设定。
- **关键技术**: `high-dimensional calibration`, `log-contrast model`, `measurement error`, `debiased estimation`, `asymptotic normality`, `compositional data`
- **为什么对您有用**: 本文直接连接您在高维统计和因果推断中的测量误差兴趣——其校准方法可视为一种特殊的instrumental variable纠偏策略，与proximal CI中的negative control设定有技术共鸣。武器库中'high-dimensional asymptotics'和'estimation theory in causal inference'可直接用于分析其估计量的finite-sample性质，属于**立即可做**的follow-up：例如用您熟悉的minimax bound验证其稀疏性条件是否紧，或将其校准框架推广至更一般的endogenous compositional covariates设定。

### 3. [10.1093/biomtc/ujae106](https://doi.org/10.1093/biomtc/ujae106) · [arXiv](https://arxiv.org/abs/2104.08300) — Semiparametric sensitivity analysis: unmeasured confounding in observational studies
- **作者**: Razieh Nabi, Matteo Bonvini, Edward H Kennedy, Ming-Yueh Huang, Marcela Smid, Daniel O Scharfstein
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在观察性研究中针对未测量混杂的敏感性分析框架下，以平均因果效应（ACE）为估计目标。作者将Robins等人、Franks等人以及Zhou和Yao发展的敏感性分析方法推广到半参数设定。利用半参数理论推导了在固定敏感性参数下ACE的非参数有效影响函数（EIF）。基于该影响函数构造了一个一步估计量（one-step estimator），并采用样本分割（split sample）和截断（truncation）技术。估计量依赖于观测数据分布的半参数模型，但这些模型不对敏感性参数的值施加任何限制。作者建立了保证估计量具有√n渐近性的充分条件。通过孕期吸烟对出生体重影响的真实数据以及模拟研究评估了方法性能。该工作直接连接您对因果推断中敏感性分析和半参数效率理论的兴趣，且其EIF推导和one-step构造思路可迁移至proximal CI框架下的敏感性分析。
- **关键技术**: `semiparametric efficiency theory`, `efficient influence function`, `one-step estimation`, `sample splitting`, `sensitivity analysis`, `unmeasured confounding`
- **为什么对您有用**: 直接命中primary interest中的causal inference（敏感性分析）和efficiency theory（EIF推导）。您可以用very_familiar的nonparametric statistics和estimation theory in causal inference工具，检验其EIF推导在proximal CI设定下是否仍成立，或将其one-step构造推广到更复杂的纵向结构。中期可做：若想将方法扩展到高维协变量，需先在moderately_familiar的semiparametric theory上补足高维EIF的收敛性分析。

### 4. [10.1093/biomtc/ujae145](https://doi.org/10.1093/biomtc/ujae145) — A Bayesian framework for causal analysis of recurrent events with timing misalignment
- **作者**: Arman Oganisian, Anthony Girard, Jon A Steingrimsson, Patience Moyo
- **期刊/来源**: Biometrics
- **机构**: Brown University · University of Pennsylvania
- **分类**: vol 80 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对观察性研究中复发事件（如住院次数）的因果效应估计，提出一个贝叶斯框架，核心挑战是治疗分配与目标人群资格时间点之间的错位（timing misalignment）。作者将错位问题重新表述为时变治疗问题：部分患者在资格时间点已接受治疗，部分未接受但可能在后续某个时间点切换治疗，前提是存活至该时间点。在右删失下，定义了平均因果效应 estimand（如治疗 vs. 对照的复发率差异），并通过 g-computation 程序进行识别和估计。估计采用联合半参数贝叶斯模型，同时建模死亡（终止事件）和复发事件过程，利用 Medicare 保险索赔数据比较不同阿片类药物治疗患者的住院率。该方法直接处理了实际流行病学数据中常见的治疗时间错位和竞争风险，对您从事的纵向因果推断和流行病学应用有直接参考价值。
- **关键技术**: `g-computation`, `semiparametric Bayesian model`, `time-varying treatment`, `recurrent events`, `competing risks`
- **为什么对您有用**: 本文直接关联您的 primary interest 中纵向因果推断（longitudinal causal inference）和流行病学应用（epidemiology）。其核心贡献——将治疗时间错位建模为时变治疗问题——是您 moderately_familiar 的 identification theory 中一个具体且实用的扩展。中期可做：您可尝试用 HOIF 或 semiparametric theory 为该 estimand 推导一个双稳健估计量，替代本文的贝叶斯 g-computation，这需要先在 moderately_familiar 的 semiparametric theory 上加强。

### 5. [10.1093/biomtc/ujae129](https://doi.org/10.1093/biomtc/ujae129) — Sensitivity analysis for studies transporting prediction models
- **作者**: Jon A Steingrimsson, Sarah E Robertson, Sarah Voter, Issa J Dahabreh
- **期刊/来源**: Biometrics
- **机构**: Brown University · Harvard University
- **分类**: vol 80 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究预测模型在目标人群中的性能度量估计问题，设定为源人群有协变量和结局数据，而目标人群仅有协变量数据。在可忽略性假设（结局与人群条件独立于协变量）下，模型性能可识别，但该假设不可检验且常存争议。作者提出指数倾斜敏感性分析模型，通过倾斜参数刻画假设违背程度，并推导目标人群风险（如预测误差）的识别结果。估计方法采用基于逆概率加权或回归的估计量，并建立其大样本性质（相合性与渐近正态性）。实证部分应用于肺癌筛查数据，展示不同倾斜参数下模型性能的变化。该工作为预测模型外推的敏感性分析提供了系统框架，对您关注的因果推断中transportability问题的敏感性分析有直接参考价值。
- **关键技术**: `exponential tilt model`, `sensitivity analysis`, `transportability`, `inverse probability weighting`, `large-sample theory`
- **为什么对您有用**: 直接连接您primary interest中的因果推断transportability子方向，特别是预测模型外推的敏感性分析。您武器库中very_familiar的estimation theory in causal inference（如IPW、回归估计）可直接用于复现或扩展其估计量的大样本性质。中期可做：若想将倾斜模型与proximal causal inference中的negative control结合，需先熟悉moderately_familiar的identification theory in causal inference。

### 6. [10.1093/biomtc/ujae139](https://doi.org/10.1093/biomtc/ujae139) — A generalized logrank-type test for comparison of treatment regimes in sequential multiple assignment randomized trials
- **作者**: Anastasios A Tsiatis, Marie Davidian
- **期刊/来源**: Biometrics
- **机构**: North Carolina State University
- **分类**: vol 80 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对序贯多分配随机试验（SMART）中多阶段治疗策略的比较问题，提出了一类广义对数秩检验。目标是比较不同嵌入治疗策略下时间至事件结局的生存分布。方法框架允许任意阶段数的SMART设计，并可纳入协变量信息以提高效率，同时适用于观察性研究数据。核心机制是构建一个基于逆概率加权和协变量调整的检验统计量，其渐近分布为卡方分布。作者明确了所需识别假设（如无未测量混杂、一致性），并证明所提检验优于或包含现有方法。模拟研究和急性早幼粒细胞白血病SMART数据应用验证了方法的有限样本性能。对您而言，本文是因果推断中纵向/序贯治疗策略比较的经典应用，其逆概率加权和协变量调整思路可迁移至您熟悉的proximal CI或IV设定下的敏感性分析。
- **关键技术**: `inverse probability weighting`, `logrank-type test`, `sequential multiple assignment randomized trial (SMART)`, `covariate adjustment for efficiency`, `embedded treatment regimes`
- **为什么对您有用**: 本文直接连接您的primary interest中的纵向因果推断（longitudinal causal inference）和mediation方向，具体是序贯治疗策略的生存结局比较。武器库中'very_familiar'的estimation theory in causal inference和inverse problems with random noise可直接用于理解其逆概率加权估计量的渐近性质；'moderately_familiar'的identification theory in causal inference可用于审视其假设（如序贯可忽略性）是否可放松。**立即可做**：用您熟悉的非参数统计和minimax bound工具，可分析该检验在弱识别或高维协变量下的效率损失。

### 7. [10.1093/biomtc/ujae110](https://doi.org/10.1093/biomtc/ujae110) — Causal effect estimation in survival analysis with high dimensional confounders
- **作者**: Fei Jiang, Ge Zhao, Rosa Rodriguez-Monguio, Yanyuan Ma
- **期刊/来源**: Biometrics
- **机构**: University of California, San Francisco · Portland State University · Pennsylvania State University
- **分类**: vol 80 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对生存数据中高维混杂（协变量数超过样本量）下的因果效应估计问题，目标 estimand 为限制平均生存时间（RMST）的处理组间差异。方法上，作者将因子模型与充分降维（SDR）结合，分别构造倾向性评分和预后评分，从而将高维协变量压缩为两个低维得分。基于这两个得分，构建了一个核函数形式的双重稳健（doubly robust）估计量，并证明了其与匹配估计的联系。理论部分建立了该估计量的相合性和渐近正态性，并给出了 valid inference 所需的方差估计。数值实验和弥漫大B细胞淋巴瘤数据集的应用展示了方法在有限样本下的表现。对您而言，该工作将高维降维与生存因果推断结合，其因子模型+SDR的降维策略可能迁移至您关注的 proximal CI 或 IV 设定中的高维混杂控制问题。
- **关键技术**: `factor model`, `sufficient dimension reduction`, `propensity score`, `prognostic score`, `doubly robust estimation`, `kernel-based matching`
- **为什么对您有用**: 直接连接 primary interest 中的因果推断（高维混杂下的生存分析）和 high-dimensional statistics。技术层面，可用您 very_familiar 的 minimax bounds 工具检验其因子模型+SDR 降维在更一般设定下的最优收敛速率，或评估其双重稳健估计量在弱混杂下的效率损失。中期可做：若想将类似思路推广至 proximal CI 的 negative control 设定，需先在 moderately_familiar 的 identification theory 上补足高维下桥函数的收敛理论。

### 8. [10.1093/biomtc/ujae143](https://doi.org/10.1093/biomtc/ujae143) — A Bayesian joint model for mediation analysis with matrix-valued mediators
- **作者**: Zijin Liu, Zhihui (Amy) Liu, Ali Hosni, John Kim, Bei Jiang, Olli Saarela
- **期刊/来源**: Biometrics
- **机构**: University Health Network · 3M (United States) · University of Toronto · Princess Margaret Cancer Centre · University of Alberta
- **分类**: vol 80 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对放疗中处方剂量对治疗中断的影响，提出一种以矩阵值剂量-体积直方图（DVH）为中介变量的贝叶斯联合中介分析模型。目标是将高维矩阵结构的中介变量纳入因果分解框架，估计自然直接效应和间接效应。方法核心是概率多线性主成分分析（MPCA）的贝叶斯改编，从矩阵值数据中提取潜在特征，同时保留其行列结构；再通过吉布斯采样联合估计所有参数，并用Varimax旋转识别活跃的中介指标。与两步法相比，联合模型在估计因果分解效应时效率更高，且能将中介效应以矩阵形式可视化。模拟和实际数据均验证了方法的有效性。该工作对您有价值：它拓展了中介分析中高维中介变量的数据类型（从向量到矩阵），与您对因果推断（特别是纵向/中介分析）和贝叶斯计算的兴趣直接相关。
- **关键技术**: `Bayesian joint mediation model`, `probabilistic multilinear principal components analysis (MPCA)`, `Gibbs sampling`, `Varimax rotation`, `causal decomposition effects`
- **为什么对您有用**: 本文直接连接您对因果推断中中介分析的兴趣，特别是处理高维结构化的中介变量（矩阵值DVH），这是传统向量中介方法无法覆盖的。从技术武器库看，您对贝叶斯计算和因果推断的估计理论非常熟悉，可以立即评估其MPCA先验设定对因果识别的影响，以及吉布斯采样在高维矩阵分解下的收敛性。中期可做：若想将此类矩阵中介模型与您熟悉的HOIF或debiased ML结合，需先在semiparametric theory上补足矩阵值中介的influence function推导（当前武器库中moderately_familiar项）。

### 9. [10.1093/biomtc/ujae154](https://doi.org/10.1093/biomtc/ujae154) — Semi-parametric sensitivity analysis for trials with irregular and informative assessment times
- **作者**: Bonnie B Smith, Yujing Gao, Shu Yang, Ravi Varadhan, Andrea J Apter, Daniel O Scharfstein
- **期刊/来源**: Biometrics
- **机构**: Johns Hopkins University · North Carolina State University · University of Pennsylvania · University of Utah
- **分类**: vol 80 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对随机对照试验中访视时间不规则且与结局相关（informative assessment times）的问题，提出一种半参数敏感性分析方法。目标是在无法验证的“可解释访视”（EA）假设下，估计处理效应。EA假设认为，给定历史协变量后，访视时间与结局条件独立。方法通过指数倾斜（exponential tilting）引入一个敏感性参数，刻画偏离EA假设的程度。估计采用基于影响函数的增广逆强度加权估计量（augmented inverse intensity-weighted estimator），允许对观测数据灵活建模（如半参数模型），且敏感性参数的设定与数据建模分离。在低收入哮喘患者的随机试验中展示了具体实施步骤。该方法对您有用：它直接连接您对因果推断中敏感性分析的兴趣，且其基于影响函数的估计框架与您的效率理论（semiparametric efficiency bounds）和debiased ML工具高度相关。
- **关键技术**: `influence function`, `augmented inverse intensity-weighted estimator`, `exponential tilting`, `semiparametric modeling`, `sensitivity analysis`
- **为什么对您有用**: 本文直接连接您对因果推断中敏感性分析的兴趣，特别是处理纵向数据中不规则访视时间这一实际挑战。其基于影响函数的估计框架与您的效率理论（semiparametric efficiency bounds）和debiased ML工具高度相关，您可以用very_familiar的估计理论（如非参统计、逆问题）来理解并可能改进该估计量的有限样本性质。中期可做：若想将方法推广到更复杂的识别设定（如proximal CI），需先在moderately_familiar的识别理论上长肌肉。

### 10. [10.1093/biomtc/ujae135](https://doi.org/10.1093/biomtc/ujae135) · [arXiv](https://arxiv.org/abs/2304.05583) — Estimating marginal treatment effect in cluster randomized trials with multi-level missing outcomes
- **作者**: Chia-Rui Chang, Rui Wang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对整群随机试验（CRT）中多层级缺失结局数据下的边际处理效应估计问题。现有方法（如IPW-GEE）仅处理个体层缺失，忽略群层（cluster-level）缺失，当群层缺失与结局相关时会导致偏倚。作者提出基于加权GEE的多层级乘性稳健（multiply robust）估计量，允许缺失发生在个体、子群（subcluster）和群三个层级。核心机制是：在每个层级分别设定倾向性得分模型（如群层缺失概率、子群层缺失概率、个体层缺失概率），估计量在任一层级模型正确设定时即保持相合和渐近正态。理论证明采用M-估计框架和分位数函数方法推导渐近方差。模拟和马达加斯加疟疾干预CRT数据验证了方法在有限样本下的表现。对您有用：该文将缺失数据机制从单层扩展到多层，其乘性稳健思想可迁移至您熟悉的因果推断中纵向或分层数据下的敏感性分析问题。
- **关键技术**: `multiply robust estimation`, `weighted generalized estimating equations`, `multi-level missing data`, `cluster randomized trials`, `propensity score weighting`
- **为什么对您有用**: 直接连接到您primary interest中的因果推断（纵向/分层数据）和估计理论。该文的乘性稳健框架可被您的M-估计理论（moderately_familiar）工具攻破：例如，用您熟悉的非参统计和minimax bound分析其多层级权重估计的收敛速率是否最优。中期可做：需先巩固M-估计理论在复杂缺失机制下的渐近性质，但核心武器（非参、高维渐近）已就绪。

### 11. [10.1093/biomtc/ujae108](https://doi.org/10.1093/biomtc/ujae108) · [arXiv](https://arxiv.org/abs/2409.09440) — Group sequential testing of a treatment effect using a surrogate marker
- **作者**: Layla Parast, Jay Bartroff
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文在利用替代标记物（surrogate marker）进行治疗效应检验的框架下，提出群序贯（group sequential）检验方法，允许在多个时间点提前停止。现有非参数检验仅使用单个时间点的替代标记物信息，且需从先前研究借力；本文将其扩展至替代标记物重复测量的情形。核心贡献在于推导了多个时间点上基于替代标记物的非参数检验统计量的联合分布性质，并据此计算了可提前停止的边界（包括疗效显著性和无效性停止）。方法通过模拟研究和两套真实艾滋病临床试验数据验证。对您而言，本文连接了因果推断中的替代标记物识别与假设检验中的序贯分析，属于您 primary interest 中“hypothesis testing”与“causal inference”的交叉点。
- **关键技术**: `nonparametric test for surrogate marker`, `group sequential stopping boundaries`, `correlated test statistics`, `borrowing information from prior study`
- **为什么对您有用**: 本文直接连接您 primary interest 中的“hypothesis testing”与“causal inference”（替代标记物用于治疗效应检验）。您的 technical arsenal 中“非参数统计”和“因果推断中的估计理论”可直接用于理解其非参数检验构造；若想进一步改进，可尝试用“higher-order U-statistics”的树宽/张量收缩视角分析其多时间点检验统计量的相关性结构（中期可做，需先在 moderately_familiar 的“higher-order U-statistics 理论”上加强）。

### 12. [10.1093/biomtc/ujae132](https://doi.org/10.1093/biomtc/ujae132) — Bayesian pathway analysis over brain network mediators for survival data
- **作者**: Xinyuan Tian, Fan Li, Li Shen, Denise Esserman, Yize Zhao
- **期刊/来源**: Biometrics
- **机构**: Yale University · University of Pennsylvania
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文提出一个贝叶斯框架，用于分析遗传暴露、脑网络中介变量与生存结局之间的因果路径。核心设定是：暴露为遗传因素（如基因型），中介变量为全脑连接网络（对称矩阵），结局为疾病发病时间（生存数据）。方法上，构建了一个结构模型，包含对称矩阵变量加速失效时间模型（用于结局）和对称矩阵响应回归（用于中介变量），并引入图内稀疏性和图间收缩先验以识别信息性网络配置并抑制噪声。该工作将网络型中介分析从连续/二值结局扩展到生存结局，并保留了全脑网络的拓扑结构而非降维为边向量。模拟表明方法优于现有替代方案；应用于ADNI数据获得了神经生物学上合理的发现。对您而言，本文是因果中介分析在复杂高维中介变量（脑网络）上的应用，其贝叶斯建模策略和稀疏化技术对您在高维因果推断中的识别与估计问题有参考价值。
- **关键技术**: `Bayesian mediation analysis`, `symmetric matrix-variate regression`, `accelerated failure time model`, `within-graph sparsity`, `between-graph shrinkage`
- **为什么对您有用**: 本文属于因果推断的中介分析方向，具体处理网络型中介变量（脑连接矩阵）与生存结局，是您 primary interest 中“causal inference (mediation)”的一个应用实例。您的武器库中“estimation theory in causal inference”和“high-dimensional asymptotics”可用于评估其贝叶斯先验选择对估计偏差的影响，但核心建模（矩阵变量回归、贝叶斯稀疏化）与您的 very_familiar 工具（非参、minimax）不完全对齐，属于**中期可做**：需先在 moderately_familiar 的“identification theory in causal inference”上加深对网络中介识别条件的理解。

### 13. [10.1093/biomtc/ujae152](https://doi.org/10.1093/biomtc/ujae152) — Adaptive randomization methods for sequential multiple assignment randomized trials (smarts) via thompson sampling
- **作者**: Peter Norwood, Marie Davidian, Eric Laber
- **期刊/来源**: Biometrics
- **机构**: Quantum Leap Healthcare Collaborative · North Carolina State University · Duke University
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文在序贯多分配随机试验（SMART）框架下，首次提出基于Thompson Sampling（TS）的自适应随机化（RAR）算法，用于多阶段治疗策略的评估。研究聚焦两个常见目标：比较SMART中嵌入的治疗策略，以及估计最优嵌入策略。作者开发了有效的后验推断程序，以应对RAR导致的非标准渐近行为——即使在单阶段设定下，标准ATE估计量在RAR下也可能呈现非正态极限分布。方法核心是将TS的随机化概率与治疗最优的后验概率对齐，并通过重抽样或贝叶斯方法构造置信区间。模拟和基于真实SMART数据的实证表明，TS能在不牺牲后验比较效率的前提下改善试验内受试者结局。对您而言，本文连接了因果推断中的序贯治疗策略（dynamic treatment regimes）与自适应试验设计，其推断程序中的非标准渐近性分析可能用到您熟悉的高维渐近工具。
- **关键技术**: `Thompson Sampling`, `Response-adaptive randomization`, `Sequential multiple assignment randomized trial`, `Dynamic treatment regimes`, `Post-study inference`, `Nonstandard asymptotic behavior`
- **为什么对您有用**: 本文直接连接您的primary interest中的因果推断子方向——序贯治疗策略（dynamic treatment regimes）的识别与估计。技术层面，您可以用very_familiar的minimax bounds和high-dimensional asymptotics工具来评估其推断程序在有限样本下的最优性，或检验其声称的“不牺牲效率”是否在更紧的界下成立。中期可做：若想深入其非标准渐近理论，需先在moderately_familiar的semiparametric theory上长肌肉（如处理RAR下影响函数非线性的问题）。

### 14. [10.1093/biomtc/ujae123](https://doi.org/10.1093/biomtc/ujae123) · [arXiv](https://arxiv.org/abs/2401.15680) — How to achieve model-robust inference in stepped wedge trials with model-based methods?
- **作者**: Bingkai Wang, Xueqi Wang, Fan Li
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `new_theory`
- **摘要**: 本文聚焦于 stepped wedge 设计（阶梯楔形设计）中基于模型的方法（线性混合模型、GEE）在模型误设下的稳健推断问题。目标 estimand 是边际处理效应，通过潜在结果非参数定义，可依赖于日历时间或暴露时间。核心理论结果是：要获得非参数 estimand 的一致估计，通常只需正确指定处理效应结构（如时间-处理交互），而协变量函数形式、随机效应结构、误差分布等其余部分可以误设；方差估计通过 sandwich 估计量获得稳健性。对于非恒等链接函数或比率 estimand，还需额外进行 g-computation 步骤才能实现模型稳健推断。模拟实验和实际数据分析验证了理论结果。对您而言，本文是纵向因果推断中 cluster-randomized trial 的 identification 与稳健估计的典型案例，与您 causal inference 方向中的 longitudinal 设定直接相关。
- **关键技术**: `linear mixed models`, `generalized estimating equations (GEE)`, `sandwich variance estimator`, `g-computation`, `marginal treatment effect estimands`, `model misspecification robustness`
- **为什么对您有用**: 本文直接对应您 primary interest 中的 causal inference 纵向设定（stepped wedge design 是 cluster-randomized trial 的常见变体），且其核心问题——模型误设下 estimand 的 consistency 条件——与您熟悉的 identification theory 和 M-estimation 理论高度相关。您可以用 very_familiar 的 M-estimation 理论（sandwich variance 的 finite-sample 性质）或 moderately_familiar 的 semiparametric theory 来审视其 g-computation 步骤的效率损失。中期可做：若想深入其 sandwich 方差在有限样本下的覆盖概率，需先在 moderately_familiar 的 semiparametric theory 上长肌肉（如 influence function 的 bootstrap 校准）。

### 15. [10.1093/biomtc/ujae118](https://doi.org/10.1093/biomtc/ujae118) — Leveraging information from secondary endpoints to enhance dynamic borrowing across subpopulations
- **作者**: Jack M Wolf, David M Vock, Xianghua Luo, Dorothy K Hatsukami, F Joseph McClernon, Joseph S Koopmeiners
- **期刊/来源**: Biometrics
- **机构**: University of Minnesota · Duke University
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对随机试验中目标总体及子总体处理效应的估计问题，提出一种利用次要终点信息增强子总体间动态借力的多源可交换性模型（MEM）。标准MEM仅依赖主要终点数据来评估子总体间的可交换性，而本文通过引入次要终点，在贝叶斯框架下构建联合模型，更高效地判断哪些子总体可以合并估计。模拟研究表明，与标准MEM相比，所提模型几乎一致地降低了均方误差：当子总体对处理反应相似时，效率提升；当子总体异质时，偏倚幅度减小。方法的核心机制是次要终点提供了关于处理效应异质性的额外信号，从而改进了可交换性先验的校准。实证部分使用一项极低尼古丁香烟试验数据，估计三个优先子总体（如按性别、种族分层）的戒烟效果，结果显示有效样本量提升至标准MEM的2-4倍。该方法对您可能有用：它直接关联您因果推断中纵向/异质性处理效应的估计问题，且其贝叶斯动态借力框架可与您熟悉的非参数统计和M估计理论结合，用于设计更稳健的敏感性分析。
- **关键技术**: `dynamic borrowing`, `multisource exchangeability model (MEM)`, `Bayesian hierarchical model`, `secondary endpoints`, `subpopulation treatment effect estimation`
- **为什么对您有用**: 本文属于因果推断中异质性处理效应估计的应用方向，具体连接您的primary interest中的纵向/子总体分析。技术层面，您可以用very_familiar的minimax bounds工具分析其动态借力策略的估计误差上界，或用moderately_familiar的M估计理论验证其贝叶斯先验的渐近性质。中期可做：若想将次要端点信息纳入您熟悉的debiased ML框架，需先在moderately_familiar的semiparametric theory上提升，以处理联合似然中的高维nuisance参数。

### 16. [10.1093/biomtc/ujae112](https://doi.org/10.1093/biomtc/ujae112) — On network deconvolution for undirected graphs
- **作者**: Zhaotong Lin, Isaac Pan, Wei Pan
- **期刊/来源**: Biometrics
- **机构**: Florida State University · University of Minnesota · Pomona College
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 本文研究网络去卷积（ND）方法在无向图上的理论基础与应用。ND 原本用于有向图，通过将总效应分解为直接效应与间接效应的和，得到直接效应网络的闭式解。作者首先澄清了 ND 隐含的线性模型假设，然后推导出一个简洁结果：在无向图上，ND 等价于使用精度矩阵（precision matrix）来估计直接关联。这一等价性为 ND 在无向图上的应用提供了严格的统计解释和合理性证明。此外，作者还形式化地表征了缩放总效应图对 ND 结果的影响。在实证部分，利用大规模 GWAS 数据，ND 被用于对比身高与冠心病风险之间的边际遗传相关与条件遗传相关，结果与推断的有向因果图一致。本文的核心贡献在于为 ND 在无向图上的应用提供了理论支撑，并展示了其在遗传流行病学中的实用价值。
- **关键技术**: `network deconvolution`, `precision matrix`, `Gaussian graphical model`, `marginal vs conditional association`, `GWAS`
- **为什么对您有用**: 本文直接连接您的因果推断兴趣（区分直接与间接效应）和流行病学应用（GWAS 数据中的遗传相关分析）。您武器库中的非参数统计和因果推断估计理论可用于评估 ND 在非高斯或高维设定下的稳健性。中期可做：需先在 moderately_familiar 的识别理论上长肌肉（如理解 ND 与 DAG 因果图假设的关系），然后可探索 ND 在 proximal causal inference 中 negative control 设定下的推广。

### 17. [10.1093/biomtc/ujae148](https://doi.org/10.1093/biomtc/ujae148) — Estimation of a genetic Gaussian network using GWAS summary data
- **作者**: Yihe Yang, Noah Lorincz-Comi, Xiaofeng Zhu
- **期刊/来源**: Biometrics
- **机构**: Case Western Reserve University
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对GWAS汇总统计量构建多表型遗传高斯网络（即遗传相关矩阵的逆矩阵）的估计问题。由于遗传相关估计存在估计误差和异质性多效性偏差，传统方法效果不佳。作者提出EGG方法，利用多变量孟德尔随机化中的工具变量技术同时消除两类偏差。该方法估计的网络可解释为表型间条件于其他表型的共享共同生物学贡献。模拟和真实数据表明EGG优于传统网络估计器。对您而言，该工作将因果推断中的IV方法（孟德尔随机化）应用于遗传网络估计，属于流行病学应用方向，且其偏差校正思路与proximal CI中的negative control思想有相通之处。
- **关键技术**: `multivariable Mendelian randomization`, `instrumental variables`, `genetic correlation matrix`, `idiosyncratic pleiotropy`, `graphical model estimation`
- **为什么对您有用**: 本文属于流行病学应用方向，直接使用因果推断中的IV方法（孟德尔随机化）解决遗传网络估计中的偏差问题，与您的secondary interest（流行病学应用）高度匹配。您武器库中'very_familiar'的'estimation theory in causal inference'可直接用于理解其IV偏差校正机制，而'moderately_familiar'的'identification theory in causal inference'可帮助评估其识别假设的合理性。这是一篇值得阅读全文的流行病学应用论文，其分析模式（利用IV处理未观测混杂）可迁移至您关注的proximal CI或sensitivity analysis问题。

### 18. [10.1093/biomtc/ujae155](https://doi.org/10.1093/biomtc/ujae155) · [arXiv](https://arxiv.org/abs/2402.13391) — De-biasing the bias: methods for improving disparity assessments with noisy group measurements
- **作者**: Solvejg Wastvedt, Joshua Snoke, Denis Agniel, Julie Lai, Marc N Elliott, Steven C Martino
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究在种族/民族信息缺失或测量有噪声时，如何评估临床决策支持算法中的公平性指标偏差。目标 estimand 是真实群体下的算法性能差异（如假阳性率差），但观测数据仅提供群体归属概率（如基于姓名和地理的 imputed probabilities）。核心贡献是提出一套去偏方法：首先推导了常用公平性指标（如假阳性率差、假阴性率差）在群体概率误差下的统计偏差解析表达式，并给出理论界；然后提出一种敏感性分析方法，允许实践者在假设的群体概率误差范围内估计偏差范围，从而评估算法偏倚的稳健性。方法工具包括偏差分解、泰勒展开和概率不等式。案例研究使用 modified Bayesian Improved First and Surname Geocoding (BIFSG) 算法 imputed 的种族概率，评估骨质疏松治疗临床决策支持算法中的 disparities。对您而言，本文的偏差分析框架和敏感性分析思路可迁移到因果推断中的 measurement error 问题（如 proximal CI 中 negative control 的测量误差敏感性），且其理论界的推导方式与您熟悉的 minimax 界技术有相通之处。
- **关键技术**: `sensitivity analysis`, `measurement error correction`, `bias decomposition`, `fairness metrics`, `imputed group probabilities`
- **为什么对您有用**: 本文直接连接您 primary interest 中的因果推断（测量误差下的偏差分析）和 epidemiology（临床算法公平性评估）。技术层面，您 very_familiar 的 minimax bounds 和 nonparametric statistics 可用于验证本文理论界的紧性，或推广到更一般的测量误差结构。中期可做：若想将本文的偏差分解框架与 proximal CI 的 negative control 假设结合，需先在 moderately_familiar 的 identification theory 上加强（具体为测量误差下的非参数识别条件）。

### 19. [10.1093/biomtc/ujae120](https://doi.org/10.1093/biomtc/ujae120) — Likelihood adaptively incorporated external aggregate information with uncertainty for survival data
- **作者**: Ziqi Chen, Yu Shen, Jing Qin, Jing Ning
- **期刊/来源**: Biometrics
- **机构**: East China Normal University · The University of Texas MD Anderson Cancer Center · National Institute of Allergy and Infectious Diseases
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对生存数据中主队列样本量小、外部汇总信息（如癌症登记数据库的汇总生存数据）存在变异性的问题，提出了一种外部信息整合的似然方法。该方法通过构建一个连接主队列似然与外部汇总统计量的联合似然函数，并显式建模外部信息的抽样变异性，从而在整合外部信息时避免过度信任。估计量通过极大化该联合似然得到，作者建立了估计量的渐近正态性，并给出了方差估计。模拟研究验证了有限样本下的性能。应用部分将MD Anderson的炎性乳腺癌队列与NCDB的汇总生存数据整合，评估了三模式治疗对不同亚型生存的影响。该方法本质上是一种利用外部汇总信息进行因果效应或预后估计的框架，与proximal CI或IV中利用外部辅助信息的思想有相通之处。对于您而言，该工作展示了在生存分析设定下如何将外部汇总信息（而非个体数据）纳入主分析，并处理其不确定性，这为流行病学应用中的数据整合提供了可借鉴的建模思路。
- **关键技术**: `external aggregate data integration`, `empirical likelihood`, `survival analysis`, `asymptotic normality`, `cancer registry data`
- **为什么对您有用**: 本文属于流行病学应用，直接对应您的secondary interest。其核心贡献在于处理外部汇总信息的不确定性，这在您熟悉的因果推断（如IV或proximal CI中利用外部辅助信息）中是一个常见但常被简化的问题。您可以用very_familiar的estimation theory in causal inference中的工具（如M-estimation框架）来重新审视其估计量的渐近性质，或将其整合思路推广到因果效应的identification中。中期可做：若想将类似方法用于proximal CI中的negative control信息整合，需先在moderately_familiar的identification theory in causal inference上深入。

### 20. [10.1093/biomtc/ujae140](https://doi.org/10.1093/biomtc/ujae140) — Optimal adaptive SMART designs with binary outcomes
- **作者**: Rik Ghosh, Bibhas Chakraborty, Inbal Nahum-Shani, Megan E Patrick, Palash Ghosh
- **期刊/来源**: Biometrics
- **机构**: Indian Institute of Technology Guwahati · National University of Singapore · Duke University · Duke-NUS Medical School · University of Michigan
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对序贯多阶段随机试验（SMART）中二元结局的优化分配问题，提出了一种自适应最优分配方法。在SMART设计中，患者在各阶段被随机分配至不同治疗组，但现有方法缺乏对每阶段最优分配的理论指导，可能引发伦理问题。作者通过约束优化框架，在固定预定义目标函数渐近方差的前提下，最小化期望总治疗失败数。理论部分推导了最优自适应分配的性质，并通过模拟验证了方法的有限样本表现。实证部分基于M-bridge研究（针对大一新生酒精风险的行为干预SMART）展示了方法的实用性。该工作直接关联因果推断中的纵向干预设计和动态治疗策略优化，对您关注的sequential multiple-assignment和mediation分析有参考价值。
- **关键技术**: `constrained optimization`, `adaptive randomization`, `sequential multiple-assignment randomized trial (SMART)`, `asymptotic variance`, `dynamic treatment regimes`
- **为什么对您有用**: 本文属于因果推断中纵向干预设计的应用方法，直接对应您primary interest中的'longitudinal'和'causal inference'子方向。技术层面，其约束优化框架可与您moderately_familiar的identification theory结合，用于评估动态治疗策略的识别条件。中期可做：需先在semiparametric theory上巩固，以理解其渐近方差约束与效率界的关系。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1093/biomtc/ujae144](https://doi.org/10.1093/biomtc/ujae144) — Robust and flexible learning of a high-dimensional classification rule using auxiliary outcomes
- **作者**: Muxuan Liang, Jaeyoung Park, Qing Lu, Xiang Zhong
- **期刊/来源**: Biometrics
- **机构**: University of Florida · University of Central Florida
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究高维线性分类规则估计问题，目标变量为感兴趣的二值结局，同时存在多个辅助结局变量。传统多任务学习（MTL）通过最小化所有结局的平均损失来共享信息，但当MTL模型设定错误时，对目标结局的估计会产生偏差。作者将估计偏差分解为子空间内偏差和子空间间偏差两类，并据此提出一种鲁棒的迁移学习方法：先用所有结局做MTL步骤以提升效率，再用仅含目标结局的数据做校准步骤以纠正两类偏差。理论分析表明，最终估计量的估计误差可低于仅用单一目标结局的估计量。模拟和真实数据分析验证了方法的优越性。本文与您的高维统计和因果推断兴趣相关，其偏差分解与校准思路可迁移至高维因果效应估计中的模型误设问题。
- **关键技术**: `multi-task learning`, `bias decomposition (within-subspace vs against-subspace)`, `transfer learning`, `high-dimensional linear discriminant rule`, `calibration step`
- **为什么对您有用**: 本文连接您的高维统计兴趣，其偏差分解与校准步骤为处理高维因果推断中的模型误设提供了可迁移的框架。您可以用非常熟悉的高维渐近理论分析其估计量的收敛速率，并检验其偏差校正是否达到半参数效率界。中期可做：将校准步骤与您的HOIF工具结合，用于高维因果效应的鲁棒估计。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1093/biomtc/ujae127](https://doi.org/10.1093/biomtc/ujae127) · [arXiv](https://arxiv.org/abs/2308.12540) — Wasserstein regression with empirical measures and density estimation for sparse data
- **作者**: Yidong Zhou, Hans-Georg Müller
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究响应变量为分布（以Wasserstein距离度量）的回归问题，目标是利用协变量预测条件分布。现有方法需先逐个体估计每个响应分布（如核密度估计），当某些个体仅有少量观测时，这些估计不一致。作者提出基于经验测度的Wasserstein回归，直接以经验累积分布函数作为响应，避免密度估计的预处理步骤。核心机制是利用协变量信息，通过全局回归模型“借力”所有个体的数据，从而对稀疏个体仍能得到一致的条件分布估计。方法采用Fr\'echet回归框架，在Wasserstein空间中定义条件Fréchet均值，并建立估计量的收敛速率。模拟和儿童健康数据表明，该方法在个体样本量差异大时显著优于逐个体估计的传统方法。对您而言，该工作展示了非参数回归与最优传输的结合，其“借力”思想可迁移至因果推断中稀疏子组的异质性处理效应估计。
- **关键技术**: `Fr\'echet regression`, `Wasserstein distance`, `empirical measure`, `conditional distribution estimation`, `borrowing strength`
- **为什么对您有用**: 连接非参数统计与因果推断：本文的“借力”思想可直接用于处理效应异质性分析中稀疏子组的分布估计。武器库中`nonparametric statistics`和`estimation theory in causal inference`足以理解并复现其核心方法，属于**立即可做**的迁移方向。

## 数理统计 / 假设检验  *(hypothesis_testing, 5 篇)*

### 1. [10.1093/biomtc/ujae142](https://doi.org/10.1093/biomtc/ujae142) — Joint mirror procedure: controlling false discovery rate for identifying simultaneous signals
- **作者**: Linsui Deng, Kejun He, Xianyang Zhang
- **期刊/来源**: Biometrics
- **机构**: Chinese University of Hong Kong, Shenzhen · Renmin University of China · Texas A&M University
- **分类**: vol 80 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文提出 Joint Mirror (JM) 过程，用于在同时检验多个假设（如中介分析中的暴露-中介效应与中介-结局效应、可重复性分析中的跨研究联合信号）时控制错误发现率（FDR）。JM 过程是一种迭代方法，通过逐步收缩拒绝域，直到保守估计的假发现比例低于目标 FDR 水平，从而在有限样本下实现 FDR 控制。作者还引入了一种更严格的错误度量——复合 FDR（cFDR），为每个假发现按其空分量数量赋予权重。利用留一法（leave-one-out）技术，证明了 JM 过程在有限样本下控制 cFDR。算法设计上，JM 过程能融入偏序信息以提高效率。模拟表明，该方法在多种场景（包括特征间检验统计量相依的情况）下有效控制 cFDR 并提升统计功效。最后，通过中介分析和可重复性分析的实际数据应用展示了方法的实用性。对您而言，本文直接关联到您对假设检验和因果推断（特别是中介分析）的兴趣，其有限样本 FDR 控制技术可迁移至您关注的纵向或高维中介设定。
- **关键技术**: `Joint mirror procedure`, `False discovery rate (FDR)`, `Composite FDR (cFDR)`, `Leave-one-out technique`, `Iterative rejection region shrinkage`, `Partial ordering information`
- **为什么对您有用**: 本文直接连接您的 primary interest 中的 hypothesis testing 和 causal inference（mediation analysis）。技术层面，您可以用 very_familiar 的 minimax bounds 或 high-dimensional asymptotics 来评估 JM 过程在高维或弱信号下的最优性，或用 moderately_familiar 的 identification theory 将其推广到更复杂的中介结构（如纵向中介）。**中期可做**：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，以处理 JM 过程在非参数中介模型中的适应性。

### 2. [10.1093/biomtc/ujae119](https://doi.org/10.1093/biomtc/ujae119) — A formal goodness-of-fit test for spatial binary Markov random field models
- **作者**: Eva Biswas, Andee Kaplan, Mark S Kaiser, Daniel J Nordman
- **期刊/来源**: Biometrics
- **机构**: Iowa State University · Colorado State University
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对空间二元数据的马尔可夫随机场（MRF）模型，提出了一种形式化的拟合优度（GOF）检验方法。核心挑战在于二元数据的邻域结构难以评估，而现有模型诊断工具不足。检验统计量基于拟合条件概率构造了一种条件Moran's I，能够检测模型形式（包括邻域结构）的偏离。数值研究表明，该检验在检测邻域设定错误等偏离时具有良好的功效。方法应用于Besag的历史菊苣数据和爱荷华州草蜢麻雀的繁殖模式数据。该工作为空间统计中的模型诊断提供了首个形式化检验框架，对您在高维统计和假设检验方面的兴趣有直接连接——检验统计量的构造思路（基于条件概率的Moran's I）可视为一种特殊的U-统计量，其高阶性质值得进一步分析。
- **关键技术**: `conditional Moran's I`, `goodness-of-fit test`, `Markov random field`, `spatial binary data`, `neighborhood specification`
- **为什么对您有用**: 本文直接连接您的假设检验兴趣，特别是空间统计中的模型诊断问题。检验统计量（条件Moran's I）本质上是一种U-统计量，您可以用higher-order U-statistics的treewidth/einsum视角分析其计算复杂度，或用minimax bound验证其功效是否最优。中期可做：需先在moderately_familiar的higher-order U-statistics理论上长肌肉，才能深入分析该统计量的高阶投影和渐近分布。

### 3. [10.1093/biomtc/ujae128](https://doi.org/10.1093/biomtc/ujae128) — Robust model averaging approach by Mallows-type criterion
- **作者**: Miaomiao Wang, Kang You, Lixing Zhu, Guohua Zou
- **期刊/来源**: Biometrics
- **机构**: Beijing University of Chinese Medicine · University of Chinese Academy of Sciences · University of Kent · Capital Normal University · Beijing Normal University
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对均值回归中模型平均方法对异常值敏感的问题，提出了一种基于Mallows准则的鲁棒模型平均方法。首先，对每个候选模型构造广义M估计量（GM估计量），然后基于GM型损失函数的最终预测误差渐近展开构建鲁棒权重方案。理论部分证明了权重估计量收敛到理论最优权重，且模型平均估计量具有有界影响函数，并定义了经验预测影响函数以评估定量鲁棒性。模拟和真实数据分析验证了有限样本性能。该方法填补了均值回归中缺乏最优鲁棒模型平均方法的空白。对您而言，该工作涉及模型平均与鲁棒统计的结合，其有界影响函数和渐近理论可能为您的因果推断中敏感性分析或高维统计中的稳健估计提供新视角。
- **关键技术**: `Mallows-type criterion`, `generalized M-estimator`, `influence function`, `model averaging`, `robust regression`
- **为什么对您有用**: 本文属于假设检验与模型平均的交叉方向，直接关联您的primary interest中的数学统计与假设检验。技术武器库中的非参数统计和M估计理论可用于分析其GM估计量的渐近性质，而您对高维渐近的熟悉程度可帮助评估该方法在高维或复杂模型下的扩展性。中期可做：需先在M估计理论上进一步熟悉，以深入理解其影响函数推导。

### 4. [10.1093/biomtc/ujae125](https://doi.org/10.1093/biomtc/ujae125) · [arXiv](https://arxiv.org/abs/2402.02867) — A new robust approach for the polytomous logistic regression model based on Rényi’s pseudodistances
- **作者**: Elena Castilla
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对多分类逻辑回归模型，提出基于 Rényi 伪距离（RP）的稳健估计与检验框架。目标是在存在误分类等污染数据时，替代传统的极大似然估计（MLE）。估计量由调节参数 α≥0 控制，当 α=0 时退化为 MLE。核心机制是极小化 RP 距离，构造 Wald 型检验统计量，并推导其渐近分布。模拟与真实数据表明，该方法在污染比例较高时显著优于 MLE，且 α 的选择可平衡效率与稳健性。对您而言，该文展示了如何将伪距离（一种非参数/半参数工具）引入经典广义线性模型，其稳健检验思路可迁移至因果推断中的敏感性分析或高维 logistic 回归的稳健推断。
- **关键技术**: `Rényi pseudodistance`, `minimum distance estimation`, `Wald-type test`, `polytomous logistic regression`, `robust estimation`
- **为什么对您有用**: 本文属于假设检验与稳健统计的交叉，直接对应 primary interest 中的 'hypothesis testing' 和 'mathematical statistics'。其核心工具 Rényi 伪距离是一种非参数距离，与您武器库中的 'nonparametric statistics' 和 'M-estimation theory' 高度匹配——您可以用 M-estimation 的渐近理论框架分析该估计量的 influence function 和 breakdown point。中期可做：将 RP 距离推广至半参数模型（如倾向得分加权或 IV 回归中的稳健估计），这需要先在 'semiparametric theory' 上长肌肉。

### 5. [10.1093/biomtc/ujae157](https://doi.org/10.1093/biomtc/ujae157) — Spatially adaptive variable screening in presurgical functional magnetic resonance imaging data analysis
- **作者**: Yifei Hu, Xinge Jessie Jeng
- **期刊/来源**: Biometrics
- **机构**: North Carolina State University
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对术前功能磁共振成像（fMRI）数据分析中的变量筛选问题，提出了一种新的贝叶斯遗漏发现率（BMDR）指标，用于在体素特异性混合模型下控制假阴性。基于BMDR，作者开发了一个空间自适应变量筛选程序，该程序不仅直接控制假阴性率，还利用了fMRI数据的空间结构信息。与现有方法相比，该程序完全数据驱动，无需人工设定阈值。数值实验表明，新方法在保留信号体素（尤其是功能区域边界的微弱信号）方面优于多种现有方法，并能更清晰地将功能区域与背景噪声分离。该方法对功能保留的神经外科手术规划具有重要应用价值。对您而言，本文提出的假阴性控制框架和空间自适应筛选策略，可迁移至您感兴趣的因果推断或流行病学中的变量选择问题，尤其是在需要优先控制假阴性的场景（如药物安全性筛查）中具有参考价值。
- **关键技术**: `Bayesian missed discovery rate (BMDR)`, `voxel-specific mixture model`, `spatial adaptive screening`, `false negative control`, `fMRI data analysis`
- **为什么对您有用**: 本文属于应用统计方法论文，与您的主要兴趣（假设检验）有直接关联，但更偏向于生物医学应用。其提出的BMDR指标和空间自适应筛选程序，在控制假阴性方面有创新性，可启发您在因果推断或流行病学中处理类似问题（如敏感性分析中的假阴性控制）。不过，本文的方法论深度有限，未涉及您武器库中的高阶工具（如U统计量或半参效率理论），因此作为应用案例阅读即可，暂不可直接迁移。

## 流行病学  *(epidemiology, 3 篇)*

### 1. [10.1093/biomtc/ujae117](https://doi.org/10.1093/biomtc/ujae117) — Case-crossover designs and overdispersion with application to air pollution epidemiology
- **作者**: Samuel Perreault, Gracia Y Dong, Alex Stringer, Hwashin Shin, Patrick E Brown
- **期刊/来源**: Biometrics
- **机构**: St. Michael's Hospital · University of Toronto · Centre for Global Health Research · St Michaels Hospital · University of Waterloo · Health Canada
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文聚焦于空气污染流行病学中常用的 case-crossover 设计，该设计通常与条件逻辑模型结合，用于估计健康结局与短期暴露（如空气污染）之间的关联。作者首先澄清了条件逻辑模型与 Poisson 时间序列模型在典型设定下的等价性，并指出传统 case-crossover 分析隐含的个体独立性假设无法处理过分散问题。为此，他们提出放松个体间独立性假设，在条件逻辑模型中显式引入过分散，从而得到过分散条件逻辑模型。理论证明该模型与过分散条件 Poisson 模型在似然上互为重新表达。作者进一步给出了贝叶斯实现细节，并通过大规模模拟研究展示：标准 case-crossover 模型在存在过分散时覆盖概率严重偏低，而所提模型表现稳健。最后，利用多伦多空气污染与发病率的实际数据，验证了新模型对节假日等异常值的鲁棒性优于传统方法。该文对您作为流行病学应用方向（secondary interest）的入门读物很有价值，其模型等价性推导和贝叶斯实现思路清晰，适合了解 case-crossover 设计的统计基础。
- **关键技术**: `case-crossover design`, `conditional logistic model`, `overdispersion`, `Poisson time series model`, `Bayesian implementation`
- **为什么对您有用**: 本文属于流行病学应用（secondary interest），适合作为 gateway reading：它清晰阐述了 case-crossover 设计的统计模型、与 Poisson 模型的等价性，以及过分散的处理方法，对不熟悉该领域的统计学家友好。武器库中 'estimation theory in causal inference' 和 'software development' 可直接用于复现或扩展其贝叶斯实现，但核心方法（条件逻辑模型、过分散建模）不在 primary interest 中，属于暂不可做方向——缺乏流行病学特定模型（如条件逻辑）的深度经验。值得花时间读全文以了解该设计框架。

### 2. [10.1093/biomtc/ujae147](https://doi.org/10.1093/biomtc/ujae147) — A likelihood approach to incorporating self-report data in HIV recency classification
- **作者**: Wenlong Yang, Danping Liu, Le Bao, Runze Li
- **期刊/来源**: Biometrics
- **机构**: Pennsylvania State University · National Cancer Institute · Division of Cancer Epidemiology and Genetics
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对HIV新近感染分类问题，提出一种基于似然的概率模型，整合自我报告检测史与生物标志物数据。在PHIA调查框架下，HIV新近状态部分可观测（如1年前阳性者必为长期感染），模型同时刻画新近状态对生物标志物的依赖机制，以及新近状态与自我报告最近检测时间对检测结果的联合影响。采用极大似然估计，并与逻辑回归、分类树（当前实践）在马拉维PHIA真实数据及模拟数据上比较。结果显示所提模型参数估计更高效、偏差更小，且对报告误差和模型误设相对稳健。对您而言，本文是流行病学中因果推断与缺失数据问题的良好应用案例，其部分可观测状态下的似然建模思路可迁移至proximal causal inference中的negative control设定。
- **关键技术**: `likelihood-based probabilistic model`, `partially observed recency status`, `self-report testing history`, `biomarker integration`, `model misspecification robustness`
- **为什么对您有用**: 本文属于流行病学应用，使用似然方法处理部分可观测状态，与您secondary interest中的流行病学数据集和因果推断方法直接相关。您的武器库中'identification theory in causal inference'和'M-estimation theory'可用来分析其部分可观测假设的识别性，以及似然估计的渐近效率。这是一篇值得读全文的入门级流行病学方法论文，但核心机器（部分可观测似然建模）在您的武器库中已有覆盖，属于**立即可做**的阅读范畴。

### 3. [10.1093/biomtc/ujae122](https://doi.org/10.1093/biomtc/ujae122) — Derivation of outcome-dependent dietary patterns for low-income women obtained from survey data using a supervised weighted overfitted latent class analysis
- **作者**: Stephanie M Wu, Matthew R Williams, Terrance D Savitsky, Briana J K Stephenson
- **期刊/来源**: Biometrics
- **机构**: Harvard University · RTI International · Bureau of Labor Statistics
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对低收入女性群体，研究饮食模式与高血压结局的关联。数据来自复杂调查（NHANES），存在选择偏差和抽样权重问题。作者提出监督加权过拟合潜类分析（SWOLCA），在贝叶斯伪似然框架下将抽样权重整合到暴露-结局离散数据模型中。模型通过MCMC吉布斯采样处理分层、整群和信息性抽样，并允许交互效应。模拟显示SWOLCA在偏差、精度和覆盖率上表现良好。实证部分刻画了与高血压相关的饮食模式。对您而言，本文是流行病学中处理复杂调查数据和潜类分析的实例，其加权伪似然思路可迁移至因果推断中处理survey-weighted estimand的识别与估计。
- **关键技术**: `Bayesian pseudo-likelihood`, `overfitted latent class analysis`, `sampling weights`, `MCMC Gibbs sampling`, `complex survey design`
- **为什么对您有用**: 本文属于流行病学应用，使用NHANES真实数据，分析模式可迁移至您关注的survey-weighted causal inference问题。武器库中'identification theory in causal inference'可用来审视其加权伪似然是否对应某个survey-weighted ATE的识别条件。中期可做：需先在moderately_familiar的'identification theory in causal inference'上长肌肉，理解survey-weighted estimand的因果解释。

## 其他  *(other, 22 篇)*

### 1. [10.1093/biomtc/ujae138](https://doi.org/10.1093/biomtc/ujae138) — Large-scale survival analysis with a cure fraction
- **作者**: Bo Han, Xiaoguang Wang, Liuquan Sun
- **期刊/来源**: Biometrics
- **机构**: Yunnan University · Dalian University of Technology · Academy of Mathematics and Systems Science · University of Chinese Academy of Sciences
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对大规模生存数据中存在治愈比例（cure fraction）的问题，提出了一种新的概率加权方法用于半参数治愈回归模型的估计与推断。模型采用混合治愈框架：发病率部分无模型假设，潜伏期部分由半参数比例风险模型刻画。通过易感概率（susceptible probability）作为权重，构建加权估计方程，在小样本场景下实现参数估计。权重采用稳健的非参数估计，保证了估计的稳定性。进一步，提出基于数据块的递归概率加权估计方法，适用于大规模或在线数据场景，显著降低了计算和内存开销。建立了所提估计量的渐近性质，并通过模拟和实际数据验证了方法的有效性。对您而言，本文的加权估计和分块递归策略可能对您在高维或大规模因果推断中的计算效率问题有启发，但整体方法学创新性一般。
- **关键技术**: `mixture cure model`, `probability-weighted estimating equation`, `recursive estimation`, `data block partitioning`, `semiparametric proportional hazards`
- **为什么对您有用**: 本文属于生存分析中治愈模型的估计方法，与您的主要兴趣（因果推断、半参理论）仅有间接关联。其加权估计和分块递归策略在计算效率上的思路可能对您在高维或大规模因果推断中的计算问题有参考价值，但核心方法学（治愈模型、比例风险）不在您的武器库核心范围内。暂不可做——需要先熟悉生存分析中的治愈模型框架和加权估计理论。

### 2. [10.1093/biomtc/ujae149](https://doi.org/10.1093/biomtc/ujae149) · [arXiv](https://arxiv.org/abs/2309.03714) — An efficient joint model for high dimensional longitudinal and survival data via generic association features
- **作者**: Van Tuan Nguyen, Adeline Fermanian, Antoine Barbieri, Sarah Zohar, Anne-Sophie Jannot, Simon Bussy et al.
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文提出 FLASH 方法，用于高维纵向数据与删失生存时间的联合建模。模型结合共享随机效应与联合潜在类思想，通过正则化自动筛选有预后意义的纵向特征。估计采用 EM 算法，并给出高效实现。在模拟和真实医疗数据上，FLASH 在实时预测的 C-index 上显著优于现有联合模型，计算速度提升数个数量级。该方法自动识别重要特征，具有可解释性。对您而言，本文属于应用型工作，方法学创新有限，但纵向数据与生存数据的联合建模是因果推断中 mediation 和 longitudinal 设定的常见场景，可作为背景参考。
- **关键技术**: `joint modeling`, `EM algorithm`, `regularization`, `high-dimensional longitudinal data`, `survival analysis`
- **为什么对您有用**: 本文属于流行病学领域的应用工作，与您的 secondary interest 中的 epidemiology 相关。方法学上以 EM 和正则化为主，与您的 technical arsenal 中非常熟悉的非参数统计、高维渐近等工具交集不大，但可作为 longitudinal causal inference 的入门阅读。暂不可做：核心方法（joint modeling with regularization）不在您的武器库中，且本文未涉及您擅长的效率理论或 U-statistic。

### 3. [10.1093/biomtc/ujae115](https://doi.org/10.1093/biomtc/ujae115) — Temporal generative models for learning heterogeneous group dynamics of ecological momentary assessment data
- **作者**: Soohyun Kim, Young-geun Kim, Yuanjia Wang
- **期刊/来源**: Biometrics
- **机构**: Columbia University · Columbia University Irving Medical Center
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对生态瞬时评估（EMA）数据的高维、相关、层次结构，提出了一种新的时间生成模型 HDRBM，以学习异质性群体动态。现有混合效应模型对固定/随机效应和相关性结构有较强假设，而循环时间受限玻尔兹曼机（RTRBM）虽能建模时间序列，但未考虑基于协变量的群体异质性。HDRBM 通过引入协变量来改进 RTRBM，从而捕捉不同子群体的动态差异。在模拟和真实 EMA 数据集上，HDRBM 在预测准确性和可解释性上优于基准模型，并能揭示群体动态的潜在驱动因素。该方法本质上是一种生成式神经网络，不涉及因果识别、半参效率或高维统计推断等核心兴趣方向。对您而言，本文属于应用统计方法论文，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接技术重叠，但可作为流行病学或精神健康领域应用工作的背景阅读。
- **关键技术**: `Restricted Boltzmann Machine`, `recurrent temporal RBM`, `generative neural network`, `mixed-effect models`, `ecological momentary assessment`
- **为什么对您有用**: 本文属于流行病学领域的应用工作，与您的次要兴趣（流行病学数据集、应用因果工作）有弱关联。但方法学上为生成式神经网络，不涉及您武器库中的非参统计、U-统计量或因果推断工具，因此暂不可做——核心机器（RBM 训练、时间序列生成模型）不在您的武器库中。可作为流行病学 EMA 数据应用的入门读物，但无需深入阅读全文。

### 4. [10.1093/biomtc/ujae150](https://doi.org/10.1093/biomtc/ujae150) — Time-dependent prognostic accuracy measures for recurrent event data
- **作者**: R Dey, D E Schaubel, J A Hanley, P Saha-Chaudhuri
- **期刊/来源**: Biometrics
- **机构**: McGill University · University of Pennsylvania · Biogen (United States)
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对复发事件数据（同一患者可能经历多次事件）提出新的预后准确性度量方法。研究设定中，基线生物标志物或复合评分用于预测复发事件风险，但现有文献缺乏针对此类数据的准确性评估工具。作者基于半参数脆弱模型（semiparametric frailty model）构建估计量，该模型能够处理标志物的信息性和患者间未观测到的异质性。估计量的渐近性质被严格推导，并通过模拟研究验证了有限样本下的低偏倚和适当覆盖率。方法被应用于囊性纤维化患者数据，评估基线肺功能指标（用力呼气量）对反复肺部感染发作的预测能力。本文属于应用统计方法开发，方法学创新程度有限，但为复发事件数据提供了实用的预测评估工具。
- **关键技术**: `semiparametric frailty model`, `prognostic accuracy measures`, `recurrent event data`, `time-dependent ROC`
- **为什么对您有用**: 本文与您的次要兴趣流行病学（复发事件数据在临床队列中常见）相关，但方法学核心（半参数脆弱模型）与您的主要兴趣方向（因果推断、高维统计、U统计量）无直接交集。您的技术武器库中非参数统计和M估计理论可用于理解其渐近性质，但本文未涉及您擅长的效率理论或高阶U统计量。暂不可做：核心问题（复发事件预后准确性）与您当前研究方向距离较远，不值得投入时间精读。

### 5. [10.1093/biomtc/ujae136](https://doi.org/10.1093/biomtc/ujae136) · [arXiv](https://arxiv.org/abs/2312.06018) — A multivariate Polya tree model for meta-analysis with event-time distributions
- **作者**: Giovanni Poli, Elena Fountzilas, Apostolia-Maria Tsimeridou, Peter Müller
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出一种多元 Polya 树（multivariate PT）先验，用于对多个事件时间分布 G_1,...,G_n 进行联合非参数贝叶斯建模，适用于 meta-analysis 场景。模型将每个研究 i 的事件时间分布 G_i 视为一个 Polya 树过程，并通过在 logit 分裂概率上引入高斯过程先验来引入研究间相关性，该高斯过程以研究层面的协变量为索引，使得协变量相似的研究具有更高的相关性。后验更新是条件共轭的，且可直接利用事件时间数据中常见的汇总统计量（如中位生存时间、生存概率）进行推断。方法在癌症免疫治疗 meta-analysis 数据上进行了展示。
- **关键技术**: `Polya tree prior`, `Gaussian process prior`, `nonparametric Bayesian meta-analysis`, `conditional conjugacy`, `event-time distribution`
- **为什么对您有用**: 本文属于贝叶斯非参数方法在 meta-analysis 中的应用，与您的主要兴趣（非参数理论、因果推断中的纵向数据）关联较弱。但若您未来涉足生存分析或 meta-analysis 中的异质性建模，该文提供的多元 Polya 树构造可作为先验建模的参考。目前武器库中缺乏贝叶斯非参数工具（如 Polya tree、Dirichlet process），因此暂不可做。

### 6. [10.1093/biomtc/ujae111](https://doi.org/10.1093/biomtc/ujae111) · [arXiv](https://arxiv.org/abs/2407.05089) — Bayesian network-guided sparse regression with flexible varying effects
- **作者**: Yangfan Ren, Christine B Peterson, Marina Vannucci
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文提出 VERGE（Varying Effects Regression with Graph Estimation），一种贝叶斯变系数回归方法，用于高维预测变量（如微生物组特征）的特征选择。模型区分预测变量（用于结果预测的特征）和主体层协变量（调节预测变量效应），构建变系数框架，并利用预测变量间的网络结构（通过贝叶斯图估计推断）来鼓励选择网络相连的预测变量。采用 spike-and-slab 先验实现变量选择，同时选择网络关联的预测变量和调节效应的协变量。模拟研究表明 VERGE 在特征选择和预测精度上优于现有方法。应用于肠道微生物组对肥胖影响的研究，识别出微生物类群及其生态依赖关系，并发现性别和饮食等协变量调节微生物预测变量的系数。本文方法学贡献在于将网络结构先验融入变系数回归，但核心工具（贝叶斯图模型、spike-and-slab）与您的主要兴趣（因果推断、高维统计、U-统计量）距离较远，且缺乏理论效率分析。
- **关键技术**: `Bayesian varying coefficient model`, `spike-and-slab prior`, `graphical model`, `network-guided feature selection`, `MCMC`
- **为什么对您有用**: 本文属于生物统计应用（微生物组），与您的次要兴趣流行病学有间接关联，但方法学核心是贝叶斯变系数回归与图模型，不涉及因果推断、高维渐近或效率理论。您的武器库（非参统计、minimax 界、U-统计量）难以直接攻入该论文的核心问题。暂不可做——缺少贝叶斯计算（MCMC 收敛诊断、后验一致性分析）的专门工具。作为流行病学应用，本文展示了微生物组数据中协变量-预测变量交互的分析流程，但方法学新颖性有限，不值得优先阅读。

### 7. [10.1093/biomtc/ujae113](https://doi.org/10.1093/biomtc/ujae113) · [arXiv](https://arxiv.org/abs/2310.07330) — Functional generalized canonical correlation analysis for studying multiple longitudinal variables
- **作者**: Lucas Sort, Laurent Le Brusquet, Arthur Tenenhaus
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出功能广义典型相关分析（functional GCCA），用于研究多个纵向随机过程之间的关联结构。方法基于多块正则化广义典型相关分析框架，能够处理稀疏和不规则观测的纵向数据。作者证明了求解过程的单调性，并引入贝叶斯方法估计典型成分。进一步扩展了框架以整合单变量或多变量响应，从而支持预测性应用。模拟研究评估了方法效率，并在一个纵向数据集上展示了实际应用。该方法对您可能有用：它涉及纵向数据的关联分析，与您对因果推断中纵向设定的兴趣有间接关联，但方法学贡献主要在于多变量函数型数据分析，而非因果识别或效率理论。
- **关键技术**: `functional generalized canonical correlation analysis`, `multiblock regularized GCCA`, `Bayesian estimation`, `sparse and irregular longitudinal data`
- **为什么对您有用**: 本文属于纵向数据分析的方法学工作，与您对因果推断中纵向设定的兴趣有间接关联，但核心方法（函数型GCCA）并非您武器库中的核心工具。武器库中'非参数统计'和'高维渐近'可用于理解其正则化框架的收敛性，但方法本身不涉及因果识别或效率理论。暂不可做：核心机器（函数型数据分析、贝叶斯典型成分估计）不在武器库中，且与您的主要兴趣方向（因果推断、高维统计、U统计量）距离较远。

### 8. [10.1093/biomtc/ujae151](https://doi.org/10.1093/biomtc/ujae151) · [arXiv](https://arxiv.org/abs/2210.11107) — Graphical model inference with external network data
- **作者**: Jack Jewson, Li Li, Laura Battaglia, Stephen Hansen, David Rossell, Piotr Zwiernik
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对高维图模型推断中样本量不足且变量数p较大时模型难以解释的问题，提出利用外部网络数据（如变量间的社交网络、地理邻近网络等）来改进推断与解释。作者构建了一个 spike-and-slab 先验框架，将偏相关系数与网络数据通过回归模型连接起来，具体建模了边概率、平均偏相关系数及其方差对网络数据的依赖关系。核心目标是检测网络数据是否与图模型相关，并在相关时解释其影响机制。方法上开发了 R 语言和概率编程语言的实现。在 COVID-19 美国县级传播与社交媒体共演的应用中，展示了引入网络数据能提升模型解释性、统计精度和样本外预测能力。本文属于应用导向的方法学工作，方法创新程度中等（novelty_flag: application）。
- **关键技术**: `spike-and-slab prior`, `graphical model`, `partial correlation regression`, `probabilistic programming`, `network data integration`
- **为什么对您有用**: 本文连接的是 secondary interest 中的流行病学应用方向（COVID-19 传播与社交网络数据），但方法学核心（图模型 + 外部网络先验）与 primary interest 中的因果推断（如网络干预、中介分析）有间接关联。武器库中 very_familiar 的 'estimation theory in causal inference' 和 'nonparametric statistics' 可帮助理解其先验设定与推断性质，但本文更偏向贝叶斯建模与计算，与研究者擅长的频率学派 minimax 和 U-statistic 工具交集有限。暂不可做——核心机器（spike-and-slab 变分推断、概率编程语言实现）不在武器库中，且方法学 novelty 不足以驱动研究者投入时间深入。

### 9. [10.1093/biomtc/ujae107](https://doi.org/10.1093/biomtc/ujae107) — Composite dyadic models for spatio-temporal data
- **作者**: Michael R Schwob, Mevin B Hooten, Vagheesh Narasimhan
- **期刊/来源**: Biometrics
- **机构**: The University of Texas at Austin · Dell Children's Medical Center of Central Texas
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对景观遗传学中的时空数据，提出了一种贝叶斯层次 dyadic 模型，用于推断影响基因流动的空间机制。现有方法未考虑时间依赖性且计算成本高，作者通过构建全连接网络并采用归一化复合似然来刻画时空依赖结构。模型将物理机制融入 dyadic 框架，并应用于青铜时代欧洲古人类 DNA 数据，以推断影响人类迁徙的机制。方法上强调可扩展性和对大数据集的适应性，但核心是应用导向的贝叶斯建模。对您而言，该文属于流行病学或应用因果推断的次级兴趣领域，但方法学 novelty 有限，主要贡献在于应用场景和计算可扩展性。
- **关键技术**: `Bayesian hierarchical model`, `composite likelihood`, `dyadic model`, `spatio-temporal dependence`, `landscape genetics`
- **为什么对您有用**: 本文属于流行病学/应用因果推断的次级兴趣领域，涉及时空依赖建模和古DNA数据。但方法学上未涉及您核心兴趣中的因果识别、高维统计或效率理论，且 dyadic 模型与您的 higher-order U-statistics 或 tensor contraction 武器库无直接连接。作为 gateway reading，本文对统计学家友好，但问题本身（推断人类迁徙机制）更偏应用，您武器库中的非参统计或因果推断工具难以直接迁移。暂不可做，因核心机器（贝叶斯层次模型、复合似然）不在您的武器库中，且缺乏与您主要兴趣的深层连接。

### 10. [10.1093/biomtc/ujae130](https://doi.org/10.1093/biomtc/ujae130) — A hierarchical random effects state-space model for modeling brain activities from electroencephalogram data
- **作者**: Xingche Guo, Bin Yang, Ji Meng Loh, Qinxia Wang, Yuanjia Wang
- **期刊/来源**: Biometrics
- **机构**: University of Connecticut · Columbia University · New Jersey Institute of Technology · Tris Pharma (United States)
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出一种层次随机效应状态空间模型（RESSM），用于分析大规模多通道静息态脑电图（EEG）数据，目标是在考虑组间和个体间异质性的同时捕捉脑区间的动态连接模式。模型在状态空间框架中引入多层次随机效应，分别刻画时间动态矩阵和空间映射矩阵的异质性，并允许连接模式随时间非平稳变化。为解决高维随机效应矩阵的可识别性问题，作者直接建模而不施加结构约束，并在贝叶斯框架下结合Gibbs采样进行推断。模拟研究表明参数估计和推断有效。应用于一项多中心重度抑郁症（MDD）临床试验，发现MDD患者与健康对照在静息态脑时间动态上存在显著差异；且RESSM导出的个体水平EEG特征对异质性治疗效应的预测能力优于传统频带功率特征。本文属于应用统计方法论文，方法学创新在于将随机效应与状态空间模型结合处理高维EEG数据，但核心工具（贝叶斯层次模型、Gibbs采样）较为经典，对您的主要兴趣方向（因果推断、高维统计、U统计量）直接关联有限。
- **关键技术**: `state-space model`, `random effects`, `Gibbs sampling`, `Bayesian hierarchical model`, `non-stationary time series`
- **为什么对您有用**: 本文属于流行病学/生物统计应用（MDD临床试验），与您的secondary interest（epidemiology）有交集，但方法学上以贝叶斯层次模型为主，未涉及您primary interests中的因果推断、高维渐近或U统计量。作为gateway reading，本文对EEG数据结构和异质性建模有清晰阐述，但武器库中very_familiar的非参数统计、minimax界等工具难以直接切入其贝叶斯推断框架。暂不可做——核心机器（贝叶斯层次模型与Gibbs采样）不在您的武器库中，且方法学新颖性有限。

### 11. [10.1093/biomtc/ujae137](https://doi.org/10.1093/biomtc/ujae137) — Cumulative link mixed-effects models in the service of remote sensing crop progress monitoring
- **作者**: Ioannis Oikonomidis, Samis Trevezas
- **期刊/来源**: Biometrics
- **机构**: National and Kapodistrian University of Athens
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出了一种基于累积链接混合效应模型（CLM）的方法，利用遥感数据（如归一化植被指数NDVI）和气象数据（热时间）来大规模监测作物生长进度。模型包括固定效应CLM和引入年度随机效应的混合效应CLM，以捕捉不同季节间的变异性。推断基于部分似然，并提出了两种似然形式：标准的多项分布CLM和基于乘积二项分布的新形式。使用美国内布拉斯加州20年的实地数据对玉米、大豆等8种作物进行了评估，展示了模型在跨作物大规模预测中的广泛适用性。为促进可重复性，作者开发了名为“Ages of Man”的R包生态系统。该研究主要是一个应用导向的方法学工作，其统计创新在于将混合效应与累积链接模型结合用于有序分类响应，并提出了新的似然形式。对您而言，本文属于应用统计范畴，与您的主要兴趣（因果推断、高维统计等）无直接技术交集，但可作为了解农业遥感领域统计建模实践的入门参考。
- **关键技术**: `cumulative link model`, `mixed-effects model`, `partial likelihood`, `product binomial distribution`, `remote sensing`, `R package ecosystem`
- **为什么对您有用**: 本文属于应用统计，与您的主要兴趣方向（因果推断、高维统计、U统计量等）无直接技术连接。武器库中的工具（如非参数统计、M估计理论）可用于理解其模型框架，但本文并未提出需要这些工具来解决的新问题。作为gateway-reading，本文对农业遥感领域的数据结构（时空相关、有序响应）和建模思路有清晰阐述，但统计方法学深度有限，不值得投入全文时间。

### 12. [10.1093/biomtc/ujae109](https://doi.org/10.1093/biomtc/ujae109) — Heterogeneity-aware integrative regression for ancestry-specific association studies
- **作者**: Aaron J Molstad, Yanwei Cai, Alexander P Reiner, Charles Kooperberg, Wei Sun, Li Hsu
- **期刊/来源**: Biometrics
- **机构**: University of Minnesota · University of Florida · Fred Hutch Cancer Center · University of Washington · University of North Carolina at Chapel Hill
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对祖先特异性蛋白质组关联研究（PWAS）中，非洲裔人群因样本量不足导致蛋白质表达预测精度低的问题，提出了一种异质性感知的整合回归方法。模型假设不同祖先群体共享部分遗传效应，同时允许回归系数和误差方差存在群体特异性，通过惩罚最大似然估计实现信息借力。作者通过重新参数化将目标函数转化为凸优化问题，并引入尺度不变惩罚以保证估计的稳定性。为提升计算效率，进一步提出了近似版本并研究了其理论性质（如估计量的收敛速率）。在真实数据中，该方法显著提高了非洲裔个体的蛋白质表达预测精度，并在下游PWAS分析中发现了多个与血脂性状相关的祖先特异性关联。对您而言，本文属于应用统计方法在遗传流行病学中的具体案例，其核心贡献在于处理异质性群体间的信息整合与预测，而非您主要关注的理论统计或因果推断方法创新。
- **关键技术**: `penalized maximum likelihood`, `convex reparameterization`, `scale-invariant penalty`, `heterogeneous error variance`, `ancestry-specific prediction`
- **为什么对您有用**: 本文属于流行病学领域的应用工作，使用惩罚回归处理群体异质性，与您的secondary interest（流行病学应用）相关。但方法学上以预测为目标，不涉及因果推断、高维统计或效率理论等您的主要兴趣方向，且未使用您武器库中的具体工具（如U-statistics、semiparametric theory）。作为流行病学入门阅读，本文数据结构和分析流程清晰，但方法学新颖性有限，不值得投入全文阅读时间。

### 13. [10.1093/biomtc/ujae121](https://doi.org/10.1093/biomtc/ujae121) — Modeling longitudinal skewed functional data
- **作者**: Mohammad Samsul Alam, Ana-Maria Staicu
- **期刊/来源**: Biometrics
- **机构**: Duke University · North Carolina State University
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对纵向函数型数据中响应变量存在点态偏斜的问题，提出了一种新的建模框架。方法的核心是将边际点态变异与纵向及函数型依赖结构解耦：边际分布用参数化分布族（如偏态分布）刻画，其参数随时间和函数自变量平滑变化；联合依赖结构则通过高斯 copula 建模，协方差采用低秩近似以降低计算复杂度。该模型统一了点态分位数估计和新时间点完整轨迹预测两个任务。模拟研究验证了方法的有限样本表现，并应用于多发性硬化症患者的弥散张量成像研究。方法已实现为 R 包 sLFDA 并公开。对于您而言，本文属于应用统计方法开发，与您的主要兴趣方向（因果推断、高维统计等）无直接技术交集，但 copula 建模思路和低秩协方差近似在纵向数据或函数型数据分析中可能具有参考价值。
- **关键技术**: `copula modeling`, `low-rank covariance approximation`, `longitudinal functional data analysis`, `pointwise quantile estimation`, `skewed distribution modeling`
- **为什么对您有用**: 本文属于纵向函数型数据分析的应用方法，与您的主要兴趣方向（因果推断、高维统计、U-统计量等）无直接技术重叠。武器库中非参数统计和软件开发的技能可帮助理解其方法框架，但核心问题（偏斜函数型数据建模）并非您当前研究重点。本文可作为方法学参考，但不值得投入全文阅读时间。

### 14. [10.1093/biomtc/ujae141](https://doi.org/10.1093/biomtc/ujae141) · [arXiv](https://arxiv.org/abs/2405.08180) — An adaptive enrichment design using Bayesian model averaging for selection and threshold-identification of predictive variables
- **作者**: Lara Maleyeff, Shirin Golchi, Erica E M Moodie, Marie Hudson
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对精准医学中生物标志物驱动的适应性富集设计，提出一种贝叶斯模型平均方法，用于从多个候选预测变量中识别连续生物标志物的阈值并定义治疗敏感亚组。模型采用自由结点B样条灵活刻画连续生物标志物与治疗效果的复杂非线性关系，并通过贝叶斯模型平均对所有可能的变量组合进行边际化，从而估计关键参数。在中期分析中，设计可评估生物标志物定义亚组的疗效增强或减弱，支持因有效性或无效性提前终止试验，并限制后续入组至治疗敏感患者。通过模拟研究，作者展示了该设计的操作特征，并与现有方法进行了比较。该论文主要贡献在临床试验设计领域，方法学上属于贝叶斯非参数建模与适应性设计的结合，但未涉及因果推断、高维统计或效率理论等您的主要兴趣方向。
- **关键技术**: `Bayesian model averaging`, `free-knot B-splines`, `adaptive enrichment design`, `biomarker threshold identification`
- **为什么对您有用**: 本文属于临床试验设计方法，与您的主要兴趣（因果推断、高维统计、半参效率理论）无直接交集，且未涉及您武器库中的具体工具（如U统计量、最小最大界、影响函数等）。作为流行病学应用方向的gateway阅读，它展示了贝叶斯适应性设计在生物标志物识别中的实际流程，但方法学深度有限，不值得投入全文时间。

### 15. [10.1093/biomtc/ujae131](https://doi.org/10.1093/biomtc/ujae131) · [arXiv](https://arxiv.org/abs/2307.02781) — Dynamic factor analysis with dependent Gaussian processes for high-dimensional gene expression trajectories
- **作者**: Jiachen Cai, Robert J B Goudie, Colin Starr, Brian D M Tom
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对高维纵向基因表达数据，提出一种贝叶斯动态因子分析模型，将高维基因表达轨迹映射到低维通路表达轨迹。核心创新在于通过依赖高斯过程（DGP）放松传统因子分析中因子间独立的假设，允许不同生物通路之间存在相关性。模型采用贝叶斯稀疏因子分析实现降维，并用DGP刻画低维轨迹的时序依赖与互相关。参数估计采用蒙特卡洛期望最大化（MCEM）算法，结合标准MCMC采样器和R包GPFDA，模块化设计便于推广。模拟和真实数据分析表明，该方法在恢复通路轨迹形状、揭示基因-通路关系及预测基因表达方面优于独立因子模型。R包DGP4LCF已发布在CRAN。本文属于应用统计方法论文，方法学新颖性有限（依赖高斯过程与因子分析的组合），对您的主攻方向（因果推断、高维统计、U-统计量）无直接技术连接。
- **关键技术**: `dependent Gaussian processes`, `Bayesian sparse factor analysis`, `Monte Carlo expectation maximization`, `Markov Chain Monte Carlo`
- **为什么对您有用**: 本文属于纵向高维数据建模的应用工作，与您的主攻方向（因果推断、高维RMT、U-统计量）无直接技术连接。武器库中very_familiar的非参数统计和软件工具可理解其贝叶斯框架，但核心问题（通路轨迹恢复）不涉及您关注的identification、minimax界或计算-统计权衡。作为gateway reading价值低：生物统计应用性强，但未提供可迁移的统计方法论洞见。暂不可做——缺乏与您技术栈的接口。

### 16. [10.1093/biomtc/ujae116](https://doi.org/10.1093/biomtc/ujae116) · [arXiv](https://arxiv.org/abs/2306.03663) — Bayesian inference for group-level cortical surface image-on-scalar regression with Gaussian process priors
- **作者**: Andrew S Whiteman, Timothy D Johnson, Jian Kang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对群体级神经影像回归分析中，传统逐像素边际广义线性模型（vertex-wise GLM）空间正则化不足、推断校准差的问题，提出了一种贝叶斯空间回归模型。模型对空间变化的回归系数函数施加高斯过程（GP）先验以实现正则化，并结合简单的非平稳误差过程，使平滑度比标准预处理方法更具数据自适应性。为克服全脑数十万位置带来的计算瓶颈，作者采用 Vecchia 型近似来保持 GP 先验的全空间秩，且该近似适用于一大类空间相关函数。方法在皮质表面 fMRI 任务对比数据（来自青少年脑认知发展研究的大队列）上进行了验证，并与逐顶点分析和若干替代方法比较。本文主要贡献在于计算可扩展的贝叶斯空间建模框架，而非统计方法学上的根本性创新。对您而言，该文属于应用统计计算，与您的主要兴趣方向（因果推断、高维统计等）无直接交集，但若您未来涉足神经影像数据分析，其 GP 近似策略（Vecchia 近似）可作为计算工具参考。
- **关键技术**: `Gaussian process priors`, `Vecchia approximation`, `spatial regression`, `Bayesian hierarchical model`, `cortical surface analysis`
- **为什么对您有用**: 本文属于应用统计计算，与您的主要兴趣（因果推断、高维随机矩阵、U-统计量等）无直接交集。其 Vecchia 型 GP 近似是一种计算技巧，但不在您的技术武器库核心范围内。作为 gateway reading 价值有限——神经影像领域的数据结构（皮质表面网格）和科学问题（任务激活定位）与您关注的统计推断问题差异较大。暂不可做：核心机器（空间 GP 建模与神经影像预处理流程）不在武器库中。

### 17. [10.1093/biomtc/ujae105](https://doi.org/10.1093/biomtc/ujae105) — ROMI: a randomized two-stage basket trial design to optimize doses for multiple indications
- **作者**: Shuqi Wang, Peter F Thall, Kentaro Takeda, Ying Yuan
- **期刊/来源**: Biometrics
- **机构**: The University of Texas MD Anderson Cancer Center · Astellas Pharma (United States)
- **分类**: vol 80 · issue 4
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文提出一种随机化两阶段篮式试验设计（ROMI），用于在多个适应症中优化剂量选择。第一阶段，每个适应症评估高剂量的疗效和毒性，并设置停止规则；未终止的适应症进入第二阶段，患者随机分配至高剂量或指定低剂量。采用潜在聚类贝叶斯层次模型在不同适应症间借用信息，同时允许适应症间最优生物剂量（OBD）存在异质性。使用适应症特异性效用函数量化疗效-毒性权衡，最终选择后验均值效用最高的剂量作为OBD。提供了两种版本：仅用第二阶段数据优化剂量，或合并两阶段数据优化。模拟显示，与忽略适应症或独立优化剂量的设计相比，ROMI具有更优的操作特征。该工作属于临床试验设计领域，与您的主要兴趣（因果推断、高维统计等）无直接技术重叠，但贝叶斯层次模型和剂量优化框架对您可能作为方法学参考。
- **关键技术**: `Bayesian hierarchical model`, `latent cluster model`, `basket trial design`, `dose optimization`, `utility-based decision`
- **为什么对您有用**: 本文属于临床试验设计，与您的主要兴趣（因果推断、高维统计、U统计量等）无直接技术重叠。但贝叶斯层次模型中的信息借用策略和两阶段自适应设计思路，对您关注的纵向因果推断或中介分析中的多组学数据整合可能有间接启发。作为方法学参考，可读性较高，但核心工具（贝叶斯层次模型、效用函数）不在您的技术武器库中，属于暂不可做方向。

### 18. [10.1093/biomtc/ujae124](https://doi.org/10.1093/biomtc/ujae124) — Clustering computer mouse tracking data with informed hierarchical shrinkage partition priors
- **作者**: Ziyi Song, Weining Shen, Marina Vannucci, Alexandria Baldizon, Paul M Cinciripini, Francesco Versace et al.
- **期刊/来源**: Biometrics
- **机构**: University of California, Irvine · Rice University · The University of Texas MD Anderson Cancer Center · University of California, Los Angeles
- **分类**: vol 80 · issue 4
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对计算机鼠标追踪数据，提出了一种新的分层收缩划分先验（HSP）用于聚类分析。HSP模型将受试者聚类定义为在实验条件下产生更相似（而非完全相同）嵌套分组的受试者集合，区别于传统双聚类方法要求条件分组完全相同。模型能够整合受试者或条件分组的先验信息，并允许受试者组内条件分组的偏差。通过模拟研究和一项初步研究的鼠标追踪数据，展示了该方法在揭示不同受试者群体行为模式方面的有效性和探索性能力。该方法属于贝叶斯非参数聚类范畴，但未涉及因果推断、高维统计或半参效率理论等您的主要兴趣方向。
- **关键技术**: `hierarchical shrinkage partition prior`, `Bayesian nonparametric clustering`, `nested partitions`, `bi-clustering`, `mouse-tracking data`
- **为什么对您有用**: 本文属于应用统计方法开发，与您的主要兴趣（因果推断、高维统计、半参理论）无直接交集。虽然贝叶斯非参数聚类可能对您次要兴趣中的流行病学数据分析有间接参考价值，但方法本身不涉及您技术武库中的核心工具（如U统计量、影响函数、极小极大界）。作为gateway reading价值有限，因为其统计设定（聚类嵌套分区）与您熟悉的问题结构差异较大。建议仅作浏览，不投入深度阅读。

### 19. [10.1093/biomtc/ujae146](https://doi.org/10.1093/biomtc/ujae146) — Unlocking the power of multi-institutional data: Integrating and harmonizing genomic data across institutions
- **作者**: Yuan Chen, Ronglai Shen, Xiwen Feng, Katherine Panageas
- **期刊/来源**: Biometrics
- **机构**: Memorial Sloan Kettering Cancer Center · University of Michigan
- **分类**: vol 80 · issue 4
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对多机构基因组数据整合中的实际挑战，提出Bridge模型。核心问题是：不同机构使用不同基因测序面板（gene panels）导致数据异质性，且基因突变模式高维稀疏、信号弱。Bridge模型采用分位数匹配的潜变量方法（quantile-matched latent variable approach），从所有可用基因数据中提取低维、降噪的整合特征，而非仅分析公共基因子集。该方法通过信息共享提升学习效率和泛化能力，捕获个体独特的真实突变模式。模拟研究验证了模型性能与参数估计的可靠性。在GENIE BPC真实数据中，提取的潜变量特征在六种癌症类型的患者生存预测中表现优异。本文是应用导向的方法学工作，但方法本身（潜变量整合、分位数匹配）与您的主要兴趣方向（因果推断、高维统计）无直接技术交集，且未涉及您武器库中的核心工具（如U统计量、半参效率理论）。
- **关键技术**: `quantile-matched latent variable`, `data harmonization`, `multi-institutional data integration`, `low-dimensional feature extraction`
- **为什么对您有用**: 本文属于流行病学/基因组学应用，但方法学贡献有限（潜变量模型+分位数匹配），未使用您熟悉的因果推断、高维统计或U统计量工具。作为流行病学应用，它展示了真实数据整合的挑战，但分析模式（生存预测）与您的核心兴趣（因果识别、效率理论）距离较远。暂不可做：核心机器（因果推断、半参效率、U统计量）在此问题中无直接切入点。

### 20. [10.1093/biomtc/ujae158](https://doi.org/10.1093/biomtc/ujae158) — Structured feature ranking for genomic marker identification accommodating multiple types of networks
- **作者**: Yeheng Ge, Tao Li, Xingdong Feng, Mengyun Wu, Hailong Liu
- **期刊/来源**: Biometrics
- **机构**: Shanghai University of Finance and Economics · Shanghai Jiao Tong University · XinHua Hospital
- **分类**: vol 80 · issue 4
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文提出一种结构化特征排序方法，用于基因组标记识别，核心创新在于通过拉普拉斯正则化有效整合预测变量间的网络结构（包括先验已知网络和数据驱动估计网络）。该方法在边际排序框架下引入网络结构，通过控制网络噪声与不确定性（调参选择）提升排序稳定性。理论部分证明了所提网络结构化度量在温和条件下比原始边际度量具有更快的收敛速度，并满足 sure screening 性质。模拟与 TCGA 黑色素瘤数据分析展示了有限样本性能的提升。该方法本质上是一种带网络约束的边际筛选工具，未涉及因果推断或半参数效率理论。
- **关键技术**: `Laplacian regularization`, `sure screening property`, `network-constrained feature ranking`, `tuning parameter selection`
- **为什么对您有用**: 本文属于生物统计应用，与您的主要兴趣（因果推断、高维统计、半参理论）无直接交集。其网络正则化思路虽可迁移至因果推断中的变量选择（如 IV 筛选），但方法学深度有限，且未涉及您武器库中的核心工具（如 U-statistic、efficiency bound）。作为流行病学应用，本文数据侧（TCGA 黑色素瘤）和模型侧（网络结构整合）的阐述对入门者有一定参考价值，但整体 novelty 较低，暂不建议深入阅读。

### 21. [10.1093/biomtc/ujae114](https://doi.org/10.1093/biomtc/ujae114) — Changepoint detection on daily home activity pattern: a sliced Poisson process method
- **作者**: Israel Martínez-Hernández, Rebecca Killick
- **期刊/来源**: Biometrics
- **机构**: Lancaster University
- **分类**: vol 80 · issue 4
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文研究居家活动模式中的变点检测问题，目标是从每日事件时间序列中检测跨天的行为模式变化，而非日内周期性变化。将每日事件时间视为一个非齐次 Poisson 过程的实现，其强度函数随一天内时间变化，从而将问题转化为检测一系列非齐次 Poisson 过程的变点。方法上，提出了一种基于切片 Poisson 过程的方法，利用局部变化信息来检测跨天变化，并允许可视化和解释结果。模拟实验评估了方法的性能。该方法适用于居家活动数据等具有日内周期性的现象。对您而言，本文属于应用统计方法，与您的主要兴趣（如因果推断、高维统计）无直接关联，但变点检测与假设检验有概念联系，且 Poisson 过程模型在流行病学中有应用。
- **关键技术**: `inhomogeneous Poisson process`, `changepoint detection`, `slice Poisson process`, `local change information`
- **为什么对您有用**: 本文属于应用统计方法，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接技术重叠。变点检测与假设检验有概念联系，但方法本身不涉及您武器库中的核心工具（如非参数统计、minimax 界、高阶 U-统计量）。作为流行病学或健康监测领域的应用，可作入门了解，但暂不可做——核心机器（Poisson 过程变点检测）不在您的武器库中，且方法学新颖性有限。

### 22. [10.1093/biomtc/ujae134](https://doi.org/10.1093/biomtc/ujae134) — An exploratory penalized regression to identify combined effects of temporal variables—application to agri-environmental issues
- **作者**: Bénedicte Fontez, Patrice Loisel, Thierry Simonneau, Nadine Hilgert
- **期刊/来源**: Biometrics
- **机构**: Université de Montpellier · Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement · Mathématiques, Informatique et Statistique pour l'Environnement et l'Agronomie · Institut Agro Montpelier · L'Institut Agro · Laboratoire d'Ecophysiologie des Plantes sous Stress environnementaux
- **分类**: vol 80 · issue 4
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文提出一种名为 SpiceFP 的稀疏结构化回归方法，用于识别两个时间变量对单个标量输出的联合影响。方法将两个时间变量离散化为分类变量，定义联合模态，然后基于联合区间频率构建多重回归模型。通过广义融合套索（generalized fused lasso）同时确定分类区间和回归系数，实现变量选择和结构正则化。模拟研究表明该方法能灵活识别非零或影响显著的模态。葡萄品质的实例分析展示了其应用价值。该方法属于探索性分析工具，侧重可解释性而非因果推断或效率理论。
- **关键技术**: `generalized fused lasso`, `sparse regression`, `categorical variable transformation`, `joint modality`, `exploratory analysis`
- **为什么对您有用**: 本文与您的主要兴趣（因果推断、高维统计、半参理论）关联较弱，属于应用导向的统计方法开发。方法学上未涉及您熟悉的非参极小极大界、U-统计量或效率理论。作为农业环境领域的应用，其数据结构和分析模式对您的流行病学或经济学应用兴趣有一定参考价值，但方法论贡献有限。暂不可做：核心机器（融合套索、分类变量建模）不在您的武器库中，且与您当前的研究方向距离较远。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

