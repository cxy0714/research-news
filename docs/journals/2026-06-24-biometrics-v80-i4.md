# Biometrics — Vol 80  Issue 4  ·  2026-06-24

- 共 52 篇 · Biometrics
- 目录核对 ⚠️ 疑似漏 2 篇（对照 OpenAlex 55 篇）：10.1093/biomtc/ujae126、10.1093/biomtc/ujae133

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

Biometrics 第80卷第4期共52篇论文，主题高度集中于因果推断方法的拓展，尤其围绕识别假设的敏感性与估计效率的提升展开。此外，半参数/非参数方法在复杂数据（生存、纵向、功能数据）中的延伸，以及高维与网络结构下的推断问题（去偏估计、图模型、中介分析）构成另外两条主线。因果推断方向论文超过三分之一，可进一步细分为：利用外部数据/辅助信息提升效率（含半参数效率界与双重稳健估计）、未测量混杂的敏感性分析（含半参数与贝叶斯框架）、生存/复发事件中的因果效应（含高维混杂与时间错位）、动态治疗与SMART设计（含自适应随机化与最优分配）、中介分析（含矩阵值与脑网络中介）。其余方向中，高维随机矩阵聚焦于测量误差校正与网络估计，半参数/非参数则覆盖分布回归、治愈模型、预后度量与变点检测。

因果推断中，效率与稳健估计是一条突出子线：多篇论文利用外部数据或辅助信息提高估计精度，如《A causal inference framework for leveraging external controls in hybrid trials》推导半参数效率界并构建双重稳健估计量；《Leveraging information from secondary endpoints to enhance dynamic borrowing across subpopulations》通过贝叶斯分层模型联合主/次要终点借力；《How to achieve model-robust inference in stepped wedge trials with model-based methods?》证明处理效应结构正确时工作模型可误设。敏感性分析是另一密集子线：四篇论文分别针对观测研究、随机试验中不规则评估、预测模型转运、测量误差等场景，提出半参数指数倾斜或贝叶斯框架量化未测量混杂的影响，包括《Semiparametric sensitivity analysis: unmeasured confounding in observational studies》（推导非参数有效影响函数）、《Sensitivity analysis for studies transporting prediction models》（利用指数倾斜模型）、《Semi-parametric sensitivity analysis for trials with irregular and informative assessment times》以及《De-biasing the bias: methods for improving disparity assessments with noisy group measurements》（将敏感性分析引向算法公平性）。生存/复发事件方向也有多篇：如《Causal effect estimation in survival analysis with high dimensional confounders》结合因子模型与双重稳健估计处理高维混杂；《A Bayesian framework for causal analysis of recurrent events with timing misalignment》将时间错位建模为时变治疗问题；《Large-scale survival analysis with a cure fraction》则提出概率加权估计方程处理治愈分数。SMART设计与自适应试验方面，《Adaptive randomization methods for sequential multiple assignment randomized trials via Thompson sampling》首次在多阶段设计中引入Thompson采样并给出事后推断方法；《Optimal adaptive SMART designs with binary outcomes》采用约束优化最小化期望治疗失败数；《A generalized logrank-type test for comparison of treatment regimes in sequential multiple assignment randomized trials》则构建加权对数秩检验。中介分析展现了高维与结构化中介变量的新进展：《A Bayesian joint model for mediation analysis with matrix-valued mediators》通过概率MPCA提取矩阵特征；《Bayesian pathway analysis over brain network mediators for survival data》将对称矩阵变量AFT与网络中介结合。

半参数/非参数主线中，值得注意的有：《Wasserstein regression with empirical measures and density estimation for sparse data》无需预估计密度即实现分布回归，证明稀疏样本下跨分布借力的一致性；《Time-dependent prognostic accuracy measures for recurrent event data》用共享脆弱项刻画未观测异质性；《A multivariate Polya tree model for meta-analysis with event-time distributions》将Polya tree先验扩展为多元GP版本。高维主线中，《Debiased high-dimensional regression calibration for errors-in-variables log-contrast models》首次在高维组合数据中实现去偏推断；《On network deconvolution for undirected graphs》证明网络解卷积等价于精度矩阵，为因果结构学习提供新视角；《Estimation of a genetic Gaussian network using GWAS summary data》利用多变量孟德尔随机化消除偏差。

因果推断与半参数效率方向（如利用外部数据的双重稳健估计、半参数敏感性分析）以及高维去偏与图模型方向的论文与您的研究兴趣最贴合，适合优先阅读。

## 因果推断  *(causal_inference, 18 篇)*

### 1. [10.1093/biomtc/ujae095](https://doi.org/10.1093/biomtc/ujae095) · [arXiv](https://arxiv.org/abs/2305.08969) — A causal inference framework for leveraging external controls in hybrid trials
- **作者**: Michael Valancius, Herbert Pang, Jiawen Zhu, Stephen R Cole, Michele Jonsson Funk, Michael R Kosorok
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 该文在混合试验（hybrid trial）框架下，探讨如何利用外部对照数据（来自历史试验的安慰剂组）与随机化试验内部数据结合，以提升平均处理效应（ATE）的估计效率。问题设定为：试验组来自当前随机对照试验（RCT），而对照组同时包含RCT内部对照和外部对照，缺乏完全随机化，因此对模型假设的依赖更强。论文给出了识别ATE的充分因果假设（包括内部-外部对照可交换性），并借助有向无环图（DAG）形式化这些假设，建立了与新颖图形判据的联系。在估计方面，作者推导了半参数效率界，并开发了高效的双重稳健（doubly robust）估计量，允许使用灵活的机器学习方法估计未知干扰参数，同时给出模型诊断工具。通过模拟研究和应用于SUNFISH临床试验（评估risdiplam对脊髓性肌萎缩症运动功能的影响），展示了该方法在有限样本下的表现。本文为利用外部对照的因果推断提供了系统的半参数效率理论框架，对您使用去偏机器学习（DML）和效率界工具的实证因果研究有直接参考价值。
- **关键技术**: `double robust estimation`, `semiparametric efficiency bound`, `exchangeability assumptions`, `external control adjustment`, `graphical criteria (DAG)`, `cross-fitting`
- **为什么对您有用**: 该文直接切入您主要兴趣中的因果推断和效率理论（半参数效率界、去偏ML），且将外部对照识别问题与您武器库中熟悉的因果推断估计理论（DR估计量）和软件实现能力挂钩。您已掌握的非参数统计和M估计理论可轻松理解其效率界推导；中期可做的是延伸其方法至更复杂的识别设定（如中介分析或时间相依处理），需要先在识别理论（moderately familiar）上巩固。

### 2. [10.1093/biomtc/ujae112](https://doi.org/10.1093/biomtc/ujae112) — On network deconvolution for undirected graphs
- **作者**: Zhaotong Lin, Isaac Pan, Wei Pan
- **期刊/来源**: Biometrics
- **机构**: Florida State University · University of Minnesota · Pomona College
- **分类**: vol 80 · issue 4
- 相关性 9/10 · novelty: `new_theory`
- **摘要**: 本文聚焦网络解卷积（ND）在无向图上的应用，其目标是从总效应网络重建直接效应网络，揭示直接与间接关联的分离。作者首先澄清了ND隐含的线性模型假设，即总效应可加性分解为直接效应与间接效应之和。核心理论贡献在于证明ND在无向图上等价于使用精度矩阵（precision matrix），这为ND的直观识别机制提供了简洁的闭式解。进一步，还形式化刻画了总效应图缩放对结果的影响。在应用层面，利用大规模GWAS数据，将ND用于对比身高与冠心病风险之间的边际遗传相关与条件遗传相关，结果与利用ND推断的有向因果图一致。本文为ND在无向图上的有效性提供了理论支撑，并展示了其在因果中介分析中的潜在用途。对您而言，该连接可迁移至因果推断中的直接/间接效应识别问题，尤其是中介分析中的分离策略。
- **关键技术**: `network deconvolution`, `precision matrix`, `direct and indirect effects`, `linear model assumption`, `GWAS`, `conditional genetic correlation`
- **为什么对您有用**: 该论文直接连接您对因果推断中中介分析与直接/间接效应分解的兴趣，特别是识别直接效应的方法论基础。您的武器库中“因果推断中的识别理论”（moderately_familiar）可用于严格评估其等价性证明的充分条件；而“高维渐近理论”（very_familiar）适合分析此方法在GWAS高维数据下的统计性质。阅读本文立即可做，因其模型假设与线性分解均处于您熟悉的非参数统计与估计理论框架内。

### 3. [10.1093/biomtc/ujae110](https://doi.org/10.1093/biomtc/ujae110) — Causal effect estimation in survival analysis with high dimensional confounders
- **作者**: Fei Jiang, Ge Zhao, Rosa Rodriguez-Monguio, Yanyuan Ma
- **期刊/来源**: Biometrics
- **机构**: University of California, San Francisco · Portland State University · Pennsylvania State University
- **分类**: vol 80 · issue 4
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 针对生存数据中高维混杂因素（协变量数超过样本量）下的因果效应估计问题，本文以受限平均生存时间（RMST）之差为处理效应目标。作者提出将因子模型与充分降维技术结合，从高维协变量中提取低维倾向得分和预后得分，从而避免直接匹配或正则化方法的偏差。在此基础上，基于核函数构造双重稳健估计量，兼具匹配思想的直观性和统计理论的支持。论文建立了估计量的一致性和渐近正态性，并推导了其方差解析形式，便于推断。通过模拟和弥漫性大B细胞淋巴瘤数据集的应用，展示了方法在有限样本下的表现。对于您而言，本文在高维因果推断中引入了降维与双重稳健的融合，直接连接您的因果推断和生存数据分析兴趣，且其理论分析思路可迁移至其他生存终点设定。
- **关键技术**: `factor model`, `sufficient dimension reduction`, `propensity score`, `prognostic score`, `kernel-based doubly robust estimator`, `restricted mean survival time`
- **为什么对您有用**: 本文连接您在高维因果推断（特别是混杂维度高、需要降维的场景）和生存分析中的兴趣。您非常熟悉的非参数统计与高维渐近理论恰好可以用于理解该估计量的收敛性质和分析其偏差-方差权衡；这是立即可做的方向，因为您的核心武器库已覆盖其关键技术（非参数核方法、双重稳健构造、高维正则化直觉）。

### 4. [10.1093/biomtc/ujae106](https://doi.org/10.1093/biomtc/ujae106) · [arXiv](https://arxiv.org/abs/2104.08300) — Semiparametric sensitivity analysis: unmeasured confounding in observational studies
- **作者**: Razieh Nabi, Matteo Bonvini, Edward H Kennedy, Ming-Yueh Huang, Marcela Smid, Daniel O Scharfstein
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文在观测研究中针对平均因果效应 (ACE) 提出了一套半参数敏感性分析框架，用于量化未测量混杂对因果结论稳健性的影响。核心设定沿袭 Robins et al. 和 Franks et al. 的敏感性参数化方法，将敏感性参数视为固定值，在不对敏感性参数施加任何限制的半参数模型下推导 ACE 的非参数有效影响函数。基于该影响函数，作者构建了 one-step、split-sample、truncated 估计量，并给出了保证估计量具有 √n-速率渐近正态性的充分条件。实证部分应用于孕期吸烟对出生体重的影响评估，模拟研究验证了估计程序的小样本表现。对您而言，这是将半参数效率理论系统应用于敏感性分析问题的范例，与您 primary interest 中的 sensitivity analysis 和 efficiency theory 直接相关。
- **关键技术**: `semiparametric sensitivity analysis`, `efficient influence function`, `one-step estimator`, `cross-fitting / split-sample`, `unmeasured confounding`, `truncated estimator`
- **为什么对您有用**: (1) 直接连接到您 primary interest 中的 sensitivity analysis 和 efficiency theory——这是将 semiparametric efficiency bounds 系统应用于敏感性分析框架的工作，而非仅是 ad-hoc 方法。(2) 您武器库中的 semiparametric theory (moderately_familiar) 和 estimation theory in causal inference (very_familiar) 正是本文的核心技术工具，可以用来审视其影响函数推导的完备性、truncation 策略对 efficiency 的影响，或探索是否能用 HOIF 改进高维协变量情形下的表现。(3) **立即可做**：技术门槛在您熟悉的范围内，可直接复现其估计量或将其框架扩展到您关注的 longitudinal / mediation 设定。

### 5. [10.1093/biomtc/ujae145](https://doi.org/10.1093/biomtc/ujae145) · [arXiv](https://arxiv.org/abs/2304.03247) — A Bayesian framework for causal analysis of recurrent events with timing misalignment
- **作者**: Arman Oganisian, Anthony Girard, Jon A Steingrimsson, Patience Moyo
- **期刊/来源**: Biometrics
- **机构**: John Brown University · Brown University
- **分类**: vol 80 · issue 4
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在观察性复发事件研究中，目标是估计目标人群在特定随访窗口内两种治疗下的事件率差异，核心困难在于资格认定时间与治疗开始时间的不对齐以及死亡等终止事件对复发过程的截断。作者将时间错位问题建模为时变治疗问题：部分患者在资格认定时已接受治疗，另一部分则可能在后续切换治疗，从而定义并识别了在右删失下的平均因果效应估计量。估计采用 g-computation 程序，结合死亡与复发事件过程的联合半参数贝叶斯模型，通过后验推断实现因果效应估计。该方法应用于 Medicare 医保索赔数据，比较不同阿片类药物治疗下的住院率差异。对您而言，这篇论文展示了复发事件因果推断中时间错位问题的识别策略与半参数贝叶斯估计方案，与您 primary interest 中的因果推断 identification 理论和半参数方法直接相关。
- **关键技术**: `g-computation`, `time-varying treatment`, `joint semiparametric Bayesian model`, `recurrent event process`, `right-censoring`, `identification under timing misalignment`
- **为什么对您有用**: (1) 连接到因果推断中的 identification 理论和半参数估计，具体是复发事件设定下的时变治疗问题与 g-computation 方法。(2) 您 very_familiar 的 estimation theory in causal inference 和 moderately_familiar 的 identification theory / semiparametric theory 可以直接用来审视其识别策略的严谨性和估计量的效率性质。(3) **立即可做**：用您熟悉的 identification 理论框架检查其时变治疗表述是否可简化为标准 g-formula 的某种特例，或用半参数效率理论评估其贝叶斯估计量是否达到效率下界。

### 6. [10.1093/biomtc/ujae129](https://doi.org/10.1093/biomtc/ujae129) · [arXiv](https://arxiv.org/abs/2306.08084) — Sensitivity analysis for studies transporting prediction models
- **作者**: Jon A Steingrimsson, Sarah E Robertson, Sarah Voter, Issa J Dahabreh
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在 transportability / external validity 框架下，目标是在仅有协变量数据（无结局数据）的目标人群中估计预测模型的性能指标（如 risk、AUC），核心识别假设是结局与人群指示变量在协变量条件下独立（即 no effect modification by population）。本文提出 exponential tilt sensitivity analysis 模型，通过引入倾向得分方向的指数倾斜参数来量化条件独立假设的违反程度，并给出在该敏感性分析模型下目标人群 risk 的识别公式。估计方面采用 one-step estimator / AIPW 形式，结合 influence function 构造，证明了估计量的 n^{-1/2}-CAN 性质和渐近正态性。实证部分应用于肺癌筛查数据，展示不同倾斜参数下模型性能指标的变化轨迹。对您而言，这是 sensitivity analysis 在 model transportability 场景的具体应用，与您 primary interest 中的 sensitivity analysis 和 identification theory 直接相关。
- **关键技术**: `exponential tilt model`, `transportability`, `sensitivity analysis`, `one-step estimator`, `influence function`, `AIPW`
- **为什么对您有用**: 直接连接到您 primary interest 中的 sensitivity analysis 和 causal identification theory——exponential tilt 是经典的敏感性分析参数化方式，这里的 transportability 设定与 proximal CI 中的 negative control 思路有方法论上的呼应。您武器库中的 identification theory in causal inference（moderately_familiar）和 semiparametric theory（moderately_familiar）足以攻这篇 paper 的理论部分。**立即可做**：用 very_familiar 的 estimation theory in causal inference 可以直接验证其 estimator 的效率性质，或尝试将 exponential tilt 与您熟悉的 proximal CI sensitivity 框架做对比。

### 7. [10.1093/biomtc/ujae143](https://doi.org/10.1093/biomtc/ujae143) · [arXiv](https://arxiv.org/abs/2310.00803) — A Bayesian joint model for mediation analysis with matrix-valued mediators
- **作者**: Zijin Liu, Zhihui (Amy) Liu, Ali Hosni, John Kim, Bei Jiang, Olli Saarela
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对放射治疗中计划剂量对治疗中断的影响，提出一个处理矩阵值中介变量的贝叶斯联合中介模型。传统中介分析通常假设中介变量为标量或向量，但本研究中器官的剂量体积直方图（DVH）以矩阵形式存在。模型通过概率多线性主成分分析（MPCA）从矩阵数据中提取潜在特征，保留矩阵结构。采用吉布斯采样联合估计所有参数，并引入Varimax旋转识别活跃的中介指标。模拟显示所提联合模型在估计因果分解效应时比两步法更高效，并能在矩阵形式下可视化和识别中介效应。该方法为高维矩阵中介分析提供了新框架，对因果推断中复杂中介结构的研究有参考价值。
- **关键技术**: `Bayesian joint mediation model`, `probabilistic multilinear principal components analysis (MPCA)`, `Gibbs sampling`, `Varimax rotation`, `matrix-valued mediators`, `causal decomposition effects`
- **为什么对您有用**: 本文直接对应您因果推断方向中的中介分析子方向，特别是处理矩阵结构的高维中介变量，这对您的‘mediation’兴趣是实质性拓展。技术层面，您熟悉的高维渐近理论和因果推断估计框架可用于评估该贝叶斯方法的频率性质（如偏差和效率），但需要先熟悉概率PCA和吉布斯采样在因果模型中的行为。因此，这是一篇‘中期可做’的论文——需先在贝叶斯高维中介模型上建立理解，再结合您已有的非参数和半参数工具进行延伸。

### 8. [10.1093/biomtc/ujae132](https://doi.org/10.1093/biomtc/ujae132) · [arXiv](https://arxiv.org/abs/2309.13677) — Bayesian pathway analysis over brain network mediators for survival data
- **作者**: Xinyuan Tian, Fan Li, Li Shen, Denise Esserman, Yize Zhao
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在脑网络中介分析中，本文提出一种贝叶斯路径分析方法，以同时建模遗传暴露、全脑网络中介和生存结局之间的因果路径。具体方法包括一个对称矩阵变量加速失效时间模型用于生存时间，以及一个对称矩阵响应回归用于网络中介；通过引入图内稀疏性和图间收缩来识别有信息的中介连接并抑制噪声；采用贝叶斯推断框架实现参数估计和不确定性量化。模拟实验表明所提方法优于现有替代方法；应用于阿尔茨海默病神经影像倡议（ADNI）的数据，获得了神经生物学合理的见解。该方法将半参数AFT模型与矩阵变量建模结合，对您在中介分析中使用非参数/半参数工具处理复杂中介变量有借鉴意义。
- **关键技术**: `Bayesian mediation analysis`, `matrix-variable accelerated failure time model`, `symmetric matrix response regression`, `within-graph sparsity`, `between-graph shrinkage`, `brain network mediator`
- **为什么对您有用**: 该论文直接连接您对因果推断中介分析的兴趣，并展示了如何在高维网络中介中引入结构假设。您可尝试用semiparametric theory（moderately_familiar）分析该贝叶斯方法的半参数效率性质，或将其识别条件与经典中介分析对比。目前该文使用贝叶斯MCMC，而非您熟悉的估计理论框架，因此属于中期可做，需要先在semiparametric theory或identification theory上进一步熟悉。

### 9. [10.1093/biomtc/ujae139](https://doi.org/10.1093/biomtc/ujae139) · [arXiv](https://arxiv.org/abs/2403.16813) — A generalized logrank-type test for comparison of treatment regimes in sequential multiple assignment randomized trials
- **作者**: Anastasios A Tsiatis, Marie Davidian
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 该论文在序贯多分配随机试验（SMART）框架下，针对多阶段治疗策略（treatment regimes）的比较，提出了一类推广的logrank型检验。研究目标是检验一组嵌入设计中的动态治疗方案之间的生存分布差异，结局为时间至事件变量。方法核心是构建一个加权对数秩检验统计量，通过逆概率加权处理SMART中患者在各阶段被分配不同治疗的非随机性，并允许纳入协变量以提高效率；框架同时适用于观察性研究。作者明确给出了产生有效检验所需的关键假设（如无未测量混杂、治疗分配机制已知或可建模），并证明该检验包络或改进了现有方法。该工作直接连接因果推断中的时序/动态处理效应评估，也涉及假设检验和半参数效率理论；研究者可基于自身在因果推断估计理论和半参数方法的积累，快速理解并尝试将该检验推广至更复杂设定（如存在删失或竞争风险）。
- **关键技术**: `logrank-type test`, `sequential multiple assignment randomized trial (SMART)`, `inverse probability weighting`, `covariate adjustment`, `embedded treatment regimes`, `semiparametric efficiency`
- **为什么对您有用**: 该论文直接关联您的两个首要兴趣子方向：因果推断中的时序/动态处理（SMART设计）和假设检验（对数秩检验）。（1）子方向连接：SMART是评估多阶段治疗策略的黄金设计，该文为其提供了正式的假设检验工具，是因果推断从识别/估计向推断延伸的重要补充；（2）技术武器连接：您对causal inference estimation theory（very_familiar）和semiparametric theory（moderately_familiar）的掌握，足以支撑您理解文中使用的逆概率加权和半参数框架，并可尝试将这一检验思路应用于您熟悉的纵向因果推断场景；（3）follow-up粗判：立即可做——基于您对因果推断估计理论的熟练掌握，可立即复现该方法在仿真或公开SMART数据集上的应用，并思考如何引入更高效的协变量调整或敏感性分析。

### 10. [10.1093/biomtc/ujae154](https://doi.org/10.1093/biomtc/ujae154) · [arXiv](https://arxiv.org/abs/2204.11979) — Semi-parametric sensitivity analysis for trials with irregular and informative assessment times
- **作者**: Bonnie B Smith, Yujing Gao, Shu Yang, Ravi Varadhan, Andrea J Apter, Daniel O Scharfstein
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 许多随机试验预设了固定的随访时间，但实际评估时间可能偏离计划，且评估时机可能与未观测的结局相关，导致治疗效果估计困难。本文提出一种半参数敏感性分析框架，以“可解释评估”(EA)为基准假设，即给定协变量历史后评估时间和结局条件独立；通过指数倾斜模型引入一个敏感性参数来量化偏离EA的程度。估计器采用基于影响函数的增强逆强度加权形式，利用半参数模型拟合观测数据，将数据建模与敏感性参数设定分离。该方法允许灵活建模（如使用样条或核），并通过渐近正态性构建置信区间。在一项低收入哮喘患者的随机对照试验中，作者展示了完整的实施流程和敏感性分析结果。对研究者而言，本文将纵向因果推断中的不规则评估问题与经典敏感性分析工具结合，其影响函数技术可直接迁移到研究者熟悉的因果推断估计理论框架中。
- **关键技术**: `influence function-based estimation`, `augmented inverse intensity-weighted estimator`, `exponential tilting sensitivity model`, `explainable assessment assumption`, `semiparametric modeling`, `sensitivity analysis parameter`
- **为什么对您有用**: 直接关联到主要兴趣中的因果推断频繁出现的纵向敏感性分析子方向，特别是试验中信息性失访或评估时间问题的处理。研究者在因果推断估计理论（very_familiar）和半参数理论（moderately_familiar）上已有基础，可立即理解并复现其增强逆强度加权估计器构造，评估是否可推广至更一般的因果参数。立即可做：用熟悉的非参数最小二乘和影响函数工具即可在类似模拟或应用中复现其方法，无需额外复杂武器。

### 11. [10.1093/biomtc/ujae135](https://doi.org/10.1093/biomtc/ujae135) · [arXiv](https://arxiv.org/abs/2304.05583) — Estimating marginal treatment effect in cluster randomized trials with multi-level missing outcomes
- **作者**: Chia-Rui Chang, Rui Wang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在 cluster randomized trials (CRTs) 设定下，目标是估计 marginal treatment effect，关键挑战是 outcome 在多个层级（个体、subcluster、cluster）存在 informative missingness。本文提出基于 weighted generalized estimating equations (WGEE) 的多层级 multiply robust estimator，通过在每个聚类层级建立 propensity score model for missingness 来构造权重。理论证明：只要每个层级的多重 propensity score 模型中至少一个正确设定，estimator 即具有 consistency 和 n^{-1/2}-CAN 性质；建立了 asymptotic normality 并给出方差估计。模拟研究验证了有限样本表现，应用于马达加斯加疟疾干预 CRT 数据。对您在 causal inference 的 identification 与 estimation 理论方向有直接参考价值，尤其是 missing data 与 robustness 的交叉。
- **关键技术**: `weighted generalized estimating equations`, `multiply robust estimation`, `propensity score for missingness`, `cluster randomized trials`, `multi-level missing data`, `asymptotic normality`
- **为什么对您有用**: (1) 直接连接 causal inference 中的 missing data 与 robust estimation 问题，属于您 primary interest 中 estimation theory in causal inference 的具体应用场景。(2) 您的 very_familiar 武器库中的 estimation theory in causal inference 和 moderately_familiar 中的 semiparametric theory 足以理解并推进这篇 paper 的理论分析——multiply robust 性质可用 semiparametric efficiency / influence function 视角重新审视。(3) **立即可做**：用 semiparametric efficiency bound 工具验证其 multiply robust estimator 是否达到 efficiency bound，或探索是否可构造 doubly robust / TMLE 版本以提升有限样本表现。

### 12. [10.1093/biomtc/ujae152](https://doi.org/10.1093/biomtc/ujae152) · [arXiv](https://arxiv.org/abs/2401.03268) — Adaptive randomization methods for sequential multiple assignment randomized trials (smarts) via thompson sampling
- **作者**: Peter Norwood, Marie Davidian, Eric Laber
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究响应自适应随机化（RAR）在序贯多分配随机试验（SMARTs）中的应用，目标是优化多阶段治疗规则的评估。传统SMARTs使用固定随机化比例，而RAR在单阶段试验中已被证明能改善伦理和统计性质，但在多阶段设计中研究不足。作者提出了一套基于Thompson Sampling（TS）的RAR算法，将每个阶段的随机化概率更新为当前治疗为最优的后验概率，并针对SMARTs的两种常见目标——比较嵌入的治疗规则和估计最优嵌入规则——设计了相应算法。关键贡献在于开发了考虑到RAR导致非标准渐近行为的事后推断方法（例如平均治疗效果估计量的非正态极限），这在多阶段试验中是首次。通过基于真实SMARTs的仿真研究，证实TS能改善试验中受试者的结局，同时不牺牲事后比较的效率。对您有用：这篇论文直接关联因果推断中动态治疗规则（DTR）的估计与推断，且其自适应设计思想可与您的纵向因果推断兴趣相结合。
- **关键技术**: `Thompson Sampling`, `Response-adaptive randomization`, `Sequential multiple assignment randomized trials (SMARTs)`, `Treatment regime estimation`, `Post-trial inference with nonstandard asymptotics`
- **为什么对您有用**: 本文聚焦于多阶段随机试验中的自适应随机化方法，属于因果推断中动态治疗规则估计的前沿应用，直接连接您的纵向因果推断兴趣。您非常熟悉的因果推断估计理论可用于分析Thompson Sampling对治疗效应估计的影响，尤其是检验其推断程序在有限样本下的表现。鉴于论文已给出完整算法和仿真评估，您可以立即可做：用您掌握的因果推断软件实现并验证其方法在自身研究场景中的适用性。

### 13. [10.1093/biomtc/ujae123](https://doi.org/10.1093/biomtc/ujae123) · [arXiv](https://arxiv.org/abs/2401.15680) — How to achieve model-robust inference in stepped wedge trials with model-based methods?
- **作者**: Bingkai Wang, Xueqi Wang, Fan Li
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `weaker_assumption`
- **摘要**: 本文研究 stepped wedge 设计（阶梯楔形设计）中基于模型推断的稳健性问题。在集群随机试验中，常用线性混合模型或广义估计方程（GEE）来分析处理效应，但这些方法在模型误设下的性质尚不清楚。作者定义了非参数边际处理效应（基于潜在结果，可能随时间或暴露时间变化），并证明了关键结果：只要处理效应结构被正确设定，工作模型的其余部分（协变量函数形式、随机效应、误差分布）可以误设，估计量仍保持一致；同时，通过 sandwich 方差估计可获得正确的推断。对于非恒等链接函数或比率型估计量，需要额外进行 g-computation 步骤以实现模型稳健推断。理论结果通过模拟和一项实际阶梯楔形试验的再分析加以验证。该研究为纵向集群随机试验中的稳健因果推断提供了易于实施的条件，对您感兴趣的纵向因果推断和模型误设下的推断问题有直接参考价值。
- **关键技术**: `linear mixed model`, `generalized estimating equations (GEE)`, `sandwich variance estimator`, `g-computation`, `marginal treatment effect estimand`, `potential outcomes`
- **为什么对您有用**: 直接连接到您 primary interest 中的纵向因果推断（stepped wedge 设计是典型的纵向 cluster RCT）。本文利用 sandwich 方差估计实现模型误设下的稳健推断，这与您武器库中“estimation theory in causal inference”高度匹配，可立即用您熟悉的非参数统计和 M-估计理论来评价其渐近性质。中期可做：将本文的稳健性条件推广到更复杂的处理效应结构（如时间-varying 效应），这需要提升 moderately_familiar 中的“identification theory in causal inference”以处理非参数部分的识别。

### 14. [10.1093/biomtc/ujae108](https://doi.org/10.1093/biomtc/ujae108) · [arXiv](https://arxiv.org/abs/2409.09440) — Group sequential testing of a treatment effect using a surrogate marker
- **作者**: Layla Parast, Jay Bartroff
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文在 surrogate marker 框架下，研究如何利用从 prior study 借信息的非参数检验，在后续研究中进行 group sequential treatment effect testing。设定是 surrogate marker 被重复测量多次，目标是利用 surrogate 信息提前做出 treatment effect 的统计推断，而非等待 primary outcome。核心方法是构建基于 surrogate 的非参数检验统计量序列，推导其在多个时间点的相关性结构，并计算 early stopping boundaries（包括 efficacy 和 futility stopping）。理论贡献包括证明检验统计量的渐近性质和 type I error 控制；实证部分通过模拟和两个 AIDS 临床试验数据展示方法性能。对您在因果推断中的 surrogate/mediation 设定以及假设检验理论有直接参考价值。
- **关键技术**: `group sequential testing`, `surrogate marker`, `nonparametric test`, `stopping boundaries`, `alpha spending`, `information borrowing from prior study`
- **为什么对您有用**: (1) 连接到因果推断中 surrogate/mediation 的 identification 与 estimation 问题，以及假设检验的 sequential design；(2) 您的 very_familiar 武器中 nonparametric statistics 和 estimation theory in causal inference 可直接分析其非参数检验的效率性质，moderately_familiar 中的 identification theory 可审视 surrogate 的因果可识别性假设；(3) **立即可做**：用 semiparametric efficiency 理论分析该非参数检验的效率，或探讨 surrogate validity 的 sensitivity analysis。

### 15. [10.1093/biomtc/ujae148](https://doi.org/10.1093/biomtc/ujae148) · [arXiv](https://arxiv.org/abs/2401.07767) — Estimation of a genetic Gaussian network using GWAS summary data
- **作者**: Yihe Yang, Noah Lorincz-Comi, Xiaofeng Zhu
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 针对GWAS摘要统计中多表型遗传高斯网络（遗传相关矩阵的逆矩阵）的估计问题，传统方法因估计误差和特异多效性导致遗传相关系数有偏。本文提出EGG（Estimation of Genetic Graph）方法，利用多变量孟德尔随机化（MVMR）框架，以遗传变异作为工具变量，同时消除估计误差偏差和特异多效性偏差。核心思想是将网络估计转化为MVMR中的因果效应估计问题，通过工具变量回归得到遗传协方差矩阵的无偏估计，再求逆得到网络。该方法无需个体层面数据，仅依赖GWAS摘要统计和LD参考面板，计算简便。模拟和真实数据分析显示，EGG估计的网络在边检测和一致性上显著优于传统方法（如直接求逆或阈值化）。这对您而言是一个直接的应用：您熟悉的因果推断中IV方法（孟德尔随机化）被用于高维遗传网络估计，与您对流行病学数据集的兴趣高度匹配。
- **关键技术**: `Mendelian randomization`, `instrumental variables`, `GWAS summary statistics`, `genetic correlation matrix`, `pleiotropy correction`, `multivariable MR`
- **为什么对您有用**: 本文直接连接您对因果推断中IV（孟德尔随机化）子方向的兴趣，以及流行病学应用。您对IV方法的熟悉程度（very_familiar）足以快速理解方法核心——多变量MR消除偏差的机制等价于因果推断中的工具变量识别。中期可做：若希望拓展至更复杂的网络结构（如含有隐藏变量），需先加强您在identification theory中对遗传工具变量排除限制的检验知识（moderately_familiar）。目前暂无可做：不涉及高维随机矩阵或U统计量，无需额外工具。

### 16. [10.1093/biomtc/ujae141](https://doi.org/10.1093/biomtc/ujae141) · [arXiv](https://arxiv.org/abs/2405.08180) — An adaptive enrichment design using Bayesian model averaging for selection and threshold-identification of predictive variables
- **作者**: Lara Maleyeff, Shirin Golchi, Erica E M Moodie, Marie Hudson
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对精准医学中的适应性富集设计，提出一种基于贝叶斯模型平均的方法，用于从多个候选生物标志物中识别预测变量并确定连续标志物的阈值。在模型上，采用自由结B样条灵活刻画连续生物标志物与治疗效果的复杂非线性关系，并通过贝叶斯模型平均对所有可能的变量组合进行边际化来估计关键参数。在中期分析时，根据累积数据评估定义的亚组是否具有增强或减弱的治疗效果，从而决定早期停止或后续仅招募敏感患者。模拟研究表明，该方法在操作特征（如检验效能和错误率）上优于现有方法。该设计既适用于预分类变量也适用于连续变量，为类风湿关节炎等疾病的试验提供了可实施框架。对您而言，该方法直接关联因果推断中的异质性处理效应识别，可通过非参数统计理论进一步分析其B样条估计的收敛性质。
- **关键技术**: `Bayesian model averaging`, `free knot B-splines`, `adaptive enrichment design`, `subgroup identification`, `interim analysis`
- **为什么对您有用**: 本文直接关联您的主要兴趣中因果推断的异质性处理效应识别子方向，特别是通过适应性富集在试验中动态发现治疗敏感亚组。您武器库中的非参数统计（尤其是B样条理论）可立即可用于分析其建模灵活性与估计效率，因此属于立即可做的follow-up方向。

### 17. [10.1093/biomtc/ujae155](https://doi.org/10.1093/biomtc/ujae155) · [arXiv](https://arxiv.org/abs/2402.13391) — De-biasing the bias: methods for improving disparity assessments with noisy group measurements
- **作者**: Solvejg Wastvedt, Joshua Snoke, Denis Agniel, Julie Lai, Marc N Elliott, Steven C Martino
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本方法论文致力于解决医疗决策算法公平性评估中因种族/民族信息缺失或测量误差导致的统计偏差问题。作者提出一套统计框架，允许研究者使用群体归属的概率（而非确切标签）来评估算法在不同亚组中的表现，并量化因概率误差引入的偏差。核心贡献包括推导了一组常用公平性指标（如假阳性率差异）统计偏差的理论上界，并设计了一种敏感性分析流程，允许实践者在不同假设的误差水平下评估偏差范围。方法采用基于贝叶斯的姓名与地理编码概率插补（BIFSG）作为案例，展示了在骨质疏松治疗临床决策支持算法中的实际应用。该工作连接了因果推断中的测量误差敏感度分析与算法公平性评估，对您的因果推断研究中处理代理变量误差或缺失标签的敏感度分析具有直接参考价值。理论上界的结果可用于与非参数下界技术（如 minimax 界）对比，验证其紧性。您现有的逆问题与估计理论工具可立即应用于扩展其偏差校正框架至更一般的因果参数（如条件平均处理效应）。
- **关键技术**: `sensitivity analysis`, `measurement error correction`, `imputed group probabilities`, `theoretical bias bounds`, `Bayesian imputation (BIFSG)`, `fairness metrics decomposition`
- **为什么对您有用**: 直接连接到您因果推断兴趣中的敏感度分析子方向：本文处理因群体归属概率误差导致的统计偏差，与因果推断中因未测量混杂或测量误差导致的偏倚校正问题结构相似。您技术库中'逆问题与随机噪声'和'因果推断估计理论'能够直接用于分析其偏差公式的稳健性，甚至改进其理论上界（例如利用极小极大下界检验界是否紧）。follow-up 粗判：立即可做——利用您非常熟悉的逆问题工具和因果推断估计理论，即可尝试将该偏差校正框架迁移到更一般的因果估计量（如 IPW 或 AIPW）中。

### 18. [10.1093/biomtc/ujae140](https://doi.org/10.1093/biomtc/ujae140) · [arXiv](https://arxiv.org/abs/2401.03326) — Optimal adaptive SMART designs with binary outcomes
- **作者**: Rik Ghosh, Bibhas Chakraborty, Inbal Nahum-Shani, Megan E Patrick, Palash Ghosh
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对序贯多阶段随机化试验（SMART）中的最优自适应分配问题，提出一种约束优化方法：在固定预定义目标函数（如某个治疗组间的比较）渐近方差的条件下，最小化整个试验中期望的治疗失败总数。研究设定为二元结局，每个阶段患者可能被随机分至不同治疗组，目标是实现各阶段的最优分配比例。方法的核心是通过推导目标函数的渐近方差显式表达式，构建约束优化问题，并给出最优分配比例的解析解或迭代更新公式。理论部分证明了所提分配序列的渐近最优性，并利用模拟验证了方法的有限样本表现。应用部分基于名为M-bridge的大学新生酒精风险SMART研究，展示了该方法在实际动态治疗策略设计中的可行性。对您的价值：该工作直接关联纵向因果推断中的动态治疗规则设计，您对因果推断估计理论的熟悉度（very_familiar）可迅速用于检验该方法的最优性条件或拓展至连续结局。
- **关键技术**: `sequential multiple-assignment randomized trial (SMART)`, `constrained optimization`, `optimal adaptive allocation`, `asymptotic variance constraint`, `binary outcome`, `dynamic treatment regimes`
- **为什么对您有用**: 本文聚焦于SMART设计中的自适应分配优化，属于纵向因果推断（dynamic treatment regimes）核心问题。您武器库中的“estimation theory in causal inference”可立即用于推演该方法在更复杂因果参数（如平均治疗效应或最优策略价值）下的渐近方差形式；此外，若希望将优化目标扩展至统计功效或泛化到多个比较，可借助“semiparametric theory”（moderately_familiar）进行拓展。**立即可做**：利用您对因果估计论和渐近分析的熟练度，直接复现或检验本文的最优分配公式在替代目标函数下的有效性。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 4 篇)*

### 1. [10.1093/biomtc/ujae153](https://doi.org/10.1093/biomtc/ujae153) · [arXiv](https://arxiv.org/abs/2409.07568) — Debiased high-dimensional regression calibration for errors-in-variables log-contrast models
- **作者**: Huali Zhao, Tianying Wang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文针对高维组合协变量存在测量误差的问题，在线性log-contrast模型框架下首次提出了统计推断方法。核心目标是建立存在测量污染时高维组合数据的校准估计及其渐近正态性。方法上，作者设计了一种校准策略，在参数稀疏性假设较宽松的条件下构造去偏估计量，并证明了其渐近正态分布。校准通过修正测量误差偏差，使得置信区间能够达到名义覆盖率。数值实验和微生物组实际数据分析验证了该方法在偏差减少和推断可靠性上的优势。该方法不仅适用于组合数据，还可推广至其他存在测量误差的高维回归场景。对您而言，该研究直接关联高维统计中的测量误差问题，其中的校准思想可能迁移至因果推断中利用负对照变量处理未测量混淆的设定。
- **关键技术**: `log-contrast model`, `high-dimensional calibration`, `debiased estimation`, `asymptotic normality`, `measurement error correction`
- **为什么对您有用**: 连接点：高维统计中的测量误差与校准推断，这正是您`primary_interests`中高维统计方向的一个具体子问题（测量误差下的inference）。武器库对应：您`very_familiar`中`高维渐近理论`可以直接用于理解该文渐近正态性证明的细节，并评估其稀疏假设是否可进一步放松；`非参数统计`中的minimax界也可用来分析校准估计是否达到最优收敛速度。Follow-up粗判：立即可做——您已具备在高维渐近下的技术背景，可尝试将校准思想与DML或proximal causal inference结合，或在您的药理项目中用类似方法处理协变量测量误差。

### 2. [10.1093/biomtc/ujae144](https://doi.org/10.1093/biomtc/ujae144) · [arXiv](https://arxiv.org/abs/2011.05493) — Robust and flexible learning of a high-dimensional classification rule using auxiliary outcomes
- **作者**: Muxuan Liang, Jaeyoung Park, Qing Lu, Xiang Zhong
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 该论文研究高维线性分类规则的鲁棒迁移学习问题。在多个相关结局（目标结局与辅助结局）并存时，传统多任务学习（MTL）通过最小化所有结局的平均损失函数获取共享信息，但当MTL模型错误指定时会导致目标结局的估计偏差。作者将估计偏差分解为子空间内偏差和子空间外偏差两类，提出先用MTL利用所有结局获得初始估计，再借助仅目标结局的校准步骤同时校正两类偏差。最终估计量被证明具有比仅使用单结局的估计量更低的估计误差。该方法在高维线性判别规则设定下给出了非渐近误差界，模拟和真实数据分析验证了其优势。该工作与您高维统计和利用辅助信息提高估计效率的兴趣点直接相关，其中的偏差分解思想在因果推断中利用负对照或工具变量进行偏倚校正也颇具启发。
- **关键技术**: `multi-task learning`, `bias decomposition (within-subspace/against-subspace)`, `high-dimensional linear discriminant rule`, `transfer learning via calibration`, `debiased estimation`
- **为什么对您有用**: 本文属于高维统计中结构辅助信息的迁移学习，直接对接您的 primary interest 中的高维渐近性。您熟悉的 high-dimensional asymptotics 武器可用来检验该文理论界的 tightness；同时校准步骤的去偏思路与您 moderately_familiar 的 semiparametric theory 中的去偏思想一脉相承。判断为立即可做——您的高维统计工具足以消化并评估本文假设与结果的严谨性。

### 3. [10.1093/biomtc/ujae109](https://doi.org/10.1093/biomtc/ujae109) · [arXiv](https://arxiv.org/abs/2306.05571) — Heterogeneity-aware integrative regression for ancestry-specific association studies
- **作者**: Aaron J Molstad, Yanwei Cai, Alexander P Reiner, Charles Kooperberg, Wei Sun, Li Hsu
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在 ancestry-specific PWAS（蛋白质组关联研究）设定下，目标是提升 historically underrepresented 人群（如非洲裔）的蛋白质表达预测精度，核心挑战是各 ancestry group 间样本量差异大且存在异质性。作者提出 penalized maximum likelihood estimator，通过跨 ancestry group 借信息拟合 joint pQTL 模型，同时允许 heterogeneous error variances 和 regression coefficients。关键技术包括：通过 alternative parameterization 使目标函数凸化且 penalty scale invariant；提出 approximate version 以提升计算效率并给出理论性质分析。实证结果显示非洲裔人群的蛋白质表达预测精度显著提升，下游 PWAS 发现多个新的蛋白-血脂关联。对您而言，这是高维惩罚回归在遗传流行病学中的应用实例，展示了 heterogeneity-aware 借信息策略。
- **关键技术**: `penalized maximum likelihood`, `multi-ancestry information borrowing`, `convex reparameterization`, `heterogeneous error variance`, `computational approximation`
- **为什么对您有用**: (1) 连接到高维统计中的 multi-task / transfer learning 设定，以及流行病学应用中的 ancestry-specific estimation 问题。(2) 您的 very_familiar 中的 high-dimensional asymptotics 和 software development 可用于分析其 estimator 的理论性质或优化算法实现。(3) **中期可做**：需先在 moderately_familiar 的 M-estimation theory 上补充 multi-task penalized M-estimator 的 oracle inequality / minimax rate 分析，方可深入其理论性质。

### 4. [10.1093/biomtc/ujae158](https://doi.org/10.1093/biomtc/ujae158) — Structured feature ranking for genomic marker identification accommodating multiple types of networks
- **作者**: Yeheng Ge, Tao Li, Xingdong Feng, Mengyun Wu, Hailong Liu
- **期刊/来源**: Biometrics
- **机构**: Shanghai University of Finance and Economics · Shanghai Jiao Tong University · XinHua Hospital
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `new_theory`
- **摘要**: 在高维基因组特征选择设定下，目标是识别与疾病表型相关的分子标记，同时利用预测变量之间的网络依赖结构。本文提出 structured feature ranking 方法，通过 Laplacian 正则化将先验网络和数据驱动网络融入边际重要性度量，并引入调参机制控制网络噪声和不确定性的影响。理论贡献包括建立 sure screening property，证明在正则条件下网络结构化度量比原始边际度量具有更快的收敛速率。模拟和 TCGA 黑色素瘤数据分析验证了有限样本性能的提升。对您而言，这篇论文展示了高维特征选择中网络结构正则化的理论分析框架，可作为 Laplacian 正则化在 minimax rate 分析中的具体案例。
- **关键技术**: `Laplacian regularization`, `sure screening property`, `feature ranking`, `network-structured estimation`, `high-dimensional variable selection`, `convergence rate analysis`
- **为什么对您有用**: 连接到高维统计中的特征选择与 minimax rate 分析。您熟悉的 minimax bounds for estimation problems 可用于审视其声称的 faster convergence rate 是否紧，以及 Laplacian 正则化引入的 bias-variance tradeoff。立即可做：用 very_familiar 的高维渐近理论工具验证其理论界是否可达最优。

## 非参数 / 半参数  *(nonparam_semipara, 8 篇)*

### 1. [10.1093/biomtc/ujae127](https://doi.org/10.1093/biomtc/ujae127) · [arXiv](https://arxiv.org/abs/2308.12540) — Wasserstein regression with empirical measures and density estimation for sparse data
- **作者**: Yidong Zhou, Hans-Georg Müller
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究分布回归问题，目标是在响应变量为未知分布、且各分布可用样本量高度不均衡（部分稀疏）的设定下，对条件分布及条件密度进行估计。核心方法是直接基于经验测度构建 Wasserstein 回归，跳过对每个分布单独进行密度估计的预处理步骤，从而避免了稀疏样本下密度估计不一致、带宽选择困难及边界偏差等问题。理论方面，作者证明了通过跨分布借力，即使对样本量极少的分布也能获得一致的分布估计，而传统逐个估计方法在稀疏情形下失效。实证部分通过模拟和 ECHO 环境健康数据展示了方法优于现有需要预估计分布的回归方法。对您在 semiparametric theory 和 minimax bounds 方面的兴趣有直接参考价值。
- **关键技术**: `Wasserstein regression`, `empirical measure`, `distribution regression`, `density estimation with sparse samples`, `Fréchet regression`, `optimal transport`
- **为什么对您有用**: 本文属于 semiparametric/nonparametric theory 范畴，涉及分布对象的回归估计，与您熟悉的 minimax bounds 和 nonparametric statistics 直接相关。您可以用 very_familiar 的 minimax bound 工具分析该方法在稀疏样本设定下的收敛率是否达到最优，或用 moderately_familiar 的 semiparametric theory 探讨其效率界。技术门槛适中，属于**立即可做**——核心是经典非参数回归与 Wasserstein 距离的结合，武器库完全覆盖。

### 2. [10.1093/biomtc/ujae138](https://doi.org/10.1093/biomtc/ujae138) — Large-scale survival analysis with a cure fraction
- **作者**: Bo Han, Xiaoguang Wang, Liuquan Sun
- **期刊/来源**: Biometrics
- **机构**: Yunnan University · Dalian University of Technology · Academy of Mathematics and Systems Science · University of Chinese Academy of Sciences
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究带治愈分数的大规模生存数据的半参数回归估计与推断问题，设定为 mixture cure model，其中 incidence 部分无参数假设、latency 部分采用半参数比例风险模型。核心方法是提出基于 susceptible probability 的概率加权估计方程，通过非参数估计权重实现回归参数的稳健估计。针对大规模数据，作者提出基于数据分块的递归概率加权估计方法，实现计算和内存效率。理论贡献包括建立估计量的渐近性质（一致性、渐近正态性），并通过模拟和实际数据分析验证方法表现。对您在半参数理论方面的兴趣有参考价值，尤其是估计方程方法与非参数权重估计的结合。
- **关键技术**: `mixture cure model`, `probability-weighted estimating equation`, `semiparametric proportional hazards model`, `nonparametric weight estimation`, `recursive block-based estimation`, `asymptotic normality`
- **为什么对您有用**: (1) 连接到 semiparametric theory 方向，具体是 mixture cure model 下的估计方程方法与权重估计的渐近理论。(2) 您的 very_familiar 中的 nonparametric statistics 和 moderately_familiar 中的 semiparametric theory、M-estimation theory 可直接用于审视其权重估计的收敛条件、估计方程的正则性假设是否充分，以及渐近方差的推导是否达到效率界。(3) **立即可做**：用 M-estimation theory 和 semiparametric theory 的工具可验证其理论推导的严谨性，或探索是否可构造更高效的 one-step / debiased 估计量。

### 3. [10.1093/biomtc/ujae121](https://doi.org/10.1093/biomtc/ujae121) — Modeling longitudinal skewed functional data
- **作者**: Mohammad Samsul Alam, Ana-Maria Staicu
- **期刊/来源**: Biometrics
- **机构**: Duke University · North Carolina State University
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对纵向功能数据中存在的点态偏斜问题，提出了一种新的建模框架。核心思路是将边际变化与纵向/功能依赖解耦：边际分布用参数化分布族刻画（随时间与功能参数光滑变化），依赖结构用高斯Copula与低秩近似协方差矩阵联合建模。方法既支持点态分位数估计，也能预测新时间点的完整轨迹。模拟实验和扩散张量成像（DTI）多发性硬化症真实数据验证了有效性。配套R包sLFDA已公开。该工作属于半参数功能数据建模的拓展，与您感兴趣的纵向数据分析和非参数建模有直接接口。
- **关键技术**: `copula methodology`, `low-rank covariance approximation`, `pointwise quantile estimation`, `Gaussian copula`, `longitudinal functional data`, `parametric distribution families`
- **为什么对您有用**: 连接至您非参数/半参数方向中的功能数据分析子课题。您的软件开发和非常熟悉的高维渐近能力可直接用于评估该方法的协方差低秩近似效果（例如用随机矩阵理论分析其谱性质，或设计更高效的压缩算法）。中期可做：需先在 moderately_familiar 的“半参数理论”中熟悉copula建模和功能主成分分析，即可将该框架与您的HOIF或U统计量工作结合。

### 4. [10.1093/biomtc/ujae150](https://doi.org/10.1093/biomtc/ujae150) — Time-dependent prognostic accuracy measures for recurrent event data
- **作者**: R Dey, D E Schaubel, J A Hanley, P Saha-Chaudhuri
- **期刊/来源**: Biometrics
- **机构**: McGill University · University of Pennsylvania · Biogen (United States)
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对重复事件数据（如患者多次发作的临床事件），提出一类新的时间依赖预后准确性度量，用于评估基线生物标志物随时间变化的预测能力（如灵敏度和特异度）。现有方法主要针对单次事件或假设事件独立性，本文采用半参数frailty模型，通过共享脆弱项刻画标志物的信息性和患者间未观测异质性，建立时间依赖的ROC/AUC估计量。估计方法基于部分似然或估计方程，在正则条件下证明估计量的一致性和渐近正态性，并给出方差估计。模拟研究表明估计量偏差小且覆盖概率适当，实际数据应用展示FEV1（肺功能指标）对囊性纤维化患者反复肺部加重的预测效度。该研究将半参数建模延伸至重复事件预后评价领域，与您的纵向数据分析兴趣（semiparametric and nonparametric theory）和因果推断中重复测量方法有潜在交叉。
- **关键技术**: `semiparametric frailty model`, `time-dependent ROC/AUC`, `prognostic accuracy measures`, `partial likelihood estimation`, `recurrent event data`, `asymptotic normality`
- **为什么对您有用**: (1) 直接联系到您的primary interest中的semiparametric theory和纵向数据（longitudinal）在因果推断中的设定，即frailty模型处理重复事件异质性的建模思路可迁移至因果推断中的重复测量方法。 (2) very_familiar中的'nonparametric statistics'和'estimation theory in causal inference'使其核心估计框架可解读；而 moderately_familiar中的'semiparametric theory'可用于评估该估计量的效率是否达到界，可能发现改进空间。 (3) 中期可做：需先在'moderately_familiar'的semiparametric theory上提升，以便深入分析该估计量的半参数效率或推导更优估计。

### 5. [10.1093/biomtc/ujae125](https://doi.org/10.1093/biomtc/ujae125) · [arXiv](https://arxiv.org/abs/2402.02867) — A new robust approach for the polytomous logistic regression model based on Rényi’s pseudodistances
- **作者**: Elena Castilla
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在多项 logistic 回归模型设定下，目标是构建对结果变量误分类（misclassification）具有稳健性的参数估计与假设检验方法。核心贡献是提出基于 Rényi 伪距离（Rényi's pseudodistance, RP）的 M-估计量族，通过调节参数 α ≥ 0 控制稳健性，MLE 对应 α = 0 的特例。作者建立了估计量的渐近正态性，并据此构造了 RP 型 Wald 检验统计量，证明了其在误分类污染下的稳健性质。模拟与实例分析显示，当存在误分类时，RP 估计量在偏差与 MSE 上显著优于 MLE，Wald 检验的水平与功效也更稳定。对您而言，这是 M-估计稳健性理论在分类模型中的应用，可作为 semiparametric / M-estimation 理论的具体案例阅读。
- **关键技术**: `M-estimation theory`, `Rényi divergence`, `robust estimation`, `Wald-type tests`, `misclassification model`, `asymptotic normality`
- **为什么对您有用**: 本文连接到您 primary interest 中的 semiparametric & nonparametric theory 以及 M-estimation theory（属于 moderately_familiar 武器库）。技术核心是经典的 M-估计稳健性分析，不涉及高维或效率理论，属于传统参数稳健推断范畴。**中期可做**：若想深入 robust inference 方向，需先在 moderately_familiar 的 M-estimation theory 上补充 influence function 与 breakdown point 的系统知识；但本文对您当前主攻的效率理论、高维或因果推断方向直接贡献有限。

### 6. [10.1093/biomtc/ujae136](https://doi.org/10.1093/biomtc/ujae136) · [arXiv](https://arxiv.org/abs/2312.06018) — A multivariate Polya tree model for meta-analysis with event-time distributions
- **作者**: Giovanni Poli, Elena Fountzilas, Apostolia-Maria Tsimeridou, Peter Müller
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在 meta-analysis 设定下，目标是估计多个研究特异性的 event-time 分布 $G_1, \ldots, G_n$，并引入研究层面协变量以刻画分布间的相依结构。本文将经典的 Polya tree (PT) 先验扩展为多元版本，核心机制是将 PT 构造中各层独立的 Beta 分裂概率先验替换为基于研究协变量索引的 Gaussian process (GP) 先验，从而在 logit 尺度上对相似研究的分裂概率施加更强的相关性。该构造保持了条件共轭性，后验更新解析可行，适用于常见的 event-time 数据摘要统计量（如 Kaplan-Meier 曲线、中位生存时间）。实证分析基于癌症免疫治疗研究的 meta-analysis 数据。对您而言，这是非参数贝叶斯方法在生存分析/meta-analysis 中的一个具体应用实例，方法学 novelty 属于对现有 PT 先验的扩展而非根本性新理论。
- **关键技术**: `Polya tree prior`, `Gaussian process prior`, `nonparametric Bayesian`, `meta-analysis`, `event-time data`, `conditionally conjugate updating`
- **为什么对您有用**: (1) 连接到 primary interest 中的 semiparametric and nonparametric theory，具体是 Polya tree 这一非参数贝叶斯先验的多元扩展。(2) 技术上，GP 先验引入协变量相依结构的思路与您熟悉的 semiparametric theory 中的 sieve / RKHS 方法有概念上的对应，但本文核心是贝叶斯先验构造而非 frequentist 效率界或估计理论。(3) follow-up 判定：**暂不可做**——本文属于贝叶斯非参数范畴，核心机器（Polya tree 后验计算、MCMC for GP）不在您的武器库中，且与您当前主攻的 frequentist semiparametric efficiency / higher-order U-statistics 方向技术路线差异较大。

### 7. [10.1093/biomtc/ujae113](https://doi.org/10.1093/biomtc/ujae113) · [arXiv](https://arxiv.org/abs/2310.07330) — Functional generalized canonical correlation analysis for studying multiple longitudinal variables
- **作者**: Lucas Sort, Laurent Le Brusquet, Arthur Tenenhaus
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对多个纵向变量之间的关联性分析，提出了功能广义典型相关分析（FGCCA）框架。该方法基于多块正则化广义典型相关分析，能够处理稀疏和不规则观测的纵向数据，并保持对数据结构的鲁棒性。作者证明了求解过程的单调性质，并引入贝叶斯方法估计典型成分，增强了模型的可解释性。进一步扩展了模型以整合单变量或多变量响应变量，从而支持预测性应用。模拟研究和真实纵向数据集上的案例验证了方法的有效性。该工作为多变量纵向数据的探索性分析提供了新的统计工具。对您可能有用：该方法可用于纵向因果推断前的数据探索阶段，或在流行病学纵向队列中识别多变量关联模式，与您的因果推断与流行病学兴趣相关。
- **关键技术**: `Functional generalized canonical correlation analysis`, `Multiblock regularized generalized canonical correlation analysis`, `Bayesian estimation`, `Sparsity-robust estimation`, `Monotonic property`, `Predictive extension`
- **为什么对您有用**: 本文直接关联到您感兴趣的纵向数据因果推断子方向，提供了一种多变量关联的探索性分析框架。您的技术武器库中的非参数统计可用于理解其功能数据平滑机制，例如通过核平滑或基函数逼近处理不规则观测。**中期可做**：需先在very_familiar的nonparametric statistics这一项上加深对功能数据正则化和基函数方法的熟悉，之后可将该方法用于流行病学纵向队列的预处理或因果效应估计的前置步骤。

### 8. [10.1093/biomtc/ujae134](https://doi.org/10.1093/biomtc/ujae134) — An exploratory penalized regression to identify combined effects of temporal variables—application to agri-environmental issues
- **作者**: Bénedicte Fontez, Patrice Loisel, Thierry Simonneau, Nadine Hilgert
- **期刊/来源**: Biometrics
- **机构**: Université de Montpellier · Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement · Mathématiques, Informatique et Statistique pour l'Environnement et l'Agronomie · Institut Agro Montpelier · L'Institut Agro · Laboratoire d'Ecophysiologie des Plantes sous Stress environnementaux
- **分类**: vol 80 · issue 4
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文研究两个时间序列预测变量对标量输出的联合效应识别问题，设定为函数型/时间序列回归框架，目标是获得可解释的稀疏模型。提出 SpiceFP 方法：先将两个时间变量离散化为联合类别模态，构建以联合区间频率为回归元的回归模型集合，再用 generalized fused lasso 同时进行变量选择和相邻系数融合。方法属于 exploratory sparse regression，理论贡献有限，主要展示模拟和葡萄品质数据的实证应用。对您而言，这是高维惩罚回归在农业环境数据的应用案例，方法学 novelty 较轻。
- **关键技术**: `generalized fused lasso`, `sparse regression`, `functional data discretization`, `joint modalities construction`, `penalized regression`
- **为什么对您有用**: (1) 属于 secondary interest 中农业/环境应用，方法涉及高维惩罚回归和变量选择，与您 primary interest 中的 high-dimensional statistics 有边缘重叠。(2) 技术上使用 generalized fused lasso，属于您 moderately_familiar 的 M-estimation 范畴，但核心是应用导向而非理论推进。(3) **暂不可做**：本文是应用型 exploratory 方法，缺乏您关心的 minimax rate、efficiency bound 或 sharper rate 等理论深度；若要跟进需转向惩罚回归的理论分析方向，但这不是您当前武器库的核心目标。

## 数理统计 / 假设检验  *(hypothesis_testing, 4 篇)*

### 1. [10.1093/biomtc/ujae119](https://doi.org/10.1093/biomtc/ujae119) — A formal goodness-of-fit test for spatial binary Markov random field models
- **作者**: Eva Biswas, Andee Kaplan, Mark S Kaiser, Daniel J Nordman
- **期刊/来源**: Biometrics
- **机构**: Iowa State University · Colorado State University
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对空间二值 Markov 随机场（MRF）模型提出一种正式的拟合优度检验方法。研究问题是环境与生态研究中常用的 MRF 模型缺乏有效的模型诊断工具，特别是邻域结构的设定难以评估。作者构建了一个基于条件 Moran's I 的检验统计量，该统计量利用拟合的条件概率检测模型形式（包括邻域结构）的偏离，并通过 Monte Carlo 模拟获取 p 值。数值实验表明该检验在检测邻域误设定方面具有良好功效，且对多种偏离模式敏感。文章应用于 Besag 的经典菊苣数据以及爱荷华州草雀的繁殖格局，展示了实际可用性。该检验属于似然框架下的残差型诊断，将经典 Moran's I 扩展到二值 MRF 模型的条件拟合值上。对您而言，这直接关联到假设检验方向，提供了一种将空间依赖纳入模型诊断的思路。
- **关键技术**: `conditional Moran's I`, `goodness-of-fit test`, `Markov random field`, `pseudo-likelihood`, `spatial binary data`, `Monte Carlo test`
- **为什么对您有用**: 本文直接连接到您 primary interest 中的 hypothesis testing 方向，属于模型诊断检验的方法学贡献。您武器库中的 nonparametric statistics（very_familiar）可用于分析该检验统计量的渐近性质（如经验过程视角下的极限分布），而 moderately_familiar 中的 M-estimation theory 则有助于理解伪似然估计对检验的影响。粗判为中期可做：需先在 M-estimation theory 上长肌肉，因为 MRF 的伪似然条件概率拟合属于 M 估计框架，而您目前对此不够熟悉。

### 2. [10.1093/biomtc/ujae142](https://doi.org/10.1093/biomtc/ujae142) · [arXiv](https://arxiv.org/abs/2304.10866) — Joint mirror procedure: controlling false discovery rate for identifying simultaneous signals
- **作者**: Linsui Deng, Kejun He, Xianyang Zhang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 该文聚焦于同时检验多个特征联合显著性的多重假设检验问题，典型场景包括中介分析（需要同时检验暴露-中介和中介-路径两条假设）和跨研究的可重复性分析。作者提出联合镜像程序（JM），通过迭代收缩拒绝区域，利用逐步释放的部分信息构造保守的虚假发现比例估计，从而在有限样本下控制FDR。同时引入复合FDR（cFDR），对每个虚假发现按其空组分数加权，并使用留一法（leave-one-out）证明该程序在有限样本下控制cFDR。算法可自然融入假设之间的部分顺序信息，提高效率。模拟表明，即使检验统计量在特征间存在依赖，JM仍能有效控制cFDR并提升统计功效。最后应用于真实的中介分析和可重复性分析数据，验证实用性。该方法直接服务于因果推断中的中介效应检验，与您对假设检验和因果推断的兴趣高度契合。
- **关键技术**: `Joint mirror (JM) procedure`, `Composite false discovery rate (cFDR)`, `Leave-one-out technique for FDR control`, `Iterative rejection region shrinkage`, `Partial ordering incorporation`
- **为什么对您有用**: 本文聚焦中介分析中的同时假设检验问题，直接连接您的因果推断（中介分析）和假设检验兴趣。您熟悉的非参数统计与极小极大理论可用于评估该有限样本FDR控制方法是否达到最优；您对多重假设检验的积累可让您快速理解JM程序并考虑将其扩展到其他因果检验场景（如IV的联合检验）。立即可做：您已掌握的估计理论和因果推理框架可直接用于结合该方法设计新的中介效应检验流程。

### 3. [10.1093/biomtc/ujae114](https://doi.org/10.1093/biomtc/ujae114) — Changepoint detection on daily home activity pattern: a sliced Poisson process method
- **作者**: Israel Martínez-Hernández, Rebecca Killick
- **期刊/来源**: Biometrics
- **机构**: Lancaster University
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究日常家庭活动模式中的变点检测问题，将每天的事件时间视为一个非齐次泊松过程的实现，目标是检测不同天之间的模式变化（而非天内的时间模式）。作者提出一种切片泊松过程方法，将一天分割为多个时间区间，利用局部变化信息构建似然比检验统计量，以判断序列中是否存在变点。该方法允许非齐次率函数随一天中的时间变化，并能同时处理多条观测序列。在模拟数据上评估显示，该方法能有效识别行为模式的变化，并随着时间推移可检测到潜在的健康衰退趋势。对您而言，本文展示了变点检测在活动数据中的应用，您可以用非参数统计工具（如核密度估计）改进其率函数的拟合，或推导检验的渐近性质。
- **关键技术**: `inhomogeneous Poisson process`, `sliced Poisson process`, `changepoint detection`, `likelihood ratio test`, `local change information`
- **为什么对您有用**: 本文属于假设检验中的变点检测方向，与您对 hypothesis testing 的兴趣直接相关。您熟悉的非参数统计（very_familiar）可以用于改进非齐次泊松率函数的估计，例如用核方法替代分段常数假定。立即可做：利用您掌握的 nonparametric statistics 设计适应性更强的率函数估计，并推导检验的渐近分布。

### 4. [10.1093/biomtc/ujae157](https://doi.org/10.1093/biomtc/ujae157) — Spatially adaptive variable screening in presurgical functional magnetic resonance imaging data analysis
- **作者**: Yifei Hu, Xinge Jessie Jeng
- **期刊/来源**: Biometrics
- **机构**: North Carolina State University
- **分类**: vol 80 · issue 4
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在术前fMRI数据分析中，准确划定肿瘤邻近的功能脑区至关重要，且漏检功能区域（假阴性）比误检（假阳性）对患者的危害更大。本文针对体素特异性混合模型，提出了一种新指标——贝叶斯遗漏发现率（BMDR），用于直接控制假阴性。基于BMDR，进一步设计了空间自适应变量筛选程序，利用fMRI数据的空间结构（体素邻域信息）来增强筛选能力。该方法完全数据驱动，无需人为设定阈值，且与现有假阴性控制方法不同，明确引入了空间依赖性。数值实验表明，相比多种现有方法，新方法能更有效地保留信号体素（尤其是功能区域边界的微弱信号），同时更干净地将功能区域与背景噪声分离。对于从事假设检验和高维变量筛选的研究者，本文的多重比较思路（控制FNR而非FDR）和空间自适应筛选机制具有方法学参考价值。
- **关键技术**: `Bayesian mixture model`, `missed discovery rate control`, `spatial variable screening`, `voxel-specific model`, `false negative control`
- **为什么对您有用**: 连接到您的假设检验（多重比较、FNR控制）和高维变量筛选子兴趣。您完全可以用非参数统计中的混合模型理论分析BMDR的渐近识别性质，或用高维渐近工具评估空间筛选的相合性。基于您对非参数统计和高维渐近的熟悉度，可立即从理论上审视该方法的统计保证（立即可做）。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1093/biomtc/ujae116](https://doi.org/10.1093/biomtc/ujae116) · [arXiv](https://arxiv.org/abs/2306.03663) — Bayesian inference for group-level cortical surface image-on-scalar regression with Gaussian process priors
- **作者**: Andrew S Whiteman, Timothy D Johnson, Jian Kang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 3/10 · novelty: `application`
- **摘要**: 论文针对组级神经影像回归分析中的空间正则化问题，提出一种贝叶斯空间回归模型。模型对空间变异的回归系数函数赋予高斯过程先验，并结合非平稳误差过程以实现比标准预处理平滑更数据自适应的平滑。关键计算挑战在于影像中大量像素位置，通过采用Vecchia型近似保留全空间秩，适用于广泛的空间相关函数，从而实现计算可扩展性。通过与标准逐顶点分析和几种替代方法的比较展示了模型性能。在ABCD研究的大规模儿童队列皮层表面fMRI任务对比数据上进行了实证分析。对您而言，该论文展示了如何利用计算技巧（Vecchia近似）使高维空间模型在群体水平分析中可行，与您的统计计算兴趣（数值方法、算法）直接相关。
- **关键技术**: `Gaussian process prior`, `Vecchia approximation`, `non-stationary error model`, `spatial regression`, `Bayesian hierarchical model`
- **为什么对您有用**: 本文涉及统计计算中的可扩展高斯过程近似方法，连接到您的统计计算兴趣（数值方法和算法）。您熟悉的nonparametric statistics和software development可用于理解Vecchia近似的理论性质和实现。但该论文基于全贝叶斯框架，核心推断工具（MCMC或变分推断）不在您当前武器库中，因此暂不可做；若未来需要处理高维空间数据中的计算瓶颈，可参考其近似策略。

## 流行病学  *(epidemiology, 8 篇)*

### 1. [10.1093/biomtc/ujae117](https://doi.org/10.1093/biomtc/ujae117) · [arXiv](https://arxiv.org/abs/2401.14338) — Case-crossover designs and overdispersion with application to air pollution epidemiology
- **作者**: Samuel Perreault, Gracia Y Dong, Alex Stringer, Hwashin Shin, Patrick E Brown
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究 case-crossover 设计在空气污染流行病学中的 overdispersion 问题，目标是在 conditional logistic model 框架下正确刻画响应变量的过度离散。核心方法是放松个体间独立性假设，通过引入个体间相关性显式构建 overdispersed conditional logistic model，证明其与 overdispersed conditional Poisson model 的似然等价性。技术实现采用 Bayesian 框架，通过模拟研究展示标准方法在 coverage probability 上的严重低估（可戏剧性偏离标称水平），而所提模型能正确校准。实证分析使用 Toronto 空气污染与发病率数据，显示新模型对 public holidays 等异常值更具稳健性。对您而言，这是流行病学应用中模型设定与推断有效性的具体案例，展示了似然等价性论证和 Bayesian computation 在实际数据分析中的价值。
- **关键技术**: `case-crossover design`, `conditional logistic regression`, `overdispersion modeling`, `Poisson-lognormal model`, `Bayesian inference`, `coverage probability calibration`
- **为什么对您有用**: (1) 连接到流行病学因果推断中的模型设定问题——case-crossover 是时间分层/匹配设计的核心工具，overdispersion 的正确处理直接影响置信区间和假设检验的有效性。(2) 您武器库中的 semiparametric theory 和 M-estimation theory 可用于分析该 overdispersed model 的效率性质，或发展 frequentist 视角下的稳健推断方法（当前论文仅提供 Bayesian 实现）。(3) **中期可做**：需先在 moderately_familiar 的 identification theory 上思考——overdispersion 参数在匹配设计下的可识别性条件、效率界如何计算，这是将 semiparametric efficiency 工具迁移到该场景的入口。

### 2. [10.1093/biomtc/ujae147](https://doi.org/10.1093/biomtc/ujae147) · [arXiv](https://arxiv.org/abs/2309.02430) — A likelihood approach to incorporating self-report data in HIV recency classification
- **作者**: Wenlong Yang, Danping Liu, Le Bao, Runze Li
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `application`
- **摘要**: 该论文针对HIV新发感染估计中区分近期与长期感染的难题，提出基于似然的概率分类模型。利用自我报告检测史和生物标志物数据，模型整合了两个机制：一是HIV近期感染状态如何依赖于生物标志物，二是该状态与最晚自报检测时间如何共同影响检测结果。部分个体的感染状态可依据检测史直接确定（如一年前阳性则为长期感染），其余个体的状态由模型推断。基于马拉维PHIA全国代表性样本，与逻辑回归和分类树（当前常用方法）相比，该模型参数估计偏差更小、效率更高，且对报告误差和模型误设定较稳健。对您而言：该方法学思路可直接迁移至流行病学队列中的部分可观测因果推断问题（如测量误差下的处理效应估计），且真实数据应用为您的流行病学次要兴趣提供了可复现的分析管道。
- **关键技术**: `likelihood-based classification model`, `self-report testing history`, `biomarker integration`, `missing data mechanism`, `binary classification tree comparison`
- **为什么对您有用**: 本文属于流行病学应用领域，直接对接您的secondary interest。它展示了如何利用部分可观测的自我报告数据增强分类精度——这种部分可观测结构在因果推断的sensitivity analysis或measurement error场景中常见。您武器库中的nonparametric statistics和M-estimation theory可用于分析该模型的识别条件或稳健性边界。总体而言，本文是流行病学与统计建模结合的扎实应用，值得作为入门阅读，但核心方法创新性一般，属中期可做方向（需在identification theory上提升以处理更复杂的部分观测结构）。

### 3. [10.1093/biomtc/ujae149](https://doi.org/10.1093/biomtc/ujae149) · [arXiv](https://arxiv.org/abs/2309.03714) — An efficient joint model for high dimensional longitudinal and survival data via generic association features
- **作者**: Van Tuan Nguyen, Adeline Fermanian, Antoine Barbieri, Sarah Zohar, Anne-Sophie Jannot, Simon Bussy et al.
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文提出FLASH方法，用于高维纵向数据与删失生存时间的联合建模。该方法结合共享随机效应和联合潜在类模型的思想，通过正则化（Lasso）自动筛选重要的预后纵向特征，适用于个性化医疗等场景。估计采用EM算法，并设计了高效实现，计算速度比现有方法快数个数量级。在蒙特卡洛模拟和公开医疗数据集上，FLASH的实时预测C-index显著优于已有联合模型，且自动识别出临床相关的特征，保证了解释性。对您而言，这是一篇高质量的流行病学应用论文，清晰展示了高维纵向数据建模的计算挑战和实际解决方案。
- **关键技术**: `Joint modeling`, `Shared random effects`, `Regularization (Lasso)`, `EM algorithm`, `High-dimensional feature selection`
- **为什么对您有用**: 本文属于流行病学领域的实际数据应用，您的 secondary interest 中包含流行病学（应用、因果推断）。论文中高维纵向数据的正则化估计与您 very_familiar 的高维渐近知识直接对接，您可以用 minimax 视角评估其变量选择的理论性质；同时其高效的 EM 实现可作为统计计算（软件 development）的参照。该文是进入流行病学数据建模的优质入门读物，武器库足以理解并批判其方法，值得花时间阅读全文以获取真实数据模式。

### 4. [10.1093/biomtc/ujae151](https://doi.org/10.1093/biomtc/ujae151) · [arXiv](https://arxiv.org/abs/2210.11107) — Graphical model inference with external network data
- **作者**: Jack Jewson, Li Li, Laura Battaglia, Stephen Hansen, David Rossell, Piotr Zwiernik
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对图模型推断中样本量相对参数数不足的问题，提出利用外部网络数据（如社交媒体网络）来改进偏相关估计和模型可解释性。方法核心是建立 spike-and-slab 先验框架，将边概率、平均偏相关及其方差回归到网络特征上，从而检测网络数据是否与图模型相关并量化其影响。计算上开发了 R 包和概率编程语言实现，便于实际推广。在 COVID-19 疫情在美国各县的社交媒体与疫情共进化数据中展示应用，发现整合网络数据能提高统计精度、模型可解释性和样本外预测能力。对您而言，这是一篇将外部结构信息引入高维图模型的流行病学应用，技术弹药库中的非参数统计和软件工具可助您快速复现并拓展其贝叶斯框架至其他纵向因果推断场景。
- **关键技术**: `spike-and-slab prior`, `partial correlation regression`, `external network integration`, `Bayesian graphical model`, `probabilistic programming implementation`
- **为什么对您有用**: 本文属于流行病学应用（COVID-19 数据），与您的 secondary interests 中的流行病学因果推断方向直接相连。您非常熟悉的软件开发和贝叶斯计算方法可以用于复现并扩展其 R 包，中期可考虑将其外部网络整合思路嫁接到您正在关注的 proximal causal inference 或 longitudinal 设定中（需要先补充图模型与网络回归的 moderately_familiar 知识）。整体而言，本文是值得全文阅读的实用方法论文，能帮您了解如何利用外部网络数据改进高维图模型推断。

### 5. [10.1093/biomtc/ujae120](https://doi.org/10.1093/biomtc/ujae120) — Likelihood adaptively incorporated external aggregate information with uncertainty for survival data
- **作者**: Ziqi Chen, Yu Shen, Jing Qin, Jing Ning
- **期刊/来源**: Biometrics
- **机构**: East China Normal University · The University of Texas MD Anderson Cancer Center · National Institute of Allergy and Infectious Diseases
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 针对罕见癌症亚型中主队列样本量不足的问题，提出一种外部知情的似然方法，以整合癌症登记数据库中的汇总生存信息（如总体生存率或中位生存时间），同时显式建模该汇总统计量的抽样变异性。方法通过构造联合似然函数连接主队列个体数据与外部汇总数据，利用经验似然或剖面似然处理外部信息的不确定性，并借助正则化或加权策略避免过度借力。在比例风险模型或加速失效时间模型框架下建立估计的相合性与渐近正态性，推导出整合后估计量的方差表达式，证明在外部数据变异性不可忽略时仍保持正确的覆盖概率。模拟研究表明该方法相比忽略外部变异性的朴素整合方法具有更好的区间覆盖率，且当外部样本量较小时优势更明显。应用部分利用MD Anderson癌症中心的炎性乳腺癌队列数据与国家癌症数据库的汇总生存数据，评估了三模式治疗对不同肿瘤亚型生存效果的影响。本文的方法论与您对流行病学中真实数据整合应用（secondary interest）直接相关，其似然整合外部信息的思想可类比于因果推断中的外部对照借用策略，但需先熟悉生存数据中部分似然的处理。
- **关键技术**: `external aggregate data integration`, `empirical likelihood`, `profile likelihood`, `survival analysis`, `uncertainty quantification`, `information borrowing`
- **为什么对您有用**: 本文属于流行病学中利用外部汇总数据提高估计效率的应用型方法工作，直接对应您的secondary interest。技术层面，其似然框架下处理外部信息变异性的思路可以借用您对'estimation theory in causal inference'（very_familiar）中正交性和效率损失的理解来评估该方法的渐近有效性；但具体实现依赖于生存分析的partial likelihood与经验似然机制，这些不在您当前核心武器库中，因此属于**中期可做**——需要先在'semiparametric theory'（moderately_familiar）上深化对剖面似然和外部数据borrowing的认识。

### 6. [10.1093/biomtc/ujae122](https://doi.org/10.1093/biomtc/ujae122) · [arXiv](https://arxiv.org/abs/2310.01575) — Derivation of outcome-dependent dietary patterns for low-income women obtained from survey data using a supervised weighted overfitted latent class analysis
- **作者**: Stephanie M Wu, Matthew R Williams, Terrance D Savitsky, Briana J K Stephenson
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对低收入女性饮食质量与高血压的关系，提出了一种监督加权过拟合潜类分析（SWOLCA）方法。该方法将调查抽样权重纳入贝叶斯伪似然框架，以校正复杂调查设计（分层、整群、信息性抽样）导致的偏差和选择性问题。模型通过马尔可夫链蒙特卡洛吉布斯抽样估计结局依赖的饮食模式，并允许通过交互项纳入效应修饰因素。模拟研究显示，SWOLCA在偏差、精度和区间覆盖方面表现良好。利用NHANES 2015-2018数据，该方法成功识别出与高血压结局相关的饮食模式，展示了实际应用价值。对您而言，本文是流行病学中处理调查数据的实用性方法案例，展示了如何在监督聚类中整合复杂设计，与您的次要兴趣“流行病学”直接相关。
- **关键技术**: `Bayesian latent class analysis`, `pseudo-likelihood`, `survey weights`, `MCMC Gibbs sampling`, `supervised clustering`, `overfitted latent class`
- **为什么对您有用**: 本文直接连接您的次要兴趣“流行病学”，提供了整合调查权重的监督聚类框架，可用于营养流行病学数据分析。作为一篇方法论驱动的应用论文，它展示了如何在复杂抽样设计下定义结局相关的潜在模式。不过，其核心工具（贝叶斯潜类模型、伪似然MCMC）不在您的武器库核心方向（如因果推断、高维统计、U-统计量），因此暂不可直接复用；但可作为流行病学方法入门阅读，帮助您理解调查数据分析中的常见偏差来源及加权策略，为未来合作奠定基础。

### 7. [10.1093/biomtc/ujae146](https://doi.org/10.1093/biomtc/ujae146) · [arXiv](https://arxiv.org/abs/2402.00077) — Unlocking the power of multi-institutional data: Integrating and harmonizing genomic data across institutions
- **作者**: Yuan Chen, Ronglai Shen, Xiwen Feng, Katherine Panageas
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `application`
- **摘要**: 研究问题是在多中心基因组数据整合中，如何处理不同机构基因面板差异、测序技术异质性以及高维稀疏突变模式带来的挑战。目标是从异质数据中提取 harmonized latent features 用于下游生存预测。作者提出 Bridge 模型，采用 quantile-matched latent variable approach，通过分位数匹配将各机构的基因突变数据映射到共享的潜在空间，在保留非共有基因信息的同时实现信息共享与降噪。方法核心是降维后的 latent variable extraction，结合跨机构的信息共享机制提升估计效率和泛化能力。模拟研究表明参数估计和特征提取表现稳健，在 GENIE BPC 六种癌症类型的真实数据上，提取的潜在特征在生存预测中表现优异。对您而言，这是流行病学/肿瘤数据应用方向的 paper，方法学 novelty 有限（latent variable + quantile matching 的组合），但数据集和 pipeline 可作为多中心数据整合的案例参考。
- **关键技术**: `quantile-matched latent variable model`, `multi-institutional data harmonization`, `dimension reduction`, `information sharing across institutions`, `survival prediction`
- **为什么对您有用**: (1) 属于 epidemiology 方向的应用 paper，涉及真实多中心肿瘤基因组数据整合与生存分析；(2) 方法学上主要是 latent variable model + quantile matching 的组合，novelty 有限，对您 primary interests（causal inference / efficiency theory / semiparametric theory）的直接技术迁移价值不高；(3) 作为 gateway reading：数据整合挑战的描述清晰，但方法学深度不足以支撑进入新方向，建议快速浏览 abstract 后决定是否需要看细节。

### 8. [10.1093/biomtc/ujae130](https://doi.org/10.1093/biomtc/ujae130) · [arXiv](https://arxiv.org/abs/2310.03164) — A hierarchical random effects state-space model for modeling brain activities from electroencephalogram data
- **作者**: Xingche Guo, Bin Yang, Ji Meng Loh, Qinxia Wang, Yuanjia Wang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文针对多通道静息态脑电图(EEG)信号分析中的异质性和非平稳性问题，提出了一种层次随机效应状态空间模型(RESSM)。模型通过引入时间和空间映射矩阵的多水平随机效应，刻画个体和群组间脑连接性的异质性，并允许其随时间变化。在贝叶斯层次框架下，采用吉布斯采样进行模型拟合，避免了传统混合效应状态空间模型中对随机效应施加的结构约束，同时处理了高维随机效应矩阵的可识别性挑战。模拟研究表明模型估计和推断有效。将该模型应用于一项多中心重度抑郁障碍(MDD)临床试验，发现MDD患者与健康个体在静息态脑时间动态上存在显著差异。此外，从RESSM导出的个体水平EEG特征在预测异质性治疗效果方面优于传统的EEG频带功率，提示EEG可能成为MDD的潜在生物标志物。该论文对于您在流行病学纵向数据建模（如生物标志物与治疗效应的关联）方面具有参考价值。
- **关键技术**: `state-space model`, `random effects model`, `Bayesian hierarchical modeling`, `Gibbs sampler`, `identifiability of high-dimensional random effects`, `EEG signal processing`
- **为什么对您有用**: 该论文是流行病学（脑电图生物标志物与抑郁治疗效应）的典型应用案例，适合作为入门读物了解如何将状态空间模型应用于纵向神经生理数据。您的武器库中的非参数统计与高维渐近理论可以支撑对该模型识别性假设的理论检验，但当前缺少贝叶斯层次模型和MCMC计算的经验。总体上值得通读全文，以掌握临床EEG数据的分析流程和建模思路，但短期内难以直接迁移到您的主研究方向。

## 其他  *(other, 9 篇)*

### 1. [10.1093/biomtc/ujae118](https://doi.org/10.1093/biomtc/ujae118) — Leveraging information from secondary endpoints to enhance dynamic borrowing across subpopulations
- **作者**: Jack M Wolf, David M Vock, Xianghua Luo, Dorothy K Hatsukami, F Joseph McClernon, Joseph S Koopmeiners
- **期刊/来源**: Biometrics
- **机构**: University of Minnesota · Duke University
- **分类**: vol 80 · issue 4
- 相关性 6/10 · novelty: `application`
- **摘要**: 在随机对照试验的子人群治疗效果估计问题中，目标是在保证 identification 的前提下，通过跨子人群借力提高估计精度。本文提出 multisource exchangeability model (MEM) 的扩展方法，利用次要终点信息辅助判断子人群间的可交换性，从而更高效地进行动态借力。核心机制是贝叶斯分层模型框架下的 exchangeability prior，通过联合建模 primary 和 secondary endpoints 来 sharpen borrowing strength 的决策。理论贡献方面，文章通过模拟研究展示了 MSE 的降低和有效样本量的提升（2-4 倍），但未给出严格的频率学派收敛率或 semiparametric efficiency bound。实证分析使用了低尼古丁香烟戒烟试验数据，展示了方法在三个优先子人群中的应用。对您而言，这是一篇应用导向的贝叶斯动态借力方法论文，方法学 novelty 有限。
- **关键技术**: `multisource exchangeability model (MEM)`, `dynamic borrowing`, `Bayesian hierarchical model`, `basket trial design`, `secondary endpoint integration`, `exchangeability prior`
- **为什么对您有用**: (1) 属于 gateway-reading 范畴（epidemiology 应用），但方法学深度较浅，主要是贝叶斯分层模型的应用，与您 primary interest 中的 semiparametric efficiency、debiasing 等理论工具无直接交集。(2) 武器库中的 semiparametric theory 和 minimax bounds 无法直接攻这篇 paper——它走的是贝叶斯路线，没有 influence function 或效率界的问题意识。(3) 暂不可做/不值得深读：核心机器（贝叶斯动态借力、exchangeability prior 的理论性质）不在您的武器库里，且该方向与您当前主攻的高维推断、因果 identification 理论距离较远，除非您有意进入 basket trial 设计领域。

### 2. [10.1093/biomtc/ujae128](https://doi.org/10.1093/biomtc/ujae128) · [arXiv](https://arxiv.org/abs/1910.12210) — Robust model averaging approach by Mallows-type criterion
- **作者**: Miaomiao Wang, Kang You, Lixing Zhu, Guohua Zou
- **期刊/来源**: Biometrics
- **机构**: Chinese Academy of Sciences · Academy of Mathematics and Systems Science
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 针对传统模型平均方法（如基于OLS或ML的Mallows准则）对离群值和模型假设偏离高度敏感的问题，本文提出一种鲁棒模型平均方法。核心思路是：对每个候选模型构造广义M (GM) 估计量，并基于GM型损失函数的最终预测误差渐近展开来构建鲁棒权重。在正则条件下，证明了权重估计量渐近收敛到理论最优权重，且模型平均估计量的影响函数有界，从而具备定量鲁棒性。进一步定义了经验预测影响函数以评估稳健性。模拟和真实数据分析展示了有限样本下的优势。对您而言，本文的M估计和影响函数理论与您兵器库中moderately_familiar的M-estimation theory直接对口，您可将该鲁棒化策略迁移到因果推断中处理离群值或模型不确定性。
- **关键技术**: `model averaging`, `Mallows criterion`, `generalized M-estimator (GM)`, `influence function`, `bounded influence estimation`, `robust regression`
- **为什么对您有用**: 本文属于M估计理论的直接应用，与您moderately_familiar的M-estimation theory完全对应，您已有的非参数统计和估计理论可帮助理解其渐近论证。中期可做：需先熟悉GM估计的具体构造和影响函数推导，但M估计基础已具备，可将此鲁棒模型平均思路引入因果推断中的模型平均（如IV估计或倾向得分模型选择），以增强对离群值的稳健性。

### 3. [10.1093/biomtc/ujae111](https://doi.org/10.1093/biomtc/ujae111) · [arXiv](https://arxiv.org/abs/2407.05089) — Bayesian network-guided sparse regression with flexible varying effects
- **作者**: Yangfan Ren, Christine B Peterson, Marina Vannucci
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出 VERGE，一种贝叶斯变系数回归方法，同时进行特征选择和网络估计。模型区分预测变量（如微生物 OTU）和受试者水平协变量（如性别、饮食），允许协变量调节预测变量对结局的效应，形成变系数结构。采用 spike-and-slab 先验实现变量选择，并利用推断的预测变量网络鼓励选择网络相连的特征。通过模拟研究显示，VERGE 在特征选择和预测精度上优于 Lasso、贝叶斯组套索等对比方法。实际应用分析肠道微生物组对肥胖的影响，识别出一组微生物类群及其生态依赖关系，并发现性别和膳食摄入对微生物—肥胖关系的调节作用。该方法属于应用统计开发，未涉及因果识别或反事实框架，主要为预测建模和关联分析。对于您，变系数框架类似于因果推断中的条件平均处理效应（CATE）建模，但本文未使用潜在结果或工具变量等因果工具，实用性有限。
- **关键技术**: `Bayesian varying coefficients`, `spike-and-slab prior`, `network-guided feature selection`, `MCMC sampling`
- **为什么对您有用**: (1) 本文的变系数回归框架与 causal inference 中处理效应异质性（CATE）建模在形式上类似，可作为入门参考。(2) 您可以用 high-dimensional asymptotics 中的稀疏性理论来评估该方法变量选择的一致性，但贝叶斯先验和 MCMC 计算不在您的技术 arsenal 内，难以直接迁移。(3) follow-up 暂不可做：核心机器是贝叶斯 MCMC 和 spike-and-slab 先验，您目前缺乏这些工具（若想跟随需先掌握贝叶斯变量选择计算）。

### 4. [10.1093/biomtc/ujae105](https://doi.org/10.1093/biomtc/ujae105) · [arXiv](https://arxiv.org/abs/2408.15502) — ROMI: a randomized two-stage basket trial design to optimize doses for multiple indications
- **作者**: Shuqi Wang, Peter F Thall, Kentaro Takeda, Ying Yuan
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出ROMI设计，一种随机两阶段篮式试验，用于在多个适应证中优化剂量。第一阶段评估高剂量（如先前确定的最大耐受剂量）的安全性和有效性，若不可接受则停止该适应证；第二阶段将患者随机分配至高剂量或指定低剂量。采用潜在聚类贝叶斯分层模型在适应证间借用信息，同时允许适应证间最优生物剂量（OBD）存在异质性。使用适应证特定的效用函数量化响应-毒性权衡，最终选择后验平均效用最高的剂量作为最优剂量。模拟表明ROMI在操作特性上优于忽略适应证或独立优化剂量的设计。该方法主要属于贝叶斯试验设计领域，与研究者主要关注的因果推断、高维统计、半参数效率等方向无直接交集。
- **关键技术**: `Bayesian hierarchical model`, `latent clustering`, `utility-based dose optimization`, `two-stage basket trial`
- **为什么对您有用**: 本文属于流行病学/医学统计领域的临床试验设计方法。研究者对流行病学有次要兴趣，但本文方法（贝叶斯分层模型、效用决策）不在研究者熟悉或中等熟悉的武器库（如树宽张量收缩、最小最大界、半参数效率界）中。论文仅提供模拟而非真实数据，且未使用因果推断工具，因此作为流行病学入门读物的价值有限。结论：暂不可做后续研究，核心机器（贝叶斯分层模型与决策理论）当前不在武器库中。

### 5. [10.1093/biomtc/ujae137](https://doi.org/10.1093/biomtc/ujae137) · [arXiv](https://arxiv.org/abs/2308.14520) — Cumulative link mixed-effects models in the service of remote sensing crop progress monitoring
- **作者**: Ioannis Oikonomidis, Samis Trevezas
- **期刊/来源**: Biometrics
- **机构**: National and Kapodistrian University of Athens
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `application`
- **摘要**: 该论文提出一种创新的累积连接模型（CLM）方法来利用遥感数据监测大面积作物生长进程。模型分为固定效应CLM和包含年际随机效应的混合效应CLM，以捕捉季节间变异。推断基于部分似然函数，有标准多项分布和新型乘积二项分布两种形式。模型在玉米、大豆等八种作物上使用来自内布拉斯加州20年的实地数据评估，利用日历时间、热时间及归一化植被指数作为预测因子。结果表明该方法可广泛应用于不同作物，提供大规模生长进程预测并估计重要农学参数。为促进可重复性，作者开发了公开的R包生态系统'Ages of Man'。该论文是统计计算在农业遥感中的一个扎实应用，其R包开发和模型实现可为统计软件开发者提供参考。
- **关键技术**: `cumulative link model`, `mixed-effects model`, `partial likelihood`, `product binomial distribution`, `R package development`
- **为什么对您有用**: 该论文与你的统计计算（软件工具开发）这一主要兴趣直接相关——你'very_familiar'中的'软件开发'技能可用来审视其R包设计思路和代码结构，学习其模型复现的最佳实践。本文属于应用型工作，方法是经典序数回归与随机效应的结合，适合作为入门级阅读了解农学纵向数据的建模套路，但不涉及因果推断、高维或半参理论等核心领域。整体而言，是一篇中等匹配的实践性论文。

### 6. [10.1093/biomtc/ujae115](https://doi.org/10.1093/biomtc/ujae115) — Temporal generative models for learning heterogeneous group dynamics of ecological momentary assessment data
- **作者**: Soohyun Kim, Young-geun Kim, Yuanjia Wang
- **期刊/来源**: Biometrics
- **机构**: Columbia University · Columbia University Irving Medical Center
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究生态瞬时评估（EMA）数据中的异质性群体动态建模问题，目标是在高维、相关、层次结构的时间序列数据下识别潜在的群体分组及其驱动因素。作者提出 HDRBM（Heterogeneous Dynamic Restricted Boltzmann Machine），在 RTRBM 的生成式神经网络框架中引入协变量来参数化群体归属概率，从而同时学习多个潜在群体的动态模式。方法核心是利用 RTRBM 的时序生成能力，通过协变量条件的多项式分配实现群体异质性建模，并采用对比散度（contrastive divergence）进行参数估计。模拟实验显示 HDRBM 在群体识别准确率和预测性能上优于标准 RTRBM 和混合效应模型；真实数据分析展示了其在精准精神病学中的应用潜力。对您而言，本文属于统计计算与神经概率生成模型的交叉，可关注其计算架构而非理论深度。
- **关键技术**: `Restricted Boltzmann Machine`, `recurrent temporal RBM`, `contrastive divergence`, `generative modeling`, `mixture model with covariates`, `ecological momentary assessment`
- **为什么对您有用**: (1) 本文属于 gateway reading 范畴，涉及统计计算中的神经概率生成模型，与您 primary interest 中的 statistical computing 有一定关联。(2) 武器库中的软件开发经验可帮助理解实现细节，但核心机器（RBM 的理论性质、对比散度收敛性）不在您的 familiar 范围内。(3) 作为入门读物尚可，但理论深度有限——缺乏对估计量渐近性质、收敛率或效率界的讨论，不值得花时间精读全文。

### 7. [10.1093/biomtc/ujae131](https://doi.org/10.1093/biomtc/ujae131) · [arXiv](https://arxiv.org/abs/2307.02781) — Dynamic factor analysis with dependent Gaussian processes for high-dimensional gene expression trajectories
- **作者**: Jiachen Cai, Robert J B Goudie, Colin Starr, Brian D M Tom
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出一种贝叶斯方法，针对高维纵向基因表达数据，利用依赖高斯过程（DGP）刻画不同生物通路之间的相关性，并通过贝叶斯稀疏因子分析将观测到的基因表达轨迹映射到低维潜在通路轨迹。首次在纵向数据中放松了经典独立因子假设，能够更灵活地建模通路间的交互。拟合算法采用蒙特卡洛期望最大化（MCEM），可结合标准MCMC采样器与GPFDA包获取DGP超参数的极大似然估计，模块化设计便于推广至其他含DGP的复杂模型。模拟和真实数据分析表明，该方法在恢复通路轨迹形状、揭示基因-通路关系、预测基因表达（点估计更准、预测区间更窄）方面均优于现有方法。配套R包DGP4LCF已发布在CRAN。本文虽不直接涉及因果推断，但其纵向高维数据降维与依赖结构建模的思路，对流行病学研究中基因表达轨迹分析有一定参考价值。
- **关键技术**: `dependent Gaussian processes`, `Bayesian sparse factor analysis`, `Monte Carlo expectation maximization`, `Markov Chain Monte Carlo`, `longitudinal data modeling`
- **为什么对您有用**: 本文属于流行病学领域的基因表达轨迹分析应用，可连接副兴趣中的流行病学数据集与建模。技术层面，研究者熟悉的非参数统计（高斯过程）和高维渐近可用于评价因子模型的可识别性与收敛性，但核心MCMC计算工具不在非常熟悉列表中，属于中期可做的方向——需要先掌握贝叶斯计算与MCMC诊断技巧。

### 8. [10.1093/biomtc/ujae107](https://doi.org/10.1093/biomtc/ujae107) · [arXiv](https://arxiv.org/abs/2311.01341) — Composite dyadic models for spatio-temporal data
- **作者**: Michael R Schwob, Mevin B Hooten, Vagheesh Narasimhan
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 3/10 · novelty: `application`
- **摘要**: 在景观遗传学设定下，目标是推断控制种群基因流动的空间机制，现有方法无法处理时间依赖且计算代价高。作者提出 Bayesian hierarchical dyadic model，通过构建全连接网络刻画时空数据，并使用 normalized composite likelihood 处理时空依赖结构。方法在计算上可扩展至大规模数据集，应用于青铜时代欧洲古人类 DNA 数据推断人类迁移机制。本文属于应用导向的方法论文献，核心 novelty 在于将 composite likelihood 与 dyadic model 结合以处理时空依赖，理论深度有限。对您而言，这是流行病学/遗传学领域的应用案例，方法学创新程度较低。
- **关键技术**: `Bayesian hierarchical model`, `composite likelihood`, `dyadic data model`, `spatio-temporal dependence`
- **为什么对您有用**: 本文属于流行病学/遗传学应用范畴，使用 Bayesian hierarchical 和 composite likelihood 处理时空依赖数据。对您 primary interest 中的因果推断、高维统计、效率理论等方向无直接方法学贡献；技术武器库中的 semiparametric theory、higher-order U-statistics 等在此无施展空间。作为应用案例可了解时空数据的建模思路，但无需深入阅读——立即可判断为低优先级。

### 9. [10.1093/biomtc/ujae124](https://doi.org/10.1093/biomtc/ujae124) · [arXiv](https://arxiv.org/abs/2410.22675) — Clustering computer mouse tracking data with informed hierarchical shrinkage partition priors
- **作者**: Ziyi Song, Weining Shen, Marina Vannucci, Alexandria Baldizon, Paul M Cinciripini, Francesco Versace et al.
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 4
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对计算机鼠标追踪数据中的受试者聚类问题，提出了一种分层收缩划分（HSP）先验模型。该模型在贝叶斯非参数框架下同时聚类受试者和实验条件，允许不同受试者群体内的条件划分存在差异（而非强制完全相同）。HSP模型区别于传统双聚类方法——后者要求受试者组内的条件划分恒等——也不同于现有嵌套聚类方法（基于参数共享定义群体）。模型通过MCMC进行后验推断，可灵活融入关于受试者或条件划分的先验信息。在模拟研究和实际鼠标追踪数据（来自一项神经科学先导实验）中，HSP有效识别出不同的行为模式群体。虽然该工作不直接涉及您的主要研究方向（因果推断、高维统计等），但聚类方法在异质性处理效应分析和个体化干预中具有潜在价值，其分层嵌套思路可启发因果推断中的子组识别问题。
- **关键技术**: `Hierarchical shrinkage partition (HSP) prior`, `Bayesian nonparametric clustering`, `Biclustering (subjects and conditions)`, `Nested partitions`, `Markov chain Monte Carlo (MCMC)`
- **为什么对您有用**: 本文属于贝叶斯聚类方法应用，不与您的主要研究方向（因果推断、高维统计、U统计）直接重合。但聚类问题在因果异质性分析（如潜在类别分析识别处理效应子组）中有潜在交叉。您的技术武器库中“非参数统计”可用于评估模型灵活性，但核心建模和计算工具（贝叶斯分层模型、MCMC）不在当前武器库中，暂不可做后续研究。可作为方法学拓展阅读，了解跨领域聚类思路。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

