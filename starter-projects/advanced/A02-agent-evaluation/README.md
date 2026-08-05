# A02 Starter：RAG/Agent 评估系统

这个 starter 不依赖真实模型。它提供固定问题、期望答案和 baseline 输出，学生需要增加评估方法并分析失败类型。

## 运行

```powershell
$env:PYTHONPATH = "src"
python -m agent_eval.run
python -m unittest discover -s tests -v
```

## 学生 Core

- 增加一个指标；
- 固定问题集和 baseline；
- 记录改动前后结果；
- 至少分类三种失败原因；
- 写出不能由当前实验支持的结论。
