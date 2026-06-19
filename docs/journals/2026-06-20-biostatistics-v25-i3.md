# Biostatistics — Vol 25  Issue 3  ·  2026-06-20

- 共 19 篇 · Biostatistics
- 目录核对 ⚠️ 疑似漏 1 篇（对照 OpenAlex 20 篇）：10.1093/biostatistics/kxac050

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期论文主要围绕三条方法论主线展开：因果推断中的复杂结构与效率提升、非参数/半参数/函数型数据的灵活建模与降维、以及贝叶斯框架下的计算优化与信息借用。因果推断主线集中了七篇文献，覆盖中介分析、平衡权重、纵向干预、公平性、个性化治疗规则及试验缺失处理；非参数/半参数主线包含四篇，侧重时空函数型数据、核权重与贝叶斯非参过程；贝叶斯计算与借用主线则横跨五篇，处理大规模马尔可夫模型、多区域试验、低报修正及析因设计。

因果推断主线本期着重推进高维与非标准设定的识别及效率。高维中介分析有两篇不同切法：DP2LM用深度神经网络逼近非线性混杂并配合惩罚部分线性模型处理高维中介，而多中介贝叶斯非参方法则用EDPM混合模型对观测分布灵活建模以捕捉中介交互。在干预效应估计上，核平衡权重针对大规模观察性数据，将RKHS基展开与Nyström低秩近似结合，通过ADMM实现非参数平衡权重的快速求解；两阶段TMLE则针对集群随机试验中的子抽样与多重缺失，在少量独立单元下扩展了半参数效率框架；此外，高维离散结局下的个性化治疗规则采用了双重稳健正则化估计方程进行变量选择，反事实公平性将交叉群体引入因果风险预测度量，而贝叶斯多变量因子模型则用潜在结构提升时间序列混合结局的因果推断效率。

非参数/半参数与贝叶斯借用主线本期在纵向与空间异质性上发力明显。多元时空函数主成分分析通过Karhunen-Loéve展开与MCMC推断，降维刻画透析人群结局的时空依赖；贝叶斯非参低报修正用Dirichlet过程先验刻画计数数据报告概率的异质聚类；半监督混合多源可交换性模型（SS-MIX MEM）则通过修正倾向得分识别外部可交换子组，实现RCT与真实世界数据的安全贝叶斯借用。在计算层面，含协变量的连续时间马尔可夫模型用Padé逼近与SGD规避了昂贵的矩阵指数运算，多区域临床试验的联合建模则用Laplace方法积分掉随机效应以规避高维MCMC。

对因果推断与半参数效率方向的研究者，两阶段TMLE（处理试验缺失与依赖）与核平衡权重（非参数效率与大规模计算）最贴合核心理论；高维中介分析（DP2LM与EDPM）及双重稳健ITR变量选择则直接推进了高维因果设定的识别与推断，适合优先看。

## 因果推断  *(causal_inference, 8 篇)*

### 1. [10.1093/biostatistics/kxad038](https://doi.org/10.1093/biostatistics/kxad038) — A Bayesian nonparametric approach for multiple mediators with applications in mental health studies
- **作者**: Samrat Roy, Michael J Daniels, Jason Roy
- **期刊/来源**: Biostatistics
- **机构**: Indian Institute of Management Ahmedabad · University of Florida · Rutgers, The State University of New Jersey
- **分类**: vol 25 · issue 3 · pp 919-932
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在多中介因果推断设定下，目标为处理对结局的总效应中经由多个中介的联合/个体/交互中介效应的 identification 与估计。现有方法多依赖参数模型易受 misspecification 影响，且常将联合中介效应简单拆解为个体效应之和而忽略中介间交互。本文提出 Bayesian nonparametric 方法，用 enriched Dirichlet process mixture (EDPM) 三层模型对观测数据联合分布做灵活建模，再通过 g-computation (standardization) 计算所有中介效应组合（含 pairwise 及高阶交互）。模拟与 Wisconsin Longitudinal Study 精神健康数据应用表明，该方法能识别显著个体中介及 pairwise 交互效应。对您有用：本文在多中介设定下用非参数贝叶斯替代参数 g-formula，与您关注的 semiparametric / nonparametric 估计及 mediation identification 理论直接相关。
- **关键技术**: `Bayesian nonparametric mediation`, `enriched Dirichlet process mixture`, `g-computation (standardization)`, `multiple mediator interaction`, `natural indirect effect identification`
- **为什么对您有用**: 本文直接连接您 primary interest 中的 mediation 与 nonparametric theory 子方向：多中介交互效应的 identification 与非参数估计。您武器库中 semiparametric theory 与 M-estimation theory（moderately_familiar）可以攻这篇 paper 的一个口子：将 Bayesian EDPM 的 g-computation 替换为 semiparametric efficient influence function / one-step estimator，从而获得 n^{-1/2}-CAN 与 efficiency bound 的理论保证，而非仅靠后验收敛。Follow-up 粗判：**中期可做**——需先在 moderately_familiar 的 semiparametric theory 上长肌肉，具体是将 HOIF / semiparametric efficiency bound 工具移植到多中介交互效应的估计中。

### 2. [10.1093/biostatistics/kxad037](https://doi.org/10.1093/biostatistics/kxad037) — DP2LM: leveraging deep learning approach for estimation and hypothesis testing on mediation effects with high-dimensional mediators and complex confounders
- **作者**: Shuoyang Wang, Yuan Huang
- **期刊/来源**: Biostatistics
- **机构**: Yale University
- **分类**: vol 25 · issue 3 · pp 818-832
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在高维中介变量与复杂混杂的因果中介分析设定下，目标是对直接与间接中介效应进行估计与假设检验，核心假设为部分线性结构及混杂的非线性可由神经网络逼近。本文提出 DP2LM 方法：用深度神经网络拟合混杂的非线性效应，同时用 penalized partially linear model 处理高维中介变量，将中介效应的估计与推断置于变量选择之上。针对直接与间接效应，作者构造了相应的检验程序，理论上证明了检验在原假设下能严格控制 Type-I error rate。模拟显示该方法在大量中介变量与非线性混杂场景下优于现有方法，并在童年创伤人群 DNA 甲基化对皮质醇应激反应的中介效应流行病学数据中做了实证分析。对您可能有用：本文将 debiased / partial linear 思想引入高维中介推断，连接了因果中介与 semiparametric efficiency 两个子方向。
- **关键技术**: `penalized partially linear model`, `deep neural network nonparametric confounding adjustment`, `mediation effect hypothesis testing`, `high-dimensional mediator inference`, `Type-I error control`
- **为什么对您有用**: 本文直接连接因果中介推断与 semiparametric 部分线性模型两个子方向，处理了高维中介+非线性混杂这一常见但棘手的设定。从 technical_arsenal 看，您 very_familiar 的高维渐近与 estimation theory in causal inference 可直接审视其 Type-I error 控制与估计收敛率的紧致性，moderately_familiar 的 semiparametric theory 可用来检验其部分线性结构下是否触及 semiparametric efficiency bound。**中期可做**：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，具体是推导部分线性中介模型的 efficient influence function，以验证其估计是否达到效率下界或可进一步 debias。

### 3. [10.1093/biostatistics/kxad032](https://doi.org/10.1093/biostatistics/kxad032) · [arXiv](https://arxiv.org/abs/2311.00568) — Scalable kernel balancing weights in a nationwide observational study of hospital profit status and heart attack outcomes
- **作者**: Kwangho Kim, Bijan A Niknam, José R Zubizarreta
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 3 · pp 736-753
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在大规模观察性数据设定下，目标是估计医院盈利状态对心脏病发作结局的因果效应，需在非参数特征空间中实现协变量平衡与权重分散度最小化。本文提出一种可扩展的核平衡权重方法，将 RKHS 基展开与凸优化结合：利用 rank-restricted Nyström 方法在近线性时空内高效计算核基，再通过 ADMM 一阶算法快速求解最优权重。模拟表明该方法在准确度与速度上显著优于现有加权估计器。实证分析 127 万患者数据发现，营利性医院干预率相似但死亡与再入院率更高。对您有用：该方法的 Nyström 低秩近似与 ADMM 求解直接触及 stat_computing 与非参数平衡估计的交叉点。
- **关键技术**: `kernel balancing weights`, `rank-restricted Nyström method`, `reproducing kernel Hilbert space`, `alternating direction method of multipliers`, `covariate balancing weighting`, `convex optimization for causal inference`
- **为什么对您有用**: 直接连接因果推断的协变量平衡加权估计与 stat_computing 的大规模数值优化。您 very_familiar 的软件开发与高维渐近理论可以攻入其 Nyström 低秩近似的理论性质口子（如近似误差对平衡权重 estimator 的影响），而 moderately_familiar 的半参数理论可用于分析该 kernel weighting estimator 是否能达到 semiparametric efficiency bound。follow-up 判断：中期可做——需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以严格建立该 ADMM+Nyström 求解路径下 estimator 的 n^{-1/2}-CAN 与 influence function 性质。

### 4. [10.1093/biostatistics/kxad030](https://doi.org/10.1093/biostatistics/kxad030) — A Bayesian multivariate factor analysis model for causal inference using time-series observational data on mixed outcomes
- **作者**: Pantelis Samartsidis, Shaun R Seaman, Abbie Harrison, Angelos Alexopoulos, Gareth J Hughes, Christopher Rawlinson et al.
- **期刊/来源**: Biostatistics
- **机构**: MRC Biostatistics Unit · UK Health Security Agency · Athens University of Economics and Business
- **分类**: vol 25 · issue 3 · pp 867-884
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 该文针对时间序列观察数据中多单元和多结果（连续、二项、计数）的干预效应估计问题，提出一种贝叶斯多变量因子分析模型。通过引入潜在因子结构刻画单元间的异质性与结果间的相关性，联合建模混合类型结局变量，从而提高因果效应估计的效率。模型采用高效马尔可夫链蒙特卡洛算法对高维后验进行采样，并自然提供所有因果估计量的不确定性量化。该方法适用于纵向观察性因果推断场景，尤其在多个结局同时受干预影响时优势明显。文章以英格兰COVID-19检测追踪计划中地方追踪伙伴关系的效果评估为例，展示了模型的实际应用。该论文的贝叶斯框架与因果推断中潜在结果模型结合，对您关注的纵向因果推断和半参数效率理论之外的方法论扩展有参考价值，尤其适合流行病学应用场景。
- **关键技术**: `Bayesian factor analysis`, `MCMC sampling`, `multivariate mixed outcomes`, `time-series causal inference`, `uncertainty quantification`
- **为什么对您有用**: 该文直接对应您主要兴趣中的纵向因果推断（longitudinal）和次级兴趣中的流行病学应用（COVID-19真实数据）。武器库中'因果推断的估计理论'（very_familiar）可用于理解其效应估计逻辑，但贝叶斯因子分析和MCMC并非当前核心工具，属于暂不可做（需补充贝叶斯建模与计算能力）。不过，论文作为流行病学应用案例，能帮助您熟悉现实中多结局时间序列因果问题的分析模式，适合作为跨界阅读。

### 5. [10.1093/biostatistics/kxad015](https://doi.org/10.1093/biostatistics/kxad015) — Blurring cluster randomized trials and observational studies: Two-Stage TMLE for subsampling, missingness, and few independent units
- **作者**: Joshua R Nugent, Carina Marquez, Edwin D Charlebois, Rachel Abbott, Laura B Balzer
- **期刊/来源**: Biostatistics
- **机构**: Kaiser Permanente · San Francisco AIDS Foundation · University of California, Berkeley
- **分类**: vol 25 · issue 3 · pp 599-616
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 该论文针对集群随机试验（CRT）中普遍存在的三个缺失来源（子抽样、基线状态测量缺失、最终状态测量缺失）以及独立单元数较少的问题，提出了一种两阶段TMLE（Two-Stage Targeted Minimum Loss-Based Estimation）扩展方法。该方法在CRT的框架下，通过将集群内的子单元视为条件独立单位来改善精度和统计功效，但需要仔细评估该假设是否合理。论文基于SEARCH-TB试验（减少结核感染）进行应用，对比了不同假设下的估计结果：依赖不切实际假设的估计显示干预增加18%的感染风险（RR=1.18），而纳入抽样、缺失和社区内依赖的估计显示干预降低27%的风险（RR=0.73, 95% CI: 0.57–0.92），凸显了方法的重要性。这篇论文直接与您的因果推断（特别是TMLE、缺失数据、集群试验）和效率理论兴趣相连，提供了扩展TMLE处理实际复杂缺失模式的范例，且流行病学真实数据应用增加了其现实意义。
- **关键技术**: `targeted minimum loss-based estimation`, `Two-Stage TMLE`, `cluster randomized trials`, `subsampling`, `missing data`, `conditional independence assumption`
- **为什么对您有用**: 该论文直接针对因果推断中的集群随机试验和缺失数据处理问题，扩展了您熟悉的TMLE方法，与您的primary interest（causal inference, efficiency theory）高度契合。您可以使用semiparametric理论和M-estimation知识来审视其估计的稳健性，并考虑将类似的two-stage TMLE框架推广到您的proximal causal inference或IV设定中。此外，SEARCH-TB应用属于流行病学领域（secondary interest），提供了真实数据分析的完整流程。从武器库角度看，您对TMLE（very_familiar中的'estimation theory in causal inference'）和semiparametric theory（moderately_familiar）已足够理解本文，适合立即可做：您可以直接复现其分析逻辑，或将其与您的高阶U统计量结合处理更复杂的依赖结构。

### 6. [10.1093/biostatistics/kxad021](https://doi.org/10.1093/biostatistics/kxad021) · [arXiv](https://arxiv.org/abs/2210.01194) — An intersectional framework for counterfactual fairness in risk prediction
- **作者**: Solvejg Wastvedt, Jared D Huling, Julian Wolfson
- **期刊/来源**: Biostatistics
- **机构**: University of Minnesota
- **分类**: vol 25 · issue 3 · pp 702-717
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在反事实公平性框架下，本文针对健康政策中的风险预测模型，定义了考虑多重交叉群体（intersectional groups）的新型不公平度量（unfairness metrics），目标 estimand 为个体在反事实世界（无歧视特征）下的风险差异。核心方法结合了反事实因果推断与交叉性分析，提出了 unfairness value（u-value）以量化不公平的相对极端程度，并构建了完整的估计与推断工具，包括标准误差和置信区间，推断部分采用了替代标准 bootstrap 的方法以应对小样本/稀疏交叉群组下的统计问题。理论贡献在于将反事实公平性从单一群体扩展到多重交叉群体，并解决了临床风险预测中因治疗引导（treatment guidance）而导致的现有公平性技术失效问题。实证部分将框架应用于中西部大型医疗系统的 COVID-19 风险预测模型。对您可能有用：本文将反事实因果推断与交叉性公平性结合，其推断工具的开发思路可借鉴至因果敏感性分析或纵向因果推断中的稀疏子群推断问题。
- **关键技术**: `counterfactual fairness`, `intersectional group analysis`, `u-value for unfairness extremity`, `alternative bootstrap inference`, `risk prediction under treatment guidance`
- **为什么对您有用**: 本文直接连接因果推断中的反事实公平性设定，属于因果 identification 与 estimation 在算法公平性中的应用。您武器库中 very_familiar 的因果推断估计理论及 moderately_familiar 的 identification theory 可直接切入本文 estimand 的 identification 假设检验与推断方法的改进（例如用 HOIF 或 semiparametric efficiency 替代其 bootstrap 推断）。follow-up 判断：**中期可做**——需先在 moderately_familiar 的 identification theory 上长肌肉，以严格审视其多重交叉反事实 identification 的可检验性，并探索更高效的 semiparametric 推断方法。

### 7. [10.1093/biostatistics/kxad022](https://doi.org/10.1093/biostatistics/kxad022) — Variable selection in high dimensions for discrete-outcome individualized treatment rules: Reducing severity of depression symptoms
- **作者**: Erica E M Moodie, Zeyu Bian, Janie Coulombe, Yi Lian, Archer Y Yang, Susan M Shortreed
- **期刊/来源**: Biostatistics
- **机构**: McGill University · Université de Montréal · Kaiser Permanente Washington Health Research Institute · University of Washington
- **分类**: vol 25 · issue 3 · pp 633-647
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文研究高维离散结局（二值结果）下个性化治疗规则（ITR）的变量选择问题，目标是从观察性数据中识别影响治疗决策的协变量，以降低抑郁症严重程度。采用双重稳健（doubly robust）正则化估计方程的新计算方法，结合加权和惩罚估计方程，在非线性联系函数下实现变量选择。方法在Kaiser Permanente Washington的抑郁症患者队列中验证，展示了双重稳健性和变量选择的有效性。该方法相比传统方法更有效地处理二值结果下的稀疏性和模型误设问题。对您而言，本文展示了因果推断中ITR估计与高维变量选择的实际应用，特别是使用流行病学数据集，与其估计理论和高维统计兴趣直接相关。
- **关键技术**: `doubly robust estimation`, `penalized estimating equations`, `individualized treatment rules`, `variable selection`, `weighted estimating equations`
- **为什么对您有用**: 本文聚焦于因果推断中的个性化治疗规则变量选择，采用双重稳健估计方程，属于您非常熟悉的估计理论在因果推断中的应用。武器库中'estimation theory in causal inference'和'high-dimensional asymptotics'可直接用于理解并复现该方法。数据来自流行病学队列，可作为应用案例快速上手。若需扩展到多值治疗或连续结局，可结合您中度熟悉的半参数理论进一步开发。总体立即可做，因为核心工具已掌握。

### 8. [10.1093/biostatistics/kxad024](https://doi.org/10.1093/biostatistics/kxad024) — Semi-supervised mixture multi-source exchangeability model for leveraging real-world data in clinical trials
- **作者**: Lillian M F Haine, Thomas A Murry, Raquel Nahra, Giota Touloumi, Eduardo Fernández-Cruz, Kathy Petoumenos et al.
- **期刊/来源**: Biostatistics
- **机构**: University of Minnesota · Cooper University Hospital · Cooper Medical School of Rowan University · National and Kapodistrian University of Athens · Hospital General Universitario Gregorio Marañón · UNSW Sydney
- **分类**: vol 25 · issue 3 · pp 617-632
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出一种半监督混合多源可交换性模型（SS-MIX MEM），用于在随机对照试验（RCT）中借用真实世界数据（RWD）以提高统计效率。目标是在保持试验内部有效性的前提下，从外部观测数据库（RWD）中识别出与试验人群可交换的子组，从而安全地借用信息。方法分两步：第一步通过修正倾向得分的半监督混合模型（SS-MIX）将RWD个体分类为与试验人群代表性高的子组；第二步基于多源可交换性模型（MEM）进行贝叶斯分层借用，仅在RWD子组与试验组结果分布一致时大量借用，否则收缩至不借用。模拟研究表明，当RWD与RCT一致时该方法能有效借用并降低方差；当存在测量或未测量混杂时能自动缓解偏倚。通过一项静脉注射高免疫免疫球蛋白治疗流感住院患者的RCT实例，展示了该方法在流感亚组分析中利用外部观测数据补充样本的应用。本文连接因果推断中利用外部数据进行识别和估计的问题，尤其涉及倾向得分和不完全可交换性下的灵敏度分析，对您在因果推断和半参数估计方面的经验有直接参考价值。
- **关键技术**: `semi-supervised mixture model`, `multi-source exchangeability model`, `propensity score`, `Bayesian borrowing`, `subgroup analysis`, `RWD integration`
- **为什么对您有用**: 本文直接关联您primary interests中因果推断在临床试验中的实际应用，特别是利用外部数据放宽可交换性假设的新识别策略。您very_familiar的“estimation theory in causal inference”和“nonparametric statistics”可以立即用来评估该方法的识别假设是否可检验、以及能否构造频率主义版本以提高效率。目前可做的是用您的估计理论框架重新审视其偏差-方差权衡，并探讨与双重稳健估计的联系。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1093/biostatistics/kxad013](https://doi.org/10.1093/biostatistics/kxad013) — Multivariate spatiotemporal functional principal component analysis for modeling hospitalization and mortality rates in the dialysis population
- **作者**: Qi Qian, Danh V Nguyen, Donatello Telesca, Esra Kurum, Connie M Rhee, Sudipto Banerjee et al.
- **期刊/来源**: Biostatistics
- **机构**: University of California, Los Angeles · University of California, Irvine · University of California, Riverside
- **分类**: vol 25 · issue 3 · pp 718-735
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 针对美国透析患者住院率与死亡率这两个相关结局，基于USRDS全国数据提出多元时空函数主成分分析模型，用以刻画时间动态与空间相关的联合模式。模型采用多元Karhunen-Loéve展开，将各区域随时间变化的曲线分解为主成分得分，并通过得分间的空间协方差矩阵引入空间依赖性。估计策略先对每个结局单独做单变量函数主成分分解，然后利用MCMC框架对空间相关性参数进行贝叶斯推断，避免直接处理高维多元协方差。模拟实验显示该方法在有限样本下能有效恢复主成分函数和空间相关结构。实际应用识别出美国境内住院率和死亡率的热点区域及高风险时间段，为透析患者的资源分配提供依据。对您而言，本文展示了函数型数据分析在流行病学多结局时空建模中的运用，其分解思路可与您熟悉的非参数统计中smoothing方法结合，也可作为统计计算中MCMC与PCA混合算法的练习案例。
- **关键技术**: `multivariate functional PCA`, `Karhunen–Loéve expansion`, `MCMC for spatial correlation`, `univariate PCA decomposition`, `spatiotemporal modeling`
- **为什么对您有用**: 本文属于流行病学与统计方法的交叉：用函数型主成分分析研究透析人群健康结局的时空模式，正好对接您的secondary interest（流行病学中的真实数据应用）。您可用very_familiar中的‘nonparametric statistics’审视其主成分函数的平滑性假设是否合理，或用‘software development’复现其估计流程并测试不同空间先验的敏感性。由于您对MCMC和条件自回归空间模型不熟悉，该方向当前暂不可做，核心缺口为空间统计建模与贝叶斯计算。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1093/biostatistics/kxad012](https://doi.org/10.1093/biostatistics/kxad012) — A scalable approach for continuous time Markov models with covariates
- **作者**: Farhad Hatami, Alex Ocampo, Gordon Graham, Thomas E Nichols, Habib Ganjgahi
- **期刊/来源**: Biostatistics
- **机构**: University of Oxford · Novartis (Switzerland) · Wellcome Centre for Integrative Neuroimaging
- **分类**: vol 25 · issue 3 · pp 681-701
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对含协变量的连续时间马尔可夫模型（CTMM）在大规模数据下面临的计算瓶颈——每个观测都需要计算矩阵指数，提出一种可扩展的优化方法。该方法采用随机梯度下降（SGD）算法，并结合Padé逼近对矩阵指数求导，从而避免了对每个样本单独进行昂贵的矩阵指数运算。作者还给出了两种标准误差计算方式：一种基于Padé展开，另一种基于幂级数展开，为不确定性量化提供了实用工具。模拟实验表明，新方法在保持估计精度的同时大幅降低了计算成本，在大型多发性硬化症（NO.MS）数据集上展示了可行性。该工作直接服务于统计计算中矩阵指数的高效近似和SGD在连续时间模型中的应用，对您而言可借助已有的软件开发经验和高维渐近知识来理解其收敛性分析，属于立即可做的技术复现或扩展方向。
- **关键技术**: `stochastic gradient descent`, `Padé approximation for matrix exponential`, `continuous time Markov model (CTMM)`, `large-scale optimization`, `standard error via Padé/power series expansion`
- **为什么对您有用**: 本文直接对接您的统计计算兴趣，尤其是大规模模型中的矩阵运算优化。您非常熟悉的软件开发经验和逆问题的误差分析能力可立即用于复现或改进该Padé-SGD算法；同时，高维渐近中处理随机矩阵的技巧也可帮助分析SGD的收敛行为。立即可做：利用现有武器（逆问题、高维渐近、软件）即可动手复现或扩展至自己的CTMM应用。

## 流行病学  *(epidemiology, 5 篇)*

### 1. [10.1093/biostatistics/kxad036](https://doi.org/10.1093/biostatistics/kxad036) — Uncertainty directed factorial clinical trials
- **作者**: Gopal Kotecha, Steffen Ventz, Sandra Fortini, Lorenzo Trippa
- **期刊/来源**: Biostatistics
- **机构**: Harvard University · Dana-Farber Cancer Institute · University of Minnesota · Bocconi University
- **分类**: vol 25 · issue 3 · pp 833-851
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对析因临床试验中多数采用平衡随机化而忽视试验目标的局限，提出了一类贝叶斯响应自适应设计。该方法基于决策理论，允许研究者指定与试验目标对应的效用函数，利用已有数据在入组期间动态调整各治疗组合的随机化概率，以最大化期望效用。核心机制是通过后验分布和贝叶斯准则构造自适应随机化算法，并建立了算法的渐近性质。作者还以三项近期析因试验（围手术期护理、戒烟、传染病预防）的真实数据构建模拟场景，对比了不同效用函数下设计的操作特征，展示了自适应设计的优势。本文为贝叶斯自适应设计在析因试验中的系统应用提供了理论框架和实用指导。您研究组在流行病学方面有 secondary interest，本文的模拟框架和设计思路可直接借鉴，同时您熟悉的统计计算和软件开发技能可以快速复现和扩展这类自适应随机化算法。
- **关键技术**: `Bayesian decision-theoretic design`, `response-adaptive randomization`, `utility function`, `factorial clinical trials`, `binary outcomes`
- **为什么对您有用**: 1. 本文属于流行病学的重要应用领域——临床试验设计，您对 epidemiology 有 secondary interest，可作为进入该方向的入口阅读。2. 您非常熟悉的软件开发技能可用于实现此类自适应随机化算法，并可扩展到更复杂的因果结构（如序贯处理）。3. 立即可做：基于本文算法，您可以直接构建 R/Stan 包实现贝叶斯自适应析因设计，并用真实数据验证。

### 2. [10.1093/biostatistics/kxad027](https://doi.org/10.1093/biostatistics/kxad027) — A Bayesian nonparametric approach to correct for underreporting in count data
- **作者**: Serena Arima, Silvia Polettini, Giuseppe Pasculli, Loreto Gesualdo, Francesco Pesce, Deni-Aldo Procaccini
- **期刊/来源**: Biostatistics
- **机构**: University of Salento · Sapienza University of Rome · Azienda Universitaria Ospedaliera Consorziale - Policlinico Bari · Fatebenefratelli Hospital
- **分类**: vol 25 · issue 3 · pp 904-918
- 相关性 5/10 · novelty: `application`
- **摘要**: 在流行病学计数数据存在低报（underreporting）的设定下，目标是修正低报偏差以估计真实患病率；假设观测计数服从复合 Poisson 模型，且报告概率通过潜在聚类结构（latent clustering）分层。核心机制为 Bayesian nonparametric 方法：对报告概率引入 Dirichlet process 或类似非参先验以刻画异质性，并结合专家意见与代理变量（proxy）对报告过程进行部分校准。模拟与真实数据（意大利 Apulia 地区慢性肾病 m=258 个市镇的多源登记数据，以及巴西早期新生儿死亡率数据）显示，当具备关于数据质量的部分信息时，该方法比现有低报修正模型更准确。对您可能有用：该文提供了一个将 Bayesian nonparametric 聚类与流行病学低报修正结合的完整应用案例，适合作为理解计数数据低报问题的入门阅读。
- **关键技术**: `compound Poisson model`, `Bayesian nonparametric clustering`, `Dirichlet process prior`, `underreporting correction`, `expert elicitation`, `proxy variable calibration`
- **为什么对您有用**: (1) 本文属于流行病学应用，直接对应 secondary interest 中的 epidemiology 数据集与因果/修正推断，处理的是计数数据低报这一经典测量误差问题。(2) 武器库中的 nonparametric statistics 与 M-estimation theory 可以用来审视其非参先验的收敛性质与聚类结构的 identifiability，但本文是纯 Bayesian 框架，与您熟悉的 frequentist minimax / semiparametric efficiency 视角差异较大。(3) 作为 gateway reading：本文对低报机制的建模（compound Poisson + 聚类报告概率）写得较为清晰，适合了解流行病学计数数据的结构；但方法论 novelty 对您而言有限（novelty_flag = application），不值得花时间深读理论细节，快速浏览数据结构与低报设定即可。

### 3. [10.1093/biostatistics/kxad028](https://doi.org/10.1093/biostatistics/kxad028) — Joint modeling in presence of informative censoring on the retrospective time scale with application to palliative care research
- **作者**: Quran Wu, Michael Daniels, Areej El-Jawahri, Marie Bakitas, Zhigang Li
- **期刊/来源**: Biostatistics
- **机构**: University of Florida · Massachusetts General Hospital · University of Alabama at Birmingham
- **分类**: vol 25 · issue 3 · pp 754-768
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对姑息治疗研究中回顾时间尺度上生活质量纵向数据的建模问题，提出一种新的联合模型以处理信息删失导致的估计偏差。模型包含两个子模型：纵向子模型采用线性混合效应模型，生存子模型采用竞争风险模型同时建模死亡时间和脱落时间，两者通过一组共享的随机效应建立关联。该结构允许删失时间依赖于生活质量和生存，放宽了传统联合模型的独立删失假设。参数通过最大似然估计，仿真表明方法在信息删失下提供无偏估计，优于忽略信息删失的现有方法。真实数据（姑息治疗临床试验）展示了可行性与临床解释价值。该方法对您在流行病学领域处理删失纵向数据具有借鉴意义，尤其与您对缺失数据机制的因果推断理解相连。
- **关键技术**: `joint modeling`, `linear mixed effects model`, `competing risks model`, `informative censoring`, `shared random effects`, `retrospective time scale`
- **为什么对您有用**: 本文属于流行病学应用，可作为入门读物：摘要和引言清晰，对熟悉生存分析基础的统计学家友好。您的武器库中M估计与半参理论可帮助理解模型识别与估计性质，但纵向数据和竞争风险模型的具体计算（EM算法、数值积分）需额外学习。若希望拓展流行病学应用并了解联合建模实践，值得一读；若仅关注理论创新，价值有限。

### 4. [10.1093/biostatistics/kxad023](https://doi.org/10.1093/biostatistics/kxad023) — Bayesian joint models for multi-regional clinical trials
- **作者**: Nathan W Bean, Joseph G Ibrahim, Matthew A Psioda
- **期刊/来源**: Biostatistics
- **机构**: University of North Carolina at Chapel Hill
- **分类**: vol 25 · issue 3 · pp 852-866
- 相关性 3/10 · novelty: `application`
- **摘要**: 在多区域临床试验（MRCT）设定下，目标是当区域样本量较小时，通过跨区域信息借用来提高全局治疗效应的检验功效。本文将 Bayesian joint modeling（纵向数据与生存数据联合建模）引入 MRCT 框架，利用 Bayesian model averaging 实现区域间参数的先验信息共享。技术核心是用 Laplace's method 积分掉个体随机效应并近似区域特异治疗效应的后验分布，避免了高维 MCMC 的计算负担。模拟表明，相较于仅分析生存数据的方法，该联合建模方法在全局治疗效应检验的拒绝率上有明显提升，并在一个心血管 MRCT 数据集上做了实证分析。对您而言，本文提供了一个流行病学/临床试验场景下 joint model 与 Bayesian model averaging 的应用案例，可作为了解 MRCT 信息借用机制的入门读物。
- **关键技术**: `Bayesian joint model`, `Bayesian model averaging`, `Laplace approximation for random effects`, `multi-regional clinical trial`, `information borrowing across regions`
- **为什么对您有用**: 本文属于流行病学/临床试验的应用与方法交叉，连接到您 secondary interest 中 epidemiology 的 applied causal work 与数据集。从 technical_arsenal 看，您 very_familiar 的 software development 与 high-dimensional asymptotics 可以用来审视其 Laplace approximation 在高维随机效应下的数值稳定性与精度边界。作为 gateway reading，本文对 MRCT 信息借用机制的阐述较为清晰，但方法学 novelty 属于已有工具（joint model + BMA）的新组合应用，理论深度有限；值得花时间读摘要与模拟设计部分，但全文精读优先级不高。

### 5. [10.1093/biostatistics/kxad020](https://doi.org/10.1093/biostatistics/kxad020) — An integrative latent class model of heterogeneous data modalities for diagnosing kidney obstruction
- **作者**: Jeong Hoon Jang, Changgee Chang, Amita K Manatunga, Andrew T Taylor, Qi Long
- **期刊/来源**: Biostatistics
- **机构**: Yonsei University · Indiana University School of Medicine · Indiana University – Purdue University Indianapolis · Emory University · University of Pennsylvania
- **分类**: vol 25 · issue 3 · pp 769-785
- 相关性 3/10 · novelty: `application`
- **摘要**: 在肾梗阻诊断缺乏金标准的设定下，目标是利用异质性多模态数据（肾功能曲线、有序专家评分、药代动力学变量、人口学信息）对潜在梗阻状态进行识别与预测。本文提出整合潜类别模型，将三类子模型（多水平功能潜因子回归、probit scalar-on-function 回归、高斯混合）分别适配不同数据模态，并以潜在梗阻类别为锚点耦合。估计与推断依赖 MCMC 算法完成后验采样，从而给出梗阻预测及不确定性量化。模拟与 Emory 肾研究数据验证了该 CAD 工具的实用性。对您而言，本文提供了一个流行病学/医学诊断中无金标准下多模态潜类别建模的完整应用案例。
- **关键技术**: `integrative latent class model`, `multilevel functional latent factor regression`, `probit scalar-on-function regression`, `Gaussian mixture model`, `MCMC posterior sampling`, `no gold standard diagnosis`
- **为什么对您有用**: 本文属于流行病学（医学诊断）应用，核心是无金标准下多模态数据的潜类别建模，与您 primary interest 中的因果推断 identification（无金标准即 latent class identification）有概念对接。用您武器库中 moderately_familiar 的 M-estimation / identification theory 可以审视该模型参数的可识别性条件是否被充分论证。follow-up 判断：**中期可做**——需先在 moderately_familiar 的 semiparametric theory 上长肌肉，才能将此处的 MCMC 全贝叶斯推断替换为频率派的 semiparametric efficient estimator 并给出效率界；作为应用案例，值得花时间读全文以了解无金标准诊断的数据结构。

## 其他  *(other, 4 篇)*

### 1. [10.1093/biostatistics/kxad034](https://doi.org/10.1093/biostatistics/kxad034) — Covariate-guided Bayesian mixture of spline experts for the analysis of multivariate high-density longitudinal data
- **作者**: Haoyi Fu, Lu Tang, Ori Rosen, Alison E Hipwell, Theodore J Huppert, Robert T Krafty
- **期刊/来源**: Biostatistics
- **机构**: University of Pittsburgh · The University of Texas at El Paso · Emory University
- **分类**: vol 25 · issue 3 · pp 666-680
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出协变量引导的贝叶斯混合样条专家模型，用于分析多变量高密度纵向数据，如脑功能成像序列。模型假设每个个体的多变量轨迹来自多个潜在组分的混合，每个组分由平滑样条刻画，且混合权重通过逻辑模型与时间无关的协变量关联。采用完全贝叶斯框架通过Gibbs采样进行后验推断，组分数目由偏差信息准则（DIC）选择。模拟研究表明该方法在聚类准确性和轨迹拟合上优于现有方法。应用于功能近红外光谱（fNIRS）数据，揭示婴儿情绪反应与压力恢复过程中的不同脑活动模式，并发现这些模式与母亲抑郁症状等协变量的关联。对您的价值：该方法虽不涉及因果推断核心工具，但其纵向聚类与协变量关联的框架适用于流行病学队列研究中异质性轨迹的识别，可作为您进入流行病学应用领域的入门参考。
- **关键技术**: `Bayesian mixture of experts`, `smoothing splines`, `multivariate longitudinal data`, `Gibbs sampling`, `deviance information criterion`
- **为什么对您有用**: 本文属于流行病学应用（fNIRS数据），与您的secondary interest方向对应，可作为流行病学异质性纵向数据分析的方法参考。您的武器库中非参统计和估计理论（very familiar）可直接用于理解其样条建模框架；中期可尝试将混合专家模型与因果推断中的g-formula结合，但当前方法未涉及因果识别，需先补充纵向因果推断工具。本文是流行病学领域的gateway阅读，方法学新颖性一般，但应用场景清晰，值得浅读。

### 2. [10.1093/biostatistics/kxad010](https://doi.org/10.1093/biostatistics/kxad010) — Quantification and statistical modeling of droplet-based single-nucleus RNA-sequencing data
- **作者**: Albert Kuo, Kasper D Hansen, Stephanie C Hicks
- **期刊/来源**: Biostatistics
- **机构**: Johns Hopkins University
- **分类**: vol 25 · issue 3 · pp 801-817
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文研究 droplet-based 单核 RNA-seq (snRNA-seq) 数据的概率分布设定，核心 estimand 是 snRNA-seq 计数数据的分布族是否与已证实的 scRNA-seq（非 zero-inflated）一致。利用小鼠 cortex (10x Chromium) 与 kidney (DropSeq) 的 pseudonegative control 数据，通过拟合与检验确认 snRNA-seq 计数服从负二项分布 (negative binomial)，表明 scRNA-seq 的参数模型可直接迁移。此外，作者发现从 scRNA-seq 迁移到 snRNA-seq 时的 quantification mapping 策略（是否包含 intronic regions）显著影响 library size 与 cell type 分类，并确认了 snRNA-seq 中 exonic 与 intronic reads 均存在 gene length bias。主要实证结论是 snRNA-seq 的分布性质与 quantification 规范化选择对下游推断至关重要；对您而言，本文是典型的生物统计应用，方法学 novelty 有限。
- **关键技术**: `negative binomial distribution fitting`, `pseudonegative control`, `droplet-based snRNA-seq quantification`, `gene length bias assessment`, `zero-inflation testing`
- **为什么对您有用**: 本文属于生物统计应用，与您 primary interests（因果推断、高维/效率理论、U-statistics）无直接技术交集，亦非您关注的 astrostats/econ/epi 应用领域。方法学 novelty 仅为分布拟合验证（novelty_flag=application），武器库中的 minimax bounds / HOIF / semiparametric theory 均无攻入口子。作为 gateway reading 价值低：数据结构（单细胞计数矩阵）虽属高维，但本文未触及高维推断或计算-统计权衡问题。不建议花时间读全文。

### 3. [10.1093/biostatistics/kxad025](https://doi.org/10.1093/biostatistics/kxad025) — Analyzing microbial evolution through gene and genome phylogenies
- **作者**: Sarah Teichman, Michael D Lee, Amy D Willis
- **期刊/来源**: Biostatistics
- **机构**: University of Washington · Ames Research Center · Blue Marble Space · Blue Marble Space Institute of Science
- **分类**: vol 25 · issue 3 · pp 786-800
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究微生物基因组进化中基因水平进化历史异质性的可视化与交互分析问题，estimand 为一组基因系统发育树的低维欧氏空间投影与离群树识别。核心方法将估计的基因树视为数据对象，利用系统发育树空间的局部线性近似（基于 Billera-Holmes-Vogtmann 空间的 geodesic / tangent 分解），将高维非欧树数据映射为低维欧氏点，并修正了既有方法在处理零长度分支与多叉树时的实际局限。理论性质侧重几何近似与算法实现，未涉及 minimax rate 或 semiparametric efficiency bound；实证部分通过 Prevotella 菌株离群基因历史识别与 Streptococcus 不同基因集系统发育对比展示方法效用。对您而言，本文的树空间局部线性近似与 R 软件实现可作为非参数统计中 manifold / tree-valued data 可视化的参考案例，但与因果推断或高维推断的核心理论关联较弱。
- **关键技术**: `BHV tree space geometry`, `local linear approximation of tree space`, `tangent space projection`, `phylogenetic tree visualization`, `outlier tree detection`
- **为什么对您有用**: 本文属于非参数/统计计算边缘交叉（tree-valued data 的 manifold 近似与可视化），与您 primary interest 中的非参数统计和统计计算有弱连接，但核心 estimand（基因树离群检测）与因果/高维/效率理论无直接交集。武器库中 very_familiar 的非参数统计与软件开发足以理解其 tangent space 近似机制与 R 包实现，但无需动用 minimax 或 HOIF 工具。follow-up 判断：**暂不可做**——若想深入 tree-valued data 的 minimax 估计或 inference，当前武器库缺 tree space 上的概率极限理论（如 BHV 空间上的 Brownian motion / Fréchet mean asymptotics），需先补齐 metric geometry 与 tree-valued diffusion 的数学基础。

### 4. [10.1093/biostatistics/kxad026](https://doi.org/10.1093/biostatistics/kxad026) · [arXiv](https://arxiv.org/abs/2209.07585) — Improved fMRI-based pain prediction using Bayesian group-wise functional registration
- **作者**: Guoqing Wang, Abhirup Datta, Martin A Lindquist
- **期刊/来源**: Biostatistics
- **分类**: vol 25 · issue 3 · pp 885-903
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文在 fMRI 神经影像预测框架下，解决标准解剖对齐后仍存在的功能拓扑跨个体错位问题，目标 estimand 为跨受试者的疼痛评分预测精度。核心提出一种 Bayesian group-wise functional registration 方法，将各受试者功能数据空间变换至公共 latent template；利用 generalized Bayes 框架与对称损失函数实现具有 inverse-consistency 的概率配准，并用 Gaussian process 建模 latent template 以捕捉空间特征。模拟与热痛 fMRI 实证表明，该方法相比传统配准提升了疼痛评分的预测准确度。对您而言，本文的 GP 建模与 inverse-consistency 概率配准机制可作为统计计算与逆问题随机噪声处理的参考案例，但方法学 novelty 偏应用层面。
- **关键技术**: `Bayesian group-wise registration`, `Gaussian process prior`, `inverse-consistent probabilistic registration`, `generalized Bayes framework`, `multivariate brain predictive model`
- **为什么对您有用**: 本文属于神经影像应用统计，与您 primary/secondary interests 的因果推断、高维 RMT、流行病学等方向无直接交集。从 gateway-reading 视角看，它不是好的入门读物（fMRI 配准领域术语密集，对圈外人不够 accessible），且底层统计模型（GP prior + generalized Bayes loss）虽清晰但未触及您关心的 efficiency 或 minimax 理论。您的武器库（逆问题随机噪声、软件开发）足以支撑读懂其算法实现，但缺乏跟进的动力——核心问题（功能拓扑错位）不在您的研究版图内。不值得花时间读全文。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

