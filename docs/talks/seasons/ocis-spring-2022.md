# OCIS · Spring 2022

- 共 12 场 · 10 篇精读

## 本季导览

> 自动生成：归纳本季主线与值得先看的几场，**不打分、不排名**。

这一季的12场报告大致可以归纳为四条主线：**因果发现与不确定性量化**（Samuel Wang, Mona Azadkia, Mathias Drton）、**数据融合与异质性处理效应**（AmirEmad Ghassami, Shu Yang, Neil Davies）、**实验设计与网络干扰**（Shuangning Li & Michael Oberst, Tim Morrison & Harrison Li）、以及**因果推断的方法论反思与应用**（Geneviève Lefebvre, Bin Yu, Mireille Schnitzer, Tyler VanderWeele）。其中，数据融合和实验设计两条主线尤为突出，且内部存在方法上的呼应。

在**数据融合**主线上，AmirEmad Ghassami 和 Shu Yang 分别从不同角度处理“实验数据+观察数据”的整合。Ghassami 聚焦于长期效应识别，利用短期实验数据与存在未观测混杂的观察数据，通过代理推断或定制工具变量来桥接短期与长期结果。Shu Yang 则关注异质性处理效应（HTE）的稳健估计，提出一种基于检验的弹性整合方法，在利用真实世界数据提升效率的同时，通过假设检验来防范偏倚。Neil Davies 的工作虽不直接涉及数据融合，但同样处理效应异质性——他讨论在工具变量框架下，如何用“无同时异质性”假设替代单调性，从而将 Wald 估计量解释为平均因果效应（ATE）而非局部平均处理效应（LATE），这与 Shu Yang 对 HTE 的精细刻画形成互补。

在**实验设计与网络干扰**主线上，Shuangning Li & Michael Oberst 和 Tim Morrison & Harrison Li 分别推进了非标准实验设计下的因果推断。前者在网络干扰场景下，利用随机图渐近理论（而非固定图）来推导处理效应估计量的渐近性质，这允许图随样本量变密，从而突破传统固定图设定下收敛速率退化的瓶颈。后者则讨论“决胜局设计”（Tie-breaker Design），这是一种介于断点回归与随机对照试验之间的设计，通过将极端值确定分配、中间值随机分配来平衡治疗受益与统计效率，并探讨了多变量情形下的最优性。两场报告都涉及“在非标准分配机制下如何获得有效推断”，但前者处理的是干扰结构，后者处理的是分配规则。

如果想快速了解这一季的核心进展，建议从**数据融合**和**实验设计**两条主线切入。打底场次可看 AmirEmad Ghassami（长期效应识别的基本框架）和 Shuangning Li & Michael Oberst（网络干扰的随机图视角）；进阶场次可看 Shu Yang（HTE 的检验-弹性整合）和 Tim Morrison & Harrison Li（多变量决胜局设计的最优性）。对因果发现不确定性感兴趣的读者，可先看 Samuel Wang（频域置信集）再读 Mathias Drton（潜变量模型的半游程准则）。

## 报告列表

### [- Uncertainty Quantification for Causal Discovery](../2022-06-28-ocis-2022-06-28-samuel-wang.md)
**讲者**: Samuel Wang · **讨论人**: Daniel Malinsky · 2022-06-28  
链接：[视频](https://youtu.be/YxgG35kDbR4) · [幻灯片](https://drive.google.com/file/d/1-m7PpD92S7JTI3T_HnR01ppKvzI32NEP/view?usp=sharing)
<details><summary>摘要</summary>

Causal discovery procedures are popular methods for discovering causal structure across the physical, biological, and social sciences. However, most procedures for causal discovery only output a single estimated causal model or single equivalence class of models. In this work, we propose a procedure for quantifying uncertainty in causal discovery. Specifically, we consider structural equation models where a unique graph can be identified and propose a procedure which returns a confidence sets of…

</details>

### Université du Québec à Montréal ) - Bayesian joint modeling for causal mediation analysis with a binary outcome and a binary mediator　*（暂无精读）*
**讲者**: Geneviève Lefebvre ( · **讨论人**: Olli Saarela · 2022-06-21  
链接：[幻灯片](https://drive.google.com/file/d/1UOikv-UAoppiCcnDilYLuMbuTwYy3ubn/view?usp=sharing)
<details><summary>摘要</summary>

Mediation analysis with a binary outcome is notoriously more challenging than with a continuous outcome. In this talk, I will present a new approach, named t-link , to perform causal mediation with a binary outcome and a binary mediator. This approach relies on the Bayesian multivariate logistic regression model introduced by O'Brien and Dunson (Biometrics, 2004, 739-746, 60(3)) and its Student-t approximation. By re-expressing the mediation formula, I show how to use this multivariate latent mo…

</details>

### [Johns Hopkins University ) - Combining Experimental and Observational Data for Identification and Estimation of Long-Term Causal Effects](../2022-06-14-ocis-2022-06-14-amiremad-ghassami.md)
**讲者**: AmirEmad Ghassami ( · **讨论人**: Guido Imbens · 2022-06-14  
链接：[视频](https://youtu.be/uVfEo9UuC20) · [幻灯片](https://drive.google.com/file/d/1NW1ggfyFz7qhiIhod0AUwuDtKgyyD2Mg/view?usp=sharing) · [arXiv](https://arxiv.org/pdf/2201.10743.pdf)
<details><summary>摘要</summary>

We consider the task of identifying and estimating the causal effect of a treatment variable on a long-term outcome variable using data from an observational domain and an experimental domain. The observational domain is subject to unobserved confounding. Furthermore, subjects in the experiment are only followed for a short period of time; hence, long-term effects of treatment are unobserved but short-term effects will be observed. Therefore, data from neither domain alone suffices for causal in…

</details>

### [- A Fast Non-parametric Approach for Causal Structure Learning in Polytrees](../2022-06-07-ocis-2022-06-07-mona-azadkia.md)
**讲者**: Mona Azadkia · **讨论人**: Bryon Aragam · 2022-06-07  
链接：[视频](https://youtu.be/ikHRbNLjYdc) · [幻灯片](https://drive.google.com/file/d/1e9tgRtVsG-nNTwChsxvUF_E_l6IkVkui/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2111.14969)
<details><summary>摘要</summary>

We study the problem of causal structure learning with no assumptions on the functional relationships and noise. We develop DAG-FOCI, a computationally fast algorithm for this setting that is based on the FOCI variable selection algorithm in (Azadkia 2021). DAG-FOCI requires no tuning parameter and outputs the parents and the Markov boundary of a response variable of interest. We provide high-dimensional guarantees of our procedure when the underlying graph is a polytree. Furthermore, we demonst…

</details>

### [- Predictability, stability, and causality with a case study to find genetic drivers of a heart disease](../2022-05-31-ocis-2022-05-31-bin-yu.md)
**讲者**: Bin Yu · **讨论人**: Jas Sekhon - · 2022-05-31  
链接：[视频](https://youtu.be/4e2EFrOUGfE) · [幻灯片](https://drive.google.com/file/d/13DGK_eu2txQQhtOcszm41M3MwJauxFBR/view?usp=sharing)
<details><summary>摘要</summary>

"A.I. is like nuclear energy -- both promising and dangerous" -- Bill Gates, 2019. Data Science is a pillar of A.I. and has driven most of recent cutting-edge discoveries in biomedical research and beyond. Human judgement calls are ubiquitous at every step of a data science life cycle, e.g., in choosing data cleaning methods, predictive algorithms and data perturbations. Such judgment calls are often responsible for the "dangers" of A.I. To maximally mitigate these dangers, we developed a framew…

</details>

### [University of Montreal ) - Estimands and estimation of COVID-19 vaccine effectiveness under the test-negative design: connections to causal inference](../2022-05-17-ocis-2022-05-17-mireille-schnitzer.md)
**讲者**: Mireille Schnitzer ( · **讨论人**: David Benkeser · 2022-05-17  
链接：[视频](https://youtu.be/NN3V2ggZXjk) · [幻灯片](https://drive.google.com/file/d/1_3ZbBLOjzF9uXdiuc8d1z6WK45g_Qc23/view?usp=sharing)
<details><summary>摘要</summary>

The test-negative design (TND) is routinely used for the monitoring of seasonal flu vaccine effectiveness. More recently, it has become integral to the estimation of COVID-19 vaccine effectiveness, in particular for more severe disease outcomes. Distinct from the case-control study, the design typically involves recruitment of participants with a common symptom presentation who are being tested for the infectious disease in question. Participants who test positive for the target infection are th…

</details>

### - Talk 1 : Optimality in multivariate tie-breaker designs　*（暂无精读）*
**讲者**: Tim Morrison ; Harrison Li · 2022-05-10  
链接：[视频](https://youtu.be/JcyOiBUt8HM) · [幻灯片](https://drive.google.com/file/d/1e6hbZvnjX7cYUeFHOPIPCMkBHIRZ9TI6/view?usp=sharing)
<details><summary>摘要</summary>

Tie-breaker designs (TBDs), in which subjects with extreme values are assigned treatment deterministically and those in the middle are randomized, are intermediate between regression discontinuity designs (RDDs) and randomized controlled trials (RCTs). TBDs thus provide a convenient mechanism by which to trade off between the treatment benefit of an RDD and the statistical efficiency gains of an RCT. We study a model where the expected response is one multivariate regression for treated subjects…

</details>

### [Causal Inference and Measure Construction: Towards a New Model of Measurement](../2022-05-03-ocis-2022-05-03-tyler-vanderweele.md)
**讲者**: Tyler VanderWeele · **讨论人**: Fredrik Sävje - Abstract. Psychosocial constructs can only be assessed indirectly, and measures are typically formed by a combination of indicators that are thought to relate to the construct. Reflective and formative measurement models offer different conceptualizations of the relation between the indicators and what is sometimes conceived of as a univariate latent variable supposedly corresponding to the construct. I argue that the empirical implications of these models will often be violated by data since the causally relevant constituents will generally be multivariate, not univariate. In fact, the assumption of an underlying univariate structural latent variable is so strong that it has empirically testable implications, even though the latent is unobserved. Formal statistical tests can be developed to reject this assumption, but factor analysis, as typically practiced, is not adequate to do so. Factor analysis also suffers from the inability to distinguish associations arising from causal versus conceptual relations. I put forward an outline for a new model of the process of measure construction and propose a causal interpretation of associations between constructed measures and subsequent outcomes that is applicable even if the usual assumptions of reflective and formative models fail. I discuss the practical implications of these observations and proposals for the provision of definitions, the selection of items, item-by-item analyses, the construction of measures, and the causal interpretation of regression analyses. · 2022-05-03  
链接：[视频](https://youtu.be/UA2WvYlT2RE) · [幻灯片](https://drive.google.com/file/d/1PifbZBL3MI9v9bnHsFfOk9UTQ1L-baWg/view?usp=sharing)

### [- Test-based integrative analysis for heterogeneous treatment effects combining randomized trial and real-world data](../2022-04-26-ocis-2022-04-26-shu-yang.md)
**讲者**: Shu Yang · **讨论人**: Issa Dahabreh · 2022-04-26  
链接：[视频](https://youtu.be/APIQujnvXNI) · [幻灯片](https://drive.google.com/file/d/1nVjTVYROGIjLW5eHHPJZJbDy7G_BQj68/view?usp=sharing) · [arXiv](http://arxiv.org/abs/2005.10579)
<details><summary>摘要</summary>

Parallel randomized trial (RT) and real-world (RW) data are becoming increasingly available for treatment evaluation. Given the complementary features of the RT and RW data, we propose a test-based elastic integrative analysis of RT and RW data for accurate and robust estimation of the heterogeneity of treatment effect (HTE), which lies at the heart of precision medicine. When the RW data are not subject to bias, e.g., due to hidden confounding, our approach combines the RT and RW data for optim…

</details>

### [- Average causal effect estimation via instrumental variables: the no simultaneous heterogeneity assumption](../2022-04-12-ocis-2022-04-12-neil-davies.md)
**讲者**: Neil Davies · **讨论人**: Eric Tchetgen Techetgen · 2022-04-12  
链接：[视频](https://youtu.be/CDEC8--Xnsw) · [幻灯片](https://drive.google.com/file/d/1f5wLwDuCCtKIyAV1cia2On8CR1txZDoY/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2010.10017)
<details><summary>摘要</summary>

Instrumental variables (IVs) can be used to provide evidence as to whether a treatment X has a causal effect on Y. Z is a valid instrument if it satisfies the three core IV assumptions of relevance, independence and the exclusion restriction. Even if the instrument satisfies these assumptions, further assumptions are required to estimate the average causal effect (ACE) of X on Y. Sufficient assumptions for this include: homogeneity in the causal effect of X on Y; homogeneity in the association o…

</details>

### [Talk #1: Random Graph Asymptotics for Treatment Effect Estimation under Network Interference](../2022-03-29-ocis-2022-03-29-shuangning-li-michael-oberst.md)
**讲者**: Shuangning Li ; Michael Oberst · 2022-03-29  
链接：[视频](https://youtu.be/Sz4Q7xGdTpU) · [幻灯片](https://drive.google.com/file/d/1zAMOW6iuAbtqocT6DGBiU-XDlDnwEY48/view?usp=sharing)

### [Technical University of Munich) - Half-Trek Criterion for Identifiability of Latent Variable Models](../2022-03-22-ocis-2022-03-22-mathias-drton.md)
**讲者**: Mathias Drton ( · **讨论人**: Robin Evans · 2022-03-22  
链接：[视频](https://youtu.be/XAoKhwMdFqI) · [幻灯片](https://drive.google.com/file/d/1wLk0zFWwZGwYVHWF4R3DRRatTAZDf0J3/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2201.04457)
<details><summary>摘要</summary>

We consider linear structural equation models with latent variables and develop a criterion to certify whether the direct causal effects between the observable variables are identifiable based on the observed covariance matrix. Linear structural equation models assume that both observed and latent variables solve a linear equation system featuring stochastic noise terms. Each model corresponds to a directed graph whose edges represent the direct effects that appear as coefficients in the equatio…

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

