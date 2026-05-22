# Biostatistics — Vol 23  Issue 2  ·  2026-05-21

- 共 18 篇 · Biostatistics

## 因果推断  *(causal_inference, 7 篇)*

### 1. [10.1093/biostatistics/kxaa045](https://doi.org/10.1093/biostatistics/kxaa045) — An efficient and robust approach to Mendelian randomization with measured pleiotropic effects in a high-dimensional setting
- **作者**: Andrew J Grant, Stephen Burgess
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 609-625
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在高维孟德尔随机化（MR）设定下，当大量遗传工具变量违反排他性约束（存在多效性）时，目标是有效且稳健地估计因果效应。传统多变量 MR 将所有潜在多效性特征作为协变量纳入以控制偏倚，但若部分协变量不在因果路径上则会导致效率损失。本文提出一种基于正则化的方法，在仅依赖汇总数据的情况下，从高维潜在多效性协变量中筛选出真正影响结果的变量。该方法允许协变量维度高达工具变量数减一，通过惩罚回归实现变量选择，从而同时保证估计的稳健性与半参数效率。模拟研究和尿酸对冠心病影响的流行病学实例表明，该方法在有限样本下优于标准 MVMR。对您有用：该文将高维正则化与 IV 估计结合以恢复效率，直接契合您对高维因果推断（IV/MR）及效率理论的兴趣，且提供了流行病学应用的数据分析范式。
- **关键技术**: `Mendelian randomization`, `multivariable MR`, `regularization / variable selection`, `summary-level data`, `pleiotropy adjustment`, `efficient IV estimation`
- **为什么对您有用**: 直接契合您对因果推断（IV/MR）和效率理论的兴趣，展示了高维正则化如何在放宽排他性假设的同时恢复 IV 估计的效率；同时其流行病学应用（尿酸与冠心病）提供了真实数据分析的参考。

### 2. [10.1093/biostatistics/kxaa040](https://doi.org/10.1093/biostatistics/kxaa040) — Evaluation of treatment effect modification by biomarkers measured pre- and post-randomization in the presence of non-monotone missingness
- **作者**: Yingying Zhuang, Ying Huang, Peter B Gilbert
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 541-557
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在疫苗试验的 principal stratification 框架下，目标是估计以中间生物标志物主层和基线生物标志物值为联合效应修饰因子的条件处理效应（CEP），关键假设为 principal ignorability 与非单调缺失机制下的 MAR。现有方法仅适用于单调缺失模式（有后随机化标志物则必有基线值），但登革热疫苗相关性研究中基线与后随机化标志物的缺失模式为非单调（non-monotone），导致联合效应修饰分析成为开放问题。本文提出基于 estimated likelihood 的方法：对基线与中间标志物的联合分布参数化建模，利用 EM 算法在非单调缺失下进行极大似然估计，再代入主层条件效应估计。数值实验表明，相比仅用完全观测数据的朴素方法，所提方法在偏差和 MSE 上均有改善；应用于两期登革热 III 期疫苗效力试验。该方法将 principal stratification 的效应修饰分析从单调缺失推广到非单调缺失场景，对您在因果推断中处理 post-treatment 变量与复杂缺失机制的联合问题有直接参考价值。
- **关键技术**: `principal stratification`, `estimated likelihood`, `EM algorithm`, `non-monotone missingness`, `bivariate effect modification`, `principal ignorability`
- **为什么对您有用**: 直接关联您 primary interest 中的因果推断（principal stratification 是处理 post-treatment 变量的核心框架），且非单调缺失下的 estimated likelihood 方法可迁移到其他有复杂缺失模式的因果推断问题；流行病学疫苗试验数据集对您的 secondary interest 也有价值。

### 3. [10.1093/biostatistics/kxaa034](https://doi.org/10.1093/biostatistics/kxaa034) — The role of body mass index at diagnosis of colorectal cancer on Black–White disparities in survival: a density regression mediation approach
- **作者**: Katrina L Devick, Linda Valeri, Jarvis Chen, Alejandro Jara, Marie-Abèle Bind, Brent A Coull
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 449-466
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在因果中介分析框架下，假设顺序可忽略性等标准假设成立，目标 estimand 为将黑人群体 BMI 分布匹配至白人群体复杂分布的假设干预下的自然直接与间接效应。提出一种基于贝叶斯密度回归的密度中介方法（density mediation），允许对中介变量进行全分布层面的干预，而非仅限于传统的均值平移。通过 Bayesian density regression 刻画中介变量的条件分布，克服了传统将连续中介变量分类导致的大偏差问题。模拟显示该方法在分布干预下优于仅做均值平移的方法，且避免分类偏差；在 CanCORS 数据集的应用揭示了不同年龄和收入群体的异质性中介效应。对您有用：该文将因果中介分析从均值干预扩展到分布干预，对您关注的 causal inference (mediation) 子方向提供了处理连续中介变量的新视角，同时 CanCORS 数据集对流行病学应用有参考价值。
- **关键技术**: `density regression mediation`, `distributional intervention`, `natural direct and indirect effects`, `Bayesian density regression`, `mediator categorization bias`
- **为什么对您有用**: 直接关联 primary interest 中的 causal inference (mediation)，将中介效应从传统的均值平移扩展到全分布干预，提供了处理连续型中介变量的新方法；同时属于 secondary interest 的 epidemiology (applied causal work)，CanCORS 数据集和异质性因果效应分析具有应用参考价值。

### 4. [10.1093/biostatistics/kxaa037](https://doi.org/10.1093/biostatistics/kxaa037) — Immune correlates analysis using vaccinees from test negative designs
- **作者**: Dean A Follmann, Lori Dodd
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 507-521
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在 test negative design (TND) 回顾性框架下，目标是识别疫苗诱导免疫反应对疾病风险的 prospective 效应（immune correlates slope），关键假设为 irrelevant immune response 不受活跃感染影响且与 relevant immune response 相关。核心机制利用 irrelevant protein（如载体蛋白）免疫反应作为 negative control proxy，替代感染时刻未观测的 relevant immune response，通过 logistic regression 对 imputed immune response 回归识别 prospective slope。识别策略实质上是 proximal causal inference 的 negative control 设定：irrelevant response 充当 outcome-inducing proxy，relevant response 充当 treatment-inducing proxy。文章详细推导了无偏推断所需假设，并在恒定与衰减免疫反应场景下模拟验证，最后应用于受 Ebola 环状疫苗接种启发的模拟数据集。对您有用：这是 proximal CI 的 negative control 框架在流行病学疫苗研究中的直接应用，可作为 proximal identification 假设在具体科学问题中如何形式化的范例。
- **关键技术**: `negative control proxy`, `proximal identification`, `test negative design`, `logistic regression imputation`, `immune correlates analysis`
- **为什么对您有用**: 直接连接您 primary interest 中的 proximal causal inference（negative control 设定）和 secondary interest 中的 epidemiology 应用；展示了回顾性设计中用 proxy 变量实现 identification 的假设结构形式化方式，可迁移到其他 proximal CI 问题。

### 5. [10.1093/biostatistics/kxaa044](https://doi.org/10.1093/biostatistics/kxaa044) — Bayesian design of clinical trials using joint models for longitudinal and time-to-event data
- **作者**: Jiawei Xu, Matthew A Psioda, Joseph G Ibrahim
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 591-608
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文在纵向-生存联合模型（joint model for longitudinal and time-to-event data）框架下，提出贝叶斯临床试验设计方法，目标参数为处理对生存终点的效应。联合模型通过将纵向轨迹纳入风险模型，允许非比例风险（如随时间递增的风险比）；推断基于时间变异风险比的加权平均，并将其分解为处理对生存终点的直接效应与经纵向结果中介的间接效应。样本量确定方法从贝叶斯视角同时控制 I 类错误与功效，通过后验概率阈值校准实现频率派 operating characteristics。文中以乳腺癌临床试验演示方法，纵向预测标志物在随访中定期采集。对您而言，中介效应分解（直接/间接效应）与纵向因果推断的连接值得关注，但方法本身是参数化贝叶斯框架，未涉及半参数效率理论或 influence function，理论深度有限。
- **关键技术**: `joint model for longitudinal and time-to-event`, `Bayesian trial design`, `mediation decomposition (direct/indirect effect)`, `non-proportional hazards`, `Bayesian type I error calibration`, `time-varying hazard ratio`
- **为什么对您有用**: 中介效应分解与纵向因果推断的设定直接关联您 primary interest 中的 causal mediation 与 longitudinal CI，但本文为参数化贝叶斯方法，不涉及半参数效率界或 debiased 方法，理论迁移价值有限；乳腺癌临床试验数据集对 epidemiology 应用有参考价值。

### 6. [10.1093/biostatistics/kxaa033](https://doi.org/10.1093/biostatistics/kxaa033) — Adaptive treatment strategies for chronic conditions: shared-parameter G-estimation with an application to rheumatoid arthritis
- **作者**: Shouao Wang, Erica Em Moodie, David A Stephens, Jagtar S Nijjar
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 430-448
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在纵向自适应治疗策略（ATS/DTR）框架下，传统序贯 G-estimation 假设各决策点参数独立，本文研究跨时间点共享决策参数的因果估计问题。提出一种新的共享参数 G-estimation 计算方法，允许同一决策规则在不同时间点复用参数，从而降低参数维度并简化临床实施。该方法继承了非共享序贯 G-estimation 的双重稳健性，并在正则条件下达到半参数有效。理论证明了估计量的渐近性质，实证部分使用苏格兰早期类风湿性关节炎（SERA）队列进行了验证。对您有用：直接推进了您关注的纵向因果推断中的 DTR 估计与效率理论，同时 SERA 队列数据对您的流行病学应用兴趣有参考价值。
- **关键技术**: `shared-parameter G-estimation`, `adaptive treatment strategies`, `double robustness`, `semiparametric efficiency`, `dynamic treatment regimes`
- **为什么对您有用**: 直接对应您 primary interest 中的纵向因果推断与效率理论（双重稳健与半参数有效），同时提供了 secondary interest 中流行病学（类风湿性关节炎队列）的真实数据集与因果分析范式。

### 7. [10.1093/biostatistics/kxaa032](https://doi.org/10.1093/biostatistics/kxaa032) — A sparse additive model for treatment effect-modifier selection
- **作者**: Hyung Park, Eva Petkova, Thaddeus Tarpey, R Todd Ogden
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 412-429
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维协变量设定下，本文研究治疗效应修饰变量的选择与非线性交互效应估计，假设交互项具有稀疏加性结构而主效应完全未指定。提出一种稀疏加性模型，通过特定约束仅估计处理与协变量的交互效应，将主效应视为无穷维干扰参数。估计过程结合稀疏惩罚与加性模型的平滑方法，实现高维非参数交互项的筛选与估计。模拟与 RCT 实证表明该方法能有效识别具有非线性交互的处理效应修饰变量。对您有用：该工作将主效应作为 nuisance parameter 的半参数建模思路，与您关注的 semiparametric efficiency 及高维因果推断中的异质性处理效应（CATE）估计直接相关。
- **关键技术**: `sparse additive model`, `treatment effect modification`, `heterogeneous treatment effects`, `semiparametric nuisance parameter`, `interaction effect selection`
- **为什么对您有用**: 直接关联您的高维因果推断与半参数理论兴趣：将主效应视为未指定的干扰参数并仅约束交互项的半参数建模思路，为高维 CATE 估计与变量选择提供了可借鉴的框架。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1093/biostatistics/kxaa043](https://doi.org/10.1093/biostatistics/kxaa043) — Integrative functional linear model for genome-wide association studies with multiple traits
- **作者**: Yang Li, Fan Wang, Mengyun Wu, Shuangge Ma
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 574-590
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在多性状 GWAS 设定下，目标是将高维 SNP 数据作为函数对象纳入联合模型，在惩罚约束下同时利用多性状相关性进行变量选择与估计。方法创新点在于首次将 SNP 近似为函数对象（functional objects），在多性状联合线性模型中引入 penalization，以同时处理 SNP 高维性和性状间相关性，实现跨性状信息借用。理论方面给出了高维设定下估计量的收敛性质（具体收敛率需参正文）。模拟显示该方法在识别和估计疾病相关遗传变异方面优于四种替代方法；2 型糖尿病数据分析得到生物学有意义的结果，预测精度和选择稳定性良好。对您而言，该文的高维惩罚函数模型思路可迁移至多结局因果推断中的高维中介/工具变量设定，2 型糖尿病 GWAS 数据集也可作为高维方法实证的参考数据源。
- **关键技术**: `functional linear model`, `penalized regression`, `multi-trait joint modeling`, `SNP functional approximation`, `high-dimensional variable selection`
- **为什么对您有用**: 高维惩罚函数建模的组合思路可迁移至您关注的高维因果推断（如高维 IV/中介分析中的变量选择），且 2 型糖尿病 GWAS 数据集对高维方法的实证检验有参考价值。

## 非参数 / 半参数  *(nonparam_semipara, 2 篇)*

### 1. [10.1093/biostatistics/kxaa035](https://doi.org/10.1093/biostatistics/kxaa035) — Bayesian sparse heritability analysis with high-dimensional neuroimaging phenotypes
- **作者**: Yize Zhao, Tengfei Li, Hongtu Zhu
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 467-484
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在高维神经影像表型的遗传力分析设定下，目标是联合估计多个脑影像性状的 heritability，假设表型间存在基于脑结构网络和体素依赖的稀疏结构。方法采用层次化贝叶斯选择机制，利用脑结构网络先验约束区域与局部测量的稀疏性；同时引入非参数 Dirichlet process mixture 对 SNP 关联的表型变异进行自适应分组，避免预设分组数。模拟表明该方法在 heritability 估计和可遗传性状选择上优于现有单表型及多变量方法。实证应用于 ADNI 和 UK Biobank 两个大规模影像遗传数据集，给出生物学可解释的结果。对您而言，该文的 Dirichlet process 非参数建模和高维稀疏贝叶斯计算策略可部分迁移到高维统计问题中，但与您核心的效率理论和因果推断方向距离较远。
- **关键技术**: `Dirichlet process mixture`, `Bayesian sparse selection`, `hierarchical structural network prior`, `high-dimensional heritability estimation`, `voxel-dependent modeling`
- **为什么对您有用**: 高维稀疏贝叶斯建模和 Dirichlet process 非参数成分与您的高维统计和非参数理论兴趣有弱关联，但核心问题（遗传力估计）和方法论（贝叶斯）与效率理论和因果推断主方向距离较远，主要收益在于了解高维表型建模的计算策略和大规模影像遗传数据集结构。

### 2. [10.1093/biostatistics/kxaa041](https://doi.org/10.1093/biostatistics/kxaa041) — Bayesian analysis of longitudinal and multidimensional functional data
- **作者**: John Shamshoian, Damla Şentürk, Shafali Jeste, Donatello Telesca
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 558-573
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究纵向多维函数数据（longitudinal functional data）的非参数贝叶斯推断，目标是在纵向函数框架下同时估计条件函数均值与函数协方差曲面，并提取低维可解释特征。方法核心是基于自适应分块 Gibbs 采样的非参数贝叶斯程序，一步完成数据平滑、条件均值估计与协方差曲面估计，后验推断依赖 Monte Carlo 样本。理论贡献集中于计算效率与多任务联合估计的框架设计，但未给出后验收敛率或 minimax 最优性结果。实证部分通过模拟比较了多种 operative characteristics，并在两个案例中展示应用：跨国年龄别生育率（经济/人口数据）与自闭症儿童的隐式学习实验（流行病学数据）。对您而言，该文的非参数函数协方差估计与自适应 Gibbs 计算方案可迁移至纵向因果推断中处理函数型混杂/中介的设定，但方法学 novelty 偏应用层面。
- **关键技术**: `nonparametric Bayesian smoothing`, `adaptive blocked Gibbs sampling`, `functional covariance surface estimation`, `longitudinal functional principal components`, `conditional functional mean estimation`
- **为什么对您有用**: 非参数贝叶斯函数数据方法与您 semiparametric/nonparametric theory 兴趣有交叉，且纵向函数协方差估计可迁移至纵向因果推断中处理函数型混杂/中介变量；流行病学案例（自闭症队列）提供真实数据集参考。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1093/biostatistics/kxaa030](https://doi.org/10.1093/biostatistics/kxaa030) — General tests of the Markov property in multi-state models
- **作者**: Andrew C Titman, Hein Putter
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 380-396
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在多状态事件历史模型设定下，本文研究马尔可夫假设（即未来转移率不依赖于历史状态）的检验问题。文章整合并比较了两种现有方法：将状态进入时间作为协变量的Cox模型检验，以及检测共享脆弱性的分层Commenges-Andersen检验。核心贡献是提出了一类新的基于对数秩统计量族的检验方法：通过按不同初始时间点所处状态对患者分组，检验后续转移率的差异。该检验被扩展至条件马尔可夫模型，并采用Wild bootstrap近似检验统计量的零分布。模拟表明Cox方法功效稳健，而新提出的对数秩检验在非马尔可夫行为不持续或不均匀时表现更优，实证应用于流行病学睡眠行为数据。该文为纵向多状态因果模型中的关键马尔可夫假设提供了具体的假设检验工具，其Wild bootstrap与分组对数秩的组合思路对您在 longitudinal 和 hypothesis testing 的交叉研究有参考价值。
- **关键技术**: `Markov property test`, `Cox model with entry time covariate`, `Commenges-Andersen test`, `stratified log-rank statistic`, `shared frailty`, `wild bootstrap`
- **为什么对您有用**: 直接关联您在 hypothesis testing 和 longitudinal causal inference 的兴趣：多状态模型是纵向因果与事件历史分析的基础，检验其 Markov 假设是保证后续推断有效性的关键；同时提供了流行病学（睡眠行为）的应用实例与数据集参考。

## 统计计算 / 算法  *(stat_computing, 3 篇)*

### 1. [10.1093/biostatistics/kxaa038](https://doi.org/10.1093/biostatistics/kxaa038) — Fast Lasso method for large-scale and ultrahigh-dimensional Cox model with applications to UK Biobank
- **作者**: Ruilin Li, Christopher Chang, Johanne M Justesen, Yosuke Tanigawa, Junyang Qian, Trevor Hastie et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 522-540
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在超高大维 Cox 比例风险模型设定下，本文目标是解决 L1 正则化部分似然在大规模数据（无法载入内存）下的可扩展计算问题。核心方法将 BASIL (Batch Screening Iterative Lasso) 算法推广至 Cox 模型，通过批量强变量筛选与迭代 Lasso 拟合来逼近完整正则化路径，并输出各 λ 下的参数估计及验证集 C-index/deviance。该方法避免了全设计矩阵的内存驻留，适用于 p≫n 的超高大维场景。实证将基于 PLINK2 开发的 snpnet-Cox 应用于 UK Biobank 的 306 种疾病基因型-生存时间数据。虽然本文侧重计算算法而非高维推断理论（如 debiased Lasso 或效率界），但其针对超高大维 Cox 模型的内存外计算策略对您的统计计算兴趣有直接参考价值，且 UK Biobank 数据集对流行病学应用具有数据集价值。
- **关键技术**: `Lasso-penalized Cox model`, `BASIL algorithm`, `out-of-core computation`, `batch screening`, `partial likelihood`, `C-index`
- **为什么对您有用**: 涉及您 primary interest 中的统计计算（超大规模数据的内存外迭代算法）和高维统计（ultrahigh-dimensional Lasso），且 UK Biobank 的基因-生存数据集对您 secondary interest 中的流行病学应用有数据集参考价值，但缺乏高维推断或效率理论。

### 2. [10.1093/biostatistics/kxaa036](https://doi.org/10.1093/biostatistics/kxaa036) — Interim recruitment prediction for multi-center clinical trials
- **作者**: Szymon Urbas, Chris Sherlock, Paul Metcalfe
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 485-506
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 本文研究多中心临床试验的期中招募预测问题，针对现有时间齐次招募模型产生过于乐观且狭窄的预测区间这一缺陷，提出新的建模与预测框架。首先构造了两个用于检测招募率衰减趋势的假设检验（附 power 分析），随后引入基于单调衰减强度函数的非齐次 Poisson 过程模型，允许任意参数曲线形状的灵活适配。方法层面提供了通用的参数先验构造策略，并通过 Bayesian model averaging 同时整合参数与模型不确定性进行预测，模拟验证了方法的有效性及对模型误设的稳健性。在肿瘤试验数据上的应用表明，新方法较现有方法给出更合理的预测区间，并能识别招募模式的异常变化。对您而言，假设检验部分（衰减检测的 power study）与 mathematical statistics & hypothesis testing 兴趣有弱连接，Bayesian model averaging 的预测框架对统计计算有参考价值，但整体方法学深度偏应用。
- **关键技术**: `inhomogeneous Poisson process`, `Bayesian model averaging`, `recruitment decay detection test`, `power analysis`, `prior elicitation for parametric models`
- **为什么对您有用**: 假设检验部分（招募率衰减的两个检验及 power study）与您 hypothesis testing 兴趣弱相关；Bayesian model averaging 预测框架对 statistical computing 有一定参考；肿瘤试验数据集对 epidemiology 应用方向有数据价值，但方法学 novelty 偏应用层面。

### 3. [10.1093/biostatistics/kxaa031](https://doi.org/10.1093/biostatistics/kxaa031) — A divide-and-conquer method for sparse risk prediction and evaluation
- **作者**: Chuan Hong, Yan Wang, Tianxi Cai
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 397-411
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在超大样本与高维协变量设定下，现有分治（DAC）算法计算代价高且无法对风险预测模型的准确度做统计推断。本文提出 SOLID 算法，将 DAC 与变量筛选及序列线性化结合，仅对筛选后协变量最大化似然并通过快速近似做 L1 惩罚估计。为评估预测准确度，作者提出修正交叉验证（MCV），利用 SOLID 的中间副产物大幅降低计算负担，这是首个对准确度做推断的 DAC 过程。理论与模拟表明，SOLID/MCV 在计算速度上显著优于现有 DAC，且统计效率与全样本估计相当，MCV 提供了有效的区间估计。实证部分基于 Partners HealthCare 电子病历文本构建疾病诊断分类模型。该工作对您在统计计算（大规模数据分治与线性化近似算法）和高维推断方面的研究有直接借鉴价值，其 EHR 数据应用也契合流行病学次要兴趣。
- **关键技术**: `divide-and-conquer`, `one-step linearization`, `sparse logistic regression`, `modified cross-validation`, `high-dimensional screening`
- **为什么对您有用**: 直接关联您在统计计算（大规模数据分治与快速近似算法）和高维统计（稀疏回归推断）方面的兴趣；其基于 EHR 临床文本的流行病学应用也契合您的次要兴趣，提供了可迁移的数据分析管线参考。

## 流行病学  *(epidemiology, 2 篇)*

### 1. [10.1093/biostatistics/kxaa028](https://doi.org/10.1093/biostatistics/kxaa028) — Surrogate-guided sampling designs for classification of rare outcomes from electronic medical records data
- **作者**: W Katherine Tan, Patrick J Heagerty
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 345-361
- 相关性 0/10 · novelty: `application`
- **摘要**: 在电子病历(EMR)罕见结局的标注设定下，针对简单随机抽样导致病例稀少且标注昂贵的问题，研究基于辅助变量的富集抽样设计。提出利用与真实结局相关的高特异性辅助变量进行分层抽样，以提升样本中病例的富集度。从理论上分析了该抽样设计对模型训练与验证阶段判别力的影响，证明富集抽样可转化为更好的统计学习表现。模拟与LIRE研究的放射学文本数据实证均支持所提设计的有效性。对您而言，该文提供了EMR罕见结局的真实数据集与处理范式，其基于替代指标的抽样机制对因果推断中处理选择偏倚或测量误差有参考价值。
- **关键技术**: `enrichment sampling design`, `stratified sampling`, `auxiliary variables`, `rare outcome classification`, `model discrimination`
- **为什么对您有用**: 属于流行病学应用，提供EMR罕见结局真实数据集；其基于替代指标的分层抽样设计思路，对因果推断中处理选择偏倚或缺失数据机制有方法迁移的参考价值。

### 2. [10.1093/biostatistics/kxaa048](https://doi.org/10.1093/biostatistics/kxaa048) — Quantifying diagnostic accuracy improvement of new biomarkers for competing risk outcomes
- **作者**: Zheng Wang, Yu Cheng, Eric C Seaberg, James T Becker
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 666-682
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在竞争风险设定下，将衡量生物标志物预测能力提升的指标 NRI 和 IDI 扩展至竞争风险结局，利用累积发生函数（CIF）量化竞争事件的累积风险。针对独立删失导致的“缺失”类别，采用逆概率加权（IPW）进行处理；模型层面涵盖了 Fine-Gray、多状态及多项逻辑斯谛等竞争风险模型。推断方面，NRI 基于估计量的渐近正态性构建假设检验，IDI 则采用 BCa bootstrap 进行区间估计。模拟验证了推断程序的有限样本表现，并在 Multicenter AIDS Cohort Study 数据上展示了认知障碍与死亡竞争风险的实际应用。对您而言，该文提供了流行病学队列数据中竞争风险与 IPW 结合的具体推断框架，可作为纵向因果推断中处理竞争删失的参考案例。
- **关键技术**: `competing risks`, `net reclassification improvement (NRI)`, `integrated discrimination improvement (IDI)`, `inverse probability weighting (IPW)`, `cumulative incidence function`, `BCa bootstrap`
- **为什么对您有用**: 虽然核心是预测指标扩展而非因果识别，但竞争风险与 IPW 的处理方式对您关注的纵向因果推断与流行病学应用有直接参考价值，且提供了真实的 AIDS 队列数据集分析范式。

## 其他  *(other, 2 篇)*

### 1. [10.1093/biostatistics/kxaa047](https://doi.org/10.1093/biostatistics/kxaa047) — Dose–response modeling in high-throughput cancer drug screenings: an end-to-end approach
- **作者**: Wesley Tansey, Kathy Li, Haoran Zhang, Scott W Linderman, Raul Rabadan, David M Blei et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 643-665
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文针对高通量癌症药物筛选实验，提出了一种层次贝叶斯剂量–响应模型，estimand 为给定分子特征条件下细胞系对药物的敏感性曲线（IC50 等参数），假设药物响应服从参数化的 sigmoid 形式并在细胞系–药物对上引入层次先验。模型拟合采用变分推断与 MCMC 混合策略，结合 conditional randomization test 进行标记物筛选——该检验在给定协变量下对零分布进行模型化重采样，属于 model-based conditional independence testing。在 held-out 预测上比传统 log-linear 方法降低约 20% 误差，案例中成功复现 Nutlin-3(a) 对 TP53 野生型 + MDM2 过表达的已知生物学关联。对您而言，conditional randomization test 的思路可迁移到因果推断中 conditional independence / marker discovery 的假设检验问题，但整体方法学 novelty 偏应用层面。
- **关键技术**: `hierarchical Bayesian model`, `conditional randomization test`, `variational inference`, `dose-response curve estimation`, `model-based conditional independence testing`
- **为什么对您有用**: conditional randomization test 与您 hypothesis testing 和 causal inference 中的 conditional independence testing 有方法迁移价值；层次贝叶斯拟合的计算方案对 statistical computing 兴趣有参考，但整体偏应用药理学，与核心理论兴趣距离较远。

### 2. [10.1093/biostatistics/kxaa046](https://doi.org/10.1093/biostatistics/kxaa046) — Principal curve approaches for inferring 3D chromatin architecture
- **作者**: Elena Tuzhilina, Trevor J Hastie, Mark R Segal
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 2 · pp 626-642
- 相关性 2/10 · novelty: `application`
- **摘要**: 在 Hi-C 数据推断 3D 染色质结构的设定下，目标是将成对邻近数据重构为三维空间中的一维曲线。现有方法通常施加计算繁重的约束或事后强制连续，本文将主曲线（principal curve）方法扩展到度量缩放（metric scaling）问题，直接寻找 1D 曲线解。该方法生成由平滑度或自由度参数索引的候选解序列，并提出了相应的模型选择方法。在 IMR90 细胞 Hi-C 数据上的实证结果表明该主曲线方法在结构变异下具有较好的重构精度和可重复性。对您而言，虽然涉及非参数平滑（主曲线），但属于基因组学特定应用，未涉及半参数效率或高维推断理论，与您核心兴趣关联较弱。
- **关键技术**: `principal curves`, `metric scaling`, `multidimensional scaling`, `smoothing parameter selection`, `Hi-C data`
- **为什么对您有用**: 本文属于基因组学应用，虽使用非参数主曲线方法，但未涉及您关注的半参数效率界或高维理论，且不在您指定的应用领域（天文/经济/流行病）内，方法学借鉴价值较低。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

