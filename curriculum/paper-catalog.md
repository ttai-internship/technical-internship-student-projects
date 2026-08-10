# 论文阅读目录（30 篇）

这份目录用于中高级学生的阅读选择，不是要求一期开完 30 篇。导师按学生基础、周期和设备从中挑选一篇，再锁定数据、代码许可、随机种子、指标和可运行范围。`analysis` 只能做论文分析或系统设计；只有标记为 `CPU-toy`/`mechanism-micro` 的方向才适合短周期动手复现。

| # | 方向 | 论文 | 原始来源 | 建议范围 | 可运行 pack |
|---:|---|---|---|---|---|
| 1 | 视觉 | AlexNet | [NIPS 2012](https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) | CPU-toy/analysis | — |
| 2 | 训练 | Dropout | [JMLR](https://jmlr.org/papers/v15/srivastava14a.html) | CPU-toy | — |
| 3 | 训练 | Batch Normalization | [arXiv](https://arxiv.org/abs/1502.03167) | CPU-toy | — |
| 4 | 优化 | Adam | [arXiv](https://arxiv.org/abs/1412.6980) | CPU-toy | — |
| 5 | 视觉 | Deep Residual Learning for Image Recognition | [arXiv](https://arxiv.org/abs/1512.03385) | mechanism-micro | `resnet-micro` |
| 6 | 视觉 | U-Net | [arXiv](https://arxiv.org/abs/1505.04597) | CPU-toy/analysis | — |
| 7 | 生成 | Generative Adversarial Nets | [arXiv](https://arxiv.org/abs/1406.2661) | CPU-toy/analysis | — |
| 8 | 生成 | Auto-Encoding Variational Bayes | [arXiv](https://arxiv.org/abs/1312.6114) | CPU-toy/analysis | — |
| 9 | 训练 | Distilling the Knowledge in a Neural Network | [arXiv](https://arxiv.org/abs/1503.02531) | CPU-toy | — |
| 10 | NLP | Sequence to Sequence Learning with Neural Networks | [arXiv](https://arxiv.org/abs/1409.3215) | CPU-toy/analysis | — |
| 11 | NLP | Attention Is All You Need | [arXiv](https://arxiv.org/abs/1706.03762) | mechanism-micro | `transformer-micro` |
| 12 | NLP | BERT: Pre-training of Deep Bidirectional Transformers | [arXiv](https://arxiv.org/abs/1810.04805) | analysis/optional-GPU | — |
| 13 | NLP | Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer | [arXiv](https://arxiv.org/abs/1910.10683) | analysis/optional-GPU | — |
| 14 | NLP | Language Models are Few-Shot Learners | [arXiv](https://arxiv.org/abs/2005.14165) | analysis | — |
| 15 | 视觉 | An Image is Worth 16x16 Words | [arXiv](https://arxiv.org/abs/2010.11929) | CPU-toy/optional-GPU | — |
| 16 | 多模态 | Learning Transferable Visual Models From Natural Language Supervision | [arXiv](https://arxiv.org/abs/2103.00020) | analysis/optional-GPU | — |
| 17 | 生成 | Denoising Diffusion Probabilistic Models | [arXiv](https://arxiv.org/abs/2006.11239) | CPU-toy/optional-GPU | — |
| 18 | 微调 | LoRA: Low-Rank Adaptation of Large Language Models | [arXiv](https://arxiv.org/abs/2106.09685) | CPU-toy/optional-GPU | — |
| 19 | 微调 | QLoRA: Efficient Finetuning of Quantized LLMs | [arXiv](https://arxiv.org/abs/2305.14314) | analysis/optional-GPU | — |
| 20 | 检索 | Dense Passage Retrieval for Open-Domain Question Answering | [arXiv](https://arxiv.org/abs/2004.04906) | CPU-toy/analysis | — |
| 21 | 检索 | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | [arXiv](https://arxiv.org/abs/2005.11401) | CPU-toy/optional-GPU | — |
| 22 | Agent | ReAct: Synergizing Reasoning and Acting in Language Models | [arXiv](https://arxiv.org/abs/2210.03629) | evaluation-micro | `react-eval` |
| 23 | Agent | Toolformer: Language Models Can Teach Themselves to Use Tools | [arXiv](https://arxiv.org/abs/2302.04761) | analysis/optional-GPU | — |
| 24 | Agent | Reflexion: Language Agents with Verbal Reinforcement Learning | [arXiv](https://arxiv.org/abs/2303.11366) | CPU-toy/analysis | — |
| 25 | 强化学习 | Playing Atari with Deep Reinforcement Learning | [arXiv](https://arxiv.org/abs/1312.5602) | CPU-toy/optional-GPU | — |
| 26 | 强化学习 | Proximal Policy Optimization Algorithms | [arXiv](https://arxiv.org/abs/1707.06347) | CPU-toy/optional-GPU | — |
| 27 | 强化学习 | Mastering the Game of Go with Deep Neural Networks and Tree Search | [Nature](https://www.nature.com/articles/nature16961) | analysis/optional-GPU | — |
| 28 | 对齐 | Training language models to follow instructions with human feedback | [arXiv](https://arxiv.org/abs/2203.02155) | analysis | — |
| 29 | 评测 | Holistic Evaluation of Language Models | [arXiv](https://arxiv.org/abs/2211.09110) | CPU-toy/analysis | — |
| 30 | 评测 | TruthfulQA: Measuring How Models Mimic Human Falsehoods | [arXiv](https://arxiv.org/abs/2109.07958) | CPU-toy/analysis | — |

## 统一阅读卡

每篇卡片至少回答：问题、方法、假设、数据/环境、指标、最小可验证机制、失败模式、资源限制、许可证/引用和“当前实验不能支持什么”。一周只做问题与机制切片；一月做 baseline 加一次受控变量；两月增加消融和稳定性；半年再考虑完整工程或研究报告。

## 首批可运行包

本仓的 A03 `paper-packs/` 已提供 `resnet-micro`、`transformer-micro` 和 `react-eval` 三个 CPU pack。它们分别对应第 5、11、22 篇，只用于机制/评价级复现，不代表原论文的完整结果。正式作业必须在私有 assignment metadata 中写入选定 pack ID。
