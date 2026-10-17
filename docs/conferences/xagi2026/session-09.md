# Session 09 · AI4Science

> XAGI 2026 交叉智能大会 · 10 月 18 日（周日）上午 10:00-12:00 · 8会（友谊宫二层8号会议室） · [返回会议总览](index.md)

- 4 场报告 · 已精读 0 场

**主持**：田润泽（中国人民大学）、谢超（清华大学）

---

### 1. Memory Mechanisms in Genomic Foundation Models

**讲者**：许慧楠（中国科学院大学 · 杭州高等研究院） · 10:00-10:30

**对应论文**：待匹配（精读该场时自动检索 arXiv / OpenAlex）

<details><summary>摘要（会议官网）</summary>

Genomic sequences exhibit widespread long‑range dependencies, and their data density is completely different from that of natural language. Architectures for information compression in natural language are not fully applicable to the genomic domain, and genome modeling requires its unique approaches. Studies including Gengram have introduced memory into genomic large models and achieved unprecedented performance across multiple tasks. Memory mechanisms can retain key biological features, mitigate attention computational costs, and improve the model’s ability to extract long‑range genomic signals, yielding promising effects for long‑sequence modeling.

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

中国科学院大学人工智能，研究方向为AI for Biology、基因组基座大模型大模型记忆、多模态大模型，在多个顶级期刊发表论文，参与Genos、CENO等重大课题，主导Meno的研发。

</details>


### 2. AI赋能聚变等离子体仿真、控制和诊断

**讲者**：吴泰霖（西湖大学 · 人工智能系） · 10:30-11:00

**对应论文**：待匹配（精读该场时自动检索 arXiv / OpenAlex）

<details><summary>摘要（会议官网）</summary>

聚变等离子体因其非线性、多尺度及强耦合特性，在仿真、实时控制与高精度诊断上面临巨大挑战。本报告将展示AI赋能这三方面的潜力与挑战，并介绍本组近期成果。在仿真方面，AI可加速大规模动力学模拟，显著提升计算效率；在控制方面，强化学习等算法能实现等离子体位形和不稳定性的自适应实时调节；在诊断方面，神经网络可高效处理多源诊断数据，实现关键参数的快速反演与异常检测。三者协同，为聚变堆的智能化运维奠定基础。

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

吴泰霖，西湖大学工学院人工智能系特聘研究员、助理教授，原力引擎创始人。北京大学物理学院本科，麻省理工学院物理系博士，斯坦福大学计算机系博士后。主要研究领域为开发机器学习方法用于大规模科学仿真、控制、设计和发现，并在聚变、流体、物理等领域科学和工程领域应用。主持国家基金委重大研究计划培育项目等。在人工智能顶级会议和物理学顶级期刊等发表文章40余篇，其中7篇被评为热点论文。

</details>


### 3. 跨发育阶段精神共病的层级神经认知模型

**讲者**：谢超（清华大学 · 心理与认知科学系） · 11:00-11:30

**对应论文**：待匹配（精读该场时自动检索 arXiv / OpenAlex）

<details><summary>摘要（会议官网）</summary>

精神疾病共病是精准精神病学研究与临床诊疗中的关键难题，其复杂的神经病理机制仍有待深入阐明。本报告将介绍围绕精神疾病共病机制开展的系列研究，我们构建了精神共病层级神经认知模型（NeuroHiP），首次识别出一种由前额叶执行控制环路高连接特征驱动、贯穿外化与内化核心症状的通用性神经精神病理因子，揭示了不同精神疾病共病背后的共性神经机制（Nature Medicine, 2023）。在此层级模型基础上，研究进一步实现了病理机制的精细化分解，分离出两类特异性神经病理因子：其一为与冲动特质相关的外化因子，主要表现为感觉运动环路连接异常增强；其二为与神经质特质相关的内化因子，核心特征为前额叶-眶额叶目标导向环路连接异常减弱（Nature Mental Health, 2026）。上述发现在覆盖青春前期至成人期的六个独立研究队列中得到系统验证，显示出良好的稳健性与可重复性。该系列研究构建了精神疾病共病的层级化神经认知机制框架，有助于厘清共病中的共性与特异性病理差异，并为精神疾病的分层早期干预、精准诊疗体系建设以及精准精神病学的发展提供新的科学视角与理论依据。

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

谢超，清华大学心理与认知科学系助理教授。研究方向为脑发育与精神共病的神经认知机制，结合大规模脑影像、连接组预测建模、行为遗传与计算建模等手段。以第一作者身份在Nature Medicine、Nature Mental Health，Science Advances等期刊上发表论文，并获得博新计划和教育部珠峰计划等支持，主持国自然面上和青年项目等项目。

</details>


### 4. 基因组大模型Carbon

**讲者**：李秋熠（北京中关村学院 · AI for Science） · 11:30-12:00

**对应论文**：待匹配（精读该场时自动检索 arXiv / OpenAlex）

<details><summary>摘要（会议官网）</summary>

Carbon是由北京中关村学院与HuggingFace联合开发的生成式基因组大模型，旨在降低基因组AI的应用门槛，使其不再高度依赖GPU集群资源。模型参数量为30亿，在多个基准任务上的表现优于70亿参数的Evo2模型，同时计算效率提升约275倍。Carbon在应用层面主要聚焦两个方向：其一，DNA序列设计，涵盖调控元件优化和mRNA疫苗设计等合成生物学与精准医学场景；其二，基因组注释，不依赖传统序列比对方法，而是基于序列内在特征直接解读DNA的功能信息，为比较基因组学、蛋白质发现和通路分析等下游任务提供基础支持。基于Carbon的注释能力，研究团队完成了对16万亿碱基序列的系统性注释，构建了目前已知规模最大的AI基因注释数据库Carbon Database，其数据量和物种多样性较现有公开资源扩大约8倍。该数据库对AI4S领域可作为训练DNA与蛋白语言模型的多源语料库；对生命科学领域则提供了识别新物种、新基因和新功能的潜在数据基础。Carbon模型与Carbon Database共同构成面向生命科学研究的基础设施框架。未来，北京中关村学院与HuggingFace计划进一步探索融合基因组理解与自然语言交互的模型体系，以支持更广泛的生命科学人机协作研究场景。

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

李秋熠，北京中关村学院AI for Science研究员，墨尔本大学应用数学博士，曾任阿里达摩院博士后、阿里云AI算法高级工程师。其研究主要聚焦大语言模型技术在生命科学，特别是基因组学中的应用。作为DNA大模型项目Gener Project的发起人与带头人，他主导研发了Gener系列基因组基础模型GENERator与GENERanno。在此基础上，他进一步联合国际知名开源社区Hugging Face推动新一代基因组基础模型Carbon的研发，在模型性能与计算效率方面均展现出国际竞争力，并拓展其在序列设计、功能分析、基因注释等场景中的应用，致力于打造生命科学领域的“DeepSeek”。

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)
