# B01：命令行任务清单

## 定位

- 等级：初级
- 推荐周期：一周起步；一月可做扩展
- 适合：会写基础 Python，但还不熟悉工程结构和 Git 协作的学生
- 主线：基础数据结构 + 模块拆分 + 测试 + Git/CI

## 背景

starter repository 已经提供一个命令行任务清单的基本框架。学生不需要从零搭建项目，而是补全任务管理、文件保存和输入校验。

## Starter code

```text
src/
└── task_cli/
    ├── model.py     # 任务数据结构
    ├── service.py   # 业务操作接口
    ├── storage.py   # JSON 文件读写接口
    └── cli.py       # 命令行入口
tests/
└── test_public.py
```

项目提供：项目入口、JSON 存储骨架、公开基线测试、运行说明和 CI 配置。

## 学生完成的核心代码

- `service.py`：新增、查询、完成、删除任务；
- `storage.py`：保存和加载 JSON；
- `cli.py`：解析命令行参数；
- `tests/`：补充正常和异常输入测试。

不要求学生实现复杂算法或数据库。

## Core 验收

| 用例 | 操作 | 通过证据 |
|---|---|---|
| 创建并列出 | `add` 后重新运行 `list` | 输出包含唯一 ID 和标题 |
| 完成任务 | `done <id>` 后重新运行 `list` | 目标行显示 `[x]`，其他任务不变 |
| 删除任务 | `delete <id>` 后重新运行 `list` | 目标任务消失，其他任务保留 |
| 重启持久化 | 更换进程后再次 `list` | JSON 中的状态与 CLI 一致 |
| 异常输入 | 空标题、未知 ID、损坏 JSON | 有明确错误，不输出成功提示 |

命令和测试必须能够在项目根目录执行：

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
```

学生还需提交至少一个 `feat`、一个 `test` 和一个 `docs` commit。

## 必交材料

- 代码和测试；
- README 运行说明；
- 一张简单结构图；
- 运行结果或命令日志；
- 一个问题定位记录。

## Stretch

- 按状态筛选；
- 增加截止日期；
- 将 JSON 存储替换为 SQLite；
- 增加一个简单的 GitHub Actions 检查。

## 周期扩展

- 一周：完成 Core 的四个命令和测试；
- 一月：完成 SQLite 或筛选功能，并进行一次重构；
- 两月以上：可以扩展为简单 Web API，但不再属于初级默认任务。

## 同步节点

- 开始：确认项目入口和任务边界；
- 中间：同步一次 commit 和一条失败用例；
- 最终：执行固定命令并进行现场说明。
