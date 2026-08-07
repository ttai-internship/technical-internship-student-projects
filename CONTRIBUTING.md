# 学生协作说明

1. 先阅读 [课程与博客推荐清单](curriculum/README.md)、B00 基础门和所选项目任务卡。
2. 每位学生只选择一个主项目，并使用自己的 feature 分支；不要直接向 `main` 推送。
3. 保持小而可解释的提交，例如：

   - `chore: reproduce starter baseline`
   - `feat: implement core behavior`
   - `test: add boundary case`
   - `docs: record design and limitation`

4. 提交前运行：

   ```powershell
   uv run --locked python scripts\validate_projects.py
   uv run --locked python scripts\run_public_tests.py --project <PROJECT_ID>
   uv run --locked python scripts\run_notebooks.py
   ```

5. Pull Request 描述必须包含修改范围、运行命令、结果和已知问题。不要提交 API Key、Token、真实个人信息或生产数据。

导师验收只依赖公开材料和现场说明；隐藏测试、导师 Notebook 和内部评分材料不在本仓库。
