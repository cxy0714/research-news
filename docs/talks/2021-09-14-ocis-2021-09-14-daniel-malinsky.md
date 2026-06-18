# Explaining the Behavior of Black-Box Prediction Algorithms with Causal Learning

**讲者**: Daniel Malinsky  
**讨论人**: Joshua Loftus  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2021-09-14  
**主题**: 因果推断  
**视频**: <https://youtu.be/itnR1xVS4YI> · [幻灯片](https://drive.google.com/file/d/1-yRmKnpwPSKiXlSq1sbaZ3Y0EqYeHy9U/view?usp=sharing)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

## 相关论文

- [2006.02482](https://arxiv.org/abs/2006.02482) *（尚未精读 — `talks read --id … --read-papers` 可补）*

---

### 一、这场报告在讲哪条工作线

这场报告属于**Explainable AI (XAI) / Interpretable Machine Learning** 与 **Causal Discovery** 的交汇子方向——「用因果学习解释黑箱预测算法的行为」。该方向的核心追问是：**如何从“因果”而非“关联”的角度，解释一个黑箱模型为什么对某个输入给出特定输出？**  

#### 主流路线与奠基  

- 当前 XAI 的主流方法分为两类：  
  1. **全局近似**（如用稀疏线性模型、决策树近似整个黑箱，Ribeiro et al. KDD 2016 的 LIME）；  
  2. **特征重要性**（如基于 Shapley 值的 SHAP，Lundberg & Lee NeurIPS 2017；基于梯度的 saliency map）。  
  这些方法本质上是 **关联性的**（衡量特征与输出之间的统计依赖或局部梯度），缺乏因果区分能力：无法判断一个特征 **仅仅是关联（因混淆）** 还是 **真正在因果上驱动** 了黑箱的输出。  

- 哲学基础是 **Woodward (2003) 的反事实因果解释理论**：一个变量 X 解释了 Y，当且仅当在适当背景条件下，对 X 的干预会改变 Y 的分布（“what would have been different” 问题）。这一框架天然与因果建模中的 **do-算子** 和 **干预** 概念对齐。

#### 该报告站在哪里  

报告提出：**将黑箱模型输出 Ŷ 视为一个“变量”，把可解释的高层特征 Z 视为它的潜在原因，然后使用允许任意未测量混淆的因果发现算法（FCI）学习 Z 与 Ŷ 之间的部分祖先图 (PAG)**。这样可以在控制未测量混淆的前提下，区分出 **可能的因果祖先**（Z → Ŷ）与 **仅因混淆而关联**（Z ↔ Ŷ 或 Z 不邻接 Ŷ 但通过隐变量相关）。  

- **关键先行工作**（讲者引用）：  
  - Spirtes, Glymour, & Scheines (2000) *Causation, Prediction, and Search*（FCI 算法奠基）。  
  - Zhang (2008) *On the completeness of orientation rules for causal discovery in the presence of latent confounders and selection bias*（FCI 的完整规则）。  
  - Chalupka, Perona, & Eberhardt (2015) *Visual causal feature learning*（从图像中自动学习因果特征，本报告模拟实验受其启发）。  
  - Woodward (2003) *Making Things Happen*（反事实因果解释理论）。  

- 报告本身是一项 **提案性工作**，而非提出新算法或新理论：  
  - 以一篇 arXiv 论文 (2006.02482) 为依托；  
  - 主要内容包括：哲学论证（为什么因果解释优于关联解释）、方法论流程（将 FCI 应用于 (Z, Ŷ)）、模拟验证、以及对两个真实图像数据集（鸟类分类、肺炎 X 光）的实证展示。  
  - **没有形式化的统计保证**（讲者在讨论环节直言「任何我能在数学上证明的定理，其假设在这个设置下都不成立，所以只能追求合理的近似」）。  

- 与研究者个人兴趣的连接：该工作属于 **因果推断的应用（可解释性）**，涉及 **图模型 / 因果发现** 和 **混淆控制**，但 **不涉及半参数效率理论、高阶 U-统计量或计算复杂度理论**。对于研究者来说，这篇报告可作为 Causal Inference 在 XAI 中应用的一个案例，但方法论深度有限。

---

### 二、最小内核 / 一个最简例子

#### 符号与设置

- **可观测数据**：{ (X_i, Y_i, Z_i) }_{i=1}^n，其中  
  - X = 低层输入（例如 256×256 像素），维度 q 很大；  
  - Y = 真实标签（例如是否患肺炎），但报告 **不关注 Y，只关注 Ŷ**；  
  - Z = 一组 **高层可解释特征**（如鸟的翅膀形状、颜色；或 X 光片上的医学发现标签），维度 p ≪ q。  
- **黑箱预测模型**：f: X^q → Ŷ，训练时使用 (X, Y)，但报告只关心 **f 的输出 Ŷ** 而非 Y。  
- **目标**：判断哪些 Z_j 是 Ŷ 的 **原因**（而非仅仅相关）。  

#### 核心假设

将真实生成过程近似为 structural causal model (SCM)：
1. Ŷ ≈ g(Ẑ_1,…,Ẑ_s, ε)，其中 {Ẑ} 是理论上所有与 Ŷ 相关的高层特征（包含我们未观测到的）；  
2. 每个 Ẑ_i = h_i(X, ν_i) 是低层像素的某个未知函数；  
3. 我们只观测到 Z ⊆ Ẑ（即 p ≤ s）；  
4. (Ẑ, Ŷ) 关于某个 DAG 满足 Markov 和 faithfulness，且 Ŷ **不是** 任何 Z 的祖先（Ŷ 不影响特征）。  

#### 最简特例：模拟实验（幻灯片第14-15页）

- **数据生成**：5000 张 2D 二值图像，包含四种形状：  
  - H = 水平条，V = 竖直条，C = 圆形，R = 矩形。  
  - 真实 label Y 由 V 和 C 决定（V 或 C 出现则 Y=1）。  
  - 混淆结构：U1 → H, U1 → V；U2 → C, U2 → R；且 H 和 V 也有自然关联（未完全画出但存在）。  
- **训练**：ResNet18 在像素上预测 Y，测试准确率 ≈81%，输出 Ŷ。  
- **因果发现**：只观测 Z = {H, V, R}（故意排除 C），运行 FCI 学习 (H, V, R, Ŷ) 的 PAG。  
- **结果**（右图）：  
  - V → Ŷ 或 V ◦→ Ŷ（V 是 Ŷ 的因果祖先或可能的因果祖先）；  
  - R ↔ Ŷ（R 与 Ŷ 之间有双箭头，表示因未观测的混淆而关联，无直接因果）；  
  - H 与 Ŷ 无直接边（可能通过 V 间接相关，但非直接因果）。  
- **为什么这个例子展示核心思想**：即使缺失重要变量 C，PAG 仍能区分出 V（真正原因）和 R（仅通过混淆关联），而 LIME/SHAP 等关联方法会错误地将 R 标为重要。

---

### 三、报告主体：讲者讲了什么

>[H:MM] 为大致时间点（以转写为准），部分时间点因 Q&A 穿插略有模糊。

**[0:00:06–0:02:10] 开场与动机**  
- 报告标题：Explaining the Behavior of Black-Box Prediction Algorithms with Causal Learning.  
- 合作者：Numair Sani, Ilya Shpitser（两位均于 JHU；讲者口音拼写为 "Numair"/"Ilia"，幻灯片正确）。  
- 实践动机：透明度/信任、算法审计（可靠性+公平性）。  
- 举例：Winkler et al. (2019) JAMA Dermatology 中手术标记 artifacts 影响皮肤病变识别；AlgorithmWatch 案例中 Google Vision API 对深肤色手的误标。

**[0:02:11–0:03:21] 哲学提案：什么是解释？**  
- 当前 XAI 方法（LIME, SHAP）聚焦于关联或局部近似。  
- 哲学背景：自 Hempel 的演绎-律则模型（D-N model）到统计解释模型，问题包括不对称性、无法区分相关/无关概括。  
- Woodward (2003) 的反事实因果理论：X 解释 Y 当且仅当对 X 的干预会改变 Y 的分布；解释回答“what would have been different”问题。  
- 报告聚焦 **type-level**（分布层面）而非 token-level（单个事件）。

**[0:03:22–0:24:10] 方法设置与 PAG 学习**  
- **设置**：低层 X（像素），黑箱 f 输出 Ŷ；高层 Z（可解释特征，p ≪ q）。目标是识别 Z 中哪些是 Ŷ 的原因。  
- **核心挑战**：未测量混淆（我们永远不会知道所有相关高层特征），所以需要允许任意隐变量的因果图模型。  
- **技术工具**：  
  - DAG → 隐变量投影 → MAG (Maximal Ancestral Graph) → PAG (Partial Ancestral Graph，等价类)。  
  - 边类型：→ 直接因果；↔ 隐变量混淆；◦→/◦–◦ 方向不确定性。  
  - 使用 **FCI 算法** (Fast Causal Inference)：约束学习，通过条件独立性测试删除边，再通过 collider 规则和 acyclicity 定向。  
  - 假设：Markov、faithfulness、Ŷ 非 Z 的祖先。  
- 幻灯片第13页给出了更正式的假设（Ŷ 近似为 g(Ẑ, ε)，Ẑ = h(X, ν)），转写中仅口头提及，但较含糊。

**[0:24:11–0:35:26] 模拟实验**  
- 生成5000张图像，含 H/V/C/R 四种形状，标签 Y 由 V 和 C 决定。  
- 训练 ResNet18 在像素上预测 Y，准确率81%。  
- 故意排除特征 C，只对 (H, V, R, Ŷ) 运行 FCI。  
- 结果 PAG 正确显示 V 是 Ŷ 的可能原因，R 通过混淆关联（双箭头），H 无直接边。  
- 讨论环节：讲者澄清“FCI 学到的是对内部机制的近似，而非声称神经网络内部真有一个 PAG”。

**[0:35:27–0:42:28] Q&A 中断（Vanessa 关于“算法上下文中的混淆含义”）**  
- 讲者回应：混淆指的是未测量高层变量（如鸟的喉部颜色）同时影响其他测到的特征和 Ŷ，导致关联但不因果。

**[0:42:29–0:47:57] 真实数据实验**  
- **鸟类分类** (Caltech-UCSD Birds 200-2011)：  
  - 3538 张图片，26 个序数属性（如背纹、眼颜色），9 类标签（分组后）。  
  - ResNet18 准确率 86.57%。  
  - **边缘稳定性**：对数据子样本多次运行 FCI，记录 Z → Ŷ 或 Z ◦→ Ŷ 的频率。最稳定的是 Wing Shape, Wing Pattern, Underparts Color, Upper Tail Color；Belly Pattern 和 Wing Color 频率极低。  
- **肺炎 X 光** (ChestX-ray8)：  
  - 239 张图像，7 个放射科医生发现（如 infiltration, atelectasis, effusion 等），二分类。  
  - ResNet18 准确率 74.55%。  
  - 最稳定因果特征：Infiltration, Atelectasis, Effusion（这些确实与肺炎相关）；Mass, Nodule, Cardiomegaly 等被判定为无关或仅混淆关联。  
- **与 LIME/SHAP 对比**（幻灯片第24-25页）：  
  - LIME 输出大片高亮像素，难以泛化；SHAP 给出像素级 Shapley 值，但同样缺乏高层语义。

**[0:47:58–0:52:27] 结论与开放问题**  
- 主要观点：PAG 学习能区分可能因果祖先与仅混淆相关，可结合背景知识（如 Ŷ 非 Z 的祖先）。  
- 依赖：需要预先定义的可解释特征。  
- 未来问题：如何自动学习可解释特征？如何验证所学的因果结构？能否用模拟干预验证？  

**[0:52:28–1:04:39] 讨论环节（Joshua Loftus）**  
- Loftus 强调：解释 Ŷ 不等于解释 Y；将解释称为“因果”可能误导用户。  
- 他提问：边缘稳定性的统计保证？能否有理论保证黑箱解释对应于真实世界因果？  
- 讲者回应：  
  - 承认区分 Ŷ 与 Y 至关重要，应明确我们解释的是“算法世界”而非“真实世界”；  
  - 边缘稳定性可参考 Bühlmann 等人的 FDR 控制工作（但只对邻接性有效，不保证方向）；  
  - 对形式化保证持怀疑态度，因为任何分布假设在此场景下都不现实，故只能追求合理近似。

---

### 四、对应论文与开放问题

#### 对应论文

- **arXiv 2006.02482**（2020）  
  标题：*Explaining the Behavior of Black-Box Prediction Algorithms with Causal Learning*  
  作者：Numair Sani, Daniel Malinsky, Ilya Shpitser  
  （讲者确认“draft paper”，幻灯片末尾给出该引用。转写中拼写为“Numair Sani”“Ilia Shpitser”，与幻灯片一致。）

- 典型引用格式（幻灯片第27页）：  
  N. Sani, D. Malinsky, and I. Shpitser, “Explaining the Behavior of Black-Box Prediction Algorithms with Causal Learning.” arXiv 2006.02482, 2020.

#### 报告留下的开放问题（每条扎根于转写对应点）

1. **如何自动学习可解释的高层特征？**  
   - 转写 [0:46:35–0:47:30] 讲者提到：“can they be learned automatically… or is human input at the feature selection stage essential?” 以及 “we explored a few automated approaches, none worked”。  
   - 问题：是否存在某种无监督/弱监督方法从图像或文本中自动发现与 Ŷ 因果相关的语义特征？

2. **可解释特征应满足什么确切的经验性标准（desiderata）？**  
   - 转写 [0:47:30–0:47:40]：“What desiderata should ‘interpretable features’ satisfy exactly?”  
   - 问题：理想的 Z 应该满足因果充分性（causal sufficiency）吗？或者仅需可干预性（manipulability）？是否有形式化定义？

3. **如何模拟现实干预来验证所学的因果结构？**  
   - 转写 [0:47:42–0:47:50]：“Can we simulate realistic interventions to validate/learn from?”  
   - 问题：能否利用生成模型（如 GAN）或反事实生成来评估“如果改变了特征 Z_j，Ŷ 是否会如 PAG 预测的那样改变”？

4. **边缘稳定性方法是否有理论保证（如 FDR 控制）？**  
   - 转写 [0:51:57–0:52:26] 讲者提及 Bühlmann 等人的 FDR 结果，但仅对邻接性（是否存在边）有效，不保证方向。  
   - 问题：更严格的 inferential 框架（如用于 PAG 方向选择的置信度、多重比较校正）是否存在？能否推广到方向性判断？

5. **在偏差或过拟合情况下，解释质量如何变化？**  
   - 转写 [0:58:40–0:58:42] Loftus 提问：“do the qualities of these explanation… vary if the black box is overfit or has poor out-of-distribution generalization?”  
   - 问题：当黑箱的泛化性能较差时，所学的 PAG 是否仍然有意义？是否更可能捕捉到虚假关联而非稳定因果结构？

6. **使用相同数据学习高层特征和训练黑箱时，假定方向性是否被违反？**  
   - 转写 [0:58:58–1:00:07] Loftus 问：“假设是否可能被破坏，如果你使用相同数据学习高层特征和训练黑箱？”  
   - 问题：如果 Z 本身也是从 X 通过某种算法（如 DNN 特征提取）得到的，那么 Z → Ŷ 的方向假设是否仍然成立？数据复用可能导致循环论证或混淆。

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

