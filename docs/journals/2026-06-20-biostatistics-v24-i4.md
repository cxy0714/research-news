# Biostatistics — Vol 24  Issue 4  ·  2026-06-20

- 共 14 篇 · Biostatistics
- 目录核对 ⚠️ 疑似漏 2 篇（对照 OpenAlex 16 篇）：10.1093/biostatistics/kxac019、10.1093/biostatistics/kxac014

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

Biostatistics Vol 24 Issue 4 的论文可归纳为三条主线：**因果推断与中介分析**、**临床试验设计与假设检验的效率改进**、**贝叶斯方法在空间与群组检测中的应用**。因果推断线占据五篇（“高维替代标记的双稳健评估”、“交叉直接效应”、“空间混杂缓解”、“受控效应评估免疫保护”、“预测性biomarker的灵活推断”），集中关注替代标记效用、中介效应分解、空间混杂偏误以及预测性biomarker的非参数推断，方法工具以半参数效率理论、双稳健估计、交叉拟合和G-computation为核心。临床试验设计线涵括“平台试验交叉比较的效率提升”、“三水平聚类试验的效应异质性检验”、“篮子试验的贝叶斯样本量确定”、“复发-终止事件联合模型试验设计”，核心推进是利用共享对照组、层次嵌套结构或信息借用机制提高估计精度或降低样本量。剩余六篇（“约束分组加性指数模型”、“计数数据的主题对齐”、“空间差异边界检测”、“贝叶斯群组检测稀释效应”、“贝叶斯篮子样本量”、“药物基因组学层次混合模型”）构成第三条主线，主要贡献在贝叶斯非参空间建模、自适应群组检测算法、以及多暴露指数构建的可解释性框架。

---

因果推断主线中的**半参数效率**与**双稳健性**是本期最突出的技术特征。“高维替代标记”将替代标记效用评估视为ATE的DR估计问题，利用cross-fitting在semiparametric模型下实现n^{-1/2}-CAN并达到有效界；“预测性biomarker的灵活推断”基于TMLE/one-step框架构建DR且渐近线性估计量，避免高维下treatment rule估计的假阳性；“受控效应评估”将疫苗保护力分析转化为因果中介，结合Cox模型和G-computation处理右删失与两阶段抽样，并给出模块化敏感性分析。“交叉直接效应”则针对双中介场景，在序贯或独立结构下给出识别表达式并在随机化设定下推导符号界，补充了中介分析的效应分解工具。这些工作共同显示了双稳健和半参数效率方法在因果估计与分析中的系统推广。

**临床试验设计与检验**主线中，“平台试验交叉比较”通过共享对照组的影响函数和效率界证明精度不劣于独立试验，并设计自适应非劣效性检验；“三水平聚类试验”推导了效应修饰因子交互项估计量的渐近协方差，为异质性检验提供精确样本量公式，依赖线性混合ANCOVA和嵌套可交换相关假设。两个工作均以渐近理论驱动设计优化。贝叶斯方法主线中，“空间差异边界检测”将多结局空间效应差异识别转化为成对多重比较，使用多变量区域参考Dirichlet过程捕捉跨区域与跨疾病依赖；“贝叶斯群组检测”针对稀释效应提出格点模型和贝叶斯减半算法，证明最优收敛性质并支持前瞻规则选池。这两篇分别展示了贝叶斯非参在空间流行病学以及自适应算法在检测效率上的创新。

---

与**因果推断**、**半参数效率**、**高维替代标记**最直接相关的论文是“高维替代标记的双稳健评估”、“预测性biomarker的灵活推断”和“受控效应评估”；对于**中介分析**与**效应分解**，可优先阅读“交叉直接效应”和“受控效应评估”；关注**空间混杂与贝叶斯空间建模**的读者可留意“空间混杂缓解”和“空间差异边界检测”；聚焦**临床试验设计与效率**的读者可关注“平台试验交叉比较”和“三水平聚类试验异质性检验”。

## 因果推断  *(causal_inference, 5 篇)*

### 1. [10.1093/biostatistics/kxac020](https://doi.org/10.1093/biostatistics/kxac020) · [arXiv](https://arxiv.org/abs/2012.01236) — Doubly robust evaluation of high-dimensional surrogate markers
- **作者**: Denis Agniel, Boris P Hejblum, Rodolphe Thiébaut, Layla Parast
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 4 · pp 985-999
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在观察性或随机化设定下，目标是评估高维替代标记（surrogate marker）对主要结局的效用，核心 estimand 为基于替代标记的 ATE 估计误差（surrogate utility measure），不要求处理随机化。方法将替代标记效用评估与经典 ATE 的双稳健估计建立形式化连接，从而构造出 DR estimator；利用机器学习估计 nuisance 函数（outcome model / treatment model）并结合 cross-fitting，在 semiparametric model 下实现 n^{-1/2}-CAN 与 semiparametric efficiency bound 达到。理论证明该 DR estimator 的双稳健性与局部效率，并指出其 estimand 与特定中介效应（mediation effect）的等价联系。实证部分在 Ebola 基因表达数据上验证了高维基因标记作为免疫激活替代的可行性。对您有用：将高维替代标记评估纳入 DR / DML 框架，直接连接到 causal inference 的 mediation 与 semiparametric efficiency 方向。
- **关键技术**: `doubly robust estimation`, `cross-fitting`, `machine learning nuisance estimation`, `surrogate marker evaluation`, `semiparametric efficiency bound`, `mediation analysis connection`
- **为什么对您有用**: 本文直接连接到 causal inference 中的 mediation 与 semiparametric efficiency 子方向，将高维替代标记效用评估转化为 DR / DML 框架下的 ATE 估计问题。您武器库中 semiparametric theory（moderately_familiar）与 estimation theory in causal inference（very_familiar）可以直接攻本文的理论部分；若想进一步在高维替代标记设定下刻画 sharper rate 或 minimax bound，需先在 HOIF（moderately_familiar）上长肌肉以分析高维 nuisance 估计的残余偏差对 DR estimator 的影响。**中期可做**。

### 2. [10.1093/biostatistics/kxac037](https://doi.org/10.1093/biostatistics/kxac037) — Cross-direct effects in settings with two mediators
- **作者**: Erin E Gabriel, Arvid Sjölander, Dean Follmann, Michael C Sachs
- **期刊/来源**: Biostatistics
- **机构**: University of Copenhagen · Karolinska Institutet · National Institute of Allergy and Infectious Diseases
- **分类**: vol 24 · issue 4 · pp 1017-1030
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对两个中介变量的场景，提出五类交叉直接效应（cross-CDE 和 cross-NDE），其核心思想是将一个中介固定为常数、另一个保留自然水平，从而扩展了传统自然直接效应（NDE）和控制直接效应（CDE）。文章考虑两种中介结构——顺序中介（一个中介影响另一个）和无相互影响的中介，并在无未观测混杂的观察性设定下给出了任意变量类型的识别表达式。针对二元变量，进一步在随机化设定下（允许结局-中介关系存在残差混杂）推导了紧的符号界。这些 estimands 在免疫学中可分解疫苗诱导免疫反应的直接与间接路径，具有实证动机。对您而言，该工作为中介分析提供了新的效应分解框架，连接您 causal inference 中 mediation 子方向；您非常熟悉的因果估计理论可直接用于构造这些 estimands 的半参数或非参数估计量。中期可做——当前 paper 仅处理识别与边界，您可通过提升 moderately_familiar 的 semiparametric theory 和 HOIF 工具开发相应的有效估计与推断方法。
- **关键技术**: `natural direct effect`, `controlled direct effect`, `sequential mediators`, `identification under no unmeasured confounding`, `symbolic bounds for binary variables`
- **为什么对您有用**: 1. 直接聚焦于 causal inference 中的 mediation 子方向，提出了传统 NDE/CDE 之外的交叉效应，拓展了效应分解框架；2. 您 very_familiar 的 estimation theory in causal inference（如 DR 估计、IPW）可用于为这些 estimands 构造估计量，结合您对非参数统计的掌握可进一步实现无模型假设的估计；3. 中期可做——论文仅提供识别和符号界，尚未处理估计与推断，您需先将 moderately_familiar 的 semiparametric theory 和 HOIF 熟化至 very_familiar 水平，进而开发出半参数有效估计量并用于流行病学实际数据。

### 3. [10.1093/biostatistics/kxac028](https://doi.org/10.1093/biostatistics/kxac028) · [arXiv](https://arxiv.org/abs/2008.06911) — Alleviating spatial confounding in frailty models
- **作者**: Douglas R M Azevedo, Marcos O Prates, Dipankar Bandyopadhyay
- **期刊/来源**: Biostatistics
- **机构**: Universidade Federal de Minas Gerais · Virginia Commonwealth University Medical Center
- **分类**: vol 24 · issue 4 · pp 945-961
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在空间 frailty 模型（广义线性混合模型在生存分析中的延伸）设定下，研究固定效应与空间随机效应之间的空间混杂问题，目标是缓解因混杂导致的固定效应推断偏误。现有基于投影的 restricted spatial model 方法因固定效应与空间随机效应维度不兼容而无法直接移植到空间生存场景。本文提出两步法：先对设计矩阵做降维投影至与空间效应维度匹配，再确保随机效应与该新设计矩阵正交以缓解混杂。在全贝叶斯范式下，采用 INLA（integrated nested Laplace approximation）实现快速估计与推断。模拟与加州呼吸道癌症生存数据的应用表明，该方法在混杂缓解与模型表现上优于替代方案。对您可能有用：此文处理空间混杂的正交投影思路与 proximal CI 中用 negative control 消除混杂的 identification 逻辑有结构相似性。
- **关键技术**: `spatial confounding alleviation`, `restricted spatial model`, `orthogonal projection of design matrix`, `frailty model`, `INLA (integrated nested Laplace approximation)`, `Bayesian spatial survival analysis`
- **为什么对您有用**: 本文连接到因果推断中的混杂调整（空间混杂）子方向，其正交投影消除混杂的机制与 proximal CI 的 negative control 设定在结构上可类比。用您 very_familiar 的 identification theory in causal inference 可以审视其投影正交性是否真正实现了 identification，而非仅是计算层面的缓解。**中期可做**：若想将此类空间正交约束与 semiparametric efficiency 结合，需先在 moderately_familiar 的 semiparametric theory 上长肌肉，以建立投影估计的 influence function 与效率界。

### 4. [10.1093/biostatistics/kxac024](https://doi.org/10.1093/biostatistics/kxac024) — A controlled effects approach to assessing immune correlates of protection
- **作者**: Peter B Gilbert, Youyi Fong, Avi Kenny, Marco Carone
- **期刊/来源**: Biostatistics
- **机构**: University of Washington · Fred Hutch Cancer Center
- **分类**: vol 24 · issue 4 · pp 850-865
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在随机化疫苗试验中，传统免疫相关风险(CoR)分析缺乏因果疫苗效应视角；本文在 biomarker 于安慰剂组恒定的设定下，定义了受控风险曲线与受控疫苗效力曲线，将 CoP 评估转化为因果中介分析问题。识别公式处理了终点右删失与 biomarker 的两阶段抽样设计，估计采用半参数模型（如 Cox 模型）下的 G-computation。作者进一步提出模块化敏感性分析方法，量化未测量混杂对 CoP 证据的稳健性。实证应用于登革热疫苗 III 期试验，显示受控登革热风险随 50% 中和抗体滴度强烈变化。本文将 controlled effects 引入流行病学因果中介评估，对您在因果推断的 identification 与 sensitivity analysis 子方向有直接参考价值。
- **关键技术**: `controlled effects`, `causal mediation analysis`, `G-computation`, `semiparametric Cox model`, `two-phase sampling`, `sensitivity analysis for unmeasured confounding`
- **为什么对您有用**: 本文直接连接因果推断的 identification 与 sensitivity analysis 子方向，将流行病学 surrogate endpoint 评估纳入因果中介框架，其 modular sensitivity analysis 可与您熟悉的 identification theory 对接。用您 very_familiar 的 estimation theory in causal inference 与 moderately_familiar 的 identification theory 可直接审视其 G-computation 估计效率与识别假设的松弛空间。**立即可做**：用 semiparametric efficiency bound 评估其 G-computation 估计是否达到最优率，或用 HOIF 探索更高效的估计路径。

### 5. [10.1093/biostatistics/kxac029](https://doi.org/10.1093/biostatistics/kxac029) · [arXiv](https://arxiv.org/abs/2205.01285) — A flexible approach for predictive biomarker discovery
- **作者**: Philippe Boileau, Nina Ting Qi, Mark J van der Laan, Sandrine Dudoit, Ning Leng
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 4 · pp 1085-1105
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在精准医学的 RCT 设定下，目标是直接评估潜在预测性 biomarker 的变量重要性参数，而非通过治疗规则估计间接筛选。作者提出一种灵活的非参数推断程序，构造了 double robust 且 asymptotically linear 的估计量，在数据生成过程较宽松的条件下允许对重要性度量进行有效推断。核心机制基于 TMLE / one-step 的双稳健框架，结合 cross-fitting 以适应中高维协变量向量，避免了传统 treatment rule estimation 方法在高维下高 false discovery rate 的问题。模拟研究验证了其统计保证，并在转移性肾细胞癌临床试验的肿瘤基因表达数据中发现了预测性 biomarker，比基于治疗规则的方法更易区分预测性与非预测性 biomarker。对您可能有用：该工作将变量重要性参数与 double robust 推断结合，为高维因果推断中的 biomarker 筛选提供了直接 targeting estimand 的视角。
- **关键技术**: `variable importance parameter`, `double robust estimation`, `asymptotically linear estimator`, `cross-fitting`, `TMLE / one-step estimation`, `predictive biomarker discovery`
- **为什么对您有用**: 直接连接因果推断的 estimation theory 子方向，特别是高维设定下的 double robust / asymptotically linear 推断。您武器库中的 semiparametric theory 和 M-estimation theory 可以直接攻这篇 paper 的双稳健估计量构造与 influence function 推导口子，验证其宽松条件下的 CAN 性质是否可进一步收紧。**立即可做**：用 very_familiar 的 minimax bounds 和 moderately_familiar 的 semiparametric theory 工具即可动手分析其效率界与高维收敛率。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1093/biostatistics/kxac030](https://doi.org/10.1093/biostatistics/kxac030) · [arXiv](https://arxiv.org/abs/2112.10967) — Improved efficiency for cross-arm comparisons via platform designs
- **作者**: Tzu-Jung Huang, Alex Luedtke, THE AMP INVESTIGATOR GROUP
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 4 · pp 1106-1124
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 在平台试验（platform trial）设定下，目标是多干预相对于同一对照组的相对风险对比（cross-arm comparison）的估计与推断，核心假设为同期随机化（contemporaneous randomization）与共享对照组。方法上，通过理论证明平台试验中共享对照组使得相对风险对比的估计精度等于或优于多个独立两臂试验，即使前者总样本量更小；估计量基于相对风险参数的 influence function 与 semiparametric efficiency bound 分析。此外，提出自适应非劣效性检验（adaptive noninferiority test），无需预先指定最强干预，通过多重检验校正控制 type-I error。数值与 HIV 单抗试验数据表明，平台设计在精度与检验功效上均有实质提升。对您可能有用：该文的效率理论分析与自适应检验框架直接连接到 efficiency theory 与 hypothesis testing 子方向。
- **关键技术**: `platform trial design`, `shared control efficiency`, `relative risk contrast`, `semiparametric efficiency bound`, `adaptive noninferiority testing`, `contemporaneous randomization`
- **为什么对您有用**: 本文直接连接到 efficiency theory（semiparametric efficiency bound 在复杂试验设计下的刻画）与 hypothesis testing（自适应非劣效性多重检验）子方向。您武器库中的 semiparametric theory 与 minimax bounds 可以攻其效率界证明的口子——验证其声称的精度优势是否达到真正的 efficiency bound，以及共享对照组带来的信息增益是否有更紧的 minimax 刻画。**中期可做**：需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以严格推导该复杂参数（相对风险对比）的 influence function 与 efficiency bound；自适应检验的多重校正部分则需补充 sequential / adaptive testing 的具体工具。

### 2. [10.1093/biostatistics/kxac026](https://doi.org/10.1093/biostatistics/kxac026) — Designing three-level cluster randomized trials to assess treatment effect heterogeneity
- **作者**: Fan Li, Xinyuan Chen, Zizhong Tian, Denise Esserman, Patrick J Heagerty, Rui Wang
- **期刊/来源**: Biostatistics
- **机构**: Yale University · Mississippi State University · Pennsylvania State University · University of Washington · Harvard University · Harvard Pilgrim Health Care
- **分类**: vol 24 · issue 4 · pp 833-849
- 相关性 4/10 · novelty: `new_theory`
- **摘要**: 在三层嵌套聚类随机试验（参与者-子聚类-聚类）中，目标是评估处理效应异质性，即检验预设亚群（效应修饰因子）下的条件平均处理效应差异。作者基于线性混合 ANCOVA 模型，推导了效应修饰因子的交互项估计量的渐近协方差矩阵，并给出了检验效应异质性的样本量与功效设计公式。关键假设为嵌套可交换相关结构，适用于聚类层、子聚类层或参与者层的修饰因子及任意层随机化设计。模拟验证了渐近公式的准确性，并用两个真实试验数据展示了应用。对您有用之处：本文将多层嵌套结构下的异质性检验形式化为精确的渐近协方差计算，其推导路径与您熟悉的 M-estimation 渐近理论及因果推断中的效应异质性 identification 直接对接。
- **关键技术**: `linear mixed ANCOVA model`, `nested exchangeable correlation structure`, `asymptotic covariance matrix derivation`, `power analysis for effect heterogeneity`, `three-level cluster randomized trial`
- **为什么对您有用**: 本文直接连接因果推断中的效应异质性（effect heterogeneity / moderation）估计与假设检验设定，属于试验设计中的数学统计推导。您武器库中 M-estimation theory（moderately_familiar）可直接攻入其渐近协方差矩阵的推导细节，验证其可交换相关假设下 influence function 的闭式解是否可推广至更一般的协方差结构。**中期可做**：需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以将本文局限于线性混合模型的功效公式拓展至半参数框架下的异质性检验。

## 流行病学  *(epidemiology, 6 篇)*

### 1. [10.1093/biostatistics/kxac023](https://doi.org/10.1093/biostatistics/kxac023) — Constrained groupwise additive index models
- **作者**: Pierre Masselot, Fateh Chebana, Céline Campagna, Éric Lavigne, Taha B M J Ouarda, Pierre Gosselin
- **期刊/来源**: Biostatistics
- **机构**: London School of Hygiene & Tropical Medicine · Institut National de la Recherche Scientifique · Institut National de Santé Publique du Québec · Health Canada · University of Ottawa · Ouranos
- **分类**: vol 24 · issue 4 · pp 1066-1084
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在环境流行病学中，本研究提出约束分组加性指数模型（CGAIM），用于从大量暴露变量中构建易于解释的综合指数以预测健康结局。模型将预测变量按自然分组，并对指数权重和响应函数形式施加线性约束（如单调性或非负性），以融入先验知识或操作需求。估计采用高效优化算法，指数选择基于似然比检验，置信区间通过线性约束下的渐近理论构造。模拟显示估计值偏差小、方差低，指数选择灵敏度和特异度良好，但置信区间覆盖率略有偏差。案例应用于加拿大热指数预警系统的构建。本文为多暴露指数建模提供了一个灵活且可解释的统计框架，对流行病学中指数类预测模型的实证研究和理论分析有参考价值。
- **关键技术**: `Groupwise additive index models`, `Constrained optimization (weight and shape constraints)`, `Likelihood ratio test for index selection`, `Environmental health index construction`, `Bias-variance tradeoff in high-dimensional prediction`
- **为什么对您有用**: 本文属于secondary interest中流行病学的应用方法论文，具体涉及环境流行病学中的多暴露综合指数构建，并提供了真实数据集和模拟框架。研究者武器库中的'nonparametric statistics'和'software development'可直接用于分析其约束加性模型的估计理论（如权重收敛性）或复现拓展算法。作为入门读物，该文问题设定清晰、数据侧和模型侧透明，武器库足以支撑深入理解，值得花时间阅读全文以熟悉流行病学指数建模的典型思路和推断需求。

### 2. [10.1093/biostatistics/kxac018](https://doi.org/10.1093/biostatistics/kxac018) · [arXiv](https://arxiv.org/abs/2109.05541) — Multiscale analysis of count data through topic alignment
- **作者**: Julia Fukuyama, Kris Sankaran, Laura Symul
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 4 · pp 1045-1065
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出了一种名为 topic alignment 的方法，用于分析不同主题数 K 的主题模型之间的结构关系。在生物计数数据（如微生物组、文本数据）中，用户通常需要指定主题数 K，但 K 的合理选择往往不唯一。该方法通过对齐不同 K 下的主题，识别哪些主题在不同模型中稳定出现、哪些是暂时性的，以及主题是否随 K 增加而分裂。作者还设计了三种诊断工具和一个可视化方案，帮助解释多模型间的模式。模拟和真实数据实验表明，该方法比单独选择一个 K 提供更深入的数据生成过程洞察。配套的 R 包 alto 已发布，便于实际应用。对您而言，本文的计数数据分析框架可直接用于流行病学数据集（如微生物组计数），且其多尺度对齐思路可能启发您在高维统计中探索类似的结构诊断方法。
- **关键技术**: `topic modeling`, `topic alignment`, `multiscale diagnostics`, `count data`, `R package alto`
- **为什么对您有用**: 本文属于流行病学计数数据的方法学工作（secondary interest），其主题对齐诊断工具可直接用于分析微生物组等流行病学数据集。您的武器库中的软件开发和非参数统计能力可帮助您快速理解并复用 alto 包；但若要深入改进对齐方法本身，需先补充主题模型理论（当前未覆盖），故暂不可做。本文适合作为流行病学应用方向的入门读物。

### 3. [10.1093/biostatistics/kxac033](https://doi.org/10.1093/biostatistics/kxac033) · [arXiv](https://arxiv.org/abs/2205.12227) — Bayesian sample size determination in basket trials borrowing information between subsets
- **作者**: Haiyan Zheng, Michael J Grayling, Pavel Mozgunov, Thomas Jaki, James M S Wason
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 4 · pp 1000-1016
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对篮子试验（basket trial）中同时评估多个患者子集（subtrial）的治疗效果问题，提出一种贝叶斯样本量确定方法，允许在疗效相似的子集之间借用信息。作者在随机化试验框架下推导了闭式样本量公式，通过预设的成对相似性（pairwise commensurability）水平，确保每个子试验有指定概率正确判断新药是否优于对照组或达到临床相关非劣效界值。该方法在无借用时退化为频率学派公式，得到可比样本量；启用借用时总样本量显著减小。通过两个真实篮子试验案例和全面的模拟研究，验证了该方法能在降低样本量的同时维持预期的真阳性率和假阳性率。对您有用：该工作直接对应二级兴趣中的流行病学（临床试验设计），其信息借用思想可迁移至因果推断中的多源数据融合与敏感性分析，且样本量公式为设计高效RCT提供了实用工具。
- **关键技术**: `Bayesian sample size determination`, `borrowing of information`, `commensurate subsets`, `closed-form sample size formula`, `basket trial design`, `randomized controlled trial`
- **为什么对您有用**: 本文连接二级兴趣中的流行病学（应用与数据集），尤其适用于需要同时评估多个亚组疗效的临床试验设计。研究者可利用已熟悉的‘estimation theory in causal inference’分析该样本量公式下估计量的渐近效率，或将其信息借用思想扩展到因果推断中多种群异质性识别问题。当前状态：暂不可做——核心方法依赖贝叶斯先验设定与MCMC计算，而武器库主要集中于频率学派与半参理论，需先补足贝叶斯试验设计的基本工具。

### 4. [10.1093/biostatistics/kxac025](https://doi.org/10.1093/biostatistics/kxac025) — Bayesian design of clinical trials using joint models for recurrent and terminating events
- **作者**: Jiawei Xu, Matthew A Psioda, Joseph G Ibrahim
- **期刊/来源**: Biostatistics
- **机构**: University of North Carolina at Chapel Hill
- **分类**: vol 24 · issue 4 · pp 866-884
- 相关性 3/10 · novelty: `application`
- **摘要**: 在复发-终止事件联合模型框架下，本文研究如何利用多 frailty 联合模型设计以复发与终止事件为多重主要终点的临床试验。核心方法采用共享 frailty刻画两类事件过程的依赖结构，推断基于互斥假设的后验模型概率。样本量确定通过贝叶斯视角下的 power 与 type I error 控制实现，同时提出用 Dirichlet 过程非参数混合替代参数 frailty 的推广方案并比较性能。实证以结直肠癌试验演示 IP 至少在一个终点上有利且在另一终点上无害的设计。对您可能有用：该文展示了 frailty 联合模型在流行病学试验设计中的贝叶斯推断流程，可作为 epi 领域应用因果/生存模型的入门案例。
- **关键技术**: `shared frailty joint model`, `Bayesian posterior model probability`, `Dirichlet process mixture`, `Bayesian sample size determination`, `recurrent-terminating event`
- **为什么对您有用**: 本文属于流行病学（临床试验设计）的 gateway reading：以结直肠癌数据演示了复发-终止事件联合模型的贝叶斯推断与设计流程，对外行读者相对友好，数据与模型设定交代清晰。武器库中的 semiparametric theory 与 M-estimation theory 可支撑理解其 Dirichlet process frailty 推广部分，但核心是贝叶斯试验设计而非您主攻的效率界/估计理论。是否值得读全文：若您想了解 epi 领域如何实际使用 frailty 模型处理复合终点，可花时间浏览其模型设定与模拟部分；若聚焦理论创新则不必深读。

### 5. [10.1093/biostatistics/kxac013](https://doi.org/10.1093/biostatistics/kxac013) — Spatial Difference Boundary Detection for Multiple Outcomes Using Bayesian Disease Mapping
- **作者**: Leiwen Gao, Sudipto Banerjee, Beate Ritz
- **期刊/来源**: Biostatistics
- **机构**: University of California, Los Angeles
- **分类**: vol 24 · issue 4 · pp 922-944
- 相关性 3/10 · novelty: `application`
- **摘要**: 在空间流行病学设定下，研究目标是识别相邻行政区域间空间效应存在显著差异的“差异边界”，以刻画健康地理差异。针对多结局（多种癌症）情形，本文将问题转化为贝叶斯成对多重比较，计算相邻空间效应不同的后验概率。核心方法是为空间随机效应赋予离散概率律，采用一类多变量区域参考 Dirichlet 过程（multivariate areally referenced Dirichlet process）模型，同时捕捉跨区域的空间依赖与跨疾病的依赖结构。模拟研究验证了方法性能，并使用 SEER 癌症发病率数据进行了实证分析。对您而言，本文提供了一个流行病学空间数据与贝叶斯非参模型结合的应用案例，但方法学 novelty 有限。
- **关键技术**: `Bayesian pairwise multiple comparisons`, `multivariate areally referenced Dirichlet process`, `spatial random effects`, `difference boundary detection`, `disease mapping`
- **为什么对您有用**: 本文属于流行病学应用，连接到 epidemiology (datasets, applied causal work) 子方向，提供了 SEER 癌症发病率数据集及空间建模分析流程。从方法学看，其核心是贝叶斯非参（Dirichlet process）与空间模型的结合，您武器库中 nonparametric statistics 可部分理解其先验构造逻辑，但空间贝叶斯层次模型与 MCMC 计算细节不在 very_familiar 范围内。作为 gateway reading，本文对空间流行病学数据结构有清晰展示，适合了解该领域数据特征与建模惯例，但方法学创新有限，不值得花时间深读全文。

### 6. [10.1093/biostatistics/kxac004](https://doi.org/10.1093/biostatistics/kxac004) — Bayesian group testing with dilution effects
- **作者**: Curtis Tatsuoka, Weicong Chen, Xiaoyi Lu
- **期刊/来源**: Biostatistics
- **机构**: Case Western Reserve University · University of California, Merced
- **分类**: vol 24 · issue 4 · pp 885-900
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对群组检测中的稀释效应（dilution effects）提出了一个贝叶斯框架，使用格点模型（lattice-based models）刻画测试样本浓度衰减对检测准确性的影响。该方法不仅支持二值结果，还能处理一般化的测试响应分布（如连续或序数指标），扩展了经典群组检测的适用范围。核心算法是“贝叶斯减半算法”（Bayesian halving algorithm），它利用模型的结构顺序在每一轮自适应地选择最优池子规模，并证明即使在强稀释效应下该算法仍具有最优的收敛性质（即分类个体所需轮数随池子大小指数递减）。进一步，作者提出了前瞻规则（look-ahead rules），允许同时选择多个池子以减少分类阶段数，并用模拟实验展示了在中等患病率下群组检测相对于个体检测的巨大测试数节省。文中还开发了一个网页计算器帮助用户权衡测试数、阶段数和变异性，并实现了高性能分布式计算以支持更大池子规模。这篇论文架构清晰、方法完整，对流行病学中大规模检测策略的设计有直接参考价值。作为流行病学应用，本文提供了真实数据模拟与公开计算工具，适合作为入门阅读；武器库中的算法设计与软件开发经验可直接用于复现或改进这类方法，值得花时间全文阅读以获取检测策略的权衡直觉。
- **关键技术**: `Bayesian group testing`, `dilution effects`, `lattice-based models`, `Bayesian halving algorithm`, `look-ahead rules`, `high-performance distributed computing`
- **为什么对您有用**: 本文属于流行病学中群组检测的方法论论文，与您的次要兴趣（流行病学应用）高度相关。文章清晰地展示了稀释效应下的贝叶斯框架及自适应算法，您的算法设计和软件开发经验可直接用于实现或扩展此类方法（如优化池子选择规则或并行计算）。作为 gateway reading，本文问题陈述和数据模型（结构、噪声、选择效应）较为清晰，非流行病学专家也能快速把握核心逻辑，值得花时间全文阅读，为将来流行病学合作储备检测策略知识。由于核心模型（格点贝叶斯）与您当前武器库（非参、因果、U统计）结构不同，目前暂不可直接动手，但算法和计算方面的经验可中期迁移。

## 其他  *(other, 1 篇)*

### 1. [10.1093/biostatistics/kxac010](https://doi.org/10.1093/biostatistics/kxac010) — Reassessing pharmacogenomic cell sensitivity with multilevel statistical models
- **作者**: Matt Ploenzke, Rafael Irizarry
- **期刊/来源**: Biostatistics
- **机构**: Harvard University · Dana-Farber Cancer Institute
- **分类**: vol 24 · issue 4 · pp 901-921
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文研究药物基因组学实验中细胞敏感性的统计估计问题。由于实验噪声大且生物变异性高，单个数据集信噪比低，而多个公共数据集的重复测量可提高统计功效。作者构建了一个层次混合模型（hierarchical mixture model），将药物效应分为广谱型（broad）和靶向型（targeted），并估计药物特异的混合分布。通过该模型可获得单个细胞系对药物敏感的后验概率（针对靶向效应）或效应大小（针对广谱效应）。案例分析显示：两个公共数据集的交叉部分存在中等程度的一致性；分析识别出携带EML4-ALK或NPM1-ALK基因融合的细胞对crizotinib敏感，并发现相关的细胞基质通路下调。本文属于应用统计建模，方法本身是已有的混合模型框架，但针对多源药物敏感性数据做了系统整合，对生物统计应用有参考价值。
- **关键技术**: `hierarchical mixture model`, `posterior probability`, `drug sensitivity assessment`, `multi-study data integration`, `Bayesian inference`
- **为什么对您有用**: 连接您secondary interest中的流行病学应用方向：本文利用多个公开药物基因组学数据集进行敏感性分析，其数据整合思路和建模框架可迁移到流行病学中的剂量-反应或生物标志物研究。技术武器库中的M估计理论（moderately_familiar）可用于分析层次混合模型的识别性和估计收敛性，非参数统计（very_familiar）可帮助理解其分布假设的稳健性。立即可做：您已具备的非参数统计和M估计背景可直接用于评估该模型假设的合理性，或将其应用于类似的流行病学数据。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

