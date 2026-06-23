# Scand. J. Stat. — Vol 50  Issue 4  ·  2026-06-23

- 共 17 篇 · Scandinavian Journal of Statistics
- 目录核对 ✅ 17 篇全部抓到（对照 OpenAlex 17 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期共 17 篇论文，呈现出高维统计推断与非参数/半参数方法双核驱动的格局，同时覆盖假设检验、计算方法及因果推断应用。主线大致分为四条：一是**高维与时间序列/网络模型**，涉及稀疏主成分、单指标模型及动态网络；二是**非参数与半参数效率理论**，涵盖粒子系统、缺失数据、Cox 过程及混合效应模型；三是**假设检验与置信推断**，包括有限样本推断与认识论解释；四是**统计计算与因果应用**，涉及球面 MCMC 及观察性研究的模型误设分析。

在**非参数与半参数效率**这条主线上，本期有多篇工作致力于在不同数据生成机制下构建自适应或有效估计量。针对缺失数据问题，*Statistical inference with semiparametric nonignorable nonresponse models* 与 *A robust model averaging approach for partially linear models* 分别通过 profile 似然和模型平均手段处理非可忽略缺失与随机缺失，旨在逼近半参数效率界或实现均方误差最优。针对更复杂的模型结构，*Plug‐in machine learning for partially linear mixed‐effects models* 利用机器学习做 nuisance 参数的正交化去除，在纵向数据下实现了固定效应的 $\sqrt{n}$ 收敛与有效推断；*Efficient t₀‐year risk regression* 则在生存分析框架下推导了风险回归的有效影响函数。此外，*Nonparametric adaptive estimation for interacting particle systems* 与 *Adaptive estimation of intensity in a doubly stochastic Poisson process* 分别将自适应估计理论拓展至交互粒子系统与 Cox 过程，均涉及模型选择下的 oracle 不等式与最优收敛速率。

**高维统计**方面，工作重心在于将经典估计理论拓展至依赖或重尾数据。*Sparse principal component analysis for high‐dimensional stationary time series* 将 SPCA 推广至平稳时间序列，利用惩罚 M 估计与谱分析建立了 oracle 不等式，不再依赖高斯假设。*Robust inference for high‐dimensional single index models* 则在椭圆对称分布假设下，结合 Huber 损失与 debiased Lasso 解决了单指标模型的稳健推断与变量选择问题。*Time‐varying β‐model for dynamic directed networks* 关注动态网络节点参数的非参数平滑估计，探讨了 $n$ 与 $T$ 发散时的渐近性质。此外，*Finite sample inference for empirical Bayesian methods* 提出了基于 Universal Inference 的有限样本检验框架，为高维参数模型提供了不依赖渐近理论的推断工具。

对于关注**因果推断与半参数效率**的研究者，建议优先阅读 *Statistical inference with semiparametric nonignorable nonresponse models* 与 *Plug‐in machine learning for partially linear mixed‐effects models*，二者分别展示了缺失数据与纵向数据下的效率理论构建；*Pitfalls of amateur regression* 则提供了一个关于观察性研究模型误设导致因果结论错误的精彩案例分析。高维方向可关注 *Sparse principal component analysis for high‐dimensional stationary time series* 与 *Robust inference for high‐dimensional single index models*。

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1111/sjos.12662](https://doi.org/10.1111/sjos.12662) · [arXiv](https://arxiv.org/abs/2104.00333) — Pitfalls of amateur regression: The Dutch New Herring controversies
- **作者**: Fengnan Gao, Richard D. Gill
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1901-1918
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文重新分析了一组关于荷兰新鲱鱼消费者排名数据，指出原始研究者使用简单线性回归模型得出排名被操纵的结论存在严重规范错误（specification error）。作者纠正了数据错误，并展示了时空因素（temporal and spatial factors）的复杂性无法用简单模型捕获，尤其是样本量小、混淆因素多时。结果表明，所谓的操纵证据很可能是模型误设造成的人为假象。该研究强调了在观察性研究中识别因果关系时，忽略时空混杂和选择模型不当的危险性。对于您主攻的因果推断方向，这是一份关于模型误设如何导致错误因果结论的警示案例，提醒在纵向数据或空间数据分析中务必谨慎处理协变量结构。
- **关键技术**: `specification error analysis`, `confounding`, `simple linear regression critique`, `descriptive statistics`
- **为什么对您有用**: 本文涉及因果推断中常见的模型误设和混淆问题，直接关联您的 primary interest（因果推断中的识别与估计）。您的武器库中 very_familiar 的非参数统计和逆问题分析可以用于对此类排名数据的更稳健建模（例如使用非参数平滑或工具变量控制未观测混杂）。这是一个中期可做的方向：需要在 moderately_familiar 的识别理论（如充分集合与阴性对照）上加强后，才能设计针对排名数据的因果推断方法。本文本身作为应用批评文章，可作入门参考。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1111/sjos.12664](https://doi.org/10.1111/sjos.12664) · [arXiv](https://arxiv.org/abs/2109.00299) — Sparse principal component analysis for high‐dimensional stationary time series
- **作者**: Kou Fujimori, Yuichi Goto, Yan Liu, Masanobu Taniguchi
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1953-1983
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 在高维平稳时间序列设定下，研究稀疏主成分分析（SPCA）的估计理论与 oracle 不等式。目标是在维度 p 远大于样本量 n 时，对带稀疏惩罚的主成分估计量建立 oracle inequality 和收敛速率。核心方法是 penalized M-estimation，结合 Lasso-type 惩罚与时间序列的谱分析技术；收敛速率依赖于稀疏度参数 s、维度 p 与样本量 n，并给出了 tuning parameter 的理论选择准则。理论结果适用于包括重尾时间序列在内的广泛过程类，不依赖高斯或轻尾假设。对您有用：这是高维统计与时间序列交叉方向的工作，涉及 minimax rate 与 oracle inequality，与您的高维统计和 minimax bound 技术直接相关。
- **关键技术**: `sparse principal component analysis`, `oracle inequality`, `penalized M-estimation`, `high-dimensional stationary processes`, `convergence rate`, `spectral analysis`
- **为什么对您有用**: 连接到您 primary interest 中的高维统计方向，具体涉及 oracle inequality 和收敛速率的建立。您武器库中的 minimax bounds for estimation problems 和 high-dimensional asymptotics 可以直接用来审视本文的收敛速率是否紧、是否可进一步改进。**立即可做**：用 very_familiar 的 minimax bound 技术验证本文速率的 optimality，或尝试将理论推广到更一般的依赖结构。

## 非参数 / 半参数  *(nonparam_semipara, 7 篇)*

### 1. [10.1111/sjos.12661](https://doi.org/10.1111/sjos.12661) — Nonparametric adaptive estimation for interacting particle systems
- **作者**: Fabienne Comte, Valentine Genon‐Catalot
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Université Paris Cité
- **分类**: vol 50 · issue 4 · pp 1716-1755
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在连续时间观测的 interacting particle system 框架下，目标是估计漂移项中两个未知的时变函数（漂移系数线性依赖于空间，扩散系数为常数）。作者在 L² 空间上构造了投影估计量，基于有限维子空间（如三角基或 Hermite 基）进行 sieve 估计，分别研究了经验范数和确定性范数下的 L² 风险收敛率。通过 model selection（惩罚投影方法）实现维度的 data-driven 选择，证明了自适应估计量在 oracle 不等式意义下达到最优收敛率。数值模拟验证了方法在有限样本下的表现。对您在 semiparametric theory 和 nonparametric estimation 方面的技术积累有直接参考价值。
- **关键技术**: `projection estimation`, `sieve estimation`, `model selection`, `oracle inequality`, `L² risk`, `interacting particle systems`
- **为什么对您有用**: 本文属于 nonparametric estimation 的经典 sieve 方法应用，连接到您 primary interest 中的 semiparametric & nonparametric theory。您武器库中的 nonparametric statistics 和 minimax bounds 工具可直接用于审视其收敛率是否紧、oracle inequality 的常数项是否可改进。立即可做：用您熟悉的 minimax lower bound 技术验证其自适应估计量的 rate optimality；或考虑将该方法推广到 drift 具有非线性结构时的 semiparametric partial linear 情形。

### 2. [10.1111/sjos.12652](https://doi.org/10.1111/sjos.12652) — Statistical inference with semiparametric nonignorable nonresponse models
- **作者**: Masatoshi Uehara, Danhyang Lee, Jae‐Kwang Kim
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Cornell University · University of Alabama · Iowa State University
- **分类**: vol 50 · issue 4 · pp 1795-1817
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究非可忽略缺失数据下的半参数响应模型，目标是在放松响应机制参数假设的条件下识别总体参数。作者提出两类有效估计量——profile最大似然估计和profile校准估计，并证明了它们收敛到半参数效率界，且具有渐近正态性。方法上，profile最大似然估计通过剖面似然函数处理响应概率的非参数部分，而profile校准估计则基于校准权重构造，两者均利用经验过程和半参数效率理论推导其渐近性质。模拟实验与韩国劳动收入面板调查的实际数据应用验证了方法的有限样本表现。对于您而言，本文与半参数理论及效率理论兴趣直接相关，为缺失数据下的半参数推断提供了清晰的理论框架和可操作的估计程序。
- **关键技术**: `profile likelihood`, `calibration estimator`, `semiparametric efficiency bound`, `nonignorable nonresponse`, `empirical process`
- **为什么对您有用**: 本文连接您的半参数理论和效率理论兴趣，使用profile似然和校准估计处理非可忽略缺失数据，理论分析中涉及经验过程和M估计方法，这些都可以用您非常熟悉的非参数统计和因果推断估计理论来理解甚至推广。注：问题发现粗判为立即可做，因为武器库中的非参数统计和M估计理论可直接用于评估本文估计量的渐近性质及拓展应用场景。

### 3. [10.1111/sjos.12651](https://doi.org/10.1111/sjos.12651) — Adaptive estimation of intensity in a doubly stochastic Poisson process
- **作者**: Thomas Deschatre
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Électricité de France (France)
- **分类**: vol 50 · issue 4 · pp 1756-1794
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 该文考虑双重随机泊松过程（Cox过程），其随机强度为连续Itô半鞅，在固定观测区间[0,T]上对两者进行连续观测。目标是自适应估计强度函数λ(t)在一个给定区间上的取值。方法采用局部多项式估计器，并提出一种非渐近框架下的带宽选择方法，能够导出oracle不等式。在渐近框架T→∞、带宽h→0且Th→∞下，对于阶数为p的Hölder函数类，当所选多项式次数大于p时，估计器达到rate (Th)^{-p/(2p+1)}，且在minimax意义下最优。实证部分将该方法应用于法国温度和电力现货价格数据，推断电尖峰强度与温度的函数关系。本文贡献在于为Cox过程强度提供可操作的局部多项式自适应估计，弥补了该方向理论结果的空白。
- **关键技术**: `local polynomial estimation`, `doubly stochastic Poisson process`, `oracle inequality`, `adaptive bandwidth selection`, `minimax optimality over Hölder classes`
- **为什么对您有用**: 直接连接您的非参数统计核心兴趣（very_familiar中的nonparametric statistics和minimax bounds），局部多项式+oracle不等式的框架与您处理自适应非参数估计的经验高度契合。实证部分对电力价格尖峰强度的推断连接了secondary interest中的经济理论应用。对于follow-up粗判：**立即可做**——您的nonparametric statistics和minimax bound估算工具可以轻松验证该文声称的最优rate是否紧，并考虑将该带宽选择方法移植到其他基于Cox过程的因果推断问题中（如事件史分析的未观测混杂调整）。

### 4. [10.1111/sjos.12650](https://doi.org/10.1111/sjos.12650) · [arXiv](https://arxiv.org/abs/2304.02421) — Time‐varying <i>β</i>‐model for dynamic directed networks
- **作者**: Yuqing Du, Lianqiang Qu, Ting Yan, Yuan Zhang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1687-1715
- 相关性 7/10 · novelty: `weaker_assumption`
- **摘要**: 本文在动态有向网络框架下推广了经典的β-模型，假设观测到T个时间点的邻接矩阵快照，节点数为n，目标是估计随时间平滑变化的节点参数（如活跃度/声望）。提出核平滑似然估计方法，利用核函数对时间维度加权构造逐点边际似然方程，估计量具有显式形式。建立了当n或T发散时估计量的相合性和渐近正态性，证明中允许T固定而n趋于无穷，或反之，这与单网络分析中要求n发散不同。技术工具包括核平滑的偏似然、渐近展开以及网络邻接的独立性假设。模拟验证了理论预测，并在邮件数据集上展示了实际应用。对您可能有用：该工作涉及高维参数（n个节点）的非参数时间平滑，其渐近分析技巧（核估计、大n或大T下的收敛性）可与您熟悉的高维渐近论和非参数统计对接，尤其对动态网络中的因果推断（如随时间变化的处理效应）有潜在启发。
- **关键技术**: `kernel-smoothed likelihood`, `β-model for directed networks`, `time-varying parameter estimation`, `asymptotic normality in high-dimensional setting`, `network snapshot data`
- **为什么对您有用**: 本文与您的主要兴趣子方向——高维统计中的非参数估计和渐近理论——直接相关。您非常熟悉的'非参数统计'技能（核估计的收敛性质、渐近展开）可直接用于审视该文的证明策略及其扩展可能性，例如是否可提出自适应带宽选择或构造时间变点检验。立即可做：该文的技术难度在您的武器库射程内，无需额外工具即可跟进全文。

### 5. [10.1111/sjos.12638](https://doi.org/10.1111/sjos.12638) — Robust inference for high‐dimensional single index models
- **作者**: Dongxiao Han, Miao Han, Jian Huang, Yuanyuan Lin
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Nankai University · Shanghai University of Finance and Economics · Hong Kong Polytechnic University · Chinese University of Hong Kong
- **分类**: vol 50 · issue 4 · pp 1590-1615
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对高维单指标模型（single index model）提出一种稳健推断方法，其中链接函数未知且协变量服从椭圆对称分布。该方法基于Huber损失函数，避免了对未知链接函数的估计，并采用Lasso进行变量选择。理论上建立了Lasso估计量在相差一个乘性常数意义下的ℓ∞相合性，并在预测变量的协方差矩阵满足irrepresentable条件时，证明了符号支持的恢复性质。基于debiased Lasso，进一步给出了逐分量和分组的置信区间与假设检验方法。大量模拟和一个核黄素生产数据集的实证分析验证了方法的有限样本性能。这篇文章的方法论与高维统计和半参数推断直接相关，尤其是其稳健损失和debiased Lasso框架可迁移到其他高维推断问题中，对您在高维统计和非参数理论方面的研究有参考价值。
- **关键技术**: `Huber loss`, `debiased Lasso`, `single index model`, `irrepresentable condition`, `signed support recovery`, `component-wise inference`
- **为什么对您有用**: 本文聚焦高维单指标模型的稳健推断，属于高维统计与半参数理论的交叉问题，直接连接您对高维统计和非参数/半参数理论的兴趣。您的技术武器库中的nonparametric statistics和high-dimensional asymptotics可以立即用于评估该估计量的minimax最优性，或检验其相合性条件在更弱设定下是否仍成立。立即可做：无需额外学习核心工具即可深入理解并可能改进该方法的理论边界。

### 6. [10.1111/sjos.12659](https://doi.org/10.1111/sjos.12659) — A robust model averaging approach for partially linear models with responses missing at random
- **作者**: Zhongqi Liang, Qihua Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Zhejiang Gongshang University · Zhejiang University · Chinese Academy of Sciences · Academy of Mathematics and Systems Science
- **分类**: vol 50 · issue 4 · pp 1933-1952
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对响应变量随机缺失 (MAR) 的部分线性模型，提出一种稳健模型平均估计方法。假设选择概率函数服从参数模型，该方法基于加权Mallows型准则得到最优模型权重。稳健性体现在：只要真实选择概率是假定模型的某个可测函数，渐近最优性就成立——即所得模型平均估计的均方误差渐近最小。方法本质上结合了逆概率加权与模型平均，并通过最小化加权Mallows准则获得权重向量。模拟和两个真实数据示例验证了方法的有限样本表现。对您而言，该工作直接属于半参数模型与缺失数据处理这一研究方向，与您的因果推断中处理缺失协变量/结局的估计问题高度相关，可作为拓展 IPW 模型平均的参考。
- **关键技术**: `model averaging`, `Mallows criterion`, `partially linear models`, `missing at random`, `inverse probability weighting`
- **为什么对您有用**: (1) 本文核心是MAR下部分线性模型的稳健估计，这是您因果推断兴趣中缺失数据处理的具体场景； (2) 您非常熟悉的'estimation theory in causal inference'（含IPW）可直接用于实现类似的模型平均方案，而'semiparametric theory'（中等熟悉）可帮您将方法推广到更复杂的因果参数（如ATE）； (3) 立即可做：您可以基于本文的MI准则尝试对因果推断中的倾向得分与结局模型进行稳健平均，作为提升双重稳健估计鲁棒性的工具。

### 7. [10.1111/sjos.12660](https://doi.org/10.1111/sjos.12660) — Deep neural network classifier for multidimensional functional data
- **作者**: Shuoyang Wang, Guanqun Cao, Zuofeng Shang, for the Alzheimer's Disease Neuroimaging Initiative
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Yale University · Auburn University · New Jersey Institute of Technology
- **分类**: vol 50 · issue 4 · pp 1667-1686
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对多维函数型数据的分类问题，提出了FDNN（functional deep neural network）方法。该方法先对训练数据提取主成分，再训练深度神经网络，用于预测新数据函数的类别标签。与传统的函数判别分析（FDA）仅适用于一维函数数据不同，FDNN可以处理非高维多维函数数据。在log密度比具有局部连通函数模块结构时，证明FDNN达到minimax最优性。通过模拟和真实数据集（阿尔茨海默病神经影像学）验证了方法的优越性。本文与您的非参数minimax理论兴趣直接相关，其minimax最优性的证明思路可启发其他非参数分类问题的分析。
- **关键技术**: `functional data analysis`, `deep neural network`, `principal component analysis`, `minimax optimality`, `classification`
- **为什么对您有用**: 本文核心贡献在非参数分类的minimax最优性，属于您primary interest中的非参数理论。您对minimax界和非常数统计非常熟悉（very_familiar），可立即验证其最优性条件的紧性，并考虑将证明思路迁移至您研究的U-统计量分类设定。因此立即可做——但本文方法偏向应用，若时间有限可仅读定理部分。

## 效率理论 / Debiased ML  *(efficiency_dml, 2 篇)*

### 1. [10.1111/sjos.12658](https://doi.org/10.1111/sjos.12658) — Efficient t0$$ {t}_0 $$‐year risk regression using the logistic model
- **作者**: Torben Martinussen, Thomas Harder Scheike
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Copenhagen
- **分类**: vol 50 · issue 4 · pp 1919-1932
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对生存分析中 t₀-year risk（患者存活超过特定时间点 t₀ 的概率）的回归问题，在 logistic 模型框架下推导了最有效的估计量。现有方法采用逆概率删失加权（IPWCC）及其增强版（AIPWCC），但 AIPWCC 基于完整数据有效影响函数构造，并非该设定下的最优估计。作者首先在单终点生存数据下给出了完整数据有效影响函数，进而推导出最有效估计量的显式形式，该估计量通过正交化（orthogonalization）消除了 nuisance 参数的影响，实现了半参数效率界（semiparametric efficiency bound）。进一步将结果推广至竞争风险（competing risks）设定，每一步都保留了 n^{-1/2}-收敛和渐近正态性质。模拟和骨髓移植患者真实数据表明，所提估计量较 IPWCC 和 AIPWCC 均有显著的效率提升。对您而言，这项工作直接连接了效率理论（semiparametric efficiency bounds）与生存/删失数据的因果推断，尤其是其中正交化思想和影响函数推导的方法，可迁移至您的脱落（attrition）或多终点研究问题。
- **关键技术**: `efficient influence function`, `IPWCC`, `AIPWCC`, `orthogonal score`, `competing risks`, `semiparametric efficiency bound`
- **为什么对您有用**: (1) 直接命中您效率理论（semiparametric efficiency bounds）和因果推断（删失数据处理）两个 primary interest 的交集——推导完整数据有效影响函数并构造最优估计量，属于经典 semiparametric theory 的落地应用。(2) 您 very_familiar 中的“estimation theory in causal inference”和 moderately_familiar 中的“semiparametric theory”以及“identification theory”可无缝攻破本工作：er您已有正交化和 cross-fitting 框架，可进一步检查其效率增益是否在更弱假设（如连续删失）下依然成立。(3) 中期可做：此文的技巧（不同原因竞争风险下的 IF）直接对应您关注的 mediation 和 longitudinal 结构，可作为扩展至 left-truncation 或时变协变量设定的起点。

### 2. [10.1111/sjos.12639](https://doi.org/10.1111/sjos.12639) — Plug‐in machine learning for partially linear mixed‐effects models with repeated measurements
- **作者**: Corinne Emmenegger, Peter Bühlmann
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: ETH Zurich
- **分类**: vol 50 · issue 4 · pp 1553-1567
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对部分线性混合效应模型（含重复测量）提出一种 plug-in 机器学习估计方法，目标是对线性固定效应系数进行半参有效推断。传统做法依赖样条或核方法处理非线性项，本文则允许使用任意机器学习算法（如随机森林、boosting）来拟合非线性部分和交互作用。核心机制是先将线性协变量和响应变量分别对非线性协变量做非参数偏调整，然后在调整后的变量上拟合标准线性混合效应模型。理论证明该固定效应估计量以参数速率 n^{-1/2} 收敛、渐近正态且达到半参效率界。模拟表明覆盖概率优于惩罚回归样条方法。在 HIV 感染者纵向数据集上给出了实证演示。该方法可直接迁移至纵向因果推断中的半参高效估计，与您的效率理论和纵向数据兴趣高度契合。
- **关键技术**: `partially linear mixed-effects model`, `plug-in estimation`, `semiparametric efficiency`, `machine learning adjustment`, `longitudinal data`, `parametric rate convergence`
- **为什么对您有用**: 本文直接相关于您的 primary interest 中的纵向因果推断（longitudinal data）及效率理论（semiparametric efficiency）。您非常熟悉的 nonparametric statistics 和 estimation theory in causal inference 足以理解其调整与推断框架，且该方法的 plug-in 思路与 DML 同源，可视为半参效率理论在重复测量场景的标准应用。**立即可做**：使用 very_familiar 的 nonparametric statistics 和 causal inference 工具即可读懂并评估其调整方法，进而考虑推广至带有反事实结果的纵向因果推断问题。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1111/sjos.12643](https://doi.org/10.1111/sjos.12643) · [arXiv](https://arxiv.org/abs/2302.14531) — Finite sample inference for empirical Bayesian methods
- **作者**: Hien Duy Nguyen, Mayetri Gupta
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1616-1640
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对经验贝叶斯（EB）推断中的置信集构建和假设检验问题提出一种通用方法。现有EB方法多集中于点估计，而推断工具缺乏普遍性且问题特定。作者基于Universal Inference框架，利用分层贝叶斯模型的holdout似然比构造有限样本有效的置信集和检验。该方法无需渐近近似，保证有限样本下的validity（覆盖率和第一类错误控制）。通过数值模拟和实际数据应用展示其实用性。该方法适用于高维参数化模型（如文中提及的复杂科学应用）。对研究者而言，该方法连接了假设检验这一主要兴趣方向，尤其提供了有限样本推断的通用框架。
- **关键技术**: `Empirical Bayes`, `Universal Inference`, `Holdout likelihood ratio`, `Finite sample inference`, `Confidence sets`, `Hypothesis tests`
- **为什么对您有用**: （1）该文紧扣假设检验（数学统计）这一主要兴趣方向，提供有限样本有效推断的通用方法，而非常见的渐近方法。 （2）研究者武器库中的‘非参数统计’和‘极小极大界’可用于评估该方法在更一般模型下的最优性；‘高阶U统计量’的树宽分解或许能协助处理该方法中的似然比计算复杂度。 （3）Follow-up粗判：中期可做——需要先在‘高阶U统计量’的树宽分解上有所积累，才能将该方法中似然比的计算与U统计量相联系；目前直接应用的障碍在于该方法针对参数模型，而研究者更关注半参数/非参数设定。

### 2. [10.1111/sjos.12654](https://doi.org/10.1111/sjos.12654) — Epistemic confidence in the observed confidence interval
- **作者**: Yudi Pawitan, Hangbin Lee, Youngjo Lee
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Karolinska Institutet · Seoul National University
- **分类**: vol 50 · issue 4 · pp 1859-1883
- 相关性 6/10 · novelty: `new_theory`
- **摘要**: 该文探讨频率学派置信区间的认识论（epistemic）解释问题。传统频率学派认为置信水平仅适用于程序（procedure），而不适用于已观测到的具体区间；本文试图为“观测到的置信区间”赋予认识论信心。作者将经典的荷兰赌（Dutch Book）论证从贝叶斯主观概率推广为更强的市场版荷兰赌，该版本防止外部代理利用未使用信息构造相关子集进行套利。前期工作已证明置信度是一种扩展似然（extended likelihood），而似然原理指出似然包含数据中所有信息，因此不再存在相关子集。直觉上，全似然关联的置信度受到荷兰赌保护，因而具有认识论意义。本文通过理论论证和实例验证这一直觉，为频率学派置信区间赋予认识论信心提供基础。该工作直接触及统计推断的基础问题，对于您的“数理统计与假设检验”兴趣方向有重要参考意义。
- **关键技术**: `Dutch Book argument`, `likelihood principle`, `extended likelihood`, `confidence distribution`, `frequentist inference`
- **为什么对您有用**: 该文直接关联您的首要兴趣“数理统计与假设检验”，因为置信区间与假设检验以对偶关系存在，理解区间估计的认识论基础能深化对检验逻辑的理解。武器库中非常熟悉的非参数统计和逆问题工具可用来探讨该框架在更一般设定（如非参数置信带）中的扩展性——这是一个中期可做方向：需先扎实掌握您的 moderately_familiar 区域的 semiparametric theory 中关于置信区间的渐近理论。本文适合作为 foundation reading，支撑后续对置信区间哲学与数学基础的研究。

### 3. [10.1111/sjos.12655](https://doi.org/10.1111/sjos.12655) — Regularized t$$ t $$ distribution: definition, properties, and applications
- **作者**: Zongliang Hu, Yiping Yang, Gaorong Li, Tiejun Tong
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Shenzhen University · Chongqing Technology and Business University · Beijing Normal University · Hong Kong Baptist University
- **分类**: vol 50 · issue 4 · pp 1884-1900
- 相关性 5/10 · novelty: `minor`
- **摘要**: 针对基因表达数据中差异表达基因检测的小样本方差估计问题，本文提出正则化t分布（regularized t distribution），推导其概率密度函数和矩母函数。进一步引入非中心正则化t分布以计算统计功效。应用上，利用正则化t分布构造正则化t检验（regularized t-test）用于差异表达基因筛选。模拟和实际数据表明，该检验在小样本情况下优于limma贝叶斯t检验。对您而言，本文属于假设检验方向的一个应用性工作，但方法本质是参数技巧，与您核心的理论方向关联弱。
- **关键技术**: `regularized t distribution`, `small-sample inference`, `differential expression analysis`, `statistical power`
- **为什么对您有用**: 本文与您主要兴趣中的‘假设检验’子方向有表面联系，但方法学创新有限，属于对小样本t检验的正则化改进，而非理论突破。技术武器库中的‘minimax bounds for estimation problems’本可用于验证其最坏情况性能，但本文未提供此类理论分析。对于该领域，您的武器库缺乏生物信息学实践经验，且方法本身较简单，因此暂不可做，不值得投入时间。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1111/sjos.12653](https://doi.org/10.1111/sjos.12653) · [arXiv](https://arxiv.org/abs/2112.12185) — Dimension‐independent Markov chain Monte Carlo on the sphere
- **作者**: Han Cheng Lie, Daniel Rudolf, Björn Sprungk, T. J. Sullivan
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Potsdam · University of Passau · TU Bergakademie Freiberg · Turing Institute · University of Warwick
- **分类**: vol 50 · issue 4 · pp 1818-1858
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对高维球面上的贝叶斯推断问题，提出了一类维数无关的马尔可夫链蒙特卡洛（MCMC）方法。研究设定基于角中心高斯先验（angular central Gaussian prior），该先验用于建模反演对称的方向数据，并出现在贝叶斯密度估计与二元水平集反问题中。核心方法是将采样问题提升到环境希尔伯特空间（ambient Hilbert space），利用线性空间中已有的维数无关采样器，再通过“推送-前向”马尔可夫核构造将链映射回球面。该方法继承了线性空间采样器的可逆性与谱间隙性质，从而保证了维数无关的混合效率。数值实验验证了算法在高维情况下仍能保持高效。对您可能有用的点是：该算法在计算上具有维数无关性，可应用于您统计计算方向中涉及高维球面先验的贝叶斯建模问题。
- **关键技术**: `dimension-independent MCMC`, `push-forward Markov kernel`, `angular central Gaussian prior`, `lifting to Hilbert space`, `spectral gap analysis`
- **为什么对您有用**: 该论文直接连接到您的统计计算（高维贝叶斯计算）兴趣子方向，且属于方法学创新，可视为高维采样算法的前沿资料。您武器库中的高维渐近分析（very_familiar）可用于检验其维数无关声明的理论紧性，而软件开发能力（very_familiar）则支持您快速实现并测试这类算法。但若要深入拓展其谱间隙理论或设计新混合策略，您当前武器库缺少MCMC谱间隙分析工具，故属于中期可做——需先在MCMC理论（如spectral gap、Hilbert空间提升）上建立基本熟悉度。

## 其他  *(other, 2 篇)*

### 1. [10.1111/sjos.12663](https://doi.org/10.1111/sjos.12663) · [arXiv](https://arxiv.org/abs/2201.09036) — Parameter estimation for linear parabolic SPDEs in two space dimensions based on high frequency data
- **作者**: Yozo Tonaki, Yusuke Kaino, Masayuki Uchida
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1568-1589
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究二维空间上线性抛物型随机偏微分方程（SPDE）的参数估计问题，基于时间和空间上的高频观测数据。模型中的随机驱动项由两种类型的Wiener过程刻画，微分算子的特征函数与特征值蕴含未知参数。作者首先利用空间方向上的稀疏化数据构造最小对比估计量，估计出现在特征函数中的参数；然后通过该估计量构建近似的坐标过程；最后基于时间方向上的稀疏化数据提出SPDE中系数参数的估计量。理论部分证明了估计量的渐近正态性，并通过数值模拟验证了有限样本表现。该方法属于高维随机过程统计算法，与因果推断、高维U-统计等主要兴趣方向缺乏直接交集。
- **关键技术**: `minimum contrast estimator`, `spectral decomposition of differential operator`, `approximate coordinate process`, `high frequency data in time and space`, `asymptotic normality for SPDE parameter estimation`
- **为什么对您有用**: 此文属于随机偏微分方程参数估计的方向，与研究者主要兴趣（因果推断、高维U-统计、半参数理论）无直接重叠。研究者武器库中的非参数统计与高维渐近理论虽可理解其技术框架，但缺乏SPDE模型背景和谱分析的具体工具，因此难以在近期内产生交叉。不建议作为重点阅读。

### 2. [10.1111/sjos.12641](https://doi.org/10.1111/sjos.12641) — A historical overview of textbook presentations of statistical science
- **作者**: Alan Agresti
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Florida
- **分类**: vol 50 · issue 4 · pp 1641-1666
- 相关性 1/10 · novelty: `survey`
- **摘要**: 本文是一篇统计教科书历史综述，覆盖1900-1970年间英语教材的演化。重点梳理了Yule、Fisher、Snedecor、Kendall、Wilks、Cramér等人的代表性著作，以及Bayes学派（Jeffreys、Savage）的后续影响。文章特别在纪念Cox的专辑中总结了他跨越多个主题的教科书贡献。结尾讨论了在数据科学时代统计基础教科书的未来走向。全文以学术史叙事为主，不含方法论新贡献。对您而言，作为统计学科研者，了解学科脉络和经典教材的演进有助于把握统计思想史，但与您的主要技术兴趣（因果推断、高维统计等）无直接对接。
- **关键技术**: `history of statistics`, `textbook evolution`, `R.A. Fisher`, `Jerzy Neyman`, `David Cox`, `Bayesian foundations`
- **为什么对您有用**: 本文属于统计学学科史综述，并不直接对接您的主要研究兴趣（因果推断、高维统计、非参理论等）。其价值在于提供学科发展背景，但无具体技术细节可迁移。从『暂不可做』判据看，缺乏与您武器库中任何工具的交集，因此仅作一般性阅读参考，不值得深读。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

