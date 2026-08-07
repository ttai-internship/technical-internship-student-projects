# Starter Projects

这里存放可以复制给学生的教学项目。它们不是生产代码，重点是：

- 有一个能运行的 baseline；
- Core 缺口足够明确；
- 学生能通过公开测试和运行日志自查；
- 学生可以使用统一验收清单自查，而不必重新设计项目。

如果学生还不能独立运行和修改 Python 文件，应先完成仓库根目录的 [B00 基础起步门](../foundation/README.md)，再进入下面的九个主项目。

## 目录

```text
starter-projects/
├── beginner/
│   ├── B01-task-cli/
│   ├── B02-data-report/
│   └── B03-web-slice/
├── intermediate/
│   ├── M01-tabular-ml/
│   ├── M02-small-dl/
│   └── M03-rl-control/
└── advanced/
    ├── A01-tool-agent/
    ├── A02-agent-evaluation/
    └── A03-paper-reproduction/
```

初级项目先提供完整实现路径和公开测试。中高级项目先提供可复现实验骨架，具体数据、模型和论文在项目开始时由学生与指导者共同确认。

## 工程化学习路径

每个项目现在配有一个顶层教学 Notebook，位置见 [Notebook 清单](../notebooks/README.md)。推荐按以下顺序工作：

1. 先读本项目 README、任务卡和对应 Notebook 的 Goal/Design；
2. 运行 starter baseline，保存命令、输出和限制；
3. 在 Notebook 中完成关键概念推导或局部实验；
4. 将可复用逻辑回写到本项目 `src/`，不要只留在 Notebook；
5. 把断言补进 `tests/`，再运行 CI；
6. 通过 Git commit、运行报告和现场答辩完成验收。

Notebook 只承担引导、实验和解释职责。最终工程交付仍然是 `src/`、`tests/`、README/设计文档、Git history 和可复现运行证据的组合。
