# OCIS · Spring 2026

- 共 10 场 · 6 篇精读 · Online Causal Inference Seminar

## 本季导览

> 自动生成：归纳本季主线与值得先看的几场，**不打分、不排名**。

OCIS Spring 2026 的十场报告可归纳为三条主线。第一条是**实验设计与推断**，涵盖自适应实验（Suhas Vijaykumar）、阶梯楔形设计（Fan Xia）以及带安全性约束的策略学习（Naoki Egami）。第二条是**半参数效率与稳健推断**，包括慢速干扰参数下的因果估计（Matteo Bonvini）、分布性平衡加权（Chan Park）以及半参数因果对比模型（Fan Xia 的工作也与此交叉）。第三条是**因果推断的形式化与表示学习**，包括因果表示学习的有限样本问题（Bryon Aragam）、因果推断的逻辑基础（Thomas Icard）以及非结构化数据中的因果推断（Yixin Wang）。James Robins 的公开讲座作为回顾性综述，贯穿所有主线。INI 的联合网络研讨会内容未提供，暂不纳入。

在半参数效率与稳健推断这条主线上，本季有多个互补的推进。Matteo Bonvini 关注当干扰参数（如倾向得分、结果回归）以慢于根号 n 的速率收敛时，如何仍能构造根号 n 一致且渐近正态的因果估计量——这直接回应了高维或非参数机器学习中“二阶余项不消失”的困境。Chan Park 则从加权角度出发，用特征函数距离直接匹配处理组与对照组的全协变量分布，而非仅匹配有限矩，从而在理论上保证加权估计的一致性不依赖于结果回归的稀疏近似。Fan Xia 在阶梯楔形设计中提出的半参数因果对比模型，将干预效果参数化而将控制集群-周期均值完全非参数化，利用设计概率实现根号 n 一致且渐近正态的推断，同时避免了对时间趋势的完整参数建模——这是对传统线性混合模型在 SWD 中模型依赖性的直接回应。这三场共同展示了“在弱假设下仍保持效率与稳健性”这一核心关切的不同技术路径：Bonvini 依赖高阶影响函数与交叉拟合，Park 依赖分布性平衡的优化对偶，Xia 依赖设计基的投影与半参数正交性。

在实验设计与推断这条主线上，Suhas Vijaykumar 提出了“演示实验”的形式化框架——目标不是精确估计处理效应，而是检验是否存在至少一个干预对某个子群或某个结局有正向效果，这对应阈值多臂老虎机中的全局零假设检验。Naoki Egami 则将策略学习与保形预测结合，在 AI 干预的背景下，要求学出的策略对每个新个体都提供分布自由的个体级安全性保证（如控制有害干预的概率）。这两场都涉及“在自适应或个性化分配中做推断”，但前者聚焦于多重比较与停止规则，后者聚焦于个体化保证与有限样本有效性。

若想快速把握本季的技术核心，建议按以下路径观看。**入口一：半参数效率与稳健推断**——先看 Matteo Bonvini 和 Chan Park，前者给出慢速干扰参数下的通用框架，后者展示分布性平衡的加权新视角；进阶可看 Fan Xia，了解如何将半参数正交性应用于阶梯楔形设计这一具体结构。**入口二：实验设计与自适应推断**——先看 Suhas Vijaykumar 的演示实验框架，再看 Naoki Egami 的保形策略学习，两者在“分配与推断的交互”上形成对照。**入口三：因果推断的形式化与表示学习**——先看 Thomas Icard 的逻辑框架（为所有因果识别问题提供统一句法），再看 Bryon Aragam 的有限样本挑战（指出当前 CRL 可识别性结果与统计推断之间的鸿沟），最后看 Yixin Wang 的非结构化数据因果推断（将上述形式化与表示学习推向实际数据场景）。James Robins 的公开讲座适合作为所有主线的背景综述，可在任意阶段观看。

## 报告列表

### Causal inference with unstructured data　*（暂无精读）*
**讲者**: Yixin Wang · 2026-06-09  
<details><summary>摘要</summary>

Causal inference traditionally relies on tabular data, where treatments, outcomes, and covariates are manually collected and labeled. However, many real-world problems involve unstructured data (e.g., images, text, and videos) where treatments or outcomes are high-dimensional and unstructured, or all causal variables are hidden within the unstructured observations. This talk explores causal inference in such settings. We begin with cases where all causal variables (including treatments, outcomes…

</details>

### [Demonstration Experiments](../2026-06-02-ocis-2026-06-02-suhas-vijaykumar.md)
**讲者**: Suhas Vijaykumar · **讨论人**: Aurélien Bibaut · 2026-06-02  
链接：[视频](https://youtu.be/iEd5f1jARBk) · [幻灯片](https://drive.google.com/file/d/1Nij0j0A_3hP_Sjs8gW2Da7lFr1qFyQl8/view?usp=sharing) · [arXiv](https://arxiv.org/pdf/2603.06941)
<details><summary>摘要</summary>

Adaptive experiments are used extensively in online platforms, healthcare and biotechnology, and the social sciences. Often, the primary goal is not to precisely estimate a treatment effect but to demonstrate that at least one candidate intervention yields a positive effect, for some subpopulation and on some measured outcome. We formalize this objective as testing the global null in a threshold bandit framework, and develop two inference procedures that are valid under general adaptive sampling…

</details>

### Rothschild Public Lecture | Forty years of causal inference: Report of a great-grandfather　*（暂无精读）*
**讲者**: James Robins · 2026-05-26  
<details><summary>摘要</summary>

F orty years ago, the following disciplines had their own languages, opinions and idiosyncrasies re causal inference: philosophy, computer science, sociology, psychology, statistics, epidemiology, political science, and economics. Today all speak a common language. Top journals have gone from knee-jerk rejection to active solicitation of articles on causal inference. The ongoing rapid development of the field has been driven by: 1. End of the historical suppression of causal language in statisti…

</details>

### [Conformal Policy Learning with Distribution-Free Safety Guarantees: Application to AI-Powered Interventions](../2026-05-19-ocis-2026-05-19-naoki-egami.md)
**讲者**: Naoki Egami · **讨论人**: Eli Ben-Michael · 2026-05-19  
链接：[视频](https://youtu.be/Tdf05OYHVUU) · [幻灯片](https://drive.google.com/file/d/1FIQFPIBjFCG9jPLNqqBtFqCgZnOjS4Gd/view?usp=share_link)
<details><summary>摘要</summary>

Generative AI is emerging as a new class of intervention in the social sciences, with applications designed to change attitudes and behaviors through scalable, personalized interactions. For example, conversational agents have been used to reduce political polarization and improve workplace productivity. At the same time, recent empirical studies highlight an important risk: while such interventions may benefit many individuals and tasks, they may also harm others. How, then, can AI intervention…

</details>

### [Robust and Efficient Semiparametric Inference for the Stepped Wedge Design](../2026-05-12-ocis-2026-05-12-fan-xia.md)
**讲者**: Fan Xia · 2026-05-12  
链接：[视频](https://youtu.be/L8ih_a5bHws)
<details><summary>摘要</summary>

Stepped wedge designs (SWDs) are increasingly used to evaluate longitudinal cluster-level interventions but pose substantial challenges for valid inference. Because crossover times are randomized, intervention effects are intrinsically confounded with secular time trends, while heterogeneity across clusters, complex correlation structures, baseline covariate imbalances, and small numbers of clusters further complicate inference. We propose a unified semiparametric framework for estimating possib…

</details>

### [Distributional Balancing for Causal Inference: A Unified Framework via Characteristic Function Distance](../2026-05-05-ocis-2026-05-05-chan-park.md)
**讲者**: Chan Park · 2026-05-05  
链接：[视频](https://youtu.be/sUlOJmdwUY8) · [幻灯片](https://drive.google.com/file/d/1--U-3hfAEns9ryki7Vf645H5Qr55-mUW/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2601.15449)
<details><summary>摘要</summary>

Weighting methods are essential tools for estimating causal effects in observational studies, with the goal of balancing pre-treatment covariates across treatment groups. Traditional approaches pursue this objective indirectly, for example, via inverse propensity score weighting or by matching a finite number of covariate moments, and therefore do not guarantee balance of the full joint covariate distributions. Recently, distributional balancing methods have emerged as robust, nonparametric alte…

</details>

### [Beyond identifiability in causal representation learning](../2026-04-28-ocis-2026-04-28-bryon-aragam.md)
**讲者**: Bryon Aragam · 2026-04-28  
链接：[视频](https://youtu.be/Xj2h0Z1qwms)
<details><summary>摘要</summary>

Causal reasoning has long been recognized as a crucial skill needed to build intelligent systems. Whether or not current systems possess this skill is the subject of much debate: Recent years have witnessed a flurry of activity with both positive and negative results on this topic from both theoretical and empirical perspectives. This talk will highlight the challenges intrinsic to this endeavour, focusing on the difficulties in translating existing causal identifiability results into practical,…

</details>

### joint webinar　*（暂无精读）*
**讲者**: INI · 2026-04-21  

### Causal Estimation and Inference under Slow Nuisance Rates　*（暂无精读）*
**讲者**: Matteo Bonvini · **讨论人**: Lars van der Laan · 2026-04-14  
链接：[幻灯片](https://drive.google.com/file/d/1ed5AwCJC5dH23m_PcSRMBp_Oxo8tCnsg/view?usp=share_link) · [arXiv](https://arxiv.org/abs/2405.08525)
<details><summary>摘要</summary>

Estimators of causal functionals based on first-order influence functions have been extremely successful in modern causal inference. Grounded in semiparametric efficiency theory, their estimation error depends on nuisance functions only through a second-order remainder term, enabling the use of flexible machine learning methods. Inference is typically justified by assuming that this remainder is asymptotically negligible. However, in high-dimensional or low-smoothness settings, nuisance estimato…

</details>

### [Causal Inference as a Logical Problem](../2026-04-07-ocis-2026-04-07-thomas-icard.md)
**讲者**: Thomas Icard · **讨论人**: Jiji Zhang · 2026-04-07  
链接：[视频](https://youtu.be/bHXGL9UlevA) · [幻灯片](https://drive.google.com/file/d/1x_RuY_8YSnVbrT_xVUaR1IbubwdkuTiR/view?usp=sharing)
<details><summary>摘要</summary>

The goal of this talk will be to show how problems of causal inference can be usefully and precisely understood as logical problems. Adapting tools and concepts from mathematical and computational logic affords new perspectives, raises new questions, and sheds light on some practical and theoretical issues in causal inference. We illustrate with several examples, including some ways in which a logical lens can help clarify the empirical status of assumptions sufficient to bridge gaps between lim…

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

