# Scand. J. Stat.  ·  2026-10-10

- 共 11 篇 · Scandinavian Journal of Statistics

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Scand. J. Stat.》的11篇论文大致可归为四条主线：**因果推断与面板数据**（DML-GMM估计量）、**分布检验与相关度量**（半距离检验、区间删失相关度量、Stein型刻画）、**非参数与半参数方法**（污染生存估计、环面预测子局部Fréchet回归）、以及**统计计算与抽样设计**（HMM后验分析、集群随机试验样本量、切片空间填充设计、有放回平衡抽样、成对卡尔曼滤波器鲁棒性）。其中前三条主线在方法深度上较为突出，且与因果、半参数效率、高维检验的交叉点密集。

因果推断主线仅一篇，但值得展开：**Partially Linear Panel Data Model With Double/Debiased Machine Learning** 将横截面DML框架推广至带双向固定效应的面板数据，通过Neyman正交条件与交叉拟合构造GMM估计量，处理机器学习估计非线性分量带来的偏差。其渐近方差的一致估计为纵向因果推断提供了效率理论支撑，应用场景（学校开放对COVID-19传播的影响）也具现实意义。这一篇与半参数效率的衔接最直接，适合关注面板因果效应的读者优先阅读。

分布检验与相关度量主线有三篇，共同点在于处理复杂数据结构下的推断问题。**Unified Semi-Distance-Based Approaches for Equal Distribution Testing** 提出基于半距离的统一两样本检验框架，覆盖高维与函数型数据，并给出根号n相合的局部备择最优功效，其快速零分布近似绕开置换检验的计算瓶颈。**A New Correlation Measure for Interval-Censored Failure Time Data** 基于秩变换构造非参数相关度量，在高维下计算负担显著降低，并衍生出具备sure screening性质的模型无关特征筛选。**Unified Stein-Type Characterizations of Bivariate Count Distributions** 将Stein方法系统推广至二元计数分布，统一三类分布的刻画并构造拟合优度与对称性检验，为多元离散数据的检验提供了新工具。这三篇分别从距离、秩、Stein恒等式切入，但都服务于高维或复杂数据下的分布推断，可对照阅读。

非参数主线两篇各有侧重：**Nonparametric Survival Estimation With Contaminated and Adjudicated Events** 在右删失与事件污染并存时引入核平滑条件专家Kaplan-Meier估计量，量化专家信息不完美导致的确定性偏差，其偏差分析框架对测量误差场景有参考价值。**Local Fréchet Regression With Toroidal Predictors** 首次将局部Fréchet回归推广至环面预测子空间，构造尊重几何结构的内在估计量并建立收敛速率，对非欧空间非参数估计的推广思路可迁移至因果推断中的非参数设定。其余四篇（HMM后验分析、集群随机试验样本量、切片空间填充设计、有放回平衡抽样、成对卡尔曼滤波器鲁棒性）分属统计计算与抽样设计，与核心方法主线关联较弱，但其中**Sample Size Determination for Win Statistics** 的闭式方差公式对集群随机试验的复合终点分析有实用价值。

若按主题优先排序：因果推断与半参数效率方向，首看DML-GMM面板数据一文；高维检验与特征筛选方向，半距离检验与区间删失相关度量两篇最贴；非参数几何推广方向，环面预测子局部Fréchet回归值得关注。

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1111/sjos.70090](https://doi.org/10.1111/sjos.70090) — Estimation of Partially Linear Panel Data Model With Double/Debiased Machine Learning
- **作者**: Peikai Wu, Zhiguo Xiao
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Fudan University
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究带双向固定效应的部分线性静态/动态面板数据模型，其中非线性分量由机器学习估计，目标是估计线性分量的参数。作者将横截面DML框架推广到面板数据，利用Neyman正交条件和交叉拟合构造GMM估计量，以消除机器学习估计带来的偏差。在温和条件下建立了DML-GMM估计量的渐近性质，并给出渐近方差的一致估计。模拟表明该方法在复杂设定下优于常见估计量。最后应用于美国K-12学校开放对COVID-19传播的影响。对您而言，该文将DML与面板数据结合，是效率理论在纵向因果推断中的直接应用。
- **关键技术**: `double/debiased machine learning`, `Neyman orthogonality`, `cross-fitting`, `GMM`, `two-way fixed effects`, `panel data`
- **为什么对您有用**: 该文直接连接您的因果推断（纵向/面板）与效率理论（DML）兴趣；您可用very_familiar的估计理论在因果推断中审视其正交条件的构造，中期可做：用semiparametric theory（moderately_familiar）验证其效率界是否紧；立即可做：将其DML-GMM框架与您熟悉的HOIF结合，探索高阶正交性。

## 非参数 / 半参数  *(nonparam_semipara, 2 篇)*

### 1. [10.1111/sjos.70095](https://doi.org/10.1111/sjos.70095) · [arXiv](https://arxiv.org/abs/2512.14959) — Nonparametric Survival Estimation With Contaminated and Adjudicated Events
- **作者**: Martin Bladt, Kristian Vilhelm Dinesen
- **期刊/来源**: Scandinavian Journal of Statistics
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究条件专家 Kaplan–Meier 估计量，用于同时存在右删失和事件污染（observed events 可能非真实结局）的生存数据，其中专家意见用于裁定不确定事件，常见于保险和信用风险场景。在已有工作的基础上，作者通过核平滑引入协变量，发展该估计量的渐近理论。在正则条件下建立了函数一致性（functional consistency）和弱收敛，并量化了专家信息不完美所导致的偏差。结果表明，无偏的专家判断保证一致性，而系统性偏差会导致可显式表征的确定性渐近偏差。通过模拟研究考察有限样本性质，并应用于贷款违约数据。对您而言，该工作将非参数生存估计与测量误差/污染数据结合，其偏差分析框架可迁移到您熟悉的因果推断中关于 misclassification 的敏感性分析问题。
- **关键技术**: `Kaplan-Meier estimator`, `kernel smoothing`, `functional weak convergence`, `asymptotic bias characterization`, `right-censoring`, `event contamination`
- **为什么对您有用**: 该文属于非参数/半参数理论方向，与您 primary interest 中的非参数估计和假设检验相关；其处理污染事件与专家裁定的设定，可类比因果推断中的 misclassification 或 measurement error 问题，您可用 very_familiar 的非参数工具（如核估计、经验过程）理解其证明，并考虑将偏差分析思路用于因果推断的敏感性分析；属于立即可读的文献，无需额外工具。

### 2. [10.1111/sjos.70093](https://doi.org/10.1111/sjos.70093) · [arXiv](https://arxiv.org/abs/2602.20572) — Local Fréchet Regression With Toroidal Predictors
- **作者**: Chang Jun Im, Jeong Min Jeon
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Seoul National University
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出首个同时处理一般度量空间响应与环面预测子的回归框架，填补了局部Fréchet回归在非欧预测空间上的空白。作者构造了内在的局部常数与局部线性估计量，分别尊重响应与预测空间的几何结构；其中局部线性估计量即使在标量响应情形下也不同于现有方法。对两种估计量均建立了相合性与收敛速率，理论分析依赖于度量空间中的非参数回归技巧与环面上的局部平滑。模拟实验涵盖标量与球面响应，并应用于图拉普拉斯值响应的真实数据，展示了方法的实用优势。该工作对您非参数与半参数理论方向有直接参考价值，尤其是将局部回归推广到非欧几何空间的思路可迁移至因果推断中的非参数估计。
- **关键技术**: `local Fréchet regression`, `intrinsic local linear estimator`, `metric space responses`, `torus predictors`, `consistency and convergence rates`
- **为什么对您有用**: 该论文属于非参数与半参数理论方向，具体涉及局部回归在非欧空间（环面预测子、度量响应）的推广，与您对非参数估计的 minimax 速率和几何结构兴趣相关。您可用 very_familiar 的非参数统计与 minimax 界工具，检验其收敛速率是否最优，或探索将此类几何感知估计量用于因果推断中的非参数 nuisance 估计。中期可做：需在 moderately_familiar 的半参数理论上稍加延伸，以处理响应空间的复杂结构。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1111/sjos.70094](https://doi.org/10.1111/sjos.70094) — Unified Semi‐Distance‐Based Approaches for Equal Distribution Testing With Applications
- **作者**: Bu Zhou, Meichen Qian, Tianming Zhu, Jin‐Ting Zhang
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Zhejiang Gongshang University · Zhejiang University · National University of Singapore · Nanyang Technological University · National Institute of Education
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文提出一种统一的基于半距离的两样本分布检验方法，适用于高维数据和函数型数据等复杂数据对象。检验统计量基于两组样本间的半距离（如能量距离的推广），其渐近零分布和非零分布均被建立。与置换方法不同，作者提出一种快速且精确的零分布近似方法，避免了计算密集的置换检验。检验被证明是根号 n 相合的（root-n consistent），即检验功效在局部备择下具有最优收敛速率。数值实验表明该方法在尺寸控制、功效和计算成本方面均表现优异，并展示了在高维和函数型数据上的应用。
- **关键技术**: `semi-distance`, `two-sample testing`, `energy distance`, `asymptotic null distribution`, `root-n consistency`
- **为什么对您有用**: 该文属于假设检验方向，与您的主要兴趣（数学统计与假设检验）直接相关。其半距离框架与能量距离的联系，可结合您熟悉的非参数统计和 U-统计量工具进行深入分析。具体而言，检验统计量可视为二阶 U-统计量，您可以用 very_familiar 的 U-统计量投影理论来推导其渐近性质，并进一步探索高阶半距离检验的推广，属于立即可做的方向。

### 2. [10.1111/sjos.70081](https://doi.org/10.1111/sjos.70081) — A New Correlation Measure for Interval‐Censored Failure Time Data and Application
- **作者**: Zhimiao Cao, Huiqiong Li, Jianguo Sun, Niansheng Tang
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Yunnan University · Shandong University of Finance and Economics · Southern University of Science and Technology
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对区间删失失效时间数据，提出一种新的相关度量并给出经验估计量。该度量基于秩变换，无需指定模型，适用于两个随机向量间的相关性度量。作者建立了估计量的相合性和渐近正态性，并特别指出在高维数据下相比现有准则计算负担显著降低。基于该度量，进一步提出模型无关的特征筛选过程，并证明了其 sure screening 性质和秩相合性。模拟研究验证了筛选过程在实践中的良好表现，并给出了实际数据示例。对您而言，该文将非参数相关度量与高维特征筛选结合，其计算优势可能对您在高维统计和统计计算方面的兴趣有参考价值。
- **关键技术**: `rank-based correlation`, `interval-censored data`, `feature screening`, `sure screening property`, `asymptotic normality`
- **为什么对您有用**: 该文属于高维统计中的特征筛选方法，与您的高维统计兴趣相关，但更偏向应用方法而非理论深度。其计算优势可能对您的统计计算兴趣有启发，但核心方法（秩相关）不在您的技术武器库中，且与您的主要研究方向（因果推断、半参数效率等）连接较弱。作为入门或应用参考可读，但非核心。

### 3. [10.1111/sjos.70092](https://doi.org/10.1111/sjos.70092) — Unified Stein‐Type Characterizations of Bivariate Count Distributions With Applications
- **作者**: Shaochen Wang, Christian H. Weiß
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: South China University of Technology · Helmut Schmidt University
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对三类二元计数分布（二元 Poisson、I 型二元二项、二元负二项）建立统一的 Stein 型刻画。作者发现一个仿射对数导数方程可以同时导出这三种分布各自的 Stein 恒等式，从而将连续与一元离散情形的 Stein 方法推广到二元计数设定。基于这些恒等式，文章给出了概率与矩的递推公式，并构造了拟合优度检验以及关于二元计数分布对称性的检验。理论部分推导了检验统计量的渐近性质，并通过模拟和真实数据示例验证了方法的实用性。对您而言，该文将 Stein 方法系统性地引入多元离散分布，为构造高维或纵向计数数据的检验提供了新工具。
- **关键技术**: `Stein's method`, `bivariate count distributions`, `goodness-of-fit tests`, `symmetry tests`, `probability and moment recursions`
- **为什么对您有用**: 本文属于假设检验方向，直接连接您对 hypothesis testing 的兴趣；Stein 恒等式是构造检验与近似的重要工具，您可用 very_familiar 的软件开发和数值方法快速实现其检验统计量，并探索扩展到更高维或纵向计数数据的可能性，属于立即可做的 follow-up。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1111/sjos.70088](https://doi.org/10.1111/sjos.70088) · [arXiv](https://arxiv.org/abs/2504.15156) — Advanced Posterior Analyses of Hidden Markov Models: Finite Markov Chain Imbedding and Hybrid Decoding
- **作者**: Zenia Elise Damgaard Bæk, Moisès Coll Macià, Laurits Skov, Asger Hobolth
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Aarhus University · University of Copenhagen
- 相关性 5/10 · novelty: `minor`
- **摘要**: 本文研究隐马尔可夫模型（HMM）的两类后验分析任务：计算隐状态序列汇总统计量的分布，以及解码隐状态序列。作者采用有限马尔可夫链嵌入（FMCI）方法，基于给定观测序列的隐状态后验样本，计算访问次数、总停留时间、逗留时间和最长游程等统计量的后验分布。在解码方面，提出混合解码（hybrid decoding）方法，结合 Viterbi 与 Posterior 解码，并引入一种新的调参过程；同时给出混合损失函数基于加权几何均值的另一种推导。在多个经典数据集上演示了 FMCI 与混合解码的性能，并附有可复现代码。对您而言，本文属于统计计算方向，其 FMCI 与混合解码思想可迁移至您熟悉的隐马尔可夫或纵向数据建模场景，但方法学新颖度有限。
- **关键技术**: `finite Markov chain imbedding`, `hybrid decoding`, `Viterbi decoding`, `posterior decoding`, `weighted geometric mean`
- **为什么对您有用**: 本文属于统计计算方向，与您的 statistical computing 兴趣直接相关；FMCI 方法涉及状态空间构造与矩阵运算，可联系您熟悉的软件开发和数值方法；混合解码的调参问题可作为中期可做的切入点，但需先熟悉 HMM 解码的细节。

## 其他  *(other, 4 篇)*

### 1. [10.1111/sjos.70099](https://doi.org/10.1111/sjos.70099) · [arXiv](https://arxiv.org/abs/2510.22709) — Sample Size Determination for Win Statistics in Cluster‐Randomized Trials
- **作者**: Xi Fang, Zhiqiang Cao, Fan Li
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Medical College of Wisconsin · Shenzhen Technology University · Yale University
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对集群随机试验（cluster-randomized trials）中复合终点（composite endpoints）的 win statistics（如 win ratio、win odds、win difference）提出了统一的功效与样本量计算框架。现有 win statistics 的推断方法主要针对个体随机试验，而集群随机试验中的功效分析缺乏正式框架，尤其对于复合时间-事件结局。作者推导了一类 win statistics 的解析方差表达式，得到闭式方差和功效公式，避免了计算密集型模拟。方差表达式显式刻画了秩内相关系数（rank intracluster correlation coefficient）、簇大小、平局概率和结局优先级对研究计划的影响。该方差公式将单变量结局的现有公式作为特例，并推广到复杂的分层有序复合终点。模拟研究验证了有限样本下的准确性，并通过案例研究展示了方法的应用。
- **关键技术**: `win statistics`, `cluster-randomized trials`, `sample size determination`, `rank intracluster correlation coefficient`, `closed-form variance`
- **为什么对您有用**: 本文属于应用统计方法学，涉及因果推断中的集群随机试验设计，与您的流行病学应用兴趣相关，但方法学新颖性有限。您的武器库（如非参数统计、U-统计量理论）足以理解其方差推导，但该问题并非您核心研究方向的直接延伸。作为流行病学应用的参考，可了解 win statistics 在集群设计中的处理，但暂不建议深入。

### 2. [10.1111/sjos.70100](https://doi.org/10.1111/sjos.70100) · [arXiv](https://arxiv.org/abs/2509.21827) — Sliced Space‐Filling Design With Mixtures
- **作者**: Zikang Xiong, Hong Qin, Yuning Huang, Jianhui Ning
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Zhongnan University of Economics and Law · Central China Normal University
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出一种基于分布函数切片代表点（sliced representative points）的新框架，用于构造混合成分的切片空间填充设计。通过能量距离分解，作者建立了全点集与其切片子集代表性之间的关系，并据此提出两种分别优先全集或子集代表性的构造方法。为平衡两个层面，进一步开发了混合能量距离准则及相应的一次性和序贯构造算法，并提供了配套的 R 包。作者还证明了三种方法生成的点集和子集的分布收敛性。数值结果表明，基于切片代表点的设计在空间填充性能和预测精度上均有显著提升。该工作属于实验设计领域，与您的主要兴趣（因果推断、高维统计、半参数理论等）无直接交集，但其中的能量距离分解和分布收敛性分析可能对您理解基于距离的统计方法有一定参考价值。
- **关键技术**: `sliced representative points`, `energy distance decomposition`, `space-filling design`, `mixture experiments`, `distributional convergence`
- **为什么对您有用**: 本文属于实验设计领域，与您的主要兴趣（因果推断、高维统计、半参数理论等）无直接交集，但其中的能量距离分解和分布收敛性分析可能对您理解基于距离的统计方法有一定参考价值。

### 3. [10.1111/sjos.70091](https://doi.org/10.1111/sjos.70091) — With‐Replacement Balanced Sampling
- **作者**: Jean Rubin, Guillaume Chauvet
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: École Nationale de la Statistique et de l'Analyse de l'Information · Institut de recherche mathématique de Rennes
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究有放回平衡抽样（with-replacement balanced sampling）问题，目标是在有放回抽样下使 Horvitz-Thompson 估计量能精确复现已知的辅助变量总量。作者基于 cube method 的推广，提出了三种新的有放回平衡抽样算法，并针对此类设计提出了方差近似公式。模拟研究评估了该方差近似在理想化条件多项抽样和所提算法下的准确性。此外，文章展示了如何利用这些方法构建单遍（single-pass）平衡流式抽样程序，在保持辅助变量平衡的同时确保期望样本量按规模成比例。该工作属于抽样调查领域，与您的主要兴趣（因果推断、高维统计等）无直接交集，但其中平衡抽样与方差近似的思想可能对调查加权或纵向数据中的抽样设计有间接参考价值。
- **关键技术**: `cube method`, `balanced sampling`, `Horvitz-Thompson estimator`, `variance approximation`, `stream sampling`
- **为什么对您有用**: 本文属于抽样调查方法，与您的主要兴趣（因果推断、高维统计、半参数理论）无直接重叠，但平衡抽样与方差近似在调查加权和纵向数据中可能有间接应用。作为 gateway reading，本文对统计学家而言入门门槛较低，但武器库（如高阶 U 统计、半参数理论）难以直接迁移，暂不可做。

### 4. [10.1111/sjos.70085](https://doi.org/10.1111/sjos.70085) — On Robustness of Pairwise Kalman Filters
- **作者**: M. Escudier, C. Fernandes, W. Pieczynski
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Institut Polytechnique de Paris · Télécom SudParis
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文研究高斯齐次马尔可夫成对模型（GH-PMM）下成对卡尔曼滤波器（PKF）的鲁棒性。目标是在模型参数与实际参数存在偏差时，快速且精确地顺序计算滤波器均方误差（MSE）的增量。作者推导了MSE增量的递推计算公式，避免了蒙特卡洛模拟，计算效率高。通过将真实GH-PMM替换为经典齐次高斯状态空间模型（GH-SSM）的数值实验，展示了滤波器性能的退化程度。最后，将该方法应用于通过温度序列滤波估计土壤湿度的真实问题。对您而言，该文属于统计计算与状态空间模型的应用，与您的主要兴趣（如统计计算）有间接关联，但方法学新颖性有限。
- **关键技术**: `Kalman filter`, `pairwise Markov models`, `robustness analysis`, `mean square error recursion`
- **为什么对您有用**: 本文属于统计计算与状态空间模型的应用，与您的主要兴趣（如统计计算）有间接关联，但方法学新颖性有限。作为入门读物，它展示了模型误设下滤波器性能的量化方法，但武器库中的工具（如U统计量、半参数理论）难以直接迁移。暂不可做，因为核心机器（状态空间模型鲁棒性分析）不在武器库中。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

