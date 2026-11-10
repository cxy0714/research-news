# AAAI 2026 · 评测方法学

> 本页 8 篇（该主题共 8 篇），按相关性排序。 [返回总览](../index.md)

### 1. ELSPR: Evaluator LLM Training Data Self-Purification on Non-Transitive Preferences via Tournament Graph Reconstruction
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38857) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38857/42819)
- **作者**: Yan Yu, Yilun Liu, Minggui He, Shimin Tao, Weibin Meng, Xinhua Yang, Li Zhang, Hongxia Ma et al.
- **会议/来源**: AAAI 2026 · Track 21
- 相关性 9/10 · `evaluation_method`
- **测什么**: 成对偏好评估中的非传递性和偏好清晰度（数据质量）
- **摘要**: 本文针对 LLM 成对评估中非传递偏好（A>B, B>C, C>A）破坏排名可靠性的问题，提出 ELSPR 框架，将偏好数据建模为锦标赛图，通过强连通分量（SCC）分析量化非传递性，并引入归一化有向图结构熵度量偏好清晰度。方法通过过滤诱导非传递性的低质量偏好对来净化训练数据，在 AlpacaEval 基准上微调模型后，非传递性降低 13.8%，结构熵下降 0.088，判别力显著提升。人类验证显示，被丢弃的数据与保留数据相比，标注者间一致性（34.4% vs 52.6%）和模型-人类一致性（51.2% vs 80.6%）均大幅降低，支持了过滤的有效性。该工作为偏好数据质量控制和评估一致性提供了图论驱动的可复用方法。
- **为什么值得看**: 该论文直接针对评估方法学中的核心问题——非传递偏好对排名可靠性的影响，并提供了基于图论的数据净化流程，可复用于偏好数据质量审计和 LLM-as-judge 训练数据筛选，对测量效度有具体贡献。
- **关键技术**: `tournament graph`, `strongly connected components`, `structural entropy`, `data filtering`, `inter-annotator agreement`

### 2. ARCHE: A Novel Task to Evaluate LLMs on Latent Reasoning Chain Extraction
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37170) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37170/41132)
- **作者**: Pengze Li, Jiaqi Liu, Junchi Yu, Lihao Liu, Mingyu Ding, Wanli Ouyang, Shixiang Tang, Xi Chen
- **会议/来源**: AAAI 2026 · Track 3
- 相关性 8/10 · `benchmark`
- **测什么**: 模型将科学论证分解为标准推理范式（演绎、归纳、溯因）并构建逻辑树的能力。
- **摘要**: ARCHE 提出一个名为“潜在推理链抽取”的新任务，要求模型将复杂科学论证分解为基于皮尔士三种推理模式（演绎、归纳、溯因）的推理逻辑树（RLT），每个推理步骤需显式分类。作者基于 70 篇 Nature Communications 文章构建了 ARCHE Bench，包含超过 1900 个引用和 38000 个观点，并设计了两个逻辑感知指标：实体覆盖率（EC）衡量内容完整性，推理边准确率（REA）衡量逐步逻辑有效性。对 10 个领先 LLM 的评估显示，模型在 REA 和 EC 之间存在权衡，且没有一个能提取出完整且标准的推理链，揭示了当前推理模型与科学论证严谨性之间的显著差距。该工作提供了新的任务定义、基准和指标，但未报告人类基线或标注者间一致性，也未进行污染检查。
- **为什么值得看**: 该论文提出了一个全新的评测任务和两个逻辑感知指标，为评测模型对科学推理范式的理解提供了新视角，但其评测方法学贡献有限，缺乏人类基线和信度验证，可作为构造性效度分析的案例。
- **关键技术**: `benchmark construction`, `logic-aware metrics`, `reasoning tree extraction`, `human baseline (absent)`

### 3. Detecting Emotional Dynamic Trajectories: An Evaluation Framework for Emotional Support in Language Models
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37189) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37189/41151)
- **作者**: Zhouxing Tan, Ruochong Xiong, Yulong Wan, Jinlong Ma, Hanlin Xue, Qichun Deng, Haifeng Jing, Zhengtong Zhang et al.
- **会议/来源**: AAAI 2026 · Track 3
- 相关性 8/10 · `benchmark`
- **测什么**: 衡量模型在长期对话中改善和稳定用户情绪状态的能力
- **摘要**: 该论文提出一个面向大模型情感支持能力的轨迹级评测框架，将评测从静态快照转向动态轨迹，关注模型能否随时间改善并稳定用户情绪状态。基准包含328个情绪情境和1152个扰动事件，模拟真实对话中的情绪波动；通过引入情境选择、认知重评等心理学验证的情绪调节策略约束模型输出，以鼓励心理学上合理的回应。用户情绪轨迹被建模为一阶马尔可夫过程，并采用因果调整的情绪估计获得无偏的情绪状态追踪。提出三个轨迹级指标：基线情绪水平（BEL）、情绪轨迹波动性（ETV）和情绪中心位置（ECP），综合刻画用户情绪动态。在多个LLM上的评估显示情绪支持能力存在显著差异，并为模型开发提供可操作见解。
- **为什么值得看**: 该框架将评测从静态快照转向动态轨迹，并引入因果调整的情绪估计和轨迹级指标，为长期交互能力的测量提供了新思路，对评测方法学有参考价值。
- **关键技术**: `trajectory-based evaluation`, `causal adjustment`, `first-order Markov process`, `psychologically grounded constraints`, `trajectory-level metrics`

### 4. NoReGeo: Non-Reasoning Geometry Benchmark
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38960) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38960/42922)
- **作者**: Irina Abdullaeva, Anton Vasiliuk, Elizaveta Goncharova, Temurbek Rahmatullaev, Zagorulko Ivan, Maxim Kurkin, Andrey Kuznetsov
- **会议/来源**: AAAI 2026 · Track 23
- 相关性 8/10 · `benchmark`
- **测什么**: LLM 在不依赖推理或代数计算的情况下，对空间关系和几何属性的原生理解能力。
- **摘要**: NoReGeo 是一个评估 LLM 内在几何理解能力（而非推理或代数计算）的基准，包含 2,500 道简单几何问题，覆盖 25 个类别，每题设计为仅凭已知物体位置即可通过原生几何理解解答。作者测试了包括 GPT-4 在内的前沿模型，发现即使在二分类任务上，最高准确率也仅为 65%，表明当前模型缺乏真正的几何认知。消融实验显示，仅通过微调无法获得这种几何理解，需要专门的训练方法。该基准揭示了 LLM 在几何概念上的显著缺陷，为未来研究提供了基础。
- **为什么值得看**: 该基准聚焦于测量'原生几何理解'这一构念，通过设计无需推理的题目来隔离能力，并报告了人类基线和污染检查（未明确提及，但题目构造简单且非推理导向），为评测方法学提供了如何分离推理与内在知识的新思路。
- **关键技术**: `benchmark construction`, `ablation study`, `human baseline`, `binary classification`

### 5. Rethinking Explanation Evaluation Under the Retraining Scheme
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/39065) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/39065/43027)
- **作者**: Yi Cai, Thibaud Ardoin, Mayank Gulati, Gerhard Wunder
- **会议/来源**: AAAI 2026 · Track 24
- 相关性 8/10 · `evaluation_method`
- **测什么**: 衡量特征归因解释在重训练方案下的评估可靠性，并诊断其与理论预期不一致的根源。
- **摘要**: 本文重新审视基于重训练（retraining）的归因解释评估方案 ROAR，指出其评估结果常与公认解释器的理论预期相矛盾。作者识别出“符号问题”（Sign issue）是导致残差信息并扭曲评估的关键因素，并提出对评估流程进行简单重构即可解决该问题。在此基础上，作者提出多个新变体，构建了更全面的解释评估视角，显著提升了评估效率，使其更适用于解释器选择和基准测试。实验在不同数据规模上验证了新方案，并揭示了可解释性研究中的开放挑战。
- **为什么值得看**: 该论文深入剖析了基于重训练的解释评估方案（ROAR）的失效机制，识别出符号问题这一关键偏差来源，并提出了改进的评估变体，为解释评估方法学提供了可复用的诊断和修正框架，对理解评估指标的有效性具有直接价值。
- **关键技术**: `retraining-based evaluation`, `feature attribution`, `sign issue analysis`, `evaluation efficiency`, `benchmarking`

### 6. Rethinking Saliency Maps: A Cognitive Human Aligned Taxonomy and Evaluation Framework for Explanations
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37375) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37375/41337)
- **作者**: Yehonatan Elisha, Seffi Cohen, Oren Barkan, Noam Koenigstein
- **会议/来源**: AAAI 2026 · Track 5
- 相关性 8/10 · `evaluation_method`
- **测什么**: 显著性图解释在参考框架和粒度维度上的忠实度
- **摘要**: 本文提出 RFxG 分类法，从参考框架（逐点 vs 对比）和粒度（类别级 vs 组级）两个轴来定义显著性图解释的语义，并指出现有评估指标主要关注逐点忠实度，忽视了对比推理和语义粒度。作者设计了四个新的忠实度指标，系统评估解释质量，覆盖 10 种 SOTA 方法、4 种模型架构和 3 个数据集。该工作从模型中心转向用户意图驱动的评估，为解释评估提供了概念基础和实用工具。
- **为什么值得看**: 该论文直接挑战了现有显著性图评估指标的构念效度，提出基于用户查询意图的分类法，并引入新的忠实度指标，为解释性评估提供了可复用的框架，对评测方法学有重要价值。
- **关键技术**: `taxonomy construction`, `faithfulness metrics`, `user-intent-driven evaluation`, `multi-dimensional evaluation`

### 7. False Positives Matter: Multidimensional Localization Evaluation and Training-Free Explainable Adversarial Patch Defense
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37474) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37474/41436)
- **作者**: Lihua Jing, Rui Wang, Jinwen Zhong, Runbo Li, Zixuan Zhu
- **会议/来源**: AAAI 2026 · Track 7
- 相关性 7/10 · `evaluation_method`
- **测什么**: 对抗补丁防御的定位精度、假阳性率与召回能力
- **摘要**: 本文针对对抗补丁防御评估中忽视假阳性补丁的问题，提出一个多维度的补丁定位评估框架，量化假阳性、召回率和整体定位精度，为防御方法提供更全面的比较视角。基于假阳性源于语义理解不足的观察，作者提出无需训练的语义感知可解释防御方法 SATED，通过构建补丁推理链实现零样本定位、误检纠正和决策解释，并集成文本引导的补丁修复。在数字与物理场景、检测与分割任务以及多种对抗补丁上的实验表明，该方法显著降低假阳性，并将整体定位精度提升一倍，同时增强泛化性和可解释性。该工作对评测方法学的贡献在于揭示了现有防御评估仅关注核心指标而忽略假阳性这一测量盲区，并提供了多维评估框架。
- **为什么值得看**: 该论文提出了一个多维评估框架，将假阳性纳入对抗补丁防御的测量，弥补了现有评估只关注核心指标的构念覆盖缺口，对评测方法学有直接参考价值。
- **关键技术**: `multidimensional evaluation framework`, `false positive quantification`, `zero-shot patch localization`, `text-guided inpainting`, `explainable defense`

### 8. Truth-Tracking Evaluation in Opinion-Based Argumentation
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/39012) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/39012/42974)
- **作者**: Juliete Rossie, Jérôme Delobelle, Sébastien Konieczny, Srdjan Vesic
- **会议/来源**: AAAI 2026 · Track 23
- 相关性 7/10 · `evaluation_method`
- **测什么**: 集体意见语义在模拟审议条件下选出与真实事实一致的论证集合的能力（真理追踪性能）。
- **摘要**: 本文在基于观点的论证框架（OBA）中正式定义了真理追踪问题，并提出了VAST评估框架，用于系统评估集体意见语义（COS）的认知充分性。VAST通过模拟不同的审议条件（如投票与论证的交互、意见分布）来测试COS能否选出与真实事实一致的论证集合。实证分析显示，不同COS在真理追踪性能上存在显著差异，且该差异受审议条件影响。该工作为集体推理系统的评测提供了可复用的模拟框架和指标，但未涉及人类基线或污染检查。
- **为什么值得看**: 该论文为集体推理/论证系统的评测提供了可复用的模拟框架（VAST），并系统比较了不同语义在真理追踪上的表现，对评测方法学中'构念效度'（如何定义并测量'真理追踪'）有参考价值。
- **关键技术**: `simulation-based evaluation`, `construct validity`, `benchmark construction`
