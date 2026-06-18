# Scand. J. Stat. — Vol 53  Issue 1  ·  2026-06-19

- 共 20 篇 · Scandinavian Journal of Statistics
- 目录核对 ✅ 20 篇全部抓到（对照 OpenAlex 27 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期论文大致聚成四条主线：一是高维与复杂模型下的假设检验，涉及固定效应分组检验、协变量边际效应核检验、高维正态性矩聚合检验及自激点过程拟合优度检验，外加基于阈值化的变量选择新路径；二是半参数/非参数估计与模型误设鲁棒性，覆盖非响应数据的多重鲁棒经验似然、非可忽略缺失的形状约束IV估计、非概率样本整合的半参数倾向得分校正、圆形响应的局部多项式回归，以及GLM误设下的残差Bootstrap；三是统计计算与大规模数据算法，聚焦多链MCMC方差估计的跨链修正、充分降维的最优子抽样IPW策略、Gamma退化过程的递归贝叶斯预测与偏最小二乘(PLS)预测的最优性理论；四是极值与点过程建模，包括重尾线性SEM的极值因果发现、多元极值的谱Bootstrap、标记Hawkes过程的多元表示，以及盲图像去模糊的渐近一致性。

高维假设检验与变量选择主线在本期推进了多种无显式模型依赖或规避重采样开销的检验构造。针对线性混合模型固定效应，二次型比值统计量配合一步迭代法绕开了Bootstrap计算；针对协变量条件均值效应，核检验统计量被近似为二次型以获取渐近正态分布；针对高维正态性，基于协三阶/协四阶矩的高阶U统计量聚合检验规避了协方差矩阵求逆；而阈值化变量选择则通过控制错误发现率渐近为零，提供了免惩罚项的√n一致无偏估计替代路径。这几篇均以二次型逼近或矩条件为核心数学工具，试图在高维设定下兼顾计算便捷与理论可解释性。

半参数效率与选择偏差校正主线集中处理了不同缺失/选择机制下的鲁棒识别与估计。非响应数据估计在推导半参数效率界后，用两步经验似然将双重鲁棒性扩展为多重鲁棒性；非可忽略缺失数据在IV识别下，对logistic可加缺失概率施加单调/凸凹形状约束以实现免调参估计；非概率样本整合则通过pseudo-profile-likelihood估计半参数倾向得分，构造difference estimator实现n^{-1/2}-CAN推断。三者均试图超越标准MAR假设与参数模型限制，在半参数框架内通过不同工具（经验似然、形状约束、倾向得分校正）增强对选择偏差与模型误设的鲁棒性。

对于关注因果推断与半参数效率的研究者，【efficiency_dml】的多重鲁棒经验似然、【nonparam_semipara】中非可忽略缺失的形状约束IV估计与非概率样本的半参数倾向得分校正这三篇最贴合选择偏差与半参数识别的讨论，适合优先看；对于关注高维统计与假设检验的研究者，【hypothesis_testing】中的高维固定效应二次型检验、协变量边际核检验与阈值化变量选择提供了高维下规避逆矩阵与重采样的不同切法，建议优先跟进。

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1111/sjos.70035](https://doi.org/10.1111/sjos.70035) · [arXiv](https://arxiv.org/abs/2502.13762) — Causal discovery in heavy‐tailed linear structural equation models via scalings
- **作者**: Mario Krali
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 291-334
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究重尾线性结构方程模型（heavy-tailed linear SEM）中的因果发现，目标是在噪声变量服从正则变化（regular variation）的框架下，从极端观测中识别因果方向。方法核心是基于极值角度测度（extremal angular measure）的缩放参数（scaling parameters）来推断变量间的因果顺序，并实现为一个算法。作者证明了所提估计量的一致性，并利用稳定性概念提出超参数选择程序。模拟实验和真实河流数据集上的应用表明，该方法在与现有唯一极值因果发现方法的比较中具有竞争性能。该工作为因果推断中的极端事件建模提供了新工具，特别适用于罕见事件（如洪水）的因果分析。对您而言，本文属于因果推断的扩展方向，但核心工具（正则变化、极值理论）不在您当前武器库中，需要额外学习才能跟进。
- **关键技术**: `regular variation`, `extremal angular measure`, `linear structural equation model`, `scaling parameters`, `causal discovery`, `stability selection`
- **为什么对您有用**: 本文直接关联您的因果推断兴趣，特别是因果发现子领域，并专注于极端值场景，这是您当前未覆盖的方向。您的非参数统计和因果估计理论知识可用于评估该方法的非参数极值估计部分，但极值理论核心（正则变化、角度测度）需要专门学习。中期可做：需先熟悉极值统计基础（如正则变化、多元极值模型）才能复现或扩展本方法。

## 非参数 / 半参数  *(nonparam_semipara, 7 篇)*

### 1. [10.1111/sjos.70034](https://doi.org/10.1111/sjos.70034) · [arXiv](https://arxiv.org/abs/2312.11393) — Assessing estimation uncertainty under model misspecification
- **作者**: Rong Li, Yichen Qin, Yang Li
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 268-290
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在广义线性模型（GLM）可能存在模型误设的设定下，目标是准确评估估计量的抽样分布与不确定性，而不依赖经典 score equation 的正确性。本文提出 local residual bootstrap 方法，通过从邻域观测的重构残差（surrogate residuals）进行重抽样，直接生成新的响应变量以逼近目标统计量的分布。该方法在模型正确设定时与经典 bootstrap 表现一致，而在误设下仍能提供准确的 uncertainty 评估，可用于标准误估计、置信区间构建与假设检验。理论部分利用 surrogate residuals 建立了 bootstrap validity 的渐近性质。对您可能有用：该工作为 M-estimation 在误设下的 inference 提供了新视角，与您关注的 semiparametric theory 及 M-estimation theory 直接相关。
- **关键技术**: `local residual bootstrap`, `surrogate residuals`, `model misspecification inference`, `generalized linear models`, `bootstrap validity`
- **为什么对您有用**: 本文直接连接到您 primary interest 中的 semiparametric & nonparametric theory，以及 technical_arsenal 中 moderately_familiar 的 M-estimation theory——它处理的是 M-estimator 在模型误设下的 inference 问题，这是 semiparametric 效率理论之外的重要补充视角。您可以用 very_familiar 的 minimax bounds 视角审视其声称的准确性是否在更广的非参空间下成立，或用 moderately_familiar 的 M-estimation 理论推导其 influence function 以验证 bootstrap validity 的条件。**中期可做**：需先在 moderately_familiar 的 M-estimation theory 上长肌肉，深入理解误设下 M-estimator 的渐近展开，才能严格评估该方法与 sandwich variance / one-step correction 的优劣。

### 2. [10.1111/sjos.70051](https://doi.org/10.1111/sjos.70051) — Shape‐restricted statistical inference for non‐ignorable missing data under a general additive model
- **作者**: Junjun Lang, Yukun Liu, Jing Qin
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: East China Normal University · National Institute of Allergy and Infectious Diseases
- **分类**: vol 53 · issue 1 · pp 554-574
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在非可忽略缺失数据（non-ignorable missing）设定下，目标是在一般可加模型与形状约束下估计总体结局均值，并借助工具变量实现 identification。作者对缺失概率采用 logistic 可加模型，每个可加成分施加单调或凸/凹等形状约束，提出无需调参的形状约束估计量。理论层面系统建立了估计量的相合性、收敛速率与渐近正态性；数值实验表明在参数模型正确时该估计量与参数方法表现相当，模型误设时则明显更优。对您可能有用：本文将形状约束（非参数理论核心工具）引入非可忽略缺失的 IV identification 设定，是半参数/非参数理论与因果推断 identification 的直接交叉。
- **关键技术**: `non-ignorable missing data`, `instrumental variable identification`, `shape-restricted estimation`, `general additive model`, `tuning-parameter-free estimator`, `asymptotic normality under shape constraints`
- **为什么对您有用**: 本文直接连接因果推断的 IV identification 设定（非可忽略缺失需 IV 识别）与非参数理论的形状约束估计，属于 primary interests 的交叉。用您 very_familiar 的非参数统计与 minimax bound 理论，可以审视其收敛速率是否达到 minimax 下界，或用 moderately_familiar 的半参数理论推导其 semiparametric efficiency bound 以判断渐近正态性是否达到有效。Follow-up 判断：**中期可做**——需先在 moderately_familiar 的半参数效率理论（特别是带形状约束约束下的 influence function 推导）上长肌肉，方可推进其效率性质的理论分析。

### 3. [10.1111/sjos.70025](https://doi.org/10.1111/sjos.70025) — Data integration with nonprobability sample: Semiparametric model‐assisted approach
- **作者**: Danhyang Lee, Sixia Chen
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Southern Methodist University · University of Oklahoma Health Sciences Center
- **分类**: vol 53 · issue 1 · pp 33-53
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在概率与非概率样本整合设定下，目标是有限总体均值等参数，关键假设为半参数倾向得分模型（扩展超越MAR以处理非可忽略选择偏差）。作者提出pseudo-profile-likelihood估计半参数倾向得分，再以概率样本为基底构造difference estimator，利用非概率样本提供的研究变量代理值进行偏差校正。理论证明了估计量的n^{-1/2}-CAN性质并给出方差估计公式，模拟与实证显示优于现有方法。对您可能有用：该半参数倾向得分+difference estimator框架与您熟悉的semiparametric efficiency及causal inference中selection bias处理直接相通。
- **关键技术**: `semiparametric propensity score model`, `pseudo-profile-likelihood estimation`, `difference estimator`, `nonprobability sample integration`, `nonignorable selection bias`
- **为什么对您有用**: 本文直接连接causal inference中的selection bias / propensity score建模与semiparametric theory的半参数模型估计。您武器库中semiparametric theory与M-estimation theory（moderately_familiar）可直接攻其pseudo-profile-likelihood的渐近性质与效率分析口子，判断其difference estimator是否达到semiparametric efficiency bound。Follow-up粗判：中期可做——需先在moderately_familiar的M-estimation theory上长肌肉以严格推导其profile likelihood的influence function。

### 4. [10.1111/sjos.70045](https://doi.org/10.1111/sjos.70045) — Adaptive blind image deblurring and denoising
- **作者**: Yicheng Kang, Anik Roy, Partha Sarathi Mukherjee
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Miami University · Emory University · Indian Statistical Institute
- **分类**: vol 53 · issue 1 · pp 413-441
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究空间变模糊（location-varying blur）下的盲图像去模糊与去噪问题，目标是在未知模糊核且模糊机制随像素位置变化的设定下恢复原始图像。核心方法分两步：首先通过自适应选择邻域窗口大小来最大化检测功效以识别模糊像素，随后利用尽可能多的清晰像素进行去模糊与去噪。理论方面，作者证明了当图像分辨率（像素数）趋于无穷时，恢复估计具有一致性，弥补了现有盲去模糊方法普遍缺乏渐近理论的空白。数值实验表明该方法在模拟与真实数据上均优于现有 state-of-the-art。对您而言，本文将自适应邻域选择与检测功效优化结合的思路，以及非平稳逆问题的渐近一致性证明，可为非参数统计中局部自适应估计与逆问题理论提供参考。
- **关键技术**: `adaptive neighborhood selection`, `local test for blur detection`, `spatially varying deconvolution`, `consistency under increasing resolution`, `nonparametric inverse problem`
- **为什么对您有用**: 本文属于非参数逆问题范畴，与您 very_familiar 的'逆问题与随机噪声'直接相关，其自适应邻域选择优化检测功效的机制可类比非参数统计中的局部带宽选择。您可用 minimax bound 与非参数估计率的标准工具审视其一致性结果是否达到最优收敛率，判断是否存在 sharper rate 的可能。**立即可做**：用您熟悉的逆问题与 minimax 理论框架评估其渐近理论的紧性。

### 5. [10.1111/sjos.70027](https://doi.org/10.1111/sjos.70027) — Semiparametric regression for circular response with application in ecology
- **作者**: Jose Ameijeiras‐Alonso, Irène Gijbels
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Universidade de Santiago de Compostela · VIB-KU Leuven Center for Microbiology · KU Leuven
- **分类**: vol 53 · issue 1 · pp 54-101
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在圆形响应变量（如方向角）对线性/圆形协变量的回归设定下，目标 estimand 为条件模态方向与集中度，假设条件密度属于允许不对称与峰度变化的参数灵活族。模态方向与集中度对协变量的依赖通过核权局部多项式拟合进行非参数建模，构成半参数结构。理论核心是建立了条件模态方向与集中度估计量的渐近正态性，并由此推导出最优光滑参数的表达式及其数据驱动选择方法。实证部分用迁徙鸟类方向对飞行高度与风向的回归展示了方法。对您可能有用：该文的局部多项式渐近正态性推导与最优窗宽理论，可直接迁移到您熟悉的非参数统计工具箱中。
- **关键技术**: `circular regression`, `local polynomial fitting`, `kernel smoothing`, `asymptotic normality`, `optimal bandwidth selection`, `semiparametric density model`
- **为什么对您有用**: 本文连接到非参数与半参数理论子方向，其局部多项式渐近正态性与最优窗宽推导属于您 very_familiar 的非参数统计范畴。用您熟悉的 minimax bounds 与非参数收敛率工具，可以验证其声称的渐近正态性是否达到最优率，甚至尝试构造 semiparametric efficiency bound 以判断当前估计量是否有效。follow-up 判断：立即可做——用 very_familiar 的非参数统计武器即可展开对其理论性质的审视与潜在改进。

### 6. [10.1111/sjos.70042](https://doi.org/10.1111/sjos.70042) · [arXiv](https://arxiv.org/abs/2501.16057) — A standardization procedure to incorporate variance partitioning‐based priors in latent Gaussian models
- **作者**: Luisa Ferrari, Massimo Ventrucci
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 364-394
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究 Latent Gaussian Models (LGMs) 中方差参数的先验设定问题；在 LGM 框架下，所有效应均赋予条件高斯先验，但方差参数缺乏直观解释，导致先验 elicitation 困难。核心方法是提出一种标准化 (standardization) 程序，将模型以方差分解 (Variance Partitioning, VP) 形式表示，并对反映各效应相对方差贡献的参数直接赋先验，从而将 VP 先验的适用范围从仅处理随机/固定效应扩展到两者同时存在的更广泛 LGM 类。技术关键在于通过尺度变换统一不同效应的方差度量基准，使得 VP 参数具有可解释性，且后验计算仍可借助 INLA 等工具高效完成。模拟与生存分析真实数据验证了标准化程序在先验 elicitation 和后验推断上的实际优势。对您可能有用：若在半参数/非参数贝叶斯模型（如 Gaussian process prior 的 sieve/RKHS 设定）中需要处理多尺度方差参数的先验 elicitation，此标准化思路提供了可解释的参数化方案。
- **关键技术**: `latent Gaussian models`, `variance partitioning priors`, `prior elicitation`, `standardization procedure`, `Bayesian hierarchical models`, `INLA`
- **为什么对您有用**: 本文连接到半参数理论中贝叶斯非参数/半参数模型的先验设定子方向，尤其是当模型同时包含固定效应与随机效应（如 RKHS/GP 先验）时方差参数的 elicitation 问题。您的 `technical_arsenal` 中 M-estimation theory 与 semiparametric theory 可用于审视此标准化参数化下后验收敛率是否达到 minimax 或 semiparametric efficiency bound，这是当前论文未触及的理论缺口。**中期可做**：需先在 moderately_familiar 的 semiparametric theory 上长肌肉（具体为贝叶斯半参数后验收敛率分析），才能将此 VP 先验的实用性推进到有理论保证的效率推断层面。

### 7. [10.1111/sjos.70033](https://doi.org/10.1111/sjos.70033) — Estimation of generalized tail distortion risk measures with applications in reinsurance
- **作者**: Roba Bairakdar, Frédéric Godin, Mélina Mailhot, Fan Yang
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: American University in Cairo · Concordia University · University of Waterloo
- **分类**: vol 53 · issue 1 · pp 238-267
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究广义尾部扭曲（GTD）风险度量在极值风险设定下的估计问题，目标 estimand 为 GTD 风险度量，关键假设为分布尾部满足极值理论（EVT）的 regularity 条件。核心方法基于 GTD 风险度量的 first-order asymptotic expansion 构建估计量，利用 EVT 中 Hill estimator 与尾部指数的渐近性质实现尾部区域的非参数推断。所提估计量形式简洁，模拟实验表明其表现与文献中现有方法相当或更优，无需复杂的 semiparametric correction。文中进一步提出基于 GTD 的再保险定价原则，并在车险索赔数据上进行了实证验证，将统计不确定性嵌入安全加载。对您而言，本文的极值尾部非参数估计框架与 semiparametric efficiency / minimax rate 的视角形成对比，可作为非参数尾部推断的应用参考。
- **关键技术**: `generalized tail distortion risk measure`, `first-order asymptotic expansion`, `extreme value theory`, `Hill estimator`, `reinsurance premium principle`, `safety loading`
- **为什么对您有用**: 本文连接到非参数理论中极值尾部估计的子方向，但技术深度停留在 first-order expansion 与经典 Hill estimator，未涉及 semiparametric efficiency bound 或 minimax rate 分析。用您 very_familiar 的 minimax bounds 工具可以审视其估计量在尾部区域是否达到最优收敛率，这是一个潜在的理论切入点。**中期可做**：若想在此方向深挖，需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以推导 GTD 估计量的 influence function 与 semiparametric efficiency bound。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1111/sjos.70043](https://doi.org/10.1111/sjos.70043) · [arXiv](https://arxiv.org/abs/2311.06719) — Efficient multiple‐robust estimation for nonresponse data under informative sampling
- **作者**: Kosuke Morikawa, Kenji Beppu, Wataru Aida
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 395-412
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在概率抽样下存在无响应的设定中，目标是估计总体参数并同时校正抽样偏差与选择偏差，关键假设是将抽样权重视为随机变量并正确指定响应/抽样机制模型。本文首先推导了该设定下的 semiparametric efficiency bound，并构造了具有 double robustness 的有效估计量，但其充分有效性依赖于所有工作模型的正确指定。为增强对模型误设的鲁棒性，作者提出了一种新颖的两步经验似然（empirical likelihood）方法，将双重鲁棒性扩展为多重鲁棒性（multiple robustness），允许在多个候选模型中自动选择正确模型以消除偏差。数值模拟与 NHANES/NHIS 数据整合的实证结果验证了该方法在有限样本下的表现。对您可能有用：本文将 semiparametric efficiency bound 与 multiple robustness 结合，为处理 informative sampling 下的缺失数据与数据整合提供了新思路。
- **关键技术**: `semiparametric efficiency bound`, `double robustness`, `multiple robustness`, `empirical likelihood`, `informative sampling`, `data integration`
- **为什么对您有用**: 本文直接连接到 efficiency theory（semiparametric efficiency bound）与 causal inference 中的缺失数据/选择偏差设定，其 multiple robustness 通过 empirical likelihood 实现的思路可对比您熟悉的 HOIF（Higher-Order Influence Functions）在鲁棒性上的技术路线。用您 very_familiar 的 semiparametric efficiency 理论可直接验证其 bound 推导；但其两步 empirical likelihood 的理论性质分析需您在 moderately_familiar 的 M-estimation theory 上长肌肉才能深入拓展。**中期可做**。

## 数理统计 / 假设检验  *(hypothesis_testing, 5 篇)*

### 1. [10.1111/sjos.70046](https://doi.org/10.1111/sjos.70046) — Fixed effects Bayesian testing in high‐dimensional linear mixed models
- **作者**: Jiamin Liu, Xingwei Liu, Heng Lian, Wangli Xu
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Science and Technology Beijing · Renmin University of China · City University of Hong Kong
- **分类**: vol 53 · issue 1 · pp 442-481
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在高维线性混合模型（p>n）设定下，本文研究固定效应的分组显著性检验问题，目标是在常规低维频率方法失效时仍能控制 type-I error。所提检验统计量由一列独立但不同分布随机变量构造的两个二次型之比构成，其零分布通过二次型的正态逼近推导。为实现快速计算临界值，作者提出一种一步迭代法（one-step iteration），避免了传统 bootstrap 的重采样开销；并在 mild regularity 条件下推导了局部替代假设下的 power 函数。数值实验表明该方法在功效上优于现有高维检验，且计算便捷。对您有用：本文将高维二次型分布逼近与一步迭代数值方法结合，直接触及您在 hypothesis testing 与 stat_computing 的交叉兴趣。
- **关键技术**: `quadratic form ratio test`, `normality approximation for quadratic forms`, `one-step iteration critical value`, `local alternative power analysis`, `high-dimensional linear mixed model`
- **为什么对您有用**: 本文直接连接您 primary interest 中的 hypothesis testing（高维混合模型下的分组检验）与 stat_computing（一步迭代法求临界值替代 bootstrap）。用您 very_familiar 的高维渐近理论可以审视其二次型正态逼近的精度条件是否可进一步放松；moderately_familiar 的 M-estimation theory 可用于分析其估计步骤的渐近性质。**立即可做**：用 very_familiar 的高维渐近与 minimax 工具验证其逼近条件的紧性，并评估一步迭代法的数值稳定性。

### 2. [10.1111/sjos.70049](https://doi.org/10.1111/sjos.70049) — Kernel‐based marginal testing for covariate effects in high‐dimensional settings
- **作者**: Hong Yin, Yijun Wang, Ancha Xu
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Zhejiang Gongshang University
- **分类**: vol 53 · issue 1 · pp 498-531
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在高维回归背景下，本文提出一种基于核的条件均值依赖（kernel‐based conditional mean dependence）的边际检验方法，用于检验单个协变量对响应变量的条件均值效应，无需假定模型形式。该方法通过核函数构造一个度量条件均值依赖的统计量，并在原假设下证明其渐近服从正态分布，在局部备择下也能给出渐近分布。理论推导依赖于将检验统计量近似为一类二次型，并利用二次型渐近理论建立极限分布。作者在线性模型和完全非参数两种框架下分析了该检验的渐近相对效率，并与多种现有方法比较。模拟和真实数据分析验证了方法的有效性。该工作直接关联你的假设检验和高维统计兴趣，且其二次型结构可借助你熟悉的高维渐近工具深入理解。
- **关键技术**: `kernel-based conditional mean dependence`, `quadratic form approximation`, `marginal testing`, `asymptotic normality`, `asymptotic relative efficiency`, `model-free inference`
- **为什么对您有用**: 该论文聚焦高维假设检验中的边际效应检验问题，直接对应你的primary interest中的hypothesis testing方向。你可以利用very_familiar中的high-dimensional asymptotics和nonparametric statistics工具来评价其理论框架，同时可以用moderately_familiar中的theory of higher-order U-statistics进一步分析其二次型统计量的投影结构（因为核统计量可视为U-统计量）。follow-up判断：立即可做——你已有的高维渐近和非参数知识足以理解并批判性地审视该方法的理论贡献，并可考虑将其思想扩展到纵向数据或因果推断中的敏感性分析场景。

### 3. [10.1111/sjos.70032](https://doi.org/10.1111/sjos.70032) · [arXiv](https://arxiv.org/abs/2503.21137) — Variable selection via thresholding
- **作者**: Ka Long Keith Ho, Hien Duy Nguyen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 207-237
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究回归中的变量选择问题，针对估计量不能自动将无关变量系数收缩至零的情形，提出了一种基于阈值化的简单选择程序，并在温和正则条件下证明了该程序能一致估计真实相关变量集。所提出的稀疏估计量达到√n一致性和渐近正态性，且其非零元素不存在收缩偏差，克服了传统正则化方法（如Lasso）的有偏问题。方法的核心是选择合适的阈值序列λ_n，使错误发现率渐近为零，理论证明依赖经验过程工具和常规的矩条件。模拟和真实数据实验验证了方法在有限样本下的表现。本文在假设检验框架内为变量选择提供了一种无需惩罚项的替代路径，其理论简洁且可解释性强。对您的高维统计兴趣而言，该方法的阈值化思路可拓展至高维设定（p随n增长），而您的武器库中‘高维渐近’和‘minimax界’可直接用于分析该方法在高维情景下的支持集恢复性和最优性。
- **关键技术**: `thresholding`, `variable selection consistency`, `asymptotic normality`, `sparse estimation`, `√n-consistency`, `empirical process`
- **为什么对您有用**: 本文涉及变量选择这一高维统计的核心问题，与您在高维统计（尤其是随机矩阵理论之外的高维推断）的兴趣直接相关。您的‘高维渐近’武器库可立即用于推广本文理论至p随n增长的情景，并验证阈值序列的渐近行为；同时‘minimax界’能检验该方法在稀疏信号模型下是否达到最优收敛率。这是一项立即可做的follow-up：将本文的固定p结果扩展至高维框架，分析其支持集恢复的相变条件。

### 4. [10.1111/sjos.70050](https://doi.org/10.1111/sjos.70050) — ATM: An aggregation test of moments approach for assessing high‐dimensional normality
- **作者**: Hengjian Cui, Lingyue Zhang
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Capital Normal University · Dongbei University of Finance and Economics
- **分类**: vol 53 · issue 1 · pp 532-553
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对高维数据下的正态性检验问题，提出基于矩条件的检验方法。传统仿射不变检验依赖协方差矩阵逆，在高维设定下失效。作者引入协三阶矩和协四阶矩两个新指数，从高阶矩层面刻画分布与高斯家族的偏离。基于这两个指数构造两个检验统计量，在温和正则条件下建立了渐近正态性和一致性。进一步采用功效增强技术将两个检验聚合，得到更灵敏的 ATM 检验。模拟和真实数据分析表明，该方法在多种维度设定下控制住了 size 并具有竞争力的 power。该工作直接连接研究者对高维假设检验的兴趣，且检验统计量可视为高阶 U-统计量，为后续效率提升提供了切入点。
- **关键技术**: `co-third moment`, `co-fourth moment`, `power enhancement technique`, `aggregation test`, `Gaussian moment characterization`
- **为什么对您有用**: 该论文聚焦高维正态性检验，直接对应研究者高维统计与假设检验的核心兴趣。研究者可以运用自身对高阶 U-统计量（very_familiar）的理解，将协三阶/四阶矩视为对称核，用投影理论分析其渐近分布或提出更高效的变体；同时高维渐近工具（very_familiar）可直接用于验证正则条件的紧性。综上，立即可做。

### 5. [10.1111/sjos.70029](https://doi.org/10.1111/sjos.70029) · [arXiv](https://arxiv.org/abs/2407.09130) — On goodness‐of‐fit testing for self‐exciting point processes
- **作者**: José Carlos Fontanesi Kling, Mathias Vetter
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 102-139
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在自激点过程（self-exciting point process, 如 Hawkes 过程）的参数模型设定下，本文旨在建立检验给定参数模型是否合适的 goodness-of-fit 检验。核心方法是 bootstrap-based 检验程序：基于拟合模型的残差时间变换（residual time transformation），通过 bootstrap 重抽样构造检验统计量，经验上对各类自激点过程均有效。理论方面，在 infill-asymptotic 设定下，仅证明了对非齐次 Poisson 过程这一特例的渐近一致性（asymptotic consistency）。对您可能有用：本文填补了自激点过程 GoF 检验的理论空白，其 bootstrap + infill-asymptotic 框架为假设检验与半参数/非参数理论交叉提供了新场景。
- **关键技术**: `self-exciting point process`, `goodness-of-fit testing`, `bootstrap-based test`, `infill-asymptotics`, `residual time transformation`, `asymptotic consistency`
- **为什么对您有用**: 直接连接到 primary interest 中的 hypothesis testing 子方向，且 infill-asymptotic 设定与 nonparametric / semiparametric theory 的连续时间推断有技术交集。用 very_familiar 的 minimax bounds 与 M-estimation theory 可以审视其仅对 Poisson 特例证明一致性的理论缺口，尝试在更一般的自激过程（如 Hawkes）下建立更严密的渐近理论。**中期可做**：需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以处理自激点过程的似然与条件强度函数的 M-估计渐近性质，才能推进一致性证明的推广。

## 统计计算 / 算法  *(stat_computing, 4 篇)*

### 1. [10.1111/sjos.70036](https://doi.org/10.1111/sjos.70036) · [arXiv](https://arxiv.org/abs/2007.04229) — Estimating Monte Carlo variance from multiple Markov chains
- **作者**: Kushagra Gupta, Dootika Vats
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Indian Institute of Technology Kanpur
- **分类**: vol 53 · issue 1 · pp 335-363
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在多链并行 MCMC 设定下，目标是估计 Monte Carlo 平均的协方差矩阵（即方差估计），关键假设为 Markov 链的弱混合条件。作者指出简单平均各链的 batch means (BM) 协方差估计量在小样本下会严重低估方差，尤其对慢混合链。为此，提出 multivariate replicated batch means (RBM) 估计量，利用跨链信息修正低估；在弱混合条件下，RBM 具有强一致性，且大样本偏差与方差与单链 BM 相当。理论上证明了在 MCMC 存在正相关时，RBM 估计量的负偏差严格小于平均 BM 估计量，从而在小运行长度下 RBM 显著优于 BM。对您有用：若在因果推断或高维推断中依赖多链 MCMC 采样（如贝叶斯 IV / proximal 模型），RBM 提供了更可靠的方差估计工具。
- **关键技术**: `replicated batch means`, `multivariate covariance estimator`, `MCMC variance estimation`, `strong consistency under weak mixing`, `bias reduction for correlated chains`
- **为什么对您有用**: 本文连接到统计计算与数值方法子方向，解决多链 MCMC 方差估计的实际计算问题。研究者武器库中的软件开发与高维渐近理论可直接用于实现与评估 RBM 在复杂贝叶斯因果模型中的表现。立即可做：用 very_familiar 的软件开发技能复现 RBM 算法并在慢混合链（如高维后验）上测试偏差改善。

### 2. [10.1111/sjos.70052](https://doi.org/10.1111/sjos.70052) — Optimal subsampling for estimation of dimension reduction directions
- **作者**: Xinru Jia, Weixuan Yuan, Xingqiu Zhao, Xuehu Zhu
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Xi'an Jiaotong University · ETH Zurich · Hong Kong Polytechnic University
- **分类**: vol 53 · issue 1 · pp 575-611
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 针对大规模高维数据下充分降维（SDR）方法因迭代过程导致计算成本过高的问题，本文提出了针对两种代表性SDR方法（基于条件密度函数的细化外积梯度法rdOPG和最小平均方差估计dMAVE）的最优子采样策略。在逆概率加权（IPW）框架内，以渐近方差协方差矩阵的迹最小化为目标，推导了最优子采样概率的显式闭式解，并建立了加权估计量的一致性和渐近正态性。该方法避免了均匀子采样带来的信息损失，在保持统计精度的同时大幅降低计算复杂度。仿真与真实数据验证表明，相比均匀子采样，该方法在估计精度和计算效率上均有显著提升。该工作直接服务于高维统计与统计计算交叉方向，其IPW框架和渐近分析技术可以迁移至研究者的因果推断M估计工具箱中。
- **关键技术**: `optimal subsampling`, `sufficient dimension reduction`, `inverse probability weighting`, `asymptotic variance minimization`, `rdOPG`, `dMAVE`
- **为什么对您有用**: 该论文直接关联您的高维统计与计算效率兴趣，将经典SDR方法与子采样结合，解决大规模数据下的计算瓶颈。研究者very_familiar中的'estimation theory in causal inference'中的IPW框架可平行类比此处的加权估计，而moderately_familiar中的'M-estimation theory'可直接用于分析其渐近效率。立即可做：您可尝试用此子采样框架替换因果推断中大规模数据的倾向得分加权估计步骤。

### 3. [10.1111/sjos.70006](https://doi.org/10.1111/sjos.70006) · [arXiv](https://arxiv.org/abs/2412.19186) — On optimal linear prediction
- **作者**: Inge S. Helland
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 16-32
- 相关性 4/10 · novelty: `new_theory`
- **摘要**: 本文在线性预测框架下，研究基于模型约简的预测方法的最优性，目标是最小化期望均方预测误差。通过引入特定假设，证明最优模型约简等价于偏最小二乘（PLS）回归的统计模型，并在一定条件下给出类PLS预测器优于其他预测器的理论依据。作者进一步将两种不同模型约简统一于量子力学设定中，提供跨学科视角。方法上，利用期望MSE作为最优性准则，构建了PLS的统计理论基础，而非传统化学计量学的算法视角。主要理论贡献在于严格证明了PLS在特定线性预测配置下的近似最优性，并显示了与量子概念的深层联系。该文对统计计算（数值算法理论）和数学统计（预测理论）均具有参考价值，尤其为理解PLS的统计性质提供了坚实框架。
- **关键技术**: `Partial least squares (PLS)`, `Model reduction`, `Expected mean squared prediction error`, `Linear prediction`, `Quantum mechanical analogy`
- **为什么对您有用**: 该文深入线性预测的最优性理论，将PLS回归纳入严格统计框架，直接连接您对统计计算（算法理论）和数学统计的兴趣。您非常熟悉的'estimation theory in causal inference'中的risk分析技巧虽直接用于因果，但其中的risk评估思路可迁移至本文的期望MSE最优性分析，帮助验证理论的一致性。纯统计部分（PLS理论）可直接作为入门材料阅读；而量子力学视角的模型约简需额外学习量子基础（目前武器库不包含），属中期可探索方向。

### 4. [10.1111/sjos.70031](https://doi.org/10.1111/sjos.70031) — Recursive Bayesian prediction of remaining useful life for gamma degradation process under conjugate priors
- **作者**: Ancha Xu, Weiwei Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Zhejiang Gongshang University
- **分类**: vol 53 · issue 1 · pp 175-206
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在齐次 Gamma 退化过程模型下，目标是推导其似然函数复杂参数结构的共轭先验，并基于此进行剩余使用寿命（RUL）的递归贝叶斯预测。核心机制是为齐次 Gamma 过程构造特定共轭先验，并设计三种后验采样算法（Gibbs sampling、离散网格采样、采样重要性重采样 SIR）以实现参数推断。进一步将共轭先验推广至带异质性效应的 Gamma 过程，在等间距监测时间点下实现后验分布的递归更新，从而开发出一种在线 RUL 预测算法。仿真与两个真实数据集（含高频监测场景）验证了算法的计算效率与估计精度。对您可能有用：本文的递归贝叶斯更新与在线算法设计思路，可作为统计计算方向中数值方法与软件实现的具体案例参考。
- **关键技术**: `conjugate prior derivation`, `Gibbs sampling`, `sampling importance resampling (SIR)`, `discrete grid approximation`, `recursive Bayesian updating`, `remaining useful life prediction`
- **为什么对您有用**: 本文属于统计计算与可靠性方向的结合，核心贡献是共轭先验推导与递归在线算法设计，连接到您 primary interest 中的 statistical computing（数值方法与算法）。从 technical_arsenal 看，您 very_familiar 的 software development 与 high-dimensional asymptotics 可直接审视其算法实现效率与渐近性质，但本文缺乏与您核心武器库（higher-order U-statistics / minimax bounds / causal inference）的直接技术接口。Follow-up 判断：**暂不可做**——本文属于可靠性工程的参数贝叶斯推断，您武器库中缺少退化过程 / 可靠性生存分析的专业先验知识，且无 minimax / efficiency / U-stat 的技术切入点，仅适合作为统计计算的泛读案例。

## 其他  *(other, 2 篇)*

### 1. [10.1111/sjos.70048](https://doi.org/10.1111/sjos.70048) — Nonparametric simulation of multivariate extreme events via spectral bootstrap
- **作者**: Nisrine Madhar, Juliette Legrand, Maud Thomas
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Centre National de la Recherche Scientifique · Université Paris Cité · Laboratoire de Probabilités et Modèles Aléatoires · Université de Bretagne Occidentale · Laboratoire de Mathématiques de Bretagne Atlantique · Université Claude Bernard Lyon 1 · Sorbonne Université
- **分类**: vol 53 · issue 1 · pp 482-497
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 极值理论（EVT）因极端观测稀少而面临推断困难。本文提出一种非参数模拟框架：多元极值事件谱bootstrap（spectral bootstrap），基于多元广义帕累托分布（mGP）的谱表示生成合成极端数据，同时保留原始数据的联合尾部依赖结构。与传统bootstrap不同，该方法仅依赖极值区域的观测，不假设尾部形状参数已知，从而在保持渐近正确性的同时增加有效样本量。通过模拟和真实数据（如气象或金融风险指标）验证，所提方法显著改善了尾部风险度量（如VaR和ES）估计的稳定性。该方法计算上允许从任意mGP谱分布中有效采样，无需参数假设，适用于高维极值场景。对您而言，该谱bootstrap虽不直接对应主要兴趣，但非参数重采样思想与极值尾部建模可为流行病学或经济中的罕见事件模拟提供工具——属于secondary兴趣的gateway reading。
- **关键技术**: `Spectral representation of multivariate generalized Pareto`, `Nonparametric bootstrap`, `Tail dependence preservation`, `Extreme value theory`, `Risk metric estimation`
- **为什么对您有用**: 本文属于极值统计领域，并非您的主要兴趣点，但其非参数模拟方法可扩展至高维极端事件分析，与您的高维统计兴趣有潜在交集。武器库中的'nonparametric statistics'可帮您理解其非参数一致性，但核心的谱分解与极值渐近理论不在现有武器库中，因此暂不可做直接follow-up。作为gateway reading，它适合快速了解极值模拟的前沿，为未来在流行病学或经济数据中处理罕见事件（secondary兴趣）储备工具。

### 2. [10.1111/sjos.70030](https://doi.org/10.1111/sjos.70030) · [arXiv](https://arxiv.org/abs/2407.03619) — Multivariate representations of univariate marked Hawkes processes
- **作者**: Louis Davis, Conor Kresin, Boris Baeumer, Ting Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 140-174
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究单变量标记 Hawkes 过程与多变量无标记 Hawkes 过程之间的基本联系，并基于此提出一种新的多元表示框架来参数化单变量标记 Hawkes 过程。方法核心是引入多元无标记 Hawkes 表示作为参数化工具，证明其能渐近逼近一大类单变量标记 Hawkes 过程，且当原始过程平稳时表示也具有平稳性。进一步证明该表示的条件强度参数可识别且具有解释性。通过模拟研究给出了参数空间扩展导致的误差启发式界。最后将方法应用于南加州地震目录数据，验证了方法的有效性。对您而言，本文的点过程表示方法虽不直接对应核心研究兴趣，但其参数化策略和可识别性分析在纵向事件数据建模（如因果推断中的 treatment timing）中具有潜在参考价值。
- **关键技术**: `Hawkes process`, `multivariate representation`, `conditional intensity`, `identifiability`, `stationarity`, `approximation bound`
- **为什么对您有用**: 本文讨论的点过程表示问题虽未直接列出在您的兴趣中，但多元表示和参数可识别性在 longitudinal causal inference（如动态 treatment 识别）中有潜在参考意义，流行病学中的事件数据建模也常涉及 Hawkes 过程。您武器库中 'computation of higher-order U-statistics (treewidth / tensor contraction / einsum)' 可用于分析多元 Hawkes 过程似然计算的高维复杂度——其参数空间扩张可能导致张量网络收缩问题。综合来看，这是一个中期可做的课题：需要先在 moderately_familiar 的 semiparametric theory 上加强，以深度理解表示误差的渐近性质。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

