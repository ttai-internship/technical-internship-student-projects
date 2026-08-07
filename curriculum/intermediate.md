# 中级路线学习材料

> 状态：v0.1 草案。中级学生在 M01、M02、M03 中选择一个主项目，不要求三类机器学习内容全部完成。

## 学习重点

1. 线性代数、微积分和概率的基本直觉；
2. 数据划分、指标、baseline、误差分析和可复现实验；
3. 机器学习、深度学习或强化学习中的一个方向；
4. 对结果、随机种子、限制条件和失败案例进行诚实表达。

## 推荐材料映射

| 学习目标 | 优先材料 | 对应实践 |
|---|---|---|
| 数据划分、评估和 Pipeline | [scikit-learn Getting Started](https://scikit-learn.org/stable/getting_started.html)；3Blue1Brown 作为数学直觉补充 | M01 表格数据机器学习实验 |
| Tensor、训练和保存 | [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)；楚国刮大风作为中文推导补充 | M02 小型深度学习模型 |
| 环境、状态、动作和奖励 | [Gymnasium Basic Usage](https://gymnasium.farama.org/introduction/basic_usage/)；京口先生作为论文表达补充 | M03 强化学习控制实验 |

## 推荐的学习记录

至少选择一个概念，完成一次“课程概念到新数据/新环境”的迁移说明。记录应包含：概念、假设、实现或实验、指标、失败情况和下一步。

## 级别边界

- M01 更重视数据、评估和实验纪律；
- M02 更重视模型结构、训练过程和误差分析；
- M03 更重视状态、动作、奖励、策略和稳定性；
- 官方材料建立技术主线，中文课程和访谈用于降低理解门槛、补充推导和行业语境，不作为唯一事实来源；
- 课程具体章节和数据集版本后续锁定。
