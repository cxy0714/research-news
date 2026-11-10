# EMNLP 2025 · Agent / 工具使用

> 本页 1 篇（该主题共 1 篇），按相关性排序。 [返回总览](../index.md)

### 1. Can LLMs Help You at Work? A Sandbox for Evaluating LLM Agents in Enterprise Environments
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.466/) · [PDF](https://aclanthology.org/2025.emnlp-main.466.pdf)
- **作者**: Harsh Vishwakarma, Ankush Agarwal, Ojas Patil, Chaitanya Devaguptapu, Mahesh Chandran
- **会议/来源**: EMNLP 2025 · Main
- 相关性 8/10 · `benchmark`
- **测什么**: LLM 智能体在企业多源数据、访问控制和跨职能任务中的任务完成能力。
- **摘要**: EnterpriseBench 是一个模拟企业环境的基准，包含 500 个跨软件工程、HR、财务和行政领域的多样化任务。它通过数据源碎片化、访问控制层级和跨职能工作流来捕捉企业关键特征。作者提出了一种新颖的数据生成流程，能从组织元数据中创建内部一致的企业任务。实验表明，最先进的 LLM 智能体任务完成率仅为 41.8%，凸显了企业 AI 系统的改进空间。该基准提供了可复现的评测框架，但未报告人类基线或污染检查。
- **为什么值得看**: 该基准针对企业环境中的复杂评测设计，提供了数据生成流程和任务构造方法，但缺乏人类基线和污染审计，其评测方法学贡献有限。
- **关键技术**: `benchmark construction`, `data generation pipeline`, `task diversity`, `access control simulation`
