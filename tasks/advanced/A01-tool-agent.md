# A01：工具调用 Agent

## 定位

- 等级：高级
- 推荐周期：一周做局部切片；一月或两月完成原型
- 适合：能独立使用 Python，理解 API、结构化输出和基本 LLM 工作流的学生
- 主线：工具定义 + Agent 流程 + 异常处理 + 固定评估

## 背景

在受限、脱敏的场景中构建一个可测试的工具调用 Agent，例如查询数据、检索文档或生成结构化报告。

## Starter code

```text
src/
└── tool_agent/
    ├── agent.py
    ├── tools.py
    ├── fake_model.py
    └── run.py
eval/
├── cases.json
└── evaluate.py
tests/
└── test_public.py
```

项目提供 fake model、本地只读工具、10 个固定案例和费用/权限边界；学生不需要 API Key，也不应在 Core 阶段接入真实模型。

## 学生完成的核心代码

- 增加一个工具或一个路由分支；
- 完成参数校验；
- 处理工具调用失败和超时；
- 增加结构化日志；
- 运行固定案例并分类失败结果。

## Core 验收

| 用例 | 最小要求 | 证据 |
|---|---|---|
| 工具协议 | 工具名、描述、参数和返回值明确 | schema 或 README |
| 正常调用 | 固定案例能路由到正确工具 | 逐案例结果 |
| 非法输入 | 未知工具、错误参数不执行 handler | 测试和日志 |
| 工具失败 | 异常被记录，并返回明确失败/降级结果 | 失败案例 |
| 固定评估 | 至少 10 个案例，含成功、失败和降级 | JSON/Markdown 报告 |
| 可复现性 | fake model 测试不依赖网络 | 命令和 CI |

建议的最小运行入口：

```powershell
$env:PYTHONPATH = "src"
python -m tool_agent.run
python eval\evaluate.py
python -m unittest discover -s tests -v
```

最终验收会检查工具注册表、失败边界和固定案例文件；真实模型只能作为 Stretch，不作为 Core 通过条件。

## 必交材料

- Agent 代码；
- 工具 schema；
- 测试集和评估结果；
- 调用日志；
- 失败类型分析；
- 成本、延迟或调用次数记录。

## Stretch

- 增加重试和超时策略；
- 增加人工确认节点；
- 增加回归测试；
- 比较两种 Agent 工作流。

## 周期扩展

- 一周：增加一个工具并通过固定测试；
- 一月：完成一个小型 Agent 工作流；
- 两月：加入评估、日志、异常处理和成本分析；
- 半年：研究记忆、规划、评估或成本优化中的一个问题。
