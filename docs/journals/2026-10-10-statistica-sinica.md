# Statistica Sinica  ·  2026-10-10

- 共 21 篇 · Statistica Sinica

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期 Statistica Sinica 的 21 篇论文大致可归为四条主线：**高维与分布式推断**（含隐私保护）、**因果识别与稳健估计**、**函数型与复杂数据建模**、以及**假设检验与重抽样方法**。高维主线覆盖了从分布式估计、污染稳健回归到矩阵时间序列与精度矩阵估计；因果主线聚焦隐藏混杂下的识别与双向效应；函数型主线则延伸至 Fréchet 回归与变系数模型；检验与重抽样主线则处理高维函数数据、空间数据及模型选择比较。

最突出的是**高维与分布式推断**这条线，多篇论文在隐私或污染约束下推进了估计与推断的效率边界。`Deconfounded-Debiased Distributed Estimation` 针对多中心数据中的异质隐藏混杂，结合多数投票变量选择与去偏聚合，同时处理隐私与高维偏差；`Adversarial Contamination Meets Hard Thresholding` 则通过交替阈值更新系数与污染向量，在非凸优化下达到 minimax 近最优，并具备信号自适应性。`Distributed Learning of Single Index Model` 将差分隐私引入半参数单指标模型，建立了非参数分量的收敛速率与指数参数的渐近正态性，是隐私约束下效率分析的典型代表。此外，`Precision Matrix Estimation for Multiple Compositional Vectors` 处理多个成分向量的联合精度矩阵，在跨域网络推断上提供了新的收敛保证。

另一条值得关注的主线是**因果推断与稳健识别**，集中在隐藏混杂与双向效应上。`Bidirectional Causal Inference for Binary Outcomes` 通过约束映射连接观测二元变量与潜在连续变量，利用双向工具变量识别因果效应，并附敏感性分析，是二元结局下少见的双向因果处理。`Deconfounded-Debiased Distributed Estimation` 虽属高维主线，但其去混杂思想与因果推断直接相关，适合关注隐藏混杂的读者。此外，`Spatial Subsample Bootstraps` 与 `Delaunay Weighted Two-sample Test` 分别从空间依赖与几何信息角度切入高维检验，前者避免了协方差矩阵估计，后者利用流形结构提升功效，对高维假设检验有兴趣者可一并参考。

若按主题优先阅读：因果推断方向可先看 `Bidirectional Causal Inference` 与 `Deconfounded-Debiased Distributed Estimation`；半参数效率与隐私权衡可关注 `Distributed Learning of Single Index Model`；高维稳健估计则看 `Adversarial Contamination Meets Hard Thresholding`；函数型数据推断可读 `Wild Bootstrap for Mean Response Inference` 与 `Varying-coefficient Fréchet Regression`。

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.5705/ss.202026.0052](https://doi.org/10.5705/ss.202026.0052) — Deconfounded-Debiased Distributed Estimation for High-Dimensional Multi-Site Data with Heterogeneous Pervasive Hidden Confounders
- **作者**: Zhaoyang Li, Chen Huang, Guoyou Qin, Zhongyi Zhu
- **期刊/来源**: Statistica Sinica
- **机构**: Fudan University
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对高维多中心观测数据中跨中心异质且普遍存在的隐藏混杂问题，提出了一种去混杂-去偏的分布式估计方法。该方法在中心站点整合多数投票进行变量选择，并聚合各局部去混杂-去偏估计量，以保护隐私。方法同时校正了异质隐藏混杂和高维估计带来的偏差，并允许各中心随机误差存在异方差。理论上证明了局部去混杂-去偏估计量的渐近正态性，以及局部个体假设检验的渐近有效性并给出功效下界。进一步建立了分布式估计的变量选择相合性和渐近正态性，并提供了变量选择的有限样本保证，包括期望假阳性率的上界和真阳性率的下界。模拟实验和UK Biobank蛋白质数据集的应用验证了方法的有限样本性能。
- **关键技术**: `deconfounded-debiased estimation`, `distributed estimation`, `majority voting`, `privacy-preserving aggregation`, `heterogeneous pervasive hidden confounders`, `high-dimensional inference`
- **为什么对您有用**: 本文直接关联因果推断中隐藏混杂的处理，特别是多中心异质场景，与您的proximal CI和敏感性分析兴趣点有交集。您非常熟悉的非参数统计和极小极大界工具可用于审视其有限样本保证的紧性，而您中等熟悉的高阶影响函数理论可能为改进其去偏步骤提供新视角。中期可做：需先在高阶影响函数上加强。

### 2. [10.5705/ss.202025.0374](https://doi.org/10.5705/ss.202025.0374) · [arXiv](https://arxiv.org/abs/2601.17695) — Bidirectional Causal Inference for Binary Outcomes in the Presence of Unmeasured Confounding
- **作者**: Yafang Deng, Kang Shuai, Shanshan Luo
- **期刊/来源**: Statistica Sinica
- **机构**: Beijing Technology and Business University · Dartmouth Institute for Health Policy and Clinical Practice
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究在存在未测量混杂时，二元结局变量之间双向因果效应的识别与估计问题。作者通过约束映射将观测的二元变量与潜在连续变量联系起来，构建结构方程模型，并利用两个方向的工具变量建立双向因果效应的识别条件。估计方法基于所提出的结构方程模型，并给出了相应的因果参数估计量。文章还针对识别条件违反的情形进行了敏感性分析。最后，将方法应用于心脏病与糖尿病之间双向因果关系的实证研究，展示了其在实际生物医学数据中的可用性。该方法为二元结局下的双向因果推断提供了新的工具变量识别策略，并考虑了实际应用中常见的假设违背问题。
- **关键技术**: `structural equation modeling`, `instrumental variables`, `binary outcomes`, `latent continuous variables`, `sensitivity analysis`
- **为什么对您有用**: 本文直接关联因果推断中工具变量与未测量混杂的核心兴趣，且针对二元结局这一常见但困难设定，扩展了双向因果推断的识别理论。可用您非常熟悉的估计理论（如M-estimation）来审视其估计量的有限样本性质，或考虑用您的中等熟悉度工具（如HOIF）推导其高阶影响函数以提升估计效率。中期可做：需先熟悉工具变量在非线性/二元模型中的识别技术。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 5 篇)*

### 1. [10.5705/ss.202025.0224](https://doi.org/10.5705/ss.202025.0224) · [arXiv](https://arxiv.org/abs/2606.27685) — Adversarial Contamination Meets Hard Thresholding: an Iterative Algorithm with Signal Adaptivity and Minimax Optimality
- **作者**: Shixiang Liu, Hanming Yang
- **期刊/来源**: Statistica Sinica
- **机构**: Renmin University of China
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究高维回归中数据被污染（测量误差、离群点或对抗性破坏）时的稳健估计问题，目标是在稀疏系数向量和稀疏污染向量同时存在时恢复真实信号。作者提出两阶段对抗污染稳健迭代硬阈值（AC-IHT）算法，通过以不同阈值尺度交替更新系数向量和污染向量，实现非凸优化下的估计。理论上证明该算法达到 minimax 近最优（至多对数因子）的估计误差，并具有信号自适应性：在适当信号条件下，可自适应获得更快的估计率和更准确的支持恢复。此外，估计量满足强 oracle 性质，为渐近推断奠定基础。数值实验显示有限样本性能优越，并讨论了向广义线性模型和重尾噪声情形的扩展。
- **关键技术**: `iterative hard thresholding`, `nonconvex optimization`, `minimax optimality`, `signal adaptivity`, `oracle property`, `sparse regression`
- **为什么对您有用**: 该论文直接关联您的高维统计与假设检验兴趣，特别是稀疏回归中的稳健估计与 minimax 理论。您可以用 very_familiar 的 minimax 界工具验证其声称的率是否紧，并利用您对非参数统计的熟悉度分析其信号自适应机制。中期可做：结合您 moderately_familiar 的 M-估计理论，将该算法推广到更一般的损失函数。

### 2. [10.5705/ss.202025.0419](https://doi.org/10.5705/ss.202025.0419) · [arXiv](https://arxiv.org/abs/2511.09542) — Local Interaction Autoregressive Model for High Dimension Time Series Data
- **作者**: Jingyang Li, Yang Chen
- **期刊/来源**: Statistica Sinica
- **机构**: Fudan University · University of Michigan
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对高维矩阵和张量时间序列中的局部依赖结构，提出局部交互自回归（LIAR）框架，假设每个条目主要与邻近小邻域交互，从而大幅降低参数维度。针对矩阵情形提出可分离LIAR模型，共享行和列分量，并设计基于并行最小二乘的估计算法及BIC型邻域选择准则。理论上证明了邻域选择的一致性，并给出核估计和自协方差估计的误差界。数值模拟显示BIC选择器能高概率恢复真实邻域，估计误差小，预测优于矩阵时间序列基线。在总电子含量（TEC）应用中，方法识别出局部的时空传播模式并提升预测精度。对您而言，该文将高维时间序列的稀疏结构与张量分解思想结合，与您的高维统计和统计计算兴趣相关。
- **关键技术**: `local interaction autoregressive model`, `separable matrix model`, `parallel least squares`, `BIC-type neighborhood selection`, `error bounds for kernel estimation`
- **为什么对您有用**: 该文属于高维时间序列建模，与您的高维统计和统计计算兴趣相关。其可分离结构可视为张量分解的特例，您可用非常熟悉的张量收缩/树宽工具分析其计算复杂度，或从 minimax 视角检验其误差界是否最优。属于中期可做：需先熟悉矩阵时间序列的谱范数集中不等式（moderately_familiar 中的高维渐近）。

### 3. [10.5705/ss.202025.0230](https://doi.org/10.5705/ss.202025.0230) — Two-way Subgroup Structure Learning for High Dimensional Clustered Survival Data
- **作者**: Ye He, Dongsheng Tu, Liu Liu, Ling Zhou
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对高维聚类生存数据，提出同时识别两类子群结构（亚组分析 SA 与同质性融合 HF）的新方法 DCAF。在固定效应模型中，通过引入可微的中心增广调和型惩罚替代传统成对惩罚，实现双向子群的同时识别，并兼顾聚类异质性与弱信号。理论上建立了估计相合性与选择相合性，数值模拟和两个真实数据案例验证了方法在识别双向子群和筛选重要生物标志物方面的有效性。该方法将高维惩罚回归与生存分析结合，对您在高维统计与统计计算方面的兴趣有直接参考价值。
- **关键技术**: `center-augmented harmonic-type penalty`, `fixed effect model`, `subgroup analysis`, `homogeneity fusion`, `high-dimensional survival data`
- **为什么对您有用**: 本文属于高维统计与统计计算交叉方向，与您的高维统计兴趣相关，但更偏向应用方法。您可用 very_familiar 的 minimax bounds 工具评估其选择相合性是否最优，或利用软件工程能力复现其算法。作为应用型论文，方法学 novelty 一般，但真实数据案例可能提供可迁移的分析流程。

### 4. [10.5705/ss.202025.0459](https://doi.org/10.5705/ss.202025.0459) · [arXiv](https://arxiv.org/abs/2503.05340) — A Hybrid Framework Combining Autoregression and Common Factors for Matrix Time Series
- **作者**: Zhiyun Fan, Xiaoyu Zhang, Di Wang
- **期刊/来源**: Statistica Sinica
- **机构**: Shanghai Jiao Tong University · Tongji University
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出矩阵时间序列的混合模型 MARCF，将降秩矩阵自回归（RRMAR）与动态矩阵因子模型（MFM）结合，通过将系数矩阵分解为公共、预测变量特异和响应特异三部分，显式刻画预测与响应子空间的交集，在灵活性与简约性间取得平衡。估计采用正则化梯度下降算法，可扩展至高维数据并处理非凸参数空间。理论上证明了算法的局部线性收敛性和估计量的统计相合性（在高维尺度下）。模拟和全球宏观经济数据集的应用展示了方法的效率与可解释性。对您而言，该工作涉及高维矩阵时间序列的结构化建模与计算，与您在高维统计和统计计算方面的兴趣相关。
- **关键技术**: `reduced-rank matrix autoregression`, `matrix factor model`, `regularized gradient descent`, `non-convex optimization`, `high-dimensional consistency`
- **为什么对您有用**: 该论文属于高维统计与统计计算的交叉，直接关联您的高维统计兴趣；其正则化梯度下降算法与您的软件开发和数值方法技能可对接，但核心理论（非凸优化的局部收敛性）需要您熟悉的非参数/半参数理论背景来理解；作为方法学论文，值得关注其在高维矩阵时间序列中的建模思路。

### 5. [10.5705/ss.202026.0002](https://doi.org/10.5705/ss.202026.0002) — Precision Matrix Estimation for Multiple Compositional Vectors
- **作者**: Shen Zhang, Huaying Fang, Tao Hu
- **期刊/来源**: Statistica Sinica
- **机构**: Qufu Normal University · Capital Normal University
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究多个成分数据向量的联合精度矩阵估计问题，目标是在成分约束、高维性和跨向量依赖下，恢复潜在绝对丰度的条件独立图。现有方法多针对单一成分向量，而微生物组研究中常同时观测细菌和真菌等多个成分谱，需要联合建模。作者提出自适应方法 Amcoda，通过处理成分数据的对数比变换和多个向量的联合结构来估计精度矩阵。理论部分建立了 Amcoda 估计量在多种矩阵范数下的收敛速率，并给出了支持恢复的保证。模拟实验表明 Amcoda 在估计精度和边检测上优于现有方法。最后应用于真实微生物组数据，推断细菌-真菌跨域网络并识别若干潜在生物学相关交互。
- **关键技术**: `precision matrix estimation`, `compositional data analysis`, `graphical models`, `log-ratio transformation`, `support recovery`
- **为什么对您有用**: 该论文属于高维统计中的图模型与精度矩阵估计，直接关联您的高维统计兴趣，且其多向量联合建模和自适应阈值思想可迁移到您熟悉的非参数与因果推断中的网络分析。技术上，您可运用 minimax 界和 U-统计量投影工具来审视其收敛速率的最优性，属于中期可做，需在 moderately_familiar 的 semiparametric theory 上稍加延伸。

## 非参数 / 半参数  *(nonparam_semipara, 3 篇)*

### 1. [10.5705/ss.202025.0406](https://doi.org/10.5705/ss.202025.0406) — Distributed Learning of Single Index Model with Differential Privacy and Massive Data
- **作者**: Fode Zhang, Lingrui Wang, Hua Liang
- **期刊/来源**: Statistica Sinica
- **机构**: Southwestern University of Finance and Economics · George Washington University
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究分布式分治框架下单指标模型（SIM）的估计与推断问题，目标是在大规模数据下估计非参数链接函数和低维指数参数，同时满足差分隐私（DP）约束。作者提出DC估计器，建立了非参数分量的收敛速率和误差界，并证明了指数参数估计量的渐近正态性；在温和条件下，聚合估计器达到最优非参数收敛速率。为提供严格隐私保护，进一步开发了满足(ε,δ)-DP的分布式算法，并给出平均平方梯度映射的高概率界，刻画隐私噪声与模型复杂度对优化精度的影响。模拟和真实数据应用验证了估计准确性和隐私保护有效性。对您而言，该文将分布式推断、半参数效率与隐私噪声的权衡结合，其非参数分量的收敛速率分析可联系您的semiparametric theory与minimax bounds工具。
- **关键技术**: `divide-and-conquer estimation`, `single-index model`, `differential privacy`, `nonparametric convergence rates`, `asymptotic normality`
- **为什么对您有用**: 该文直接关联您的semiparametric & nonparametric theory兴趣，特别是单指标模型的分布式估计与推断；其非参数分量的收敛速率分析可用您very_familiar的minimax bounds工具验证是否最优，而DP噪声对估计精度的影响分析可联系您对statistical-computational tradeoff的gateway阅读兴趣。中期可做：需在moderately_familiar的semiparametric theory上进一步熟悉，以深入推导影响函数；暂不可做：若涉及隐私-精度权衡的精细刻画，可能需要补充信息论或复杂度工具。

### 2. [10.5705/ss.202025.0349](https://doi.org/10.5705/ss.202025.0349) · [arXiv](https://arxiv.org/abs/2509.11061) — Varying-coefficient Fréchet Regression
- **作者**: Yanzhao Wang, Jianqiang Zhang, Wangli Xu
- **期刊/来源**: Statistica Sinica
- **机构**: Renmin University of China · Zhejiang Gongshang University
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文提出变系数 Fréchet 回归模型，将经典变系数框架推广到响应变量为随机对象（如度量空间中的分布、流形上的点）的情形，同时允许效应修饰变量 U 为欧氏或非欧氏，而预测变量 X 为欧氏。针对 U 的两种类型分别设计估计方法，核心思想是利用局部加权 Fréchet 均值，并通过核平滑处理非欧氏 U。作者引入模型的平滑版本，将估计误差分解为偏差项和随机项分别分析，建立了收敛速率。模拟和真实数据应用验证了方法的有效性。该工作属于非欧氏数据回归建模的前沿，对您而言，其局部加权估计与偏差-方差分解的分析框架可迁移到您熟悉的非参数统计和半参数理论中，尤其适合作为扩展 Fréchet 回归文献的入门读物。
- **关键技术**: `Fréchet regression`, `varying-coefficient model`, `local weighted Fréchet mean`, `kernel smoothing`, `bias-variance decomposition`
- **为什么对您有用**: 本文属于非参数/半参数回归在非欧氏响应上的扩展，直接关联您的非参数与半参数理论兴趣；其局部加权估计和偏差-随机项分解的分析技术，可用您非常熟悉的非参数统计工具（如核方法、U-统计量投影）来审视和推广，属于立即可做的方向。

### 3. [10.5705/ss.202025.0307](https://doi.org/10.5705/ss.202025.0307) · [arXiv](https://arxiv.org/abs/2606.16089) — Wild Bootstrap for Mean Response Inference in Functional Linear Regression Models
- **作者**: Hyemin Yeon, Xiongtao Dai, Daniel Nordman
- **期刊/来源**: Statistica Sinica
- **机构**: University of California, Berkeley · Iowa State University
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究函数型线性回归中均值响应推断的bootstrap方法。在函数型协变量设定下，目标是构造响应均值的置信区间，但误差异方差性使残差bootstrap失效，而配对bootstrap虽稳健但计算代价高。作者提出一种wild bootstrap方法，作为残差bootstrap的修正版，在保持计算效率的同时适用于异方差误差，并建立了理论一致性。数值实验表明该方法在覆盖率和计算速度上均表现良好。此外，针对均值响应推断问题，提出了一种实用的截断水平选择策略。方法通过天气数据示例展示，并提供了R包BTSinFLRM实现。对您而言，该方法与您在高维和半参数推断中的bootstrap理论兴趣相关，且其截断选择策略可能对函数型数据中的推断问题有参考价值。
- **关键技术**: `wild bootstrap`, `functional linear regression`, `heteroscedastic errors`, `truncation level selection`, `confidence interval calibration`
- **为什么对您有用**: 本文属于半参数/非参数推断方向，与您对bootstrap和假设检验的兴趣直接相关。您可以用very_familiar的非参数统计和minimax理论来评估其bootstrap一致性的证明条件，或考虑将wild bootstrap扩展到函数型数据中的其他推断问题（如部分线性模型）。中期可做：需先熟悉函数型数据分析的特定工具（如FPCA），但核心bootstrap机制在您的武器库内。

## 数理统计 / 假设检验  *(hypothesis_testing, 8 篇)*

### 1. [10.5705/ss.202025.0356](https://doi.org/10.5705/ss.202025.0356) · [arXiv](https://arxiv.org/abs/2505.19974) — Two Sample Testing for High-dimensional Functional Data: A Multi-Resolution Projection Method
- **作者**: Shouxia Wang, Jiguo Cao, Hua Liu, Jinhong You, Jicai Liu
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究高维函数型数据的两样本均值检验问题，目标是在函数维度 p 随样本量增大时检验两组均值函数是否相等。现有方法多针对低维函数数据，在高维情形下失效，作者提出一种多分辨率投影（MRP）方法，将函数投影到多尺度基函数上，构造检验统计量。作者建立了检验统计量的渐近正态性，并分析了高维情形下的功效性质。针对实际中函数观测离散且异步的特点，理论分析了函数重构对检验统计量的影响。通过大量模拟和两个真实数据应用验证了方法的有限样本性能，其中全球气候数据分析显示中等排放路径（RCP4.5）与高排放路径（RCP8.5）下气候变量的函数均值存在显著差异。该方法对您可能有用，因为它结合了高维统计与函数型数据分析，可联系您在高维假设检验和随机矩阵理论方面的兴趣。
- **关键技术**: `multi-resolution projection`, `high-dimensional functional data`, `asymptotic normality`, `power analysis`, `function reconstruction`
- **为什么对您有用**: 本文属于高维假设检验方向，直接关联您的主要兴趣之一。您可以用 very_familiar 的高维渐近理论来审视其检验统计量的构造与功效分析，特别是其投影方法是否可推广到更一般的基函数或与随机矩阵理论结合。中期可做：若想深入其函数重构的影响，需在 moderately_familiar 的 semiparametric theory 上加强。

### 2. [10.5705/ss.202025.0337](https://doi.org/10.5705/ss.202025.0337) · [arXiv](https://arxiv.org/abs/2508.14268) — Comparing Model-agnostic Feature Selection Methods Through Relative Efficiency
- **作者**: Chenghui Zheng, Garvesh Raskutti
- **期刊/来源**: Statistica Sinica
- **机构**: University of Wisconsin–Madison
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文在模型无关的特征选择框架下，提出基于相对效率（relative efficiency）的统一比较框架，用相对变异度 σ/μ 来调整不同统计量均值差异的影响。重点比较了两种主流方法：广义协方差度量（GCM）和留一协变量估计（LOCO），在三种模型设定下进行理论比较：线性模型、非线性可加模型和模拟单层神经网络的单指标模型。理论结果和模拟、真实数据均表明，在由某个相关性量定义的正则条件下，GCM 类方法通常优于 LOCO，该相关性量量化了渐近相对效率。实证部分涵盖了神经网络和梯度提升树等常用机器学习方法，并考虑了误设定模型。
- **关键技术**: `Generalized Covariance Measure (GCM)`, `Leave-One-Covariate-Out (LOCO)`, `relative efficiency`, `asymptotic relative efficiency`, `single index model`
- **为什么对您有用**: 本文属于假设检验与特征选择交叉领域，直接关联您对 hypothesis testing 和 semiparametric/nonparametric theory 的兴趣。其比较框架基于渐近相对效率，与您熟悉的 semiparametric efficiency 理论有直接接口。您可以用 very_familiar 的 minimax bounds 和 estimation theory 来审视其效率比较的紧性，或进一步分析 GCM 在更复杂模型下的效率性质。中期可做：若想深入其理论证明，需在 moderately_familiar 的 semiparametric theory 上加强。

### 3. [10.5705/ss.202025.0286](https://doi.org/10.5705/ss.202025.0286) — Statistical Inference for Heavy-tailed Vector Arma-gacrh/Igarch Models
- **作者**: Bibi Cai, Mengya Liu, Shiqing Ling
- **期刊/来源**: Statistica Sinica
- **机构**: Hong Kong University of Science and Technology
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对重尾向量 ARMA-GARCH/IGARCH 模型提出了一套完整的统计推断程序。首先引入自加权拟极大似然估计（self-weighted QMLE），在分数阶矩条件下建立了估计量的相合性和渐近正态性。基于自加权 QMLE，进一步建立了当噪声服从有限二阶矩向量 GARCH 或 IGARCH 模型时 VARMA 模型的局部 QMLE 的渐近正态性。利用这两种估计量，构造了用于检验线性和非线性约束的 Wald 统计量，特别提出了检验向量 IGARCH 模型的 Wald 统计量。此外还构造了两个 portmanteau 检验用于模型充分性诊断，所有检验统计量在样本量趋于无穷时均渐近服从 χ² 分布。模拟研究验证了有限样本下的良好表现，并通过一个真实数据示例展示了建模流程。对您而言，该文在重尾时间序列的假设检验与估计理论上提供了完整的工具，与您对 hypothesis testing 和 semiparametric 理论的兴趣直接相关。
- **关键技术**: `self-weighted quasi-maximum likelihood estimation`, `asymptotic normality under fractional moments`, `Wald tests for linear and nonlinear restrictions`, `portmanteau tests`, `vector GARCH/IGARCH models`
- **为什么对您有用**: 本文属于 hypothesis testing 与 semiparametric 估计理论的交叉，直接对应您 primary interests 中的 mathematical statistics (hypothesis testing) 和 semiparametric/nonparametric theory。您可运用 very_familiar 的 M-estimation 理论来审视其 self-weighted QMLE 的渐近论证，并考虑将高阶 U-统计量或张量收缩的工具用于检验统计量的高阶改进，属于立即可做的方向。

### 4. [10.5705/ss.202025.0436](https://doi.org/10.5705/ss.202025.0436) — Upper- and Lower-Quantile Functions with an Emphasis on Discrete Populations
- **作者**: Xiaolin Chen, Ruiyun Zhang, Min-Ge Xie, Xiaodong Yan
- **期刊/来源**: Statistica Sinica
- **机构**: Rutgers, The State University of New Jersey · Qufu Normal University · Beijing University of Technology · Xi'an Jiaotong University
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对离散总体下经典分位数估计量不一致且不渐近正态的问题，提出上分位数和下分位数两种新定义，通过线性插值技术消除经典分位数函数的间断性。样本上/下分位数在离散和绝对连续总体下均具有相合性和渐近正态性，从而为离散总体的分位数推断提供了有效工具。作者给出了理论证明和模拟验证，并展示了实际应用示例。该工作为离散数据的分位数估计与推断提供了新方法，对您在高维或非参数设定下处理离散协变量的分位数回归可能有用。
- **关键技术**: `linear interpolation`, `quantile estimation`, `asymptotic normality`, `discrete populations`
- **为什么对您有用**: 本文属于数学统计与假设检验方向，直接关联您对分位数估计和离散数据推断的兴趣。您可运用非参数统计中的经验过程理论来审视其渐近性质的证明，并考虑将其扩展到高维或因果推断中的分位数处理效应估计。

### 5. [10.5705/ss.202025.0271](https://doi.org/10.5705/ss.202025.0271) · [arXiv](https://arxiv.org/abs/2410.00574) — Asymmetric Garch Modelling Without Moment Conditions
- **作者**: Yuxin Tao, Huan Gong, Dong Li
- **期刊/来源**: Statistica Sinica
- **机构**: National University of Defense Technology · Tsinghua University
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出一种非对称 GARCH 模型，其创新点在于使用标准化非高斯稳定分布作为创新分布，从而允许方差乃至均值无限，摆脱了传统 GARCH 模型对有限矩的依赖。作者在平稳和爆炸两种情形下建立了完整的推断框架，证明了极大似然估计量（包括尾指数参数）的强相合性和渐近正态性，并讨论了多种渐近方差估计量。为进行诊断检验，他们构造了修正的 Kolmogorov 型检验统计量，并提出了严格平稳性和非对称性的检验。通过蒙特卡洛模拟和股票收益率的实证分析，展示了所提模型在重尾数据下的有限样本表现和实用性。该工作将稳定分布与 GARCH 建模结合，为金融时间序列的稳健推断提供了新工具。
- **关键技术**: `stable distribution`, `asymmetric GARCH`, `maximum likelihood estimation`, `asymptotic normality`, `Kolmogorov-type test`, `heavy-tailed time series`
- **为什么对您有用**: 本文属于假设检验与重尾时间序列推断，连接您对 hypothesis testing 和 heavy-tailed 数据的兴趣。您可用 very_familiar 的 minimax 或非参数工具审视其检验的功效与最优性，或利用 moderately_familiar 的 M-estimation 理论验证其估计量的渐近性质。立即可做的是基于其检验统计量进行数值模拟或理论扩展。

### 6. [10.5705/ss.202026.0032](https://doi.org/10.5705/ss.202026.0032) — Spatial Subsample Bootstraps for High-dimensional Spatial Data with Irregular Spacing
- **作者**: Yue Li, Shibin Zhang
- **期刊/来源**: Statistica Sinica
- **机构**: Shanghai Normal University
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文针对不规则空间位置上的高维空间数据，提出了一类空间子样本自助法（SSB），目标是在一般空间依赖下逼近高维空间统计量的联合分布，无需规则采样设计或显式估计依赖结构。具体提出了两种实现：空间乘子子样本自助法（SMSB）和空间经验子样本自助法（SESB），均基于重叠空间子样本统计量构造。作者在温和矩条件和弱空间依赖条件下，建立了对高维统计量（包括 max-type 和 studentized 统计量）联合分布逼近的渐近有效性，且允许维度随样本量发散甚至超过样本量。该方法避免了高维协方差矩阵的估计，在高维情形下计算高效。进一步，通过平衡自助逼近的偏差和方差主导项，推导了渐近最优子样本大小，并提出了具有最优性保证的数据驱动 plug-in 选择器。该结果为不规则设计下高维空间问题的基于自助法的推断提供了通用理论基础。对您而言，其子样本自助法的理论框架和最优子样本量选择机制，可迁移至高维空间因果推断中的不确定性量化问题。
- **关键技术**: `spatial subsample bootstrap`, `multiplier bootstrap`, `empirical bootstrap`, `max-type statistics`, `studentized statistics`, `optimal subsample size selection`
- **为什么对您有用**: 本文属于假设检验与高维统计的交叉，直接关联您对 hypothesis testing 和高维统计的兴趣。其子样本自助法为不规则空间数据提供分布逼近，可视为一种非参数重抽样工具，您可用 very_familiar 的 minimax bounds 和 high-dimensional asymptotics 来评估其最优子样本量选择器的有限样本表现，或将其思想扩展到空间因果推断中的敏感性分析。中期可做：需先熟悉空间统计中的强混合条件等依赖结构假设（moderately_familiar 的 semiparametric theory 可辅助），但核心方法（自助法）已在武器库内，因此立即可做初步理论探索。

### 7. [10.5705/ss.202025.0280](https://doi.org/10.5705/ss.202025.0280) · [arXiv](https://arxiv.org/abs/2404.03198) — Delaunay Weighted Two-sample Test for High-dimensional Data by Incorporating Geometric Information
- **作者**: Jiaqi Gu, Ruoxu Tan, Guosheng Yin
- **期刊/来源**: Statistica Sinica
- **机构**: University of Hong Kong
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文针对高维两样本检验问题，在数据位于低维流形的假设下，提出利用 Delaunay 三角剖分构造权重矩阵，以同时捕捉数据点间的距离与方向信息，克服传统仅基于成对距离的相似度度量在高维下的局限性。作者开发了学习未知流形并近似 Delaunay 权重的计算流程，并基于该权重矩阵构造非参数检验统计量。理论上证明了原假设下统计量的渐近正态性以及备择假设下的一致性。模拟研究表明，当分布差异体现在协方差矩阵的主方向时，新检验具有显著的功率提升，且对流形学习过程具有稳健性。在真实的小鼠蛋白质表达数据集上，该检验也检测到了显著差异。对您而言，该工作将几何信息引入高维两样本检验，与您在高维统计和假设检验方面的兴趣直接相关，其流形学习与权重构造思路可能为后续研究提供新视角。
- **关键技术**: `Delaunay triangulation`, `manifold learning`, `weighted two-sample test`, `asymptotic normality`, `high-dimensional testing`
- **为什么对您有用**: 该论文属于高维假设检验方向，直接对应您的主要兴趣之一。其利用几何信息构造检验统计量的思路，可结合您熟悉的非参数统计和极小极大界工具进行深入分析，例如检验统计量的收敛速率或权重矩阵的估计误差影响。从可行性看，您现有的非参数统计和极小极大界工具足以支撑理解与初步扩展，属于中期可做的方向，但需在流形学习的具体技术上稍作补充。

### 8. [10.5705/ss.202025.0172](https://doi.org/10.5705/ss.202025.0172) · [arXiv](https://arxiv.org/abs/2403.13544) — A Class of Bootstrap Based Residuals for Compositional Data
- **作者**: Gustavo H. A. Pereira, Jianwen Cai
- **期刊/来源**: Statistica Sinica
- **机构**: University of North Carolina at Chapel Hill
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文针对成分数据（compositional data）回归模型，提出了一类基于 bootstrap 的多元残差，其渐近服从标准正态分布，填补了该领域缺乏此类残差的空白。作者通过蒙特卡洛模拟验证了所提残差在小样本下分布近似标准正态的良好性质，并比较了不同残差在识别模型误设定方面的表现。模拟数据应用表明，所提残差中某一种在检测模型误设定上优于现有竞争者。最后，通过睡眠阶段数据的实例分析展示了最佳残差的实际用途。该方法不仅适用于成分数据回归，也可推广到其他多元回归模型。
- **关键技术**: `bootstrap residuals`, `compositional data regression`, `multivariate residuals`, `model misspecification diagnostics`, `Monte Carlo simulation`
- **为什么对您有用**: 本文属于假设检验与诊断分析的范畴，与您对 hypothesis testing 和 semiparametric/nonparametric theory 的兴趣相关。虽然成分数据不是您的核心方向，但残差构造与 bootstrap 方法在多元回归诊断中的思路，可能对您处理高维或半参数模型中的检验问题有启发。从技术武器库看，您对 nonparametric statistics 和 M-estimation 的熟悉程度足以理解本文方法，但若要深入推广到更复杂的模型，可能需要补充多元诊断理论的知识。总体而言，本文可作为中期可做的参考，但非立即可迁移的核心工作。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.5705/ss.202025.0275](https://doi.org/10.5705/ss.202025.0275) — Efficient Learning of Sparse Differential Networks in Multi-Source Non-Paranormal Models
- **作者**: Mojtaba Nikahd, Seyed Abolfazl Motahari
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究多源非参数正态（nonparanormal）图模型下稀疏差分网络的高效估计问题，目标是在两类图模型间识别结构变化（即差分网络）。现有基于lasso惩罚的D-trace损失方法计算成本高且存在近似误差，本文提出一种基于分段线性路径跟踪的solution-path算法，利用目标函数的结构在正则化参数范围内高效计算精确解，消除了近似误差并显著降低计算成本。同时，作者引入数据整合机制处理异质多源数据，并推导出与同质数据相匹配的非渐近样本复杂度界，表明统计效率无损。在合成数据上，该方法在速度和估计精度上均优于现有技术；在卵巢癌耐药和乳腺癌亚型两个真实数据集上，识别出的关键基因得到生物医学文献支持。对您而言，该文的solution-path算法与计算复杂度分析可迁移至您的高阶U统计量计算或统计计算兴趣，但核心贡献在于优化算法而非统计推断理论。
- **关键技术**: `D-trace loss`, `lasso penalization`, `piecewise-linear path-following`, `solution-path algorithm`, `nonparanormal graphical models`, `data integration`
- **为什么对您有用**: 该文属于统计计算方向，与您的primary interest中的statistical computing直接相关，尤其其路径跟踪算法可借鉴到您熟悉的高阶U统计量计算中。但该文核心是优化算法，而非您更核心的因果推断或高维理论，因此相关度中等。从武器库看，您对软件开发和数值方法熟悉，可立即理解算法实现，但若要深入分析其统计性质（如非渐近界），需借助您moderately_familiar的M估计理论。总体而言，作为统计计算的应用型论文，值得一读但非高优先。

## 其他  *(other, 2 篇)*

### 1. [10.5705/ss.202026.0091](https://doi.org/10.5705/ss.202026.0091) · [arXiv](https://arxiv.org/abs/2602.22282) — Differentially Private Truncation of Unbounded Data Via Public Second Moments
- **作者**: Zilong Cao, Xuan Bi, Hai Zhang
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究差分隐私（DP）框架下无界数据分布的截断问题。传统DP方法通常要求数据有界，而本文利用少量公开数据的二阶矩信息，提出Public-moment-guided Truncation（PMT）方法，将私有数据变换后按仅依赖维度和样本量的半径进行截断。该变换使二阶矩矩阵条件数良好，从而显著增强对DP噪声的抵抗能力。作者进一步将PMT应用于惩罚回归和广义线性回归，设计新的损失函数和算法，并保证变换空间中的解可映射回原空间。理论分析和实验表明，PMT在保持隐私的同时提升了估计精度。
- **关键技术**: `differential privacy`, `second-moment matrix`, `truncation`, `penalized regression`, `generalized linear regression`
- **为什么对您有用**: 本文属于统计计算与隐私保护交叉领域，与您的统计计算兴趣相关，但并非核心方向。作为入门读物，它清晰展示了如何利用公开数据辅助私有数据推断，但方法本身不涉及您武器库中的高阶U统计或因果推断工具。

### 2. [10.5705/ss.202026.0109](https://doi.org/10.5705/ss.202026.0109) — Inference for Extreme Value Index Through Individualized Fusion Learning
- **作者**: Hongfang Sun, Yu Chen, Tao Xu, Zhengjun Zhang
- **期刊/来源**: Statistica Sinica
- **机构**: Nanjing Normal University · University of Science and Technology of China · Fujian Agriculture and Forestry University
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出一种新的极值指数（EVI）估计框架——个体化融合学习（iFusion），旨在利用多个相关数据源的尾部信息来提高目标变量EVI的估计精度。在独立假设下，基于Hill估计量构造iFusion估计量，并证明其相合性和渐近正态性；进一步通过调整融合策略扩展到尾部相依数据源。模拟研究和臭氧浓度数据应用表明，该方法在方差缩减和样本外预测方面显著优于现有方法。该工作属于极值统计与多源数据融合的交叉领域，其核心思想与因果推断中的数据融合（如多个研究间的信息借用）有潜在联系，但方法论上更侧重于极值指标的估计效率。
- **关键技术**: `Hill estimator`, `individualized fusion learning`, `asymptotic normality`, `tail dependence`, `multi-source data`
- **为什么对您有用**: 本文涉及多源数据融合与效率提升，与您的主要兴趣（如效率理论、数据融合）有间接关联，但更偏向极值统计应用。作为gateway reading，它展示了如何在不同数据源间借用信息，可能对您思考因果推断中的跨样本信息整合有启发。武器库中的非参数统计和估计理论足以理解其核心方法，但该主题并非您的核心方向，建议作为拓展阅读。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

