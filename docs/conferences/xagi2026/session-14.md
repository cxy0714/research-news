# Session 14 · Agent技术及应用

> XAGI 2026 交叉智能大会 · 10 月 18 日（周日）下午 14:00-16:00 · 3会（友谊宫二层3号会议室） · [返回会议总览](index.md)

- 4 场报告 · 已精读 0 场

**主持**：从鑫（清华大学）

## 本场导览

> 自动生成：归纳本场主线，**不打分、不排名**。

这一场报告围绕“智能体如何从工具走向协作伙伴”展开，四条主线分别对应教育、科研、系统架构和评估基准。王宏宁的AI Cosmos聚焦多智能体驱动的教学场景，强调自然语言交互与虚实融合；李鹏的AIM系统面向数学研究，探索智能体在定理发现与验证中的角色；闫宇坤的PilotDeck则从操作系统层面解决多项目并行、记忆污染和Token成本问题；从鑫的工作则补上评估缺口，关注LLM在统计问题形式化中的能力。

最突出的主线是“智能体在专业领域中的自主性与协作机制”。李鹏的AIM系统与王宏宁的AI Cosmos形成互补：前者以数学定理为对象，通过自然语言交互和智能体协作辅助问题探索与可信验证，后者以教学任务为载体，让多智能体自主编排角色研讨、代码实训和仿真实验。两者都依赖自然语言作为交互界面，但AIM更强调推理链的可信性，AI Cosmos更侧重场景构建的灵活性。闫宇坤的PilotDeck则从底层设计切入，提出独立工作舱、项目制白盒记忆和常驻式主动执行，试图解决前两者可能面临的记忆污染和能动性缺失问题——这构成一种递进关系：从任务级智能体到系统级智能体。从鑫的基准研究则独立于前三者，为这类系统提供可量化的评估维度，尤其关注用户目标未明确时的任务推断能力。

若想快速建立整体图景，建议先看闫宇坤的PilotDeck（系统架构视角）和从鑫的基准工作（评估视角），这两场能帮你理解智能体系统的边界与瓶颈。若你关注具体应用落地，可再深入李鹏的AIM（数学研究）和王宏宁的AI Cosmos（教育场景），两者分别展示了智能体在知识发现和教学互动中的实际路径。按主题选择入口即可：系统设计打底看闫宇坤，评估方法打底看从鑫，领域应用进阶看李鹏或王宏宁。

---

### 1. 情境学习与协作发现：人工智能赋能教育教学新范式

**讲者**：王宏宁（清华大学 · 计算机系） · 14:00-14:30

**对应论文**：未检索到公开论文（以下为依据报告摘要与讲者方向的推断）

<details><summary>摘要（会议官网）</summary>

<p>AI Cosmos是由清华大学计算机系交互式人工智能实验室（CoAI）研发的一款多智能体驱动的情景化教学系统（官网：aicosmos.ai），致力于将人工智能从简单的辅助教学工具进化为激发学生认知与创造力的核心伙伴。该系统突破传统AI教学工具的技术门槛，实现全流程自然语言交互，让使用者无需AI或编程基础即可通过多智能体自主编排，轻松构建涵盖多角色研讨、代码实训、交互式视频生成以及仿真实验室的虚实融合“实践空间”。AI Cosmos让师生能够全身心投入到“在做中学”的沉浸式教学体验中，实现教育创新与前沿AI技术的无缝衔接。</p>

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

<p>王宏宁，清华大学计算机系长聘副教授，国家高层次人才，长期专注于强化学习、大模型技术的研究。曾任美国弗吉尼亚大学计算机系Copenhaver讲席副教授，2023年秋加入清华大学后，重点投身于AI赋能教育教学的探索与实践，积累了丰富的理论研究与实践经验。</p>

</details>


### 2. 自然语言驱动的数学研究智能体 - AIM系统的探索与实践

**讲者**：李鹏（清华大学 · 智能产业研究院） · 14:30-15:00

**对应论文**：未检索到公开论文（以下为依据报告摘要与讲者方向的推断）

<details><summary>摘要（会议官网）</summary>

<p>数学作为科学进步的重要基石，长期支撑着各学科的发展与突破。近年来，人工智能的迅猛发展正在推动科学研究范式发生深刻变革，也为数学研究带来了新的机遇与挑战。当 AI 遇见数学，尤其是当自然语言成为数学研究智能体理解问题、组织推理与协同探索的重要界面时，将会产生怎样的化学反应？本报告将围绕“自然语言驱动的数学研究智能体”这一主题，简要回顾 AI 在数学研究中的发展脉络与代表性进展，分析 AI 面向研究级数学问题时所面临的核心挑战。在此基础上，报告将重点介绍本团队研发的 AI 数学家系统 AIM，展示其如何通过自然语言交互与智能体协作机制，辅助数学问题探索、定理形成与可信验证。</p>

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

<p>李鹏，清华大学智能产业研究院副研究员，主要研究方向包括大模型、智能体、AI4Math 与 AI 驱动的科学发现，在人工智能重要国际会议和期刊发表论文 100 余篇。曾获 ACL 2023 Outstanding Paper Award、ICAIS 2025 Responsible AI Research Award、中国中文信息学会钱伟长中文信息处理科学技术奖一等奖等荣誉，主持科技创新 2030 重大项目课题、国家自然科学基金面上项目等科研项目，曾担任 ICLR、ACL、EMNLP、NAACL 等国际会议领域主席。其研究成果在腾讯微信、百度等千万级日活产品中获得应用并取得显著成效。</p>

</details>


### 3. PilotDeck - 面向生产力的智能体操作系统尝试

**讲者**：闫宇坤（启元实验室 · 大模型研究中心） · 15:00-15:30

**对应论文**：未检索到公开论文（以下为依据报告摘要与讲者方向的推断）

<details><summary>摘要（会议官网）</summary>

<p>近年来，智能体技术经历了&quot;推理能力增强 → 工具能力提升 → 复杂问题拆解&quot;等发展阶段，正从&quot;问答工具&quot;和&quot;专业智能体&quot;迈向更具通用能力的智能体操作系统（Agent OS）。然而，当前Agent OS在多项目并行的记忆污染、不加区分的Token成本浪费、以及问答范式下的能动性缺失等方面仍存在显著瓶颈。 PilotDeck以&quot;解放生产力的第一性原理 - 提供好的生产关系&quot;为设计思路，为大型语言模型提供最适合其工作的生产环境与执行模式，核心创新包括独立工作舱、项目制白盒记忆、多模型智能路由、常驻式主动执行等方面。</p>

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

<p>闫宇坤，启元实验室（Qiyuan Lab）大模型中心副研究员，清华大学自然语言处理实验室（THUNLP）客座研究员，博士毕业于清华大学脑与智能实验室，主要研究方向为大模型知识增强与智能体技术。近年来，在ICLR、NeurIPS、ICML、ACL等人工智能顶级国际会议发表论文40余篇，Google引用超千次，多次担任领域主席与审稿人。主持负责大模型相关开源项目UltraRAG（Github Trending Rank 2）、PilotDeck等，累计星标量1万以上；主持负责开源模型MiniCPM-Emedding系列、VisRAG-Ret系列等，累计下载量超50万次。</p>

</details>


### 4. Benchmarking Language Models for Statistical Problem Formulation

**讲者**：从鑫（清华大学 · 统计与数据科学系） · 15:30-16:00

**对应论文**：Benchmarking Language Models for Statistical Problem Formulation · [arXiv:2609.01982](https://arxiv.org/abs/2609.01982)

<details><summary>摘要（会议官网）</summary>

<p>Large language models (LLMs) are increasingly used as assistants for statistical and data science work, yet existing evaluations largely assume the analysis target is already specified. In practice, users arrive with informal goals and heterogeneous data, leaving the model to decide what statistical task is implied and which data are relevant. We first formalize this upstream step as Statistical Problem Formulation and decompose it into two subtasks: (1) Statistical Problem Classification and (2) Variable Identification &amp; Role Assignment. We then introduce StatFormBench, a benchmark built from five cross-domain statistics textbooks and a data science case library, covering diverse problem types, data representations, and scenario styles. It contains 1,013 samples spanning 20 coarse-grained and 85 fine-grained statistical problem categories. Across 14 LLMs, the best one reach only 72.0 fine-grained classification accuracy and 63.2 variable set overlap.</p>

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

<p>从鑫， 清华大学统计与数据科学系助理教授， 主要研究方向为人工智能、大语言模型、自主智能体、智能数据分析。曾在 ACL、ICLR、NeurlPS 等人工智能顶级国际学术会议或期刊上发表论文 40 余篇，Google Scholar 总引用 7000 余次。曾主持发布了大语言模型工具学习框架 ToolLLM、大语言模型驱动的自主智能体框架XAgent 等工作。 其中 ToolLLM 被 ICLR 2024 评选为 Spotlight 论文， XAgent 在世界影响力最大的开源平台 Github 上获得超过 8K 颗星标关注，受到了国内外众多知名学者和企业的高度评价。</p>

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)
