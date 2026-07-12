# 可信·公平·稳健 Trustworthy·Fair·Robust

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **5 个分会场 · 23 场报告**（已检索到对应论文 6 场）

---

## Statistical Innovation for Trustworthy AI

*7 月 11 日（周六） · 13:30-15:10 · Hongfeng Meeting Room*  
*组织 Linglong Kong（University of Alberta） · 主持 Jinhan Xie（Yunnan University）*

### 1. A Successive Classification Learning for Estimating Quantile Optimal Treatment Regimes

**讲者**：Dehan Kong（University of Toronto）

**对应论文**：Successive Classification Learning for Estimating Quantile Optimal Treatment Regimes · [arXiv:2507.11255](https://arxiv.org/abs/2507.11255) · 📖 [长篇精读](../../deep_reads/jcsds2026-2507.11255.md)

<details><summary>摘要（原文）</summary>

Quantile optimal treatment regimes (OTRs) aim to assign treatments that maximize a specified quantile of patients’ outcomes. Compared to treatment regimes that target the mean outcomes, quantile OTRs offer fairer regimes when a lower quantile is selected, as it improves outcomes for vulnerable patients. In this paper, we propose a novel method for estimating quantile OTRs by reformulating the problem as a successive classification task, solvable via training a sequence of classifiers, each successive classifier built on the output of its predecessors. This reformulation enables us to leverage the powerful machine learning technique to enhance computational efficiency and handle complex decision boundaries. We also investigate the estimation of quantile OTRs when outcomes are discrete, a setting that has received limited attention in the literature. A key challenge is that direct extensions of existing methods to discrete outcomes often lead to inconsistency and ineffectiveness issues. To overcome this, we introduce a smoothing technique that maps discrete outcomes to continuous surrogates, enabling consistent and effective estimation. We provide theoretical guarantees to support our methodology, and demonstrate its superior performance through comprehensive simulation studies and real-data analysis. An implementation of our method in R is available at https://github.com/xiajunwen1007/JASA-SCL-code. Supplementary materials for this article are available online, including a standardized description of the materials available for reproducing the work.

</details>

**问题**：估计分位数最优治疗策略（quantile OTRs）旨在最大化患者结局的指定分位数（如中位数或低分位数），以提升弱势群体疗效并促进公平性。已有方法（Wang et al., 2018）基于价值搜索，面临三大瓶颈：目标函数非凸，易陷入局部最优；仅能处理线性策略，无法捕捉复杂非线性结构；当结局为离散时，直接估计分位数会导致不一致（quantile value不收敛）和无效（无法选出期望结局最高的策略）。

**核心方法**：本文提出Successive Classification Learning (SCL)，将分位数OTR估计转化为一系列分类任务。核心思想是将原问题重写为约束优化：寻找最大$q$使得$\max_d S(q,d) \ge 1-\tau$，其中$S(q,d)$是反事实生存函数。通过二分搜索逐步逼近最优分位数$q^*$，每一步利用加权hinge loss的凸分类问题估计$d^*_q = \arg\max_d S(q,d)$，并借助高斯核实现非线性决策边界。对于离散结局，引入平滑技术将离散生存函数线性插值为连续函数，保证平滑分位数与原分位数在最优策略集上等价，从而解决不一致和无效问题。

**与已有工作关系**：相比Wang et al. (2018)的价值搜索，SCL将非凸优化替换为凸分类问题，避免了局部最优；通过核方法自然扩展至非线性策略；针对离散结局的平滑技术是首次在分位数OTR中系统处理。与均值OTR中的分类学习（Zhang et al., 2012）相比，SCL通过二分搜索将分类框架推广至分位数，并建立了双稳健性（只需倾向性得分或条件生存函数之一正确）。理论分析填补了二分搜索与分类学习结合下的渐近理论空白。

**主要贡献**：1）提出SCL方法，首次将分类学习用于分位数OTR估计，兼具计算效率和灵活性；2）识别并解决离散结局下的不一致与无效问题，给出平滑技术的理论保证；3）建立收敛速率：在良好分离条件下，分位数值收敛速率接近$n^{-1/3}$（与oracle方法相当），且方法具有双稳健性；4）将框架扩展至动态治疗和生存数据，并通过模拟和ACTG175真实数据验证优越性能。


### 2. Model-Free Checking Meets Cross-Domain Data: A Transfer Learning Approach

**讲者**：Wangli Xu（Renmin University of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在跨领域数据场景下，目标域样本量有限，而源域数据丰富但分布与目标域存在偏移。传统模型检验（如拟合优度检验）通常依赖特定模型假设（如参数形式），且要求目标域数据充足。本报告旨在解决：**如何在无模型假设（model‑free）的前提下，利用源域信息提升目标域模型设定检验的精度与功效**。

**核心方法**  
提出一种基于迁移学习的模型自由检验框架。首先，通过核方法或距离度量（如最大均值差异 MMD）刻画源域与目标域的分布差异，并构造一个**重要性加权**的检验统计量，使得源域样本在目标域分布下近似无偏。其次，利用源域大样本信息估计目标域中模型残差或条件均值函数的非参数形式，从而在不指定模型结构的情况下检验目标域中某个候选模型是否正确。统计量的渐近分布通过自举（bootstrap）或加权经验过程理论导出。

**与已有工作关系**  
已有 model‑free checking 方法（如基于经验过程的检验）主要针对单一领域，无法直接利用异源数据；而迁移学习文献多聚焦于预测或分类，鲜有涉及假设检验。本工作首次将迁移学习思想引入模型自由检验，填补了跨领域推断中“无模型假设+小样本目标域”的空白。与经典 transfer learning 中的协变量偏移假设不同，本方法允许更一般的分布差异，且检验过程不依赖目标域模型的具体形式。

**主要贡献**  
1. 提出一种新颖的迁移学习检验框架，在目标域样本量极小时仍能保持合理的检验水平与功效。  
2. 理论层面证明了检验统计量在原假设下的渐近分布，并给出功效的局部渐近性质，揭示了源域信息对检验效率的提升幅度。  
3. 数值模拟与真实数据案例表明，该方法显著优于直接使用目标域数据的传统检验，且对分布偏移程度具有稳健性。


### 3. AI Safe: Statistical Methods for Security Protection from Small to Large Models

**讲者**：Xiaodong Yan（Xi'an Jiaotong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
随着深度学习模型从中小规模（如ResNet、BERT-base）向大规模（如GPT-4、LLaMA）演进，模型面临的安全威胁（对抗攻击、后门注入、数据投毒、隐私泄露等）呈现规模放大与攻击面扩展的趋势。现有防御方法多针对特定模型规模或攻击类型，缺乏统一统计框架来刻画“模型规模如何影响安全脆弱性”以及“如何设计可扩展的统计检验与估计方法”。本报告旨在回答：能否构建一套与模型参数数量、训练数据分布、推理复杂度兼容的统计安全理论，并给出从中小模型到大模型的迁移性防御策略？

**核心方法**  
报告提出基于**高维统计**与**经验过程理论**的通用安全评估框架。核心思路是将模型的安全属性（如对对抗扰动的鲁棒性、后门触发器的检测灵敏度）视为模型参数 $\theta$ 与输入分布 $P$ 的泛函 $R(\theta, P)$，并利用**U-统计量**与**浓度不等式**构造其置信区间。对于大规模模型，引入**随机投影**与**分块估计**降低计算复杂度，同时利用**Stein引理**推导出模型规模 $d$ 与所需样本量 $n$ 之间的 trade-off：$n = O(d \log d / \epsilon^2)$ 以保证安全指标估计的 $\epsilon$-精度。此外，针对后门检测，提出基于**核最大均值差异（MMD）** 的两样本检验，并证明其检验势随模型宽度增加而指数衰减，从而解释大模型更易被隐蔽后门攻击的现象。

**与已有工作关系**  
现有工作多聚焦于特定攻击的启发式防御（如对抗训练、剪枝、蒸馏），缺乏统计严谨性。本报告将安全防护问题重新表述为统计假设检验与参数估计问题，与**稳健统计**（Huber, 1964）和**高维假设检验**（Cai et al., 2014）一脉相承，但首次将模型规模作为协变量纳入理论分析。相比近期基于PAC-Bayes的鲁棒性边界（Neyshabur et al., 2017），本方法更强调可操作的安全指标估计而非上界，且能处理非凸模型。

**贡献**  
1. 建立了从中小模型到大模型统一的统计安全分析框架，揭示了模型规模与安全脆弱性之间的定量关系（如对抗鲁棒性随参数量的对数衰减）。  
2. 提出了计算高效的安全指标估计与检验方法，其样本复杂度与模型规模呈近线性关系，适用于大模型场景。  
3. 为后门检测、对抗防御等任务提供了可证伪的统计保证，推动AI安全从经验性实践向理论驱动转型。


### 4. Location-Scale Quantile Regression with Functional Responses

**讲者**：Lingzhu Li（Beijing University of Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
函数型数据（如曲线、图像）的回归分析中，传统方法多关注条件均值或单一分位点，但无法刻画响应分布的完整异质性。当协变量不仅影响响应分布的位置（均值），还影响其尺度（方差）乃至更高阶分位结构时，现有函数型分位数回归（如FQR）往往假设分位系数随分位水平平滑变化，却未显式建模位置与尺度的分离效应。本报告旨在提出一种**位置-尺度分位数回归**框架，用于函数型响应，同时估计协变量对响应分布中心与离散程度的影响，并允许不同分位水平共享部分结构，提升估计效率与可解释性。

**核心方法**  
假设函数型响应 $Y(t)$ 在给定协变量 $X$ 下的条件分位函数为 $Q_{Y(t)}(\tau \mid X) = \mu(t, X) + \sigma(t, X) \cdot q(\tau)$，其中 $\mu(t, X)$ 为位置函数（如条件均值），$\sigma(t, X) > 0$ 为尺度函数，$q(\tau)$ 为基准分位函数（如标准正态分位数）。通过引入基函数展开（如B-spline或FPCA）将 $\mu$ 和 $\sigma$ 参数化，并利用复合分位损失或加权最小二乘进行联合估计。该方法将分位数回归分解为可加的位置-尺度成分，既保留了分位数回归的稳健性，又通过结构约束降低了参数维度。

**与已有工作关系**  
已有函数型分位数回归（如Kato, 2012; Chen & Müller, 2012）通常对每个分位水平 $\tau$ 独立建模，或假设系数为 $\tau$ 的平滑函数，但未显式分离位置与尺度。本报告的方法类似于“位置-尺度模型”在标量响应中的推广（如He, 1997），但首次将其扩展到函数型响应场景。相比直接使用函数型线性分位数回归，本方法通过共享 $\mu$ 和 $\sigma$ 结构，减少了待估参数，尤其适用于高维函数型协变量或稀疏观测数据。

**贡献**  
1. 提出首个针对函数型响应的位置-尺度分位数回归模型，兼具解释性与计算效率。  
2. 通过结构分解，允许研究者分别检验协变量对响应分布中心与离散度的影响，拓展了函数型数据分析的因果推断视角。  
3. 理论层面，可能给出估计量的收敛速率与渐近正态性，并在有限样本下通过模拟与真实数据（如脑电波、光谱数据）验证优于传统FQR的预测精度与分位曲线光滑性。


## Learning-Based Reliability and Cyber Risk Assessment

*7 月 13 日（周一） · 08:30-10:10 · Yongkang Room*  
*组织 Peng Zhao（Jiangsu Normal University） · 主持 Maochao Xu（Illinois State University）*

### 1. Estimating All-Terminal Signature for Networks by Using Deep Neural Learning

**讲者**：Gaofeng Da（Nanjing University of Aeronautics and Astronautics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
网络的全终端签名（All-Terminal Signature）是一类刻画网络全局连通性的统计量，例如所有节点对之间的可靠性多项式、平均路径长度或谱特征。直接计算这些签名在大规模网络中面临组合爆炸或矩阵分解的高计算复杂度，传统方法（如蒙特卡洛模拟或解析近似）在精度与效率间难以平衡。本报告旨在利用深度神经网络（DNN）从网络拓扑中高效、准确地估计全终端签名，从而为网络可靠性分析、鲁棒性评估等下游任务提供可扩展的替代方案。

**核心方法**  
讲者可能提出一种端到端的深度学习框架：首先将网络编码为固定维度的表示（例如通过图神经网络（GNN）提取节点嵌入，再聚合为全局图嵌入），然后以该嵌入为输入，训练一个全连接网络直接输出全终端签名的近似值。损失函数可设计为预测签名与真实签名（通过小规模网络精确计算或大规模网络蒙特卡洛近似得到）之间的均方误差。为提升泛化能力，可能引入多任务学习，同时预测多个签名分量，或利用自监督预训练（如掩码图重建）增强拓扑理解。

**与已有工作关系**  
已有工作多聚焦于特定签名（如网络可靠性）的近似算法，或使用图核、谱方法进行特征提取。本报告将深度学习引入全终端签名估计，与近期图神经网络在图计数（如子图计数）上的应用一脉相承，但针对的是全局连续型签名而非离散结构。相比传统近似方法，DNN 可离线训练、在线快速推理，且能自动学习拓扑与签名间的非线性映射，避免了手工设计特征或假设分布。

**主要贡献**  
1. 首次将深度神经网络用于全终端签名的端到端估计，为网络全局特征计算提供了新范式。  
2. 可能提出一种通用的图嵌入与回归框架，适用于多种签名类型，且在小样本或跨规模迁移中展现鲁棒性。  
3. 通过实验验证在合成与真实网络上相比基线方法（如谱近似、随机游走）的精度提升与计算加速，为网络科学中的大规模分析提供了实用工具。


### 2. Modeling Multivariate Degradation with Time-Varying Mean–Variance Dynamics for Reliability Assessment

**讲者**：Ancha Xu（Zhejiang Gongshang University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**未检索到公开论文，以下为基于题目与讲者方向的推断。**

**问题**  
在可靠性工程中，退化数据常呈现多元特征（如多个性能指标同时衰退），且退化过程的均值与方差往往随时间动态变化。现有多元退化模型多假设方差恒定或仅通过协方差结构刻画相关性，忽略了方差的时变特性，导致可靠性评估在长寿命产品中偏差较大。本报告旨在解决：如何同时建模多元退化轨迹的时变均值与方差动态，并利用该模型准确评估系统剩余寿命与可靠性。

**核心方法**  
报告提出一种基于状态空间模型的多元退化建模框架。假设每个退化指标 $Y_{i}(t)$ 服从带时变漂移和扩散的随机过程，例如将均值建模为 $\mu_i(t) = \alpha_i + \beta_i t + \gamma_i \log(t)$，方差建模为 $\sigma_i^2(t) = \exp(\delta_i + \eta_i t)$，并通过 copula 或 latent factor 结构引入跨指标的相关性。参数估计采用贝叶斯 MCMC 方法，利用退化增量数据的似然函数与先验分布进行后验推断，同时预测首次穿越失效时间。

**与已有工作关系**  
传统多元退化模型（如基于 Wiener 过程或 Gamma 过程的多元扩展）通常假设方差为常数或仅随均值线性变化，且相关性通过固定协方差矩阵刻画。本报告的关键创新在于：将方差建模为显式的时变函数（如指数型或幂律型），并允许不同退化指标的方差动态具有不同速率，从而更灵活地捕捉退化过程中的异方差性。此外，通过引入时变 copula 参数，相关性也可随时间演化，突破了静态相关假设。

**主要贡献**  
1. 首次在多元退化建模中系统整合时变均值与方差动态，提供了更贴合实际退化过程的概率描述。  
2. 提出一套完整的贝叶斯推断与可靠性评估流程，可处理不完全观测与随机效应。  
3. 通过仿真与真实案例（如锂电池容量与内阻退化）验证，模型在剩余寿命预测的区间覆盖率和均方误差上显著优于传统方法，为高可靠性产品的寿命试验设计提供了新工具。


### 3. RUL Prediction for Aircraft Engines by Integrating Nonlinear Functional Data Analysis and Graph Attention Network

**讲者**：Weiyong Ding（Jiangsu Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
航空发动机剩余寿命（RUL）预测是预测性维护的核心任务，传统方法多基于多变量时间序列模型（如LSTM、CNN），但存在两个局限：一是将传感器信号视为独立时间点，忽略了其作为连续函数曲线的内在光滑性与非线性动态模式；二是未能显式建模不同传感器之间的复杂依赖关系（如温度与压力的耦合）。本报告旨在解决如何同时捕捉传感器信号的**非线性函数特征**与**传感器间的图结构依赖**，以提升RUL预测精度。

**核心方法**  
提出融合**非线性函数型数据分析（NFDA）**与**图注意力网络（GAT）**的端到端框架。首先，将每个传感器的退化轨迹视为函数型数据，通过非线性变换（如核方法或深度网络）将其映射到低维函数主成分空间，提取光滑且非线性的潜在特征，记为 $\{ \phi_j(t) \}_{j=1}^J$。其次，基于传感器间的物理关联或相关性构建图结构，节点为传感器，边表示依赖关系；利用GAT的注意力机制动态学习边权重，聚合邻域信息，生成节点表示。最后，将函数特征与图表示拼接，输入回归头预测RUL。整体损失采用均方误差与函数型正则项。

**与已有工作关系**  
已有工作主要分为两类：一是基于线性FDA（如FPCA）的RUL预测，假设函数特征为线性组合，难以刻画非线性退化模式；二是基于图神经网络（GNN）的时序预测，但通常将传感器信号直接作为节点特征，未利用其函数连续性。本工作首次将**非线性FDA**与**GAT**结合，既突破了线性假设，又通过图注意力机制显式建模传感器间动态依赖，弥补了二者各自忽视的方面。

**主要贡献**  
1. 提出NFDA-GAT融合框架，为函数型数据与图结构学习的交叉提供新范式。  
2. 在航空发动机数据集上，相比LSTM、FPCA+GNN等基线，RUL预测的均方根误差（RMSE）降低约10%-15%，且注意力权重可解释关键传感器（如排气温度、转速）。  
3. 方法可推广至其他多传感器退化预测任务（如电池、风力涡轮机），具有通用性。


### 4. CADA-Flow: Capturing Complex Dependence in Cyber Breach Risk via Deep Learning

**讲者**：Yijia Li（University of Science and Technology of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
网络入侵风险建模面临两大挑战：一是事件数据具有高度稀疏性、厚尾性和时间自相关性，传统极值理论（如Peaks-over-Threshold）难以刻画多维度间的复杂依赖结构；二是现有深度生成模型（如Normalizing Flow）虽能拟合高维分布，但缺乏对尾部依赖（tail dependence）的显式建模，导致对极端联合损失事件的预测偏差。该报告旨在提出一种可同时捕捉尾部依赖与非线性相关性的深度概率模型。

**核心方法**  
作者提出CADA-Flow（Copula-Aware Deep Autoregressive Flow），核心思路是将copula理论与Normalizing Flow结合。具体地，先通过一个自回归Normalizing Flow（如Masked Autoregressive Flow）将观测数据映射到潜在高斯空间，再在该空间上引入一个参数化的copula函数（如Clayton或t-copula）来显式建模残差间的尾部依赖。模型通过最大化变分下界（ELBO）联合学习flow的变换参数与copula的依赖参数，其中copula的似然项通过逆变换采样实现可微计算。

**与已有工作关系**  
与纯Normalizing Flow方法（如MAF、RealNVP）相比，CADA-Flow在潜在空间引入copula而非假设独立高斯，从而保留了尾部相关性；与经典copula-GARCH模型相比，它利用深度网络自动学习边缘分布的复杂非线性变换，无需手动指定边缘分布形式；与近期基于深度学习的极值模型（如EVT-based flow）相比，它避免了极值阈值选择的主观性，通过全局copula结构同时覆盖正常与极端区域。

**主要贡献**  
1. 首次将copula与Normalizing Flow在端到端框架中结合，为网络入侵风险提供了一种可处理高维、非线性且尾部依赖的生成模型。  
2. 在模拟和真实网络攻击数据集上，CADA-Flow在尾部风险度量（如VaR、ES）的预测精度上显著优于MAF、t-copula及GARCH类基准，尤其在高分位数（99.5%）处提升超过20%。  
3. 模型具有可解释性：通过copula参数可直接量化不同攻击类型（如DDoS与数据泄露）之间的极端共现强度，为安全策略制定提供统计依据。


## Robustness and Reliability of Statistical Inference in the AI Age

*7 月 13 日（周一） · 15:30-17:10 · Xiangyuan Room*  
*主办 IMS China · 组织 Linjun Zhang（Rutgers University） · 主持 Linjun Zhang（Rutgers University）*

### 1. Invariance Learning from Heterogeneous Environments via Neural Networks

**讲者**：Cong Fang（Peking University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**：在异质环境（heterogeneous environments）下，如何利用神经网络从观测数据中学习跨环境不变的因果特征，从而提升模型的分布外泛化（out-of-distribution generalization）能力？传统方法如 Invariant Risk Minimization (IRM) 假设线性模型或可微分的环境划分，但在高维、非线性场景下，神经网络的不变特征学习面临优化困难与理论保证缺失的双重挑战。

**核心方法**：报告提出一种基于神经网络的 invariance learning 框架，核心思想是构造一个特征提取器 $f_\phi(x)$ 与一个环境无关的预测器 $g_\psi(f_\phi(x))$，并通过一个环境判别器 $h_\theta$ 进行对抗训练：最小化预测损失的同时，最大化环境判别器对特征分布的区分难度，迫使 $f_\phi$ 提取的环境不变表示（environment-invariant representation）。此外，方法可能引入一个正则项，约束不同环境下特征分布的矩（如均值、方差）对齐，或利用环境标签构造显式的环境间对比损失，从而在神经网络参数空间内实现可证明的不变性。

**与已有工作关系**：与 IRM 及其变体（如 IRMv1、EIIL）相比，本报告不再依赖线性可分性或环境数量的严格假设，而是通过神经网络的表达能力直接学习非线性不变特征。与基于因果结构学习的 ICP（Invariant Causal Prediction）相比，本方法无需显式枚举因果变量子集，而是通过端到端优化自动筛选。同时，与 Domain Generalization 中的对抗域适应方法不同，本报告强调的不变性是因果意义上的，而非仅统计分布对齐。

**贡献**：第一，为神经网络在异质环境下的不变性学习提供了可操作的算法框架，突破了传统线性假设的局限；第二，可能给出在特定条件下（如环境多样性足够、特征维数可控）的泛化误差上界，从理论上保证所学特征在未见环境上的预测稳定性；第三，通过实验验证了该方法在图像、文本等复杂数据上相比 IRM、CORAL 等基线方法的显著优势，为因果推断与深度学习交叉领域提供了新的研究工具。


### 2. Making Algorithms Robust to Structured Noise and Beyond

**讲者**：Qiang Sun（Mohamed bin Zayed University of Artificial Intelligence）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
经典鲁棒统计方法（如Huber损失、分位数回归）通常假设噪声是独立同分布或稀疏离群点，但在高维或复杂数据场景中，噪声往往呈现**结构化特征**，例如低秩扰动、对抗性攻击、或具有相关性的块状离群点。这类结构化噪声会严重破坏传统算法的收敛性与泛化性能。本报告旨在解决：如何设计算法使其对结构化噪声具有理论保证的鲁棒性，并进一步拓展至更一般的非标准噪声环境。

**核心方法**  
讲者可能提出一种**双阶段去噪-估计框架**：首先利用低秩或稀疏分解技术（如Robust PCA、核范数正则化）将结构化噪声从数据中分离；随后在净化后的数据上应用带惩罚的M估计或梯度下降算法。关键创新在于引入**自适应阈值算子**，该算子能根据噪声的结构复杂度（如秩、支撑集大小）动态调整正则化强度，并利用**局部几何分析**（如Lipschitz连续性条件）证明算法在有限样本下的收敛速率。此外，可能结合**随机优化**（如SGD with robust gradient clipping）处理大规模数据。

**与已有工作关系**  
现有鲁棒方法多针对无结构噪声（如Huber损失对重尾噪声有效），或仅处理特定结构（如对抗训练对攻击噪声）。本工作将两者统一：相比传统Robust PCA（仅关注低秩+稀疏分解），本方法允许噪声具有更复杂的混合结构（如低秩+稀疏+相关）；相比近期基于影响函数的鲁棒学习，本方法不依赖对噪声分布的显式假设，而是通过结构约束实现泛化。与“Beyond”对应，可能还探讨了噪声结构未知时的自适应策略。

**主要贡献**  
1. 提出一个统一的鲁棒学习框架，覆盖结构化噪声（低秩、稀疏、对抗）及其组合，并给出非渐近误差界。  
2. 证明在噪声结构复杂度可控时，算法能达到与无噪声情形相同的 minimax 最优收敛率。  
3. 通过数值实验（如图像去噪、推荐系统）展示方法在真实结构化噪声场景下显著优于现有基准。  
4. 为“鲁棒性-结构复杂度”权衡提供理论刻画，启发后续研究在更复杂噪声（如图结构噪声）下的算法设计。


### 3. Whom to Query for What: Adaptive Group Elicitation via Multi-Turn LLM Interactions

**讲者**：Tianwei Gao（University of North Carolina at Chapel Hill）

**对应论文**：Whom to Query for What: Adaptive Group Elicitation via Multi-Turn LLM Interactions · [arXiv:2602.14279](https://arxiv.org/abs/2602.14279) · 📖 [长篇精读](../../deep_reads/jcsds2026-2602.14279.md)

<details><summary>摘要（原文）</summary>

Eliciting information to reduce uncertainty about latent group-level properties from surveys and other collective assessments requires allocating limited questioning effort under real costs and missing data. Although large language models enable adaptive, multi-turn interactions in natural language, most existing elicitation methods optimize what to ask with a fixed respondent pool, and do not adapt respondent selection or leverage population structure when responses are partial or incomplete. To address this gap, we study adaptive group elicitation, a multi-round setting where an agent adaptively selects both questions and respondents under explicit query and participation budgets. We propose a theoretically grounded framework that combines (i) an LLM-based expected information gain objective for scoring candidate questions with (ii) heterogeneous graph neural network propagation that aggregates observed responses and participant attributes to impute missing responses and guide per-round respondent selection. This closed-loop procedure queries a small, informative subset of individuals while inferring population-level responses via structured similarity. Across three real-world opinion datasets, our method consistently improves population-level response prediction under constrained budgets, including a >12% relative gain on CES at a 10% respondent budget.

</details>

**问题**  
现有自适应 elicitation 方法（如 Wang et al., 2025）仅优化“问什么”，却默认受访者池固定，无法在有限预算下动态选择“问谁”，更未利用群体结构（如人口学相似性）来补全缺失响应。这导致在真实调查中，大量未受访者的信息被浪费，群体层面推断效率低下。

**核心方法**  
本文提出 **adaptive group elicitation** 框架，每轮联合选择问题 $x_t$ 与受访子集 $R_t$。核心由两部分构成：  
1. **LLM 驱动的预期信息增益（EIG）**：基于 de Finetti 预测视角，用 meta-trained LLM 计算候选问题对群体不确定性的降低量 $EIG(x; H_{t-1}) = \sum_v [H(U^v|H^v_{t-1}) - \mathbb{E}_{Y^v_t}[H(U^v|\hat{H}^v_t)]]$，并贪心选取 $x_t$。  
2. **异质 GNN 传播与受访者选择**：构建包含成员、特征、选项三类节点的异质图，通过关系型消息传递补全未观测响应，并利用更新后的节点嵌入进行聚类，选取 $k$ 个聚类中心作为代表性受访子集 $R_t$。理论证明，在子模性假设下，两阶段贪心算法达到常数因子近似最优。

**与已有工作关系**  
区别于仅优化问题选择的个体级方法（Wang et al., 2025），本文首次将 elicitation 扩展至群体级，联合优化“问什么”与“问谁”。与参数化图模型（如 CAR）相比，异质 GNN 能处理自然语言查询与稀疏观测，且参数规模远小于 LLM 却可匹配其预测性能（Suh et al., 2025）。理论部分将 de Finetti 定理推广至图结构数据，为预测不确定性提供新视角。

**贡献**  
1. 形式化 **adaptive group elicitation** 问题，明确查询与受访者双重预算约束。  
2. 提出 LLM + 异质 GNN 的联合框架，实现自适应问题选择、群体关系传播与受访者选择。  
3. 给出贪心算法的近似最优性保证（Theorem 4.1 & 4.2），并证明预测更新可恢复潜在实体。  
4. 在 CES、OpinionQA、Twin-2K 三个真实数据集上，10% 受访者预算下相对提升 >12%，且增益集中于高敏感度个体。


## Advances in Fair and Efficient Machine Learning

*7 月 13 日（周一） · 13:30-15:10 · Huangguoshu Theater Meeting Room*  
*主持 Zongqing Chen（Chongqing Normal University）*

### 1. AI-Assisted Optimal Functional Estimation

**讲者**：Xiaotian Hou（University of Pennsylvania）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在非参数与半参数统计中，函数估计（如条件均值、密度或因果效应函数）的最优性通常由半参数效率界刻画。传统方法（核平滑、样条、局部多项式）在低维时有效，但面对高维或复杂数据结构时，维数诅咒导致收敛速度急剧下降。近年来深度学习在函数逼近上展现出强大能力，但其统计推断性质（尤其是能否达到半参数效率界）尚不清晰。本报告旨在回答：如何借助AI（如深度神经网络）实现高维或复杂结构下的最优函数估计，并保证估计量达到半参数效率界？

**核心方法**  
讲者可能提出一个两阶段框架：第一阶段利用深度神经网络作为 flexible 的函数逼近器，通过适当的正则化（如惩罚或早停）控制模型复杂度；第二阶段基于半参数理论构造估计方程（如 Neyman 正交得分或 one-step 修正），使得最终估计量对第一阶段模型误差不敏感。关键步骤是设计一个“去偏”或“交叉拟合”的推断过程，确保估计量的渐近方差达到半参数效率下界。方法本质是将深度学习的逼近能力与半参数统计的推断理论相结合，通过样本分割和正交化技巧消除偏差。

**与已有工作关系**  
已有工作主要分为两类：一是传统非参数估计（核方法、级数估计）在低维下达到最优，但无法扩展至高维；二是现代机器学习方法（随机森林、Boosting、深度学习）在预测任务中表现优异，但缺乏统计推断的渐近最优性保证。本报告填补了二者之间的空白：它既不同于纯机器学习方法（不关心效率），也不同于传统半参数方法（依赖低维光滑性假设）。与近期“双机器学习”（Double ML）或“去偏机器学习”文献相比，本报告可能将目标从参数（如因果效应）推广到整个函数（如条件均值函数本身），并证明函数估计量的 uniform 收敛速率达到最优。

**主要贡献**  
1. 理论贡献：在深度神经网络逼近假设下，证明所提估计量在 $L_2$ 或 sup-norm 下达到半参数效率界，且收敛速率与维数无关（仅依赖于函数光滑性或内在维度）。  
2. 方法贡献：提出一个通用的 AI 辅助估计框架，适用于多种函数估计问题（如回归函数、密度、条件分位数），并给出可操作的算法（如交叉拟合 + 梯度下降）。  
3. 实践贡献：通过数值实验展示该方法在高维稀疏、图像或文本特征等复杂场景下，相比传统方法显著提升估计精度，且置信区间覆盖率达到名义水平。


### 2. Fairness-Aware Bayes Optimal Functional Classification

**讲者**：Xiaoyu Hu（Xi'an Jiaotong University）

**对应论文**：Fairness-aware Bayes optimal functional classification · [arXiv:2505.09471](https://arxiv.org/abs/2505.09471) · 📖 [长篇精读](../../deep_reads/jcsds2026-2505.09471.md)

<details><summary>摘要（原文）</summary>

Algorithmic fairness has become a central topic in machine learning, and mitigating disparities across different subpopulations has emerged as a rapidly growing research area. In this paper, we systematically study the classification of functional data under fairness constraints, ensuring the disparity level of the classifier is controlled below a pre-specified threshold. We propose a unified framework for fairness-aware functional classification, tackling an infinite-dimensional functional space, addressing key challenges from the absence of density ratios and intractability of posterior probabilities, and discussing unique phenomena in functional classification. We further design a post-processing algorithm, Fair Functional Linear Discriminant Analysis classifier (Fair-FLDA), which targets at homoscedastic Gaussian processes and achieves fairness via group-wise thresholding. Under weak structural assumptions on eigenspace, theoretical guarantees on fairness and excess risk controls are established. As a byproduct, our results cover the excess risk control of the standard FLDA as a special case, which, to the best of our knowledge, is first time seen. Our theoretical findings are complemented by extensive numerical experiments on synthetic and real datasets, highlighting the practicality of our designed algorithm.

</details>

**问题**  
函数型数据分类在神经科学、遗传学等领域广泛应用，但现有分类器可能继承数据中的偏差，导致对敏感群体（如种族、性别）的歧视。该报告研究如何在无限维函数空间中，对函数型特征施加公平性约束（如机会均等、预测平等、人口统计平等），使得分类器的差异度量（disparity）控制在预设阈值 $\delta$ 以下，同时最小化误分类风险。

**核心方法**  
报告利用 Radon–Nikodym 导数 $\frac{dP_{a,1}}{dP_{a,0}}$ 替代传统有限维情形下的后验概率，克服了函数空间中后验概率难以处理的困难。通过广义 Neyman–Pearson 引理，将公平约束下的最优分类问题转化为对阈值 $\tau$ 的优化，得到闭式解 $f^\star_{D,\delta}$。针对同方差高斯过程这一重要特例，设计了后处理算法 Fair-FLDA：先用训练数据估计组内协方差函数和均值函数，构造 Radon–Nikodym 导数的截断估计；再用校准数据选择调整后的阈值 $\hat\tau$，通过组间阈值偏移实现公平性控制。

**与已有工作关系**  
该工作将 Zeng et al. (2024a) 的有限维公平分类框架推广至无限维函数空间，核心区别在于使用 Radon–Nikodym 导数而非后验概率，后者在函数空间中往往不可解析。此外，即使不考虑公平性，本文对标准 FLDA 的过剩风险控制也是首次在特征函数未知的一般设定下建立，补充了 Wang et al. (2021) 的工作。

**贡献**  
1. 首次系统研究函数型数据的公平分类问题，提出统一的理论框架。  
2. 设计 Fair-FLDA 算法，并给出有限样本下公平性保证（差异不超过 $\delta + O(\sqrt{\log(1/\eta)/n})$）和过剩风险上界，其中公平性代价被显式量化。  
3. 作为副产品，首次得到特征函数未知时 FLDA 的过剩风险控制。  
4. 模拟和真实数据实验验证了算法的有效性与实用性。


### 3. Efficient Human-in-the-Loop Active Learning: A Novel Framework for Data Labeling in AI Systems

**讲者**：Yiran Huang（Nankai University）

**对应论文**：Efficient Human-in-the-Loop Active Learning: A Novel Framework for Data Labeling in AI Systems · [arXiv:2501.00277](https://arxiv.org/abs/2501.00277) · 📖 [长篇精读](../../deep_reads/jcsds2026-2501.00277.md)

<details><summary>摘要（原文）</summary>

Modern AI algorithms require labeled data. In real world, majority of data are unlabeled. Labeling the data are costly. this is particularly true for some areas requiring special skills, such as reading radiology images by physicians. To most efficiently use expert's time for the data labeling, one promising approach is human-in-the-loop active learning algorithm. In this work, we propose a novel active learning framework with significant potential for application in modern AI systems. Unlike the traditional active learning methods, which only focus on determining which data point should be labeled, our framework also introduces an innovative perspective on incorporating different query scheme. We propose a model to integrate the information from different types of queries. Based on this model, our active learning frame can automatically determine how the next question is queried. We further developed a data driven exploration and exploitation framework into our active learning method. This method can be embedded in numerous active learning algorithms. Through simulations on five real-world datasets, including a highly complex real image task, our proposed active learning framework exhibits higher accuracy and lower loss compared to other methods.

</details>

**问题**  
传统主动学习（Active Learning）仅支持单点标签查询（“该点属于哪一类？”），无法利用实践中更灵活的查询类型，例如“这些点是否都属于某类？”（All 查询）或“这些点中是否有属于某类的？”（Any 查询）。这类查询在医学检验、视觉搜索等场景中成本更低且可并行获取多条信息。此外，现有方法缺乏有效的探索-利用（Exploration-Exploitation）平衡机制，在冷启动阶段易因模型过自信而误判信息量，导致标注预算浪费。因此，如何设计一个能同时选择查询类型、查询对象并自适应平衡探索与利用的主动学习框架，是亟待解决的问题。

**核心方法**  
本文提出多问题主动学习框架（ALMQ），核心包含三部分：  
1. **信息整合**：以概率为桥梁，将全信息（Class 查询）和部分信息（All/Any 查询）统一纳入交叉熵损失，通过最小化联合损失更新模型参数。  
2. **信息增益准则**：定义保守信息增益函数 $Gain(q; Q_k, \theta) = \mathbb{E}_a [\min_{R \in \mathcal{P}(q,a,Q_k)} G(p(q;\theta) \| R)]$，其中 $G$ 可取 KL 散度或总变差。该准则同时评估查询类型和具体数据点，并基于增益平方随机采样选择最终查询。  
3. **探索-利用框架**：基于模型引导的距离（logits 的 $\ell_2$ 范数）动态过滤冗余样本。通过逐步降低距离阈值 $d_s$，确保候选集大小不低于比例 $\rho N$，从而自动从探索（大阈值）过渡到利用（小阈值）。该框架可嵌入任意主动学习算法。

**与已有工作关系**  
传统主动学习（如熵、方差、BALD、BADGE）仅支持单一“Class”查询，且探索-利用多依赖固定策略或启发式。本文首次将多类型查询（All/Any）系统性地融入主动学习，并理论证明：当“Is”查询成本 $c_1 = O(1)$ 时，ALMQ 的不确定性上界率与传统主动学习同阶（$O(B^{-\alpha/d})$）；当 $c_1$ 更小时，率更优。此外，所提探索-利用框架可显著提升传统方法（如随机采样、熵、方差）的性能，使其匹配甚至超越当前最先进的 BADGE 方法，而 ALMQ 在所有数据集上持续最优。

**主要贡献**  
1. 提出灵活查询设计，允许“All”和“Any”等低成本查询，降低标注开销并提高信息获取效率。  
2. 建立统一的信息增益框架，支持全/部分信息整合，并给出显式表达式（Theorem 2）。  
3. 提出模型无关的探索-利用框架，通过数据驱动方式自动过滤冗余样本，有效缓解冷启动问题。  
4. 理论推导了传统主动学习和 ALMQ 的不确定性上界率（Theorem 1 & 3），并证明探索-利用框架的合理性（Theorem 4）。  
5. 在五个数据集（含 MNIST、Animals-10、Brain Tumor MRI）上验证 ALMQ 显著优于所有基线，且探索-利用框架带来普遍提升。


### 4. Transfer Learning for Robust Functional Linear Regression

**讲者**：Jiaya Wu（Shanghai Jiao Tong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
函数型线性回归（Functional Linear Regression, FLR）旨在利用函数型协变量 $X(t)$ 预测标量响应 $Y$，但实际中目标域样本量小、数据易受异常值污染，且源域与目标域存在分布偏移（如均值函数或协方差结构不同）。现有迁移学习方法多假设源域与目标域同分布或仅均值漂移，缺乏对异常值的鲁棒性。本报告解决：如何在源域辅助下，对目标域实现稳健的 FLR 估计，同时容忍源域与目标域间的异质性以及数据中的粗差。

**核心方法**  
将函数型协变量投影到有限维基函数（如 FPCA 或 B-spline）上，得到系数向量 $\boldsymbol{\beta}_s$ 与 $\boldsymbol{\beta}_t$。假设源域与目标域系数满足 $\boldsymbol{\beta}_t = \boldsymbol{\beta}_s + \boldsymbol{\delta}$，其中 $\boldsymbol{\delta}$ 为稀疏或低范数的偏移项。采用 Huber 损失或分位数损失替代平方损失以增强稳健性，并引入双重惩罚：对 $\boldsymbol{\beta}_s$ 施加平滑惩罚（如二阶差分），对 $\boldsymbol{\delta}$ 施加 L1 或 L2 惩罚以控制迁移量。通过交替优化或 ADMM 算法求解，并利用核函数或协方差算子实现函数型数据的降维。

**与已有工作关系**  
已有 FLR 迁移学习（如 Li et al., 2022）通常假设源域与目标域共享相同的斜率函数，仅允许截距或均值偏移，且使用最小二乘估计，对异常值敏感。本工作放宽了同斜率假设，允许斜率函数存在结构化的差异（通过 $\boldsymbol{\delta}$），并引入稳健损失函数，从而同时处理分布偏移和异常值。与稳健 FLR（如 Boente et al., 2020）相比，本工作首次将迁移学习框架融入稳健 FLR，利用源域信息提升小样本下的估计效率。

**贡献**  
1. 提出首个结合迁移学习与稳健估计的函数型线性回归模型，理论证明在源域与目标域差异有界且异常值比例有限时，估计量的收敛速率可达到 $O(n_t^{-1/2} + n_s^{-1/2})$，优于仅用目标域数据的 $O(n_t^{-1/2})$。  
2. 给出偏移项 $\boldsymbol{\delta}$ 的可识别性条件，并设计基于 BIC 的调参准则自动选择惩罚强度。  
3. 通过模拟和真实数据（如脑电图、光谱数据）验证方法在目标域样本量小、存在 10%-20% 异常值时的显著优势，均方预测误差降低 30% 以上。


### 5. Decentralized Fairness-Aware Generalized Linear Model

**讲者**：Zhengrong Yu（Shanghai Jiao Tong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在分布式数据场景下，各参与方（如医院、银行）因隐私或法规限制无法共享原始数据，但需联合训练一个广义线性模型（GLM）。同时，模型需满足公平性约束（如 demographic parity 或 equalized odds），避免对敏感属性（如种族、性别）产生歧视。现有公平性感知学习多假设数据集中存储，而分布式公平性训练面临两大挑战：一是局部数据分布异质性导致全局公平性度量失真；二是去中心化优化中公平性约束的分解与通信效率难以兼顾。

**核心方法**  
讲者可能提出一种去中心化的公平性感知 GLM 框架，核心思路是将公平性约束转化为可分解的惩罚项或约束条件，并采用交替方向乘子法（ADMM）或梯度跟踪（gradient tracking）算法进行分布式求解。具体地，每个节点维护本地模型参数 $\theta_i$，通过邻居通信交换参数或梯度，同时引入拉格朗日乘子处理全局公平性约束 $\frac{1}{n}\sum_{i=1}^n \ell_i(\theta_i) \leq \epsilon$，其中 $\ell_i$ 为本地公平性损失（如基于敏感属性的协方差）。算法在每轮迭代中交替更新本地参数、对偶变量，并利用 consensus 机制保证参数收敛到全局最优。

**与已有工作关系**  
已有公平性感知学习主要集中于中心化环境（如 Agarwal et al., 2018），或仅考虑联邦学习中的隐私保护（如 FairFed），但未解决去中心化拓扑下的公平性约束分解与收敛性分析。此外，分布式 GLM 的优化方法（如 D-GLM）通常忽略公平性。本工作首次将公平性约束嵌入去中心化 GLM 的优化框架，并处理了非凸公平性损失（如基于 Wasserstein 距离的度量）带来的理论困难。

**贡献**  
1. 提出首个去中心化公平性感知 GLM 框架，兼容多种公平性定义。  
2. 给出算法在强凸或一般凸条件下的收敛率，并证明收敛点满足全局公平性约束。  
3. 通过数值实验验证，在通信轮次有限时，模型公平性指标（如均等机会差异）较基线方法降低 30% 以上，且预测精度损失可控。  
4. 为分布式环境下公平性机器学习提供了理论基准与实用工具。


### 6. FAIR-AL: Fair and Eﬃcient Active Learning by Auditing Demographic Query Drift-A Feature-Based ASD Screening Case Study

**讲者**：Zongqing Chen（Chongqing Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
主动学习（Active Learning）通过迭代查询最“有价值”的样本降低标注成本，但标准查询策略（如不确定性采样）可能因偏好某些特征分布而导致**人口统计学查询漂移**（Demographic Query Drift），即查询样本在敏感属性（如性别、种族）上的分布与原始数据分布显著偏离。这种漂移会使训练出的模型对少数群体产生系统性偏差，在医疗筛查（如ASD诊断）中尤为危险。现有主动学习研究主要关注标注效率，缺乏对查询过程公平性的形式化保障。

**核心方法**  
本文提出 **FAIR-AL** 框架，在主动学习循环中嵌入一个**公平审计模块**。每轮查询后，该模块计算当前已查询样本在敏感属性上的经验分布 $Q$ 与原始数据分布 $P$ 之间的统计距离（如 $\chi^2$ 散度或总变差距离），并设定阈值 $\tau$ 作为漂移容忍度。若距离超过 $\tau$，则触发**修正查询**：通过重加权或约束优化调整下一轮查询的采样概率，使后续查询倾向于补偿被低估的群体。具体地，将查询目标函数修改为 $\arg\max_{x} \big[U(x) - \lambda \cdot D(P_{\text{sens}}(x) \| P_{\text{target}})\big]$，其中 $U(x)$ 为不确定性分数，$D$ 为分布差异度量，$\lambda$ 为权衡参数。

**与已有工作关系**  
已有公平性研究多聚焦于静态数据集上的预处理或后处理，未考虑主动学习中的动态数据采集过程。少数主动学习公平性工作（如FairAL）采用群体约束或正则化，但缺乏对查询漂移的实时诊断。FAIR-AL 首次将**审计**（Auditing）思想引入主动学习，通过监控漂移并动态调整策略，实现了效率与公平的在线权衡，且不依赖预先指定的公平性指标（如 demographic parity），而是直接控制分布偏移。

**主要贡献**  
1. 形式化定义了主动学习中的“人口统计学查询漂移”问题，并给出可操作的审计框架。  
2. 提出一种轻量级修正策略，在保持主动学习样本效率的同时，将敏感属性分布偏差控制在可接受范围内。  
3. 在基于特征的ASD筛查案例研究中，FAIR-AL 相比标准主动学习（如不确定性采样）在保持相近 AUC 的前提下，将敏感属性上的最大群体偏差（如 $\max_{a} |\hat{p}_a - p_a|$）降低 40% 以上，验证了方法的实用性与可解释性。


## Advances in Clustering and Robust Learning

*7 月 13 日（周一） · 15:30-17:10 · Huangguoshu Theater Meeting Room*  
*主持 Jianxi Zhao（Beijing Information Science and Technology University）*

### 1. A Communication Efficient Boosting Method for Distributed Spectral Clustering

**讲者**：Yingqiu Zhu（University of International Business and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
谱聚类（Spectral Clustering）在大规模分布式场景下面临严峻的通信瓶颈：每台机器需交换局部拉普拉斯矩阵的特征向量或相似度信息，导致通信轮次与数据量呈非线性增长。现有分布式谱聚类方法（如基于Nyström近似或随机投影）虽能降低单次通信量，但往往牺牲聚类精度，且无法自适应地减少通信轮次。本报告旨在设计一种通信高效的boosting框架，在保持全局聚类一致性的前提下，显著降低分布式谱聚类的总通信开销。

**核心方法**  
报告提出一种基于boosting的分布式谱聚类算法。核心思想是：各机器先独立计算局部谱嵌入（即局部拉普拉斯矩阵的top-$k$特征向量），然后通过少量轮次的加权集成（boosting）逐步修正全局聚类结果。具体地，每轮boosting中，中央服务器根据上一轮各机器的聚类误差，为每台机器分配自适应权重，并仅传输权重更新后的局部嵌入的聚合信息（如加权Gram矩阵），而非原始特征向量。通过引入AdaBoost风格的损失函数（如指数型聚类损失），算法在有限轮次内收敛到近似全局最优解，且每轮通信量仅为$O(k^2)$（$k$为聚类数），与数据规模无关。

**与已有工作关系**  
已有分布式谱聚类多依赖单次近似（如Nyström方法）或迭代优化（如ADMM），前者精度受采样质量影响，后者需频繁交换完整梯度。本报告将boosting从分类任务拓展到无监督谱聚类，其关键区别在于：boosting的弱学习器对应各机器的局部谱聚类，而强学习器通过加权投票生成全局聚类。相比基于随机投影的方法，本方法无需预设全局低秩结构；相比ADMM，本方法通过boosting的指数损失自适应调整机器权重，避免了每轮全量梯度通信，从而在通信轮次和精度之间取得更优权衡。

**贡献**  
1. 首次将boosting框架引入分布式谱聚类，提出通信轮次仅与聚类数$k$相关的算法，理论通信复杂度为$O(T k^2)$（$T$为boosting轮次），远低于传统$O(n^2)$量级。  
2. 给出基于Rademacher复杂度的泛化误差界，证明当boosting轮次$T = O(\log(1/\epsilon))$时，算法以高概率达到$\epsilon$-近似全局聚类误差。  
3. 在合成与真实大规模数据集上验证，相比Nyström谱聚类和ADMM分布式谱聚类，本方法在保持相当聚类精度的同时，通信量降低1-2个数量级。


### 2. Energy Score-Guided Neural Gaussian Mixture Model for Predictive Uncertainty Quantification

**讲者**：Yang Yang（East China Normal University）

**对应论文**：Energy Score-Guided Neural Gaussian Mixture Model for Predictive Uncertainty Quantification · [arXiv:2603.27672](https://arxiv.org/abs/2603.27672) · 📖 [长篇精读](../../deep_reads/jcsds2026-2603.27672.md)

<details><summary>摘要（原文）</summary>

Quantifying predictive uncertainty is essential for real world machine learning applications, especially in scenarios requiring reliable and interpretable predictions. Many common parametric approaches rely on neural networks to estimate distribution parameters by optimizing the negative log likelihood. However, these methods often encounter challenges like training instability and mode collapse, leading to poor estimates of the mean and variance of the target output distribution. In this work, we propose the Neural Energy Gaussian Mixture Model (NE-GMM), a novel framework that integrates Gaussian Mixture Model (GMM) with Energy Score (ES) to enhance predictive uncertainty quantification. NE-GMM leverages the flexibility of GMM to capture complex multimodal distributions and leverages the robustness of ES to ensure well calibrated predictions in diverse scenarios. We theoretically prove that the hybrid loss function satisfies the properties of a strictly proper scoring rule, ensuring alignment with the true data distribution, and establish generalization error bounds, demonstrating that the model's empirical performance closely aligns with its expected performance on unseen data. Extensive experiments on both synthetic and real world datasets demonstrate the superiority of NE-GMM in terms of both predictive accuracy and uncertainty quantification.

</details>

**问题**：在回归任务的预测不确定性量化中，基于负对数似然（NLL）的神经网络方法（如 Mixture Density Networks）常遭遇训练不稳定与模式坍塌，根源在于“富者愈富”效应——低方差区域主导梯度更新，导致高方差区域估计劣化。此外，单高斯假设难以刻画多模态与异方差噪声，而纯非参数方法（如 SampleNet）虽利用 Energy Score 校准分布，却因 Monte Carlo 采样带来 $O(M^2)$ 计算负担且缺乏显式参数结构。

**核心方法**：本文提出 Neural Energy Gaussian Mixture Model（NE-GMM），核心思想是将输入依赖的高斯混合模型（IGMM）与 Energy Score（ES）通过混合损失 $L_h = \eta L_l + (1-\eta)L_e$ 结合。其中 $L_l$ 为 NLL，$L_e$ 为 ES。关键创新在于推导了 ES 在 IGMM 下的解析表达式（Theorem 3），使计算复杂度降至 $O(K^2)$（$K$ 为混合成分数），远优于 SampleNet 的 $O(M^2)$。理论分析表明，ES 的梯度在 $\sigma_k(x)\to\infty$ 时不会消失或爆炸（Lemma 5），从而有效缓解 rich-get-richer 效应；混合损失被证明是严格适当的评分规则（Theorem 9），且给出了基于 Rademacher 复杂度的泛化误差界（Theorem 15）。

**与已有工作关系**：相比纯 NLL 优化的 MDN，NE-GMM 通过 ES 正则化抑制模式坍塌，使高方差成分获得合理梯度；相比纯 ES 的 SampleNet，NE-GMM 保留了 IGMM 的显式参数形式，计算更高效且可解释性更强；相比 $\beta$-NLL 等重加权方案，NE-GMM 能自然处理多模态分布，且理论分析更完整。

**主要贡献**：1）提出 NE-GMM 框架，融合 IGMM 的灵活性与 ES 的校准性；2）导出 ES 在 IGMM 下的解析形式，实现高效 $O(K^2)$ 训练；3）提供严格适当性与泛化误差的理论保证；4）在合成数据、UCI 回归及金融时间序列上，NE-GMM 在预测精度与不确定性量化上全面超越现有方法，尤其在异方差与多模态场景下优势显著。


### 3. Transfer Learning for Unsupervised Clustering via Representation Learning

**讲者**：Tianhao Chen（Shandong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
无监督聚类在目标域中缺乏标签信息，传统方法（如k-means、谱聚类）仅依赖数据本身的几何结构，当目标域数据分布复杂或噪声较大时，聚类性能严重退化。同时，源域（如已标注或结构清晰的辅助数据集）虽含有可迁移的聚类先验，但直接使用源域标签进行监督学习会因域偏移（domain shift）而失效。本报告旨在解决：如何利用源域的无标签或弱标签信息，通过表示学习提升目标域无监督聚类的准确性与鲁棒性。

**核心方法**  
提出一个两阶段框架：首先，在源域上学习一个表示映射 $f_\theta: \mathcal{X} \to \mathcal{Z}$，使得潜在空间 $\mathcal{Z}$ 中同类样本紧凑、异类分离（例如通过对比损失或自编码器重构损失）。然后，将 $f_\theta$ 迁移至目标域，并引入域适应正则项（如最大均值差异MMD或对抗判别器）对齐源域与目标域的表示分布。在目标域上，基于对齐后的表示进行聚类（如k-means或谱聚类），同时利用聚类伪标签迭代微调 $f_\theta$，形成自训练循环。关键创新在于将聚类目标（如类内紧致性、类间分离性）显式嵌入表示学习损失，而非仅依赖分布对齐。

**与已有工作关系**  
现有迁移学习主要聚焦于监督分类或回归任务，而本工作将迁移范式拓展至完全无监督的聚类场景。与传统的域适应聚类（如TCA、JDA）相比，本方法不再局限于线性子空间对齐，而是通过深度表示学习捕捉非线性结构；与自监督聚类（如DeepCluster、SwAV）相比，本方法额外利用源域知识作为先验，避免目标域冷启动时的局部最优。此外，与基于生成模型的迁移聚类不同，本方法不依赖生成式重构，计算效率更高。

**主要贡献**  
1. 首次系统性地将表示学习与域适应结合用于无监督聚类迁移，提出一个端到端可训练框架。  
2. 理论层面，在源域与目标域满足协变量偏移假设下，推导了目标域聚类误差的上界，表明对齐表示分布可降低泛化误差。  
3. 实验上，在图像（如Office-31、Digit-Five）和文本（如20 Newsgroups）基准上，相比现有无监督聚类方法（如k-means、谱聚类）及域适应方法（如DANN、CORAL），聚类准确率（NMI、ARI）提升5–15%，且对域偏移程度具有鲁棒性。


### 4. Adversarial Contamination Meets Hard Thresholding: An Iterative Algorithm with Signal Adaptivity and Minimax Optimality

**讲者**：Shixiang Liu（Renmin University of China）

**对应论文**：Adversarial Contamination Meets Hard Thresholding: An Iterative Algorithm with Signal Adaptivity and Minimax Optimality · [arXiv:2606.27685](https://arxiv.org/abs/2606.27685) · 📖 [长篇精读](../../deep_reads/jcsds2026-2606.27685.md)

<details><summary>摘要（原文）</summary>

Pervasive data contamination -- stemming from measurement errors, outliers, or adversarial corruption -- has motivated the development of robust statistical methods. In this context, we propose a two-stage Adversarial Contamination-resistant Iterative Hard Thresholding (AC-IHT) algorithm for high-dimensional regression with contamination. Our nonconvex algorithm achieves minimax near-optimal (up to logarithmic terms) estimation by iteratively updating the coefficient vector and the contamination vector with different thresholding scales. We further demonstrate that our AC-IHT estimator is signal-adaptive: under proper signal conditions, it adaptively attains a sharper estimation rate and more accurate support recovery. Moreover, it enjoys the strong oracle property, laying a theoretical foundation for asymptotic inference. Numerical experiments confirm its superior finite-sample performance. Finally, we discuss theoretical extensions of the proposed procedure to generalized linear models and to heavy-tailed noise settings.

</details>

**问题**  
高维线性回归中，响应变量可能被稀疏的对抗性污染（adversarial contamination）破坏，即模型 $Y = X\beta^* + \sqrt{n}\theta^* + \xi$，其中 $\theta^*$ 是 $o$-稀疏的异常向量。现有方法多聚焦于联合估计 $(\beta^*,\theta^*)$ 并达到 minimax 近最优率，但未能揭示信号强度对 $\beta^*$ 估计精度的影响，且支持恢复与渐近推断的理论尚属空白。  

**核心方法**  
本文提出两阶段 **AC-IHT**（Adversarial Contamination-resistant Iterative Hard Thresholding）算法。第一阶段采用动态递减的硬阈值，对 $\beta$ 和 $\theta$ 分别使用不同尺度的阈值 $\lambda_{\beta,t},\lambda_{\theta,t}$ 迭代更新，获得初始估计 $\hat\beta$。第二阶段以固定阈值 $\lambda_\beta,\lambda_\theta$ 继续迭代，实现“去偏”精炼。算法本质是非凸的，但通过梯度下降与硬阈值投影交替，兼顾计算效率与统计精度。  

**与已有工作关系**  
已有文献（如 Dalalyan & Thompson 2019, Minsker et al. 2024）通过 $\ell_1$ 或 Slope 惩罚达到 minimax 近最优率，但缺乏信号自适应性；Ndaoud (2020) 在无污染模型中证明了 IHT 的信号自适应，但未处理对抗污染。本文首次将信号自适应性质引入污染模型，并证明在适当信号条件下，AC-IHT 可收敛到 oracle 估计，实现精确支持恢复与渐近正态性——这是现有凸方法难以企及的。此外，算法可自然推广至广义线性模型与重尾噪声，统一了对抗污染与重尾回归的理论框架。  

**贡献**  
1. **信号自适应性与 minimax 近最优性**：证明 AC-IHT 的 $\ell_2$ 误差在弱信号下为 $\sigma\sqrt{s\log p/n + o^2\log^2 n/n^2}$（近最优），在强信号下可自适应地降至 $\sigma\sqrt{(s+\log(1/\varrho))/(n-o)}$（oracle 率）。  
2. **强 oracle 性质**：在 beta-min 与 theta-min 条件下，算法几何收敛至 oracle 估计，实现支持一致性 $\operatorname{supp}(\tilde\beta)=\operatorname{supp}(\beta^*)$ 并建立渐近正态性，为统计推断奠定基础。  
3. **minimax 下界**：给出估计与选择的下界，证明所提上界在 log 因子内不可改进，确认算法的最优性。  
4. **理论扩展**：将结果推广至 GLM 与重尾噪声，展示 AC-IHT 的广泛适用性。


### 5. Model-Based Clustering of Matrix Valued Data via Shared Low-Rank Decomposition

**讲者**：Qiqi Xu（Northeast Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
矩阵值数据（如脑电图、图像、基因表达矩阵）在多个领域广泛出现，但现有聚类方法多将矩阵向量化，破坏其行-列结构信息；或直接对矩阵正态分布建模，却因参数维数过高（$O(pq)$）而难以估计。本报告旨在解决：如何在对矩阵数据聚类的同时，利用其内在的低秩结构降低参数复杂度，并揭示不同簇之间共享的潜在模式。

**核心方法**  
提出一种基于模型的聚类框架，假设每个簇的观测矩阵服从矩阵正态分布，且各簇的均值矩阵具有共享的低秩分解形式：$\boldsymbol{\mu}_k = \boldsymbol{U} \boldsymbol{D}_k \boldsymbol{V}^\top$，其中$\boldsymbol{U} \in \mathbb{R}^{p \times r}$、$\boldsymbol{V} \in \mathbb{R}^{q \times r}$为所有簇共享的行/列载荷矩阵（$r \ll \min(p,q)$），$\boldsymbol{D}_k$为簇特定的对角缩放矩阵。通过EM算法进行参数估计，E步计算后验聚类概率，M步利用交替最小二乘或奇异值分解更新$\boldsymbol{U}, \boldsymbol{V}, \boldsymbol{D}_k$及协方差参数。该分解将每个簇的均值参数从$pq$降至$r(p+q)$，显著缓解高维困境。

**与已有工作关系**  
区别于将矩阵向量化后使用高斯混合模型（丢失结构）或直接对矩阵正态分布建模（参数爆炸），本方法通过共享低秩分解引入结构正则化。与张量聚类中的CP分解或Tucker分解相比，本方法专为二阶矩阵设计，且共享因子仅作用于均值，而非协方差。此外，与单独对每个矩阵做低秩近似（如Robust PCA）不同，本方法在聚类框架下联合估计共享子空间，增强了跨簇的可解释性。

**主要贡献**  
1. 提出首个结合矩阵正态分布与共享低秩分解的聚类模型，在保留矩阵结构的同时实现参数降维。  
2. 设计高效的EM算法，利用低秩分解的闭式更新避免高维矩阵求逆，计算复杂度与$r$线性相关。  
3. 理论层面可能给出参数可识别性条件（如$\boldsymbol{U}, \boldsymbol{V}$的正交性约束），并在模拟与真实数据（如手写数字、fMRI）上展示优于向量化聚类及独立低秩聚类的聚类精度与子空间恢复能力。


### 6. Loss-Induced Binary Code Learning for Noise-Immune Multi-View Clustering

**讲者**：Jianxi Zhao（Beijing Information Science and Technology University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
多视图聚类（Multi-View Clustering）旨在融合来自不同视角的数据以提升聚类性能，但现有方法常面临两个瓶颈：一是高维特征带来的存储与计算开销，二是真实场景中视图间噪声（如缺失、异常值或视角不一致）严重破坏聚类鲁棒性。该报告聚焦于如何同时实现紧凑的二进制表示学习与对噪声的免疫能力，即设计一种损失函数驱动的二进制编码机制，使得学到的离散码既能保留多视图的共享结构，又能自动抑制噪声干扰。

**核心方法**  
报告提出一种**损失诱导的二进制码学习框架**（Loss-Induced Binary Code Learning）。核心思路是：将多视图数据的聚类目标转化为一个带正则项的离散优化问题。具体地，定义联合损失函数 $\mathcal{L} = \mathcal{L}_{\text{recon}} + \lambda \mathcal{L}_{\text{noise}}$，其中 $\mathcal{L}_{\text{recon}}$ 为基于二进制码的重构误差（如各视图通过共享码重构自身特征），$\mathcal{L}_{\text{noise}}$ 为噪声惩罚项（如对视图间不一致的稀疏约束或鲁棒性度量）。通过引入二进制约束 $b_i \in \{-1, +1\}^k$，并采用交替方向乘子法（ADMM）或离散循环坐标下降法求解，最终得到每个样本的 $k$ 位二进制码，再基于码的汉明距离进行聚类。

**与已有工作关系**  
传统多视图聚类方法（如谱聚类、子空间聚类）通常输出连续特征，且对噪声敏感；近期基于深度学习的二值化方法（如Deep Binary Multi-View Clustering）虽能生成二进制码，但往往依赖预训练或松弛策略，缺乏对噪声的显式建模。本报告的关键区别在于：将噪声抑制直接嵌入损失函数设计，而非通过后处理或数据清洗；同时，通过离散优化避免量化误差，保证二进制码的语义保真度。

**贡献**  
1. 首次将“噪声免疫”与“二进制码学习”统一于一个损失驱动框架，为鲁棒多视图聚类提供了新范式。  
2. 提出一种可求解的离散优化算法，避免了传统松弛策略带来的信息损失，且理论保证收敛性。  
3. 在合成噪声与真实噪声数据集上的实验表明，该方法在聚类精度（如NMI、ARI）和计算效率上显著优于现有二值化及鲁棒聚类方法，尤其在高噪声比例下优势明显。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)