# Stat. Comput. — Vol 36  Issue 4  ·  2026-07-14

- 共 28 篇 · Statistics and Computing
- 目录核对 ⚠️ 疑似漏 12 篇（对照 OpenAlex 40 篇）：10.1007/s11222-026-10930-9、10.1007/s11222-026-10863-3、10.1007/s11222-026-10894-w、10.1007/s11222-026-10904-x、10.1007/s11222-026-10909-6 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

Stat. Comput. Vol 36 Issue 4 的 28 篇论文可归纳为四条主线：**因果推断与迁移学习**（1 篇）、**高维稀疏与稳健方法**（2 篇）、**统计计算与算法创新**（约 15 篇，涵盖采样、变分推断、分治策略、贝叶斯计算等）、以及**假设检验与非参数/半参数方法**（约 4 篇，含变量重要性、排序检验、非线性回归）。其余论文涉及时间序列建模（排名 GARCH、马尔可夫切换 BEKK）、异常检测与域适应、以及偏微分方程反问题等应用方向。

**因果推断**主线仅一篇，但直接聚焦于 CATE 估计在数据稀疏场景下的迁移学习问题。该文将 Wang (2016) 的 offset 方法系统性地引入因果森林，通过估计源域与目标域的分布偏移来校正 CATE 估计，并给出了 L1 一致性与误差上界。**高维稀疏与稳健方法**主线有两篇：一篇提出基于指数型损失函数的稳健 Lasso，在重尾噪声下达到与次高斯噪声相同的收敛速率，且无需显式截断；另一篇通过变量去相关预处理来缓解 Lasso 在相关预测变量下的不稳定性，并证明去相关后 irrepresentable 条件得以满足。**统计计算**主线最为密集，涵盖多个子方向：采样方法方面，有基于垂直加权条带的拒绝采样、针对截断多元高斯的连续高斯混合 MCMC、以及不可逆离散采样器 PDHAMS；变分推断方面，有加速粒子变分推断和针对计数数据的稳健变分 GP 回归；分治与并行方面，有将黑箱估计器分区域训练后加权合并的框架；贝叶斯计算方面，有摊销贝叶斯混合模型、基于持续同调的先验、以及 Wasserstein 排斥高斯混合模型；此外还有聚焦加权平均最小二乘（FWALS）的半正交化降维策略、嵌套 EnKF 用于非线性状态空间模型参数推断、以及神经后验估计在 ERGM 中的偏差评估。**假设检验**主线中，正则化 MMD 用于变量重要性度量，通过优化变量权重自适应反映分布差异；非参数排序估计方法则针对多变量二元数据，在控制 FWER 的同时估计总体排序。

与因果推断方向最直接相关的论文是《Transfer learning for causal forests》，适合优先阅读。半参数/非参方向可关注《An interpretable varying coefficients approach to non-linear regression》和《Nonparametric estimation of the joint and conditional survival functions》。高维方向可优先看《Robust sparse penalization under heavy-tailed noise》和《Stability selection via variable decorrelation》。

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.1007/s11222-026-10919-4](https://doi.org/10.1007/s11222-026-10919-4) — Transfer learning for causal forests
- **作者**: Bérénice-Alexia Jocteur, Véronique Maume-Deschamps, Pierre Ribereau
- **期刊/来源**: Statistics and Computing
- **机构**: Université Claude Bernard Lyon 1 · Centre National de la Recherche Scientifique · Institut Camille Jordan · Institut National des Sciences Appliquées de Lyon
- **分类**: vol 36 · issue 4
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究迁移学习在因果森林（HTERF）中的应用，目标是在源域数据充足、目标域数据稀疏且存在模型偏移时，估计条件平均处理效应（CATE）。方法核心是Wang (2016)的offset方法，通过训练中间模型来估计源域与目标域分布之间的偏移量，并将该偏移量作为校正项融入因果森林的构建中。作者建立了算法的L1一致性结果，并推导了目标域CATE估计误差的上界，该上界依赖于中间模型的估计误差。仿真实验在多种偏移设定下验证了方法的有效性。本文的贡献在于将迁移学习的思想系统性地引入因果森林框架，为处理目标域样本量不足时的CATE估计提供了理论保证和实用算法。对您而言，本文直接关联因果推断中的CATE估计和纵向/迁移设定，且其理论分析（一致性、误差上界）与您熟悉的非参数统计和minimax bound技术高度契合，可作为立即可做的切入点。
- **关键技术**: `causal forest`, `transfer learning`, `offset method`, `conditional average treatment effect (CATE)`, `L1 consistency`
- **为什么对您有用**: 本文直接连接您的primary interest中的因果推断（CATE估计）和迁移学习设定。您very_familiar的nonparametric statistics和minimax bounds可用于分析其误差上界是否紧，而moderately_familiar的identification theory可帮助评估其偏移校正假设的可检验性。立即可做：用您已有的因果推断和nonparametric工具复现或扩展其理论结果。

### 2. [10.1007/s11222-026-10921-w](https://doi.org/10.1007/s11222-026-10921-w) — Nonparametric estimation of the joint and conditional survival functions of the time to an event of interest and associated integrated covariate processes
- **作者**: Ashwini Joshi, Dario Gasbarra, Sangita Kulathinal
- **期刊/来源**: Statistics and Computing
- **机构**: University of Helsinki · Helsinki Institute of Physics · University of Vaasa
- **分类**: vol 36 · issue 4
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文研究慢性疾病治疗中，事件发生时间与累积协变量过程（如药时曲线下面积）的联合与条件生存函数的非参数估计。设定中，累积响应随时间增长，事件时间与累积响应首次超过阈值的时间可能被同一删失机制截断，形成一种特殊的双变量删失结构。作者提出逆概率删失加权（IPCW）估计量，根据删失分布估计中利用信息量的不同，给出不同效率的估计量，并引入分层分析中的合并估计量。进一步，给定协变量过程历史，估计事件时间的条件生存函数，并讨论其在医疗决策中的应用。方差估计采用jackknife方法。方法可推广至多个协变量过程，并通过年龄相关性黄斑变性（AMD）的临床试验和真实世界数据验证。对您而言，本文的IPCW框架与删失处理技巧可迁移至纵向因果推断中的复合终点或累积暴露效应估计，且其非参数估计思路与您的非参数统计和因果推断兴趣直接相关。
- **关键技术**: `inverse-probability of censoring weighting (IPCW)`, `bivariate survival function`, `conditional survival function`, `jackknife variance estimation`, `stratified analysis`
- **为什么对您有用**: 本文直接关联您的primary interest中的因果推断（纵向设定）和非参数统计。其IPCW估计量处理删失的思路，可迁移至您熟悉的非参数统计和因果推断中的逆概率加权方法。中期可做：若将本文的删失结构推广至带有time-varying confounding的因果效应估计，需先在moderately_familiar的identification theory in causal inference上长肌肉（如g-formula与IPCW的结合）。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 2 篇)*

### 1. [10.1007/s11222-026-10931-8](https://doi.org/10.1007/s11222-026-10931-8) · [arXiv](https://arxiv.org/abs/2511.15332) — Robust sparse penalization under heavy-tailed noise and outliers with exponential-type loss via the LASSO
- **作者**: The Tien Mai
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 4
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文在高维稀疏线性回归框架下，针对经典 Lasso 对重尾噪声和异常值敏感的问题，提出一种基于指数型损失函数的稳健 Lasso 方法。该损失函数在残差较小时近似二次型以保持高斯噪声下的统计效率，在残差较大时平滑下降以自动降权极端异常值，无需显式截断或分位数阈值。理论上，作者证明了在重尾污染下估计量的收敛速率与经典 Lasso 在次高斯噪声下的最优速率一致，即达到 n^{-1/2} 量级的 l2 误差和 s log p / n 量级的预测误差，且不牺牲鲁棒性。计算上采用 Majorization-Minimization (MM) 算法，将原问题迭代转化为加权 Lasso 子问题，保证了数值稳定性。模拟和真实数据实验表明，该方法在污染场景下显著优于经典 Lasso，在纯高斯噪声下性能几乎不损失。该方法已封装为 R 包 heavylasso 并开源。对您而言，本文提供了一种在高维因果推断（如 IV 或 mediation 的第一阶段）中处理异常值的现成工具，且其理论分析框架（指数型损失 + Lasso 收敛速率）可直接与您熟悉的 minimax bound 技术对接，中期可做：将指数型损失扩展到 DML 的 nuisance 函数估计中，检验其是否保持正交性条件。
- **关键技术**: `exponential-type loss function`, `redescending M-estimator`, `Majorization-Minimization (MM) algorithm`, `weighted Lasso`, `high-dimensional convergence rates`
- **为什么对您有用**: 本文直接连接到您 primary interest 中的高维统计和因果推断：其提出的稳健 Lasso 可替代经典 Lasso 作为因果推断中 nuisance 函数的估计器（如 IV 第一阶段或倾向性得分），尤其适用于流行病学或经济学数据中常见的重尾噪声和异常值。您的技术武器库中 'minimax bounds for estimation problems' 和 'high-dimensional asymptotics' 可直接用于验证本文声称的收敛速率是否紧，而 'software development' 经验可帮助您快速复现或扩展 heavylasso 包。中期可做：需先在 'semiparametric theory' 上熟悉 DML 的正交性条件，才能将指数型损失嵌入双稳健估计框架。

### 2. [10.1007/s11222-026-10916-7](https://doi.org/10.1007/s11222-026-10916-7) · [arXiv](https://arxiv.org/abs/2505.20864) — Stability selection via variable decorrelation
- **作者**: Mahdi Nouraie, Connor Smith, Samuel Muller
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 4
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对高维线性模型中 Lasso 变量选择在相关预测变量下不稳定的问题，提出了一种预处理方法：在应用 Lasso 之前对变量进行去相关（decorrelation）。核心思想是通过对设计矩阵施加某种正交化变换（如基于协方差矩阵估计的 Cholesky 分解或谱分解），使得变换后的变量近似不相关，从而缓解 Lasso 对相关性的敏感性。作者证明，在去相关后，保证 Lasso 一致变量选择的 irrepresentable 条件在两种假设下得以满足。该方法不限于高维设定，在低维相关数据中也有效。实验表明，去相关预处理能提升多种变量选择方法（如 Lasso、adaptive Lasso）的稳定性。文章还提供了 R 包以方便应用。对您而言，这是一篇统计计算与高维统计交叉的实用方法论文，其去相关预处理思路可与您在高维统计和软件工具开发方面的兴趣直接对接。
- **关键技术**: `variable decorrelation`, `Lasso`, `irrepresentable condition`, `high-dimensional regression`, `variable selection stability`
- **为什么对您有用**: 本文直接连接您的高维统计兴趣，特别是 Lasso 在相关变量下的稳定性问题。您的武器库中'高维渐近理论'和'软件工具开发'两项非常熟悉，可以立即动手复现其 R 包并测试去相关预处理在您关注的因果推断高维设定（如 IV 选择工具变量）中的效果。中期可做：将去相关思路与您 moderately_familiar 的 HOIF 结合，研究去相关对高阶影响函数估计的影响。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1007/s11222-026-10903-y](https://doi.org/10.1007/s11222-026-10903-y) — An interpretable varying coefficients approach to non-linear regression
- **作者**: Davide Fabbrico, Matteo Pedone, Francesco Claudio Stingo
- **期刊/来源**: Statistics and Computing
- **机构**: Azienda Ospedaliero Universitaria San Giovanni Battista · University of Florence
- **分类**: vol 36 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出一种可解释的非线性回归模型，通过半参数样条基分解将线性与非线性效应正交分离，并引入协变量依赖的回归系数以增强灵活性。该方法等价于一种非线性交互模型，且证明了对协变量顺序的不变性。模拟研究表明，与现有方法相比，该模型在拟合性能上具有竞争力。两个实际数据应用展示了不同程度的非线性关联。该工作对您可能有用：其半参数样条分解与正交化思路可迁移至高维因果推断中的部分线性模型或非参数效应估计。
- **关键技术**: `semi-parametric spline`, `orthogonal basis decomposition`, `varying coefficients`, `non-linear interaction model`
- **为什么对您有用**: 该文属于半参数/非参数理论方向，与您的primary interest中的semiparametric and nonparametric theory直接相关。其正交分解与协变量依赖系数的设计，可借助您very_familiar中的nonparametric statistics和minimax bounds工具进行理论分析（如估计量的收敛速率）。中期可做：若需将方法推广至高维或因果设定，需先在moderately_familiar的semiparametric theory上加强。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1007/s11222-026-10927-4](https://doi.org/10.1007/s11222-026-10927-4) — Regularized maximum mean discrepancy for variable importance measure
- **作者**: Junfeng Huo, Bingyao Huang, Yanyan Liu, Liuhua Peng
- **期刊/来源**: Statistics and Computing
- **机构**: Wuhan University · Guangdong University of Technology · The University of Melbourne
- **分类**: vol 36 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文在最大均值差异（MMD）框架下提出了一种新的变量重要性度量方法。核心思想是为每个变量赋予权重，并通过正则化MMD准则优化这些权重，使其自适应地反映各变量的信号强度。优化后的权重直接量化了每个变量对两个分布之间差异的贡献，从而作为变量重要性的度量。进一步地，作者开发了面向目标的变量选择方法，基于优化权重选出的变量旨在最小化特定任务的损失函数。在双样本检验和分类两个常见场景中，该方法增强了MMD检验的功效并提高了分类准确率。论文建立了估计权重的一致性理论，并通过大量模拟和真实数据应用验证了方法的实际有效性。该工作将变量选择与分布对比检验有机结合，对高维假设检验和特征筛选有直接参考价值。
- **关键技术**: `Maximum Mean Discrepancy (MMD)`, `regularized optimization`, `variable importance measure`, `kernel methods`, `two-sample testing`
- **为什么对您有用**: 本文直接关联您的首要兴趣——假设检验与高维统计。其核心是使用正则化MMD进行变量重要性排序，这为高维分布对比检验中的变量筛选提供了新思路。您武器库中的非参数统计和最小最大界技术可用于分析该方法的检验功效与最优性，属于**立即可做**的跟进方向。

### 2. [10.1007/s11222-026-10900-1](https://doi.org/10.1007/s11222-026-10900-1) — An innovative nonparametric ranking estimation method with multivariate binary variables
- **作者**: Stefano Bonnini, Michela Borghesi, Massimiliano Giacalone
- **期刊/来源**: Statistics and Computing
- **机构**: University of Ferrara · University of Campania "Luigi Vanvitelli"
- **分类**: vol 36 · issue 4
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对多变量二元数据，提出一种新的非参数排序估计方法。研究问题是在C个多元总体之间进行两两比较并估计其排序，目标是在控制族系错误率（FWER）的同时获得可靠的排序。方法分为两步：第一步，对每对总体进行多元假设检验（基于非参数组合检验）；第二步，利用第一步得到的p值信息估计总体排序。该方法克服了现有类似方法在多重比较下无法控制FWER、易错误拒绝原假设的缺陷。通过大量模拟研究验证了方法的有效性，并应用于一项关于意大利中小企业采用工业4.0技术倾向性的原始调查，以排序不同经济部门。对您而言，本文的非参数检验与排序框架与您的假设检验兴趣直接相关，但其方法学新颖性有限（主要是现有方法的组合应用），且未涉及您更核心的高维或因果推断方向。
- **关键技术**: `nonparametric combination test`, `family-wise error rate control`, `multivariate pairwise comparisons`, `ranking estimation via p-values`
- **为什么对您有用**: 本文直接关联您的假设检验兴趣，特别是多重比较下的FWER控制问题。但方法学贡献有限（组合现有技术），且未涉及您更核心的高维统计或因果推断方向。武器库中'非参数统计'和'M估计理论'可理解其检验步骤，但本文未提供新的理论突破或可迁移的技术工具。暂不可做：核心机器不在武器库里（缺乏对多元非参数组合检验的深入经验，且问题本身与您的主要研究方向距离较远）。

## 统计计算 / 算法  *(stat_computing, 19 篇)*

### 1. [10.1007/s11222-026-10872-2](https://doi.org/10.1007/s11222-026-10872-2) · [arXiv](https://arxiv.org/abs/2510.03729) — Beyond regularization: inherently sparse principal component analysis
- **作者**: Jan O. Bauer
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 4
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文提出一种超越正则化的稀疏主成分分析（sparse PCA）新方法，核心思想是识别数据矩阵中不相关的子矩阵，即协方差矩阵呈现稀疏块对角结构。该方法不依赖L1正则化等惩罚项，而是利用数据本身的固有结构来产生稀疏奇异向量，从而避免过度正则化导致的估计偏差。由于子矩阵不相关，得到的奇异向量天然正交，解决了传统稀疏PCA中分量共享信息、解释方差计算复杂的问题。方法适用于高维低样本量场景（如基因微阵列），但不限于此。通过模拟和真实数据应用验证了有效性。对您而言，本文提供了一种新的稀疏化思路，其块对角结构识别与您的统计计算兴趣（算法设计）相关，且方法本身不依赖复杂优化，易于实现。
- **关键技术**: `sparse block diagonal covariance`, `inherently sparse singular vectors`, `orthogonal components`, `submatrix identification`
- **为什么对您有用**: 本文属于统计计算方法创新，直接对应您的primary interest中的'statistical computing (numerical methods, algorithm)'。其核心思想——利用数据固有块对角结构而非正则化实现稀疏性——提供了一种新的算法设计视角。您可以用very_familiar的'软件开发和算法实现'能力快速复现并评估该方法，属于'立即可做'的范畴。

### 2. [10.1007/s11222-026-10910-z](https://doi.org/10.1007/s11222-026-10910-z) · [arXiv](https://arxiv.org/abs/2412.20323) — When the whole is greater than the sum of its parts: Scaling black-box inference to large data settings through divide-and-conquer
- **作者**: Emily C. Hector, Amanda Lenzi
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对黑箱估计方法（如深度神经网络）在训练数据模拟成本高昂时无法扩展的问题，提出了一种分而治之的估计与推断框架。核心思想是将多元数据域划分为多个子区域，在每个子区域上独立训练黑箱估计器并进行参数自助法推断，最后通过加权平均合并各子区域的估计和推断结果。分治步骤大幅降低了训练数据的模拟成本，且估计与自助法可并行计算。合并步骤通过统计与计算高效的加权平均处理子区域间的依赖关系。在高维空间过程（高斯过程与最大稳定过程）设定下验证了框架的有效性，并在 NOAA 极端温度数据上展示了可对数万个位置的最大稳定过程参数进行估计与推断。该框架对您作为统计计算方向的研究者具有直接参考价值，尤其是其分治策略与加权合并的设计思路可迁移至您熟悉的软件开发和计算密集型统计方法中。
- **关键技术**: `divide-and-conquer`, `black-box estimation`, `parametric bootstrap`, `weighted average combining`, `spatial process`, `max-stable process`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的 primary interest 中的 statistical computing。其分治框架与并行化策略可迁移至您熟悉的软件开发与高维统计计算场景。武器库中 very_familiar 的软件开发和 high-dimensional asymptotics 可直接用于理解并复现其加权合并的统计性质；中期可做：若想将分治思想推广到更一般的因果推断或 U-统计量计算中，需先在 moderately_familiar 的 M-estimation theory 上巩固。

### 3. [10.1007/s11222-026-10914-9](https://doi.org/10.1007/s11222-026-10914-9) · [arXiv](https://arxiv.org/abs/2509.11532) — E-ROBOT: a dimension-free method for robust statistics and machine learning via Schrödinger bridge
- **作者**: Davide La Vecchia, Hang Liu
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出 E-ROBOT 框架，将鲁棒最优传输 (ROBOT) 与熵正则化结合，基于 Schrödinger bridge 问题定义鲁棒 Sinkhorn 散度 W̄_{ε,λ}，其中 λ 控制鲁棒性、ε 控制正则化强度。核心理论贡献是证明该散度的样本复杂度为 O(n^{-1/2})，即维度无关，避免了标准 ROBOT 的维度灾难。这一性质使得 W̄_{ε,λ} 可作为高维统计与机器学习任务中的损失函数。文章展示了四个应用：拟合优度检验、受污染 2D/3D 形状的 barycenter 计算、梯度流定义、图像颜色迁移。计算上，该方法可通过修改现有 Python 例程轻松实现。对您而言，该工作属于统计计算方向，其维度无关的样本复杂度结果与您在高维统计和 minimax 界的兴趣直接相关，且计算实现简单，适合作为 gateway reading 评估是否值得深入。
- **关键技术**: `Schrödinger bridge`, `entropic regularization`, `robust optimal transport`, `Sinkhorn divergence`, `dimension-free sample complexity`
- **为什么对您有用**: 本文属于统计计算方向，核心贡献是维度无关的样本复杂度 O(n^{-1/2})，这与您在高维统计和 minimax 界的兴趣直接相关。您可以用 very_familiar 中的 minimax bounds 工具验证其声称的维度无关率是否紧，并评估该框架在您熟悉的因果推断或高维设定中的适用性。中期可做：若想将 E-ROBOT 用于因果推断中的分布偏移检测，需先在 moderately_familiar 的 semiparametric theory 上加强，以处理 nuisance 函数估计的影响。

### 4. [10.1007/s11222-026-10890-0](https://doi.org/10.1007/s11222-026-10890-0) · [arXiv](https://arxiv.org/abs/2504.01360) — A persistent-homology-based Bayesian prior for potential coefficient reconstruction in an elliptic partial differential equation
- **作者**: Zhiliang Deng, Haiyang Liu, Xiaofei Guan, Zhiyuan Wang, Xiaomei Yang
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文在贝叶斯框架下解决椭圆型偏微分方程中势系数反演问题，目标是从分布观测数据重建具有尖锐不连续性的系数函数。针对传统高斯先验无法有效捕捉不连续性的缺陷，提出一种基于持续同调（persistent homology, PH）的先验分布，通过候选函数的持续对（persistent pairs）量化并编码其拓扑特征。为确保在无穷维空间中的良定义性，该先验以高斯参考测度为基础构建，仅要求未知函数属于合适的拓扑空间，显著增强了适用性。数值实验表明，PH先验优于高斯先验，且相比经典全变差（TV）先验有适度但一致的改进。对您而言，本文展示了拓扑数据分析工具（持续同调）在统计反问题中的创新应用，与您对统计计算（数值方法）的兴趣直接相关，且其先验构造思路可能启发您在逆问题或高维统计中的新方法。
- **关键技术**: `persistent homology`, `Bayesian inverse problems`, `elliptic PDE`, `Gaussian reference measure`, `total variation prior`
- **为什么对您有用**: 本文连接您对统计计算（数值方法）的兴趣，展示了持续同调作为先验在反问题中的新应用。您的武器库中'逆问题与随机噪声'非常熟悉，可直接评估其先验构造的统计效率；但持续同调本身是您不熟悉的拓扑工具，属于'暂不可做'——核心机器（持续同调计算与拓扑数据分析）不在武器库中，需先学习该领域基础。

### 5. [10.1007/s11222-026-10887-9](https://doi.org/10.1007/s11222-026-10887-9) · [arXiv](https://arxiv.org/abs/2504.21391) — Bayesian wasserstein repulsive gaussian mixture models
- **作者**: Weipeng Huang, Tin Lok James Ng
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出贝叶斯 Wasserstein 排斥高斯混合模型，旨在促进聚类成分间的良好分离。与现有排斥混合方法仅关注分离成分均值不同，该方法基于 Wasserstein 距离来鼓励混合成分间的分离。在非参数密度估计框架下，建立了后验收缩率。后验采样采用 blocked-collapsed Gibbs 采样器实现。通过模拟研究和真实数据应用，展示了所提模型的有效性。该工作对您可能有用：其核心是统计计算中的贝叶斯非参数建模与采样算法，与您的 statistical computing 兴趣直接相关，且 Wasserstein 距离的使用为混合模型的后验推断提供了新视角。
- **关键技术**: `Wasserstein distance`, `repulsive Gaussian mixture models`, `Bayesian nonparametrics`, `posterior contraction rates`, `blocked-collapsed Gibbs sampler`
- **为什么对您有用**: 本文属于统计计算与贝叶斯非参数方法，直接对应您的 primary interest 中的 statistical computing。其核心贡献在于使用 Wasserstein 距离定义排斥先验，这为混合模型的后验推断提供了新工具。从您的技术武器库看，您对 nonparametric statistics 和 M-estimation theory 非常熟悉，但本文的贝叶斯框架（后验收缩率、Gibbs 采样）属于 moderately_familiar 的 M-estimation 理论可触及的范畴——您可以用 minimax 视角分析其收缩率是否最优，或对比其与频率派方法的计算效率。中期可做：需先在 moderately_familiar 的 M-estimation theory 上进一步熟悉贝叶斯非参数的后验收缩率工具。

### 6. [10.1007/s11222-026-10935-4](https://doi.org/10.1007/s11222-026-10935-4) · [arXiv](https://arxiv.org/abs/2511.15155) — Outlier detection in state-space models using mean-shift penalisation
- **作者**: Rajan Shankar, Ines Wilms, Jakob Raymaekers, Garth Tarr
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 4
- 相关性 4/10 · novelty: `application`
- **摘要**: 针对状态空间模型（SSM）对异常值敏感的问题，提出了一种鲁棒估计方法 ROAMS。该方法通过在观测方程中引入每个时间点的移位参数，将异常值建模为均值偏移，并利用惩罚项自动检测异常点。估计过程同时优化模型参数和移位参数，实现异常值的自动识别与参数鲁棒估计。在模拟和真实动物轨迹追踪数据上，ROAMS 相比经典方法和现有基准方法得到更可靠的参数估计。该方法还提供了 BIC 曲线等实用诊断工具，帮助选择调优参数和可视化异常结构。对您而言，这是一篇统计计算与鲁棒方法结合的应用型工作，其惩罚框架和诊断工具可迁移至您熟悉的因果推断纵向数据中的异常值处理问题。
- **关键技术**: `mean-shift penalisation`, `state-space model`, `robust estimation`, `BIC-based tuning`, `additive outlier model`
- **为什么对您有用**: 本文属于统计计算方向，核心是鲁棒估计与异常检测的算法设计。您熟悉的非参数统计和软件工程经验可直接用于复现或扩展其惩罚框架（立即可做）。若将移位参数思想引入纵向因果推断中的敏感度分析，需先熟悉您 moderately_familiar 的 identification theory（中期可做）。

### 7. [10.1007/s11222-026-10915-8](https://doi.org/10.1007/s11222-026-10915-8) · [arXiv](https://arxiv.org/abs/2603.03008) — Focused weighted-average least squares estimator
- **作者**: Shou-Yung Yin
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 4
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出聚焦加权平均最小二乘（FWALS）估计量，旨在解决聚焦模型平均（FMA）中遍历所有子模型（2^{k_2}个）的计算瓶颈。核心创新是将辅助回归变量半正交化，使权重选择从指数级子模型缩减至最多k_2个回归变量级权重，得到一个可处理的次优程序。在局部到零（local-to-zero）设定下，推导了FWALS对光滑聚焦函数的极限分布，并给出了基于plug-in AMSE准则的数据驱动权重选择方法。模拟表明，FWALS在均方误差上接近聚焦信息准则（FIC）基准，且在脉冲响应函数等聚焦函数设定下表现稳定。该方法属于模型平均与计算统计的交叉，对您而言，其半正交化降维思路可迁移至高维U-统计量的计算复杂度分析（如利用树宽/张量收缩的einsum复杂度视角），且AMSE准则的推导涉及M-估计理论，与您的semiparametric理论工具箱有直接接口。
- **关键技术**: `semi-orthogonalization`, `focused model averaging`, `plug-in AMSE criterion`, `local-to-zero asymptotics`, `weighted least squares`
- **为什么对您有用**: 本文属于统计计算方向，直接连接您的primary interest中的'statistical computing (numerical methods, algorithm)'。其半正交化降维策略与您非常熟悉的'higher-order U-statistics (treewidth / tensor contraction / einsum)'有结构类比——可将子模型枚举视为张量收缩的指数级求和，用树宽视角分析FWALS的计算复杂度是否最优。中期可做：需先在moderately_familiar的'M-estimation theory'上巩固（AMSE准则的渐近理论），但核心降维思路立即可用very_familiar的einsum工具进行数值验证。

### 8. [10.1007/s11222-026-10911-y](https://doi.org/10.1007/s11222-026-10911-y) · [arXiv](https://arxiv.org/abs/2501.10229) — Amortized Bayesian Mixture Models
- **作者**: Šimon Kucharský, Paul-Christian Bürkner
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 4
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对贝叶斯混合模型的计算困难（高维后验推断、标签切换、似然不可解析等），提出了一种摊销贝叶斯推断（ABI）框架的扩展。核心思想是将后验分解为参数分布和（类别）混合指示变量分布，分别用生成神经网络进行参数推断、用分类网络识别混合成员。该方法无需显式似然，支持独立和依赖混合模型（含滤波和平滑），且推断速度快。在合成和真实数据集上验证了有效性。对您而言，这是统计计算方向的一个实用算法创新，展示了神经网络如何绕过MCMC在混合模型上的瓶颈，可作为您软件开发和计算方法的参考。
- **关键技术**: `Amortized Bayesian Inference`, `generative neural networks`, `classification networks`, `simulation-based inference`, `mixture models`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的 primary interest 中的 statistical computing。它展示了如何用摊销推断解决混合模型的计算瓶颈，您可以用 very_familiar 的软件开发和 high-dimensional asymptotics 视角来评估其计算效率与收敛性。中期可做：若想深入其理论保证，需在 moderately_familiar 的 M-estimation theory 上补足（神经网络估计的渐近性质）。

### 9. [10.1007/s11222-026-10901-0](https://doi.org/10.1007/s11222-026-10901-0) · [arXiv](https://arxiv.org/abs/2504.03158) — Accelerating particle-based energetic variational inference
- **作者**: Xuelian Bao, Lulu Kang, Chun Liu, Yiwei Wang
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 4
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出一种加速粒子变分推断（ParVI）的新方法，针对 Wang et al. (2021) 的 Energetic Variational Inference with Implicit scheme (EVI-Im) 进行改进。核心思路是借鉴梯度流的能量二次化（EQ）和算子分裂技术，在保持稳定性的同时更高效地驱动粒子向目标分布演化。与 EVI-Im 使用隐式欧拉法求解变分粒子动力学不同，新算法避免了每个时间步内重复计算粒子间相互作用项，从而显著降低计算成本。该方法框架可推广至其他基于梯度的采样技术。数值实验表明，在效率和鲁棒性方面，该方法在特定参数区间优于现有 ParVI 方法。对您而言，本文属于统计计算中采样方法的算法改进，其算子分裂和能量二次化技巧可能对您在高阶 U-统计量计算中的张量收缩优化有启发，属于中期可做的方向——需先在 moderately_familiar 的 HOIF 或 M-estimation 理论中积累梯度流与变分推断的交叉知识。
- **关键技术**: `particle-based variational inference`, `energy quadratization`, `operator splitting`, `gradient flow`, `implicit Euler method`, `Kullback-Leibler divergence minimization`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的 primary interest 中的 statistical computing。其算子分裂和能量二次化技巧是梯度流数值方法的核心，可能迁移到您在高阶 U-统计量计算中遇到的张量收缩优化问题（如通过算子分裂降低 contraction 的 treewidth）。目前您对梯度流和变分推断的熟悉度有限，属于**中期可做**：需先在 moderately_familiar 的 HOIF 或 M-estimation 理论中积累相关背景，再评估能否将本文的加速思路用于您的 tensor-network 成本模型。

### 10. [10.1007/s11222-026-10899-5](https://doi.org/10.1007/s11222-026-10899-5) · [arXiv](https://arxiv.org/abs/2511.21497) — Nested ensemble Kalman filter for static parameter inference in nonlinear state-space models
- **作者**: Andrew Golightly, Sarah E. Heaps, Chris Sherlock, Laura E. Wadkin, Darren J. Wilkinson
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 4
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出嵌套集成卡尔曼滤波器（Nested EnKF），用于非线性状态空间模型（SSM）中静态参数的联合推断。核心思路是将 EnKF 替代 SMC² 算法中的粒子滤波器，利用 EnKF 的 shifting-based 更新维持粒子多样性，同时通过重采样-移动步骤（resample-move step）对参数粒子进行加权，权重基于 EnKF 计算的观测数据似然。算法扩展包括在 rejuvenation 步骤中使用延迟接受核（delayed acceptance kernel）以及纳入非线性观测模型。通过多个应用案例展示了方法的有效性。该方法在计算效率上优于传统 SMC²，尤其适用于高维动态系统。对您而言，本文属于统计计算方向的应用型工作，展示了 EnKF 与 SMC 框架的巧妙结合，可作为您软件开发和算法设计的参考案例。
- **关键技术**: `Ensemble Kalman filter`, `SMC²`, `resample-move`, `delayed acceptance`, `state-space models`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的 primary interest 中的 statistical computing。EnKF 与 SMC 的结合是计算密集型算法，您可以用 very_familiar 的软件开发和 high-dimensional asymptotics 工具分析其计算复杂度或收敛性。中期可做：若想深入理解 EnKF 在高维 SSM 中的理论性质，需先在 moderately_familiar 的 M-estimation theory 上加强。

### 11. [10.1007/s11222-026-10906-9](https://doi.org/10.1007/s11222-026-10906-9) · [arXiv](https://arxiv.org/abs/2412.11875) — Bayesian surrogate training on multiple data sources: a hybrid modeling strategy
- **作者**: Philipp Reiser, Paul-Christian Bürkner, Anneli Guthke
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 4
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出两种概率性混合建模策略，用于在代理模型训练中同时整合仿真数据与真实测量数据。第一种方法为每个数据源训练独立的代理模型，再通过加权组合其预测分布；第二种方法则训练单一代理模型，直接融合两类数据。两种方法均采用一种新颖的加权策略，该策略不依赖于代理模型的具体族类，可灵活应用于高斯过程、神经网络等常见代理形式。通过合成与真实案例研究，作者展示了混合策略在提升预测精度与覆盖概率方面的优势，并指出其可用于诊断仿真模型的系统偏差。该工作本质上属于统计计算中的模型逼近与不确定性量化问题，其加权融合思路对处理多源异构数据具有通用参考价值。对您而言，本文的加权策略与代理模型训练框架可作为统计计算方向的一个实用案例，但方法学新颖性有限，主要贡献在于应用层面的整合与验证。
- **关键技术**: `surrogate modeling`, `Bayesian model averaging`, `multi-source data fusion`, `weighted likelihood`, `predictive distribution combination`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的primary interest中的'statistical computing (numerical methods, algorithm)'。加权融合多源数据的策略可迁移至您熟悉的'软件开发'与'非参数统计'工具箱，例如在因果推断中整合实验与观测数据。但核心方法（加权似然、模型平均）属于成熟技术，新颖性有限，属于中期可做的参考案例——需先在'moderately_familiar'的'identification theory in causal inference'上理解数据融合的识别条件，才能将本文思路转化为具体方法贡献。

### 12. [10.1007/s11222-026-10896-8](https://doi.org/10.1007/s11222-026-10896-8) · [arXiv](https://arxiv.org/abs/2504.09349) — Neural posterior estimation on exponential random graph models: evaluating bias and implementation challenges
- **作者**: Yefeng Fan, Simon Richard White
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 4
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文系统研究了神经后验估计（NPE）在指数随机图模型（ERGM）中的应用。ERGM 的似然函数难以计算，传统贝叶斯推断需通过交换算法进行大量模拟，可扩展性差。NPE 利用神经网络密度估计器从模拟数据中学习后验分布，已在宇宙学等领域成功应用，但在 ERGM 中尚缺乏系统评估。作者首次实现了 ERGM 的 NPE 推断，并与传统贝叶斯方法、神经似然估计和神经比率估计进行了比较。在合成数据实验中，用 50 万次模拟训练的 NPE 可替代传统方法约 40 亿次模拟，实现实时后验估计。文章重点分析了 ERGM 特有的偏差来源和实现挑战，为统计计算中的模拟推断方法提供了实证基准。
- **关键技术**: `neural posterior estimation`, `simulation-based inference`, `exponential random graph models`, `normalizing flows`, `exchange algorithm`
- **为什么对您有用**: 本文属于统计计算（stat_computing）方向的 gateway reading，对您作为统计计算领域的 outsider 非常友好：问题设定清晰（ERGM 的双重难解似然），方法机制（NPE 用 normalizing flows 学习后验）解释充分，且明确给出了计算成本对比（50万 vs 40亿次模拟）。您的武器库中 'software development' 和 'high-dimensional asymptotics' 足以支撑理解本文的模拟设计和偏差分析，但核心的 normalizing flows 和 SBI 工具链属于 moderately_familiar 之外的领域，因此暂不可做——若想进入该方向，需先在 'M-estimation theory' 上长肌肉以理解密度估计的收敛性。

### 13. [10.1007/s11222-026-10928-3](https://doi.org/10.1007/s11222-026-10928-3) — Approximate Bayesian Computation of reduced-bias extreme risk measures from heavy-tailed distributions
- **作者**: Jonathan El Methni, Stéphane Girard
- **期刊/来源**: Statistics and Computing
- **机构**: Université Grenoble Alpes · Centre Inria de l'Université Grenoble Alpes
- **分类**: vol 36 · issue 4
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对重尾分布下极端风险测度（如尾部风险值）的估计问题，提出用 Refined Pareto Distribution (RPD) 替代经典的广义帕累托分布 (GPD) 来对超阈值分布进行二阶近似，从而降低估计偏差。参数估计采用近似贝叶斯计算 (ABC) 方法，这是一种模拟推断技术，无需显式似然函数，适用于复杂模型。基于 ABC 得到的 RPD 参数后验样本，进一步构造了极端风险测度的缩减偏差估计量及其可信区间。数值实验表明，该 ABC 估计量在多种重尾分布下表现良好，并在两个保险理赔数据集上展示了实用性。对您而言，本文的 ABC 框架与您统计计算（数值方法）的兴趣直接相关，且其模拟推断思路可迁移至您熟悉的因果推断或高维设定中处理复杂似然问题。
- **关键技术**: `Approximate Bayesian Computation (ABC)`, `Refined Pareto Distribution (RPD)`, `extreme value theory`, `reduced-bias estimation`, `credible intervals`
- **为什么对您有用**: 本文属于统计计算（ABC 方法）在极端值估计中的应用，与您的 primary interest 中统计计算（数值方法）直接相关。您的武器库中 very_familiar 的软件开发和 high-dimensional asymptotics 可用于复现和扩展其 ABC 算法（如调整模拟步数或先验），但核心的 ABC 模拟推断机制您目前仅 moderately_familiar，需先熟悉 ABC 的接受/拒绝采样和核密度调节步骤。中期可做：将 ABC 框架与您熟悉的 U-statistics 或因果推断中的逆概率加权结合，开发新的缩减偏差估计量。

### 14. [10.1007/s11222-026-10923-8](https://doi.org/10.1007/s11222-026-10923-8) — A continuous gaussian mixture approach to sample multivariate gaussians constrained by linear inequalities
- **作者**: Mehdi Amrouche, Jérôme Idier, Hervé Carfantan
- **期刊/来源**: Statistics and Computing
- **机构**: Centre National de la Recherche Scientifique · Université Toulouse III - Paul Sabatier · Institut de Recherche en Astrophysique et Planétologie · École Centrale de Nantes · Laboratoire des Sciences du Numérique de Nantes · Nantes Université
- **分类**: vol 36 · issue 4
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文提出一种新的MCMC方法，用于在线性不等式约束下从截断多元高斯（TMG）分布中采样。该方法适用于底层无约束高斯分布为病态（improper）的情况，且对约束数量无限制。核心机制基于连续高斯混合分解，通过新的积分恒等式导出，在可行域内精确成立。算法采用分块Gibbs更新结合拒绝步骤，以渐近精确地从TMG中采样。实验表明，在一系列具有挑战性的设定下，该方法优于现有最先进替代方案。对您而言，该方法在统计计算中提供了处理高维约束采样问题的实用工具，尤其适用于需要高效MCMC的贝叶斯推断或因果推断中的后验采样场景。
- **关键技术**: `blocked Gibbs sampling`, `continuous Gaussian mixture decomposition`, `truncated multivariate Gaussian`, `rejection sampling`, `linear inequality constraints`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的primary interest中的'statistical computing (numerical methods, algorithm)'。您武器库中的'软件开发和逆问题'技能可直接用于实现或扩展该算法。该方法是中期可做的：您需要先在moderately_familiar的M-estimation理论中熟悉MCMC收敛诊断，但核心的Gibbs采样和拒绝采样是very_familiar的。

### 15. [10.1007/s11222-026-10907-8](https://doi.org/10.1007/s11222-026-10907-8) · [arXiv](https://arxiv.org/abs/2507.21982) — Preconditioned Discrete-HAMS: A Second-order Irreversible Discrete Sampler
- **作者**: Yuze Zhou, Zhiqiang Tan
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 4
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对离散分布采样问题，提出 Preconditioned Discrete-HAMS (PDHAMS) 算法。该算法在 DHAMS 基础上引入势函数的二阶（二次）近似，利用 Gaussian integral trick 避免直接采样成对马尔可夫随机场，从而在保持广义细致平衡（不可逆采样）的同时，对二次势函数目标分布实现无拒绝采样。数值实验表明 PDHAMS 在多个离散分布采样任务上一致优于 NCG、AVG 和 DHAMS 等基线方法。对您而言，该工作属于统计计算中的 MCMC 方法创新，其核心机制（二阶近似 + 不可逆性）与您对算法设计和数值方法的兴趣直接相关，可作为 gateway reading 了解离散采样前沿。
- **关键技术**: `Gaussian integral trick`, `second-order approximation`, `irreversible Markov chain`, `generalized detailed balance`, `rejection-free sampling`
- **为什么对您有用**: 本文属于统计计算（MCMC 方法）的创新，直接对应您的 primary interest 中的 'statistical computing (numerical methods, algorithm)'。您武器库中的 'software development' 和 'high-dimensional asymptotics' 可用于评估其算法实现和收敛性分析，但核心的离散采样机制（Gaussian integral trick、不可逆链）属于您 moderately_familiar 之外的领域，因此属于 gateway reading：值得花时间读全文以了解离散 MCMC 的当前技术状态，但暂不可做 follow-up 工作（缺离散 MCMC 的收敛理论工具）。

### 16. [10.1007/s11222-026-10897-7](https://doi.org/10.1007/s11222-026-10897-7) — Multivariate Markov switching BEKK models: filtering, estimation and data analysis
- **作者**: Maddalena Cavicchioli, Jie Cheng
- **期刊/来源**: Statistics and Computing
- **机构**: University of Modena and Reggio Emilia · Keele University
- **分类**: vol 36 · issue 4
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文扩展了标准多元BEKK模型，引入不可观测的马尔可夫链来驱动无条件相关性和参数，形成马尔可夫切换BEKK模型。核心贡献在于提出了两种基于扩展卡尔曼滤波的估计算法，这些算法源自模型的状态空间表示。数值实验验证了所提非线性估计方法的有效性。在金融收益率数据上的实证分析表明，该模型能很好地解释高波动持续性和相关性变化，并通过与马尔可夫切换CCC和DCC模型的比较，展示了其在分析股市金融传染和风险价值预测方面的优势。对您而言，本文在统计计算（滤波算法设计）和金融时间序列建模方面提供了具体的技术参考，但方法论创新性有限，属于应用拓展。
- **关键技术**: `Extended Kalman filter`, `State space representation`, `Markov switching BEKK model`, `Nonlinear estimation`, `Financial contagion analysis`
- **为什么对您有用**: 本文属于统计计算（滤波算法）在金融时间序列中的应用，与您的primary interest中的'statistical computing (numerical methods, algorithm)'有直接关联。您可以用'very_familiar'中的'high-dimensional asymptotics'和'software development'来评估其算法效率或复现实证部分。但核心方法（扩展卡尔曼滤波）不在您的武器库中，属于'暂不可做'——需要先熟悉状态空间模型和滤波理论。

### 17. [10.1007/s11222-026-10882-0](https://doi.org/10.1007/s11222-026-10882-0) · [arXiv](https://arxiv.org/abs/2401.09696) — Rejection sampling with vertical weighted strips
- **作者**: Andrew M. Raim, James A. Livsey, Kyle M. Irimata
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 4
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文提出一种基于垂直加权条带（vertical weighted strips）的拒绝采样方法，用于从加权密度（基密度与权重函数的乘积）中生成精确样本。该方法将目标密度分解为有限混合，每个分量对应支撑集的一个划分区域，并在每个区域上通过权重函数的上界构造提议分布。与自适应拒绝采样等算法不同，本方法不要求权重函数满足对数凹性等正则条件，适用性更广。拒绝概率的上界可解析表达，用于在采样前评估提议效率；进一步提出基于该上界贡献的递归二分划分策略，以优化分区。数值实验以 von Mises Fisher 分布为例展示了框架的有效性。对您而言，本文属于统计计算中的采样方法创新，与您的统计计算兴趣直接相关，且其分区优化策略可能启发您在高阶 U-统计量计算中类似的自适应划分思路。
- **关键技术**: `rejection sampling`, `weighted density`, `piecewise majorization`, `adaptive partition`, `von Mises Fisher distribution`
- **为什么对您有用**: 本文属于统计计算中的采样方法，直接对应您的 primary interest 中的 statistical computing。其分区优化策略（基于上界贡献的递归二分）与您在高阶 U-统计量计算中使用的树宽/张量收缩优化有潜在类比——都是通过划分支撑集来降低计算或采样成本。目前属于中期可做：您需要先在 moderately_familiar 的 HOIF 或高阶 U-统计量理论上长肌肉，才能将这种自适应划分思想迁移到您的计算框架中。

### 18. [10.1007/s11222-026-10895-9](https://doi.org/10.1007/s11222-026-10895-9) — Robust Variational Gaussian Process Regression for Count Data with the Trimmed Marginal Likelihood
- **作者**: Daniel Andrade
- **期刊/来源**: Statistics and Computing
- **机构**: Hiroshima University
- **分类**: vol 36 · issue 4
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 针对计数数据（如住院人数）的 GP 回归对异常值敏感的问题，提出用负二项似然替换高斯似然，并通过优化一个截断变分下界（trimmed variational lower bound）来训练模型。截断比例对应异常值数量的上界，在稀疏变分推断框架下推导出高效且对异常值鲁棒的训练算法。进一步提出自动调优截断比例的方法，避免保守估计导致统计效率损失。实验表明该方法在预测不确定性上几乎不受训练数据异常值影响，并优于贝叶斯数据重加权和 γ-散度方法。对您而言，本文的截断变分下界思路可迁移到您熟悉的非参数统计和因果推断中的稳健估计问题，但核心机器（变分 GP、负二项似然）不在您的武器库中，属于暂不可做的方向。
- **关键技术**: `trimmed variational lower bound`, `sparse variational inference`, `negative binomial likelihood`, `robust Gaussian process regression`, `Bayesian data re-weighting`
- **为什么对您有用**: 本文属于统计计算方向，与您的 primary interest 中的统计计算（numerical methods, algorithm）直接相关。但核心方法（变分 GP、负二项似然、截断变分推断）不在您的技术武器库中（very_familiar 和 moderately_familiar 均未覆盖），属于暂不可做的方向。不过，截断变分下界的思路（用上界控制异常值影响）可能对您熟悉的稳健估计问题有启发，但需要先补充变分推断和 GP 的基础知识才能深入。

### 19. [10.1007/s11222-026-10917-6](https://doi.org/10.1007/s11222-026-10917-6) — On the Observability of Copula State Space Models using a Bayesian Approach
- **作者**: Ariane Hanebeck, Claudia Czado
- **期刊/来源**: Statistics and Computing
- **机构**: Technical University of Munich
- **分类**: vol 36 · issue 4
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对 copula 状态空间模型（SSM）的可观测性问题，提出了一种新颖的可观测性定义及数值评估方法。传统 copula SSM 的估计方法直接应用于数据而未验证其可靠性，本文填补了这一空白。作者将参数与状态轨迹合并为增广状态，并基于观测轨迹恢复该状态。由于非线性 SSM 的可观测性非全局性质，本文采用准随机、确定性、低差异采样的离散密度近似点（设计轨迹）代表观测与状态轨迹的联合分布。通过贝叶斯 MCMC 框架计算，若对所有设计轨迹均收敛，则模型可观测；否则不可观测。此外，还提出了可观测程度的量化指标。实验表明，对于单变量和多变量时间序列的 copula SSM，该方法表现出高可观测性。本文对您作为统计计算研究者有直接参考价值，其可观测性定义与数值验证框架可迁移至您熟悉的因果推断或高维统计中的复杂模型诊断问题。
- **关键技术**: `Copula State Space Models`, `Observability Definition`, `Bayesian MCMC`, `Quasi-Random Sampling`, `Low-Discrepancy Sequences`, `Discrete Density Approximation`
- **为什么对您有用**: 本文属于统计计算方向，直接关联您的 primary interest 中的 statistical computing。其提出的可观测性数值评估方法（基于设计轨迹和 MCMC 收敛性）可视为一种模型诊断工具，您可以用 very_familiar 的软件开发和 high-dimensional asymptotics 技能来复现或扩展该方法到更复杂的因果模型（如 proximal causal inference 中的 latent variable 模型）。中期可做：需先在 moderately_familiar 的 identification theory 上理解 latent variable 模型的可观测性条件，再结合本文的数值框架进行验证。

## 其他  *(other, 2 篇)*

### 1. [10.1007/s11222-026-10898-6](https://doi.org/10.1007/s11222-026-10898-6) · [arXiv](https://arxiv.org/abs/2508.07049) — Statistical inference for autoencoder-based anomaly detection after representation learning-based domain adaptation
- **作者**: Tran Tuan Kiet, Nguyen Thang Loi, Vo Nguyen Le Duy
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 4
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出 STAND-DA 框架，在表示学习域适应（DA）后，对基于自编码器的异常检测（AD）进行统计推断。核心问题是：DA 引入的额外不确定性使 AD 结果难以给出有效的统计结论。方法基于选择性推断（Selective Inference, SI）框架，计算检测到异常的条件 p 值，并严格将假阳性率控制在预设水平 α 以下。为克服 SI 在深度模型中的计算瓶颈，作者开发了 GPU 加速的 SI 实现，显著提升了可扩展性和运行效率。在合成和真实数据集上的实验验证了理论结果和计算效率。该工作将经典假设检验框架与深度学习域适应结合，属于统计计算与机器学习交叉的应用型方法。
- **关键技术**: `Selective Inference`, `Conditional p-value`, `Autoencoder-based anomaly detection`, `Representation learning-based domain adaptation`, `GPU-accelerated computation`
- **为什么对您有用**: 本文连接您的统计计算（GPU 加速实现）和假设检验（SI 框架）兴趣，但核心方法（选择性推断）不在您的技术武器库中，且问题设定（域适应后的异常检测）与您的主要研究方向（因果推断、高维统计）距离较远。作为 gateway reading 价值有限：入门门槛较高（需理解 SI 和 DA 背景），且方法学 novelty 一般（主要是 SI 在特定应用场景的工程实现）。暂不可做——核心机器（选择性推断的条件分布计算）不在武器库中。

### 2. [10.1007/s11222-026-10884-y](https://doi.org/10.1007/s11222-026-10884-y) · [arXiv](https://arxiv.org/abs/2502.05102) — Time series analysis of rankings: A GARCH-type approach
- **作者**: Luiza S. C. Piancastelli, Wagner Barreto-Souza
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 4
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对时间序列排名数据提出了一类新的模型，即排名GARCH模型。模型假设给定过去排名后，当前排名服从Mallows分布，其隐式依赖于一个距离度量；通过该距离的条件期望引入自回归和反馈成分，从而刻画时间动态。作者建立了模型的平稳性和遍历性等理论性质。参数估计采用最大似然估计（完全观测数据）或蒙特卡洛EM算法（缺失数据）。模拟研究验证了估计量在有无缺失数据场景下的表现，并以2015-2019年职业网球选手周排名数据为例进行应用。该模型将GARCH思想扩展到非数值的排名数据，填补了时间序列排名分析的方法空白。对您而言，本文属于统计计算与建模的应用方向，与您的主要兴趣（因果推断、高维统计等）无直接交集，但可作为时间序列非标准数据建模的参考。
- **关键技术**: `Mallows distribution`, `GARCH-type model`, `Monte Carlo EM algorithm`, `maximum likelihood estimation`, `stationarity and ergodicity`
- **为什么对您有用**: 本文属于统计计算与建模的应用方向，与您的主要兴趣（因果推断、高维统计等）无直接交集。作为gateway-reading，本文对非标准时间序列数据建模有清晰阐述，但武器库中缺乏处理排名数据的专用工具（如Mallows分布、排序距离度量），暂不可做。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

