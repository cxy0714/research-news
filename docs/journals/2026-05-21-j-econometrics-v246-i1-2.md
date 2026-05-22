# J. Econometrics — Vol 246  Issue 1-2  ·  2026-05-21

- 共 6 篇 · Journal of Econometrics

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.1016/j.jeconom.2024.105895](https://doi.org/10.1016/j.jeconom.2024.105895) — From LATE to ATE: A Bayesian approach
- **作者**: Isaac M. Opper
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 246 · issue 1-2 · pp 105895
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在工具变量（IV）设定下，研究从不完全依从RCT中估计的LATE外推至总体ATE的问题，核心关注边际处理效应（MTE）函数的部分识别。提出一种贝叶斯模型构建MTE函数的后验分布，即使在MTE不可识别的情况下，也能对ATE或always-takers效应等未识别因果参数给出后验分布。该方法突破了二元IV的限制，允许连续IV及额外外生变量的引入。在Oregon健康保险实验的应用发现，ATE推断的不确定性主要来自传统统计变异而非MTE的不可识别性。对您有用：直接关联您因果推断中IV与敏感性/部分识别的兴趣，提供贝叶斯视角量化不可识别参数不确定性的新方法，并包含经典经济学因果推断数据集的应用范例。
- **关键技术**: `Bayesian partial identification`, `marginal treatment effect (MTE)`, `instrumental variables`, `LATE to ATE extrapolation`, `posterior distribution of unidentifiable estimands`
- **为什么对您有用**: 直接关联您因果推断中IV与敏感性分析的兴趣，提供了一种将LATE外推至ATE的贝叶斯部分识别方法；同时作为经济学应用，包含经典的Oregon健康保险实验数据集，对经济理论中的因果推断应用有参考价值。

### 2. [10.1016/j.jeconom.2024.105902](https://doi.org/10.1016/j.jeconom.2024.105902) — Consistent causal inference for high-dimensional time series
- **作者**: Francesco Cordoni, Alessio Sancetta
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 246 · issue 1-2 · pp 105902
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究高维时间序列中的因果识别问题，设定为数据经单调变换后服从高斯向量自回归（VAR）过程，即依赖结构由高斯 Copula 刻画。方法无需估计或已知边际分布，将半参数推断转化为对稀疏相关矩阵的估计，利用惩罚回归一致识别动态参数。在稀疏性条件下，通过条件独立关系重构有向无环图（DAG）以确定变量间的条件因果方向。理论上证明了高维参数与因果图结构估计的一致性，实证应用于石油冲击与限价指令簿的宏观/微观因果分析。对您有用：该文将高维稀疏 VAR 与半参数 Copula 结合处理时间序列因果图识别，为 longitudinal causal inference 和高维半参数理论提供了可迁移的思路。
- **关键技术**: `Gaussian copula VAR`, `high-dimensional sparse VAR`, `directed acyclic graph`, `semiparametric identification`, `conditional independence testing`
- **为什么对您有用**: 直接连接到 primary interest 的 causal inference (longitudinal/time series) 和 high-dimensional statistics / semiparametric theory；同时应用部分契合 secondary interest 的 econ_theory。阅读收益在于提供了一种在半参数边际下利用高维稀疏结构进行时间序列因果图识别的新框架。

## 非参数 / 半参数  *(nonparam_semipara, 2 篇)*

### 1. [10.1016/j.jeconom.2024.105899](https://doi.org/10.1016/j.jeconom.2024.105899) — GLS under monotone heteroskedasticity
- **作者**: Yoichi Arai, Taisuke Otsu, Mengshan Xu
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 246 · issue 1-2 · pp 105899
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在异方差回归设定下，目标是在条件方差函数非参单调约束下实现有效 GLS 估计。本文利用保序回归估计条件方差函数，构建了可行 GLS 估计量。理论证明该估计量与已知真实条件方差的不可行 GLS 渐近等价，且仅需边界修剪调谐参数而免去了常规非参带宽选择。核心理论贡献在于拓展了保序回归的适用范围，证明含生成变量的保序估计可作为第一阶段代入半参目标，且不破坏 n^{-1/2}-CAN 性质与有效影响函数。模拟与实证（重访 Acemoglu & Restrepo 2017 老龄化与增长数据）验证了方法优势。对您有用：本文处理半参两阶段估计中第一阶段非参侵入式估计的渐近等价性，直接关联您关注的半参数理论与效率理论。
- **关键技术**: `isotonic regression`, `infeasible GLS`, `generated regressors`, `semiparametric plug-in`, `boundary trimming`, `asymptotic equivalence`
- **为什么对您有用**: 证明了含生成变量的保序回归作为第一阶段估计不破坏半参目标的渐近效率，直接关联您关注的半参数理论与效率理论（两阶段估计的侵入性偏差消除）；实证部分涉及经济增长因果推断数据，契合您的经济理论应用兴趣。

### 2. [10.1016/j.jeconom.2024.105894](https://doi.org/10.1016/j.jeconom.2024.105894) — Pseudo-variance quasi-maximum likelihood estimation of semi-parametric time series models
- **作者**: Mirko Armillotta, Paolo Gorgi
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 246 · issue 1-2 · pp 105894
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究一类半参数时间序列模型，其中条件期望通过参数函数建模，而条件分布不作参数假设，目标是在此设定下获得比传统 QML 更高效的估计量。核心方法是构造基于高斯拟似然的伪方差估计器（pseudo-variance QMLE），在伪方差中引入与条件期望参数相关的参数约束（restricted estimator），这些约束在支撑有界的观测驱动模型（如计数过程、双界时间序列）中自然出现。理论结果表明：无论伪方差是否正确设定，估计量均保持 n^{-1/2}-CAN 及渐近正态性；当约束成立时，restricted estimator 相比无约束 QMLE 可实现效率提升；此外导出了参数约束的有效性检验统计量，其渐近分布为标准 χ²。模拟与实证部分涵盖整数自回归过程（检验稀疏算子散度假设）及双界数据自回归（应用于已实现相关系数序列）。对您有用：该工作在半参数效率理论框架下展示了通过伪方差约束提升 QMLE 效率的机制，且约束检验可直接用于半参数模型的设定检验，与您在 semiparametric efficiency bounds 和 hypothesis testing 方向的兴趣直接相关。
- **关键技术**: `Gaussian quasi-likelihood`, `pseudo-variance specification`, `parameter restrictions in variance`, `n^{-1/2}-CAN asymptotics`, `Wald-type specification test`, `observation-driven models`
- **为什么对您有用**: 直接连接您 primary interest 中的 semiparametric efficiency theory（通过伪方差约束实现效率提升）和 hypothesis testing（参数约束的 χ² 检验），同时实证应用涉及经济时间序列数据，对 secondary interest 的 econ_theory 也有参考价值。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1016/j.jeconom.2024.105898](https://doi.org/10.1016/j.jeconom.2024.105898) — Validating approximate slope homogeneity in large panels
- **作者**: Tim Kutta, Holger Dette
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 246 · issue 1-2 · pp 105898
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在大截面面板线性模型中，传统精确斜率同质性检验对微小异质性过于敏感，本文提出近似斜率同质性（允许参数偏差小于某阈值）的检验方法。作者构造了一个渐近枢轴（asymptotically pivotal）的检验统计量，无需对误差项的截面与时间相依性做严格限制。在 $N, T \to \infty$ 的渐近框架下，证明了该检验具有渐近水平 $\alpha$，且对局部备择假设类具有一致相合性。相比传统检验，该方法避免了因微小异质性而拒绝池化（pooling）的问题，提升了面板估计的稳定性。对您有用：该文将'近似零假设'引入面板模型，为假设检验方向提供了容忍微小偏差的新思路，且面板设定直接契合经济理论中的因果推断应用。
- **关键技术**: `approximate null hypothesis`, `asymptotically pivotal test`, `uniform consistency against local alternatives`, `panel data slope homogeneity`, `intersectional and temporal dependence`
- **为什么对您有用**: 直接契合您在数学统计（假设检验）和经济理论（面板模型、因果推断）的兴趣；“近似零假设”的检验思路可迁移至其他容忍微小模型偏差的半参数/非参数检验场景。

### 2. [10.1016/j.jeconom.2024.105900](https://doi.org/10.1016/j.jeconom.2024.105900) — Variable selection in high dimensional linear regressions with parameter instability
- **作者**: Alexander Chudik, M. Hashem Pesaran, Mahrad Sharifvaghefi
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 246 · issue 1-2 · pp 105900
- 相关性 0/10 · novelty: `weaker_assumption`
- **摘要**: 本文研究高维线性回归在参数不稳定（如结构突变）设定下的变量选择问题，区分了信号、伪信号与噪声变量，目标是在参数不稳定下实现一致选择。核心方法为 OCMT（One Covariate at a Time Multiple Testing），通过逐个协变量进行多重检验来筛选变量。理论证明，在参数不稳定下 OCMT 仍能渐近选出包含所有信号且无噪声变量的逼近模型。此外，选择后回归的样本内拟合具有 oracle 性质，且理论支持在筛选阶段使用未加权观测、仅在预测阶段降权的两步策略。蒙特卡洛与实证表明，该策略的预测均方误差优于 Lasso、Adaptive Lasso 和 Boosting。对您可能有用：该文将多重检验引入高维变量选择并放松了参数稳定假设，为高维统计与假设检验的交叉提供了不同于惩罚回归的视角。
- **关键技术**: `OCMT (One Covariate at a Time Multiple Testing)`, `parameter instability`, `oracle property`, `post-selection regression`, `multiple testing`
- **为什么对您有用**: 该文将多重检验方法应用于高维变量选择，直接关联您的高维统计与假设检验主兴趣；同时放松了参数稳定假设，对计量经济学中的高维预测与因果推断前步筛选有实际参考价值。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

