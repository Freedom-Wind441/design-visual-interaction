# Validation record

[简体中文](./VALIDATION.zh-CN.md)

Release: **0.3.1**, 2026-10-29 (Asia/Shanghai).

The previous 0.3.0 exercise results below are historical. Version 0.3.1 adds interface-copy rules; static/package and existing fixture checks do not demonstrate real-world usability or screen-reader behavior.

## Scope

Validation separates package integrity, bounded forward exercises, and actual application quality. This release does not certify universal UI improvement or host compatibility.

## Reproducible checks

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
node scripts/check_public_examples.cjs
python -m unittest discover -s tests
node --test docs/evaluation/button-case/press.test.cjs
```

- Skill Creator's `quick_validate.py` accepted the installed entrypoint.
- Repository validator: required metadata, 13 reachable modules and common module sections, 18-file allowlist, local links/anchors, SVG XML, matching MIT licenses, version consistency, scoped privacy/placeholder patterns, SHA-256 manifest and independently checked clean installation-layout copy.
- Seven release-contract tests exercise a valid copy and rejection of duplicate metadata, missing modules, escaping references, machine-specific paths, symlinks and fingerprint drift.
- Three additional tests check the guarded upstream edit, rejection of source drift, and rejection of repeated application.
- Fourteen Node event-model tests cover cancellation/release, capture loss, focus/lifecycle interruption, disable/removal, cleanup, unrelated pointers, shared-button consumers and unchanged range/action behavior.

The manifest at [docs/skill-manifest.json](./docs/skill-manifest.json) fingerprints the installable files. It is regenerated explicitly with `python scripts/validate.py --write-manifest` after intentional changes; the normal validator never silently updates it.

Pattern scanning is limited to the installable folder and known patterns. It is not a comprehensive secret detector or proof of absence of personal data. External links and badge availability are not continuously checked.

## Current-rule exercise

A fresh isolated token task exercised the revised rules: only two Save styles changed to existing duration/easing/scale tokens, inheriting reduced motion. The parent independently compared the output and preserved theme/button semantics. Chromium was unavailable; no rendered acceptance is asserted. [Task and raw before/after](./docs/evaluation/token-case/TASK.md).

These checks support the stated fixture contracts and one observed token route. Three separate public-project source cases are described below. The general rules remain policy constraints awaiting broader outcome evidence; no claim of universal validation is made.

## Public-source case checks

[Three real upstream cases](./docs/examples/README.md) use pinned commit/parent source excerpts and retained Apache-2.0/NOTICE, MIT and BSD-3-Clause licenses. The original source and relevant upstream diffs/tests were read. Local excerpt fingerprints match [provenance](./docs/examples/public-provenance.json).

`node scripts/check_public_examples.cjs` runs eight JS adapter/closure contracts against both versions: press-capture old 3/4 → later 4/4; slider-commit old 3/4 → later 4/4. It also checks three actual Dart expression chains statically: old 0/3 → later 3/3. Expected baseline failures are counterexamples, not baseline passes. The runner does not replace the full hooks/components, real drag/index-selection, browser dispatch or Flutter runtime. Upstream tests were not rerun; the Radix commit contains no test file. These historical fixes are not attributed to this Skill.

## Forward exercises

Three initial agents, two additional 0.2.0 agents and one 0.3.0 token-task agent received the Skill path and isolated task artifacts, without expected fixes or diagnoses. Inputs and observed outputs are summarized in [docs/evaluation/results.md](./docs/evaluation/results.md). This is a small qualitative exercise, not a generalization benchmark.

| Case | Observed result | Bound |
| --- | --- | --- |
| Mature button fixture | Fixed the shared press handler, preserved styles and range behavior, supplied passing event-model tests | No real-browser rendering or physical-input validation |
| New desktop project | Produced a baseline and representative-flow plan; kept native fonts and solid surfaces; did not implement | Suggested values remain proposals, no running app |
| Static hierarchy brief | Preserved approved product identity and content; proposed three focused changes; separated design hypotheses from observed facts | No application source or rendered/behavioral acceptance |
| Web/Compose adaptation brief | Rejected uniform CSS dimensions/ARIA/blur across rendering layers; preserved native controls | No actual defect or platform conformance was established |
| Existing-token button task | Reused existing theme/press tokens with only two declarations changed | Source comparison only; Chromium unavailable |
| Oral slider report only | Distinguished the reported symptom from hypotheses, withheld a full-refactor conclusion and identified evidence needs | No source or runtime available; no root cause established |

The button agent attempted local browser validation, but Chromium was unavailable. No browser installation or live deployment occurred. The event fixture uses a synthetic DOM/event surface and is not a production component library.

## Compatibility and remaining gaps

- Local authoring, standalone folder validation and isolated agent reading were exercised.
- The authored Skill was saved through the Skills workspace; availability after client refresh is not a cross-client loading test.
- Codex CLI/IDE discovery, ChatGPT import/API upload, Windows/macOS clients and every Agent Skills host were not tested.
- No real Android/iOS/desktop application was modified or visually accepted for this release.
- Liquid-glass quality, performance, native system material APIs and assistive-technology behavior remain project-specific validation work.
- Full English execution-rule translation and user-approved before/after device examples are not included.

Do not convert static validation or these exercises into a claim of successful real-device UI optimization.
