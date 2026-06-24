# Epidemiology — Vol 37  Issue 1S  ·  2026-06-24

- 共 11 篇 · Epidemiology

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期围绕因果识别与推断的实证挑战展开，尤其聚焦于**因果推断方法比较**、**中介与联合效应分析**，以及**测量误差与调查设计**三条主线。在因果推断方法比较中，一篇关于COVID-19疫苗有效性估计的论文（Comparative Evaluation of COVID-19 Vaccine Effectiveness During Omicron）系统地对比了传统logistic回归、边际结构模型、参数g-formula和TMLE四种方法，突出暴露重叠与时变混杂的处理，并展示了TMLE在2022–23季给出显著保护而其他方法未检测到关联的实例。中介分析方面，两篇论文分别探讨肥胖在食物获取与乳腺癌发病率之间的中介角色（Role of obesity in mediating the association between long-term geospatial food access and breast cancer incidence），以及产前农药暴露与母亲心理社会压力对儿童脑发育的单独与联合效应（Joint effects of prenatal pesticide exposure and maternal psychosocial stressors on brain development），后者使用了分位数g计算（qgcomp）和加权分位数和回归（WQS）这类处理多暴露联合影响的工具。测量误差与调查设计方面，两篇随机实验评估了问题措辞与产品图片对无烟烟草使用率自报准确性的影响（Impact of question wording and product imagery on estimates of smokeless tobacco use），以及信任在社区非医疗渠道健康信息接收意愿中的调节效应（Modifying Effect of Trust in Health Information from Neighborhood Food and Beauty Shops），前者通过随机分配控制混杂，后者则用逻辑回归及交互项刻画信任的异质性。

在因果推断方法比较这条线上，除了VE论文中TMLE相较其他方法的敏感性值得关注，还隐含了**g-methods（g-formula、IPTW）与机器学习规格整合**的实践。中介分析论文中，食物获取研究采用基于反事实框架的paramed宏估计自然直接与间接效应，是流行病学中传统中介分析的典型应用；而农药与压力联合效应研究则通过两类加权回归（qgcomp、WQS）处理多暴露的共线性与非线性，在方法上更贴近高维暴露混合物分析的当前进展。此外，家庭网络对移民精神病发病风险的研究（The impact of family networks during migration on the risk of non-affective psychotic disorders）虽仅使用泊松回归，但其暴露定义（是否独自迁移）反映了迁移过程中社会网络结构的因果测量问题，方法上虽基础但问题的因果识别思路有启发性。

与**因果推断**（方法比较、g-methods、TMLE）和**中介分析/联合暴露**（paramed、qgcomp、WQS）方向最贴的论文包括：Comparative Evaluation of COVID-19 Vaccine Effectiveness、Role of obesity in mediating the association、Joint effects of prenatal pesticide exposure and maternal psychosocial stressors。此外，The impact of family networks during migration虽方法简单但因果问题设计值得参考。

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1097/01.ede.0001193372.55415.f3](https://doi.org/10.1097/01.ede.0001193372.55415.f3) — Comparative Evaluation of COVID-19 Vaccine Effectiveness During Omicron Using Conventional and Causal Inference Approaches in a Longitudinal Cohort
- **作者**: Jade Yangyupei Yang, Jennifer Head, Amy Callear, Matthew Smith, Emileigh Johnson, Arnold Monto et al.
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 5-5
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文利用密歇根州HIVE纵向家庭队列数据，在Omicron流行期间估计COVID-19疫苗对症状性感染的有效性（VE），面临重叠暴露和时间变混杂的因果识别挑战。主要暴露为接种当前季节疫苗，结局为SARS-CoV-2症状性感染。研究比较了四种估计方法：传统合并logistic回归、边际结构模型（IPTW+IPCW）、参数g-formula和TMLE（使用机器学习规格）。结果发现，2022–23季VE估计值在方法间差异较大，TMLE给出25.5%（95% CI: 2.0–43.4%），而其他方法估计接近零且不显著；2023–24季所有方法均显示中度保护（约30–40%）。作者强调因果推断方法和机器学习可增强现实疫苗研究中的因果解释力度。对您而言，该论文直接展示了纵向数据中多种因果估计方法的实际表现差异，是验证您熟悉的因果估计理论（如DR估计、交叉拟合）在复杂队列数据中适用性的好案例。
- **关键技术**: `pooled logistic regression`, `marginal structural models (IPTW+IPCW)`, `parametric g-formula`, `targeted maximum likelihood estimation (TMLE)`, `machine learning specifications`
- **为什么对您有用**: 1) 直接关联纵向因果推断中的疫苗有效性估计，用户可借此考察TMLE与g-formula在非参数识别假设下的实际差异；2) 用户熟悉的'因果推断中的估计理论'和'M-estimation理论'可用于严格评估其估计量的方差估计是否稳健，或检验交叉拟合是否改善有限样本性能；3) 立即可做：用户可基于该数据模式，利用自己熟悉的非参数统计工具（如双稳健估计、影响力函数诊断）复现并扩展分析。

## 流行病学  *(epidemiology, 10 篇)*

### 1. [10.1097/01.ede.0001193368.84230.3f](https://doi.org/10.1097/01.ede.0001193368.84230.3f) — Role of obesity in mediating the association between long-term geospatial food access and breast cancer incidence in Metropolitan Chicago
- **作者**: Niyati Sudhalkar, Vanessa Oddo, Caryn Peterson, Neng Wan, Jiehuan Sun, Jonathan Coloff et al.
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 5-5
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文利用芝加哥大都市区30年的地理编码数据和乳腺癌病例对照研究（7,396例病例，21,900例对照），探讨长期食物获取与乳腺癌发病率之间的关联是否由肥胖（BMI）中介。研究者创新地构建了累积邻近度指标，将居住历史与健康/非健康食品店距离动态结合。采用Stata中的paramed宏估计自然直接效应和间接效应，调整多个混杂因素后，发现健康食品店邻近度与更低乳腺癌风险相关（OR=0.42），而非健康食品店邻近度与更高风险相关（OR=2.49），但间接效应接近1，提示肥胖并非主要中介通路。本文是流行病学中因果中介分析在实际大型观察性研究中的典型应用，使用的识别假设与方法（Mediation Analysis via Counterfactual Framework）为评估暴露-中介-结局关系提供模板。对您有用的是，该研究展示了中介分析在流行病学队列中的操作流程与潜在偏倚来源（如BMI测量误差），可作为因果推断方法在公共卫生问题中的实践案例。
- **关键技术**: `mediation analysis`, `natural direct and indirect effects`, `Stata paramed macro`, `cumulative food access metric`, `case-control study design`, `geospatial exposure assessment`
- **为什么对您有用**: 本文属于流行病学领域的因果中介分析应用，直接连接到您的secondary interest“epidemiology (datasets, applied causal work)”。您可以用causal inference的identification theory评估其识别假设（如无未测量混杂、一致性）是否合理，以及BMI测量误差对间接效应估计的影响。该论文使用标准paramed方法，技术难度较低，作为应用案例可帮助您熟悉流行病学中介分析的数据结构与Stata实现，但方法学上无直接拓展空间，属于“中期可做”：需先补充流行病学中介分析的假设检验与敏感性分析方法（如E值），这些工具您通过moderately_familiar的identification theory可以较快掌握。

### 2. [10.1097/01.ede.0001193476.44765.da](https://doi.org/10.1097/01.ede.0001193476.44765.da) — A prospective study on the association between potential prescribing omissions and hospitalizations in community-dwelling older adults
- **作者**: Liat Orenstein, Angela Chetrit, Keren Laufer, Rachel Dankner
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 13-13
- 相关性 6/10 · novelty: `application`
- **摘要**: 本研究使用以色列社区老年人队列（1210人）的前瞻性数据，探究潜在处方遗漏（PPOs）与12个月内住院结果（住院次数、住院时长≥4天、住院严重程度）之间的关联。PPOs依据START v3标准识别，59.3%的参与者存在至少一种PPO。采用负二项回归、二项逻辑回归和序数逻辑回归模型，调整社会人口学、生活方式和健康相关协变量后，结果显示有PPO暴露者住院次数增加（IRR=1.44），住院延长和严重程度风险分别升高约1.8倍和1.6倍，且呈现剂量-反应关系（0, 1-2, ≥3 PPOs）。该论文是流行病学中药物利用和处方质量评估的典型实证研究，分析流程清晰，统计方法虽经典但规范。对您而言，可作为入口级流行病学应用案例，熟悉队列数据分析模式和常见结果指标（IRR、OR等），但未涉及您最核心的因果推断或半参数等方法。
- **关键技术**: `START criteria (Screening Tool to Alert doctors to Right Treatment)`, `negative binomial regression`, `ordinal logistic regression`, `multivariable adjustment`, `dose-response analysis`
- **为什么对您有用**: 本文属于流行病学（secondary interest）的应用实证研究，展示了在队列中利用START工具定义暴露、以住院为结局的完整分析流程。研究者当前的非参数和回归基础完全足以理解本文方法，可作为流行病学入门阅读材料：数据来自人群队列、处理混杂调整、结果呈现方式（IRR、OR、剂量-反应）均是流行病学标准范式。本文不涉及因果推断前沿或计算统计，因此不属深读方向，但快速浏览全文约10-15分钟即可掌握该领域常见分析模式，对后续阅读更复杂的流行病学因果推断论文（如工具变量、目标试验模拟）有帮助。

### 3. [10.1097/01.ede.0001193396.74974.f3](https://doi.org/10.1097/01.ede.0001193396.74974.f3) — Joint effects of prenatal pesticide exposure and maternal psychosocial stressors on brain development in children from a South African birth cohort
- **作者**: Najiyah Williamson, Sarina Abrishamcar, Nadia Hoffman, Stephanie M. Eick, Dana Boyd Barr, Kirsty A. Donald et al.
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 7-7
- 相关性 6/10 · novelty: `application`
- **摘要**: 该研究利用南非 Drakenstein 儿童健康研究的出生队列（N=120），旨在评估产前农药暴露与母亲心理社会压力对 2-3 岁儿童大脑皮层结构（皮层厚度和表面积）的单独和联合效应。孕期第二 trimester 测量了尿液农药代谢物（如 CINA6）和心理社会因素，并通过结构 MRI 获取神经解剖学指标。单暴露分析采用线性回归，联合暴露使用分位数 g 计算（qgcomp）和加权分位数和回归（WQS），调整了母亲年龄、种族、社会经济状况、BMI 和颅内体积。单暴露模型中，CINA6 水平每增加一个单位与左半球表面积减小 669.21 mm²（95% CI: -1264.23, -74.19）及总表面积减小 1156.81 mm²（95% CI: -2301.34, -12.29）显著相关；但任何联合效应模型均未发现显著的混合物效应（无论是否包含心理社会因素）。结论提示 CINA6 可能具有神经发育毒性，但需进一步研究验证。对于您的流行病学二级兴趣，本文是混合暴露与神经影像学结局实际应用的案例，分析方法（qgcomp、WQS）虽非前沿，但数据结构和分析流程值得作为流行病学因果推断的实践参考。
- **关键技术**: `quantile g-computation`, `weighted quantile sum regression`, `mixture exposure analysis`, `single-exposure linear regression`, `structural MRI cortical measures`
- **为什么对您有用**: (1) 本文连接您的二级兴趣流行病学中的实际因果推断案例，展示了在资源有限环境下处理多重环境暴露与心理社会因素的联合效应分析框架。 (2) 您的技术武器库中的非参数统计与高维统计可以用于理解 qgcomp 和 WQS 背后的权重估计和线性假设，甚至可以尝试更灵活的非参数混合物模型来改进敏感性。 (3) 整体上，本文是流行病学混合暴露分析的一个清晰入门样例，方法学深度中等，值得花费少量时间通读以熟悉该领域的数据结构（N=120 小样本、多暴露、MRI 结局）和分析流程，属于暂不可做的直接延伸，但可作为拓展流行病学应用视野的 gateway reading。

### 4. [10.1097/01.ede.0001193452.77726.2d](https://doi.org/10.1097/01.ede.0001193452.77726.2d) — Impact of question wording and product imagery on estimates of smokeless tobacco use: Results from two randomized survey experiments
- **作者**: Michelle T. Bover Manderski, Nishi J. Gonsalves
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 11-11
- 相关性 6/10 · novelty: `application`
- **摘要**: 该研究通过两个随机调查实验（实验1 N=1387，实验2 N=1345），评估问题措辞变化对无烟烟草使用率自报准确性的影响。实验1比较标准描述与添加澄清语句（说明不包括尼古丁袋）的效果；实验2比较添加澄清语句与同时展示产品图片的效果。使用卡方检验比较不同组间报告的无烟烟草使用率。结果显示添加澄清语句后报告使用率显著降低（23.2% vs 17.9%，p=0.015），而增加图片未进一步降低报告率（19.1% vs 17.9%，p=0.59）。该研究属于流行病学调查设计中的简单随机实验，通过最小测量误差改进调查质量。虽无复杂统计方法，但展示了随机分配在减弱混淆中的作用，对了解流行病学中因果推断的入门设计有参考价值。统计方法简单且易复制，研究者可快速理解该领域的数据收集与分析逻辑。
- **关键技术**: `randomized survey experiment`, `chi-square test`, `prevalence estimation`
- **为什么对您有用**: 该论文是流行病学中调查测量误差的应用实例，可作为该方向的入门读物，帮助理解随机实验在测量效应识别中的基本逻辑。研究者的因果推断与非参数统计武器库（如DML、潜变量模型）足以在更复杂的测量误差场景中做进一步拓展，但本文本身方法简单、无新统计工具，建议快速浏览即可，不必深入阅读全文。

### 5. [10.1097/01.ede.0001193352.86357.6e](https://doi.org/10.1097/01.ede.0001193352.86357.6e) — Associations of reproductive factors with expression of stromal markers in women with benign breast biopsies
- **作者**: Maisey Ratcliffe, Yujing J. Heng, Brian Sardella, Bernard Rosner, Rulla Tamimi, Lusine Yaghjyan
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 4-4
- 相关性 5/10 · novelty: `application`
- **摘要**: 本研究旨在探索生殖因素（如产次、初产年龄、哺乳史、初潮年龄等）与良性乳腺活检女性中基质成纤维细胞标记物（αSMA、TNC、FAP、s100A6、MMP14）表达之间的关联。数据来源于护士健康研究II队列，纳入697例活检确诊良性乳腺疾病的女性，通过免疫荧光染色对组织芯片进行标记物定量。采用广义线性回归模型，调整潜在混杂因素后，分析各生殖因素与对数转化后标记物阳性率的关系。结果显示，未产状态、初潮年龄、初产年龄、初潮至初产间隔时间及哺乳史均与所有基质标记物表达无显著关联。研究提示生殖因素可能不直接影响乳腺基质的这些表型，但需更大样本或不同亚组进一步验证。本文是典型的流行病学病因学应用，使用基础回归分析，未涉及因果推断的高级识别策略或稳健估计方法。
- **关键技术**: `generalized linear regression`, `immunofluorescence quantification`, `tissue microarray`, `Nurses' Health Study II cohort`, `log-transformed outcomes`
- **为什么对您有用**: 本文属于流行病学应用研究，直接对应secondary interest的流行病学数据集与因果推断应用方向。但方法层面仅限于多变量回归调整，未使用工具变量、proximal因果推断或敏感性分析等武器库中的工具，因此对于提升因果识别技术帮助有限。若要基于此数据探讨生殖因素对基质标记物的因果关系，可尝试用IV或负对照方法进行再分析，这属于中期可做任务——需先在因果推断identification理论（moderately familiar）上进一步提升。全文可作为流行病学应用案例了解问题背景，但方法论借鉴价值较低。

### 6. [10.1097/01.ede.0001193360.72136.15](https://doi.org/10.1097/01.ede.0001193360.72136.15) — Associations of alcohol use with expression of stromal markers in benign breast biopsy samples
- **作者**: Anjoli Armstrong, Yujing J. Heng, Maisey Ratcliffe, Rulla M. Tamimi, Lusine Yaghjyan
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 4-4
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文利用护士健康研究II（NHS II）中683名活检确认良性乳腺疾病但未患癌的女性数据，探究酒精摄入与五种基质标志物（α-SMA、TNC、FAP、MMP14、S100A6）表达水平的关联。酒精消费通过半定量食物频率问卷（FFQ）评估，分为近期和累积平均摄入量（连续变量和分类变量），标志物表达通过免疫荧光定量（inForm软件）得到每核心阳性百分比，并对数值进行对数转换。采用广义线性回归（GLM）模型，调整已知乳腺癌风险因素（如年龄、绝经状态、BMI等）。结果发现：累积平均酒精摄入连续变量与TNC表达呈边缘显著正相关（每11g/day，b=0.59, p=0.06）；每日≥2 drinks（≥22g/day）与不饮酒相比，TNC表达显著更高（b=2.50, 95%CI 0.20-4.80）。其他标志物无显著关联。结论提示酒精可能通过影响TNC表达参与乳腺癌早期发生。本文是典型的流行病学应用研究，分析方法常规（线性回归），但提供了真实观察性数据集的分析流程和协变量调整策略，对从事流行病学因果推断应用的研究者有参考价值。
- **关键技术**: `generalized linear regression`, `covariate adjustment`, `semi-quantitative Food Frequency Questionnaire (FFQ)`, `immunofluorescence quantification (inForm)`
- **为什么对您有用**: (1) 直接对应 secondary interest 中的流行病学方向，使用真实队列数据集（NHS II）分析酒精摄入与生物标志物的关联； (2) 虽然方法简单（广义线性回归 + 协变量调整），但数据集结构（纵向更新协变量、重复测量暴露）和分析中处理混杂的思路可迁移至更复杂的因果推断问题（如使用IV或DML重新估计）； (3) 武器库中“estimation theory in causal inference”与“identification theory in causal inference”足以理解并改进其分析框架（例如加入倾向性评分或双重稳健估计），属于**立即可做**的扩展方向。

### 7. [10.1097/01.ede.0001193320.10343.64](https://doi.org/10.1097/01.ede.0001193320.10343.64) — The impact of family networks during migration on the risk of non-affective psychotic disorders among first-generation migrant groups
- **作者**: Jahin Ali Khan, Jordan Edwards, Britney Le, Daniel Lizotte, Kelly Anderson
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 1-2
- 相关性 5/10 · novelty: `application`
- **摘要**: 本研究基于安大略省 1992-2011 年约 200 万移民的回顾性队列，探索移民过程中家庭网络（是否独自迁移）与非情感性精神病障碍发病风险的关联，并分性别和移民类别进行分析。数据来源于健康行政数据库，通过验证算法识别首发精神病病例。统计方法为多变量泊松回归，调整社会人口学和迁移相关因素。初步结果显示：整体队列中，独自迁移与男女较高发病风险相关，但成年后迁移的男性群体中此关联不再显著；分移民类别后，经济类和难民类中独自迁移风险更高，而家庭团聚类男性中独自迁移风险反而降低。该研究引入了衡量迁移家庭网络的新变量并采纳性别视角，为移民–精神病病因学提供了线索。作为一项流行病学应用研究，其主要价值在于揭示效应异质性，但未使用因果推断领域较前沿的识别策略（如工具变量或敏感性分析），因此方法论创新有限。
- **关键技术**: `retrospective cohort`, `multivariable Poisson regression`, `validated case algorithm (NAPD)`, `stratified analysis by sex and migrant class`
- **为什么对您有用**: 本文属于流行病学应用，直接对接研究者的二级兴趣（流行病学数据集与因果推断应用）。研究关注移民–精神病关联的效应修饰，但仅依赖泊松回归调整，而非因果推断意义上的识别（未使用工具变量、敏感性分析或双重稳健方法）。研究者若进入该方向，可用自身熟悉的因果推断估计理论（如 DML、IV）对类似问题做更严谨的因果识别，但当前论文本身方法论简单，暂不具备当前武器库直接可复用的技术元件。

### 8. [10.1097/01.ede.0001193340.89856.58](https://doi.org/10.1097/01.ede.0001193340.89856.58) — Modifying Effect of Trust in Health Information from Neighborhood Food and Beauty Shops on Community Willingness to receive Health Information from these Non-Healthcare Sources
- **作者**: Angela Chow, Seema K. Aithal, Huiling Guo
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 3-3
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文研究社区居民对非医疗来源（社区食品店、美容店）提供的健康信息的信任如何影响其接收意愿。数据来自新加坡两个社区的横断面调查（N=403），使用多元逻辑回归分析。主要发现：之前未接触过非医疗来源健康信息的居民中，约31%愿意未来接收；信任这些来源的健康信息（AOR 3.71）和高健康信息导向（AOR 1.89）显著增加意愿。信任的调节效应在年轻（21-34岁、35-49岁）和男性群体中更强（AOR分别为4.98、8.02、6.22）。本文是典型的流行病学应用研究，方法标准（逻辑回归、交互项），但未涉及因果推断或高级统计方法。对您而言，该论文可作为流行病学领域简单应用案例，但方法学和数据复杂程度较低，与您的主要统计研究兴趣关联较弱。
- **关键技术**: `multivariable logistic regression`, `effect modification (interaction)`, `cross-sectional survey`, `adjusted odds ratio`
- **为什么对您有用**: 本文属于流行病学应用（secondary interest），展示了如何用标准回归分析检验信任的调节效应。但方法仅涉及基本逻辑回归，未使用因果推断或高级分析工具；您的武器库中的非参数统计、因果推断等工具在此论文中无用武之地。**暂不可做**：核心问题不需要您已有的统计技术，且数据和分析层次简单，值得花时间阅读全文的优先级较低。

### 9. [10.1097/01.ede.0001193484.36988.ec](https://doi.org/10.1097/01.ede.0001193484.36988.ec) — Caffeine intake and semen quality in a preconception cohort
- **作者**: Sachelly Julian-Serrano, Ruth J. Geller, Martha R. Koenig, Greg Sommer, Michael L. Eisenberg, Elizabeth E. Hatch et al.
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 14-14
- 相关性 4/10 · novelty: `application`
- **摘要**: 该研究基于 Pregnancy Study Online 队列，纳入 929 名男性伴侣（共 1668 份精液样本），评估咖啡因及含咖啡因饮料摄入与精液质量（精液量、精子浓度、总数、活力等）的关联。采用线性回归估计均值百分比差异（%D），调整禁欲时间及潜在混杂因素（如含糖饮料摄入）。结果发现总咖啡因摄入与精液质量无显著关联，咖啡摄入与精子活力略呈正相关（≥2杯/天 vs. 0杯/天的活动精子百分比 %D=6.5, 95% CI -0.1, 13.1）。这是一项典型的观察性流行病学因果推断应用，使用标准回归控制混杂，方法学上无新颖贡献。对您而言，该文可作为流行病学因果推断的实例，展示在队列中如何使用线性回归处理连续结局和暴露的分组比较，但方法深度有限。
- **关键技术**: `linear regression`, `covariate adjustment`, `percentage difference estimation`, `self-reported dietary assessment`
- **为什么对您有用**: 本文直接连接次级兴趣中的流行病学因果推断应用，展示了在生育健康队列中分析暴露-结局关联的典型流程。您武器库中很熟悉的「因果推断估计理论」可以审视其调整变量选择是否合理、未测量的混杂如何影响结论，但方法本身简单（线性回归），中期可做的工作：若将您的「HOIF」或「双机器学习」技术应用于此类数据以处理高维混杂或非线性效应，需先熟悉流行病学数据分析的结构。立即可做：复制其分析并检验稳健性。

### 10. [10.1097/01.ede.0001193456.38708.d1](https://doi.org/10.1097/01.ede.0001193456.38708.d1) — Molecular characterization of norovirus circulating in district Lahore
- **作者**: Ayesha Saif, Nadia Mukhtar
- **期刊/来源**: Epidemiology
- **分类**: vol 37 · issue 1S · pp 11-12
- 相关性 1/10 · novelty: `application`
- **摘要**: 本研究旨在分子鉴定2024年1月至12月拉合尔地区儿科急性胃肠炎患者中诺如病毒的流行株。共收集240份粪便样本，通过RT-PCR靶向VP1基因扩增，27%样本呈阳性。阳性样本测序后使用MEGA11进行系统发育分析，发现GII基因型为主要流行株。社会人口学分析显示三岁以下儿童阳性率最高(56.9%)，与腹泻频率存在显著关联。尽管性别和季节无显著关联，冬季阳性率最高(36.9%)。本研究提供了拉合尔地区诺如病毒分子多样性和风险因素的基线数据，但方法学上为经典描述性流行病学，未涉及因果推断或现代统计建模。对于您的流行病学数据应用兴趣，可作为常规规范设计的示例，但缺乏方法学新意。
- **关键技术**: `RT-PCR`, `Sanger sequencing`, `phylogenetic analysis (MEGA11)`, `chi-square test`, `molecular genotyping`
- **为什么对您有用**: 该论文属于secondary interest中的流行病学应用，但仅使用了最基本的分子检测和卡方检验，未涉及您武器库中的任何方法。您的technical arsenal中无可用武器来处理此类描述性流行病学数据，缺乏因果推断或高维统计的入口。整体而言，读全文的收益有限——属于常规监测报告，无需花费时间深入阅读。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

