# Scand. J. Stat. — Vol 52  Issue 4  ·  2026-06-19

- 共 27 篇 · Scandinavian Journal of Statistics
- 目录核对 ✅ 未见遗漏（对照 OpenAlex 26 篇，权威目录可能尚未完全收录本期）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期论文大致聚成四条主线：因果识别与推断（路径特定效应、异质性处理效应VIM、约束型因果发现）、半参数/非参数理论（分位数整合的DR估计、加性风险率平滑反投影、条件随机测度经验过程、PLS非渐近分析）、高维与随机矩阵（张量投影估计、极值尖峰协方差主成分个数）、以及假设检验与计算方法（MMD分布无关检验、多项小样本精确推断、Stein矩估计、子采样一步估计、PDMP耦合去偏）。此外，零散涉及测量误差推断、混合模型误选率控制、Hawkes过程谱推断及生存分析一致性指标等。

因果推断主线本期推进了缺失与删失下的非参数/半参数识别及效率问题。Nonparametric estimation... 引入影子变量解决非可忽略缺失下的中介路径特定效应识别，以sieve回归避免缺失机制参数建模；Variable importance measures... 在右删失生存数据下为CATE的变量重要性度量和部分线性投影构造了半参数有效影响函数及一步估计；A general framework... 则在约束型因果发现侧，抽象出property概念统一比较各类算法（如PC）的正确性条件，证明SMR是输出极小DAG算法的最弱条件。半参数/非参数主线侧重投影与稳健性：Combining probability... 结合非参数参与概率与半参数分位数回归构造DR估计器；Smooth backfitting... 将平滑反投影移植到加性风险率模型，赋予其L2最优投影解释及逐成分CAN性质；A Donsker... 为极值理论关联的条件随机测度建立GC与Donsker收敛及bootstrap有效性；A non-asymptotic analysis... 则给出单成分PLS及sPLS的有限样本预测误差非渐近上界。

高维/随机矩阵主线本期聚焦张量降维与极值尖峰结构：Projection‐based estimators... 通过随机投影平均将多变量估计闭式扩展至矩阵/张量，在投影数超线性增长下保持渐近正态；Estimation of the number... 将AIC/BIC推广至高维多元极值尖峰协方差，利用Marchenko-Pastur定律推导一致性条件。检验与计算主线推进了计算加速与检验便利性：Subsampled One‐Step... 利用一步更新将子采样估计收敛率提升至全样本N^{-1/2}；Debiasing piecewise... 通过连续时间耦合消除PDMP采样器的非渐近偏差；Asymptotic distribution‐free tests... 借特征核二阶矩构造MMD的渐近分布无关检验，免除重抽样；Improved small‐sample... 为多项分布不可微参数函数提供控制一类错误的精确推断；Stein's method... 基于Stein算子给出显式且可趋近MLE的矩估计框架。

与因果推断最贴的是路径特定效应、异质性处理效应VIM及约束型因果发现三篇；与半参数效率最贴的是生存CATE的VIM/投影、非概率样本DR估计及加性风险率平滑反投影；与高维最贴的是张量投影估计、极值尖峰协方差AIC/BIC及PLS非渐近分析，适合优先看。

## 因果推断  *(causal_inference, 3 篇)*

### 1. [10.1111/sjos.70002](https://doi.org/10.1111/sjos.70002) · [arXiv](https://arxiv.org/abs/2409.01248) — Nonparametric estimation of path‐specific effects in the presence of nonignorable missing covariates
- **作者**: Jiawei Shan, Ting Wang, Wei Li, Chunrong Ai
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1556-1593
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文针对存在非可忽略缺失协变量（nonignorable missing covariates）时，从处理到结果通过多个中介变量的路径特定效应（PSE）的估计问题。通过引入一个影子变量（shadow variable），证明PSE可识别为观测数据的泛函，且相关nuisance函数可通过序列优化问题唯一确定。提出基于sieve的回归插补估计量，完全避免对缺失机制进行参数建模。建立了估计量的大样本理论（一致性、渐近正态性），并给出推断方法。模拟实验和NHANES实际数据分析展示了方法的有限样本表现。该工作为因果推断中的中介分析提供了缺失数据下的非参数解决方案，尤其适合敏感变量缺失的场景。
- **关键技术**: `shadow variable`, `sieve regression imputation`, `sequential optimization`, `nonignorable missingness`, `path-specific effects`, `nonparametric identification`
- **为什么对您有用**: 本文直接对应您primary interest中的因果推断子方向——中介分析中的路径特定效应与非可忽略缺失协变量处理。您非常熟悉的非参数统计思想和因果推断估计理论可直接用于理解sieve回归和识别策略，且识别框架可迁移至其他复杂缺失数据场景。follow-up粗判：立即可做——您现有的nonparametric tools和estimation toolkit完全支撑您复现该方法或将其嵌入您自己的因果推断项目（如结合cross-fitting或双稳健扩展）。

### 2. [10.1111/sjos.70001](https://doi.org/10.1111/sjos.70001) · [arXiv](https://arxiv.org/abs/2412.11790) — Variable importance measures for heterogeneous treatment effects with survival outcome
- **作者**: Simon Christoffer Ziersen, Torben Martinussen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1505-1555
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在右删失生存数据设定下，本文研究异质性处理效应（HTE）的变量重要性度量（VIM）与部分线性投影估计。目标参数为基于生存函数与限制平均生存时间（RMST）两种 CATE 定义下的 TE-VIM 及最优部分线性投影系数，核心识别假设为无混杂与独立删失。基于半参数效率理论，作者为所有目标参数构造了 efficient influence function，并利用 one-step estimation / estimating equation 方法得到估计量；在 nuisance 参数满足收敛率条件（如 2-norm 达 n^{-1/4}）时，证明估计量具有渐近线性性与 n^{-1/2}-CAN 性质。模拟与两个真实数据集（流行病学/医学队列）验证了有限样本表现。对您可能有用：本文将半参数效率理论从连续/二元结局的 TE-VIM 延伸至生存设定，是因果推断-效率理论交叉方向的直接拓展。
- **关键技术**: `conditional average treatment effect (CATE)`, `semiparametric efficiency theory`, `efficient influence function`, `one-step estimation`, `restricted mean survival time (RMST)`, `variable importance measure (TE-VIM)`
- **为什么对您有用**: 本文直接连接因果推断（HTE/VIM）与效率理论（efficient influence function / one-step estimator）两个 primary interest 子方向，且真实数据应用属于流行病学队列范畴。用 very_familiar 的 semiparametric efficiency bound 推导与 moderately_familiar 的 identification theory 即可攻入本文的估计量构造与渐近线性性证明口子。follow-up 判断：**立即可做**——可尝试将 HOIF（moderately_familiar）引入此生存 TE-VIM 设定以构造更高阶的 debiased 估计量，或用 minimax bound 验证其声称的收敛率条件是否紧。

### 3. [10.1111/sjos.70023](https://doi.org/10.1111/sjos.70023) · [arXiv](https://arxiv.org/abs/2408.07575) — A general framework on conditions for constraint‐based causal learning
- **作者**: Kai Z. Teh, Kayvan Sadeghi, Terry Soo
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 2209-2241
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 在约束型因果发现设定下，本文研究各类算法（如 PC）返回正确因果图所需的 correctness condition（如 faithfulness）的必要性与强弱关系。作者引入 property 概念将任意约束型算法抽象化，构建统一框架以系统生成和比较不同算法的正确性条件。基于该框架，推导出 PC 算法的精确正确性条件，并将其与现有算法的条件建立联系；进一步证明，对于输出 ancestral graph 或满足任何极小性定义的 DAG 的算法，sparsest Markov representation (SMR) 是最弱的可能正确性条件。最后指出 Pearl-minimality 对有意义因果学习是必要的但不足以放松 faithfulness，必须结合背景知识等加以强化。对您有用：本文对因果发现 identification 条件的强弱排序提供了严格的理论刻画，直接补充了您在 causal inference identification theory 方向的体系化理解。
- **关键技术**: `constraint-based causal discovery`, `correctness conditions`, `graph property representation`, `sparsest Markov representation`, `Pearl-minimality`, `faithfulness`
- **为什么对您有用**: 本文直接连接 causal inference 的 identification theory 子方向，对 faithfulness、minimality、SMR 等图模型识别条件的强弱给出了严格的偏序比较与最弱条件刻画。您可以用 moderately_familiar 中的 identification theory 工具审视其 property 框架的抽象是否可迁移至 proximal CI 或 IV 设定下的 identification 条件分析。属于**中期可做**：需先在 identification theory 的图模型与极小性假设部分长肌肉，才能将此框架与您熟悉的 semiparametric identification 理论做深度交叉。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 2 篇)*

### 1. [10.1111/sjos.70021](https://doi.org/10.1111/sjos.70021) — Projection‐based estimators for matrix/tensor‐valued data
- **作者**: Joni Virta, Stanislav Nagy, Klaus Nordhausen
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Turku · Charles University · Statistics Finland · University of Helsinki · University of Jyväskylä
- **分类**: vol 52 · issue 4 · pp 2152-2186
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文提出了一种通用的投影基估计方法，用于将多变量估计量扩展到矩阵/张量数据。核心思想是：通过随机投影将张量的维度投影出去，对每个投影计算多变量估计量，然后取平均作为最终联合估计。在基本情况下，该估计量可得到闭式解，且某些特例与现有方法一致。作者推导了在弱假设下估计量相合性和渐近正态性的充分条件：只要投影数量以超线性速度随样本量增长，渐近正态性得到保持；而相合性对增长速率无要求。与竞争方法的比较表明，该扩展在分类问题中能有效提取成分，并产生充分的降维估计量。本文的方法对高维张量数据分析具有直接价值，尤其与您在张量数据方法方面的统计计算兴趣相契合。
- **关键技术**: `random projections`, `multivariate estimator averaging`, `sufficient dimension reduction`, `tensor data analysis`, `asymptotic normality`
- **为什么对您有用**: 本文直接关联到您的高维统计和统计计算兴趣（张量数据处理）。您可以使用非常熟悉的高维渐近理论来分析该投影平均估计量的统计效率，并与您熟悉的高阶U统计量（张量收缩视角）进行对比——这可能揭示投影基方法与einsum/树宽方法在计算-统计权衡上的异同。根据技术武器库，此方向属于立即可做：您现有的高维渐近和估计理论工具足以理解并延伸该方法的理论性质。

### 2. [10.1111/sjos.70026](https://doi.org/10.1111/sjos.70026) · [arXiv](https://arxiv.org/abs/2505.22437) — Estimation of the number of principal components in high‐dimensional multivariate extremes
- **作者**: Lucas Butsch, Vicky Fasen‐Hartmann
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 2270-2313
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 针对高维多元极值的角测度协方差矩阵，提出使用主成分分析进行降维的方法，并开发AIC和BIC准则来估计主成分个数（即尖峰特征值的个数）。在固定维数下证明了BIC弱一致而AIC不一致；在高维情景下，利用随机矩阵理论（Marchenko-Pastur定律、尖峰模型）推导了AIC和BIC一致性的充分条件，涵盖了维数随样本量增长的多种渐近框架。模拟研究和美国降水量数据应用验证了所提准则在有限样本下的表现。该工作将经典信息准则推广到极值分析的尖峰协方差结构设定中，为高维极值依赖结构的降维提供了可操作的理论工具。对您的高维统计与随机矩阵理论兴趣有直接连接，尤其是RMT工具为分析信息准则在spiked模型下的相变行为提供了精确刻画。
- **关键技术**: `spiked covariance model`, `random matrix theory`, `AIC/BIC consistency`, `angular measure`, `high-dimensional extremes`, `principal component analysis`
- **为什么对您有用**: 连接您的primary interest中'高维统计与随机矩阵理论'子方向——论文在极值尖峰协方差模型中利用RMT推导信息准则的一致性，对应您熟悉的Marchenko-Pastur律和相变分析。技术上，您可用随机矩阵理论中的特征值分布工具（如Tracy-Widom分布）进一步研究该准则的渐近分布或构造假设检验；目前武器库的'高维渐近'项可直接支撑对文中渐近框架的复现或扩展，属于'立即可做'的follow-up。此外，本文的极值应用场景也可作为您进入极端事件统计分析的入门阅读。

## 非参数 / 半参数  *(nonparam_semipara, 8 篇)*

### 1. [10.1111/sjos.70020](https://doi.org/10.1111/sjos.70020) — Combining probability and non‐probability samples using semi‐parametric quantile regression and a nonparametric estimator of the participation probability
- **作者**: Emily Berg, Sixia Chen, Cindy Yu
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Iowa State University · University of Oklahoma Health Sciences Center
- **分类**: vol 52 · issue 4 · pp 2128-2151
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在非概率样本与概率样本的数据整合设定下，目标是估计总体分位数等 estimand，关键假设是参与概率的 positivity 与样本间的可整合性。本文提出两种方法：基于半参数分位数回归的 mass-imputation 估计器，以及融合非参数参与概率估计器的 doubly-robust (DR) 估计器。半参数分位数回归对模型误设与异常值更稳健；DR 估计器在参与概率模型或分位数回归模型之一正确时即可保证一致性。理论部分给出了所提估计器的方差估计与渐近正态性。对您可能有用：本文的 DR 框架与非参数参与概率估计的结合，直接关联到 semiparametric efficiency 与 causal inference 中的 selection bias 校正。
- **关键技术**: `doubly-robust estimation`, `semi-parametric quantile regression`, `mass imputation`, `nonparametric participation probability estimation`, `data integration`, `variance estimation`
- **为什么对您有用**: 本文直接连接到 semiparametric theory 与 causal inference 中的 selection bias / missing data 设定，其 doubly-robust 结构与非参数参与概率估计器是 semiparametric efficiency 理论的典型应用场景。用 technical_arsenal 中 very_familiar 的 estimation theory in causal inference 与 moderately_familiar 的 semiparametric theory，可以分析其 DR 估计器是否达到 semiparametric efficiency bound，或用 minimax bounds 验证其非参数参与概率估计的收敛率是否影响 DR 估计器的整体率。follow-up 判断：立即可做——用 very_familiar 的 minimax bounds 与 estimation theory 即可展开对其效率性质的验证与改进。

### 2. [10.1111/sjos.70008](https://doi.org/10.1111/sjos.70008) — Collapsibility of the Conditional Models of CG‐Graphical Models
- **作者**: Xiangdong Xie, Jianhua Guo, Shiyuan He
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Beijing Technology and Business University
- **分类**: vol 52 · issue 4 · pp 1735-1762
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 在 CG-图模型（chain graph mixed graphical models）框架下，研究条件模型在变量边际化后的可折叠性（collapsibility），即剔除部分变量后模型结构及参数估计是否保持不变。Didelez & Edwards (2004) 曾给出等价条件但依赖特定假设，Liu & Guo (2013) 在纯离散或纯连续设定下去除了该假设。本文通过考察边际化后模型交互作用的保留（interaction preservation），绕开了不可处理的条件密度计算，在混合变量类型的最一般设定下完全去除了额外假设，给出了模型可折叠性的一组等价条件。进一步，本文证明了条件模型的模型可折叠性与估计可折叠性（estimate-collapsibility）的等价性。对您可能有用：图模型的可折叠性理论与因果推断中的干预可识别性及混杂消除有深层结构对应，本文的 interaction preservation 技术视角可为 proximal CI 中的 negative control 选择提供图模型侧的理论参照。
- **关键技术**: `CG-graphical models`, `model collapsibility`, `estimate collapsibility`, `interaction preservation`, `mixed variable graphical models`, `marginalization equivalence`
- **为什么对您有用**: 本文连接到因果推断中的图模型 identification theory 子方向：可折叠性本质上刻画了图模型中哪些变量可被安全边际化而不破坏因果参数的识别与估计，与混杂消除、IV 设定直接相关。用您 very_familiar 的 nonparametric statistics 与 moderately_familiar 的 identification theory in causal inference，可以审视本文的 interaction preservation 条件在 DAG/chain graph 因果解释下的等价干预条件，寻找从图模型折叠性到 semiparametric efficiency bound 影响的延伸问题。Follow-up 粗判：中期可做——需先在 moderately_familiar 的 identification theory 上长肌肉，将图模型折叠性的代数条件翻译为因果 identification 的可测试假设。

### 3. [10.1111/sjos.70007](https://doi.org/10.1111/sjos.70007) — A Donsker and Glivenko‐Cantelli theorem for random measures linked to extreme value theory
- **作者**: B. Bobbia, C. Dombry, D. Varron
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Clinique Pasteur · Laboratoire de Mathématiques de Besançon · Université Marie et Louis Pasteur · Université de Franche-Comté · National Higher French Institute of Aeronautics and Space
- **分类**: vol 52 · issue 4 · pp 1708-1734
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 本文研究一类与经验测度共享性质的条件随机点测度，在给定外生随机现象下，探讨其 Glivenko-Cantelli 与 Donsker 定理的成立条件。核心设定涉及随机测度对另一随机变量的条件分布，关键 regularity 假设为函数类的 uniform entropy number 条件。作者证明，传统的 uniform entropy number 条件足以推导出此类条件随机测度的 GC 与 Donsker 收敛，并进一步建立了 bootstrap Donsker 定理。主要理论结果为条件经验过程的渐近正态性与 bootstrap 有效性，应用覆盖极值理论与最近邻规则。对您有用之处在于，该框架为条件分布/条件经验过程的非参数推断提供了严格的 empirical process 工具，可直接支撑 semiparametric theory 中涉及条件均值/条件分布的 influence function 分析。
- **关键技术**: `uniform entropy number`, `Donsker theorem for random measures`, `Glivenko-Cantelli class`, `bootstrap empirical process`, `conditional point measure`, `extreme value theory`
- **为什么对您有用**: 本文直接连接到 semiparametric & nonparametric theory 子方向，为条件经验过程提供了 Donsker/GC 收敛的严格工具，这在推导 semiparametric efficiency bound 与 one-step estimator 的 influence function 时是关键前提。您武器库中 very_familiar 的 nonparametric statistics 与 minimax bounds 可直接用来验证本文 entropy 条件在具体 semiparametric 模型（如条件 ATE 估计）中的适用性，判断其 bootstrap 有效性是否可迁移到 debiased ML 场景。判断：立即可做——用您熟悉的 empirical process 与非参数理论即可展开阅读与迁移尝试。

### 4. [10.1111/sjos.70004](https://doi.org/10.1111/sjos.70004) · [arXiv](https://arxiv.org/abs/2302.09510) — Smooth backfitting for additive hazard rates
- **作者**: Stephan M. Bischofberger, Munir Hiabu, Enno Mammen, Jens Perch Nielsen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1625-1669
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在右截断与右删失生存数据设定下，本文研究加性风险率模型（additive hazard rate）的非参数估计，目标 estimand 为各协变量的平滑加性风险率成分。核心方法是将 smooth backfitting 从加性回归移植到风险率模型，构造出将数据投影到多变量平滑加性风险率函数空间的估计量；即使真实风险率不具备加性结构，该估计量仍收敛到 L2 最优加性投影，这区别于传统加性结构估计在模型误设时目标模糊的问题。全文给出估计量的完整渐近理论，包括逐成分的 n^{-1/2}-CAN 性质与联合渐近正态性。对您可能有用：该投影解释与 Mammen 等人一系列 smooth backfitting 工作一脉相承，为 additive semiparametric 模型的 misspecification-robust 估计提供了一个清晰的 L2-projection 视角。
- **关键技术**: `smooth backfitting`, `additive hazard rate model`, `L2-projection under misspecification`, `right-censoring and right-truncation`, `n^{-1/2}-CAN asymptotic theory`
- **为什么对您有用**: 本文直接连接到 semiparametric & nonparametric theory 子方向，特别是 additive model 的 smooth backfitting 估计及其在模型误设下的 L2-projection 解释。您武器库中 very_familiar 的 nonparametric statistics 与 moderately_familiar 的 M-estimation theory / semiparametric theory 完全可以攻入这篇 paper 的渐近理论部分，尤其是验证其投影估计量的 influence function 与 semiparametric efficiency bound 是否可达。**立即可做**：用 very_familiar 的 minimax bounds 工具检查该加性风险率估计是否达到最优收敛率，或用 moderately_familiar 的 semiparametric theory 推导其 one-step debiased 版本。

### 5. [10.1111/sjos.70028](https://doi.org/10.1111/sjos.70028) · [arXiv](https://arxiv.org/abs/2310.10115) — A non‐asymptotic analysis of the single component PLS regression
- **作者**: Luca Castelli, Irène Gannaz, Clément Marteau
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Institut Camille Jordan · Laboratoire des Sciences pour la Conception, l'Optimisation et la Production
- **分类**: vol 52 · issue 4 · pp 2314-2351
- 相关性 5/10 · novelty: `sharper_rate`
- **摘要**: 在高维回归设定下研究单成分偏最小二乘(PLS)的预测误差，目标是在有限样本下给出高概率的二次损失非渐近上界。核心机制是对第一PLS成分施加预正则化，从而在高维设计矩阵下控制预测风险；随后将结论推广至稀疏PLS(sPLS)，证明其上界与Lasso的预测误差界同阶，但需额外对设计矩阵施加restricted eigenvalue条件。关键技术工具包括非渐近高维分析、restricted eigenvalue条件与PLS成分的正则化控制。主要理论结果是给出了单成分PLS及sPLS的非渐近预测误差界，对您可能有用：为高维半参数/非参数估计中PLS型投影估计器的风险分析提供有限样本保证。
- **关键技术**: `Partial Least Squares (single-component)`, `non-asymptotic prediction bound`, `sparse PLS`, `restricted eigenvalue condition`, `preliminary regularization of PLS component`
- **为什么对您有用**: 连接到高维统计与半参数理论子方向：PLS是半参数投影估计的常用工具，本文给出的非渐近界为评估其高维风险提供直接依据。用 very_familiar 的 minimax bounds for estimation problems 可以验证本文声称的 sharper rate 是否紧，或与 Lasso 界做更精细的对比。**中期可做**：需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以将单成分结论推广至多成分 PLS 的 M-估计框架。

### 6. [10.1111/sjos.70010](https://doi.org/10.1111/sjos.70010) — Distorted distributions and ROC curves
- **作者**: Marco Capaldo, Jorge M. Arevalillo, Jorge Navarro
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Salerno · Universidad Nacional de Educación a Distancia · Universidad de Murcia
- **分类**: vol 52 · issue 4 · pp 1786-1815
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文在ROC曲线和序优势（OD）曲线的基础上提出了一类新的扭曲分布函数。通过将ROC和OD扭曲解释为适当相对随机变量的累积分布函数，刻画了多种随机序和老化性质，并与Lorenz曲线和Gini指数建立了联系。进一步定义了基于ROC曲线和OD曲线下部分面积的新扭曲函数，指出其与单变量偏斜模型及均衡分布的关系。理论结果通过实际数据应用加以展示，使用了ROC曲线的半参数估计方法。这对熟悉半参数和非参数理论的读者而言，是ROC分析中扭曲方法的一个系统扩展，尤其适用于流行病学诊断准确性评估。
- **关键技术**: `ROC curve`, `ordinal dominance curve`, `distortion function`, `semiparametric estimation`, `Lorenz curve`, `Gini index`
- **为什么对您有用**: 本文聚焦ROC曲线的半参数估计和新扭曲函数，属于非参数/半参数方法的研究，与研究者primary interest中的semiparametric & nonparametric theory直接重叠。此外，ROC分析是流行病学诊断评估的核心工具，对secondary interest中的流行病学方向具有实际应用价值。研究者熟悉的非参数统计和半参理论足以理解和评估本文方法，立即可将其应用于流行病学数据中的诊断准确性分析。

### 7. [10.1111/sjos.70018](https://doi.org/10.1111/sjos.70018) · [arXiv](https://arxiv.org/abs/2405.12581) — Spectral analysis for the inference of noisy Hawkes processes
- **作者**: Anna Bonnet, Felix Cheysson, Miguel Martinez Herrera, Maxime Sangnier
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Laboratoire d’Analyse et de Mathématiques Appliquées
- **分类**: vol 52 · issue 4 · pp 2061-2109
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在带噪声的 Hawkes 过程设定下，观测事件是真实 Hawkes 过程与独立 Poisson 过程的不可区分混合，目标是同时估计两过程的参数。由于标准 MLE 不可行或计算代价过高，本文基于过程的二阶谱性质（spectral log-likelihood）提出新估计量。核心理论贡献包括给出模型可辨识性的充分条件，主要聚焦指数核但也讨论了其他核形式。估计量无需知道每个观测事件的来源标签，且在估计两个过程参数时均表现准确。对您可能有用：该谱方法本质上是一种频域上的 semiparametric/非参数推断思路，可辨识性分析对理解混合点过程的 identification 有参考价值。
- **关键技术**: `Hawkes process with Poisson noise`, `spectral log-likelihood`, `second-order spectral properties`, `model identifiability`, `exponential kernel`
- **为什么对您有用**: 本文连接到 semiparametric & nonparametric theory 子方向中的 identification theory：混合点过程的可辨识性充分条件是纯粹的 identification 问题，与因果推断中的 identification 逻辑同构。用 technical_arsenal 中 very_familiar 的 minimax bounds for estimation problems 可尝试分析该谱估计量的收敛率是否达到 minimax optimal，或用 moderately_familiar 的 identification theory in causal inference 视角审视其可辨识性条件的松弛可能。follow-up 判断：中期可做——需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以严格建立该谱 M-估计量的渐近正态性与效率界。

### 8. [10.1111/sjos.70012](https://doi.org/10.1111/sjos.70012) · [arXiv](https://arxiv.org/abs/2501.13599) — Learning under commission and omission event outliers
- **作者**: Yuecheng Zhang, Guanhua Fang, Wen Yu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1852-1880
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在时间点过程（temporal point process）框架下，目标是学习事件流的强度函数，同时处理两类异常事件：commission（多余事件）与 omission（缺失事件）。作者提出一种新颖的权重函数，动态调整每个观测事件的贡献，使得最终估计器在无异常时保持无偏性、有异常时具备鲁棒性。该方法被应用于分类与变点检测两个下游任务，理论分析证明了估计器的统计性质，数值实验验证了其有效性。据作者声称，这是首个能在理论上同时处理两类异常事件的方法。对您可能有用：该权重函数的构造与鲁棒 M-estimation 思路相近，其无偏-鲁棒双重性质的证明可类比 semiparametric efficiency 中的 influence function 设计。
- **关键技术**: `temporal point process`, `robust M-estimation`, `weighted intensity estimation`, `commission and omission outliers`, `change point detection`
- **为什么对您有用**: 本文连接到 semiparametric & nonparametric theory 子方向中的鲁棒估计问题，其权重函数的构造与您熟悉的 M-estimation theory 和 influence function 设计有直接对应。用您 very_familiar 的 M-estimation theory 可以直接审视其声称的 unbiasedness + robustness 双重性质的紧性，甚至用 minimax bound 检验其鲁棒性 rate 是否可达最优。follow-up 判断：立即可做——用 M-estimation 与 influence function 工具即可展开对其理论性质的深入分析。

## 数理统计 / 假设检验  *(hypothesis_testing, 5 篇)*

### 1. [10.1111/sjos.70009](https://doi.org/10.1111/sjos.70009) — Inference on data with both multiplicative and additive measurement errors
- **作者**: Yuxiang Zong, Yinfu Liu, Yanyuan Ma, Ingrid Van Keilegom
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Statistics Belgium · KU Leuven · Maastricht University · Pennsylvania State University
- **分类**: vol 52 · issue 4 · pp 1763-1785
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究变量同时受加法和乘法测量误差影响时的统计推断问题。首先建立两种误差方差的可识别性条件，然后提出基于矩的估计量，证明其相合性和渐近正态性，并构造检验误差类型是否存在的假设检验。进一步开发基于似然的方法以逼近误差变量的密度函数。在线性回归框架下，结合回归校准（Regression Calibration）和模拟外推（SIMEX）方法讨论回归参数的估计与修正。数值模拟和实际数据应用验证了所提方法的有效性。该工作直接涉及测量误差的推断，与您对逆问题随机噪声和识别理论的熟悉领域高度相关，可借鉴其矩估计和检验思路到因果推断中的测量误差处理。
- **关键技术**: `moment-based estimation`, `asymptotic normality`, `hypothesis testing for measurement error types`, `likelihood-based density approximation`, `Regression Calibration`, `SIMEX`
- **为什么对您有用**: 本文与您的主要兴趣“逆问题随机噪声”和“识别理论”直接相关，特别是同时存在加法和乘法误差的可识别性条件和矩估计方法可以迁移到因果推断中处理测量误差问题（如IV估计中的测量误差）。您对“inverse problems with random noise”非常熟悉，可以立即尝试将本文方法嵌入现有因果推断框架中，属于立即可做的方向。

### 2. [10.1111/sjos.70019](https://doi.org/10.1111/sjos.70019) — Asymptotic distribution‐free tests related to maximum mean discrepancy
- **作者**: Kai Xu
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Anhui Normal University
- **分类**: vol 52 · issue 4 · pp 2110-2127
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在基于最大均值差异（MMD）的多变量两样本 goodness-of-fit 检验设定下，目标是克服原假设分布依赖未知分布而需昂贵 permutation test 的瓶颈。本文提出基于特征核均值相等性的组合概率检验（combined probability test），利用特征核的二阶矩存在性作为关键 regularity 条件。核心机制是构造渐近分布无关（asymptotically distribution-free）的检验统计量，使其具有已知临界值，无需重抽样；同时通过局部功效分析证明该检验在 √n-邻域内具有非平凡功效（n^{-1/2}-局部一致性）。主要理论结果包括：对所有固定替代假设的一致性，以及在 √n-局部替代下的非平凡功效界；实证通过模拟与基因表达数据验证。对您有用：本文直接涉及假设检验与非参数理论，其渐近分布无关的构造思路可启发您在 higher-order U-statistics / HOIF 框架下设计免于 permutation 的检验统计量。
- **关键技术**: `maximum mean discrepancy (MMD)`, `combined probability test`, `asymptotically distribution-free test`, `characteristic kernel mean`, `local power analysis`, `n^{-1/2}-neighborhood consistency`
- **为什么对您有用**: 本文直接连接到您 primary interest 中的假设检验与非参数理论子方向，处理的是 MMD 两样本检验的计算-统计权衡（避免 permutation 的计算代价）。您武器库中 very_familiar 的 higher-order U-statistics 计算与 moderately_familiar 的 HOIF 理论可以直接攻本文的口子：用 HOIF / U-statistic projection 视角分析其组合概率检验的功效界是否可进一步 sharpen，或探索更高阶核均值统计量的分布无关性。**立即可做**：用 very_familiar 的 U-statistic 工具复现并扩展其局部功效分析。

### 3. [10.1111/sjos.70013](https://doi.org/10.1111/sjos.70013) · [arXiv](https://arxiv.org/abs/2406.19141) — Improved small‐sample inference for functions of parameters in the k$$ k $$‐sample multinomial problem
- **作者**: Michael C. Sachs, Erin E. Gabriel, Michael P. Fay
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1881-1898
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在 k 样本多项分布设定下，目标是推断多项概率的实值连续函数（如 risk difference / ratio），当函数在真实参数处不可微或样本量小时，bootstrap 与 delta method 表现不佳。本文提出一种 exact inference 方法，构造精确 p-value 与置信区间，严格证明其控制 type I error 且覆盖率不低于名义水平。由于精确 p-value 计算复杂，作者给出 Monte Carlo 近似实现并证明其关于迭代次数的一致性。方法适用于任意 k 样本、任意类别数的一般连续函数。对您有用：为小样本因果效应参数（如不可微的 risk difference）的精确检验提供新工具，连接 hypothesis testing 与因果推断 estimation 的交叉点。
- **关键技术**: `exact test`, `multinomial parameter function`, `Monte Carlo p-value`, `nondifferentiable parameter inference`, `small-sample coverage guarantee`
- **为什么对您有用**: 本文直接连接 hypothesis testing 子方向，处理小样本下不可微参数函数的精确推断，这在 epidemiology 的 risk difference / ratio 应用中常见。用 very_familiar 中的 nonparametric statistics 与 M-estimation theory（moderately_familiar）即可审视其 exact p-value 构造与一致性证明的细节。立即可做：用现有武器复现其 Monte Carlo 实现并检验在不可微 ATE 函数下的表现。

### 4. [10.1111/sjos.70003](https://doi.org/10.1111/sjos.70003) · [arXiv](https://arxiv.org/abs/2305.19031) — Stein's method of moments
- **作者**: Bruno Ebner, Adrian Fischer, Robert E. Gaunt, Babette Picker, Yvik Swan
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1594-1624
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文基于Stein算子对概率分布的微分算子刻画，提出了一类新的点估计方法——Stein矩估计法（SMOM），适用于严格平稳遍历过程的边际参数估计。SMOM估计量具有相合性和渐近正态性，且由于Stein算子通常形式简单，可在标准方法（如伪极大似然需要数值优化）时给出显式估计。对于i.i.d.观测，通过选取数据依赖的测试函数可以获得渐近有效估计，并且存在一列显式SMOM估计量收敛到极大似然估计。模拟表明，在若干单变量连续分布上，SMOM在偏差和均方误差方面与MLE及其他常用方法竞争性相当。该方法提供了一个统一且灵活的估计框架，特别适合需要显式估计且避免数值优化的场景。对您的意义在于：该方法属于数学统计与估计理论的新工具，可与您熟悉的非参数统计和估计理论结合，探索其在因果推断灵敏度分析或半参数估计中的应用潜力。
- **关键技术**: `Stein operator`, `method of moments`, `asymptotic efficiency`, `consistency and asymptotic normality`, `data-dependent test functions`
- **为什么对您有用**: 该论文直接关联您的数学统计与估计理论兴趣，提出了一种基于Stein算子的新点估计框架，与您熟悉的估计理论（very_familiar中的估计理论）直接对接。您可以用非参数统计工具分析SMOM在不同分布族上的表现，或将其思想推广到半参数模型。中期可做：需先熟悉Stein算子及其计算性质，但目前非核心武器；一旦掌握，可探索与您高阶U统计量（treewidth/einsum）结合的可能性。

### 5. [10.1111/sjos.70017](https://doi.org/10.1111/sjos.70017) — False selection rate control in mixture models
- **作者**: Ariane Marandon, Tabea Rebafka, Etienne Roquain, Nataliya Sokolovska
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: The Alan Turing Institute · Centre National de la Recherche Scientifique · Université Paris Cité · Sorbonne Université · Sorbonne Paris Cité · Université Sorbonne Nouvelle · Biologie Computationnelle, Quantitative et Synthétique
- **分类**: vol 52 · issue 4 · pp 2014-2060
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在无监督混合模型框架下，研究聚类任务中部分分类（abstention）的误选率（FSR）控制问题，目标 estimand 为 FSR，关键假设为混合模型参数可辨识及常规 regularity 条件。核心提出 plug-in FSR 控制程序：先估计混合参数，再基于后验概率设定分类阈值，仅对置信度足够高的样本做簇归属判定，其余 abstain；并给出 FSR 偏离目标水平的显式余项界。Bootstrap 版本通过重采样修正参数估计不确定性，数值实验显示其 FSR 控制更紧、有效样本占比更高。对您有用：此工作将多重检验 FDR 控制逻辑迁移到无监督聚类，与您 hypothesis testing 和 semiparametric theory 的兴趣直接交汇。
- **关键技术**: `false selection rate control`, `mixture model plug-in estimation`, `classification with abstention`, `bootstrap correction`, `posterior probability thresholding`
- **为什么对您有用**: 直接连接 hypothesis testing 子方向（将 FDR/FSR 框架从监督迁移到无监督设定），也触及 semiparametric theory（混合模型参数估计与余项界）。用 very_familiar 的 minimax bounds 与 M-estimation theory（moderately_familiar）可以审视其 plug-in 余项界是否紧、是否可推导更优的 higher-order 修正。**中期可做**：需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以推导更精细的 FSR 偏差展开或 semiparametric efficiency bound。

## 统计计算 / 算法  *(stat_computing, 4 篇)*

### 1. [10.1111/sjos.70022](https://doi.org/10.1111/sjos.70022) · [arXiv](https://arxiv.org/abs/2407.13446) — Subsampled One‐Step Estimation for Fast Statistical Inference
- **作者**: Miaomiao Su, Ruoyu Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 2187-2208
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在大规模数据中，子采样是降低计算负担的常用手段，但现有子采样估计器收敛速率仅为 n^{-1/2}（n 为子样本量），远逊于全数据估计器的 N^{-1/2}（N 为全样本量），造成显著的估计效率损失。本文提出子采样一步（SOS）估计方法，利用子采样估计器与全数据估计器之间的渐近展开关系，对子采样估计进行一步更新，从而将收敛速率提升至 N^{-1/2}。SOS 估计器在一般情形下渐近分布非正态，作者据此构造了置信区间；当子样本占比 n/N → 0 时，其渐近正态且与全数据估计等价。模拟与真实数据分析表明，SOS 估计器在计算时间与均匀子采样几乎持平的同时，估计效率接近全数据估计器。该工作直接回应了大规模统计推断中计算与效率的权衡，您可将其与自己的统计计算与效率理论兴趣对接，尤其在处理因果推断中的大样本数据时，SOS 能作为加速估计的即用工具。
- **关键技术**: `subsampling`, `one-step estimation`, `asymptotic expansion`, `confidence interval construction`, `N^{-1/2} convergence rate`, `uniform subsampling estimator`
- **为什么对您有用**: 本文直接涉及您 primary interest 中的统计计算（大规模数据的子采样加速）与效率理论（通过一步更新弥补效率损失），与您近年关注的统计计算权衡（computationally constrained statistics）高度相关。您武器库中“M-estimation theory”和“nonparametric statistics”足以完全理解其渐近论证，并可立即将其思想迁移到因果推断中 IPW/DR 估计量的子采样版本，或扩展到更高阶的 U-统计量场景（您的 work on higher-order U-statistics 已涉及计算复杂度）。该方法是立即可做的：利用您熟悉的渐近理论和软件开发经验复现算法并设计更复杂的子采样策略（如 Leverage-based subsampling）。

### 2. [10.1111/sjos.70015](https://doi.org/10.1111/sjos.70015) · [arXiv](https://arxiv.org/abs/2306.15422) — Debiasing piecewise deterministic Markov process samplers using couplings
- **作者**: Adrien Corenflos, Matthew Sutton, Nicolas Chopin
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1932-1974
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在连续时间 PDMP（piecewise deterministic Markov process）采样器框架下，目标是构造在无限计算资源而非无限迭代次数下精确无偏的期望估计量。本文将 MCMC coupling debiasing 方法推广至连续时间，为 bouncy、boomerang 和 coordinate sampler 三类 PDMP 构造了具体耦合机制，从而消除非渐近偏差，使估计量可尴尬并行化。核心技术工具是 PDMP 路径的同步耦合与 meeting time 截断，理论保证基于 Lindvall 等人的经典耦合不等式。初步实验表明方法随目标分布维度的增长具有合理的 scaling。对您可能有用：该工作将统计计算中的无偏并行化技术拓展至连续时间采样器，为高维 PDMP 的计算效率与偏差消除提供了新路径。
- **关键技术**: `PDMP samplers`, `coupled MCMC debiasing`, `bouncy particle sampler`, `boomerang sampler`, `meeting time`, `embarrassingly parallelization`
- **为什么对您有用**: 本文连接到统计计算与数值方法方向，聚焦 PDMP 采样器的无偏并行化，属于计算算法层面的推进。从 technical_arsenal 看，您 very_familiar 的软件开发与高维渐近理论可以直接评估其维度 scaling 实验的合理性，但 PDMP 连续时间耦合构造本身需要随机过程耦合的专门知识（您武器库中缺此）。follow-up 判断：**中期可做**——需先在 moderately_familiar 的 M-estimation 理论之外，补充连续时间 Markov 过程耦合与 meeting time 分析的基础（点名缺随机过程耦合理论），才能深入改进其耦合效率或做理论 rate 分析。

### 3. [10.1111/sjos.70024](https://doi.org/10.1111/sjos.70024) — On optimal blocked definitive screening designs: Theoretical insights and computational simplifications
- **作者**: Bo Hu, Yaping Wang, Fasheng Sun
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Dongbei University of Finance and Economics · East China Normal University · Northeast Normal University
- **分类**: vol 52 · issue 4 · pp 2242-2269
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 本文研究确定性筛选设计（DSD）在分块方案下的最优性问题。在线性加二次效应模型下，作者推导了最优分块DSD的理论性质，证明了某些已有分块设计的最优性，并显著降低了搜索最优正交分块设计时的计算复杂度。核心方法包括利用对称性和组合结构来化简优化问题，使得在大规模因子数下也能高效识别最优设计。数值实验验证了理论结果的实际有效性。虽然该文聚焦于实验设计，但其计算简化思路对统计计算中的组合优化问题有一定的参考价值。不过，这与因果推断、高维统计等主要兴趣方向关联较弱。
- **关键技术**: `definitive screening designs`, `blocked designs`, `optimality criteria`, `combinatorial search`, `computational simplification`
- **为什么对您有用**: 本文属于实验设计领域，与您的 primary interests（因果推断、高维统计等）无直接关联。但其关于计算复杂度的化简方法（如利用对称性缩小搜索空间）对 statistical computing 中的组合优化问题有启发；不过目前武器库中缺乏实验设计的核心工具（如具体的最优准则推导），暂不可做后续拓展。

### 4. [10.1111/sjos.70016](https://doi.org/10.1111/sjos.70016) · [arXiv](https://arxiv.org/abs/2304.08242) — The deep latent position topic model for clustering and representation of networks with textual edges
- **作者**: Rémi Boutin, Pierre Latouche, Charles Bouveyron
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Laboratoire de Probabilités et Modèles Aléatoires · Laboratoire de Probabilités, Statistique et Modélisation · Institut Universitaire de France · Laboratoire de Mathématiques Blaise Pascal · Université Côte d'Azur · Laboratoire Jean-Alexandre Dieudonné
- **分类**: vol 52 · issue 4 · pp 1975-2013
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 本文提出Deep-LPTM，一种结合变分图自编码器和概率主题模型的网络聚类与表示方法，处理节点-文本边构成的异构图。模型通过两个嵌入空间分别表示节点和文本边，并引入IC2L准则进行模型选择，以平衡聚类质量和可视化效果。推断使用变分贝叶斯算法。在合成数据上，Deep-LPTM在节点聚类恢复上优于ETSBM和STBM等现有方法。最后在Enron邮件数据上展示了有意义的图结构可视化。该方法属于非监督图表示学习，其变分推断框架可用于统计计算中的混合模型推理。
- **关键技术**: `variational graph auto-encoder`, `model-based clustering`, `topic model`, `IC2L model selection criterion`, `latent position model`
- **为什么对您有用**: 本文连接统计计算方向，展示了变分推理在图数据聚类中的具体实现。你的武器库中“软件开发”能力可用于复现或扩展其变分EM代码，但核心的图神经网络训练技术（如消息传递）不在当前熟悉范围内，属于暂不可做的gateway阅读——需先积累图神经网络变分推断知识。

## 其他  *(other, 5 篇)*

### 1. [10.1111/sjos.70005](https://doi.org/10.1111/sjos.70005) · [arXiv](https://arxiv.org/abs/2504.10022) — Parameters estimation of a threshold Chan–Karolyi–Longstaff–Sanders process from continuous and discrete observations
- **作者**: Sara Mazzonetto, Benoît Nieto
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1670-1707
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对带多个阈值的自激遍历连续时间过程（threshold CKLS 过程），研究漂移参数的最大似然估计（MLE）与拟最大似然估计（QMLE）的渐近性质。该过程是 Vasicek、CIR、Black-Scholes 等经济计量模型的推广，允许动态在阈值处发生改变。在连续时间观测和高频离散观测下，证明了估计量满足相同的渐近正态性，且收敛速率与经典连续时间结果一致。还讨论了扩散系数的估计方法，并通过模拟与真实数据验证了带多个阈值的实际必要性。方法上未引入新的估计框架或效率理论，而是将标准 MLE/QMLE 推广到该门限模型。对您而言，本文属于经典参数估计理论在经济模型中的应用，但未涉及因果推断、高维或半参效率等核心兴趣方向，可作为了解时间序列阈值模型的快速入门。
- **关键技术**: `Maximum likelihood estimation`, `Quasi-maximum likelihood estimation`, `Threshold process`, `High-frequency observations`, `Asymptotic normality`, `Diffusion coefficient estimation`
- **为什么对您有用**: 本文与您的主要兴趣（数学统计中的估计理论）有弱关联，但实质是参数模型在特定阈值过程中的应用，未涉及因果推断、高维或半参效率等核心方向。在次要兴趣的经济理论中，该过程常用于利率建模，可作为应用实例。从技术武器库看，本文的 MLE 渐近分析可用 moderately_familiar 中的 M-estimation 理论进行验证，但结果已完备，暂无可直接推进的新问题。总体来说，本文相关性较低，不值得投入深度阅读。

### 2. [10.1111/sjos.70011](https://doi.org/10.1111/sjos.70011) · [arXiv](https://arxiv.org/abs/2501.08810) — Nonparametric inference for Poisson‐Laguerre tessellations
- **作者**: Thomas van der Jagt, Geurt Jongbloed, Martina Vittorietti
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1816-1851
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对Poisson-Laguerre分割（一种由泊松过程生成的随机凸多面体分划）中的统计推断问题，目标是估计生成点到达时间的分布函数，该函数唯一决定泊松过程的强度测度。提出了两个非参数估计量，它们仅依赖于生成非空细胞的泊松过程点及对应的细胞本身。证明了当观测窗口无界扩张至全空间时，估计量具有强相合性。还考虑了立体学（stereological）设置：根据观测到的截面Poisson-Laguerre分割来估计高维母体分割对应的分布函数。方法上均采用经验分布构造和细胞几何特征，未使用核或样条等平滑技术。该问题的统计推断模型类似于空间点过程中的非参数反问题，但其目标分布并非直接观测。对您可能有用：虽然该模型与您的核心研究方向（因果推断、高维统计）距离较远，但其非参数估计的一致性证明思路可迁移至其他涉及随机几何结构的设定，不过需额外投入学习随机分割的基础知识。
- **关键技术**: `Poisson-Laguerre tessellation`, `strong consistency`, `nonparametric estimation`, `stereological inference`, `point process intensity measure`
- **为什么对您有用**: 本文属于非参数统计在空间点过程（随机几何）中的具体应用，与您的主要兴趣“非参数统计”子方向相关。您非常熟悉的工具“nonparametric statistics”可用于分析此类估计量的渐近性质，但本文仅证明了强相合性，尚未给出收敛速度或 minimax 界——这恰好是您的武器库中“minimax bounds for estimation problems”可以立即可做的方向。不过，该问题模型的几何背景（Laguerre分割）需要额外学习空间统计的基础概念，但核心非参数分析工具已足够。因此 follow-up 粗判：立即可做（用现有 minimax 理论推导该估计量的收敛速率并判断最优性）。

### 3. [10.1111/sjos.70000](https://doi.org/10.1111/sjos.70000) — A proper concordance index for models with crossing hazards
- **作者**: A. Gandy, T. J. Matcham
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Imperial College London
- **分类**: vol 52 · issue 4 · pp 1479-1504
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在生存分析中，一致指数（concordance index）是模型选择与评估最常用的指标之一，但现有版本在风险函数可交叉（crossing hazards）的模型（如分层比例风险模型或某些机器学习模型）下并不保证是 proper 的——即可能偏好错误的模型而非真实生成模型。本文首先精确刻画了以配对个体第一个事件时间的预测风险率排序时，一致指数保持 proper 所需的条件。基于该条件，作者提出一个新的 proper concordance index，并通过一系列实验证明，先前指标可能错误地偏好错误模型，而新指标不会。此外，还探讨了将一致指数作为深度学习模型辅助损失函数目标的应用。新指标保持了解释性，可作为生存模型的可靠评价指标。对您而言，本文关于“proper scoring rule”的严格论证思路，可启发因果推断中治疗效果评估、预测校准等场景的指标设计，但需要先熟悉生存分析中交叉风险的设定。
- **关键技术**: `proper concordance index`, `crossing hazards`, `risk ordering via predicted hazard rate`, `stratified proportional hazards`, `model evaluation in survival analysis`
- **为什么对您有用**: 本文深入研究了一个常用评估指标（concordance index）在模型有交叉风险时的 properness 问题，这直接联系到您在假设检验和模型评价中对指标性质的关注。您非常熟悉的 ‘minimax bounds for estimation problems’ 思路可迁移至此：检查新指标在哪些数据分布下达到最优判别力，但需要补足生存分析中交叉风险的具体 theory（如时变风险函数估计）。目前此文献属于中期可做——可先用非参数生存模型数值验证其 properness 条件，再尝试将类似条件推广到因果推断中的平均处理效果评估指标。

### 4. [10.1111/sjos.70014](https://doi.org/10.1111/sjos.70014) — Construction of maximum projection Latin hypercube designs using number‐theoretic methods
- **作者**: Yuxing Ye, Ru Yuan, Yaping Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: East China Normal University · Zhongnan University of Economics and Law
- **分类**: vol 52 · issue 4 · pp 1899-1931
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 本文针对计算机实验中仅部分因子活跃的场景，研究最大投影拉丁超立方体设计（MaxPro LHD）的代数构造问题。基于好格点设计（good lattice point designs）和数论方法，提出了两种显式构造方案，无需搜索或优化即可生成设计。所得设计在log‐距离准则下达到渐近最优，并几乎满足MaxPro下界；同时在列正交性、最大最小距离和均匀投影准则上表现优异。构造方法依赖于数论中的同余类划分和整数格理论，避免了传统随机搜索的计算开销。仿真实验验证了设计在多种维度下的实用性与鲁棒性。对您而言，本文涉及统计计算中的算法构造，是计算机实验设计领域的方法学进展，但与其主要研究方向（因果推断、高维统计等）连接较弱。
- **关键技术**: `good lattice point designs`, `number-theoretic construction`, `asymptotic optimality in log-distance`, `MaxPro lower bound`, `uniform projection criterion`
- **为什么对您有用**: 本文属于统计计算中的实验设计构造，与您的统计计算（numerical methods, algorithm）兴趣有一定交集，但核心问题（MaxPro LHD的代数构造）与您的主要研究方向（因果推断、高维统计、效率理论）距离较远，属于间接相关。武器库中的'非参数统计'和'高维渐近'在此处不直接适用，且您对实验设计领域尚未建立深入知识，因此暂不可做。

### 5. [10.1111/sjos.12728](https://doi.org/10.1111/sjos.12728) — Issue Information
- **作者**: 
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4
- 相关性 0/10 · novelty: `minor`
- **摘要**: 该论文是《Scandinavian Journal of Statistics》第52卷第4期的目录与版权信息，属于期刊前页内容，不包含任何研究论文。摘要讲述了Wiley出版社的ESG使命，与统计学无关。因此无实质性统计方法或应用贡献。
- **为什么对您有用**: 该论文为非研究性内容，与因果推断、高维统计、半参理论等研究方向无任何关联。不作为阅读推荐。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

