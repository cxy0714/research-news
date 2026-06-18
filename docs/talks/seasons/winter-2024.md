# OCIS · Winter 2024

- 共 2 场 · 1 篇精读 · Online Causal Inference Seminar

## 本季导览

> 自动生成：归纳本季主线与值得先看的几场，**不打分、不排名**。

OCIS Winter 2024 两场报告聚焦于因果推断的**基础数学结构**与**因果表示学习的可识别性**，分别从公理化与交互式学习两个方向切入。Krikamol Muandet 的工作试图为因果性建立类似 Kolmogorov 概率论的测度论公理体系，将干预能力编码为概率空间上的转移概率核，从而在比结构因果模型（SCM）更底层处统一观测与干预分布。Sara Magliacane 的 BISCUIT 则关注在二元交互（如机器人操作）中，当智能体无法直接观测干预目标时，如何从交互数据中识别潜在的因果变量——这属于因果表示学习在弱监督交互场景下的可识别性问题。

两条主线虽分属不同层次，但共享一个核心关切：**因果结构的先验假设与可识别性之间的张力**。Muandet 的公理化试图用测度论语言消解 SCM 对有限变量、无环、离散索引集的依赖，为连续时间、不可数索引集等场景提供统一框架；Magliacane 则在交互场景中证明，即使干预目标未知，只要交互满足某些结构条件（如二元性、稀疏性），因果变量仍可被识别。两者都触及了“因果信息从何而来”这一根本问题：Muandet 从概率空间的扩展中寻找，Magliacane 从交互的对称性与约束中提取。

若想快速把握这一季的脉络，建议先看 Muandet 的报告作为**基础层**——它提供了理解因果公理化的测度论视角，适合对因果数学基础感兴趣的读者；再看 Magliacane 的报告作为**应用层**——它展示了公理化思想在具体交互学习问题中的落地，适合关注因果表示学习与机器人学习的读者。两场报告在难度上大致平行，但 Muandet 更偏理论构造，Magliacane 更偏算法与可识别性证明。

## 报告列表

### [A Measure-Theoretic Axiomatisation of Causality](../2024-03-26-ocis-2024-03-26-krikamol-muandet.md)
**讲者**: Krikamol Muandet · **讨论人**: Ricardo Silva - Q&A moderator: Junhyung Park · 2024-03-26  
链接：[视频](https://youtu.be/uiFdGZcKbSY) · [幻灯片](https://drive.google.com/file/d/1bmT27qVWDvYJ94RGVD17kl7iQq4OYaS2/view?usp=sharing) · [arXiv](https://arxiv.org/abs/2305.17139)
<details><summary>摘要</summary>

Causality is a central concept in a wide range of research areas, yet there is still no universally agreed axiomatisation of causality. We view causality both as an extension of probability theory and as a study of \textit{what happens when one intervenes on a system}, and argue in favour of taking Kolmogorov's measure-theoretic axiomatisation of probability as the starting point towards an axiomatisation of causality. To that end, we propose the notion of a \textit{causal space}, consisting of …

</details>

### BISCUIT: Causal Representation Learning from Binary Interactions　*（暂无精读）*
**讲者**: Sara Magliacane · **讨论人**: Sébastien Lachapelle · 2024-03-19  
链接：[视频](https://youtu.be/vPpfExqOdCE) · [幻灯片](https://drive.google.com/file/d/1nllryOY_DUveYyQSViBobu3-5Ewi4SAR/view?usp=sharing)
<details><summary>摘要</summary>

Identifying the causal variables of an environment and how to intervene on them is of core value in applications such as robotics and embodied AI. While an agent can commonly interact with the environment and may implicitly perturb the behavior of some of these causal variables, often the targets it affects remain unknown. In this talk, we show that causal variables can still be identified for many common setups, e.g., additive Gaussian noise models, if the agent's interactions with a causal var…

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

