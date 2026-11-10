# ICML 2026 · 评测方法学

> 本页 22 篇（该主题共 22 篇），按相关性排序。 [返回总览](../index.md)

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

### 3. A Judge-Aware Ranking Framework for Evaluating Large Language Models without Ground Truth
- **链接**: [论文页](https://proceedings.mlr.press/v306/xu26ay.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xu26ay/xu26ay.pdf) · [OpenReview](https://openreview.net/forum?id=yFUmcOtUYD)
- **作者**: Mingyuan Xu, Xinzi Tan, Jiawei Wu, Doudou Zhou
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 衡量法官可靠性差异下模型排名的准确性与不确定性校准
- **摘要**: 该论文针对无真实标签的开放任务中LLM-as-judge评测的可靠性问题，提出一种法官感知的排序框架，扩展Bradley-Terry-Luce模型，引入法官特定的区分度参数，联合估计潜在模型质量与法官可靠性，无需参考标签。作者证明了在自然归一化下的可识别性，以及极大似然估计的一致性和渐近正态性，从而为分数差异和排名比较提供置信区间。在多个公开基准和新收集的数据集上，该方法相比未加权基线提高了与人类偏好的一致性，数据效率更高，并产生校准的不确定性量化。
- **为什么值得看**: 该论文直接回应了评测方法学中的核心问题：法官可靠性差异和聚合模型误设定，提供了可复用的统计框架（扩展BTL模型）来校准法官权重并量化排名不确定性，对LLM-as-judge的验证和统计可靠性有重要价值。
- **关键技术**: `Bradley-Terry-Luce model`, `judge-specific discrimination`, `maximum likelihood estimation`, `identifiability`, `confidence intervals`

### 4. AI Cartography: Mapping the Latent Landscape of AI Benchmark Ecosystems
- **链接**: [论文页](https://proceedings.mlr.press/v306/hardy26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/hardy26a/hardy26a.pdf) · [OpenReview](https://openreview.net/forum?id=Vr4YScS9DT)
- **作者**: Michael Hardy, Anka Reuel, Lijin Zhang, Jodi M. Casabianca, Sang T. Truong, Yash Satish Dave, Hansol Lee, Benjamin W. Domingue et al.
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `analysis`
- **测什么**: benchmark 排名方差的来源与潜在结构的可靠性
- **摘要**: 本文提出一个测量 AI benchmark 生态潜在结构的框架，将验证性因子分析（CFA）和概化理论应用于 Open LLM Leaderboard 上 4000+ 模型的数据，分解排名方差的来源。主要发现包括：当前报告实践假设的结构低估了 benchmark 间关系的强度；存在局部依赖，削弱了将 benchmark 作为测量工具的有效性；贡献者元数据解释了约 9% 的排名相关方差，高于架构或部署类别；显式分数的“缩放定律”斜率可靠性低（R_beta=0.53），而潜在一般因子的大小斜率则高度稳定（R_g=0.97）。该框架还能揭示哪些 benchmark 受模型规模影响、哪些受后训练实践影响，并提供诊断工具以判断排名可信度和改进 benchmark 设计。
- **为什么值得看**: 该论文将心理测量学方法（CFA、概化理论）引入 AI 评测，量化了排名中的测量噪声来源，并揭示了当前评分系统下 benchmark 作为测量工具的效度问题，为评测方法学提供了可复用的方差分解和可靠性诊断流程。
- **关键技术**: `Confirmatory Factor Analysis`, `Generalizability Theory`, `variance decomposition`, `reliability analysis`, `local dependence testing`

### 5. Are LLM Evaluators Really Narcissists? Sanity Checking Self-Preference Evaluations
- **链接**: [论文页](https://proceedings.mlr.press/v306/roytburg26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/roytburg26a/roytburg26a.pdf) · [OpenReview](https://openreview.net/forum?id=sRPyBOSZQk)
- **作者**: Dani Roytburg, Matthew Bozoukov, Matthew Nguyen, Jou Barzdukas, Mackenzie Puig-Hall, Narmeen Fatimah Oozeer
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: LLM评估器在自我评估时是否存在真实的自我偏好偏差，而非由评估器质量差异导致的混淆。
- **摘要**: 该论文质疑了先前关于LLM评估器存在自我偏好（narcissism）的结论，指出这些发现可能混淆了评估器质量与作者身份。作者提出一种新的基线方法：直接比较评估器在评估自身输出与评估其他模型输出时的投票分布，以控制评估器质量的影响。通过重新分析先前数据，发现只有51%的示例在统计上显著支持自我偏好假设，但这些示例覆盖了89.6%的自我偏好概率质量。此外，作者比较了投票分布的熵，表明不确定性驱动的重叠可能解释部分现象。该工作为评估器偏差研究提供了更严谨的统计检验框架，有助于区分真实偏差与混淆因素。
- **为什么值得看**: 该论文直接针对LLM-as-judge评估方法学中的核心问题——自我偏好偏差，提出了一个可复用的统计基线（评估器质量基线）来区分真实偏差与混淆因素，对评测方法学具有重要价值。
- **关键技术**: `statistical significance testing`, `baseline correction`, `voting distribution analysis`, `entropy comparison`, `confound control`

### 6. Benchmarking at the Edge of Comprehension
- **链接**: [论文页](https://proceedings.mlr.press/v306/marro26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/marro26a/marro26a.pdf) · [OpenReview](https://openreview.net/forum?id=BhahZSDowo)
- **作者**: Samuele Marro, Jialin Yu, Emanuele La Malfa, Oishi Deb, Jiawei Li, Yibo Yang, Ebey Abraham, Sunando Sengupta et al.
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 模型在人类无法完全理解的任务上的解决能力与生成困难但可解问题的能力。
- **摘要**: 该论文提出“后理解时代”（post-comprehension regime）的概念，指出当前沿模型在基准测试上迅速饱和、人类难以生成有区分度的任务或提供准确答案时，传统评测将失效。为此，作者提出“批评韧性基准测试”（Critique-Resilient Benchmarking）框架，将正确性定义为“没有对手能令人信服地证明其错误”，人类仅作为有界验证者，对局部声明进行审查，从而在任务超出人类完全理解时仍能保持评测完整性。方法上，采用分项二部 Bradley-Terry 模型，联合排名模型解决难题的能力和生成困难但可解问题的能力。在数学领域对八个前沿 LLM 进行实验，结果显示分数稳定且与外部能力指标相关。该框架将基准测试重构为对抗性生成-评估博弈，人类作为最终裁决者。
- **为什么值得看**: 该论文直接回应基准饱和与人类标注能力上限的方法学挑战，提出一种不依赖完整人类理解的评测框架，并引入对抗性验证与配对比较模型，为评测效度提供了新思路，对测量设计有重要参考价值。
- **关键技术**: `adversarial verification`, `Bradley-Terry model`, `human-as-bounded-verifier`, `critique-resilient correctness`, `benchmark saturation`

### 7. CapBencher: Give Your LLM Benchmark a Built-in Alarm for Test-Set Overfitting
- **链接**: [论文页](https://proceedings.mlr.press/v306/ishida26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/ishida26a/ishida26a.pdf) · [OpenReview](https://openreview.net/forum?id=oCNT5PcMSQ)
- **作者**: Takashi Ishida, Thanawat Lodkaew, Ikko Yamane
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 检测模型在 benchmark 上是否因测试集过拟合或数据泄露而超过理论准确率上限。
- **摘要**: CapBencher 提出一种发布 benchmark 的新方法，旨在防止测试集过拟合和标签泄露。其核心思想是：为每个问题准备多个逻辑上正确的答案，但只在基准中公开其中一个作为标准答案，从而降低贝叶斯准确率（即理论上可达到的最高准确率）。由于即使最强模型也不应超过贝叶斯准确率，任何超过该阈值的模型都强烈暗示存在测试集过拟合或数据污染。作者从理论和实验两方面验证了该方法在多种基准、模型和训练场景下能准确检测过拟合。该方法允许公开评估 LLM，同时避免完全披露真实答案，为 benchmark 发布提供了新的安全机制。
- **为什么值得看**: 该论文直接针对 benchmark 评测中的污染与过拟合问题，提出了一种可复用的检测机制（基于贝叶斯准确率阈值），并提供了理论保证和实证验证，对评测方法学有重要贡献。
- **关键技术**: `Bayes accuracy`, `test-set overfitting detection`, `answer randomization`, `theoretical analysis`, `empirical validation`

### 8. CHB: A Diagnostic Toolkit for Hardness-Aware Clustering Evaluation
- **链接**: [论文页](https://proceedings.mlr.press/v306/durani26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/durani26a/durani26a.pdf) · [OpenReview](https://openreview.net/forum?id=9zXUOLxbcL)
- **作者**: Walid Durani, Philipp Jahn, Collin Leiber, David B. Hoffmann, Thomas Seidl, Claudia Plant, Christian Böhm
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 聚类算法在不同数据硬度条件下的性能与鲁棒性，以及表示变化对性能的影响。
- **摘要**: CHB 是一个面向聚类评测的诊断工具包，旨在替代将性能压缩为单一排名的传统榜单。它通过可扩展的持久同调摘要，为每个数据集-表示对生成可解释的硬度指纹，涵盖分离度、内聚性与尺度异质性、拓扑结构三个维度。在该诊断空间内，CHB 在标准化、计算感知的轨道下评估聚类算法，将比较转化为诊断：在广泛的数据集和表示上，它揭示了可复现的结构性机制、跨方法族的机制依赖排名反转，以及包括拓扑相关崩溃在内的鲁棒性特征。CHB 还支持表示审计，将性能提升归因于硬度指纹的可测量变化，而非仅外部性能变化。工具包以开放、可扩展的形式发布，供在共享诊断框架下评估新聚类方法和嵌入。
- **为什么值得看**: 该论文提出了一种基于硬度指纹的条件化评测方法，将聚类性能比较转化为对数据属性与算法失败模式的诊断，为评测方法学提供了可复用的框架，尤其适用于揭示排名反转和鲁棒性特征。
- **关键技术**: `hardness fingerprint`, `persistent homology`, `compute-aware evaluation`, `representation auditing`, `regime-dependent analysis`

### 9. Coverage, Not Averages: Semantic Stratification for Trustworthy Retrieval Evaluation
- **链接**: [论文页](https://proceedings.mlr.press/v306/klearman26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/klearman26a/klearman26a.pdf) · [OpenReview](https://openreview.net/forum?id=Q9LweGI2B9)
- **作者**: Andrew Klearman, Radu Revutchi, Rohin Garg, Rishav Chakravarti, Samuel Marc Denton, Yuan Xue
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 检索评估集的语义覆盖完整性及检索失败模式的结构性差异
- **摘要**: 该论文将检索评估形式化为统计估计问题，指出基于启发式构造的查询集存在内在偏差，限制了指标可靠性。作者提出语义分层（semantic stratification）方法，基于实体簇将语料库组织为可解释的全局空间，并系统生成缺失层的查询，从而提供形式化的语义覆盖保证，并揭示检索失败模式。实验在多个基准和检索方法上验证了框架，暴露了系统性覆盖缺口，识别出解释检索性能方差的结构信号，并表明分层评估比聚合指标更稳定、透明。论文还提供了可复用的评估集构造流程，有助于提升RAG评估的可信度。
- **为什么值得看**: 该论文直接针对评测方法学中的构念覆盖与选择偏差问题，提出了可复用的语义分层评估框架，并给出了覆盖保证与失败模式可见性，对评测设计具有方法论价值。
- **关键技术**: `semantic stratification`, `coverage guarantees`, `entity-based clustering`, `query generation`, `failure mode analysis`

### 10. Cutting LLM Evaluation Costs with SySRs: A Bandit Algorithm That Provably Exploits Model Similarity
- **链接**: [论文页](https://proceedings.mlr.press/v306/lyu26h.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/lyu26h/lyu26h.pdf) · [OpenReview](https://openreview.net/forum?id=vkG1xVVKOH)
- **作者**: Zifan Lyu, Chahine Nejma, Tobias Wegel, Fanny Yang, Florian E. Dorner
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 在有限预算下识别最佳模型的能力，即评测效率与识别可靠性。
- **摘要**: 该论文提出 SySRs（Synchronized Successive Rejects），一种用于大模型评测的自适应预算分配算法，旨在通过最佳臂识别（best-arm identification）降低评测成本。其核心思想是：若某模型明显劣于其他模型，则无需精确估计其性能，从而将预算集中于有竞争力的模型。SySRs 在经典 Successive Rejects 算法基础上引入配对比较，利用模型间对同一提示的相似响应来提升效率，且无需超参数，并提供了随模型相似度提高而改善的性能保证。实验在 15 个标准 benchmark 上验证，SySRs 在平均错误率和识别最佳模型的最坏预算方面均优于基线。该方法为评测成本控制提供了理论上有保证的框架，但未涉及评测内容本身的效度或污染问题。
- **为什么值得看**: 该论文为评测方法学提供了可复用的自适应预算分配框架，将统计上的最佳臂识别与模型相似性结合，直接回应了评测成本与统计可靠性之间的权衡，对大规模模型比较的测量设计有参考价值。
- **关键技术**: `best-arm identification`, `Successive Rejects`, `paired comparisons`, `adaptive budget allocation`, `model similarity`

### 11. Dependence-Aware Label Aggregation for LLM-as-a-Judge via Ising Models
- **链接**: [论文页](https://proceedings.mlr.press/v306/balasubramanian26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/balasubramanian26a/balasubramanian26a.pdf) · [OpenReview](https://openreview.net/forum?id=VCU3hGm0O6)
- **作者**: Krishna Balasubramanian, Aleksandr Podkopaev, Shiva Kasiviswanathan
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: LLM 裁判标签聚合的鲁棒性，特别是标注者依赖对聚合准确性的影响
- **摘要**: 该论文针对 LLM-as-a-judge 场景中的标签聚合问题，指出经典方法（如 Dawid-Skene、加权多数投票）假设标注者在给定真实标签下条件独立，但 LLM 裁判因共享数据、架构、提示和失败模式而违反此假设，导致后验校准不良甚至自信地给出错误预测。作者提出基于 Ising 图模型和潜在因子的依赖感知聚合层级模型：类依赖 Ising 模型的贝叶斯对数几率是投票的二次函数，类无关耦合则退化为带相关调整参数的线性加权投票。通过有限 K 示例证明，条件独立方法即使匹配每个标注者的边际分布，也可能翻转贝叶斯标签；分离结果表明这些方法在裁判数量增长时仍严格次优，潜在因子下产生非消失的过剩风险。在三个真实数据集上，所提方法优于经典基线。
- **为什么值得看**: 该论文为 LLM-as-judge 的聚合提供了依赖建模框架，揭示了条件独立假设失效的后果，并给出可复用的分离结果和实证验证，对评测方法学中的标注可靠性问题有直接贡献。
- **关键技术**: `Ising graphical models`, `latent factor models`, `Bayes optimal aggregation`, `separation results`, `excess risk analysis`

### 12. Efficient Inference for Noisy LLM-as-a-Judge Evaluation
- **链接**: [论文页](https://proceedings.mlr.press/v306/chen26cq.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26cq/chen26cq.pdf) · [OpenReview](https://openreview.net/forum?id=tPcL3fgkjc)
- **作者**: Yiqun T. Chen, Sizhu Lu, Sijia Li, Moran Guo, Shengyi Li
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: LLM-as-judge 在估计平均分数或成对胜率时的系统性偏差与估计效率
- **摘要**: 本文从半参数效率理论出发，系统比较了两类用于校正 LLM-as-judge 系统性误差的估计方法：基于误分类模型的测量误差校正（如 Rogan-Gladen 型估计）与基于金标准人类标签的预测加权推断（PPI）。作者推导了这两类估计量的高效影响函数形式，给出了统一框架，并刻画了 PPI 型估计量渐近方差严格小于测量误差校正的条件。通过模拟实验验证了理论结果，并在真实数据上展示了开源软件包的应用。该工作为评测中如何利用少量人工标注校准 LLM 评判偏差提供了统计理论基础。
- **为什么值得看**: 该论文直接回应了 LLM-as-judge 的测量误差问题，给出了两类校正方法的效率比较，为评测方法学中'如何用少量人类标签提升估计精度'提供了可操作的统计准则，具有明确的 meta-evaluation 价值。
- **关键技术**: `semiparametric efficiency`, `influence function`, `prediction-powered inference`, `measurement error correction`, `Rogan-Gladen estimator`

### 13. Evaluating LLMs When They Do Not Know the Answer: Statistical Evaluation of Mathematical Reasoning via Comparative Signals
- **链接**: [论文页](https://proceedings.mlr.press/v306/dong26o.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/dong26o/dong26o.pdf) · [OpenReview](https://openreview.net/forum?id=nOQOjKYwTM)
- **作者**: Zihan Dong, Zhixian Zhang, Yang Zhou, Can Jin, Ruijia Wu, Linjun Zhang
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 数学推理能力在小样本高噪声条件下的稳定估计与排名可靠性
- **摘要**: 该论文针对数学推理评测中基准规模有限和模型随机性导致的高方差、排名不稳定问题，提出利用模型对候选解答的成对比较信号作为控制变量，构建基于有效影响函数（EIF）的半参数估计器。在观测到辅助推理链的设置下，该一步估计器达到半参数效率界，严格保证方差缩减，并具有渐近正态性以支持不确定性量化。模拟实验显示，随着模型输出噪声增大，排名精度提升更显著；在GPQA Diamond、AIME 2025和GSM8K上的实验表明，小样本场景下性能估计和模型排名更可靠。该方法学贡献在于将统计效率工具引入评测，为小样本高噪声环境下的可靠评估提供了新途径。
- **为什么值得看**: 该论文直接回应了评测方法学中的统计可靠性问题，通过控制变量和半参数效率界提供了可复用的方差缩减框架，对榜单稳定性分析具有方法论价值。
- **关键技术**: `control variates`, `efficient influence function`, `semiparametric estimation`, `pairwise comparison`, `variance reduction`

### 14. Expanding the AI Evaluation Toolbox with Statistical Models
- **链接**: [论文页](https://proceedings.mlr.press/v306/keller26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/keller26a/keller26a.pdf) · [OpenReview](https://openreview.net/forum?id=THqrfMr0r1)
- **作者**: Drew Keller, Kweku Kwegyir-Aggrey, Ryan Steed, Anita K. Rao, Julia L. Sharp, A. Stevie Bergman
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 测量基准准确率与广义准确率的差异，以及模型性能的方差分解和题目难度。
- **摘要**: 本文提出用统计模型改进AI基准评测的实践。作者首先区分了基准准确率（benchmark accuracy）与广义准确率（generalized accuracy，即对所有潜在相似测试题目的表现），指出现有方法常混淆二者。在模拟实验和22个API访问的前沿大语言模型在3个流行基准上的大规模评测中，他们展示了广义线性混合模型（GLMM）能正确估计广义准确率，并比现有无回归方法更高效地量化不确定性。该方法还提供方差分解和题目难度估计，揭示LLM表现和基准构建的重要方面。
- **为什么值得看**: 该论文直接回应评测方法学核心问题：区分基准分数与广义能力，并用GLMM提供更可靠的估计和不确定性量化，为统计可靠性分析提供了可复用的框架。
- **关键技术**: `generalized linear mixed model`, `variance decomposition`, `item difficulty estimation`, `uncertainty quantification`, `benchmark accuracy vs generalized accuracy`

### 15. Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving
- **链接**: [论文页](https://proceedings.mlr.press/v306/ammanamanchi26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/ammanamanchi26a/ammanamanchi26a.pdf) · [OpenReview](https://openreview.net/forum?id=bHYAWawd4A)
- **作者**: Pawan Sasanka Ammanamanchi, Siddharth Bhat, Stella Biderman
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `analysis`
- **测什么**: 形式化数学基准中语句与原始问题的一致性、证明的有效性及评测鲁棒性
- **摘要**: 本文审计了五个广泛使用的 Lean 定理证明基准及其分支，发现即使有机器校验的证明，基准仍可能因形式化语句与原始非形式问题不一致而失效。通过语料级静态检查器，作者识别出 4,833 个发现，其中 398 个为机械可验证的问题，包括反例、空洞定理和不健全公理；还记录了缺失假设、问题简化、翻译错误等语义缺陷。作者进一步展示了这些缺陷在修正子集上会高估或低估证明器的得分，并提出了缺陷分类法、自动化检查器套件和语义审计提示，以及发布标准。该工作提供了可复用的基准质量审计流程，对形式化数学评测的效度有重要贡献。
- **为什么值得看**: 该论文系统性地揭示了'机器校验证明'并不保证基准效度，提出了可复用的缺陷分类法和自动化审计工具，为形式化数学基准的构造与验证提供了方法学框架，直接回应了测量效度问题。
- **关键技术**: `static analysis`, `fault taxonomy`, `semantic audit prompts`, `benchmark validation`, `contamination audit`

### 16. How to Correctly Report LLM-as-a-Judge Evaluations
- **链接**: [论文页](https://proceedings.mlr.press/v306/lee26bl.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/lee26bl/lee26bl.pdf) · [OpenReview](https://openreview.net/forum?id=VX8H2713oA)
- **作者**: Chungpa Lee, Thomas Zeng, Jongwon Jeong, Jy-Yong Sohn, Kangwook Lee
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: LLM-as-judge 评估分数的偏差校正与统计可靠性
- **摘要**: 该论文针对 LLM-as-judge 评估中的系统性偏差问题，提出一个即插即用的偏差校正框架。它利用人类标注的校准数据集估计 judge 的敏感性和特异性，并据此校正原始评估分数，同时构建同时考虑测试集和校准集不确定性的置信区间。框架采用自适应策略分配校准样本，以在给定预算下获得更紧的区间。作者刻画了真实分数与 judge 敏感/特异性组合的参数区域，在这些区域内 LLM 评估比纯人类评估更可靠。此外，框架在测试集与校准集存在分布偏移时仍保持无偏，优于现有方法。
- **为什么值得看**: 该论文直接回应了 LLM-as-judge 的测量误差问题，提供了偏差校正和不确定性量化的统计框架，并分析了其适用条件，对评测方法学有重要价值。
- **关键技术**: `bias correction`, `confidence intervals`, `sensitivity/specificity estimation`, `adaptive sampling`, `distribution shift robustness`

### 17. Instance-Level Costs for Nuanced Classifier Evaluation
- **链接**: [论文页](https://proceedings.mlr.press/v306/kang26m.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/kang26m/kang26m.pdf) · [OpenReview](https://openreview.net/forum?id=qMI1xD8O3x)
- **作者**: Kabir Kang, Stephen Mussmann
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 分类模型在实例级代价加权下的错误表现，特别是模糊样本上的错误集中度。
- **摘要**: 本文提出归一化超额代价（NEC）指标，用于在分类任务中按实例赋予不同错误代价，从而更细致地评估模型性能。NEC 基于上下文赌博机框架，将每个样本的代价（如标注者投票差距、与决策边界的距离或置信度）加权到错误上，当代价均匀时退化为标准错误率。在文本、图像和表格基准上，NEC 通常显著低于错误率（例如 5% 错误率对应 1.8% NEC），表明大部分错误集中在模糊、低代价样本上。作者还发现，代价敏感训练、focal loss 和后处理阈值等方法并不能一致地改善 NEC。该框架为推导和评估实例级误分类代价提供了实用方法。
- **为什么值得看**: 该论文提出了一种新的评估指标 NEC，并系统分析了错误分布与实例难度之间的关系，为评测方法学提供了可复用的代价推导和评估流程，有助于更细致地理解模型在模糊样本上的表现。
- **关键技术**: `instance-level cost weighting`, `contextual bandit framework`, `error distribution analysis`, `cost-aware training comparison`

### 18. Is Your Diffusion Sampler Actually Correct? A Sampler-Centric Evaluation of Discrete Diffusion Language Models
- **链接**: [论文页](https://proceedings.mlr.press/v306/tang26ad.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tang26ad/tang26ad.pdf) · [OpenReview](https://openreview.net/forum?id=oYCCOl7ahf)
- **作者**: Luhan Tang, Longxuan Yu, Shaorong Zhang, Greg Ver Steeg
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 离散扩散语言模型采样器的分布正确性（采样器误差）
- **摘要**: 该论文针对离散扩散语言模型（dLLM）的评测提出质疑：现有指标（如NLL、GenPPL、MAUVE）混淆了去噪器近似误差与采样器动态引入的误差，而自回归模型不存在此问题。作者引入一个基于真实马尔可夫链的oracle框架，用精确的隐马尔可夫模型后验替代学习到的去噪器，从而在受控条件下隔离采样器误差。实验表明，即使使用oracle去噪器，少步离散扩散采样器在分布上也不正确，转移级不匹配仅在步数接近序列长度时才消失。此外，NLL、GenPPL或MAUVE的改进并不保证采样正确性。该工作为dLLM评测提供了新的方法论视角，强调采样器正确性应作为独立维度。
- **为什么值得看**: 该论文揭示了现有dLLM评测指标在构念效度上的缺陷，提出了一种可复用的oracle框架来分离采样器误差，对评测方法学有直接贡献，尤其适用于生成模型评测的误差分解。
- **关键技术**: `oracle framework`, `error decomposition`, `Hidden Markov Model posterior`, `distributional correctness`, `sampler-centric evaluation`

### 19. Item Response Scaling Laws: A Measurement Theory Approach for Efficient and Generalizable Neural Scaling Estimation
- **链接**: [论文页](https://proceedings.mlr.press/v306/truong26b.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/truong26b/truong26b.pdf) · [OpenReview](https://openreview.net/forum?id=QFgM1iNKmg)
- **作者**: Sang T. Truong, Yuheng Tu, Rylan Schaeffer, Sanmi Koyejo
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 语言模型潜在能力与题目特征，以及跨基准的性能泛化。
- **摘要**: 本文提出 Item Response Scaling Laws (IRSL)，将项目反应理论（IRT）融入缩放定律估计，以降低传统方法所需的巨大评估成本。IRSL 将模型能力与题目特征分离，把参数复杂度从 O(M×N) 降至 O(M+N)，并采用 Beta-IRT 利用语言模型的概率响应（如预训练 token 概率、测试时采样通过率）而非二元正确性。作者在预训练下游缩放（6,612 个检查点、10 个基准、37,682 题）和测试时缩放（12 个模型、4 个基准、每题最多 2,500 次采样）两种范式下验证，结果显示仅用每基准 50 题（减少 99.9%）即可获得与传统方法相当或更优的决策准确率。此外，估计的潜在能力可跨共享测量目标的基准泛化，实现性能预测。该方法为缩放定律估计提供了测量理论视角，显著降低评估成本。
- **为什么值得看**: 该论文将 IRT 引入缩放定律估计，提供了一种可复用的测量框架，能大幅减少评估所需样本量，并验证了潜在能力跨基准的泛化性，对评测方法学中的效率与效度问题有直接贡献。
- **关键技术**: `Item Response Theory`, `Beta-IRT`, `scaling law estimation`, `parameter reduction`, `cross-benchmark generalization`

### 20. Judging What We Cannot Solve: A Consequence-Based Approach for Oracle-Free Evaluation of Research-Level Math
- **链接**: [论文页](https://proceedings.mlr.press/v306/son26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/son26a/son26a.pdf) · [OpenReview](https://openreview.net/forum?id=Dkwqzk5sAD)
- **作者**: Guijin Son, Donghun Yang, Hitesh Laxmichand Patel, Hyunwoo Ko, Amit Agarwal, Sunghee Ahn, Kyong-Ha Lee, Youngjae Yu
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 研究级数学问题解答的方法级信息质量（作为示例的效用）
- **摘要**: 该论文提出一种无需人工标注的评测方法 Consequence-Based Utility，用于评估研究级数学问题的解答质量。其核心假设是：一个正确的解答应包含足够的方法级信息，当作为上下文示例应用于一组相关的可验证问题时，能比错误解答带来更好的下游性能。作者构建了一个包含研究级数学问题、每个问题配有一个专家解答和九个 LLM 生成解答的数据集，并在此上评估该方法。结果显示，该方法在排序质量上持续优于奖励模型、生成式奖励模型和 LLM 裁判，例如在 GPT-OSS-120B 上将 Acc@1 从 67.2 提升至 76.3，AUC 从 71.4 提升至 79.6。此外，与 LLM 裁判相比，该方法在求解器难以解决的实例上仍能保持更强的正确-错误区分能力。
- **为什么值得看**: 该论文提出了一种无需 oracle 的评测方法，通过下游任务性能来间接评估解答质量，为无法直接验证的开放性问题提供了可复用的评测范式，并系统比较了与奖励模型和 LLM 裁判的排序质量，对评测方法学有直接贡献。
- **关键技术**: `consequence-based evaluation`, `in-context exemplar`, `ranking quality comparison`, `oracle-free evaluation`

### 21. Leaderboard Incentives: Model Rankings under Strategic Post-Training
- **链接**: [论文页](https://proceedings.mlr.press/v306/chen26gf.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26gf/chen26gf.pdf) · [OpenReview](https://openreview.net/forum?id=r6wfuAKmVb)
- **作者**: Yatong Chen, Guanhua Zhang, Moritz Hardt
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `analysis`
- **测什么**: 基准协议在战略后训练下诱导的模型排名激励与均衡性质
- **摘要**: 本文从博弈论视角研究排行榜对模型开发者的激励结构，将基准评测建模为基准设计者与多个模型提供者之间的Stackelberg博弈。每个竞争者拥有未知的潜在质量，并可通过分配资源到基准特定改进来虚增观测分数。作者证明当前基准诱导的博弈不存在纳什均衡，这解释了为何现有实践导致激励错位和策略性行为。在温和条件下，他们证明近期提出的tune-before-test协议能诱导具有唯一纳什均衡的基准，该均衡按潜在质量对模型排序。该工作为评测协议设计提供了理论依据，表明基准可以避免不良激励。
- **为什么值得看**: 该论文为评测协议设计提供了博弈论框架，证明当前基准缺乏均衡，并给出tune-before-test协议的理论保证，对评测方法学有直接贡献，可指导设计抗策略操纵的基准。
- **关键技术**: `Stackelberg game`, `Nash equilibrium`, `tune-before-test protocol`, `incentive analysis`

### 22. Margin-Adaptive Confidence Ranking for Reliable LLM Judgement
- **链接**: [论文页](https://proceedings.mlr.press/v306/jin26h.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/jin26h/jin26h.pdf) · [OpenReview](https://openreview.net/forum?id=o3JP1sHHSY)
- **作者**: Gaojie Jin, Yong Tao, Lijia Yu, Tianjin Huang
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: LLM 判断置信度与人类分歧风险之间的单调关系及一致性保证的成功率
- **摘要**: 本文针对 LLM-as-judge 与人类判断一致性检验中置信度单调性假设可能失效的问题，提出学习专门的置信度估计器而非依赖启发式信号。方法上，通过模拟标注者多样性生成训练数据，并采用基于间隔的排序损失来显式建模模型区分人类一致与不一致案例的置信度。作者推导了该估计器的泛化保证，揭示了间隔相关的权衡，并据此设计了自适应的训练流程。在多个数据集和 judge 模型上，将学习到的置信度集成到固定序列检验中，提升了排序准确率，增强了置信度与分歧风险之间的单调关系，从而提高了达到目标一致水平的成功率。
- **为什么值得看**: 该工作直接针对 LLM-as-judge 验证中的核心方法学问题——置信度估计的可靠性与泛化，提供了可复用的训练流程和理论分析，对评测方法学中 judge 校准与一致性保证具有重要价值。
- **关键技术**: `confidence estimation`, `margin-based ranking`, `generalization bound`, `simulated annotator diversity`, `fixed-sequence testing`
