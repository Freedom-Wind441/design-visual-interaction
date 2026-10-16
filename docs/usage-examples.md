# Minimal usage examples

**English** · [简体中文](./usage-examples.zh-CN.md)

Describe a goal and its boundary. The agent should load only the modules needed for the current evidence gap; a small task need not create a baseline document or read every reference. See [the synthetic button before/after exercise](./evaluation/results.md#1-mature-button-fixture) and [the token exercise](./evaluation/token-case/TASK.md) for concrete changes and their limits. These are synthetic fixtures; [three separate public-project source cases](./examples/README.md) show historical fixes with pinned evidence and retained licenses.

## Only repair button press feedback

```text
Use $design-visual-interaction to fix this button's interrupted press feedback.
Preserve the existing theme, action and stored settings. Check shared consumers;
change only the necessary handler/style. Report which input paths were actually tested.
```

Expected boundary: locate the current component and token/theme source, then use buttons, motion-feedback and verification as needed. Preserve action semantics; do not replace the input framework or add a glass style. Verify normal release, cancellation, interruption, disabled state and re-entry where affected. Source/event checks cannot replace rendered or native-input evidence.

## Only repair settings hierarchy

```text
Use $design-visual-interaction to reorganize only this settings destination.
Keep existing options, stored values, defaults and distinct interval meanings.
Identify current routes and parent-child dependencies from source before editing.
```

Expected boundary: reuse existing settings builders, disclose a necessary legacy-route adjustment, and keep business policy with its existing owner. Check parent off/on, value retention, late callbacks, back navigation, and representative language/font conditions. A route edit does not authorize unrelated Dock or business changes.

## Audit without modifying code

```text
Use $design-visual-interaction to audit this page. Do not modify files.
For each material finding, give source/observation, impact, confirmed cause or
hypothesis, smallest proposed change, and the missing validation evidence.
A no-change conclusion is acceptable.
```

Expected boundary: report a diagnosis and proposal only. Distinguish supplied screenshots from directly inspected source. Do not implement, reformat or "prepare" code without a later implementation request. Static-only audits can finish with explicit runtime gaps.

## When instructions, design and platform guidance conflict

Suppose an approved app uses solid surfaces and existing theme tokens, and the user says “make this button feel more modern.” This does not authorize glass or a parallel theme. Reuse the existing press tokens and constrain the fix to the button. If the user explicitly requests a glass experiment, isolate the requested component, retain semantic/focus/contrast requirements, reuse the theme, and define its existing-material fallback. A platform recommendation is evidence to assess, not authority to silently override a user-approved product decision. Explain a concrete unresolved conflict; ask only if a consequential choice cannot be resolved from the project or request.

## Why only a few modules?

The baseline and platform modules supply context only when it is missing; component modules supply the actual fix. Verification selects evidence for that change. Related links are conditional, not transitive dependencies. See [the routing relationship](./module-routing.md).
