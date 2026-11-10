# AAAI 2026 · 多模态评测

> 本页 34 篇（该主题共 34 篇），按相关性排序。 [返回总览](../index.md)

### 1. Do Large Language Models Reason About Uncertainty Like Humans? A Benchmark on Hurricane Forecast Visualization Comprehension
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38812) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38812/42774)
- **作者**: Le Liu, Yuhao Wang, Bohan Shen, Wei Zeng, Shizhou Zhang, Di Xu, Peng Wang
- **会议/来源**: AAAI 2026 · Track 21
- 相关性 9/10 · `benchmark`
- **测什么**: 人类与 LLM 在不确定性可视化（飓风路径）上的推理能力及认知偏差复现程度
- **摘要**: UnReason 是首个系统比较人类与 LLM 在飓风预报不确定性可视化上推理能力的基准。它包含两个递进阶段、七种可视化格式、六个真实飓风案例，以及三类主体（人类、有上下文 LLM、无上下文 LLM），共 880 张可视化图和 117,600 个结构化问答对，并在匹配的评估条件下进行。阶段一评估隐式和显式不确定性编码下的推理，阶段二考察单一与多维不确定性表征下的推理。研究全面评估了损失估计、推理策略和理解模式，发现 LLM 对不确定性有更强的语义和概念理解，较少被视觉变异性误导，但在决策时仍复现了人类的关键偏差。该基准为在不确定性丰富的视觉推理任务中校准 LLM 行为与人类认知提供了洞见。
- **为什么值得看**: 该基准提供了跨主体（人类 vs. LLM）的匹配评估设计，可复用于检验 LLM 是否复现人类认知偏差，并揭示了 LLM 在不确定性理解上的优势与局限，对评测方法学中的人类基线与构念效度有直接价值。
- **关键技术**: `matched evaluation conditions`, `human baseline`, `multi-phase task design`, `structured QA pairs`, `cross-agent comparison`

### 2. CausalStep: A Benchmark for Explicit Stepwise Causal Reasoning in Videos
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37582) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37582/41544)
- **作者**: Xuchen Li, Xuzhao Li, Shiyu Hu, Kaiqi Huang, Wentao Zhang
- **会议/来源**: AAAI 2026 · Track 8
- 相关性 8/10 · `benchmark`
- **测什么**: 视频中显式逐步因果推理的能力，包括因果单元识别和顺序推理的鲁棒性。
- **摘要**: CausalStep 是一个面向视频显式逐步因果推理的基准，包含 100 个视频（6 个类别）和 1,852 个多项选择问答对。它通过将视频分割为因果关联单元，并采用严格的逐步问答协议，要求模型按顺序作答，从而防止利用全局上下文取巧。每个问题基于错误类型分类法构造干扰项，以增强诊断价值。作者引入七个诊断指标，用于细粒度评估因果推理能力。实验对比了领先的专有和开源模型及人类基线，发现当前模型与人类逐步推理能力差距显著。该基准为视频因果推理提供了严格的评测框架，但规模较小，且未报告污染检查或人类基线标注细节。
- **为什么值得看**: 该基准通过逐步问答协议和基于错误类型的干扰项设计，展示了如何防止捷径解并提升诊断效度，对视频推理评测方法有参考价值；但其规模有限，且未提供污染检查或人类基线信度分析，限制了其方法学贡献的推广。
- **关键技术**: `stepwise QA protocol`, `error type taxonomy`, `diagnostic metrics`, `human baseline`

### 3. CrossVid: A Comprehensive Benchmark for Evaluating Cross-Video Reasoning in Multimodal Large Language Models
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37550) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37550/41512)
- **作者**: Jingyao Li, Jingyun Wang, Molin Tan, Haochen Wang, Cilin Yan, Likun Shi, Jiayin Cai, Xiaolong Jiang et al.
- **会议/来源**: AAAI 2026 · Track 8
- 相关性 8/10 · `benchmark`
- **测什么**: 多模态模型跨视频时空推理与信息聚合能力
- **摘要**: CrossVid 是首个专门评估多模态大模型跨视频推理（CVR）能力的基准，要求模型同时理解多段视频并聚合、比较信息。基准包含四个高层维度和十个具体任务，覆盖 5,331 个视频和 9,015 个问答对，题型包括单选、多选和开放题。实验显示 Gemini-2.5-Pro 表现最佳，平均准确率仅 50.4%，多数模型因无法整合跨视频证据而表现不佳。该基准提供了分层任务设计和多题型覆盖，但未报告人类基线或污染检查，方法学贡献有限。
- **为什么值得看**: 该基准填补了跨视频推理评测的空白，其分层任务设计可作为多视频聚合能力的构念覆盖参考，但缺乏人类基线和污染控制，限制了其作为测量工具的效度论证。
- **关键技术**: `benchmark construction`, `hierarchical task design`, `multi-choice QA`

### 4. DISCODE: Distribution-Aware Score Decoder for Robust Automatic Evaluation of Image Captioning
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37440) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37440/41402)
- **作者**: Nakamasa Inoue, Kanoko Goto, Masanari Oi, Martyna Gruszka, Mahiro Ukai, Takumi Hirose, Yusuke Sekikawa
- **会议/来源**: AAAI 2026 · Track 7
- 相关性 8/10 · `evaluation_method`
- **测什么**: 图像描述评估指标在跨领域场景下与人类判断的一致性
- **摘要**: DISCODE 提出一种免微调的图像描述自动评估方法，旨在提升 LVLM 评估器在跨领域场景下的鲁棒性。其核心是测试时自适应评估，引入 Adaptive Test-Time (ATT) 损失，利用高斯先验分布约束评分解码，并推导出解析解以高效优化。作者还构建了 MCEval 基准，覆盖六个不同领域，用于检验评估指标的鲁棒性。实验表明，DISCODE 在 MCEval 及四个现有基准上达到参考无关评估指标的最优性能。该方法为评估指标的领域迁移问题提供了新的解决思路，但未涉及人类基线或 judge 验证的详细分析。
- **为什么值得看**: 该论文针对评估指标在领域偏移下的鲁棒性问题，提出测试时自适应方法，并构建多领域基准，为评测方法学提供了可复用的领域鲁棒性检验框架。
- **关键技术**: `test-time adaptation`, `Gaussian prior`, `reference-free evaluation`, `multi-domain benchmark`

### 5. EvalMuse-40K: A Fine-Grained Benchmark with Comprehensive Human Annotations for Text-to-Image Generation Model Alignment Evaluation
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/42458) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/42458/46419)
- **作者**: Shuhao Han, Haotian Fan, Jiachen Fu, Liang Li, Tao Li, Junhui Cui, Yunqiu Wang, Yang Tai et al.
- **会议/来源**: AAAI 2026 · Track 6
- 相关性 8/10 · `benchmark`
- **测什么**: 文本到图像生成模型的图像-文本细粒度对齐能力（对象、属性、关系等）。
- **摘要**: EvalMuse-40K 是一个用于文本到图像（T2I）生成模型对齐评估的细粒度基准，包含 40K 个图像-文本对，并带有细粒度的人类标注，覆盖对象、属性、关系等对齐相关元素。构建过程中采用了平衡提示采样和数据重新标注等策略，以确保数据集的多样性和可靠性。基于该数据集，作者提出了 FGA-BLIP2，一种仅输入图像和文本即可实现细粒度对齐评估的高效自动方法，无需对每个细粒度元素进行视觉问答。实验表明，FGA-BLIP2 在多个图像-文本对齐数据集上取得了良好性能，并可作为奖励模型用于改进 T2I 模型的对齐能力。该工作主要贡献在于提供了大规模细粒度标注数据集和高效评估方法，但未涉及污染检查或人类基线校准等评测方法学细节。
- **为什么值得看**: 该论文提供了一个大规模、细粒度标注的基准数据集，并验证了自动评估方法的效率与有效性，对评测方法学中'细粒度构念覆盖'和'评估成本'问题有参考价值，但缺乏对评估方法本身的统计可靠性或偏差分析。
- **关键技术**: `benchmark construction`, `human annotation`, `balanced sampling`, `data re-annotation`, `efficient evaluation`

### 6. FineVAU: A Novel Human-Aligned Benchmark for Fine-Grained Video Anomaly Understanding
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37790) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37790/41752)
- **作者**: Joao Alexandre Cardeira Pereira, Vasco Lopes, João C. Neves, David Semedo
- **会议/来源**: AAAI 2026 · Track 10
- 相关性 8/10 · `benchmark`
- **测什么**: 视频异常理解中事件、实体和位置的细粒度视觉元素覆盖度
- **摘要**: FineVAU 是一个面向细粒度视频异常理解（VAU）的新基准，将任务分解为事件（What）、参与实体（Who）和位置（Where）三个维度。作者提出 FV-Score 指标，通过检测 LVLM 回答中是否包含关键视觉元素来评估事实相关性，而非仅依赖语言质量；同时构建了 FineW³ 数据集，通过全自动流程扩充现有标注，加入细粒度视觉信息。人类评估显示 FV-Score 与人类对异常的感知一致性优于 BLEU/ROUGE-L 和 LLM-based 评估。实验揭示 LVLM 在需要空间和细粒度时间理解的异常事件上存在明显缺陷，尽管在粗粒度、静态信息和强视觉线索事件上表现良好。
- **为什么值得看**: 该论文提出了一种新的评估指标 FV-Score，并验证了其与人类判断的一致性，为视频异常理解任务提供了可复用的细粒度评估方法，同时揭示了现有 n-gram 和 LLM-based 指标在事实相关性上的不足。
- **关键技术**: `benchmark construction`, `human evaluation`, `metric validation`, `fine-grained annotation`, `LLM-based evaluation comparison`

### 7. JRDB-Reasoning: A Difficulty-Graded Benchmark for Visual Reasoning in Robotics
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37443) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37443/41405)
- **作者**: Simindokht Jahangard, Mehrzad Mohammadi, Yi Shen, Zhixi Cai, Hamid Rezatofighi
- **会议/来源**: AAAI 2026 · Track 7
- 相关性 8/10 · `benchmark`
- **测什么**: 视觉语言模型在多人场景中不同复杂度下的视觉推理能力。
- **摘要**: JRDB-Reasoning 是一个面向机器人视觉推理的难度分级基准，基于 JRDB 数据集扩展了人-物交互和几何关系标注。它形式化了推理复杂度的定义，并引入自适应查询引擎，可生成不同难度、可定制的题目，且附带逐步推理的工作流标注。基准包含约 1,000 个问题，覆盖多个难度层级，用于细粒度评估视觉语言模型（VLMs）的推理能力。论文报告了多个 VLM 在基准上的表现，显示模型在低难度任务上表现较好，但在高难度任务上显著下降，验证了难度分级的有效性。方法学贡献在于提供了可复用的推理复杂度定义和查询引擎，但未报告人类基线或污染检查。
- **为什么值得看**: 该论文提出了推理复杂度的形式化定义和自适应查询引擎，为视觉推理基准的难度校准提供了可复用的方法学框架，但缺乏人类基线和污染检查，限制了其效度论证的完整性。
- **关键技术**: `difficulty grading`, `adaptive query engine`, `step-by-step reasoning annotations`, `benchmark construction`

### 8. LongT2IBench: A Benchmark for Evaluating Long Text-to-Image Generation with Graph-structured Annotations
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38168) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38168/42130)
- **作者**: Zhichao Yang, Tianjiao Gu, Jianjie Wang, Feiyu Lin, Xiangfei Sheng, Pengfei Chen, Leida Li
- **会议/来源**: AAAI 2026 · Track 14
- 相关性 8/10 · `benchmark`
- **测什么**: 长文本到图像生成中图像与文本的细粒度对齐程度（实体、属性、关系层面）。
- **摘要**: LongT2IBench 是一个面向长文本到图像（T2I）生成的对齐评测基准，包含 14K 个长文本-图像对，并配有图结构的人工标注。针对长提示细节密集的特点，作者设计了 Generate-Refine-Qualify 标注协议，将长提示转换为包含实体、属性和关系的文本图结构，并基于这些细粒度元素进行对齐标注。标注结果可转化为对齐分数和解释，支持可解释的评测。基于该基准，作者提出 LongT2IExpert，通过层级对齐链式思维（CoT）指令微调多模态大模型，使其能输出定量分数和结构化解释。实验表明 LongT2IExpert 在评估对齐和解释方面优于现有方法。该工作为长 T2I 评测提供了细粒度、可解释的标注方案，但未报告人类基线一致性或污染检查。
- **为什么值得看**: 该基准将长提示分解为图结构，实现了细粒度、可解释的对齐标注，为评测长文本条件下的图像生成提供了新的构念操作化方法，并展示了如何将结构化标注转化为可训练的评估模型。
- **关键技术**: `graph-structured annotation`, `chain-of-thought`, `instruction tuning`, `human annotation protocol`

### 9. Multigranular Evaluation for Brain Visual Decoding
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38845) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38845/42807)
- **作者**: Weihao Xia, Cengiz Oztireli
- **会议/来源**: AAAI 2026 · Track 21
- 相关性 8/10 · `evaluation_method`
- **测什么**: 脑视觉解码结果在结构保真度、语义对齐和上下文连贯性上的多粒度视觉相似度。
- **摘要**: 该论文提出 BASIC，一个针对脑视觉解码的统一多粒度评测框架，旨在弥补现有粗粒度指标（如像素级或高层语义相似度）无法区分模型间细微差异、缺乏神经科学依据的不足。框架在结构层面引入基于分割的分层指标套件，包括前景、语义、实例和组件掩码，并通过粒度感知的对应关系量化结构保真度；在语义层面利用多模态大语言模型提取包含对象、属性和关系的结构化场景表示，实现与真实刺激的详细、可扩展且上下文丰富的比较。作者在多个刺激-神经影像数据集上对多种视觉解码方法进行了基准测试，验证了该框架的判别力、可解释性和全面性。论文的主要贡献在于提出了一种新的评测方法学，而非报告特定模型的性能。
- **为什么值得看**: 该论文直接回应了评测方法学中的核心问题：粗粒度指标导致的测量不敏感和构念覆盖不足。它通过分层结构指标和LLM提取的语义表示，提供了更细粒度和可解释的评测维度，并展示了跨数据集的可复用性，对评测设计具有方法论价值。
- **关键技术**: `multigranular evaluation`, `segmentation-based metrics`, `LLM-based scene representation`, `cross-dataset benchmarking`

### 10. Seeing from Another Perspective: Evaluating Multi-View Understanding in MLLMs
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38188) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38188/42150)
- **作者**: Chun-Hsiao Yeh, Chenyu Wang, Shengbang Tong, Ta-Ying Cheng, Ruoyu Wang, Tianzhe Chu, Yuexiang Zhai, Yubei Chen et al.
- **会议/来源**: AAAI 2026 · Track 14
- 相关性 8/10 · `benchmark`
- **测什么**: 多视角场景理解能力，包括跨视角物体对应和空间布局推理。
- **摘要**: 该论文提出 All-Angles Bench，一个用于评估多模态大语言模型（MLLM）多视角理解能力的基准。基准包含来自 90 个真实世界场景的 2100 多个问答对，由人工精心标注，覆盖跨视角物体对应、空间布局推理等任务。作者在 38 个通用及 3D 空间推理 MLLM 上进行了广泛评估，发现模型与人类表现存在显著差距。通过错误分析，他们识别出两个核心失败模式：跨视角物体不匹配和跨视角空间错位，表明当前 MLLM 缺乏多视角感知能力。该基准为构建空间智能体提供了诊断工具，并强调需要架构层面的创新而非仅提示调优。
- **为什么值得看**: 该基准提供了针对多视角理解这一特定构念的评测设计，并进行了失败模式分析，有助于理解 MLLM 在空间推理上的测量效度；其人工标注流程和错误分类可作为类似空间评测的参考。
- **关键技术**: `benchmark construction`, `human annotation`, `failure mode analysis`, `cross-view correspondence`

### 11. Video SimpleQA: Towards Factuality Evaluation in Large Video Language Models
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37249) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37249/41211)
- **作者**: Meng Cao, Pengfei Hu, Yingyao Wang, Jihao Gu, Haoran Tang, Haoze Zhao, Chen Wang, Jiahua Dong et al.
- **会议/来源**: AAAI 2026 · Track 4
- 相关性 8/10 · `benchmark`
- **测什么**: 视频理解中多跳事实性问答的准确性与置信度校准
- **摘要**: Video SimpleQA 是首个面向视频大模型（LVLM）的事实性评测基准，包含约 500 道多跳事实性问答题，要求模型结合视频外部知识并严格基于时间片段作答，答案设计为短格式、无歧义，以降低评分方差。每个问题附带逐跳的子问题，支持细粒度的逐步评估。作者在 33 个 LVLM 上进行了评测，最佳模型 o3 的 F-score 仅 66.3%，显示当前模型事实遵循能力不足；多数模型过度自信，自报置信度高于实际准确率；RAG 能一致提升性能但增加推理开销；多跳问答性能显著低于单跳子问题，首跳物体/事件识别是主要瓶颈。该基准在构造上强调时间定位、外部知识整合和严格事实性，并提供了逐跳分解的评估设计，对视频事实性评测方法有参考价值。
- **为什么值得看**: 该基准在评测设计上提供了多跳问题分解为单跳子问题的细粒度评估框架，并报告了模型置信度与准确率的校准差距，对评测方法学中的构念覆盖和测量误差分析有借鉴意义。
- **关键技术**: `multi-hop QA decomposition`, `temporal grounding`, `short-form answer design`, `confidence calibration analysis`, `RAG evaluation`

### 12. Your AI-Generated Image Detector Can Secretly Achieve SOTA Accuracy, If Calibrated
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38146) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38146/42108)
- **作者**: Muli Yang, Gabriel James Goenawan, Henan Wang, Huaiyuan Qin, Chenghao Xu, Yanhua Yang, Fen Fang, Ying Sun et al.
- **会议/来源**: AAAI 2026 · Track 14
- 相关性 8/10 · `evaluation_method`
- **测什么**: AI生成图像检测器在分布偏移下的决策阈值校准鲁棒性
- **摘要**: 该论文针对AI生成图像检测器在测试时系统性偏向将假图判为真的问题，提出基于贝叶斯决策理论的后验校准框架。作者假设该偏差源于训练时学到的隐式先验与测试时假样本分布偏移，导致决策阈值错位。方法是在冻结骨干网络的前提下，于目标分布的小型验证集上优化一个可学习的标量logit修正项，无需真实标签即可重新对齐决策边界。实验在多个挑战性基准上验证了该方法能显著提升鲁棒性，且无需重训练。论文提供了理论支撑和轻量级解决方案，但未给出具体数据集规模、模型数量等可核对数字。
- **为什么值得看**: 该工作揭示了AI生成图像检测评测中一个被忽视的测量问题——训练集平衡但测试时存在分布偏移导致的系统性误判，并提供了可复用的后验校准流程，对评测方法学中决策阈值校准与分布偏移控制有直接参考价值。
- **关键技术**: `post-hoc calibration`, `Bayesian decision theory`, `distribution shift`, `logit correction`, `frozen backbone`

### 13. AirCopBench: A Benchmark for Multi-drone Collaborative Embodied Perception and Reasoning
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37126) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37126/41088)
- **作者**: Jirong Zha, Yuxuan Fan, Tianyu Zhang, Geng Chen, Yingfeng Chen, Chen Gao, Xinlei Chen
- **会议/来源**: AAAI 2026 · Track 2
- 相关性 7/10 · `benchmark`
- **测什么**: 多无人机协同感知与推理能力，包括场景理解、物体理解、感知评估和协同决策。
- **摘要**: AirCopBench 是首个面向多无人机协同具身感知与推理的评测基准，旨在评估多模态大模型（MLLMs）在真实退化感知条件下的协同能力。基准包含 14.6k+ 道题目，数据来自仿真器和真实世界，覆盖场景理解、物体理解、感知评估和协同决策四个任务维度，共 14 种任务类型。题目通过模型生成、规则生成和人工标注三种方式构建，并经过严格质量控制；数据来自具有挑战性的退化感知场景，并标注了协同事件。评测了 40 个 MLLMs，发现协同感知任务上性能差距显著，最佳模型平均落后人类 24.38%，且跨任务表现不一致。微调实验验证了仿真到真实迁移的可行性。
- **为什么值得看**: 该基准填补了多智能体协同感知评测的空白，其构造流程（多来源数据、混合标注、质量控制）和人类基线对比为评测方法学提供了可参考的框架，尤其适合研究协同场景下的构念覆盖和难度校准。
- **关键技术**: `benchmark construction`, `human baseline`, `sim-to-real transfer`, `multi-agent evaluation`, `quality control`

### 14. AR-Nav Benchmark: Augmented Reality Navigation with Vision and Language
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38849) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38849/42811)
- **作者**: Liqi Yan, Yihao Wu, Chenyi Xu, Chao Yang, Jianhui Zhang, Pan Li
- **会议/来源**: AAAI 2026 · Track 21
- 相关性 7/10 · `benchmark`
- **测什么**: AR 导航中视觉-语言理解、空间记忆和路径规划的综合能力
- **摘要**: AR-Nav 是一个面向增强现实（AR）导航的视觉-语言基准，包含数据集和配套评测套件，旨在评估多楼层室内和室外停车场等动态、大规模场景下的空间智能。基准构建采用提出的 AR-VLM² 模型生成结构化、语义丰富且带时间索引的记忆表示，以支持长期导航；同时引入 ARN-Pilot 模块进行分层拓扑推理和语言引导的路径规划，以及闭环交互模块支持多模态反馈和动态记忆更新。实验表明，AR-Nav 套件在多个指标上优于现有 AR 导航方法，但论文未提供详细的评测方法学分析，如人类基线或污染检查。
- **为什么值得看**: 该基准提出了针对 AR 导航的评测框架，但缺乏对测量效度（如任务难度校准、人类表现基线）的深入验证，其方法学贡献有限，主要价值在于填补 AR 导航评测空白。
- **关键技术**: `benchmark construction`, `multi-modal evaluation`, `spatial memory modeling`, `human-in-the-loop`

### 15. Benchmarking Visual LLMs Resilience to Unanswerable Questions on Visually Rich Documents
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37759) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37759/41721)
- **作者**: Davide Napolitano, Luca Cagliero, Fabrizio Battiloro
- **会议/来源**: AAAI 2026 · Track 10
- 相关性 7/10 · `benchmark`
- **测什么**: VLLM 在视觉丰富文档中检测不可回答问题的能力，以及不同扰动类型和知识注入策略的影响。
- **摘要**: VRD-UQA 是一个用于评估视觉大语言模型（VLLM）在视觉丰富文档（VRD）上对“看似合理但不可回答”问题鲁棒性的基准。它通过自动替换原问题中的实体（同类型但属于不同文档元素或布局位置）生成扰动问题，并利用 VLLM-as-judge 验证其不可回答性。基准基于现有 VQA 数据集构建，涵盖多页文档，并在 12 个模型上评估了页面级和文档级的不可回答检测能力，以及不同扰动类型（NLP 实体、文档元素、布局）和知识注入策略（OCR、多页选择、不可回答提示）的影响。结果显示 VLLM 在此任务上存在明显局限，VRD-UQA 可作为开发鲁棒文档 VQA 系统的评测框架。
- **为什么值得看**: 该工作提供了针对不可回答问题的扰动生成流程和 VLLM-as-judge 验证方法，可复用于其他评测场景；同时揭示了 VLLM 在检测不可回答问题上的系统性失败模式，对评测效度（construct coverage）有方法学价值。
- **关键技术**: `benchmark construction`, `perturbation generation`, `LLM-as-judge`, `unanswerability verification`, `in-context learning`

### 16. Beyond Counting: Evaluating Abstract and Emotional Reasoning in Vision-Language Models
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38389) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38389/42351)
- **作者**: Yuan Zhou, Yan Zhang, Jianlong Chang, Xin Gu, Ying Wang, Kun Ding, Guangwen Yang, Shiming Xiang
- **会议/来源**: AAAI 2026 · Track 16
- 相关性 7/10 · `benchmark`
- **测什么**: VLM 在抽象、情感与组合逻辑等细粒度高阶推理能力上的表现
- **摘要**: EmojiGrid 是一个针对视觉语言模型（VLM）细粒度与高阶推理能力的诊断基准，利用表情符号的语义丰富性构建网格视觉数据集，包含 29,000+ 问答对。任务基于三层认知分类法（感知与信息提取、关系与结构推理、抽象与高级认知），细分为九个类别，覆盖计数、空间关系、组合逻辑、语义情感等能力。作者评估了 25 个开源与专有 VLM，发现模型在抽象与情感推理上显著落后于基础感知任务，尤其在组合逻辑、空间一致性和情感语义理解上表现不佳。该基准提供了可量化的细粒度诊断工具，但未报告污染检查或人类基线验证，其构造效度有待进一步确认。
- **为什么值得看**: 该论文提出了一个基于认知分类法的细粒度评测框架，将抽象与情感推理操作化，为评测构念覆盖提供了新思路；但其缺乏人类基线与污染审计，限制了测量效度的论证，可作为评测方法学中'构念效度验证'的案例。
- **关键技术**: `benchmark construction`, `cognitive taxonomy`, `fine-grained evaluation`, `grid-based visual reasoning`

### 17. DynamicEarth: How Far Are We from Open-Vocabulary Change Detection?
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37554) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37554/41516)
- **作者**: Kaiyu Li, Xiangyong Cao, Yupeng Deng, Chao Pang, Zepeng Xin, Hui Qiao, Tieliang Gong, Deyu Meng et al.
- **会议/来源**: AAAI 2026 · Track 8
- 相关性 7/10 · `benchmark`
- **测什么**: 开放词汇变化检测中模型对任意类别变化识别的泛化能力与鲁棒性
- **摘要**: 本文提出开放词汇变化检测（OVCD）任务，旨在检测任意类别的土地覆盖变化，突破传统变化检测依赖预定义类别的限制。作者构建了两种免训练框架 M-C-I（先发现变化再分类）和 I-M-C（先识别目标再判断状态变化），并集成 SAM、DINOv2、Grounding-DINO 等现成基础模型实现多种方法。在 4 个基准数据集上评估，显示优于现有监督和无监督方法，并发布 DynamicEarth 代码库。方法学贡献在于提出新任务定义和免训练集成框架，但未涉及污染检查或人类基线验证。
- **为什么值得看**: 该论文提出了新的评测任务（OVCD）和基准数据集，为多模态（视觉-语言）变化检测提供了评测框架，但缺乏对评测方法学（如标注一致性、难度校准）的深入探讨，其价值主要在于任务定义和基线方法。
- **关键技术**: `open-vocabulary task formulation`, `training-free framework`, `foundation model integration`, `benchmark evaluation`

### 18. EgoCross: Benchmarking Multimodal Large Language Models for Cross-Domain Egocentric Video Question Answering
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37589) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37589/41551)
- **作者**: Yanjun Li, Yuqian Fu, Tianwen Qian, Qi'Ao Xu, Silong Dai, Danda Pani Paudel, Luc Van Gool, Xiaoling Wang
- **会议/来源**: AAAI 2026 · Track 8
- 相关性 7/10 · `benchmark`
- **测什么**: 多模态大模型在跨领域自我中心视频问答中的泛化能力（预测、识别、定位、计数）。
- **摘要**: EgoCross 是一个用于评测多模态大模型（MLLM）在跨领域自我中心视频问答（EgocentricQA）中泛化能力的基准。它覆盖四个与日常生活差异显著的领域：手术、工业、极限运动和动物视角，包含约 1000 个 QA 对（798 个视频片段），并设计了预测、识别、定位和计数四类任务，每个 QA 对同时提供开放问答（OpenQA）和封闭问答（CloseQA）两种格式以支持细粒度评估。实验表明，大多数通用或自我中心专用的 MLLM 在跨领域场景下表现不佳，凸显了现有模型的泛化局限。论文还进行了微调和强化学习等初步探索以改进性能。该基准的贡献在于填补了现有 EgocentricQA 基准仅覆盖日常活动的空白，并提供了跨领域泛化的评测框架。
- **为什么值得看**: 该基准明确聚焦于跨领域泛化这一评测构念，通过选择视觉风格和语义内容差异显著的领域来测试模型鲁棒性，并同时提供 OpenQA/CloseQA 格式，有助于分析任务格式对评测结果的影响，对评测方法学有参考价值。
- **关键技术**: `benchmark construction`, `cross-domain generalization`, `OpenQA/CloseQA formats`, `task taxonomy`

### 19. Game Ground Bench: Probing the Limits of LVLMs in Complex Semantic Grounding Across Game Universes
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37800) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37800/41762)
- **作者**: Zhangyang Qi, Jinsong Li, Hongjian Wu, Jiaqi Wang, Hengshuang Zhao
- **会议/来源**: AAAI 2026 · Track 10
- 相关性 7/10 · `benchmark`
- **测什么**: LVLMs 在复杂游戏场景中将语言指令与对象/UI 元素关联的细粒度基础能力
- **摘要**: GGBench 是一个跨游戏类型的视觉语言基础（grounding）评测基准，包含 10 类游戏（卡牌、FPS、RPG 等）共 1335 张测试图，任务要求将自然语言指令与游戏内对象和 UI 元素关联。作者指出现有基准的不足：RefCOCO 等真实数据集存在领域差距，GUI 基准缺乏游戏界面复杂度，而既有游戏基准过于简单或狭窄。实验显示现有 LVLMs 在 GGBench 上表现差，尤其在复杂场景中基础能力弱；由于数据规模有限，直接微调困难。为此提出 Game-R1 训练方法，基于 GRPO 算法最大化有限交互数据的效用，实现跨游戏的少样本泛化，并在 GGBench 上显著超越现有模型。该基准为游戏环境中的智能体研究提供了评测平台，但论文未报告污染检查或人类基线，方法学贡献主要在训练方法而非评测设计。
- **为什么值得看**: 该基准填补了游戏场景中细粒度语义基础评测的空白，但其评测方法学贡献有限：未提供人类基线、难度校准或污染检测，主要价值在于任务多样性和场景覆盖，可作为评测构念覆盖的参考案例。
- **关键技术**: `benchmark construction`, `cross-genre task design`, `few-shot generalization`, `GRPO`

### 20. GeoX-Bench: Benchmarking Cross-View Geo-Localization and Pose Estimation Capabilities of Large Multimodal Models
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38353) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38353/42315)
- **作者**: Yushuo Zheng, Jiangyong Ying, Huiyu Duan, Chunyi Li, Zicheng Zhang, Jing Liu, Xiaohong Liu, Guangtao Zhai
- **会议/来源**: AAAI 2026 · Track 16
- 相关性 7/10 · `benchmark`
- **测什么**: 跨视角地理定位和姿态估计能力
- **摘要**: GeoX-Bench 是一个用于评估大型多模态模型（LMMs）在跨视角地理定位和姿态估计能力的基准。它包含来自49个国家128个城市的10,859对全景-卫星图像，并生成755,976个问答对，其中42,900个用于基准测试，其余用于指令微调。作者评估了25个SOTA LMMs，发现模型在地理定位任务上表现尚可，但在更复杂的姿态估计任务上性能显著下降，表明该领域仍需改进。此外，使用GeoX-Bench训练数据进行指令微调能显著提升模型的跨视角地理感知能力。该基准提供了大规模、多城市的数据集，并包含训练/测试划分，但未明确提及污染检查或人类基线验证。
- **为什么值得看**: 该基准为跨视角地理定位和姿态估计提供了大规模、多城市的评测数据集，并揭示了LMMs在姿态估计上的能力短板，对评测方法学有参考价值，但缺乏对评测本身（如污染、人类基线）的深入验证。
- **关键技术**: `benchmark construction`, `instruction tuning`, `cross-view geo-localization`

### 21. Human-Centric Open-Future Task Discovery: Formulation, Benchmark, and Scalable Tree-Based Search
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38829) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38829/42791)
- **作者**: Zijian Song, Xiaoxin Lin, Tao Pu, Zhenlong Yuan, Guangrun Wang, Liang Lin
- **会议/来源**: AAAI 2026 · Track 21
- 相关性 7/10 · `benchmark`
- **测什么**: 多模态模型在开放未来场景中主动发现减少人类负担任务的能力
- **摘要**: 该论文提出人类中心开放未来任务发现（HOTD）问题，旨在让多模态大模型在开放未来场景中主动发现能减少人类负担的任务。作者构建了HOTD-Bench基准，包含超过2000个真实世界视频，采用半自动标注流程，并设计了面向开放集未来评估的模拟协议。同时提出协作多智能体搜索树（CMAST）框架，通过多智能体系统分解复杂推理，并用可扩展搜索树结构化推理过程。实验表明CMAST在HOTD-Bench上显著优于现有LMM，且能即插即用地提升现有模型性能。该基准关注动态人类意图和未来任务发现，但评测方法学贡献有限，缺乏对标注可靠性、人类基线或污染控制的详细分析。
- **为什么值得看**: 该基准提出了开放集未来任务发现的评测协议，但未深入探讨测量效度（如标注一致性、任务难度校准），对评测方法学的增量贡献有限，主要价值在于定义新任务范式。
- **关键技术**: `benchmark construction`, `simulation-based evaluation`, `multi-agent system`, `search tree`

### 22. LLM-Free Image Captioning Evaluation in Reference-Flexible Settings
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/42472) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/42472/46433)
- **作者**: Shinnosuke Hirano, Yuiga Wada, Kazuki Matsuda, Seitaro Otsuki, Komei Sugiura
- **会议/来源**: AAAI 2026 · Track 6
- 相关性 7/10 · `evaluation_method`
- **测什么**: 图像描述生成质量，包括与参考描述的一致性及无参考时的整体相关性。
- **摘要**: 本文提出 Pearl，一个无需 LLM 的监督式图像描述评估指标，适用于有参考和无参考两种设置。现有基于 LLM 的指标偏向自身生成，中立性存疑；而多数无 LLM 指标性能不高。Pearl 通过新机制学习图像-描述和描述-描述相似性表示，并构建了包含约 33.3 万条人工判断、来自 2360 名标注者、覆盖 7.5 万张图像的数据集。在 Composite、Flickr8K-Expert、Flickr8K-CF、Nebula 和 FOIL 数据集上，Pearl 在两种设置下均优于现有无 LLM 指标。该工作提供了大规模人工标注数据，并验证了无 LLM 指标在参考灵活场景下的有效性。
- **为什么值得看**: 提供了大规模人工判断数据集（33.3 万条）用于指标验证，并系统比较了 LLM-free 与 LLM-based 指标的中立性，对评测方法学中指标偏差和参考设置灵活性有参考价值。
- **关键技术**: `supervised metric`, `human-annotated dataset`, `reference-free evaluation`, `similarity learning`

### 23. MME-SCI: A Comprehensive and Challenging Science Benchmark for Multimodal Large Language Models
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37829) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37829/41791)
- **作者**: Jiacheng Ruan, Dan Jiang, Xian Gao, Ting Liu, Yuzhuo Fu, Yangyang Kang
- **会议/来源**: AAAI 2026 · Track 11
- 相关性 7/10 · `benchmark`
- **测什么**: 多模态科学推理能力，包括跨语言、跨模态的知识理解与推理。
- **摘要**: MME-SCI 是一个面向多模态大语言模型（MLLMs）的科学推理基准，包含 1,019 道高质量问答对，覆盖数学、物理、化学、生物四个学科，支持中、英、法、西、日五种语言，并设计了三种评测模式（如图像、文本等）。该基准旨在弥补现有科学基准在多语言推理、模态覆盖和知识点细粒度标注方面的不足。作者对 16 个开源和 4 个闭源模型进行了实验，结果显示基准难度较高，例如 o4-mini 在图像模式下数学准确率仅 52.11%，物理 24.73%，化学 36.57%，生物 29.80%。利用多语言和细粒度知识属性，作者分析了模型弱点，如 o4-mini 在“磁场”相关问题上仅答对 33 题中的 5 题。该基准提供了细粒度知识点标注，有助于定位模型的具体能力缺陷。
- **为什么值得看**: 该基准提供了细粒度的知识点标注和跨语言评测设计，可用于分析模型在不同学科和知识点上的能力分布，对评测的构念效度（construct validity）有参考价值；同时其难度校准和模型弱点暴露方式，为评测方法学提供了可借鉴的案例。
- **关键技术**: `benchmark construction`, `multilingual evaluation`, `fine-grained annotation`, `difficulty calibration`, `model weakness analysis`

### 24. MosaicDoc: A Large-Scale Bilingual Benchmark for Visually Rich Document Understanding
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37282) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37282/41244)
- **作者**: Ketong Chen, Yuhao Chen, Yang Xue
- **会议/来源**: AAAI 2026 · Track 4
- 相关性 7/10 · `benchmark`
- **测什么**: 视觉丰富文档理解中的多任务能力（OCR、VQA、阅读顺序、定位）及复杂版面鲁棒性。
- **摘要**: MosaicDoc 是一个大规模中英双语视觉丰富文档理解（VRDU）基准，包含 72K 张来自报纸和杂志的图像，覆盖 196 家出版商的多样复杂版面（多栏、非曼哈顿布局），并配有超过 600K 的 QA 对，支持 OCR、VQA、阅读顺序和定位等多任务标注。基准通过 DocWeaver 多智能体流水线自动生成，利用 LLM 合成任务和标注，以低成本扩展规模。作者对多个 SOTA VLM 进行了评估，揭示其在真实文档复杂性上的不足。方法学上，该工作提出了自动化基准生成流程，但未报告人类基线或污染检查，限制了其效度论证。
- **为什么值得看**: 该论文展示了用 LLM 多智能体流水线自动构造大规模多语言基准的可行性，但缺乏人类基线和污染审计，为评测方法学提供了关于自动生成基准效度验证的案例。
- **关键技术**: `multi-agent pipeline`, `benchmark construction`, `bilingual dataset`, `multi-task annotation`

### 25. OpenScan: A Benchmark for Generalized Open-Vocabulary 3D Scene Understanding
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38331) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38331/42293)
- **作者**: Youjun Zhao, Jiaying Lin, Shuquan Ye, Qianshi Pang, Rynson W. H. Lau
- **会议/来源**: AAAI 2026 · Track 16
- 相关性 7/10 · `benchmark`
- **测什么**: 模型对 3D 场景中细粒度属性（如功能、材质）的开放词汇理解能力
- **摘要**: OpenScan 提出了广义开放词汇 3D 场景理解（GOV-3D）任务，将开放词汇从物体类别扩展到细粒度、对象特定的属性查询，涵盖 8 个语言方面（如功能、属性、材质）。基准包含 3D 对象属性标注，规模未明确给出，但评估了多种 SOTA OV-3D 方法。结果显示现有方法难以理解抽象词汇，且仅扩大训练类别无法解决。论文分析了失败模式并探讨了改进方向，但未报告人类基线或污染检查。
- **为什么值得看**: 该基准扩展了开放词汇评测的构念覆盖，从类别识别转向属性理解，揭示了现有评测的覆盖缺口，为 3D 场景理解评测提供了新的任务设计和难度校准思路。
- **关键技术**: `benchmark construction`, `open-vocabulary evaluation`, `attribute annotation`, `failure analysis`

### 26. PEOD: A Pixel-Aligned Event-RGB Benchmark for Object Detection Under Challenging Conditions
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38883) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38883/42845)
- **作者**: Luoping Cui, Hanqing Liu, Mingjie Liu, Endian Lin, Donghong Jiang, Yuhao Wang, Chuang Zhu
- **会议/来源**: AAAI 2026 · Track 22
- 相关性 7/10 · `benchmark`
- **测什么**: 在低光、过曝和高速运动等挑战条件下，事件相机与 RGB 融合目标检测的鲁棒性。
- **摘要**: PEOD 是一个像素级对齐的高分辨率（1280×720）Event-RGB 目标检测基准，旨在评估极端光照和高速运动等挑战条件下的检测器。数据集包含 130+ 时空对齐序列和 34 万个人工标注框，其中 57% 的数据来自低光、过曝和高速运动场景，覆盖了现有数据集（分辨率≤640×480）的不足。作者在 PEOD 上对 14 种方法在三种输入配置（仅事件、仅 RGB、事件-RGB 融合）下进行了基准测试。结果显示，在完整测试集和正常子集上融合模型表现最佳，但在光照挑战子集上，最佳事件模型超越了所有融合模型，而融合模型仍优于其 RGB 对应模型，表明当帧模态严重退化时现有融合方法的局限性。该基准为多模态感知提供了现实且高质量的评测资源，并计划公开。
- **为什么值得看**: 该论文通过构建高分辨率、像素级对齐的挑战性场景基准，并系统比较不同输入配置下的模型表现，揭示了融合方法在极端条件下的失效模式，为多模态评测的构念覆盖和难度校准提供了参考。
- **关键技术**: `benchmark construction`, `pixel-aligned annotation`, `challenging condition subset`, `cross-modal comparison`

### 27. Perceptual Quality Assessment of 3D Gaussian Splatting: A Subjective Dataset and Prediction Metric
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37928) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37928/41890)
- **作者**: Zhaolin Wan, Yining Diao, Jingqi Xu, Hao Wang, Zhiyang Li, Xiaopeng Fan, Wangmeng Zuo, Debin Zhao
- **会议/来源**: AAAI 2026 · Track 12
- 相关性 7/10 · `benchmark`
- **测什么**: 3DGS渲染内容在多种失真条件下的感知质量
- **摘要**: 本文提出3DGS-QA，首个针对3D高斯泼溅（3DGS）渲染内容的主观质量评估数据集，包含15类物体、225个退化重建样本，系统覆盖视点稀疏、训练迭代不足、点云下采样、噪声和颜色失真等常见失真因素。作者招募受试者进行主观评分，构建了带人类标注的质量基准。基于该数据集，提出一种无参考质量预测模型，直接操作原生3D高斯原语，无需渲染图像或真值，提取空间和光度线索进行结构感知的质量估计。实验对比了传统和基于学习的现有质量评估方法，所提模型性能最优。数据集和代码已公开。
- **为什么值得看**: 该工作为3DGS这一新兴渲染技术建立了首个带人类标注的主观质量基准，提供了失真因素控制的构造范例，并验证了无参考指标与人类感知的一致性，对评测方法学中'新模态基准的构建与验证'有参考价值。
- **关键技术**: `subjective quality assessment`, `no-reference quality prediction`, `3D Gaussian primitives`, `distortion factor control`, `human baseline`

### 28. SpatialLogic-Bench: A Diagnostic Benchmark for Task-Oriented Spatiotemporal Reasoning
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/39022) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/39022/42984)
- **作者**: Xiaoda Yang, Shenzhou Gao, Can Wang, Jiahe Zhang, Menglan Tang, Jingyang Xue, Sheng Liu, Peijian Zhang et al.
- **会议/来源**: AAAI 2026 · Track 23
- 相关性 7/10 · `benchmark`
- **测什么**: 视觉语言模型在任务导向场景中的时空逻辑推理能力，特别是对时间顺序的依赖程度。
- **摘要**: SpatialLogic-Bench 是一个面向视觉语言模型（VLM）的任务导向时空推理诊断基准，旨在评估模型对动态场景中时空逻辑的理解以及任务进展判断能力。基准包含两个核心能力维度：细粒度视觉判别（感知状态帧间的细微物理变化）和逻辑推理（将变化与任务目标关联并判断进展）。为缓解时间依赖偏差，作者设计了双任务范式，将图像对以时间顺序和逆序两种方式呈现，同时保持任务描述一致。通过改变帧间时间间隔构建多尺度评估体系：小间隔测试细粒度感知，大间隔要求更复杂的逻辑推理。实验发现多数 VLM 在逆序任务上性能显著下降，表明模型过度依赖时间线索而非稳健推理。该基准暴露了当前模型的动态空间感知局限，为改进提供了方向。
- **为什么值得看**: 该基准通过双任务范式（正序/逆序）系统性地控制时间顺序偏差，为评测动态推理能力提供了可复用的实验设计，并揭示了模型对时间线索的依赖这一测量效度问题。
- **关键技术**: `dual-task paradigm`, `temporal order control`, `multi-scale time intervals`, `diagnostic benchmark`

### 29. Textured Geometry Evaluation: Perceptual 3D Textured Shape Metric via 3D Latent-Geometry Network
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37707) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37707/41669)
- **作者**: Tianyu Luan, Xuelu Feng, Zixin Zhu, Phani Nuney, Sheng Liu, Xuan Gong, David Doermann, Chunming Qiao et al.
- **会议/来源**: AAAI 2026 · Track 9
- 相关性 7/10 · `evaluation_method`
- **测什么**: 带纹理 3D 网格的感知保真度，即与参考形状的几何和颜色相似度。
- **摘要**: 本文提出 TGE，一种直接基于带纹理 3D 网格的保真度评估指标，无需渲染，联合使用几何与颜色信息计算输入网格与参考形状的相似度。现有指标如 Chamfer Distance 与人类感知不一致，而基于渲染的指标受视角选择和结构覆盖不全影响，且多在合成失真上训练，存在域差距。作者构建了包含真实世界失真的人工标注数据集用于训练和评估，实验表明 TGE 在真实失真数据集上优于基于渲染和仅几何的方法。该工作为 3D 生成质量评估提供了新的度量思路，但未涉及污染检查或人类基线校准等评测方法学细节。
- **为什么值得看**: 该论文提出了一种新的 3D 内容评估指标，直接基于网格而非渲染，并构建了真实失真数据集，对评测方法学中构念覆盖和域差距问题有参考价值，但缺乏对指标效度的系统验证。
- **关键技术**: `3D mesh evaluation`, `human-annotated dataset`, `real-world distortions`, `geometry and color fusion`

### 30. Unaligned UAV RGBT Tracking: A Largescale Benchmark and a Novel Approach
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38079) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38079/42041)
- **作者**: Yun Xiao, Yuhang Wang, Jiandong Jin, Wankang Zhang, Chenglong Li
- **会议/来源**: AAAI 2026 · Track 13
- 相关性 7/10 · `benchmark`
- **测什么**: 无人机场景下 RGB 与热红外模态空间未对齐时的多模态跟踪鲁棒性
- **摘要**: 该论文提出无人机场景下未对齐的 RGBT 跟踪任务，并构建了首个大规模未对齐 RGB-TIR 视频数据集，包含 1,453 对无人机拍摄序列，具有精确的双模态边界框标注，覆盖 42 个目标类别、22 种挑战属性和多种空间错位尺度。现有 RGBT 跟踪方法依赖空间对齐输入，无法处理无人机双传感器固有的错位问题，该工作填补了这一空白。方法上设计了混合移位估计专家模块和跨模态对齐融合模块，以自适应估计和补偿不同尺度下的空间移位及非线性形变。实验表明所提跟踪器显著优于现有 SOTA 方法，验证了其在真实未对齐场景中的实用性。作为新任务基准，该数据集为评测未对齐多模态跟踪提供了基础，但未涉及污染检查或人类基线等评测方法学细节。
- **为什么值得看**: 该基准首次系统性地引入空间错位作为多模态跟踪的评测维度，为评测设计提供了新的构念覆盖（未对齐鲁棒性），但缺乏对标注一致性或难度校准的方法学验证，其评测贡献主要在于任务定义和数据集构建。
- **关键技术**: `benchmark construction`, `spatial misalignment simulation`, `dual-modal annotation`, `cross-modal alignment`

### 31. VAGU & GtS: LLM-Based Benchmark and Framework for Joint Video Anomaly Grounding and Understanding
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/42412) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/42412/46373)
- **作者**: Shibo Gao, Peipei Yang, Yangyang Liu, Yi Chen, Han Zhu, Xu-Yao Zhang, Linlin Huang
- **会议/来源**: AAAI 2026 · Track 6
- 相关性 7/10 · `benchmark`
- **测什么**: 视频异常事件的时间定位精度与语义理解能力，以及推理速度与准确率的综合表现。
- **摘要**: VAGU 是首个联合评测视频异常时间定位与语义理解的基准，包含 1,000 个真实监控视频片段，提供细粒度时间边界标注和客观多项选择视频问答，共约 10,000 道题目。作者提出 GtS（Glance then Scrutinize）无训练框架，通过先粗后细的两阶段策略平衡时间精度与语义可解释性，并引入 JeAUG 指标综合评估速度与准确率。实验表明 GtS 在精度和效率上优于现有方法，且基准具有较好的区分度。方法学贡献在于将异常检测的两个子任务联合评测，并设计了兼顾速度与精度的综合指标。
- **为什么值得看**: 该工作为视频异常评测提供了联合任务基准和综合指标 JeAUG，展示了如何平衡时间定位精度与语义理解，对评测方法学中多任务联合测量和效率-精度权衡有参考价值。
- **关键技术**: `benchmark construction`, `multi-task evaluation`, `metric design`, `training-free framework`

### 32. VIR-Bench: Evaluating Geospatial and Temporal Understanding of MLLMs via Travel Video Itinerary Reconstruction
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37938) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37938/41900)
- **作者**: Hao Wang, Eiki Murata, Lingfang Zhang, Ayako Sato, So Fukuda, Ziqi Yin, Wentao Hu, Keisuke Nakao et al.
- **会议/来源**: AAAI 2026 · Track 12
- 相关性 7/10 · `benchmark`
- **测什么**: 多模态模型对长时间、大空间跨度视频的地理空间与时间理解能力（行程重建）。
- **摘要**: VIR-Bench 是一个用于评估多模态大语言模型（MLLM）地理空间与时间理解能力的新基准，通过旅行视频的行程重建任务来测试模型。基准包含 200 个旅行视频，覆盖长时间、大空间跨度的场景，要求模型从视频中提取并重建完整的行程信息。实验表明，包括专有模型在内的 SOTA MLLM 在该任务上得分很低，凸显了长时空跨度视频理解的难度。作者还进行了案例研究，开发了一个旅行规划智能体，利用基准洞察显著提升了行程推荐质量，验证了评测协议的实际应用价值。该基准的构造考虑了任务难度校准，但未提及污染检查或人类基线。
- **为什么值得看**: 该基准填补了视频评测中长距离、大时空跨度场景的空白，其任务设计（行程重建）为评测地理空间与时间推理提供了新的构念覆盖，并展示了评测结果如何转化为下游应用性能提升，对评测方法学有参考价值。
- **关键技术**: `benchmark construction`, `task design`, `case study`, `agent evaluation`

### 33. VisAssist: A Visually Impaired-Captured Video Question Answering Benchmark for Assistive Systems
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/42410) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/42410/46371)
- **作者**: Qi Gao, Heng Li, Yixin Zhou, Meixuan Zhou, Jieqiong Chen, Xinyu Chai
- **会议/来源**: AAAI 2026 · Track 6
- 相关性 7/10 · `benchmark`
- **测什么**: 多模态模型在第一人称动态视频中的空间推理、信息缺失判别和文本理解能力。
- **摘要**: VisAssist 是首个面向视障用户拍摄的真实世界视频问答基准，包含 13,413 个第一人称视角视频，填补了辅助视觉研究中缺乏真实用户视角数据的空白。与依赖第三人称镜头的现有基准不同，该数据集捕捉了盲人摄影中的独特挑战，如非常规构图、运动伪影和信息频繁缺失。对 SOTA 多模态模型的评估揭示了系统性局限：在动态第一人称视角下空间推理严重不足，无法区分信息缺失与拍摄质量差导致危险幻觉，以及在非理想条件下对非拉丁文字的理解脆弱。该工作建立了重要的真实世界基准，并强调专用架构在视觉辅助系统中的必要性。
- **为什么值得看**: 该基准提供了真实用户视角的生态效度，揭示了现有基准在构念覆盖上的缺口（第一人称动态视角），并暴露了模型在信息缺失与质量差之间的判别失败，这对评测方法学中关于任务设计和失败模式分析有参考价值。
- **关键技术**: `real-world dataset`, `first-person perspective`, `benchmark construction`, `failure mode analysis`

### 34. VP-Bench: A Comprehensive Benchmark for Visual Prompting in Multimodal Large Language Models
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38114) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38114/42076)
- **作者**: Mingjie Xu, Jinpeng Chen, Yuzhi Zhao, Jason Chun Lok Li, Yue Qiu, Zekang Du, Mengyang Wu, Pingping Zhang et al.
- **会议/来源**: AAAI 2026 · Track 13
- 相关性 7/10 · `benchmark`
- **测什么**: 多模态大语言模型对视觉提示（如边界框、点）的感知能力及其对下游任务的影响
- **摘要**: VP-Bench 是首个系统评估多模态大语言模型（MLLM）视觉提示（Visual Prompting）能力的基准，覆盖边界框、点、箭头等 8 种提示形状和 355 种属性组合，共 10 万条可视化提示。评测采用两阶段框架：第一阶段测试模型在自然场景中对视觉提示的感知能力，第二阶段衡量视觉提示对下游任务（如细粒度物体识别）的实际影响。作者在 21 个 MLLM（包括 GPT-4o、InternVL-2.5、Qwen2.5-VL）上进行了评估，并分析了属性变化和模型规模等因素对视觉提示理解的影响。该基准填补了现有评测空白，为研究 MLLM 的接地引用问题提供了新参考框架。
- **为什么值得看**: 该基准提出了一个两阶段评测框架，将视觉提示感知与下游任务效用分离，并系统控制了提示形状和属性组合，为评测多模态模型的空间指代能力提供了可复用的任务设计和难度校准思路。
- **关键技术**: `two-stage evaluation framework`, `attribute combination control`, `multi-shape prompt design`, `model scale analysis`
