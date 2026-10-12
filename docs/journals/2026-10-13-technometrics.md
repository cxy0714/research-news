# Technometrics  ·  2026-10-13

- 共 16 篇 · Technometrics

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期《Technometrics》的 16 篇论文大致可归为四条主线：**非参数与半参数方法**（含非欧数据特征筛选、校准贝叶斯容差区间）、**假设检验与不确定性量化**（多元函数型数据检验、联邦共形预测）、**统计计算与实验设计**（张量强化学习、函数边网络、傅里叶神经算子、序贯设计、拉丁超立方、主动学习、点云监控、OofA 设计、加速退化试验）、以及**应用驱动的建模与控制**（时空高斯过程风功率曲线、离线强化学习过程控制）。其中，计算与设计类论文数量最多，但方法论交叉明显，例如非参数思想渗透进容差区间和特征筛选，而张量与函数型工具则同时出现在网络建模和强化学习中。

最突出的主线是**统计计算与实验设计**，共 8 篇，覆盖从代理模型到监控的全流程。`Tensor-Efficient Q-learning` 用低秩 CP 张量压缩状态-动作空间，配合不确定性引导探索，直接回应高维强化学习的维度灾难；`Functional-Edged Network Modeling` 将函数 Tucker 分解与张量补全结合，处理边权随时间连续变化的网络，两者共享张量分解工具但目标迥异。实验设计方面，`Grouped Latin Hypercube Designs` 通过块正交化控制组间/组内相关性，`Hamming Weight Uniform Designs` 则用 Hamming 距离度量均匀性以构造对模型误设稳健的 OofA 设计，二者均强调设计矩阵的结构约束而非单纯空间填充。`Active Learning with Adaptive Non stationary Kernel` 与 `Fully Bayesian Sequential Design` 都聚焦序贯采样，前者针对连续保真度代理模型，后者用双高斯过程和 EB-IMSPE 准则处理异方差仿真，计算成本权衡是共同关切。`Registration-Free Monitoring` 和 `Quality-Ensured In-Situ Monitoring` 则把几何特征提取与深度典型相关分析引入工业监控，属于计算方法的落地应用。

第二条值得注意的主线是**假设检验与不确定性量化**，虽仅 3 篇但方法论互补。`A Modified Test for Linear Hypotheses in Multivariate Functional Data` 将 Wilks lambda 推广至函数型数据，用 Wishart 近似和 U 统计量自由度估计解决小样本异方差问题，直接面向多元均值函数检验；`Federated Conformal Approach` 针对联邦学习中交换性违反，用多水平隐马尔可夫模型估计重要性权重修正覆盖缺口，提供分布自由的预测区间；`Calibrated Bayesian Nonparametric Tolerance Intervals` 则从贝叶斯角度用校准 Gibbs 后验构造容差区间，将非参数先验与频率覆盖性质结合。三篇分别从频率检验、共形预测、贝叶斯校准切入，但都聚焦小样本或分布偏移下的推断可靠性。

若按主题优先阅读：因果推断方向虽无直接论文，但 `Calibrated Bayesian Nonparametric Tolerance Intervals` 的校准思路和 `Federated Conformal Approach` 的重要性加权修正可迁移至因果效应的稳健推断；半参数效率方向可关注 `Nonparametric Feature Screening for Non-Euclidean Data` 的 Fréchet R² 性质及其筛选一致性；高维方向则推荐 `Tensor-Efficient Q-learning` 和 `Functional-Edged Network Modeling` 的张量分解策略，以及 `Grouped Latin Hypercube Designs` 的块正交化思想。

## 非参数 / 半参数  *(nonparam_semipara, 2 篇)*

### 1. [10.1080/00401706.2026.2735885](https://doi.org/10.1080/00401706.2026.2735885) — Nonparametric Feature Screening for Non-Euclidean Data
- **作者**: Moshu Xu, Leheng Cai, Qirui Hu, Xu Guo
- **期刊/来源**: Technometrics
- **机构**: Tsinghua University · Shanghai University of Finance and Economics · Beijing Normal University
- **分类**: pp 1-92
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究响应变量取值于非欧几里得空间（如分布、矩阵）且结构非线性时的特征筛选问题。作者重新审视了 Fréchet R⊕2 的概念，并证明其具有经典 R2 的存在性、有界性、拟合优度、单调性和尺度不变性等性质。基于这些性质，提出了一种新的筛选过程——局部 Fréchet 确信独立筛选（local Fréchet sure independence screening），通过单变量局部 Fréchet 回归的经验 Fréchet R⊕2 来识别重要协变量。在温和条件下，建立了该过程的一致一致性、确信筛选和确信排序性质。大量数值研究支持了方法的正确性和有效性，并用死亡率数据和巴塞罗那足球俱乐部比赛数据（分别对应分布值和矩阵值响应）展示了实际性能。
- **关键技术**: `Fréchet regression`, `sure independence screening`, `local polynomial smoothing`, `uniform consistency`, `non-Euclidean data`
- **为什么对您有用**: 本文属于非参数统计与特征筛选的交叉方向，与您的非参数/半参数理论兴趣直接相关。您可以用 very_familiar 的 minimax 界工具来检验其确信筛选性质的有限样本表现，或考虑将 Fréchet R⊕2 与您熟悉的 U-统计量投影技术结合，分析其高阶性质。中期可做：若想深入其局部回归的收敛性，需在非欧几里得空间的度量结构上补充知识。

### 2. [10.1080/00401706.2026.2699103](https://doi.org/10.1080/00401706.2026.2699103) · [arXiv](https://arxiv.org/abs/2603.10924) — Calibrated Bayesian Nonparametric Tolerance Intervals
- **作者**: Tony Pourmohamad, Robert Richardson, Bruno Sansó
- **期刊/来源**: Technometrics
- **机构**: Brigham Young University · University of California, Santa Cruz
- **分类**: pp 1-13
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文提出一种基于校准 Gibbs 后验的完全非参数容差区间构造方法，适用于参数假设失效或小样本情形。作者利用容差限与总体分位数的联系，采用非对称 Laplace（check）损失函数构建 Gibbs 后验，并校准学习率以保证名义频率覆盖。模拟研究表明，该方法在保持可靠覆盖的同时，区间长度常短于经典非参数基准（如 Wilks 区间）。应用实例涵盖生态学、生物制药制造和环境监测，展示了方法的灵活性和稳健性。对您而言，该方法将贝叶斯非参数与频率覆盖性质结合，可能为半参数效率理论中的稳健推断提供新视角。
- **关键技术**: `Gibbs posterior`, `asymmetric Laplace loss`, `learning rate calibration`, `tolerance intervals`, `nonparametric quantile estimation`
- **为什么对您有用**: 本文属于非参数与半参数理论方向，涉及分位数估计和覆盖性质，与您的非参数/半参数理论兴趣直接相关。您可以用 very_familiar 的非参数统计和 minimax 界工具来分析其校准 Gibbs 后验的覆盖精度与最优性，例如检验其区间长度是否达到 minimax 最优。中期可做：需在 moderately_familiar 的 M-估计理论上加强，以严格推导其渐近性质。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1080/00401706.2026.2740126](https://doi.org/10.1080/00401706.2026.2740126) — A Modified Test for Linear Hypotheses in Multivariate Functional Data Under Heteroscedasticity and Small Samples
- **作者**: Tianming Zhu
- **期刊/来源**: Technometrics
- **机构**: Nanyang Technological University
- **分类**: pp 1-117
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对多元函数型数据（MFD）中的一般线性假设检验问题，提出了一种有限样本检验方法，目标是检验均值函数的线性组合是否满足给定假设。现有方法要么是重采样检验（耗时），要么是渐近检验（小样本下第一类错误控制不佳）。作者将MANOVA中的Wilks lambda检验推广到MFD，构造基于两个对称非负定矩阵的检验统计量，并用Wishart分布近似，自由度通过U统计量方法估计。该检验具有仿射不变性，对异方差稳健，计算效率高于重采样方法，且在小样本下比渐近检验更好地控制显著性水平。通过真实数据示例展示了其实用性。对您而言，该文将多元假设检验与函数型数据结合，并利用U统计量估计自由度，与您对假设检验和U统计量的兴趣直接相关。
- **关键技术**: `Wilks' lambda test`, `Wishart approximation`, `U-statistics-based degrees of freedom estimation`, `multivariate functional data`, `affine invariance`
- **为什么对您有用**: 该文属于假设检验方向，具体是函数型数据的多元线性假设检验，与您对假设检验的兴趣直接相关。文中用U统计量估计自由度，您可以用您对高阶U统计量的熟悉程度（如投影、渐近性质）来审视其估计的效率和有限样本表现。此外，该文提出的有限样本修正方法可能启发您在其他高维或函数型设定下设计类似检验。从可行性看，该文的核心工具（U统计量、Wishart近似）在您的武器库中属于非常熟悉或中等熟悉，因此可以立即可做：例如，验证其自由度估计的渐近性质或比较不同U统计量估计量的表现。

### 2. [10.1080/00401706.2026.2722103](https://doi.org/10.1080/00401706.2026.2722103) — Federated Conformal Approach for Trustworthy Uncertainty Quantification in Distributed Fleet Prognostics
- **作者**: Zihan Li, Mostafa Reisi Gahrooei, Minhee Kim
- **期刊/来源**: Technometrics
- **机构**: University of Florida
- **分类**: pp 1-21
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究联邦学习场景下预测模型的不确定性量化问题，目标是构造具有统计保证的预测区间。由于联邦学习中不同客户端数据分布存在异质性，且同一单元内部存在退化或进展模式，标准共形预测所依赖的交换性假设被违反，导致覆盖概率出现偏差。作者提出一种模型无关、分布自由的共形预测方法，通过多水平隐马尔可夫模型和联邦广义期望最大化算法估计重要性权重，以修正交换性违反带来的覆盖缺口。方法可事后应用于任意预测模型，并提供形式化的覆盖保证。在发动机退化与阿尔茨海默病进展两个数据集上的案例研究表明，该方法相比标准联邦学习和共形预测方法，能以更窄的区间达到目标覆盖率。对您而言，本文的覆盖缺口分析与重要性加权修正思路，可迁移到您关注的纵向因果推断中处理时间依赖与异质性时的推断问题。
- **关键技术**: `conformal prediction`, `importance weighting`, `hidden Markov model`, `federated expectation maximization`, `coverage guarantee`
- **为什么对您有用**: 本文属于假设检验/不确定性量化方向，与您的一级兴趣（假设检验）相关，但更偏向应用。其核心问题是交换性违反下的覆盖修正，与您在纵向因果推断中处理时间依赖和异质性时的推断问题有相通之处。您可以用非常熟悉的非参数统计和估计理论来审视其重要性权重估计的收敛性，中期可尝试将加权共形方法引入您的因果推断框架。

## 统计计算 / 算法  *(stat_computing, 8 篇)*

### 1. [10.1080/00401706.2026.2702440](https://doi.org/10.1080/00401706.2026.2702440) · [arXiv](https://arxiv.org/abs/2511.03595) — Tensor-Efficient High-Dimensional <i>Q</i> -learning
- **作者**: Junyi Wu, Dan Li
- **期刊/来源**: Technometrics
- **机构**: University of Washington
- **分类**: pp 1-12
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对高维强化学习中 Q-learning 的维度灾难问题，提出 Tensor-Efficient Q-Learning (TEQL) 方法。该方法将 Q 函数表示为离散状态-动作空间上的低秩 CP 张量，利用张量结构进行参数高效表示，并引入 Error-Uncertainty Guided Exploration (EUGE) 机制，结合张量近似误差与访问次数指导动作选择，同时采用频率感知正则化稳定更新。在匹配参数预算下，经典控制任务的实验表明 TEQL 在样本效率上优于矩阵低秩方法和深度 RL 基线。该方法适用于采样成本高的资源受限场景。对您而言，本文展示了如何将低秩张量分解与不确定性量化结合，提升高维估计问题的计算与样本效率，与您在高阶 U 统计量中利用张量收缩计算效率的兴趣点直接相关。
- **关键技术**: `CP tensor decomposition`, `low-rank tensor representation`, `uncertainty-aware exploration`, `frequency-aware regularization`, `Q-learning`
- **为什么对您有用**: 本文属于统计计算方向，直接关联您对张量分解与计算效率的兴趣。您可运用 very_familiar 的 tensor contraction / einsum 复杂度分析工具，评估 TEQL 中 CP 分解的更新成本，并探索将 EUGE 的不确定性量化思想迁移到高阶 U 统计量的计算中。中期可做：需在 moderately_familiar 的强化学习理论（如 regret 界）上补充知识，以严格分析 TEQL 的样本效率。

### 2. [10.1080/00401706.2026.2724145](https://doi.org/10.1080/00401706.2026.2724145) · [arXiv](https://arxiv.org/abs/2404.00218) — Functional-Edged Network Modeling
- **作者**: Haijie Xu, Bo Zhang, Chen Zhang
- **期刊/来源**: Technometrics
- **机构**: Tsinghua University
- **分类**: pp 1-17
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究一类新型网络——函数边网络，其中每条边的权重是随时间平滑变化的函数而非标量或向量。为建模此类网络，作者引入函数邻接张量，将传统邻接矩阵扩展出连续函数维度。为分析该张量的结构模式，提出函数 Tucker 分解框架，并对基矩阵施加对称正则化以捕捉节点社区结构。针对函数边观测不规则的问题，将模型推断表述为张量补全问题，并采用黎曼共轭梯度法求解。理论上建立了所提模型的估计性质，并在香港地铁系统和工业物联网 RSSI 数据上验证了有效性。对您而言，该文的函数 Tucker 分解与张量补全算法可能为您的统计计算兴趣提供新的数值方法参考，但其核心并非您的主要研究方向。
- **关键技术**: `functional Tucker decomposition`, `tensor completion`, `Riemannian conjugate gradient`, `symmetry regularization`, `functional adjacency tensor`
- **为什么对您有用**: 本文属于统计计算方向，与您的 statistical computing 兴趣相关，但并非核心。其函数张量分解和黎曼优化方法可能对您处理高维张量问题有启发，但您更熟悉的是 U-统计量和张量收缩复杂度，本文未涉及计算复杂度分析。作为入门读物，本文方法清晰但应用导向，不值得深入阅读。

### 3. [10.1080/00401706.2026.2736750](https://doi.org/10.1080/00401706.2026.2736750) · [arXiv](https://arxiv.org/abs/2601.01813) — Spatio-temporal modeling and forecasting with Fourier neural operators
- **作者**: Pratik Nag, Andrew Zammit-Mangion, Sumeetpal Singh, Noel Cressie
- **期刊/来源**: Technometrics
- **机构**: University of Wollongong · UNSW Sydney
- **分类**: pp 1-78
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文提出使用傅里叶神经算子（FNO）构建统计动态时空模型（DST）用于预测，目标是在无需显式偏微分方程（PDE）知识的情况下，高效逼近未知或非线性PDE的解算子。FNO作为函数映射，通过输入输出样本学习，避免了传统高斯过程等统计模型在复杂环境异质性和交互作用上的建模困难。通过已知解的PDE模拟，作者将FNO预测与最先进的统计时空预测方法比较，并在大西洋海表温度和欧洲降水数据上验证了FNO-DST的预测能力。结果显示FNO-DST预测准确且提供了有效的不确定性量化。
- **关键技术**: `Fourier neural operators`, `spatio-temporal modeling`, `uncertainty quantification`, `PDE solution operator approximation`, `deep learning forecasting`
- **为什么对您有用**: 本文属于统计计算方向，涉及深度学习方法在时空建模中的应用，与您的统计计算兴趣相关。虽然FNO不是您熟悉的传统统计方法，但作为统计计算的新兴工具，值得了解其方法论和不确定性量化框架。武器库中的非参数统计和软件工程技能可帮助您评估其预测性能，但核心的神经网络架构和训练机制不在当前武器库中，属于中期可探索方向。

### 4. [10.1080/00401706.2026.2703239](https://doi.org/10.1080/00401706.2026.2703239) · [arXiv](https://arxiv.org/abs/2506.09722) — Fully Bayesian Sequential Design for Heteroscedastic Stochastic Simulations
- **作者**: Yuying Huang, Samuel W. K. Wong
- **期刊/来源**: Technometrics
- **机构**: University of Waterloo
- **分类**: pp 1-16
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出一种全贝叶斯序贯设计策略，用于预测异方差随机仿真模型的均值响应面。采用双高斯过程作为代理模型，并基于期望贝叶斯积分均方预测误差（EB-IMSPE）作为选择准则，在序贯采样中充分考虑参数不确定性。通过序贯重要性采样高效更新参数后验分布，适用于预算有限的昂贵仿真模型。在合成数据上展示了相比现有方法在预测精度、噪声估计和不确定性量化方面的优势，并在木结构裙楼建筑抗震设计的实际应用中验证了有效性。对您而言，该文涉及统计计算与算法设计，与您对统计计算（数值方法、算法）的兴趣直接相关，其中序贯采样和代理模型优化策略可能对您的高维或因果推断中的计算问题有启发。
- **关键技术**: `dual Gaussian processes`, `expected Bayesian integrated mean-square prediction error`, `sequential importance sampling`, `Bayesian sequential design`, `heteroscedastic stochastic simulation`
- **为什么对您有用**: 本文属于统计计算方向，与您的统计计算（数值方法、算法）兴趣直接相关。您可以用您非常熟悉的软件开发和数值方法技能，快速复现其序贯设计算法，并探索将其应用于您熟悉的因果推断或高维问题中的计算瓶颈。该文是应用导向的方法论文，可作为中期可做的参考，无需额外长肌肉。

### 5. [10.1080/00401706.2026.2719486](https://doi.org/10.1080/00401706.2026.2719486) · [arXiv](https://arxiv.org/abs/2509.19652) — Quality-Ensured In-Situ Process Monitoring with Deep Canonical Correlation Analysis
- **作者**: Xiaoyang Song, Wenbo Sun, Metin Kayitmazbatir, Jionghua (Judy) Jin
- **期刊/来源**: Technometrics
- **机构**: University of Michigan · Istanbul Technical University
- **分类**: pp 1-13
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出一种基于深度典型相关分析（DCCA）的在线过程监控方法，用于先进制造中高维过程信号（如光谱）与离线产品质量数据（如CT图像）的非线性关联建模。该方法通过联合特征提取与相关性分析，学习质量导向的表示，无需标记缺陷样本，并避免了传统控制图方法对非正态性的依赖。作者给出了算法稳定性与收敛性的理论保证，并通过仿真和直接金属沉积（DMD）增材制造的真实案例验证了其有效性。对您而言，其多模态数据融合与无监督表示学习框架，可作为统计计算与高维数据降维应用的一个参考案例。
- **关键技术**: `Deep Canonical Correlation Analysis (DCCA)`, `multi-modal feature extraction`, `unsupervised representation learning`, `process monitoring`, `control chart`
- **为什么对您有用**: 本文属于统计计算与高维数据应用方向，与您的统计计算兴趣相关，但方法学新颖性一般。作为入门读物，它展示了深度学习工具在工业过程监控中的实际应用，但理论深度有限。您的武器库（如高维统计、U统计量）足以理解其方法，但无需深入跟进。

### 6. [10.1080/00401706.2026.2707208](https://doi.org/10.1080/00401706.2026.2707208) — Grouped Latin Hypercube Designs with Controlled Correlations
- **作者**: Wenlong Li, Jian-Feng Yang, Peter Chien
- **期刊/来源**: Technometrics
- **机构**: Beijing Jiaotong University · Nankai University · University of Wisconsin–Madison
- **分类**: pp 1-11
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对现代计算机实验中输入变量分组的情形，提出了一类新的拉丁超立方设计——分组拉丁超立方设计（GLHD-CC）。该设计将设计矩阵的列划分为不相交的组，使得组间列相关性被控制在一个较低水平，而组内列相关性更低，从而在保持整体空间填充性的同时实现分组结构。构造方法基于多元线性回归中的多元块正交化技术，可同时控制多个变量间的相关性。作者给出了高效的构造算法，并建立了理论性质，算法在运行次数和输入维度上具有灵活性。通过三个常用测试函数和一个真实黑箱模拟器案例验证了方法的有效性。对您而言，该文属于统计计算与实验设计交叉方向，其块正交化与相关性控制思想可迁移到您在高维统计或因果推断中处理分组协变量时的设计问题。
- **关键技术**: `Latin hypercube design`, `block orthogonalization`, `multivariate linear regression`, `correlation control`, `computer experiments`
- **为什么对您有用**: 该文属于统计计算与实验设计方向，与您的 statistical computing 兴趣直接相关。您可用 very_familiar 的软件开发和数值方法技能快速实现其算法，并检验其理论性质；中期可做的是将块正交化思想与您 moderately_familiar 的 M-estimation 理论结合，用于分组协变量的半参数估计设计；暂不可做则无需，因为核心工具已在武器库内。

### 7. [10.1080/00401706.2026.2702433](https://doi.org/10.1080/00401706.2026.2702433) · [arXiv](https://arxiv.org/abs/2503.23158) — Active Learning with Adaptive Non stationary Kernel for Continuous-Fidelity Surrogate Models
- **作者**: Romain Boutelet-Smith, Chih-Li Sung
- **期刊/来源**: Technometrics
- **机构**: Michigan State University
- **分类**: pp 1-12
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对多保真度计算机实验的代理模型问题，其中保真度由连续参数控制（如有限元网格密度），目标是利用廉价低保真模拟辅助昂贵高保真模拟，并对未观测保真度水平进行推断。作者提出一种新的自适应非平稳核函数，以更准确地刻画模拟输出随保真度参数变化的非平稳行为。同时，基于积分均方预测误差（IMSPE）准则开发主动学习策略，在输入参数和保真度参数空间中联合选择设计点，并将不同保真度的计算成本纳入优化。方法通过数值例子和有限元应用验证，并提供了开源的R包。对您而言，该文的主动学习与计算成本权衡思路可迁移到您在高维或因果推断中涉及昂贵模拟或计算受限的场景。
- **关键技术**: `multi-fidelity surrogate modeling`, `non-stationary kernel`, `active learning`, `IMSPE`, `Gaussian process`
- **为什么对您有用**: 本文属于统计计算方向，与您的 primary interest 中的 statistical computing 直接相关。您可以用 very_familiar 的软件开发和 minimax 估计视角来审视其主动学习准则的统计效率，例如分析 IMSPE 选择是否在计算成本约束下达到某种最优性。中期可做：若想深入理论，需在 moderately_familiar 的 M-estimation 理论上加强，以推导其估计量的渐近性质。

### 8. [10.1080/00401706.2026.2702438](https://doi.org/10.1080/00401706.2026.2702438) · [arXiv](https://arxiv.org/abs/2511.05623) — Registration-Free Monitoring of Unstructured Point Cloud Data via Intrinsic Geometrical Properties
- **作者**: Mariafrancesca Patalano, Giovanna Capizzi, Kamran Paynabar
- **期刊/来源**: Technometrics
- **机构**: University of Padua · Georgia Institute of Technology
- **分类**: pp 1-13
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对现代制造中非结构化点云数据（PCD）的在线监控问题，提出一种免配准（registration-free）的统计过程控制方法，无需预处理中的配准和网格重建步骤，以避免其引入的误差和伪影。方法包含两种特征学习方案，分别基于拉普拉斯算子和测地距离提取形状的内在几何特征，并采用无分布监控方案处理数百维特征。监控方案中利用阈值技术进一步筛选对异常状态最敏感的内在特征，以提升检测能力。数值实验和案例研究验证了该方法在识别不同类型缺陷（如局部变形、表面异常）方面的有效性。该方法对您可能有用，因为它展示了将几何特征提取与统计监控结合的新思路，可连接到您的统计计算兴趣，尤其是算法设计和数值方法在工业应用中的实践。
- **关键技术**: `Laplacian eigenfeatures`, `geodesic distance features`, `distribution-free monitoring`, `feature selection via thresholding`, `point cloud data analysis`
- **为什么对您有用**: 本文属于统计计算与工业应用交叉领域，与您的统计计算兴趣相关，但并非核心方法学创新。作为入门读物，它清晰展示了点云数据的特征提取和监控流程，但武器库（如非参数统计、高维方法）足以支撑理解，无需额外工具。值得花时间读全文以了解工业场景中的实际问题，但方法学迁移性有限。

## 其他  *(other, 4 篇)*

### 1. [10.1080/00401706.2026.2705589](https://doi.org/10.1080/00401706.2026.2705589) · [arXiv](https://arxiv.org/abs/2607.00051) — Spatio-Temporal Gaussian Process for Building Terrain-Incorporating Wind Power Curves
- **作者**: Ahmadreza Chokhachian, V. Roshan Joseph, Yu Ding
- **期刊/来源**: Technometrics
- **机构**: Georgia Institute of Technology
- **分类**: pp 1-13
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文提出一种非参数时空高斯过程模型，用于构建融合地形协变量的风力发电功率曲线。现有模型多仅考虑风速、温度等时间变量，而忽略影响入流条件的地形特征。模型采用可分离核结构同时捕捉空间与时间依赖，但风场数据缺乏时间对齐，作者通过构造共享的代表性时间协变量集解决此问题，该集合大小比原始数据小一个数量级。在真实风场数据上的实证分析表明，该方法优于现有基线，并能量化地形特征对涡轮性能的影响。
- **关键技术**: `spatio-temporal Gaussian process`, `separable kernel`, `representative temporal covariate set`, `nonparametric regression`
- **为什么对您有用**: 本文属于统计计算与高斯过程建模的应用，与您的统计计算兴趣相关，但并非核心方向。作为入门阅读，它展示了如何将复杂时空数据转化为可计算的可分离核模型，但方法学新颖性有限，主要贡献在于数据对齐策略。武器库中的非参数统计和高维渐近工具足以理解其方法，但无需深入跟进。

### 2. [10.1080/00401706.2026.2739351](https://doi.org/10.1080/00401706.2026.2739351) — Hamming Weight Uniform Designs for Order-of-Addition Experiments
- **作者**: Yuwei Song, Min-Qian Liu, Jianbin Chen
- **期刊/来源**: Technometrics
- **机构**: Nankai University · Beijing Institute of Technology
- **分类**: pp 1-46
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究 order-of-addition (OofA) 实验设计，目标是构造对模型误设稳健的设计，使估计量在多种模型下保持一致性和渐近等价性。作者引入 Hamming weight 作为新的均匀性度量，建立了全设计中 Hamming weight 分布的理论性质，并据此高效构造 Hamming weight uniform designs (HWUDs)。HWUDs 保证估计量一致性，与全设计渐近等价，并在不同模型下表现稳健。此外，HWUDs 为渠道归因问题提供了基于设计的模型稳健框架。真实数据实验表明，HWUDs 在统计精度和计算效率上均优于现有方法。
- **关键技术**: `Hamming weight`, `uniform designs`, `order-of-addition experiments`, `model-robust design`, `asymptotic equivalence`
- **为什么对您有用**: 本文属于实验设计领域，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接交集，但其中对模型稳健性和渐近等价性的处理思路，可能对您在因果推断中的敏感性分析有所启发。作为 gateway reading，本文对实验设计的基本概念有清晰阐述，但并非您当前研究方向的直接入口，武器库足以理解，但无需深入。

### 3. [10.1080/00401706.2026.2733032](https://doi.org/10.1080/00401706.2026.2733032) — Planning Dual-Stress Accelerated Degradation Tests with Random-Effects Wiener Process Models
- **作者**: Guanqi Fang, Xi He, Yizi Wang, Rong Pan
- **期刊/来源**: Technometrics
- **机构**: Zhejiang Gongshang University · Arizona State University
- **分类**: pp 1-114
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文研究加速退化试验（ADT）的最优设计问题，在随机效应Wiener过程框架下同时考虑单元间初始退化水平和退化速率的异质性及其相关性（即“initiation-growth”相关）。目标是选择试验条件设置和样本分配，以最小化正常使用条件下第p分位寿命估计的渐近方差。针对双应力ADT，提出一种分裂策略，将两点退化设计中的低应力点沿等应力方向分解，同时保持加权质心不变，从而生成统计上等价的三点非退化设计，并证明边界极端分裂在该类设计中达到D-最优性。还探讨了增强鲁棒性的折中设计，以及基于初始退化水平排序的分配规则，但比较显示该规则并不总是优于随机分配。案例研究验证了方法的实用性。
- **关键技术**: `Wiener process with random effects`, `asymptotic variance minimization`, `C-optimality`, `D-optimality`, `design of experiments`
- **为什么对您有用**: 本文属于工程统计中的试验设计领域，与您的主要兴趣（因果推断、高维统计等）无直接交集，但作为Technometrics的应用统计工作，其最优设计框架和渐近方差方法可能对您理解统计计算中的优化问题有一定参考价值。不过，它并非您关注的核心方向，且不涉及您武器库中的具体工具，因此仅作为边缘阅读。

### 4. [10.1080/00401706.2026.2689966](https://doi.org/10.1080/00401706.2026.2689966) — Model-Based Prior for Model-Free Reinforcement Learning in Process Control: An Offline Methodology for Semiconductor Manufacturing
- **作者**: Yanrong Li, Fugee Tsung, Wei Jiang, Juan Du, Zhi-Sheng Ye
- **期刊/来源**: Technometrics
- **机构**: National University of Singapore · Hong Kong University of Science and Technology · The Hong Kong University of Science and Technology (Guangzhou) · Shanghai Jiao Tong University
- **分类**: pp 1-15
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对先进制造中的过程控制问题，提出一种融合基于模型先验知识的无模型强化学习（RL）控制方法。在离线学习阶段，利用非参数回归近似未知过程动态，并用高斯过程预测不可观测的扰动；在线控制阶段，将这两者与策略梯度搜索 RL 算法结合，仅依赖固定历史数据，无需实时试验。理论性质（如估计误差对控制性能的影响）得到讨论，并通过仿真和结晶过程案例验证有效性。该方法的核心贡献在于用模型先验简化模型结构并降低无模型控制器的方差，属于统计与控制的交叉应用。对您而言，本文的非参数回归与高斯过程组合建模思路，以及离线-在线两阶段框架，可能对您在高维或半参数估计中的实际应用有启发，但方法论新颖性有限。
- **关键技术**: `nonparametric regression`, `Gaussian process`, `policy gradient RL`, `offline RL`, `process control`
- **为什么对您有用**: 本文属于统计计算与工业应用交叉，与您的统计计算兴趣有间接关联，但并非核心方向。作为应用型论文，其非参数回归与高斯过程结合的方法可迁移性有限，且未涉及因果推断或高维理论。武器库中的非参数统计和软件技能足以理解，但无需深入。建议作为了解工业界统计应用的泛读材料，不值得投入全文精读。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

