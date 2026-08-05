# M01 Starter：表格数据机器学习实验

## 环境

```powershell
python -m pip install -r requirements.txt
$env:PYTHONPATH = "src"
python -m tabular_ml.run --model baseline
python -m unittest discover -s tests -v
```

## 学生 Core

基线使用多数类预测器。学生需要：

1. 复现 baseline；
2. 在 `model.py` 中增加一个受控的模型或特征方案；
3. 使用同一个数据划分和指标比较结果；
4. 提交至少五个错误样本或错误类型的分析。

数据很小，目的是练习实验规范，不是追求高分数。
