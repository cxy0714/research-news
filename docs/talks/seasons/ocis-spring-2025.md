# OCIS · Spring 2025

- 共 11 场 · 9 篇精读

## 本季导览

> 自动生成：归纳本季主线与值得先看的几场，**不打分、不排名**。

OCIS Spring 2025 的 11 场报告可归纳为四条主线：**多维与复杂设计下的因果推断**（Cattaneo、Keele、Small）、**高维与部分识别下的稳健推断**（Kennedy、Zhou、Pimentel）、**因果与机器学习的交叉**（Locatello、Guo、Kallus），以及**形状约束与图模型**（Young researchers' seminar）。此外，Josse 的元分析替代方案和 Small 的跨团队交叉筛查分别从聚合证据和单一研究内复制两个角度补充了方法工具箱。

**多维与复杂设计**是这一季最密集的线索。Cattaneo 系统处理了**边界断点设计**（多维 RD）中沿一维边界的估计与推断，包括 BATEC 和 LBATE 等参数，并指出距离法在边界不光滑时的缺陷。Keele 则聚焦**簇级治疗分配**（COS），强调其与个体级分配的本质区别，并梳理了从识别到敏感性分析的完整工具链。Small 的“双团队交叉筛查”在单一观测研究中同时实现探索、确认与复制，利用证据因子和自然子群体（如天主教 vs. 非天主教妇女）替代样本分裂，是**研究设计层面**的创新。

**高维与部分识别**是另一条突出主线。Kennedy 处理**治疗水平数接近或超过样本量**的高维治疗场景，讨论估计的极限与不可避免的正性违反。Zhou 将**边际敏感性模型（MSM）** 扩展到离线强化学习，在时序外生未观测混杂下对 Q 函数和价值函数做部分识别，并优化最坏情况策略。Pimentel 则将**design sensitivity** 从匹配框架推广到加权观测研究，允许在设计阶段优化对未测量混杂的稳健性。这三场共享“在不可识别时给出有意义的界”这一核心思路，但分别面向高维治疗、动态决策和加权估计。

**因果与机器学习的交叉**以 Locatello 和 Guo 为代表。Locatello 覆盖因果发现、表示学习和推断三个支柱，强调 ML 如何赋能因果分析。Guo 用**minimax 优化**统一多源学习中的分布鲁棒优化（DRO）和因果不变性，目标是从多个源域学到对目标域稳健的预测模型。Kallus 则从**历史 A/B 实验**中学习代理指标（surrogate index），将 ill-posed inverse problem（NPIV）与对抗性 ML 结合，对长期效应的线性泛函做去偏推断。这三场都涉及“从数据中学习因果结构或稳健预测器”，但工具各异：Locatello 侧重图与表示，Guo 侧重优化与不变性，Kallus 侧重逆问题与去偏。

**形状约束与图模型**由 Young researchers' seminar 单独代表，该工作将单调性假设系统化地注入图因果模型的非参数识别算法，证明图模型也能容纳 PO 框架中经典的 LATE 型识别，并给出完整的算法化处理。

若想快速切入，建议按以下路径：**多维设计入门**：先看 Cattaneo（边界断点设计的基础概念与推断），再读 Keele（簇级设计的完整框架）；**部分识别与稳健性**：从 Pimentel（design sensitivity 的基本思想）开始，再读 Zhou（MSM 在动态决策中的扩展）；**因果与 ML 交叉**：先看 Kallus（代理指标与 NPIV 的直观问题），再读 Guo（DRO 与不变性的统一视角）；**形状约束**：直接看 Young researchers' seminar（图模型+单调性的算法化）。Josse 和 Small 分别适合对元分析替代方案或单一研究内复制设计感兴趣的读者。

## 报告列表

### Causal Alternatives to Meta-Analysis　*（暂无精读）*
**讲者**: Julie Josse · **讨论人**: Larry Han · 2025-06-17  
链接：[视频](https://youtu.be/C9VMl3xgE98) · [幻灯片](https://drive.google.com/file/d/1136x5pwhzf0CKHJinlUCNOFlwQqvle6X/view?usp=sharing) · [arXiv](https://arxiv.org/pdf/2505.20168)
<details><summary>摘要</summary>

Meta-analysis, by aggregating effect estimates from multiple studies conducted in diverse settings, stands at the top of the evidence-based medicine hierarchy. However, conventional approaches face key limitations: they often lack a clear causal interpretation, and practical constraints, such as data silos and regulatory barriers, frequently prevent access to individual-level data, limiting the feasibility of individual patient data meta-analyses. In this talk, we introduce three causal alternat…

</details>

### [Estimation and Inference in Boundary Discontinuity Designs](../2025-06-10-ocis-2025-06-10-matias-cattaneo.md)
**讲者**: Matias Cattaneo · 2025-06-10  
链接：[视频](https://youtu.be/QkAdvFdkImc) · [幻灯片](https://drive.google.com/file/d/1moSCQz6W62K18XgJQmn9U9BDlV7QSGHo/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2505.05670)
<details><summary>摘要</summary>

Boundary Discontinuity Designs are used to learn about treatment effects along a continuous boundary that splits units into control and treatment groups according to a bivariate score variable. These research designs are also called Multi-Score Regression Discontinuity Designs, a leading special case being Geographic Regression Discontinuity Designs. We study the statistical properties of commonly used local polynomial treatment effects estimators along the continuous treatment assignment bounda…

</details>

### Causal inference with high-dimensional treatments　*（暂无精读）*
**讲者**: Edward Kennedy, - · **讨论人**: Iván Díaz · 2025-06-03  
链接：[arXiv](https://arxiv.org/pdf/2602.21423)
<details><summary>摘要</summary>

In this work we consider causal inference when the number of treatment levels is comparable to or larger than the number of observations. This setting brings two unique challenges: first, the treatment effects of interest are a high-dimensional vector rather than a low-dimensional scalar and, second, positivity violations are unavoidable. We first discuss fundamental limits of estimating effects in such settings, showing consistent estimation is impossible without further assumptions. We go on t…

</details>

### [Powering causality with ML: Discovery, Representations, and Inference](../2025-05-27-ocis-2025-05-27-francesco-locatello.md)
**讲者**: Francesco Locatello · **讨论人**: Jason Hartford · 2025-05-27  
链接：[视频](https://youtu.be/YGo9rTI2bZE) · [幻灯片](https://drive.google.com/file/d/10NZf3U4jWhCzkKFFha5DtoK_jPzKWmBV/view?usp=share_link)
<details><summary>摘要</summary>

Machine learning and AI have the potential to transform data-driven scientific discovery, enabling not only accurate predictions for several scientific phenomena but also accelerating causal understanding. In this talk, I will show how machine learning has the potential to power causal analysis across 3 pillars: discovery, representations, and inference. I will discuss first how causal structure can be discovered using score matching approaches. Next, I will turn to a new interpretation of causa…

</details>

### [Clustered Observational Studies: A Review of Concepts and Methods](../2025-05-20-ocis-2025-05-20-luke-keele.md)
**讲者**: Luke Keele · **讨论人**: Eli Ben-Michael · 2025-05-20  
链接：[视频](https://youtu.be/sOuxZtYJKlQ) · [幻灯片](https://drive.google.com/file/d/1z4SHdGPLaalteaGNyohQzHWZ6iZm0LzH/view?usp=share_link)
<details><summary>摘要</summary>

The clustered observational study (COS) design is the observational counterpart to the clustered randomized trial. In a COS, a treatment is assigned to intact groups, and all units within the group are exposed to the treatment. However, the treatment is non-randomly assigned. COSs are common in both education and health services research. In education, treatments may be given to all students within some schools but withheld from all students in other schools. In health studies, treatments may be…

</details>

### [Design Sensitivity and Its Implications for Weighted Observational Studies](../2025-05-13-ocis-2025-05-13-sam-pimentel.md)
**讲者**: Sam Pimentel · **讨论人**: Jacob Dorn · 2025-05-13  
链接：[视频](https://youtu.be/O2Yt9N5FVbY) · [幻灯片](https://drive.google.com/file/d/167kX0QzysTqqL2b6eHpujAR95QA_zQiU/view?usp=drive_link) · [arXiv](https://arxiv.org/abs/2307.00093)
<details><summary>摘要</summary>

Sensitivity to unmeasured confounding is not typically a primary consideration in designing weighted treated-control comparisons in observational studies. We introduce a framework allowing researchers to optimize robustness to omitted variable bias at the design stage using a measure called design sensitivity. Design sensitivity, which describes the asymptotic power of a sensitivity analysis, allows transparent assessment of the impact of different weighted estimation strategies on sensitivity. …

</details>

### [Multi-Source Learning with Minimax Optimization: From Adversarial Robustness to Causal Invariance](../2025-05-06-ocis-2025-05-06-zijian-guo.md)
**讲者**: Zijian Guo · **讨论人**: Kaizheng Wang · 2025-05-06  
链接：[视频](https://youtu.be/1X9691nTTc8) · [幻灯片](https://drive.google.com/file/d/19YqS1DBxrWx_7VJIMAJeMFZ3QmlgcQzW/view?usp=sharing)
<details><summary>摘要</summary>

Empirical risk minimization often fails to deliver reliable predictions when the target distribution deviates from source populations. This talk explores leveraging multi-source data to build models that generalize and transfer effectively to target domains. We propose a distributionally robust optimization framework that maximizes worst-case performance over a set of potential target distributions. We first introduce the definition of a distributionally robust prediction model and show that it …

</details>

### [Robust Fitted-Q-Evaluation and Iteration under Sequentially Exogenous Unobserved Confounders](../2025-04-29-ocis-2025-04-29-angela-zhou.md)
**讲者**: Angela Zhou · **讨论人**: Qingyuan Zhao · 2025-04-29  
链接：[视频](https://youtu.be/isWP1pdCI_U) · [幻灯片](https://drive.google.com/file/d/1HRaboxuAzXl0oBf8W0NvCRL-itIAo4YP/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2302.00662)
<details><summary>摘要</summary>

Offline reinforcement learning is important in domains such as medicine, economics, and e-commerce where online experimentation is costly, dangerous or unethical, and where the true model is unknown. However, most methods assume all covariates used in the behavior policy’s action decisions are observed. Though this assumption, sequential ignorability/unconfoundedness, likely does not hold in observational data, most of the data that accounts for selection into treat- ment may be observed, motiva…

</details>

### [Monotonicity in graphical causal models: an algorithmic approach](../2025-04-22-ocis-2025-04-22-young-researchers-seminar.md)
**讲者**: Young researchers' seminar · 2025-04-22  
链接：[视频](https://youtu.be/Ik4MTjhHaVM) · [幻灯片](https://drive.google.com/file/d/1qOKm4awkpPxy3vKTwOfK193Lpp720ZVY/view)
<details><summary>摘要</summary>

A longstanding debate between the proponents of the potential outcomes (PO) and the graphical models (GM) approach to causal inference concerns the identification of causal effects under shape constraints (such as monotonicity). Scholars in the PO framework have developed seminal results leveraging monotonicity constraints in practical applications, such as in identification of local average treatment effects (LATE). Various assertions have been made in the PO literature that the graphical appro…

</details>

### [Learning Surrogate Indices from Historical A/Bs: Adversarial ML for Debiased Inference on Functionals of Ill-Posed Inverses](../2025-04-08-ocis-2025-04-08-nathan-kallus.md)
**讲者**: Nathan Kallus · **讨论人**: Rahul Singh · 2025-04-08  
链接：[视频](https://youtu.be/Os1jikCZTvg) · [幻灯片](https://drive.google.com/file/d/100Y7I-RGkeBpwcjRFgFjSghLnShnBrn3/view?usp=share_link)
<details><summary>摘要</summary>

Experimentation on digital platforms often faces a dilemma: we want rapid innovation but we also want to make decisions based on long-term impact. Usually one resorts to looking at indices (i.e., scalar-valued functions) that combine multiple short-term surrogate outcomes. Constructing indices by regressing long-term metrics on short-term ones is easy with off-the-self ML but suffers bias from confounding and direct (i.e., unmediated) effects. I will discuss how to instead leverage past experime…

</details>

### [Exploration, Confirmation, and Replication in the Same Observational Study: A Two Team Cross-Screening Approach to Studying the Effect of Unwanted Pregnancy on Mothers’ Later Life Outcomes](../2025-04-01-ocis-2025-04-01-dylan-small.md)
**讲者**: Dylan Small · **讨论人**: Ying Jin · 2025-04-01  
链接：[视频](https://youtu.be/xW-pKDS8VlU) · [幻灯片](https://csap.yale.edu/sites/default/files/files/ds-qrmw-1-30-25.pdf)
<details><summary>摘要</summary>

The long term consequences of unwanted pregnancies carried to term on mothers have not been much explored. We use data from the Wisconsin Longitudinal Study (WLS) and propose a novel approach, namely two team cross-screening, to study the possible effects of unwanted pregnancies carried to term on various aspects of mothers’ later-life mental health, physical health, economic well-being and life satisfaction. Our method, unlike existing approaches to observational studies, enables the investigat…

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

