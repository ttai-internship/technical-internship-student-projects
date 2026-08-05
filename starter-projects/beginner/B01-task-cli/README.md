# B01 Starter：命令行任务清单

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
