# J. Econometrics — Vol 244  Issue 2  ·  2026-05-21

- 共 6 篇 · Journal of Econometrics

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1016/j.jeconom.2024.105702](https://doi.org/10.1016/j.jeconom.2024.105702) — State-dependent local projections
- **作者**: Sílvia Gonçalves, Ana María Herrera, Lutz Kilian, Elena Pesavento
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 2 · pp 105702
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在状态依赖的宏观计量模型中，研究局部投影（LP）估计量能否渐近恢复结构冲击对宏观经济总体的脉冲响应，关键假设在于经济状态的确定方式与冲击大小。当状态变量外生时，LP估计量无论冲击大小均可一致恢复总体响应。但当状态依赖于宏观经济冲击（即内生状态）时，LP仅能恢复对无穷小冲击的条件响应，无法识别较大冲击的响应。理论分析揭示了此时LP估计量收敛于非目标条件期望，产生本质性识别偏误。模拟显示脉冲响应估计偏误可达82%，财政乘子偏误达40%。对您有用：该文揭示了条件变量受处理影响时的识别陷阱，与因果推断中条件调整/碰撞偏误的理论逻辑高度一致，为状态依赖下的因果识别提供了渐近分析参考。
- **关键技术**: `local projections`, `impulse response function`, `state-dependent models`, `asymptotic identification`, `endogenous conditioning`
- **为什么对您有用**: 该文深入剖析了状态（条件变量）内生时的识别偏误，与您关注的因果推断中条件调整和识别理论直接相关；同时作为宏观计量的前沿应用因果工作，对经济理论（次要兴趣）中的结构冲击估计有重要启示。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1016/j.jeconom.2023.105521](https://doi.org/10.1016/j.jeconom.2023.105521) — Target PCA: Transfer learning large dimensional panel data
- **作者**: Junting Duan, Markus Pelger, Ruoxuan Xiong
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 2 · pp 105521
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究高维面板数据在存在大量缺失观测下的潜因子模型估计问题，通过引入辅助面板数据提出 target-PCA 估计量。核心机制是利用辅助数据的因子结构信息增强目标数据中弱因子的信号，突破传统 PCA 在弱因子（特征值发散不足）下无法识别的瓶颈。作者在近似因子模型与一般缺失模式下推导了渐近推断理论，证明该估计量具有更高效率并能一致估计弱因子。技术工具涉及高维 PCA 的特征分析、随机矩阵理论中谱分离条件的放松及矩阵补全。实证部分在混频宏观经济面板数据填补中展示了显著优于基准方法的表现。对您有用：本文将高维 RMT 的弱因子推断与迁移学习结合，提供了更锐利的效率结果，且混频宏观数据集对经济理论应用有直接价值。
- **关键技术**: `latent factor model`, `high-dimensional PCA`, `transfer learning`, `weak factor identification`, `random matrix theory`, `mixed-frequency data imputation`
- **为什么对您有用**: 直接推进高维统计与 RMT 在弱因子设定下的理论边界（放松传统 PCA 的谱分离条件），同时提供宏观经济面板数据实证，契合您在 high-dimensional statistics 与 economic theory 的双重兴趣。

## 经济理论 / 应用  *(econ_theory, 4 篇)*

### 1. [10.1016/j.jeconom.2024.105871](https://doi.org/10.1016/j.jeconom.2024.105871) — Estimation of continuous-time linear DSGE models from discrete-time measurements
- **作者**: Bent Jesper Christensen, Luca Neri, Juan Carlos Parra-Alvarez
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 2 · pp 105871
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在连续时间线性 DSGE 模型设定下，目标是基于离散时间观测数据估计结构参数，假设系统服从线性随机微分方程。核心机制是通过矩阵指数与 Jordan 标准形将连续时间参数精确映射为离散时间状态空间表示，避免了 Euler 离散化带来的误差。估计采用基于 Kalman 滤波的极大似然推断，涉及连续代数 Riccati 方程的数值求解与非线性参数约束优化。理论上给出了估计量的渐近正态性，实证表明连续时间方法在宏观金融高频数据拟合上优于离散近似。对您而言，其中的矩阵指数计算、Riccati 方程数值算法及状态空间似然推断，直接关联您在统计计算（矩阵数值方法）及经济理论模型上的兴趣。
- **关键技术**: `matrix exponential`, `Kalman filter`, `continuous-time state-space model`, `maximum likelihood estimation`, `algebraic Riccati equation`, `DSGE`
- **为什么对您有用**: 本文将连续时间 SDE 转化为离散状态空间的矩阵指数与 Riccati 方程求解，直接关联您在统计计算（矩阵数值方法）的兴趣；同时 DSGE 模型是宏观经济学核心，契合您在经济理论模型与数据集上的次级兴趣。

### 2. [10.1016/j.jeconom.2024.105722](https://doi.org/10.1016/j.jeconom.2024.105722) — Local projections vs. VARs: Lessons from thousands of DGPs
- **作者**: Dake Li, Mikkel Plagborg-Møller, Christian K. Wolf
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 2 · pp 105722
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文在数千个模拟宏观经济数据生成过程（DGP）下，系统比较了局部投影（LP）与向量自回归（VAR）对结构脉冲响应（动态因果效应 estimand）的估计表现。研究涵盖了多种识别方案及估计变体（偏差校正、收缩先验、模型平均），揭示了清晰的偏差-方差权衡：LP 估计量偏差较低，但在中长期预测时方差显著高于 VAR。若研究者极度重视无偏性，偏差校正 LP 是首选；若同时关注精度，VAR 方法更具吸引力（短期/长期用贝叶斯 VAR，中期用最小二乘 VAR）。该工作本质上是对宏观时序因果推断中两种主流估计量的有限样本性质的大规模计算实验。对您在经济理论应用中评估动态因果效应的估计策略与精度-偏差权衡具有直接参考价值。
- **关键技术**: `structural impulse response`, `local projection`, `vector autoregression`, `bias-variance trade-off`, `Bayesian shrinkage`
- **为什么对您有用**: 直接对应您在经济理论（因果推断）方向的兴趣，通过大规模模拟系统展示了宏观时序中动态因果效应估计的偏差-方差权衡，为实际应用中选择 LP 还是 VAR 提供了明确的有限样本指导。

### 3. [10.1016/j.jeconom.2024.105750](https://doi.org/10.1016/j.jeconom.2024.105750) — Vector autoregressions with dynamic factor coefficients and conditionally heteroskedastic errors
- **作者**: Paolo Gorgi, Siem Jan Koopman, Julia Schaumburg
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 2 · pp 105750
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文提出了一种分析具有时变系数矩阵和条件异方差误差的向量自回归（VAR）模型的新方法，目标是在系统整体稳定性假设下推导出明确定义的脉冲响应函数（IRF）。该方法通过引入动态因子结构来参数化时变系数矩阵，降低了参数维度并保证了估计的可行性；误差项采用条件异方差设定以捕捉波动率聚类。脉冲响应函数的推导依赖于系统的稳定性条件，而非传统的局部平稳假设。实证分析美国工业生产、通胀和债券利差的数据表明，固定系数VAR模型在危机期间会严重低估金融冲击对产出和通胀的影响，而时变因子模型能有效捕捉经济与金融变量间的时变联动。对您可能有用：该文提供了宏观经济学中结构冲击识别（IRF）的时变参数模型框架，适合作为经济理论中因果推断（结构VAR冲击识别）的应用案例和数据参考。
- **关键技术**: `time-varying vector autoregression`, `dynamic factor structure`, `impulse response function`, `conditional heteroskedasticity`, `structural shock identification`
- **为什么对您有用**: 该文属于经济理论中的因果推断应用（结构VAR的脉冲响应与冲击识别），展示了时变参数模型在宏观金融数据中的实证价值，为您在经济数据集上的因果推断应用提供了模型参考与数据集思路。

### 4. [10.1016/j.jeconom.2024.105786](https://doi.org/10.1016/j.jeconom.2024.105786) — Scenario-based quantile connectedness of the U.S. interbank liquidity risk network
- **作者**: Tomohiro Ando, Jushan Bai, Lina Lu, Cindy M. Vojtech
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 2 · pp 105786
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究美国银行间流动性风险网络在不同市场情景（分位数）下的溢出连通性，设定为高维因子增广向量自回归（FAVAR）框架。方法上，通过分位数回归估计高维VAR系数，引入潜在因子结构克服维度灾难，并基于预测误差方差分解构建情景依赖的连通性指数。估计过程采用惩罚分位数回归与因子提取的迭代算法，其渐近性质依赖于大N大T联合收敛理论。实证揭示了流动性风险在尾部极端情景下的溢出机制与均值情景存在显著差异，系统性风险高度集中于少数核心银行。对您有用：该文是高维因子模型与分位数回归在经济网络中的典型应用，其大N大T联合渐近框架及高维矩阵计算细节对您的 high-dimensional statistics 与 stat_computing 兴趣有直接参考价值，同时提供了金融风险传染的实证数据模式。
- **关键技术**: `high-dimensional factor model`, `quantile vector autoregression`, `spillover index`, `penalized quantile regression`, `large N and large T asymptotics`
- **为什么对您有用**: 论文的核心方法是大N大T下的高维因子增广分位数VAR，直接关联您的 high-dimensional statistics 兴趣；同时作为经济网络应用，其数据结构与建模思路对 econ_theory 兴趣有实证参考价值。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

