# Biometrics — Vol 82  Issue 2  ·  2026-06-19

- 共 7 篇 · Biometrics
- 目录核对 ⚠️ 疑似漏 45 篇（对照 OpenAlex 56 篇）：10.1093/biomtc/ujag076、10.1093/biomtc/ujag071、10.1093/biomtc/ujag057、10.1093/biomtc/ujag090、10.1093/biomtc/ujag099 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期论文主要围绕三条方法论主线展开：因果识别与可解释性、复杂缺失与截断机制下的生存分析、以及临床试验中的效率提升与动态决策。因果推断主线涵盖了元分析中的传输性、阶梯式楔形试验的异质性效应、以及高维中介分析的未观测混杂去偏；生存分析主线聚焦于顺序截断下的伪观察回归与多类型复发事件的触发结构建模；临床试验设计与检验主线则处理了协变量调整对数秩检验的方差缩减与成组序贯设计的第一类错误控制，以及贝叶斯平台试验中延迟结局的数据扩充。

因果识别与可解释性主线在本期推进了不同数据结构与混杂设定下的效应估计问题。“整合汇总数据的因果元分析”将传输性思想引入传统群体调整间接比较（MAIC），通过逆概率加权与M估计的补偿计算，解决仅具汇总数据时的目标人群标准化处理效应推断；“阶梯式楔形试验的广义DID”以2×2 DID为构建块进行加权平均，在交错采纳面板下灵活适配group-time ATT等异质性可解释estimand，明确无偏与方差-泛化权衡；“存在未观测混杂的贝叶斯结构中介分析”（BASMU）则针对高维空间数据（如脑成像），将空间潜在混杂效应纳入结果模型去偏，并给出自然直接/间接效应的渐近偏倚分析与可识别条件。

复杂缺失与临床试验效率主线分别从观测数据的截断依赖和试验设计的实操瓶颈切入。“顺序截断数据的伪观察回归”针对事件时间需依次满足多截断条件的依赖缺失机制，提出修改版伪观察以消除传统方法的偏差，并分别适配Cox与AFT模型；“多类型复发事件的触发效应模型”在Cox型比例强度框架下估计异类事件的触发参数与非线性衰减，通过partial likelihood给出渐近理论；“协变量调整对数秩检验的实际考虑”量化了基线预后协变量调整带来的方差缩减，并针对成组序贯设计中的第一类错误膨胀提出修正；“贝叶斯Phase I/II平台设计”则利用数据扩充迭代插补延迟结局，跨适应症分层借用信息以优化剂量决策。

对于关注因果推断与半参数效率的研究者，“阶梯式楔形试验的广义DID”与“整合汇总数据的因果元分析”在异质性estimand无偏估计与跨人群传输的M估计上推进显著，适合优先看；关注复杂缺失与生存分析者可重点看“顺序截断数据的伪观察回归”对依赖截断的去偏修正；聚焦高维潜在混杂与因果中介的读者则可直接切入“BASMU”框架。

## 因果推断  *(causal_inference, 5 篇)*

### 1. [10.1093/biomtc/ujag107](https://doi.org/10.1093/biomtc/ujag107) · [arXiv](https://arxiv.org/abs/2503.05634) — Integration of aggregate data in causally interpretable meta-analysis by inverse weighting
- **作者**: Tat-Thang Vo, Tran Trong Khoi Le, Sivem Afach, Stijn Vansteelandt
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在因果可解释元分析框架下，旨在通过逆概率加权整合汇总数据（aggregate data）与个体参与者数据（IPD），以估计目标人群的标准化处理效应。假设至少有一项试验提供完整IPD，其余试验仅提供汇总协变量分布，方法扩展了卫生技术评估中常用的基于矩的群体调整间接比较（MAIC），并利用M估计理论进行推断。为解决实践中汇总数据缺失导致M估计不可行的问题，作者发展了计算补偿策略（如通过参数化或模拟近似）。模拟研究验证了有限样本性能，真实数据示例比较了risankizumab与ustekinumab对银屑病的疗效。论文的技术核心在于将传输性（transportability）思想与传统随机效应元分析结合，通过逆概率加权消除效应修饰因子分布差异。该工作对您直接有用：它连接了因果推断中的标准化估计（primary interest）与M估计理论（您的moderately_familiar工具），且计算策略部分可迁移至您的统计计算兴趣。
- **关键技术**: `inverse probability weighting`, `M-estimation`, `transportability`, `population-adjusted indirect comparisons`, `moment-based methods`, `meta-analysis`
- **为什么对您有用**: 直接连接causal inference中的传输性/标准化估计方向，使用的逆概率加权和M估计理论均在您的技术范围内（very_familiar的估计理论、moderately_familiar的M估计）。该文为方法学论文，思路清晰，可立即可做的follow-up：尝试用您的higher-order U-statistics工具（treewidth/einsum）分析其加权估计量的方差结构，或检验其M估计的有限样本偏差。

### 2. [10.1093/biomtc/ujag105](https://doi.org/10.1093/biomtc/ujag105) — A generalized difference-in-differences estimator for stepped-wedge cluster-randomized trials
- **作者**: Lee Kennedy-Shaffer
- **期刊/来源**: Biometrics
- **机构**: Yale University
- **分类**: vol 82 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在阶梯式楔形随机试验（SWT）及交错采纳面板数据设定下，本文目标是处理效应异质性下的可解释因果 estimand（如 group-time ATT）的无偏估计。核心方法是将经典 2×2 DID 估计量作为基本构建块，通过加权平均构造非参数广义 DID 估计量，以灵活适配不同异质性假设下的目标 estimand。该方法无需正确设定方差模型，通过高效利用所有有效 DID 对比来缓解精度损失，在偏差-方差-泛化性权衡中提供清晰解法。理论贡献在于明确了异质性下的无偏性与可解释性条件；实证与模拟基于结核病诊断工具的 SWT 数据及 R 代码实现。对您有用之处：该加权 2×2 DID 构建块思路与 Callaway-Sant'Anna / Sun-Sarah 框架同源，可直接作为 longitudinal causal inference 中异质性 estimand 的非参数估计参考。
- **关键技术**: `stepped-wedge cluster-randomized trial`, `staggered treatment adoption`, `2-by-2 DID building blocks`, `weighted average estimator`, `treatment effect heterogeneity`, `group-time ATT`
- **为什么对您有用**: 本文直接连接 longitudinal causal inference 中交错采纳设定下的异质性 estimand 识别与估计问题。您 technical_arsenal 中的 'identification theory in causal inference' 可直接攻破其加权构建块的 estimand 分解逻辑，判断其无偏性条件是否可进一步放松或推广至连续处理/IV 设定。**立即可做**：用 very_familiar 的因果识别理论审视其 estimand 定义，并基于 R 代码复现模拟验证其精度与现有 HOIF / semipara 方法的对比。

### 3. [10.1093/biomtc/ujag110](https://doi.org/10.1093/biomtc/ujag110) · [arXiv](https://arxiv.org/abs/2407.04142) — Bayesian Structured Mediation analysis with Unobserved confounders
- **作者**: Yuliang Xu, Shu Yang, Jian Kang
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究在高维中介分析中（如脑成像数据），当存在未观测混杂变量时，如何对具有空间平滑结构的中介变量进行因果效应估计。目标是在空间潜在混杂效应（subject-specific spatial confounding effects）的框架下识别自然间接效应（NIE）和自然直接效应（NDE）。作者提出BASMU（BAyesian Structured Mediation analysis with Unobserved confounders）框架，通过将空间潜在效应纳入结果模型以去偏，并建立模型可识别条件。理论部分分析了忽略未观测混杂时NIE和NDE的渐近偏倚，证明引入空间效应可以降低偏倚。方法上采用两阶段估计算法，第一阶段从中介变量提取空间潜在混杂，第二阶段用这些估计校正结果模型。仿真表明BASMU在各种场景下大幅降低偏倚，并应用于ADHD脑功能成像数据，相比已有方法识别出更多具有显著中介效应的体素（NIE增加41%，NDE减少26%）。本文直接连接到您对因果中介分析及未观测混杂敏感性的兴趣，且高维中介变量设定与您熟悉的高维渐近理论相互呼应。
- **关键技术**: `Bayesian mediation analysis`, `spatial confounding effects`, `two-stage estimation`, `identifiability conditions`, `high-dimensional mediators`, `natural indirect effect`
- **为什么对您有用**: 本文直接针对您因果推断兴趣中的中介分析与未观测混杂敏感性（primary interest），并涉及高维中介变量的空间结构。您 moderately_familiar 中的"identification theory in causal inference"可用来推敲本文的识别条件是否在更弱假设下仍成立，而 very_familiar 中的"high-dimensional asymptotics"可立即用于检查其渐近偏倚结论的严格性与最优性。综合判断：本文的核心贡献（可识别性+两阶段去偏）属于您熟悉的方法学框架，立即可用已有工具进行复现验证或扩展。

### 4. [10.1093/biomtc/ujag084](https://doi.org/10.1093/biomtc/ujag084) — Pseudo-observation regression for sequentially truncated data
- **作者**: Jing Qian, Erik T Parner, Morten Overgaard, Rebecca A Betensky
- **期刊/来源**: Biometrics
- **机构**: University of Massachusetts Amherst · Aarhus University · New York University
- **分类**: vol 82 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对观察性队列研究中的顺序截断数据（sequential truncation），即事件时间需在多个截断时间依次满足条件才被观测，提出了基于伪观察（pseudo-observation）的回归建模方法。传统伪观察方法在处理截断依赖协变量时可能失效，因此作者引入一种修改版伪观察（modified pseudo-observation），通过调整个体对无偏估计的贡献，消除依赖偏差。方法分别应用于Cox比例风险模型和加速失效时间（AFT）模型，通过模拟研究评估了有限样本表现。应用到阿尔茨海默病队列研究数据，展示了顺序截断情景下的实际适用性。对您而言，该工作衔接了生存分析中复杂缺失机制与因果推断常用的伪观察技术，且数据来源为流行病学队列，与您的次要兴趣（流行病学数据集）直接相关。
- **关键技术**: `pseudo-observation`, `jackknife`, `modified pseudo-observation`, `Cox proportional hazards model`, `accelerated failure time (AFT) model`, `sequential truncation`
- **为什么对您有用**: 论文处理的顺序截断问题常见于流行病学队列，与您的次要兴趣（流行病学数据集及应用因果工作）高度吻合。伪观察方法是因果推断中处理删失和竞争风险的常用工具（属于您的very_familiar中的'causal inference estimation theory'），您可直接理解其简单版和修改版机制，并评估该方法在您熟悉的因果框架下的可推广性。鉴于您对伪观察技术的已有掌握，阅读本文属**立即可做**的入门级应用工作。

### 5. [10.1093/biomtc/ujag109](https://doi.org/10.1093/biomtc/ujag109) — Practical considerations when using the covariate-adjusted log-rank test for the analysis of time-to-event endpoints in oncology trials
- **作者**: Daniel Backenroth, Sanne Roels, Shiva Dibaj, Ting Ye, Fredrik Öhrn, Kelly Van Lancker
- **期刊/来源**: Biometrics
- **机构**: Johnson & Johnson (United States) · Johnson Engineering (United States) · Johnson & Johnson (Brazil) · University of Washington · Johnson & Johnson (Sweden) · HOGENT University of Applied Sciences and Arts · Vrije Universiteit Brussel · Ghent University
- **分类**: vol 82 · issue 2
- 相关性 6/10 · novelty: `application`
- **摘要**: 本论文聚焦于随机对照肿瘤试验中，针对时间至事件终点（如总生存期）使用协变量调整对数秩检验的实际考虑。首先介绍如何基于历史数据估计不同协变量调整策略（包括调整预后评分）所能实现的方差缩减，并比较这些策略对第一类错误率控制的影响。核心方法是协变量调整对数秩检验，它通过纳入基线预后协变量来减少结局变异性，从而提升统计检验功效。论文还针对在成组序贯设计中嵌入协变量调整可能引发的第一类错误率膨胀问题，提出了一种修正方法。通过模拟研究评估了不同预后协变量强度、事件数、分层因素和中期分析场景下的表现。最后，重新分析了一项转移性结直肠癌试验的总生存期数据，展示了成组序贯设计中协变量调整的实际应用。本文虽未发展新的理论方法，但对半参数效率理论中通过协变量调整实现方差缩减的原理提供了具体数值验证，对您在因果推断中处理生存数据的研究有直接参考价值。
- **关键技术**: `Covariate-adjusted log-rank test`, `Prognostic score`, `Group sequential design`, `Variance reduction estimation`, `Type I error rate inflation correction`, `Simulation-based power analysis`
- **为什么对您有用**: 与您在效率理论（半参数效率界）中的兴趣直接相关：协变量调整对数秩检验正是通过估计协变量对结局方差的影响来逼近半参数效率界，您的 estimation theory (causal inference) 武器库可用来严格验证论文中方差缩减估计量的渐近性质。本论文可快速阅读案例部分，理解生存数据协变量调整的实践操作，属立即能做（立即可做）的范畴。

## 流行病学  *(epidemiology, 1 篇)*

### 1. [10.1093/biomtc/ujag094](https://doi.org/10.1093/biomtc/ujag094) — Competing-triggering effect models for multitype recurrent event data
- **作者**: Tianhao Song, Jason Fine, Payal Khincha, Anastasia Ivanova, Paul Albert
- **期刊/来源**: Biometrics
- **机构**: University of North Carolina at Chapel Hill · University of Pittsburgh · National Cancer Institute
- **分类**: vol 82 · issue 2
- 相关性 5/10 · novelty: `minor`
- **摘要**: 本文研究多类型复发事件数据中不同事件类型间的触发效应，目标是在 Cox 型比例强度框架下估计各类事件对后续同类及异类事件的触发参数。作者提出广义 Cox 型结构，允许不同事件类型共享部分触发参数，同时保留非线性衰减函数刻画触发效应随时间的衰减。核心估计方法为 partial likelihood estimator，在标准 regularity 条件下证明了其一致性、渐近正态性，并给出了 plug-in 方差估计。模拟实验验证了有限样本表现，实证分析应用于 Li-Fraumeni 综合征队列中乳腺癌与非乳腺癌间的触发效应。对您而言，这是流行病学队列中复发事件因果/触发结构的典型应用案例，但方法学 novelty 有限。
- **关键技术**: `multitype recurrent events`, `Cox proportional intensity model`, `partial likelihood estimation`, `triggering effect modeling`, `asymptotic normality`
- **为什么对您有用**: 本文属于流行病学队列数据的复发事件建模应用，连接到 epidemiology secondary interest 的 applied causal work 子方向。方法学上仅是经典 partial likelihood 在多类型事件上的推广，novelty_flag 为 minor；您的 technical_arsenal 中 M-estimation theory 与 semiparametric theory 足以完全理解其渐近理论，但本文未触及 semiparametric efficiency bound 或 higher-order 修正，对您的研究无直接推进。作为 gateway reading：它展示了流行病学中复发事件数据的结构（多类型、触发、衰减），但数据/模型 exposition 较常规，不值得花时间读全文。

## 其他  *(other, 1 篇)*

### 1. [10.1093/biomtc/ujag096](https://doi.org/10.1093/biomtc/ujag096) — A Bayesian phase I/II platform design with data augmentation accounting for delayed outcomes
- **作者**: Wentao Yang, Rongji Mu, Zhangsheng Yu
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对贝叶斯 phase I/II 平台试验中剂量优化面临的延迟结局（如迟发性毒性和疗效）问题，提出了一种结合数据扩充的增强设计 BPDD。该方法通过迭代数据扩充过程预测未观测到的结局，将观测数据和插补数据合并以更新剂量-毒性和剂量-疗效的估计，从而支持最优剂量决策并缩短临床试验时间。利用分层建模跨适应症借用信息，提高参数估计的准确性，并促进有效的风险-收益权衡分析。每次中期分析时，根据更新后的估计指导剂量递增、递减和最优生物剂量识别。模拟研究表明该方法在处理延迟结局时具有稳健性和灵活性，在剂量优化的准确性和时间效率方面表现良好。该框架有望提高多适应症平台试验的效率和加速药物开发。作为流行病学次级兴趣中的临床试验统计方法，本文展现了贝叶斯数据扩充在优化决策中的实用价值。
- **关键技术**: `Bayesian data augmentation`, `iterative imputation`, `hierarchical modeling`, `dose optimization`, `delayed outcome prediction`, `platform trial design`
- **为什么对您有用**: 本文属于流行病学次级兴趣中的临床试验统计方法，与因果推断中介分析中的纵向数据缺失处理有方法学共鸣。武器库中 'software development' 能力可用于复现其模拟框架或扩展至真实数据应用。暂不可做：核心贝叶斯分层模型建模和马尔可夫链蒙特卡洛实现目前不在武器库内，需先补足贝叶斯计算基础。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

