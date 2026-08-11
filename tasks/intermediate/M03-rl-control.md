# M03：强化学习控制实验

## 定位

- 等级：中级；一周完成 GridWorld Core。
- 主线：状态、动作、奖励、终止、Q-learning、随机种子和多回合评估。
- 不要求一开始使用 Gymnasium；CartPole 只能在掌握闭环后作为 Stretch。

## Starter 结构

```text
src/rl_control/env.py
src/rl_control/agent.py
src/rl_control/train.py
src/rl_control/evaluate.py
tests/test_public.py
```

## Core

- 解释环境、状态、动作、奖励和终止条件；
- 补全 tabular `q_learning`；
- 与 RandomAgent 进行多回合对比；
- 固定随机种子并记录平均回报和失败轨迹；
- 分析一个失败原因和一个可验证的改进假设。

## 验收

1. learned policy 在固定评估协议下优于随机 baseline；
2. 每个 episode 的回报都被记录；
3. 训练参数、随机种子和环境边界明确；
4. 结论基于多次运行，而不是一次幸运结果；
5. Notebook、测试、报告和答辩能解释 Q 值更新。

一月比较探索策略；两月加入稳定性分析；半年再考虑标准环境或研究问题。
