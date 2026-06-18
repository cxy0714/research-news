# OCIS · Spring 2021

- 共 11 场 · 9 篇精读 · Online Causal Inference Seminar

## 本季导览

> 自动生成：归纳本季主线与值得先看的几场，**不打分、不排名**。

这一季的 11 场报告围绕三条主线展开：**分布偏移与不变性**（Bottou、Pfister、Magliacane）、**干扰与网络结构下的因果推断**（Johari、Zigler、Abadie）、以及**识别与估计的统计效率**（Nabi、Rotnitzky、Dahabreh、Berk、Stuart）。其中，分布偏移与不变性贯穿多场，从表示学习、假设检验到域适应，形成一条从方法到应用的完整链条；干扰问题则从双边平台实验、空气污染传输到合成控制，展示了不同场景下对干扰结构的建模与估计策略；统计效率主线聚焦于调整集选择、半参数效率界、以及时间序列设计中的偏差控制。

**分布偏移与不变性**是这一季最突出的主线。Bottou 的 IRM 从因果不变性出发，要求表示在所有环境中保持最优分类器一致，直接回应 OOD 泛化；Pfister 则转向假设检验，在已知似然比下将观测分布数据转化为对目标分布的检验，为迁移场景提供推断工具；Magliacane 的无监督域适应通过寻找分离集（P(Y|分离集)跨域不变），将因果图与 soft intervention 结合，与 Bottou 的 IRM 形成互补——前者要求表示不变，后者要求条件分布不变。这三场共同推进了“如何利用多环境数据实现跨分布泛化”这一核心问题。

**干扰与网络结构**是另一条密集主线。Johari 针对双边平台，放弃暴露模型，改用平均场极限刻画市场动态，直接估计全局处理效应（GTE），并指出传统个体随机化在资源竞争下的偏倚；Zigler 的二部图干扰结构（处理单元为电厂、结果单元为邮编区）依赖大气传输模型构建干扰网络，与 Johari 的“资源竞争”形成对比——干扰来源是物理过程而非市场交互；Abadie 的惩罚合成控制则处理多处理单元情境，通过稀疏权重和低插值偏差估计个体效应，与 Johari、Zigler 共享“干扰下效应估计”的关切，但方法上更接近经典合成控制。这三场展示了干扰问题在不同应用中的多样化建模策略。

**统计效率与识别**是第三主线。Nabi 在 ADMG 中系统推导半参数影响函数，给出不同估计量（IPW、AIPW、双稳健）依赖的条件密度集，并讨论 Verma 约束如何提升效率；Rotnitzky 在非参数图模型中比较不同调整集的渐近方差，给出最优选择准则，与 Nabi 的效率分析形成直接对话——前者关注调整集选择，后者关注估计量构造；Dahabreh 将多随机试验结果运输到目标总体，讨论识别条件与估计量，与 Rotnitzky 的调整集选择共享“如何从观测数据中提取无偏因果效应”的目标；Berk 和 Stuart 则聚焦时间序列设计：Berk 讨论 ITS 中模型选择后的推断不确定性，Stuart 用堆叠比较 ITS 处理交错实施的州级政策，两者都面对“单一或少量处理单元”的识别挑战，与 Abadie 的合成控制形成方法上的对照。

若想快速把握这一季的核心，建议按主题选择入口：**分布偏移与不变性**可先看 Bottou（IRM 奠基）和 Magliacane（域适应中的分离集），再读 Pfister（迁移检验）作为进阶；**干扰与网络结构**可先看 Johari（双边平台实验）和 Zigler（二部图干扰），再读 Abadie（多单元合成控制）作为方法对比；**统计效率与识别**可先看 Rotnitzky（调整集最优选择）和 Nabi（半参数效率界），再读 Dahabreh（运输推断）作为应用延伸；**时间序列设计**可先看 Berk（ITS 模型选择问题）和 Stuart（堆叠 ITS 处理交错政策），与 Abadie 的合成控制对照理解。

## 报告列表

### [Learning Representations Using Causal Invariance](../2021-06-08-ocis-2021-06-08-leon-bottou.md)
**讲者**: Leon Bottou · **讨论人**: Dominik Rothenhäusler · 2021-06-08  
链接：[视频](https://youtu.be/Rewr4GmkYEk)
<details><summary>摘要</summary>

Learning algorithms often capture spurious correlations present in the training data distribution instead of addressing the task of interest. Such spurious correlations occur because the data collection process is subject to uncontrolled confounding biases. Suppose however that we have access to a few distinct datasets exemplifying the same concept but whose distributions exhibit different biases. Can we learn something that is common across all these distributions, while ignoring the spurious w…

</details>

### [Statistical Testing under Distributional Shifts](../2021-06-01-ocis-2021-06-01-niklas-pfister.md)
**讲者**: Niklas Pfister · **讨论人**: Thomas Berrett · 2021-06-01  
链接：[视频](https://youtu.be/ZrIivZDygmo) · [幻灯片](https://drive.google.com/file/d/17VKr_I2OqewBk2W6b1Gn4dHV_QcgPrOs/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2105.10821)
<details><summary>摘要</summary>

Statistical hypothesis testing is a central problem in empirical inference. Observing data from a distribution P, one is interested in testing whether P lies in a given null hypothesis while controlling the probability of false rejections. In this talk, we will introduce a framework for statistical testing under distributional shifts. Our goal will be to test a target hypothesis P in H0 using observed data from a distribution Q, where we assume that P is related to Q through a known distribution…

</details>

### [Semiparametric inference for causal effects in graphical models with hidden variables](../2021-05-25-ocis-2021-05-25-razieh-nabi.md)
**讲者**: Razieh Nabi · **讨论人**: Eric Tchetgen Tchetgen · 2021-05-25  
链接：[视频](https://youtu.be/hNOXL4qHP8c) · [幻灯片](https://drive.google.com/file/d/11mp9BrtXUvX1p9ljA4Dm_PdWAbdOuVh-/view?usp=sharing)
<details><summary>摘要</summary>

There exist sound and complete algorithms for identifying causal effects in causal graphical models with unmeasured confounders. However, these algorithms remain underused due to the complexity of estimating the identifying functionals that they output. In this work, we bridge the gap between identification and estimation of population-level causal effects involving a single treatment and a single outcome. The majority of the talk focuses on semiparametric estimation of effects that are identifi…

</details>

### [Experimental design in two-sided platforms: an analysis of bias](../2021-05-18-ocis-2021-05-18-ramesh-johari.md)
**讲者**: Ramesh Johari · **讨论人**: Panos Toulis · 2021-05-18  
链接：[视频](https://youtu.be/NDWuhbHtzMI) · [幻灯片](https://drive.google.com/file/d/1oVJMLNJOIujfRI4phnBQJbZ_mk4ydNVL/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2002.05670)
<details><summary>摘要</summary>

We develop an analytical framework to study experimental design in two-sided marketplaces. Many of these experiments exhibit interference, where an intervention applied to one market participant influences the behavior of another participant. This interference leads to biased estimates of the treatment effect of the intervention. We develop a stochastic market model and associated mean field limit to capture dynamics in such experiments, and use our model to investigate how the performance of di…

</details>

### [Bipartite inference and air pollution transport: estimating health effects of power plant interventions](../2021-05-11-ocis-2021-05-11-corwin-zigler.md)
**讲者**: Corwin Zigler · **讨论人**: Forrest Crawford · 2021-05-11  
链接：[视频](https://youtu.be/PiiWu-YtIXs) · [幻灯片](https://drive.google.com/file/d/1VAK3oqJz4L_ROOGDn07hU22Jsinhi7rP/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2012.04831)
<details><summary>摘要</summary>

Evaluating air quality interventions is confronted with the challenge of interference since interventions at a particular pollution source likely impact air quality and health at distant locations and air quality and health at any given location are likely impacted by interventions at many sources. The structure of interference in this context is dictated by complex atmospheric processes governing how pollution emitted from a particular source is transformed and transported across space, and can…

</details>

### [Domain adaptation by using causal inference to predict invariant conditional distributions](../2021-05-04-ocis-2021-05-04-sara-magliacane.md)
**讲者**: Sara Magliacane · **讨论人**: Dominik Rothenhäusler · 2021-05-04  
链接：[视频](https://youtu.be/z748Lf4QTlE) · [幻灯片](https://drive.google.com/file/d/1UHU9qZGCyZNQmQ_sGqjk53Il9w9PhZNx/view?usp=sharing) · [arXiv](https://arxiv.org/abs/1707.06422)
<details><summary>摘要</summary>

An important goal common to domain adaptation and causal inference is to make accurate predictions when the distributions for the source (or training) domain(s) and target (or test) domain(s) differ. In many cases, these different distributions can be modeled as different contexts of a single underlying system, in which each distribution corresponds to a different perturbation of the system, or in causal terms, an intervention. We focus on a class of such causal domain adaptation problems, where…

</details>

### Causally interpretable meta-analysis: transporting inferences from multiple randomized trials to a target population　*（暂无精读）*
**讲者**: Issa Dahabreh · **讨论人**: Eloise Kaizar · 2021-04-27  
链接：[幻灯片](https://drive.google.com/file/d/1p2kCGfKpZR2Ac3v-Cscr-mMd9qSre6Wq/view?usp=sharing)
<details><summary>摘要</summary>

We present methods for causally interpretable meta-analyses that combine information from multiple randomized trials to estimate potential (counterfactual) outcome means and average treatment effects in a target population. We consider identifiability conditions, derive implications of the conditions for the law of the observed data, and obtain identification results for transporting causal inferences from a collection of independent randomized trials to a new target population in which experime…

</details>

### [A Penalized Synthetic Control Estimator for Disaggregated Data](../2021-04-20-ocis-2021-04-20-alberto-abadie.md)
**讲者**: Alberto Abadie · **讨论人**: Stefan Wager · 2021-04-20  
链接：[视频](https://youtu.be/I7AVRmadkU4) · [幻灯片](https://drive.google.com/file/d/1tzOYj7kO-_DxPGjQyl62SQuPODW9AOWg/view?usp=sharing)
<details><summary>摘要</summary>

Synthetic control methods are commonly applied in empirical research to estimate the effects of treatments or interventions on aggregate outcomes. A synthetic control estimator compares the outcome of a treated unit to the outcome of a weighted average of untreated units that best resembles the characteristics of the treated unit before the intervention. When disaggregated data are available, constructing separate synthetic controls for each treated unit may help avoid interpolation biases. Howe…

</details>

### [Optimal adjustment sets in non-parametric graphical models](../2021-04-13-ocis-2021-04-13-andrea-rotnitzky.md)
**讲者**: Andrea Rotnitzky · **讨论人**: Ema Perkovi c · 2021-04-13  
链接：[视频](https://youtu.be/VBfMhMaIE-8) · [幻灯片](https://drive.google.com/file/d/1WDfsU2dyaVrodyYi91nljBiwQogd1uAZ/view?usp=sharing)
<details><summary>摘要</summary>

We consider the selection of potential confounding variables at the stage of the design of a planned observational study. Given a tentative non-parametric graphical causal model, possibly including unobservable variables, the aim is to select the set of observable covariates that both suffices to control for confounding under the model and yields a non-parametric estimator of the causal contrast of interest with smallest variance. For studies without unobservables aimed at assessing the effect o…

</details>

### [Firearm Sales in California Through the Myopic Vision of an Interrupted Time Series Causal Analysis Discus sant: John Donohue (Stanford)](../2021-04-06-ocis-2021-04-06-richard-berk.md)
**讲者**: Richard Berk · 2021-04-06  
链接：[视频](https://youtu.be/5TS9M3fXgjE) · [幻灯片](https://drive.google.com/file/d/1Ah59Po0F5lhTXoqLhBE4pl9y5z0hLB9M/view?usp=sharing)
<details><summary>摘要</summary>

There have been many claims in the media and a bit respectable research about the causes of variation in firearm sales. The challenges for causal inference can be quite daunting. In this talk, I report on an analysis of daily firearm sales in California from 1996 through most of 2018 using an interrupted time series design and analysis. The design was introduced to social scientists in 1963 by Campbell and Stanley, analysis methods were proposed by Box and Tiao in 1975, and more recent treatment…

</details>

### Using stacked comparative interrupted time series to estimate opioid policy effects　*（暂无精读）*
**讲者**: Elizabeth Stuart · **讨论人**: Laura Hatfield · 2021-03-30  
链接：[幻灯片](https://drive.google.com/file/d/1q2StsuqQ9pqX7-Saq67PNS8Z9smOd288/view?usp=sharing)
<details><summary>摘要</summary>

Many opioid policies are being implemented at the state level; as one example, 37 states have passed laws limiting the dose and/or duration of opioid prescriptions. However, studying state policy effects can be challenging, especially when states that do and don’t implement the policies differ from one another, and when states implement laws across time (staggered implementation); recent work has shown that standard “two way fixed effects” analysis approaches can lead to substantial bias, and th…

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

