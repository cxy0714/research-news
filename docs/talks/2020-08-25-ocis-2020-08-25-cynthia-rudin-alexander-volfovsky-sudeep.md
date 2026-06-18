# Almost Matching Exactly

**讲者**: Cynthia Rudin, Alexander Volfovsky, Sudeepa Roy  
**讨论人**: Guillaume Basse  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2020-08-25  
**主题**: 因果推断  
**视频**: <https://www.youtube.com/watch?v=-So_cL-eMFQ> · [幻灯片](https://drive.google.com/file/d/1gdVhaltmZWJ5QvoQU1S2cJod0xYOkbNe/view?usp=sharing)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

---

### 一、这场报告在讲哪条工作线: Almost Matching Exactly 及其定位

这场报告的核心工作线是 Alomost Matching Exactly (AME) ——一套用于观测性因果推断的新型匹配方法论。它不仅是一篇论文作者提出的算法合集 (FLAME/DAME) ，更是一个由杜克大学三位教授 (计算机科学的 Cynthia Rudin, 统计系的 Alexander **Volfovsky (报告中的 Volfovsky多次出现) ，和计算机系的Sudipa Roy) 引领的、有明确方法论立场的研究项目。

**1. 子方向追问的问题**

整个子方向追问的核心问题是: **在观测数据中，如何可靠地估计条件平均处理效应 (CATE) ，同时保持过程可解释、可验证？**

- **目标**：从每对粗协整的单元里，构造一个内部高度同质的“准重-析”分组（通常是治疗组与控制单元的匹配组），然后比较组内结果。
- **经典路径**：Rosenbaum & Rubin (1983) 的倾向性得分（覆盖研究的主要前提条件）将高维协整X投影为标量 p(X)，消除了协整维数的诅咒，但仍需要面对：（1）**目标量通常是 ATE，而非 CATE**，因为一维投影牺牲了个体保真度；（2）匹配后人看起来很“等价于随机化”，但实际比较的是“具有相似倾向得分”的个体，这些人本身的协整概览可能差距巨大。
- **互补路径**：精确匹配 (exact matching / subclassification)基元是孪生思想，但由于维数灾难，几乎不可能在高维协整上找到完备的精确匹配。因此，Rosenbaum (1983) 就指出“更多的子类空了，即在亚总体下无法进行因果推断”。

**2. 奠基与主流路线**

保障无混杂性 (ignorability) 的情况下，估计CATE的三大途径是:
- **直接结果模型** (BART; Hill, 2011)
- **重加权/倾向得分分层** (PS stratification, 逆概率加权 IPW)
- **平衡/匹配** (Covariate matching, Mahalanobis distance matching, genetic matching; Diamond & Sekhon, 2013)
- **组合法** (Doubly Robust, Targeted Maximum Likelihood Estimation, Causal Forests)

本工作属于 **匹配** 这一分支，但其核心创新不在于提出一个新的匹配距离（如 Mahalanobis 或`遗传匹配），而在于**: 在匹配过程中**直接、自适应地学习协整重要性的方法**，将“匹配”与“预测”问题联系起来。

**3. 当前前沿与本工作的位置**

在匹配方向，一个主要的分水岭是：
- **传统的 projection-based matching** (PSM, prognostic scoring; Hansen, 2008)：在匹配阶段避免接触结果变量，仅利用协整提供的信息。强调设计的客观性 (Rosenbaum, 2007).
- **结果引导的匹配（outcome-guided matching）**: 在匹配过程中使用结果信息来筛选协整，识别哪些协整对预测结果最关键，从而在保持匹配精度的同时控制维数。这套理论在实践中被认为本质上违背双盲设计。

AME就站在此分水岭上，采用了鲜明的目标: **使用结果信息（通过一个单独的“训练集”），主动识别哪些协整值得精确匹配，哪些可以忽略。**

**关键相关工作记要（可验证引用）**:
- Rosenbaum & Rubin (1983).  \textit{The central role of the propensity score...}. Biometrika.
- Rubin (2007). 关于观察性研究设计的书籍，明确主张应屏蔽结果数据。
- Hansen (2008). \textit{The prognostic analogue of the propensity score}. Biometrika.
- Hill (2011). \textit{Bayesian nonparametric modeling for causal inference}. JCGS.  (BART).
- Schneeweiss et al. (2009). 高维倾向得分模型中协整筛选的实证。
- Diamond & Sekhon (2013).  \textit{Genetic matching...}. Review of Economics and Statistics.

---

### 二、最小内核 / 一个最简例子

**1. 符号体系（基于转写与幻灯片 [H:00:14-00:19]）**

- **数据**: 匹配集 (matching set)，由观测组成, 每个含: 协整向量 **X** (大小为 p 的列, 元素假设是二值或多值分类变量, 如 {0,1,2})；处理变量 **T** ∈ {0,1}；结果变量 **Y** (我们在主要例子中是连续的)。
- **输出**: 对每个治疗单元 **i** (T=1)，构造一个匹配组 \(M(i,\theta)\) = {控制单元 j 其 X[j] 在 `\theta` 指标协整上与 i 完全相同}。
- **核心变量**: **`θ`** (Theta) ——一个大小为 p 的**二进制变量选择指示变量**，即哪些协整要精确匹配。
  例如: θ = [1, 1, 0, 0, 1] 表示只匹配变量 1、2、5。匹配组就是在这个三子空间里值相同的所有控制单元。
- **训练集**: 来自同一个数据分布但不同子集的**独立训练样本**。 其唯一作用是**计算** `θ` 的好坏。
- **误差度量**: **PE(θ)** = 在训练集上，用 `θ` 选出的协整去拟合结果 Y(使用任意机器学习算法 F, 如线性回归或 CART) 的均方预测误差。

**2. 一个最简例子（d=2 协整，都是二值）**

假设我们只有 2 个协整: `X1` (是否吸烟, 0/1), `X2` (是否住地下室，0/1)。 共有 4 类人。

- **数据**:
  - 训练集: 用来决定哪个协整预测 Y (例如 Y = 肺癌风险) 重要。
  - 匹配集: 用来做匹配计算 CATE.
- **训练集学习 `θ`**:
  - F 被现代线性回归模型。
  - 尝试两种 `θ`:
    1. θ₁ = [1, 1] (匹配 `X1` 和 `X2`)
       - 拟合训练集上的 Y=f(X1, X2) → 效果好，因为 X1 和 X2 都与 Y 强相关。但匹配集里有 N=100 个单元，按 4 类精确匹配，每一类只有 ~25 个单元（1 治疗 24 控制，如果有重叠的话），匹配组太小。
    2. θ₂ = [1, 0] (只匹配 `X1`)
       - 拟合 Y=f(X1) → 效果稍差（因为漏掉了 `X2` 的效应）, 但匹配集里现在每个 X1 值都有 ~50 个控制单元（非常多），匹配组很大、稳定。
  - **关键**: PE(θ₁) < PE(θ₂)，但 θ₁ 在匹配集上不可行（很多治疗单元在匹配组里找不到严格匹配，因为 X2 的取值组合太多）。AME的核心就是平衡这两个。
- **算法执行-匹配**: 对一个特定的治疗单元（例如一个有 1个吸烟=1、住地下室=1）
  - **FLAME 第一轮**: 匹配所有的 4 个匹配组.
  - 发现 `θ=[1,1]` 无法形成有效组（因为只有 1 个这样的治疗单元，匹配集里该类别有 0 个控制单元），于是 `θ=[1,1]` 被放弃。
  - FLAME 第二轮: ML 说 `X2` 是较不重要的；丢弃`X2`，只保留 `X1` → 有效匹配组大小很大 (例如匹配集里有 50 个不吸烟的控制单元给吸烟的治疗单元；后者分成两类).
  - FLAME 第三轮: 进入DAME阶段尝试精细调整：是否能把X2的其中一些取值拉回来 （“放回”子集），看看能否在不显著降低匹配组大小的情况下提高预测精度。 例如, 对一个单元 `(X1=1，X2=陳)》`，DAME尝试匹配 `(X1=1，X2=0)` 的控制单元——形成一个 包含 2 种地下室状态但吸烟状态一致的组.
- **CATE 估计**: 对每个治疗单元 i, 取其匹配组 M(i)，组内取平均 Y(T=1) - Y(T=0)。这给出每个（或相近协整模式）人的 CATE. 可以进一步对匹配组平滑。

---

### 三、报告主体：讲者讲了什么

**[0:00:00 – 0:05:00]** **问题设定** (Cynthia Rudin)
- 提出“精确匹配-牢记精良”是人们真正想要的：做出如孪生试验般的匹配，直接比较。
- 描述维数灾难: 协整多，匹配组就空。因此需要从 big pile of data 中挑出重要的协整去精确匹配。
- 引子“toenail problem”: 如果没用距离度量，大量无关协整（如指甲长度）会 hiijack 距离，导致匹配选择完全错误的变量。

**[0:05:00 – 0:13:20]** **相关工作 & 动机** (Alex Vo l f o v s k y)
- 回顾匹配文献：偏向 ATE 而非 CATE；使用固定距离而非自适应学习。
- 强调 Rosenbaum & Rubin (1983) 对精确匹配 (subclassification) 的评价：直观、有说服力，但“高维灾难”使全部空箱子。
- 展示 Lalonde 里的一个实例：我们的方法与 PS 匹配的比较，AME的结果匹配组更醒目地内部一致。

**[0:13:20 – 0:31:00]** **AME 形式化与 FLAME/DAME 算法** (Cynthia Rudin)
- 严格定义 `θ`, `PE(θ)`, 匹配组 `M(i,θ)` 的概念。 [0:17:50]
- 形式化**对每个治疗单元的问题**: 选 `θ` 使得其训练集 PE 尽量小，同时保证匹配组非空。 [0:18:15]
- 两步法:

  1. **FLAME**: 贪心逆向消除 (backward elimination)
     - 从对全部协整（θ = all-1）开始，跑 BasicExactMatch。
     - 用训练集 ML 找出当前最不重要的一个协整（其在训练中减少 PE 最小），丢弃。
     - 重复，直到 PE 上升至预设阈值以上（如增加 5%）。所有未被匹配的单元宣告无法估计. [2:21:00]

  2. **DAME**: 更精细的回溯消除 (subset elimination)
     - 从 FLAME 结束位置或初始大量协整开始，每次 ML 选出**一个能丢弃的**变量子集（不一定是单个，看哪个子集对PE的提升最小），丢弃并尝试匹配。关键性质: 必须在丢弃子集之前，所有该子集的真子集都已被考虑过（downward-closure property），这确保最优子集不会被早扔。 (转写用[0:22:00-00:23:00] 的例子解释：配对消除后，子集 `{10，9}` 只能丢弃一次，是在 `{10}` 和 `{9}` 都已被尝试后)。 停止条件仍然是 PE 阈值。

- **实践**：通常 FLAME 快速降到可管理维度 (~10)，然后 DAME 来更细调。

**[0:23:20 – 0:29:00]** **仿真实验** (Cynthia Rudin)
- 设计: 仅前 10 个协整有效（线性和二次项），治疗/控制组在 20 个无关协整上分布不同（无关协整忠实地模仿了“脚指甲问题”）。
- 燃耗的性能: 非参 FLAME 完美（无噪声），因为精确匹配能处理非线性、缺模型纠正。标准线性回归应当 misspecified。
- 与其他方法对比：Genetic Matching、Mahalanobis、PSM (各种近邻) 都无法清晰得到 CATE（出现散点云）；Causal Forests 预测出 150 (+真实20)；BART 勉强好但不透明；CTMLE 也不好。 [0:26:00]这组的对比明确支持了 FLAME 在识别好的协整子集上的优势。

**[0:29:00 – 0:38:00]** **计算可伸缩性** (Sudeepa Roy)
- 聚焦核心子例程: BasicExactMatch，需要快速分斎 + 验证每组同时含 T=1 和 T=0.
- 两个系统:
  - **Flame-Bit**: 用位向量（bit-vector）编码协整数值（每个协整对应一位），通过巧妙的 counting 判断组是否为有效组。适用于小数据（内存）。
  - **Flame-DB**: 用标准 SQL 的 `GROUP BY ... HAVING COUNT(T=1)>=1 AND COUNT(T=0)>=1`。利用 DBMS 几十年的优化（索引、并行等），可扩展到 1.2M 条记录 (US Census 1990 数据)。[0:34:00-00:35:00]

**[0:38:00 – 0:53:00]** **可视化、连续扩展与总结**
- 皇帝图 (Natality dataset, 2010) : 非常直观——展示匹配组大小 vs. CATE 估计值。告诉研究者哪些 group 太不稳定（红点，小样本，过大噪声，应忽略）。 [0:44:00]
- 连续变量的方法: **自适应超矩形** (Adaptive Hyperbox; Morucci-Orlandi-Roy-Rudin-Volfovsky, UAI 2020) 用于在协整空间上寻找大且恒定（平）的 K 维箱（U邸-预测表面平坦），使匹配高效；**MALTS** (Matching After Learning To Stretch; Parikh-Rudin-Volfovsky, arXiv 2020) 学习一个可解释的指标拉伸。 [0:48:30]
- **总结** 与更多扩展：网络、工具变量、生存分析、双重差分。

**[0:53:00 – end]** **讨论 (Guillaume Basse)**
- 提供了技术评论: 与其他结果引导方法 (如预后评分分层) 的关系，并指出使用结果信息的传统反对意见 (Rosenbaum 设计哲学) 。 他对AME的独立训练集用法表示赞许（这使客观化）。
- 提出关键开放问题:
  - **后匹配推断（variance estimation）**: 处理数据有高度自适应选择，如何正确获取标准误差？[有提及但尚未解决]
  - 大规模行政数据应用时，协整不足（impoverished covariates）导致 bias 大？需敏感度分析 (sensitivity analysis)。 [此问题直接引用了 Cook (2000s 论文) 的批评，强调需要 SUTVA 外还需更多条件。] [1:05]
- 讲者回应: 在考虑用 BART 等为FLAME group 提供后验方差。同意敏感度分析是正确方向，并指出 *局部精度* (locally accurate training for each unit) 是待考虑的扩展。 [1:09]

---

### 四、对应论文与开放问题

**0. 对应论文**

本工作主线，对应几篇有明确标注的论文：

1. **Wang, Morucci, Awan, Liu, Roy, Rudin, Volfovsky (2019).** \textit{FLAME: Fast Large Almost Matching Exactly}. (可能是 AISTATS 或类似会议，但在幻灯片中被错误镜像标注）。转写说"Wang-Morucci-Awan-Liu-Roy-Rudin-Volfovsky (2019)"，"AISTATS 2019"。这个是三篇最初算法介绍。
2. **Dieng, Liu, Roy, Rudin, Volfovsky (AISTATS 2019).** \textit{DAME: Dynamic Almost Matching Exactly}. （幻灯片有误，再确认标题）
3. **Morucci, Orlandi, Roy, Rudin, Volfovsky (UAI 2020).**  \textit{Adaptive Hyper-Boxes for Conditional Average Treatment Effects}. （连续协整扩展）
4. **Parikh, Rudin, Volfovsky (arXiv 2020, OS 2020).** \textit{Matching After Learning to Stretch (MALTS)}. （连续协整扩展：learned stretch metric）
5. **Morucci, Awan, Orlandi, Roy, Rudin, Volfovsky (AISTATS 2020).** \textit{Causal Inference on Relational Data}.
6. Slide 提到 Awan-Liu-Morucci-Roy-Rudin-Volfovsky (UAI 2019) 可能是 instrumental variable 匹配的论文。

- **注意**: 转写里很多人名和年份靠ASR识别，转写里出现的 "Valdovsky" *应为* Volfovsky。 https://almostmatchingexactly.github.io 是该项目的已确认官方网址。

**2. 报告留下的明确开放问题**

每条问题直接来自于报告的某个时刻，**不对可行性或匹配用户工具箱做判断**。

1.  **推断（Inference）与方差估计** [0:59:20-01:00:30, 讨论环节多处]。
    - **具体描述**: 讲者承认后匹配推断尚不成熟。 因为 `θ` 是数据驱动的，且通过交叉拟合保留 (但训练/匹配划分已提供一些抗多重复用) 。 使用 bootstrap、子采样，或“用 BART 得到后验拟合然后计算方差”被提及作为探索方向。 目前没有形式化的大样本置信区间结果。

2.  **敏感度分析** [1:05:30-1:06:00]
    - **具体描述**: 讲者与讨论者都指出，在行政数据（如 U.S. Census) 上使用时，若协整稀疏 (impoverished covariates) ，忽略性 (ignorability) 可能假定不成立。 目前方法只基于*观察到的*协整来预测。 弘需开发一个AME专属的敏感度分析框架（如比率或Rosenbaum bounds），以量化未观测混杂可能的影响。

3.  **对每个单元的不同 `θ` 是否影响结果可比性** [0:32:00 左右的Q&A与后续交流会]。
    - **具体描述**: 在一次 Q&A 里，Fred Gruber 提问: 每个治疗单元可能匹配在不同的 `θ` 子集上（如单元 A 只匹配变量 1,2，单元 B 只匹配 3,4），是否破坏了匹配的可比性？ 讲者回应“只要那个子集预测能力好就行”。 但这背后的 ** 因果解释** 一致性仍需深入探讨——不同子集对应不同的条件分布，跨子集的 CATE 是否可比？ (这个问题本质: CATE 是 “给定 X”，但不同的 `θ` 对应忽略了一些X，形成近似，近似导致的 bias 是多少？)

4.  **局部预测精度** [1:08:00-1:09:00, Vo l f o v s k y 回应]
    - **具体描述**: 为了判断一个匹配组的好坏，只在全局训练集上计算 `PE(θ)`，但匹配可能在协整的一个局部区域（例如某个特定基组）。 但 `PE(θ)` 是在*整个* 训练集上计算的，而非该局部区域。 这会引入偏差：变量的重要性可能是异质的（在某个区域的群体里 X2 重要，在另一里不）。 讲者回应这是待处理的开放扩展：需要一种“局部准确”的预测模型，可能使用 K 近邻或加权的版本。

5.  **混合协整类型与距离度量的自动化** [0:48:00 左右, 当转到 MALTS & hyperbox 时]
    - **具体描述**: 针对连续与分类混和协整的正确自动匹配，目前渐进的 MALTS 和 hyperbox 假设某种 metric 学习，但**它的理论属性（一致性、最优性）以及高维的适用性**几乎是悬而未决的。 MALTS 提出一个可解释的拉伸度量，但其与因果参数估计的交织并无大样本经典理论。

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

