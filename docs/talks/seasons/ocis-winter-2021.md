# OCIS · Winter 2021

- 共 10 场 · 8 篇精读

## 本季导览

> 自动生成：归纳本季主线与值得先看的几场，**不打分、不排名**。

这一季OCIS Winter 2021的10场报告大致可归纳为三条主线：**因果推断的识别与估计方法**（Angrist、Keele、Athey、van der Laan）、**因果表示学习与高维随机化检验**（Zhang、Bates）、以及**实验设计与平台实践**（Green、Tingley & Wong、Li、Robins访谈）。其中，Robins访谈作为方法史回顾，贯穿多条主线。

最突出的主线是**因果效应的识别与估计方法**，覆盖了从面板数据到医院质量比较的多个场景。Angrist利用学校分配中的随机化构造简单可信的增值估计，Keele通过近似平衡权重实现医院质量的直接标准化，Athey提出合成双重差分（SDID）以融合DID与合成控制法的优势，van der Laan则推进高阶TMLE以处理有限样本中二阶余项主导的问题。这些工作共同关注如何在非理想条件下（如非随机分配、稀疏数据、高维nuisance）获得稳健且高效的估计。另一条主线是**因果表示学习与随机化检验**：Zhang系统介绍从观测数据中发现因果关系的方法，包括利用非平稳数据特性进行因果发现；Bates则利用父母-子代三人家组中的孟德尔随机化构造条件独立性检验，以检测基因组区域对表型的因果效应，两者都强调从数据中恢复因果结构而非仅估计效应。此外，**实验设计与平台实践**也值得注意：Green通过乌干达的大规模安慰剂对照实验检测教育娱乐的溢出效应，Tingley & Wong介绍Netflix的民主化实验平台如何支持快速创新，Li则处理稀疏不规则纵向数据下的因果中介分析。

若想快速了解这一季的核心内容，建议按以下路径选择：**面板数据与政策评估**可先看Athey（SDID）打底，再读Angrist（学校分配中的随机化）和Keele（医院质量比较）作为不同场景的延伸；**因果发现与高维检验**可从Zhang（因果表示学习）入手，再读Bates（遗传三人家组随机化检验）作为具体应用；**实验设计与溢出效应**可先看Green（安慰剂对照与溢出测量），再读Tingley & Wong（平台实践）和Li（纵向中介分析）作为补充；**方法理论基础**则直接看van der Laan（高阶TMLE）和Robins访谈（方法史回顾）。

## 报告列表

### Simple and Credible Value-Added Estimation Using Centralized School Assignment　*（暂无精读）*
**讲者**: Joshua Angrist · **讨论人**: Jesse Rothstein · 2021-03-23  
链接：[幻灯片](https://drive.google.com/file/d/16xoMEFqgtI-w6My8e0AgH6P1zKgZC-lW/view?usp=sharing)
<details><summary>摘要</summary>

Many large urban school districts match students to schools using algorithms that incorporate an element of random assignment. We introduce two simple empirical strategies to harness this randomization for value-added models (VAMs) measuring the causal effects of individual schools. The first estimator controls for the probability of being offered admission to different schools, treating the take-up decision as independent of potential outcomes. Randomness in school assignments is used to test t…

</details>

### [Learning and Using Causal Representations](../2021-03-16-ocis-2021-03-16-kun-zhang.md)
**讲者**: Kun Zhang · **讨论人**: C osma Shalizi Abstrac t: When do we have to make use of causal knowledge, and when does associational information suffice for machine learning? Can we find the causal direction between two variables by analyzing their observed values? Can we figure out where latent causal variables should be and how they are related? For the purpose of understanding and manipulating systems properly, people often attempt to answer such causal questions. Furthermore, we are often concerned with artificial intelligence in complex environments. For instance, how can we do transfer learning in a principled way? How can machines deal with adversarial attacks? Interestingly, it has recently been shown that causal information can facilitate understanding and solving various AI problems. This talk focused on how to learn causal representations from observation data and why and how the causal perspective allows adaptive prediction and a potentially higher level of artificial intelligence. · 2021-03-16  
链接：[视频](https://youtu.be/_MVi6XzOdD0) · [幻灯片](https://drive.google.com/file/d/172ikPRXvnPD_T1JDEdLYzkJdB1VKrCiY/view?usp=sharing)

### [Hospital Quality Risk Standardization via Approximate Balancing Weights](../2021-03-09-ocis-2021-03-09-luke-keele.md)
**讲者**: Luke Keele · **讨论人**: Sam Pimentel · 2021-03-09  
链接：[视频](https://youtu.be/dErj2RsHm5Y) · [幻灯片](https://drive.google.com/file/d/1Th02gZrFyDFGn0Uq1JlTucagbOBuEtc4/view?usp=sharing) · [arXiv](https://arxiv.org/abs/1911.03071)
<details><summary>摘要</summary>

Comparing outcomes across hospitals, often to identify underperforming hospitals, is a critical task in health services research. However, naive comparisons of average outcomes, such as surgery complication rates, can be misleading because hospital case mixes differ — a hospital’s overall complication rate may be lower due to more effective treatments or simply because the hospital serves a healthier population overall. In this paper, we develop a method of “direct standardization” where we re-w…

</details>

### [Causal Mediation Analysis for Sparse and Irregular Longitudinal Data](../2021-02-23-ocis-2021-02-23-fan-li.md)
**讲者**: Fan Li · **讨论人**: Georgia Papadogeorgou · 2021-02-23  
链接：[视频](https://youtu.be/l1C3DPf9eZw) · [幻灯片](https://drive.google.com/file/d/1B_ptIK4B6FeyIkOW7J6ACh7bNqR82tbb/view?usp=sharing)
<details><summary>摘要</summary>

Causal mediation analysis seeks to investigate how the treatment effect of an exposure on outcomes is mediated through intermediate variables. Although many applications involve longitudinal data, the existing methods are not directly applicable to settings where the mediator and outcome are measured on sparse and irregular time grids. We extend the existing causal mediation framework from a functional data analysis perspective, viewing the sparse and irregular longitudinal data as realizations …

</details>

### [Using Placebo-Controlled Designs to Detect Edutainment Effects and Spillovers: Results from Two Large-Scale Experiments in Uganda](../2021-02-16-ocis-2021-02-16-donald-green.md)
**讲者**: Donald Green · **讨论人**: Molly Offer-Westort · 2021-02-16  
链接：[视频](https://youtu.be/qD5Ed9CF7f8) · [幻灯片](https://drive.google.com/file/d/1wizN17wB83E79K-b1T2af-O4SDDwzJ3U/view?usp=sharing)
<details><summary>摘要</summary>

Education–entertainment refers to dramatizations designed to convey information and to change attitudes. Buoyed by observational studies suggesting that education–entertainment strongly influences beliefs, attitudes and behaviours, scholars have recently assessed education–entertainment by using rigorous experimental designs in field settings. Studies conducted in developing countries have repeatedly shown the effectiveness of radio and film dramatizations on outcomes ranging from health to grou…

</details>

### Supporting Innovation and Scale with a Democratized Experimentation Platform　*（暂无精读）*
**讲者**: Martin Tingley and Jeffrey Wong · **讨论人**: Iavor Bojinov · 2021-02-09  
<details><summary>摘要</summary>

The Netflix Experimentation Platform is democratized and modular: data scientists can contribute metrics, causal inference methods, and visualizations directly to the platform, and use these building blocks to compose flexible reports that flow through to our frontend UI. This contribution model supports rapid prototyping and innovation, as data scientists contribute directly to production systems. To ensure that the platform continues to support the required scale (number and size of tests), we…

</details>

### [ocis-2021-02-02-interview-with-james-robins](../2021-02-02-ocis-2021-02-02-interview-with-james-robins.md)
**讲者**: Interview with James Robins · 2021-02-02  
链接：[视频](https://youtu.be/j26nYFxRJr0)

### [Causal Inference in Genetic Trio studies](../2021-01-26-ocis-2021-01-26-stephen-bates.md)
**讲者**: Stephen Bates · **讨论人**: Qingyuan Zhao · 2021-01-26  
链接：[视频](https://youtu.be/FLDT6T52Kcc) · [幻灯片](https://drive.google.com/file/d/13E4hwS93QZmqTzGwCKxH5isjaGbEoTtE/view?usp=sharing)
<details><summary>摘要</summary>

This work introduces a randomization test using high-dimensional genotypes to identify causal relationships between regions of the genome and outcomes (e.g., presence or absence of asthma). The proposed method is immune to the confounding factors typically encountered in genetic association studies because inference relies only on the randomness in the process of inheritance, a source of plausibly independent variation. As a randomization test, the proposed method can leverage black-box machine …

</details>

### [Higher order Targeted Maximum Likelihood Estimation](../2021-01-19-ocis-2021-01-19-mark-van-der-laan.md)
**讲者**: Mark van der Laan · **讨论人**: Alex Luedtke · 2021-01-19  
链接：[视频](https://www.youtube.com/watch?v=2jumfnRQpxs) · [幻灯片](https://drive.google.com/file/d/1DfsoZUjgf3L8ly_wO3ye_U45-LNWMwfX/view?usp=sharing)
<details><summary>摘要</summary>

Asymptotic linearity and efficiency of targeted maximum likelihood estimators (TMLE) of target features of the data distribution relies on a a second order remainder being asymptotically negligible. However, in finite samples, the second order remainder can dominate the sampling distribution so that inference based on asymptotic normality would be anti-conservative. We propose a new higher order (say k-th order) TMLE, generalizing the regular (first order) TMLE. We prove that it satisfies an exa…

</details>

### [Synthetic Difference in Differences](../2021-01-12-ocis-2021-01-12-susan-athey.md)
**讲者**: Susan Athey · 2021-01-12  
链接：[视频](https://www.youtube.com/watch?v=r2DzGAigTl4&feature=youtu.be) · [幻灯片](https://drive.google.com/file/d/1gRHwttUSBKq6nf-10Ta9ut5V1TPnD8CS/view?usp=sharing) · [arXiv](https://arxiv.org/abs/1812.09970)
<details><summary>摘要</summary>

We present a new estimator for causal effects with panel data that builds on insights behind the widely used difference in differences and synthetic control methods. Relative to these methods, we find, both theoretically and empirically, that the proposed ``synthetic difference in differences'' estimator has desirable robustness properties, and that it performs well in settings where the conventional estimators are commonly used in practice. We study the asymptotic behavior of the estimator when…

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

