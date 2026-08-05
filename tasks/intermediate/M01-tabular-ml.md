# M01：表格数据机器学习实验

## 定位

- 等级：中级
- 推荐周期：一周起步；一月或两月更合适
- 适合：会使用 Python，理解基本统计概念，能够阅读 Notebook 或训练脚本的学生
- 主线：数据划分 + baseline + 模型比较 + 错误分析

## 背景

starter repository 提供固定的脱敏数据集、字段说明、baseline 和评估脚本。学生需要完成一次可复现的分类或回归实验。

## Starter code

```text
data/
├── train.csv
└── test.csv
src/
└── tabular_ml/
    ├── data.py
    ├── model.py
    ├── evaluate.py
    └── run.py
tests/
└── test_public.py
```

项目提供 baseline 结果、固定数据划分和指标说明。当前数据字段固定为 `hours`、`assignments`、`attendance`，标签为 `passed`；包含的测试集上多数类 baseline 的 accuracy 是 `0.50`。

## 学生完成的核心代码

- 完成数据预处理；
- 运行并复现 baseline；
- 选择一个改进模型或特征方案；
- 输出指标对比；
- 分析至少五个错误样本或错误类型。

## Core 验收

1. `python -m tabular_ml.run --model baseline` 可以重新运行并报告 `count=4`；
2. `build_student_model()` 可以接收训练特征和标签，并对测试特征给出预测；
3. 至少有一次受控对比实验，训练/测试文件和指标不被中途更换；
4. 报告同时给出 accuracy、混淆矩阵和错误样本/类型，不用单一指标夸大结果；
5. 明确说明预处理在哪个数据集上拟合，以及是否存在数据泄漏；
6. 运行参数、随机种子、环境版本和失败结果完整记录。

建议的最小运行入口：

```powershell
$env:PYTHONPATH = "src"
python -m tabular_ml.run --model baseline
python -m tabular_ml.run --model student
python -m unittest discover -s tests -v
```

最终验收会检查学生模型接口、固定数据契约和公开测试；不会把一次偶然的高分当作研究结论。

## 必交材料

- 训练和评估代码；
- baseline 与改进结果表；
- 错误分析；
- 实验报告；
- 可重复运行命令。

## Stretch

- 增加交叉验证；
- 比较第二种模型；
- 增加一个简单的数据质量检查；
- 分析不同子群体上的表现差异。

## 周期扩展

- 一周：baseline 加一次对比实验；
- 一月：完整实验报告和两轮改进；
- 两月：增加数据质量、特征分析或模型解释；
- 半年：形成有明确研究问题的实验课题。
