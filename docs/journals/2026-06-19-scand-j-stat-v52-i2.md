# Scand. J. Stat. — Vol 52  Issue 2  ·  2026-06-19

- 共 21 篇 · Scandinavian Journal of Statistics
- 目录核对 ✅ 未见遗漏（对照 OpenAlex 20 篇，权威目录可能尚未完全收录本期）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Scandinavian Journal of Statistics》第52卷第2期的21篇论文大致分布于三条主线：**高维统计中的偏差修正与后选择推断**、**缺失数据与非参数条件估计**、以及**生存/时间至事件预测的推断框架**。其余散见于实验设计（最优设计检验成对差异）、贝叶斯非参数（enriched Pitman–Yor过程）、协整秩不确定性、流数据复合分位数回归、函数响应回归、空间交通估计等专题，主题相对分散。

高维统计领域出现最密集，共4篇直接处理高维下的估计偏差与选择后推断。“高维方差估计在抽样调查中”揭示了传统方差估计量在高维辅助模型下的偏差来源，并基于高维渐近理论提出偏差修正估计量。“高维中介分析带生存结局”利用半参数高效影响函数构造稳定一步估计量，实现对筛选后最大自然间接效应的后选择推断，不依赖重抽样或Bonferroni校正。“高维异方差均值回归的支持估计与符号恢复”使用光滑Huber损失和自适应LASSO，在异方差重尾误差下达到符号一致性和ℓ∞最优收敛速率，并联系了knockoffs的FDR控制。“Ratio‐consistency of some invariant U‐statistic‐based estimators”在高维设定下系统构造协方差矩阵函数的不变估计量，推导比率一致性的充分条件，并应用于高维数据排序。这几篇共同关注的是高维参数空间下估计量的偏差、选择不确定性与后选择推断，工具涉及U统计量、高效影响函数、正则化惩罚与偏差修正。

缺失数据与非参数条件估计构成另一条密集主线。“非可忽略缺失数据的半参数方法”避开工具变量假设，联合logistic倾向得分与半参数比例似然比模型改善可识别性，利用密度比模型构造经验似然捕获协变量边际信息，得到√n一致估计量。“统计推断在回归树与随机森林插补调查数据中”在高维框架下给出插补估计量的均方一致性条件，并提出基于K折交叉验证的方差估计器。“条件Aalen–Johansen估计”在有限状态跳过程中估计给定协变量的条件状态占据概率，建立强一致性与渐近正态性。“Kernel density estimation in metric spaces”将核密度估计推广到一般度量空间，给出一致性与渐近正态性，并推导基于MISE的带宽选择准则。“单调回归函数的联合估计”对多个单调函数施加自适应惩罚，利用似然比检验控制惩罚权重，实现效率增益而不过度平滑。这些论文共同处理非参数/半参数框架下的缺失数据、插补、条件分布估计和函数估计，方法工具包括密度比模型、经验似然、随机森林、核估计、惩罚似然等。

生存数据推断主题下有三篇可集中关注：“条件Aalen–Johansen估计”提供非参数条件分布估计的基础工具；“基于受限平均生存时间的预测评估框架”使用逆概率删失加权与模型无关的保形预测，构建预测区间和变量重要性检验；“区间删失数据Cox模型的后选择推断”构造pivot量实现渐近有效的p值与置信区间，绕过选择偏差。三篇分别从非参数条件估计、预测评估和半参数后选择推断角度切入生存数据。

此外，“距离协方差用于分类数据”涉及假设检验与高阶U统计量（鲁棒性、强相合筛选、近似零分布），可归入高维检验主题；“检验成对差异的最优设计”以图论博弈框架推导最大最小最优分配，显式构造新颖设计。

对于因果推断方向的研究者，可优先看“高维中介分析带生存结局”（因果路径中的后选择推断）和“非可忽略缺失数据的半参数方法”（缺失机制下的识别与估计）；半参数效率方向还可关注“高维方差估计在抽样调查中”的偏差修正思路与“条件Aalen–Johansen估计”的渐近正态性结果；高维方向则推荐上述四篇高维论文以及“距离协方差用于分类数据”的筛选和近似分布结果。

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1111/sjos.12770](https://doi.org/10.1111/sjos.12770) · [arXiv](https://arxiv.org/abs/2408.06517) — Post‐selection inference for high‐dimensional mediation analysis with survival outcomes
- **作者**: Tzu‐Jung Huang, Zhonghua Liu, Ian W. McKeague
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 756-776
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在高维中介分析设定下，目标是识别从暴露到生存结局的因果路径中的中介变量，并对筛选后最大自然间接效应（maximal NIE）进行有效 post-selection 推断。核心方法是利用 semiparametric efficient influence function 构造 stabilized one-step estimator，并在 mediator selection 步骤纳入考量后建立其渐近正态性。该推断程序解决了高维筛选带来的 selection 误差，无需依赖重抽样或 Bonferroni 等保守校正。模拟与肺癌基因组数据实证表明方法有良好的经验表现，识别出多个可能中介吸烟对肺癌生存效应的 CpG 位点。对您可能有用：本文将 semiparametric efficiency theory 与 post-selection inference 结合处理高维 mediation，直接连接您对 mediation 与 efficiency bound 的核心兴趣。
- **关键技术**: `semiparametric efficient influence function`, `one-step estimator`, `post-selection inference`, `maximal natural indirect effect`, `high-dimensional mediation`, `survival outcome`
- **为什么对您有用**: 本文直接连接您 primary interest 中的 mediation 分析与 semiparametric efficiency theory：它用 efficient influence function 构造 one-step estimator 解决高维 mediator 筛选后的推断问题，正是您熟悉的 efficiency bound 与 estimation theory 在因果中介设定下的具体应用。您可以用 very_familiar 的 semiparametric theory 与 moderately_familiar 的 identification theory 直接审视其 influence function 构造与 selection-adjusted 渐近正态性证明是否完备，甚至可以尝试用 HOIF 视角看更高阶修正能否进一步改善 finite-sample 表现。**立即可做**：用 very_familiar 的 estimation theory 与 moderately_familiar 的 M-estimation / semiparametric theory 即可展开对其 one-step estimator 渐近性质的验证与潜在改进。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 2 篇)*

### 1. [10.1111/sjos.12776](https://doi.org/10.1111/sjos.12776) — On high‐dimensional variance estimation in survey sampling
- **作者**: Esther Eustache, Mehdi Dagdoug, David Haziza
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Lausanne · McGill University · University of Ottawa
- **分类**: vol 52 · issue 2 · pp 924-959
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在抽样调查的高维线性回归模型设定下（变量数 p 相对样本量 n 较大），研究总体参数方差估计的准确性问题；指出基于一阶 Taylor 展开或 jackknife 的传统方差估计量在此设定下会产生 substantial bias。通过理论与实证分析揭示了偏差来源：高维下辅助模型预测残差的交叉项与正则化偏差未被一阶近似捕捉。提出 bias-adjusted variance estimator，利用高维渐近理论修正偏差，理论上证明修正后估计量在 bias 上表现良好，实证亦验证了其稳健性。对您可能有用：该文的高维偏差修正思路与 debiased ML / semiparametric efficiency 的 orthogonalization 逻辑相通，且 jackknife 失效的分析视角可迁移至高维因果推断的 variance estimation。
- **关键技术**: `high-dimensional linear regression`, `jackknife variance estimation`, `Taylor linearization variance`, `bias-adjusted variance estimator`, `high-dimensional asymptotics`, `survey sampling prediction`
- **为什么对您有用**: 直接连接高维统计与效率理论：高维下传统 jackknife / Taylor 一阶方差估计的 bias 机制分析，与 debiased ML 中 one-step correction 的动机同构。可用 very_familiar 的高维渐近工具直接审视其 bias-adjusted estimator 的渐近展开是否达到 n^{-1/2}-CAN，并判断其修正项是否隐含了某种 orthogonal score 结构。follow-up 判断：立即可做——用 minimax bound / high-dimensional asymptotics 验证其声称的 bias reduction rate 是否紧，并尝试将其 survey sampling 设定下的修正逻辑移植到高维因果推断的 variance estimation 场景。

### 2. [10.1111/sjos.12772](https://doi.org/10.1111/sjos.12772) — Support estimation and sign recovery in high‐dimensional heteroscedastic mean regression
- **作者**: Philipp Hermann, Hajo Holzmann
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Philipps University of Marburg
- **分类**: vol 52 · issue 2 · pp 805-839
- 相关性 7/10 · novelty: `weaker_assumption`
- **摘要**: 本文研究高维线性均值回归模型，允许随机设计和潜在的异方差、重尾误差，目标是支持估计（变量选择）与符号恢复。作者使用一种严格凸的光滑Huber损失函数（其调谐参数依赖问题参数）并结合自适应LASSO惩罚以保证计算效率。理论证明该估计量在异方差重尾设置下达到与同方差轻尾情况相同的符号一致性以及在ℓ∞范数下的最优收敛速率。模拟部分还连接了阈值LASSO和基于knockoffs的FDR控制，展示了Donoho-Tanner过渡曲线在变量选择中的相关性，说明方法具有良好的数值性能。对您而言，该工作直接关联您在高维统计与假设检验方面的兴趣，可作为稳健变量选择理论的扩展参考。
- **关键技术**: `Huber loss (smooth variant)`, `adaptive LASSO`, `sign-consistency`, `high-dimensional linear regression`, `heavy-tailed errors`, `variable selection`
- **为什么对您有用**: 本文属于高维统计中变量选择与符号恢复的稳健推断方向，直接契合您的primary interest中high-dimensional statistics和hypothesis testing的子方向。您very_familiar的high-dimensional asymptotics工具可直接用于分析该估计量的收敛性质（如ℓ∞速率），moderately_familiar的M-estimation理论也可帮助理解Huber损失的非光滑性扩展。**立即可做**：可尝试将本文方法推广至其他模型（如广义线性模型或基于U-statistics的变量选择），利用您对高维渐近和估计理论的掌握快速产出。

## 非参数 / 半参数  *(nonparam_semipara, 10 篇)*

### 1. [10.1111/sjos.12767](https://doi.org/10.1111/sjos.12767) — A novel semiparametric approach to nonignorable missing data by catching covariate marginal information
- **作者**: Manli Cheng, Yukun Liu, Jing Qin
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: East China Normal University · National Institutes of Health · National Institute of Allergy and Infectious Diseases
- **分类**: vol 52 · issue 2 · pp 691-709
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在非可忽略缺失数据设定下，目标参数常因缺失机制与结果变量相关而面临 identifiability 困境；本文避开 instrumental / shadow variable 假设，通过联合 logistic propensity score 模型与 semiparametric proportional likelihood ratio model (SPLRM) 来改善 identifiability。在可识别情形下，作者基于 density-ratio-model 构造 empirical likelihood 以捕获协变量边际分布信息，所得 estimator 证明为 n^{-1/2}-CAN 且达到 semiparametric efficiency bound。在不可识别的例外情形下，则利用协变量边际信息进行 sensitivity analysis。模拟显示该方法对模型误设更稳健。对您有用：本文将 density-ratio / empirical likelihood 与 semiparametric efficiency 结合，直接触及您 primary interest 中的 semiparametric efficiency bound 与 identification theory。
- **关键技术**: `semiparametric proportional likelihood ratio model`, `density-ratio-model-based empirical likelihood`, `semiparametric efficiency bound`, `nonignorable missing data identification`, `sensitivity analysis for unidentifiable case`
- **为什么对您有用**: 本文直接连接您 primary interest 中的 semiparametric efficiency bound 与 causal inference 的 identification theory：在非可忽略缺失（类比于因果中的 unmeasured confounding）下，用 SPLRM 替代 IV/shadow variable 来实现 identification，并在可识别情形下证明达到 efficiency bound。用您 very_familiar 的 minimax bounds / estimation theory 可验证其效率声称是否紧；用 moderately_familiar 的 semiparametric theory 可推导其 influence function 是否为唯一有效路径。Follow-up 判断：**立即可做**——用您熟悉的 semiparametric M-estimation 工具即可复现其 efficiency bound 推导并探索更一般的 propensity 模型设定。

### 2. [10.1111/sjos.12779](https://doi.org/10.1111/sjos.12779) — Kernel density estimation in metric spaces
- **作者**: Chenfei Gu, Mian Huang, Xinyu Song, Xueqin Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Shanghai University of Finance and Economics · University of Science and Technology of China
- **分类**: vol 52 · issue 2 · pp 1018-1057
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文在非欧几里得数据分析背景下，提出了一种基于度量分布函数的度量空间核密度估计方法（MKDE），将传统KDE推广到一般度量空间。方法包含局部和全局两种版本，并建立了在正则性条件下的一致性和渐近正态性等大样本性质。作者进一步推导了基于平均积分平方误差（MISE）的带宽选择准则，使带宽选择在非欧几里得设定下具有可操作性。通过多种模拟设定验证了有限样本性能，并在阿尔茨海默症海马体形状数据的实际应用中展示了方法的有效性。对您而言，本文直接关联您非常熟悉的非参数统计理论，同时其度量空间框架是经典密度估计的自然扩展，便于您利用现有武器库（如 minimax 界、U-statistic 投影）分析其最优性和效率。
- **关键技术**: `Kernel density estimation`, `Metric distribution function`, `Mean integrated squared error (MISE)`, `Bandwidth selection`, `Non-Euclidean data analysis`
- **为什么对您有用**: 本文直接对应您 primary_interests 中的非参数统计理论，提供了在度量空间中进行密度估计的一般框架，属于经典 KDE 的自然推广。您技术中非常熟悉的 nonparametric statistics 和 minimax bounds for estimation problems 足以评估该方法的收敛速度和最优带宽率（立即可做）。此外，文章的真实数据应用（海马体形状）属于形态测量学，可作为您统计计算兴趣的练习数据集。

### 3. [10.1111/sjos.12774](https://doi.org/10.1111/sjos.12774) · [arXiv](https://arxiv.org/abs/2303.02119) — Conditional Aalen–Johansen estimation
- **作者**: Martin Bladt, Christian Furrer
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 873-902
- 相关性 6/10 · novelty: `new_theory`
- **摘要**: 在有限状态跳过程（multi-state model）设定下，本文提出条件 Aalen–Johansen 估计量，目标是估计给定外部或内部协变量信息的条件状态占据概率（conditional state occupation probabilities）。该估计量为通用非参数方法，在生存模型特例下退化为条件 Kaplan–Meier 估计量，且在离散协变量下涵盖近期的 landmark 估计量。核心理论结果是在多变量计数过程的宽松矩条件下（允许转移数无界），建立了强一致性与渐近正态性。对您可能有用：该工作为纵向/多状态因果推断中的非参数条件分布估计提供了基础工具，其渐近正态性结果可进一步用于推导 semiparametric efficiency bound 或构造 one-step 估计量。
- **关键技术**: `conditional Aalen-Johansen estimator`, `multi-state counting process`, `strong uniform consistency`, `asymptotic normality`, `landmark estimation`, `conditional Kaplan-Meier`
- **为什么对您有用**: 直接连接 causal inference 的 longitudinal / multi-state 设定，为条件状态占据概率提供非参数估计基础；用 technical_arsenal 中 moderately_familiar 的 semiparametric theory 可攻其 influence function 与 efficiency bound 的推导口子。中期可做：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，以将本文的渐近正态性结果推进到 semiparametric efficiency bound 与 debiased/one-step 估计。

### 4. [10.1111/sjos.12775](https://doi.org/10.1111/sjos.12775) · [arXiv](https://arxiv.org/abs/2305.17711) — A joint estimation approach for monotonic regression functions in general dimensions
- **作者**: Christian Rohrbeck, Deborah A. Costain
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 903-923
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究多维单调回归函数的联合估计问题，目标是在多个单调函数存在相似性时通过信息借用提升估计效率，设定涵盖固定与随机设计及任意维度回归变量。核心方法是对不同函数估计值之间的 pairwise differences 施加惩罚，惩罚权重由函数在某点等价的统计检验决定，随后通过迭代优化逐个更新函数估计直至收敛。理论性质方面，该方法在函数间确有相似性时能显著降低估计方差实现效率增益，而在函数间无相似性时因检验控制惩罚权重而不会过度平滑。模拟研究覆盖正态与二项响应数据，验证了上述自适应行为；实证分析应用于巴西新生儿死亡率与英格兰中风患者两套流行病学数据集。对您可能有用：该框架为非参数单调约束下的多函数联合估计提供了自适应 shrinkage 机制，直接连接非参数统计与流行病学应用。
- **关键技术**: `monotonic regression`, `penalized pairwise differences`, `equivalence test-based penalty weight`, `iterative optimization`, `information borrowing across functions`, `adaptive shrinkage`
- **为什么对您有用**: 本文连接非参数统计（primary）与流行病学数据集（secondary）：(1) 非参数单调回归的多函数联合估计与信息借用机制，属于非参数统计与半参数效率理论的交叉地带；(2) 您的 very_familiar 武器库中 minimax bounds 与 nonparametric statistics 可直接用来分析该 penalized estimator 的收敛率与效率界，判断其声称的效率增益是否达到 semiparametric efficiency bound；(3) **立即可做**：用 minimax bound 工具验证该惩罚估计在函数相似/不相似两种 regime 下的 rate 是否 sharp，并可探讨 equivalence test 控制惩罚权重的渐近性质。

### 5. [10.1111/sjos.12777](https://doi.org/10.1111/sjos.12777) — Statistical inference in the presence of imputed survey data through regression trees and random forests
- **作者**: Mehdi Dagdoug, Camelia Goga, David Haziza
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: McGill University · Centre National de la Recherche Scientifique · Université Marie et Louis Pasteur · University of Ottawa
- **分类**: vol 52 · issue 2 · pp 960-998
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 在调查抽样缺失数据插补设定下，目标是有限总体均值（finite population mean）的估计，关键假设为高维框架下预测变量数可发散及插补模型的一致性条件。本文研究回归树与随机森林作为非参数插补工具，在高维设定下给出了插补估计量的均方一致性（mean square consistency）条件。提出基于 K-fold 交叉验证的新方差估计器，以处理插补带来的额外变异。模拟评估了偏差、效率及正态置信区间覆盖率，并对随机森林超参数选择做了理论与实证分析。对您有用：本文将随机森林插补纳入高维非参数 M-estimation 理论框架，与您在 semiparametric theory 及 high-dimensional asymptotics 方向的兴趣直接相关。
- **关键技术**: `random forest imputation`, `mean square consistency`, `K-fold cross-validation variance estimation`, `high-dimensional diverging predictors`, `regression tree`, `survey sampling nonresponse`
- **为什么对您有用**: 本文连接到您 semiparametric / nonparametric theory 与 high-dimensional asymptotics 的子方向：它实质上是高维非参数回归（树/森林）在 survey sampling 中的 M-estimation 一致性与方差分析。用您 very_familiar 的高维渐近理论与 minimax bounds 工具，可以审视其一致性条件是否可进一步收紧至 minimax rate，或用 moderately_familiar 的 M-estimation theory 分析其方差估计器的 influence function 结构。Follow-up 判断：**立即可做**——用 very_familiar 的高维渐近工具即可检验其收敛率是否达到最优，并尝试用 HOIF 视角刻画插补估计量的 higher-order bias。

### 6. [10.1111/sjos.12769](https://doi.org/10.1111/sjos.12769) — Robust Composite Quantile Regression with Large‐scale Streaming Data Sets
- **作者**: Kangning Wang, Di Zhang, Xiaofei Sun
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Shandong Institute of Business and Technology
- **分类**: vol 52 · issue 2 · pp 736-755
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在 streaming data 设定下，目标是实现 composite quantile regression (CQR) 的在线估计，克服内存受限与 CQR 目标函数非光滑的双重挑战。作者首先对 CQR 目标函数构造光滑近似，随后提出基于新到达数据块的 online renewable CQR 算法，无需存储全部历史数据即可更新估计。理论上证明了该 renewable estimator 具有 oracle property，即其渐近分布与基于全样本的一次性估计等价，保证了估计效率与鲁棒性不因在线更新而损失。数值实验验证了方法的有效性。对您可能有用：该文的 streaming M-estimation 框架与 oracle property 证明路径，可迁移至因果推断中 longitudinal/sequential 数据的 online semiparametric estimation 问题。
- **关键技术**: `composite quantile regression`, `online renewable estimation`, `smooth approximation of non-smooth objective`, `oracle property`, `streaming data M-estimation`
- **为什么对您有用**: 本文连接到 semiparametric theory 与 statistical computing 两个子方向：renewable estimator 的 oracle property 证明本质上是 M-estimation theory 在 online/sequential 设定下的推广。用您 very_familiar 的 M-estimation theory 与 moderately_familiar 的 semiparametric theory，可以直接审视其 oracle property 的 regularity 条件是否可放宽或迁移到更一般的 semiparametric model（如 causal ATE 的 online one-step estimator）。**立即可做**：用熟悉的 M-estimation 工具检查其光滑近似引入的 bias 与 online updating 的 variance 之间的 trade-off 是否达到 semiparametric efficiency bound。

### 7. [10.1111/sjos.12766](https://doi.org/10.1111/sjos.12766) · [arXiv](https://arxiv.org/abs/2306.16075) — A comprehensive framework for evaluating time to event predictions using the restricted mean survival time
- **作者**: Ariane Cwiling, Vittorio Perduca, Olivier Bouaziz
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Université Paris Cité · Département mathématiques, informatique, sciences de la donnée et technologies du numérique · Mathématiques Appliquées à Paris 5
- **分类**: vol 52 · issue 2 · pp 658-690
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在右删失生存数据设定下，本文提出基于受限平均生存时间（RMST）的预测评估框架，目标 estimand 为 RMST 估计量的均方误差及全局/局部变量重要性。核心机制包括：用逆概率删失加权（IPCW）估计 RMST 估计量的 MSE；提出适用于右删失数据的 model-agnostic conformal prediction 算法以构建预测区间并评估局部变量重要性；开发 model-agnostic 统计检验以评估全局变量重要性。理论保证方面，框架对任何渐近收敛的 RMST 估计量均有效，且在模型误设下依然成立。对您可能有用：本文将 IPCW 与 conformal prediction 结合处理删失数据的思路，可为半参数理论中 influence function 构造及因果推断中 censored outcome 的 sensitivity 分析提供参考。
- **关键技术**: `restricted mean survival time (RMST)`, `inverse probability censoring weighting (IPCW)`, `conformal prediction for right-censored data`, `model-agnostic variable importance testing`, `asymptotic convergence under misspecification`
- **为什么对您有用**: 本文连接到半参数理论（IPCW 估计的渐近性质与模型误设下的鲁棒性）与流行病学应用（生存数据的预测评估）。研究者武器库中 very_familiar 的非参数统计与 moderately_familiar 的半参数理论可直接攻入 IPCW 估计量的 influence function 与渐近收敛分析口子，评估其是否达到 semiparametric efficiency bound。follow-up 粗判：立即可做——可用 M-estimation 理论与 HOIF 工具分析 IPCW-RMST 估计量的高阶渐近性质。

### 8. [10.1111/sjos.12778](https://doi.org/10.1111/sjos.12778) · [arXiv](https://arxiv.org/abs/2108.11551) — Adaptively robust small area estimation: Balancing robustness and efficiency of empirical bayes confidence intervals
- **作者**: Daisuke Kurisu, Takuya Ishihara, Shonosuke Sugasawa
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 999-1017
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在 Fay-Herriot 小区域估计的 Empirical Bayes 框架下，目标是当存在异常区域时，在 robustness 与 efficiency 之间自适应平衡以构建可靠的置信区间。核心方法是用 γ-divergence 替代边际 log-likelihood 进行估计，并通过优化控制 robustness 的 tuning parameter 来追求 EB 置区间的效率（覆盖率/长度）。理论贡献包括：在分布正确设定与存在异常区域两种情形下均建立了渐近理论，证明了方法在无异常时渐近有效、有异常时保持 robust。模拟与犯罪率数据应用验证了方法优势。对您可能有用：该文在 semiparametric/EB 框架下处理 robustness-efficiency tradeoff 的渐近分析思路，与您在 efficiency theory 和 M-estimation theory 中的兴趣直接相关。
- **关键技术**: `Empirical Bayes small area estimation`, `Fay-Herriot model`, `gamma-divergence minimization`, `robustness-efficiency tradeoff`, `asymptotic coverage of confidence intervals`, `M-estimation theory`
- **为什么对您有用**: 本文直接连接到您 primary interest 中的 efficiency theory（semiparametric efficiency bounds / asymptotic efficiency）以及 moderately_familiar 中的 M-estimation theory：γ-divergence 作为一种 robust M-estimator，其 tuning parameter 的选择以置信区间效率为准则，而非传统的纯估计偏差/方差，这一 criterion shift 对您思考 efficiency bound 在 robust 估计下的重新定义有启发。用您 very_familiar 的 minimax bounds 工具，可以尝试分析该 γ-divergence EB estimator 在异常比例已知时的 minimax risk，验证其声称的 adaptive efficiency 是否紧；这属于**立即可做**的 follow-up。

### 9. [10.1111/sjos.12773](https://doi.org/10.1111/sjos.12773) — Likelihood analysis of latent functional response regression models for sequences of correlated binary data
- **作者**: Fatemeh Asgari, Mohammad H. Alamatsaz, Saeed Hayati, Valeria Vitelli
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Oslo · University of Isfahan
- **分类**: vol 52 · issue 2 · pp 840-872
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究潜在函数响应回归模型，目标 estimand 为 Function-on-Scalar 回归系数与主成分，设定为潜在响应为可分 Hilbert 空间中的 Gaussian 随机元素，观测仅为不等间距的关联二值序列。核心方法是通过参数扩展（PX-EM）技术构建完全数据似然，并提出自适应 EM 算法实现最大似然估计，以处理缺失观测与不等间距问题。算法产出函数回归系数与主成分的平滑估计，收敛性质依赖 EM 的单调上升与 PX-EM 的加速收敛，但未给出 n^{-1/2}-CAN 或 semiparametric efficiency bound 的理论保证。实证通过模拟与真实数据验证，并提供 R 包 dfrr。对您而言，本文展示了 Hilbert 空间 Gaussian 过程先验下二值数据的 EM 计算框架，但缺乏您关注的 semiparametric efficiency 与 influence function 理论。
- **关键技术**: `functional data analysis`, `parameter expansion EM (PX-EM)`, `Function-on-Scalar regression`, `Gaussian process in separable Hilbert space`, `adaptive EM algorithm`, `dichotomized latent variable`
- **为什么对您有用**: 本文属于 functional data 与 latent variable 交叉的 semiparametric-like 模型，连接到您 primary interest 中的 semiparametric theory 子方向。您可用 technical_arsenal 中 moderately_familiar 的 M-estimation theory 分析该 EM 估计的渐近性质，补上目前缺失的 n^{-1/2}-CAN 与 efficiency bound 理论——这是一个**中期可做**的 follow-up，需先在 M-estimation 的非标准/缺失数据设定上长肌肉。若仅关注计算框架与 R 包实现，则属于 stat_computing 的入门级参考，但理论深度不足以支撑核心推进。

### 10. [10.1111/sjos.12780](https://doi.org/10.1111/sjos.12780) — Road traffic estimation and algorithmic routing in a spatially dependent network
- **作者**: Rens Kamphuis, Michel Mandjes, Paulo Serra
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Vrije Universiteit Amsterdam · University of Amsterdam
- **分类**: vol 52 · issue 2 · pp 1058-1091
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在空间依赖的道路网络中，目标是基于独立探测车辆的实测行程时间，估计各边行程时间的联合分布。设定允许边间存在一般的空间相关性，估计器基于非参数/半参数框架构造，证明了其一致性并达到 minimax rate-optimal 收敛速率。核心机制在于利用行程时间的空间依赖结构，在车辆行进中迭代更新剩余行程时间的预测分布（predictive distribution），从而实现动态路由。路由策略支持包含风险厌恶和估计不确定性在内的一般目标函数，数值实验系统评估了估计器与路由策略的组合表现。对您可能有用：本文的 minimax rate-optimal 估计与空间依赖下的迭代预测更新，为空间相关结构下的半参数效率理论提供了一个具体应用场景。
- **关键技术**: `minimax rate-optimal estimation`, `spatial dependence modeling`, `predictive distribution updating`, `dynamic routing policy`, `risk-averse objective function`
- **为什么对您有用**: 本文连接到 semiparametric & nonparametric theory 子方向，具体涉及空间依赖下的 minimax rate-optimal 估计。您武器库中 minimax bounds for estimation problems 可直接用来审视其声称的 rate-optimal 是否紧，以及空间相关结构是否改变了经典的效率界。follow-up 粗判：立即可做——用 very_familiar 的 minimax bound 工具验证其收敛速率的紧性，并可尝试用 higher-order U-statistics / HOIF 视角分析其估计器在空间依赖下的高阶修正潜力。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1111/sjos.12757](https://doi.org/10.1111/sjos.12757) — Optimal designs for testing pairwise differences: A graph‐based game theoretic approach
- **作者**: Arpan Singh, Satya Prakash Singh, Ori Davidov
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Indian Institute of Technology Hyderabad · Indian Institute of Technology Kanpur · University of Haifa
- **分类**: vol 52 · issue 2 · pp 533-571
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究在多重处理组比较实验中，如何最优分配样本以检验成对差异的假设。具体考虑两类科学问题：(1)是否存在某些处理对之间有差异；(2)是否所有指定处理对之间都有差异。作者采用图论建模，将处理组作为节点、需比较的配对作为边，构建一个基于博弈论的最大最小（max-min）最优设计框架。该框架将实验设计问题转化为零和博弈，求解博弈均衡得到最优分配方案。得到的部分设计是已知的（如完全随机化设计、平衡不完全区组设计），但此前未被识别为最大最小意义下的最优；另有一些设计是新颖的，在最小可检测差异（minimum detectable difference）意义上优于朴素设计。本文提供了显式的设计构造和最优性证明，并通过数值例子验证了其在最坏情况下的性能优势。对您而言，本文直接关联假设检验和实验设计的理论，可将其中最大最小最优性与您熟悉的半参数效率界（semiparametric efficiency bound）进行对比，以评估该设计框架在更一般设定下的最优性。
- **关键技术**: `Max-min optimal designs`, `Graph-based game theory`, `Pairwise hypothesis testing`, `Combinatorial designs`
- **为什么对您有用**: 本文直接关联您primary interest中的hypothesis testing子方向（检验成对处理差异），并引入图论-博弈框架优化实验设计。您可利用手头的minimax bounds工具（very_familiar）评估其设计的紧性，并与semiparametric efficiency bound（moderately_familiar）进行对比，属于中期可做：需先在semiparametric theory上进一步熟悉，方能将设计效率与半参数效率界联系起来。

### 2. [10.1111/sjos.12768](https://doi.org/10.1111/sjos.12768) · [arXiv](https://arxiv.org/abs/2306.13870) — Post‐selection inference for the Cox model with interval‐censored data
- **作者**: Jianrui Zhang, Chenxi Li, Haolei Weng
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 710-735
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在 Cox 比例风险模型下针对区间删失数据，研究 Lasso 模型选择后的 post-selection inference（PoSI）问题，目标是提供条件于选定模型的渐近有效 p 值与置信区间。核心方法构造了一个 pivotal quantity，并在局部参数（local parameters）设定下证明其收敛到均匀分布，从而绕过选择偏差导致的分布扭曲。为实现该 pivot，需要估计 efficient information matrix，文中提出多种估计途径并证明其一致性。模拟显示该方法在中等样本下表现良好，并以阿尔茨海默病数据作实证展示。对您可能有用：本文将 semiparametric efficient information 与 PoSI 结合，是 semiparametric efficiency theory 在 hypothesis testing / selective inference 中的具体应用案例。
- **关键技术**: `post-selection inference`, `Cox proportional hazards model`, `interval censoring`, `pivotal quantity`, `efficient information matrix`, `lasso selection`
- **为什么对您有用**: 本文直接连接到 primary interest 中的 hypothesis testing 与 semiparametric efficiency theory：efficient information matrix 的估计与一致性证明是 semiparametric efficiency bound 在区间删失 Cox 模型下的具体落地，而 pivotal quantity 的构造为 selective inference 提供了新的渐近框架。用您 very_familiar 的 minimax bounds / high-dimensional asymptotics 视角，可以审视其 local parameter 设定下的 pivot 收敛率是否紧；用 moderately_familiar 的 M-estimation theory，可以检查 efficient information matrix 估计的 M-estimator 收敛条件是否可进一步放松。Follow-up 粗判：中期可做——需先在 moderately_familiar 的 semiparametric theory 上长肌肉（特别是区间删失下 efficient influence function 的具体计算），才能将本文 pivot 方法推广到更一般的 semiparametric 模型或高维设定。

## 其他  *(other, 6 篇)*

### 1. [10.1111/sjos.12781](https://doi.org/10.1111/sjos.12781) — Ratio‐consistency of some invariant <i>U</i>‐statistic‐based estimators with an application to high‐dimensional data ranking
- **作者**: Jia Guo, Bu Zhou
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Zhejiang University of Technology · Zhejiang Gongshang University
- **分类**: vol 52 · issue 2 · pp 1092-1110
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文在U统计量框架下，针对协方差矩阵的某些函数（如特征值函数），提出一种系统构造无偏且满足旋转平移不变性的估计量的方法。这些估计量基于线性组合的U统计量，具有显式表达式和良好的不变性，适用于高维设定。作者利用U统计量方差公式，推导了所提出估计量达到比率一致性（ratio-consistency）的充分条件，即估计量依概率收敛于真实值的速率优于参数空间维数的影响。比率一致性在高维统计中尤为重要，可保证即使维数p随样本量n增长，估计量的相对误差仍可控。作为应用，文章提出了一种新的高维数据排序程序，利用这些不变估计量构建评分函数，并在模拟和实证中展示了有效性。该文深化了U统计量在协方差矩阵高维推断中的理论应用，其证明技术可迁移至更一般的U统计量组合估计问题，与您对higher-order U-statistics和高维统计的兴趣高度契合。
- **关键技术**: `U-statistics`, `ratio-consistency`, `invariant estimators`, `covariance matrix`, `high-dimensional ranking`
- **为什么对您有用**: 本文直接关联到您的主要兴趣——higher-order U-statistics，特别是利用U统计量的线性组合构造协方差矩阵函数的无偏估计并证明比率一致性。您非常熟悉的U统计量计算理论（如treewidth/张量收缩）可用于分析此类估计量的方差结构或计算效率，属于立即可做的方向。此外，高维数据排序应用与您的高维统计兴趣也有交集。

### 2. [10.1111/sjos.12771](https://doi.org/10.1111/sjos.12771) · [arXiv](https://arxiv.org/abs/2403.17882) — On the properties of distance covariance for categorical data: Robustness, sure screening, and approximate null distributions
- **作者**: Qingyang Zhang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 777-804
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对分类变量关联检验中Pearson卡方检验在稀疏大列联表统计功效低的问题，系统研究了距离协方差（distance covariance）的统计性质。作者证明距离协方差泛函对任意类别数（固定或发散）具有B-鲁棒性，而卡方检验不具备此性质。在变量筛选情景下，建立了距离协方差筛选的强相合性，模拟显示其在稀疏大表上显著优于卡方筛选。此外，推导了偏差校正距离相关估计的近似零分布，可用于构造快速近似检验以避免昂贵的置换操作。理论贡献包括鲁棒性、相合性以及近似分布，通过模拟和GSS数据验证。对您而言，本文直接关联假设检验和高阶U统计量（距离协方差估计本质上是U统计量），您的U统计量计算专长（treewidth/einsum）可用于分析其计算效率，筛选思路可拓展至高维分类数据的变量选择。
- **关键技术**: `distance covariance`, `U-statistic permutation test`, `B-robustness`, `sure screening`, `categorical contingency tables`, `approximate null distribution`
- **为什么对您有用**: 本文核心连接您的假设检验与高阶U统计量兴趣子方向：分类数据独立性检验的U统计量方法。您的very_familiar武器库中'高阶U统计量计算（treewidth/einsum）'可直接用于分析该U统计量估计的计算代价或优化收缩策略，属于立即可做的工作。此外，筛选的相合性结果可用于高维分类变量选择，与您的高维统计兴趣对接。

### 3. [10.1111/sjos.12764](https://doi.org/10.1111/sjos.12764) · [arXiv](https://arxiv.org/abs/2208.04779) — Weighted reduced rank estimators under cointegration rank uncertainty
- **作者**: Christian Holberg, Susanne Ditlevsen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 595-630
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究协整分析中秩误设对降秩回归估计量的影响。协整分析通常先估计协整秩，然后基于估计秩进行降秩回归，但渐近性质通常在秩已知的假设下推导。作者量化了当秩被错误设定时协整向量的渐近偏差，并推导出其渐近分布。针对秩选择困难的情形，提出了一类加权降秩估计器，通过对不同秩的估计量加权平均来减少秩不确定性带来的风险。实证结果表明，适当选择权重可以在秩不确定时提高预测准确性。最后，该估计器被应用于视觉处理实验中记录的EEG数据。本文主要贡献在于处理了秩选择不确定性，但方法本身属于经典时间序列框架，与您的主要研究方向（因果推断、高维统计、U统计量等）关联较弱，可作为拓宽视野的参考文献。
- **关键技术**: `cointegration analysis`, `reduced rank regression`, `weighted estimators`, `rank misspecification`, `asymptotic distribution`
- **为什么对您有用**: 本文属于时间序列计量经济学，与您的主要兴趣方向（因果推断、高维统计、U统计量）没有直接交集。尽管协整中的降秩回归与低秩矩阵估计存在概念上的相似性，但本文未涉及高维设定或现代非渐近理论。您的技术武器库中缺少时间序列协整的核心工具（VAR模型、Johansen检验），因此此文暂不可做直接的技术对接。如果您未来想拓展至经济时间序列的因果分析（如格兰杰因果），则可作为预备阅读。

### 4. [10.1111/sjos.12765](https://doi.org/10.1111/sjos.12765) · [arXiv](https://arxiv.org/abs/2003.12200) — Enriched Pitman–Yor processes
- **作者**: Tommaso Rigon, Sonia Petrone, Bruno Scarpa
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 631-657
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 论文提出了一种称为 enriched Pitman–Yor 过程的离散非参数先验，用于处理嵌套聚类结构。该先验扩展了 enriched Dirichlet 过程，并建立了与归一化随机测度的正式联系。作者给出了 square-breaking 表示，推导了后验分布和 urn 方案的闭式表达式。证明了许多现有模型（如 spike-and-slab 基测度的 Dirichlet 过程、混合模型族）是该先验的特例，从而提供了统一的贝叶斯非参数框架。最后通过一个物种抽样生态学问题展示了实际应用。对您而言，本文主要涉及贝叶斯非参数领域，与您关注的因果推断、半参效率理论等方向无直接交集，但非参数先验构造思路可作为理解离散先验灵活性的参考。
- **关键技术**: `Pitman–Yor process`, `square-breaking representation`, `urn scheme`, `normalized random measures`, `enriched Dirichlet process`
- **为什么对您有用**: 本文属于贝叶斯非参数领域，与您的主要兴趣（因果推断、高维统计、U统计量、半参效率、统计计算权衡）无直接对应。但该文提出的 enriched Pitman–Yor 过程作为统一框架，可视为对离散先验理论的一个扩充；如果您未来在因果推断中需要灵活的先验处理（如异质性建模），该文提供的 square-breaking 表示和 urn 方案可能提供一种实现思路。不过，目前您的技术武器库中缺少贝叶斯非参数工具的深入经验（如 Dirichlet 过程后验性质），因此该文暂不属于立即可做的范畴，但可作为入门阅读拓展视野。

### 5. [10.1111/sjos.12763](https://doi.org/10.1111/sjos.12763) — Graph neural networks for the localization of faults in a partially observed regional transmission system
- **作者**: Mantautas Rimkus, Piotr Kokoszka, Dongliang Duan, Xuao Wang, Haonan Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Colorado State University · University of Wyoming
- **分类**: vol 52 · issue 2 · pp 572-594
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文针对部分观测的输电系统中故障定位这一工程问题，提出结合回归图神经网络与统计方法的解决方案。其核心贡献在于，所构建的网络无需使用包含故障位置信息的标签数据进行训练，即可实现故障定位。方法上，作者将图神经网络作为非线性特征提取器，再通过统计建模（如回归框架）进行位置推断，形成深度学习和统计的协同框架。实验验证表明，该联合方法优于单独使用深度学习或传统统计方法。从方法学角度看，本文创新主要在于工程应用层面的训练策略（无标签训练），而非基础统计理论或推断方法的突破。本文与您的主要研究兴趣（因果推断、高维统计、随机矩阵、U-统计、半参效率、计算统计权衡）无直接重叠，属于电力系统监测的专门应用。
- **关键技术**: `regression graph neural networks`, `fault localization`, `partially observed systems`, `statistical-deep learning synergy`, `unsupervised training for localization`
- **为什么对您有用**: 本文属于工程领域的应用统计工作，与您核心兴趣方向（因果推断、高维、U-统计、效率理论等）无直接关联。您武器库中的工具（非参统计、高维渐近、软件开发）不直接适用于图神经网络框架，且本文未涉及统计计算权衡或高阶U-统计等您熟悉的计算模型。**暂不可做**：当前武器库缺乏图神经网络和电力系统建模的领域知识，无法将本文方法有效迁移到您的研究问题中。

### 6. [10.1111/sjos.12726](https://doi.org/10.1111/sjos.12726) — Issue Information
- **作者**: 
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2
- 相关性 0/10 · novelty: `minor`
- **摘要**: 该条目为《Scandinavian Journal of Statistics》第52卷第2期的期刊信息页（Issue Information），并非研究论文。内容仅为Wiley出版社关于ESG（环境、社会、治理）的一般性声明，不包含任何统计、方法学或应用方面的学术贡献。因此，与研究者所有兴趣方向皆无关。
- **为什么对您有用**: 完全不相关。该条目是期刊卷首信息，无学术内容，不值得阅读。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

