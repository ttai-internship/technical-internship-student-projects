# A03：论文阅读、受控复现与算法改进

## 定位

- 等级：高级；一月起步，两月或半年更适合完整研究。
- 30 篇论文先提供阅读卡；每期只发放已锁定的3个可运行论文包。
- GPT-3、原始 Transformer 大规模结果等只能做分析或缩小机制复现，不能冒充完整复现。

## Assignment readiness

A03 只有在 `references/paper-pack.json` 标记 `ready_for_assignment: true` 且生成作业时选定一个 `PaperPack` 后才能正式发放。论文包必须锁定原文、代码/数据许可、CPU 可运行范围、baseline、指标、随机种子和预期结果。

## Starter 结构

```text
baseline/{train.py,evaluate.py,config.yaml}
experiments/{reproduce.py,ablation.py,results/}
references/{paper-pack.json,paper-notes.md}
src/paper_reproduction/{experiment.py,run.py}
tests/test_public.py
```

## Core

- 填写论文问题、方法、假设和复现边界；
- 只围绕 assignment metadata 中的一个 `paper_pack_id` 工作；
- 运行 baseline；
- 只改变一个主要变量；
- 保存配置、结果和失败记录；
- 将复现结果、改动结果和个人推断分开；
- 说明哪些结论没有被当前实验支持。

## 验收

1. 环境、数据、版本和运行命令完整；
2. baseline 与改动实验可分别复现；
3. 结果表或图包含不确定性和资源限制；
4. 报告区分事实、观察和推断；
5. 答辩能解释指标、随机性和复现失败原因。

一周做局部机制复现；一月完成 baseline 加一次受控改动；两月增加消融和稳定性；半年形成研究报告或可交接原型。首批可选 pack 为 `resnet-micro`、`transformer-micro` 和 `react-eval`，均为 CPU 微型复现。
