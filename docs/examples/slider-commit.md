# Commit a range change when thumbs overlap

**Public source:** Radix Primitives, [commit 78a9d2b](https://github.com/radix-ui/primitives/commit/78a9d2baedf2e009e3a3786e46e1a29edc640162), parent `e6e99a5d43a1b537baf8dd19f8a5db67b3ae6080`.

**Problem.** Dragging a two-thumb range from `[105, 107]` to `[105, 105]` could finish without calling `onValueCommit`.

**Source cause.** The [old handler](./slider-commit.before.txt) compared just the values at `valueIndexToChangeRef.current`. At overlap, the upstream index lookup can point to index zero for both thumbs, making the compared first elements equal even though the full range changed. The [new handler](./slider-commit.after.txt) compares the whole numeric array before deciding whether to commit. See [pinned provenance](./public-provenance.json).

**Modules and minimum change.** Use sliders-input to distinguish changing preview from final commit, then verification for unchanged values and endpoint cases. Keep the existing state and callback owner; repair the end-of-gesture predicate rather than replacing the slider or persistence layer. `String(values)` is the choice in this upstream numeric-array context, not a universal equality strategy for objects, nested arrays or every input model.

**Validation performed.** The upstream commit changes the production handler only; no regression-test file is present in that commit. Our runner executes both actual handler excerpts with the captured closure state and four callback contracts: overlap, ordinary right-thumb change, unchanged range and left-thumb change. Old source misses only the overlap commit; later source passes all four. The runner supplies the described index state; it does not reproduce the full drag/index-selection pipeline.

**Unverified.** Physical dragging, actual index calculation, React render timing, focus behavior, pointer cancellation and visuals. No full Radix test suite or browser was run. This excerpt is an explanatory slice, not a drop-in component patch.

**Attribution.** Copyright (c) 2022 WorkOS. MIT; see [license](./third-party-notices.md).
