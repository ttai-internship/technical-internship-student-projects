# A03 Starter：论文复现与算法改进

当前仓库提供三个 CPU 可运行的微型 pack。正式发放时，导师必须通过私有
assignment 生成器选择一个 pack，并把选中的 ID 写入 `.internship/assignment.json`；
这里的 `ready_for_assignment` 只表示 pack 的工程边界已经锁定，不表示完成了
原论文的完整复现。

## 运行

```powershell
$env:PYTHONPATH = "src"
python baseline/train.py
python paper-packs/transformer-micro/run.py
python -m paper_reproduction.run --variant baseline
python -m unittest discover -s tests -v
```

学生需要填写 `references/paper-notes.md`，运行导师指定的 `paper_pack/run.py`
和 baseline，控制一个变量，保存结果和失败记录，并在报告中区分复现证据与
个人推断。
