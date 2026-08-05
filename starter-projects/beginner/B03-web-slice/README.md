# B03 Starter：小型 Web 功能切片

这是一个只使用 Python 标准库的最小 HTTP Demo，目的是让学生把注意力放在需求切片、请求流程和 Git/CI，而不是依赖安装。

## 运行

```powershell
$env:PYTHONPATH = "src"
python -m web_slice.server
```

然后访问：`http://127.0.0.1:8000/api/tickets`

运行测试：

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
```

## 学生 Core

从以下一个切片中选择一个：

- 增加 `status` 查询筛选；
- 增加非法参数的错误响应；
- 增加空结果的明确响应字段。

同时提交 `design.md`，画出请求从 HTTP 入口到数据结果的流程。
