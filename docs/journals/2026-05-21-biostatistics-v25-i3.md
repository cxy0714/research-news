# Biostatistics — Vol 25  Issue 3  ·  2026-05-21

- 共 19 篇 · Biostatistics

## 因果推断  *(causal_inference, 7 篇)*

### 1. [10.1093/biostatistics/kxad037](https://doi.org/10.1093/biostatistics/kxad037) — DP2LM: leveraging deep learning approach for estimation and hypothesis testing on mediation effects with high-dimensional mediators and complex confounders
- **作者**: Shuoyang Wang, Yuan Huang
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 3 · pp 818-832
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在高维中介变量与非线性混杂的因果中介分析设定下，目标是直接效应（direct effect）和间接效应（indirect effect）的估计与假设检验，采用部分线性中介模型框架。DP2LM 将深度神经网络用于拟合混杂的非线性效应（非参数部分），同时对高维中介变量施加惩罚部分线性模型（参数部分），实现了混杂灵活调整与高维中介降维的统一。与多数聚焦中介变量选择的工作不同，本文优先关注中介效应本身的估计与推断，构造了直接效应和间接效应的检验程序，理论上证明了检验的 Type-I error rate 渐近控制。模拟显示在大量中介变量场景下估计与推断性能优于现有方法；实证应用于 DNA 甲基化对皮质醇压力反应性的中介效应分析。该工作对您有用：在中介分析（您 primary interest 的 mediation 子方向）中结合了半参数部分线性模型与高维惩罚，并给出假设检验的理论保证，框架可迁移至纵向中介或敏感性分析设定。
- **关键技术**: `penalized partially linear model`, `deep neural network for nonparametric confounding`, `mediation effect hypothesis testing`, `high-dimensional mediator penalization`, `Type-I error rate control`
- **为什么对您有用**: 直接命中您 primary interest 的 mediation 子方向，同时涉及半参数部分线性模型、高维惩罚与假设检验三个子方向；方法框架可迁移至纵向中介或敏感性分析，实证数据集（DNA 甲基化 + 流行病学队列）对 epidemiology secondary interest 也有参考价值。

### 2. [10.1093/biostatistics/kxad038](https://doi.org/10.1093/biostatistics/kxad038) — A Bayesian nonparametric approach for multiple mediators with applications in mental health studies
- **作者**: Samrat Roy, Michael J Daniels, Jason Roy
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 3 · pp 919-932
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在多重中介的因果推断设定下，目标是在存在中介间交互作用时识别与估计联合及个体中介效应，现有参数方法易受模型误设影响且常忽略中介交互。本文提出一种贝叶斯非参数方法，利用三层 enriched Dirichlet process mixture (EDPM) 灵活建模观测数据（结局、多中介、处理、混杂）的联合分布。通过 g-computation (standardization) 计算所有可能的中介效应，包括两两及高阶交互效应，避免了将联合效应简单等同于个体效应之和的强假设。模拟与实证（Wisconsin Longitudinal Study 的心理健康数据，CES-D）表明该方法能有效识别显著的个体与成对中介效应。对您有用：该文将 EDPM 引入多中介分析，为处理中介交互与模型误设提供了贝叶斯非参数视角，其 g-computation 框架与流行病学队列数据应用对您的中介分析与因果应用方向有直接参考价值。
- **关键技术**: `multiple mediators`, `Bayesian nonparametrics`, `enriched Dirichlet process mixture`, `g-computation`, `mediation interaction effects`
- **为什么对您有用**: 直接关联您的主兴趣 causal inference (mediation) 与 nonparametric theory，以及副兴趣 epidemiology (datasets, applied causal)；EDPM 结合 g-computation 的框架为处理多中介交互与模型误设提供了非参数解法，且附带了流行病学真实数据集分析流程。

### 3. [10.1093/biostatistics/kxad032](https://doi.org/10.1093/biostatistics/kxad032) — Scalable kernel balancing weights in a nationwide observational study of hospital profit status and heart attack outcomes
- **作者**: Kwangho Kim, Bijan A Niknam, José R Zubizarreta
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 3 · pp 736-753
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在观察性研究的因果推断设定下，传统平衡权重方法在大规模数据中难以对再生核希尔伯特空间（RKHS）的广义基函数进行灵活平衡。本文提出一种可扩展的核平衡权重方法，将 RKHS 基扩展与凸优化技术结合。具体而言，利用降秩 Nyström 方法在近线性时空复杂度内高效计算核基，并采用一阶交替方向乘子法（ADMM）快速求解最小化权重散度的最优平衡权重。模拟研究表明该方法在精度和速度上显著优于现有方法。实证部分在 127 万患者的心脏病发作与医院盈利状态关系的流行病学数据中验证了其可扩展性。对您有用：该方法将 RKHS 非参数理论与统计计算（Nyström 降秩、ADMM）深度结合，为大规模因果推断提供了可迁移的计算框架，且其流行病学数据集对应用因果工作有参考价值。
- **关键技术**: `kernel balancing weights`, `reproducing kernel Hilbert space (RKHS)`, `rank-restricted Nyström method`, `alternating direction method of multipliers (ADMM)`, `covariate balancing`
- **为什么对您有用**: 该文将 RKHS 非参数平衡与数值优化（Nyström 降秩、ADMM）结合，直接契合您在因果推断估计、非参数理论与统计计算上的交叉兴趣；同时 127 万患者的流行病学应用为医疗因果推断提供了真实数据集参考。

### 4. [10.1093/biostatistics/kxad030](https://doi.org/10.1093/biostatistics/kxad030) — A Bayesian multivariate factor analysis model for causal inference using time-series observational data on mixed outcomes
- **作者**: Pantelis Samartsidis, Shaun R Seaman, Abbie Harrison, Angelos Alexopoulos, Gareth J Hughes, Christopher Rawlinson et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 3 · pp 867-884
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在多单元、多结果的纵向观察性时间序列数据设定下，目标是估计干预效应，假设潜在因子结构捕获了结果间的依赖性与未观测混杂。提出一种贝叶斯多变量因子分析模型，通过联合建模受干预影响的混合类型结果（连续、二项、计数）来提高因果效应估计的效率。核心计算挑战在于高维且不可解析的后验分布，作者开发了高效的 MCMC 算法进行采样，从而自然实现因果估计算子的不确定性量化。实证部分评估了英格兰 COVID-19 测试与追踪计划中 Local Tracing Partnerships 的干预效果。对您可能有用：该文提供了流行病学时间序列因果推断的应用范例，其处理混合类型结果联合建模提升效率的思路，以及高维后验 MCMC 采样算法，对纵向因果推断与统计计算子方向有参考价值。
- **关键技术**: `Bayesian factor analysis`, `time-series causal inference`, `mixed-type outcomes`, `Markov chain Monte Carlo (MCMC)`, `joint modeling for efficiency`
- **为什么对您有用**: 该文属于流行病学（secondary interest）中的纵向因果推断应用，其联合建模混合类型结果以提升效率的思路及高维 MCMC 采样算法，对您在纵向因果推断与统计计算方向的方法开发有迁移价值。

### 5. [10.1093/biostatistics/kxad024](https://doi.org/10.1093/biostatistics/kxad024) — Semi-supervised mixture multi-source exchangeability model for leveraging real-world data in clinical trials
- **作者**: Lillian M F Haine, Thomas A Murry, Raquel Nahra, Giota Touloumi, Eduardo Fernández-Cruz, Kathy Petoumenos et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 3 · pp 617-632
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在 RCT 借用外部真实世界数据（RWD）的设定下，目标是提升亚组分析的效率，关键假设是外部数据与试验数据在修正倾向得分上的可交换性。方法提出两步贝叶斯框架 SS-MIX MEM：第一步用半监督混合模型对修正倾向得分建模，识别试验人群中的代表性子群；第二步用多源可交换性模型（MEM）在结局差异大时自动停止借用，从而在测量与未测量协变量不一致时控制偏差。模拟显示，当试验与 RWD 一致时借用效率高，不一致时偏差显著低于竞争方法。实证分析将方法用于流感住院患者静脉免疫球蛋白 RCT，借用外部观察研究数据补充流感亚型分析。对您而言，修正倾向得分识别代表性子群的思路与 proximal CI 中 negative control 设定下识别可交换子群有结构相似性，MEM 的自适应借用逻辑也可迁移到纵向因果推断中多源数据融合的场景。
- **关键技术**: `modified propensity score`, `semi-supervised mixture model`, `multisource exchangeability model`, `Bayesian dynamic borrowing`, `real-world data integration`
- **为什么对您有用**: 修正倾向得分识别代表性子群的思路与 proximal CI 的 negative control 识别策略有结构相似性；MEM 自适应借用机制可迁移到因果推断中多源数据融合与敏感性分析的设定，同时实证部分提供了流行病学 RCT 数据集参考。

### 6. [10.1093/biostatistics/kxad021](https://doi.org/10.1093/biostatistics/kxad021) — An intersectional framework for counterfactual fairness in risk prediction
- **作者**: Solvejg Wastvedt, Jared D Huling, Julian Wolfson
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 3 · pp 702-717
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在临床风险预测与治疗分配的设定下，针对现有算法公平性方法忽略交叉群体及预测引导治疗带来的统计偏差（如碰撞偏倚），本文提出基于反事实因果框架的交叉不公平性度量。作者构建了完整的估计与推断框架，包括衡量不公平相对极端程度的 u-value。为处理非标准渐近性质，推断部分采用替代标准 bootstrap 的方法计算标准误与置信区间。理论上明确了在治疗分配受预测结果影响时，传统公平性指标失效的因果机制。实证部分将该方法应用于美国中西部医疗系统的 COVID-19 风险预测数据。对您可能有用：该文将反事实因果推断与公平性结合，处理了预测影响治疗分配时的统计偏差，其非标准 bootstrap 推断工具及真实流行病学数据集对您的因果推断与流行病学应用兴趣有参考价值。
- **关键技术**: `counterfactual fairness`, `intersectional bias metrics`, `collider bias adjustment`, `non-standard bootstrap inference`, `u-value extremity measure`
- **为什么对您有用**: 将反事实因果推断引入算法公平性，处理了预测引导治疗时的碰撞偏倚问题，其非标准 bootstrap 推断工具和真实流行病学（COVID-19）数据集对您的因果推断应用与流行病学兴趣有直接参考价值。

### 7. [10.1093/biostatistics/kxad022](https://doi.org/10.1093/biostatistics/kxad022) — Variable selection in high dimensions for discrete-outcome individualized treatment rules: Reducing severity of depression symptoms
- **作者**: Erica E M Moodie, Zeyu Bian, Janie Coulombe, Yi Lian, Archer Y Yang, Susan M Shortreed
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 3 · pp 633-647
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维设定下针对二值结局构建个体化治疗规则（ITR），目标是在非线性链接函数下实现因果效应估计与变量选择。作者采用加权且带惩罚的估计方程，结合新的计算算法求解近期提出的双重稳健（DR）正则化估计方程。该方法在实现高维变量选择的同时，保持了双重稳健性，即只要倾向得分或结局模型之一正确指定，估计即一致。理论与模拟证明了该方法的变量选择有效性与双重稳健性质，并在 Kaiser Permanente Washington 的抑郁症治疗数据上进行了实证分析。对您有用：该文将双重稳健与高维惩罚估计结合，直接关联您的主兴趣（因果推断中的高维变量选择与 DR 估计）及次兴趣（流行病学数据集的因果应用）。
- **关键技术**: `individualized treatment rules`, `doubly robust estimation`, `regularized estimating equation`, `high-dimensional variable selection`, `penalized weighted estimation`
- **为什么对您有用**: 直接关联您的主兴趣因果推断（高维 ITR 估计与双重稳健性）与次兴趣流行病学（抑郁症治疗真实数据应用），展示了 DR 正则化估计方程在二值结局因果问题中的计算与理论处理。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1093/biostatistics/kxad034](https://doi.org/10.1093/biostatistics/kxad034) — Covariate-guided Bayesian mixture of spline experts for the analysis of multivariate high-density longitudinal data
- **作者**: Haoyi Fu, Lu Tang, Ori Rosen, Alison E Hipwell, Theodore J Huppert, Robert T Krafty
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 3 · pp 666-680
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对多变量高密度纵向数据（如脑成像）的异质性问题，提出基于协变量引导的贝叶斯样条混合专家模型进行轨迹聚类。设定中假设每个多变量纵向轨迹为多个平滑样条成分的混合，时间独立协变量通过混合专家模型的 logistic 权重与混合成分关联。推断在完全贝叶斯框架下利用 Gibbs 抽样完成，并以 DIC 准则选择混合成分数量。模拟与 fNIRS 婴儿情绪反应实证分析揭示了不同的脑活动模式及其与协变量的关联。对您而言，该文展示了平滑样条在纵向异质数据中的非参数建模及贝叶斯计算方案，其混合专家结构可为纵向因果推断中处理异质性混淆或潜在类别提供参考。
- **关键技术**: `Bayesian mixture of experts`, `smoothing splines`, `multivariate high-density longitudinal data`, `Gibbs sampling`, `deviance information criterion`
- **为什么对您有用**: 涉及纵向数据的非参数样条建模与贝叶斯计算，虽非因果推断或效率理论，但其对异质性轨迹的混合建模思路可为纵向因果推断中处理异质性混淆或潜在类别提供方法借鉴。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1093/biostatistics/kxad026](https://doi.org/10.1093/biostatistics/kxad026) — Improved fMRI-based pain prediction using Bayesian group-wise functional registration
- **作者**: Guoqing Wang, Abhirup Datta, Martin A Lindquist
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 3 · pp 885-903
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在 fMRI 个体间功能定位差异导致预测特征错位的设定下，本文提出贝叶斯群组功能配准方法，目标是将个体功能数据空间变换至公共潜在模板。方法基于广义贝叶斯框架，利用对称群组配准损失函数实现具有逆向一致性的概率配准；潜在模板采用高斯过程（GP）建模以捕捉空间特征并提升估计精度。模拟与热痛 fMRI 实证表明该配准方法显著提升了疼痛评分的预测精度。对您而言，本文展示了 GP 先验与广义贝叶斯在空间变换计算中的具体实现，可为统计计算与半/非参数建模提供应用层面的算法参考。
- **关键技术**: `Bayesian group-wise registration`, `Gaussian process prior`, `generalized Bayes framework`, `inverse-consistent transformation`, `spatial functional alignment`
- **为什么对您有用**: 涉及高斯过程先验（非参数理论）与广义贝叶斯计算（统计计算），虽然核心是神经影像配准而非纯理论推进，但其计算框架和 GP 建模思路对统计计算与半/非参数方向有应用层面的参考价值。

### 2. [10.1093/biostatistics/kxad012](https://doi.org/10.1093/biostatistics/kxad012) — A scalable approach for continuous time Markov models with covariates
- **作者**: Farhad Hatami, Alex Ocampo, Gordon Graham, Thomas E Nichols, Habib Ganjgahi
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 3 · pp 681-701
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在带协变量的连续时间马尔可夫模型(CTMM)设定下，现有方法因每个观测需单独计算矩阵指数而面临 O(n·p³) 级计算瓶颈。本文提出将 Padé 近似用于矩阵指数的自动微分，并结合随机梯度下降(SGD)进行优化，使大规模数据拟合可行。标准误计算方面，给出两种方法：基于 Padé 展开的新方法，以及基于矩阵指数幂级数展开的方法，均避免了重复矩阵指数运算。模拟显示相比现有 CTMM 方法在计算效率上有数量级提升，并在多发性硬化症大规模数据集 NO.MS 上进行了实证演示。对您有用：直接关联您 statistical computing 中对 matrix 数值方法与算法的兴趣，Padé 近似求导矩阵指数的技巧可迁移至其他涉及矩阵指数的模型（如连续时间生存/马尔可夫决策）的计算场景。
- **关键技术**: `matrix exponential differentiation`, `Padé approximation`, `stochastic gradient descent`, `power series expansion`, `continuous time Markov model`
- **为什么对您有用**: 直接命中 primary interest 中 statistical computing 的 matrix 数值方法方向；Padé 近似求导矩阵指数的方案对其他涉及矩阵指数的半参数/纵向模型计算有迁移价值，NO.MS 数据集也可作为流行病学应用的参考。

## 流行病学  *(epidemiology, 4 篇)*

### 1. [10.1093/biostatistics/kxad028](https://doi.org/10.1093/biostatistics/kxad028) — Joint modeling in presence of informative censoring on the retrospective time scale with application to palliative care research
- **作者**: Quran Wu, Michael Daniels, Areej El-Jawahri, Marie Bakitas, Zhigang Li
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 3 · pp 754-768
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在回顾性时间尺度（距死亡时间）下，本文旨在解决纵向生活质量与生存数据联合建模中的信息性删失问题，核心假设是删失、生存与纵向过程通过共享随机效应关联。方法采用线性混合效应模型刻画纵向轨迹，竞争风险模型刻画死亡与删失时间，三者共享随机效应以消除信息性删失导致的偏倚。模拟与真实姑息治疗数据表明，相较于忽略信息性删失的现有方法，该模型能提供无偏的参数估计。对您而言，该文提供了一个处理纵向数据信息性删失的真实数据集与应用范式，可作为将更高级的半参数或因果推断方法（如边际结构模型）引入姑息治疗研究的切入点。
- **关键技术**: `joint modeling`, `informative censoring`, `shared random effects`, `competing risks model`, `linear mixed effects model`, `retrospective time scale`
- **为什么对您有用**: 符合您在流行病学（secondary interest）中的应用与数据集需求；其对纵向数据信息性删失的处理框架，可为您在纵向因果推断（primary interest）中引入半参数效率理论或敏感性分析提供现实数据与应用场景。

### 2. [10.1093/biostatistics/kxad027](https://doi.org/10.1093/biostatistics/kxad027) — A Bayesian nonparametric approach to correct for underreporting in count data
- **作者**: Serena Arima, Silvia Polettini, Giuseppe Pasculli, Loreto Gesualdo, Francesco Pesce, Deni-Aldo Procaccini
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 3 · pp 904-918
- 相关性 0/10 · novelty: `application`
- **摘要**: 针对流行病学计数数据的低报问题，提出非参数复合泊松模型，设定真实计数服从泊松分布且报告概率具有潜在聚类结构。采用贝叶斯非参数方法引入报告概率的潜在聚类，结合专家先验与报告过程的代理变量进行参数估计。利用MCMC进行后验推断，在模拟及真实数据上与现有方法比较，证明在部分数据质量信息可用时估计更准确。实证分析了意大利阿普利亚258个市镇的慢性肾病患病率及巴西早期新生儿死亡率。对您而言，该文提供了处理流行病学低报数据的贝叶斯非参数视角和多源登记数据集，但缺乏您关注的频率学派半参数效率或因果推断框架。
- **关键技术**: `Bayesian nonparametrics`, `compound Poisson model`, `latent clustering`, `underreporting correction`, `MCMC posterior inference`
- **为什么对您有用**: 涉及流行病学应用和真实多源登记数据集（慢性肾病、新生儿死亡率），且使用了非参数模型处理低报问题；但方法为贝叶斯非参数，与您关注的频率学派半参数效率/因果推断关联较弱，主要价值在于数据集和低报建模思路借鉴。

### 3. [10.1093/biostatistics/kxad020](https://doi.org/10.1093/biostatistics/kxad020) — An integrative latent class model of heterogeneous data modalities for diagnosing kidney obstruction
- **作者**: Jeong Hoon Jang, Changgee Chang, Amita K Manatunga, Andrew T Taylor, Qi Long
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 3 · pp 769-785
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文针对肾梗阻诊断中缺乏金标准且数据模态异质（renogram曲线、序数专家评分、药代动力学变量、人口学信息）的问题，提出一种整合潜类别模型。模型将梗阻状态视为潜类别，针对不同数据模态构建三个子模型：多水平函数潜因子回归处理renogram曲线，probit scalar-on-function回归处理序数评分，高斯混合模型处理标量变量。推断采用高效的MCMC算法进行参数估计与潜类别预测，并提供不确定性量化。仿真和Emory肾研究数据应用表明该模型作为计算机辅助诊断工具的有效性。虽然方法偏向贝叶斯潜类别而非您关注的半参数效率或因果推断，但其处理无金标准（潜类别）和异质数据模态的建模思路对流行病学应用中的测量误差或潜变量因果推断有参考价值。
- **关键技术**: `integrative latent class model`, `multilevel functional latent factor regression`, `probit scalar-on-function regression`, `Gaussian mixture model`, `Markov chain Monte Carlo`
- **为什么对您有用**: 本文属于流行病学临床诊断应用，提供了Emory肾研究的真实异质数据集；其处理无金标准诊断（潜类别）和函数型数据的建模框架，对您在流行病学因果推断中处理测量误差或潜变量设定有参考价值。

### 4. [10.1093/biostatistics/kxad013](https://doi.org/10.1093/biostatistics/kxad013) — Multivariate spatiotemporal functional principal component analysis for modeling hospitalization and mortality rates in the dialysis population
- **作者**: Qi Qian, Danh V Nguyen, Donatello Telesca, Esra Kurum, Connie M Rhee, Sudipto Banerjee et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 3 · pp 718-735
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文针对透析患者住院率与死亡率的时空联合建模问题，提出多元时空函数型主成分分析（MFPCA）模型，基于美国肾脏数据系统（USRDS）进行分析。方法核心基于多元 Karhunen-Loève 展开提取时间维度的主变异方向，并通过区域特异性得分引入空间相关性。估计程序仅需单变量主成分分解结合 MCMC 框架推断空间相关结构，避免了直接处理高维交叉协方差矩阵的计算瓶颈。实证分析揭示了美国透析人群高住院率/死亡率的时空热点及高风险时段。对您而言，该文提供了流行病学队列（USRDS）的时空数据结构范例，其函数型 PCA 与 MCMC 结合的计算策略可迁移至纵向因果推断中的潜变量或时空混杂建模。
- **关键技术**: `multivariate functional PCA`, `Karhunen-Loève expansion`, `spatiotemporal modeling`, `Markov Chain Monte Carlo`, `USRDS dataset`
- **为什么对您有用**: 属于流行病学应用，提供了 USRDS 透析人群的时空数据集范例；其函数型 PCA 与 MCMC 的计算策略对您在纵向因果推断中的潜变量或时空混杂调整具有方法迁移价值。

## 其他  *(other, 5 篇)*

### 1. [10.1093/biostatistics/kxad036](https://doi.org/10.1093/biostatistics/kxad036) — Uncertainty directed factorial clinical trials
- **作者**: Gopal Kotecha, Steffen Ventz, Sandra Fortini, Lorenzo Trippa
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 3 · pp 833-851
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在因子临床试验（factorial clinical trials）设定下，目标是估计干预效应、发现协同作用或识别最优治疗组合，传统设计采用平衡随机化而忽略试验具体目标。本文提出一类基于贝叶斯决策论的响应自适应随机化设计，针对二值结局，根据累积数据动态调整各治疗组合的分配概率。核心机制为：研究者指定反映试验目标的效用函数，自适应算法以最大化该效用函数为导向更新随机化概率；文中构造了多种效用函数及对应的因子设计，并研究了所提自适应设计的渐近行为。模拟比较了不同设计的关键操作特征（如选择概率、效应估计精度），并利用三项真实因子试验（围手术期、戒烟、传染病预防）的数据摘要构建仿真场景展示优势。对您而言，该文的贝叶斯决策论框架与自适应随机化渐近分析与您在效率理论和统计计算方面的兴趣有方法层面交叉，但核心贡献在试验设计而非因果识别或半参数估计。
- **关键技术**: `Bayesian decision-theoretic design`, `response-adaptive randomization`, `utility function optimization`, `asymptotic properties of adaptive designs`, `factorial trial operating characteristics`
- **为什么对您有用**: 与您在效率理论（效用函数下的最优分配渐近性）和统计计算（自适应随机化算法）的兴趣有方法交叉，但属于试验设计方向，对因果推断或半参数理论的直接推进有限。

### 2. [10.1093/biostatistics/kxad010](https://doi.org/10.1093/biostatistics/kxad010) — Quantification and statistical modeling of droplet-based single-nucleus RNA-sequencing data
- **作者**: Albert Kuo, Kasper D Hansen, Stephanie C Hicks
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 3 · pp 801-817
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文研究 droplet-based 单核 RNA-seq (snRNA-seq) 数据是否与单细胞 RNA-seq 数据服从相同概率分布，核心问题是零膨胀假设与负二项分布的适用性。利用小鼠皮层（10x Chromium）和肾脏（DropSeq）的伪阴性对照数据，作者发现 snRNA-seq 计数服从负二项分布而非零膨胀，表明 scRNA-seq 的参数模型可迁移至 snRNA-seq。进一步发现量化策略——尤其是参考转录组是否包含内含子区域——显著影响文库大小与细胞类型分类结果。确认了基因长度偏差存在于外显子和内含子读数中，并探讨了潜在成因。方法学贡献主要为经验验证而非新理论或新估计量。对您而言，该文与 primary interests 直接关联有限，但伪阴性对照的设计思路与 proximal CI 中 negative control 识别策略有概念上的平行，可作类比参考。
- **关键技术**: `negative binomial distribution`, `zero-inflation testing`, `pseudonegative control`, `quantification mapping strategy`, `gene length bias`
- **为什么对您有用**: 与您的研究方向直接关联较弱；伪阴性对照实验设计与 proximal CI 中 negative control 假设有概念平行，但统计方法层面（标准 NB 模型、分布拟合检验）无新理论或 sharper rate 贡献，阅读收益有限。

### 3. [10.1093/biostatistics/kxad025](https://doi.org/10.1093/biostatistics/kxad025) — Analyzing microbial evolution through gene and genome phylogenies
- **作者**: Sarah Teichman, Michael D Lee, Amy D Willis
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 3 · pp 786-800
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究微生物基因组进化中基因水平系统发育树与全基因组系统发育树之间的差异可视化问题，将估计的基因树视为数据对象，在 phylogenetic tree space 上使用 local linear approximation 将其投影到低维欧氏空间。核心方法是对 Billera-Holmes-Vogtmann (BHV) 树空间做局部线性逼近，克服了已有方法（如 PCA on tree space）在处理 tree space 拓扑结构时的实践限制，实现了对复杂树对象的直观可视化与交互式探索。理论贡献有限，主要是方法与软件实现；实证部分通过 Prevotella 菌株的离群基因历史识别和 Streptococcus 不同基因集系统发育对比展示了工具的实用性。方法以 R 包形式开源。对您而言，该文与 primary interests 的直接关联较弱，local linear approximation 属非参数技术但未涉及效率理论或半参数框架，仅统计计算层面的交互式可视化思路或可参考。
- **关键技术**: `local linear approximation on tree space`, `BHV tree space geometry`, `phylogenetic tree visualization`, `dimension reduction for tree objects`, `interactive data analysis`
- **为什么对您有用**: 与您的主要研究方向（因果推断、半参数效率、高维统计）关联较弱；local linear approximation 虽属非参数方法，但本文未涉及效率界或收敛率理论，仅统计计算与可视化层面有微弱参考价值。

### 4. [10.1093/biostatistics/kxad023](https://doi.org/10.1093/biostatistics/kxad023) — Bayesian joint models for multi-regional clinical trials
- **作者**: Nathan W Bean, Joseph G Ibrahim, Matthew A Psioda
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 3 · pp 852-866
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文在多区域临床试验（MRCT）框架下，提出基于贝叶斯模型平均（BMA）的纵向与生存数据联合建模方法，以在各区域样本量较小时实现跨区域信息借用。核心设定为 joint model 的 shared random-effects 结构，区域特异性处理效应通过 Laplace 方法对个体随机效应积分后近似其后验分布。模拟表明，相较于仅分析生存数据的方法，联合建模可提高全局处理效应检验的拒绝率，尤其在区域样本量小且纵向与生存结局关联较强时增益明显。最后将方法应用于心血管结局 MRCT 数据。该方法学 novelty 有限，主要是将已有 joint model 与 BMA 组合应用于 MRCT 新场景，对您核心兴趣方向的直接贡献较弱。
- **关键技术**: `Bayesian model averaging`, `joint longitudinal-survival model`, `Laplace approximation for random effects`, `multi-regional clinical trial design`, `information borrowing across regions`
- **为什么对您有用**: 与您 primary interests 的直接关联较弱；Laplace 近似随机效应积分属统计计算技巧但非核心，全局处理效应检验涉及假设检验但方法深度不足；若关注临床试验中区域异质性的因果/半参方法可略读。

### 5. [10.1093/biostatistics/kxad015](https://doi.org/10.1093/biostatistics/kxad015) — Blurring cluster randomized trials and observational studies: Two-Stage TMLE for subsampling, missingness, and few independent units
- **作者**: Joshua R Nugent, Carina Marquez, Edwin D Charlebois, Rachel Abbott, Laura B Balzer
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 3 · pp 599-616
- 相关性 0/10
- **摘要**: {
  "topic": "causal_inference",
  "summary_zh": "在整群随机试验（CRT）中，当仅对部分参与者进行子采样评估结局、且存在基线与终态测量缺失时，目标是估计干预效应（risk ratio）在缺失机制与有限簇数下的无偏识别与有效估计。本文将 Two-Stage TMLE 扩展至同时处理三类缺失：子采样选择、基线状态缺失、以及发病队列终态缺失，利用 targeted minimum loss 更新步骤实现 semiparametric efficiency。核心讨论在于：当簇内子单元在条件独立假设下被视为独立单位时，CRT 退化为观察性研究，精度提升但需额外 unmeasured dependence 的可忽略性假设；违反该假设可导致效应方向反转（文中从 RR=1.18 翻转为 RR=0.73）。SEARCH-TB 应用展示了不同测量与依赖假设对因果估计的实际影响。对您有用：TMLE 在 CRT 缺失设定下的扩展直接关联您对 semiparametric efficiency / TMLE 的兴趣，而"条件独立子单元"假设的批判性讨论为 longitudinal / cluster 因果推断的敏感性分析提供了可迁移思路。",
  "key_techniques": [
    "Two-Stage TMLE",
    "subsample


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

