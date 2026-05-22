# Biometrics — Vol 81  Issue 1  ·  2026-05-21

- 共 37 篇 · Biometrics

## 因果推断  *(causal_inference, 12 篇)*

### 1. [10.1093/biomtc/ujae165](https://doi.org/10.1093/biomtc/ujae165) — Penalized G-estimation for effect modifier selection in a structural nested mean model for repeated outcomes
- **作者**: Ajmery Jaman, Guanbo Wang, Ashkan Ertefaie, Michèle Bally, Renée Lévesque, Robert W Platt et al.
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 10/10 · novelty: `new_method`
- **摘要**: 在纵向/重复结局的 SNMM (structural nested mean model) 框架下，本文研究在存在时变混杂时，如何估计时变暴露的因果效应并数据自适应地选择未知的效应修饰变量。作者提出了一种双重稳健的惩罚 G-估计量，通过在 G-估计方程中引入惩罚项，实现了效应修饰变量的选择与因果参数估计的同步进行。理论上证明了该估计量具有 oracle 性质，即渐近下能以概率 1 正确识别零系数，且非零系数的估计量达到 n^{-1/2}-CAN 收敛速率。该方法填补了现有 MSM 或 ODT 变量选择方法仅适用于单次结局的空白，适用于重复测量场景下的时变混杂调整。模拟研究验证了其有限样本表现与双重稳健性，并在终末期肾病血液透析的流行病学队列中进行了实证分析。对您有用：直接推进了 longitudinal causal inference 中的估计与变量选择问题，其 oracle property 与 double robustness 的理论推导对您关注的 semiparametric efficiency 理论有直接借鉴意义。
- **关键技术**: `structural nested mean model`, `penalized G-estimation`, `double robustness`, `effect modifier selection`, `oracle property`, `time-varying confounding`
- **为什么对您有用**: 直接契合 longitudinal causal inference 的核心设定（时变混杂与 SNMM），其惩罚 G-估计的 oracle property 与双重稳健性对您关注的 semiparametric efficiency 理论有直接参考价值，同时提供了流行病学纵向数据的真实应用范式。

### 2. [10.1093/biomtc/ujaf010](https://doi.org/10.1093/biomtc/ujaf010) — Instrumental variable estimation of complier casual treatment effects with interval-censored competing risks data
- **作者**: Yichen Lou, Yuqing Ma, Jianguo Sun, Peijie Wang, Zhisheng Ye
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文研究在同时存在区间删失与竞争风险的情形下，利用工具变量估计 complier 因果处理效应的问题，目标参数为累积发生函数（CIF）变换模型下的回归系数。方法上，在 CIF 变换模型类（包含 Fine-Gray 子分布比例风险/比例优势模型作为特例）下提出 IV 估计，以处理内生处理选择偏倚。所得回归参数估计量被证明具有相合性与渐近正态性，但文中未讨论是否达到半参数有效界。模拟研究表明有限样本表现良好，并应用于乳腺癌筛查流行病学数据。对您而言，该文将 IV 因果推断推广至区间删失竞争风险这一复杂删失结构，在纵向/生存因果推断的 IV 设定下具有方法可迁移价值，同时提供了流行病学真实数据集参考。
- **关键技术**: `instrumental variable estimation`, `cumulative incidence function transformation model`, `competing risks`, `interval censoring`, `Fine-Gray model`, `complier causal effect`
- **为什么对您有用**: 直接关联您 primary interest 中的 IV 因果推断，将 IV 推广至区间删失竞争风险设定，方法可迁移至纵向/生存因果推断场景；同时提供流行病学真实数据集（乳腺癌筛查），对 secondary interest 中的流行病学应用有参考价值。

### 3. [10.1093/biomtc/ujaf016](https://doi.org/10.1093/biomtc/ujaf016) — The subtype-free average causal effect for heterogeneous disease etiology
- **作者**: A Sasson, M Wang, S Ogino, D Nevo
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在疾病异质性设定下（如结直肠癌不同微卫星不稳定MSI亚型），针对暴露对不同亚型效应差异的因果识别问题，本文基于主分层（principal stratification）框架提出了新 estimand：Subtype-Free Average Causal Effect (SF-ACE)。SF-ACE 定义为在任意暴露水平下均不会患其他亚型疾病的人群中的平均因果效应。文章研究了该 estimand 的非参数识别，探讨了比标准设定更精细的 monotonicity 假设。由于主分层效应的识别假设通常不可检验且过强，作者开发了放松假设的敏感性分析方法。估计方面，提出了三种估计量，包括一个双重稳健（doubly robust）估计量。实证分析应用于两个大型流行病学队列，研究吸烟对结直肠癌MSI亚型的异质性因果效应。对您有用：本文将主分层与敏感性分析结合处理异质性病因的思路，可直接迁移至您关注的因果推断（主分层/敏感性分析）及流行病学应用中。
- **关键技术**: `principal stratification`, `non-parametric identification`, `monotonicity assumptions`, `sensitivity analysis`, `doubly robust estimation`
- **为什么对您有用**: 直接涉及您 primary interest 中的因果推断（主分层识别、敏感性分析、DR估计）以及 secondary interest 中的流行病学（大型队列数据应用），提供了处理异质性结局的因果识别新视角及配套的敏感性分析框架。

### 4. [10.1093/biomtc/ujae163](https://doi.org/10.1093/biomtc/ujae163) — Causal inference with cross-temporal design
- **作者**: Yi Cao, Pedro L Gozalo, Roee Gutman
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在观察性鼓励设计下，当鼓励无法随机化时，目标是估计干预的因果效应，但时间趋势会与干预效应相混淆。本文提出跨时间设计，用时间模拟随机鼓励实验，并用时间假设（如共同趋势）替代传统的排他性限制来实现因果识别。估计方面，作者开发了贝叶斯程序进行效应估计，模拟显示其在估计精度上优于工具变量（IV）和匹配方法，且对共同趋势假设的违反具有一定稳健性。实证分析了2011-2017年Medicare Advantage扩张对专业护理机构居民30天再入院风险的影响。该文用时间假设替代排他性限制的识别策略，为您在纵向因果推断或IV假设放松方面的研究提供了新的识别思路，同时Medicare数据集对流行病学应用有参考价值。
- **关键技术**: `cross-temporal design`, `encouragement design`, `exclusion restriction replacement`, `temporal assumptions`, `Bayesian causal inference`, `instrumental variables`
- **为什么对您有用**: 提出了用时间假设替代排他性限制的因果识别策略，对您在纵向因果推断和IV假设放松方面的研究有启发；同时提供了Medicare流行病学真实数据集的应用范例。

### 5. [10.1093/biomtc/ujaf013](https://doi.org/10.1093/biomtc/ujaf013) — Addressing selection bias in cluster randomized experiments via weighting
- **作者**: Georgia Papadogeorgou, Bo Liu, Fan Li, Fan Li
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在整群随机化实验中，个体常在干预分配后招募，导致招募样本与总体存在系统性差异而引发选择偏差；本文在可忽略招募假设下定义了总体和招募人群的因果 estimand。证明招募人群的 ATE 可通过逆概率加权（IPW）一致估计，而总体 ATE 通常不可识别。借助主分层（principal stratification）框架，识别出总体中两个有意义子群（始终招募者与仅干预下招募者）的因果效应。提出了相应的估计策略与针对可忽略招募假设的敏感性分析方法，并配套开源 R 包 CRTrecruit。该文对您有用，因为其在主分层框架下处理随机化后选择偏差的 identification 逻辑与敏感性分析思路，可直接迁移至您关注的因果推断识别与敏感性分析子方向。
- **关键技术**: `inverse probability weighting`, `principal stratification`, `sensitivity analysis`, `ignorable recruitment assumption`, `cluster randomized experiments`
- **为什么对您有用**: 直接关联您 primary interest 中的因果推断（identification 与 sensitivity analysis），展示了在主分层框架下如何处理随机化后选择偏差的不可识别问题及敏感性分析，方法可迁移至流行病学整群实验设计。

### 6. [10.1093/biomtc/ujaf019](https://doi.org/10.1093/biomtc/ujaf019) — Individualized multi-treatment response curves estimation using RBF-net with shared neurons
- **作者**: Peter Chang, Arkaprava Roy
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在多处理（multi-treatment）设定下，本文研究基于协变量的异质性处理效应（HTE）与个体化响应曲线的非参数估计问题。提出一种基于共享隐层神经元的径向基函数网络（RBF-net）来建模不同处理结果之间的共性；在贝叶斯框架下，利用阈值化最佳线性投影（thresholded best linear projections）发展估计与推断方案，并通过 MCMC 算法实现，全面量化不确定性。模拟与 MIMIC 脓毒症数据应用表明，该方法能有效估计多处理响应曲线并揭示不同治疗策略对 ICU 住院时长和 SOFA 评分的差异化影响。对您有用：该文将非参数建模与贝叶斯推断结合用于多处理 CATE 估计，其共享结构设计对处理多离散干预的因果推断问题有参考价值，且 MIMIC 数据分析对流行病学应用有直接借鉴意义。
- **关键技术**: `heterogeneous treatment effect`, `multi-treatment setting`, `radial basis function network`, `Bayesian nonparametrics`, `Markov chain Monte Carlo`, `thresholded best linear projection`
- **为什么对您有用**: 涉及因果推断中的多处理异质性效应（CATE）估计，采用非参数贝叶斯方法，且包含 MIMIC 临床数据集的流行病学应用，对您在因果推断（多处理设定）和流行病学应用方向的兴趣有直接参考价值。

### 7. [10.1093/biomtc/ujaf026](https://doi.org/10.1093/biomtc/ujaf026) — Optimal treatment regime estimation in practice: challenges and choices in a randomized clinical trial for depression
- **作者**: Florian Stijven, Trung Dung Tran, Ellen Driessen, Ariel Alonso Abad, Geert Molenberghs, Geert Verbeke et al.
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文在随机临床试验（心境恶劣障碍）数据上估计最优处理方案（optimal treatment regime, OTR），目标 estimand 为最大化期望收益的决策规则，假设为随机化试验设定。方法上采用 Q-learning 与 value search estimation 两种经典 OTR 估计方法，缺失数据通过多重插补处理；文章重点不在新估计量或新理论，而在于详细记录实际分析中面临的选择与挑战（如多重插补与 value search 的具体实现细节）。理论贡献有限，未涉及效率界、influence function 或收敛率的新结果；主要价值在于作为 OTR 实践操作的指南性案例。对您而言，若关注 causal inference 中个体化处理决策的落地实现流程与缺失数据处理策略，可作参考，但理论深度不足以推进您在效率理论或半参数推断方面的研究。
- **关键技术**: `Q-learning`, `value search estimation`, `optimal treatment regime`, `multiple imputation`, `randomized clinical trial`
- **为什么对您有用**: 与您 primary interest 中的 causal inference（处理方案估计）有方法论关联，但本文是应用导向的实践指南，无新理论或 sharper rate；对流行病学 RCT 数据分析流程有参考价值，但理论收益有限。

### 8. [10.1093/biomtc/ujaf033](https://doi.org/10.1093/biomtc/ujaf033) — Regression to the mean for bivariate distributions
- **作者**: Manzoor Khan, Jake Olivier
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 4/10 · novelty: `weaker_assumption`
- **摘要**: 在 pre-post 研究设计中，基于基线截断筛选受试者时，条件均数差异是回归均值（RTM）与处理效应的叠加；本文旨在任意双变量分布下识别 RTM。相较于以往仅限于双变量正态、泊松或二项分布的强假设方法，本文在更弱的假设下推导了 RTM 的一般表达式。针对指数族分布，作者推导了最大似然估计（MLE），并严格证明了其无偏性、一致性与渐近正态性。实证部分利用男性胆固醇与患者舒张压数据，成功将条件均数差异分解为 RTM 与处理效应。对您有用：为 pre-post 因果推断中 RTM 与处理效应的识别提供了更一般的数学统计框架，且流行病学数据集可直接借鉴。
- **关键技术**: `regression to the mean`, `bivariate distribution`, `maximum likelihood estimation`, `exponential family`, `pre-post design`, `treatment effect decomposition`
- **为什么对您有用**: 涉及因果推断中 pre-post 设计的 identification 问题（RTM 与处理效应分离），并在指数族下给出了 MLE 的渐近理论；同时提供了流行病学应用数据集。

### 9. [10.1093/biomtc/ujae161](https://doi.org/10.1093/biomtc/ujae161) — Weighted Q-learning for optimal dynamic treatment regimes with nonignorable missing covariates
- **作者**: Jian Sun, Bo Fu, Li Su
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在纵向动态治疗策略（DTR）的 Q-learning 框架下，目标是估计最优 DTR，但电子病历中非随机缺失的协变量会导致反向归纳中前序阶段的伪结果也呈现非随机缺失。为解决此缺失数据问题，提出加权 Q-learning 方法，通过逆概率加权（IPW）修正伪结果的缺失机制。权重的获取依赖于引入无应答工具变量的估计方程或进行敏感性分析。推导了加权 Q-learning 估计量的渐近性质，仿真和基于 MIMIC-III 脓毒症数据的实证分析验证了方法的有效性。对您有用：该文将 IV 和敏感性分析整合进纵向 DTR 的缺失数据处理，直接契合您对因果推断（纵向、IV、敏感性分析）及流行病学应用的关注。
- **关键技术**: `Q-learning`, `dynamic treatment regimes`, `inverse probability weighting`, `nonresponse instrumental variable`, `sensitivity analysis`, `pseudo-outcome`
- **为什么对您有用**: 直接契合您对因果推断（纵向 DTR、IV、敏感性分析）及流行病学应用的关注；MIMIC-III 数据集的分析流程对临床因果推断有迁移价值。

### 10. [10.1093/biomtc/ujaf024](https://doi.org/10.1093/biomtc/ujaf024) — Bayesian nonparametric trees for principal causal effects
- **作者**: Chanmin Kim, Corwin Zigler
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在 principal stratification 框架下，当中间变量为连续型时基本 principal strata 数量无穷，principal causal effects 的 identification 与 estimation 面临维数挑战。本文提出基于 Bayesian Causal Forests (BCF) 的非参数方法，同时建立两个 BART 模型：一个灵活建模 principal stratum membership，另一个建模给定 strata 下结局的条件期望。BCF 捕捉处理效应异质性的能力使其适合刻画连续型 principal strata 表面上的效应变化曲面，同时通过 targeted selection 机制与正则化缓解混淆偏倚。模拟研究展示了有限样本表现，实证分析研究了电厂排放控制技术对颗粒物污染的因果效应如何随其对 SO₂ 排放的影响而变化。对您有用：该工作将 BCF 引入连续型 principal stratification，为中间变量/mediation 设定下的效应异质性分析提供了可迁移的非参数工具，直接关联您关注的 causal inference (mediation, intermediate variable) 与 nonparametric theory 交叉方向。
- **关键技术**: `Bayesian Causal Forests`, `Bayesian Additive Regression Trees`, `principal stratification`, `treatment effect heterogeneity`, `targeted selection`, `Bayesian nonparametric`
- **为什么对您有用**: 直接关联您 primary interest 中的 causal inference (principal stratification 与 mediation/intermediate variable 设定) 及 nonparametric theory；BCF-BART 组合为连续型 strata 下的效应异质性提供了可迁移的非参数框架，实证部分也涉及流行病学/环境健康数据集。

### 11. [10.1093/biomtc/ujaf015](https://doi.org/10.1093/biomtc/ujaf015) — Multiply robust difference-in-differences estimation of causal effect curves for continuous exposures
- **作者**: Gary Hettinger, Youjin Lee, Nandita Mitra
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在连续暴露的倍差法（DiD）框架下，本文目标是估计因果效应曲线，同时处理干预状态、暴露水平和结果趋势的多重混杂。提出了一种多重稳健估计量，允许干预、暴露和结果模型中的部分误设，且不对效应曲线施加参数假设。方法核心基于半参数理论构建，利用影响函数实现多重稳健性，避免了连续暴露下传统参数模型的限制。理论上证明了估计量的统计性质，模拟和营养消费税的流行病学应用验证了方法的有效性。对您有用：直接推进了您在因果推断（DiD与连续处理）和半参数效率理论（多重稳健与影响函数）方面的兴趣，且应用部分契合流行病学因果分析。
- **关键技术**: `difference-in-differences`, `continuous exposure`, `multiply robust estimation`, `causal dose-response curve`, `influence function`
- **为什么对您有用**: 直接推进了您在因果推断（DiD与连续处理变量）和半参数效率理论（多重稳健估计与影响函数）方面的核心兴趣，同时流行病学应用（营养税）契合您的次要兴趣。

### 12. [10.1093/biomtc/ujaf008](https://doi.org/10.1093/biomtc/ujaf008) — Combining experimental and observational data through a power likelihood
- **作者**: Xi Lin, Jens Magelund Tarp, Robin J Evans
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在 RCT 与观察性数据融合的设定下，目标是利用大规模但有隐藏混杂偏差的观察性数据来提升 ATE 估计的效率。作者提出 power likelihood 方法，将观察性数据的似然提升至一个小于 1 的幂次（learning rate），以控制混杂偏差对融合估计的影响。核心机制是通过最大化 expected log predictive density (ELPD) 的数据自适应程序选取最优 learning rate，在偏差-方差权衡下调节观察性信息的贡献。理论上，该方法在观察性数据与 RCT 同分布时退化为全似然融合，在存在混杂时通过降权保持近似名义覆盖率。模拟显示 power 提升同时覆盖率近似保持，实证分析将 PIONEER 6 临床试验与 US health claims 数据融合验证了方法有效性。对您有用：power likelihood 提供了一种不同于 orthogonal score / debiased ML 的偏差-效率权衡视角来融合异质数据源，与您在 causal inference 的数据融合及 efficiency theory 中的兴趣直接相关。
- **关键技术**: `power likelihood`, `data fusion`, `expected log predictive density (ELPD)`, `bias-variance tradeoff`, `treatment effect estimation`, `RCT-observational data integration`
- **为什么对您有用**: 直接关联 causal inference 中 RCT 与观察性数据融合的估计问题；power likelihood 作为调节偏差-效率的工具，为 efficiency theory 提供了不同于 debiased ML / orthogonal score 的正则化视角，方法可迁移到您关注的 proximal CI 或 IV 设定下的多源数据融合。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1093/biomtc/ujaf017](https://doi.org/10.1093/biomtc/ujaf017) — Positive-definite regularized estimation for high-dimensional covariance on scalar regression
- **作者**: Jie He, Yumou Qiu, Xiao-Hua Zhou
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究高维协方差矩阵对标量协变量的回归估计问题，目标是在给定协变量下对条件平均协方差矩阵的回归系数进行稀疏正则化估计，同时保证正定性约束。核心挑战在于协方差回归参数空间巨大且正定性对回归系数施加了非平凡约束；作者给出了条件协方差矩阵正定的充要条件，并在此基础上构建带约束的 L1 正则化优化问题，使估计量同时满足稀疏性与正定性。计算上提出 ADMM 算法求解该约束正则化问题，并证明算法收敛性；理论上推导了回归系数与异质协方差估计量的收敛速率。模拟与脑连接组数据实证验证了方法表现。对您有用：该工作将高维协方差回归的正定性约束从充分条件推进到充要条件，且 ADMM 求解方案可直接迁移到您在统计计算方向中遇到的类似约束优化问题。
- **关键技术**: `covariance regression`, `positive-definite constraints`, `ADMM algorithm`, `L1 regularization`, `convergence rate analysis`, `heterogeneous covariance modeling`
- **为什么对您有用**: 直接关联您的高维统计与统计计算兴趣：正定性充要条件下的约束正则化估计及 ADMM 求解，为高维协方差结构建模提供了更紧的理论框架和可迁移的算法方案。

## 非参数 / 半参数  *(nonparam_semipara, 7 篇)*

### 1. [10.1093/biomtc/ujaf022](https://doi.org/10.1093/biomtc/ujaf022) — Statistical inference on change points in generalized semiparametric segmented models
- **作者**: Guangyu Yang, Baqun Zhang, Min Zhang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 9/10 · novelty: `new_theory`
- **摘要**: 本文在广义结果变量的分段模型中研究变点的存在性检验与位置估计，构建了综合半参数框架。变点估计基于半光滑估计方程，假设检验则提出平均得分型检验统计量。理论上严格证明了所有参数估计量的 n^{-1/2} 相合性、渐近正态性与渐近有效性，并推导了零假设下检验统计量的渐近分布。模拟与 Blue Cross Blue Shield 医学理赔数据应用表明，该方法能成功识别具有临床意义的显著变点效应。对您有用：该文将半参数效率理论与变点假设检验结合，处理非正则参数推断，对您在半参数效率界和假设检验方面的研究有直接参考价值；其医学数据应用也契合流行病学方向。
- **关键技术**: `semismooth estimating equation`, `average score-type test`, `semiparametric efficiency`, `change-point estimation`, `asymptotic normality`
- **为什么对您有用**: 论文严格推导了半参数分段模型下参数的渐近有效性，并提出了平均得分型检验，直接契合您在半参数效率理论与假设检验方面的核心兴趣；医学理赔数据的应用也符合流行病学次级兴趣。

### 2. [10.1093/biomtc/ujae164](https://doi.org/10.1093/biomtc/ujae164) — High-dimensional partially linear functional Cox models
- **作者**: Xin Chen, Hua Liu, Jiaqi Men, Jinhong You
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在高维部分线性泛函 Cox 模型设定下，目标是估计功能预测变量对风险率的非线性效应，同时处理随样本量发散的标量预测变量和功能主成分（FPC）。方法上，采用 group SCAD 进行标量预测变量和 FPC 的变量选择，并利用 B-splines 对非线性效应进行平滑估计。理论部分证明了估计量在发散维度下的收敛性质，模拟和肾移植数据实证验证了方法的有效性。对您有用：该文将高维惩罚回归与半参数部分线性结构结合，其 group SCAD 与 B-spline 的理论处理对您在半参数理论及高维统计方面的研究有参考价值，且肾移植数据集可作流行病学应用素材。
- **关键技术**: `partially linear functional Cox model`, `group SCAD`, `B-spline estimation`, `functional principal components`, `diverging dimensions`
- **为什么对您有用**: 结合了高维变量选择与半参数部分线性模型，group SCAD 与 B-spline 的理论分析对您在半参数理论方面的研究有直接参考价值；肾移植数据集也可作为流行病学应用案例。

### 3. [10.1093/biomtc/ujaf007](https://doi.org/10.1093/biomtc/ujaf007) — Feature screening for metric space-valued responses based on Fréchet regression with its applications
- **作者**: Bing Tian, Jian Kang, Wei Zhong
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在超高维预测变量与度量空间值响应（如分布数据、矩阵数据）的设定下，本文目标是基于全局 Fréchet 回归实现确定性特征筛选。提出 Fréchet-SIS 方法，利用仅需数据对象间距离的边际广义残差平方和作为边际效用指标，评估预测变量重要性。理论上在温和正则条件下证明了该筛选程序具有 sure screening property（确定性筛选性质）。模拟与实证表明其有限样本表现良好，并在阿尔茨海默病影像遗传学（582,591个SNPs筛选）与经济学案例中识别出关键变量。对您有用：将高维筛选理论拓展至非欧度量空间，且其实证数据集（流行病学队列与经济学）直接契合您的次级兴趣，提供了非标准结构数据下的高维筛选范式。
- **关键技术**: `sure independence screening`, `Frechet regression`, `metric space-valued data`, `marginal general residual sum of squares`, `sure screening property`
- **为什么对您有用**: 将高维筛选理论拓展至非欧度量空间，且其实证数据集（流行病学队列与经济学）直接契合您的次级兴趣，提供了非标准结构数据下的高维筛选范式。

### 4. [10.1093/biomtc/ujae156](https://doi.org/10.1093/biomtc/ujae156) — Gaussian processes for time series with lead–lag effects with applications to biology data
- **作者**: Wancen Mu, Jiawen Chen, Eric S Davis, Kathleen Reed, Douglas Phanstiel, Michael I Love et al.
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究非均匀间隔时间序列中的 lead-lag（领先-滞后）效应，目标是在外部因素干扰下估计瞬态时滞并量化序列间相似性。作者提出基于高斯过程（GP）的模型，通过构造新协方差核函数灵活处理非均匀采样与瞬态 lead-lag。该方法输出时滞估计与相异性得分（dissimilarity scores），支持多时间序列基于 lead-lag 强度的排序与聚类。理论上，证明了所提核函数的有效性及核参数的可识别性（identifiability）。模拟与动态染色质交互的真实数据表明该方法优于现有方法。对您而言，该文在非参数理论（核参数可识别性）和纵向数据分析（非均匀时间点 lead-lag 估计）方面有参考价值，其相异性度量思路或可迁移至纵向因果推断中的时间依赖性建模。
- **关键技术**: `Gaussian process`, `kernel identifiability`, `lead-lag effect`, `irregular time series`, `dissimilarity score`
- **为什么对您有用**: 涉及非参数理论（GP 核参数可识别性证明）与纵向数据（非均匀时间序列）的 lead-lag 估计，其相异性度量思路对纵向因果推断中的时间依赖性建模有参考价值。

### 5. [10.1093/biomtc/ujae168](https://doi.org/10.1093/biomtc/ujae168) — Improving estimation efficiency for survival data analysis by integrating a coarsened time-to-event outcome from an external study
- **作者**: Daxuan Deng, Lijun Zhang, Hao Feng, Vernon M Chinchilli, Chixiang Chen, Ming Wang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在数据整合框架下，研究如何将主研究的连续 time-to-event 结局与外部研究的粗化（区间删失）结局及部分协变量结合，以提高生存分析回归参数的估计效率。核心方法是对外部粗化结局与子集协变量设定 working model，通过经验似然构造信息权重，进而构建加权估计量。理论证明新估计量相比仅用主研究的传统估计量具有更高效率，且该效率增益对 working model 误设具有鲁棒性——即使模型误设，渐近方差也不会增大。模拟研究确认了有限样本下的效率提升与误设鲁棒性；实证分析整合 NACC 与 ADNI 阿尔茨海默病队列数据。对您有用：经验似然加权整合粗化外部数据的效率提升机制，直接关联您关注的半参数效率理论与流行病学队列数据应用场景。
- **关键技术**: `empirical likelihood weighting`, `coarsened time-to-event data`, `working model misspecification robustness`, `data integration for survival analysis`, `asymptotic efficiency improvement`
- **为什么对您有用**: 经验似然加权构造与效率鲁棒性理论直接关联您 primary interest 中的半参数效率界研究；ADNI/NACC 阿尔茨海默病队列整合案例为流行病学 secondary interest 提供了可复用的数据整合分析范式。

### 6. [10.1093/biomtc/ujae169](https://doi.org/10.1093/biomtc/ujae169) — Change surface regression for nonlinear subgroup identification with application to warfarin pharmacogenomics data
- **作者**: Pan Liu, Yaguang Li, Jialiang Li
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在药理基因组学设定下，目标是识别药物-基因关联在不同亚群间的异质性，关键假设是亚群划分可由非遗传因素通过非线性 change surface 刻画。作者提出 change surface regression 模型，将传统 change point 推广为 change surface 以容纳非线性亚群边界，并通过 doubly penalized 方法同时实现变量选择与亚群识别以处理高维协变量。估计采用两阶段迭代算法：第一阶段做 change point 检测，第二阶段用 smoothed local adaptive majorize-minimization 算法拟合 surface regression。在 IWPC 华法林数据上识别出 3 个具有不同药理基因组学关系的亚群，提供了新的临床发现。该方法对您在 semiparametric theory 方面的兴趣有参考价值——change surface 作为半参数结构的估计理论（收敛率、惩罚一致性等）尚有深入空间，同时药理基因组学异质性分析与流行病学 secondary interest 中的因果异质性/亚群分析有直接交集。
- **关键技术**: `change surface model`, `doubly penalized regression`, `local adaptive majorize-minimization`, `change point detection`, `nonlinear subgroup identification`
- **为什么对您有用**: change surface 模型属于半参数回归框架，其估计理论（收敛率、oracle 性质）与您 semiparametric theory 兴趣相关；IWPC 药理基因组学数据集与流行病学 secondary interest 的因果异质性分析有交集，数据集本身有复用价值。

### 7. [10.1093/biomtc/ujaf006](https://doi.org/10.1093/biomtc/ujaf006) — Pseudo-observations for bivariate survival data
- **作者**: Yael Travis-Lumer, Micha Mandel, Rebecca A Betensky
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文将伪观测（pseudo-observations）方法从单变量右删失生存数据推广至双变量失效时间数据，目标是在右删失下对联合生存概率等参数进行回归估计。核心机制是先非参数估计联合生存函数（分别采用 Lin-Ying 1993 和 Dabrowska 1988 两个估计量），再基于其构造双变量伪观测作为广义线性模型的响应变量。对两种联合生存函数估计量，作者均证明了所得回归估计量具有一致性与渐近正态性，关键工具涉及 jackknife 伪观测与 influence function 的联系以及非参数泛函的渐近分析。方法可估计协变量对固定双变量时间点联合生存概率的效应，也可同时考虑多个时间点并估计条件生存概率。仿真与两个真实数据集（流行病学场景）验证了方法表现。对您而言，伪观测与 influence function 的理论联系直接关联 semiparametric efficiency 理论，且双变量删失设定在流行病学队列研究中有应用价值。
- **关键技术**: `pseudo-observations`, `bivariate survival function estimation`, `Dabrowska estimator`, `Lin-Ying estimator`, `jackknife influence function`, `asymptotic normality`
- **为什么对您有用**: 伪观测方法本质上与 one-step estimation / influence function 理论紧密相连，属于您关注的 semiparametric efficiency 理论范畴；双变量删失生存数据的回归设定在流行病学队列研究中有直接应用场景。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1093/biomtc/ujaf020](https://doi.org/10.1093/biomtc/ujaf020) — Combining covariate adjustment with group sequential, information-adaptive designs to improve randomized trial efficiency
- **作者**: Kelly Van Lancker, Joshua F Betz, Michael Rosenblum
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文在随机试验的组序贯设计（GSD）设定下，研究如何结合基线协变量调整以提升 ATE 估计精度并允许提前终止，核心 estimand 为处理效应，关键假设为估计量具有正则渐近线性（RAL）性质。针对调整估计量缺乏 GSD 标准停止边界所需的独立增量结构这一问题，作者对跨分析时间的调整估计量序列施加线性变换，构造出具有独立增量性质的相合渐近正态估计量序列，且精度不损失或提升。该结果将基于半参数有效估计量的经典 GSD 理论推广至任意 RAL 估计量。针对协变量预后价值不确定导致试验效力误判的实际问题，提出信息自适应设计，即持续招募直至达到预设信息水平而非固定样本量。理论上证明了变换后估计量的独立增量性与渐近正态性，实证显示该设计在不牺牲有效性及检验效力的前提下加速试验。对您有用：该文将半参数有效/RAL 估计量与序贯假设检验结合，直接连接了您的 efficiency theory 与 hypothesis testing 兴趣，且信息自适应设计对流行病学 RCT 有迁移价值。
- **关键技术**: `covariate adjustment`, `group sequential design`, `independent increments structure`, `regular asymptotically linear estimators`, `information-adaptive design`, `semiparametric efficient estimators`
- **为什么对您有用**: 直接连接您的 efficiency theory（RAL 估计量与半参数有效估计的线性变换）与 hypothesis testing（序贯检验的独立增量与停止边界），且方法可迁移至流行病学 RCT 的实际设计。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1093/biomtc/ujaf001](https://doi.org/10.1093/biomtc/ujaf001) — A unified combination framework for dependent tests with applications to microbiome association studies
- **作者**: Xiufan Yu, Linjun Zhang, Arun Srinivasan, Min-ge Xie, Lingzhou Xue
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文提出一个统一的 meta-analysis 框架，用于在一般设定下组合相依检验（dependent tests），并以微生物组关联研究为应用场景。核心方法基于经典 P 值聚合与更一般的置信分布（confidence distribution）组合，并将其推广至处理分量间存在相依性的情形。作者证明广泛使用的 vanilla Cauchy 组合方法是其框架的特例，且当 Cauchy 方法的分布假设被违反时，新框架提供了修正途径。数值结果表明忽略分量间相依性会导致严重的 size distortion，而所提框架能准确刻画相依结构、有效利用信息，构造出 size 准确且 power 提升的组合检验。对您而言，该文在相依检验组合这一假设检验子方向上提供了新的理论框架与 Cauchy 组合的推广，可直接服务于高维多重检验中相依结构处理的兴趣。
- **关键技术**: `confidence distribution combination`, `Cauchy combination test`, `dependent P-value aggregation`, `size control under dependence`, `microbiome association testing`
- **为什么对您有用**: 直接关联您在 mathematical statistics 中的假设检验兴趣：将相依检验组合从 Cauchy 方法推广到置信分布框架，对高维多重检验中处理相依结构有方法论迁移价值。

### 2. [10.1093/biomtc/ujaf011](https://doi.org/10.1093/biomtc/ujaf011) — A simple and powerful method for large-scale composite null hypothesis testing with applications in mediation analysis
- **作者**: Yaowu Liu
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在大规模中介分析背景下，本文研究复合零假设 H₀: αβ=0（即 α=0 或 β=0）的多重检验问题，目标是在 family-wise 或 FDR 控制下提升检验功效。经典 Sobel 检验与联合显著性检验（joint significance）因复合零假设的 union 结构而过于保守，导致严重功效损失。作者提出一种基于区域计数（region counting）的简单检验方法：仅需统计落入特定二维区域的检验统计量数目即可构造 p-value，无需估计复合零分布的精确形式。在弱假设下建立了非渐近（non-asymptotic）理论，证明该方法严格控制 type I error 且功效优于经典方法。模拟与 DNA 甲基化数据实证均验证了理论结论。对您有用：该工作处于 mediation 与 composite null hypothesis testing 的交叉点，直接对应您 causal inference (mediation) 和 hypothesis testing 两个 primary interest，其非渐近理论框架和无需分布估计的计数策略可迁移至其他复合零假设场景（如高维 IV 的弱识别检验）。
- **关键技术**: `composite null hypothesis testing`, `region counting method`, `non-asymptotic theory`, `large-scale multiple testing`, `mediation analysis`, `joint significance test`
- **为什么对您有用**: 直接推进中介分析中复合零假设 H₀: αβ=0 的检验理论，与您 causal inference (mediation) 和 hypothesis testing 两个 primary interest 交叉；非渐近理论框架和无需分布估计的计数策略可迁移至其他复合零假设场景。

## 统计计算 / 算法  *(stat_computing, 3 篇)*

### 1. [10.1093/biomtc/ujae159](https://doi.org/10.1093/biomtc/ujae159) — Distributed model building and recursive integration for big spatial data modeling
- **作者**: Emily C Hector, Brian J Reich, Ani Eloyan
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 针对神经影像等超高维似然空间数据建模的计算瓶颈，本文提出一种基于分布式模型构建与递归积分的高斯过程参数估计与推断框架。核心思想是从全局视角转向局部数据视角，对空间域进行递归划分；其主干是一个兼顾计算与统计效率的积分程序，通过递归方式同时融合空间分辨率内与分辨率间的依赖关系。该方法避免了直接对超大规模协方差矩阵求逆，属于分治-整合计算策略。理论上证明了该分布式估计的统计与计算性质，模拟与 ABIDE 自闭症脑影像数据应用验证了其可行性。对您有用：该文在超高维似然下的分布式计算与统计效率兼顾策略，直接契合您对统计计算（数值方法与算法）及效率理论的兴趣，其递归积分思想可迁移至其他高维/大数据场景。
- **关键技术**: `distributed model building`, `recursive integration`, `Gaussian process`, `ultra-high-dimensional likelihood`, `divide-and-conquer estimation`
- **为什么对您有用**: 直接契合您在统计计算（数值方法与算法）方向的兴趣，展示了如何在超高维似然下兼顾计算与统计效率；同时其自闭症脑影像的应用属于流行病学数据集，具有应用参考价值。

### 2. [10.1093/biomtc/ujaf027](https://doi.org/10.1093/biomtc/ujaf027) — Evaluating the effects of high-throughput structural neuroimaging predictors on whole-brain functional connectome outcomes via network-based matrix-on-vector regression
- **作者**: Tong Lu, Yuan Zhang, Vince Lyzinski, Chuan Bi, Peter Kochunov, Elliot Hong et al.
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文在矩阵（网络）-对-向量回归框架下，提出多层级子图提取方法（dense bipartite with nested unipartite graph），用于识别对功能连接子网络有强烈系统性影响的结构影像特征子集，同时在大规模数据中有效控制假阳性。目标 estimand 为结构影像特征（白质微结构完整性 WMMI、皮层厚度）对全脑功能连接组矩阵的效应。方法核心是将矩阵响应-向量预测的回归问题转化为二部图（SI 特征 ↔ FC 边）与嵌套单部图（FC 边间网络结构）的稠密子图检测，实现空间特异性变量选择与网络模式识别。在 UK Biobank n=4242 的多模态神经影像数据上应用，发现皮质脊髓束与小脑下脚的 WMMI 显著影响感觉运动、突显及执行子网络的功能连接（平均相关 0.81, p<0.001）。对您而言，该矩阵回归中的结构化子图提取算法与大规模多重比较假阳性控制策略，可迁移至高维统计计算中结构化矩阵推断的算法设计。
- **关键技术**: `matrix-on-vector regression`, `dense bipartite sub-graph extraction`, `nested unipartite graph`, `false positive control in large-scale testing`, `network regression`, `multimodal neuroimaging integration`
- **为什么对您有用**: 矩阵-对-向量回归中的结构化子图提取与大规模假阳性控制算法与您的统计计算兴趣（数值方法与算法）有方法交叉；但该文聚焦神经影像应用，缺乏 RMT 或效率理论层面的深度，主要收益在于算法设计思路的可迁移性。

### 3. [10.1093/biomtc/ujaf012](https://doi.org/10.1093/biomtc/ujaf012) — Potential outcome simulation for efficient head-to-head comparison of adaptive dose-finding designs
- **作者**: Michael Sweeting, Daniel Slade, Dan Jackson, Kristian Brock
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在自适应剂量寻找试验的模拟研究中，传统逐个设计独立模拟的方法计算量大且蒙特卡洛误差高，本文提出基于潜在结果的模拟框架以提升头对头比较效率。核心机制是预先模拟每个个体在所有剂量水平上的潜在结果，再将同一套完整数据集应用于不同竞争设计，本质上利用了公共随机数（common random numbers）实现方差缩减。案例研究表明，当比较的设计相似度较高时，新方法可将蒙特卡洛误差大幅降低，所需模拟规模可缩减至传统方法的约 1/48。该方法已在 R 包 escalation 中实现，对您在统计计算与模拟算法设计方面的兴趣有直接参考价值，其将因果推断潜在结果框架用于模拟方差缩减的思路也可借鉴。
- **关键技术**: `potential outcomes`, `Monte Carlo variance reduction`, `common random numbers`, `adaptive dose-finding`, `simulation efficiency`
- **为什么对您有用**: 将因果推断的潜在结果框架创造性地应用于统计计算中的蒙特卡洛模拟方差缩减，对您在统计计算与算法设计上的兴趣有直接的方法论借鉴意义。

## 流行病学  *(epidemiology, 7 篇)*

### 1. [10.1093/biomtc/ujae166](https://doi.org/10.1093/biomtc/ujae166) — Distributed lag models for retrospective cohort data with application to a study of built environment and body weight
- **作者**: Jennifer F Bobb, Stephen J Mooney, Maricela Cruz, Anne Vernez Moudon, Adam Drewnowski, David Arterburn et al.
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在回顾性队列研究中，分布式滞后模型（DLM）用于估计多时间滞后暴露的健康效应，但参与者暴露历史长度不一致导致估计困难。传统做法是限定具有最短暴露历史的子队列，但这会损失功效并可能因远端滞后相关暴露的混杂而引入选择偏差。本文提出全队列方法，利用多重插补（MI）补全缺失暴露历史，从而同时估计最长可识别滞后下的暴露效应。模拟表明子队列方法因远端滞后混杂产生偏差，而全队列 MI 方法可避免该偏差并高效估计滞后效应与累积效应。实证分析使用 EHR 数据研究 12 年居住密度与体重的关联，发现近 1-2 年的即时效应及 12 年前的远端关联。对您而言，该文展示了纵向暴露因果推断中因不完整暴露历史导致的选择偏差问题，虽方法学深度有限（MI 为标准工具），但其对远端滞后混杂的识别思路可迁移至纵向因果推断的敏感性分析考量。
- **关键技术**: `distributed lag models`, `multiple imputation for missing exposure history`, `retrospective cohort selection bias`, `confounding by correlated distant-lag exposures`, `critical window identification`
- **为什么对您有用**: 连接您 secondary interest 的流行病学应用（EHR 回顾性队列数据集）与 primary interest 的纵向因果推断（多滞后暴露的混杂与选择偏差），读它的收益在于理解不完整暴露历史下子队列选择如何引入混杂偏差，以及 MI 在该场景的实用策略。

### 2. [10.1093/biomtc/ujaf021](https://doi.org/10.1093/biomtc/ujaf021) — Sparse Bernoulli mixture modeling with negative-unlabeled data: an approach to identify and characterize long COVID
- **作者**: Tingyi Cao, Harrison T Reeder, Andrea S Foulkes
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在 negative-unlabeled (NU) 数据设定下（未感染者必为阴性，感染者标签未知），目标是识别 long COVID (PASC) 亚表型并筛选最小特征集。作者提出一种 Bernoulli 混合模型，通过新参数化适配 NU 数据结构，并引入 Bayesian 先验实现特征稀疏以提升解释性。估计采用 EM 算法，超参数（聚类数与稀疏度）通过 grid search 选取。模拟与 RECOVER-Adult 队列数据分析验证了该方法在 PASC 亚型划分中的有效性。对您而言，虽然该文核心是参数混合模型而非半参数/因果效率理论，但 NU 数据设定与流行病学潜变量识别问题相通，且 RECOVER 队列数据对 epi 应用方向有直接参考价值。
- **关键技术**: `negative-unlabeled learning`, `Bernoulli mixture model`, `sparse Bayesian prior`, `EM algorithm`, `feature selection`
- **为什么对您有用**: NU 数据设定与流行病学潜变量/部分识别问题相通，且 RECOVER 队列真实数据对您的流行病学应用方向有数据集参考价值。

### 3. [10.1093/biomtc/ujaf025](https://doi.org/10.1093/biomtc/ujaf025) — A model-free framework for evaluating the reliability of a new device with multiple imperfect reference standards
- **作者**: Ying Cui, Qi Yu, Amita Manatunga, Jeong Hoon Jang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在无金标准参考的临床诊断设定下，目标是评估新设备与多个异质性不完美参考标准之间的一致性。核心方法提出一种无模型加权聚合框架，通过无监督归纳程序递归分配权重：评估一致性高（形成多数意见）的参考标准获得更高权重，差异大者权重低。该方法无需对参考标准的异质准确度做参数假设或依赖外部数据，仅需指定一致性指数即可完成权重分配与设备评估。实证应用于肾梗阻CAD设备的诊断评级。对您而言，处理潜在真实结果不可观测（无金标准）下多代理变量的聚合思路，与proximal CI中利用多negative control识别因果效应的设定有概念相通之处，且该文提供了流行病学诊断评价的真实数据集。
- **关键技术**: `model-free weighting`, `unsupervised inductive procedure`, `agreement index`, `latent gold standard`, `diagnostic accuracy evaluation`
- **为什么对您有用**: 处理无金标准下多不完美代理的聚合问题，与proximal CI中利用多negative control的设定有概念上的相似性；同时提供了流行病学诊断评价的真实数据集和应用范式。

### 4. [10.1093/biomtc/ujaf028](https://doi.org/10.1093/biomtc/ujaf028) — A mixed-effects Bayesian regression model for multivariate group testing data
- **作者**: Christopher S McMahan, Chase N Joyner, Joshua M Tebbs, Christopher R Bilder
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 2/10 · novelty: `application`
- **摘要**: 在多重检测的混样测试数据下，本文目标是估计混合多变量 probit 模型，以刻画真实疾病状态间的相关性与群体异质性。方法上，构建了贝叶斯框架，引入 spike-and-slab 先验实现自动变量选择，并开发了相应的后验采样算法以适应复杂的混样数据结构。数值模拟与 Iowa 大学衣原体及淋病混样筛查数据验证了方法的有效性。对您而言，该文提供了流行病学混样筛查数据集及贝叶斯计算流程，但方法学核心（标准贝叶斯 probit 与 spike-and-slab）较为常规，理论创新有限。
- **关键技术**: `multivariate probit model`, `group testing (pooled testing)`, `spike-and-slab priors`, `Bayesian hierarchical model`, `multiplex assay`
- **为什么对您有用**: 属于流行病学应用，提供了混样筛查数据集和贝叶斯计算算法，但方法学（标准贝叶斯 probit 与 spike-and-slab）与您主攻的半参数/因果推断理论距离较远，主要价值在于数据结构认知。

### 5. [10.1093/biomtc/ujaf018](https://doi.org/10.1093/biomtc/ujaf018) — Jointly modeling means and variances for nonlinear mixed effects models with measurement errors and outliers
- **作者**: Qian Ye, Lang Wu, Viviane Dias Lima
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文在纵向数据分析框架下，针对具有测量误差和异常值的非线性混合效应模型（NLME），研究联合建模均值和个体内方差的问题。作者提出对均值使用NLME模型，同时对个体内方差建立参数模型以吸收异常值影响，并基于联合模型进行统计推断。推断采用计算高效的近似方法实现，避免了高维数值积分。理论与模拟表明，相较于忽略方差建模的传统方法，该联合估计方法能获得更有效的参数估计，并对异常值具有稳健性。实证分析基于HIV病毒动力学数据集，揭示了新的生物学发现。对您而言，该文展示了在纵向流行病学数据中通过方差建模提升估计效率的思路，可为纵向因果推断中处理异方差与异常值提供计算方法上的参考。
- **关键技术**: `nonlinear mixed effects model`, `joint mean-variance modeling`, `approximate likelihood inference`, `robust estimation`, `longitudinal data analysis`
- **为什么对您有用**: 论文属于流行病学纵向数据分析的应用，其联合建模均值与方差的计算高效近似方法，可为您在纵向因果推断（primary interest）中处理异方差和异常值提供计算与建模思路。

### 6. [10.1093/biomtc/ujae167](https://doi.org/10.1093/biomtc/ujae167) — Estimating hypothetical estimands with causal inference and missing data estimators in a diabetes trial case study
- **作者**: Camila Olarte Parra, Rhian M Daniel, David Wright, Jonathan W Bartlett
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文在 ICH E9 估计框架下，针对 2 型糖尿病临床试验，研究在“假设策略”（hypothetical strategy）下如何处理救援治疗和随机化治疗中止等间发事件以识别和估计因果 estimand。文章系统比较了五种估计方法：重复测量混合模型（MMRM）、多重插补（MI）、逆概率加权（IPTW）、G-formula 和 G-estimation，并详细阐述了各自的因果/缺失数据假设与 R 语言实现细节。实证结果显示各估计量在点估计和标准误上整体相似。然而，在计算时间、缺失数据处理、是否纳入间发事件后数据、时变混杂调整及不同间发事件类型建模方面，各方法存在显著的实际权衡。该文虽无新理论，但为纵向因果推断中的 G-formula、IPTW 及 G-estimation 提供了完整的真实数据应用范式，对您在流行病学试验数据中应用纵向因果推断方法具有直接的参考价值。
- **关键技术**: `hypothetical estimands`, `inverse probability of treatment weighting (IPTW)`, `G-formula`, `G-estimation`, `multiple imputation`, `intercurrent events`
- **为什么对您有用**: 对应您在流行病学方向的次级兴趣，提供了纵向因果推断（IPTW, G-formula, G-estimation）在真实糖尿病临床试验数据集上的完整应用流程与 R 代码，适合作为应用因果分析的参考范式。

### 7. [10.1093/biomtc/ujaf005](https://doi.org/10.1093/biomtc/ujaf005) — A regularized Bayesian Dirichlet-multinomial regression model for integrating single-cell-level omics and patient-level clinical study data
- **作者**: Yanghong Guo, Lei Yu, Lei Guo, Lin Xu, Qiwei Li
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文针对单细胞RNA测序计数数据与患者临床协变量的整合分析问题，在成分数据框架下提出正则化贝叶斯 Dirichlet-multinomial 回归模型。模型利用 Dirichlet-multinomial 分布刻画细胞类型丰度的过度离散特征，并引入层次树结构以在不同细胞分辨率下识别临床变量与细胞丰度的关联。贝叶斯正则化机制用于高维临床协变量的变量选择与收缩。在肺纤维化、COVID-19和非小细胞肺癌三个真实数据集上，模型揭示了特定细胞类型与临床变量的显著关联。对您而言，该文提供了流行病学领域的单细胞组学数据集及分析流程，但方法学属于参数化贝叶斯框架，与您关注的半参数效率或因果推断理论距离较远。
- **关键技术**: `Dirichlet-multinomial regression`, `Bayesian regularization`, `hierarchical tree structure`, `compositional data analysis`, `single-cell RNA-seq integration`
- **为什么对您有用**: 提供了流行病学/临床领域的单细胞组学数据集及整合分析流程，但方法学属于参数贝叶斯模型，与您主攻的半参数/效率/因果理论无直接交集，仅作数据集或应用场景参考。

## 其他  *(other, 4 篇)*

### 1. [10.1093/biomtc/ujaf009](https://doi.org/10.1093/biomtc/ujaf009) — Composite likelihood inference for space-time point processes
- **作者**: Abdollah Jalilian, Francisco Cuevas-Pacheco, Ganggang Xu, Rasmus Waagepetersen
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 2/10 · novelty: `weaker_assumption`
- **摘要**: 在时空点过程框架下，针对雨林动态（新生与死亡树木），基于当前状态与空间协变量建立条件强度与条件概率的回归模型，目标是回归参数的估计与推断。方法采用条件复合似然进行参数估计，仅依赖条件一阶性质；在构建协方差矩阵估计量时采用 assumption-lean 策略，仅需空间条件相关性衰减的温和假设，并通过复合似然得分函数的条件中心化避免了对时间相关性的假设。为应对短时间序列与大空间区域的特征，采用固定时间跨度-空间域递增（increasing spatial domain）的渐近框架推导中心极限定理，并处理了由过去点模式构造的随机协变量带来的挑战。理论上证明了空间域递增下的渐近正态性，仅需对时空过程的创新项施加弱依赖假设。对您可能有用：其 assumption-lean 协方差估计与利用条件中心化消除时间依赖的技巧，与半参数/鲁棒推断有方法论共通性，可为处理复杂依赖结构的推断提供参考。
- **关键技术**: `composite likelihood`, `assumption-lean covariance estimation`, `increasing domain asymptotics`, `conditional centering`, `space-time point process`
- **为什么对您有用**: 虽然属于空间统计，但其 assumption-lean 协方差估计与条件中心化处理时间相关性的技巧，与半参数理论中的鲁棒推断有方法论共通性，可为处理复杂依赖结构的推断问题提供参考。

### 2. [10.1093/biomtc/ujae160](https://doi.org/10.1093/biomtc/ujae160) — Robust Bayesian graphical regression models for assessing tumor heterogeneity in proteomic networks
- **作者**: Tsung-Hung Yao, Yang Ni, Anindya Bhadra, Jian Kang, Veerabhadran Baladandayuthapani
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 0/10
- **摘要**: {
  "topic": "nonparam_semipara",
  "summary_zh": "在协变量依赖的高维图模型设定下，目标是估计非正态数据的异质性精度矩阵（图结构），放松传统 GGM 的同质性与正态性假设。rBGR 框架通过随机边际变换（random marginal transformation）容纳非正态边际分布，通过图回归技术构建协变量依赖的精度矩阵以刻画异质性。提出"带协变量的条件符号独立性"（conditional sign independence with covariates）作为新的边缘依赖刻画，替代传统偏相关，并给出高效的后验采样算法。模拟显示在多种非正态程度下，rBGR 在边缘选择和协变量选择上均优于现有图回归模型。应用于肺癌与卵巢癌蛋白质组学网络，揭示与免疫细胞丰度差异关联的蛋白质-蛋白质交互作用。对您而言，随机边际变换的半参数思想与协变量依赖图结构的建模方式，可为高维图模型中非参数/半参数推断提供思路借鉴。",
  "key_techniques": [
    "random marginal transformation",
    "graphical regression",
    "conditional sign independence",
    "Bayesian posterior sampling",
    "co

### 3. [10.1093/biomtc/ujaf023](https://doi.org/10.1093/biomtc/ujaf023) — Bayesian scalar-on-network regression with applications to brain functional connectivity
- **作者**: Xiaomeng Ju, Hyung G Park, Thaddeus Tarpey
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究标量结果变量与脑功能连接（表示为对称正定 SPD 矩阵）之间的回归问题，设定在 SPD 矩阵的 Riemannian 流形切空间上进行建模。与直接向量化矩阵预测变量不同，该方法尊重 SPD 矩阵的 Riemannian 几何结构，利用切空间建模进行降维，并将低维表示与响应变量关联。降维矩阵通过在 Stiefel 流形上施加稀疏诱导先验以监督方式学习，防止过拟合并实现模型简约性。该方法在贝叶斯框架下量化所有参数的不确定性，并识别预测结果的关键脑区。模拟研究和 Human Connectome Project 数据的实证分析表明，该方法在预测 Picture Vocabulary 得分上表现良好。对您而言，虽然本文是贝叶斯流形回归，但其对结构化矩阵的切空间降维与 Stiefel 流形稀疏先验思路，可为高维统计中处理结构化协变量提供几何视角的参考。
- **关键技术**: `SPD matrix Riemannian geometry`, `tangent space dimension reduction`, `Stiefel manifold sparsity prior`, `Bayesian scalar-on-network regression`
- **为什么对您有用**: 本文主要属于生物统计与神经影像应用，与您核心的因果推断或半参数效率理论关联较弱；但其处理结构化矩阵数据的切空间降维与 Stiefel 流形稀疏先验技术，可为高维统计中协变量结构化建模提供几何视角的启发。

### 4. [10.1093/biomtc/ujaf014](https://doi.org/10.1093/biomtc/ujaf014) — A general, flexible, and harmonious framework to construct interpretable functions in regression analysis
- **作者**: Tianyu Zhan, Jian Kang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 0/10 · novelty: `minor`
- **摘要**: 在连续结局回归分析中，针对可解释性的主观性与多样性，本文提出基于用户先验期望定义“功能骨架”（functional skeleton）的通用框架来构建可解释函数。方法核心是提出基于 Mallows $C_p$ 统计量的新度量，用于在模型选择中平衡近似误差、泛化能力与可解释性。应用上，展示了自适应临床试验样本量计算、贝叶斯 Go/No-Go 决策以及推广至分类结局的 Fisher 精确检验。实证部分基于 NHANES 流行病学数据探讨实验室指标间关系。对您而言，该文虽涉及模型选择与假设检验，但理论深度偏向应用层面的可解释性定义，缺乏半参数效率或高维推断的严格理论，可快速略读其约束构建思路。
- **关键技术**: `Mallows Cp statistic`, `functional skeleton`, `model selection criterion`, `interpretable regression`
- **为什么对您有用**: 涉及回归模型选择与假设检验，并在 NHANES 流行病学数据上应用，但理论贡献偏向应用层面的可解释性定义，与您关注的半参数效率或高维理论距离较远，仅作扩展阅读。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

