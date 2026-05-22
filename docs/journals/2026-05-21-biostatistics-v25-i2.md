# Biostatistics — Vol 25  Issue 2  ·  2026-05-21

- 共 16 篇 · Biostatistics

## 因果推断  *(causal_inference, 3 篇)*

### 1. [10.1093/biostatistics/kxad006](https://doi.org/10.1093/biostatistics/kxad006) — Systematically missing data in causally interpretable meta-analysis
- **作者**: Jon A Steingrimsson, David H Barker, Ruofan Bie, Issa J Dahabreh
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 2 · pp 289-305
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在因果可解释的元分析（将RCT结果外推至目标人群）设定下，本文研究当部分试验系统性缺失某些基线协变量（即某些试验中全体参与者的协变量均缺失）时，目标人群潜在结果均值和平均因果效应（ATE）的识别与估计问题。作者在系统缺失机制下给出了反事实结果的识别条件，并提出了三种ATE估计量（基于IPW、结果回归及双重稳健方法）。渐近性质分析表明这些估计量具有 n^{-1/2}-相合性和渐近正态性，且双重稳健估计量在模型正确指定时可达半参数有效界。针对NHANES复杂抽样设计，方法进一步扩展以纳入调查权重和聚类结构。模拟显示有限样本表现良好；实证分析结合了肺癌筛查试验与NHANES数据。对您有用：该文处理了因果推断中数据融合与外推性（generalizability）的系统性缺失问题，其识别策略与DR估计量的渐近分析直接关联您对因果识别与半参数效率理论的兴趣，同时NHANES的流行病学应用也具数据集参考价值。
- **关键技术**: `causally interpretable meta-analysis`, `systematically missing data`, `transportability and generalizability`, `doubly robust estimation`, `complex survey weighting`
- **为什么对您有用**: 直击因果推断中数据融合与外推性设定下的系统性缺失难题，其识别结果与DR估计量的渐近性质分析对您关注的因果识别与半参数效率理论有直接参考价值；同时NHANES流行病学数据的应用也契合您的次级兴趣。

### 2. [10.1093/biostatistics/kxad014](https://doi.org/10.1093/biostatistics/kxad014) — Tree-based subgroup discovery using electronic health record data: heterogeneity of treatment effects for DTG-containing therapies
- **作者**: Jiabei Yang, Ann W Mwangi, Rami Kantor, Issa J Dahabreh, Monicah Nyambura, Allison Delong et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 2 · pp 323-335
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在纵向电子病历(EHR)数据下，针对时变混杂、重复测量和非对齐时间点等挑战，本文目标是发现异质性处理效应(HTE)的子群。作者提出纵向数据子群发现算法，将广义交互树算法与纵向目标极大似然估计(longitudinal TMLE)相结合。longitudinal TMLE 保证了在时变混杂和删失下估计量的半参数有效性和双重稳健性，而交互树实现了数据驱动的子群划分。该方法被应用于HIV患者EHR数据，识别出使用含DTG抗逆转录病毒疗法后体重增加风险更高的子群。该工作将纵向因果推断与半参数效率理论结合，且提供了流行病学EHR真实数据集的分析范例，直接契合您对 longitudinal CI 和流行病学因果应用的兴趣。
- **关键技术**: `longitudinal targeted maximum likelihood estimation`, `heterogeneous treatment effects`, `generalized interaction tree`, `time-varying confounding`, `double robust estimation`
- **为什么对您有用**: 结合了纵向因果推断与半参数效率理论(longitudinal TMLE)，并提供了流行病学EHR真实数据集的应用范例，直接契合您对 longitudinal CI 和流行病学因果应用的兴趣。

### 3. [10.1093/biostatistics/kxac051](https://doi.org/10.1093/biostatistics/kxac051) — DeLIVR: a deep learning approach to IV regression for testing nonlinear causal effects in transcriptome-wide association studies
- **作者**: Ruoyu He, Mingyang Liu, Zhaotong Lin, Zhong Zhuang, Xiaotong Shen, Wei Pan
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 2 · pp 468-485
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在全转录组关联研究（TWAS）的两样本 IV 回归设定下，目标是检验基因表达对性状的非线性因果效应，克服传统 TWAS 仅考虑线性/二次效应以及 DeepIV 方法求解积分方程不适定且缺乏假设检验框架的缺陷。DeLIVR 通过估计一个相关但不同的目标函数来规避不适定逆问题，利用深度学习非参数地建模非线性效应。核心贡献在于为非线性 IV 回归构建了假设检验框架，且算法相比 DeepIV 更快更稳定。模拟显示 DeLIVR 在速度和稳定性上优于 DeepIV。实证分析基于 GTEx 和 UK Biobank 数据，发现了与 HDL/LDL 胆固醇非线性关联的额外基因（如 BUD13, SLC44A2）。对您有用：该文将深度学习引入非参数 IV 估计并补充了假设检验理论，直接契合您在因果推断（IV）与假设检验方面的核心兴趣，同时其流行病学数据集的应用分析也具参考价值。
- **关键技术**: `instrumental variable regression`, `nonparametric hypothesis testing`, `deep learning`, `ill-posed inverse problem`, `transcriptome-wide association study`
- **为什么对您有用**: 直接契合您在因果推断（IV）与假设检验方面的核心兴趣，展示了如何为非参数 IV 估计构建检验框架，且其基于 UK Biobank 的流行病学应用分析也具参考价值。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 2 篇)*

### 1. [10.1093/biostatistics/kxad007](https://doi.org/10.1093/biostatistics/kxad007) — Identifying covariate-related subnetworks for whole-brain connectome analysis
- **作者**: Shuo Chen, Yuan Zhang, Qiong Wu, Chuan Bi, Peter Kochunov, L Elliot Hong
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 2 · pp 541-558
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在全脑连接组（whole-brain connectome）高维边变量设定下，目标是识别与协变量相关的子网络结构，其中既不知道哪些边与协变量相关，也不知道其拓扑组织。作者从图论与组合学角度刻画协变量相关子网络的图性质，并据此将单边推断与子网络推断桥接起来。核心方法是对多元边变量回归施加 ℓ₀ 惩罚以精确提取协变量相关子网络，同时控制虚假阳性噪声和近乎无限的边组合可能性。算法层面给出了高效求解方案，模拟中与现有方法进行了系统对比。应用于两套精神分裂症静息态 fMRI 数据，获得了高可重复性的疾病相关子网络。对您而言，ℓ₀ 惩罚下的高维组合选择与多重检验校正思路可迁移至高维假设检验与统计计算方向，但理论深度（如收敛率、minimax 最优性）有限。
- **关键技术**: `ℓ₀ norm penalty`, `graph combinatorial structure`, `high-dimensional edge variable selection`, `subnetwork inference`, `multiple testing correction`
- **为什么对您有用**: 高维边变量选择与 ℓ₀ 惩罚组合优化与您的高维统计和统计计算兴趣相邻，但本文偏方法应用，理论贡献（rate、efficiency bound）有限，主要价值在于连接组数据的分析范式可作参考。

### 2. [10.1093/biostatistics/kxad001](https://doi.org/10.1093/biostatistics/kxad001) — Estimating the overall fraction of phenotypic variance attributed to high-dimensional predictors measured with error
- **作者**: Soutrik Mandal, Do Hyun Kim, Xing Hua, Shilan Li, Jianxin Shi
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 2 · pp 486-503
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在前瞻性基因组学研究中，目标是估计高维基因组变量存在测量误差时对表型方差的总贡献度（OFPV），关键假设为因果与非因果变量的测量误差方差分布相似。作者证明在此假设下，渐近衰减因子等于所有变量的平均组内相关系数（ICC），可通过重复测量的先导研究估计。忽略测量误差的现有 GWAS 方法会严重低估 OFPV，本文通过 ICC 修正衰减因子来纠正偏差。理论还表明测量误差不会对双性状效应大小相关性估计造成实质偏差。实证将该方法应用于美国肠道项目（American Gut Project）的微生物群对 BMI 和过敏特征的贡献估计。对您有用：该文处理高维变量测量误差的衰减因子思路，可为您在高维统计与流行病学数据结合的应用场景中提供方法借鉴与数据集参考。
- **关键技术**: `variance component estimation`, `measurement error correction`, `intraclass correlation coefficient`, `asymptotic attenuation factor`, `high-dimensional heritability`
- **为什么对您有用**: 涉及高维统计中的方差成分估计与测量误差修正，并在流行病学数据（American Gut Project）上实证，对您结合高维统计与流行病学应用有直接参考价值。

## 非参数 / 半参数  *(nonparam_semipara, 2 篇)*

### 1. [10.1093/biostatistics/kxac052](https://doi.org/10.1093/biostatistics/kxac052) — Characterizing quantile-varying covariate effects under the accelerated failure time model
- **作者**: Harrison T Reeder, Kyu Ha Lee, Sebastien Haneuse
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 2 · pp 449-467
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在 AFT 模型框架下，本文研究生存分位数上协变量效应异质性的刻画问题，放松了传统 AFT 假设协变量效应为常数乘性位移的限制。作者在 AFT 模型中嵌入灵活回归结构，推导出分位数尺度上可解释效应的新公式；基于 g-formula 的回归标准化方案，实现了暴露变量的条件效应与边际效应估计；采用贝叶斯方法处理左截断与复杂删失下的估计和不确定性量化。模拟与阿尔茨海默病队列应用展示了方法性能。对您而言，g-formula 回归标准化在生存分析中的边际效应估计思路可迁移至 longitudinal causal inference 的设定，且分位数异质性效应建模对 semiparametric theory 中灵活结构模型有参考价值。
- **关键技术**: `quantile-varying AFT model`, `g-formula regression standardization`, `Bayesian estimation with left truncation`, `marginal effect estimation`, `accelerated failure time model`
- **为什么对您有用**: g-formula 回归标准化估计边际效应的思路可直接迁移到 longitudinal causal inference 的生存分析设定；分位数异质性协变量效应的灵活建模框架对 semiparametric theory 中结构模型的推广有方法论参考。

### 2. [10.1093/biostatistics/kxac048](https://doi.org/10.1093/biostatistics/kxac048) — A transformation perspective on marginal and conditional models
- **作者**: Luisa Barbanti, Torsten Hothorn
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 2 · pp 402-428
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文针对聚类/纵向数据提出一种基于线性变换模型（linear transformation model）的边际建模框架：边际分布由变换模型刻画，簇内相关性由联合多元正态分布描述，二者联合给出边际分布的解析公式。变换模型的半参数性质使其适用于任意类型响应（有界、偏态、二值、有序、生存），无需对边际分布做参数假设。实证部分涵盖睡眠剥夺反应时间（放松正态假设）、趾甲数据（边际 odds ratio）、疼痛 VAS 评分（边际比例 odds）及直肠癌无病生存（边际 hazard ratio），并与 GEE 和条件混合效应模型做系统比较。R 包 tram 提供了完整实现。对您而言，该框架在纵向因果推断中直接提供边际处理效应的半参数估计路径，且变换模型的结构便于后续推导 influence function 与效率界。
- **关键技术**: `linear transformation model`, `marginal vs conditional modeling`, `multivariate normal copula for clustering`, `semiparametric marginal distribution`, `GEE comparison`, `mixed-effects model comparison`
- **为什么对您有用**: 直接连接您 primary interest 中的纵向因果推断（边际处理效应是因果 estimand 的核心）与半参数理论（变换模型为半参数模型，可进一步推导 efficiency bound）；R 包 tram 也可作为统计计算层面的参考实现。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1093/biostatistics/kxac045](https://doi.org/10.1093/biostatistics/kxac045) — Longitudinal regression of covariance matrix outcomes
- **作者**: Yi Zhao, Brian S Caffo, Xi Luo
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 2 · pp 385-401
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在纵向协方差矩阵结果的回归设定下，本文提出多层广义线性模型，将协方差矩阵回归到时变协变量上，同时识别协变量关联成分、估计回归系数并刻画within-subject变异，关键正则假设为层次似然可逼近性及高维下适当的稀疏条件。低维情形下，通过最大化逼近层次似然函数获得估计量，证明其渐近一致且协方差矩阵估计量达到该模型类下的最有效性；高维情形下，所提估计量在恒等矩阵与样本协方差矩阵的一切线性组合中达到一致最小二次损失。核心技术工具包括层次似然优化、协方差矩阵的回归参数化分解、以及高维线性组合类的极小极大最优性论证。实证应用于ADNI纵向静息态fMRI数据，识别出不同疾病阶段男女差异的脑网络，较横截面分析提升统计功效。对您有用：低维效率结果与高维最优性直接关联您的efficiency theory和high-dimensional statistics兴趣，纵向设定也与您causal inference中的longitudinal方向衔接。
- **关键技术**: `hierarchical-likelihood optimization`, `multilevel generalized linear model`, `uniformly minimum quadratic loss`, `asymptotic efficiency for covariance estimation`, `longitudinal covariance regression`
- **为什么对您有用**: 低维下协方差估计的最有效性与高维下线性组合类的最优二次损失直接对应您efficiency theory和high-dimensional statistics的核心关注；纵向协方差回归框架可迁移至您causal inference中longitudinal设定的协方差结构建模。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1093/biostatistics/kxad004](https://doi.org/10.1093/biostatistics/kxad004) — Multi-trait analysis of gene-by-environment interactions in large-scale genetic studies
- **作者**: Lan Luo, Devan V Mehrotra, Judong Shen, Zheng-Zheng Tang
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 2 · pp 504-520
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在基因-环境交互作用（GEI）分析中，单 trait 检验因低功效而难以发现信号，大型联盟研究亟需可扩展的多 trait 联合检验方法。本文提出 MTAGEI 框架，基于汇总统计量（summary statistics）对多 trait 进行 GEI 检验：先生成不同环境条件下多 trait 的遗传关联汇总统计量，再整合进行 GEI meta-analysis。方法通过跨 trait 和跨 variant 聚合微弱 GEI 信号提升功效，并通过组合互补检验（complementary tests）在多种遗传架构下保持稳健性，计算上适用于 UK Biobank 规模数据。模拟和 UKB 全外显子测序数据分析表明 MTAGEI 相较现有单 trait GEI 检验有显著功效提升。对您而言，该文的多 trait 互补检验组合策略与假设检验方向直接相关，且 UKB 数据分析流程对流行病学队列研究的应用有参考价值。
- **关键技术**: `multi-trait GEI test`, `summary-statistics-based meta-analysis`, `complementary test combination`, `gene-environment interaction`, `aggregate signal across traits and variants`
- **为什么对您有用**: 多 trait 互补检验组合策略与您 hypothesis testing 方向直接相关；UKB 全外显子测序数据的 GEI 分析流程对流行病学队列研究（secondary interest）中因果交互作用检验有迁移价值。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1093/biostatistics/kxad008](https://doi.org/10.1093/biostatistics/kxad008) — Differential transcript usage analysis incorporating quantification uncertainty via compositional measurement error regression modeling
- **作者**: Amber M Young, Scott Van Buren, Naim U Rashid
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 2 · pp 559-576
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在 RNA-seq 差异转录本使用（DTU）分析设定下，目标是检验同一基因下不同条件间转录本相对丰度比例的差异，现有方法常受限于计算可扩展性且忽略量化不确定性。本文提出 CompDTU，利用成分回归建模转录本相对丰度，并依赖快速矩阵运算实现大规模样本下的高效假设检验与协变量调整。进一步将其扩展为 CompDTUme，通过成分测量误差模型整合 RNA-seq 量化工具输出的不确定性。模拟表明 CompDTU 具有更优的灵敏度和假阳性控制，CompDTUme 在高不确定性基因上进一步提升检验功效。TCGA 乳腺癌数据（740样本）实证显示该方法计算时间大幅缩短并发现新显著基因。对您可能有用：其处理成分数据测量误差的回归建模与快速矩阵计算策略，可为统计计算方向的高维成分数据算法优化提供参考。
- **关键技术**: `compositional regression`, `measurement error model`, `matrix-based computation`, `differential transcript usage testing`, `covariate adjustment`
- **为什么对您有用**: 虽然应用场景为基因组学，但其成分测量误差建模与快速矩阵运算策略直接关联您关注的统计计算与假设检验方向，对处理高维比例数据的算法设计与误差修正有迁移价值。

### 2. [10.1093/biostatistics/kxad019](https://doi.org/10.1093/biostatistics/kxad019) — Fast and flexible inference for joint models of multivariate longitudinal and survival data using integrated nested Laplace approximations
- **作者**: Denis Rustand, Janet van Niekerk, Elias Teixeira Krainski, Håvard Rue, Cécile Proust-Lima
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 2 · pp 429-448
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究多元纵向与生存数据联合模型的贝叶斯推断问题，设定为通过共享或相关随机效应连接多个子模型，传统 MCMC 估计因高维随机效应积分而计算代价高昂。作者引入基于积分嵌套 Laplace 近似（INLA）的贝叶斯近似算法，通过 Laplace 近似逼近边际后验分布，避免了 MCMC 采样。该方法大幅降低计算负担并放宽了对纵向标志物和随机效应维度的限制。模拟研究显示，相比传统估计策略，R-INLA 显著缩短计算时间并降低参数估计的变异性。在原发性胆汁性胆管炎临床试验数据（5个标志物、16个随机效应、竞争风险）中验证了其可行性。对您有用：INLA 作为高效的数值计算与软件工具，可直接服务于纵向因果推断中联合模型的估计问题，同时该 PBC 临床数据集对流行病学应用具有参考价值。
- **关键技术**: `integrated nested Laplace approximation`, `joint models of longitudinal and survival data`, `shared random effects`, `Bayesian approximate inference`, `competing risks`
- **为什么对您有用**: INLA 是重要的统计计算与数值方法，其 R-INLA 实现为纵向因果推断中常见的联合模型估计提供了高效计算工具；同时，文中的 PBC 临床数据集对流行病学应用因果工作有数据集价值。

## 流行病学  *(epidemiology, 4 篇)*

### 1. [10.1093/biostatistics/kxad011](https://doi.org/10.1093/biostatistics/kxad011) — Multiple imputation of more than one environmental exposure with nondifferential measurement error
- **作者**: Yuanzhi Yu, Roderick J Little, Matthew Perzanowski, Qixuan Chen
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 2 · pp 306-322
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在环境流行病学回归模型中，多个暴露变量均存在非差异性测量误差（strong nondifferential ME），目标是校正回归系数的偏差与方差估计。作者提出 constrained chained equations multiple imputation（CEMI）算法，在 chained equations imputation 中对插补模型参数施加非差异性测量误差约束，结合外部或内部校准样本信息；并扩展该方法以处理主研究中误差暴露变量的未检出值（nondetects）。方差估计采用 bootstrap 配合两次插补的方案，避免 Rubin 规则在测量误差场景下的方差低估。模拟显示 CEMI 相较于忽略测量误差、经典校准和回归预测方法，偏差更小且置信区间覆盖率接近名义水平；实证分析使用纽约市 Neighborhood Asthma and Allergy Study 数据，考察多种室内过敏原浓度与 FeNO 的关联。对您而言，该文提供了一个流行病学真实数据集及测量误差校正的完整分析流程，且 CEMI 的约束插补思路可迁移至因果推断中 mismeasured confounder/exposure 的敏感性分析场景。
- **关键技术**: `constrained chained equations multiple imputation`, `nondifferential measurement error correction`, `bootstrap variance estimation with multiple imputation`, `calibration sample integration`, `nondetects imputation`
- **为什么对您有用**: 连接您 secondary interest 中的流行病学应用与数据集（NYC 哮喘儿童队列），同时测量误差校正在因果推断中 mismeasured exposure/confounder 场景下有直接迁移价值，约束插补思路可为 sensitivity analysis 提供新视角。

### 2. [10.1093/biostatistics/kxad009](https://doi.org/10.1093/biostatistics/kxad009) — Modeling biomarker variability in joint analysis of longitudinal and time-to-event data
- **作者**: Chunyu Wang, Jiaming Shen, Christiana Charalambous, Jianxin Pan
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 2 · pp 577-596
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文在纵向与生存数据联合建模框架下，提出一种新的生物标志物变异性度量，旨在分离真实生物学波动与测量误差导致的随机变异。设定上，纵向子模型采用混合效应模型，均值函数以 cubic spline 参数化，变异性度量为随机效应的二次型；生存子模型为 Cox 模型，将变异性及潜在轨迹当前水平同时纳入协变量。理论上建立了联合模型 MLE 的渐近性质；计算上采用 EM 算法，E-step 使用 fully exponential Laplace 近似以缓解随机效应维度增加带来的计算负担。模拟显示该方法优于两阶段法及忽略变异性的简化联合模型；实证分析基于 MRC 老年试验数据，考察收缩压变异性对心血管事件的影响。对您而言，该文在纵向因果推断的纵向子模型建模（如 g-formula 中的轨迹建模）以及 EM + Laplace 近似的计算策略上有参考价值，但方法学 novelty 偏增量式。
- **关键技术**: `joint modeling of longitudinal and survival data`, `mixed-effects model with cubic spline mean`, `quadratic form of random effects`, `EM algorithm with fully exponential Laplace approximation`, `Cox proportional hazards model`, `MLE asymptotic properties`
- **为什么对您有用**: 与您 primary interest 中的 longitudinal causal inference 有间接连接——联合模型中的纵向子模型结构可迁移到 g-formula / proximal longitudinal 设定下的轨迹建模；同时 EM + Laplace 近似的计算策略对统计计算方向有参考，但核心方法学 novelty 有限。

### 3. [10.1093/biostatistics/kxad016](https://doi.org/10.1093/biostatistics/kxad016) — A joint Bayesian hierarchical model for estimating SARS-CoV-2 genomic and subgenomic RNA viral dynamics and seroconversion
- **作者**: Tracy Q Dong, Elizabeth R Brown
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 2 · pp 336-353
- 相关性 0/10 · novelty: `application`
- **摘要**: 在 COVID-19 病毒动力学研究中，目标是联合估计 genomic RNA 病毒载量、subgenomic RNA (sgRNA) 病毒载量（反映活跃复制）以及血清转化的速率与时序（反映抗体出现），关键假设为两类病毒载量共享潜在动态过程且与血清转化存在关联。作者提出贝叶斯分层模型，通过共享随机效应与相关结构刻画两类病毒载量间的动态关系，实现病毒载量与抗体数据间的信息借用，并识别病毒载量特征与血清转化倾向的潜在预测因子。方法应用于 COVID-19 暴露后预防研究数据，交叉验证表明模型可对仅有 genomic RNA 数据的个体 impute sgRNA 轨迹。该工作属于流行病学应用，方法学上为标准贝叶斯分层联合建模的工程化适配，理论 novelty 有限。对您而言，若关注流行病学纵向队列中多标记物联合建模的数据结构与建模范式，可作参考，但无因果推断或半参数效率理论贡献。
- **关键技术**: `Bayesian hierarchical model`, `joint longitudinal-survival modeling`, `shared random effects`, `information borrowing`, `cross-validation imputation`
- **为什么对您有用**: 属于流行病学（secondary interest）应用，提供 COVID-19 纵向多标记物数据结构与联合建模范式，但方法学为标准贝叶斯分层模型，理论贡献有限，主要价值在于数据集与建模思路的可迁移性。

### 4. [10.1093/biostatistics/kxad003](https://doi.org/10.1093/biostatistics/kxad003) — A Bayesian approach to estimating COVID-19 incidence and infection fatality rates
- **作者**: Justin J Slater, Aiyush Bansal, Harlan Campbell, Jeffrey S Rosenthal, Paul Gustafson, Patrick E Brown
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 2 · pp 354-384
- 相关性 0/10 · novelty: `application`
- **摘要**: 在 COVID-19 血清学调查设定下，目标是估计累计发病率与感染死亡率（IFR），需克服优先检测带来的选择偏倚及不完全死亡数据的不确定性。传统方法将连续抗体滴度离散化，导致信息损失；本文提出基于多元混合模型直接对连续滴度建模，以区分既往感染与未感染人群。结合后分层技术校正样本代表性偏差，并在近似贝叶斯框架下实现发病率与 IFR 的联合推断。该框架通过传播感染人数估计与死亡数据缺失的双重不确定性，提供更可靠的 IFR 区间估计。实证分析基于加拿大 Action to Beat Coronavirus 数据集展示了方法应用。对您而言，该文是流行病学血清学数据偏倚校正的应用案例，展示了连续代理变量的建模思路，但方法学核心为标准贝叶斯混合模型，理论新颖度有限。
- **关键技术**: `multivariate mixture model`, `post-stratification`, `approximate Bayesian inference`, `serosurvey titer modeling`, `selection bias adjustment`
- **为什么对您有用**: 属于流行病学（secondary interest）应用，展示了在优先检测偏倚下利用连续代理变量建模的贝叶斯推断流程，对处理流行病学数据偏倚有参考价值，但方法学核心为标准贝叶斯混合模型，理论新颖度有限。

## 其他  *(other, 1 篇)*

### 1. [10.1093/biostatistics/kxad005](https://doi.org/10.1093/biostatistics/kxad005) — Cohort-based smoothing methods for age-specific contact rates
- **作者**: Yannick Vandendijck, Oswaldo Gressani, Christel Faes, Carlo G Camarda, Niel Hens
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 2 · pp 521-540
- 相关性 2/10
- **摘要**: {
  "topic": "epidemiology",
  "summary_zh": "本文研究社交接触矩阵（respondent 年龄 × contact 年龄）的平滑估计问题，目标是利用 POLYMOD 等人群接触调查数据获得 age-specific contact rates，假设同龄群体随年龄变化的接触行为光滑。核心创新在于提出"队列视角"平滑：利用接触的互惠性约束，沿接触矩阵的对角线（即同一出生队列）而非传统的行/列方向施加 P-spline 惩罚；具体给出两种实现——(i) 重排矩阵对角元素后对标准惩罚矩阵做平滑，(ii) 直接重排惩罚矩阵使其作用于对角方向。参数估计在似然框架下通过 constrained penalized IRLS 完成，模拟显示 cohort-based 平滑在减少 MSE 方面优于 bivariate 行列平滑，并在比利时 POLYMOD 2006 数据上做了实证。对您而言，该文提供了流行病学接触调查数据的矩阵结构与建模思路，若未来在传染病因果推断或纵向因果模型中需要参数化接触模式，此数据集与平滑框架可直接迁移。",
  "key_techniques": [
    "penalized B-splines (P-splines)",
    "cohort-based diagonal smoothing",
    "penaliz


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

