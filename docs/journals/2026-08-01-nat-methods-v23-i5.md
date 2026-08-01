# Nat. Methods — Vol 23  Issue 5  ·  2026-08-01

- 共 8 篇 · Nature Methods
- 目录核对 ⚠️ 疑似漏 19 篇（对照 OpenAlex 27 篇）：10.1038/s41592-026-03043-8、10.1038/s41592-026-03064-3、10.1038/s41592-026-03068-z、10.1038/s41592-026-03061-6、10.1038/s41592-026-03070-5 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Nature Methods》共8篇论文，整体聚焦于**生物成像与分子检测技术的工程化创新**，主线可归纳为三条：**计算成像与信号处理**（NeAT、MicroSplit、超快铅笔光束）、**RNA与基因调控的测序/建模方法**（sm-PORE-cupine、CREsted）、以及**荧光探针与传感器工程**（PinkyCaMP、VIS-Fb、自发闪烁染料）。其中，前两条主线涉及统计建模与机器学习，后一条以化学/生物工程为主。

**计算成像与信号处理**是本期最突出的方法学主线。NeAT利用神经场联合估计波前像差和样本结构，将自适应光学从硬件依赖转向计算驱动，核心是3D图像堆栈中的联合优化问题。MicroSplit采用变分分裂编码器-解码器网络，在单荧光通道中同时成像多个结构后通过计算分离，其模型显式建模后验分布以提供不确定性估计和空间分辨的预测误差。超快铅笔光束则通过自聚焦效应生成旁瓣抑制的贝塞尔型光束，属于物理光学与成像系统的结合，不涉及统计建模。这三篇中，前两篇展示了深度学习/变分推断在显微成像中的典型应用，适合关注计算成像与不确定性量化的读者。

**RNA与基因调控的测序/建模方法**是另一条与统计直接相关的线索。sm-PORE-cupine将SHAPE化学探针与纳米孔直接RNA测序结合，在单分子水平识别RNA结构ensemble，其核心创新在于直接信号对齐（而非碱基映射）提高可映射比例，并采用Bernoulli混合模型聚类分离不同结构ensemble——这是典型的无监督聚类与信号处理结合。CREsted则是一个端到端的深度学习软件包，从单细胞ATAC-seq数据建模细胞类型特异性增强子，核心是卷积神经网络学习序列语法，并支持合成增强子的设计验证。两篇分别涉及混合模型聚类和序列深度学习，适合对RNA结构推断和基因调控建模感兴趣的读者。

**与因果推断/半参数效率/高维方向最贴合的论文**：本期无直接因果推断或半参数效率论文。若从统计建模角度，sm-PORE-cupine的Bernoulli混合模型聚类（涉及混合模型与信号对齐）和MicroSplit的变分推断（涉及后验分布建模与不确定性估计）最贴近统计方法学；CREsted的深度学习序列建模属于高维序列数据预测，但非传统高维统计框架。其余论文均为工程或化学工具开发，无统计理论贡献。

## 其他  *(other, 8 篇)*

### 1. [10.1038/s41592-026-03069-y](https://doi.org/10.1038/s41592-026-03069-y) — Direct RNA sequencing and signal alignment reveal RNA structure ensembles in a eukaryotic cell
- **作者**: Jiaxu Wang, Jian Han, Wen Ting Tan, Anthony Youzhi Cheng, Jong Ghut Ashley Aw, Yue Wang et al.
- **期刊/来源**: Nature Methods
- **机构**: Ministry of Education · Genome Institute of Singapore · Agency for Science, Technology and Research · National University of Singapore · A*STAR Graduate Academy
- **分类**: vol 23 · issue 5 · pp 914-923
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文提出 sm-PORE-cupine 方法，将 SHAPE 化学探针与纳米孔直接 RNA 测序结合，在单分子水平上识别 RNA 结构 ensemble。核心创新在于使用直接信号对齐（而非仅碱基映射）提高可映射序列比例，并采用 Bernoulli 混合模型聚类准确分离不同结构 ensemble。方法应用于 SARS-CoV-2 基因组和白色念珠菌转录组，发现 RNA 在体外、高温及 3' UTR 区域结构更均一，且结构 ensemble 与翻译效率和 RNA 降解相关。作为 Nature Methods 上的方法学论文，本文清晰阐述了数据生成（纳米孔信号）和建模（混合模型聚类）流程，适合作为统计学家了解单分子 RNA 结构分析的入门读物。对您而言，本文属于 gateway reading，其信号对齐和聚类问题可能激发对高维混合模型或序列数据统计方法的兴趣，但核心工具不在您的武器库中，暂不可做。
- **关键技术**: `Bernoulli mixture model`, `direct signal alignment`, `nanopore direct RNA sequencing`, `SHAPE chemical probing`, `single-molecule structure ensemble`
- **为什么对您有用**: 本文属于 Nature Methods 上的方法学论文，作为 gateway reading 对统计学家友好：清晰说明了数据生成（纳米孔电信号）和统计建模（Bernoulli 混合模型聚类）流程，适合了解单分子 RNA 结构分析领域。武器库中的非参数统计和混合模型知识可帮助理解聚类方法，但核心生物学问题和纳米孔信号处理不在熟悉范围内，属于暂不可做的方向。

### 2. [10.1038/s41592-026-03057-2](https://doi.org/10.1038/s41592-026-03057-2) — CREsted: modeling genomic and synthetic cell-type-specific enhancers across tissues and species
- **作者**: Niklas Kempynck, Seppe De Winter, Casper H. Blaauw, Vasileios Konstantakos, Eren Can Ekşi, Sam Dieltiens et al.
- **期刊/来源**: Nature Methods
- **机构**: VIB-KU Leuven Center for Cancer Biology · VIB-KU Leuven Center for Brain & Disease Research · VIB.AI · KU Leuven · Royal Netherlands Academy of Arts and Sciences · University Medical Center Utrecht · Oncode Institute · Illumina (United States) 等
- **分类**: vol 23 · issue 5 · pp 946-959
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文介绍了一个名为 CREsted 的软件包，用于从单细胞 ATAC-seq 数据中建模和设计细胞类型特异性的增强子。该软件整合了数据预处理、基于序列的染色质可及性建模、序列解释与设计等流程，采用深度学习模型（如卷积神经网络）学习增强子的序列语法。作者在多个数据集上验证了 CREsted 的功能，包括小鼠皮层、人类外周血单核细胞、肿瘤间充质样细胞状态比较以及斑马鱼发育图谱。特别地，他们利用斑马鱼模型训练后，设计并体内验证了细胞类型特异性的合成增强子。本文的核心贡献在于提供了一个端到端的、可复现的软件工具，降低了计算生物学中增强子建模与设计的门槛。对于统计计算方向的研究者，该工作展示了如何将深度学习模型与生物数据管道系统性地集成，但其方法学创新性有限，主要是一个工程实现和应用的贡献。
- **关键技术**: `deep learning for sequence modeling`, `single-cell ATAC-seq preprocessing`, `sequence-to-activity prediction`, `in vivo enhancer validation`, `transfer learning / fine-tuning`
- **为什么对您有用**: 本文属于 Nature Methods 上的方法学工具论文，作为 gateway reading 对统计计算研究者有参考价值：(1) 它清晰地展示了从原始测序数据到可解释模型再到实验验证的完整 pipeline，数据结构和模型假设（序列到染色质可及性的映射）阐述得比较清楚，适合作为进入计算基因组学领域的入门读物；(2) 武器库中的 'software development' 和 'high-dimensional asymptotics'（用于理解模型复杂度）可以用于分析其模型的可解释性和泛化误差，但核心深度学习框架不在当前武器库中（缺序列模型和生物信息学背景）；(3) 值得花时间读全文以了解该领域的典型数据结构和建模范式，但不太可能直接催生后续的统计理论工作。

### 3. [10.1038/s41592-026-03082-1](https://doi.org/10.1038/s41592-026-03082-1) — $${\bf{Micro}}{{\mathbb{S}}}{\bf{plit}}$$: semantic unmixing of fluorescent microscopy data
- **作者**: Ashesh Ashesh, Federico Carrara, Igor Zubarev, Vera Galinova, Melisande Croft, Melissa Pezzotti et al.
- **期刊/来源**: Nature Methods
- **机构**: Human Technopole · Università Campus Bio-Medico · University of Pavia · University of Illinois Chicago · University of Chicago · Howard Hughes Medical Institute · Janelia Research Campus
- **分类**: vol 23 · issue 5 · pp 1047-1057
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文提出 MicroSplit，一种基于深度学习的计算多路复用方法，旨在解决荧光显微镜中成像速度、分辨率和光毒性之间的权衡问题。该方法允许在单个荧光通道中同时成像多个细胞结构，然后通过计算将其分离。核心模型是变分分裂编码器-解码器网络（Variational Splitting Encoder-Decoder），它建模了解决方案的后验分布，从而能够进行不确定性感知的预测，并从后验变异性中估计空间分辨的预测误差。实验表明，MicroSplit 能够将多达四个叠加的噪声结构分离为不同的、去噪的图像通道，并在多种数据集、噪声水平和成像条件下表现稳健。该方法还展示了通过减少光子暴露来改善下游分析的能力。所有方法、数据和训练模型均已开源，便于在生物成像中立即采用计算多路复用。
- **关键技术**: `Variational Splitting Encoder-Decoder`, `computational multiplexing`, `uncertainty-aware prediction`, `deep learning for microscopy`
- **为什么对您有用**: 本文属于 Nature Methods 的通用科学论文，作为 gateway reading 对统计学家有入门价值：它清晰地阐述了成像中的多路复用问题（数据侧：噪声、光子预算、结构叠加）和模型侧（变分编码器、后验分布），且问题本身（从叠加噪声信号中分离多个结构）具有统计推断的趣味性。然而，该论文的核心方法是深度学习架构，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接技术重叠，且武器库中缺乏变分推断或深度生成模型的专门工具。作为入门读物值得一读以拓宽视野，但暂不可做 follow-up。

### 4. [10.1038/s41592-026-03053-6](https://doi.org/10.1038/s41592-026-03053-6) — Adaptive optical correction for in vivo two-photon fluorescence microscopy with neural fields
- **作者**: Iksung Kang, Hyeonggeon Kim, Ryan Natan, Qinrong Zhang, Stella X. Yu, Na Ji
- **期刊/来源**: Nature Methods
- **机构**: Korea Advanced Institute of Science and Technology · University of California, Berkeley · City University of Hong Kong · University of Michigan · Berkeley College · Lawrence Berkeley National Laboratory
- **分类**: vol 23 · issue 5 · pp 1037-1046
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文提出 NeAT，一种基于神经场（neural fields）的自适应光学计算框架，用于双光子荧光显微镜的像差校正。NeAT 从 3D 图像堆栈中联合估计波前像差和样本结构，无需外部训练数据，并集成了运动校正和共轭误差校正，适用于商业显微镜。在定制显微镜和商业显微镜上，NeAT 在活体小鼠脑成像中实现了实时像差校正，显著提高了突触和神经元的谷氨酸及钙成像的信号质量和准确性。该方法将自适应光学从硬件依赖转向计算驱动，降低了生物实验室的部署门槛。对您而言，这是一篇 Nature Methods 的通用科学入门读物，展示了神经场在计算成像中的应用，但方法学核心（神经场优化）不在您的主要兴趣或技术武器库中。
- **关键技术**: `neural fields`, `adaptive optics`, `wavefront estimation`, `motion correction`, `two-photon microscopy`
- **为什么对您有用**: 本文属于 general science 范畴的 Nature Methods 论文，作为 gateway reading 评估：(a) 对统计学家友好，清晰解释了自适应光学的生物成像问题和 NeAT 的计算方案，无需深度光学知识；(b) 阐明了更大的科学问题——活体脑成像中像差校正对信号质量的关键作用；(c) 有明确的数据/建模维度：3D 图像堆栈的逆问题、波前像差的参数化估计、运动校正的联合优化，统计学家可关注其不确定性量化或估计效率；(d) 科学趣味性高，适合拓宽视野。但方法核心（神经场优化）与您的 primary interests 无直接技术重叠，且武器库中缺乏神经场/隐式神经表示工具，暂不可做 follow-up。值得花时间读全文作为入门。

### 5. [10.1038/s41592-026-03067-0](https://doi.org/10.1038/s41592-026-03067-0) · [arXiv](https://arxiv.org/abs/2504.11618) — Self-localized ultrafast pencil beam for volumetric multiphoton imaging
- **作者**: Honghao Cao, Sarah Spitz, Li-Yu Yu, Kunzan Liu, Zhengyu Zhang, Federico Presutti et al.
- **期刊/来源**: Nature Methods
- **分类**: vol 23 · issue 5 · pp 1024-1036
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文报道了一种在多模光纤中自发形成的超快铅笔光束，该光束在临界功率附近通过自聚焦效应产生，具有旁瓣抑制的贝塞尔型轮廓和显著改善的稳定性。仅需简单的轴上高斯光束入射即可生成，易于集成到标准多光子显微镜中。作者将该光束应用于小鼠肠神经系统的双光子成像，相比传统贝塞尔光束展现出更低的旁瓣和更强的像差鲁棒性。进一步，在活体人血脑屏障模型中实现了分钟级分辨率的三维扫描，监测转铁蛋白摄取动力学，揭示了不同细胞类型间的时空异质性。该方法提供了一种鲁棒的超快铅笔光束生成方案，支持高通量三维生物系统成像。对您而言，这是一篇典型的Nature Methods方法学论文，属于跨学科科普阅读范畴，不涉及您核心统计兴趣方向的方法论转移。
- **关键技术**: `self-focusing`, `Bessel beam`, `multiphoton microscopy`, `volumetric imaging`, `spatiotemporal localization`
- **为什么对您有用**: 本文属于general science（Nature Methods）的gateway reading，作为数据统计学家可了解生物成像领域的前沿光学方法。武器库中无直接可攻工具，暂不可做。但文章对数据采集和成像模型有清晰描述（噪声、分辨率、三维扫描结构），可作为入门读物拓宽视野。

### 6. [10.1038/s41592-026-03065-2](https://doi.org/10.1038/s41592-026-03065-2) — PinkyCaMP: an mScarlet-based calcium sensor with enhanced brightness, photostability and multiplexing capabilities
- **作者**: Ryan Fink, Shosei Imai, Nala Gockel, German Lauer, Kim Renken, Jonas Wietek et al.
- **期刊/来源**: Nature Methods
- **机构**: University of Bremen · University of Cologne · The University of Tokyo · German Center for Neurodegenerative Diseases · Ruhr University Bochum · Humboldt-Universität zu Berlin · Freie Universität Berlin · Charité - Universitätsmedizin Berlin 等
- **分类**: vol 23 · issue 5 · pp 998-1010
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文报道了PinkyCaMP，一种基于明亮红色荧光蛋白mScarlet的新型基因编码钙离子指示剂。现有红色GECIs普遍存在亮度低、信噪比差、在蓝光下发生光开关等问题，限制了其在全光学实验（结合光遗传学或多色成像）中的应用。PinkyCaMP通过工程改造显著提升了亮度、光稳定性和信噪比，同时完全兼容蓝光光遗传学和双色成像。该传感器在体外和体内均对神经元无毒性或聚集，表现良好。PinkyCaMP支持多种成像模态，包括单光子方法（光纤光度法、宽场成像、微型显微镜成像）以及清醒小鼠的双光子成像。本文属于方法学工具开发，核心贡献在于工程优化而非统计或计算理论。对您而言，这是一篇Nature Methods上的工具论文，可作为跨学科科普阅读了解神经科学成像前沿，但无直接统计方法学迁移价值。
- **关键技术**: `genetically encoded calcium indicator`, `protein engineering`, `fluorescence imaging`, `two-photon microscopy`, `fiber photometry`
- **为什么对您有用**: 本文属于general science（Nature Methods）的gateway reading范畴。作为一篇纯工具开发论文，它没有统计或计算理论成分，但(a) 对神经科学外行读者较为友好，方法部分清晰说明了现有GECIs的局限和PinkyCaMP的改进；(b) 阐明了神经科学领域对钙成像工具的核心需求（亮度、光稳定性、多色兼容性）；(c) 数据维度（成像数据）涉及信号处理问题，但本文未深入讨论统计推断或不确定性量化。武器库中无相关工具可直接攻入，属于暂不可做方向——核心机器（蛋白质工程、光学成像物理）不在武器库内。建议作为科普阅读浏览摘要即可，不值得花时间读全文。

### 7. [10.1038/s41592-026-03056-3](https://doi.org/10.1038/s41592-026-03056-3) — Synthetic multicolor antigen-stabilizable nanobody platform for intersectional labeling and functional imaging
- **作者**: Natalia V. Barykina, Erin M. Carey, Olena S. Oliinyk, Juliana M. Mendonça-Gomes, Sofia de Oliveira, Axel Nimmerjahn et al.
- **期刊/来源**: Nature Methods
- **机构**: Albert Einstein College of Medicine · Salk Institute for Biological Studies · University of Helsinki
- **分类**: vol 23 · issue 5 · pp 972-985
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文报道了一种合成多色抗原稳定荧光纳米抗体（VIS-Fb）平台，覆盖450-660 nm全可见光谱。通过将20多种荧光蛋白和生物传感器工程化嵌入8种纳米抗体，实现了仅在结合目标抗原时发出荧光的通用设计。该平台包括组成型、光激活和光开关型荧光蛋白，以及基于荧光强度的生物传感器。携带生物传感器的VIS-Fb可同时监测两个代谢物在限定位置的动态，而靶向生物传感器的FP-VIS-Fb则能在小鼠脑中进行比率功能成像。研究进一步利用VIS-Fb追踪斑马鱼胚胎中内源β-catenin在正常发育和Wnt信号调控下的动态。该合成生物学平台实现了细胞内蛋白的无背景可视化、多抗原多色检测以及特定细胞群和区室的选择性标记。作为Nature Methods的方法学论文，本文对统计学家而言是了解前沿光学成像工具的优秀入门读物，但方法学本身不涉及统计推断或计算问题。
- **关键技术**: `antigen-stabilizable nanobody`, `fluorescent protein engineering`, `biosensor design`, `multicolor imaging`, `ratiometric functional imaging`
- **为什么对您有用**: 本文属于general science gateway reading范畴（Nature Methods）。作为方法学论文，它清晰地展示了合成生物学工具的设计逻辑和生物成像应用，对统计学家而言是了解现代光学成像技术的好材料，但缺乏直接的统计推断或计算问题。武器库中的工具无法直接应用于本文内容，暂不可做后续统计方法研究。

### 8. [10.1038/s41592-026-03062-5](https://doi.org/10.1038/s41592-026-03062-5) — A series of spontaneously blinking dyes for super-resolution microscopy
- **作者**: Katie L. Holland, Sarah E. Plutkis, Brian P. English, Timothy A. Daugird, Abhishek Sau, Jonathan B. Grimm et al.
- **期刊/来源**: Nature Methods
- **机构**: Howard Hughes Medical Institute · Janelia Research Campus · University of North Carolina at Chapel Hill · Texas A&M University · Texas A&M Health Science Center · North Carolina State University · Albert Einstein College of Medicine · Oregon Health & Science University
- **分类**: vol 23 · issue 5 · pp 909-913
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文报道了一系列自发闪烁荧光染料，无需笼锁基团或氧化还原缓冲液即可在非荧光与荧光形式之间切换，从而实现超分辨率显微成像。这些染料的固有闪烁行为由分子结构决定并受环境调节，不存在适用于所有成像场景的通用荧光染料。研究团队通过调节染料的开关比，使其适用于单分子定位显微镜和超分辨率光学波动成像。实验在体外和细胞中展示了这些染料对生物分子结构的成像能力。本文是化学与成像技术的应用型工作，未涉及统计方法或理论创新。对您而言，这是一篇方法学工具论文，但无直接统计关联。
- **关键技术**: `single-molecule localization microscopy`, `super-resolution optical fluctuation imaging`, `fluorophore engineering`
- **为什么对您有用**: 本文属于化学/成像技术应用，与您的统计研究兴趣无直接关联。作为Nature Methods上的方法学工具论文，它展示了前沿成像技术，但缺乏统计建模或数据分析维度，不适合作为gateway reading。武器库中无相关工具可攻，暂不可做。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

