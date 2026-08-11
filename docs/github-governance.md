# GitHub 治理与外部配置

> 决策版本：2026-08-11。组织创建、仓库迁移和分支规则仍属于 GitHub 外部设置，不能仅靠提交 Markdown 自动完成。

## 已确认的治理决策

- 目标组织：`ttai-internship`。
- 当前管理者：`Densityyang` 本账号作为唯一 Owner/管理员，负责 PR 审查、任务生成、发放、验收和删除；后续再邀请导师并按角色分权。
- 学生作业：一人一个独立私有仓库。
- 学生权限：仅 `Write`，不授予 Admin，不允许修改仓库设置、Actions Secrets 或组织权限。
- 学生仓库和提交材料只使用 pseudonymous assignment ID，不写入真实姓名、学号、简历或面试记录。
- 作业、评分、答辩记录、AI 使用记录和 ID 映射在最终验收后保留 30 个自然日，之后由当前管理员删除；争议或法定留存例外必须记录原因和新的删除日期。
- 允许使用 AI，但必须提交 `AI_USE.md`，并在现场说明关键修改、验证方式和一个被拒绝或改写的建议。
- 培训评价采用 `Core 完成 + 总分 >= 60`，优秀采用 `Core 完成 + 总分 >= 85`；人才库、留用和后续岗位判断不从自动分数推导。

## 仓库边界

- 公开学生仓：只发布 starter、学生 Notebook、公共测试、任务卡和提交模板。
- 私有导师仓：维护导师 Notebook、隐藏 Core 测试、评分、assignment pack 和内部记录。
- 学生私有作业仓：由私有导师仓生成 pack 后单独创建，每个仓只对应一个 pseudonymous assignment ID。
- 当前公开仓和私有仓仍在 `Densityyang` 个人账号下；组织创建并完成设置核验后，再按迁移计划转入 `ttai-internship`。

## 分发路线

GitHub Classroom 已进入迁移期，不作为新项目的默认依赖。当前采用“私有导师仓生成 assignment pack → 由当前管理员在组织下创建一人一仓”的路线。已有 Classroom 的课程需要在官方迁移窗口内导出或迁移，不把新的业务流程绑定到旧 Classroom。

创建每个作业仓前，管理员至少确认：

1. assignment ID 只包含可追踪但不含真实身份的信息；
2. 项目、周期和 A03 paper pack 已写入 assignment metadata；
3. 仓库可见性为 Private，学生权限为 Write；
4. 仓库不包含导师 Notebook、隐藏测试、评分记录或其他学生数据；
5. 学生收到的 CI 只需要 `contents: read`，不配置生产 Secrets。

## PR 与合并门禁

1. `main` 禁止直接 push、force-push 和删除。
2. PR 必须先完成人工审查，再通过对应 CI：公开仓为 `student-checks`，私有仓为 `repository-checks`。
3. 默认采用 squash merge；关闭 Auto-merge。P0→P1→P2 等 stacked PR 必须按依赖顺序合并，未完成下游合并前不要删除中间分支。
4. 当前所有审查由 `Densityyang` 执行。由于 PR 作者不能批准自己的 PR，GitHub 的“至少一名审批人”规则应在第二个导师账号加入后再启用；在此之前，人工审查记录和 CI 是实际门禁。
5. 合并后的主分支仍需保留可追踪的 CI 记录和 PR 链接。

## Actions 与依赖安全

- 每个工作流声明 `permissions: contents: read`，不向学生 PR 提供写权限或生产 Secrets。
- 第三方 Action 固定到完整 commit SHA，并由 Dependabot 提交更新 PR。
- 组织创建后，Actions 允许列表收紧为实际使用的 Action（如 checkout、setup-python、setup-uv），不长期保留仓库级 `allowed_actions: all`。
- 来自学生仓库或 Fork 的代码只能在无敏感 Secrets 的环境执行；需要外部服务时必须提供离线 fallback 或固定 trace。

## 当前外部设置待执行

- 创建 `ttai-internship`，当前账号作为唯一 Owner；暂不邀请其他成员。
- 将公开学生仓和私有导师仓迁移到组织，并核对迁移后的 remote、Actions、Dependabot 和访问权限。
- 在组织/仓库层配置 `main` 分支保护；公开仓可使用 Free 分支保护，私有仓需确认组织方案是否支持保护规则。
- 创建后续角色：`mentor-reviewer`、`assignment-operator`、`data-retention-admin`；当前均由 `Densityyang` 承担。
- 建立 30 天删除台账，不把真实身份映射或删除记录提交到 Git。

具体留存规则见[数据留存与删除政策](data-retention.md)。
