# Bounded forward exercises

Date: 2026-10-16 (Asia/Shanghai). These are qualitative release-development exercises, not blinded model benchmarks or device-acceptance evidence.

## Setup

Each fresh agent was instructed to use the local installable Skill and received only its own fixture location and the task below. Agents were not given expected diagnoses or fixes. They could read the Skill's referenced modules. The parent inspected outputs and reran deterministic checks. No production source or private project data was used.

## 1. Mature button fixture

Task: fix operation buttons that sometimes remain scaled after an interrupted press; check same-kind buttons; preserve styling, navigation and range behavior; implement and verify.

Inputs: [AGENTS.md](./button-case/AGENTS.md), [original press handler](./button-case/press.original.cjs), [app.cjs](./button-case/app.cjs), [index.html](./button-case/index.html).

Read modules: buttons, motion-feedback, verification, plus the main entrypoint. The independent Reasoning Workflow was also available in the host.

Observed: changed only the shared press handler and added event tests. Added reset paths for release/cancel, focus and lifecycle interruption, disable/removal and cleanup. Did not manually synthesize action clicks or take pointer capture. The original cancellation sequence retained the pressed flag; the final handler cleared it. Fourteen Node tests passed when rerun by the parent.

Outputs: [press.cjs](./button-case/press.cjs), [press.test.cjs](./button-case/press.test.cjs). Browser validation could not run because Chromium was absent. Synthetic event tests cannot certify native click targeting, rendered appearance, real gestures, performance or browser-specific behavior. The document-wide mutation observer in this small fixture is an implementation choice requiring workload review before production reuse; the Skill does not prescribe it.

## 2. New desktop project

Task: establish a concise visual/interaction baseline and first implementation/verification slice; plan only, no code or file changes.

Input: [BRIEF.md](./new-case/BRIEF.md).

Read modules: project-baseline, typography-layout, verification. The agent proposed import → search → inspect metadata → remove-from-list, with empty/error, keyboard, screen-reader and reduced-motion checks. It retained system fonts, light/dark themes and solid surfaces; it did not impose liquid glass or generate a framework.

Suggested dimensions and undo behavior were design proposals, not validated requirements or approved parameters. No project was built or visually tested. The input tree remained unchanged.

## 3. Oral report with no source

Task: diagnose a slider that “seems stuck” and assess full refactoring or liquid glass; diagnosis only, no file changes.

Input: [REPORT.md](./readonly-case/REPORT.md).

Read modules: sliders-input, motion-feedback, materials-color, style-liquid-glass and verification. More than the typical 1–3 modules were read because the request explicitly included a material change and verification limits.

Observed: separated the reported symptom from possible causes, withheld a full-refactor conclusion, identified input/state/performance evidence needs and treated glass as a separate optional experiment. No cause, rendering success or performance gain was asserted. The input tree remained unchanged.

## 4. Static hierarchy brief (0.2.0)

Task: critique hierarchy in a mature two-pane research manager, preserve approved identity, navigation and all content, plan only.

Input: [BRIEF.md](./composition-case/BRIEF.md).

Read modules: visual-composition, typography-layout, verification. Observed: proposed three focused changes to task emphasis, grouping and action priority; kept the approved fonts/theme and destructive confirmation; did not rewrite the shared large-size token or claim equal text size alone proved a defect. No files were changed. Source observations were supplied in the brief rather than directly inspected, and no rendered UI or user outcome was verified.

## 5. Web/Compose boundary brief (0.2.0)

Task: assess uniform 44-by-44 pixels, aria-label and browser blur across a Web settings page and Android Compose page; analysis only.

Input: [BRIEF.md](./platform-case/BRIEF.md).

Read modules: platform-adaptation, verification, materials-color, buttons. Observed: rejected mechanical unit/API conversion and ARIA on native surfaces, preserved approved system fonts and controls, and separated existing evidence from proposed checks. It did not invent a confirmed defect or uninspected platform threshold. No files or services were changed.

## Interpretation

These exercises support that the entrypoint can route five concrete tasks and constrain unsupported claims in those contexts. They do not establish broad cross-stack effectiveness, universal host compliance, repeatability across models, token savings or improved user satisfaction. No numeric success-rate claim is made.
