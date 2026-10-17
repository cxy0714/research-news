# Session 13 · AI的数理和计算基础

> XAGI 2026 交叉智能大会 · 10 月 18 日（周日）下午 14:00-16:00 · 4会（友谊宫二层4号会议室） · [返回会议总览](index.md)

- 3 场报告 · 已精读 0 场

**主持**：周峰（中国人民大学）

---

### 1. Spiked Matrix Models with Rotationally Invariant Noise: AMP Algorithms and Optimality

**讲者**：马俊杰（中国科学院数学与系统科学研究院 · 计算数学与科学工程计算研究所） · 14:00-14:40

**对应论文**：待匹配（精读该场时自动检索 arXiv / OpenAlex）

<details><summary>摘要（会议官网）</summary>

In this talk, I will present our recent work on the optimality of Approximate Message Passing (AMP) algorithms for spiked matrix models with rotationally invariant noise. We introduce a new AMP algorithm that employs a matrix denoiser - acting on the eigenvalues of the observed matrix - and an iterate denoiser - applied to the AMP iterates. The resulting dynamics admit a simple state-evolution characterization, which allows us to identify the optimal pair of denoisers achieving the minimum possible asymptotic estimation error among a broad class of iterative algorithms.

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

马俊杰，中国科学院数学与系统科学研究院长聘副研究员，2015年在香港城市大学取得博士学位。曾于哥伦比亚大学、哈佛大学从事博士后研究。研究兴趣为复杂信号处理的数学理论与算法，在AOS、IEEE TIT、NeurIPS、ICML等国际期刊和会议发表多篇学术论文。曾入选中科院百人计划，主持3项国家自然基金委项目（青年项目、面上项目、青年科学基金B类项目），并参与中科院先导科技专项、科技部重点专项等科研项目。担任中国运筹学会青年工作委员会副秘书长（2022-2024）、中国现场统计研究会随机矩阵理论与应用分会理事。

</details>


### 2. An Improved SE(3)-Transformer Driven by Hamiltonian Flow

**讲者**：许洪腾（中国人民大学 · 高瓴人工智能学院） · 14:40-15:20

**对应论文**：待匹配（精读该场时自动检索 arXiv / OpenAlex）

<details><summary>摘要（会议官网）</summary>

The Transformer architecture plays a central role in modern deep learning, and its SE(3)-equivariant variants have been widely applied to molecular conformation modeling and optimization. In this study, we propose an improved SE(3)-Transformer architecture, called HamFormer, which revisits the design of SE(3)-Transformer through the lens of Hamiltonian flow. In particular, we define a parametrized Hamiltonian flow in the phase space of position and velocity, corresponding to optimizing an energy functional that combines an optimal transport-based potential with a damped momentum. The Lie-Trotter splitting framework of the Hamiltonian flow leads to the proposed HamFormer architecture, whose feedforward computation achieves the optimization step of the proposed energy functional. Furthermore, we combine HamFormer with Equivariant Graph Neural Network (EGNN), build a new model for molecular conformation optimization.

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

许洪腾，中国人民大学高瓴人工智能学院长聘副教授，博导，国家高层次青年人才。其研究方向为通用人工智能技术及其应用，特别是（1）最优传输驱动的机器学习理论与方法；（2）生成式大模型架构设计、模型压缩、模型融合；（3）AI4Math以及AI4Science等前沿应用。近年来的代表性工作包括基于最优传输距离的图神经网络设计与学习方法、数值算法驱动的大模型架构设计与高效适配、基于生成式人工智能的柔性大分子建模技术等。研究工作曾获得ICML2025 AI for Math研讨会杰出论文提名奖，入选《Environmental Science & Technology》副封面文章等荣誉。主持国家自然科学基金重大研究计划培育项目、中央引导地方人工智能专项等项目。

</details>


### 3. 高效大模型

**讲者**：周峰（中国人民大学 · 统计学院） · 15:20-16:00

**对应论文**：待匹配（精读该场时自动检索 arXiv / OpenAlex）

<details><summary>摘要（会议官网）</summary>

面向大模型在长序列建模与自回归生成中的效率瓶颈，相关研究从注意力计算和推理解码两个层面展开。在注意力计算方面，Flexformer通过学习随机傅里叶特征的谱频率，实现灵活且高效的注意力核建模，提升了线性注意力的表达能力。在推理解码方面，MDSeq采用多草稿序列级验证机制，通过优化接受概率与残差分布，提高推测解码的期望接受长度。理论分析与实验结果表明，该系列工作能够在保持模型性能与采样正确性的同时，有效提升长序列建模和大模型推理效率，为高效大模型的研究与应用提供了新的技术路径。

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

周峰，中国人民大学统计学院副教授，主要研究领域包括统计机器学习、贝叶斯方法、随机过程、大模型推理加速等，主持国家自然科学基金青年项目、面上项目，在JMLR、STCO、ICML、NeurIPS、ICLR、AAAI、KDD等国际期刊和会议上发表论文40余篇，担任NeurIPS、ICLR、IJCAI、AISTATS等国际会议领域主席，国际期刊《Statistics and Computing》副主编，《Transactions on Machine Learning Research》执行编辑，《Journal of Machine Learning Research》编委。

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)
