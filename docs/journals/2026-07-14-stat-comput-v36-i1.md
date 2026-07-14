# Stat. Comput. — Vol 36  Issue 1  ·  2026-07-14

- 共 31 篇 · Statistics and Computing
- 目录核对 ⚠️ 疑似漏 28 篇（对照 OpenAlex 59 篇）：10.1007/s11222-025-10773-w、10.1007/s11222-025-10778-5、10.1007/s11222-025-10766-9、10.1007/s11222-025-10799-0、10.1007/s11222-025-10788-3 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Stat. Comput.》第36卷第1期的31篇论文，整体上可归纳为四条主线：**因果推断与缺失/误差数据**（约3篇）、**统计计算与算法设计**（约12篇，涵盖MCMC、变分推断、稀有事件采样、优化等）、**高维/鲁棒统计与模型选择**（约4篇，包括稀疏回归、鲁棒PCA、贝叶斯收缩先验）、以及**非参数/半参数与函数型数据建模**（约3篇）。此外，还有少量论文涉及假设检验、流行病学聚类、网络分析、空间统计等应用方向。

在**因果推断**主线上，本期有三篇论文从不同角度处理数据质量问题。FATE方法（Inverse probability weighting estimation under ultrahigh-dimensional error-prone covariates and misclassified treatments）同时应对超高维协变量测量误差和处理错分，通过四步法（特征筛选、自适应Lasso、两类误差校正）实现ATE的相合估计，并给出了渐近正态性。BSIV方法（Best-subset instrumental variable selection method using mixed integer optimization）将混合整数优化引入工具变量选择，在IV有效性未知时仍能稳健估计因果效应，无需事先假定所有IV有效，相比Lasso类IV方法在偏差和效率上更优。Fair conformal prediction for incomplete covariate data则聚焦缺失数据下的不确定性量化，通过核平滑得分函数实现渐近条件有效的保形预测，其框架可迁移至因果效应的区间估计。

**统计计算**是本期最密集的主线，覆盖了采样、优化、积分等多个子方向。在MCMC方面，Fast sampling and model selection for Bayesian mixture models通过无拒绝采样从组件分配边缘后验直接采样，显著优于标准Gibbs；A note on auxiliary mixture sampling for Bayesian Poisson models系统分析了高斯混合近似的精度问题并给出鲁棒改进；Novel Bayesian algorithms for ARFIMA long-memory processes比较了滤波MCMC与ABC方法。在变分推断方面，Scalable variational inference for multinomial probit models under large choice sets and sample sizes利用神经嵌入和重参数化技巧，在大选择集（20项）和大样本（100万）下实现高效推断。在优化方面，Sequential Sample Average Majorization–Minimization提出顺序数据子集的随机MM算法，无需凸性或光滑性假设；Optimal sparse phase retrieval via a quasi-Bayesian approach用PAC-Bayes框架给出稀疏相位恢复的极小极大最优率，并设计了Langevin Monte Carlo算法。在稀有事件采样方面，Importance sampling for rare event tracking within the ensemble Kalman filtering framework和Adaptive Reduced Multilevel Splitting分别处理SDE轨迹稀有事件和基于近似得分函数的自适应多层分裂。此外，Transporting higher-order quadrature rules将传输映射应用于拟蒙特卡洛点和稀疏网格，为混合分布积分提供优于N^{-1/2}的收敛速率；Unbiased parameter estimation for bayesian inverse problems通过随机化技巧消除数值离散偏差，实现无偏参数估计。

在**高维/鲁棒统计**方向，Heavy Lasso（Heavy Lasso: sparse penalized regression under heavy-tailed noise via data-augmented soft-thresholding）针对重尾噪声，采用t分布损失函数并通过数据增广实现软阈值，建立了ℓ1和ℓ2范数下的非渐近界。Sparse outlier-robust PCA for multi-source data通过鲁棒协方差估计和全局-局部结构化稀疏惩罚，同时实现特征选择、多源模式检测和抗离群值。The Group R2D2 Shrinkage Prior for Sparse Linear Models with Grouped Covariates将R2D2先验扩展到分组变量选择，通过组级和变量级Dirichlet先验实现自适应收缩。Removal of redundant candidate points for the exact D-optimal design problem利用近似设计必要条件快速剔除冗余候选点，使混合整数规划可求解大规模精确D-最优设计问题。

对于因果推断方向的研究者，建议优先关注FATE、BSIV和Fair conformal prediction这三篇，它们分别处理了测量误差、工具变量有效性和缺失数据这三个因果推断中的核心数据挑战。对于半参数/非参数效率方向，Penalized spatial function-on-function regression和Low-rank regularization of global fréchet regression models for distributional responses提供了函数型数据与空间依赖下的估计理论，但本期在半参效率界方面贡献较少。对于高维方向，Heavy Lasso和The Group R2D2 Shrinkage Prior分别从鲁棒性和分组结构角度推进了稀疏回归，而Sparse outlier-robust PCA for multi-source data则拓展了高维降维的鲁棒性。

## 因果推断  *(causal_inference, 3 篇)*

### 1. [10.1007/s11222-025-10755-y](https://doi.org/10.1007/s11222-025-10755-y) — Inverse probability weighting estimation under ultrahigh-dimensional error-prone covariates and misclassified treatments
- **作者**: Li-Pang Chen
- **期刊/来源**: Statistics and Computing
- **机构**: National Chengchi University
- **分类**: vol 36 · issue 1
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文研究在协变量和 treatments 均存在测量误差且协变量为超高维（p >> n）时，如何估计平均处理效应（ATE）。目标 estimand 是 ATE，识别基于倾向得分的逆概率加权（IPW），但数据中协变量测量误差和处理错分同时存在，且潜在结果对协变量有非线性依赖。作者提出 FATE 方法，整合了四个步骤：基于测量误差校正数据的特征筛选（screening）、adaptive lasso 变量选择、处理错分校正、协变量误差校正。倾向得分估计器在同时校正两类误差后具有相合性，并考虑了多重共线性问题。理论部分证明了 ATE 估计量的相合性和渐近正态性。模拟实验表明 FATE 在有限样本下一致优于若干对比方法。对您而言，本文连接了高维统计（超高维特征筛选）与因果推断（ATE 估计）的交叉点，且涉及测量误差这一实际挑战，但方法学 novelty 主要在于组合已有工具而非提出全新理论框架。
- **关键技术**: `inverse probability weighting`, `feature screening`, `adaptive lasso`, `measurement error correction`, `treatment misclassification`, `ultrahigh-dimensional covariates`
- **为什么对您有用**: 本文直接连接您 primary interest 中的因果推断（ATE 估计）和高维统计（超高维协变量），但方法学上主要是将特征筛选、adaptive lasso、误差校正等已有工具组合，理论贡献（相合性与渐近性）较为常规。从武器库看，您对高维渐近和因果推断估计理论非常熟悉，因此**立即可做**：可以尝试用您熟悉的 minimax 下界工具检验 FATE 估计量在超高维+测量误差设定下是否达到最优收敛速率，或将其与您熟悉的 debiased ML 框架对比。

### 2. [10.1007/s11222-025-10760-1](https://doi.org/10.1007/s11222-025-10760-1) — Best-subset instrumental variable selection method using mixed integer optimization with applications to health-related quality of life and education–wage analyses
- **作者**: Muhammad Qasim, Kristofer Månsson, Narayanaswamy Balakrishnan
- **期刊/来源**: Statistics and Computing
- **机构**: Lund University · Linnaeus University · Jönköping University · McMaster University
- **分类**: vol 36 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对工具变量（IV）回归中经典 best-subset 选择方法因 NP-hard 而难以计算的问题，提出将混合整数优化（MIO）算法引入 IV 设定，开发了 BSIV 方法。该方法在 IV 有效性未知（即可能存在直接效应或与未测量变量相关）时仍能稳健估计因果效应，无需事先假定所有 IV 均有效。BSIV 通过 MIO 求解稀疏 IV 选择问题，在 Monte Carlo 模拟中相比两阶段最小二乘、Lasso 类 IV 以及中位数/众数估计器在偏差和相对效率上均表现更优。作者还分析了健康相关生活质量指数与邻近性、教育-工资关系两个实际数据集，展示了方法的实用性。对您而言，本文连接了因果推断中 IV 的稳健估计与统计计算中的 MIO 算法，属于您 primary interest 中 IV 方向的一个具体计算实现。
- **关键技术**: `mixed integer optimization (MIO)`, `best-subset selection`, `instrumental variable regression`, `two-stage least squares`, `Lasso-type IV`
- **为什么对您有用**: 本文直接对应您 primary interest 中的 IV 因果推断方向，且其核心 MIO 算法属于统计计算（statistical computing）范畴，与您武器库中 'software development' 和 'estimation theory in causal inference' 非常熟悉。您可立即可做：用您熟悉的 M-estimation 理论分析 BSIV 的渐近性质（如一致性、收敛速率），或将其与您熟悉的 higher-order U-statistics 结合，处理多 IV 情形下的高阶偏差校正。

### 3. [10.1007/s11222-025-10775-8](https://doi.org/10.1007/s11222-025-10775-8) · [arXiv](https://arxiv.org/abs/2504.12582) — Fair conformal prediction for incomplete covariate data
- **作者**: Jingsen Kong, Yiming Liu, Guangren Yang, Ding Zhong
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究协变量缺失场景下保形预测（conformal prediction）的不确定性量化问题。在不可交换保形预测框架下，作者证明覆盖保证依赖于缺失模式（mask），并据此提出一种满足边际和mask条件有效性的方法。进一步，为达到渐近条件有效性，引入基于核平滑的新得分函数的局部化保形预测方法，在适当假设下同时实现边际、mask条件和渐近条件有效性。模拟和真实数据分析验证了所提方法的优势。该工作对您可能有用：缺失数据是因果推断（如proximal CI、IV）中的常见挑战，本文的保形预测框架可迁移至因果效应的不确定性量化。
- **关键技术**: `nonexchangeable conformal prediction`, `mask-conditional validity`, `kernel smoothing score function`, `localized conformal prediction`
- **为什么对您有用**: 本文直接关联您的primary interest中的因果推断（缺失数据是proximal CI和IV的常见设定），且其mask条件有效性思路可迁移至因果效应的条件覆盖问题。武器库中'非参数统计'和'因果推断中的估计理论'可直接用于分析其渐近性质，属于**立即可做**的follow-up：例如将局部化保形预测与double machine learning结合，为ATE提供缺失协变量下的条件保形区间。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1007/s11222-025-10785-6](https://doi.org/10.1007/s11222-025-10785-6) · [arXiv](https://arxiv.org/abs/2506.07790) — Heavy Lasso: sparse penalized regression under heavy-tailed noise via data-augmented soft-thresholding
- **作者**: The Tien Mai
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对高维线性回归中重尾噪声或异常值破坏经典Lasso性能的问题，提出Heavy Lasso方法。该方法在Lasso惩罚框架下采用基于t分布的损失函数，对小残差保持二次行为，对大偏差自适应降权，从而增强鲁棒性。计算上通过数据增广方案和软阈值算法实现，可与经典Lasso求解器无缝集成。理论上利用局部凸性框架建立了ℓ1和ℓ2范数下的非渐近界，表明Heavy Lasso估计量达到与Huber损失相当的收敛速率。数值实验显示其在重尾噪声下优于经典Lasso及其他鲁棒变体。对您而言，该工作直接关联高维统计中的鲁棒估计问题，其数据增广+软阈值的计算策略可迁移至您熟悉的因果推断或U统计量中的稳健化处理。
- **关键技术**: `data augmentation`, `soft-thresholding algorithm`, `localized convexity framework`, `Student's t-distribution loss`, `non-asymptotic bounds`
- **为什么对您有用**: 本文直接连接您的高维统计兴趣，特别是重尾噪声下的稀疏回归。您武器库中的'高维渐近理论'和'非参数统计'可直接用于评估其ℓ1/ℓ2界的紧性，而'软件发展'技能可帮助复现或扩展其Github包。中期可做：若想将t分布损失推广至因果推断中的双稳健估计，需先在'半参数理论'上加强（moderately_familiar），以推导相应的影响函数。

## 非参数 / 半参数  *(nonparam_semipara, 2 篇)*

### 1. [10.1007/s11222-025-10805-5](https://doi.org/10.1007/s11222-025-10805-5) · [arXiv](https://arxiv.org/abs/2505.04926) — Low-rank regularization of global fréchet regression models for distributional responses
- **作者**: Kyunghee Han, Hsin-Hsiung Huang
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文在 Fréchet 回归框架下，针对分布函数型响应变量（非欧几里得空间）提出一种全局回归估计方法，并引入低秩正则化。核心设定是：协变量为欧几里得，响应为分布函数（属于 Wasserstein 空间或 L2 空间），目标是在该非欧空间中建立全局线性模型。方法上，作者利用模型参数的低秩结构来提升拟合效率与精度，这与传统的维度缩减（如主成分分析）不同，低秩正则化直接作用于 Fréchet 回归的目标函数。理论部分给出了大样本性质，包括估计量的收敛速率，但未涉及半参效率界或影响函数。数值实验验证了有限样本下的性能提升。对您而言，本文连接了非参数回归与低秩结构，后者在高维统计和计算复杂度中常见，但本文的低秩正则化思路可迁移到您熟悉的逆问题或因果推断中的高维协变量降维场景。
- **关键技术**: `Fréchet regression`, `low-rank regularization`, `distributional responses`, `Wasserstein space`, `global linear model`
- **为什么对您有用**: 本文连接您的非参数统计兴趣（Fréchet 回归处理非欧响应）和统计计算中的低秩正则化。技术武器库中'非参数统计'和'高维渐近'可直接用于理解其收敛速率推导，但低秩正则化与 Fréchet 回归的结合是您 moderately_familiar 的 M-估计理论可攻的方向。中期可做：若您想将低秩正则化引入因果推断中的分布效应估计，需先在 moderately_familiar 的'半参理论'上长肌肉（如处理非欧响应的影响函数）。

### 2. [10.1007/s11222-025-10792-7](https://doi.org/10.1007/s11222-025-10792-7) · [arXiv](https://arxiv.org/abs/2512.00237) — Penalized spatial function-on-function regression
- **作者**: Ufuk Beyaztas, Han Lin Shang, Gizel Bakicierler Sezer
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文提出一种惩罚空间函数对函数回归模型，用于处理函数型协变量与响应变量之间的回归关系，同时允许观测之间存在空间依赖性。现有方法大多假设观测独立，这在空间结构数据中不成立；作者将广义空间两阶段最小二乘估计量扩展到函数数据，并用B样条张量积对回归系数函数施加粗糙度惩罚，以控制过拟合并提高可解释性。所提惩罚空间两阶段最小二乘估计量在温和正则条件下达到√n-相合性和渐近正态性。蒙特卡洛模拟表明，在中等到强空间依赖下，该方法显著优于非惩罚估计量。北达科他州气象数据应用展示了模型在空间相关气象变量建模中的实用性。对您而言，本文涉及函数型数据与空间统计的交叉，其惩罚估计和渐近理论可联系到您的非参数/半参数理论兴趣，但方法学新颖性有限，属于现有框架的扩展应用。
- **关键技术**: `spatial two-stage least squares`, `B-spline tensor product`, `roughness penalty`, `function-on-function regression`, `√n-consistency`
- **为什么对您有用**: 本文属于非参数/半参数理论方向，具体是函数型数据回归中的空间依赖建模。您的武器库中'非参数统计'和'高维渐近'可以直接用于理解其惩罚估计的渐近性质，但核心方法（空间两阶段最小二乘）与您的因果推断或U-统计量兴趣交集不大。中期可做：若您想进入函数型数据分析，需先在'半参数理论'上熟悉函数型主成分等工具。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1007/s11222-025-10762-z](https://doi.org/10.1007/s11222-025-10762-z) · [arXiv](https://arxiv.org/abs/2410.20918) — Bootstrap tests for almost goodness-of-fit
- **作者**: Amparo Baíllo, Javier Cárcamo
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文提出“几乎拟合优度检验”（almost goodness-of-fit test），用于检验一个参数模型族是否在 L^p 距离下与真实分布足够接近（而非精确相等）。原假设 H0: ||F - G(θ_F)||_p ≥ ε，备择 H1: ||F - G(θ_F)||_p < ε，其中 ε>0 是预设的容忍误差。模型代表 G(θ_F) 通过 M-估计量确定，检验统计量为经验分布函数与估计模型分布函数之间的 L^p 距离。作者给出了两种一致且易于实现的 bootstrap 方案来执行检验，并量化了所提模型相对于无信息常数基准的百分比改进。模拟研究和真实数据分析展示了方法的性能。该工作将经典拟合优度检验从“点零假设”推广到“区间零假设”，更贴近实际应用中模型近似可接受的需求。
- **关键技术**: `goodness-of-fit test`, `L^p distance`, `bootstrap`, `M-estimation`, `empirical distribution function`
- **为什么对您有用**: 本文直接关联您对假设检验的兴趣，特别是将经典拟合优度检验推广到“几乎拟合”的区间假设，这在实践中比精确零假设更合理。您武器库中非常熟悉的非参数统计和 M-估计理论可直接用于理解其 bootstrap 方案的一致性证明。中期可做：若想将类似“几乎拟合”思路推广到高维或因果推断设定，需先在 moderately_familiar 的 semiparametric theory 上加强。

### 2. [10.1007/s11222-025-10751-2](https://doi.org/10.1007/s11222-025-10751-2) · [arXiv](https://arxiv.org/abs/2407.08599) — Goodness of fit in relational event models
- **作者**: Martina Boschi, Ernst C. Wit
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对关系事件模型（REM）的拟合优度检验问题，提出了一种基于加权鞅残差的通用框架。REM 用于建模随时间变化的、由节点间交互构成的事件序列，其拟合评估长期依赖计算密集的模拟-比较方法。作者聚焦于 Kolmogorov-Smirnov 型检验及其多元扩展，通过构造加权鞅残差来检验协变量是否准确刻画了网络动态。模拟实验评估了检验的势和覆盖概率，并在一个包含 57,791 封邮件的波兰公司员工社交网络数据集上进行了实证应用。该方法已实现为 R 包。对您而言，本文的假设检验框架（尤其是基于鞅的残差分析）与您对 hypothesis testing 和 longitudinal/causal inference 的兴趣直接相关，其加权残差构造思路可能迁移到因果推断中的模型诊断。
- **关键技术**: `weighted martingale residuals`, `Kolmogorov-Smirnov type test`, `relational event model`, `multivariate extensions`, `simulation-based power analysis`
- **为什么对您有用**: 本文属于 hypothesis testing 方向，直接对应您的 primary interest。其加权鞅残差方法为 REM 这类复杂时序模型提供了计算可行的拟合优度检验，您可以用 very_familiar 的非参数统计和 high-dimensional asymptotics 工具来理解其渐近性质，并评估其检验势的 minimax 最优性。中期可做：若想将类似残差框架推广到因果推断中的时序模型（如 longitudinal 的 g-formula 诊断），需先在 moderately_familiar 的 M-estimation theory 上加强，以处理估计方程带来的额外变异性。

## 统计计算 / 算法  *(stat_computing, 15 篇)*

### 1. [10.1007/s11222-025-10764-x](https://doi.org/10.1007/s11222-025-10764-x) · [arXiv](https://arxiv.org/abs/2308.10081) — Transporting higher-order quadrature rules - Quasi-Monte Carlo points and sparse grids for mixture distributions
- **作者**: Ilja Klebanov, T. J. Sullivan
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究如何将高维概率分布上的积分/采样问题转化为对简单参考分布的积分，核心工具是传输映射（transport map）。作者提出将传输映射不仅应用于随机样本，还应用于拟蒙特卡洛点、高阶网和稀疏网格，使得变换后的样本继承原始方法优于 N^{-1/2} 的收敛速率。主要贡献是针对目标分布为混合分布（如高斯混合）的情形，推导出显式的传输映射，其计算只需解一个右端项为闭式的常微分方程。该映射可直接用于从混合分布中采样，且采样步骤的收敛速率优于 N^{-1/2}。这一结果对许多先以混合近似目标分布、再从中采样的方法（如重要性重加权）具有直接改进意义。对您而言，本文属于统计计算中的数值积分与采样方法，与您的 statistical computing 兴趣直接相关，且其传输映射的显式构造思路可能为您的软件开发和数值方法工作提供新工具。
- **关键技术**: `transport map`, `quasi-Monte Carlo`, `sparse grids`, `mixture distributions`, `ODE-based sampling`
- **为什么对您有用**: 本文属于 statistical computing 方向，直接对应您的 primary interest 中的统计计算（数值方法与算法）。您的 technical arsenal 中 very_familiar 的软件开发和 inverse problems 经验可用于实现本文的传输映射 ODE 求解器，并评估其数值稳定性与效率。中期可做：若您希望将本文的 QMC 传输思路推广到更一般的非混合目标分布，需先在 moderately_familiar 的 M-estimation theory 上加强，以处理传输映射的估计误差与收敛性分析。

### 2. [10.1007/s11222-025-10779-4](https://doi.org/10.1007/s11222-025-10779-4) · [arXiv](https://arxiv.org/abs/2504.09509) — Optimal sparse phase retrieval via a quasi-Bayesian approach
- **作者**: The Tien Mai
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究稀疏相位恢复问题，目标是从仅含幅值的线性变换观测中重建稀疏信号。作者提出一种准贝叶斯方法，使用缩放的学生 t 分布作为连续收缩先验来诱导稀疏性，并利用 PAC-Bayes 不等式框架给出首次理论保证。在亚指数噪声下，所提贝叶斯估计量达到了极小极大最优收敛速率，与最先进的频率学派方法匹配。为降低计算负担，设计了高效的 Langevin Monte Carlo 采样算法。数值实验表明该方法在噪声环境下与现有频率学派方法性能相当。对您而言，该工作展示了贝叶斯方法在逆问题中达到 minimax 最优率的可能性，其 PAC-Bayes 分析工具和 Langevin 采样策略可迁移至高维统计推断或因果推断中的计算问题。
- **关键技术**: `PAC-Bayesian inequality`, `Langevin Monte Carlo`, `scaled Student's t-prior`, `minimax optimal rate`, `sparse phase retrieval`
- **为什么对您有用**: 本文属于统计计算与高维逆问题的交叉，直接关联您对 inverse problems with random noise 和 minimax bounds 的熟悉领域。其 PAC-Bayes 分析框架和 Langevin 采样算法可视为您武器库中 'inverse problems with random noise' 和 'software development' 的延伸应用——您可以用 minimax 下界技术验证其收敛率是否紧，也可将 Langevin 采样思路移植到因果推断中的高维参数估计。中期可做：需先在 moderately_familiar 的 'M-estimation theory' 上加深对 PAC-Bayes 与经验过程关系的理解，然后可尝试将类似先验用于高维 IV 或 proximal CI 中的稀疏结构学习。

### 3. [10.1007/s11222-025-10780-x](https://doi.org/10.1007/s11222-025-10780-x) — Sequential Sample Average Majorization–Minimization
- **作者**: Gersende Fort, Florence Forbes, Hien Duy Nguyen
- **期刊/来源**: Statistics and Computing
- **机构**: Centre National de la Recherche Scientifique · Université Toulouse III - Paul Sabatier · Université Fédérale de Toulouse Midi-Pyrénées · Laboratoire d'Analyse et d'Architecture des Systèmes · Institut National des Sciences Appliquées de Toulouse · Toulouse Mathematics Institute · Institut de Mathématiques de Toulouse · Institut polytechnique de Grenoble 等
- **分类**: vol 36 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出一种新的随机 MM 算法 SAM2，用于求解期望泛函的优化问题。传统 SAA 方法需同时使用全部 N 个观测，在大数据或流数据场景下不可行。SAM2 通过顺序使用数据子集构建 SAA 形式的 majorizer，避免了凸性、光滑性或函数类限制。理论收敛性基于新提出的双数组一致强大数定律。数值实验展示了 SAM2 在分位数回归（含凸与非凸目标函数）上的表现。该算法为统计计算中大规模优化提供了实用工具。
- **关键技术**: `Majorization-Minimization (MM) algorithm`, `Sample Average Approximation (SAA)`, `double array uniform strong law of large numbers`, `stochastic optimization`, `quantile regression`
- **为什么对您有用**: 本文属于统计计算方向，直接对应 primary interest 中的 statistical computing。SAM2 算法不依赖凸性假设，与您熟悉的非参数统计和 M-估计理论有技术交集。该文可作为 gateway reading，帮助您了解随机 MM 框架；武器库中的 minimax bounds 和 high-dimensional asymptotics 可用于分析其收敛速率。中期可做：若想深入，需先在 moderately_familiar 的 M-估计理论上加强。

### 4. [10.1007/s11222-025-10753-0](https://doi.org/10.1007/s11222-025-10753-0) · [arXiv](https://arxiv.org/abs/2501.07668) — Fast sampling and model selection for Bayesian mixture models
- **作者**: M. E. J. Newman
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究贝叶斯混合模型的估计问题，主张直接对组件分配（component assignments）的边缘后验进行采样，而非传统的从组件和参数的联合后验进行Gibbs采样。作者指出，先前文献认为前一种方法混合慢，但本文证明若实现得当，其性能可以非常优秀。具体地，提出一种新的蒙特卡洛算法，利用从组件分配先验的无拒绝采样（rejection-free sampling）来实现优异的混合时间，在典型应用中显著优于标准Gibbs采样。方法适用于一般可积混合模型，并在高斯、泊松模型及潜类分析中展示了应用。对您而言，本文属于统计计算方向，展示了如何通过算法设计（无拒绝采样）提升MCMC效率，与您的统计计算兴趣直接相关，可作为了解高效采样技术的入门读物。
- **关键技术**: `rejection-free sampling`, `marginal posterior sampling`, `Gibbs sampling`, `Monte Carlo algorithm`, `mixture models`
- **为什么对您有用**: 本文属于统计计算方向，与您的primary interest中的统计计算（numerical methods, algorithm）直接相关。您武器库中的软件开发和M-estimation理论可用于理解其算法实现和收敛性分析。本文是gateway-reading，适合作为了解高效MCMC采样技术的入门，值得花时间读全文以获取算法设计思路。

### 5. [10.1007/s11222-025-10736-1](https://doi.org/10.1007/s11222-025-10736-1) · [arXiv](https://arxiv.org/abs/2403.12793) — Importance sampling for rare event tracking within the ensemble Kalman filtering framework
- **作者**: Nadhir Ben Rached, Erik von Schwerin, Gaukhar Shaimerdenova, Raúl Tempone
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文在集合卡尔曼滤波（EnKF）框架下，针对随机微分方程（SDE）解的运行最大值的小概率稀有事件跟踪问题，提出了一种重要性抽样（IS）后处理步骤。该方法不修改EnKF本身，而是利用当前观测时刻的集合来估计下一观测时刻前发生稀有事件的概率。作者提出了三种IS策略：对SDE初始条件进行IS、通过随机最优控制公式对Wiener过程进行IS、以及两者结合的IS。这些策略都需要近似求解带边界条件的Kolmogorov后向方程（KBE）；在高维情形下，采用马尔可夫投影降维技术将KBE近似为一维PDE来求解。在Double Well SDE、Langevin动力学和带噪声的Charney-deVore模型三个算例上，该方法相比标准Monte Carlo和另一种基于抽样的IS技术（多层交叉熵）实现了显著的方差缩减。本文属于统计计算中稀有事件模拟与数据同化的交叉，其降维思路和IS框架对您在高维统计计算和软件实现方面的兴趣有参考价值。
- **关键技术**: `importance sampling`, `ensemble Kalman filter`, `stochastic optimal control`, `Kolmogorov backward equation`, `Markovian projection dimension reduction`
- **为什么对您有用**: 本文属于统计计算（稀有事件模拟与数据同化）方向，是您secondary interest中的gateway-reading范畴。文章清晰阐述了问题设定（EnKF框架下跟踪SDE运行最大值的稀有事件概率）、数据侧（集合近似与观测时间点）和模型侧（SDE、KBE、最优控制），对统计计算领域的入门者友好。您的武器库中'软件开发和逆问题'可直接用于复现或扩展其降维方法，但核心的随机最优控制与PDE求解工具不在当前武器库中（属于moderately_familiar之外），因此暂不可做直接follow-up，但值得作为了解EnKF与稀有事件结合方法的入门读物。

### 6. [10.1007/s11222-025-10797-2](https://doi.org/10.1007/s11222-025-10797-2) · [arXiv](https://arxiv.org/abs/2402.14390) — Composite likelihood inference for the Poisson log-normal model
- **作者**: Julien Stoehr, Stéphane Robin
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对 Poisson log-normal 模型（一种处理多元计数数据的潜变量模型）的参数推断问题。该模型的难点在于给定观测数据后潜变量的条件分布不可处理，导致极大似然估计难以直接计算。现有方法中，变分推断计算快但缺乏理论保证，而采样方法（如 MCMC）理论性质好但计算代价高，尤其在高维潜变量空间中。作者首先提出一个 Monte Carlo EM 算法，能实现极大似然估计，但仅适用于低维潜变量。然后提出一种新推断流程，将 EM 框架与 composite likelihood 和重要性采样估计结合。该算法保留了极大似然估计的渐近性质（如一致性、渐近正态性），同时通过 composite likelihood 避免高维积分瓶颈，从而在中等规模数据集上保持计算可行性。该方法支持参数估计、置信区间和假设检验。在 Barents Sea 鱼类数据集上的应用展示了算法识别显著环境效应和残差种间相关性的能力。对您而言，本文的 composite likelihood + importance sampling 策略是处理高维潜变量模型的一种实用计算技巧，与您的统计计算兴趣（数值方法、算法）直接相关，可作为处理类似不可处理似然问题的参考范例。
- **关键技术**: `Monte Carlo EM`, `composite likelihood`, `importance sampling`, `Poisson log-normal model`, `latent variable model`
- **为什么对您有用**: 本文属于统计计算（stat_computing）方向，直接对应您的 primary interest 中的“statistical computing (numerical methods, algorithm)”。文中 composite likelihood 与 importance sampling 的结合策略，是处理高维潜变量模型积分瓶颈的实用技巧，您可以用 very_familiar 的“软件开发和算法实现”能力快速复现或扩展该方法。中期可做：若想将类似策略推广到更复杂的因果推断模型（如 proximal CI 中的高维 nuisance 函数），需先在 moderately_familiar 的“identification theory in causal inference”上加强。

### 7. [10.1007/s11222-025-10791-8](https://doi.org/10.1007/s11222-025-10791-8) · [arXiv](https://arxiv.org/abs/2407.13402) — Block-Additive Gaussian Processes under Monotonicity Constraints
- **作者**: Mathis Deronzier, Andrés F. López-Lopera, François Bachoc, Olivier Roustant, Jérémy Rohmer
- **期刊/来源**: Statistics and Computing
- **机构**: Université Toulouse III - Paul Sabatier · Institut National des Sciences Appliquées de Toulouse · Institut de Mathématiques de Toulouse · Université Polytechnique Hauts-de-France · Bureau de Recherches Géologiques et Minières
- **分类**: vol 36 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文在加性约束高斯过程框架下引入块加性结构，以处理输入变量间的交互作用，同时在整个输入空间上强制执行单调性约束。模型通过将输入变量分组为块，在块内允许交互而块间保持加性，从而在保持计算可处理性的同时扩展了表达能力。作者开发了MaxMod序贯算法用于模型选择，包括活跃输入变量和块结构的自动选择，并通过高效的矩阵计算和显式表达式加速了算法实现。数值实验展示了方法在高达120维的合成数据以及5维真实海岸洪水应用中的可扩展性和可解释性。该方法在统计计算与高斯过程建模的交汇处提供了实用的工具，尤其适合高维且需保持单调性的场景。
- **关键技术**: `block-additive Gaussian process`, `monotonicity constraints`, `MaxMod sequential algorithm`, `matrix computations`
- **为什么对您有用**: 本文属于统计计算方向，与您的primary interest中的统计计算（数值方法、算法）直接相关。您武器库中的非参数统计和高维渐近工具可用于分析该块加性GP的逼近误差和模型选择一致性，而您对软件开发的熟悉度可帮助您将MaxMod算法实现为可复用的R/Python包。中期可做：若想深入理论（如块结构可识别性），需先在M估计理论上加强。

### 8. [10.1007/s11222-025-10771-y](https://doi.org/10.1007/s11222-025-10771-y) · [arXiv](https://arxiv.org/abs/2407.16299) — Sparse outlier-robust PCA for multi-source data
- **作者**: Patricia Puchhammer, Ines Wilms, Peter Filzmoser
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对多源数据（multi-source data）提出一种稀疏且抗离群值的主成分分析（PCA）方法。现有稀疏鲁棒PCA方法大多针对单一数据源，而多源数据（如多个相关数据集需联合分析）在众多科学领域普遍存在。该方法通过一个正则化问题同时实现三个目标：(i) 选择重要特征，(ii) 检测跨数据源的全局稀疏模式以及各数据源特有的局部模式，(iii) 抵抗离群值干扰。核心机制是使用一种鲁棒协方差估计量（ssMRCD）作为插件，并设计一个能容纳全局-局部结构化稀疏模式的惩罚项。算法实现采用交替方向乘子法（ADMM），保证了计算效率。模拟和实际应用展示了该方法的实用优势。对您而言，本文属于统计计算（statistical computing）方向的算法贡献，其ADMM实现和结构化稀疏惩罚的设计思路，可迁移至您在高维统计或因果推断中处理多源异构数据时的降维与稳健估计问题。
- **关键技术**: `sparse PCA`, `outlier-robust covariance estimation`, `ssMRCD`, `global-local structured sparsity`, `alternating direction method of multipliers (ADMM)`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的primary interest中的'statistical computing (numerical methods, algorithm)'。其ADMM算法实现和结构化稀疏惩罚的设计，是您'very_familiar'的'软件开发和'high-dimensional asymptotics'工具可以攻克的——您可以用自己的高维统计知识验证其稀疏恢复的理论性质，或将其ADMM框架推广到因果推断中的高维协变量选择问题。**中期可做**：需先在'moderately_familiar'的'M-estimation theory'上长肌肉，以严格分析其惩罚估计量的相合性。

### 9. [10.1007/s11222-025-10789-2](https://doi.org/10.1007/s11222-025-10789-2) · [arXiv](https://arxiv.org/abs/2507.10945) — Scalable variational inference for multinomial probit models under large choice sets and sample sizes
- **作者**: Gyeongjun Kim, Yeseul Kang, Lucas Kock, Prateek Bansal, Keemin Sohn
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 该论文针对多项 probit (MNP) 模型在大选择集和大样本下的计算瓶颈，提出了一种可扩展的条件变分推断 (CVI) 方法。传统基于似然或 MCMC 的估计器在高维选择设定下计算成本极高。作者利用神经嵌入定义潜效用的灵活变分分布，并通过重参数化技巧保证协方差矩阵的正定性。CVI 估计器结构类似于变分自编码器，其中变分模型为编码器，MNP 数据生成过程为解码器。为处理 'argmax' 操作，采用了直通估计和 Gumbel-SoftMax 近似，从而避免从高维截断正态分布中采样，大幅降低了随选择项数量增长的计算成本。实验表明，在 20 个选择项和 100 万观测样本下，该方法约 28 分钟即可完成校准，比现有基准快约 36 倍，且点估计精度与 MCMC 后验均值接近。虽然主要面向高效点估计，但通过自助法也可进行有效的统计推断。该工作对您作为统计计算方向的研究者具有直接参考价值，尤其是其处理高维离散选择模型的计算策略，可启发您开发更高效的算法。
- **关键技术**: `conditional variational inference`, `neural embeddings`, `reparameterization trick`, `straight-through estimation`, `Gumbel-SoftMax approximation`, `variational autoencoder`
- **为什么对您有用**: 本文直接对应您的 primary interest 中的 'statistical computing (numerical methods, algorithm)'，属于计算方法的实质性贡献。您武器库中 'very_familiar' 的 'software development' 和 'high-dimensional asymptotics' 可用于分析其变分推断的收敛性，而 'moderately_familiar' 的 'M-estimation theory' 可帮助评估其变分目标函数的理论性质。**中期可做**：若您先提升 'moderately_familiar' 中的 'semiparametric theory' 以理解变分推断的渐近效率，则可进一步探索该方法在因果推断中处理多值处理变量的扩展。

### 10. [10.1007/s11222-025-10781-w](https://doi.org/10.1007/s11222-025-10781-w) · [arXiv](https://arxiv.org/abs/2502.04938) — A note on auxiliary mixture sampling for Bayesian Poisson models
- **作者**: Aldo Gardini, Fedele Greco, Carlo Trivisano
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 3/10 · novelty: `minor`
- **摘要**: 本文针对贝叶斯泊松分层模型的辅助混合抽样算法，系统分析了其高斯混合近似步骤的精度问题。该算法通过两步数据增广——先利用泊松过程理论，再用高斯混合近似残差分布——实现近似Gibbs采样。作者指出，在某些参数设置下，标准混合近似无法准确刻画真实分布，导致算法不收敛。他们提出了鲁棒版本，包括检测近似失效的机制、对辅助变量右尾的增强近似，以及必要时引入Metropolis-Hastings校正步骤。模拟和真实数据实验验证了改进算法的有效性。对您而言，本文属于统计计算中MCMC算法设计的实用工作，与您对统计计算（数值方法、算法）的兴趣直接相关，可作为了解贝叶斯计算中数据增广与近似策略的入门参考。
- **关键技术**: `auxiliary mixture sampling`, `data augmentation`, `Gaussian mixture approximation`, `Metropolis-Hastings correction`, `latent Gaussian models`, `Gibbs sampling`
- **为什么对您有用**: 本文属于统计计算中MCMC算法设计的实用工作，直接对应您primary interest中的统计计算（数值方法、算法）。您武器库中的软件开发和M-estimation理论虽不直接用于贝叶斯抽样，但本文对近似精度和收敛诊断的讨论，可作为您进入贝叶斯计算方向的gateway reading——武器库足以理解其核心思想，但若想深入改进算法，需在MCMC理论（moderately_familiar之外）上补课。值得花时间读全文，尤其关注其近似失效检测机制。

### 11. [10.1007/s11222-025-10777-6](https://doi.org/10.1007/s11222-025-10777-6) · [arXiv](https://arxiv.org/abs/2410.13261) — Novel Bayesian algorithms for ARFIMA long-memory processes: a comparison between MCMC and ABC approaches
- **作者**: James Cohen Gabor, Clara Grazian
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 3/10 · novelty: `minor`
- **摘要**: 本文比较了两种贝叶斯方法（MCMC 和 ABC）用于估计 ARFIMA 长记忆时间序列模型的参数。提出了一种新的 MCMC 算法，将时间序列分解为长记忆和 ARMA 分量分别滤波，并与标准方法对比。同时提出了一种新的 ABC 方法，使用三种不同的汇总统计量进行后验估计。通过广泛的模拟研究和实际金融数据集（美国季度 GNP）验证了方法的有效性。结果显示滤波 MCMC 在多个指标上表现更优。该研究增进了对贝叶斯技术在 ARFIMA 建模中优势与局限的理解。对您而言，本文属于统计计算中的算法比较研究，与您的 statistical computing 兴趣相关，但方法学新颖性有限。
- **关键技术**: `Markov Chain Monte Carlo`, `Approximate Bayesian Computation`, `ARFIMA model`, `summary statistics`
- **为什么对您有用**: 本文属于统计计算中的算法比较研究，与您的 statistical computing 兴趣相关。但方法学新颖性有限，主要是现有方法的组合与比较。武器库中的软件开发和 M-estimation 理论可帮助评估其算法效率，但核心问题（长记忆时间序列）与您的主要兴趣方向（因果推断、高维统计）距离较远。暂不可做：缺乏与您核心兴趣的直接连接。

### 12. [10.1007/s11222-025-10768-7](https://doi.org/10.1007/s11222-025-10768-7) · [arXiv](https://arxiv.org/abs/2502.03920) — Unbiased parameter estimation for bayesian inverse problems
- **作者**: Neil K. Chada, Ajay Jasra, Mohamed Maama, Raul Tempone
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究贝叶斯逆问题中未知参数的无偏估计。核心挑战在于：微分方程解的数值近似误差、边际似然及其梯度的解析不可处理性，导致传统估计存在偏差。作者基于 Awadelkarim et al. (2024) 对部分观测扩散过程的无偏参数估计思想，提出了一种新方法，能够产生在期望上等于边际似然最大化值的随机估计量，且不含数值近似误差。方法的关键在于通过随机化技巧消除离散化偏差，并利用耦合马尔可夫链实现无偏估计。理论部分证明了估计量的无偏性，数值实验表明该方法在 PDE 和 ODE 逆问题中比现有最先进方法更快。对您而言，本文属于统计计算方向，其无偏化技巧（随机化消除离散偏差）与您熟悉的逆问题随机噪声设定有直接关联，可作为 gateway reading 了解贝叶斯逆问题中的计算 tradeoff。
- **关键技术**: `unbiased estimation`, `randomized multilevel Monte Carlo`, `coupled Markov chains`, `Bayesian inverse problems`, `marginal likelihood maximization`
- **为什么对您有用**: 本文属于统计计算方向，与您的 primary interest 中 'statistical computing (numerical methods, algorithm)' 直接相关。其核心技巧——通过随机化消除数值离散化偏差——可视为一种 'computational-statistical tradeoff' 的实例：用随机性换取无偏性，但可能增加方差。您武器库中 'inverse problems with random noise' 和 'high-dimensional asymptotics' 可用于分析该方法的收敛速度与方差行为。**中期可做**：需先在 'semiparametric theory' 上长肌肉，以理解其无偏估计量的效率损失与半参数效率界的关系。

### 13. [10.1007/s11222-025-10763-y](https://doi.org/10.1007/s11222-025-10763-y) — BOB: Bayesian optimized bootstrap for approximate posterior sampling in Gaussian mixture models
- **作者**: Santiago Marin, Bronwyn Loong, Anton H. Westveld
- **期刊/来源**: Statistics and Computing
- **机构**: Australian National University · Virginia Commonwealth University
- **分类**: vol 36 · issue 1
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对高斯混合模型（GMM）的贝叶斯后验采样问题，提出了一种名为BOB（Bayesian Optimized Bootstrap）的计算方法。标准MCMC在GMM后验采样中面临计算挑战，而加权似然bootstrap和加权贝叶斯bootstrap作为替代方案，其核心是反复从随机加权的后验密度中计算MAP估计，但随机权重的选择问题尚未解决。BOB通过贝叶斯优化自动调整这些随机权重，最小化真实后验与近似后验之间的反向KL散度（黑箱、带噪声）。该方法在恢复贝叶斯后验方面优于现有方法，并保留了关键渐近性质。模拟和真实数据分析验证了其性能。对您而言，本文属于统计计算方向，涉及bootstrap和优化方法，与您的统计计算兴趣相关，但方法学新颖性有限，属于应用性改进。
- **关键技术**: `Bayesian optimization`, `weighted likelihood bootstrap`, `weighted Bayesian bootstrap`, `reverse KL divergence`, `Gaussian mixture models`
- **为什么对您有用**: 本文属于统计计算方向，与您的primary interest中的统计计算（numerical methods, algorithm）直接相关。您武器库中的软件开发和M-estimation理论可用于复现或扩展其优化框架，但核心的贝叶斯优化工具您不熟悉，属于暂不可做。

### 14. [10.1007/s11222-025-10724-5](https://doi.org/10.1007/s11222-025-10724-5) · [arXiv](https://arxiv.org/abs/2312.15256) — Adaptive Reduced Multilevel Splitting
- **作者**: Frédéric Cérou, Patrick Héas, Mathias Rousset
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究稀有事件（rare event）的蒙特卡洛采样问题，目标分布由计算代价极高的得分函数定义。作者假设可以构建一个带有误差界的近似替代得分函数，并提出一种完全自适应的算法，通过逐步采样替代稀有事件分布来逼近目标。核心贡献在于每步迭代中，算法根据替代得分及其误差界自动确定一个临界水平（critical level），该水平对应一个与目标重要性采样相关的特定成本。从方法上看，该工作将流行的自适应多层分裂（adaptive multilevel splitting）算法扩展到使用得分近似的情形，实现了序列化采样。数值实验以计算复杂度与均方误差的权衡为指标，评估了所提重要性采样算法的性能。特别地，作者在参数化PDE解的稀有事件模拟中验证了算法，其中PDE解由缩减基（reduced basis）近似。对您而言，本文的“自适应替代模型+稀有事件采样”框架与您统计计算（numerical methods, algorithm）兴趣直接相关，其误差界驱动的自适应策略可能启发您在因果推断或高维统计中处理计算昂贵的目标函数。
- **关键技术**: `adaptive multilevel splitting`, `importance sampling`, `surrogate score with error bounds`, `reduced basis approximation`, `critical level selection`
- **为什么对您有用**: 本文属于统计计算（stat_computing）方向，是您primary interest中的gateway reading。它展示了如何用带误差界的替代模型自适应地加速稀有事件采样，这与您武器库中“inverse problems with random noise”和“software development”高度契合——您可以用熟悉的非参数统计或高维渐近工具分析其自适应策略的收敛性。中期可做：若想将类似框架迁移到因果推断中的敏感性分析（如稀有处理效应），需先在moderately_familiar的“identification theory in causal inference”上长肌肉。

### 15. [10.1007/s11222-025-10819-z](https://doi.org/10.1007/s11222-025-10819-z) · [arXiv](https://arxiv.org/abs/2509.00719) — Removal of redundant candidate points for the exact D-optimal design problem
- **作者**: Radoslav Harman, Samuel Rosa
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究线性或局部线性模型在大型有限候选集上的精确 D-最优设计问题。精确 D-最优设计是一个整数优化问题，计算难度远高于近似 D-最优设计。作者提出基于近似设计的必要条件，任何 D-最优精确设计的支撑点都必须满足该条件，从而可以快速剔除冗余候选点而不损失最优性。该方法能大幅缩减候选集规模（实验显示可降低数个数量级），进而使混合整数二阶锥规划（MISOCP）能够求解并给出最优性保证。理论部分还证明，当试验次数足够大时，精确 D-最优设计的支撑集包含在近似 D-最优设计的支撑集中。该方法在候选点达 1 亿的随机生成基准模型和 100 万点的约束混合模型上得到验证。对您而言，本文展示了如何用近似问题的解来剪枝精确优化问题，这种思路可迁移到您熟悉的统计计算中的算法加速问题。
- **关键技术**: `exact D-optimal design`, `approximate design`, `mixed-integer second-order cone programming (MISOCP)`, `redundant candidate point elimination`, `support point necessary condition`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的 primary interest 中的 statistical computing。您非常熟悉的软件开发和算法设计技能可直接用于复现或扩展其剪枝思路。中期可做：将近似解剪枝精确优化的思想迁移到您 moderately_familiar 的 HOIF 或 U-statistics 计算中，例如用低阶影响函数剪枝高阶影响函数的计算图。

## 流行病学  *(epidemiology, 1 篇)*

### 1. [10.1007/s11222-025-10756-x](https://doi.org/10.1007/s11222-025-10756-x) · [arXiv](https://arxiv.org/abs/2410.09552) — Model-based clustering of time-dependent observations with common structural changes
- **作者**: Riccardo Corradin, Luca Danese, Wasiur R. KhudaBukhsh, Andrea Ongaro
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文提出一种基于模型的时间序列聚类方法，核心假设是：若两条时间序列的结构变化发生在同一时刻，则它们属于同一组。方法利用随机序（random orders）对每条序列的结构变化点进行潜在表示，并通过诱导不同观测之间的联结（ties）实现聚类。该策略具有一般性，可与多种已知的时间依赖模型结合。研究动机来自流行病学问题：对欧盟国家的新冠病毒传播过程进行聚类，使得传播过程结构变化时间一致的国家归为一类。方法学上，本文属于应用导向的建模创新，并未提供新的理论收敛性或效率结果。对您而言，本文可作为流行病学中时间序列聚类的一个具体案例，但其方法学新颖性有限，主要价值在于应用场景和建模思路。
- **关键技术**: `model-based clustering`, `random orders`, `structural change detection`, `time series clustering`
- **为什么对您有用**: 本文直接关联您的 secondary interest 中的流行病学应用，提供了一个具体的数据分析案例（COVID-19 传播过程的聚类）。然而，方法学上并未涉及您 primary interest 中的因果推断、高维统计或效率理论，且未提供理论保证（如聚类一致性）。作为 gateway reading，本文适合快速了解流行病学中时间序列聚类的常见问题设定，但武器库中的工具（如非参数统计、M估计理论）难以直接用于改进或扩展本文方法，因为核心建模思路（随机序诱导联结）与您的技术栈距离较远。因此，本文暂不可做，缺乏直接可迁移的方法学接口。

## 其他  *(other, 7 篇)*

### 1. [10.1007/s11222-025-10812-6](https://doi.org/10.1007/s11222-025-10812-6) · [arXiv](https://arxiv.org/abs/2412.15293) — The Group R2D2 Shrinkage Prior for Sparse Linear Models with Grouped Covariates
- **作者**: Eric Yanchenko, Kaoru Irie, Shonosuke Sugasawa
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出一种名为 gR2D2 的贝叶斯收缩先验，用于处理具有分组结构的高维稀疏线性回归。该方法将 R2D2 先验扩展到分组变量选择场景，通过为每个组的决定系数（R²）赋予 Dirichlet 先验分布，实现组级别和变量级别的自适应收缩。作者推导了该先验的若干理论性质（如矩、收缩强度），并开发了相应的 MCMC 采样算法。模拟和真实数据分析表明，gR2D2 在估计精度、变量选择和预测方面优于传统的全局-局部收缩先验（如 Horseshoe、Regularized Horseshoe）以及组级先验（如 Group Horseshoe）。该工作属于贝叶斯高维回归的方法论贡献，但核心工具（Dirichlet 分解、MCMC）与您的主要兴趣方向（因果推断、半参效率、U-统计量）交集有限。
- **关键技术**: `R2D2 prior`, `Dirichlet decomposition`, `group-level shrinkage`, `Markov Chain Monte Carlo`, `global-local shrinkage priors`
- **为什么对您有用**: 本文属于贝叶斯高维统计计算的方法学论文，与您的主要兴趣方向（因果推断、半参理论、U-统计量）无直接关联。您的武器库中 very_familiar 的高维渐近理论可用来评估其收缩先验的 minimax 最优性，但该文未涉及因果识别或效率理论。作为统计计算方向的 gateway reading，它展示了如何将 R2D2 先验扩展到分组结构，但 MCMC 实现本身不涉及您关注的 tensor-contraction 或 einsum 复杂度。**暂不可做**：核心机器（贝叶斯分层模型、MCMC 收敛诊断）不在您的武器库中，且缺乏与您主要兴趣的明确连接点。

### 2. [10.1007/s11222-025-10758-9](https://doi.org/10.1007/s11222-025-10758-9) · [arXiv](https://arxiv.org/abs/2409.03181) — Wrapped Gaussian Process Functional Regression Model for Batch Data on Riemannian Manifolds
- **作者**: Jinzhao Liu, Chao Liu, Jian Qing Shi, Tom Nye
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出一种针对黎曼流形上批次数据的并发函数回归模型，响应变量服从 wrapped Gaussian 分布，协变量可为函数型或标量。模型同时估计均值结构与协方差结构，以捕捉流形值响应与欧氏协变量间的非线性关系。估计方法基于最大似然与高斯过程先验，计算上依赖数值优化。模拟与真实数据实验表明模型在流形回归任务中有效。该文属于非欧空间统计建模，与您的主要兴趣（因果推断、高维统计、U-统计量）无直接交集。
- **关键技术**: `wrapped Gaussian distribution`, `Gaussian process regression`, `functional data analysis`, `Riemannian manifolds`
- **为什么对您有用**: 本文属于流形上的函数回归，与您的主要兴趣方向（因果推断、高维统计、U-统计量）无直接技术交集。武器库中无流形统计或 wrapped 分布相关工具，暂不可做。若您未来考虑进入流形数据分析方向，本文可作为入门阅读，但当前优先级低。

### 3. [10.1007/s11222-025-10810-8](https://doi.org/10.1007/s11222-025-10810-8) · [arXiv](https://arxiv.org/abs/2111.07840) — Bayesian modelling and computation utilising directed cycles in multiple network data
- **作者**: Anastasia Mantziou, Sally A. Keith, David M. P. Jacoby, Simón Lunagómez, Robin Mitra
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文提出一种贝叶斯建模与计算方法，用于分析多个网络数据，核心创新在于引入有向环（directed cycles）作为网络距离度量，并将其嵌入球面网络族（Spherical Network Family, SNF）模型框架中。SNF模型允许任意度量，但此前难以显式捕捉环结构；作者定义了一种基于有向环相似性的新距离，使推断能直接反映竞争与层级交互等生态学中重要的网络模体。由于SNF模型似然函数难以处理，作者进一步开发了针对中等规模网络的后验计算框架，可能涉及MCMC或近似推断技术。方法应用于一组鱼类攻击性交互的生态网络数据，展示了模型在环行为推断上的优势，超越了不考虑环结构的模型。本文主要贡献在于提出一种新的网络距离度量并解决其计算可行性，属于应用驱动的统计计算创新。对您而言，本文与您的主要兴趣方向（因果推断、高维统计、U-统计量等）无直接技术重叠，但作为统计计算与生态网络应用的交叉案例，可作为gateway reading了解网络数据分析中的计算挑战。
- **关键技术**: `Spherical Network Family (SNF)`, `network distance metric`, `directed cycles`, `Bayesian inference`, `intractable likelihood`, `ecological network data`
- **为什么对您有用**: 本文属于统计计算与生态网络应用的交叉，可作为gateway reading：武器库中的'软件发展'和'非参数统计'能帮助理解其计算框架，但核心的SNF模型与环距离度量不在您的主要兴趣方向内，且缺乏与因果推断或高维统计的直接连接。暂不可做——核心机器（SNF模型、网络距离度量、生态网络推断）不在武器库中，且与您的primary interests无技术交集。

### 4. [10.1007/s11222-025-10790-9](https://doi.org/10.1007/s11222-025-10790-9) — Penalized distributed lag non-linear models for small area data using Laplacian-P-splines
- **作者**: Sara Rutten, Bryan Sumalinab, Oswaldo Gressani, Thomas Neyens, Elisa Duarte, Niel Hens et al.
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对空间参考数据中的分布式滞后非线性模型（DLNM），提出了一种贝叶斯DLNM-Laplacian-P-splines（DLNM-LPS）方法。该方法通过条件自回归（CAR）先验引入空间依赖性，解决了现有惩罚DLNM框架中空间依赖建模的空白。模型使用Laplace近似逼近回归参数的条件后验分布，避免了MCMC采样，显著提升了计算效率。模拟研究验证了方法的有效性，并应用于伦敦温度与死亡率关系的分析。该方法在空间流行病学中具有实用价值，但统计方法学创新有限，主要贡献在于计算实现。
- **关键技术**: `distributed lag non-linear models`, `conditional autoregressive priors`, `Laplacian-P-splines`, `Laplace approximation`, `Bayesian inference`
- **为什么对您有用**: 本文属于流行病学应用（温度-死亡率关系），但方法学上主要是贝叶斯空间建模的工程实现，与您的主要兴趣（因果推断、高维统计、U统计量）无直接交集。武器库中的非参数统计和软件工程经验可帮助理解其P-spline和Laplace近似部分，但核心问题（空间DLNM的识别与计算）并非您当前方向。作为流行病学入门阅读，本文数据结构和模型设定清晰，但统计深度不足以进入深度阅读。

### 5. [10.1007/s11222-025-10798-1](https://doi.org/10.1007/s11222-025-10798-1) · [arXiv](https://arxiv.org/abs/2408.07463) — A novel framework for quantifying nominal outlyingness
- **作者**: Efthymios Costa, Ioanna Papatsouma
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文针对名义型（nominal）数据的异常值检测问题，提出了一种新的离群度量化框架。核心思路是借鉴关联规则挖掘（association rule mining）中的概念，将名义变量的取值序列视为多项分布生成的随机事件，通过计算观测序列相对于期望模式的偏离程度来定义离群度。框架包括：基于频繁项集的支持度（support）和置信度（confidence）构建离群度评分函数；引入变量贡献（variable contributions）和离群深度（outlyingness depth）以增强可解释性；并给出了超参数（如最小支持度阈值）的选择方法。在合成数据和公开数据集上的实验表明，该方法与最先进的频繁模式挖掘算法性能相当，在某些场景下甚至更优。该工作主要面向数据挖掘和异常检测社区，方法学上属于应用导向的启发式框架，缺乏严格的统计推断理论（如渐近分布、检验水平控制等）。对您而言，本文与您的主要兴趣方向（因果推断、高维统计、U-统计量等）无直接技术交集，但若您未来涉足分类数据或离散型数据的异常检测应用，其关联规则思路可作参考。
- **关键技术**: `association rule mining`, `frequent pattern mining`, `multinomial distribution`, `outlier detection`, `nominal data`
- **为什么对您有用**: 本文属于数据挖掘领域的应用型工作，与您的主要兴趣方向（因果推断、高维统计、U-统计量、半参效率理论等）无直接技术关联。其方法缺乏严格的统计推断框架（如假设检验、渐近理论），且未涉及您武器库中的任何具体工具（如U-统计量投影、minimax界、影响函数等）。因此，本文暂不可做，核心机器（关联规则挖掘的启发式框架）不在您的武器库中，且该方向本身并非您的研究重点。若您仅作为泛读了解离散数据异常检测的常见思路，可快速浏览其框架定义和实验部分。

### 6. [10.1007/s11222-025-10767-8](https://doi.org/10.1007/s11222-025-10767-8) · [arXiv](https://arxiv.org/abs/2503.08821) — Questioning normality: A study of wavelet leaders distribution
- **作者**: Wejdene Ben Nasr, Hélène Halconruy, Stéphane Jaffard
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究小波领袖（wavelet leaders）的分布假设问题，这是应用多重分形分析中的基础工具。作者质疑了大多数贝叶斯估计方法中隐含的log-正态性假设，通过统计检验拒绝该假设后，提出了基于log-凹分布的更灵活模型。在经典随机过程（分数布朗运动、多重分形随机游走、Mandelbrot级联）和真实马拉松数据上验证了新模型。在log-正态性假设下，重新审视了第一阶标度指数c1和第二阶标度指数c2的估计程序，并给出了置信区间。最后，在随机小波级数框架下建立了log-领袖分布的理论结果。本文属于统计计算与信号处理交叉领域的方法学工作，对您而言，其核心价值在于展示了如何用假设检验驱动模型选择——这一思路可迁移到您熟悉的非参数统计和因果推断中的敏感性分析设定。
- **关键技术**: `wavelet leaders`, `multifractal analysis`, `log-concave distributions`, `hypothesis testing for distributional assumptions`, `confidence intervals for scaling exponents`
- **为什么对您有用**: 本文属于统计计算（stat_computing）方向，但并非您核心兴趣中的信息-计算权衡或张量网络复杂度。它展示了如何用假设检验驱动模型选择，这一思路可迁移到您熟悉的非参数统计和因果推断中的敏感性分析设定。武器库中'非参数统计'和'软件工程'可支撑您复现其方法并扩展到其他信号处理场景，但核心问题（多重分形分析）与您的主要兴趣方向距离较远，属于'暂不可做'——缺乏小波理论和多重分形领域的背景知识。

### 7. [10.1007/s11222-025-10772-x](https://doi.org/10.1007/s11222-025-10772-x) · [arXiv](https://arxiv.org/abs/2503.21443) — Sparse Bayesian learning for label efficiency in cardiac real-time MRI
- **作者**: Anja Bach, Achim Basermann, Darius A. Gerlach, Philipp Knechtges, Jens Tank, Raúl Tempone et al.
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 1
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文针对心脏实时MRI中外部切片分割标签稀缺的问题，提出稀疏贝叶斯学习（SBL）方法。假设心室容积时间序列由心脏和呼吸频率对应的稀疏频率主导，SBL通过type-II似然优化超参数，自动剪枝无关成分，从内切片中识别这些稀疏频率。利用识别出的稀疏频率指导外切片图像的标签选择，最小化后验方差，并提供了贪心算法的性能保证。在患者数据上验证，仅需少量标签即可准确预测容积，且标签选择有效避免了低效图像。贝叶斯框架还提供了不确定性估计，可标记不可靠预测。该方法本质上是贝叶斯变量选择与主动学习的结合，与您的主要兴趣（因果推断、高维统计、U统计量）无直接方法学关联，但可作为统计计算在医学影像中应用的案例参考。
- **关键技术**: `sparse Bayesian learning`, `type-II likelihood maximization`, `greedy algorithm`, `active learning`, `uncertainty quantification`
- **为什么对您有用**: 本文属于统计计算在医学影像中的应用，与您的主要兴趣（因果推断、高维统计、U统计量）无直接方法学连接。作为gateway reading，本文对统计计算方向有一定参考价值，但武器库中的工具（如非参数统计、高维渐近）难以直接攻入其核心机制（SBL的type-II似然优化与主动学习策略）。暂不可做——核心机器（贝叶斯变量选择与主动学习的理论分析）不在武器库中。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

