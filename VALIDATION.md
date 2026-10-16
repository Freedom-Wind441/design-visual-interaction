# Validation record

[简体中文](./VALIDATION.zh-CN.md)

Release: **0.2.0**, 2026-10-16 (Asia/Shanghai).

## Scope

Validation separates package integrity, bounded forward exercises, and actual application quality. This release does not certify universal UI improvement or host compatibility.

## Reproducible checks

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests
node --test docs/evaluation/button-case/press.test.cjs
```

- Skill Creator's `quick_validate.py` accepted the installed entrypoint.
- Repository validator: required metadata, 12 reachable modules and common module sections, 17-file allowlist, local links/anchors, SVG XML, matching MIT licenses, version consistency, scoped privacy/placeholder patterns, SHA-256 manifest and independently checked clean installation-layout copy.
- Seven release-contract tests exercise a valid copy and rejection of duplicate metadata, missing modules, escaping references, machine-specific paths, symlinks and fingerprint drift.
- Three additional tests check the guarded upstream edit, rejection of source drift, and rejection of repeated application.
- Fourteen Node event-model tests cover cancellation/release, capture loss, focus/lifecycle interruption, disable/removal, cleanup, unrelated pointers, shared-button consumers and unchanged range/action behavior.

The manifest at [docs/skill-manifest.json](./docs/skill-manifest.json) fingerprints the installable files. It is regenerated explicitly with `python scripts/validate.py --write-manifest` after intentional changes; the normal validator never silently updates it.

Pattern scanning is limited to the installable folder and known patterns. It is not a comprehensive secret detector or proof of absence of personal data. External links and badge availability are not continuously checked.

## Forward exercises

Three initial agents and two additional fresh agents received the Skill path and isolated task artifacts, without expected fixes or diagnoses. Inputs and observed outputs are summarized in [docs/evaluation/results.md](./docs/evaluation/results.md). This is a small qualitative exercise, not a generalization benchmark.

| Case | Observed result | Bound |
| --- | --- | --- |
| Mature button fixture | Fixed the shared press handler, preserved styles and range behavior, supplied passing event-model tests | No real-browser rendering or physical-input validation |
| New desktop project | Produced a baseline and representative-flow plan; kept native fonts and solid surfaces; did not implement | Suggested values remain proposals, no running app |
| Static hierarchy brief | Preserved approved product identity and content; proposed three focused changes; separated design hypotheses from observed facts | No application source or rendered/behavioral acceptance |
| Web/Compose adaptation brief | Rejected uniform CSS dimensions/ARIA/blur across rendering layers; preserved native controls | No actual defect or platform conformance was established |
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
