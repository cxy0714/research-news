# Biostatistics — Vol 25  Issue 2  ·  2026-06-20

- 共 16 篇 · Biostatistics
- 目录核对 ✅ 16 篇全部抓到（对照 OpenAlex 17 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期论文大致聚成三条主线：因果推断与可移植性（含异质性、IV非线性、缺失数据与分位数效应）、纵向与生存数据的联合建模及计算（含协方差矩阵回归、贝叶斯INLA加速与生物标志物变异）、以及流行病学中的测量误差与偏差校正（含高维方差解释、多暴露插补与血清学推断）。此外，零散涉及高维网络提取与成分数据假设检验。

因果推断主线本期在多个细分设定下推进识别与估计。针对效应异质性，Tree-based subgroup与纵向TMLE结合以处理时依混杂与不对齐测量；针对可移植性，Systematically missing在RCT系统性缺失基线协变量时推导了目标人群ATE的IPW/g-formula/DR估计；针对非线性效应，DeLIVR通过回避不适定积分方程构建了两样本IV回归的非线性因果检验框架；针对生存分析，Quantile-varying AFT将g-formula标准化扩展至分位数尺度的边际效应估计。

纵向与联合建模主线本期侧重于结构扩展与计算加速。Longitudinal covariance regression在多层级广义线性模型下实现了低维半参数有效界与高维均匀最小二次损失界；Transformation perspective通过线性变换模型与多元正态相关结构统一了聚类数据的多类型边际响应，为边际处理效应估计提供解析框架；Fast INLA用集成嵌套拉普拉斯近似将多变量纵向-生存联合模型的高维随机效应积分转化为稀疏矩阵运算，突破了MCMC计算瓶颈；Modeling biomarker variability则在联合模型中用样条随机效应二次型刻画纵向波动对生存的预测。

对因果推断与半参数效率方向最贴的是Longitudinal covariance regression（低维有效界与高维损失界）、Systematically missing（可移植性下的DR估计与CAN性质）以及Transformation perspective（聚类数据的边际模型解析框架），适合优先看；关注高维与计算方法者可优先看Fast INLA与Identifying subnetwork（ℓ0惩罚提取）。

## 因果推断  *(causal_inference, 4 篇)*

### 1. [10.1093/biostatistics/kxad014](https://doi.org/10.1093/biostatistics/kxad014) — Tree-based subgroup discovery using electronic health record data: heterogeneity of treatment effects for DTG-containing therapies
- **作者**: Jiabei Yang, Ann W Mwangi, Rami Kantor, Issa J Dahabreh, Monicah Nyambura, Allison Delong et al.
- **期刊/来源**: Biostatistics
- **机构**: Brown University · Moi University · AMPATH · Harvard University
- **分类**: vol 25 · issue 2 · pp 323-335
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 这篇论文旨在利用电子健康记录（EHR）中的纵向数据，发现治疗效应异质性的亚组。主要挑战包括时依混杂、重复且时间上不对齐的协变量与结局测量、以及失访。作者将广义交互树算法与纵向目标最大似然估计（TMLE）相结合，开发了纵向亚组发现算法（subgroup discovery for longitudinal data algorithm）。该方法通过树结构识别协变量空间上的亚组，并在每个亚组内使用TMLE估计条件平均处理效应，同时利用交叉拟合控制过拟合。应用部分使用HIV患者的EHR数据，探索接受含Dolutegravir（DTG）的抗逆转录病毒治疗时体重增加风险较高的亚组。该算法为纵向因果推断中的异质性分析提供了可复用的工具，与您主要兴趣中的因果推断（尤其是纵向数据与异质性处理效应）直接对接。
- **关键技术**: `generalized interaction tree algorithm`, `longitudinal targeted maximum likelihood estimation (TMLE)`, `cross-fitting`, `time-varying confounding adjustment`, `subgroup discovery`
- **为什么对您有用**: 论文直接涉及纵向数据中的处理效应异质性分析，属于因果推断的核心子方向。您熟悉的因果推断估计理论（如TMLE的渐近性质和交叉拟合技巧）可以立即用于评估该算法的收敛行为或提出改进。鉴于您对非参数统计和因果推断软件开发的熟练程度，该工作可立即可做：复现算法、扩展至其他纵向设定或结合更灵活的树模型。

### 2. [10.1093/biostatistics/kxad006](https://doi.org/10.1093/biostatistics/kxad006) · [arXiv](https://arxiv.org/abs/2205.00610) — Systematically missing data in causally interpretable meta-analysis
- **作者**: Jon A Steingrimsson, David H Barker, Ruofan Bie, Issa J Dahabreh
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 2 · pp 289-305
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在因果可解释meta-analysis框架下，目标是估计目标人群的ATE，当部分RCT系统性缺失某些基线协变量（即某些试验中所有参与者均缺失该协变量）时，研究identification与估计问题。基于可识别性结果，提出三种ATE估计器（IPW、g-formula、DR），并证明其在常规正则条件下为n^{-1/2}-CAN。模拟显示有限样本表现良好；实证分析结合NLST/PLCO肺癌筛查试验与NHANES目标人群数据，进一步将方法扩展至处理复杂抽样设计的survey weight与聚类。对您可能有用：本文将系统性缺失数据结构引入transportability/generalizability的因果推断设定，提供了完整的identification与semiparametric估计理论。
- **关键技术**: `causally interpretable meta-analysis`, `systematically missing data identification`, `transportability / generalizability`, `doubly robust estimation`, `survey sampling weights integration`
- **为什么对您有用**: 本文直接连接因果推断中的transportability/generalizability子方向，处理RCT到目标人群外推时协变量系统性缺失的identification与估计。您武器库中semiparametric theory与M-estimation theory（moderately_familiar）可直接切入分析其DR估计器的效率界与influence function，判断是否达到semiparametric efficiency bound。**中期可做**：需先在moderately_familiar的identification theory上长肌肉，以厘清systematically missing下的identifiability条件与no-unmeasured-confounding假设的交互限制，之后可推导更优的one-step/TMLE估计器。

### 3. [10.1093/biostatistics/kxac051](https://doi.org/10.1093/biostatistics/kxac051) — DeLIVR: a deep learning approach to IV regression for testing nonlinear causal effects in transcriptome-wide association studies
- **作者**: Ruoyu He, Mingyang Liu, Zhaotong Lin, Zhong Zhuang, Xiaotong Shen, Wei Pan
- **期刊/来源**: Biostatistics
- **机构**: University of Minnesota
- **分类**: vol 25 · issue 2 · pp 468-485
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在两样本 IV 回归的 TWAS 设定下，目标是检验基因表达对复杂性状的非线性因果效应，IV 假设与标准 TWAS 相同。现有 TWAS-L 仅建模线性效应，TWAS-LQ 建模线性+二次效应但参数化限制灵活性；DeepIV 非参数建模非线性效应但需求解不适定积分方程（Monte Carlo 近似），导致计算慢且不稳定，且缺乏假设检验框架。本文提出 DeLIVR，通过估计一个相关但不同的目标函数回避不适定逆问题，并构建了针对非线性因果效应的假设检验框架。模拟表明 DeLIVR 比 DeepIV 更快更稳；在 GTEx 与 UK Biobank 数据上，DeLIVR 对 HDL/LDL 各多检出 8/7 个非线性关联基因（如 BUD13、SLC44A2），均被线性与二次方法遗漏。对您有用：本文将 IV 回归的非参数估计与假设检验结合，直接触及 IV 方法与 hypothesis testing 两个 primary interest。
- **关键技术**: `instrumental variable regression`, `nonparametric causal effect testing`, `deep learning for IV`, `two-sample TWAS`, `ill-posed inverse problem avoidance`, `transcriptome-wide association study`
- **为什么对您有用**: 本文直接连接 IV 方法与 hypothesis testing 两个 primary interest 子方向，在两样本 IV 设定下实现了非线性因果效应的检验，填补了 DeepIV 缺乏 inference 的空白。从 technical_arsenal 看，本文的 IV identification 与 M-estimation 理论属于 moderately_familiar，可用来审视其目标函数重构如何改变 influence function 与检验的 asymptotic null distribution。Follow-up 判断：**中期可做**——需先在 moderately_familiar 的 semiparametric theory / M-estimation 上长肌肉，以严格推导 DeLIVR 估计量的 asymptotic distribution 与 power 性质，并评估其是否达到 semiparametric efficiency bound。

### 4. [10.1093/biostatistics/kxac052](https://doi.org/10.1093/biostatistics/kxac052) · [arXiv](https://arxiv.org/abs/2301.03057) — Characterizing quantile-varying covariate effects under the accelerated failure time model
- **作者**: Harrison T Reeder, Kyu Ha Lee, Sebastien Haneuse
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 2 · pp 449-467
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文在加速失效时间（AFT）模型框架下，提出了一种刻画协变量效应随生存时间分位数变化的通用方法。传统AFT假设协变量效应在所有分位数上为常数乘法偏移，无法捕捉异质性效应。作者将灵活回归结构嵌入AFT模型，推导出分位数尺度上可解释的效应公式。采用基于g-formula的回归标准化方案，同时估计协变量条件效应和暴露的边际效应。估计和不确定性量化通过用户友好的贝叶斯方法实现，能处理左截断和复杂删失。模拟和阿尔茨海默病研究实例表明方法有效。对您有用：该方法将因果推断中的g-formula标准化扩展到生存分析分位数效应，连接您的causal inference兴趣中的标准化估计和marginal effect估计。
- **关键技术**: `accelerated failure time model`, `quantile-varying effects`, `g-formula standardization`, `Bayesian survival analysis`, `regression standardization`
- **为什么对您有用**: (1) 直接连接causal inference兴趣中的g-formula标准化方法，用于估计分位数上的边际效应。(2) 您非常熟悉的'估计理论在因果推断中的应用'可直接用于分析该标准化方案的渐近性质（如g-formula的double robustness潜力）。(3) 立即可做：用very_familiar的causal estimation理论和nonparametric工具，可以设计和分析该模型下g-formula的double robust估计量。

## 非参数 / 半参数  *(nonparam_semipara, 2 篇)*

### 1. [10.1093/biostatistics/kxac045](https://doi.org/10.1093/biostatistics/kxac045) · [arXiv](https://arxiv.org/abs/2202.04553) — Longitudinal regression of covariance matrix outcomes
- **作者**: Yi Zhao, Brian S Caffo, Xi Luo
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 2 · pp 385-401
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 本文研究纵向协方差矩阵结果的回归问题，设定为多层级广义线性模型，将协方差矩阵回归到时变协变量上，同时识别协变量关联成分、估计回归系数并刻画矩阵的个体内变异。低维情形下通过最大化近似层级似然提出最优估计量，证明其渐近一致且协方差矩阵估计量达到半参数有效界；高维情形下提出同类估计量，证明其在所有单位阵与样本协方差矩阵的线性组合中达到均匀最小二次损失。模拟显示该方法在成分识别与参数估计上表现良好，应用于ADNI纵向fMRI数据识别了不同疾病阶段的性别差异脑网络。对您可能有用：高维协方差估计的均匀最小二次损失界与低维有效界结果，可直接对接您在效率理论与高维渐近方面的兴趣。
- **关键技术**: `multilevel generalized linear model`, `hierarchical-likelihood approximation`, `uniformly minimum quadratic loss`, `semiparametric efficiency bound`, `covariance matrix regression`, `longitudinal fMRI analysis`
- **为什么对您有用**: 本文直接连接效率理论子方向：低维下协方差矩阵估计达到半参数有效界，高维下达到均匀最小二次损失，这为您的 minimax bound 与效率理论武器提供了具体应用场景。用您 very_familiar 的高维渐近与 minimax bound 工具，可验证其高维最小二次损失界是否紧、是否可扩展到更一般的损失函数或随机矩阵谱域。立即可做：用 minimax bound 武器检查其声称的 sharper rate 是否紧，并探索该框架在 RMT Marchenko-Pastur 设定下的推广。

### 2. [10.1093/biostatistics/kxac048](https://doi.org/10.1093/biostatistics/kxac048) · [arXiv](https://arxiv.org/abs/1910.09219) — A transformation perspective on marginal and conditional models
- **作者**: Luisa Barbanti, Torsten Hothorn
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 2 · pp 402-428
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对聚类观测数据（如多中心试验、纵向调查）提出联合模型，边际分布由线性变换模型刻画，相关结构由多元正态分布建模，并给出边际分布的解析表达式。该框架涵盖多种响应类型（连续、二元、有序、生存），通过睡眠剥夺数据集（反应时间）、趾甲数据（边际优势比）及两个临床试验（疼痛VAS比例优势模型、直肠癌无病生存边际风险比）展示实用性。经验评估中，新方法与GEE（二元响应）和条件混合模型（连续响应）对比，性能相当。模型在R包tram中实现，便于推广。对您的价值：可直接用于纵向因果推断中的边际处理效应估计（与您的纵向兴趣一致），且R实现为您的统计计算兴趣提供了现成工具。
- **关键技术**: `linear transformation model`, `multivariate normal copula`, `marginal likelihood`, `proportional-odds model`, `survival analysis (Weibull, Cox)`, `R package tram`
- **为什么对您有用**: 直接对接纵向因果推断中的边际效应估计问题（您的primary interest），同时其R包实现满足您的统计计算兴趣。您可以用very_familiar的nonparametric statistics分析变换模型的半参数灵活性，并考虑将其嵌入现有因果推断框架。立即可做：只需在您熟悉的非参数统计和软件工具基础上调整，即可在纵向数据中应用此模型。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1093/biostatistics/kxad008](https://doi.org/10.1093/biostatistics/kxad008) — Differential transcript usage analysis incorporating quantification uncertainty via compositional measurement error regression modeling
- **作者**: Amber M Young, Scott Van Buren, Naim U Rashid
- **期刊/来源**: Biostatistics
- **机构**: University of North Carolina at Chapel Hill
- **分类**: vol 25 · issue 2 · pp 559-576
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究差异转录本使用（DTU）检测问题，目标是在不同条件下识别同一基因内多个转录本相对丰度的变化，采用成分回归（compositional regression）直接对转录本相对丰度建模。核心方法 CompDTU 利用快速矩阵计算，可高效处理大样本，并支持多个分类或连续协变量的检验与调整。扩展方法 CompDTUme 进一步融入RNA-seq表达定量中的量化不确定性，通过利用常见定量工具的输出（如bootstrap或后验样本）来校正测量误差。模拟研究表明 CompDTU 相比现有方法具有更好的敏感性和更低的假阳性率，而 CompDTUme 在高不确定性基因上进一步提升了性能，同时保持了速度与可扩展性。在TCGA乳腺癌浸润癌数据集上，新方法大幅缩短了计算时间，并检测到多个亚型间显著DTU的新基因。该方法通过成分回归处理测量误差的思路，与您在因果推断中处理测量误差的敏感性分析有方法学上的相通之处，而其快速矩阵计算策略也值得您在高阶U统计量计算中借鉴。
- **关键技术**: `compositional regression`, `measurement error modeling`, `RNA-seq quantification uncertainty`, `fast matrix-based computation`, `hypothesis testing for DTU`
- **为什么对您有用**: 本文与您的主要兴趣点在假设检验（DTU检测）和统计计算（快速矩阵算法）上有直接交集。您非常熟悉的M估计理论可用于分析成分回归的渐近性质，而软件开发和矩阵计算技能可帮助复现或改进CompDTUme的实现效率。**立即可做**：利用您擅长的M估计框架推导该方法的半参效率界，或基于已有软件经验开发更通用的成分回归工具。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1093/biostatistics/kxad019](https://doi.org/10.1093/biostatistics/kxad019) · [arXiv](https://arxiv.org/abs/2203.06256) — Fast and flexible inference for joint models of multivariate longitudinal and survival data using integrated nested Laplace approximations
- **作者**: Denis Rustand, Janet van Niekerk, Elias Teixeira Krainski, Håvard Rue, Cécile Proust-Lima
- **期刊/来源**: Biostatistics
- **机构**: King Abdullah University of Science and Technology · Université de Bordeaux · Inserm · Bordeaux Population Health
- **分类**: vol 25 · issue 2 · pp 429-448
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 该论文针对多变量纵向数据与生存数据的联合建模问题，提出一种基于集成嵌套拉普拉斯近似（INLA）的贝叶斯推断框架，解决了传统方法因高维随机效应积分导致的计算瓶颈。通过R-INLA包实现，算法将多维积分转化为高效的稀疏矩阵运算，极大缩短了估计时间，同时降低了参数估计的波动性。模拟研究显示，与MCMC等方法相比，INLA在保持精度的前提下显著加速。实际应用中，论文分析了原发性胆汁性胆管炎临床试验数据，包含5个不同分布类型的纵向标志物（连续、计数、二元）和16个随机效应，并考虑了死亡与移植的竞争风险。作者证明INLA能够处理此类复杂结构，且结果可靠。对于统计计算和流行病学研究，本文展示了贝叶斯近似方法在高维随机效应模型中的实用价值。
- **关键技术**: `Integrated Nested Laplace Approximation (INLA)`, `Joint models for longitudinal and survival data`, `Bayesian inference`, `R-INLA package`, `Competing risks`
- **为什么对您有用**: 该论文是流行病学联合模型分析的一篇良好入门读物：它清晰阐述了模型结构（纵向子模型+生存子模型通过随机效应关联）和计算策略（INLA的拉普拉斯近似），并提供了R-INLA的实际代码路径。研究者具备统计软件开发和渐近理论背景，能够快速把握算法的计算逻辑；但若要深入INLA的误差分析与收敛性质，需额外补充贝叶斯计算中的拉普拉斯近似知识。整体而言，本文值得花时间阅读，有助于拓展研究者对现代统计计算工具（INLA）在健康科学复杂数据中应用的理解。

## 流行病学  *(epidemiology, 7 篇)*

### 1. [10.1093/biostatistics/kxad001](https://doi.org/10.1093/biostatistics/kxad001) — Estimating the overall fraction of phenotypic variance attributed to high-dimensional predictors measured with error
- **作者**: Soutrik Mandal, Do Hyun Kim, Xing Hua, Shilan Li, Jianxin Shi
- **期刊/来源**: Biostatistics
- **机构**: National Cancer Institute · Division of Cancer Epidemiology and Genetics · University of California, Los Angeles · Fred Hutch Cancer Center
- **分类**: vol 25 · issue 2 · pp 486-503
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在高维前瞻性基因组研究（如 DNA 甲基化、宏基因组）设定下，目标是估计高维变量解释表型方差的总比例（OFPV，类似 GWAS 的 heritability），核心假设为测量误差方差在因果与非因果变量间同分布。现有 GWAS 方法直接套用会因忽略测量误差导致 OFPV 严重低估；本文证明渐进衰减因子等于所有基因组变量的平均组内相关系数（ICC），可通过有重复测量的 pilot study 估计。方法在 American Gut Project 数据集上应用于肠道微生物对 BMI 及过敏性状的方差贡献估计，并证明测量误差对两性状效应大小相关性的估计不产生实质性偏差。对您可能有用：本文提供了流行病学高维数据中 heritability-type estimand 的测量误差校正框架，直接连接到 epidemiology secondary interest 的应用因果工作。
- **关键技术**: `attenuation factor correction`, `intraclass correlation coefficient (ICC)`, `high-dimensional variance component estimation`, `measurement error modeling`, `heritability estimation`
- **为什么对您有用**: 本文直接连接到 epidemiology secondary interest 的高维基因组/微生物组数据集与方差解释（heritability-type）估计。从 technical_arsenal 角度，您可以用 high-dimensional asymptotics（very_familiar）审视其渐进衰减因子在更一般误差分布假设下的鲁棒性，或用 minimax bounds（very_familiar）验证 OFPV 估计率是否可达紧界。Follow-up 判断：**立即可做**——用您熟悉的高维渐进工具即可对当前同分布误差假设的必要性进行理论拓展。

### 2. [10.1093/biostatistics/kxad016](https://doi.org/10.1093/biostatistics/kxad016) — A joint Bayesian hierarchical model for estimating SARS-CoV-2 genomic and subgenomic RNA viral dynamics and seroconversion
- **作者**: Tracy Q Dong, Elizabeth R Brown
- **期刊/来源**: Biostatistics
- **机构**: Fred Hutch Cancer Center · University of Washington
- **分类**: vol 25 · issue 2 · pp 336-353
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对SARS-CoV-2的病毒动力学和自然免疫问题，提出一个贝叶斯分层模型联合估计基因组RNA病毒载量、亚基因组RNA病毒载量（反映活跃病毒复制）以及血清转化率与时机。模型显式刻画两种病毒载量之间的动态关系和相关性结构，并允许在病毒载量与抗体数据之间借用信息，同时识别与病毒载量特征及血清转化倾向相关的潜在协变量。通过COVID-19暴露后预防研究数据验证模型表现，并实施交叉验证展示其利用仅有基因组RNA数据的人群插补亚基因组RNA轨迹的能力。该方法是现有贝叶斯纵向模型在传染病数据上的直接应用，方法学本身的新颖性有限，但提供了一个完整的、可复现的数据分析流程。作为流行病学应用，这篇论文对您有参考价值：可以让您快速了解纵向病毒动态数据集的典型结构、缺失机制和分析挑战，适合作为进入纵向流行病学应用的入门读物。
- **关键技术**: `Bayesian hierarchical model`, `joint modeling`, `viral dynamics`, `seroconversion`, `cross-validation`
- **为什么对您有用**: 这是一篇流行病学的应用论文，以真实COVID-19数据演示了贝叶斯分层模型如何联合估计病毒RNA动态和血清转化，属于您secondary interest中的流行病学方向。您的武器库中'软件发展'一项可用于复现和扩展其MCMC实现，'非参数统计'知识可用于评价其模型假设的稳健性。作为入门读物，它值得您花时间读全文，以把握纵向传染病数据在实际分析中的关键处理步骤和建模选择。

### 3. [10.1093/biostatistics/kxad011](https://doi.org/10.1093/biostatistics/kxad011) — Multiple imputation of more than one environmental exposure with nondifferential measurement error
- **作者**: Yuanzhi Yu, Roderick J Little, Matthew Perzanowski, Qixuan Chen
- **期刊/来源**: Biostatistics
- **机构**: Columbia University · University of Michigan
- **分类**: vol 25 · issue 2 · pp 306-322
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在环境流行病学研究中，多个暴露变量常带有测量误差，但现有校正方法多针对单一暴露。本文提出有约束的链式方程多重插补（CEMI）方法，结合外部或内部校准样本（同时含有真实和错误测量值）与主研究数据（仅含错误测量值），在校准插补模型中施加强非差分测量误差的约束。方法还可处理主研究中暴露变量低于检测限的情况。方差估计采用bootstrap结合两次插补。模拟结果显示，CEMI相比忽略测量误差、经典校准和回归预测等方法，偏差更小且置信区间覆盖率接近名义水平。应用至纽约哮喘和过敏研究，分析多种室内过敏原浓度与哮喘儿童呼出气一氧化氮水平的关联。CEMI可通过R包mice和bootImpute实现约束矩阵。
- **关键技术**: `constrained chained equations multiple imputation`, `nondifferential measurement error`, `calibration sample`, `bootstrap variance estimation`, `R mice package`
- **为什么对您有用**: （1）本文对多暴露测量误差的校准多重插补问题阐述清晰，数据生成和假设机制较为透明，适合作为统计学家进入流行病学统计应用的入门文献。（2）您武器库中的“估计理论在因果推断中的应用”和“软件实现经验”可直接协助理解约束构造与代码实现，支撑您涉足这一应用方向。（3）方法具有一定的创新性（约束插补）并经过真实数据验证，值得花费时间阅读全文以掌握测量误差校正的建模思路与实际操作。

### 4. [10.1093/biostatistics/kxad004](https://doi.org/10.1093/biostatistics/kxad004) — Multi-trait analysis of gene-by-environment interactions in large-scale genetic studies
- **作者**: Lan Luo, Devan V Mehrotra, Judong Shen, Zheng-Zheng Tang
- **期刊/来源**: Biostatistics
- **机构**: Decision Sciences (United States) · University of Wisconsin–Madison
- **分类**: vol 25 · issue 2 · pp 504-520
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对大规模遗传研究中的基因-环境交互作用（GEI）分析提出多性状分析框架MTAGEI。GEI分析面临统计效力不足的挑战，而大型联合体数据集（如UK Biobank）为克服此问题提供了机会。MTAGEI首先在多种环境条件下生成多性状的遗传关联汇总统计量，然后通过汇总统计量的整合来实现GEI分析，从而在多个性状和变异上聚合信号，提升效力。该方法还通过整合互补检验实现鲁棒性，以适应广泛的遗传架构。通过模拟研究和UK Biobank全外显子测序数据的实际分析，MTAGEI优于现有基于单性状的GEI检验。该方法对遗传流行病学中交互作用分析有直接贡献，可作为流行病学应用的有效工具。对于您的流行病学次级兴趣，该论文提供了清晰的方法框架和大规模数据实践参照，便于入门。
- **关键技术**: `meta-analysis of summary statistics`, `gene-environment interaction test`, `multi-trait aggregation`, `UK Biobank whole exome sequencing`, `robustness through combined tests`
- **为什么对您有用**: 本文属于流行病学领域的应用方法工作（secondary interest），聚焦于大规模遗传研究中基因-环境交互作用（GEI）的统计检验问题，与该方向的方法学发展密切相关。您武器库中'high-dimensional asymptotics'（very_familiar）可用于理解其在大规模汇总统计量整合中的渐近行为，'software development'（very_familiar）有助于复现或扩展MTAGEI框架。作为流行病学入门读物，本文方法叙述清楚，数据描述详实（UK Biobank），值得阅读全文。

### 5. [10.1093/biostatistics/kxad003](https://doi.org/10.1093/biostatistics/kxad003) — A Bayesian approach to estimating COVID-19 incidence and infection fatality rates
- **作者**: Justin J Slater, Aiyush Bansal, Harlan Campbell, Jeffrey S Rosenthal, Paul Gustafson, Patrick E Brown
- **期刊/来源**: Biostatistics
- **机构**: University of Toronto · St. Michael's Hospital · Centre for Global Health Research · University of British Columbia
- **分类**: vol 25 · issue 2 · pp 354-384
- 相关性 5/10 · novelty: `application`
- **摘要**: 在 COVID-19 流行病学设定下，目标 estimand 为累积发病率与感染病死率（IFR），核心挑战是偏好检测导致的偏差与不完全死亡数据带来的不确定性。本文提出在近似贝叶斯框架下，用多变量混合模型处理连续型血清学滴度值以识别既往感染状态，避免了先前方法对连续指标的离散化截断信息损失。结合事后分层校正选择偏差，并将感染人数估计的不确定性与死亡数据缺失的不确定性同时纳入 IFR 的贝叶斯推断。方法应用于加拿大 ABC 队列数据，给出了校正后的发病率与 IFR 估计。对您可能有用：本文展示了流行病学队列数据中处理连续代理变量与选择偏差的贝叶斯混合模型策略，可作为 epi 领域应用因果/半参数方法的入门数据场景。
- **关键技术**: `multivariate mixture model`, `approximate Bayesian inference`, `post-stratification`, `serosurvey titer values`, `infection fatality rate estimation`
- **为什么对您有用**: (1) 连接 epidemiology secondary interest，具体是血清学调查数据中用连续代理变量识别感染状态的设定；(2) 武器库中 moderately_familiar 的 identification theory in causal inference 可切入本文的偏好检测偏差校正问题——将 post-stratification 视为一种粗粒度的 IPW/selection-bias identification，可尝试用 semiparametric efficiency bound 替代其贝叶斯框架以获得更优的 rate；(3) **中期可做**：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，才能将本文的混合模型 identification 转化为正式的 semiparametric proximal/selection model 并推导 efficient influence function。

### 6. [10.1093/biostatistics/kxad009](https://doi.org/10.1093/biostatistics/kxad009) — Modeling biomarker variability in joint analysis of longitudinal and time-to-event data
- **作者**: Chunyu Wang, Jiaming Shen, Christiana Charalambous, Jianxin Pan
- **期刊/来源**: Biostatistics
- **机构**: University of Cambridge · University of Manchester · MRC Biostatistics Unit · Beijing Normal-Hong Kong Baptist University · Beijing Normal University
- **分类**: vol 25 · issue 2 · pp 577-596
- 相关性 4/10 · novelty: `minor`
- **摘要**: 本文研究纵向生物标志物变异性对生存时间的预测作用，提出一种新的生物变异度量：在混合效应模型中用三次样条拟合个体轨迹，将变异定义为随机效应的二次型。纵向子模型采用线性混合模型，生存子模型为Cox模型，同时纳入当前轨迹水平和波动性作为协变量，构成联合建模框架。作者推导了MLE的渐近性质，估计采用EM算法，E步使用完全指数拉普拉斯近似以降低高维随机效应的计算负担。模拟显示该方法优于两阶段法和不考虑变异性的简单联合模型。实证部分用MRC老年试验数据研究收缩压变异性对心血管事件的影响。对您而言，这是一篇流行病学领域的应用方法论文，展示了联合模型如何处理生物标志物波动的实际问题，但方法学创新幅度有限，可作为入门级阅读了解该领域常规技术（混合模型、Cox、EM）的整合套路。
- **关键技术**: `joint modeling`, `mixed-effects model`, `cubic splines`, `Cox model`, `EM algorithm with Laplace approximation`, `maximum likelihood with asymptotics`
- **为什么对您有用**: 本文属于流行病学应用（secondary interest），使用的联合模型是纵向数据与时间事件数据结合的标准框架。作为入门读物，它清晰地展示了如何将生物变异度量（二次型）嵌入混合模型并采用EM+拉普拉斯估计，数据结构和模型假设交代完整（MRC老年试验），适合想了解流行病学分析中联合建模应用的统计学家。不过，方法学工具（混合模型、Cox、EM）是您的very_familiar武器库中的常规内容，无需额外修炼即可理解，但本文并未提出与您核心兴趣（因果推断、高维U统计、效率理论）直接对接的问题或新方法，阅读价值中等，若时间充裕可浏览。

### 7. [10.1093/biostatistics/kxad005](https://doi.org/10.1093/biostatistics/kxad005) — Cohort-based smoothing methods for age-specific contact rates
- **作者**: Yannick Vandendijck, Oswaldo Gressani, Christel Faes, Carlo G Camarda, Niel Hens
- **期刊/来源**: Biostatistics
- **机构**: Hasselt University · Institut national d'études démographiques · University of Antwerp
- **分类**: vol 25 · issue 2 · pp 521-540
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文关注传染病建模中年龄特异性接触率的估计问题，利用接触调查数据（如POLYMOD）构建社会接触矩阵。传统方法采用二维平滑（受访者年龄×接触者年龄），而本文提出沿矩阵对角线（含所有子对角线）引入平滑约束，称为队列视角平滑，理由是接触行为随年龄平滑变化。两种实现方式：重排对角线分量或重排惩罚矩阵。参数估计通过约束惩罚迭代重加权最小二乘法在似然框架下完成。模拟表明队列平滑在偏差和均方误差上优于传统方法。最后应用于比利时POLYMOD数据，代码公开可复现。本文为您提供了一个流行病学数据分析的典型示例，展示了领域知识如何引导光滑约束的设计。
- **关键技术**: `Penalized likelihood`, `Constrained iterative reweighted least squares`, `Bivariate smoothing`, `Cohort smoothing`, `Social contact matrix`
- **为什么对您有用**: 本文是流行病学应用数据的良好入门读物：清晰展示了社会接触矩阵的估计流程与数据特点，方法（惩罚光滑序列）对统计学家友好。您非常熟悉的非参数光滑理论可直接用于理解其光滑机制和收敛性，但当前无需动手复现。值得花时间读全文以熟悉流行病学建模的数据结构，拓展应用视野。

## 其他  *(other, 1 篇)*

### 1. [10.1093/biostatistics/kxad007](https://doi.org/10.1093/biostatistics/kxad007) — Identifying covariate-related subnetworks for whole-brain connectome analysis
- **作者**: Shuo Chen, Yuan Zhang, Qiong Wu, Chuan Bi, Peter Kochunov, L Elliot Hong
- **期刊/来源**: Biostatistics
- **机构**: University of Maryland, Baltimore · The Ohio State University · University of Pennsylvania
- **分类**: vol 25 · issue 2 · pp 541-558
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 全脑连接组数据分析中，需要识别与协变量（如疾病状态）相关的子网络，但相关边及其拓扑结构未知。由于假阳性噪声和边组合可能性极多，任务具有挑战性。本文提出以多元边变量为结果的新统计方法，从图论与组合数学角度推导协变量相关子网络的图性质。采用 ℓ0 范数惩罚开发高效算法，从全脑连接组中精确提取子网络。通过模拟研究验证性能，并应用于两个独立精神分裂症静息态 fMRI 数据集，获得高度可复现的疾病相关子网络。对您可能有用：本文涉及高维网络推断与 ℓ0 正则化，与您的高维统计兴趣有细微关联，但核心方向并非因果推断或半参理论。
- **关键技术**: `ℓ0 norm penalized estimation`, `graph theory for subnetworks`, `combinatorial optimization`, `efficient algorithm for whole-brain connectome`
- **为什么对您有用**: 具体兴趣子方向：高维统计中的网络推断。可用 very_familiar 中的 high-dimensional asymptotics 和 minimax bounds 分析 ℓ0 惩罚估计的选择一致性，但当前武器库对图网络推断的特殊结构（如边组合性质）覆盖不足。中期可做：需在 high-dimensional asymptotics 基础上学习图网络选择一致性理论。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

