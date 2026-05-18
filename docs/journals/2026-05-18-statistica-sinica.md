# Statistica Sinica  ·  2026-05-18

- 共 27 篇 · Statistica Sinica

## 因果推断  *(causal_inference, 3 篇)*

### 1. [10.5705/ss.202025.0331](https://doi.org/10.5705/ss.202025.0331) — Semiparametric Causal Discovery and Inference with Invalid Instruments
- **作者**: Jing Zou, Wei Li, Wei Lin
- **期刊/来源**: Statistica Sinica
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在存在未观测混杂和潜在无效工具变量（IV）的设定下，本文研究基于部分线性结构方程模型（PLSEM）的因果发现与推断问题。作者通过构造替代有效IV（surrogate valid IVs）实现了在半参数模型下的因果识别，并提出了一种有限样本下的因果结构与效应估计程序。理论上证明了该程序能一致地学习因果结构，估计量具有渐近正态性，且在边恢复（edge recovery）中能有效控制错误发现率（FDR）。模拟与阿尔茨海默病基因调控网络推断验证了方法优越性。对您有用：该文将半参数理论与无效IV设定结合，其替代IV构造思路与渐近正态性证明对您在IV敏感性分析及半参数效率理论方向的研究有直接参考价值。
- **关键技术**: `partially linear SEM`, `invalid instrumental variables`, `surrogate valid IVs`, `asymptotic normality`, `false discovery rate control`
- **为什么对您有用**: 直接关联您在因果推断中对IV和半参数理论的兴趣；其处理无效IV的识别策略和渐近正态性结果，可为IV敏感性分析及半参数估计提供新思路。

### 2. [10.5705/ss.202025.0476](https://doi.org/10.5705/ss.202025.0476) — Conformal Causal Inference for Cluster Randomized Trials: Model-robust Inference Without Asymptotic Approximations
- **作者**: Bingkai Wang, Fan Li, Mengxin Yu
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在整群随机试验(CRT)设定下，传统推断依赖簇数趋于无穷的渐近理论，本文提出基于 conformal inference 的因果推断框架，在有限样本下对反事实结果之差构建预测区间，无需渐近近似。与传统聚焦 ATE 点估计不同，该框架对反事实结果差异提供预测区间。方法兼容任意工作结局模型（包括自适应 ML 方法），并对模型误设具有鲁棒性。理论上证明了有限样本覆盖保证；计算上开发了针对簇/个体水平处理效应预测区间的高效算法，并扩展至协变量子群推断。实证基于一项慢性疼痛 CRT 数据。对您有用：该文将 conformal prediction 引入因果推断，提供了有限样本假设检验/区间估计的新视角，且涉及流行病学应用数据。
- **关键技术**: `conformal prediction`, `cluster randomized trials`, `finite-sample inference`, `model-robust inference`, `counterfactual prediction interval`
- **为什么对您有用**: 结合了因果推断与有限样本假设检验（conformal inference），放松了传统 CRT 推断对大簇数的渐近依赖，并在流行病学 CRT 数据上进行了应用，对您在因果推断和假设检验的交叉研究有参考价值。

### 3. [10.5705/ss.202025.0315](https://doi.org/10.5705/ss.202025.0315) — Balancing Covariates in Survey Experiments
- **作者**: Pengfei Tian, Jiyang Ren, Yingying Ma
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在总体调查实验（随机抽样+随机分配）设定下，针对有限样本协变量不平衡问题，提出分层拒绝抽样与重随机设计以改善协变量平衡。基于设计视角（design-based），推导了分层均值差估计量的渐近理论，证明其极限分布为正态分布与两个截断正态分布的卷积，且比现有设计的极限分布更集中于真实ATE。进一步在分析阶段提出协变量调整方法以提升估计效率。该文推导的非标准渐近分布及设计-分析双重效率提升策略，直接关联您关注的因果推断ATE估计与效率理论。
- **关键技术**: `rerandomization`, `stratified rejective sampling`, `design-based asymptotic theory`, `truncated normal distribution`, `covariate adjustment`, `difference-in-means`
- **为什么对您有用**: 直接关联因果推断的ATE估计与效率理论，其推导的非标准渐近分布（正态与截断正态卷积）对理解重随机设计下的推断有理论价值，且协变量调整方法提供了效率提升的具体路径。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 5 篇)*

### 1. [10.5705/ss.202025.0014](https://doi.org/10.5705/ss.202025.0014) — Detecting Structural Breaks in High-dimensional Functional Time Series Factor Models
- **作者**: Caixia Xu, Huacheng Su, Xu Liu, Jinhong You
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究高维函数时间序列因子模型中因子载荷存在未知次数结构突变的估计问题。提出三步法：首先逐点估计因子载荷并计算相邻时间点载荷差异序列；其次采用 Wild Binary Segmentation (WBS) 算法对该差异序列进行变点检测，估计突变数量与位置；最后基于估计的变点位置重新估计函数因子模型。理论上给出了变点位置估计的收敛速率，并在高维设定下保证了因子模型重估计的统计性质。对您有用：该文将高维因子模型与变点检测结合，其 WBS 与逐点特征分析技术对您在 high-dimensional statistics 中的假设检验/变点检测研究有直接参考价值，且模型适用于经济时间序列数据。
- **关键技术**: `high-dimensional factor model`, `functional time series`, `wild binary segmentation (WBS)`, `change-point detection`, `time-varying factor loadings`
- **为什么对您有用**: 将高维因子模型与变点检测结合，WBS与逐点特征分析技术对您在 high-dimensional statistics 中的假设检验/变点检测研究有直接参考价值，且模型适用于经济时间序列数据。

### 2. [10.5705/ss.202025.0303](https://doi.org/10.5705/ss.202025.0303) — Linear Shrinkage Convexification of Penalized Linear Regression with Missing Data
- **作者**: Seongoh Park, Seongjin Lee, Nguyen Thi Hai Yen, Nguyen Phuoc Long, Johan Lim
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在含缺失数据的惩罚线性回归设定下，缺失导致协方差矩阵非正定、最小二乘损失非凸，目标是恢复凸性并证明 Lasso 估计的 selection consistency 与收敛率。本文提出 linear shrinkage positive definite (LPD) 修改，对缺失下的协方差估计施加线性收缩以保证正定性和一致性，从而将惩罚回归问题凸化。LPD 修改有解析表达式，计算高效；理论上证明了 Lasso+LPD 的 selection consistency，并给出 ℓ₂ 误差率 s₀^{3/2}√(log p/n)（s₀ 为非零系数数）。该速率比标准 Lasso minimax 率 √(s₀ log p/n) 多了 s₀ 因子，源于缺失引入的额外偏差。实证部分用 GDSC 癌症基因组数据验证。对您有用：LPD 的线性收缩思路与 RMT 中 Ledoit-Wolf 收缩估计一脉相承，且凸化技巧可迁移到高维缺失数据下其他正则化问题的计算与理论分析。
- **关键技术**: `linear shrinkage covariance estimation`, `convexification of non-convex loss`, `Lasso selection consistency`, `missing data imputation via covariance modification`, `ℓ₁-penalized regression`
- **为什么对您有用**: 直接关联您的高维统计与 RMT 兴趣（线性收缩估计与 Ledoit-Wolf 同源），同时涉及统计计算（凸化使优化可解）；ℓ₂ 收敛率中 s₀^{3/2} 因子提示仍有改进空间，对关注 sharper rate 的您有理论启发。

### 3. [10.5705/ss.202024.0276](https://doi.org/10.5705/ss.202024.0276) — Grade of Membership Analysis for Multi-Layer Ordinal Categorical Data
- **作者**: Huan Qing
- **期刊/来源**: Statistica Sinica
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 在多层有序分类数据（如纵向心理测试）的 Grade of Membership (GoM) 设定下，目标是估计个体跨时间共享的混合隶属度，假设个体以不同权重从属于多个潜类。本文提出 multi-layer GoM 模型将传统 GoM 推广至多层有序数据，并设计基于去偏 Gram 矩阵和的估计方法，利用矩阵谱方法提取潜结构。理论上给出了 GoM-DSoG 的逐个体收敛速率，证明更多个体、项目、层数及更少无响应有利于估计，并提出了潜类数目的选择方法。对您可能有用：其去偏 Gram 矩阵和的技术思路可迁移至高维统计与随机矩阵理论中的潜变量估计，且算法实现涉及统计计算中的矩阵数值方法。
- **关键技术**: `Grade of Membership model`, `debiased sum of Gram matrices`, `spectral method`, `per-subject convergence rate`, `latent class selection`
- **为什么对您有用**: 去偏 Gram 矩阵和的估计策略与高维统计/随机矩阵理论中的谱方法紧密相关，其收敛率分析对您研究高维潜变量模型的逐点收敛性质有参考价值。

### 4. [10.5705/ss.202025.0036](https://doi.org/10.5705/ss.202025.0036) — Robust Max Statistics for High-dimensional Inference
- **作者**: Mingshuo Liu, Miles Lopes
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `weaker_assumption`
- **摘要**: 在高维重尾数据设定下，本文研究 max statistic 的高维假设检验问题，放松了传统文献对轻尾（如次高斯）分布的假设。提出基于稳健成分的 robust max statistic，并证明其分布可通过 bootstrap 精确逼近。关键正则条件为扩展的 L^4-L^2 矩等价条件与弱方差衰减条件。在 Kolmogorov 距离下，bootstrap 逼近达到近参数速率（near-parametric rate），且该收敛速率与数据维度 p 无关。理论结果在欧氏与函数型数据的模拟中得到了验证。对您有用：直接推进了高维统计与假设检验的交叉方向，通过放松轻尾假设提供了更稳健的高维检验方法，对处理重尾高维数据推断具有直接参考价值。
- **关键技术**: `robust max statistics`, `bootstrap approximation`, `heavy-tailed data`, `L^4-L^2 moment equivalence`, `Kolmogorov metric`, `high-dimensional hypothesis testing`
- **为什么对您有用**: 直接推进了您 primary interest 中的高维统计与假设检验方向；通过放松轻尾假设，为重尾高维数据的 max-type 检验提供了近参数速率的 bootstrap 理论，对处理实际中的重尾高维推断有直接参考价值。

### 5. [10.5705/ss.202025.0205](https://doi.org/10.5705/ss.202025.0205) — Sparsity Learning via Structured Functional Factor Augmentation
- **作者**: Hanteng Ma, Ziliang Shen, Xingdong Feng, Xin Liu
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究高维函数线性回归模型中的变量选择问题，目标是在函数协变量存在相关性的设定下实现稀疏学习与有效推断。针对高维函数协变量间的相关性带来的统计挑战，文章提出了一种新的函数因子增广结构（fFAS）。在此基础上构建了多元函数因子增广选择模型（fFASM），通过提取潜在因子结构来解耦协变量相关性，并结合稀疏惩罚实现变量选择。理论上证明了 fFAS 结构的合理性，并建立了 fFASM 的估计收敛速度与选择一致性。数值实验表明该方法在估计精度和选择一致性上具有优势。对您而言，该文将因子增广思想引入高维函数数据的稀疏推断，为高维统计中处理复杂相关协变量结构提供了可迁移的方法论视角。
- **关键技术**: `functional factor augmentation`, `high-dimensional functional regression`, `variable selection consistency`, `multivariate functional series`, `sparsity learning`
- **为什么对您有用**: 该文处理高维函数协变量相关结构下的变量选择与推断，属于高维统计与无限维（非参数）理论的交叉，为您在高维统计中处理非标准协变量（函数数据）的稀疏学习与推断提供了因子增广的新视角。

## 非参数 / 半参数  *(nonparam_semipara, 9 篇)*

### 1. [10.5705/ss.202024.0298](https://doi.org/10.5705/ss.202024.0298) — Minimax Rates of Convergence for Nonparametric Regression Under Adversarial Attacks
- **作者**: Jingfu Peng, Yuhong Yang
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 本文在非参数回归设定下研究对抗攻击下的鲁棒性极限，目标是在输入受 l∞ 约束的对抗扰动时，回归函数估计在 adversarial sup-norm 下的 minimax 收敛速率。核心发现是：对抗设定下的 minimax rate 等于标准无攻击 minimax rate 与真实回归函数在扰动区域内最大偏差之和。作者证明，由标准设定下 minimax 最优估计量构造的 adversarial plug-in 过程即可达到该最优速率，无需额外复杂算法。文中以 Holder 类和单调函数类为例具体展示了收敛速率表达式。该工作对您在非参数理论及 minimax rate 方面的兴趣有直接借鉴价值，提供了对抗设定下 sup-norm risk 分解的新理论视角。
- **关键技术**: `minimax rate of convergence`, `adversarial sup-norm risk`, `nonparametric regression`, `adversarial plug-in procedure`, `Holder class`
- **为什么对您有用**: 直接推进了您 primary interest 中的非参数理论，给出了对抗设定下 sup-norm minimax rate 的精确分解与可达性证明，对研究高维/非参数效率界及鲁棒估计有理论迁移价值。

### 2. [10.5705/ss.202025.0389](https://doi.org/10.5705/ss.202025.0389) — Conformal Inference for Missing Data Under Multiple Robust Learning
- **作者**: Wenlu Tang, Hongni Wang, Xingcai Zhou, Bei Jiang, Linglong Kong
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在 Missing at Random (MAR) 设定下，本文研究缺失数据的 conformal inference 问题，目标是构建具有覆盖保证的预测区间。提出 CM-MRL 方法，将 split conformal calibration 与 multiple robust empirical-likelihood (EL) 重加权方案结合。核心机制是通过 EL 对 complete-case scores 进行双重校准重加权，使其分布匹配 MAR 隐含的全校准分布，即使部分 working model 误判仍保持有效性。利用 empirical process theory 建立估计量的渐近性质，证明预测区间在边际和条件覆盖下均可靠，并给出区间长度占优结果。多重稳健性是对传统 doubly robust 的推广，允许部分 nuisance model 误判仍保证有效性，与 semiparametric efficiency 理论紧密相连。对您有用：多重稳健 EL 重加权框架可直接迁移至 causal inference 中的 IPW/DR 估计设定，且 empirical process 渐近分析工具对您在 semiparametric efficiency bounds 方面的研究有参考价值。
- **关键技术**: `split conformal prediction`, `multiple robust empirical likelihood`, `double calibration`, `empirical process theory`, `MAR missing data`
- **为什么对您有用**: 多重稳健 EL 重加权框架可直接迁移至 causal inference 的 IPW/DR 估计（primary interest: causal inference 的 identification/estimation），且 empirical process 渐近分析对 semiparametric efficiency bounds 研究有工具性参考价值。

### 3. [10.5705/ss.202025.0069](https://doi.org/10.5705/ss.202025.0069) — Quantile Index Regression
- **作者**: Yingying Zhang, Qianqian Zhu, Yuefeng Si, Guodong Li
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在极值分位数（尾部）数据稀疏的设定下，本文提出分位数指标回归（QIR），通过引入分位数指标的灵活参数结构，利用数据丰富区域的估计外推至远端尾部。方法上采用复合分位数回归（CQR）获得非交叉分位数估计量。理论上，对低维协变量情形证明了估计量的渐近正态性，对高维情形则推导了非渐近误差界。仿真与实证表明该方法在尾部估计中的实用性。该文在高维设定下的非渐近误差界与低维渐近正态性理论，直接契合您对高维统计与半/非参数理论的兴趣，其尾部外推思想也可为因果推断中极端处理效应的估计提供参考。
- **关键技术**: `quantile index regression`, `composite quantile regression`, `non-asymptotic error bounds`, `tail extrapolation`, `non-crossing quantile estimation`
- **为什么对您有用**: 高维情形下的非渐近误差界与低维渐近正态性理论契合您对高维统计与半/非参数理论的兴趣；尾部外推与CQR方法可为极端处理效应估计提供思路。

### 4. [10.5705/ss.202025.0156](https://doi.org/10.5705/ss.202025.0156) — Conformal Prediction Under Nonignorable Missingness
- **作者**: Menghan Yi, Yingying Zhang, Yanlin Tang, Huixia Judy Wang
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在非可忽略缺失(nonignorable missingness)设定下，目标是构建响应变量的预测集，面临不可识别性与数据不可交换性两大挑战。核心方法是在目标点附近构造局部子集上的最高条件密度预测集，并通过倾向得分(propensity score)校正选择偏差。提出一种偏差调整的半参数条件密度估计方法：对观测数据拟合分位数过程，并利用倾向得分逆概率加权修正偏差。该估计量嵌入共形预测框架，保证了边际覆盖、局部覆盖及渐近条件覆盖，同时达到渐近最优区间长度。理论证明了覆盖有效性与渐近最优性，并在HIV-CD4流行病学数据上进行了实证。对您有用：该文利用倾向得分加权修正半参数分位数过程偏差的思路，可直接迁移至因果推断中处理选择偏差/不可忽略缺失的半参数估计问题。
- **关键技术**: `conformal prediction`, `nonignorable missingness`, `propensity score weighting`, `semiparametric conditional density estimation`, `quantile process`, `selection bias correction`
- **为什么对您有用**: 利用倾向得分加权修正半参数分位数过程偏差的框架，与因果推断中处理不可忽略缺失/混杂的半参数理论高度同源；HIV-CD4数据集对流行病学应用有参考价值。

### 5. [10.5705/ss.202025.0148](https://doi.org/10.5705/ss.202025.0148) — Identification and Estimation of General Nonlinear Structured Latent Factor Model for Functional Data
- **作者**: Xiaorui Wang, Yimang Zhang, Jian Qing Shi
- **期刊/来源**: Statistica Sinica
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文在功能性数据框架下提出一般非线性结构化潜因子模型，目标是在潜因子相关且具有结构化可识别性的设定下估计非线性联系函数与潜因子。方法上采用高斯过程（GP）先验估计未知非线性联系函数，并通过最近邻高斯过程（NNGP）大幅降低计算复杂度。理论上建立了潜因子与未知参数的一致性，以及联系函数的后验一致性；结构化可识别性条件确保潜因子具有物理可解释性。模拟表明 NNGP 相比 GP 显著节省计算时间，且模型在非线性设定下灵活有效。实证分析应用于步态数据以早期检测神经退行性疾病。对您而言，GP/NNGP 估计非线性联系函数的半参数/非参数框架及结构化可识别性理论，与您关注的 semiparametric theory 和 statistical computing 均有直接方法学交集。
- **关键技术**: `nonlinear structured latent factor model`, `Gaussian process prior`, `nearest neighbor Gaussian process (NNGP)`, `structured identifiability`, `posterior consistency`, `functional data analysis`
- **为什么对您有用**: GP 先验估计非线性联系函数属于 semiparametric/nonparametric theory 范畴，NNGP 加速与 statistical computing 直接相关；步态数据的神经退行性疾病应用对 epidemiology secondary interest 有数据集参考价值。

### 6. [10.5705/ss.202025.0207](https://doi.org/10.5705/ss.202025.0207) — A Model-free Correlation Coefficient for Censored Data
- **作者**: Linlin Dai, Tengfei Li, Kani Chen
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 针对右删失生存数据，本文提出了一种无需模型假设的依赖性度量及其估计量——删失秩相关系数（CRC），旨在克服 Cox 模型无法捕捉非单调或非线性关联的局限。CRC 基于秩统计量构造，其目标参数取值于 [0,1]，当且仅当变量独立时为 0，当且仅当存在可测函数关系时为 1。该方法不依赖变量分布，计算复杂度为 O(n log n)，并通过 power-consistent 置换检验构建了检验独立性的 p 值。理论上证明了 CRC 的强相合性与渐近正态性。模拟与 ADNI 阿尔茨海默病数据表明其在检测非线性关联上优于 Cox 模型。对您有用：该文结合了非参数依赖度量与假设检验，其渐近正态性推导对您在非参数/半参数理论及假设检验方向的兴趣有直接参考价值，且 ADNI 数据集对流行病学应用有借鉴意义。
- **关键技术**: `rank-based correlation`, `right-censored data`, `permutation test`, `asymptotic normality`, `model-free dependence measure`
- **为什么对您有用**: 该文提出的非参数依赖度量及渐近正态性理论直接契合您在非参数/半参数理论和假设检验方面的兴趣；同时，其在 ADNI 阿尔茨海默病数据上的应用对您在流行病学数据集上的应用有参考价值。

### 7. [10.5705/ss.202025.0318](https://doi.org/10.5705/ss.202025.0318) — Semiparametric Analysis for Paired Comparisons with Covariates
- **作者**: Haoyue Song, Lianqiang Qu, Ting Yan, Yuguo Chen
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在成对比较数据（如 Bradley-Terry 模型）的设定下，为放松参数模型假设，本文提出一个半参数框架，引入分布未知的潜在随机变量来刻画项目优势与协变量效应，且参数维度随项目数发散。采用基于核函数的最小二乘法估计所有未知参数。在每对项目比较次数固定且项目数趋于无穷的 increasing dimension 设定下，证明了所有估计量的一致性，并推导出其渐近正态分布。这是首个在维度发散下对成对比较进行半参数分析的工作。对您有用：该文将半参数理论与 increasing dimension 设定结合推导渐近正态性的技术路线，对您在半参数理论及高维统计方面的研究有直接参考价值。
- **关键技术**: `semiparametric framework`, `kernel-based least squares`, `increasing dimension`, `asymptotic normality`, `Bradley-Terry model`
- **为什么对您有用**: 论文结合了半参数理论与 increasing dimension 设定，推导了估计量的渐近正态性，这与您在半参数理论和高维统计方面的 primary interests 直接相关，其处理发散参数维度的技术路线可作参考。

### 8. [10.5705/ss.202025.0120](https://doi.org/10.5705/ss.202025.0120) — Estimation of Piecewise Continuous Regression Function in Finite Dimension using Oblique-axis Regression Tree with Applications in Image Denoising
- **作者**: Subhasish Basak, Anik Roy, Partha Sarathi Mukherjee
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在固定设计点下研究有限维分段连续回归函数的估计问题，目标是准确捕捉二维回归函数中跳跃位置曲线（JLCs）的复杂形状。作者提出斜轴回归树（ORT），通过递归树划分对局部像素强度进行聚类，并利用局部叶节点平均来估计回归函数。与传统回归树估计分段常数函数不同，ORT在有限维下能更好地保留JLCs的复杂结构。由于对底层回归函数的假设不同，其理论证明框架与现有回归树文献有显著差异。图像去噪的数值实验表明该方法在去噪的同时能有效保留复杂边缘结构。对您可能有用：虽然应用场景为图像处理，但其针对分段连续非参函数估计的新证明框架和树划分算法，可为您的非参数理论和统计计算兴趣提供参考。
- **关键技术**: `Oblique-axis Regression Tree (ORT)`, `piecewise continuous regression`, `jump location curves (JLCs)`, `recursive tree partitioning`, `local leaf-only averaging`
- **为什么对您有用**: 本文属于非参数理论范畴，其针对分段连续函数的树估计方法及不同的理论证明框架，对您在非参数理论及统计计算（树算法实现）方面的兴趣有方法论参考价值。

### 9. [10.5705/ss.202024.0402](https://doi.org/10.5705/ss.202024.0402) — Robust Mean Signal Estimation and Inference for Imaging Data
- **作者**: Yang Long, Guanqun Cao, David Kepplinger, Lily Wang
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究噪声成像数据中均值信号的稳健估计与推断问题，将含噪成像数据建模为受污染的函数数据，目标是在不规则区域和空间依赖下估计均值函数。提出基于三角剖分上的双变量惩罚样条的稳健平滑 M-estimator，以应对数据污染和空间相关性。理论上，在特定正则条件下建立了该均值函数估计量的 L2 收敛速率，并证明了其渐近正态性。此外，提出了一种构建均值信号同时置信带的新方法。模拟与脑成像真实数据验证了方法的有效性。对您而言，该文在非参数理论（双变量样条 M-estimator 的渐近正态性与 L2 收敛）和假设检验（同时置信带构建）方面提供了严谨的理论结果，且其处理不规则区域的计算策略可迁移至其他空间统计问题。
- **关键技术**: `robust M-estimation`, `bivariate penalized splines over triangulation`, `contaminated functional data`, `simultaneous confidence corridor`, `asymptotic normality`, `L2 convergence rate`
- **为什么对您有用**: 直接契合您在非参数理论（M-estimator 渐近正态性与收敛率）和假设检验（同时置信带推断）方面的核心兴趣，其处理不规则区域空间依赖的计算与理论框架也可为统计计算与空间因果推断提供借鉴。

## 数理统计 / 假设检验  *(hypothesis_testing, 4 篇)*

### 1. [10.5705/ss.202024.0334](https://doi.org/10.5705/ss.202024.0334) — Optimal Robust Sequential Tests of Circular Nonconforming Probability
- **作者**: Qunzhi Xu, Yajun Mei
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 在非参数序贯检验框架下，目标是检验圆形不合格概率（CNP）——即系统偏离预设二维圆盘目标的概率，不假设观测数据的参数分布形式。本文证明 Bernoulli SPRT 在所有具有相同或更小 I/II 类错误概率的检验（含固定样本与序贯检验）中，最小化最大期望样本量，达到 minimax 最优性。由于序贯分析渐近理论常假设极小错误概率，实际未必可行，作者进一步提出设计并实现 Bernoulli SPRT 的实用算法。该工作将经典 SPRT 的最优性从参数设定推广至非参数 minimax 设定，对您在假设检验方向上研究非参数/极小化极大序贯检验有直接参考价值。
- **关键技术**: `sequential probability ratio test (SPRT)`, `minimax optimality`, `nonparametric sequential testing`, `Bernoulli SPRT`, `circular nonconforming probability`
- **为什么对您有用**: 直接关联您在 hypothesis testing 方向的兴趣：将 SPRT 的最优性从参数推广到非参数 minimax 设定，提供了非参数序贯检验的理论框架与实用算法，可迁移至其他非参数序贯检验问题。

### 2. [10.5705/ss.202025.0295](https://doi.org/10.5705/ss.202025.0295) — Inference on Two-Sample Covariance Difference for Large-Scale Functional Data
- **作者**: Kaijie Xue, Lan Xue, Riquan Zhang
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `weaker_assumption`
- **摘要**: 在两样本大规模函数数据设定下，目标是推断协方差差异，无需对协方差或相关性强加结构约束，且放松了分布假设。提出基于 multiplier bootstrap 的计算高效推断程序，构建协方差差异的置信域，进而导出更优功效的检验及一致的估计功效函数。该方法具有“eigenvalue-decay-free”和“square-integrable-free”的特性，避免了函数数据常见的谱衰减条件限制。理论和模拟表明该方法在广泛替代假设下功效函数一致。对您有用：此工作将 multiplier bootstrap 应用于高维函数数据协方差检验，放松了特征值衰减等假设，对您在假设检验与高维统计（协方差矩阵推断）交叉方向的研究有直接参考价值。
- **关键技术**: `multiplier bootstrap`, `covariance difference inference`, `large-scale functional data`, `eigenvalue-decay-free`, `confidence region construction`
- **为什么对您有用**: 直接关联您在假设检验和高维统计方面的 primary interests；其放松特征值衰减与平方可积假设的 multiplier bootstrap 方法，对高维协方差推断与检验具有方法学迁移价值。

### 3. [10.5705/ss.202025.0113](https://doi.org/10.5705/ss.202025.0113) — Multiple Testing of Local Extrema for Detection of Structural Breaks in Piecewise Linear Models
- **作者**: Zhibing He, Dan Cheng, Yunpeng Zhao
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在平稳高斯噪声下的分段线性模型中，本文研究结构突变点（连续折点 Type I 与跳跃点 Type II）的数量与位置检测问题。方法通过核平滑与微分将变点检测转化为局部极值识别，利用平滑高斯过程的峰值高度分布为所有局部极值计算 p 值，并结合 Benjamini-Hochberg (BH) 程序进行多重检验以控制 FDR。理论上证明了在序列长度、斜率变化或跳跃大小增加时，该方法具有渐近 FDR 控制与功效一致性。计算上仅需对所有候选极值执行一次检验，复杂度与序列长度成正比（O(n)），优于传统递归分割方法。该工作将非参数平滑与多重检验结合，对您在假设检验（FDR 控制）与统计计算（低复杂度算法）方向的研究有直接的方法论借鉴意义。
- **关键技术**: `kernel smoothing`, `smooth Gaussian process`, `peak height distribution`, `Benjamini-Hochberg procedure`, `FDR control`, `O(n) algorithm`
- **为什么对您有用**: 将变点检测转化为多重检验问题并实现 O(n) 算法，直接契合您在假设检验（FDR 控制）与统计计算（数值方法与算法）方面的核心兴趣，其高斯过程极值理论的应用也对非参数理论有参考价值。

### 4. [10.5705/ss.202025.0155](https://doi.org/10.5705/ss.202025.0155) — Subgroup Testing in Change-Plane Models and Its Applications to Medical Data
- **作者**: Xu Liu, Jian Huang, Yong Zhou, Feipeng Zhang, Panpan Ren
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究 change-plane 模型中系数的假设检验问题，旨在检测变点平面的存在性以指导个性化治疗，其原假设下分组参数不可识别。针对经典指数平均检验在此类非正则问题下功效不佳的缺陷，提出了加权平均平方得分检验统计量（WAST），通过对分组参数空间上的平方得分统计量加权平均，并在适当权重下获得闭式表达。推导了 WAST 在原假设和备择假设下的渐近分布，并提出了带有理论保证的 Bootstrap 方法逼近临界值。方法进一步扩展至广义估计方程（GEE）框架与多重变点平面情形，模拟与三个医学数据集实证表明 WAST 显著提升检验功效。对您有用：该文处理原假设下参数不可识别的假设检验方法（WAST）及渐近理论，直接契合您在 mathematical statistics (hypothesis testing) 方向的兴趣，且 change-plane 模型在流行病学个性化干预的因果异质性分析中具有应用价值。
- **关键技术**: `change-plane model`, `weighted average of squared score test (WAST)`, `non-regular testing`, `bootstrap approximation`, `generalized estimating equation (GEE)`
- **为什么对您有用**: 直接契合您在 mathematical statistics (hypothesis testing) 的核心兴趣，特别是针对原假设下参数不可识别的非正则检验问题提出了新统计量与渐近理论；同时 change-plane 模型在流行病学个性化干预的因果异质性分析中具有应用价值。

## 统计计算 / 算法  *(stat_computing, 5 篇)*

### 1. [10.5705/ss.202025.0087](https://doi.org/10.5705/ss.202025.0087) — Distributed Algorithms for High-Dimensional Statistical Inference and Structure Learning with Heterogeneous Data
- **作者**: Hongru Zhao, Xiaotong Shen
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在分布式多站点高维异质数据且仅共享汇总统计量的隐私约束设定下，目标是同时估计全局效应与站点特定效应并进行有效推断。方法上，构建异质模型整合全局与局部效应，采用基于差分凸规划（DC programming）的非凸正则化与 ℓ_0 约束以保证选择一致性。尽管底层优化为最坏情况 NP-hard，该算法在现实条件下能以高概率在多项式时间内收敛至全局极小值。推断方面，仅对干扰参数施加 ℓ_0 惩罚而保留目标参数无惩罚，从而获得有效的统计推断。理论上证明了选择一致性与推断有效性，并在多站点临床试验数据中验证了方法。该工作结合了高维推断与分布式计算，其部分惩罚推断策略与计算收敛性分析对您的高维统计与统计计算方向有直接参考价值。
- **关键技术**: `distributed statistical inference`, `high-dimensional heterogeneous model`, `difference of convex (DC) programming`, `ℓ_0 penalization`, `partial penalization`
- **为什么对您有用**: 直接关联您的高维统计与统计计算方向；其仅惩罚干扰参数以实现有效推断的策略（与debiased ML精神一致）以及多项式时间收敛的分布式非凸优化算法，对研究高维异质数据下的debiasing和计算方法有重要借鉴意义。

### 2. [10.5705/ss.202024.0329](https://doi.org/10.5705/ss.202024.0329) — Efficient Decoding from Heterogeneous 1-Bit Compressive Measurements over Networks
- **作者**: Canyi Chen, Zhengtian Zhu, Liping Zhu
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在去中心化网络设定下，研究异质1-bit压缩感知(CS)的高维信号恢复问题，目标estimand为稀疏信号及其支撑集。针对符号函数不连续、符号翻转及网络异质性挑战，将1-bit CS重构为惩罚最小二乘任务。基于此重构，开发了广义交替方向乘子法(ADMM)进行去中心化优化，算法实现简单。理论上证明了算法具有线性收敛速率，且在有限次通信后即可达到近oracle统计收敛率，并在温和条件下保证支撑集可靠恢复。对您可能有用：该工作将高维1-bit CS与去中心化数值优化结合，其ADMM算法设计与近oracle收敛率分析对您在统计计算（数值方法与算法）和高维统计方向的研究有直接参考价值。
- **关键技术**: `1-bit compressive sensing`, `decentralized optimization`, `generalized ADMM`, `penalized least squares`, `near-oracle rate`, `support recovery`
- **为什么对您有用**: 结合了高维统计与统计计算，其去中心化ADMM算法设计与近oracle收敛率证明对您在统计计算（数值算法）和高维稀疏恢复方向的研究有直接参考价值。

### 3. [10.5705/ss.202024.0308](https://doi.org/10.5705/ss.202024.0308) — Heterogeneous Autoregressive Modeling with Flexible Cascade Structures
- **作者**: Huiling Yuan, Guodong Li, Kexin Lu, Alan T.K. Wan, Yong Zhou
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 针对高频数据已实现测度的预测问题，本文在异质自回归 (HAR) 框架下提出多线性低秩异质自回归 (MLRHAR) 模型，用数据驱动方法替代固定波动成分。核心机制是引入四阶张量技术处理日历效应，在响应、预测变量及短期/日历时间方向同时降维，从而自动选择异质成分并缩减参数空间。理论方面，本文建立了高维 HAR 模型的非渐近性质。算法方面，设计了带理论收敛保证的投影梯度下降算法进行参数估计。模拟与标普500成分股实证表明该模型具有显著预测优势。对您而言，其高维非渐近界推导与张量降维优化算法可为高维统计与统计计算方向提供方法论借鉴，同时标普500数据应用契合经济理论兴趣。
- **关键技术**: `multilinear low-rank tensor decomposition`, `non-asymptotic bounds`, `projected gradient descent`, `heterogeneous autoregressive model`, `calendar effect`
- **为什么对您有用**: 高维非渐近性质与张量降维算法直接关联您的高维统计与统计计算兴趣；标普500高频数据应用契合经济理论方向。

### 4. [10.5705/ss.202025.0109](https://doi.org/10.5705/ss.202025.0109) — Communication-Efficient Estimation of Regularized Smoothed Support Tensor Machine
- **作者**: Zihao Song, Lei Wang, Riquan Zhang, Weihua Zhao
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文在张量分类问题中，基于管秩和管核范数正则化提出了平滑支持张量机，并研究其在分布式环境下的通信高效估计。设定中避免了传统张量展开破坏结构信息，采用管核范数刻画低秩结构。核心估计量采用管核范数正则化的 SVM 变体，并在分布式框架下提出仅需主节点局部数据和其余节点梯度信息的通信高效估计量。理论部分建立了该正则化估计量的统计性质，推导了分布式估计量的收敛速率，并利用管核范数性质提供了低秩结构恢复的理论保证。计算上采用交替优化算法求解。对您可能有用：该文将张量管秩正则化与分布式通信高效算法结合，其低秩恢复理论和交替优化算法设计可直接迁移至您关注的统计计算与高维统计（张量/矩阵低秩结构）方向。
- **关键技术**: `tubal nuclear norm regularization`, `smoothed support tensor machine`, `communication-efficient distributed estimation`, `low-rank tensor recovery`, `alternating optimization algorithm`
- **为什么对您有用**: 本文涉及张量低秩正则化与分布式通信高效算法，与您在统计计算（数值方法与算法）及高维统计（矩阵/张量低秩结构）方向的兴趣高度契合；其分布式估计量收敛率与低秩恢复的理论分析可为高维张量推断提供新视角。

### 5. [10.5705/ss.202025.0466](https://doi.org/10.5705/ss.202025.0466) — Out-of-cluster Prediction for Model Selection in Regression with Unsupervised Clustering
- **作者**: Masao Ueki
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在无监督聚类回归（先对解释变量聚类再分组建回归）设定下，目标是选择正确的聚类数及回归模型。本文提出利用簇外预测（out-of-cluster prediction）精度下降的特性，构建模型排除程序（model exclusion procedure），在AIC/BIC选择前剔除冗余模型。针对Cox回归中标准偏似然函数的发散问题，提出归一化偏似然函数以实现稳定的模型选择。理论上证明了AIC结合该排除程序可达到模型选择一致性（model selection consistency），模拟研究（高斯、Logistic、Cox+K-means）证实了其改进效果。对您可能有用：其模型选择一致性证明及Cox似然的数值修正，为您在统计计算（数值方法与算法）和数学统计方向的兴趣提供了具体的方法论参考。
- **关键技术**: `out-of-cluster prediction`, `model exclusion procedure`, `normalized partial log-likelihood`, `model selection consistency`, `unsupervised clustering regression`
- **为什么对您有用**: 模型选择一致性证明与Cox偏似然数值修正算法，对应您在统计计算（数值方法与算法）和数学统计方向的兴趣，提供处理聚类回归模型选择的新颖排除机制与数值稳定化技巧。

## 其他  *(other, 1 篇)*

### 1. [10.5705/ss.202025.0049](https://doi.org/10.5705/ss.202025.0049) — Mirror-Symmetric Orthogonal Latin Hypercubes with Attractive Space-Filling Properties
- **作者**: Chunyan Wang, Min-Qian Liu
- **期刊/来源**: Statistica Sinica
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 本文研究计算机实验中的镜像对称正交拉丁超方体（mirror-symmetric orthogonal Latin hypercubes）的构造问题，目标是在保持正交性与一维最大分层的同时获得高阶正交性和低维空间填充性质。作者基于 Reed-Solomon 码生成的正交阵列提出新的构造方法，理论结果保证所得设计具有正交性、低维空间填充性，部分设计还在 maximin distance 准则下达到最优。模拟比较表明新设计优于现有设计。该方法学 novelty 集中在实验设计构造，与您关注的统计推断理论（因果推断、效率界、高维推断）无直接交集，仅在设计矩阵正交性层面与高维/计算统计有微弱关联。
- **关键技术**: `orthogonal Latin hypercubes`, `mirror-symmetric design`, `Reed-Solomon codes`, `orthogonal arrays`, `maximin distance criterion`, `space-filling design`
- **为什么对您有用**: 与您的主要兴趣方向（因果推断、效率理论、高维统计）基本无直接关联；仅在'正交设计矩阵'这一概念上与高维推断中的设计矩阵条件数问题有极弱的方法论呼应，阅读收益有限。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

