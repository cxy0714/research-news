# Biometrics — Vol 80  Issue 2  ·  2026-05-21

- 共 33 篇 · Biometrics

## 因果推断  *(causal_inference, 14 篇)*

### 1. [10.1093/biomtc/ujae055](https://doi.org/10.1093/biomtc/ujae055) — Doubly robust proximal synthetic controls
- **作者**: Hongxiang Qiu, Xu Shi, Wang Miao, Edgar Dobriban, Eric Tchetgen Tchetgen
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 10/10 · novelty: `new_method`
- **摘要**: 在面板数据的合成控制（SC）设定下，针对单一处理单元的 ATT 识别，传统方法依赖反事实结果模型的正确设定与近乎完美的前测拟合。本文引入 proximal causal inference 框架与协变量偏移（covariate shift）概念，推导出两个非参数识别公式：一个基于权重，另一个结合了反事实结果与权重函数。基于广义矩估计（GMM），作者提出了两个处理效应估计量，其中一个是双重稳健（doubly robust）的：当结果模型或权重模型至少一个正确设定时，该估计量具有相合性与渐近正态性。该方法放松了传统 SC 对完美前测拟合的依赖，并在巴西肺炎球菌疫苗效果的流行病学数据中进行了验证。对您而言，这篇论文将 proximal CI 拓展至纵向面板 SC 设定，其双重稳健估计与 GMM 构造直接契合您在 proximal CI 与半参数效率理论方面的研究兴趣。
- **关键技术**: `proximal causal inference`, `doubly robust estimation`, `generalized method of moments`, `synthetic control`, `covariate shift`
- **为什么对您有用**: 直接将您主要关注的 proximal CI 框架拓展至纵向面板数据的合成控制问题，给出了双重稳健估计量与 GMM 构造，对研究 SC 设定下的半参数效率与弱假设识别具有直接参考价值；同时其流行病学应用契合您的次级兴趣。

### 2. [10.1093/biomtc/ujae046](https://doi.org/10.1093/biomtc/ujae046) — Integrating randomized and observational studies to estimate optimal dynamic treatment regimes
- **作者**: Anna Batorsky, Kevin J Anstrom, Donglin Zeng
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在纵向因果推断设定下，本文目标是融合 SMART（序贯多重分配随机试验）与观察性研究（OS）数据，以更高效率估计最优动态治疗策略（DTR）及其值函数。作者提出多阶段增强 Q-learning 估计量（MAQE），将单阶段试验-观察数据融合的增强方法扩展至多阶段 Q-learning 框架。核心机制是在每个决策阶段的 Q 函数估计中，利用 OS 数据的辅助信息构造增强项，实现类似 AIPW 的方差缩减。在标准因果正则假设（如 OS 无未测量混杂、一致性）下，MAQE 保持 n^{-1/2}-CAN 性质并具有更优的渐近效率。模拟与慢性腰痛数据分析表明，MAQE 在估计精度和平均值函数上均优于未增强的 Q-learning，且对样本量比例和噪声变量稳健。该文将数据融合的效率提升拓展至多阶段决策，其增强估计量的构造思路对您研究纵向因果推断与半参数效率理论具有直接参考价值。
- **关键技术**: `dynamic treatment regimes`, `Q-learning`, `data fusion`, `augmented estimator`, `variance reduction`, `sequential multiple assignment randomized trial`
- **为什么对您有用**: 直接关联您 primary interest 中的纵向因果推断与效率理论，展示了如何在多阶段决策中通过融合观察性数据构造增强估计量以实现方差缩减；同时其慢性腰痛的应用背景契合您 secondary interest 中的流行病学因果应用。

### 3. [10.1093/biomtc/ujae027](https://doi.org/10.1093/biomtc/ujae027) — Single proxy control
- **作者**: Chan Park, David B Richardson, Eric J Tchetgen Tchetgen
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 9/10 · novelty: `new_theory`
- **摘要**: 在非实验研究中利用负控制结果（NCO）校正未观测混淆，目标是在单代理（single proxy）设定下非参数识别受处理组平均因果效应（ATT）。本文将 COCA（Control Outcome Calibration Approach）从经典的秩保留结构模型推广至非参数识别框架，从而允许无限制的处理效应异质性。作者提出了三种估计策略：扩展倾向得分法、结果桥函数法以及双重稳健（doubly-robust）估计法。理论上，该工作实现了仅需单一负控制代理的混淆控制，突破了近期 proximal CI 必须依赖一对混淆代理（NCO+NCE）的识别限制。实证部分通过评估巴西寨卡病毒爆发对出生率的因果影响展示了方法应用。对您有用：直接推进了 proximal CI 的理论边界（单代理识别放松了成对假设），且双重稳健估计器与您的效率理论兴趣高度契合，流行病学应用也提供了真实数据参考。
- **关键技术**: `proximal causal inference`, `negative control outcome`, `single proxy identification`, `outcome bridge function`, `doubly robust estimation`, `Control Outcome Calibration Approach (COCA)`
- **为什么对您有用**: 直接推进了您关注的 proximal causal inference 领域，将识别条件从一对代理放松至单一代理，其双重稳健估计策略也与您的效率理论兴趣高度契合，流行病学应用提供了真实数据参考。

### 4. [10.1093/biomtc/ujae050](https://doi.org/10.1093/biomtc/ujae050) — Dissecting the colocalized GWAS and eQTLs with mediation analysis for high-dimensional exposures and confounders
- **作者**: Qi Zhang, Zhikai Yang, Jinliang Yang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在高维暴露、混杂与中介的设定下，本文研究 GWAS/eQTL 共定位数据的中介效应估计，目标参数为每个暴露的总体间接效应（overall IE）。提出 MedDiC 方法，基于系数差法（difference-in-coefficients）构建 IE 估计量，以应对高维暴露与混杂的挑战。方法结合了高维惩罚回归与去偏推断技术，保证了高维设定下 IE 的有效估计与置信区间构造。模拟研究表明，MedDiC 相较于竞争方法具有更高的检验功效、更短的置信区间及更快的计算速度。在玉米与小鼠基因组的实证分析中，MedDiC 产出了跨性状可复现且受外部生物学证据支持的结果。对您有用：该方法直接推进了高维中介分析，其处理高维混杂的 difference-in-coefficients 策略与快速计算实现，对您在因果推断（中介分析）与高维统计交叉方向的研究具有直接参考价值。
- **关键技术**: `mediation analysis`, `difference-in-coefficients`, `high-dimensional penalized regression`, `debiased inference`, `overall indirect effect`
- **为什么对您有用**: 直接命中您 primary interest 中的因果推断（中介分析）与高维统计交叉方向。其基于 difference-in-coefficients 处理高维暴露/混杂的推断策略及快速计算实现，对您研究高维中介效应的估计与统计算法设计有直接借鉴意义。

### 5. [10.1093/biomtc/ujae058](https://doi.org/10.1093/biomtc/ujae058) — Differential recall bias in estimating treatment effects in observational studies
- **作者**: Suhwan Bong, Kwonsang Lee, Francesca Dominici
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在回顾性队列研究的因果推断中，当自我报告的二值暴露存在依赖于结局的差异性回忆偏倚（differential recall bias）时，ATE 的识别面临根本性挑战。本文在无验证子样本（validation study）的设定下，推导了 ATE 的识别界（bounds），并基于不同的先验假设提出了多种估计方法。同时，作者提出了一种敏感性分析框架，将先验流行病学知识编码为偏倚参数的约束，以评估因果结论对差异性误分类的稳健性。模拟表明所提方法在模型误配下仍具稳健性，实证分析评估了童年虐待对成年心理健康的影响。对您有用：该文在无验证数据下的 bound 推导与敏感性分析框架，直接契合您在因果推断中 sensitivity analysis 与 identification 的核心兴趣，且提供了流行病学应用场景的完整分析范式。
- **关键技术**: `differential misclassification`, `partial identification bounds`, `sensitivity analysis`, `recall bias correction`, `observational study without validation data`
- **为什么对您有用**: 直接契合您在因果推断中 sensitivity analysis 与 identification 的核心兴趣；无验证数据下的 bound 推导放松了传统假设，且实证部分提供了流行病学队列研究的因果分析范式。

### 6. [10.1093/biomtc/ujae023](https://doi.org/10.1093/biomtc/ujae023) — Behavioral carry-over effect and power consideration in crossover trials
- **作者**: Danni Shi, Ting Ye
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 6/10 · novelty: `new_theory`
- **摘要**: 本文在潜在结果框架下研究交叉设计中的遗留效应问题，目标参数为处理效应，关键假设为遗留效应的符号条件。发现当遗留效应存在且满足符号条件时，基本估计量会低估处理效应，此偏差不膨胀单边检验的第一类错误但会降低功效。基于此推导了交叉设计与平行组设计的功效权衡条件，明确了交叉设计在不膨胀第一类错误且保持更高功效的适用边界。此外，提出了交叉试验的协变量调整方法以提升估计效率。理论与方法在 MTN-034/REACH 流行病学数据中进行了评估。对您有用：该文将潜在结果框架引入交叉设计，结合了因果推断与假设检验的功效分析，且协变量调整方法对您在纵向因果推断与效率理论方面的研究有直接参考价值。
- **关键技术**: `potential outcomes framework`, `carry-over effect`, `power trade-off analysis`, `covariate adjustment`, `one-sided hypothesis testing`
- **为什么对您有用**: 直接连接到您的主要兴趣“因果推断（纵向）”与“假设检验”，将潜在结果框架用于交叉设计遗留效应的识别与功效推导，同时协变量调整部分涉及效率提升，并在流行病学数据集上进行了应用。

### 7. [10.1093/biomtc/ujae019](https://doi.org/10.1093/biomtc/ujae019) — Case weighted power priors for hybrid control analyses with time-to-event data
- **作者**: Evan Kwiatkowski, Jiawen Zhu, Xiao Li, Herbert Pang, Grazyna Lieberman, Matthew A Psioda
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在 RCT 与外部对照数据融合的设定下，目标是处理未测量混杂导致的系统差异，实现稳健的混合控制分析。本文扩展了 power prior，为每个外部对照个体单独计算折扣权重，而非对整体施加单一折扣。权重通过 RCT 估计的生存分析参数后验分布导出的外部对照预测分布来确定，衡量个体与随机对照数据的兼容性。模型采用分段常数基线风险的比例风险回归，并在非小细胞肺癌真实数据上进行了验证。仿真和实证表明，当外部对照与 RCT 人群存在不兼容时，该方法能提供稳健推断。对您有用：其处理外部数据未测量混杂的个体级折扣思路，可为因果推断中的数据融合与可移植性研究提供启发，且 NSCLC 数据集对流行病学应用有参考价值。
- **关键技术**: `power prior`, `Bayesian borrowing`, `hybrid control`, `proportional hazards model`, `predictive compatibility weighting`, `time-to-event analysis`
- **为什么对您有用**: 涉及因果推断中数据融合与未测量混杂的调整思路（个体级折扣权重），并提供非小细胞肺癌真实数据集，对流行病学应用与因果推断可移植性研究有参考价值。

### 8. [10.1093/biomtc/ujae033](https://doi.org/10.1093/biomtc/ujae033) — Identifying temporal pathways using biomarkers in the presence of latent non-Gaussian components
- **作者**: Shanghong Xie, Donglin Zeng, Yuanjia Wang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在纵向时间序列数据中，目标是识别网络节点间的时序路径（temporal pathways），设定中允许存在潜在的未观测非高斯混杂（如伪影、遗传风险等）。方法首先利用独立成分分析（ICA）提取并剥离潜在的非高斯成分，随后基于残差通过矩估计法（method of moments）分别估计同期网络与时序网络。理论部分证明了在非高斯假设下时序与同期网络的可识别性，并给出了网络估计量的渐近性质。模拟与ADHD脑影像生物标志物应用表明，该方法能有效区分时序与同期关系，发现时序边跨脑区而同期边多为同区双侧连接。对您有用：该文将非高斯性作为识别工具解决纵向因果网络的可识别性问题，其 identification 思路和渐近理论对 longitudinal causal inference 和流行病学应用有直接参考价值。
- **关键技术**: `Independent Component Analysis (ICA)`, `method of moments`, `temporal network identification`, `latent non-Gaussian components`, `asymptotic properties`
- **为什么对您有用**: 直接关联 primary interest 中的 longitudinal causal inference 和 identification，利用非高斯性实现潜在混杂下的因果图可识别性；同时涉及 secondary interest 中的流行病学数据应用（ADHD脑区生物标志物）。

### 9. [10.1093/biomtc/ujae047](https://doi.org/10.1093/biomtc/ujae047) — Sequential covariate-adjusted randomization via hierarchically minimizing Mahalanobis distance and marginal imbalance
- **作者**: Haoyu Yang, Yichen Qin, Yang Li, Feifang Hu
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究比较实验中逐个入组（sequential）的协变量均衡随机化问题，目标是在无法等待配对/分组时，对当前个体即时分配处理并最小化协变量失衡与边际失衡。作者提出将协变量失衡（用新定义的 modified Mahalanobis distance 度量）与边际失衡（两组样本量之差）分层处理，按显式优先级依次最小化。理论上证明了失衡度量的收敛性以及后续处理效应估计的渐近性质；模拟与真实数据表明该方法在保持边际均衡的同时达到更优的协变量均衡。对您而言，该文虽属实验设计而非观察性因果推断，但其对 Mahalanobis 距离的修正与分层优化思路，以及处理效应估计的理论保证，可为 RCT 场景下的因果推断提供随机化方案参考。
- **关键技术**: `modified Mahalanobis distance`, `sequential covariate-adjusted randomization`, `hierarchical imbalance minimization`, `marginal balance constraint`, `treatment effect asymptotic theory`
- **为什么对您有用**: 与您 causal inference 中实验设计/随机化方向间接相关，分层最小化失衡的思路和处理效应估计的理论保证可作 RCT 因果推断的随机化方案参考，但与您核心关注的 proximal CI / IV / mediation 距离较远。

### 10. [10.1093/biomtc/ujae054](https://doi.org/10.1093/biomtc/ujae054) — Incorporating nonparametric methods for estimating causal excursion effects in mobile health with zero-inflated count outcomes
- **作者**: Xueqing Liu, Tianchen Qian, Lauren Bell, Bibhas Chakraborty
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在移动健康微观随机化试验（MRT）的纵向设定下，本文针对零膨胀计数型近端结局，定义并识别了因果漂移效应。作者提出了结合非参数技术的估计方法，以处理零膨胀结构带来的非线性与异质性，避免了强参数假设。理论方面，建立了所提估计量的双向渐近性质，即在个体数与决策时间点数量同时增长下的收敛性与渐近正态性。模拟与 Drink Less 试验的实证分析验证了方法在有限样本下的表现。对您有用：直接关联您在纵向因果推断与半参数/非参数理论方面的兴趣，MRT中的因果漂移效应与proximal CI紧密相关，双向渐近性及非参数估计框架为处理复杂纵向因果estimand提供了可迁移的理论工具。
- **关键技术**: `causal excursion effect`, `micro-randomized trials`, `zero-inflated count outcomes`, `nonparametric estimation`, `bidirectional asymptotics`
- **为什么对您有用**: 直接关联您在纵向因果推断与半参数/非参数理论方面的核心兴趣；MRT中的因果漂移效应与proximal CI设定紧密相关，双向渐近性及非参数估计框架为处理复杂纵向因果estimand提供了可迁移的理论工具与实证参考。

### 11. [10.1093/biomtc/ujae025](https://doi.org/10.1093/biomtc/ujae025) — Confounder-dependent Bayesian mixture model: Characterizing heterogeneity of causal effects in air pollution epidemiology
- **作者**: Dafne Zorzetto, Falco J Bargagli-Stoffi, Antonio Canale, Francesca Dominici.
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在潜在结果框架下，目标是识别和刻画处理效应异质性，具体 estimand 为 group average treatment effect (GATE)，关键假设为混杂变量条件下的可忽略性。方法提出 Confounder-Dependent Bayesian Mixture Model (CDBMM)，利用 dependent Dirichlet process 对给定协变量和处理水平下的潜在结果分布进行贝叶斯非参数建模，以数据驱动方式识别具有相似 GATE 的互斥子群并在各子群内估计因果效应。该框架无需预先指定子群数目，通过后验推断同时完成聚类与效应估计，避免了参数化分组的强假设。模拟显示方法能有效恢复异质性结构；应用于德州 Medicare 数据发现 PM2.5 对死亡率的因果效应在六个互斥子群间存在显著异质性。对您有用：该文将 dependent Dirichlet process 引入 GATE 异质性刻画，连接了您 primary interest 中的因果推断（处理效应异质性/子群识别）与半参数非参数理论，同时提供了流行病学真实数据（Medicare claims）的分析范例。
- **关键技术**: `dependent Dirichlet process`, `group average treatment effect`, `Bayesian nonparametric mixture`, `potential outcomes framework`, `treatment effect heterogeneity`, `posterior clustering inference`
- **为什么对您有用**: 连接您 primary interest 中的因果推断（GATE/异质性识别）与半参数非参数理论（dependent Dirichlet process），同时提供流行病学真实数据集（Medicare claims）的应用范例，贝叶斯非参数聚类思路可迁移至其他因果异质性场景。

### 12. [10.1093/biomtc/ujae028](https://doi.org/10.1093/biomtc/ujae028) — Causal inference for time-to-event data with a cured subpopulation
- **作者**: Yi Wang, Yuhao Deng, Xiao-Hua Zhou
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在存在治愈亚群的删失生存数据设定下，本文基于主分层（principal stratification）定义了 always-uncured 亚组的两个因果 estimand：timewise risk difference 与 mean survival time difference。由于删失导致潜在治愈状态不可观测，作者引入潜在治愈状态的替代变量（substitutional variable），在可忽略处理分配假设下证明了这两个 estimand 的非参数可识别性。估计方面，基于 mixture cure model 构建了相应的估计量。实证部分将该方法应用于比较不同移植类型对急性淋巴细胞白血病无白血病生存率的因果效应。对您有用：主分层框架下的替代变量识别策略与您关注的 causal inference (identification) 直接相关，且流行病学队列数据应用可提供方法迁移参考。
- **关键技术**: `principal stratification`, `substitutional variable identification`, `mixture cure model`, `time-to-event analysis`, `ignorable treatment assignment`
- **为什么对您有用**: 主分层框架下的替代变量识别策略直接契合您在 causal inference (identification) 方向的核心兴趣，同时其流行病学应用场景与您 secondary interest 中的 epidemiology (causal inference) 高度吻合。

### 13. [10.1093/biomtc/ujae032](https://doi.org/10.1093/biomtc/ujae032) — Direct and indirect treatment effects in the presence of semicompeting risks
- **作者**: Yuhao Deng, Yi Wang, Xiao-Hua Zhou
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在完全随机化实验的半竞争风险（semicompeting risks）设定下，目标是分解处理对终点事件（如死亡）的总效应为直接效应与经非终点事件（如疾病进展）的间接效应。作者提出两种分解策略：分别通过调整非终点事件的患病率（prevalence）与风险率（hazard）实现识别，两者对 cross-world 量需要不同的可识别性假设。在识别性基础上，建立了反事实累积发生率及分解处理效应估计量的渐近性质。模拟与两个真实数据应用揭示了两种分解的微妙差异。对您有用：该工作将 mediation 分析拓展至半竞争风险框架，直接关联您 primary interest 中的因果推断（mediation）与半参数理论（渐近性质），且流行病学应用数据集具有参考价值。
- **关键技术**: `semicompeting risks mediation`, `prevalence-based decomposition`, `hazard-based decomposition`, `cross-world identifiability assumptions`, `counterfactual cumulative incidence`, `asymptotic normality`
- **为什么对您有用**: 直接关联您 primary interest 中的因果推断（mediation）与半参数理论（渐近性质）；半竞争风险设定下的 cross-world 识别假设讨论对您思考 mediation 敏感性分析有启发，流行病学真实数据集也可作为应用素材。

### 14. [10.1093/biomtc/ujae045](https://doi.org/10.1093/biomtc/ujae045) — Doubly robust estimation and sensitivity analysis for marginal structural quantile models
- **作者**: Chao Cheng, Liangyuan Hu, Fan Li
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在纵向时间变化处理设定下，本文研究边际结构分位数模型（MSQM）的因果效应估计，关键假设为序列可忽略性。在半参数框架下推导了 MSQM 的有效影响函数（EIF），并据此提出新的双重稳健（DR）估计量；该估计量在处理分配模型或潜在结果分布模型之一正确时一致，两者均正确时达到半参数有效。计算上，通过求解平滑估计方程（smoothed estimating equation）来实现点估计与方差估计的高效数值计算。此外，提出混杂函数（confounding function）方法，对违反序列可忽略性（即存在未测量基线和时变混杂）的情形进行敏感性分析。理论与模拟验证了 DR 估计量的有效性与鲁棒性，并在流行病学电子病历数据中实证；对您有用之处在于，它完整展示了纵向因果推断中分位数效应的 EIF 推导与 DR 构造，以及时变混杂敏感性分析的具体操作，直接契合您在 longitudinal causal inference 和 sensitivity analysis 上的核心兴趣。
- **关键技术**: `marginal structural quantile model`, `efficient influence function`, `doubly robust estimation`, `smoothed estimating equation`, `confounding function sensitivity analysis`
- **为什么对您有用**: 直接契合您在 longitudinal causal inference 和 sensitivity analysis 上的核心兴趣；完整展示了分位数因果效应的 EIF 推导与 DR 构造，且其时变混杂敏感性分析框架可直接迁移至其他纵向因果设定。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1093/biomtc/ujae031](https://doi.org/10.1093/biomtc/ujae031) — High-dimensional covariate-augmented overdispersed poisson factor model
- **作者**: Wei Liu, Qingzhi Zhong
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维计数数据设定下，现有 Poisson 因子模型常忽略可观测协变量的解释力，本文提出协变量增强的过度散布 Poisson 因子模型，目标是在响应变量与协变量维度随样本量发散时联合估计因子结构与高维系数矩阵。文中给出一组可识别性条件以保证计算可识别性，并对高维系数矩阵施加低秩约束以刻画响应变量与协变量间的相互依赖。针对非线性、双高维潜变量矩阵及低秩约束带来的计算挑战，提出结合 Laplace 与 Taylor 近似的变分估计方案。此外，提出基于奇异值比值的准则来确定因子数与系数矩阵的秩。模拟与 CITE-seq 数据应用表明该方法在估计精度与计算效率上优于现有方法，并提供了 R 包 COAP。对您有用：该文的高维低秩因子模型设定与奇异值比值定阶直接关联高维统计与 RMT 兴趣，其变分计算方案对统计计算与算法设计有参考价值。
- **关键技术**: `overdispersed Poisson factor model`, `low-rank coefficient matrix constraint`, `variational estimation`, `Laplace approximation`, `singular value ratio criterion`
- **为什么对您有用**: 直接关联您的高维统计与 RMT 兴趣（低秩矩阵约束与奇异值比值定阶），其结合 Laplace 与 Taylor 近似的变分计算方案对您的统计计算与算法兴趣有直接参考价值。

## 非参数 / 半参数  *(nonparam_semipara, 5 篇)*

### 1. [10.1093/biomtc/ujae035](https://doi.org/10.1093/biomtc/ujae035) — Efficient data integration under prior probability shift
- **作者**: Ming-Yueh Huang, Jing Qin, Chiung-Yu Huang
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在 prior probability shift（P(Y) 跨数据集变化但 P(X|Y) 不变）设定下，本文研究如何高效整合多源数据以估计目标总体参数。提出一种可同时处理离散与连续结局的估计算法，通过 semiparametric likelihood 最大化实现多源信息的高效组合，突破了现有方法仅适用于离散结局的限制。对高维协变量引入 adaptive LASSO 惩罚进行变量选择，所得估计量具有 oracle 性质。进一步，将零假设条件密度嵌入 Neyman's smooth alternatives，构造了 semiparametric likelihood ratio test 来检验 prior probability shift 假设的合理性。模拟与真实数据验证了方法的有效性。对您有用：该文将 semiparametric likelihood 与 Neyman smooth test 结合做假设检验的思路，以及高维 adaptive LASSO 下 oracle efficiency 的结果，可直接迁移到您关注的 semiparametric efficiency 与 hypothesis testing 交叉方向。
- **关键技术**: `prior probability shift`, `semiparametric likelihood ratio test`, `Neyman's smooth alternatives`, `adaptive LASSO`, `oracle property`, `multi-source data integration`
- **为什么对您有用**: 直接关联您 primary interests 中的 semiparametric theory（semiparametric likelihood 构造）、hypothesis testing（Neyman smooth test 检验 shift 假设）与 high-dimensional statistics（adaptive LASSO oracle 估计）；检验 shift 假设的框架也可迁移到因果推断中外部有效性/transportability 的设定。

### 2. [10.1093/biomtc/ujae024](https://doi.org/10.1093/biomtc/ujae024) — Deep partially linear cox model for current status data
- **作者**: Qiang Wu, Xingwei Tong, Xingqiu Zhao
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 6/10 · novelty: `new_theory`
- **摘要**: 在 current status data（当前状态数据）的生存分析设定下，本文提出深度部分线性 Cox 模型，以克服高维协变量的维数灾难并估计处理效应。方法上，采用深度神经网络（DNN）拟合非线性协变量效应，并用单调样条逼近基准累积风险函数，通过最大似然估计（MLE）求解。理论上，建立了非参数成分 MLE 的收敛速率，并证明有限维处理效应估计量具有 $\sqrt{n}$-相合性、渐近正态性，且达到半参数有效界。该工作为 DNN 在生存分析中的半参数效率理论提供了严格证明，对您研究 semiparametric efficiency bounds 与 DNN 结合的理论，以及因果推断中处理效应的半参数有效估计有直接参考价值。
- **关键技术**: `deep partially linear Cox model`, `current status data`, `monotone splines`, `semiparametric efficiency`, `deep neural networks`, `maximum likelihood estimation`
- **为什么对您有用**: 直接涉及您 primary interest 中的 semiparametric efficiency bounds 和 semiparametric theory，展示了 DNN 逼近下有限维参数如何达到半参数有效界，对因果推断中处理效应的半参数有效估计有方法迁移价值。

### 3. [10.1093/biomtc/ujae049](https://doi.org/10.1093/biomtc/ujae049) — Robustness of response-adaptive randomization
- **作者**: Xiaoqing Ye, Feifang Hu, Wei Ma
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 4/10 · novelty: `weaker_assumption`
- **摘要**: 在响应自适应随机化（DBCD）框架下，本文研究设计模型与分析模型双重误设时处理效应估计的稳健性。作者首先证明，即使响应的真实分布偏离设计模型，分配比例仍保持一致性与渐近正态性。针对处理效应的推断，文章考察了差均法、ANCOVA I 与 ANCOVA II 三种线性回归模型，允许其任意误设而不反映真实数据生成过程。在此弱假设下，推导出三种模型下处理效应估计量的一致性与渐近正态性。渐近方差对比表明，包含协变量-处理交互项的 ANCOVA II 模型具有最高渐近效率。对您有用：该文在误设模型下对协变量调整估计量渐近效率的严格推导，可为效率理论中协变量-处理交互项如何收紧半参数有效界提供实验设计视角的参考。
- **关键技术**: `response-adaptive randomization`, `model misspecification`, `asymptotic normality`, `ANCOVA`, `treatment effect estimation`
- **为什么对您有用**: 论文在放松模型正确指定假设下推导处理效应估计量的渐近性质与效率排序，与您在效率理论和因果推断（处理效应估计）方面的兴趣直接相关，可加深对协变量调整及交互项如何提升渐近效率的理解。

### 4. [10.1093/biomtc/ujae029](https://doi.org/10.1093/biomtc/ujae029) — Addressing age measurement errors in fish growth estimation from length-stratified samples
- **作者**: Nan Zheng, Atefeh Kheirollahi, Yildiz Yilmaz
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在长度分层年龄采样（LSAS）的两相响应选择性抽样设定下，目标是校正年龄测量误差（ME）以准确估计鱼类生长模型参数；假设年龄 ME 为结构式误差且真实年龄分布服从 continuation ratio-logit 模型。方法结合经验比例似然（empirical proportion likelihood）处理 LSAS 的选择偏差，并用结构式变量误差（structural errors-in-variables）框架校正年龄 ME；对年龄和长度分布采用离散化策略以提升计算效率。理论上给出了参数估计的不确定性度量及标准化残差用于模型验证，但未推导 influence function 或 semiparametric efficiency bound。模拟表明即使 ME 很小，忽略它也会导致生长参数显著偏倚，而所提方法在各 ME 水平下均表现良好。对您而言，该文在两相抽样下联合处理测量误差与选择偏差的思路可迁移到流行病学队列/横断面研究中的纠偏设计，但理论深度有限，semiparametric efficiency 方面无新贡献。
- **关键技术**: `empirical proportion likelihood`, `structural errors-in-variables`, `continuation ratio-logit model`, `two-phase response-selective sampling`, `discretization for computational efficiency`
- **为什么对您有用**: 两相抽样+测量误差的联合校正思路可迁移到流行病学应用中的纠偏设计（secondary interest: epidemiology），但本文未涉及 influence function 或 efficiency bound 理论，对 primary interest 的 semiparametric efficiency 理论贡献有限。

### 5. [10.1093/biomtc/ujae017](https://doi.org/10.1093/biomtc/ujae017) — Estimating the size of a closed population by modeling latent and observed heterogeneity
- **作者**: Francesco Bartolucci, Antonio Forcina
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在封闭总体标记-重捕设定下，将经验似然（EL）扩展至允许序列依赖的潜类别模型，目标是直接估计总体规模而非累加条件协变量配置的估计。核心方法上，作者提出Fisher-scoring算法实现极大似然估计，并引入比传统EL更高效的替代方法来估计协变量的非参数成分。理论方面，证明了协变量非参数分布与从未被捕获概率之间的映射是一一对应且严格单调的，并给出了渐近结果及总体规模的轮廓似然置信区间构建程序。模拟与实证表明，在估计总体漏报时，该方法比条件极大似然估计具有显著更高的效率，尤其在样本量有限时优势明显。对您有用：本文对非参数成分的效率提升与轮廓经验似然渐近理论，直接关联您对半参数/非参数理论与效率理论的兴趣；其总体规模估计框架也可迁移至流行病学中的隐藏人群估计问题。
- **关键技术**: `empirical likelihood`, `latent class models`, `profile likelihood`, `Fisher-scoring algorithm`, `semiparametric efficiency`
- **为什么对您有用**: 本文处理带非参数协变量分布的经验似然估计并证明其相对条件MLE的效率优势，直接关联您对半参数/非参数理论与效率理论的兴趣；标记-重捕框架亦常用于流行病学隐藏人群估计。

## 数理统计 / 假设检验  *(hypothesis_testing, 5 篇)*

### 1. [10.1093/biomtc/ujae051](https://doi.org/10.1093/biomtc/ujae051) — On exact randomization-based covariate-adjusted confidence intervals
- **作者**: Jacob Fiksel
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在 Fisher 随机化检验（FRT）框架下，针对小样本随机化实验，目标是构建协变量调整后处理效应的精确置信区间，避免传统检验反演的巨大计算开销。本文扩展了 Zhu & Liu 的差值统计量结果，推导出基于协变量调整均值差（ANCOVA）统计量的随机化置信区间闭式解。作者提供了一个可基于观测数据检验的充分条件，保证该闭式区间具有正确的覆盖概率。该方法利用代数求解直接绕过了逐点计算精确 P 值的反演步骤，将计算时间降至与单次精确 P 值计算相当。模拟表明该区间对非正态结果稳健，实证分析展示了其在 I 期临床试验数据中的应用。对您有用：该文将随机化推断的计算复杂度大幅降低，直接契合您对假设检验与统计计算（数值算法）的交叉兴趣，且为小样本 RCT 的因果效应推断提供了精确且快速的协变量调整工具。
- **关键技术**: `Fisher randomization test`, `exact confidence interval`, `test inversion`, `covariate-adjusted difference-in-means`, `closed-form solution`, `randomization inference`
- **为什么对您有用**: 直接契合您在因果推断（随机化实验的精确推断）与假设检验的交叉兴趣；同时闭式解消除了检验反演的计算瓶颈，对您的统计计算（数值算法）兴趣亦有启发。

### 2. [10.1093/biomtc/ujae036](https://doi.org/10.1093/biomtc/ujae036) — Testing conditional quantile independence with functional covariate
- **作者**: Yongzhen Feng, Jie Li, Xiaojun Song
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 本文研究标量响应与函数型协变量在连续分位数水平上的非参数条件独立性检验问题，目标是在 mild regularity 假设下建立有效的检验程序。构建基于经验过程的 Cramér-von Mises 型检验统计量，通过对函数型协变量进行随机投影来索引经验过程，从而在投影假设（与原假设几乎必然等价）下有效规避维数灾难。推导了该统计量的渐近零分布，并证明了其能检测以参数率 n^{-1/2} 收敛到原假设的局部替代假设。采用 multiplier bootstrap 方法估计临界值，保证计算的可行性。理论上证明了全局与局部功效性质，模拟与 EEG 数据分析验证了有限样本表现。对您有用：该文将随机投影与经验过程结合处理函数型数据的假设检验，其局部替代假设的 n^{-1/2} 检验率与 multiplier bootstrap 计算方案，对您在非参数假设检验与统计计算方面的研究有直接参考价值。
- **关键技术**: `conditional quantile independence`, `Cramer-von Mises test`, `random projection`, `empirical process`, `multiplier bootstrap`, `local alternatives at parametric rate`
- **为什么对您有用**: 直接契合您在数学统计（假设检验）与非参数理论方面的兴趣；其利用随机投影规避函数数据维数灾难、以及达到 n^{-1/2} 局部检验率的技巧，对处理高维/无穷维条件独立性检验具有方法论迁移价值。

### 3. [10.1093/biomtc/ujae021](https://doi.org/10.1093/biomtc/ujae021) — High-dimensional multisubject time series transition matrix inference with application to brain connectivity analysis
- **作者**: Xiang Lyu, Jian Kang, Lexin Li
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究高维向量自回归(VAR)模型在含测量误差与多主体设定下的转移矩阵推断问题，目标是检验主体条件变化对有效连接模式的影响。提出的同时检验程序包含三个核心组件：处理测量误差的改进EM算法、基于滞后自协方差偏差校正估计量并给定协变量的张量回归检验统计量，以及阈值化的同时检验。理论上证明了改进EM估计量的均匀一致性，且后续检验实现一致的错误发现率(FDR)控制与渐近功效1。该方法在模拟与任务态fMRI脑连接数据中验证了有效性。对您有用：该工作将高维同时检验与张量回归、偏差校正结合，为您在高维时间序列/图模型中的假设检验与统计计算研究提供了直接的方法论参考。
- **关键技术**: `high-dimensional VAR`, `simultaneous testing`, `modified EM algorithm`, `tensor regression`, `bias-corrected estimator`, `false discovery rate control`
- **为什么对您有用**: 直接契合您在“假设检验”和“高维统计”方向的兴趣，其结合偏差校正与张量回归的高维同时检验框架，以及处理测量误差的EM计算方案，对研究高维图/时间序列推断有方法迁移价值。

### 4. [10.1093/biomtc/ujae056](https://doi.org/10.1093/biomtc/ujae056) — Efficient testing of the biomarker positive and negative subgroups in a biomarker-stratified trial
- **作者**: Lang Li, Anastasia Ivanova
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在生物标志物分层随机试验中，目标是同时检验标志物阳性与阴性亚组的处理效应，核心假设为阳性组效应不低于阴性组（isotonic assumption）。作者利用该序约束构建了针对两组处理效应的联合检验方法，避免了传统方法仅因总体有效而忽略阴性组无效的缺陷。通过整合序约束信息，该检验显著降低了所需样本量，核心理论工具涉及序约束下的假设检验与功效分析。理论与模拟表明，当阳性亚组比例小于0.5时样本量缩减尤为显著。对您有用：直接关联您对假设检验的兴趣，展示了序约束如何在因果推断亚组分析中提升检验功效，且方法可迁移至流行病学试验设计。
- **关键技术**: `isotonic assumption`, `order-restricted hypothesis testing`, `subgroup analysis`, `sample size calculation`, `biomarker-stratified trial`
- **为什么对您有用**: 直接关联您对数学统计（假设检验）和因果推断（亚组处理效应）的兴趣；展示了序约束假设如何放松独立检验要求并提升检验功效，方法可迁移至流行病学RCT设计。

### 5. [10.1093/biomtc/ujae022](https://doi.org/10.1093/biomtc/ujae022) — Flagging unusual clusters based on linear mixed models using weighted and self-calibrated predictors
- **作者**: Charles E McCulloch, John M Neuhaus, Ross D Boylan
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在分层线性混合模型设定下，研究如何基于随机效应预测值识别或“标记”极端聚类（如表现不佳的医院），目标是控制错误标记率。作者通过理论推导与数值计算证明，基于传统 BLUP 或固定效应预测值的标记规则表现极差：错误标记率要么不可接受地高（极限下趋近0.5），要么过于保守（远低于0.05导致正确标记率极低）。为此，提出了一种新的“自校准”加权预测标记方法，无需繁琐调整即可精确控制错误标记率。新方法在保证错误标记率受控的前提下，显著提高了正确标记率，并在儿童哮喘住院时长数据上进行了实证展示。对您而言，该文将随机效应标记问题转化为假设检验中的错误率控制问题，其自校准思路在纵向/聚类因果推断或流行病学应用中的异常值筛查具有参考价值。
- **关键技术**: `linear mixed models`, `best linear unbiased predictor (BLUP)`, `outlier flagging`, `error rate control`, `self-calibrated predictor`
- **为什么对您有用**: 将聚类标记问题转化为假设检验中的错误率控制问题，其自校准思路对您在流行病学队列或纵向因果推断中处理异常聚类/单位有方法迁移价值。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1093/biomtc/ujae057](https://doi.org/10.1093/biomtc/ujae057) — A Bayesian convolutional neural network-based generalized linear model
- **作者**: Yeseul Jeon, Won Chang, Seonghyun Jeong, Sanghoon Han, Jaewoo Park
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文在广义线性模型（GLM）框架中嵌入 CNN，提出 Bayesian CNN-GLM：用 MC dropout 从 CNN 最后一层隐节点提取特征作为 GLM 协变量，再对多次 dropout 实现拟合集成 GLM 以传播特征提取不确定性。设定为图像/空间高维相关输入加向量协变量的回归，目标是在保持预测精度的同时获得可解释的回归系数推断与不确定性量化。核心计算策略是 MC dropout 近似后验 + ensemble GLM，避免对整个 CNN 做全贝叶斯推断，计算代价较低。理论方面未给出收敛率或效率界，主要贡献在方法整合与计算流程。实证覆盖疟疾发病率、脑肿瘤影像和 fMRI 三个流行病学/生物学数据集。对您而言，该文在统计计算（MC dropout 集成算法）和流行病学数据应用上有参考价值，但缺乏 semiparametric efficiency 或 influence function 层面的理论深度。
- **关键技术**: `MC dropout approximate posterior`, `CNN feature extraction in GLM`, `ensemble Bayesian GLM`, `uncertainty quantification via dropout`, `image regression with spatial covariates`
- **为什么对您有用**: 统计计算方面（MC dropout 集成算法的数值实现）与流行病学数据集（疟疾发病率）对您的 secondary interests 有直接参考；但未触及 semiparametric efficiency 或 causal inference，理论收益有限。

### 2. [10.1093/biomtc/ujae030](https://doi.org/10.1093/biomtc/ujae030) — Topical hidden genome: discovering latent cancer mutational topics using a Bayesian multilevel context-learning approach
- **作者**: Saptarshi Chakraborty, Zoe Guan, Colin B Begg, Ronglai Shen
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在超稀疏、超高维全基因组体细胞突变数据设定下，目标是推断极罕见突变与癌症类型的关联。作者提出贝叶斯多层级 multilogistic 'hidden genome' 模型，利用层级结构将极罕见突变的信息凝聚为突变上下文的 meta-features。为解决突变上下文的高维、相关及不可解释性问题，引入计算语言学中的 topic model 进行降维，生成可解释且去相关的 meta-feature topics。计算上，设计了高效的 MCMC 算法实现大规模全贝叶斯推断，可处理数千万变异和数千肿瘤，突破了现有高维多类回归方法的可扩展性瓶颈。在 PCAWG 数据集上的应用揭示了与紫外线暴露、衰老等相关的突变主题，交叉验证显示其预测性能可与随机森林和深度学习竞争。对您可能有用：该文处理超稀疏高维数据的贝叶斯降维思路及大规模 MCMC 计算方案，可为您的统计计算兴趣提供参考，但与半参数效率/RMT/因果推断距离较远。
- **关键技术**: `Bayesian multilevel model`, `topic model`, `MCMC algorithm`, `high-dimensional sparse data`, `multilogistic regression`
- **为什么对您有用**: 该文处理超稀疏高维数据的降维策略及大规模 MCMC 计算方案与您的统计计算兴趣相关，但核心方法（贝叶斯 topic model）与您主攻的半参数/效率理论/RMT 距离较远，属于外围参考。

## 流行病学  *(epidemiology, 4 篇)*

### 1. [10.1093/biomtc/ujae038](https://doi.org/10.1093/biomtc/ujae038) — Bayesian meta-analysis of penetrance for cancer risk
- **作者**: Thanthirige Lakshika M Ruberu, Danielle Braun, Giovanni Parmigiani, Swati Biswas
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 3/10 · novelty: `application`
- **摘要**: 在多基因面板测试背景下，目标是估计携带特定基因突变的年龄特异性癌症发病风险（penetrance），核心挑战是整合报告不同风险度量（penetrance、相对风险、优势比）的异质性研究。本文提出基于贝叶斯分层随机效应模型的荟萃分析方法，统一整合不同风险度量并量化其不确定性。通过 MCMC 算法估计参数后验分布，进而获得 penetrance 的估计与可信区间。模拟研究（基于 ATM 和 PALB2 基因）表明，该方法在覆盖概率和均方误差上显著优于现有方法，并最终应用于 ATM 基因乳腺癌真实数据。对您而言，该文提供了一个流行病学中整合异质性风险度量的贝叶斯层级建模案例，但方法学上缺乏半参数效率或因果推断的理论深度。
- **关键技术**: `Bayesian hierarchical random-effects model`, `Markov chain Monte Carlo (MCMC)`, `meta-analysis of heterogeneous risk measures`, `penetrance estimation`
- **为什么对您有用**: 属于流行病学应用，涉及不同风险度量（OR/RR/penetrance）的整合问题；但方法为纯贝叶斯层级模型，缺乏您关注的半参数效率或因果推断理论，仅作应用数据集参考。

### 2. [10.1093/biomtc/ujae037](https://doi.org/10.1093/biomtc/ujae037) — Regression models for average hazard
- **作者**: Hajime Uno, Lu Tian, Miki Horiguchi, Satoshi Hattori, Kenneth L Kehl
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在时间-事件数据设定下，针对传统Cox模型风险比在非比例风险等情况下的局限，本文提出基于截断时间τ的带生存权重平均风险（AH）回归方法，目标estimand为特定时间窗内的无删失人时发病率。作者考察了三种删失机制下的AH回归：独立删失、组别特异删失与协变量依赖删失。核心机制上，AH回归与稳健Poisson回归紧密相关，但在存在删失时通过引入生存权重修正而更为稳健。该方法允许在调整协变量的同时，以绝对差异和相对比率两种尺度总结处理效应，从而提升效应量的可解释性。理论部分给出了估计量的渐近正态性与方差估计，实证分析验证了其在临床终点数据上的表现。对您而言，若在流行病学队列或因果推断的生存数据应用中需避开PH假设并关注绝对风险差，此方法可作为Cox模型的实用替代方案。
- **关键技术**: `average hazard with survival weight`, `robust Poisson regression`, `covariate-dependent censoring`, `absolute risk difference`, `time-to-event outcomes`
- **为什么对您有用**: 涉及流行病学和因果推断中常见的生存数据与处理效应估计，提供了一种避开比例风险假设的回归替代方案，对处理时间-事件数据的因果效应汇报有应用参考价值。

### 3. [10.1093/biomtc/ujae034](https://doi.org/10.1093/biomtc/ujae034) — Data science for infectious disease data analytics: an introduction with R, by Lily Wang, CRC Press, 2022 ISBN-13: 978-1032187426, https://www.routledge.com/Data-Science-for-Infectious-Disease-Data-Analytics-An-Introduction-with-R/Wang/p/book/9781032187426
- **作者**: Gillian Cheng, Andrei R Akhmetzhanov
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 2/10 · novelty: `minor`
- **摘要**: 本文是对 Lily Wang 所著《Data science for infectious disease data analytics: an introduction with R》的书评，概述了该书在传染病数据分析与 R 语言实现方面的内容设定。书评指出该书侧重于传染病数据（如传播动力学、监测数据）的基础处理与可视化，属于入门级数据科学教材。原书涵盖基本的流行病学模型与 R 代码实现，但未涉及高阶因果推断、半参数理论或高维统计方法。作为书评，本文无任何新理论或新方法贡献，仅提供对原书内容与适用人群的评价。对您而言，该材料方法学新颖度极低，与您关注的效率理论、proximal CI 或高维推断完全无关；仅在您需要寻找流行病学入门级 R 代码或基础教学案例时有微弱参考价值。
- **关键技术**: `infectious disease modeling`, `R programming`, `epidemiological data visualization`
- **为什么对您有用**: 虽然流行病学是您的次要兴趣，但此书评及原书仅为入门级 R 数据分析，缺乏您关注的深层因果推断方法或复杂真实数据集，对理论或方法研究的参考价值极低。

### 4. [10.1093/biomtc/ujae048](https://doi.org/10.1093/biomtc/ujae048) — A Bayesian semi-parametric model for learning biomarker trajectories and changepoints in the preclinical phase of Alzheimer’s disease
- **作者**: Kunbo Wang, William Hua, MeiCheng Wang, Yanxun Xu
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文在阿尔茨海默病（AD）临床前期的异质人群中，目标是估计生物标志物的纵向轨迹及其相对于症状发作的变点（changepoint），该变点受左截断与右删失影响。提出一种贝叶斯半参数框架，联合建模纵向轨迹与变点，利用半参数先验刻画轨迹的灵活特征。与假设所有人最终发病的传统方法不同，该模型引入 cure rate 机制，允许部分个体永远不发生轻度认知障碍（MCI）。通过贝叶斯后验推断处理变点的左截断与右删失，避免了频率学派下复杂的影响函数推导。模拟研究验证了方法在有限样本下的表现，并在 BIOCARD 队列的 ptau181 数据上展示了临床实用性。对您而言，该文提供了流行病学队列的纵向删失数据集与半参数变点建模思路，可迁移至您关注的纵向因果推断中处理依从性或删失机制的设定。
- **关键技术**: `Bayesian semiparametric framework`, `changepoint model`, `left truncation and right censoring`, `cure rate model`, `longitudinal trajectory modeling`
- **为什么对您有用**: 属于流行病学应用，提供 BIOCARD 真实队列数据集及左截断/右删失下的半参数变点建模方法，对您在纵向因果推断中处理异质性与删失机制有方法迁移价值。

## 其他  *(other, 2 篇)*

### 1. [10.1093/biomtc/ujae026](https://doi.org/10.1093/biomtc/ujae026) — Well-spread samples with dynamic sample sizes
- **作者**: Blair Robertson, Chris Price, Marco Reale
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究空间抽样设计问题，目标是在任意辅助空间上生成分布均匀（well-spread）的样本，以提升具有空间趋势的总体的参数估计精度。提出一种仅依赖总体单元间距离度量的新抽样方法，支持动态样本量与主抽样（master sampling）框架。数值实验表明该方法在样本空间覆盖均匀性上优于现有设计。实证部分利用巴西亚马逊地区的地上生物量等多重响应变量展示了多目的调查（multipurpose surveys）的应用。该方法学创新属于新抽样设计，但对您的主要研究方向（因果推断、半参数效率、高维理论）关联较弱，仅在空间数据抽样算法设计上有边缘参考价值。
- **关键技术**: `spatially balanced design`, `distance-based sampling`, `master sampling`, `multipurpose survey`
- **为什么对您有用**: 本文主要关注空间抽样设计，与您核心的因果推断、半参数效率及高维理论兴趣关联较弱，仅在统计计算（抽样算法）层面有极边缘的参考价值。

### 2. [10.1093/biomtc/ujae053](https://doi.org/10.1093/biomtc/ujae053) — Introduction to statistical modelling and inference by Murray Aitkin, CRC Press, 2023, ISBN: 978-1032105710, https://www.routledge.com/Introduction-to-Statistical-Modelling-and-Inference/Aitkin/p/book/9781032105710
- **作者**: Chuhsing Kate Hsiao
- **期刊/来源**: Biometrics
- **分类**: vol 80 · issue 2
- 相关性 0/10 · novelty: `survey`
- **摘要**: 本文是 Murray Aitkin 所著《Introduction to Statistical Modelling and Inference》（CRC Press, 2023）的书评，发表于 Biometrics。该书面向入门读者，涵盖经典统计建模与推断的基本概念，包括似然、贝叶斯推断、广义线性模型等标准主题。书评作者简要介绍了各章节内容安排与教学适用性，未涉及任何新的理论或方法贡献。作为入门教材的评介，其内容深度远低于您所关注的半参数效率界、高维推断或因果识别等前沿方向。对您的研究几乎没有直接参考价值。
- **关键技术**: `likelihood inference`, `Bayesian modelling`, `generalized linear models`
- **为什么对您有用**: 与您的 primary interests（因果推断、高维 RMT、半参数效率理论等）无实质重叠；入门教材书评不提供新理论、sharper rate 或放松假设的洞见。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

