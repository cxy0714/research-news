# ACL 2026 · AI 评测 / Benchmark

> 只收录与「评测 / benchmark」相关的论文：标题命中评测词表（ACL 系另加摘要）后，按**评测方法学价值**打分，取高分做中文精摘。**不是会议全量**。

- 收录 **459** 篇 · 已打分 **459** · 精摘 **30** · 更新于 2026-11-10
- 口径：测量设计 / 构念覆盖 / 污染控制 / 难度校准 / 人类基线 / judge 验证 / 统计可靠性；纯榜单提升不加分。

## 主题分布

| 主题 | 精摘篇数 | 页面 |
|---|---:|---|
| 评测方法学 | 20 | [1](topics/methodology.md) |
| 通用能力评测 | 1 | [1](topics/llm_general.md) |
| Agent / 工具使用 | 5 | [1](topics/agents_tools.md) |
| 多模态评测 | 1 | [1](topics/multimodal.md) |
| 安全 / 事实性 | 1 | [1](topics/safety_factuality.md) |
| 领域基准 | 2 | [1](topics/domain.md) |

## 必读 Top 20

### 1. BenchMarker: An Education-Inspired Toolkit for Highlighting Flaws in Multiple-Choice Benchmarks
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.719/) · [PDF](https://aclanthology.org/2026.acl-long.719.pdf)
- **作者**: Nishant Balepur, Bhavya Rajasekaran, Hyunjin Jane Oh, Michael Xie, Atrey Desai, Vipul Gupta, Steven James Moore, Eunsol Choi et al.
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `evaluation_method`
- **测什么**: MCQA 基准中的污染、捷径和写作错误三类缺陷及其对准确率和排名的影响。
- **摘要**: BenchMarker 是一个受教育学启发的工具包，利用 LLM 作为 judge 来标记多项选择题（MCQA）基准中的三类常见缺陷：污染（题目与网上内容完全一致）、捷径（选项中的线索导致可猜测）和写作错误（基于 19 条教育规则的结构/语法问题）。作者用人类标注验证了该工具，然后对 12 个基准进行了审计，发现污染的 MCQ 往往虚增准确率，而写作错误则降低准确率并可能改变排名。他们还发现，先前的基准修复（如用 LLM 编写干扰项）虽解决了目标问题，却无意中引入了新缺陷（如不可信的干扰项、多个正确答案）。该工具包已发布，旨在连接教育与 NLP 评测领域。
- **为什么值得看**: 提供了一个可复用的缺陷审计流程，将 LLM-as-judge 与人类标注进行一致性验证，并揭示了基准修复可能引入新偏差的机制，对评测方法学有直接价值。
- **关键技术**: `LLM-as-judge`, `human annotation validation`, `contamination audit`, `education rubric`, `benchmark repair analysis`

### 2. Beyond the Leaderboard: Rethinking Medical Benchmarks for Large Language Models
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.1996/) · [PDF](https://aclanthology.org/2026.acl-long.1996.pdf)
- **作者**: Wenxuan Wang, Zizhan Ma, Guo Yu, Yiu-Fai Cheung, Meidan Ding, Jie Liu, Wenting Chen, Linlin Shen
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `evaluation_method`
- **测什么**: 医学 LLM benchmark 在临床保真度、数据完整性和安全评估维度上的质量与效度
- **摘要**: MedCheck 是首个面向医学 LLM benchmark 的生命周期评估框架，将 benchmark 开发解构为从设计到治理的五个阶段，并提供包含 46 条医学定制标准的检查清单。作者用 MedCheck 对 56 个医学 LLM benchmark 进行了深入的实证评估，揭示了普遍存在的系统性问题：与临床实践严重脱节、因污染风险未缓解导致的数据完整性危机，以及系统性忽视安全关键评估维度（如模型鲁棒性和不确定性意识）。该框架既是现有 benchmark 的诊断工具，也是更标准化、可靠和透明的医疗 AI 评估的可行指南。论文的方法学贡献在于提出了一个可复用的 benchmark 质量评估框架，并提供了大规模实证证据。
- **为什么值得看**: 该论文提供了一个可复用的 benchmark 质量评估框架（五阶段、46 条标准），并系统性地诊断了 56 个医学 benchmark 的效度问题（临床保真度、污染、安全维度缺失），对评测方法学中的构念覆盖和测量效度有直接参考价值。
- **关键技术**: `benchmark quality assessment framework`, `lifecycle-oriented evaluation`, `contamination risk audit`, `construct coverage analysis`, `safety dimension checklist`

### 3. BrowseComp-Plus: A Fair and Disentangled Evaluation Benchmark for Deep Search Agents
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.1023/) · [PDF](https://aclanthology.org/2026.acl-long.1023.pdf)
- **作者**: Zijian Chen, Xueguang Ma, Shengyao Zhuang, Ping Nie, Kai Zou, Sahel Sharifymoghaddam, Andrew Liu, Joshua Green et al.
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `benchmark`
- **测什么**: 深度搜索智能体在多跳查询中的端到端准确率，以及检索器对整体性能的独立贡献。
- **摘要**: BrowseComp-Plus 是一个面向深度搜索智能体的评测基准，从 BrowseComp 派生而来，但将黑盒网页搜索 API 替换为固定且经人工验证的语料库，从而解决公平性和可解耦性问题。该基准包含约 1,266 道多跳问题，并配套一个约 1,000 万文档的固定语料库，支持可控的检索实验。评测结果显示，使用 BM25 检索器时，开源模型 Search-R1 的准确率为 3.86%，而 GPT-5 达到 55.9%；当 GPT-5 搭配 Qwen3-Embedding-8B 检索器时，准确率进一步提升至 70.1%，同时减少了搜索调用次数。该基准的主要方法学贡献在于：通过固定语料库，实现了对智能体端到端性能与检索器贡献的分离测量，并提供了可复现的评测流程。
- **为什么值得看**: 该基准为智能体评测提供了可复现的固定语料库设计，解决了黑盒 API 导致的公平性问题，并首次实现了检索器贡献与智能体能力的解耦测量，对评测方法学具有直接价值。
- **关键技术**: `fixed corpus construction`, `human verification`, `disentangled evaluation`, `retriever contribution analysis`, `reproducibility`

### 4. Controllable Contamination Detection for Reliable LLM Evaluation with Statistical Guarantees
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.1390/) · [PDF](https://aclanthology.org/2026.acl-long.1390.pdf)
- **作者**: Zheng Zhang, Qi Liu, Siyuan Liang, Ning Li, Zirui Hu, Weibo Gao, Rui Li, Zhenya Huang et al.
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `evaluation_method`
- **测什么**: 评测数据中污染样本的检测与过滤，控制误保留污染样本的比例（FDR）。
- **摘要**: 本文提出 FTD（FDR-controlled Training Data detection）框架，用于检测并过滤 LLM 评测数据中的污染样本，同时提供统计保证：被误保留为干净的污染样本比例（即错误发现率 FDR）可被控制在用户指定阈值以下。FTD 通过自适应加权策略整合多个互补的检测器，理论上证明在有效控制 FDR 的同时具有较高的统计功效。在真实基准上的实验表明，相比现有方法，FTD 能显著降低残余污染，同时保持评测一致性。该方法针对黑盒 LLM 场景，解决了现有训练数据检测器因黑盒性质而残留污染的问题。
- **为什么值得看**: 该论文为评测污染检测提供了可复用的统计框架，将 FDR 控制引入数据过滤流程，并给出理论保证，对评测方法学中污染控制与统计可靠性具有直接价值。
- **关键技术**: `FDR control`, `adaptive weighting`, `multiple detectors`, `contamination detection`, `statistical guarantee`

### 5. Decentralized Arena: Towards Democratic and Scalable Automatic Evaluation of Language Models
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.1639/) · [PDF](https://aclanthology.org/2026.acl-long.1639.pdf)
- **作者**: Yanbin Yin, Kun Zhou, Zhen Wang, Xiangdong Zhang, Yifei Shao, Shibo Hao, Yi Gu, Jieyuan Liu et al.
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `evaluation_method`
- **测什么**: 衡量 LLM 之间成对比较的偏好一致性，以及排序结果与人类判断的相关性。
- **摘要**: Decentralized Arena 提出一个全自动的分布式评测框架，让所有 LLM 互相进行成对评估，以缓解单一或少数权威模型作为 judge 的偏差。框架包含两个关键组件：粗到细的排序算法，支持新模型的快速增量插入，复杂度低于二次方；以及自动问题选择策略，用于构建新的评测维度。在 66 个 LLM 上的实验显示，其与人类判断的相关性高达 97%，同时大幅降低成本。该方法旨在解决封闭式基准（如 MMLU）的饱和问题，以及众包竞技场（如 Chatbot Arena）依赖昂贵人工 judge 的局限。
- **为什么值得看**: 该论文提供了一种可扩展的民主化 LLM-as-judge 方法，并验证了其与人类判断的一致性（97% 相关性），对评测方法学中 judge 偏差缓解和成本-效度权衡有直接贡献。
- **关键技术**: `LLM-as-judge`, `pairwise evaluation`, `coarse-to-fine ranking`, `question selection`, `human correlation`

### 6. DeepFact: Co-Evolving Benchmarks and Agents for Deep Research Factuality
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.1586/) · [PDF](https://aclanthology.org/2026.acl-long.1586.pdf)
- **作者**: Yukun Huang, Leonardo F. R. Ribeiro, Momchil Hardalov, Bhuwan Dhingra, Markus Dreyer, Venkatesh Saligrama
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `evaluation_method`
- **测什么**: 深度研究报告的声明级事实性（验证器对声明的判断准确性）
- **摘要**: 本文提出 Audit-then-Score (AtS) 方法，用于构建和持续演化深度研究报告（DRR）的声明级事实性评测基准。作者发现，在博士级专家参与的受控研究中，未经辅助的专家对隐藏已知答案声明的标注准确率仅为 60.8%，表明直接标注不可靠。AtS 允许标签和理由在评测过程中被修订：当验证器与当前基准不一致时，可提交证据，由审计员裁决，接受的修订会更新基准后再评分。经过三轮 AtS 迭代，专家准确率提升至 90.9%，说明专家作为审计员优于一次性标注者。基于此，作者发布了 DeepFactBench（带可审计理由的版本化基准）和 DeepFactEval（声明级验证器）。在冻结的 DeepFactBench 上，DeepFactEval 准确率达 83.4%，比最佳深度研究验证器和传统事实核查器分别高 14.3 和 24.9 个百分点，并能迁移到外部事实性数据集。
- **为什么值得看**: 该论文提出了一种可复用的基准演化流程（AtS），解决了专家标注不可靠的问题，并展示了如何通过迭代审计提高标签质量，对评测方法学中的人类基线可靠性和基准动态更新具有重要参考价值。
- **关键技术**: `benchmark construction`, `human baseline`, `iterative auditing`, `claim-level verification`, `transfer evaluation`

### 7. Evaluating Legal Reasoning Traces with Legal Issue Tree Rubrics
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.150/) · [PDF](https://aclanthology.org/2026.acl-long.150.pdf)
- **作者**: Jinu Lee, Kyoung-Woon On, Sophia Simeng Han, Arman Cohan, Julia Hockenmaier
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `benchmark`
- **测什么**: LLM 法律推理轨迹的议题覆盖度和正确性
- **摘要**: 本文提出 LEGIT（LEGal Issue Trees），一个大规模（24K 实例）专家级法律推理数据集，专门用于评估 LLM 生成的推理轨迹质量。作者将法院判决转换为层级树结构，包含对立双方的论点及法院结论，作为评估推理轨迹议题覆盖度和正确性的评分标准（rubrics）。通过人类专家标注和与粗略、信息量较少的评分标准对比，验证了该评分标准的可靠性。实验表明，LLM 的法律推理能力受议题覆盖度和正确性显著影响；RAG 和基于评分标准的 RL 带来互补收益：RAG 提升整体推理能力，而 RL 提升正确性但降低覆盖度。
- **为什么值得看**: 该论文提供了一种将领域知识结构化为层级评分标准（rubrics）的评测方法，并验证了其与人类专家标注的一致性，为复杂推理轨迹的评测提供了可复用的方法论，尤其适用于专家领域。
- **关键技术**: `rubric-based evaluation`, `hierarchical tree structure`, `human expert annotation`, `inter-annotator agreement`, `retrieval-augmented generation`

### 8. From Word Sequences to Behavioral Sequences: Adapting Modeling and Evaluation Paradigms for Longitudinal NLP
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.2182/) · [PDF](https://aclanthology.org/2026.acl-long.2182.pdf)
- **作者**: Adithya V Ganesan, Vasudha Varadarajan, Oscar Kjell, Whitney Ringwald, Scott M. Feltman, Benjamin J. Luft, Roman Kotov, Ryan L. Boyd et al.
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `evaluation_method`
- **测什么**: 纵向NLP模型中个体间差异与个体内动态的预测准确率，以及跨人和跨时间的泛化能力。
- **摘要**: 本文提出面向纵向NLP数据的建模与评测范式，针对传统将文档视为独立无序样本的假设在纵向研究中失效的问题，更新了评测流程的四个部分：按人泛化（横截面）和按时间泛化（前瞻性）的划分、区分个体间差异与个体内动态的准确率指标、默认纳入历史信息的序列输入、以及支持不同历史状态粗粒度的模型内部结构。在238名参与者的17k条每日日记转录与PTSD症状严重度配对数据上，发现传统文档级评测可能产生与生态效度更高的建模和评测截然不同甚至相反的结论。该工作为纵向NLP的评测设计提供了方法学框架，强调从词序列评测转向行为序列评测。
- **为什么值得看**: 该论文直接挑战了标准benchmark的独立同分布假设，提出了面向纵向数据的评测划分和指标设计，对评测方法学中关于样本依赖性和测量效度的讨论具有重要价值。
- **关键技术**: `longitudinal evaluation splits`, `between-person vs within-person metrics`, `sequence modeling`, `ecological validity`

### 9. GenPT: Beyond Self-Report for Reliable LLM Psychometrics via Generative Projective Testing
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.1901/) · [PDF](https://aclanthology.org/2026.acl-long.1901.pdf)
- **作者**: Ming Wang, Shuang Wu, Bixuan Wang, Lu Lin, Yuxin Chen, Xiaocui Yang, Daling Wang, Shi Feng et al.
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `evaluation_method`
- **测什么**: LLM 在人格特质和心理健康风险上的心理测量属性，特别是对污染和方向偏差的鲁棒性。
- **摘要**: GenPT 提出将投射测验范式（TAT、罗夏墨迹、SCT）改造为 LLM 心理测量工具，以应对自陈式问卷（BFI、BDI、MBTI、BSS）在 LLM 评测中的三大威胁：训练语料污染、社会赞许性方向偏差、对上下文不敏感。评估流程分为行为收集、解释、诊断三阶段，基于 SCORS-G 和简化罗夏分析系统进行编码。在人格特质（大五、MBTI）和心理健康风险（抑郁、自杀意念）任务上，问卷在社会赞许性框架下表现出系统性方向偏移（自杀意念最强），而 GenPT 的行为模式保持对称基线；在纵向咨询情境下，GenPT 的抑郁评估偏移比问卷大约一个数量级。在干净人格特质任务上，问卷仍具竞争力。作者公开了代码和刺激材料。
- **为什么值得看**: 该论文为 LLM 评测提供了新的测量范式，系统比较了自陈式与投射式工具在污染抵抗、偏差对称性和上下文敏感性上的差异，对评测方法学中'测量工具效度'问题有直接贡献。
- **关键技术**: `projective testing`, `behavior collection`, `SCORS-G coding`, `contamination resistance`, `bias asymmetry analysis`

### 10. Illusions of the Gold Standard: A Large-scale Analysis of Human Evaluation Protocols for Long-form Text Generation
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.635/) · [PDF](https://aclanthology.org/2026.acl-long.635.pdf)
- **作者**: Katelyn X. Mei, Yi-Li Hsu, Minjoon Choi, Zongwan Cao, Chenjun Xu, Bingbing Wen, Su Lin Blodgett, Lucy Lu Wang
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `analysis`
- **测什么**: 人类评估协议的报告完整性与可复现性
- **摘要**: 本文对 2023–2025 年 *CL 会议中长文本生成任务的人类评估协议进行了大规模分析，旨在揭示评估报告的不透明性。作者人工审阅了 284 篇论文，并借助 LLM 辅助分析了另外 1800+ 篇论文，定义了 20 项与可复现性相关的报告标准，系统检查了社区的报告规范。研究发现，人类评估设计的关键方面（如测量内容、评判者身份、判断解释）普遍报告不足，导致评估结果难以解读和复现。基于这些发现，作者提出了提高透明度和可复现性的具体建议。该研究为人类评估协议的报告提供了可操作的检查清单，对评测方法学具有直接参考价值。
- **为什么值得看**: 该研究系统量化了人类评估报告中的缺失，提供了可复用的 20 项报告标准清单，有助于提升评测的透明度和可复现性，对评测方法学有直接贡献。
- **关键技术**: `human evaluation protocol analysis`, `reporting criteria`, `LLM-assisted analysis`, `manual review`

### 11. Label Effects: Shared Heuristic Reliance in Trust Assessment by Humans and LLM-as-a-Judge
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.1495/) · [PDF](https://aclanthology.org/2026.acl-long.1495.pdf)
- **作者**: Xin Sun, Di Wu, Sijing Qin, Isao Echizen, Abdallah El Ali, Saku Sugawara
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `analysis`
- **测什么**: 来源标签对 LLM 与人类信任判断的启发式偏差
- **摘要**: 本文通过反事实设计检验 LLM-as-a-Judge 的信任判断是否受来源标签（人类撰写 vs AI 生成）影响。实验发现，人类和 LLM 法官对标注为人类撰写的内容给予更高信任，即使内容完全相同。眼动数据显示人类依赖标签作为启发式线索，而 LLM 内部注意力分析显示模型对标签区域的关注密度高于内容区域，且在人类标签下更强，与人类注视模式一致。此外，模型在 AI 标签下的决策不确定性（logits）更高。研究揭示了标签敏感评估的效度问题，并指出对齐人类偏好可能将启发式依赖传播给模型，呼吁去偏评估与对齐。
- **为什么值得看**: 该研究为 LLM-as-judge 的效度提供了具体证据，通过反事实设计和眼动/内部状态分析揭示了标签启发式偏差，对评测方法学中 judge 验证和偏差控制有直接价值。
- **关键技术**: `counterfactual design`, `eye-tracking`, `attention analysis`, `logits uncertainty`, `LLM-as-judge validation`

### 12. LLMEval-Fair: A Large-Scale Longitudinal Study on Robust and Fair Evaluation of Large Language Models
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.972/) · [PDF](https://aclanthology.org/2026.acl-long.972.pdf)
- **作者**: Ming Zhang, Yujiong Shen, Jingyi Deng, Yuhui Wang, Huayu Sha, Kexin Tan, Qiyuan Peng, Yue Zhang et al.
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `evaluation_method`
- **测什么**: 动态评测下模型的知识记忆能力、污染鲁棒性及排名稳定性
- **摘要**: LLMEval-Fair 提出一种动态评测框架，基于 22 万道研究生水平私有题库，每次评测动态采样未见过的测试集，以缓解静态基准的数据污染和榜单过拟合问题。其自动化流程包括抗污染的数据筛选、防作弊架构，以及经校准的 LLM-as-judge 流程，与人类专家的一致性达 90%，并辅以相对排名系统进行公平比较。对近 60 个主流模型进行了为期 30 个月的纵向研究，揭示了知识记忆的性能天花板，并暴露了静态基准无法检测的数据污染漏洞。框架在排名稳定性和一致性上表现出色，为动态评测范式提供了实证支持。
- **为什么值得看**: 该论文提供了动态评测的完整方法论，包括污染检测流程、LLM-as-judge 与人类评分的一致性验证（90% agreement），以及排名稳定性的纵向分析，对评测方法学有直接参考价值。
- **关键技术**: `dynamic benchmark sampling`, `contamination-resistant curation`, `LLM-as-judge calibration`, `relative ranking system`, `longitudinal study`

### 13. Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.2192/) · [PDF](https://aclanthology.org/2026.acl-long.2192.pdf)
- **作者**: Preethi Seshadri, Samuel Cahyawijaya, Ayomide Odumakinde, Sameer Singh, Seraphina Goldfarb-Tarrant
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `evaluation_method`
- **测什么**: LLM模拟用户作为人类用户代理在智能体评测中的可靠性、校准性和公平性
- **摘要**: 该论文通过一项覆盖美国、印度、肯尼亚和尼日利亚参与者的用户研究，系统检验了LLM模拟用户作为智能体评测代理的可靠性。研究基于τ-Bench零售任务，比较了LLM模拟用户与真实人类用户在评估智能体性能时的差异。结果发现，模拟用户缺乏稳健性，不同LLM模拟用户导致的智能体成功率差异高达9个百分点；模拟用户系统性校准偏差，低估困难任务成功率而高估中等难度任务；非洲裔美国英语（AAVE）使用者比标准美语（SAE）使用者成功率更低且校准误差更大，且年龄加剧差异；模拟用户对不同人群的代理有效性不同，对AAVE和印度英语人群表现最差。此外，模拟用户引入对话伪影并暴露与人类用户不同的失败模式。该研究揭示了当前评测实践可能误导对智能体能力的评估，并掩盖真实部署挑战。
- **为什么值得看**: 该论文为LLM-as-user代理评测提供了系统性的效度检验，揭示了模拟用户在不同人群中的测量偏差和校准问题，对评测方法学中代理有效性（proxy validity）和人群公平性具有重要参考价值。
- **关键技术**: `user study`, `LLM-simulated users`, `calibration analysis`, `cross-population fairness`, `proxy validity`

### 14. Macaron: Controlled, Human-Written Benchmark for Multilingual and Multicultural Reasoning via Template-Filling
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.2211/) · [PDF](https://aclanthology.org/2026.acl-long.2211.pdf)
- **作者**: Alaa Elsetohy, Sama Hadhoud, Haryo Akbarianto Wibowo, Chenxi Whitehouse, Genta Indra Winata, Fajri Koto, Alham Fikri Aji
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `benchmark`
- **测什么**: 多语言多文化背景下不同推理类型（如数学、计数）的推理能力，以及语言间性能差距。
- **摘要**: Macaron 是一个模板优先的多语言多文化推理基准，通过 100 个语言无关模板分解推理类型（7 种）和文化方面（22 种），由母语标注者生成英文和本地语言的选择题及系统推导的真假题。数据集包含 11,862 个实例，覆盖 20 个国家/文化背景、10 种文字和 20 种语言（含阿姆哈拉语、约鲁巴语、祖鲁语、吉尔吉斯语等低资源语言）。零样本评估 21 个多语言 LLM，推理模式模型表现最佳（总体 80.8%），英文与本地语言差距小（ΔMC = -1.3%），而开放权重模型在本地语言上显著下降（ΔMC = -6.8%），且在真假题上常接近随机。文化相关的数学和计数模板最难。该基准通过模板填充控制推理类型和文化方面，避免了翻译数据集的英语中心偏差，并提供了系统化的真假题生成方法。
- **为什么值得看**: 该论文展示了如何通过模板填充实现推理类型和文化方面的因子化设计，从而控制构念覆盖并减少语言偏差，为多语言评测提供了可复用的构造方法；同时报告了模型在本地语言上的性能退化，揭示了现有基准可能高估多语言能力。
- **关键技术**: `template-based construction`, `factorized design`, `native annotators`, `multilingual evaluation`, `zero-shot evaluation`

### 15. MedEinst: Benchmarking the Einstellung Effect in Medical LLMs through Counterfactual Differential Diagnosis
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.1847/) · [PDF](https://aclanthology.org/2026.acl-long.1847.pdf)
- **作者**: Wenting Chen, Guolin Huang, Wenxuan Wang, Zhongrui Zhu
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `benchmark`
- **测什么**: 医疗大模型在反事实诊断中对统计捷径的依赖程度（定势效应）
- **摘要**: MedEinst 是一个针对医疗大模型‘定势效应’（Einstellung Effect）的反事实基准，包含 5,383 对临床病例，覆盖 49 种疾病。每对由对照病例和陷阱病例组成，陷阱病例通过改变关键鉴别证据使诊断翻转，用于检测模型是否依赖统计捷径而非患者特异性证据。作者提出 Bias Trap Rate 指标，即正确诊断对照但误诊陷阱的概率，以量化定势易感性。评测发现前沿模型在常规基准上准确率高，但 Bias Trap Rate 严重，表明该失败模式普遍存在。论文还提出 ECR-Agent 方法，通过动态因果推理和批评驱动的图记忆进化来缓解该问题，但基准本身的方法学贡献是核心。
- **为什么值得看**: 该基准针对现有医疗评测的构念覆盖缺口，提供了可复用的反事实病例构造流程和 Bias Trap Rate 指标，能揭示模型在典型病例上的高分可能掩盖对非典型病例的脆弱性，对评测效度分析有直接价值。
- **关键技术**: `counterfactual benchmark construction`, `bias trap rate`, `paired case design`, `evidence audit`, `dynamic causal inference`

### 16. Mediocrity is the key for LLM as a Judge Anchor Selection
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.706/) · [PDF](https://aclanthology.org/2026.acl-long.706.pdf)
- **作者**: Shachar Don-Yehiya, Asaf Yehudai, Leshem Choshen, Omri Abend
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `analysis`
- **测什么**: 锚点选择对LLM-as-judge评估结果与人类排序一致性的影响
- **摘要**: 本文系统研究了LLM-as-judge中锚点选择对评估可靠性的影响，在Arena-Hard-v2.0上评估了22个不同锚点。发现锚点选择至关重要：表现最好和最差的模型作为锚点会显著降低与人类排序的相关性，因为极端锚点很少能区分模型间的相对排名。锚点选择的影响大小与judge模型选择相当。作者进行了功效分析，指出标准基准规模不足以可靠区分竞争模型，并提供了选择信息性锚点的实用指南。
- **为什么值得看**: 该研究揭示了锚点选择作为评估设计中的关键变量，其影响可与judge模型选择相媲美，并提供了功效分析和样本量建议，对评估方法的统计可靠性有直接贡献。
- **关键技术**: `anchor selection`, `power analysis`, `correlation with human rankings`, `benchmark size sufficiency`

### 17. MQM Re-Annotation: A Technique for Collaborative Evaluation of Machine Translation
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.1553/) · [PDF](https://aclanthology.org/2026.acl-long.1553.pdf)
- **作者**: Parker Riley, Daniel Deutsch, Mara Finkelstein, Colten DiIanni, Juraj Juraska, Markus Freitag
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `evaluation_method`
- **测什么**: 机器翻译人工标注的准确性与完整性（错误发现率）
- **摘要**: 该论文提出 MQM 重标注（re-annotation）技术，用于提升机器翻译人工评测的标注质量。在标准 MQM 标注流程后，增加第二阶段，让标注者审阅并修改第一阶段的标注结果，这些结果可能来自自己、其他人类标注者或自动系统。实验表明，重标注行为符合预期，且能显著提高标注质量，主要原因是发现了第一轮遗漏的错误。论文提供了对标注质量提升的量化分析，并探讨了不同来源（自评、他评、自动）的重标注效果差异。
- **为什么值得看**: 该研究直接关注人工评测的标注质量与信度，提出了可复用的两阶段标注流程，并分析了标注者行为，对评测方法学中的人类基线可靠性和标注一致性有具体贡献。
- **关键技术**: `MQM annotation`, `re-annotation`, `human evaluation`, `annotation quality`, `error detection`

### 18. ROSE: An Intent-Centered Evaluation Metric for NL2SQL
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.257/) · [PDF](https://aclanthology.org/2026.acl-long.257.pdf)
- **作者**: Wenqi Pei, Shizheng Hou, Boyan Li, Chen Han, Zhichao Shi, Yuyu Luo
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `evaluation_method`
- **测什么**: 预测 SQL 是否真正回答用户意图，而非与 ground-truth 的语法一致性。
- **摘要**: ROSE 提出一种以用户意图为中心的 NL2SQL 评测指标，替代传统执行准确率（EX）。它采用对抗式 Prover-Refuter 级联：SQL Prover 独立评估预测 SQL 对用户意图的语义正确性，Adversarial Refuter 则利用 ground-truth SQL 作为证据挑战并修正判断。在专家对齐的验证集 ROSE-VEC 上，ROSE 与人类专家的一致性（Cohen's Kappa）比次优指标高出近 24%。作者还对 19 种 NL2SQL 方法进行了大规模重评估，揭示了四个有价值的见解。该工作提供了可复用的指标和验证集，以促进更可靠的 NL2SQL 研究。
- **为什么值得看**: 该论文直接针对现有评测指标（EX）的效度问题，提出了一种新的评测方法，并提供了与人类判断的一致性验证，对评测方法学有具体贡献。
- **关键技术**: `adversarial cascade`, `LLM-as-judge`, `human agreement validation`, `Cohen's Kappa`, `re-evaluation`

### 19. SPENCE: A Syntactic Probe for Detecting Contamination in NL2SQL Benchmarks
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.926/) · [PDF](https://aclanthology.org/2026.acl-long.926.pdf)
- **作者**: Mohammadtaher Safarzadeh, Hitesh Laxmichand Patel, Afshin Oroojlooy, Graham Horwood, Dan Roth
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `evaluation_method`
- **测什么**: NL2SQL 基准测试中模型对句法变体的鲁棒性，以推断训练数据泄漏程度。
- **摘要**: SPENCE 提出一种句法探针框架，用于检测和量化 NL2SQL 基准测试中的训练数据污染。它系统性地为 Spider、SParC、CoSQL 和 BIRD 四个数据集生成测试查询的句法变体，并在执行准确率评分下评估多个高容量 LLM。通过测量随句法差异程度变化的准确率变化（Delta Accuracy），并用 Kendall's tau 和 bootstrap 置信区间量化排名敏感性，作者发现时间梯度：较老的 Spider 基准表现出最强的负向敏感性，提示高泄漏风险，而较新的 BIRD 几乎不受影响。该方法为污染检测提供了可复用的流程，并强调时间情境化评估的重要性。
- **为什么值得看**: 该论文提供了一种可复用的污染检测流程，通过句法扰动和准确率变化分析，为评估基准的泄漏风险提供了量化手段，对评测方法学有直接贡献。
- **关键技术**: `syntactic probing`, `contamination audit`, `delta accuracy`, `Kendall's tau`, `bootstrap confidence intervals`

### 20. Stress Testing Factual Consistency Metrics for Long-Document Summarization
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.1472/) · [PDF](https://aclanthology.org/2026.acl-long.1472.pdf)
- **作者**: Zain Muhammad Mujahid, Dustin Wright, Isabelle Augenstein
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `evaluation_method`
- **测什么**: 长文档摘要事实一致性指标在语义等价扰动下的鲁棒性和对信息密度的敏感性
- **摘要**: 该论文系统评估了六种常用的无参考事实一致性指标在长文档摘要评测中的可靠性，这些指标原本为短文本摘要设计。作者通过七种保持事实性的扰动（如改写、简化、同义词替换、逻辑等价否定、压缩、源文本插入）来探测指标的鲁棒性，并分析其对检索上下文和声明信息密度的敏感性。实验覆盖科幻、法律和科学三个领域的三个长文档基准数据集，结果显示现有短文本指标对语义等价的摘要给出不一致的分数，且对信息密集、与源文档多处语义相似的声明可靠性下降。扩展检索上下文在某些领域提升稳定性，但没有指标在长上下文条件下始终维持事实对齐。论文提出了改进方向，包括多跨度推理、上下文感知校准和基于意义保持变体的训练，以增强长文本摘要评测的鲁棒性。
- **为什么值得看**: 该研究提供了对现有事实性指标在长文档场景下测量效度的系统验证，揭示了指标对语义等价变体的不一致性和信息密度敏感性，为评测方法学中的鲁棒性测试和上下文校准提供了可复用的扰动框架。
- **关键技术**: `perturbation testing`, `factuality-preserving transformations`, `robustness analysis`, `context sensitivity analysis`, `multi-domain evaluation`

## 全部收录

共 459 篇，按分数排序：[1](all.md) · [2](all-2.md) · [3](all-3.md) · [4](all-4.md)
