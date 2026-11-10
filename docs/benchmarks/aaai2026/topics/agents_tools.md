# AAAI 2026 · Agent / 工具使用

> 本页 4 篇（该主题共 4 篇），按相关性排序。 [返回总览](../index.md)

### 1. D-GARA: A Dynamic Benchmarking Framework for GUI Agent Robustness in Real-World Anomalies
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38795) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38795/42757)
- **作者**: Sen Chen, Tong Zhao, Yi Bin, Fei Ma, Wenqi Shao, Zheng Wang
- **会议/来源**: AAAI 2026 · Track 21
- 相关性 8/10 · `benchmark`
- **测什么**: GUI 代理在真实世界异常（如权限对话框、电池警告）下的任务完成鲁棒性。
- **摘要**: D-GARA 是一个动态评测框架，用于评估 Android GUI 代理在真实世界异常环境中的鲁棒性。它引入了一组常见的异常类型，如权限对话框、电池警告和更新提示，并基于此构建了一个包含常用 Android 应用且嵌入异常的基准数据集。实验表明，最先进的 GUI 代理在异常丰富的环境中性能显著下降，凸显了鲁棒性感知学习的必要性。该框架是模块化和可扩展的，支持集成新任务、异常类型和交互场景。
- **为什么值得看**: 该工作针对现有 GUI 基准静态、理想化的问题，提出了动态异常注入的评测方法，为评测代理在非理想条件下的鲁棒性提供了可复用的框架，对评测方法学有直接贡献。
- **关键技术**: `dynamic benchmark construction`, `anomaly injection`, `modular framework`, `robustness evaluation`

### 2. Towards Autonomous UAV Visual Object Search in City Space: Benchmark and Agentic Methodology
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38898) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38898/42860)
- **作者**: Yatai Ji, Zhengqiu Zhu, Yong Zhao, Beidan Liu, Chen Gao, Yihao Zhao, Sihang Qiu, Yue Hu et al.
- **会议/来源**: AAAI 2026 · Track 22
- 相关性 8/10 · `benchmark`
- **测什么**: 无人机在复杂城市环境中基于视觉输入自主搜索静态目标的成功率与效率
- **摘要**: 本文提出 CityAVOS，首个面向城市静态目标自主搜索的无人机视觉搜索基准，包含 2,420 个任务、6 类目标，并设计了不同难度等级以评估搜索策略。同时提出 PRPSearcher 智能体方法，利用多模态大模型构建三种地图（语义、认知、不确定性）并引入去噪机制和提示机制，在成功率（+37.69%）和搜索效率（SPL +28.96%，MSS -30.69%，NE -46.40%）上显著优于基线。基准的难度校准和任务多样性设计值得关注，但未报告人类基线或污染检查。
- **为什么值得看**: 该基准提供了针对具身视觉搜索任务的难度分级和任务构造流程，可作为评估智能体在长时程、探索-利用权衡场景下能力的参考，但缺乏对评测方法学（如人类基线、污染控制）的深入验证。
- **关键技术**: `benchmark construction`, `difficulty calibration`, `agentic evaluation`, `multi-modal LLM`

### 3. Who Is Helping Whom? Analyzing Inter-Dependencies to Evaluate Cooperation in Human-AI Teaming
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38787) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38787/42749)
- **作者**: Upasana Biswas, Vardhan Palod, Siddhant Bhambri, Subbarao Kambhampati
- **会议/来源**: AAAI 2026 · Track 21
- 相关性 8/10 · `evaluation_method`
- **测什么**: 人机团队中智能体与人类动作之间的相互依赖程度，即协作质量。
- **摘要**: 该论文提出“建设性相互依赖”（constructive interdependence）作为评估人机协作质量的新指标，弥补了仅用任务奖励评估的不足。作者在STRIPS框架下基于动作交互定义依赖度，并在Overcooked环境中将SOTA智能体与学习的人类模型及真实人类配对，进行用户研究。结果显示，尽管这些智能体任务奖励高，但相互依赖度持续偏低，表明它们未能诱导真正的协作行为；且团队绩效与任务奖励并不必然相关。论文提供了可复用的协作评估方法，并揭示了任务奖励作为协作代理指标的局限性。
- **为什么值得看**: 该论文对评测方法学的价值在于：提出了一种不依赖主观报告、可计算的协作质量指标（相互依赖度），并实证展示了任务奖励与协作质量之间的脱节，为多智能体/人机协作评测提供了新的构念覆盖和验证流程。
- **关键技术**: `constructive interdependence`, `STRIPS formalism`, `human-agent teaming`, `user study`, `task reward comparison`

### 4. SoMe: A Realistic Benchmark for LLM-based Social Media Agents
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37113) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37113/41075)
- **作者**: Dizhan Xue, Jing Cui, Shengsheng Qian, Chuanrui Hu, Changsheng Xu
- **会议/来源**: AAAI 2026 · Track 2
- 相关性 7/10 · `benchmark`
- **测什么**: 社交智能体在真实社交媒体环境中的多步任务执行、用户行为理解和决策能力
- **摘要**: SoMe 是一个面向 LLM 社交智能体的评测基准，旨在评估智能体在真实社交媒体环境中理解内容、用户行为并做出复杂决策的能力。基准包含 8 个任务、916 万条帖子、6591 个用户画像和 25686 份报告，并配有 17869 条人工标注的查询。任务设计覆盖了信息检索、用户分析、内容生成等典型社交场景，数据来自多个平台和外部网站，强调真实性和多样性。评测发现当前主流闭源和开源 LLM 在社交智能体任务上表现均不理想，揭示了模型在长上下文推理、多步工具调用和用户意图理解方面的不足。该基准提供了首个系统性的社交智能体评测平台，并附带详细的定量与定性分析。
- **为什么值得看**: 该基准在任务设计上强调真实性和生态效度，并提供了大规模人工标注数据，可作为社交智能体评测的参考标准；其揭示的模型局限有助于理解现有评测的覆盖缺口和难度校准问题。
- **关键技术**: `benchmark construction`, `human annotation`, `task diversity`, `realistic environment simulation`, `quantitative and qualitative analysis`
