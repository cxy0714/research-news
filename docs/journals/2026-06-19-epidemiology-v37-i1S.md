# Epidemiology — Vol 37  Issue 1S  ·  2026-06-19

- 共 28 篇 · Epidemiology

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期的28篇论文可大致归为四条主线：**因果识别与偏倚机制**（约5篇）、**半参数/多水平建模与效应修饰**（约6篇）、**空间/环境流行病学与时空建模**（约5篇），以及**方法学评估与模拟研究**（约4篇）。其余为描述性生态或横断面关联分析，方法上多依赖标准回归。因果推断方向集中于对常用分析框架（如两阶段回归、准实验前后比较）的偏倚敏感性验证，半参数方向体现在贝叶斯联合模型、混合效应模型与log-binomial等非线性建模的选择与评估中。

**因果识别与偏倚机制**是本期方法学密度最高的主线。Confounding and scale-dependency of interactions 系统模拟了两阶段估计空调对热适应的因果效应时，遗漏时不变混杂（如距海岸距离）引入的偏倚，发现加性交互估计对所有未调整模型均有偏倚，即使调整混杂也仅在部分场景无偏——直接指向Meta回归在交互评估中的脆弱性。How Small Outcome Misclassification 针对罕见事件场景（死亡率<3%），模拟对称/不对称1–3%的结局误分类如何在大样本中扭曲风险比估计，并导致虚假“显著获益”概率升至近100%，为罕见病流行病学中的测量误差敏感性提供了定量警示。Effects of Lagged Deforestation 虽然主要使用贝叶斯空间负二项模型，但作者明确下一步将应用g-formula处理治疗-混杂反馈——这是本期唯一提及纵向因果推断框架的论文。此外，Examining inclusionary zoning 与The Association between Abortion legalization 分别尝试用多水平逻辑回归和政策前后比较评估因果效应，但均缺乏严格识别策略，可作为“朴素因果分析”的对照案例。

**效应修饰与混合效应建模**的几篇论文在方法上各有侧重。Exploring Effect Modification by Obesity 使用离散时间Cox模型并引入BMI分层交互，展示了修饰效应的标准化评估流程。Fetal Growth and Childhood BMI 用GLM估计胎儿腹围对儿童BMI的线性效应，但未处理反复测量内的相关性。Metabolic syndrome and memory decline 采用混合效应线性模型引入时间×MetS交互项，允许记忆衰退斜率随状态变化——是纵向数据中效应修饰的典型应用。Body size and thyroid autoimmunity 使用贝叶斯联合模型处理重复测量生长指标与生存事件的联合分布，是本期中最接近半参数效率框架的论文。其他如Green Space and Cardiovascular Health 的线性混合模型、Food Insecurity & homelessness 的朴素逻辑回归，方法上均无新意。

**空间/环境流行病学**中，State-Level HPAI Hotspots 使用Kulldorff扫描统计量做局部热点检测，但无因果识别。Mapping Food Is Medicine 与Mapping coffee shops 均为描述性空间展示。Epidemiological impacts of urban noise 是系统综述，指出暴露测量异质性是该领域主要方法学空白。这些论文为空间分析的应用范例，但方法学贡献有限。

对于因果推断/半参数方向的研究者，优先阅读：**Confounding and scale-dependency of interactions**（两阶段方法的混杂偏倚）、**How Small Outcome Misclassification**（测量误差对罕见事件的影响）、**Effects of Lagged Deforestation**（提及g-formula作为下一步）。对于半参数效率/联合建模感兴趣者，建议关注**Body size and thyroid autoimmunity**（贝叶斯联合模型处理纵向暴露与生存结局）和**Metabolic syndrome and memory decline**（混合效应交互模型）。若关注模拟方法评估，则可看**A simulation of potential air cleaning interventions**（队列-状态转移模型，但参数校准未披露）。

## 流行病学  *(epidemiology, 28 篇)*

### 1. [10.1097/01.ede.0001193384.94971.ba](https://doi.org/10.1097/01.ede.0001193384.94971.ba) — Confounding and scale-dependency of interactions: Threats to validity when quantifying the contribution of air conditioning to heat adaptation
- **作者**: Jaime Daniel Reyes-Sánchez, Sandrah Proctor Eckel, Juan Pablo Lewinger, Erika Garcia
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 6-6
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文在流行病学因果推断框架下，系统评估了量化空调使用（AC）对热适应贡献时常用的两阶段方法的稳健性。研究聚焦于时不变混杂因素（如距海岸距离）缺失所导致的偏倚，并通过模拟40个美国城市1988-1998年的日死亡数据（基于实际温度和AC普及率）进行分析。方法上，阶段一估计热死亡率随时间变化的效应，阶段二通过meta回归将效应与AC交互（乘性及加性尺度），并比较是否调整混杂的模型偏倚。结果表明，在假定AC对死亡率无主效应的前提下，未调整模型在4/4个混杂场景中均有偏倚，调整模型仅在1/4场景有偏倚；而一旦允许AC主效应非零，所有模型在加性交互上均存在偏倚。结论强调两阶段方法对遗漏时不变混杂敏感，且依赖AC无主效应的强假设。对您而言，这篇流行病学应用论文清晰展示了交互作用因果估计中混杂控制的关键性，可直接连接您的因果推断兴趣中关于未观测混杂敏感性的子方向。
- **关键技术**: `two-stage meta-regression`, `simulation-based sensitivity analysis`, `additive vs multiplicative interaction`, `time-varying effect estimation`, `unmeasured time-invariant confounder`
- **为什么对您有用**: (1) 本文属于流行病学应用论文，聚焦于因果推断中交互作用的混杂敏感性问题，直接连接您的 secondary interest 中的流行病学应用子方向；(2) 武器库中的 'estimation theory in causal inference' 可以用于分析两阶段估计的偏倚来源，而 'identification theory in causal inference' 能帮助理解交互作用的因果识别假设（如无主效应假设）；(3) 这是一篇值得通读的方法评估论文——它不像入门口径，但通过模拟暴露了实际数据分析中容易忽略的偏倚机制，如果你计划在未来流行病学合作中使用两阶段设计，读本文能预先规避假设陷阱。

### 2. [10.1097/01.ede.0001193348.87092.20](https://doi.org/10.1097/01.ede.0001193348.87092.20) — How Small Outcome Misclassification and Large Sample Sizes Can Distort Rare-Event Analyses in Differentiated Thyroid Cancer
- **作者**: David Zachariah Allen, Merry Sebelik
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 3-4
- 相关性 6/10 · novelty: `application`
- **摘要**: 该研究针对分化型甲状腺癌（DTC）中罕见事件（死亡率<2-3%）的场景，通过模拟评估结果误分类对风险比（RR）估计的影响。模拟设置对称误分类（两组误分类率相同）和不对称误分类（如1% vs 3%），并考察样本量从每臂500增至2500以上的变化。无分类错误时，RR估计中位数为1.00（IQR 0.81-1.24），体现低事件率下的高变异性。对称误分类使估计变窄，产生虚假的组间等价外观；不对称误分类则引入方向性偏倚，中位数RR降至0.98。随着样本量增大，错误报告“显著获益”的概率从64%升至近100%，表明大数据集可放大极小误分类。结论指出：在罕见事件研究中，即使1-3%的误分类也足以扭曲效应估计并误导推论，对流行病学观察性研究的因果推断有警示意义。该模拟设计清晰、结果直观，可作为流行病学中测量误差敏感性分析的入门读物。
- **关键技术**: `simulation study`, `misclassification analysis`, `rare-event epidemiology`, `risk ratio estimation`, `sample size amplification`
- **为什么对您有用**: （1）本文属于流行病学应用，直接关联您的 secondary interest 中流行病学数据驱动的因果推断问题，特别是罕见事件下测量误差对效应估计的扭曲。 （2）您非常熟悉「estimation theory in causal inference」和「identification theory」，可立即理解误分类如何影响效应估计的偏差与方差；文中提到的大样本放大效应也值得在研究敏感性分析方法时参考。 （3）作为 gateway reading，该文是清晰的入门读物，无需额外武器即能读懂全文；值得花时间阅读以直观掌握罕见事件中误分类的后果，并思考是否需要在您自己的因果推断方法中纳入类似敏感性考量。

### 3. [10.1097/01.ede.0001193388.41649.da](https://doi.org/10.1097/01.ede.0001193388.41649.da) — Effects of Lagged Deforestation on Malaria Risk in the Peruvian Amazon: A Spatio-Temporal Analysis
- **作者**: Jose Matta-Chuquisapon, Julianne, Sergio
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 6-6
- 相关性 5/10 · novelty: `application`
- **摘要**: 本研究利用秘鲁亚马逊地区2010–2020年的区级监测数据，评估滞后森林砍伐对疟疾风险的影响。采用贝叶斯混合效应模型（负二项族）并通过INLA进行拟合，同时控制气候、环境和社会人口协变量。结果显示，滞后砍伐率的对数转化效应相对风险为1.36（95% CI [1.06–1.75]），而分类砍伐率呈现非线性模式：在砍伐面积>5%和>10%时风险显著增加，>20%时不再显著。砍伐与人口密度的交互作用仅在第二四分位数处显著（RR=2.69），表明中等人群密度区域风险最高。风险地图显示北部持续高风险，南部具有保护效应。作者明确下一步将应用g-formula分析纵向数据中治疗-混杂反馈。作为一项扎实的流行病学应用研究，本文清晰展示了空间-时间数据的建模流程，并直接指向纵向因果推断方法（g-formula），对您感兴趣的流行病学应用和因果推断（纵向研究）均有参考价值。
- **关键技术**: `Bayesian mixed-effects model`, `INLA (Integrated Nested Laplace Approximation)`, `spatio-temporal analysis`, `g-formula (future work)`
- **为什么对您有用**: 本文属于流行病学应用，数据集（秘鲁亚马逊2010–2020年国家监测数据）和建模流程（贝叶斯负二项混合模型+INLA）可为您提供真实数据在空间-时间分析中的典型范式。更重要的是，作者明确提出下一步使用g-formula处理纵向数据中的治疗-混杂反馈，直接连接到您主要兴趣中的因果推断（纵向、g-formula）。您的技术武器库中moderately_familiar的识别理论（如g-formula）恰好可支撑对该应用后续方法的深入理解，因此可列为中期可做方向——在您的g-formula方法基础上可自然讨论滞后效应的识别假设、时变混杂等问题。本文作为流行病学应用，阅读门槛较低，值得花时间读全文以理解数据结构和分析设计。

### 4. [10.1097/01.ede.0001193416.22474.52](https://doi.org/10.1097/01.ede.0001193416.22474.52) — Examining the influence of local inclusionary zoning policies on the relationship between type 2 diabetes and COVID-19 mortality
- **作者**: James Groh, Keith Dookeran, Chibuzor Abasilim, Linnea Laestadius, Lorraine Halinka Malcoe
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 8-9
- 相关性 5/10 · novelty: `application`
- **摘要**: 该研究探讨美国地方包容性区划（IZ）政策对2型糖尿病（T2D）与COVID-19死亡率之间关系的影响。利用国家COVID队列协作（N3C）数据仓库的电子病历记录，结合CityHealth评估数据，纳入38,629名成年人COVID-19确诊病例。采用多水平逻辑回归模型，评估IZ政策有无及质量（黄金 vs. 无/铜/银）对T2D与死亡率关联的修饰效应，同时按种族/民族分层并加入社会剥夺指数（SDI）作为第三层。调整合并症、年龄、性别和城市医院容量。敏感性分析考虑政策实施与结果之间的滞后时间。主要估计值为比值比和95%置信区间，并通过组内相关系数（ICC）衡量IZ政策解释的死亡率变异比例。目前结果因联邦政府关闭而延迟，未见最终估计。本研究是首次将IZ政策与T2D结局联系起来的流行病学分析，丰富了社区层面政策与慢性病健康公平交叉的实证证据。
- **关键技术**: `multilevel logistic regression`, `effect modification via stratification`, `Social Deprivation Index (SDI)`, `sensitivity analysis for policy lag`, `intraclass correlation coefficient (ICC)`
- **为什么对您有用**: 本文属于流行病学应用方向（secondary interest），展示了使用多水平模型评估地方政策对健康公平影响的标准分析流程。您可以在因果推断框架下（如用DID或IV替代相关设计）更严格地处理政策内生性，或将识别理论中的负对照思想用于政策效果的敏感性分析。由于论文目前缺乏完整结果且方法学创新性不足，作为 'gateway reading' 可快速了解这类政策评估的数据结构，但暂不需要深度投入——您的武器库中 '因果推断中的估计理论' 可直接用于设计更稳健的 estimator。

### 5. [10.1097/01.ede.0001193316.46363.33](https://doi.org/10.1097/01.ede.0001193316.46363.33) — The Association between Abortion legalization and Sexual Risk Behavior Among Adolescents in Uruguay
- **作者**: Maria Urrea Suescun, Elizabeth Kelvin
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 1-1
- 相关性 5/10 · novelty: `application`
- **摘要**: 本研究利用乌拉圭全球学校健康调查（GSHS）的三波横截面数据（2006、2012、2019），评估堕胎合法化政策前后青少年性风险行为（SRB）的变化。研究定义了五个结局指标：初次性行为年龄<14岁、性伴侣≥2、末次性行为未使用避孕套、未使用其他避孕措施以及综合风险指标。分析采用加权逻辑回归，控制年龄、性别、饥饿感（作为社会经济地位的代理）以及复杂调查设计，分别比较政策前期、初期与后期。结果显示，与合法化前相比，合法化初期和后期综合SRB无显著变化，唯一显著的是合法化后避孕套使用下降（OR=0.70）。该论文是流行病学政策评估的应用实例，但设计上缺乏对照组，因果推断较粗糙。对您而言，本文可作为入门读物，让您快速了解流行病学中传统的多轮横截面分析方法，并可用您熟悉的双重差分或敏感性分析等工具进行改进。
- **关键技术**: `logistic regression`, `complex survey design`, `repeated cross-sectional study`, `adjusted odds ratio`, `proxy for SES (hunger)`
- **为什么对您有用**: 本文属于流行病学应用领域，方法透明简单，是入门政策评估的良好范例。您武器库中的因果推断估计理论完全足以理解和复现该分析，且 identification theory（如 DID 识别）可作为中期改进方向。由于方法学深度有限，花少量时间通读即可把握其分析逻辑，后续可考虑引入更严谨的因果设计。

### 6. [10.1097/01.ede.0001193480.19306.16](https://doi.org/10.1097/01.ede.0001193480.19306.16) — Exploring Effect Modification by Obesity in Associations of Iron Deficiency with Fecundability After Pregnancy Loss
- **作者**: Sarah Rothbard, Ellen C. Caniglia, Stefanie N. Hinkle, Enrique F. Schisterman, Robert M. Silver, Chase D. Latour et al.
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 13-13
- 相关性 5/10 · novelty: `application`
- **摘要**: 该研究利用EAGeR前瞻性队列数据（1,228名有流产史的女性），探讨缺铁（血清铁蛋白<30 µg/L）与生育力（受孕时间）的关联，并检验肥胖（按BMI分层）是否修饰该效应。采用离散时间Cox模型调整人口学、生活方式和阿司匹林治疗分配，并用多重插补处理缺失协变量。结果表明，缺铁与正常BMI女性的生育力降低呈不精确的负相关（HR=0.85, 95%CI: 0.66–1.08），肥胖女性中关联更强（HR=0.65, 95%CI: 0.41–1.02），而超重女性中未见关联（HR=1.26, 95%CI: 0.86–1.84）。使用WHO更严格缺铁定义（<15 µg/L）后关联方向一致但更不精确。结论提示肥胖可能放大缺铁对生育力的不利影响，但对您有用的是：这是一篇典型的流行病学应用工作，使用的离散时间Cox模型和效应修饰分析是因果推断中效应修饰的常见设定，可作为检验交互作用方法的实证参考，数据结构和分析流程对理解流行病学数据（如先验流产队列）有入门价值。
- **关键技术**: `discrete-time Cox model`, `effect modification`, `multiple imputation`, `serum ferritin biomarker`
- **为什么对您有用**: 该文属于secondary interest中的流行病学应用（实际数据集、效应修饰分析），可视为一个标准的效应修饰Cox回归案例，帮助您了解流行病学队列中生物标志物-结局关联的分析实践。您当前的非常熟悉武器库中的'estimation theory in causal inference'足以理解其HR估计和分层策略，无需额外工具。立即可做：直接读懂其方法和结果解释，作为流行病学因果推断应用实例。

### 7. [10.1097/01.ede.0001193432.96976.70](https://doi.org/10.1097/01.ede.0001193432.96976.70) — Etiology of sepsis and in-hospital mortality in France: impact of the COVID-19 pandemic
- **作者**: Marie Al Rahmoun, Alexandre Sabaté-Elabbadi, Didier Guillemot, Christian Brun-Buisson, Laurence Watier
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 9-10
- 相关性 5/10 · novelty: `application`
- **摘要**: 该研究利用法国国家医保数据库（2018–2022年），纳入604,517名脓毒症ICU住院患者，旨在评估COVID-19大流行如何改变脓毒症病因（细菌性 vs. 病毒性）与院内死亡风险之间的关联。采用多变量Cox比例风险模型，按合并感染与否分层，并调整年龄、性别、合并症、感染部位和脓毒性休克。大流行前，无论有无合并感染，病毒性脓毒症的死亡风险均低于细菌性（aHR约0.6–0.7）；大流行期间（病毒性主要为COVID-19），这一关系逆转，病毒性脓毒症风险显著高于细菌性（aHR约1.1–1.4）。作者指出目前缺乏明确的病毒性脓毒症ICD-10编码，可能低估其负担。研究设计为标准观察性流行病学分析，未采用因果推断的先进方法（如工具变量或目标最大似然估计），但数据库规模大、协变量调整较全面，可作为大规模行政数据中因果问题的可读范例。
- **关键技术**: `Cox proportional hazards model`, `administrative health database (SNDS)`, `ICD-10 coding for sepsis`
- **为什么对您有用**: 直接对应您对流行病学应用研究的兴趣——使用大规模国家行政数据集（法国SNDS）分析COVID-19对脓毒症病因与预后关系的改变。您武器库中的`estimation theory in causal inference`和`identification theory`可进一步用于检查此处Cox模型的比例风险假设及未测量混杂（如用差分法或工具变量），但目前该文仅用了标准回归。作为流行病学入门阅读，本文清晰展示了研究问题、数据结构和分析流程；但若要严格处理时间依赖性混杂或COVID-19期间护理模式改变带来的偏差，您的因果推断工具箱尚缺处理动态治疗的专门方法（如g-computation或g-estimation），因此目前`暂不可做`——除非先补充纵向因果推断的武器。

### 8. [10.1097/01.ede.0001193500.48420.ac](https://doi.org/10.1097/01.ede.0001193500.48420.ac) — Green Space, Walkability, and Cardiovascular Health Across the Menopausal Transition: The Study of Women’s Health Across the Nation
- **作者**: Seema Desai, Xiangmei (May) Wu, Jinshil Hyun, Carol A. Derby, L. Elaine Waetjen, Bradley M. Appelhans et al.
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 15-15
- 相关性 4/10 · novelty: `application`
- **摘要**: 在 SWAN 多中心纵向队列（N=2008，随访约16年）中，研究居住地绿化与步行友好度对中年女性心血管生物标志物的影响，estimand 为炎症/血脂指标的长期平均差异。暴露基于 NLCD 与 NDVI 两种地理空间指标按 1000-m 缓冲区计算，并以 12 个月居住史加权；步行友好度作为另一暴露。采用线性混合效应模型估计关联，调整社会人口与环境协变量，并做绝经状态与 BMI 的交互分析。结果显示中等绿化与 hs-CRP 降低 11.5% 及纤维蛋白原降低相关，而中等步行友好度反而与 LDL/总胆固醇升高相关。对您而言，本文展示了流行病学队列中环境暴露与纵向生物标志物的典型分析范式，但方法学 novelty 有限。
- **关键技术**: `linear mixed-effects model`, `Normalized Difference Vegetation Index (NDVI)`, `National Land Cover Database (NLCD)`, `geospatial buffer exposure assignment`, `interaction analysis by menopausal status`
- **为什么对您有用**: 本文属于流行病学应用，连接到 epidemiology secondary interest 的纵向队列因果分析方向。武器库中 linear mixed-effects model 与 longitudinal data 结构是 very_familiar 的，但本文未涉及 IV、DML 或 semiparametric efficiency 等您关注的核心方法，仅是传统回归调整，无法用 HOIF 或 higher-order U-stat 等武器攻入。作为 gateway reading：本文对中年女性心血管环境流行病学入门尚可，数据结构（重复生物标志物+地理暴露）清晰，但方法学深度不足，不值得花时间读全文。

### 9. [10.1097/01.ede.0001193472.19427.6b](https://doi.org/10.1097/01.ede.0001193472.19427.6b) — Fetal Growth is Associated with Future Childhood BMI Percentile in a Diverse U.S. Cohort.
- **作者**: Erin Alsbrook, Brian Neelon, Roger B. Newman, Hermes Florez, Stefanie Hinkle, Kelly J. Hunt
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 13-13
- 相关性 4/10 · novelty: `application`
- **摘要**: 在流行病学队列设定下，研究目标是超声测量的胎儿腹围（AC）及其生长速度与4-8岁儿童BMI百分位的关联。数据来自NICHD Fetal Growth Studies与ECHO-FGS的816对母婴，AC在15、20、28、37周标准临床时间点测量，生长速度定义为15-28周与28-37周的AC差值。方法采用广义线性模型（GLM），在调整人口学与临床特征后估计AC及AC速度对年龄-性别标准化BMI百分位的效应。结果显示15、20、28周AC每增加1cm，儿童BMI百分位分别平均上升4.47、5.28、3.58；15-28周AC生长速度（mm/周）的中位数对应BMI百分位56.69。本文为纯应用关联分析，未涉及因果identification或semiparametric效率理论，方法学novelty有限。
- **关键技术**: `generalized linear model`, `growth velocity parameterization`, `age-sex standardized BMI percentile`, `cohort study design`, `perinatal exposure`
- **为什么对您有用**: 本文属于流行病学应用，连接到epidemiology的perinatal exposure与childhood BMI方向，但仅用GLM做关联分析，未触及causal inference的identification或sensitivity分析。武器库中的estimation theory in causal inference与identification theory in causal inference可以攻这篇paper的口子：当前GLM关联结果受混杂影响严重，若要走向prenatal intervention的因果claim，需要引入IV（如随机化干预时机）或mediation（AC growth作为mediator）框架。follow-up粗判：中期可做——需先在moderately_familiar的identification theory in causal inference上长肌肉，将longitudinal mediation与time-varying confounding结合到fetal growth trajectory的因果路径中，才能把当前关联结果升级为因果证据。

### 10. [10.1097/ede.0000000000001981](https://doi.org/10.1097/ede.0000000000001981) — “Hours for what we will”: Paid time off and cardiovascular disease events, The Health and Retirement Study, 2010-2022
- **作者**: Samuel L Swift, Mussammat Snigdha Sowrin, Tali Elfassy, Adina Zeki Al Hazzouri, Barbara N. Harding
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 1-1
- 相关性 4/10 · novelty: `application`
- **摘要**: 在纵向队列设定下，目标是评估雇主提供带薪休假（PTO）对50岁以上在职人群心血管疾病（CVD）事件风险的因果效应，关键假设为Cox比例风险模型成立及无未测量的混杂。方法上使用Cox PH模型估计调整后的HR，控制了人口学、经济和临床特征，属于经典的IPW/回归调整类生存分析框架，收敛性质为标准n^{-1/2}渐近正态。主要实证结果为：有PTO访问权的人群CVD事件风险降低31%（HR=0.69, 95% CI 0.50–0.95），样本来自HRS 2010–2016队列5604人，随访6–14年。对您可能有用：本文提供了流行病学纵向队列中政策干预与健康结局的典型数据结构和分析范式，但方法学上未使用现代因果推断工具（如IV、proximal CI或sensitivity analysis）处理未测量混杂。
- **关键技术**: `Cox proportional hazards model`, `adjusted hazard ratio`, `prospective cohort study`, `confounding adjustment`
- **为什么对您有用**: 本文属于流行病学纵向队列中政策/暴露与健康结局的典型应用，连接到 epidemiology 的因果推断应用子方向，但方法学仅用 Cox PH + 回归调整，未触及您 primary interest 中的 IV / proximal CI / sensitivity analysis 等工具。用您 very_familiar 的 estimation theory in causal inference 或 moderately_familiar 的 identification theory 可以直接审视其未测量混杂的脆弱性，甚至用 proximal negative-control 框架重新分析 HRS 数据。follow-up 粗判：**立即可做**——用 very_familiar 的因果推断估计理论即可对本文的混杂偏倚做 sensitivity analysis 或重新设计 identification 策略。

### 11. [10.1097/01.ede.0001193444.11143.8f](https://doi.org/10.1097/01.ede.0001193444.11143.8f) — Empirical support for a mechanism-driven approach to categorizing Multiracial participants in depression disparities research
- **作者**: Sarah Forthal, Katherine Keyes
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 11-11
- 相关性 4/10 · novelty: `application`
- **摘要**: 在流行病学种族差异研究中，多种族（Multiracial）人群的分类方式缺乏理论依据，本文提出按抑郁差异驱动机制（如歧视、创伤、收入等9种）来指导分类方案。使用NESARC-III横断面数据（N=36,309），比较了三种分类方案（合并多种族、拆分多种族、与最低收入单种族合并即hypodescent）对9个机制变量的标准化效应量及R²/AIC/BIC/95% CI宽度。结果显示，不同机制下最优分类方案不同：歧视机制适用拆分方案，身份认同/收入/创伤适用合并方案，不良童年经历/健康/压力适用hypodescent方案。结论是按机制对齐分类可提升差异研究的效度。对您可能有用：本文展示了流行病学数据中分类假设如何影响因果效应估计的敏感性，提供了一个具体的数据集（NESARC-III）和机制驱动的分组思路。
- **关键技术**: `mechanism-driven categorization`, `standardized effect size comparison`, `model selection criteria (AIC/BIC/R²)`, `cross-sectional disparity analysis`, `hypodescent grouping`
- **为什么对您有用**: 本文属于流行病学应用，直接连接到 epidemiology secondary interest 的因果差异研究数据集（NESARC-III）与分组敏感性分析。从 causal inference 的 identification theory 视角看，分类方案本质上是 treatment 变量的不同 operationalization，不同方案对应不同因果机制假设，这为研究者在流行病学数据中做 sensitivity analysis 提供了实证参考。作为 gateway reading，本文对统计学者入门种族差异研究的数据结构和建模惯例是不错的读物，但方法学 novelty 有限（仅用标准化效应量与 AIC/BIC 对比，无 semiparametric / debiased ML 等现代工具），武器库完全够用但无需动用高级武器。建议：若对流行病学差异研究的实证模式感兴趣可快速浏览，无需深读全文。

### 12. [10.1097/01.ede.0001193448.22599.d0](https://doi.org/10.1097/01.ede.0001193448.22599.d0) — Examining age- and sex-related patterns of agreement between a literature-based framework and legacy risk calculators for coronary heart disease, diabetes, and dementia
- **作者**: Julia Blumkaitis-Bosankic, Boaz Saffer
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 11-11
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文在流行病学风险预测设定下，比较文献驱动框架与既有风险计算器（Framingham CHD、QDiabetes、DemPoRT dementia）在合成队列上的风险估计一致性。核心方法为构造合成队列复现各 legacy 模型的推导人群，用相同预测变量生成配对风险估计，以 Bland-Altman bias/limits、ICC 和相关系数量化一致性。结果显示总体相关性较高（CHD r≈0.95, dementia r=0.80），但一致性随年龄和性别系统性漂移：CHD 平均偏差约 3 pp 且随年龄增至 5 pp；痴呆在 80+ 女性偏差扩大；男性一致限更窄。结论指出老年、女性及含生物标志物模型需重新校准。对您而言，本文是流行病学风险模型校准与外部有效性评估的实证案例，展示了合成队列+Bland-Altman 的标准分析流程。
- **关键技术**: `synthetic cohort construction`, `Bland-Altman analysis`, `intraclass correlation coefficient`, `risk model recalibration`, `legacy risk calculator comparison`
- **为什么对您有用**: 本文属于流行病学应用，连接到 epidemiology 的风险模型与数据集方向。(1) 作为 gateway reading，本文清晰展示了流行病学中风险计算器外部有效性评估的标准流程（合成队列+配对预测+Bland-Altman），对不熟悉该领域的统计学者入门友好；(2) 武器库中 estimation theory in causal inference 与 software development 足以支撑复现此类分析，但本文无因果推断或高维/半参数理论 novelty；(3) 值得快速浏览摘要和图表以了解流行病学风险校准的实证范式，但无需花时间深读全文。

### 13. [10.1097/01.ede.0001193328.36446.8d](https://doi.org/10.1097/01.ede.0001193328.36446.8d) — Food Insecurity &amp; homelessness are positively associated with cardiovascular disease in a cross sectional study of college students
- **作者**: Hallie Sullivan, Ryan J. Gamba, Joseph J. Garo, Natasha L. Burke, Giovanna N. Rafanello, Ian S. Cohen et al.
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 2-2
- 相关性 4/10 · novelty: `application`
- **摘要**: 在横断面流行病学设定下，研究目标是食物不安全与无家可归对大学生心血管疾病指标（BMI、腰围、高血压等）的关联效应，模型假设为线性/逻辑回归调整有限协变量后的条件独立性。核心方法仅为常规多变量回归（线性回归用于连续结局，逻辑回归用于二分类结局），无任何因果推断设计（如IV、DML、proximal）或半参数效率考量。主要实证结果显示食物不安全与自报高血压(OR=2.10)及体脂率升高相关，无家可归与测量肥胖(OR=2.63)及多项指标恶化显著关联，但自报与测量肥胖结果不一致提示测量偏倚。对您可能有用：本文提供大学生社会决定因素与心血管风险的流行病学数据集，但方法学层面完全依赖朴素回归，无因果identification或效率理论贡献。
- **关键技术**: `cross-sectional study design`, `multivariable linear regression`, `multivariable logistic regression`, `self-reported vs measured outcome comparison`
- **为什么对您有用**: 本文属于流行病学应用，提供了大学生食物不安全/无家可归与心血管风险的数据集与关联估计，但方法仅为朴素回归调整，未触及您 primary interest 中的因果 identification / sensitivity / semiparametric efficiency。您的 technical_arsenal 中 estimation theory in causal inference 与 semiparametric theory 完全可以攻这篇 paper 的核心口子：横断面数据中存在严重混杂与测量偏倚，当前的朴素回归无法给出因果结论，可用 proximal CI 或 sensitivity analysis 重新审视 identification 假设的脆弱性。follow-up 粗判：**中期可做**——需先在 moderately_familiar 的 identification theory in causal inference 上长肌肉（如 proximal negative control 设定），才能对该数据集做有因果意义的重新分析。

### 14. [10.1097/01.ede.0001193440.36725.99](https://doi.org/10.1097/01.ede.0001193440.36725.99) — The association between dietary diversity and depressive symptoms among participants in a group-based microfinance program in rural western Kenya
- **作者**: Charles Opondo, Molly Rosenberg, Sonak Pastakia, James Akiruga, James Kamadi
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 10-10
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文基于肯尼亚西部农村地区参与小额信贷项目的311名成人横截面数据，旨在估计膳食多样性（过去24小时摄入五种食物组中的种类）与抑郁症状（CES-D量表）之间的关联。采用线性回归调整一系列协变量，以评估高度膳食多样性（五种全摄入）与连续抑郁评分的关系，并通过Wald检验考察财富状态的效应修饰。进一步使用分位数回归分析关联在不同抑郁评分分布分位点上的变化。结果显示，高膳食多样性与较低的抑郁症状评分相关（调整β=-3.19, 95%CI: -6.40,0.02），且在低财富个体中效应更强（交互p=0.05），并在较高分位点（50th、75th、90th）效应量更大。作者认为改善膳食多样性可能对资源匮乏环境中社会经济弱势群体的心理健康有益。这是一篇典型应用流行病学研究，尽管方法上仅使用标准回归，但研究问题和数据（小额信贷项目、横截面调查）对您关注的应用因果推断和流行病学数据集有一定参考价值，且可通过纵向或IV设计改进识别。
- **关键技术**: `linear regression`, `quantile regression`, `effect modification testing`, `CES-D scale`, `cross-sectional analysis`
- **为什么对您有用**: 此项流行病学应用研究直接关联您的次要兴趣领域——流行病学中的实际数据集与因果推断问题。虽然本文仅采用基础回归方法，未涉及高级因果推断工具，但其所用的小额信贷项目数据和横截面分析模式为您提供了一个可切入的真实数据场景。若未来希望在此类资源匮乏环境中运用更稳健的纵向或工具变量方法，本文可作为基线参考。当前武器库中的因果推断估计理论（如IV、纵向方法）可直接用于改进其识别策略，属于**暂不可做**（论文本身不需要武器，但需额外长期数据才能动手）。

### 15. [10.1097/01.ede.0001193344.84558.5b](https://doi.org/10.1097/01.ede.0001193344.84558.5b) — Exploring Maternal-Fetal Stress Dynamics: A Feasibility Analysis
- **作者**: Gesulla Cavanaugh, Stachyse Stanis, Pearly Trivedi, Donna Williams-Newman, Odette Hamilton, Nithin Subramaniam
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 3-3
- 相关性 4/10 · novelty: `application`
- **摘要**: 本研究评估慢性心理社会压力对孕妇及胎儿健康影响的可行性，目标 estimand 为母胎压力动态关联及孕期压力对早产/发病风险的因果效应，但仅停留在相关性描述层面。方法上招募35名27-39周孕妇，通过Tobii眼动仪、Shimmer生理传感器与唾液皮质醇采集暴露于三种情绪视频后的反应数据，使用SPSS做多元分析与t检验。核心发现仅为胎儿心率与母亲心率的正相关（r=0.64, p<0.05）及同步稳定模式，未涉及任何因果识别策略或半参数效率理论。结论宣称可为大规模干预研究提供可行性依据，但方法学 novelty 极低，纯属描述性流行病学可行性报告。对您而言，本文仅提供母胎压力数据集的采集范式参考，无统计理论贡献。
- **关键技术**: `feasibility study design`, `multivariate analysis`, `t-test`, `physiological stress measurement`, `correlation analysis`
- **为什么对您有用**: 本文属于流行病学应用，但仅使用基础t检验与相关分析，未涉及IV、proximal CI或semiparametric方法，对您的因果推断与效率理论武器库无直接接口。数据采集范式（眼动+心率+皮质醇）可能为未来更严格的因果中介分析提供数据基础，但当前可行性阶段样本量仅35人，无法支撑高维或半参数方法。**中期可做**：若未来大规模数据公开，可用您 moderately_familiar 的因果识别理论（mediation / longitudinal）重新分析母胎压力传导路径，但需先在 longitudinal mediation 的 semiparametric efficiency bound 上长肌肉。

### 16. [10.1097/01.ede.0001193428.30463.39](https://doi.org/10.1097/01.ede.0001193428.30463.39) — State-Level Geographic Hotspots and Temporal Pattern of Highly Pathogenic Avian Influenza Virus Occurrence in Turkey Across the United States, 2022-2025
- **作者**: Shamim Sarkar, Gary Vroegindewey
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 9-9
- 相关性 4/10 · novelty: `application`
- **摘要**: 本研究旨在识别2022–2025年间美国各州火鸡高致病性禽流感（HPAI H5N1）的地理热点与时间模式，estimand为空间聚集风险比与全局空间自相关指数。数据源自USDA/APHIS监测系统，共484起事件；方法上采用Global Moran's I检验全局空间自相关（I=0.25, p=0.020），并用Kulldorff圆形扫描统计量（CSSS）定位局部地理热点。核心结果显示明尼苏达与南达科他州事件最密集，冬季检出率最高（33%）；CSSS识别出涵盖明尼苏达、南达科他、爱荷华与威斯康星的主要热点集群（RR=16.4, p<0.0001）。本文为纯应用空间流行病学描述性分析，未涉及因果推断或半参数建模。对您而言，本文的价值在于提供了一个现成的兽医流行病学空间监测数据集，可作为空间因果推断或时空半参数模型的实证载体。
- **关键技术**: `Global Moran's I`, `Kulldorff's circular scan statistics`, `spatial autocorrelation`, `spatial epidemiology`
- **为什么对您有用**: 本文属于流行病学应用，直接连接到您的secondary interest——流行病学数据集与应用因果工作。虽然本文仅用描述性空间扫描方法，但该USDA/APHIS的时空监测数据集（含明确的空间自相关与季节异质性）为您的technical_arsenal中'identification theory in causal inference'提供了潜在实证场景：例如可尝试在该数据上引入空间IV或proximal negative-control来识别生物安全干预的因果效应。Follow-up判断：**中期可做**——需先在moderately_familiar的'identification theory in causal inference'上补充空间因果identification的文献肌肉，再结合very_familiar的软件开发能力搭建分析pipeline。

### 17. [10.1097/01.ede.0001193332.82657.09](https://doi.org/10.1097/01.ede.0001193332.82657.09) — Metabolic syndrome and memory decline: evidence from a longitudinal aging cohort in rural South Africa
- **作者**: Maria Klein, Erika Beidelman, Thomas Gaziano, Chodziwadziwa Whiteson Kabudula, Molly Rosenberg
- **期刊/来源**: Epidemiology
- **机构**: Indiana University · Columbia University · Harvard University Press · University of the Witwatersrand
- **分类**: vol 37 · issue 1S · pp 2-2
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文利用南非农村HAALSA Indepth纵向老龄化队列，评估代谢综合征（MetS）与记忆衰退的关联。使用混合效应线性回归模型，引入MetS与时间交互项以允许斜率随MetS状态变化，并分年龄和性别层分析。结果显示MetS与较高基线记忆得分相关（β=0.07 SD, 95%CI 0.02-0.13），但与更快的记忆衰退相关（β=-0.01 SD/年, 95%CI -0.02-0.00）。作者认为MetS可作为低资源环境痴呆风险分层的标志。方法学上仅采用标准混合效应模型，未涉及工具变量或g-formula等因果推断框架。本文作为流行病学应用，提供了资源有限地区纵向数据与代谢-认知关联的实证证据，但其分析策略对您主要兴趣中的因果推断方法（如纵向g-computation或DML）有启发——可在此基础上探索更严谨的因果识别路径。
- **关键技术**: `mixed effects linear regression`, `interaction term`, `longitudinal cohort`, `stratified analysis`
- **为什么对您有用**: (1) 直接匹配您的secondary interest 'epidemiology (application, datasets, causal inference)'，是纵向队列中代谢暴露与认知结局的应用研究。 (2) 技术武库中'nonparametric statistics'和'estimation theory in causal inference'可用于将本文的简单模型升级为叠加交互的g-estimation或doubly robust方法——例如用semiparametric效率界评估当前混合效应模型的方差是否最优。 (3) follow-up粗判：中期可做——需先在moderately_familiar的'identification theory in causal inference'上提升，才能将本文描述性关联转化为因果效应估计（如处理时变混杂）。

### 18. [10.1097/01.ede.0001193496.49453.94](https://doi.org/10.1097/01.ede.0001193496.49453.94) — Excess mortality following discharge from substance use disorder treatment in Chile, 2010–2020
- **作者**: Jay Kaufman, Andres González-Santa Cruz, Álvaro Castillo-Carniglia
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 14-15
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文基于智利2010-2020年物质使用障碍治疗登记册与死亡登记册的链接，构建回顾性队列，量化治疗出院后患者的超额死亡率。研究对象为70,064名18-64岁成人，通过直接标准化法计算年龄、性别、年份调整后的死亡率及标准化死亡率比（SMR）。总体SMR为3.5（95%CI 3.3-3.8），女性（SMR=5.5）、酒精为主要物质（SMR=4.7）、住院治疗（SMR=4.8）及未完成治疗（SMR=3.9）的患者相对风险更高。外部死因（自我伤害、意外、袭击）及非外部死因（消化、呼吸、感染）均有显著超额。结论强调应加强治疗保留、综合心理卫生及出院后监测。本文是流行病学中标准化率与队列链接的典型应用，适合作为了解描述性流行病学分析思路的入门读物。
- **关键技术**: `Standardized mortality ratio (SMR)`, `Direct standardization`, `Registry linkage`, `Retrospective cohort design`, `Cause-specific mortality`
- **为什么对您有用**: 本文是流行病学领域的典型应用研究，清晰地展示了通过行政数据链接进行队列构建和标准化率计算的流程，对熟悉因果推断但少接触描述性流行病学的统计研究者而言，是理解真实数据分析和结果解读的好范例。研究者的武器库（非参数估计、软件工具）足以支撑复现或改进分析，但若涉及更复杂的混杂控制或因果框架，则需补充工具（如倾向评分加权）。本文值得一读，可快速了解药物滥用流行病学的数据结构和关键结论。

### 19. [10.1097/01.ede.0001193468.40223.3b](https://doi.org/10.1097/01.ede.0001193468.40223.3b) — Body size and composition in relation to the risk of thyroid autoimmunity in children: A prospective analysis in the TEDDY cohort
- **作者**: Joanna Clasen, Jaakko Koskenniemi, Jimin Yang, Jukka Kero, Helena Elding Larsson, Berglind Jonsdottir et al.
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 12-13
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文利用TEDDY前瞻性队列（美国和欧洲，5188名儿童），纵向评估身体大小和组成（身高、体重、BMI、体脂%、脂肪质量、瘦质量）与儿童甲状腺自身免疫（TPO和TG自身抗体）风险的关系。主要估计量为风险比（HR），使用贝叶斯联合模型处理重复测量的生长指标与时间至自身免疫事件之间的关联，并调整了混杂因素。关键发现是身高z评分与甲状腺自身免疫风险显著正相关（HR每SD 1.13, 95% CrI 1.04–1.24），且该关联在3–8岁最强，尤其女孩中更明显（HR 1.21 vs 0.99）。中亲身高也呈正相关（HR每cm 1.02, 95% CI 1.003–1.035）。方法上采用联合建模（shared random effects）将纵向过程和生存过程结合，避免了简单分两阶段的偏倚。对您而言，这是一篇典型的流行病学纵向因果推断应用，展示了如何利用观测性队列数据检验生长与自身免疫的因果关系，其分析模式（联合模型、敏感性考虑）可为您在因果推断纵向数据方向提供实际案例参考。
- **关键技术**: `Bayesian joint models`, `longitudinal cohort`, `shared random effects`, `survival analysis`, `autoantibody screening`
- **为什么对您有用**: 本文属于流行病学应用论文，直接连接您的secondary interest中的流行病学（纵向队列、因果推断应用）。虽然方法学新颖度不高，但为您展示了贝叶斯联合模型在长期随访数据中分析时间依赖暴露与生存结局的实际操作流程，是进入流行病学数据分析领域的良好入门读物。您的武器库中'very_familiar'的estimation theory in causal inference和nonparametric statistics足以理解和评估该方法，但若要进一步改进（如引入双重稳健估计或时变混杂处理），需先在'moderately_familiar'的identification theory in causal inference上加强。值得花时间读全文以获得实际数据结构和分析细节。

### 20. [10.1097/01.ede.0001193380.72525.c0](https://doi.org/10.1097/01.ede.0001193380.72525.c0) — A simulation of potential air cleaning interventions to reduce Long COVID incidence and disease burden
- **作者**: Alison Cohen, Toni Jaudon, Julia Moore Vogel, Devin Lane
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 6-6
- 相关性 3/10 · novelty: `application`
- **摘要**: 在 Long COVID 的公共健康设定下，目标是量化非药物干预（HEPA 过滤、远紫外线消毒、口罩）对 Long COVID 发病率和 DALY 负担的减少量。作者构建了队列-状态转移模型（cohort-state transition model），将 SARS-CoV-2 感染/再感染与 Long COVID 状态耦合，模拟不同干预场景下 10 年期 DALY 的变化。核心估计为：广泛采用 HEPA 与远紫外线消毒可在 10 年内每 1000 人减少 127 DALY。模型假设了自然恢复率低于 5% 及再感染可触发 Long COVID，但摘要未披露参数校准来源或不确定性量化方式。对您可能有用：作为流行病学队列-状态转移模型的实证案例，展示如何将因果干预效应嵌入多状态 Markov 模型进行 DALY 评估。
- **关键技术**: `cohort-state transition model`, `disability-adjusted life-years (DALY)`, `non-pharmaceutical intervention simulation`, `multi-state Markov model`
- **为什么对您有用**: 本文属于流行病学应用，连接到 epidemiology secondary interest 的因果干预评估与数据集方向。从 technical_arsenal 角度，您熟悉的 causal identification theory 可用于审视该多状态模型中再感染与 Long COVID 状态转移的因果识别假设（如 unmeasured confounding 是否被忽略）；但本文未涉及 semiparametric / DML 等高级估计方法，方法学 novelty 有限。粗判：**暂不可做**——本文是纯模拟预测模型，缺乏真实数据集与高级统计推断框架，对您当前武器库（higher-order U / efficiency bound / RMT）无直接技术入口，仅可作为多状态因果模型的轻量入门读物浏览。

### 21. [10.1097/01.ede.0001193464.47528.d7](https://doi.org/10.1097/01.ede.0001193464.47528.d7) — The Role of Parent-Paediatrician Relationship on Preventive Medical Care Utilization among U.S. children aged 1-17: Results from the National Survey of Children’s Health 2022-2023
- **作者**: Ogochukwu Abasilim, Kenechukwu Nwosu, Odinakachukwu Dimgba, Nkemasom Nwadei, Ogochukwu Ezeigwe, Meghna Lama et al.
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 12-12
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文利用2022-2023年全美儿童健康调查（NSCH）数据，考察家长-儿科医生关系质量对美国1-17岁儿童预防性医疗利用的影响。研究采用描述性统计和逻辑回归分析，以预防性医疗利用为二分类结局，以家长-儿科医生关系指数为主要暴露变量，调整家庭收入、父母教育、保险类型等混杂因素。结果显示，高质量关系与预防性医疗利用的比值比（aOR=7.87, 95% CI: 7.00–8.85）显著正相关；同时年龄越大利用概率下降，有保险比无保险利用概率高约3-4倍。值得注意的是，该分析仅基于截面数据与单水平logistic模型，未使用因果推断框架处理混杂、测量误差或选择偏倚。对您而言，本文提供了一个流行病学调查数据集（NSCH）的实际分析案例，但方法学上留有大量改进空间——例如可采用倾向得分匹配、工具变量或中介分析来增强因果解释力，这些正是您武器库中非常熟悉或中度熟悉的技术。
- **关键技术**: `logistic regression`, `odds ratio`, `National Survey of Children's Health (NSCH)`, `cross-sectional analysis`, `adjusted odds ratio`
- **为什么对您有用**: 本文属于您二级兴趣“流行病学”的应用实例，直接使用了公开可得的NSCH数据集，该数据包含丰富的儿童健康变量，可作为后续因果推断方法（如IV、中介分析、敏感性分析）的试验平台。您的武器库中“identification theory in causal inference”与“estimation theory in causal inference”可直接用于改进该关联分析的因果识别，例如使用负对照或工具变量来校正未测量混杂。本文方法简单，您无需额外工具即可快速复现并替换更先进的方法，属于“立即可做”的follow-up项目。

### 22. [10.1097/01.ede.0001193356.04076.d2](https://doi.org/10.1097/01.ede.0001193356.04076.d2) — Trends in Place-based Disparities in Cancer Risk Factors and Cancer Screening Utilization in the U.S., 1997-2023
- **作者**: Xiaofang Lai, Xuesong Han, K. Robin Yabroff, Lu Zhang
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 4-4
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文是一项县级生态学研究，旨在估计1997–2023年间美国城乡癌症风险因素与筛查利用率的差异趋势。目标参数为各年份的流行率比值（PR，城市 vs 农村），关键假设为县级聚合数据的时空可比性及2013年城乡连续代码的稳定分类。方法上仅使用描述性统计与P-trend趋势检验，无个体层面混杂调整或因果识别策略。主要结果显示：烟草使用与肥胖的城乡PR随时间显著扩大（P-trend分别为0.0013与0.027），乳腺X线筛查差异缩小（P-trend=0.02），而巴氏涂片差异未变。对您可能有用：本文展示了流行病学中 place-based disparity 的典型数据结构与描述性分析范式，但缺乏因果推断或半参数效率方法的应用。
- **关键技术**: `ecological study design`, `prevalence ratio`, `trend test (P-trend)`, `county-level small area estimates`, `Rural-Urban Continuum Codes`
- **为什么对您有用**: 本文属于流行病学应用，连接到 epidemiology 的 place-based disparity 子方向，但方法仅为描述性趋势检验，未涉及 IV / DML / semiparametric 等您熟悉的因果或效率工具。用 very_familiar 中的 minimax bounds 或 estimation theory in causal inference 无法直接攻破本文的口子，因为核心缺口在于生态学数据的因果识别与混杂调整，而非估计效率。follow-up 粗判：暂不可做——若想在此类流行病学数据上做方法学推进，需先在 moderately_familiar 的 identification theory in causal inference 上长肌肉（特别是 ecological-level causal identification 与 aggregate data bias），当前武器库不覆盖生态推断的因果识别。

### 23. [10.1097/01.ede.0001193436.76257.84](https://doi.org/10.1097/01.ede.0001193436.76257.84) — Log-binomial modeling of association between risky driving behaviours and incident road traffic crashes during the past one-year among young adults in a middle eastern country
- **作者**: Saeed Akhtar, Hoor Al-Somali, Ghala Al-Mezrem, Noura Al-Mansour, Hessa Al-Shuraian, Fatmah Mataqi et al.
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 10-10
- 相关性 3/10 · novelty: `application`
- **摘要**: 这篇横断面研究评估了科威特年轻成人过去一年道路交通事故（RTC）的一年期患病率，以及手持手机通话与RTC的关联。研究通过社交媒体自填电子问卷收集数据，纳入了1755名成年驾驶员。主要方法为多变量log-binomial回归，直接估计患病率比（aPR）及其95%置信区间。结果显示，定期使用手机通话、忽视交通规则、超速违规、驾驶经验（1-6年）以及较年轻年龄（18-35岁）均与RTC显著相关。Log-binomial模型在常见结局（患病率>10%）时优于逻辑回归，避免了比值比对患病率比的高估。该研究提供了横断面研究中关联分析的完整流程，可作为流行病学数据分析的入门范例。对您而言，这篇应用论文展示了真实世界数据中log-binomial回归的标准用法，与您流行病学应用这一secondary interest直接相关。
- **关键技术**: `log-binomial regression`, `prevalence ratio`, `cross-sectional study`, `self-administered questionnaire`, `multivariable regression`
- **为什么对您有用**: 该论文属于流行病学应用型研究，使用了log-binomial回归直接估计患病率比，与您的secondary interest“流行病学（应用、数据集、因果推断）”高度吻合。从武器库角度看，您的非参数统计学背景（very_familiar）可用于评估log-binomial模型的对数线性假设是否合理（如通过残差诊断或广义加性模型扩展）。本文的完整分析管道（问卷设计、数据收集、模型选择、解释）立即可理解并复现，属于**立即可做**的范畴——您可以用自己熟悉的数据分析工具（R或Python中的glm）快速重现结果，并考察log-binomial与改进Poisson回归的差异。

### 24. [10.1097/01.ede.0001193488.30452.01](https://doi.org/10.1097/01.ede.0001193488.30452.01) — The Association of the Supply of OBGYNs with Abortion Access in the United States
- **作者**: Kelly A. DeBie, Kayleigh P. Keller, Margaret J. Gutilla, David Rojas-Rueda, Jennifer L. Peel, Brittany M. Charlton et al.
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 14-14
- 相关性 3/10 · novelty: `application`
- **摘要**: 在Dobbs判决后美国各州堕胎政策变动的背景下，目标是估计州级堕胎政策限制程度与妇产科医生（OBGYN）供给率的关联。方法采用横截面回归，将AMA/AAMC提供的2018与2023年州级医生计数对二值堕胎政策指标做回归，调整人口规模，报告Rate Ratio与95% CI；敏感性分析构建了包含堕胎法与反LGBTQ政策的复合暴露指标并检验线性趋势。核心发现是：限制性州的OBGYN供给率显著低于保护性州（2018 RR=0.72, 2023 RR=0.71），但截至2023年底尚无证据表明Dobbs后供给发生短期位移；复合指标显示自主权限制程度与医生供给呈线性负相关。本文为纯应用流行病学观察性研究，方法学上使用标准Poisson/线性回归与率比估计，无新因果识别或半参数理论贡献；对您可能有用之处在于提供了一个政策干预后医生供给变化的真实数据集，可用于练习IV或DML等因果方法。
- **关键技术**: `rate ratio estimation`, `cross-sectional regression`, `sensitivity analysis with composite exposure`, `linear trend test`
- **为什么对您有用**: (1) 连接到流行病学应用因果工作——本文提供了Dobbs判决前后州级OBGYN供给与堕胎政策的真实数据集，但原分析仅为简单横截面回归调整人口，未处理政策内生性或混杂。(2) 用武器库中very_familiar的causal inference estimation theory或moderately_familiar的identification theory，可以攻击本文的核心缺口：州级政策自选择带来的内生性，例如用其他州级特征做IV或用DML做debiasing。(3) **中期可做**：需先在moderately_familiar的identification theory上长肌肉，设计合理的州级IV或panel data因果识别策略，才能将此数据集从关联分析提升到因果推断。

### 25. [10.1097/01.ede.0001193392.77346.aa](https://doi.org/10.1097/01.ede.0001193392.77346.aa) — Epidemiological impacts of urban noise pollution on oral health in low- and middle-income countries
- **作者**: Edmond Appiah, Christabel Adu
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 6-7
- 相关性 3/10 · novelty: `survey`
- **摘要**: 本文通过系统范围综述，研究城市噪声污染对低收入和中等收入国家口腔健康（包括牙周病、磨牙症、唾液皮质醇水平及口面疼痛）的影响。文章检索了PubMed、Scopus、Embase、Web of Science及区域数据库，两位审稿人独立筛选并提取数据，最终纳入14项观察性研究。大多数研究采用环境分贝图或自报噪声暴露作为测量方式；结果显示较高噪声暴露与磨牙症患病率增加、唾液皮质醇升高、牙周炎症加重及口面疼痛报告增多存在正相关，但暴露测量的高度异质性限制了结果的可比性。目前尚无纵向研究或使用客观个体噪声监测的数据，且缺乏系统的人口代表性样本。本文揭示了该领域的主要方法学空白：标准化暴露指标、纵向设计和生理应激生物标志物的整合。对于您而言，该综述清晰勾画了流行病学中一个亟待因果推断方法介入的应用场景（如使用负对照或敏感性分析来改进噪声-口腔健康因果效应的识别）。
- **关键技术**: `systematic scoping review`, `environmental noise exposure assessment (dB mapping, self-report)`, `salivary cortisol as stress biomarker`, `observational study synthesis`
- **为什么对您有用**: 本文直接对应您的次要兴趣——流行病学应用，特别是环境暴露与口腔健康的因果推断问题。您 moderately_familiar 中的 identification theory（如负对照、敏感性分析）可用于系统评估现有研究中暴露测量的效度和因果偏倚方向，该文明确指出的缺乏纵向设计和客观监测正是这些工具可以发力的缺口。但该方向的核心数据（纵向队列、客观噪声监测）您目前无法获取，且领域内缺乏标准化暴露测量协议，因此**暂不可做**直接贡献；作为了解流行病学应用需求的 gateway 阅读有一定价值。

### 26. [10.1097/01.ede.0001193324.87330.69](https://doi.org/10.1097/01.ede.0001193324.87330.69) — Mapping Food Is Medicine Across Texas: Regional and Demographic Disparities in Program Availability
- **作者**: Ogochukwu Abasilim, Naomi Tice, Shreela Sharma
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 2-2
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文利用2024年12月至2025年4月间的全州扫描数据，描绘了德克萨斯州“食物即医学”（FIM）项目的空间分布，并结合CDC PLACES的县级慢性病患病率进行地理差异分析。研究发现254个县中仅62个有FIM项目（76%的县为零覆盖），项目高度集中于Harris County（27个）和Fort Bend County（8个），其中医疗定制杂货（MTG）占54%。糖尿病（21–24%）、高血压（36–39%）、肥胖（45–50%）患病率最高的县反而没有任何FIM项目，孕产妇人群也面临28%的服务缺口。研究主要依赖描述性统计和GIS可视化，未采用回归调整或因果推断方法。结论指向政策需优先向高负担农村地区倾斜。对您而言，本文是典型的流行病学描述性应用研究，方法简单但数据整理与地理编码可供参考，不涉及您擅长的非参数或因果推断工具。
- **关键技术**: `GIS mapping`, `CDC PLACES data`, `Landscape scan`, `Descriptive analysis`
- **为什么对您有用**: 本文属于流行病学应用领域，聚焦于公共卫生项目分布的地域与人口差异。作为入门读物，它清晰地展示了如何利用公共数据库进行描述性评估，但未使用回归、倾向性评分或因果推断等您熟悉的统计工具。武器库中的非参数和高效推断方法在此无直接用武之地，因此全文价值有限，仅作背景了解为宜，不值得投入深度阅读。

### 27. [10.1097/01.ede.0001193492.49418.b2](https://doi.org/10.1097/01.ede.0001193492.49418.b2) — Understanding Treatment Adherence Barriers and Facilitators in Youth with Type 2 Diabetes: A Mixed-Methods Protocol
- **作者**: Gianfranco Morote Galvez, Celesthe Rodriguez, Megan O. Bensignor, Amy E. Noser
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 14-14
- 相关性 2/10 · novelty: `application`
- **摘要**: 该文研究青少年2型糖尿病治疗依从性的障碍与促进因素，提出一项混合方法研究方案。阶段一：招募10-21岁青少年及家长，完成基线调查（家庭功能、心理健康等），随后进行14天的生态瞬时评估（EMA），同时佩戴加速度计并使用电子药帽，实时记录饮食、体力活动和服药行为。阶段二：对部分参与者进行定性访谈，深化对EMA结果的理解并探索社区干预偏好。数据收集已于2025年8月完成：26名10-17岁青少年完成阶段一，12人完成阶段二；7名18-21岁青年完成阶段一，2人完成阶段二。该方案整合实时行为数据、客观金标准测量与定性见解，为开发文化敏感的家庭为中心干预提供依据。对您的流行病学应用方向，此文展示了实时行为监测与混合方法设计的具体实施，可为同类研究的数据收集与分析提供参考。
- **关键技术**: `ecological momentary assessment (EMA)`, `accelerometer`, `electronic pill cap`, `mixed-methods protocol`, `qualitative interviews`, `real-time behavioral data`
- **为什么对您有用**: 本文属于流行病学领域的应用研究，连接您的secondary interest中的流行病学。您武器库中的非参数统计（如处理EMA重复测量）和因果推断识别理论（如治疗依从性建模）可用于分析此类实时行为数据。本文作为应用实例，值得读全文以理解混合方法整合策略，对您未来参与流行病学合作研究有直接借鉴意义。

### 28. [10.1097/01.ede.0001193336.73816.49](https://doi.org/10.1097/01.ede.0001193336.73816.49) — Mapping the Opportunities: Using Network Analysis to identify Possibilities for engaging Neighborhood Coffee Shops and Diners for Health Promotion in the Community
- **作者**: Angela Chow, Huiling Guo, Seema K. Aithal, Hwee Pin Phua
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 2-3
- 相关性 2/10 · novelty: `application`
- **摘要**: 本研究针对新加坡两个社区的居民，通过混合方法（定性访谈+问卷调查）收集了人们对社区诊所、餐饮店和美容店的到访数据。研究利用两模网络（two-mode network）分析方法，将受访者与他们过去12个月到访的店铺连接起来，并计算各店铺的度中心性（degree centrality）以衡量其被访问的频率。结果显示餐饮店的中位度中心性（47）远高于诊所（18）和美容店（5），且前三大餐饮店的访问者覆盖了所有性别、种族和年龄组。作者认为社区咖啡店和餐厅具有更高的群众基础，可作为健康教育和促进的潜在场所。该研究是典型的流行病学应用研究，方法上仅使用了基础的网络描述性统计，没有涉及因果推断或高级统计建模。对您而言，本文展示了网络分析在公共卫生领域的简易应用，但其技术深度不足以直接迁移到您的研究方向。
- **关键技术**: `network analysis`, `two-mode network`, `degree centrality`
- **为什么对您有用**: 本文属于流行病学应用（secondary interest），使用网络分析方法识别社区健康促进的潜在场所。但方法十分基础（仅描述性度中心性），未涉及因果推断或更复杂的网络模型。研究者当前武器库中的工具（如高维统计、因果推断）在此处均无用武之地，因此暂不可做；该论文主要价值在于了解流行病学领域如何应用简易网络分析，而非为研究者提供可攻克的统计问题。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

