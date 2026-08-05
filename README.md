# 技术实习学生项目仓

这是一个公开的学生项目仓。每位实习生在自己的 Fork 中，从初级、中级、高级对应的 3 个项目中选择 1 个，完成代码、测试/实验、Notebook、Git 提交和 CI 验证。

仓库只包含学生材料：starter、任务卡、学生版 Notebook、公共测试和提交模板。不要在这里提交 API Key、个人隐私数据或真实生产数据。

## 快速开始

先 Fork 本仓库，再克隆自己的 Fork：

```powershell
git clone https://github.com/Densityyang/technical-internship-student-projects.git
cd technical-internship-student-projects
git remote rename origin upstream
git remote add origin https://github.com/<your-account>/technical-internship-student-projects.git
```

选择项目并创建自己的开发分支：

```powershell
git checkout -b feature/B01-task-cli
.\scripts\select_project.ps1 -Project B01 -StudentId S001 -Duration one-week
# macOS/Linux 或不使用 PowerShell 时：
uv run --locked python scripts/select_project.py --project B01 --student-id S001 --duration one-week
```

配置环境。Windows 推荐使用 `uv`；也可以按项目 README 使用 Conda：

```powershell
.\scripts\bootstrap.ps1 -Project B01
uv run --locked python scripts\validate_projects.py
uv run --locked python scripts\run_public_tests.py --project B01
uv run --locked python scripts\run_notebooks.py
```

## 项目选择

| 等级 | 项目 | 适合方向 |
|---|---|---|
| 初级 | [B01 Task CLI](tasks/beginner/B01-task-cli.md) | Python、数据结构、分层、Git/CI |
| 初级 | [B02 Data Report](tasks/beginner/B02-data-report.md) | CSV、数据质量、可复现报告 |
| 初级 | [B03 Web Slice](tasks/beginner/B03-web-slice.md) | HTTP、参数校验、JSON API |
| 中级 | [M01 Tabular ML](tasks/intermediate/M01-tabular-ml.md) | 机器学习实验和误差分析 |
| 中级 | [M02 Small DL](tasks/intermediate/M02-small-dl.md) | 深度学习训练闭环 |
| 中级 | [M03 RL Control](tasks/intermediate/M03-rl-control.md) | Q-learning 和控制实验 |
| 高级 | [A01 Tool Agent](tasks/advanced/A01-tool-agent.md) | 工具协议、Agent 和失败处理 |
| 高级 | [A02 Agent Evaluation](tasks/advanced/A02-agent-evaluation.md) | 固定评估和失败分类 |
| 高级 | [A03 Paper Reproduction](tasks/advanced/A03-paper-reproduction.md) | 受控复现和算法实验 |

一周只要求完成所选项目的 Core；一月、两月和半年通过增加实验深度、模块责任和报告要求扩展，不改变等级定义。

## 开发、提交和推送

正式代码必须回写到所选项目的 `starter-projects/<level>/<project>/src/`，测试回写到该项目的 `tests/`，Notebook 只用于引导和证据记录。

```powershell
git status
git add PROJECT_SELECTION.json starter-projects notebooks/student docs
git commit -m "feat: complete <project-id> Core"
git push -u origin feature/<project-id>-<slice>
```

每次提交后检查 GitHub Actions。提交说明、日报和报告模板位于 `templates/`；统一评价口径见 [assessment](docs/assessment.md)。

## 常用目录

- `config/projects.json`：学生项目清单；
- `starter-projects/`：九个项目的学生 starter；
- `notebooks/student/`：九个学生引导 Notebook；
- `tasks/`：项目目标、Core、Stretch 和周期要求；
- `curriculum/`：课程、Bilibili 和行业内容入口；
- `scripts/`：环境、项目选择、测试和 Notebook 执行；
- `.github/workflows/`：学生仓 CI。
