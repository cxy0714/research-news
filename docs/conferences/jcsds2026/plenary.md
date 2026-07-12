# 大会报告 Plenary Lectures

> JCSDS 2026 · Plenary Lectures · [返回会议总览](index.md)

- 含 **6 个分会场 · 6 场报告**（已检索到对应论文 6 场）

---

## Plenary Talk

*7 月 11 日（周六） · 09:00-09:50 · Colourful Guizhou Ballroom*  
*主持 Jiashun Jin（Southeast University）*

### 1. Nobel Prizes for Data Science

**讲者**：David Donoho（Stanford University）

**对应论文**：Data Science at the Singularity · [arXiv:2310.00865](https://arxiv.org/abs/2310.00865)

David Donoho 是斯坦福统计系资深教授、美国科学院院士，现代高维统计与信号处理的奠基人之一：小波（wavelet）阈值去噪、压缩感知（compressed sensing）、$\ell_1$ 稀疏恢复、最小最大风险理论均与其名字紧密相连，长期思考"数据科学作为一门学科"的本质。此次大会报告并非对应单篇论文，而是基于其近年关于数据科学发展观的系列思辨，尤其是 2023 年的《Data Science at the Singularity》（arXiv:2310.00865）及其在 HDSR 上引发的大讨论。

报告主题"Nobel Prizes for Data Science"是一个引人深思的切入点：数学有 Fields、计算机有 Turing，但数据科学至今无对应"诺奖级"的荣誉标尺。Donoho 由此追问——数据科学究竟贡献了哪些堪称划时代的成果，又该以何种标准衡量其科学价值。他提出经验机器学习（empirical machine learning）近年之所以爆发，源于"无摩擦可复现性"（frictionless reproducibility）三要素的成熟：公开数据（data）、公开代码（code）、公开竞赛与排行榜（challenge）。当研究、复现、迭代的成本趋近于零，领域便进入"奇点"式加速，AlphaFold、大语言模型等成就正是其产物。

报告很可能借"诺奖"隐喻，反思统计学与数据科学的关系：哪些进步是范式级突破、哪些只是工程红利，以及在 AI 狂飙时代统计学界应如何定位自身价值、争取学科话语权。对统计研究者而言，这是一场关于学科认同、评价体系与未来方向的战略性演讲，而非具体方法论报告。


## Plenary Talk

*7 月 11 日（周六） · 10:10-11:00 · Colourful Guizhou Ballroom*  
*主持 Jianqing Fan（Princeton University）*

### 1. Nonparametric Estimators of Nonstationary Densities of Streaming Data

**讲者**：Aurore Delaigle（University of Melbourne）

**对应论文**：Nonparametric Estimators of Nonstationary Densities of Streaming Data · [论文/主页](https://findanexpert.unimelb.edu.au/profile/13215-aurore-delaigle)

Aurore Delaigle 是墨尔本大学统计学教授、澳大利亚科学院院士，非参数统计、测量误差（measurement error）与函数型数据分析（functional data analysis）领域的国际权威，与已故统计学家 Peter Hall 长期合作。她最具代表性的贡献集中在**含误差变量的反卷积（deconvolution）密度与回归估计**：当观测 $W=X+U$ 被测量误差 $U$ 污染时，如何借助核方法与傅里叶反卷积一致地估计潜在变量 $X$ 的密度 $f_X$，并给出误差分布已知/未知、重复测量等情形下的收敛率与最优带宽理论。这类问题的收敛速度常常只有对数级（logarithmic rate），刻画了反问题的固有难度。

本次大会报告聚焦**流数据（streaming data）的非平稳密度估计**——这是把她擅长的非参数密度理论推向现代大数据场景的自然延伸。传统核密度估计假设样本同分布（stationary）且可一次性访问全部数据；而流数据的分布随时间漂移（nonstationary/concept drift），且数据量巨大、只能单遍扫描、无法全存。报告很可能讨论：如何构造随时间自适应、可在线递归更新（online/recursive）的非参数估计器，用遗忘因子或局部时间窗跟踪演化的密度 $f_t(x)$，并建立其偏差-方差权衡、带宽与窗宽的联合选择及一致性/渐近正态性理论。

对听众而言，这是一场兼具方法论深度与应用价值的报告：它把经典非参数平滑理论、时间自适应与计算受限的流式计算框架结合，回应了工业界实时监控、传感网络等场景中"分布在变、内存有限"的核心统计挑战。因主题较新，尚无单一对应论文，此解读基于讲者一贯的非参数与测量误差研究脉络。


## Plenary Talk

*7 月 11 日（周六） · 11:00-11:50 · Colourful Guizhou Ballroom*  
*主持 Hongyu Zhao（Yale University）*

### 1. Bridging Minds and Machines: Rethinking Embodied Intelligence and Agentic AI

**讲者**：Bingyi Jing（The Chinese University of Hong Kong, Shenzhen）

**对应论文**：Bridging Minds and Machines: Rethinking Embodied Intelligence and Agentic AI · [论文/主页](https://sai.cuhk.edu.cn/en/teacher/162)

Bing-Yi Jing（荆炳义）现为香港中文大学（深圳）数据科学学院教授，此前长期任教于香港科技大学数学系。他是概率极限理论与统计推断的资深学者，早年以**经验似然（empirical likelihood）、自助法（bootstrap）、$U$-统计量与自正则化（self-normalized）极限定理**等方向著称，近年将研究重心转向高维统计、网络数据分析（network/graph）、随机矩阵与机器学习的理论基础，兼具深厚数理功底与对 AI 前沿的关注。

本次大会报告"连接心智与机器"面向当下最热的两大范式——**具身智能（embodied intelligence）与智能体 AI（agentic AI）**。具身智能强调智能必须通过身体与物理世界交互、在感知-行动闭环中涌现，而非仅靠离线文本训练；agentic AI 则关注让大模型具备自主规划、工具调用、记忆与多步决策能力，形成能在开放环境中持续行动的"智能体"。报告标题中的"rethinking"提示讲者意在从统计与数理科学视角重新审视这些工程驱动的概念：智能体的决策与泛化能否用统计学习理论、序贯决策（强化学习、bandits）、因果与不确定性量化的语言刻画？世界模型（world model）中的表示学习、In-Context Learning 的涌现机制又蕴含怎样的可分析结构？

作为一位从传统数理统计跨入 AI 的学者，Jing 的报告很可能强调"机器"（大模型、机器人本体）与"心智"（认知、推理、决策）之间的桥梁，呼吁统计学界在具身与智能体浪潮中提供理论工具与严谨评估框架，而非旁观。因属方向性综述报告，无单篇对应论文，此解读基于讲者研究脉络与该主题的学术内涵。


## Plenary Talk

*7 月 12 日（周日） · 08:30-09:20 · Colourful Guizhou Ballroom*  
*主持 Yuantao Hao（Peking University）*

### 1. Conditional Generation via Diffusion, Flow, and Schrödinger Bridges

**讲者**：Jun Liu（Tsinghua University）

**对应论文**：Schrödinger bridge based deep conditional generative learning · [arXiv:2409.17294](https://arxiv.org/abs/2409.17294)

Jun Liu（刘军）是国际顶尖统计学家、美国科学院院士，长期任教于哈佛大学统计系，近年回国执掌清华大学讲席教职并领衔其课题组。他是**贝叶斯计算与蒙特卡洛方法的奠基性人物**：序贯蒙特卡洛（sequential Monte Carlo）、数据增广、Gibbs 采样收敛分析及生物信息学中的基序发现（Gibbs motif sampler）均是其标志性贡献，著作《Monte Carlo Strategies in Scientific Computing》影响深远。他对"如何从复杂分布中采样"有着数十年的深刻积累，这与当代生成模型的核心问题高度契合。

本次大会报告聚焦**条件生成（conditional generation）的三大现代范式**：扩散模型（diffusion）、流匹配（flow matching）与薛定谔桥（Schrödinger bridge）。三者本质都在学习一条把简单参考分布输运到复杂目标分布的路径——扩散模型通过前向加噪与反向去噪的 SDE，流模型通过学习连续时间的 ODE 速度场，薛定谔桥则在两端分布固定下求解带熵正则的最优输运（entropic optimal transport），是更一般的动态桥接框架。所谓"条件"生成，即建模条件分布 $p(y\mid x)$，使给定协变量 $x$ 即可采样响应 $y$，这直接服务于统计中的条件密度估计、回归、后验推断与不确定性量化。

代表作 arXiv:2409.17294《Schrödinger bridge based deep conditional generative learning》正体现这一思路，用薛定谔桥构造深度条件生成器并给出统计学习保证。报告很可能从统计学家视角统一审视这三类方法的联系、采样效率与理论性质（如收敛率、样本复杂度），并把生成式 AI 重新锚定到经典的采样与推断传统之中，为统计推断提供新的计算引擎。


## Plenary Talk

*7 月 12 日（周日） · 09:20-10:10 · Colourful Guizhou Ballroom*  
*主持 Linglong Kong*

### 1. Asymptotic Theory in the AI Era

**讲者**：Qiman Shao（Southern University of Science and Technology）

**对应论文**：Asymptotic Theory in the AI Era · [论文/主页](http://www.sta.cuhk.edu.hk/peoples/qmshao/)

Qi-Man Shao（邵启满）是南方科技大学统计与数据科学系讲席教授、概率极限理论的国际权威。他最负盛名的贡献是**自正则化（self-normalized）极限理论与 Cramér 型中偏差（moderate deviation）**：与 Bing-Yi Jing、王前进等合作建立了自正则化和 Studentized 统计量的大偏差、中偏差与 Berry-Esseen 界，突破了对高阶矩的苛刻要求，使得极限定理在重尾、依赖数据下依然稳健。他也是 **Stein 方法**的领军人物之一，与合作者合著《Normal Approximation by Stein's Method》，系统发展了正态与非正态逼近的精细收敛率理论。

本次大会报告"AI 时代的渐近理论"是一篇立意宏大的方向性演讲。经典渐近理论建立在"样本量 $n\to\infty$、维度 $p$ 固定"的框架上，而现代 AI 面对的是**高维乃至超高维（$p\gg n$）、过参数化神经网络、非凸优化、依赖与非独立同分布数据**的全新格局。报告很可能追问：在这样的场景下，中心极限定理、收敛率、置信区间与假设检验的渐近保证还成立吗？如何为高维统计量、随机算法（SGD 轨迹）乃至深度学习估计量提供分布逼近与不确定性量化？Stein 方法、中偏差理论、高维 CLT 等正是搭建这座桥梁的利器。

报告的核心关切在于**统计学的理论价值如何在 AI 时代延续**——当预测精度由算力和数据驱动时，渐近理论仍是理解算法为何有效、量化误差与风险、赋予 AI 输出可信度（valid inference）的根基。相关思路亦见于其近期"From Asymptotics to Action"的公开演讲。这是一场号召统计理论家主动介入 AI 前沿、以严谨渐近分析支撑可信 AI 的报告，无单篇对应论文，此解读基于讲者研究脉络。


## Plenary Talk

*7 月 12 日（周日） · 10:30-11:20 · Colourful Guizhou Ballroom*  
*主持 Ying Fang（Xiamen University）*

### 1. Causal Generalist Medical AI

**讲者**：Hongtu Zhu（University of North Carolina at Chapel Hill）

**对应论文**：Causal Inference in Biomedical Imaging via Functional Linear Structural Equation Models · [arXiv:2601.20610](https://sph.unc.edu/adv_profile/hongtu-zhu-phd/)

Hongtu Zhu（朱宏图）是北卡罗来纳大学教堂山分校（UNC Chapel Hill）生物统计系杰出教授、ASA/IMS Fellow，医学影像统计与神经影像大数据分析的国际领军人物。他长期主持 UK Biobank、ADNI 等大型影像遗传学（imaging genetics）研究，方法学贡献涵盖**函数型数据与流形上的回归、影像基因组关联、张量/高维成像数据的统计建模、以及大规模生物医学数据的因果推断**，兼具深厚统计理论与真实医疗场景落地经验。

本次大会报告"因果通用医学 AI"直击当前医学 AI 的两大痛点。其一是"通用（generalist）"：借鉴基础模型（foundation model）范式，构建能跨模态（影像、文本、基因、电子病历）、跨任务（诊断、分割、预后、报告生成）统一处理的通用医学 AI，而非为每个任务单训一个模型。其二、也是核心的是"因果（causal）"：现有医学大模型多为相关性驱动的黑箱预测，易受混杂（confounding）、分布漂移与虚假关联影响，难以支撑治疗决策与临床干预。报告主张把**因果推断框架（结构方程、反事实、$do$-算子、混杂调整）**嵌入通用医学 AI，使模型不仅回答"是什么"，更能回答"如果干预会怎样"，从而提升可解释性、公平性与跨人群的可迁移性。

代表性思路可见其近作《Causal Inference in Biomedical Imaging via Functional Linear Structural Equation Models》，将结构方程模型推广到函数型影像数据以刻画因果通路。该报告亦为其在 NISS、Duke DISS 等多个场合宣讲的主题。整体上这是一场融合因果推断、基础模型与医学影像的前沿愿景报告，倡导以因果性为医学 AI 注入可信与可行动的临床价值。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)