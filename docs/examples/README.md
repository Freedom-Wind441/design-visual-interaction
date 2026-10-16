# Real public-source before/after cases

**English** · [简体中文](./README.zh-CN.md)

Three historical fixes from public upstream repositories illustrate the current Skill modules retrospectively. They are not fixes performed by this Skill, measurements of Skill effectiveness, complete application ports, or reasons to install a new UI library. No private project source is included.

| Public project | Problem → minimal change | Modules | Verified here |
| --- | --- | --- | --- |
| [React Aria](./press-capture.md) | Release called without checking capture ownership → guard the existing path | buttons, motion-feedback, verification | Four JS adapter cases on each excerpt; old source fails one |
| [Radix Slider](./slider-commit.md) | Commit missed when thumbs overlap → compare the full value array | sliders-input, verification | Four JS closure cases on each excerpt; old source fails one |
| [Flutter NavigationBar](./navigation-theme.md) | No widget-level label-style override → retain the existing widget/theme/default chain | dock-navigation, typography-layout, project-baseline | Three static precedence checks per excerpt; no Dart runtime |

Each case links a pinned commit, its parent, original source and actual before/after excerpts, then separates the reported problem, confirmed code path, module selection, minimal change, checks and remaining gaps. [public-provenance.json](./public-provenance.json) records commit/file locations and excerpt fingerprints. [Third-party notices](./third-party-notices.md) preserve source attribution and licenses.

```bash
node scripts/check_public_examples.cjs
```

The check executes two extracted JavaScript paths with explicit collaborators and inspects one Dart expression chain. It intentionally checks both versions: expected old failures confirm the described counterexamples; only the later excerpts must pass all checks. It does not install or run the full React Aria, Radix or Flutter suites, simulate native pointer routing, draw a frame, or prove physical-device behavior. Upstream regression tests were inspected where included in the commits; their passing status was not independently rerun here.

The existing [button event fixture](../evaluation/results.md#1-mature-button-fixture) and [token fixture](../evaluation/token-case/TASK.md) are separately labeled synthetic exercises. The full excerpts, licenses and repository-only check do not ship in the installable Skill folder. A compact original-language case reference with upstream links is available on demand inside the Skill.
