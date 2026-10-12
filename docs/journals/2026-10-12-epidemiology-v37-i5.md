# Epidemiology — Vol 37  Issue 5  ·  2026-10-12

- 共 16 篇 · Epidemiology
- 目录核对 ⚠️ 疑似漏 7 篇（对照 OpenAlex 26 篇）：10.1097/ede.0000000000001998、10.1097/ede.0000000000001982、10.1097/ede.0000000000002001、10.1097/ede.0000000000002003、10.1097/ede.0000000000001997 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Epidemiology》整体上围绕**因果推断的识别与推广**、**测量误差与偏倚校正**、以及**环境与政策暴露的健康效应评估**三条主线展开。因果识别与推广是绝对核心，涉及多篇论文：从方法层面看，有面向Riesz表示定理与半参数效率的入门性介绍（Riesz Representers for the Rest of Us），有结合两个观测研究同时校正混杂与结局测量误差的融合设计（Combining Observational Studies to Reduce Multiple Biases），也有在嵌套队列中通过逆概率加权将效应推广回目标总体的应用（Generalizing Findings in Nested Cohorts），以及将随机试验结果外推至试验合格人群和治疗候选人群的g-标准化实例（Extending Inferences from a Randomized Trial）。测量误差与偏倚校正方面，除融合设计外，还有针对长期随访中分类误差随时间变化的验证子研究设计（Differential Misclassification by Time）。环境与政策暴露评估则包括义务教育法作为自然实验的长期效应分析（The Long Arm of Childhood Policy）、监狱温度-死亡关联的病例交叉设计（Lagged and Nonlinear Effects of Temperature Extremes）、智能电表空调普及率对温度-急诊关联的效应修饰（Smart Meter-derived Air Conditioning）、工业空气毒物暴露的共享脆弱模型（Industrial Air Toxicant Exposure），以及过量预防中心对社区行人拦截的增强合成控制（Changes in Community-level Pedestrian Stops）。

最值得展开的是**因果识别与推广**这条主线，它从多个角度切入同一问题：如何将非随机样本中的效应估计推广到目标总体。Generalizing Findings in Nested Cohorts 和 Extending Inferences from a Randomized Trial 分别处理观测数据和试验数据的外推，前者用IPW校正选择偏倚，后者用g-标准化将试验结局模型标准化到目标人群协变量分布，两者互补地展示了外部有效性在流行病学中的操作化。Combining Observational Studies to Reduce Multiple Biases 则更进一步，提出融合设计同时处理混杂和测量误差，构建了IPW、g-computation和AIPW三类估计量，在方法上更接近半参数效率理论。Riesz Representers for the Rest of Us 虽为教学性文章，但恰好为上述方法提供了统一的理论框架——它将ATE、ATT等目标泛函表示为对Riesz representer的期望，并说明正交得分如何实现一阶不敏感性，这直接支撑了融合设计和DML类方法的构造逻辑。这四篇放在一起，构成了从理论工具到具体应用的完整链条。

另一条值得注意的主线是**测量误差与偏倚的时间动态**。Differential Misclassification by Time 直接针对分类误差随时间变化的场景，提出在随访不同时点进行验证抽样以估计时变PPV/NPV，并通过模拟比较了有目的抽样与随机抽样的表现。这与Combining Observational Studies中处理结局测量误差的思路形成对照：前者在单一研究中通过验证子设计校正，后者通过外部金标准数据校正。两篇都强调偏倚参数不能视为常数，这一共同关注点在本期中尤为突出。

此外，**环境与政策暴露评估**的应用类论文虽方法相对常规，但各有特色：Lagged and Nonlinear Effects of Temperature Extremes 将病例交叉设计与DLNM结合，处理极端温度的滞后和非线性效应；Smart Meter-derived Air Conditioning 利用高分辨率智能电表数据构造社区级暴露修饰变量，体现了数据源创新；Changes in Community-level Pedestrian Stops 则用增强合成控制法评估政策干预的社区效应，属于准实验设计的应用。这些论文对因果推断方法本身的贡献有限，但展示了方法在不同数据场景下的适配。

若按主题优先阅读：因果推断与半参数效率方向，建议先看Riesz Representers for the Rest of Us（理论框架）、Combining Observational Studies to Reduce Multiple Biases（方法创新）、Generalizing Findings in Nested Cohorts 和 Extending Inferences from a Randomized Trial（外推应用）；测量误差方向，Differential Misclassification by Time 是唯一专门处理时变偏倚的论文；高维或机器学习方向，本期没有直接涉及，但HTE-Scan（Identifying Demographic Predictors）和增强合成控制（Changes in Community-level Pedestrian Stops）涉及机器学习工具在效应异质性和政策评估中的应用。

## 因果推断  *(causal_inference, 5 篇)*

### 1. [10.1097/ede.0000000000001999](https://doi.org/10.1097/ede.0000000000001999) — Combining Observational Studies to Reduce Multiple Biases
- **作者**: Stephen R. Cole, Paul N. Zivich, Bonnie E. Shook-Sa, David B. Richardson, Michael G. Hudgens, Jessie K. Edwards
- **期刊/来源**: Epidemiology
- **机构**: University of North Carolina at Chapel Hill · University of Oxford · University of California, Irvine
- **分类**: vol 37 · issue 5 · pp 565-574
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文提出一种融合设计（fusion design），旨在结合两个观测性研究的数据，同时校正混杂偏倚和结局测量误差。设定中，研究一有充分的混杂控制但结局存在误分类，研究二有金标准结局但混杂控制不足；目标是估计平均结局或处理效应。方法上，作者分别构建了逆概率加权（IPW）、g-computation 和增强逆概率加权（AIPW）三类估计量，通过将研究一的结局模型与研究二的混杂校正模型相结合，实现双重偏倚的消除。Monte Carlo 实验表明，所提估计量在有限样本下能同时去除混杂和测量偏倚，且 95% 置信区间覆盖良好，而标准分析则存在明显偏差。该设计为流行病学中多源数据整合提供了原则性框架，其估计量构造与半参数效率理论中的增强估计思想一脉相承。对您而言，本文是因果推断中数据融合与测量误差校正的典型应用，其 AIPW 构造可联系您的效率理论兴趣，且流行病学应用场景与您的 secondary interest 直接相关。
- **关键技术**: `inverse probability weighting`, `g-computation`, `augmented inverse probability weighting`, `measurement error correction`, `data fusion design`
- **为什么对您有用**: 本文直接关联您的因果推断兴趣中的测量误差与数据融合子方向，且属于流行病学应用。您可用 very_familiar 的估计理论（如 influence function 推导）来审视其 AIPW 估计量的效率性质，或检验其方差估计是否达到半参数效率界。中期可做：若想深入推广到更复杂的偏倚结构，需在 semiparametric theory 上再积累（moderately_familiar）。总体而言，本文是值得一读的应用型方法论文，但方法学 novelty 有限。

### 2. [10.1097/ede.0000000000002012](https://doi.org/10.1097/ede.0000000000002012) — Generalizing Findings in Nested Cohorts
- **作者**: Ashley I. Naimi, Ya-Hui Yu, Sara M. Parisi, Lisa M. Bodnar
- **期刊/来源**: Epidemiology
- **机构**: Emory University · University of Pittsburgh
- **分类**: vol 37 · issue 5 · pp 578-581
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文在嵌套队列（nested cohort）框架下，目标是将在源样本（nuMoM2b-HHS）中估计的肥胖与子痫前期关联推广回目标总体（nuMoM2b），采用逆概率选择加权（IPW）方法构建权重，并估计三个风险比：目标样本、源样本、以及加权源样本。结果显示加权后的风险比（2.0）与目标样本（2.0）一致，而源样本未加权时略有偏差（2.2），表明选择偏差可被校正。作者讨论了推广所需的假设（如可忽略性、正性）及现有方法，强调在嵌套队列研究中应常规使用此类推广技术。对您而言，本文是因果推断中外部有效性（generalizability）的简洁应用示例，与您的因果推断兴趣中的估计方法直接相关，但方法学新颖性有限。
- **关键技术**: `inverse probability of selection weighting`, `generalizability`, `nested cohort`, `risk ratio estimation`
- **为什么对您有用**: 本文属于流行病学应用，直接关联您的secondary interest中的流行病学因果推断应用，且展示了IPW在推广估计中的具体操作。作为gateway reading，它清晰说明了推广的假设和步骤，适合入门；但方法学深度有限，您的武器库（如IPW、因果推断估计）足以理解并复现，无需额外工具。

### 3. [10.1097/ede.0000000000001994](https://doi.org/10.1097/ede.0000000000001994) — Extending Inferences from a Randomized Trial to Trial-eligible and Treatment-candidate Target Populations: Examples of Generalizability and Transportability
- **作者**: Jessica C. Young, Issa J. Dahabreh, Stefan James, David Erlinge, Ole Fröbert, Anita Berglund et al.
- **期刊/来源**: Epidemiology
- **机构**: Karolinska Institutet · Quantify Research (Sweden) · Beth Israel Deaconess Medical Center · Harvard University · Uppsala University · Lund University · Skåne University Hospital · Aarhus University 等
- **分类**: vol 37 · issue 5 · pp 603-611
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文在随机试验外推（generalizability/transportability）框架下，将VALIDATE-SWEDEHEART试验的因果效应估计扩展到两个目标人群：试验合格人群（trial-eligible）和治疗候选人群（treatment-candidate）。目标估计量为各治疗组的180天结局风险及风险差/风险比，通过将试验数据中的结局模型标准化到目标人群的基线协变量分布上实现。方法上采用逻辑回归拟合结局模型，并利用瑞典医疗登记数据刻画目标人群的协变量分布，属于g-标准化（g-standardization）的直接应用。结果显示风险比与试验内部估计接近，但绝对风险略高，提示外推时需关注绝对风险的校准。本文是方法学应用型论文，未提出新理论，但展示了外推估计在真实数据中的完整流程，对您从事流行病学应用因果推断研究有参考价值。
- **关键技术**: `g-standardization`, `logistic regression`, `target population inference`, `generalizability and transportability`, `registry data`
- **为什么对您有用**: 本文属于流行病学领域的应用因果推断，直接对应您的secondary interest中的流行病学应用因果工作。您可以用very_familiar的估计理论（如g-formula）快速复现其标准化步骤，并考虑用semiparametric theory（moderately_familiar）评估其估计的效率损失。中期可做：若想深入，需在transportability的识别条件上加强（moderately_familiar的identification theory）。

### 4. [10.1097/ede.0000000000002002](https://doi.org/10.1097/ede.0000000000002002) — The Long Arm of Childhood Policy: Historical Schooling Laws and COVID-19 Pandemic-era Mortality
- **作者**: Whitney Wells, Yea-Hung Chen, Rafeya V. Raquib, Marie-Laure Charpignon, Ah-Reum Lee, Ruijia Chen et al.
- **期刊/来源**: Epidemiology
- **机构**: University of California, San Francisco · Boston University · Boston Children's Hospital · Kaiser Permanente · Kaiser Permanente Northern California · University of California, Berkeley · Stanford University
- **分类**: vol 37 · issue 5 · pp 654-661
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文利用美国各州历史上的义务教育法（CSLs）作为自然实验，评估教育对老年人群COVID-19死亡率及全因死亡率的长期因果效应。研究将2019年美国社区调查的老年人个体数据与各州在其学龄期的CSL要求相链接，采用控制出生年份、性别、种族、州级人口特征及出生州固定效应的回归模型，估计CSL对个体死亡结局的影响。结果显示，每增加一年强制教育年限与COVID-19死亡率降低相关（如8年vs9年的OR=1.16），且该梯度在黑人女性中最为陡峭。研究结论支持教育政策对几十年后人口健康的因果影响。对您而言，该文是流行病学中利用政策自然实验进行因果推断的典型应用，其识别策略和固定效应设计可借鉴于您的因果推断研究。
- **关键技术**: `natural experiment`, `compulsory schooling laws`, `fixed effects`, `instrumental variables`, `causal inference`
- **为什么对您有用**: 该文属于流行病学领域的应用因果推断，直接关联您的secondary interest中的流行病学应用。其利用政策变化作为自然实验的识别策略，与您的因果推断工具（如IV）高度相关。您可以用very_familiar的估计理论来审视其固定效应模型的假设，或用moderately_familiar的识别理论来评估其因果解释的稳健性。中期可做：若想深入，可考虑用更精细的因果推断方法（如工具变量）重新分析，但需先熟悉相关数据。

### 5. [10.1097/ede.0000000000001995](https://doi.org/10.1097/ede.0000000000001995) — Pooled Multinomial Logistic Regression for Parametric G-computation in the Presence of Competing Events
- **作者**: Lucas M. Neuroth, Monica E. Swilley-Martinez, Paul N. Zivich, Jessie K. Edwards
- **期刊/来源**: Epidemiology
- **机构**: University of North Carolina at Chapel Hill
- **分类**: vol 37 · issue 5 · pp 591-595
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对存在竞争事件时的参数化 g-computation 方法，提出用单一 pooled multinomial logistic 模型替代多个 pooled logistic 回归模型来估计总效应。在 Women’s Interagency HIV Study（n=1,164）中，估计了 2 年 HAART 启动和 AIDS/死亡（作为竞争事件）的边际风险，并比较了两种实现。两种方法结果完全一致，例如历史注射吸毒对 HAART 启动的风险差为 -12.5%（95% CI: -18.0%, -7.0%），对 AIDS/死亡为 13.2%（6.8%, 19.7%）。该方法简化了参数化 g-computation 的估计过程，同时正确处理了右删失和竞争事件。对您而言，这为纵向因果推断中的竞争风险问题提供了一个更简洁的 nuisance 模型选择，可直接应用于流行病学队列研究。
- **关键技术**: `parametric g-computation`, `pooled multinomial logistic regression`, `competing risks`, `marginal risk difference`, `right-censoring`
- **为什么对您有用**: 本文属于流行病学应用，使用参数化 g-computation 估计总效应，与您的因果推断（纵向、竞争事件）和流行病学应用兴趣直接相关。虽然方法新颖性有限（主要是实现简化），但数据集和分析流程（处理右删失和竞争事件）具有参考价值。从武器库看，您对 g-computation 和因果推断估计已很熟悉，可立即理解并复现该方法；中期可考虑将其扩展到更灵活的 nuisance 模型（如使用 HOIF 提高鲁棒性）。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1097/ede.0000000000001996](https://doi.org/10.1097/ede.0000000000001996) · [arXiv](https://arxiv.org/abs/2507.19413) — Riesz Representers for the Rest of Us
- **作者**: Nicholas T. Williams, Oliver J. Hines, Kara E. Rudolph
- **期刊/来源**: Epidemiology
- **机构**: Columbia University
- **分类**: vol 37 · issue 5 · pp 596-602
- 相关性 8/10 · novelty: `survey`
- **摘要**: 本文面向流行病学与因果推断研究者，旨在以非技术方式介绍 Riesz 表示定理及其在 semiparametric efficient estimation 中的作用。作者通过逐步演算的实例，展示了如何将目标泛函（如 ATE、ATT 等）表示为对 nuisance 函数（即 Riesz representer）的期望，并说明 Riesz regression 如何用于构造正交得分（orthogonal score）以实现对 nuisance 估计误差的一阶不敏感性。文章强调了 Riesz representer 在 double/debiased machine learning 框架中的核心地位，并解释了为何其估计的收敛速度要求可放宽至 n^{-1/4}。作为教学性综述，本文不提出新方法，但为流行病学应用者提供了理解现代 semiparametric 估计器的直观桥梁。对您而言，这是一篇极佳的入门读物，可快速厘清 Riesz 表示与 influence function 之间的联系，尤其适合用于教学或向合作者解释 DML 的机制。
- **关键技术**: `Riesz representation theorem`, `Riesz regression`, `orthogonal score`, `semiparametric efficiency`, `double machine learning`
- **为什么对您有用**: 本文直接关联您的效率理论（semiparametric efficiency bounds, debiased ML）与流行病学应用兴趣，作为 gateway reading 非常合适：它清晰解释了 Riesz representer 在正交得分中的角色，而您对 influence function 和 semiparametric 理论已很熟悉，足以支撑快速理解。武器库中的 semiparametric theory 和 estimation theory in causal inference 足以覆盖本文内容，因此立即可读，且可作为向流行病学合作者解释 DML 的现成材料。

## 流行病学  *(epidemiology, 10 篇)*

### 1. [10.1097/ede.0000000000002000](https://doi.org/10.1097/ede.0000000000002000) — Changes in Community-level Pedestrian Stops Following Overdose Prevention Center Implementation in New York City: An Augmented Synthetic Control Approach
- **作者**: Ignacio Bórquez, Bennett Allen, Cale Basaraba, Audrey Renson, Brandi Moore, Brandon D. L. Marshall et al.
- **期刊/来源**: Epidemiology
- **机构**: New York University · Brown University
- **分类**: vol 37 · issue 5 · pp 667-678
- 相关性 7/10 · novelty: `application`
- **摘要**: 本研究评估纽约市两家过量预防中心（OPC）开设对周边社区行人拦截（pedestrian stops）数量的影响，采用增强合成控制法（augmented synthetic control）进行因果推断。数据来自纽约警察局拦截搜身项目（2017-2024），以5分钟和10分钟步行缓冲区内的双月平均拦截数为结局，57个注射服务或阿片治疗点作为供体单元，协变量包括社区人口、警务呼叫和移动出行数据。结果显示华盛顿高地OPC在5分钟缓冲区内ATT为-2.8（95%CI: -9.4, 4.0），10分钟缓冲区为-9.2（95%CI: -18.3, -1.3）；东哈莱姆OPC在两种距离下ATT分别为-8.4（95%CI: -12.2, -4.5）和-13.7（95%CI: -22.1, -4.2）。置换检验表明效应落在供体单元安慰剂效应范围内，结论为证据有限，可能效应集中在东哈莱姆前两年。对您而言，本文是流行病学中合成控制法应用的实例，其增强版本（augmented synthetic control）与您的因果推断兴趣（尤其是纵向设定）相关，可作为方法学参考。
- **关键技术**: `augmented synthetic control`, `permutation test`, `placebo effects`, `donor pool`, `walking buffer`
- **为什么对您有用**: 本文属于流行病学应用，使用增强合成控制法评估社区干预效应，与您的secondary interest（流行病学应用因果推断）直接相关。您可用very_familiar的估计理论（如最小化均方误差的权重选择）审视其合成控制权重构造，或用moderately_familiar的识别理论（如平行趋势假设）评估其因果解释。作为gateway reading，本文方法清晰、数据公开，适合作为进入合成控制法的入门读物，武器库足以支撑理解，值得花时间读全文。

### 2. [10.1097/ede.0000000000001992](https://doi.org/10.1097/ede.0000000000001992) — Identifying Demographic Predictors of Increased Nonfatal Opioid Overdose Risk Among New York State Medicaid Enrollees After the COVID-19 Pandemic: An Analysis of Heterogeneous Treatment Effects
- **作者**: John R. Pamplin, Katherine Wheeler-Martin, Allison Perry, Zachary Mannes, Noa Krawczyk, Stephen Crystal et al.
- **期刊/来源**: Epidemiology
- **机构**: New York University · Columbia University · Columbia University Irving Medical Center · Rutgers, The State University of New Jersey · New York State Psychiatric Institute · Courant Institute of Mathematical Sciences
- **分类**: vol 37 · issue 5 · pp 640-650
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文利用纽约州2019-2020年102万Medicaid参保者的回顾性队列数据，估计COVID-19疫情爆发对非致命性阿片类药物过量风险的异质性处理效应。目标估计量为疫情爆发这一‘处理’对个体过量风险的因果效应，但识别依赖于未明确讨论的假设（如无未测量混杂）。方法上采用Heterogeneous Treatment Effect-Scan（HTE-Scan），一种基于机器学习的高效子群发现算法，通过扫描特征空间识别风险增幅显著高于总体的子群，并控制多重比较。结果显示总体风险增加22%，并识别出两个高风险子群：45-64岁无基线OUD记录的黑人和西班牙裔男性（风险增加54%），以及45-64岁有老年/盲/残疾状态且无基线OUD记录者（风险增加57%）。结论强调结构性因素在复杂社会事件后驱动过量风险异质性中的重要性。对您而言，本文是流行病学中应用因果推断方法（异质性处理效应发现）的实例，其HTE-Scan方法可能与您关注的因果推断子方向（如异质性效应估计）相关，但方法学新颖性有限，更多是应用示范。
- **关键技术**: `Heterogeneous Treatment Effect-Scan (HTE-Scan)`, `subgroup discovery`, `machine learning`, `retrospective cohort`, `multiple testing control`
- **为什么对您有用**: 本文属于流行病学应用，使用因果推断中的异质性处理效应方法，与您的secondary interest（流行病学应用）直接相关。作为gateway reading，本文数据规模大、问题实际，但方法学上HTE-Scan并非您武器库中的核心工具（如DML或semiparametric方法），您可用very_familiar的估计理论评估其子群发现的统计性质，但无需深入。武器库足以理解其分析流程，但若要改进方法（如更严格的因果识别），需补充identification theory（moderately_familiar）。总体而言，值得作为流行病学应用案例阅读，但非方法学突破。

### 3. [10.1097/ede.0000000000002008](https://doi.org/10.1097/ede.0000000000002008) — Differential Misclassification by Time: A Proposed Validation Substudy Design to Account for Time Trends in Bias Parameters
- **作者**: Katherine A. Lawson-Michod, Julie Barberio, Richard F. MacLehose, Thomas P. Ahern, Timothy L. Lash, Lindsay J. Collin
- **期刊/来源**: Epidemiology
- **机构**: University of Utah · Huntsman Cancer Institute · Emory University · University of Minnesota · University of Vermont · University of Vermont Medical Center
- **分类**: vol 37 · issue 5 · pp 582-590
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对长期随访队列中暴露或结局分类误差随时间变化的问题，提出了一种验证子研究设计，以估计随时间变化的阳性预测值（PPV）和阴性预测值（NPV）。作者通过模拟10,000人的队列，在三种场景（无时间趋势但暴露患病率变化、线性时间趋势、对数时间趋势）下诱导暴露错分，并在随访的开始、中期和末期进行验证抽样。利用这些验证数据，以时间为函数插补整个研究期间的PPV和NPV，并与真实值比较。结果表明，在存在时间趋势时，有目的的抽样（purposeful sampling）能够准确估计随时间变化的预测值，且当验证子研究覆盖较大比例的暴露/结局层时，估计最接近真实值。结论建议，当分类参数存在时间趋势时，应使用允许估计时变预测值的设计，而非传统估计单一汇总分类参数的验证设计。对您而言，本文是流行病学中定量偏倚分析（quantitative bias analysis）的应用实例，其模拟和插补框架可迁移至您关注的因果推断中的测量误差问题。
- **关键技术**: `validation substudy design`, `purposeful sampling`, `predictive value imputation`, `quantitative bias analysis`, `simulation study`
- **为什么对您有用**: 本文属于流行病学应用，涉及因果推断中的测量误差和偏倚校正，与您的secondary interest（流行病学应用）直接相关。作为gateway reading，本文清晰展示了验证子研究设计和模拟方法，适合作为入门读物；您的武器库（如模拟、插补）足以支撑理解，但方法学新颖性有限，属于应用型工作，值得快速浏览以了解领域实践。

### 4. [10.1097/ede.0000000000002004](https://doi.org/10.1097/ede.0000000000002004) — A Novel Transmission Model-based Method to Evaluate Population Attribution Methods for Norovirus and Rotavirus Diarrhea
- **作者**: Dehao Chen, Kayoko Shioda, Andrew F. Brouwer, Alicia N.M. Kraay, Andreas Handel, Benjamin A. Lopman et al.
- **期刊/来源**: Epidemiology
- **机构**: Emory University · Boston University · University of Michigan · Gates Foundation · Institute for Disease Modeling · University of Georgia
- **分类**: vol 37 · issue 5 · pp 620-628
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对肠道病原体（诺如病毒和轮状病毒）腹泻负担的归因估计问题，比较了三种传统人群归因分数（PAF）计算方法（detection-as-etiology、odds-ratio、risk-ratio）与基于传播机制模型得到的模型化PAF。作者利用MAL-ED八国出生队列的qPCR检测数据拟合传播模型，以模型平衡态计算参考PAF，并量化传统方法的偏差。结果显示，odds-ratio和risk-ratio方法的偏差较小（-5%至+3%），而detection-as-etiology方法一致高估PAF且偏差最大。该研究为评估PAF估计方法提供了独立的机制模型基准，验证了基于比值比和风险比的方法在肠道负担量化中的可行性。对您而言，本文展示了在流行病学应用中如何用机制模型作为ground truth来评估统计估计量，这与您在因果推断中关注估计量偏差和识别假设的兴趣点相呼应。
- **关键技术**: `population attributable fraction`, `transmission model`, `mechanistic model`, `qPCR data`, `bias quantification`
- **为什么对您有用**: 本文属于流行病学应用，使用机制模型作为参考来评估统计估计方法，与您的secondary interest（流行病学应用）相关。作为gateway reading，本文清晰展示了数据（qPCR检测）和模型（传播模型）的设定，适合入门。您的武器库（如估计理论、因果推断）足以理解其方法，但本文方法学新颖性有限，主要价值在于应用和比较框架。

### 5. [10.1097/ede.0000000000002009](https://doi.org/10.1097/ede.0000000000002009) — Longitudinal Transitions Between Internalizing and Externalizing Symptoms and Associations with Substance Use among US Young Adults, 2016–2023
- **作者**: Dae-Hee Han, Katherine M. Keyes
- **期刊/来源**: Epidemiology
- **机构**: Emory University · Winship Cancer Institute · Columbia University
- **分类**: vol 37 · issue 5 · pp 679-687
- 相关性 5/10 · novelty: `application`
- **摘要**: 本研究利用美国烟草与健康人口评估研究（PATH）2016-2023年四波纵向数据（N=5,575），对18-24岁年轻成人中内化症状（如抑郁、焦虑）与外化症状（如攻击、冲动）的四种状态（无/低症状、纯内化、纯外化、共病）进行Markov多状态转移建模，估计状态转移概率，并考察当前尼古丁使用、暴饮、大麻使用、处方药滥用及社会人口特征与状态转移的关联。结果显示，基线时共病状态占13.9%，从纯内化或纯外化向共病转移的概率在短期（下一波）分别达21.6%和19.7%，共病状态稳定性高于单一症状状态。尼古丁使用与从无/低症状向内化转移相关，暴饮和处方药滥用与外化转移相关，大麻使用与内化和外化转移均相关。该研究为纵向因果推断中状态转移的实证分析提供了范例，但其方法学贡献有限，主要依赖标准Markov模型，未涉及因果识别的高级策略。对您而言，本文可作为流行病学纵向队列研究中多状态建模的应用参考，但方法学上无显著新意。
- **关键技术**: `Markov multistate transition modeling`, `prospective cohort study`, `longitudinal data analysis`, `transition probabilities`
- **为什么对您有用**: 本文属于流行病学应用研究，涉及纵向数据中的状态转移建模，与您的secondary interest（流行病学应用、因果推断）相关。但方法学上仅使用标准Markov模型，未涉及因果推断的高级策略（如IV、DML），因此作为应用案例可读，但方法学迁移价值有限。您的武器库（如semiparametric theory、causal inference identification）足以理解并批判性评估其建模假设，但无需深入。

### 6. [10.1097/ede.0000000000002007](https://doi.org/10.1097/ede.0000000000002007) — Lagged and Nonlinear Effects of Temperature Extremes on Mortality in US Federal Prisons: A Case-Crossover Study, 2009–2021
- **作者**: Kristen N. Cowan, Jérémie Boudreault, Katherine LeMasters, Lauren Brinkley-Rubinstein
- **期刊/来源**: Epidemiology
- **机构**: University at Buffalo, State University of New York · Institut National de la Recherche Scientifique · University of Colorado Anschutz · Duke University
- **分类**: vol 37 · issue 5 · pp 698-708
- 相关性 5/10 · novelty: `application`
- **摘要**: 本研究旨在估计美国联邦监狱中环境温度与全因死亡率之间的关联，采用2009-2021年的死亡数据与日均温度数据，聚焦极端温度事件对弱势群体的健康影响。方法上，研究使用病例交叉设计（case-crossover design）结合分布式滞后非线性模型（DLNM），分别分析热季（5-9月）和冷季（11-3月）的温度-死亡关系，并以各监狱中位温度为参照，估计极端温度百分位（5th和95th）的死亡比值比（OR）。结果显示，在5,182例死亡中，极端高温（95th）和极端低温（5th）的累积效应呈保护性但估计不精确；然而，在特定滞后天数（高温滞后2天，低温当天）观察到死亡风险增加。结论指出，联邦监狱的结果与先前州监狱研究不同，强调未来需改进室内温度暴露估计并量化空调可及性。对您而言，本文是流行病学中因果推断的典型应用，其病例交叉设计和DLNM的联合使用为纵向数据中的暴露-结局关联提供了可借鉴的分析框架。
- **关键技术**: `case-crossover design`, `distributed lag nonlinear models`, `conditional logistic regression`, `temperature-mortality association`, `lagged effects`
- **为什么对您有用**: 本文属于流行病学应用，直接关联您的secondary interest中的流行病学因果推断。病例交叉设计是控制时间不变混杂的经典方法，DLNM则处理非线性滞后效应，两者结合的分析流程对您理解纵向因果推断的实际操作有参考价值。从技术武器库看，您对因果推断的identification theory和估计方法很熟悉，足以理解本文的设计和模型，但本文未涉及高级方法（如DML或proximal CI），因此作为入门级应用阅读，可快速把握领域常用工具。

### 7. [10.1097/ede.0000000000002006](https://doi.org/10.1097/ede.0000000000002006) — Smart Meter-derived Air Conditioning Penetration Rate Modifies the Association Between Ambient Temperature and Emergency Department Visits
- **作者**: Xiaping Zheng, McKenna Peplinski, Diego Ramos Aguilera, Kelly T. Sanders, Stefanie Ebelt, Noah Scovronick et al.
- **期刊/来源**: Epidemiology
- **机构**: Emory University · University of Southern California · Jet Propulsion Laboratory
- **分类**: vol 37 · issue 5 · pp 719-723
- 相关性 5/10 · novelty: `application`
- **摘要**: 本研究利用南加州2015-2019年家庭智能电表数据，在ZIP代码层面估计空调普及率，并考察其对环境温度与急诊就诊关联的效应修饰作用。作者先估计各ZIP代码在温度第95至第50百分位数范围内，热相关急诊就诊相对风险（RR）与滞后4天温度的关系，再通过meta回归估计效应修饰，以RR之比衡量。结果显示非沿海地区空调普及率每增加10%，热相关急诊风险降低（干球温度RR比=0.79，湿球温度RR比=0.80），而沿海地区无显著修饰作用。该研究将空调暴露从粗粒度提升至社区尺度，为热健康效应评估提供了更精细的暴露指标。对您而言，这是一篇流行病学应用论文，其meta回归框架和效应修饰分析思路可迁移至因果推断中的异质性效应评估。
- **关键技术**: `meta-regression`, `effect modification`, `relative risk ratio`, `smart meter data`, `ZIP code-level exposure`
- **为什么对您有用**: 本文属于流行病学应用，使用meta回归评估效应修饰，与您的流行病学应用兴趣相关；其分析模式（先估计区域特定效应，再回归修饰因子）可迁移至因果推断中的异质性效应研究。武器库中的M-estimation理论可用于理解meta回归估计的性质，但本文方法较简单，无需新工具。作为gateway reading，本文数据来源新颖（智能电表），但方法学贡献有限，适合快速浏览。

### 8. [10.1097/ede.0000000000002005](https://doi.org/10.1097/ede.0000000000002005) — Industrial Air Toxicant Exposure and Individual Mortality: Evidence from the Americans’ Changing Lives Cohort, 1986–2019
- **作者**: Reed T. DeAngelis, Lindsey Burnside, David Rigby, Paul Mohai, Devon Payne-Sturges, Margaret T. Hicken
- **期刊/来源**: Epidemiology
- **机构**: University of Michigan · Institute for Social Research
- **分类**: vol 37 · issue 5 · pp 709-718
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文利用美国全国代表性队列 Americans' Changing Lives（1986–2019，N=3329）与 EPA 的 Risk-Screening Environmental Indicators 地理微数据，研究工业空气毒物暴露对个体死亡风险的影响。暴露变量为受访者住所周围 1–25 km 五个环形缓冲区内记录的毒物水平，结局为随访期间的死亡时间。方法上采用加速失效时间-共享脆弱模型（AFT-shared frailty），以控制未观测的个体间异质性，并纳入时变个体与区域层面协变量。主要发现包括：毒物暴露与死亡风险呈非线性关联，低暴露区居民平均寿命仍短 1–2 年；关联随缓冲区半径增大而增强（最污染 25-km 缓冲区居民平均短寿 4 年）；非西班牙裔黑人、低收入及高贫困社区人群的关联更强。该研究为环境流行病学中暴露测量尺度与效应异质性提供了实证证据，但其方法学新颖性有限，核心价值在于数据集与分析流程。
- **关键技术**: `accelerated failure time model`, `shared frailty model`, `time-varying exposure`, `spatial buffers`, `prospective cohort analysis`
- **为什么对您有用**: 本文属于流行病学应用型论文，可作为环境健康因果推断的入门读物，展示了暴露测量（多尺度缓冲区）与生存分析（AFT-frailty）的结合方式。您的武器库（如生存分析、因果推断中的时变暴露处理）足以支撑理解其方法，但若要深入批判其未观测混杂处理（frailty 假设）或暴露-响应非线性建模，需补充环境暴露评估知识。值得花时间读全文以获取数据集和分析流程的细节，但方法学迁移价值有限。

### 9. [10.1097/ede.0000000000001993](https://doi.org/10.1097/ede.0000000000001993) — The Separate and Joint Associations of Own and Spousal Depression with Mortality in Couples
- **作者**: Toshiaki Komura, Säde Stenlund, Laura D. Kubzansky
- **期刊/来源**: Epidemiology
- **机构**: Harvard University · University of Turku · Turku University Hospital
- **分类**: vol 37 · issue 5 · pp 688-697
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文利用美国健康与退休研究（HRS）中 8442 名老年人（4225 对夫妻）的全国代表性样本，评估夫妻双方抑郁状态对个体 11 年死亡风险的联合与独立关联。抑郁状态分为四类：双方均无抑郁、仅本人抑郁、仅配偶抑郁、双方均抑郁，使用 Cox 比例风险模型估计死亡风险比，并调整了 27 个个体、配偶及家庭层面的协变量。结果显示，仅本人抑郁时死亡风险比（HR）为 1.44（95% CI: 1.26, 1.66），仅配偶抑郁时 HR 为 1.18（95% CI: 1.01, 1.39），双方均抑郁时 HR 为 1.53（95% CI: 1.26, 1.86），表明配偶抑郁对个体死亡风险有独立且叠加的影响。该研究为流行病学中家庭背景对健康影响的证据提供了新视角，但作为应用性论文，方法学新颖性有限，主要价值在于数据集和分析模式。对您而言，本文可作为流行病学队列研究中因果推断（如配偶效应）的应用案例，但需注意其观察性设计可能存在的未测量混杂问题。
- **关键技术**: `Cox proportional hazards model`, `Health and Retirement Study`, `couple-level exposure classification`, `confounder adjustment`
- **为什么对您有用**: 本文属于流行病学应用研究，直接关联您的 secondary interest 中的流行病学队列研究。作为 gateway reading，本文数据描述清晰，方法常规，适合作为流行病学数据分析的入门读物。您的武器库（如 Cox 模型、混杂调整）足以理解全文，但若要深入探讨配偶效应的因果解释，可能需要更复杂的因果推断方法（如敏感性分析），这属于 moderately_familiar 领域，可中期拓展。总体而言，值得花时间阅读全文以了解 HRS 数据结构和分析流程。

### 10. [10.1097/ede.0000000000002013](https://doi.org/10.1097/ede.0000000000002013) — Stratification and Accumulation?: Explaining Changing Mortality Inequities Between Business Owners and Non-owners in the United States (1984–2022)
- **作者**: Jerzy Eisenberg-Guyot, Seth J. Prins, Anita Minh, Anjum Hajat, Audrey Renson
- **期刊/来源**: Epidemiology
- **机构**: New York University · SUNY Downstate Health Sciences University · Portland State University · Oregon Health & Science University · University of Washington
- **分类**: vol 37 · issue 5 · pp 629-639
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文利用1984-2013年PSID纵向数据（22,103名受访者，103,965个观测），通过g-computation估计美国25-64岁企业主与非企业主之间10年年龄调整死亡风险的差异及其随时间的变化。研究发现，非企业主相对企业主的死亡风险比从1984年的1.4上升到2013年的2.3，风险比之比为1.7（95% CI: 1.1, 2.5），表明阶级间死亡不平等显著扩大。作者进一步通过调整社会分层（如职业、教育等）来分解变化，发现分层调整后年内不平等减弱，但跨年增加仅部分衰减（风险比之比降至1.5）。最后，反事实分析显示，若收入和财富分布保持在1984年水平，不平等增加并未显著减轻，说明个体层面的收入和财富差异不能完全解释趋势。该研究展示了纵向因果推断方法（g-computation）在流行病学社会不平等研究中的应用，对您作为流行病学应用因果推断方向的参考有价值。
- **关键技术**: `g-computation`, `longitudinal causal inference`, `counterfactual decomposition`, `age-adjusted mortality risk`, `Panel Study of Income Dynamics`
- **为什么对您有用**: 本文是流行病学领域应用因果推断方法的实证研究，直接关联您的secondary interest中的流行病学应用因果推断方向。它展示了g-computation在纵向数据中估计和分解因果效应的完整流程，您可以用您very_familiar的估计理论（如g-formula的渐近性质）来审视其估计的稳健性，或考虑用更高效的估计量（如TMLE）改进。作为应用论文，其数据和分析流程值得参考，但方法学novelty有限，属于中期可做的范畴，需先熟悉g-computation的纵向实现细节。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

