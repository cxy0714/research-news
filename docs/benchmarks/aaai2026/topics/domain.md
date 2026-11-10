# AAAI 2026 · 领域基准

> 本页 9 篇（该主题共 9 篇），按相关性排序。 [返回总览](../index.md)

### 1. BAG: Benchmarking Anomaly Detection on Dynamic Graphs
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38510) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38510/42472)
- **作者**: Fengrui Hua, Yiyan Qi, Zikai Wei, Yuxing Tian, Chengjin Xu, Xiaojun Wu, Jia Li, Jian Guo
- **会议/来源**: AAAI 2026 · Track 17
- 相关性 8/10 · `benchmark`
- **测什么**: 动态图中边级和节点级异常的检测能力，以及模型对合成与有机异常的区分度。
- **摘要**: BAG 是首个面向动态图异常检测（DyGAD）的系统性基准，覆盖 25 个主流模型（含经典方法与动态图神经网络 DGNN）和 10 个真实数据集，数据集同时包含合成异常与自然发生的异常，支持边级和节点级两种评估粒度。主要发现是连续时间动态图（CTDG）模型在边异常检测上显著优于离散时间动态图（DTDG）模型；同时，现有方法对有机（自然）异常的检测效果较差，归因于时间异常的存在和高度不平衡的样本。基准在数据集选择、指标应用和模型训练方面做了改进，并开源了所有模型、数据集和评估协议以支持可复现性。该工作为 DyGAD 提供了统一的评测框架，但未涉及污染检查或人类基线等评测方法学细节。
- **为什么值得看**: 该基准统一了动态图异常检测的评测协议，明确了不同模型族（CTDG vs DTDG）的能力差异，并揭示了现有方法在有机异常上的系统性短板，为后续评测设计提供了任务难度校准和样本不平衡处理的参考。
- **关键技术**: `benchmark construction`, `multi-dataset evaluation`, `model comparison`, `open-source repository`

### 2. GEMA-Score: Granular Explainable Multi-Agent Scoring Framework for Radiology Report Evaluation
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38302) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38302/42264)
- **作者**: Zhenxuan Zhang, KinHei Lee, Peiyuan Jing, Weihang Deng, Huichi Zhou, Zihao Jin, Jiahao Huang, Zhifan Gao et al.
- **会议/来源**: AAAI 2026 · Track 15
- 相关性 8/10 · `evaluation_method`
- **测什么**: 放射学报告生成的临床可靠性，包括诊断准确性、位置、严重性、不确定性以及文本质量。
- **摘要**: GEMA-Score 提出一个基于 LLM 多智能体工作流的放射学报告评估框架，旨在解决现有指标在临床可靠性上的不足。它通过多个智能体交互，对结构化报告进行客观量化（疾病诊断、位置、严重性、不确定性）和主观评估（完整性、可读性、临床术语），并提供可解释的反馈。在 ReXVal 和 RadEvalX 公共数据集上，GEMA-Score 与人类专家的 Kendall 相关系数分别达到 0.69 和 0.45，优于现有方法。该工作强调了评估的可解释性和细粒度，但未报告人类基线规模或标注者间一致性，也未进行污染检查。
- **为什么值得看**: 该论文展示了如何将多智能体 LLM 用于医学报告评估，并验证了与人类专家的相关性，为 LLM-as-judge 在专业领域的应用提供了案例，但其方法学贡献有限，缺乏对评估信度和效度的深入分析。
- **关键技术**: `multi-agent workflow`, `LLM-as-judge`, `human correlation`, `explainable scoring`

### 3. MicroEvoEval: A Systematic Evaluation Framework for Image-Based Microstructure Evolution Prediction
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37130) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37130/41092)
- **作者**: Qinyi Zhang, Duanyu Feng, Ronghui Han, Yangshuai Wang, Hao Wang
- **会议/来源**: AAAI 2026 · Track 2
- 相关性 8/10 · `benchmark`
- **测什么**: 图像型微观组织演化预测的数值精度、物理保真度、长期稳定性与计算效率
- **摘要**: MicroEvoEval 是首个面向图像型微观组织演化预测的标准化评测框架，覆盖四个代表性任务，并分别构造了短期与长期评估的数据集。作者系统比较了 14 个模型，包括领域专用模型与通用时空架构（如 VMamba），评测维度不仅包括数值精度和计算成本，还引入了一组结构保持指标来评估物理保真度。关键发现是 VMamba 等现代架构在长期稳定性和物理保真度上更优，且计算效率高一个数量级。该工作填补了该领域缺乏统一基准的空白，并强调了多维度整体评测的必要性。
- **为什么值得看**: 该论文提出了一个多维度评测框架，将物理保真度指标纳入图像预测评估，并区分短期与长期误差传播，为领域基准的构念覆盖和评测维度设计提供了可借鉴的范例。
- **关键技术**: `benchmark construction`, `multi-faceted evaluation`, `structure-preserving metrics`, `error propagation analysis`, `model comparison`

### 4. CMedBench: A Comprehensive Benchmark for Efficient Medical Large Language Models
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/39264) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/39264/43225)
- **作者**: Shengbo Gao, Jinyang Guo, Lixian Su, Yifu Ding, Shiqiao Gu, Aishan Liu, Yuqing Ma, Zhiwang Zhang et al.
- **会议/来源**: AAAI 2026 · Track 25
- 相关性 7/10 · `benchmark`
- **测什么**: 压缩医学大模型在知识、应用、可信赖性、压缩组合及计算效率五个维度的综合表现。
- **摘要**: CMedBench 是首个面向医学场景下压缩大模型（如量化、剪枝、蒸馏）的综合评测基准，旨在系统评估压缩对医学 LLM 临床能力的影响。基准覆盖五个核心维度：医学知识能力、医学应用能力、可信赖性维持、压缩交叉组合和计算效率，通过多模型、多数据集和多压缩策略的实证研究，分析效率与临床性能之间的权衡。论文揭示了当前评测实践的关键局限，并提供了将压缩策略与医学需求对齐的框架。具体规模（题目数、模型数等）未在摘要中给出，但作为首个此类基准，其方法学贡献在于将压缩效率与医学能力、可信赖性纳入统一评测框架。
- **为什么值得看**: 该基准首次系统性地将模型压缩（效率）与医学能力、可信赖性纳入同一评测框架，为评测压缩模型时的测量维度设计提供了可参考的构念覆盖思路，并指出了现有评测实践在压缩场景下的不足。
- **关键技术**: `benchmark construction`, `multi-dimensional evaluation`, `compression strategy analysis`, `efficiency-performance trade-off`

### 5. Complex Mathematical Expression Recognition: Benchmark, Large-Scale Dataset and Strong Baseline
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37224) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37224/41186)
- **作者**: Weikang Bai, Yongkun Du, Yuchen Su, Yazhen Xie, Zhineng Chen
- **会议/来源**: AAAI 2026 · Track 4
- 相关性 7/10 · `benchmark`
- **测什么**: 数学表达式识别模型在不同复杂度（简单、中等、复杂）下的识别准确率与鲁棒性。
- **摘要**: 本文针对复杂数学表达式识别（MER）提出 CMER-Bench 基准，按难度分为简单、中等、复杂三级，并系统评估了现有 MER 模型与多模态大模型（MLLMs），发现它们在复杂表达式上性能显著下降，归因于现有训练数据以简单样本为主。作者构建了大规模数据集 MER-17M 和 CMER-3M，强调复杂样本的覆盖。为建模复杂空间布局，提出新的表达式分词器和结构化数学语言（Structured Mathematical Language），显式建模层级与空间结构，并基于此训练了 125M 参数的 CMERNet，在 CMER-Bench 上显著超越现有模型。该工作提供了难度分层基准和针对性数据集，但未报告污染检查或人类基线验证。
- **为什么值得看**: 该基准按难度分层设计，有助于分析模型在不同复杂度下的性能退化，为评测构念覆盖和难度校准提供了实例；但缺乏对数据污染和人类基线的验证，限制了其作为评测方法学参考的严谨性。
- **关键技术**: `difficulty stratification`, `benchmark construction`, `large-scale dataset`, `tokenizer design`, `spatial structure modeling`

### 6. FIXME: Towards End-to-End Benchmarking of LLM-Aided Design Verification
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37079) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37079/41041)
- **作者**: Gwok-Waa Wan, SamZaak Wong, Shengchu Su, Chenxu Niu, Ning Wang, Xinlai Wan, Qixiang Chen, Mengnv Xing et al.
- **会议/来源**: AAAI 2026 · Track 2
- 相关性 7/10 · `benchmark`
- **测什么**: LLM 在硬件设计功能验证各子任务（规格理解、测试生成、调试等）上的端到端能力。
- **摘要**: FIXME 是首个面向硬件设计功能验证（FV）的端到端大规模基准，包含 747 个来自真实硬件设计的任务，覆盖规格理解、参考模型生成、测试平台生成、断言设计和 RTL 调试五个子集。数据通过 AI-人类协作框架进行敏捷整理和标注，产出 25,000 行验证过的 RTL、35,000 行增强测试平台和超过 1,200 条 SystemVerilog 断言。在多智能体辅助流程中，专家引导优化使平均功能覆盖率提升 45.57%，验证了基准的稳健性。对 GPT-4.1 等先进模型的评估揭示了关键局限并提供了可操作见解。该基准为硬件验证领域的 LLM 评测提供了首个标准化任务集，但未报告人类基线或污染检查。
- **为什么值得看**: 该基准首次系统覆盖硬件验证的多个子任务，为评测 LLM 在专业工程领域的端到端能力提供了可复用的任务构造和标注流程，但其方法学贡献有限，缺乏对测量效度（如人类基线、难度校准）的深入分析。
- **关键技术**: `benchmark construction`, `AI-human collaborative annotation`, `multi-agent flow`, `functional coverage`

### 7. ReFINE: A Reward-Based Framework for Interpretable and Nuanced Evaluation of Radiology Report Generation
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37680) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37680/41642)
- **作者**: Yunyi Liu, Yingshu Li, Zhanyu Wang, Xinyu Liang, Lingqiao Liu, Lei Wang, Luping Zhou
- **会议/来源**: AAAI 2026 · Track 9
- 相关性 7/10 · `evaluation_method`
- **测什么**: 放射学报告生成质量，包括细粒度标准下的子分数和聚合质量。
- **摘要**: ReFINE 提出一种基于奖励的框架，用于训练可解释的放射学报告生成（R2Gen）评估模型。它通过新颖的边际奖励强制损失，将报告质量分解为用户定义标准下的细粒度子分数，提升可解释性。利用 GPT-4 生成包含成对接受/拒绝报告的多样化训练数据，在奖励系统下训练评估模型。ReFINE Score 提供细粒度子分数和聚合质量评估，支持标准特定评估。实验表明，ReFINE 与人类判断的对齐优于传统指标，在模型选择上表现更佳；其鲁棒性在三个专家标注数据集（包括胸部 X 光和覆盖 9 种影像模态的多模态报告）及两种评分系统下得到验证。
- **为什么值得看**: 该工作直接针对医学报告生成评测中传统指标与人类判断不一致的问题，提出了一种可解释的细粒度评估框架，并验证了与人类判断的对齐性，对评测方法学有参考价值。
- **关键技术**: `reward-based training`, `margin-based loss`, `GPT-4 data generation`, `fine-grained scoring`, `human alignment validation`

### 8. scCluBench: Comprehensive Benchmarking of Clustering Algorithms for Single-Cell RNA Sequencing
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37110) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37110/41072)
- **作者**: Ping Xu, Zaitian Wang, Zhirui Wang, Pengjiang Li, Jiajia Wang, Ran Zhang, Pengfei Wang, Yuanchun Zhou
- **会议/来源**: AAAI 2026 · Track 2
- 相关性 7/10 · `benchmark`
- **测什么**: 单细胞 RNA 测序数据中聚类算法的准确性、鲁棒性、可扩展性及下游任务实用性。
- **摘要**: scCluBench 是一个针对单细胞 RNA 测序（scRNA-seq）聚类算法的综合基准。它整合了来自多个公共来源的 36 个数据集，覆盖多种组织，并统一处理以保证一致性。基准收集并复现了传统、深度学习、图基和生物基础模型等各类聚类方法，使用核心性能指标和可视化分析进行定量与定性评估。此外，它构建了标记基因识别和细胞类型注释等下游生物学任务，以评估实际效用。该基准系统评估了不同聚类模型在多种分析任务中的性能差异、适用边界、鲁棒性和可扩展性，提供了标准化的数据集、统一的评估协议和透明的分析。
- **为什么值得看**: 该基准为 scRNA-seq 聚类评测提供了标准化的数据集和统一的评估协议，解决了现有基准碎片化的问题，并纳入了最新的 AI 方法，对评测方法学有参考价值。
- **关键技术**: `benchmark construction`, `standardized evaluation protocol`, `downstream task evaluation`, `robustness analysis`, `scalability analysis`

### 9. Ψ-Arena: Interactive Assessment and Optimization of LLM-based Psychological Counselors with Tripartite Feedback
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37211) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37211/41173)
- **作者**: Shijing Zhu, Zhuang Chen, Guanqun Bi, Binghang Li, Yaxi Deng, Dazhen Wan, Libiao Peng, Xiyao Xiao et al.
- **会议/来源**: AAAI 2026 · Track 3
- 相关性 7/10 · `evaluation_method`
- **测什么**: 评估 LLM 心理咨询师在多轮对话中的咨询能力，包括共情、问题解决和安全性等维度。
- **摘要**: Ψ-Arena 提出了一个交互式框架，用于评估和优化基于 LLM 的心理咨询师。它通过多阶段对话模拟真实咨询场景，其中 NPC 客户端具有心理画像，并整合了客户端、督导和咨询师三方视角的评估。该框架还支持基于诊断反馈的闭环优化。实验在八个 SOTA LLM 上进行，显示不同场景和评估视角下性能差异显著，基于反思的优化使咨询性能提升高达 141%。该工作为心理健康领域 LLM 应用的可靠评估提供了新范式。
- **为什么值得看**: 该论文针对现有心理咨询评估的静态性、单一视角和开环问题，提出了一个包含多角色评估和闭环优化的交互式评测框架，为复杂交互场景下的评测方法学提供了可复用的设计思路。
- **关键技术**: `interactive evaluation`, `multi-perspective assessment`, `closed-loop optimization`, `NPC simulation`, `reflection-based feedback`
