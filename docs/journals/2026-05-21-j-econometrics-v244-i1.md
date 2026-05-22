# J. Econometrics — Vol 244  Issue 1  ·  2026-05-21

- 共 16 篇 · Journal of Econometrics

## 因果推断  *(causal_inference, 6 篇)*

### 1. [10.1016/j.jeconom.2024.105856](https://doi.org/10.1016/j.jeconom.2024.105856) — Heterogeneous treatment effect bounds under sample selection with an application to the effects of social media on political polarization
- **作者**: Phillip Heiler
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 1 · pp 105856
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在无排除约束的样本选择模型下（处理影响结果是否可观测），本文研究异质性因果效应的局部识别与边界估计问题。方法将条件效应边界表示为政策相关前置变量的函数，从而允许对未识别的条件效应进行有效的统计推断。估计方面采用 debiased/double machine learning (DML) 框架，以适应非线性函数形式与高维混淆因子。理论上给出了易于验证的高层条件、抗模型误设的置信区间以及均匀置信带。实证重新分析了带有缺失的 Facebook 反态度新闻订阅实验，相比传统方法获得了更紧的效应边界，发现年轻用户存在去极化效应。对您有用：该文将 DML 推广至部分识别/样本选择下的边界估计，直接契合您对因果推断（样本选择/边界）与效率理论（DML/抗误设推断）的交叉兴趣。
- **关键技术**: `partial identification bounds`, `sample selection without exclusion restriction`, `debiased double machine learning`, `misspecification-robust inference`, `uniform confidence bands`
- **为什么对您有用**: 直接契合您对因果推断（无排除约束的样本选择与边界估计）和效率理论（DML 在部分识别下的应用及抗误设推断）的交叉兴趣，且提供了经济学因果应用的实证范式。

### 2. [10.1016/j.jeconom.2024.105854](https://doi.org/10.1016/j.jeconom.2024.105854) — Identification in discrete choice models with imperfect information
- **作者**: Cristina Gualdani, Shruti Sinha
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 1 · pp 105854
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在决策者对世界状态具有不完全信息的静态单主体离散选择模型中，研究偏好的识别问题，核心目标是刻画结构参数和反事实结果的 sharp identified set。引入 Bergemann and Morris (2016) 的单人 Bayes Correlated Equilibrium (BCE) 概念，为 sharp identified set 提供了易于处理的刻画。基于 sieve approach 开发了一种实际构造该 sharp identified set 的计算程序，并推导了反事实结果的 sharp bounds。该方法避免了传统离散选择模型中对信息结构的强分布假设，允许信息结构与未观测扰动任意相关。实证部分利用 2017 年英国大选数据估计了空间投票模型，量化了不完全信息对选民和政党福利的影响。对您有用：该文将 BCE 引入计量经济学识别问题，结合 sieve 方法构造 sharp bounds，为 causal inference 中的 partial identification 和放松假设的 sensitivity analysis 提供了新工具与经济数据应用范例。
- **关键技术**: `partial identification`, `Bayes Correlated Equilibrium`, `sharp identified set`, `sieve approach`, `discrete choice model`, `counterfactual bounds`
- **为什么对您有用**: 直接关联 causal inference 中的 identification 与 sensitivity analysis（放松不可检验的信息结构假设），同时使用了 semiparametric theory 中的 sieve approach 构造识别域，并在 economic theory 领域提供了真实选举数据集与空间投票模型的应用。

### 3. [10.1016/j.jeconom.2024.105846](https://doi.org/10.1016/j.jeconom.2024.105846) — A method of moments approach to asymptotically unbiased Synthetic Controls
- **作者**: Joseph Fry
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 1 · pp 105846
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在固定控制单元数量的合成控制（SC）设定下，传统基于预处理期结果拟合的 SC 估计量在拟合不完美时存在渐近偏差。本文提出一种基于广义矩估计（GMM）的 SC 构造方法，将未纳入合成控制组的单元作为工具变量（IV），利用其外生性构建矩条件。该方法在预处理期 $T_0 \to \infty$ 时，即使拟合不完美且控制单元数 $N$ 固定，处理效应估计量也能实现渐近无偏；若 $T_0$ 和 $T_1$ 同时趋于无穷，则可一致估计平均处理效应。模拟与实证表明该方法相比传统 SC 显著降低了偏差。对您有用：该文将 IV 排除约束引入 SC 框架解决固定 $N$ 下的渐近偏差问题，直接契合您对因果推断中 IV 方法与经济理论应用的关注，且 GMM 框架为后续效率理论探讨提供了接口。
- **关键技术**: `Synthetic Control`, `General Method of Moments`, `Instrumental Variables`, `Asymptotic Unbiasedness`, `Panel Data`
- **为什么对您有用**: 直接契合您对因果推断中 IV 方法以及经济理论中应用因果工作的关注；将 IV 排除约束引入 SC 解决固定 N 下的渐近偏差，为 SC 的识别与估计提供了新视角，且 GMM 框架便于后续探讨效率界。

### 4. [10.1016/j.jeconom.2024.105829](https://doi.org/10.1016/j.jeconom.2024.105829) — Tuning-parameter-free propensity score matching approach for causal inference under shape restriction
- **作者**: Yukun Liu, Jing Qin
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 1 · pp 105829
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在因果推断的倾向得分匹配（PSM）框架下，本文针对匹配数选择难题，在单调性形状约束下研究 ATE 的无调参估计。作者利用单调约束下的非参数极大似然估计（NPMLE）估计倾向得分，该估计具有分段常数形式，从而自动对数据进行分组，免去了传统 PSM 的带宽或匹配数选择。理论上，在一维协变量情形下，所提估计量达到了半参数有效界；在多维情形下，当结局与倾向得分对协变量的依赖方向一致时，该估计同样渐近有效。文章进一步证明，仅基于倾向得分的匹配方法在一般情形下无法达到半参数有效界。这对您有用：该文将形状约束下的 NPMLE 与半参数效率理论结合，为 PSM 的效率极限提供了精确刻画，直接契合您在因果推断与半参数效率界方面的核心兴趣，且其无调参分组机制对统计计算亦有启发。
- **关键技术**: `propensity score matching`, `nonparametric maximum likelihood estimation (NPMLE)`, `monotonicity constraint`, `semiparametric efficiency bound`, `piecewise constant estimation`
- **为什么对您有用**: 直接连接因果推断与半参数效率理论，证明纯 PS 匹配的效率极限并给出达到有效界的条件，契合您对 semiparametric efficiency bounds 和 causal inference 的核心关注；无调参的自动分组机制对统计计算也有参考价值。

### 5. [10.1016/j.jeconom.2024.105858](https://doi.org/10.1016/j.jeconom.2024.105858) — Identification and estimation of unconditional policy effects of an endogenous binary treatment: An unconditional MTE approach
- **作者**: Julian Martinez-Iriarte, Yixiao Sun
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 1 · pp 105858
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究内生二元处理下无条件政策效应的识别与估计，设定在边际处理效应（MTE）与工具变量（IV）框架下。核心创新是利用政策目标泛函的影响函数，定义了一类新的无条件边际处理效应（unconditional MTE）。理论证明，无条件政策效应可表示为新定义 MTE 在处理状态无差异个体上的加权平均，并给出了相应的点识别条件。针对分位数作为目标泛函的情形，作者提出了无条件工具变量分位数估计器（UNIQUE），并推导了其一致性与渐近正态性。实证部分评估了学费补贴对工资分布分位数的因果效应。对您有用：该文将影响函数引入 MTE 框架重新定义 estimand，直接连接了您关注的因果推断（IV/识别）与效率理论，且内生处理下的分位数推断方法对经济与流行病学应用均有迁移价值。
- **关键技术**: `marginal treatment effect (MTE)`, `influence function`, `instrumental variable`, `quantile treatment effect`, `asymptotic normality`, `point identification`
- **为什么对您有用**: 直接连接您关注的因果推断（IV/内生性）与效率理论（影响函数定义 estimand），且属于经济理论中的因果应用，UNIQUE 估计器的渐近理论对内生处理下的分位数推断有方法迁移价值。

### 6. [10.1016/j.jeconom.2024.105852](https://doi.org/10.1016/j.jeconom.2024.105852) — High-dimensional model-assisted inference for treatment effects with multi-valued treatments
- **作者**: Wenfu Xu, Zhiqiang Tan
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 1 · pp 105852
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维设定下研究多值处理的平均处理效应（ATE）估计，基于增广逆概率加权（AIPW）框架，关注结果回归与倾向得分模型可能误判时的推断有效性。提出正则化校准估计方法，在损失函数中引入稀疏惩罚（group Lasso）的同时，通过校准方程确保后续推断在模型误判下仍有效。针对多值处理推广了 AIPW 估计量，利用新校准方程实现参数的恰好识别，且倾向得分损失函数直接与处理组间的协变量平衡挂钩。计算上创新性地结合 Fisher scoring 与 group Lasso 实现高效求解，并在稀疏条件下给出了严格的高维理论分析。实证应用于母亲吸烟对婴儿出生体重的影响。对您有用：直接推进了高维因果推断中 AIPW 的效率理论与计算实现，校准思想与协变量平衡的连接对多值处理推断有重要启发。
- **关键技术**: `augmented IPW (AIPW)`, `regularized calibrated estimation`, `covariate balance`, `group Lasso`, `Fisher scoring`, `high-dimensional sparsity`
- **为什么对您有用**: 直接推进了您在因果推断（多值处理 ATE）与高维统计交叉领域的研究，其正则化校准方法在模型误判下仍保证有效推断，且 Fisher scoring + group Lasso 的算法实现及 R 包对您的统计计算兴趣有直接参考价值。

## 非参数 / 半参数  *(nonparam_semipara, 3 篇)*

### 1. [10.1016/j.jeconom.2024.105865](https://doi.org/10.1016/j.jeconom.2024.105865) — On uniform confidence intervals for the tail index and the extreme quantile
- **作者**: Yuya Sasaki, Yulong Wang
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 1 · pp 105865
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 本文研究局部非参数尾部分布族下尾部指数与极值分位数的均匀置信区间构造问题。首先，作者证明了在该非参数族中，构造同时满足长度最优与正确均匀覆盖的置信区间是不可能的。针对此不可能性结果，文章通过纳入局部非参数族内的最坏情形偏差，构建了具有均匀有效性的诚实置信区间。该方法基于极值理论与非参数偏差感知推断框架，并在模拟数据及美国国家卫生统计中心的真实数据上进行了验证。该文的不可行性定理与偏差感知推断思路，直接关联您关注的非参数理论与假设检验（均匀有效性）方向，提供了严谨的理论范例。
- **关键技术**: `uniform confidence intervals`, `impossibility result`, `honest inference`, `worst-case bias`, `extreme value theory`
- **为什么对您有用**: 证明了非参数尾部推断中均匀置信区间的不可行性，并给出基于最坏情形偏差的诚实区间，直接关联您关注的非参数理论与假设检验（均匀有效性）方向，提供了不可行性定理与偏差感知推断的严谨范例。

### 2. [10.1016/j.jeconom.2024.105849](https://doi.org/10.1016/j.jeconom.2024.105849) — Empirical risk minimization for time series: Nonparametric performance bounds for prediction
- **作者**: Christian Brownlees, Jordi Llorens-Terrazas
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 1 · pp 105849
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究时间序列经验风险最小化（ERM）的预测性质，设定为单变量 location-scale 参数驱动过程的 1 步向前预测，且可用算法类为递归形式（预测值依赖滞后预测与序列本身），不假设数据生成机制与算法类的特定关系。核心方法是在时间序列依赖结构下建立非参数性能界，证明由 ERM 选择的算法在给定递归算法类中渐近达到最优预测表现。技术工具涉及处理时间序列依赖的经验过程理论（如混合序列的收敛性）以及非参数 excess risk 的推导。主要理论结果保证了 ERM 估计量的 excess risk 渐近收敛至零，实现类内最优。对您有用：这为依赖数据下的非参数渐近理论提供了严格框架，可补充您在非参数/半参数理论及计量经济学应用中的理论工具箱。
- **关键技术**: `empirical risk minimization`, `nonparametric performance bounds`, `recursive forecasting algorithms`, `time series dependence`, `excess risk`
- **为什么对您有用**: 本文严格证明了依赖数据下 ERM 的渐近最优性，直接关联您 primary interest 中的非参数/半参数理论，同时其计量经济学设定也契合您 secondary interest 中的经济理论应用，收益在于获取时间序列非参数 excess risk 界的推导技巧。

### 3. [10.1016/j.jeconom.2024.105853](https://doi.org/10.1016/j.jeconom.2024.105853) — GMM estimation for high-dimensional panel data models
- **作者**: Tingting Cheng, Chaohua Dong, Jiti Gao, Oliver Linton
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 1 · pp 105853
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究带有交互效应的高维矩约束面板数据模型，其中因子不可观测且因子载荷是个体特征变量的非参数未知光滑函数，参数维度与矩条件数量随样本量发散。为估计未知参数、因子及非参数载荷，提出基于筛的广义矩估计方法，在简单识别条件下证明了所有未知量的一致性并推导了估计量的渐近分布。进一步构造了过度识别检验与因子载荷函数的设定检验，并建立了其大样本性质。模拟与股票收益预测的实证表明方法具有良好的有限样本表现与实证适用性。对您有用之处在于，该文将高维发散矩条件与筛估计结合，其非参数函数设定检验的思路可直接迁移至您关注的半参数/非参数理论及假设检验研究中。
- **关键技术**: `sieve GMM`, `high-dimensional moment restrictions`, `interactive effects`, `nonparametric factor loadings`, `over-identification test`, `specification test`
- **为什么对您有用**: 该文将高维发散矩条件与筛估计结合，其非参数函数设定检验的思路可直接迁移至您关注的半参数/非参数理论及假设检验研究中；同时高维GMM的渐近理论对您的高维统计与效率理论兴趣有直接参考价值。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1016/j.jeconom.2024.105845](https://doi.org/10.1016/j.jeconom.2024.105845) — Testing for sparse idiosyncratic components in factor-augmented regression models
- **作者**: Jad Beyhum, Jonas Striaukas
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 1 · pp 105845
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在因子增强回归模型中，本文研究如何检验纯稠密模型（因子回归）与稠密加稀疏替代模型（包含稀疏特质成分）的假设检验问题，设定允许时间序列依赖与多项式尾部分布。提出一种基于 bootstrap 的检验方法，核心在于区分稀疏偏离与稠密偏离，对稀疏替代假设具有高功效而对稠密偏离保持低功效。理论部分证明了该检验在时间序列及重尾下的渐近性质，并给出了调谐参数的数据驱动选择规则及其理论有效性。宏观与金融数据集上的实证结果频繁拒绝纯稠密原假设，表明经济数据中普遍存在“稠密+稀疏”结构；配套 R 包 FAS 便于方法复现。对您有用：该文将高维稀疏检验与因子模型结合，直接推进了您在假设检验与高维统计交叉领域的兴趣，且其经济数据实证对您的经济理论应用兴趣有参考价值。
- **关键技术**: `factor-augmented regression`, `bootstrap test`, `sparse plus dense alternative`, `time series dependence`, `polynomial tails`, `data-driven tuning parameter`
- **为什么对您有用**: 直接推进您在“假设检验”与“高维统计”交叉方向的兴趣（稀疏vs稠密结构检验），同时其宏观/金融数据集的实证分析对您的“经济理论”应用兴趣具有数据集与方法借鉴价值。

### 2. [10.1016/j.jeconom.2024.105840](https://doi.org/10.1016/j.jeconom.2024.105840) — An unbounded intensity model for point processes
- **作者**: Kim Christensen, Aleksey Kolokolov
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 1 · pp 105840
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究实轴上点过程强度函数局部无界（intensity burst）但不引发爆炸的建模与检验问题，关键假设是 heavy traffic condition。与传统的有序点过程（短时间内多于一个事件的概率可忽略）不同，该方法允许强度函数存在奇异性从而导致事件的极端聚集。提出一种非参数检验方法来检测这种强度突发，基于 heavy traffic 条件在有限时间区间内实现了点过程的统计推断。蒙特卡洛模拟表明该检验在原假设下具有 size control，在备择假设下具有高功效。实证应用于 EUR/USD 高频汇率数据，检测到交易活动异常激增，并发现强度突发与波动率、非流动性及漂移突发概率正相关。该文展示了在非标准点过程下构建非参数检验的渐近框架，对您在非参数理论及假设检验方面的研究有参考价值，高频数据应用也契合经济理论的数据兴趣。
- **关键技术**: `nonparametric hypothesis testing`, `unbounded intensity point process`, `heavy traffic condition`, `high-frequency financial data`, `extreme clustering`
- **为什么对您有用**: 涉及非参数假设检验与渐近理论，属于 primary interest 中的 mathematical statistics (hypothesis testing) 与 nonparametric theory；同时高频外汇数据的应用契合 secondary interest 中的 economic theory (data sets, model)。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1016/j.jeconom.2024.105862](https://doi.org/10.1016/j.jeconom.2024.105862) — A gentle introduction to matrix calculus
- **作者**: Jan R. Magnus
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 1 · pp 105862
- 相关性 0/10 · novelty: `survey`
- **摘要**: 本文是一篇关于矩阵微积分的教程，旨在为涉及矩阵的函数优化和敏感性分析提供系统性的理论基础。文章梳理了矩阵求导的核心理论与符号系统，涵盖了标量、向量及矩阵对矩阵求导的各类情形，并提供了大量完整计算的练习与实例。特别强调了该领域常见的“隐性知识”（tacit knowledge），如微分与导数的严格区分、Kronecker积与vec算子的运用，这些是处理高维似然或Fisher信息矩阵的关键工具。虽无新理论贡献，但作为工具书可极大简化半参数效率界、高维估计量渐近方差以及张量计算的推导过程。对您有用：直接服务于您在统计计算（矩阵/张量数值方法）与效率理论（影响函数求导）中的推导需求，是极佳的案头参考。
- **关键技术**: `matrix differential`, `Kronecker product`, `vec operator`, `sensitivity analysis`, `matrix optimization`
- **为什么对您有用**: 直接对应您 primary interest 中的统计计算（矩阵与张量）和效率理论，掌握矩阵微积分是推导半参数效率界、高维似然及随机矩阵理论中复杂导数的基础，本文作为系统教程可大幅降低推导门槛。

## 经济理论 / 应用  *(econ_theory, 2 篇)*

### 1. [10.1016/j.jeconom.2024.105864](https://doi.org/10.1016/j.jeconom.2024.105864) — Estimating option pricing models using a characteristic function-based linear state space representation
- **作者**: H. Peter Boswijk, Roger J.A. Laeven, Evgenii Vladimirov
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 1 · pp 105864
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在一般仿射跳跃扩散驱动的参数化期权定价模型下，目标是估计模型参数并推断潜在状态向量。核心方法是将期权隐含的（模型无关）条件对数特征函数与模型隐含的条件对数特征函数进行对比，后者关于状态向量是函数仿射的。由此推导出一个线性状态空间表示，并建立了相应测量误差的渐近性质。基于此线性状态空间，采用修正的卡尔曼滤波推断潜在状态，并结合拟最大似然估计（QMLE）估计模型参数，显著降低了计算复杂度。蒙特卡洛模拟验证了有限样本表现，实证分析将其应用于标普500期权定价及Covid-19再生数与经济政策不确定性等外生变量的影响评估。对您而言，该文展示了如何通过特征函数构造线性状态空间以实现计算加速，其 QMLE 渐近理论与 Kalman 滤波方案对统计计算和经济理论（期权定价）的交叉研究有参考价值。
- **关键技术**: `characteristic function`, `linear state space representation`, `Kalman filtering`, `quasi-maximum likelihood estimation`, `affine jump-diffusion`
- **为什么对您有用**: 属于经济理论（期权定价）与统计计算的交叉；其通过特征函数构造线性状态空间并利用修正 Kalman 滤波实现计算加速的思路，对您在统计计算（数值方法与算法）方面的兴趣有直接参考价值，同时提供了包含宏观外生变量（Covid-19/EPU）的实证数据集。

### 2. [10.1016/j.jeconom.2024.105841](https://doi.org/10.1016/j.jeconom.2024.105841) — Threshold spatial autoregressive model
- **作者**: Kunpeng Li, Wei Lin
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 1 · pp 105841
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究带阈值效应的空间自回归（SAR）模型，目标是在空间依赖下对阈值参数及区制依赖的回归系数进行估计与推断。核心方法将 SAR 的工具变量/极大似然估计与阈值最小二乘思想结合，阈值参数的估计量具有非标准收敛速率（超一致性），而区制内回归系数可达 n^{-1/2}-CAN。假设检验方面，阈值存在性检验涉及 Davies 问题（sup-type 统计量），需借助边界分布或 bootstrap 校正临界值。空间滞后矩阵 W 的引入使渐近理论比普通阈值回归更复杂，需处理空间相关性对经验过程的扰动。主要理论贡献是给出了阈值估计的极限分布及检验统计量的渐近临界值。对您有用之处在于：阈值检验的非标准渐近理论与您对 hypothesis testing 的兴趣直接相关，且空间经济模型为 IV/semiparametric 推断提供了有价值的 applied 场景。
- **关键技术**: `spatial autoregressive model`, `threshold estimation`, `sup-type test`, `non-standard asymptotics`, `instrumental variable estimation`, `bootstrap critical value`
- **为什么对您有用**: 阈值存在性检验的 sup-type 统计量与 Davies 问题属于您 primary interest 中 hypothesis testing 的非标准情形；空间 SAR 模型的 IV 估计与 semiparametric 推断框架可迁移至您关注的 causal inference / efficiency theory 场景。

## 其他  *(other, 2 篇)*

### 1. [10.1016/j.jeconom.2024.105831](https://doi.org/10.1016/j.jeconom.2024.105831) — Fixed-<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" altimg="si420.svg" display="inline" id="d1e5003"><mml:mi>b</mml:mi></mml:math> asymptotics for panel models with two-way clustering
- **作者**: Kaicheng Chen, Timothy J. Vogelsang
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 1 · pp 105831
- 相关性 6/10
- **摘要**: {
  "topic": "hypothesis_testing",
  "summary_zh": "本文研究线性面板模型中双向聚类（two-way clustering）下的稳健方差估计量（CHS估计量），目标是在横截面与时间维度联合发散的设定下改善假设检验的有限样本性质。作者首先从代数上证明CHS估计量是单一个体聚类估计量、"HAC of averages"与"average of HACs"三者的线性组合。基于此分解，推导了该方差估计量及对应检验统计量的 fixed-b 渐近分布。进一步提出了两种简单的偏差校正方差估计量，并导出其 fixed-b 极限分布。模拟与实证（行业盈利与市场集中度）表明，偏差校正结合 fixed-b 临界值能显著提升有限样本覆盖概率。对您有用：直接契合您在 mathematical statistics (hypothesis testing) 的兴趣，fixed-b 渐近与偏差校正技术可迁移至因果推断或高维设定下的稳健标准误计算。",
  "key_techniques": [
    "fixed-b asymptotics",
    "two-way clustering",
    "cluster robust variance estimator",
    "bias correction",
    "panel data inf

### 2. [10.1016/j.jeconom.2024.105842](https://doi.org/10.1016/j.jeconom.2024.105842) — Measuring diagnostic test performance using imperfect reference tests: A partial identification approach
- **作者**: Filip Obradović
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 244 · issue 1 · pp 105842
- 相关性 0/10
- **摘要**: ```json
{
  "topic": "causal_inference",
  "summary_zh": "在诊断测试性能评估中，当参考测试（reference test）不完美时，传统方法仅能识别"表观"灵敏度/特异度而非真实性能。本文在标准设定下，对真实 true positive rate 和 true negative rate 推导出最小可能的 partial identification bounds，并进一步导出患病率和预测值等政策相关参数的界。推断基于 moment inequalities 构建在相关分布族上一致一致的置信集（uniformly consistent confidence sets）。应用于 BinaxNOW COVID-19 抗原测试的 EUA 及独立研究数据，发现有症状和无症状患者的真实假阴性率分别可达表观假阴性率的 3.17 和 4.59 倍。该 partial identification 思路可推广至调查响应、推断受保护类别等不完美代理变量场景。对您有用：partial identification 与 moment inequality 推断框架可直接迁移至因果推断中 sensitivity analysis 与部分识别问题，同时提供了流行病学诊断测试的真实数据集与分析范式。",
  "key_techniques": ["pa


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

