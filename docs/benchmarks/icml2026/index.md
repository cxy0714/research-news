# ICML 2026 · AI 评测 / Benchmark

> 只收录与「评测 / benchmark」相关的论文：标题命中评测词表（ACL 系另加摘要）后，按**评测方法学价值**打分，取高分做中文精摘。**不是会议全量**。

- 收录 **605** 篇 · 已打分 **605** · 精摘 **29** · 更新于 2026-11-10
- 口径：测量设计 / 构念覆盖 / 污染控制 / 难度校准 / 人类基线 / judge 验证 / 统计可靠性；纯榜单提升不加分。

## 主题分布

| 主题 | 精摘篇数 | 页面 |
|---|---:|---|
| 评测方法学 | 22 | [1](topics/methodology.md) |
| Agent / 工具使用 | 4 | [1](topics/agents_tools.md) |
| 多模态评测 | 2 | [1](topics/multimodal.md) |
| 安全 / 事实性 | 1 | [1](topics/safety_factuality.md) |

## 必读 Top 20

### 1. Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks
- **链接**: [论文页](https://proceedings.mlr.press/v306/li26fx.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26fx/li26fx.pdf) · [OpenReview](https://openreview.net/forum?id=ItJEC1Mk0V)
- **作者**: Peiyu Li, Xiuxiu Tang, Si Chen, Ying Cheng, Ronald Metoyer, Ting Hua, Nitesh V Chawla
- **会议/来源**: ICML 2026 · Main
- 相关性 10/10 · `evaluation_method`
- **测什么**: 模型在给定题库上的潜在能力（latent ability），并据此重建准确率与排名。
- **摘要**: ATLAS 提出一种基于项目反应理论（IRT）的自适应测试框架，用于替代静态基准测试中的固定题集。它利用 Fisher 信息引导的选题策略，在保持测量精度的同时将所需题目数减少高达 90%，例如在 HellaSwag（5600 题）上仅用 41 题即可达到与全题库相当的估计（MAE 0.157）。作者进一步从能力估计中重建准确率，发现重建值与原始准确率在五个基准上高度一致，表明能力估计保留了全局性能结构。此外，ATLAS 在准确率相同的模型中提供了更细粒度的区分：在超过 3000 个模型中，23–31% 的模型排名变动超过 10 位。论文提供了校准的题库和代码，并展示了自适应测试在评测效率与效度上的潜力。
- **为什么值得看**: 该论文将心理测量学中的 IRT 与自适应测试引入 LLM 评测，直接回应了静态基准的测量效率与区分度问题，提供了可复用的题库校准和选题流程，对评测方法学有实质贡献。
- **关键技术**: `Item Response Theory`, `Adaptive Testing`, `Fisher Information`, `Ability Estimation`, `Benchmark Efficiency`

### 2. Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory
- **链接**: [论文页](https://proceedings.mlr.press/v306/choi26n.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/choi26n/choi26n.pdf) · [OpenReview](https://openreview.net/forum?id=6xRIf7H6Nb)
- **作者**: Junhyuk Choi, Sohhyung Park, Chanhee Cho, Hyeonchu Park, Bugeun Kim
- **会议/来源**: ICML 2026 · Main
- 相关性 10/10 · `evaluation_method`
- **测什么**: LLM-as-judge 在提示变化下的稳定性及其与人类评分的一致性
- **摘要**: 本文提出一个基于项目反应理论（IRT）的两阶段诊断框架，用于评估 LLM-as-a-Judge 的可靠性。框架采用等级反应模型（GRM），从两个维度刻画可靠性：内在一致性（在提示变化下测量行为的稳定性）和人类对齐（与人类质量评估的一致性）。作者对七个 LLM 裁判进行了实证检验，表明 IRT-GRM 能提供可解释的信号，用于系统诊断裁判行为，并识别不可靠的潜在原因。该工作将心理测量学方法引入 LLM 裁判验证，超越了仅基于输出层面的验证。
- **为什么值得看**: 该论文将 IRT 应用于 LLM-as-judge 的可靠性诊断，提供了可复用的框架来量化裁判的内在一致性和人类对齐，对评测方法学有直接贡献。
- **关键技术**: `Item Response Theory`, `Graded Response Model`, `LLM-as-Judge`, `reliability diagnosis`, `human alignment`

### 3. A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness
- **链接**: [论文页](https://proceedings.mlr.press/v306/schwinn26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/schwinn26a/schwinn26a.pdf) · [OpenReview](https://openreview.net/forum?id=RgnoWsmYBM)
- **作者**: Leo Schwinn, Moritz Ladenburger, Tim Beyer, Mehrnaz Mofakhami, Gauthier Gidel, Stephan Günnemann
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `meta_evaluation`
- **测什么**: LLM-as-judge在红队攻击下评估有害性的可靠性（与人类标签的一致性）。
- **摘要**: 本文系统审计了LLM-as-judge在红队安全评测中的可靠性，发现现有验证协议未考虑红队场景固有的分布偏移：不同受害模型的生成风格、攻击对输出模式的扭曲、以及越狱场景的语义模糊性，导致judge性能在6642个人工验证标签上常降至接近随机水平，与先前报告的高人类一致性形成鲜明对比。作者进一步指出，许多攻击通过利用judge的缺陷而非真正诱导有害内容来虚增成功率。为此，他们提出ReliableBench（一组更稳定可判的行为基准）和JudgeStressTest（暴露judge失败的数据集），以支持更可靠的评测。
- **为什么值得看**: 该研究揭示了LLM-as-judge在分布偏移下信度崩塌的问题，并提供了可复用的压力测试数据集和基准，对评测方法学中judge验证与污染控制具有直接价值。
- **关键技术**: `LLM-as-judge`, `human-verified labels`, `distribution shift audit`, `adversarial robustness`, `benchmark construction`

### 4. A Judge-Aware Ranking Framework for Evaluating Large Language Models without Ground Truth
- **链接**: [论文页](https://proceedings.mlr.press/v306/xu26ay.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xu26ay/xu26ay.pdf) · [OpenReview](https://openreview.net/forum?id=yFUmcOtUYD)
- **作者**: Mingyuan Xu, Xinzi Tan, Jiawei Wu, Doudou Zhou
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 衡量法官可靠性差异下模型排名的准确性与不确定性校准
- **摘要**: 该论文针对无真实标签的开放任务中LLM-as-judge评测的可靠性问题，提出一种法官感知的排序框架，扩展Bradley-Terry-Luce模型，引入法官特定的区分度参数，联合估计潜在模型质量与法官可靠性，无需参考标签。作者证明了在自然归一化下的可识别性，以及极大似然估计的一致性和渐近正态性，从而为分数差异和排名比较提供置信区间。在多个公开基准和新收集的数据集上，该方法相比未加权基线提高了与人类偏好的一致性，数据效率更高，并产生校准的不确定性量化。
- **为什么值得看**: 该论文直接回应了评测方法学中的核心问题：法官可靠性差异和聚合模型误设定，提供了可复用的统计框架（扩展BTL模型）来校准法官权重并量化排名不确定性，对LLM-as-judge的验证和统计可靠性有重要价值。
- **关键技术**: `Bradley-Terry-Luce model`, `judge-specific discrimination`, `maximum likelihood estimation`, `identifiability`, `confidence intervals`

### 5. AgentSuite: Toward More Reliable Agent Evaluation with a Component-Based Benchmark Auditing Pipeline
- **链接**: [论文页](https://proceedings.mlr.press/v306/suh26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/suh26a/suh26a.pdf) · [OpenReview](https://openreview.net/forum?id=2Exmr1eIKZ)
- **作者**: Hyewon Suh, Binfei Ji, Seojune Lee, Rishi Khare, Basit Khan, Hyunjun Kim, Tianyi Zhang, Venkat Krishna Srinivasan et al.
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: agent 基准中由指令、环境、工具、轨迹和评估协议交互产生的有效性问题（缺陷）
- **摘要**: AgentSuite 提出 COBA，一个组件化的基准审计流水线，用于诊断和过滤 LLM agent 基准中的有效性问题。COBA 将 agent 任务分解为用户、环境、真实轨迹和评估四个标准化组件，并利用混合规则检测器和分类学引导的 LLM 评估来操作化组件级问题分类。在六个广泛使用的 agent 基准上，COBA 与专家判断的 F1 分数在 0.791 到 0.874 之间，表现出强一致性。分析表明基准缺陷普遍存在且显著影响评估结果，COBA 还能以最小适配泛化到未见过的基准。作者发布了 AgentSuite 平台，包含 COBA 流水线和审计后的基准变体。
- **为什么值得看**: 该论文提供了一种可复用的基准审计流程，将任务分解为组件并系统化检测缺陷，直接回应了评测方法学中的效度问题，有助于识别基准伪影与模型错误的混淆。
- **关键技术**: `component-based decomposition`, `rule-based detectors`, `LLM-as-judge`, `taxonomy-guided evaluation`, `benchmark auditing`

### 6. AI Cartography: Mapping the Latent Landscape of AI Benchmark Ecosystems
- **链接**: [论文页](https://proceedings.mlr.press/v306/hardy26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/hardy26a/hardy26a.pdf) · [OpenReview](https://openreview.net/forum?id=Vr4YScS9DT)
- **作者**: Michael Hardy, Anka Reuel, Lijin Zhang, Jodi M. Casabianca, Sang T. Truong, Yash Satish Dave, Hansol Lee, Benjamin W. Domingue et al.
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `analysis`
- **测什么**: benchmark 排名方差的来源与潜在结构的可靠性
- **摘要**: 本文提出一个测量 AI benchmark 生态潜在结构的框架，将验证性因子分析（CFA）和概化理论应用于 Open LLM Leaderboard 上 4000+ 模型的数据，分解排名方差的来源。主要发现包括：当前报告实践假设的结构低估了 benchmark 间关系的强度；存在局部依赖，削弱了将 benchmark 作为测量工具的有效性；贡献者元数据解释了约 9% 的排名相关方差，高于架构或部署类别；显式分数的“缩放定律”斜率可靠性低（R_beta=0.53），而潜在一般因子的大小斜率则高度稳定（R_g=0.97）。该框架还能揭示哪些 benchmark 受模型规模影响、哪些受后训练实践影响，并提供诊断工具以判断排名可信度和改进 benchmark 设计。
- **为什么值得看**: 该论文将心理测量学方法（CFA、概化理论）引入 AI 评测，量化了排名中的测量噪声来源，并揭示了当前评分系统下 benchmark 作为测量工具的效度问题，为评测方法学提供了可复用的方差分解和可靠性诊断流程。
- **关键技术**: `Confirmatory Factor Analysis`, `Generalizability Theory`, `variance decomposition`, `reliability analysis`, `local dependence testing`

### 7. Are LLM Evaluators Really Narcissists? Sanity Checking Self-Preference Evaluations
- **链接**: [论文页](https://proceedings.mlr.press/v306/roytburg26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/roytburg26a/roytburg26a.pdf) · [OpenReview](https://openreview.net/forum?id=sRPyBOSZQk)
- **作者**: Dani Roytburg, Matthew Bozoukov, Matthew Nguyen, Jou Barzdukas, Mackenzie Puig-Hall, Narmeen Fatimah Oozeer
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: LLM评估器在自我评估时是否存在真实的自我偏好偏差，而非由评估器质量差异导致的混淆。
- **摘要**: 该论文质疑了先前关于LLM评估器存在自我偏好（narcissism）的结论，指出这些发现可能混淆了评估器质量与作者身份。作者提出一种新的基线方法：直接比较评估器在评估自身输出与评估其他模型输出时的投票分布，以控制评估器质量的影响。通过重新分析先前数据，发现只有51%的示例在统计上显著支持自我偏好假设，但这些示例覆盖了89.6%的自我偏好概率质量。此外，作者比较了投票分布的熵，表明不确定性驱动的重叠可能解释部分现象。该工作为评估器偏差研究提供了更严谨的统计检验框架，有助于区分真实偏差与混淆因素。
- **为什么值得看**: 该论文直接针对LLM-as-judge评估方法学中的核心问题——自我偏好偏差，提出了一个可复用的统计基线（评估器质量基线）来区分真实偏差与混淆因素，对评测方法学具有重要价值。
- **关键技术**: `statistical significance testing`, `baseline correction`, `voting distribution analysis`, `entropy comparison`, `confound control`

### 8. Benchmarking at the Edge of Comprehension
- **链接**: [论文页](https://proceedings.mlr.press/v306/marro26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/marro26a/marro26a.pdf) · [OpenReview](https://openreview.net/forum?id=BhahZSDowo)
- **作者**: Samuele Marro, Jialin Yu, Emanuele La Malfa, Oishi Deb, Jiawei Li, Yibo Yang, Ebey Abraham, Sunando Sengupta et al.
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 模型在人类无法完全理解的任务上的解决能力与生成困难但可解问题的能力。
- **摘要**: 该论文提出“后理解时代”（post-comprehension regime）的概念，指出当前沿模型在基准测试上迅速饱和、人类难以生成有区分度的任务或提供准确答案时，传统评测将失效。为此，作者提出“批评韧性基准测试”（Critique-Resilient Benchmarking）框架，将正确性定义为“没有对手能令人信服地证明其错误”，人类仅作为有界验证者，对局部声明进行审查，从而在任务超出人类完全理解时仍能保持评测完整性。方法上，采用分项二部 Bradley-Terry 模型，联合排名模型解决难题的能力和生成困难但可解问题的能力。在数学领域对八个前沿 LLM 进行实验，结果显示分数稳定且与外部能力指标相关。该框架将基准测试重构为对抗性生成-评估博弈，人类作为最终裁决者。
- **为什么值得看**: 该论文直接回应基准饱和与人类标注能力上限的方法学挑战，提出一种不依赖完整人类理解的评测框架，并引入对抗性验证与配对比较模型，为评测效度提供了新思路，对测量设计有重要参考价值。
- **关键技术**: `adversarial verification`, `Bradley-Terry model`, `human-as-bounded-verifier`, `critique-resilient correctness`, `benchmark saturation`

### 9. Benchmarking World-Model Learning with Environment-Level Queries
- **链接**: [论文页](https://proceedings.mlr.press/v306/warrier26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/warrier26a/warrier26a.pdf) · [OpenReview](https://openreview.net/forum?id=Ny6UYZ8ysN)
- **作者**: Archana Warrier, Dat Nguyen, Michelangelo Naim, Moksh Jain, Yichao Liang, Karen Schroeder, Cambridge Yang, Joshua B. Tenenbaum et al.
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `benchmark`
- **测什么**: 衡量智能体是否学习到支持多种环境级查询（如可达性、干预效果）的通用世界模型。
- **摘要**: WorldTest 提出一种评测协议，用于检验智能体是否学到支持多种环境级查询的世界模型，而非仅能预测下一帧或优化任务回报。它包含 43 个交互式网格世界环境和 129 个任务，覆盖三个查询族（如可达性、干预效果），这些查询的答案依赖于全局环境结构，无法由单一轨迹分布确定。AutumnBench 作为其实例，同时收集了 517 名人类参与者和五个前沿模型的表现，结果显示人类显著优于模型，差距归因于探索和信念更新方式的差异。该工作强调评测应超越可观测交互属性，关注模型对环境的通用理解能力。
- **为什么值得看**: 该论文提出了一个评测协议，明确区分了从观测轨迹可推断的属性与需要全局环境理解才能回答的查询，为评测世界模型的构念效度提供了新视角；同时通过人类基线和多查询族设计，展示了如何系统评估模型泛化能力，对评测方法学有直接贡献。
- **关键技术**: `benchmark construction`, `human baseline`, `query family design`, `environment-level evaluation`, `exploration analysis`

### 10. CapBencher: Give Your LLM Benchmark a Built-in Alarm for Test-Set Overfitting
- **链接**: [论文页](https://proceedings.mlr.press/v306/ishida26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/ishida26a/ishida26a.pdf) · [OpenReview](https://openreview.net/forum?id=oCNT5PcMSQ)
- **作者**: Takashi Ishida, Thanawat Lodkaew, Ikko Yamane
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 检测模型在 benchmark 上是否因测试集过拟合或数据泄露而超过理论准确率上限。
- **摘要**: CapBencher 提出一种发布 benchmark 的新方法，旨在防止测试集过拟合和标签泄露。其核心思想是：为每个问题准备多个逻辑上正确的答案，但只在基准中公开其中一个作为标准答案，从而降低贝叶斯准确率（即理论上可达到的最高准确率）。由于即使最强模型也不应超过贝叶斯准确率，任何超过该阈值的模型都强烈暗示存在测试集过拟合或数据污染。作者从理论和实验两方面验证了该方法在多种基准、模型和训练场景下能准确检测过拟合。该方法允许公开评估 LLM，同时避免完全披露真实答案，为 benchmark 发布提供了新的安全机制。
- **为什么值得看**: 该论文直接针对 benchmark 评测中的污染与过拟合问题，提出了一种可复用的检测机制（基于贝叶斯准确率阈值），并提供了理论保证和实证验证，对评测方法学有重要贡献。
- **关键技术**: `Bayes accuracy`, `test-set overfitting detection`, `answer randomization`, `theoretical analysis`, `empirical validation`

### 11. CHB: A Diagnostic Toolkit for Hardness-Aware Clustering Evaluation
- **链接**: [论文页](https://proceedings.mlr.press/v306/durani26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/durani26a/durani26a.pdf) · [OpenReview](https://openreview.net/forum?id=9zXUOLxbcL)
- **作者**: Walid Durani, Philipp Jahn, Collin Leiber, David B. Hoffmann, Thomas Seidl, Claudia Plant, Christian Böhm
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 聚类算法在不同数据硬度条件下的性能与鲁棒性，以及表示变化对性能的影响。
- **摘要**: CHB 是一个面向聚类评测的诊断工具包，旨在替代将性能压缩为单一排名的传统榜单。它通过可扩展的持久同调摘要，为每个数据集-表示对生成可解释的硬度指纹，涵盖分离度、内聚性与尺度异质性、拓扑结构三个维度。在该诊断空间内，CHB 在标准化、计算感知的轨道下评估聚类算法，将比较转化为诊断：在广泛的数据集和表示上，它揭示了可复现的结构性机制、跨方法族的机制依赖排名反转，以及包括拓扑相关崩溃在内的鲁棒性特征。CHB 还支持表示审计，将性能提升归因于硬度指纹的可测量变化，而非仅外部性能变化。工具包以开放、可扩展的形式发布，供在共享诊断框架下评估新聚类方法和嵌入。
- **为什么值得看**: 该论文提出了一种基于硬度指纹的条件化评测方法，将聚类性能比较转化为对数据属性与算法失败模式的诊断，为评测方法学提供了可复用的框架，尤其适用于揭示排名反转和鲁棒性特征。
- **关键技术**: `hardness fingerprint`, `persistent homology`, `compute-aware evaluation`, `representation auditing`, `regime-dependent analysis`

### 12. Coverage, Not Averages: Semantic Stratification for Trustworthy Retrieval Evaluation
- **链接**: [论文页](https://proceedings.mlr.press/v306/klearman26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/klearman26a/klearman26a.pdf) · [OpenReview](https://openreview.net/forum?id=Q9LweGI2B9)
- **作者**: Andrew Klearman, Radu Revutchi, Rohin Garg, Rishav Chakravarti, Samuel Marc Denton, Yuan Xue
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 检索评估集的语义覆盖完整性及检索失败模式的结构性差异
- **摘要**: 该论文将检索评估形式化为统计估计问题，指出基于启发式构造的查询集存在内在偏差，限制了指标可靠性。作者提出语义分层（semantic stratification）方法，基于实体簇将语料库组织为可解释的全局空间，并系统生成缺失层的查询，从而提供形式化的语义覆盖保证，并揭示检索失败模式。实验在多个基准和检索方法上验证了框架，暴露了系统性覆盖缺口，识别出解释检索性能方差的结构信号，并表明分层评估比聚合指标更稳定、透明。论文还提供了可复用的评估集构造流程，有助于提升RAG评估的可信度。
- **为什么值得看**: 该论文直接针对评测方法学中的构念覆盖与选择偏差问题，提出了可复用的语义分层评估框架，并给出了覆盖保证与失败模式可见性，对评测设计具有方法论价值。
- **关键技术**: `semantic stratification`, `coverage guarantees`, `entity-based clustering`, `query generation`, `failure mode analysis`

### 13. Cutting LLM Evaluation Costs with SySRs: A Bandit Algorithm That Provably Exploits Model Similarity
- **链接**: [论文页](https://proceedings.mlr.press/v306/lyu26h.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/lyu26h/lyu26h.pdf) · [OpenReview](https://openreview.net/forum?id=vkG1xVVKOH)
- **作者**: Zifan Lyu, Chahine Nejma, Tobias Wegel, Fanny Yang, Florian E. Dorner
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 在有限预算下识别最佳模型的能力，即评测效率与识别可靠性。
- **摘要**: 该论文提出 SySRs（Synchronized Successive Rejects），一种用于大模型评测的自适应预算分配算法，旨在通过最佳臂识别（best-arm identification）降低评测成本。其核心思想是：若某模型明显劣于其他模型，则无需精确估计其性能，从而将预算集中于有竞争力的模型。SySRs 在经典 Successive Rejects 算法基础上引入配对比较，利用模型间对同一提示的相似响应来提升效率，且无需超参数，并提供了随模型相似度提高而改善的性能保证。实验在 15 个标准 benchmark 上验证，SySRs 在平均错误率和识别最佳模型的最坏预算方面均优于基线。该方法为评测成本控制提供了理论上有保证的框架，但未涉及评测内容本身的效度或污染问题。
- **为什么值得看**: 该论文为评测方法学提供了可复用的自适应预算分配框架，将统计上的最佳臂识别与模型相似性结合，直接回应了评测成本与统计可靠性之间的权衡，对大规模模型比较的测量设计有参考价值。
- **关键技术**: `best-arm identification`, `Successive Rejects`, `paired comparisons`, `adaptive budget allocation`, `model similarity`

### 14. DEER: A Benchmark for Evaluating Deep Research Agents on Expert Report Generation
- **链接**: [论文页](https://proceedings.mlr.press/v306/han26m.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/han26m/han26m.pdf) · [OpenReview](https://openreview.net/forum?id=ILRx5neJk6)
- **作者**: Janghoon Han, Heegyu Kim, Changho Lee, Dahm Lee, Min Hyung Park, Hosung Song, Stanley Jungkyu Choi, Moontae Lee et al.
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `benchmark`
- **测什么**: 深度研究智能体生成报告的多维质量（如逻辑完整性、证据质量）及声明准确性。
- **摘要**: DEER 是一个用于评估深度研究智能体生成专家级报告质量的基准。它通过专家开发的分类体系（7 个维度、25 个子维度）操作化为 101 个细粒度评分项，并提供了任务特定的专家评估指南以支持 LLM 作为评判者。除了基于评分项的评估，DEER 还提出了一种声明验证架构，用于验证引用和未引用的声明，并量化证据质量。实验表明，当前系统能生成结构合理、引用证据的报告，但在满足专家级用户需求和逻辑完整性方面仍有不足。DEER 不仅比较性能，还使系统优缺点可解释，并提供改进的诊断信号。
- **为什么值得看**: 该基准系统化了深度研究报告的评估标准，并提供了 LLM-as-judge 的专家指南，同时引入了声明验证架构，对评测方法学有具体贡献，特别是多维评分项的构建和证据质量量化。
- **关键技术**: `expert-developed taxonomy`, `rubric-based assessment`, `LLM-as-judge`, `claim verification architecture`, `evidence quality quantification`

### 15. Dependence-Aware Label Aggregation for LLM-as-a-Judge via Ising Models
- **链接**: [论文页](https://proceedings.mlr.press/v306/balasubramanian26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/balasubramanian26a/balasubramanian26a.pdf) · [OpenReview](https://openreview.net/forum?id=VCU3hGm0O6)
- **作者**: Krishna Balasubramanian, Aleksandr Podkopaev, Shiva Kasiviswanathan
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: LLM 裁判标签聚合的鲁棒性，特别是标注者依赖对聚合准确性的影响
- **摘要**: 该论文针对 LLM-as-a-judge 场景中的标签聚合问题，指出经典方法（如 Dawid-Skene、加权多数投票）假设标注者在给定真实标签下条件独立，但 LLM 裁判因共享数据、架构、提示和失败模式而违反此假设，导致后验校准不良甚至自信地给出错误预测。作者提出基于 Ising 图模型和潜在因子的依赖感知聚合层级模型：类依赖 Ising 模型的贝叶斯对数几率是投票的二次函数，类无关耦合则退化为带相关调整参数的线性加权投票。通过有限 K 示例证明，条件独立方法即使匹配每个标注者的边际分布，也可能翻转贝叶斯标签；分离结果表明这些方法在裁判数量增长时仍严格次优，潜在因子下产生非消失的过剩风险。在三个真实数据集上，所提方法优于经典基线。
- **为什么值得看**: 该论文为 LLM-as-judge 的聚合提供了依赖建模框架，揭示了条件独立假设失效的后果，并给出可复用的分离结果和实证验证，对评测方法学中的标注可靠性问题有直接贡献。
- **关键技术**: `Ising graphical models`, `latent factor models`, `Bayes optimal aggregation`, `separation results`, `excess risk analysis`

### 16. DSGym: A Holistic Framework for Evaluating and Training Data Science Agents
- **链接**: [论文页](https://proceedings.mlr.press/v306/nie26b.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/nie26b/nie26b.pdf) · [OpenReview](https://openreview.net/forum?id=2WrNPRW9Km)
- **作者**: Fan Nie, Junlin Wang, Harper Hua, Federico Bianchi, Yongchan Kwon, Zhenting Qi, Owen Queen, Shang Zhu et al.
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `benchmark`
- **测什么**: 数据科学智能体在端到端数据分析任务中的规划、执行和验证能力，以及避免捷径解的能力。
- **摘要**: DSGym 是一个用于评估和训练数据科学智能体的标准化框架，提供自包含的执行环境。作者首先指出现有数据科学基准存在碎片化接口、任务覆盖窄和缺乏数据接地的问题，并证明当前基准中相当一部分任务可以在不使用实际数据的情况下解决（即捷径可解）。DSGym 通过模块化架构支持添加任务、智能体脚手架和工具，作为可扩展的活测试平台。他们构建了 DSGym-Tasks，整合并精炼现有基准，通过质量和捷径可解性过滤；并新增 DSBio（专家衍生的生物信息学任务）和 DSPredict（跨视觉、分子预测、单细胞扰动等领域的预测任务）。此外，DSGym 支持通过执行验证的数据合成流水线进行智能体训练，案例研究用 2000 个示例训练集显著提升了 4B 模型在标准化分析基准上的表现。该框架旨在严格端到端测量智能体在现实科学情境中规划、实施和验证数据分析的能力。
- **为什么值得看**: 该论文对评测方法学的价值在于：系统性地揭示了现有数据科学基准中的捷径可解性问题，并提出了可复用的过滤流程（质量与捷径可解性过滤）；同时，其模块化框架和任务套件为跨基准比较和持续扩展提供了标准化接口，有助于提高评测的构念效度和可比性。
- **关键技术**: `benchmark construction`, `shortcut solvability filtering`, `execution-verified data synthesis`, `modular framework`, `human-expert task derivation`

### 17. Efficient Inference for Noisy LLM-as-a-Judge Evaluation
- **链接**: [论文页](https://proceedings.mlr.press/v306/chen26cq.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26cq/chen26cq.pdf) · [OpenReview](https://openreview.net/forum?id=tPcL3fgkjc)
- **作者**: Yiqun T. Chen, Sizhu Lu, Sijia Li, Moran Guo, Shengyi Li
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: LLM-as-judge 在估计平均分数或成对胜率时的系统性偏差与估计效率
- **摘要**: 本文从半参数效率理论出发，系统比较了两类用于校正 LLM-as-judge 系统性误差的估计方法：基于误分类模型的测量误差校正（如 Rogan-Gladen 型估计）与基于金标准人类标签的预测加权推断（PPI）。作者推导了这两类估计量的高效影响函数形式，给出了统一框架，并刻画了 PPI 型估计量渐近方差严格小于测量误差校正的条件。通过模拟实验验证了理论结果，并在真实数据上展示了开源软件包的应用。该工作为评测中如何利用少量人工标注校准 LLM 评判偏差提供了统计理论基础。
- **为什么值得看**: 该论文直接回应了 LLM-as-judge 的测量误差问题，给出了两类校正方法的效率比较，为评测方法学中'如何用少量人类标签提升估计精度'提供了可操作的统计准则，具有明确的 meta-evaluation 价值。
- **关键技术**: `semiparametric efficiency`, `influence function`, `prediction-powered inference`, `measurement error correction`, `Rogan-Gladen estimator`

### 18. Evaluating LLMs When They Do Not Know the Answer: Statistical Evaluation of Mathematical Reasoning via Comparative Signals
- **链接**: [论文页](https://proceedings.mlr.press/v306/dong26o.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/dong26o/dong26o.pdf) · [OpenReview](https://openreview.net/forum?id=nOQOjKYwTM)
- **作者**: Zihan Dong, Zhixian Zhang, Yang Zhou, Can Jin, Ruijia Wu, Linjun Zhang
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 数学推理能力在小样本高噪声条件下的稳定估计与排名可靠性
- **摘要**: 该论文针对数学推理评测中基准规模有限和模型随机性导致的高方差、排名不稳定问题，提出利用模型对候选解答的成对比较信号作为控制变量，构建基于有效影响函数（EIF）的半参数估计器。在观测到辅助推理链的设置下，该一步估计器达到半参数效率界，严格保证方差缩减，并具有渐近正态性以支持不确定性量化。模拟实验显示，随着模型输出噪声增大，排名精度提升更显著；在GPQA Diamond、AIME 2025和GSM8K上的实验表明，小样本场景下性能估计和模型排名更可靠。该方法学贡献在于将统计效率工具引入评测，为小样本高噪声环境下的可靠评估提供了新途径。
- **为什么值得看**: 该论文直接回应了评测方法学中的统计可靠性问题，通过控制变量和半参数效率界提供了可复用的方差缩减框架，对榜单稳定性分析具有方法论价值。
- **关键技术**: `control variates`, `efficient influence function`, `semiparametric estimation`, `pairwise comparison`, `variance reduction`

### 19. Expanding the AI Evaluation Toolbox with Statistical Models
- **链接**: [论文页](https://proceedings.mlr.press/v306/keller26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/keller26a/keller26a.pdf) · [OpenReview](https://openreview.net/forum?id=THqrfMr0r1)
- **作者**: Drew Keller, Kweku Kwegyir-Aggrey, Ryan Steed, Anita K. Rao, Julia L. Sharp, A. Stevie Bergman
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 测量基准准确率与广义准确率的差异，以及模型性能的方差分解和题目难度。
- **摘要**: 本文提出用统计模型改进AI基准评测的实践。作者首先区分了基准准确率（benchmark accuracy）与广义准确率（generalized accuracy，即对所有潜在相似测试题目的表现），指出现有方法常混淆二者。在模拟实验和22个API访问的前沿大语言模型在3个流行基准上的大规模评测中，他们展示了广义线性混合模型（GLMM）能正确估计广义准确率，并比现有无回归方法更高效地量化不确定性。该方法还提供方差分解和题目难度估计，揭示LLM表现和基准构建的重要方面。
- **为什么值得看**: 该论文直接回应评测方法学核心问题：区分基准分数与广义能力，并用GLMM提供更可靠的估计和不确定性量化，为统计可靠性分析提供了可复用的框架。
- **关键技术**: `generalized linear mixed model`, `variance decomposition`, `item difficulty estimation`, `uncertainty quantification`, `benchmark accuracy vs generalized accuracy`

### 20. Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving
- **链接**: [论文页](https://proceedings.mlr.press/v306/ammanamanchi26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/ammanamanchi26a/ammanamanchi26a.pdf) · [OpenReview](https://openreview.net/forum?id=bHYAWawd4A)
- **作者**: Pawan Sasanka Ammanamanchi, Siddharth Bhat, Stella Biderman
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `analysis`
- **测什么**: 形式化数学基准中语句与原始问题的一致性、证明的有效性及评测鲁棒性
- **摘要**: 本文审计了五个广泛使用的 Lean 定理证明基准及其分支，发现即使有机器校验的证明，基准仍可能因形式化语句与原始非形式问题不一致而失效。通过语料级静态检查器，作者识别出 4,833 个发现，其中 398 个为机械可验证的问题，包括反例、空洞定理和不健全公理；还记录了缺失假设、问题简化、翻译错误等语义缺陷。作者进一步展示了这些缺陷在修正子集上会高估或低估证明器的得分，并提出了缺陷分类法、自动化检查器套件和语义审计提示，以及发布标准。该工作提供了可复用的基准质量审计流程，对形式化数学评测的效度有重要贡献。
- **为什么值得看**: 该论文系统性地揭示了'机器校验证明'并不保证基准效度，提出了可复用的缺陷分类法和自动化审计工具，为形式化数学基准的构造与验证提供了方法学框架，直接回应了测量效度问题。
- **关键技术**: `static analysis`, `fault taxonomy`, `semantic audit prompts`, `benchmark validation`, `contamination audit`

## 全部收录

共 566 篇，按分数排序：[1](all.md) · [2](all-2.md) · [3](all-3.md) · [4](all-4.md)
