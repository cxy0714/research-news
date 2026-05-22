# J. Econometrics — Vol 242  Issue 2  ·  2026-05-21

- 共 6 篇 · Journal of Econometrics

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1016/j.jeconom.2024.105804](https://doi.org/10.1016/j.jeconom.2024.105804) — A Correlated Random Coefficient panel model with time-varying endogeneity
- **作者**: Louise Laage
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 242 · issue 2 · pp 105804
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究具有随机系数的线性面板模型，在不限制时恒定不可观测异质性与协变量联合分布的设定下，目标是识别平均偏效应（APE）。当固定效应方法无法控制回归变量与时变扰动项的相关性（时变内生性）时，作者利用控制变量提出了构造性的两步识别论证。第一步非参数识别给定回归变量和控制变量下扰动项的条件期望，第二步利用“组间”变异修正内生性以识别 APE。基于此，提出 APE 的半参数估计量，证明了其 √n-CAN 性质并导出渐近方差，算法计算简便。该文对您有用，因为其在面板数据中处理时变内生性的控制变量思路，以及半参数 √n-CAN 估计量的推导，直接关联您关注的纵向因果推断与半参数理论。
- **关键技术**: `random coefficient model`, `time-varying endogeneity`, `control variable approach`, `semiparametric estimation`, `sqrt(n)-CAN`, `between-group variation`
- **为什么对您有用**: 该文处理面板数据中的时变内生性问题，属于纵向因果推断范畴；其半参数估计量推导和 √n-CAN 性质与您关注的半参数效率理论高度契合，且提供了经济学中的实证应用案例。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1016/j.jeconom.2024.105809](https://doi.org/10.1016/j.jeconom.2024.105809) — On LASSO for high dimensional predictive regression
- **作者**: Ziwei Mei, Zhentao Shi
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 242 · issue 2 · pp 105809
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究高维线性预测回归（$p>n$）中包含大量单位根回归元时的 LASSO 估计性质。LASSO 的一致性依赖于回归元与误差项交叉乘积的偏差界（deviation bound）以及 Gram 矩阵的 restricted eigenvalue (RE)，作者针对平稳、非平稳及协整混合回归元的场景推导了这两个关键分量的新概率界。理论证明，在单位根存在时 LASSO 的收敛率与截面数据情形不同，但在尺度标准化后仍能保持渐近保证。实证部分结合宏观经济学先验，在 FRED-MD 数据库上预测失业率展示了良好表现。对您有用：该文对高维 LASSO 在非平稳设定下的 RE 条件与偏差界的新推导，直接契合您的高维统计理论兴趣，且 FRED-MD 数据集对经济理论应用方向具有数据价值。
- **关键技术**: `LASSO`, `restricted eigenvalue`, `deviation bound`, `nonstationary time series`, `unit root`, `predictive regression`
- **为什么对您有用**: 拓展了高维 LASSO 的 RE 条件与偏差界至非平稳时间序列，直接契合您对高维统计理论的兴趣；同时 FRED-MD 宏观经济数据集对经济理论应用方向有数据价值。

## 非参数 / 半参数  *(nonparam_semipara, 2 篇)*

### 1. [10.1016/j.jeconom.2024.105806](https://doi.org/10.1016/j.jeconom.2024.105806) — Identification and estimation of dynamic structural models with unobserved choices
- **作者**: Yingyao Hu, Yi Xin
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 242 · issue 2 · pp 105806
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究单主体动态离散选择模型中代理人行动不可观测时的非参数识别与估计问题，核心 estimand 为选择概率与潜在状态转移规则。利用连续状态变量的变分，作者证明了在正则条件下上述目标的非参数可识别性，并将该策略拓展至含序列相关不可观测异质性、选择受限及动态博弈的设定。估计方面，提出了筛极大似然估计量以恢复效用函数原参数与转移规则。蒙特卡洛模拟支持了该方法的有效性。该文对您有用，因为它在复杂经济结构模型中展示了 sieve MLE 的非参数识别与估计机制，直接契合您在半参数/非参数理论及经济理论模型方面的兴趣。
- **关键技术**: `dynamic discrete choice model`, `nonparametric identification`, `sieve maximum likelihood estimation`, `unobserved heterogeneity`, `latent state transition`
- **为什么对您有用**: 直接契合您在半参数/非参数理论及经济理论模型方面的兴趣；展示了如何在存在不可观测行动与异质性的复杂结构模型中构建 sieve MLE 并证明非参数识别，对处理潜在变量模型的识别与估计有方法论借鉴意义。

### 2. [10.1016/j.jeconom.2024.105805](https://doi.org/10.1016/j.jeconom.2024.105805) — Nonparametric identification and estimation of stochastic block models from many small networks
- **作者**: Koen Jochmans
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 242 · issue 2 · pp 105805
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文在观测多个独立且固定规模小网络的设定下，研究带节点潜变量的加权随机块模型（SBM）的非参数识别与估计。在一个简单的秩条件下，作者证明了仅凭固定规模图上边与权重的联合边际分布，即可非参数识别潜社区的数量、分布及条件分布。该识别论证具有构造性，据此提出的非参数估计量在计算上可行。极限理论在网络数量趋于无穷而网络规模固定的渐近框架下建立，推导了估计量的渐近性质。该文的秩条件识别策略与构造性估计方法，对您关注的非参数/半参数理论及经济理论中的网络计量模型具有直接参考价值。
- **关键技术**: `stochastic block model`, `nonparametric identification`, `rank condition`, `latent community structure`, `many-network asymptotics`
- **为什么对您有用**: 该文利用秩条件实现有限混合模型的非参数识别，其构造性估计与渐近理论对您关注的非参数/半参数理论有直接启发，且属于经济理论中的网络计量模型。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1016/j.jeconom.2024.105816](https://doi.org/10.1016/j.jeconom.2024.105816) — Semiparametrically optimal cointegration test
- **作者**: Bo Zhou
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 242 · issue 2 · pp 105816
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在有限阶 VAR 模型的协整秩检验问题中，将创新分布视为无穷维 nuisance 参数，目标是构造半参数意义下最优的检验。基于 Le Cam 极限实验理论，推导出该情境下的极限实验为 Locally Asymmptotically Brownian Functional (LABF)，并利用其结构形式 Ornstein-Uhlenbeck 实验建立渐近不变检验的 power envelope（含/不含时间趋势两种设定）。提出基于非参数密度估计的可行检验，证明其功效可达半参数 power envelope，从而实现半参数最优性。模拟显示小样本下 size 控制良好且功效显著优于 Gaussian 基准；非 Gauss 分布下可获得可观的额外功效。对您有用：该文将 Le Cam 效率理论、半参数 power envelope 与非参数密度估计结合，直接推进了您在半参数效率界与假设检验交叉方向的理解，且协整检验是计量经济学的经典应用场景。
- **关键技术**: `Le Cam limit experiment theory`, `Locally Asymptotically Brownian Functional (LABF)`, `Ornstein-Uhlenbeck experiment`, `semiparametric power envelope`, `nonparametric density estimation`, `asymptotically invariant tests`
- **为什么对您有用**: 直接连接您在半参数效率界与假设检验两个 primary interest：用 Le Cam 理论推导半参数 power envelope 并构造可达该包络的可行检验，方法框架可迁移至其他半参数检验问题；同时协整秩检验是经济理论 secondary interest 的核心议题。

### 2. [10.1016/j.jeconom.2024.105811](https://doi.org/10.1016/j.jeconom.2024.105811) — Change-point analysis of time series with evolutionary spectra
- **作者**: Alessandro Casini, Pierre Perron
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 242 · issue 2 · pp 105811
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究局部平稳时间序列谱密度的变点检测问题，设定在原假设下谱密度随时间平滑变化，而在备择假设下出现断点或平滑度下降。针对谱密度在未知日期和频率处的间断，以及短时期内无断点但发生突变的情况，作者将其统一归结为谱密度随时间平滑度的变化。在检验方面，推导了极小化最优检验区分边界（minimax distinguishable boundary）的最优收敛率，即在统一控制第一、二类误差前提下可检测的最小断点幅度。在估计方面，提出了一种基于 wild sequential top-down 算法的变点估计方法，并证明了该方法在断点幅度收缩且变点数量可能增长的情况下的一致性。对您有用：本文的极小化最优检验框架与区分边界率推导直接契合您对假设检验与数学统计理论的兴趣，其 wild sequential 算法也为统计计算提供了新思路。
- **关键技术**: `minimax optimal testing`, `distinguishable boundary`, `evolutionary spectra`, `locally stationary process`, `wild sequential top-down algorithm`, `spectral density estimation`
- **为什么对您有用**: 本文对极小化最优检验区分边界的理论推导直接契合您在假设检验与数学统计方面的核心兴趣；同时，其针对经济时间序列的应用及提供的软件包也符合您对经济理论中数据集与方法的关注。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

