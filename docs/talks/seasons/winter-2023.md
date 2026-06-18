# OCIS · Winter 2023

- 共 10 场 · 8 篇精读 · Online Causal Inference Seminar

## 本季导览

> 自动生成：归纳本季主线与值得先看的几场，**不打分、不排名**。

这一季 OCIS Winter 2023 的 10 场报告可归纳为四条主线：**因果建模与参数化**（Robin Evans、Stijn Vansteelandt）、**因果推断中的偏倚与敏感性分析**（Ingeborg Waernbaum、Lauren Dang、Jessica Young）、**干扰与实验设计**（Christina Yu）、以及**因果推断在社会与算法问题中的应用**（Issa Kohler-Hausmann & Lily Hu 两场、Moritz Hardt、Ilya Shpitser）。其中，后两条主线（干扰与实验设计、社会应用）各只有一场，但前两条主线内部有紧密的方法论对话。

**因果建模与参数化**是这一季最突出的主线。Robin Evans 的“节俭参数化”直接回应了边际结构模型（MSM）的“似然缺失”问题：通过构造一个与目标因果参数变差独立的联合分布参数化，使得 MLE 和贝叶斯推断成为可能，并绕开 g-null paradox。Stijn Vansteelandt 的“假设精简因果建模”则从另一角度切入：保留回归模型的简洁性，但将目标参数重新定义为模型无关的可解释量（如加权平均的层特异性效果），从而在模型错误时仍能明确知道估计量在估计什么。两场都试图在“完全非参”与“强参数假设”之间找到实用折中，但 Evans 更侧重参数化与模拟，Vansteelandt 更侧重推断与沟通。

**偏倚与敏感性分析**是另一条密集主线。Ingeborg Waernbaum 聚焦选择偏倚，将 Smith & VanderWeele 的界限法推广到多重纳排标准，并给出可操作的敏感性参数。Lauren Dang 处理 RCT 与观测数据的整合，提出一个“偏倚感知”的估计量，用数据本身判断是否借用外部信息。Jessica Young 则从竞争风险切入，指出传统统计量（如 subdistribution hazard ratio）可能对应有问题的因果目标，并建议用反事实语言先定义清楚再估计。三场都涉及“当标准假设不成立时，如何量化或控制偏倚”，但 Waernbaum 和 Dang 更偏重操作化工具，Young 更偏重概念澄清。

**社会与算法应用**的两场（Issa Kohler-Hausmann & Lily Hu）和 Ilya Shpitser 的报告都涉及因果推断在公平性中的使用，但切入角度不同。Kohler-Hausmann & Hu 的两场分别质疑“控制下游中介”的因果量是否定义得当，以及审计研究中“种族因果效应”的隔离是否可能——它们更多是概念批判，而非提出新方法。Shpitser 则正面提出路径特定因果公平性，用因果图上的“好/坏”路径划分来定义不公平，并给出算法。Moritz Hardt 的报告虽不直接属于公平性，但同样关注预测的因果效应，提出“performative power”框架来测量数字平台的市场力量，与 Kohler-Hausmann & Hu 的批判性视角形成互补。

若想快速把握这一季的方法论核心，建议先看 **Robin Evans** 和 **Stijn Vansteelandt** 打底，理解因果建模中参数化与推断的张力；接着看 **Ingeborg Waernbaum** 和 **Lauren Dang** 了解偏倚控制的操作化进展。若对概念批判感兴趣，可先看 **Issa Kohler-Hausmann & Lily Hu** 的两场；若对算法公平性感兴趣，则从 **Ilya Shpitser** 入手。**Christina Yu** 和 **Moritz Hardt** 分别代表干扰实验设计与预测因果效应两个独立方向，可按需选看。

## 报告列表

### [Parameterizing and Simulating from Causal Models](../2023-03-28-ocis-2023-03-28-robin-evans.md)
**讲者**: Robin Evans · **讨论人**: Larry Wasserman · 2023-03-28  
链接：[视频](https://youtu.be/Ez861340pp4) · [幻灯片](https://drive.google.com/file/d/1OO197i1_eOE9kxXjn8tJgpS4ngpazDFR/view?usp=share_link)
<details><summary>摘要</summary>

Many statistical problems in causal inference involve a probability distribution other than the one from which data are actually observed; as an additional complication, the object of interest is often a marginal quantity of this other probability distribution. This creates many practical complications for statistical inference, even where the problem is non-parametrically identified. In particular, it is difficult to perform likelihood-based inference, or even to simulate from the model in a ge…

</details>

### [Causal inference with competing events](../2023-03-21-ocis-2023-03-21-jessica-young.md)
**讲者**: Jessica Young · **讨论人**: Jacqueline Rudolph , Q&A moderator: Mats Stensrud · 2023-03-21  
链接：[视频](https://youtu.be/vgNznhe4ofQ) · [幻灯片](https://drive.google.com/file/d/1SqwXejTPzlVes5FSa-z9r-4pDb_kL0-N/view?usp=share_link)
<details><summary>摘要</summary>

A competing (risk) event is any event that makes it impossible for the event of interest in a study to occur. For example, cardiovascular disease death is a competing event for prostate cancer death because an individual cannot die of prostate cancer once he has died of cardiovascular disease. Various statistical estimands have been posed in the classical competing risks literature, most prominently the cause-specific cumulative incidence, the marginal cumulative incidence, the cause-specific ha…

</details>

### [Exploiting Neighborhood Interference with Low Order Interactions under Unit Randomized Design](../2023-02-28-ocis-2023-02-28-christina-yu.md)
**讲者**: Christina Yu · **讨论人**: Chencheng Cai - Q&A moderator: Mayleen Cortez and Matt Eichhorn · 2023-02-28  
链接：[视频](https://youtu.be/pskRH11mADI) · [幻灯片](https://drive.google.com/file/d/1gtePOA1lwd2xbm1o0gElbWWSA3TYvew5/view?usp=share_link)
<details><summary>摘要</summary>

Network interference, where the outcome of an individual is affected by the treatment assignment of those in their social network, is pervasive in many real-world settings. However, it poses a challenge to estimating causal effects. We consider the task of estimating the total treatment effect (TTE), or the difference between the average outcomes of the population when everyone is treated versus when no one is, under network interference. Under a Bernoulli randomized design, we utilize knowledge…

</details>

### [Selection bias and multiple inclusion criteria in observational studies](../2023-02-21-ocis-2023-02-21-ingeborg-waernbaum.md)
**讲者**: Ingeborg Waernbaum · **讨论人**: Maya Mathur , Q&A moderator: Stina Zetterström · 2023-02-21  
链接：[视频](https://youtu.be/u_TmBqJjEiA) · [幻灯片](https://drive.google.com/file/d/1bzK4X5GOsZpFmDHSw6F1NvQQxjud6FUi/view?usp=share_link)
<details><summary>摘要</summary>

Selection bias can be a result of applying inclusion/exclusion criteria when selecting the study population in an observational study. The bias can threaten the validity of the study and sensitivity analysis for assessing the effect of the selection is desired. Bounds for selection bias based on values of sensitivity parameters were previously proposed by Smith and VanderWeele (SV). The sensitivity parameters describe aspects of the joint distribution of the outcome, selection and a vector of un…

</details>

### [Assumption-lean Causal Modeling](../2023-02-14-ocis-2023-02-14-stijn-vansteelandt.md)
**讲者**: Stijn Vansteelandt · **讨论人**: Elizabeth Ogburn · 2023-02-14  
链接：[视频](https://youtu.be/DkyNCJLWqUg) · [幻灯片](https://drive.google.com/file/d/1ZUmcWx0dNDGtNsEA7bvEuxjZLHKzYz9e/view?usp=share_link)
<details><summary>摘要</summary>

Causal inference research has shifted from being primarily descriptive (describing the data-generating mechanism using statistical models) to being primarily prescriptive (evaluating the effects of specific interventions). The focus has thereby moved from being centered on statistical models to being centered on causal estimands. This evolution has been driven by the increasing need for practical solutions to real-world problems, such as designing effective interventions, making policy decisions…

</details>

### [Integration of Observational and Randomized Controlled Trial Data: Approaches, Challenges, A Novel Estimator, and Application to the LEADER Cardiovascular Outcomes Trial](../2023-02-07-ocis-2023-02-07-lauren-dang.md)
**讲者**: Lauren Dang · **讨论人**: Robin Evans · 2023-02-07  
链接：[视频](https://youtu.be/KilwkNczs0U) · [幻灯片](https://docs.google.com/presentation/d/1cNp6fIUhK0-JjMvDU4iKI0lshc14qkBTE48Bu47Yefo/edit?usp=sharing) · [arXiv](https://arxiv.org/abs/2210.05802)
<details><summary>摘要</summary>

Although the randomized controlled trial (RCT) is the gold standard for evidence generation, conducting an adequately powered RCT is not always feasible or desirable. A traditional RCT may be impracticable for very rare diseases, and excessive randomization to control may be considered unethical for severe diseases without effective treatments or for certain pediatric drug approvals. In such cases, we may wish to integrate data from a small RCT with real-world data (RWD) to increase power but at…

</details>

### Causal mediators and misdefined causal quantities　*（暂无精读）*
**讲者**: Issa Kohler-Hausmann, Lily Hu · 2023-01-31  
<details><summary>摘要</summary>

A number of influential causal inference researchers have asked the following question: Can we quantify an effect of race on a decision that takes place downstream of other decisions that were themselves causally affected by race? If so, how? In this talk, we ask if causal quantities that attempt to “hold constant” or intervene on downstream mediators are misdefined . We explore this question by asking whether causal inference is—for lack of a more precise word—“messed up” when we fail to take a…

</details>

### What is the causal effect an effect of in audit/correspondence studies?　*（暂无精读）*
**讲者**: Issa Kohler-Hausmann, Lily Hu · 2023-01-24  
<details><summary>摘要</summary>

Many researchers have expressed an interest in isolating and measuring the causal effect that social statues such as race or gender has on decision outcomes in various domains. In such endeavors, the effort to “isolate” (e.g.) race means disentangling the causal effect of just race on the decision of interest from the causal effect of so-called non-race factors on the decision. For example, researchers have described the quantity of interest in general terms, saying that they seek to measure the…

</details>

### [From prediction to power](../2023-01-17-ocis-2023-01-17-moritz-hardt-max-planck-institute-for-in.md)
**讲者**: Moritz Hardt, Max Planck Institute for Intelligent Systems) · **讨论人**: Michael P. Kim · 2023-01-17  
链接：[视频](https://youtu.be/dShLLhc48yw) · [幻灯片](https://docs.google.com/presentation/d/1478yiG_0OWEa_9HxWpvJlhy1gvd7wCvm5UI3AMorVkM/edit?usp=sharing)
<details><summary>摘要</summary>

A recent formal framework, called performative prediction, draws attention to the fundamental difference between learning from a population and steering a population through predictions. Against this backdrop, we'll examine the role of prediction in questions of power in digital markets. Building on performative prediction, I'll introduce the notion of performative power that measures the ability of a firm operating an algorithmic system to benefit from steering. Traditional economic tools strug…

</details>

### [Fairness By Causal Mediation Analysis: Criteria, Algorithms, and Open Problems](../2023-01-10-ocis-2023-01-10-ilya-shpitser.md)
**讲者**: Ilya Shpitser · **讨论人**: Ricardo Silva · 2023-01-10  
链接：[视频](https://youtu.be/6Yn4efwBIGQ) · [幻灯片](https://drive.google.com/file/d/1mE7W-NWtIQH-HfpkvSFMdWn4LeZnVb4R/view?usp=share_link)
<details><summary>摘要</summary>

Systematic discriminatory biases present in our society influence the way data is collected and stored, the way variables are defined, and the way scientific findings are put into practice as policy. Automated decision procedures and learning algorithms applied to such data may serve to perpetuate existing injustice or unfairness in our society. We consider how to solve prediction and policy learning problems in a way which ``breaks the cycle of injustice'' by correcting for the unfair dependenc…

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

