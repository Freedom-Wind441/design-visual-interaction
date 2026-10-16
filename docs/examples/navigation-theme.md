# Add a scoped label-style override without a parallel theme

**Public source:** Flutter, [commit 148be5f](https://github.com/flutter/flutter/commit/148be5f894aa64d7c4e8318100b5db5ae3c9b823), parent `423aa2ac7476120ad522a577bda1dae77ffa3ff4`.

**Problem.** NavigationBar could obtain label styling from its theme but lacked the widget-level label-style override added by this fix. A local component customization should not require a second theme system or a global theme rewrite.

**Source cause.** The [old excerpt](./navigation-theme.before.txt) resolves selected, unselected and disabled labels from the navigation theme, then defaults. The [new excerpt](./navigation-theme.after.txt) checks the widget-provided property first and preserves both existing fallback sources. The complete upstream patch also adds and forwards that optional property; these expressions alone are not a complete port. See [provenance](./public-provenance.json).

**Modules and minimum change.** Use dock-navigation and typography-layout for affected label states, and project-baseline when tracing existing style authority. Add the scoped override to the established resolution chain. Preserve theme/default behavior when the override is null; do not introduce parallel colors/fonts or set every navigation label to one fixed style.

**Validation performed.** The upstream commit adds a widget regression covering selected, unselected and disabled label sizes/colors. We read the added test and source but did not run Flutter. The local script checks the three actual expressions for widget → theme → default order. Old source fails all three widget-override checks; later source passes all three. These are static checks, not executable Dart behavior or verified pixels.

**Unverified.** Dart compilation, actual theme resolution at runtime, animation between states, text scaling, localization, assistive semantics and device appearance. Follow the target Flutter version's APIs; this historical commit is not a claim that its exact type names are current for every release.

**Attribution.** Copyright 2014 The Flutter Authors. All rights reserved. BSD-3-Clause; see [license](./third-party-notices.md).
