#!/usr/bin/env python3
"""Apply a narrowly scoped documentation correction to the inspected upstream blob."""
import argparse
import hashlib
from pathlib import Path

TARGET = Path(".claude/skills/interface-design/SKILL.md")
EXPECTED_BLOB = "92e1df4eb5ca30923149c60f142db7ebeaaad334"
OLD = "**Hit areas — 44×44px (WCAG), 40 at minimum.**"
NEW = "**Hit areas — aim for 44×44 CSS px or larger as a usability target.**"
NOTE = (
    "- **Web target-size criteria:** WCAG 2.2 "
    "[SC 2.5.8 (AA)](https://www.w3.org/TR/WCAG22/#target-size-minimum) "
    "specifies 24×24 CSS px, with spacing and other exceptions. "
    "[SC 2.5.5 (AAA)](https://www.w3.org/TR/WCAG22/#target-size-enhanced) "
    "specifies 44×44 CSS px with its own exceptions. "
    "Do not treat a project's usability target as a universal conformance minimum; "
    "use the target platform's units and guidance for native interfaces."
)

def apply(root):
    target = root / TARGET
    original = target.read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(original)).encode("ascii") + b"\0" + original).hexdigest()
    if blob != EXPECTED_BLOB:
        raise ValueError("Upstream changed: inspect the new file before applying; no file was written.")
    text = original.decode("utf-8")
    if text.count(OLD) != 1:
        raise ValueError("Expected one source phrase; no file was written.")
    changed = text.replace(OLD, NEW)
    start = changed.index(NEW)
    end = changed.index("\n", start)
    changed = changed[:end] + "\n" + NOTE + changed[end:]
    target.write_bytes(changed.encode("utf-8"))
    return target

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkout", type=Path)
    args = parser.parse_args()
    try:
        print(apply(args.checkout))
    except (ValueError, OSError) as error:
        parser.exit(1, f"Not applied: {error}\n")
