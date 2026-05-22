# Biostatistics — Vol 24  Issue 4  ·  2026-05-21

- 共 14 篇 · Biostatistics

## 因果推断  *(causal_inference, 6 篇)*

### 1. [10.1093/biostatistics/kxac037](https://doi.org/10.1093/biostatistics/kxac037) — Cross-direct effects in settings with two mediators
- **作者**: Erin E Gabriel, Arvid Sjölander, Dean Follmann, Michael C Sachs
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 4 · pp 1017-1030
- 相关性 9/10 · novelty: `new_theory`
- **摘要**: 在双中介设定下，本文研究跨越控制类型的直接效应（cross-CDE / -NDE），即固定一个中介为常数、另一中介取自然水平时的因果 estimand。作者引入五种新的 cross-direct estimands，分别覆盖中介间有序列影响与无影响两种场景。在无残余混杂的观察性设定下，对任意类型的干预、结局与中介变量，给出非参数识别表达式。在存在结局-中介残余混杂的随机化设定下，对所有变量均为二元的情形，推导出紧符号界（tight symbolic bounds）。以 SARS-CoV-2 疫苗免疫反应为例说明 estimand 的实际动机。对您有用：直接推进您在因果中介分析（特别是多中介、cross-world estimand）方面的理论兴趣，且提供的符号界方法可迁移到敏感性分析框架。
- **关键技术**: `cross-controlled direct effect`, `cross-natural direct effect`, `multiple mediation`, `nonparametric identification`, `tight symbolic bounds`, `sensitivity analysis`
- **为什么对您有用**: 直接推进您在因果中介分析（特别是多中介、cross-world estimand）方面的理论兴趣，且提供的符号界方法可迁移到敏感性分析框架。

### 2. [10.1093/biostatistics/kxac029](https://doi.org/10.1093/biostatistics/kxac029) — A flexible approach for predictive biomarker discovery
- **作者**: Philippe Boileau, Nina Ting Qi, Mark J van der Laan, Sandrine Dudoit, Ning Leng
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 4 · pp 1085-1105
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在精准医疗的预测性生物标志物发现中，传统治疗规则估计方法在高维协变量下常导致高假发现率，本文提出一种直接评估标志物重要性的 variable importance parameter 及其非参推断程序。该估计量基于灵活的非参数框架，在数据生成过程的宽松条件下被证明具有双重稳健性（double robustness）和渐近线性（asymptotically linear），从而保证了对重要性度量的有效推断。方法避免了直接估计最优治疗规则，而是通过目标参数的 influence function 构建推断，有效区分预测性与非预测性标志物。模拟研究（中高维 RCT）和转移性肾细胞癌临床试验的基因表达数据应用均表明，该方法比基于治疗规则估计的程序更准确。对您有用：本文将 semiparametric efficiency 与 causal variable importance 结合，其 double robust / asymptotically linear 的证明思路及 R 包 uniCATE 对您在因果推断与半参效率理论方向的研究有直接参考价值。
- **关键技术**: `variable importance parameter`, `double robustness`, `asymptotically linear estimator`, `nonparametric inference`, `predictive biomarker discovery`
- **为什么对您有用**: 直接关联您的因果推断与半参效率理论兴趣：展示了如何在宽松条件下为 causal variable importance 构造 double robust 且渐近线性的估计量，且附有高维 RCT 模拟与真实临床数据应用，方法可迁移至流行病学因果异质性分析。

### 3. [10.1093/biostatistics/kxac026](https://doi.org/10.1093/biostatistics/kxac026) — Designing three-level cluster randomized trials to assess treatment effect heterogeneity
- **作者**: Fan Li, Xinyuan Chen, Zizhong Tian, Denise Esserman, Patrick J Heagerty, Rui Wang
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 4 · pp 833-849
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在三层聚类随机试验（参与者嵌套于子聚类如医生，子聚类嵌套于聚类如诊所）设定下，本文研究如何为确认性治疗效应异质性分析进行试验设计。作者基于线性混合 ANCOVA 模型的渐近协方差矩阵，推导了新的解析设计公式，适用于评估聚类层、子聚类层和参与者层的效应修饰因子，且随机化可在任意层执行。核心技术贡献在于刻画了效应修饰因子与条件结果之间的嵌套可交换相关结构，并由此给出异质性检验的 power 与样本量公式。模拟验证了公式精度，两个真实试验案例展示应用。对您而言，本文提供了多层结构下 treatment effect heterogeneity 的设计视角，与因果推断中 effect modification 的估计与推断问题有连接，但理论深度偏试验设计而非半参数效率或识别理论。
- **关键技术**: `linear mixed ANCOVA model`, `asymptotic covariance matrix`, `nested exchangeable correlation`, `effect modification`, `power calculation`, `three-level cluster randomization`
- **为什么对您有用**: 与因果推断中 effect modification / subgroup analysis 的估计与推断问题有方法学连接，但核心贡献是试验设计公式而非识别或效率理论，对您 primary interest 的直接推进有限。

### 4. [10.1093/biostatistics/kxac028](https://doi.org/10.1093/biostatistics/kxac028) — Alleviating spatial confounding in frailty models
- **作者**: Douglas R M Azevedo, Marcos O Prates, Dipankar Bandyopadhyay
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 4 · pp 945-961
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在空间生存分析（frailty 模型）设定下，研究固定效应与空间随机效应之间的空间混杂问题，目标是在存在不可观测空间异质性时获得固定效应的有效推断。现有广义线性混合模型中的投影方法因维度不兼容无法直接推广至 frailty 模型；本文提出两步法：(i) 通过降维将设计矩阵投影至空间效应维度；(ii) 约束随机效应与投影后的设计矩阵正交以消除混杂。在全贝叶斯框架下，采用 INLA（integrated nested Laplace approximation）实现快速计算与推断。模拟与加州呼吸道癌症生存数据实证表明，该方法在混杂消除与模型表现上优于传统方案。对您有用：该文将正交投影引入空间混杂消除，其 INLA 计算方案与流行病学实证对您在因果推断（混杂识别与消除）和统计计算方向的研究具有参考价值。
- **关键技术**: `spatial confounding`, `frailty models`, `orthogonal projection`, `restricted spatial models`, `INLA`, `dimension reduction`
- **为什么对您有用**: 直击因果推断中的混杂消除问题，通过正交投影与降维解决空间生存模型的识别与推断，且 INLA 计算方法与流行病学数据应用对您的统计计算和流行病学应用兴趣有直接参考价值。

### 5. [10.1093/biostatistics/kxac024](https://doi.org/10.1093/biostatistics/kxac024) — A controlled effects approach to assessing immune correlates of protection
- **作者**: Peter B Gilbert, Youyi Fong, Avi Kenny, Marco Carone
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 4 · pp 850-865
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在随机化安慰剂对照疫苗试验中，传统免疫相关物仅反映关联而非因果效应，本文在因果中介框架下定义受控风险曲线与受控疫苗效力（VE）曲线，目标是在右删失与两阶段抽样下识别因果保护相关物。核心方法基于受控直接效应，当安慰剂组生物标志物为常数时，通过 G-computation 在半参数模型（如 Cox 模型）下进行估计与推断。此外，作者提出模块化敏感性分析策略，量化未测量混杂对受控 VE 估计的干扰。实证分析登革热疫苗 III 期试验数据，表明受控登革热风险随中和抗体滴度强烈变化。对您而言，本文将受控直接效应中介分析引入疫苗评价的框架及处理两阶段抽样/右删失的识别策略，可直接迁移至流行病学队列研究的因果中介与敏感性分析中。
- **关键技术**: `controlled direct effect`, `causal mediation analysis`, `G-computation`, `semiparametric Cox model`, `sensitivity analysis to unmeasured confounding`, `two-phase sampling`
- **为什么对您有用**: 本文将受控直接效应中介分析引入疫苗评价，其识别与 G-computation 估计框架对您在流行病学应用因果推断（中介与敏感性分析）有直接迁移价值，且提供了真实的两阶段抽样疫苗数据集。

### 6. [10.1093/biostatistics/kxac020](https://doi.org/10.1093/biostatistics/kxac020) — Doubly robust evaluation of high-dimensional surrogate markers
- **作者**: Denis Agniel, Boris P Hejblum, Rodolphe Thiébaut, Layla Parast
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 4 · pp 985-999
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在观察性研究设定下，本文研究高维替代标志物的效用评估问题，目标 estimand 为替代标志物对处理效应的捕捉比例，关键假设包括无混杂及一致性。作者将替代标志物效用评估与平均处理效应（ATE）的因果推断框架建立等价联系，提出了一种双重稳健（DR）估计量。该方法利用机器学习灵活估计干扰函数，结合交叉拟合技术放松模型依赖，以实现 n^{-1/2}-CAN 及达到半参数有效界。文中进一步揭示了高维替代标志物评估与因果中介分析之间的内在理论联系。理论上证明了估计量的双重稳健性与渐近正态性，并在埃博拉研究数据上验证了基因表达作为免疫激活替代标志物的效用。对您有用：该文将高维替代标志物与中介效应打通，其基于 DML 的双重稳健框架可直接迁移至您关注的因果中介效应与半参数效率理论研究。
- **关键技术**: `doubly robust estimation`, `surrogate marker evaluation`, `cross-fitting`, `machine learning nuisance estimation`, `causal mediation connection`, `semiparametric efficiency`
- **为什么对您有用**: 直接关联您 primary interest 中的因果推断（中介效应）与效率理论（双重稳健、DML），同时其埃博拉流行病学数据应用契合您 secondary interest 中的流行病学因果应用；高维替代标志物的 DR 框架可迁移至高维中介分析。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1093/biostatistics/kxac030](https://doi.org/10.1093/biostatistics/kxac030) — Improved efficiency for cross-arm comparisons via platform designs
- **作者**: Tzu-Jung Huang, Alex Luedtke, THE AMP INVESTIGATOR GROUP
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 4 · pp 1106-1124
- 相关性 3/10 · novelty: `new_theory`
- **摘要**: 在平台试验与多个独立两臂试验的设定下，目标是估计多干预相对于共同对照的相对风险之差（cross-arm contrast），并在 contemporaneous randomization 假设下比较两者的统计效率。理论证明由于平台试验中对照的共享机制，基于平台数据的估计量具有与独立试验相同或更优的精度，即使前者入组人数更少。进一步提出了一种自适应非劣效性检验程序，用于检验某干预相对于其他最优干预的非劣效性，无需预先指定哪个干预最优。数值研究与 HIV 单抗试验数据表明，平台试验在估计精度和检验功效上均显著优于独立试验。该文从效率理论角度严格量化了共享对照带来的精度增益，且自适应非劣效检验直接关联您对假设检验与效率理论的兴趣。
- **关键技术**: `platform trial design`, `shared control efficiency`, `relative risk contrast`, `adaptive noninferiority testing`, `contemporaneous randomization`
- **为什么对您有用**: 严格量化了共享对照带来的效率增益（关联 efficiency theory），并提出自适应非劣效检验（关联 hypothesis testing），同时包含 HIV 流行病学队列数据的应用。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1093/biostatistics/kxac033](https://doi.org/10.1093/biostatistics/kxac033) — Bayesian sample size determination in basket trials borrowing information between subsets
- **作者**: Haiyan Zheng, Michael J Grayling, Pavel Mozgunov, Thomas Jaki, James M S Wason
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 4 · pp 1000-1016
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在篮子试验的随机化设定下，本文研究如何在各亚组试验间借用信息以确定样本量，目标是在控制一类错误和指定功效的前提下求解各亚组所需样本量。作者提出一种贝叶斯样本量确定方法，通过预设亚组间的成对同质性先验来实现信息借调。核心贡献是推导了闭式样本量公式，使得各亚组试验的样本量可基于功效和显著性水平联立求解。在不借用信息时，该贝叶斯公式退化为与频率派可比的结果；而在同质亚组间借用信息时，可显著降低所需总样本量。模拟与真实试验实例表明该方法能有效维持目标真阳性与假阳性率。对您而言，本文虽涉及贝叶斯假设检验与功效计算，但属于临床试验设计范畴，缺乏半参数或高维理论深度，仅作为多假设检验框架下信息借用机制的泛读参考。
- **关键技术**: `Bayesian sample size determination`, `basket trial design`, `information borrowing`, `commensurability prior`, `closed-form power formula`
- **为什么对您有用**: 本文涉及贝叶斯假设检验与功效计算，但属于临床试验设计范畴，理论深度较浅，与您关注的数学统计/半参数效率等核心方向距离较远，仅作多假设检验框架下信息借用机制的泛读参考。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1093/biostatistics/kxac018](https://doi.org/10.1093/biostatistics/kxac018) — Multiscale analysis of count data through topic alignment
- **作者**: Julia Fukuyama, Kris Sankaran, Laura Symul
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 4 · pp 1045-1065
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在生物计数数据的主题模型分析中，针对主题数 K 难以确定且真实值可能不存在的问题，本文提出一种跨不同 K 值模型的多尺度对齐方法。核心机制是通过 topic alignment 追踪不同 K 下主题的分裂与合并关系，并基于此设计了三种诊断工具，以判断主题的持续性、短暂性或分裂性。方法结合了可视化表示，并在模拟与真实数据上验证了其解释力，配套发布了 R 包 alto。该方法避免了单一 K 值选择的武断性，提供了比传统模型选择更丰富的生成过程洞察。对您而言，虽然本文缺乏严格的半参数效率或假设检验理论，但其跨模型对齐的计算思路和 R 包实现可为统计计算方向提供模型稳定性诊断的算法参考。
- **关键技术**: `topic alignment`, `multiscale model comparison`, `LDA diagnostics`, `count data modeling`, `R package alto`
- **为什么对您有用**: 本文主要属于统计计算与探索性数据分析，虽无严格的半参数或高维推断理论，但其跨模型对齐的算法设计与 R 包实现可为您的统计计算兴趣提供模型稳定性诊断的计算参考。

### 2. [10.1093/biostatistics/kxac004](https://doi.org/10.1093/biostatistics/kxac004) — Bayesian group testing with dilution effects
- **作者**: Curtis Tatsuoka, Weicong Chen, Xiaoyi Lu
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 4 · pp 885-900
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文在 group testing 框架下引入稀释效应（dilution effects），建立基于格（lattice）的 Bayesian 模型，目标是在池化检测中同时估计个体感染状态与稀释参数，允许非二元检测响应分布。核心方法为 Bayesian halving algorithm——一种利用模型序结构的直观分组选择规则，在强稀释效应下仍具有最优收敛性质；同时提出 look-ahead 规则以减少分类阶段数。计算层面实现了高性能分布式计算以支持更大池化规模，并提供了 web 计算器辅助决策。理论结果表明即使在中度流行率下 group testing 仍大幅节省检测次数，但需权衡阶段数与变异性增加。对您而言，分布式计算实现与序结构下的最优收敛分析可作统计计算兴趣的参考案例，流行病学场景下的池化设计也可作为 secondary interest 中流行病学应用的入门阅读。
- **关键技术**: `Bayesian group testing`, `lattice-based model`, `dilution effects`, `Bayesian halving algorithm`, `look-ahead selection rules`, `distributed computing`
- **为什么对您有用**: 分布式计算实现与序结构下的最优收敛性质连接到统计计算兴趣；流行病学池化检测场景可作为 secondary interest 中流行病学应用的入门阅读，但方法学核心（Bayesian 设计/组合优化）与 primary interests（causal inference / efficiency theory / semiparametrics）距离较远。

## 流行病学  *(epidemiology, 2 篇)*

### 1. [10.1093/biostatistics/kxac025](https://doi.org/10.1093/biostatistics/kxac025) — Bayesian design of clinical trials using joint models for recurrent and terminating events
- **作者**: Jiawei Xu, Matthew A Psioda, Joseph G Ibrahim
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 4 · pp 866-884
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在复发事件与终止事件联合建模的临床试验设定下，本文提出基于多脆弱项（multi-frailty）联合模型的贝叶斯试验设计方法。两过程间的依赖通过共享脆弱项（shared frailty）刻画，推断基于互斥假设的后验模型概率进行。作者提出了样本量确定方法以保证贝叶斯视角下的高功效与I类错误率控制，并进一步将参数模型推广至使用Dirichlet过程非参数混合来建模脆弱项分布。实证以结直肠癌临床试验展示设计流程。对您而言，该文在纵向/事件时间数据的联合建模及非参数脆弱项设定上有一定参考价值，但核心贝叶斯试验设计与您主攻的半参数效率/因果推断距离较远。
- **关键技术**: `joint model for recurrent and terminating events`, `shared frailty model`, `Bayesian clinical trial design`, `Dirichlet process mixture`, `posterior model probability`
- **为什么对您有用**: 涉及纵向/事件时间数据的联合建模及非参数脆弱项，与因果推断中的纵向数据设定有一定交集，但核心为贝叶斯试验设计，对半参数效率与因果推断的直接启发有限。

### 2. [10.1093/biostatistics/kxac023](https://doi.org/10.1093/biostatistics/kxac023) — Constrained groupwise additive index models
- **作者**: Pierre Masselot, Fateh Chebana, Céline Campagna, Éric Lavigne, Taha B M J Ouarda, Pierre Gosselin
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 4 · pp 1066-1084
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在环境流行病学设定下，目标是构建可解释的复合暴露指数以预测健康结局，模型假设为约束分组可加指数模型（CGAIM），将自然同组的变量合为指数并允许对指数权重及与响应的关系函数施加线性约束。估计采用基于 penalized spline 的 backfitting 型算法，配合指数选择（类似 group lasso 的惩罚）与基于 influence function 的推断程序。模拟显示估计偏差与方差较低、指数选择敏感度与特异度良好，但置信区间覆盖率存在不可忽略的误差。实证部分用高温健康预警系统的热指数构建展示方法。对您而言，该文的可加指数模型属于 semiparametric sieve/penalized spline 估计范畴，约束推断的 influence function 构造可作方法参考，但理论深度有限且覆盖率问题未解决，主要价值在于流行病学暴露指数建模的应用范式与数据结构。
- **关键技术**: `additive index model`, `penalized spline backfitting`, `group-wise variable selection`, `linear constraints on index weights`, `influence function based inference`
- **为什么对您有用**: 连接您 secondary interest 的流行病学应用（环境暴露指数建模），semiparametric additive index 模型的约束估计与推断可作方法借鉴，但理论贡献偏应用层面。

## 其他  *(other, 2 篇)*

### 1. [10.1093/biostatistics/kxac013](https://doi.org/10.1093/biostatistics/kxac013) — Spatial Difference Boundary Detection for Multiple Outcomes Using Bayesian Disease Mapping
- **作者**: Leiwen Gao, Sudipto Banerjee, Beate Ritz
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 4 · pp 922-944
- 相关性 3/10
- **摘要**: ```json
{
  "topic": "epidemiology",
  "summary_zh": "在区域单元（县、州等）上对多种相关疾病进行"差异边界"检测，即识别相邻区域间空间效应显著不同的边界线。方法将问题表述为贝叶斯成对多重比较，通过计算相邻空间效应不同的后验概率来判定边界；空间随机效应采用一类多变量区域化 Dirichlet 过程先验，同时刻画空间依赖与疾病间依赖。模拟研究验证了方法在有限样本下的检测性能，实证分析使用 NCI SEER 项目多种癌症数据识别差异边界。该文提供了 SEER 癌症区域数据集及贝叶斯空间建模的完整 pipeline，对您在流行病学队列数据上的因果/应用工作有数据集和建模思路参考价值，但方法本身（Bayesian disease mapping / Dirichlet process）与您 primary interests 中的 semiparametric efficiency 或 hypothesis testing 理论重叠有限。",
  "key_techniques": [
    "Bayesian pairwise multiple comparisons",
    "areally referenced Dirichlet process",
    "multivariate spatial random effec

### 2. [10.1093/biostatistics/kxac010](https://doi.org/10.1093/biostatistics/kxac010) — Reassessing pharmacogenomic cell sensitivity with multilevel statistical models
- **作者**: Matt Ploenzke, Rafael Irizarry
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 4 · pp 901-921
- 相关性 2/10 · novelty: `application`
- **摘要**: 在药物基因组学设定下，目标是量化细胞系对变剂量药物的敏感性并区分药物效应类型（广谱 vs 靶向），面临生物与实验变异导致的低信噪比挑战。本文提出一种分层混合模型，利用跨数据集的重复测量来估计药物特异性的混合分布，以提升估计功效。该模型框架可输出靶向效应下细胞易感的后验概率，或广谱效应下的相对效应大小。实证分析验证了多个公开药理基因组数据集间的配对一致性，并识别出携带 EML4-ALK 或 NPM1-ALK 基因融合的细胞对 crizotinib 的敏感性。本文核心为贝叶斯分层建模在生统领域的应用，对您关注的因果推断、半参数效率或高维推断理论无直接方法学推进，但在处理重复测量低信噪比数据的分层建模思路上有一定参考价值。
- **关键技术**: `hierarchical mixture model`, `posterior probability estimation`, `Bayesian inference`, `pharmacogenomic data integration`, `drug sensitivity quantification`
- **为什么对您有用**: 本文属于生物统计应用，与您的主要理论兴趣（因果推断、半参数/高维理论）无直接重叠；虽涉及医学数据，但未使用您关注的因果推断方法，方法学新颖度有限，仅作为处理低信噪比重复测量数据的分层建模参考。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

