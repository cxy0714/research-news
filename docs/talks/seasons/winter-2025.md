# OCIS · Winter 2025

- 共 11 场 · 11 篇精读 · Online Causal Inference Seminar

## 本季导览

> 自动生成：归纳本季主线与值得先看的几场，**不打分、不排名**。

这一季的 11 场报告围绕四条主线展开：**面板数据与非参数识别**（Imbens）、**合成控制与实验设计**（Abadie）、**近端因果推断及其应用**（Keith, Syrgkanis, Tchetgen Tchetgen, Kolesár）、以及**因果表示学习与发现评估**（Young researchers, Petersen, Zhao）。此外，**干扰与空间因果**（Zigler）和**遥感数据融合**（Viviano）构成两条独立但方法上互补的支线。

**近端因果推断**是本季最突出的主线，覆盖四场报告。Keith 将 proximal 框架引入文本数据，利用未标注文本作为未观测混杂的代理变量，绕过传统监督标注需求；Syrgkanis 则将其应用于临床偏见检测，用代理变量分离患者真实健康状态与医生决策偏差。Tchetgen Tchetgen 回归经典二元 IV 模型，提出 NATE（Nudge ATT）概念，在单调性不成立时仍用 Wald 比率识别处理组平均效应，与 Kolesár 的工作形成对照——后者在多值 IV 下放弃单调性，转向反事实政策评估的偏识别方法。这四场共同推进了“在弱假设下如何用代理或工具变量恢复因果效应”这一核心问题。

**合成控制与实验设计**是另一条紧密主线。Abadie 将合成控制从观察性研究转向实验设计，提出如何选择处理单元与 donor 池以最小化基线不匹配，与 Imbens 的面板数据非参数识别形成互补——前者关注设计阶段，后者关注识别阶段。Zigler 的二分图干扰模型则从另一角度处理空间结构：电厂排放与居民健康之间的干扰由物理模型引入，而非假设已知，这与 Abadie 的“设计驱动”思路形成对比。Viviano 的遥感数据融合工作虽不直接涉及合成控制，但同样面临“结果变量不可直接观测”的困境，其数据融合策略（观测性数据 + 实验数据）与 Keith 的文本代理方法在逻辑上相通。

**因果表示学习与发现评估**构成第三主线。Young researchers 的综述聚焦多域干预数据下潜变量因果结构的可识别性，梳理了从非线性 ICA 到近期干预驱动方法的进展。Petersen 则从评估方法论切入，提出因果发现算法应区分“结构恢复”与“因果推断用途”两种视角，并建议用调整距离（AID）替代传统 SHD。Zhao 的 ADMG 基础理论为这些工作提供了图形语义支撑——他主张用非参数方程系统作为 ADMG 的默认解释，统一了统计模型与因果模型之间的歧义。

若想快速把握本季核心，建议从三条路径切入：**近端因果推断**可先看 Keith 和 Syrgkanis 打底，再读 Tchetgen Tchetgen 和 Kolesár 进阶；**合成控制与实验设计**以 Abadie 为主，辅以 Imbens 的面板识别；**因果表示学习**以 Young researchers 的综述为入口，再读 Petersen 的评估视角和 Zhao 的图形基础。Zigler 和 Viviano 适合对空间干扰或数据融合感兴趣的读者作为补充。

## 报告列表

### [Identification of nonparametric factor models for average treatment effects](../2025-03-25-ocis-2025-03-25-guido-imbens.md)
**讲者**: Guido Imbens · **讨论人**: Bryan Graham · 2025-03-25  
链接：[视频](https://youtu.be/6YuY-J3CXMI) · [幻灯片](https://drive.google.com/file/d/1p5kk32LOkCuCSqjutpZNDLD0LjlzL3oH/view?usp=drive_link)
<details><summary>摘要</summary>

There is a growing literature on methods for estimating causal effects in settings with panel or longitudinal data using two-way-fixed-effect, linear factor, and synthetic control methods. These methods attempt to adjust for unobserved differences between units as well as unobserved differences over time. Many of these methods partly rely on functional form assumptions to allow for such adjustments. Here we propose a set up that does not involve functional form assumptions. We show that by match…

</details>

### [Synthetic Controls for Experimental Design](../2025-03-18-ocis-2025-03-18-alberto-abadie.md)
**讲者**: Alberto Abadie · **讨论人**: Dmitry Arkhangelsky · 2025-03-18  
链接：[视频](https://youtu.be/FeS9a_USwqA) · [幻灯片](https://economics.mit.edu/sites/default/files/2023-12/Synthetic%20Controls%20for%20Experimental%20Design.pdf)
<details><summary>摘要</summary>

This article studies experimental design in settings where the experimental units are large aggregate entities (e.g., markets), and only one or a small number of units can be exposed to the treatment. In such settings, randomization of the treatment may result in treated and control groups with very different characteristics at baseline, inducing biases. We propose a variety of experimental non-randomized synthetic control designs (Abadie, Diamond and Hainmueller, 2010, Abadie and Gardeazabal, 2…

</details>

### [Proximal Causal Inference with Text Data](../2025-03-11-ocis-2025-03-11-katherine-a-keith.md)
**讲者**: Katherine A. Keith · **讨论人**: Naoki Egami · 2025-03-11  
链接：[视频](https://youtu.be/uWHBJ35n4_8) · [幻灯片](https://drive.google.com/file/d/1jW1zdszZz5EkJ1H0dzAPaMsjBp_4Ny-p/view?usp=drive_link)
<details><summary>摘要</summary>

Recent text-based causal methods attempt to mitigate confounding bias by estimating proxies of confounding variables that are partially or imperfectly measured from unstructured text data. These approaches, however, assume analysts have supervised labels of the confounders given text for a subset of instances, a constraint that is sometimes infeasible due to data privacy or annotation costs. In this work, we address settings in which an important confounding variable is completely unobserved. We…

</details>

### [Detecting clinician implicit biases in diagnoses using proximal causal inference](../2025-03-04-ocis-2025-03-04-vasilis-syrgkanis.md)
**讲者**: Vasilis Syrgkanis · **讨论人**: Ilya Shpitser · 2025-03-04  
链接：[视频](https://youtu.be/ThSwOyrK5dg) · [幻灯片](https://docs.google.com/presentation/d/1-VUGr9a5YbBJu2hBpU1pADUP9L3yD9k9/edit?usp=sharing&ouid=103522914004166230828&rtpof=true&sd=true) · [arXiv](https://arxiv.org/abs/2501.16399v1)
<details><summary>摘要</summary>

Clinical decisions to treat and diagnose patients are affected by implicit biases formed by racism, ableism, sexism, and other stereotypes. These biases reflect broader systemic discrimination in healthcare and risk marginalizing already disadvantaged groups. Existing methods for measuring implicit biases require controlled randomized testing and only capture individual attitudes rather than outcomes. However, the "big-data" revolution has led to the availability of large observational medical d…

</details>

### [Multi-Domain Causal Representation Learning](../2025-02-25-ocis-2025-02-25-young-researchers-seminar.md)
**讲者**: Young researchers' seminar · 2025-02-25  
链接：[视频](https://youtu.be/PAXimAZbkPM) · [幻灯片](https://proceedings.neurips.cc/paper_files/paper/2023/file/67089958e98b243d5cc1881ad60418b8-Paper-Conference.pdf) · [arXiv](https://arxiv.org/abs/2304.14545)
<details><summary>摘要</summary>

A key obstacle to more widespread use of causal models is requiring the relevant variables to be specified a priori. Yet, the causal relations of interest often do not occur at the level of raw observations such as pixels, but instead play out among abstract high-level latent concepts. Machine learning (ML) has proven successful at automatically extracting useful and compact representations of such complex data. Causal representation learning (CRL) aims to combine core strengths of ML and causal…

</details>

### [Revisiting Identification in the Binary Instrumental Variable Model: the NATE and Beyond](../2025-02-18-ocis-2025-02-18-eric-tchetgen-tchetgen.md)
**讲者**: Eric Tchetgen Tchetgen · 2025-02-18  
链接：[视频](https://youtu.be/-ltDXMH9ZPA) · [幻灯片](https://drive.google.com/file/d/16zYSKCLaLiPqR6cQO9PIf75u1t2_sErY/view?usp=drive_link) · [arXiv](https://arxiv.org/abs/2410.23590)
<details><summary>摘要</summary>

This talk revisits the identification problem in the canonical binary instrumental variable model. The work reveals new conditions for the classical Wald ratio estimand (WR) to be endowed with a nonparametric causal interpretation. Specifically, we describe a straightforward set of conditions under which the Wald Ratio point identifies the Nudge Average Treatment Effect (NATE), defined as the average causal effect for the subgroup of units whose treatment can be manipulated by the instrument, a …

</details>

### [Causal health impacts of power plant emission controls under modeled and uncertain physical process interference](../2025-02-11-ocis-2025-02-11-corwin-zigler.md)
**讲者**: Corwin Zigler · **讨论人**: Fredrik Sävje · 2025-02-11  
链接：[视频](https://youtu.be/Lj-oRwvspsY) · [幻灯片](https://drive.google.com/file/d/1SbJ76PTQ31v0Alr9uyuwKrzf7yLUeqFQ/view?usp=share_link)
<details><summary>摘要</summary>

Causal inference with spatial environmental data is often challenging due to the presence of interference: outcomes for observational units depend on some combination of local and nonlocal treatment. This is especially relevant when estimating the effect of power plant emissions controls on population health, as pollution exposure is dictated by: (i) the location of point-source emissions as well as (ii) the transport of pollutants across space via dynamic physical-chemical processes. In this wo…

</details>

### [Evaluating Counterfactual Policies Using Instruments](../2025-02-04-ocis-2025-02-04-michal-koles-r.md)
**讲者**: Michal Kolesár · **讨论人**: Edward Vytlacil · 2025-02-04  
链接：[视频](https://youtu.be/KUOpFA5QLhc) · [幻灯片](https://drive.google.com/file/d/1sEuvbxExTj8qEOyhACzIXlOvbRaQjJ-J/view?usp=sharing)
<details><summary>摘要</summary>

In settings with instrumental variables, the TSLS estimator is the most popular way of summarizing causal evidence. Yet in many settings, the instrument monotonicity assumption needed for its causal interpretation is refuted. A prominent example are designs using the (quasi-)random assignment of defendants to judges as an instrument for incarceration. But ultimately, we may not be interested in the TSLS estimand itself, but rather in the impact of some counterfactual policy intervention (e.g. an…

</details>

### [What are we discovering? Two perspectives on interpretable evaluation of causal discovery algorithms](../2025-01-28-ocis-2025-01-28-anne-helby-petersen.md)
**讲者**: Anne Helby Petersen · **讨论人**: Vanessa Didelez · 2025-01-28  
链接：[视频](https://youtu.be/KfqEZdQwz2M) · [幻灯片](https://drive.google.com/file/d/18QggMdJfRmj4mEY1EO7CYuylo4tpETzP/view?usp=share_link) · [arXiv](https://arxiv.org/abs/2412.10039)
<details><summary>摘要</summary>

Causal discovery algorithms aim to recover (parts) of causal data generating mechanism by analyzing empirical data they generated. Methodological research on causal discovery has been immensely productive, but a standard practice for evaluating performance has still not been established. It is therefore difficult to understand what algorithms may be most suited for what tasks, and what performance we can expect on real data. Evaluating performance of causal discovery algorithms can be divided in…

</details>

### [Program Evaluation with Remotely Sensed Outcomes](../2025-01-21-ocis-2025-01-21-davide-viviano.md)
**讲者**: Davide Viviano · **讨论人**: Hyunseung Kang · 2025-01-21  
链接：[视频](https://youtu.be/PUod1h8OywA) · [幻灯片](https://drive.google.com/file/d/1L5kIyczLmAgKD15MzUVSdgHVGnCBE0pi/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2411.10959)
<details><summary>摘要</summary>

While traditional program evaluations typically rely on surveys to measure outcomes, certain economic outcomes such as living standards or environmental quality may be infeasible or costly to collect. As a result, recent empirical work estimates treatment effects using remotely sensed variables (RSVs), such mobile phone activity or satellite images, instead of ground-truth outcome measurements. Common practice predicts the economic outcome from the RSV, using an auxiliary sample of labeled RSVs,…

</details>

### [On statistical and causal models associated with acyclic directed mixed graphs](../2025-01-14-ocis-2025-01-14-qingyuan-zhao.md)
**讲者**: Qingyuan Zhao · **讨论人**: Thomas Richardson · 2025-01-14  
链接：[视频](https://youtu.be/cjYEionaRGQ) · [幻灯片](https://drive.google.com/file/d/115xxL7Bb7LkNfKzWx3ukPYglnqLl7Z12/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2501.03048)
<details><summary>摘要</summary>

Causal models in statistics are often described using acyclic directed mixed graphs (ADMGs), which contain directed and bidirected edges and no directed cycles. This article surveys various interpretations of ADMGs, discusses their relations in different sub-classes of ADMGs, and argues that one of them -- nonparametric equation system (the E model below) -- should be used as the default interpretation. The E model is closely related to but different from the interpretation of ADMGs as directed …

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

