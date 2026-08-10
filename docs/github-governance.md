# GitHub 治理与外部配置

仓库文件可以固定流程和检查，但下面几项属于 GitHub 组织/仓库设置，不能仅靠提交 Markdown 自动完成。

## 目标结构

- 组织：`densityyang-internship`（待确认是否采用）；
- 私有导师仓：维护隐藏 Core 测试、导师 Notebook、评分和 cohort 配置；
- 公开学生仓：只发布 starter、学生 Notebook、公共测试和模板；
- 正式分发：用 GitHub Classroom 为每位学生生成私有独立仓，不让学生直接共享同一个开发仓。

## 建议的仓库设置

1. 默认分支设为 `main`，禁止直接 push。
2. PR 必须通过 `repository-checks`/`student-checks` 后才能合并；至少一名导师审查。
3. 开启分支保护、强制线性历史或 squash merge，并关闭学生仓不需要的 Actions 写权限。
4. 默认 `GITHUB_TOKEN` 只读；工作流中的 Action 固定到完整 commit SHA，Dependabot 每周提出更新 PR。
5. 私有仓的隐藏测试目录和导师记录不通过 GitHub Classroom 分发。

## 仍需负责人确认

- 是否现在创建并使用 `densityyang-internship` 组织；
- 负责审查 PR 的 GitHub 账号；
- 每期学生包的命名规则、机构数据保留期限和删除责任人；
- Core 通过阈值是否维持 60 分、优秀是否维持 85 分；
- 是否允许学生将个人项目仓公开，以及公开前的脱敏审查人。
