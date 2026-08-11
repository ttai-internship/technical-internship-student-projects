# 环境入口

本仓库把 Python 3.12 作为唯一支持的主版本，并提供两条等价的本地入口。两条入口都必须能够运行项目契约、公开测试和学生 Notebook；不要在同一个工作副本里混用两个虚拟环境。

## 入口 A：uv（CI 的标准路径）

```powershell
uv python install 3.12
uv sync --locked --all-groups --python 3.12
uv run --locked python scripts\validate_projects.py
uv run --locked python scripts\run_public_tests.py
```

`pyproject.toml`、`.python-version` 和 `uv.lock` 共同定义版本边界。提交依赖变化时必须同步更新锁文件，并在提交说明中说明原因。

## 入口 B：Conda/Miniforge

```powershell
conda env update --name technical-internship --file environment.yml --prune
conda run --name technical-internship python scripts\validate_projects.py
conda run --name technical-internship python scripts\run_public_tests.py
```

也可以运行仓库脚本：

```powershell
.\scripts\bootstrap-conda.ps1
```

`environment.yml` 提供与 uv 项目组相同的基础、Notebook、机器学习和深度学习范围。Conda 负责环境，项目代码和依赖版本仍以仓库中的配置为准；不要把 `.conda` 环境目录提交到 Git。

## 学生 assignment pack

独立学生包不要求安装导师仓的隐藏依赖。按包内 `README.md` 或 `requirements.txt` 安装项目依赖，并使用包内生成的 CI。学生包不能通过复制导师仓的 `uv.lock` 来获得隐藏测试或评分材料。
