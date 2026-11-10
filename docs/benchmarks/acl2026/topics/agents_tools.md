# ACL 2026 · Agent / 工具使用

> 本页 5 篇（该主题共 5 篇），按相关性排序。 [返回总览](../index.md)

### 1. BrowseComp-Plus: A Fair and Disentangled Evaluation Benchmark for Deep Search Agents
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.1023/) · [PDF](https://aclanthology.org/2026.acl-long.1023.pdf)
- **作者**: Zijian Chen, Xueguang Ma, Shengyao Zhuang, Ping Nie, Kai Zou, Sahel Sharifymoghaddam, Andrew Liu, Joshua Green et al.
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `benchmark`
- **测什么**: 深度搜索智能体在多跳查询中的端到端准确率，以及检索器对整体性能的独立贡献。
- **摘要**: BrowseComp-Plus 是一个面向深度搜索智能体的评测基准，从 BrowseComp 派生而来，但将黑盒网页搜索 API 替换为固定且经人工验证的语料库，从而解决公平性和可解耦性问题。该基准包含约 1,266 道多跳问题，并配套一个约 1,000 万文档的固定语料库，支持可控的检索实验。评测结果显示，使用 BM25 检索器时，开源模型 Search-R1 的准确率为 3.86%，而 GPT-5 达到 55.9%；当 GPT-5 搭配 Qwen3-Embedding-8B 检索器时，准确率进一步提升至 70.1%，同时减少了搜索调用次数。该基准的主要方法学贡献在于：通过固定语料库，实现了对智能体端到端性能与检索器贡献的分离测量，并提供了可复现的评测流程。
- **为什么值得看**: 该基准为智能体评测提供了可复现的固定语料库设计，解决了黑盒 API 导致的公平性问题，并首次实现了检索器贡献与智能体能力的解耦测量，对评测方法学具有直接价值。
- **关键技术**: `fixed corpus construction`, `human verification`, `disentangled evaluation`, `retriever contribution analysis`, `reproducibility`

### 2. Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.2192/) · [PDF](https://aclanthology.org/2026.acl-long.2192.pdf)
- **作者**: Preethi Seshadri, Samuel Cahyawijaya, Ayomide Odumakinde, Sameer Singh, Seraphina Goldfarb-Tarrant
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `evaluation_method`
- **测什么**: LLM模拟用户作为人类用户代理在智能体评测中的可靠性、校准性和公平性
- **摘要**: 该论文通过一项覆盖美国、印度、肯尼亚和尼日利亚参与者的用户研究，系统检验了LLM模拟用户作为智能体评测代理的可靠性。研究基于τ-Bench零售任务，比较了LLM模拟用户与真实人类用户在评估智能体性能时的差异。结果发现，模拟用户缺乏稳健性，不同LLM模拟用户导致的智能体成功率差异高达9个百分点；模拟用户系统性校准偏差，低估困难任务成功率而高估中等难度任务；非洲裔美国英语（AAVE）使用者比标准美语（SAE）使用者成功率更低且校准误差更大，且年龄加剧差异；模拟用户对不同人群的代理有效性不同，对AAVE和印度英语人群表现最差。此外，模拟用户引入对话伪影并暴露与人类用户不同的失败模式。该研究揭示了当前评测实践可能误导对智能体能力的评估，并掩盖真实部署挑战。
- **为什么值得看**: 该论文为LLM-as-user代理评测提供了系统性的效度检验，揭示了模拟用户在不同人群中的测量偏差和校准问题，对评测方法学中代理有效性（proxy validity）和人群公平性具有重要参考价值。
- **关键技术**: `user study`, `LLM-simulated users`, `calibration analysis`, `cross-population fairness`, `proxy validity`

### 3. A Functionality-Grounded Benchmark for Evaluating Web Agents in E-commerce Domains
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.68/) · [PDF](https://aclanthology.org/2026.acl-long.68.pdf)
- **作者**: Xianren Zhang, Shreyas Prasad, Di Wang, Qiuhai Zeng, Suhang Wang, Wenbo Yan, Mat Hans
- **会议/来源**: ACL 2026 · Long
- 相关性 8/10 · `benchmark`
- **测什么**: 网页智能体在电商任务上的任务完成性能与操作安全性（如误购、误删等风险）。
- **摘要**: Amazon-Bench 是一个面向电商领域网页智能体的新基准，旨在弥补现有基准只关注商品搜索、忽略账户管理/礼品卡等真实功能以及忽视操作安全性的两大缺陷。数据生成管线利用网页内容和交互元素（按钮、复选框等）自动构造覆盖地址管理、心愿单、品牌关注等多样化、功能导向的用户查询。评测框架同时评估智能体的任务完成性能与安全性（如误购、误删地址、错误配置自动充值等风险）。作者系统评测了多个现有智能体，发现它们在复杂查询上表现不佳且存在安全风险。该基准提供了可复用的数据生成与安全评测流程，对网页智能体评测方法学有直接贡献。
- **为什么值得看**: 该论文提出了一个功能导向的基准构造流程（基于网页交互元素生成查询）和同时评估性能与安全性的自动化评测框架，为网页智能体评测提供了可复用的方法论，特别是对安全失败模式的测量设计。
- **关键技术**: `benchmark construction`, `data generation pipeline`, `safety evaluation`, `web agent evaluation`

### 4. ACIArena: Toward Unified Evaluation for Agent Cascading Injection
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.457/) · [PDF](https://aclanthology.org/2026.acl-long.457.pdf)
- **作者**: Hengyu An, Minxi Li, Jinghuai Zhang, Naen Xu, Chunyi Zhou, Changjiang Li, Xiaogang Xu, Tianyu Du et al.
- **会议/来源**: ACL 2026 · Long
- 相关性 8/10 · `benchmark`
- **测什么**: 多智能体系统对级联注入攻击的鲁棒性，涵盖指令劫持、任务破坏和信息窃取等失败模式。
- **摘要**: ACIArena 提出一个统一框架，用于评估多智能体系统（MAS）对 Agent Cascading Injection（ACI）攻击的鲁棒性。它覆盖多个攻击面（外部输入、智能体画像、智能体间消息）和攻击目标（指令劫持、任务破坏、信息窃取），并建立统一规范以支持 MAS 构建和攻防模块。基准包含 1,356 个测试用例，覆盖六种广泛使用的 MAS 实现。评测结果显示，仅凭拓扑结构评估鲁棒性不足，需要刻意设计角色和控制交互模式；此外，在简化环境中开发的防御在真实场景中往往失效，窄范围的防御甚至可能引入新漏洞。该工作为 MAS 设计原则的深入探索提供了基础。
- **为什么值得看**: 该论文系统化地构建了多攻击面、多目标的鲁棒性评测套件，并揭示了简化环境与真实环境之间的防御迁移差距，对评测方法学中关于生态效度和构念覆盖的讨论有直接价值。
- **关键技术**: `benchmark construction`, `attack surface taxonomy`, `defense transfer analysis`, `unified specification`

### 5. AgentGym2: Benchmarking Large Language Model Agents in De-Idealized Real-World Environments
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.2058/) · [PDF](https://aclanthology.org/2026.acl-long.2058.pdf)
- **作者**: Zhiheng Xi, Dingwen Yang, Jiaqi Liu, Jixuan Huang, Honglin Guo, Baodai Huang, Tinggang Chen, Qi Zhang et al.
- **会议/来源**: ACL 2026 · Long
- 相关性 8/10 · `benchmark`
- **测什么**: 智能体在噪声和欠指定信息下的端到端任务执行、工具探索与组合能力。
- **摘要**: AgentGym2 提出了一个面向真实世界端到端工作需求的智能体评测框架，旨在弥补现有 benchmark 在理想化设定下的不足。它包含基于真实工作需求构造的任务实例，强调执行端到端流程、通过探索发现工具、为未见任务组合工具，以及对噪声和欠指定信息的鲁棒性。实验覆盖 15 个专有和开源模型，结果显示包括 Gemini 和 GPT-5 在内的 SOTA 系统也表现挣扎，揭示了当前智能体能力与现实应用需求之间的显著差距。该工作还提供了对任务难度和模型表现的详细分析，但未明确报告污染检查或人类基线。
- **为什么值得看**: 该工作直接回应了评测方法学中的生态效度问题，通过去理想化环境设计（噪声、欠指定输入、工具探索）提供了可复用的任务构造思路，并揭示了现有 benchmark 低估真实部署难度的系统性偏差。
- **关键技术**: `benchmark construction`, `task design`, `tool discovery`, `robustness evaluation`, `human baseline`
