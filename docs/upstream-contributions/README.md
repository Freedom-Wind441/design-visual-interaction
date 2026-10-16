# Upstream contribution candidate

Status: **prepared locally, not submitted**.

Target: [Dammyjay93/interface-design](https://github.com/Dammyjay93/interface-design), inspected commit `2f9be3206855bcb2d1d0af262c8bae25cba6658d`.

Change: clarify WCAG target-size levels while preserving the project's recommended larger usability target. [PR body](./interface-target-size-pr.md) and [guarded edit script](./apply-interface-target-size.py).

Run the script against a separate upstream checkout, not this repository:

```bash
python docs/upstream-contributions/apply-interface-target-size.py /path/to/interface-design-checkout
```

It checks the exact Git blob before writing and refuses a changed source. Reinspect upstream before using an outdated snapshot. The script is a repository-development artifact and is not bundled in the installable Skill.

The upstream issue/PR listings were checked for an existing target-size proposal; none appeared in the returned complete current listing on the inspection date. Check again before submission.

Submission workflow: fork → apply → inspect diff → commit to a feature branch → submit the prepared focused PR. Recheck upstream's current contribution policy first. Upstream acceptance is not guaranteed.
