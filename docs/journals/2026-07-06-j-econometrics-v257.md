# J. Econometrics — Vol 257  ·  2026-07-06

- 共 1 篇 · Journal of Econometrics
- 目录核对 ⚠️ 疑似漏 3 篇（对照 OpenAlex 4 篇）：10.1016/j.jeconom.2026.106271、10.1016/j.jeconom.2026.106273、10.1016/j.jeconom.2026.106274

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Journal of Econometrics》第257卷仅收录一篇论文，主题高度聚焦于网络数据的假设检验。整体来看，本期围绕稀疏网络下的模型诊断展开，核心主线是**高维稀疏网络的拟合优度检验**，涉及极值统计量、抽样机制与bootstrap校正等工具。

该篇论文针对稀疏随机块模型（SBM）提出一种拟合优度检验，其核心创新在于通过邻接矩阵最大条目偏差的抽样构造来缓解稀疏性对极值统计量的影响。理论部分同时给出了零假设下的渐近分布（收敛到Type-I极值分布）和备择假设下的渐近势，并引入bootstrap校正以改进有限样本表现。方法还扩展至degree-corrected SBM，并通过模拟和两个实证（涵盖稠密与稀疏网络）验证了有效性。该工作直接连接了**高维稀疏网络**与**假设检验**两个方向，适合关注网络数据分析、模型诊断或极值统计理论的研究者优先阅读。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1016/j.jeconom.2026.106276](https://doi.org/10.1016/j.jeconom.2026.106276) · [arXiv](https://arxiv.org/abs/2503.11990) — A goodness-of-fit test for sparse networks
- **作者**: Yujia Wu, Wei Lan, Long Feng, Chih-Ling Tsai
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 257 · pp 106276
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 针对稀疏网络（连接概率为 O(log n/n) 且社区数发散）下随机块模型（SBM）的拟合优度检验问题，提出一种基于邻接矩阵最大条目偏差抽样构造的检验统计量。核心机制是通过抽样过程缓解网络稀疏性对极值统计量的负面影响，使统计量在零假设下收敛到 Type-I 极值分布，且收敛性不依赖网络结构。理论贡献包括：推导了零假设下的渐近分布、备择假设下的渐近势，并引入 bootstrap 校正以改进有限样本表现，以及增广检验统计量以提高势。方法扩展至 degree-corrected SBM。模拟和两个实证（含稠密与稀疏网络）验证了方法的有效性。该工作直接连接您对 hypothesis testing 和 high-dimensional statistics 的兴趣，特别是稀疏设定下极值统计量的渐近理论，可用您熟悉的 minimax bounds 视角评估其检验势的最优性。
- **关键技术**: `extreme value distribution`, `bootstrap-corrected test`, `maximum entry-deviation`, `stochastic block model`, `sparse network asymptotics`
- **为什么对您有用**: 连接 hypothesis testing 中稀疏高维设定下的检验问题，具体是 SBM 拟合优度检验在连接概率 O(log n/n) 且社区数发散时的渐近理论。您可以用 very_familiar 的 minimax bounds 工具分析该检验的势是否达到最优（例如与稀疏网络下社区检测的信息论下界对比），这是立即可做的 follow-up。此外，该文的抽样构造思路可能启发您在高维 U-statistics 中处理稀疏性。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

