# Scand. J. Stat. — Vol 51  Issue 3  ·  2026-05-21

- 共 17 篇 · Scandinavian Journal of Statistics

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1111/sjos.12706](https://doi.org/10.1111/sjos.12706) — Estimation of treatment effect among treatment responders with a time‐to‐event endpoint
- **作者**: Andreas Nordland, Torben Martinussen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 1161-1180
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在主分层（principal stratification）框架下，本文研究有生物标志物定义的“处理响应者”群体的因果效应，设定为生存结局且允许右删失，识别条件假设非响应者无处理效应（排他性约束）。作者推导了该主分层因果参数的 efficient influence function，并据此构建了 doubly robust 且半参数有效的估计量。该方法通过影响函数实现了对生存数据右删失及干扰参数的鲁棒性，避免了参数模型误设的风险。模拟研究验证了估计量的有限样本表现，并应用于 Leader 试验评估利拉鲁肽对心血管事件的影响。对您有用：该文展示了如何在主分层排他性约束下结合 EIF 构建生存数据的 DR 估计量，直接契合您在因果推断与效率理论方面的兴趣，且提供了流行病学试验的应用范例。
- **关键技术**: `principal stratification`, `efficient influence function`, `doubly robust estimation`, `survival analysis`, `exclusion restriction`
- **为什么对您有用**: 直接契合您在因果推断（主分层与排他性约束）和效率理论（EIF与DR估计量）方面的核心兴趣，同时提供了流行病学临床试验（利拉鲁肽与心血管事件）的实证分析范例。

## 非参数 / 半参数  *(nonparam_semipara, 5 篇)*

### 1. [10.1111/sjos.12709](https://doi.org/10.1111/sjos.12709) — Efficient drift parameter estimation for ergodic solutions of backward SDEs
- **作者**: Teppei Ogihara, Mitja Stadje
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 1181-1205
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 本文研究连续时间倒向 SDE 的漂移参数在离散观测下的估计问题，estimand 为漂移参数 θ，设定为遍历半参数扩散与 BSDE 模型，关键假设是随机积分部分不可观测且非参数。核心方法是 quasi-maximum likelihood estimation (QMLE)，在随机被积函数（nuisance）未知且非参数的条件下，通过构造近似对数似然来估计漂移参数。理论结果包括参数估计的相合性与渐近正态性，证明中需处理非参数 nuisance 对似然函数的影响以及离散观测与连续时间模型之间的逼近误差。模拟实验验证了收敛性质。对您而言，该文展示了半参数模型中非参数 nuisance 下的参数效率推断思路，与您关注的 semiparametric efficiency theory 直接相关，但技术路线偏随机分析，可选择性关注其 nuisance 处理策略是否可迁移至因果推断中的半参数设定。
- **关键技术**: `quasi-maximum likelihood estimation`, `backward SDE`, `ergodic diffusion`, `semiparametric nuisance`, `asymptotic normality`, `discrete-time observation of continuous-time model`
- **为什么对您有用**: 与您 primary interest 中的 semiparametric theory 和 efficiency theory 相关——本文在非参数 nuisance（不可观测随机被积函数）下推导参数的渐近有效估计，属于半参数效率推断问题，但技术路线偏随机分析而非因果/debiased ML 路线，可选择性浏览。

### 2. [10.1111/sjos.12717](https://doi.org/10.1111/sjos.12717) — Empirical likelihood M‐estimation for the varying‐coefficient model with functional response
- **作者**: Xingcai Zhou, Dehan Kong, Matthew Stephen Pietrosanu, Linglong Kong, Rohana J. Karunamuni
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 1357-1387
- 相关性 6/10 · novelty: `new_theory`
- **摘要**: 本文研究函数响应变系数模型，在函数数据存在观测内依赖的设定下，目标是函数系数的稳健估计与推断。提出基于广义经验似然的 M-estimator，构建了函数系数的统计推断程序、同时置信域以及全局一般线性假设检验。理论上证明了其对数似然比过程的弱收敛性，并建立了非参数版本的 Wilks 定理，保证了似然比统计量的渐近 χ² 性质。模拟显示所提置信集覆盖概率接近名义水平，神经影像应用表明 MMSE 和 APOE 基因与各向异性分数显著关联。对您有用：非参数 Wilks 定理与同时置信域构建直接关联您对 hypothesis testing 与 semiparametric theory 的兴趣，其神经影像应用（APOE 基因与认知评分）也具有流行病学数据分析的参考价值。
- **关键技术**: `generalized empirical likelihood`, `varying-coefficient model`, `M-estimation`, `nonparametric Wilks theorem`, `simultaneous confidence regions`, `functional data analysis`
- **为什么对您有用**: 非参数 Wilks 定理与全局线性假设检验直接契合您在 hypothesis testing 和 semiparametric theory 方向的兴趣；广义经验似然 M-估计为复杂依赖结构下的推断提供了理论工具，其神经影像应用（APOE 基因与认知评分）也具有流行病学数据集的参考价值。

### 3. [10.1111/sjos.12700](https://doi.org/10.1111/sjos.12700) — Confidence bands for survival curves from outcome‐dependent stratified samples
- **作者**: Takumi Saegusa, Peter Nandori
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 1086-1102
- 相关性 6/10 · novelty: `new_theory`
- **摘要**: 在 outcome-dependent stratified sampling (ODSS) 设计下，目标是构建生存曲线的 confidence band；关键假设是 stratification 与 without-replacement sampling 导致的样本依赖结构。现有文献多用 Bernoulli sampling 近似 ODSS，但会高估方差；即使在此近似下，IPW Kaplan-Meier 估计量的极限分布为一般 Gauss 过程，其 supremum 分位数无解析解。本文对 weighted Kaplan-Meier 估计量给出了严格考虑样本依赖性的渐近理论，推导出极限过程的精确协方差结构。提出 hybrid method：对极限过程的一部分用参数模拟、另一部分用 bootstrap，从而计算具有渐近正确覆盖概率的 confidence band，避免了纯解析或纯 bootstrap 的困难。模拟研究表明所提 band 在有限样本下覆盖性质良好且优于 Bernoulli 近似；Wilms tumor 数据展示了应用。对您有用：ODSS 下严格处理依赖结构的渐近理论对 semiparametric efficiency 理论有参考价值，hybrid simulation-bootstrap 方法对统计计算中处理复杂极限分布具有可迁移性，Wilms tumor 案例对流行病学应用有数据集价值。
- **关键技术**: `inverse probability weighted Kaplan-Meier`, `outcome-dependent stratified sampling`, `Gaussian process supremum`, `hybrid simulation-bootstrap`, `weak convergence under dependent sampling`
- **为什么对您有用**: 严格处理 ODSS 依赖结构的渐近理论对您关注的 semiparametric efficiency 理论有直接参考价值；hybrid simulation-bootstrap 方法可迁移至其他复杂极限分布推断场景（统计计算方向）；Wilms tumor 案例对流行病学因果/生存分析应用有数据集价值。

### 4. [10.1111/sjos.12713](https://doi.org/10.1111/sjos.12713) — A two‐step estimation procedure for semiparametric mixture cure models
- **作者**: Eni Musta, Valentin Patilea, Ingrid Van Keilegom
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 987-1011
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在半参数混合治愈模型（parametric incidence + semiparametric latency）框架下，目标是估计治愈概率，克服潜变量导致的 EM-MLE 在有限样本下的缺陷。提出两步估计法：首先构造治愈概率的非参数预平滑（presmoothing）估计量，随后将其投影至目标参数空间（如 logistic 族）。理论上推导了该投影估计量的渐近性质，避免了 EM 算法的迭代不稳定问题。在 logistic-Cox 模型的模拟中，新方法在中小样本下显著优于 MLE，并应用于两个黑色素瘤数据集。对您有用：该文将“非参数预平滑+参数投影”的经典半参数技巧拓展至带潜变量的生存设定，其理论推导对您在半参数理论方面的研究有参考价值，且附带流行病学数据集。
- **关键技术**: `mixture cure model`, `presmoothing`, `nonparametric projection`, `semiparametric survival model`, `EM algorithm`
- **为什么对您有用**: 将非参数预平滑与参数投影的半参数技巧应用于带潜变量的生存模型，对您在半参数理论方面的兴趣有直接参考价值；同时包含黑色素瘤流行病学数据集，契合您的流行病学应用兴趣。

### 5. [10.1111/sjos.12702](https://doi.org/10.1111/sjos.12702) — Nonparametric plug‐in classifier for multiclass classification of S.D.E. paths
- **作者**: Christophe Denis, Charlotte Dion‐Blanc, Eddy Ella‐Mintsa, Viet Chi Tran
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 1103-1160
- 相关性 4/10 · novelty: `new_theory`
- **摘要**: 在多类分类问题中，特征为时间齐次扩散过程（SDE）的样本路径，各类别由漂移函数区分而扩散系数未知且各类共享。作者提出基于漂移和扩散函数非参数估计的 plug-in 分类器，在温和正则条件下证明分类程序的一致性，并在不同假设集下给出收敛速率。核心技术涉及扩散系数与漂移函数的非参数核型估计、基于估计密度的 Bayes 规则 plug-in 实现，以及分类超额风险（excess risk）的收敛速率分析。数值实验验证了理论结论。对您而言，该文是非参数理论在连续时间随机过程分类中的直接应用，与您关注的非参数收敛速率分析方向相关，但 SDE 路径设定较为专门，可借鉴其 plug-in 分类器风险分解与速率推导思路。
- **关键技术**: `nonparametric drift estimation`, `plug-in Bayes classifier`, `diffusion coefficient kernel estimation`, `excess risk convergence rate`, `time-homogeneous SDE path classification`
- **为什么对您有用**: 直接关联您 primary interest 中的非参数理论方向——漂移/扩散函数的非参数估计与分类超额风险的收敛速率分析是核心贡献；SDE 路径设定虽专门，但 plug-in 分类器的风险分解与速率推导框架可迁移至其他非参数决策问题。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1111/sjos.12716](https://doi.org/10.1111/sjos.12716) — Semiparametric efficient estimation in high‐dimensional partial linear regression models
- **作者**: Xinyu Fu, Mian Huang, Weixin Yao
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 1259-1287
- 相关性 10/10 · novelty: `new_theory`
- **摘要**: 在高维部分线性回归模型下，针对未知误差分布导致传统最小二乘估计效率损失的问题，本文目标是参数分量的半参数有效估计。提出一种基于惩罚估计的新方法，在超高频维设定下结合半参数有效理论构造估计量。该方法对参数分量产生稀疏估计，并具有 oracle 变量选择性质；在非高斯误差下达到半参数有效界（与已知误差分布的 oracle MLE 同效），在高斯误差下退化为与最小二乘同效。理论证明了该估计的 oracle 性质与半参数有效性，模拟与实证支持了非高斯情形下的效率提升。对您有用：直接推进了您关注的“半参数有效界”与“高维统计”交叉方向，展示了在部分线性模型中如何通过惩罚估计而非典型 cross-fitting 路径达到 oracle 效率。
- **关键技术**: `semiparametric efficiency bound`, `partial linear regression`, `penalized estimation`, `oracle variable selection`, `high-dimensional sparse model`
- **为什么对您有用**: 直接推进了您关注的“半参数有效界”与“高维统计”交叉方向，展示了在部分线性模型中如何通过惩罚估计路径达到 oracle 效率，对高维半参数模型的效率理论推导有直接参考价值。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1111/sjos.12710](https://doi.org/10.1111/sjos.12710) — Statistical inference for generative adversarial networks and other minimax problems
- **作者**: Mika Meitz
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 1323-1356
- 相关性 6/10 · novelty: `new_theory`
- **摘要**: 本文在非凸非凹极小极大设定下研究GAN等模型的统计推断，目标是对具有多重解的总体极小极大解集进行估计与置信域构造。作者首先证明样本GAN解集是总体解集的Hausdorff一致估计量，突破了传统点估计唯一性假设。针对解集的置信域推断，提出一种计算密集型程序（基于子抽样），并证明其具有目标覆盖概率。该理论框架不依赖凸凹性，适用于一般的多重解极小极大问题。对您有用之处在于：其针对非正则、集合值参数的推断理论，为您在数学统计（假设检验/置信集）及半参数理论中处理类似非标准推断问题提供了直接的理论工具与思路借鉴。
- **关键技术**: `minimax estimation`, `Hausdorff consistency`, `set-valued inference`, `confidence sets for multiple solutions`, `nonconvex-nonconcave optimization`
- **为什么对您有用**: 本文核心是多重解极小极大问题的置信域构造，直接对应您在数学统计与假设检验方向的兴趣；其处理非正则、集合值参数推断的理论框架，对半参数/非参数理论中类似非标准问题的推断具有方法迁移价值。

### 2. [10.1111/sjos.12708](https://doi.org/10.1111/sjos.12708) — Asymptotic inference of the ARMA model with time‐functional variance noises
- **作者**: Bibi Cai, Enwen Zhu, Shiqing Ling
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 1230-1258
- 相关性 4/10 · novelty: `new_theory`
- **摘要**: 本文研究带时间函数方差（TFV）噪声的 ARMA 模型（ARMA-TFV），目标是在过程非平稳的设定下建立最小二乘估计量（LSE）的渐近理论并进行假设检验。作者证明了 LSE 的相合性与渐近正态性，并基于变量选择和模型检验理论构建了 Wald 检验与 portmanteau 检验。由于噪声方差具有时间函数形式（可视为无限维干扰参数），过程非平稳，传统平稳时间序列技术不再适用，因此证明技术是非标准的。模拟与实际数据验证了方法在有限样本下的表现。对您有用：本文处理非平稳时间序列中无限维方差干扰下的渐近推断与检验，其非标准证明技术与您在数学统计（假设检验）及半/非参数理论方面的兴趣直接相关。
- **关键技术**: `ARMA with time-functional variance`, `least squares estimator (LSE)`, `asymptotic normality under non-stationarity`, `Wald test`, `portmanteau test`
- **为什么对您有用**: 本文聚焦非平稳时间序列的渐近推断与假设检验，处理了无限维方差函数作为干扰参数的情形，与您在数学统计（假设检验）和半/非参数理论方面的兴趣直接契合，其非标准证明思路可提供借鉴。

### 3. [10.1111/sjos.12744](https://doi.org/10.1111/sjos.12744) — Testing for time‐varying nonlinear dependence structures: Regime‐switching and local Gaussian correlation
- **作者**: Kristian Gundersen, Timothée Bacri, Jan Bulla, Sondre Hølleland, Antonello Maruotti, Bård Støve
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 1012-1060
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究一对随机变量间的非线性和时变依赖结构，在机制切换模型框架下，利用局部高斯相关性（LGC）检验不同机制下的依赖结构是否相同。提出了一种基于 LGC 的 bootstrap 检验方法，LGC 作为半参数方法避免了依赖结构的参数化设定（如 copula 模型）。通过 Monte Carlo 模拟评估了该检验的水平与功效性质，表明其具有良好的有限样本表现。实证分析应用于美英股市及美股与国债市场，揭示了机制间依赖结构的异质性。对您可能有用：该文将半参数局部相关性与假设检验结合，为非线性依赖结构的检验提供了无需 copula 设定的替代方案，直接关联您对假设检验与半参数理论的兴趣。
- **关键技术**: `local Gaussian correlation`, `regime-switching model`, `bootstrap hypothesis testing`, `semi-parametric dependence`, `Monte Carlo simulation`
- **为什么对您有用**: 论文提出的基于半参数 LGC 的 bootstrap 检验方法，直接关联您对假设检验与半参数理论的兴趣；同时金融市场的实证应用也契合您对经济理论中数据集与应用方法的关注。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1111/sjos.12705](https://doi.org/10.1111/sjos.12705) — Log‐density gradient covariance and automatic metric tensors for Riemann manifold Monte Carlo methods
- **作者**: Tore Selland Kleppe
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 1206-1229
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在 Riemann 流形 Monte Carlo 框架下，针对非线性贝叶斯分层模型的度量张量构造问题，提出基于对数密度梯度协方差 (LGC) 矩阵的新度量张量。LGC 推广了 Fisher 信息矩阵，通过度量随机变量及其参数的联合信息含量与依赖结构，使得正定度量张量不仅可由观测似然构造（现有做法），还可从任意复杂的非线性先验/潜变量条件分布构造，前提是各条件分布的 LGC 可求。该方法高度自动化、可利用模型稀疏性，并与 Riemann 流形变体的数值广义随机化 Hamiltonian Monte Carlo 结合，在贝叶斯分层模型的困难目标分布上表现优异。对您统计计算方向（数值方法与算法）有直接参考价值，LGC 推广 Fisher 信息的思路也可能对效率理论中信息几何视角的思考有启发。
- **关键技术**: `Riemann manifold Monte Carlo`, `log-density gradient covariance`, `Fisher information matrix`, `metric tensor construction`, `generalized randomized Hamiltonian Monte Carlo`, `Bayesian hierarchical models`
- **为什么对您有用**: 直接属于统计计算（数值方法与算法）方向，为分层模型的 RMMC 提供自动化度量张量方案；LGC 对 Fisher 信息的推广视角也可能对您在效率理论/半参数效率界中的信息几何理解提供新思路。

### 2. [10.1111/sjos.12720](https://doi.org/10.1111/sjos.12720) — Cox processes driven by transformed Gaussian processes on linear networks—A review and new contributions
- **作者**: Jesper Møller, Jakob G. Rasmussen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 1288-1322
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在任意线性网络上，本文研究由各向同性高斯过程经变换驱动的Cox过程，旨在填补线性网络点过程模型的空白。引入对数高斯、中断（interrupted）和永久（permanental）三类Cox过程，通过变换保证随机强度函数具有各向同性对相关函数。首次为这些参数族模型提出统计推断程序，并构造了线性网络上高斯过程的新模拟算法。详细讨论了测地距离与电阻距离在构建各向同性Cox过程中的适用性与选择依据。本文属于空间点过程领域，其高斯过程模拟算法设计对您的统计计算兴趣有微弱参考价值，但与因果推断、高维或效率理论的核心方向距离较远。
- **关键技术**: `Cox process on linear networks`, `isotropic Gaussian process transformation`, `isotropic pair correlation function`, `geodesic metric`, `resistance metric`, `simulation algorithm`
- **为什么对您有用**: 文中构造的高斯过程模拟算法对您的统计计算（数值方法与算法）兴趣有一定参考价值，但整体属于空间点过程领域，与您核心的因果推断、高维RMT及效率理论重叠度很低。

## 其他  *(other, 5 篇)*

### 1. [10.1111/sjos.12737](https://doi.org/10.1111/sjos.12737) — Nonparametric estimation of densities on the hypersphere using a parametric guide
- **作者**: María Alonso‐Pena, Gerda Claeskens, Irène Gijbels
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 956-986
- 相关性 5/10
- **摘要**: {
  "topic": "nonparam_semipara",
  "summary_zh": "本文研究超球面上的核密度估计（KDE），引入参数引导分布（parametric guide）来修正非参数估计的偏差。核心设定是在紧支撑的超球面上，以 von Mises-Fisher 密度作为引导分布，当引导模型接近真实密度时偏差显著降低而方差不变；即使引导模型错误，估计表现也不差于经典 KDE——这一"安全网"性质依赖于超球面的紧支撑性，与实值数据情形形成对比。方法的关键是利用参数引导对核权重进行重标定，理论分析给出偏差与方差的渐近展开。同时提供了光滑参数的数据驱动选择方法。模拟与真实数据（方向统计）验证了有限样本表现。对您而言，这是非参数理论中一个有趣的"参数辅助非参数"策略，紧支撑带来的安全网性质值得注意，但与您关注的效率界、高维或因果推断方向距离较远。",
  "key_techniques": [
    "hyperspherical kernel density estimation",
    "von Mises-Fisher distribution",
    "parametric guide bias correction",
    "asymptotic bias-variance expansion",
    "data-driven bandwi

### 2. [10.1111/sjos.12712](https://doi.org/10.1111/sjos.12712) — Martingale posterior distributions for cumulative hazard functions
- **作者**: Stephen G. Walker
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 936-955
- 相关性 5/10
- **摘要**: {
  "topic": "nonparam_semipara",
  "summary_zh": "本文研究累积危险函数（cumulative hazard function）的非参数贝叶斯建模与不确定性量化，estimand 为随机累积危险函数的后验分布。基础先验为 beta process，经典频率估计为 Nelson–Aalen 估计量；作者构造一列估计量使其构成鞅（martingale），从而从鞅后验（martingale posterior）中获得随机累积危险函数的样本路径。文中建立了该鞅后验与 beta process 之间的理论联系，并通过数值例子展示不确定性量化效果。该方法无需指定完整似然，仅依赖鞅结构即可构造后验，为非参数生存分析提供了一种新的推断框架。对您而言，鞅后验作为连接贝叶斯非参数与频率推断的桥梁，与您关注的半参数/非参数理论及效率推断有方法论上的交叉参考价值。",
  "key_techniques": [
    "martingale posterior distribution",
    "beta process prior",
    "Nelson-Aalen estimator",
    "cumulative hazard function",
    "nonparametric Bayesian inference",

### 3. [10.1111/sjos.12699](https://doi.org/10.1111/sjos.12699) — G‐optimal grid designs for kriging models
- **作者**: Subhadra Dasgupta, Siuli Mukhopadhyay, Jonathan Keith
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 1061-1085
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究二维输入与可分指数协方差结构下 Kriging 模型的 G-最优网格设计，目标为最小化超均方预测误差 (SMSPE)。作者提出了二维网格设计的“均匀性”概念，并证明在前瞻性设计场景下，等距网格即为 G-最优设计。针对回顾性设计（在已有设计上增删点），开发了最小化 SMSPE 的确定性算法，发现更均匀分布的设计在 G-最优准则下表现最佳。上述理论结果在频率学派和贝叶斯框架下均成立，并在时空河流水质监测实验中进行了演示。该文属于空间实验设计，与您核心的因果推断或高维效率理论关联较弱，仅确定性优化算法对统计计算兴趣有微弱参考。
- **关键技术**: `G-optimal design`, `kriging models`, `separable exponential covariance`, `supremum of mean squared prediction error`, `retrospective design algorithm`
- **为什么对您有用**: 属于空间统计与实验设计，与您核心的因果推断/高维/半参数效率理论关联较弱，仅确定性优化算法对统计计算兴趣有微弱参考。

### 4. [10.1111/sjos.12732](https://doi.org/10.1111/sjos.12732) — A conversation with Nils Lid Hjort
- **作者**: Ørnulf Borgan, Ingrid K. Glad
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 914-935
- 相关性 1/10
- **摘要**: {
  "topic": "survey",
  "summary_zh": "本文是对挪威统计学家 Nils Lid Hjort 的访谈记录，涵盖其四十余年在生存分析、Bayesian nonparametrics、empirical likelihood、密度估计、focused inference、模型选择及 confidence distributions 等领域的贡献与思想脉络。对话强调 Hjort 如何以好奇心和深刻理解在不同统计子领域间建立"意外连接"，并鼓励统计社区关注跨领域的非预期关联。文中涉及 confidence distribution 与 fiducial inference 的讨论、focused inference（基于特定 estimand 的模型选择而非全局准则）的理念，以及 Bayesian nonparametrics 与 frequentist 方法的交汇。作为访谈类文章，无新理论或方法贡献，但对理解 Hjort 多条研究线索（尤其是 confidence distributions 与 focused inference）的思想源头有参考价值。对您而言，confidence distributions 与假设检验/效率理论的联系、以及 focused inference 对 semiparametric efficiency 思路的可能启发

### 5. [10.1111/sjos.12741](https://doi.org/10.1111/sjos.12741) — Commentary on “Pitfalls of amateur regression: The Dutch New Herring controversies”
- **作者**: Jan C. Van Ours, Ben Vollaard
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 1388-1389
- 相关性 0/10


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

