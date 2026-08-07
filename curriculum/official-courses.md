# 官方课程与文档主线

这是一份给实习生直接阅读和选择的课程推荐页。每个人只需要根据自己的基础、周期和项目选择一条主线，不需要把所有课程全部看完。

Bilibili 仍然是中文观看的主要媒介，但 Bilibili 搜索结果只是观看入口。正式学习时，请同时保留下面的官方来源；如果观看的是翻译或搬运视频，要检查简介是否注明原始课程、作者和译制来源。

## 先看结论

| 你的情况 | 先选什么 | 然后做什么 |
|---|---|---|
| 完全没有编程基础 | [Helsinki Python MOOC 2026](https://programming-26.mooc.fi/) 或 [CS50P](https://cs50.harvard.edu/python/) 二选一 | 完成 [B00 零基础起步门](../foundation/README.md)，再从 B01/B02/B03 三选一 |
| 会写简单 Python，但不会规范开发 | [Python 官方教程](https://docs.python.org/3/tutorial/) 按任务查阅 + [Introduction to GitHub](https://github.com/skills/introduction-to-github) | 选择一个初级项目，补齐测试、commit、push 和 CI |
| 已经有 Python 和机器学习基础 | 按项目选择 scikit-learn、PyTorch 或 Gymnasium | 从 M01/M02/M03 三选一，围绕一次可复现实验完成闭环 |
| 能独立读技术文档或论文 | 按项目选择 Hugging Face Agents Course 或 LLM Course | 从 A01/A02/A03 三选一，提交工程评估或受控复现 |

## 零基础与共同工具线：B00

### Python 主线（二选一）

| 课程 | 适合谁 | 建议范围 | Bilibili 入口 |
|---|---|---|---|
| [Python Programming MOOC 2026](https://programming-26.mooc.fi/) | 希望从变量、输入、条件和循环开始逐步练习的人 | Part 1--3 中与诊断失败项对应的小节 | [搜索 Python MOOC](https://search.bilibili.com/all?keyword=Python%20MOOC) |
| [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/) | 需要一门结构完整、节奏较慢的 Python 入门课的人 | 只学习与诊断失败项对应的周次，不与 MOOC 重复完成 | [搜索 CS50P Python](https://search.bilibili.com/all?keyword=CS50P%20Python) |

### 必要工具练习

| 工具材料 | 你要学会什么 | 完成证据 |
|---|---|---|
| [Introduction to GitHub](https://github.com/skills/introduction-to-github) | 分支、commit、Pull Request 和最小协作闭环 | 一个可追溯的分支和至少一次有意义的 commit |
| [Jupyter 官方入门](https://jupyter.org/try-jupyter/notebooks/?path=notebooks%2FIntro.ipynb) | 单元格、运行顺序和可复现实验记录 | 顺序运行一个官方 Notebook 和一个本仓库学生 Notebook |

## 初级：B01 / B02 / B03

初级不要求算法题、机器学习或 AI。官方材料的作用是帮助你把代码写清楚、测得出来、提交得可追溯。

| 项目 | 官方主线 | 建议学到哪里 | 适合解决的问题 |
|---|---|---|---|
| B01 Task CLI | [Python 官方教程](https://docs.python.org/3/tutorial/) + [GitHub Skills](https://github.com/skills/introduction-to-github) | 模块、函数、异常、文件和基础测试；GitHub Skills 完成核心练习 | 命令行输入、数据结构、分层和 Git/CI |
| B02 Data Report | [Python 官方教程](https://docs.python.org/3/tutorial/) + [Jupyter 官方入门](https://jupyter.org/try-jupyter/notebooks/?path=notebooks%2FIntro.ipynb) | 文件读写、列表/字典、函数和可复现 Notebook | CSV、数据质量、汇总和报告 |
| B03 Web Slice | [Python 官方教程](https://docs.python.org/3/tutorial/) + [GitHub Skills](https://github.com/skills/introduction-to-github) | 函数、异常、字典、输入校验和测试 | 请求参数、JSON 响应和错误边界 |

Python 官方教程是查阅和巩固入口，不是完全零基础学生的第一门课；零基础学生应先完成 B00。

## 中级：M01 / M02 / M03

中级只选择一个方向。每个项目都要求 baseline、指标、误差或失败分析和可复现实验记录。

| 项目 | 官方主线 | 建议学到哪里 | 主要交付 |
|---|---|---|---|
| M01 Tabular ML | [scikit-learn Getting Started](https://scikit-learn.org/stable/getting_started.html) | estimator、train/test split、Pipeline 和 evaluation | 数据划分、指标、baseline、误差分析 |
| M02 Small DL | [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) | Tensors、Dataset/DataLoader、Build Model、Optimization、Save/Load | 训练闭环、模型结构、曲线和失败记录 |
| M03 RL Control | [Gymnasium Basic Usage](https://gymnasium.farama.org/introduction/basic_usage/) | reset、step、observation、action、reward 和 episode 结构 | 环境契约、Q-learning、策略和稳定性分析 |

## 高级：A01 / A02 / A03

高级路线要求学生能够阅读原始文档或论文，并把工程选择、失败模式和评价指标说清楚。

| 项目 | 官方主线 | 建议学到哪里 | 主要交付 |
|---|---|---|---|
| A01 Tool Agent | [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction) | Unit 0，以及与工具调用、RAG 直接相关的章节 | 工具协议、调用轨迹、失败处理 |
| A02 Agent Evaluation | [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction) | Agent 结构、工具边界和评估相关章节 | 固定案例、指标、失败分类和回归检查 |
| A03 Paper Reproduction | [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) | Transformer、datasets 或 training 中与论文方法直接相关的章节 | 原始论文、代码/数据版本、baseline 和受控复现 |

## 中文补充材料

中文材料用于降低理解门槛、补充数学直觉和建立行业语境；它们不替代官方文档、论文、代码和实验验收。

| 材料 | 推荐用法 | 入口 |
|---|---|---|
| 3Blue1Brown | 初级可选；中级用于线性代数、微积分和概率直觉；高级按论文需要选用 | [Bilibili 搜索](https://search.bilibili.com/all?keyword=3Blue1Brown) · [官方 About](https://www.3blue1brown.com/about/) |
| 楚国刮大风 | 数学推导、计算机基础原理和 coding 实战；观看前记录原始课程来源 | [Bilibili 搜索](https://search.bilibili.com/all?keyword=%E6%A5%9A%E5%9B%BD%E5%88%AE%E5%A4%A7%E9%A3%8E) |
| 张小珺商业访谈录 | 训练问题意识、技术商业化理解和表达，不作为技术事实来源 | [Bilibili 搜索](https://search.bilibili.com/all?keyword=%E5%BC%A0%E5%B0%8F%E7%8F%BA%E5%95%86%E4%B8%9A%E8%AE%BF%E8%B0%88%E5%BD%95) |
| 硅谷 101 | 了解科技公司和产业背景；中高级可对节目观点做资料交叉核对 | [Bilibili 搜索](https://search.bilibili.com/all?keyword=%E7%A1%85%E8%B0%B7%20101) · [节目介绍](https://sv101.fireside.fm/82) |
| WhynotTV | 高级优先，用于技术对话、研究表达和观点辨析 | [Bilibili 搜索](https://search.bilibili.com/all?keyword=WhynotTV) |
| 京口先生 | 中高级可选，用于论文、研究进展和技术演讲的中文理解 | [Bilibili 搜索](https://search.bilibili.com/all?keyword=%E4%BA%AC%E5%8F%A3%E5%85%88%E7%94%9F) |

## 每次学习要留下什么

不要求提交完整课程笔记。每次只需记录：

1. 实际观看的课程、章节或视频和日期；
2. 一个帮助你做出项目设计决定的概念；
3. 一个材料中没有原样出现的迁移问题和尝试；
4. 运行记录、代码、实验结果或现场可复述的证据。

课程是实践的辅助材料，不替代项目 Core 验收。导师可按一周、一月、两月或半年周期锁定更小的章节范围。

## 给维护者的说明

本页是学生和导师的可读入口；[catalog.json](catalog.json) 只用于脚本、版本管理和维护课程元数据。每期开班前仍需核验官方页面可用性、Bilibili 实际观看入口、章节范围和字幕/转载说明。
