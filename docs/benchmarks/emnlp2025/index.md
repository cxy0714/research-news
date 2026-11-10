# EMNLP 2025 · AI 评测 / Benchmark

> 只收录与「评测 / benchmark」相关的论文：标题命中评测词表（ACL 系另加摘要）后，按**评测方法学价值**打分，取高分做中文精摘。**不是会议全量**。

- 收录 **315** 篇 · 已打分 **315** · 精摘 **35** · 更新于 2026-11-10
- 口径：测量设计 / 构念覆盖 / 污染控制 / 难度校准 / 人类基线 / judge 验证 / 统计可靠性；纯榜单提升不加分。

## 主题分布

| 主题 | 精摘篇数 | 页面 |
|---|---:|---|
| 评测方法学 | 31 | [1](topics/methodology.md) |
| Agent / 工具使用 | 1 | [1](topics/agents_tools.md) |
| 多模态评测 | 1 | [1](topics/multimodal.md) |
| 安全 / 事实性 | 2 | [1](topics/safety_factuality.md) |

## 必读 Top 20

### 1. Analyzing Uncertainty of LLM-as-a-Judge: Interval Evaluations with Conformal Prediction
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.569/) · [PDF](https://aclanthology.org/2025.emnlp-main.569.pdf)
- **作者**: Huanxin Sheng, Xinyi Liu, Hangfeng He, Jieyu Zhao, Jian Kang
- **会议/来源**: EMNLP 2025 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: LLM-as-judge 评分的预测区间覆盖率和中点分数的偏差
- **摘要**: 本文首次将 conformal prediction 应用于 LLM-as-a-judge 的评分不确定性分析，为离散评分任务设计序数边界调整，构造具有覆盖保证的预测区间。作者提出区间中点作为低偏差的替代分数，并探索 judge 重提示对判断质量的影响。实验覆盖多个 NLG 任务和 LLM judge，验证了区间覆盖的有效性，并分析了中点分数与重提示的实用性。方法学贡献在于为 LLM 评测提供了可复用的不确定性量化框架，弥补了现有评测中缺乏置信区间的不足。
- **为什么值得看**: 为 LLM-as-judge 的评分提供了统计上严格的置信区间，解决了评测中不确定性未量化的问题；其序数边界调整和区间中点方法可直接用于改进评测报告的可靠性。
- **关键技术**: `conformal prediction`, `ordinal boundary adjustment`, `prediction interval`, `judge reprompting`, `coverage guarantee`

### 2. Benchmark Profiling: Mechanistic Diagnosis of LLM Benchmarks
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.789/) · [PDF](https://aclanthology.org/2025.emnlp-main.789.pdf)
- **作者**: Dongjun Kim, Gyuho Shim, Yongchan Chun, Minhyuk Kim, Chanjun Park, Heuiseok Lim
- **会议/来源**: EMNLP 2025 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: benchmark 实际调用的认知能力构成及其对模型性能的贡献
- **摘要**: 本文提出 Benchmark Profiling，一个用于诊断 LLM benchmark 实际测量能力的框架。它将 benchmark 性能分解为十种认知能力，通过梯度重要性评分和参数消融计算 Ability Impact Score (AIS)，量化每种能力对模型在给定 benchmark 上成功的贡献。作者对三个指令微调模型在十个常用 benchmark 上进行剖析，发现：多数 benchmark 依赖多种能力而非单一能力；标签相似的数据集依赖不同的能力组合；代码生成 benchmark 奖励广泛的多技能提升，因此窄领域微调收益有限；与任务无关的能力可能对性能产生负面影响。该框架为 benchmark 审计和模型可解释性提供了透明工具。
- **为什么值得看**: 该论文直接回应了 benchmark 构念效度问题，提供了一种可复用的方法学工具来检验 benchmark 是否真正测量其声称的能力，对评测方法学有重要价值。
- **关键技术**: `gradient-based importance scoring`, `parameter ablation`, `ability impact score`, `benchmark audit`

### 3. Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.511/) · [PDF](https://aclanthology.org/2025.emnlp-main.511.pdf)
- **作者**: Simin Chen, Yiming Chen, Zexin Li, Yifan Jiang, Zhongwei Wan, Yixin He, Dezhi Ran, Tianle Gu et al.
- **会议/来源**: EMNLP 2025 · Main
- 相关性 9/10 · `analysis`
- **测什么**: 梳理数据污染对基准效度的影响，并提出动态基准的设计原则与评估标准。
- **摘要**: 本文是一篇关于大语言模型评测中数据污染问题的综述，系统梳理了从静态基准到动态基准的演进。作者首先分析了增强静态基准的各种方法（如加密、定期更新、私密测试集等），并指出其固有局限，例如加密可被破解、更新成本高、私密测试集难以大规模验证。随后，文章指出现有动态基准缺乏统一的评估标准这一关键缺口，并基于此提出了一系列动态基准设计原则，包括时间戳隔离、动态生成、污染检测流程等。综述还分析了现有动态基准（如FreshQA、LiveBench等）在遵循这些原则方面的不足。作者维护了一个GitHub仓库持续收集静态与动态基准方法。该工作为评测方法学提供了系统性的框架梳理，但作为综述，其提出的设计原则尚未经过实证验证。
- **为什么值得看**: 该综述系统梳理了数据污染检测与动态基准设计的方法学进展，并明确指出现有动态基准缺乏标准化评估标准，为后续建立动态基准的效度验证框架提供了基础。
- **关键技术**: `contamination audit`, `dynamic benchmarking`, `benchmark design principles`, `static benchmark enhancement`

### 4. Beyond the Surface: Measuring Self-Preference in LLM Judgments
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.86/) · [PDF](https://aclanthology.org/2025.emnlp-main.86.pdf)
- **作者**: Zhi-Yuan Chen, Hao Wang, Xinyu Zhang, Enrui Hu, Yankai Lin
- **会议/来源**: EMNLP 2025 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: LLM 作为 judge 时对自己响应的偏好偏差（自偏好偏差），剥离响应质量影响后的净偏差。
- **摘要**: 该论文针对 LLM-as-judge 的自偏好偏差测量提出新方法。现有方法通过比较 judge 模型对自己响应与其他模型响应的评分差来度量偏差，但该差值混淆了偏差与响应质量差异。作者引入 gold judgments（人类或更可靠模型提供的参考答案）作为响应质量的代理，提出 DBG 分数，即 judge 对自己响应的评分与对应 gold judgment 评分之差，从而剥离质量混杂因素。基于 DBG 分数，论文在多个 LLM（不同版本、规模、推理能力）上系统评估自偏好偏差，并探究响应文本风格和 post-training 数据对偏差的影响，还从注意力机制角度分析偏差成因。实验揭示了自偏好偏差的普遍性及其与模型属性、训练数据的关系，并提供了代码和数据。
- **为什么值得看**: 该论文直接针对评测方法学中的偏差测量问题，提出一种可复用的去混杂偏差指标（DBG），并验证了其有效性，对 LLM-as-judge 的效度研究具有重要参考价值。
- **关键技术**: `bias measurement`, `gold judgment`, `confounding control`, `LLM-as-judge`, `attention analysis`

### 5. Can Large Language Models Outperform Non-Experts in Poetry Evaluation? A Comparative Study Using the Consensual Assessment Technique
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.1625/) · [PDF](https://aclanthology.org/2025.emnlp-main.1625.pdf)
- **作者**: Piotr Sawicki, Marek Grzes, Dan Brown, Fabricio Goes
- **会议/来源**: EMNLP 2025 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: LLM在诗歌质量评估中与人类非专家相比的排序准确性和可靠性
- **摘要**: 该研究将艺术评估中的共识评估技术（CAT）改编为LLM诗歌评估方法，使用90首诗的数据集，以发表场所作为地面真值。方法采用小批量随机分组内的强制选择排序，使Claude-3-Opus与地面真值的Spearman秩相关达到0.87，远超非专家人类评估者的0.38。LLM评估还表现出高评分者间信度，表明该方法稳健。研究证明LLM在比较框架下可有效可靠地评估诗歌，为其他创意领域提供借鉴。
- **为什么值得看**: 该论文提供了LLM-as-judge在主观创意评估中的验证流程，包括与人类基线（非专家）的对比、地面真值构建（发表场所）以及评分者间信度分析，对评测方法学中主观任务的judge验证有参考价值。
- **关键技术**: `Consensual Assessment Technique`, `forced-choice ranking`, `inter-rater reliability`, `Spearman rank correlation`, `human baseline`

### 6. CheckEval: A reliable LLM-as-a-Judge framework for evaluating text generation using checklists
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.796/) · [PDF](https://aclanthology.org/2025.emnlp-main.796.pdf)
- **作者**: Yukyung Lee, JoongHoon Kim, Jaehee Kim, Hyowon Cho, Jaewook Kang, Pilsung Kang, Najoung Kim
- **会议/来源**: EMNLP 2025 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 文本生成质量的主观评价一致性（跨评测模型与人类判断的 agreement）
- **摘要**: CheckEval 提出一种基于清单（checklist）的 LLM-as-a-Judge 评测框架，旨在解决现有文本生成评测中评分不一致、跨评测模型 agreement 低、方差大的问题。其核心设计是将主观评价标准分解为一系列二值问题（如“是否包含必要信息”“是否逻辑连贯”），每个问题独立判断，最终汇总为分数。作者在多个数据集上用 12 个评测模型进行实验，发现 CheckEval 与人类判断高度相关，且将跨模型平均 agreement 提升 0.45，同时显著降低评分方差。该方法还提高了可解释性，因为每个二值决策可追溯，便于分析哪些属性驱动了质量判断。论文未报告具体题目数或标注人数，但实验规模涵盖 12 个评测模型和多个数据集。
- **为什么值得看**: 该论文直接针对 LLM-as-judge 的测量可靠性问题，提供了可复用的二值分解协议，并系统比较了跨模型 agreement 与人类相关性，对评测方法学有明确贡献。
- **关键技术**: `checklist-based decomposition`, `binary questions`, `LLM-as-judge`, `inter-annotator agreement`, `variance reduction`

### 7. DCR: Quantifying Data Contamination in LLMs Evaluation
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.1173/) · [PDF](https://aclanthology.org/2025.emnlp-main.1173.pdf)
- **作者**: Cheng Xu, Nan Yan, Shuhao Guan, Changhong Jin, Yuke Mei, Yibing Guo, Tahar Kechadi
- **会议/来源**: EMNLP 2025 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 衡量基准数据中模型记忆污染的风险程度，并校准污染对准确率的影响。
- **摘要**: DCR 提出一个轻量级、可解释的数据污染风险量化框架，从语义、信息、数据、标签四个粒度检测并量化基准数据污染（BDC）。它通过模糊推理系统合成污染分数，生成统一的 DCR Factor，用于将原始准确率调整为污染感知的准确率。在 9 个 LLM（0.5B-72B）上，针对情感分析、假新闻检测和算术推理三个任务验证，调整后的准确率与未污染基线平均误差在 4% 以内。该方法强调计算效率和透明度，旨在将污染评估集成到常规评测流程中。
- **为什么值得看**: 提供了可复用的污染检测与校准流程（DCR Factor），并验证了其在不同模型规模和任务上的有效性，对评测方法学中的污染控制有直接参考价值。
- **关键技术**: `contamination audit`, `fuzzy inference system`, `multi-level detection`, `accuracy adjustment`

### 8. DyePack: Provably Flagging Test Set Contamination in LLMs Using Backdoors
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.776/) · [PDF](https://aclanthology.org/2025.emnlp-main.776.pdf)
- **作者**: Yize Cheng, Wenxiao Wang, Mazda Moayeri, Soheil Feizi
- **会议/来源**: EMNLP 2025 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 模型是否在训练时接触过 benchmark 测试集（即测试集污染）
- **摘要**: DyePack 提出一种基于后门攻击的测试集污染检测框架，无需访问模型内部（loss/logits）即可识别在训练时见过 benchmark 测试集的模型。其核心设计是向测试数据中混入多个带随机目标的后门样本，使得对每个模型的判定都能精确计算假阳性率（FPR），从而在理论上保证不误判，同时为每个检测到的污染案例提供强证据。作者在 MMLU-Pro、Big-Bench-Hard 和 Alpaca 三个数据集上对五个模型进行实验，覆盖多项选择和开放式生成任务；在多项选择任务中，使用八个后门即可在 MMLU-Pro 上以低至 0.000073% 的保证 FPR 检测出所有污染模型，在 Big-Bench-Hard 上为 0.000017%，在开放式生成任务 Alpaca 上使用六个后门达到 0.127% 的 FPR。该方法为污染检测提供了可证明的统计保证，是评测方法学的重要进展。
- **为什么值得看**: 该工作提供了一种可复用的污染检测流程，其精确 FPR 计算为污染判定提供了统计可靠性，解决了现有检测方法缺乏理论保证的问题，对 benchmark 的可信度评估具有直接价值。
- **关键技术**: `backdoor attacks`, `false positive rate control`, `contamination detection`, `stochastic targets`, `black-box detection`

### 9. Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.1006/) · [PDF](https://aclanthology.org/2025.emnlp-main.1006.pdf)
- **作者**: Andong Hua, Kenan Tang, Chenhe Gu, Jindong Gu, Eric Wong, Yao Qin
- **会议/来源**: EMNLP 2025 · Main
- 相关性 9/10 · `analysis`
- **测什么**: 提示模板变化下模型性能的稳定性，以及不同评分方法对敏感性的影响。
- **摘要**: 该论文重新审视了LLM的提示敏感性现象，提出其可能主要源于评测方法而非模型固有缺陷。作者在6个基准（含多项选择和开放生成任务）上，用12种提示模板系统评估了7个模型（如GPT、Gemini系列），对比了启发式评分（log-likelihood、严格答案匹配）与LLM-as-judge两种评估方式。结果显示，启发式方法因忽略同义或改写表达而放大了性能波动，而LLM-as-judge显著降低了跨模板的方差，并提高了模型排名的跨提示一致性。研究提示现代LLM对提示模板的鲁棒性可能被低估，评测设计需警惕评分机制带来的伪敏感性。
- **为什么值得看**: 该研究直接揭示了评测方法（评分机制）如何影响测量结果的有效性，为区分模型真实能力与评测伪影提供了可复用的对比框架，对评测方法学中的构念效度有重要启示。
- **关键技术**: `prompt sensitivity analysis`, `LLM-as-judge`, `heuristic scoring comparison`, `variance analysis`, `ranking correlation`

### 10. Languages Still Left Behind: Toward a Better Multilingual Machine Translation Benchmark
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.1018/) · [PDF](https://aclanthology.org/2025.emnlp-main.1018.pdf)
- **作者**: Chihiro Taguchi, Seng Mai, Keita Kurabe, Yusuke Sakai, Georgina Agyei, Soudabeh Eslami, David Chiang
- **会议/来源**: EMNLP 2025 · Main
- 相关性 9/10 · `analysis`
- **测什么**: 多语言机器翻译基准的构念效度（领域代表性、文化中立性、命名实体依赖）
- **摘要**: 本文针对广泛使用的多语言机器翻译基准 FLORES+ 提出批评，并基于四种语言（阿散蒂契维语、日语、景颇语、南阿塞拜疆语）的深入分析，揭示了该基准在评测效度上的严重缺陷。人类评估发现，许多翻译质量低于其声称的 90% 标准，且标注者报告源句过于领域特定、偏向英语世界文化。作者进一步证明，简单的启发式方法（如复制命名实体）即可获得非平凡的 BLEU 分数，表明评测协议存在漏洞。此外，在自然数据上训练的 MT 模型在 FLORES+ 上表现不佳，但在其领域相关的评测集上却有显著提升，说明基准与实际翻译挑战脱节。基于这些发现，作者主张多语言 MT 基准应使用领域通用、命名实体无关、文化中立的源文本，以更好地反映真实世界的翻译需求。
- **为什么值得看**: 该论文提供了可复用的基准效度审计流程（人类评估、启发式攻击、领域相关对比集），并揭示了现有基准的构念覆盖偏差和饱和问题，对评测方法学有直接价值。
- **关键技术**: `human evaluation`, `heuristic attack`, `domain-relevant evaluation set`, `construct validity audit`

### 11. PERSEVAL: A Framework for Perspectivist Classification Evaluation
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.1137/) · [PDF](https://aclanthology.org/2025.emnlp-main.1137.pdf)
- **作者**: Soda Marem Lo, Silvia Casola, Erhan Sezerer, Valerio Basile, Franco Sansonetti, Antonio Uva, Davide Bernardi
- **会议/来源**: EMNLP 2025 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 模型在个体标注者层面的预测一致性，以及用户特定信息（如社会人口学特征）对模型输出的影响和偏差。
- **摘要**: PersEval 是首个面向 NLP 中视角主义（perspectivist）模型评估的统一框架，旨在替代多数投票的标签聚合方式，将不同标注者的视角视为合法真值。该框架在个体标注者层面评估模型，并明确区分标注者与用户，以贴近真实应用场景。作者基于编码器与解码器模型进行实验，并分析了社会人口学提示（sociodemographic prompting）的影响。框架提供全局、文本级、特质级和用户级四类评估指标，能够揭示模型受用户特定信息影响的程度及由此引入的偏差。实验表明，PersEval 可用于比较不同视角主义方法，并分析其对不同用户和人口统计子群体的影响。
- **为什么值得看**: 该论文提出了一种新的评测框架，将评估粒度从聚合标签细化到个体标注者，并区分标注者与用户，为评测方法学提供了可复用的指标体系和偏差分析工具，尤其适用于主观任务（如仇恨言论、情感分析）的效度研究。
- **关键技术**: `perspectivist evaluation`, `individual-level metrics`, `user-level analysis`, `sociodemographic prompting`, `bias analysis`

### 12. Reliable Evaluation and Benchmarks for Statement Autoformalization
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.907/) · [PDF](https://aclanthology.org/2025.emnlp-main.907.pdf)
- **作者**: Auguste Poiroux, Gail Weiss, Viktor Kunčak, Antoine Bosselut
- **会议/来源**: EMNLP 2025 · Main
- 相关性 9/10 · `benchmark`
- **测什么**: 自然语言数学语句自动形式化的准确性和指标可靠性
- **摘要**: 本文针对自然语言数学语句自动形式化（如翻译为 Lean 4）的评测问题，提出了一套综合方法，包括改进的指标、稳健的基准和系统评估。作者引入 BEq+ 自动指标，与人类判断高度相关，并构建了 ProofNetVerif 数据集（含 3,752 个标注示例）用于评估指标质量。此外，开发了两个新基准：修正版 ProofNet# 和 RLM25（含 619 对来自六个形式化项目的研究级数学题）。系统实验表明，现有技术在本科数学上可达 45.1% 准确率，但在缺乏上下文的研究级内容上表现不佳。该工作为自动形式化系统的可靠评测奠定了基础。
- **为什么值得看**: 该论文提供了可复用的指标验证流程（BEq+ 与人类判断的相关性分析）和基准修正方法（ProofNet#），并揭示了现有基准的缺陷，对评测方法学有直接贡献。
- **关键技术**: `metric validation`, `human correlation`, `benchmark construction`, `dataset annotation`, `error analysis`

### 13. SimulatorArena: Are User Simulators Reliable Proxies for Multi-Turn Evaluation of AI Assistants?
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.1786/) · [PDF](https://aclanthology.org/2025.emnlp-main.1786.pdf)
- **作者**: Yao Dou, Michel Galley, Baolin Peng, Chris Kedzie, Weixin Cai, Alan Ritter, Chris Quirk, Wei Xu et al.
- **会议/来源**: EMNLP 2025 · Main
- 相关性 9/10 · `benchmark`
- **测什么**: 用户模拟器在多大程度上能替代真实用户进行多轮对话评估（行为匹配度和评分一致性）
- **摘要**: SimulatorArena 提出了一个用于评估用户模拟器（user simulator）可靠性的基准，包含 909 条带标注的人机对话，覆盖数学辅导和文档创作两个交互任务。它从两个维度衡量模拟器：生成消息与真实用户行为的匹配度，以及模拟器对助手评分的排序与人类判断的一致性。实验发现，基于用户画像（如背景、消息风格）条件化的模拟器与人类判断高度一致，Spearman 相关系数达 0.7，可作为人类评估的实用替代。作者还使用最佳模拟器对 18 个助手（包括 GPT-5、Claude 4.1 Opus、Gemini 2.5 Pro）进行了基准测试。该工作填补了用户模拟器缺乏系统验证的空白，为多轮对话评估提供了方法学参考。
- **为什么值得看**: 该论文直接针对评测方法学中的代理有效性（proxy validity）问题，系统比较了模拟用户与真实用户的行为和评分一致性，提供了可复用的验证流程和相关性指标，对依赖 LLM 模拟的自动评估设计具有重要参考价值。
- **关键技术**: `benchmark construction`, `human-LLM conversation annotation`, `Spearman correlation`, `user profile conditioning`, `assistant rating alignment`

### 14. SMART: Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.1274/) · [PDF](https://aclanthology.org/2025.emnlp-main.1274.pdf)
- **作者**: Alexander Scarlatos, Nigel Fernandez, Christopher Ormerod, Susan Lottridge, Andrew Lan
- **会议/来源**: EMNLP 2025 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 预测开放式题目的难度参数（IRT 难度）
- **摘要**: SMART 提出一种用模拟学生预测题目难度的方法，面向开放式题目，解决传统 IRT 需要真实学生作答、无法用于冷启动的问题。方法核心是用 DPO 对齐模拟学生与指定能力水平，偏好对基于真实 IRT 模型下的响应似然构建；随后生成数千条模拟响应，用 LLM 评分模型评估，再拟合 IRT 模型得到难度估计。在两个真实学生响应数据集上，SMART 优于其他难度预测方法，表明能力对齐是关键。该方法为评测中的题目难度校准提供了无需真实作答的替代方案，但依赖 LLM 评分模型的可靠性。
- **为什么值得看**: 该方法为 benchmark 题目难度预测提供了一种可复用的模拟流程，将 IRT 与 LLM 结合，可用于冷启动场景下的难度校准，对评测方法学中的题目选择与难度控制有直接价值。
- **关键技术**: `item response theory`, `direct preference optimization`, `LLM-as-judge`, `simulated students`, `cold-start difficulty prediction`

### 15. The Illusion of Progress: Re-evaluating Hallucination Detection in LLMs
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.1761/) · [PDF](https://aclanthology.org/2025.emnlp-main.1761.pdf)
- **作者**: Denis Janiak, Jakub Binkowski, Albert Sawczyn, Bogdan Gabrys, Ravid Shwartz-Ziv, Tomasz Jan Kajdanowicz
- **会议/来源**: EMNLP 2025 · Main
- 相关性 9/10 · `meta_evaluation`
- **测什么**: 幻觉检测方法在人类对齐指标下的真实性能，以及评测指标（ROUGE）的效度。
- **摘要**: 该论文重新评估了LLM幻觉检测方法的评测方式，指出广泛使用的ROUGE指标基于词法重叠，与人类判断不一致。通过人类研究，作者发现ROUGE虽然召回率高，但精确度极低，导致对检测方法性能的高估；改用LLM-as-Judge等语义对齐指标后，若干既有检测方法的性能下降高达45.9%。此外，基于响应长度的简单启发式方法竟能与复杂检测技术匹敌，暴露了当前评测实践的根本缺陷。论文主张采用语义感知且稳健的评测框架，以准确衡量幻觉检测的真实性能。
- **为什么值得看**: 该研究提供了对评测指标（ROUGE）效度的系统性验证，通过人类基线对比揭示了指标偏差，并量化了LLM-as-Judge与人类判断的一致性，对评测方法学有直接贡献。
- **关键技术**: `human study`, `LLM-as-judge`, `metric validation`, `baseline comparison`

### 16. A Causal Lens for Evaluating Faithfulness Metrics
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.1496/) · [PDF](https://aclanthology.org/2025.emnlp-main.1496.pdf)
- **作者**: Kerem Zaman, Shashank Srivastava
- **会议/来源**: EMNLP 2025 · Main
- 相关性 8/10 · `evaluation_method`
- **测什么**: 衡量解释忠实度指标区分忠实与不忠实解释的诊断能力
- **摘要**: 该论文提出 Causal Diagnosticity，一个用于评估自然语言解释忠实度指标（faithfulness metrics）的测试框架。它利用模型编辑（model editing）方法生成忠实与不忠实的解释配对，从而在受控条件下检验指标能否区分二者。基准涵盖四个任务：事实核查、类比、物体计数和多跳推理，并评估了包括事后解释和思维链在内的多种主流忠实度指标。结果显示，诊断性能因任务和模型而异，Filler Tokens 指标总体表现最佳；连续指标通常比二值指标更具诊断性，但对噪声和模型选择敏感。该工作为忠实度指标的对比提供了原则性方法，并揭示了现有指标的鲁棒性不足。
- **为什么值得看**: 该工作为评估指标本身提供了可复用的测试框架（testbed），通过因果干预（模型编辑）构造 ground-truth 忠实度标签，避免了依赖人类判断或模型自评的间接性，对评测方法学中的指标验证具有直接参考价值。
- **关键技术**: `model editing`, `causal intervention`, `paired generation`, `diagnosticity`, `benchmark construction`

### 17. A Fully Probabilistic Perspective on Large Language Model Unlearning: Evaluation and Optimization
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.452/) · [PDF](https://aclanthology.org/2025.emnlp-main.452.pdf)
- **作者**: Anda Cheng, Wei Huang, Yinggui Wang
- **会议/来源**: EMNLP 2025 · Main
- 相关性 8/10 · `evaluation_method`
- **测什么**: 大模型遗忘后对语义相似输入的信息泄露风险（概率化度量）
- **摘要**: 本文提出一个全概率评估框架（FPE）用于大模型遗忘（LLMU），针对现有确定性评估过于乐观的问题。FPE 通过输入分布采样（IDS）生成语义相似但多样的输入，并对每个输入进行多次采样，从而获得概率化的信息泄露风险度量。作者还提出对比嵌入损失（CEL）改进遗忘效果，通过对比学习拉远遗忘样本与对比样本的表示，同时对齐随机向量。实验在 Llama-2-7B 上显示 FPE 能发现更多泄露风险，CEL 将遗忘效果提升至少 50.1%，鲁棒性提升至少 37.2%，同时保持模型效用。该工作为遗忘评估提供了概率化视角，但未涉及人类基线或污染检查。
- **为什么值得看**: 该工作挑战了确定性评估的乐观偏差，提出概率化评估框架，为测量信息泄露风险提供了更严格的方法，对评测方法学有直接贡献。
- **关键技术**: `probabilistic evaluation`, `input distribution sampling`, `contrastive learning`, `unlearning robustness`

### 18. A Necessary Step toward Faithfulness: Measuring and Improving Consistency in Free-Text Explanations
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.797/) · [PDF](https://aclanthology.org/2025.emnlp-main.797.pdf)
- **作者**: Lingjun Zhao, Hal Daumé III
- **会议/来源**: EMNLP 2025 · Main
- 相关性 8/10 · `evaluation_method`
- **测什么**: 自由文本解释与模型预测之间的一致性（支持或反对程度）
- **摘要**: 本文提出一种衡量自由文本解释与预测之间一致性的指标 PEX consistency，基于证据权重（weight of evidence）的扩展，量化解释对预测的支持或反对程度。作者在多个 LLM 生成解释的数据集上分析发现，超过 62% 的解释缺乏这种一致性。通过直接偏好优化（DPO）训练，三个模型家族的解释一致性提升 43.1% 至 292.3%，同时解释忠实度最高提升 9.7%。该指标无需人工标注，可自动计算，为解释忠实度提供了一种可操作的量化方法。
- **为什么值得看**: 该研究提出了一种新的自动评估指标，用于量化解释与预测的一致性，并验证了其与人类评估的相关性，为解释忠实度的测量提供了可复用的方法学框架。
- **关键技术**: `weight of evidence`, `consistency metric`, `direct preference optimization`, `automatic evaluation`

### 19. Agent-as-Judge for Factual Summarization of Long Narratives
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.1204/) · [PDF](https://aclanthology.org/2025.emnlp-main.1204.pdf)
- **作者**: Yeonseok Jeong, Minsoo Kim, Seung-won Hwang, Byung-Hak Kim
- **会议/来源**: EMNLP 2025 · Main
- 相关性 8/10 · `evaluation_method`
- **测什么**: 长叙事摘要的事实性，包括角色关系与状态的准确性。
- **摘要**: NarrativeFactScore (NFS) 是首个针对长叙事文本（>100K tokens）摘要事实性评估的 Agent-as-a-Judge 框架。它从输入叙事中抽取角色知识图谱（CKG），基于该图谱评估摘要的事实性，并提供可操作的修正建议（如缺失或错误事实）。实验表明，构建 CKG 使事实性计算量降至先前方法的 1/3，同时与人类判断的相关性提高三倍；利用建议进行摘要精炼能显著提升质量。该工作针对传统指标（ROUGE/BERTScore）和 LLM-as-a-Judge 在长叙事中角色关系理解不足的问题，提出结构化知识引导的评估范式。
- **为什么值得看**: 该工作将评测从纯文本判断转向结构化知识图谱引导，展示了如何通过外部知识注入提升 LLM-as-Judge 的事实性评估效度，并提供了计算成本与人类相关性之间的权衡证据，对评测方法学有直接参考价值。
- **关键技术**: `Agent-as-a-Judge`, `Character Knowledge Graph`, `factuality evaluation`, `human correlation`, `refinement guidance`

### 20. Are Checklists Really Useful for Automatic Evaluation of Generative Tasks?
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.538/) · [PDF](https://aclanthology.org/2025.emnlp-main.538.pdf)
- **作者**: Momoka Furuhashi, Kouta Nakayama, Takashi Kodama, Saku Sugawara
- **会议/来源**: EMNLP 2025 · Main
- 相关性 8/10 · `analysis`
- **测什么**: 自动生成的checklist在成对比较和直接打分中对评估准确性的影响及其与人类评分的一致性。
- **摘要**: 本文系统研究了自动生成的checklist在生成任务自动评估中的有效性，比较了六种生成方法、八种模型规模，并在成对比较和直接打分两种任务上进行了实验。研究发现，选择性使用checklist在成对比较中能提升评估性能，但在直接打分中效果不稳定。进一步分析表明，即使与人类评分相关性低的checklist项也常反映人类标准，暗示人类评估本身存在不一致性。作者据此强调需要更明确地定义客观评估标准，以指导人类和自动评估。
- **为什么值得看**: 该研究为LLM-as-judge的prompt设计提供了实证依据，揭示了checklist使用的条件性效果，并指出了人类评估标准的不一致性，对评测方法学中judge验证和标准制定有直接参考价值。
- **关键技术**: `checklist generation`, `pairwise comparison`, `direct scoring`, `correlation analysis`, `human evaluation`

## 全部收录

共 315 篇，按分数排序：[1](all.md) · [2](all-2.md) · [3](all-3.md)
