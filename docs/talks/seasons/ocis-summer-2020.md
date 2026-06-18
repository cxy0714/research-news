# OCIS · Summer 2020

- 共 13 场 · 13 篇精读

## 本季导览

> 自动生成：归纳本季主线与值得先看的几场，**不打分、不排名**。

OCIS Summer 2020 的 13 场报告可归纳为四条主线：**匹配与设计基础**（Rudin/Volfovsky/Roy、Toulis、Eckles、Rosenbaum）、**半参数效率与有限样本推断**（Kolesár、Papadogeorgou/Lei）、**因果图与结构学习**（Maathuis、Uhler、Peters）、以及**实验设计与平台应用**（Bakshy、Gelman、Lok、Xu/Pang）。其中，匹配与设计基础、半参数效率两条主线贯穿多场，且对同一问题（如有限样本偏差、干扰下的推断）提供了不同切法。

**匹配与设计基础**是这一季最密集的主线。Rudin/Volfovsky/Roy 的 **Almost Matching Exactly** 直接挑战倾向得分匹配的个体保真度损失，用可解释的精确匹配估计 CATE。Toulis 用图论构造条件随机化检验，处理干扰下的尖锐原假设问题——与 Eckles 的 **Noise induced randomization in RDD** 形成对照：后者将阈值附近的随机化归因于运行变量的测量噪声，而非人为构造条件事件。Rosenbaum 的 **Replication and Evidence Factors** 则从更高层面整合多个设计（如不同偏差来源的检验），为观察性研究提供非重复复制框架。这四场共同追问：在非随机化设定下，如何通过设计（而非模型）保证推断的有效性。

**半参数效率与有限样本推断**是另一条突出主线。Kolesár 的 **Finite-Sample Optimal Estimation** 直接批评主流半参数方法在有限样本中的偏差，用非参数光滑约束构造最优置信区间，不依赖渐近正态临界值。Papadogeorgou/Lei 的两部分报告分别处理时空点过程因果效应（用随机干预对比定义效应）和条件平均处理效应的不确定性量化——后者与 Kolesár 共享对“渐近外衣”的警惕，但采用不同的技术路径（贝叶斯 vs 频率学派有限样本最优）。这两场可视为对半参数效率理论“有限样本脆弱性”的两种回应。

**因果图与结构学习**主线由 Maathuis 和 Uhler 代表。Maathuis 的 **IDA 算法**将结构学习（CPDAG）与协变量调整（back-door 准则）端到端整合，估计总因果效应并给出有效调整集的图论刻画。Uhler 则聚焦药物重定位，将问题拆解为跨干预的因果迁移（用 DAG 结构预测未实验干预的效果）和跨细胞类型的迁移（用因果特征选择保证分布泛化）。Peters 的 **Causality and distribution generalization** 从理论层面统一了这类问题：用结构因果模型刻画分布变化，比较因果预测与 DRO 的优劣。这三场共同推进“如何用因果图指导预测与迁移”。

**实验设计与平台应用**主线以 Bakshy 的 **Efficient Experimentation** 为核心，讨论高维决策空间下的贝叶斯优化与元分析，强调 batch 更新而非逐次赌博机。Gelman 的 **100 Stories** 从元科学角度批判个案故事作为证据的可靠性，与 Rosenbaum 的证据因子形成互补（故事 vs 形式化复制）。Lok 的 **Causal organic indirect and direct effects** 处理中介分析中的交叉世界假设，提出产品方法在二元中介下的推广。Xu/Pang 的 **Bayesian SCM** 用动态多层潜因子模型替代合成控制法，提供形式化推断。

**快速入口指引**：若想了解匹配与设计基础，先看 Rudin/Volfovsky/Roy（AME 核心思想）和 Toulis（条件随机化检验），进阶看 Eckles（RDD 噪声随机化）和 Rosenbaum（证据因子）。若关注半参数效率的有限样本问题，先看 Kolesár（有限样本最优 CI），再看 Papadogeorgou/Lei 的第二部分（CATE 不确定性）。若对因果图与迁移感兴趣，先看 Maathuis（IDA 流程），再看 Peters（分布泛化理论），Uhler 作为应用案例。若关注实验设计，先看 Bakshy（贝叶斯优化），再看 Gelman（故事与证据）作为方法论反思。

## 报告列表

### [Almost Matching Exactly](../2020-08-25-ocis-2020-08-25-cynthia-rudin-alexander-volfovsky-sudeep.md)
**讲者**: Cynthia Rudin, Alexander Volfovsky, Sudeepa Roy · **讨论人**: Guillaume Basse · 2020-08-25  
链接：[视频](https://www.youtube.com/watch?v=-So_cL-eMFQ) · [幻灯片](https://drive.google.com/file/d/1gdVhaltmZWJ5QvoQU1S2cJod0xYOkbNe/view?usp=sharing)

### [Causal organic indirect and direct effects: closer to Baron and Kenny, with a product method for binary mediators](../2020-08-18-ocis-2020-08-18-judith-lok.md)
**讲者**: Judith Lok · 2020-08-18  
链接：[视频](https://www.youtube.com/watch?v=AB_DR0JhflU) · [幻灯片](https://drive.google.com/file/d/1lZWnpLU3bQttTb6IIljm2jDoionxS0Lb/view?usp=sharing) · [arXiv](https://arxiv.org/abs/1903.04697)

### [Randomization tests for spillovers under general interference: A graph-theoretic approach](../2020-08-11-ocis-2020-08-11-panos-toulis.md)
**讲者**: Panos Toulis · **讨论人**: Peng Ding · 2020-08-11  
链接：[视频](https://www.youtube.com/watch?v=75G5NUekSj0) · [幻灯片](https://drive.google.com/file/d/1LcZgOYYyYnf8By5ckALswYh7bESLUcBv/view?usp=sharing) · [arXiv](https://arxiv.org/pdf/1910.10862.pdf)
<details><summary>摘要</summary>

Interference exists when a unit’s outcome depends on another unit’s treatment assignment. For example, intensive policing on one street could have a spillover effect on neighboring streets. Classical randomization tests typically break down in this setting because many null hypotheses of interest are no longer sharp under interference. A promising alternative is to instead construct a conditional randomization test on a subset of units and assignments for which a given null hypothesis is sharp. …

</details>

### [100 Stories of Causal Inference](../2020-08-04-ocis-2020-08-04-andrew-gelman.md)
**讲者**: Andrew Gelman · 2020-08-04  
链接：[视频](https://www.youtube.com/watch?v=jnI5KI843Lk) · [幻灯片](http://www.stat.columbia.edu/~gelman/research/published/storytelling.pdf)
<details><summary>摘要</summary>

In social science we learn from stories. The best stories are anomalous and immutable (see http://www.stat.columbia.edu/~gelman/research/published/storytelling.pdf ). We shall briefly discuss the theory of stories, the paradoxical nature of how we learn from them, and how this relates to forward and reverse causal inference. Then we will go through some stories of applied causal inference and see what lessons we can draw from them. We hope this talk will be useful as a model for how you can bett…

</details>

### [Causal inference with spatio-temporal data: estimating the effects of airstrikes on insurgent violence in Iraq](../2020-07-28-ocis-2020-07-28-georgia-papadogeorgou-and-lihua-lei.md)
**讲者**: Georgia Papadogeorgou and Lihua Lei · 2020-07-28  
链接：[视频](https://www.youtube.com/watch?v=Tvm3fFYVroo) · [幻灯片](https://drive.google.com/file/d/1qa_SWRshbEFLZQ7msGiC2gc5MxaTBlkI/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2006.06138)
<details><summary>摘要</summary>

Evaluating treatment effect heterogeneity widely informs treatment decision making. At the moment, much emphasis is placed on the estimation of the conditional average treatment effect via flexible machine learning algorithms. While these methods enjoy some theoretical appeal in terms of consistency and convergence rates, they generally perform poorly in terms of uncertainty quantification. This is troubling since assessing risk is crucial for reliable decision-making in sensitive and uncertain …

</details>

### [A Bayesian Alternative to Synthetic Control for Comparative Case Studies: A Dynamic Multilevel Latent Factor Model with Hierarchical Shrinkage](../2020-07-21-ocis-2020-07-21-yiqing-xu-and-xun-pang.md)
**讲者**: Yiqing Xu and Xun Pang · **讨论人**: Dmitry Arkhangelsky · 2020-07-21  
链接：[视频](https://www.youtube.com/watch?v=BAX_VuIPMf0) · [幻灯片](https://drive.google.com/file/d/1oyygJDn5u_HXMAKtGyFhXdiwvweSJQey/view?usp=sharing)
<details><summary>摘要</summary>

This paper proposes a Bayesian alternative to the synthetic control method (SCM) for comparative case studies based on a posterior predictive approach to Rubin's causal model. Our counterfactual imputation method generalizes the SCM by assigning observation-specific parameters to covariates of treated units and exploiting high-order relationships between treated and control time series. The model includes a dynamic latent factor term to correct biases induced by unit-specific time trends and oth…

</details>

### [Finite-Sample Optimal Estimation and Inference on Average Treatment Effects Under Unconfoundedness](../2020-07-14-ocis-2020-07-14-michal-koles-r.md)
**讲者**: Michal Kolesár · **讨论人**: Luke Miratrix · 2020-07-14  
链接：[视频](https://www.youtube.com/watch?v=KhEWdQ8Mtmo) · [幻灯片](https://drive.google.com/file/d/1mU1mKUwtrtliH5jfakZwX8MtBqBxUI1V/view?usp=sharing)
<details><summary>摘要</summary>

We consider estimation and inference on average treatment effects under unconfoundedness conditional on the realizations of the treatment variable and covariates. Given nonparametric smoothness and/or shape restrictions on the conditional mean of the outcome variable, we derive estimators and confidence intervals (CIs) that are optimal in finite samples when the regression errors are normal with known variance. In contrast to conventional CIs, our CIs use a larger critical value that explicitly …

</details>

### [Causal Inference in the Light of Drug Repurposing for SARS-CoV-2](../2020-07-07-ocis-2020-07-07-caroline-uhler.md)
**讲者**: Caroline Uhler · 2020-07-07  
链接：[视频](https://www.youtube.com/watch?v=e-xUUdTIFeU) · [幻灯片](https://drive.google.com/file/d/1yTmliTXycGhEJ-yTJZK-S-ibfJYQWe0W/view?usp=sharing)
<details><summary>摘要</summary>

Massive data collection holds the promise of a better understanding of complex phenomena and ultimately, of better decisions. An exciting opportunity in this regard stems from the growing availability of perturbation / intervention data (drugs, knockouts, overexpression, etc.) in biology. In order to obtain mechanistic insights from such data, a major challenge is the development of a framework that integrates observational and interventional data and allows predicting the effect of yet unseen i…

</details>

### [Total causal effect estimation by combining causal structure learning and covariate adjustment](../2020-06-30-ocis-2020-06-30-marloes-maathuis.md)
**讲者**: Marloes Maathuis · **讨论人**: Daniel Malinsky · 2020-06-30  
链接：[视频](https://www.youtube.com/watch?v=fpildpVeRTk) · [幻灯片](https://drive.google.com/file/d/1IQBi6bZFpVc5jKFIoqneCzQcYFZmbJfD/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2002.06825)
<details><summary>摘要</summary>

I will discuss a line of work that combines causal structure learning and covariate adjustment to estimate causal effects from observational data. In particular, I will discuss the IDA algorithm and some of its variations, the generalized backdoor criterion, the generalized adjustment criterion, and a graphical characterization of efficient adjustment sets. Throughout, examples will be used to illustrate the concepts.

</details>

### [Efficient Experimentation and Inference for Large Decision Spaces](../2020-06-23-ocis-2020-06-23-eytan-bakshy.md)
**讲者**: Eytan Bakshy · **讨论人**: Dean Eckles · 2020-06-23  
链接：[视频](https://www.youtube.com/watch?v=z0cHeMEYpNU) · [幻灯片](https://drive.google.com/file/d/1OLJTSuGKzL3hgKYdd3hu-innCoHbEPjX/view?usp=sharing)
<details><summary>摘要</summary>

Internet service providers routinely leverage randomized experiments to optimize products and improve decision making. I will describe recent directions in adaptive experimentation, meta-analysis, and causal inference that draw on large-scale experiments at Facebook. I will first describe the general problem of experimenting with large action spaces, and a simple solution to this problem: Bayesian optimization. I will then describe how meta-analysis can be used to improve decision quality, and m…

</details>

### [Causality and distribution generalization](../2020-06-16-ocis-2020-06-16-jonas-peters.md)
**讲者**: Jonas Peters · **讨论人**: Yuansi Chen · 2020-06-16  
链接：[视频](https://www.youtube.com/watch?v=pg51RFCIr48) · [幻灯片](https://drive.google.com/file/d/1Ly2CIwP_-WObVOgMTFkYA0O3HOdpYtcF/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2006.07433)
<details><summary>摘要</summary>

Purely predictive methods do not perform well when the test distribution changes too much from the training distribution. Causal models are known to be stable with respect to distributional shifts such as arbitrarily strong interventions on the covariates, but may not perform well when the test distribution differs only mildly from the training distribution. As a result, methods have been proposed that provide a trade off between causal and predictive models. We provide conditions under which su…

</details>

### [Noise induced randomization in regression discontinuity designs](../2020-06-09-ocis-2020-06-09-dean-eckles.md)
**讲者**: Dean Eckles · **讨论人**: Michal Kolesár · 2020-06-09  
链接：[视频](https://www.youtube.com/watch?v=pCYINm_YrbI) · [幻灯片](https://drive.google.com/file/d/1s5AQlHa2zp7pEvgLR4pUxCYP-FC82dSo/view?usp=sharing)
<details><summary>摘要</summary>

Joint work with Nikolaos Ignatiadis, Stefan Wager & Han Wu. Regression discontinuity designs are used to estimate causal effects in settings where treatment is determined by whether an observed running variable crosses a pre-specified threshold. While the resulting sampling design is sometimes described as akin to a locally randomized experiment in a neighborhood of the threshold, standard formal analyses do not make reference to probabilistic treatment assignment and instead identify treatment …

</details>

### [Replication and Evidence Factors in Observational Studies](../2020-06-02-ocis-2020-06-02-paul-rosenbaum.md)
**讲者**: Paul Rosenbaum · 2020-06-02  
链接：[视频](https://www.youtube.com/watch?v=xQRfPcd3XqA) · [幻灯片](https://drive.google.com/file/d/12OPu8lgCYoRaV_hghzyz9wnKMt1RQcZt/view?usp=sharing)
<details><summary>摘要</summary>

Observational studies are often biased by failure to adjust for a covariate that was not measured. A series of studies may replicate an association because the bias that produced this association has been replicated, not because a treatment effect has been demonstrated. To be of value, a replication should remove, or reduce, or at least vary a potential source of bias that resulted in uncertainty in earlier studies. Having defined the goal of replication in this way, we may ask: Can one observat…

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

