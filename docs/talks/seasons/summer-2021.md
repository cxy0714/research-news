# OCIS · Summer 2021

- 共 9 场 · 9 篇精读 · Online Causal Inference Seminar

## 本季导览

> 自动生成：归纳本季主线与值得先看的几场，**不打分、不排名**。

这一季的九场报告围绕三条主线展开：**因果鲁棒性与分布漂移**（Makar）、**面板数据与多干预因果推断**（Agarwal & Shen, Menchetti & Taeb）、以及**实验设计与选择性推断**（Volfovsky, Andrews, Pimentel, Wager, Imbens）。此外，Textor 的软件教程和 Imbens 的实验-观察数据融合分别提供了工具链和跨设计方法论的补充。

**因果鲁棒性与分布漂移**主线中，Makar 利用辅助标签和因果图建模，通过重要性加权和 MMD 惩罚消除虚假关联，直接对抗分布漂移下的 shortcut 学习。**面板数据与多干预推断**主线最为密集：Agarwal & Shen 的合成干预（SI）将合成控制法推广到多干预场景，利用低维潜因子结构补全 N×D 个因果参数；Menchetti & Taeb 的 C-ARIMA 则在时间序列中为单一持续性干预提供频率学派替代方案，明确写出潜在结果过程的 ARIMA 结构。**实验设计与选择性推断**主线覆盖了网络干扰下的配对随机化（Volfovsky）、赢家诅咒的条件推断（Andrews）、匹配设计中的多目标帕累托优化（Pimentel）、以及市场均衡下的全局干扰（Wager）。Imbens 的工作则横跨实验与观察数据，放弃代理条件独立性假设，用实验数据校正观察偏差。

若想快速切入，建议按以下路径：**面板数据与多干预**入口可先看 Agarwal & Shen（打底合成控制推广）和 Menchetti & Taeb（时间序列 ARIMA 框架）；**实验设计**入口可先看 Volfovsky（网络干扰配对设计）和 Andrews（选择性推断基础）；**因果鲁棒性**入口可先看 Makar（shortcut 消除的因果图方法）；**跨设计融合**入口可先看 Imbens（实验-观察数据校正）。Textor 的 DAGitty 教程适合作为工具补充，Pimentel 的匹配优化和 Wager 的市场均衡则属进阶内容。

## 报告列表

### [Talk #1: Causally motivated shortcut removal using auxiliary labels (Maggie Makar)](../2021-08-10-ocis-2021-08-10-maggie-makar.md)
**讲者**: Maggie Makar · 2021-08-10  
链接：[视频](https://youtu.be/R555VwMXSZ4) · [幻灯片](https://drive.google.com/file/d/1BB8vU6R_7eY2w16jg4bclOYkM3D-9DX7/view?usp=sharing) · [arXiv](http://arxiv.org/abs/2108.03849)
<details><summary>摘要</summary>

Robustness to certain forms of distribution shift is a key concern in many ML applications. Often, robustness can be formulated as enforcing invariances to particular interventions on the data generating process. Here, we study a flexible, causally-motivated approach to enforcing such invariances, paying special attention to shortcut learning, where a robust predictor can achieve optimal i.i.d generalization in principle, but instead it relies on spurious correlations or shortcuts in practice. O…

</details>

### [Synthetic Interventions](../2021-08-03-ocis-2021-08-03-anish-agarwal-and-dennis-shen.md)
**讲者**: Anish Agarwal and Dennis Shen · **讨论人**: Jason Poulos · 2021-08-03  
链接：[视频](https://youtu.be/e8nomN9hxZM) · [幻灯片](https://drive.google.com/file/d/1w8R6T1FlbYGFeYwo6cXuMjS-rzVeNdyx/view?usp=sharing) · [arXiv](https://arxiv.org/pdf/2006.07691.pdf)
<details><summary>摘要</summary>

Consider a setting where there are N heterogeneous units (e.g., individuals, sub-populations) and D interventions (e.g., socio-economic policies). Our goal is to learn the potential outcome associated with every intervention on every unit (i.e., N x D causal parameters). Towards this, we present a causal framework, synthetic interventions (SI), to infer these N x D causal parameters while only observing each of the N units under at most two interventions, independent of D. This can be significan…

</details>

### [Causal Inference using the R package DAGitty](../2021-07-27-ocis-2021-07-27-johannes-textor.md)
**讲者**: Johannes Textor · 2021-07-27  
链接：[视频](https://youtu.be/LCC4BkLZo-g) · [幻灯片](https://drive.google.com/file/d/122hfAj3t75vl5WlqxrFJ44K554x6xIB4/view?usp=sharing)
<details><summary>摘要</summary>

The R package "DAGitty" is a port of the online tool " dagitty.net " to the R platform for statistical computing. It provides access to graphical causal identification methods such as adjustment sets and instrumental variables, and has capabilities for simulating data from pre-specified graphical causal models. In this talk, I will explain the history and design principles behind the package, and show how it can be used in conjunction with other powerful packages such as ggdag, bnlearn, pcalg, a…

</details>

### [Talk 1: Estimating the causal effect of an intervention in a time series setting: the C-ARIMA approach (Fiammetta Menchetti)](../2021-07-20-ocis-2021-07-20-fiammetta-menchetti-armeen-taeb.md)
**讲者**: Fiammetta Menchetti ; Armeen Taeb · 2021-07-20  
链接：[视频](https://youtu.be/RjMEtv3C5S0) · [幻灯片](https://drive.google.com/file/d/1rI7kf9hsPyRcxxaLXHbJBUM0hJk6cJM9/view?usp=sharing)
<details><summary>摘要</summary>

The Rubin Causal Model (RCM) is a framework that allows to define the causal effect of an intervention as a contrast of potential outcomes. In recent years, several methods have been developed under the RCM to estimate causal effects in time series settings. None of these makes use of ARIMA models, which are instead very common in the econometrics literature. We propose a novel approach, C-ARIMA, to define and estimate the causal effect of an intervention in a time series setting under the RCM. …

</details>

### [Online experimentation for studying political polarization](../2021-07-13-ocis-2021-07-13-alexander-volfovsky.md)
**讲者**: Alexander Volfovsky · **讨论人**: Edo Airoldi · 2021-07-13  
链接：[视频](https://youtu.be/CoxmwebAsOw) · [幻灯片](https://drive.google.com/file/d/1PaT1yqjDA99-xZvL_dleL4gGoJcHnqQF/view?usp=sharing)
<details><summary>摘要</summary>

Social media sites are often blamed for exacerbating political polarization by creating “echo chambers” that prevent people from being exposed to information that contradicts their preexisting beliefs. We conducted a field experiment during which a large group of Democrats and Republicans followed bots that retweeted messages by elected officials and opinion leaders with opposing political views. Republican participants expressed substantially more conservative views after following a liberal Tw…

</details>

### [Inference on Winners](../2021-07-06-ocis-2021-07-06-isaiah-andrews.md)
**讲者**: Isaiah Andrews · **讨论人**: Will Fithian · 2021-07-06  
链接：[视频](https://youtu.be/Zs6FqGvRIuQ) · [幻灯片](https://scholar.harvard.edu/files/iandrews/files/inference_on_winners.pdf)
<details><summary>摘要</summary>

Many empirical questions concern target parameters selected through optimization. For example, researchers may be interested in the effectiveness of the best policy found in a randomized trial, or the best-performing investment strategy based on historical data. Such settings give rise to a winner’s curse, where conventional estimates are biased and conventional confidence intervals are unreliable. This paper develops optimal confidence intervals and median-unbiased estimators that are valid con…

</details>

### [Optimal tradeoffs in matched designs comparing US-trained and internationally-trained surgeons.](../2021-06-29-ocis-2021-06-29-sam-pimentel.md)
**讲者**: Sam Pimentel · **讨论人**: Magdalena Bennett · 2021-06-29  
链接：[视频](https://youtu.be/eCafnLGnYEM) · [幻灯片](https://www.stat.berkeley.edu/~spi/optimal_tradeoffs_unblinded.pdf)
<details><summary>摘要</summary>

Does receiving a medical education outside the United States impact a surgeon's performance? We study this question by matching operations performed by internationally-trained surgeons to those performed by US-trained surgeons in reanalysis of a large health outcomes study. An effective matched design must achieve several goals, including balancing covariate distributions marginally, ensuring units within individual pairs have similar values on key covariates, and using a sufficiently large samp…

</details>

### [Treatment Effects in Market Equilibrium (joint work with Evan Munro and Kuang Xu)](../2021-06-22-ocis-2021-06-22-stefan-wager.md)
**讲者**: Stefan Wager · **讨论人**: Fredrik Sävje · 2021-06-22  
链接：[视频](https://youtu.be/MW4Kmx9wYmw) · [幻灯片](https://drive.google.com/file/d/1KdMDPdMhVsREu0Sf6KorG6CaAMAXgiiC/view?usp=sharing)
<details><summary>摘要</summary>

In order to evaluate social and economic policy, it is important to measure policy effects within a market economy, where individuals interact by buying and selling various goods at the prevailing market price. In this setting, there is a direct policy effect on individual outcomes, and an indirect effect through resulting changes in equilibrium prices, which makes inference through standard randomized trials impossible. We define a stochastic general equilibrium model where interference occurs …

</details>

### [Using Experiments to Correct for Selection in Observational Studies](../2021-06-15-ocis-2021-06-15-guido-imbens.md)
**讲者**: Guido Imbens · **讨论人**: Nathan Kallus · 2021-06-15  
链接：[视频](https://youtu.be/5qs2UV_u2vw) · [幻灯片](https://drive.google.com/file/d/1e-72waq998DcFGFaV1sMDBDCy_lt7wz_/view?usp=sharing)
<details><summary>摘要</summary>

In the social sciences there has been an increase in interest in randomized experiments to estimate causal effects, partly because their internal validity tends to be high, but they are often small and contain information on only a few variables. At the same time, as part of the big data revolution, large, detailed, and representative, administrative data sets have become more widely available. However, the credibility of estimates of causal effects based on such data sets alone can be low. In t…

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

