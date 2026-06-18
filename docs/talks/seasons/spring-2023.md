# OCIS · Spring 2023

- 共 7 场 · 6 篇精读 · Online Causal Inference Seminar

## 本季导览

> 自动生成：归纳本季主线与值得先看的几场，**不打分、不排名**。

OCIS Spring 2023 的七场报告可归纳为三条主线：**高维与半参数因果推断**（Yuhao Wang、Philipp Bach & Sven Klaassen）、**图模型与结构方程的形式化约束**（M. van Ommen、Niels Richard Hansen）、以及**因果推断的基础与敏感性分析**（Matthew Gentzkow、Interview with Philip Dawid、Student talks）。其中，DoubleML 教程与 Yuhao Wang 的报告共享对 DML 框架的依赖，但分别侧重软件实现与稀疏性理论；van Ommen 与 Hansen 的报告则从不同角度（线性代数约束 vs. 循环动态系统）拓展了图模型的可识别性理论。

**高维与半参数因果推断**是这一季最密集的主线。Yuhao Wang 的报告推进了 **DIPW** 方案，在倾向得分稀疏但结果回归可能非稀疏时，仍能实现 \(\sqrt{n}\)-一致估计，其核心是构造 Neyman 正交得分并利用交叉拟合，与 DML 框架（Chernozhukov et al. 2018）一脉相承。Philipp Bach & Sven Klaassen 的教程则系统展示了 **DoubleML** 软件如何将 DML 的三大要素（正交性、交叉拟合、ML 集成）封装为统一接口，支持 PLR、IRM、PLIV 等模型，并处理聚类标准误与异质性效应。两场报告共同指向一个核心问题：如何在高维或非参数 nuisance 函数下，用正交化与交叉拟合消除正则化偏差。

**图模型与结构方程的形式化约束**这一主线包含两场理论报告。M. van Ommen 聚焦于 **线性结构方程模型（LSEM）** 中超越条件独立性的多项式约束（如消退 tetrads），并探讨如何用这些约束刻画模型等价类或用于因果发现。Niels Richard Hansen 则处理 **循环因果图**，将循环 SEM 与连续时间随机过程（如 Langevin 方程）的稳态分布联系起来，并讨论在非线性或非高斯情形下 d-分离失效时的可学习性。两场报告都试图回答：当图模型包含双向边或环时，观测数据施加的约束比条件独立性更丰富，如何系统描述并利用这些约束？

**因果推断的基础与敏感性分析**这一主线涵盖三场风格迥异的报告。Matthew Gentzkow 讨论 **结构 IV 估计量的因果解释**，提出“sharp-zero consistency”概念，确保当内生变量无因果效应时估计量收敛到零，即使模型存在误设。Interview with Philip Dawid 则回溯了 Dawid 的 **决策论因果框架**，该框架拒绝潜在结果与 do-calculus，仅依赖条件独立性演算与干预分配（regime）来推导因果结论，与主流形成鲜明对比。Student talks 提出 **方差基敏感性模型**，通过约束权重估计量的方差而非极值比（如 MSM 的 Λ），得到更紧且更可解释的未测混杂边界。

若想快速把握这一季的核心技术脉络，建议按以下入口阅读：**高维因果推断入门**：先看 Philipp Bach & Sven Klaassen 的 DoubleML 教程（打底 DML 框架），再读 Yuhao Wang 的报告（进阶稀疏性理论）。**图模型的形式化约束**：M. van Ommen 的报告适合对线性代数约束感兴趣的读者，Niels Richard Hansen 的报告则适合关注循环系统与动态系统建模的读者。**因果推断基础与敏感性分析**：Matthew Gentzkow 的报告适合对 IV 稳健性感兴趣的读者，Interview with Philip Dawid 适合想了解非主流因果框架的读者，Student talks 则适合关注敏感性分析新方法的读者。

## 报告列表

### [Root-n-consistent estimators for average treatment effect with minimal sparsity](../2023-05-09-ocis-2023-05-09-yuhao-wang.md)
**讲者**: Yuhao Wang · **讨论人**: Rajarshi Mukherjee · 2023-05-09  
链接：[视频](https://youtu.be/HJCIQthynP0) · [幻灯片](https://drive.google.com/file/d/1mWfabrkmsXLAPg8ivqhynutlhKhF4qzT/view?usp=share_link) · [arXiv](https://arxiv.org/abs/2011.08661)
<details><summary>摘要</summary>

This talk is about root-n-consistent estimation of average treatment effects with high dimensional confounders under minimal sparsity conditions. The entire talk is splitted into two parts. In part I, we introduce a debiased inverse propensity score weighting (DIPW) scheme for average treatment effect estimation that delivers root-n-consistent estimates when the propensity score follows a sparse logistic regression model; and the outcome regression functions are permitted to be arbitrarily compl…

</details>

### [Graphical Representations for Algebraic Constraints of Linear Structural Equations Models](../2023-05-02-ocis-2023-05-02-m-van-ommen.md)
**讲者**: M. van Ommen · **讨论人**: Rohit Bhattacharya · 2023-05-02  
链接：[视频](https://youtu.be/2B_-z9wNfXg) · [幻灯片](https://drive.google.com/file/d/1t56dfjXzLlLOrFDGOv1NffJ-x5Tn2u6g/view?usp=share_link)
<details><summary>摘要</summary>

For any directed acyclic graph, the set of observational distributions realizable by that graph can be described in terms of conditional independence constraints. When latent confounders are considered, conditional independence constraints no longer suffice for this purpose. We study linear structural equation models, where the constraints take the form of polynomial (in)equalities on the observed covariance matrix. However, these polynomials can be exponentially large, making them impractical f…

</details>

### Causal Interpretation of Structural IV Estimands　*（暂无精读）*
**讲者**: Matthew Gentzkow · **讨论人**: Peter Hull · 2023-04-25  
<details><summary>摘要</summary>

We study the causal interpretation of instrumental variables (IV) estimands of nonlinear, multivariate structural models with respect to rich forms of model misspecification. We focus on guaranteeing that the researcher's estimator is sharp-zero consistent, meaning that the researcher concludes that the endogneous variable has no causal effect on the outcome whenever this is actually the case. Sharp-zero consistency generally requires a condition on the researcher's estimator that we call strong…

</details>

### [( Tutorial) DoubleML - A state-of-the-art framework for double machine learning in Python and R](../2023-04-18-ocis-2023-04-18-philipp-bach-sven-klaassen.md)
**讲者**: Philipp Bach, Sven Klaassen · 2023-04-18  
链接：[视频](https://youtu.be/ErecsyKEq74) · [幻灯片](https://drive.google.com/file/d/1MJKgkG_hV5-c41NIZfq5PF7fDW3L5NH5/view?usp=share_link) · [arXiv](https://arxiv.org/abs/2103.09603)
<details><summary>摘要</summary>

The Python and R packages DoubleML implement the double/debiased machine learning framework of Chernozhukov et al. (2018) for causal machine learning. This talk serves as an introduction to the double machine learning framework and as a tutorial for the implementation in Python and R. The double machine learning framework consists of three key ingredients: Neyman orthogonality, high-quality machine learning estimation and sample splitting. In DoubleML, estimation of nuisance components can be pe…

</details>

### [Cyclic graphical models and causal learning](../2023-04-11-ocis-2023-04-11-niels-richard-hansen.md)
**讲者**: Niels Richard Hansen · **讨论人**: Patrick Forré · 2023-04-11  
链接：[视频](https://youtu.be/BgEE1_7Id1U) · [幻灯片](https://drive.google.com/file/d/13yUdg8Xn8hgqm4mAU3U0cLOst9DpnMCT/view?usp=sharing)
<details><summary>摘要</summary>

Directed Graphs (DGs) can be used both formally and informally to represent and communicate causal relations. The formal mathematical theory is particularly well developed for Directed Acyclic Graphs (DAGs) to support structural causal models, do-calculus, identification theory and causal learning. It is natural to interpret DGs with cycles as allowing for feedback mechanisms, but this can be formalized by different incompatible mathematical theories. In the first part of the talk I will survey …

</details>

### [Interviewer: Vanessa Didelez](../2023-04-04-ocis-2023-04-04-interview-with-philip-dawid.md)
**讲者**: Interview with Philip Dawid · 2023-04-04  
链接：[视频](https://youtu.be/0uFmoytcjHU)

### [Variance-based sensitivity analysis for weighting estimators results in more informative bounds](../2023-03-14-ocis-2023-03-14-student-talks.md)
**讲者**: Student talks · 2023-03-14  
链接：[视频](https://youtu.be/j_nKU3hU-wc) · [幻灯片](https://drive.google.com/file/d/1dD7DSyRkckUSHRMe0KuSOFXlvyZcPBU3/view?usp=share_link)


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

