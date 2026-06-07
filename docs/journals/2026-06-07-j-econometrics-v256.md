# J. Econometrics — Vol 256  ·  2026-06-07

- 共 7 篇 · Journal of Econometrics

## 因果推断  *(causal_inference, 3 篇)*

### 1. [10.1016/j.jeconom.2026.106253](https://doi.org/10.1016/j.jeconom.2026.106253) · [arXiv](https://arxiv.org/abs/2007.10432) — Treatment effects with targeting instruments
- **作者**: Sokbae Lee, Bernard Salanié
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 256 · pp 106253
- 相关性 9/10 · novelty: `new_theory`
- **摘要**: 在多值处理与离散工具变量的因果推断设定下，本文研究“靶向”（targeting）概念——即特定工具变量针对特定处理水平——对复合遵从者组反事实均值与处理效应的识别作用。作者利用靶向假设结合单调性，给出了点识别与部分识别的条件；进一步引入正向选择假设（positive selection）以收紧识别域。方法上，这属于非参数 IV identification 理论的拓展，无需依赖强参数假设即可推导出局部平均处理效应的界。实证部分重访了 Head Start Impact Study，所得非参数界表明 Head Start 扩展效应的益处低于以往参数估计。对您有用：本文为多值处理 IV 的 identification 与 partial identification 提供了新框架，直接关联您 primary interest 中的 IV 与 identification theory。
- **关键技术**: `multivalued treatments`, `targeting instruments`, `partial identification`, `positive selection assumption`, `composite complier groups`, `local average treatment effect bounds`
- **为什么对您有用**: 直接关联 primary interest 中的 IV 与 identification theory，以及 secondary interest 中的 econ theory (applied causal work)。您 technical_arsenal 中 moderately_familiar 的 identification theory in causal inference 可直接用来审视其靶向假设与 partial identification 的逻辑；very_familiar 的 estimation theory in causal inference 可用于后续将此 bounds 转化为半参数有效估计量的拓展。Follow-up 粗判：立即可做——用现有的 identification 与 estimation 理论武器，即可尝试将本文的 partial identification bounds 推向半参数有效估计或 sensitivity analysis 框架。

### 2. [10.1016/j.jeconom.2026.106266](https://doi.org/10.1016/j.jeconom.2026.106266) — Estimation and inference in boundary discontinuity designs: Distance-based methods
- **作者**: Matias D. Cattaneo, Rocío Titiunik, Ruiqi (Rae) Yu
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 256 · pp 106266
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究边界断点设计（boundary discontinuity design）下的因果处理效应估计与推断，设定为二元位置评分（bivariate location score）形成的连续边界将单元分为处理与对照，目标 estimand 为边界平均处理效应曲线（BATEC）及其加权聚合（WBATE）与最大聚合（LBATE），涵盖 sharp 与 fuzzy 设计。核心方法为基于距离的局部多项式估计器，直接利用二元评分坐标；理论贡献包括 BATEC 的逐点与一致推断，以及 WBATE/LBATE 的估计与推断，关键工具为局部多项式回归与非参数一致收敛理论。实证用真实数据演示并提供通用软件包。对您可能有用：本文将空间断点设计的非参数估计与推断系统化，直接连接因果推断的 identification 与 semiparametric estimation 子方向。
- **关键技术**: `boundary discontinuity design`, `local polynomial regression`, `uniform inference`, `bivariate score`, `fuzzy RD`, `BATEC / WBATE / LBATE`
- **为什么对您有用**: 本文直接连接因果推断的 identification 与 semiparametric estimation 子方向（空间断点设计），一致推断部分涉及 nonparametric statistics 与 minimax rate 的技术 arsenal。用 very_familiar 的 nonparametric statistics 与 minimax bounds 武器可立即审视其一致收敛率是否紧；若想深入 fuzzy 设计的 semiparametric efficiency bound，需先在 moderately_familiar 的 semiparametric theory 上长肌肉。整体判断：立即可做——用现有武器即可检验其理论率与推断性质。

### 3. [10.1016/j.jeconom.2026.106254](https://doi.org/10.1016/j.jeconom.2026.106254) — Bounding treatment effects by pooling limited information across observations
- **作者**: Sokbae Lee, Martin Weidner
- **期刊/来源**: Journal of Econometrics
- **机构**: Columbia University · University of Oxford
- **分类**: vol 256 · pp 106254
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在 unconfoundedness 假设下，本文研究 ATT 的部分识别与估计，针对倾向得分重叠性（overlap）被破坏或协变量取值过多的困难情形。核心机制是提出“有限信息池化”（limited pooling）估计量：其被构造为样本函数的平均，且每个观测值的贡献仅依赖于有限个其他观测的处理状态。无池化对应 Manski bounds（稳健但宽），无限池化对应 IPW（窄但依赖强 overlap），本文探索两者之间的中间地带，实质上构造了阶数受限的 U-statistic 型估计量。作者为这些中间界提供了推断方法，并在 Monte Carlo 与实证中验证了其稳健性与信息量。对您可能有用：该估计量的“有限池化”结构直接对应 higher-order U-statistics 的阶数控制，您可以用 U-statistic projection 与 HOIF 理论分析其收敛性质与效率损失，并探索与 semiparametric efficiency bound 的距离。
- **关键技术**: `partial identification`, `limited information pooling`, `overlap violation robustness`, `U-statistic of restricted order`, `inference for bounds`, `inverse propensity score weighting`
- **为什么对您有用**: (1) 直接对应 causal inference 中 overlap violation / partial identification 设定，以及 higher-order U-statistics 的阶数与信息池化关系；(2) 可用 "theory of higher-order U-statistics" 与 "HOIF" 分析其有限池化估计量的投影与效率界，验证其稳健性是否以牺牲 semiparametric efficiency 为代价；(3) **立即可做**：用 very_familiar 的 "computation of higher-order U-statistics (treewidth / einsum)" 视角审视其估计量的计算复杂度，并用 moderately_familiar 的 HOIF 理论推导其 influence function。

## 非参数 / 半参数  *(nonparam_semipara, 2 篇)*

### 1. [10.1016/j.jeconom.2026.106264](https://doi.org/10.1016/j.jeconom.2026.106264) — A kernelization-based approach to nonparametric binary choice models
- **作者**: Guo Yan
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 256 · pp 106264
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在非参数二元选择模型设定下，estimand 为 weighted average partial derivative（WAPD），对系统函数和误差分布均不做参数假设。作者将 RKHS 视为特殊 sieve 空间，配合 spectral cut-off 正则化实现降维，使协变量维度中等时仍保持计算可扩展性——避免了传统 sieve（polynomial/power series）在 moderate d 下导致的高维优化瓶颈。建立了 estimator 的一致性和 WAPD plug-in estimator 的渐近正态性。模拟显示模型误设时优于 parametric 方法，正确设定时效率损失温和；实证用美国移民法庭 asylum 申请数据+天气污染变量，检验室外温度对法官裁决的影响。对您有用：RKHS sieve + spectral cut-off 降维策略直接连接 nonparametric theory 与 semiparametric efficiency 兴趣，且 judge decision + weather shock 的应用属于 econ_theory 的 applied causal work。
- **关键技术**: `RKHS sieve estimation`, `spectral cut-off regularization`, `weighted average partial derivative`, `nonparametric binary choice`, `asymptotic normality of plug-in`, `kernel method for dimension reduction`
- **为什么对您有用**: 本文连接 nonparametric theory（RKHS 作为 sieve）和 semiparametric efficiency（WAPD 的渐近正态性），实证场景（法官决策+外生天气冲击）属于 econ_theory 的 applied causal work。用 very_familiar 的 nonparametric statistics 和 minimax bounds 可验证其 spectral cut-off rate 是否 minimax optimal；用 moderately_familiar 的 semiparametric theory 可分析 WAPD estimator 是否达到 semiparametric efficiency bound 或可构造 HOIF 改进。中期可做：需先在 moderately_familiar 的 semiparametric theory 上确认其 influence function 构造，再判断能否用 HOIF 获得 higher-order correction。

### 2. [10.1016/j.jeconom.2026.106242](https://doi.org/10.1016/j.jeconom.2026.106242) · [arXiv](https://arxiv.org/abs/2405.18089) — Semi-nonparametric models of multidimensional matching: An optimal transport approach
- **作者**: Dongwoo Kim, Young Jun Lee
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 256 · pp 106242
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在可转移效用（transferable utility）的多维匹配模型中，目标是在放宽特征分布的联合正态假设下，识别并估计生产技术、均衡工资与匹配函数。利用最优传输（optimal transport）理论建立非参数识别性；基于此提出筛法（sieve）估计量，并证明其一致性、渐近正态性及半参数有效性。实证重访美国劳动力数据（1990-2010），发现认知能力偏向的技术进步幅度远超原参数模型结论，且对工资不平等演化的拟合更优。对您有用：本文将筛法半参数估计与最优传输结合应用于经济匹配模型，直接呼应您对 semiparametric efficiency 的兴趣，并提供了经济理论中的高质量实证数据集。
- **关键技术**: `sieve estimation`, `optimal transport theory`, `semiparametric efficiency bound`, `multidimensional matching model`, `transferable utility`
- **为什么对您有用**: 直接连接您 primary interest 中的 semiparametric & nonparametric theory（sieve estimator 的 CAN 与 efficiency）以及 secondary interest 中的 economic theory（多维匹配模型与工资数据）。您的 `very_familiar` (nonparametric statistics) 与 `moderately_familiar` (semiparametric theory / M-estimation) 完全可以用来审视其 sieve 估计量的渐近推导与效率界。**立即可做**：用 minimax bounds 或 M-estimation 理论评估其 sieve 空间选择对收敛率的影响，或探讨最优传输约束下的效率界是否紧。

## 经济理论 / 应用  *(econ_theory, 2 篇)*

### 1. [10.1016/j.jeconom.2026.106267](https://doi.org/10.1016/j.jeconom.2026.106267) — Estimation of characteristics-based quantile factor models
- **作者**: Liang Chen, Juan J. Dolado, Jesús Gonzalo, Haozi Pan
- **期刊/来源**: Journal of Econometrics
- **机构**: Peking University · Universidad Carlos III de Madrid · Centro de Estudios Monetarios y Financieros
- **分类**: vol 256 · pp 106267
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在特征驱动的分位数因子模型设定下，因子载荷是观测个体特征的未知函数，误差项满足条件分位数约束，目标是估计因子、载荷函数及因子个数。提出三阶段估计程序：第一阶段估计因子，第二阶段非参数估计载荷函数，第三阶段用一致准则选择因子个数。推导了估计因子与载荷函数的收敛速率及极限分布，并在一般条件下给出因子个数的一致选择准则。方法在误差重尾、时间维度不大、因子数超过特征数三种困难情形下仍有效。有限样本模拟与S&P500日收益率面板实证验证了理论结果。对您可能有用：该文的非参数载荷函数估计与收敛速率分析触及半参数理论，且因子模型+金融面板数据直接对接经济理论应用。
- **关键技术**: `characteristic-based quantile factor model`, `three-stage estimation procedure`, `nonparametric loading function estimation`, `convergence rate derivation`, `factor number selection criterion`, `conditional quantile restriction`
- **为什么对您有用**: 本文连接到 semiparametric theory（载荷函数为未知函数的半参数估计）和 econ_theory（因子模型 + S&P500 面板数据应用）。用 moderately_familiar 的 semiparametric theory 可以攻一个口子：当前论文未讨论该模型下的 semiparametric efficiency bound 和 efficient influence function，推导效率界是自然的 follow-up。中期可做：需先在 moderately_familiar 的 semiparametric theory 上长肌肉（特别是 quantile restriction 下的效率界推导），才能正式切入该模型的效率分析。

### 2. [10.1016/j.jeconom.2026.106265](https://doi.org/10.1016/j.jeconom.2026.106265) — Time domain estimation of non-fundamental ARMA models in the presence of heteroskedasticity of unknown form
- **作者**: Ignacio N. Lobato, Carlos Velasco
- **期刊/来源**: Journal of Econometrics
- **机构**: Instituto Tecnológico Autónomo de México · Universidad Carlos III de Madrid
- **分类**: vol 256 · pp 106265
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文在非高斯线性 ARMA 模型（允许非因果/非可逆，即 non-fundamental）设定下，研究时域估计问题，关键假设是创新为鞅差序列且可具有未知形式的条件异方差。作者不显式参数化波动过程，而是基于创新的二阶与三阶幂的可预测性构造最小距离目标函数，进而提出 efficient GMM 估计量。该估计量被证明一致且渐近正态，并在 29 个 OECD 国家通胀数据上广泛应用，发现大量 non-fundamentalness 证据。对您可能有用：该文将 GMM 与高阶矩条件结合处理异方差非基本 ARMA，与您在 higher-order U-statistics 及 semiparametric efficiency 方向的兴趣有方法论交叉。
- **关键技术**: `non-fundamental ARMA`, `efficient GMM`, `minimum distance estimation`, `martingale difference innovations`, `conditional heteroskedasticity of unknown form`, `higher-order moment conditions`
- **为什么对您有用**: 本文连接到您在 econ_theory 子方向的因果/结构模型估计兴趣，其 efficient GMM 与高阶矩条件的组合可被视为一种 semiparametric efficiency 追求（不参数化波动过程）。用您 very_familiar 中的 minimax bounds / high-dimensional asymptotics 可审视其渐近正态声称的紧致性；但核心 GMM/时间序列非基本模型工具不在武器库中，属于中期可做——需先在 moderately_familiar 的 M-estimation theory 上长肌肉以深入其目标函数性质。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

