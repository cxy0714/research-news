# Session 06 · AI + Finance

> XAGI 2026 交叉智能大会 · 10 月 17 日（周六）下午 14:00-16:00 · 4会（友谊宫二层4号会议室） · [返回会议总览](index.md)

- 4 场报告 · 已精读 0 场

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

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

<p>韩佳乐，深圳河套学院社会科学智能中心研究助理教授，曾在香港科技大学商学院从事博士后研究，获北京邮电大学计算机科学博士学位。研究聚焦人工智能与经济金融交叉领域，重点关注经济世界模型，大语言模型驱动的社会模拟，以及自主经济与金融智能体。在 ICLR、ICML、ACL、IEEE TKDE 等AI会议和期刊发表论文30余篇，另有两篇论文在 UTD-24 商科顶级期刊处于大修阶段。研究成果曾获 COLING 2025 Outstanding Paper Award。在学术服务方面，担任 ACL 等国际会议领域主席，并长期为多个人工智能与商科领域重要会议和期刊担任审稿人，获 ICML 2026 Silver Reviewer Award。</p>

</details>


### 2. Who Verifies Decentralized Information? Economic Incentives, Accountability, and Trustworthy AI Across Oracle Protocols

**讲者**：Luyao Zhang（Duke Kunshan University · Digital Innovation Research Center and Social Science Division） · 14:30-15:00

**对应论文**：未检索到公开论文（以下为依据报告摘要与讲者方向的推断）

<details><summary>摘要（会议官网）</summary>

<p>Who Verifies Decentralized Information? Economic Incentives, Accountability, and Trustworthy AI Across Oracle Protocols Blockchain oracles enable smart contracts to use external information, but their records remain fragmented and difficult to compare. The Oracle Incentive and Accountability Atlas integrates 56 oracle categories with data from UMA, Chainlink, Flare, Tellor, and Pyth. It reconstructs verification and dispute lifecycles, identifying actors, decisions, capital at risk, rewards, penalties, and outcomes across 105.6 million traceable records. By connecting computational infrastructure with mechanism design, the Atlas reveals how incentives shape participation, information quality, and accountability. It establishes a comparative science of decentralized verification and supports the design of more resilient oracle markets, safer digital finance, and trustworthy AI systems.</p>

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

<p>Dr.Luyao Zhang is an Assistant Professor of Economics and Senior Research Scientist at the Digital Innovation Research Center at Duke Kunshan University. She earned her Ph.D. in Economics from The Ohio State University and holds a B.A. in Economics and a B.S. in Mathematics and Applied Mathematics from Peking University. Her continuing education through programs at the University of Oxford and MIT spans blockchain strategy, machine learning, generative AI, reinforcement learning, data engineering, and quantum computing. Her interdisciplinary research bridges economics and computational science, with publications including the Review of Economics and Statistics, Scientific Data (Nature Portfolio), NeurIPS, ACM CSCW, IEEE S&amp;P, ACM CCS, and AAAI/ACM AIES. She leads a project funded by the National Natural Science Foundation of China titled “Trust Mechanism Design on Blockchain: An Interdisciplinary Approach of Mechanism Design, Reinforcement Learning, and Human–AI Interactions.” In education, she advances pedagogical innovation for the generative AI era through credit-bearing courses in Duke Kunshan University’s U.S.–China joint-degree program. Her approach integrates interdisciplinary research, project-based education, community-based learning, and the Industry 4.0 Open Education Resource Publication Initiatives. She guides students in transforming research, data, code, and interactive projects into openly accessible knowledge resources while cultivating their aspirations to become scientists, entrepreneurs, and philanthropists who benefit local communities and advance the United Nations Sustainable Development Goals (SDGs). Her public and professional service advances open science, responsible data governance, international standards, and trustworthy technological innovation in support of the UN SDGs. She serves on the Editorial Board of Scientific Data and is Secretary of the IEEE P3469 Working Group, which is developing an environmental-liability accounting process model for traceable supply-chain and product emissions. She also serves as Faculty Lead of the I-SEE (Intelligent and Sustainable Economic Ecosystem) Initiative at the Global Institute of Finance, Technology, and Society (GIFTS), founded by Professor Lin William Cong. She is Vice Chair of SG1 (Thematic Document Structure) within IEEE P7999, which is developing a standard for integrating organizational ethics oversight into projects and processes involving artificial intelligence. At Duke Kunshan University, she serves as the founding faculty advisor for the AI Club, Finance Club, DKU Hackathon, and Digital Innovation Contest.</p>

</details>


### 3. Large and Deep Factor Models

**讲者**：Yuan Zhang（上海财经大学 · 金融学院） · 15:00-15:30

**对应论文**：Large and Deep Factor Models · [DOI](https://doi.org/10.2139/ssrn.6225778)

<details><summary>摘要（会议官网）</summary>

<p>We show that a deep neural network (DNN) trained to construct a stochastic discount factor (SDF) admits an additive decomposition separating nonlinear characteristic discovery from the pricing rule that aggregates them. This decomposition yields a linear factor representation governed by the Portfolio Tangent Kernel (PTK), which summarizes the network’s learned features. In population, the implied SDF converges to a ridge-regularized version of the true SDF, with the degree of regularization determined by spectral complexity. Empirically, using U.S. equity data, the PTK representation delivers economically and statistically significant performance gains, while rising spectral complexity imposes tighter limits on finite-sample pricing.</p>

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

<p>张元 / Yuan Zhang Yuan Zhang is an Associate Professor of Finance at Shanghai University of Finance and Economics. His research spans asset pricing, financial intermediation, and machine learning in financial markets. He has published in the Review of Financial Studies and is currently developing AI-driven methods for factor modeling and portfolio optimization, including work on benchmarking large language models in quantitative finance at ICLR 2026. He received his Ph.D. from the Swiss Finance Institute at EPFL and was a visiting Ph.D. student at MIT Sloan.</p>

</details>


### 4. Incorporating Return Prediction in High-Dimensional Mean-Variance Portfolio Optimization

**讲者**：黄睿钊（香港科技大学 · ISOM） · 15:30-16:00

**对应论文**：Incorporating Return Prediction in High-Dimensional Mean-Variance Portfolio Optimization · [DOI](https://doi.org/10.2139/ssrn.5801843)

<details><summary>摘要（会议官网）</summary>

<p>We develop a framework that incorporates return prediction to achieve unconditional mean-variance efficiency in high dimensions. Our method, termed MAXSER-PR, builds upon the seminal “MAXSER” estimator of Ao, Li, and Zheng (2019) by integrating conditional information into the optimization, thereby providing a tractable bridge between conditional return prediction and unconditional mean-variance efficiency. Under an elliptical model for the unpredictable return component that allows for heteroskedasticity, heavy-tailedness and serial dependence, and an elastic net regularity condition, our method asymptotically attains unconditional mean-variance efficiency. We demonstrate that our method delivers superior performance through comprehensive empirical studies across multiple prediction models and high-dimensional settings.</p>

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

<p>Ruizhao Huang is a PhD candidate at The Hong Kong University of Science and Technology (HKUST), supervised by Professors Yingying Li and Xinghua Zheng. His research interests include large portfolio optimization, high-frequency data, empirical asset pricing, and statistical machine learning.</p>

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)
