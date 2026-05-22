# Statistica Sinica  ·  2026-05-21

- 共 156 篇 · Statistica Sinica

## 因果推断  *(causal_inference, 15 篇)*

### 1. [10.5705/ss.202025.0104](https://doi.org/10.5705/ss.202025.0104) — Efficient Estimation of Average Treatment Effects with Unmeasured Confounding and Proxies
- **作者**: Chunrong Ai, Jiawei Shan
- **期刊/来源**: Statistica Sinica
- 相关性 10/10 · novelty: `new_theory`
- **摘要**: 在 proximal causal inference 框架下，本文研究存在未测量混淆时 ATE 的有效估计问题，核心识别假设是存在满足积分方程的 bridge function。传统两步法（先估 bridge function 再代入 ATE）因积分方程估计困难和忽略步骤间相关性而损失效率。作者提出用递增矩约束（increasing moment restrictions）逼近积分方程，并对 bridge function 和 ATE 进行联合估计。在适当正则条件下，该估计量达到了半参数有效界，并提供了数据驱动的矩约束个数选择方法。模拟和 SUPPORT 研究的右心导管数据应用验证了方法实用性。该方法对您研究 proximal CI 的效率理论和半参数估计有直接参考价值。
- **关键技术**: `proximal causal inference`, `bridge function`, `increasing moment restrictions`, `semiparametric efficiency bound`, `joint GMM estimation`
- **为什么对您有用**: 直接推进了您 primary interest 中的 proximal CI 估计理论，通过联合估计与递增矩约束达到了半参数有效界，对研究 proximal 框架下的 efficiency theory 和半参数方法具有重要借鉴意义。

### 2. [10.5705/ss.202025.0066](https://doi.org/10.5705/ss.202025.0066) — Semiparametric Principal Stratification Analysis Beyond Monotonicity
- **作者**: Jiaqi Tong, Brennan Kahan, Michael O. Harhay, Fan Li
- **期刊/来源**: Statistica Sinica
- 相关性 10/10 · novelty: `new_method`
- **摘要**: 在 principal stratification 框架下，针对 intercurrent events 定义局部平均处理效应 estimand，放松传统的单调性与反事实中间变量独立性假设。引入 margin-free 的条件优势比（conditional odds ratio）作为敏感性参数，在 principal ignorability 下推导出非参数识别公式。提出两类高效估计方法：条件双重稳健（conditionally doubly robust）参数估计器与基于 data-adaptive nuisance learners 的 debiased ML 估计器。模拟表明错误假设单调性常导致偏误推断，而单调性成立时错误假设非单调性仍近似有效；应用于重症监护试验（单调性不成立的场景）。对您在 causal inference 的敏感性分析及 efficiency theory 的 debiased ML 估计方向有直接借鉴价值。
- **关键技术**: `principal stratification`, `conditional odds ratio sensitivity parameter`, `principal ignorability`, `conditionally doubly robust estimation`, `debiased machine learning`, `nonparametric identification`
- **为什么对您有用**: 直接推进因果推断中 principal stratification 的半参数效率理论与敏感性分析，放松单调性假设并提供 debiased ML 估计器，对您在 causal inference（sensitivity analysis / identification）和 efficiency theory（debiased ML / DR）方向的工作有直接迁移价值。

### 3. [10.5705/ss.202025.0476](https://doi.org/10.5705/ss.202025.0476) — Conformal Causal Inference for Cluster Randomized Trials: Model-robust Inference Without Asymptotic Approximations
- **作者**: Bingkai Wang, Fan Li, Mengxin Yu
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在整群随机试验（CRT）中，传统因果推断依赖簇数趋于无穷的渐近理论，本文提出一种无需渐近逼近的有限样本 conformal 因果推断框架。该框架不直接估计 ATE，而是构建反事实结果差异的预测区间，为同类群体提供决策工具。方法兼容任意工作结局模型（包括数据自适应 ML），且对模型误设具有鲁棒性。核心工具为 conformal prediction，结合高效计算算法，可处理群组、个体及协变量子群的推断目标。理论证明了有限样本覆盖性质与模型鲁棒性，仿真与慢性疼痛 CRT 实证进一步验证了方法表现。对您有用：将 conformal prediction 引入 CRT 因果推断，提供了有限样本下不依赖大样本渐近的推断新路径，且其与 ML 工作模型的兼容性对您在效率理论与半参数推断中考虑数据自适应方法有直接启发。
- **关键技术**: `conformal prediction`, `cluster randomized trials`, `finite-sample inference`, `counterfactual prediction interval`, `model-robustness`
- **为什么对您有用**: 直接连接您 primary interest 中的因果推断（CRT设定）与假设检验（有限样本 conformal inference），同时其允许 ML 工作模型的特性与您关注的 efficiency theory / debiased ML 思路有共通之处，实证部分也涉及流行病学数据。

### 4. [10.5705/ss.202023.0317](https://doi.org/10.5705/ss.202023.0317) — Statistical Inference for Local Granger Causality
- **作者**: Yan Liu, Masanobu Taniguchi, Hernando Ombao
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 本文在多元局部平稳过程设定下，研究局部 Granger 因果性的估计与检验问题，以捕捉非平稳时间序列中随时间演化的因果关系。该方法将局部 Granger 因果性在频域中表征，并基于局部 Whittle 似然对参数化时变谱密度矩阵进行估计。在正则条件下，作者证明了该估计量具有渐近多元正态性。进一步，构建了检验局部 Granger 因果性的统计量，并推导出其渐近分布为多元正态分布的二次型。仿真基于时变 VAR 模型验证了有限样本性质，实证分析揭示了脑信号的功能连接与金融数据的结构变化。对您有用：该文为非平稳纵向数据提供了严格的因果假设检验框架，其时变谱矩阵的局部似然推断方法可为您在纵向因果推断中的理论推导提供借鉴。
- **关键技术**: `local Whittle likelihood`, `time-varying spectral density matrix`, `locally stationary processes`, `asymptotic normality`, `quadratic form test statistic`, `Granger causality`
- **为什么对您有用**: 直接关联您在纵向因果推断与假设检验方面的兴趣；文中对时变因果参数的渐近正态性及二次型检验统计量的推导，为非平稳数据下的因果假设检验提供了严格的理论框架，且金融数据应用契合您的经济学次级兴趣。

### 5. [10.5705/ss.202025.0315](https://doi.org/10.5705/ss.202025.0315) — Balancing Covariates in Survey Experiments
- **作者**: Pengfei Tian, Jiyang Ren, Yingying Ma
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 在总体抽样调查实验（survey experiment）设定下，目标是 ATE 在有限样本协变量不平衡时的更优估计。作者提出分层拒绝抽样与重随机化（rerandomization）设计来增强协变量平衡性，并建立设计基（design-based）渐近理论：分层差均值估计量相合，且极限分布为正态与两个截断正态的卷积，该分布比现有实验设计下的极限分布更集中于真实 ATE。此外在分析阶段提出协变量调整方法进一步提升估计效率。数值实验验证了有限样本下效率提升。对您有用：该文的非标准极限分布推导与协变量调整效率增益直接关联您在 efficiency theory 与 design-based causal inference 方面的兴趣，截断正态卷积分布的刻画手法也可为 hypothesis testing 提供新视角。
- **关键技术**: `stratified rejective sampling`, `rerandomization design`, `design-based asymptotic theory`, `truncated normal convolution limit`, `covariate adjustment`, `difference-in-means estimator`
- **为什么对您有用**: 直接关联您 primary interest 中的 causal inference（ATE 的 design-based 估计）与 efficiency theory（协变量调整提升效率）；非标准极限分布（正态-截断正态卷积）的精确刻画对 mathematical statistics / hypothesis testing 也有方法论参考价值。

### 6. [10.5705/ss.202025.0331](https://doi.org/10.5705/ss.202025.0331) — Semiparametric Causal Discovery and Inference with Invalid Instruments
- **作者**: Jing Zou, Wei Li, Wei Lin
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在存在未观测混淆和潜在无效工具变量（IV）的设定下，本文研究部分线性结构方程模型（SEM）中的因果发现与推断问题。通过构造替代有效 IV（surrogate valid IVs），作者在半参数框架下实现了因果结构的识别，并提出了有限样本估计程序。理论上，该方法不仅能一致恢复因果图结构，其因果效应估计量具备渐近正态性，且在边恢复中实现了错误发现率（FDR）控制。仿真与阿尔茨海默病基因调控网络数据验证了方法的有效性。对您而言，该文在放宽 IV 有效性假设下结合半参数理论推导渐近正态性，直接推进了您关注的 IV 推断与半参数效率方向。
- **关键技术**: `partially linear SEM`, `invalid instrumental variables`, `surrogate valid IVs`, `asymptotic normality`, `false discovery rate control`, `causal discovery`
- **为什么对您有用**: 直接契合您在因果推断（IV 识别与估计）和半参数理论（渐近正态性）方面的核心兴趣；放宽 IV 有效性假设的半参数框架对处理实际混淆问题具有方法学迁移价值，且流行病学应用提供了真实数据集参考。

### 7. [10.5705/ss.202025.0168](https://doi.org/10.5705/ss.202025.0168) — Doubly Robust Estimation of Optimal Individual Treatment Regime in A Semi-supervised Framework
- **作者**: Xintong Li, Mengjiao Peng, Yong Zhou
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在半监督框架下，目标是利用大量无标签数据与少量标签数据估计最优个体化治疗方案（ITR），设定为 model-free 且 propensity score 可能未知。方法核心分两步：先用 single index kernel smoothing 对无标签数据进行灵活插补（高维协变量下仍有效），再通过直接优化插补后的 value function 确定最优 ITR。在观察性研究中 propensity score 未知的情形下，进一步基于 monotonic index model 类发展了 doubly robust 半监督估计量。理论结果表明，估计量具有 cube root 收敛速率，其非标准渐近分布为带二次漂移的中心化 Gauss 过程的最大值（Chernoff-type 分布）。模拟与 ACTG 175 实证展示了相对于纯监督方法的效率提升与双重稳健性。对您有用：DR 与半监督学习结合的思路可迁移至 proximal CI 等因果设定中处理无标签数据，且 cube root 收敛与非标准渐近分布的理论分析对您在数学统计与假设检验方向的兴趣有直接参考价值。
- **关键技术**: `doubly robust estimation`, `single index kernel smoothing`, `monotonic index model`, `cube root convergence`, `value function optimization`, `semi-supervised imputation`
- **为什么对您有用**: 直接推进因果推断中 optimal treatment regime 的半监督 DR 估计，其 cube root 收敛与非标准渐近分布（Chernoff-type）对您在数学统计假设检验方向的兴趣有理论参考价值，DR+半监督的框架也可迁移至 proximal CI 等设定。

### 8. [10.5705/ss.202025.0267](https://doi.org/10.5705/ss.202025.0267) — Semi-Parametric Estimation of Potential Outcome Distributions and General Causal Estimands by Borrowing Information from Both Treatments and Controls
- **作者**: Manli Cheng, Yukun Liu
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在潜在结果框架下，针对传统方法忽略不同处理组潜在结果相似性导致的效率损失问题，本文提出半参数比例似然比模型（SPLRM）联合建模潜在结果的条件分布。SPLRM 通过共享基线分布从处理组和对照组借用信息，采用最大经验似然估计（MELE）估计底层参数及一般因果被估量，并开发了迭代经验似然算法。理论证明所提估计量具有渐近正态性，且检验分布处理效应的似然比统计量渐近服从中心卡方分布。相比分别估计的传统方法，该途径提升了效率与稳健性，并在经典 NSW 数据集上验证了实用性。对您有用：直接关联因果推断的效率理论与半参数估计，其借用信息提升效率的思路和经验似然假设检验方法可迁移至您关注的因果推断与假设检验子方向。
- **关键技术**: `semi-parametric proportional likelihood ratio model`, `maximum empirical likelihood estimation`, `iterative empirical likelihood algorithm`, `likelihood ratio test`, `asymptotic normality`, `potential outcome distribution`
- **为什么对您有用**: 直接关联您 primary interest 中的因果推断（潜在结果框架）、半参数理论及效率理论（通过共享基线分布借用信息提升效率），同时涉及假设检验（分布处理效应的 LRT），方法可迁移至一般因果被估量的高效率推断。

### 9. [10.5705/ss.202025.0236](https://doi.org/10.5705/ss.202025.0236) — Quantification and Inference of Asymmetric Relations Under Generative Exposure Mappings
- **作者**: Soumik Purkayastha, Peter Xuekun Song
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在双变量因果发现设定下，本文提出在生成暴露映射（GEM, Y=g(X)+ε）框架下基于Shannon熵的“非对称系数”，以量化变量间的方向性非对称。方法利用生成函数的丰富类别，通过数据分割与交叉拟合（cross-fitting）建立大样本理论保证，并采用基于快速傅里叶变换（FFT）的密度估计避免带宽调参。该框架允许结果变量存在测量污染，填补了现有双变量因果发现方法缺乏不确定性推断的空白。模拟显示其优于现有因果发现方法；在表观遗传学（DNA甲基化与血压）流行病学数据应用中揭示了心血管疾病基因的新通路。对您有用：该文将交叉拟合与半参数理论应用于因果方向推断，其FFT密度估计与处理测量污染的思路可迁移至您关注的proximal CI或测量误差下的因果推断问题。
- **关键技术**: `bivariate causal discovery`, `Shannon entropy`, `generative exposure mapping`, `cross-fitting`, `FFT-based density estimation`, `outcome contamination`
- **为什么对您有用**: 结合了因果推断（双变量方向发现）与半参数理论（交叉拟合、非参数密度估计），并在流行病学数据上应用；其处理测量污染与交叉拟合推断的框架对您关注的proximal CI及测量误差下的因果推断有直接借鉴意义。

### 10. [10.5705/ss.202024.0199](https://doi.org/10.5705/ss.202024.0199) — Efficient Learning of DAG Structures in Heavy-tailed Data
- **作者**: Wei Zhou, Xueqian Kang, Wei Zhong, Junhui Wang
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究误差项服从重尾分布（如Pareto、Cauchy等）的线性有向无环图（DAG）结构学习问题，目标是在不依赖常见faithfulness假设下实现因果结构的有效识别。作者提出两步算法TopHeat：首先基于重尾DAG的新重构准则，以自顶向下方式分层重构拓扑层；其次通过针对重尾分布修改的条件独立性检验恢复有向边。理论上证明了算法在精确DAG结构恢复上的一致性。模拟与17国汇率数据的实证分析表明，该方法在重尾设定下优于现有方法，并揭示了欧元推出后欧洲金融传染效应趋于稳定。对您有用：该文放松了faithfulness假设并处理重尾数据，其修改的条件独立性检验对您在因果推断与假设检验交叉领域的研究有参考价值，实证部分也提供了金融传染的经济数据集。
- **关键技术**: `DAG structure learning`, `topological layer reconstruction`, `conditional independence testing`, `heavy-tailed distributions`, `causal discovery without faithfulness`
- **为什么对您有用**: 涉及因果发现（DAG学习）与假设检验（条件独立性），放松了faithfulness假设并处理重尾误差，对因果推断的结构学习与假设检验交叉方向有参考价值；汇率实证对经济理论兴趣有数据集价值。

### 11. [10.5705/ss.202024.0227](https://doi.org/10.5705/ss.202024.0227) — Collaborative Analysis for Paired A/B Testing Experiments
- **作者**: Qiong Zhang, Lulu Kang, Xinwei Deng
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究在同一用户群体上进行的配对 A/B 测试的协同分析问题，目标是在个体效应导致实验间响应相关时，更精确地估计处理效应。提出一种协同分析框架，利用同一受试者在不同实验中的响应相关性构建联合线性估计量。通过消除个体效应干扰，推导出该估计量的渐近分布，并在一定假设下证明其为渐近最佳线性无偏估计（ABLUE）。相比传统独立分析，该方法具有更小的渐近方差，且计算高效、易于实现。对您有用：虽然理论深度不及半参数效率界，但其“利用共享个体效应提升多实验 ATE 估计效率”的思路，可为纵向或多次干预下的因果推断效率理论提供线性框架下的直观参照。
- **关键技术**: `paired A/B testing`, `asymptotically best linear unbiased estimator (ABLUE)`, `individual random effect`, `generalized least squares`, `average treatment effect estimation`
- **为什么对您有用**: 涉及 A/B 测试（随机化实验因果推断）和渐近最优线性估计（效率理论），可为多实验/纵向因果推断的效率提升提供线性框架下的直观参照。

### 12. [10.5705/ss.202024.0306](https://doi.org/10.5705/ss.202024.0306) — Rematching Estimators For Average Treatment Effects
- **作者**: Lam Lam Hui, Kin Wai Chan
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在因果推断的匹配估计框架下，针对固定匹配数（M0）的简单匹配估计量通常不具备渐近有效性（inefficient）的问题，本文提出了一种通过“重新匹配”（rematching）变匹配数来提升效率的新估计量。核心机制在于不增加原有的M0（避免引入额外偏差），而是从反方向对处理组单元进行重新匹配，以利用未匹配的对照组单元。所提的 rematching 估计量适用于 ATE 和 ATT，并在理论上被证明是渐近有效的，且在相同 M0 下比传统匹配估计量一致更优（uniformly more efficient）。仿真实验和经典 NSW（National Supported Work）数据集的实证结果均验证了该方法在有限样本下的效率提升。对您有用：该研究直接触及您 primary interest 中的因果推断估计与效率理论，提供了一种在不增加偏差前提下提升匹配估计量效率的新视角，且 NSW 数据应用对经济理论方向的因果实证有参考价值。
- **关键技术**: `matching estimators`, `variable number of matches`, `asymptotic efficiency`, `uniform efficiency improvement`, `average treatment effect`
- **为什么对您有用**: 直接关联您 primary interest 中的因果推断估计与效率理论，提供在不增加偏差前提下提升匹配估计量效率的新机制；NSW 数据应用对经济理论方向的因果实证亦有参考价值。

### 13. [10.5705/ss.202023.0202](https://doi.org/10.5705/ss.202023.0202) — Addressing Label Noise in Causation Classification via Kernel Embeddings
- **作者**: Pingbo Hu, Grace Y. Yi
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究因果方向分类问题：给定 i.i.d. 成对向量序列，判断二者间是否存在因果关系，视为二分类任务。方法上，利用核均值嵌入（kernel mean embedding）将经验分布映射到 RKHS 特征空间，再在特征空间中训练分类器推断因果方向。核心挑战在于因果标注数据中常见的误标签（mislabeling）问题，作者量化了误标签对分类器的影响，并提出了校正误标签效应的鲁棒学习方法，给出了理论保证。该工作将非参数核方法与因果推断交叉，对您在因果推断中处理测量误差/标签噪声的设定有参考价值，同时核均值嵌入的技术路线也可迁移至您关注的半参数/非参数效率理论中。
- **关键技术**: `kernel mean embedding`, `RKHS classification`, `label noise robustness`, `mislabeling effect quantification`, `causation classification`
- **为什么对您有用**: 因果推断中的标签噪声与您关注的 sensitivity analysis 和 identification 问题相通；核均值嵌入作为非参数工具，与您 primary interest 中的半参数/非参数理论及效率理论直接相关。

### 14. [10.5705/ss.202024.0188](https://doi.org/10.5705/ss.202024.0188) — Conditional Generative Adversarial Network for Individualized Causal Mediation Analysis with Survival Outcome
- **作者**: Cheng Huan, Xinyuan Song, Hongwei Yuan
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究生存结局下的个体化因果中介分析，目标是在无强参数假设下识别与估计个体化的直接和间接中介效应。提出基于条件生成对抗网络（CGAN）的个体化因果中介分析方法（CGAN-ICMA-SO），通过条件生成器学习潜在结局的分布以捕捉个体异质性。理论上证明了在温和正则条件下，推断条件生成器的估计分布收敛于真实条件分布。该方法避免了传统生存模型对特定分布的依赖，但未提供半参数有效界或 n^{-1/2}-CAN 的渐近正态性保证。数值实验表明其优于五种现有方法，并在阿尔茨海默病神经影像数据集上揭示了 APOE-4 等位基因对 AD 发病时间的个体化直接与间接效应。对您而言，该文将深度生成模型引入因果中介分析，提供了生存数据下个体化效应的算法实现思路，但理论深度（如影响函数、半参数效率）相对有限。
- **关键技术**: `causal mediation analysis`, `conditional generative adversarial network`, `individualized causal effects`, `survival outcome`, `distribution convergence`
- **为什么对您有用**: 论文涉及您 primary interest 中的因果中介分析与生存数据，并触及 secondary interest 的流行病学数据应用；但其基于 GAN 的方法缺乏半参数效率理论和影响函数推导，可作为了解 ML 在中介分析中应用的参考，而非理论借鉴。

### 15. [10.5705/ss.202025.0157](https://doi.org/10.5705/ss.202025.0157) — Robust Control Experiments for Multivariate Tests with Covariates and Network Information
- **作者**: Shaohua Xu, Yongdao Zhou
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在多变量检验（multivariate testing）设定下，处理效应受协变量混淆且个体间存在网络连接，目标是寻找对协方差结构误设定具有鲁棒性的最优实验分配方案。本文首次引入混合效应模型以同时刻画协变量不确定性与网络结构，并提出了衡量协方差误设定导致效率后悔（regret of efficiency）的准则。基于该准则，作者推导出 minimax 鲁棒实验方案，并创新性地提出将设计与鲁棒协方差结构进行最优匹配的方案。理论证明该方案对多种最优性准则具有弹性，且在模型误设定下仍能保持统计效率；仿真与实例验证了其相较于现有方法的优越性。该文将 minimax 理论与网络干扰下的实验设计结合，对您在因果推断中处理网络干扰与设计效率的思考有直接参考价值。
- **关键技术**: `minimax robust design`, `mixed effect model`, `network interference`, `regret of efficiency`, `optimal experimental design`, `covariance misspecification`
- **为什么对您有用**: 本文处理因果推断实验设计（A/B testing）中的网络干扰与协变量混淆，其 minimax 鲁棒设计与效率后悔准则对您在因果推断（实验设计/网络干扰）及效率理论方面的研究有直接参考价值。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 31 篇)*

### 1. [10.5705/ss.202025.0036](https://doi.org/10.5705/ss.202025.0036) — Robust Max Statistics for High-dimensional Inference
- **作者**: Mingshuo Liu, Miles Lopes
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `weaker_assumption`
- **摘要**: 在高维重尾数据设定下，本文研究基于 max statistic 的假设检验问题，目标是对高维均值等参数进行推断，放松了传统文献对轻尾分布的限制。提出基于 robust max statistic 的 bootstrap 推断方法，在扩展的 L^4-L^2 矩等价条件与弱方差衰减条件下，证明了 bootstrap 逼近在 Kolmogorov 距离下可达到近参数速率（near-parametric rate），且该收敛速率与数据维度无关。理论结果适用于欧氏数据与函数型数据，仿真实验验证了方法在重尾设定下对第一类错误和功效的良好控制。对您有用：直接推进了高维假设检验在重尾假设下的理论，其中 L^4-L^2 矩条件与您关注的 RMT 高维协方差阵理论高度同源，可为您在高维重尾推断方面提供更弱的假设参考。
- **关键技术**: `robust max statistics`, `bootstrap approximation`, `L^4-L^2 moment equivalence`, `weak variance decay condition`, `Kolmogorov metric`
- **为什么对您有用**: 直接对应您的高维统计与假设检验兴趣；文章使用的 L^4-L^2 矩等价条件是 RMT 与高维协方差估计中的核心假设，阅读本文可了解如何在重尾假设下获得与维度无关的 bootstrap 近参数收敛速率，为高维检验放松假设提供思路。

### 2. [10.5705/ss.202023.0364](https://doi.org/10.5705/ss.202023.0364) — Concentration Inequalities for High-Dimensional Linear Processes with Dependent Innovations
- **作者**: Eduardo Fonseca Mendes, Fellipe Lopes Lima Leite
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `weaker_assumption`
- **摘要**: 本文研究高维向量线性过程在依赖创新（sub-Weibull、mixingale）下的 l∞ 范数浓度不等式，并据此给出 lag-h 自协方差矩阵最大逐元素范数的浓度界。核心设定允许创新序列兼具重尾（sub-Weibull）与时间依赖（mixingale），突破了传统 i.i.d. sub-Gaussian 假设。应用方面，将不等式用于高维 VAR(p) 的稀疏估计（如 l1-penalized）及高维 HAC 协方差矩阵估计，给出了相应的有限样本误差界。技术工具包括 mixingale 不等式、Bernstein-type 浓度界与 entrywise max 控制策略。对您有用：该浓度不等式可直接服务于高维推断（如 debiased ML / HAC 中的噪声控制），且 mixingale + sub-Weibull 的弱假设框架与您关注的 RMT 及高维效率理论中依赖数据设定高度契合。
- **关键技术**: `sub-Weibull concentration`, `mixingale inequality`, `l_infinity norm concentration`, `lag-h autocovariance matrix`, `high-dimensional VAR sparse estimation`, `HAC covariance estimation`
- **为什么对您有用**: 直接推进您 primary interest 中高维统计 / RMT 的浓度不等式工具箱，mixingale + sub-Weibull 弱假设对高维依赖数据推断（HAC、debiased ML 噪声项控制）有迁移价值。

### 3. [10.5705/ss.202023.0242](https://doi.org/10.5705/ss.202023.0242) — Statistical Inference For Ultrahigh Dimensional Location Parameter Based On Spatial Median
- **作者**: Guanghui Cheng, Liuhua Peng, Changliang Zou
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 本文在超高维一般多元模型下，研究基于样本空间中位数的位置参数统计推断问题，目标包括同时置信区间构建、全局检验及 FDR 多重检验。为实现推断，作者推导了样本空间中位数的新型 Bahadur 表示，并给出了余项的最大范数界。在此基础上，建立了样本空间中位数在超矩形类上的高斯逼近。进一步提出了乘子 Bootstrap 算法来近似统计量分布，且证明了该逼近在维度 p 随样本量 n 指数级发散时依然成立。理论结果将空间中位数的推断拓展至超高维区域，模拟与基因微阵列数据分析验证了方法的有效性。对您有用：该文的 Bahadur 展开与高斯逼近技术可直接迁移至您关注的高维假设检验问题，乘子 Bootstrap 算法也对统计计算有参考价值。
- **关键技术**: `spatial median`, `Bahadur representation`, `Gaussian approximation`, `multiplier bootstrap`, `ultrahigh dimensional inference`, `FDR control`
- **为什么对您有用**: 直接涉及您关注的高维假设检验，其超高维 Bahadur 表示与最大范数界的技术细节对研究高维稳健估计的渐近性质有直接启发，乘子 Bootstrap 算法也契合您的统计计算兴趣。

### 4. [10.5705/ss.202025.0069](https://doi.org/10.5705/ss.202025.0069) — Quantile Index Regression
- **作者**: Yingying Zhang, Qianqian Zhu, Yuefeng Si, Guodong Li
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对极端分位数水平下因数据稀疏导致估计不可靠的问题，提出分位数指标回归模型，通过在数据丰富的中间分位数水平拟合并外推至尾部。该模型对尾部施加灵活的参数结构，并利用复合分位数回归（CQR）获得非交叉的分位数估计量。理论方面，低维情形下证明了估计量的渐近正态性，高维情形下推导了非渐近误差界。核心技术依赖于分位数指标的重参数化与 CQR 目标函数的凸性以保证计算可行性与理论收敛率。对您有用：高维设定下的非渐近误差界推导直接契合您对高维统计理论的兴趣，且 CQR 的凸优化结构可为高维 debiased 推断或统计计算提供潜在的理论切入点。
- **关键技术**: `quantile index regression`, `composite quantile regression`, `non-asymptotic error bounds`, `tail extrapolation`, `asymptotic normality`
- **为什么对您有用**: 高维设定下的非渐近误差界推导直接契合您对高维统计理论的兴趣，且 CQR 的凸优化结构可为高维 debiased 推断或统计计算提供潜在的理论切入点。

### 5. [10.5705/ss.202025.0044](https://doi.org/10.5705/ss.202025.0044) — High-dimensional Extreme Quantile Regression
- **作者**: Yiwei Tang, Huixia Judy Wang, Deyuan Li
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究协变量维度 p 随样本量 n 增长的高维极端条件分位数估计问题，目标是在极值理论(EVT)外推框架下识别极尾条件分位数。针对传统固定 p 方法在高维下失效的问题，作者提出结合变量选择与极值外推的新估计方法。理论上建立了所提估计量在维度增长设定下的渐近性质与收敛速率，克服了高维惩罚带来的额外偏差与极值外推的叠加误差。模拟表明该方法在 p 增长及超高维场景下优于现有方法，车险数据实证亦验证了其变量选择与极值索赔估计的有效性。对您有用：该文将高维选择机制与极值外推结合，其高维渐近理论推导对您在 high-dimensional statistics 和 semiparametric theory 的交叉研究有直接参考价值。
- **关键技术**: `extreme value theory extrapolation`, `high-dimensional quantile regression`, `variable selection`, `asymptotic properties under growing dimension`, `tail index estimation`
- **为什么对您有用**: 直接涉及您 primary interest 中的 high-dimensional statistics（维度随样本量增长的渐近性质）与 semiparametric theory（分位数回归与极值外推），其高维极值估计的渐近收敛率与变量选择机制可为您的高维推断或半参数效率研究提供方法学借鉴。

### 6. [10.5705/ss.202024.0279](https://doi.org/10.5705/ss.202024.0279) — Estimating Covariance Matrices at Different Levels in Repeated Measurements
- **作者**: Sunpeng Duan, Guo Yu, Juntao Duan, Yuedong Wang
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在重复测量（层次结构）数据设定下，本文目标是分别估计组间与组内的高维协方差矩阵，并施加稀疏与正定约束。现有高维稀疏协方差估计多假设样本独立，忽略层次内相关会导致推断失效。作者提出基于凸优化的稀疏正定估计器，保证了计算的高效性与矩阵的正定性。理论上，文章建立了所提估计器的收敛速率。模拟与临床数据应用验证了方法在恢复协方差图结构上的优越表现。对您有用：直接契合您的高维统计与统计计算兴趣，凸优化算法实现与误差阶分析可迁移至高维协方差推断与图模型学习。
- **关键技术**: `sparse covariance estimation`, `convex optimization`, `positive-definite constraint`, `hierarchical data structure`, `estimation error rate`
- **为什么对您有用**: 直接关联您的高维统计（协方差矩阵估计）与统计计算（凸优化求解）兴趣，其组间/组内分解思路对纵向/层次数据的协方差建模有参考价值。

### 7. [10.5705/ss.202025.0014](https://doi.org/10.5705/ss.202025.0014) — Detecting Structural Breaks in High-dimensional Functional Time Series Factor Models
- **作者**: Caixia Xu, Huacheng Su, Xu Liu, Jinhong You
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究高维泛函时间序列因子模型中因子载荷随时间发生未知次数结构突变的估计问题。提出三阶段检测方法：首先逐点估计因子载荷并计算相邻时间点的差异序列；其次采用 Wild Binary Segmentation (WBS) 算法对该差异序列进行变点检测，同时估计突变点的数量与位置；最后基于估计的变点位置对泛函因子模型进行重新估计。理论上证明了变点数量与位置估计的相合性，并在高维泛函设定下给出了相应的收敛率。对您有用：该工作属于高维统计（因子模型）与假设检验（变点检测）的交叉，WBS 结合逐点载荷差异的算法设计对您关注的高维统计计算与变点推断有直接借鉴价值。
- **关键技术**: `high-dimensional functional factor model`, `structural break detection`, `wild binary segmentation`, `time-varying factor loadings`, `change point estimation`
- **为什么对您有用**: 属于高维统计（因子模型）与假设检验（变点检测）的交叉方向；WBS 结合逐点载荷差异的算法设计对您关注的高维统计计算与变点推断有直接借鉴价值。

### 8. [10.5705/ss.202025.0109](https://doi.org/10.5705/ss.202025.0109) — Communication-Efficient Estimation of Regularized Smoothed Support Tensor Machine
- **作者**: Zihao Song, Lei Wang, Riquan Zhang, Weihua Zhao
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文在张量分类问题中，基于管秩（tubal rank）和管核范数正则化提出平滑支持张量机，避免了传统CP/Tucker分解需展开张量而破坏内在结构的问题。估计量采用管核范数正则化以实现低秩结构恢复，并建立了其统计收敛性质。进一步将框架扩展至分布式设定，提出仅需首台机器局部数据与其他机器梯度信息的通信高效正则化估计量，推导了其收敛率并给出低秩恢复的理论保证。计算上采用交替方向法求解。理论结果证明了分布式估计量在保持统计收敛率的同时显著降低通信成本。对您有用：该文将高维张量低秩正则化与分布式计算结合，其收敛率推导与通信高效算法设计对您在统计计算与高维统计方面的研究有直接参考价值。
- **关键技术**: `tubal nuclear norm regularization`, `smoothed support tensor machine`, `communication-efficient distributed estimation`, `low-rank tensor recovery`, `alternating direction method`
- **为什么对您有用**: 涉及高维张量低秩正则化的收敛率与恢复理论，以及分布式通信高效算法，直接契合您在“高维统计”与“统计计算（数值方法与算法）”上的兴趣，可借鉴其分布式估计量构造与收敛率分析技巧。

### 9. [10.5705/ss.202024.0423](https://doi.org/10.5705/ss.202024.0423) — Simultaneous Estimation and Dataset Selection for Transfer Learning in High Dimensions by a Non-convex Penalty
- **作者**: Zeyu Li, Dong Liu, Yong He, Xinsheng Zhang
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在高维迁移学习设定下，本文研究如何同时进行模型参数估计与信息源数据集选择，目标 estimand 为稀疏线性回归与广义低秩迹回归的系数或低秩矩阵。区别于传统先筛选数据集再迁移的两步法，提出基于非凸惩罚的联合估计与选择方法。计算上，针对非凸优化问题采用 DC（Difference of Convex）规划结合 ADMM（交替方向乘子法）求解。理论上，从统计与计算双重视角证明了算法的收敛性与参数估计的 oracle 性质。数值实验验证了联合方法的优势，并开发了 R 包 MHDTL。对您有用：该工作将非凸惩罚与 DC-ADMM 结合，为高维统计计算提供了具体的数值算法与理论保证，直接契合您在高维统计与统计计算方面的兴趣。
- **关键技术**: `high-dimensional transfer learning`, `non-convex penalty`, `DC programming`, `ADMM`, `low-rank trace regression`, `oracle property`
- **为什么对您有用**: 直接契合您在高维统计与统计计算方面的兴趣；DC-ADMM求解非凸惩罚的算法设计与收敛保证，对您关注的高维数值方法与软件实现有直接参考价值。

### 10. [10.5705/ss.202024.0283](https://doi.org/10.5705/ss.202024.0283) — High-Dimensional-Responses-Assisted Heterogeneous Nodal Influence Analysis
- **作者**: Dongxue Zhang, Wei Lan, Danyang Huang, Huazhen Lin
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在 m×n 矩阵网络数据（m 个节点、每节点 n 维响应）下，m 与 n 均发散，目标是通过 link function 将异质节点影响力参数与高维响应关联并估计。提出 response-assisted network influence model，允许异质误差方差；因传统 MLE 在此设定下失效，构建限制权重矩阵对角元的 GMM 估计量以回避未知误差方差的估计，并证明其一致性与渐近正态性。进一步提出同质性检验（homogeneity test）以检验影响力异质性，给出检验统计量的渐近分布。模拟与基金-股票实证展示了方法实用性。对您有用：双发散维度下 GMM 的构造与渐近理论、以及同质性检验，直接关联您的高维统计与假设检验兴趣，实证部分也涉及经济数据集。
- **关键技术**: `generalized method of moments`, `high-dimensional network model`, `double-asymptotics (m, n → ∞)`, `homogeneity test`, `heterogeneous error variance`, `asymptotic normality`
- **为什么对您有用**: 双发散维度下的 GMM 估计与渐近正态性理论、以及同质性检验，直接对应您的高维统计与假设检验 primary interests；基金-股票实证数据对经济理论 secondary interest 也有参考价值。

### 11. [10.5705/ss.202025.0071](https://doi.org/10.5705/ss.202025.0071) — Bayesian High-Dimensional Grouped-Regression Using Sparse Projection-posterior
- **作者**: Samhita Pal, Subhashis Ghosal
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究高维分组回归下的贝叶斯变量选择与估计问题，在稀疏性假设下通过降维映射重构后验分布。核心方法为稀疏投影后验（sparse projection posterior），利用 Group LASSO、Group SCAD 及 Adaptive Group LASSO 惩罚构造投影映射，将稠密后验样本浸入稀疏空间以实现组选择。理论上证明了该方法在估计与预测上具有最优后验收缩率（optimal posterior contraction rate），且满足模型选择相合性。进一步提出 Debiased Group LASSO 投影映射以保证置信集的精确覆盖，并在非参数可加模型中结合 B-spline 展开进行应用。模拟与 ADNI 阿尔茨海默症脑 MRI 数据验证了方法有效性；其 debiased 投影机制与 B-spline 非参数设定，直接关联您的高维 debiased 推断及非参数理论兴趣。
- **关键技术**: `sparse projection posterior`, `group LASSO/SCAD penalty`, `posterior contraction rate`, `debiased group LASSO`, `nonparametric additive model`, `B-spline expansion`
- **为什么对您有用**: 论文提出的 Debiased Group LASSO 投影映射解决了高维分组回归中的精确推断（置信区间覆盖）问题，直接关联您的高维统计与效率理论（debiased inference）兴趣；其非参数可加模型设定及 ADNI 流行病学数据应用也契合您的非参数理论与流行病学应用方向。

### 12. [10.5705/ss.202025.0205](https://doi.org/10.5705/ss.202025.0205) — Sparsity Learning via Structured Functional Factor Augmentation
- **作者**: Hanteng Ma, Ziliang Shen, Xingdong Feng, Xin Liu
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在高维函数线性回归设定下，针对函数协变量间存在相关性导致的变量选择与推断挑战，本文提出了函数因子增广结构（fFAS）。核心方法 fFASM 通过对多变量函数序列引入潜在因子增广结构以缓解协变量共线性，进而实现稀疏学习与函数变量选择。理论上证明了 fFAS 结构的合理性，并建立了 fFASM 的估计相合性与选择一致性。数值实验表明该方法在估计精度和选择一致性上优于忽略协变量相关性的传统方法。对您有用：该文处理高维函数协变量相关性的因子增广思路，可为您在高维统计（特别是函数/张量数据的变量选择）或半参数推断中提供方法迁移参考。
- **关键技术**: `functional linear regression`, `factor augmentation`, `high-dimensional variable selection`, `sparsity learning`, `selection consistency`
- **为什么对您有用**: 文章聚焦高维函数回归的变量选择与推断，属于高维统计与半/非参数理论的交叉，其因子增广处理协变量相关性的思路对您研究高维统计或半参数推断具有方法学参考价值。

### 13. [10.5705/ss.202024.0329](https://doi.org/10.5705/ss.202024.0329) — Efficient Decoding from Heterogeneous 1-Bit Compressive Measurements over Networks
- **作者**: Canyi Chen, Zhengtian Zhu, Liping Zhu
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究去中心化网络中异质 1-bit 压缩感知 (1-bit CS) 的高维信号恢复问题，设定为仅允许局部邻居通信且存在符号翻转与网络异质性。作者将 1-bit CS 重构为带惩罚的最小二乘问题，并基于此设计了广义交替方向乘子法 (ADMM) 进行分布式求解。算法层面，该 ADMM 算法实现简单且被证明具有线性收敛速率；统计层面，在有限次通信后，估计量即可达到近 oracle 统计收敛速率，并在温和条件下实现可靠的支撑集恢复。理论结果同时给出了算法收敛与统计误差的显式保证，数值实验进一步验证了方法的有效性。对您有用：该文将高维 1-bit CS 推广至去中心化设定，其 ADMM 算法设计与线性收敛/近 oracle 速率的双重保证，对您在统计计算（分布式优化算法）与高维统计（1-bit 信号恢复率）方向的研究有直接参考价值。
- **关键技术**: `1-bit compressive sensing`, `decentralized optimization`, `generalized ADMM`, `penalized least squares`, `near-oracle convergence rate`, `support recovery`
- **为什么对您有用**: 直接关联您的高维统计与统计计算兴趣：提供了去中心化高维 1-bit CS 的 ADMM 算法实现及其线性收敛与近 oracle 统计速率的双重理论保证，算法与理论分析技巧可迁移至其他分布式高维估计问题。

### 14. [10.5705/ss.202025.0147](https://doi.org/10.5705/ss.202025.0147) — Effects-Nested Multi-Level Supervised Heterogeneity Analysis
- **作者**: Ruiyue Wang, Sanguo Zhang, Shuangge Ma
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在监督异质性分析框架下，本文研究多水平（如两层）的异质性结构，设定高层重要变量嵌套于低层重要变量中。提出一种惩罚估计与变量选择方法来实现多水平分组与嵌套变量筛选，并建立了其理论（如选择相合性）与计算性质。核心技术为嵌套稀疏结构下的惩罚回归与定制优化算法。仿真与 TCGA 乳腺癌数据验证了其分组与估计表现。对您而言，该文在多水平异质性建模与惩罚估计上的理论推导，可为高维变量选择及因果推断中异质性处理效应（CATE）的分层估计提供结构化参考。
- **关键技术**: `penalized estimation`, `variable selection`, `multi-level heterogeneity`, `nested sparsity`, `group-wise regression`
- **为什么对您有用**: 涉及高维惩罚估计与变量选择的理论性质，与您的高维统计兴趣相关；其多水平异质性建模思路也可为因果推断中的异质性处理效应（如 CATE 的分层估计）提供结构化借鉴。

### 15. [10.5705/ss.202024.0435](https://doi.org/10.5705/ss.202024.0435) — Mixed Membership Network with the Autoregressive Structure
- **作者**: Tianyi Sun, Bo Zhang, Baisuo Jin, Yuehua Wu
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文在动态随机块网络设定下，提出带一阶自回归结构的混合隶属度网络模型，目标是在时间依赖下估计隶属度矩阵并完成社区检测。作者设计了 AR-1 混合谱聚类算法进行隶属度矩阵估计，并引入经验特征值阈值估计器来确定社区数量（隐含高维谱界与随机矩阵相变思想）。模拟表明该方法的泛化能力优于以往方法，且显式错误率在多种设定下不劣于现有基准。实证分析验证了方法的有效性。对您而言，经验特征值阈值估计器的设计与高维统计/随机矩阵理论中的谱方法直接相关，可作为动态网络谱聚类中秩估计的参考。
- **关键技术**: `mixed membership stochastic blockmodel`, `autoregressive network structure`, `spectral clustering`, `empirical eigenvalue threshold`, `community detection`
- **为什么对您有用**: 文中用于估计社区数的经验特征值阈值方法与高维统计和随机矩阵理论中的谱界/相变现象紧密相关，对您研究高维网络或矩阵谱方法有参考价值。

### 16. [10.5705/ss.202024.0258](https://doi.org/10.5705/ss.202024.0258) — Grouped Heterogeneous Gaussian Graphical Models for High-Dimensional Clustered Data
- **作者**: Xin Zeng, Shuangge Ma, Qingzhao Zhang
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 针对高维聚类数据的网络异质性分析问题，本文在假定聚类可划分为不同组、且组间异质性由簇级混合概率刻画的设定下，提出分组异质高斯图模型（Grouped-HGGM）。与多数需预先指定成分数的现有方法不同，该方法通过融合技术（fusion technique）同时实现网络结构的稀疏估计与成分数的自动确定。模型将异质性来源归因于组间差异，并在组内采用混合概率刻画簇级网络变化。理论上，文章建立了高维设定下估计量的相合性（consistency properties）。对您可能有用：若您关注高维统计中的图模型估计与聚类结构，本文的融合惩罚与自适应成分选择机制可提供方法学参考。
- **关键技术**: `Gaussian graphical models`, `high-dimensional clustered data`, `fusion penalty`, `mixture probability`, `sparse estimation`, `consistency theory`
- **为什么对您有用**: 本文属于高维统计范畴，虽然未涉及您核心关注的 RMT 或半参数效率界，但其针对高维图模型的融合惩罚与自适应成分选择方法，对处理高维聚类数据的网络结构推断有直接参考价值。

### 17. [10.5705/ss.202025.0101](https://doi.org/10.5705/ss.202025.0101) — Multilayer Network Regression with Eigenvector Centrality and Community Structure
- **作者**: Zhuoye Han, Tiandong Wang, Zhiliang Ying
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文在多层网络（四阶张量结构）设定下，提出结合特征向量中心性与社区结构的两阶段回归模型，目标是在层内与层间依赖结构下整合信息并估计回归系数。方法首先定义基于社区的中心性度量，将其作为回归协变量；针对网络数据的固有噪声，分别考察了无测量误差与有测量误差下的中心性指标，并利用最小二乘法进行回归推断。理论部分证明了最小二乘估计的相合性，核心涉及谱方法（特征向量中心性）与测量误差模型的结合。实证部分将该方法应用于世界投入产出数据集，研究国家与行业间的网络结构对总产出的影响。对您而言，该文将高维谱方法与测量误差结合的理论分析，以及投入产出网络的经济数据应用，与您的高维统计/随机矩阵理论及经济理论兴趣直接相关。
- **关键技术**: `eigenvector centrality`, `multilayer network regression`, `community structure`, `measurement error model`, `spectral method`, `tensor-like network`
- **为什么对您有用**: 理论层面涉及高维谱方法与测量误差的结合（关联高维统计与随机矩阵理论），应用层面提供了世界投入产出网络数据集及模型（关联经济理论的数据集与模型兴趣）。

### 18. [10.5705/ss.202024.0276](https://doi.org/10.5705/ss.202024.0276) — Grade of Membership Analysis for Multi-Layer Ordinal Categorical Data
- **作者**: Huan Qing
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多层有序分类数据（如纵向心理测试）设定下，假设个体在不同时间层共享相同的混合隶属度（mixed membership），目标是估计这些潜在类别的权重。本文将传统的 Grade of Membership (GoM) 模型扩展至多层有序数据，提出 multi-layer GoM 模型。为估计共享的混合隶属度，作者提出基于去偏 Gram 矩阵和的新方法，利用矩阵去偏技术消除高维误差。理论上给出了 GoM-DSoG 的个体级收敛速率，并证明无响应减少、个体/项目/层数增加有利于估计精度。实验验证了理论发现及该方法在确定潜在类数上的准确性。对您可能有用：其基于 Gram 矩阵和的去偏估计思路与高维统计和随机矩阵理论中的谱方法高度相关，可为您在 RMT 或高维潜在变量模型推断中提供矩阵去偏技术的参考。
- **关键技术**: `Grade of Membership model`, `debiased sum of Gram matrices`, `mixed membership estimation`, `per-subject convergence rate`, `multi-layer ordinal data`
- **为什么对您有用**: 论文核心的“去偏 Gram 矩阵和”(DSoG) 估计方法直接涉及高维统计与随机矩阵理论中的矩阵去偏与谱分析技术，为您在 RMT 框架下处理多层/高维潜在变量推断提供了可借鉴的收敛率分析与去偏策略。

### 19. [10.5705/ss.202025.0087](https://doi.org/10.5705/ss.202025.0087) — Distributed Algorithms for High-Dimensional Statistical Inference and Structure Learning with Heterogeneous Data
- **作者**: Hongru Zhao, Xiaotong Shen
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在分布式多站点高维异质数据且仅共享汇总统计量的隐私约束设定下，目标是同时估计全局效应与站点特异效应并进行有效统计推断。提出异质模型整合全局与局部效应，采用非凸正则化（DC规划）与 ℓ₀ 约束实现变量选择一致性；尽管底层优化是NP-hard，算法在合理条件下以高概率在多项式时间内收敛至全局最优。推断的核心技巧是对 nuisance 参数施加 ℓ₀ 惩罚而保持目标参数无惩罚，从而避免正则化偏差，获得有效的 post-selection 推断。理论上证明了选择一致性与推断有效性，算法上提供了收敛保证。对您有用：该文将高维推断的 debiasing 思想与分布式非凸优化计算结合，直接契合您对高维统计推断、效率理论及统计计算（数值算法）的核心兴趣。
- **关键技术**: `distributed high-dimensional inference`, `heterogeneous data modeling`, `difference of convex (DC) programming`, `ℓ₀ penalization`, `post-selection inference`
- **为什么对您有用**: 直接契合您的高维统计推断与统计计算兴趣：在分布式隐私约束下，通过 ℓ₀ 惩罚 nuisance 参数而保留目标参数无惩罚的 debiasing 技巧，以及 DC 规划的数值收敛保证，为高维异质数据的有效推断提供了新算法与理论。

### 20. [10.5705/ss.202025.0303](https://doi.org/10.5705/ss.202025.0303) — Linear Shrinkage Convexification of Penalized Linear Regression with Missing Data
- **作者**: Seongoh Park, Seongjin Lee, Nguyen Thi Hai Yen, Nguyen Phuoc Long, Johan Lim
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维惩罚线性回归设定下，缺失数据会导致协变量协方差矩阵非正定，使最小二乘损失非凸。本文提出线性收缩正定（LPD）修正法，通过对协方差矩阵施加线性收缩以保证其正定性与一致性，从而将非凸优化转化为凸问题。该修正具有解析表达式，计算高效。理论上，作者证明了在缺失数据下基于 LPD 的 ℓ₁ 惩罚回归估计量具有选择一致性，且 ℓ₂ 误差收敛率为 s₀^{3/2}√(log p / n)（s₀ 为非零系数个数）。实证部分将方法应用于癌症药物敏感性（GDSC）基因组数据集。对您有用：该文将线性收缩（RMT 经典工具）与高维 Lasso 结合解决缺失数据下的非凸问题，其协方差修正思路与收敛率证明对您的高维统计与 RMT 兴趣有直接参考价值。
- **关键技术**: `linear shrinkage estimator`, `covariance matrix positive definite modification`, `penalized linear regression (Lasso)`, `selection consistency`, `convexification`
- **为什么对您有用**: 直接关联您的高维统计与 RMT 兴趣：利用线性收缩修正协方差矩阵以凸化高维 Lasso 问题，且提供了具体的 ℓ₂ 收敛率与选择一致性证明，计算上具有解析解，对高维推断与计算算法设计有借鉴意义。

### 21. [10.5705/ss.202024.0341](https://doi.org/10.5705/ss.202024.0341) — Regularized Estimation of High-Dimensional Matrix-Variate Autoregressive Models
- **作者**: Hangjin Jiang, Baining Shen, Yuzhou Li, Zhaoxing Gao
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在行/列维度与样本量 T 同时发散的设定下，本文研究高维矩阵时间序列的双线性矩阵自回归（bilinear MAR）模型的正则化估计。针对高维下迭代最小二乘参数过多的问题，提出两种降维方法：一是假设系数矩阵带状结构，采用两步法（先迭代最小二乘初估，再带状迭代最小二乘）并用 BIC 选取带宽；二是假设系数矩阵稀疏，施加 LASSO 正则化。在维度发散且 T→∞ 的设定下，推导了两种估计量的渐近性质。模拟与实证展示了预测效果。对您有用：该文处理高维矩阵自回归的算法与渐近理论，直接关联您的高维统计与矩阵计算兴趣，且其经济数据应用对经济模型子方向有参考价值。
- **关键技术**: `bilinear matrix-variate autoregressive model`, `iterated least-squares`, `banded coefficient matrix`, `LASSO regularization`, `diverging dimensions asymptotics`, `BIC for bandwidth selection`
- **为什么对您有用**: 直接关联您的高维统计与矩阵计算兴趣，提供了高维矩阵时间序列参数估计的渐近理论与两步迭代算法；同时其经济数据应用对 secondary interest 中的经济模型有参考价值。

### 22. [10.5705/ss.202025.0223](https://doi.org/10.5705/ss.202025.0223) — High-Dimensional Log Contrast Models with Measurement Errors
- **作者**: Wenxi Tan, Lingzhou Xue, Songshan Yang, Xiang Zhan
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维成分数据回归设定下，当成分协变量存在测量误差时，由于成分约束使得单一分量的误差会传播至其他分量，传统 error-in-variable 回归方法不再适用。本文提出 Eric Lasso（Error-in-composition Lasso），同时处理成分约束结构与设计矩阵中的测量误差。理论上建立了 Eric Lasso 的估计误差上界（estimation error bound）以及渐近符号一致性选择性质（sign-consistent selection）。模拟实验和实际数据应用验证了有限样本表现。对您有用之处在于：高维成分数据的测量误差修正框架可迁移至因果推断中处理 mismeasured confounder 的场景，且误差界分析技术对高维推断有参考价值。
- **关键技术**: `error-in-variable regression`, `compositional data log-contrast model`, `Lasso-type penalization`, `estimation error bound`, `sign-consistent variable selection`
- **为什么对您有用**: 直接属于高维统计范畴，且成分约束下测量误差传播的建模思路可迁移至因果推断中 mismeasured confounder/IV 的设定，误差界与选择一致性结果对高维 debiased 方法有理论参考价值。

### 23. [10.5705/ss.202025.0115](https://doi.org/10.5705/ss.202025.0115) — Empirical Bayes Data Integration for Multi-Response Regression
- **作者**: Antik Chakraborty, Fei Xue
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多响应回归的数据整合设定下，本文提出基于经验贝叶斯的线性收缩估计量，通过收缩数据矩阵的奇异值来整合不同来源的向量值结果。该问题与特定损失下的协方差矩阵估计等价，作者为此构造了渐近最优估计量，并将基本线性收缩扩展为局部线性收缩估计量以提升灵活性。方法无需预设稀疏或低秩结构，在稀疏/稠密、低秩/非低秩参数设定下均适用，且相比全贝叶斯方法计算扩展性更强。理论上证明了估计量在特定损失下的渐近最优性，数值实验和 GTEx 项目的 TWAS 真实数据验证了方法的有效性。对您有用：奇异值收缩与协方差估计的渐近最优性直接关联高维统计与 RMT 兴趣，局部收缩与计算可扩展性对统计计算方向有参考价值，GTEx 数据也触及遗传流行病学数据集兴趣。
- **关键技术**: `empirical Bayes`, `singular value shrinkage`, `covariance matrix estimation`, `local linear shrinkage`, `asymptotic optimality`
- **为什么对您有用**: 奇异值收缩与协方差估计的渐近最优性直接关联您的高维统计与 RMT 兴趣，局部收缩与计算可扩展性对统计计算方向有参考价值；GTEx 数据应用也触及流行病学/遗传学数据集兴趣。

### 24. [10.5705/ss.202025.0211](https://doi.org/10.5705/ss.202025.0211) — Inference for High-dimensional Model Averaging Estimators
- **作者**: Lise Léonard, Eugen Pircalabelu, Rainer von Sacks
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在 p>n 的高维回归设定下，传统变量选择方法忽略了模型选择不确定性导致方差低估，本文旨在构建可进行统计推断的高维模型平均估计量。该估计量基于 debiased Lasso 构造，权重选取以最小化预测风险为目标。理论部分推导了该估计量在高维框架下的渐近正态分布，从而允许进行假设检验与置信区间构造，并给出了预测风险的最小损失保证。与现有方法相比，该方法同时实现了模型平均降低预测风险与基于渐近正态性的统计推断。对您有用：直接推进了高维统计与 debiased ML 的交叉方向，为高维模型平均后的假设检验提供了渐近理论工具。
- **关键技术**: `debiased Lasso`, `model averaging`, `high-dimensional inference`, `asymptotic normality`, `prediction risk minimization`
- **为什么对您有用**: 直接连接您的高维统计与 efficiency theory (debiased ML) 兴趣，为高维模型平均后的假设检验提供了基于 debiased Lasso 的渐近正态推断工具。

### 25. [10.5705/ss.202024.0248](https://doi.org/10.5705/ss.202024.0248) — Hybrid Denoising-screening for High-dimensional Contaminated Data
- **作者**: Liming Wang, Peng Lai, Chen Xu, Xingxiang Li
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究高维污染数据下的特征筛选问题，目标是在观测存在噪声行（污染样本）时同时剔除噪声观测与无关特征，保证筛选准确性。提出 hybrid denoising-screening（HDS）方法，核心是 dual sample-feature L0 拟合：对样本数和特征数同时施加 L0 约束，精确控制保留的观测与特征数量。HDS 在筛选过程中仅保留干净观测并自然考虑特征间联合效应，理论部分给出了筛选一致性（sure screening property）及迭代版本的收敛保证。模拟与真实数据实验表明，在污染比例较高时 HDS 优于传统 SIS/DCS 等筛选方法。对您而言，该文在高维筛选中引入行-列联合 L0 选择的思路，可启发高维稳健推断中 outlier-robust variable selection 的设计，但与您关注的 RMT 推断或 semiparametric efficiency 距离较远。
- **关键技术**: `L0 dual fitting`, `sure screening property`, `feature screening`, `contaminated observations`, `iterative screening`
- **为什么对您有用**: 与您的高维统计兴趣相关，但侧重 feature screening 而非 RMT 或 debiased inference；L0 行-列联合选择的计算与理论框架可迁移至高维稳健变量选择场景。

### 26. [10.5705/ss.202025.0232](https://doi.org/10.5705/ss.202025.0232) — Transfer Learning for Ridge Regression with Random Coefficients
- **作者**: Hongzhe Zhang, Hongzhe Li
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在高维随机系数 ridge 回归框架下，本文研究从多个源任务迁移学习到目标任务的问题，其中源任务的信息量由其系数与目标系数的相关性刻画。提出两个加权估计器——分别最小化估计风险和预测风险——均为目标与源 ridge 估计的最优线性组合。在高维渐近 p/n → γ 设定下，利用随机矩阵理论（Marchenko-Pastur 型极限）推导出最优权重及对应风险的闭式极限。模拟与脂质性状、结直肠癌微生物组预测应用均显示方法优于仅用目标或简单池化的 ridge 回归。对您有用：该文将 RMT 工具系统性地引入迁移学习风险最优权重求解，是高维 RMT 在新问题场景中的理论拓展，可直接借鉴其 RMT 闭式风险分析技术。
- **关键技术**: `random matrix theory`, `ridge regression with random coefficients`, `transfer learning optimal weighting`, `high-dimensional asymptotic risk`, `Marchenko-Pastur limit`
- **为什么对您有用**: 直接属于您 primary interest 中高维统计与 RMT 的交叉：用 RMT 闭式求解迁移学习 ridge 回归的最优权重与风险极限，技术路线可迁移到其他高维正则化估计的迁移/多任务设定。

### 27. [10.5705/ss.202024.0395](https://doi.org/10.5705/ss.202024.0395) — Large Dimensional Spearman's Rank Correlation Matrices: The Central Limit Theorem and Its Applications
- **作者**: Hantao Chen, Cheng Wang
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究高维设定下（p/n → c > 0）Spearman 秩相关矩阵的渐近性质，关注其线性谱统计量（LSS）的极限分布及改进版 Spearman 相关矩阵（3 阶 U-统计量）的谱分析。基于随机矩阵理论，文章证明了 Spearman 相关矩阵 LSS 的中心极限定理（CLT），将 Pearson 相关矩阵的已有结果推广至非参数秩相关情形；同时对改进的 Spearman 相关矩阵，将其视为 3 阶 U-统计量并建立相应的谱理论。基于上述 CLT，构造了三个新的高维独立性检验统计量，数值实验验证了其有限样本表现。对您有用：该工作直接推进了高维 RMT 中 LSS 的 CLT 理论，并将 3 阶 U-统计量嵌入 RMT 框架，为您在“高维假设检验”与“高阶 U-统计量”交叉方向提供了具体的理论工具与检验构造思路。
- **关键技术**: `linear spectral statistics`, `random matrix theory`, `central limit theorem`, `U-statistic of order 3`, `Spearman's rank correlation`, `high-dimensional independence test`
- **为什么对您有用**: 直接结合了您关注的“高维随机矩阵理论”与“高阶 U-统计量”，将 LSS 的 CLT 推广至秩相关及 3 阶 U-统计量情形，为高维独立性假设检验提供了新统计量与理论保证。

### 28. [10.5705/ss.202023.0131](https://doi.org/10.5705/ss.202023.0131) — Adaptive Block Banding Precision Matrix Estimation For Multivariate Longitudinal Data
- **作者**: Chunhui Liang, Wenqing Ma, Yanyuan Ma
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多元纵向数据设定下，本文研究具有 Banded Kronecker Sparse (BKS) 结构的精度矩阵估计问题，假设精度矩阵为自适应带状矩阵与稀疏矩阵的 Kronecker 乘积且均正定。估计方法结合了专门设计的自适应带状惩罚与 Lasso 惩罚，分别刻画时间维度的衰减相关与变量维度的稀疏性。计算上采用 Alternative Convex Search (ACS) 算法实现高效优化，并证明了该算法的计算收敛性。理论上建立了估计量的渐近收敛速率，提供了统计保证。模拟与 EEG/ADHD 实证表明该方法在捕捉带状稀疏特征上优于现有方法。对您有用之处在于其针对纵向数据的 Kronecker 结构建模与 ACS 优化算法，可为纵向因果推断中的高维协方差/逆协方差估计提供计算与理论参考。
- **关键技术**: `Kronecker product precision matrix`, `adaptive banding penalty`, `Lasso sparsity`, `Alternative Convex Search (ACS)`, `asymptotic convergence rate`
- **为什么对您有用**: 论文涉及高维纵向数据的结构化精度矩阵估计与优化算法，其 Kronecker 建模思路与 ACS 计算方法可为纵向因果推断中的高维协方差估计与统计计算提供直接参考。

### 29. [10.5705/ss.202024.0307](https://doi.org/10.5705/ss.202024.0307) — Estimation and Inference for High-dimensional Multi-response Growth Curve Model
- **作者**: Xin Zhou, Yin Xia, Lexin Li
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在高维多响应纵向生长曲线模型(GCM)设定下，目标是估计具Kronecker结构的高维协方差矩阵，并对全局及个体效应进行推断。方法引入Kronecker乘积分解超大规模协方差矩阵以汇聚相关样本提升精度，并设计非平凡的多步估计法分别估计各协方差分量。推断方面，构建了全局与个体效应的假设检验程序，严格证明了检验的size/power性质及FDR控制。理论给出了高维GCM下协方差估计与多重检验的渐近保证，并在阿尔茨海默病纵向神经影像数据中验证。对您有用：Kronecker协方差分解与多步估计技巧契合您的高维统计与矩阵计算兴趣，检验理论对应假设检验方向，且提供了流行病学纵向数据的应用范式。
- **关键技术**: `Kronecker product covariance decomposition`, `multi-step estimation`, `high-dimensional hypothesis testing`, `false discovery rate control`, `growth curve model`, `longitudinal neuroimaging analysis`
- **为什么对您有用**: Kronecker协方差分解与多步估计技巧直接对应您的高维统计与矩阵计算兴趣；全局/个体检验及FDR控制理论契合您的假设检验方向；同时提供了流行病学纵向神经影像数据的应用范式。

### 30. [10.5705/ss.202024.0310](https://doi.org/10.5705/ss.202024.0310) — Auxiliary Learning and its Statistical Understanding
- **作者**: Hanchao Yan, Feifei Wang, Chuanxin Xia, Hansheng Wang
- **期刊/来源**: Statistica Sinica
- 相关性 0/10
- **摘要**: 本文研究高维小样本下利用共享协变量的辅助任务提升主任务参数估计效率。在线性回归中，作者构造主任务与若干辅助任务的 OLS 估计的线性组合为加权估计量，并解析给出最优权重，证明其方差小于仅用主任务的 OLS。随后将加权估计量推广到广义线性模型，给出渐近正态性与方差缩减的理论。数值实验与智能售货机深度学习实例验证了效率提升。对您有用：该工作为高维回归中的多任务效率提供了显式最优权与方差界，可迁移至您关注的 semiparametric efficiency 与 debiased ML 中多源信息融合的效率改进。
- **关键技术**: `auxiliary learning`, `weighted OLS estimator`, `optimal weight derivation`, `GLM extension`, `variance reduction`
- **为什么对您有用**: 与您 primary interest 中的 efficiency theory (semiparametric efficiency bounds, debiased ML) 直接相关，提供了多任务共享协变量时显式最优权与方差缩减的解析结果，可迁移至高维 debiased ML 的多源信息融合效率改进。

### 31. [10.5705/ss.202024.0170](https://doi.org/10.5705/ss.202024.0170) — Network Assisted Approximate Factor Model Estimation
- **作者**: Yuzhou Zhao, Xinyan Fan, Bo Zhang
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `sharper_rate`
- **摘要**: 在近似因子模型（AFM）设定下，针对小样本（T 较小）时经典极大似然估计（MLE）收敛受限的问题，研究如何利用辅助网络信息改进因子载荷与潜因子的估计。提出一种联合拟极大似然估计，该方法灵活融合网络邻接信息并允许网络异质性。理论上严格证明了估计量的渐近性质，获得了比经典 MLE 更快的收敛速率，尤其在样本量较小时优势显著。数值模拟验证了该方法在有限样本下的表现。对您可能有用：该文在高维因子模型中利用网络结构突破了传统收敛下界，属于 sharper_rate 的理论推进，与您关注的高维统计与 RMT 理论直接契合。
- **关键技术**: `approximate factor model`, `joint quasi-maximum likelihood estimation`, `network-assisted estimation`, `convergence rate improvement`, `network heterogeneity`
- **为什么对您有用**: 直接关联您的高维统计与 RMT 兴趣：通过引入网络辅助信息在高维因子模型中获得了比经典 MLE 更快的收敛速率，属于 sharper_rate 类型的理论推进，其 joint QMLE 的渐近理论对高维似然推断有借鉴价值。

## 非参数 / 半参数  *(nonparam_semipara, 45 篇)*

### 1. [10.5705/ss.202024.0380](https://doi.org/10.5705/ss.202024.0380) — Kernel-Profile Efficient Estimation in Generalized Partially Linear Models with Missing Outcomes in Longitudinal Studies
- **作者**: Zhongzhe Ouyang, Chang Wang, Lu Wang
- **期刊/来源**: Statistica Sinica
- 相关性 9/10 · novelty: `new_theory`
- **摘要**: 本文研究纵向研究中结果变量缺失下的广义部分线性模型(GPLM)，目标是估计参数与非参数成分，假设缺失机制为MAR并利用辅助变量建模缺失概率与条件均值。提出纵向增广逆概率加权(AIPW)核-轮廓估计方程，对非参数部分使用核估计方程，对参数部分使用轮廓估计方程。所得估计量具有双重稳健性，即缺失模型或条件均值模型任一正确即可保证一致性。作者推导了该设定下的半参数有效界，并证明在多元正态假设下参数部分估计量达到该半参数有效界。模拟与 CD4 计数数据应用验证了方法的有效性。对您有用：本文将 AIPW 双重稳健与半参数效率理论结合推广至纵向缺失数据，直接契合您在纵向因果推断、半参数理论及效率界方面的核心兴趣。
- **关键技术**: `augmented inverse probability weighting (AIPW)`, `kernel estimating equation`, `profile estimating equation`, `doubly robust estimation`, `semiparametric efficiency bound`, `generalized partially linear model`
- **为什么对您有用**: 直接契合您在纵向因果推断（缺失数据）、半参数理论及效率界方面的核心兴趣；AIPW 双重稳健与半参数有效界的推导对处理纵向缺失/因果推断问题具有直接的方法论迁移价值。

### 2. [10.5705/ss.202024.0204](https://doi.org/10.5705/ss.202024.0204) — Identification and Efficient Estimation in Regression Analysis with Response Missing Not At Random
- **作者**: Qinglong Tian, Donglin Zeng, Jiwei Zhao
- **期刊/来源**: Statistica Sinica
- 相关性 9/10 · novelty: `new_theory`
- **摘要**: 在回归分析中处理 missing not at random (MNAR) 数据时，非参数缺失机制导致模型不可识别，而强参数假设虽可提升效率却牺牲稳健性。本文引入 shadow variable 解决 MNAR 下的 identifiability 问题，随后用 sieve 方法对缺失机制做非参数建模，构造半参数似然函数。所提估计量在非参数缺失机制下达到 semiparametric efficiency bound，即具有最小渐近方差。理论部分严格给出了可识别条件、半参数似然构造及效率性证明；计算上设计了 EM-type 迭代算法（含 E-step/M-step 及方差估计）。模拟与实际数据验证了方法优于现有做法。对您有用：该工作将 shadow variable identification 与 sieve 半参数效率结合，直接推进了您关注的 semiparametric efficiency bound 和非参数/半参数理论方向，且 EM 算法细节对统计计算兴趣亦有参考价值。
- **关键技术**: `shadow variable identification`, `sieve estimation`, `semiparametric likelihood`, `EM-type algorithm`, `semiparametric efficiency bound`, `MNAR missingness mechanism`
- **为什么对您有用**: 直接推进您 primary interest 中的 semiparametric efficiency bound 理论——在 MNAR 设定下用 shadow variable 放松假设并达到效率下界；sieve + EM 的计算方案也契合您对 statistical computing 的兴趣。

### 3. [10.5705/ss.202024.0298](https://doi.org/10.5705/ss.202024.0298) — Minimax Rates of Convergence for Nonparametric Regression Under Adversarial Attacks
- **作者**: Jingfu Peng, Yuhong Yang
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 本文在非参数回归设定下研究对抗攻击对模型鲁棒性影响的理论极限，目标 estimand 为受输入扰动下的回归函数，并在 adversarial sup-norm 下考察 minimax 收敛速率。作者证明对抗设定下的 minimax rate 恰好等于两项之和：标准无攻击设定下的 minimax rate，加上真实回归函数在输入扰动范围内的最大偏差。该最优速率可通过对抗性 plug-in 程序实现，即直接将标准设定下的 minimax 最优估计量代入对抗风险中。这一速率分解表明对抗误差具有可加性结构，且在当前框架下无需专门设计全新的估计器即可达到最优。对您有用：该文将经典非参数 minimax 理论拓展至对抗设定，其速率分解与 plug-in 最优性论证对您关注的非参数理论及因果推断中的敏感性分析具有直接的理论借鉴价值。
- **关键技术**: `minimax rate of convergence`, `adversarial sup-norm`, `nonparametric regression`, `adversarial plug-in procedure`, `rate decomposition`
- **为什么对您有用**: 直接推进您在“非参数理论”方向的兴趣；其 minimax 速率分解与对抗性 plug-in 最优性论证，为理解扰动下的估计极限提供了精确的数学刻画，对因果推断中的敏感性分析假设有理论借鉴意义。

### 4. [10.5705/ss.202025.0318](https://doi.org/10.5705/ss.202025.0318) — Semiparametric Analysis for Paired Comparisons with Covariates
- **作者**: Haoyue Song, Lianqiang Qu, Ting Yan, Yuguo Chen
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 在成对比较数据中，针对参数模型（如 Bradley-Terry）易受模型误设影响的问题，本文提出半参数框架，引入分布未指明的潜在随机变量刻画项目优势与协变量效应，且参数维度随项目数发散。为解决此高维半参数推断难题，作者采用基于核的最小二乘法估计未知参数。在每对项目比较次数固定而项目数趋于无穷的设定下，证明了所有估计量的一致性并推导出其渐近正态分布。这是首个在维度发散情形下对成对比较进行半参数分析的工作，模拟与 NBA 数据分析验证了其有限样本表现。对您有用：该文在维度发散下的半参数推断与渐近正态性推导，直接契合您在半参数理论与高维统计方面的兴趣，其处理潜在变量的核技巧也可为高维效率理论研究提供参考。
- **关键技术**: `semiparametric framework`, `kernel-based least squares`, `increasing dimension asymptotics`, `latent random variables`, `asymptotic normality`
- **为什么对您有用**: 直接契合您在半参数理论与高维统计方面的兴趣；在参数维度发散设定下推导渐近正态分布的理论技巧，对研究高维半参数效率与推断具有参考价值。

### 5. [10.5705/ss.202025.0148](https://doi.org/10.5705/ss.202025.0148) — Identification and Estimation of General Nonlinear Structured Latent Factor Model for Functional Data
- **作者**: Xiaorui Wang, Yimang Zhang, Jian Qing Shi
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对函数型数据提出一般非线性结构化潜因子模型，设定潜因子间存在相关性以刻画函数数据的时间依赖，并研究结构化可辨识性以保证潜因子的唯一性与物理可解释性。方法上，采用高斯过程（GP）先验估计未知非线性联系函数，并引入最近邻高斯过程（NNGP）以大幅提升计算效率。理论上，建立了潜因子与未知参数的相合性，以及未知联系函数的后验相合性。仿真与步态数据分析验证了模型的灵活性与 NNGP 的计算加速效果。对您而言，该文在非线性潜变量模型中的可辨识性证明与 NNGP 计算加速策略，可为处理高维/函数型数据中的非参数估计与计算瓶颈提供参考。
- **关键技术**: `nonlinear structured latent factor model`, `Gaussian process prior`, `nearest neighbor Gaussian process (NNGP)`, `structured identifiability`, `posterior consistency`
- **为什么对您有用**: 涉及非参数理论（GP后验相合性）与统计计算（NNGP加速），对您在非参数估计理论及高维/函数型数据计算加速方面的兴趣有参考价值。

### 6. [10.5705/ss.202024.0358](https://doi.org/10.5705/ss.202024.0358) — Estimation and Model Selection Procedures in Generalized Functional Partially Additive Hybrid Model with Diverging Number of Covariates
- **作者**: Yanxia Liu, Zhihao Wang, Yu Zhen, Wolfgang K. Härdle, Maozai Tian
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_theory`
- **摘要**: 在广义函数部分可加混合模型（GF-PAHM）下，设定响应变量受带测量误差的无穷维函数预测变量与高维标量协变量影响，且非线性成分数量随样本量发散。本文提出非凸惩罚似然估计量以实现同时变量选择与估计。核心机制在于结合函数主成分展开处理无穷维预测器，并通过非凸惩罚对发散维数的可加成分进行收缩。理论难点在于无穷维函数空间与发散维数非线性成分的交织，文中证明了估计量的选择相合性与渐近性质。模拟显示中等样本下方法有效，并应用于饼干面团数据。该文对您有用：其发散维数下部分可加模型的渐近理论推导，直接契合您对半参数理论与高维变量选择的兴趣。
- **关键技术**: `nonconvex penalized likelihood`, `functional principal component analysis`, `diverging dimensionality`, `partially additive model`, `variable selection consistency`
- **为什么对您有用**: 涉及您关注的半参数理论与高维统计，特别是发散维数下的半参数可加模型估计与变量选择，其处理无穷维与高维交织的渐近理论推导可作参考。

### 7. [10.5705/ss.202025.0221](https://doi.org/10.5705/ss.202025.0221) — Nonparametric Shrinkage Estimation in High Dimensional Glms via Polya Trees
- **作者**: Asaf Weinstein, Jonas Wallin, Daniel Yekutieli, Malgorzata Bogdan
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在高维 GLM（固定效应）设定下，本文研究不依赖稀疏性假设的通用最优正则化估计，estimand 为系数向量本身。作者首先构造一个 oracle Bayes 估计量——对系数向量的所有排列赋予等权先验，使其仅依赖真实系数的经验 CDF，并在 frequentist 与 Bayesian 框架下证明其最优性。为实现该 oracle 估计，构建层次 Bayes 模型：将各系数视为 i.i.d. 抽自共同分布 G，对 G 赋予 Polya tree 先验以反映对分布形状的不确定性。理论表明 G 的后验均值能非参数地自适应真实系数的经验 CDF，系数后验均值从而逼近 oracle 估计量。数值实验显示，相比 L_p 正则化、penalized-likelihood 及其他 Bayesian 高维回归方法，该方法在估计与预测精度上均有优势。对您有用：该工作在 high-dimensional regression 中放弃稀疏性假设、改用 Polya tree 非参数先验自适应系数分布的思路，与您在 semiparametric/nonparametric theory 和 high-dimensional statistics 方向的兴趣直接相关，为不依赖 sparsity 的高维推断提供了新路径。
- **关键技术**: `Polya tree prior`, `oracle Bayes estimator`, `permutation-invariant prior`, `hierarchical Bayes model`, `nonparametric shrinkage`, `empirical CDF adaptation`
- **为什么对您有用**: 该工作在高维 GLM 中用 Polya tree 非参数先验替代稀疏性假设，与您在 semiparametric/nonparametric theory 和 high-dimensional statistics 的兴趣直接对接；不依赖 sparsity 的 shrinkage 思路可为高维效率理论与 debiased 方法提供新视角。

### 8. [10.5705/ss.202024.0320](https://doi.org/10.5705/ss.202024.0320) — Model-free Multivariate Change Point Detection and Localization with Statistical Guarantee
- **作者**: Xin Xing, Zuofeng Shang, Hongyu Miao, Pang Du
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_theory`
- **摘要**: 本文在多变量变点检测设定下，基于再生核希尔伯特空间（RKHS）的非参数密度估计，研究无模型变点识别与定位问题。针对现有非参数检验依赖无穷统计量序列导致渐近行为受限的缺陷，作者构造了基于非参数密度估计的 CUSUM 似然比检验统计量。理论方面，建立了非参数密度估计的完整非渐近（non-asymptotic）理论框架，实现了 I 类错误的渐近控制，并证明了变点定位的最优收敛速率。该方法在 RKHS 框架下统一了变点检测的检验与估计，对您研究非参数理论中的非渐近分析及假设检验的最优性有直接参考价值。
- **关键技术**: `RKHS density estimation`, `CUSUM likelihood ratio test`, `non-asymptotic theory`, `optimal localization rate`, `change point detection`
- **为什么对您有用**: 直接契合您在非参数理论和假设检验方面的 primary interests；其基于 RKHS 的非渐近理论框架和最优收敛速率的推导，对您理解非参数检验的有限样本性质和最优性有重要参考价值。

### 9. [10.5705/ss.202023.0143](https://doi.org/10.5705/ss.202023.0143) — Sufficient Dimension Reduction for Classification
- **作者**: Xin Chen, Jingjing Wu, Zhigang Yao, Jia Zhang
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对高维分类问题提出了一种新的充分降维（SDR）方法——最大均值方差（MMV），在预测变量与多分类响应变量的依赖性度量下进行 model-free 降维，无需估计联系函数。MMV 基于 Cui et al. (2015) 的均值方差指数，通过最大化该指数来寻找中心降维子空间。理论方面，在固定和发散维度 p（甚至 n<p）以及类别数发散的设定下，证明了 MMV 估计量的相合性；在固定 p 下建立了估计量的渐近正态性。模拟与实证表明该方法在 n<p 时分类效率有显著提升。对您而言，该文在发散参数下的渐近理论推导和 model-free 降维思路，可为处理高维半参数模型中的降维与推断问题提供参考。
- **关键技术**: `sufficient dimension reduction`, `mean variance index`, `diverging dimension asymptotics`, `model-free estimation`, `asymptotic normality`
- **为什么对您有用**: 本文属于半参数/非参数理论和高维统计的交叉，其发散维度下的相合性与渐近正态性证明，对您研究高维半参数效率理论及降维后的推断具有直接参考价值。

### 10. [10.5705/ss.202025.0207](https://doi.org/10.5705/ss.202025.0207) — A Model-free Correlation Coefficient for Censored Data
- **作者**: Linlin Dai, Tengfei Li, Kani Chen
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 在右删失生存数据设定下，针对传统 Cox 模型无法捕捉非线性或非单调关联的问题，本文提出一种无需模型假设的依赖度量及其估计量——删失秩相关系数（CRC）。CRC 取值于 [0,1]，当且仅当变量独立时为 0，当且仅当存在可测函数关系时为 1，且不依赖变量的边际分布。该估计量具有强相合性与渐近正态性，计算复杂度为 O(n log n)，并可通过 power-consistent 的置换检验进行独立性假设检验。模拟与 ADNI 阿尔茨海默病真实数据表明，CRC 在检测非线性关联及重度删失场景下优于 Cox 模型等方法。对您有用：该文构造非参数依赖度量与独立性检验的渐近理论，直接契合您在非参数理论与假设检验方面的兴趣，其 O(n log n) 算法设计也具计算参考价值。
- **关键技术**: `rank-based correlation`, `model-free dependence measure`, `permutation test`, `asymptotic normality`, `right-censored survival data`
- **为什么对您有用**: 提出了全新的非参数依赖度量与独立性检验方法，直接契合您在非参数理论与假设检验方面的核心兴趣；同时 ADNI 真实数据应用对流行病学方向的关联分析有参考价值。

### 11. [10.5705/ss.202025.0144](https://doi.org/10.5705/ss.202025.0144) — Conditional Density Estimation with Deep Neural Networks
- **作者**: Chenxuan He, Yuan Gao, Liping Zhu, Jian Huang
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `sharper_rate`
- **摘要**: 在非参数条件密度估计问题中，目标是在无参数假设下估计条件密度 f(y|x)，作者提出基于深度神经网络（DNN）的非参数最小二乘方法。将条件密度估计建模为 L2 损失下的非参数最小二乘问题，利用 DNN 的逼近能力拟合条件密度函数，避免了 restrictive parametric 假设。证明了该方法在一般设定下达到 minimax 最优收敛速率。进一步证明，当高维数据满足低维流形假设时，收敛速率的维度依赖可从原始协变量维度降至流形内在维度，显著改善高维 curse of dimensionality。数值实验（模拟与真实数据）表明该方法一致优于 KDE、sieve 等已有方法。对您有用：直接关联您 primary interest 中的非参数理论与高维统计——minimax rate 的建立和流形假设下的速率改善为高维非参数推断提供了理论基准，且非参数最小二乘框架可与 semiparametric efficiency / debiased ML 的正交化思路结合。
- **关键技术**: `deep neural network approximation`, `nonparametric least squares`, `minimax convergence rate`, `low-dimensional manifold assumption`, `conditional density estimation`, `L2 loss regression`
- **为什么对您有用**: 直接推进您 primary interest 中的非参数理论：建立了 DNN 条件密度估计的 minimax 最优速率，并在流形假设下给出 sharper rate，为高维非参数推断提供理论基准；非参数最小二乘框架可迁移至 semiparametric 效率理论中的 nuisance estimation。

### 12. [10.5705/ss.202024.0234](https://doi.org/10.5705/ss.202024.0234) — Estimation and Inference of Change Points in Functional Regression Time Series
- **作者**: Shivam Kumar, Haotian Xu, Haeran Cho, Daren Wang
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在函数线性回归时间序列中，研究斜率函数发生变点时的变点估计与推断问题，模型允许函数协变量与测量误差存在时间依赖及重尾。提出 FRBS（Functional Regression Binary Segmentation）算法，在 RKHS 框架下利用分段常数函数线性回归的预测能力实现多重变点检测一致性，且计算高效。进一步提出精炼步骤改善初始估计的定位速率，并在由变点幅度决定的两种 regime 下推导精炼估计量的渐近分布。为基于极限分布构造变点置信区间，提出一致的 block-type 长期方差估计量。实证部分通过模拟与 S&P 500 数据验证方法有效性。对您而言，该文在 RKHS 框架下的变点渐近推断（两种 regime 的极限分布、置信区间构造）与您对 semiparametric theory 和 hypothesis testing 的兴趣直接相关，其处理时间依赖与重尾的技术思路可迁移至其他依赖结构下的 inference 问题。
- **关键技术**: `binary segmentation`, `RKHS framework`, `functional linear regression`, `change point asymptotic distribution`, `block long-run variance estimator`, `localization rate refinement`
- **为什么对您有用**: RKHS 框架下的变点渐近推断（两种 regime 极限分布、置信区间）直接关联您对 semiparametric theory 和 hypothesis testing 的兴趣；处理时间依赖与重尾的技术可迁移至其他依赖结构下的 inference 场景。

### 13. [10.5705/ss.202024.0104](https://doi.org/10.5705/ss.202024.0104) — A Semiparametric Quantile Single-Index Model for Zero-Inflated and Overdispersed Outcomes
- **作者**: Zirui Wang, Tianying Wang
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `weaker_assumption`
- **摘要**: 针对微生物组数据中常见的零膨胀与过度分散特征，在放弃零膨胀泊松/负二项等强参数假设的设定下，目标是估计半参数单指标分位数回归模型的指标系数与分位数曲线。提出半参数单指标分位数回归，允许关联函数形式灵活且适应不同个体的零比例，从而放松了现有零膨胀模型的参数分布限制。理论上建立了指标系数估计量与分位数回归曲线估计的渐近性质（如一致性、渐近正态性）。模拟表明该半参数方法在模型拟合上优于传统参数方法。该文是典型的半参数理论工作，其放松参数假设并推导渐近性质的思路，对您在 semiparametric theory 方向的研究有直接参考价值。
- **关键技术**: `semiparametric single-index model`, `quantile regression`, `zero-inflated outcomes`, `asymptotic normality`, `overdispersion modeling`
- **为什么对您有用**: 直接对应您 primary interest 中的 semiparametric theory，展示了如何在非标准数据结构（零膨胀）下放松参数假设并严格推导估计量的渐近性质，理论推导框架可借鉴。

### 14. [10.5705/ss.202025.0120](https://doi.org/10.5705/ss.202025.0120) — Estimation of Piecewise Continuous Regression Function in Finite Dimension using Oblique-axis Regression Tree with Applications in Image Denoising
- **作者**: Subhasish Basak, Anik Roy, Partha Sarathi Mukherjee
- **期刊/来源**: Statistica Sinica
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在固定设计点设定下，本文研究有限维分段连续回归函数的估计问题，核心 estimand 为保留二维回归函数中跳跃位置曲线（JLCs）复杂形状的回归曲面。提出斜轴回归树（ORT），通过递归树划分对局部像素强度聚类，并基于局部叶节点平均估计回归函数。与传统分段常数树不同，ORT 能有效保留 JLCs 的复杂几何结构。理论分析采用了与现有回归树文献不同的底层回归函数假设与证明框架。图像去噪实验显示其在去噪与边缘保留间的良好平衡。对您而言，本文扩展了非参数回归树的理论边界，但其固定设计假设与图像处理导向对您关注的因果/高维/效率等核心方向的直接迁移价值有限。
- **关键技术**: `Oblique-axis Regression Tree`, `piecewise continuous regression`, `jump location curves`, `recursive tree partitioning`, `fixed design regression`
- **为什么对您有用**: 涉及非参数回归理论（分段连续函数估计与新型树方法），与您 primary interest 中的非参数理论有交集，但固定设计假设和图像去噪应用场景与因果推断/高维统计距离较远，理论迁移价值一般。

### 15. [10.5705/ss.202023.0017](https://doi.org/10.5705/ss.202023.0017) — Multiscale Autoregression on Adaptively Detected Timescales
- **作者**: Rafal Baranowski, Yining Chen, Piotr Fryzlewicz
- **期刊/来源**: Statistica Sinica
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文提出自适应多尺度自回归模型（AMAR），对大阶数 AR 模型进行自适应正则化：回归元取为过程在多个时间尺度上的近期均值，尺度数量与跨度均未知，通过变点检测技术从数据中估计。模型设定允许最长尺度随样本量增长，理论给出了变点估计一致性及 AR 系数的渐近性质。核心机制是将大阶数 AR 的滞后项按多尺度局部均值分组，等价于一种数据驱动的分组/收缩正则化，兼顾可解释性与灵活性。模拟显示 AMAR 在大阶数场景下优于朴素 AR 及 Lasso 型正则化；扩展至 AMVAR 并在英美失业率数据上验证。对您而言，该文的数据驱动分组正则化思路可迁移至高维纵向/时间序列因果推断中的 nuisance 估计，且变点检测与假设检验方向直接相关。
- **关键技术**: `change-point detection`, `multiscale local averaging`, `adaptive regularization of large-order AR`, `vector autoregression extension`, `wild binary segmentation`
- **为什么对您有用**: 大阶数 AR 的自适应分组正则化与您的高维统计兴趣相通；变点检测部分与假设检验方向直接相关；AMVAR 扩展可为经济时间序列因果分析提供可迁移的工具。

### 16. [10.5705/ss.202025.0389](https://doi.org/10.5705/ss.202025.0389) — Conformal Inference for Missing Data Under Multiple Robust Learning
- **作者**: Wenlu Tang, Hongni Wang, Xingcai Zhou, Bei Jiang, Linglong Kong
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在 Missing at Random (MAR) 设定下，本文研究缺失数据的 conformal prediction 问题，目标是构造边际与条件覆盖均可靠的预测区间。提出 CM-MRL 方法：将 split conformal calibration 与多重稳健经验似然 (EL) 重加权结合，通过对 complete-case conformity scores 做 EL 重加权实现双重校准，使其分布匹配 MAR 隐含的全样本校准分布。核心理论工具为经验过程理论，证明了估计量的渐近性质、预测区间的边际与条件覆盖保证，以及区间长度占优结果。多重稳健性意味着即使部分工作模型误设，方法仍保持覆盖有效性。数值实验验证了方法在缺失数据下的表现。对您有用：多重稳健 EL 重加权是 doubly/multiply robust 估计在 conformal inference 中的自然推广，与您在因果推断中 IPW/DR 估计及半参数效率理论的兴趣直接相关。
- **关键技术**: `split conformal prediction`, `multiple robust empirical likelihood`, `double calibration`, `missing at random`, `empirical process theory`, `interval-length dominance`
- **为什么对您有用**: 多重稳健 EL 重加权是因果推断中 doubly robust 思想在 conformal inference 的推广，与您 primary interest 中的因果推断 (IPW/DR 估计) 和半参数效率理论直接相连；覆盖保证与区间长度占优结果对假设检验与推断有参考价值。

### 17. [10.5705/ss.202025.0156](https://doi.org/10.5705/ss.202025.0156) — Conformal Prediction Under Nonignorable Missingness
- **作者**: Menghan Yi, Yingying Zhang, Yanlin Tang, Huixia Judy Wang
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在非可忽略缺失(nonignorable missing)响应下，本文研究如何构建模型无关的预测集，核心 estimand 为条件预测集及其覆盖保证，关键假设为倾向得分(propensity score)可被一致估计。针对非可忽略缺失带来的两大挑战——不可识别性与数据不可交换性，作者提出利用目标点附近局部子集构建最高条件密度预测集，并通过倾向得分加权修正选择偏差。具体地，发展了一种偏差调整的半参数条件密度估计方法：先对观测数据拟合分位数过程，再用倾向得分权重做偏差校正；该估计量无缝嵌入 conformal 框架，同时保证边际覆盖、局部覆盖与渐近条件覆盖，且区间长度渐近最优。模拟与 HIV-CD4 真实数据验证了方法的有效性。对您有用：该文将倾向得分加权（因果推断/缺失数据核心工具）与 conformal prediction 结合，半参数条件密度估计的偏差校正思路可迁移至您关注的 semiparametric efficiency 与 sensitivity analysis 场景。
- **关键技术**: `conformal prediction`, `propensity score weighting`, `semiparametric conditional density estimation`, `quantile process fitting`, `nonignorable missing data`, `local highest density prediction set`
- **为什么对您有用**: 将因果推断中处理选择偏差的倾向得分加权技术引入 conformal prediction，半参数条件密度估计的偏差校正框架对您关注的 semiparametric efficiency 与缺失数据下 sensitivity analysis 有直接迁移价值；HIV-CD4 数据集也可作为流行病学应用的参考案例。

### 18. [10.5705/ss.202024.0402](https://doi.org/10.5705/ss.202024.0402) — Robust Mean Signal Estimation and Inference for Imaging Data
- **作者**: Yang Long, Guanqun Cao, David Kepplinger, Lily Wang
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在 contaminated functional data 框架下，本文目标是含噪成像数据中均值信号函数的稳健估计与推断，假设数据存在污染点、空间依赖及不规则区域。提出基于三角剖分上双变量 penalized spline 的 robust smoothed M-estimator，通过 M-estimation 的稳健性与 roughness penalty 的空间平滑性同时应对污染与空间相关性。在正则条件下建立了均值函数估计量的 L₂ 收敛速率，并证明其渐近正态性；进一步构造了均值信号的 simultaneous confidence corridor，实现整体推断与显著效应定位。模拟与脑成像数据应用验证了方法有效性。对您有用之处在于：M-estimator 在不规则域上的收敛速率与渐近正态性结果、以及 simultaneous confidence corridor 的构造思路，可直接迁移到非参数理论中函数型数据的推断问题。
- **关键技术**: `bivariate penalized splines over triangulation`, `robust M-estimation`, `L2 convergence rate`, `asymptotic normality`, `simultaneous confidence corridor`, `contaminated functional data`
- **为什么对您有用**: 本文属于非参数理论范畴，M-estimator 的收敛速率与渐近正态性结果以及 simultaneous confidence corridor 构造方法，对您在非参数推断与假设检验方向的研究有直接参考价值；三角剖分上 penalized spline 的计算实现也对统计计算方向有借鉴意义。

### 19. [10.5705/ss.202024.0256](https://doi.org/10.5705/ss.202024.0256) — Asymptotic Theory for Linear Functionals of Kernel Ridge Regression
- **作者**: Rui Tuo, Lu Zou
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在 RKHS 等价于 Sobolev 空间的设定下，本文研究核岭回归预测函数的线性泛函（点估计、导数估计、L₂ 内积等）的渐近理论。核心发现是：为平衡方差与 worst-case bias，平滑参数 λ∼n⁻¹ 是泛函估计的通用最优阶，而非传统最小化 L₂ 误差的最优阶 λ∼n^{-2m/(2m+d)}。作者建立了估计的上下界及渐近正态性，并由此推出在 λ∼n⁻¹log n 下可达到核岭回归的最优 L∞ 误差。该结果对您有用：直接推进了非参数理论中泛函估计的渐近分布与最优调节参数选择，与您关注的 semiparametric efficiency 及 nonparametric theory 子方向紧密相关。
- **关键技术**: `kernel ridge regression`, `reproducing kernel Hilbert space`, `Sobolev space equivalence`, `asymptotic normality of linear functionals`, `worst-case bias-variance tradeoff`, `optimal smoothing parameter selection`
- **为什么对您有用**: 直接推进非参数泛函估计的渐近正态性与最优调节参数理论，与您 primary interest 中的 semiparametric/nonparametric theory 和 efficiency theory（泛函的 influence function 与最优收敛率）高度相关；λ∼n⁻¹ 的通用最优阶结果可迁移到您关注的 debiased ML / semiparametric 估计中核方法的 tuning 选择。

### 20. [10.5705/ss.202025.0187](https://doi.org/10.5705/ss.202025.0187) — Inference for A Two-Step Joint Model of Extreme Quantile and Expected Shortfall Regression
- **作者**: Qingzhao Zhong, Jingyu Ji, Liujun Chen, Yanxi Hou, Deyuan Li
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究极值水平下条件期望短缺（ES）与分位数联合回归模型的推断问题，克服了尾部观测稀疏带来的估计挑战。作者提出一种两步联合建模框架，结合极值理论与半参数方法处理尾部外推，并推导了估计量的渐近性质与影响函数。该方法有效解决了极值ES回归的推断难题，提供了严密的数学统计保证。对您而言，该文在半参数尾部推断与经济风险建模的交叉处提供了新思路，其处理稀疏尾部的半参数技巧可迁移至其他极值因果或推断场景。
- **关键技术**: `Expected Shortfall regression`, `extreme quantile regression`, `two-step estimation`, `semiparametric inference`, `influence function`
- **为什么对您有用**: 涉及半参数推断理论与经济金融中的风险建模，其处理尾部稀疏数据的推断方法对您在半参数理论和经济理论应用方面的研究有借鉴意义。

### 21. [10.5705/ss.202025.0151](https://doi.org/10.5705/ss.202025.0151) — Variable Selection and Minimax Prediction in High-dimensional Functional Linear Models
- **作者**: Xingche Guo, Yehua Li, Tailen Hsing
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `sharper_rate`
- **摘要**: 在超高维泛函线性模型中（协变量为无穷维函数，p 可超维），本文研究未知系数函数属于 RKHS 时的变量选择与预测问题。方法上，对系数函数的 RKHS 范数施加 group elastic-net 惩罚，并证明损失函数的 Gateaux 次可微性及估计量在乘积 RKHS 中的唯一存在性。理论方面，在稀疏性与泛函不可表示条件下，推导出变量选择相合性的非渐近尾部界。进一步，允许真实预测变量数 q 随样本量发散，后选择精炼估计量可达 oracle minimax 最优预测率。实证通过模拟与 Human Connectome Project 数据验证。对您有用：本文将高维变量选择与非参数 RKHS 理论结合，其非渐近界与 minimax rate 的推导思路可直接迁移至您关注的高维统计与半参数/非参数效率理论研究中。
- **关键技术**: `functional linear model`, `RKHS regularization`, `group elastic-net`, `non-asymptotic tail bound`, `oracle minimax rate`, `functional irrepresentable condition`
- **为什么对您有用**: 直接涉及您 primary interest 中的高维统计与半参数/非参数理论；其 RKHS 惩罚下的非渐近界与 oracle minimax rate 结果，为您在高维泛函数据下的效率理论推导提供了可迁移的理论工具。

### 22. [10.5705/ss.202024.0294](https://doi.org/10.5705/ss.202024.0294) — Uncertainty Quantification for Large-Scale Deep Neural Networks via Post-StoNet Modeling
- **作者**: Yan Sun, Faming Liang
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 针对大规模深度神经网络（DNN）预测的不确定性量化（UQ）问题，本文提出一种后处理方法：将预训练 DNN 最后一层隐藏层输出输入到随机神经网络（StoNet）中。该方法在验证集上对 StoNet 施加稀疏惩罚（sparse penalty）进行训练，并据此构建未来观测的预测区间。理论上，文章证明了稀疏 StoNet 的参数估计一致性，这是保证预测区间有效性的核心条件。StoNet 框架提供了一个平台，使得线性模型中的稀疏学习理论和方法能够直接迁移到 DNN 的 UQ 中。实验表明，相比 conformal 方法，该方法能构建更短的诚实置信区间，且校准效果优于其他后处理校准技术。对您有用：该文将高维稀疏学习引入 DNN 的 UQ，其参数一致性证明和 StoNet 建模思路对您在非参数/半参数理论及高维统计中的研究有方法论迁移价值。
- **关键技术**: `stochastic neural network (StoNet)`, `sparse penalty`, `parameter estimation consistency`, `prediction interval`, `post-hoc calibration`, `conformal prediction`
- **为什么对您有用**: 将高维稀疏学习理论迁移至 DNN 不确定性量化的思路，以及 StoNet 参数一致性证明，对您在非参数/半参数理论和高维统计方向的研究具有直接的方法论迁移价值。

### 23. [10.5705/ss.202024.0253](https://doi.org/10.5705/ss.202024.0253) — Predictive Distributions and the Transition from Sparse to Dense Functional Data
- **作者**: Álvaro Gajardo, Xiongtao Dai, Hans-Georg Müller
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在稀疏纵向数据的功能主成分分析(FPCA)框架下，目标是将每个个体的噪声纵向观测映射到 FPC scores 的多元高斯预测分布，并研究从稀疏(纵向)到密集(功能)采样过渡时预测分布的收敛性质。核心机制：在 Gaussian 假设下证明预测分布向真实 FPC 的点测度收缩(shrinkage)，并将结果扩展到截断点 K=K(n) 随样本量发散的 K-截断预测分布情形。针对功能线性模型中稀疏纵向预测变量下点预测非一致性的问题，构建预测分布并推导真实与估计预测分布之间 2-Wasserstein 距离的渐近收敛速率。实证部分使用 Baltimore Longitudinal Study of Aging 数据展示。该工作在纵向数据的非参数理论框架下给出了 Wasserstein 收敛率，与您关注的 longitudinal causal inference 和 semiparametric efficiency 理论有方法论上的联系，且 BLSA 数据集对流行病学应用有参考价值。
- **关键技术**: `functional principal component analysis`, `predictive distribution`, `2-Wasserstein metric`, `K-truncated FPC expansion`, `sparse-to-dense transition`, `functional linear model`
- **为什么对您有用**: 纵向数据的非参数渐近理论与您 primary interest 中的 longitudinal causal inference 和 semiparametric efficiency 有方法论交叉；Wasserstein 收敛率的分析思路可迁移到您关注的分布al推断/敏感性分析问题；BLSA 数据集对 epidemiology secondary interest 有直接参考价值。

### 24. [10.5705/ss.202024.0414](https://doi.org/10.5705/ss.202024.0414) — GROS: A General Robust Aggregation Strategy
- **作者**: Alejandro Cholaquidis, Emilien Joly, Leonardo Moreno
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在一般度量空间设定下，本文提出 GROS（General Robust Aggregation Strategy），将样本分为 K 组、各组独立计算估计量后，通过度量空间上的极小化问题进行鲁棒聚合，目标 estimand 为度量空间中的任意位置参数。方法推广了 median-of-means 思路：作者证明 GROS 估计量满足 sub-Gaussian 浓度不等式，并给出 Donoho 意义下的 breakdown point；关键技术工具为经验过程与度量空间上的集中不等式。核心计算贡献：将极小化从整个度量空间限制到样本点上，sub-Gaussian 性质仅损失常数因子，使方法实际可行。模拟涵盖 k-means 分类、多臂老虎机、回归、噪声集合估计及鲁棒持久图。对您而言，sub-Gaussian 浓度界与 breakdown point 的严格推导属于数学统计范畴，样本级极小化的计算可行性结果直接关联统计计算兴趣。
- **关键技术**: `median-of-means aggregation`, `sub-Gaussian concentration inequality`, `Donoho breakdown point`, `metric space minimization`, `robust persistent diagram`
- **为什么对您有用**: 严格证明 sub-Gaussian 浓度界与 breakdown point 属于数学统计核心问题，样本级极小化保持常数倍 sub-Gaussian 性的计算可行性结果直接对接统计计算兴趣；鲁棒聚合框架可迁移至高维/半参数估计的稳健推断场景。

### 25. [10.5705/ss.202025.0076](https://doi.org/10.5705/ss.202025.0076) — Nonparametric Inference on Treatment-biomarker Interaction Based on Probability Index
- **作者**: Zehui Wang, Yanglei Song, Wenyu Jiang, Dongsheng Tu
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在精准医学设定下，本文基于概率指数（probability index）提出非参数的处理-生物标志物交互作用度量，以评估按生物标志物二分亚组的处理效应差异。当截断点预定时，使用 Wilcoxon 型统计量检验无交互作用的原假设；当截断点未预定时，取 Wilcoxon 型统计量在截断点范围上的上确界进行检验，p 值通过 bootstrap 计算。理论证明两种情况下检验的水平均收敛到名义水平。对于未预定截断点，提出极大化处理效应差异的 profile 估计量，证明其具有 n^{-1/3} 立方收敛速率且渐近服从缩放 Chernoff 分布。此外，引入 m-out-of-n bootstrap 估计渐近分布中的未知缩放因子。对您有用：该文将非参数假设检验与处理效应异质性结合，其关于立方收敛速率与 Chernoff 分布的理论推导对您在非参数理论及因果推断异质性分析有直接参考价值。
- **关键技术**: `probability index`, `Wilcoxon-type statistic`, `supremum test`, `cubic-rate convergence`, `Chernoff's distribution`, `m-out-of-n bootstrap`
- **为什么对您有用**: 本文结合了因果推断中的处理效应异质性与非参数假设检验，其关于 profile 估计量的 n^{-1/3} 立方收敛速率及 Chernoff 分布的理论推导，对您在非参数理论和假设检验方面的研究有直接的方法论参考价值。

### 26. [10.5705/ss.202025.0294](https://doi.org/10.5705/ss.202025.0294) — Estimation of Conditional Extremiles in Reproducing Kernel Hilbert Spaces with Application to Large Commercial Banks Data
- **作者**: Fang Chen, Caixing Wang
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在多协变量存在的情况下，研究条件极值（conditional extremiles）的非参数估计问题，目标是在重尾分布下实现高风险水平的可靠外推。方法结合再生核希尔伯特空间（RKHS）与分位数回归过程逼近，灵活建模条件极值结构。理论方面，作者建立了估计误差的非渐近误差界（non-asymptotic error bound），严格证明了方法在重尾设定下的理论有效性。相比传统极值估计，该框架通过 RKHS 正则化有效利用了辅助协变量信息，提升了极端尾部模式的捕捉与外推能力。实证部分将方法应用于大型商业银行数据，展示了其在金融风险度量中的实用性。对您而言，该文的 RKHS 非参数估计技巧及非渐近界推导，可直接迁移至您关注的非参数/半参数理论及经济数据应用中。
- **关键技术**: `conditional extremiles`, `reproducing kernel Hilbert spaces (RKHS)`, `quantile regression process approximation`, `non-asymptotic error bound`, `heavy-tailed extrapolation`
- **为什么对您有用**: 直接关联您的非参数/半参数理论兴趣（RKHS 估计与非渐近界推导），同时其商业银行数据应用契合您对经济理论（数据集与应用）的次级兴趣，可提供重尾数据下非参数推断的思路借鉴。

### 27. [10.5705/ss.202024.0345](https://doi.org/10.5705/ss.202024.0345) — Temporally-Evolving Generalised Networks and Their Reproducing Kernels
- **作者**: Tobia Filosi, Claudio Agostinelli, Emilio Porcu
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究时变广义网络上的随机场建模问题，设定为边非线性、随机过程同时以顶点和边为连续指标、且拓扑结构（顶点/边的出现与消失、边的形状与长度）随时间变化的网络。作者为这类时变网络建立了严格的数学框架，分别考虑线性时间与周期性（圆形）时间两种情形，并比较了各自的优劣。核心贡献是构造了适用于时变拓扑结构的半距离（semi-distance），使广义网络成为半距离空间，进而通过半距离与核函数的复合，指导如何在时变网络上构建随机场的协方差核。技术工具主要依赖 RKHS 理论与度量空间构造，但未涉及估计效率或收敛率结果。对您而言，RKHS 与半距离构造的框架可迁移性有限，除非您关注网络结构上的非参数协方差建模或空间统计中的核方法。
- **关键技术**: `reproducing kernel Hilbert space`, `semi-distance construction`, `graphs with Euclidean edges`, `spatiotemporal covariance kernel`, `random fields on networks`
- **为什么对您有用**: 与您 primary interest 中 semiparametric/nonparametric theory 的 RKHS 部分有微弱连接，但本文聚焦空间统计中协方差核构造而非估计效率或 inference，迁移价值较低。

### 28. [10.5705/ss.202024.0181](https://doi.org/10.5705/ss.202024.0181) — Mean Independent Component Analysis for Multivariate Time Series
- **作者**: Chung Eun Lee, Zeda Li
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多元时间序列设定下，本文提出均值独立成分分析（Mean ICA），通过同期线性变换寻找单变量均值独立成分，使各成分可分别建模，无需参数模型或分布假设。核心估计工具为鞅差散度（MDD），以此最小化跨成分与跨时间的均值依赖；框架统一处理固定维度与发散维度两种情形，并在两种设定下均建立估计量一致性。进一步将方法推广至分组均值独立成分分析，并提出未知分组结构的识别方法。主要理论贡献为固定与发散维度下的一致性结果，模拟与社区流动性真实数据验证了方法效果。对您而言，MDD 作为 U-统计量型依赖度量与高阶 U-统计量理论直接相关，发散维度下的非参数降维一致性也对高维统计方向有参考价值。
- **关键技术**: `martingale difference divergence`, `mean independent component analysis`, `contemporaneous linear transformation`, `diverging dimension consistency`, `group structure identification`, `nonparametric dependence measure`
- **为什么对您有用**: 鞅差散度本质是 U-统计量型依赖度量，与您的高阶 U-统计量兴趣直接相关；发散维度下的非参数降维一致性证明对高维统计与非参数理论方向有可迁移的理论技巧。

### 29. [10.5705/ss.202024.0349](https://doi.org/10.5705/ss.202024.0349) — Intrinsic Functional Sliced Inverse Regression on Riemannian Manifolds and Wasserstein Spaces
- **作者**: Xinyu Li, Jianjun Xu
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `sharper_rate`
- **摘要**: 本文针对 Riemannian 流形与 Wasserstein 空间上的函数型预测变量与标量响应，提出了一种内在函数切片逆回归模型，目标是对数泛函中心子空间的估计与推断。沿 Fréchet 均值曲线定义对数映射后，作者在内在几何框架下发展了基于截断的估计程序并建立其渐近性质。关键在于，利用 Wasserstein 空间的平坦性，该方法可识别最优截断数，从而使对数泛函中心子空间估计达到 minimax 最优收敛速率。模拟与实证分析验证了有限样本表现。对您有用：该文在非欧流形上推导充分降维的 minimax rate，对您关注的非参数理论及收敛速率分析有直接参考价值。
- **关键技术**: `sliced inverse regression`, `Riemannian manifold`, `Wasserstein space`, `Frechet mean`, `minimax optimal convergence rate`, `sufficient dimension reduction`
- **为什么对您有用**: 论文在非参数充分降维框架下推导了 Wasserstein 空间上的 minimax 最优收敛速率，直接契合您对非参数理论与 minimax rate 的兴趣，且其流形上的对数映射与截断估计技术可迁移至其他复杂结构数据的半参数/非参数推断。

### 30. [10.5705/ss.202024.0371](https://doi.org/10.5705/ss.202024.0371) — On a Flexible Generalized Model Averaging Forecasting of Nonlinear Time Series
- **作者**: Rong Peng, Zudi Lu, Fangsheng Ge
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在非线性时间序列预测中，针对多滞后变量非参数回归的维数诅咒及非高斯/离散响应的建模困难，本文提出半参数广义边际预测模型平均（GMAFMA）框架。该框架基于灵活的条件指数族分布，通过边际预测的加权组合规避维数诅咒，并统一处理连续与离散型非高斯数据。估计方面，采用半参数条件似然方法求解边际预测的组合权重，在温和的时间序列生成条件下证明了权重的渐近正态性。此外，提出自适应惩罚 PGMAFMA 以筛选重要边际预测，提升模型可解释性与预测精度。对您而言，该文在半参数似然推断与渐近正态性证明上的技术细节可作参考，尽管其预测导向与您的因果推断主方向不同，但边际建模组合思路对高维降维有一定启发。
- **关键技术**: `semiparametric conditional likelihood`, `model averaging`, `marginal forecasting`, `asymptotic normality`, `adaptive penalization`
- **为什么对您有用**: 虽然核心是时间序列预测，但其半参数条件似然推断与渐近正态性推导属于您的半参数理论兴趣范畴；边际建模组合思路对克服高维诅咒有参考价值。

### 31. [10.5705/ss.202024.0003](https://doi.org/10.5705/ss.202024.0003) — Rank-Based Inference for the Accelerated Failure Time Model with Partially Interval-Censored Data
- **作者**: Taehwa Choi, Sangbum Choi, Dipankar Bandyopadhyay
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究部分区间删失数据下加速失效时间(AFT)模型的秩基推断问题，目标参数为回归系数，无需对残差分布做参数假设。基于加权log-rank检验思想构造Gehan型单调估计函数，并推广至一般秩基估计函数类；估计量通过线性规划求解，利用经验过程理论证明一致性与渐近正态性。与基于最大似然的区间删失回归方法不同，该途径避免了对残差分布函数的复杂非参估计，直接给出回归系数估计及高效方差估计。方法进一步推广至多变量聚类部分区间删失数据的线性回归，模拟与结直肠癌数据示例验证了有限样本表现。对您而言，秩基估计函数的构造与经验过程渐近性证明可为semiparametric theory方向提供方法参考，结直肠癌流行病学数据集亦具secondary interest应用价值。
- **关键技术**: `rank-based estimating function`, `Gehan-type monotone estimator`, `weighted log-rank test`, `empirical process theory`, `linear programming estimation`, `interval censoring`
- **为什么对您有用**: 秩基估计的构造与经验过程渐近理论证明路径与您semiparametric theory方向直接相关；部分区间删失设定下的方差估计程序对效率理论有参考价值；结直肠癌数据集对epidemiology应用方向有数据集价值。

### 32. [10.5705/ss.202024.0167](https://doi.org/10.5705/ss.202024.0167) — On Efficient Estimation for Value-at-Risk via Location-Scale Time Series Models
- **作者**: Chaoxu Lei, Qianqian Zhu
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在 location-scale 时间序列框架下，本文研究 Value-at-Risk (VaR) 的高效估计，提出半参数与参数复合分位数回归 (CQR) 方法，前者不假设创新分布，后者假设创新具有参数分位数函数。半参数 CQR 通过聚合多分位数水平信息，相比传统分位数回归提升了估计效率；参数 CQR 则在估计高条件分位数（数据稀疏场景）时进一步利用参数结构增强效率。理论上，本文建立了两种 CQR 估计量在 ARMA-GARCH、双自回归及 NAR-GARCH 模型下的渐近性质，并推导了它们与高斯/指数 QMLE 的渐近相对效率。结论表明半参数 CQR 在放宽分布假设下仍具效率优势，而参数 CQR 在尾部估计中效率增益显著。对您有用：该文在半参数模型下的效率对比与渐近性质推导，直接契合您对 semiparametric efficiency theory 的兴趣，且 VaR 估计属于经济理论中的典型应用场景。
- **关键技术**: `composite quantile regression`, `semi-parametric efficiency`, `location-scale time series`, `asymptotic relative efficiency`, `quasi-maximum likelihood estimation`, `ARMA-GARCH`
- **为什么对您有用**: 直接契合您对 semiparametric efficiency theory 的兴趣，展示了半参数 CQR 相对传统 QR 和 QMLE 的效率提升机制；同时 VaR 估计属于经济金融时间序列的典型应用，具有方法论迁移价值。

### 33. [10.5705/ss.202023.0396](https://doi.org/10.5705/ss.202023.0396) — On the Optimality of Functional Sliced Inverse Regression
- **作者**: Rui Chen, Songtao Tian, Dongming Huang, Qian Lin, Jun S. Liu
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在函数型充分降维（functional sufficient dimension reduction）框架下，本文研究 FSIR 估计 central space 的极小极大最优性，设定为多指标模型且 Y 无需离散。首先，作者给出了条件均值协方差 FSIR 估计量的 concentration inequality，并据此建立该估计量像空间的 root-n 相合性。其次，采用截断正则化估计协方差算子的逆，明确给出截断参数的选取条件，使 FSIR 达到估计 central space 的极小极大最优收敛速率。据作者所知，这是首篇严格证明 FSIR 在多指标模型与一般 Y 下 minimax 最优性的工作。模拟验证了截断参数的最优选取与估计效率。对您有用：该文将 concentration inequality 与协方差算子截断正则化结合推导 minimax rate 的技术路线，可直接迁移到您关注的半参数效率界与高维/函数型推断问题中。
- **关键技术**: `functional sliced inverse regression`, `concentration inequality`, `covariance operator truncation`, `minimax convergence rate`, `sufficient dimension reduction`, `root-n consistency`
- **为什么对您有用**: 直接推进您关注的半参数/非参数理论：首次给出 FSIR 的 minimax 最优速率证明，其 concentration inequality + 算子截断正则化的分析框架可迁移到函数型/高维半参数效率界研究中。

### 34. [10.5705/ss.202024.0063](https://doi.org/10.5705/ss.202024.0063) — Empirical Bayes Estimation with Side Information: A Nonparametric Integrative Tweedie Approach
- **作者**: Jiajun Luo, Trambak Banerjee, Gourab Mukherjee, Wenguang Sun
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在 compound estimation of normal means 设定下，本文研究如何利用辅助变量（side information）提升经验贝叶斯估计精度，目标参数为各均值的后验期望。核心方法是非参数整合 Tweedie（NIT）：通过凸优化直接估计边际密度的对数梯度（即 score function），从而将结构约束自然嵌入 Tweedie 公式 μ + σ²∇log f 中。理论上，作者建立了 NIT 渐近风险收敛到 oracle 估计量的速率，并精确量化了辅助变量维度增加时估计风险的改善与收敛速率恶化之间的 trade-off。数值实验和真实数据均显示 NIT 优于现有方法。对您而言，该文的非参数 score 估计与凸优化结合思路，以及辅助信息维度对收敛速率的量化分析，可直接迁移到 semiparametric efficiency 与 debiased ML 中 nuisance 参数估计的理论研究。
- **关键技术**: `empirical Bayes Tweedie formula`, `log-density gradient estimation via convex optimization`, `oracle convergence rate`, `compound decision theory`, `structural constraints on score function`
- **为什么对您有用**: 非参数 score 估计与 oracle 收敛速率分析直接对应您在 semiparametric efficiency 和 debiased ML 方向的兴趣；辅助信息维度对速率的 trade-off 量化对高维 nuisance 参数估计有理论迁移价值。

### 35. [10.5705/ss.202023.0312](https://doi.org/10.5705/ss.202023.0312) — Bayesian Inference of Spatially Varying Correlations via the Thresholded Correlation Gaussian Process
- **作者**: Moyan Li, Lexin Li, Jian Kang
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多模态神经影像设定下，本文目标是推断两种模态间的空间变相关性并识别相关性统计显著的区域。提出阈值相关高斯过程（TCGP）这一贝叶斯非参数模型，通过阈值机制同时保证空间相关性的分段平滑、稀疏性与跳跃不连续性，适用于小样本及低信噪比场景。理论层面证明了模型可识别性与大支撑性质，并严格推导了后验一致性与选择一致性。计算层面设计了高效的 Gibbs 采样器及其变体以实现后验分布的快速求解。实证分析基于模拟与 Human Connectome Project 的 fMRI 数据验证了方法表现。对您有用：本文的后验与选择一致性理论及高效采样器设计，可为您的非参数理论与统计计算兴趣提供贝叶斯视角的参考，选择一致性亦直接关联假设检验中的变量选择问题。
- **关键技术**: `thresholded correlation Gaussian process`, `Bayesian nonparametrics`, `posterior consistency`, `selection consistency`, `Gibbs sampler`
- **为什么对您有用**: 本文的后验与选择一致性理论及高效采样器设计，可为您的非参数理论与统计计算兴趣提供贝叶斯视角的参考，选择一致性亦直接关联假设检验中的变量选择问题。

### 36. [10.5705/ss.202024.0339](https://doi.org/10.5705/ss.202024.0339) — Nonparametric Spatial Modeling towards the Mode
- **作者**: Tao Wang, Weixin Yao
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文提出空间模回归（spatial modal regression），假设给定协变量 X 下响应 Y 的条件众数服从非参数回归结构 m(·)，而非传统的条件均值或分位数。估计通过核密度方法定位条件众数，作者推导了在适当带宽选择下模估计量的渐近分布，并提出了改进的模期望最大化（MEM）算法配合高斯核进行数值求解。为缓解高维协变量下的维数灾难，进一步将模型推广为可加和形式（additive sum form），实现高维场景下的可行估计。模拟与实例表明有限样本表现良好，但渐近效率与均值回归下的最优性比较未深入讨论。对您而言，本文的非参数模回归框架可作为非参数理论兴趣中的补充视角，其可加推广与带宽选择策略对高维非参数建模有参考价值。
- **关键技术**: `modal regression`, `kernel density estimation`, `modal expectation-maximization (MEM) algorithm`, `additive model extension`, `bandwidth selection`, `asymptotic distribution`
- **为什么对您有用**: 属于非参数理论兴趣范畴，模回归提供了均值/分位数之外的补充视角；可加推广对高维非参数建模有参考，但与效率理论、RMT 等核心方向距离较远。

### 37. [10.5705/ss.202024.0100](https://doi.org/10.5705/ss.202024.0100) — The Population and Personalized Areas Under the Receiving Operating Characteristic Curve
- **作者**: Haben Michael, Lu Tian
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在聚类数据（clustered data）设定下，将经典 AUC 推广为总体 AUC（population AUC）与个体 AUC（personalized AUC）两个目标参数，分别刻画群体层面与簇内层面的判别能力。作者通过具体模型与可视化阐明两者何时分歧、何时一致，并给出定量关系。估计与推断方面，提出了联合估计程序，其核心依赖于 AUC 的 U-statistic 结构在聚类依赖下的扩展，模拟验证了方法表现。实证部分将方法应用于城市警务行为数据。对您而言，AUC 本质是 Mann-Whitney U-statistic，聚类推广必然涉及退化/高阶 U-statistic 的投影与方差估计，与您关注的 higher-order U-statistics 方向有直接方法学联系。
- **关键技术**: `clustered U-statistic`, `Mann-Whitney estimator`, `joint estimation of correlated AUCs`, `nonparametric discrimination measure`, `influence function for clustered data`
- **为什么对您有用**: AUC 的聚类数据推广涉及 dependent U-statistic 的投影与方差分析，直接连接您关注的 higher-order U-statistics 与非参数推断理论；推断程序中 influence function 的推导也可与 semiparametric efficiency 的视角对照。

### 38. [10.5705/ss.202024.0222](https://doi.org/10.5705/ss.202024.0222) — Distributed Inference for Tail Risks
- **作者**: Liujun Chen, Deyuan Li, Chen Zhou
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在分布式数据设定下（数据存储在多台机器），本文研究极值统计中尾部经验过程和分位数过程的渐近性质，目标是建立分布式极值估计量的 oracle 性质。核心工具是将尾部经验过程和分位数过程在分布式场景下分解为局部过程的聚合，利用经验过程理论证明聚合后的过程收敛到与全局数据相同的极限分布。作者展示了该工具包可以直截了当地为大多数分布式极值估计量（如 Hill 估计量、尾部指数估计量等）建立 oracle 性质，即分布式估计量达到与集中式估计量相同的渐近方差和 n^{-1/2} 收敛率。主要理论贡献是一套统一的分布式尾部过程渐近分析框架，并通过多个例子验证实用性。对您而言，该文的分布式 oracle property 证明技术可迁移到其他 semiparametric 分布式估计问题，且涉及的经验过程工具与您的 nonparametric theory 兴趣相关。
- **关键技术**: `tail empirical process`, `tail quantile process`, `distributed oracle property`, `extreme value index estimation`, `empirical process theory`, `Hill estimator`
- **为什么对您有用**: 分布式 oracle property 的证明框架可迁移到 semiparametric efficiency 理论中的分布式估计问题；尾部经验过程的分析技术与您 nonparametric theory 兴趣中的经验过程工具有直接重叠。

### 39. [10.5705/ss.202024.0159](https://doi.org/10.5705/ss.202024.0159) — Dimension Reduction for Extreme Regression via Contour Projection
- **作者**: Liujun Chen, Jing Zeng
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在极端回归（推断响应变量条件极端值）设定下，高维与重尾预测变量使经典条件极值推断工具失效，本文定义了 central extreme subspace (CES) 并证明其在温和条件下存在且唯一。CES 类似充分降维中的 central subspace，但保留的是条件极值信息而非全部条件分布信息；投影到 CES 后预测变量维数降低且极值信息无损。提出 COPES（contour projection）方法估计 CES，核心利用轮廓投影构造估计量，对重尾预测变量具有鲁棒性，并建立了一致性理论保证。模拟与中国股市数据应用验证了方法有效性。对您而言，CES 的 semiparametric 降维框架与充分降维理论一脉相承，COPES 对重尾的鲁棒性思路可迁移至高维重尾设定下的 inference 问题。
- **关键技术**: `central extreme subspace`, `contour projection`, `sufficient dimension reduction`, `heavy-tailed robustness`, `consistency theory`
- **为什么对您有用**: CES 是充分降维在极值回归中的 semiparametric 推广，与您关注的 semiparametric theory 和高维降维直接相关；COPES 对重尾预测变量的鲁棒性思路可迁移至高维重尾 inference 场景。

### 40. [10.5705/ss.202024.0369](https://doi.org/10.5705/ss.202024.0369) — Quantile Residual Lifetime Regression for Multivariate Failure Time Data
- **作者**: Tonghui Yu, Liming Xiang, Jong-Hyeon Jeong
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多变量失效时间数据下，同一受试者的多个事件时间潜在相关，目标是评估协变量对分位数残差寿命（QRL）的效应，采用边际半参数 QRL 回归模型。提出基于无偏估计方程的估计方法，证明估计量具有一致性与渐近正态性。为克服推断中的额外挑战，提供三种方差估计方法——基于重抽样技术和三明治估计量，并构建 Wald 型检验统计量。模拟与真实临床数据分析表明方法表现良好。该工作属于半参数理论在生存分析中的应用，其边际建模与三明治方差估计思路可迁移至纵向因果推断中的相关失效时间设定，Wald 型检验的构造对您的假设检验兴趣有参考价值。
- **关键技术**: `semiparametric QRL regression`, `unbiased estimating equations`, `sandwich variance estimator`, `resampling techniques`, `Wald-type test`, `multivariate failure time`
- **为什么对您有用**: 半参数边际模型与渐近正态性理论直接对应您的 semiparametric theory 兴趣；Wald 型检验与 sandwich 方差估计对您 hypothesis testing 与 longitudinal causal inference 的推断有方法迁移价值。

### 41. [10.5705/ss.202023.0418](https://doi.org/10.5705/ss.202023.0418) — Residual-based Alternative Partial Least Squares for Generalized Functional Linear Models
- **作者**: Yue Wang, Xiao Wang, Joseph G. Ibrahim, Hongtu Zhu
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在广义函数线性模型（GFLM）框架下，同时包含函数型和标量协变量，目标是估计未知斜率函数及标量参数。提出残差替代偏最小二乘（RAPLS）算法，通过迭代方式将 APLS 扩展至非连续结局与标量协变量情形。理论上，建立了 RAPLS 估计量对未知斜率函数的收敛速率。进一步引入校准步骤，证明了校准后 RAPLS 估计量对标量参数的渐近正态性与半参数有效性。模拟与 ADNI 阿尔茨海默症神经影像数据应用验证了方法的有效性。对您有用：该文在函数数据模型下推导标量参数的半参数有效估计，其校准步骤与效率理论推导思路可直接迁移至您关注的半参数效率界与 debiased ML 研究；同时 ADNI 数据集对流行病学应用有参考价值。
- **关键技术**: `functional linear models`, `partial least squares`, `convergence rate`, `asymptotic normality`, `semiparametric efficiency`, `calibration step`
- **为什么对您有用**: 该文在函数数据模型下推导标量参数的半参数有效估计，其校准步骤与效率理论推导思路可直接迁移至您关注的半参数效率界与 debiased ML 研究；同时 ADNI 数据集对流行病学应用有参考价值。

### 42. [10.5705/ss.202024.0180](https://doi.org/10.5705/ss.202024.0180) — Semiparametric Inference for Functional Survival Models
- **作者**: Hongyi Zhou, Wenqing Su, Qixian Zhong, Ying Yang
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在右删失生存数据设定下，本文将基于常微分方程(ODE)的生存模型扩展至函数型协变量，目标是标量参数和函数型参数的半参数推断。针对标量系数，作者构造了估计量并严格证明了其渐近正态性与半参数有效性，即达到了半参数效率界。对于函数型参数，文章推导了其渐近同时置信带，从而实现了函数参数的全局推断。核心技术工具依赖于半参数效率理论、经验过程以及函数型数据分析。模拟研究验证了所提方法在有限样本下的表现。该工作对您在效率理论方面的兴趣有直接参考价值，特别是在复杂（函数型）协变量下如何推导并达到半参数效率界。
- **关键技术**: `semiparametric efficiency bound`, `functional covariates`, `ODE survival model`, `simultaneous confidence band`, `right-censored data`
- **为什么对您有用**: 直接涉及您 primary interest 中的 efficiency theory (semiparametric efficiency bounds)，展示了在函数型协变量生存模型下如何构造有效估计量并推导效率界，对处理带函数数据的半参数推断有方法迁移价值。

### 43. [10.5705/ss.202024.0418](https://doi.org/10.5705/ss.202024.0418) — Tail Risk Equivalent Level Transition And Its Application for Estimating Extreme Lp-Quantiles
- **作者**: Qingzhao Zhong, Yanxi Hou
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在极值理论与风险度量交叉设定下，本文提出尾部风险等价水平转换（TRELT）概念，用于刻画两种 Lp-quantile（VaR 与 expectile 的推广）之间尾部风险的等价转换关系。受 Li & Wang (2023) 的 PELVE 启发，作者在正则条件下证明了 TRELT 的存在性与唯一性，并建立其渐近性质。基于 TRELT 的风险转换机制，发展了针对 TRELT 及极端 Lp-quantile 的推断方法，该方法作为极值理论中的新型外推技术，利用中间水平分位数信息推断极端水平。模拟与实证分析验证了方法表现。对您而言，该文的渐近推断框架与极值外推思路可为经济理论中金融风险度量的 semiparametric 推断提供参考。
- **关键技术**: `Lp-quantile`, `tail risk equivalent level transition`, `extreme value extrapolation`, `PELVE`, `asymptotic inference`
- **为什么对您有用**: 渐近推断与极值外推方法可迁移至经济理论中金融风险度量的 semiparametric 推断；数学统计层面的存在性/唯一性证明思路对非参数理论有借鉴价值。

### 44. [10.5705/ss.202022.0206](https://doi.org/10.5705/ss.202022.0206) — Asymmetric Estimation for Varying-Coefficient Additive Model with Functional Response in Reproducing Kernel Hilbert Space
- **作者**: Yi Liu, Wei Tu, Yanchun Bao, Bei Jiang, Linglong Kong
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究 function-on-scalar 回归框架下 varying-coefficient additive model 的 expectile 回归估计问题，目标是在 RKHS 正则性假设下对功能型响应做非对称回归，以捕捉异方差性。方法上，将 expectile loss 与 RKHS 惩罚结合，构造了 varying-coefficient additive expectile estimator，并在随机设计与固定设计两种情境下分别推导了 minimax 收敛速率，证明所提估计量达到统计最优。模拟部分验证了不同设定下的稳健表现，实证分析使用了乳腺癌临床试验生活质量纵向数据。对您而言，该文将 RKHS minimax 理论拓展至 expectile 功能回归，与您关注的半/非参数理论及效率理论直接相关，且纵向功能数据的 expectile 估计思路可迁移至因果推断中纵向结局的异质性分析。
- **关键技术**: `expectile regression`, `reproducing kernel Hilbert space`, `varying-coefficient additive model`, `minimax rate of convergence`, `function-on-scalar regression`, `asymmetric loss`
- **为什么对您有用**: RKHS 下的 minimax rate 推导直接对应您 primary interest 中的半/非参数理论与效率理论；expectile 对异方差功能响应的建模思路可迁移至纵向因果推断中处理效应异质性的估计。

### 45. [10.5705/ss.202023.0366](https://doi.org/10.5705/ss.202023.0366) — Functional Varying-Coefficient Model Under Heteroskedasticity with Application to DTI Data
- **作者**: Pratim Guha Niyogi, Ping-Shou Zhong, Xiaohong Joe Zhou
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究函数型变系数模型在异方差与空间依赖下的估计问题，目标参数为随函数型预测变量光滑变化的系数函数。方法上提出多步估计：先以局部线性 GMM 基于连续矩条件做初始估计，再将矩条件投影到协方差算子的特征函数上并以特征值加权组合，从而避免直接求逆协方差算子的困难。核心贡献是构造最优工具变量，在所有局部线性 GMM 估计类中最小化渐近方差函数，使估计在异方差下显著提升精度。渐近性质（包括最优性）得到严格推导，模拟与 DTI 实数据验证了有限样本表现。对您有用：该文将最优 IV 思想嵌入非参数 GMM 框架、以特征投影处理空间依赖的策略，可直接迁移到您关注的 semiparametric efficiency 与 IV 估计的交叉研究中。
- **关键技术**: `local-linear GMM`, `optimal instrument variable`, `eigen-function projection`, `weighted eigen-value combination`, `functional varying-coefficient model`, `heteroskedasticity-robust estimation`
- **为什么对您有用**: 最优 IV 最小化渐近方差函数直接关联您 primary interest 中的 efficiency theory 与 IV 估计；特征投影处理空间依赖的技术路线对 semiparametric 框架下高维/函数型数据的矩条件推断有方法论迁移价值。

## 效率理论 / Debiased ML  *(efficiency_dml, 8 篇)*

### 1. [10.5705/ss.202024.0261](https://doi.org/10.5705/ss.202024.0261) — Semi-supervised Regression Analysis with Model Misspecification and High-dimensional Data
- **作者**: Ye Tian, Peng Wu, Zhiqiang Tan
- **期刊/来源**: Statistica Sinica
- 相关性 9/10 · novelty: `weaker_assumption`
- **摘要**: 在半监督学习(SSL)与协变量偏移迁移学习(CSTL)设定下，目标是对条件均值模型的回归系数进行推断，允许结果回归(OR)模型误设且数据为高维。作者提出基于正则化校准估计量的AIPW方法，对倾向得分(PS)和OR两个nuisance模型进行序贯估计，而非独立估计。核心理论结果：当PS模型正确设定时，即使OR模型误设且为高维数据，所提估计量仍具有一致性、渐近正态性和有效置信区间——即从双重稳健放松为单重稳健仍可保证推断有效性。作者进一步证明已有SSL/CSTL方法可统一于该AIPW框架。对您而言，该工作将AIPW在半监督设定下的稳健性条件弱化至仅PS正确，结合高维正则化校准估计，直接关联您在semiparametric efficiency bounds与high-dimensional debiased inference方面的研究兴趣。
- **关键技术**: `augmented inverse probability weighting (AIPW)`, `regularized calibrated estimation`, `sequential nuisance estimation`, `double robustness under misspecification`, `high-dimensional propensity score`
- **为什么对您有用**: 将AIPW双重稳健性在半监督/迁移学习设定下弱化为仅PS正确即可保证n^{-1/2}-CAN推断，结合高维正则化校准，对您研究semiparametric efficiency与high-dimensional debiased ML的交互有直接借鉴价值。

### 2. [10.5705/ss.202025.0034](https://doi.org/10.5705/ss.202025.0034) — Assumption-Lean Quantile Regression
- **作者**: Georgi Baklicharov, Christophe Ley, Vanessa Gorasso, Brecht Devleesschauwer, Stijn Vansteelandt
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在部分线性分位回归设定下，目标是估计暴露变量对条件分位数的关联效应，即使分位模型误设定也要求 estimand 有因果/关联意义。作者将目标参数映射到一个非参数主效应 estimand，该 estimand 在模型误设定时仍捕获所关心的条件关联。利用非参数模型下的 efficient influence function 构建估计量，允许纳入 data-adaptive 方法（变量选择、机器学习），从而对变量选择诱导的偏差与过度不确定性具有鲁棒性。估计量在正则条件下一致且 n^{-1/2}-CAN。模拟研究与超重相关年度医疗费用数据验证了方法表现。对您有用：该工作将 EIF / assumption-lean 思路系统引入分位回归，与您关注的 semiparametric efficiency bounds 及 debiased ML 直接对接，部分线性结构的稳健化策略可迁移至 causal inference 中 exposure effect 的可靠估计。
- **关键技术**: `efficient influence function`, `partially linear quantile regression`, `nonparametric main effect estimand`, `assumption-lean modeling`, `data-adaptive estimation`, `one-step estimation`
- **为什么对您有用**: 直接推进 semiparametric efficiency 在分位回归中的应用，与您关注的 efficiency bounds / debiased ML / assumption-lean causal inference 高度契合；EIF + data-adaptive 的框架可迁移到 proximal CI 或 mediation 设定中的稳健估计。

### 3. [10.5705/ss.202024.0268](https://doi.org/10.5705/ss.202024.0268) — Asymptotic Normality of Robust Risk Minimizers
- **作者**: Stanislav Minsker
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 本文研究鲁棒经验风险最小化估计量的渐近性质，设定为在弱矩条件下用 median-of-means 等鲁棒均值代理替代经典经验平均来最小化风险。作者证明，在广泛参数问题中，该鲁棒估计量不仅以最优速率收敛到真实风险最小值，且通常具有与经典 ERM 相同的渐近方差，即达到渐近有效。核心机制依赖于鲁棒代理的线性化与影响函数分析，并比较了 min-max 鲁棒程序与直接风险最小化的渐近表现。理论结果表明，基于 min-max 形式的鲁棒算法在渐近方差上严格优于直接最小化算法。这对您有用：直接推进了 efficiency theory 中关于弱假设下 M-estimator 渐近有效性的研究，其鲁棒代理构造思路对 debiased ML 中处理重尾干扰的正交得分设计有直接启发。
- **关键技术**: `median-of-means estimator`, `robust empirical risk minimization`, `asymptotic efficiency`, `min-max robust procedure`, `influence function linearization`
- **为什么对您有用**: 直接关联您 primary interest 中的 efficiency theory：证明了基于 median-of-means 的鲁棒 M-estimator 可达到与经典 ERM 相同的渐近方差（即渐近有效），为重尾或弱假设下的有效估计提供了 new_theory，其 min-max 鲁棒构造思路可迁移至 debiased ML 中的正交得分设计。

### 4. [10.5705/ss.202024.0359](https://doi.org/10.5705/ss.202024.0359) — A Maximin Optimal Approach for Sampling Designs in Two-phase Studies
- **作者**: Ruoyu Wang, Qihua Wang, Wang Miao
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在两阶段抽样研究（phase 1 全样本收集廉价变量，phase 2 按预设规则对子样本测量昂贵变量）中，目标是设计最优抽样规则以最小化一般参数估计的 semiparametric efficiency bound。现有文献多局限于特定参数模型下的标量参数，本文提出基于 semiparametric efficiency bound 的 maximin 准则来构造 model-free 的最优抽样规则。核心机制：对任意估计问题，先求出两阶段设计下的 efficient influence function 与效率界，再以 maximin 思想选择使效率界最不利情形最小化的抽样概率；标量参数时等价于直接最小化效率界，多维参数时保证每个分量的效率界均改善。理论结果保证所得抽样规则在 semiparametric 框架下具有最优性，模拟与实例验证了方差缩减效果。对您有用：该工作将 semiparametric efficiency bound 从被动评价工具推进为主动设计工具，直接关联您对效率理论和 semiparametric 方法的兴趣，且两阶段设计在流行病学队列研究中极为常见，方法可迁移至您关注的 applied causal 场景。
- **关键技术**: `semiparametric efficiency bound`, `maximin optimal design`, `two-phase sampling`, `efficient influence function`, `model-free estimation`
- **为什么对您有用**: 直接推进 semiparametric efficiency bound 的应用——从估计评价变为抽样设计准则，契合您对效率理论的 primary interest；两阶段设计在流行病学中常见，方法可迁移至您关注的 epidemiology applied causal 场景。

### 5. [10.5705/ss.202025.0083](https://doi.org/10.5705/ss.202025.0083) — Estimation and Inference for Density-convoluted Support Vector Machine with Streaming Data
- **作者**: Haochen Rao, Xu Guo, Heng Lian, Haobo Qi
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究高维流数据下 SVM 系数的估计与推断问题，目标参数为线性 SVM 的系数向量，关键正则性假设包括稀疏性及流数据的在线可更新性。为处理 hinge loss 的非光滑性，采用密度卷积（density convolution）技术构造光滑代理损失，并提出在线 Lasso 估计器，其代理损失以可再生二次型近似历史信息，仅需新到数据与有限历史统计量即可在线更新。在温和条件下导出在线 Lasso 的误差界；进一步提出在线去偏 Lasso 估计器，建立其渐近正态性，从而实现逐系数的有效推断。计算上采用 proximal gradient descent 算法，适用于高维场景且计算高效。该工作将 debiased ML 推断从批量高维设定推广到流数据非光滑损失场景，对您在 debiased ML 及统计计算方向的研究有直接参考价值。
- **关键技术**: `density convolution`, `online debiased lasso`, `renewable quadratic surrogate loss`, `proximal gradient descent`, `asymptotic normality`, `streaming data inference`
- **为什么对您有用**: 直接连接您 primary interest 中的 efficiency theory（debiased ML 在流数据非光滑损失下的推断）与 statistical computing（在线算法、proximal GD），同时涉及高维稀疏推断，方法框架可迁移至其他非光滑损失场景的在线去偏推断。

### 6. [10.5705/ss.202025.0057](https://doi.org/10.5705/ss.202025.0057) — Robust Jackknife Model Averaging
- **作者**: Kang You, Miaomiao Wang, Guohua Zou
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维且可能存在异常值的大数据设定下，传统基于最小二乘或极大似然的模型平均方法会严重退化，本文提出鲁棒折刀模型平均（RJMA）框架以解决此问题。RJMA 通过最小化基于鲁棒损失的留一交叉验证（leave-one-out CV）准则来选择权重，适用于候选模型维度随样本量增加的半参数式设定。理论上证明了 RJMA 估计量的渐近最优性（最小化样本外最终预测误差 FPE）以及权重估计量向理论最优权重向量的相合性；若候选集中包含正确模型，RJMA 会将全部权重分配给正确模型。进一步推导了 RJMA 估计量的影响函数（influence function），并引入经验预测影响函数来定量评估其鲁棒性。本文将影响函数工具从传统 M 估计拓展至模型平均权重选择，对您在效率理论（特别是 influence function 推导）和半参数框架下的鲁棒性研究有直接的方法论借鉴意义。
- **关键技术**: `jackknife model averaging`, `influence function`, `asymptotic optimality`, `leave-one-out cross-validation`, `robust loss function`
- **为什么对您有用**: 直接关联您的效率理论兴趣：文章详细推导了模型平均估计量的影响函数（influence function），这是半参数效率与鲁棒性理论的核心工具；其渐近最优性证明对半参数/非参数理论下的权重选择研究有参考价值。

### 7. [10.5705/ss.202024.0378](https://doi.org/10.5705/ss.202024.0378) — Semiparametric Efficient Estimation of Quantile Regression
- **作者**: Zhanfeng Wang, Kani Chen, Yuanyuan Lin, Zhiliang Ying
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在半参数分位数回归模型下（假设响应变量分位数与协变量线性相关），目标是推导回归系数的半参数有效得分与效率边界。作者首先计算了该模型的有效得分函数及对应的半参数效率下界，随后提出了一种具体的半参数有效估计量构造方法。该估计量通过估计有效影响函数实现 n^{-1/2}-CAN 且达到半参数效率边界。模拟结果显示，相较于标准分位数回归方法，该估计量具有显著的效率提升。对您有用：本文直接推进了半参数效率理论在分位数模型中的应用，为您在效率边界推导和有效影响函数构造方面提供了经典的理论参考。
- **关键技术**: `semiparametric efficiency bounds`, `efficient influence function`, `quantile regression`, `semiparametric efficient scores`, `asymptotically linear estimator`
- **为什么对您有用**: 直接契合您 primary interest 中的 efficiency theory (semiparametric efficiency bounds) 与 semiparametric theory，提供了分位数回归设定下有效得分与效率边界的标准推导范式，对您研究其他半参数模型的效率边界有直接借鉴价值。

### 8. [10.5705/ss.202024.0105](https://doi.org/10.5705/ss.202024.0105) — Efficient Estimation of the Accelerated Failure Time Model with Auxiliary Aggregate Information
- **作者**: Huijuan Ma, Manli Cheng, Yukun Liu, Donglin Zeng, Yong Zhou
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在 AFT（加速失效时间）模型下，研究如何结合个体数据与辅助聚合数据以提高回归参数的估计效率，关键假设是聚合数据提供了额外的边际生存分布信息。为克服全似然最大化带来的计算挑战，提出一种 one-step estimator：以不利用聚合信息的条件极大似然估计为初始值，通过一步更新逼近全似然估计。理论上证明该估计量具有相合性与渐近正态性，其渐近方差具有闭式表达且可通过 plug-in 规则估计，效率严格优于仅用个体数据的初始估计。模拟实验验证了效率提升，并在 III 期结肠癌化疗的流行病学数据中进行了实证分析。对您有用：该文利用 one-step 更新融合辅助信息实现效率增益的框架，直接对应您在 efficiency theory 与 semiparametric efficiency 方向的兴趣，且包含流行病学队列数据的应用参考。
- **关键技术**: `one-step estimator`, `full likelihood`, `auxiliary aggregate information`, `accelerated failure time model`, `asymptotic efficiency gain`
- **为什么对您有用**: 直接契合您在 efficiency theory 的兴趣，展示了如何通过 one-step 更新融合辅助信息实现效率增益；同时提供了流行病学（结肠癌）真实数据应用案例。

## 数理统计 / 假设检验  *(hypothesis_testing, 27 篇)*

### 1. [10.5705/ss.202025.0194](https://doi.org/10.5705/ss.202025.0194) — Post-Selection Inference in Generalized Linear Models via Parametric Programming
- **作者**: Qinyan Shen, Karl Gregory, Xianzheng Huang
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在广义线性模型（GLM）经 Lasso 变量选择后的 post-selection inference 设定下，目标是修正选择偏差以对回归系数进行有效的假设检验与区间估计。本文将线性模型中基于参数规划的 PoSI 策略推广至非高斯 GLM，核心在于将 GLM 的 MLE 与线性模型的 OLS 建立类比。通过构造基于原始数据的伪响应与协变量的线性化模型，将 GLM 的选择事件转化为线性模型中的多面体选择事件，从而利用参数规划路径追踪选择区域。模拟表明，该方法有效修正了忽略选择偏差的朴素推断，且比基于多面体的 PoSI 方法具有更高的统计效率。对您有用：该文将高维 Lasso 选择后的推断从高斯推广至 GLM，直接契合您对假设检验与高维统计的兴趣，其参数规划的计算技巧也对统计计算方向有参考价值。
- **关键技术**: `post-selection inference`, `parametric programming`, `Lasso variable selection`, `polyhedral selection region`, `pseudo-response linearization`, `generalized linear models`
- **为什么对您有用**: 直接契合您在数学统计（假设检验）与高维统计方面的核心兴趣；其利用参数规划与伪响应线性化处理选择偏差的技巧，不仅放松了高斯假设，也为高维推断的计算方法提供了新思路。

### 2. [10.5705/ss.202025.0183](https://doi.org/10.5705/ss.202025.0183) — A Conditionally Studentized Test for High-dimensional Parametric Regression via Sample Splitting
- **作者**: Feng Liang, Chuhan Wang, Jiaqi Huang, Lixing Zhu
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 在高维参数回归模型检验问题中，本文提出 Conditionally Studentized Test (COST)，目标是在不依赖降维或稀疏假设的条件下对一般参数回归模型进行 model checking，关键正则条件允许预测变量维度 p 超过样本量 n。COST 将样本分为两块，用其中一块构造权重矩阵对另一块做条件学生化，使得无论初始统计量是全局光滑型还是局部光滑型，零假设下均可获得渐近正态性；对 p 与 n 的关系不做限制（固定或发散均可），在回归函数正则条件下 p 可大于 n；对局部替代假设具有快速检测速率。主要理论结果为零假设下的渐近正态性与局部替代下的检测速率，数值实验验证了 p=n 等高维场景的有限样本表现。对您有用：条件学生化+样本分割的技巧可直接迁移到您关注的高维假设检验与 inference 子方向，且不依赖稀疏假设的设定与 debiased ML 的思路形成互补。
- **关键技术**: `sample splitting`, `conditional studentization`, `high-dimensional model checking`, `asymptotic normality under null`, `local alternative detection rate`, `global and local smoothing-based test statistic`
- **为什么对您有用**: 直接推进高维假设检验理论，条件学生化+样本分割的技巧可迁移到您关注的 high-dimensional inference 与 hypothesis testing 子方向，且不依赖稀疏假设的设定与 debiased ML 的思路互补。

### 3. [10.5705/ss.202024.0022](https://doi.org/10.5705/ss.202024.0022) — Multiple Testing of One-Sided Hypotheses under Unknown Dependence
- **作者**: Seonghun Cho, Youngrae Kim, Johan Lim, Hyungwon Choi, DoHwan Park, Woncheol Jang
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在多重检验框架下，单侧假设导致经验零分布（或 p 值）趋于保守，若不加以处理会造成检验功效显著损失。本文提出 DAB-PFA（discarding adaptively with bounding on principal factor approximation）程序，用于在检验统计量具有一般未知相依结构时同时检验大量单侧假设。方法核心有两步：一是采用 Fan and Han (2017) 的主因子近似（PFA）刻画检验统计量间的相依结构，二是在估计已实现 false discovery proportion（FDP）时自适应地丢弃过小或过大的 p 值以消除单侧假设带来的保守偏差。作者推导了所提 FDP 估计量的收敛速率，并在 FDR 与 TPR 指标上与 BH、Efron (2004) 及 Wang and Fan (2017) 等方法进行了数值比较。仿真与卵巢腺癌蛋白磷酸化数据实证均显示 DAB-PFA 在控制 FDR 的同时显著提升功效。对您有用：该文将 PFA（与高维因子模型/RMT 密切相关）引入单侧多重检验，直接连接您的高维统计与假设检验两个 primary interest，且自适应丢弃策略的思想可迁移至其他保守 p 值场景。
- **关键技术**: `principal factor approximation (PFA)`, `adaptive p-value discarding`, `realized FDP estimation`, `false discovery rate control`, `one-sided hypothesis testing`, `factor model dependence structure`
- **为什么对您有用**: 直接连接您 hypothesis testing 与 high-dimensional statistics 两个 primary interest：PFA 源于高维因子模型理论，自适应丢弃策略为单侧检验保守性问题提供了新解法，收敛速率结果对理解高维相依结构下多重检验的效率有参考价值。

### 4. [10.5705/ss.202024.0334](https://doi.org/10.5705/ss.202024.0334) — Optimal Robust Sequential Tests of Circular Nonconforming Probability
- **作者**: Qunzhi Xu, Yajun Mei
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 本文研究二维系统命中预定义圆盘目标概率（CNP）的极小极大非参数序贯检验问题，目标是在不对原始二维数据做任何参数分布假设下检验 CNP 是否达标。作者证明了 Bernoulli 序贯概率比检验（SPRT）在所有满足相同或更小第一、二类错误概率的检验（含固定样本量检验）中，能够最小化最大期望样本量，从而具备极小极大最优性。针对传统序贯分析渐近理论常假设极小错误概率而不实用的局限，文中进一步提出了有限样本下设计与实现 Bernoulli SPRT 的具体算法。对您有用：该文将非参数极小极大理论与序贯假设检验结合，直接推进了您在 mathematical statistics (hypothesis testing) 与 nonparametric theory 交叉方向的理解，且其最优性证明与算法设计对统计计算亦有参考价值。
- **关键技术**: `Sequential Probability Ratio Test (SPRT)`, `minimax optimality`, `nonparametric hypothesis testing`, `Circular Nonconforming Probability`, `expected sample size minimization`
- **为什么对您有用**: 直接契合您在 mathematical statistics (hypothesis testing) 和 nonparametric theory 方向的兴趣；文章在非参数设定下证明 SPRT 的极小极大最优性，提供了序贯检验效率的新理论视角，且算法部分对 statistical computing 有参考价值。

### 5. [10.5705/ss.202025.0132](https://doi.org/10.5705/ss.202025.0132) — Random Weighting Approximation of M-estimators with Increasing Dimensions of Parameter
- **作者**: Ruixing Ming, Chengyao Yu, Min Xiao, Zhanfeng Wang
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 本文研究参数维度随样本量发散（increasing dimensions）时，一般参数模型下 M-估计量的随机加权（RW）逼近问题。核心证明了 RW 估计量与原参数 M-估计量具有相同的渐近分布，使得统计推断无需估计渐近分布中的冗余参数。同时建立了 RW 估计量的 Bahadur 表示与收敛速度，为高维发散下的重抽样理论提供了严格基础。该结果意味着 RW 作为 bootstrap 的替代方案在维度增加时依然有效，对您在假设检验与高维统计计算方向的研究有直接参考价值，特别是在避免冗余参数估计的推断场景中。
- **关键技术**: `random weighting`, `M-estimation`, `Bahadur representation`, `increasing dimension`, `asymptotic distribution approximation`
- **为什么对您有用**: 该文将随机加权逼近从固定维度推广到发散维度，对您在数学统计（假设检验）与高维统计计算方向的研究有直接参考价值；其避免估计冗余参数的特性也与半参数效率推断的思想相通。

### 6. [10.5705/ss.202023.0099](https://doi.org/10.5705/ss.202023.0099) — Reproducible Learning in Large-Scale Multiple Graphical Models
- **作者**: Jia Zhou, Guangming Pan, Zeming Zheng, Changchun Tan
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 在异质高维多重图模型设定下，本文研究底层稀疏图结构的可复现学习（即 FDR 控制）问题。提出 multiple graphical knockoff filter 方法，通过构造 knockoff 变量从异质数据中高效恢复总体连接结构。理论上证明了该方法的渐近 FDR 控制性质，并首次建立了 graphical knockoff 过程的势（power）分析理论。数值实验进一步验证了 FDR 控制与高 power 的表现。对您有用：该文将 knockoff 拓展至异质图模型，其高维假设检验中 FDR 与 power 的理论分析框架对您的高维统计与假设检验方向有直接参考价值。
- **关键技术**: `multiple graphical knockoff filter`, `false discovery rate (FDR) control`, `power analysis`, `high-dimensional graphical models`, `data heterogeneity`
- **为什么对您有用**: 直接关联您的高维统计与假设检验方向；首次给出 graphical knockoff 的 power 理论，对研究高维多重检验的 FDR 与 power 权衡具有理论参考价值。

### 7. [10.5705/ss.202023.0385](https://doi.org/10.5705/ss.202023.0385) — Universally Consistent Tests for the Graph of a Gaussian Graphical Model
- **作者**: Thien-Minh Le, Ping-Shou Zhong, Chenlei Leng
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 在高维 Gaussian 图模型（GGM）设定下，目标是检验图结构（精度矩阵零模式）的充分性，即进行全局 goodness-of-fit 检验。本文首先提出直接 plug-in 检验统计量，证明其零假设下的渐近分布为 Gumbel 分布，位置参数依赖于真实图结构；但该检验对包含真实图但不等于其的备择假设无检验效力。为此，作者提出 consistency-empowered 检验统计量，通过放大估计中的噪声来获得功效，并证明其对所有固定备择假设具有普遍一致性（universally consistent）。模拟显示检验具有正确的水平和良好的功效，并在 COVID-19 数据集上展示了图结构选择对估计效率的提升。对您有用：该工作直接推进您在 mathematical statistics & hypothesis testing 方向的兴趣，其通过放大噪声构造一致性检验的技巧具有方法论启发，同时 COVID-19 应用也契合您的 epidemiology 兴趣。
- **关键技术**: `Gaussian graphical model`, `goodness-of-fit test`, `Gumbel distribution`, `universally consistent test`, `noise amplification`, `high-dimensional inference`
- **为什么对您有用**: 直接推进您在 mathematical statistics & hypothesis testing 方向的兴趣，'放大噪声以获得一致性'的检验构造技巧具有方法论启发，且 COVID-19 应用契合您的 epidemiology 兴趣。

### 8. [10.5705/ss.202024.0316](https://doi.org/10.5705/ss.202024.0316) — Bootstrapping Portmanteau Tests for Functional White Noise under Unknown Dependence
- **作者**: Yu Miao, Muyi Li, Wai Keung Li, Xingbai Xu
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在函数时间序列框架下，本文针对函数白噪声假设（允许过程不独立但互不相关）提出基于经验自相关函数平方和的 portmanteau 检验。利用 Hilbert 空间方法，推导了零假设下检验统计量的极限性质；由于序列内部存在未知依赖导致统计量非 pivotal，作者采用分块随机加权 bootstrap（blockwise random weighting bootstrap）获取临界值并证明其有效性。进一步将该方法推广至函数自回归模型的诊断检验，并提供了配套的 R 软件包以方便实际应用。模拟与实际数据表明该检验在有限样本下具有良好的水平控制和功效；对您研究 hypothesis testing 与 statistical computing 有直接参考价值，特别是处理非 pivotal 统计量的 bootstrap 方案及函数空间假设检验的构造思路。
- **关键技术**: `portmanteau test`, `functional time series`, `Hilbert space approach`, `blockwise random weighting bootstrap`, `non-pivotal test`
- **为什么对您有用**: 直接对应您 primary interest 中的 hypothesis testing 与 statistical computing；处理非 pivotal 统计量的分块 bootstrap 算法及函数空间极限理论对高维或非参数假设检验问题有方法迁移价值。

### 9. [10.5705/ss.202025.0127](https://doi.org/10.5705/ss.202025.0127) — Classification Uncertainty Quantification: A Comparison Between Bootstrap and Conformal ROC Confidence Bands
- **作者**: Zheshi Zheng, Bo Yang, Peter Song
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在二分类设定下，本文研究 ROC 曲线及 Youden 指数的不确定性量化（UQ）问题，指出传统 Bootstrap 方法在构造置信带时存在覆盖不足的局限。核心方法引入 Conformal Prediction，利用其分布无关（distribution-free）的有限样本覆盖保证，为 ROC 曲线和 Youden 指数构造有效的置信带。理论证明 Conformal 推断在覆盖性质上严格优于 Bootstrap，数值实验进一步验证了其优势。对您而言，本文展示了 Conformal Inference 替代 Bootstrap 进行严格统计推断的潜力，可为假设检验与统计计算方向提供分布无关推断的新视角。
- **关键技术**: `conformal prediction`, `ROC confidence band`, `bootstrap`, `Youden index`, `distribution-free inference`, `coverage guarantee`
- **为什么对您有用**: 涉及假设检验与统计计算中的不确定性量化，对比了 Conformal inference 与 Bootstrap 的理论保证与计算表现，对您在假设检验和统计计算方向的兴趣有直接参考价值。

### 10. [10.5705/ss.202025.0390](https://doi.org/10.5705/ss.202025.0390) — Modelling Time Series of Counts with Hysteresis
- **作者**: Xintong Ma, Dong Li, Howell Tong
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对计数时间序列提出带阈值的滞后泊松自回归（HPART）模型，将线性泊松自回归推广为非线性分段线性结构，并通过引入科学相关的控制因子实现真正的滞后（hysteresis）效应，而非仅名义上的滞后。同时重新审视带阈值的缓冲泊松自回归（BPART）模型，两模型共享分段线性便利结构但 HPART 更深入刻画了体制切换的动态机制。在估计方面，统一研究了两种模型参数的 MLE 及其渐近性质；在检验方面，针对 BPART 与 HPART 这对非嵌套模型建立了 separate families 假设检验。Monte Carlo 模拟验证了有限样本下参数估计与检验的功效，两个实际计数时间序列展示了 HPART 的可解释性与样本外预测改进。对您有用之处在于：非嵌套假设检验的框架可迁移至因果推断中不同 identification 策略（如 proximal vs IV）的模型选择问题，且 MLE 渐近理论的处理方式对数学统计假设检验方向有参考价值。
- **关键技术**: `non-nested hypothesis testing`, `separate families of hypotheses`, `MLE asymptotic theory`, `piecewise linear Poisson autoregression`, `regime switching`, `hysteresis modeling`
- **为什么对您有用**: 非嵌套假设检验框架直接关联您在数学统计假设检验方向的兴趣，且该检验思路可迁移至因果推断中比较不同 identification 策略（proximal CI vs IV）的场景；MLE 渐近性质的统一处理对半参数效率理论有间接参考价值。

### 11. [10.5705/ss.202025.0113](https://doi.org/10.5705/ss.202025.0113) — Multiple Testing of Local Extrema for Detection of Structural Breaks in Piecewise Linear Models
- **作者**: Zhibing He, Dan Cheng, Yunpeng Zhao
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在分段线性模型与平稳高斯噪声设定下，本文研究结构变点（连续折点 Type I 与跳跃点 Type II）的数量与位置检测问题。方法通过核平滑与微分将变点检测转化为局部极值识别，利用平滑高斯过程的峰值高度分布计算各极值的 p 值，并结合 BH 程序进行多重检验以控制 FDR。理论上证明了在序列长度、斜率变化或跳跃量增加时，方法具有渐近 FDR 控制与功效一致性；相比传统递归分割法，仅需单次检验，计算复杂度降至 O(n)。数值研究显示在非渐近情形下（变化量较小时）仍能保持 FDR 控制与功效，并提供了 R 包 dSTEM。该文将非参数平滑与高斯过程极值理论结合解决多重检验问题，对您在假设检验（FDR 控制）与非参数理论交叉方向的研究有直接参考价值，且 O(n) 算法对统计计算实践有借鉴意义。
- **关键技术**: `kernel smoothing`, `peak height distribution of smooth Gaussian processes`, `Benjamini-Hochberg procedure`, `FDR control`, `piecewise linear models`, `O(n) algorithm`
- **为什么对您有用**: 将非参数核平滑与高斯过程极值分布引入多重假设检验以控制 FDR，直接契合您在假设检验与非参数理论方面的 primary interests；其 O(n) 算法与 R 包实现也对统计计算兴趣有参考价值。

### 12. [10.5705/ss.202025.0155](https://doi.org/10.5705/ss.202025.0155) — Subgroup Testing in Change-Plane Models and Its Applications to Medical Data
- **作者**: Xu Liu, Jian Huang, Yong Zhou, Feipeng Zhang, Panpan Ren
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究 change-plane 模型中系数的假设检验问题，旨在检测变点平面的存在性，其核心难点在于零假设下分组参数不可识别（non-identifiable under null）。针对经典指数平均检验功效不佳的问题，作者提出了加权平均平方得分检验统计量（WAST），通过对分组参数空间上的平方得分统计量取加权平均，并在适当权重下获得了闭式表达。推导了 WAST 在零假设与备择假设下的渐近分布，并提出了具有理论保证的 Bootstrap 方法来逼近临界值。方法进一步扩展至广义估计方程（GEE）框架及多重变点平面情形，模拟与三个医学数据集的应用展示了 WAST 在提升检验功效方面的优势。对您有用：该文处理的是非正则条件下（参数不可识别）的假设检验问题，其构造 WAST 的思路与渐近理论对您在数学统计（hypothesis testing）方向的研究有直接参考价值，且医学数据应用契合流行病学因果推断的亚组分析场景。
- **关键技术**: `change-plane model`, `score test statistic`, `non-identifiable parameter under null`, `weighted average test (WAST)`, `bootstrap approximation`, `generalized estimating equation (GEE)`
- **为什么对您有用**: 直接关联您在数学统计（hypothesis testing）方向的兴趣，特别是非正则（零假设下参数不可识别）检验统计量的构造与渐近性质推导；同时，change-plane 模型在流行病学与因果推断的异质性处理效应（subgroup/personalized treatment）评估中应用广泛，方法与数据集均具迁移价值。

### 13. [10.5705/ss.202025.0126](https://doi.org/10.5705/ss.202025.0126) — A Variation-Ratio Test for Volatility Jumps Using Noisy High Frequency Data
- **作者**: Guangying Liu, Kewen Shi, Zhiyuan Zhang
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `sharper_rate`
- **摘要**: 本文在带有微观结构噪声的高频数据设定下，研究波动率跳跃的检验问题，目标是区分波动率是否为连续半鞅。提出了一种基于变差比（variation-ratio）的检验统计量，在原假设（无波动率跳跃）下渐近正态。在备择假设下，该统计量以 n^{1/4-ε} 的速率发散，显著优于现有文献中最优的约 n^{1/8} 发散速率。方法核心在于利用不同采样频率下的变差比来分离微观结构噪声与跳跃信号。模拟与对90支美股的实证分析验证了理论，发现相当比例的股票存在波动率跳跃。对您有用：该文直接推进了数学统计中假设检验的理论，提供了更尖锐的检验发散速率，且高频金融数据的实证对经济理论应用有参考价值。
- **关键技术**: `variation-ratio test`, `high-frequency data inference`, `microstructure noise`, `asymptotic normality`, `rate of divergence`
- **为什么对您有用**: 直接推进了数学统计中假设检验的理论，提供了比现有文献更尖锐的检验发散速率（n^{1/4} vs n^{1/8}）；同时高频金融数据的实证分析对经济理论（波动率建模）有参考价值。

### 14. [10.5705/ss.202024.0078](https://doi.org/10.5705/ss.202024.0078) — Structural Testing of High-dimensional Correlation Matrices
- **作者**: Tingting Zou, Guangren Yang, Ruitao Lin, Guoliang Tian, Shurong Zheng
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究高维相关矩阵的一般线性结构检验问题，目标是在高维设定下检验相关矩阵是否满足如带状或复合对称等特定线性结构，这因尺度不变性而与协方差矩阵检验有本质不同。作者首先基于二次损失函数提出了结构中未知参数的估计程序；随后分别针对稠密和稀疏备择假设，构造了基于二次范数（L2）和无穷范数（L∞）的检验统计量。在原假设和备择假设下，分别推导了所提检验统计量的极限分布，并通过模拟与实证分析验证了有限样本表现。对您有用：该文将高维假设检验中的L2/L∞范数检验范式拓展至相关矩阵的一般线性结构，对您在高维统计与假设检验交叉领域的研究有直接参考价值。
- **关键技术**: `high-dimensional correlation matrix`, `quadratic loss estimation`, `L2 and Linfinity norm test statistics`, `dense and sparse alternatives`, `limiting distributions`
- **为什么对您有用**: 直接契合您在“高维统计”与“假设检验”方面的核心兴趣，文中针对稠密/稀疏备择假设分别构造L2/L∞检验统计量的思路，可为您在高维协方差/相关矩阵推断中的理论推导提供方法借鉴。

### 15. [10.5705/ss.202025.0327](https://doi.org/10.5705/ss.202025.0327) — A Data-Adaptive Integrated Approach to Covariance Change Point Detection in High-dimensional Settings
- **作者**: Canhuang Xu, Lei Shu, Yu Chen, Qing Yang
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维随机向量序列中，本文研究协方差矩阵变点的检测问题，目标是在维度 p 可远大于样本量 n 的设定下识别协方差结构的变化点。提出一种 reweighted CUSUM-type 统计量，通过 data-adaptive 参数选择方法优化权重确定，避免手动调参。基于该统计量构建了完整的变点检测框架：先做变点存在性的假设检验，再进行变点位置估计。理论上证明了参数选择方法的有效性以及变点估计的 consistency，但摘要未明确给出收敛速率或检测边界（detection boundary）的具体形式。仿真与实际数据验证了方法的实用性。对您的高维假设检验研究有参考价值，特别是 reweighted CUSUM 在高维协方差变点检测中的 data-adaptive 构造思路可迁移至其他高维检验问题。
- **关键技术**: `reweighted CUSUM statistic`, `data-adaptive parameter selection`, `high-dimensional covariance change point`, `consistency of change point estimation`, `hypothesis testing for change point existence`
- **为什么对您有用**: 直接关联您的高维统计与假设检验两个 primary interest；reweighted CUSUM 的 data-adaptive 权重构造思路可迁移至其他高维检验场景，但未涉及 RMT 工具或效率理论，理论深度偏中档。

### 16. [10.5705/ss.202024.0153](https://doi.org/10.5705/ss.202024.0153) — Tests on Dynamic Ranking
- **作者**: Nan Lu, Jian Shi, Xin-Yu Tian, Kai Song
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究动态 Bradley-Terry 模型下的假设检验问题，关注动态得分函数变异性与成对相似性的检验，以及动态排序性质的推断。针对得分变异和成对相似性，构造了相应检验统计量并推导其渐近零分布，证明了检验的相合性。为解决由上确界型统计量带来的保守性问题，引入基于符号得分差的统计量进行排序推断。此外，提出了动态排序的置信带构造方法及一般性的动态排序性质检验框架。理论上给出了所提方法的渐近保证，模拟与实证也验证了其有效性。对您有用：本文处理上确界型统计量保守性的技巧及渐近分布推导，直接契合您在数学统计与假设检验方向的兴趣，且动态排序模型在经济与流行病学成对比较数据中有应用潜力。
- **关键技术**: `dynamic Bradley-Terry model`, `supreme-type test statistic`, `signed score difference statistic`, `asymptotic null distribution`, `confidence band for dynamic rank`
- **为什么对您有用**: 直接契合您在“数学统计与假设检验”方向的兴趣，特别是处理上确界型统计量保守性的技巧；动态 Bradley-Terry 模型也可迁移至经济学或流行病学中的成对比较数据分析。

### 17. [10.5705/ss.202024.0035](https://doi.org/10.5705/ss.202024.0035) — An Automatic MDDM-Based Test for Martingale Difference Hypothesis
- **作者**: Chenglong Zhong, Guochang Wang
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多变量时间序列参数条件均值模型下，目标是检验误差项是否为鞅差序列（MDH），而现有基于鞅差散度矩阵（MDDM）的检验需预设滞后阶数。本文提出一种数据驱动的自动 MDDM 检验，通过从数据中自适应选择滞后阶数克服了该限制。核心机制在于：原假设下自动选择的滞后阶数依概率收敛于 1，从而简化了渐近分布；而在备择假设下，该方法能有效检测高阶依赖导致的模型设定不足。理论上证明了所提检验统计量的渐近性质及一致性。模拟与实证表明该自动检验在检测高阶依赖时具有优异功效。该工作直接推进了您关注的假设检验理论，且 MDDM 的渐近推导与非参数依赖度量及高阶 U 统计量投影技术密切相关，其自适应阶数选择机制对时间序列因果推断中的混淆因素检验亦有参考价值。
- **关键技术**: `Martingale Difference Divergence Matrix (MDDM)`, `automatic lag order selection`, `martingale difference hypothesis testing`, `multivariate time series`, `asymptotic distribution theory`
- **为什么对您有用**: 直接契合您在数学统计（假设检验）方向的兴趣；MDDM 的渐近理论推导与非参数依赖度量及高阶 U 统计量投影紧密相关，且自适应阶数选择机制对时间序列因果推断中的高阶混淆依赖检验有方法迁移价值。

### 18. [10.5705/ss.202024.0266](https://doi.org/10.5705/ss.202024.0266) — Center-Outward Ranks and Signs for Testing Conditional Quantile Independence
- **作者**: Kai Xu, Huijun Shi, Daojiang He
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究多维条件下分位数独立性（conditional quantile independence）的非参数渐近分布自由检验问题，目标是在无矩假设下构造无需 bootstrap 校准的检验统计量。方法核心是将 quantile martingale difference divergence（QMDD）与近年提出的 multivariate center-outward ranks and signs 相结合，利用 QMDD 的退化 V-type / U-type 结构以及 center-outward ranks 的 Glivenko-Cantelli 强一致性与分布自由性，导出检验统计量的渐近零分布表示，从而可直接计算极限零分布而无需重抽样。理论证明 center-outward 版 QMDD 检验对所有固定替代一致，且局部功效分析表明在 root-n 邻域内具有非平凡功效。该方法无需矩假设、计算可行，模拟与基因表达数据实证均验证了优势。对您有用之处在于：退化 U/V-statistic 渐近表示技术与 center-outward rank 的分布自由性可直接迁移到您关注的 higher-order U-statistics 理论与非参数假设检验问题中。
- **关键技术**: `center-outward ranks and signs`, `quantile martingale difference divergence`, `degenerate V-type and U-type statistics`, `Glivenko-Cantelli consistency`, `local power over root-n neighborhoods`, `distribution-free testing`
- **为什么对您有用**: 直接关联您 primary interest 中的 hypothesis testing 与 higher-order U-statistics：论文对退化 U/V-statistic 结构的渐近零分布推导以及 center-outward rank 的分布自由性质，为非参数检验中绕过 bootstrap 提供了可迁移的技术路线。

### 19. [10.5705/ss.202024.0330](https://doi.org/10.5705/ss.202024.0330) — Weighted Conditional Network Testing for Multiple High-Dimensional Correlated Data Sets
- **作者**: Takwon Kim, Inyoung Kim, Ki-Ahm Lee
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维高斯图模型设定下，本文研究在给定其他精度矩阵条件下的两个精度矩阵相等性检验问题。提出一种加权条件网络检验方法，通过引入权重矩阵整合条件依赖的其他网络信息，构建针对条件精度矩阵差异的检验统计量。理论部分证明了该统计量在高维设定下的渐近性质，克服了现有方法无法处理条件网络差异检验的局限。模拟与基因通路分析验证了方法在控制第一类错误和提升检验功效上的优势。该文直接推进了高维假设检验与精度矩阵推断理论，其条件检验框架对您在 high-dimensional statistics 与 hypothesis testing 交叉领域的研究具有直接参考价值。
- **关键技术**: `high-dimensional hypothesis testing`, `precision matrix`, `Gaussian graphical models`, `conditional network testing`, `weighted test statistic`
- **为什么对您有用**: 直接对应您在 high-dimensional statistics 与 mathematical statistics (hypothesis testing) 的核心兴趣，提供了高维精度矩阵条件相等性检验的新方法与渐近理论。

### 20. [10.5705/ss.202024.0051](https://doi.org/10.5705/ss.202024.0051) — Spatial-Sign Based Maxsum Test for High Dimensional Location Parameters
- **作者**: Jixuan Liu, Long Feng, Ping Zhao, Zhaojun Wang
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在高维位置参数检验设定下，本文提出基于空间符号（spatial-sign）的稳健检验方法以应对未知稀疏度的备择假设。作者首先构造了针对稀疏信号的 spatial-sign max-type 检验统计量，随后严格证明了该 max-type 统计量与现有的 spatial-sign sum-type 统计量之间的渐近独立性。基于此独立性结果，文章构建了 max-sum 组合检验程序，自适应于信号的稀疏与稠密情形。理论结果表明该组合检验保持了水平稳健性（尤其是对重尾分布），模拟也验证了其在不同稀疏度下的功效优势。对您有用：直接推进了高维假设检验理论，max-sum 统计量渐近独立性的证明技巧及组合检验思路可为您在高维检验方向的研究提供直接参考。
- **关键技术**: `spatial-sign transformation`, `max-type test statistic`, `sum-type test statistic`, `asymptotic independence`, `high-dimensional location testing`, `sparse alternatives`
- **为什么对您有用**: 直接对应您 primary interest 中的高维统计与假设检验；max-type 与 sum-type 统计量的渐近独立性证明及组合检验策略，对处理高维稀疏/稠密信号检验问题具有直接的方法论迁移价值。

### 21. [10.5705/ss.202024.0255](https://doi.org/10.5705/ss.202024.0255) — Testing for Treatment Effect in Multitreatment Case
- **作者**: Pier Luigi Conti, Livia De Giovanni, Ayoub Mounim
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究多水平处理效应存在性的非参数假设检验问题，目标是在多处理组设定下检验处理效应是否为零以及随机占优关系。作者提出一种基于经典 Kruskal-Wallis 检验原理的新检验统计量，并推导了其渐近理论性质；同时针对随机占优问题构造了相应的检验统计量。模拟实验表明，相较于常用检验方法，所提检验在控制第一类错误和检验功效上表现更优，并附带真实数据验证。对您有用：直接契合您对假设检验的兴趣，其多值处理下的非参数秩检验构造可为因果推断中多值处理的效应评估提供方法学参考。
- **关键技术**: `Kruskal-Wallis test`, `rank-based test`, `stochastic dominance`, `nonparametric hypothesis testing`, `multitreatment comparison`
- **为什么对您有用**: 直接契合您在数学统计中对假设检验的兴趣；多水平处理效应和随机占优的检验构造可为因果推断中多值处理的效应评估提供非参数检验思路。

### 22. [10.5705/ss.202024.0002](https://doi.org/10.5705/ss.202024.0002) — A Locally Adaptive Algorithm for Multiple Testing with Network Structure
- **作者**: Ziyi Liang, T. Tony Cai, Wenguang Sun, Yin Xia
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维多重检验设定下，研究如何整合与主数据维度或结构不同的辅助信息（如网络、空间）以提升检验功效，目标是在控制 FDR 的前提下优化 power。提出 LASLA（locally adaptive structure learning algorithm）算法，采用 p-value weighting 策略，利用网络拓扑或空间结构提取数据驱动的权重以区分假设重要性。理论证明在 p 值独立或弱相依条件下，LASLA 渐近控制 FDR，并在辅助信息有效时严格提升 power。仿真与真实数据（网络/空间结构）验证了其数值表现。对您有用：该文直接推进您 primary interest 中的 mathematical statistics & hypothesis testing，其利用图结构进行 p-value 加权的思想可迁移至高维因果推断中多重干预/结局的多重比较问题。
- **关键技术**: `multiple testing`, `FDR control`, `p-value weighting`, `network structure`, `side information integration`
- **为什么对您有用**: 直接属于您 primary interest 中的 mathematical statistics & hypothesis testing 方向；其利用网络/空间辅助信息进行 p-value 加权的框架，对高维因果推断中多重处理/结局的多重比较问题有方法迁移价值。

### 23. [10.5705/ss.202024.0249](https://doi.org/10.5705/ss.202024.0249) — Catoni-type Confidence Sequences under Infinite Variance
- **作者**: Guanhua Fang, Sujay Bhatt, Ping Li, Gennady Samorodnitsky
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文在数据生成分布方差无限（仅存在 $p \in (1,2)$ 阶矩）的重尾设定下，构建了在任意数据依赖停止时间下均有效的置信序列。作者利用 Ville 不等式推导了 Catoni 型置信序列，改进了基于 Dubins-Savage 不等式的现有上界；进一步建立了 $p \in (1,2]$ 时该置信序列宽度的下界，揭示了单纯依赖 Ville 不等式的统计局限性。为弥补上下界间隙，引入 stitching 技巧构建了更紧的置信序列。理论结果在重尾设定下实现了更优的宽度收敛率，可应用于风险控制和参数估计。对您有用：直接推进了数学统计中 anytime-valid inference 与序贯假设检验的理论，且下界结果与 stitching 技巧对理解检验极限与重尾半/非参数推断具有迁移价值。
- **关键技术**: `Catoni estimator`, `confidence sequences`, `Ville's inequality`, `stitching method`, `heavy-tailed inference`, `anytime-valid inference`
- **为什么对您有用**: 直接推进了数学统计中 anytime-valid inference 与序贯假设检验的理论；Catoni 估计与 stitching 技巧在重尾半/非参数理论中具有迁移价值，且下界结果对理解检验的统计极限有启发。

### 24. [10.5705/ss.202024.0106](https://doi.org/10.5705/ss.202024.0106) — On Runs Tests for Directional Data and Their Local and Asymptotic Optimality Properties
- **作者**: Maxime Boucher, Christian Francq, Yuichi Goto, Thomas Verdebout
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究方向性数据（directional data）中序列相关性的检测问题，目标是在单位球面上定义适用于方向性数据的 runs 概念并构建假设检验。作者将经典 runs 检验推广至方向性设定，提出基于方向性 runs 的检验统计量，并证明其在局部序列依赖备择假设下具有局部渐近最优性（local asymptotic optimality）。理论分析采用局部渐近正态性（LAN）框架，刻画了检验的局部渐近势函数。Monte Carlo 模拟评估了有限样本表现，并以太阳黑子位置（sunspots）多周期数据作实证分析。对您有用：该文将 runs 检验与 LAN 最优性理论结合，直接契合您对 hypothesis testing 与数学统计理论的兴趣；太阳黑子数据也可作为 astrostatistics 入门阅读的数据实例。
- **关键技术**: `runs test for directional data`, `local asymptotic normality (LAN)`, `local asymptotic optimality`, `serial correlation detection`, `directional statistics on sphere`
- **为什么对您有用**: 直接契合您 primary interest 中的 hypothesis testing 与数学统计理论（LAN 框架下的局部渐近最优性）；太阳黑子实证部分为 astrostatistics 提供了可访问的数据分析案例。

### 25. [10.5705/ss.202023.0408](https://doi.org/10.5705/ss.202023.0408) — A Robust Framework for Graph-Based Two-Sample Tests Using Weights
- **作者**: Yichuan Bai, Lynna Chu
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究高维数据下的非参数两样本检验问题，针对基于相似图（如 K-最小生成树）的检验在图结构存在异常（如 hub 节点）时功效低下且不稳定的问题。作者提出一种基于边加权的稳健图检验统计量，利用图的内在特征对边进行加权，以削弱 hub 节点对检验统计量的过度影响。推导了该稳健检验统计量的极限零分布，并证明了其在有限样本下的适用性。该加权策略计算简单高效，无需复杂优化。模拟研究与芝加哥出租车数据的实证分析表明，新方法在多种设定下显著提升了检验功效和稳定性。该工作直接推进了高维非参数假设检验理论，其针对图结构异常的稳健性加权思路可为您在假设检验或高维推断中的研究提供新视角。
- **关键技术**: `graph-based two-sample test`, `edge-weighting strategy`, `K-minimum spanning tree`, `limiting null distribution`, `robust test statistic`
- **为什么对您有用**: 直接契合您在数学统计（假设检验）和非参数理论方面的核心兴趣；针对高维数据图结构异常提出的稳健加权策略，为高维假设检验的稳定性与功效提升提供了新思路。

### 26. [10.5705/ss.202022.0397](https://doi.org/10.5705/ss.202022.0397) — Localizing Multivariate CAViaR
- **作者**: Xiu Xu, Yegor Klochkov, Li Chen, Wolfgang Karl Härdle
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在多变量 CAViaR（条件自回归 VaR）框架下，研究金融市场极端风险传染的时变结构，目标是检验参数齐性并实现局部自适应估计。作者构建了一个参数齐性检验统计量，采用完全数据驱动的临界值，并证明了该临界值能达到预设的渐近置信水平。基于此检验，提出了一种能够自适应参数时变特性的局部估计程序，核心依赖于非参数局部化技术与多变量分位数回归的结合。模拟与美、德金融市场实证表明，该方法能有效检测结构性变化并刻画动态尾部风险溢出，发现美国市场在风险传染中起主导作用。对您而言，其参数齐性检验的构造与数据驱动临界值推导可为数学统计中的假设检验与变点检测提供方法借鉴，同时金融风险溢出的实证模式也契合经济理论应用兴趣。
- **关键技术**: `parameter homogeneity test`, `data-driven critical values`, `localized estimation`, `multivariate CAViaR`, `quantile regression`
- **为什么对您有用**: 本文的参数齐性检验构造与数据驱动临界值推导直接关联您的数学统计（假设检验）兴趣，同时其金融风险溢出的实证应用契合您的经济理论（应用模型）兴趣，可为您在时变参数模型下的假设检验提供方法迁移。

### 27. [10.5705/ss.202024.0037](https://doi.org/10.5705/ss.202024.0037) — Testing High-dimensional White Noise Based On Modified Portmanteau Tests
- **作者**: Zeren Zhou, Min Chen
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维时间序列设定下，本文研究非独立同分布白噪声的检验问题，目标是在维度 p 随样本量 n 发散时构造有效的 portmanteau 检验统计量。方法基于修正的高维 portmanteau 统计量，通过聚合高维自协方差矩阵的信息来检测密集型备择假设（dense alternatives）。由于高维下统计量的渐近分布难以解析获得，作者采用 multiplier bootstrap 方法逼近检验的临界值。理论上证明了在零假设下 bootstrap 检验的渐近水平有效性，并在模拟与实例中展示了该方法对密集备择假设的检验功效优于现有方法。对您有用：该文将经典低维检验推广至高维并使用 bootstrap 计算临界值，直接契合您在 high-dimensional hypothesis testing 与 statistical computing 方向的兴趣，其 multiplier bootstrap 技术在高维推断中具有可迁移性。
- **关键技术**: `high-dimensional white noise test`, `modified portmanteau test`, `multiplier bootstrap`, `dense alternatives`, `high-dimensional time series`
- **为什么对您有用**: 直接契合您在 high-dimensional hypothesis testing 的核心兴趣，展示了如何用 multiplier bootstrap 解决高维下渐近分布难以解析推导的计算问题，对高维检验的构造与计算有参考价值。

## 统计计算 / 算法  *(stat_computing, 17 篇)*

### 1. [10.5705/ss.202024.0308](https://doi.org/10.5705/ss.202024.0308) — Heterogeneous Autoregressive Modeling with Flexible Cascade Structures
- **作者**: Huiling Yuan, Guodong Li, Kexin Lu, Alan T.K. Wan, Yong Zhou
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对高频数据的已实现测度预测，提出多线性低秩异质自回归（MLRHAR）模型，在经典HAR框架下用数据驱动方式替代固定的异质波动成分。为处理日历效应，引入四阶张量结构同时在响应、预测变量、短期与日历时间四个方向降维，自动选择异质成分并大幅缩减参数空间。理论上建立了高维HAR模型的非渐近性质，并提出带理论保证的投影梯度下降算法进行参数估计。模拟与S&P 500成分股实盘数据均显示预测优势。对您有用之处在于：张量降维与非渐近分析的组合可直接迁移到您关注的高维统计与统计计算（张量算法）交叉研究中，投影梯度下降的收敛保证也可作为算法理论参考。
- **关键技术**: `tensor decomposition (multilinear low-rank)`, `non-asymptotic analysis`, `projected gradient descent`, `heterogeneous autoregressive model`, `calendar effect modeling`, `high-dimensional HAR`
- **为什么对您有用**: 四阶张量降维与投影梯度下降算法直接对应您 primary interest 中的统计计算（matrix/tensor 数值方法）；高维HAR的非渐近界可为高维统计理论提供新的 rate 参照。

### 2. [10.5705/ss.202023.0332](https://doi.org/10.5705/ss.202023.0332) — Likelihood-free Gibbs Sequential Monte Carlo Sampling
- **作者**: Weixuan Zhu, Wei Li, Weining Shen
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对不可解似然(intractable likelihood)模型的 Bayesian 推断，在 ABC 框架下解决参数维度增大时的维度灾难问题。核心方法是将 Gibbs kernel 嵌入 Sequential Monte Carlo (SMC) 框架，逐分量更新参数，并利用多种 regression adjustment 方法近似各参数的条件后验分布。作者证明了 Gibbs kernel 在此设定下的理论性质（收敛性），并讨论了相较于全参数联合 SMC-ABC 的计算优势：Gibbs 分解将高维问题降为一系列低维条件采样，缓解了 summary statistic 匹配在高维下的效率衰减。模拟与细胞运动(cell motility)实例表明，在中等至高维参数空间下，Gibbs SMC-ABC 的精度和有效样本量显著优于标准 SMC-ABC 与 MCMC-ABC。对您而言，该工作直接属于 statistical computing 方向，Gibbs-SMC 的算法设计思路和 kernel 理论性质分析可迁移至其他 likelihood-free 或复杂后验采样场景。
- **关键技术**: `Gibbs kernel`, `Sequential Monte Carlo`, `Approximate Bayesian computation`, `regression adjustment`, `conditional posterior approximation`, `likelihood-free inference`
- **为什么对您有用**: 直接对应您 primary interest 中的 statistical computing（数值方法与算法）；Gibbs-SMC 的逐分量降维策略和 kernel 收敛理论分析，对处理高维参数的 likelihood-free 推断具有方法学迁移价值。

### 3. [10.5705/ss.202024.0342](https://doi.org/10.5705/ss.202024.0342) — Functional Tensor Regression
- **作者**: Tongyu Li, Fang Yao, Anru R. Zhang
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究协变量兼具张量结构与函数光滑性时的回归问题，提出 functional tensor regression 框架，目标是在 Tucker 低秩与函数光滑双重正则下估计高维回归系数。方法核心是对系数张量施加低 Tucker rank 分解，同时对函数模式施加光滑惩罚，从而同时缓解维度灾难与保证函数连续性。计算上提出 functional Riemannian Gauss-Newton 算法，证明了二次收敛速率；理论上给出依赖于张量协变量维度的估计误差界。模拟与神经影像数据分析验证了有限样本表现。对您有用之处在于：Riemannian 优化算法的可证明二次收敛为统计计算方向提供了可迁移的数值方法思路，Tucker 低秩加光滑正则的组合策略也可借鉴到高维张量推断问题中。
- **关键技术**: `Tucker rank decomposition`, `Riemannian Gauss-Newton optimization`, `smooth regularization`, `functional tensor regression`, `quadratic convergence rate`
- **为什么对您有用**: 直接命中您 primary interest 中的 statistical computing（数值方法与算法）：Riemannian Gauss-Newton 的可证明二次收敛是少见的优化收敛率结果；同时 Tucker 低秩估计误差界与您 high-dimensional statistics 兴趣相关，方法框架可迁移至高维张量推断。

### 4. [10.5705/ss.202024.0281](https://doi.org/10.5705/ss.202024.0281) — Generalized Tensor Regression with Internal Variation Regularization
- **作者**: Yang Bai, Ting Li, Yang Sui
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在广义张量回归设定下，目标是估计标量与张量系数，并利用高阶影像数据的分段常数空间结构。本文提出带有内部变异（IV）正则化的广义张量回归框架，通过 IV 正则化显式捕捉影像的分段常数特性。开发了高效的 IV 正则化优化算法，并推导了估计量的理论性质，特别是给出了正则化张量系数估计的误差界。模拟与慢性鼻窦炎 CT 影像数据应用表明该方法优于现有方法，识别出与诊断相关的最激活子区域。对您有用：该文的张量优化算法与误差界分析对您在统计计算（张量/矩阵算法）及高维统计推断方面的兴趣有直接参考价值，同时提供了流行病学影像数据的分析范式。
- **关键技术**: `generalized tensor regression`, `Internal Variation regularization`, `error bounds`, `regularized optimization`, `piecewise constant structure`
- **为什么对您有用**: 张量优化算法与误差界分析对您在统计计算（张量/矩阵算法）及高维统计推断的兴趣有直接参考价值，同时提供了流行病学影像数据的分析范式。

### 5. [10.5705/ss.202024.0109](https://doi.org/10.5705/ss.202024.0109) — Joint Mean and Correlation Regression Models for Multivariate Data
- **作者**: Zhi Yang Tho, Francis K. C. Hui, Tao Zou
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 针对多元离散与半连续响应数据，提出联合均值与相关性回归模型，将响应均值关于协变量回归、响应间相关性关于相似性/距离度量回归，设定中允许响应维度 m→∞。构造联合估计方程估计均值系数与相关性参数，证明了在均值系数跨响应异质且维度发散时，联合估计量相合且渐近正态，并明确推导出不同参数的异质收敛速率。开发了在约束参数空间内求解的迭代估计算法。模拟与苏格兰甲虫计数数据应用验证了方法表现。对您有用：该文在响应维度发散下的异质收敛速率理论，对您在 high-dimensional statistics 中处理不同参数收敛阶的问题有参考价值，其约束参数空间的迭代算法也可供 stat_computing 借鉴。
- **关键技术**: `joint estimating equations`, `diverging dimension asymptotics`, `varying convergence rates`, `correlation regression`, `constrained iterative estimation`
- **为什么对您有用**: 涉及响应维度发散下的渐近理论（不同收敛速率），与您 primary interest 中的 high-dimensional statistics 渐近性质相关；其约束参数空间的迭代求解算法对 stat_computing 有借鉴意义。

### 6. [10.5705/ss.202024.0346](https://doi.org/10.5705/ss.202024.0346) — Gaussian Variational Approximation with Composite Likelihood for Crossed Random Effect Models
- **作者**: Libai Xu, Nancy Reid, Dehan Kong
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在交叉随机效应模型（crossed random effect models）的 Poisson 和 Gamma 回归设定下，针对全似然计算困难的问题，本文提出结合复合似然（composite likelihood）与高斯变分近似（Gaussian variational approximation）的估计方法。复合似然忽略响应分量间的依赖以简化结构，而变分近似忽略参数分量间的依赖以加速优化；两者结合进一步降低了计算复杂度。作者推导了基于复合对数似然的高斯变分近似目标函数，并严格证明了所得估计量的一致性与渐近正态性。模拟实验表明，相较于基于全对数似然的高斯变分近似，该方法在计算速度上有显著提升，同时保持了良好的有限样本性质。对您有用：若您在纵向因果推断或流行病学应用中遇到交叉随机效应的高维积分计算瓶颈，此变分近似算法与渐近理论提供了计算与推断的折中方案。
- **关键技术**: `Gaussian variational approximation`, `composite likelihood`, `crossed random effects`, `asymptotic normality`, `Poisson regression`
- **为什么对您有用**: 涉及统计计算（数值近似算法）与数学统计（渐近正态性证明），且交叉随机效应模型在纵向因果推断与流行病学中有广泛应用，其计算加速方案对处理大规模层级数据有参考价值。

### 7. [10.5705/ss.202024.0194](https://doi.org/10.5705/ss.202024.0194) — Convoluted Support Matrix Machine in High Dimensions
- **作者**: Bingzhen Chen, Canyi Chen
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在高维矩阵输入的二分类设定下，针对传统 SVM 铰链损失非光滑导致的理论与计算瓶颈，本文提出一种凸光滑化支持矩阵机。方法核心是对铰链损失进行凸光滑化近似，并引入 elastic-net 型惩罚以处理高维矩阵协变量。理论上证明了该方法在高维设定下达到最优统计收敛速率；计算上，光滑凸损失使得算法具有线性收敛速率且实现简单。模拟与脑电图数据验证了其分类精度与计算效率。对您有用之处在于：其高维矩阵分类的 elastic-net 惩罚与最优收敛速率分析，以及光滑化损失下的快速优化算法，可为高维统计与统计计算（数值优化）方向提供方法学参考。
- **关键技术**: `convex smoothing of hinge loss`, `elastic-net penalty for matrix inputs`, `optimal statistical convergence rate`, `linear convergence optimization`, `support matrix machine`
- **为什么对您有用**: 涉及高维矩阵输入的 elastic-net 惩罚与最优收敛速率，以及光滑凸优化算法的线性收敛性质，直接关联您的高维统计与统计计算（数值优化算法）兴趣。

### 8. [10.5705/ss.202024.0318](https://doi.org/10.5705/ss.202024.0318) — Estimating Shapley Effects in Big-Data Emulation and Regression Settings using Bayesian Additive Regression Trees
- **作者**: Akira Horiguchi, Matthew T. Pratola
- **期刊/来源**: Statistica Sinica
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在非参数回归与计算机实验仿真设定下，本文目标是估计高维输入（$p$ 达数百）下函数对输入依赖程度的 Shapley effects（全局敏感性指标）。现有估计量在 $p$ 为数百量级时计算不可行，本文提出基于元模型的估计量：先拟合 Bayesian Additive Regression Trees (BART)，再利用拟合模型计算 Shapley-effect，突破了高维计算瓶颈。理论上，本文在较宽泛的函数类上证明了该 Shapley-effect 估计量的后验一致性。数值实验表明，该方法在 $p=500$ 的测试函数上仍具计算可行性。对您而言，若关注高维非参数回归的计算方法或 BART 的理论性质，本文提供了具体案例；但需注意此处的 Shapley effect 属于方差分解的敏感性分析，而非因果中介分析。
- **关键技术**: `Shapley effects`, `Bayesian Additive Regression Trees`, `posterior consistency`, `metamodel-based estimation`, `global sensitivity analysis`
- **为什么对您有用**: 本文聚焦高维输入下敏感性分析的计算与 BART 的后验一致性理论，对您在统计计算（高维算法可解性）和非参数理论方面的兴趣有参考价值；但需区分此处的 Shapley effect 与因果推断中的 Shapley value。

### 9. [10.5705/ss.202024.0145](https://doi.org/10.5705/ss.202024.0145) — Construction of Maximin Distance Latin Hypercube Designs via Good Lattice Point Sets
- **作者**: Xueru Zhang, Dennis K.J. Lin, Wei Zheng
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究计算机实验中 space-filling Latin hypercube design (LHD) 的构造问题，目标是在任意行数和灵活列数下获得 maximin distance 性质的设计。方法为混合策略：代数部分基于 good lattice point (GLP) 集与 level permutation 技术生成初始设计，适用于任意行数；算法部分进一步搜索覆盖代数方法无法处理的列数组合。对代数组件给出了 maximin Lp-distance 最优性的理论分析；数值实验表明所得设计在 Lp-distance、列正交性和投影均匀性上均表现良好。该工作与您的主要兴趣关联较弱，仅算法构造思路（代数+搜索的混合策略）对统计计算中的组合优化问题有间接参考价值。
- **关键技术**: `good lattice point sets`, `level permutation`, `maximin distance criterion`, `Latin hypercube design`, `space-filling design`
- **为什么对您有用**: 与您 primary interest 中的统计计算（数值方法与算法）仅有弱关联——涉及组合搜索算法设计，但不涉及矩阵/张量计算或数值线性代数；其余方向（因果推断、高维/RMT、半参数效率等）基本无直接联系。

### 10. [10.5705/ss.202023.0287](https://doi.org/10.5705/ss.202023.0287) — Consistent Community Detection in Multi-Layer Networks with Heterogeneous Differential Privacy
- **作者**: Yaoming Zhen, Shirong Xu, Junhui Wang
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 在多层网络与异质差分隐私框架下，本文研究社区检测的效用问题，设定为多层度修正随机块模型（DCSBM）。核心机制是个性化边翻转，允许数据发布者根据节点隐私偏好保护边信息。通过适当的去偏处理，多层 DCSBM 下的社区结构在隐私扰动后保持不变，从而实现一致的社区检测。理论上，文章证明了去偏后社区检测的一致性，并严格刻画了隐私-效用权衡。该工作展示了去偏技术在隐私保护网络模型中的有效性；对您而言，其去偏策略与隐私-效用权衡的理论分析在统计计算（差分隐私）和高维网络模型推断中具有借鉴意义。
- **关键技术**: `heterogeneous differential privacy`, `multi-layer degree-corrected stochastic block model`, `edge-flipping mechanism`, `debiasing`, `privacy-utility tradeoff`
- **为什么对您有用**: 涉及统计计算中的差分隐私机制与高维网络模型的去偏估计，其去偏思想与 privacy-utility 权衡的理论刻画对您在 stat_computing 和高维推断方面的研究有方法论参考。

### 11. [10.5705/ss.202025.0279](https://doi.org/10.5705/ss.202025.0279) — Space-filling Designs with Kronecker Product Structures under Kernel-Based Criteria
- **作者**: Ruonan Zheng, Xinran Zhang, Jian-Feng Yang, Min-Qian Liu
- **期刊/来源**: Statistica Sinica
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 本文研究计算机实验中具有 Kronecker 乘积结构的空间填充设计，目标是在核函数准则下建立不同空间填充准则之间的系统联系。核心机制是将多种空间填充准则（如最大距离、最小势等）统一表达为核函数形式，利用核函数的优雅性质推导准则间的等价与序关系。针对 Kronecker 乘积结构设计，给出了核准则的显式表达式及相应理论结果，并提出了最优设计的构造方法与一个生成算法，所得设计在数值比较中优于现有方案。对您而言，Kronecker 结构与核函数的显式分解可能对统计计算中矩阵/张量算法设计有迁移价值，但整体属于实验设计领域，与您核心兴趣的直接重叠有限。
- **关键技术**: `Kronecker product structure`, `kernel-based space-filling criteria`, `RKHS connection`, `optimal design construction`, `space-filling design algorithm`
- **为什么对您有用**: Kronecker 乘积结构的显式分解与核函数统一框架对统计计算中的矩阵/张量数值方法有潜在迁移价值，但论文核心贡献在实验设计而非推断或高维理论，与您 primary interests 的直接重叠较小。

### 12. [10.5705/ss.202024.0215](https://doi.org/10.5705/ss.202024.0215) — Distributed Sequential Federated Estimation
- **作者**: Zhanfeng Wang, Xinyu Zhang, Yuan-chin Chang
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在分布式多站点数据场景下，简单平均聚合因数据非同质性会导致信息损失，本文研究如何在不集中数据的前提下进行统计有效的信息整合。作者将经典序贯自适应设计（sequential adaptive design）原则引入联邦学习框架，提出一种数据驱动的分布式序贯联邦估计方法，兼顾数据安全与估计效率。方法通过序贯更新机制逐步整合各站点信息，避免了全局迭代通信的开销，同时处理站点间异质性带来的可比性问题。理论上方法保持了经典序贯设计的渐近性质；数值模拟和墨西哥 32 家医院 COVID-19 回归数据的应用验证了其有限样本表现。对您而言，该文在分布式计算算法设计上提供了可借鉴的序贯整合思路，COVID-19 多中心数据集也可作为流行病学应用中联邦因果推断的参考案例。
- **关键技术**: `federated learning`, `sequential adaptive design`, `distributed estimation`, `data homogeneity adjustment`, `regression under non-homogeneity`
- **为什么对您有用**: 直接关联您 primary interest 中的 statistical computing（分布式算法设计），序贯整合思路可迁移至联邦 debiased ML 或联邦因果推断场景；COVID-19 多医院数据集对您 secondary interest 流行病学应用有数据参考价值。

### 13. [10.5705/ss.202025.0283](https://doi.org/10.5705/ss.202025.0283) — A Primal Dual Active Set with Continuation Algorithm for ℓ0-penalized High-dimensional Accelerated Failure Time Model
- **作者**: Peili Li, Ruoying Hu, Yanyun Ding, Yunhai Xiao
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维右删失生存数据下，本文研究基于加权最小二乘与 ℓ₀ 惩罚的加速失效时间（AFT）模型的变量选择与估计问题。算法层面，采用原始-对偶活跃集（PDAS）算法并结合连续化策略（continuation）选择正则化参数；理论层面，利用协变量矩阵的互不相干性（MIC）与受限等距性（RIP）对迭代过程中活跃集的估计误差进行分析。证明了活跃集在迭代中具有单调性，且算法能在有限步内收敛至 oracle 解。模拟与乳腺癌真实数据验证了方法相较于现有方法的优势。对您有用：该文将 PDAS 算法拓展至高维删失数据，其数值优化方法与有限步收敛证明对您在统计计算（数值算法）与高维统计方向的研究有直接参考价值，同时乳腺癌真实数据的应用也契合流行病学方向。
- **关键技术**: `ℓ₀-penalized regression`, `accelerated failure time model`, `primal dual active set algorithm`, `mutual incoherence property`, `restricted isometry property`, `continuation strategy`
- **为什么对您有用**: 直接契合您在统计计算（数值算法设计）与高维统计的兴趣，PDAS 算法的有限步收敛证明及连续化策略对开发高效高维优化算法有迁移价值；同时 AFT 模型与乳腺癌数据集对流行病学应用方向有参考意义。

### 14. [10.5705/ss.202025.0060](https://doi.org/10.5705/ss.202025.0060) — Distributed Focused Information Criterion and Focused Frequentist Model Averaging for Massive Data
- **作者**: Yifan Zhang, Xiaolin Chen, Yuzhan Xing
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在局部渐近框架下研究线性回归模型的大规模分布式数据下的聚焦信息准则（FIC）与聚焦频率模型平均估计。针对每个候选模型的回归系数向量，提出三种分治策略（一次性合并与两种迭代方法）进行估计，并建立相应估计量的极限分布与均方误差上界。基于这些分布式估计量，进一步发展了分布式 FIC 与分布式聚焦频率模型平均估计，严格推导了在固定权重与数据驱动权重下目标参数的渐近分布及模型平均估计的 MSE 上界。理论结果表明分布式方法在保持与全局方法相同的渐近风险阶的同时显著降低通信与计算开销。对您而言，本文的分布式算法设计与局部渐近下的风险界分析直接关联统计计算与效率理论两个 primary interest，且 FIC 的聚焦最优权重思想可迁移至半参数效率框架下的参数导向推断。
- **关键技术**: `focused information criterion`, `frequentist model averaging`, `divide-and-conquer estimation`, `local asymptotic framework`, `data-driven weight selection`, `MSE upper bound`
- **为什么对您有用**: 直接关联您 primary interest 中的统计计算（分布式分治算法设计）与效率理论（聚焦参数的最优模型平均权重与风险界），FIC 的 focus parameter 思想可迁移至半参数效率框架下的目标参数推断。

### 15. [10.5705/ss.202024.0213](https://doi.org/10.5705/ss.202024.0213) — Inference for Delay Differential Equations Using Manifold-Constrained Gaussian Processes
- **作者**: Yuxuan Zhao, Samuel W.K. Wong
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究从稀疏带噪数据中推断延迟微分方程（DDE）未知参数（含时滞参数）的问题，设定为带流形约束的贝叶斯框架。方法扩展了流形约束高斯过程（MGP），对系统轨迹施加GP先验并约束其满足DDE流形条件。针对时滞参数导致现有绕过数值求解器的方法失效的挑战，开发了线性插值方案以近似时滞系统输出，并给出了近似导数的理论误差界。仿真（Hutchinson方程、lac操纵子）与安大略省COVID-19数据验证了方法有效性。该文将GP非参数先验与数值近似计算结合，为处理带时滞的动态系统提供了计算方案与理论误差界分析，对您的统计计算与流行病学应用兴趣有参考价值。
- **关键技术**: `manifold-constrained Gaussian processes`, `delay differential equations`, `Bayesian parameter inference`, `linear interpolation scheme`, `theoretical error bounds`
- **为什么对您有用**: 结合了统计计算（线性插值近似与误差界）和非参数方法（GP先验），并在流行病学（COVID-19）数据上应用，对您在动态系统/流行病学模型的数值计算与非参数推断有参考价值。

### 16. [10.5705/ss.202024.0195](https://doi.org/10.5705/ss.202024.0195) — Maximizing Area Under the Receiver Operating Characteristic Curve for Biomarker Combination
- **作者**: Yuxuan Chen, Yijian Huang
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多生物标志物线性组合的诊断精度优化问题中，目标是最大化 AUC 关于组合系数的估计；核心困难在于 AUC 对线性组合具有尺度不变性（多数现有方法固定一个系数回避此问题），且经验 AUC 为分段常数函数导致标准梯度算法不可用，现有核平滑方法则对带宽选择敏感。本文提出直接最大化经验 AUC 的新方法，绕过核平滑，同时提供计算高效的点估计与方差估计算法。AUC 本质上是 Mann-Whitney U-统计量，其组合系数的方差估计涉及 influence function 推导与渐近正态性论证。模拟表明该方法在计算效率与统计性能上均表现良好，并以临床数据作示例。对您有用：该工作在统计计算（非光滑目标函数的优化算法）和半参数效率（U-统计量框架下方差估计与 influence function）两个子方向上提供了可迁移的思路。
- **关键技术**: `empirical AUC maximization`, `Mann-Whitney U-statistic`, `influence function`, `scale-invariant optimization`, `piecewise-constant objective`, `variance estimation for rank-based estimators`
- **为什么对您有用**: 直接连接您 primary interest 中的统计计算（非光滑目标函数的数值优化）与 higher-order U-statistics / efficiency theory（AUC 作为 U-统计量的 influence function 与方差估计），方法可迁移至其他 rank-based 或分段常数目标函数的优化场景。

### 17. [10.5705/ss.202024.0092](https://doi.org/10.5705/ss.202024.0092) — The Method of Limits and Its Application to The Analysis of Count Data in Genome-wide Association Studies
- **作者**: Jiming Jiang, Leqi Xu, Yiliang Zhang, Hongyu Zhao
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在 GWAS 计数数据设定下，目标是估计遗传力与因果 SNP 比例，现有似然方法（如 PQLseq）面临严重计算瓶颈。本文提出极限法（MoL），将其视为矩估计的推广，通过构造样本矩的极限方程绕过计算困难。作者在正则条件下严格证明了 MoL 估计量的相合性与渐近正态性，并导出了因果 SNP 比例的相合估计。模拟与 UK Biobank 实证表明，MoL 在计算效率与平均统计效率（ASE）上均优于 PQLseq。对您而言，MoL 的渐近理论推导及计算-统计效率权衡策略，对统计计算与高维推断方向的研究具有直接的方法论参考价值。
- **关键技术**: `method of limits`, `asymptotic normality`, `method of moments extension`, `heritability estimation`, `computational-statistical efficiency tradeoff`
- **为什么对您有用**: MoL 作为矩估计的推广，其渐近正态性的建立与计算-统计效率权衡，对您在统计计算与高维推断方面的研究有方法论启发。

## 经济理论 / 应用  *(econ_theory, 1 篇)*

### 1. [10.5705/ss.202025.0450](https://doi.org/10.5705/ss.202025.0450) — Bubble Modeling and Tagging: a Stochastic Nonlinear Autoregression Approach
- **作者**: Xuanling Yang, Dong Li, Ting Zhang
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文针对经济金融时间序列中的局部爆炸性（bubble）行为，提出随机非线性自回归模型（stochastic NAR），该模型在全局严格平稳且几何遍历的条件下，当非线性自回归系数超出特定范围时能产生周期性爆炸行为以刻画泡沫动态。核心估计方法为拟极大似然估计（QMLE），在关于创新的最小假设下建立了强一致性与渐近正态性；同时提出了模型拟合充分性的诊断检验统计量。泡沫标记方面，分别从残差视角和零状态视角给出两种 tagging 方法，并通过 Monte Carlo 评估有限样本表现。实证部分将模型应用于恒生指数月度数据，展示泡沫检测效果。对您而言，该文的 QMLE 渐近理论与诊断检验构造可参考其数学统计处理方式，而泡沫动态建模框架对经济理论中金融时间序列的应用分析有直接借鉴价值。
- **关键技术**: `quasi-maximum likelihood estimation`, `stochastic nonlinear autoregression`, `geometric ergodicity`, `diagnostic checking statistic`, `bubble tagging via residuals and null-state`
- **为什么对您有用**: 连接您 secondary interest 中的经济理论（金融时间序列模型与数据集），QMLE 渐近理论与诊断检验统计量的构造也触及您 primary interest 中的 mathematical statistics / hypothesis testing 子方向。

## 其他  *(other, 12 篇)*

### 1. [10.5705/ss.202025.0295](https://doi.org/10.5705/ss.202025.0295) — Inference on Two-Sample Covariance Difference for Large-Scale Functional Data
- **作者**: Kaijie Xue, Lan Xue, Riquan Zhang
- **期刊/来源**: Statistica Sinica
- 相关性 7/10
- **摘要**: {
  "topic": "hypothesis_testing",
  "summary_zh": "本文研究大尺度函数型数据下两样本协方差差异的推断问题，目标是在无协方差/相关结构约束的宽松条件下对协方差差构建置信域。核心方法采用计算高效的乘子Bootstrap（multiplier bootstrap），避开了传统方法仅能做检验的局限。该程序具有"特征值衰减无关"（eigenvalue-decay-free）和"平方可积无关"（square-integrable-free）特性，免除了对谱衰减速率的严格依赖。由此不仅导出比现有方法更具功效的检验，还获得了在广泛备择假设下相合的估计功效函数。理论上证明了置信域的覆盖性质与功效函数的相合性，模拟与实证支持了方法的有效性。对您有用：该文在假设检验与高维统计的交叉处，通过放松特征值衰减与平方可积假设为高维协方差推断提供了更稳健的框架，乘子Bootstrap计算方案也契合您对统计计算的兴趣。",
  "key_techniques": [
    "multiplier bootstrap",
    "covariance difference testing",
    "large-scale functional data",
    "eigenvalue-decay-free",
    "consistent power

### 2. [10.5705/ss.202025.0466](https://doi.org/10.5705/ss.202025.0466) — Out-of-cluster Prediction for Model Selection in Regression with Unsupervised Clustering
- **作者**: Masao Ueki
- **期刊/来源**: Statistica Sinica
- 相关性 2/10
- **摘要**: {
  "topic": "hypothesis_testing",
  "summary_zh": "在无监督聚类回归（先对解释变量聚类，再在各簇内分别建回归模型）设定下，目标是选择聚类数 K 及排除冗余模型，假设不同簇间回归系数不同。核心提出一种"跨簇预测"（out-of-cluster prediction）模型排除程序：利用跨簇预测精度低于簇内预测这一特征，在 AIC 等准则筛选前先排除冗余模型。对 Cox 回归，提出归一化偏似然（normalized partial log-likelihood）以避免标准偏似然在模型选择时的发散问题。理论上证明 AIC 结合该排除程序可实现模型选择一致性；模拟覆盖 Gaussian 线性、logistic 和 Cox 回归 + K-means 聚类。对您而言，模型选择一致性的证明思路及 Cox 归一化偏似然的技术处理可参考，但与核心 primary interest（causal inference / efficiency / RMT）的直接关联较弱。",
  "key_techniques": [
    "out-of-cluster prediction",
    "model exclusion procedure",
    "model selection consistency",
    "normalized pa

### 3. [10.5705/ss.202025.0049](https://doi.org/10.5705/ss.202025.0049) — Mirror-Symmetric Orthogonal Latin Hypercubes with Attractive Space-Filling Properties
- **作者**: Chunyan Wang, Min-Qian Liu
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究计算机实验中的镜像对称正交拉丁超方体（Mirror-Symmetric Orthogonal Latin Hypercubes）的构造问题，目标是同时实现一维最大分层、正交性以及高阶正交性。作者利用基于 Reed-Solomon 码的正交阵列提出了一种新的构造方法，理论证明了所得设计具备优良的正交性和低维空间填充性质，且部分设计在 maximin distance 准则下达到最优。镜像对称结构有助于主效应与交互效应的识别，而 Reed-Solomon 码的代数结构保证了构造的系统性。模拟比较进一步验证了新设计相对于现有设计的优越性。本文属于试验设计领域，与您核心的因果推断或高维理论距离较远，但其中基于代数编码的矩阵构造算法对统计计算（数值方法与算法）子方向有微弱的参考价值。
- **关键技术**: `Orthogonal Latin hypercubes`, `Mirror-symmetric designs`, `Reed-Solomon codes`, `Orthogonal arrays`, `Maximin distance criterion`
- **为什么对您有用**: 本文属于试验设计，与您的主要研究方向（因果、高维、半参数）无直接重叠；仅其代数构造算法与统计计算（数值方法）有微弱关联，阅读收益较低。

### 4. [10.5705/ss.202024.0029](https://doi.org/10.5705/ss.202024.0029) — Grouped Orthogonal Arrays And Their Construction Methods
- **作者**: Guanzhou Chen, Yuanzhen He, Devon Lin, Fasheng Sun
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在计算机实验设计设定下，针对变量组间无交互（即底层函数为分组可加）的先验知识，研究如何构造比传统空间填充设计更合适的实验设计。提出了“分组正交阵列”（grouped orthogonal arrays）的概念，并在素数幂水平下给出了多种构造方法。相比于现有技术，该方法能生成更多运行次数灵活的设计，且具有更好的组内投影性质。文中提供了大量可供实际使用的构造设计表。该工作属于实验设计（DoE）领域，与您关注的半参数可加模型在“分组可加结构”假设上有概念重叠，但对因果推断或效率理论的直接参考价值有限。
- **关键技术**: `grouped orthogonal arrays`, `space-filling designs`, `additive model structure`, `combinatorial construction`, `projection properties`
- **为什么对您有用**: 论文属于实验设计（DoE）领域，与您关注的高维推断、半参数效率或因果推断关联较弱；仅在“分组可加结构”与半参数可加模型的假设层面有微弱概念重叠，对您核心研究的直接收益有限。

### 5. [10.5705/ss.202025.0075](https://doi.org/10.5705/ss.202025.0075) — D-Optimal Designs for Ordinal Response Experiments
- **作者**: Huiping Dang, Jun Yu, Fasheng Sun
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究有序响应实验中 adjacent-category 模型在一般 link function 下的 D-optimal design 问题，涵盖定量与定性因子。理论上推导了局部 D-optimal design 的结构性质，包括支撑点数目与一个简单完全类（simple complete class）。基于所得结构性质，提出高效搜索算法计算对应 D-optimal design，并进一步讨论了整数分配的实用实现。数值例子表明所提设计在统计效率与计算时间上均有优势。对您而言，该文的完全类刻画与算法设计思路可作 optimal design 领域的参考，但与您核心关注（semiparametric efficiency / 高维推断 / 因果识别）的直接关联较弱。
- **关键技术**: `D-optimal design`, `adjacent-category logit model`, `complete class theorem`, `Fisher information matrix`, `integer-valued allocation`, `general link function`
- **为什么对您有用**: 属于数理统计与计算统计的交叉，完全类定理的证明与搜索算法对 experimental design 有方法论价值，但与您 primary interests 中的 semiparametric efficiency bounds / 高维推断 / 因果推断距离较远，收益有限。

### 6. [10.5705/ss.202025.0225](https://doi.org/10.5705/ss.202025.0225) — Integrating External Summary Information via James-Stein Shrinkage
- **作者**: Peisong Han, Haoyue Li, Jeremy M. G. Taylor
- **期刊/来源**: Statistica Sinica
- 相关性 0/10
- **摘要**: {
  "topic": "efficiency_dml",
  "summary_zh": "在一般参数回归（如 GLM）设定下，目标是将外部研究的参数估计（summary statistics）整合到内部个体数据拟合中，以改进参数估计的渐近风险。作者采用 bias-variance trade-off 路线，构造 James-Stein shrinkage estimator，将内部 MLE 向外部估计收缩；关键性质是无论内外总体异质性程度如何，shrinkage estimator 的渐近风险均不超过内部 MLE，即提供 guaranteed risk improvement。这一"安全通行"性质在现有方法中罕见——多数方法在异质性较大时会产生过度偏差。模拟与前列腺癌数据应用验证了数值表现。对您有用：该工作为外部信息整合提供了 shrinkage 视角，与效率理论中 bias-variance trade-off 及 semiparametric efficiency 的思路相通，可迁移至因果推断中借调外部 RCT/观察研究 summary 的场景。",
  "key_techniques": [
    "James-Stein shrinkage",
    "asymptotic risk dominance",
    "bias-variance trade-off

### 7. [10.5705/ss.202024.0379](https://doi.org/10.5705/ss.202024.0379) — Sliced Orthogonal Designs for Computer Experiments
- **作者**: Omar A. Alhelali, S.D. Georgiou, S. Stylianou
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在计算机实验（computer experiments）框架下，提出 sliced orthogonal designs 的概念，是 sliced Latin hypercube designs 的推广，目标是为含分片结构（如多因子水平/多批次）的实验同时保证整体及各 slice 对一阶与二阶模型均具正交性。构造方法利用零自相关序列（T-sequences、Golay sequences）及 disjoint amicable sequences，首次给出此类设计的无穷族。所生成设计按文献中多种准则（如 orthogonality criterion、space-filling 性质）进行评估，结果以表格供实践者参考。该方法学 novelty 限于实验设计构造，不涉及估计/推断理论。
- **关键技术**: `sliced orthogonal design`, `zero autocorrelation sequences (T-sequences, Golay sequences)`, `disjoint amicable sequences`, `Latin hypercube design`, `orthogonal array construction`
- **为什么对您有用**: 与您的主要兴趣（因果推断、高维/半参数理论、效率理论）直接关联较弱；仅通过正交设计与矩阵构造间接触及 statistical computing 中的矩阵/序列工具，收益有限。

### 8. [10.5705/ss.202025.0139](https://doi.org/10.5705/ss.202025.0139) — Testing Conditional Tail Independence
- **作者**: Zhaowen Wang, Huixia Judy Wang, Deyuan Li
- **期刊/来源**: Statistica Sinica
- 相关性 0/10
- **摘要**: {
  "topic": "hypothesis_testing",
  "summary_zh": "本文在极值理论框架下，针对存在协变量的情形，提出了条件尾部相依指数（conditional tail dependence index），目标是检验给定协变量下的条件尾部独立性原假设。作者构造了名为条件尾部商相关系数（CTQCC）的检验统计量，并严格推导了其在原假设下的渐近分布。该方法无需对边缘分布或相依结构施加强参数假设，属于非参数假设检验范畴。模拟研究与降水/风速的实证分析表明 CTQCC 能有效识别条件尾部相依结构。对您有用：该文将尾部独立性检验推广到条件版本，其检验统计量构造与渐近分布推导思路对您在数学统计（假设检验）及非参数理论方向的研究有直接参考价值。",
  "key_techniques": [
    "conditional tail dependence index",
    "quotient correlation coefficient",
    "asymptotic distribution",
    "extreme value theory",
    "nonparametric hypothesis testing"
  ],
  "why_relevant": "直接契合您在"数学统计（假设检验）"和"非参数理论"方面的兴趣；检验条

### 9. [10.5705/ss.202025.0196](https://doi.org/10.5705/ss.202025.0196) — Exploratory Hierarchical Factor Analysis with an Application to Psychological Measurement
- **作者**: Jiawei Qiao, Yunxiao Chen, Zhiliang Ying
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在层级因子模型（bifactor 为特例）设定下，目标是探索性地从数据中学习因子载荷矩阵的层级零约束结构，克服传统 Schmid-Leiman 变换易失效的缺陷。本文首先建立了一般层级因子模型的可识别性理论，证明在温和正则条件下层级结构是可学习的。其次，提出一种计算高效的分治算法来估计该层级结构。最后，渐近理论证明所提方法能一致地恢复真实的层级因子结构。仿真与人格测试数据验证了方法有效性。对您而言，其可识别性证明与分治计算策略对处理高维潜变量模型的结构学习有参考价值，尽管应用领域与您的主方向有一定距离。
- **关键技术**: `hierarchical factor model`, `identifiability theory`, `divide-and-conquer algorithm`, `consistent structure recovery`, `Schmid-Leiman transformation`
- **为什么对您有用**: 涉及潜变量模型的可识别性理论与分治计算策略，与您在统计计算（数值方法与算法）和数学统计方面的兴趣有轻微交叉，但其心理测量背景与您的主方向较远，主要收益在于借鉴其结构学习算法思路。

### 10. [10.5705/ss.202025.0285](https://doi.org/10.5705/ss.202025.0285) — Bi-optimal Quantile-based Test Planning for Accelerated Degradation Test Based on Wiener Process
- **作者**: Ya-Shan Cheng, Chien-Yu Peng
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在 Wiener 过程框架下，本文研究加速退化试验的最优设计，目标是在资源受限下确定样本量、终止时间和测量次数，以最小化 q-分位数估计的近似方差。传统 V_{t_q}-最优设计仅针对单一准则，本文提出双最优分位数设计，通过选择合适的 q 使得该设计在两个最优性准则下同时达到 100% 效率。核心贡献是推导了该双最优设计存在性与唯一性的充要条件，并据此确定加速退化试验的最优配置。数值算例验证了方法的实用性。该文属于可靠性工程中的最优实验设计，与您关注的半参数效率界距离较远，但充要条件的严格推导对数学统计有一定参考价值。
- **关键技术**: `Wiener process`, `optimal experimental design`, `quantile estimation`, `bi-optimal test plan`, `variance minimization`
- **为什么对您有用**: 属于可靠性数学统计的最优实验设计，虽涉及效率概念但非您关注的半参数效率界；充要条件的理论推导属于数学统计范畴，但与您核心兴趣（因果/高维/半参数）重叠度低。

### 11. [10.5705/ss.202025.0350](https://doi.org/10.5705/ss.202025.0350) — Models for Order-of-Addition Screening Experiments
- **作者**: Jing-Wen Huang, Hongquan Xu
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究序贯添加筛选实验(order-of-addition screening)的建模与设计问题，设定为在资源受限下仅能施加部分组件，需同时选择组件及其最优添加顺序。作者提出了一系列针对此类实验的参数模型，并研究了其理论性质。核心贡献在于推导了相应的最优设计(optimal designs)理论结果，旨在优化参数估计的方差性质。实证部分将所提模型应用于带拒绝惩罚的作业调度问题。对您而言，虽然序贯添加的形式与因果推断中的纵向/序列干预设定有概念上的相似，但本文核心是最优实验设计而非观察性因果识别或半参数效率，方法直接迁移价值有限。
- **关键技术**: `order-of-addition experiments`, `screening designs`, `optimal design theory`, `D-optimal criterion`
- **为什么对您有用**: 本文属于实验设计(DOE)领域，与您关注的观察性因果推断、高维统计或半参数效率重叠较少；仅序贯添加的形式与纵向因果推断的序列干预设定有微弱概念联系，但技术路线差异较大。

### 12. [10.5705/ss.202023.0401](https://doi.org/10.5705/ss.202023.0401) — Two-level Isomorphic Foldovers Designs
- **作者**: Chunyan Wang, Dennis K. J. Lin
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究二水平非正交阵列的构造问题，提出一类新的非正则设计——同构折叠设计（Isomorphic Foldovers Design, IFD），由初始设计的若干折叠组合而成。核心方法是对任意初始设计枚举所有不等价 f-IFD，并以 G-aberration 或 G2-aberration 为准则给出两个算法筛选最优设计。IFD 具有 parallel flats 结构，比一般非正则设计更易理解和分析；且基于非正则初始设计构造优良 IFD 的成功率高于直接在单一 flat 上搜索。文中还证明若干已有设计是 IFD 的特例。该文属于实验设计（DOE）的组合构造方向，与您关注的因果推断、半参数效率或高维推断理论几乎没有交集，仅在 RCT 设计层面有极远端联系。
- **关键技术**: `foldover construction`, `G-aberration criterion`, `G2-aberration criterion`, `parallel flats structure`, `nonregular fractional factorial design`
- **为什么对您有用**: 与您的主要兴趣方向（因果推断、半参数效率、高维RMT等）基本无直接关联；仅在'实验设计作为因果推断的基石'这一极宽泛意义下有微弱联系，阅读收益很低。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

