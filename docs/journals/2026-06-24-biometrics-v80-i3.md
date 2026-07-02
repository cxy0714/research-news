# Biometrics — Vol 80  Issue 3  ·  2026-06-24

- 共 39 篇 · Biometrics
- 目录核对 ⚠️ 疑似漏 2 篇（对照 OpenAlex 45 篇）：10.1093/biomtc/ujae077、10.1093/biomtc/ujae102

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期文章主要围绕**因果推断方法与理论**、**高维统计与假设检验**、以及**半参数/非参数建模**三条主线展开，同时在流行病学应用与统计计算方面有若干延伸。因果推断主线阵容最强，涵盖中介分析、生存分析、纵向数据、图模型及元分析等多个细分场景；高维与检验主线侧重于变量选择后的推断、FDR控制及混合模型估计；半参数与非参数工作则聚焦于诊断试验、剂量反应及时空点过程的效率与稳健性。

**因果推断**方向本期推进甚多，核心关注点在于**复杂设计下的识别与效率**。针对生存数据，*Propensity weighting plus adjustment...* 一文澄清了比例风险模型下倾向得分加权与Cox回归组合并不具备双重稳健性，并提出了替代方案；针对纵向观察性研究，*Multiply robust estimation of marginal structural models...* 在协变量驱动观测时间的设定下构造了乘法稳健估计量，*Causal inference using multivariate generalized linear mixed-effects models* 则通过联合建模处理动态治疗方案下的未测量混杂。另一条支线关注**高维与结构学习**：*Controlling false discovery rate for mediator selection...* 将Knockoff方法引入高维中介选择以控制FDR，*Joint structure learning and causal effect estimation...* 利用RJMCMC实现DAG结构学习与效应估计的联合推断。此外，*Causal meta-analysis...* 提出FLEXOR加权解决多队列元分析的协变量平衡问题。

**高维统计与假设检验**方向，重点在于**高维设定下的推断与计算效率**。*High-dimensional multivariate analysis of variance...* 基于几何中位数构造了组间位置检验统计量，配合wild bootstrap解决$p \gg n$下的检验问题。*Post-selection inference in regression models for group testing data* 将选择后推断框架拓展至群体检测数据的逻辑回归，利用polyhedral lemma校正选择偏差。*Summary statistics knockoffs inference...* 则在仅有摘要统计量的场景下实现了FWER控制。计算与估计方面，*Leveraging independence in high-dimensional mixed linear regression* 利用预测变量与混合成分的独立性假设加速EM算法，*Reduced-rank clustered coefficient regression...* 通过低秩结构与融合惩罚解决异质性系数估计中的多重共线性问题。

**半参数与非参数方法**侧重于**诊断与剂量反应中的稳健识别**。*Nonparametric receiver operating characteristic curve analysis...* 在金标准不完美时证明了ROC曲线的可识别性并提出了非参数估计策略。*Semi-parametric benchmark dose analysis...* 利用单调可加模型与penalized B-splines估计基准剂量，构造了近似的pivot进行推断。*Nonparametric second-order estimation for spatiotemporal point patterns* 放弃了时空平稳性假设，提出了更灵活的二阶估计量。

总体来看，关注**因果推断效率理论**的读者可优先阅读关于乘法稳健估计与双重稳健性讨论的文章；关注**高维假设检验与选择后推断**的读者可关注基于Knockoff与几何中位数的几篇工作；**半参数效率与识别**的相关讨论则散见于诊断试验与基准剂量分析的文章中。

## 因果推断  *(causal_inference, 11 篇)*

### 1. [10.1093/biomtc/ujae099](https://doi.org/10.1093/biomtc/ujae099) — A Bayesian nonparametric approach for causal mediation with a post-treatment confounder
- **作者**: Woojung Bae, Michael J Daniels, Michael G Perri
- **期刊/来源**: Biometrics
- **机构**: University of Florida · University of Florida Health
- **分类**: vol 80 · issue 3
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文研究存在 post-treatment confounder 时因果中介效应的识别与估计问题，目标参数为自然直接效应 (NDE) 和自然间接效应 (NIE)。识别策略采用 Hong et al. 提出的扩展序贯可忽略性假设，并辅以 Gaussian copula 模型假设以保证可识别性。估计方法使用 enriched Dirichlet process mixture (EDPM) 对观测数据的联合分布进行贝叶斯非参数建模，通过 data augmentation 处理缺失数据。模拟研究显示方法在有限样本下表现良好，应用于 Rural LITE 试验数据时未发现中介效应的强证据。对您而言，这是 mediation 分析中处理 post-treatment confounding 的一个具体方案，涉及 semiparametric identification 与非参数贝叶斯估计。
- **关键技术**: `causal mediation analysis`, `post-treatment confounder`, `extended sequential ignorability`, `enriched Dirichlet process mixture`, `Gaussian copula`, `Bayesian nonparametric estimation`
- **为什么对您有用**: 直接连接到 primary interest 中的 mediation 分析，特别是 post-treatment confounder 这一经典难题。从 technical_arsenal 角度，您可以用 semiparametric theory / identification theory 的工具审视其 identification 假设的强弱，或用 efficiency theory 探讨 NDE/NIE 的 semiparametric efficiency bound 是否可达。**中期可做**：若想深入，需先在 moderately_familiar 的 semiparametric theory 上补充 Bayesian nonparametric 的 posterior contraction rate 相关知识，才能评判 EDPM 在此问题上的理论性质。

### 2. [10.1093/biomtc/ujae100](https://doi.org/10.1093/biomtc/ujae100) · [arXiv](https://arxiv.org/abs/2303.02201) — Causal inference using multivariate generalized linear mixed-effects models
- **作者**: Yizhen Xu, Ji Soo Kim, Laura K Hummers, Ami A Shah, Scott L Zeger
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文关注动态治疗方案下因果效应的个体化预测，具体设定为纵向观察性研究中，治疗随时间改变，存在未测量的时间不变混杂因素。作者提出多元广义线性混合效应模型（multivariate GLMM），将结果、时变混杂和治疗分配作为联合分布建模，通过引入个体随机效应捕捉未测量的时间不变因素导致的治疗偏好异质性。识别策略是：在给定随机效应（即治疗分配异质性）条件下，假设序列可忽略性（sequential ignorability），类比于平衡潜在治疗偏好。估计采用贝叶斯g-computation算法，通过MCMC后验抽样获得各组干预收益的后验分布。模拟研究验证了有限样本性能，真实数据分析评估了霉酚酸酯在不同硬皮病患者亚组中的持续使用效果。本文是因果推断与纵向数据混合效应模型的有机结合，对您在纵向因果推断设定下处理未测量混杂的研究有参考价值。
- **关键技术**: `multivariate generalized linear mixed-effects models`, `Bayesian g-computation`, `sequential ignorability`, `random effects for unmeasured confounding`, `dynamic treatment regimes`
- **为什么对您有用**: 本文直接连接到您primary interest中的纵向因果推断（longitudinal causal inference）子方向，特别是未测量时间不变混杂的处理。您熟悉非参数统计和因果推断估计理论，可以用于检查该参数化随机效应假设的稳健性，或探索半参拓展（如允许随机效应分布误设的灵敏度分析）。这是中期可做的工作——需先在 moderately_familiar 的 semiparametric theory 上加强，以评估模型误设对干预效应估计的影响。

### 3. [10.1093/biomtc/ujae069](https://doi.org/10.1093/biomtc/ujae069) · [arXiv](https://arxiv.org/abs/2310.16207) — Propensity weighting plus adjustment in proportional hazards model is not doubly robust
- **作者**: Erin E Gabriel, Michael C Sachs, Ingeborg Waernbaum, Els Goetghebeur, Paul F Blanche, Stijn Vansteelandt et al.
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 本文研究在比例风险模型下，将倾向得分加权与 Cox 回归调整相结合是否能构造出双重稳健估计量。目标估计量是暴露效应的风险比（hazard ratio），关键假设包括无未测量混杂、正确指定倾向得分模型或生存模型之一。作者证明：在存在因果效应时，这种组合即使在回归标准化后也不具备双重稳健性；但在零假设（无因果效应）下，若删失机制可正确建模，则该组合在倾向得分或生存模型任一正确指定时一致。模拟验证覆盖半参数 Cox、Weibull 和灵活参数模型，均显示非双重稳健性。作者提出两个针对固定时点生存差的双重稳健估计量和一个针对完整生存曲线的方法，并提供了 R 实现。对您有用：直接涉及因果推断中生存分析的双重稳健理论，与您 primary interest 中的 semiparametric efficiency 和 identification theory 相关。
- **关键技术**: `propensity score weighting`, `proportional hazards model`, `double robustness`, `Cox partial likelihood`, `regression standardization`, `survival difference estimation`
- **为什么对您有用**: 本文直接触及因果推断中生存分析的双重稳健估计问题，属于您 primary interest 中 causal inference 与 semiparametric theory 的交叉。您武器库中的 semiparametric theory 和 M-estimation theory 可以用来分析作者提出的估计量的效率性质，或探索是否存在其他形式的双重稳健构造。**立即可做**：用 very_familiar 的 estimation theory in causal inference 验证作者声称的双重稳健性条件，或用 moderately_familiar 的 semiparametric theory 推导 influence function。

### 4. [10.1093/biomtc/ujae067](https://doi.org/10.1093/biomtc/ujae067) · [arXiv](https://arxiv.org/abs/2306.16068) — Joint structure learning and causal effect estimation for categorical graphical models
- **作者**: Federico Castelletti, Guido Consonni, Marco L Della Vedova
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文考虑分类变量系统中对某个变量的外部干预，目标是评估其对结果变量的因果效应，同时学习变量之间的有向无环图（DAG）结构。方法特色在于同时处理结构学习和效应估计中的不确定性：将DAG和参数视为随机变量，提出可逆跳跃MCMC（RJMCMC）算法，在DAG空间和参数空间联合采样后验分布。算法利用高效的可逆跳跃提议，在每次迭代中可改变图结构并自适应调整参数，从而避免分别拟合多个图模型。模拟研究表明该方法在因果效应估计的准确性上优于当前基于贝叶斯模型平均或结构学习的常用方法（如BMA、BGe）。最后将该方法应用于大学生抑郁与焦虑的观察性数据，给出风险因素到抑郁的因果效应估计及其后验区间。对您而言，本文虽采用贝叶斯框架，但关注的核心问题（分类变量干预效应的识别与估计）属于因果推断的子方向，可从中借鉴对离散混杂因素的处理思路及结构不确定性下的推理方法。
- **关键技术**: `reversible-jump MCMC`, `causal effect estimation`, `categorical graphical models`, `directed acyclic graph (DAG)`, `posterior inference over DAGs`, `structure learning uncertainty`
- **为什么对您有用**: (1) 本文直接对应 primary interest 中的因果推断（尤其是干预效应的识别和估计），处理的是分类变量系统的因果效应，属于您关注的 estimation theory in causal inference 领域。(2) 您熟悉的 identification theory in causal inference 可用来审视其因果识别假设（如无混杂、一致性是否在分类框架下被适当假定），并检验其贝叶斯估计是否可能随着样本量增大收敛到识别后的真值——这是您用 semiparametric theory 可以攻击的一个口子。(3) 中期可做：本文的贝叶斯图模型工具（RJMCMC）不在您当前的 arsenal 中，但若想将类似的不确定性量化思路移植到您熟悉的半参数因果框架（如 DML 或 proximal CI），需要先花时间掌握 reversible-jump 和 DAG 后验抽样的基本原理。

### 5. [10.1093/biomtc/ujae065](https://doi.org/10.1093/biomtc/ujae065) — Multiply robust estimation of marginal structural models in observational studies subject to covariate-driven observations
- **作者**: Janie Coulombe, Shu Yang
- **期刊/来源**: Biometrics
- **机构**: Université de Montréal · North Carolina State University
- **分类**: vol 80 · issue 3
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在纵向观察性研究中，目标是估计边际结构模型（MSM）的因果效应，核心挑战在于同时存在混杂偏差和协变量驱动的非规则观测时间（covariate-driven observation times）。本文提出了一种新的乘法稳健估计器，通过构造包含多个 nuisance function 的加权估计，在至少一个 nuisance 模型正确指定时保持一致性。理论证明该估计器具有双重稳健性扩展形式，并在适度正则条件下达到半参数有效界；模拟研究显示其相比现有的双重加权估计器具有更高的有限样本效率。实证分析使用 Add Health 数据估计心理治疗对美国青少年饮酒行为的因果效应。对您在纵向因果推断和效率理论方向的研究有直接参考价值。
- **关键技术**: `multiply robust estimation`, `marginal structural models`, `inverse probability weighting`, `covariate-driven observation times`, `semiparametric efficiency`, `longitudinal causal inference`
- **为什么对您有用**: 直接连接纵向因果推断中的 MSM 估计与半参数效率理论，涉及您熟悉的 efficiency bound 和 robust estimation。您可以用 very_familiar 的 estimation theory in causal inference 攻击其效率性质，或用 moderately_familiar 的 semiparametric theory 验证其声称的 multiply robust 性质是否达到效率界。立即可做：用您熟悉的 minimax bound 和效率理论框架审视其估计器的最优性。

### 6. [10.1093/biomtc/ujae070](https://doi.org/10.1093/biomtc/ujae070) · [arXiv](https://arxiv.org/abs/2306.16715) — Causal meta-analysis by integrating multiple observational studies with multivariate outcomes
- **作者**: Subharup Guha, Yi Li
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在整合多个观察性研究进行因果元分析的情境下，针对回顾性队列的样本非代表性和协变量不平衡问题，提出基于伪总体（pseudo-population）的协变量平衡框架，将现有的加权方法扩展至多队列、多组比较。核心贡献是 FLEXOR（FLEXible, Optimized, Realistic）加权方法，通过最大化每个队列的有效样本量来构造伪总体，使得不同队列间的加权样本可比。在此基础上，作者开发了面向定量、分类及多变量结局的多个组比较的无混杂推断的加权估计量，并证明了这些估计量的一致性和渐近正态性。模拟研究与 TCGA 真实数据整合分析验证了该方法的可靠性和实用性。该工作直接对接您的因果推断和流行病学应用兴趣，为您在多源观察性研究中应用加权或伪总体方法提供了易于迁移的工具和理论保证。
- **关键技术**: `covariate-balancing weighting`, `pseudo-population`, `FLEXOR weighting`, `meta-analysis of observational studies`, `weighted estimators for multivariate outcomes`, `asymptotic theory for meta-analytic estimators`
- **为什么对您有用**: 本文直接涉及您 primary interest 中的因果推断（identification 与 estimation）以及 secondary interest 中的流行病学应用。您可以用 very_familiar 中的『estimation theory in causal inference』深入分析该权重构造的识别条件与方差表现；也可结合 moderately_familiar 中的『identification theory』评估其在不同偏倚来源下的稳健性。该框架立即可在您熟悉的多队列因果比较中实现，属于『立即可做』的探索方向。

### 7. [10.1093/biomtc/ujae064](https://doi.org/10.1093/biomtc/ujae064) — Controlling false discovery rate for mediator selection in high-dimensional data
- **作者**: Ran Dai, Ruiyang Li, Seonjoo Lee, Ying Liu
- **期刊/来源**: Biometrics
- **机构**: University of Nebraska Medical Center · Columbia University
- **分类**: vol 80 · issue 3
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文提出一个框架，在高维候选中介变量集合中进行FDR控制的选择。研究问题是在高维数据（如神经影像、遗传数据）中识别中介变量，同时控制假发现率。方法将近年发展的knockoff变量选择方法扩展到中介选择场景，通过构造knockoff变量和适当的检验统计量，在有限样本下实现FDR控制。算法上利用了knockoff的对称性来保证FDR性质。模拟实验显示该方法比现有方法有更好的检验功效和有限样本性能。最后应用到ABCD研究，筛选出静息态功能磁共振连接作为童年不良事件与认知评分之间关系的中介。本文连接了因果推断中的中介分析和高维假设检验的FDR控制，对您思考高维中介变量选择的统计推断问题有直接参考价值。
- **关键技术**: `knockoff`, `false discovery rate control`, `mediator selection`, `high-dimensional inference`, `multiple testing adjustment`
- **为什么对您有用**: 1) 直接连接您的primary interest中的causal inference（mediation）和hypothesis testing（FDR控制），在高维设定下处理中介变量的选择问题。2) 您的技术武器库中'high-dimensional asymptotics'和'estimation theory in causal inference'可以用于评估该方法的理论性质，例如是否可以达到渐近最优或是否需要更强的假设。3) 立即可做：您对knockoff和FDR控制有一定了解（very_familiar中的high-dimensional asymptotics和estimation theory），可以尝试将该方法与其他因果推断方法（如instrumental variables或proximal causal inference）结合进行类似的问题拓展。

### 8. [10.1093/biomtc/ujae094](https://doi.org/10.1093/biomtc/ujae094) · [arXiv](https://arxiv.org/abs/2302.01269) — Adjusting for incomplete baseline covariates in randomized controlled trials: a cross-world imputation framework
- **作者**: Yilin Song, James P Hughes, Ting Ye
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文在随机对照试验（RCT）中处理基线协变量缺失问题，目标是通过调整协变量提高处理效应估计的精度。作者提出一个名为跨世界插补（CWI）的理论框架，将单一插补法和缺失指标法（MIM）作为特例统一起来，从而在统一视角下比较二者的效率。关键机制在于：MIM隐式地搜索最优CWI值，因此自动达到最优效率；而单一插补法则搜索最优单一插补值，其效率达到MIM水平需要特定条件。作者推导了这些条件的数学刻画，并通过模拟和儿童腺样体扁桃体切除术试验（CHAT）数据验证。该工作直接关联因果推断中协变量调整的效率理论，为处理不完全协变量提供了清晰的识别与估计策略，对您熟悉的无偏性和效率论证（如半参数效率界）有直接参考价值。
- **关键技术**: `cross-world imputation`, `missingness-indicator method (MIM)`, `single imputation`, `efficiency comparison`, `covariate adjustment`, `randomized controlled trials`
- **为什么对您有用**: 本文属于因果推断中RCT协变量调整和缺失数据处理的效率问题，直接连接到您的primary interest 'causal inference'下的估计精度提升。您熟练的'estimation theory in causal inference'可以轻松理解其CWI框架的识别逻辑和效率比较，属于立即可做的范畴——可将该框架中的最优插补思想迁移到您自己的因果推断估计问题（如proximal CI或IV）中处理类似缺失结构。

### 9. [10.1093/biomtc/ujae073](https://doi.org/10.1093/biomtc/ujae073) — A generalized outcome-adaptive sequential multiple assignment randomized trial design
- **作者**: Xue Yang, Yu Cheng, Peter F Thall, Abdus S Wahed
- **期刊/来源**: Biometrics
- **机构**: University of Pittsburgh · The University of Texas MD Anderson Cancer Center · University of Rochester
- **分类**: vol 80 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在 SMART（Sequential Multiple Assignment Randomized Trial）框架下，目标是估计动态治疗策略（DTR）的效应，传统设计忽略历史数据导致过多患者接受劣质治疗。本文提出 GO-SMART 设计，通过 outcome-adaptive randomization 在各阶段自适应地向更优治疗臂倾斜随机化概率。为校正自适应随机化引入的偏差，作者构造了 G-estimator 和逆概率加权（IPW）估计量，并在正则性条件下证明其一致性。模拟结果显示，相比标准 SMART 和其他自适应设计，GO-SMART 在保持统计功效的同时，显著增加了接受最优 DTR 的患者比例和总响应数。对您在 longitudinal/sequential treatment setting 下的因果推断工作有直接参考价值。
- **关键技术**: `dynamic treatment regime (DTR)`, `SMART design`, `outcome-adaptive randomization`, `G-estimation`, `inverse probability weighting (IPW)`, `sequential decision making`
- **为什么对您有用**: 直接连接到 primary interest 中的 longitudinal 和因果推断设定。您熟悉的 IPW 理论和 semiparametric theory（moderately_familiar）可以用来分析这些 estimator 的效率性质，例如是否达到 semiparametric efficiency bound。立即可做：用 very_familiar 的 estimation theory 审视其 consistency 条件和效率损失；中期可做：若想深入 DTR 理论，需在 identification theory（moderately_familiar）上补充 dynamic regime 的 counterfactual 框架。

### 10. [10.1093/biomtc/ujae061](https://doi.org/10.1093/biomtc/ujae061) — Optimal refinement of strata to balance covariates
- **作者**: Katherine Brumberg, Dylan S Small, Paul R Rosenbaum
- **期刊/来源**: Biometrics
- **机构**: University of Michigan · University of the Sciences · University City Science Center · University of Pennsylvania · Philadelphia University
- **分类**: vol 80 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在观察性研究的分层匹配框架中，本文研究如何将一个现有层最优地划分为两个子层，使得层内多个协变量的不平衡度量最小化，从而提升后续因果效应估计的精度。作者将这一层次优化问题表述为整数规划，并利用线性规划松弛与随机舍入（randomized rounding）来近似求解，避免直接求解NP难的组合问题。当层内个体数远大于协变量个数时，他们证明了两个关键性质：(i) 随机舍入的解几乎与线性规划松弛的解一致，即几乎不引入额外随机性；(ii) 线性松弛和随机舍入分别给出了不可达的整数规划最优解的上下界，且这些界在所述条件下是紧的。实证部分使用R包optrefine对一个倾向得分分层进行细化，从5层扩展为10层，在保留全部5735名患者的同时获得了良好的协变量平衡。该方法直接服务于匹配前分层的协变量平衡，与您的causal inference兴趣点（尤其是识别理论和匹配设计）紧密相连。
- **关键技术**: `integer programming`, `linear programming relaxation`, `randomized rounding`, `covariate balancing`, `propensity score stratification`
- **为什么对您有用**: 本文直接关联您primary interest中的causal inference（分层匹配与协变量平衡），特别是识别理论和匹配设计。您very_familiar中的'estimation theory in causal inference'可用来评估该分层优化对ATE估计偏差和方差的影响，并可尝试将其扩展到IV或纵向设置下的分层策略。立即可做：您已有足够工具理解该方法，并可在R中复现或调整至您自己的因果推断研究。

### 11. [10.1093/biomtc/ujae080](https://doi.org/10.1093/biomtc/ujae080) · [arXiv](https://arxiv.org/abs/2401.05124) — Nonparametric worst-case bounds for publication bias on the summary receiver operating characteristic curve
- **作者**: Yi Zhou, Ao Huang, Satoshi Hattori
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对诊断测试准确性meta分析中由选择性发表引起的publication bias (PB)问题，以SROC曲线为感兴趣的汇总统计量。现有PB敏感性分析方法均采用参数选择函数建模选择性发表机制，本文提出一种新方法，在最小假设下采用非参数选择函数推导SROC曲线的最坏情况界（worst-case bounds）。估计流程先使用Monte Carlo方法近似PB对SROC曲线及其AUC的偏差，再通过非线性规划优化给定边际选择概率范围下PB的最大值与最小值。该方法不对选择函数做参数形式假设，只依赖可识别性约束，增强了敏感性分析的稳健性。应用于两个真实meta分析数据集，展示了最坏情况界如何帮助判断诊断准确性的meta分析结论对PB的敏感程度。本文的方法对您从事因果推断中基于非参数工具的敏感性分析有直接借鉴意义，尤其是处理未测量混杂或选择性偏差的worst-case界构造思路，可迁移至您的proximal causal inference工作。
- **关键技术**: `nonparametric selection function`, `worst-case bounds`, `Monte Carlo approximation`, `nonlinear programming`, `SROC curve`, `publication bias sensitivity analysis`
- **为什么对您有用**: （1）本文处理publication bias的worst-case敏感性分析，属于因果推断中‘选择偏差’这一子方向，与您对proximal CI及一般敏感性分析的关注高度契合。（2）您武器库中‘nonparametric statistics’和‘minimax bounds for estimation problems’可直接用于理解和扩展本文的worst-case界构造（例如，能否得到sharp界或更快的收敛率），而‘estimation theory in causal inference’则可协助将其形式化为一种可估计的灵敏度参数。（3）**立即可做**：您完全可以用熟悉的非参数估计和Monte Carlo工具复现并扩展本文的方法（例如，将边际选择概率的优化范围推广到基于协变量的条件选择概率）。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 2 篇)*

### 1. [10.1093/biomtc/ujae103](https://doi.org/10.1093/biomtc/ujae103) — Leveraging independence in high-dimensional mixed linear regression
- **作者**: Ning Wang, Kai Deng, Qing Mai, Xin Zhang
- **期刊/来源**: Biometrics
- **机构**: Beijing Normal University · Florida State University
- **分类**: vol 80 · issue 3
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究高维混合线性回归（High-dimensional Mixed Linear Regression）中回归系数估计与变量选择问题，设定为 p ≫ n，假设预测变量与潜在混合指示变量独立。作者提出 fast group-penalized EM 算法，利用该独立性假设实现跨混合成分的协同变量选择，并显著降低计算成本。理论上给出估计量的 non-asymptotic convergence rate，建立参数估计误差的显式上界。实证部分通过模拟和 Cancer Cell Line Encyclopedia 数据集验证方法在抗癌药物敏感性预测中的表现。对您而言，这是高维稀疏估计与 EM 算法非渐近理论的具体实例。
- **关键技术**: `group-penalized EM`, `non-asymptotic convergence rate`, `high-dimensional mixed linear regression`, `coordinate descent`, `variable selection consistency`, `sparsity-inducing penalty`
- **为什么对您有用**: 连接到您 primary interest 中的 high-dimensional statistics 与 estimation theory。您 very_familiar 的 minimax bounds for estimation problems 可用于检验本文声称的 convergence rate 是否紧，moderately_familiar 的 M-estimation theory 可用于分析 EM 迭代的收敛性质。立即可做：用您熟悉的高维渐近工具审视其 non-asymptotic bound 的 sharpness。

### 2. [10.1093/biomtc/ujae096](https://doi.org/10.1093/biomtc/ujae096) — Heterogeneous latent transfer learning in Gaussian graphical models
- **作者**: Qiong Wu, Chi Wang, Yong Chen
- **期刊/来源**: Biometrics
- **机构**: University of Pittsburgh · University of Pennsylvania · University of Kentucky
- **分类**: vol 80 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在高维 Gaussian graphical model (GGM) 设定下，本文研究如何在目标数据集与源数据集之间存在潜在异质性（latent heterogeneity）时进行迁移学习，目标是精确估计目标 precision matrix。核心方法是 Latent-TL 算法：通过联合聚类识别源-目标样本间的共同子群结构，并在同子群内借用源样本信息以提升目标 GGM 的估计精度；估计采用 penalized likelihood / neighborhood selection 类技术，结合 group-wise 信息聚合。理论贡献包括在高维设定下证明估计误差的收敛率优于单样本学习，并刻画了在何种异质性程度下迁移学习有效（避免 negative transfer）。实证部分通过模拟和乳腺癌基因共表达网络数据验证方法优势；对您而言，这是高维协方差/精度矩阵估计与迁移学习交叉的一个具体应用案例。
- **关键技术**: `Gaussian graphical model`, `precision matrix estimation`, `transfer learning`, `latent heterogeneity`, `penalized likelihood`, `high-dimensional convergence rate`
- **为什么对您有用**: 连接到您 primary interest 中的 high-dimensional statistics（高维精度矩阵估计），涉及异质性迁移学习这一较新方向。您武器库中的 high-dimensional asymptotics 和 minimax bounds 可用于审视本文声称的收敛率是否紧、异质性条件的数学刻画是否足够清晰。判断：**中期可做**——需先在 moderately_familiar 的 semiparametric theory 或 M-estimation theory 上补充高维 penalized M-estimator 的非渐近理论工具，才能深入分析其理论性质或提出改进。

## 非参数 / 半参数  *(nonparam_semipara, 6 篇)*

### 1. [10.1093/biomtc/ujae063](https://doi.org/10.1093/biomtc/ujae063) — Nonparametric receiver operating characteristic curve analysis with an imperfect gold standard
- **作者**: Jiarui Sun, Chao Tang, Wuxiang Xie, Xiao-Hua Zhou
- **期刊/来源**: Biometrics
- **机构**: Peking University · Peking University International Hospital · Peking University First Hospital · Peking University People's Hospital
- **分类**: vol 80 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究在诊断试验中金标准不完美时，如何非参数地估计ROC曲线及其曲线下面积（AUC）。设定依赖于已知或可估计的不完美参照标准准确率以及条件独立假设，在此框架下证明了ROC曲线的可识别性，并提出了非参数估计方法。当不完美参照标准准确率未知时，进一步证明两个AUC差值的符号是可识别的，并据此开发了假设检验方法，用于判断哪一个诊断指标更优。相比现有参数方法，本文方法不依赖参数模型假设，且同时适用于连续型和有序型生物标志物。理论分析和模拟研究验证了所提方法的统计性质，并在两个真实诊断数据中进行了应用。对您而言，本文的非参数识别策略与假设检验思路与您熟悉的nonparametric statistics和hypothesis testing方向紧密相关，同时其处理测量误差的识别框架对proximal causal inference中的negative control设定也有参考价值。
- **关键技术**: `Nonparametric identification`, `Conditional independence assumption`, `Hypothesis testing for AUC difference`, `Imperfect gold standard`, `ROC curve estimation`
- **为什么对您有用**: 本文连接您primary interest中的nonparametric theory（非参数识别与估计）以及hypothesis testing（AUC差值符号检验）。武器库中的nonparametric statistics与estimation theory in causal inference可直接用于理解本文方法的识别逻辑与估计性质——例如用您熟悉的minimax bounds分析其非参数收敛速率。follow-up粗判：立即可做——阅读全文并复现方法没有技术障碍，因为方法与您现有的nonparametric toolkit口径一致，且数据生成机制清晰，可直接用您的软件工程能力实现模拟和数据分析。

### 2. [10.1093/biomtc/ujae098](https://doi.org/10.1093/biomtc/ujae098) · [arXiv](https://arxiv.org/abs/2311.09935) — Semi-parametric benchmark dose analysis with monotone additive models
- **作者**: Alex Stringer, Tugba Akkaya Hocagil, Richard J Cook, Louise M Ryan, Sandra W Jacobson, Joseph L Jacobson
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究毒理学中 benchmark dose (BMD) 的估计与推断问题，目标参数是使 adverse outcome 风险达到预设基准水平的暴露剂量，核心假设是剂量-反应曲线的单调性。方法上，作者提出用 penalized B-splines 在可加模型框架下拟合单调曲线，通过 Laplace 近似边际似然选择惩罚参数，并开发 reflective Newton 方法结合 de Boor 算法实现高效数值优化。推断方面，核心贡献是构造了一个关于 BMD 估计方程的近似 pivot，由此得到置信下限，避免了 Delta method 在非线性估计中的不稳定性和 bootstrap 的计算负担。理论部分证明了估计量的 consistency 并讨论了近似 pivot 的渐近性质，模拟显示其覆盖率优于 Delta method 且与 parametric bootstrap 相当但计算更快。实证分析整合了六个纵向队列研究的数据，估计了孕期酒精暴露导致儿童认知缺陷的 BMD。对您而言，本文展示了 semiparametric model 下非线性泛函推断的一种实用路径，与您关注的 semiparametric efficiency 和 influence function 思路有相通之处。
- **关键技术**: `penalized B-splines`, `monotone additive model`, `Laplace-approximate marginal likelihood`, `reflective Newton method`, `approximate pivot construction`, `benchmark dose inference`
- **为什么对您有用**: 本文属于 semiparametric theory 在流行病学剂量-反应分析中的应用，涉及非线性泛函（BMD）的估计与置信区间构造，与您 primary interest 中的 semiparametric efficiency 和 influence function 理论直接相关。技术上，本文的 approximate pivot 方法可视为 influence function 思路的一种变体，但未涉及 semiparametric efficiency bound 的理论最优性讨论。follow-up 判断：**中期可做**——您可以用 very_familiar 的 nonparametric statistics 和 moderately_familiar 的 semiparametric theory 分析该估计量的 efficiency 性质，或探索是否可用 one-step correction 进一步改进推断；但需先补足 M-estimation theory 中关于 nonlinear estimator 推断的细节。

### 3. [10.1093/biomtc/ujae071](https://doi.org/10.1093/biomtc/ujae071) — Nonparametric second-order estimation for spatiotemporal point patterns
- **作者**: Decai Liang, Jialing Liu, Ye Shen, Yongtao Guan
- **期刊/来源**: Biometrics
- **机构**: Nankai University · Sun Yat-sen University · University of Georgia · Shenzhen Research Institute of Big Data · Chinese University of Hong Kong, Shenzhen
- **分类**: vol 80 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 针对时空点过程，现有方法通常假设空间和时间二阶平稳性，但实际数据常违背该假设。本文提出一种灵活的、无需平稳性假设的非参数二阶估计方法，用于估计时空点过程的pair correlation函数。方法采用核平滑，对空间和时间相关性分别处理，并可结合不同的一阶强度估计量以提高实用性。在空间递增域渐近框架下，证明了估计量的一致性。模拟结果显示，与现有方法相比，所提方法显著提高了统计效率。COVID-19数据分析进一步展示了方法的灵活性和可解释性。对于您的流行病学应用兴趣，该方法提供了处理时空依赖数据的非参数工具。
- **关键技术**: `kernel smoothing`, `pair correlation function`, `spatially increasing-domain asymptotics`, `second-order intensity estimation`, `point process`
- **为什么对您有用**: 本文属于非参数时空点过程估计，连接您的非参数理论兴趣和流行病学应用兴趣（COVID-19数据）。您非常熟悉minimax bound和非参数统计，可用来评估该估计量的收敛速率是否达到最优，或探究能否利用U-统计量/高阶影响函数提升效率。目前需要补足点过程理论（暂不可做），但中期可通过阅读空间统计文献后跟进。

### 4. [10.1093/biomtc/ujae091](https://doi.org/10.1093/biomtc/ujae091) — Unit information Dirichlet process prior
- **作者**: Jiaqi Gu, Guosheng Yin
- **期刊/来源**: Biometrics
- **机构**: Stanford University · University of Hong Kong
- **分类**: vol 80 · issue 3
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出一种新的非参数贝叶斯先验——单位信息狄利克雷过程（UIDP），用于生存分析中时间-事件数据的分布建模。该先验在狄利克雷过程基础上，通过构造关于累积风险函数微分的Fisher信息量，使其先验信息量与历史数据集的加权平均单位信息相匹配。UIDP先验能够自适应地借用历史信息，同时利用参数和非参数信息，提升了贝叶斯推断的统计效率。该方法通过马尔可夫链蒙特卡洛（MCMC）算法实现，并在模拟和真实数据分析中验证了效果。对于您而言，该工作连接了非参数理论与流行病学中生存数据分析的交叉点，其中非参数先验的构造思路可能迁移到因果推断中的敏感性问题。然而，您对贝叶斯非参数和MCMC的专门经验有限，因此属于暂不可做的方向，需先补充相关领域知识。
- **关键技术**: `Dirichlet process prior`, `unit information prior`, `Fisher information for cumulative hazard`, `nonparametric Bayesian survival analysis`, `Markov chain Monte Carlo`
- **为什么对您有用**: 本文涉及非参数贝叶斯先验在生存分析中的应用，连接了您的非参数理论兴趣和流行病学数据分析方向。您的技术武器库中'非参数统计'和'软件工具'可以用于理解框架，但贝叶斯非参数和MCMC的具体工具不在您的核心武器库内，因此属于暂不可做：需要先学习贝叶斯非参数推断才能独立扩展该工作。尽管如此，该文作为非参数先验构造的新思路，值得关注以启发因果推断中历史数据利用的方法。

### 5. [10.1093/biomtc/ujae078](https://doi.org/10.1093/biomtc/ujae078) — Factor-augmented transformation models for interval-censored failure time data
- **作者**: Hongxi Li, Shuwei Li, Liuquan Sun, Xinyuan Song
- **期刊/来源**: Biometrics
- **机构**: Guangzhou University · Academy of Mathematics and Systems Science · University of Chinese Academy of Sciences · Chinese University of Hong Kong
- **分类**: vol 80 · issue 3
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 该文针对区间删失失效时间数据提出因子增强变换模型（factor-augmented transformation model），旨在降维并缓解多重共线性。核心设定是：多个相关协变量通过因子分析模型浓缩为少量潜因子，再纳入半参数变换模型（含未知递增变换函数和回归系数）以刻画失效风险。估计采用非参数极大似然估计（NPMLE）并开发了稳健的EM算法，计算中利用因子结构的稀疏性提高收敛性。渐近性质（一致性和渐近正态性）通过经验过程理论证明，模拟表明有限样本表现良好。文章还提供了R包ICTransCFA和真实数据（ADNI阿尔茨海默病研究）应用。对于您关注的流行病学方向，该文提供了一个清晰的区间删失数据联合建模框架，而半参数变换模型的渐近理论也可迁移到您熟悉的因果推断中类似模型的效率分析。
- **关键技术**: `factor analysis model`, `semiparametric transformation model`, `nonparametric maximum likelihood estimation (NPMLE)`, `expectation-maximization algorithm`, `interval-censored failure time data`, `asymptotic properties via empirical process`
- **为什么对您有用**: 该文直接连接到您的流行病学（ADNI数据集）和半参数/非参数理论兴趣。您武器库中的semiparametric theory（moderately_familiar）和nonparametric statistics（very_familiar）可轻松理解其NPMLE的渐近论证及因子分析降维逻辑。对于follow-up，立即可做——您已有的经验过程和高维渐近工具足以评估其估计量的效率或改进其EM算法；无需额外强化武器。

### 6. [10.1093/biomtc/ujae090](https://doi.org/10.1093/biomtc/ujae090) — Integrating external summary information in the presence of prior probability shift: an application to assessing essential hypertension
- **作者**: Chixiang Chen, Peisong Han, Shuo Chen, Michelle Shardell, Jing Qin
- **期刊/来源**: Biometrics
- **机构**: University of Maryland, Baltimore · Foundation for the National Institutes of Health · Gilead Sciences (United States) · National Institute of Allergy and Infectious Diseases
- **分类**: vol 80 · issue 3
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究在利用外部摘要信息进行内部研究时，因数据分布差异导致的先验概率偏移（prior probability shift）问题，即两组数据分布差异依赖于结局变量。作者提出一种新的半参数约束优化方法，通过引入结局依赖选择函数（outcome-dependent selection function）来刻画偏移，并无需外部已知的方差-协方差估计即可进行有效推断。该方法在估计目标参数时联合使用内部个体数据和外部汇总信息，通过约束优化实现效率提升，属于经验似然/半参数M-估计类型。模拟显示该方法在二值和连续结局下均比现有方法偏差更小、方差更低。论文进一步应用于原发性高血压风险因素分析，整合外部摘要信息后估计变异性降低。对您而言，该方法将外部数据整合与半参数约束优化结合，与您的半参数理论和效率理论兴趣直接相关；武器库中的M估计理论可用于分析其渐近性质，目前您处于moderately_familiar水平，可视为中期可做方向。
- **关键技术**: `semiparametric constrained optimization`, `prior probability shift`, `outcome-dependent selection function`, `summary-level information integration`, `empirical likelihood`, `inference without known variance-covariance`
- **为什么对您有用**: 本文属于半参数信息整合方法，连接您的半参数理论与效率理论兴趣子方向。其核心是半参数约束优化估计，可用武器库中moderately_familiar的M估计理论（empirical likelihood框架）系统分析估计量的渐近行为和鲁棒性。**中期可做**：需先在moderately_familiar的semiparametric theory方面提升，例如深入学习经验似然和profile likelihood，即可将此类方法推广到您的因果推断或U-统计量问题中。

## 数理统计 / 假设检验  *(hypothesis_testing, 4 篇)*

### 1. [10.1093/biomtc/ujae088](https://doi.org/10.1093/biomtc/ujae088) — High-dimensional multivariate analysis of variance via geometric median and bootstrapping
- **作者**: Guanghui Cheng, Ruitao Lin, Liuhua Peng
- **期刊/来源**: Biometrics
- **机构**: Guangzhou University · Guangdong University of Finance · The University of Texas MD Anderson Cancer Center · The University of Melbourne
- **分类**: vol 80 · issue 3
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究高维多组位置参数的检验问题，目标是在维数 p 可远大于样本量 n 的设定下，检验多组数据的几何中位数是否相等。作者提出基于组间几何中位数差异的 maximum-type 检验统计量，利用 Gaussian approximation 导出其在零假设下的渐近分布，并证明了备择假设下检验的一致性。为逼近高维下检验统计量的分布，设计了 wild bootstrap 算法并给出理论保证。模拟研究覆盖多种维数、样本量和数据生成模型，展示了有限样本表现；实证分析应用于乳腺癌基因表达数据。对您的高维假设检验与高维渐近理论兴趣有直接参考价值。
- **关键技术**: `geometric median`, `maximum-type test statistic`, `Gaussian approximation`, `wild bootstrap`, `high-dimensional MANOVA`, `robust location estimation`
- **为什么对您有用**: 直接连接到您的高维假设检验兴趣，特别是高维渐近理论与检验统计量的分布逼近。您熟悉的 high-dimensional asymptotics 与 minimax bounds 可用于审视其 Gaussian approximation 的 sharpness 与检验的 optimality。立即可做：用 very_familiar 的高维渐近工具验证其 Gaussian approximation 条件是否可放松或改进，或探索该检验在更一般分布假设下的 robustness。

### 2. [10.1093/biomtc/ujae101](https://doi.org/10.1093/biomtc/ujae101) · [arXiv](https://arxiv.org/abs/2504.11767) — Post-selection inference in regression models for group testing data
- **作者**: Qinyan Shen, Karl Gregory, Xianzheng Huang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对群体检测数据（group testing data）中响应变量部分观测的逻辑回归模型，开发了变量选择后的有效推断方法。在群体检测中，个体真实感染状态无法直接观测，仅获得有误差的混合检测结果，导致似然函数复杂。作者采用EM算法求解LASSO惩罚下的最大似然估计，实现变量选择的同时处理缺失信息。在推断阶段，基于polyhedral lemma（多面体引理）推导选定协变量系数的条件分布，从而构造调整选择偏差的置信区间和p值。模拟实验表明，忽略选择步骤的天真推断严重扭曲第一类错误，而所提方法能有效控制覆盖概率和检验水平。该方法将经典后选择推断框架拓展至不完全响应数据场景，对您而言，其核心思想（条件推断调整选择偏差）与假设检验兴趣直接相关，且高维渐近分析能力可用于评估拟似然中的有限样本行为。
- **关键技术**: `LASSO penalized logistic regression`, `EM algorithm`, `polyhedral lemma`, `post-selection inference`, `group testing data`
- **为什么对您有用**: 本文连接了假设检验中后选择推断这一具体子方向，且使用polyhedral lemma处理变量选择后的条件分布，呼应您对高维渐近和假设检验的兴趣。您非常熟悉的high-dimensional asymptotics可直接用于理解该方法的渐近有效性条件，而software development技能有助于复现其EM与推断算法。整体：立即可做——您可用模拟框架检验该方法在不同缺失机制下的表现，并考虑将polyhedral思想延伸到其他部分观测响应模型。

### 3. [10.1093/biomtc/ujae082](https://doi.org/10.1093/biomtc/ujae082) · [arXiv](https://arxiv.org/abs/2310.09493) — Summary statistics knockoffs inference with family-wise error rate control
- **作者**: Catherine Xinrui Yu, Jiaqi Gu, Zhaomeng Chen, Zihuai He
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在仅有边际依赖的 summary statistics 可得的设定下，本文研究如何对条件独立性进行多重假设检验并控制 family-wise error rate (FWER)。核心方法是采用 GhostKnockoff 框架直接对 summary statistics 生成 knockoff copies，并设计新的 filter 筛选与响应条件依赖的特征。理论贡献包括证明所提方法在 FWER 控制上的有效性，以及开发了一种计算高效的 knockoff 生成算法，在不损失统计功效和错误率控制的前提下大幅降低计算成本。模拟研究和阿尔茨海默病遗传学真实数据验证了方法在功效和计算效率上优于现有替代方案。对您可能有用：这是 knockoff inference 在 summary-level data 场景的拓展，涉及多重检验的 FWER 控制和计算效率优化。
- **关键技术**: `model-X knockoffs`, `GhostKnockoff`, `family-wise error rate control`, `conditional independence testing`, `summary statistics inference`, `computational efficiency optimization`
- **为什么对您有用**: 连接到 hypothesis testing 这一 primary interest 子方向，具体是多重检验中的 FWER 控制问题。您在 technical_arsenal 中 very_familiar 的 software development 和 computation of higher-order U-statistics（涉及计算效率优化）可以用来审视其 knockoff 生成算法的复杂度改进。follow-up 判断：立即可做——用您熟悉的 minimax bounds 和 nonparametric statistics 视角可以评估其功效上界是否紧，或用 software development 能力复现并扩展到其他遗传学数据集。

### 4. [10.1093/biomtc/ujae079](https://doi.org/10.1093/biomtc/ujae079) — Hypothesis tests in ordinal predictive models with optimal accuracy
- **作者**: Yuyang Liu, Shan Luo, Jialiang Li
- **期刊/来源**: Biometrics
- **机构**: Shanghai Zhangjiang Laboratory · Shanghai Jiao Tong University · National University of Singapore
- **分类**: vol 80 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在多类别有序判别问题中，目标是检验多个预测变量的线性组合是否能达到最优 HUM（hypervolume under ROC manifolds）。本文提出用 jackknife empirical likelihood 方法进行统计推断，在正则条件下证明了 Wilks 定理，并给出了 Pitman 备择下的功效分析。核心计算涉及一个一般的多样本 U-statistic，作者设计了基于网络结构的快速算法来降低计算复杂度。模拟显示该方法在检验水平、功效和计算时间上均优于现有方法。对您有用之处在于：U-statistic 的快速计算算法与您在 higher-order U-statistics 和 tensor contraction 方面的工作直接相关。
- **关键技术**: `jackknife empirical likelihood`, `U-statistic computation`, `HUM (hypervolume under ROC manifolds)`, `Wilks theorem`, `network-based algorithm`, `Pitman alternative`
- **为什么对您有用**: 本文的 U-statistic 快速计算算法直接关联您 very_familiar 的「higher-order U-statistics 的 treewidth / tensor contraction / einsum」武器库——可以审视其网络算法与 tensor contraction 视角的等价性，或探索能否用您的框架进一步优化。follow-up 判断：立即可做——用您的 treewidth / einsum 视角分析其算法复杂度，或尝试推广到更高阶 U-statistic 场景。

## 统计计算 / 算法  *(stat_computing, 3 篇)*

### 1. [10.1093/biomtc/ujae076](https://doi.org/10.1093/biomtc/ujae076) — Reduced-rank clustered coefficient regression for addressing multicollinearity in heterogeneous coefficient estimation
- **作者**: Yan Zhong, Kejun He, Gefei Li
- **期刊/来源**: Biometrics
- **机构**: East China Normal University · Renmin University of China
- **分类**: vol 80 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对聚类系数回归（CCR）中常见的多重共线性导致估计不稳定的问题，提出了一种降秩聚类系数回归方法。该方法引入系数矩阵的低秩结构，并设计了一种自适应组融合惩罚（adaptive group fusion penalty）来同时实现系数聚类和降维。估计通过一个非凸优化问题求解，作者开发了带收敛保证的迭代算法。理论上推导了系数估计误差的界，展示了统计性质。模拟研究和 COVID-19 死亡率数据分析表明，新方法在共线性存在时比现有 CCR 方法更稳定准确。该方法将低秩结构与聚类回归结合，为高维异质性建模提供了新的计算工具。您熟悉的高维渐近和极小极大界理论可直接用于验证该估计量的最优性，算法实现也便于您在流行病学数据集上应用。
- **关键技术**: `reduced-rank regression`, `clustered coefficient regression`, `adaptive group fusion penalty`, `non-convex optimization`, `low-rank structure`, `error bound analysis`
- **为什么对您有用**: 该论文直接关联您的高维统计和统计计算兴趣：低秩结构是高维建模的经典手法，您用 high-dimensional asymptotics 和 minimax bounds 工具可以分析估计误差界的紧性，并考虑理论改进。COVID-19 死亡率数据应用也触及您的流行病学兴趣。您的弹药库中 'minimax bounds for estimation problems' 和 'high-dimensional asymptotics' 两项可立即可用于评估其理论贡献，算法实现则可利用 'software development' 经验复现或扩展。总体而言，这是一篇方法学论文，您可以在立即可做的层面上吸收其技术并迁移至其他异质性建模场景。

### 2. [10.1093/biomtc/ujae104](https://doi.org/10.1093/biomtc/ujae104) — Planning cost-effective operational forest inventories
- **作者**: Santeri Karppinen, Liviu Ene, Lovisa Engberg Sundström, Juha Karvanen
- **期刊/来源**: Biometrics
- **机构**: University of Jyväskylä · Forestry Research Institute of Sweden
- **分类**: vol 80 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究林业运营中的贝叶斯两阶段决策问题：外阶段选择采伐前库存的精度（成本约束），内阶段基于库存估计安排采伐以满足需求目标。目标函数为最大化库存决策的后验价值，但计算涉及NP难的广义二次分配问题和高维积分。作者提出一个近似方法，结合蒙特卡洛采样和贪心随机化算法求解外阶段决策问题。在瑞典100个森林地块的数据集上验证了方法的有效性，估计了不同预算下信息获取的价值。本文的近似框架对于统计计算中的数值优化和贝叶斯决策有参考价值。
- **关键技术**: `Bayesian two-stage decision problem`, `Monte Carlo approximation`, `greedy randomized heuristic`, `generalized quadratic assignment problem`, `value of information`
- **为什么对您有用**: 本文属于统计计算中数值方法与算法设计，与您的统计计算兴趣直接相关。您的technical_arsenal中的software development技能可用于实现和扩展本文的近似算法。由于您熟悉数值方法和优化，可以尝试将此方法应用于其他资源分配决策问题（如医疗资源调度），属于立即可做的探索。

### 3. [10.1093/biomtc/ujae089](https://doi.org/10.1093/biomtc/ujae089) · [arXiv](https://arxiv.org/abs/2307.11941) — Visibility graph-based covariance functions for scalable spatial analysis in non-convex partially Euclidean domains
- **作者**: Brian Gilbert, Abhirup Datta
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对非凸部分欧几里得域（如水体）中的空间高斯过程建模，提出基于可见性图（visibility graph）的协方差函数构造方法，以解决标准测地距离协方差函数在该类域上不保证正定性、而现有非欧方法又无法保留部分欧几里得性的问题。方法核心是：利用域内可见图定义连通性，对直接连通的点对保留欧几里得距离协方差，对非连通点对通过条件独立性假设引入非凸几何影响，从而构造合法（正定）且边缘平稳的协方差函数。理论部分证明了该方法在全部参数空间上保持正定性和边缘平稳性，这是已有方法未必满足的性质。计算方面，提供了有用近似以降低计算复杂度，实现可扩展算法。模拟研究在合成非凸域上对比了竞争方法，并应用于切萨皮克湾酸度数据，展示了实际生态监测中的潜力。对您而言，本文的可扩展算法设计和正定性理论框架可作为统计计算（特别是近似算法与数值方法）的一个具体案例，也可为非参数高斯过程建模提供域约束下的新思路。
- **关键技术**: `visibility graph`, `Gaussian process`, `covariance function`, `positive definiteness`, `marginal stationarity`, `scalable algorithm`, `partial Euclidean domain`
- **为什么对您有用**: 本文与您的主要兴趣“统计计算（numerical methods, algorithm）”直接相关，其中为降低计算复杂度而设计的近似策略属于可扩展算法，可借鉴于您熟悉的统计计算工具箱。此外，协方差函数的正定性证明涉及非参数理论，与您 moderately_familiar 的 M-estimation 理论有方法交叉（约束条件下的 valid 构造）。作为一篇 Biometrics 上的方法论 paper，它展示了真实空间数据（切萨皮克湾酸度）的应用，若您未来涉足环境流行病学应用方向，本文的分析流程（域构造→协方差设计→可扩展推断→案例研究）可作为参考模板。当前您对空间统计并不专门，但若想将统计计算能力拓展到地理空间建模，本文提供了中等复杂度的切入点——您已有的非参数与高维工具足够理解理论部分，但需要补充 spatial domain 和 graph-based 协方差的基础知识（中期可做）。

## 流行病学  *(epidemiology, 9 篇)*

### 1. [10.1093/biomtc/ujae074](https://doi.org/10.1093/biomtc/ujae074) · [arXiv](https://arxiv.org/abs/2308.15770) — Semiparametric inference of effective reproduction number dynamics from wastewater pathogen surveillance data
- **作者**: Isaac H Goldstein, Daniel M Parker, Sunny Jiang, Volodymyr M Minin
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文研究如何从废水病原体监测数据推断有效再生数（effective reproduction number, Rt）的动态变化。核心设定是一个时变泊松移民过程，新感染到达率被参数化为 Rt 与当前感染数的乘积，从而避免对易感人群动态的不可验证假设。估计方法采用 semiparametric 框架，结合广义加性模型对感染到达率进行光滑估计，并通过 agent-based 模拟和洛杉矶 SARS-CoV-2 废水数据验证。理论贡献在于提出了一种新的 Rt 识别策略，但本文主要是方法应用与数据实证，未给出严格的 semiparametric efficiency 或 asymptotic normality 理论。对您而言，这是流行病学监测数据建模的一个应用实例，展示了 semiparametric 思想在复杂观测数据中的使用。
- **关键技术**: `semiparametric estimation`, `time-varying Poisson process`, `generalized additive model`, `agent-based simulation`, `effective reproduction number`
- **为什么对您有用**: (1) 连接到流行病学应用方向，展示了 semiparametric 建模在传染病监测数据中的实际使用，但未涉及您核心关注的 efficiency theory 或 debiased ML；(2) 技术层面，本文的 semiparametric 框架较为基础，未触及 HOIF 或 higher-order U-statistics，武器库中的 semiparametric theory（moderately_familiar）足以覆盖其方法核心；(3) 作为 gateway reading，本文适合了解废水监测这一新兴数据源及其统计建模挑战，但若您追求 semiparametric efficiency bound 或 sharper rate，此文深度不足，属于**中期可做**——需先在 semiparametric theory 上积累，才能将更精细的 efficiency 理论带入此类应用问题。

### 2. [10.1093/biomtc/ujae062](https://doi.org/10.1093/biomtc/ujae062) — Absolute risk from double nested case-control designs: cause-specific proportional hazards models with and without augmented estimating equations
- **作者**: Minjung Lee, Mitchell H Gail
- **期刊/来源**: Biometrics
- **机构**: Kangwon National University · National Cancer Institute · Division of Cancer Epidemiology and Genetics
- **分类**: vol 80 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在 competing risks 框架下，目标是利用 double nested case-control (DNCC) 设计数据估计 cause-specific proportional hazards 模型的相对风险和绝对风险（cumulative incidence）。核心方法是设计加权估计量，通过 Samuelsen-type 计算逆抽样概率，并进一步提出 augmented estimating equations 以利用队列全员的部分协变量信息提升效率。理论贡献包括建立估计量的渐近性质、推导绝对风险估计的方差估计量，并证明 augmented 设计加权估计量比普通设计加权估计量更高效。模拟显示有限样本性质良好，实证分析使用前列腺癌死亡率数据。对您而言，这是流行病学背景下 semiparametric efficiency theory 与 augmented IPW 方法的具体应用实例。
- **关键技术**: `augmented estimating equations`, `design-weighted estimators`, `inverse probability weighting`, `cause-specific hazards model`, `competing risks`, `nested case-control design`
- **为什么对您有用**: 连接到 epidemiology 应用因果工作与 semiparametric efficiency theory（augmented estimation 提升效率）。您 very_familiar 的 minimax bounds 与 estimation theory 可用于审视其效率增益是否达到 semiparametric efficiency bound；moderately_familiar 的 semiparametric theory 可帮助理解 augmented estimating equations 的构造原理。**立即可做**：用 semiparametric efficiency bound 验证其 augmented estimator 是否达到效率下界，或扩展到其他 sampling design。

### 3. [10.1093/biomtc/ujae072](https://doi.org/10.1093/biomtc/ujae072) — Improving prediction of linear regression models by integrating external information from heterogeneous populations: James–Stein estimators
- **作者**: Peisong Han, Haoyue Li, Sung Kyun Park, Bhramar Mukherjee, Jeremy M G Taylor
- **期刊/来源**: Biometrics
- **机构**: Gilead Sciences (United States) · University of Michigan
- **分类**: vol 80 · issue 3
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文考虑内部研究基于个体数据拟合线性回归模型用于预测，同时外部研究提供了使用部分协变量子集的简化模型系数估计（无个体数据）。由于不同研究人群存在异质性，直接合并参数可能降低预测精度。作者将James–Stein收缩方法适配于此设置，提出整合外部模型摘要信息的估计量，其在预测均方误差指标上不劣于且常优于仅用内部数据的估计量，且不依赖于异质性程度。通过广泛的模拟研究验证了估计量的数值性能，并应用于整合已发表文献的摘要信息以改进基于血铅水平等协变量预测髌骨骨铅水平的模型。该方法本质上是一种经验贝叶斯收缩策略，能够自动权衡内部数据与外部信息的权重。对于您从事流行病学数据分析或因果推断中的预测性外推问题，本文提供了一个直接可用的工具框架，可帮助利用外部汇总统计提高模型稳健性。
- **关键技术**: `James–Stein shrinkage`, `linear regression prediction`, `external information integration`, `multi-study heterogeneity`, `mean squared error evaluation`
- **为什么对您有用**: 该论文直接应用于流行病学预测问题（髌骨骨铅水平），属于您的secondary interest。方法核心是James–Stein收缩，您可借助estimation theory（很熟悉）分析其MSE性质与最优收缩系数，并将其推广到因果推断中的外推场景（如利用外部汇总数据改进ATE预测）。中期可做：需先在中度熟悉的identification theory中建立预测与因果的联系。当前文献暂不涉及因果识别，但方法本身可作为工具直接使用（立即可做）。

### 4. [10.1093/biomtc/ujae083](https://doi.org/10.1093/biomtc/ujae083) · [arXiv](https://arxiv.org/abs/2303.05223) — LEAP: the latent exchangeability prior for borrowing information from historical data
- **作者**: Ethan M Alt, Xiuya Chang, Xun Jiang, Qing Liu, May Mo, Hong Amy Xia et al.
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文提出潜交换性先验（LEAP），用于从历史数据中有选择地借用信息。与传统先验（如power prior、commensurate prior）对所有历史观测统一折扣不同，LEAP通过潜变量将历史观测分为可交换与不可交换两组，仅对与当前数据可交换的历史子集施以信息借用。该方法解决了倾向得分方法仅关注协变量分布而忽视结局参数交换性的局限。在模拟中，LEAP在历史数据异质性高时优于现有方法，并在银屑病Ⅲ期临床试验的不平衡随机化设计中成功增补对照臂。对您而言，本文是流行病学临床试验中借用历史数据的新工具，其潜变量分类思想可与您熟悉的非参数估计（如逆概率加权）结合，但核心贝叶斯推断（MCMC、先验构造）不在您武器库中，目前暂不可直接复现，可作为方向拓展的入门阅读。
- **关键技术**: `Latent exchangeability prior`, `Bayesian borrowing`, `Propensity score sub-classification`, `Power prior`, `Meta-analytic predictive prior`, `Clinical trial control arm augmentation`
- **为什么对您有用**: 1) 连接至流行病学次级兴趣：本文直接处理临床试验中借用历史数据的问题，有真实数据案例（银屑病III期试验），符合您对应用因果/统计方法的关注。2) 方法层面：潜变量分类的思想与因果推断中的子分类/分层方法相通，可尝试用您very_familiar的非参数估计或M-estimation框架重新表述。3) 暂不可做：核心贝叶斯推断（潜变量先验、MCMC）不在武器库中，需先熟悉贝叶斯方法或寻找非贝叶斯替代策略。

### 5. [10.1093/biomtc/ujae097](https://doi.org/10.1093/biomtc/ujae097) — Designing cancer screening trials for reduction in late-stage cancer incidence
- **作者**: Kehao Zhu, Ying-Qi Zhao, Yingye Zheng
- **期刊/来源**: Biometrics
- **机构**: University of Washington · Fred Hutch Cancer Center
- **分类**: vol 80 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对早期癌症筛查生物标志物临床试验设计的独特挑战（疾病自然进展漫长、筛查效果时变、缺乏时间尺度信息），提出基于通用多状态疾病历史模型的模型化效应量方法。该方法将测试灵敏度等关键性能指标与晚期癌症发病率这一主要终点直接关联，同时整合真实筛查程序（如重复检测次数和间隔）的实施细节。基于随机对照试验的日历时间尺度，研究者可评估检验功效随新筛查项目特征（灵敏度、随访时长、检测频率）的变化。作者提供了计算工具，并通过国家肺筛查试验数据演示了方法。对您而言，该工作直接对应于流行病学中筛查试验的功率计算与设计优化，其多状态建模思路还可迁移至纵向因果推断中时变处理效应的估计。
- **关键技术**: `multistate disease model`, `model-based effect size`, `time-varying screening effect`, `screening trial power calculation`, `early detection biomarker evaluation`
- **为什么对您有用**: 本文属于流行病学中筛查试验设计方法，与研究者对流行病学数据和应用因果工作的兴趣直接相关。您 familiar 的 estimation theory in causal inference 可用于检查该模型中的因果假设（如无混淆、测量误差），而软件开发技能可用于实现或扩展其计算工具。对本文的 follow-up 可立即可做：直接使用其提供数值工具复现或调整至不同癌症筛查场景。

### 6. [10.1093/biomtc/ujae092](https://doi.org/10.1093/biomtc/ujae092) · [arXiv](https://arxiv.org/abs/2404.06837) — Sensitivity analysis for publication bias in meta-analysis of sparse data based on exact likelihood
- **作者**: Taojun Hu, Yi Zhou, Satoshi Hattori
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 针对稀疏数据元分析中发表偏倚的敏感性分析问题，传统正态-正态随机效应模型因正态近似在低事件率时不准确导致推断偏差。本文扩展了Copas基于t统计量选择函数的似然敏感性分析框架到广义线性混合模型（GLMM），采用精确似然替代近似正态模型。方法通过联合建模效应大小和发表机制，利用选择函数刻画发表偏倚，并通过极大似然估计进行敏感性分析。模拟和真实数据应用表明，所提方法显著优于基于正态近似的方法，尤其在稀疏数据场景下偏差更小、覆盖率更稳定。该方法为流行病学元分析中的发表偏倚评估提供了更可靠的工具，且其似然推断框架可直接与因果推断中的敏感性分析方法对话。对研究者而言，本文是流行病学应用方法的优质入门读物，技术武器库中的M-estimation理论足以理解其估计框架。
- **关键技术**: `sensitivity analysis`, `publication bias`, `generalized linear mixed model`, `exact likelihood`, `Copas selection function`, `meta-analysis`
- **为什么对您有用**: 本文直接涉及流行病学元分析中的发表偏倚敏感性分析，属于次要兴趣方向。研究者武器库中的M-estimation理论可解析其似然推断结构，且因果推断中的敏感性分析思路可与此交叉。作为流行病学应用方法的gateway reading，本文模型清晰、可读性强，武器库足以支撑理解，值得读全文。

### 7. [10.1093/biomtc/ujae068](https://doi.org/10.1093/biomtc/ujae068) · [arXiv](https://arxiv.org/abs/2208.03157) — A Gaussian-process approximation to a spatial SIR process using moment closures and emulators
- **作者**: Parker Trostle, Joseph Guinness, Brian J Reich
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 该论文针对空间传染病传播的推断难题，提出了一种高斯过程（GP）近似方案。首先定义了一个空间扩展的SIR随机过程，随后利用矩闭包（moment closure）推导出易感者和感染者的均值与协方差随时间演化的常微分方程组（ODE）。由于ODE作为MCMC拟合的瓶颈，作者进一步采用低秩仿真器（low-rank emulator）近似ODE的解，作为层次模型的基石，处理带噪声和低报的新增感染计数数据。在模拟数据上验证了推断性能，并应用于2015–2016年巴西寨卡病毒的实际感染数据。该方法的核心亮点是将复杂的空间随机过程压缩为可计算的GP框架，保留了传播动力学的关键特征。对您而言，这是一篇流行病学中统计建模的扎实应用，其矩闭包与仿真器结合的技术思路可迁移到其他含潜在过程的纵向数据建模场景（如你的因果推断中的纵向设置）。
- **关键技术**: `moment closure`, `Gaussian process emulator`, `low-rank approximation`, `spatial SIR model`, `ODE approximation`
- **为什么对您有用**: 本文直接对应你对流行病学（secondary interest）中数据集和分析模式的兴趣，提供了一个完整的空间传播建模案例。你非常熟悉的统计计算和软件开发技能（`technical_arsenal`中`very_familiar`的软件开发和逆问题处理）可用于实现或扩展其矩闭包-仿真器框架，例如设计更高效的降维方案或不确定性量化方法。目前可视为**立即可做**：用你的统计计算经验复现其仿真部分、测试不同低秩近似对推断质量的影响，是进入这一应用领域的低门槛入口。

### 8. [10.1093/biomtc/ujae060](https://doi.org/10.1093/biomtc/ujae060) — PathGPS: discover shared genetic architecture using GWAS summary data
- **作者**: Zijun Gao, Qingyuan Zhao, Trevor Hastie
- **期刊/来源**: Biometrics
- **机构**: University of Southern California · University of Cambridge · Institute of Mathematical Statistics · Stanford University
- **分类**: vol 80 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: PathGPS提出一种基于GWAS摘要数据的探索性分析工具，通过线性结构方程模型将性状的遗传与环境成分解耦。该方法通过对比“信号”基因与“噪音”基因的GWAS关联来估计遗传成分。随后利用主成分分析和因子分析提取低秩稀疏的遗传路径。采用bagging集成策略以提高对数据扰动和超参数选择的稳健性。在代谢组学数据和UK Biobank的应用中，PathGPS复现了已知的基因-性状聚类并生成多个新假设。该工作为遗传流行病学中共享遗传架构的发现提供了一个实用的统计框架。
- **关键技术**: `Linear structural equation model`, `Principal component analysis`, `Factor analysis`, `Bootstrap aggregating (bagging)`, `GWAS summary data`
- **为什么对您有用**: 本文属于流行病学应用，利用因果推断中的结构方程模型思想从GWAS摘要数据中分离遗传和环境影响。研究者的因果推断工具箱（尤其是线性SEM）可帮助理解方法假设，但GWAS数据的特殊结构和术语可能需要额外入门。整体而言，本文可作为进入遗传流行病学统计方法的良好读物，值得花时间阅读全文。研究者现有知识足以理解核心方法（立即可做），但若需原创性跟进，需补充GWAS质量控制等流行病学专门知识（中期可做）。

### 9. [10.1093/biomtc/ujae075](https://doi.org/10.1093/biomtc/ujae075) · [arXiv](https://arxiv.org/abs/2308.10583) — The multivariate Bernoulli detector: change point estimation in discrete survival analysis
- **作者**: Willem van den Boom, Maria De Iorio, Fang Qian, Alessandra Guglielmi
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文研究离散时间 competing risks 场景下的变点估计问题，目标是在多因失败时间数据中识别各风险基线 hazard 的变点位置与数量。方法上提出 multivariate Bernoulli detector，采用 Bayesian nonparametric prior 对变点数量与位置建模，并通过 multivariate Bernoulli prior 捕捉不同风险之间变点的依赖结构。推断采用 tailored MCMC 算法，结合 data augmentation 与 nonconjugate 更新策略，聚焦 cause-specific hazard rates 与跨风险依赖的后验估计。模拟与 ICU 数据实证表明方法在变点检测准确性上优于忽略 competing risks 或连续时间近似的方法。对您而言，这是一篇 epidemiology 领域的 applied Bayesian 方法论文，方法学 novelty 有限。
- **关键技术**: `competing risks model`, `discrete-time survival analysis`, `Bayesian nonparametric prior`, `change point detection`, `MCMC with data augmentation`
- **为什么对您有用**: 本文属于 epidemiology 应用文，使用真实 ICU 数据集，适合作为 competing risks 与离散生存分析的入门阅读。方法核心是 Bayesian nonparametric 与 MCMC，不在您的 technical_arsenal 中（您更熟悉 frequentist semiparametric theory 与 efficiency bounds），因此难以用现有武器库直接攻入或迁移。建议作为 gateway reading 快速浏览数据结构与模型设定，若对 competing risks 的 identification theory 有兴趣可进一步追踪文献，否则无需精读。

## 其他  *(other, 4 篇)*

### 1. [10.1093/biomtc/ujae081](https://doi.org/10.1093/biomtc/ujae081) · [arXiv](https://arxiv.org/abs/2308.12859) — Towards automated animal density estimation with acoustic spatial capture-recapture
- **作者**: Yuheng Wang, Juan Ye, Xiaohui Li, David L Borchers
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本研究针对被动声学监测中物种自动识别产生的假阳性问题，提出一种声学空间捕获-再捕获（ASCR）方法。该方法将物种身份视为潜变量，将机器学习个体级检测结果视为依赖于潜身份的随机变量，从而构建混合模型似然并通过最大化来估计呼叫密度。与现有常见的“校正因子”方法相比，该方法在真实蛙类调查和基于长臂猿声学数据模拟的实验中，估计结果更接近无假阳性时的ASCR基准。模拟表明该方法偏差接近零、覆盖概率准确，且远优于忽略假阳性的传统ASCR。该工作将统计模型与机器学习输出有机结合，为生态统计中的测量误差问题提供了新思路。
- **关键技术**: `latent variable mixture model`, `acoustic spatial capture-recapture (ASCR)`, `maximum likelihood estimation`, `false positive handling`, `machine learning detection output`
- **为什么对您有用**: 该文提出的潜变量混合模型框架与您在因果推断中通过负对照处理测量误差的思想在结构上有相通之处；同时，将机器学习分类输出作为随机变量纳入统计模型，对您在高维统计或半参估计中处理噪声预测变量具有方法学参考价值。但该文属于生态统计应用，与您主要兴趣（因果推断、高维统计等）距离较远，暂不构成直接可做的问题，可作为gateway-reading了解潜变量技术在该领域的应用。

### 2. [10.1093/biomtc/ujae066](https://doi.org/10.1093/biomtc/ujae066) — An interpretable Bayesian clustering approach with feature selection for analyzing spatially resolved transcriptomics data
- **作者**: Huimin Li, Bencong Zhu, Xi Jiang, Lei Guo, Yang Xie, Lin Xu et al.
- **期刊/来源**: Biometrics
- **机构**: The University of Texas at Dallas · Chinese University of Hong Kong · Southern Methodist University · Southwestern Medical Center · The University of Texas Southwestern Medical Center
- **分类**: vol 80 · issue 3
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对空间转录组学（SRT）数据的聚类问题，提出了一个结合特征选择的贝叶斯混合模型。模型假设观测服从 zero-inflated negative binomial 分布以刻画 SRT 数据的稀疏性与 overdispersion，通过 spike-and-slab 先验实现基因层面的特征选择，提升聚类结果的可解释性。空间依赖性通过 Markov random field (MRF) 先验引入，利用邻接结构约束相邻 spot/cell 倾向于属于同一 cluster。理论层面未给出严格的收敛率或后验收缩结果，主要通过模拟与三个真实数据集展示相较于现有方法在聚类准确性与特征选择稳定性上的提升。本文属于生物统计方法应用，核心工具是贝叶斯分层建模与 MCMC 推断，对您 primary interests 中的因果推断、高维理论或效率理论无直接贡献。
- **关键技术**: `zero-inflated negative binomial mixture model`, `spike-and-slab prior`, `Markov random field prior`, `Bayesian clustering`, `feature selection`, `spatially resolved transcriptomics`
- **为什么对您有用**: 本文属于生物统计应用，与您 primary interests（因果推断、高维统计、效率理论、U-statistics）的核心方法学方向无直接交集。技术工具（贝叶斯分层模型、MRF 先验、MCMC）不在您 technical_arsenal 的熟悉范围内，且本文未涉及 semiparametric efficiency、debiasing、或高维推断理论。作为流行病学/生物统计的数据分析案例，其数据结构（空间转录组）与因果推断或高维理论的连接较弱。follow-up 判断：**暂不可做**——核心机器（贝叶斯空间模型、MCMC）不在武器库中，且主题与您当前研究议程偏离。

### 3. [10.1093/biomtc/ujae059](https://doi.org/10.1093/biomtc/ujae059) — Bayesian inference for multivariate probit model with latent envelope
- **作者**: Kwangmin Lee, Yeonhee Park
- **期刊/来源**: Biometrics
- **机构**: Chonnam National University · University of Wisconsin–Madison
- **分类**: vol 80 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文将响应包络（response envelope）模型从连续响应扩展到多元二元响应，提出probit包络模型。该模型利用潜变量包络结构识别响应的物质部分与无关部分，旨在提高回归系数的估计效率。通过essential identifiability概念解决模型可识别性问题，并采用贝叶斯方法进行参数估计。模拟研究表明，相比标准多元probit模型，probit包络模型在估计上具有潜在效率提升。实际数据分析展示了该模型在多标签分类中的实用性。本文的方法将包络降维思路引入离散潜变量模型，与高维统计中的降维效率问题直接相关。
- **关键技术**: `response envelope`, `multivariate probit model`, `latent variable`, `essential identifiability`, `Bayesian inference`, `multi-label classification`
- **为什么对您有用**: 该论文将包络降维方法引入离散响应模型，属于高维统计中提高估计效率的技术，与您对高维统计和半参数效率理论的兴趣有交集。使用您熟悉的minimax bound工具可分析该模型的理论效率增益是否最优。中期可做，因为需要先熟悉包络模型的识别与贝叶斯计算细节。

### 4. [10.1093/biomtc/ujae093](https://doi.org/10.1093/biomtc/ujae093) — A Bayesian latent-subgroup platform design for dose optimization
- **作者**: Rongji Mu, Xiaojiang Zhan, Rui (Sammi) Tang, Ying Yuan
- **期刊/来源**: Biometrics
- **机构**: Shanghai Jiao Tong University · The University of Texas MD Anderson Cancer Center
- **分类**: vol 80 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在肿瘤药物剂量优化（FDA Project Optimus）背景下，目标是同时识别多个适应症下新药联合标准护理的最优生物学剂量（OBD）。方法采用主方案平台试验设计，核心是 Bayesian latent subgroup model 用于刻画不同适应症间的治疗异质性，并通过 Bayesian hierarchical model 在亚组内借力信息。估计量更新基于后验分布，决策规则依赖 utility-based risk-benefit tradeoff，通过 interim analysis 动态调整剂量升降。模拟研究显示设计具有满意的 operating characteristics，可缩短药物开发周期。本文属于临床试验设计的方法学创新，对您 primary interest 中的因果推断理论贡献有限，但可作为流行病学/临床试验应用背景的 gateway reading。
- **关键技术**: `Bayesian latent subgroup model`, `Bayesian hierarchical model`, `platform trial design`, `utility-based dose optimization`, `interim analysis`, `master protocol`
- **为什么对您有用**: 本文属于临床试验设计领域，与您 primary interest 中的因果推断理论、高维统计、效率理论等技术方向无直接交集。核心机器（Bayesian latent subgroup model、hierarchical borrowing）不在您熟悉的 minimax bounds、semiparametric efficiency、higher-order U-statistics 等武器库内。**暂不可做**：若要进入此方向，需先补充 Bayesian adaptive design 和 decision-theoretic utility framework 的基础知识。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

