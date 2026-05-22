# Biometrics — Vol 81  Issue 3  ·  2026-05-21

- 共 41 篇 · Biometrics

## 因果推断  *(causal_inference, 5 篇)*

### 1. [10.1093/biomtc/ujaf089](https://doi.org/10.1093/biomtc/ujaf089) — Tree-based additive noise directed acyclic graphical models for nonlinear causal discovery with interactions
- **作者**: Fangting Zhou, Kejun He, Yang Ni
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 在非线性因果发现设定下，传统加性噪声模型（ANM）假设结构因果函数平滑且加性，无法刻画因果交互作用，本文旨在放松该假设并研究其可识别性。提出基于树的ANM（Tree-ANM），利用树结构生成分段常数因果函数以显式建模交互效应。由于分段常数函数破坏了经典ANM的连续/平滑假设，本文给出了Tree-ANM因果可识别性的新理论条件。算法层面，开发了递归源节点识别算法与基于得分（score-based）的排序搜索算法，兼顾计算可行性与可解释性。模拟与乳腺癌蛋白质交互网络数据表明，在存在强因果交互时该方法优于传统ANM。对您有用：本文对分段常数结构方程给出的新因果可识别性条件，直接推进了您在因果推断 identification 方向的理论兴趣，且其排序搜索算法对统计计算子方向有参考价值。
- **关键技术**: `additive noise model`, `causal identifiability`, `tree-based structural equation`, `score-based ordering search`, `piecewise constant function`
- **为什么对您有用**: 直接推进了因果推断中关于 identification 的理论兴趣（分段常数函数下的可识别性条件），且其基于树的排序搜索算法对统计计算与因果发现算法设计有参考价值。

### 2. [10.1093/biomtc/ujaf104](https://doi.org/10.1093/biomtc/ujaf104) — Semiparametric joint modeling to estimate the treatment effect on a longitudinal surrogate with application to chronic kidney disease trials
- **作者**: Xuan Wang, Jie Zhou, Layla Parast, Tom Greene
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在纵向替代终点受终止事件（如死亡或肾衰竭）干扰的设定下，本文研究处理效应对纵向替代指标（如 GFR 斜率）的估计问题。提出半参数联合建模框架：纵向结局采用半参数模型，纵向轨迹与终止事件的关联设定为非参数，终止事件采用半参数 Cox 模型。基于估计方程方法构造处理效应估计量，并允许纵向轨迹的非线性扩展。推导了所提估计量的大样本渐近性质，模拟显示有限样本表现良好，并在 RENAAL 临床试验数据上实证了 Losartan 对 GFR 斜率的效应。对您有用：该工作将半参数联合建模与纵向替代终点的处理效应估计结合，其估计方程推导与半参数渐近理论可直接迁移至您关注的纵向因果推断及流行病学应用场景。
- **关键技术**: `semiparametric joint model`, `estimating equation`, `semiparametric Cox model`, `longitudinal surrogate`, `nonparametric link function`
- **为什么对您有用**: 直接关联您 primary interest 中的纵向因果推断与半参数理论，同时提供了慢性肾病临床试验（epidemiology secondary interest）的真实数据集与分析流程，半参数联合建模的估计方程推导对处理 informative censoring 有方法学迁移价值。

### 3. [10.1093/biomtc/ujaf082](https://doi.org/10.1093/biomtc/ujaf082) — Sparse 2-stage Bayesian meta-analysis for individualized treatments
- **作者**: Junwei Shen, Erica E M Moodie, Shirin Golchi
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多站点个体水平数据无法共享的设定下，目标是估计最优个体化治疗规则（ITR），面临不同站点人群异质性与治疗-协变量交互效应稀疏性的双重挑战。采用两阶段贝叶斯元分析方法：第一阶段各站点独立拟合模型提取后验样本，第二阶段中心节点通过稀疏先验（如spike-and-slab）整合信息以识别非零交互效应。该方法在保护数据隐私的同时，解决了跨站点参数不可识别的问题，并能一致估计刻画最优ITR的参数。模拟显示参数估计具有一致性，实证应用于国际华法林药物基因组学联盟数据。对您有用：该文处理多站点因果推断中异质性与稀疏性的思路，可为分布式因果推断或高维ITR估计提供参考，尽管贝叶斯框架与您关注的半参数效率路径不同。
- **关键技术**: `individualized treatment rules`, `Bayesian meta-analysis`, `spike-and-slab prior`, `multi-site distributed estimation`, `treatment-covariate interaction`
- **为什么对您有用**: 涉及因果推断中的个体化治疗规则（ITR）估计，且处理了多站点异质性与稀疏性问题；虽然采用贝叶斯框架而非您关注的半参数效率路径，但其对分布式因果推断与高维交互效应稀疏性的建模思路具有参考价值。

### 4. [10.1093/biomtc/ujaf102](https://doi.org/10.1093/biomtc/ujaf102) — Sensitivity analysis for attributable effects in case2 studies
- **作者**: Kan Chen, Ting Ye, Dylan S Small
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在 case² (case-case) 研究设计中，目标估计量为第一类案例的归因效应，其识别依赖“处理不导致第二类案例”与“处理不改变案例类型”两个核心不可检验假设。本文提出一套敏感性分析框架，通过引入敏感性参数对上述假设的偏离程度进行参数化，量化假设违反对归因效应推断的影响。同时，该框架整合了对未测量混杂的敏感性分析，评估遗漏变量引入的偏倚。方法推导了在敏感性参数空间下归因效应的识别界与推断程序。实证基于 1993 National Mortality Followback Survey 数据，评估了生前暴力行为对自杀风险归因效应的稳健性。对您有用：直接呼应您 primary interest 中的 causal sensitivity analysis，且提供了流行病学（secondary interest）真实数据的应用范例，其参数化假设偏离的思路可迁移至其他因果设定的敏感性分析。
- **关键技术**: `case-case design`, `attributable effect`, `sensitivity analysis`, `unmeasured confounding`, `partial identification`
- **为什么对您有用**: 直接呼应您 primary interest 中的 causal sensitivity analysis，且作为流行病学（secondary interest）的实证应用，展示了如何在不可验证假设下构建敏感性参数与识别界，方法框架可迁移至其他因果效应的敏感性分析。

### 5. [10.1093/biomtc/ujaf093](https://doi.org/10.1093/biomtc/ujaf093) — Two-stage estimators for spatial confounding with point-referenced data
- **作者**: Nate Wiecha, Jane A Hoppin, Brian J Reich
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在空间回归中，当解释变量与空间相关残差（如未测量环境混杂）相关时会产生空间混杂偏倚，本文针对点参考数据研究该混杂的估计问题。作者将地理加法结构方程模型（gSEM）与双重机器学习（DML）及两阶段半参数回归联系起来，提出双重空间回归（DSR）估计器。DSR 利用带 Matérn 协方差的 Gaussian process 估计空间趋势，通过两阶段正交化消除混杂偏倚。在正则条件下，推导了 DSR 的 n^{-1/2}-CAN 性质、一致性及闭式方差估计。模拟表明在标准空间回归严重偏倚且覆盖率为 0 时，DSR 能有效消除偏倚并达到 nominal coverage。该文将 DML 理论拓展至空间混杂场景，对您在因果推断（空间/未测量混杂）与半参数效率理论（DML 的非参数收敛率要求）交叉方向的研究有直接借鉴价值。
- **关键技术**: `double machine learning`, `spatial confounding`, `Gaussian process regression`, `semiparametric two-stage estimation`, `root-n asymptotic normality`
- **为什么对您有用**: 将 DML/正交化框架应用于空间混杂（未测量混杂的特例），推导了基于 GP nuisance 估计的 n^{-1/2}-CAN 条件，直接契合您在因果推断（混杂识别/敏感性）与效率理论（debiased ML）的核心兴趣。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1093/biomtc/ujaf107](https://doi.org/10.1093/biomtc/ujaf107) — High-dimensional multi-study multi-modality covariate-augmented generalized factor model
- **作者**: Wei Liu, Qingzhi Zhong
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多研究多模态数据整合设定下，本文提出高维广义因子模型，同时纳入额外协变量，目标是对 study-shared 与 study-specific 潜因子及载荷矩阵进行估计与识别。模型涉及 4 个大型潜随机矩阵，观测似然含不可解高维非线性积分，作者采用变分下界（variational lower bound）近似观测对数似然，引入变分后验分布简化推断。通过 profile 变分参数，利用 M-estimation 理论建立参数估计量的渐近性质，并给出可识别性条件以增强模型可解释性。计算上设计变分 EM 算法，提出共享因子与特定因子数目的选择准则；模拟与真实数据表明估计精度和计算效率优于现有方法。对您而言，高维因子模型结构与 RMT 中 spiked covariance model 有自然联系，变分 EM 框架可作统计计算方向参考，但渐近理论基于 M-estimation 而非 semiparametric efficiency bound，方法学新颖性中等。
- **关键技术**: `variational lower bound`, `variational EM algorithm`, `M-estimation theory`, `generalized factor model`, `identifiability conditions`, `profile variational parameters`
- **为什么对您有用**: 高维潜因子模型与您关注的 RMT（spiked model）直接相关，变分 EM 计算框架对统计计算兴趣有参考价值；但渐近理论走 M-estimation 路线而非 efficiency bound / debiased ML，核心方法与您 primary interest 的重叠偏间接。

## 非参数 / 半参数  *(nonparam_semipara, 10 篇)*

### 1. [10.1093/biomtc/ujaf123](https://doi.org/10.1093/biomtc/ujaf123) — Binary regression and classification with covariates in metric spaces
- **作者**: Yinan Lin, Zhenhua Lin
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 9/10 · novelty: `new_theory`
- **摘要**: 本文研究协变量位于一般度量空间（无向量结构）时的二分类回归与分类问题，提出受 logistic 回归启发的回归模型。针对度量空间回归系数，作者提出极大似然估计量（MLE），并在多种度量熵条件下导出估计误差上界。对常见度量空间推导了匹配的极小极大下界，从而建立了 MLE 的极小极大最优性。在黎曼流形上，进一步给出了更精细的上下界，证明了分类器的最优性。对您有用：该文将非参数极小极大理论（度量熵、收敛率）拓展至非欧几里得结构数据，对您关注的非参数/半参数理论及数学统计中的极小极大率有直接参考价值。
- **关键技术**: `maximum likelihood estimation`, `metric entropy`, `minimax lower bounds`, `Riemannian manifold`, `binary regression`
- **为什么对您有用**: 直接关联您 primary interest 中的非参数/半参数理论与数学统计，展示了如何利用度量熵与极小极大理论在非欧几里得空间建立收敛率与最优性，理论工具可迁移。

### 2. [10.1093/biomtc/ujaf101](https://doi.org/10.1093/biomtc/ujaf101) — Smooth and shape-constrained quantile distributed lag models
- **作者**: Yisen Jin, Aaron J Molstad, Ander Wilson, Joseph Antonelli
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在环境流行病学的分布式滞后模型（DLM）设定下，传统方法仅建模条件均值，无法捕捉暴露-结局关系的异质性及临床关注的极端分位数，本文旨在估计具有平滑和形状约束（如单峰性、凹性）的分位数分布式滞后模型（QDLM）。作者提出两种新的 QDLM 估计量，通过在分位数回归框架下施加平滑性与形状约束，增强了滞后效应曲线的可解释性并提升了估计效率。形状约束在半参数模型中通常能带来更优的收敛速率或效率；实证上，该方法应用于科罗拉多出生队列数据，成功识别了孕期污染对出生体重极端分位数影响的易感关键窗口。该文将形状约束引入分位数半参数估计的思路，对您在半参数效率理论及流行病学应用中的纵向暴露推断具有方法迁移价值。
- **关键技术**: `quantile distributed lag models`, `shape constraints (unimodality, concavity)`, `semiparametric quantile regression`, `critical window identification`, `smoothness regularization`
- **为什么对您有用**: 结合了您在半参数理论（形状约束提升效率/收敛率）和流行病学（出生队列环境暴露数据及关键窗口识别）两个方向的兴趣，提供了分位数半参数估计在流行病学中应用的具体范式。

### 3. [10.1093/biomtc/ujaf097](https://doi.org/10.1093/biomtc/ujaf097) — Covariance-on-covariance regression
- **作者**: Yi Zhao, Yize Zhao
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出协方差对协方差回归模型，设定中假设存在（至少）一对分别作用于结局协方差矩阵和预测协方差矩阵的线性投影，使得投影空间中的方差通过 log-linear 模型关联，并可纳入额外协变量。提出 OLS 型估计量同时识别投影方向与估计回归系数，在正则条件下证明估计量的渐近一致性。核心技术工具为矩阵投影的联合估计与 log-link 参数化，但理论结果仅到一致性而未触及效率界或 minimax rate。模拟显示优于现有方法，应用于 Human Connectome Project Aging 数据，识别出 3 对脑网络（全局信号网络、任务相关与任务无关网络），静息态功能连接预测任务态功能连接。对您而言，该文的矩阵回归建模思路可迁移至高维协方差结构推断场景，但理论深度有限，主要价值在于协方差回归这一建模框架本身。
- **关键技术**: `covariance-on-covariance regression`, `linear projection identification`, `log-linear link model`, `OLS-type joint estimator`, `asymptotic consistency`, `matrix regression`
- **为什么对您有用**: 协方差矩阵回归的建模框架与您的高维统计（协方差结构推断）和统计计算（矩阵方法）兴趣相邻，但理论仅到一致性、未触及效率界或更精细的收敛率，读后主要收益是了解协方差对协方差这一新回归范式的设计思路。

### 4. [10.1093/biomtc/ujaf090](https://doi.org/10.1093/biomtc/ujaf090) — Adjusted predictions for generalized estimating equations
- **作者**: Francis K C Hui, Samuel Muller, Alan H Welsh
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在纵向数据的广义估计方程 (GEE) 框架下，针对新时间点的预测问题，传统方法仅依赖边际均值模型，本文提出一种利用簇内工作互相关性的调整预测方法。核心机制是将 GEE 视为求解迭代工作线性模型，并借鉴泛克里金 (universal kriging) 思想，构建利用当前与新观测间工作交叉相关性的调整预测量。理论上，作者建立了调整 GEE 预测量优于标准 GEE 预测量的严格条件，证明即使在工作相关结构误设时，该方法仍能提升预测精度。模拟与 Sitka spruce 生长纵向数据应用表明，该调整预测量不仅优于标准 GEE 和使用全部时间点的“神谕” GEE 预测量，甚至在某些情况下优于广义线性混合模型 (GLMM) 的簇特定预测。对您有用：该文将 kriging 思想引入 GEE 的纵向预测，其理论分析框架对您在纵向因果推断中处理工作相关结构与边际模型交互具有参考价值。
- **关键技术**: `generalized estimating equations`, `universal kriging`, `working correlation matrix`, `iterative working linear model`, `longitudinal prediction`
- **为什么对您有用**: 与您关注的纵向因果推断和半参数理论相关：GEE是纵向数据边际建模的核心半参数工具，本文通过kriging调整利用工作相关结构改进预测的理论条件，对纵向因果推断中处理时间依赖相关性和边际估计具有方法学迁移价值。

### 5. [10.1093/biomtc/ujaf118](https://doi.org/10.1093/biomtc/ujaf118) — Nonparametric Bayesian approach for dynamic borrowing of historical control data
- **作者**: Tomohiro Ohigashi, Kazushi Maruo, Takashi Sozu, Masahiko Gosho
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在将历史对照数据整合到当前 RCT 分析的设定下，目标是处理由未测量因素导致的试验间异质性，实现动态借力（dynamic borrowing）。作者提出基于 Dirichlet process（DP）混合的非参数贝叶斯方法，并进一步引入 dependent DP mixture 以强化历史对照与当前对照之间的冲突检测与降权机制；该方法对聚合层面数据与个体层面数据统一适用。此外，基于目标参数的后验分布构造了新的试验间相似性指标。模拟与实例分析表明，dependent DP mixture 在异质性场景下能更准确地从同质历史对照借力、同时抑制异质对照的影响，优于典型 DP mixture 及 meta-analytic 方法。对您而言，该文提供了 Bayesian nonparametrics 处理未测量异质性的思路，可与您关注的 proximal CI 中 negative-control 设定下未测量混杂的处理逻辑做对比，但方法框架（贝叶斯 vs 频率）差异较大。
- **关键技术**: `Dirichlet process mixture`, `dependent Dirichlet process`, `dynamic borrowing`, `posterior similarity index`, `historical control integration`
- **为什么对您有用**: 与您关注的 causal inference 中未测量混杂处理（proximal CI / sensitivity analysis）有场景重叠，但方法路径为贝叶斯非参数而非频率半参数/效率理论，主要价值在于了解 DP mixture 在异质性借力中的冲突解决机制，可作对比参考。

### 6. [10.1093/biomtc/ujaf083](https://doi.org/10.1093/biomtc/ujaf083) — Frequency band analysis of nonstationary multivariate time series
- **作者**: Raanju R Sundararajan, Scott A Bruce
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在多元局部平稳时间序列设定下，本文研究如何以数据驱动方式识别频域分割点，从而最优总结非平稳动态特征。核心构造是基于 L2 范数的差异度量，用于捕捉时变谱密度矩阵在频率上的变点，并推导了其渐近性质。提出非参数 bootstrap 检验来识别显著的频率分割点，以及谱矩阵中随频率变化的分量与交叉分量，避免了依赖预定义频带。模拟与静息态脑电图（EEG）应用验证了方法提取时变频带特征的有效性。对您可能有用：本文的非参数 bootstrap 检验构造与谱矩阵渐近理论，可为非参数假设检验及复杂依赖结构下的推断提供方法学参考。
- **关键技术**: `time-varying spectral density matrix`, `L2-norm discrepancy measure`, `nonparametric bootstrap test`, `locally stationary time series`, `frequency-domain partition`
- **为什么对您有用**: 本文涉及非参数假设检验与渐近性质推导，与您在数学统计（假设检验）及非参数理论方面的兴趣直接相关，其针对复杂依赖结构的 bootstrap 检验构造思路可迁移借鉴。

### 7. [10.1093/biomtc/ujaf105](https://doi.org/10.1093/biomtc/ujaf105) — A monotone single index model for spatially referenced multistate current status data
- **作者**: Snigdha Das, Minwoo Chae, Debdeep Pati, Dipankar Bandyopadhyay
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在空间相关的多状态当前状态数据下，目标是估计疾病状态转移时间，设定为仅观测单次随机检查时间的状态快照且存在空间聚类。提出贝叶斯半参数加速失效时间模型，误差项采用高斯Dirichlet过程混合，空间随机效应使用逆Wishart提议。系统成分采用单调单指标模型，未知联系函数通过积分基展开估计，基系数赋予约束高斯过程先验以保证单调性。计算上结合椭圆切片采样、快速循环嵌入技术及硬约束平滑，实现参数与状态转移概率的高效推断，并证明了参数可识别性。仿真与牙周病真实数据验证了方法的有限样本性质及模型误设下的稳健性。该文的半参数单指标建模（约束GP先验）与快速循环嵌入计算技巧，对您在半参数理论与统计计算方向的研究有直接参考价值。
- **关键技术**: `monotone single index model`, `Dirichlet process mixture`, `constrained Gaussian process prior`, `elliptical slice sampling`, `circulant embedding`, `accelerated failure time model`
- **为什么对您有用**: 结合了半参数单指标模型（约束GP先验）与高效MCMC计算（循环嵌入、椭圆切片采样），直接对应您在半参数理论与统计计算上的主要兴趣；同时多状态当前状态数据的应用场景对流行病学方向有参考价值。

### 8. [10.1093/biomtc/ujaf095](https://doi.org/10.1093/biomtc/ujaf095) — Valid and efficient inference for nonparametric variable importance in two-phase studies
- **作者**: Guorong Dai, Raymond J Carroll, Jinbo Chen
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在两阶段抽样设计下（大量(Y,X)观测，昂贵协变量Z仅在小子样本中测量），目标是推断Z对预测Y的非参数变量重要性，该参数通过一般损失函数聚合Z在预测模型中的最大潜在贡献来定义。方法核心：用(Y,X)的函数替代每个个体对涉及Z的预测损失的贡献，从而在Z缺失时仍能估计重要性参数。理论上，该方法在Z贡献为零或为正时均实现统一且有效的推断——边界点（零重要性）通常导致非正则性使标准渐近理论失效，但此处因缺失数据结构反而获得了这一性质。作为中间理论贡献，作者在半监督推断和两阶段非参数估计两个领域建立了新结果。数值模拟和真实数据均验证了方法的优越表现。对您有用：该工作直接推进了非参数效率理论在缺失数据/两阶段设计下的边界推断问题，且两阶段设计在流行病学队列研究中极为常见，方法可迁移至您关注的epidemiology应用场景。
- **关键技术**: `nonparametric variable importance`, `two-phase design`, `efficient influence function`, `boundary inference`, `semi-supervised inference`, `missing data substitution`
- **为什么对您有用**: 直接推进非参数效率理论在两阶段缺失数据下的边界推断（零重要性时仍n^{-1/2}-CAN且有效），且两阶段设计在流行病学中常见，方法可迁移至您关注的epidemiology因果应用场景。

### 9. [10.1093/biomtc/ujaf122](https://doi.org/10.1093/biomtc/ujaf122) — Exploring the heterogeneity in recurrent episode lengths based on quantile regression
- **作者**: Yi Liu, Guillermo E Umpierrez, Limin Peng
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究慢性病中复发事件持续时间（recurrent episode lengths）的异质性问题，目标是在依赖删失、依赖截断与信息性簇大小（informative cluster size）共存时，对分位数回归系数进行估计与推断，不要求个体内发作时长满足可交换性或特定分布假设。方法将复发发作视为聚类数据，采用分位数回归纳入时变协变量，提出相应的估计程序以同时处理上述三种复杂特征。估计量具有 n^{-1/2}-CAN 性质及理想的渐近分布，计算实现简单。数值模拟表明该方法优于现有方法的朴素适配。该工作对您有用之处在于：分位数回归框架下处理 informative cluster size 与 dependent censoring/truncation 的半参数推断思路，可迁移至纵向因果推断中复发结局的 semiparametric efficiency 讨论及流行病学队列数据分析。
- **关键技术**: `quantile regression`, `informative cluster size`, `dependent censoring`, `dependent truncation`, `recurrent episode clustering`, `n^{-1/2}-CAN estimation`
- **为什么对您有用**: 半参数分位数回归处理 informative cluster size 与 dependent censoring/truncation 的推断框架，可直接迁移至您关注的纵向因果推断中复发结局的 semiparametric theory，同时该文的应用场景（慢性病队列）对您 epidemiology secondary interest 有数据集价值。

### 10. [10.1093/biomtc/ujaf100](https://doi.org/10.1093/biomtc/ujaf100) — Regression analysis of interval-censored failure time data with change points and a cured subgroup
- **作者**: Yichen Lou, Mingyue Du, Xinyuan Song
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在区间删失生存数据下，本文研究包含治愈亚组和变点的回归问题，设定为部分线性变换模型与混合治愈模型框架。提出基于 Bernstein 多项式与分段线性函数的筛最大似然估计（sieve MLE）进行推断，并设计了数据驱动的自适应程序以识别变点的数量与位置。理论上建立了筛估计量与变点估计的渐近性质（包括收敛率与渐近分布）。仿真与乳腺癌真实数据验证了方法实用性。对您而言，该文是筛方法在复杂生存数据中的典型应用，其变点识别的渐近理论推导对您关注的半参数理论及流行病学应用有直接参考价值。
- **关键技术**: `sieve maximum likelihood estimation`, `partly linear transformation model`, `mixture cure model`, `Bernstein polynomial`, `change point detection`, `interval-censored data`
- **为什么对您有用**: 涉及您关注的半参数理论（sieve MLE 及其渐近性质）和流行病学应用（乳腺癌区间删失数据），变点识别的渐近理论推导对研究复杂半参数模型有参考价值。

## 效率理论 / Debiased ML  *(efficiency_dml, 2 篇)*

### 1. [10.1093/biomtc/ujaf084](https://doi.org/10.1093/biomtc/ujaf084) — Doubly robust nonparametric estimators of the predictive value of covariates for survival data
- **作者**: Torben Martinussen, Mark J van der Laan
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在生存数据设定下，研究如何评估新标记物在已有预测因子基础上的增量预测价值，目标 estimand 为基于非参数评分规则的正预测值（PPV）曲线。将该 estimand 视为数据生成分布的单一变换，通过推导其 efficient influence function (EIF) 构建了双重稳健（doubly robust）的非参数估计量。该方法不依赖强参数假设，利用 EIF 保证了估计量在部分模型误判下的鲁棒性，并建立了相应的渐近理论（如 n^{-1/2}-CAN 性质）。数值模拟和两个癌症数据集的应用验证了方法的实际表现。对您有用：本文是利用 efficient influence function 构建双重稳健估计量的典型范例，直接契合您在 semiparametric efficiency bounds 方面的核心兴趣，且其癌症流行病学应用对您的 secondary interest 有数据集参考价值。
- **关键技术**: `efficient influence function`, `doubly robust estimation`, `positive predictive value curve`, `nonparametric scoring rule`, `survival analysis`
- **为什么对您有用**: 直接展示了如何通过推导 efficient influence function 构建双重稳健估计量，完美契合您在 semiparametric efficiency bounds 和 nonparametric theory 方面的核心兴趣；同时癌症数据应用对您的流行病学 secondary interest 有参考价值。

### 2. [10.1093/biomtc/ujaf098](https://doi.org/10.1093/biomtc/ujaf098) — Causal machine learning for heterogeneous treatment effects in the presence of missing outcome data
- **作者**: Matthew Pryce, Karla Diaz-Ordaz, Ruth H Keogh, Stijn Vansteelandt
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在结果变量缺失（MAR）的设定下，本文研究条件平均处理效应（CATE）的识别与估计，关键假设为缺失机制仅依赖协变量。提出两种 debiased ML 估计器 mDR-learner 与 mEP-learner，通过在 DR-learner 和 EP-learner 中整合逆概率删失权重（IPCW）来修正子群代表性不足导致的偏差。理论上证明在 nuisance 函数（倾向得分与缺失概率）以 o(n^{-1/4}) 速率收敛的条件下，这两种估计器具有 oracle efficiency，即 CATE 估计可达 n^{-1/2}-CAN 且达到半参数有效界。模拟结果表明其优于直接删除或简单插补的基线方法，并在 GBSG2 乳腺癌临床试验中展示了激素疗法的异质性处理效应。对您有用：该文将 IPCW 与 debiased ML 框架结合处理缺失数据，其 oracle efficiency 的推导思路可直接迁移到您关注的 debiased ML 与效率理论研究中。
- **关键技术**: `debiased machine learning`, `conditional average treatment effect`, `inverse probability of censoring weighting`, `DR-learner`, `EP-learner`, `oracle efficiency`
- **为什么对您有用**: 直接关联您 primary interest 中的 debiased ML 与效率理论，展示了如何在缺失数据下保持 CATE 估计的 oracle efficiency；同时其临床试验应用属于 epidemiology 的因果推断范畴，提供了可复用的真实数据分析流程。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1093/biomtc/ujaf114](https://doi.org/10.1093/biomtc/ujaf114) — Revisiting optimal allocations for binary responses: insights from considering type-I error rate control
- **作者**: Lukas Pin, Sofía S Villar, William F Rosenberger
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在二分类响应的最优响应自适应设计（response-adaptive design, RAD）中，本文系统揭示了此类设计在原假设下会加剧 type-I error rate 膨胀——该现象此前未被充分记录。作者考察了文献中多种缓解膨胀的策略（如条件随机化、方差膨胀修正等），发现均无法给出稳健解。为此，通过在优化问题中用 score test 替代 Wald test、用有限样本估计量替代未知真值，推导出两个新最优分配比例：一个最大化检验功效，另一个在固定方差约束下最小化试验失败总数。模拟（早期与确证性试验场景）表明新分配在控制 type-I error 的同时可显著改善患者结局；框架可自然推广至其他结局类型与多臂试验。对您而言，该文在自适应随机化下 score/Wald 检验的有限样本 type-I error 差异及修正机制方面提供了具体参考，与您 hypothesis testing 方向的兴趣直接相关。
- **关键技术**: `response-adaptive randomization`, `score test vs Wald test`, `optimal allocation proportion`, `type-I error rate inflation`, `finite-sample estimator correction`, `power optimization under variance constraint`
- **为什么对您有用**: 直接关联您 primary interest 中的 hypothesis testing——自适应设计下 score test 与 Wald test 的 type-I error 表现差异及有限样本修正是检验理论中值得了解的视角；若您关注随机化推断或试验设计中的检验问题，此文提供了具体的技术对比与新分配公式。

### 2. [10.1093/biomtc/ujaf120](https://doi.org/10.1093/biomtc/ujaf120) — Statistical significance of clustering for count data
- **作者**: Yifan Dai, Di Wu, Yufeng Liu
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对高维计数数据（如单细胞RNA测序与电子病历），研究聚类结果统计显著性的假设检验问题，原假设为数据来自单一离散分布。现有SigClust方法主要针对连续高斯数据，在非高斯离散数据下面临功效不足的缺陷。作者提出SigClust-DEV方法，基于偏差构建检验统计量，并在原假设下通过拟合离散分布进行Monte Carlo模拟来计算p值。该方法克服了高维非高斯设定下检验统计量分布难以解析求解的困难，有效控制了第一类错误并提升了检验功效。模拟与真实数据表明SigClust-DEV在计数数据上优于现有方法。对您有用之处：提供了一个高维离散数据假设检验的具体框架，可关注其如何处理非高斯高维数据的检验统计量与显著性评估，对您在假设检验方向的思考有参考价值。
- **关键技术**: `SigClust`, `deviance-based test statistic`, `Monte Carlo hypothesis testing`, `high-dimensional count data`, `single-cell RNA-seq analysis`
- **为什么对您有用**: 本文核心是高维非高斯数据的假设检验问题，直接关联您在 mathematical statistics (hypothesis testing) 和 high-dimensional statistics 方面的兴趣；虽然理论深度可能不及RMT，但其处理高维离散数据检验统计量的思路可作借鉴。

### 3. [10.1093/biomtc/ujaf086](https://doi.org/10.1093/biomtc/ujaf086) — Multiple tests for restricted mean time lost with competing risks data
- **作者**: Merle Munko, Dennis Dobler, Marc Ditzhaus
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在竞争风险框架下，本文研究受限平均损失时间（RMTL）的多重检验问题，RMTL 定义为累积发生函数至预设时间点的曲线下面积。现有 RMTL 检验仅限两样本比较且多为两种事件类型，本文提出基于 Wald-type 统计量的一般对比检验，适用于因子设计与任意事件类型数。关键地，作者去掉了事件时间分布的连续性假设，允许数据中存在结（ties），这在实际中（如按整天测量）常见。为改善小样本表现，进一步提出基于置换的检验方法；在多重检验步骤中，利用局部检验统计量之间的渐近精确依赖结构以提升功效。模拟显示小样本表现良好，并以白血病患者骨髓移植数据作实证分析。对您而言，该文在多重检验中利用依赖结构提升功效的思路，以及放松连续性假设的技术处理，可迁移至您关注的假设检验与半参数理论中的相关场景。
- **关键技术**: `Wald-type test statistic`, `competing risks cumulative incidence`, `permutation test`, `multiple testing with dependence structure`, `restricted mean time lost`, `factorial design contrast test`
- **为什么对您有用**: 直接关联您在假设检验方向的兴趣：多重检验中利用渐近精确依赖结构提升功效的思路具有方法学迁移价值；放松连续性假设的技术处理对半参数理论中正则条件讨论有参考意义；流行病学数据集（骨髓移植）也可作为竞争风险场景的实证素材。

## 统计计算 / 算法  *(stat_computing, 4 篇)*

### 1. [10.1093/biomtc/ujaf121](https://doi.org/10.1093/biomtc/ujaf121) — The Cox-Pólya-Gamma algorithm for flexible Bayesian inference of multilevel survival models
- **作者**: Benny Ren, Jeffrey S Morris, Ian Barnett
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文在 Bayesian Cox 半参数回归框架下，提出 Cox-Pólya-Gamma 算法以统一处理多水平生存模型（case weights、frailties、smoothing splines）。核心利用 Cox 模型的椭圆信息几何，通过 Poisson 过程将 Cox 模型近似为负二项过程，从而将 Bayesian 计算归约为迭代 Gaussian 采样；再借助充分维数缩减，以 beta 充分统计量折叠 Gibbs sampler 中的 Markov transition，简洁地解决非参数基准累积危险率的单调性约束问题。理论上给出了算法一致遍历性（uniform ergodicity）的条件。该方法将多水平 Cox 回归的计算简化为几行代码即可实现。对您而言，该文在半参数 Cox 模型的计算策略（Gibbs collapse、维数缩减）上提供了可迁移的思路，尤其对统计计算方向中复杂约束下的采样器设计有参考价值。
- **关键技术**: `Pólya-Gamma data augmentation`, `elliptical information geometry of Cox models`, `negative binomial process approximation via Poisson process`, `sufficient dimension reduction in Gibbs sampler`, `monotonicity-constrained cumulative hazard`, `uniform ergodicity of Markov chains`
- **为什么对您有用**: 虽然该文聚焦 Bayesian 生存分析而非您核心的频率派效率理论，但其半参数 Cox 模型设定与统计计算中的 Gibbs collapse 和维数缩减策略，对您在统计计算方向（尤其是带约束的半参数模型采样器设计）有直接的方法论借鉴价值。

### 2. [10.1093/biomtc/ujaf112](https://doi.org/10.1093/biomtc/ujaf112) — Model robust designs for dose-response models
- **作者**: Belmiro P M Duarte, Anthony C Atkinson, Nuno M C Oliveira
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在剂量-反应建模中，真实模型形式通常未知但属于有限候选模型池，本文研究在此模型不确定性下的近似最优模型稳健实验设计。针对包含非线性模型的局部最优设计，作者提出了三种基于半定规划（SDP）的求解框架，分别对应 Läuter 提出的三类模型稳健性准则。通过利用稳健性准则的半定可表示性，将稳健设计问题转化为半定规划问题；同时采用标准化设计以确保不同模型间信息矩阵的可比性。理论上给出了 SDP 求解的保证，实证以包含七个候选剂量-反应模型的研究展示了方法的有效性。对您可能有用：SDP 求解框架可迁移至您在统计计算中的优化问题，且模型稳健设计与信息矩阵的理论触及您关注的效率理论（efficiency theory）。
- **关键技术**: `Semidefinite Programming (SDP)`, `model robust experimental design`, `Läuter robustness criteria`, `standardized designs`, `locally optimal design`, `Fisher information matrix`
- **为什么对您有用**: 涉及统计计算中的半定规划（SDP）数值优化求解框架，且模型稳健设计与信息矩阵的理论触及您关注的效率理论（efficiency theory）；剂量-反应应用也与流行病学背景相关。

### 3. [10.1093/biomtc/ujaf110](https://doi.org/10.1093/biomtc/ujaf110) — Mastering rare event analysis: subsample-size determination in Cox and logistic regressions
- **作者**: Tal Agassi, Nir Keret, Malka Gorfine
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在超大规模数据集下，现有最优子采样方法（如基于似然的 subsampling）虽能减少效率损失，但缺乏如何选择子样本量的系统工具。本文针对三类场景——稀有事件的 Cox 回归、平衡与不平衡数据的 logistic 回归——提出了子样本量确定方法，并针对不平衡 logistic 回归给出了新的最优子采样程序。核心技术路线基于估计量的渐近方差与全样本方差的比值，推导出在给定效率损失容忍度下所需的最小子样本量公式；对不平衡 logistic 回归，通过重新设计采样权重使稀有类信息被更充分利用。模拟与两个大规模数据集（UK Biobank 结直肠癌生存数据约 3.5 亿行、关联出生与婴儿死亡数据约 2800 万观测）验证了方法的有效性。对您而言，子样本量确定工具可直接用于大规模流行病学队列的计算加速，且不平衡 logistic 子采样权重设计可迁移到其他稀有事件因果推断场景。
- **关键技术**: `optimal subsampling`, `subsample-size determination`, `Cox regression rare events`, `imbalanced logistic regression`, `asymptotic relative efficiency`, `weighted subsampling`
- **为什么对您有用**: 直接关联您 primary interest 中的 statistical computing（大规模数据的子采样算法设计），同时两个真实数据集（UK Biobank、出生死亡关联数据）对您 secondary interest 的流行病学应用有数据集价值；不平衡 logistic 子采样权重设计可迁移到稀有暴露/treatment 的因果推断场景。

### 4. [10.1093/biomtc/ujaf117](https://doi.org/10.1093/biomtc/ujaf117) — A group distributional ICA method for decomposing multi-subject diffusion tensor imaging
- **作者**: Guangming Yang, Ben Wu, Jian Kang, Ying Guo
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 针对多被试扩散张量成像（DTI）数据的降维与盲源分离问题，本文提出组分布独立成分分析（G-DICA）方法，以处理 3D 正定扩散张量带来的分布约束。传统 ICA 无法直接作用于 DTI 张量数据，G-DICA 转而对观测数据分布函数中的参数进行混合独立源信号分解。该方法在多被试层面实现了张量数据的联合分解，从而提取出对应主要白质纤维束的结构网络。模拟与真实数据应用表明，G-DICA 在重现性与分离性能上优于现有方法。对您而言，该文展示了针对特殊矩阵/张量数据（如 SPD 矩阵）的统计计算与分解算法设计，但缺乏渐近效率或高维理论，主要提供计算与应用视角的参考。
- **关键技术**: `Group Distributional ICA`, `blind source separation`, `diffusion tensor decomposition`, `multi-subject analysis`, `distribution function parameter separation`
- **为什么对您有用**: 涉及统计计算中的张量/矩阵分解算法设计，但缺乏您关注的半参数效率或高维理论，仅作为特殊数据结构（正定张量）计算方法的参考。

## 流行病学  *(epidemiology, 7 篇)*

### 1. [10.1093/biomtc/ujaf103](https://doi.org/10.1093/biomtc/ujaf103) — Evaluating longitudinal treatment effects for Duchenne muscular dystrophy using dynamically enriched Bayesian small sample, sequential, multiple assignment randomized trial (snSMART)
- **作者**: Sidi Wang, Satrajit Roychoudhury, Kelley M Kidwell
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 7/10 · novelty: `application`
- **摘要**: 在小样本序贯多重分配随机试验（snSMART）框架下，目标是评估杜氏肌营养不良症（DMD）的纵向处理效应，关键假设包括外部对照与试验数据间的基线混杂可测量性及数据源间无不可观测冲突。方法采用两步稳健元分析整合外部对照数据：第一步调整基线混杂（propensity-type weighting），第二步以 Bayesian 层级模型融合信息；同时引入分段模型（piecewise model）处理 SMART 设计中阶段依赖的处理分配，并纳入基线协变量刻画患者异质性。理论贡献有限，未给出收敛率或效率界；主要在 DMD 案例中展示该方法相比仅用试验数据的分析可提升后验精度。对您而言，该文提供了 SMART/动态处理策略（DTR）在罕见病纵向因果推断中的应用实例，外部对照借用的 meta-analytic 策略可迁移至其他小样本因果设定，但方法为 Bayesian 参数路线，非半参数效率路线。
- **关键技术**: `snSMART design`, `Bayesian hierarchical model`, `robust meta-analytic external control borrowing`, `piecewise model for stage-wise assignment`, `dynamic treatment regime`, `propensity-type confounding adjustment`
- **为什么对您有用**: 涉及纵向因果推断（SMART/DTR 设计）与流行病学罕见病应用，外部对照借用的两步策略可迁移至其他小样本因果设定；但方法为 Bayesian 参数路线，对半参数效率理论和高维推断的直接启发有限。

### 2. [10.1093/biomtc/ujaf088](https://doi.org/10.1093/biomtc/ujaf088) — Simple simulation based reconstruction of incidence rates from death data
- **作者**: Simon N Wood
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 3/10 · novelty: `minor`
- **摘要**: 在已知感染至死亡时间分布的设定下，研究如何从每日死亡数据回推每日发病率。现有方法依赖简化非线性动力学模型（易引入模型伪影）或样条反卷积（技术门槛高且不透明）。本文提出一种基于模拟的简单重构方法，仅需最小假设，通过模拟延迟分布来反推发病轨迹，并允许对备择假设轨迹进行检验。该方法透明、易于快速部署，适用于类似 COVID 的公共卫生紧急情况。对您而言，该文展示了流行病学中延迟分布反卷积问题的简化计算思路，虽缺乏半参数/效率理论深度，但可作为流行病学数据重构的应用案例参考。
- **关键技术**: `simulation-based reconstruction`, `infection-to-death distribution`, `deconvolution`, `epidemic trajectory inference`
- **为什么对您有用**: 涉及流行病学（secondary interest）中的发病率重构与延迟分布反卷积问题；虽然方法刻意避开深度的半参数/样条理论，但作为流行病学应用中反卷积推断的简化计算案例，有助于理解该领域的数据结构与建模痛点。

### 3. [10.1093/biomtc/ujaf049](https://doi.org/10.1093/biomtc/ujaf049) — Cumulative incidence function estimation using population-based biobank data
- **作者**: Malka Gorfine, David M Zucker, Shoval Shoham
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在基于人群的生物银行数据框架下，目标是估计累积发生率函数（CIF），设定包含招募时报告发病年龄的患病病例与随访新发病例，面临左截断与信息利用不充分的问题。现有方法通常舍弃患病病例信息；本文提出一种新 CIF 估计量，通过有效整合患病病例数据实现双重优势：提升估计效率与将 CIF 估计外推至招募年龄下限 $c_L$ 之前。方法核心在于处理左截断与患病采样下的似然重构与信息整合。主要结果表明该估计量在生物银行数据下具有效率优势与更宽的估计范围；对您在流行病学队列数据（secondary interest）的因果/生存分析应用有直接参考价值，其效率提升机制也可与半参数效率理论（primary interest）结合思考。
- **关键技术**: `cumulative incidence function`, `prevalent sampling`, `left-truncation`, `efficiency gain`, `biobank data`
- **为什么对您有用**: 直接关联您的流行病学（secondary interest）应用兴趣，提供了生物银行数据结构下的新估计方法；同时“效率提升”的核心机制对您在半参数效率理论（primary interest）方面的研究有启发。

### 4. [10.1093/biomtc/ujaf119](https://doi.org/10.1093/biomtc/ujaf119) — Joint disease mapping for bivariate count data with residual correlation due to unknown number of common cases
- **作者**: Edouard Chatignoux, Zoé Uhry, Laurent Remontet, Isabelle Albert
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在空间流行病学双变量计数（如两种疾病）的联合建模中，传统 Poisson 共享成分模型 (P-SCM) 假设潜变量完全捕获了结果间的相关性。本文证明当两种疾病存在未知数量的共同病例时，双变量计数会产生正的“残差”相关性，P-SCM 会将其错误归因于潜变量协方差，导致推断偏倚。为修正此偏倚，作者提出基于双变量 Poisson 分布的 BP-SCM，将每个计数分解为共同病例与不同病例的计数，并使用高斯马尔可夫随机场 (GMRF) 对这三个计数分别建模。模型在贝叶斯框架下采用 Hamiltonian Monte Carlo (HMC) 进行推断。模拟与真实数据表明 BP-SCM 消除了 P-SCM 的偏倚并提升了预测性能，同时输出共同/不同病例的空间变异等流行病学信息。对您而言，该文展示了在流行病学空间数据中处理残差相关性的贝叶斯潜变量分解策略，对在流行病学或经济学计数数据中构建类似潜变量结构具有方法迁移价值。
- **关键技术**: `Bivariate Poisson distribution`, `Shared component model`, `Gaussian Markov Random Fields`, `Hamiltonian Monte Carlo`, `Bayesian latent variable model`
- **为什么对您有用**: 属于流行病学应用方向，展示了在空间计数数据中通过潜变量分解修正偏倚的贝叶斯建模方法，对您在流行病学数据集上处理相关计数结果或潜变量结构有参考价值。

### 5. [10.1093/biomtc/ujaf116](https://doi.org/10.1093/biomtc/ujaf116) — Estimating associations between cumulative exposure and health via generalized distributed lag non-linear models using penalized splines
- **作者**: Tianyi Pan, Hwashin Hyun Shin, Glen McGee, Alex Stringer
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在广义分布滞后非线性模型（DLNM）框架下，研究累积环境暴露与健康结局的关联，目标参数为累积暴露-响应曲线在广义响应（如计数数据）下的估计。方法上，将现有仅适用于连续结局的 ACE-DLNM 扩展至广义响应类型，引入 penalized splines 对暴露-滞后-响应三维关系进行半参数建模，并通过 profile likelihood 与 Laplace 近似边际似然（LAML）结合 Newton 型算法实现惩罚参数的高效选择与估计。模拟显示该方法在计算可扩展性和推断稳定性上优于固定暴露窗口的广义可加模型；应用于 2001–2018 年加拿大空气污染与呼吸系统住院数据，获得了更稳定且可解释的推断。对您而言，penalized spline 的 LAML 选择机制与 profile Newton 计算策略在半参数计算方面有参考价值，同时流行病学队列数据集可作为因果推断方法的潜在应用场景。
- **关键技术**: `penalized splines`, `distributed lag non-linear models`, `profile likelihood`, `Laplace approximate marginal likelihood`, `Newton-type optimization`, `generalized additive models`
- **为什么对您有用**: penalized spline 的 LAML 选择与 profile Newton 计算策略对您的统计计算兴趣有直接参考价值；加拿大全国空气污染-住院计数数据集可作为流行病学因果推断（如 IV 或 sensitivity analysis）的应用素材。

### 6. [10.1093/biomtc/ujaf125](https://doi.org/10.1093/biomtc/ujaf125) — A Bayesian semiparametric mixture model for clustering zero-inflated microbiome data
- **作者**: Suppapat Korsurat, Matthew D Koslovsky
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在微生物组零膨胀多变量成分计数数据设定下，本文目标是同时学习未知聚类数与进行聚类分配。提出一种贝叶斯半参数混合模型框架，利用非参数先验自动推断聚类数，并显式建模零膨胀与成分约束结构。模拟实验表明，相较于距离法与经典模型法，该方法在聚类准确性上表现更优，且正确处理零膨胀对推断至关重要。实证分析将其应用于肠道微生物组成与腹泻病关联的流行病学数据。对您而言，该文虽涉及半参数与流行病学，但核心为贝叶斯非参数聚类，与您关注的频率派效率界及因果推断范式差异较大，仅可作为流行病学零膨胀成分数据结构的参考。
- **关键技术**: `Bayesian semiparametric mixture`, `zero-inflated counts`, `compositional data`, `Dirichlet process prior`, `cluster allocation`
- **为什么对您有用**: 涉及半参数建模与流行病学应用（肠道微生物与腹泻病数据集），但核心为贝叶斯非参数聚类，与您关注的频率派半参数效率界、因果推断距离较远，主要价值在于了解流行病学零膨胀成分数据的结构特征。

### 7. [10.1093/biomtc/ujaf099](https://doi.org/10.1093/biomtc/ujaf099) — Negative binomial mixed effects location-scale models for intensive longitudinal count-type physical activity data provided by wearable devices
- **作者**: Qianheng Ma, Genevieve F Dunton, Donald Hedeker
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 针对可穿戴设备产生的密集纵向计数型体力活动（PA）数据，本文提出负二项混合效应位置-尺度模型（NBMLS），旨在刻画个体在均值与离散度上的异质性。模型允许受试者的均值（位置）与方差（尺度）均具有随机效应，从而区分活动规律（低离散）与久坐伴突发活动（高离散）的异质模式。针对 PA 数据中常见的零膨胀问题，进一步构建 hurdle/零膨胀版本，对 PA>0 的概率进行联合建模。估计方法基于边际似然与自适应高斯-埃尔米特求积，属于参数混合效应框架。实证结果表明该模型能有效捕捉高频计数数据的异质特征。对您而言，该文提供了流行病学高频计数数据的结构特征与建模思路，可作为纵向因果推断或动态处理效应在流行病学应用中的数据前置参考。
- **关键技术**: `negative binomial mixed effects model`, `location-scale model`, `zero-inflated model`, `hurdle model`, `intensive longitudinal data`
- **为什么对您有用**: 提供了流行病学中密集纵向计数数据（可穿戴设备）的建模框架，对您在纵向因果推断（primary）或流行病学应用（secondary）中处理类似高频零膨胀计数数据有参考价值。

## 其他  *(other, 9 篇)*

### 1. [10.1093/biomtc/ujaf043](https://doi.org/10.1093/biomtc/ujaf043) — Precision generalized phase I-II designs
- **作者**: Saijun Zhao, Peter F Thall, Ying Yuan, Juhee Lee, Pavlos Msaouel, Yong Zang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文提出了一类贝叶斯精准剂量优化设计（PGen I-II），在同时观察早期疗效、早期毒性和长期治疗失败时间的设定下，通过亚组（如预后水平、生物标志物）刻画患者异质性。方法假设失败时间服从分段指数分布，并引入亚组特异的剂量、响应与毒性效应；同时利用潜变量对具有相似剂量-结局分布的亚组进行自适应聚类，以在同类亚组间借力简化模型。该设计支持亚组层面的自适应决策，包括剔除不可接受剂量、随机化或基于长期随访确定最优剂量。模拟研究表明，PGen I-II 设计优于假设患者同质性或在各亚组独立开展试验的设计。对您而言，本文属于贝叶斯临床试验设计，与您关注的半参数/效率理论或因果推断关联较弱，但潜变量聚类借力的计算思路可作一般性参考。
- **关键技术**: `Bayesian adaptive design`, `piecewise exponential distribution`, `latent variable clustering`, `dose optimization`, `subgroup analysis`
- **为什么对您有用**: 本文属于贝叶斯临床试验设计，与您关注的因果推断、半参数效率或高维理论等核心方向关联较弱；仅潜变量自适应聚类借力的计算思路可作一般性参考。

### 2. [10.1093/biomtc/ujaf127](https://doi.org/10.1093/biomtc/ujaf127) — Spatially aware adjusted Rand index for evaluating spatial transcriptomics clustering
- **作者**: Yinqiao Yan, Xiangnan Feng, Xiangyu Luo
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 2/10 · novelty: `minor`
- **摘要**: 在空间转录组学(ST)聚类评估设定下，传统ARI指标完全忽略空间信息，本文目标是构建融合空间距离的聚类评价指标 spRI/spARI。核心机制是在比较两个划分时，对不一致的对象对赋予基于空间距离的权重（而非RI的零权重），从而偏好空间连贯性；spARI通过在特定零模型下调整期望为零来修正随机效应。文章推导了spRI和spARI的统计性质（如零模型下的期望），并在模拟与真实ST数据中验证了其相对ARI的优越性。该工作主要属于生物信息学中的评价指标构建，理论深度较浅，对您在因果推断或高维统计等核心方向的研究直接参考价值有限。
- **关键技术**: `adjusted Rand index`, `spatial distance weighting`, `null model expectation`, `spatial transcriptomics clustering`
- **为什么对您有用**: 本文属于聚类评价指标的局部改进，虽然涉及零模型下的期望计算，但理论深度与您关注的半参数效率/高维推断/U统计量等核心方向差距较大，仅作为应用统计中指标构造的参考。

### 3. [10.1093/biomtc/ujaf085](https://doi.org/10.1093/biomtc/ujaf085) — A positivity robust strategy to study effects of switching treatment
- **作者**: Matias Janvin, Pål C Ryalen, Aaron L Sarvet, Mats J Stensrud
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10
- **摘要**: {
  "topic": "causal_inference",
  "summary_zh": "在治疗切换（treatment switching）因果推断设定下，当 positivity 严重违反——即很少或没有个体在治疗组间切换——时，目标是量化切换治疗对后续复发事件的平均效应。作者提出新 estimand 刻画"切换效应"，并在部分识别（partial identification）框架下推导该 estimand 的非参数上下界。界的估计采用非参数估计器；同时定义动态切换策略的 value 与 regret 函数，在部分识别下给出三类最优策略：悲观（maximin value）、乐观（maximax value）、机会主义（minimax regret）。悲观策略保证至少不劣于标准护理，提供了实际可操作的保守决策规则。实证部分将方法应用于 SPRINT 收缩压试验数据。对您有用：该工作在因果推断中直接处理 positivity 违反下的部分识别与决策，与您关注的 causal inference（identification / sensitivity analysis）高度相关，minimax regret 思路可迁移至其他部分识别场景。",
  "key_techniques": [
    "partial identification bounds",
    "

### 4. [10.1093/biomtc/ujaf094](https://doi.org/10.1093/biomtc/ujaf094) — Improved prediction and flagging of extreme random effects for non-Gaussian outcomes using weighted methods
- **作者**: John Neuhaus, Charles McCulloch, Ross Boylan
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10
- **摘要**: {
  "topic": "stat_computing",
  "summary_zh": "在广义线性混合模型（GLMM）框架下，针对纵向/聚类数据中极端随机效应的预测与异常标记（flagging）问题，本文将此前仅适用于 Gaussian 结局的加权预测方法推广至二值、计数等非 Gaussian 结局。由于非 Gaussian 结局下预测随机效应及正确/错误标记概率无闭式表达，作者发展了"self-calibrated"调参理论——通过简单标记规则控制错误标记率（Type I error），并设计了计算加权预测量及其性能评估的创新数值算法。核心方法是对极端区域赋予更高权重的加权预测，相比传统 BLUP/EB 预测量，在极端值处大幅降低 MSE 并提高正确标记率，同时控制错误标记率。综合数值实验和哮喘儿童急诊再入院数据的应用验证了方法优势。对您而言，本文在非 Gaussian 混合模型下无闭式解时的数值算法设计策略可迁移至统计计算方向的工作，同时纵向聚类数据的设定与您因果推断中纵向数据的兴趣有交叉。",
  "key_techniques": ["weighted prediction of random effects", "self-calibrated algorithm", "GLMM non-Gaussian outcomes", "flagging extreme

### 5. [10.1093/biomtc/ujaf092](https://doi.org/10.1093/biomtc/ujaf092) — Using model-assisted calibration methods to improve efficiency of regression analyses using two-phase samples or pooled samples under complex survey designs
- **作者**: Lingxiao Wang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10
- **摘要**: ```json
{
  "topic": "efficiency_dml",
  "summary_zh": "在两阶段抽样（two-phase sampling）及复杂调查设计下，目标是提高仅于第二阶段子样本中观测变量的回归系数估计效率，关键假设为两阶段均为已知入样概率的随机抽样。本文提出基于回归模型得分函数（score function）的模型辅助校准（model-assisted calibration）方法：利用第一阶段样本对第二阶段变量的预测值构造校准辅助变量，将第二阶段样本权重校准至加权第一阶段样本，从而借力第一阶段全部观测信息提升效率。理论方面，证明了校准权重下估计的一致性，并给出了两阶段设计及嵌套"池化设计"（pooled design，部分协变量仅在特定调查轮次测量）下回归系数的方差估计量。模拟与 NHANES 实例表明，相比现有校准与插补方法，所提方法在效率与稳健性上均有优势。对您而言，该文将 score function 引入校准权重的思路与 semiparametric efficiency 中利用 influence function 提升效率的逻辑相通，且 NHANES 两阶段数据结构对流行病学因果推断中的 missing-at-random / selection bias 问题有直接迁移价值。",
  "key_techniques": [

### 6. [10.1093/biomtc/ujaf115](https://doi.org/10.1093/biomtc/ujaf115) — Bayesian inference for copy number intra-tumoral heterogeneity from single-cell RNA-sequencing data
- **作者**: PuXue Qiao, Chun Fung Kwok, Guoqi Qian, Davis J McCarthy
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文在单细胞 RNA 测序（scRNA-seq）数据下，目标是同时聚类细胞为亚肿瘤克隆并识别各克隆的拷贝数变异（CNA）profile，假设克隆数未知且无需先验知识。作者提出贝叶斯联合模型，将细胞聚类与克隆 CNA 检测统一在一个概率框架内，融合基因表达与胚系 SNP 两种信号，并通过 Gibbs 采样进行后验推断。方法以 R 包 Chloris 发布，在模拟和真实数据（转移性黑色素瘤、间变性甲状腺癌）上对比现有工具，聚类与 CNA 识别精度均有提升。该方法学 novelty 主要在于生物问题的联合建模，统计理论层面（收敛率、效率界、假设检验）无新贡献。对您而言，仅在统计计算（Gibbs 采样实现、R 包设计）方面有轻微参考价值，与核心兴趣方向重叠极低。
- **关键技术**: `Bayesian mixture model`, `Gibbs sampling`, `joint clustering and profile inference`, `single-cell RNA-seq CNA detection`, `germline SNP integration`
- **为什么对您有用**: 与您的主要兴趣（因果推断、RMT、半参数效率、高阶 U 统计量）几乎无交集；仅在统计计算（Gibbs 采样算法实现、R 包工程）方面有极轻微参考，不推荐深读。

### 7. [10.1093/biomtc/ujaf113](https://doi.org/10.1093/biomtc/ujaf113) — Semi-supervised linear regression: enhancing efficiency and robustness in high dimensions
- **作者**: Kai Chen, Yuqian Zhang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10
- **摘要**: {
  "topic": "efficiency_dml",
  "summary_zh": "在高维半监督设定下，本文研究线性回归系数的估计与推断，挑战了"无标签数据仅在模型误设时才改善线性参数估计"的传统观点。针对稠密情形，作者提出无需总体斜率稀疏假设的鲁棒半监督估计量，证明即使在真实模型为线性时，利用大规模无标签数据也能有效降低估计偏差，从而提升估计精度与推断鲁棒性。针对稀疏情形，进一步提出具有更高渐近效率的半监督估计方法，其核心依赖于偏差校正与有效得分函数的构造。理论结果表明，半监督信息在高维下能突破全监督方法的效率瓶颈。对您有用：本文直接推进了高维统计与效率理论的交叉，为高维 debiased ML 和半参数效率界的研究提供了半监督视角的新颖理论工具。",
  "key_techniques": [
    "semi-supervised learning",
    "high-dimensional debiased estimation",
    "bias reduction",
    "efficient score function",
    "robust inference",
    "sparse and dense regimes"
  ],
  "why_relevant": "直接推进了高维统计与效率理论的交叉，展示了无标签数据如何在无稀

### 8. [10.1093/biomtc/ujaf087](https://doi.org/10.1093/biomtc/ujaf087) — A flexible framework for <i>N</i>-mixture occupancy models: applications to breeding bird surveys
- **作者**: Huu-Dinh Huynh, J Andrew Royle, Wen-Han Hwang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10 · novelty: `minor`
- **摘要**: 在生态监测的不完全检测设定下，目标是估计物种丰度（abundance），传统 N-mixture 模型依赖严格的封闭假设（closure assumption），违反时导致有偏估计。本文提出基于 mixed Gamma-Poisson 模型的扩展框架，引入社区参数表示调查期间持续存在的个体比例，当该参数取 0 和 1 时分别退化为 zero-inflated occupancy 模型和标准 N-mixture 模型。估计采用参数混合模型的似然方法，通过模拟和两个真实鸟类调查数据集（北美繁殖鸟调查 5 物种、瑞士繁殖鸟调查 46 物种）验证了放松封闭假设后估计偏差的改善。该框架本质上是参数混合模型的特例整合，方法学 novelty 有限；对您而言，不完全检测下的潜变量建模思路与流行病学测量误差问题有概念相似性，但本文未涉及半参数效率或因果推断，直接收益较低。
- **关键技术**: `Gamma-Poisson mixture`, `N-mixture model`, `zero-inflated occupancy model`, `closure assumption relaxation`, `community parameter`
- **为什么对您有用**: 不完全检测/潜变量建模与流行病学测量误差问题有概念相似性，但本文为参数模型扩展，未触及半参数效率或因果推断，对您核心兴趣的直接收益有限。

### 9. [10.1093/biomtc/ujaf081](https://doi.org/10.1093/biomtc/ujaf081) — Inference on age-specific fertility in ecology and evolution. Learning from other disciplines and improving the state of the art
- **作者**: Fernando Colchero
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 0/10 · novelty: `survey`
- **摘要**: 本文针对生态与进化领域中年龄别生育率(age-specific fertility)的建模与推断问题，系统综述了自1940年代以来形式人口学、统计学和社会科学提出的两大类模型——多项式模型与基于概率密度函数的模型，并讨论它们对生育率不同阶段的表达能力。作者指出该领域长期依赖简单最小二乘推断，对生态数据而言不够充分，因此开发了R包BaFTA(Bayesian Fertility Trajectory Analysis)，采用贝叶斯方法实现推断与模型选择。将该方法应用于狮子和狒狒的公开聚合数据，并通过模拟研究验证其在个体水平数据上的表现，表明即使追踪的亲本数量较少也能实现合理的推断与模型选择。本文方法学新颖性有限，主要是跨学科综述加贝叶斯R包实现，对您的研究兴趣直接关联较弱。
- **关键技术**: `polynomial fertility models`, `probability density function models`, `Bayesian model selection`, `MCMC inference`, `aggregated vs individual-level data`
- **为什么对您有用**: 本文属于生态/进化领域的应用综述，与您的主要兴趣（因果推断、半参数效率理论、高维统计）和次要兴趣（天文、经济、流行病学）均无直接交集；仅R包开发部分与统计计算有微弱关联，但方法为标准贝叶斯MCMC，无可迁移的新算法或理论。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

