# 同类项目比较与采用记录

[English](./comparison.md)

检索与源码核对日期：2026-10-16（Asia/Shanghai）。准确 commit 和关键文件 blob 见 [research-snapshots.json](./research-snapshots.json)。比较依据为实际规则、源文件与许可证；没有按 star 排名，也没有安装、运行或评测这些完整产品。

## 比较结果

| 项目 | 值得借鉴的实际能力 | 本版采用方式与边界 |
| --- | --- | --- |
| [Impeccable](https://github.com/pbakaus/impeccable)，Apache-2.0 | 区分技术审查/设计评议、按任务分配参考、长期产品/设计记录、原生专项审查与确定性 Web 检查器 | 区分技术证据和设计判断，按用户影响排序，检查工具误报；不引入整套引擎、指令集、主观总分和审美禁令 |
| [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)，MIT | 按领域/技术栈搜索，生成设计系统，保存全局规范及页面覆盖，保护已有决策 | 按问题和真实技术栈分配模块，明确全局规则/局部例外；不打包其数据库和生成器，也不要求局部任务生成整套设计系统 |
| [Anthropic frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design)，该 Skill 为 Apache-2.0 | 从产品内容形成方向，重视排版、构图、文案和设计自检 | 新增构图与视觉层级；选择应服务任务，不把新奇作为验收条件，保留已认可的系统字体和合理布局 |
| [Vercel Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines)，MIT | 明确到文件位置的语义、焦点、内容、输入与性能检查 | 补强具体发现和误报核验；不将全部 Web 写法套到原生，也不每轮强制抓取远程规则 |
| [Google Stitch skills](https://github.com/google-labs-code/stitch-skills)，Apache-2.0 | 从设计与源码提取 DESIGN.md，按框架定位主题、token 与组件 | 记录语义角色、实现值/单位、源码和作用域；提取出的现状不等于已认可或渲染通过，不引入 Stitch MCP 依赖 |
| [Interface Design](https://github.com/Dammyjay93/interface-design)，MIT | 视觉层级、密度、原生/成熟基础控件复用与跨会话设计记录 | 补强层级和决策保留；不照搬固定确认/保存提问、字体禁令或未区分平台等级的尺寸规则 |

同类能力已经存在，部分项目比本技能初版覆盖更广。本仓库不应宣称首次提出模块化 UI 规范，也不能据文档比较宣称优于这些项目。需要完整 Web 设计工具链时，直接使用成熟方案可能更合适。

本项目保留的定位是：软件架构 Skill 的轻量配套扩展，依据源码选择局部模块、渐进修改，在跨平台工作中明确证据和验证边界。

## 已落实到 0.2.0

- 新增构图/视觉层级与平台适配两份模块。
- 区分技术审查、设计评议、局部修复和新建/重设计，不要求专用命令。
- 分开产品事实、设计提案、实现现状与用户认可。
- 全局规范与局部例外明确作用域，保护已有记录。
- 区分用户影响与证据充分程度，核验检查器适用性，限制无终点的反复润色。
- 补充数字排版、任务导向文案、错误/空状态和恢复方式。

采用的是可迁移的方法，并针对本项目重新编写规则；没有复制或翻译上游整段规则，没有纳入第三方实现、数据库、指令集或完整 Skill。安装目录继续不含运行脚本和依赖包，第三方归属与许可独立。

## 上游贡献判断

已为 Interface Design 准备一个具体修正：区分项目推荐命中尺寸、WCAG 2.2 AA/AAA 条件、CSS 单位及例外。见[贡献材料](./upstream-contributions/README.md)，包含校验上游内容指纹的修改脚本与可审阅 PR 正文。

Impeccable 的贡献约定要求先讨论并取得维护者许可，且对非维护者授权的 AI Issue/PR 有明确限制。本轮没有向它发送 Issue、评论或 PR，也没有修改其生成副本。

**尚未向任何上游实际提交 PR。** 这是一份独立准备的贡献候选，不代表上游已经接受。提交前需重新核对当前源文件、贡献约定和重复提案。
