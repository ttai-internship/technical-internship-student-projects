# B03：小型 Web 功能切片

## 定位

- 等级：初级；推荐一周起步。
- 主线：需求切片、模块边界、HTTP 请求流程和 Git/CI。
- 完全零基础学生先完成 B00；本项目不要求前端框架、数据库或部署。

## Starter 结构

```text
src/web_slice/app.py
src/web_slice/server.py
tests/test_public.py
design.md
```

这是一个 Python 标准库 HTTP Demo。学生先调用 `filter_tickets` 和
`encode_tickets`，最后再运行服务端。

## 三选一 Core 切片

- 增加 `status` 筛选；
- 增加非法参数的明确错误响应；
- 增加空结果的明确响应字段。

必须补充至少两个边界测试和 `design.md` 中的请求流程图。

## 验收

1. 正常、空输入和非法输入均有明确行为；
2. `count` 与 `items` 一致，原有功能不回归；
3. 测试、CI 和 Notebook 通过；
4. 学生能说明请求从入口到业务函数和 JSON 响应经过哪些模块；
5. PR 描述包含背景、修改范围和验证结果。

一周完成一个切片；一月完成两个切片并做一次小重构；两月以上再考虑分页、排序或服务化。
