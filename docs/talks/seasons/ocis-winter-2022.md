# OCIS · Winter 2022

- 共 9 场 · 8 篇精读

## 本季导览

> 自动生成：归纳本季主线与值得先看的几场，**不打分、不排名**。

这一季的 9 场报告围绕三条主线展开：**动态系统下的因果推断与策略学习**（Chengchun Shi、Kosuke Imai）、**分布漂移与域适应**（Yuansi Chen、Dominik Rothenhäusler）、**观测研究中的估计与敏感性分析**（Luke Keele、Zhimei Ren、Daniel McCaffrey、Sach Mukherjee）。此外，Guido Imbens 的访谈为这些子方向提供了历史背景与学术生态的回顾。

**动态系统与策略学习**是这一季最突出的主线。Chengchun Shi 直接处理 A/B 测试中因系统状态演化导致的携带效应，用强化学习框架为交替时间间隔设计提供序贯检验方法。Kosuke Imai 则聚焦于确定性基线策略下的安全策略学习，利用部分识别与稳健优化确保新策略不劣于现状。两条工作都涉及“动态”与“决策”，但切入角度不同：Shi 侧重假设检验与序贯监控，Imai 侧重策略学习与保守性保障。**分布漂移与域适应**是另一条密集主线。Yuansi Chen 从结构因果模型出发，为域适应提供理论条件，明确何时利用目标域无标签数据能超越仅用源域数据的基线。Dominik Rothenhäusler 则提出“校准推断”框架，将分布不确定性（如抽样偏差、未观测混杂）与研究者自由度纳入推断，本质上是对域适应中“目标域未知”这一问题的更一般化处理。两条工作都试图为“数据分布变化下的可靠推断”提供理论保证，但 Chen 聚焦于预测任务，Rothenhäusler 聚焦于参数估计与置信区间。

**观测研究中的估计与敏感性分析**覆盖了从方法选择到个体效应推断的多个层面。Luke Keele 在无未观测混杂假设下，系统比较回归、倾向性评分、双稳健机器学习等调整方法的实际表现，为实践者提供选择指南。Zhimei Ren 将共形推断与敏感性分析结合，为个体处理效应提供对未观测混杂强度（Gamma 值）的稳健量化。Daniel McCaffrey 则处理非随机样本问题，讨论抽样权重应在倾向得分估计还是结果加权阶段使用，连接了抽样调查与因果推断。Sach Mukherjee 在高维场景下用机器学习方法重构因果结构学习，与 Keele 的“估计方法选择”形成互补——前者关注结构，后者关注效应。

若想快速把握这一季的核心贡献，建议按以下路径观看：**动态系统与策略学习**入口：先看 Chengchun Shi（打底，理解携带效应与序贯检验的基本框架），再看 Kosuke Imai（进阶，学习如何将部分识别与稳健优化融入策略学习）。**分布漂移与域适应**入口：先看 Yuansi Chen（打底，理解结构因果模型如何为域适应提供识别条件），再看 Dominik Rothenhäusler（进阶，理解分布不确定性与研究者自由度如何被统一量化）。**观测研究中的估计与敏感性分析**入口：先看 Luke Keele（打底，了解主流调整方法的实际表现），再看 Zhimei Ren（进阶，学习个体效应推断与共形推断的结合），最后可看 Daniel McCaffrey 与 Sach Mukherjee 作为补充（分别处理抽样偏差与高维结构学习）。Guido Imbens 的访谈适合作为背景阅读，穿插在任何主线之后。

## 报告列表

### [- A reinforcement learning framework for dynamic causal effects evaluation in A/B testing](../2022-03-15-ocis-2022-03-15-chengchun-shi.md)
**讲者**: Chengchun Shi · **讨论人**: Will Wei Sun · 2022-03-15  
链接：[视频](https://youtu.be/Zor1CmRyycw) · [幻灯片](https://drive.google.com/file/d/1oq59VQ2rWP2P5sFG9U_cV0BYYYyIQ3Gs/view?usp=sharing)
<details><summary>摘要</summary>

A/B testing, or online experiment is a standard business strategy to compare a new product with an old one in pharmaceutical, technological, and traditional industries. Major challenges arise in online experiments of two-sided marketplace platforms (e.g., Uber) where there is only one unit that receives a sequence of treatments over time. In those experiments, the treatment at a given time impacts current outcome as well as future outcomes. In this talk, we introduce a reinforcement learning fra…

</details>

### [- Domain adaptation under structural causal models](../2022-03-08-ocis-2022-03-08-yuansi-chen.md)
**讲者**: Yuansi Chen · **讨论人**: Biwei Huang · 2022-03-08  
链接：[视频](https://youtu.be/d-5KomewQis) · [幻灯片](https://drive.google.com/file/d/14mXLxH6-Z1sqqkeyRxSlsV890I_PBb2u/view?usp=sharing)
<details><summary>摘要</summary>

Domain adaptation (DA) arises as an important problem in statistical machine learning when the source data used to train a model is different from the target data used to test the model. Recent advances in DA have mainly been application-driven and have largely relied on the idea of a common subspace for source and target data. To understand the empirical successes and failures of DA methods, we propose a theoretical framework via structural causal models that enables analysis and comparison of …

</details>

### [Safe Policy Learning through Extrapolation: Application to Pre-trial Risk Assessment](../2022-03-01-ocis-2022-03-01-kosuke-imai.md)
**讲者**: Kosuke Imai · **讨论人**: Yifan Cui · 2022-03-01  
链接：[视频](https://youtu.be/Gd2-MxJQTKA) · [幻灯片](https://drive.google.com/file/d/1QR08Lrr0P0BrpiK0IA1v5GrmKIQorMrG/view?usp=sharing) · [arXiv](https://arxiv.org/pdf/2109.11679.pdf)
<details><summary>摘要</summary>

Algorithmic recommendations and decisions have become ubiquitous in today’s society. Many of these and other data-driven policies, especially in the realm of public policy, are based on known, deterministic rules to ensure their transparency and interpretability. For example, algorithmic pre-trial risk assessments, which serve as our motivating application, provide relatively simple, deterministic classification scores and recommendations to help judges make release decisions. How can we use the…

</details>

### [Rothenhäusler - Calibrated inference: statistical inference that accounts for both sampling uncertainty and distributional uncertainty](../2022-02-22-ocis-2022-02-22-dominik.md)
**讲者**: Dominik · **讨论人**: Guido Imbens · 2022-02-22  
链接：[视频](https://youtu.be/LrMzAKDEbDA) · [幻灯片](https://drive.google.com/file/d/1iCQ_Hi1GnvCA3nKSqglT5Ha8fCEbmPZl/view?usp=sharing)
<details><summary>摘要</summary>

During data analysis, analysts often have to make seemingly arbitrary decisions. For example during data pre-processing, there are a variety of options for dealing with outliers or inferring missing data. Similarly, many specifications and methods can be reasonable to address a certain domain question. This may be seen as a hindrance to reliable inference since conclusions can change depending on the analyst's choices. In this paper, we argue that this situation is an opportunity to construct co…

</details>

### [- So Many Choices: The Comparative Performance of Statistical Adjustment Methods](../2022-02-15-ocis-2022-02-15-luke-keele.md)
**讲者**: Luke Keele · **讨论人**: Iván Díaz · 2022-02-15  
链接：[视频](https://youtu.be/CjZnQ3ToJjg) · [幻灯片](https://drive.google.com/file/d/1cNB6jpr2ABMK7c_U2U4779OWgjVOR5lO/view?usp=sharing)
<details><summary>摘要</summary>

Much evidence in applied research is based on observational studies where investigators assume that there are no unobservable differences between the groups under comparison. Treatment effects are estimated after adjusting for observed confounders via statistical methods. However, even if the assumption of no unobserved confounding holds, bias from model misspecification may be significant. Traditionally, regression models of various kinds have been used to adjust for confounders. Such models im…

</details>

### [- Sensitivity Analysis of Individual Treatment Effects: A Robust Conformal Inference Approach](../2022-02-08-ocis-2022-02-08-zhimei-ren.md)
**讲者**: Zhimei Ren · **讨论人**: Stefan Wager · 2022-02-08  
链接：[视频](https://youtu.be/aM3auY7kgSA) · [幻灯片](https://drive.google.com/file/d/1Fdq3fhUZa0wi-goqGtzDUHxobNHsh6I3/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2111.12161)
<details><summary>摘要</summary>

We propose a model-free framework for sensitivity analysis of individual treatment effects (ITEs), building upon ideas from conformal inference. For any unit, our procedure reports the Gamma-value, a number which quantifies the minimum strength of confounding needed to explain away the evidence for ITE. Our approach rests on the reliable predictive inference of counterfactuals and ITEs in situations where the training data is confounded. Under the marginal sensitivity model of Tan (2006), we cha…

</details>

### [- Nonrandom Samples and Causal Inference](../2022-01-25-ocis-2022-01-25-daniel-mccaffrey.md)
**讲者**: Daniel McCaffrey · **讨论人**: Shu Yang · 2022-01-25  
链接：[视频](https://youtu.be/et3eUSM0mu0) · [幻灯片](https://drive.google.com/file/d/1Xjl0cXxLMd2t9ywiDmCEQthDMxP3VJgW/view?usp=sharing)
<details><summary>摘要</summary>

Causal inferences, i.e., estimates of how a treatment or intervention affects outcomes, are of great interest in many fields. There are many causal modeling methods for estimating causal effects from observational data that attempt to adjust for potential biases due to the differences between individuals receiving different treatments in natural settings. These methods nearly universally implicitly assume the data are a random sample from the population of interest. Nonrandom samples occur when …

</details>

### - A machine learning approach for causal structure estimation in high dimensions　*（暂无精读）*
**讲者**: Sach Mukherjee · **讨论人**: Yuhao Wang · 2022-01-18  
链接：[幻灯片](https://drive.google.com/file/d/1aeATEv81wjqBmWt581k9pgG_A5ZvHdlX/view?usp=sharing)
<details><summary>摘要</summary>

Causal structure learning refers to the task of estimating graphical structures encoding causal relationships between variables. This remains challenging, especially under conditions of high dimensionality, latent variables and noisy, finite data, as seen in many real world applications. I will discuss our recent efforts to reframe specific aspects of causal structure learning from a machine learning perspective. The approaches I will discuss differ from classical structure learning tools in tha…

</details>

### [ocis-2022-01-11-interview-with-guido-imbens](../2022-01-11-ocis-2022-01-11-interview-with-guido-imbens.md)
**讲者**: Interview with Guido Imbens · 2022-01-11  
链接：[视频](https://youtu.be/DuVVy1WM-qM) · [幻灯片](https://drive.google.com/file/d/1258iqrVEHTaz7J6xBnqOIpSKret3z9d6/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2108.03726)


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

