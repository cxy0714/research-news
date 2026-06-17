# J. Econometrics — Vol 254  ·  2026-06-07

- 共 12 篇 · Journal of Econometrics

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.1016/j.jeconom.2026.106219](https://doi.org/10.1016/j.jeconom.2026.106219) — The informativeness of combined experimental and observational data under dynamic selection
- **作者**: Yechan Park, Yuya Sasaki
- **期刊/来源**: Journal of Econometrics
- **机构**: Harvard University Press · Vanderbilt University
- **分类**: vol 254 · pp 106219
- 相关性 9/10 · novelty: `new_theory`
- **摘要**: 在动态选择（survivorship bias）设定下，本文研究长期因果效应 ATETS（Average Treatment Effect on the Treated Survivors）的 identification 问题。第一个理论结果：在无模型约束且无辅助数据时，ATETS 的 informative bounds 不可能获得——即 partial identification 下的完全负结果。第二个结果：利用短期实验数据与长期观测数据的组合（data combination，沿 Athey et al. 2020 路线），可以在不施加经典模型约束下获得 informative bounds，推翻上述不可能性。基于 Chesher & Rosen (2017) 的 systematic partial identification framework，本文推导了融合 data-combination principle 与经典模型约束的 sharp bounds。实证应用于职业培训项目对就业的长期效应。对您有用：本文的 impossibility-to-possibility via data combination 逻辑与 proximal CI 用 negative control 打破 identification impossibility 的思路有结构相似性，且 ATETS 的 dynamic selection 设定直接连接您 longitudinal causal inference 的子方向。
- **关键技术**: `partial identification`, `sharp bounds (Chesher-Rosen framework)`, `data combination (experimental + observational)`, `ATETS under dynamic selection`, `impossibility result without auxiliary data`
- **为什么对您有用**: 本文直接命中您 causal inference 中 identification theory 和 longitudinal 子方向：ATETS 在 dynamic selection 下的 impossibility 结果与 proximal CI 的 identification impossibility/possibility 结构高度相似。您 moderately_familiar 的 identification theory 可以直接切入——impossibility 部分的论证逻辑与您熟悉的 minimax bound 思路有共鸣，sharp bounds 推导需在 Chesher-Rosen framework 上稍作 lifting。**中期可做**：需先在 moderately_familiar 的 identification theory 上长肌肉（特别是 partial identification / sharp bounds 的数学工具），之后可以尝试将 data-combination principle 与 proximal CI 的 negative control 设定做统一框架。

### 2. [10.1016/j.jeconom.2026.106186](https://doi.org/10.1016/j.jeconom.2026.106186) — Regularizing fairness in optimal policy learning with distributional targets
- **作者**: Anders Bredahl Kock, David Preinerstorfer
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 254 · pp 106186
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在最优政策学习框架下，决策者利用训练数据学习处理效应并选择使目标泛函（如均值或分位数）最优的实施机制，但可能对特定子群体的结果分布偏离总体最优分布（即“不公平”）产生顾虑。本文提出一个正则化框架，允许决策者在广泛类别的目标泛函和公平性度量下，对子群体与总体结果分布的偏离进行惩罚调节。核心方法是带（可能数据驱动）偏好参数的 empirical success policy，作者建立了该政策的 regret 界和一致性保证，并通过数值实验和两个实证应用加以验证。对您可能有用：该框架的 regret 分析与 semiparametric efficiency / minimax 理论有自然对接，且公平性正则化可视为对 policy value 的 constrained optimization，与您在 causal inference estimation theory 的兴趣直接相关。
- **关键技术**: `optimal policy learning`, `empirical success policy`, `regret bounds`, `distributional target functional`, `fairness regularization`, `data-driven preference parameters`
- **为什么对您有用**: 直接连接 causal inference 中的最优政策学习与 estimation theory：regret 界的建立涉及 minimax / semiparametric 效率视角下的 policy value 估计，与您 very_familiar 的 minimax bounds 和 moderately_familiar 的 semiparametric theory 对接。用 minimax bound 验证其 regret 界是否紧是一个可攻的口子。Follow-up 判断：中期可做——需先在 moderately_familiar 的 semiparametric theory 上长肌肉（具体是 constrained semiparametric efficiency / policy learning 的 influence function 分析），才能判断其 regret 界是否可达 sharper rate。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1016/j.jeconom.2026.106203](https://doi.org/10.1016/j.jeconom.2026.106203) · [arXiv](https://arxiv.org/abs/1307.0578) — High-dimensional conditional factor model
- **作者**: Zhonghao Fu, Shang Gao, Liangjun Su, Xia Wang
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 254 · pp 106203
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文提出非参数条件因子回归（NCFR）模型，处理高维输入-响应设定下的回归问题，estimand 为条件均值响应，关键假设为响应与输入通过低维潜因子中介且因子载荷具有无限稀疏先验。方法核心引入 Indian Buffet Process（IBP）先验对潜因子维度做非参数贝叶斯推断，实现自动维度选择与降维，替代传统因子回归的固定秩约束。理论方面未给出 minimax rate 或 semiparametric efficiency bound，仅以实验对比展示预测精度优于线性回归及若干替代方法。对您可能有用：若将 NCFR 的 IBP-因子结构嵌入 proximal CI 的 negative-control 框架，可探索高维混杂调整中的非参数降维路径。
- **关键技术**: `Indian Buffet Process prior`, `nonparametric Bayesian factor model`, `latent factor regression`, `high-dimensional dimensionality reduction`, `conditional mean estimation`
- **为什么对您有用**: 本文连接到高维统计中的因子模型降维方向，但未触及 RMT 或 minimax 理论，属于贝叶斯非参数方法侧。用您 very_familiar 的高维渐近理论可审视其因子估计的收敛性质是否可给出 rate；用 moderately_familiar 的 semiparametric 理论可尝试为 NCFR 构造 efficient influence function 与 debiased 版本。中期可做：需先在 moderately_familiar 的 semiparametric 理论上长肌肉，才能将 IBP-因子结构纳入 semiparametric efficiency 框架做理论分析。

## 非参数 / 半参数  *(nonparam_semipara, 2 篇)*

### 1. [10.1016/j.jeconom.2026.106187](https://doi.org/10.1016/j.jeconom.2026.106187) — Minimax rates of convergence for nonparametric location-Scale models
- **作者**: Bingxin Zhao, Yuhong Yang
- **期刊/来源**: Journal of Econometrics
- **机构**: University of Minnesota · Huaibei Mining (China) · Tsinghua University
- **分类**: vol 254 · pp 106187
- 相关性 9/10 · novelty: `new_theory`
- **摘要**: 在非参数 location-scale 模型（涵盖 mean、quantile、expectile 回归）设定下，本文研究回归函数在 squared L2 损失下的 minimax 收敛速率，关键 regularity 假设为误差分布的 Hellinger 可微性。核心结论表明，minimax rate 完全由非参数函数类的 metric entropy 决定，将经典熵驱动速率结构推广至更一般的 location-scale 框架。文章具体验证了 asymmetric Laplace、Cauchy、normal-Laplace 等误差分布下的 Hellinger 可微条件，并推导了 low order interaction 与 multiple index 模型的 minimax rate。对您有用：本文直接推进了您 very_familiar 的 minimax bounds 与 nonparametric statistics 交叉领域，并为 econometrics 中的 quantile/expectile 回归提供了理论基准。
- **关键技术**: `minimax rate of convergence`, `metric entropy`, `Hellinger differentiability`, `location-scale regression`, `quantile and expectile regression`, `multiple index model`
- **为什么对您有用**: (1) 本文连接到非参数理论中的 minimax estimation bounds，以及 econ theory 中常用的 quantile/expectile regression 模型设定。(2) 您 very_familiar 的 minimax bounds for estimation problems 和 nonparametric statistics 可以直接用来审视本文的 entropy-driven rate 结论是否紧，并探索将其推广到您 moderately_familiar 的 semiparametric theory 框架（如部分线性 location-scale 模型）。(3) **立即可做**：用熟悉的 minimax 与 entropy 工具即可验证/拓展本文的 multiple index model 速率到高维或 semiparametric 设定。

### 2. [10.1016/j.jeconom.2024.105732](https://doi.org/10.1016/j.jeconom.2024.105732) — Intraday volatility patterns from short-dated options
- **作者**: Viktor Todorov, Yang Zhang
- **期刊/来源**: Journal of Econometrics
- **机构**: Northwestern University
- **分类**: vol 254 · pp 105732
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文在in-fill渐近框架下，提出一种从短期期权（零日与一日到期）高频日内数据中非参数估计波动率确定性周期成分的方法。核心estimand是波动率的周期性成分，关键假设为期权strike网格足够密且到期时间极短。方法机制为：在每个时间点，分别对两种tenor的期权聚合，形成条件风险中性期望未来积分变差的非参数估计；通过两者之比，消除条件期望中的随机成分（至高阶余项），提取确定性周期成分。理论结果给出CLT，收敛速率由strike网格间距与到期时间长度决定，属于非参数率。实证应用于S&P 500指数期权数据。对您可能有用：该文的非参数比率消随机成分技巧与semiparametric效率理论中的orthogonalization思路有结构相似性，且in-fill渐近与高频infill设定可类比于您熟悉的inverse problems with random noise。
- **关键技术**: `nonparametric sieve estimation`, `in-fill asymptotics`, `risk-neutral expectation ratio`, `central limit theorem for nonparametric estimator`, `high-frequency options data`
- **为什么对您有用**: 本文连接到nonparametric/semiparametric理论子方向，其比率消随机成分的技巧与HOIF/orthogonal score的思路有结构类比，但具体金融期权模型与您当前武器库（treewidth/tensor contraction、minimax bounds for estimation）不直接对口。中期可做：若先在moderately_familiar的semiparametric theory上加深对in-fill渐近与inverse-problem非参数率的理解，可尝试将该比率估计的效率界与您熟悉的minimax框架对接，验证其速率是否紧。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1016/j.jeconom.2026.106217](https://doi.org/10.1016/j.jeconom.2026.106217) · [arXiv](https://arxiv.org/abs/2403.18248) — Statistical inference of optimal allocations I: Regularities and their implications
- **作者**: Kai Feng, Han Hong, Denis Nekipelov
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 254 · pp 106217
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 在最优分配（optimal allocation）问题中，目标是推断政策价值函数（value function）的渐近性质与估计。本文通过几何测度论工具分析排序算子（sorting operator）的性质，推导出价值函数的 Hadamard 可微性。基于该可微性结果，应用 functional delta method 得到二元约束最优分配价值函数过程及 plug-in ROC 曲线估计量的渐近分布。进一步，价值函数的凸性导致其对政策参数的一阶导数退化（degeneracy），作者据此构造了 double/debiased 估计量。值得注意的是，验证 Hadamard 可微性的条件恰好对应分类文献中的 margin assumption，从而为 plug-in 方法的快速收敛率提供了理论解释。对您而言，本文将 Hadamard 可微性 + functional delta method 与 debiased estimation 在政策价值函数场景下统一，直接连接到 efficiency theory 与 causal inference 中 treatment allocation 的估计问题。
- **关键技术**: `Hadamard differentiability`, `functional delta method`, `sorting operator`, `geometric measure theory`, `double/debiased estimator`, `margin assumption`
- **为什么对您有用**: 本文直接推进 efficiency theory 中 debiased estimator 在最优分配价值函数（causal inference 的 policy evaluation 子方向）的理论；一阶 IF 退化场景与您 moderately_familiar 的 HOIF 天然对接——可用 HOIF 视角审视其 debiased 构造是否可被更高阶 influence function 修正进一步 sharpen rate。Follow-up 判断：中期可做——需先在 HOIF 理论上长肌肉，才能系统地将 higher-order influence function 推广到此类 degenerate value function 估计并验证是否可获得更优收敛率。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1016/j.jeconom.2025.106132](https://doi.org/10.1016/j.jeconom.2025.106132) — Testing for jumps in a discretely observed price process with endogenous sampling times
- **作者**: Qiyuan Li, Yifan Li, Ingmar Nolte, Sandra Nolte, Shifan Yu
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 254 · pp 106132
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在离散观测的 Itô 半鞅价格过程设定下，本文提出一种非参数高频跳跃检验方法，目标是区分布朗运动成分导致的阈值越界与真实跳跃。观测时间由对称双边界首次退出时间递归生成（endogenous sampling），检验统计量在此非均匀采样下仍可行且对市场微结构噪声稳健。核心机制利用首次退出时间的分布性质构造阈值准则，将连续扩散的越界概率与跳跃导致的越界分离，从而实现 feasible test。模拟显示有限样本表现优于现有方法；NYSE 实证分析提供跳跃存在的统计证据且对伪检测稳健。对您可能有用：该文将非参数检验与 endogenous sampling 结合，是 hypothesis testing 子方向中处理非均匀观测的新视角。
- **关键技术**: `Itô semimartingale jump test`, `first exit time sampling`, `endogenous sampling times`, `nonparametric threshold test`, `noise-robust inference`, `high-frequency financial data`
- **为什么对您有用**: 本文直接连接到 hypothesis testing 子方向，在非均匀 endogenous sampling 下构造非参数跳跃检验，是经典 Itô 半鞅跳跃检验（如 Ait-Sahalia/Jacod 框架）的扩展。用您 very_familiar 的 nonparametric statistics 与 minimax bounds 工具，可以审视该检验在更一般采样机制下的 rate 是否达到最优；若要深入其 endogenous sampling 的分布理论，需在 moderately_familiar 的 M-estimation theory 上补充随机时间变换的极限理论。中期可做。

## 经济理论 / 应用  *(econ_theory, 5 篇)*

### 1. [10.1016/j.jeconom.2026.106193](https://doi.org/10.1016/j.jeconom.2026.106193) — To be or not to be: Roughness or long memory in volatility?
- **作者**: Mikkel Bennedsen, Kim Christensen, Peter Korsbakke Christensen
- **期刊/来源**: Journal of Econometrics
- **机构**: Aarhus University · Danish Institute for International Studies
- **分类**: vol 254 · pp 106193
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文在连续时间平稳高斯过程框架下，提出基于 composite likelihood 的参数估计方法，目标是随机 log-spot variance 过程的参数 identification 与估计。核心估计量为 maximum composite likelihood estimator (MCLE)，作者推导了其渐近理论（一致性、渐近正态），并通过模拟证明 MCLE 在所考察的粗糙波动率与长记忆波动率模型设定下优于 method-of-moments 估计。实证部分利用加密货币市场高频数据构造 intraday spot log-realized variance，发现短期与长期相关性结构解耦的机制更能刻画波动率动态，spot log-trading volume 的辅助分析也支持该结论。对您可能有用：若关注经济理论中高频金融数据的 semiparametric / parametric 估计与渐近效率，本文的 composite likelihood 渐近理论提供了一个具体案例。
- **关键技术**: `composite likelihood estimation`, `continuous-time Gaussian process`, `asymptotic normality of MCLE`, `rough volatility model`, `long-memory volatility model`, `high-frequency realized variance`
- **为什么对您有用**: 本文连接到经济理论中金融高频数据的参数估计与模型识别问题。composite likelihood 的渐近效率分析可与您武器库中 semiparametric theory / M-estimation theory 对接——用 M-estimation 渐近理论审视 MCLE 的效率界是否达到 semiparametric efficiency bound，是一个中期可做的方向（需先在 moderately_familiar 的 semiparametric theory 上长肌肉以做效率比较）。作为实证应用论文，数据集与分析模式对经济理论方向有参考价值，值得花时间读全文以了解高频波动率建模的常见设定。

### 2. [10.1016/j.jeconom.2025.106150](https://doi.org/10.1016/j.jeconom.2025.106150) — Efficient sampling for realized variance estimation in time-changed diffusion models
- **作者**: Timo Dimitriadis, Roxana Halbleib, Jeannine Polivka, Jasper Rennspies, Sina Streicher, Axel Friedrich Wolter
- **期刊/来源**: Journal of Econometrics
- **机构**: Goethe University Frankfurt · University of Freiburg · University of St.Gallen · ETH Zurich · Swiss Finance Institute · University of Konstanz
- **分类**: vol 254 · pp 106150
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文在时间变换扩散模型(time-changed diffusion)设定下，研究按内在时间(intrinsic time)采样日内收益率对realized variance(RV)估计量的效率影响。模型假设资产价格服从被跳跃过程时间变换的扩散，允许杠杆设定与Hawkes型跳跃过程，分别刻画交易强度与tick方差。在有限样本下理论证明：依允许的采样信息量，RV估计量在hitting time采样（价格变动达阈值即采样）或新提出的realized business time采样（按观测交易与估计tick方差组合采样）下达到最高效率。模拟与股票实证表明低噪声下hitting time采样最优、噪声增大时realized business time更优。对您而言，本文展示了econometrics中如何将效率比较具体化为有限样本采样方案选择，可作为经济理论secondary interest的实证参考案例。
- **关键技术**: `realized variance estimation`, `time-changed diffusion model`, `hitting time sampling`, `realized business time sampling`, `Hawkes-type jump process`, `finite-sample efficiency comparison`
- **为什么对您有用**: 本文属于经济理论secondary interest范畴，提供金融高频数据中RV估计的采样效率比较框架与真实股票数据集。研究者very_familiar的minimax bounds与estimation theory可用来审视其有限样本效率声称是否可推广为更一般的rate/bound结果。中期可做：需先在moderately_familiar的M-estimation theory上补充时间变换扩散模型的极限理论，才能将此处的采样效率分析提升到semiparametric efficiency bound层面；当前作为gateway reading值得花时间读全文了解econometrics高频数据的模型与数据结构。

### 3. [10.1016/j.jeconom.2024.105810](https://doi.org/10.1016/j.jeconom.2024.105810) · [arXiv](https://arxiv.org/abs/2301.06742) — Robust realized integrated beta estimator with application to dynamic analysis of integrated beta
- **作者**: Minseog Oh, Donggyu Kim, Yazhen Wang
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 254 · pp 105810
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文在高频金融数据设定下，目标是在存在微观结构噪声且噪声具有依赖结构、beta时变的非参数框架中，估计 realized integrated beta。作者提出 robust realized integrated beta estimator，利用其作为 proxy 发现 integrated beta 具有 ARMA 动态结构，进而建立 DR Beta 模型并引入高频数据生成过程填补非参数估计与低频动态模型之间的 gap。参数估计采用 quasi-likelihood 方法，并建立所提估计量的渐近定理（收敛率与分布）。模拟与 S&P 500 实证表明 DR Beta 模型有效刻画个股市场 beta 动态并改善预测。对您可能有用：该文在 econometrics 高频设定下结合非参数估计与低频动态模型，其 quasi-likelihood 与渐近分析思路可迁移至您对 semiparametric theory 与 M-estimation 的兴趣。
- **关键技术**: `realized integrated beta`, `microstructure noise correction`, `quasi-likelihood estimation`, `ARMA dynamic structure`, `asymptotic distribution theory`, `nonparametric robust estimator`
- **为什么对您有用**: 本文连接到您 secondary interest 的 econ_theory（高频金融数据的动态 beta 模型与实证）。技术层面，其 quasi-likelihood 渐近分析可由您 moderately_familiar 的 M-estimation theory 直接切入，验证其声称的渐近性质是否紧。Follow-up 判断：中期可做——需先在 moderately_familiar 的 M-estimation theory 上长肌肉以深入其渐近证明细节，但核心框架与您现有武器库兼容。

### 4. [10.1016/j.jeconom.2024.105813](https://doi.org/10.1016/j.jeconom.2024.105813) — Realized drift
- **作者**: Sébastien Laurent, Roberto Renò, Shuping Shi
- **期刊/来源**: Journal of Econometrics
- **机构**: Centre National de la Recherche Scientifique · Institut Universitaire de France · Aix-Marseille Université · École des hautes études en sciences sociales · École Supérieure des Sciences Économiques et Commerciales · Macquarie University
- **分类**: vol 254 · pp 105813
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文在 Itō 半鞅框架下研究高频金融数据中漂移项的检测与估计问题，设定包含微观结构噪声污染与漂移/波动率爆炸。作者提出将 realized variance 分解为漂移分量与波动率分量的新方法，核心估计量基于 realized autocovariance 实现。理论部分在漂移与波动率同时存在跳跃/爆炸的设定下给出估计量的渐近性质，实证表明该分解显著提升波动率预测精度。对您可能有用：若关注高维渐近或逆问题中的随机噪声设定，此文的 realized autocovariance 技术与 semimartingale 渐近分析可提供金融高频数据的应用视角。
- **关键技术**: `realized autocovariance`, `Itō semimartingale`, `microstructure noise`, `realized variance decomposition`, `drift explosion`
- **为什么对您有用**: 本文属于经济理论/金融计量应用，连接到 secondary interest 的经济理论数据集与模型方向。技术层面，realized autocovariance 与 Itō 半鞅渐近理论属于您 very_familiar 的'高维渐近'与'带随机噪声的逆问题'武器可触及的范围，但核心金融计量细节（microstructure noise 建模、drift explosion）需要额外学习。follow-up 判断：中期可做——需先在 moderately_familiar 的 M-estimation 理论或金融计量渐近工具上长肌肉，才能将您的高维渐近/逆问题工具迁移到此设定。

### 5. [10.1016/j.jeconom.2025.106040](https://doi.org/10.1016/j.jeconom.2025.106040) — A multivariate realized GARCH model
- **作者**: Ilya Archakov, Peter Reinhard Hansen, Asger Lunde
- **期刊/来源**: Journal of Econometrics
- **机构**: York University
- **分类**: vol 254 · pp 106040
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 在多变量 GARCH 框架下，目标是利用 realized measures of volatilities 与 correlations 建模联合波动率动态，核心假设是 correlation matrix 可通过 matrix logarithmic transformation 实现无约束向量参数化且天然保持 positive definiteness。方法的关键机制：matrix log 变换将 correlation matrix 映射为无约束向量，避免优化中的正定性约束问题；factor approach 在高维系统中引入 parsimonious 结构，且若干已有模型的因子框架可自然涌现。实证应用于 9 只资产收益，采用 block correlation specification 的因子结构；辅助发现是参数化 realized correlations 的经验分布近似 Gaussian，类比 log-transformed realized variances 的已知结果。对您可能有用：matrix log parametrization 是统计计算中处理 correlation matrix 的数值技巧，与您 statistical computing 兴趣相关；同时该文提供金融数据集与经济理论模型。
- **关键技术**: `matrix logarithmic transformation`, `realized GARCH`, `unconstrained correlation parametrization`, `factor structure for high-dimensional correlations`, `block correlation specification`
- **为什么对您有用**: 本文连接到经济理论（金融多变量波动率模型、9资产数据集）和统计计算（matrix log 无约束参数化 correlation matrix 的数值方法）。武器库中 very_familiar 的 software development 可直接复现 matrix log 参数化的计算部分，但核心计量经济学 likelihood 估计与 GARCH 动态建模不在当前 arsenal 范围。中期可做：若想进入金融计量方向，需先在 moderately_familiar 的 M-estimation theory 上扩展到 GARCH-type quasi-likelihood；若仅关注 matrix log 参数化作为通用计算工具，立即可用 software development 体验复现与推广。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

