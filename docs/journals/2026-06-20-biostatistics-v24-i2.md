# Biostatistics — Vol 24  Issue 2  ·  2026-06-20

- 共 19 篇 · Biostatistics
- 目录核对 ✅ 19 篇全部抓到（对照 OpenAlex 19 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期聚焦因果推断与半参数方法的交叉应用，同时涵盖流行病学中的复杂数据建模、高维特征选择及临床试验设计。论文可归为四条主线：**因果识别与效率理论**（5篇，涉及IV生存、聚类随机试验TMLE、泛化性分数、纵向缺失的贝叶斯半参数、外部模型整合的元推断）、**非参数/半参数建模**（3篇：多水平函数型PCA、双变量分位数变系数模型、生存费用轨迹的张量积脊估计）、**流行病学中因果-预测融合**（1篇集成框架及数篇癌症预后/风险预测应用）、**假设检验与计算**（选择性推断、遗传算法特征选择、贝叶斯剂量寻找等）。其中因果与半参数效率主线最为密集，且多篇以删失数据或聚类设计为背景。

**因果识别与效率理论**是该期的方法核心。Doubly robust nonparametric IV for survival outcomes 在删失生存结局下将双稳健IV估计扩展到LATE识别，基于有效影响函数构建，可嵌入机器学习；Two-Stage TMLE 将靶向最小损失估计推广至聚类随机试验，通过两步更新同时处理缺失和协变量不平衡，具备双鲁棒性；A generalizability score 从协变量分布差异角度提出一个诊断工具，辅助效应泛化时的子群体选择，但未给出渐近理论；A meta-inference framework 整合多个外部模型的信息到当前研究，通过加权复合经验贝叶斯提高效率，且允许协变量集不一致，理论上优于纯内部估计。这四篇共同推进了因果推断中效率与稳健性的边界，且处理的数据结构（删失、聚类、泛化、外部信息整合）较为多样。

**非参数/半参数建模**方面，Interpretable PCA for multilevel multivariate functional data 通过凸优化结合粗糙度惩罚和稀疏性惩罚分解多水平函数型数据，适用于脑电或影像数据；Bivariate quantile varying coefficient model 用B样条和ADMM估计两个神经影像指标随空间位置的联合变化，属于多变量分位数回归的扩展；Statistical modeling of longitudinal medical cost trajectory 采用张量积离散化和有效脊惩罚估计费用-生存二元曲面，处理删失和死亡事件。这些方法在灵活性和可解释性之间取得平衡，且均涉及高维或结构化数据。

与因果推断、半参数效率最密切的论文包括：Doubly robust nonparametric IV for survival outcomes、Two-Stage TMLE、A generalizability score、A meta-inference framework。适合优先阅读。非参数半参数方向可关注 Interpretable PCA for multilevel multivariate functional data 和 Bivariate quantile varying coefficient model。假设检验方向的 Selective inference for calcium spikes 展示了选择性推断在神经科学中的应用思路。

## 因果推断  *(causal_inference, 4 篇)*

### 1. [10.1093/biostatistics/kxab036](https://doi.org/10.1093/biostatistics/kxab036) · [arXiv](https://arxiv.org/abs/2007.12973) — Doubly robust nonparametric instrumental variable estimators for survival outcomes
- **作者**: Youjin Lee, Edward H Kennedy, Nandita Mitra
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 518-537
- 相关性 10/10 · novelty: `new_method`
- **摘要**: 本文在工具变量（IV）框架下，针对删失生存结局，研究局部平均处理效应（LATE）对生存概率的识别与估计。作者提出非参数估计器，适用于协变量依赖删失和结局依赖删失两种机制，基于有效影响函数（EIF）构建，并给出相应的简单估计程序。该估计器具有双稳健性，即只要倾向得分或条件生存函数之一正确指定，即可保证一致性；同时可灵活嵌入机器学习方法进行非参数估计。模拟研究验证了不同删失场景下估计器的灵活性与双稳健性。真实数据应用来自前列腺、肺、结直肠和卵巢癌筛查试验（PLCO），估计筛查对生存概率的因果效应，并比较不同删失假设下的因果对比。对您有用的是：该工作将 IV 方法与删失生存数据结合，直接连接您的因果推断（特别是 IV）和半参效率理论兴趣；其 EIF 推导与双稳健结构可使用您的非参统计和 M-估计理论武器进行解读或扩展。
- **关键技术**: `efficient influence function`, `doubly robust estimation`, `instrumental variable`, `local average treatment effect`, `nonparametric estimation with machine learning`, `survival analysis with censoring`
- **为什么对您有用**: (1) 连接因果推断中的 IV 方法在删失生存结局这一实际场景的扩展，属于您 primary_interests 的 IV 子方向。 (2) 可用您非常熟悉的非参统计和估计理论（very_familiar）对其 EIF 的推导和双稳健性质进行验证或改进，无需额外武器。 (3) 立即可做：您现有的非参统计和因果推断基础足以理解并批判该方法的效率与鲁棒性；后续可考虑将该框架推广到更复杂的因果参数或敏感性分析。

### 2. [10.1093/biostatistics/kxab043](https://doi.org/10.1093/biostatistics/kxab043) · [arXiv](https://arxiv.org/abs/2106.15737) — Two-Stage TMLE to reduce bias and improve efficiency in cluster randomized trials
- **作者**: Laura B Balzer, Mark van der Laan, James Ayieko, Moses Kamya, Gabriel Chamie, Joshua Schwab et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 502-517
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 针对聚类随机试验（CRT）中个体结局缺失和基线协变量不平衡导致估计偏倚和效率损失的问题，提出了两阶段靶向最小损失估计（two-stage TMLE）。该方法首先控制基线及后基线缺失机制，然后自适应调整基线协变量以优化精度。模拟研究表明，相比现有CRT估计量，该估计能几乎消除因结局差异测量导致的偏倚。应用到SEARCH社区随机试验数据，展示了在控制个体水平结局缺失后对基线协变量进行自适应调整带来的效率增益。该方法基于半参数效率理论和双鲁棒性质，通过两步靶向更新实现偏差纠正。对您有用：本文直接将效率理论（TMLE）扩展到CRT这一常见因果推断设计，与您的因果推断/半参数理论兴趣高度匹配；您熟悉的causal inference estimation理论可以快速理解其核心步骤，属于立即可做的阅读。
- **关键技术**: `Targeted Minimum Loss-based Estimation (TMLE)`, `two-stage TMLE`, `double robust estimation`, `adaptive covariate adjustment`, `cluster randomized trials`, `semiparametric efficiency`
- **为什么对您有用**: 直接连接您的primary interest中的因果推断（CRT是纵向/群组因果设计）和效率理论（TMLE源于半参数效率界）。您very_familiar中的'estimation theory in causal inference'足以理解该估计量的双鲁棒和靶向步骤，属于立即可做的阅读。

### 3. [10.1093/biostatistics/kxab029](https://doi.org/10.1093/biostatistics/kxab029) · [arXiv](https://arxiv.org/abs/2106.14243) — A generalizability score for aggregate causal effect
- **作者**: Rui Chen, Guanhua Chen, Menggang Yu
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 309-326
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在因果效应异质性下，将平均处理效应从源群体泛化到目标群体时，协变量分布差异导致重加权或回归方法方差大甚至不可靠。作者提出泛化性分数（generalizability score）作为选择目标子群体的准则，旨在识别与源群体协变量分布更接近的目标子集以降低泛化误差。该分数的简化版避免使用结局信息，可防止无意接触结局导致的认知偏差。模拟和两个实际数据分析表明，该分数能有效筛选出泛化更稳健的目标子群体。该方法为泛化问题提供了可操作的工具，但未给出分数的渐近性质或最优性理论。对您有用：直接关联因果推断中的外推/泛化问题，可用于流行病学或经济学中效应泛化前的子群体诊断。
- **关键技术**: `generalizability score`, `target subpopulation selection`, `covariate overlap`, `reweighting estimator`, `outcome-free score`
- **为什么对您有用**: 本文直接关联因果推断中的泛化外推子方向，是研究者‘estimation theory in causal inference’可立即应用的问题；可借助 minimax bounds 为该分数在有限重叠下的最优子群体选择提供理论保证，属于‘立即可做’的 follow-up。

### 4. [10.1093/biostatistics/kxab012](https://doi.org/10.1093/biostatistics/kxab012) — A Bayesian semiparametric approach for inference on the population partly conditional mean from longitudinal data with dropout
- **作者**: Maria Josefsson, Michael J Daniels, Sara Pudas
- **期刊/来源**: Biostatistics
- **机构**: Umeå University · University of Florida
- **分类**: vol 24 · issue 2 · pp 372-387
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对纵向数据中因选择性入组和脱落导致的非代表性样本问题，提出一种估计总体部分条件均值（population partly conditional mean）的贝叶斯半参数方法。该estimand定义为给定存活至特定时间点的结局变量的有限总体均值，可用于概括记忆轨迹等纵向目标。方法基于贝叶斯预测框架，利用总体层面的纵向辅助信息构建灵活的半参数模型，不依赖参数分布假设。通过敏感性分析评估不可检验假设（如缺失机制、实践效应）对结果的影响，并与逆概率加权等现有方法进行模拟比较。应用在15年Betula纵向队列研究中估计情节记忆的生命周期轨迹，展示了从非代表性样本向目标总体推广的全流程。这对于因果推断中长期随访研究的transportability问题具有直接参考价值。
- **关键技术**: `Bayesian semiparametric predictive estimator`, `population partly conditional mean`, `dropout`, `sensitivity analysis`, `longitudinal data`, `predictive inference`
- **为什么对您有用**: 本文属于纵向数据缺失机制下的总体推断，与您primary interest中因果推断的longitudinal方向直接相关。其识别假设和敏感性分析框架可被您moderately_familiar的identification theory in causal inference工具所剖析——例如评估其忽略的缺失机制假设是否可被proximal causal inference放松。中期可做：需要先强化semiparametric贝叶斯建模（目前不在武器库中），但迁移部分条件均值的识别思路本身就是高价值习题。

## 非参数 / 半参数  *(nonparam_semipara, 2 篇)*

### 1. [10.1093/biostatistics/kxab018](https://doi.org/10.1093/biostatistics/kxab018) · [arXiv](https://arxiv.org/abs/1909.08024) — Interpretable principal component analysis for multilevel multivariate functional data
- **作者**: Jun Zhang, Greg J Siegle, Tao Sun, Wendy D’andrea, Robert T Krafty
- **期刊/来源**: Biostatistics
- **机构**: University of Pittsburgh
- **分类**: vol 24 · issue 2 · pp 227-243
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在 multilevel multivariate functional data 设定下，目标是分解总变异为 subject-level 与 within-subject-level（电极级）变异，并进行可解释的主成分分析。核心机制是对传统 functional PCA 施加 roughness penalty 保证平滑性，并通过创新的 rank-one convex optimization 结合 block Frobenius penalty 与 matrix L1-norm penalty，实现跨变量（频段）的稀疏性与时间域的局部支撑。估计问题被转化为带结构性惩罚的凸优化，无需非凸迭代即可获得 sparse & smooth 的 loadings。实证应用于创伤与解离症状的 EEG 数据，揭示了 subject- 与 electrode-level 脑活动的新神经生理关联。对您可能有用：该文的 multilevel 分解与结构性 convex penalty 设计，为 semiparametric / nonparametric 理论中的 structured M-estimation 提供了一个具体案例。
- **关键技术**: `multilevel functional PCA`, `block Frobenius norm penalty`, `matrix L1-norm penalty`, `rank-one convex optimization`, `roughness penalty for smoothness`, `structured M-estimation`
- **为什么对您有用**: 本文连接到 nonparametric statistics 与 M-estimation theory 子方向，其 rank-one convex optimization 与结构性惩罚的设计可被视为 structured penalized M-estimator 的具体实例。您武器库中 moderately_familiar 的 M-estimation theory 可直接攻入其惩罚项的收敛率与 oracle property 理论缺口（原文偏算法与应用，理论分析较薄）。中期可做：需先在 moderately_familiar 的 M-estimation theory 上长肌肉，推导带 block Frobenius + L1 双重惩罚下的 minimax rate 与 sparsity recovery 界。

### 2. [10.1093/biostatistics/kxab031](https://doi.org/10.1093/biostatistics/kxab031) — Estimation for the bivariate quantile varying coefficient model with application to diffusion tensor imaging data analysis
- **作者**: Matthew Pietrosanu, Haoxu Shu, Bei Jiang, Linglong Kong, Giseon Heo, Qianchuan He et al.
- **期刊/来源**: Biostatistics
- **机构**: University of Alberta · Fred Hutch Cancer Center · University of North Carolina at Chapel Hill
- **分类**: vol 24 · issue 2 · pp 465-480
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 该论文提出双变量分位数变系数模型（bivariate quantile varying coefficient model），用于联合建模两个功能性神经影像指标（如扩散张量成像中的分数各向异性和平均扩散率）随域（如脑区位置）和协变量（如胎龄、性别）的变化。估计方法基于交替方向乘子法（ADMM）和传播分离算法，采用B样条基展开并施加L2光滑惩罚以增强可解释性。模拟研究和真实神经发育数据集展示了模型在刻画双变量功能响应上的灵活性和临床洞察力。该方法拓展了经典变系数模型至多变量分位数回归框架，属于半参数建模的范畴。对您而言，本文的B样条估计和惩罚正则化技巧可与非参数统计理论中的收敛率分析技术连接，您熟悉的非参数工具可用于推导其渐近性质。
- **关键技术**: `varying coefficient model`, `quantile regression`, `bivariate functional response`, `alternating direction method of multipliers`, `B-spline basis`, `L2 smoothness penalty`
- **为什么对您有用**: 本文属于半参数/非参数建模在神经影像中的应用，可直接连接至您primary interest中的非参数统计与半参数理论；您武器库中已熟悉的非参数估计和minimax bound技术可用于分析该B样条估计的收敛速率。目前可立即可做：用已有的非参数工具推导其一致性及最优收敛率，但需注意本文是方法论文，无严格的渐近理论，因此您的研究工作可填补这一空白。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1093/biostatistics/kxab017](https://doi.org/10.1093/biostatistics/kxab017) · [arXiv](https://arxiv.org/abs/2010.09971) — A meta-inference framework to integrate multiple external models into a current study
- **作者**: Tian Gu, Jeremy M G Taylor, Bhramar Mukherjee
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 406-424
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对内部数据集规模有限但存在多个外部模型提供的摘要信息的问题，提出一个元推断框架以整合外部信息。框架包含两个加权估计量，均为复合经验贝叶斯估计量，可处理外部模型使用不完全相同协变量集的情况。方法能自动识别最相关的外部信息并减弱不兼容信息的影响，通过平衡偏差-方差权衡来最大化效率增益。理论证明了所提估计量比单纯使用内部数据的估计量更高效，也优于其他朴素组合。模拟和实际数据验证了方法的稳健性和效率优势。该工作与效率理论及半参数估计紧密相关，可应用于因果推断中的外部信息整合（如运输性分析），也值得用M估计理论或minimax界进一步验证其最优性。
- **关键技术**: `meta-inference framework`, `weighted empirical Bayes estimator`, `composite estimator`, `bias-variance trade-off`, `external information integration`
- **为什么对您有用**: 直接连接到效率理论与半参数估计的兴趣子方向，特别是利用外部信息提升内部推断效率的问题。技术库中的“M估计理论”可立即用于分析该框架估计量的渐近性质和正则性条件，而“minimax界”可用于检验其效率增益是否达到理论最优。粗判：立即可做——核心分析工具已熟悉。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1093/biostatistics/kxab034](https://doi.org/10.1093/biostatistics/kxab034) · [arXiv](https://arxiv.org/abs/2103.07818) — Quantifying uncertainty in spikes estimated from calcium imaging data
- **作者**: Yiqun T Chen, Sean W Jewell, Daniela M Witten
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 481-501
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究钙成像数据中神经元尖峰估计的不确定性量化问题，在指数衰减钙信号模型下，检验特定时间点是否发生尖峰（即钙瞬时增加）。经典假设检验因使用同一数据估计尖峰和检验而膨胀第一类错误。作者提出选择性推断方法，在给定观测数据和尖峰估计结果的前提下计算条件p值和置信区间，控制选择性第一类错误。算法高效，能给出有限样本精确p值。模拟和spikefinder数据集上的实证表明方法有效控制错误率。对您可能有用：本文展示了选择性推断在神经科学数据分析中的应用，与您的假设检验兴趣直接相关，且其条件推断思路可迁移至因果推断中的后选择推断问题。
- **关键技术**: `selective inference`, `finite-sample p-values`, `conditional testing`, `spike detection`, `calcium imaging`
- **为什么对您有用**: 本文聚焦选择性推断这一统计假设检验的前沿方法，直接呼应您对hypothesis testing的兴趣。您very_familiar的'nonparametric statistics'武器可用于评估模型假设的稳健性，'software development'武器可用于复现并扩展算法至其他时序结构（如因果推断中的纵向数据）。立即可做：武器库中已有假设检验和算法开发基础，可直接复现并尝试推广至更一般的信号检测问题。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1093/biostatistics/kxab022](https://doi.org/10.1093/biostatistics/kxab022) — Feature selection for support vector regression using a genetic algorithm
- **作者**: Shannon B McKearnan, David M Vock, G Elisabeta Marai, Guadalupe Canahuate, Clifton D Fuller, Julian Wolfson
- **期刊/来源**: Biostatistics
- **机构**: University of Minnesota · University of Illinois Chicago · University of Iowa · The University of Texas MD Anderson Cancer Center
- **分类**: vol 24 · issue 2 · pp 295-308
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文针对支持向量回归（SVR）在高维特征下易过拟合的问题，提出一种基于遗传算法的特征选择方法。该方法将特征子集编码为染色体，通过交叉、变异等遗传操作迭代优化用户定义的适应度函数（如交叉验证预测误差），从而选出最优特征集。在模拟研究中，与LASSO、随机森林（RF）及全变量SVR进行了系统比较：所提方法在非线性关系下优于LASSO，在特征相关时优于RF，在部分线性场景下与RF表现相当。应用于UNOS肾移植数据库，预测术后1年肾功能，展示实际预测性能改善。本文属于预测建模方法的应用研究，未涉及因果识别或半参效率理论，但提供了一个可复现的GA-SVR特征选择流程，其flexible fitness函数设计思路可迁移至其他预测任务。
- **关键技术**: `genetic algorithm`, `support vector regression`, `feature subset selection`, `LASSO`, `random forest`, `cross-validation based fitness`
- **为什么对您有用**: 本文属于统计计算与预测建模的交叉应用，与您的`statistical computing`兴趣（数值方法/算法）直接对应。您的`very_familiar`武器库中的`software development`和`nonparametric statistics`可快速复现或扩展该GA-SVR流程（如改用更高效的适应度函数或并行化）。但本文方法学贡献有限，遗传算法特征选择并非新颖理论，且不涉及您核心关注的因果识别、半参效率或高维收敛速率，因此**暂不可做**有深度的方法延拓，仅可作为入门级案例阅读。

## 流行病学  *(epidemiology, 7 篇)*

### 1. [10.1093/biostatistics/kxab047](https://doi.org/10.1093/biostatistics/kxab047) · [arXiv](https://arxiv.org/abs/2010.11330) — Integrated causal-predictive machine learning models for tropical cyclone epidemiology
- **作者**: Rachel C Nethery, Nina Katz-Christy, Marianthi-Anna Kioumourtzoglou, Robbie M Parks, Andrea Schumacher, G Brooke Anderson
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 449-464
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文在热带气旋流行病学领域提出一个集成因果-预测机器学习框架，目标是在高空间分辨率下量化气旋对健康的即时影响（全因死亡率和心血管/呼吸系统住院率），并识别异质性模式和关键风险因素。框架包括两个部分：因果推断组件用于估计历史气旋的因果效应，预测组件用于捕获气旋气象特征及社区社会经济特征如何与健康影响关联。作者将其应用于包含详细气旋暴露信息和Medicare受助者健康记录的丰富数据平台。主要实证结果发现历史气旋的健康影响存在高度异质性，气旋持续风速是死亡率和呼吸系统风险的主要驱动因素。本文是流行病学中因果推断与机器学习相结合的应用典范，对研究者的次要兴趣——流行病学应用（特别是因果推断在环境健康中的应用）具有直接参考价值。
- **关键技术**: `Causal-predictive machine learning`, `Heterogeneous health impact estimation`, `Medicare claims analysis`, `Spatial exposure assessment`
- **为什么对您有用**: 该论文属于流行病学应用方向，清晰展示了因果推断和机器学习在环境健康问题中的整合方式，作为进入这一领域的入门读物可读性强。研究者掌握的因果推断估计理论和非参数方法足以理解并评估其识别策略与估计量，因此值得全文阅读。

### 2. [10.1093/biostatistics/kxab024](https://doi.org/10.1093/biostatistics/kxab024) — Statistical modeling of longitudinal medical cost trajectory: renal cell cancer care cost analyses
- **作者**: Shikun Wang, Yu Shen, Ya-Chen Tina Shih, Ying Xu, Liang Li
- **期刊/来源**: Biostatistics
- **机构**: The University of Texas MD Anderson Cancer Center
- **分类**: vol 24 · issue 2 · pp 244-261
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对纵向医疗费用数据，在存在死亡事件和右删失的背景下，估计癌症患者从确诊开始的费用轨迹。目标参数是给定生存时间的条件平均费用轨迹，构成一个二元曲面。作者提出两阶段半参数方法：第一阶段联合建模纵向费用和生存时间，第二阶段用测量时间和生存时间的张量积离散化以及有效脊惩罚来估计费用-生存二元曲面。该方法在模型灵活性、统计效率和计算可行性之间取得平衡。利用SEER-Medicare数据库估计肾细胞癌患者的费用轨迹，展示了实际应用。该文的联合建模和正则化张量积估计技术，与您对纵向数据建模和半参数方法的关注点直接相关，可作为流行病学应用方向的一个实例参考。
- **关键技术**: `two-stage semiparametric approach`, `joint modeling of longitudinal cost and survival`, `tensor product of discretized time and survival`, `ridge penalty`, `bivariate surface estimation`
- **为什么对您有用**: 本文属于流行病学应用方向（secondary interest），涉及纵向医疗成本数据建模，与您对流行病学数据集和应用因果工作的兴趣吻合。您可以用very_familiar中的非参数统计和minimax bounds来评估该半参数估计量的光滑性假设与收敛率，或用moderately_familiar中的半参数理论分析其效率。这项工作是立即可做的——您已有的工具足以理解并可能批判其理论性质。

### 3. [10.1093/biostatistics/kxab038](https://doi.org/10.1093/biostatistics/kxab038) — Bayesian finite mixture of regression analysis for cancer based on histopathological imaging–environment interactions
- **作者**: Yunju Im, Yuan Huang, Aixin Tan, Shuangge Ma
- **期刊/来源**: Biostatistics
- **机构**: Yale University · University of Iowa
- **分类**: vol 24 · issue 2 · pp 425-442
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对癌症异质性分析，提出一种贝叶斯有限混合回归（FMR）模型，整合低维临床/环境变量与高维组织病理学图像特征及其交互作用。现有FMR研究多基于临床/组学数据，本文首次将高维图像特征与环境交互纳入FMR框架，以更好地刻画癌症表型与协变量之间的异质性关联。方法上，采用贝叶斯变量选择机制，通过层次性先验强制满足“主效应先于交互作用”的结构，在高维设定下实现信号筛选与噪声剔除。开发了基于马尔可夫链蒙特卡洛（MCMC）的高效计算算法，模拟实验表明该方法在变量选择和参数估计上优于现有方法。在TCGA肺鳞癌数据分析中，识别出若干与影像特征和环境因素交互作用相关的亚组，揭示了传统方法忽略的异质性模式。对您而言，这是一篇流行病学应用中处理高维交互作用与异质性的典型工作，您可利用熟悉的高维渐近工具评估其估计量的相合性，或借鉴其变量选择框架到因果推断中的子组分析。
- **关键技术**: `Finite mixture of regression`, `Bayesian variable selection with hierarchy`, `High-dimensional interaction analysis`, `Histopathological image feature extraction`, `MCMC algorithm`
- **为什么对您有用**: 本文属于流行病学应用中的高维交互分析与异质性建模，直接对应您的次要兴趣（流行病学数据集与模型）。您武器库中的 high-dimensional asymptotics 可用于分析该贝叶斯方法的变量选择相合性，而 semiparametric theory 中的识别概念可为混合回归的隐变量结构提供另一种理论视角。**中期可做**：建议先熟悉 Bayesian variable selection 的基本收敛结果（属 moderately_familiar 的 M-estimation 范畴），再考虑将类似层次性交互选择框架迁移至 causal mediation 或 IV 设定。

### 4. [10.1093/biostatistics/kxab009](https://doi.org/10.1093/biostatistics/kxab009) — Prognosis of cancer survivors: estimation based on differential equations
- **作者**: Pål C Ryalen, Bjørn Møller, Christoffer H Laache, Mats J Stensrud, Kjetil Røysland
- **期刊/来源**: Biostatistics
- **机构**: University of Oslo · Cancer Registry of Norway · École Polytechnique Fédérale de Lausanne
- **分类**: vol 24 · issue 2 · pp 345-357
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文聚焦癌症幸存者的预后参数估计问题，目标是在累积风险函数驱动的微分方程框架下构建通用估计量。作者利用微分方程的解表达预后参数，从而将估计问题转化为对累积风险函数的积分。他们开发了易于用标准统计软件实现的plug-in型估计量，并显式给出了几种常用预后参数的估计公式，其中部分参数据作者所知此前未被用于预后评估。方法的核心在于将微分方程与Aalen型加性风险模型或Cox模型估计的累积风险结合，通过数值积分获得参数估计。最后，作者将所提方法应用于挪威五种常见癌症（如结直肠癌、乳腺癌等）的登记数据，评估长期预后指标。本文对您（陈星宇）的二级兴趣——流行病学应用——是一次直接的数据分析展示，其中微分方程驱动的估计策略与您擅长的非参数统计和估计理论可以衔接，作为进入流行病学方向的应用型入门读物值得一读。
- **关键技术**: `differential equations driven by cumulative hazards`, `plug-in estimation`, `Aalen-type additive hazard model`, `survival prognosis parameters`, `cancer registry data analysis`
- **为什么对您有用**: 本文直接对应您的二级兴趣——流行病学中的应用统计，特别是癌症生存数据分析中的预后估计。您武器库中的非参数统计和估计理论（如累积风险函数的性质、一致估计量的构造）足以理解本文估计量的理论基础，并可在此基础上思考更高效的估计或敏感性分析。作为流行病学方向的入门应用型论文，本文立即可读，无需额外补充工具。

### 5. [10.1093/biostatistics/kxab032](https://doi.org/10.1093/biostatistics/kxab032) — Predicting the onset of breast cancer using mammogram imaging data with irregular boundary
- **作者**: Shu Jiang, Jiguo Cao, Graham A Colditz, Bernard Rosner
- **期刊/来源**: Biostatistics
- **机构**: Washington University in St. Louis · Simon Fraser University · Brigham and Women's Hospital · Harvard University
- **分类**: vol 24 · issue 2 · pp 358-371
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对乳腺X线图像中存在不规则边界的问题，提出了一种有监督的函数型主成分分析（sFPCA over triangulations）方法，用于提取与失效时间结局相关的图像特征以改进乳腺癌风险预测。方法利用三角剖分上的二元样条拟合图像数据，处理不规则区域。通过特征值分解算法实现高效计算。与传统的无监督FPCA相比，该方法在模拟研究中得到更低的Brier分数和更高的AUC。应用于Stieman癌症中心的Joanne Knight Breast Health Cohort数据，结果显示优于无监督FPCA及其他基准模型，并揭示了图像中的重要风险模式。对您而言，该工作展示了一种非参数降维方法在流行病学风险预测中的应用，与您的非参数统计和流行病学次级兴趣相匹配，但因果推断成分较弱，可作为流行病学数据集的参考。
- **关键技术**: `supervised functional principal component analysis (sFPCA)`, `triangulation-based bivariate splines`, `eigenvalue decomposition`, `Brier score`, `AUC`
- **为什么对您有用**: 本文属于流行病学应用（乳腺癌风险预测），使用函数型数据分析（FPCA）处理图像数据，与您对流行病学（数据集、应用）的次要兴趣直接相关。方法学上涉及非参数降维（三角剖分样条），可视为半参数/非参数方法论的一个具体案例。但该文不涉及因果推断或效率理论，属于温和的方法学贡献。作为流行病学实例，值得了解其数据预处理和预测建模流程。

### 6. [10.1093/biostatistics/kxab028](https://doi.org/10.1093/biostatistics/kxab028) — Bayesian adaptive model selection design for optimal biological dose finding in phase I/II clinical trials
- **作者**: Ruitao Lin, Guosheng Yin, Haolun Shi
- **期刊/来源**: Biostatistics
- **机构**: The University of Texas MD Anderson Cancer Center · University of Hong Kong · Simon Fraser University
- **分类**: vol 24 · issue 2 · pp 277-294
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 该文针对phase I/II临床试验中最佳生物学剂量（OBD）的确定问题，提出一种贝叶斯自适应模型选择设计。同时纳入毒性（toxicity）和疗效（efficacy）两种结局，不施加任何参数假设或形状约束，采用curve-free模型对剂量-反应曲线进行建模。通过综合所有剂量水平的观测数据，设计实现剂量分配的相干性，从而提升剂量选择效率与准确性。与现有phase I/II设计相比，该设计具有理想的相干性性质，并允许处理免疫治疗中常见的延迟结局。通过广泛模拟验证了其稳健性能，并以一个phase I/II临床试验为例说明应用。该设计提供了一种灵活且无需参数假设的剂量寻找新框架。
- **关键技术**: `Bayesian model selection`, `adaptive design`, `curve-free model`, `toxicity-efficacy joint modeling`, `coherence property`
- **为什么对您有用**: 本文属于流行病学/临床试验应用领域，连接研究者secondary interest中的流行病学应用方向。其中curve-free模型实质上是一种非参数建模策略，研究者非常熟悉的非参数统计可以解析其灵活性。但由于核心算法依赖贝叶斯MCMC，不在研究者当前技术武库中（缺少贝叶斯计算经验），因此暂不可直接利用；建议作为领域知识了解。

### 7. [10.1093/biostatistics/kxab027](https://doi.org/10.1093/biostatistics/kxab027) — Bayesian multiregional clinical trials using model averaging
- **作者**: Nathan W Bean, Joseph G Ibrahim, Matthew A Psioda
- **期刊/来源**: Biostatistics
- **机构**: University of North Carolina at Chapel Hill
- **分类**: vol 24 · issue 2 · pp 262-276
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对多区域临床试验（MRCT）中区域样本量小导致区域特异性治疗效果估计精度差的问题，提出一种基于贝叶斯模型平均的推断方法。该方法通过后验模型概率加权固定效应和随机效应模型，能够同时估计区域特异性和全球治疗效应，并可纳入患者协变量。后验模型概率还可作为跨区域治疗效应一致性的量化证据，辅助监管决策。模拟研究表明，与固定效应线性回归相比，所提方法均方误差更低；与贝叶斯分层模型相比，I型错误控制更优。该方法为多区域试验中的区域效应估计提供了新工具，与您关注的流行病学临床试验设计中的统计推断问题直接相关，但其贝叶斯框架与您常用的频率学派半参数方法不同，可作为方法学参考。
- **关键技术**: `Bayesian model averaging`, `posterior model probabilities`, `fixed-effects linear regression`, `hierarchical model`, `type I error control`, `multiregional clinical trials`
- **为什么对您有用**: 本文属于流行病学领域中的临床试验方法学，与您次要兴趣中的流行病学应用直接相关。您可以用 estimation theory in causal inference 中的效率评估框架审视其 MSE 与现有因果方法（如分层估计）的比较，但该方法本身不涉及因果识别。follow-up 粗判：暂不可做，因为贝叶斯模型平均和 MCMC 工具不在您当前武器库中，需补充贝叶斯计算能力才能深入。

## 其他  *(other, 3 篇)*

### 1. [10.1093/biostatistics/kxab040](https://doi.org/10.1093/biostatistics/kxab040) — Historical controls in clinical trials: a note on linking Pocock’s model with the robust mixture priors
- **作者**: Andrea Callegaro, Nicholas Galwey, Juan J Abellan
- **期刊/来源**: Biostatistics
- **机构**: GlaxoSmithKline (Belgium)
- **分类**: vol 24 · issue 2 · pp 443-448
- 相关性 4/10 · novelty: `minor`
- **摘要**: 本文在临床试验历史对照信息借用设定下，研究 Pocock 偏差-方差模型与 robust mixture priors (RMP) 的理论联系。核心 estimand 为新试验与对照组的参数差异，关键假设为历史数据与当前数据可能存在系统性偏差。作者证明 Pocock 模型中的偏差参数与 RMP 中的两个关键设定——先验权重 w（新试验与历史试验存在系统性差异的概率）与模糊成分方差 s_v^2——存在等价映射关系，不同 (w, s_v^2) 组合可表达相同的先验信念。据此建议固定 s_v^2（例如令模糊成分"等价于一个受试者"的信息量），从而将先验信念的调节简化为单一参数 w 的选择。该结果为贝叶斯历史对照借用提供了参数选择的实用指南，对您在因果推断中处理外部对照数据或先验敏感性分析有参考价值。
- ⚠️ *摘要不完整，待重跑（`python -m research_news.rerun`）*
- **关键技术**: `robust mixture priors`, `Pocock's bias-variance model`, `commensurate prior`, `historical control borrowing`, `prior variance calibration`
- **为什么对您有用**: 本文连接到因果推断中外部对照/历史数据借用的先验建模子方向，但核心是贝叶斯先验参数的等价性分析而非 semiparametric/效率理论。您的 technical_arsenal 中 identification theory in causal inference 可用于审视历史对照可借用性的 identification 条件（如不可混淆假设的跨期稳定性），但本文未触及此层面。follow-up 判断：**暂不可做**——本文属于贝叶斯先验参数校准的专门讨论，缺乏您熟悉的 minimax/semiparametric/influence function 工器可切入的理论口子，且不涉及高维或效率界问题，仅作为应用参考阅读即可。

### 2. [10.1093/biostatistics/kxab013](https://doi.org/10.1093/biostatistics/kxab013) — ACTOR: a latent Dirichlet model to compare expressed isoform proportions to a reference panel
- **作者**: Sean D McCabe, Andrew B Nobel, Michael I Love
- **期刊/来源**: Biostatistics
- **机构**: University of North Carolina at Chapel Hill
- **分类**: vol 24 · issue 2 · pp 388-405
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文提出ACTOR模型（一种潜在狄利克雷模型），用于将目标数据集的异构体表达比例与外部参考面板进行比较。模型假设每个基因的异构体计数服从Dirichlet-Multinomial分布，组别归属通过潜在变量建模。采用变分贝叶斯（variational Bayes）推断后验分布，估计样本的组别概率。以GTEx为参考面板，在模拟和真实RNA-seq数据上评估了组织类型分类性能。模型以R包形式发布（提供完整实现与文档）。核心贡献在于将经典的潜在狄利克雷分配（LDA）框架适配到异构体比例比较这一特定生物问题，并利用公共参考数据实现分类。对您而言，本文是统计建模与软件开发的完整案例，展示了变分推断在分层计数数据中的应用，对您的统计计算（软件开发）兴趣有直接参考价值。
- **关键技术**: `latent Dirichlet model`, `Dirichlet Multinomial`, `variational Bayes`, `RNA-seq isoform analysis`, `reference panel comparison`
- **为什么对您有用**: 本文属于生物统计应用，与您的因果推断、高维统计等核心兴趣无直接重叠，但其潜变量建模和变分推断技术是统计计算的典型范例，且提供了完整R包实现（可直接审视代码结构）。您的软件开发经验可评估其实现效率；若未来将类似分层模型用于因果推断中的测量误差或多群体比较，也有潜在迁移价值。整体上，本文可作为了解生物统计应用领域的入门读物，对核心研究方向的直接启示有限。

### 3. [10.1093/biostatistics/kxaa055](https://doi.org/10.1093/biostatistics/kxaa055) · [arXiv](https://arxiv.org/abs/2007.01680) — Developing a predictive signature for two trial endpoints using the cross-validated risk scores method
- **作者**: Svetlana Cherlin, James M S Wason
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 2 · pp 327-344
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 该文将交叉验证风险评分（CVRS）设计从单结局扩展至双结局（CVRS2），用于从高维协变量中识别对两个疗效终点均有获益的敏感患者亚组。方法上，先对每个患者计算双变量风险评分，再通过非参数聚类将患者分为不同群组。基于模拟数据评估了CVRS2的识别能力，并在一项随机精神科临床试验中进行了实证，其中基线协变量数以百计，两个结局为罪犯状态和物质使用状态。结果显示CVRS2能可靠识别出两个结局均显著受益的敏感组，而原始CVRS仅在一个结局上显著。文章主要贡献在于提供了一种实用性强的多终点亚组识别工具，但方法学创新有限。对您而言，这篇论文涉及高维协变量下的亚组划分，与您在高维统计和因果推断中对异质性处理的兴趣有间接关联。
- **关键技术**: `cross-validated risk scores`, `bivariate clustering`, `high-dimensional covariates`, `subgroup identification`, `randomized clinical trial`
- **为什么对您有用**: (1) 本文涉及高维协变量下的敏感亚组识别，可视为因果推断中treatment effect heterogeneity的辅助方法，但并非直接因果识别。(2) 武器库中的'high-dimensional asymptotics'和'nonparametric statistics（非参数聚类）'可用于理解该方法的重现性和最优性，但该文的聚类程序分析空间不大。(3) 暂不可做——该文属于Biostatistics应用型方法，不涉及研究者武器的直接攻口；若要深入，需先熟悉临床试验设计文献（非武器库项）。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

