# A02：Agent 评测系统

## 定位

- 等级：高级；一周完成离线评测切片，一月或两月完成完整闭环。
- 主线：固定案例、baseline、指标、失败分类和可重复比较。
- RAG 检索器或在线 LLM 只是长期 Stretch；Core 不需要 API key。

## Starter 结构

```text
src/agent_eval/{cases.py,metrics.py,run.py}
eval/{cases.json,README.md}
tests/test_public.py
```

`eval/cases.json` 是固定的离线 trace 集合。学生不得改写原始案例顺序来制造更高分。

## Core

- 保留 baseline 指标；
- 增加一个指标或更清晰的失败分类；
- 保留逐案例结果、pass rate 和 failure counts；
- 比较改动前后同一案例集；
- 报告检索、生成、理解和其他失败，并说明指标局限。

## 验收

1. 固定案例顺序不变；
2. 每个案例有 `id`、`passed`、`failure_type`；
3. 结果可重复；
4. 不能只展示成功案例；
5. 一周版本不依赖外部服务，一月以上再接入 RAG 或真实模型。
