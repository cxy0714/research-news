# OCIS · Spring 2020

- 共 9 场 · 9 篇精读

## 本季导览

> 自动生成：归纳本季主线与值得先看的几场，**不打分、不排名**。

这一季的九场报告大致可归纳为三条主线：**工业实验与自适应推断**（Ya Xu, Susan Murphy）、**半参数效率与双稳健估计**（Eric Tchetgen Tchetgen, Edward Kennedy, Hyunseung Kang）、以及**因果推断的扩展场景**——包括缺失数据（Ilya Shpitser）、网络依赖（Elizabeth Ogburn）、推广性（Elizabeth Tipton）和精细理论检验（Dylan Small）。其中，双稳健方法在多个报告中反复出现，成为贯穿全季的方法论底色。

**半参数效率与双稳健估计**是这一季最密集的主线。Eric Tchetgen Tchetgen 直接处理“如何从多个候选机器学习学习器中选出最优组合来估计半参数目标泛函”这一模型选择问题，提出选择性机器学习框架，核心工具是 Neyman 正交性和交叉拟合。Edward Kennedy 则将双稳健思路延伸到条件平均处理效应（CATE）的估计，推导出最优收敛速率，并给出基于高效影响函数的伪结果回归方法。Hyunseung Kang 的 IV 工作虽不直接使用双稳健框架，但同样涉及“先检验后推断”的选择性推断问题，与 Tchetgen Tchetgen 的模型选择问题在“推断前需处理数据依赖的筛选”这一结构上形成呼应。此外，Susan Murphy 的批处理赌博机推断也涉及自适应数据收集后的推断校正，与上述“选择后推断”问题有方法论上的亲缘性。

**工业实验与网络依赖**构成另一条重要线索。Ya Xu 从 LinkedIn 视角系统梳理了工业 A/B 测试中的实际挑战，包括网络干扰、长期效应和序贯实验，为后续更技术性的报告提供了应用背景。Elizabeth Ogburn 则从社交网络依赖出发，揭示了独立同分布假设被违反时虚假关联的产生机制，并指出其与未测量混杂的差异——这一工作直接呼应了 Ya Xu 提到的网络干扰问题，但提供了更严格的统计理论分析。Elizabeth Tipton 的推广性问题（从随机试验到目标总体）虽不直接涉及网络，但同样处理“样本非随机”这一核心困难，其采样可忽略性假设与 Ogburn 讨论的依赖结构形成对比。

**缺失数据与精细理论检验**是两条相对独立但各有深度的支线。Ilya Shpitser 利用图模型（m-DAGs）统一刻画缺失数据机制，在 MNAR 下给出了识别条件与估计公式，其技术路线与因果推断中的 do-calculus 和 g-formula 一脉相承。Dylan Small 则回溯 Fisher 和 Cochran 的传统，将“精细理论”形式化为多重可检验后果的联合推断，其证据因子框架与 Rosenbaum 的敏感性分析紧密相关，为观察性研究提供了一种不同于单一估计量的证据累积策略。

若想快速把握这一季的核心方法论进展，建议从 **Eric Tchetgen Tchetgen**（选择性机器学习 + 双稳健）和 **Edward Kennedy**（CATE 最优估计）入手，这两场直接推进了半参数效率理论的前沿。若对工业应用或自适应实验感兴趣，可先看 **Ya Xu**（全景式问题介绍）再读 **Susan Murphy**（批处理赌博机推断）。若关注网络依赖或推广性问题，**Elizabeth Ogburn** 和 **Elizabeth Tipton** 提供了互补的视角。**Hyunseung Kang** 和 **Dylan Small** 分别代表“选择后推断”和“证据累积”两条独立但重要的方法论路径，适合作为进阶阅读。

## 报告列表

### [Causal Inference Challenges in Industry : A perspective from experiences at LinkedIn](../2020-05-26-ocis-2020-05-26-ya-xu.md)
**讲者**: Ya Xu · **讨论人**: Iavor Bojinov · 2020-05-26  
链接：[视频](https://www.youtube.com/watch?v=OoKsLAvyIYA) · [幻灯片](https://drive.google.com/file/d/1rcqZ56lWZB2LW_pO5hJ2qlQXm8TqbC_X/view?usp=sharing)
<details><summary>摘要</summary>

In this talk, we will briefly give some background how online controlled experiments are commonly used in industry, and introduce some challenges we face, and also some opportunities in novel applications.

</details>

### [Inference for Batched Bandits](../2020-05-19-ocis-2020-05-19-susan-murphy.md)
**讲者**: Susan Murphy · **讨论人**: Stefan Wager · 2020-05-19  
链接：[视频](https://www.youtube.com/watch?v=iLJ1hC5k-IQ) · [幻灯片](https://drive.google.com/file/d/1u3Pppn9cqmOPVwvM4jd8reR5b1xoz1hv/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2002.03217)
<details><summary>摘要</summary>

As bandit algorithms are increasingly utilized in scientific studies and industrial applications, there is an associated increasing need for reliable inference methods based on the resulting adaptively collected data. In this work, we develop methods for inference on data collected in batches using a bandit algorithm. When there is no unique arm we prove that the ordinary least squares estimator(OLS) is not asymptotically normal on data collected using standard bandit algorithms. This is the cas…

</details>

### [Identification and estimation in graphical models of missing data](../2020-05-12-ocis-2020-05-12-ilya-shpitser.md)
**讲者**: Ilya Shpitser · **讨论人**: Jin Tian · 2020-05-12  
链接：[视频](https://www.youtube.com/watch?v=FRYkkQBfrDg) · [幻灯片](http://auai.org/uai2019/proceedings/papers/428.pdf) · [arXiv](https://arxiv.org/abs/1909.01848)
<details><summary>摘要</summary>

Missing data is a pervasive problem in data analyses, resulting in datasets that contain censored realizations of a target distribution. Many approaches to inference on the target distribution using censored observed data rely on missing data models represented as a factorization with respect to a graph. We describe a simple characterization of all identified missing data models where the full data distribution factorizes with respect to a directed acyclic graph (DAG). We show how statistical in…

</details>

### [Selective Machine Learning of Doubly Robust Functionals](../2020-05-05-ocis-2020-05-05-eric-tchetgen-tchetgen.md)
**讲者**: Eric Tchetgen Tchetgen · **讨论人**: Stijn Vansteelandt · 2020-05-05  
链接：[视频](https://www.youtube.com/watch?v=K-Uo5XbIE9I) · [幻灯片](https://drive.google.com/file/d/1XqTTTNVfrPbWihhnEwKwQdME7eLW05MK/view?usp=sharing) · [arXiv](https://arxiv.org/abs/1911.02029)
<details><summary>摘要</summary>

While model selection is a well-studied topic in parametric and nonparametric regression or density estimation, model selection of possibly high-dimensional nuisance parameters in semiparametric problems is far less developed. In this paper, we propose a selective machine learning framework for making inferences about a finite-dimensional functional defined on a semiparametric model, when the latter admits a doubly robust estimating function. We introduce two model selection criteria for bias re…

</details>

### [Optimal doubly robust estimation of heterogeneous causal effects](../2020-04-28-ocis-2020-04-28-edward-kennedy.md)
**讲者**: Edward Kennedy · **讨论人**: James Robins · 2020-04-28  
链接：[视频](https://www.youtube.com/watch?v=AUOnAfUjDVE) · [幻灯片](https://drive.google.com/file/d/1_fzpAsIuDgzVSgab1NlIelSUAuNmn5l8/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2004.14497)
<details><summary>摘要</summary>

Heterogeneous effect estimation has become a major enterprise in causal inference, with ramifications across medicine and social science, e.g., improving understanding of variation, as well as informing policy and optimizing treatment decisions. Many methods for estimating the conditional average treatment effect (CATE) have been proposed in recent years; however, there are important gaps in the literature, particularly on the theory side, vis-a-vis understanding if and when such methods can be …

</details>

### [Social network dependence, unmeasured confounding, and the replication crisis](../2020-04-21-ocis-2020-04-21-elizabeth-ogburn.md)
**讲者**: Elizabeth Ogburn · **讨论人**: Ilya Shpitser · 2020-04-21  
链接：[视频](https://www.youtube.com/watch?v=uFSVZTDl0aM) · [幻灯片](https://drive.google.com/file/d/1g33lgUXo_q9Etc2puuI__BHGcJq22LUc/view?usp=sharing) · [arXiv](https://arxiv.org/pdf/1908.00520.pdf)

### [W ill this Intervention Work in this Population? Designing Randomized Trials for Generalization](../2020-04-14-ocis-2020-04-14-elizabeth-tipton.md)
**讲者**: Elizabeth Tipton · **讨论人**: Andrew Gelman · 2020-04-14  
链接：[视频](https://www.youtube.com/watch?v=HYP32wzEZMA) · [幻灯片](https://drive.google.com/file/d/1rM3tWP6FKBhgDfODp8zyGRm-bOCp0pm5/view?usp=sharing)

### [Inferring Treatment Effects After Testing Instrument Strength in Linear Models](../2020-04-08-ocis-2020-04-08-hyunseung-kang.md)
**讲者**: Hyunseung Kang · **讨论人**: Will Fithian · 2020-04-08  
链接：[视频](https://www.youtube.com/watch?v=FLxng_1YCGk) · [幻灯片](https://drive.google.com/file/d/1hE1GFeq3Pjk3hqHPylTVkyNDPTGnumnN/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2003.06723)
<details><summary>摘要</summary>

A common practice in IV studies is to check for instrument strength, i.e. its association to the treatment, with an F-test from regression. If the F-statistic is above some threshold, usually 10, the instrument is deemed to satisfy one of the three core IV assumptions and used to test for the treatment effect. However, in many cases, the inference on the treatment effect does not take into account the strength test done a priori. In this paper, we show that not accounting for this pretest can se…

</details>

### [T esting an Elaborate Theory of a Causal Hypothesis](../2020-03-31-ocis-2020-03-31-dylan-small.md)
**讲者**: Dylan Small · **讨论人**: Peter Bühlmann · 2020-03-31  
链接：[视频](https://www.youtube.com/watch?v=DWTDIPuff14) · [幻灯片](http://www-stat.wharton.upenn.edu/~bikramk/papers/integrationef41.pdf)
<details><summary>摘要</summary>

When R.A. Fisher was asked what can be done in observational studies to clarify the step from association to causation, he replied, “Make your theories elaborate” -- when constructing a causal hypothesis, envisage as many different consequences of its truth as possible and plan observational studies to discover whether each of these consequences is found to hold. William Cochran called “this multi-phasic attack…one of the most potent weapons in observational studies.” Statistical tests for the v…

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

