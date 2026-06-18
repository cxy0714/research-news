# OCIS · Spring 2024

- 共 17 场 · 15 篇精读

## 本季导览

> 自动生成：归纳本季主线与值得先看的几场，**不打分、不排名**。

这一季的 17 场报告大致可归纳为四条主线：**因果识别与推断的基础框架**（Pinto、Miao）、**因果效应估计中的偏差与稳健性**（Ye、Díaz、Yang、Robertson & Dahabreh、Dwivedi）、**因果与机器学习的交叉**（van der Schaar、Ma、Imai、Magliacane & Lippe、Veitch、Peters et al.），以及**因果推断在特定领域的应用与设计**（Kang、Glymour、Tipton、Lagnado）。其中，多条主线共享对“未观测混杂”和“分布漂移”的关切，但切入角度和方法工具差异显著。

**因果识别与推断的基础框架** 是这一季的理论锚点。Pinto 对比潜在结果、SCM 和其提出的“假设模型”，试图统一因果的形式化语言；Miao 则从多处理多结局的稀疏性假设出发，提出无需已知负对照的“特异性分数”检验，为弱假设下的因果推断提供了新工具。两者都触及因果推断的底层逻辑，但前者更偏哲学与教学，后者更偏可操作的方法。

**因果效应估计中的偏差与稳健性** 是内容最密集的主线。Ye 聚焦多变量孟德尔随机化中的弱工具变量偏差，提出去偏估计量；Díaz 处理中介分析中的中间混杂问题，用“recanting twins”框架扩展路径特异性效应；Yang 解决中介变量和结局同时非随机缺失时的识别问题，利用图形假设避免强参数假设；Robertson & Dahabreh 讨论非依从性下的意向治疗和按方案效应向目标总体的运输；Dwivedi 将双重稳健性引入潜因子模型，以应对非低秩结局和稀疏邻居问题。这些工作共同展示了如何在不同识别策略（IV、中介、缺失、运输、面板数据）下，通过去偏、稳健化或敏感性分析来应对核心假设的违反。

**因果与机器学习的交叉** 覆盖了从因果发现到表示学习再到泛化理论。van der Schaar 提出从数据中发现闭式控制方程（ODE/PDE）作为因果之梯的更高层；Ma 尝试构建“因果基础模型”，利用注意力机制与因果推断的对偶性实现零样本因果效应估计；Imai 的“cram”方法用单次数据通过同时学习和评估，解决后选择推断的效率问题；Magliacane & Lippe 从二元交互的序列数据中无监督学习因果表示；Veitch 为生成模型中的线性表示假设提供因果形式化基础；Peters et al. 系统分析基于不变性的分布泛化，给出外推的理论边界。这些工作将因果思想嵌入深度学习的不同环节，但共同面临可识别性与泛化性的权衡。

**应用与设计** 主线展示了因果推断在具体领域的落地。Kang 将迁移学习与敏感性分析结合，讨论选举广告效果从 2020 到 2024 年的可迁移性；Glymour 以痴呆症研究为例，展示证据三角测量如何整合不同偏倚来源的估计；Tipton 重新设计随机试验以预测个体处理效应，给出样本量公式的修正；Lagnado 从认知科学角度考察人类因果推理的生态效度。这些报告虽不开发新方法，但为方法选择与结果解读提供了重要视角。

若想快速切入，建议按以下路径：**基础理论**可先看 Pinto（框架对比）和 Miao（稀疏性检验）；**偏差与稳健性**可从 Ye（弱IV去偏）和 Díaz（中间混杂）入手，再进阶到 Yang（MNAR缺失）和 Dwivedi（双重稳健潜因子）；**因果与ML交叉**可从 Imai（同时学习与评估）和 Peters et al.（不变性泛化）打底，再深入 Ma（因果基础模型）和 van der Schaar（控制方程发现）；**应用设计**可从 Kang（迁移敏感性分析）和 Tipton（ITE预测设计）开始，再参考 Glymour（三角测量）和 Lagnado（认知因果）。

## 报告列表

### [Introducing the specificity score: a measure of causality beyond P value](../2024-06-04-ocis-2024-06-04-wang-miao.md)
**讲者**: Wang Miao · **讨论人**: Qingyuan Zhao · 2024-06-04  
链接：[视频](https://youtu.be/gyxzf09JYzU)
<details><summary>摘要</summary>

There is considerable debate about P value in scientific research and its use is banished in several prestigious journals in recent years. Particularly in observational studies where confounding or selection bias arises, P value as a measure of statistical significance fails to capture the causal association of scientific interest, and could lead to false or trivial scientific discoveries. In this talk, I will introduce a specificity score for testing the existence of causal effects in the prese…

</details>

### [What is causality? How to express it? And why it matters](../2024-05-28-ocis-2024-05-28-rodrigo-pinto.md)
**讲者**: Rodrigo Pinto · **讨论人**: Ilya Shpitser · 2024-05-28  
链接：[视频](https://youtu.be/fz4ZWsCiM6Q) · [幻灯片](https://drive.google.com/file/d/11PxtA9cTzTJV1Q7GaCJHKXwWYbcD-Cpf/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2211.08209)
<details><summary>摘要</summary>

Causality is a well-studied concept in economics, yet effective causal analysis necessitates tools beyond traditional statistics and probability theory. Economists have historically employed structural equations and causal tools for this purpose. Alongside this traditional approach, several frameworks have been developed to address and manipulate causal inquiries. This paper explores the advantages and drawbacks of three prominent approaches: Haavelmo's Hypothetical Model Approach, the Language …

</details>

### Integrating Double Robustness into Causal Latent Factor Models　*（暂无精读）*
**讲者**: Raaz Dwivedi · **讨论人**: James Robins · 2024-05-07  
链接：[视频](https://youtu.be/QDTTR7JH3DM) · [幻灯片](https://drive.google.com/file/d/1FzZ-nxIjj5wsxLKYPedLlh65lXj1simL/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2402.11652)
<details><summary>摘要</summary>

Latent factor models are widely utilized for causal inference in panel data, involving multiple measurements across various units. Popular inference methods include matrix completion for estimating the average treatment effect (ATE) and the nearest neighbor approach for individual treatment effects (ITE). However, these methods respectively underperform with non-low-rank outcomes or when faced with diverse units in the data. To tackle these challenges, we integrate double robustness principles w…

</details>

### [Transfer Learning Between U.S. Presidential Elections: How much can we learn from a 2020 ad campaign to inform 2024 elections?](../2024-04-30-ocis-2024-04-30-hyunseung-kang.md)
**讲者**: Hyunseung Kang · **讨论人**: Melody Huang · 2024-04-30  
链接：[视频](https://youtu.be/WzH2YzaVQx0) · [幻灯片](https://drive.google.com/file/d/1XgoVvSFh-tm9s0aShds7Yaq7DYe9e4ds/view?usp=sharing)
<details><summary>摘要</summary>

In the 2020 U.S presidential election, Aggarwal et al. (2023) ran a large-scale, randomized experiment to analyze the impact of an online ad campaign on voter turnout and found that the overall impact was “effectively equivalent to zero." As the 2024 election approaches, a natural question to ask is whether a similar ad campaign would remain ineffective during this election. Despite some similarities between 2020 and 2024, such as the same presumptive candidates and concerns about the economy, d…

</details>

### [The (Causal) Discovery Ladder: Unravelling Governing Equations and Beyond using Machine Learning](../2024-04-16-ocis-2024-04-16-mihaela-van-der-schaar.md)
**讲者**: Mihaela van der Schaar · 2024-04-16  
链接：[视频](https://youtu.be/P-GxxhhcLUo) · [幻灯片](https://drive.google.com/file/d/1Y3s5gzw-I-K7F1g75i_i3oYAOkaKSbVV/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2002.04083)

### [Towards Causal Foundation Model: on Duality between Causal Inference and Attention](../2024-04-09-ocis-2024-04-09-chao-ma.md)
**讲者**: Chao Ma · **讨论人**: Jiaqi Zhang · 2024-04-09  
链接：[视频](https://youtu.be/cnz17Q6g6Lw)
<details><summary>摘要</summary>

Foundation models have brought changes to the landscape of machine learning, demonstrating sparks of human-level intelligence across a diverse array of tasks. However, a gap persists in complex tasks such as causal inference, primarily due to challenges associated with intricate reasoning steps and high numerical precision requirements. In this work, we take a first step towards building causally-aware foundation models for complex tasks. We propose a novel, theoretically sound method called Cau…

</details>

### [The Cram Method for Efficient Simultaneous Learning and Evaluation](../2024-04-02-ocis-2024-04-02-kosuke-imai.md)
**讲者**: Kosuke Imai · **讨论人**: Rui Song and Hengrui Cai - Q&A moderator: Michael Li · 2024-04-02  
链接：[视频](https://youtu.be/DSAcBPsoPa4) · [幻灯片](https://imai.fas.harvard.edu/talk/files/OnlineCausal24.pdf)
<details><summary>摘要</summary>

We introduce the `cram' method, a general and efficient approach to simultaneous learning and evaluation using a generic machine learning (ML) algorithm. In a single pass of batched data, the proposed method repeatedly trains an ML algorithm and tests its empirical performance. Because it utilizes the entire sample for both learning and evaluation, cramming is significantly more data-efficient than sample-splitting. The cram method also naturally accommodates online learning algorithms, making i…

</details>

### [BISCUIT: Causal Representation Learning from Binary Interactions](../2024-03-19-ocis-2024-03-19-sara-magliacane-phillip-lippe.md)
**讲者**: Sara Magliacane, Phillip Lippe · **讨论人**: Sébastien Lachapelle · 2024-03-19  
链接：[视频](https://youtu.be/vPpfExqOdCE) · [幻灯片](https://drive.google.com/file/d/1nllryOY_DUveYyQSViBobu3-5Ewi4SAR/view?usp=sharing)

### [Causality in Mind: Learning, Reasoning and Blaming](../2024-03-12-ocis-2024-03-12-david-lagnado.md)
**讲者**: David Lagnado · **讨论人**: Neil Bramley · 2024-03-12  
链接：[视频](https://youtu.be/jC9bE0jjmwk) · [幻灯片](https://drive.google.com/file/d/1uyefaOJO_CraBeKtWBR7jPYJFhEQYpuk/view?usp=sharing)

### [Evidence triangulation in dementia research](../2024-02-27-ocis-2024-02-27-maria-glymour.md)
**讲者**: Maria Glymour · **讨论人**: George Davey Smith · 2024-02-27  
链接：[视频](https://youtu.be/JPqpHxck0DA)

### [Recanting twins: addressing intermediate confounding in mediation analysis](../2024-02-20-ocis-2024-02-20-iv-n-d-az.md)
**讲者**: Iván Díaz · **讨论人**: Daniel Malinsky · 2024-02-20  
链接：[视频](https://youtu.be/9hAUwC6Ecnw) · [幻灯片](https://drive.google.com/file/d/1eGWvEoJL1J-0jVn0SEV7FJtUhDBO1Sqh/view?usp=sharing)

### [Debiased Multivariable Mendelian Randomization](../2024-02-13-ocis-2024-02-13-ting-ye.md)
**讲者**: Ting Ye · **讨论人**: Neil Davies · 2024-02-13  
链接：[视频](https://youtu.be/HjQ0nuq1l0M)

### [Mediation analysis with the mediator and outcome missing not at random](../2024-02-06-ocis-2024-02-06-fan-yang.md)
**讲者**: Fan Yang · **讨论人**: Xiaohua Zhou · 2024-02-06  
链接：[视频](https://youtu.be/IAmPuLuP1DA) · [幻灯片](https://drive.google.com/file/d/1grhMiHG_ODCi9CeS-oOOSpcFkzsQzsLV/view?usp=sharing)

### Transporting inferences about intention-to-treat effects and per-protocol effects when there is non-adherence　*（暂无精读）*
**讲者**: Sarah Robertson, Issa Dahabreh, ) · **讨论人**: Paul Zivich · 2024-01-30  

### [Linear Structure of High-Level Concepts in Text-Controlled Generative Models, and the role of Causality](../2024-01-23-ocis-2024-01-23-victor-veitch.md)
**讲者**: Victor Veitch · **讨论人**: Francesco Locatello · 2024-01-23  
链接：[视频](https://youtu.be/uA19kr95zG8) · [幻灯片](https://drive.google.com/file/d/1UDHou33JO0Ss9QV1aOY3y68-MKdgATOZ/view?usp=sharing)

### [On Invariance-based Generalization and Extrapolation](../2024-01-16-ocis-2024-01-16-jonas-peters-nicola-gnecco-sorawit-saeng.md)
**讲者**: Jonas Peters, Nicola Gnecco, Sorawit Saengkyongam · 2024-01-16  
链接：[视频](https://youtu.be/9eAZ0mv1PxE) · [幻灯片](https://drive.google.com/file/d/1RoehZaE1293SyI55-7vLnwsQ4-lVfcZ7/view?usp=sharing)

### [Designing Randomized Trials to Predict Treatment Effects](../2024-01-09-ocis-2024-01-09-elizabeth-tipton.md)
**讲者**: Elizabeth Tipton · **讨论人**: Andrew Gelman · 2024-01-09  
链接：[视频](https://youtu.be/d8w3pKBeeqw) · [幻灯片](https://drive.google.com/file/d/1NNpZ641c4vW2yKyv0KQeQiOFy5GANMfY/view?usp=sharing)


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

