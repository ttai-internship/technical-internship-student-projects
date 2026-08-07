# 学生版教学 Notebook

Notebook 用于 B00 基础门和项目的问题拆解、实验记录和证据整理；正式逻辑必须回写到项目 `src/`，断言和边界行为必须回写到项目 `tests/`。

全部 Notebook 可在仓库根目录执行：

```powershell
uv run --locked python scripts\run_notebooks.py
```

源 Notebook 不会被覆盖，带输出副本写入 `artifacts/notebooks/`。

## 清单

- [B00 Python 基础起步](student/foundation/B00-python-foundation.ipynb)
- [B01](student/beginner/B01-task-cli.ipynb) · [B02](student/beginner/B02-data-report.ipynb) · [B03](student/beginner/B03-web-slice.ipynb)
- [M01](student/intermediate/M01-tabular-ml.ipynb) · [M02](student/intermediate/M02-small-dl.ipynb) · [M03](student/intermediate/M03-rl-control.ipynb)
- [A01](student/advanced/A01-tool-agent.ipynb) · [A02](student/advanced/A02-agent-evaluation.ipynb) · [A03](student/advanced/A03-paper-reproduction.ipynb)
