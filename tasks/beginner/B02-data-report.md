# B02：数据清洗与报告

## 定位

- 等级：初级；推荐一周起步。
- 主线：文件处理、数据质量、可重复运行和结果解释。
- 如果还不能独立运行和修改 Python 文件，先完成 B00；不要求先学 pandas。

## Starter 结构

```text
data/raw/sample.csv
data/expected/summary.json
src/data_report/{reader,validator,cleaner,report,main}.py
tests/test_public.py
```

输入是脱敏教学数据。`expected/summary.json` 是一份可观察的目标契约，不代表学生可以跳过代码实现。

## Core

- 检查缺失、重复、非法金额和未知状态；
- 选择并记录“删除”或“修复”规则，不能修改原始输入；
- 输出 JSON 和 Markdown 报告；
- 为至少三条数据质量规则补充测试；
- 说明清洗前后行数、金额汇总和异常数量。

## 验收

1. 同一输入重复运行结果一致；
2. 清洗后的记录满足字段与金额约束；
3. 异常不会被静默吞掉；
4. 报告包含行数、异常数、主要统计量和规则说明；
5. CI、Notebook、提交记录和答辩证据齐全。

一周完成固定规则；一月增加可配置规则和一张图表；两月以上可以做数据服务接口，但不把模型作为 Core。
