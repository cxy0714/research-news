# Session 06 · AI + Finance

> XAGI 2026 交叉智能大会 · 10 月 17 日（周六）下午 14:00-16:00 · 4会（友谊宫二层4号会议室） · [返回会议总览](index.md)

- 4 场报告 · 已精读 4 场

**主持**：祝武（清华大学）

## 本场导览

> 自动生成：归纳本场主线，**不打分、不排名**。

这一场报告围绕“AI 如何重构经济与金融系统的建模与决策”展开，可归纳为两条主线：一是经济系统的生成式仿真与去中心化治理（韩佳乐、Luyao Zhang），二是资产定价与组合优化的统计学习方法（Yuan Zhang、黄睿钊）。前者关注宏观层面的系统设计与信息验证机制，后者聚焦微观层面的因子提取与投资决策，两条线在“如何用AI处理复杂经济数据”上形成互补。

生成式仿真主线由韩佳乐与Luyao Zhang共同推进，但路径不同。韩佳乐提出经济世界模型（EWMs）的系统蓝图，将经济模拟拆解为六级能力体系，从固定规则智能体到自我演化、制度内生演化及“仿真到现实”对齐，并基于文献综述指出现有研究多停留在低层级，缺乏对智能体演化与实证对齐的整合。Luyao Zhang则从区块链预言机切入，构建Oracle Incentive and Accountability Atlas，整合56类预言机协议（UMA、Chainlink、Flare、Tellor、Pyth），分析经济激励与问责机制如何影响去中心化信息的可信度。两者互补：韩佳乐提供生成式经济仿真的顶层架构，Luyao Zhang则聚焦于仿真所需外部数据的验证基础设施，共同指向“可信经济AI”的构建。

统计学习主线中，Yuan Zhang与黄睿钊分别处理因子模型与组合优化的高维问题。Yuan Zhang证明深度神经网络训练的随机贴现因子（SDF）可分解为非线性特征发现与定价规则两部分，并通过Portfolio Tangent Kernel（PTK）导出线性因子表示，在总体层面给出可解释的定价结构。黄睿钊则在MAXSER估计器基础上引入条件收益预测，提出MAXSER-PR框架，将预测信息嵌入高维均值-方差优化，实现无条件均值-方差效率。两者递进：Yuan Zhang提供因子提取的理论分解，黄睿钊则将该类因子用于实际组合构建，解决预测与优化的衔接问题。

若按主题选择入口：对经济仿真与系统设计感兴趣，可先看韩佳乐（打底框架）再读Luyao Zhang（数据验证细节）；对资产定价方法，Yuan Zhang提供理论分解（打底），黄睿钊展示应用延伸（进阶）。若时间有限，韩佳乐与Yuan Zhang分别代表两条主线的核心方法，可作为优先阅读对象。

---

### 1. From Economic Agents to Agentic Economies: A Systems Blueprint for Economic World Models

**讲者**：韩佳乐（深圳河套学院 · 社会科学智能中心） · 14:00-14:30

**对应论文**：From Economic Agents to Agentic Economies: A Systems Blueprint for Economic World Models · [arXiv:2608.06020](https://arxiv.org/abs/2608.06020)

<details><summary>摘要（会议官网）</summary>

<p>经济世界模型（Economic World Models，EWMs）是一类生成式经济模型，通过刻画异质主体及其信念与行动，以及主体互动形成宏观结果所依赖的市场与制度机制，内生地模拟经济系统的演化。本文提出一条经济世界模型的实现路线，将其构建为由异质主体持续行动、互动、适应，并与市场和制度共同演化的生成引擎，从而自下而上地产生经济动态。我们构建了一个六级能力体系，涵盖固定规则智能体世界、自适应规则智能体世界、基于大语言模型的智能体世界、自我演化智能体、演化中的制度世界，以及与现实观测持续对齐的“仿真到现实”经济孪生。基于该体系的系统性文献综述表明，现有研究仍主要集中于较低层级的智能体与仿真环境，而具备智能体自我演化、制度内生演化、持续实证对齐和经济机制验证能力的系统仍较为少见。通过将经济世界模型的研究愿景转化为可实施的系统蓝图，本文旨在推动下一代经济仿真环境的发展，使其既能作为人类决策者的高保真试验场，也能为智能体提供训练、规划、评估与安全验证的基础环境。</p>

</details>

**问题**  
本报告要解决的是：如何从孤立的“经济智能体”走向可运行的“智能体经济”（Agentic Economies），即把经济世界模型（EWMs）从概念变成可实施的系统蓝图。官网摘要指出，EWMs 是一类生成式经济模型，通过刻画异质主体的信念与行动，以及市场与制度机制，内生地模拟经济演化；但现有工作多停留在较低层级的智能体与仿真环境，缺少对自我演化智能体、内生制度演化、持续实证对齐等能力的系统整合。报告认为，当前 LLM 提供了信念、记忆与推理的基质，工具调用与多智能体仿真使经济行动可执行，前沿实验室也开始设立经济学研究机构，因此现在值得把这一愿景工程化。

**核心方法**  
报告提出一个模块化经济运行时（runtime）而非单体预测器，包含智能体层、环境层、共演化层和现实对齐层。形式上，经济世界模型被写作 $\hat{s}_{t+1}=T(s_t,u_t)$，其中状态 $s_t=(x_t,\{z^i_t,b^i_t\}_{i=1}^{N_t},I_t)$ 同时包含总量经济变量、智能体私有状态与信念，以及制度环境。智能体通过信念更新 $B^i$、决策规则 $\pi^i$、状态转移 $\Omega^i$ 行动，市场通过聚合算子 $G$ 形成宏观结果，制度算子 $\Phi$ 允许规则演化。报告还给出六级能力阶梯：固定规则智能体世界、自适应规则智能体世界、LLM 智能体世界、自我演化智能体、演化中的制度世界、仿真到现实经济孪生，并据此对现有文献做系统综述。

**与已有工作的关系**  
该路线直接承接 Cong (2025) 的 EWM/DDGE 框架，但把重心从经济学均衡概念转向 AI 系统实现；同时将经济世界模型与物理世界模型（如 Ha & Schmidhuber 的世界模型）对照，强调经济状态由主体内生生成而非外部定律驱动。报告把金融领域的组件级原型——如 Cong et al. (2021) 的强化学习投资组合智能体、Campello et al. (2025) 的公司政策搜索、Cong et al. (2024) 的在线信贷“智能体–数据–模型”反馈、Bini et al. (2025) 的 LLM 决策智能体行为校准——重新定位为完整 EWM 的可复用模块，而非最终系统。

**贡献与边界**  
主要贡献是把 EWM 研究愿景转译为可实施的系统蓝图：给出六级能力阶梯、四层运行时架构、最小执行接口（`ewm.make`、`world.run_agents`、`world.step`），并发布配套论文清单。边界也很明确：这是一篇蓝图/路线图性质的工作，不是完整实现；六级体系是“实现成熟度”分类，并不自动保证经济学的反事实一致性——原文明确说能力层级高不等于满足 DDGE 式反事实约束。官网摘要未给出具体实验验证或基准结果，因此其有效性仍取决于后续系统能否在真实数据上完成持续对齐与机制验证。

<details><summary>讲者简介</summary>

<p>韩佳乐，深圳河套学院社会科学智能中心研究助理教授，曾在香港科技大学商学院从事博士后研究，获北京邮电大学计算机科学博士学位。研究聚焦人工智能与经济金融交叉领域，重点关注经济世界模型，大语言模型驱动的社会模拟，以及自主经济与金融智能体。在 ICLR、ICML、ACL、IEEE TKDE 等AI会议和期刊发表论文30余篇，另有两篇论文在 UTD-24 商科顶级期刊处于大修阶段。研究成果曾获 COLING 2025 Outstanding Paper Award。在学术服务方面，担任 ACL 等国际会议领域主席，并长期为多个人工智能与商科领域重要会议和期刊担任审稿人，获 ICML 2026 Silver Reviewer Award。</p>

</details>


### 2. Who Verifies Decentralized Information? Economic Incentives, Accountability, and Trustworthy AI Across Oracle Protocols

**讲者**：Luyao Zhang（Duke Kunshan University · Digital Innovation Research Center and Social Science Division） · 14:30-15:00

**对应论文**：未检索到公开论文（以下为依据报告摘要与讲者方向的推断）

<details><summary>摘要（会议官网）</summary>

<p>Who Verifies Decentralized Information? Economic Incentives, Accountability, and Trustworthy AI Across Oracle Protocols Blockchain oracles enable smart contracts to use external information, but their records remain fragmented and difficult to compare. The Oracle Incentive and Accountability Atlas integrates 56 oracle categories with data from UMA, Chainlink, Flare, Tellor, and Pyth. It reconstructs verification and dispute lifecycles, identifying actors, decisions, capital at risk, rewards, penalties, and outcomes across 105.6 million traceable records. By connecting computational infrastructure with mechanism design, the Atlas reveals how incentives shape participation, information quality, and accountability. It establishes a comparative science of decentralized verification and supports the design of more resilient oracle markets, safer digital finance, and trustworthy AI systems.</p>

</details>

*（未检索到公开论文，以下依据报告摘要与讲者方向推断）*

**问题**：区块链预言机为智能合约提供外部数据，但各协议的数据记录彼此割裂，难以横向比较，导致“谁在验证去中心化信息、验证是否可信”缺乏系统性答案。报告针对这一缺口，聚焦预言机验证过程中的经济激励与问责机制。其动机在于：预言机是数字金融与可信AI系统依赖链下数据的关键环节，若验证者的激励设计不当，信息质量与系统韧性都会受损；而现有讨论多停留在单个协议或技术层面，缺少跨协议、可量化的比较框架。

**核心方法**：报告提出“Oracle Incentive and Accountability Atlas”，将56个预言机类别与UMA、Chainlink、Flare、Tellor、Pyth的数据整合，重建验证与争议解决的生命周期，识别其中的参与者、决策节点、风险资本、奖励、惩罚与结果，覆盖1.056亿条可追溯记录。该方法将计算基础设施与机制设计相连接，通过大规模数据重构来揭示激励如何塑造参与行为、信息质量与问责效果，从而建立一种“去中心化验证的比较科学”。

**与已有工作的关系**：该工作相对单协议案例研究或纯技术安全分析，推进到跨预言机协议的系统比较。摘要中明确以UMA、Chainlink、Flare、Tellor、Pyth为数据来源，这些协议分别代表不同的验证机制（如乐观验证、质押投票、去中心化价格供给等）。结合讲者长期从事机制设计、强化学习与人类-AI交互研究，该框架可能借鉴了机制设计中的激励相容分析思路，但摘要未给出具体理论模型或基线方法。

**贡献与边界**：主要贡献是提供一个公开可比较的预言机激励与问责图谱，为设计更有韧性的预言机市场、更安全的数字金融以及可信AI系统提供实证基础。边界在于：分析依赖链上可追溯记录，可能无法覆盖链下治理或非结构化信息；56个类别与五个协议的选择未必代表全部预言机生态；摘要未给出具体因果结论、政策建议或对失败案例的归因，因此其解释力仍限于描述与关联层面。

<details><summary>讲者简介</summary>

<p>Dr.Luyao Zhang is an Assistant Professor of Economics and Senior Research Scientist at the Digital Innovation Research Center at Duke Kunshan University. She earned her Ph.D. in Economics from The Ohio State University and holds a B.A. in Economics and a B.S. in Mathematics and Applied Mathematics from Peking University. Her continuing education through programs at the University of Oxford and MIT spans blockchain strategy, machine learning, generative AI, reinforcement learning, data engineering, and quantum computing. Her interdisciplinary research bridges economics and computational science, with publications including the Review of Economics and Statistics, Scientific Data (Nature Portfolio), NeurIPS, ACM CSCW, IEEE S&amp;P, ACM CCS, and AAAI/ACM AIES. She leads a project funded by the National Natural Science Foundation of China titled “Trust Mechanism Design on Blockchain: An Interdisciplinary Approach of Mechanism Design, Reinforcement Learning, and Human–AI Interactions.” In education, she advances pedagogical innovation for the generative AI era through credit-bearing courses in Duke Kunshan University’s U.S.–China joint-degree program. Her approach integrates interdisciplinary research, project-based education, community-based learning, and the Industry 4.0 Open Education Resource Publication Initiatives. She guides students in transforming research, data, code, and interactive projects into openly accessible knowledge resources while cultivating their aspirations to become scientists, entrepreneurs, and philanthropists who benefit local communities and advance the United Nations Sustainable Development Goals (SDGs). Her public and professional service advances open science, responsible data governance, international standards, and trustworthy technological innovation in support of the UN SDGs. She serves on the Editorial Board of Scientific Data and is Secretary of the IEEE P3469 Working Group, which is developing an environmental-liability accounting process model for traceable supply-chain and product emissions. She also serves as Faculty Lead of the I-SEE (Intelligent and Sustainable Economic Ecosystem) Initiative at the Global Institute of Finance, Technology, and Society (GIFTS), founded by Professor Lin William Cong. She is Vice Chair of SG1 (Thematic Document Structure) within IEEE P7999, which is developing a standard for integrating organizational ethics oversight into projects and processes involving artificial intelligence. At Duke Kunshan University, she serves as the founding faculty advisor for the AI Club, Finance Club, DKU Hackathon, and Digital Innovation Contest.</p>

</details>


### 3. Large and Deep Factor Models

**讲者**：Yuan Zhang（上海财经大学 · 金融学院） · 15:00-15:30

**对应论文**：Large and Deep Factor Models · [DOI](https://doi.org/10.2139/ssrn.6225778)

<details><summary>摘要（会议官网）</summary>

<p>We show that a deep neural network (DNN) trained to construct a stochastic discount factor (SDF) admits an additive decomposition separating nonlinear characteristic discovery from the pricing rule that aggregates them. This decomposition yields a linear factor representation governed by the Portfolio Tangent Kernel (PTK), which summarizes the network’s learned features. In population, the implied SDF converges to a ridge-regularized version of the true SDF, with the degree of regularization determined by spectral complexity. Empirically, using U.S. equity data, the PTK representation delivers economically and statistically significant performance gains, while rising spectral complexity imposes tighter limits on finite-sample pricing.</p>

</details>

**问题**：深度神经网络（DNN）在构造随机贴现因子（SDF）时，特征发现与定价规则纠缠，导致因子结构难以解释。报告旨在通过可加性分解，将非线性特征发现与聚合定价规则分离，从而得到线性因子表示。当前深度学习在资产定价中应用广泛，但缺乏理论解释，该分解为理解深度因子模型提供了新视角。

**核心方法**：报告提出，训练DNN构造SDF可分解为两部分：特征发现和定价规则。该分解产生由Portfolio Tangent Kernel（PTK）控制的线性因子表示，PTK总结了网络学到的特征。在总体中，隐含SDF收敛到真实SDF的岭正则化版本，正则化程度由谱复杂度决定。实证使用美国股票数据，PTK表示带来经济和统计上显著的性能提升，但谱复杂度上升会限制有限样本定价。

**与已有工作的关系**：该工作属于将机器学习方法引入因子模型的研究路线。通过PTK和岭正则化，将深度模型与线性因子模型及核方法联系起来。材料未明确列出基线，但可推断其与正则化线性定价模型和核方法相关。讲者此前在资产定价和机器学习领域有研究，该报告是其AI驱动因子建模方向的延续。

**贡献与边界**：主要贡献是给出DNN-SDF的可加性分解，使深度因子模型具备线性可解释性，并刻画了谱复杂度对有限样本定价的约束。边界在于：理论结果依赖谱复杂度概念，实证仅基于美国股票数据；材料未给出具体数据规模、性能提升数值，且论文摘要未在材料中给出，因此无法评估更广泛的适用性。

<details><summary>讲者简介</summary>

<p>张元 / Yuan Zhang Yuan Zhang is an Associate Professor of Finance at Shanghai University of Finance and Economics. His research spans asset pricing, financial intermediation, and machine learning in financial markets. He has published in the Review of Financial Studies and is currently developing AI-driven methods for factor modeling and portfolio optimization, including work on benchmarking large language models in quantitative finance at ICLR 2026. He received his Ph.D. from the Swiss Finance Institute at EPFL and was a visiting Ph.D. student at MIT Sloan.</p>

</details>


### 4. Incorporating Return Prediction in High-Dimensional Mean-Variance Portfolio Optimization

**讲者**：黄睿钊（香港科技大学 · ISOM） · 15:30-16:00

**对应论文**：Incorporating Return Prediction in High-Dimensional Mean-Variance Portfolio Optimization · [DOI](https://doi.org/10.2139/ssrn.5801843)

<details><summary>摘要（会议官网）</summary>

<p>We develop a framework that incorporates return prediction to achieve unconditional mean-variance efficiency in high dimensions. Our method, termed MAXSER-PR, builds upon the seminal “MAXSER” estimator of Ao, Li, and Zheng (2019) by integrating conditional information into the optimization, thereby providing a tractable bridge between conditional return prediction and unconditional mean-variance efficiency. Under an elliptical model for the unpredictable return component that allows for heteroskedasticity, heavy-tailedness and serial dependence, and an elastic net regularity condition, our method asymptotically attains unconditional mean-variance efficiency. We demonstrate that our method delivers superior performance through comprehensive empirical studies across multiple prediction models and high-dimensional settings.</p>

</details>

**问题**：高维均值-方差组合优化中，如何将收益预测纳入优化框架并同时保证无条件均值-方差效率？现有MAXSER估计器虽能处理高维协方差矩阵，但未利用条件信息。随着预测模型和高维数据日益丰富，需要一个可处理的桥接方法，使条件预测能直接服务于无条件效率的组合选择。

**核心方法**：提出MAXSER-PR，在MAXSER基础上整合条件信息。具体地，对不可预测收益成分假设椭圆分布，允许异方差、重尾和序列相关；在弹性网正则条件下，构造估计器并证明其渐近达到无条件均值-方差效率。官网摘要未给出目标函数或算法细节，也未报告实证中的具体数值。

**与已有工作的关系**：直接基于Ao, Li, and Zheng (2019)的MAXSER估计器，将其从无条件协方差估计扩展为条件信息整合。与条件收益预测模型结合，但摘要未点名具体预测模型。相比原MAXSER，新方法在保持高维可处理性的同时，桥接了条件预测与无条件效率。

**贡献与边界**：主要贡献是提出一个在高维下同时利用收益预测并实现无条件均值-方差效率的框架，且理论允许非高斯、异方差和序列依赖。边界：依赖椭圆模型和弹性网正则条件，理论为渐近性质；实证覆盖多个预测模型和高维设置，但官网摘要未给出数据集、样本区间或业绩对比数字，因此无法评估实际改进幅度。

<details><summary>讲者简介</summary>

<p>Ruizhao Huang is a PhD candidate at The Hong Kong University of Science and Technology (HKUST), supervised by Professors Yingying Li and Xinghua Zheng. His research interests include large portfolio optimization, high-frequency data, empirical asset pricing, and statistical machine learning.</p>

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)
