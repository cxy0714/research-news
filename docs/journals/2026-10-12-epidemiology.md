# Epidemiology  ·  2026-10-12

- 共 12 篇 · Epidemiology

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期以流行病学应用与方法学为主，12篇论文大致可归为四条主线：一是因果识别与偏倚校正（PrEP启动后STI诊断率变化、nirsevimab免疫规划效果评估、外部有效性中的碰撞偏倚），二是预测模型与标志物的可移植性（预后标志物跨人群移植），三是疾病负担与监测系统的估计方法（患病数间接估计、职业死亡监测敏感性、SEER与Medicare数据源比较），四是暴露-结局关联的环境与行为流行病学（超细颗粒物与神经退行性疾病死亡、动物养殖场暴露与早产、饮食模式与不良妊娠结局、青少年风险行为网络分析、挪威胎儿婴儿死亡率长期趋势）。

最突出的主线是因果推断在流行病学中的应用，且各篇对偏倚来源的处理方式形成互补。PrEP研究采用自我对照病例系列设计，结合贝叶斯模型推导零假设下的预期诊断率，将筛查频率变化从行为风险补偿中分离出来，量化了诊断偏倚对IRR的贡献（80-81%的增幅归因于无症状筛查增加）；nirsevimab评估则用双重差分配合恒定住院比例反事实方法，以非适龄组时间趋势为对照，估计RSV住院下降59%。这两篇共同展示了在非随机干预场景下，如何利用设计选择与反事实建模逼近因果效应。外部有效性那篇则从理论层面切入，区分效应修饰因子与样本成员关系的方向，指出后者条件下调整EMM可能因碰撞分层引入偏倚，并引入“选择依赖”调整集概念——与PrEP和nirsevimab中处理的选择偏倚形成理论呼应。

另一条值得注意的主线是监测系统与数据源评估。职业死亡监测研究用逆概率加权外推抽样漏报，估计总体敏感性仅67.8%，并发现按死亡意图和种族的异质性；SEER与Medicare数据源比较则用kappa统计量量化两种数据源在评估治疗充分性上的不一致。这两篇都指向同一问题：基于行政或登记数据的流行病学结论对数据生成机制的敏感性。此外，预后标志物可移植性一文从充分组分病因框架重新推导预测值可移植的隐含假设，提出“公正”假设下的新移植方法，与外部有效性那篇在“人群间外推”主题上形成跨方法对话。

与因果推断、半参数效率、高维方向最贴的优先看：PrEP诊断偏倚量化、nirsevimab双重差分评估、外部有效性碰撞偏倚分析、预后标志物可移植性。若关注监测系统方法，职业死亡敏感性估计与SEER-Medicare数据源比较也值得一读。

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1097/ede.0000000000002048](https://doi.org/10.1097/ede.0000000000002048) — Understanding potential collider bias in external validity analysis depending on types of effect measure modifiers
- **作者**: Fabian Manke-Reimers, Vincent Brugger, Michael Webster-Clark
- **期刊/来源**: Epidemiology
- **机构**: Heidelberg University · Medizinische Fakultät Mannheim · University of North Carolina at Chapel Hill · Wake Forest University Health Sciences · Wake Forest University · McGill University
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 本文研究外部有效性分析中协变量选择的问题，特别是效应修饰因子（EMM）与样本成员关系方向对充分调整集的影响。作者区分了两种场景：样本成员由EMM导致（如社会人口学影响试验参与概率）与EMM由样本成员导致（如试验参与效应），并指出前者条件下调整EMM不会引入偏倚，而后者可能因碰撞分层（collider conditioning）使样本成员成为新的EMM，从而产生碰撞偏倚。通过模拟实验，作者展示了碰撞偏倚的大小取决于碰撞变量关联强度、交互作用强度及样本量，并引入“选择依赖”（s-dependent）调整集的概念。文章强调，弱交互和弱关联可能不足以产生实质性偏倚，但研究者应明确EMM与样本成员间的因果方向以避免碰撞偏倚。该研究为外部有效性分析中的协变量选择提供了新的理论指导，对因果推断中transportability和generalizability的实践有直接意义。
- **关键技术**: `causal directed acyclic graphs (DAGs)`, `collider bias`, `effect measure modification`, `external validity analysis`, `simulation study`
- **为什么对您有用**: 本文直接关联您的因果推断兴趣，特别是外部有效性（transportability/generalizability）中的识别与偏倚问题。您可以用very_familiar的因果推断估计理论来审视其模拟设计，或进一步用DAG工具扩展其理论结果。中期可做：结合您的identification theory in causal inference（moderately_familiar）来形式化s-dependent调整集的充分性条件。

## 流行病学  *(epidemiology, 11 篇)*

### 1. [10.1097/ede.0000000000002044](https://doi.org/10.1097/ede.0000000000002044) · [arXiv](https://arxiv.org/abs/2511.04065) — Transportability of Prognostic Markers
- **作者**: Mohsen Sadatsafavi, Gavin Pereira, Wenjia Chen
- **期刊/来源**: Epidemiology
- **机构**: University of British Columbia · St. Paul's Hospital · Centre for Heart Lung Innovation · State University of Malang · Curtin University · National University of Singapore
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文从充分组分病因（sufficient-component cause）框架重新审视预后标志物（prognostic markers）的可移植性（transportability），即预测模型在不同人群中保持性能的能力。作者指出，直接移植标志物隐式假设预测值（predictive values）可移植，而常规的患病率校正则将可移植性转移至灵敏度与特异度等准确性指标。通过将风险预测分解为因果组分，作者证明这两种方法都依赖于关于病因分布稳定性的强假设。在仅知结局患病率而无外部信息时，作者提出一种“公正”假设，即所有病因共同导致患病率变化，由此导出新的标志物移植方法。数值实验表明，不同可移植性假设导致不同程度的信息损失，取决于病因在不同人群中的分布。该文挑战了标志物可移植性的常见假设与实践，并基于病因变化的显式假设提出了新方法。对您而言，本文是流行病学中因果框架应用于预测模型外部验证的典型范例，可作为入门读物，但方法学贡献有限。
- **关键技术**: `sufficient-component cause framework`, `prevalence adjustment`, `sensitivity and specificity`, `risk prediction decomposition`, `numerical experiments`
- **为什么对您有用**: 本文属于流行病学应用，涉及因果推断框架（充分组分病因）在预测模型可移植性中的应用，与您的流行病学应用兴趣相关。作为入门读物，本文对因果框架的阐述清晰，但方法学深度一般。您的武器库（如因果推断识别理论）足以理解本文，但无需深入跟进。

### 2. [10.1097/ede.0000000000002052](https://doi.org/10.1097/ede.0000000000002052) — Enhanced screening and bacterial sexually-transmitted infection diagnoses after HIV pre-exposure prophylaxis initiation
- **作者**: Anna M. Parker, Samuel M. Jenness, Benjamin J. Singer, Jennifer J. Chang, Katia J. Bruxvoort, Joseph A. Lewnard
- **期刊/来源**: Epidemiology
- **机构**: Berkeley Public Health Division · University of California, Berkeley · Emory University · Los Angeles Medical Center · University of Alabama at Birmingham · Center for Information Technology Research in the Interest of Society
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文研究 HIV PrEP 启动后淋病和衣原体诊断率升高的原因，区分行为风险补偿与筛查频率增加导致的诊断偏倚。采用自我对照病例系列设计，比较 PrEP 启动前后诊断率，并利用贝叶斯框架下的数学模型推导零假设下的预期诊断率。结果显示启动后诊断率显著升高（淋病 IRR=3.47，衣原体 IRR=3.59），但校正筛查频率后，实际诊断率仅比零假设预期高 8-14%，估计 80-81% 的增幅归因于无症状筛查增加。该研究为流行病学中诊断偏倚的量化提供了方法学范例，对您关注的应用因果推断方向有参考价值。
- **关键技术**: `self-controlled case series`, `Bayesian model`, `matched incidence rate ratio`, `diagnostic bias adjustment`, `screening frequency modeling`
- **为什么对您有用**: 本文属于流行病学应用因果推断，直接关联您的 secondary interest 中的流行病学方向。其核心方法——用数学模型量化筛查偏倚——可视为一种敏感性分析，您可用 very_familiar 的因果推断估计理论来审视其识别假设（如无未测量混杂）是否成立，属于立即可做的批判性阅读。

### 3. [10.1097/ede.0000000000002049](https://doi.org/10.1097/ede.0000000000002049) — Indirect Estimation of the Number of Prevalent Cases – Relaxing the Steady State Assumption
- **作者**: W. Dana Flanders, Michael Goodman, Cathy Lally
- **期刊/来源**: Epidemiology
- **机构**: Emory University
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文针对流行病学中常用的间接估计患病数公式（患病数=年发病数×平均病程）依赖稳态假设、现实中常不成立的问题，推导了一个替代公式，将患病数与一段时间内的发病数、平均病程和病程均方联系起来。该公式不要求稳态假设，只需发病数随时间近似线性变化。作者通过示例说明公式的使用，并指出结果对用于估计发病线性趋势的时间段数量具有一定稳健性。本文是应用导向的方法学贡献，为流行病学中的疾病负担估计提供了更灵活的间接估计工具。对您而言，该公式的推导和稳健性分析思路可能对您关注的流行病学应用中的因果推断或纵向数据建模有参考价值。
- **关键技术**: `indirect estimation`, `prevalence-incidence relation`, `steady-state relaxation`, `linear trend approximation`
- **为什么对您有用**: 本文属于流行病学应用领域，是您次要兴趣之一。作为入门读物，它清晰展示了流行病学中常见估计问题的设定和解决思路，但方法学深度有限，武器库足以理解。是否值得读全文取决于您对流行病学间接估计方法的兴趣，可作为了解该领域数据建模问题的窗口。

### 4. [10.1097/ede.0000000000002054](https://doi.org/10.1097/ede.0000000000002054) — Long-term exposure to ultrafine particles and mortality from neurodegenerative diseases: a population-based cohort study
- **作者**: Emmanuelle Batisse, Marshall Lloyd, Christel Renoux, Arman Ganji, Junshi Xu, Marianne Hatzopoulou et al.
- **期刊/来源**: Epidemiology
- **机构**: McGill University Health Centre · McGill University · Jewish General Hospital · Centre de Santé et de Services Sociaux de la Montagne · University of Toronto
- 相关性 6/10 · novelty: `application`
- **摘要**: 这是一项基于加拿大人口队列（CanCHECs）的流行病学研究，旨在估计长期暴露于超细颗粒物（UFP，<0.1μm）与神经退行性疾病死亡率（痴呆、帕金森病、肌萎缩侧索硬化）之间的关联。研究纳入蒙特利尔和多伦多2001-2019年约210万成年人，通过居住邮编分配高分辨率UFP数浓度和粒径的三年移动平均值作为暴露。使用Cox比例风险模型估计风险比（HR），并采用逆概率删失加权处理竞争事件，同时调整UFP粒径、社会人口因素和共污染物。结果显示，UFP数浓度每增加10,000颗粒/cm³，痴呆死亡率增加22%（HR=1.22, 95% CI: 1.17–1.27），其中血管性痴呆关联最强（HR=1.49），但对帕金森病和ALS无显著效应。该研究提供了UFP暴露与痴呆死亡关联的流行病学证据，其分析模式（队列、暴露评估、竞争风险）对您关注的流行病学应用因果推断具有参考价值。
- **关键技术**: `Cox proportional hazards model`, `inverse probability of censoring weighting`, `competing risks`, `residential exposure assessment`, `moving average exposure`
- **为什么对您有用**: 本文属于流行病学应用研究，直接对应您的secondary interest中的流行病学队列研究。其使用Cox模型和逆概率加权处理竞争风险，是因果推断中处理删失的常用方法，您可以用very_familiar的估计理论来审视其加权估计的稳健性。作为gateway reading，本文数据和分析流程清晰，适合作为流行病学队列研究的入门读物，但方法学新颖性有限，不值得深入挖掘。

### 5. [10.1097/ede.0000000000002051](https://doi.org/10.1097/ede.0000000000002051) — Evaluating Data Sources for Monitoring Guideline-Concordant Endometrial Cancer Treatment Among Older Adults
- **作者**: Caitlin E. Meade, Jennifer A. Sinnott, Simran A. Kanal, Allison M. Quick, Kemi M. Doll, Ashley S. Felix
- **期刊/来源**: Epidemiology
- **机构**: Wake Forest University Health Sciences · Wake Forest University · The Ohio State University · The Ohio State University Comprehensive Cancer Center – Arthur G. James Cancer Hospital and Richard J. Solove Research Institute · University of Washington
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文比较了基于 SEER 登记数据与基于 Medicare 索赔数据评估老年子宫内膜癌患者指南一致性治疗（guideline-concordant treatment）的差异。SEER 仅记录是否接受推荐治疗方式，而索赔数据还能捕捉治疗的充分性（如时机、周期数、放疗次数、持续时间）。研究使用 SEER-Medicare 关联数据，对 2000-2019 年诊断的 29,209 名手术患者和 14,372 名辅助治疗患者，分别按 NCCN 指南评估一致性，并用 kappa 统计量衡量两种数据源的一致性。结果显示 SEER 评估的一致性比例显著高于索赔数据（手术：88.2% vs 79.8%；辅助治疗：85.4% vs 71.6%），且两者一致性仅为中等（kappa≈0.46-0.47）。结论是仅依赖登记数据的治疗字段可能高估指南一致性，因为未考虑治疗充分性。对您而言，这是一篇典型的流行病学应用研究，展示了数据源选择对测量偏倚的影响，可作为因果推断中测量误差问题的实例。
- **关键技术**: `kappa statistics`, `SEER-Medicare linked data`, `claims-based treatment adequacy`, `guideline concordance assessment`
- **为什么对您有用**: 本文属于流行病学应用研究，涉及数据源比较和测量误差，与您的流行病学应用兴趣相关。作为 gateway reading，它清晰展示了健康数据结构和测量问题，但方法学上较为常规（kappa 一致性），武器库足以理解。值得花时间读全文以了解 SEER-Medicare 数据细节，但无需深入方法学。

### 6. [10.1097/ede.0000000000002046](https://doi.org/10.1097/ede.0000000000002046) — Association Between Proximity to Animal Agriculture During Pregnancy and Spontaneous Preterm Birth Among Nulliparous Women in a California Cohort
- **作者**: Saskia Comess, Joshua L. Warren, Gary M. Shaw, Daniel E. Ho
- **期刊/来源**: Epidemiology
- **机构**: Stanford University · Yale University
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文利用加州 2007–2011 年 811,953 例初产妇出生队列，研究孕期居住地附近动物养殖场（CAFO）暴露与自发性早产（极早产 20–31 周、中早产 32–36 周）的关联。暴露变量基于距离、密度和风向加权，采用时间-事件（Cox 比例风险）和贝叶斯模型估计风险比和优势比，并调整了母亲、时间、社会经济和环境协变量。贝叶斯模型同时推断关联的距离范围和强度，发现逆距离每单位增加对应极早产调整风险比 1.007（95% CI: 1.002–1.012），下风向加权暴露更强（1.043）。贝叶斯结果显示，居住地 25.23 km 内有至少一个 CAFO 的孕妇极早产优势比为 1.16（95% HDI: 1.10–1.22），且距离范围类似但中早产优势比更小。结论认为 CAFO 暴露可能增加早产风险，尤其对极早产和主导下风向暴露。对您而言，这是一项流行病学应用研究，其暴露测量和贝叶斯空间建模思路可迁移至您关注的因果推断中的暴露-结局关联分析。
- **关键技术**: `time-to-event analysis`, `Bayesian hierarchical models`, `wind-based exposure weighting`, `inverse distance weighting`, `confounder adjustment`
- **为什么对您有用**: 本文属于流行病学应用研究，直接对应您的 secondary interest 中的流行病学方向。其暴露变量构造（距离、密度、风向加权）和贝叶斯建模框架，可启发您在因果推断中处理连续暴露和空间相关性的方法。从技术武器库看，您熟悉的估计理论（如 IPW、DR 估计）可用于评估其调整协变量后的因果解释，但本文未使用工具变量或敏感性分析，您可考虑用 IV 或负对照方法加强因果推断。总体而言，本文作为流行病学应用案例，值得阅读以了解数据结构和分析流程，但方法学新颖性有限。

### 7. [10.1097/ede.0000000000002053](https://doi.org/10.1097/ede.0000000000002053) — Occupational Fatality Data Systems: A Sensitivity Analysis of North Carolina Data Systems for Occupational Fatality from 1992-2017
- **作者**: Catherine S Wolff, Chelsea Leonard Martin, Maryalice Nocera, Shabbar I Ranapurwala, David B Richardson, Elizabeth S McClure et al.
- **期刊/来源**: Epidemiology
- **机构**: Harborview Injury Prevention and Research Center · University of North Carolina at Chapel Hill · University of California, Irvine · Samueli Institute · Irvine University
- 相关性 5/10 · novelty: `application`
- **摘要**: 本研究旨在评估北卡罗来纳州1992-2017年职业死亡监测系统的敏感性，即OCME数据系统和死亡证明对职业死亡的识别能力。研究者从OCME数据中抽取非职业死亡的5%样本（偶数年），经裁定后识别出41例被误分类的职业死亡，并利用抽样分数的逆概率外推至全部人群，估计约有1520例职业死亡被漏报，总体敏感性为67.8%（95% CI: 66.5%-69.1%）。敏感性因死亡意图和方式而异：非故意驾驶相关死亡为62.1%，非驾驶非故意死亡为73.5%，故意死亡为61.3%；按种族分，黑人死者为63.2%，白人死者为66.9%。结论指出职业死亡监测系统存在显著漏报，尤其对非故意驾驶和故意死亡事件以及黑人死者，提示需要改进分类和报告流程。对您而言，本文展示了流行病学中基于抽样设计和逆概率加权的敏感性分析方法，可作为应用因果推断中测量误差校正的实例，与您的流行病学应用兴趣相关。
- **关键技术**: `inverse probability weighting`, `sensitivity analysis`, `sampling design`, `misclassification correction`
- **为什么对您有用**: 本文属于流行病学应用，使用逆概率加权估计监测系统敏感性，方法简单但可迁移；作为gateway reading，它清晰展示了流行病学中数据质量评估的统计思路，武器库中的非参数统计和因果推断知识足以理解；值得花时间读全文以了解实际数据结构和分析流程。

### 8. [10.1097/ede.0000000000002045](https://doi.org/10.1097/ede.0000000000002045) — Adolescent Interplay of Adversity and Risk: An Ising Network Analysis of the 2023 Youth Risk Behavior Survey
- **作者**: Diego A. Díaz-Faes, Sonali Rajan, Charles C. Branas
- **期刊/来源**: Epidemiology
- **机构**: Columbia University
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文利用2023年美国青少年风险行为调查（YRBS，N=20,103）的26个指标，构建Ising网络模型，考察不良童年经历、受害、自杀行为、物质使用和暴力五个领域间的条件关联。研究计算节点强度和桥接强度中心性，并通过网络比较检验（NCT）评估性别、性取向和种族/民族亚组间的网络不变性。结果显示网络稳定且整体连通性高，自杀意念、照护者情感虐待和无望感具有最高节点强度，无望感、肢体冲突和携带枪支是跨领域桥接的关键变量。亚组比较发现网络结构大体相似，但黑人与白人受访者间存在最显著的结构差异。作者指出这些关联可能反映级联过程，为未来因果假设提供线索，但本文本质是描述性网络分析，未涉及因果识别或推断方法。对您而言，本文可作为流行病学中网络分析应用的入门读物，但其方法学新颖性有限，与您的因果推断或高维统计兴趣关联较弱。
- **关键技术**: `Ising network model`, `node strength centrality`, `bridge centrality`, `Network Comparison Test`, `bootstrapped stability analysis`
- **为什么对您有用**: 本文属于流行病学应用，使用网络分析处理横断面调查数据，可作为流行病学数据结构和常见分析流程的入门读物；但方法学上未涉及因果推断或高级统计，与您的主要兴趣（如proximal CI、DML）无直接交集。武器库足以理解其方法，但无需深入；若您想了解流行病学中网络分析的现状，可快速浏览，否则不值得花时间精读。

### 9. [10.1097/ede.0000000000002047](https://doi.org/10.1097/ede.0000000000002047) — Association between high fat, sugar, and sodium diet and adverse pregnancy outcomes, modified by fruit and vegetable intake density
- **作者**: Ya-Hui Yu, Lisa M. Bodnar, Sharon I. Kirkpatrick, Sara M. Parisi, Ashley I. Naimi
- **期刊/来源**: Epidemiology
- **机构**: Emory University · University of Pittsburgh · University of Waterloo
- 相关性 5/10 · novelty: `application`
- **摘要**: 本研究利用 Nulliparous Pregnancy Outcomes Study 的 8,259 名初产妇数据，评估围孕期高脂肪、高糖、高钠饮食模式与不良妊娠结局（先兆子痫、妊娠糖尿病、早产、小于胎龄儿）的关联，并检验蔬菜和水果摄入密度是否作为效应修饰因子。采用双重稳健学习器结合集成机器学习估计风险差，并分别考察复合结局和单一结局。结果显示该饮食模式与复合结局及多数单一结局（除早产外）存在正相关，每 100 例妊娠增加 1.0–2.9 例不良结局。蔬菜摄入密度可能修饰关联，但估计不精确，水果摄入密度未见明显修饰作用，联合修饰效应亦不显著。结论为未发现蔬菜/水果摄入密度能显著改变该饮食模式的风险。
- **关键技术**: `doubly robust learner`, `ensemble machine learning`, `risk difference estimation`, `effect modification`
- **为什么对您有用**: 本文是流行病学领域的应用研究，使用双重稳健估计和集成机器学习评估效应修饰，与您的流行病学应用兴趣直接相关。虽然方法学新颖性有限，但其分析流程（如处理效应修饰和联合修饰）可迁移至您的因果推断应用场景。武器库中的估计理论（如双重稳健估计）足以支撑理解，但本文无新方法学贡献，属于应用型论文，可作入门阅读。

### 10. [10.1097/ede.0000000000002055](https://doi.org/10.1097/ede.0000000000002055) — Fetal and infant mortality in Norway: A steady rate of decline over time
- **作者**: Allen J Wilcox, Rolv Terje Lie, Dag Moster
- **期刊/来源**: Epidemiology
- **机构**: National Institutes of Health · Norwegian Institute of Public Health · National Institute of Environmental Health Sciences · University of Bergen · Haukeland University Hospital
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文利用挪威国家医学出生登记处1967至2025年的数据，描述死产和婴儿死亡率的长期下降趋势。研究发现死产率每年约下降2.8%，新生儿死亡率每年下降3.7%，且均未显示减缓迹象。相比之下，出生后28天至1年的婴儿死亡率在1973-2000年间因婴儿猝死综合征（SIDS）流行而出现显著超额死亡，该流行与当时推荐的俯卧睡眠姿势有关。自1990年代初睡眠姿势建议逆转后，出生后死亡率迅速回归到每年3.5%的下降基线。作者以估计的恒定下降风险为基准，计算得出挪威有1367名婴儿因俯卧睡眠建议而死亡。该研究展示了长期趋势分析在识别有害干预影响中的价值，对您而言，其利用国家登记数据进行长期纵向趋势建模的方法，可作为流行病学队列研究中描述性分析的参考。
- **关键技术**: `national birth registry`, `long-term trend analysis`, `counterfactual benchmark`, `excess death estimation`
- **为什么对您有用**: 本文属于流行病学应用研究，使用国家登记数据，与您的secondary interest（流行病学应用）相关。作为gateway reading，它清晰展示了长期趋势数据结构和简单的反事实基准计算，武器库中的非参数统计和因果推断概念足以理解。值得花时间读全文，以了解流行病学中如何利用自然实验（睡眠姿势建议变化）评估干预效果。

### 11. [10.1097/ede.0000000000002050](https://doi.org/10.1097/ede.0000000000002050) — Impact of the first nirsevimab immunization campaign on infant RSV-related emergency department visits and hospitalizations in Québec, Canada
- **作者**: Amandine Bemmo, Élise Fortin, Patrick Fortin, Radhouene Doggui, Charles-Antoine Guay, Rachid Amini et al.
- **期刊/来源**: Epidemiology
- **机构**: Centre hospitalier universitaire de Québec · Université Laval · Centre de recherche du CHU de Québec-Université Laval · Institut National de Santé Publique du Québec · Université de Montréal · Institut universitaire de cardiologie et de pneumologie de Québec · Montreal Children's Hospital · McGill University Health Centre 等
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文评估了加拿大魁北克省2024-2025年RSV季节首次universal nirsevimab婴儿免疫规划对0-5月龄婴儿RSV相关急诊就诊和住院的影响。研究人群为全省<18岁儿童，利用主动监测和行政健康数据计算RSV确诊住院、RSV相关住院及RSV相关急诊就诊的发病率，并设置nirsevimab适龄组（0-5月龄）与非适龄组（6-11月龄及1-17岁）作为对照。方法上采用双重差分（difference-in-differences）和恒定住院比例反事实方法，以非目标年龄组的时间趋势调整干预前后的变化。结果显示，RSV确诊住院和RSV相关住院分别下降59%（95% CI: 49–70）和66%（95% CI: 58–71），急性细支气管炎急诊就诊下降35%（95% CI: 28–41），RSV相关急诊就诊下降60%（95% CI: 56–65）。估计2024-25季节避免了323至746例住院。结论认为nirsevimab运动与魁北克0-5月龄婴儿RSV相关住院和急诊就诊减少三分之二相关。对您而言，这是一篇典型的流行病学应用论文，展示了在真实世界疫苗效果评估中如何结合行政数据与反事实方法，其DID设计和对时间趋势的调整策略可为您在因果推断应用方面提供参考。
- **关键技术**: `difference-in-differences`, `counterfactual approach`, `administrative health data`, `active surveillance`, `incidence rate calculation`
- **为什么对您有用**: 本文属于流行病学应用领域，直接关联您的secondary interest中的流行病学因果推断应用。其DID和反事实方法虽不新颖，但展示了在真实世界疫苗效果评估中的具体操作，您可以用very_familiar的因果推断估计理论来审视其识别假设（如平行趋势）是否合理，并考虑是否可用更稳健的估计方法（如DML）改进。作为应用论文，值得作为入门读物了解RSV疫苗效果评估的数据结构和分析流程，但方法学novelty有限，若时间紧张可略读。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

