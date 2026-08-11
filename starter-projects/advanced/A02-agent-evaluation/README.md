# A02 Starter：Agent 评测与失败分析

这是一个离线、固定 trace 的评测 starter，不需要 API key。先运行：

```powershell
$env:PYTHONPATH = "src"
python -m agent_eval.run
python -m unittest discover -s tests -v
```

学生需要在同一份 `eval/cases.json` 上保留 baseline，补充指标或失败分类，
输出逐案例结果、通过率和失败统计，并解释当前实验不能证明什么。
