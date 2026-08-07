# B0：Python 基础起步门

B0 是初级路线的共同基础门，不是第四个主项目。它面向第一次接触编程、还不能独立阅读项目代码的学生；已经能运行和修改基础 Python 的学生可以通过第一天诊断后跳过部分内容。

## 目标

完成 B0 后，学生应能够：

- 在 VS Code 或终端运行一个 Python 文件；
- 修改字符串、数字和变量；
- 使用输入、条件、循环和列表完成小程序；
- 编写一个带参数和返回值的函数；
- 用最小测试检查自己的函数；
- 创建分支、提交两次有意义的 commit、push 并查看 CI。

B0 不要求 JSON 持久化、命令行参数解析、HTTP、pandas、机器学习或 AI。

## 五个微任务

| 微任务 | 主题 | 推荐时间 |
|---|---|---:|
| B0-01 | 运行程序并修改输出 | 30 分钟 |
| B0-02 | 变量、输入和简单计算 | 45 分钟 |
| B0-03 | 条件、循环和列表 | 60 分钟 |
| B0-04 | 函数和最小测试 | 60 分钟 |
| B0-05 | Git 分支、commit、push 和 CI | 45 分钟 |

每个微任务都按“先预测、再运行、解释一行、修改一处、增加一个新案例”的顺序完成。学生的代码必须保存在 starter 的 src/ 中，Notebook 只用于引导和记录。

## 一周安排

1. 第一天：完成能力诊断、B0-01 和 GitHub Skills 的基础练习；
2. 第二天：B0-02；
3. 第三天：B0-03；
4. 第四天：B0-04；
5. 第五天：B0-05、小型整合、现场说明和进入 B01/B02/B03 的建议。

## 运行和验收

~~~powershell
uv run --locked python scripts/run_public_tests.py --project B00
uv run --locked python scripts/run_notebooks.py
~~~

导师验收关注三个可观察结果：

1. 学生可以从零运行并修改程序；
2. 学生可以用一个测试证明修改有效；
3. 学生可以解释自己遇到的一个错误和定位过程。

B0 完成后，初级学生仍然从 B01、B02、B03 中选择一个主项目；B0 不改变三选一规则。

## 学习材料

- 主线课程：University of Helsinki [Python Programming MOOC 2026](https://programming-26.mooc.fi/)，第一周只指定 Part 1--3 的必要小节；
- Git：GitHub Skills [Introduction to GitHub](https://github.com/skills/introduction-to-github)；
- Notebook：Jupyter [官方入门](https://jupyter.org/try-jupyter/notebooks/?path=notebooks%2FIntro.ipynb)；
- 中文讲解、数学直觉和行业访谈保留在课程目录中，作为补充材料而不是 B0 的技术门槛。
