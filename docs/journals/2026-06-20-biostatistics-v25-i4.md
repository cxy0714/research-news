# Biostatistics — Vol 25  Issue 4  ·  2026-06-20

- 共 19 篇 · Biostatistics
- 目录核对 ⚠️ 疑似漏 1 篇（对照 OpenAlex 21 篇）：10.1093/biostatistics/kxae011

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

第一期《Biostatistics》的19篇文章主要围绕四条主线展开：因果推断与识别（中介分析、动态治疗、孟德尔随机化、测量误差校正）、函数型数据与非参数检验、贝叶斯层次建模及计算、以及高维缺失数据处理与流行病学应用。因果推断方向最为集中，覆盖了多中介与中间混杂的非参数估计、基于剩余寿命的最优治疗规则、不可观测暴露的孟德尔随机化、信息性时间下的序贯治疗、以及联合建模与测量误差修正；非参数/半参数方向涉及稀疏多变量函数数据的两样本检验、函数SVM分类回归，以及复发事件时变判别指标。流行病学应用篇中有相当比例内嵌因果识别问题（单臂pre-post的回归均值偏差校正、多源域死因迁移），贝叶斯方法则贯穿序贯治疗、联合模型、差异调控、药物-基因交互及脑网络关联等多个场景，计算方面关注协变量辅助的矩阵补全。

因果推断主线推进了多个核心纠偏问题。中介分析方面，“Practical causal mediation”通过扩展影响函数和交叉拟合，首次将非参数双稳健估计器推广至多中介与多中间混杂共存的情形，直接回应实际分析中的常见难点。动态治疗方面，“Residual life value estimator”将Q-learning与IPW结合，在电子病历数据中优化累积受限剩余寿命，其反事实值函数构造思路可迁移至其他纵向因果估计。孟德尔随机化方面，“Multiple biomarkers of an underlying common exposure”利用二阶矩约束绕过潜在暴露不可观测性，仅需GWAS summary数据即可识别因果效应并控制多效性，为多生物标志物MR提供了可操作框架。测量误差校正方面，“Exponential family measurement error models”针对单细胞CRISPR中的非经典测量误差，证明现有thresholded回归的偏差并给出一致估计量，其误差-in-变量框架对因果推断中的暴露测量误差问题有直接启示。此外，“Bayesian semiparametric sequential treatment”用Gamma Process建模信息性时间下的转移强度，并通过G-computation调整时变混杂，将因果推断延拓至连续时间生存设定。

贝叶斯方法是另一条突出手段，覆盖了从联合建模到迁移学习的多样应用。“Bayesian joint modeling of multivariate longitudinal and survival”通过结构化copula相关矩阵在小样本下提升效率，其协方差分解思想可推广至因果敏感性分析；“Tree-informed Bayesian multi-source domain adaptation”利用树结构先验进行跨人群死因分配，spike-and-slab机制实现自适应信息池化，为多源域因果迁移提供了可扩展的变分推断方案；“DifferentialRegulation”处理RNA-seq读段多映射不确定性，潜变量分配嵌入因果推断所需的误差量化；“Bayesian approach for pharmacogenetics”通过高斯过程复合核函数编码治疗历史，适合时变处理效应的敏感性建模。这些方法不仅在各自应用中有效，其先验构造与后验推断策略对因果推断中的不确定性量化亦有参考价值。

与因果推断和半参数效率最贴近的优先阅读篇目包括：中介分析（Practical causal mediation）、测量误差修正（Exponential family measurement error models）、单臂pre-post校正（Identifying predictors of resilience to stressors）、孟德尔随机化（Mendelian randomization using multiple biomarkers），以及动态治疗（Residual life value estimator）。与函数型数据高维检验相关的可关注投影检验（Projection-based two-sample inference）和功能SVM（Functional support vector machine）。

## 因果推断  *(causal_inference, 5 篇)*

### 1. [10.1093/biostatistics/kxae012](https://doi.org/10.1093/biostatistics/kxae012) — Practical causal mediation analysis: extending nonparametric estimators to accommodate multiple mediators and multiple intermediate confounders
- **作者**: Kara E Rudolph, Nicholas T Williams, Ivan Diaz
- **期刊/来源**: Biostatistics
- **机构**: Columbia University · New York University
- **分类**: vol 25 · issue 4 · pp 997-1014
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文聚焦于因果中介分析中的实际挑战：同时存在多个中介变量和多个暴露后中间混杂因素时，如何估计干预的直接和间接效应（IDE/IIE）。现有IDE/IIE的非参数估计器无法直接处理多变量中介与多变量中间混杂并存的情况，而这在真实数据分析中很常见。作者基于最近发展的单变量IDE/IIE非参数估计器，通过扩展影响函数和交叉拟合框架，提出了可同时纳入多变量中介与中间混杂的估计量。该估计量继承了非参数双稳健性质，并在有限样本下通过模拟验证性能。方法应用于评估儿童时期获得Section 8住房券对青少年精神障碍风险的间接效应，其中中介包括邻里贫困、学校环境等，并处理了中介之间的相关性。对您而言，这是一篇直接服务于您因果推断兴趣中中介分析的方法论文，且附带了流行病学实际数据应用。
- **关键技术**: `Interventional direct and indirect effects (IDE/IIE)`, `nonparametric estimation`, `influence function`, `cross-fitting`, `multiple mediators`, `intermediate confounders`
- **为什么对您有用**: 本文直接针对您主要兴趣中的因果中介分析，尤其是IDE/IIE在多变量设置下的非参数估计扩展。您非常熟悉非参数统计与因果推断估计理论，可立即评估该估计量的效率性质或与其他方法比较。此外，流行病学实际数据应用也符合您的次要兴趣。立即可做的后续工作：利用您掌握的估计理论验证双稳健性在多种混杂结构下的表现，或尝试将HOIF (higher-order influence functions) 扩展至此设定。

### 2. [10.1093/biostatistics/kxae002](https://doi.org/10.1093/biostatistics/kxae002) — Estimation of optimal treatment regimes with electronic medical record data using the residual life value estimator
- **作者**: Grace Rhodes, Marie Davidian, Wenbin Lu
- **期刊/来源**: Biostatistics
- **机构**: Eli Lilly (United States) · North Carolina State University
- **分类**: vol 25 · issue 4 · pp 933-946
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在纵向电子病历（EMR）数据设定下，目标是估计最大化期望累积受限剩余寿命（cumulative restricted residual life）的最优动态治疗规则（DTR）。本文提出 ReLiVE 估计量，用于估计固定治疗规则下的受限剩余寿命期望值，并在此基础上构建 ReLiVE-Q 方法，通过 Q-learning 的向后归纳算法寻找最优 DTR。核心机制结合了 IPW 与 Q-learning 的值函数近似，在多阶段决策中利用累积患者信息进行策略优化。模拟与 MIMIC-III 脓毒症 ICU 数据实证表明，ReLiVE-Q 能有效优化具有临床意义的剩余寿命结局。对您可能有用：本文将 DTR 的 estimand 从常见均值扩展至受限剩余寿命，为 longitudinal causal inference 的 Q-learning 方法提供了新结局变量的理论框架。
- **关键技术**: `dynamic treatment regime`, `Q-learning backward induction`, `restricted residual life`, `inverse probability weighting`, `value function estimation`, `electronic medical record longitudinal data`
- **为什么对您有用**: 本文直接连接到 longitudinal causal inference 的 DTR 估计子方向，将 estimand 从传统均值扩展至受限剩余寿命，丰富了 Q-learning 的值函数设定。从 technical_arsenal 看，您对 identification theory in causal inference（moderately_familiar）可直接审视其 estimand 的 identification 条件与 IPW 构造是否完备，但本文未涉及 semiparametric efficiency bound 或 higher-order 修正，理论深度有限。Follow-up 判断：**中期可做**——若想在此方向深入，需先在 moderately_familiar 的 semiparametric theory 上长肌肉，为 ReLiVE 构造 doubly-robust / one-step efficient estimator 及其 influence function。

### 3. [10.1093/biostatistics/kxae006](https://doi.org/10.1093/biostatistics/kxae006) — Mendelian randomization analysis using multiple biomarkers of an underlying common exposure
- **作者**: Jin Jin, Guanghao Qi, Zhi Yu, Nilanjan Chatterjee
- **期刊/来源**: Biostatistics
- **机构**: Johns Hopkins University · University of Pennsylvania · University of Washington · Johns Hopkins Medicine · Cancer Research And Biostatistics · Broad Institute
- **分类**: vol 25 · issue 4 · pp 1015-1033
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在 Mendelian randomization (MR) 框架下，当核心暴露（如系统性炎症）不可直接观测时，目标是通过多个共调节生物标志物的 GWAS summary statistics 对潜在暴露的因果效应进行 identification 与方向检验。作者提出 MRLE 方法，在结构方程模型设定下（允许遗传变异通过潜在暴露的间接效应及对性状的直接效应，即多效性），基于可观测性状的二阶矩构造一组估计函数。该方法仅需 GWAS summary-level 数据，通过二阶矩约束绕开潜在暴露的不可观测性，在多种多效性设定下保持了 type I error 的良好控制并提升了检验功效。模拟与五项炎症生物标志物的实证分析表明，MRLE 能检测到炎症对冠心病、结直肠癌和类风湿性关节炎的因果证据，而标准单性状 MR 则无法一致检出。对您可能有用：本文将 IV/MR 方法拓展至 latent exposure 设定，与因果推断的 identification 理论及 IV 多效性敏感性分析直接相关。
- **关键技术**: `Mendelian randomization`, `structural equation model`, `second-order moment estimating functions`, `GWAS summary statistics`, `latent exposure identification`, `pleiotropy robust inference`
- **为什么对您有用**: 本文直接连接到因果推断中的 IV 方法与 identification 理论子方向，处理了 IV 分析中暴露变量 latent 时的 identification 与估计问题。研究者武器库中 very_familiar 的 estimation theory in causal inference 与 moderately_familiar 的 identification theory in causal inference 可直接用来审视其 SEM 设定下的二阶矩 identification 逻辑是否完备、估计函数的 semiparametric efficiency 是否可达。follow-up 粗判：立即可做——可用 semiparametric efficiency bound 工具分析该二阶矩估计函数的效率性质，并探索是否可构造 one-step / orthogonal 修正以提升有限样本表现。

### 4. [10.1093/biostatistics/kxad035](https://doi.org/10.1093/biostatistics/kxad035) · [arXiv](https://arxiv.org/abs/2211.16393) — Bayesian semiparametric model for sequential treatment decisions with informative timing
- **作者**: Arman Oganisian, Kelly D Getz, Todd A Alonzo, Richard Aplenc, Jason A Roy
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 947-961
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在纵向动态治疗设定下，目标是估计儿科 AML 患者在不同动态 ACT 用药策略下的潜在生存概率，面临时变混杂、信息性时间（恢复时间影响后续治疗与生存）及死亡/退出截断三重障碍。作者提出基于 Gamma Process 先验的贝叶斯半参数生成模型，在连续时间下刻画每个治疗阶段的状态转移，并通过 G-computation 计算调整时变混杂后的潜在生存概率后验分布。核心机制在于用 Gamma Process 灵活建模转移强度，避免参数化风险设定假设，同时将信息性时间直接纳入生成模型的转移结构。实证分析表明，基于心脏功能动态调整 ACT 的策略能提升生存概率。对您有用：本文将信息性时间与纵向因果推断结合，是 longitudinal causal inference 中处理 informative timing 的具体贝叶斯半参数实现。
- **关键技术**: `Bayesian semiparametric model`, `Gamma Process prior`, `G-computation`, `dynamic treatment regimes`, `informative timing`, `time-varying confounding`
- **为什么对您有用**: 直接连接 longitudinal causal inference 子方向，处理了纵向因果中常见的 informative timing 与时变混杂问题。可用 technical_arsenal 中 moderately_familiar 的 semiparametric theory 与 identification theory 来审视其 Gamma Process 先验的半参数建模是否达到非参数效率界，或对比 frequentist 的 longitudinal TMLE / HOIF 路径。中期可做：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，才能将此贝叶斯生成框架与 frequentist 效率理论做系统性对比与拓展。

### 5. [10.1093/biostatistics/kxae009](https://doi.org/10.1093/biostatistics/kxae009) — Bayesian joint modeling of multivariate longitudinal and survival outcomes using Gaussian copulas
- **作者**: Seoyoon Cho, Matthew A Psioda, Joseph G Ibrahim
- **期刊/来源**: Biostatistics
- **机构**: University of North Carolina at Chapel Hill · GlaxoSmithKline (United States)
- **分类**: vol 25 · issue 4 · pp 962-977
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出一种基于高斯copula的联合模型，用于同时分析多元纵向结果（如多个生活质量指标）和生存时间（如无病生存期），允许保持各边缘分布的边际模型形式，同时通过copula刻画纵向与生存之间的相关性。方法核心是提出一种结构化的相关矩阵分解，可施加如自回归等协方差结构，相比传统的无结构相关矩阵在小样本下提高效率并减少计算负担。采用贝叶斯马尔可夫链蒙特卡洛（MCMC）进行参数估计，并给出完整的计算流程。通过模拟研究验证了方法的有限样本表现。实际数据来自国际乳腺癌研究组试验，分析生活质量纵向轨迹与复发/死亡风险的关联。本文方法适用于流行病学队列的联合建模，也可推广到因果推断中的时变暴露与删失结局的敏感性分析，与您对纵向因果推断和统计计算的兴趣关联紧密。
- **关键技术**: `Gaussian copula`, `correlation matrix decomposition`, `Bayesian MCMC`, `joint modeling of longitudinal and survival data`, `auto-regressive covariance structure`
- **为什么对您有用**: 本文的纵向-生存联合建模直接适用于流行病学队列研究，属于您的secondary interest epidemiology，同时也可用于因果推断中的时变治疗和生存结局（causal inference longitudinal）。您的very_familiar工具中的软件开发和统计计算经验可以用于复现和扩展该模型的编程实现；不过需要先补充贝叶斯MCMC的深入知识（属于moderately_familiar范畴），因此该论文可作为中期可做的学习与follow-up素材。

## 非参数 / 半参数  *(nonparam_semipara, 3 篇)*

### 1. [10.1093/biostatistics/kxae004](https://doi.org/10.1093/biostatistics/kxae004) · [arXiv](https://arxiv.org/abs/2302.05612) — Projection-based two-sample inference for sparsely observed multivariate functional data
- **作者**: Salil Koner, Sheng Luo
- **期刊/来源**: Biostatistics
- **机构**: Duke University
- **分类**: vol 25 · issue 4 · pp 1156-1177
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在稀疏纵向设计下，目标是检验多变量函数型数据的两组总体均值差异，假设协方差结构属于宽泛的非平稳类。方法先用 multivariate functional principal component analysis (MFPCA) 对无限维多模态函数降维并保留分量间的动态相关，再基于投影构造单一 p-value 的两样本显著性检验，避免了逐分量检验的多重校正问题。理论方面，文章证明了在稀疏观测下 MFPCA 估计的一致性，并给出检验统计量的渐近零分布与功效性质。模拟显示该方法在有限样本下维持 type-I error 且功效优于现有逐分量或单变量函数检验。对您可能有用：该投影检验框架可视为纵向/函数型数据中的 semiparametric hypothesis testing 问题，其 MFPCA 降维+投影构造与您熟悉的 semiparametric efficiency 及 minimax bound 视角有方法论交集。
- **关键技术**: `multivariate functional PCA`, `sparse longitudinal design`, `projection-based two-sample test`, `non-stationary covariance`, `asymptotic null distribution`
- **为什么对您有用**: 本文连接到 semiparametric & nonparametric theory 中的函数型数据 hypothesis testing 子方向，其 MFPCA 降维+投影构造单一检验统计量的思路，可用您 very_familiar 的 minimax bounds 视角审视其投影维数选择是否达到最优 rate，或用 moderately_familiar 的 M-estimation theory 分析稀疏观测下 MFPCA 估计的收敛条件是否可进一步弱化。follow-up 粗判：中期可做——需先在 moderately_familiar 的 semiparametric theory 上长肌肉，具体是将函数型数据的 semiparametric efficiency bound 理论引入该投影检验框架，以评估当前构造是否达到效率下界。

### 2. [10.1093/biostatistics/kxae010](https://doi.org/10.1093/biostatistics/kxae010) · [arXiv](https://arxiv.org/abs/2201.01879) — Exponential family measurement error models for single-cell CRISPR screens
- **作者**: Timothy Barry, Kathryn Roeder, Eugene Katsevich
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 1254-1272
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在单细胞 CRISPR 筛选数据设定下，目标 estimand 是基因扰动对基因表达的因果效应，但扰动指示变量存在非经典测量误差（零膨胀计数）且与响应共享混杂。本文首先证明现有标准方法 thresholded regression 存在 attenuation bias，且其 tuning parameter 的选择面临 bias-variance tradeoff。为此提出 GLM-EIV 方法，将经典 errors-in-variables 模型推广至响应与带噪预测变量均服从指数族分布、且受同一混杂影响的情形，通过修正测量误差实现 consistent estimation。作者还开发了基于云/集群的并行计算基础设施，将方法应用于两个大规模真实数据集并给出生物学新发现。对您可能有用：该模型实质上是带测量误差的因果推断问题，其指数族 EIV 校正思路可迁移至流行病学或经济学中带测量误差的 IV / proximal CI 设定。
- **关键技术**: `errors-in-variables model`, `exponential family distribution`, `attenuation bias correction`, `single-cell CRISPR screen`, `parallel statistical computing`
- **为什么对您有用**: 本文直接连接到因果推断中的测量误差与混杂校正问题（proximal CI / IV 的 negative control 设定常面临同类 measurement error 结构）。您武器库中的 semiparametric theory 与 M-estimation theory 可直接攻入其 EIV 模型的效率界与鲁棒性分析口子（当前方法仅给出 consistency，未讨论 semiparametric efficiency bound）。**中期可做**：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，推导该指数族 EIV 模型的 efficient influence function 与 debiased 估计器。

### 3. [10.1093/biostatistics/kxae007](https://doi.org/10.1093/biostatistics/kxae007) · [arXiv](https://arxiv.org/abs/2508.05567) — Functional support vector machine
- **作者**: Shanghong Xie, R Todd Ogden
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 1178-1194
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在函数数据（scalar-on-function）设定下，当标量响应与函数预测量之间存在非线性关系且函数预测量含较大测量误差时，传统线性/广义线性函数模型易受模型误设影响。本文提出将函数主成分分析（FPCA）与支持向量机（SVM）结合的 Functional SVM 方法，用于分类与回归：先通过 FPCA 提取函数预测量的主成分得分以降维并刻画连续性/高相关性，再将其作为特征输入 SVM 以捕捉非线性边界。模拟与两项真实数据（EEG 信号分类酒精依赖者、近红外光谱预测 glucobrassicin 浓度）表明，该方法在函数预测量测量误差较大时优势明显。对您可能有用：FPCA+SVM 的降维-非线性两步架构为函数数据下的非参数分类提供了实用工具，但理论性质（如收敛率、minimax 优化性）尚待建立。
- **关键技术**: `functional principal component analysis`, `support vector machine`, `scalar-on-function regression`, `kernel trick`, `measurement error in functional predictors`
- **为什么对您有用**: 本文属于函数数据非参数建模，连接到您 primary interest 中的 semiparametric & nonparametric theory 子方向。您 technical_arsenal 中的 minimax bounds for estimation problems 可用于攻本文的理论缺口：当前方法完全是算法+实证驱动，缺乏对 FPCA+SVM 两步 estimator 的收敛率或 minimax 优化性的分析，用 minimax 理论可验证其声称的测量误差较大时的优势是否对应某个 sharper rate。Follow-up 判断：**中期可做**——需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以建立两步（FPCA 估计 + SVM 优化）复合 estimator 的渐近理论。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1093/biostatistics/kxad031](https://doi.org/10.1093/biostatistics/kxad031) — Evaluating dynamic and predictive discrimination for recurrent event models: use of a time-dependent C-index
- **作者**: Jian Wang, Xinyang Jiang, Jing Ning
- **期刊/来源**: Biostatistics
- **机构**: The University of Texas MD Anderson Cancer Center
- **分类**: vol 25 · issue 4 · pp 1140-1155
- 相关性 5/10 · novelty: `application`
- **摘要**: 在复发事件数据的风险预测模型中，目标是评估模型在不同时间点的局部判别能力（time-dependent discriminative ability），而非仅依赖全局 C-index。作者将 time-dependent C-index 参数化为时间的函数，并基于 concordance 构造似然（concordance-based likelihood）进行估计与推断；方差估计采用 perturbation-resampling 方法。模拟与结直肠癌再住院数据的应用展示了该方法在捕捉模型判别能力动态变化上的实用性。对您可能有用：该文将判别指标参数化并构造似然进行推断的思路，与 semiparametric efficiency 及 M-estimation 理论有结构相似性，可作为 epidemiology 应用中模型评估的参考。
- **关键技术**: `time-dependent C-index`, `concordance-based likelihood`, `perturbation-resampling`, `recurrent event regression`, `dynamic discrimination`
- **为什么对您有用**: 本文属于 epidemiology 二级兴趣的应用工作，提供了复发事件数据判别指标的具体数据集与分析流程。从方法学看，concordance-based likelihood 的构造与推断属于 M-estimation 范畴，您 moderately_familiar 的 M-estimation theory 可直接审视其效率与一致性证明是否有改进空间。作为 gateway reading，本文数据集与模型设定清晰，值得花时间读全文以了解流行病学中复发事件模型评估的常见范式，但核心方法学 novelty 属应用层面，无深刻理论突破。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1093/biostatistics/kxae016](https://doi.org/10.1093/biostatistics/kxae016) — Fast matrix completion in epigenetic methylation studies with informative covariates
- **作者**: Mélina Ribaud, Aurélie Labbe, Khaled Fouda, Karim Oualkacha
- **期刊/来源**: Biostatistics
- **机构**: HEC Montréal · Université du Québec à Montréal
- **分类**: vol 25 · issue 4 · pp 1062-1078
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对DNA甲基化研究中缺失值填充问题，提出一种高效的协变量辅助矩阵补全方法。具体设定为：少量样本通过昂贵的全基因组亚硫酸氢盐测序（WGBS）获得高密度甲基化谱，大量样本通过低成本阵列技术获得低密度谱，目标是利用高密度信息与协变量预测低密度样本的缺失值。模型LMCC假设每个位点的甲基化向量可分解为固定协变量效应与一组潜在因子的线性组合，并对固定效应和潜在因子系数向量分别施加高斯过程先验，以刻画位点间的空间相关性。参数通过极大似然估计，算法计算复杂度可控。仿真表明，在缺失数据与解释变量相关时，引入协变量可显著提高填充精度；尤其当列数远大于行数时，模型效率优势明显。在两个真实甲基化数据集上，LMCC优于现有方法，并揭示了细胞类型、组织类型、年龄等协变量对预测的贡献。该方法展示了协变量信息在矩阵补全中的实用价值，您可将您武器库中的非参数统计和逆问题分析能力用于进一步理论化其预测误差界。
- **关键技术**: `Linear Model of Coregionalisation`, `matrix completion`, `Gaussian processes`, `covariate-informed imputation`, `high-density methylation reference`
- **为什么对您有用**: 本文直连您统计计算中的算法开发兴趣，提出一种融合协变量和空间相关性的矩阵补全新方法；您武器库中的非参数统计（如再生核希尔伯特空间理论）可用于严格分析其预测误差，逆问题视角可给出其正则化机理；中期可做：需先熟悉甲基化数据特有的缺失机制和噪声结构，但方法的计算框架本身可直接迁移至其他高维列数远大于行数的应用场景。

## 流行病学  *(epidemiology, 6 篇)*

### 1. [10.1093/biostatistics/kxad018](https://doi.org/10.1093/biostatistics/kxad018) — Identifying predictors of resilience to stressors in single-arm studies of pre–post change
- **作者**: Ravi Varadhan, Jiafeng Zhu, Karen Bandeen-Roche
- **期刊/来源**: Biostatistics
- **机构**: Johns Hopkins University · Sidney Kimmel Comprehensive Cancer Center · Northwestern University · Northwestern Medicine
- **分类**: vol 25 · issue 4 · pp 1094-1111
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在单臂 pre-post 研究设定下，目标是识别影响老年人压力恢复（resilience）的预测因子，estimand 为协变量对 pre-post 变化量的因果效应。核心挑战是 naive 回归 change-on-baseline 因数学耦合与回归均值（RTM）导致偏差。作者提出基于反事实对照组的校正估计量，仅需极弱分布假设，并将方法扩展至包含协变量与敏感性分析框架。模拟验证了估计量的有效性；TKR 队列（N=7239）实证表明，校正后基线功能与恢复不再显著相关，仅年龄与合并症数量稳健负向预测恢复。对您可能有用：本文为流行病学单臂 pre-post 设定提供了处理 RTM 偏差的识别与估计框架，可直接迁移至类似纵向因果推断问题。
- **关键技术**: `mathematical coupling correction`, `regression to the mean adjustment`, `counterfactual control group`, `sensitivity analysis for unobserved control`, `pre-post change estimation`
- **为什么对您有用**: 本文连接到流行病学应用因果推断的单臂 pre-post 设定，核心是 RTM 与数学耦合导致的识别偏差问题。您武器库中 identification theory in causal inference（moderately_familiar）可直接攻破其反事实对照组构建与敏感性分析的 formalization 口子，将其从 ad-hoc 校正提升为严格 semiparametric identification 框架。判断：立即可做——用 very_familiar 的 estimation theory in causal inference 重写其估计量并推导 influence function 与效率界。

### 2. [10.1093/biostatistics/kxae003](https://doi.org/10.1093/biostatistics/kxae003) · [arXiv](https://arxiv.org/abs/2401.04753) — Dynamic models augmented by hierarchical data: an application of estimating HIV epidemics at sub-national level
- **作者**: Bao Le, Xiaoyue Niu, Tim Brown, Jeffrey W Imai-Eaton
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 1049-1061
- 相关性 5/10 · novelty: `application`
- **摘要**: 在 HIV 亚国家级流行病学估计设定下，目标是利用动态模型同时估计 prevalence、incidence 与 mortality，但许多地区数据不足导致估计不稳定。核心难点在于直接在 HIV 动态模型内嵌入层级结构计算代价高昂且模型复杂。本文提出一种利用辅助数据（auxiliary data）将层级信息融入动态系统的简便方法，通过构造层级先验或惩罚项而非修改动态模型内部结构来跨区域借信息，从而在不增加计算负担的前提下实现多区域信息共享。理论层面，该方法改善了预测能力与不确定性评估（uncertainty assessment），实证应用于亚国家级 HIV 数据集展示了更窄的置信区间与更稳健的估计。对您可能有用：本文展示了流行病学应用中动态模型与层级借信息的计算-统计权衡策略，可作为 epidemiology 方向的应用案例阅读。
- **关键技术**: `dynamic epidemic model`, `hierarchical information borrowing`, `auxiliary data integration`, `sub-national prevalence estimation`, `uncertainty quantification`
- **为什么对您有用**: 本文属于 epidemiology 方向的 gateway reading：(1) 作为入门读物，它清晰展示了流行病学动态模型在亚国家级数据稀缺时的层级借信息策略，数据与模型结构交代清楚；(2) 武器库中的 M-estimation theory 与 software development 经验足以支撑研究者理解并复现其计算简化逻辑；(3) 值得花时间读全文以了解 HIV 数据集结构与动态模型在 epi 中的标准用法，但方法学 novelty 属于应用层面的计算简化（novelty_flag = application），对 primary interest 的理论推进有限。

### 3. [10.1093/biostatistics/kxad029](https://doi.org/10.1093/biostatistics/kxad029) — Signal detection statistics of adverse drug events in hierarchical structure for matched case–control data
- **作者**: Seok-Jae Heo, Sohee Jeong, Dagyeom Jung, Inkyung Jung
- **期刊/来源**: Biostatistics
- **机构**: Yonsei University
- **分类**: vol 25 · issue 4 · pp 1112-1121
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文关注药物不良反应（ADE）信号检测中的层次数据结构问题，采用树形扫描统计量进行数据挖掘。针对自发报告系统（SRS）中回顾性病例对照研究设计，现有Bernoulli模型未能恰当处理匹配对内部的依赖关系。作者提出三种基于匹配病例对照数据的信号检测统计量：McNemar检验、条件逻辑回归的Wald检验以及多项分布似然比检验。通过模拟研究，新方法在I类错误率、检验效能、敏感性和错误发现率方面均优于现有方法。最后利用韩国不良事件报告系统数据，检测抗高血压药物相关头晕不良反应的信号。该工作为流行病学中药物安全监测提供了更稳健的统计工具，对研究者关注的应用因果推断和流行病学数据集有参考价值。
- **关键技术**: `tree-based scan statistic`, `matched case-control design`, `McNemar's test`, `conditional logistic regression`, `likelihood ratio test`, `spontaneous reporting system (SRS)`
- **为什么对您有用**: 本文属于流行病学领域的应用因果推断工作，匹配病例对照设计和条件逻辑回归是研究者secondary interest中流行病学方向的标准分析工具。研究者武器库中的非参数统计和因果推断知识可用于理解该方法的假设与局限性，但本文属于应用方法创新，缺乏与核心理论（如高阶U统计、半参效率界）的直接深度连接。作为流行病学案例，值得阅读以了解药物安全监测中的实际数据结构和分析模式，但暂不可直接扩展至研究者已有的理论工作。

### 4. [10.1093/biostatistics/kxae005](https://doi.org/10.1093/biostatistics/kxae005) · [arXiv](https://arxiv.org/abs/2112.10978) — Tree-informed Bayesian multi-source domain adaptation: cross-population probabilistic cause-of-death assignment using verbal autopsy
- **作者**: Zhenke Wu, Zehang R Li, Irena Chen, Mengbing Li
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 1233-1253
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在 verbal autopsy (VA) 多源域迁移设定下，目标是跨人群估计 cause-specific mortality fractions (CSMF) 与个体死因分配；关键假设是人群间存在由预设根加权树编码的相似性结构，且各域内症状条件分布可用潜在类别模型刻画。方法核心是 logistic stick-breaking Gaussian diffusion process 先验沿树结构传播类别混合权重，配合 node-specific spike-and-slab 先验实现数据驱动的信息池化与域间差异自适应。推断采用 scalable variational Bayes 算法而非 MCMC，以应对高维多源数据。模拟与验证数据集显示，树引导的域迁移显著改善 CSMF 估计精度与个体 COD 分配准确率。对您可能有用：本文将树结构先验与 spike-and-slab 稀疏选择结合用于多源因果推断的信息融合，其域迁移框架与流行病学数据集对因果推断的 identification 与 estimation 有参考价值。
- **关键技术**: `logistic stick-breaking process`, `Gaussian diffusion tree prior`, `spike-and-slab variable selection`, `latent class model`, `variational Bayes inference`, `domain adaptation`
- **为什么对您有用**: 本文属于流行病学因果推断应用，提供了真实的 VA 多源死因数据集与树结构域迁移模型，对您 secondary interest 的流行病学应用有直接参考。(2) 您武器库中 very_familiar 的软件开发与 moderately_familiar 的 identification theory 可直接切入：树结构先验的稀疏选择机制可用 M-estimation 或 semiparametric 视角审视其 identification 条件，variational Bayes 的数值实现则落在 stat_computing 范畴。(3) **立即可做**：用 very_familiar 的软件开发能力复现其 variational Bayes 算法，并用 moderately_familiar 的 identification theory 检视其 latent class 模型在多源设定下的 identifiability 条件是否充分。

### 5. [10.1093/biostatistics/kxae017](https://doi.org/10.1093/biostatistics/kxae017) — <i>DifferentialRegulation</i> : a Bayesian hierarchical approach to identify differentially regulated genes
- **作者**: Simone Tiberi, Joël Meili, Peiying Cai, Charlotte Soneson, Dongze He, Hirak Sarkar et al.
- **期刊/来源**: Biostatistics
- **机构**: SIB Swiss Institute of Bioinformatics · University of Zurich · Accademia di Belle Arti di Bologna · University of Bologna · Friedrich Miescher Institute · University of Maryland, College Park · Princeton University · Harvard University 等
- **分类**: vol 25 · issue 4 · pp 1079-1093
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对RNA-seq数据中剪接与未剪接mRNA的联合分析问题，提出DifferentialRegulation——一种贝叶斯层次模型，用于发现不同实验条件（如健康vs疾病）下未剪接mRNA相对丰度的差异调控。该方法通过潜变量分配机制处理读段的多映射不确定性，将每条读段分配到基因/转录本及其剪接类型，从而量化估计不确定性。模型采用马尔可夫链蒙特卡洛进行后验推断，同时适用于bulk和单细胞RNA-seq数据。在多项基准测试中，DifferentialRegulation在敏感性和错误控制方面优于现有方法。本文还提供了Bioconductor R包的完整实现，便于统计实践者直接使用。对于您而言，本文可作为流行病学中基因表达差异分析的统计计算案例，展示贝叶斯层次模型在不确定性量化中的应用，但方法本身与您的主要兴趣领域（因果推断、高维统计等）无直接联系。
- **关键技术**: `Bayesian hierarchical model`, `latent variable allocation`, `multi-mapping read quantification`, `RNA velocity inference`, `Bioconductor R package`
- **为什么对您有用**: 本文属于流行病学方向的应用论文，处理疾病组间RNA-seq差异分析，与您次要兴趣中的流行病学应用匹配。您非常熟悉统计计算与软件开发，本文提供的R包实现可以作为开发统计工具的参考。但核心方法（贝叶斯层次潜变量模型）不在您当前武器库（非参数统计、U-统计、因果推断等）中，且需要额外学习RNA-seq量化背景知识，因此**暂不可做**——如需深入该方向，需先补充生物信息学与贝叶斯层次模型推断基础。全文阅读价值中等：作为入门级方法论文，可用于了解统计软件在生物信息学中的部署模式，但方法创新性有限。

### 6. [10.1093/biostatistics/kxae001](https://doi.org/10.1093/biostatistics/kxae001) — A Bayesian approach for investigating the pharmacogenetics of combination antiretroviral therapy in people with HIV
- **作者**: Wei Jin, Yang Ni, Amanda B Spence, Leah H Rubin, Yanxun Xu
- **期刊/来源**: Biostatistics
- **机构**: Johns Hopkins University · University of Baltimore · Texas A&M University · Georgetown University · Johns Hopkins Medicine · Behavioral Pharma (United States)
- **分类**: vol 25 · issue 4 · pp 1034-1048
- 相关性 3/10 · novelty: `application`
- **摘要**: 该文针对HIV患者联合抗逆转录病毒治疗（ART）的遗传药理学问题，提出一种贝叶斯方法以纵向分析药物组合与基因多态性对抑郁症状的交互效应。核心挑战在于FDA批准的30多种ART药物组合与大量遗传位点带来了高维交互建模困难。方法利用高斯过程复合核函数直接编码个体治疗历史，捕捉纵向联合用药的时变效应；并通过贝叶斯分类回归树（BCART）纳入个体异质性。模拟及妇女HIV队列研究（WIHS）实际数据表明该方法能有效识别影响抑郁症状的关键药物-基因交互，辅助个体化治疗决策。本文对您作为流行病学应用读者的价值在于：提供了纵向治疗历史建模的实用贝叶斯框架，其复合核函数思想可迁移至因果推断中时变处理效应的敏感性分析。
- **关键技术**: `Gaussian process with composite kernel`, `Bayesian classification and regression tree`, `longitudinal treatment history encoding`, `pharmacogenetics interaction modeling`, `Women's Interagency HIV Study`
- **为什么对您有用**: 该文直接对应您流行病学（应用型）的兴趣方向，使用真实HIV队列数据，并建模纵向药物组合效应。您武器库中的nonparametric statistics（very_familiar）可直接用于分析其高斯过程核函数的逼近性质；同时，其纵向治疗历史编码方法对您因果推断中时变处理效应的identification可能有借鉴意义。Follow-up粗判：立即可做——用非参视角理解其核函数选择；中期可做——如需将本文方法扩展至因果ATE估计，需先补充semiparametric theory（moderately_familiar）中的纵向因果推断技术。

## 其他  *(other, 3 篇)*

### 1. [10.1093/biostatistics/kxae024](https://doi.org/10.1093/biostatistics/kxae024) · [arXiv](https://arxiv.org/abs/2305.10360) — Neuroimaging meta regression for coordinate based meta analysis data with a spatial model
- **作者**: Yifan Yu, Rosario Pintos Lobo, Michael Cody Riedel, Katherine Bottenhorn, Angela R Laird, Thomas E Nichols
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 1210-1232
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出一种坐标基神经影像元回归（CBMR）框架，用于对功能磁共振成像（fMRI）研究中的激活焦点坐标进行元分析。目标是通过空间平滑模型估计脑激活强度函数，并考察研究层面协变量（如发表年份、样本量）的影响。方法采用样条参数化对脑激活的空间结构建模，并考虑四种随机模型（Poisson、二项、负二项、零膨胀）来描述焦点位置的随机变异性。模型通过广义线性模型框架拟合，使用迭代加权最小二乘估计，计算上高效。在20个真实元分析数据集上验证，进行了体素水平空间同质性检验，并与传统核方法和基于模型的方法比较。结果显示出较好的激活检测性能和协变量效应解释性。本文提供了可操作的软件实现，属于神经影像元分析的实用工具。
- **关键技术**: `coordinate-based meta-analysis`, `spline parameterization`, `spatial generalized linear model`, `random effects model`, `voxel-wise homogeneity test`
- **为什么对您有用**: 本文涉及空间统计建模和GLM框架，与您的高维非参方法有一定技术重叠（样条、随机效应），但主题完全在神经影像元分析领域，与您的主要兴趣（因果推断、高维U统计等）无直接连接。作为元分析方法学，其随机模型选择和计算策略可作为广义元回归的参考资料，但您的武器库中缺乏神经影像数据结构和空间相关性的专门工具，深层复现或改进需先补域知识。暂不可做。

### 2. [10.1093/biostatistics/kxae008](https://doi.org/10.1093/biostatistics/kxae008) · [arXiv](https://arxiv.org/abs/2305.09099) — Bayesian mixed model inference for genetic association under related samples with brain network phenotype
- **作者**: Xinyuan Tian, Yiting Wang, Selena Wang, Yi Zhao, Yize Zhao
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 4 · pp 1195-1209
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在影像遗传学设定下，目标是估计遗传变异对脑网络连接表型（network-variate phenotype）的效应，同时处理样本间亲属关系（pedigree/unknown relatedness）带来的相关性问题。作者提出 Bayesian network-response mixed-effect model，将随机效应建模为效应网络配置（effect network configurations），并施加 inter-network sparsity 与 intra-network shrinkage 以分离受风险基因影响的表型网络子结构。推断通过 MCMC 完成，实现不确定性量化；模拟与 Human Connectome Project 数据应用展示了方法的可行性。本文本质上是针对网络表型 + 家系结构的贝叶斯线性混合模型扩展，方法学 novelty 主要在先验构造与 MCMC 设计，对您可能有用之处在于其处理高维网络响应与相关样本的建模思路。
- **关键技术**: `Bayesian linear mixed model`, `network-variate outcome`, `inter-network sparsity prior`, `intra-network shrinkage prior`, `MCMC sampling`, `pedigree-relatedness structure`
- **为什么对您有用**: 本文处理的是网络表型（高维矩阵响应）+ 家系相关样本的贝叶斯混合模型，与您 primary interest 中的高维统计与 semiparametric theory 有场景重叠，但核心推断机器是贝叶斯先验 + MCMC，而非您熟悉的 minimax bound / influence function / U-statistic 路线。用您 very_familiar 的高维渐近理论或 moderately_familiar 的 M-estimation theory，可以尝试对这类网络响应混合模型给出频率派视角的收敛率或效率界分析，作为 follow-up 理论补充。**中期可做**：需先在 moderately_familiar 的 M-estimation theory 上长肌肉（特别是矩阵响应回归的渐近理论），才能切入频率派理论替代。

### 3. [10.1093/biostatistics/kxad033](https://doi.org/10.1093/biostatistics/kxad033) — Similarity-based multimodal regression
- **作者**: Andrew A Chen, Sarah M Weinstein, Azeez Adebimpe, Ruben C Gur, Raquel E Gur, Kathleen R Merikangas et al.
- **期刊/来源**: Biostatistics
- **机构**: Medical University of South Carolina · Temple University · Penn Center for AIDS Research · Lifespan · University of Pennsylvania · University of Pennsylvania Health System · National Institutes of Health · National Institute of Mental Health 等
- **分类**: vol 25 · issue 4 · pp 1122-1139
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文提出一种新的基于距离的多模态回归方法 SiMMR，旨在整合不同数据类型（如影像、移动健康数据等）以分析复杂人类表型。传统方法要求数据类型兼容或需大量预处理，而 SiMMR 通过距离轮廓同时回归多个模态，适用于矩阵值、向量值等多种结构的数据。方法核心是将各模态的距离矩阵纳入一个回归框架，通过置换检验进行推断，并比较了多种检验统计量的表现。模拟和两个真实数据（脑影像、纵向移动健康）分析表明，SiMMR 在样本量较小时仍能检测临床变量与多模态数据间的关联。该方法门槛较低，但缺乏与因果推断、高维 U 统计等核心方向的直接联系，对于流行病学应用（次要兴趣）可能有参考价值。
- **关键技术**: `distance matrix regression`, `multimodal fusion`, `permutation test`, `simulation study`, `longitudinal mobile health analysis`
- **为什么对您有用**: 本文属于多模态回归方法的应用，连接到次要兴趣中的流行病学（真实数据来自脑影像和移动健康队列）。武器库中的非参数统计和距离方法虽可理解思路，但方法本身不直接使用熟悉的 U 统计、因果推断或高维工具，短期内难以转化为自身科研产出。核心机器不在武器库里，暂不可做，但可作了解流行病学数据结构和回归思路的入门阅读。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

