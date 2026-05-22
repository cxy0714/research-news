# Scand. J. Stat. — Vol 53  Issue 1  ·  2026-05-21

- 共 20 篇 · Scandinavian Journal of Statistics

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1111/sjos.70035](https://doi.org/10.1111/sjos.70035) — Causal discovery in heavy‐tailed linear structural equation models via scalings
- **作者**: Mario Krali
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 291-334
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究重尾噪声下线性结构方程模型（SEM）的极值因果依赖结构，目标是在正则变差（regular variation）框架下实现因果图的结构发现（identification）。作者提出基于极值角测度（extremal angular measure）缩放参数的因果发现方法，将因果方向识别转化为极值指标的排序问题。算法层面结合了稳定性准则（stability）进行超参数选择，并在理论上建立了该因果发现算法的相合性（consistency）。模拟与河流流量数据应用表明该方法优于现有极值因果发现替代方案。对您而言，该文将因果图发现与极值理论结合，为重尾场景下的因果识别提供了非参数视角的新工具，直接补充了因果推断的识别理论与非参数理论交叉方向。
- **关键技术**: `causal discovery`, `linear structural equation models`, `regular variation`, `extremal angular measure`, `consistency proof`, `stability selection`
- **为什么对您有用**: 将因果图的结构发现从常见的高斯或有限矩设定拓展到重尾极值场景，结合正则变差与角测度等非参数工具，对您在因果推断的识别理论与非参数理论交叉方向有直接参考价值。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1111/sjos.70032](https://doi.org/10.1111/sjos.70032) — Variable selection via thresholding
- **作者**: Ka Long Keith Ho, Hien Duy Nguyen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 207-237
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在回归设定下，针对初始估计量无法将无关信号收缩至零的问题，本文研究通过阈值化剔除小系数的变量选择方法，目标是在温和正则条件下一致估计相关变量集。作者形式化分析了此类阈值化程序，提出一种简单的阈值选择方法，并基于此构建了稀疏估计量。该估计量具有 n^{-1/2}-相合性与渐近正态性，且其非零元素不承受收缩偏差。核心技术依赖于初始估计量的渐近展开与阈值收敛速率的精细匹配，以控制假阳性选择概率。理论证明了变量选择的一致性及去偏后的渐近正态性，数值实验验证了其有限样本表现。对您有用之处在于：该文从非稀疏初始估计量出发获得无偏 n^{-1/2}-CAN 估计量的后处理框架，其阈值去偏思想可为您在高维推断或假设检验中构建正交/去偏估计量提供参考。
- **关键技术**: `thresholding variable selection`, `sqrt(n)-consistent estimation`, `asymptotic normality`, `shrinkage bias correction`, `consistent model selection`
- **为什么对您有用**: 该文通过阈值化实现无收缩偏差的 n^{-1/2}-CAN 估计，其去偏与后处理思想与您关注的高维统计推断及 debiased ML 有方法论上的联系，可为构建正交得分或假设检验提供参考。

## 非参数 / 半参数  *(nonparam_semipara, 6 篇)*

### 1. [10.1111/sjos.70051](https://doi.org/10.1111/sjos.70051) — Shape‐restricted statistical inference for non‐ignorable missing data under a general additive model
- **作者**: Junjun Lang, Yukun Liu, Jing Qin
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 554-574
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在非可忽略缺失（MNAR）设定下，目标为总体均值 E[Y] 的识别与估计；假设缺失概率服从 logistic 模型，其中协变量效应为一般可加结构且各分量满足形状约束（单调递增/递减、凸/凹或其组合），并借助工具变量实现识别。作者提出无需调参的形状约束估计量（shape-restricted estimator），利用 IV 分离缺失机制对结果变量的依赖，同时通过形状约束避免非参数模型的过拟合与收敛率过慢问题。系统建立了估计量的一致性、收敛率与渐近正态性，其中收敛率依赖于各可加分量的形状约束类型及光滑度。模拟表明：当参数模型正确时该估计量与参数方法表现相当，模型误判时则显著优于参数方法。对您有用之处在于：将 IV 识别与半参数形状约束结合处理 MNAR 的思路，可迁移至 proximal CI 中 negative control 设定下的非参数识别问题，且渐近正态性的推导对您在 semiparametric efficiency 方面的研究有参考价值。
- **关键技术**: `shape-restricted estimation`, `instrumental variable identification`, `non-ignorable missing data`, `additive model with monotonicity/convexity`, `tuning-parameter-free estimation`, `asymptotic normality under shape constraints`
- **为什么对您有用**: 直接关联您 primary interest 中的因果推断 IV 方法与半参数理论：IV 用于 MNAR 识别的框架与 proximal CI 的 negative control 思路高度平行，形状约束下的渐近理论对 semiparametric efficiency bound 研究有方法论借鉴。

### 2. [10.1111/sjos.70048](https://doi.org/10.1111/sjos.70048) — Nonparametric simulation of multivariate extreme events via spectral bootstrap
- **作者**: Nisrine Madhar, Juliette Legrand, Maud Thomas
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 482-497
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文在多元极值理论（EVT）框架下，针对极端观测稀少导致推断困难的问题，基于多元广义 Pareto 分布的谱表示提出了一种非参数模拟方案（spectral bootstrap）。与标准 bootstrap 不同，该方法通过保留数据的联合尾部行为来生成合成极端数据，核心在于利用谱分解在非参数设定下重构并模拟尾部依赖结构。该方案在理论上保证了多元极端事件联合分布尾部性质的保真度，避免了传统重采样方法对尾部概率的低估。模拟与真实数据结果表明，该方法在估计尾部风险指标时有效提升了推断的稳定性与可靠性。对您而言，该文展示了非参数谱表示与 bootstrap 在极端值模拟中的计算实现，可为非参数理论及统计计算方向提供尾部依赖建模的参考。
- **关键技术**: `spectral bootstrap`, `multivariate generalized Pareto distribution`, `nonparametric simulation`, `tail dependence`, `extreme value theory`
- **为什么对您有用**: 涉及非参数理论与统计计算，其基于谱表示的 bootstrap 模拟机制可为多元非参数推断和计算方法提供尾部建模的新视角。

### 3. [10.1111/sjos.70006](https://doi.org/10.1111/sjos.70006) — On optimal linear prediction
- **作者**: Inge S. Helland
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 16-32
- 相关性 3/10 · novelty: `minor`
- **摘要**: 在线性预测设定下，本文研究基于模型降维的近最优预测方法，目标是最小化期望均方预测误差（EMSPE）。在特定假设下，最优模型降维对应于作者此前提出的偏最小二乘（PLS）回归统计模型；在进一步条件下，证明了 PLS 型预测量相对于其他预测量具有优良性质。文章还将两种不同模型降维的情形嵌入量子力学框架，试图用量子基础概念重新诠释预测问题。整体是数学统计、化学计量学算法与量子基础三者的综合。对您而言，PLS 在高维共线性预测中的最优性分析可作参考，但与您关注的 RMT 或 semiparametric efficiency 方向距离较远。
- **关键技术**: `partial least squares regression`, `model reduction`, `expected mean squared prediction error`, `linear prediction optimality`, `quantum mechanical analogy`
- **为什么对您有用**: 与您的高维统计兴趣有弱关联（高维共线性下的模型降维预测），但核心是 PLS 最优性而非 RMT 或 efficiency bound 理论，量子力学视角更偏概念类比，方法学迁移价值有限。

### 4. [10.1111/sjos.70045](https://doi.org/10.1111/sjos.70045) — Adaptive blind image deblurring and denoising
- **作者**: Yicheng Kang, Anik Roy, Partha Sarathi Mukherjee
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 413-441
- 相关性 1/10 · novelty: `weaker_assumption`
- **摘要**: 在空间变模糊（spatially varying blur）与噪声叠加的设定下，本文研究盲图像去模糊与去噪问题，放松了传统方法中模糊核位置不变的假设。方法核心在于自适应检测模糊像素：通过优化检测功效（detection power）选择最优邻域大小，并利用尽可能多的清晰像素进行去模糊与去噪。理论上，本文证明了随着图像分辨率提升，图像估计量具有一致性，弥补了多数现有去模糊方法缺乏渐近性质的不足。数值模拟与真实数据均显示其优于现有方法。对您而言，虽然应用场景为图像处理，但其“优化检测功效选择邻域”的思路对非参数理论中的自适应窗宽选择及假设检验功效分析有一定参考价值。
- **关键技术**: `adaptive neighborhood selection`, `detection power optimization`, `spatially varying blur`, `nonparametric consistency`, `blind deconvolution`
- **为什么对您有用**: 涉及非参数理论（一致性证明）与假设检验（优化检测功效），其自适应邻域选择的思路对非参数估计与检验的局部自适应方法有参考价值，但与核心因果/高维/效率理论距离较远。

### 5. [10.1111/sjos.70027](https://doi.org/10.1111/sjos.70027) — Semiparametric regression for circular response with application in ecology
- **作者**: Jose Ameijeiras‐Alonso, Irène Gijbels
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 54-101
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在圆形响应变量（角度数据）的回归设定下，本文假设条件密度属于允许非对称和变峰度的参数族，而模态方向与集中度非参数地依赖于协变量。方法上，采用带核权重的局部多项式拟合来估计条件模态方向和集中度。理论方面，建立了这两个估计量的渐近正态性，并基于此推导了最优平滑参数的表达式及数据驱动选择器。实证部分将模型应用于生态学中候鸟迁徙方向对飞行高度和风向的回归。尽管应用领域非您关注，但其局部多项式在半参数圆形回归中的渐近正态性推导，对您在 nonparametric theory 方面的理论工具箱有一定参考价值。
- **关键技术**: `circular regression`, `local polynomial fitting`, `kernel smoothing`, `asymptotic normality`, `semiparametric density model`
- **为什么对您有用**: 涉及您 primary interest 中的 semiparametric & nonparametric theory（局部多项式与核平滑的渐近正态性推导），但应用领域（生态学）和圆形数据设定与您其他关注点重叠较少，主要提供非参数推断的理论参考。

### 6. [10.1111/sjos.70025](https://doi.org/10.1111/sjos.70025) — Data integration with nonprobability sample: Semiparametric model‐assisted approach
- **作者**: Danhyang Lee, Sixia Chen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 33-53
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究概率与非概率样本的数据整合，目标是在非概率样本存在不可忽略选择偏差下估计有限总体参数。为放宽缺失随机（MAR）假设，作者提出灵活的半参数倾向得分模型，并采用伪剖面似然（pseudo-profile-likelihood）法进行估计。随后以概率样本为基准构建差分估计量，利用非概率样本中基于估计倾向得分得到的代理值进行修正。理论上推导了估计量的渐近性质与方差估计公式，证明了其稳健性与效率。该工作将半参数倾向得分与伪似然结合处理不可忽略缺失，对您在因果推断中选择偏差处理及半参数理论推导有直接参考价值。
- **关键技术**: `semiparametric propensity score`, `pseudo-profile-likelihood`, `model-assisted difference estimator`, `nonignorable selection bias`, `data integration`
- **为什么对您有用**: 直接关联您的 primary interest 中的半参数理论与因果推断中的选择偏差处理；其半参数倾向得分加伪似然的设定对处理不可忽略缺失的半参数效率与推断具有方法迁移价值。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1111/sjos.70043](https://doi.org/10.1111/sjos.70043) — Efficient multiple‐robust estimation for nonresponse data under informative sampling
- **作者**: Kosuke Morikawa, Kenji Beppu, Wataru Aida
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 395-412
- 相关性 10/10 · novelty: `new_theory`
- **摘要**: 在 informative sampling 与 nonresponse 的调查抽样设定下，本文将抽样权重视为随机变量，研究目标参数的识别与估计。作者推导了该框架下的 semiparametric efficiency bound，并构造了具有 double robustness 的有效估计量。为缓解模型误设风险，提出两步经验似然（two-step empirical likelihood）方法，将双重稳健性扩展至多重稳健性（multiple robustness），确保在多个工作模型中至少一个正确时估计量仍一致。理论证明所提估计量达到半参数有效界，模拟与 NHANES 流行病学数据整合应用验证了其有限样本表现。对您有用：本文展示了 informative sampling 下 semiparametric efficiency bound 的推导及 empirical likelihood 实现多重稳健的技巧，可迁移至因果推断中处理选择偏差的半参数效率理论。
- **关键技术**: `semiparametric efficiency bound`, `multiple robustness`, `two-step empirical likelihood`, `informative sampling`, `double robustness`
- **为什么对您有用**: 直接推导了 informative sampling 下的 semiparametric efficiency bound，并通过 empirical likelihood 实现多重稳健，与您关注的效率理论及因果推断中的选择偏差/稳健估计高度契合；同时 NHANES 数据集对流行病学应用有参考价值。

## 数理统计 / 假设检验  *(hypothesis_testing, 4 篇)*

### 1. [10.1111/sjos.70050](https://doi.org/10.1111/sjos.70050) — ATM: An aggregation test of moments approach for assessing high‐dimensional normality
- **作者**: Hengjian Cui, Lingyue Zhang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 532-553
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文研究高维数据的正态性检验问题，目标是在避免使用协方差矩阵逆的条件下，构造对高维高斯分布族具有仿射不变性的检验方法。作者引入了共三阶矩(co-third moment)和共四阶矩(co-fourth moment)两个新指标来刻画高维分布形状偏离高斯性的程度，并基于此提出两个渐近正态的检验统计量。通过聚合这两个统计量并结合power enhancement技术，本文构建了更为敏感的ATM检验。理论分析在温和的正则条件下给出了统计量的渐近性质，成功规避了高维情形下估计逆协方差矩阵的难题。数值研究与实际数据分析表明，ATM检验在有效控制第一类错误的同时具备竞争力的检验功效。对您有用：本文直接推进了高维假设检验与数学统计的理论，其绕开高维协方差逆的矩聚合方法与power enhancement技巧，对您关注的高维推断与假设检验研究具有直接的构造性借鉴意义。
- **关键技术**: `high-dimensional normality test`, `co-third moment`, `co-fourth moment`, `power enhancement technique`, `affine invariant test`
- **为什么对您有用**: 直接对应您在数学统计（假设检验）与高维统计方面的核心兴趣；其绕开协方差逆的矩聚合方法与power enhancement技术，对高维假设检验的统计量构造具有直接借鉴意义。

### 2. [10.1111/sjos.70046](https://doi.org/10.1111/sjos.70046) — Fixed effects Bayesian testing in high‐dimensional linear mixed models
- **作者**: Jiamin Liu, Xingwei Liu, Heng Lian, Wangli Xu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 442-481
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在高维线性混合模型（LMM）设定下，本文研究固定效应的群组显著性检验问题，传统固定维度频率派方法在此失效。作者提出一种贝叶斯动机的检验统计量，其构造基于独立但非同分布随机变量的两个二次型之比。零分布通过二次型的正态近似进行推导，并创新性地引入一步迭代法来确定检验临界值，避免了繁重的模拟负担。在温和正则条件下，推导了局部替代假设下的功效函数，从理论上刻画了检验的灵敏度。对您有用：该工作将高维假设检验与二次型渐近理论结合，直接契合您在“高维统计”与“假设检验”的交叉兴趣，其一步迭代临界值算法对“统计计算”方向亦有参考价值。
- **关键技术**: `high-dimensional linear mixed models`, `Bayesian-motivated testing`, `quadratic form ratio`, `normality approximation`, `one-step iteration for critical value`, `local alternative power analysis`
- **为什么对您有用**: 直接契合您在“高维统计”与“假设检验”的交叉兴趣；二次型正态近似与一步迭代临界值算法对您在“数学统计”与“统计计算”方向的研究有直接迁移价值。

### 3. [10.1111/sjos.70049](https://doi.org/10.1111/sjos.70049) — Kernel‐based marginal testing for covariate effects in high‐dimensional settings
- **作者**: Hong Yin, Yijun Wang, Ancha Xu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 498-531
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在高维设定下，本文研究协变量对响应变量的边际效应检验问题，目标是在无参数模型假设下检验基于核的条件均值依赖性（kernel-based conditional mean dependence）。提出一种边际检验统计量，通过渐近逼近一类二次型（quadratic form），分别在零假设和局部替代假设下建立统计量的极限正态分布。从线性模型框架和全非参数设定两个角度，系统考察了所提检验相对于现有方法的渐近相对效率（ARE）。理论结果表明，该方法在较弱的矩条件和维数要求下仍保持检验一致性，且在非参数设定下对局部替代具有非平凡的检验势。模拟和实际数据分析验证了方法的有效性。对您而言，该文将高维假设检验与非参数核方法结合，二次型逼近与 ARE 分析的技巧可直接迁移至您关注的高维假设检验与非参数效率理论研究。
- **关键技术**: `kernel-based conditional mean dependence`, `quadratic form approximation`, `asymptotic relative efficiency`, `marginal testing`, `high-dimensional limiting distribution`, `local alternative power analysis`
- **为什么对您有用**: 直接涉及高维假设检验与非参数理论两个 primary interest，其二次型逼近技巧和 ARE 分析框架可为您在高维非参数/半参数检验的效率理论研究提供方法借鉴与对比基准。

### 4. [10.1111/sjos.70029](https://doi.org/10.1111/sjos.70029) — On goodness‐of‐fit testing for self‐exciting point processes
- **作者**: José Carlos Fontanesi Kling, Mathias Vetter
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 102-139
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究自激点过程（如 Hawkes 过程）参数模型的拟合优度检验问题，目标是在给定参数模型下检验观测数据是否服从该自激过程。作者提出一种基于 bootstrap 的拟合优度检验统计量，经验上适用于各类自激点过程甚至更广的相依结构。在 infill-asymptotic 设定下，文章证明了该检验的渐近一致性，但理论保证目前仅限于底层过程为非齐次 Poisson 过程的特例。该工作填补了自激点过程缺乏通用 GoF 检验的空白，尽管理论完备性受限于 Poisson 假设。对您有用：本文直接对应您 primary interest 中的假设检验方向，其 bootstrap 检验构造与 infill 渐近分析思路可迁移至其他复杂相依数据的假设检验问题。
- **关键技术**: `goodness-of-fit test`, `self-exciting point process`, `bootstrap test`, `infill asymptotics`, `asymptotic consistency`
- **为什么对您有用**: 直接对应您 primary interest 中的数学统计（假设检验）方向；其 bootstrap 检验构造与 infill 渐近分析为点过程假设检验提供了新思路，尽管理论一致性目前仅在 Poisson 假设下成立。

## 统计计算 / 算法  *(stat_computing, 4 篇)*

### 1. [10.1111/sjos.70052](https://doi.org/10.1111/sjos.70052) — Optimal subsampling for estimation of dimension reduction directions
- **作者**: Xinru Jia, Weixuan Yuan, Xingqiu Zhao, Xuehu Zhu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 575-611
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在充分降维（SDR）框架下，针对大规模数据中迭代型 SDR 方法的计算瓶颈，本文发展了基于逆概率加权（IPW）的最优子抽样策略，目标是最小化估计量渐近方差-协方差矩阵的迹。具体考虑两类代表性方法：基于条件密度的改进外积梯度法（rdOPG）与基于条件密度的最小平均方差估计（dMAVE），推导出显式最优子抽样概率形式，并建立了所得估计量的一致性与渐近正态性。核心机制在于通过 IPW 权重修正子抽样偏差，同时在计算效率与统计精度之间取得最优权衡；渐近理论表明子抽样估计量达到与全样本估计量相同的渐近结构，仅方差放大一个可控因子。模拟与实证表明，相比均匀子抽样，最优子抽样在大幅降低计算量的同时提升了估计精度。对您有用之处：该文将效率理论（渐近方差最小化）与统计计算（最优子抽样）结合于半参数降维问题，思路可迁移至您关注的高维因果推断中大规模数据的计算加速场景。
- **关键技术**: `optimal subsampling`, `inverse probability weighting`, `sufficient dimension reduction`, `rdOPG`, `dMAVE`, `asymptotic variance minimization`
- **为什么对您有用**: 将效率理论（渐近方差矩阵迹最小化）与统计计算（最优子抽样）统一于半参数降维框架，对您在效率理论和统计计算两个 primary interest 的交叉研究有直接借鉴价值；IPW 权重修正与渐近正态性的推导模式也可迁移至高维因果推断的大规模计算场景。

### 2. [10.1111/sjos.70042](https://doi.org/10.1111/sjos.70042) — A standardization procedure to incorporate variance partitioning‐based priors in latent Gaussian models
- **作者**: Luisa Ferrari, Massimo Ventrucci
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 364-394
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在潜高斯模型(LGM)框架下，针对方差参数先验设定缺乏直观解释性的问题，本文旨在通过方差分解(VP)为同时包含固定效应和随机效应的LGM构建可解释先验。现有基于VP的先验通常将固定效应与随机效应分开处理，本文提出一种标准化程序，将模型参数转化为反映各效应对总方差相对贡献的比例参数，从而将VP先验的适用性扩展到更广泛的LGM类。该标准化技巧使得实践者能够直接在方差贡献尺度上指定先验，而不必处理难以解释的原始方差参数。方法层面保证了标准化后模型仍保持LGM的计算优势（如INLA的高效近似推断），实证部分通过模拟和生存分析数据集展示了先验设定的直观性与推断的准确性。对您而言，若在统计计算中涉及贝叶斯层次模型的先验构建，此标准化技巧可作参考，但与您核心的频率派半参数效率或因果推断方向关联较弱。
- **关键技术**: `latent Gaussian models`, `variance partitioning priors`, `Bayesian hierarchical models`, `prior elicitation`, `standardization procedure`
- **为什么对您有用**: 本文主要关注贝叶斯层次模型的先验设定与计算，与您核心的频率派效率理论、因果推断或高维统计关联较弱，仅在统计计算（层次模型先验标准化技巧）方面有边缘的方法论参考价值。

### 3. [10.1111/sjos.70036](https://doi.org/10.1111/sjos.70036) — Estimating Monte Carlo variance from multiple Markov chains
- **作者**: Kushagra Gupta, Dootika Vats
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 335-363
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多链并行 MCMC 设定下，目标是估计 Monte Carlo 平均的协方差矩阵；现有单链 batch means (BM) 估计量的简单多链平均在小样本下严重低估方差，尤其对慢混合链。作者提出 multivariate replicated batch means (RBM) 估计量，利用并行链间信息修正低估问题。在弱混合条件下证明 RBM 强一致，且大样本偏差与方差与 BM 估计量相当。关键理论结果：在 MCMC 正相关存在时，RBM 估计量的负偏差严格小于平均 BM 估计量，因此小运行次数下 RBM 显著优于简单平均。对您在统计计算方向（MCMC 诊断与方差估计的数值方法）有直接参考价值，理论分析手法（偏差界、强一致性）也可迁移至其他序列估计问题。
- **关键技术**: `replicated batch means`, `batch means variance estimation`, `parallel Markov chains`, `strong consistency under weak mixing`, `bias comparison for correlated chains`
- **为什么对您有用**: 直接对应您 primary interest 中的统计计算（数值方法与算法）；RBM 的偏差界分析与强一致性证明手法可迁移至其他序列/并行估计场景，对 MCMC 实际计算中的方差诊断有实用价值。

### 4. [10.1111/sjos.70031](https://doi.org/10.1111/sjos.70031) — Recursive Bayesian prediction of remaining useful life for gamma degradation process under conjugate priors
- **作者**: Ancha Xu, Weiwei Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 175-206
- 相关性 0/10 · novelty: `minor`
- **摘要**: 在齐次 Gamma 退化过程模型下，本文推导了参数的共轭先验分布，解决了 Gamma 过程似然函数参数结构复杂导致贝叶斯推断困难的问题。为进行后验采样，作者设计了三种算法（Gibbs sampling、discrete grid sampling、sampling importance resampling），模拟显示其计算效率与估计精度均较高。进一步将共轭先验推广至含异质效应的 Gamma 过程，在等间距观测时间点下实现了后验分布的递归更新，并据此提出在线预测多系统剩余寿命（RUL）的算法。该方法在两个真实数据集和高频监测模拟场景中验证了有效性。对您而言，该文在统计计算层面的 novelty 有限（Gibbs/grid/SIR 均为成熟工具），递归后验更新的思路或可参考，但与您关注的矩阵/张量数值方法和高维推断计算关联较弱。
- **关键技术**: `conjugate prior derivation`, `Gibbs sampling`, `discrete grid sampling`, `sampling importance resampling`, `recursive posterior update`, `remaining useful life prediction`
- **为什么对您有用**: 与您 primary interest 中的 statistical computing 有微弱关联（递归后验更新算法），但核心场景为可靠性退化建模，所用计算工具为成熟 MCMC/SIR 方法，对您关注的矩阵/张量数值方法或高维推断计算无直接迁移价值。

## 其他  *(other, 3 篇)*

### 1. [10.1111/sjos.70034](https://doi.org/10.1111/sjos.70034) — Assessing estimation uncertainty under model misspecification
- **作者**: Rong Li, Yichen Qin, Yang Li
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 268-290
- 相关性 0/10
- **摘要**: ```json
{
  "topic": "stat_computing",
  "summary_zh": "在广义线性模型(GLM)可能被误设的设定下，目标是准确评估估计量的不确定性并完成有效推断；经典 bootstrap 与渐近理论因依赖模型假设而在此场景下失效。本文提出局部残差 bootstrap(local residual bootstrap)：从近邻观测的残差中重抽样以近似目标统计量的抽样分布，绕过对 score equation 的依赖，直接重建响应变量。理论上，利用 surrogate residuals 建立了 bootstrap validity 的严格证明；在模型正确设定时退化为经典 bootstrap，在误设下提供更准确的不确定性量化。方法可一站式完成标准误估计、置信区间、假设检验及模型选择。对您而言，该工作在统计计算（新 bootstrap 算法）与假设检验（误设下有效推断）交叉处提供了新工具，且"误设下仍有效"的思路与半参数效率理论中不依赖 nuisance model 正确设定的 robust inference 理念相通。",
  "key_techniques": [
    "local residual bootstrap",
    "surrogate residuals",
    "GLM misspecification",

### 2. [10.1111/sjos.70030](https://doi.org/10.1111/sjos.70030) — Multivariate representations of univariate marked Hawkes processes
- **作者**: Louis Davis, Conor Kresin, Boris Baeumer, Ting Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 140-174
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在点过程建模框架下，本文建立了单变量标记 Hawkes 过程与多变量无标记 Hawkes 过程之间的基本联系，目标是在可识别性条件下对标记过程进行参数化与渐近逼近。作者提出用多变量无标记 Hawkes 表示作为参数化工具，证明了该表示能渐近逼近一大类单变量标记 Hawkes 过程，且在原过程平稳时保持平稳性。理论结果表明，所得条件强度参数是可识别且可解释的，模拟研究给出了多变量参数空间引入误差的启发式界。实证部分将该方法应用于南加州地震目录数据。该文对您在数学统计中对随机过程渐近表示与可识别性的兴趣有理论参考价值，地震目录应用也可作为统计计算与时空点过程建模的入门数据集。
- **关键技术**: `marked Hawkes process`, `multivariate representation`, `asymptotic approximation`, `identifiability`, `conditional intensity`
- **为什么对您有用**: 虽非核心因果或高维推断，但其对随机过程渐近表示与参数可识别性的理论推导对数学统计兴趣有参考价值；地震目录应用可作为统计计算与时空点过程建模的入门数据集。

### 3. [10.1111/sjos.70033](https://doi.org/10.1111/sjos.70033) — Estimation of generalized tail distortion risk measures with applications in reinsurance
- **作者**: Roba Bairakdar, Frédéric Godin, Mélina Mailhot, Fan Yang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 238-267
- 相关性 0/10 · novelty: `minor`
- **摘要**: 本文在极值风险设定下，研究广义尾部失真(GTD)风险度量的估计问题，关键假设为分布的厚尾性质。所提估计量基于GTD风险度量的一阶渐近展开构建，形式简单且易于实施。模拟实验表明，该估计量的表现与现有方法相当或更优。作者进一步基于GTD风险度量提出了一种再保险保费原则，并在车险理赔数据上进行了应用，通过嵌入安全附加来抵御统计不确定性。该研究属于精算与极值统计交叉领域，对您关注的因果推断、半参数效率或高维统计等核心方向的直接参考价值较低。
- **关键技术**: `first-order asymptotic expansion`, `generalized tail distortion risk measure`, `extreme value theory`, `safety loading`
- **为什么对您有用**: 属于精算与极值统计领域，与您关注的因果推断、高维/效率理论等核心方向重叠极低，仅在一阶渐近展开的数学技巧上有微弱关联，直接参考价值有限。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

