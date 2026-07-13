# Technometrics — Vol 68  Issue 1  ·  2026-07-13

- 共 23 篇 · Technometrics
- 目录核对 ✅ 23 篇全部抓到（对照 OpenAlex 23 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Technometrics》第68卷第1期的23篇论文，整体上呈现出两条清晰的主线：**统计计算与实验设计**（尤其是高斯过程代理模型与主动学习）以及**工程可靠性/退化建模**。前者占据了近半数论文，后者则集中在剩余寿命预测与过程监控。此外，还有少量书评、应用导向的方法（如共享单车模式、AI调参）和一篇天体物理校准论文，与核心主线关联较弱。

在**统计计算与实验设计**主线中，高斯过程（GP）是绝对的核心工具，但各篇切入角度不同。多篇论文聚焦于**主动学习/序贯设计**以提升样本效率：例如，“An Adjacency-Adaptive Gaussian Process Method”通过邻接向量引入流形信息，并采用复合似然避免矩阵求逆；“Solving Bayesian Inverse Problems Using Gaussian Process Regression with Goal-Oriented Active Learning”将逐步不确定性缩减框架推广到逆问题，提出两种可解析计算的目标导向策略；“Active Learning of Piecewise Gaussian Process Surrogates”则针对分段GP，强调需同时考虑偏差与方差；“Efficient Active Learning Strategies for Computer Experiments”结合筛选设计与新型核函数（MIM核）来优化初始点选择。另一批论文关注**计算效率与可扩展性**：“A Scalable Variational Bayes Approach to Fit High-Dimensional Spatial Generalized Linear Mixed Models”用变分贝叶斯实现百万级空间数据的推断；“A Local Variational Inference Framework for the Orthogonal Gaussian Process Calibration”提出无梯度局部变分推断以降低校准计算成本；“Information Sharing for Robust and Stable Cross-Validation”则通过追踪局部极小值匹配来解决非凸优化下交叉验证的不稳定性。这些工作共同展示了GP在代理建模、校准、逆问题中的最新计算策略，尤其是主动学习准则的设计与变分推断的适配。

另一条主线是**退化过程建模与剩余寿命预测**，集中在工程可靠性领域。多篇论文针对传统Wiener过程或Gamma过程的局限提出扩展：“Degradation Data Analysis based on Wiener Process with a Nonlinear Drift and a Stochastic Volatility”用函数主成分分析非参数估计随机波动率；“A Periodic Fractional Wiener Process for Remaining Useful Life Prediction of Photovoltaic Systems with Long-Range Dependence”引入分数布朗运动刻画长程依赖与准周期性；“Remaining Useful Life Prediction of Lithium-Ion Batteries Using Monotone Decomposition”则通过单调分解将容量退化信号分离为趋势项与波动项，再分别用GP和深度自回归模型预测。这些工作均以实际工程数据（光伏、锂电池）为驱动，方法上强调对退化特征（非线性、随机波动、长程依赖）的精细刻画。

对于因果推断方向的研究者，本期直接相关的论文较少，但**统计计算主线中的主动学习与序贯设计**（如“Solving Bayesian Inverse Problems”、“Active Learning of Piecewise Gaussian Process Surrogates”）中的不确定性量化与目标导向策略，可能对因果推断中的实验设计或反事实预测有间接启发。**半参数效率**方向无直接论文，但“Orthogonal Calibration via Posterior Projections”中的正交偏差与后验投影思想，与半参数方法中的正交性概念有潜在联系。**高维统计**方向，本期仅“Information Sharing for Robust and Stable Cross-Validation”涉及高维稳健回归中的模型选择，其余高维内容（如空间GLMM的变分贝叶斯）更偏向计算而非理论。建议优先关注统计计算主线中涉及主动学习与变分推断的几篇，以及退化建模中处理复杂随机过程的论文。

## 统计计算 / 算法  *(stat_computing, 7 篇)*

### 1. [10.1080/00401706.2025.2564129](https://doi.org/10.1080/00401706.2025.2564129) — An Adjacency-Adaptive Gaussian Process Method for Sample Efficient Response Surface Modeling and Test-Point Acquisition
- **作者**: Stanford Samuel Martinez, Adel Alaeddini
- **期刊/来源**: Technometrics
- **机构**: The University of Texas at San Antonio · Southern Methodist University
- **分类**: vol 68 · issue 1 · pp 202-214
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对复杂系统响应面建模中样本效率低的问题，提出了一种邻接自适应高斯过程方法。该方法在半监督与主动学习框架下，利用邻接向量（adjacency vectors）引入流形信息，为高斯过程协方差函数增加数据驱动的特征。作者还给出了基参数的解析形式，实现了自适应特征提取，并采用复合似然函数进行训练，避免了边际似然中昂贵的矩阵求逆。通过大量仿真与案例研究，与多种常见方法对比，验证了该方法在样本效率与预测精度上的优势。对您而言，本文在统计计算中探索了高斯过程与流形学习的结合，其复合似然训练策略可视为一种计算效率优化技巧，与您对统计计算中数值方法的兴趣相关。
- **关键技术**: `Gaussian process`, `semi-supervised learning`, `active learning`, `manifold learning`, `composite likelihood`, `adjacency vectors`
- **为什么对您有用**: 本文属于统计计算方法改进，直接对应您 primary interest 中的 statistical computing。其复合似然替代边际似然的思路，可视为一种计算-精度权衡策略，与您 moderately_familiar 的 M-estimation 理论有潜在联系（复合似然可看作一种 M-estimator）。但核心机制（流形信息嵌入高斯过程）与您武器库中 very_familiar 的非参数统计和软件工具距离较远，属于**中期可做**：需先在 moderately_familiar 的 M-estimation 理论上加强，才能深入分析其复合似然的渐近性质。

### 2. [10.1080/00401706.2025.2561745](https://doi.org/10.1080/00401706.2025.2561745) — Solving Bayesian Inverse Problems Using Gaussian Process Regression with Goal-Oriented Active Learning
- **作者**: Paul Lartaud, Philippe Humbert, Josselin Garnier
- **期刊/来源**: Technometrics
- **机构**: École Polytechnique · Commissariat à l'Énergie Atomique et aux Énergies Alternatives · CEA DAM Île-de-France · Centre de Mathématiques Appliquées de l'École polytechnique · Institut Polytechnique de Paris · Laboratoire de Mathématiques Blaise Pascal
- **分类**: vol 68 · issue 1 · pp 172-185
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究在贝叶斯逆问题中，使用高斯过程回归构建替代模型时的序贯设计策略，目标是在有限计算预算下高效地选择新设计点以降低后验不确定性。核心方法基于逐步不确定性缩减框架，提出了两种目标导向策略：约束集查询策略将搜索空间限制在最大后验估计的Mahalanobis距离球内，以改进MMSE设计；逆问题SUR策略以后验加权积分均方预测误差作为不确定性度量，并证明了不确定性泛函的几乎必然收敛性。两种策略在高斯过程替代模型下均可解析计算，无需额外近似。数值实验中，CSQ和IP-SUR在多个测试案例中均优于标准目标导向设计，尤其在后验分布尾部区域有显著改进。本文的方法学贡献在于将SUR框架从单纯预测问题推广到逆问题设定，并提供了收敛性保证。对您而言，这是一篇统计计算方向的论文，涉及高斯过程、序贯设计和贝叶斯逆问题，与您的统计计算兴趣直接相关，可作为了解该领域标准方法的入门读物。
- **关键技术**: `Gaussian process regression`, `Stepwise Uncertainty Reduction`, `sequential design`, `Bayesian inverse problem`, `Mahalanobis distance`, `integrated mean squared prediction error`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的primary interest中的'statistical computing (numerical methods, algorithm)'。武器库中'nonparametric statistics'和'high-dimensional asymptotics'可用于分析GP替代模型的收敛速率，但核心的序贯设计框架（SUR、主动学习）不在您的very_familiar或moderately_familiar列表中。本文是gateway reading：它清晰阐述了序贯设计的基本框架和两种具体策略，数学上可追踪（GP、MSE、收敛性证明），适合作为进入主动学习/序贯实验设计领域的入门材料。武器库足以理解方法细节，但若要跟进（如提出新的不确定性度量或改进计算效率），需在'statistical computing'方向补充主动学习相关工具。暂不可做：核心机器（序贯设计、SUR框架）不在武器库中，但本文本身是好的入门读物，值得花时间读全文以了解该领域的基本概念和问题设定。

### 3. [10.1080/00401706.2025.2540970](https://doi.org/10.1080/00401706.2025.2540970) · [arXiv](https://arxiv.org/abs/2409.12890) — Information Sharing for Robust and Stable Cross-Validation
- **作者**: David Kepplinger, Siqi Wei
- **期刊/来源**: Technometrics
- **分类**: vol 68 · issue 1 · pp 54-64
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对高维稳健线性回归中惩罚参数选择问题，提出一种新的自适应交叉验证策略。传统CV在非凸目标函数下因多重局部极小值导致性能不稳定，本文通过追踪每个超参数组合和数据子集的多个局部极小值，并设计匹配方案将全数据上的极小值与CV折上的最佳匹配极小值对齐，从而正确评估预测误差。该方法有效降低了性能估计的变异性，使CV曲线更平滑，显著提升了稳健惩罚估计量的可靠性和实用性。核心贡献在于解决了非凸优化下CV的局部极小值错配问题，属于计算统计方法创新。对您而言，该工作展示了如何通过算法设计改善非凸问题的模型选择，与您统计计算兴趣中的数值方法方向直接相关，且其匹配策略可迁移至其他非凸估计场景。
- **关键技术**: `adaptive cross-validation`, `robust penalized regression`, `non-convex optimization`, `multiple local minima matching`
- **为什么对您有用**: 本文直接关联您的统计计算兴趣，特别是数值方法和算法设计。您武器库中'软件开发和M估计理论'可用来复现或扩展其匹配策略至其他非凸估计问题（如高维因果推断中的正则化）。中期可做：需先在moderately_familiar的M估计理论上加深对非凸损失函数局部极小值行为的理解，然后可尝试将本文的CV匹配方案应用于您熟悉的因果推断中的高维IV或倾向得分模型。

### 4. [10.1080/00401706.2025.2561141](https://doi.org/10.1080/00401706.2025.2561141) · [arXiv](https://arxiv.org/abs/2402.15705) — A Scalable Variational Bayes Approach to Fit High-Dimensional Spatial Generalized Linear Mixed Models
- **作者**: Jin Hyung Lee, Ben Seiyon Lee
- **期刊/来源**: Technometrics
- **分类**: vol 68 · issue 1 · pp 146-158
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对高维空间广义线性混合模型（SGLMM）的可扩展计算问题，提出两种变分贝叶斯（VB）方法，适用于连续空间域中中等规模（百万级）的高斯和非高斯离散空间数据。方法核心是利用半参数近似（如基函数表示）对潜在空间过程进行低秩逼近，并结合并行计算实现计算效率的大幅提升。与黄金标准MCMC相比，VB方法在推断和预测性能上相当，但计算速度提升高达3600倍；在多数设定下优于INLA和Hamiltonian Monte Carlo等前沿替代方法。数值实验和真实数据应用验证了方法的有效性。本文的VB框架使得在普通笔记本电脑上即可建模数百万个离散非高斯空间观测，显著降低了高级空间建模工具的使用门槛。对您而言，本文展示了变分推断在大规模空间统计中的实用化路径，其计算加速策略（低秩近似+并行化）可迁移至您的高维因果推断或U统计量计算中，属于统计计算方向的具体算法创新。
- **关键技术**: `Variational Bayes`, `spatial generalized linear mixed models`, `low-rank basis approximation`, `parallel computing`, `INLA comparison`, `Hamiltonian Monte Carlo`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您primary interest中的'statistical computing (numerical methods, algorithm)'。其核心贡献——通过半参数低秩近似和并行化实现VB对大规模空间模型的实用化——与您武器库中'very_familiar'的'nonparametric statistics'和'high-dimensional asymptotics'高度契合：您可以用非参数逼近的minimax理论分析其低秩近似的误差-计算权衡，或用高维渐近工具刻画VB后验的收敛速度。中期可做：若您想将类似VB加速策略推广至因果推断中的空间混杂调整，需先在'moderately_familiar'的'semiparametric theory'上补强空间过程的影响函数推导。

### 5. [10.1080/00401706.2025.2561746](https://doi.org/10.1080/00401706.2025.2561746) · [arXiv](https://arxiv.org/abs/2301.08789) — Active Learning of Piecewise Gaussian Process Surrogates
- **作者**: Chiwoo Park, Robert Waelder, Bonggwon Kang, Benji Maruyama, Soondo Hong, Robert B. Gramacy
- **期刊/来源**: Technometrics
- **分类**: vol 68 · issue 1 · pp 186-201
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对分段高斯过程（Jump GP）替代模型的主动学习问题展开研究。Jump GP 在输入空间的不同区域内连续，但在区域边界处允许跳跃，适用于材料自主设计、智能工厂配置等存在不连续性的物理/计算机模拟实验。核心贡献在于：将传统 GP 主动学习中的采集函数（如期望改进、预测方差）适配到 Jump GP 框架时，发现仅考虑模型不确定性（方差）是不够的，必须额外考虑模型偏差（bias）。为此，作者开发了 Jump GP 模型的偏差与方差联合估计器，并基于此设计了新的主动学习准则。方法在一系列合成基准和不同复杂度的真实模拟实验上展示了优势。对您而言，本文属于统计计算与实验设计交叉的实用方法，其偏差-方差分解思路可迁移到您熟悉的非参数统计与因果推断中的模型选择问题。
- **关键技术**: `Gaussian process surrogates`, `piecewise GP (Jump GP)`, `active learning acquisition functions`, `bias-variance decomposition`, `model bias estimation`
- **为什么对您有用**: 本文属于统计计算（stat_computing）中的主动学习方法，与您 primary interest 中的统计计算和软件工具开发直接相关。您武器库中非常熟悉的非参数统计和 minimax 界可用于分析 Jump GP 的偏差-方差权衡的理论性质；中期可做：若您想将偏差校正思想迁移到因果推断（如 DML 中的 nuisance 函数估计），需先在 moderately_familiar 的 semiparametric theory 上进一步熟悉 influence function 的偏差结构。

### 6. [10.1080/00401706.2025.2560344](https://doi.org/10.1080/00401706.2025.2560344) — A Local Variational Inference Framework for the Orthogonal Gaussian Process Calibration
- **作者**: Jingru Huang, Hui Lan, Yan Wang, Linhan Ouyang
- **期刊/来源**: Technometrics
- **机构**: Beijing University of Technology · Nanjing University of Aeronautics and Astronautics
- **分类**: vol 68 · issue 1 · pp 137-145
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对正交高斯过程校准（OGP calibration）中计算复杂度高且易陷入局部最优的问题，提出了一种无梯度的局部变分推断框架。OGP calibration 是计算机模型与物理观测数据匹配的经典方法，其估计量具有快速收敛率和良好不确定性量化能力，但优化困难。作者通过引入变分密度近似校准参数和模型偏差，并利用最小二乘估计作为先验信息来避免局部最优，从而在不显著牺牲精度的前提下大幅降低计算成本。数值模拟和实际案例验证了该方法的有效性。对于您而言，本文展示了统计计算中变分推断与高斯过程模型的结合，属于统计计算方向，可作为算法设计的参考。
- **关键技术**: `variational inference`, `Gaussian process calibration`, `gradient-free optimization`, `least-squares prior`, `orthogonal Gaussian process`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的 primary interest 中的 statistical computing。您武器库中的软件开发和 M-estimation 理论可用于分析其变分近似的收敛性，但核心的变分推断机制您目前 moderately_familiar，需先熟悉变分下界推导才能深入。暂不可做：缺乏变分推断的实操经验。

### 7. [10.1080/00401706.2025.2546366](https://doi.org/10.1080/00401706.2025.2546366) · [arXiv](https://arxiv.org/abs/2501.13841) — Efficient Active Learning Strategies for Computer Experiments
- **作者**: Difan Song, V. Roshan Joseph
- **期刊/来源**: Technometrics
- **分类**: vol 68 · issue 1 · pp 65-78
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对计算机实验中的主动学习问题，提出了一种结合筛选设计（MOFAT）与新型相关函数（MIM核）的高效策略。研究设定为使用高斯过程代理模型进行仿真或优化，目标是减少昂贵函数评估次数。核心方法包括：用最大单因子一次一变量（MOFAT）设计替代传统的空间填充设计作为初始点，并引入乘法逆多二次（MIM）核作为高斯过程的相关函数，该核在核理论中已知但未用于主动学习。通过将筛选步骤自动融入模型估计，提出了集成的MOFAT-MIM策略。理论分析和模拟表明，该方法在代理建模和优化目标上均显著优于现有方法，并在真实的气相渗透实验中验证了效果。对您而言，本文展示了统计计算中实验设计（初始点选择）与核函数设计（MIM核）的巧妙结合，其思路可迁移至您熟悉的非参数统计和高维渐近分析领域，但核心机器（主动学习与高斯过程优化）不在您当前武器库中，属于暂不可做的方向。
- **关键技术**: `Gaussian process surrogate`, `active learning`, `space-filling design`, `one-factor-at-a-time (OFAT) design`, `inverse multiquadric (IMQ) kernel`, `screening design`
- **为什么对您有用**: 本文属于统计计算方向，但核心是实验设计与高斯过程代理模型，与您的主要兴趣（因果推断、高维统计）无直接交集。作为gateway reading，本文对主动学习领域的入门者较为友好，清晰阐述了初始设计（MOFAT）和核函数（MIM）的动机，但未涉及您熟悉的minimax界或U统计量工具。武器库中very_familiar的非参数统计和高维渐近分析可帮助理解理论部分，但主动学习与高斯过程优化的核心方法（如采集函数、贝叶斯优化）不在当前武器库中，属于暂不可做方向。建议仅作为了解计算机实验领域的快速阅读，无需深入。

## 天体统计  *(astrostats, 1 篇)*

### 1. [10.1080/00401706.2025.2526428](https://doi.org/10.1080/00401706.2025.2526428) · [arXiv](https://arxiv.org/abs/2404.03152) — Orthogonal Calibration via Posterior Projections with Applications to the Schwarzschild Model
- **作者**: Antik Chakraborty, Jonelle L. Walsh, Louis Strigari, Bani K. Mallick, Anirban Bhattacharya
- **期刊/来源**: Technometrics
- **分类**: vol 68 · issue 1 · pp 14-23
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对天体物理中 Schwarzschild 轨道叠加模型的校准问题，提出了一种贝叶斯多元校准方法。该模型用于研究黑洞与宿主星系的动力学，其输出为多元物理测量值，需要找到最优参数并量化不确定性。作者通过正交偏差函数确保参数可识别性，核心创新在于将后验投影到合适的函数空间，从而允许对偏差函数使用任意非参数先验（如 BART），而不必局限于高斯过程。方法基于 Hilbert 空间理论构建函数投影，并给出了有限维近似。在真实数据应用中，多元校准解决了单变量校准导致的矛盾。本文是典型的 astrostatistics 应用，方法学贡献在于将后验投影与正交偏差结合，但理论深度有限。
- **关键技术**: `Bayesian calibration`, `orthogonal bias functions`, `posterior projection`, `Hilbert space projection`, `BART prior`, `multivariate outcomes`
- **为什么对您有用**: 本文属于 astrostatistics 的 gateway reading：它清晰阐述了天体物理中的校准问题（Schwarzschild 模型）、数据结构和不确定性来源，对统计学家友好。武器库中的非参数统计和贝叶斯方法足以理解全文，但方法学 novelty 不高（后验投影+正交偏差并非全新框架）。值得花时间读全文，作为进入 astrostatistics 领域的入门材料，但无需深入跟进其理论细节。

## 其他  *(other, 15 篇)*

### 1. [10.1080/00401706.2026.2615594](https://doi.org/10.1080/00401706.2026.2615594) — Partial Least Squares Regression: and Related Dimension Reduction Methods
- **作者**: David J. Olive
- **期刊/来源**: Technometrics
- **分类**: vol 68 · issue 1 · pp 216-218
- 相关性 4/10 · novelty: `survey`
- **摘要**: 这是一本关于偏最小二乘回归（PLS）及相关降维方法的专著，重点介绍了包络理论（envelope theory）在降维中的应用。书中系统阐述了PLS、主成分回归（PCR）、岭回归等方法的理论框架，并讨论了如何利用包络理论统一这些方法。作者从多元线性回归模型出发，逐步引入降维概念，并给出了详细的数学推导和算法实现。本书还涵盖了模型选择、预测评估以及实际数据分析案例。对于统计计算和降维方法感兴趣的读者，本书提供了扎实的理论基础和实用指导。然而，本书更偏向于经典多元统计和计算方法的综述，与您的主要研究兴趣（因果推断、高维统计、U-统计量等）的直接关联较弱。
- **关键技术**: `Partial Least Squares (PLS)`, `Envelope theory`, `Principal Component Regression (PCR)`, `Ridge regression`, `Dimension reduction`
- **为什么对您有用**: 本书属于统计计算和降维方法的综述性著作，与您的主要研究兴趣（因果推断、高维随机矩阵理论、高阶U-统计量）关联度较低。虽然包络理论在降维中有一定理论深度，但本书并未涉及您武器库中的核心工具（如非参数统计、极小极大界、因果推断的识别理论）。作为一本教材或参考书，它可能对您了解PLS等经典方法有帮助，但不太可能直接推动您当前的研究。建议仅作为背景阅读，不纳入深度阅读列表。

### 2. [10.1080/00401706.2026.2615598](https://doi.org/10.1080/00401706.2026.2615598) — Regression Models in Engineering and the Applied Sciences
- **作者**: Stan Lipovetsky
- **期刊/来源**: Technometrics
- **分类**: vol 68 · issue 1 · pp 224-225
- 相关性 4/10 · novelty: `survey`
- **摘要**: 这是一篇书评，介绍了一本涵盖多种回归模型及其在R软件中应用的书籍。该书分为四章，系统介绍了线性回归、非线性回归、广义线性模型、混合效应模型等常见回归技术，并提供了实际工程与科学项目的案例分析。书评概述了各章内容，强调了书籍的实用性和教学价值。对于统计研究者而言，这是一本入门级或教学参考书，而非前沿方法学贡献。
- **关键技术**: `linear regression`, `generalized linear models`, `mixed-effects models`, `R software`
- **为什么对您有用**: 本文为书评，不涉及新方法或理论，与您的主要研究方向（因果推断、高维统计、半参数理论等）无直接关联。作为教学参考，可能对统计软件教学或入门级回归应用有参考价值，但非研究前沿。

### 3. [10.1080/00401706.2026.2615595](https://doi.org/10.1080/00401706.2026.2615595) — Predictive Safety Analytics; Reducing Risk through Modeling and Machine Learning
- **作者**: Johanes Robert Kera, Dewanti
- **期刊/来源**: Technometrics
- **分类**: vol 68 · issue 1 · pp 218-219
- 相关性 3/10 · novelty: `application`
- **摘要**: 这是一本关于预测性安全分析的书籍，旨在将安全管理从回顾性分析转变为预测性风险识别。书中提出了一个数据驱动的框架，利用建模和机器学习技术来识别潜在风险。作者认为传统的安全指标已不足以应对现代复杂系统的风险。该书可能涵盖了数据收集、特征工程、模型选择和评估等标准流程。然而，从摘要来看，本书更偏向工业安全领域的应用实践，而非统计方法论的创新。对于统计研究者而言，其方法学深度有限，缺乏与因果推断、高维统计或半参理论等核心兴趣的直接关联。
- **关键技术**: `predictive modeling`, `machine learning`, `risk identification`
- **为什么对您有用**: 本书属于工业安全领域的应用书籍，与您的主要研究兴趣（因果推断、高维统计、半参理论等）无直接关联。其方法学贡献有限，不涉及您武器库中的具体工具。作为gateway reading，它并非统计方法的前沿读物，不值得投入时间精读。

### 4. [10.1080/00401706.2026.2615597](https://doi.org/10.1080/00401706.2026.2615597) · [arXiv](https://arxiv.org/abs/cond-mat/0307229) — The History of Correlation
- **作者**: Firdous Ahmad Mala
- **期刊/来源**: Technometrics
- **分类**: vol 68 · issue 1 · pp 223-224
- 相关性 3/10 · novelty: `survey`
- **摘要**: 本文是一篇书评，评述了《The History of Correlation》一书。该书系统梳理了相关系数从提出到现代应用的历史脉络，涵盖了Pearson、Spearman等关键人物的工作。书评指出该书对统计思想史有详实的文献考据，但未涉及任何新的方法论或理论结果。对于统计研究者而言，这是一本了解学科发展背景的读物，但无直接的技术或方法学贡献。
- **为什么对您有用**: 本文属于统计史书评，不涉及任何方法学进展或数据分析。与您的主要研究方向（因果推断、高维统计、U-统计量等）无直接关联，也不属于任何次级兴趣领域的入门读物。无需阅读全文。

### 5. [10.1080/00401706.2025.2560340](https://doi.org/10.1080/00401706.2025.2560340) — A Dynamic Screening System for Early Detection of Multiple Interconnected Events
- **作者**: Zibo Tian, Peihua Qiu
- **期刊/来源**: Technometrics
- **机构**: University of Florida Health · University of Florida
- **分类**: vol 68 · issue 1 · pp 122-136
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对多个相互关联事件的早期检测问题，提出了一种动态筛选系统（DySS）的扩展方法。传统统计过程控制图仅适用于单过程单事件的监测，而现有DySS方法也仅能处理单一事件。作者引入条件风险概念，利用单指标多项逻辑回归模型刻画多个事件之间的关联性，并基于此构建序贯监测框架。该方法通过实时追踪条件风险的变化，实现对多事件早期信号的同步检测。数值模拟表明，该方法在检测多个相互关联事件方面具有有效性。该方法属于统计过程控制与序贯决策领域，与您的主要研究兴趣（因果推断、高维统计、半参数理论等）无直接交集，但序贯监测框架中的风险建模思路可能对纵向因果推断中的时变处理效应评估有间接启发。
- **关键技术**: `dynamic screening system`, `single-index multinomial logistic regression`, `conditional risk`, `sequential monitoring`, `statistical process control`
- **为什么对您有用**: 本文属于统计过程控制的应用方向，与您的主要研究兴趣（因果推断、高维统计、半参数理论）无直接交集。但序贯监测框架中的条件风险建模思路，可能对纵向因果推断中时变处理效应的识别与估计有间接启发。武器库中'非参数统计'和'因果推断中的估计理论'可部分理解其方法，但核心问题（多事件早期检测）与您的兴趣方向差异较大，属于暂不可做的领域。

### 6. [10.1080/00401706.2025.2551351](https://doi.org/10.1080/00401706.2025.2551351) — Degradation Data Analysis based on Wiener Process with a Nonlinear Drift and a Stochastic Volatility
- **作者**: Linjie Qin, Yan Shen
- **期刊/来源**: Technometrics
- **机构**: Xiamen University · Xiamen University of Technology
- **分类**: vol 68 · issue 1 · pp 79-95
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对退化过程建模，提出一种集成非线性漂移和随机波动的Wiener过程模型。核心创新在于使用函数主成分分析（FPCA）方法估计双幂次变差（bipower variance），从而非参数地估计随机波动率，避免模型误设。该方法能有效捕捉扩散过程中的跨单元变异和时变特征，并减少由跳跃点引起的估计偏差。剩余寿命分布和平均失效时间均以显式形式给出。通过两个模拟实验和两个实际案例验证了模型和方法的有效性。该文属于工程可靠性领域的应用统计方法，与您的主要研究方向（因果推断、高维统计、U-统计量等）无直接交集。
- **关键技术**: `Functional Principal Component Analysis (FPCA)`, `Bipower variance`, `Wiener process with stochastic volatility`, `Nonparametric estimation of drift and volatility`
- **为什么对您有用**: 本文属于工程可靠性领域的应用统计方法，与您的主要研究方向（因果推断、高维统计、U-统计量等）无直接交集。FPCA方法虽在非参数统计中常见，但本文的应用场景（退化过程建模）与您的兴趣方向距离较远。暂不可做：核心机器不在武器库里（缺退化过程建模和可靠性工程背景）。

### 7. [10.1080/00401706.2025.2520860](https://doi.org/10.1080/00401706.2025.2520860) · [arXiv](https://arxiv.org/abs/2505.03990) — Batch Sequential Experimental Design for Calibration of Stochastic Simulation Models
- **作者**: Özge Sürer
- **期刊/来源**: Technometrics
- **分类**: vol 68 · issue 1 · pp 1-13
- 相关性 3/10 · novelty: `minor`
- **摘要**: 本文研究随机仿真模型校准中的批序贯实验设计问题。目标是在并行计算环境下，通过智能选择下一批仿真参数点（是重复已有参数还是探索新参数），最小化后验预测不确定性。方法基于高斯过程代理模型，提出新的批设计准则，在每次迭代中决定批内各点应分配给已有位置还是新位置。通过模拟实验和流行病学真实数据实验，验证了该方法相比传统序贯设计能显著改善后验预测精度。对您而言，本文属于统计计算与实验设计交叉方向，与您的统计计算（数值方法、算法）兴趣有弱关联，但核心方法（高斯过程、序贯设计）不在您的主要技术武器库中，且缺乏与因果推断、高维统计等主方向的直接连接。
- **关键技术**: `Gaussian process emulator`, `batch sequential design`, `posterior uncertainty minimization`, `stochastic simulation calibration`
- **为什么对您有用**: 本文属于统计计算与实验设计方向，与您的统计计算（数值方法、算法）兴趣有弱关联，但核心方法（高斯过程、序贯设计）不在您的主要技术武器库中（very_familiar 和 moderately_familiar 均未覆盖）。作为 gateway reading 价值有限：问题设定（仿真模型校准）与您的因果推断、高维统计等主方向无直接连接，且方法学 novelty 程度较低（主要是现有序贯设计的批扩展）。暂不可做——缺乏高斯过程序贯设计的核心工具。

### 8. [10.1080/00401706.2025.2565971](https://doi.org/10.1080/00401706.2025.2565971) — Non-Equilibrium Statistical Mechanics, 1st ed.
- **作者**: Oktaviyani Daswati, Yunia Hasnataeni
- **期刊/来源**: Technometrics
- **机构**: Advanced Pharma
- **分类**: vol 68 · issue 1 · pp 221-223
- 相关性 2/10 · novelty: `survey`
- **摘要**: 这是一本关于非平衡统计力学的教材，主要介绍远离热平衡系统的统计力学理论。书中融合了经典方法和现代技术，涵盖非平衡过程的数学框架。该书由Technometrics期刊书评栏目介绍，属于物理学教材而非统计学研究论文。对于统计学家而言，本书可能提供一些随机过程或动力系统的背景知识，但缺乏直接的统计方法学贡献。
- **关键技术**: `non-equilibrium statistical mechanics`, `stochastic processes`
- **为什么对您有用**: 该论文属于书评，内容为物理学教材，与您的主要研究方向（因果推断、高维统计、半参数理论等）无直接关联。作为gateway-reading，它既不是astrostats入门读物，也未提供可迁移的统计方法。暂不可做。

### 9. [10.1080/00401706.2025.2561744](https://doi.org/10.1080/00401706.2025.2561744) · [arXiv](https://arxiv.org/abs/2411.12563) — Stream-Based Active Learning for Process Monitoring
- **作者**: Christian Capezza, Antonio Lepore, Kamran Paynabar
- **期刊/来源**: Technometrics
- **分类**: vol 68 · issue 1 · pp 159-171
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文提出一种基于流的主动学习策略用于统计过程监控（SPM），目标是在标注预算有限的情况下动态分类过程状态（受控/失控）。传统SPM多为无监督方法，而监督方法依赖昂贵的人工标注；作者将主动学习扩展到实时数据流场景，利用部分隐马尔可夫模型（partial hidden Markov model）显式建模时间依赖性，整合已标注和未标注观测。方法在探索（检测新过程状态）与利用（提升已知状态分类精度）之间平衡，为每个新到达数据点实时决定是否请求标注。通过模拟实验和汽车工业电阻点焊过程案例研究评估性能。对您而言，本文属于应用导向的统计方法，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接技术重叠，但主动学习与标注预算约束的思想在流行病学或经济学的数据收集场景中可能有间接启发。
- **关键技术**: `stream-based active learning`, `partially hidden Markov model`, `statistical process monitoring`, `exploration-exploitation trade-off`
- **为什么对您有用**: 本文属于工业统计应用，与您的主要兴趣方向（因果推断、高维统计、U-统计量等）无直接技术连接。武器库中无对应工具可攻本文核心方法（主动学习+隐马尔可夫模型）。暂不可做——核心机器（序列决策、部分可观测模型）不在武器库中。

### 10. [10.1080/00401706.2025.2539785](https://doi.org/10.1080/00401706.2025.2539785) — A Periodic Fractional Wiener Process for Remaining Useful Life Prediction of Photovoltaic Systems with Long-Range Dependence
- **作者**: Ruixian Li, Yongxiang Li, Yao Cheng
- **期刊/来源**: Technometrics
- **机构**: Chinese University of Hong Kong · University of Hong Kong · Shanghai Jiao Tong University
- **分类**: vol 68 · issue 1 · pp 37-53
- 相关性 2/10 · novelty: `application`
- **摘要**: 该文针对光伏系统退化数据中同时存在的长程依赖性和准周期性，提出周期分数维维纳过程（PFWP）模型。传统退化模型（如Wiener过程、Gamma过程）无法同时刻画这两种特征，导致剩余寿命（RUL）预测精度不足。PFWP通过引入分数布朗运动（fBm）的Hurst参数捕捉长程依赖，并叠加周期核函数描述准周期波动，将退化过程建模为时变漂移+分数维扩散项。参数估计采用两阶段极大似然法：先通过周期图法估计周期成分，再基于残差估计Hurst参数和扩散参数。在五种不同技术类型的光伏系统公开数据集上，PFWP在数据拟合（AIC/BIC）和RUL预测（RMSE/MAE）上均优于ARIMA、标准Wiener过程及分数Wiener过程等基准模型，且能在失效前一年给出稳定的失效时间估计。该文方法学贡献在于将分数维随机过程与周期结构结合，但核心工具（fBm、MLE）属于经典时间序列范畴，未涉及因果推断、高维统计或效率理论等您的主要兴趣方向。
- **关键技术**: `fractional Brownian motion`, `periodic kernel`, `two-stage maximum likelihood estimation`, `remaining useful life prediction`, `long-range dependence`
- **为什么对您有用**: 该文属于工程可靠性建模，与您的主要兴趣（因果推断、高维统计、U-统计量）无直接交集。您的武器库中非参数统计和逆问题工具可处理退化过程的非参数估计，但本文的分数维过程设定与您的核心方向距离较远。作为gateway-reading，本文对统计学家入门光伏退化建模有一定参考价值，但方法学新颖性有限（主要是fBm的工程应用），暂不值得投入全文阅读。

### 11. [10.1080/00401706.2025.2552296](https://doi.org/10.1080/00401706.2025.2552296) · [arXiv](https://arxiv.org/abs/2208.08150) — Capturing Usage Patterns in Bike Sharing System via Multilayer Network Fused Lasso
- **作者**: Yunjin Choi, Haeran Cho, Hyelim Son
- **期刊/来源**: Technometrics
- **分类**: vol 68 · issue 1 · pp 96-105
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文研究共享单车系统中站点级使用模式的建模问题，目标是在考虑时空依赖性和协变量效应的同时，捕捉不同站点间的同质性。作者采用多层网络融合Lasso（multilayer network fused Lasso）惩罚的回归方法，将时空连接嵌入网络结构中，从而在不人为划分数据的前提下，自动识别具有相似使用模式的站点群。该方法的核心机制是通过融合惩罚（fusion penalty）鼓励相邻节点（在时空网络上相连的站点）的系数趋于一致，实现结构化的稀疏估计。在三个城市真实数据集上的实验表明，该方法在预测性能上具有竞争力，并能提供对数据的新解释。本文属于应用导向的方法学工作，方法本身（网络融合Lasso）并非全新，但将多层网络框架引入共享单车数据分析是一个合理的应用创新。
- **关键技术**: `multilayer network fused Lasso`, `fusion penalty`, `spatio-temporal network`, `penalized regression`
- **为什么对您有用**: 本文属于应用统计方法学，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接交集。方法上使用的网络融合Lasso是广义线性模型中的正则化技术，不涉及您武器库中的核心工具（如非参极小极大界、高阶U-统计量、半参效率理论）。作为流行病学或经济学应用方向的入门阅读，其数据分析流程（时空网络建模、融合惩罚）有一定参考价值，但整体方法学新颖性有限。暂不可做——核心机器（网络融合Lasso的优化与理论分析）不在您的武器库中，且与您的主要研究方向距离较远。

### 12. [10.1080/00401706.2025.2552297](https://doi.org/10.1080/00401706.2025.2552297) — Remaining Useful Life Prediction of Lithium-Ion Batteries Using Monotone Decomposition
- **作者**: Xinyan Li, Dianpeng Wang, Piao Chen
- **期刊/来源**: Technometrics
- **机构**: Beijing Institute of Technology · Zhejiang University-University of Edinburgh Institute
- **分类**: vol 68 · issue 1 · pp 106-121
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文针对锂离子电池剩余使用寿命（RUL）预测问题，提出了一种新的数据分解框架MonoD-GPR-DeepAR。核心挑战在于电池容量退化过程中存在非线性行为与间歇性容量再生现象（相邻循环间容量突然增加），导致传统经验模态分解（EMD）方法出现端点效应、信息泄漏且缺乏不确定性量化。MonoD算法将原始容量信号解耦为平滑递减趋势项和波动容量再生项，从而缓解端点效应。随后对子序列分别应用高斯过程回归（GPR）和深度自回归（DeepAR）模型进行预测并给出不确定性区间。通过仿真和三个真实锂离子电池数据集验证，MonoD-GPR-DeepAR在捕捉真实老化轨迹特征方面优于对比方法。本文属于工程应用领域的方法论文，方法学新颖性有限（novelty_flag: application），但对统计计算中的信号分解与不确定性量化有一定参考价值。
- **关键技术**: `Monotone Decomposition (MonoD)`, `Gaussian Process Regression (GPR)`, `Deep Autoregressive (DeepAR)`, `Empirical Mode Decomposition (EMD)`, `uncertainty quantification`
- **为什么对您有用**: 本文属于工程应用，与您的primary interests（因果推断、高维统计等）无直接关联。但MonoD作为一种信号分解方法，其处理非平稳时间序列的思路（趋势-波动解耦）对统计计算中的算法设计有一定启发。作为gateway reading，本文对统计学家友好，清晰描述了数据结构和模型假设，但核心方法（GPR+DeepAR）并非您武器库中的强项。暂不可做：缺乏与您核心工具（U-statistics、minimax bound等）的直接连接，不值得花时间精读全文。

### 13. [10.1080/00401706.2025.2537033](https://doi.org/10.1080/00401706.2025.2537033) — Multi-Layer Sliced Design and Analysis with Application to AI Assurance
- **作者**: Qing Guo, Xinwei Deng, Peter Chien
- **期刊/来源**: Technometrics
- **机构**: Virginia Tech · University of Wisconsin–Madison
- **分类**: vol 68 · issue 1 · pp 24-36
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文针对AI算法调参中的超参数效应检测与量化问题，提出了一种多层切片实验设计方法。核心思想是将超参数分为切片因子和设计因子，通过多层切片设计来捕捉不同AI配置下超参数效应的异质性。分析方法上，开发了相应的效应估计与显著性检验流程。模拟研究和实际AI应用案例验证了方法的有效性。该工作属于实验设计在AI调参中的应用，方法学上以分层设计为主，未涉及因果推断、高维统计或半参效率理论等核心兴趣方向。
- **关键技术**: `multi-layer sliced design`, `slice factor`, `design factor`, `effect estimation`, `significance testing`
- **为什么对您有用**: 本文属于实验设计在AI调参中的应用，与您的主要兴趣（因果推断、高维统计、半参理论）和方法库（非参统计、U统计量）均无直接交集。作为gateway-reading，本文面向工程应用而非统计理论，不涉及您武器库中的具体工具。暂不可做——核心机器（实验设计中的切片策略）不在您的武器库中，且与您的统计计算兴趣（信息-计算权衡）无关联。

### 14. [10.1080/00401706.2026.2615590](https://doi.org/10.1080/00401706.2026.2615590) — Special Integrals
- **作者**: Stan Lipovetsky
- **期刊/来源**: Technometrics
- **分类**: vol 68 · issue 1 · pp 215-216
- 相关性 1/10 · novelty: `survey`
- **摘要**: 本文是Technometrics期刊上的一篇书评，介绍了一本名为《Special Integrals》的教科书。该书属于大学数学科学教材系列，主要面向本科生和研究生，作为微积分及相关课程的补充资源。书评简要概述了该书的内容和定位，但未涉及任何统计方法或数据分析。本文不包含任何统计推断、因果分析或计算方法的实质性内容。对于统计研究者而言，这是一篇纯粹的数学教材介绍，与您的研究兴趣无直接关联。
- **为什么对您有用**: 本文是一篇书评，内容为微积分教材介绍，与您的主要研究兴趣（因果推断、高维统计、半参数理论等）和次要兴趣（天体统计、经济理论、流行病学）均无关联。武器库中的任何工具都无法应用于本文。不值得花时间阅读全文。

### 15. [10.1080/00401706.2026.2615596](https://doi.org/10.1080/00401706.2026.2615596) — Sex Robots: Social Impact and the Future of Human Relations
- **作者**: Stan Lipovetsky
- **期刊/来源**: Technometrics
- **分类**: vol 68 · issue 1 · pp 219-221
- 相关性 0/10 · novelty: `survey`
- **摘要**: 本文是一篇书评，评论了《Sex Robots: Social Impact and the Future of Human Relations》一书。该书探讨了性机器人技术的社会影响，包括机械工程、人工智能和材料科学等领域的进步如何推动性机器人的发展。文章讨论了性机器人可能对人际关系、伦理和社会规范产生的影响。作为一篇书评，本文没有提出新的统计方法或理论。本文与您的研究兴趣（因果推断、高维统计、半参数理论等）没有直接关联。
- **为什么对您有用**: 本文与您的主要研究兴趣（因果推断、高维统计、半参数理论等）无关，属于书评性质，不涉及统计方法或数据应用。不建议投入时间阅读。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

