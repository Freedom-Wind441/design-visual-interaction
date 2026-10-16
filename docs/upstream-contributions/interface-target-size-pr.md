# Clarify WCAG target-size levels and usability guidance

The current hit-area guidance mixes a recommended usability target with WCAG conformance requirements and an unexplained smaller minimum. This can cause an agent to treat a design recommendation as the standard's universal threshold.

Keep the recommendation to aim for a larger hit area, and explicitly distinguish:

- [WCAG 2.2 SC 2.5.8, Level AA](https://www.w3.org/TR/WCAG22/#target-size-minimum): 24×24 CSS px, with spacing and other exceptions.
- [WCAG 2.2 SC 2.5.5, Level AAA](https://www.w3.org/TR/WCAG22/#target-size-enhanced): 44×44 CSS px, with its own exceptions.
- Native-platform dimensions and semantics, which should use the relevant platform guidance.

The change is limited to the static-polish hit-area paragraph in the core Skill. It preserves the smaller-visible-control example and the rule against overlapping hit targets. No runtime, plugin version, installation surface or unrelated style guidance changes.

Validation:

- Compared the source against the inspected upstream Git blob before applying.
- Applied the change to a temporary copy and checked that only the intended paragraph and clarification were changed.
- Verified a second application rejects the changed blob without another write.
- Checked the two normative W3C criteria.
- No runtime or rendered-UI test applies to this documentation-only correction.

AI assistance: prepared with OpenAI Codex and reviewed against the cited W3C criteria. This proposal is not a report of a real-device accessibility audit.
