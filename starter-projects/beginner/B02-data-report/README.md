# B02 Starter：数据清洗与报告

## 运行

```powershell
$env:PYTHONPATH = "src"
python -m data_report.main --input data/raw/sample.csv --output artifacts/report.json
python -m unittest discover -s tests -v
```

## 学生 Core

基线已经可以读取 CSV 并生成基础记录数和金额汇总。学生需要补全：

- `validator.py` 的数据质量规则；
- `cleaner.py` 的重复、缺失和非法金额处理；
- Markdown 报告输出；
- 至少三条数据质量规则的测试。

输入数据是教学用脱敏数据，不得替换成生产数据。
