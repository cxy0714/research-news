# AAAI 2026 · 安全 / 事实性

> 本页 1 篇（该主题共 1 篇），按相关性排序。 [返回总览](../index.md)

### 1. An LLM-based Quantitative Framework for Evaluating High-Stealthy Backdoor Risks in OSS Supply Chains
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37116) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37116/41078)
- **作者**: Zihe Yan, Kai Luo, Haoyu Yang, Yang Yu, Zhuosheng Zhang, Guancheng Li
- **会议/来源**: AAAI 2026 · Track 2
- 相关性 6/10 · `evaluation_method`
- **测什么**: 开源软件供应链中高隐蔽性后门攻击的多阶段风险水平
- **摘要**: 该论文提出一个基于LLM的量化框架，用于评估开源软件供应链中的高隐蔽性后门风险。框架从攻击者视角建模后门攻击的各个阶段，并为每个阶段定义针对性指标，同时利用LLM对代码仓库进行语义评估，以弥补静态分析在评估维护活动可靠性（如提交者权限提升、审查参与度）方面的不足。在Debian生态系统的66个高优先级软件包上验证了框架的有效性，结果显示当前开源供应链存在一系列安全风险。方法学贡献在于将后门风险评估转化为可量化的多阶段指标，并引入LLM作为语义分析工具，但缺乏对LLM评估结果与人工审计的一致性验证。
- **为什么值得看**: 该框架展示了如何将LLM用于安全领域的结构化风险评估，并定义了可复用的攻击阶段指标，对评测方法学中'构念操作化'和'自动化评估验证'有参考价值，但未提供LLM判断的可靠性分析。
- **关键技术**: `LLM-as-judge`, `risk assessment framework`, `semantic code analysis`, `attack stage modeling`
