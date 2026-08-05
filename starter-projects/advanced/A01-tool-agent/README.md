# A01 Starter：工具调用 Agent

这个 starter 使用 fake model 和本地工具，不需要 API Key。学生先完成工具协议、参数校验、失败处理和固定案例评估；真实模型接入属于 Stretch。

## 运行

```powershell
$env:PYTHONPATH = "src"
python -m tool_agent.run
python eval\evaluate.py
python -m unittest discover -s tests -v
```

`eval/cases.json` 提供 10 个固定、可重复的案例。学生可以增加案例，但 Core 报告必须保留原有案例的逐条结果。

## 学生 Core

- 增加一个本地工具；
- 在 `agent.py` 中补充参数校验或错误处理；
- 用至少 10 个固定案例评估；
- 记录成功、失败和降级结果。
