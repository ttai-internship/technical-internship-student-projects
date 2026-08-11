# A03 论文微型复现包

本目录提供三个可选的 cohort pack。每个 pack 都能在 CPU 上独立运行，但它们复现的是论文中的一个机制或评价切片，不声称复现原论文的完整数据、模型规模或 SOTA 结果。

| Pack | 论文机制 | Core 运行方式 |
|---|---|---|
| `resnet-micro` | 残差连接与表示变化 | `python run.py` |
| `transformer-micro` | 缩放点积注意力 | `python run.py` |
| `react-eval` | 思考-行动固定轨迹与工具成功率 | `python run.py` |

导师在生成 assignment pack 时指定一个 pack。学生只对指定 pack 提交实验和解释；其他 pack 仅用于自学对照。每个 pack 的 `test_pack.py` 是公开的机制级回归检查，不替代私有 Core 验收。
