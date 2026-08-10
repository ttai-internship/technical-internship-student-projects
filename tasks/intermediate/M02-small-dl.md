# M02：小型深度学习模型

## 定位

- 等级：中级；一周可完成 Core，一月起适合完整实验。
- 主线：数据、模型、训练、评估、checkpoint 和过拟合诊断。
- Core 使用合成二维数据，CPU 可完成；MNIST、GPU 和大型数据集只能作为 Stretch。

## Starter 结构

```text
src/small_dl/data.py
src/small_dl/model.py
src/small_dl/train.py
src/small_dl/evaluate.py
tests/test_public.py
requirements.txt
```

## Core

- 运行并记录 baseline；
- 完成小批量过拟合检查；
- 在 `model.py` 中修改一个结构或训练策略；
- 让 `train(..., return_model=True)` 返回模型；
- 使用 `evaluate` 和 `save_checkpoint` 验证、保存和重新加载结果；
- 记录训练曲线、对比结果和一次失败或不稳定现象。

## 验收

1. 固定种子后结果可重复；
2. 训练与评估模式边界清楚，评估不更新权重；
3. checkpoint 可写出且可解释；
4. 至少有一组改动前后对比；
5. 报告解释过拟合、欠拟合或随机性，而不是只展示最高准确率。

一月比较两个结构或训练策略；两月增加专项改进；半年形成完整可复现实验。
