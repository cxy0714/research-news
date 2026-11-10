# AAAI 2026 · AI 评测 / Benchmark

> 只收录与「评测 / benchmark」相关的论文：标题命中评测词表（ACL 系另加摘要）后，按**评测方法学价值**打分，取高分做中文精摘。**不是会议全量**。

- 收录 **134** 篇 · 已打分 **134** · 精摘 **58** · 更新于 2026-11-10
- 口径：测量设计 / 构念覆盖 / 污染控制 / 难度校准 / 人类基线 / judge 验证 / 统计可靠性；纯榜单提升不加分。

## 主题分布

| 主题 | 精摘篇数 | 页面 |
|---|---:|---|
| 评测方法学 | 8 | [1](topics/methodology.md) |
| Agent / 工具使用 | 4 | [1](topics/agents_tools.md) |
| RAG / 长上下文 | 1 | [1](topics/rag_longctx.md) |
| 多模态评测 | 34 | [1](topics/multimodal.md) |
| 安全 / 事实性 | 1 | [1](topics/safety_factuality.md) |
| 领域基准 | 9 | [1](topics/domain.md) |
| 其他 | 1 | [1](topics/other.md) |

## 必读 Top 20

### 1. Do Large Language Models Reason About Uncertainty Like Humans? A Benchmark on Hurricane Forecast Visualization Comprehension
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38812) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38812/42774)
- **作者**: Le Liu, Yuhao Wang, Bohan Shen, Wei Zeng, Shizhou Zhang, Di Xu, Peng Wang
- **会议/来源**: AAAI 2026 · Track 21
- 相关性 9/10 · `benchmark`
- **测什么**: 人类与 LLM 在不确定性可视化（飓风路径）上的推理能力及认知偏差复现程度
- **摘要**: UnReason 是首个系统比较人类与 LLM 在飓风预报不确定性可视化上推理能力的基准。它包含两个递进阶段、七种可视化格式、六个真实飓风案例，以及三类主体（人类、有上下文 LLM、无上下文 LLM），共 880 张可视化图和 117,600 个结构化问答对，并在匹配的评估条件下进行。阶段一评估隐式和显式不确定性编码下的推理，阶段二考察单一与多维不确定性表征下的推理。研究全面评估了损失估计、推理策略和理解模式，发现 LLM 对不确定性有更强的语义和概念理解，较少被视觉变异性误导，但在决策时仍复现了人类的关键偏差。该基准为在不确定性丰富的视觉推理任务中校准 LLM 行为与人类认知提供了洞见。
- **为什么值得看**: 该基准提供了跨主体（人类 vs. LLM）的匹配评估设计，可复用于检验 LLM 是否复现人类认知偏差，并揭示了 LLM 在不确定性理解上的优势与局限，对评测方法学中的人类基线与构念效度有直接价值。
- **关键技术**: `matched evaluation conditions`, `human baseline`, `multi-phase task design`, `structured QA pairs`, `cross-agent comparison`

### 2. ELSPR: Evaluator LLM Training Data Self-Purification on Non-Transitive Preferences via Tournament Graph Reconstruction
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38857) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38857/42819)
- **作者**: Yan Yu, Yilun Liu, Minggui He, Shimin Tao, Weibin Meng, Xinhua Yang, Li Zhang, Hongxia Ma et al.
- **会议/来源**: AAAI 2026 · Track 21
- 相关性 9/10 · `evaluation_method`
- **测什么**: 成对偏好评估中的非传递性和偏好清晰度（数据质量）
- **摘要**: 本文针对 LLM 成对评估中非传递偏好（A>B, B>C, C>A）破坏排名可靠性的问题，提出 ELSPR 框架，将偏好数据建模为锦标赛图，通过强连通分量（SCC）分析量化非传递性，并引入归一化有向图结构熵度量偏好清晰度。方法通过过滤诱导非传递性的低质量偏好对来净化训练数据，在 AlpacaEval 基准上微调模型后，非传递性降低 13.8%，结构熵下降 0.088，判别力显著提升。人类验证显示，被丢弃的数据与保留数据相比，标注者间一致性（34.4% vs 52.6%）和模型-人类一致性（51.2% vs 80.6%）均大幅降低，支持了过滤的有效性。该工作为偏好数据质量控制和评估一致性提供了图论驱动的可复用方法。
- **为什么值得看**: 该论文直接针对评估方法学中的核心问题——非传递偏好对排名可靠性的影响，并提供了基于图论的数据净化流程，可复用于偏好数据质量审计和 LLM-as-judge 训练数据筛选，对测量效度有具体贡献。
- **关键技术**: `tournament graph`, `strongly connected components`, `structural entropy`, `data filtering`, `inter-annotator agreement`

### 3. ARCHE: A Novel Task to Evaluate LLMs on Latent Reasoning Chain Extraction
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37170) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37170/41132)
- **作者**: Pengze Li, Jiaqi Liu, Junchi Yu, Lihao Liu, Mingyu Ding, Wanli Ouyang, Shixiang Tang, Xi Chen
- **会议/来源**: AAAI 2026 · Track 3
- 相关性 8/10 · `benchmark`
- **测什么**: 模型将科学论证分解为标准推理范式（演绎、归纳、溯因）并构建逻辑树的能力。
- **摘要**: ARCHE 提出一个名为“潜在推理链抽取”的新任务，要求模型将复杂科学论证分解为基于皮尔士三种推理模式（演绎、归纳、溯因）的推理逻辑树（RLT），每个推理步骤需显式分类。作者基于 70 篇 Nature Communications 文章构建了 ARCHE Bench，包含超过 1900 个引用和 38000 个观点，并设计了两个逻辑感知指标：实体覆盖率（EC）衡量内容完整性，推理边准确率（REA）衡量逐步逻辑有效性。对 10 个领先 LLM 的评估显示，模型在 REA 和 EC 之间存在权衡，且没有一个能提取出完整且标准的推理链，揭示了当前推理模型与科学论证严谨性之间的显著差距。该工作提供了新的任务定义、基准和指标，但未报告人类基线或标注者间一致性，也未进行污染检查。
- **为什么值得看**: 该论文提出了一个全新的评测任务和两个逻辑感知指标，为评测模型对科学推理范式的理解提供了新视角，但其评测方法学贡献有限，缺乏人类基线和信度验证，可作为构造性效度分析的案例。
- **关键技术**: `benchmark construction`, `logic-aware metrics`, `reasoning tree extraction`, `human baseline (absent)`

### 4. BAG: Benchmarking Anomaly Detection on Dynamic Graphs
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38510) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38510/42472)
- **作者**: Fengrui Hua, Yiyan Qi, Zikai Wei, Yuxing Tian, Chengjin Xu, Xiaojun Wu, Jia Li, Jian Guo
- **会议/来源**: AAAI 2026 · Track 17
- 相关性 8/10 · `benchmark`
- **测什么**: 动态图中边级和节点级异常的检测能力，以及模型对合成与有机异常的区分度。
- **摘要**: BAG 是首个面向动态图异常检测（DyGAD）的系统性基准，覆盖 25 个主流模型（含经典方法与动态图神经网络 DGNN）和 10 个真实数据集，数据集同时包含合成异常与自然发生的异常，支持边级和节点级两种评估粒度。主要发现是连续时间动态图（CTDG）模型在边异常检测上显著优于离散时间动态图（DTDG）模型；同时，现有方法对有机（自然）异常的检测效果较差，归因于时间异常的存在和高度不平衡的样本。基准在数据集选择、指标应用和模型训练方面做了改进，并开源了所有模型、数据集和评估协议以支持可复现性。该工作为 DyGAD 提供了统一的评测框架，但未涉及污染检查或人类基线等评测方法学细节。
- **为什么值得看**: 该基准统一了动态图异常检测的评测协议，明确了不同模型族（CTDG vs DTDG）的能力差异，并揭示了现有方法在有机异常上的系统性短板，为后续评测设计提供了任务难度校准和样本不平衡处理的参考。
- **关键技术**: `benchmark construction`, `multi-dataset evaluation`, `model comparison`, `open-source repository`

### 5. CausalStep: A Benchmark for Explicit Stepwise Causal Reasoning in Videos
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37582) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37582/41544)
- **作者**: Xuchen Li, Xuzhao Li, Shiyu Hu, Kaiqi Huang, Wentao Zhang
- **会议/来源**: AAAI 2026 · Track 8
- 相关性 8/10 · `benchmark`
- **测什么**: 视频中显式逐步因果推理的能力，包括因果单元识别和顺序推理的鲁棒性。
- **摘要**: CausalStep 是一个面向视频显式逐步因果推理的基准，包含 100 个视频（6 个类别）和 1,852 个多项选择问答对。它通过将视频分割为因果关联单元，并采用严格的逐步问答协议，要求模型按顺序作答，从而防止利用全局上下文取巧。每个问题基于错误类型分类法构造干扰项，以增强诊断价值。作者引入七个诊断指标，用于细粒度评估因果推理能力。实验对比了领先的专有和开源模型及人类基线，发现当前模型与人类逐步推理能力差距显著。该基准为视频因果推理提供了严格的评测框架，但规模较小，且未报告污染检查或人类基线标注细节。
- **为什么值得看**: 该基准通过逐步问答协议和基于错误类型的干扰项设计，展示了如何防止捷径解并提升诊断效度，对视频推理评测方法有参考价值；但其规模有限，且未提供污染检查或人类基线信度分析，限制了其方法学贡献的推广。
- **关键技术**: `stepwise QA protocol`, `error type taxonomy`, `diagnostic metrics`, `human baseline`

### 6. CrossVid: A Comprehensive Benchmark for Evaluating Cross-Video Reasoning in Multimodal Large Language Models
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37550) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37550/41512)
- **作者**: Jingyao Li, Jingyun Wang, Molin Tan, Haochen Wang, Cilin Yan, Likun Shi, Jiayin Cai, Xiaolong Jiang et al.
- **会议/来源**: AAAI 2026 · Track 8
- 相关性 8/10 · `benchmark`
- **测什么**: 多模态模型跨视频时空推理与信息聚合能力
- **摘要**: CrossVid 是首个专门评估多模态大模型跨视频推理（CVR）能力的基准，要求模型同时理解多段视频并聚合、比较信息。基准包含四个高层维度和十个具体任务，覆盖 5,331 个视频和 9,015 个问答对，题型包括单选、多选和开放题。实验显示 Gemini-2.5-Pro 表现最佳，平均准确率仅 50.4%，多数模型因无法整合跨视频证据而表现不佳。该基准提供了分层任务设计和多题型覆盖，但未报告人类基线或污染检查，方法学贡献有限。
- **为什么值得看**: 该基准填补了跨视频推理评测的空白，其分层任务设计可作为多视频聚合能力的构念覆盖参考，但缺乏人类基线和污染控制，限制了其作为测量工具的效度论证。
- **关键技术**: `benchmark construction`, `hierarchical task design`, `multi-choice QA`

### 7. D-GARA: A Dynamic Benchmarking Framework for GUI Agent Robustness in Real-World Anomalies
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38795) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38795/42757)
- **作者**: Sen Chen, Tong Zhao, Yi Bin, Fei Ma, Wenqi Shao, Zheng Wang
- **会议/来源**: AAAI 2026 · Track 21
- 相关性 8/10 · `benchmark`
- **测什么**: GUI 代理在真实世界异常（如权限对话框、电池警告）下的任务完成鲁棒性。
- **摘要**: D-GARA 是一个动态评测框架，用于评估 Android GUI 代理在真实世界异常环境中的鲁棒性。它引入了一组常见的异常类型，如权限对话框、电池警告和更新提示，并基于此构建了一个包含常用 Android 应用且嵌入异常的基准数据集。实验表明，最先进的 GUI 代理在异常丰富的环境中性能显著下降，凸显了鲁棒性感知学习的必要性。该框架是模块化和可扩展的，支持集成新任务、异常类型和交互场景。
- **为什么值得看**: 该工作针对现有 GUI 基准静态、理想化的问题，提出了动态异常注入的评测方法，为评测代理在非理想条件下的鲁棒性提供了可复用的框架，对评测方法学有直接贡献。
- **关键技术**: `dynamic benchmark construction`, `anomaly injection`, `modular framework`, `robustness evaluation`

### 8. Detecting Emotional Dynamic Trajectories: An Evaluation Framework for Emotional Support in Language Models
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37189) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37189/41151)
- **作者**: Zhouxing Tan, Ruochong Xiong, Yulong Wan, Jinlong Ma, Hanlin Xue, Qichun Deng, Haifeng Jing, Zhengtong Zhang et al.
- **会议/来源**: AAAI 2026 · Track 3
- 相关性 8/10 · `benchmark`
- **测什么**: 衡量模型在长期对话中改善和稳定用户情绪状态的能力
- **摘要**: 该论文提出一个面向大模型情感支持能力的轨迹级评测框架，将评测从静态快照转向动态轨迹，关注模型能否随时间改善并稳定用户情绪状态。基准包含328个情绪情境和1152个扰动事件，模拟真实对话中的情绪波动；通过引入情境选择、认知重评等心理学验证的情绪调节策略约束模型输出，以鼓励心理学上合理的回应。用户情绪轨迹被建模为一阶马尔可夫过程，并采用因果调整的情绪估计获得无偏的情绪状态追踪。提出三个轨迹级指标：基线情绪水平（BEL）、情绪轨迹波动性（ETV）和情绪中心位置（ECP），综合刻画用户情绪动态。在多个LLM上的评估显示情绪支持能力存在显著差异，并为模型开发提供可操作见解。
- **为什么值得看**: 该框架将评测从静态快照转向动态轨迹，并引入因果调整的情绪估计和轨迹级指标，为长期交互能力的测量提供了新思路，对评测方法学有参考价值。
- **关键技术**: `trajectory-based evaluation`, `causal adjustment`, `first-order Markov process`, `psychologically grounded constraints`, `trajectory-level metrics`

### 9. DISCODE: Distribution-Aware Score Decoder for Robust Automatic Evaluation of Image Captioning
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37440) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37440/41402)
- **作者**: Nakamasa Inoue, Kanoko Goto, Masanari Oi, Martyna Gruszka, Mahiro Ukai, Takumi Hirose, Yusuke Sekikawa
- **会议/来源**: AAAI 2026 · Track 7
- 相关性 8/10 · `evaluation_method`
- **测什么**: 图像描述评估指标在跨领域场景下与人类判断的一致性
- **摘要**: DISCODE 提出一种免微调的图像描述自动评估方法，旨在提升 LVLM 评估器在跨领域场景下的鲁棒性。其核心是测试时自适应评估，引入 Adaptive Test-Time (ATT) 损失，利用高斯先验分布约束评分解码，并推导出解析解以高效优化。作者还构建了 MCEval 基准，覆盖六个不同领域，用于检验评估指标的鲁棒性。实验表明，DISCODE 在 MCEval 及四个现有基准上达到参考无关评估指标的最优性能。该方法为评估指标的领域迁移问题提供了新的解决思路，但未涉及人类基线或 judge 验证的详细分析。
- **为什么值得看**: 该论文针对评估指标在领域偏移下的鲁棒性问题，提出测试时自适应方法，并构建多领域基准，为评测方法学提供了可复用的领域鲁棒性检验框架。
- **关键技术**: `test-time adaptation`, `Gaussian prior`, `reference-free evaluation`, `multi-domain benchmark`

### 10. EvalMuse-40K: A Fine-Grained Benchmark with Comprehensive Human Annotations for Text-to-Image Generation Model Alignment Evaluation
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/42458) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/42458/46419)
- **作者**: Shuhao Han, Haotian Fan, Jiachen Fu, Liang Li, Tao Li, Junhui Cui, Yunqiu Wang, Yang Tai et al.
- **会议/来源**: AAAI 2026 · Track 6
- 相关性 8/10 · `benchmark`
- **测什么**: 文本到图像生成模型的图像-文本细粒度对齐能力（对象、属性、关系等）。
- **摘要**: EvalMuse-40K 是一个用于文本到图像（T2I）生成模型对齐评估的细粒度基准，包含 40K 个图像-文本对，并带有细粒度的人类标注，覆盖对象、属性、关系等对齐相关元素。构建过程中采用了平衡提示采样和数据重新标注等策略，以确保数据集的多样性和可靠性。基于该数据集，作者提出了 FGA-BLIP2，一种仅输入图像和文本即可实现细粒度对齐评估的高效自动方法，无需对每个细粒度元素进行视觉问答。实验表明，FGA-BLIP2 在多个图像-文本对齐数据集上取得了良好性能，并可作为奖励模型用于改进 T2I 模型的对齐能力。该工作主要贡献在于提供了大规模细粒度标注数据集和高效评估方法，但未涉及污染检查或人类基线校准等评测方法学细节。
- **为什么值得看**: 该论文提供了一个大规模、细粒度标注的基准数据集，并验证了自动评估方法的效率与有效性，对评测方法学中'细粒度构念覆盖'和'评估成本'问题有参考价值，但缺乏对评估方法本身的统计可靠性或偏差分析。
- **关键技术**: `benchmark construction`, `human annotation`, `balanced sampling`, `data re-annotation`, `efficient evaluation`

### 11. FineVAU: A Novel Human-Aligned Benchmark for Fine-Grained Video Anomaly Understanding
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37790) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37790/41752)
- **作者**: Joao Alexandre Cardeira Pereira, Vasco Lopes, João C. Neves, David Semedo
- **会议/来源**: AAAI 2026 · Track 10
- 相关性 8/10 · `benchmark`
- **测什么**: 视频异常理解中事件、实体和位置的细粒度视觉元素覆盖度
- **摘要**: FineVAU 是一个面向细粒度视频异常理解（VAU）的新基准，将任务分解为事件（What）、参与实体（Who）和位置（Where）三个维度。作者提出 FV-Score 指标，通过检测 LVLM 回答中是否包含关键视觉元素来评估事实相关性，而非仅依赖语言质量；同时构建了 FineW³ 数据集，通过全自动流程扩充现有标注，加入细粒度视觉信息。人类评估显示 FV-Score 与人类对异常的感知一致性优于 BLEU/ROUGE-L 和 LLM-based 评估。实验揭示 LVLM 在需要空间和细粒度时间理解的异常事件上存在明显缺陷，尽管在粗粒度、静态信息和强视觉线索事件上表现良好。
- **为什么值得看**: 该论文提出了一种新的评估指标 FV-Score，并验证了其与人类判断的一致性，为视频异常理解任务提供了可复用的细粒度评估方法，同时揭示了现有 n-gram 和 LLM-based 指标在事实相关性上的不足。
- **关键技术**: `benchmark construction`, `human evaluation`, `metric validation`, `fine-grained annotation`, `LLM-based evaluation comparison`

### 12. GEMA-Score: Granular Explainable Multi-Agent Scoring Framework for Radiology Report Evaluation
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38302) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38302/42264)
- **作者**: Zhenxuan Zhang, KinHei Lee, Peiyuan Jing, Weihang Deng, Huichi Zhou, Zihao Jin, Jiahao Huang, Zhifan Gao et al.
- **会议/来源**: AAAI 2026 · Track 15
- 相关性 8/10 · `evaluation_method`
- **测什么**: 放射学报告生成的临床可靠性，包括诊断准确性、位置、严重性、不确定性以及文本质量。
- **摘要**: GEMA-Score 提出一个基于 LLM 多智能体工作流的放射学报告评估框架，旨在解决现有指标在临床可靠性上的不足。它通过多个智能体交互，对结构化报告进行客观量化（疾病诊断、位置、严重性、不确定性）和主观评估（完整性、可读性、临床术语），并提供可解释的反馈。在 ReXVal 和 RadEvalX 公共数据集上，GEMA-Score 与人类专家的 Kendall 相关系数分别达到 0.69 和 0.45，优于现有方法。该工作强调了评估的可解释性和细粒度，但未报告人类基线规模或标注者间一致性，也未进行污染检查。
- **为什么值得看**: 该论文展示了如何将多智能体 LLM 用于医学报告评估，并验证了与人类专家的相关性，为 LLM-as-judge 在专业领域的应用提供了案例，但其方法学贡献有限，缺乏对评估信度和效度的深入分析。
- **关键技术**: `multi-agent workflow`, `LLM-as-judge`, `human correlation`, `explainable scoring`

### 13. Inference Scaling Law for Retrieval Augmented Generation
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38692) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38692/42654)
- **作者**: Shu Zhou, Yuxuan Ao, Yunyang Xuan, Xin Wang, Tao Fan, Hao Wang
- **会议/来源**: AAAI 2026 · Track 19
- 相关性 8/10 · `analysis`
- **测什么**: RAG推理性能随检索器规模、生成器规模、文档数和上下文长度的缩放规律
- **摘要**: 本文系统研究检索增强生成（RAG）在推理阶段的缩放规律，考察检索器规模、生成器规模、检索文档数和上下文窗口长度四个因素对性能的影响。基于多个基准数据集的大量实验，作者发现性能与这些因素间存在幂律和S型关系，并构建了带理论依据的联合推理缩放定律。该定律可用于预测不同计算资源下RAG模型的性能趋势，为高效部署提供指导。方法学贡献在于将缩放定律从训练阶段拓展到推理阶段，并给出了可验证的定量关系。
- **为什么值得看**: 为RAG评测提供了预测性框架，可帮助研究者理解资源投入与性能增益的边际效应，对评测中的资源分配和实验设计有方法学参考价值。
- **关键技术**: `scaling law`, `power-law fitting`, `sigmoid fitting`, `joint scaling model`

### 14. JRDB-Reasoning: A Difficulty-Graded Benchmark for Visual Reasoning in Robotics
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37443) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37443/41405)
- **作者**: Simindokht Jahangard, Mehrzad Mohammadi, Yi Shen, Zhixi Cai, Hamid Rezatofighi
- **会议/来源**: AAAI 2026 · Track 7
- 相关性 8/10 · `benchmark`
- **测什么**: 视觉语言模型在多人场景中不同复杂度下的视觉推理能力。
- **摘要**: JRDB-Reasoning 是一个面向机器人视觉推理的难度分级基准，基于 JRDB 数据集扩展了人-物交互和几何关系标注。它形式化了推理复杂度的定义，并引入自适应查询引擎，可生成不同难度、可定制的题目，且附带逐步推理的工作流标注。基准包含约 1,000 个问题，覆盖多个难度层级，用于细粒度评估视觉语言模型（VLMs）的推理能力。论文报告了多个 VLM 在基准上的表现，显示模型在低难度任务上表现较好，但在高难度任务上显著下降，验证了难度分级的有效性。方法学贡献在于提供了可复用的推理复杂度定义和查询引擎，但未报告人类基线或污染检查。
- **为什么值得看**: 该论文提出了推理复杂度的形式化定义和自适应查询引擎，为视觉推理基准的难度校准提供了可复用的方法学框架，但缺乏人类基线和污染检查，限制了其效度论证的完整性。
- **关键技术**: `difficulty grading`, `adaptive query engine`, `step-by-step reasoning annotations`, `benchmark construction`

### 15. LongT2IBench: A Benchmark for Evaluating Long Text-to-Image Generation with Graph-structured Annotations
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38168) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38168/42130)
- **作者**: Zhichao Yang, Tianjiao Gu, Jianjie Wang, Feiyu Lin, Xiangfei Sheng, Pengfei Chen, Leida Li
- **会议/来源**: AAAI 2026 · Track 14
- 相关性 8/10 · `benchmark`
- **测什么**: 长文本到图像生成中图像与文本的细粒度对齐程度（实体、属性、关系层面）。
- **摘要**: LongT2IBench 是一个面向长文本到图像（T2I）生成的对齐评测基准，包含 14K 个长文本-图像对，并配有图结构的人工标注。针对长提示细节密集的特点，作者设计了 Generate-Refine-Qualify 标注协议，将长提示转换为包含实体、属性和关系的文本图结构，并基于这些细粒度元素进行对齐标注。标注结果可转化为对齐分数和解释，支持可解释的评测。基于该基准，作者提出 LongT2IExpert，通过层级对齐链式思维（CoT）指令微调多模态大模型，使其能输出定量分数和结构化解释。实验表明 LongT2IExpert 在评估对齐和解释方面优于现有方法。该工作为长 T2I 评测提供了细粒度、可解释的标注方案，但未报告人类基线一致性或污染检查。
- **为什么值得看**: 该基准将长提示分解为图结构，实现了细粒度、可解释的对齐标注，为评测长文本条件下的图像生成提供了新的构念操作化方法，并展示了如何将结构化标注转化为可训练的评估模型。
- **关键技术**: `graph-structured annotation`, `chain-of-thought`, `instruction tuning`, `human annotation protocol`

### 16. Measuring What Matters: Scenario-Driven Evaluation for Trajectory Predictors in Autonomous Driving
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/36978) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/36978/40940)
- **作者**: Longchao Da, David Isele, Hua Wei, Manish Saroya
- **会议/来源**: AAAI 2026 · Track 1
- 相关性 8/10 · `evaluation_method`
- **测什么**: 轨迹预测器在关键场景下的精度与多样性综合表现，及其对自车驾驶性能的贡献
- **摘要**: 本文针对自动驾驶轨迹预测器的评测提出场景驱动（scenario-driven）的评估流程，主张传统误差指标（ADE/FDE）仅反映事后精度，忽略预测器对自车（SDV）决策的实际影响，尤其在复杂交互场景中，预测器应同时捕捉邻车所有可能运动方向以支持谨慎决策。作者基于场景关键性（criticality）动态组合精度与多样性两个维度，生成最终评分；在真实世界数据集的闭环基准上实验，显示该流程比传统指标更能反映预测器评估与自车驾驶性能的相关性。方法学贡献在于将评测从单一误差转向多维度、场景自适应的综合评分，并验证了其与下游驾驶性能的关联。
- **为什么值得看**: 该论文提出了一种新的评测维度组合方式（精度+多样性，按场景关键性动态加权），并验证了评测分数与下游任务性能的相关性，对评测效度（construct validity）有直接贡献，可作为任务特定评测方法学的参考。
- **关键技术**: `scenario-driven evaluation`, `adaptive weighting`, `closed-loop benchmark`, `accuracy-diversity tradeoff`, `construct validity`

### 17. MicroEvoEval: A Systematic Evaluation Framework for Image-Based Microstructure Evolution Prediction
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37130) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37130/41092)
- **作者**: Qinyi Zhang, Duanyu Feng, Ronghui Han, Yangshuai Wang, Hao Wang
- **会议/来源**: AAAI 2026 · Track 2
- 相关性 8/10 · `benchmark`
- **测什么**: 图像型微观组织演化预测的数值精度、物理保真度、长期稳定性与计算效率
- **摘要**: MicroEvoEval 是首个面向图像型微观组织演化预测的标准化评测框架，覆盖四个代表性任务，并分别构造了短期与长期评估的数据集。作者系统比较了 14 个模型，包括领域专用模型与通用时空架构（如 VMamba），评测维度不仅包括数值精度和计算成本，还引入了一组结构保持指标来评估物理保真度。关键发现是 VMamba 等现代架构在长期稳定性和物理保真度上更优，且计算效率高一个数量级。该工作填补了该领域缺乏统一基准的空白，并强调了多维度整体评测的必要性。
- **为什么值得看**: 该论文提出了一个多维度评测框架，将物理保真度指标纳入图像预测评估，并区分短期与长期误差传播，为领域基准的构念覆盖和评测维度设计提供了可借鉴的范例。
- **关键技术**: `benchmark construction`, `multi-faceted evaluation`, `structure-preserving metrics`, `error propagation analysis`, `model comparison`

### 18. Multigranular Evaluation for Brain Visual Decoding
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38845) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38845/42807)
- **作者**: Weihao Xia, Cengiz Oztireli
- **会议/来源**: AAAI 2026 · Track 21
- 相关性 8/10 · `evaluation_method`
- **测什么**: 脑视觉解码结果在结构保真度、语义对齐和上下文连贯性上的多粒度视觉相似度。
- **摘要**: 该论文提出 BASIC，一个针对脑视觉解码的统一多粒度评测框架，旨在弥补现有粗粒度指标（如像素级或高层语义相似度）无法区分模型间细微差异、缺乏神经科学依据的不足。框架在结构层面引入基于分割的分层指标套件，包括前景、语义、实例和组件掩码，并通过粒度感知的对应关系量化结构保真度；在语义层面利用多模态大语言模型提取包含对象、属性和关系的结构化场景表示，实现与真实刺激的详细、可扩展且上下文丰富的比较。作者在多个刺激-神经影像数据集上对多种视觉解码方法进行了基准测试，验证了该框架的判别力、可解释性和全面性。论文的主要贡献在于提出了一种新的评测方法学，而非报告特定模型的性能。
- **为什么值得看**: 该论文直接回应了评测方法学中的核心问题：粗粒度指标导致的测量不敏感和构念覆盖不足。它通过分层结构指标和LLM提取的语义表示，提供了更细粒度和可解释的评测维度，并展示了跨数据集的可复用性，对评测设计具有方法论价值。
- **关键技术**: `multigranular evaluation`, `segmentation-based metrics`, `LLM-based scene representation`, `cross-dataset benchmarking`

### 19. NoReGeo: Non-Reasoning Geometry Benchmark
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38960) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38960/42922)
- **作者**: Irina Abdullaeva, Anton Vasiliuk, Elizaveta Goncharova, Temurbek Rahmatullaev, Zagorulko Ivan, Maxim Kurkin, Andrey Kuznetsov
- **会议/来源**: AAAI 2026 · Track 23
- 相关性 8/10 · `benchmark`
- **测什么**: LLM 在不依赖推理或代数计算的情况下，对空间关系和几何属性的原生理解能力。
- **摘要**: NoReGeo 是一个评估 LLM 内在几何理解能力（而非推理或代数计算）的基准，包含 2,500 道简单几何问题，覆盖 25 个类别，每题设计为仅凭已知物体位置即可通过原生几何理解解答。作者测试了包括 GPT-4 在内的前沿模型，发现即使在二分类任务上，最高准确率也仅为 65%，表明当前模型缺乏真正的几何认知。消融实验显示，仅通过微调无法获得这种几何理解，需要专门的训练方法。该基准揭示了 LLM 在几何概念上的显著缺陷，为未来研究提供了基础。
- **为什么值得看**: 该基准聚焦于测量'原生几何理解'这一构念，通过设计无需推理的题目来隔离能力，并报告了人类基线和污染检查（未明确提及，但题目构造简单且非推理导向），为评测方法学提供了如何分离推理与内在知识的新思路。
- **关键技术**: `benchmark construction`, `ablation study`, `human baseline`, `binary classification`

### 20. Rethinking Explanation Evaluation Under the Retraining Scheme
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/39065) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/39065/43027)
- **作者**: Yi Cai, Thibaud Ardoin, Mayank Gulati, Gerhard Wunder
- **会议/来源**: AAAI 2026 · Track 24
- 相关性 8/10 · `evaluation_method`
- **测什么**: 衡量特征归因解释在重训练方案下的评估可靠性，并诊断其与理论预期不一致的根源。
- **摘要**: 本文重新审视基于重训练（retraining）的归因解释评估方案 ROAR，指出其评估结果常与公认解释器的理论预期相矛盾。作者识别出“符号问题”（Sign issue）是导致残差信息并扭曲评估的关键因素，并提出对评估流程进行简单重构即可解决该问题。在此基础上，作者提出多个新变体，构建了更全面的解释评估视角，显著提升了评估效率，使其更适用于解释器选择和基准测试。实验在不同数据规模上验证了新方案，并揭示了可解释性研究中的开放挑战。
- **为什么值得看**: 该论文深入剖析了基于重训练的解释评估方案（ROAR）的失效机制，识别出符号问题这一关键偏差来源，并提出了改进的评估变体，为解释评估方法学提供了可复用的诊断和修正框架，对理解评估指标的有效性具有直接价值。
- **关键技术**: `retraining-based evaluation`, `feature attribution`, `sign issue analysis`, `evaluation efficiency`, `benchmarking`

## 全部收录

共 123 篇，按分数排序：[1](all.md)
