<div align="center">

# 视觉与交互设计

### 保留项目特色，修复真正需要改动的部分。

用于 UI 一致性审查、局部交互修复与渐进设计优化的模块化 Agent Skill。

[English](./README.md) · **简体中文**

[![Version](https://img.shields.io/badge/version-0.3.1-2563eb)](./CHANGELOG.zh-CN.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-475569)](./LICENSE)
[![Validation](https://github.com/Freedom-Wind441/design-visual-interaction/actions/workflows/validate.yml/badge.svg)](https://github.com/Freedom-Wind441/design-visual-interaction/actions/workflows/validate.yml)

[快速开始](#快速开始) · [模块](#模块) · [配套关系](#与其他-skill-的关系) · [验证](./VALIDATION.zh-CN.md)

**[浏览 Skill](./skills/design-visual-interaction/)** · [阅读执行规则](./skills/design-visual-interaction/SKILL.md)

</div>

---

## 快速开始

在具备 `$skill-installer` 的 Codex 中输入：

```text
$skill-installer install https://github.com/Freedom-Wind441/design-visual-interaction/tree/v0.3.1/skills/design-visual-interaction
```

建议固定 **v0.3.1**，保证安装可复现；`main` 用于开发，升级前先看变更记录。

然后直接描述目标：

```text
使用 $design-visual-interaction，只优化这个按钮的按压反馈。
保留当前主题、动作语义和配置，检查共享消费者并验证结果。
```

执行者自行判断需要哪些模块，使用者不用记忆文件结构。

<details>
<summary>手动安装与固定版本</summary>

将完整的 [`skills/design-visual-interaction/`](./skills/design-visual-interaction/) 复制到宿主规定的位置。Codex 的项目级与用户级位置分别为 `.agents/skills/design-visual-interaction/` 和 `~/.agents/skills/design-visual-interaction/`。

保留 `SKILL.md`、`agents/`、`references/`、`assets/` 与 `LICENSE`。其他宿主请遵循各自文档。需要可复现安装时使用已发布 tag 或准确 commit；快速开始中的链接已固定到本版。

</details>

Skill 不需要运行脚本、API 密钥、固定 MCP 服务或安装依赖包。具体修改仍需项目源码、构建工具，以及适当的渲染与输入验证条件。

## 能做什么

| 项目或任务 | 默认做法 |
| --- | --- |
| 新项目 | 建立小规模设计基线，先实现并验证代表流程 |
| 成长中的项目 | 从源码追踪组件、token、事件或平台根因，渐进修复 |
| 成熟项目 | 保留成熟决策，只改有证据的问题，允许零修改 |
| 只改一个组件 | 读取相关模块与必要依赖，检查共享消费者 |
| 只审查或出方案 | 交付诊断或方案，不擅自修改工程 |

默认目标是**产品内部一致**。它不提供现成 UI 组件库，不自动换肤，不要求全面重写，也不保证所有项目必然改善。

本版已核对六类同类项目的实际规则与源码，见[比较与采用记录](./docs/comparison.zh-CN.md) / [English](./docs/comparison.md)。本项目不声称首创这一类别，也不替代这些覆盖更广的工具链。

## 模块

主入口提供公共规则与调度索引，详细规范按需读取；关联模块不等于全部加载。

| 模块 | 关注内容 |
| --- | --- |
| [项目基线](./skills/design-visual-interaction/references/project-baseline.md) | 产品约束、现有 token、稳定规则与试验参数 |
| [构图与视觉层级](./skills/design-visual-interaction/references/visual-composition.md) | 任务重点、分组、密度、设计方向与评议 |
| [平台适配](./skills/design-visual-interaction/references/platform-adaptation.md) | 实际渲染层、平台单位、语义与对应验证 |
| [Dock 与导航](./skills/design-visual-interaction/references/dock-navigation.md) | 选中、历史、手势、安全区域 |
| [按钮](./skills/design-visual-interaction/references/buttons.md) | 语义角色、命中区、取消、激活 |
| [排版与布局](./skills/design-visual-interaction/references/typography-layout.md) | 层级、字体回退、本地化、大字号 |
| [滑块与数值输入](./skills/design-visual-interaction/references/sliders-input.md) | 范围映射、预览/提交、手势、持久化 |
| [设置与引导](./skills/design-visual-interaction/references/settings-onboarding.md) | 入口、下级选项、能力适配 |
| [动效与反馈](./skills/design-visual-interaction/references/motion-feedback.md) | 动画中断、清理、减少动态效果 |
| [颜色与材质](./skills/design-visual-interaction/references/materials-color.md) | 语义色、对比、合成、降级 |
| [可选实验：液态玻璃](./skills/design-visual-interaction/references/style-liquid-glass.md) | 清晰内容层、限制折射、性能边界 |
| [公开真实案例](./skills/design-visual-interaction/references/worked-examples.md) | 紧凑历史模式、原始来源与验证边界 |
| [验证与交付](./skills/design-visual-interaction/references/verification.md) | 与实际改动和环境对应的证据 |

![组件分层与取消路径示意](./skills/design-visual-interaction/assets/component-anatomy.svg)

这是原创原则示意，不是认可的产品截图、已测视觉效果或固定风格预设。

## 与其他 Skill 的关系

本项目是[软件架构 Skill](https://github.com/Freedom-Wind441/design-software-architecture) 的**视觉与交互配套扩展**，独立维护、安装和使用，没有强制技能依赖。

| Skill | 职责 | 归属 |
| --- | --- | --- |
| **视觉与交互设计** | 体验目标、组件规范、视觉一致性与 UI 验收 | Freedom-Wind441，本仓库 |
| **[软件架构](https://github.com/Freedom-Wind441/design-software-architecture)** | 职责边界、状态所有权、复用与必要迁移 | Freedom-Wind441，独立仓库 |
| **[Reasoning Workflow](https://github.com/zy839971925-zyy/Agent--deep-research-Workflow-Skills)** | 通用推理、证据与执行控制 | 独立第三方 zy839971925-zyy |

结构问题阻碍可靠 UI 修复时，才联动架构 Skill；局部参数修改不扩大为架构重写。Reasoning Workflow 可用时配合使用，按[上游说明](https://github.com/zy839971925-zyy/Agent--deep-research-Workflow-Skills#start-in-30-seconds) 独立安装。

本仓库不复制、打包、自动安装或重新许可配套技能，不将 Reasoning Workflow 归为作者作品，也不通过虚构 manifest 字段声称能自动调用其他技能。

## 示例

[最小使用案例](./docs/usage-examples.zh-CN.md)包含按钮反馈、设置层级和只读审计；[合成按钮演练](./docs/evaluation/results.md#1-mature-button-fixture)附事件代码前后对照，另有 token 样例记录局部样式变化；[三个公开项目真实案例](./docs/examples/README.zh-CN.md)补充 React Aria 按压、Radix范围提交与Flutter导航字体修复，附固定源码、许可和有界检查；[模块关系图](./docs/module-routing.md)解释按需加载。

**审查已有产品**

```text
使用 $design-visual-interaction 审查视觉与交互一致性。
保留产品特色，从源码与运行证据确定根因，不修改文件，
交付建议并说明实际验证结果及缺口。
```

**从零建立基线**

```text
使用 $design-visual-interaction 为新的桌面应用建立精简规范。
遵守平台习惯，保留键盘访问与明暗主题，先完成代表流程，
再按实际需要扩展组件。
```

**与架构 Skill 协作**

```text
使用 $design-visual-interaction 和 $design-software-architecture
修复共享控件不一致。只有现有结构阻碍修复时才重构，
保留行为与配置，验证受影响的使用位置。
```

## 验证与限制

这是实验版本。v0.3.0 补强 token 提取与复用、按改动类型分层验证和玻璃实验边界；合成演练与三组公开源码历史案例分别标记；片段/事件检查不代表实机验收或技能造成的提升。仓库检查覆盖元数据、本地链接、模块可达性、许可证/版本、限定范围的隐私模式、内容指纹和干净安装布局复制。隔离任务演练及其限制见[验证记录](./VALIDATION.zh-CN.md)。静态检查不能证明视觉品质或宿主兼容性。

安装包的执行规则与专项模块使用简体中文；仓库文档和显示元数据默认英文，并提供中文文档入口。此版没有把全部执行规则翻译为英文。

按需加载可以减少无关上下文，但实际 token 消耗还取决于宿主、任务和返工，不承诺固定节省比例。

## 仓库结构

| 位置 | 用途 |
| --- | --- |
| [`skills/design-visual-interaction/`](./skills/design-visual-interaction/) | 自包含的可安装 Skill |
| [`CHANGELOG.md`](./CHANGELOG.md) / [中文](./CHANGELOG.zh-CN.md) | 更新记录，版本号见 [VERSION](./VERSION) |
| [`VALIDATION.md`](./VALIDATION.md) / [中文](./VALIDATION.zh-CN.md) | 证据与限制 |
| [`docs/usage-examples.zh-CN.md`](./docs/usage-examples.zh-CN.md) | 三个有界提示词与冲突示例 |
| [`docs/examples/`](./docs/examples/) | 公开项目真实差分、原许可及验证限制 |
| [`docs/evaluation/`](./docs/evaluation/) | 可复现的隔离演练输入及结果 |
| [`docs/sources.md`](./docs/sources.md) | 格式来源与原始规范链接 |
| [`scripts/validate.py`](./scripts/validate.py) | 仓库检查，不随技能安装 |

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
node scripts/check_public_examples.cjs
python -m unittest discover -s tests
```

## 许可证

[MIT](./LICENSE) · Copyright (c) 2026 Freedom-Wind441。安装目录附带相同许可证；引用的第三方项目保留自己的许可。
