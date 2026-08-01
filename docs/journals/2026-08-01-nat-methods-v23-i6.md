# Nat. Methods — Vol 23  Issue 6  ·  2026-08-01

- 共 12 篇 · Nature Methods
- 目录核对 ⚠️ 疑似漏 17 篇（对照 OpenAlex 29 篇）：10.1038/s41592-026-03076-z、10.1038/s41592-026-03114-w、10.1038/s41592-026-03091-0、10.1038/s41592-026-03092-z、10.1038/s41592-026-03117-7 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Nature Methods》第23卷第6期的12篇论文整体围绕**生物分子动态与空间解析**这一核心主题展开，可归纳为三条主线：**构象系综与动态预测**（从静态结构到动态系综的跨越）、**空间与单细胞转录组学的数据质量与解析**（噪声校正、细胞类型特异性表达、lncRNA多样性）、以及**原位与亚细胞成像技术**（代谢成像、化学映射、多模态显微镜）。此外，还有几篇涉及**高通量筛选与转录本组装**的方法学改进。

在**构象系综与动态预测**主线上，Perspective文章《From possibility to precision in macromolecular ensemble prediction》系统梳理了当前AI工具（如AlphaFold）在静态结构预测成功后的瓶颈——缺乏高分辨率基准数据来验证动态构象系综，并呼吁整合异质实验数据为统一编码表示。另一篇《eSIG-Net: an interaction language model that decodes the protein code of single mutations》则从序列出发，利用语言模型预测单点突变对蛋白质-蛋白质相互作用的影响，属于动态功能预测的序列建模分支。这两篇共同指向从静态快照向动态分子理解的范式转变，但前者更侧重数据基础设施，后者更侧重预测模型。

**空间与单细胞转录组学**是本期最密集的方法学主线。三篇论文分别从不同角度切入：Xenium平台的数据噪声评估论文《Resolving sensitivity, specificity and signal contamination in Xenium spatial transcriptomics》提出了SPLIT方法，通过单核RNA测序量化转录本溢出并校正混合信号，直接提升细胞类型分辨率；《Decoding sequence determinants of gene expression in diverse cellular and disease states》的Decima模型将序列-功能预测从bulk组织扩展到单细胞分辨率，学习细胞类型特异性的顺式调控语法；《Unraveling lncRNA diversity at a single cell resolution and in a spatial context across different cancer types》则构建了大规模lncRNA资源库SPanC-Lnc，整合单细胞与空间数据。这三篇共同展示了空间/单细胞数据从噪声校正、功能预测到资源构建的完整链条，其中SPLIT的噪声建模和Decima的序列-表达映射对统计方法有直接参考价值。

**原位与亚细胞成像技术**主线包含四篇技术论文：FILM技术《FILM: mapping organellar metabolism by mid-infrared photothermal-modulated fluorescence》结合中红外光热显微镜与AI去噪，实现单个溶酶体的代谢成像；《Subcellular chemical mapping using correlated cryogenic electron and mass spectrometry imaging》将冷冻电镜与质谱成像关联，解决电子密度对应化学物质的识别问题；《A multimodal adaptive optical microscope for in vivo imaging from molecules to organisms》的MOSAIC平台集成多种成像模态，实现跨尺度关联；《AreTomoLive: automated reconstruction of comprehensively corrected and denoised cryo-electron tomograms in real time and at high throughput》则聚焦冷冻电镜断层扫描的实时自动化预处理。这些论文虽以工程和实验创新为主，但其中涉及的去噪、解卷积、多模态对齐等计算问题，对统计方法在成像数据处理中的应用有启发。

其余论文中，《Multiplexed perturbation enables scalable pooled screens》和《StringTie3 improves total RNA-seq assembly by resolving nascent and mature transcripts》分别涉及高通量筛选的实验设计优化和转录本组装算法改进，前者对统计学家理解CRISPR筛选的数据结构有实用价值，后者通过建模共转录剪接过程区分新生与成熟转录本，属于生物信息学中的序列建模问题。综述《Recommendations and considerations for hydroxyl radical protein footprinting–mass spectrometry》则提供了HRPF-MS技术的标准化操作框架，数据分析部分涉及肽段定量与统计评估。

对于因果推断方向的研究者，本期无直接相关论文；对于半参数/非参方向，SPLIT方法中的混合信号解析可视为一种非参数信号分离问题；对于高维方向，Decima模型从DNA序列预测单细胞表达涉及高维序列特征学习；对于计算方法方向，eSIG-Net的对比学习框架和AreTomoLive的GPU加速流水线值得关注。建议优先阅读：空间转录组学噪声校正（SPLIT）、序列-表达预测（Decima）、以及构象系综基准数据讨论（Perspective）。

## 其他  *(other, 12 篇)*

### 1. [10.1038/s41592-026-03084-z](https://doi.org/10.1038/s41592-026-03084-z) · [arXiv](https://arxiv.org/abs/2505.01919) — From possibility to precision in macromolecular ensemble prediction
- **作者**: Stephanie A. Wankowicz, Massimiliano Bonomi
- **期刊/来源**: Nature Methods
- **分类**: vol 23 · issue 6 · pp 1100-1108
- 相关性 7/10 · novelty: `survey`
- **摘要**: 本文是一篇 Perspective 文章，讨论蛋白质等大分子构象系综预测的现状与挑战。当前 AI 工具（如 AlphaFold）在静态结构预测上取得突破，但无法捕捉动态构象系综，而构象系综对催化、别构调控和分子识别至关重要。文章指出，缺乏高分辨率、大规模的真实基准数据是主要瓶颈——单一实验技术无法完全解析构象景观的原子级复杂性，且在定义、表示、比较和验证结构系综方面仍存在困难。作者概述了克服这些障碍所需的基础设施和方法学进展，包括整合异质实验数据为统一系综编码表示，并利用这些数据构建基准和系综特异性验证协议。文章还展望了系综预测将推动实验与计算创新的交互循环，使结构生物学从静态快照迈向动态分子行为的全面理解。作为 Nature Methods 的 Perspective，本文是面向数据科学家的优秀入门读物，清晰阐述了结构生物学中一个重要的数据建模问题，但未提出具体的新统计方法或理论贡献。
- **关键技术**: `conformational ensemble prediction`, `heterogeneous data integration`, `ensemble encoding representation`, `validation protocols`
- **为什么对您有用**: 本文属于 general science 范畴（Nature Methods），作为 gateway reading 质量很高：(a) 对统计学家友好，不依赖领域行话，自包含地介绍了构象系综预测的核心挑战；(b) 清晰阐述了更大的科学问题——为什么结构生物学需要从静态走向动态；(c) 具有真实的数据/建模维度：异质实验数据（X射线、NMR、冷冻电镜等）的整合、系综表示与验证，是一个非平凡的统计推断问题。武器库方面：本文不涉及可直接迁移的方法，但作为了解结构生物学数据挑战的入门读物值得一读，属于**暂不可做**——核心机器（生物物理建模、分子动力学模拟）不在武器库中。

### 2. [10.1038/s41592-026-03089-8](https://doi.org/10.1038/s41592-026-03089-8) — Resolving sensitivity, specificity and signal contamination in Xenium spatial transcriptomics
- **作者**: Mariia Bilous, Daria Buszta, Jonathan Bac, Senbai Kang, Yixing Dong, Stephanie Tissot et al.
- **期刊/来源**: Nature Methods
- **机构**: University of Lausanne · Swiss Cancer Center Léman · Ludwig Cancer Research · Idiap Research Institute · Hôpital Orthopédique de la Suisse Romande · SIB Swiss Institute of Bioinformatics · Centre Hospitalier Universitaire Vaudois · École Polytechnique Fédérale de Lausanne
- **分类**: vol 23 · issue 6 · pp 1152-1162
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文针对 Xenium 空间转录组学平台的数据质量进行系统评估，基于超过 40 个乳腺和肺肿瘤切片的实测数据集，系统剖析了技术噪声（包括转录本溢出）、检测特异性、基因面板性能和分割策略等关键问题。作者利用单核 RNA 测序实现对转录本污染的精确量化，并在此基础上提出 SPLIT 方法，通过解析混合转录信号来提升信号纯度。SPLIT 改善了背景校正和细胞类型分辨率，能够揭示与恶性细胞共定位相关的 T 细胞耗竭特征，而这些信号在原始数据中会被掩盖。该研究为 Xenium 平台的性能提供了关键基准，并引入了一种可扩展的信号精炼策略。作为 Nature Methods 上的方法学论文，本文对数据噪声结构和信号分离问题的刻画清晰，适合作为空间组学领域的入门读物。
- **关键技术**: `spatial transcriptomics`, `Xenium platform`, `transcript spillover correction`, `single-nucleus RNA sequencing`, `signal deconvolution`
- **为什么对您有用**: 本文属于 general science / Nature Methods 的 gateway reading，适合作为空间组学数据噪声分析领域的入门读物。武器库中的非参数统计和逆问题经验可用于理解其信号分离框架，但本文不涉及研究者核心兴趣中的因果推断或高维统计方法，属于拓宽视野的阅读材料。

### 3. [10.1038/s41592-026-03102-0](https://doi.org/10.1038/s41592-026-03102-0) — Decoding sequence determinants of gene expression in diverse cellular and disease states
- **作者**: Avantika Lal, Alexander Karollus, Laura Gunsalus, David Garfield, Surag Nair, Alex M. Tseng et al.
- **期刊/来源**: Nature Methods
- **机构**: Gene Therapy Laboratory · Munich Center for Machine Learning · Technical University of Munich · California Institute for Regenerative Medicine · Regenerative Medicine Institute · Institut thématique Génétique, génomique et bioinformatique
- **分类**: vol 23 · issue 6 · pp 1138-1151
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文提出 Decima 模型，从 DNA 序列预测基因在特定细胞类型和疾病状态下的表达水平。该模型基于超过 2200 万个细胞的单细胞 RNA 测序数据训练，能够学习细胞类型特异性的顺式调控语法。Decima 可预测未见基因的细胞类型特异性表达，揭示疾病中基因表达变化的调控机制，并以细胞类型分辨率预测非编码变异效应。此外，模型还能设计具有精确调控功能的 DNA 元件。该工作属于计算生物学与基因组学领域，核心贡献在于将序列-功能模型从 bulk 组织扩展到单细胞分辨率。
- **关键技术**: `sequence-to-function model`, `single-cell RNA-seq`, `cis-regulatory grammar`, `deep learning`
- **为什么对您有用**: 本文属于 Nature Methods 上的方法学论文，作为跨学科通识阅读有较好价值：问题阐述清晰，数据规模大（2200 万细胞），模型设计有明确的统计学习维度（从序列预测表达）。但该工作与您的主要研究方向（因果推断、高维统计、U-统计量等）无直接方法学连接，武器库中的工具难以直接迁移。作为 gateway reading 值得一读以拓宽视野，但无需深入跟进。

### 4. [10.1038/s41592-026-03071-4](https://doi.org/10.1038/s41592-026-03071-4) — Unraveling lncRNA diversity at a single cell resolution and in a spatial context across different cancer types
- **作者**: P. Prakrithi, Tuan Vo, Zherui Xiong, Hani Vu, Loan T. Nguyen, Andrew Newman et al.
- **期刊/来源**: Nature Methods
- **机构**: The University of Queensland · QIMR Berghofer Medical Research Institute · Indian Institute of Technology Delhi · Hunter Medical Research Institute · University of Newcastle Australia · Agriculture and Food · Takara (Sweden) · Queensland Health 等
- **分类**: vol 23 · issue 6 · pp 1236-1249
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文利用单细胞和空间转录组学数据，系统分析了13种癌症类型中219,442个潜在长链非编码RNA（lncRNA）。通过TAR-scRNA-seq流程鉴定lncRNA，并评估其细胞类型特异性和空间分布。与五个现有数据库对比，确认了已知lncRNA并发现了94,795个未注释的lncRNA。实验验证跨越七种癌症类型，使用了三种单细胞分辨率空间转录组平台和两种长读长空间转录组测序方法。通过基因组共定位、疾病变异和与蛋白编码基因的空间自相关分析，推断lncRNA的潜在功能。最终构建了免费、快速的云数据库SPanC-Lnc。本文是典型的资源型方法学论文，核心贡献在于数据资源和分析流程，而非统计方法创新。
- **关键技术**: `single-cell transcriptomics`, `spatial transcriptomics`, `TAR-scRNA-seq pipeline`, `long-read sequencing`, `spatial autocorrelation analysis`
- **为什么对您有用**: 本文属于Nature Methods上的资源型论文，作为gateway reading，它清晰展示了单细胞和空间转录组学数据的结构、噪声和规模，以及lncRNA功能推断的建模思路，对统计学家了解这一前沿领域有入门价值。但武器库中缺乏处理此类高维稀疏计数数据的专门工具（如单细胞统计模型），且无直接可迁移的方法学，暂不可做。

### 5. [10.1038/s41592-026-03090-1](https://doi.org/10.1038/s41592-026-03090-1) · [arXiv](https://arxiv.org/abs/2504.04305) — FILM: mapping organellar metabolism by mid-infrared photothermal-modulated fluorescence
- **作者**: Jianpeng Ao, Jiaze Yin, Haonan Lin, Guangrui Ding, Youchen Guan, Marzia Savini et al.
- **期刊/来源**: Nature Methods
- **分类**: vol 23 · issue 6 · pp 1196-1206
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文报道了一种名为FILM的荧光检测中红外光热显微镜技术，用于在活细胞和生物体内对单个溶酶体的代谢活动进行高分辨率成像。该方法结合了光学boxcar解调照明、人工智能辅助数据去噪和光谱解卷积，能够区分溶酶体内部的脂解和蛋白水解异质性，并检测衰老过程中溶酶体功能的早期失调。研究还发现了与多种溶酶体贮积症相关的细胞器水平代谢变化。FILM技术提供了一种在天然环境下无创分析单个细胞器代谢指纹的方法，有望构建高分辨率的化学细胞图谱。该工作主要是一项生物成像技术的方法学贡献，而非统计方法学创新。
- **关键技术**: `mid-infrared photothermal microscopy`, `optical boxcar demodulation`, `AI-assisted denoising`, `spectral deconvolution`, `fluorescence imaging`
- **为什么对您有用**: 本文属于Nature Methods上的生物成像技术论文，作为gateway reading，其数据采集和去噪流程（AI去噪、光谱解卷积）对统计学家有一定趣味性，但核心方法并非统计推断或建模问题。武器库中的非参数统计或高维工具与此无直接接口，暂不可做。可作为科普性阅读了解前沿生物成像技术，但不值得投入时间精读。

### 6. [10.1038/s41592-026-03086-x](https://doi.org/10.1038/s41592-026-03086-x) — eSIG-Net: an interaction language model that decodes the protein code of single mutations
- **作者**: Xingxin Pan, Aditya Shrawat, Sidharth Raghavan, Chuanpeng Dong, Yuntao Yang, Zhao Li et al.
- **期刊/来源**: Nature Methods
- **机构**: Neurosciences Institute · Temple College · The University of Texas at Austin · Case Western Reserve University · Baylor University · Baylor College of Medicine · Yale Cancer Center · Systems Biology Institute 等
- **分类**: vol 23 · issue 6 · pp 1115-1120
- 相关性 6/10 · novelty: `application`
- **摘要**: 该论文提出 eSIG-Net，一个基于语言模型的框架，用于预测单点突变如何改变蛋白质-蛋白质相互作用（即“蛋白质代码”）。模型整合了蛋白质序列嵌入、语法感知和进化感知的突变编码以及对比学习，直接从序列信息预测突变驱动的相互作用变化。在多个基准数据集上，eSIG-Net 优于现有的基于序列和结构的预测方法，并能提名因果变异和提供机制性见解。该工作属于计算生物学中的预测建模，不涉及因果推断、高维统计或效率理论等核心统计方法。对于统计研究者而言，本文可作为了解生物信息学中序列建模和对比学习应用的入门读物，但方法学上的直接迁移价值有限。
- **关键技术**: `language model`, `contrastive learning`, `protein sequence embedding`, `mutation encoding`
- **为什么对您有用**: 本文属于 Nature Methods 上的方法学论文，作为 gateway reading 可帮助了解生物信息学中语言模型的应用。但论文核心是预测建模而非统计推断，与 primary interests（因果推断、高维统计、U-统计量等）无直接连接。武器库中的非参数统计或高维渐近工具难以直接迁移。暂不可做——核心机器（蛋白质语言模型、对比学习）不在武器库中。

### 7. [10.1038/s41592-026-03095-w](https://doi.org/10.1038/s41592-026-03095-w) — Multiplexed perturbation enables scalable pooled screens
- **作者**: Stefan Oberlin, Neil Q. Tay, Albert Xue, Ruzbeh Mosadeghi, Harold Pimentel, Michael T. McManus
- **期刊/来源**: Nature Methods
- **机构**: University of California, San Francisco · University of Würzburg · University of California, Los Angeles · UCLA Health · Chan Zuckerberg Initiative (United States) · UCSF Helen Diller Family Comprehensive Cancer Center
- **分类**: vol 23 · issue 6 · pp 1163-1173
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究在CRISPR干扰（CRISPRi）筛选中通过高感染复数（MOI）共递送多个引导RNA（sgRNA）的策略，旨在减少所需细胞数量并提高筛选效率。系统评估了不同MOI水平（2.5-10）对敲低效率、sgRNA代表性及多重sgRNA表型干扰的影响。结果表明，sgRNA多重化可在保持筛选性能的同时显著降低细胞需求。进一步将优化条件应用于全基因组CRISPR筛选，成功鉴定出ICAM-1调控因子，仅需50万个细胞。该研究为资源有限条件下的CRISPR筛选提供了实用框架。作为Nature Methods上的方法学论文，本文清晰展示了实验设计、数据结构和分析流程，适合作为统计学家了解高通量功能基因组学筛选的入门读物。
- **关键技术**: `CRISPR interference (CRISPRi)`, `multiplicity of infection (MOI)`, `pooled genetic screens`, `sgRNA multiplexing`, `genome-wide screen`
- **为什么对您有用**: 本文属于general science（Nature Methods）范畴，作为gateway reading： (a) 对高通量筛选领域的外行统计学家友好，实验设计和数据分析流程阐述清晰； (b) 提出了一个统计学家会感兴趣的数据/建模问题——多重sgRNA的表型干扰建模与统计推断； (c) 武器库中的非参数统计和因果推断工具可用于分析多重扰动下的表型效应，但本文主要是实验方法贡献，方法学转移空间有限； (d) 值得花时间读全文以拓宽对功能基因组学筛选的理解。

### 8. [10.1038/s41592-026-03080-3](https://doi.org/10.1038/s41592-026-03080-3) — StringTie3 improves total RNA-seq assembly by resolving nascent and mature transcripts
- **作者**: Ida Shinder, Geo Pertea, Richard Hu, Zoe Rudnick, Mihaela Pertea
- **期刊/来源**: Nature Methods
- **机构**: Johns Hopkins University · Johns Hopkins Medicine · University of Baltimore · Lieber Institute for Brain Development
- **分类**: vol 23 · issue 6 · pp 1126-1137
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文提出 StringTie3，一个针对总 RNA 测序（rRNA-depleted RNA-seq）的转录本组装工具的重大更新。现有方法常将未完全加工的新生 RNA 与成熟异构体混淆，导致组装错误和定量偏差。StringTie3 引入“新生模式”，通过建模共转录剪接过程来区分新生与成熟转录本，并改进了长读长模块以区分真实 polyA 位点与引物伪迹。在短读长、长读长和混合读长数据集上，StringTie3 显著减少了组装错误，性能优于现有工具。在 Argonaute 敲除实验中，新生模式分析揭示单敲除主要影响新生转录本，而多敲除同时影响两个组分；在乳腺癌样本中，某些基因的新生与成熟表达不一致，提示存在转录后调控。该工具为利用总 RNA-seq 研究转录与转录后过程提供了框架。对您而言，这是一篇方法学软件论文，属于统计计算与软件开发的兴趣范畴，但核心贡献在生物信息学而非统计理论，可作为跨领域阅读了解 RNA-seq 数据分析的挑战。
- **关键技术**: `transcript assembly`, `co-transcriptional splicing modeling`, `long-read RNA-seq`, `short-read RNA-seq`, `hybrid-read assembly`
- **为什么对您有用**: 本文属于统计计算与软件开发的兴趣范畴，但核心是生物信息学方法，与您的主要统计兴趣（因果推断、高维、U-统计等）无直接技术重叠。作为 gateway reading，它清晰阐述了 RNA-seq 数据分析中的核心问题（新生 vs 成熟转录本区分），数据结构和模型假设（共转录剪接）对统计学家友好。武器库中 'software development' 项可支撑理解其算法实现，但无需深入。暂不可做：核心机器不在武器库里，缺转录组组装领域的领域知识。

### 9. [10.1038/s41592-026-03093-y](https://doi.org/10.1038/s41592-026-03093-y) — AreTomoLive: automated reconstruction of comprehensively corrected and denoised cryo-electron tomograms in real time and at high throughput
- **作者**: Ariana Peck, Yue Yu, Mohammadreza Paraan, Dari Kimanius, Utz H. Ermel, Joshua Hutchings et al.
- **期刊/来源**: Nature Methods
- **机构**: Chan Zuckerberg Initiative (United States) · University of California, San Francisco · Chan Zuckerberg Biohub San Francisco
- **分类**: vol 23 · issue 6 · pp 1121-1125
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文介绍 AreTomoLive，一个用于冷冻电子断层扫描（cryo-ET）数据实时自动预处理的流水线。该流水线由两个 GPU 加速包组成：AreTomo3 负责断层对齐与重建，新增功能可完全考虑样品几何并局部校正对比传递函数（CTF）；DenoisET 利用 AreTomo3 的校正断层图，在对比度增强过程中保留更多中分辨率特征。整个流水线强调自动化，支持在数据采集的同时进行大规模预处理。作为 Nature Methods 上的方法学论文，它展示了计算工具如何解决高吞吐量数据处理瓶颈，但对统计方法本身无直接贡献。本文适合作为计算生物学领域的入门读物，了解冷冻电镜数据处理流程，但研究者无需深入阅读。
- **关键技术**: `GPU-accelerated tomographic reconstruction`, `contrast transfer function correction`, `denoising for cryo-ET`
- **为什么对您有用**: 本文属于 general science 范畴的 gateway reading。作为 Nature Methods 上的方法学论文，它清晰阐述了冷冻电镜数据处理中的计算挑战和流水线设计，对统计学家而言是了解该领域数据结构和计算需求的良好入门。但研究者武器库中的工具（如非参数统计、高维渐近理论）与此无直接关联，且本文不涉及统计推断或不确定性量化，因此暂不可做任何 follow-up。

### 10. [10.1038/s41592-026-03109-7](https://doi.org/10.1038/s41592-026-03109-7) — Subcellular chemical mapping using correlated cryogenic electron and mass spectrometry imaging
- **作者**: Hannah Ochner, Buse Isbilir, Sonja Blasche, David Scheidweiler, Yuexuan Zhang, Zhexin Wang et al.
- **期刊/来源**: Nature Methods
- **机构**: MRC Laboratory of Molecular Biology · University of Cambridge · MRC Toxicology Unit · MRC Laboratory for Molecular Cell Biology
- **分类**: vol 23 · issue 6 · pp 1174-1183
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出了一种将冷冻电镜（cryo-EM）与聚焦离子束二次离子质谱（FIB-SIMS）相结合的相关工作流程，用于对未标记生物样本进行亚细胞尺度的化学成像。该方法解决了冷冻电镜难以直接识别观察到的电子密度对应何种化学物质的核心问题。通过将高空间分辨率的形貌信息与元素/分子质谱信号对齐，实现了对细菌细胞和真核生物冷冻薄片中特定分子的亚细胞定位。作为生物学应用案例，研究揭示了环境污染物双酚AF在环境细菌细胞质内形成相分离聚集体并被储存，且细菌外排泵即使显著上调也无法将其清除。该工作主要是一项实验技术与生物学发现，不涉及新的统计方法或理论。对于一位统计学家而言，本文可作为了解冷冻电镜与质谱成像数据结构的入门读物，但其中没有可直接迁移的统计推断问题或方法论贡献。
- **关键技术**: `correlative cryo-EM and FIB-SIMS`, `subcellular chemical mapping`, `focused ion beam secondary ion mass spectrometry`
- **为什么对您有用**: 本文属于Nature Methods上的多学科旗舰论文，作为gateway reading，其数据侧（质谱成像的空间分辨率、噪声结构、多模态图像配准）和模型侧（化学物种的定位与丰度推断）有潜在的统计问题，但本文未展开任何统计建模。武器库中'非参数统计'和'高维渐近'无法直接攻入，因为核心挑战是实验流程而非推断方法。暂不可做——缺乏明确的统计估计或假设检验问题框架。

### 11. [10.1038/s41592-026-03066-1](https://doi.org/10.1038/s41592-026-03066-1) — A multimodal adaptive optical microscope for in vivo imaging from molecules to organisms
- **作者**: Tian-Ming Fu, Gaoxiang Liu, Daniel E. Milkie, Xiongtao Ruan, Frederik Görlitz, Yu Shi et al.
- **期刊/来源**: Nature Methods
- **机构**: Howard Hughes Medical Institute · Janelia Research Campus · University of California, Berkeley · University of North Carolina at Chapel Hill · University of Illinois Chicago · University of Chicago · Monash University · University of Maryland, Baltimore 等
- **分类**: vol 23 · issue 6 · pp 1184-1195
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文介绍了一种名为MOSAIC的多模态自适应光学显微镜，它集成了光片、无标记、超分辨和多光子等多种先进成像技术，并配备自适应光学系统。该显微镜能够在培养细胞和活体多细胞生物中实现亚细胞动力学的非侵入性成像，在毫米级膨胀组织中进行纳米级分子结构映射，以及在活体小鼠中进行结构和功能神经成像。MOSAIC通过在同一标本中实现跨生物尺度的关联研究，为广泛的生物学研究提供了一个集成平台。从统计学家的视角看，本文主要是一项工程和生物学工具的创新，不涉及新的统计方法或理论。对于一位以统计理论和方法为核心兴趣的研究者，本文作为科普级阅读材料，展示了现代生物成像技术的前沿，但缺乏可直接迁移的统计方法论。
- **关键技术**: `adaptive optics`, `light-sheet microscopy`, `super-resolution microscopy`, `multiphoton microscopy`, `multimodal imaging`
- **为什么对您有用**: 本文属于Nature Methods上的多学科旗舰期刊论文，作为gateway reading，它清晰阐述了生物成像中的多尺度观测挑战，但数据侧（图像噪声、选择效应、尺度）和模型侧（似然、潜在变量、假设）的统计维度并未展开，因此对统计学家而言，其作为入门读物的价值有限。武器库中的非参数统计或高维渐近理论无法直接应用于本文所描述的成像系统设计。本文不值得花时间全文阅读，因为其核心贡献是工程实现而非统计方法。

### 12. [10.1038/s41592-026-03083-0](https://doi.org/10.1038/s41592-026-03083-0) — Recommendations and considerations for hydroxyl radical protein footprinting–mass spectrometry
- **作者**: Aaron T. Wecksler, Lingfei Wang, Lisa J. Bernstein, Richard Y. -C. Huang, Sayan Gupta, Line G. Kristensen et al.
- **期刊/来源**: Nature Methods
- **机构**: Gene Therapy Laboratory · Analytical Services · Biostatistical Consulting (United States) · Johnson & Johnson (United States) · Johnson & Johnson (Israel) · Lawrence Berkeley National Laboratory · University of Leeds · Albert Einstein College of Medicine 等
- **分类**: vol 23 · issue 6 · pp 1089-1099
- 相关性 4/10 · novelty: `survey`
- **摘要**: 本文是一篇关于羟基自由基蛋白质足迹-质谱（HRPF-MS）技术的共识性指南。该技术通过羟基自由基标记蛋白质侧链，结合液相色谱-质谱检测，定量反映溶剂可及性，用于研究蛋白质-蛋白质相互作用、配体结合、构象变化等结构生物学问题。文章系统总结了实验设计、样品处理、氧化条件（光解、芬顿化学、电化学、X射线等）、数据采集与分析的最佳实践。在数据分析部分，涉及肽段鉴定、定量比较、统计显著性评估及与正交数据的整合策略。文章还讨论了该技术在学术和生物制药研究中的应用现状与局限性。作为一篇方法学综述，本文未提出新的统计理论或方法，而是为领域内研究者提供标准化操作框架。对您而言，本文属于跨学科方法学阅读，但其中关于质谱数据定量比较的统计问题（如多重检验校正、效应量估计）可能与您的假设检验兴趣有微弱关联，不过整体方法学新颖性较低。
- **关键技术**: `hydroxyl radical protein footprinting`, `bottom-up proteomics`, `liquid chromatography-mass spectrometry`, `solvent accessibility quantification`, `statistical significance testing`
- **为什么对您有用**: 本文属于Nature Methods上的方法学综述，作为gateway reading，其数据维度（质谱峰强度定量比较）涉及统计检验问题，但整体与您的primary interests（因果推断、高维统计、U统计量等）无直接关联。武器库中无直接可攻工具，属于暂不可做范畴——核心机器（蛋白质组学数据处理流程）不在武器库内。可作为跨学科科普阅读，但无需深入精读。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

