# A03 Starter：论文复现与算法改进

这是一个可替换的确定性实验骨架。项目开始时需要补充具体论文、代码来源、数据和 baseline 范围。

## 运行

```powershell
$env:PYTHONPATH = "src"
python -m paper_reproduction.run --variant baseline
python -m unittest discover -s tests -v
```

## 学生 Core

- 阅读项目指定论文并填写 `references/paper-notes.md`；
- 运行 baseline；
- 只改变一个主要变量；
- 保存配置、结果和失败记录；
- 解释结果与论文预期的差异。
