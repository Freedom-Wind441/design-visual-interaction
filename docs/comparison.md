# Related projects and adopted ideas

[简体中文](./comparison.zh-CN.md)

Inspection: 2026-10-16 (Asia/Shanghai). Exact inspected commits and important file blobs are recorded in [research-snapshots.json](./research-snapshots.json). Findings come from actual Skill, reference, source and license files, not star rankings. External products were not installed or benchmarked.

## Comparison

| Project | Useful capability found | Integration decision and boundary |
| --- | --- | --- |
| [Impeccable](https://github.com/pbakaus/impeccable) — Apache-2.0 | Separate audit/critique and task playbooks, durable product/design context, source-based native audit, deterministic frontend detectors | Separate technical evidence from design judgment; prioritize findings by user impact; verify detector applicability. Do not add its engine, full command set, subjective scoring or stylistic prohibitions as dependencies. |
| [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) — MIT | Searchable domain/stack guidance, design-system generation, master/page persistence and preservation of existing decisions | Route by actual concern and detected stack; record global rules and scoped exceptions. Do not copy its data tables, generator or force each local task through a full design-system search. |
| [Anthropic frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) — Apache-2.0 for this Skill | Product-specific visual direction, purposeful typography/layout/copy, critique of generic composition | Add explicit composition and hierarchy work; connect choices to user tasks. Keep approved native/system fonts and legitimate patterns; novelty is not an acceptance criterion. |
| [Vercel Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines) — MIT | Concrete file-located checks for semantics, focus, content, interaction and performance | Improve actionable findings and false-positive checks; preserve the distinction between Web checks and native evidence. Do not import every Web prescription as a universal rule or refetch remote rules on every run. |
| [Google Stitch skills](https://github.com/google-labs-code/stitch-skills) — Apache-2.0 | DESIGN.md synthesis and source-based extraction with framework-specific routing | Preserve semantic role, exact implementation values/units, source and scope in existing project records. Extraction is an observation, not proof of approved or rendered design. No Stitch MCP dependency is added. |
| [Interface Design](https://github.com/Dammyjay93/interface-design) — MIT | Visual hierarchy, density, native/primitive reuse and reusable design memory | Improve hierarchy and decision retention while keeping the existing project as authority. Do not adopt mandatory direction confirmation, repeated save prompts, font bans or unqualified dimensional rules. |

These are existing, capable alternatives. This repository does not claim to invent modular UI guidance or to outperform them. A project that wants a larger web-oriented design toolchain may reasonably choose an established package directly. The intended scope here is a small, source-aware, progressively loaded companion to Software Architecture, with local fixes and evidence boundaries.

## Changes made in 0.2.0

- Added visual composition/hierarchy and platform-adaptation references.
- Distinguished audit, critique, focused repair and new-direction work without requiring special commands.
- Separated product facts, proposed design, observed implementation and approved decisions.
- Added global defaults plus explicitly scoped component/page exceptions.
- Added impact/evidence separation, scanner false-positive checks and bounded re-verification.
- Strengthened numeric layout and task-oriented error/empty-state copy.

Instructions were authored for this repository from these transferable concepts. No third-party implementation, database, command set, text translation or bundled Skill was incorporated. The runtime remains instruction-only; each upstream retains its own ownership and license.

## Contribution assessment

A concrete candidate is prepared for Interface Design: distinguish its recommended hit area from WCAG 2.2 SC 2.5.8 (AA), SC 2.5.5 (AAA), their CSS units and exceptions. The [proposal](./upstream-contributions/README.md) includes a guarded edit script and ready-to-review PR body.

The inspected Impeccable AGENTS.md requires issue-first maintainer approval and restricts AI-created issues/PRs to explicitly authorized maintainer work. No issue, comment or PR was sent there. Its generated harness files were not treated as canonical source.

No upstream PR has been opened. The candidate is a separately prepared contribution, not an accepted upstream change. Recheck the current source, contribution policy and existing proposals before submitting.
