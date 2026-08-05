# M02 Starter：小型深度学习模型

## 环境

```powershell
python -m pip install -r requirements.txt
$env:PYTHONPATH = "src"
python -m small_dl.train --epochs 3
python -m unittest discover -s tests -v
```

默认使用合成二维数据，不需要下载大型数据集或配置 GPU。之后可以替换为 MNIST、Fashion-MNIST 或项目指定的数据。

## 学生 Core

- 运行 baseline；
- 完成小批量过拟合检查；
- 在 `model.py` 中修改一个结构或训练策略；
- 保存训练曲线和对比结果；
- 解释一次训练失败或不稳定现象。
