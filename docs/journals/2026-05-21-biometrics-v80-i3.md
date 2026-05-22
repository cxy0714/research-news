# Biometrics — Vol 80  Issue 3  ·  2026-05-21

- 共 39 篇 · Biometrics

## 因果推断  *(causal_inference, 10 篇)*

### 1. [10.1093/biomtc/ujae065](https://doi.org/10.1093/biomtc/ujae065) — Multiply robust estimation of marginal structural models in observational studies subject to covariate-driven observations
- **作者**: Janie Coulombe, Shu Yang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 10/10 · novelty: `new_method`
- **摘要**: 在纵向观察性数据（如电子病历）中，因果效应估计面临混杂和不规则、协变量驱动的观测时间双重挑战，目标是估计边际结构模型（MSM）的因果参数。现有双重加权估计量依赖处理与观测时间两个干扰模型的联合正确设定，本文提出一种新的多重稳健估计量。该方法基于影响函数构造，允许处理机制与观测机制的多组工作模型中至少一组正确即可保证一致性。相比仅有的双重加权替代方案，新估计量在放松模型设定假设的同时具有更优的渐近效率。模拟与 Add Health 数据的实证分析验证了其有限样本表现。对您有用：该文将多重稳健性引入带不规则观测时间的纵向因果推断，其基于影响函数的构造思路可直接迁移至您关注的 longitudinal causal inference 与 semiparametric efficiency 领域。
- **关键技术**: `multiply robust estimation`, `marginal structural models`, `covariate-driven observation times`, `inverse probability weighting`, `influence function`
- **为什么对您有用**: 直接推进了您关注的 longitudinal causal inference 与 efficiency theory：在带不规则观测时间的 MSM 框架下实现了多重稳健与效率提升，其影响函数构造思路对处理纵向缺失/不规则观测的半参数推断具有直接借鉴价值。

### 2. [10.1093/biomtc/ujae067](https://doi.org/10.1093/biomtc/ujae067) — Joint structure learning and causal effect estimation for categorical graphical models
- **作者**: Federico Castelletti, Guido Consonni, Marco L Della Vedova
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在多类别变量的因果推断设定下，目标是在对某一变量进行外部干预后估计其对结局变量的因果效应，假设变量间依赖结构可用 DAG 表示但 DAG 本身未知。作者提出贝叶斯联合推断框架，通过 MCMC 算法同时学习 DAG 结构与模型参数，目标是 DAG 和参数的联合后验分布。核心技术为 reversible-jjump MCMC 提案方案，在 DAG 空间与参数空间之间联合跳转，从而将结构不确定性显式纳入因果效应的估计与推断。模拟研究表明该方法在估计精度上优于现有 state-of-the-art；实证分析应用于大学生抑郁与焦虑数据集。对您而言，该文提供了类别变量下联合结构学习与因果效应估计的贝叶斯视角，与您关注的因果 identification/estimation 方向相关，但方法路线（贝叶斯 MCMC vs 半参数效率/IF）差异较大；流行病学应用数据集对 secondary interest 有参考价值。
- **关键技术**: `reversible-jump MCMC`, `DAG structure learning`, `joint posterior over DAGs and parameters`, `categorical graphical models`, `causal effect under structure uncertainty`
- **为什么对您有用**: 与您 primary interest 中的因果推断 identification/estimation 相关，展示了在 DAG 结构未知时如何联合建模的结构学习路线；但方法范式（贝叶斯 MCMC）与您关注的半参数效率理论和 debiased ML 差异较大，主要收益在于了解类别变量因果推断的结构不确定性处理思路及流行病学实证数据集。

### 3. [10.1093/biomtc/ujae073](https://doi.org/10.1093/biomtc/ujae073) — A generalized outcome-adaptive sequential multiple assignment randomized trial design
- **作者**: Xue Yang, Yu Cheng, Peter F Thall, Abdus S Wahed
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在纵向动态治疗策略（DTR）与序贯多重分配随机试验（SMART）框架下，目标是识别最优多阶段治疗策略，同时解决传统 SMART 无法利用历史数据减少劣效治疗暴露的问题。本文提出广义结局自适应（GO-SMART）设计，根据既往患者的结局自适应地调整各阶段随机化概率，向更优治疗倾斜。为纠正结局自适应随机化引入的选择偏倚，提出了 DTR 效应的 G-估计量和逆概率加权（IPW）估计量，并解析证明了其一致性。模拟表明，相较于传统 SMART 及其他自适应 SMART，GO-SMART 能让更多患者接受最优 DTR 并获得更多总响应，同时保持相当或更优的统计功效。该文将 IPW 与 G-estimation 推广至带有复杂自适应随机化机制的纵向因果设定，对您研究纵向因果推断的估计方法具有应用层面的参考价值。
- **关键技术**: `dynamic treatment regimes`, `sequential multiple assignment randomized trial`, `outcome-adaptive randomization`, `G-estimation`, `inverse probability weighting`
- **为什么对您有用**: 涉及您 primary interest 中的纵向因果推断（DTR），其处理自适应随机化偏倚的 IPW 与 G-estimation 策略对研究复杂纵向干预下的因果估计有参考价值。

### 4. [10.1093/biomtc/ujae099](https://doi.org/10.1093/biomtc/ujae099) — A Bayesian nonparametric approach for causal mediation with a post-treatment confounder
- **作者**: Woojung Bae, Michael J Daniels, Michael G Perri
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在存在治疗后混杂因素的因果中介分析设定下，目标是识别和估计自然直接效应（NDE）与自然间接效应（NIE），识别依赖于扩展的序贯可忽略性假设与高斯 copula 模型。方法上，采用 enriched Dirichlet process mixture (EDPM) 对观测数据的联合分布进行贝叶斯非参数建模，从而避免参数模型误设。通过数据增广机制处理可忽略缺失数据，并在贝叶斯框架下直接抽样获取 NDE/NIE 的后验分布。模拟研究显示该方法在有限样本下表现良好，在 Rural LITE 试验的流行病学应用中发现缺乏中介效应的强证据。对您有用：该文处理了中介分析中经典的 post-treatment confounder 问题，其基于高斯 copula 的识别策略与贝叶斯非参数联合建模思路，可与您关注的半参数效率理论及频率学派中介分析方法形成对比与补充。
- **关键技术**: `causal mediation analysis`, `post-treatment confounder`, `Enriched Dirichlet Process Mixture (EDPM)`, `Gaussian copula`, `extended sequential ignorability`, `Bayesian nonparametrics`
- **为什么对您有用**: 直接涉及您 primary interest 中的因果中介分析，特别是处理 post-treatment confounder 这一棘手设定；同时提供了流行病学临床试验的真实数据集，契合您 secondary interest 中的 epi 应用与因果分析。

### 5. [10.1093/biomtc/ujae100](https://doi.org/10.1093/biomtc/ujae100) — Causal inference using multivariate generalized linear mixed-effects models
- **作者**: Yizhen Xu, Ji Soo Kim, Laura K Hummers, Ami A Shah, Scott L Zeger
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在纵向观察性研究的动态治疗策略（DTR）下，目标是估计亚组特异性的干预获益，面临未测量时不变混杂的挑战。提出多元广义线性混合效应模型（MGLMM），将未测量时不变因素作为随机效应，构建结局、时变混杂和处理分配的联合分布。基于此联合分布，采用贝叶斯 g-computation 算法计算动态处理效应的后验分布。识别条件依赖于处理分配异质性的序贯可忽略性假设，即通过平衡由未测量因素引起的潜在处理偏好来实现因果识别。模拟研究验证了方法的有效性，并在硬皮病临床观察数据中评估了霉酚酸酯的持续使用疗效。对您有用：该文将随机效应引入纵向因果推断的 g-computation 以处理未测量混杂，其条件序贯可忽略性假设的识别策略对您在 longitudinal causal inference 和流行病学应用中的建模有直接参考价值。
- **关键技术**: `Bayesian g-computation`, `multivariate GLMM`, `dynamic treatment regimes`, `sequential ignorability`, `subject-specific random effects`, `unmeasured time-invariant confounding`
- **为什么对您有用**: 将随机效应与贝叶斯 g-computation 结合处理纵向未测量混杂，其条件序贯可忽略性假设的识别思路对您在 longitudinal causal inference 和流行病学应用中的建模有直接参考价值。

### 6. [10.1093/biomtc/ujae070](https://doi.org/10.1093/biomtc/ujae070) — Causal meta-analysis by integrating multiple observational studies with multivariate outcomes
- **作者**: Subharup Guha, Yi Li
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在多回顾性队列的因果元分析设定下，目标是对大总体中多组潜在结果进行无混杂比较，但便利样本通常缺乏代表性且协变量不平衡。本文提出基于伪总体的协变量平衡框架，将传统加权方法扩展至多组多队列情形，并引入 FLEXOR 加权法通过最大化有效样本量构建伪总体。针对定量、分类及多变量结果的组间比较，构造了无混杂推断的加权估计量，并推导了其渐近性质。仿真与 TCGA 数据应用验证了 FLEXOR 方法的稳健性与通用性。对您有用：该文将因果推断中的协变量平衡与加权估计推广至多研究元分析框架，其渐近理论推导和针对多变量结果的估计策略对您在因果推断估计与效率理论方面的研究有直接参考价值。
- **关键技术**: `covariate balancing weighting`, `pseudo-population`, `meta-analysis of observational studies`, `FLEXOR weighting`, `asymptotic properties of weighted estimators`, `multivariate potential outcomes`
- **为什么对您有用**: 直接关联您 primary interest 中的因果推断估计与效率理论，其多队列元分析下的协变量平衡加权框架及渐近性质推导，可为多源数据因果推断提供新方法参考。

### 7. [10.1093/biomtc/ujae061](https://doi.org/10.1093/biomtc/ujae061) — Optimal refinement of strata to balance covariates
- **作者**: Katherine Brumberg, Dylan S Small, Paul R Rosenbaum
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在观察性研究的分层设计中，本文研究如何将一个层（stratum）最优拆分为两个子层以最大程度降低多协变量的层内不平衡，estimand 为层内协变量不平衡度。将此问题建模为整数规划（IP），通过对线性规划松弛解的随机舍入（randomized rounding）近似求解：LP 可将个体分数分配至子层，随机舍入以偏置硬币将完整个体依概率分配。当层内样本量远大于协变量维度时，证明：(i) 随机舍入几乎不做额外随机化，与 LP 松弛解高度一致；(ii) LP 松弛与随机舍入分别给出不可达 IP 最优解的下界与上界，且二者通常紧近。实证用 5735 名患者数据对比 propensity score matched pairs（仅保留 2016 人）与 5→10 精细分层，后者保留全部患者且协变量平衡更优。对您而言，该文将组合优化（IP/LP 松弛/随机舍入）引入因果推断设计阶段的思路，与您在统计计算和因果推断交叉方向的兴趣直接相关。
- **关键技术**: `integer programming`, `linear programming relaxation`, `randomized rounding`, `propensity score stratification`, `covariate balance`
- **为什么对您有用**: 将整数规划与随机舍近这一组合优化工具引入因果推断设计阶段，与您在统计计算（数值方法与算法）和因果推断的交叉兴趣直接相关；LP/IP 松弛的界分析思路也可为分层设计中的理论性质提供参考。

### 8. [10.1093/biomtc/ujae083](https://doi.org/10.1093/biomtc/ujae083) — LEAP: the latent exchangeability prior for borrowing information from historical data
- **作者**: Ethan M Alt, Xiuya Chang, Xun Jiang, Qing Liu, May Mo, Hong Amy Xia et al.
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在利用历史数据构建先验的贝叶斯临床试验设定下，目标是解决现有先验（power prior、commensurate prior、robust MAPP prior）对历史数据做整体折扣（blanket discounting）而无法区分可交换与不可交换子集的问题。本文提出 latent exchangeability prior（LEAP），通过潜变量将历史观测分为可交换与不可交换两组，仅对可交换子集借力，从而实现选择性折扣。与已有基于倾向得分的方法仅关注协变量分布不同，LEAP 同时利用结局参数评估可交换性。模拟与斑块状银屑病 III 期临床试验（非平衡随机化）案例展示了 LEAP 相较于整体折扣先验的优势。对您而言，LEAP 将可交换性的因果概念引入先验构建的思路，可迁移至 transportability / generalizability 中选择可交换目标人群的因果推断问题。
- **关键技术**: `latent exchangeability classification`, `power prior`, `commensurate prior`, `robust meta-analytic predictive prior`, `propensity score for exchangeability`, `Bayesian historical data borrowing`
- **为什么对您有用**: LEAP 将可交换性（因果推断核心概念）与先验折扣机制结合，对您在 proximal CI / transportability 中处理异质性人群的选择性借力有方法学启发；银屑病临床试验数据集也可作为流行病学应用案例参考。

### 9. [10.1093/biomtc/ujae069](https://doi.org/10.1093/biomtc/ujae069) — Propensity weighting plus adjustment in proportional hazards model is not doubly robust
- **作者**: Erin E Gabriel, Michael C Sachs, Ingeborg Waernbaum, Els Goetghebeur, Paul F Blanche, Stijn Vansteelandt et al.
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在因果效应 hazard ratio 估计中，实践中常将倾向得分加权（IPW）与比例风险模型（如 Cox）结合，期望获得双重稳健估计量。本文证明：当存在因果效应时，即使经过回归标准化，该组合一般并不双重稳健——无论 Cox 模型通过偏似然还是全似然拟合，也无论使用半参 Cox、Weibull 或灵活参数 PH 模型。作者给出新证明：仅在暴露无因果效应（null）且特定删失机制下，该组合才在倾向得分或结局模型之一正确时一致。基于此，提出两种在给定时间点生存差的双重稳健估计量（需正确建模删失机制），以及一种对整条生存曲线的双重稳健估计方法，并附 R 代码实现。对您有用：该结果直接修正了因果推断中生存分析双重稳健性的常见误解，且所提估计量涉及 influence function 与 censoring model 的交互，与您关注的 semiparametric efficiency 及流行病学应用中的因果生存分析紧密相关。
- **关键技术**: `propensity score weighting`, `Cox proportional hazards model`, `double robustness`, `regression standardization`, `partial likelihood`, `survival difference estimation`
- **为什么对您有用**: 直接修正因果推断中 PS+PH 模型双重稳健性的理论误解，涉及 semiparametric efficiency 与 influence function 的生存分析扩展，对您关注的因果推断理论及流行病学因果生存分析均有重要参考价值。

### 10. [10.1093/biomtc/ujae064](https://doi.org/10.1093/biomtc/ujae064) — Controlling false discovery rate for mediator selection in high-dimensional data
- **作者**: Ran Dai, Ruiyang Li, Seonjoo Lee, Ying Liu
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维数据（如神经影像、基因数据）的中介分析设定下，本文研究如何从高维候选集中筛选中介变量并控制错误发现率（FDR）。作者将中介变量选择问题转化为多重假设检验框架，并将基于 knockoff 的 FDR 控制变量选择方法扩展至中介选择，构建了相应的 knockoff mediator filter 算法。理论上证明了该方法在有限样本下即可实现 FDR 控制，无需依赖大样本渐近性质。模拟显示其在功效和有限样本表现上优于现有方法；实证分析 ABCD 研究数据，筛选出静息态功能磁共振成像连接性标记物作为不良童年事件与认知得分的中介。对您有用：该文将高维中介选择与 knockoff 假设检验结合，直接推进了您关注的因果推断（中介分析）与高维统计/假设检验的交叉方向，且 ABCD 数据分析对流行病学应用有参考价值。
- **关键技术**: `knockoff filter`, `false discovery rate control`, `high-dimensional mediation analysis`, `multiple hypothesis testing`, `finite sample FDR guarantee`
- **为什么对您有用**: 直接连接您的主兴趣“因果推断（中介分析）”与“高维统计/假设检验”，提供了高维中介变量筛选的有限样本 FDR 控制方法；同时 ABCD 研究的实证分析对您关注的流行病学应用（真实数据集与因果分析）具有直接借鉴价值。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 3 篇)*

### 1. [10.1093/biomtc/ujae076](https://doi.org/10.1093/biomtc/ujae076) — Reduced-rank clustered coefficient regression for addressing multicollinearity in heterogeneous coefficient estimation
- **作者**: Yan Zhong, Kejun He, Gefei Li
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在异质系数回归（CCR）设定下，针对多重共线性导致的估计与聚类不稳定问题，本文对系数矩阵引入低秩结构以实现降维与正则化。提出一个带自适应组融合惩罚（adaptive group fusion penalty）的非凸优化问题，专门适配该低秩结构。开发了保证收敛的迭代算法求解此非凸问题，并推导出系数估计误差的上界，展示了估计量的统计性质。模拟与 COVID-19 死亡率数据集的实证表明该方法优于现有 CCR 方法。对您有用：低秩系数矩阵的惩罚优化与误差界分析对高维统计中的多重共线性处理有借鉴意义，非凸迭代算法对统计计算方向有参考价值，COVID-19 数据集也可作为流行病学应用案例。
- **关键技术**: `reduced-rank regression`, `clustered coefficient regression`, `adaptive group fusion penalty`, `non-convex optimization`, `estimation error bound`
- **为什么对您有用**: 低秩结构与惩罚优化属于高维统计范畴，非凸优化算法设计属于统计计算方向，COVID-19实证属于流行病学应用；对您在高维多重共线性处理及非凸算法收敛性分析有直接参考价值。

### 2. [10.1093/biomtc/ujae096](https://doi.org/10.1093/biomtc/ujae096) — Heterogeneous latent transfer learning in Gaussian graphical models
- **作者**: Qiong Wu, Chi Wang, Yong Chen
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维 Gaussian 图模型 (GGM) 的迁移学习设定下，目标是估计目标域的精度矩阵，但现有方法常忽略样本内与样本间的潜在异质性（如未知亚群结构），易导致负迁移。本文提出 Latent-TL 算法，通过联合识别公共亚群结构与各亚群下的 GGM，实现“learn from the alike”。方法在目标域与源域同亚群样本间共享精度矩阵信息，采用交替优化同时完成聚类与惩罚图估计，从而在异质性存在时避免负迁移。理论上证明了 Latent-TL 相较于单站点学习及忽略异质性的标准迁移学习具有更优的估计误差界；实证应用于乳腺癌基因共表达网络。该文处理高维图模型迁移学习中的潜在异质性，其“同亚群迁移”的思想对您的高维统计结构学习及流行病学亚群因果推断有借鉴价值。
- **关键技术**: `Gaussian graphical models`, `transfer learning`, `latent heterogeneity`, `penalized likelihood`, `negative transfer avoidance`
- **为什么对您有用**: 直接涉及高维统计中的图模型估计与迁移学习，处理潜在异质性的思路对高维结构学习及流行病学/生物医学数据的亚群因果推断有方法学借鉴价值。

### 3. [10.1093/biomtc/ujae103](https://doi.org/10.1093/biomtc/ujae103) — Leveraging independence in high-dimensional mixed linear regression
- **作者**: Ning Wang, Kai Deng, Qing Mai, Xin Zhang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在高维混合线性回归（MLR）设定下，目标是估计回归系数并进行变量选择，关键假设为预测变量与潜类别指示变量相互独立。现有基于 EM 算法的稀疏惩罚方法多最大化条件似然且忽略预测变量的变异性；本文利用上述独立性结构，提出快速组惩罚 EM 估计器，实现了跨混合分量的协同变量选择与高效计算。理论上，本文建立了该估计器向真实参数收敛的非渐近收敛速率。实证方面，通过模拟和癌症细胞系百科全书（CCLE）数据集验证了方法的有效性。该文在高维 EM 算法下的非渐近理论分析与计算优化，对您在 high-dimensional statistics 和 statistical computing 方向的研究具有直接参考价值。
- **关键技术**: `high-dimensional mixed linear regression`, `group-penalized EM`, `non-asymptotic convergence rate`, `synergistic variable selection`, `latent indicator independence`
- **为什么对您有用**: 本文提出的高维 MLR 估计器及其非渐近收敛速率证明，直接契合您在 high-dimensional statistics（非渐近理论）和 statistical computing（EM 算法优化）方面的核心兴趣。

## 非参数 / 半参数  *(nonparam_semipara, 8 篇)*

### 1. [10.1093/biomtc/ujae080](https://doi.org/10.1093/biomtc/ujae080) — Nonparametric worst-case bounds for publication bias on the summary receiver operating characteristic curve
- **作者**: Yi Zhou, Ao Huang, Satoshi Hattori
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在诊断试验准确度 Meta 分析的 SROC 曲线估计中，针对选择性发表导致的发表偏倚（PB），现有敏感性分析方法均依赖参数化选择函数。本文提出一种非参数敏感性分析框架，在极小假设下利用非参数选择函数推导 SROC 曲线的最坏情况边界（worst-case bounds）。估计过程采用 Monte Carlo 方法近似 SROC 曲线及 AUC 的偏倚，并通过非线性规划优化给定边际选择概率范围下的 PB 极值。相较于传统参数化选择机制，该方法从根本上放松了对发表选择过程的参数化建模假设。实证分析展示了该边界在评估诊断试验 Meta 分析稳健性时的实用性。对您有用：该文将非参数边界思想引入敏感性分析，其 worst-case bounds 框架对您在因果推断中做无参数假设的敏感性分析（如放宽 Rosenbaum 模型）具有方法上的迁移价值。
- **关键技术**: `nonparametric selection function`, `worst-case bounds`, `Monte Carlo approximation`, `nonlinear programming`, `sensitivity analysis`
- **为什么对您有用**: 该文属于敏感性分析（您 primary interest）与非参数理论的交叉，其用非参数选择函数替代参数化假设推导 worst-case bounds 的思路，可迁移至因果推断中未观测混杂的敏感性分析；应用场景亦契合流行病学（secondary interest）。

### 2. [10.1093/biomtc/ujae071](https://doi.org/10.1093/biomtc/ujae071) — Nonparametric second-order estimation for spatiotemporal point patterns
- **作者**: Decai Liang, Jialing Liu, Ye Shen, Yongtao Guan
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在时空点过程框架下，针对现有方法要求二阶强度或对相关函数在时空上均平稳的局限，本文提出一种灵活的非参数方法来估计非平稳时间相关下的二阶特征。估计量采用核平滑技术，差异化地处理空间与时间相关性，并允许嵌入不同的一阶强度估计量以提升实用性。在空间递增域渐近框架下，作者建立了所提估计量的一致性。模拟实验表明，相比现有方法，该估计量显著提升了统计效率；COVID-19 数据应用进一步展示了其灵活性与可解释性。对您有用：该文在非参数核估计与渐近一致性方面的理论推导，以及流行病学时空数据的应用，与您的非参数理论和流行病学兴趣契合，可借鉴其非平稳设定下的渐近分析技巧。
- **关键技术**: `spatiotemporal point process`, `kernel smoothing`, `second-order intensity`, `pair correlation function`, `increasing-domain asymptotics`
- **为什么对您有用**: 涉及非参数理论（核平滑与渐近一致性）和流行病学（COVID-19）应用，与您的非参数理论及流行病学兴趣契合，可借鉴其时空非平稳假设下的渐近分析技巧与数据结构处理。

### 3. [10.1093/biomtc/ujae078](https://doi.org/10.1093/biomtc/ujae078) — Factor-augmented transformation models for interval-censored failure time data
- **作者**: Hongxi Li, Shuwei Li, Liuquan Sun, Xinyuan Song
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在区间删失失效时间数据设定下，针对多重共线性和高维协变量问题，提出因子增强半参数转换模型，目标是降维并估计协变量效应。联合建模框架包含因子分析模型（提取潜因子）与半参数转换模型（引入增强因子）。采用非参数极大似然估计（NPMLE），并开发计算稳定的 EM 算法进行求解。理论部分建立了潜因子与回归参数估计量的渐近性质（一致性、渐近正态性）。实证应用于 ADNI 阿尔茨海默病队列数据，并发布 R 包 ICTransCFA。对您有用：该文将因子分析融入半参数转换模型的理论推导与 EM 算法实现，对处理流行病学高维共线性数据及半参数渐近理论有直接参考价值。
- **关键技术**: `semiparametric transformation model`, `nonparametric maximum likelihood estimation (NPMLE)`, `factor-augmented model`, `EM algorithm`, `interval-censored data`
- **为什么对您有用**: 该文结合因子分析与半参数转换模型推导 NPMLE 渐近性质并提供 EM 算法，直接契合您在半参数理论与统计计算方面的兴趣；同时 ADNI 阿尔茨海默病数据集对流行病学应用有数据集价值。

### 4. [10.1093/biomtc/ujae090](https://doi.org/10.1093/biomtc/ujae090) — Integrating external summary information in the presence of prior probability shift: an application to assessing essential hypertension
- **作者**: Chixiang Chen, Peisong Han, Shuo Chen, Michelle Shardell, Jing Qin
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在数据整合设定下，目标是在两个队列间存在 prior probability shift（即分布差异依赖于结局变量）时，利用外部汇总统计量提升内部研究的估计效率。作者提出基于半参数约束优化的整合方法，引入 outcome-dependent selection function 刻画分布偏移，并在约束中纳入外部汇总信息；该方法无需外部方差-协方差的已知估计即可进行有效推断，从而处理了外部汇总信息本身的估计不确定性。理论上，所提估计量在 prior probability shift 下保持一致性并降低方差；模拟显示对二值与连续结局均具有更小偏差和方差。实证应用于原发性高血压风险因素分析，整合外部汇总信息后估计变异性显著降低。对您有用：该工作将半参数约束优化与分布偏移下的信息整合结合，直接关联您关注的 semiparametric theory 与 efficiency theory，且 prior probability shift 的处理思路可迁移至 causal inference 中的 transportability / external validity 问题。
- **关键技术**: `semi-parametric constrained optimization`, `outcome-dependent selection function`, `prior probability shift`, `summary-level data integration`, `variance estimation without external covariance`
- **为什么对您有用**: 半参数约束优化方法直接关联您 primary 的 semiparametric theory 与 efficiency theory；prior probability shift 的建模思路可迁移至 causal inference 中 transportability / external validity 设定；高血压流行病学应用提供真实数据集参考。

### 5. [10.1093/biomtc/ujae091](https://doi.org/10.1093/biomtc/ujae091) — Unit information Dirichlet process prior
- **作者**: Jiaqi Gu, Guosheng Yin
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在生存分析的非参数贝叶斯框架下，提出基于单位信息的 Dirichlet 过程先验（UIDP），用于刻画时间事件数据的潜在分布。通过推导累积风险函数微分形式的 Fisher 信息，UIDP 先验将其先验单位信息与历史数据集中单位信息的加权平均相匹配，从而自适应地融合参数与非参数历史信息。基于 MCMC 算法的模拟与实证表明，该方法能有效借用历史信息并提升统计效率。对您而言，该文将 Fisher 信息与 Dirichlet 过程结合的思路，可为非参数理论中先验构造与效率提升的交叉研究提供参考，尽管其贝叶斯视角与您关注的频率派半参数效率界有所不同。
- **关键技术**: `Dirichlet process prior`, `unit information prior`, `Fisher information of cumulative hazard`, `historical data borrowing`, `Markov chain Monte Carlo`
- **为什么对您有用**: 文章涉及非参数先验构造与 Fisher 信息的结合，与您关注的非参数理论及效率理论有一定交集；但其核心为贝叶斯框架而非频率派的半参数效率界，主要提供先验构造思路的参考。

### 6. [10.1093/biomtc/ujae062](https://doi.org/10.1093/biomtc/ujae062) — Absolute risk from double nested case-control designs: cause-specific proportional hazards models with and without augmented estimating equations
- **作者**: Minjung Lee, Mitchell H Gail
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在竞争风险下的 cause-specific proportional hazards 模型中，针对 double nested case-control (DNCC) 设计，目标是估计相对风险和绝对风险（累积发生率），关键假设为 Samuelsen-type 逆抽样概率计算与 phase-two 采样设计。提出两种估计器：design-weighted estimator 使用逆抽样概率加权；augmented design-weighted estimator 在估计方程中增补一项利用全队列辅助信息，该增广项期望为零但减小方差。建立了两种估计器（含绝对风险估计器）的渐近性质，导出一致方差估计器，并证明增广估计器比纯加权估计器更有效。关键技术工具包括 Samuelsen-type 权重计算、augmented estimating equations 与 competing risks 的 cause-specific hazard 分解。模拟显示有限样本下名义覆盖良好；应用于 NCI 前列腺癌筛查试验数据。对您有用：augmented estimating equations 的效率提升思路与 semiparametric efficiency theory 直接相关（利用辅助信息逼近效率界），且 DNCC 设计在流行病学队列研究中常见，方法可迁移到两阶段采样下的因果推断问题。
- **关键技术**: `augmented estimating equations`, `design-weighted estimation`, `cause-specific proportional hazards`, `competing risks`, `Samuelsen-type inverse sampling probability`, `double nested case-control design`
- **为什么对您有用**: augmented estimating equations 利用辅助信息提升效率的思路与 semiparametric efficiency theory 直接相关，且 DNCC 设计在流行病学队列研究中常见，方法可迁移到两阶段采样下的因果推断与效率优化问题。

### 7. [10.1093/biomtc/ujae063](https://doi.org/10.1093/biomtc/ujae063) — Nonparametric receiver operating characteristic curve analysis with an imperfect gold standard
- **作者**: Jiarui Sun, Chao Tang, Wuxiang Xie, Xiao-Hua Zhou
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究在参考标准存在误分类（imperfect gold standard）的诊断准确性研究中，非参数识别和估计 ROC 曲线及 AUC 的问题。在已知或可估参考标准准确度及条件独立性假设下，作者证明了 ROC 曲线的非参数可识别性，并提出了非参数估计方法。当参考标准准确度未知时，ROC 曲线不可识别，但作者证明了两个 AUC 差值符号的可识别性，据此构建了比较 AUC 相对优势的假设检验方法。该方法无需参数模型假设，适用于连续和有序生物标志物。理论分析与模拟研究验证了方法性质，并在两项真实诊断数据中进行了应用。对您有用之处在于：其基于条件独立性的非参数识别策略与 proximal CI 中的 proxy 假设结构相似，且在部分识别下利用差值符号构建假设检验的思路，对您的假设检验与因果敏感性分析方向有直接启发。
- **关键技术**: `nonparametric identification`, `conditional independence assumption`, `AUC difference testing`, `imperfect reference standard`, `partial identifiability`
- **为什么对您有用**: 条件独立性假设下的非参数识别策略与 proximal CI 的 proxy 结构高度相似；在参数不可识别时利用差值符号构建假设检验的思路，对您的数学统计假设检验及因果敏感性分析有方法论启发。

### 8. [10.1093/biomtc/ujae098](https://doi.org/10.1093/biomtc/ujae098) — Semi-parametric benchmark dose analysis with monotone additive models
- **作者**: Alex Stringer, Tugba Akkaya Hocagil, Richard J Cook, Louise M Ryan, Sandra W Jacobson, Joseph L Jacobson
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在基准剂量（benchmark dose, BMD）分析框架下，利用单调可加半参数剂量–反应模型估计毒素暴露的临界水平，并以置信区间下限量化不确定性。模型拟合采用 penalized B-spline 结合 Laplace 近似边际似然选择光滑参数，估计通过 reflective Newton 方法实现，内嵌 de Boor 算法高效计算样条及其导数。推断方面，作者针对 BMD 估计所满足的非线性方程构造了近似枢轴量（approximate pivot），据此计算 BMD 下限，相比 Delta method 和参数 bootstrap 有更优的覆盖性质。实证部分将方法应用于六项 NIH 纵向队列研究，推断产前酒精暴露与儿童认知缺陷的关联剂量，并提供了 R 包 semibmd。对您而言，该文的近似枢轴量构造思路可迁移至其他半参数非线性估计的区间推断问题，同时 penalized spline + Laplace marginal likelihood 的计算方案对统计计算方向有参考价值。
- **关键技术**: `penalized B-spline`, `Laplace-approximate marginal likelihood`, `reflective Newton method`, `de Boor's algorithm`, `approximate pivot for nonlinear estimator`, `monotone additive model`
- **为什么对您有用**: 半参数单调可加模型的推断与计算直接关联您的 semiparametric theory 和 statistical computing 兴趣；近似枢轴量构造为非线性半参数估计的置信区间提供了可迁移思路；流行病学纵向队列的实证分析契合您的 epidemiology secondary interest。

## 数理统计 / 假设检验  *(hypothesis_testing, 4 篇)*

### 1. [10.1093/biomtc/ujae088](https://doi.org/10.1093/biomtc/ujae088) — High-dimensional multivariate analysis of variance via geometric median and bootstrapping
- **作者**: Guanghui Cheng, Ruitao Lin, Liuhua Peng
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究高维数据下的多元方差分析（MANOVA）问题，目标是在多组高维总体中基于几何中位数（geometric median）检验位置参数的异质性。作者提出一种基于组间几何中位数差异的 maximum-type 检验统计量，利用 Gaussian approximation 推导了其在零假设下的极限分布，并证明了备择假设下的检验一致性。为解决高维下统计量分布的逼近问题，提出并理论验证了 wild bootstrap 算法的有效性。仿真实验和乳腺癌基因表达数据的实证分析表明，相较于传统均值方法，该检验在有限样本下对异常值具有更好的鲁棒性。对您有用：该文将几何中位数引入高维假设检验，其 maximum-type 统计量构造与 wild bootstrap 计算方案可直接迁移到您关注的高维假设检验与统计计算方向。
- **关键技术**: `geometric median`, `maximum-type test statistic`, `Gaussian approximation`, `wild bootstrap`, `high-dimensional MANOVA`, `robust location estimation`
- **为什么对您有用**: 直接切中您的高维假设检验与统计计算兴趣；其基于几何中位数的 maximum-type 统计量构造及 wild bootstrap 算法理论，为高维鲁棒检验提供了新的计算与推断思路。

### 2. [10.1093/biomtc/ujae101](https://doi.org/10.1093/biomtc/ujae101) — Post-selection inference in regression models for group testing data
- **作者**: Qinyan Shen, Karl Gregory, Xianzheng Huang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在 group testing 数据的 logistic 回归中，响应变量仅通过有误的池化检测结果部分观测，目标是变量选择后对选中协变量效应进行有效推断。作者先用 EM 算法计算 LASSO 惩罚下的 MLE 以完成变量选择，随后将基于 polyhedral lemma 的 post-selection inference 方法扩展到响应缺失/有误的设定，构造选择条件下的有效置信区间与检验。模拟表明，相比不做选择调整的朴素推断，该方法在覆盖率和 Type-I error 控制上更可靠。该文将 selective inference 从完全观测设定推广至部分观测响应，对您在假设检验方向了解 polyhedral lemma 在非标准数据结构下的扩展有参考价值。
- **关键技术**: `post-selection inference`, `polyhedral lemma`, `EM algorithm`, `LASSO penalization`, `group testing`, `selective inference`
- **为什么对您有用**: 直接关联您 primary interest 中的假设检验方向——post-selection inference 是 selective inference 的重要子领域；polyhedral lemma 从完全观测到部分观测响应的扩展，为非标准数据结构下的选择后推断提供了可迁移的方法论模板。

### 3. [10.1093/biomtc/ujae079](https://doi.org/10.1093/biomtc/ujae079) — Hypothesis tests in ordinal predictive models with optimal accuracy
- **作者**: Yuyang Liu, Shan Luo, Jialiang Li
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在多类别有序判别设定下，目标是检验多个预测变量的线性组合是否达到最优 ROC 流形超体积（HUM），现有推断方法计算代价高昂。本文提出基于 Jackknife 经验似然（JEL）的检验框架，在温和正则条件下建立了 Wilks 定理，并推导了 Pitman 备择下的功效分析。核心计算瓶颈在于检验统计量涉及一般多样本 U-统计量，作者为此提出了一种基于网络图的快速计算算法以大幅降低计算复杂度。模拟显示该方法在检验水平、功效和运行时间上均具优势，并在真实医学数据中展示了新发现。对您有用：该文不仅推进了有序分类的假设检验理论，其针对多样本 U-统计量的网络快速算法对您在统计计算与高阶 U-统计量方向的研究具有直接的迁移价值。
- **关键技术**: `jackknife empirical likelihood`, `hypervolume under ROC manifolds`, `multi-sample U-statistic`, `Wilks' theorem`, `network-based computation algorithm`, `Pitman alternative`
- **为什么对您有用**: 直接切中您在假设检验与高阶 U-统计量的核心兴趣；其针对多样本 U-统计量提出的网络快速算法，对您在统计计算方向的工作（尤其是 U-统计量的数值优化与算法设计）具有直接的借鉴价值。

### 4. [10.1093/biomtc/ujae082](https://doi.org/10.1093/biomtc/ujae082) — Summary statistics knockoffs inference with family-wise error rate control
- **作者**: Catherine Xinrui Yu, Jiaqi Gu, Zhaomeng Chen, Zihuai He
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在仅有边际依赖汇总统计量可用的设定下，本文研究条件独立性多重假设检验，目标是在控制 family-wise error rate (FWER) 的前提下筛选与响应条件相关的特征。方法采用 GhostKnockoff 框架直接生成汇总统计量的 knockoff 副本，并提出了一种新的 filter 规则来挑选条件依赖变量。此外，作者开发了一种计算高效的算法，大幅降低了 knockoff 副本生成的计算复杂度，且不损失统计功效与 FWER 控制。模拟与阿尔茨海默病遗传学真实数据实验表明，该方法在统计功效与计算效率上均优于现有替代方案。该工作将高维多重假设检验与计算优化结合，其基于汇总统计量的 knockoff 推断框架对您在假设检验与高维统计计算方向的研究有直接参考价值，且遗传学数据集对流行病学应用有借鉴意义。
- **关键技术**: `GhostKnockoff`, `family-wise error rate control`, `conditional independence testing`, `summary statistics`, `high-dimensional variable selection`
- **为什么对您有用**: 直接涉及高维多重假设检验（FWER）与计算优化，属于您 primary interest 中的 hypothesis testing 与 statistical computing 交叉；真实数据应用（阿尔茨海默病遗传学）也与您 secondary interest 中的 epidemiology 数据集契合。

## 统计计算 / 算法  *(stat_computing, 3 篇)*

### 1. [10.1093/biomtc/ujae059](https://doi.org/10.1093/biomtc/ujae059) — Bayesian inference for multivariate probit model with latent envelope
- **作者**: Kwangmin Lee, Yeonhee Park
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在多元 probit 模型的潜变量框架下，本文提出 latent envelope 概念以剥离“无关变异”，从而提升回归系数的估计效率。该方法将响应包络模型的思想引入多元 probit 的高斯潜变量结构中，通过 essential identifiability 概念解决模型的可识别性问题，并提出基于贝叶斯 MCMC 的参数估计流程。模拟研究表明，相比标准多元 probit 模型，该模型在参数估计上具有效率增益；实证分析展示了其在多标签分类中的实用性。对您可能有用：虽然本文关注参数效率而非半参数效率界，但 envelope 降维思想对处理多元二值响应（常见于计量经济学和流行病学应用）的效率提升具有借鉴意义。
- **关键技术**: `latent envelope model`, `multivariate probit model`, `essential identifiability`, `Bayesian MCMC`, `parametric efficiency improvement`
- **为什么对您有用**: 涉及多元二值响应模型的估计效率提升，与您关注的 efficiency theory 相关（尽管是参数效率而非半参数效率），且多元 probit 模型是计量经济学和流行病学的常用工具，方法可迁移。

### 2. [10.1093/biomtc/ujae089](https://doi.org/10.1093/biomtc/ujae089) — Visibility graph-based covariance functions for scalable spatial analysis in non-convex partially Euclidean domains
- **作者**: Brian Gilbert, Abhirup Datta
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在非凸部分欧几里得域（如水体）的空间分析中，目标是构建高斯过程的有效协方差函数，解决基于测地距离的协方差未必正定且现有方法无法保持部分欧氏性质的问题。利用域上的可见性图（visibility graph），提出一类新协方差函数：对域内可见点对保留欧氏协方差，对不可见点对通过条件独立性引入非凸几何。理论证明该方法在保证协方差正定性与边缘平稳性的同时，保持了域内局部几何的部分欧氏性质。引入近似策略提升计算效率，实现可扩展算法。模拟与切萨皮克湾酸度数据验证了方法优势。对您有用：若关注统计计算中大规模图结构协方差或高斯过程的数值算法与正定性理论，本文的图构造与近似计算思路可作参考。
- **关键技术**: `visibility graph`, `Gaussian process covariance`, `positive definiteness`, `partially Euclidean domain`, `scalable spatial algorithm`
- **为什么对您有用**: 涉及统计计算中的可扩展算法与协方差矩阵正定性理论，若您对高斯过程或图结构协方差的数值计算与理论性质感兴趣，本文的图构造与近似策略可提供方法迁移的参考。

### 3. [10.1093/biomtc/ujae104](https://doi.org/10.1093/biomtc/ujae104) — Planning cost-effective operational forest inventories
- **作者**: Santeri Karppinen, Liviu Ene, Lovisa Engberg Sundström, Juha Karvanen
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 1/10 · novelty: `application`
- **摘要**: 本文研究运营林业中的贝叶斯两阶段决策问题：外层选择伐前清查精度，内层根据清查信息调度采伐以满足需求目标。外层被建模为预算约束下后验价值最大化问题，其解析计算不可行——需要在高维积分内求解一个 NP-hard 的广义二次指派问题。作者提出将 Monte Carlo 采样与贪心随机化方法结合的近似算法来求解外层问题，并在 100 个瑞典林地的数据集上给出了不同预算下的清查决策及信息价值估计。该方法对高维积分内嵌组合优化的计算框架有参考意义，但对您而言方法学新颖性有限，主要价值在于 Monte Carlo + 组合优化近似这一计算思路可迁移到其他贝叶斯决策问题。
- **关键技术**: `Bayesian two-stage decision problem`, `posterior value of information`, `Monte Carlo integration`, `greedy randomized approximation`, `generalized quadratic assignment problem`
- **为什么对您有用**: 与您 statistical computing 兴趣有弱连接：高维积分内嵌 NP-hard 优化的 Monte Carlo + 贪心近似思路可迁移，但问题设定偏应用且无 semiparametric / efficiency / high-dim inference 层面的贡献。

## 流行病学  *(epidemiology, 6 篇)*

### 1. [10.1093/biomtc/ujae092](https://doi.org/10.1093/biomtc/ujae092) — Sensitivity analysis for publication bias in meta-analysis of sparse data based on exact likelihood
- **作者**: Taojun Hu, Yi Zhou, Satoshi Hattori
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在稀疏数据（低事件率二项/计数结局）的 Meta 分析设定下，传统 normal-normal 随机效应模型因正态近似失效导致推断不稳定，本文目标是基于精确似然对发表偏倚进行敏感性分析。方法上，作者采用广义线性混合模型 (GLMM) 替代正态近似以消除稀疏性偏差，并将 Copas 基于似然的敏感性分析（结合 t-统计量选择函数）扩展至 GLMM 框架。核心机制在于通过精确似然构建选择函数下的修正估计量，从而在选择性发表机制下评估总体效应的稳健性。模拟与实际数据分析表明，基于 GLMM 的方法在稀疏设定下显著优于基于 normal-normal 模型的同类方法。虽然本文的敏感性分析针对发表偏倚而非因果未观测混杂，但其处理稀疏数据精确似然及选择函数的思路，对您在流行病学罕见结局因果推断中的敏感性分析有一定参考价值。
- **关键技术**: `generalized linear mixed model`, `exact likelihood`, `Copas selection model`, `sensitivity analysis`, `random-effects meta-analysis`
- **为什么对您有用**: 虽然本文做的是发表偏倚而非因果敏感性分析，但稀疏数据（常见于流行病学罕见结局）下用精确似然替代正态近似的思路，对您在流行病学应用中处理罕见事件因果推断的敏感性分析有方法迁移价值。

### 2. [10.1093/biomtc/ujae075](https://doi.org/10.1093/biomtc/ujae075) — The multivariate Bernoulli detector: change point estimation in discrete survival analysis
- **作者**: Willem van den Boom, Maria De Iorio, Fang Qian, Alessandra Guglielmi
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在离散时间-事件数据的竞争风险框架下，本文目标是估计原因别基准风险（cause-specific baseline hazards）中的变点及风险间依赖结构。提出多元 Bernoulli 检测器，通过变点数量与位置的先验实现跨风险变点依赖及变点数的数据驱动学习；条件于变点，使用多元 Bernoulli 先验推断涉及的风险。推断聚焦于原因别风险率与跨风险依赖（源于影响所有风险的个体特定时间变化）。计算上采用定制的 local-global MCMC 算法，结合数据增广与非共轭贝叶斯非参数更新。模拟与 ICU 数据验证了其性能。对您而言，该文提供了流行病学竞争风险场景的贝叶斯非参数变点方法与数据集，但缺乏您核心关注的半参数效率或因果推断理论。
- **关键技术**: `competing risks`, `discrete survival analysis`, `multivariate change point model`, `Bayesian nonparametrics`, `local-global MCMC`, `data augmentation`
- **为什么对您有用**: 提供了流行病学（ICU数据）离散生存分析与竞争风险的贝叶斯非参数变点方法，可作为纵向/生存数据的应用场景参考，但缺乏您核心关注的半参数效率界或因果推断设定。

### 3. [10.1093/biomtc/ujae097](https://doi.org/10.1093/biomtc/ujae097) — Designing cancer screening trials for reduction in late-stage cancer incidence
- **作者**: Kehao Zhu, Ying-Qi Zhao, Yingye Zheng
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在癌症早筛随机对照试验（RCT）设计中，目标是量化生物标志物检测对晚期癌症发病率的因果效应，但面临疾病自然史漫长和时变筛查效应难以刻画的挑战。本文提出一种通用多状态疾病史模型（multistate disease history model），将检测敏感度等关键性能指标与晚期发病率等主要终点相联系。基于 RCT 的日历时间尺度，推导了模型驱动的效应量（model-based effect sizes），并据此评估新筛查方案（检测敏感度、随访时长、检测频率）下的统计功效。该方法还整合了生物标志物检测在真实场景中的实际执行情况。通过国家肺癌筛查试验（NLST）的数值实例展示了该工具在策略制定中的快速评估能力。对您可能有用：该文将多状态模型与筛查的时变因果效应评估结合，为流行病学队列中的纵向因果推断和 RCT 功效分析提供了可迁移的建模思路。
- **关键技术**: `multistate disease history model`, `model-based effect size`, `time-varying screening effect`, `RCT power calculation`, `late-stage cancer incidence`
- **为什么对您有用**: 涉及流行病学应用中的纵向因果效应评估（筛查对晚期发病率的因果作用）和真实数据集（NLST），其多状态建模思路对您在纵向因果推断和流行病学应用方向的 RCT 设计有参考价值。

### 4. [10.1093/biomtc/ujae074](https://doi.org/10.1093/biomtc/ujae074) — Semiparametric inference of effective reproduction number dynamics from wastewater pathogen surveillance data
- **作者**: Isaac H Goldstein, Daniel M Parker, Sunny Jiang, Volodymyr M Minin
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在废水病原体监测数据下，目标是估计有效再生数（R_t）的动态变化，设定为时变移民率模型，从而避免对易感人群动态的强假设。方法采用半参数推断框架，将新感染到达过程建模为时变移民过程，并由此构建 R_t 的估计量。该框架作为副产品也适用于传统病例数据的 R_t 估计，模拟部分采用基于智能体的模型并纳入真实的时变病毒脱落机制来检验估计量表现。实证分析将模型应用于洛杉矶大型废水处理厂的 SARS-CoV-2 RNA 浓度数据。对您有用：该文结合了半参数理论与流行病学应用，对您在流行病学数据集上探索放松假设的半参数估计方法具有直接参考价值。
- **关键技术**: `semiparametric inference`, `time-varying immigration process`, `effective reproduction number estimation`, `agent-based simulation`, `wastewater epidemiology`
- **为什么对您有用**: 直接结合了您的主攻方向“半参数理论”与次攻方向“流行病学数据集”，展示了如何在放松易感人群动态假设的半参数框架下进行推断，方法可迁移至其他动态流行病学参数估计。

### 5. [10.1093/biomtc/ujae068](https://doi.org/10.1093/biomtc/ujae068) — A Gaussian-process approximation to a spatial SIR process using moment closures and emulators
- **作者**: Parker Trostle, Joseph Guinness, Brian J Reich
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 0/10 · novelty: `application`
- **摘要**: 在空间流行病学设定下，本文针对带噪声与漏报的时空感染计数，提出一种基于高斯过程近似的推断框架。作者首先将经典 SIR 随机过程扩展至空间情形，并通过矩闭合（moment-closure）近似推导出描述易感与感染人群均值及协方差随时间演化的常微分方程（ODE）。由于 ODE 求解是 MCMC 拟合的计算瓶颈，文中采用低秩模拟器（low-rank emulator）对其进行快速近似，并以此构建处理漏报数据的层级贝叶斯模型。模拟与巴西寨卡病毒真实数据的应用表明该方法在计算效率与推断精度间取得了良好平衡。对您而言，该文不仅提供了流行病学空间面板数据的建模案例，其用低秩模拟器加速 ODE 与 MCMC 的计算策略对统计计算方向亦有借鉴意义。
- **关键技术**: `spatial SIR process`, `Gaussian process approximation`, `moment-closure approximation`, `low-rank emulator`, `hierarchical Bayesian model`, `MCMC acceleration`
- **为什么对您有用**: 属于流行病学应用方向，提供了空间面板数据的层级建模与漏报处理案例；其用低秩模拟器加速 ODE 求解与 MCMC 采样的计算技巧，对您的统计计算兴趣有直接参考价值。

### 6. [10.1093/biomtc/ujae060](https://doi.org/10.1093/biomtc/ujae060) — PathGPS: discover shared genetic architecture using GWAS summary data
- **作者**: Zijun Gao, Qingyuan Zhao, Trevor Hastie
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在 GWAS 汇总数据设定下，提出 PathGPS 探索性分析工具，旨在通过线性结构方程模型（SEM）发现共享遗传结构，假设表型受遗传与环境路径共同调控。方法核心通过对比“信号基因”与“噪声基因”的 GWAS 关联差异，解耦遗传与环境成分；随后利用低秩与稀疏性质，对提取的遗传成分进行主成分分析与因子分析以挖掘遗传路径；此外，采用 bagging 算法提升数据扰动与超参数调优下的稳定性。在代谢组学与 UK Biobank 上的应用验证了已知基因-表型簇并提出了新假设。对您而言，该文展示了线性 SEM 在高维基因组数据中的降维与解耦应用，其基于信号/噪声对比的解耦思路可为因果推断中混淆因素的识别或高维因子模型提供启发。
- **关键技术**: `linear structural equation model`, `principal component analysis`, `low-rank sparse factor analysis`, `bootstrap aggregating`, `GWAS summary statistics`
- **为什么对您有用**: 虽然是流行病学应用，但其利用线性 SEM 解耦遗传与环境成分的思路，以及高维低秩因子分析的实现，对您在因果推断（SEM 识别与解耦）和高维统计（低秩稀疏降维）方面的研究有方法论参考；同时 UK Biobank 数据集对流行病学应用也有价值。

## 其他  *(other, 5 篇)*

### 1. [10.1093/biomtc/ujae093](https://doi.org/10.1093/biomtc/ujae093) — A Bayesian latent-subgroup platform design for dose optimization
- **作者**: Rongji Mu, Xiaojiang Zhan, Rui (Sammi) Tang, Ying Yuan
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文在 FDA Project Optimus 背景下，针对肿瘤药物剂量优化提出基于 master protocol 的平台试验设计，目标是在多个适应症中同时识别最优生物剂量（OBD）。核心方法为 Bayesian latent subgroup model 以刻画跨适应症的治疗异质性，并采用 Bayesian hierarchical model 在子群间借信息；每期 interim analysis 更新子群归属、剂量-毒性/疗效曲线及 utility 估计，指导剂量升降决策。模拟显示该设计相比独立试验有更优的 operating characteristics，可缩短开发周期并降低成本。方法学上属于贝叶斯自适应试验设计，理论 novelty 有限，未涉及半参数效率界或高维推断；对您而言仅在与贝叶斯计算或 latent class 模型的数值实现方面有边际参考价值。
- **关键技术**: `Bayesian latent subgroup model`, `Bayesian hierarchical borrowing`, `platform trial master protocol`, `dose-finding utility optimization`, `adaptive interim analysis`
- **为什么对您有用**: 与您的主要兴趣方向（因果推断、半参数效率、高维理论）重叠极小；仅在 Bayesian computing 的数值实现层面有微弱关联，不构成优先阅读。

### 2. [10.1093/biomtc/ujae081](https://doi.org/10.1093/biomtc/ujae081) — Towards automated animal density estimation with acoustic spatial capture-recapture
- **作者**: Yuheng Wang, Juan Ye, Xiaohui Li, David L Borchers
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在声学空间标记-重捕（ASCR）框架下，目标是估计动物叫声密度，核心挑战是机器学习分类器产生的误报（false positives）问题。本文提出将物种身份作为潜在变量，将ML分类器的个体级输出视为依赖于该潜在身份的随机变量，从而构建混合模型似然函数。通过最大化该混合似然函数实现叫声密度的估计，无需依赖传统的启发式校正因子。模拟与实证数据（青蛙与长臂猿声学调查）表明，该方法偏差近零且置信区间覆盖概率准确，显著优于忽略误报的ASCR及校正因子法。对您而言，该文将误分类问题转化为潜在变量进行identification与似然推断的思路，可为因果推断中处理测量误差或处理变量错分类提供模型构建上的参考。
- **关键技术**: `spatial capture-recapture`, `latent variable model`, `mixture model likelihood`, `false positive misclassification`, `measurement error correction`
- **为什么对您有用**: 虽然属于生态学应用，但其将误分类（false positive）视为潜在变量进行identification与似然推断的思路，可为因果推断中处理测量误差或错分类问题提供模型构建上的参考。

### 3. [10.1093/biomtc/ujae066](https://doi.org/10.1093/biomtc/ujae066) — An interpretable Bayesian clustering approach with feature selection for analyzing spatially resolved transcriptomics data
- **作者**: Huimin Li, Bencong Zhu, Xi Jiang, Lei Guo, Yang Xie, Lin Xu et al.
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对空间转录组学（SRT）数据，提出一种基于零膨胀负二项（ZINB）混合模型的可解释贝叶斯空间聚类方法。为提升可解释性，模型内嵌特征选择机制以筛选区分性基因，提供低维摘要；同时通过马尔可夫随机场（MRF）先验整合空间地理信息，实现分子特征与空间结构的联合建模。仿真与真实数据表明该联合建模策略在聚类精度上优于现有方法。对您而言，该文展示了高维计数数据的贝叶斯特征选择与空间先验建模思路，但在半参数/效率理论或因果推断方面的方法学深度有限。
- **关键技术**: `zero-inflated negative binomial mixture`, `Markov random field prior`, `Bayesian feature selection`, `spatial clustering`
- **为什么对您有用**: 涉及高维分子数据的特征选择与空间先验建模，但方法为参数化贝叶斯框架，与您关注的半参数效率界、RMT或因果推断等核心理论方向重叠较低，主要提供高维计数数据建模的应用视角。

### 4. [10.1093/biomtc/ujae072](https://doi.org/10.1093/biomtc/ujae072) — Improving prediction of linear regression models by integrating external information from heterogeneous populations: James–Stein estimators
- **作者**: Peisong Han, Haoyue Li, Sung Kyun Park, Bhramar Mukherjee, Jeremy M G Taylor
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在内部研究有个体数据拟合线性回归、外部研究仅提供基于部分协变量的降维模型系数估计且总体存在异质性的设定下，本文目标是整合外部摘要信息以提升内部模型的预测精度。作者将 James-Stein 收缩方法适配于此设定，提出一类新的收缩估计量。理论上，无论总体间异质性程度如何，该估计量在预测均方误差（PMSE）意义下保证不劣于（且通常优于）仅用内部数据的 OLS 估计量。模拟研究全面验证了所提估计量的数值表现。实证部分将该方法应用于膝盖骨铅水平预测，通过整合已发表文献的摘要信息成功提升了预测精度。对您可能有用：虽然本文聚焦预测而非因果推断，但其处理外部异质数据整合的 James-Stein 收缩思路，可为流行病学（secondary interest）中多源数据整合或元分析提供数学统计视角的参考。
- **关键技术**: `James-Stein shrinkage`, `prediction mean squared error`, `external summary data integration`, `heterogeneous populations`, `domination result`
- **为什么对您有用**: 虽然核心是预测而非因果推断，但处理外部异质总体摘要数据的 James-Stein 收缩框架，对您在流行病学（secondary interest）中整合多源数据或进行多中心因果推断时的效率提升有参考价值。

### 5. [10.1093/biomtc/ujae094](https://doi.org/10.1093/biomtc/ujae094) — Adjusting for incomplete baseline covariates in randomized controlled trials: a cross-world imputation framework
- **作者**: Yilin Song, James P Hughes, Ting Ye
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 3
- 相关性 0/10
- **摘要**: {
  "topic": "causal_inference",
  "summary_zh": "在 RCT 中调整基线协变量可提升处理效应估计精度，但协变量常有缺失；本文在 Zhao & Ding (2022) 的基础上，提出 cross-world imputation (CWI) 理论框架，统一了 single imputation 与 missingness-indicator method (MIM) 两种策略。CWI 框架将缺失值填充视为跨"世界"（处理/对照）的借补问题，在此视角下证明 MIM 隐式地搜索了最优 CWI 值，从而达到最优效率；同时推导了 single imputation 在何种条件下通过优化填充值可达到与 MIM 相同的效率界。理论工具主要涉及线性回归模型下协变量调整的方差分解与效率比较。模拟与 Childhood Adenotonsillectomy Trial 数据验证了结论。对您有用：该文将缺失协变量调整的效率问题置于统一理论框架，直接连接您 primary interest 中的因果推断（RCT 协变量调整）与效率理论（不同策略的效率界比较）。",
  "key_techniques": [
    "cross-world imputation framework",
    "missingness-indicator method",


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

