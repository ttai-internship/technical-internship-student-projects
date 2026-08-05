# A01 固定评估

`cases.json` 是 Core 的固定案例集。学生可以增加案例，但不能删除或改写已有案例后再报告结果。

在项目根目录执行：

```powershell
$env:PYTHONPATH = "src"
python eval\evaluate.py
```

最终提交至少保留逐案例结果，并把成功、失败、降级和限制分别说明。评估脚本只使用 fake model 和本地工具，不需要 API Key 或网络。
