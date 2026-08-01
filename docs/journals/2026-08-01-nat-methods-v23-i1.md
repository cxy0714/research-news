# Nat. Methods — Vol 23  Issue 1  ·  2026-08-01

- 共 17 篇 · Nature Methods
- 目录核对 ⚠️ 疑似漏 19 篇（对照 OpenAlex 36 篇）：10.1038/s41592-025-02782-4、10.1038/s41592-025-02908-8、10.1038/s41592-025-02942-6、10.1038/s41592-025-02916-8、10.1038/s41592-025-02911-z 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Nature Methods》整体聚焦于**生物医学成像与组学数据的计算工具开发**，主线可归纳为三条：**生成式模型在生物序列与细胞状态预测中的应用**（Squidiff、RFdiffusion2、ImmunoMatch）、**数据缺失与异质性问题的统计/机器学习方法**（LatentSNA、DISK、细胞迁移综述）、以及**实验通量与成像精度的工程化提升**（SmartEM、TIRTL-seq、并行单分子技术、CaBLAM、ExoSloNano、mScarlet3‑S2）。此外，还有若干基准评估（TCR‑表位预测）和资源型工作（DynamicAtlas）。

在生成式模型这条线上，Squidiff 用扩散模型预测单细胞转录组对扰动和分化的响应，本质是高维条件生成；RFdiffusion2 则从原子坐标出发，用深度生成模型直接设计酶活性位点支架，实现了序列无关的蛋白质骨架生成。两者都展示了生成式框架在生物序列与状态空间中的泛化能力，但前者不涉及因果推断，后者是结构生物学应用。ImmunoMatch 则是一个更经典的分类/嵌入模型，用于预测抗体轻重链配对，其数据结构和评估方式对免疫信息学有参考价值。

数据缺失与异质性方面，LatentSNA 提出贝叶斯潜变量模型用于脑网络与行为关联，核心是保留拓扑结构的无偏估计和不确定性量化，在大规模队列中提升了统计功效。DISK 用深度学习填补动物姿态估计中的关键点缺失，利用时空依赖性和潜在表示，但方法本身是纯深度学习应用。两篇细胞迁移综述则系统整理了轨迹分析中的参数提取与异质性量化，可作为生物医学数据分析的入门参考。

与因果推断/半参数效率/高维统计最贴合的论文是：**LatentSNA**（贝叶斯潜变量模型，涉及无偏估计与不确定性量化）、**Squidiff**（高维条件生成模型，虽非因果但可视为反事实预测的生成式替代）、以及**TCR‑表位预测的基准评估**（涉及混杂控制与泛化性评估，对高维分类模型的评估框架有参考价值）。其余论文多为工程化工具或领域特定应用，统计方法论贡献有限。

## 其他  *(other, 17 篇)*

### 1. [10.1038/s41592-025-02896-9](https://doi.org/10.1038/s41592-025-02896-9) — Latent space-based network analysis for brain–behavior linking in neuroimaging
- **作者**: Selena Wang, Xinzhi Zhang, Yunhe Liu, Wanwan Xu, Xinyuan Tian, Yize Zhao
- **期刊/来源**: Nature Methods
- **机构**: Indiana University Health · Indiana University School of Medicine · Indiana University – Purdue University Indianapolis · Yale University · Texas A&M University
- **分类**: vol 23 · issue 1 · pp 225-235
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文提出 LatentSNA，一种基于潜变量空间（latent space）的生成式贝叶斯网络统计方法，用于神经影像中的脑-行为关联分析。该方法将网络科学嵌入贝叶斯框架，保留神经学上有意义的脑拓扑结构，旨在解决当前成像生物标志物检测中统计功效不足和 II 类错误膨胀的问题。LatentSNA 能够无偏估计生物标志物对行为变异的影响，量化不确定性，并评估估计效应相对于随机水平的似然性。在多个大规模队列（8,003–11,861 名参与者）中，该方法在中等至大数据集上实现了平均 110–150% 的准确率提升和 153% 的可重复性改进。本文属于应用方法学贡献，方法本身是领域特定的贝叶斯潜变量模型，而非通用统计理论创新。对您而言，这是一篇 Nature Methods 的入门级阅读材料，展示了统计网络分析在神经科学中的应用，但方法论迁移性有限。
- **关键技术**: `latent space model`, `Bayesian generative framework`, `network topology preservation`, `imaging biomarker detection`, `brain-behavior association`
- **为什么对您有用**: 本文属于 general science 范畴（Nature Methods），作为 gateway reading 适合了解统计网络分析在神经影像中的应用。武器库中的非参数统计和软件工程经验可帮助理解其贝叶斯框架，但核心方法（潜变量空间网络模型）与您的主要兴趣方向（因果推断、高维统计、U-统计量）无直接技术交集。本文值得花时间读全文作为科普拓展，但暂不可做 follow-up 工作，因为缺少与您武器库的直接连接点。

### 2. [10.1038/s41592-025-02935-5](https://doi.org/10.1038/s41592-025-02935-5) — Methods to analyze cell migration data: fundamentals and practical guidelines
- **作者**: Pei-Hsun Wu, Jude M. Phillip, Wenxuan Du, Andre Forjaz, Praful R. Nair, Denis Wirtz
- **期刊/来源**: Nature Methods
- **机构**: Johns Hopkins University · Johns Hopkins Medicine
- **分类**: vol 23 · issue 1 · pp 43-55
- 相关性 7/10 · novelty: `survey`
- **摘要**: 本文是 Nature Methods 上的一篇综述，系统介绍从细胞迁移实验原始数据中提取定量参数的基本原理与实用指南。核心参数包括细胞速度、均方位移、扩散系数、持久性、各向异性等，并讨论了如何量化细胞异质性。文章还介绍了包括基于 AI 的追踪方法在内的新型成像与计算技术，旨在为从实验设计到数据分析的全流程提供实用指导。作为一篇方法学综述，本文并未提出新的统计理论或方法，而是整合现有分析工具并给出最佳实践建议。对于统计研究者而言，本文可作为了解生物医学成像数据分析中常见统计问题（如轨迹分析、异质性量化）的入门读物。
- **关键技术**: `mean-squared displacement`, `cell tracking`, `persistence analysis`, `anisotropy quantification`, `AI-based image analysis`
- **为什么对您有用**: 本文属于 general science 范畴的 gateway reading，适合作为统计研究者了解细胞迁移数据分析的入门读物。文章清晰阐述了数据结构和分析流程（轨迹、噪声、异质性），但核心统计工具（如均方位移、扩散模型）不在研究者当前武器库的核心范围内，且缺乏与 primary interest（因果推断、高维统计、U-统计量）的直接连接。作为 Nature Methods 上的方法学综述，值得花时间阅读以拓宽视野，但暂不可做后续方法学跟进。

### 3. [10.1038/s41592-025-02910-0](https://doi.org/10.1038/s41592-025-02910-0) — Assessment of computational methods in predicting TCR–epitope binding recognition
- **作者**: Yanping Lu, Yuyan Wang, Meng Xu, Bingbing Xie, Yumeng Yang, Haodong Xu et al.
- **期刊/来源**: Nature Methods
- **机构**: Yunnan University · ShanghaiTech University · Chinese Academy of Sciences · Guangzhou Institutes of Biomedicine and Health · University of Chinese Academy of Sciences · Sun Yat-sen University · Sun Yat-sen University Cancer Center · Central South University 等
- **分类**: vol 23 · issue 1 · pp 248-259
- 相关性 7/10 · novelty: `application`
- **摘要**: 该论文系统评估了50种TCR-表位结合预测模型在21个数据集上的性能，覆盖762个表位和数十万结合TCR。研究发现负样本来源显著影响模型准确性，外部负样本可能引入未控制的混杂因素。模型性能通常随每个表位的TCR数量增加而提升，凸显大规模多样化数据集的重要性。融合多特征的模型通常优于仅使用CDR3β信息的模型，但所有模型在泛化到未见表位时仍存在困难。独立测试集对无偏评估至关重要。这些发现为开发更准确、更可泛化的TCR-表位预测模型提供了指导。作为Nature Methods上的基准评估论文，其方法学贡献有限，但数据规模和评估框架对免疫信息学领域有参考价值。
- **关键技术**: `benchmark evaluation`, `negative sampling`, `generalization assessment`, `feature integration`
- **为什么对您有用**: 本文属于Nature Methods上的基准评估论文，作为gateway reading，其数据规模（762表位、50模型）和评估框架（负样本来源、泛化性）对统计学家有入门价值，但方法学新颖性有限。武器库中'软件工程'能力可复现其评估流程，但核心免疫学问题与主要兴趣方向（因果推断、高维统计等）无直接连接，属于暂不可做的领域。

### 4. [10.1038/s41592-025-02913-x](https://doi.org/10.1038/s41592-025-02913-x) — ImmunoMatch learns and predicts cognate pairing of heavy and light immunoglobulin chains
- **作者**: Dongjun Guo, Deborah K. Dunn-Walters, Franca Fraternali, Joseph C. F. Ng
- **期刊/来源**: Nature Methods
- **机构**: King's College London · Institute of Structural and Molecular Biology · University College London · University of Surrey · Birkbeck, University of London
- **分类**: vol 23 · issue 1 · pp 106-117
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文提出 ImmunoMatch，一个基于配对 B 细胞重链（H）和轻链（L）序列训练的机器学习框架，用于预测抗体 H-L 链的天然配对兼容性。模型区分 cognate 配对与随机配对，并捕捉 κ 与 λ 轻链的差异，反映骨髓中 B 细胞选择机制。方法应用于空间 VDJ 测序数据重建配对抗体，并研究健康与疾病状态下 B 细胞成熟过程中 H-L 配对的精炼。模型对 H-L 界面序列差异敏感，揭示了抗体组装与稳定性的生物学原理。作为 Nature Methods 的方法学论文，本文清晰阐述了数据（配对序列）和模型（分类/嵌入）结构，适合作为计算生物学入门读物。对您而言，本文属于 gateway reading，武器库中的非参数统计和软件工程经验可辅助理解其机器学习流程，但核心问题（抗体配对预测）与您的主要兴趣方向无直接方法学迁移点，不值得深入跟进。
- **关键技术**: `machine learning`, `sequence embedding`, `paired B cell receptor sequencing`, `VDJ recombination`
- **为什么对您有用**: 本文属于 Nature Methods 的通用科学 gateway reading，数据（配对序列）和模型（分类器）结构清晰，适合作为计算生物学入门。武器库中的非参数统计和软件工程经验可辅助理解其流程，但核心问题（抗体配对预测）与您的主要兴趣（因果推断、高维统计、U-统计量）无直接方法学迁移点，不值得花时间全文阅读。

### 5. [10.1038/s41592-025-02877-y](https://doi.org/10.1038/s41592-025-02877-y) — Squidiff: predicting cellular development and responses to perturbations using a diffusion model
- **作者**: Siyu He, Yuefei Zhu, Daniel Naveed Tavakol, Haotian Ye, Yeh-Hsing Lao, Zixian Zhu et al.
- **期刊/来源**: Nature Methods
- **机构**: Columbia University Irving Medical Center · Columbia University · Stanford University · University at Buffalo, State University of New York
- **分类**: vol 23 · issue 1 · pp 65-77
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文提出 Squidiff，一个基于扩散模型的生成式框架，用于预测单细胞转录组在细胞分化、基因扰动和药物响应下的变化。模型通过连续去噪和语义特征整合，学习瞬态细胞状态并预测高分辨率转录组景观。在血管类器官发育、中子辐射和生长因子响应等场景中验证了其鲁棒性。该方法本质上是一个高维条件生成模型，不涉及因果推断或统计效率理论。对您而言，这是一篇 Nature Methods 的通用科学入门读物，展示了扩散模型在生物信息学中的应用，但方法论上无直接可迁移性。
- **关键技术**: `diffusion model`, `single-cell RNA-seq`, `generative framework`, `continuous denoising`, `semantic feature integration`
- **为什么对您有用**: 本文属于 general science 范畴的 gateway reading。作为 Nature Methods 文章，它清晰阐述了单细胞数据结构和生成模型的建模思路，适合作为生物信息学入门读物。但武器库中无扩散模型相关工具，且问题不涉及因果推断或高维统计理论，暂不可做 follow-up。

### 6. [10.1038/s41592-025-02880-3](https://doi.org/10.1038/s41592-025-02880-3) — C-COMPASS: a user-friendly neural network tool profiles cell compartments at protein and lipid levels
- **作者**: Daniel T. Haas, Daniel Weindl, Pamela Kakimoto, Eva-Maria Trautmann, Julia P. Schessner, Xia Mao et al.
- **期刊/来源**: Nature Methods
- **机构**: Helmholtz Zentrum München · Deutsches Diabetes-Zentrum e.V. · German Center for Diabetes Research · Heinrich Heine University Düsseldorf · University of Bonn · Max Planck Institute of Biochemistry · Regeneron (United States) · Max Delbrück Center 等
- **分类**: vol 23 · issue 1 · pp 118-130
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文介绍 C-COMPASS，一个基于神经网络回归模型的开源软件工具，用于系统性地预测蛋白质和脂质在细胞内的空间分布。该方法利用蛋白质相关性谱和 LOPIT 等细胞器组学数据，能够处理复杂的多定位模式，并通过整合蛋白质丰度建模不同条件下的细胞器组成变化。在脂质定位方面，C-COMPASS 通过共生成的标记蛋白谱训练神经网络，克服了缺乏细胞器特异性脂质标记的难题。作者将其应用于人源化小鼠肝脏数据，揭示了代谢扰动下的细胞器重塑。该工具无需高级计算技能，旨在为蛋白质组学和脂质组学的多组学细胞器动态研究提供易用平台。作为 Nature Methods 的方法学论文，本文对统计学家而言是了解计算细胞生物学中数据建模问题的入门读物，但其方法学创新性有限，核心贡献在于软件工程和易用性。
- **关键技术**: `neural network regression`, `protein correlation profiling`, `LOPIT`, `multi-organelle profiling`, `lipid spatial profiling`
- **为什么对您有用**: 本文属于 general science 范畴的 Nature Methods 方法学论文，作为 gateway reading 对统计学家有参考价值：它清晰展示了细胞器组学数据的结构（蛋白质丰度谱、标记物集）和建模目标（多定位预测），数据维度与噪声结构明确，是一个值得统计方法介入的 inference 问题。但本文核心贡献在软件工程而非统计理论，武器库中的非参数统计或高维方法难以直接迁移。暂不可做——核心机器（神经网络回归与组学数据整合）不在武器库中，且问题本身更偏向计算生物学而非统计推断。

### 7. [10.1038/s41592-025-02893-y](https://doi.org/10.1038/s41592-025-02893-y) — Deep Imputation for Skeleton data (DISK) for behavioral science
- **作者**: France Rose, Monika Michaluk, Timon Blindauer, Bogna M. Ignatowska-Jankowska, Liam O’Shaughnessy, Greg J. Stephens et al.
- **期刊/来源**: Nature Methods
- **机构**: University of Cologne · University Hospital Cologne · University of Warsaw · Okinawa Institute of Science and Technology Graduate University · Vrije Universiteit Amsterdam · Okinawa University · Salk Institute for Biological Studies · Cologne Excellence Cluster on Cellular Stress Responses in Aging Associated Diseases
- **分类**: vol 23 · issue 1 · pp 236-247
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文提出一种名为 DISK 的深度学习方法，用于填补动物姿态估计数据中缺失的关键点坐标。该方法利用关键点之间的空间依赖性和时间动力学信息进行插补，无需人工标注。作者在七种动物骨架数据（包括多动物场景）上验证了性能，表明插补后的数据能检测到更多运动事件（如步态），并在实验条件间比较时得到更稳健的统计结果。此外，DISK 在学习插补的过程中还学到了有意义的潜在表示，可捕捉底层动作。该方法作为独立软件包发布，适用于基于标记或无标记的追踪系统输出。作为 Nature Methods 上的方法学论文，本文对统计学家而言是了解动物行为学中数据缺失问题的良好入门读物，但方法本身是纯深度学习应用，与您的主要统计兴趣（因果推断、高维、U-统计量等）无直接技术重叠。
- **关键技术**: `deep learning imputation`, `pose estimation`, `keypoint tracking`, `spatiotemporal dependencies`, `animal kinematics`
- **为什么对您有用**: 本文属于 Nature Methods 上的方法学论文，作为 gateway reading 值得一读：(a) 对非动物行为学背景的统计学家友好，问题设定清晰（追踪数据缺失），方法框架自包含；(b) 数据维度（关键点坐标序列）和缺失模式（随机/系统性）是统计学家能理解的建模问题；(c) 武器库中的非参数统计和逆问题经验可用于思考更高效的插补策略（如利用低秩结构或时间序列模型），但核心深度学习工具不在武器库中，因此暂不可做直接的方法改进。

### 8. [10.1038/s41592-025-02907-9](https://doi.org/10.1038/s41592-025-02907-9) — TIRTL-seq: deep, quantitative and affordable paired TCR repertoire sequencing
- **作者**: Mikhail V. Pogorelyy, Allison M. Kirk, Samir Adhikari, Anastasia A. Minervina, Balaji Sundararaman, Kasi Vegesana et al.
- **期刊/来源**: Nature Methods
- **机构**: St. Jude Children's Research Hospital
- **分类**: vol 23 · issue 1 · pp 56-64
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文介绍 TIRTL-seq，一种高通量、低成本的配对 T 细胞受体（TCR）α/β 链测序方法。该方法在 384 孔板中并行生成数百个 TCR 文库，每板成本低于 200 美元，支持队列规模的配对 TCR 测序。实验流程结合了 bulk TCR-seq 的成本优势和单细胞技术的配对准确性，可同时提供精确的克隆频率估计和链配对信息。作者用纵向样本将其与 10x Genomics 和 bulk 方法对比，验证了 SARS-CoV-2 和 EBV 特异性克隆扩增的动态检测能力。作为 Nature Methods 上的方法学论文，本文对您作为统计学家而言是很好的入门读物：它清晰展示了免疫组库测序的数据结构（稀疏计数、配对约束、克隆扩增动态），但方法本身是实验和计算流程，不涉及您核心兴趣中的统计推断或计算复杂度理论。
- **关键技术**: `TCR repertoire sequencing`, `paired-chain sequencing`, `384-well plate library generation`, `clonal frequency estimation`
- **为什么对您有用**: 本文属于 general science / Nature Methods 的 gateway reading。作为统计学家，您可以从本文了解免疫组库数据的生成过程、配对约束和克隆频率估计问题，但武器库中无直接可攻的技术口子（不涉及因果推断、高维统计或计算复杂度）。本文适合作为拓宽科学视野的入门读物，不值得投入全文精读。

### 9. [10.1038/s41592-025-02929-3](https://doi.org/10.1038/s41592-025-02929-3) — SmartEM: machine learning-guided electron microscopy
- **作者**: Yaron Meirovitch, Ishaan Singh Chandok, Core Francisco Park, Pavel Potocek, Lu Mi, Shashata Sawmya et al.
- **期刊/来源**: Nature Methods
- **机构**: Harvard University · Harvard University Press · Thermo Fisher Scientific (Netherlands) · Saarland University · Allen Institute for Brain Science · Allen Institute · Massachusetts Institute of Technology · Johns Hopkins University Applied Physics Laboratory
- **分类**: vol 23 · issue 1 · pp 193-204
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文提出 SmartEM，一种将机器学习集成到单束扫描电子显微镜实时图像采集中的方法，旨在加速连接组学（connectomics）中的高分辨率成像。传统上，机器学习仅用于成像后的图像分割与重建，而 SmartEM 将推理前置到采集阶段：先以短像素驻留时间快速扫描全区域，再通过实时分析识别需要更高信噪比的子区域，仅对这些子区域进行慢速重扫描。该方法在秀丽隐杆线虫、小鼠和人类脑组织样本上实现了约 7 倍的成像加速，并在小鼠皮层部分重建中达到了与传统电子显微镜相当的精度。SmartEM 本质上是一种数据感知的自适应采样策略，其核心是实时图像质量评估与资源分配。对于您而言，本文属于计算成像与实验设计的交叉，虽不直接对应您的主要统计兴趣，但其“先粗扫再精扫”的自适应采样思想与统计中的两阶段抽样或序贯设计有概念上的联系，可作为跨领域阅读的入门材料。
- **关键技术**: `adaptive sampling`, `real-time machine learning`, `scanning electron microscopy`, `connectomics`, `image quality assessment`
- **为什么对您有用**: 本文属于 general science / Nature Methods 的 gateway reading。作为数据统计学家，您可以从本文中看到：自适应采样策略如何将计算资源与成像时间分配到信息量最大的区域——这与统计中的序贯实验设计、两阶段抽样和主动学习有概念上的共鸣。武器库中的非参数统计和 minimax 界工具可用于分析这种自适应策略的统计效率（例如，在给定总像素预算下，最优的粗扫/精扫分配比）。本文不要求您具备电子显微镜专业知识，适合作为跨领域阅读的入门材料，值得花时间读全文以拓宽视野。

### 10. [10.1038/s41592-025-02897-8](https://doi.org/10.1038/s41592-025-02897-8) — DynamicAtlas: a morphodynamic atlas for Drosophila development
- **作者**: Matthew F. Lefebvre, Vishank Jain-Sharma, Nikolas Claussen, Noah P. Mitchell, Marion K. Raich, Hannah J. Gustafson et al.
- **期刊/来源**: Nature Methods
- **机构**: University of California, Santa Barbara · University of Chicago · Technical University of Munich · Quantitative BioSciences · Max Planck Institute of Psychiatry
- **分类**: vol 23 · issue 1 · pp 260-270
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文构建了果蝇胚胎发育的形态动力学图谱（DynamicAtlas），整合了500个野生型与18个突变体胚胎的活体与静态成像数据，并统一对齐到共同的形态学时间轴。核心发现是野生型表面组织流动呈现离散的“形态动力学模块”——即全局运动模式在特定时间段内保持平稳，这些模块与关键发育阶段对应。突变体分析表明，沿背-腹轴打破空间对称性的基因决定了平稳流动模式。温度扰动实验揭示，形态动力学模块的变化响应于累积的组织变形而非绝对时间。该方法还扩展至胚胎中肠的三维动态表面协变测量。本文本质上是发育生物学的数据资源与现象学发现，而非统计学方法学贡献。
- **关键技术**: `live imaging`, `morphodynamic atlas`, `tissue flow analysis`, `morphological timeline alignment`, `mutant phenotyping`
- **为什么对您有用**: 本文属于Nature Methods上的发育生物学资源论文，作为gateway reading，其数据规模（500胚胎）和动态对齐流程对统计学家有入门价值，但缺乏明确的统计推断或建模问题（如不确定性量化、高维流场降维）。武器库中无直接可攻口子，暂不可做。

### 11. [10.1038/s41592-025-02890-1](https://doi.org/10.1038/s41592-025-02890-1) — Selecting the optimal cell migration assay: fundamentals and practical guidelines
- **作者**: Wenxuan Du, Praful R. Nair, Andre Forjaz, Jude M. Phillip, Pei-Hsun Wu, Denis Wirtz
- **期刊/来源**: Nature Methods
- **机构**: Johns Hopkins University · Johns Hopkins Medicine
- **分类**: vol 23 · issue 1 · pp 30-42
- 相关性 4/10 · novelty: `survey`
- **摘要**: 本文是一篇综述，系统介绍了十种常用的体外和体内细胞迁移实验方法，包括划痕实验、Transwell、微流控芯片等。文章的核心贡献在于提供了一个实用的决策树和选择指南，帮助研究者根据具体的生物学问题（如二维 vs 三维迁移、单细胞 vs 群体迁移、趋化性 vs 机械引导）选择最合适的实验方案。文章详细讨论了每种实验的优缺点、适用场景、数据采集要求和常见陷阱。作为 Nature Methods 的综述，本文面向生物学家，语言通俗，不涉及高级统计方法。对您而言，这是一篇跨学科的通识阅读材料，有助于了解细胞生物学中一个核心实验范式的数据生成过程和数据特点，但本身不提供可直接迁移的统计方法。
- **关键技术**: `cell migration assay`, `live-cell microscopy`, `decision tree`, `in vitro assay`, `in vivo assay`
- **为什么对您有用**: 本文属于 general science 通识阅读范畴（Nature Methods）。作为一篇面向非专家的综述，它清晰阐述了细胞迁移实验的数据结构（时间序列图像、轨迹、速度、方向性）和噪声来源（细胞异质性、微环境变化），对统计学家而言是了解该领域数据生成机制的良好入门读物。武器库中的非参数统计和软件工具可用于分析此类轨迹数据，但本文本身不提供新方法，属于暂不可做的通识阅读。

### 12. [10.1038/s41592-025-02905-x](https://doi.org/10.1038/s41592-025-02905-x) — Orthogonal RNA-regulated destabilization domains for three-color RNA imaging with minimal RNA perturbation
- **作者**: Tien G. Pham, Omoyemi Ajayi, Jiaze He, Irina Sagarbarria, Jeanne A. Hardy, Jiahui Wu
- **期刊/来源**: Nature Methods
- **机构**: University of Massachusetts Amherst
- **分类**: vol 23 · issue 1 · pp 165-174
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文报道了两种正交的RNA调控去稳定化结构域（mDeg和pDeg），用于活细胞中三色mRNA成像。此前单色RNA成像方法存在RNA标签过长导致RNA不稳定的问题。新方法通过设计正交的去稳定化结构域，实现了对结合在内质网膜、质膜内表面和胞质中的mRNA同时成像。mDeg系统比先前报道的tDeg系统检测mRNA更有效，且可与短RNA标签（9XMS2）结合，在不影响RNA稳定性的前提下实现单分子RNA成像。该工作为活细胞中多色RNA动态研究提供了新工具。作为Nature Methods上的方法学论文，本文对统计学家而言是了解前沿生物成像技术的入门读物，但方法论上无直接统计贡献。
- **关键技术**: `live-cell RNA imaging`, `RNA-regulated destabilization domain`, `orthogonal protein domains`, `single-molecule fluorescence microscopy`
- **为什么对您有用**: 本文属于Nature Methods上的方法学论文，适合作为gateway reading了解活细胞RNA成像的前沿技术。武器库中的统计工具（如非参数统计、高维渐近）与此文无直接接口，但作为跨学科阅读可拓宽视野。值得花时间读全文以了解生物成像领域的数据生成机制和实验设计，但无需期待方法论迁移。

### 13. [10.1038/s41592-025-02944-4](https://doi.org/10.1038/s41592-025-02944-4) — Parallel stopped-flow interrogation of diverse biological systems at the single-molecule scale
- **作者**: Roman Kiselev, Ryan A. Brady, Arnab Modak, F. Aaron Cruz-Navarrete, Jose L. Alejo, Daniel S. Terry et al.
- **期刊/来源**: Nature Methods
- **机构**: St. Jude Children's Research Hospital · New York Psychoanalytic Society and Institute · New York State Psychiatric Institute · Columbia University
- **分类**: vol 23 · issue 1 · pp 78-87
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文介绍了一种并行快速交换单分子荧光和单分子FRET技术，旨在解决传统单分子成像方法通量低、实验变异大的问题。该方法通过同时进行稳态和预稳态测量，实现了对多个生物样本的并行分析。作者利用该技术阐明了β-arrestin1激活过程中不同构象事件的时间顺序，揭示了抗生素对mRNA解码保真度的影响，并证明了内源性核糖体RNA序列变异可调节抗生素敏感性。该方法具有通用性和可扩展性，有望提高单分子生物分子功能定量研究的范围和可重复性。作为一篇方法学论文，其核心贡献在于实验硬件和流程的并行化，而非统计推断或计算方法的创新。对您而言，本文属于Nature Methods上的跨学科前沿技术，可作为了解单分子生物物理实验数据生成过程的入门读物，但其中不涉及您主要关注的因果推断、高维统计或计算复杂性等方向。
- **关键技术**: `single-molecule FRET`, `parallel stopped-flow`, `pre-steady-state kinetics`, `microfluidics`
- **为什么对您有用**: 本文属于Nature Methods上的跨学科前沿技术，适合作为gateway reading了解单分子生物物理实验的数据生成过程。武器库中的非参数统计和软件工程能力可用于分析此类实验产生的时序荧光轨迹数据，但本文本身不涉及您主要关注的因果推断、高维统计或计算复杂性理论。作为入门读物，它清晰地展示了实验设计、数据结构和噪声来源，值得花时间阅读全文以拓宽视野，但中期内难以直接转化为您的研究问题。

### 14. [10.1038/s41592-025-02975-x](https://doi.org/10.1038/s41592-025-02975-x) — Atom-level enzyme active site scaffolding using RFdiffusion2
- **作者**: Woody Ahern, Jason Yim, Doug Tischer, Saman Salike, Seth M. Woodbury, Donghyo Kim et al.
- **期刊/来源**: Nature Methods
- **机构**: University of Washington · Massachusetts Institute of Technology · Howard Hughes Medical Institute · PDL BioPharma (United States)
- **分类**: vol 23 · issue 1 · pp 96-105
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文提出 RFdiffusion2，一种基于深度生成模型的原子级酶活性位点支架设计方法。传统方法需预先指定催化残基的序列位置和主链构象，而 RFdiffusion2 直接从反应过渡态周围功能基团的原子坐标出发，无需逆旋转异构体生成，实现了序列无关的活性位点支架设计。在 41 个多样活性位点的计算机基准测试中，RFdiffusion2 成功构建了所有位点的蛋白质支架，而此前最先进的深度学习方法仅成功 16/41。针对三个不同催化位点的实验验证中，每个位点仅测试不到 96 条序列即鉴定出活性催化剂。该方法展示了原子分辨率生成模型在直接从反应机制设计全新酶方面的潜力。作为 Nature Methods 上的方法学论文，本文对统计研究者而言是了解计算生物学前沿的入门读物，但方法本身（扩散模型、蛋白质结构预测）与您的核心统计兴趣（因果推断、高维统计、U-统计量等）无直接技术关联。
- **关键技术**: `diffusion model`, `protein backbone generation`, `atomic coordinate conditioning`, `sequence-agnostic design`, `RosettaFold`
- **为什么对您有用**: 本文属于 general science 范畴的 gateway reading。作为 Nature Methods 上的方法学论文，它清晰阐述了计算生物学中的生成模型问题，数据侧（蛋白质结构、序列）和模型侧（扩散过程、条件生成）的 exposition 对统计研究者友好。但您的武器库（非参数统计、U-统计量、因果推断）与本文核心方法（蛋白质扩散模型）无直接交集，属于暂不可做方向——缺乏蛋白质结构建模和扩散模型训练的专业知识。值得花时间读全文作为跨学科视野拓展，但不适合作为方法学迁移的起点。

### 15. [10.1038/s41592-025-02972-0](https://doi.org/10.1038/s41592-025-02972-0) — CaBLAM: a high-contrast bioluminescent Ca2+ indicator derived from an engineered Oplophorus gracilirostris luciferase
- **作者**: Gerard G. Lambert, Emmanuel L. Crespo, Jeremy Murphy, Kevin L. Turner, Emily Gershowitz, Michaela Cunningham et al.
- **期刊/来源**: Nature Methods
- **机构**: University of California San Diego · Central Michigan University · Allen Institute for Brain Science · New York University · University of North Carolina at Chapel Hill · Technical University of Munich · Scintillon Institute · University of Edinburgh
- **分类**: vol 23 · issue 1 · pp 205-215
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文报道了一种新型生物发光钙指示剂 CaBLAM，它基于工程化的 Oplophorus gracilirostris 荧光素酶改造而成。与传统的荧光 GECI 相比，CaBLAM 无需激发光，从而避免了光漂白、背景自发荧光和光毒性等伪影。该指示剂在信号对比度上实现了数量级的提升，且其钙亲和力可调，能够匹配生理细胞质钙浓度。实验表明，CaBLAM 可在培养神经元中实现视频帧率的单细胞和亚细胞活动成像，并能在清醒行为动物中持续成像数小时。这些性能使 CaBLAM 成为荧光 GECI 的稳健通用替代方案，将钙成像推广到激发光不适用或不可行的场景。作为 Nature Methods 上的方法学论文，本文对统计学家而言是了解生物发光成像这一新兴领域的入门读物，但其中不涉及统计推断或数据建模问题。
- **关键技术**: `bioluminescent calcium indicator`, `engineered luciferase`, `genetically encoded calcium indicator (GECI)`, `in vivo imaging`
- **为什么对您有用**: 本文属于 general science 范畴的 Nature Methods 论文，作为 gateway reading 来看：(a) 对生物发光成像的门外汉而言，文章在方法原理和实验验证上写得较为清晰，但需要一定的分子生物学背景；(b) 文章很好地阐述了为什么生物发光成像比荧光成像有优势，以及 CaBLAM 解决了哪些关键瓶颈；(c) 从数据/建模维度看，本文是纯实验方法学贡献，没有统计推断或不确定性量化问题，统计学家难以从中找到方法学切入点；(d) 作为跨学科阅读，了解生物发光成像的基本原理和进展有一定价值。综合判断：这是一篇优秀的实验方法学论文，但对统计学家而言作为 gateway reading 的价值有限，不值得花时间读全文。

### 16. [10.1038/s41592-025-02928-4](https://doi.org/10.1038/s41592-025-02928-4) — ExoSloNano: multimodal nanogold labels for identification of macromolecules in live cells and cryo-electron tomograms
- **作者**: Lindsey N. Young, Alice Sherrard, Huabin Zhou, Farhaz Shaikh, Joshua Hutchings, Margot Riggi et al.
- **期刊/来源**: Nature Methods
- **机构**: University of California San Diego · Yale University · The University of Texas Southwestern Medical Center · University of California, San Francisco · Chan Zuckerberg Initiative (United States) · Max Planck Institute of Biochemistry · Howard Hughes Medical Institute · Yale Cancer Center
- **分类**: vol 23 · issue 1 · pp 131-142
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文介绍了一种名为 ExoSloNano 的多模态纳米金标记系统，用于在活细胞和冷冻电子断层扫描（cryo-ET）中识别特定蛋白质。该方法通过将纳米金探针引入活细胞，在不破坏分子网络和细胞活性的前提下，实现对细胞质和核蛋白的高效标记。结合相关光电子显微镜（CLEM）和树脂包埋电子显微镜，该系统能够在从微米到纳米的多尺度上定位目标蛋白。在 cryo-ET 中，纳米金探针提供高对比度的电子密度信号，使得小尺寸或低拷贝数的蛋白质得以在原生细胞环境中被识别。实验展示了该系统在室温电子显微镜和 cryo-ET 中的有效性，并解析了相关结构。该工作扩展了电子显微镜可探测的蛋白质组范围，为原位结构生物学提供了新工具。
- **关键技术**: `correlative light and electron microscopy (CLEM)`, `cryo-electron tomography (cryo-ET)`, `nanogold labeling`, `live-cell labeling`, `multimodal imaging`
- **为什么对您有用**: 本文属于 Nature Methods 上的方法学论文，作为 gateway reading 对统计学家有吸引力：(1) 文章清晰阐述了 cryo-ET 数据中的蛋白质识别问题——小尺寸、低拷贝数、原生环境下的目标检测，这是一个典型的信号检测与定位问题，统计学家能理解其数据结构和挑战；(2) 虽然方法本身是湿实验技术，但其核心问题（在噪声背景中识别稀疏信号）与高维统计中的稀疏检测问题有概念上的连接，可作为跨领域阅读拓宽视野；(3) 武器库中的非参数统计和 minimax 理论可用于思考此类标记效率的理论极限，但当前缺乏 cryo-ET 图像处理的具体概率模型知识，属于暂不可做方向。

### 17. [10.1038/s41592-025-02962-2](https://doi.org/10.1038/s41592-025-02962-2) — A highly photostable monomeric red fluorescent protein for dual-color 3D STED and time-lapse 3D SIM imaging
- **作者**: Ya Ding, Wenting He, Kunhao Wang, Fudong Xue, Ke Zheng, Shiqun Zhao et al.
- **期刊/来源**: Nature Methods
- **机构**: Chinese Academy of Sciences · Institute of Biophysics · University of Chinese Academy of Sciences · Nankai University · Peking University · Beijing Institute of Optoelectronic Technology · Beijing Founder Electronics (China) · Zhejiang University
- **分类**: vol 23 · issue 1 · pp 143-152
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文报道了一种新型红色荧光蛋白mScarlet3‑S2，其光稳定性相比前代mScarlet3提升了29倍，且优于现有其他红色荧光蛋白。该蛋白适用于结构光照明显微镜（SIM）和受激发射损耗显微镜（STED）的长时间2D和3D成像。利用mScarlet3‑S2，作者在3D STED成像中实现了超过150个Z-stack的采集，清晰揭示了内质网（ER）的精细结构。关键发现包括非平面ER连接、核膜（NE）内陷、ER–NE接触的3D图谱、多种接触形态类型（点状、带状和分支状）以及极化的ER–NE连接分布。这些结果重新定义了对ER–NE界面的结构理解，展示了mScarlet3‑S2在揭示亚细胞复杂性方面的价值。作为一篇Nature Methods上的方法学论文，它提供了可复用的荧光探针工具，但统计方法学贡献有限，适合作为科普性阅读了解超分辨成像的前沿工具。
- **关键技术**: `fluorescence microscopy`, `STED`, `SIM`, `protein engineering`, `photostability assay`
- **为什么对您有用**: 本文属于Nature Methods上的方法学工具论文，作为gateway reading，它清晰阐述了超分辨成像中光稳定性这一核心实验瓶颈，并提供了可复用的探针方案，适合统计学家了解生物成像数据采集的前沿工具。武器库中的非参数统计和软件工具可用于分析此类成像数据（如点模式分析、空间统计），但本文本身不涉及统计方法创新，属于暂不可做的领域——核心机器（荧光蛋白工程）不在武器库中。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

