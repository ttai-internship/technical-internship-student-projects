# `resnet-micro`

原始论文：[Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)。本 pack 只复现“残差函数加回输入”的机制：比较 plain block `F(x)` 与 residual block `x + F(x)` 的输出形状和变化量，不训练 ImageNet/CIFAR-10 的完整网络。

运行：

```powershell
python run.py
python -m unittest discover -s . -p "test_pack.py" -v
```

Core 证据：解释输入/输出、固定随机种子、残差连接的作用、一个受控变量和一个不被当前实验支持的强结论。
