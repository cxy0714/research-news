# Scand. J. Stat. — Vol 50  Issue 4  ·  2026-05-21

- 共 17 篇 · Scandinavian Journal of Statistics

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1111/sjos.12662](https://doi.org/10.1111/sjos.12662) — Pitfalls of amateur regression: The Dutch New Herring controversies
- **作者**: Fengnan Gao, Richard D. Gill
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1901-1918
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文针对一位经济学家对荷兰新鲱鱼排名数据使用简单线性回归得出“排名被操纵”结论的事件，重新审视了该观测数据的因果推断假设。作者重构并修正了原数据集，指出原分析存在严重的模型设定错误（specification error）。原研究忽略了复杂的时空因素，在小样本下使用简单模型导致遗漏变量偏误，将统计伪影（artifact）误判为人为操纵的证据。本文强调，在观测数据中做因果声明时，对模型设定和遗漏变量的敏感性分析至关重要。主要结论是原经济学家的因果声明不可靠，简单回归无法捕捉多因素决定的味觉感知。本文虽无新方法学理论（属于应用案例批判），但直观展示了简单回归的脆弱性。对您有用：这是一个极佳的因果推断反面案例，展示了在经济数据应用中遗漏变量偏误的危害，对理解因果敏感性分析有直接启发。
- **关键技术**: `linear regression`, `specification error`, `omitted variable bias`, `observational data analysis`, `sensitivity to model assumptions`
- **为什么对您有用**: 作为因果推断与经济理论交叉的典型案例，本文直观展示了遗漏变量偏误与模型设定错误如何导致虚假的因果结论，对您在因果推断敏感性分析及经济数据应用中的方法论思考有警示与借鉴价值。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1111/sjos.12638](https://doi.org/10.1111/sjos.12638) — Robust inference for high‐dimensional single index models
- **作者**: Dongxiao Han, Miao Han, Jian Huang, Yuanyuan Lin
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1590-1615
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维单指标模型(SIM)设定下，假设协变量服从椭圆对称分布且联系函数未知，目标是实现信号恢复与参数推断。方法基于Huber损失构建Lasso估计器，巧妙避开了对未知联系函数的估计，并证明了估计器在相差一个标量因子下的ℓ1和ℓ2一致性。在协方差矩阵满足不可表示条件时，该方法可恢复真实参数的符号支持集。进一步，基于去偏Lasso(debiased Lasso)构造估计器，实现了对高维指标参数的逐分量与分组推断。理论上建立了渐近正态性以保证推断有效性，并在核黄素生产数据集上进行了实证验证。该工作将去偏推断与半参数单指标模型结合，对您研究高维半参数推断及去偏ML理论有直接参考价值。
- **关键技术**: `high-dimensional single index model`, `Huber loss`, `debiased Lasso`, `elliptically symmetric distribution`, `irrepresentable condition`
- **为什么对您有用**: 直接涉及您的高维统计与半参数理论兴趣：在半参数单指标模型下推导去偏Lasso的推断方法，为高维半参数效率界与去偏ML提供了具体的模型实例与理论工具。

## 非参数 / 半参数  *(nonparam_semipara, 6 篇)*

### 1. [10.1111/sjos.12659](https://doi.org/10.1111/sjos.12659) — A robust model averaging approach for partially linear models with responses missing at random
- **作者**: Zhongqi Liang, Qihua Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1933-1952
- 相关性 7/10 · novelty: `weaker_assumption`
- **摘要**: 在部分线性模型（partially linear model）且响应变量随机缺失（MAR）的设定下，本文提出基于加权 Mallows 型准则的稳健模型平均估计方法，目标是回归系数与非线性成分的联合估计。方法核心在于：对选择概率函数假定一个参数工作模型，通过 IPW 型加权构造 Mallows 准则来选取最优模型平均权重向量；稳健性体现在——只要真实选择概率是所设参数模型的某个可测函数（即允许工作模型误设），渐近最优性仍成立。理论上证明了该模型平均估计量达到渐近最小可能平方误差（asymptotic optimality），且权重向量估计收敛至最优权重。模拟与两个实际数据示例验证了方法表现。对您而言，该文在部分线性模型的半参数框架下放松了选择概率模型正确指定的假设，与您关注的 semiparametric efficiency 及 MAR/IPW 类因果推断中的 sensitivity to propensity model misspecification 直接相关。
- **关键技术**: `model averaging`, `weighted Mallows criterion`, `partially linear model`, `missing at random`, `IPW weighting`, `asymptotic optimality`
- **为什么对您有用**: 与您 primary interest 中的 semiparametric theory（部分线性模型）和 efficiency theory（渐近最优性）直接相关；其对选择概率模型误设的稳健性对 MAR/IPW 框架下的因果推断 sensitivity 分析有方法迁移价值。

### 2. [10.1111/sjos.12660](https://doi.org/10.1111/sjos.12660) — Deep neural network classifier for multidimensional functional data
- **作者**: Shuoyang Wang, Guanqun Cao, Zuofeng Shang, for the Alzheimer's Disease Neuroimaging Initiative
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1667-1686
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 本文针对多维非高斯函数型数据的分类问题，提出了函数型深度神经网络（FDNN）分类器，核心设定假设对数密度比具有局部连通的函数模结构。方法上，FDNN 先提取训练数据的函数主成分，再基于这些主成分训练 DNN 以预测类别标签，从而突破了传统函数判别分析仅限于一维高斯数据的局限。理论方面，文章在对数密度比满足局部连通函数模结构的条件下，严格证明了 FDNN 分类器达到了 minimax 最优收敛速率。实证部分通过模拟实验与 ADNI 阿尔茨海默病神经影像学数据集验证了方法的有效性。对您而言，本文的价值在于其非参数 DNN 分类器的 minimax 速率证明，该理论分析框架可为高维/函数型非参数假设检验或半参数效率界研究提供 DNN 逼近速率的推导借鉴。
- **关键技术**: `functional deep neural network`, `functional principal components`, `minimax optimality`, `locally connected functional modular structure`, `non-Gaussian functional classification`
- **为什么对您有用**: 本文涉及非参数理论中的 minimax 最优收敛速率证明，与您关注的非参数/半参数理论直接相关；其 DNN 逼近与收敛速率的分析技巧可迁移至高维非参数假设检验或效率界的研究中。

### 3. [10.1111/sjos.12661](https://doi.org/10.1111/sjos.12661) — Nonparametric adaptive estimation for interacting particle systems
- **作者**: Fabienne Comte, Valentine Genon‐Catalot
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1716-1755
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究具有常数扩散系数与空间线性漂移的交互粒子系统，目标是基于 $[0,T]$ 上的连续观测（固定粒子数 $N$、大 $T$）非参数估计漂移中的两个未知确定性函数。作者在 $L^2$ 的有限维子空间上构建投影估计量（sieve），分别在经验范数与确定性范数下分析其 $L^2$-风险。随后通过数据驱动的维度选择（模型选择）构造自适应估计量，并建立相应的风险界。理论给出了自适应估计的收敛率，模拟实验验证了方法的有限样本表现。对您有用：这是经典非参数自适应估计在相依数据上的拓展，其投影估计与模型选择技术可为您在非参数理论方向提供分析范本。
- **关键技术**: `projection estimator`, `sieve estimation`, `adaptive model selection`, `L2-risk`, `interacting particle systems`
- **为什么对您有用**: 直接关联您的非参数理论兴趣；展示了在相依数据（交互粒子系统）下如何通过投影与模型选择实现自适应非参数估计，其理论分析手法可迁移至其他复杂依赖结构。

### 4. [10.1111/sjos.12650](https://doi.org/10.1111/sjos.12650) — Time‐varying <i>β</i>‐model for dynamic directed networks
- **作者**: Yuqing Du, Lianqiang Qu, Ting Yan, Yuan Zhang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1687-1715
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文将静态有向网络的 β-模型扩展至动态网络设定，假设在离散时间点观测到邻接矩阵快照，目标是估计随时间变化的节点参数。作者提出了核平滑似然估计方法，利用局部时间窗内的网络快照进行非参数平滑。在渐近理论方面，证明了当节点数 n 或时间点 T 发散时，核平滑估计量均具有一致性与渐近正态性。该结论突破了单网络分析中必须要求 n→∞ 的经典限制。模拟研究与真实邮件网络数据验证了理论预测与方法表现。对您有用：该文的核平滑似然与 n/T 双索引渐近理论，可为非参数/半参数理论及纵向数据（longitudinal）中的时变参数估计提供方法论参考。
- **关键技术**: `kernel-smoothed likelihood`, `time-varying parameter estimation`, `beta-model`, `asymptotic normality`, `dynamic network`
- **为什么对您有用**: 核心是时变参数的非参数核平滑估计与双索引渐近理论，与您关注的非参数/半参数理论及纵向数据（longitudinal）设定有方法交叉，可借鉴其处理时间维度渐近性的技巧。

### 5. [10.1111/sjos.12652](https://doi.org/10.1111/sjos.12652) — Statistical inference with semiparametric nonignorable nonresponse models
- **作者**: Masatoshi Uehara, Danhyang Lee, Jae‐Kwang Kim
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1795-1817
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究非忽略缺失数据(nonignorable nonresponse)下的统计推断问题，在响应机制上采用半参数模型以放松传统参数假设，目标是总体参数在半参数缺失机制下的 identification 与有效估计。作者提出了两类估计器：profile maximum likelihood estimator 与 profile calibration estimator，前者通过轮廓似然消除无限维 nuisance parameter，后者利用校准约束构造估计方程。两者均基于半参数效率理论，推导了 efficient influence function，并证明了估计量达到半参数效率下界。理论上证明了估计量的 n^{-1/2}-CAN 性质与渐近正态性，模拟和韩国劳动收入面板调查(KLIPS)实证表明方法对模型误设具有鲁棒性。对您有用：该文将半参数效率界与 profile 估计理论应用于非忽略缺失（选择偏差）设定，直接契合您对 semiparametric efficiency bounds 与 causal inference (selection/missing) 的核心兴趣，且面板调查数据对经济理论应用有参考价值。
- **关键技术**: `semiparametric response model`, `profile maximum likelihood`, `profile calibration estimator`, `efficient influence function`, `nonignorable nonresponse`
- **为什么对您有用**: 直接推进了半参数效率理论在非忽略缺失（选择偏差）下的应用，契合您对 semiparametric efficiency bounds 和 causal inference (selection bias) 的核心兴趣；面板数据实证对经济理论应用有数据集参考价值。

### 6. [10.1111/sjos.12651](https://doi.org/10.1111/sjos.12651) — Adaptive estimation of intensity in a doubly stochastic Poisson process
- **作者**: Thomas Deschatre
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1756-1794
- 相关性 0/10 · novelty: `sharper_rate`
- **摘要**: 在双重随机 Poisson 过程（Cox 过程）框架下，强度过程 λ_t = f(Y_t) 由连续 Itô 半鞅 Y_t 驱动，两过程在 [0,T] 上连续观测，目标是估计函数 f。作者提出局部多项式估计量，并在非渐近框架下构造带宽选择方法，导出 oracle 不等式。在 T→∞ 渐近下，当多项式阶数充分大时，估计量在 Hölder(β) 类上的收敛速率为 T^{-β/(2β+1)}，达到 minimax 最优。该方法应用于法国气温与电力现货价格数据，推断电力价格尖峰强度关于温度的函数关系。对您有用：minimax 最优率与 oracle 不等式的非渐近分析直接契合您对非参数理论及效率的兴趣，电力现货价格应用也可作为经济理论 secondary interest 的数据集参考。
- **关键技术**: `local polynomial estimation`, `oracle inequality`, `minimax rate`, `Hölder class`, `doubly stochastic Poisson process`, `Itô semi-martingale`
- **为什么对您有用**: 非参数 minimax 最优率与 oracle 不等式直接对应您 primary interest 中的非参数理论与效率；电力现货价格数据集对经济理论 secondary interest 有参考价值。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1111/sjos.12639](https://doi.org/10.1111/sjos.12639) — Plug‐in machine learning for partially linear mixed‐effects models with repeated measurements
- **作者**: Corinne Emmenegger, Peter Bühlmann
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1553-1567
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在纵向重复测量的部分线性混合效应模型中，目标是在非参数/高维非线性项存在下推断线性固定效应。方法通过机器学习算法对线性变量和响应进行非参数调整（partialling out），消除非线性项影响，使调整后的变量满足标准线性混合效应模型，从而可用传统方法估计固定效应。理论证明该固定效应估计量具有 n^{-1/2} 参数收敛率、渐近正态性，并达到半参数有效界。模拟表明其覆盖率优于惩罚回归样条，并在 HIV 纵向数据及 R 包 dmlalg 中实现了算法。对您有用：将 orthogonal score / debiased ML 推广至 longitudinal mixed-effects 设定，直接契合您对半参数效率界与纵向因果推断的兴趣，且附带流行病学数据与计算工具。
- **关键技术**: `partially linear mixed-effects model`, `double machine learning`, `semiparametric efficiency bound`, `partialling out / orthogonalization`, `longitudinal data`, `n^{-1/2}-CAN`
- **为什么对您有用**: 将 orthogonal score / debiased ML 推广至 longitudinal mixed-effects 设定，直接契合您对半参数效率界与纵向因果推断的兴趣，且附带流行病学数据与 R 计算工具可复用。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1111/sjos.12655](https://doi.org/10.1111/sjos.12655) — Regularized t$$ t $$ distribution: definition, properties, and applications
- **作者**: Zongliang Hu, Yiping Yang, Gaorong Li, Tiejun Tong
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1884-1900
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 针对小样本基因表达数据中方差估计不稳定的问题，本文提出了一种正则化 t 分布并推导其统计性质。作者严格推导了该分布的概率密度函数与矩母函数，并定义了非中心正则化分布以计算检验功效。方法核心在于通过正则化手段修正方差估计，进而构建正则化 t 统计量的零分布，形成差异表达基因的正则化 t 检验。理论与数值结果表明，在小样本设定下，该检验的 I 类错误控制与功效优于 limma 包中的贝叶斯 t 检验。对您而言，该文虽属生物统计应用，但其对小样本 t 统计量零分布的参数化修正思路，可为假设检验（您的 primary interest）中的小样本推断提供一个特例参考，不过缺乏高维或半参数理论深度。
- **关键技术**: `regularized t-distribution`, `variance regularization`, `noncentral distribution`, `moment generating function`, `small-sample hypothesis testing`
- **为什么对您有用**: 论文核心是假设检验与零分布构造（对应您的 primary interest: hypothesis testing），但方法局限于小样本参数修正，对您关注的高维/半参数/效率理论无直接迁移价值，仅作小样本检验的边缘参考。

### 2. [10.1111/sjos.12654](https://doi.org/10.1111/sjos.12654) — Epistemic confidence in the observed confidence interval
- **作者**: Yudi Pawitan, Hangbin Lee, Youngjo Lee
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1859-1883
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文探讨观测置信区间的“认知置信度”（epistemic confidence），即能否将置信水平赋予已观测的具体区间而非仅赋予抽样程序。作者将经典贝叶斯主观概率的 Dutch Book 论证扩展为更强的市场版本，以防止外部代理利用“相关子集”（relevant subset）中的未用信息套利。基于其先前工作——置信度是一种扩展似然——结合似然原理（似然包含数据所有信息，故无相关子集），论证了基于全似然的置信度免受 Dutch Book 攻击。通过理论推导与实例验证了该直觉：与全似然关联的置信度具有认知性质。对您在假设检验与频率推断基础的理解有深化作用，特别是 relevant subset 与条件推断的关联，对效率理论中影响函数的条件推断有底层逻辑启发。
- **关键技术**: `epistemic confidence`, `Dutch Book argument`, `relevant subset`, `likelihood principle`, `extended likelihood`
- **为什么对您有用**: 直接关联您在 mathematical statistics (hypothesis testing) 方向的兴趣，深化对置信区间条件解释与 relevant subset 问题的理论理解，为频率学派推断的哲学基础提供新视角。

### 3. [10.1111/sjos.12643](https://doi.org/10.1111/sjos.12643) — Finite sample inference for empirical Bayesian methods
- **作者**: Hien Duy Nguyen, Mayetri Gupta
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1616-1640
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在经验贝叶斯（EB）框架下，针对参数模型构建有限样本有效的置信集与假设检验仍缺乏通用方法。受 Universal Inference 启发，本文提出基于 holdout likelihood ratio 的通用推断方法，利用贝叶斯模型的层级结构构造检验统计量。该方法通过样本分割确保似然比计算中训练集与测试集的独立性，从而在有限样本下严格保证第一类错误控制与置信区间的覆盖概率。虽然有限样本有效性通常以统计效力为代价，但避免了正则性条件失效的风险。数值实验与真实数据验证了该方法在复杂高维场景下的实用性。对您有用：直接关联您对假设检验的兴趣，Universal Inference 的有限样本有效性与其相对于渐近有效检验的效力权衡，是效率理论中的经典对比问题。
- **关键技术**: `empirical Bayes`, `Universal Inference`, `holdout likelihood ratio`, `finite sample validity`, `sample splitting`
- **为什么对您有用**: 直接关联您对假设检验的兴趣；Universal Inference 提供有限样本有效检验，但其与渐近有效/半参数有效检验之间的效力权衡是效率理论的核心问题，值得对比研究。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1111/sjos.12653](https://doi.org/10.1111/sjos.12653) — Dimension‐independent Markov chain Monte Carlo on the sphere
- **作者**: Han Cheng Lie, Daniel Rudolf, Björn Sprungk, T. J. Sullivan
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1818-1858
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究高维球面上的贝叶斯推断问题，采用 angular central Gaussian (ACG) 先验，该先验适用于对跖对称方向数据且可自然定义在 Hilbert 空间上。核心方法是将球面上的采样问题提升（lift）到环境 Hilbert 空间，利用已有的维度无关线性空间采样器（如 pCN），再通过 push-forward Markov 核构造将样本投影回球面。理论证明 push-forward 核继承了线性空间采样器的可逆性与谱间隙（spectral gap），从而获得维度无关的计算效率。数值实验验证了算法在高维设定下混合性能不随维度退化。对您在统计计算与高维推断交叉方向有参考价值，push-forward 构造思路可迁移至其他流形上的 MCMC 设计。
- **关键技术**: `angular central Gaussian prior`, `push-forward Markov kernel`, `preconditioned Crank-Nicolson (pCN) sampler`, `spectral gap preservation`, `Hilbert space MCMC`, `dimension-independent sampling`
- **为什么对您有用**: 直接关联您 primary interest 中的统计计算（数值方法与算法），push-forward 谱间隙继承的证明技巧对高维流形上 MCMC 理论分析有迁移价值；ACG 先验在非参数密度估计中的应用也触及 semiparametric/nonparametric theory。

## 其他  *(other, 4 篇)*

### 1. [10.1111/sjos.12664](https://doi.org/10.1111/sjos.12664) — Sparse principal component analysis for high‐dimensional stationary time series
- **作者**: Kou Fujimori, Yuichi Goto, Yan Liu, Masanobu Taniguchi
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1953-1983
- 相关性 6/10
- **摘要**: {
  "topic": "high_dim_rmt",
  "summary_zh": "本文研究高维平稳时间序列的稀疏主成分分析（SPCA），在维度远大于样本量的设定下，目标是对惩罚主成分估计量建立理论性质。针对包含重尾过程在内的一大类平稳时间序列，作者对惩罚主成分估计量推导了 oracle inequalities，并给出了其收敛速率。文章进一步阐明了调优参数选择的理论速率，确保了惩罚估计量的最优性。核心技术依赖于对高维时间序列依赖结构的控制以及稀疏惩罚项的谱范数界分析。主要理论结果为高维相依数据下的 SPCA 提供了非渐近的有限样本保证，数值模拟与气温数据应用验证了其实用性。对您有用：直接推进了您在"高维统计"方向对高维 PCA 估计量非渐近性质的理解，且时间序列依赖结构下的稀疏化处理对计量经济学等应用场景有迁移价值。",
  "key_techniques": [
    "sparse principal component analysis",
    "oracle inequality",
    "high-dimensional stationary process",
    "penalized estimation",
    "non-asymptotic convergence rate"
  ],
  "why_relevant": "直接对应您

### 2. [10.1111/sjos.12663](https://doi.org/10.1111/sjos.12663) — Parameter estimation for linear parabolic SPDEs in two space dimensions based on high frequency data
- **作者**: Yozo Tonaki, Yusuke Kaino, Masayuki Uchida
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1568-1589
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在二维空间线性抛物型随机偏微分方程(SPDE)设定下，本文研究基于时空高频观测数据的参数估计问题。方法采用两步策略：首先对空间维度数据进行稀疏化(thinning)，基于最小对比估计量(minimum contrast estimator)估计微分算子特征函数中的参数，并构造SPDE的近似坐标过程；随后对时间维度进行稀疏化，利用该近似坐标过程估计SPDE的系数参数。理论上推导了所提估计量的渐近性质，仿真实验验证了方法的有限样本表现。对您而言，本文的稀疏化与坐标过程近似技巧属于统计计算与无穷维推断的交叉，但与您核心的半参数效率、高维RMT或因果推断方向距离较远，仅作数值方法层面的边缘参考。
- **关键技术**: `minimum contrast estimator`, `stochastic partial differential equation (SPDE)`, `coordinate process approximation`, `spatial and temporal thinning`, `high-frequency data`
- **为什么对您有用**: 涉及统计计算中的数据稀疏化与近似推断技巧，但核心设定为SPDE参数估计，与您关注的半参数效率、高维RMT或因果推断重叠较小，仅作数值方法参考。

### 3. [10.1111/sjos.12658](https://doi.org/10.1111/sjos.12658) — Efficient t0$$ {t}_0 $$‐year risk regression using the logistic model
- **作者**: Torben Martinussen, Thomas Harder Scheike
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1919-1932
- 相关性 0/10
- **摘要**: ```json
{
  "topic": "efficiency_dml",
  "summary_zh": "在右删失生存数据下，目标是 t0-year risk（特定时间点前事件概率）的 logistic 回归参数估计，关键假设为 censoring 条件独立于协变量与生存时间。标准 IPWCC 和基于全数据 efficient influence function 构造的 AIPWCC 并非该观测数据模型下的最优估计。本文推导了该问题的 semiparametric efficient influence function，由此构造的 one-step estimator 达到了 semiparametric efficiency bound，其关键在于 nuisance tangent space 投影给出的修正项与全数据 EIF 的 augmentation 方向不同。结果从单一生存终点推广至 competing risks 设定，给出了 efficient influence function 的闭式表达。模拟与骨髓移植真实数据均显示所提估计量较 AIPWCC 有可观的方差缩减。对您有用：该工作清晰展示了"全数据 EIF 直接套用 ≠ 观测数据最优"这一效率理论中的微妙点，对您在 semiparametric efficiency bounds 与 IPW/AIPW 估

### 4. [10.1111/sjos.12641](https://doi.org/10.1111/sjos.12641) — A historical overview of textbook presentations of statistical science
- **作者**: Alan Agresti
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 4 · pp 1641-1666
- 相关性 0/10
- **摘要**: ```json
{
  "topic": "other",
  "summary_zh": "本文综述 1900–1970 年间英语统计学教材的演变，聚焦 Fisher 与 Neyman 的研究贡献如何重塑教材呈现方式。早期 Yule 的教材侧重描述统计，随后 Fisher 与 Snedecor 的方法型教材推动现代统计方法在科学实践中的普及；二战时期 Kendall、Wilks、Cramér 的教材则确立了以理论根基为核心的"数理统计"范式。Bayes 方法的教材化较晚，受 Jeffreys 与 Savage 著作影响；战后二十五年数理统计及各专题教材爆发式增长。文末讨论数据科学时代统计基础教材的未来，并纪念 David Cox 的教材贡献。本文为纯历史综述，无新方法或理论结果，但对理解假设检验、似然推断等核心概念的教材化脉络有参考价值。",
  "key_techniques": [
    "historical bibliometric analysis",
    "Fisher-Neyman paradigm shift",
    "Bayesian textbook evolution",
    "mathematical statistics foundations"
  ],
  "why_relevant": "与您 primary interest 中的


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

