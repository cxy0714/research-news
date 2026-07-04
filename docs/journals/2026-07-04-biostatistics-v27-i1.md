# Biostatistics — Vol 27  Issue 1  ·  2026-07-04

- 共 1 篇 · Biostatistics
- 目录核对 ⚠️ 疑似漏 20 篇（对照 OpenAlex 21 篇）：10.1093/biostatistics/kxaf052、10.1093/biostatistics/kxag001、10.1093/biostatistics/kxag011、10.1093/biostatistics/kxag004、10.1093/biostatistics/kxag006 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期仅收录一篇论文，主题聚焦于高维成分数据的贝叶斯建模，核心挑战来自婴儿微生物组纵向数据的多重复杂性：重复测量、零膨胀、过度离散与成分性。该文提出贝叶斯函数并发零膨胀Dirichlet-multinomial回归模型，将函数并发框架与零膨胀Dirichlet-multinomial分布结合，同时处理成分结构、零膨胀及时间变化效应，并通过贝叶斯推断实现回归系数的平滑估计。模拟验证了模型在恢复潜在函数关系上的准确性，实际应用则揭示了α多样性与胎龄、母乳喂养比例的正相关。

由于本期仅此一篇，其方法论主线可视为对高维成分数据中零膨胀与时间动态性的统一处理。工具层面，作者提供了R包与Shiny应用，便于方法落地。对于关注贝叶斯非参数、成分数据分析或微生物组统计的研究者，这篇论文是本期唯一且直接相关的阅读对象。

## 其他  *(other, 1 篇)*

### 1. [10.1093/biostatistics/kxag019](https://doi.org/10.1093/biostatistics/kxag019) · [arXiv](https://arxiv.org/abs/2603.26914) — A Bayesian functional concurrent zero-inflated Dirichlet-multinomial regression model with application to infant microbiome
- **作者**: Brody Erlandson, Ander Wilson, Matthew D. Koslovsky
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对婴儿微生物组纵向研究中存在的重复测量、过度离散、成分性、高维参数空间和零膨胀等挑战，提出了一种贝叶斯函数并发零膨胀Dirichlet-multinomial回归模型。该模型能够同时处理成分数据结构和零膨胀问题，并扩展至重复测量设计，以估计协变量对微生物组成的时间变化效应。模型采用函数并发框架，允许回归系数随时间平滑变化，并通过贝叶斯方法进行推断。模拟研究表明，模型能准确恢复潜在的函数关系，并适用于大规模成分空间。应用于11周产后婴儿微生物组数据，发现α多样性（个体内微生物多样性）与较高胎龄和母乳喂养比例正相关。文章还提供了R包和Shiny应用以方便方法实施和可视化。
- **关键技术**: `Dirichlet-multinomial regression`, `zero-inflation`, `functional concurrent model`, `Bayesian inference`, `longitudinal compositional data`
- **为什么对您有用**: 本文属于应用统计方法开发，与您的主要兴趣（因果推断、高维统计、半参理论）无直接交集。但作为流行病学/微生物组数据分析的案例，其处理零膨胀和成分数据的贝叶斯函数回归框架对您了解纵向数据建模有一定参考价值。武器库中'非参数统计'和'高维渐近'可帮助理解其函数回归的平滑性假设，但核心贝叶斯机制与您当前工具链距离较远，属于暂不可做方向。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

