# Session 02 · AI4Math & Theory

> XAGI 2026 交叉智能大会 · 10 月 17 日（周六）下午 14:00-16:00 · 9会（友谊宫二层9号会议室） · [返回会议总览](index.md)

- 4 场报告 · 已精读 0 场

**主持**：刘方辉（上海交通大学）

## 本场导览

> 自动生成：归纳本场主线，**不打分、不排名**。

这一场报告围绕“AI4Math与理论”展开，核心关切是数学与AI的双向互动：一方面，如何用数学理论解释深度学习机制；另一方面，如何用AI辅助数学研究。四条主线清晰可辨：其一，深度学习理论的方法论反思（刘方辉），讨论理论应具备何种知识形态与设计价值；其二，AI驱动的数学形式化与证明（邹荻凡、沈皓），聚焦从自然语言到形式语言的自动化流程；其三，数学工具用于解析训练动力学（罗涛），涉及几何测度论、动力系统等；其四，数学文献的智能处理与交互（罗涛），强调表示框架对检索和研读的支撑。

最突出的主线是“AI4Math”方向，即用大模型和智能体自动化数学形式化与证明。邹荻凡的VALG Agent和OpenTheoryBench直接挑战现有基准的局限——它们只验证预形式化定理，而VALG试图覆盖从原始论文提取、结构化到验证的完整流程，并引入贡献分类、来源审计和证明重建等步骤，这相当于把“问题提出”纳入自动化范围。沈皓的MechGeo则聚焦欧氏几何，通过GeoFormalizer将非正式问题翻译为Lean 4并修复语句，再用GeoProver整合几何推理与符号计算，所有证明经Lean 4内核验证，强调“忠实形式化”与“可认证构造”。两者互补：VALG面向通用ML理论，MechGeo专精几何领域，但共享“智能体+形式验证”的架构思路。罗涛的算子树与结构化自然语言框架则从另一侧切入，通过改进表示来提升自动形式化的准确率，与邹、沈的工作形成递进——先有更好的语义表示，才有更可靠的翻译与证明。

若想快速进入这一场，建议按主题选择入口。对“AI4Math自动化”感兴趣，先看邹荻凡的VALG与OpenTheoryBench，理解当前基准缺口和智能体流程；再看沈皓的MechGeo，看领域特化如何落地。对“深度学习理论”本身，刘方辉的报告提供方法论框架，适合作为理论定位的起点；罗涛的报告则给出具体数学工具的应用案例，可作进阶阅读。若关注数学文献处理，罗涛的表示框架是直接入口。四场报告无先后依赖，但邹、沈、罗三场在“形式化”主题上可串联阅读，刘方辉的报告则独立提供理论视角。

---

### 1. 深度学习理论的技术科学道路

**讲者**：刘方辉（上海交通大学 · 自然科学研究院） · 14:00-14:30

**对应论文**：未检索到公开论文（以下为依据报告摘要与讲者方向的推断）

<details><summary>摘要（会议官网）</summary>

<p>在这次观点报告中，我将探讨深度学习需要怎样的理论？数学证明、机制解释与经验预测分别提供什么知识，理论又应当如何指导实践？本报告以“scaling law 算不算理论”为切入点，讨论理论的定义、功能与评价，区分数学严密性、经验有效性与设计价值，进而提出发展深度学习技术科学理论的研究立场。 我以工程实践学科中的旧三论：信息论、控制论和系统论为参照，重点回顾控制理论与工程实践相互推动的发展历程，探讨如何从具体问题中形成共性的理论对象，以及如何构造连接观测、分析与设计的有效描述。在此基础上，回到深度学习的具体问题，讨论训练动力学中的有效状态、近似闭合、干预响应与迁移边界，并结合大语言模型预训练的尺度律与跨日程预测，探讨从预测训练响应走向训练日程设计所需的进一步工作。</p>

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

<p>刘方辉，上海交通大学自然科学研究院与数学科学学院副教授，数学学院与人工智能学院博士生导师，之前在英国华威大学担任助理教授。研究方向为机器学习数学理论与大模型机理分析。其主要研究工作包括函数空间视角下的机器学习理论、尺度扩展下的泛化理论，并进一步推动理论指导实践的研究范式。2023年入选国家高层次人才青年项目，2024年获得AAAI新教师奖，2025年入选TUM全球访问教授计划，2026年获得美国数学与统计创新研究所（IMSI）长期访问学者资助项目。研究获得基金委面上项目、英国皇家学会、谷歌的资助。主办 NeurIPS‘24，’26研讨会，担任IJCV专刊客座编辑，在 ICASSP’23、CVPR’23、ISIT’24 等国际顶级会议上主讲tutorial。担任NeurIPS、ICLR、AISTATS等会议领域主席。</p>

</details>


### 2. LLM for ML Theory at Scale: The VALG Agent and OpenTheoryBench

**讲者**：邹荻凡（香港大学 · 计算与数据科学学院） · 14:30-15:00

**对应论文**：VALG: An Agentic System for ML Theory Research · [arXiv:2608.13060](https://arxiv.org/abs/2608.13060)

<details><summary>摘要（会议官网）</summary>

<p>LLM capabilities for ML theory are not validated. Existing benchmarks rely on pre-formalized theorems, missing the core challenge: formulating problems from raw papers - extracting, structuring, and validating theoretical claims. We present two contributions. VALG is an agentic pipeline automating the full paper-to-proof process: contribution triage, source auditing, proof reconstruction, and rubric-based evaluation. OpenTheoryBench is an open-source benchmark built from recent arXiv papers, providing hundreds of realistic proof problems covering dependency planning, quantitative reasoning, and capability integration. Together they test novel-theorem solving and diagnose interpretation, strategy, and derivation failures. Empirical validation shows strong discriminative power, with model performance tracking task complexity monotonically. Finally, we aim to bridge informal mathematical writing and machine-verifiable reasoning, advancing AI for theoretical ML research.</p>

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

<p>Dr.Difan Zou is an assistant professor in computer science department and institute of data science at HKU. He has received his PhD degree in Department of Computer Science, University of California, Los Angeles (UCLA). His research interests are broadly in machine learning, deep learning theory, graph learning, mechanism interpretation, and interdisciplinary research between AI and other subjects. His research is published in top‑tier machine learning conferences (ICML, NeurIPS, COLT, ICLR) and journal papers (IEEE Trans., JMLR, Nature Comm., PNAS, etc.). He serves as an area chair/senior PC member for NeurIPS, ICML and AAAI, and PC members for ICLR, COLT, etc.</p>

</details>


### 3. 数学自然语言的形式化与结构化

**讲者**：罗涛（上海交通大学 · 数学科学学院） · 15:00-15:30

**对应论文**：未检索到公开论文（以下为依据报告摘要与讲者方向的推断）

<details><summary>摘要（会议官网）</summary>

<p>人工智能的蓬勃发展正重塑科学研究范式，数学与AI的深度交叉呈现出“双向赋能”的新格局。本报告将汇报团队近期在“Math4AI”（基于数学理论的深度学习机理解析）与“AI4Math”（基于人工智能的数学研究辅助）两个方向的初步探索。在Math4AI层面，我们引入几何测度论、动力系统与渐近分析方法，深入剖析深度学习的训练动力学机制，针对偏微分方程求解中的泛化失效、神经网络训练中的参数凝聚与秩坍缩现象，以及注意力机制中“聚焦-稀释”的多阶段演化规律提供了初步的理论诠释。在AI4Math层面，我们致力于弥合自然语言与形式语言的语义鸿沟，提出了算子树与结构化自然语言等创新性表示框架。该框架不仅显著提升了自动形式化的准确率与语义评估的鲁棒性，更为数学文献的智能检索与学生、专家的交互式研读提供了有力工具。报告最后将展望这一交叉领域的未来挑战与研究愿景。</p>

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

<p>罗涛，上海交通大学数学科学学院/自然科学研究院副教授。2012年获上海交通大学致远学院学士学位，2017年获香港科技大学博士学位，并获香港数学会最佳博士论文奖。2017至2020年，担任普渡大学数学系Golomb访问助理教授。研究方向为计算材料科学、深度学习数学理论（Math4AI）和数学智能（AI4Math）。研究内容包括材料科学的 Peierls–Nabarro 模型、Cauchy–Born 法则；深度学习的频率原则、凝聚理论；数学智能的自动形式化、语义评估、结构化自然语言等。在 ARMA/SIAM 系/M3AS/JMLR/NeurIPS/ICML/ICLR 等应用数学和机器学习期刊和会议发表论文 40 余篇。获NeurIPS 2021 Spotlight、NeurIPS 2025 Oral、ICML 2026 Oral等。</p>

</details>


### 4. MechGeo: Autoformalizing and Proving Euclidean Geometry in Lean 4

**讲者**：沈皓（中国科学院大学 · 中国科学院数学与系统科学研究院） · 15:30-16:00

**对应论文**：MechGeo: Autoformalizing and Proving Euclidean Geometry in Lean 4 · [arXiv:2608.02295](https://arxiv.org/abs/2608.02295)

<details><summary>摘要（会议官网）</summary>

<p>We present MechGeo, a Mathlib-native agentic framework for faithful autoformalization and certified proof construction in Euclidean geometry. It combines GeoFormalizer, which translates informal problems into Lean 4 and repairs formal statements, with GeoProver, which integrates geometric reasoning, selective algebraization, and symbolic computation. All proofs and counterexamples are checked by the Lean kernel. On 43 historical IMO geometry problems, MechGeo proves 29 statements generated by GeoFormalizer, refutes the remaining 14 with Lean-verified counterexamples, and proves all 14 after expert repair. Together with IMO 2026 Problem 2, this yields faithful formalizations and kernel-checked proofs for 44 IMO geometry problems. On the 14 geometry statements in LEAP’s Lean-IMOBench, MechGeo proves 12, refutes the remaining two, and proves both repaired statements.</p>

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

<p>中国科学院大学、中国科学院数学与系统科学研究院应用数学博士研究生 研究方向：AI4M、形式化数学、人工智能</p>

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)
