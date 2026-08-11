# `react-eval`

原始论文：[ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)。本 pack 使用固定的离线轨迹，复现“工具动作序列可被评价”的切片；不调用在线 LLM，不把固定 trace 的结果当作模型能力结论。

运行：

```powershell
python run.py
python -m unittest discover -s . -p "test_pack.py" -v
```

Core 证据：解释工具动作、终止回答、失败分类和 pass rate，新增一个固定案例，并说明为什么离线 trace 不能代表真实模型泛化。
