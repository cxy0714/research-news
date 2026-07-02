# Epidemiology — Vol 36  Issue 2  ·  2026-06-24

- 共 11 篇 · Epidemiology
- 目录核对 ⚠️ 疑似漏 8 篇（对照 OpenAlex 21 篇）：10.1097/ede.0000000000001820、10.1097/ede.0000000000001807、10.1097/ede.0000000000001826、10.1097/ede.0000000000001812、10.1097/ede.0000000000001813 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期内容主要围绕**因果识别与偏差分析**、**流行病学数据结构处理**以及**环境与社会因素的描述性关联**三条主线展开。因果推断方面，聚焦于 APC 模型的非参数识别与测量误差的参数化校正；数据结构方面，重点讨论了多胞胎聚类与稀疏验证数据的处理；其余篇幅则为环境暴露、社会事件与健康结局的经典关联研究。

在因果识别与偏差分析主线，本期推进了对模型结构识别与测量误差的量化处理。**Age–Period–Cohort Models** 一文针对 APC 模型的线性识别难题，引入中介变量切断线性依赖路径，将 mechanism-based 方法推广至非参数情形，实现了因果效应的识别与 G-formula 估计；**Parameterization of Beta Distributions** 则针对二元暴露错误分类中的稀疏验证数据问题，比较了多种 Beta 先验设定，发现在零细胞频数出现时均匀先验能有效改善概率偏倚分析的覆盖概率。这两篇分别从模型结构识别和测量误差参数化角度，提供了具体的解决方案。

在流行病学数据结构与方法应用主线，本期关注特定数据结构对估计量的影响。**Accounting for Twins** 系统比较了围产期研究中处理多胞胎的不同策略（仅单胎、妊娠水平、婴儿水平聚类），指出了分析决策如何改变目标估计量及其解释；**Body Shapes of Multiple Anthropometric Traits** 利用 PCA 提取体型主成分并结合 Cox 模型分析死亡率，展示了高维人体测量数据的降维分析模板；**Influenza Activity and Preterm Birth** 则通过时间序列分析探讨了社区流感暴露与早产的关联。这些研究提示，数据结构的处理方式（如聚类、降维、时间层级）直接影响效应估计的有效性。

对于关注因果推断与半参数效率的研究者，建议优先阅读 **Age–Period–Cohort Models**（非参数识别与 G-computation）和 **Parameterization of Beta Distributions**（偏倚参数的先验设定）；对于关注数据结构与估计理论的研究者，**Accounting for Twins** 提供了关于分析单位与估计量定义的精彩讨论。

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1097/ede.0000000000001811](https://doi.org/10.1097/ede.0000000000001811) — A Generalization of the Mechanism-based Approach for Age–Period–Cohort Models
- **作者**: Arvid Sjölander, Erin E. Gabriel
- **期刊/来源**: Epidemiology
- **机构**: Karolinska Institutet · University of Copenhagen
- **分类**: vol 36 · issue 2 · pp 227-236
- 相关性 9/10 · novelty: `new_theory`
- **摘要**: 本文在年龄-时期-队列（APC）模型框架下，针对其固有的线性识别问题（age, period, cohort 的确定性线性关系导致效应不可识别），将已有的 mechanism-based 方法从参数情形推广到非参数情形。通过引入一组中介变量（mediators），作者在显式的数据生成机制假设下给出了年龄、时期、队列的因果效应的非参数识别条件，其核心思想是利用中介切断线性依赖路径。这一识别结果直接对应参数化 G-formula 估计，使得研究者可以仿照因果推断中的标准 G-computation 过程进行参数估计，类似处理时变混杂中的标准流程。作者证明了当中介变量满足排他性和一致性假设时，因果效应可识别，且估计量具有相合性。此前相关文献仅考虑特定参数设定，而本文提供了更一般化的理论保证，并且严格陈述了所需假设。本文对您的主要兴趣——因果推断中的识别和估计、尤其是中介分析和 longitudinal 设定（APC 本质上涉及时间维度）——直接相关，且涉及非参数识别理论（您的 moderately familiar 领域），可作为进一步探讨 APC 模型中交叉拟合或半参数效率界的基础。
- **关键技术**: `Mechanism-based approach`, `Nonparametric identification`, `G-formula (parametric)`, `Mediators for identifiability`, `Causal age-period-cohort effects`
- **为什么对您有用**: 本文直接连接您 primary interest 的因果推断——特别是中介分析和识别理论（moderately familiar 中的识别理论）。APC 模型的识别问题与纵向因果推断有深层联系，本文提供的非参数识别框架可为您后续使用半参数效率理论或 debiased ML 进行更高效估计提供起点。由于您对因果推断估计理论非常熟悉，本文提出的 G-formula 估计器可立即用您的 very_familiar 工具（非参数统计、估计理论）进行理解与扩展（例如引入 cross-fitting 或推导效率界），属于**立即可做**的 follow-up 方向。

## 流行病学  *(epidemiology, 10 篇)*

### 1. [10.1097/ede.0000000000001824](https://doi.org/10.1097/ede.0000000000001824) — Cold-related Mortality in US State and Private Prisons: A Case–Crossover Analysis
- **作者**: Julianne Skarha, Keith Spangler, David Dosa, Josiah D. Rich, David A. Savitz, Antonella Zanobetti
- **期刊/来源**: Epidemiology
- **机构**: Brown University · Boston University · Providence VA Medical Center · Providence College · Center for Health Justice · Harvard University
- **分类**: vol 36 · issue 2 · pp 207-215
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文使用病例交叉设计（case–crossover）分析2001–2019年美国州立和私立监狱中低温暴露与囚犯死亡率的关联。研究设定以冷季（11–3月）死亡事件为病例，利用条件逻辑回归估计温度每降低10°F及极端寒冷（低于第10百分位数）对总死亡、心脏病、呼吸疾病和自杀风险的滞后效应。结果显示，6天滑动平均温度每降低10°F对应总死亡率上升5.1%（95%CI: 2.1%–8.0%），极端冷日的10天累积效应使自杀风险增加55%（95%CI: 11%–114%）。效应修饰分析表明，1980年前建造、位于南部或西部、以及作为专门医疗设施的监狱中风险更高。作为流行病学领域典型的环境暴露与健康结局应用，本文在因果推断设计上利用了自身对照控制时间不变混杂，但方法学创新有限。对您有用：该研究展示了病例交叉设计在大型行政数据中的实施流程，可与您的因果推断识别假设与估计理论（如estimation theory in causal inference）对接，但本身不涉及新方法。
- **关键技术**: `case-crossover design`, `conditional logistic regression`, `distributed lag model`, `effect modification analysis`
- **为什么对您有用**: 本文属于流行病学应用，直接连接您的secondary interest中流行病学（应用、数据集、因果推断）子方向。该研究的病例交叉设计是经典自身对照方法，您可以用identification theory in causal inference（非常熟悉）解析其交换性假设，并用estimation theory分析条件逻辑回归的渐近行为。这是一篇高质量的入门读物，帮助熟悉流行病学常用因果设计的数据结构（多期、滞后效应），且武器库中的非参数/高维工具对于理解其结果报告（置信区间、累积效应）已足够，无需额外技能，可立即可读。

### 2. [10.1097/ede.0000000000001825](https://doi.org/10.1097/ede.0000000000001825) — The Association Between Ambient Particulate Matter Exposure and Anemia in HIV/AIDS Patients
- **作者**: Wei Liang, Aojing Han, Dong Hou, Ruihan Li, Qilin Hu, Huanfeng Shen et al.
- **期刊/来源**: Epidemiology
- **机构**: Wuhan University · Wuhan Donghu University · Yangzhou University · Xinjiang Uygur Autonomous Region Disease Prevention and Control Center · Zhongnan Hospital of Wuhan University
- **分类**: vol 36 · issue 2 · pp 216-226
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究 HIV/AIDS 患者中环境颗粒物（PM1、PM2.5、PM10）暴露与贫血之间的关联，数据来源于中国 HIV/AIDS 综合防治信息系统 2004–2021 年的 6808 名患者、36,266 次血红蛋白测量。方法上，短期暴露使用线性混合效应模型估计对 Hb 水平的影响，长期暴露分别用 logistic 回归估计基线贫血患病率关联、用 time-varying Cox 模型估计随访期间贫血发病风险，并进行了 CKD 的中介效应分析。主要结果显示：PM 暴露与 Hb 水平下降、贫血患病率和发病率上升显著相关，CKD 在 PM 诱导贫血中起部分中介作用。本文是典型的流行病学应用研究，方法学 novelty 有限，但提供了完整的纵向队列数据分析范例。
- **关键技术**: `linear mixed-effects model`, `time-varying Cox proportional hazards model`, `mediation analysis`, `logistic regression`, `longitudinal cohort study`
- **为什么对您有用**: (1) 本文属于 epidemiology secondary interest，展示了 environmental epidemiology 中纵向队列数据的常规分析流程（mixed model + time-varying Cox + mediation），可作为了解该领域数据分析范式的入门阅读。(2) 从方法学角度，本文未涉及 causal inference 的前沿 identification 或 sensitivity analysis 工具，武器库中的 identification theory / semiparametric theory / efficiency theory 在此无施展空间。(3) 作为 gateway reading，本文数据结构描述清晰、模型选择有代表性，但方法学贡献有限，建议快速浏览即可，无需精读全文。

### 3. [10.1097/ede.0000000000001822](https://doi.org/10.1097/ede.0000000000001822) — Examining the Interactive Associations of Cannabis and Alcohol Outlets With Self-harm Injuries in California: A Spatiotemporal Analysis
- **作者**: Rafael Charris, Jennifer Ahern, Dorie E. Apollonio, Victoria Jent, Laurie M. Jacobs, Shelley Jung et al.
- **期刊/来源**: Epidemiology
- **机构**: New York University · University of California, Berkeley · University of California, San Francisco · Lee University · Institute for Research and Evaluation · Pacific Institute For Research and Evaluation
- **分类**: vol 36 · issue 2 · pp 196-206
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究加州 2017–2019 年间娱乐用大麻零售店和酒精销售点的密度与自伤率（致命与非致命）的时空关联，estimand 是 outlet density 变化对自伤率的风险差。方法上采用贝叶斯时空模型，在 ZIP code 季度层面建模，控制混杂并处理空间自相关，从后验分布估计假设性干预（如减少 20% 酒精销售点）的效应。主要发现：大麻零售店的开业与自伤率无显著关联，且与酒精销售点密度无交互作用；但酒精销售点密度降低 20% 与非致命自伤率下降相关（风险差 −1.59/10 万人，95% CI: −2.60, −0.59）。这是一篇典型的流行病学应用研究，方法学 novelty 有限，但提供了完整的州级时空数据和分析范例。
- **关键技术**: `Bayesian spatiotemporal modeling`, `spatial autocorrelation`, `risk difference estimation`, `posterior predictive inference`, `ZIP code-level longitudinal data`
- **为什么对您有用**: (1) 属于流行病学 secondary interest 的应用因果研究，展示了时空数据中处理空间自相关的贝叶斯建模策略；(2) 武器库中的 identification theory in causal inference 可用于审视其假设性干预（counterfactual outlet density）的识别条件是否充分——本文本质是关联性分析而非严格因果，混杂控制依赖可观测协变量；(3) 作为 gateway reading 值得一读：数据结构清晰、模型设定明确，但方法学深度有限，适合了解流行病学时空分析的标准范式，不必花时间精读全文。

### 4. [10.1097/ede.0000000000001818](https://doi.org/10.1097/ede.0000000000001818) — Parameterization of Beta Distributions for Bias Parameters of Binary Exposure Misclassification in Probabilistic Bias Analysis
- **作者**: Qi Zhang, Richard F. MacLehose, Lindsay J. Collin, Thomas P. Ahern, Timothy L. Lash
- **期刊/来源**: Epidemiology
- **机构**: Emory University · Methodist University · University of Minnesota · University of Utah · Huntsman Cancer Institute · University of Vermont
- **分类**: vol 36 · issue 2 · pp 237-244
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文探讨在概率偏倚分析中处理二元暴露错误分类时，对偏倚参数（阳性预测值和阴性预测值）的Beta分布参数化方法。当内部验证子样本出现零细胞频数时，传统方法会导致极端的偏倚校正估计。作者模拟了不同规模的队列研究，比较了五种方法：无先验的传统法、均匀先验（Beta(1,1)）、Jeffreys先验（Beta(0.5,0.5)）、仅零细胞时使用Jeffreys连续性校正、仅零细胞时使用均匀连续性校正。模拟结果显示，在稀疏验证数据时，施加先验或连续性校正的方法均改善了覆盖概率和均方误差，其中均匀先验表现最佳；当无零细胞时各方法差异很小。结论是若预测验证数据稀疏，使用均匀先验可提高偏倚调整的有效性。该研究为流行病学中暴露错误分类的灵敏度分析提供了具体操作建议，与因果推断中测量误差问题的校正思路直接相关。
- **关键技术**: `probabilistic bias analysis`, `beta distribution`, `prior distributions`, `continuity correction`, `validation substudy`, `simulation study`
- **为什么对您有用**: 本文属于流行病学应用方向，直接对应研究者secondary interests中的流行病学数据分析和因果推断中的暴露测量误差问题。研究者可运用very_familiar的‘因果推断估计理论’来审视本文的假设（如非差错误分类）并理解其识别条件，同时可用‘软件工具’快速复现模拟代码。由于方法简单且已有明确比较结果，属于‘立即可做’的范畴——无需新工具即可评估其对自身因果推断项目的适用性。

### 5. [10.1097/ede.0000000000001815](https://doi.org/10.1097/ede.0000000000001815) — The Recent Rise in Homicide: An Analysis of Weekly Mortality Data, United States, 2018–2022
- **作者**: Michelle Degli Esposti, Terry L. Schell, Rosanna Smart
- **期刊/来源**: Epidemiology
- **机构**: University of Michigan · RAND Corporation
- **分类**: vol 36 · issue 2 · pp 174-182
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文利用美国国家生命统计系统2018-2022年每周死亡率数据，对凶杀率在COVID-19疫情前后的变化趋势进行了描述性流行病学分析。研究将凶杀分为持枪与非持枪两类，通过季节性调整和平滑处理，量化了不同时间点（疫情宣布、乔治·弗洛伊德事件、2020大选）前后的变化幅度，并按社会人口学特征和地理区域进行分层。主要发现：持枪凶杀率在此期间上升了54%，而非持枪凶杀率保持稳定；上升趋势始于2019年10月，在2020年11月趋于平稳；至疫情被宣布为国家紧急状态时，已有28%的增幅发生。所有社会人口学和地理群体均经历了大幅增长。结论认为，现有理论（如疫情）不足以解释此次以持枪凶杀为主的、始于2019年底的全域性激增。作为流行病学领域的实证数据集和趋势分析方法案例，本文为研究者提供了真实世界死亡率数据的分析管道和季节性调整应用实例，但其统计方法较为基础（描述性统计+平滑），方法学新颖性较低。
- **关键技术**: `seasonal adjustment`, `smoothing`, `descriptive epidemiology`, `stratified trend analysis`, `National Vital Statistics System`
- **为什么对您有用**: 本文属于流行病学应用类论文，直接对应您的二级兴趣；提供了美国国家级死亡率数据集的公开来源和分析流程模板，可作为您进入流行病学真实数据领域的入门读物。现有武器库（非参数统计、高维渐近）难以直接应用于此类低维描述性分析，但其中关于枪杀特异性、季节模式调整的发现可能启发因果推断中控制混淆变量的设计。整体而言，本文方法学简单，暂不可做方法拓展，但作为了解流行病学数据结构和分析习惯的窗口，值得短时间浏览。

### 6. [10.1097/ede.0000000000001817](https://doi.org/10.1097/ede.0000000000001817) — Association of Early-life Trauma With Gestational Diabetes and Hypertensive Disorders of Pregnancy
- **作者**: Sharonda M. Lovett, Jennifer M. P. Woo, Katie M. O’Brien, Samantha E. Parker, Dale P. Sandler
- **期刊/来源**: Epidemiology
- **机构**: Boston University · National Institute of Environmental Health Sciences · TCL (China)
- **分类**: vol 36 · issue 2 · pp 149-159
- 相关性 4/10 · novelty: `application`
- **摘要**: 本研究利用Sister Study队列（34,879名经产妇女）评估18岁前创伤经历与妊娠糖尿病（GDM）及妊娠高血压疾病（HDP）的关联。暴露通过改编的简短背叛创伤量表在第一轮随访时测量，结局为自我报告的GDM和HDP史。使用对数二项回归估计相对风险（RR），并通过潜在类别分析处理创伤的共病模式。调整混杂后，任何早期创伤与GDM的RR=1.1（95% CI: 1.0-1.3），与HDP的RR=1.2（95% CI: 1.2-1.3）。在潜在类别分析中，高创伤类别的GDM风险升高（RR=1.9, 95% CI: 1.5-2.6），HDP风险升高（RR=1.7, 95% CI: 1.4-2.0）。结论支持早期创伤增加不良妊娠结局风险的假说。本文是流行病学中暴露测量与结局关联的典型应用，其数据结构和分析流程（自我报告暴露、潜在类别建模、混淆调整）对统计学家理解观察性研究设计具有参考价值。
- **关键技术**: `log-binomial regression`, `latent class analysis`, `relative risk estimation`, `self-reported exposure measurement`
- **为什么对您有用**: 本文属于流行病学应用方向，直接对应研究者的secondary interest（流行病学数据集和因果推断应用）。其使用潜在类别分析处理多重共病暴露，研究者已有的非参数统计和因果推断背景（如识别假设和混淆调整）足以理解核心方法。作为流行病学入门级读物，本文清晰展示了队列研究的数据结构、暴露测量和结局定义，值得花时间读全文以获取实际分析思路和数据集灵感。

### 7. [10.1097/ede.0000000000001819](https://doi.org/10.1097/ede.0000000000001819) — Influenza Activity and Preterm Birth in the Atlanta Metropolitan Area: A Time-Series Analysis from 2010 to 2017
- **作者**: Xiaping Zheng, Tingyu Wang, Hua Hao, Rohan R. D’Souza, Matthew J. Strickland, Joshua L. Warren et al.
- **期刊/来源**: Epidemiology
- **机构**: Emory University · University of Nevada, Reno · Yale University
- **分类**: vol 36 · issue 2 · pp 141-148
- 相关性 4/10 · novelty: `application`
- **摘要**: 该研究通过时间序列分析探究社区流感活动与早产风险之间的短期关联。研究使用2010-2017年亚特兰大市区316,253例出生数据，以四种方式定义流感暴露（病毒检测阳性率、ILI门诊比例、复合指标、住院率），并采用Poisson log-linear模型调整时变混杂及在孕人口。结果显示，复合暴露指标每增加一个IQR，同周早产风险增加1.014倍（95%CI: 1.001-1.027），且效应在已婚、非黑人及西班牙裔孕妇中更显著。方法上利用多种暴露度量和滞后结构进行稳健性检验，但未涉及个体层面混杂或因果推断框架。对于从事因果推断应用的研究者，这是一个典型的生态学时间序列研究，其局限性（如未测量混杂、聚合偏倚）恰好提供了使用proximal causal inference或工具变量方法进行敏感性分析的切入点。
- **关键技术**: `time-series analysis`, `Poisson log-linear model`, `composite exposure measure`, `exposure lag`, `effect modification`
- **为什么对您有用**: 本文属于流行病学应用领域，是研究者secondary interest的具体实例，展现了时间序列设计在环境暴露-健康效应研究中的典型分析流程。研究者可以利用自己在因果推断估计理论方面的专长（very_familiar），针对该设计中未测量混杂问题提出更严格的识别策略或进行敏感性分析，这是立即可做的方向。同时，该研究的暴露度量和数据处理细节为后续方法论验证提供了现实数据集。

### 8. [10.1097/ede.0000000000001809](https://doi.org/10.1097/ede.0000000000001809) — Accounting for Twins and Other Multiple Births in Perinatal Studies of Live Births Conducted Using Healthcare Administration Data
- **作者**: Jeremy P. Brown, Jennifer J. Yland, Paige L. Williams, Krista F. Huybrechts, Sonia Hernández-Díaz
- **期刊/来源**: Epidemiology
- **机构**: Harvard University · In-Q-Tel · Brigham and Women's Hospital
- **分类**: vol 36 · issue 2 · pp 165-173
- 相关性 4/10 · novelty: `application`
- **摘要**: 本研究聚焦围产期研究中双胞胎或多胎分娩的数据分析方法比较，常见策略包括: 仅保留单胎、在妊娠水平上计数（至少一个双胞胎出现结局则计为1）、以及在婴儿水平上考虑聚类（如GEE或混合效应模型）。作者通过蒙特卡洛模拟、代数公式和MarketScan保险数据实例，系统展示不同策略对应不同的目标估计量、假设条件与实际结论。结果指出，在诊断结果常被错误分配给单一婴儿标识的管理数据库中，不得已的选择（限制单胎或妊娠水平分析）会显著影响效应估计的幅度与方向。对于流行病学应用统计研究者，此文是一个极好的对照案例: 看似微小的分析决策（如处理多胞胎的方式）可能改变估计量的解释，而这恰是用户'估计理论'和'因果推断'武器库中 estimand 概念的直接应用场景。
- **关键技术**: `Monte Carlo simulation`, `algebraic formulas`, `generalized estimating equations (GEE)`, `mixed effects models`, `singleton restriction`, `pregnancy-level analysis`
- **为什么对您有用**: (1) 连接到流行病学中的真实数据分析问题（MarketScan数据库），与用户secondary interest中的流行病学应用因果工作高度相关。(2) 用户武器库中 very_familiar 的 'estimation theory in causal inference' 可直接用于批判性评估文中各策略的 estimand 定义及其假设合理性，moderately_familiar 的 'identification theory in causal inference' 可用于评价因果解释的效度。(3) 立即可做——无需额外学习新工具，用户已有的估计理论和流行病学基础足以读懂论文并产出审读意见。

### 9. [10.1097/ede.0000000000001810](https://doi.org/10.1097/ede.0000000000001810) — Body Shapes of Multiple Anthropometric Traits and All-cause and Cause-specific Mortality in the UK Biobank
- **作者**: Patricia Bohmann, Michael J. Stein, Andrea Weber, Julian Konzok, Emma Fontvieille, Laia Peruchet-Noray et al.
- **期刊/来源**: Epidemiology
- **机构**: University of Regensburg · Centre international de recherche sur le cancer · Universitat de Barcelona · Inserm · Centre Léon Bérard · University Hospital Regensburg
- **分类**: vol 36 · issue 2 · pp 264-274
- 相关性 3/10 · novelty: `application`
- **摘要**: 本研究利用 UK Biobank 中 462,301 名成年人的数据，通过主成分分析（PCA）从 BMI、身高、体重、腰围、臀围和腰臀比中提取了四种体型特征。采用多变量调整的 Cox 比例风险模型估计体型主成分得分与全因及特定病因死亡率之间的风险比。结果显示，一般肥胖体型与死亡风险呈 U 型关联；高大中心性肥胖体型呈剂量反应式的风险增加（HR=1.16, 95%CI=1.14-1.18）；而高大瘦削或运动体型则未见增加风险。该研究使用的大规模前瞻性队列和标准生存分析方法，为流行病学中体型与死亡率关联提供了典型分析模板。对您作为熟悉高维统计与因果推断的研究者而言，本文可作为理解 UK Biobank 数据结构和常用流行病学方法的入门读物。
- **关键技术**: `Principal Component Analysis`, `Cox proportional hazards model`, `UK Biobank`, `anthropometric traits`, `multivariable adjustment`
- **为什么对您有用**: 本文是流行病学领域应用队列数据研究体型与死亡率的实证分析，对统计学家而言是一篇清晰的入门读物，详细展示了 UK Biobank 的数据结构、PCA 变量降维和 Cox 模型调整策略。研究者已有的高维统计和估计理论经验足以理解并批判性评估其方法学选择。如果未来计划涉足流行病学合作或使用 UK Biobank 数据，值得花时间阅读全文以熟悉常见分析流程。

### 10. [10.1097/ede.0000000000001823](https://doi.org/10.1097/ede.0000000000001823) — Validation of Lactational Mastitis Diagnosis Codes in Electronic Health Care Data
- **作者**: Malini B. DeSilva, Elisabeth M. Seburg, Kirsten Ehresmann, Gabriela Vazquez-Benitez, Yihe G. Daida, Kimberly K. Vesco et al.
- **期刊/来源**: Epidemiology
- **机构**: HealthPartners · Kaiser Permanente · Kaiser Permanente Center for Health Research
- **分类**: vol 36 · issue 2 · pp 160-164
- 相关性 2/10 · novelty: `application`
- **摘要**: 该研究旨在验证电子健康记录中哺乳期乳腺炎诊断代码（ICD-10-CM代码N61.0和O91.2）的阳性预测值（PPV）。在三个医疗系统中纳入2020年12月至2022年9月分娩且有哺乳记录的19,660名患者，通过医疗记录审查确认诊断。对119份随机抽样的疑似病例进行审查，评估“很可能”（乳房症状伴全身症状）和“可能”（仅乳房症状）的乳腺炎定义。结果显示，仅代码的PPV为76%（很可能）和97%（很可能或可能）；添加抗生素处方后PPV提高至80%和100%，但病例数减少。研究结论是诊断代码单独使用具有较好的PPV，抗生素数据可进一步改善准确性，但会降低敏感性。该研究为流行病学中诊断代码验证提供了具体范例，其PPV估计方法可直接应用于其他疾病代码验证场景。
- **关键技术**: `Positive Predictive Value (PPV)`, `ICD-10-CM coding validation`, `Electronic health record (EHR) data`, `Medical record review`, `Confidence interval estimation`
- **为什么对您有用**: 该论文直接对应您的二级兴趣——流行病学应用，展示了如何使用医疗记录审查来验证诊断代码的有效性。您武器库中的‘estimation theory in causal inference’（如置信区间构造）可用于批判性评估本文PPV估计的精密度；同时，该验证设计可作为您将来处理流行病学数据集中的测量误差问题的入门参考。属于值得一读的应用典范。

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

