# Nat. Methods — Vol 23  Issue 9  ·  2026-10-13

- 共 12 篇 · Nature Methods
- 目录核对 ⚠️ 疑似漏 25 篇（对照 OpenAlex 37 篇）：10.1038/s41592-025-02948-0、10.1038/s41592-025-02871-4、10.1038/s41592-026-03037-6、10.1038/s41592-026-03055-4、10.1038/s41592-026-03174-y 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Nature Methods》整体上以**生物医学成像与空间组学技术**为主线，辅以**蛋白质结构预测与冷冻电镜方法**的工程改进，统计方法本身并非核心贡献，但多篇论文的数据生成流程与高维图像/序列分析为统计学家提供了新的应用场景。按主题可聚为三条主线：一是**空间组学与多模态整合**（SACCELERATOR、Spl-ISO-Seq2、REDCAT、PASTA），二是**蛋白质与单分子分析**（ProteinDPO、Iterative Mapping of tau proteoforms、nanocrates），三是**大规模基准测试与模型行为研究**（Kaggle挑战赛、BioVFM、GHT-SELEX）。其余如电压成像与AI综述属于技术展示，统计含量有限。

最值得展开的是**空间组学与多模态整合**这条主线。SACCELERATOR 直接挑战现有基准方法，指出人工注释作为金标准的偏差，并提出共识引导的工作流，用描述性空间指标识别高熵区域——这实质上是将不确定性量化引入聚类评估，对空间统计的误差传播有参考价值。Spl-ISO-Seq2 则从技术端推进，将条形码容量提升三个数量级，并强调区域无关分析能发现区域比较遗漏的异构体模式，暗示了空间异质性检验的统计功效问题。REDCAT 与 PASTA 均聚焦多模态数据对齐与信号放大，前者整合拉曼光谱与免疫荧光，后者兼容蛋白与核酸共检测，两者都依赖计算流程处理高维图像配准，但未提出新统计模型。这条主线的共性问题是：**如何在高维、低信噪比、且存在技术伪影的空间数据中做可靠的推断**，统计学家可关注其数据预处理与误差来源建模。

另一条突出主线是**蛋白质生成模型与实验适应度对齐**。ProteinDPO 将直接偏好优化引入结构条件蛋白语言模型，用稳定/不稳定序列对构造偏好数据，微调后生成更可能稳定的蛋白——这本质上是将排序损失用于生成模型的强化学习对齐，与因果推断中的策略优化有形式上的相似性。Iterative Mapping of tau proteoforms 则处理单分子级蛋白质组数据，用迭代荧光标记实现百万级分子并行检测，其统计贡献在于对低丰度（0.1%）信号的可靠量化与变异系数控制，涉及极端值处理与多重比较问题。nanocrates 解决冷冻电镜的气-液界面伪影，属于样品制备的工程创新，但为后续结构解析提供了更干净的输入数据，间接影响后续三维重构的统计质量。

若按主题筛选，与**因果推断、半参数效率或高维统计**最贴近的优先阅读顺序为：SACCELERATOR（空间聚类中的金标准偏差与不确定性评估）、ProteinDPO（偏好优化与生成模型对齐，可类比因果效应中的策略学习）、BioVFM（大规模模型缩放行为，涉及高维表征的泛化分析）。其余如Kaggle挑战赛的过度拾取容忍性分析、GHT-SELEX的内在序列特异性测量，虽非统计方法创新，但提供了真实数据生成过程的细节，适合作为方法验证的基准案例。

## 其他  *(other, 12 篇)*

### 1. [10.1038/s41592-026-03198-4](https://doi.org/10.1038/s41592-026-03198-4) — Lessons learned from a Kaggle challenge for particle picking in cryo-electron tomography
- **作者**: Ariana Peck, Joshua Hutchings, Jonathan Schwartz, Yue Yu, Utz H. Ermel, Saugat Kandel et al.
- **期刊/来源**: Nature Methods
- **机构**: Chan Zuckerberg Initiative (United States) · Universidade Estadual de Maringá · Google (United States) · Kaggle · University of California, San Francisco
- **分类**: vol 23 · issue 9 · pp 1908-1916
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文报告了一项关于冷冻电子断层扫描（cryo-ET）中粒子拾取（particle picking）的Kaggle挑战赛的结果。该挑战赛旨在利用机器学习方法，在数百张实验断层扫描图上对五种分子物种进行自动标注，以克服手动拾取这一瓶颈。比赛吸引了超过1000名来自不同领域的参与者，获胜模型在性能上超越了现有最先进方法。系统比较显示，亚断层扫描平均（subtomogram averaging）对中等程度的过度拾取具有容忍性，但严重过度拾取会损害结果，这凸显了需要更稳健的标注质量度量。获胜模型还强调了数据增强在应对有限训练数据中的重要性。所有比赛断层扫描图、真实标注及获胜团队的标注已发布在CryoET Data Portal上，作为基准资源。
- **关键技术**: `machine learning`, `data augmentation`, `particle picking`, `cryo-electron tomography`, `benchmarking`
- **为什么对您有用**: 本文属于天体统计学/一般科学领域的入门读物，但更偏向生物成像应用。作为统计学家，本文展示了真实数据挑战中的标注质量度量和模型泛化问题，但方法学新颖性有限。武器库中的非参数统计和因果推断工具难以直接迁移，但可作为了解机器学习在科学图像分析中应用的入门材料。

### 2. [10.1038/s41592-026-03177-9](https://doi.org/10.1038/s41592-026-03177-9) — GHT-SELEX demonstrates unexpectedly high intrinsic sequence specificity and complex DNA binding of many human transcription factors
- **作者**: Arttu Jolma, Aldo Hernandez-Corchado, Ally W. H. Yang, Ali Fathi, Kaitlin U. Laverty, Alexander Brechalov et al.
- **期刊/来源**: Nature Methods
- **机构**: University of Toronto · McGill University · Memorial Sloan Kettering Cancer Center · SIB Swiss Institute of Bioinformatics · Russian Academy of Sciences · Institute of Protein Research · Vavilov Institute of General Genetics · École Polytechnique Fédérale de Lausanne 等
- **分类**: vol 23 · issue 9 · pp 1775-1785
- 相关性 5/10 · novelty: `application`
- **摘要**: 该研究提出 GHT-SELEX 方法，用于高通量测量纯化转录因子（TF）与裸基因组 DNA 的内在结合，以评估 TF 独立指定基因组结合位点的程度。方法将基因组 DNA 片段化后与 TF 孵育，通过高通量测序鉴定结合峰，并应用于 179 个人类 TF。结果显示 GHT-SELEX 峰与体内 ChIP-seq 峰高度重叠，表明许多 TF 的内在序列特异性比预期更强，可独立解释大部分体内结合。对于 C2H2 锌指蛋白，研究发现模块化、交替的锌指结构域参与是常态，导致多种不同类型的靶位点，且常涉及内部重复和分化。该工作为转录因子结合特异性的系统研究提供了新工具和数据集，但方法学上主要是实验技术的改进，统计方法较为常规。
- **关键技术**: `GHT-SELEX`, `ChIP-seq overlap analysis`, `motif analysis`, `C2H2 zinc finger domain modularity`
- **为什么对您有用**: 本文属于 gateway reading 范畴（Nature Methods 的通用科学/方法学论文），并非直接推进您的主要兴趣。作为入门读物，它清晰展示了高通量实验数据（SELEX 峰）与统计推断（峰重叠、motif 分析）的结合，但统计方法并不前沿。您的武器库（如非参数统计、高维推断）足以理解其分析，但无需深究。若您对转录组学或基因组学数据感兴趣，可作为了解该领域数据结构的入门材料，但鉴于其方法学 novelty 有限，不值得花时间读全文。

### 3. [10.1038/s41592-026-03194-8](https://doi.org/10.1038/s41592-026-03194-8) — Beyond benchmarking: an expert-guided consensus approach to spatially aware clustering
- **作者**: Jieran Sun, Kirti Biharie, Peiying Cai, Niklas Müller-Bötticher, Paul Kiessling, Meghan A. Turner et al.
- **期刊/来源**: Nature Methods
- **机构**: Centre Hospitalier Universitaire Vaudois · Leiden University Medical Center · Delft University of Technology · SIB Swiss Institute of Bioinformatics · University of Zurich · Berlin Institute of Health at Charité - Universitätsmedizin Berlin · Universitätsklinikum Aachen · RWTH Aachen University 等
- **分类**: vol 23 · issue 9 · pp 1814-1826
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对空间组学中空间感知聚类（SAC）方法的基准测试问题，指出现有基准过度聚焦于Visium平台和脑组织数据，且错误地将人工注释视为金标准。作者提出社区驱动的可扩展框架SACCELERATOR，统一数据格式、方法集成和指标评估，以支持快速纳入新方法和数据集。分析显示SAC方法的泛化性和可重复性存在显著局限，常用解剖标签作为金标准存在偏差且不适合基准测试。作者不主张排名，而是提出共识引导的工作流，利用描述性空间指标突出方法分歧的高熵区域，为组织专家提供针对性反馈。在脑和癌症数据集上的应用发现了单个SAC方法和人工注释遗漏的生物学模式，强调迭代式专家参与评估的必要性。
- **关键技术**: `spatially aware clustering`, `benchmarking framework`, `consensus-guided workflow`, `high-entropy regions`, `expert-in-the-loop evaluation`
- **为什么对您有用**: 本文属于Nature Methods的通用科学网关阅读，面向统计学家介绍空间组学数据中的聚类评估问题。作为入门读物，它清晰阐述了数据结构和评估挑战，但方法学贡献有限，主要在于框架构建而非新统计方法。您的武器库（如非参数统计、高维推断）足以理解其分析，但无需深入。若您对空间统计或生物信息学应用感兴趣，可作为了解领域问题的起点，但不必花时间精读全文。

### 4. [10.1038/s41592-026-03202-x](https://doi.org/10.1038/s41592-026-03202-x) — From pixels to patterns: the AI revolution in stem cell-derived models
- **作者**: Luca Deininger, Paolo Caldarelli, Magdalena Zernicka-Goetz, Ralf Mikut
- **期刊/来源**: Nature Methods
- **机构**: Karlsruhe Institute of Technology · Heidelberg University · ETH Zurich · California Institute of Technology
- **分类**: vol 23 · issue 9 · pp 1710-1723
- 相关性 4/10 · novelty: `survey`
- **摘要**: 这是一篇发表在 Nature Methods 上的 Perspective 综述，探讨 AI（尤其是深度学习、卷积神经网络和基础模型）如何变革干细胞衍生模型（如类器官和胚胎模型）的图像分析。文章系统梳理了 AI 在自动分类、分割、表型分析中的应用，并展示了在药物筛选、机制发现、实时命运预测等方面的案例。同时，作者讨论了标注数据有限、模型可解释性差、活体成像约束等实际挑战，并展望了多模态整合、实时实验引导和协议优化等未来方向。核心观点是 AI 不仅是分析工具，更是提升可重复性、加速洞察并推动对自组织机制理解的发现引擎。
- **关键技术**: `deep learning`, `convolutional neural networks`, `foundation models`, `image segmentation`, `phenotyping`
- **为什么对您有用**: 本文属于 general science 的 gateway reading 范畴，作为 Nature Methods 的 Perspective，它面向跨学科读者，对干细胞图像分析的 AI 方法做了清晰概述，适合作为入门读物。研究者作为统计学家，虽不直接涉足该领域，但可从中了解图像数据结构和分析流程，评估统计方法（如高维特征提取、不确定性量化）的潜在应用。武器库中的非参数统计和软件工具足以支撑理解，但无需深入方法学细节，值得花时间读全文以拓宽视野。

### 5. [10.1038/s41592-026-03182-y](https://doi.org/10.1038/s41592-026-03182-y) · [arXiv](https://arxiv.org/abs/2505.09329) — Benchmarking biomedical foundation models
- **作者**: Julio Saez-Rodriguez, Philipp Sven Lars Schäfer, Nikolas Kalavros, Gustavo Stolovitzky
- **期刊/来源**: Nature Methods
- **机构**: Chinese Academy of Sciences · Peng Cheng Laboratory · Shenzhen Institutes of Advanced Technology · University of Chinese Academy of Sciences · Tsinghua University · Macao Polytechnic University
- **分类**: vol 23 · issue 9 · pp 1724-1733
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文系统研究了生物医学视觉基础模型（foundation models）的缩放行为（scaling behavior），即在模型规模、数据规模、预训练算法和成像模态等维度上，性能如何随规模变化。作者构建了包含2100万张生物医学图像的大规模数据集BioVFM-21M，覆盖多种模态和解剖结构，并基于自监督学习预训练了BioVFM模型。实验发现，规模扩大确实带来性能提升，但提升幅度因任务而异，且与任务特性、数据多样性、预训练方法和计算效率等因素相关。BioVFM在12个医学基准上超越了此前的最先进基础模型。本文属于应用型研究，方法学上的新颖性有限，主要贡献在于大规模数据集和系统的实证分析。
- **关键技术**: `self-supervised learning`, `foundation models`, `scaling laws`, `benchmarking`, `medical image analysis`
- **为什么对您有用**: 本文属于一般科学（Nature Methods）的入门级阅读，作为统计学家可了解生物医学图像基础模型的现状和缩放规律，但方法学上无直接可迁移的统计技术。武器库足以理解其核心实验设计（如数据规模、模型规模对性能的影响），但无需深入方法细节。值得花时间读全文以拓宽视野，但非优先阅读。

### 6. [10.1038/s41592-026-03137-3](https://doi.org/10.1038/s41592-026-03137-3) — Aligning protein-generative models to experimental fitness with ProteinDPO
- **作者**: Talal Widatalla, Ashir A. Borah, Samuel H. King, Claudia L. Driscoll, Rafael Rafailov, Brian L. Hie
- **期刊/来源**: Nature Methods
- **机构**: Arc Research Institute · Stanford University · University of California, San Francisco
- **分类**: vol 23 · issue 9 · pp 1805-1813
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文提出 ProteinDPO，一种将直接偏好优化（DPO）应用于结构条件蛋白语言模型的方法，以对齐生成模型与实验适应度（如蛋白质稳定性）。核心问题是弥合无监督预训练与任务特定模型之间的“对齐差距”，即在保留预训练通用知识的同时注入任务特定信息。方法上，作者构建了偏好数据集（稳定 vs 不稳定序列），利用 DPO 微调模型，使其生成更可能稳定的序列。实验表明，ProteinDPO 在稳定性预测上达到与任务特定模型相当的性能，并优于无监督和标准微调版本。模型还能泛化到训练数据之外，改善多链蛋白复合物的稳定性和结合亲和力预测。在流感疫苗血凝素三聚体的稳定化应用中，约 80% 的设计达到或超过天然稳定性，部分设计对新兴哺乳动物毒株的稳定性提升高达 32°C。本文为生物基础模型的对齐提供了通用框架，但方法学上属于应用导向的深度学习技术，与您的统计理论兴趣交集有限。
- **关键技术**: `direct preference optimization (DPO)`, `protein language model`, `structure-conditioned generation`, `alignment gap`, `stability prediction`
- **为什么对您有用**: 本文属于 Nature Methods 的通用科学入门读物，而非您主要兴趣的方法学论文。作为统计学家，您可能对 DPO 的偏好优化框架（类似强化学习）感兴趣，但本文未涉及因果推断、高维统计或效率理论。武器库中的统计工具（如 U-统计量、半参数理论）在此应用场景中难以直接迁移。因此，本文仅适合作为跨学科广度阅读，不值得深入研读。

### 7. [10.1038/s41592-026-03179-7](https://doi.org/10.1038/s41592-026-03179-7) — Voltage imaging of neurons distributed across entire brains of larval zebrafish
- **作者**: Zeguan Wang, Jie Zhang, Panagiotis Symvoulidis, Wei Guo, Davy Deng, Adam Amsterdam et al.
- **期刊/来源**: Nature Methods
- **机构**: McGovern Institute for Brain Research · Massachusetts Institute of Technology · Harvard–MIT Division of Health Sciences and Technology · Koch Institute for Integrative Cancer Research At MIT
- **分类**: vol 23 · issue 9 · pp 1895-1907
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文介绍了一种远程扫描光片显微镜，能够以200.8 Hz的体积成像速率记录斑马鱼幼鱼全脑中约四分之一神经元的电压信号。作者使用基因编码的电压指示剂，实现了对跨脑区神经元电压轨迹的同步测量。研究发现，视觉诱发序列映射到视顶盖，而刺激无关的爆发活动映射到小脑和延髓，表明不同时序的神经元活动具有空间分布规律。该工作主要贡献在于工程和神经科学层面，而非统计学方法创新。对您而言，本文可作为神经影像数据生成背景的入门读物，但统计方法含量有限。
- **关键技术**: `light-sheet microscopy`, `genetically encoded voltage indicators`, `high-speed volumetric imaging`
- **为什么对您有用**: 本文属于神经影像技术应用，与您的统计兴趣无直接交集，但可作为了解大规模神经数据采集流程的入门材料。您的武器库（如高维统计、非参数方法）足以理解其数据分析需求，但本文未提供值得深入的方法学问题，因此仅建议快速浏览摘要和图表。

### 8. [10.1038/s41592-026-03211-w](https://doi.org/10.1038/s41592-026-03211-w) — Spatial isoform sequencing at single-cell resolution reveals cell-type-specific spatial isoform variability in multiple brain cell types
- **作者**: Lieke Michielsen, Andrey D. Prjibelski, Careen Foord, Yelizaveta Spiegelman, Taewoo Kim, Wen Hu et al.
- **期刊/来源**: Nature Methods
- **机构**: Cornell University · Weill Cornell Medicine · University of Helsinki · Düsseldorf University Hospital · Deutsches Diabetes-Zentrum e.V. · Heinrich Heine University Düsseldorf
- **分类**: vol 23 · issue 9 · pp 1869-1881
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文开发了空间长读测序技术 Spl-ISO-Seq2，实现 500 纳米分辨率的单细胞水平空间异构体测序，并配套软件 Spl-IsoQuant-2 和 Spl-IsoFind，将可测序的条形码数量从 8 万提升至超过 4.5 亿。应用于成年小鼠大脑，比较了已知区域间的差异异构体丰度，并采用不依赖预定义区域的空间异构体模式分析，两者均识别出如少突胶质细胞中的 Rps24 等重叠信号。对于已知的 Snap25 空间异构体变异，证明其发生在兴奋性神经元中；区域无关方法还发现了区域比较遗漏的模式，如 Ighm。许多空间异构体信号并非仅由细胞类型组成驱动，表明存在细胞类型内部的空间异构体变异。软件适用于多种空间和单细胞测序协议，并在 Visium HD 和 Stereo-seq 等平台间展示了可重复性。对您而言，本文作为 Nature Methods 的通用科学入口阅读，展示了空间转录组学中复杂数据结构和统计建模问题，但方法学上主要是实验和生物信息学贡献，与您的核心统计兴趣关联较弱。
- **关键技术**: `spatial long-read sequencing`, `single-cell resolution`, `barcode multiplexing`, `isoform quantification`, `differential expression analysis`
- **为什么对您有用**: 本文属于 Nature Methods 的通用科学入口阅读，作为统计学家可了解空间转录组学中数据结构和分析流程，但方法学上主要是实验和生物信息学贡献，与您的核心统计兴趣（因果推断、高维、半参数等）关联较弱。武器库足以理解其统计部分（如差异表达分析），但无需深入。不值得花时间读全文，除非对空间转录组学数据建模感兴趣。

### 9. [10.1038/s41592-026-03188-6](https://doi.org/10.1038/s41592-026-03188-6) — Large-scale single-molecule analysis of tau proteoforms
- **作者**: James Joly, Vivekananda Budamagunta, Zhengjian Zhang, Brittany Nortman, Maryam Jouzi, Rajat Bhatnagar et al.
- **期刊/来源**: Nature Methods
- **机构**: Nautilus (United States) · Genentech · Neural Stem Cell Institute · Mount Sinai Hospital · Icahn School of Medicine at Mount Sinai · Stanford Medicine · Stanford University
- **分类**: vol 23 · issue 9 · pp 1786-1797
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文介绍了一种名为 Iterative Mapping of proteoforms 的单分子蛋白质组学方法，通过迭代荧光标记抗体实现数百万至数十亿个单蛋白分子的并行检测。以 tau 蛋白为对象，使用 12 个位点特异性抗体，该方法在灵敏度（可检测 0.1% 丰度）、重现性（中位变异系数 <5.5%）和动态范围（>3 个数量级）上优于传统技术。在类器官、小鼠脑和人类阿尔茨海默病样本中鉴定出 130 种 tau 蛋白形式组，最多含 6 个磷酸化事件，且磷酸化分布非随机，提示有序的位点特异性修饰过程。作为 Nature Methods 的方法学论文，其统计贡献主要在于大规模单分子数据的处理与量化，但未涉及新的统计推断理论。
- **关键技术**: `single-molecule proteomics`, `iterative antibody probing`, `proteoform quantification`, `dynamic range assessment`, `reproducibility analysis`
- **为什么对您有用**: 本文属于 Nature Methods 的通用科学阅读，作为 gateway reading 可了解单分子蛋白质组学的数据生成与量化流程，但统计方法较为常规（变异系数、动态范围等），与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接交集。武器库足以理解其数据分析，但无需深入。可作为拓宽视野的泛读材料，不值得精读。

### 10. [10.1038/s41592-026-03180-0](https://doi.org/10.1038/s41592-026-03180-0) — All-optical multimodal mapping of single-cell-type-specific metabolic activities via REDCAT
- **作者**: Yajuan Li, Zhaojun Zhang, Archibald Enninful, Negin Farzad, Presha Rajbhandari, Hua Tian et al.
- **期刊/来源**: Nature Methods
- **机构**: University of California San Diego · University of Pennsylvania · Yale University · Columbia University · University of Pittsburgh · Columbia University Irving Medical Center · Herbert Irving Comprehensive Cancer Center · Yale Cancer Center
- **分类**: vol 23 · issue 9 · pp 1840-1853
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文提出 REDCAT，一种全光学平台，将拉曼散射显微镜与高多重免疫荧光结合，在组织原位以单细胞分辨率同时绘制代谢活动和细胞类型。该方法实现了对蛋白质、脂质、核代谢物和氧化还原代谢的亚细胞 profiling，并在淋巴结、淋巴瘤和肝脏中揭示了细胞类型特异的代谢特化、肿瘤转化中的代谢重编程以及肝小叶分区依赖的代谢梯度。技术核心在于整合拉曼光谱的生化特异性和免疫荧光的细胞身份标记，并通过计算流程对齐和整合多模态数据。作为 Nature Methods 的方法学论文，其统计贡献主要体现在多模态数据整合和空间代谢状态的定量分析上，但并非面向统计学家的方法论创新。对您而言，本文可作为了解前沿生物医学成像技术和多模态数据结构的入门读物，但其统计方法深度有限。
- **关键技术**: `Raman scattering microscopy`, `high-plex immunofluorescence`, `multimodal data integration`, `spatial metabolomics`, `single-cell profiling`
- **为什么对您有用**: 本文属于 Nature Methods 的通用科学入门读物，而非直接的方法学贡献。作为统计学家，您可以从中了解多模态空间数据的结构和分析需求，但武器库中的统计工具（如高维、因果推断）在此并无直接应用点。鉴于其方法学 novelty 有限，且与您的主要兴趣无直接交集，不值得花时间精读全文，仅可作为拓宽视野的泛读材料。

### 11. [10.1038/s41592-026-03184-w](https://doi.org/10.1038/s41592-026-03184-w) — Overcoming air–water interface-induced artifacts in cryo-EM with protein nanocrates
- **作者**: Matthew C. Jenkins, Daija Bobe, Jake D. Johnston, Jonah Cheung, Akira Karasawa, Christina M. Zimanyi et al.
- **期刊/来源**: Nature Methods
- **机构**: Georgia Institute of Technology · New York Structural Biology Center · Columbia University · Chan Zuckerberg Initiative (United States)
- **分类**: vol 23 · issue 9 · pp 1798-1804
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文提出一种名为‘nanocrates’的蛋白质封装方法，用于解决冷冻电镜（cryo-EM）样品制备中气-液界面引起的分子取向偏好、分布不均及损伤等伪影问题。该方法利用源自MS2噬菌体的高亲水性、结构均一且稳定的蛋白质外壳，将目标蛋白包裹其中，从而使其在气-液界面随机取向。作者通过三个原理验证案例展示了该方法的有效性：apoferritin（高分辨率）、thyroglobulin（解决已知的取向偏好问题）以及7,8-二氢新蝶呤醛缩酶（此前未被cryo-EM解析的结构）。文章详细描述了封装、数据采集和重构流程，并展示了所得结构的质量。该方法为cryo-EM样品制备提供了一种通用且有效的替代方案，尤其适用于难以获得随机取向的蛋白。
- **关键技术**: `cryo-EM sample preparation`, `protein encapsulation`, `air-water interface artifact mitigation`, `single-particle analysis`
- **为什么对您有用**: 本文属于方法学应用，但主题为结构生物学，与您的主要兴趣（因果推断、高维统计等）无直接关联。作为Nature Methods上的方法学论文，它展示了如何通过实验设计解决数据采集中的系统性偏差，这或许能类比到观测数据中的选择偏差问题，但迁移性有限。作为跨学科阅读，它提供了生物成像中数据质量控制的实例，但并非入门级读物，且武器库中的统计工具在此场景下无用武之地。因此，不建议深入阅读。

### 12. [10.1038/s41592-026-03200-z](https://doi.org/10.1038/s41592-026-03200-z) — PASTA: versatile tyramide-oligonucleotide amplification for multimodal spatial biology
- **作者**: Hendrik A. Michel, Paige McCallum, Wenrui Wu, Huaying Qiu, Jia Le Lee, Shuli Luo et al.
- **期刊/来源**: Nature Methods
- **机构**: Beth Israel Deaconess Medical Center · Harvard University · McGill University · Brigham and Women's Hospital · European Institute of Oncology · Translational Research Institute · The University of Queensland · Singapore General Hospital 等
- **分类**: vol 23 · issue 9 · pp 1769-1774
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文介绍了一种名为 PASTA 的空间生物学信号放大技术，通过辣根过氧化物酶介导的寡核苷酸沉积和循环成像，实现高多重、多模态的空间蛋白和核酸共检测。该方法兼容抗体偶联和原位杂交，适用于福尔马林固定石蜡包埋样本，为从发现到临床验证提供了经济有效的桥梁。PASTA 是一种平台无关的信号放大方法，可提升检测灵敏度并支持多模态整合。该技术主要面向生物医学应用，不涉及新的统计理论或方法。对您而言，本文属于跨学科科普阅读，其数据生成过程可能涉及高维图像数据的统计分析，但当前与您的研究方向无直接交集。
- **关键技术**: `tyramide signal amplification`, `oligonucleotide deposition`, `multiplexed imaging`, `in situ hybridization`
- **为什么对您有用**: 本文属于 Nature Methods 的跨学科科普阅读，作为 gateway reading 可了解空间生物学的前沿技术，但其核心是实验方法而非统计方法。武器库中的统计工具（如高维数据分析）虽可用于处理此类图像数据，但本文未提供可直接迁移的统计问题。因此，本文仅适合作为拓宽视野的阅读，不值得深入投入时间。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

