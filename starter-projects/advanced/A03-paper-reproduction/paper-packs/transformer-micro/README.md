# `transformer-micro`

原始论文：[Attention Is All You Need](https://arxiv.org/abs/1706.03762)。本 pack 只复现缩放点积注意力 `softmax(QK^T / sqrt(d))V`，不训练机器翻译 Transformer，也不声称达到论文 BLEU 结果。

运行：

```powershell
python run.py
python -m unittest discover -s . -p "test_pack.py" -v
```

Core 证据：解释缩放项、注意力权重行和为 1 的原因、一个受控输入变化，以及当前实验不能支持的关于语言质量的结论。
