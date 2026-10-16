# Isolated token task

Use the Skill to unify only Save button press feedback with the other controls, making it feel more modern. Preserve colors, behavior and the rest of the interface. Implement and verify what is feasible.

Input: `before.html` and `theme.css`, named `index.html` and `theme.css` in an isolated directory. The agent received only the Skill location, fixture location, requested scope and no-external-action constraint. No expected fix, historical examples, tests or parent diagnosis was provided. It did not modify the Skill.

Observed output: `after.html`. Only Save's two declarations changed to the existing duration/easing and scale variables. `theme.css` and native button/form semantics were retained. Parent source comparison confirmed these facts. Browser launch failed because Chromium was unavailable; there is no rendered, input or device acceptance. This single exercise is not a cross-model benchmark.
