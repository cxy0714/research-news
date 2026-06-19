# Epidemiology — Vol 36  Issue 6  ·  2026-06-19

- 共 13 篇 · Epidemiology
- 目录核对 ⚠️ 疑似漏 1 篇（对照 OpenAlex 14 篇）：10.1097/ede.0000000000001904

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Epidemiology》围绕流行病学因果推断中的方法论挑战展开，核心关注三类问题：**因果识别框架与估计策略**、**纵向因果推断中的时间相关偏倚**、以及**测量误差与左截断的修正**。此外，若干论文展示了机器学习在估计与分解中的角色，以及自然实验在应用中的识别逻辑。各条主线的主要论文如下：因果识别方面有“Causal Approaches to Disease Progression”“Illustrating an Adaptive Prespecification”“Algorithm Selection for Estimating Causal Effects”；纵向因果与时间偏差方面有“Time-related Bias”“Reducing Prescription Opioid Dose”“Is Checking for Sequential Positivity”（sPoRT）和“Does Delayed Response”；测量误差与左截断方面有“Addressing Measurement Error”“Impact of Washout Duration”；实证应用方面有“Life Course Financial Hardship”“Disaggregating Health Differences”。

**纵向因果推断与时间相关偏倚**是本期最突出的线索。“Time-related Bias”直接对比时间固定与时变暴露定义对早产效应的估计，展示 immortal-time bias 的修正机制。“Reducing Prescription Opioid Dose”采用局部修正治疗策略，在序贯时间点定义干预并校正删失，以评估剂量/时长降低对成瘾风险的因果效应。“sPoRT”则聚焦于纵向边际结构模型中顺序正性违反的诊断，通过回归树自动识别问题子组并给出处理建议，增强正性假设的可操作性。“Does Delayed Response”利用急救车忙碌程度的外生变异作为自然实验，估计响应延迟对死亡和住院的因果作用，为纵向因果识别提供了另一种设计思路。这四篇从不同角度处理了时间-暴露-结局之间的时序关系与识别假设。

**因果识别框架与估计方法**构成另一条主线。“Causal Approaches to Disease Progression”系统区分了疾病发生是否可被干预的设定，论证在不可操纵时 principal stratification 是合适框架，并讨论结局定义对潜在结果可定义性的影响。“Illustrating an Adaptive Prespecification”在 target trial emulation 下提出自适应预指定策略，允许在分阶段盲态下根据预设诊断调整样本限制、治疗定义、倾向评分模型等，提升观察性研究的规范性。“Algorithm Selection for Estimating Causal Effects”比较不同算法库对 AIPW/TMLE 估计 ATE 的影响，发现单一算法（如极端梯度提升）会增大估计变异，而 Super Learner 组合具有稳健性。这三篇分别从概念分类、操作流程、算法稳定性推进因果估计的实践。

此外，测量误差与左截断的修正也有集中讨论。“Addressing Measurement Error”对比多维定量偏差分析与多重过度填补，通过敏感性网格和贝叶斯填补修正自我报告数据中的误报/漏报。“Impact of Washout Duration”则展示不同 washout 期限如何剔除 prevalent case 以处理左截断，并量化对发病率估计的偏倚影响。这两篇为模拟研究与实际数据分析提供了可复用的偏差评估工具。

与因果推断方向最贴的几篇包括：**Causal Approaches to Disease Progression**（提供 principal stratification 框架）、**Is Checking for Sequential Positivity**（纵向正性诊断工具）、**Reducing Prescription Opioid Dose**（局部修正治疗策略的纵向应用）、**Time-related Bias**（时变暴露与 immortal-time 修正），以及**Algorithm Selection for Estimating Causal Effects**（双重稳健估计与算法选择）。它们在识别框架、估计策略、假设诊断上各有推进，适合优先阅读。

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.1097/ede.0000000000001902](https://doi.org/10.1097/ede.0000000000001902) · [arXiv](https://arxiv.org/abs/2412.10245) — Is Checking for Sequential Positivity Violations Getting You Down? Try sPoRT!
- **作者**: Arthur Chatton, Michael Schomaker, Miguel-Angel Luque-Fernandez, Robert W. Platt, Mireille E. Schnitzer
- **期刊/来源**: Epidemiology
- **分类**: vol 36 · issue 6 · pp 751-759
- 相关性 8/10 · novelty: `application`
- **摘要**: 在纵向因果推断（如边际结构模型）中，顺序正性假设常难以直接验证，因其依赖多个可能误设的倾向性得分模型。本文提出 sPoRT（sequential Positivity Regression Tree）算法，通过回归树自动识别违反顺序正性的子组，并给出违反特征与潜在解决方案。算法提供基于时间分层或聚合、静态或动态治疗策略的多种版本，并以 HIV 治疗时机数据做实证演示。主要贡献是增强了正性诊断的可解释性与实用性，避免逐层检查模型。输出易于解读的子组模式，辅助研究者调整估计策略。对您而言，这是纵向因果推断中敏感性分析的一个直接工具，可用 R notebook 快速上手，结合您已有的因果推断估计经验可用于实际数据诊断。
- **关键技术**: `sequential positivity`, `regression tree (CART)`, `marginal structural models`, `positivity violation detection`
- **为什么对您有用**: 直接连接到您 primary interest 中纵向因果推断的 identification/sensitivity analysis 子方向，正性检验是实际估计前的关键诊断步骤。您的 technical arsenal 中的“estimation theory in causal inference”和“software development”允许立即可用——可直接复现 sPoRT 的 R 实现并应用于您手头的纵向数据，或基于树方法扩展其理论性质（如高维协变量下的稳定性）。立即可做。

### 2. [10.1097/ede.0000000000001899](https://doi.org/10.1097/ede.0000000000001899) — Reducing Prescription Opioid Dose and Duration to Reduce Risk of Opioid Use Disorder Among Patients With Musculoskeletal Pain
- **作者**: Shodai Inose, Nicholas T. Williams, Katherine L. Hoffman, Allison Perry, Iván Díaz, Kara E. Rudolph
- **期刊/来源**: Epidemiology
- **机构**: Columbia University · NYU Langone Health
- **分类**: vol 36 · issue 6 · pp 811-819
- 相关性 6/10 · novelty: `application`
- **摘要**: 该研究估计降低处方阿片类药物剂量与持续时间对肌肉疼痛初诊患者发生阿片类药物使用障碍或过量风险的因果效应。利用纽约州Medicaid队列（N=324,389），采用局部修正治疗策略（local modified treatment policies，一种ATT的推广）定义干预，并在15个月随访期内通过序贯3个月时间点估计校正删失后的风险差异。总体而言，将全队列剂量与天数普遍降低20%仅产生临床微弱的绝对风险降低（约0.1个百分点）；但对基线剂量≥90 MME、天数>30天或两者均较高（≥50 MME且>7天）的亚组，相同20%降低可带来约1个百分点以上的临床有意义风险下降。分析使用了纵向因果推断中的g计算公式或逆概率加权，并考虑了时依混杂与删失。该文是modified treatment policies在流行病学中的一个清晰应用，展示了针对高风险人群而非泛化干预的精准策略价值。
- **关键技术**: `local modified treatment policies`, `generalized average treatment effect on the treated`, `longitudinal causal inference`, `g-computation / inverse probability weighting for censoring`
- **为什么对您有用**: 连接到causal inference子方向——modified treatment policies的估计与解释，以及流行病学中的实际应用。您对causal inference estimation theory非常熟悉，可立即评估其估计方法（如g-computation或IPW）的假设合理性，并思考是否可用更高效的debiased ML或正交估计量改进。属立即可做：您已有足够武器（estimation theory in causal inference）来批判性阅读并复现其分析。

## 流行病学  *(epidemiology, 11 篇)*

### 1. [10.1097/ede.0000000000001893](https://doi.org/10.1097/ede.0000000000001893) — Causal Approaches to Disease Progression Analyses
- **作者**: Bronner P. Gonçalves, Etsuji Suzuki
- **期刊/来源**: Epidemiology
- **机构**: University of Surrey · Okayama University
- **分类**: vol 36 · issue 6 · pp 732-740
- 相关性 9/10 · novelty: `survey`
- **摘要**: 在流行病学因果推断设定下，本文系统梳理了暴露对疾病进展效应的不同因果估计目标与识别框架。核心区分基于两个维度：疾病发生是否可被干预操纵，以及结局变量的类型。作者引入了由疾病发生与进展的联合潜在结果构成的响应类型集，论证了在疾病发生不可操纵的更常见设定下，principal stratification 是概念化分析的合适框架。进一步指出结局的精确定义（特别是其允许水平的界定）决定了不同人群分层中与进展相关的潜在结果是否可定义。本文为疾病进展的因果分析提供了概念澄清与框架指引，对您在流行病学应用中构建 principal stratification 与识别理论有直接参考价值。
- **关键技术**: `principal stratification`, `response types`, `joint potential outcomes`, `causal estimands`, `manipulability of treatment`
- **为什么对您有用**: 本文直接连接到流行病学因果推断应用，并在疾病发生不可操纵设定下明确推荐 principal stratification 框架，触及您 moderately_familiar 中的 identification theory in causal inference。您可用 very_familiar 的 estimation theory in causal inference 为本文指出的 principal stratification 估计目标构造 semiparametric efficient estimator 或做 sensitivity analysis，属于立即可做的 follow-up 方向。

### 2. [10.1097/ede.0000000000001901](https://doi.org/10.1097/ede.0000000000001901) — Illustrating an Adaptive Prespecification Framework for Observational Research: Target Trial Emulations Comparing Immunomodulator Treatments for COVID-19
- **作者**: Andrew R. Weckstein, Vera Frajzyngier, Sarah E. Vititoe, Aidan Baglivo, Elisha Beebe, Priya Govil et al.
- **期刊/来源**: Epidemiology
- **机构**: Harvard University · Aetion (United States) · Engineering Information Foundation · Federal Reserve · Faculdades Guarulhos · Center for Drug Evaluation and Research · United States Food and Drug Administration · Charles River Associates 等
- **分类**: vol 36 · issue 6 · pp 791-801
- 相关性 8/10 · novelty: `application`
- **摘要**: 在观察性研究的 target trial emulation 框架下，本文针对 COVID-19 免疫调节剂治疗的因果效应估计，提出并演示了一套 adaptive prespecification 策略。核心机制是在预注册协议中预先设定诊断阈值与应对方案，通过分阶段（baseline 与 postbaseline）实施，允许在部分盲态下根据预设规则进行数据驱动的调整。具体调整包括：样本限制、从类别级到产品级的治疗定义重设、倾向评分模型修正与权重截断；postbaseline 阶段诊断触发后，进一步修改因果对比（causal contrast）、引入逆概率截断加权（IPCW）处理非依从、使用 cause-specific hazard 竞争风险估计，以及逐步截断随访期的 HR 报告。实证表明，该框架增强了因果假设的合理性并提升了发现的相关性，同时为迭代尝试提供了明确的停止规则。对您可能有用：本文展示了流行病学应用中如何系统化地处理因果识别假设的脆弱性与分析计划的适应性调整。
- **关键技术**: `target trial emulation`, `adaptive prespecification`, `inverse probability of censoring weighting (IPCW)`, `propensity score model revision`, `cause-specific hazard estimation`, `weight truncation`
- **为什么对您有用**: (1) 直接连接到流行病学（secondary interest）中的因果推断应用，展示了 target trial emulation 框架下处理因果识别假设与分析计划调整的实操流程；(2) 您武器库中 very_familiar 的「identification theory in causal inference」可以直接审视本文中因果对比修改、IPCW 引入等适应性调整对 estimand identification 的影响，判断其假设变动的合理性；(3) **立即可做**：用您熟悉的因果识别理论工具，可以立刻评估此类 adaptive prespecification 框架下 estimand 随诊断触发而变动的 identification 逻辑是否自洽，甚至可提出更严格的 semiparametric efficiency 视角下的敏感性分析框架。

### 3. [10.1097/ede.0000000000001906](https://doi.org/10.1097/ede.0000000000001906) — Algorithm Selection for Estimating Causal Effects: Nulliparous Pregnancy Outcomes Study: Monitoring Mothers to Be
- **作者**: Zhaohua Zeng, Lisa M. Bodnar, Ashley I. Naimi
- **期刊/来源**: Epidemiology
- **机构**: Emory University · University of Pittsburgh
- **分类**: vol 36 · issue 6 · pp 760-768
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文在流行病学背景下，利用 Super Learner 集成学习与双重稳健估计器（AIPW 和 TMLE）估计高孕前水果蔬菜摄入密度与子痫前期风险的平均处理效应（ATE）。数据来自 nuMoM2b 研究（7,923 名孕妇），以风险差为尺度，AIPW 估计 ATE 为 -0.019（95%CI: -0.036, -0.003），TMLE 为 -0.023（95%CI: -0.039, -0.007）。研究系统比较了不同算法库组合对估计的影响，发现排除任一算法对结果影响微小，但仅用单一算法（如 extreme gradient boosting）时估计变异性显著增大。结论支持在双重稳健估计中使用多样化的灵活机器学习算法构建集成模型。该应用为实际流行病学数据分析中算法库选择提供了实证依据，对你在类似队列研究中采用 TMLE 或 AIPW 时的实践操作有直接参考价值。
- **关键技术**: `Super Learner ensemble`, `augmented inverse probability weighting (AIPW)`, `targeted minimum loss-based estimation (TMLE)`, `doubly robust estimation`, `average treatment effect (ATE)`
- **为什么对您有用**: 本文属于流行病学领域的因果推断应用，直接连接你的 secondary interest 中流行病学的应用数据集和因果推断实践。研究中使用的双重稳健估计器（AIPW/TMLE）与 Super Learner 集成属于你 very_familiar 的 estimation theory in causal inference 范畴，你可以用现有的模拟或复现能力快速验证其结论的稳健性，并扩展至其他敏感度分析方法（如你的 proximal CI 兴趣）。立即可做：你的技术武器库足以复现本文分析，甚至进一步探索不同识别假设（如无未测量混杂）对结果的影响。

### 4. [10.1097/ede.0000000000001896](https://doi.org/10.1097/ede.0000000000001896) — Addressing Measurement Error in Intimate Partner Violence Self-report Data Using Multiple Overimputation and Multidimensional Quantitative Bias Analysis
- **作者**: Irina Bergenfeld, Robin A. Richardson, Alexandria R. Hadd, Cari Jo Clark, Regine Haardörfer, Charis Wiltshire et al.
- **期刊/来源**: Epidemiology
- **机构**: Emory University
- **分类**: vol 36 · issue 6 · pp 741-750
- 相关性 7/10 · novelty: `application`
- **摘要**: 在流行病学自我报告数据设定下，目标是修正亲密伴侣暴力（IPV）患病率估计中的测量误差（误报与漏报）。本文对比两种偏差调整方法：多维定量偏差分析（直接对汇总患病率施加敏感性10%–100%、特异性95%–100%的网格进行修正以界定合理范围）与多重过度填补（multiple overimputation，将测量误差先验融入观测值重估并跨50次迭代平均）。理论结果显示，95%特异性假设下部分患病率估计为负值，证实假阳性可忽略；合理敏感性跨国家与IPV类型差异极大，源于问卷条目数不同；多重过度填补修正估计仅在未修正DHS估计<5%且高度偏离时才与原始值显著不同，过去一年估计偏差小于终身估计，提示回忆偏差的作用。对您可能有用：本文展示了在流行病学应用中如何将外部验证数据与测量误差先验结合进行偏差分析，是理解 epi 数据测量误差修正策略的入门案例。
- **关键技术**: `multidimensional quantitative bias analysis`, `multiple overimputation`, `measurement error correction`, `sensitivity-specificity grid adjustment`, `recall bias assessment`
- **为什么对您有用**: 本文属于流行病学应用，连接到 epidemiology secondary interest 中的测量误差与偏差修正实践。从 technical_arsenal 角度，本文的多维偏差分析仅是简单的网格搜索与直接修正，多重过度填补也是标准贝叶斯缺失数据填补的变体，无需动用 very_familiar 或 moderately_familiar 中的高阶工具即可理解与复现。作为 gateway reading：本文对 epi 测量误差问题的数据结构（DHS vs 验证调查）与先验设定阐述清晰，适合作为入门读物了解流行病学中定量偏差分析的实操流程；武器库完全足够支撑进入此方向；但方法学 novelty 有限（novelty_flag=application），不值得花时间深读全文，浏览图表与结论即可。

### 5. [10.1097/ede.0000000000001898](https://doi.org/10.1097/ede.0000000000001898) — Time-related Bias When Studying Perinatal Complications After Maternal Injuries: Application to Maternal Injuries and Preterm Birth
- **作者**: Asma M. Ahmed, Allison Musty, Joseph Rigdon, Jennifer A. Hutcheon
- **期刊/来源**: Epidemiology
- **机构**: Wake Forest University · University of British Columbia
- **分类**: vol 36 · issue 6 · pp 781-790
- 相关性 6/10 · novelty: `application`
- **摘要**: 在围产期流行病学设定下，研究目标是估计孕期母体损伤对早产（<37周）的因果效应，关键问题在于时间固定暴露定义引入的 immortal-time bias 与 selection bias。方法上，对比了 logistic 回归的时间固定分析（暴露为 yes/no）与 Cox 比例风险模型的时间变异分析（暴露为 time-varying，并限制随访至有早产风险的孕期时段）。核心机制在于时间变异方法通过 at-risk 期间的正确对齐避免了 immortal time，从而修正了第三孕期损伤看似"保护性"的伪阴性偏倚。在 58,897 名产妇的回顾性队列中，时间变异方法给出总体调整 HR=1.16 (95% CI 1.01-1.32)，而时间固定方法对第三孕期损伤给出反向的调整 OR=0.73。对您可能有用：本文是流行病学中 time-varying exposure 与 immortal-time bias 的典型应用案例，直接连接到您 causal inference 中的 longitudinal/time-varying 设定。
- ⚠️ *摘要不完整，待重跑（`python -m research_news.rerun`）*
- **关键技术**: `immortal-time bias correction`, `time-varying exposure definition`, `Cox proportional hazards model`, `retrospective cohort study`, `gestational age at-risk restriction`
- **为什么对您有用**: 本文直接连接到您 causal inference 中 longitudinal/time-varying exposure 的 identification 设定，展示了 immortal-time bias 如何破坏 identification 并导致伪保护效应。用您 very_familiar 的 estimation theory in causal inference 即可分析其 Cox 模型与 at-risk 对齐背后的 hazard ratio estimand 的因果解释问题。立即可做：用您熟悉的 causal identification 理论审视其 time-varying Cox HR 的因果含义（是否需要额外假设如 no unmeasured confounding for time-varying treatment），并评估其 sensitivity analysis 的缺失。

### 6. [10.1097/ede.0000000000001892](https://doi.org/10.1097/ede.0000000000001892) — Disaggregating Health Differences and Disparities With Machine Learning and Observed-to-expected Ratios: Application to Major Lower Limb Amputation
- **作者**: Paula D. Strassle, Samantha D. Minc, Corey A. Kalbaugh, Macarius M. Donneyong, Jamie S. Ko, Katharine L. McGinigle
- **期刊/来源**: Epidemiology
- **机构**: National Institutes of Health · National Institute on Minority Health and Health Disparities · University of Maryland, College Park · Duke University · Indiana University Bloomington · Indiana University · The Ohio State University · University of California, Los Angeles 等
- **分类**: vol 36 · issue 6 · pp 841-848
- 相关性 6/10 · novelty: `application`
- **摘要**: 本研究利用2017-2019年佛罗里达、佐治亚等五个州的HCUP住院数据，以主要下肢截肢为结局，探究种族/民族和城乡差异是由临床因素、医院因素还是结构因素所致。方法上使用LASSO筛选协变量，分别构建未调整、仅调整临床因素、以及调整临床+医院+社会决定因素的三类模型，计算观察/期望比率（O/E）并比较。结果显示，调整临床因素后，农村黑人、西班牙裔、原住民和白人以及非农村黑人和原住民仍存在截肢差异；进一步加入医院和社会因素后，农村白人差异消失，但其他种族差异持续存在。该分析表明临床和结构性因素无法完全解释种族间截肢差异，暗示隐性偏见可能发挥作用。对您而言，这是一篇典型的流行病学应用论文，展示了如何利用行政数据和多阶段调整分解差异，但未采用因果推断识别策略。
- **关键技术**: `LASSO`, `observed-to-expected ratio`, `administrative claims data analysis`, `health disparities decomposition`
- **为什么对您有用**: 直接对应您的secondary interest中的流行病学应用方向，展示了真实数据集下的协变量调整分析。您可以用high-dimensional asymptotics武器评估LASSO变量选择的稳定性及预测误差，但论文未使用因果识别框架（如DAG或IV），因此若要将此分析升级为因果解释，需要先在moderately_familiar的identification theory上补充知识——这是中期可做的follow-up方向。

### 7. [10.1097/ede.0000000000001905](https://doi.org/10.1097/ede.0000000000001905) — Impact of Washout Duration to Account for Left Truncation in Register-based Epidemiologic Studies: Estimating the Risk of Mental Disorders
- **作者**: Oleguer Plana-Ripoll, Natalie C. Momen, Dídac Gallego-Alabanda, Danni Chen, Stefan Nygaard Hansen, Guadalupe Gómez Melis et al.
- **期刊/来源**: Epidemiology
- **机构**: Aarhus University · Aarhus University Hospital · Universitat Politècnica de Catalunya
- **分类**: vol 36 · issue 6 · pp 719-729
- 相关性 5/10 · novelty: `application`
- **摘要**: 在基于登记数据（如电子健康记录）的流行病学队列研究中，目标 estimand 为精神障碍的发病率与累积发病率，核心问题是如何通过 washout 期限处理左截断以排除 prevalent case 被误计入风险集所导致的偏倚。本文利用丹麦 2010–2021 年全人群队列（6,478,162 人），分别设定 0 至 41 年的六种 washout 期限，基于历史住院记录识别并剔除 prevalent case，进而估计不同 washout 下的 incidence rate 与 cumulative incidence。结果显示，无 washout 时终生累积发病率高达 49.4%（女）/45.1%（男），而使用最长 41 年 washout 后降至 40.3%/36.6%，特定病种的偏倚幅度最高可达 60%。结论强调行政登记数据若不充分处理左截断，将严重高估风险指标。对您有用：本文提供了流行病学队列中左截断偏倚的大规模实证量化，是理解 register-based 研究中 identification 假设与实际数据差距的具体案例。
- **关键技术**: `left truncation`, `washout period`, `prevalent case exclusion`, `cumulative incidence estimation`, `register-based cohort`, `population-based epidemiology`
- **为什么对您有用**: 本文直接连接到流行病学（secondary interest）中因果推断与观察性研究的 identification 问题——左截断导致的 prevalent case 偏倚本质上是 at-risk 集合的 mis-specification，与因果推断中 selection bias / conditioning on survivors 的结构相似。从 technical_arsenal 看，用您 very_familiar 的因果推断 identification theory 可以将 washout 机制形式化为 DAG 上的 selection 条件，进而推导更一般的 sensitivity analysis 框架（当前论文仅做实证比较，未给理论界）。Follow-up 判断：**中期可做**——需先在 moderately_familiar 的 identification theory 上长肌肉，将左截断偏倚纳入 formal selection-bias 框架并推导偏倚界，这比纯实证 washout 比较更有方法学贡献。

### 8. [10.1097/ede.0000000000001900](https://doi.org/10.1097/ede.0000000000001900) — Life Course Financial Hardship and Fecundability in a North American Preconception Cohort Study
- **作者**: Molly N. Hoffman, Collette N. Ncube, Eleanor J. Murray, Dmitrii Krivorotko, Amelia K. Wesselink, Sharonda M. Lovett et al.
- **期刊/来源**: Epidemiology
- **机构**: Yale University · Boston Medical Center
- **分类**: vol 36 · issue 6 · pp 769-780
- 相关性 5/10 · novelty: `application`
- **摘要**: 在北美孕前队列 PRESTO（N=6377）中，研究生命历程各阶段经济困难对生育力（fecundability）的影响，estimand 为 fecundability ratio（FR）。采用 inverse probability-weighted proportional probabilities model 估计 FR 及 95% CI，以处理时变混杂与选择偏差。结果显示：仅成年期经济困难与生育力显著降低相关（FR=0.83），童年/青春期影响较弱；累积经济困难（成年+早年）效应更强（FR=0.77）。本文为典型流行病学应用，方法学 novelty 有限，但提供了纵向因果设定下 IPW 处理时变混杂的实证范例。
- **关键技术**: `inverse probability weighting`, `proportional probabilities model`, `time-dependent confounding`, `selection bias adjustment`, `fecundability ratio`, `life course epidemiology`
- **为什么对您有用**: 本文属于流行病学应用，直接连接 epidemiology secondary interest 中的因果推断应用。IPW 处理时变混杂的设定与您 primary interest 中的 longitudinal causal inference 有场景重叠，但方法本身（IPW proportional probabilities model）对您而言是 very_familiar 的常规武器。作为 gateway reading，本文数据结构（preconception cohort、随访12个月、多阶段暴露）清晰，适合了解流行病学队列中累积暴露的因果分析范式，但无需花时间读全文——方法细节可快速扫过，关注其时变混杂与选择偏差的调整策略即可。

### 9. [10.1097/ede.0000000000001894](https://doi.org/10.1097/ede.0000000000001894) — Does Delayed Response Due to Busy Ambulances Impact Risk of Death and Hospital Service Use?: A Cohort Study of 240,000 Medical Emergencies
- **作者**: Andreas Asheim, Lars Eide Næss, Andreas Krüger, Oddvar Uleberg, Jostein Dale, Helge Haugland et al.
- **期刊/来源**: Epidemiology
- **机构**: Norwegian University of Science and Technology · St Olav's University Hospital · Stiftelsen Norsk Luftambulanse · University of Oslo · Nord University
- **分类**: vol 36 · issue 6 · pp 830-840
- 相关性 5/10 · novelty: `application`
- **摘要**: 基于挪威中部2013-2022年239,320例急诊数据，评估急救车忙碌导致的响应延迟对患者死亡和住院风险的影响。利用同一区域同时段急救车忙碌程度的外生变化作为自然实验，通过比较不同等待时间的患者结果来识别因果效应。调整潜在混杂后，5分钟延迟与7天内死亡风险增加0.10个百分点（95%CI: -0.17, 0.36），但住院率增加1.24个百分点，一年内住院费用增加616欧元。结论认为延迟未显著增加死亡风险，但可能通过增加住院和费用反映发病率上升。该研究展示了流行病学中自然实验设计进行因果推断的完整分析管道，数据集和识别策略为评估更高级因果方法（如工具变量、近端因果推断）提供了真实场景。
- **关键技术**: `natural experiment`, `busy ambulance as instrument`, `time-stratified comparison`, `multivariable adjustment`, `linked registry data`
- **为什么对您有用**: 本文是流行病学中利用自然实验（基于同一区域同时段急救车忙碌程度的外生变化）进行因果推断的典型应用，适合作为统计学家进入流行病学因果推断应用的入门读物。武器库中“identification theory in causal inference”可立即理解其识别策略，并思考用IV或近端因果推断更严格处理未测量混杂。数据集规模和链接质量提供了丰富的分析管道，值得花时间读全文以借鉴其实证分析框架。

### 10. [10.1097/ede.0000000000001903](https://doi.org/10.1097/ede.0000000000001903) — Unexpected Transmission Dynamics in a University Town: Lessons From COVID-19
- **作者**: Erin Clancey, Matthew S. Mietchen, Corrin McMichael, Eric T. Lofgren
- **期刊/来源**: Epidemiology
- **机构**: Washington State University · University of North Carolina at Chapel Hill · Whitman College
- **分类**: vol 36 · issue 6 · pp 802-810
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文研究2020年秋季华盛顿州立大学（Pullman校区）学生返校后COVID-19在大学生与社区之间的传播动态。作者构建了一个两群体常微分方程（ODE）机制模型，分别刻画学生与社区居民内部的传播率以及跨群体交叉传播率。利用Pullman市报告的发病率数据，采用贝叶斯参数估计（MCMC）拟合模型，并计算时变有效再生数（Rt）来评估暴发潜力。结果表明，在已实施的缓解措施下，学生回归并未给周围社区带来不成比例的风险；指数传播被迅速控制，Rt仅在短期略高于1。本文属于流行病学领域的实证应用，模型简单透明，数据来源清晰，适合作为统计学者了解传染病传播机制建模的入门案例。对您而言，这是一个直观的流行病学应用实例，有助于理解ODE机制模型在真实政策问题中的使用，且其数据结构和分析流程可为未来研究提供参考。
- **关键技术**: `ODE mechanistic model`, `Bayesian parameter estimation`, `MCMC`, `time-varying reproductive number`, `two-population transmission model`
- **为什么对您有用**: 本文属于您secondary interest中的流行病学应用方向，提供了一个完整的传染病传播建模案例，数据源和模型设定明确。您的very_familiar工具（非参数统计、高维渐近）虽不直接用于该模型，但可用来审视其估计量的不确定性或进行敏感性分析。从技术上，该文使用的贝叶斯MCMC和Rt计算属于基本统计计算，无需额外工具即可理解，立即可做入门阅读；若要深入拓展（如更复杂的因果问题），则需要补充传染病动力学专业知识（如SIR类模型的辨识性、时变参数估计）。

### 11. [10.1097/ede.0000000000001895](https://doi.org/10.1097/ede.0000000000001895) — Opioid Agonist Therapy Adherence Trajectories Among Commercially and Publicly Insured People Living With Hepatitis C in the United States
- **作者**: Catherine Psaras, Onyebuchi A. Arah, Kara W. Chew, Sung-Jae Lee, Marjan Javanbakht, Roch A. Nianogo et al.
- **期刊/来源**: Epidemiology
- **机构**: University of California, Los Angeles · Aarhus University
- **分类**: vol 36 · issue 6 · pp 820-829
- 相关性 4/10 · novelty: `application`
- **摘要**: 本研究利用美国 MarketScan 医保理赔数据（2015-2019），对 5,495 名合并丙肝和阿片使用障碍的患者，在启动阿片激动剂治疗（OAT）后 15 个月内的用药依从性轨迹进行刻画。采用增长混合模型（growth mixture modeling）识别出三条依从性轨迹：快速下降型（35%）、稳步下降型（39%）和持续高依从型（26%）。持续高依从组患者年龄较大、女性比例高、白人占比高、基线期接受丙肝直接抗病毒治疗的比例高，且非阿片物质使用诊断比例最低。该分析仅使用了描述性和聚类方法，未涉及因果推断或潜在结局反事实框架。作为流行病学应用论文，其数据预处理流程和轨迹建模思路可为同类纵向理赔数据的描述性分析提供参考。
- **关键技术**: `growth mixture modeling`, `latent class trajectory analysis`, `healthcare claims data analysis`, `longitudinal clustering`
- **为什么对您有用**: (1) 本文是流行病学领域典型的纵向数据应用论文，适合作为研究者了解医保理赔数据结构和轨迹分析实践的基础读物。 (2) 武器库中非参数统计和因果推断的熟悉技术无法直接用于此类参数化增长混合模型，但研究者熟悉的高维支持向量等工具在模型选择或诊断方面可能有迁移潜力。 (3) 鉴于方法学创新有限且与研究者主要兴趣（因果/半参/高维）距离较远，读全文投入产出比不高，若仅想了解流行病学数据描述性分析流程可快速浏览。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

