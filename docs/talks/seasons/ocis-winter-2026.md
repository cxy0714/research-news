# OCIS · Winter 2026

- 共 9 场 · 9 篇精读

## 本季导览

> 自动生成：归纳本季主线与值得先看的几场，**不打分、不排名**。

OCIS Winter 2026 的九场报告可归纳为三条主线：**半参数效率与调参**（Mukherjee、Young Researchers' Seminar on DAGs）、**因果识别与偏识别**（Sadeghi、Song、Young Researchers' Seminar on DAGs）、**政策相关性与网络干扰**（Young Researchers' Seminar on Policy Learning、Eckles）。此外，**处理后变量条件化效应**（Stensrud）、**AI 辅助需求分析**（Chernozhukov）和**敏感性分析**（Rosenbaum）各成独立支线。

最突出的主线是**半参数效率与调参**。Mukherjee 直接挑战经典半参数框架中“预测最优的困扰估计即足够”的默认假设，以期望条件协方差为例，论证下游目标泛函的 MSE 可能要求特意欠平滑或过平滑。Young Researchers' Seminar on DAGs 则从另一侧切入：在隐藏变量 DAG 中，当识别函数已知后，如何构造非参数有效的一步校正估计量，并给出针对特定图类的渐近理论——这本质上是将调参问题从“单一困扰函数”扩展到“多个困扰函数构成的识别泛函”。两场共同指向：半参数效率的实践瓶颈不在于理论框架，而在于困扰估计的调参策略与下游目标的匹配。

第二条主线是**因果识别与偏识别**。Sadeghi 试图在纯概率论公理下定义因果，不依赖 SCM 的方程或图结构，仅从干预分布族出发推导马尔可夫性质——这是对 Pearl 框架的激进简化。Song 则聚焦分类 IV 的偏识别，给出封闭形式的识别集刻画，统一了单调性、工具独立性等不同版本 IV 模型的边界。Young Researchers' Seminar on DAGs 的识别部分也属此线：它利用 ADMG 的 sound and complete 识别算法，将可识别参数自动转化为估计问题。三场从不同抽象层级（公理化、图模型、分类 IV）推进了“什么条件下因果量可识别”这一核心追问。

第三条主线是**政策相关性与网络干扰**。Young Researchers' Seminar on Policy Learning 将噪声代理变量纳入最优分配规则，分析代理精度与政策遗憾之间的权衡。Eckles 则从网络干扰出发，质疑现有 estimand（如直接效应、溢出效应）是否真正具有政策相关性——他提出两个判据（可解释为个体效应、可指导政策选择），并指出暴露映射框架下的 estimand 往往只满足其一。两场共享“政策导向”视角，但前者聚焦个体异质性的代理问题，后者聚焦网络结构下的 estimand 选择。

若想快速把握这一季的核心进展，建议按以下路径切入：**半参数效率**入口：先看 Mukherjee（调参问题的基础论述），再看 Young Researchers' Seminar on DAGs（多困扰函数下的具体构造）。**因果识别**入口：先看 Song（分类 IV 的封闭形式边界，技术门槛较低），再看 Sadeghi（公理化框架，更抽象）。**政策导向**入口：先看 Young Researchers' Seminar on Policy Learning（噪声代理与遗憾界），再看 Eckles（网络干扰下的 estimand 选择）。其余三场（Stensrud、Chernozhukov、Rosenbaum）可作为独立专题补充。

## 报告列表

### [Policy Learning with Unobserved Heterogeneity](../2026-03-24-ocis-2026-03-24-young-researchers-seminar.md)
**讲者**: Young Researchers' Seminar · 2026-03-24  
链接：[视频](https://youtu.be/fzowqjMUj1s) · [幻灯片](https://drive.google.com/file/d/1TL2VTXhDoR_dC6rfiiyG0QEcokBWwFBV/view)
<details><summary>摘要</summary>

Empirical research shows that individuals' responses to treatments vary along latent characteristics, such as innate ability or motivation. Therefore, a policymaker seeking to maximize social welfare may consider assigning treatments not only based on observed characteristics, but also on estimated latent traits. I characterize how the accuracy of these estimates affects the worst-case performance of policies, deriving sharp regret bounds for assignment rules that include or exclude them, and il…

</details>

### [Nuisance Parameter Tuning for Estimating Doubly Robust Functionals](../2026-03-17-ocis-2026-03-17-rajarshi-mukherjee.md)
**讲者**: Rajarshi Mukherjee · 2026-03-17  
链接：[视频](https://youtu.be/gOcHwBF5R9Q) · [幻灯片](https://drive.google.com/file/d/1iDS5RQCzXk7D72dcTkBVLaoAg-TckX3U/view?usp=share_link)
<details><summary>摘要</summary>

The purpose is to discuss the issue of nuisance parameter tuning for estimating quantities in observational studies, such as the average treatment effect and measures of conditional dependence. Typical methods for estimating such quantities of interest rely on estimating nuisance functions often through the lens of nonparametric and/or high-dimensional machine learning methods. Whereas many popular ideas pertain to tuning these nuisance function estimators from a prediction perspective and subse…

</details>

### [Policy relevance of causal quantities in networks](../2026-03-10-ocis-2026-03-10-dean-eckles.md)
**讲者**: Dean Eckles · 2026-03-10  
链接：[视频](https://youtu.be/pBhOtOhKEtc) · [幻灯片](https://drive.google.com/file/d/1a8SVAcGS3XQxkDGNrobq6sW1V-z9l8cX/view?usp=share_link) · [arXiv](https://arxiv.org/abs/2507.14391)
<details><summary>摘要</summary>

In settings where units' outcomes are affected by others' treatments, there has been a proliferation of ways to quantify effects of treatments on outcomes, including via indirect exposure to other units' treatments. Here we consider two properties we might want estimands to have: being interpretable as summaries of unit-level effects, and being relevant to choice of a policy governing treatment assignment. We characterize many estimands as involving one of two orders of averaging over units in a…

</details>

### [Causal effects conditional on post-treatment variables](../2026-03-03-ocis-2026-03-03-mats-stensrud.md)
**讲者**: Mats Stensrud · 2026-03-03  
链接：[视频](https://youtu.be/r9Y38RiZ51Y?si=2RcCvO4-VoNLVIZ2) · [幻灯片](https://drive.google.com/file/d/1QswMjLnF3d7JDpmNNrjB8JXP3pBPTsvx/view?usp=sharing)
<details><summary>摘要</summary>

Many studies aim to estimate treatment effects on outcomes that are defined only for individuals who experience a post-treatment event. For example, the effect of cancer therapies on quality of life is only well defined among individuals who are alive. Similarly, the effect of vaccines on post-infection outcomes is only of interest among individuals who become infected. A naive comparison of outcomes conditional on such post-treatment events generally lacks a causal interpretation, even when tre…

</details>

### [A theory of causality with multiple interventions](../2026-02-24-ocis-2026-02-24-kayvan-sadeghi.md)
**讲者**: Kayvan Sadeghi · 2026-02-24  
链接：[视频](https://youtu.be/EkpY1l1sjPQ) · [幻灯片](https://drive.google.com/file/d/1FpXibixrorvPuURys08rx9nzAmTMmT-0/view?usp=share_link)
<details><summary>摘要</summary>

Causal intervention is an essential tool in causal inference. By considering a family of interventional distributions for multiple interventions, we propose simple assumptions that lead to a theory of causality that has several advantages: it does not need to make use of any modeling assumptions such as those imposed by structural causal models; it includes most cases with latent variables and causal cycles; and more importantly, it does not assume the existence of an underlying true causal grap…

</details>

### [Average Causal Effect Estimation in DAGs with Hidden Variables: Beyond Back-Door and Front-Door Criteria](../2026-02-17-ocis-2026-02-17-young-researchers-seminar.md)
**讲者**: Young Researchers' Seminar · 2026-02-17  
链接：[视频](https://youtu.be/GO1z9bECD2k) · [幻灯片](https://drive.google.com/file/d/1pyNTF31HmxdbiGp_6oS7flqBQbCjWl_O/view?usp=sharing) · [arXiv](https://urldefense.com/v3/__https://arxiv.org/abs/2312.10234__;!!G92We9drHetJ8EofZw!br8Se5Hfe2Awk-gMwidOaXwNIcD8eqLn_QgZfj5069BRRr-1Qifuq7GFYX0e_EPqjDya-V5tXTc8speX-cLp_34$)
<details><summary>摘要</summary>

This talk focuses on flexible estimation of causal effects in hidden-variable graphical models. While the identification theory for causal effects in directed acyclic graphs (DAGs) with hidden variables is well developed, methods for estimation and inference of causal functionals beyond the g-formula remain limited. In the first part, we introduce novel one-step–corrected plug-in estimators and targeted minimum loss-based estimators (TMLE) for causal effects in a class of hidden-variable DAGs th…

</details>

### [The Categorical Instrumental Variable Model: Characterization, Partial Identification, and Statistical Inference](../2026-01-13-ocis-2026-01-13-yilin-song.md)
**讲者**: Yilin Song · **讨论人**: Desire Kedagni · 2026-01-13  
链接：[视频](https://youtu.be/GxiyMtWMRVE) · [幻灯片](https://drive.google.com/file/d/1XXoj74siuw30w6j-G4aV9z-EH0WiiAsr/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2405.09510)
<details><summary>摘要</summary>

We study categorical instrumental variable (IV) models with instrument, treatment, and outcome taking finitely many values. We derive a simple closed-form characterization of the set of joint distributions of potential outcomes that are compatible with a given observed data distribution in terms of a set of inequalities. These inequalities unify several different IV models defined by versions of the independence and exclusion restriction assumptions and are shown to be non-redundant. Finally, gi…

</details>

### [Adventures in Demand Analysis Using AI](../2025-01-27-ocis-2025-01-27-victor-chernozhukov.md)
**讲者**: Victor Chernozhukov · 2025-01-27  
链接：[视频](https://youtu.be/YN29rc-E530?si=0Kx99EFwLznzG1_Y)
<details><summary>摘要</summary>

This paper advances empirical demand analysis by integrating multimodal product representations derived from artificial intelligence (AI). Using a detailed dataset of toy cars on Amazon.com , we combine text descriptions, images, and tabular covariates to represent each product using transformer-based embedding models. These embeddings capture nuanced attributes, such as quality, branding, and visual characteristics, that traditional methods often struggle to summarize. Moreover, we fine-tune th…

</details>

### [Being Realistic About Unmeasured Biases in Observational Studies](../2025-01-20-ocis-2025-01-20-paul-rosenbaum.md)
**讲者**: Paul Rosenbaum · 2025-01-20  
链接：[视频](https://youtu.be/S27_5l7leZI?si=6tRwk-DTUPCmVpMC)
<details><summary>摘要</summary>

Observational studies of the effects caused by treatments are always subject to the concern that an ostensible treatment effect may reflect a bias in treatment assignment, rather than an effect actually caused by the treatment. The degree of legitimate concern is strongly affected by simple decisions that an investigator makes during the design and analysis of an observational study. Poor choices lead to heightened concern; that is, poor choices make a study sensitive to small unmeasured biases …

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

