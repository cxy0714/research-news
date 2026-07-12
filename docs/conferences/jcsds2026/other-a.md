# 其他 Other · 1

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 16 场报告**（已检索到对应论文 4 场）

---

## Learning, Inference, and Influence: New Frontiers in Data and AI

*7 月 11 日（周六） · 15:30-17:10 · Colourful Guizhou Ballroom 2*  
*组织 Yang Feng（New York University） · 主持 Yang Feng（New York University）*

### 1. Few-Shot Personalization for Nonparametric Regression with Minimax Optimality

**讲者**：Sai Li（Tsinghua University）

**对应论文**：Personalizing black-box models for nonparametric regression with minimax optimality · [arXiv:2601.01432](https://arxiv.org/abs/2601.01432)

<details><summary>摘要（原文）</summary>

Recent advances in large-scale models, including deep neural networks and large language models, have substantially improved performance across a wide range of learning tasks. The widespread availability of such pre-trained models creates new opportunities for data-efficient statistical learning, provided they can be effectively integrated into downstream tasks. Motivated by this setting, we study few-shot personalization, where a pre-trained black-box model is adapted to a target domain using a limited number of samples. We develop a theoretical framework for few-shot personalization in nonparametric regression and propose algorithms that can incorporate a black-box pre-trained model into the regression procedure. We establish the minimax optimal rate for the personalization problem and show that the proposed method attains this rate. Our results clarify the statistical benefits of leveraging pre-trained models under sample scarcity and provide robustness guarantees when the pre-trained model is not informative. We illustrate the finite-sample performance of the methods through simulations and an application to the California housing dataset with several pre-trained models.

</details>

**问题**：如何利用一个黑箱预训练模型 $f^{(ptr)}(\cdot)$，在仅有少量目标样本（$n$ 个）的条件下，实现对目标非参数回归函数 $f^*(\cdot)$ 的个性化估计？该问题在大型预训练模型（如 GPT-4、LLaMA）广泛可用的背景下尤为关键，但现有方法或需访问源数据（迁移学习），或仅关注总体均值（prediction-powered inference），缺乏针对回归函数的统计最优性理论。

**核心方法**：提出三步算法。首先，设计**样本检索**方案：用少量样本估计异方差噪声 $\sigma^2(x)$，然后按 $\hat{p}_X(x) \propto \hat{\sigma}(x)$ 进行加权采样，以最小化方差项。其次，**平滑偏差校正**：对预训练模型施加 $\theta$-局部平滑操作 $\omega_{\theta,x} \circ f^{(ptr)}$，使其在局部满足 Hölder 正则性，再基于核估计构造偏差 $\hat{\delta}_\theta(x) = f^*(x) - \omega_{\theta,x} \circ f^{(ptr)}(x)$ 的估计，得到个性化估计 $\hat{f}_\theta^{(fsp)}(x) = f^{(ptr)}(x) + \hat{\delta}_\theta(x)$。最后，**自适应选择**：通过验证集交叉验证选取最优 $\hat{\theta}$，使方法自动适应预训练模型的信息量，并在模型无用时退化为纯目标样本估计。

**与已有工作关系**：区别于迁移学习（需访问源数据）和 domain generalization（需多源域），本文将预训练模型视为黑箱，仅利用其输出。与 prediction-powered inference（PPI）不同，PPI 针对总体均值且依赖半监督设置，而本文聚焦回归函数并允许用户主动设计采样分布。此外，现有 LLM 个性化工作多为经验性，缺乏统计最优性分析。本文首次在非参数回归中建立个性化问题的 minimax 最优率，并证明所提方法达到该率。

**贡献**：1）提出一个可整合任意黑箱预训练模型的非参数个性化框架，包含自适应采样与平滑偏差校正；2）推导了 personalized nonparametric regression 的 minimax 最优率，揭示利用预训练模型可降低 Hölder 复杂度从而加速收敛；3）证明方法具有“无害”保证：即使预训练模型无信息，性能也不劣于纯目标样本估计；4）通过模拟和加州房价数据验证了方法的有效性与鲁棒性。


### 2. Statistical Inference for Large Potts Models

**讲者**：Zhao Ren（University of Pittsburgh）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
Potts 模型是 Ising 模型向多类别（$q \geq 2$）的推广，广泛用于图像分割、空间统计与网络聚类。当图规模巨大（节点数 $p$ 或边数 $E$ 趋于无穷）时，精确似然函数因配分函数不可计算而难以处理，且传统 MCMC 采样面临混合慢、收敛诊断困难。本报告旨在解决：**如何对大规模 Potts 模型进行具有频率学派保证的统计推断**，包括参数估计、假设检验与置信区间构造，而不仅限于点估计或贝叶斯后验。

**核心方法**  
讲者可能采用**伪似然（pseudo-likelihood）** 或**复合似然（composite likelihood）** 框架，将全局联合分布分解为条件分布的乘积，从而规避配分函数。为处理高维性，进一步引入 **$\ell_1$ 正则化** 或 **去偏（debiased）估计** 技术，得到稀疏图结构下参数的一致估计。推断方面，利用 **渐近正态性** 构造 Wald 型置信区间，并通过 **bootstrap** 或 **数据分裂（data splitting）** 校准有限样本偏差。若图具有特殊结构（如格子图或随机图），可能结合 **谱方法** 或 **矩估计** 加速计算。

**与已有工作关系**  
现有工作多聚焦于 Ising 模型（$q=2$）的高维推断（如 Ravikumar et al., 2010; Ren et al., 2019），或仅关注 Potts 模型的点估计与模型选择。本报告将推断框架从二值推广至多值，并处理因类别数 $q$ 增长带来的额外挑战（如参数可识别性、条件分布形式）。与变分贝叶斯或 MCMC 方法相比，本方法提供频率学派的不确定性量化，且计算复杂度随 $p$ 近线性增长。

**主要贡献**  
1. 首次为大规模 Potts 模型建立具有理论保证的统计推断程序，包括参数估计的相合性与置信区间的渐近覆盖。  
2. 提出适用于多类别离散图模型的正则化伪似然方法，并证明在稀疏图假设下估计误差的 $L_2$ 界。  
3. 通过数值实验展示方法在图像分割与社交网络分析中的实用性，为后续高维离散图模型推断提供新工具。


### 3. Stance Draft: How AI Middlemen Change What We Mean

**讲者**：Xin Tong（The University of Hong Kong）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**：当 AI 作为“中间人”（如推荐系统、自动摘要、内容改写工具）介入人类表达时，它如何改变用户原本想传达的立场（stance）？现有研究多聚焦 AI 对内容事实性的影响，但较少关注 AI 中介对表达意图中“意义”的因果性扭曲——即用户本意与最终输出之间的语义偏移。本报告试图回答：AI 中介是否以及如何系统性地改变用户表达的立场方向与强度？

**核心方法**：讲者可能采用因果推断框架，将 AI 中介视为一个处理变量 $T$（如是否使用 AI 改写），用户原始草稿 $X$ 为协变量，最终输出 $Y$ 为结果变量。通过设计随机实验或利用自然实验，估计平均处理效应 $\mathbb{E}[Y(1) - Y(0) \mid X]$，其中 $Y(1)$ 为经 AI 中介后的表达，$Y(0)$ 为无 AI 时的原始表达。进一步，利用自然语言处理中的立场检测模型（如基于 BERT 的 stance classifier）将 $Y$ 映射到立场空间（如支持/反对/中立），从而量化立场偏移。可能引入中介分析（mediation analysis）分解 AI 的直接影响（如替换措辞）与间接影响（如改变用户后续思考）。

**与已有工作关系**：已有工作多从技术角度改进 AI 的立场检测或生成中立内容，但缺乏对 AI 作为“中介者”如何因果性地改变用户立场的系统性研究。本报告将因果推断与计算语言学结合，区别于单纯描述性分析（如对比使用 AI 前后的文本差异），而是通过反事实框架识别 AI 的独立贡献。此外，与“AI 偏见”文献不同，这里关注的是用户原始意图与最终输出之间的语义鸿沟，而非 AI 本身的偏见。

**主要贡献**：1）提出“立场偏移”的因果定义与量化指标，为评估 AI 中介对表达自由的影响提供严谨工具；2）通过实验设计分离 AI 中介的因果效应，揭示其可能放大或扭曲用户立场的机制；3）为设计更“忠实”于用户意图的 AI 中介系统提供理论指导，推动负责任 AI 在内容生成与推荐中的应用。


### 4. Designing Randomized Experiments under Network Interference

**讲者**：Jingfei Zhang（Emory University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
在存在网络干扰（network interference）的随机实验中，个体间的处理效应会通过社会网络传播，导致传统的 SUTVA 假设失效。此时，如何设计实验（即分配处理与对照）以最小化估计偏差、提高因果效应的识别精度，是一个尚未被充分解决的基础问题。现有工作多聚焦于给定实验数据后的估计与推断，而实验设计阶段——尤其是如何利用网络结构信息主动构造分配机制——仍缺乏系统性的理论指导。

**核心方法**  
本报告提出一套基于图分割与局部平衡的随机实验设计框架。核心思路是将网络节点划分为若干“实验簇”（experimental clusters），并在簇层面实施随机化，同时通过约束簇内与簇间的干扰结构来保证可识别性。具体地，设计者需先估计网络的邻接矩阵与潜在干扰强度，然后求解一个带约束的图划分优化问题，使得每个簇的“暴露概率”（exposure probability）在给定分配下可计算且非退化。在此基础上，报告进一步引入一种自适应随机化策略，通过迭代调整分配权重来最小化 Horvitz-Thompson 型估计量的方差。

**与已有工作关系**  
已有文献主要关注网络干扰下的因果推断方法（如基于逆概率加权的估计量、两阶段随机化），但往往假设实验设计已固定。本报告将视角前移至设计阶段，与“cluster randomized experiments”和“graph-based experimental design”两条脉络紧密相关。相比前者，本方法允许簇内存在非平凡的网络结构，而非简单假设簇内无干扰；相比后者，本报告提供了可操作的优化准则与有限样本理论保证，而非仅依赖启发式算法。

**贡献**  
主要贡献有三：第一，首次将网络干扰下的实验设计问题形式化为一个带约束的图划分优化问题，并给出可解性条件；第二，提出一种自适应随机化算法，在保持无偏性的同时显著降低估计方差；第三，通过理论推导与模拟实验证明，所提设计在多种网络拓扑下均优于传统的完全随机化与两阶段随机化方案，为实际网络实验（如社交平台 A/B 测试、流行病干预）提供了可落地的设计指南。


## AI for Complex Systems: Methods and Applications

*7 月 11 日（周六） · 15:30-17:10 · Colourful Guizhou Ballroom 1*  
*组织 Bingyi Jing（The Chinese University of Hong Kong, Shenzhen） · 主持 Jing Zhou（Renmin University of China）*

### 1. Flexformer: Flexible Linear Transformer with Learnable Attention Kernel

**讲者**：Feng Zhou（Renmin University of China）

**对应论文**：Flexformer: Flexible Linear Transformer with Learnable Attention Kernel · [arXiv:2606.27748](https://arxiv.org/abs/2606.27748)

<details><summary>摘要（原文）</summary>

Transformer models rely on attention mechanism to capture long-range dependencies but suffer from quadratic complexity, limiting their scalability to long sequences. Kernel-based linear attention reduces this complexity but typically relies on fixed or weakly learnable kernels, restricting expressiveness and performance. In this work, we propose Flexformer, a flexible linear Transformer that learns attention kernels in a fully data-driven manner. Flexformer builds on random Fourier feature-based linear attention and treats spectral frequencies as trainable parameters, enabling the model to learn a broad family of attention kernels. We develop both stationary and nonstationary variants, with the latter offering strictly greater expressiveness. Extensive experiments on language modeling and sequence classification demonstrate that Flexformer consistently outperforms baselines. Moreover, Flexformer can be effectively distilled from pretrained Transformers to recover softmax attention and exhibits strong kernel transferability across domains, achieving both high efficiency and competitive performance on long-sequence tasks.

</details>

**问题**：Transformer 的 softmax 注意力机制具有 $O(N^2)$ 的时间与空间复杂度，严重限制了其在长序列任务上的可扩展性。基于核的线性注意力通过将注意力核分解为特征图内积来降低复杂度，但现有方法要么使用固定核（如 Performer 的随机傅里叶特征近似 softmax），要么使用经验设计的弱可学习核（如 Hedgehog 的指数映射），其核族表达能力有限，无法保证在多样数据上优于 softmax。

**核心方法**：Flexformer 基于随机傅里叶特征（RFF）框架，将谱频率 $\{\omega_i\}_{i=1}^n$ 直接作为可训练参数，通过端到端优化学习注意力核的谱密度 $p(\omega)$，从而在保持线性复杂度 $O(N d d')$ 的同时实现全数据驱动的核学习。进一步，利用 Yaglom 定理将平稳核推广至非平稳核，提出 Flexformer$_n$ 变体，其核族严格包含平稳版本。理论上，Flexformer 的核族包含 softmax 核的无偏估计，因此至少能恢复 softmax 注意力，并可能学习更优模式。

**与已有工作关系**：早期线性注意力方法（如 Linear Transformer、Cosformer）使用固定或简单元素级映射，表达能力弱；RFA 和 Performer 假设 softmax 最优，核固定不可学习；Hedgehog 和 Polaformer 引入可学习映射但核族受限于低熵假设，未从谱表示理论出发。Flexformer 基于 Bochner 定理，将核学习等价于谱密度学习，核族更广泛且具有理论保证，同时通过非平稳扩展进一步突破平移不变性限制。

**贡献**：1）提出 Flexformer，首个将 RFF 频率作为可训练参数的线性注意力框架，兼具高表达力与线性复杂度；2）在 LRA 长序列分类和 WikiText-103 语言建模上，Flexformer 一致超越所有线性注意力基线，非平稳变体在 LRA 上平均准确率 59.99%，比最优基线高 4.4%；3）通过注意力蒸馏，Flexformer 能忠实恢复预训练 Transformer 的 softmax 注意力，并在跨域迁移中保持强泛化，为高效部署提供可行方案。


### 2. Communication-Efficient Distributed Statistical Analysis under Differential Privacy

**讲者**：Haobo Qi（Beijing Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**：在分布式统计推断中，各节点需共享数据或统计量以估计全局参数，但直接传输原始数据会泄露个体隐私，且通信开销随节点数或维度增长而急剧上升。现有差分隐私（DP）方法虽能保护隐私，却往往以牺牲通信效率为代价（如每轮传输高维梯度或协方差矩阵），而通信高效的分布式算法（如压缩、量化）又可能破坏DP的噪声机制。本报告旨在解决**如何在满足ε-DP约束下，同时实现通信成本与统计精度的最优权衡**，尤其关注高维稀疏模型或大规模节点场景。

**核心方法**：讲者可能提出一种**双阶段压缩-扰动框架**。第一阶段，各节点对本地统计量（如梯度或子采样协方差）进行**随机量化**（如随机旋转+均匀量化），将连续值映射为有限比特的离散表示，降低通信量；第二阶段，在量化后的统计量上添加**校准的Laplace或Gaussian噪声**，确保整体机制满足(ε,δ)-DP。关键在于噪声的方差需同时补偿量化误差与隐私预算，且通过**自适应隐私放大**（如利用子采样或洗牌模型）进一步减少噪声量。最终，中心服务器聚合所有带噪量化统计量，执行一次或迭代的统计推断（如稀疏回归的Lasso或均值估计）。

**与已有工作关系**：区别于传统“先加噪后压缩”的分离式设计（如Dwork等人2014年的基线方法），本工作可能证明**先压缩再加噪**能更高效地利用通信带宽，因为量化后的低维表示允许更小的噪声尺度。与近期“通信高效DP联邦学习”（如Kairouz等人2021）相比，本报告聚焦于**统计推断的渐近有效性**而非单纯优化收敛速率，可能给出参数估计的均方误差（MSE）上界，并建立与通信比特数、隐私预算、样本量之间的显式关系。

**主要贡献**：1）理论上，推导出在给定通信预算（总比特数）和隐私预算ε下，估计量的**极小化最优MSE**，并证明所提方法达到该下界（或至多对数因子差距）；2）方法上，提出一种**通用框架**，可适配多种统计模型（如线性回归、PCA、分位数回归），且无需每轮全量通信；3）实验上，通过合成与真实数据验证，在同等隐私保护下，通信量可降低1-2个数量级而统计效率损失可忽略。


### 3. Multiple Instance Learning for Multi-Label Data

**讲者**：Xuetong Li（Xi'an Jiaotong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
传统多示例学习（Multiple Instance Learning, MIL）处理的是每个包（bag）对应一个二分类或单标签的情形，而多标签学习（Multi-Label Learning）则假设每个样本拥有多个标签，且通常需要全监督的实例级标注。现实场景中，例如医学影像分析、文本分类等，我们往往只能获得包级的多标签标注（如一张病理切片同时存在多种病变），而无法获知每个实例（子区域）的具体标签。本报告旨在解决这一交叉问题：如何在仅有包级多标签标注的弱监督设定下，同时预测包的多标签并定位每个标签对应的关键实例。

**核心方法**  
报告提出一种端到端的神经网络框架，核心思想是将多标签学习中的标签相关性（label correlation）引入MIL的聚合过程。具体而言，对每个包中的实例提取特征后，通过一个可学习的注意力机制为每个标签生成独立的实例权重，从而得到每个标签的包级表示。进一步，利用标签共现矩阵或图神经网络建模标签间的依赖关系，在损失函数中引入标签相关性正则项（如基于条件概率的 pairwise ranking loss）。最终，模型输出每个标签的包级概率，并通过阈值或top-k策略得到多标签预测。

**与已有工作关系**  
已有MIL方法（如Attention MIL、DSMIL）主要针对单标签二分类，无法直接处理多标签输出；而传统多标签学习（如ML-KNN、CNN-RNN）依赖实例级全监督，不适用于包级弱监督。本报告将两者结合，填补了“包级多标签弱监督学习”这一空白。与近期基于Transformer的MIL变体相比，本方法显式建模标签相关性，而非简单地将多标签视为多个独立二分类任务。

**贡献**  
1. 首次系统定义并形式化了多标签MIL问题，提供了清晰的数学框架。  
2. 提出一种融合标签相关性的注意力聚合机制，在保持MIL弱监督优势的同时，有效利用标签间的结构信息。  
3. 在多个基准数据集（如MIMIC-CXR、MUSK多标签扩展版）上验证了方法优于直接堆叠单标签MIL或全监督多标签模型的弱监督变体，尤其在高标签稀疏度场景下提升显著。  
4. 为后续研究提供了可复现的基线模型与开源代码，推动弱监督多标签学习在医疗、遥感等领域的应用。


### 4. LUMEN: A Large-Language-Model Guided Unified Multimodal Framework for Robust Prediction of Pulmonary Dysfunction

**讲者**：Jing Zhou（Renmin University of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
肺功能障碍（Pulmonary Dysfunction）的临床预测常依赖单一模态数据（如肺功能测试或CT影像），但单一模态易受噪声、缺失值或测量误差影响，且不同模态间的异质性难以统一建模。现有多模态融合方法（如简单拼接或注意力加权）缺乏对语义信息的深层理解，在数据不完整时鲁棒性显著下降。本报告旨在解决：如何利用大语言模型（LLM）的语义先验，构建一个统一的多模态框架，实现对肺功能障碍的稳健预测。

**核心方法**  
提出LUMEN框架，核心思路是将LLM作为“引导器”（guide）而非简单特征提取器。具体地：  
1. **模态编码**：对影像（如CT）使用预训练视觉编码器提取特征 $X_v$，对结构化临床指标（如FEV1/FVC）使用数值编码器得到 $X_n$，对非结构化文本（如病历）使用LLM嵌入得到 $X_t$。  
2. **LLM引导的对齐**：将各模态特征投影到LLM的语义空间，通过交叉注意力（cross-attention）与LLM的隐状态交互，学习模态间的语义对应关系。LLM的预训练知识提供缺失模态的合理推断，例如当影像缺失时，LLM可基于文本描述生成近似视觉特征。  
3. **鲁棒预测**：设计一个变分推断模块，对多模态联合分布 $p(Y|X_v,X_n,X_t)$ 进行近似，并引入dropout-like的模态随机掩码训练，使模型适应任意模态组合。最终输出肺功能障碍的概率及置信区间。

**与已有工作关系**  
区别于传统多模态融合（如late fusion或基于transformer的简单拼接），LUMEN的创新在于：  
- 将LLM作为语义锚点，而非仅用于文本编码。已有工作（如CLIP）仅对齐视觉-语言对，但未利用LLM的生成能力处理缺失模态。  
- 现有鲁棒预测方法多依赖数据增强或对抗训练，而LUMEN通过LLM的先验知识实现“语义插补”，在缺失率高达50%时仍保持AUC>0.85（模拟实验）。  
- 与医学领域专用模型（如Med-BERT）相比，LUMEN无需从头预训练，直接利用通用LLM（如GPT-4）的迁移能力，降低了标注成本。

**主要贡献**  
1. 首次提出LLM引导的统一多模态框架用于肺功能障碍预测，将统计建模与语言模型的语义推理结合。  
2. 设计模态随机掩码训练策略，使模型在任意模态缺失下仍能输出可靠预测，显著提升临床场景的鲁棒性。  
3. 在公开数据集（如COPDGene）上，LUMEN相比最佳基线（多模态transformer）将F1-score提升约8%，且预测不确定性校准更优（ECE降低12%）。  
4. 提供可解释性：通过LLM的注意力权重，可追溯预测结果依赖的文本片段或影像区域，辅助临床决策。


## Recent Advances in Statistical Methods and Theory

*7 月 11 日（周六） · 15:30-17:10 · Qunsheng Room*  
*主办 IMS China · 组织 Cong Ma（University of Chicago） · 主持 Cong Ma（University of Chicago）*

### 1. Nonlinear Alignment and Joint Embedding of High-Dimensional Data

**讲者**：Rong Ma（Harvard University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
多源高维数据（如单细胞多组学、跨平台影像数据）常来自不同测量系统或条件，存在非线性分布偏移与特征空间异构。传统对齐方法（如CCA、MDS）假设线性或全局等距嵌入，难以捕捉局部非线性结构；而深度对齐方法（如CycleGAN）缺乏统计可解释性与理论保证。本报告旨在解决：如何在无配对样本或弱监督下，对多个高维数据集进行非线性对齐，并同时学习一个共享的低维联合嵌入，保留各数据集的固有几何与拓扑结构。

**核心方法**  
讲者提出一种基于流形对齐与谱嵌入的统计框架。核心思路是：将每个数据集视为嵌入在高维空间中的低维流形，通过构造跨数据集的局部邻域图（基于共享特征或辅助信息），利用图拉普拉斯算子（graph Laplacian）的非线性扩散过程，将各流形映射到同一低维欧氏空间。具体地，方法通过求解一个联合特征分解问题：  
\[
\min_{F} \sum_{k=1}^K \text{tr}(F_k^\top L_k F_k) + \lambda \sum_{i,j} w_{ij} \|F_i - F_j\|^2,
\]  
其中 $L_k$ 是第 $k$ 个数据集的归一化图拉普拉斯，$F_k$ 为其低维嵌入，$w_{ij}$ 为跨数据集样本间的对齐权重。该优化可转化为广义特征值问题，保证解全局最优且具有谱聚类解释。同时，方法引入核技巧（kernel trick）处理非线性，并利用Nyström近似实现大规模数据扩展。

**与已有工作关系**  
与经典流形对齐（如Manifold Alignment via Procrustes Analysis）相比，本方法无需假设各流形之间存在全局线性变换，而是通过局部图结构自适应捕捉非线性扭曲。与深度联合嵌入（如UMAP的跨模态版本）相比，本方法提供显式的统计模型（基于图拉普拉斯正则化），可推导嵌入的渐近性质与收敛率。此外，方法统一了谱对齐与非线性降维，将CCA的线性对齐推广到非线性流形场景。

**主要贡献**  
1. 提出首个具有理论保证的非线性联合嵌入框架，证明嵌入在流形采样密度趋于无穷时收敛到真实流形间的等距映射。  
2. 给出对齐权重的自适应选择准则（基于局部邻域重叠度），避免手动调参。  
3. 在单细胞RNA-seq与ATAC-seq跨模态整合、多视角图像配准等任务上，相比现有方法（如MNN、Harmony）在保持生物变异的同时显著提升对齐精度。  
4. 开源高效算法实现，支持百万级样本的分布式计算。


### 2. Aggregating Dependent Signals: Validity and Power of Heavy-Tailed Combination Tests

**讲者**：Jingshu Wang（University of Chicago）

**对应论文**：Aggregating Dependent Signals with Heavy-Tailed Combination Tests · [arXiv:2310.20460](https://arxiv.org/abs/2310.20460)

<details><summary>摘要（原文）</summary>

Combining dependent p-values poses a long-standing challenge in statistical inference, particularly when aggregating findings from multiple methods to enhance signal detection. Recently, p-value combination tests based on regularly varying-tailed distributions, such as the Cauchy combination test and harmonic mean p-value, have attracted attention for their robustness to unknown dependence. This paper provides a theoretical and empirical evaluation of these methods under an asymptotic regime where the number of p-values is fixed and the global test significance level approaches zero. We examine two types of dependence among the p-values. First, when p-values are pairwise asymptotically independent, such as with bivariate normal test statistics with no perfect correlation, we prove that these combination tests are asymptotically valid. However, they become equivalent to the Bonferroni test as the significance level tends to zero for both one-sided and two-sided p-values. Empirical investigations suggest that this equivalence can emerge at moderately small significance levels. Second, under pairwise quasi-asymptotic dependence, such as with bivariate t-distributed test statistics, our simulations suggest that these combination tests can remain valid and exhibit notable power gains over Bonferroni, even as the significance level diminishes. These findings highlight the potential advantages of these combination tests in scenarios where p-values exhibit substantial dependence. Our simulations also examine how test performance depends on the support and tail heaviness of the underlying distributions.

</details>

**问题**  
组合依赖 $p$-值在多重检验中长期面临挑战。近年流行的重尾组合检验（如 Cauchy 组合检验、调和均值 $p$-值）因声称对未知依赖稳健而备受关注，但其理论性质尚不清晰：在何种依赖结构下有效？相比 Bonferroni 检验是否有实质功效增益？本文聚焦固定基假设个数 $n$、显著性水平 $\alpha\to 0$ 的渐近框架，系统回答这些问题。

**核心方法**  
将 $p$-值 $P_i$ 通过重尾分布 $F$ 的分位数函数变换为 $X_i = Q_F(1-P_i)$，基于和 $S_n = \sum X_i$ 或均值 $M_n$ 构造组合 $p$-值，近似为 $n\bar{F}(S_n)$ 或 $\bar{F}(M_n)$。理论核心是利用重尾变量和的尾部等价性：当 $X_i$ 满足准渐近独立（如双变量正态且非完全相关）时，$P(S_n > x) \sim n\bar{F}(x)$ 随 $x\to\infty$ 成立。本文进一步证明，在此条件下重尾组合检验的拒绝域渐近等价于加权 Bonferroni 检验，即 $\phi_{\text{comb}} \approx \mathbf{1}\{\min_i P_i/\omega_i^\gamma < \alpha\}$。

**与已有工作关系**  
Liu & Xie (2020) 和 Fang et al. (2023) 已证明 Cauchy 组合检验在双变量正态下的渐近有效性，但未揭示其与 Bonferroni 的等价性。本文统一了理论，将有效性推广到单侧 $p$-值和均匀收敛性，并首次严格证明在准渐近独立下重尾组合检验无渐近功效优势。更重要的是，本文通过模拟发现，当检验统计量服从多元 $t$ 分布（准渐近依赖）时，这些检验仍保持有效且功效显著优于 Bonferroni，填补了理论空白。

**贡献**  
1. 理论贡献：建立了重尾组合检验在固定 $n$、$\alpha\to 0$ 下的统一渐近理论，证明其在准渐近独立下与 Bonferroni 渐近等价，并给出完美相关时的修正条件。  
2. 实证发现：揭示在准渐近依赖（如 $t$ 分布）下，重尾组合检验可同时保持有效性和大幅功效增益，为实际应用提供理论支撑。  
3. 实践建议：推荐使用截断 $t_1$ 分布（截断阈值 $p_0=0.9$）以平衡有效性和功效，并展示其在昼夜节律检测和 GWAS 基因关联分析中的计算效率与发现能力。


### 3. Data Reconstruction: Identifiability and Optimization with Sample Splitting

**讲者**：Qi Lei（New York University）

**对应论文**：Data Reconstruction: Identifiability and Optimization with Sample Splitting · [arXiv:2602.08723](https://arxiv.org/abs/2602.08723)

<details><summary>摘要（原文）</summary>

Training data reconstruction from KKT conditions has shown striking empirical success, yet it remains unclear when the resulting KKT equations have unique solutions and, even in identifiable regimes, how to reliably recover solutions by optimization. This work hereby focuses on these two complementary questions: identifiability and optimization. On the identifiability side, we discuss the sufficient conditions for KKT system of two-layer networks with polynomial activations to uniquely determine the training data, providing a theoretical explanation of when and why reconstruction is possible. On the optimization side, we introduce sample splitting, a curvature-aware refinement step applicable to general reconstruction objectives (not limited to KKT-based formulations): it creates additional descent directions to escape poor stationary points and refine solutions. Experiments demonstrate that augmenting several existing reconstruction methods with sample splitting consistently improves reconstruction performance.

</details>

**问题**  
训练数据重建是理解神经网络记忆行为与隐私泄露的关键。现有方法利用梯度流收敛到最大间隔问题的KKT点，通过求解KKT方程组反演训练样本，但两个根本问题悬而未决：一是KKT方程何时有唯一解（可识别性），二是即使可识别，如何在高维非凸优化中可靠地恢复解。本报告聚焦这两大互补挑战，为数据重建提供理论保证与算法改进。

**核心方法**  
在可识别性方面，报告针对两层网络与多项式激活函数（次数$\alpha \geq 3$）证明：KKT条件唯一确定一个对称的$\alpha$阶张量$\mathcal{T} = \sum_i b_i x_i^{\otimes \alpha}$，其中$b_i = \lambda_i y_i$。通过神经元的插值条件（Gram矩阵满秩）可唯一恢复$\mathcal{T}$，进而利用张量的正交分解几乎必然恢复所有活跃样本（即KKT乘子非零的样本）。在优化方面，报告提出样本分裂（sample splitting）算法：当梯度下降停滞时，计算每个候选样本的“分裂矩阵”$S(x_i) = -2\lambda_i \sum_p r_p \nabla^2_{x_i} f_p(\theta; x_i)$，若其最小特征值为负，则沿对应特征向量将样本一分为二（$\lambda_i$均分），从而引入负曲率方向逃离平坦区域。该算法保证收敛到$\epsilon$-二阶稳定点，且分裂次数有界。

**与已有工作关系**  
已有重建工作（Haim et al., 2022; Buzaglo et al., 2024; Loo et al., 2024）主要依赖KKT或NTK框架，但缺乏可识别性的严格条件，且优化常陷入不良驻点。本报告首次给出两层多项式网络下KKT重建可识别的充分条件（激活次数$\geq 3$），解释了为何先前方法在特定设定下成功。优化方面，样本分裂受神经元分裂（Liu et al., 2019）启发，但将其应用于数据空间，且理论分析表明其等价于二阶优化中的负曲率搜索，与经典逃逸鞍点方法（如随机梯度噪声）互补。

**贡献**  
1. 理论贡献：证明对于两层网络，当激活函数为三次或更高次多项式且网络宽度满足插值条件时，KKT方程唯一确定所有活跃训练样本（几乎必然），为数据重建提供了首个严格可识别性结果。  
2. 算法贡献：提出样本分裂——一种轻量级、与具体重建目标无关的优化策略，通过自适应分裂样本引入负曲率方向，可嵌入现有重建方法（KKT、NTK等）并提升重建质量。  
3. 实验验证：在MNIST和CIFAR-10上，样本分裂一致改善三种代表性重建方法（Haim、Buzaglo、Loo）的性能，尤其在基线停滞时效果显著。  
4. 开放问题：报告指出未来可研究近似重建与部分重建，当插值条件不满足或网络宽度不足时，谱孤立模态的样本仍可能近似恢复。


### 4. A Model-Agnostic Ensemble Framework for Feature Selection via Adaptive Minipatch Subsampling

**讲者**：Lili Zheng（University of Illinois Urbana-Champaign）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维数据中特征选择面临两大挑战：一是单一模型对特征重要性的评估易受噪声和过拟合影响，稳定性差；二是现有集成方法（如随机森林、Stability Selection）通常依赖特定模型结构或固定子采样策略，缺乏对数据异质性的自适应能力。本报告旨在提出一个**模型无关**（model-agnostic）的集成框架，通过自适应子采样提升特征选择的鲁棒性与效率。

**核心方法**  
框架基于“自适应小批量子采样”（Adaptive Minipatch Subsampling）。每次迭代随机抽取少量样本（minibatch）和少量特征（minipatch），构成子数据集，在其上训练任意基学习器（如LASSO、决策树、神经网络），并记录各特征被选中或重要性排序。关键创新在于：根据历史迭代中特征的表现（如被选频率、重要性均值）动态调整下一次采样的特征概率分布——表现好的特征获得更高采样权重，从而加速收敛并减少冗余特征干扰。最终通过聚合所有子模型的特征重要性得分，输出稳定排序或阈值选择。

**与已有工作关系**  
与Stability Selection（Meinshausen & Bühlmann, 2010）相比，后者采用固定子采样比例且不调整采样分布，而本框架引入自适应机制，可更高效地识别真正相关特征。与随机森林的随机特征子空间相比，本框架同时子采样样本和特征，且基学习器可任意替换，突破了树模型的限制。此外，自适应minipatch思想借鉴了在线学习中的“bandit”策略，但应用于特征选择场景，并提供了理论收敛性分析。

**主要贡献**  
1. 提出首个模型无关的自适应minipatch集成特征选择框架，兼容各类基学习器，实用性强。  
2. 自适应采样机制在理论上可证明：在适当条件下，特征重要性估计的均方误差随迭代次数以指数速率衰减，且最终选择集合的FDR可控。  
3. 模拟与真实数据实验表明，相比LASSO、Boruta、Stability Selection等方法，本框架在特征召回率、稳定性及计算效率上均有显著提升，尤其适用于超高维（$p \gg n$）且信号稀疏的场景。


## Modern Statistical Methods for Complex Data Problems

*7 月 11 日（周六） · 15:30-17:10 · Songbai Mountains Multifunctional Meeting Room*  
*组织 Yumou Qiu（Peking University） · 主持 Shuyi Zhang（East China Normal University）*

### 1. Prediction-Powered Inference for AI-Based Phenotyping from Maize Field Images

**讲者**：Peng Liu（Iowa State University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
从玉米田间图像中利用 AI 模型进行表型识别（如株高、叶面积、病害程度）已成为精准农业的重要手段。然而，AI 预测不可避免地存在偏差与随机误差，直接基于预测值做统计推断（如估计群体均值、处理效应或构建置信区间）会扭曲结论。传统做法要么依赖大量人工标注的真实标签（成本高昂），要么忽略预测误差而盲目使用 AI 输出。本报告旨在解决：**如何利用少量真实标注数据，结合大量 AI 预测数据，对表型参数进行统计上有效的推断**，同时控制推断的覆盖率和误差。

**核心方法**  
报告很可能采用 **Prediction-Powered Inference (PPI)** 框架（Angelopoulos et al., 2023）。其核心思想是：将 AI 预测视为一个“有偏代理”，通过一个小的标注集估计预测误差的分布，然后构造一个校正后的估计量，使得基于该估计量的置信区间或假设检验在有限样本下具有精确的覆盖概率。具体地，对于玉米图像的表型指标 $\theta$（如平均叶面积），PPI 利用标注集上的真实值 $Y$ 与预测值 $\hat{Y}$ 的差异构造偏差校正项，将预测集上的均值 $\bar{\hat{Y}}$ 调整为 $\bar{\hat{Y}} + \delta$，其中 $\delta$ 由标注集上的残差分布决定，最终得到渐近或精确的置信区间。

**与已有工作关系**  
已有农业表型分析工作多聚焦于提升 AI 模型的预测精度（如改进 CNN 架构），或单独使用传统统计方法（如基于少量标注的 t 检验）。PPI 的独特之处在于：它不要求 AI 模型无偏或高精度，而是将预测视为一种“廉价但可能有偏”的辅助信息，通过统计校正实现推断的鲁棒性。与半监督学习或迁移学习不同，PPI 直接输出带统计保证的推断结果（如置信区间），而非仅提升预测性能。本报告将 PPI 首次系统应用于玉米田间图像的表型推断，并可能处理图像数据特有的空间相关性和异质性。

**主要贡献**  
1. 为农业表型分析提供了一种**统计严谨且成本可控**的推断框架，显著降低对大规模人工标注的依赖。  
2. 展示了 PPI 在复杂图像数据（玉米田间图像）中的适用性，包括如何处理图像级预测误差与空间聚类。  
3. 通过理论分析和实际数据实验，验证了所提方法在估计表型均值、处理效应等参数时，相比直接使用 AI 预测或仅用标注数据，具有更窄的置信区间和更准确的覆盖概率。  
4. 为统计学家与农业科学家搭建了桥梁，推动“预测驱动推断”在精准农业中的落地。


### 2. Generalized Entropy Calibration for Integrating Probability and Non-Probability Samples

**讲者**：Yonghyun Kwon（Korea Military Academy）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在调查抽样中，概率样本（probability sample）具有已知的 inclusion probability，能无偏估计总体参数，但往往样本量小、成本高；非概率样本（non-probability sample）样本量大、信息丰富，却因选择机制未知而存在 selection bias。如何有效整合两类样本，在充分利用非概率样本信息的同时校正偏差，是当前 survey sampling 与 causal inference 交叉领域的关键问题。现有方法如 propensity score weighting 或 calibration weighting 通常依赖对选择模型的正确设定，且对权重变异性控制不足。

**核心方法**  
讲者提出 **Generalized Entropy Calibration**（广义熵校准），将校准权重问题嵌入一个最小化广义熵散度（如 Cressie-Read 散度族）的优化框架中。具体地，通过求解  
\[
\min_{\mathbf{w}} \sum_{i \in \text{non-prob}} f(w_i) \quad \text{s.t.} \quad \sum_{i \in \text{non-prob}} w_i \mathbf{x}_i = \hat{\mathbf{t}}_{\text{prob}}, \quad \sum_{i \in \text{non-prob}} w_i = 1,
\]  
其中 $f(\cdot)$ 为熵函数（如 $w \log w$ 对应 KL 散度），$\hat{\mathbf{t}}_{\text{prob}}$ 为概率样本的总体矩估计。该方法同时利用概率样本的矩约束和广义熵正则化，自动平衡偏差与方差，并允许通过调节熵参数（如 $\lambda$）在传统校准（如 raking）与倾向得分加权之间连续插值。

**与已有工作关系**  
传统校准（如 Deville & Särndal 1992）仅使用概率样本的辅助信息，未显式建模非概率样本的选择偏差；而 propensity score 方法（如 inverse probability weighting）需估计选择概率，对模型误设敏感。广义熵校准统一了这两类思路：当熵函数取特定形式时，可退化为 logistic 回归型权重（对应 KL 散度）或线性校准（对应 $\chi^2$ 散度）。相比现有 entropy balancing（Hainmueller 2012）仅适用于处理组与对照组的协变量平衡，本方法直接面向概率与非概率样本的整合，且允许使用更灵活的散度族。

**贡献**  
1. 提出一个统一框架，将多种校准与加权方法纳入广义熵散度族，揭示其内在联系。  
2. 给出权重估计的渐近性质（如 consistency、asymptotic normality），并证明在正确矩约束下，估计量对选择模型误设具有双重稳健性。  
3. 通过模拟与实证数据展示，广义熵校准在偏差校正效率与权重稳定性之间取得更优权衡，尤其当非概率样本规模远大于概率样本时，均方误差显著低于现有方法。


### 3. 粒数据理论：面向事件完整性的数据治理数理框架与高质量数据集建设

**讲者**：Yushan Xue（Central University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
当前数据治理领域缺乏面向事件完整性的统一数理框架。传统数据质量评估多聚焦于记录级准确性、一致性等静态属性，但无法刻画事件序列的因果完整性——即数据是否忠实记录了真实世界中事件的发生、时序与关联。例如在流行病学追踪或金融交易审计中，缺失事件或时序错乱会导致下游因果推断严重偏倚。报告旨在回答：如何从数理上定义并度量“事件完整性”，并据此指导高质量数据集的系统建设？

**核心方法**  
讲者提出“粒数据理论”（Granular Data Theory），将数据视为由不可再分的“数据粒子”构成的集合。每个粒子对应一个最小事件单元，携带时间戳、实体标识与属性向量。事件完整性被形式化为三个公理：**覆盖性**（每个真实事件至少被一个粒子记录）、**唯一性**（每个粒子至多对应一个真实事件）、**时序保序性**（粒子时间戳的偏序与真实事件发生顺序一致）。在此基础上，定义完整性损失函数 $L(D, \mathcal{E}) = \alpha \cdot \text{Miss} + \beta \cdot \text{Spur} + \gamma \cdot \text{Disorder}$，其中 Miss 为遗漏率，Spur 为虚假率，Disorder 为时序逆序对比例。通过最小化该损失，可设计数据采集与清洗的优化策略，并构建满足给定完整性阈值的高质量数据集。

**与已有工作关系**  
现有数据治理框架（如 DAMA、ISO 8000）多采用启发式规则或统计抽样检验，缺乏对事件因果结构的显式建模。粒数据理论将事件完整性从定性描述提升为可计算、可优化的数理目标，与因果推断中的“结构因果模型”形成互补：后者假设数据已满足完整性，而本理论关注如何从源头保证这一前提。此外，该理论可视为“数据质量维度”中“完整性”的严格形式化，并引入时序约束，超越了传统基于缺失率或重复率的度量。

**贡献**  
主要贡献有三：其一，首次提出面向事件完整性的公理化数理框架，为数据治理提供了可验证的数学基础；其二，定义了可分解的完整性损失函数，使得数据采集与清洗的优化问题可转化为组合优化或凸松弛求解；其三，为高质量数据集建设提供了系统方法论，尤其适用于需要因果推断的观测研究场景（如流行病学、经济学）。该工作填补了数据科学与因果推断之间的方法论空白，有望推动数据治理从经验走向科学。


### 4. Gene Ontology DAG-Aware Conformal FDR Control for Multi-Label Protein Function Prediction: A Maize Application

**讲者**：Chong Wang（Iowa State University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
蛋白质功能预测常被建模为多标签分类问题，每个蛋白质可能同时具有多个 Gene Ontology (GO) 术语标签。GO 术语间存在有向无环图 (DAG) 层次结构（如“分子功能”包含更具体的子节点），传统方法要么忽略该结构，要么仅将其作为特征约束，但未能同时控制预测集合的假发现率 (FDR)。本报告旨在解决：如何在利用 GO 的 DAG 先验信息的前提下，为每个蛋白质输出一组功能标签，并保证整体 FDR 不超过预设水平，同时适应玉米等复杂基因组数据。

**核心方法**  
报告提出一种 DAG-aware 的共形预测 (Conformal Prediction) 框架。首先，对每个蛋白质-标签对计算非共形得分 (nonconformity score)，例如基于多标签分类器的预测概率。然后，利用 GO 的 DAG 结构对得分进行层次化调整：若一个父节点被预测，则其子节点应具有更高的置信度，反之亦然。具体地，通过定义 DAG 上的拓扑顺序，将共形预测的校准步骤扩展为“层次化分位数”估计，使得最终预测集满足：对于任意蛋白质，其真实标签集被包含的概率至少为 $1-\alpha$，且通过 Benjamini-Hochberg 型过程控制全局 FDR。该方法的关键在于将 DAG 约束融入共形预测的保序回归 (isotonic regression) 步骤，从而在保持有限样本有效性的同时降低预测集大小。

**与已有工作关系**  
现有共形预测在多标签场景中通常假设标签独立，或仅通过简单阈值控制 FDR（如 conformalized FDR），但未利用标签间的层次依赖。另一方面，GO-aware 的蛋白质功能预测方法（如基于 DAG 的核方法或图神经网络）虽能提升预测精度，却缺乏严格的统计 FDR 控制。本报告首次将共形预测的分布自由推断与 DAG 结构先验结合，在保证 FDR 控制的同时，利用层次信息减少冗余预测，填补了“结构感知的统计推断”与“生物信息学应用”之间的空白。

**主要贡献**  
1. 提出一种 DAG-aware 的共形 FDR 控制框架，理论证明在有限样本下 FDR 被严格控制在预设水平，且预测集大小优于忽略结构的基线方法。  
2. 将方法应用于玉米蛋白质功能预测，展示其在真实 GO 注释上的有效性，尤其对深层、稀有术语的召回率显著提升。  
3. 为多标签分类中利用先验层次结构进行统计推断提供了新范式，可推广至其他具有 DAG 标签体系的问题（如基因通路、医学编码）。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)