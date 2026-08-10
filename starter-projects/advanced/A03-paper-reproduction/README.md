# A03 Starter：论文复现与算法改进

当前仓库只提供受控实验骨架。正式发放前，导师必须在
`references/paper-pack.json` 中锁定一篇论文和可运行范围；当
`ready_for_assignment` 为 `false` 时，这个项目只能用于示范，不能作为
正式作业。

## 运行

```powershell
$env:PYTHONPATH = "src"
python baseline/train.py
python -m paper_reproduction.run --variant baseline
python -m unittest discover -s tests -v
```

学生需要填写 `references/paper-notes.md`，运行 baseline，控制一个变量，
保存结果和失败记录，并在报告中区分复现证据与个人推断。
