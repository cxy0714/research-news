# Nat. Methods — Vol 23  Issue 2  ·  2026-08-01

- 共 8 篇 · Nature Methods
- 目录核对 ⚠️ 疑似漏 23 篇（对照 OpenAlex 31 篇）：10.1038/s41592-025-02980-0、10.1038/s41592-025-02981-z、10.1038/s41592-025-02974-y、10.1038/s41592-025-02926-6、10.1038/s41592-025-02918-6 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Nature Methods》整体上以**计算生物学工具与实验方法**为主，统计方法学贡献较少。论文可归为三条主线：**单细胞与空间组学分析框架**（pertpy、cellSTAAR）、**生物图像与结构预测的深度学习**（CELTIC、OpenStructure基准测试）、以及**实验技术与报告标准**（谷氨酸指示剂、神经类器官筛选、MIHCLE标准）。此外，还有一篇跨物种知识转移的综述。

在**单细胞与空间组学**主线上，pertpy 提供了一个模块化框架，整合了扰动数据的元数据注释和距离计算，填补了现有方法缺乏统一分析平台的空白；cellSTAAR 则聚焦于罕见变异关联检验，通过整合单细胞ATAC-seq数据构建细胞类型特异的功能注释，并用omnibus框架处理cCRE-基因连接的不确定性，直接服务于大规模WGS队列（如TOPMed、UK Biobank）的非编码区关联分析。这两篇分别从分析框架和统计检验两个角度推进了单细胞数据的实用化。

在**生物图像与结构预测**主线上，CELTIC 通过显式编码细胞上下文（如有丝分裂状态、群落位置）作为条件输入，提升了无标记显微镜图像中细胞器荧光标记的跨分布泛化能力，属于条件生成模型在生物图像中的应用；OpenStructure基准测试则针对蛋白质复合物结构预测，提出了适用于大型系统的三级、四级结构及界面评分策略，强调计算可扩展性，并集成到开源框架中。这两篇都涉及高维数据（图像、结构）的定量比较与泛化问题。

对于因果推断、半参数效率、高维统计方向的研究者，本期最相关的论文是 **cellSTAAR**（罕见变异关联检验中的功能注释整合与不确定性处理）和 **pertpy**（扰动分析的标准化框架，可能涉及因果对比）。其余论文多为实验技术或综述，与核心统计兴趣无直接方法学关联。

## 其他  *(other, 8 篇)*

### 1. [10.1038/s41592-025-02909-7](https://doi.org/10.1038/s41592-025-02909-7) — Pertpy: an end-to-end framework for perturbation analysis
- **作者**: Lukas Heumos, Yuge Ji, Lilly May, Tessa D. Green, Stefan Peidli, Xinyue Zhang et al.
- **期刊/来源**: Nature Methods
- **机构**: Helmholtz Zentrum München · German Center for Lung Research · Technical University of Munich · Broad Institute · Dana-Farber/Harvard Cancer Center · Humboldt-Universität zu Berlin · European Molecular Biology Laboratory · Charité - Universitätsmedizin Berlin 等
- **分类**: vol 23 · issue 2 · pp 350-359
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文介绍 pertpy，一个基于 Python 的模块化框架，用于大规模单细胞扰动实验的端到端分析。该框架整合了多种扰动数据集与元数据库，并提供了多种已建立和新型方法的快速实现，包括自动元数据注释和扰动距离计算。作为 scverse 生态系统的一部分，pertpy 与现有单细胞分析库互操作，并易于扩展。当前方法多聚焦于差异比较或特定任务，缺乏可扩展且融入生物学上下文的统一分析框架。pertpy 填补了这一空白，为统计学家和计算生物学家提供了一个标准化、可复用的分析平台。对您而言，本文属于 Nature Methods 的通用科学阅读，虽不直接涉及您的主要统计兴趣（因果推断、高维统计等），但作为了解单细胞扰动数据分析生态的入门读物，有助于拓宽跨学科视野。
- **关键技术**: `single-cell perturbation analysis`, `modular framework`, `metadata annotation`, `perturbation distance`, `scverse ecosystem`
- **为什么对您有用**: 本文属于通用科学（Nature Methods）的 gateway reading，适合作为单细胞扰动数据分析领域的入门读物。武器库中的软件开发和非参数统计经验可帮助理解其框架设计，但本文不涉及您核心的统计理论或方法创新，属于暂不可做的领域拓展阅读。

### 2. [10.1038/s41592-025-02919-5](https://doi.org/10.1038/s41592-025-02919-5) — cellSTAAR: incorporating single-cell-sequencing-based functional data to boost power in rare variant association testing of noncoding regions
- **作者**: Eric Van Buren, Yi Zhang, Xihao Li, Margaret Sunitha Selvaraj, Zilin Li, Hufeng Zhou et al.
- **期刊/来源**: Nature Methods
- **机构**: Harvard University · Duke University · Duke Cancer Institute · University of North Carolina at Chapel Hill · Broad Institute · Massachusetts General Hospital · Northeast Normal University · Wake Forest University 等
- **分类**: vol 23 · issue 2 · pp 338-349
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文提出 cellSTAAR，一种整合全基因组测序（WGS）与单细胞 ATAC-seq 数据的罕见变异关联检验方法，目标是非编码区候选顺式调控元件（cCRE）的罕见变异关联检验。核心挑战在于 cCRE 的调控功能在不同细胞类型间高度异质，且 cCRE-基因连接存在不确定性。方法上，cellSTAAR 利用单细胞染色质可及性数据构建细胞类型特异的功能注释和变异集合，并通过一个整合多种流行连接方法的 omnibus 框架来反映 cCRE-基因连接的不确定性。在 TOPMed Freeze 8（N≈60,000）和 UK Biobank（N≈190,000）的四个血脂表型（LDL、高 LDL 二值变量、HDL、甘油三酯）上进行了应用和复制验证。模拟和真实数据分析表明，cellSTAAR 能提升非编码区罕见变异关联检验的统计功效并改善结果的可解释性。这是一篇应用导向的方法学论文，对您作为统计研究者的直接方法学迁移价值有限，但可作为了解单细胞数据与罕见变异关联分析交叉领域的入门读物。
- **关键技术**: `rare variant association testing`, `single-cell ATAC-seq`, `functional annotation`, `omnibus test`, `cCRE-gene linking`
- **为什么对您有用**: 本文属于 general science 范畴（Nature Methods），作为 gateway reading 来看：(a) 对单细胞数据和罕见变异关联分析的外行读者较为友好，但需要一定遗传学背景；(b) 清晰阐述了科学问题（非编码区调控元件的细胞类型特异性功能注释如何提升检验功效）；(c) 有真实的数据分析维度（WGS 数据整合、功能注释构建、多重检验校正），但统计方法本身（omnibus test）较为常规；(d) 作为 Nature Methods 文章，适合拓宽知识面。武器库中无直接可攻的口子，属于暂不可做范畴——核心机器（罕见变异关联检验的统计遗传学工具）不在武器库中。

### 3. [10.1038/s41592-025-02931-9](https://doi.org/10.1038/s41592-025-02931-9) · [arXiv](https://arxiv.org/abs/2408.08503) — Computational strategies for cross-species knowledge transfer
- **作者**: Hao Yuan, Christopher A. Mancuso, Kayla Johnson, Ingo Braasch, Arjun Krishnan
- **期刊/来源**: Nature Methods
- **机构**: Evolutionary Genomics (United States) · University of Colorado Anschutz Medical Campus
- **分类**: vol 23 · issue 2 · pp 312-327
- 相关性 7/10 · novelty: `survey`
- **摘要**: 本文是一篇综述性 Perspective，系统回顾了跨物种知识转移的计算方法，主要聚焦于利用转录组数据和分子网络的方法。文章覆盖四个关键领域：(1) 跨物种疾病和基因注释知识转移，(2) 功能等效分子组分的识别，(3) 等效扰动基因或基因集的推断，(4) 等效细胞类型的识别。文中提出了‘agnology’概念，即基于数据驱动的功能等效性，不依赖于进化起源。文章最后讨论了未来方向和关键挑战。作为 Nature Methods 的综述，本文对统计学家而言是了解计算生物学中跨物种分析问题的入门读物，但本身不提出新的统计方法或理论。
- **关键技术**: `cross-species knowledge transfer`, `transcriptome data analysis`, `molecular network analysis`, `functional equivalence`, `agnology`
- **为什么对您有用**: 本文属于 general science 范畴的 gateway reading，适合作为统计学家了解计算生物学中跨物种分析问题的入门材料。文章清晰阐述了数据层面（转录组、分子网络）和模型层面（功能等效性推断）的问题，但未涉及研究者武器库中的具体工具（如因果推断、高维统计、U-统计量等）。作为 Nature Methods 的综述，值得花时间阅读全文以拓宽视野，但暂不可做后续方法学跟进——核心问题（功能等效性推断的统计框架）不在当前武器库中。

### 4. [10.1038/s41592-025-02960-4](https://doi.org/10.1038/s41592-025-02960-4) — Cell context-dependent in silico organelle localization in label-free microscopy images
- **作者**: Nitsan Elmalam, Assaf Zaritsky
- **期刊/来源**: Nature Methods
- **机构**: Ben-Gurion University of the Negev
- **分类**: vol 23 · issue 2 · pp 405-416
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文提出 CELTIC，一种基于细胞上下文（cell context）的深度学习模型，用于从无标记显微镜图像中预测细胞器荧光标记（in silico labeling）。核心问题是：当细胞类型、分裂状态或群落位置等上下文变化导致图像分布偏移（out-of-distribution）时，传统模型预测性能严重下降。CELTIC 通过显式编码生物学有意义的上下文信息（如细胞是否处于有丝分裂、是否在群落边缘）作为模型条件输入，增强了跨上下文泛化能力。方法上采用条件生成架构，利用生物先验（biological priors）引导模型学习上下文与细胞器组织的关联。实验表明，CELTIC 在多种分布外场景（如有丝分裂细胞、群落边缘细胞）下显著优于基线模型，并能生成单细胞在不同上下文间的过渡图像，以克服细胞间变异性。该工作为构建通用化的 in silico labeling 基础模型提供了路径，但方法学上属于应用型深度学习，未涉及新的统计推断理论。对您而言，这是一篇 Nature Methods 的 gateway reading，展示了生物图像分析中如何利用领域知识处理分布偏移，但方法学 novelty 有限，不直接涉及因果推断或高维统计等核心兴趣。
- **关键技术**: `in silico labeling`, `conditional deep learning`, `out-of-distribution generalization`, `biological priors`, `label-free microscopy`
- **为什么对您有用**: 本文属于 general science（Nature Methods）的 gateway reading，适合作为生物图像分析领域的入门读物。文章清晰阐述了数据分布偏移问题及利用生物上下文解决该问题的思路，但方法学上以工程应用为主，不涉及您核心兴趣中的因果推断、高维统计或效率理论。武器库中的工具（如非参数统计、高维渐近）与此文无直接接口，暂不可做 follow-up。作为跨领域阅读，值得花时间了解生物图像分析中的典型数据结构和建模挑战，但无需深入技术细节。

### 5. [10.1038/s41592-025-02973-z](https://doi.org/10.1038/s41592-025-02973-z) — A fully automated benchmarking suite to compare macromolecular complexes
- **作者**: Gabriel Studer, Xavier Robin, Stefan Bienert, Janani Durairaj, Peter Škrinjar, Gerardo Tauriello et al.
- **期刊/来源**: Nature Methods
- **机构**: SIB Swiss Institute of Bioinformatics · University of Basel
- **分类**: vol 23 · issue 2 · pp 387-394
- 相关性 5/10 · novelty: `survey`
- **摘要**: 本文综述了蛋白质复合物结构预测的基准测试方法，重点讨论了在AI方法兴起后，如何对大型、复杂的生物大分子复合物进行自动化、无监督的评分。作者指出了现有评分方法在处理冷冻电镜等实验解析的大尺寸结构时的局限性，并提出了针对三级结构、四级结构、蛋白质-蛋白质界面和蛋白质-配体复合物的更合适的评分策略。这些新方法在设计上注重计算可扩展性，能够高效评估大型系统。所有工具均已集成到开源软件OpenStructure的结构基准测试框架中。本文属于方法学综述与工具开发，而非提出新的统计理论。对于您而言，这是一篇优秀的入门级阅读材料，展示了结构生物学领域对大规模、高维数据（如冷冻电镜密度图）进行定量比较的实际需求，但其中涉及的评分函数和比对算法与您的主要统计研究方向（因果推断、高维统计）无直接技术交集。
- **关键技术**: `structure comparison scoring`, `protein complex benchmarking`, `cryo-EM data analysis`, `scalable evaluation metrics`
- **为什么对您有用**: 本文属于Nature Methods上的方法学综述，可作为gateway reading了解结构生物学中大规模数据（冷冻电镜）的定量评估问题。您的武器库中的非参数统计和软件工程经验可用于理解其评分框架，但核心问题（结构比对算法）与您的主要研究方向（因果推断、高维统计）无直接技术迁移点。本文值得一读以拓宽视野，但暂不可做后续研究。

### 6. [10.1038/s41592-025-02927-5](https://doi.org/10.1038/s41592-025-02927-5) — Systematic scRNA-seq screens profile neural organoid response to morphogens
- **作者**: Fátima Sanchís-Calleja, Nadezhda Azbukina, Akanksha Jain, Zhisong He, Ryoko Okamoto, Charlotte Rusimbi et al.
- **期刊/来源**: Nature Methods
- **机构**: ETH Zurich · University of Copenhagen · Novo Nordisk Foundation · Roche (Switzerland) · University of Basel
- **分类**: vol 23 · issue 2 · pp 465-478
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文利用多重单细胞转录组筛选技术，系统研究了形态发生素对人类神经类器官区域特化的影响。作者通过改变形态发生素的时机、浓度和组合，发现这些参数强烈影响类器官的细胞类型和区域组成，且细胞系和神经诱导方法也会改变响应。研究在微流控芯片中施加浓度梯度或在多孔板中增加静态浓度，观察到不同的模式形成动力学。结合深度学习模型，本文提供了一个详细的神经谱系特化资源，可用于预测人类干细胞系统中的分化结果。这是一篇以实验和资源为主的生物学论文，方法学贡献有限，主要价值在于数据集和实验设计。
- **关键技术**: `single-cell RNA-seq`, `multiplexed screening`, `neural organoids`, `microfluidic gradient`, `deep learning prediction`
- **为什么对您有用**: 本文属于一般科学（Nature Methods）范畴，作为入门读物： (a) 对统计学家友好，实验设计和数据生成过程描述清晰，但需要一定发育生物学背景； (b) 科学问题明确——形态发生素如何调控神经区域化，但更偏向生物学机制而非统计方法； (c) 数据维度（单细胞转录组）和建模（深度学习预测分化结果）有统计趣味，但方法本身是标准工具； (d) 作为跨学科阅读有价值，但武器库中无直接可攻问题。暂不可做——核心是实验生物学，统计方法已成熟，缺乏需要新理论或计算工具的具体口子。

### 7. [10.1038/s41592-025-02965-z](https://doi.org/10.1038/s41592-025-02965-z) — Glutamate indicators with increased sensitivity and tailored deactivation rates
- **作者**: Abhi Aggarwal, Adrian Negrean, Yang Chen, Rishyashring Iyer, Daniel Reep, Anyi Liu et al.
- **期刊/来源**: Nature Methods
- **机构**: Howard Hughes Medical Institute · University of Calgary · Janelia Research Campus · Allen Institute · Allen Institute for Neural Dynamics · Libin Cardiovascular Institute of Alberta · Munich Cluster for Systems Neurology · University of California San Diego 等
- **分类**: vol 23 · issue 2 · pp 417-425
- 相关性 2/10 · novelty: `application`
- **摘要**: 该论文开发了第四代荧光蛋白谷氨酸指示剂 iGluSnFR4f 和 iGluSnFR4s，分别针对快速动力学追踪和大规模突触群体记录进行了优化。通过蛋白质工程改造，这些变体在保持高空间特异性的同时，实现了单囊泡水平的体内灵敏度。作者在小鼠皮层1-4层、海马CA1区和中脑等脑区进行了双光子成像和光度测量验证，展示了其记录自然突触传递模式的能力。该工作主要贡献在于生物传感器性能的提升（灵敏度、速度、可扩展性），而非统计方法学创新。对于统计研究者而言，本文可作为神经科学成像数据生成过程的入门读物，了解高维时空数据的噪声结构和实验设计。但论文本身不涉及新的统计推断或计算方法，与主要研究兴趣无直接关联。
- **关键技术**: `protein engineering`, `fluorescence imaging`, `two-photon microscopy`, `photometry`
- **为什么对您有用**: 本文属于 Nature Methods 的通用科学论文，作为 gateway reading 评估：(a) 对神经科学外行较友好，但需一定生物学背景理解指示剂设计；(b) 清晰阐述了神经科学中监测突触传递的科学问题；(c) 数据维度（时空成像）对统计学家有一定趣味性，但未深入讨论噪声模型或推断问题；(d) 作为跨学科阅读可拓宽视野，但方法学转移价值有限。武器库中无直接可攻工具，暂不可做。

### 8. [10.1038/s41592-025-02862-5](https://doi.org/10.1038/s41592-025-02862-5) — A Minimum Information about a High Containment Laboratory Experiment (MIHCLE) reporting standard
- **作者**: Jonathan Ewbank, Bernadett Pályi, Åsa Szekely Björndal, Romain David, József Pete, Kurt Zatloukal
- **期刊/来源**: Nature Methods
- **机构**: European Research Council · Association des Operateurs Postaux Publics Europeens · Institut National de Santé Publique · National Public Health and Medical Officer Service · Public Health Agency of Sweden · Government of Hungary · Medical University of Graz
- **分类**: vol 23 · issue 2 · pp 277-283
- 相关性 1/10 · novelty: `survey`
- **摘要**: 本文提出了一项针对高等级生物安全实验室（BSL-3/BSL-4）实验报告的最低信息标准（MIHCLE）。该标准旨在规范涉及高致病性病原体实验的报道内容，涵盖实验设计、病原体信息、安全措施、数据记录等关键要素。文章以评论形式发表在Nature Methods上，主要面向生物安全领域的研究人员和实验室管理者。文中并未涉及任何统计方法、数据建模或计算技术，而是聚焦于实验报告的标准化和可重复性。对于统计研究者而言，本文不包含可迁移的方法学内容，但可作为了解生物安全实验数据报告规范的入门读物。
- **为什么对您有用**: 本文属于general science（Nature Methods）的gateway reading范畴，但完全不涉及统计方法或数据建模。作为入门读物，它清晰阐述了高等级生物安全实验的报告需求，但缺乏统计研究者感兴趣的推断、估计或不确定性量化维度。武器库中的任何工具均无法直接应用于本文内容，因此不值得花时间全文阅读。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

