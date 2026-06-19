# Biometrics — Vol 81  Issue 1  ·  2026-06-19

- 共 19 篇 · Biometrics
- 目录核对 ⚠️ 疑似漏 19 篇（对照 OpenAlex 38 篇）：10.1093/biomtc/ujae167、10.1093/biomtc/ujaf015、10.1093/biomtc/ujaf014、10.1093/biomtc/ujaf001、10.1093/biomtc/ujae160 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期以因果推断方法为主体，覆盖多种复杂数据结构和识别策略，同时半参数/非参模型、高维协方差回归、流行病学纵向建模等方向亦有推进。可将论文大致聚为四条主线：**因果识别与估计**（交叉时序设计、惩罚G估计、工具变量+竞争风险、整群加权、最优治疗规则、群序贯协变量调整）、**半参数/非参推断**（变点检验、部分线性函数Cox、二元分布回归均值）、**高维协方差回归**（正定约束ADMM）、**流行病学应用与混合效应模型**（非线性子组识别、分布式滞后插补、非线性混合效应、组群检测贝叶斯）。

因果推断主线最为密集。交叉时序设计通过共同趋势假设替代排除限制，在工具变量框架下以贝叶斯程序估计因果效应，对常见趋势违反相对稳健。惩罚G估计在纵向时变暴露的SNMM中，利用L1/自适应Lasso同时选择效应修饰变量并估计因果效应，具有双重稳健性和oracle性质。工具变量+区间删失竞争风险一文将转变模型（含Fine-Gray）推广至内生治疗选择下的compiler因果效应，半参数估计量一致且渐近正态。整群随机实验的选择偏差问题通过逆概率加权与主分层识别总体子群效应，配套敏感性分析。最优治疗规则那篇则关注RCT中MI与Q-learning/value search的衔接难题，暴露了算法选择与插补模型的非标准挑战。群序贯设计一文为协变量调整构建了具有独立增量结构的检验序列，将半参数有效估计的GSD理论推广至任意正则渐近线性估计量。

半参数/非参主线中，广义半参数分段模型针对变点位置与系数联合估计，基于半光滑方程实现根n一致性与渐近效率，检验使用平均得分型统计量且渐近分布精确。高维部分线性函数Cox模型结合group SCAD与B样条逼近，在发散维数下分析函数型协变量对生存的非线性影响。回归均值一文在任意二元分布下分解条件均值差异，无需正态假设，为pre-post因果推断的RTM校正提供M估计理论基础。

与因果推断/半参数效率最贴的论文包括：交叉时序设计、惩罚G估计、工具变量+竞争风险、整群加权、群序贯协变量调整，以及广义半参数分段模型和高维部分线性函数Cox。高维协方差回归一文的正定约束ADMM算法亦对涉及协方差回归的设置具有参考价值。

## 因果推断  *(causal_inference, 6 篇)*

### 1. [10.1093/biomtc/ujae163](https://doi.org/10.1093/biomtc/ujae163) — Causal inference with cross-temporal design
- **作者**: Yi Cao, Pedro L Gozalo, Roee Gutman
- **期刊/来源**: Biometrics
- **机构**: Novartis (Switzerland) · Tris Pharma (United States) · Brown University · Department of Health Services
- **分类**: vol 81 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文提出交叉时序设计（cross-temporal design），用于观察性研究中的因果效应估计，以在鼓励无法随机化时模拟随机鼓励实验。核心识别假设是用时间趋势的共同趋势假设（common trends assumption）替代传统的排除限制（exclusion restriction），从而区分时间混杂与干预效应。估计采用贝叶斯程序，在模拟中与工具变量法和匹配法比较，结果表明贝叶斯方法在估计精度上更优，且对共同趋势假设的违反相对稳健。文章进一步将方法应用于Medicare Advantage（MA）扩张（2011-2017）背景下，估计MA参保对出院后30天内再住院风险的影响。该工作直接触及因果推断中工具变量设计的替代识别策略，其贝叶斯框架与常见的半参/双机器学习方法形成对照，适用于流行病学队列研究。对您而言，本文的识别策略（以时间维度模拟随机化）可与您的identification theory知识对接，而贝叶斯估计的有限样本表现值得用您熟悉的估计理论（如finite-sample bounds）进一步审视。
- **关键技术**: `cross-temporal design`, `common trends assumption`, `Bayesian causal inference`, `instrumental variables`, `encouragement design`, `Medicare Advantage application`
- **为什么对您有用**: 本文直接对应您的primary interest“causal inference”中的IV设计，提出了新的识别策略（用时间趋势假设替代排除限制），属于identification theory的拓展。您的very_familiar工具“estimation theory in causal inference”可用于评估贝叶斯估计器与频繁学替代（如GMM）的有限样本差异，而moderately_familiar的“identification theory”是理解并扩展本文假设（如放松共同趋势）的必要基础。follow-up粗判：中期可做——需先在moderately_familiar的identification theory上长肌肉，才能系统分析本文识别假设的可检验性及其替代方案。

### 2. [10.1093/biomtc/ujae165](https://doi.org/10.1093/biomtc/ujae165) · [arXiv](https://arxiv.org/abs/2402.00154) — Penalized G-estimation for effect modifier selection in a structural nested mean model for repeated outcomes
- **作者**: Ajmery Jaman, Guanbo Wang, Ashkan Ertefaie, Michèle Bally, Renée Lévesque, Robert W Platt et al.
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在重复结局的时变暴露结构嵌套均值模型(SNMM)框架下，研究效应修饰变量的选择问题，目标是在存在时变混杂时估计条件平均处理效应的异质性。作者提出一种双重稳健的惩罚G估计量，通过在估计方程中引入L1或自适应Lasso惩罚，同时实现效应修饰变量的选择和因果效应的估计。理论部分证明了该估计量具有oracle性质，即模型选择一致且渐近正态。估计量采用双重稳健结构，只要倾向性得分或结局模型之一正确，就能得到一致估计。模拟研究验证了有限样本下的选择性能和双重稳健性，实际数据应用于血液透析患者重复治疗效果的异质性分析。该工作为纵向因果推断中的效应修饰识别提供了可直接使用的双重稳健工具，与研究者对纵向因果推断和半参数效率理论的兴趣高度相关。
- **关键技术**: `structural nested mean models`, `penalized G-estimation`, `oracle property`, `doubly robust estimation`, `effect modifier selection`, `time-varying confounding`
- **为什么对您有用**: 本文直接对应主要兴趣中的纵向因果推断（时变暴露的效应修饰识别）和双重稳健估计（半参数效率理论）。研究者可用 `very_familiar` 中的因果推断估计理论和高维渐近工具轻松理解其 oracle 性质证明，并评估惩罚方法在自身纵向数据分析中的适用性。立即可做：无需额外工具即可读懂全文，并可进一步探讨将惩罚G估计扩展到工具变量或近端因果推断设定。

### 3. [10.1093/biomtc/ujaf010](https://doi.org/10.1093/biomtc/ujaf010) — Instrumental variable estimation of complier casual treatment effects with interval-censored competing risks data
- **作者**: Yichen Lou, Yuqing Ma, Jianguo Sun, Peijie Wang, Zhisheng Ye
- **期刊/来源**: Biometrics
- **机构**: Chinese University of Hong Kong · Jilin University · University of Missouri · National University of Singapore
- **分类**: vol 81 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文在区间删失竞争风险数据下，研究工具变量估计处理效应的问题。目标估计量是遵循治疗分配（compiler）的因果效应，应用场景为生物统计和流行病学中常见的时间-事件结局。方法基于一类累积发病率函数的转变模型（transformation model），包括子分布比例风险模型（Fine-Gray模型）作为特例，通过工具变量处理内生治疗选择偏差。估计器使用半参数似然或估计方程框架，证明估计量的一致性和渐近正态性。模拟研究表明有限样本性能良好，并应用于乳腺癌筛查研究。这对您因果推断方向中工具变量在复杂删失数据下的扩展提供了具体方法，连接您熟悉的因果推断估计理论（非常熟悉）和非参数统计工具，可立即用类似估计方程思路分析其性质。
- **关键技术**: `instrumental variable`, `transformation model for cumulative incidence function`, `sub-distributional proportional hazards (Fine-Gray model)`, `interval-censored competing risks`, `complier average causal effect (CACE)`
- **为什么对您有用**: 该论文直接针对因果推断中的工具变量方法，在区间删失和竞争风险这一现实但未被充分研究的设定下提出半参数估计，与您的因果推断估计理论（非常熟悉）紧密相连。您可以使用非参数统计和M-估计理论来验证或改进其渐近效率。属于立即可做的方向。

### 4. [10.1093/biomtc/ujaf013](https://doi.org/10.1093/biomtc/ujaf013) · [arXiv](https://arxiv.org/abs/2309.07365) — Addressing selection bias in cluster randomized experiments via weighting
- **作者**: Georgia Papadogeorgou, Bo Liu, Fan Li, Fan Li
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在整群随机化实验中，个体常在群组干预分配后招募，导致招募样本与总体及各干预组间存在选择偏差。本文定义了总体与招募样本的平均因果效应（ATE）作为目标 estimand，并在可忽略招募（ignorable recruitment）假设下证明：对招募人群的 ATE 可通过逆概率加权（IPW）一致估计。总体 ATE 一般不可识别，但通过主分层（principal stratification）框架，本文证明可利用加权识别总体的两个有意义子群（always-recruited 与 treatment-recruited）的因果效应。估计策略结合了 IPW 与主分层，并开发了针对可忽略招募假设的敏感性分析方法，已封装为 R 包 CRTrecruit。对您可能有用：本文将主分层与 IPW 结合处理选择偏差的框架，可直接迁移至流行病学队列或经济评估中的 post-treatment selection 问题。
- **关键技术**: `inverse probability weighting`, `principal stratification`, `ignorable recruitment assumption`, `sensitivity analysis`, `cluster randomized experiments`
- **为什么对您有用**: 本文直接连接到因果推断中的主分层与选择偏差识别，属于您 primary interest 中 identification theory 与 sensitivity analysis 的具体应用场景。您武器库中 very_familiar 的 estimation theory in causal inference 与 moderately_familiar 的 identification theory 可直接攻破本文的 IPW 估计与主分层识别逻辑，敏感性分析部分也可用 semiparametric theory 框架审视其效率与鲁棒性边界。**立即可做**：用 very_familiar 的因果推断估计理论审视其 IPW estimator 的 semiparametric efficiency bound 是否可达，或用 moderately_familiar 的 identification theory 探索在更弱假设下总体 ATE 的部分识别边界。

### 5. [10.1093/biomtc/ujaf026](https://doi.org/10.1093/biomtc/ujaf026) — Optimal treatment regime estimation in practice: challenges and choices in a randomized clinical trial for depression
- **作者**: Florian Stijven, Trung Dung Tran, Ellen Driessen, Ariel Alonso Abad, Geert Molenberghs, Geert Verbeke et al.
- **期刊/来源**: Biometrics
- **机构**: KU Leuven · Pro Persona · Hasselt University
- **分类**: vol 81 · issue 1
- 相关性 5/10 · novelty: `application`
- **摘要**: 在随机临床试验的 precision medicine 设定下，目标是估计最优治疗规则（optimal treatment regime, OTR），即将基线特征映射到治疗选择以最大化期望获益的决策规则。本文对心境恶劣障碍 RCT 数据进行再分析，采用 Q-learning 与 value search estimation 两种主流 OTR 估计方法。核心挑战在于缺失数据处理：采用多重插补（MI），但 MI 与 OTR 估计的衔接涉及非标准统计问题（如插补模型与决策规则的兼容性、Rubin's rule 的适用性）。Value search 的具体实现亦带来优化与搜索策略的选择难题。文章详述了所有分析决策及其动机，本质上是一篇应用导向的实践指南，而非方法学创新。对您有用之处在于：它展示了 OTR 估计在真实 RCT 中的完整 pipeline 与痛点，可作为因果推断中个体化治疗规则估计的应用案例参考。
- **关键技术**: `optimal treatment regime estimation`, `Q-learning`, `value search estimation`, `multiple imputation`, `precision medicine`, `randomized clinical trial`
- **为什么对您有用**: 本文连接到因果推断中的个体化治疗规则（OTR）估计子方向，展示了 Q-learning 与 value search 在真实 RCT 缺失数据下的实现细节与痛点。从您的 technical_arsenal 看，identification theory in causal inference 与 M-estimation theory（moderately_familiar）可以用来审视本文中 MI 与 OTR 估计结合时的 identification 与 M-estimation 一致性问题——这是一个值得深挖的理论口子。Follow-up 粗判：**中期可做**——需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以严格分析 MI+OTR 联合估计的渐近性质；本文本身作为应用实践指南，值得花时间读全文以了解 OTR 真实数据分析的完整流程与常见陷阱。

### 6. [10.1093/biomtc/ujaf020](https://doi.org/10.1093/biomtc/ujaf020) · [arXiv](https://arxiv.org/abs/2201.12921) — Combining covariate adjustment with group sequential, information-adaptive designs to improve randomized trial efficiency
- **作者**: Kelly Van Lancker, Joshua F Betz, Michael Rosenblum
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在随机化试验的 group sequential design (GSD) 设定下，目标是结合协变量调整与早期停止规则以同时提升精度与效率，关键假设是 estimator 具有常规、渐近线性性质。核心挑战之一是调整估计量（如 ANCOVA / efficient influence function estimator）在跨分析时间点缺乏独立增量结构，作者通过线性变换构造出一组保持一致性、渐近正态性且具有独立增量性质的估计量序列，精度不降或提升，该结果将基于 semiparametric efficient estimator 的 GSD 基础理论推广至任意 regular asymptotically linear (RAL) 估计量。第二个挑战是试验规划时协变量预后价值的不确定性会导致 power 误算，提出 information-adaptive design，即持续招募直至达到所需信息水平，避免 over/underpowered。对您可能有用：本文将 semiparametric efficient / RAL 估计量的独立增量结构问题给出了显式线性变换解法，直接连接 semiparametric efficiency theory 与 longitudinal / sequential 试验设计。
- **关键技术**: `group sequential design`, `independent increments property`, `regular asymptotically linear estimator`, `semiparametric efficient estimator`, `information-adaptive design`, `covariate adjustment`
- **为什么对您有用**: 直接连接 causal inference 中的协变量调整估计与 semiparametric efficiency theory（RAL / efficient influence function），属于试验设计中的 estimation theory 问题。您武器库中的 semiparametric theory 与 M-estimation theory（moderately_familiar）可以直接攻破本文 RAL 估计量线性变换的独立增量结构推导与信息量计算口子。**立即可做**：用 very_familiar 的 estimation theory in causal inference 验证其线性变换在不同调整估计量（如 IPW / DR）下的精度保持条件，并可扩展至 longitudinal 设置。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1093/biomtc/ujaf017](https://doi.org/10.1093/biomtc/ujaf017) — Positive-definite regularized estimation for high-dimensional covariance on scalar regression
- **作者**: Jie He, Yumou Qiu, Xiao-Hua Zhou
- **期刊/来源**: Biometrics
- **机构**: Nanjing University of Aeronautics and Astronautics · Peking University
- **分类**: vol 81 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在高维协方差回归设定下，目标是在给定协变量时估计条件平均协方差矩阵的回归系数，同时满足正定约束与稀疏性。核心挑战在于正定约束对回归参数施加的充要条件使得优化问题非标准；作者提出正定约束下的正则化估计，并设计 ADMM 算法求解该约束+稀疏优化问题，证明了算法收敛。理论上给出了回归系数与异质协方差估计的收敛速率，模拟与脑连接数据实证验证了方法。对您有用：该文的高维协方差回归+正定约束 ADMM 框架直接触及高维统计与统计计算交叉点，可作为协方差回归这一子方向的入门参考。
- **关键技术**: `covariance regression`, `positive-definite constraint`, `ADMM algorithm`, `regularized estimation`, `convergence rate`, `high-dimensional covariance`
- **为什么对您有用**: 直接连接高维统计（协方差矩阵回归与收敛速率）与统计计算（ADMM 算法设计）两个 primary interest 子方向。您武器库中的 very_familiar（高维渐近理论、软件开发）可直接复现并审视其 ADMM 收敛证明与速率界是否紧；若想深挖理论，可用 moderately_familiar 的 M-estimation theory 检查其正则化估计的渐近性质是否达到 minimax rate。Follow-up 判断：立即可做——用 very_familiar 工具即可复现算法并验证速率界。

## 非参数 / 半参数  *(nonparam_semipara, 3 篇)*

### 1. [10.1093/biomtc/ujaf022](https://doi.org/10.1093/biomtc/ujaf022) — Statistical inference on change points in generalized semiparametric segmented models
- **作者**: Guangyu Yang, Baqun Zhang, Min Zhang
- **期刊/来源**: Biometrics
- **机构**: Renmin University of China · Shanghai University of Finance and Economics · Vanke (China) · Tsinghua University
- **分类**: vol 81 · issue 1
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 在广义半参数分段模型（segmented model）设定下，研究变点的存在性检验与位置估计，目标参数包含变点位置及分段回归系数。核心估计机制基于半光滑估计方程（semismooth estimating equation）实现变点估计，检验机制则采用平均得分型检验（average score-type test）判断变点是否存在。理论上严格证明了所有参数估计量的根n一致性、渐近正态性及渐近效率，并推导了检验统计量在零假设下的精确渐近分布。模拟与BCBS真实流行病学数据应用验证了方法性能，成功识别了基线GFR与BMI对出血干预的变点效应。对您有用：该框架的渐近效率论证与得分型检验构造，直接关联您关注的半参数效率界与假设检验理论。
- **关键技术**: `semismooth estimating equation`, `average score-type test`, `root-n consistency`, `asymptotic efficiency`, `generalized semiparametric segmented model`, `change-point estimation`
- **为什么对您有用**: 本文直接关联您primary interest中的半参数效率界与假设检验子方向，其平均得分型检验与渐近效率证明是您熟悉的semiparametric theory的具体实例。您可用very_familiar中的M-estimation theory与moderately_familiar中的semiparametric theory审视其效率界是否达到semiparametric efficiency bound，或用HOIF视角探索更高阶修正能否改善变点估计的收敛。follow-up判断：**立即可做**——用现有武器库即可复现其效率论证并尝试HOIF扩展。

### 2. [10.1093/biomtc/ujae164](https://doi.org/10.1093/biomtc/ujae164) — High-dimensional partially linear functional Cox models
- **作者**: Xin Chen, Hua Liu, Jiaqi Men, Jinhong You
- **期刊/来源**: Biometrics
- **机构**: Shanghai Lixin University of Accounting and Finance · Xi'an Jiaotong University · Shanghai University of Finance and Economics
- **分类**: vol 81 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在高维部分线性函数 Cox 模型设定下，目标是对含函数型协变量的生存数据进行估计与变量选择，允许标量协变量与函数主成分（FPC）个数随样本量发散。方法上，对线性部分采用 group SCAD 进行变量选择，对函数协变量的非线性效应采用 B-spline sieve 逼近，在 hazard 模型框架下联合估计。理论贡献主要在于 diverging dimension 下的有限样本性质与收敛率分析，但摘要未明确给出 oracle property 或 minimax rate 的具体界。实证方面通过模拟与肾移植数据集验证了方法，揭示了函数协变量对 hazard 的非线性影响。对您有用之处在于：这是 semiparametric sieve 估计在高维生存分析中的具体应用，可作为 B-spline + penalization 联合框架的参考案例。
- **关键技术**: `partially linear Cox model`, `functional principal component scores`, `group SCAD variable selection`, `B-spline sieve estimation`, `diverging dimension asymptotics`
- **为什么对您有用**: 本文连接到 semiparametric & nonparametric theory 子方向（sieve M-estimation 在高维 Cox 模型的应用）。用您 very_familiar 的 nonparametric statistics 与 high-dimensional asymptotics 武器，可以直接审视其 diverging dimension 下的收敛率是否紧、group SCAD 的 oracle property 是否在函数 Cox 设定下成立。判断：**立即可做**——用 minimax bound 验证其声称的 rate 是否可达下界，或用 M-estimation theory 检查其 sieve + penalization 联合估计的渐近性质。

### 3. [10.1093/biomtc/ujaf033](https://doi.org/10.1093/biomtc/ujaf033) — Regression to the mean for bivariate distributions
- **作者**: Manzoor Khan, Jake Olivier
- **期刊/来源**: Biometrics
- **机构**: Quaid-i-Azam University · UNSW Sydney
- **分类**: vol 81 · issue 1
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 在 pre-post 研究设定下，目标是分解条件均值差异为回归均值效应（RTM）与处理效应之和，以往仅限于二元正态/Poisson/Binomial且假设严苛。本文在更弱假设下推导了任意二元分布的 RTM 表达式，突破了正态性依赖。对指数族推导了 MLE，并证明了其无偏性、一致性与渐近正态性。实证用胆固醇与血压数据展示了 RTM 与处理效应的分解比例。对您可能有用：为 pre-post 因果推断中 RTM 偏差的非参数校正提供了更一般的 semipara/M-estimation 理论基础。
- **关键技术**: `regression to the mean decomposition`, `bivariate distribution theory`, `exponential family MLE`, `asymptotic normality`, `pre-post study design`
- **为什么对您有用**: 连接因果推断的 pre-post 设定中 RTM 偏差校正问题，属于 identification 与 estimation 的交叉。用您 very_familiar 的 M-estimation theory（moderately_familiar）可直接审视其指数族 MLE 的渐近性质与效率；若想推进，可用 semiparametric efficiency bound 检验其 MLE 是否达到半参数有效界，或拓展至非指数族的 one-step/debiased 估计。**立即可做**：用 M-estimation 工具验证其渐近正态性条件是否可进一步弱化。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1093/biomtc/ujae168](https://doi.org/10.1093/biomtc/ujae168) — Improving estimation efficiency for survival data analysis by integrating a coarsened time-to-event outcome from an external study
- **作者**: Daxuan Deng, Lijun Zhang, Hao Feng, Vernon M Chinchilli, Chixiang Chen, Ming Wang
- **期刊/来源**: Biometrics
- **机构**: Pennsylvania State University · Case Western Reserve University · University of Maryland, Baltimore
- **分类**: vol 81 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文聚焦于生存分析中的数据整合问题，主研究拥有连续时间结局和完整协变量，外部研究则包含区间删失的粗化时间结局且仅测量部分协变量。为利用外部信息并处理数据形式异质性，作者基于工作模型通过经验似然获取信息权重，进而构建加权估计量。理论分析表明，新估计量相较于传统仅利用主研究的估计量具有更高的估计效率，且该效率提升对工作模型误设定具有稳健性，模拟研究进一步验证了理论结论。在实证中，作者将方法应用于国家阿尔茨海默病协调中心数据，以改进阿尔茨海默病神经影像学计划一期研究的分析。该方法的核心在于通过经验似然校准权重，实现了跨数据源的信息借入，且无需对数据生成机制做出强参数假设。对您而言，本文的数据整合框架与效率改进理论可迁移至因果推断中的多源数据融合问题，尤其适用于使用较弱识别假设的设定。
- **关键技术**: `empirical likelihood weighting`, `weighted estimating equation`, `data integration with heterogeneous outcomes`, `coarsened time-to-event data`, `robustness to model misspecification`
- **为什么对您有用**: 本文直接对应您的效率理论兴趣（半参数下的估计效率改进），且方法中使用的经验似然加权与您武器库中「非常熟悉」的高维渐近和估计理论高度匹配，易于理解。由于本文未推导达到半参数效率界，您可以用「中等熟悉」的半参数理论工具严格检验其效率上界是否紧致，属于中期可做方向（需先巩固半参数效率界的计算技术）。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1093/biomtc/ujaf012](https://doi.org/10.1093/biomtc/ujaf012) · [arXiv](https://arxiv.org/abs/2402.15460) — Potential outcome simulation for efficient head-to-head comparison of adaptive dose-finding designs
- **作者**: Michael Sweeting, Daniel Slade, Dan Jackson, Kristian Brock
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在剂量寻找试验的模拟研究中，目标是高效比较不同自适应设计的 operating characteristics（如推荐最优剂量的概率）。核心机制是预先模拟所有潜在结果（potential outcomes），即每个受试者在所有剂量水平下的可能反应，随后将同一套预生成数据集依次施加于各竞争设计，从而实现配对式 head-to-head 比较。该方法利用同一 Monte Carlo 样本下两个设计决策的高度正相关，大幅缩减比较性能指标差异时的 Monte Carlo 误差；在 Phase I/II 设计变体的高相关案例中，新方法所需模拟量约为传统方法的 1/48。理论实质是经典的 correlated sampling / common random numbers variance reduction 技术。对您可能有用：此处的 potential outcomes 预模拟与因果推断中的 potential outcomes 框架形式一致，其方差缩减机制可启发您在因果敏感性分析或 IV 模拟中的计算效率优化。
- **关键技术**: `potential outcomes simulation`, `common random numbers variance reduction`, `Monte Carlo error comparison`, `adaptive dose-finding design`, `head-to-head simulation`, `R package escalation`
- **为什么对您有用**: 本文直接连接到统计计算与模拟效率优化，属于 gateway-reading：它将因果推断中熟悉的 potential outcomes 语言用于试验设计的预模拟，实现了显著的方差缩减（common random numbers）。您的 very_familiar 武器库中 software development 与 high-dimensional asymptotics 完全足以支撑进入此方向，甚至可以立即可做：将此 correlated sampling 思路移植到您熟悉的因果推断模拟（如 proximal CI / IV 的 operating characteristics 比较）中，验证方差缩减幅度。作为计算方法论文章，值得花时间读全文以评估该技巧在更复杂 semiparametric estimator 比较场景下的泛化性。

## 流行病学  *(epidemiology, 5 篇)*

### 1. [10.1093/biomtc/ujae169](https://doi.org/10.1093/biomtc/ujae169) — Change surface regression for nonlinear subgroup identification with application to warfarin pharmacogenomics data
- **作者**: Pan Liu, Yaguang Li, Jialiang Li
- **期刊/来源**: Biometrics
- **机构**: National University of Singapore · University of Science and Technology of China · Anhui University of Science and Technology · Anhui Science and Technology University · Anhui University of Technology
- **分类**: vol 81 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在药物基因组学（IWPC 华法林数据）的异质性因果效应设定下，目标是识别出受不同药物-基因关联影响的多个非线性亚群。作者提出 change surface regression 模型，将亚群划分边界参数化为非线性曲面，突破了传统 change point 模型仅能处理线性或单变量分割的限制。高维协变量通过 doubly penalized approach（同时惩罚亚群边界参数与回归系数）实现变量选择与可解释性。估计采用两阶段迭代算法：第一阶段用 change point detection 粗定位，第二阶段用 smoothed local adaptive majorize-minimization (SLAMM) 做曲面回归精修。实证在 IWPC 数据中识别出 3 个具有不同药代动力学关系的亚群，揭示了剂量需求的异质性。对您可能有用：该文提供了一套在流行病学队列中处理效应异质性与非线性亚群识别的应用范式。
- **关键技术**: `change surface regression`, `nonlinear subgroup identification`, `doubly penalized approach`, `smoothed local adaptive majorize-minimization (SLAMM)`, `two-stage iterative estimation`, `pharmacogenomic heterogeneity`
- **为什么对您有用**: (1) 本文连接到流行病学因果推断中的效应异质性（heterogeneous treatment effect）与亚群识别问题，属于 secondary interest 的应用因果工作。(2) 武器库中 M-estimation theory 与 semiparametric theory 可用于审视其两阶段 SLAMM 算法的收敛性与 change surface 估计的渐近性质——原文似乎缺乏严格的理论保证（如 n^{-1/2}-CAN 或 oracle property），这是一个具体口子。(3) **中期可做**：若想从理论角度切入，需先在 moderately_familiar 的 M-estimation theory 上长肌肉，为两阶段 penalized change surface 估计量建立严格的渐近理论；若仅关注应用范式与数据集，则属于立即可读的 gateway reading。

### 2. [10.1093/biomtc/ujaf025](https://doi.org/10.1093/biomtc/ujaf025) — A model-free framework for evaluating the reliability of a new device with multiple imperfect reference standards
- **作者**: Ying Cui, Qi Yu, Amita Manatunga, Jeong Hoon Jang
- **期刊/来源**: Biometrics
- **机构**: Emory University · The University of Texas Medical Branch at Galveston
- **分类**: vol 81 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在没有金标准的多源诊断评估中，提出一种无需模型假设、仅依赖内部一致性的无监督归纳框架，用于评估新设备的可靠性。该方法通过递归迭代为多个不完美参考标准分配权重，权重反映各标准之间的一致性程度，与多数意见一致的参照获得更高权重。不需要任何外部数据或建模假设（如 latent class 模型），只需指定适当的agreement index（如加权kappa）即可同时完成权重分配和最终的一致性评估。框架的数学基础基于“多数一致性”直觉，每次迭代更新权重直至收敛，具有计算简单、可解释性强的优点。应用于肾梗阻计算机辅助诊断设备评估，展示其与多位核医学医师评级的比较结果。对您有用：该问题直接关联流行病学中诊断准确性研究的核心挑战——无金标准情景下的验证；其无监督权重估计与您的非参统计和逆问题工具（如多指标迭代加权）有潜在接口，适合作为流行病学应用领域的阅读材料。
- **关键技术**: `unsupervised weight assignment`, `multiple imperfect reference standards`, `recursive iterative procedure`, `agreement index`, `majority-consensus weighting`
- **为什么对您有用**: 本文处理流行病学中常见的无金标准诊断设备评估，属于您的二级兴趣（流行病学实际数据与分析）的具体案例。方法中的无模型归纳权重估计与您技术库中的inverse problems with random noise（递归权重更新可看作一种迭代求解）和非参数统计思想有结构相似性。作为流行病学应用文章，值得一读以了解该领域的数据结构和方法缺口；若要跟进，利用U-statistics的工具分析agreement index的分布性质是中期可做的方向（需在HOIF或更高阶U统计量的计算上再强化）。

### 3. [10.1093/biomtc/ujae166](https://doi.org/10.1093/biomtc/ujae166) — Distributed lag models for retrospective cohort data with application to a study of built environment and body weight
- **作者**: Jennifer F Bobb, Stephen J Mooney, Maricela Cruz, Anne Vernez Moudon, Adam Drewnowski, David Arterburn et al.
- **期刊/来源**: Biometrics
- **机构**: Kaiser Permanente Washington Health Research Institute · University of Washington
- **分类**: vol 81 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本研究针对回顾性队列数据中分布式滞后模型（DLM）的应用难题——各参与者的暴露历史长度不一致（常见于电子健康档案数据），提出全队列分析方法。标准做法是定义具有最小暴露历史的子队列，但会损失样本量并可能引入选择偏误。作者提出利用所有可用数据的全队列方法，通过多重插补补全暴露历史，从而同时估计最长可达滞后期的效应。模拟表明子队列方法因远端相关暴露混杂导致偏差，而全队列DLM可有效避免此类偏差并高效估计滞后效应及累积效应。将方法应用于居住密度（可步行性代理）与体重关联的12年回顾性队列，发现前1-2年有即时效应，且最远滞后期（12年）也有关联，提示早期或累积效应。对于从事流行病学因果推断的研究者，该方法可直接应用于纵向暴露-健康关系研究。
- **关键技术**: `Distributed lag models`, `Multiple imputation for exposure history`, `Retrospective cohort design`, `Confounding by correlated exposures`, `Cumulative effect estimation`
- **为什么对您有用**: 本文直接连接至流行病学应用因果推断中的纵向暴露效应识别问题。研究者非常熟悉的因果推断估计理论可用来评估文章识别假设（如暴露无遗漏混杂）的合理性，且多重插补与全队列设计为处理缺失暴露数据提供借鉴。该方向可立即可做：运用因果推断工具检验识别条件并扩展至更灵活的暴露响应模型。

### 4. [10.1093/biomtc/ujaf018](https://doi.org/10.1093/biomtc/ujaf018) — Jointly modeling means and variances for nonlinear mixed effects models with measurement errors and outliers
- **作者**: Qian Ye, Lang Wu, Viviane Dias Lima
- **期刊/来源**: Biometrics
- **机构**: University of British Columbia
- **分类**: vol 81 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在纵向数据分析中，针对个体内方差随时间变化且存在异常值的问题，提出联合建模均值和方差的非线性混合效应模型。方法采用计算高效的近似推断（如线性化或拉普拉斯近似），同时估计均值参数和方差参数，方差模型能够自动识别并降权异常值，实现稳健推断。模拟结果表明，所提方法相比仅建模均值的传统方法更有效，且对异常值具有稳健性。真实数据应用基于HIV病毒动力学研究，揭示了新的生物学发现。该工作展示了在复杂纵向设定中联合建模均值与方差的实用性，其思路可迁移至因果推断中的测量误差或异方差问题。
- **关键技术**: `nonlinear mixed effects model`, `joint mean-variance modeling`, `approximate likelihood inference`, `robust estimation against outliers`
- **为什么对您有用**: 本文直接连接secondary interest中的流行病学应用（HIV纵向数据），其联合方差建模策略可用于处理因果推断中的异方差或测量误差。研究者弹药库中的nonparametric statistics可帮助放松该方法的分布假设，但当前方法依赖参数近似推断，研究者需先熟悉混合效应模型的逼近理论——属于中期可做（需在semiparametric theory上长肌肉）。

### 5. [10.1093/biomtc/ujaf028](https://doi.org/10.1093/biomtc/ujaf028) — A mixed-effects Bayesian regression model for multivariate group testing data
- **作者**: Christopher S McMahan, Chase N Joyner, Joshua M Tebbs, Christopher R Bilder
- **期刊/来源**: Biometrics
- **机构**: Clemson University · University of South Carolina · University of Nebraska–Lincoln
- **分类**: vol 81 · issue 1
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文针对使用多重检测试剂的组群检测（group testing）数据，开发了一个混合效应贝叶斯回归模型。组群检测结合多重检测可提高大规模传染病筛查效率，但产生依赖性的多元二元结果（如多种疾病携带状态）。模型采用多元probit框架，通过潜变量捕获疾病状态间的相关性，并纳入随机效应以刻画人群亚组异质性。变量选择通过 spike-and-slab 先验实现，后验采样算法基于吉布斯采样，直接利用截断正态分布。数值实验及衣原体/淋病实测数据表明模型能有效估计疾病流行率和亚组风险因子。对您而言，这是一篇流行病学应用文章，展示了贝叶斯建模处理结构化检测数据的完整流程，但方法学新颖性有限，核心工具不在您的武器库中，暂不可用于直接迁移。
- **关键技术**: `multivariate probit model`, `Bayesian mixed-effects model`, `spike-and-slab priors`, `Gibbs sampling`, `group testing with multiplex assays`
- **为什么对您有用**: 本文属于流行病学应用，与您的次要兴趣（流行病学数据集、实际因果工作）对接，但无因果推断成分。方法层面未涉及您的任何技术武器，属于'暂不可做'——其核心机器为贝叶斯MCMC与潜变量模型，与您的非常熟悉武器（非参、U-统计、因果推断）无直接交集。可作为流行病学组检测数据处理的入门读物，但不需要花全文时间细读。

## 其他  *(other, 2 篇)*

### 1. [10.1093/biomtc/ujae156](https://doi.org/10.1093/biomtc/ujae156) · [arXiv](https://arxiv.org/abs/2401.07400) — Gaussian processes for time series with lead–lag effects with applications to biology data
- **作者**: Wancen Mu, Jiawen Chen, Eric S Davis, Kathleen Reed, Douglas Phanstiel, Michael I Love et al.
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对生物时间序列中的 lead-lag 效应（提前-滞后关系）估计问题，提出了基于高斯过程的灵活模型，能处理观测时间点非均匀间隔、效应瞬态及外部因素干扰等挑战。方法上，作者设计了专门的高斯过程核函数来刻画 lead-lag 结构，并同时输出不相似性分数，以支持多对时间序列的排序或聚类。作者给出了核函数有效性和参数可识别性的理论证明，确保模型在非参数设定下的统计保障。仿真和真实数据（动态染色质相互作用）展示了比现有方法更好的估计精度。虽然该工作不直接聚焦因果推断或高维统计，但其高斯过程核设计思路和可识别性论证对非参数时间序列建模有参考价值。
- **关键技术**: `Gaussian process`, `lead–lag kernel`, `irregular time series`, `kernel identifiability`, `pairwise dissimilarity measure`
- **为什么对您有用**: 本文的核心方法（高斯过程 + 可识别性证明）可作为非参数时间序列建模的案例学习，但与其主要兴趣（因果推断、高维统计、半参理论）交集较少。武器库中的'非参数统计'和'逆问题'可帮助理解其核函数构造和可识别性论证，但无直接可攻问题。因此仅作泛读，不进入深度阅读。

### 2. [10.1093/biomtc/ujaf009](https://doi.org/10.1093/biomtc/ujaf009) · [arXiv](https://arxiv.org/abs/2402.12548) — Composite likelihood inference for space-time point processes
- **作者**: Abdollah Jalilian, Francisco Cuevas-Pacheco, Ganggang Xu, Rasmus Waagepetersen
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文研究空间-时间点过程的复合似然推断，针对雨林树木的更新（新树）和死亡模式，建立了基于当前树木和空间协变量的条件强度回归模型（更新事件）和条件死亡概率模型。估计采用条件复合似然函数，仅利用条件一阶性质，避免了指定高阶依赖结构。在协方差矩阵估计中，仅需空间上的弱相关衰减假设，并通过条件中心化技巧避免对时间相关结构的假定，从而在固定时间跨度、扩大空间域的渐近框架下使用中心极限定理。模拟研究和雨林数据分析验证了方法的有效性。该方法论创新在于弱依赖假设下简化了空间-时间点过程的推断，但本质上属于经典复合似然框架的应用。
- **关键技术**: `Composite likelihood`, `Conditional intensity`, `Conditional centering of score functions`, `Fixed-timespan increasing-domain asymptotics`, `CLT for weakly dependent spatial data`, `Stochastic covariates from past point patterns`
- **为什么对您有用**: 本文的复合似然框架和弱依赖渐近理论属于您 moderately_familiar 的 M-estimation 范畴，其中的条件中心化技巧对纵向因果推断中的复合条件似然估计可能有参考价值；但核心问题（空间点过程）与您的主要兴趣（因果推断、高维、U统计）距离较远，作为应用型论文，中期可做：先完善 M-estimation 在空间相依数据下的渐近理论（moderately_familiar），再考虑是否将类似简化技术移植到您关注的纵向因果推断中。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

