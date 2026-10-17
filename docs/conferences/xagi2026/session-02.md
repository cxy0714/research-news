# Session 02 · AI4Math & Theory

> XAGI 2026 交叉智能大会 · 10 月 17 日（周六）下午 14:00-16:00 · 9会（友谊宫二层9号会议室） · [返回会议总览](index.md)

- 4 场报告 · 已精读 4 场

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

（未检索到公开论文，以下为推断）

**问题**：这场报告要解决的是“深度学习需要怎样的理论”这一元问题。当前以 scaling law 为代表的大模型经验规律大量涌现，但其理论地位模糊：它算不算理论？数学证明、机制解释与经验预测分别提供何种知识？报告以“scaling law 算不算理论”为切入点，认为现有讨论常混淆数学严密性、经验有效性与设计价值，因此需要重新界定理论的功能与评价标准，并在此基础上提出发展深度学习技术科学理论的研究立场。

**核心方法**：报告不提出具体算法，而是给出一个方法论框架：参照工程实践学科中的“旧三论”——信息论、控制论和系统论，尤其以控制理论与工程实践相互推动的历史为范本，探讨如何从具体问题中提炼共性的理论对象，并构造连接观测、分析与设计的有效描述。落到深度学习，报告提出四个关键概念：训练动力学中的有效状态、近似闭合、干预响应与迁移边界；并结合大语言模型预训练的尺度律与跨日程预测，讨论如何从“预测训练响应”走向“训练日程设计”。

**与已有工作的关系**：报告明显区别于当前以数学证明为主导的深度学习理论路线，后者追求严格定理，而报告强调经验有效性与设计价值。其以控制论为参照的立场，与“旧三论”中控制论“面向设计”的传统一脉相承；对 scaling law 的讨论则直接回应了近年来大模型经验规律的理论化尝试。讲者自身在函数空间视角与尺度扩展泛化理论上的工作，可视为这一“理论指导实践”范式的前期积累，但报告本身更偏向立场倡导而非技术推进。

**贡献与边界**：主要贡献是提出一套评价深度学习理论的多维标准，将设计价值与数学严密性、经验有效性并列，并以控制论为类比给出从观测到设计的路径设想。边界也很明显：这是一场观点报告，官网摘要未给出具体定理、实验或系统实现；以控制论类比深度学习是否成立、有效状态与近似闭合等概念能否严格化，均未在摘要中展开。因此其价值在于提供研究议程，而非可验证的结论。

<details><summary>讲者简介</summary>

<p>刘方辉，上海交通大学自然科学研究院与数学科学学院副教授，数学学院与人工智能学院博士生导师，之前在英国华威大学担任助理教授。研究方向为机器学习数学理论与大模型机理分析。其主要研究工作包括函数空间视角下的机器学习理论、尺度扩展下的泛化理论，并进一步推动理论指导实践的研究范式。2023年入选国家高层次人才青年项目，2024年获得AAAI新教师奖，2025年入选TUM全球访问教授计划，2026年获得美国数学与统计创新研究所（IMSI）长期访问学者资助项目。研究获得基金委面上项目、英国皇家学会、谷歌的资助。主办 NeurIPS‘24，’26研讨会，担任IJCV专刊客座编辑，在 ICASSP’23、CVPR’23、ISIT’24 等国际顶级会议上主讲tutorial。担任NeurIPS、ICLR、AISTATS等会议领域主席。</p>

</details>


### 2. LLM for ML Theory at Scale: The VALG Agent and OpenTheoryBench

**讲者**：邹荻凡（香港大学 · 计算与数据科学学院） · 14:30-15:00

**对应论文**：VALG: An Agentic System for ML Theory Research · [arXiv:2608.13060](https://arxiv.org/abs/2608.13060)

<details><summary>摘要（会议官网）</summary>

<p>LLM capabilities for ML theory are not validated. Existing benchmarks rely on pre-formalized theorems, missing the core challenge: formulating problems from raw papers - extracting, structuring, and validating theoretical claims. We present two contributions. VALG is an agentic pipeline automating the full paper-to-proof process: contribution triage, source auditing, proof reconstruction, and rubric-based evaluation. OpenTheoryBench is an open-source benchmark built from recent arXiv papers, providing hundreds of realistic proof problems covering dependency planning, quantitative reasoning, and capability integration. Together they test novel-theorem solving and diagnose interpretation, strategy, and derivation failures. Empirical validation shows strong discriminative power, with model performance tracking task complexity monotonically. Finally, we aim to bridge informal mathematical writing and machine-verifiable reasoning, advancing AI for theoretical ML research.</p>

</details>

**问题**：LLM 在机器学习理论上的能力尚未被系统验证。现有基准大多基于已形式化的定理，只测试“证明给定命题”的能力，而遗漏了理论研究的核心环节——从原始论文中提取、结构化并验证理论主张，即“问题形式化”本身。报告指出，ML 理论研究需要同时处理问题设定、定理目标与证明技术的协同演化，而现有评测无法覆盖这一过程。因此，VALG 与 OpenTheoryBench 的提出，是为了把评测从“证明已知结论”推进到“从原始文献出发构造并求解新问题”，并诊断模型在解释、策略与推导层面的具体失败模式。

**核心方法**：VALG 是一个智能体流水线，将 ML 理论研究组织为“源相对定理分支”（source-relative theorem branch）。其工作流分为两个阶段：第一阶段（形式化前）通过文献调研、视角选择与想法生成，将研究问题具体化为“定理契约”（固定数学设定与唯一目标）；第二阶段（证明与评审）采用 sketch–global–step–assembly 四步流水线：先构造带类型的证明依赖图，再做全局诊断检查定量依赖、收敛模式、对象兼容性与边界行为，然后按依赖序逐条证明局部引理，最后组装成完整手稿。失败时按定位路由到推导、结构或形式化层级的重试。在 COLT 2026 五个开放问题的九个子问题上，VALG 产出 22 个内部定稿的定理候选，其中两个与源问题范围完全匹配，其余七个为受限方法、特例或条件定理。OpenTheoryBench 则从近期 arXiv 论文构建含数百个真实证明问题的开源基准，覆盖依赖规划、定量推理与能力整合。

**与已有工作的关系**：该工作区别于形式化定理证明智能体（如 LeanDojo、DeepSeek-Prover 等），后者以固定形式化目标为前提，不处理问题设定本身的修订；也区别于数学研究智能体（如 Aletheia、Danus 等）——Danus 的共享事实图虽与 VALG 的依赖图相近，但 Danus 在目标给定后终止，而 VALG 显式区分“形式化障碍”与“推导障碍”，并允许因形式化问题生成新的源相关定理分支。与 AI4SLT 等将已有 ML 理论形式化的工作相比，VALG 更早介入，在定理目标尚未固定时工作，并可将定稿分支交给形式化验证流程。

**贡献与边界**：主要贡献是把“未形式化的 ML 理论研究”建模为可评测的智能体任务，并提供了区分源范围匹配、弱化结果与失败分支的评测框架。边界方面：论文评估仅基于 COLT 2026 开放问题的子问题，样本量小且结果多为内部定稿，未给出外部同行验证；OpenTheoryBench 的构建细节与评测指标在官网摘要中未展开。依赖假设包括：源问题需有可检索的文献支撑、定理契约需能形式化表述，且智能体对“源范围”的判断依赖人工或模型对原始问题的理解——若源问题本身模糊，分支分类的可靠性会受影响。

<details><summary>讲者简介</summary>

<p>Dr.Difan Zou is an assistant professor in computer science department and institute of data science at HKU. He has received his PhD degree in Department of Computer Science, University of California, Los Angeles (UCLA). His research interests are broadly in machine learning, deep learning theory, graph learning, mechanism interpretation, and interdisciplinary research between AI and other subjects. His research is published in top‑tier machine learning conferences (ICML, NeurIPS, COLT, ICLR) and journal papers (IEEE Trans., JMLR, Nature Comm., PNAS, etc.). He serves as an area chair/senior PC member for NeurIPS, ICML and AAAI, and PC members for ICLR, COLT, etc.</p>

</details>


### 3. 数学自然语言的形式化与结构化

**讲者**：罗涛（上海交通大学 · 数学科学学院） · 15:00-15:30

**对应论文**：未检索到公开论文（以下为依据报告摘要与讲者方向的推断）

<details><summary>摘要（会议官网）</summary>

<p>人工智能的蓬勃发展正重塑科学研究范式，数学与AI的深度交叉呈现出“双向赋能”的新格局。本报告将汇报团队近期在“Math4AI”（基于数学理论的深度学习机理解析）与“AI4Math”（基于人工智能的数学研究辅助）两个方向的初步探索。在Math4AI层面，我们引入几何测度论、动力系统与渐近分析方法，深入剖析深度学习的训练动力学机制，针对偏微分方程求解中的泛化失效、神经网络训练中的参数凝聚与秩坍缩现象，以及注意力机制中“聚焦-稀释”的多阶段演化规律提供了初步的理论诠释。在AI4Math层面，我们致力于弥合自然语言与形式语言的语义鸿沟，提出了算子树与结构化自然语言等创新性表示框架。该框架不仅显著提升了自动形式化的准确率与语义评估的鲁棒性，更为数学文献的智能检索与学生、专家的交互式研读提供了有力工具。报告最后将展望这一交叉领域的未来挑战与研究愿景。</p>

</details>

*（未检索到公开论文，以下依据报告摘要与讲者方向推断）*

**问题**：数学与AI的交叉被概括为“双向赋能”：一方面，深度学习在偏微分方程求解、注意力机制等场景中仍缺乏可解释的训练动力学理论；另一方面，数学文献的机器阅读与形式化验证受制于自然语言与形式语言之间的语义鸿沟。报告针对这两个方向分别提出理论解析与表示框架需求，属于当前AI4Math与Math4AI交叉领域正在快速成形的议题。

**核心方法**：在Math4AI方向，引入几何测度论、动力系统与渐近分析工具，刻画神经网络训练中的参数凝聚、秩坍缩以及注意力“聚焦-稀释”的多阶段演化，并对PDE求解的泛化失效给出理论诠释。在AI4Math方向，提出“算子树”与“结构化自然语言”两类表示框架，将数学表述拆解为可计算的树状结构，用于提升自动形式化的准确率与语义评估的鲁棒性，并支撑数学文献检索与交互式研读。官网摘要未给出具体模型规模或实验数值。

**与已有工作的关系**：该工作延续了讲者此前在深度学习频率原则、凝聚理论方面的研究脉络，将其拓展到注意力机制与PDE泛化分析；AI4Math部分则与自动形式化、语义评估领域常见的语法树/语义解析路线相关，但“算子树”与“结构化自然语言”的具体构造在摘要中未展开，无法确认其与既有形式化工具（如Lean、Isabelle等）的对接方式。

**贡献与边界**：主要贡献是提出一个贯通“理论解析—表示框架—工具应用”的初步方案，覆盖从训练动力学到数学文献智能处理的链条。边界在于：Math4AI部分仅为“初步理论诠释”，未给出可验证的定量结论；AI4Math部分未报告数据集、对比基线与准确率提升幅度；且未检索到公开论文，因此无法评估其理论假设的适用范围与实现细节。

<details><summary>讲者简介</summary>

<p>罗涛，上海交通大学数学科学学院/自然科学研究院副教授。2012年获上海交通大学致远学院学士学位，2017年获香港科技大学博士学位，并获香港数学会最佳博士论文奖。2017至2020年，担任普渡大学数学系Golomb访问助理教授。研究方向为计算材料科学、深度学习数学理论（Math4AI）和数学智能（AI4Math）。研究内容包括材料科学的 Peierls–Nabarro 模型、Cauchy–Born 法则；深度学习的频率原则、凝聚理论；数学智能的自动形式化、语义评估、结构化自然语言等。在 ARMA/SIAM 系/M3AS/JMLR/NeurIPS/ICML/ICLR 等应用数学和机器学习期刊和会议发表论文 40 余篇。获NeurIPS 2021 Spotlight、NeurIPS 2025 Oral、ICML 2026 Oral等。</p>

</details>


### 4. MechGeo: Autoformalizing and Proving Euclidean Geometry in Lean 4

**讲者**：沈皓（中国科学院大学 · 中国科学院数学与系统科学研究院） · 15:30-16:00

**对应论文**：MechGeo: Autoformalizing and Proving Euclidean Geometry in Lean 4 · [arXiv:2608.02295](https://arxiv.org/abs/2608.02295)

<details><summary>摘要（会议官网）</summary>

<p>We present MechGeo, a Mathlib-native agentic framework for faithful autoformalization and certified proof construction in Euclidean geometry. It combines GeoFormalizer, which translates informal problems into Lean 4 and repairs formal statements, with GeoProver, which integrates geometric reasoning, selective algebraization, and symbolic computation. All proofs and counterexamples are checked by the Lean kernel. On 43 historical IMO geometry problems, MechGeo proves 29 statements generated by GeoFormalizer, refutes the remaining 14 with Lean-verified counterexamples, and proves all 14 after expert repair. Together with IMO 2026 Problem 2, this yields faithful formalizations and kernel-checked proofs for 44 IMO geometry problems. On the 14 geometry statements in LEAP’s Lean-IMOBench, MechGeo proves 12, refutes the remaining two, and proves both repaired statements.</p>

</details>

**问题**：MechGeo 要解决欧氏几何问题从自然语言到 Lean 4 的忠实自动形式化与可信证明构造。官网摘要指出，非形式几何题的语义依赖文本、图形与隐含约定（如“D 在 BC 上”可能指直线、线段或严格介于 B、C 之间，且 B≠C 常被省略），编译器通过并不代表语义正确。随着 Lean 4/Mathlib 成熟和 IMO 级别基准出现，端到端“形式化+证明”成为可检验的目标，而此前多数系统只处理已形式化的陈述，把忠实翻译这一前置难题留给了人工。

**核心方法**：MechGeo 是 Mathlib-native 的 agentic 框架，由 GeoFormalizer 与 GeoProver 组成。GeoFormalizer 先将非形式问题表示为中间语言 GeoIR，再经确定性规则翻译成 Lean 4 语句，并用结构诊断与语义评分迭代修复候选陈述；GeoProver 则先构造几何证明计划，再对合适子目标做选择性代数化，借助 Singular 或 SymPy 生成代数证书，但所有证明与反例最终都由 Lean 内核检查。实验覆盖 7 个 LLM 后端：在 43 个历史 IMO 几何题中，GeoFormalizer 生成的陈述有 29 个被直接证明，14 个被 Lean 验证的反例推翻，经专家修复后全部得证；加上 IMO 2026 Problem 2，共得到 44 个 IMO 几何问题的内核验证证明。在 LEAP 的 Lean-IMOBench 的 14 个几何陈述上，MechGeo 首次证明 12 个，形式化反例 2 个，修复后也全部证明。

**与已有工作的关系**：与 AlphaGeometry、TongGeometry 等使用专用几何语言、依赖符号演绎与学习引导的系统不同，MechGeo 直接生成 Mathlib 语句，证明可复用且由内核验证；与 Eucleant 等自动形式化工具相比，MechGeo 将形式化、语义修复与证明构造统一进同一流程，并加入 Lean 验证的代数化层；与 LeanEuclid、LeanGeo 相比，MechGeo 通过选择性代数化和外部 CAS 证书处理多项式子目标，同时保持几何推理对结构的利用。论文还对比了 AlphaProof、Seed-Prover、DeepSeek-Prover-V2 等通用证明器，但 MechGeo 的定位是几何领域端到端可信自动化。

**贡献与边界**：主要贡献是提出“反例引导诊断 + 选择性代数化 + 内核验证”的实用范式，并给出目前最大的 IMO 几何题 Lean 证明集合。边界同样明显：14 个反例与修复依赖专家介入，说明全自动语义对齐尚未完全解决；反例构造与代数化依赖坐标表示，对三维构型、不等式或含任意多点构造的问题可能失效；官网摘要未给出计算资源、运行时间及失败案例的详细分析，因此难以评估其可扩展性与稳定性。

<details><summary>讲者简介</summary>

<p>中国科学院大学、中国科学院数学与系统科学研究院应用数学博士研究生 研究方向：AI4M、形式化数学、人工智能</p>

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)
