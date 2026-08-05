# M03 Starter：强化学习控制实验

这是一个不依赖 Gymnasium 的小型 GridWorld，目的是把时间放在状态、动作、奖励和评估上。确认学生掌握闭环后，可以替换成 CartPole 等标准环境。

## 运行

```powershell
$env:PYTHONPATH = "src"
python -m rl_control.train --agent random --episodes 5
python -m unittest discover -s tests -v
```

## 学生 Core

- 解释环境、状态、动作、奖励和终止条件；
- 补全 `q_learning`；
- 与 random baseline 对比多回合结果；
- 固定随机种子并记录训练曲线；
- 分析一个失败原因。
