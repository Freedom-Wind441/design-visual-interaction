# Sources and provenance

Format baseline: [Software Architecture v0.2.0](https://github.com/Freedom-Wind441/design-software-architecture), default-branch tree `6f89204d56e2828ffa3689ea962fce471ed252d8`, inspected on 2026-10-16 (Asia/Shanghai). Reused conventions: English landing page, Chinese counterpart, separate installable folder, license copy, version file and reproducible validation. Its architecture execution rules were not copied into this Skill.

Primary specification references inspected for this release:

- [Agent Skills specification](https://agentskills.io/specification): naming, metadata, directory structure, progressive disclosure and relative resources.
- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills): host-facing skill guidance. Host loading/import behavior still requires separate testing.
- [W3C: Contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) and [Target size minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html): web accessibility context. Normative criteria, exceptions and target level must be checked for the project; CSS pixel thresholds are not native-app dimensions.
- [Apple: Materials](https://developer.apple.com/design/human-interface-guidelines/materials): a platform reference for future project work; full page content was not retrievable in this session. No claim of Apple conformance is based on it.

The execution modules and schematic are original guidance for this repository, not copied vendor components or approved screenshots. No screenshots, fonts, third-party packages or private project assets are bundled.

For the 0.2.0 research update, see [the six-project comparison](./comparison.md), [中文](./comparison.zh-CN.md), and [exact inspected snapshots](./research-snapshots.json). Adopted concepts were independently authored into the local rules; no third-party implementation or whole-rule translation is bundled. The guarded upstream correction is a separate repository-development artifact, not an installed runtime dependency.

[Reasoning Workflow](https://github.com/zy839971925-zyy/Agent--deep-research-Workflow-Skills) is only linked. Its contents, ownership and license remain upstream. Design decisions suggested by this Skill still require project-specific evidence.
