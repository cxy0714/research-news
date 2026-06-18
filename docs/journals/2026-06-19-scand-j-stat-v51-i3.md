# Scand. J. Stat. — Vol 51  Issue 3  ·  2026-06-19

- 共 17 篇 · Scandinavian Journal of Statistics
- 目录核对 ⚠️ 疑似漏 1 篇（对照 OpenAlex 18 篇）：10.1111/sjos.12745

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期 Scand. J. Stat. Vol 51 Issue 3 的 17 篇论文可归纳为三条主线：**非参数与半参数方法的多样化扩展**（约 7 篇，涉及密度估计、变系数模型、生存分析、分类、生成对抗网络等）、**效率理论与半参数推断**（3 篇，包括高维部分线性回归、后向 SDE 参数估计、因果效应 doubly robust 估计）、**假设检验**（2 篇，分别检验时变非线性依赖和 ARMA 模型方差结构）。此外，因果推断方向另有 1 篇关于 principal stratification 的评论，流行病学方向有 1 篇关于复杂抽样下生存曲线置信带，统计计算方向 1 篇关于 Riemann manifold MCMC 的自动度量张量，以及空间点过程、kriging 最优设计和访谈各 1 篇。

最突出的是非参数/半参数主线。其中，**Nonparametric estimation of densities on the hypersphere using a parametric guide** 利用 von Mises-Fisher 引导分布修正核密度估计，在紧支撑下偏误降低而不牺牲方差，并与经典 KDE 对比。**Empirical likelihood M‐estimation for the varying‐coefficient model with functional response** 将经验似然与 M 估计结合，处理函数型响应变系数模型的内相关性，并证明非参数 Wilks 定理。**Martingale posterior distributions for cumulative hazard functions** 从 Nelson–Aalen 估计量构造鞅后验，无需先验指定。**A two‐step estimation procedure for semiparametric mixture cure models** 通过先非参数平滑后投影到参数类，避免了 EM 的初始值敏感。**Nonparametric plug‐in classifier for multiclass classification of S.D.E. paths** 基于核估计漂移与扩散函数，导出分类收敛速率。**Statistical inference for generative adversarial networks and other minimax problems** 将解集视为随机集，用 Hausdorff 距离和子采样构造置信集。**Efficient drift parameter estimation for ergodic solutions of backward SDEs** 对含有隐藏非参数成分的随机过程提出拟 MLE，建立半参数渐近正态性。这些工作覆盖了从紧支集密度、函数型数据、生存分析到随机微分方程和深度学习的广泛场景，共享非参数/半参数框架下的效率或推断目标。

另一条效率主线聚焦于半参数效率界。**Semiparametric efficient estimation in high‐dimensional partial linear regression models** 在高维线性部分引入惩罚，使估计量在非高斯误差下达到 oracle MLE 的半参数效率界，并具备变量选择性质。**Efficient drift parameter estimation for ergodic solutions of backward SDEs** 虽属于非参数/半参数主线，但其拟 MLE 的理论也属于半参数效率范畴。**Estimation of treatment effect among treatment responders with a time‐to‐event endpoint** 基于 principal stratification，构造 efficient influence function 的 doubly robust 估计量并证明半参数效率，是因果推断与效率理论的直接结合。假设检验主线中，**Testing for time‐varying nonlinear dependence structures** 利用局部高斯相关与 bootstrap 检验 regime 间依赖结构是否相等；**Asymptotic inference of the ARMA model with time‐functional variance noises** 推导 LSE 渐近性并构造 Wald 检验与 portmanteau 检验。

对因果推断、半参数效率、高维方向最贴近的优先阅读：**Semiparametric efficient estimation in high‐dimensional partial linear regression models**（高维半参数效率）、**Estimation of treatment effect among treatment responders with a time‐to‐event endpoint**（因果推断与 doubly robust 效率）、**Efficient drift parameter estimation for ergodic solutions of backward SDEs**（半参数似然推断）、以及 **Statistical inference for generative adversarial networks and other minimax problems**（非凸极小元推断，与高维/神经网络统计推断相关）。

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.1111/sjos.12706](https://doi.org/10.1111/sjos.12706) — Estimation of treatment effect among treatment responders with a time‐to‐event endpoint
- **作者**: Andreas Nordland, Torben Martinussen
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Copenhagen
- **分类**: vol 51 · issue 3 · pp 1161-1180
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在安慰剂对照临床试验中，当治疗效应可能仅存在于对特定生物标志物有响应的亚组时，目标是估计 treatment responders 上的因果效应。该 estimand 基于 principal stratification 定义，在排除 nonresponders 治疗效应的排除约束下实现 identification。针对右删失 time-to-event 结局，作者构造了基于 efficient influence function 的 doubly robust 估计量，并证明了其 semiparametric efficiency。模拟研究验证了估计量的有限样本性质，并在 LEADER 试验（liraglutide 对心血管事件的影响）数据上进行了实证分析。对您可能有用：本文将 principal stratification 与 survival outcome 的 semiparametric efficiency theory 结合，为 longitudinal/mediation 场景下处理中间响应变量的因果推断提供了直接参考。
- **关键技术**: `principal stratification`, `doubly robust estimation`, `efficient influence function`, `time-to-event outcome`, `right censoring`, `exclusion restriction`
- **为什么对您有用**: 直接连接 causal inference 的 principal stratification 与 semiparametric efficiency theory 子方向；您 very_familiar 的 estimation theory in causal inference 与 moderately_familiar 的 semiparametric theory 完全足以攻破本文 efficient influence function 的推导与 DR estimator 的收敛性质分析。属于立即可做：可用现有武器库直接复现推导并拓展至更复杂的 longitudinal setting。

### 2. [10.1111/sjos.12741](https://doi.org/10.1111/sjos.12741) — Commentary on “Pitfalls of amateur regression: The Dutch New Herring controversies”
- **作者**: Jan C. Van Ours, Ben Vollaard
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Erasmus University Rotterdam · Tilburg University
- **分类**: vol 51 · issue 3 · pp 1388-1389
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文是对Gao & Gill (2023)批评的回应，围绕“Dutch New Herring”争议讨论非盲专家评审中存在的系统性偏见。作者重申其2022年论文中基于明确识别假设的因果主张：通过构造同质样本（控制熟度、清洁质量、感官评分等）来隔离供应商冲突利益对评分的影响。在同质样本内，冲突利益方供应商的平均评分高出0.5分（满分10分），且其鱼贩均位列前十名——这在统计上难以用偶然解释。作者指出批评者忽视了独立学术机构LOWI（2019）对同一工作的审查结论，即未违反任何良好科研原则。全文旨在捍卫研究设计的严谨性，并邀请读者通过公开数据和代码自行验证。对您而言，这是一个因果推断在真实政策争议中的应用案例，展示了如何利用同质化设计识别利益冲突导致的偏差，可作为经济或流行病学领域因果应用研究的参考。
- **关键技术**: `causal identification via homogeneous sample`, `identifying assumption`, `sensitivity of rankings to outliers`
- **为什么对您有用**: 本文直接关联您对应用因果推断（尤其是经济领域利益冲突问题）的兴趣。您熟悉的非参统计与因果识别基础足以理解其设计逻辑；若需深入评估其识别假设的敏感性，可借助 moderately_familiar 的识别理论进行形式化检验。本文属于“可立即阅读”的入口级应用案例，虽无新方法，但数据集和分析模式值得借鉴。

## 非参数 / 半参数  *(nonparam_semipara, 7 篇)*

### 1. [10.1111/sjos.12737](https://doi.org/10.1111/sjos.12737) — Nonparametric estimation of densities on the hypersphere using a parametric guide
- **作者**: María Alonso‐Pena, Gerda Claeskens, Irène Gijbels
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Universidad de Granada · Universidade de Santiago de Compostela · KU Leuven · Statistics Belgium · VIB-KU Leuven Center for Microbiology
- **分类**: vol 51 · issue 3 · pp 956-986
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在超球面（hyperspherical）非参数密度估计设定下，目标密度定义在紧支撑上，研究引入参数引导分布（parametric guide）的核密度估计器（KDE）的统计性质。核心机制是利用 von Mises-Fisher 密度作为引导分布，通过修正核函数构造新估计器；当引导分布接近真实密度时，偏误显著降低而方差保持不变，且当引导模型错误甚至偏离真实分布时，该估计器的表现仍与经典 KDE 相当，这得益于超球面紧支撑的特殊性（与实值数据下的类似方法形成对比）。文章还提供了平滑参数的数据驱动选择方法。主要理论结果给出了偏误-方差权衡的精确刻画及渐近性质；对您可能有用：该工作展示了紧支撑下非参数-半参数混合估计的鲁棒性，其偏误缩减机制与您熟悉的非参数统计及 minimax bound 分析直接相关。
- **关键技术**: `hyperspherical kernel density estimation`, `von Mises-Fisher distribution`, `parametric guide bias reduction`, `smoothing parameter selection`, `bias-variance tradeoff on compact support`
- **为什么对您有用**: 本文直接连接到非参数统计与半参数理论子方向：在紧支撑（超球面）上利用参数引导实现偏误缩减，属于非参数估计的 sharper rate 改进。您可以用 minimax bounds for estimation problems 的武器库直接检验其声称的偏误缩减率是否紧，或探究该引导机制在一般紧支撑流形上的 minimax 性质。立即可做：用 very_familiar 的非参数 minimax 工具分析其收敛率边界。

### 2. [10.1111/sjos.12717](https://doi.org/10.1111/sjos.12717) — Empirical likelihood M‐estimation for the varying‐coefficient model with functional response
- **作者**: Xingcai Zhou, Dehan Kong, Matthew Stephen Pietrosanu, Linglong Kong, Rohana J. Karunamuni
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Nanjing Audit University · University of Toronto · University of Alberta
- **分类**: vol 51 · issue 3 · pp 1357-1387
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对带函数型响应的变系数模型，提出了一种基于广义经验似然的M估计方法，旨在稳健地处理观测内相关性，填补了函数型数据分析中的空白。方法核心是将经验似然与M估计结合，构建同时置信区域和全局一般线性假设检验。理论部分建立了对数似然比过程的弱收敛性，并证明了非参数版Wilks定理，给出了估计量的渐近性质。模拟显示置信集具有接近名义水平的覆盖概率。在神经影像数据集的应用中，揭示了MMSE评分和APOE基因型与分数各向异性的显著关联。该工作为函数型回归中的稳健推断提供了新工具，与您对非参数理论和假设检验的兴趣直接相连，尤其适用于生物医学纵向或图像数据。
- **关键技术**: `Empirical likelihood`, `M-estimation`, `Varying-coefficient model with functional response`, `Wilks' theorem for functional models`, `Global general linear hypothesis test`
- **为什么对您有用**: 本文属于非参数回归与推断方向，核心是经验似然M估计在函数型变系数模型中的应用。您武器库中的“非参数统计”可直接理解其渐近框架，而“M估计理论”（moderately_familiar）是理解其稳健推断机制的关键，需先深入该方向才能复现或扩展方法。属于中期可做：需在M-estimation理论上提升，并结合函数型数据分析。

### 3. [10.1111/sjos.12712](https://doi.org/10.1111/sjos.12712) — Martingale posterior distributions for cumulative hazard functions
- **作者**: Stephen G. Walker
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: The University of Texas at Austin
- **分类**: vol 51 · issue 3 · pp 936-955
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在非参数生存分析设定下，本文研究累积风险函数的不确定性量化，目标 estimand 为累积风险 Λ(t)。经典贝叶斯非参数基础模型为 beta process，经典估计量为 Nelson–Aalen 估计量。作者构造了一列随样本量递增的估计量，证明其构成鞅序列，从而通过鞅后验分布获得随机累积风险函数的完整后验样本。文中建立了该鞅后验与 beta process 之间的理论联系，并通过模拟示例展示方法表现。对您可能有用：鞅后验为非参数模型提供了一种不依赖先验指定、直接从估计量序列构造后验的思路，与您熟悉的非参数统计及 M-estimation 理论有直接交集。
- **关键技术**: `martingale posterior distribution`, `beta process`, `Nelson-Aalen estimator`, `cumulative hazard function`, `nonparametric Bayesian survival analysis`
- **为什么对您有用**: 本文连接到非参数理论子方向，具体在生存分析累积风险的鞅后验构造上，提供了一种绕过传统先验指定的新路径。您武器库中 very_familiar 的非参数统计与 moderately_familiar 的 M-estimation 理论可以直接攻入该估计量序列的鞅性质验证与收敛率分析。follow-up 判断：立即可做——用 minimax bound 检验该鞅后验收敛率是否达到非参数最优，或用 M-estimation 理论刻画其影响函数。

### 4. [10.1111/sjos.12702](https://doi.org/10.1111/sjos.12702) · [arXiv](https://arxiv.org/abs/2212.10259) — Nonparametric plug‐in classifier for multiclass classification of S.D.E. paths
- **作者**: Christophe Denis, Charlotte Dion‐Blanc, Eddy Ella‐Mintsa, Viet Chi Tran
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 1103-1160
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 研究基于时间齐次扩散过程混合模型的多类分类问题，其中类别由漂移函数区分而扩散系数未知。构建非参数插件分类器：先通过核方法非参数估计漂移和扩散函数，再基于估计量对SDE路径进行分类。在温和假设下证明了分类器的一致性，并在不同正则性条件下给出了收敛速率（依赖漂移函数光滑度与时域长度）。数值实验验证了有限样本表现。该工作将非参数函数估计与分类决策融合，为具有复杂时间序列特征的高维分类问题提供了理论框架。对您可能有用：可作为非参数分类理论的一个标准案例，了解扩散设定下估计与分类误差传播的关系。
- **关键技术**: `plug-in classifier`, `nonparametric drift estimation`, `diffusion coefficient estimation`, `multiclass classification`, `convergence rates`
- **为什么对您有用**: 直接对应 primary_interests 中的非参数与半参数理论（非参数估计的收敛率与分类器泛化误差关联），可视为非参数函数估计在统计决策中的应用。武器库中 'nonparametric statistics' 和 'minimax bounds for estimation problems' 可直接用于分析类似的估计-决策复合体，属于‘立即可做’的延伸工作。

### 5. [10.1111/sjos.12713](https://doi.org/10.1111/sjos.12713) — A two‐step estimation procedure for semiparametric mixture cure models
- **作者**: Eni Musta, Valentin Patilea, Ingrid Van Keilegom
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Amsterdam · École Nationale de la Statistique et de l'Analyse de l'Information · Centre de Recherche en Économie et Statistique · KU Leuven
- **分类**: vol 51 · issue 3 · pp 987-1011
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对半参数混合治愈模型（mixture cure model）中的治愈概率估计问题。传统方法依赖EM算法进行最大似然估计，但小样本下表现不稳定。作者提出两步估计程序：第一步利用非参数方法（如核平滑）构造治愈概率的初始估计，第二步将该非参数估计投影到预先指定的参数模型类（如logistic）上。该方法不需要迭代算法，且避免了EM对初始值的敏感性。理论结果表明该两步估计量具有相合性和渐近正态性，且通过logistic-Cox模型的模拟研究验证了其在小样本下显著优于传统MLE。最后用两个黑色素瘤数据集展示了实际应用。本文与您的半参数理论兴趣（投影估计、presmoothing）直接相关，且属于流行病学应用，可能激发您对治愈模型与因果推断（如潜在治愈状态的处理效应）的交叉思考。
- **关键技术**: `presmoothing`, `two-step estimation`, `nonparametric projection`, `mixture cure model`, `semiparametric M-estimation`
- **为什么对您有用**: 本文连接您的半参数非参数理论方向，具体涉及投影估计和presmoothing技术。您的技术武器库中'nonparametric statistics'（非常熟悉）可直接用于分析该两步估计量的渐近性质，您也可考虑将投影方法推广至因果推断中的治疗效应异质性估计（如cure结构下的ATE）。follow-up粗判：中期可做——需先熟悉生存分析治愈模型文献（目前武器库未涵盖），但核心非参数工具已具备。

### 6. [10.1111/sjos.12710](https://doi.org/10.1111/sjos.12710) · [arXiv](https://arxiv.org/abs/2104.10601) — Statistical inference for generative adversarial networks and other minimax problems
- **作者**: Mika Meitz
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 1323-1356
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文从统计推断角度研究生成对抗网络（GAN）中极小极大问题的参数估计。在GAN框架下，总体解集由生成器和判别器网络的多个平衡点组成。作者首先证明样本解集是总体解集在Hausdorff度量下的一致估计，该结果不要求问题凸性。进一步，基于子采样（subsampling）构造样本解集周围的置信集，并证明其渐近覆盖概率达到名义水平。技术核心在于将解集视为随机集，利用Hausdorff距离和极值分布理论导出收敛率。数值实验和蒙特卡洛模拟验证了理论覆盖性质。该方法论可推广至更一般的非凸非凹极小极大推断问题。对您而言，本文连接了非参数统计推断与神经网络驱动的最优化问题，其置信集构造思路可能启发研究者将更高阶U统计量的推断框架迁移至复杂生成模型。
- **关键技术**: `Hausdorff consistency`, `confidence sets via subsampling`, `generative adversarial networks`, `minimax estimation`, `non-convex non-concave optimization`, `solution set estimation`
- **为什么对您有用**: (1) 本文直接对应非参数统计推断这一核心兴趣子方向——极小极大解集的Hausdorff一致性属于非参数估计的推广。 (2) 技术武器库中'nonparametric statistics'和'minimax bounds for estimation problems'两项very_familiar工具可直接用于分析该文的一致性条件与收敛速度是否最优。 (3) 中期可做：若想扩展该置信集方法至更复杂的依赖图结构（如时间序列GAN），需先在moderately_familiar的'semiparametric theory'上强化对神经网络函数类覆盖数的理解。

### 7. [10.1111/sjos.12709](https://doi.org/10.1111/sjos.12709) · [arXiv](https://arxiv.org/abs/2109.08415) — Efficient drift parameter estimation for ergodic solutions of backward SDEs
- **作者**: Teppei Ogihara, Mitja Stadje
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 1181-1205
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对离散时间观测的遍历随机过程，其漂移参数依赖于未观测且非参数的随机积分部分，提出了拟最大似然估计方法。在遍历半参数扩散和后向SDE的设定下，证明了估计量的相合性和渐近正态性。核心是构造基于离散观测的拟似然函数，并利用遍历性建立大样本性质。随机积分部分的非参数性使得该问题属于半参数框架，且漂移与隐积分非线性关联。模拟验证了方法有限样本下的收敛表现。该工作将经典拟MLE扩展到一类含有隐藏非参数成分的随机过程模型，对处理复杂遍历过程的参数推断提供了理论保证。
- **关键技术**: `quasi-maximum likelihood`, `ergodic diffusion`, `backward SDE`, `semiparametric model`, `asymptotic normality`
- **为什么对您有用**: 直接关联您对半参数与非参数理论的兴趣——本文展示了在非参数随机积分干扰下识别有限维漂移参数的拟MLE方法，其分析框架（离散观测下的半参数推断）可迁移至因果推断中带有未测量混杂的动态模型。武器库中的非参数统计与M估计理论足以理解其核心论证，属于立即可做型。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1111/sjos.12716](https://doi.org/10.1111/sjos.12716) — Semiparametric efficient estimation in high‐dimensional partial linear regression models
- **作者**: Xinyu Fu, Mian Huang, Weixin Yao
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Shanghai University of Finance and Economics · University of California, Riverside
- **分类**: vol 51 · issue 3 · pp 1259-1287
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在高维部分线性回归模型（$Y=X^T\beta+g(Z)+\epsilon$）设定下，本文提出一种新的半参数有效估计方法，旨在克服传统最小二乘法在未知误差分布下的效率损失。核心估计量通过惩罚估计与半参数效率理论结合，对参数部分给出稀疏估计，并在非高斯误差下达到如同已知误差分布时的 oracle MLE 的半参数效率界；在高斯误差下则退化为与最小二乘估计相同的效率。理论证明该过程在超高维情形下具有 oracle 变量选择性质与 $n^{-1/2}$-CAN 收敛率，并通过模拟与实证数据验证了非高斯设定下的效率提升。对您有用：本文直接推进了高维半参数模型中的效率理论，其 oracle 效率界与惩罚稀疏估计的交互机制可为您研究 debiased ML / HOIF 在部分线性设定下的效率增益提供参照。
- **关键技术**: `semiparametric efficiency bound`, `oracle maximum likelihood estimator`, `penalized variable selection`, `partial linear regression`, `high-dimensional sparse estimation`, `adaptive efficiency under unknown error distribution`
- **为什么对您有用**: 本文直接连接到 primary interest 中的 efficiency theory（半参数效率界）与 semiparametric theory（部分线性模型）。您可用 very_familiar 的高维渐近理论验证其声称的 oracle 效率界是否紧，并用 moderately_familiar 的 HOIF 视角审视其非高斯效率增益是否可由更高阶 influence function 进一步刻画。follow-up 判断：**立即可做**——用您熟悉的 minimax bound 与 HOIF 工具即可动手分析该估计量的更高阶偏差修正与效率极限。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1111/sjos.12744](https://doi.org/10.1111/sjos.12744) — Testing for time‐varying nonlinear dependence structures: Regime‐switching and local Gaussian correlation
- **作者**: Kristian Gundersen, Timothée Bacri, Jan Bulla, Sondre Hølleland, Antonello Maruotti, Bård Støve
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Bergen · University of Regensburg · Norwegian School of Economics · Libera Università Maria SS. Assunta
- **分类**: vol 51 · issue 3 · pp 1012-1060
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究检验两个时间序列变量间非线性时变依赖结构是否在不同状态（regime）下相等的问题。作者将 regime-switching 模型与局部高斯相关（LGC）结合，提出了一种基于 LGC 的 bootstrap 检验方法。该方法通过 bootstrap 近似检验统计量的分布，避免了参数依赖结构的假设，是半参数方法。蒙特卡洛模拟显示该检验在水平和功效方面表现良好，且比基于 copula 的竞争方法更直观。文中以美国-英国股市收益率和美国股市与国债市场收益率数据为例，展示了依赖结构在状态间的变化。本研究连接了假设检验与非参数依赖度量，并可通过非参数 bootstrap 理论对其有限样本性质做进一步理论分析。
- **关键技术**: `Local Gaussian correlation (LGC)`, `regime-switching model`, `bootstrap test`, `semi-parametric dependence`, `Monte Carlo simulation`
- **为什么对您有用**: 本文直接关联 hypothesis testing 与非参数/半参数依赖程度的兴趣子方向。技术武器库中 'nonparametric statistics'（bootstrap 一致性、渐近有效性）可用于严格证明该检验的渐近性质。立即可做：可利用非常熟悉的非参数统计理论设计改进版本或进行更严格的 power 上界分析。

### 2. [10.1111/sjos.12708](https://doi.org/10.1111/sjos.12708) — Asymptotic inference of the ARMA model with time‐functional variance noises
- **作者**: Bibi Cai, Enwen Zhu, Shiqing Ling
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Hong Kong University of Science and Technology · Changsha University of Science and Technology
- **分类**: vol 51 · issue 3 · pp 1230-1258
- 相关性 2/10 · novelty: `weaker_assumption`
- **摘要**: 本文研究ARMA模型，其噪声方差随时间函数变化（time-functional variance, TFV），形成ARMA-TFV模型，该过程非平稳。首先证明最小二乘估计（LSE）的一致性和渐近正态性，推导出估计量的收敛速率。在此基础上，基于变量选择和模型检验理论构造Wald检验和portmanteau检验，用于模型阶数选择与残差诊断。通过模拟实验评估有限样本下检验的表现，并给出两个真实数据实例。该工作的技术处理因非平稳性而非常规，为时变方差时间序列的推断提供了新途径。对您而言，该文涉及的假设检验构造和LSE渐近分析可连接到您对 hypothesis testing 的兴趣，且LSE作为M-估计的特例，可用您 moderately_familiar 中的 M-estimation 理论审视其渐近论证。
- **关键技术**: `autoregressive moving average (ARMA)`, `time-functional variance`, `least squares estimator (LSE)`, `asymptotic normality`, `Wald test`, `portmanteau test`
- **为什么对您有用**: 本文直接涉及 hypothesis testing 子方向（Wald检验、portmanteau检验的构造与渐近性质），且LSE属于M-估计框架，您 moderately_familiar 中的 M-estimation theory 可用于检验其渐近论证的完备性。缺点在于：该文不涉及您最熟悉的高维/半参/因果工具，故 follow-up 暂不可做（缺乏鞅差时间序列的工具），但可作为时间序列推断的入门阅读，了解非平稳方差下的经典推断方法。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1111/sjos.12705](https://doi.org/10.1111/sjos.12705) · [arXiv](https://arxiv.org/abs/2211.01746) — Log‐density gradient covariance and automatic metric tensors for Riemann manifold Monte Carlo methods
- **作者**: Tore Selland Kleppe
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 1206-1229
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 论文提出一种基于对数密度梯度协方差（LGC）矩阵的自动度量张量构建方法，专门用于非线性贝叶斯层次模型的黎曼流形蒙特卡洛（RMMC）采样。LGC矩阵推广了Fisher信息矩阵，能够同时量化随机变量和参数的信息内容与依赖结构，从而从任意复杂的先验/潜变量条件分布中构造正定度量张量。该方法高度自动化，可自动利用模型中的稀疏性，并集成到数值广义随机哈密顿蒙特卡洛（NGRHMC）流程中。实验表明，对于挑战性的贝叶斯层次目标分布，该方法的采样效率显著优于现有方法。本文属于统计计算中MCMC方法的前沿进展，对处理高维复杂贝叶斯模型具有实用价值。
- **关键技术**: `Log-density gradient covariance (LGC)`, `Riemann manifold Monte Carlo`, `Fisher information generalization`, `automatic metric tensor construction`, `sparse Bayesian hierarchical models`, `generalized randomized Hamiltonian Monte Carlo`
- **为什么对您有用**: 直接对应您 primary interest 中的 statistical computing（数值算法方向），LGC 为高维贝叶斯模型的自动 MCMC 提供了新框架。您的 very_familiar 武器库中 'software development' 可立即用于实现该算法并测试其稀疏性利用效果；'high-dimensional asymptotics' 可用于分析 LGC 在高维参数空间中的渐近性质（如估计稳定性）。中期可做：需先夯实 'Riemann manifold HMC' 理论（不在当前武库中），但构建的 LGC 与 Fisher 信息的联系很容易用您的非参数/半参数基础补足。

## 流行病学  *(epidemiology, 1 篇)*

### 1. [10.1111/sjos.12700](https://doi.org/10.1111/sjos.12700) — Confidence bands for survival curves from outcome‐dependent stratified samples
- **作者**: Takumi Saegusa, Peter Nandori
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Maryland, College Park · Yeshiva University
- **分类**: vol 51 · issue 3 · pp 1086-1102
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 针对结果依赖的分层抽样（outcome-dependent stratified sampling）下的生存曲线，如何构造渐近正确的置信带。难点在于样本内依赖（无放回抽样）导致加权 Kaplan-Meier 估计量的极限过程为一般高斯过程，其上确界分位数无法解析计算。本文首先建立了考虑样本依赖的逆概率加权 Kaplan-Meier 估计量的严格渐近理论，随后提出一种混合方法：对极限过程的部分成分进行模拟、对剩余成分进行 Bootstrap，从而获得渐近覆盖概率正确的置信带。模拟实验显示有限样本表现良好，并给出了 Wilms 肿瘤实际数据分析。对您有用的点：该工作将复杂抽样设计下的非参数推断与 Bootstrap 理论结合，是流行病学中常见病例-对照或分层队列数据的一个实用工具。
- **关键技术**: `inverse probability weighting`, `Kaplan-Meier estimator`, `confidence bands`, `outcome-dependent stratified sampling`, `hybrid bootstrap`, `Gaussian process approximation`
- **为什么对您有用**: 连接流行病学的实际数据分析（Wilms tumor），属于 secondary interest 中的流行病学应用。论文的方法核心是加权非参估计 + Bootstrap 推断，研究者对 nonparametric statistics 和 high-dimensional asymptotics 非常熟悉，可立即可用此类思路处理流行病学中其他复杂抽样设计下的推断问题。

## 其他  *(other, 3 篇)*

### 1. [10.1111/sjos.12720](https://doi.org/10.1111/sjos.12720) · [arXiv](https://arxiv.org/abs/2212.08402) — Cox processes driven by transformed Gaussian processes on linear networks—A review and new contributions
- **作者**: Jesper Møller, Jakob G. Rasmussen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 1288-1322
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 该文针对线性网络上点过程模型匮乏的问题，提出了由变换高斯过程驱动的Cox过程模型，包括对数高斯、中断和永久Cox过程三类新模型。方法核心是通过各向同性高斯过程的变换获得各向同性对相关函数，并首次为这些参数族建立了统计推断程序。文中还构造了适用于线性网络的高斯过程模拟算法，并深入讨论测地度量与电阻度量在Cox过程建模中的选择依据。主要理论贡献在于将Cox过程框架扩展至任意线性网络拓扑，但模型假设和推断方法局限于各向同性设定。本文虽不涉及因果推断、高维统计等主题，但其模拟算法与统计计算兴趣相关，可作为空间点过程建模的入门阅读。
- **关键技术**: `Cox process`, `linear network`, `transformed Gaussian process`, `log Gaussian Cox process`, `geodesic metric`, `resistance metric`
- **为什么对您有用**: (1) 该论文涉及线性网络上高斯过程的模拟算法和点过程建模，与研究者的统计计算兴趣（算法实现）有微弱连接。(2) 武器库中very_familiar的软件开发经验可用于复现和优化模拟算法，但需先补充线性网络空间统计的知识。(3) 目前缺乏点过程理论及网络拓扑建模的相关工具，暂不可做深入跟进，仅适合作为方法学储备阅读。

### 2. [10.1111/sjos.12699](https://doi.org/10.1111/sjos.12699) · [arXiv](https://arxiv.org/abs/2111.06632) — G‐optimal grid designs for kriging models
- **作者**: Subhadra Dasgupta, Siuli Mukhopadhyay, Jonathan Keith
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 3 · pp 1061-1085
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究二维输入、可分离指数协方差结构的kriging模型下的G-最优网格设计问题。作者首先发展了网格设计均匀性的数学概念，并建立了设计点与最大均方预测误差（SMSPE）之间的解析关系。对于前瞻性设计（实验前确定设计），通过理论推导证明规则网格是G-最优设计，即最小化SMSPE。对于回顾性设计（从已有设计增删点），构造了确定性算法以迭代寻找近似最优配置，数值实验表明均匀性越高则性能越优。频率学派和贝叶斯框架下的结果均被讨论。最后，将提出方法应用于一个时空河流水质监测实验，展示了实际可行性。该论文涉及空间统计最优设计，与您的主要兴趣（因果推断、高维统计等）无直接重叠，但其确定性算法设计思路可作为统计计算中算法开发的一个参考案例。
- **关键技术**: `G-optimal design`, `kriging / Gaussian process`, `separable exponential covariance`, `SMSPE (supremum of mean squared prediction error)`, `deterministic optimization algorithm`, `prospective vs. retrospective designs`
- **为什么对您有用**: 该论文不属于您 primary interests 中的任何子方向（因果推断、高维统计、U-统计量、半参数效率等），因此作为一篇方法论文章，其连接性较弱。不过，文中开发确定性算法求解最优设计的思路可与您 arsenal 中的“软件开发”结合，作为设计效率比较的典型示例；技术层面，您可借用“非参数统计”中的均匀性概念来评估该类算法是否达到设计下界，但核心问题（kriging 设计）本身并非您的主要研究领域。**Follow-up 粗判**：暂不可做——缺少空间统计或实验设计领域的基本工具（如协方差结构建模、最优设计理论），需要先补充相关知识才能进行实质性改进。

### 3. [10.1111/sjos.12732](https://doi.org/10.1111/sjos.12732) — A conversation with Nils Lid Hjort
- **作者**: Ørnulf Borgan, Ingrid K. Glad
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Oslo
- **分类**: vol 51 · issue 3 · pp 914-935
- 相关性 1/10 · novelty: `survey`
- **摘要**: 本文是对挪威统计学家 Nils Lid Hjort 的访谈记录，回顾了他四十余年的学术生涯与跨领域贡献。访谈涵盖其在生存分析、Bayesian nonparametrics、经验似然、密度估计、focused inference、模型选择及置信分布等方向的开创性工作。核心线索是 Hjort 如何凭借好奇心与深刻理解，在不同统计子领域及其应用之间建立意想不到的连接，并强调聚焦推断（针对特定参数而非全局模型）的哲学。文章旨在鼓励统计学界主动寻找学科间的意外关联，拥抱跨领域的学术交流。对您而言，Hjort 在 focused inference 与 confidence distribution 上的工作与 semiparametric efficiency theory 有深层联系，可作为拓宽视角的轻松读物。
- **关键技术**: `focused inference`, `confidence distributions`, `Bayesian nonparametrics`, `empirical likelihood`, `survival analysis`
- **为什么对您有用**: 本文属于 gateway-reading 范畴：(1) 是了解 Hjort 学术脉络与统计哲学的好入门读物，尤其 focused inference 与 confidence distribution 的思想脉络讲得清晰；(2) 武器库中 semiparametric theory 与 minimax bounds 完全足够支撑研究者理解访谈中提及的理论视角；(3) 值得花半小时浏览访谈，但无需精读全文——方法论 novelty 程度低，主要是学术史与视角启发。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

