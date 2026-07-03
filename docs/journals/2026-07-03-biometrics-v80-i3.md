# Biometrics — Vol 80  Issue 3  ·  2026-07-03

- 共 39 篇 · Biometrics
- 目录核对 ⚠️ 疑似漏 2 篇（对照 OpenAlex 45 篇）：10.1093/biomtc/ujae077、10.1093/biomtc/ujae102

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Biometrics》第80卷第3辑的39篇论文，整体上围绕**因果推断中的识别与稳健性**、**高维与汇总统计推断**、以及**生存分析与流行病学设计**三条主线展开。因果推断方向论文最多，集中探讨了在比例风险模型、纵向数据、中介分析等场景下，双重稳健性、多重稳健性及贝叶斯非参数方法的适用边界与替代方案。高维与汇总统计方向则聚焦于knockoff框架下的FDR/FWER控制、迁移学习中的异质性处理，以及利用外部汇总信息提升估计效率。此外，生存分析与流行病学设计方向涵盖了区间删失、竞争风险、筛查试验设计及新型数据源（如废水监测）的建模。

在因果推断主线中，**“Propensity weighting plus adjustment in proportional hazards model is not doubly robust”** 通过理论和模拟揭示了比例风险模型中倾向性评分加权与回归调整组合在非零效应下不满足双重稳健性的根本冲突，并提出了针对生存差异和完整生存曲线的双重稳健替代估计量。**“Multiply robust estimation of marginal structural models in observational studies subject to covariate-driven observations”** 针对协变量驱动的不规则观测时间，提出了仅需至少一个权重模型正确的多重稳健估计量，放松了传统方法的模型假设。**“A Bayesian nonparametric approach for causal mediation with a post-treatment confounder”** 则利用 enriched Dirichlet process mixture 处理治疗后混杂，扩展了中介分析的识别条件。这三篇从不同角度挑战或完善了因果推断中的稳健性理论，值得关注。

在高维与汇总统计方向，**“Summary statistics knockoffs inference with family-wise error rate control”** 将GhostKnockoff框架扩展到仅依赖汇总统计量的场景，并实现了FWER控制，计算效率显著提升。**“Heterogeneous latent transfer learning in Gaussian graphical models”** 通过同时识别样本亚群结构，解决了迁移学习中源与目标异质性导致的负迁移问题。**“Integrating external summary information in the presence of prior probability shift”** 则针对先验概率漂移，提出半参数约束优化方法整合外部汇总信息，无需外部方差估计。这些工作在高维推断和外部数据整合方面提供了新的技术路径。

与因果推断方向最贴合的论文包括：**“Propensity weighting plus adjustment in proportional hazards model is not doubly robust”**（双重稳健性理论）、**“Multiply robust estimation of marginal structural models”**（纵向因果推断）、**“A Bayesian nonparametric approach for causal mediation”**（中介分析）、**“Causal inference using multivariate generalized linear mixed-effects models”**（动态治疗方案）、**“Causal meta-analysis by integrating multiple observational studies”**（元分析）。与半参数/非参数方向相关的有：**“Nonparametric second-order estimation for spatiotemporal point patterns”**（核平滑渐近理论）、**“Semi-parametric benchmark dose analysis with monotone additive models”**（单调约束半参数推断）。高维方向可优先看：**“Summary statistics knockoffs inference with family-wise error rate control”**（汇总统计量FWER控制）、**“Heterogeneous latent transfer learning in Gaussian graphical models”**（异质性迁移学习）。

## 因果推断  *(causal_inference, 17 篇)*

### 1. [10.1093/biomtc/ujae069](https://doi.org/10.1093/biomtc/ujae069) · [arXiv](https://arxiv.org/abs/2310.16207) — Propensity weighting plus adjustment in proportional hazards model is not doubly robust
- **作者**: Erin E Gabriel, Michael C Sachs, Ingeborg Waernbaum, Els Goetghebeur, Paul F Blanche, Stijn Vansteelandt et al.
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 本文研究在比例风险模型（Cox、Weibull、flexible parametric）中，将倾向性评分加权与回归调整结合是否能得到双重稳健估计量。作者通过模拟和理论证明指出，当暴露存在因果效应时，这种组合通常不满足双重稳健性——即只有当倾向性评分模型或结局模型之一正确且包含所有混杂时，估计量才在零假设（无因果效应）下一致，而在非零效应下则不然。证明基于部分似然和全似然的渐近性质，揭示了比例风险模型与双重稳健性之间的根本冲突。作为替代，作者提出了两个在给定时间点对生存差异双重稳健的简单估计量，以及一个对完整生存曲线双重稳健的估计方法，前提是删失机制可正确建模。这些替代估计量基于逆概率删失加权和回归标准化，并提供了R代码。对您而言，本文直接关联因果推断中的双重稳健估计理论，尤其适用于流行病学队列研究中生存结局的效应估计，提醒您在应用Cox模型+倾向性评分加权时需警惕其非双重稳健性。
- **关键技术**: `doubly robust estimation`, `propensity score weighting`, `proportional hazards model`, `partial likelihood`, `inverse probability of censoring weighting`, `regression standardization`
- **为什么对您有用**: 本文直接关联您primary interest中的因果推断（identification & estimation）和流行病学应用。它揭示了比例风险模型下倾向性评分加权+回归调整并非双重稳健这一反直觉事实，对您使用或评估此类方法有直接警示作用。从技术武器库看，您对非参数统计和因果推断估计理论非常熟悉，可以立即动手复现其模拟并检验替代估计量在您关注的纵向数据或高维协变量下的表现（立即可做）。

### 2. [10.1093/biomtc/ujae067](https://doi.org/10.1093/biomtc/ujae067) · [arXiv](https://arxiv.org/abs/2306.16068) — Joint structure learning and causal effect estimation for categorical graphical models
- **作者**: Federico Castelletti, Guido Consonni, Marco L Della Vedova
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文针对分类变量系统，研究在外部干预一个变量后对结果变量的因果效应估计问题。设定中变量间通过有向无环图（DAG）表示依赖结构，效应沿多条路径传播。方法的核心是联合学习DAG结构与因果效应，同时考虑结构和参数的不确定性。作者提出了一种基于可逆跳转（reversible-jump）提议方案的马尔可夫链蒙特卡洛（MCMC）算法，对DAG和参数的后验分布进行联合采样。模拟研究表明该方法在估计精度上优于现有主流方法。最后，论文将方法应用于大学生抑郁与焦虑数据集。对您而言，本文属于因果推断中结构学习与效应估计的贝叶斯方法，与您的因果推断（特别是纵向/中介设定）和统计计算兴趣相关，但方法学新颖性有限，主要是贝叶斯MCMC在分类变量DAG上的应用。
- **关键技术**: `Bayesian structure learning`, `reversible-jump MCMC`, `directed acyclic graph (DAG)`, `causal effect estimation`, `categorical graphical models`
- **为什么对您有用**: 本文连接您的因果推断兴趣，特别是结构学习与效应估计的联合贝叶斯方法。技术武器库中'identification theory in causal inference'和'M-estimation theory'可用来分析其贝叶斯后验的渐近性质或与频率学派方法的比较。中期可做：需先在moderately_familiar的semiparametric theory上长肌肉，以理解其贝叶斯方法与半参数效率界限的关系。

### 3. [10.1093/biomtc/ujae065](https://doi.org/10.1093/biomtc/ujae065) — Multiply robust estimation of marginal structural models in observational studies subject to covariate-driven observations
- **作者**: Janie Coulombe, Shu Yang
- **期刊/来源**: Biometrics
- **机构**: Université de Montréal · North Carolina State University
- **分类**: vol 80 · issue 3
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对电子健康记录等观察性数据中，因协变量驱动的不规则观测时间导致的因果推断问题，提出了一种新的多重稳健估计量。目标是在存在时变混杂和协变量驱动观测机制下，估计边际结构模型（MSM）中的因果效应。现有方法依赖两个权重模型（观测时间权重和治疗权重）的正确设定，而本文提出的估计量仅需至少一个模型正确即可保证一致性，从而放松了模型假设。该估计量基于加权和回归的框架，通过结合多个逆概率权重和结果回归模型，实现了多重稳健性。理论分析和模拟研究表明，该估计量比现有替代方法更灵活、更高效。应用于美国Add Health研究数据，估计了心理咨询对青少年饮酒量的因果效应。该方法对您在纵向因果推断和识别理论方面的兴趣有直接参考价值，特别是处理不规则观测时间这一实际挑战。
- **关键技术**: `multiply robust estimation`, `marginal structural models`, `inverse probability weighting`, `covariate-driven observation times`, `doubly robust estimation`
- **为什么对您有用**: 本文直接关联您的primary interest中的纵向因果推断（longitudinal causal inference），特别是协变量驱动观测时间这一实际难题。您武器库中的非参数统计和因果推断估计理论（very_familiar）可直接用于理解其多重稳健性机制，而识别理论（moderately_familiar）可用于评估其假设的合理性。中期可做：若您希望在纵向设定下开发更高效的估计量，需先加强半参数理论（moderately_familiar）中的影响函数工具。

### 4. [10.1093/biomtc/ujae099](https://doi.org/10.1093/biomtc/ujae099) — A Bayesian nonparametric approach for causal mediation with a post-treatment confounder
- **作者**: Woojung Bae, Michael J Daniels, Michael G Perri
- **期刊/来源**: Biometrics
- **机构**: University of Florida · University of Florida Health
- **分类**: vol 80 · issue 3
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文提出一种贝叶斯非参数方法，用于在存在治疗后混杂变量（post-treatment confounder）时估计因果中介效应（NDE 和 NIE）。研究动机来自 Rural LITE 试验，其中治疗后混杂的存在使得标准中介分析失效。作者采用 enriched Dirichlet process mixture (EDPM) 对观测数据（结局、中介、治疗后混杂、处理、基线混杂）的联合分布进行建模。为识别因果效应，使用了 Hong 等人提出的扩展序贯可忽略性（sequential ignorability）假设，并辅以 Gaussian copula 模型假设。该方法通过数据增广处理缺失数据，并允许对混杂变量的子集计算 NIE 和 NDE。模拟研究评估了方法性能，并在 Rural LITE 数据中应用，发现潜在中介的证据不强。对您而言，本文展示了在复杂纵向设定下（治疗后混杂）如何结合贝叶斯非参数与因果识别假设，与您 causal inference 方向中的 mediation 和 longitudinal 子方向直接相关。
- **关键技术**: `enriched Dirichlet process mixture`, `Gaussian copula`, `sequential ignorability`, `Bayesian nonparametrics`, `data augmentation`
- **为什么对您有用**: 本文直接连接您的 primary interest 中 causal inference 的 mediation 和 longitudinal 子方向，特别是治疗后混杂这一实际难题。您的 technical arsenal 中 very_familiar 的 nonparametric statistics 和 estimation theory in causal inference 可用于评估其 EDPM 建模的灵活性及识别假设的合理性。中期可做：若想将本文的贝叶斯非参数思路与您的 semiparametric theory 结合（如推导更紧的效率界），需先在 moderately_familiar 的 semiparametric theory 上加强。

### 5. [10.1093/biomtc/ujae100](https://doi.org/10.1093/biomtc/ujae100) · [arXiv](https://arxiv.org/abs/2303.02201) — Causal inference using multivariate generalized linear mixed-effects models
- **作者**: Yizhen Xu, Ji Soo Kim, Laura K Hummers, Ami A Shah, Scott L Zeger
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文针对精准医学中动态治疗方案的因果效应预测问题，提出了一种多变量广义线性混合效应模型（MGLMM）与贝叶斯g-computation算法。在观测研究中，治疗分配和效应的实际机制未知，作者通过将未测时不变因素作为受试者随机效应纳入结果、时变混杂和治疗分配的联合分布中，识别了条件于治疗分配异质性的序贯可忽略性假设，这类似于平衡因未测时不变因素导致的潜在治疗偏好。方法的核心是贝叶斯g-computation，用于计算动态治疗方案的亚组特异性干预效益的后验分布。模拟研究评估了方法的性能，并应用于硬皮病患者持续使用霉酚酸盐的观察性临床数据。该工作对您可能有用：它连接了您的主要兴趣——因果推断中的纵向数据与动态治疗，且其贝叶斯g-computation框架与您熟悉的非参数统计和因果推断估计理论有交叉，但方法学新颖性有限，属于应用扩展。
- **关键技术**: `Bayesian g-computation`, `multivariate generalized linear mixed-effects model`, `sequential ignorability`, `dynamic treatment regimes`, `random effects for unmeasured confounding`
- **为什么对您有用**: 本文直接关联您的主要兴趣——因果推断中的纵向数据与动态治疗方案。其贝叶斯g-computation框架与您熟悉的非参数统计和因果推断估计理论有交叉，但方法学新颖性有限，属于应用扩展。从武器库看，您可以用'very_familiar'中的'nonparametric statistics'和'estimation theory in causal inference'来理解其模型假设和估计策略，但核心的贝叶斯计算和混合效应模型并非您的核心工具，因此属于'中期可做'——需先在'moderately_familiar'的'identification theory in causal inference'上进一步熟悉纵向因果推断的识别条件。

### 6. [10.1093/biomtc/ujae094](https://doi.org/10.1093/biomtc/ujae094) · [arXiv](https://arxiv.org/abs/2302.01269) — Adjusting for incomplete baseline covariates in randomized controlled trials: a cross-world imputation framework
- **作者**: Yilin Song, James P Hughes, Ting Ye
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 本文针对随机对照试验中基线协变量缺失的问题，提出一个名为“跨世界插补”（CWI）的统一理论框架。该框架将单值插补法和缺失指示变量法（MIM）作为特例纳入，从而在统一视角下比较两种方法的效率。通过CWI框架，作者证明MIM隐式地搜索了最优的CWI值，因此能够达到最优效率。同时，推导了单值插补法通过搜索最优插补值可以达到与MIM相同效率的条件。理论结果通过模拟研究和儿童腺样体扁桃体切除术试验的真实数据分析得到验证。该工作为处理缺失协变量提供了理论指导，对您关注的因果推断中纵向数据或随机试验的估计效率问题有直接参考价值。
- **关键技术**: `cross-world imputation`, `missingness-indicator method`, `efficiency comparison`, `single imputation`
- **为什么对您有用**: 本文直接关联您primary interest中的因果推断（随机对照试验中的协变量调整与效率提升），且其效率比较框架与您熟悉的非参数统计和估计理论高度契合。您可以用very_familiar的minimax bound工具来验证其声称的最优效率是否紧，或进一步探索在更复杂缺失机制下的推广。中期可做：若想将CWI框架扩展到proximal causal inference中的负对照设定，需先在moderately_familiar的identification theory上加强。

### 7. [10.1093/biomtc/ujae103](https://doi.org/10.1093/biomtc/ujae103) — Leveraging independence in high-dimensional mixed linear regression
- **作者**: Ning Wang, Kai Deng, Qing Mai, Xin Zhang
- **期刊/来源**: Biometrics
- **机构**: Beijing Normal University · Florida State University
- **分类**: vol 80 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究高维混合线性回归中的系数估计与变量选择问题，设定中预测变量数远大于样本量。现有方法通常将预测变量视为固定或忽略其内在变异性，作者利用预测变量与混合潜在指示变量之间的独立性，提出一种快速组惩罚EM估计器。该方法通过独立性假设实现计算效率的提升，并在所有混合成分间进行协同变量选择。作者建立了所提估计器到真实回归参数的非渐近收敛速率。模拟实验和癌症细胞系百科全书（CCLE）数据集的抗癌药物敏感性预测应用验证了方法的有效性。对您而言，该工作在高维设定下利用独立性假设进行变量选择与估计的思路，可迁移至因果推断中高维混杂调整或工具变量选择问题。
- **关键技术**: `group-penalized EM`, `non-asymptotic convergence rate`, `independence between predictor and latent variable`, `high-dimensional mixed linear regression`, `variable selection`
- **为什么对您有用**: 本文连接您的高维统计与因果推断兴趣：高维混合回归中的变量选择与估计问题，其利用预测变量与潜在变量独立性的技巧，可类比于因果推断中工具变量或负对照变量的独立性假设。您的技术武器库中'高维渐近理论'和'因果推断中的估计理论'可直接用于分析该方法的有限样本性质或将其推广至因果参数估计。中期可做：需先在 moderately_familiar 的'识别理论'上理解独立性假设在因果图下的具体含义，再考虑迁移。

### 8. [10.1093/biomtc/ujae073](https://doi.org/10.1093/biomtc/ujae073) — A generalized outcome-adaptive sequential multiple assignment randomized trial design
- **作者**: Xue Yang, Yu Cheng, Peter F Thall, Abdus S Wahed
- **期刊/来源**: Biometrics
- **机构**: University of Pittsburgh · The University of Texas MD Anderson Cancer Center · University of Rochester
- **分类**: vol 80 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对动态治疗策略（DTR）的序贯随机试验设计，提出广义结局自适应序贯多分配随机试验（GO-SMART）设计。传统SMART设计在每一阶段以固定概率随机分配治疗，忽略了既往患者结局信息，可能导致新患者被分配至劣效治疗，降低依从性。GO-SMART根据既往患者的结局数据，自适应地调整各阶段的随机化概率，使更多患者接受更优的治疗序列。为校正结局自适应随机化引入的选择偏倚，作者提出了G估计量和逆概率加权估计量，并证明了它们的一致性。模拟结果显示，与标准SMART、响应自适应SMART等设计相比，GO-SMART能使更多患者接受最优DTR，并提高总响应数，同时保持相似或更优的统计检验效能。该设计直接服务于因果推断中的序贯治疗策略评估，其自适应随机化机制与您关注的纵向因果推断和IV方法中的工具变量选择有潜在联系。
- **关键技术**: `G-estimation`, `inverse probability weighting`, `sequential multiple assignment randomized trial`, `outcome-adaptive randomization`, `dynamic treatment regime`
- **为什么对您有用**: 本文属于因果推断中纵向数据与序贯决策的交叉方向，直接对应您primary interest中的'longitudinal'和'causal inference'子方向。您武器库中'very_familiar'的'estimation theory in causal inference'可直接用于分析其G估计量的渐近性质，而'moderately_familiar'的'identification theory in causal inference'可用于评估其自适应随机化下的识别假设是否可放松。**中期可做**：需先在'moderately_familiar'的'identification theory in causal inference'上深入，以处理自适应随机化带来的时变混杂问题。

### 9. [10.1093/biomtc/ujae070](https://doi.org/10.1093/biomtc/ujae070) · [arXiv](https://arxiv.org/abs/2306.16715) — Causal meta-analysis by integrating multiple observational studies with multivariate outcomes
- **作者**: Subharup Guha, Yi Li
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对整合多个观察性研究进行因果元分析的问题，目标是在自然总体中比较多个组的潜在结果。研究设定中，各回顾性队列是便利样本，通常不能代表目标总体，且组间协变量分布不平衡。作者提出一个基于伪总体的协变量平衡框架，将经典的加权方法（如逆概率加权）扩展到多个队列、多个组的元分析场景。核心方法是 FLEXOR（FLEXible, Optimized, and Realistic）加权法，通过最大化各队列的有效样本量来构造伪总体，从而得到更稳定和高效的权重。在此基础上，发展了针对定量、分类或多变量结局的加权估计量，用于无混杂推断，并证明了估计量的渐近性质。模拟和TCGA数据实例展示了方法的灵活性和可靠性。对于您关注的因果推断中纵向/多组设定下的加权方法，本文的FLEXOR框架在有效样本量优化和多元结局处理上提供了新思路。
- **关键技术**: `pseudo-population weighting`, `covariate balancing`, `effective sample size maximization`, `inverse probability weighting`, `meta-analysis of observational studies`
- **为什么对您有用**: 本文直接关联您 primary interest 中的因果推断（identification, estimation）和纵向/多组设定。FLEXOR 方法通过最大化有效样本量来优化权重，这一思路可以用您 very_familiar 的 minimax 估计理论来检验其最优性——例如，能否证明该权重在某种意义下达到半参数效率界？此外，多元结局的加权估计量可借助您 moderately_familiar 的 M-估计理论进行渐近分析。**中期可做**：需先在 moderately_familiar 的 semiparametric theory 上进一步熟悉，以严格推导该估计量的影响函数和效率界。

### 10. [10.1093/biomtc/ujae064](https://doi.org/10.1093/biomtc/ujae064) — Controlling false discovery rate for mediator selection in high-dimensional data
- **作者**: Ran Dai, Ruiyang Li, Seonjoo Lee, Ying Liu
- **期刊/来源**: Biometrics
- **机构**: University of Nebraska Medical Center · Columbia University
- **分类**: vol 80 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文在高维候选集（如神经影像、遗传数据）中提出一个多重假设检验框架，用于选择中介变量（mediator）并控制错误发现率（FDR）。方法将近年发展的基于 knockoff 的 FDR 控制变量选择扩展到中介选择场景，证明了有限样本下 FDR 控制的理论保证。核心机制是构造 knockoff 变量来模拟原始中介变量的分布，从而在保持 FDR 控制的同时实现变量选择。模拟实验表明该方法在统计功效和有限样本性能上优于现有方法。最后应用于 ABCD 研究，筛选出静息态功能磁共振连接标记作为不良童年事件与 NIH 工具箱结晶复合得分之间关系的中介。对您而言，本文连接了因果推断中的中介分析和高维统计中的 FDR 控制，且其 knockoff 框架与您熟悉的非参数统计和因果推断估计理论有潜在交叉，值得关注。
- **关键技术**: `knockoff filter`, `false discovery rate control`, `high-dimensional mediator selection`, `multiple hypothesis testing`
- **为什么对您有用**: 本文直接连接您 primary interest 中的因果推断（中介分析）和高维统计，且使用 knockoff 这一您 moderately_familiar 的识别理论工具。武器库中 'estimation theory in causal inference' 和 'high-dimensional asymptotics' 可用于分析其 FDR 控制的理论紧性。中期可做：若想将 knockoff 与您的 HOIF 或 higher-order U-statistics 结合，需先在 'identification theory in causal inference' 上加强。

### 11. [10.1093/biomtc/ujae072](https://doi.org/10.1093/biomtc/ujae072) — Improving prediction of linear regression models by integrating external information from heterogeneous populations: James–Stein estimators
- **作者**: Peisong Han, Haoyue Li, Sung Kyun Park, Bhramar Mukherjee, Jeremy M G Taylor
- **期刊/来源**: Biometrics
- **机构**: Gilead Sciences (United States) · University of Michigan
- **分类**: vol 80 · issue 3
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文研究如何整合来自异质性总体的外部模型摘要信息（仅含部分协变量的简化模型系数估计）来提升内部线性回归模型的预测精度。目标是在内部有个体级数据、外部仅有汇总统计量的设定下，通过James–Stein收缩方法构造新的估计量，使得整合后的预测均方误差不劣于、且通常优于仅用内部数据的模型。该方法不依赖于总体同质性假设，对异质性程度具有稳健性。模拟研究验证了所提估计量在不同异质性水平下的数值表现。实际应用中，作者将方法用于整合已发表文献中的摘要信息，以改善基于血铅水平和其他协变量预测髌骨骨铅水平的模型。对您而言，该工作属于流行病学应用中的预测模型整合问题，其核心思想（利用外部汇总信息进行收缩估计）与您熟悉的因果推断中数据融合（如proximal CI的negative control整合外部信息）有相通之处，可作为中期可做的迁移方向。
- **关键技术**: `James–Stein shrinkage`, `external summary information integration`, `linear regression prediction`, `heterogeneous populations`
- **为什么对您有用**: 本文属于流行病学应用（骨铅水平预测），直接对应secondary interest中的流行病学方向。其利用外部汇总统计量提升内部模型精度的思路，与您熟悉的因果推断中数据融合（如proximal CI利用negative control整合外部信息）有方法论上的可迁移性。中期可做：需先在moderately_familiar的identification theory上长肌肉，以将James–Stein收缩思想推广到因果效应的数据融合设定。

### 12. [10.1093/biomtc/ujae080](https://doi.org/10.1093/biomtc/ujae080) · [arXiv](https://arxiv.org/abs/2401.05124) — Nonparametric worst-case bounds for publication bias on the summary receiver operating characteristic curve
- **作者**: Yi Zhou, Ao Huang, Satoshi Hattori
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对诊断试验荟萃分析中SROC曲线受发表偏倚影响的问题，提出了一种非参数最坏情况界方法。现有方法依赖参数选择函数建模选择性发表机制，而本文在最小假设下采用非参数选择函数，推导SROC曲线的最坏情况界。估计过程通过蒙特卡洛方法近似SROC曲线上的偏倚及对应曲线下面积，然后利用非线性规划在边际选择概率范围内优化发表偏倚的最大最小值。该方法应用于真实荟萃分析，展示了SROC曲线最坏情况界对诊断试验准确性荟萃分析结果稳健性的讨论价值。对您而言，本文属于因果推断中敏感性分析的一个具体应用场景（发表偏倚），其非参数最坏情况界思路可与您熟悉的非参数统计和因果推断中的敏感性分析工具（如E-value）形成对比，但方法学新颖性有限（应用为主）。
- **关键技术**: `nonparametric selection functions`, `worst-case bounds`, `Monte Carlo approximation`, `nonlinear programming`, `sensitivity analysis`
- **为什么对您有用**: 本文属于因果推断中敏感性分析的应用，具体针对诊断试验荟萃分析的发表偏倚问题。您的武器库中'非参数统计'和'因果推断中的估计理论'可直接用于理解其非参数选择函数设定和最坏情况界推导，但方法学贡献偏应用，新颖性有限。中期可做：若想深入，需先在'moderately_familiar'的'因果推断中的识别理论'上加强，以评估其识别假设的合理性。

### 13. [10.1093/biomtc/ujae061](https://doi.org/10.1093/biomtc/ujae061) — Optimal refinement of strata to balance covariates
- **作者**: Katherine Brumberg, Dylan S Small, Paul R Rosenbaum
- **期刊/来源**: Biometrics
- **机构**: University of Michigan · University of the Sciences · University City Science Center · University of Pennsylvania · Philadelphia University
- **分类**: vol 80 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究在观察性研究中，如何通过最优划分（refinement）已有的倾向性评分层（strata）来平衡多个协变量。作者将“将一个层拆分为两个子层以最小化层内协变量不平衡”这一组合优化问题形式化为整数规划，并用线性规划松弛加随机舍入（randomized rounding）来近似求解。核心理论贡献是：当层内样本数远大于协变量数时，随机舍入的随机性很小，因此线性松弛解与随机舍入解分别构成不可达整数规划解的下界和上界，且这两个界往往很接近，从而验证了随机舍入解的质量。方法通过一个实际观察性研究（2016名患者，5735名对照）展示：用5个倾向性评分层细化成10个层，在保留全部患者的同时获得了极好的协变量平衡。该方法已实现为R包optrefine。对您而言，本文属于因果推断中匹配/分层平衡协变量的实用工具，其整数规划+随机舍入的近似策略可迁移到您熟悉的倾向性评分分层或匹配设计场景中。
- **关键技术**: `integer programming`, `linear programming relaxation`, `randomized rounding`, `propensity score stratification`, `covariate balance`
- **为什么对您有用**: 本文直接关联您的primary interest中的因果推断（匹配/分层平衡协变量），属于应用性较强的方法论文。您的武器库中“estimation theory in causal inference”和“software development”可直接用于理解其方法并尝试复现或扩展（例如将分层细化思路与您熟悉的proximal CI或IV设定结合）。**中期可做**：若想将此类组合优化方法推广到更复杂的因果结构（如工具变量分层），需先在moderately_familiar的“identification theory in causal inference”上加强，以明确目标函数（平衡什么协变量、对什么estimand最优）。

### 14. [10.1093/biomtc/ujae083](https://doi.org/10.1093/biomtc/ujae083) · [arXiv](https://arxiv.org/abs/2303.05223) — LEAP: the latent exchangeability prior for borrowing information from historical data
- **作者**: Ethan M Alt, Xiuya Chang, Xun Jiang, Qing Liu, May Mo, Hong Amy Xia et al.
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出潜在可交换性先验（LEAP），用于在贝叶斯框架下从历史数据中借力。目标是在当前试验的对照组中，仅借用与当前数据可交换的历史个体信息，而非对整个历史数据集进行统一折扣。LEAP 通过潜变量模型将历史观测分类为可交换与不可交换两组，并基于后验概率进行加权，从而实现对历史数据的选择性借用。与倾向得分方法不同，LEAP 直接针对结果参数的可交换性建模，而非仅依赖协变量分布。模拟和银屑病III期临床试验案例表明，LEAP 在控制偏差和提升精度方面优于 power prior、commensurate prior 等传统方法。该方法为因果推断中外部数据整合提供了一种新的识别策略，尤其适用于随机化不平衡或对照组样本量不足的场景。对您而言，该工作与您 causal inference 方向中 IV 和纵向设定下的数据整合问题有直接关联，其潜变量分类思路可启发 sensitivity analysis 中关于未测量混杂的建模。
- **关键技术**: `latent exchangeability prior`, `propensity score`, `power prior`, `commensurate prior`, `Bayesian hierarchical model`, `subgroup borrowing`
- **为什么对您有用**: 本文属于 causal inference 方向中外部数据整合的子问题，与您 primary interest 中的 IV 和纵向设定下的数据融合直接相关。您的 technical arsenal 中 'estimation theory in causal inference' 和 'identification theory in causal inference' 可直接用于分析 LEAP 的识别假设（如可交换性条件是否可检验）和估计效率（与 power prior 的方差对比）。中期可做：若想将 LEAP 扩展到高维协变量或非参数设定，需先在 moderately_familiar 的 'semiparametric theory' 上长肌肉，以处理潜变量分类的非参数识别。

### 15. [10.1093/biomtc/ujae090](https://doi.org/10.1093/biomtc/ujae090) — Integrating external summary information in the presence of prior probability shift: an application to assessing essential hypertension
- **作者**: Chixiang Chen, Peisong Han, Shuo Chen, Michelle Shardell, Jing Qin
- **期刊/来源**: Biometrics
- **机构**: University of Maryland, Baltimore · Foundation for the National Institutes of Health · Gilead Sciences (United States) · National Institute of Allergy and Infectious Diseases
- **分类**: vol 80 · issue 3
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究在存在先验概率漂移（prior probability shift）时，如何整合外部汇总信息（summary information）以提升内部研究的估计效率和预测精度。先验概率漂移指两个队列的数据分布差异由结局变量驱动，这在利用外部汇总信息时是一个关键挑战。作者提出了一种新的半参数约束优化方法，通过引入结局依赖的选择函数来刻画先验概率漂移，并处理外部汇总信息的估计不确定性。该方法无需外部源提供已知的方差-协方差估计即可进行有效推断。模拟研究表明，该方法在二元和连续结局下均优于现有方法，具有更小的估计偏差和方差。应用部分展示了该方法在评估原发性高血压风险因素中的实用性，整合外部汇总信息后估计变异性显著降低。对您而言，本文的约束优化框架和半参数推断思路可迁移至因果推断中的敏感性分析或数据融合问题，尤其是当外部信息存在异质性时，您熟悉的非参数统计和M估计理论可直接用于分析该方法的渐近性质。
- **关键技术**: `semiparametric constrained optimization`, `prior probability shift`, `outcome-dependent selection function`, `summary information integration`, `empirical likelihood`
- **为什么对您有用**: 本文直接关联您的主要兴趣——因果推断中的数据融合与异质性处理，特别是先验概率漂移这一设定在proximal causal inference或IV方法中也有类似挑战。您武器库中'非参数统计'和'M估计理论'可直接用于分析该约束优化估计量的渐近性质（如半参数效率界），属于'立即可做'的follow-up：可尝试将该框架扩展到存在未测量混杂时的因果效应估计。

### 16. [10.1093/biomtc/ujae092](https://doi.org/10.1093/biomtc/ujae092) · [arXiv](https://arxiv.org/abs/2404.06837) — Sensitivity analysis for publication bias in meta-analysis of sparse data based on exact likelihood
- **作者**: Taojun Hu, Yi Zhou, Satoshi Hattori
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对稀疏数据（低事件率二分类或计数结局）的meta分析中发表偏倚的敏感性分析问题。传统正态-正态随机效应模型在稀疏数据下因正态近似不准确而导致推断偏差，广义线性混合模型（GLMM）通过精确似然替代近似正态的within-study模型可减少此偏差。作者将Copas基于t统计量选择函数的似然敏感性分析框架扩展到多种GLMM设定下，提出了一种新的敏感性分析方法。该方法通过联合建模效应量分布与发表选择机制，利用精确似然进行参数估计和敏感性评估。模拟和真实数据应用表明，所提方法在稀疏数据场景下优于基于正态-正态模型的传统方法。对您而言，本文属于因果推断中敏感性分析的一个具体应用场景（发表偏倚），其核心思想——在精确似然框架下处理选择机制——与您熟悉的proximal CI中的negative control假设有相通之处，但方法学新颖性有限，属于已有框架的扩展应用。
- **关键技术**: `Copas selection function`, `generalized linear mixed model (GLMM)`, `exact likelihood`, `sensitivity analysis`, `publication bias`
- **为什么对您有用**: 本文属于流行病学/因果推断中发表偏倚的敏感性分析，连接您的secondary interest（流行病学应用）和primary interest（因果推断中的敏感性分析）。技术层面，您武器库中'identification theory in causal inference'（moderately_familiar）可用于理解其选择模型的可识别性假设，但核心方法（GLMM精确似然+选择函数）与您主要武器（非参、minimax bound、U-statistics）的直接接口较少。**暂不可做**：要深入改进此方法，需熟悉meta分析的选择模型文献和GLMM的数值计算，这些不在您当前武器库中。

### 17. [10.1093/biomtc/ujae060](https://doi.org/10.1093/biomtc/ujae060) — PathGPS: discover shared genetic architecture using GWAS summary data
- **作者**: Zijun Gao, Qingyuan Zhao, Trevor Hastie
- **期刊/来源**: Biometrics
- **机构**: University of Southern California · University of Cambridge · Institute of Mathematical Statistics · Stanford University
- **分类**: vol 80 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文提出 PathGPS，一种利用 GWAS 汇总统计量探索遗传架构的探索性数据分析工具。方法基于线性结构方程模型，将性状的遗传与环境路径解耦，通过对比“信号”基因与“噪声”基因的 GWAS 关联来实现。从估计的遗传成分中，利用主成分分析和因子分析提取低秩稀疏的遗传路径。为提升稳定性，作者引入了 bagging 算法以应对数据扰动和超参数调优。在代谢组学数据和 UK Biobank 上的应用验证了已知的基因-性状聚类，并提出了新假设。对您而言，本文的 SEM 解耦思路与因果推断中的 mediation 和 IV 方法有技术关联，且其低秩稀疏因子分析可迁移至高维统计中的降维问题。
- **关键技术**: `linear structural equation model`, `principal component analysis`, `factor analysis`, `bagging`, `GWAS summary data`
- **为什么对您有用**: 本文连接 causal inference 的 mediation 方向（遗传与环境路径解耦）和 high-dimensional statistics 的低秩稀疏方法。您的 technical_arsenal 中 'estimation theory in causal inference' 和 'high-dimensional asymptotics' 可直接用于分析其 SEM 识别条件与因子估计的收敛性。中期可做：需先在 'identification theory in causal inference' 上长肌肉以严格处理路径解耦的因果假设。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1093/biomtc/ujae096](https://doi.org/10.1093/biomtc/ujae096) — Heterogeneous latent transfer learning in Gaussian graphical models
- **作者**: Qiong Wu, Chi Wang, Yong Chen
- **期刊/来源**: Biometrics
- **机构**: University of Pittsburgh · University of Pennsylvania · University of Kentucky
- **分类**: vol 80 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究高斯图模型（GGM）的迁移学习，目标是在存在潜在异质性（如亚群）时，从多个源数据集中借力以改进目标数据集的图估计。现有迁移学习方法通常假设源与目标同质，忽略了样本内和样本间的异质性，可能导致负迁移。作者提出 Latent-TL 方法，核心思想是“向相似者学习”：同时识别样本的潜在亚群结构，并仅在同一亚群内进行源到目标的 GGM 迁移。算法通过交替优化实现亚群分配和亚群特异 GGM 的联合估计，属于一种带约束的 M-estimation 框架。模拟和乳腺癌基因共表达网络实证表明，Latent-TL 在边识别和网络结构恢复上优于单数据集学习和忽略异质性的标准迁移学习。该工作将高维图模型与迁移学习结合，并处理了实际生物医学数据中常见的异质性挑战，对您在高维统计和因果推断中处理多源异质性数据（如多中心 IV 或纵向数据）有直接的方法学参考价值。
- **关键技术**: `Gaussian graphical model`, `transfer learning`, `latent heterogeneity`, `subpopulation identification`, `M-estimation`
- **为什么对您有用**: 该论文直接关联您的高维统计兴趣，特别是处理异质性多源数据时的图模型估计问题。您的武器库中“高维渐近理论”和“M-estimation 理论”可直接用于分析其估计量的收敛性和亚群恢复的一致性，属于**中期可做**：需先在 moderately_familiar 的“identification theory in causal inference”上长肌肉，以将类似 latent structure 思想迁移到因果结构学习或异质性处理效应估计中。

## 非参数 / 半参数  *(nonparam_semipara, 2 篇)*

### 1. [10.1093/biomtc/ujae098](https://doi.org/10.1093/biomtc/ujae098) · [arXiv](https://arxiv.org/abs/2311.09935) — Semi-parametric benchmark dose analysis with monotone additive models
- **作者**: Alex Stringer, Tugba Akkaya Hocagil, Richard J Cook, Louise M Ryan, Sandra W Jacobson, Joseph L Jacobson
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文在基准剂量分析（benchmark dose analysis）中提出了一套基于单调可加剂量-反应模型的半参数推断框架。目标是在给定临床显著不良结局概率下，估计暴露剂量的基准水平（BMD）及其置信下限（BMDL）。方法上，首先采用惩罚B样条和Laplace近似边际似然拟合单调可加模型，保证剂量-反应曲线的单调性约束。然后开发了基于de Boor算法计算样条及其导数的反射牛顿法（reflective Newton method），用于高效估计BMD。最后，针对BMD估计所求解的非线性方程，构造了一个近似枢轴量（approximate pivot）来计算BMDL，并与Delta方法和参数bootstrap进行了比较。在六个NIH资助的纵向队列研究中，该方法被应用于评估产前酒精暴露与儿童认知缺陷的关联。本文的方法学贡献在于将单调性约束与半参数可加模型结合，并提供了计算BMDL的新途径。对您而言，该文的单调可加模型拟合与推断策略可迁移至因果推断中的剂量-反应曲线估计，尤其是当暴露-结局关系存在单调性假设时，其B样条+惩罚似然的框架值得关注。
- **关键技术**: `penalized B-splines`, `Laplace-approximate marginal likelihood`, `reflective Newton method`, `de Boor's algorithm`, `approximate pivot`, `monotone additive models`
- **为什么对您有用**: 该文直接关联您的非参数/半参数理论兴趣，特别是单调性约束下的样条估计与推断。您武器库中'非参数统计'和'M估计理论'可直接用于分析其估计量的收敛速度与渐近分布，而'软件工程'技能可帮助复现或扩展其semibmd R包。中期可做：若想将单调可加模型推广至因果推断中的连续处理效应估计，需先在'半参数理论'上加强（如处理高维协变量时的正交性条件）。

### 2. [10.1093/biomtc/ujae071](https://doi.org/10.1093/biomtc/ujae071) — Nonparametric second-order estimation for spatiotemporal point patterns
- **作者**: Decai Liang, Jialing Liu, Ye Shen, Yongtao Guan
- **期刊/来源**: Biometrics
- **机构**: Nankai University · Sun Yat-sen University · University of Georgia · Shenzhen Research Institute of Big Data · Chinese University of Hong Kong, Shenzhen
- **分类**: vol 80 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对时空点过程，提出了一种非参数二阶估计方法，目标是在空间和时间非平稳假设下估计二阶强度或对相关函数。现有方法通常假设时空平稳性，这在实践中往往不成立。作者采用核平滑技术，分别处理空间和时间的相关性，允许时间相关性非平稳。在空间递增域渐近框架下，证明了估计量的相合性，且估计量可基于不同的一阶强度估计量构建，增强了实用性。模拟结果显示，相比现有方法，该方法显著提高了统计效率。COVID-19数据集的应用进一步展示了方法的灵活性和可解释性。该工作与您的非参数统计和半参数理论兴趣直接相关，其核平滑和渐近理论框架可迁移至您熟悉的非参数估计问题。
- **关键技术**: `kernel smoothing`, `increasing-domain asymptotics`, `nonstationary spatiotemporal point processes`, `pair correlation function estimation`
- **为什么对您有用**: 本文属于非参数统计方法，直接连接您的 primary interest 中的非参数统计理论。您非常熟悉的非参数统计工具（如核方法、渐近理论）可直接用于理解本文的估计框架和相合性证明。中期可做：若想将类似方法推广至因果推断中的时空数据，需先在 moderately_familiar 的识别理论（如时空混淆）上提升。

## 数理统计 / 假设检验  *(hypothesis_testing, 4 篇)*

### 1. [10.1093/biomtc/ujae088](https://doi.org/10.1093/biomtc/ujae088) — High-dimensional multivariate analysis of variance via geometric median and bootstrapping
- **作者**: Guanghui Cheng, Ruitao Lin, Liuhua Peng
- **期刊/来源**: Biometrics
- **机构**: Guangzhou University · Guangdong University of Finance · The University of Texas MD Anderson Cancer Center · The University of Melbourne
- **分类**: vol 80 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究高维多元方差分析（MANOVA）问题，利用几何中位数作为多组位置参数的稳健估计量。提出一个基于组间几何中位数差异的最大型检验统计量，适用于高维数据。在零假设下，通过高斯逼近推导了该统计量的渐近分布，并在备择假设下证明了检验的一致性。为逼近高维下的分布，提出并理论证明了野自助法（wild bootstrap）。模拟研究覆盖多种维度、样本量和数据生成模型，展示了有限样本性能，并应用于乳腺癌基因表达数据集。该工作将经典MANOVA推广至高维稳健设定，对您在高维假设检验方向有直接参考价值。
- **关键技术**: `geometric median`, `maximum-type statistic`, `Gaussian approximation`, `wild bootstrap`, `high-dimensional MANOVA`
- **为什么对您有用**: 直接连接到您的高维统计与假设检验兴趣：本文在高维MANOVA中引入几何中位数作为稳健位置估计，并利用高斯逼近和野自助法进行推断。您的技术武器库中'高维渐近理论'和'非参数统计'可直接用于理解其理论框架，而'极小极大界'可用于评估其检验功效的最优性。中期可做：若想将几何中位数与您的U-统计量工作结合，需先在'高阶U-统计量理论'上加强。

### 2. [10.1093/biomtc/ujae082](https://doi.org/10.1093/biomtc/ujae082) · [arXiv](https://arxiv.org/abs/2310.09493) — Summary statistics knockoffs inference with family-wise error rate control
- **作者**: Catherine Xinrui Yu, Jiaqi Gu, Zhaomeng Chen, Zihuai He
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究在仅能获取边际依赖的汇总统计量（如GWAS中的z-score）时，如何对条件独立性假设进行多重检验并控制族系错误率（FWER）。作者采用GhostKnockoff框架，直接生成汇总统计量的knockoff副本，并提出一个新的筛选规则来选择与响应变量条件相关的特征。该方法的核心优势在于无需原始个体级数据，仅依赖汇总统计量即可进行推断。此外，作者开发了一种计算高效的算法，大幅降低了knockoff副本生成的计算成本，同时不牺牲统计功效和FWER控制。模拟实验和阿尔茨海默病遗传学真实数据表明，该方法在统计功效和计算效率上均优于现有替代方法。对您而言，本文的FWER控制框架与您在高维假设检验和因果推断中的兴趣直接相关，其基于汇总统计量的思路在遗传流行病学等应用中具有实用价值。
- **关键技术**: `GhostKnockoff`, `summary statistics knockoffs`, `family-wise error rate control`, `conditional independence testing`, `computationally efficient algorithm`
- **为什么对您有用**: 本文直接连接您在高维假设检验和因果推断中的兴趣，特别是FWER控制这一经典问题。您的技术武库中'high-dimensional asymptotics'和'estimation theory in causal inference'可直接用于分析该方法的渐近性质或扩展至因果设定。中期可做：若想将knockoff框架与您的proximal causal inference工作结合，需先在'moderately_familiar'的identification theory上加强。

### 3. [10.1093/biomtc/ujae079](https://doi.org/10.1093/biomtc/ujae079) — Hypothesis tests in ordinal predictive models with optimal accuracy
- **作者**: Yuyang Liu, Shan Luo, Jialiang Li
- **期刊/来源**: Biometrics
- **机构**: Shanghai Zhangjiang Laboratory · Shanghai Jiao Tong University · National University of Singapore
- **分类**: vol 80 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对多类有序判别问题中基于线性组合的最优预测模型，提出了一种统计推断方法。目标是对达到最优超体积（HUM）的预测变量组合进行假设检验。现有方法计算成本高，作者采用经验似然方法，并建立了Wilks定理和Pitman备择下的功效分析。核心创新在于提出了一种基于网络的快速算法，用于计算检验过程中涉及的一般多样本U-统计量。该算法利用U-统计量的结构，显著降低了计算复杂度。模拟实验表明，该方法在检验水平、功效和计算时间上均优于现有方法。最后，通过一个真实医学数据集展示了方法的实用性。本文直接连接您对higher-order U-statistics和hypothesis testing的兴趣，其网络算法为U-统计量的高效计算提供了新视角。
- **关键技术**: `jackknife empirical likelihood`, `Wilks' theorem`, `Pitman alternative`, `multi-sample U-statistic`, `network-based computation algorithm`, `hypervolume under ROC manifolds (HUM)`
- **为什么对您有用**: 本文直接连接您的primary interest：hypothesis testing和higher-order U-statistics。其提出的网络快速算法与您非常熟悉的higher-order U-statistics的treewidth/tensor contraction计算视角高度相关，可以尝试用einsum复杂度分析该算法的计算成本，并探索是否可推广到更一般的U-统计量。中期可做：需先在moderately_familiar的HOIF理论上长肌肉，以理解该检验在更复杂设定下的效率。

### 4. [10.1093/biomtc/ujae063](https://doi.org/10.1093/biomtc/ujae063) — Nonparametric receiver operating characteristic curve analysis with an imperfect gold standard
- **作者**: Jiarui Sun, Chao Tang, Wuxiang Xie, Xiao-Hua Zhou
- **期刊/来源**: Biometrics
- **机构**: Peking University · Peking University International Hospital · Peking University First Hospital · Peking University People's Hospital
- **分类**: vol 80 · issue 3
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究在参考标准（金标准）存在测量误差时，如何非参数地估计ROC曲线及其曲线下面积（AUC）。核心设定是：疾病状态的参考标准不完美，但研究者已知或可估计其灵敏度与特异度，并假设在给定真实疾病状态下，测试结果与参考标准条件独立。在此假设下，作者证明了ROC曲线是可识别的，并提出了基于经验分布的非参数估计方法。当参考标准的准确度完全未知时，ROC曲线不可识别，但两个AUC之差的符号仍然可识别；基于此，作者构建了一个假设检验方法来判断两个诊断测试的相对优劣。该方法不依赖参数模型假设，适用于连续型生物标志物的ROC/AUC分析以及有序分类生物标志物的AUC比较。理论结果和模拟研究验证了所提方法的有效性，并通过两个真实诊断研究进行了说明。对您而言，本文在非参数识别与假设检验框架下处理测量误差问题，与您对因果推断中测量误差（如proximal causal inference）和假设检验的兴趣直接相关，其识别策略（利用已知或可估计的参考标准准确度）可能为处理类似问题提供新思路。
- **关键技术**: `nonparametric identification`, `receiver operating characteristic (ROC) curve`, `area under the curve (AUC)`, `imperfect gold standard`, `conditional independence assumption`, `hypothesis testing for AUC difference`
- **为什么对您有用**: 本文直接关联您对因果推断中测量误差问题的兴趣（如proximal CI中的negative control），其非参数识别策略（利用已知的参考标准准确度）与您武器库中'identification theory in causal inference'的思路高度一致。您可以用'nonparametric statistics'和'minimax bounds'工具来评估其估计量的收敛速率是否最优，或探索在更弱假设下的识别可能性。中期可做：若想将方法推广到更复杂的协变量调整场景，需先在'semiparametric theory'上长肌肉。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1093/biomtc/ujae089](https://doi.org/10.1093/biomtc/ujae089) · [arXiv](https://arxiv.org/abs/2307.11941) — Visibility graph-based covariance functions for scalable spatial analysis in non-convex partially Euclidean domains
- **作者**: Brian Gilbert, Abhirup Datta
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对非凸部分欧几里得域（如水体）上的空间分析，提出一种基于可见性图（visibility graph）构造有效协方差函数的新方法。标准协方差函数基于测地距离时无法保证正定性，而现有非欧几里得方法未能尊重域的部分欧几里得性质（即某些点对间测地距离与欧氏距离一致）。该方法通过可见性图定义域内点对的连接关系，对连接点保留基于欧氏距离的协方差，同时通过条件独立性假设纳入非凸几何的影响。理论证明了该方法在整个参数空间上保持协方差函数的正定性和边际平稳性，且保留了域的内在部分欧几里得几何。为提升计算可扩展性，作者提供了有用的近似算法。模拟和切萨皮克湾酸度数据应用展示了该方法在非凸域生态监测中的潜力。对您而言，本文涉及统计计算中的可扩展算法设计，与您的统计计算兴趣（数值方法、算法）直接相关，且其图结构近似思路可能启发您在高阶U统计量计算中利用图论优化收缩顺序。
- **关键技术**: `visibility graph`, `covariance function`, `positive definiteness`, `non-convex domain`, `Gaussian process`, `scalable algorithm`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的primary interest中的统计计算（数值方法、算法）。其核心贡献——利用可见性图构造协方差函数并设计可扩展近似算法——与您武器库中'软件开发和逆问题'的算法设计经验有交集。中期可做：若您想将图结构近似思路迁移到高阶U统计量的计算成本优化（treewidth/tensor contraction），需先在moderately_familiar的'高阶U统计量理论'上加深理解，以评估图近似对收缩顺序的精度影响。

## 流行病学  *(epidemiology, 3 篇)*

### 1. [10.1093/biomtc/ujae074](https://doi.org/10.1093/biomtc/ujae074) · [arXiv](https://arxiv.org/abs/2308.15770) — Semiparametric inference of effective reproduction number dynamics from wastewater pathogen surveillance data
- **作者**: Isaac H Goldstein, Daniel M Parker, Sunny Jiang, Volodymyr M Minin
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对废水病原体监测数据，提出一个半参数模型来推断有效再生数（Rt）。模型将新感染视为随时间变化的迁入过程，其迁入率可解释为每个感染者单位时间产生的二次感染数，从而避免了对易感人群动态的强假设。作为副产品，该框架也适用于病例数据。通过基于智能体的仿真验证了模型在现实病原体脱落动态下的表现，并应用于洛杉矶废水SARS-CoV-2 RNA数据估计Rt。方法核心是将Rt的估计转化为一个半参数推断问题，可能涉及M估计或广义线性模型技术。对您而言，这是一篇流行病学应用论文，展示了如何用统计模型从新型数据源（废水）中提取关键流行病学参数，其建模思路（避免不可验证假设）与您因果推断中的识别策略有共鸣。
- **关键技术**: `semiparametric model`, `immigration rate model`, `agent-based simulation`, `effective reproduction number estimation`
- **为什么对您有用**: 本文属于流行病学应用，直接连接您的secondary interest。它展示了一个半参数建模策略来规避易感人群动态的不可验证假设，这与因果推断中通过负对照或工具变量放松识别假设的思路有方法论上的平行性。武器库中'identification theory in causal inference'的识别策略可类比于此处的建模选择。作为应用论文，值得花时间读全文以了解废水数据结构和分析流程，但核心方法学新颖性有限，属于'中期可做'——需先在'moderately_familiar'的流行病学数据特征上熟悉。

### 2. [10.1093/biomtc/ujae062](https://doi.org/10.1093/biomtc/ujae062) — Absolute risk from double nested case-control designs: cause-specific proportional hazards models with and without augmented estimating equations
- **作者**: Minjung Lee, Mitchell H Gail
- **期刊/来源**: Biometrics
- **机构**: Kangwon National University · National Cancer Institute · Division of Cancer Epidemiology and Genetics
- **分类**: vol 80 · issue 3
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对双嵌套病例对照设计（DNCC），在竞争风险框架下估计原因别比例风险模型的相对风险与绝对风险（累积发病率）。DNCC 设计在阶段二不仅匹配主要病因的病例，还匹配竞争风险病例，以获取完整协变量；其他队列成员仅有生存结局和部分协变量。作者采用 Samuelsen 型逆抽样概率构建设计加权估计方程，并引入增广估计方程（augmented estimating equations），利用全队列成员的额外信息提高效率。建立了包括绝对风险估计量在内的渐近性质，并推导了一致方差估计量。模拟显示所提方法在有限样本下具有名义操作特性。该方法在流行病学队列研究中具有直接应用价值，尤其适用于大型筛查试验的竞争风险分析。
- **关键技术**: `design-weighted estimation`, `augmented estimating equations`, `cause-specific proportional hazards model`, `competing risks`, `double nested case-control design`, `Samuelsen-type weights`
- **为什么对您有用**: 本文属于流行病学应用，直接涉及竞争风险下的因果参数（绝对风险）估计，与您 secondary interest 中的流行病学数据集和因果推断方法高度相关。您武器库中 'estimation theory in causal inference' 和 'identification theory in causal inference' 可直接用于理解其增广估计方程的效率提升机制。本文是值得花时间读全文的入门级流行病学方法论文，方法学新颖性适中（增广估计方程的应用），但分析模式对您处理类似队列数据有参考价值。

### 3. [10.1093/biomtc/ujae097](https://doi.org/10.1093/biomtc/ujae097) — Designing cancer screening trials for reduction in late-stage cancer incidence
- **作者**: Kehao Zhu, Ying-Qi Zhao, Yingye Zheng
- **期刊/来源**: Biometrics
- **机构**: University of Washington · Fred Hutch Cancer Center
- **分类**: vol 80 · issue 3
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文针对癌症早期检测生物标志物的随机对照试验（RCT）设计难题，提出基于多状态疾病历史模型的效应量推导方法。传统以死亡率为终点的筛查试验面临疾病自然史漫长、时变筛查效应难以刻画等挑战。作者将生物标志物检测的灵敏度等性能指标与晚期癌症发病率这一替代终点通过多状态模型直接关联，并纳入实际筛查程序（如检测频率、随访时长）的时序特征。方法基于RCT的日历时间尺度，允许研究者评估不同检测灵敏度、随访长度及重复检测次数下的统计功效。数值示例基于国家肺筛查试验（NLST）数据，展示了工具的实际应用。该工作为筛查试验的样本量计算和设计优化提供了可操作的统计工具，对您而言，这是一篇流行病学领域的应用型方法论文，其多状态模型框架与因果推断中的纵向数据设定有直接联系，且工具化思路对您开发统计软件有参考价值。
- **关键技术**: `multistate disease model`, `time-varying screening effect`, `sample size calculation for screening trials`, `surrogate endpoint (late-stage cancer incidence)`
- **为什么对您有用**: 本文属于流行病学领域的应用型方法论文，直接连接您的secondary interest。其多状态模型将检测灵敏度与晚期癌症发病率关联，本质是纵向因果推断中的替代终点问题，与您熟悉的非参数统计和因果推断中的identification理论有交集。武器库中'very_familiar'的'软件工具开发'可直接用于复现或扩展其计算工具；但核心方法（多状态模型下的功效分析）属于流行病学试验设计专用，与您primary interest的因果推断理论（如proximal CI）无直接技术重叠，因此属于'暂不可做'——缺少流行病学筛查试验设计的领域知识。作为入门读物，本文清晰展示了生物标志物评估中的统计挑战和建模思路，值得花时间读全文以理解应用场景。

## 其他  *(other, 11 篇)*

### 1. [10.1093/biomtc/ujae101](https://doi.org/10.1093/biomtc/ujae101) · [arXiv](https://arxiv.org/abs/2504.11767) — Post-selection inference in regression models for group testing data
- **作者**: Qinyan Shen, Karl Gregory, Xianzheng Huang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对分组检测（group testing）数据中响应变量部分缺失（仅观测到有误差的检测结果而非真实状态）的 logistic 回归模型，开发了变量选择后的有效推断方法。研究采用 EM 算法计算带 LASSO 惩罚的最大似然估计，实现变量选择与缺失信息处理。在变量选择后，基于多面体引理（polyhedral lemma）扩展了经典的后选择推断（post-selection inference）框架，对所选协变量的效应进行条件推断。模拟实验表明，该方法相比未调整选择过程的朴素推断（即用同一数据同时做选择和推断）提供了更可靠的覆盖率和检验水平。该方法主要贡献在于将 post-selection inference 从完全观测响应推广到部分观测响应场景，但核心工具（LASSO + polyhedral lemma）均为已有技术。对您而言，本文属于应用统计方法开发，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接技术交集，且分组检测设定在您的研究领域中较为边缘。
- **关键技术**: `EM algorithm`, `LASSO penalization`, `polyhedral lemma`, `post-selection inference`, `logistic regression`
- **为什么对您有用**: 本文属于生物统计应用（分组检测），与您的主要兴趣方向（因果推断、高维RMT、U-统计量、半参效率理论）无直接技术连接。武器库中的工具（如 minimax bound、higher-order U-statistics）难以直接攻入该文的设定。该文可视为流行病学应用的一个特例，但方法学 novelty 有限（主要是将已有 post-selection inference 框架移植到缺失响应场景），不值得作为 gateway reading 投入时间。

### 2. [10.1093/biomtc/ujae076](https://doi.org/10.1093/biomtc/ujae076) — Reduced-rank clustered coefficient regression for addressing multicollinearity in heterogeneous coefficient estimation
- **作者**: Yan Zhong, Kejun He, Gefei Li
- **期刊/来源**: Biometrics
- **机构**: East China Normal University · Renmin University of China
- **分类**: vol 80 · issue 3
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对聚类系数回归（CCR）中因多重共线性导致的估计与聚类不稳定性问题，提出了一种低秩结构约束的CCR方法。该方法将系数矩阵分解为低秩部分，并引入自适应组融合惩罚项以同时实现系数聚类与秩选择。通过一个非凸优化问题联合估计低秩结构与聚类模式，并开发了具有收敛保证的迭代算法。理论方面给出了系数估计误差的上界，证明了估计量的统计性质。模拟与COVID-19死亡率数据分析表明，该方法在多重共线性下比现有CCR方法更稳定。对您而言，该工作属于应用统计方法，与您的主要兴趣（因果推断、高维统计）无直接技术关联，但低秩+聚类的思想在异质性处理效应估计中可能有启发。
- **关键技术**: `clustered coefficient regression`, `low-rank matrix decomposition`, `adaptive group fusion penalty`, `non-convex optimization`, `iterative algorithm`
- **为什么对您有用**: 本文属于应用统计方法，与您的主要兴趣（因果推断、高维统计、半参理论）无直接技术重叠。低秩+聚类的思路在异质性处理效应估计中可能有启发，但核心机器（非凸优化、融合惩罚）不在您的武器库中。暂不可做——缺乏非凸优化与融合惩罚的熟悉度。

### 3. [10.1093/biomtc/ujae091](https://doi.org/10.1093/biomtc/ujae091) — Unit information Dirichlet process prior
- **作者**: Jiaqi Gu, Guosheng Yin
- **期刊/来源**: Biometrics
- **机构**: Stanford University · University of Hong Kong
- **分类**: vol 80 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出了一类新的非参数先验——单位信息狄利克雷过程（UIDP），用于生存分析中时间-事件数据的分布建模。核心思想是将参数模型下的单位信息（UI）概念扩展到非参数设定，通过推导累积风险函数微分的Fisher信息，使UIDP先验的先验UI与历史数据集的加权平均UI相匹配。该方法能够同时利用历史数据集提供的参数和非参数信息，实现自适应信息借用。通过马尔可夫链蒙特卡洛算法进行后验推断，模拟和真实数据分析表明UIDP先验能有效提高生存分析中的统计效率。本文主要贡献在于将单位信息先验从参数模型推广到非参数贝叶斯框架，为历史数据整合提供了新工具。
- **关键技术**: `Unit information prior`, `Dirichlet process`, `Cumulative hazard function`, `Fisher information`, `Markov chain Monte Carlo`, `Bayesian survival analysis`
- **为什么对您有用**: 本文属于贝叶斯非参数方法，与您的主要兴趣（非参数理论、统计计算）有间接关联，但核心问题（先验构建与信息借用）并非您当前研究重点。武器库中非参数统计和MCMC计算可理解本文方法，但缺乏贝叶斯非参数先验设计的专门知识，属于暂不可做方向。作为Biometrics期刊的方法学论文，对流行病学应用有参考价值，但方法学新颖性有限（主要是概念扩展而非理论突破）。

### 4. [10.1093/biomtc/ujae068](https://doi.org/10.1093/biomtc/ujae068) · [arXiv](https://arxiv.org/abs/2208.03157) — A Gaussian-process approximation to a spatial SIR process using moment closures and emulators
- **作者**: Parker Trostle, Joseph Guinness, Brian J Reich
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出一种空间SIR传染病传播模型的近似推断方法。核心思路是用高斯过程逼近复杂的空间随机SIR过程：先构造一个空间扩展的SIR随机过程，然后通过矩封闭（moment closure）推导出易感者和感染者均值和协方差随时间演化的常微分方程组（ODEs）。由于这些ODEs在MCMC中计算瓶颈过高，作者进一步用低秩仿真器（low-rank emulator）近似ODEs的解，以此作为层次模型的基础，对含噪声、低报的新增感染计数进行推断。模拟实验验证了方法对真实空间SIR跳跃过程的恢复能力，并应用于2015-2016年巴西Zika疫情数据。方法学上属于计算统计与近似推断的交叉，但未涉及因果推断、高维统计或效率理论等核心兴趣方向。
- **关键技术**: `moment closure`, `Gaussian process emulator`, `low-rank approximation`, `spatial SIR model`, `hierarchical Bayesian model`
- **为什么对您有用**: 本文属于统计计算与传染病建模的应用工作，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接交集。作为gateway reading，它展示了矩封闭和仿真器在复杂随机过程中的计算策略，但武器库中very_familiar的软件开发和MCMC经验可帮助理解其计算框架。暂不可做：核心问题（空间SIR的矩封闭推导与ODEs仿真器）不在您的技术栈中，且与您的主要研究方向距离较远，不值得花时间精读全文。

### 5. [10.1093/biomtc/ujae059](https://doi.org/10.1093/biomtc/ujae059) — Bayesian inference for multivariate probit model with latent envelope
- **作者**: Kwangmin Lee, Yeonhee Park
- **期刊/来源**: Biometrics
- **机构**: Chonnam National University · University of Wisconsin–Madison
- **分类**: vol 80 · issue 3
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出 probit envelope 模型，将响应包络（response envelope）思想推广到多元二元响应变量的情景。在多元 probit 模型中，通过引入潜变量并利用包络方法分离潜变量空间中的材料部分与不相关部分，从而在估计回归系数时获得效率提升。作者利用 essential identifiability 概念解决了模型的可识别性问题，并采用贝叶斯方法进行参数估计。模拟研究表明，相比标准多元 probit 模型，probit envelope 模型在估计效率上具有潜在优势。真实数据分析展示了该模型在多标签分类中的实用性。本文属于方法学应用型工作，核心贡献在于将包络方法从连续响应扩展到离散响应，但理论深度有限，未涉及效率界或渐近理论。
- **关键技术**: `response envelope model`, `multivariate probit model`, `latent variable model`, `Bayesian estimation`, `essential identifiability`
- **为什么对您有用**: 本文与您的主要兴趣（因果推断、半参理论）关联较弱，属于多元统计方法的应用扩展。虽然包络方法与降维和效率提升有关，但本文未涉及您熟悉的半参效率界、U-统计量或高维渐近工具。作为 Biometrics 上的应用型工作，对您而言可能仅作为多元分类方法的背景阅读，暂不可做后续跟进。

### 6. [10.1093/biomtc/ujae078](https://doi.org/10.1093/biomtc/ujae078) — Factor-augmented transformation models for interval-censored failure time data
- **作者**: Hongxi Li, Shuwei Li, Liuquan Sun, Xinyuan Song
- **期刊/来源**: Biometrics
- **机构**: Guangzhou University · Academy of Mathematics and Systems Science · University of Chinese Academy of Sciences · Chinese University of Hong Kong
- **分类**: vol 80 · issue 3
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对区间删失失效时间数据，提出因子增强变换模型（factor-augmented transformation model），以同时处理高维相关协变量带来的多重共线性问题。模型由两部分组成：因子分析模型将多个观测变量降维为少数潜因子，再将这些潜因子作为协变量纳入半参数变换模型，分析其对失效时间的影响。估计方法采用非参数最大似然（NPMLE），并开发了计算稳定的EM算法。作者证明了估计量的相合性和渐近正态性，并通过模拟和ADNI（阿尔茨海默病神经影像学计划）实际数据验证了方法性能。该工作主要贡献在于将因子分析与生存分析中的变换模型结合，解决区间删失数据下的降维和共线性问题。对您而言，本文属于应用统计方法论文，与您的主要兴趣（因果推断、高维统计、半参理论）方向有间接关联，但方法学创新性有限，且未涉及您核心关注的识别、效率理论或计算-统计权衡问题。
- **关键技术**: `factor analysis`, `semiparametric transformation model`, `nonparametric maximum likelihood estimation`, `EM algorithm`, `interval-censored data`
- **为什么对您有用**: 本文属于生存分析应用领域，与您的主要兴趣（因果推断、高维统计、半参理论）方向有间接关联，但方法学创新性有限。您武器库中的非参数统计和M估计理论可用于理解其NPMLE渐近性质，但核心问题（降维与共线性）并非您当前关注焦点。暂不可做：本文未涉及您核心关注的识别、效率理论或计算-统计权衡问题，且区间删失数据并非您武器库中的核心设定。

### 7. [10.1093/biomtc/ujae066](https://doi.org/10.1093/biomtc/ujae066) — An interpretable Bayesian clustering approach with feature selection for analyzing spatially resolved transcriptomics data
- **作者**: Huimin Li, Bencong Zhu, Xi Jiang, Lei Guo, Yang Xie, Lin Xu et al.
- **期刊/来源**: Biometrics
- **机构**: The University of Texas at Dallas · Chinese University of Hong Kong · Southern Methodist University · Southwestern Medical Center · The University of Texas Southwestern Medical Center
- **分类**: vol 80 · issue 3
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对空间分辨转录组学（SRT）数据，提出了一种可解释的贝叶斯聚类方法。核心设定是：每个spot/cell的分子表达服从零膨胀负二项（ZINB）分布，聚类目标是将区域划分为互斥的空间域。方法的关键机制包括：(1) 通过特征选择机制自动识别判别性基因，避免对高维分子谱进行黑箱降维；(2) 利用马尔可夫随机场（MRF）先验整合空间邻近信息，实现空间平滑聚类。模型采用贝叶斯框架进行推断，输出聚类结果及判别基因列表，增强了可解释性。通过模拟和三个真实数据集（如人脑组织、乳腺癌组织）的实证，展示了该方法在聚类准确性上优于现有非空间和空间聚类方法。对您而言，本文属于生物统计应用，与您的主要兴趣（因果推断、高维统计等）无直接方法学连接，但可作为了解空间转录组学数据结构和聚类分析流程的入门读物。
- **关键技术**: `Zero-inflated negative binomial mixture model`, `Markov random field prior`, `Bayesian feature selection`, `Spatially resolved transcriptomics`
- **为什么对您有用**: 本文属于生物统计应用，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接方法学连接。作为gateway-reading，本文对SRT数据结构和贝叶斯空间聚类方法有清晰介绍，但未涉及您武器库中的核心工具（如非参、minimax界、高阶U-统计量）。暂不可做：核心机器（贝叶斯空间模型、ZINB混合模型）不在武器库中，且方法学新颖性有限（novelty_flag=application）。

### 8. [10.1093/biomtc/ujae075](https://doi.org/10.1093/biomtc/ujae075) · [arXiv](https://arxiv.org/abs/2308.10583) — The multivariate Bernoulli detector: change point estimation in discrete survival analysis
- **作者**: Willem van den Boom, Maria De Iorio, Fang Qian, Alessandra Guglielmi
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对离散时间、多竞争风险（competing risks）的生存数据，提出一种多元伯努利检测器（multivariate Bernoulli detector）用于变化点（change point）估计。模型在 cause-specific baseline hazards 上引入多元变化点结构，通过先验对变化点数目和位置施加跨风险的依赖关系，并利用多元伯努利先验推断哪些风险在变化点处发生改变。后验推断采用定制的局部-全局 MCMC 算法，结合数据增广和非共轭贝叶斯非参数方法。模拟和 ICU 数据实例表明，该方法在估计 cause-specific hazard rates 和跨风险依赖方面优于现有方法。本文属于贝叶斯非参数生存分析的应用方法，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接技术重叠。
- **关键技术**: `multivariate change point model`, `competing risks`, `cause-specific baseline hazards`, `MCMC with data augmentation`, `nonconjugate Bayesian nonparametrics`
- **为什么对您有用**: 本文属于贝叶斯生存分析的应用方法，与您的主要兴趣方向（因果推断、高维统计、U-统计量等）无直接技术连接。武器库中 very_familiar 的非参统计和 moderately_familiar 的 M-估计理论可帮助理解模型设定，但核心贝叶斯变化点推断与您的工具链差异较大。暂不可做——缺少贝叶斯非参数和 MCMC 算法设计的核心机器。

### 9. [10.1093/biomtc/ujae093](https://doi.org/10.1093/biomtc/ujae093) — A Bayesian latent-subgroup platform design for dose optimization
- **作者**: Rongji Mu, Xiaojiang Zhan, Rui (Sammi) Tang, Ying Yuan
- **期刊/来源**: Biometrics
- **机构**: Shanghai Jiao Tong University · The University of Texas MD Anderson Cancer Center
- **分类**: vol 80 · issue 3
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对肿瘤药物开发中剂量优化（从最大耐受剂量转向最优生物剂量OBD）的实际需求，提出了一种基于主协议（master-protocol）的平台试验设计。该设计采用贝叶斯潜在亚组模型来刻画不同适应症间的治疗异质性，并利用贝叶斯分层模型在亚组内借用信息。在每次中期分析时，模型根据所有治疗臂的观测数据更新亚组归属、剂量-毒性、剂量-疗效以及风险-收益权衡的效用估计，从而指导各臂的剂量升降决策并识别OBD。模拟研究表明该设计具有良好的操作特征，能灵活高效地实现剂量优化。该方法有望缩短药物开发时间线、降低重叠基础设施成本并加速监管审批。
- **关键技术**: `Bayesian latent subgroup model`, `Bayesian hierarchical model`, `platform trial design`, `dose optimization`, `risk-benefit utility`
- **为什么对您有用**: 本文属于临床试验设计的方法学论文，与您的主要兴趣（因果推断、高维统计等）无直接交集。其贝叶斯分层模型和潜在亚组建模技术虽有一定统计趣味，但并非您武器库中的核心工具。作为gateway reading价值有限，不建议深入阅读。

### 10. [10.1093/biomtc/ujae081](https://doi.org/10.1093/biomtc/ujae081) · [arXiv](https://arxiv.org/abs/2308.12859) — Towards automated animal density estimation with acoustic spatial capture-recapture
- **作者**: Yuheng Wang, Juan Ye, Xiaohui Li, David L Borchers
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文针对被动声学监测中机器学习自动检测产生的假阳性问题，提出一种声学空间捕获-再捕获（ASCR）方法。将物种身份视为潜变量，ML输出的个体级检测结果作为依赖于该潜变量的随机变量，构建混合模型似然函数来估计叫声密度。该方法无需人工校正假阳性，直接通过EM或数值优化最大化似然。应用于青蛙调查和基于真实长臂猿数据的模拟实验，估计偏差接近零且覆盖概率准确，显著优于未处理假阳性的ASCR和常用的校正因子方法。对您而言，本文属于应用统计方法在生态学中的案例，与您的主要兴趣方向（因果推断、高维统计等）无直接技术重叠，但展示了潜变量模型处理测量误差的思路。
- **关键技术**: `spatial capture-recapture`, `mixture model likelihood`, `latent variable model`, `passive acoustic monitoring`, `false positive correction`
- **为什么对您有用**: 本文属于生态统计应用，与您的主要兴趣方向（因果推断、高维统计、U统计量等）无直接技术连接。武器库中的非参数统计和M估计理论可理解其似然框架，但核心问题（声学检测假阳性校正）并非您当前研究领域。作为gateway reading，本文对生态学外行较友好，但统计方法学贡献有限（混合模型+潜变量是标准工具）。暂不可做：缺乏生态学数据和应用场景，且方法学新颖性不足以驱动您投入时间。

### 11. [10.1093/biomtc/ujae104](https://doi.org/10.1093/biomtc/ujae104) — Planning cost-effective operational forest inventories
- **作者**: Santeri Karppinen, Liviu Ene, Lovisa Engberg Sundström, Juha Karvanen
- **期刊/来源**: Biometrics
- **机构**: University of Jyväskylä · Forestry Research Institute of Sweden
- **分类**: vol 80 · issue 3
- 相关性 1/10 · novelty: `application`
- **摘要**: 本文研究运营林业中的贝叶斯两阶段决策问题：内层阶段根据需求目标安排采伐计划，外层阶段选择预采伐库存调查的精度以估计林区木材体积。外层问题被建模为在预算约束下最大化库存决策的后验价值，该后验价值依赖于内层问题的解，且计算上难以处理——涉及NP难的二元优化问题和高维积分。内层优化是广义二次分配问题的特例。作者提出一种实用方法，将蒙特卡洛采样与贪心随机化方法结合来近似求解外层问题。基于100个瑞典林区的数据集，推导了不同库存预算下的决策，并估计了所获信息的价值。本文是应用导向的方法学工作，但统计方法（贝叶斯决策、蒙特卡洛近似）较为常规，与您的主要研究方向（因果推断、高维统计、U统计量等）无直接交集。
- **关键技术**: `Bayesian decision theory`, `Monte Carlo sampling`, `greedy randomized algorithm`, `generalized quadratic assignment problem`
- **为什么对您有用**: 本文属于林业运筹学应用，与您的主要兴趣方向（因果推断、高维统计、U统计量）无直接技术关联。武器库中的非参数统计或M估计理论在此处没有直接切入点。作为gateway-reading，本文对统计学家而言入门门槛低，但核心问题（NP难优化+贝叶斯决策）并非您当前武器库能直接攻克的领域。建议仅作泛读，不投入深度阅读时间。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

