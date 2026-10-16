# Check pointer capture before releasing it

**Public source:** Adobe React Spectrum / React Aria, [commit a9ce237](https://github.com/adobe/react-spectrum/commit/a9ce2379c424ab80612933451dd3fee4181ac39a), parent `808343c2b7ebf7d58443d0a53b88b135e1ba5461`.

**Problem and cause.** `usePress` released pointer capture whenever the target exposed the release method. Method availability alone did not establish that the target held capture for this pointer. The commit also fixes the analogous `useCalendarCell` consumer. This is a shared input-path issue, not evidence that the button needs new geometry or a material change.

**Modules.** Use buttons for activation/capture semantics, motion-feedback for interruption, and verification for source versus actual input evidence.

**Before/after.** The [original excerpt](./press-capture.before.txt) calls release directly; the [later excerpt](./press-capture.after.txt) checks `hasPointerCapture(pointerId)` when available and retains the existing compatibility branch when that method is absent. Exact source locations are pinned in [provenance](./public-provenance.json). Both excerpts retain their original TypeScript syntax.

**Minimum change.** Guard the existing release operation; inspect equivalent consumers before deciding whether the shared root cause extends beyond one button. Preserve native activation, pointer IDs and existing enter/leave behavior. Do not infer from this case that every control should take capture, or that every target without the check method is safe to release in other projects.

**Validation performed.** The upstream diff includes a regression for capture absent and adjusts capture-present expectations. Those tests were read, not run. Our four isolated cases execute each actual excerpt with recording targets: capture true, capture false, check method unavailable, and release method unavailable. Old source fails the capture-false contract; later source passes all four. The runner only erases the TypeScript type assertion to execute JavaScript; it preserves the control flow.

**Unverified.** Native capture/dispatch, real pointer leave/enter, keyboard/touch cancellation, rendered press feedback and browser compatibility. These adapter results cannot certify the entire `usePress` hook or the calendar consumer.

**Attribution.** Copyright 2020 Adobe. All rights reserved. Apache-2.0; React-derived portions carry the upstream notice. See [licenses and notices](./third-party-notices.md).
