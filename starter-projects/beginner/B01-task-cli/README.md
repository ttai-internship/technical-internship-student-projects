# B01 Starter：命令行任务清单

如果你还不能独立运行和修改一个 Python 文件，请先完成仓库根目录的 [B00 基础起步门](../../../foundation/README.md)。B01 的第一步不是读完整个项目，而是只打开 `service.py`，完成一个 `complete` 用例。

## 运行

在项目目录执行：

```powershell
$env:PYTHONPATH = "src"
python -m task_cli.cli add --title "first task"
python -m task_cli.cli list
python -m unittest discover -s tests -v
```

默认数据文件为当前目录的 `tasks.json`，可以通过 `TASK_CLI_DATA` 指定其他位置。

## 学生 Core

基线已经支持 `add` 和 `list`。学生需要补全：

- `TaskService.complete`；
- `TaskService.delete`；
- CLI 的 `done` 和 `delete` 子命令；
- 至少两个异常输入测试。

公开测试只覆盖基线能力。最终验收按本项目任务卡中的 Core 用例执行，并检查提交记录和 CI。

建议顺序：先写一个最小函数行为 → 跑一个测试 → 再接上存储 → 最后接 CLI。每次只改变一个层，不要从一开始同时修改四个文件。
