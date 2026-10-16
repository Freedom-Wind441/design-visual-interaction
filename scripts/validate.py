#!/usr/bin/env python3
"""Validate release structure; does not certify UI quality or host loading."""
import argparse
import hashlib
import json
import re
import shutil
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree
import yaml

NAME = "design-visual-interaction"
REFERENCES = {
    "project-baseline", "dock-navigation", "buttons", "typography-layout",
    "sliders-input", "settings-onboarding", "motion-feedback",
    "materials-color", "style-liquid-glass", "verification",
    "visual-composition", "platform-adaptation", "worked-examples",
}
EXPECTED = {"SKILL.md", "LICENSE", "agents/openai.yaml",
            "assets/component-anatomy.svg", "assets/task-hierarchy.svg"} | {
    f"references/{name}.md" for name in REFERENCES
}
SECTIONS = ("适用条件", "目标与约束", "依赖与联动", "实施", "验收")

class UniqueLoader(yaml.SafeLoader):
    """Reject duplicate keys instead of silently overwriting metadata."""

def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node)
    return result

UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
                             unique_mapping)

def require(condition, message):
    if not condition:
        raise ValueError(message)

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def headings(content):
    content = re.sub(r"```.*?```", "", content, flags=re.S)
    result, counts = set(), {}
    for line in content.splitlines():
        match = re.match(r"^#{1,6}\s+(.+)$", line)
        if match:
            slug = re.sub(r"[^\w\- ]", "", match[1].strip().lower()).replace(" ", "-")
            count = counts.get(slug, 0)
            counts[slug] = count + 1
            result.add(slug + (f"-{count}" if count else ""))
    return result

def check_links(path, root):
    content = re.sub(r"```.*?```", "", path.read_text(), flags=re.S)
    links = re.findall(r"\]\(([^\s)]+)\)", content)
    links += re.findall(r'(?:src|href)="([^"]+)"', content)
    for link in links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        require(target.is_relative_to(root), f"link escapes boundary: {path.name}: {link}")
        require(target.exists(), f"broken local link: {path.name}: {link}")
        if url.fragment and target.suffix == ".md":
            require(unquote(url.fragment) in headings(target.read_text()),
                    f"broken heading link: {path.name}: {link}")

def skill_fingerprints(skill):
    return {str(path.relative_to(skill)): digest(path)
            for path in sorted(skill.rglob("*")) if path.is_file()}

def validate_skill(skill):
    require(skill.name == NAME, "invalid install directory name")
    for path in skill.rglob("*"):
        require(not path.is_symlink(), f"symlink forbidden: {path}")
    actual = {str(path.relative_to(skill)) for path in skill.rglob("*") if path.is_file()}
    require(actual == EXPECTED, f"unexpected/missing Skill files: {actual ^ EXPECTED}")
    entry = (skill / "SKILL.md").read_text()
    match = re.match(r"\A---\n(.*?)\n---\n", entry, re.S)
    require(match is not None, "missing frontmatter")
    metadata = yaml.load(match[1], Loader=UniqueLoader)
    require(isinstance(metadata, dict) and set(metadata) == {"name", "description"},
            "unexpected frontmatter fields")
    require(metadata["name"] == NAME and len(NAME) <= 64, "invalid metadata name")
    description = metadata["description"]
    require(isinstance(description, str) and 1 <= len(description) <= 1024,
            "invalid description")
    require(len(entry.splitlines()) < 160, "entrypoint grew beyond release budget")
    for name in REFERENCES:
        require(f"(references/{name}.md)" in entry, f"unreachable module: {name}")
        content = (skill / f"references/{name}.md").read_text()
        for section in SECTIONS:
            require(f"## {section}" in content, f"missing module section: {name}/{section}")
        require(len(content.splitlines()) <= 100, f"module grew beyond release budget: {name}")
    ui = yaml.load((skill / "agents/openai.yaml").read_text(), Loader=UniqueLoader)
    require(isinstance(ui, dict) and set(ui) == {"interface"}, "unexpected UI fields")
    interface = ui["interface"]
    require(set(interface) == {"display_name", "short_description", "default_prompt"},
            "unexpected interface fields")
    require(all(isinstance(value, str) and value for value in interface.values()),
            "invalid UI strings")
    require(interface["display_name"] == "Visual & Interaction Design", "display name drift")
    require(25 <= len(interface["short_description"]) <= 64, "UI blurb length")
    require(f"$"+"design-visual-interaction" in interface["default_prompt"], "missing invocation")
    for asset in sorted((skill / "assets").glob("*.svg")):
        require(ElementTree.parse(asset).getroot().tag ==
                "{http://www.w3.org/2000/svg}svg", f"invalid SVG: {asset.name}")
    forbidden = {
        "machine path": r"/(?:root|workspace|Users|home)/|[A-Za-z]:\\(?:Users|Windows)\\",
        "email": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        "credential": r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{20,}",
        "private project": r"GPT-Quota-Glass|OnePlus|ColorOS|PLK110",
        "placeholder": r"\bTODO\b|\bFIXME\b",
    }
    for relative in EXPECTED:
        path = skill / relative
        content = path.read_text(encoding="utf-8")
        for kind, pattern in forbidden.items():
            require(not re.search(pattern, content), f"potential {kind}: {relative}")
        if path.suffix == ".md":
            check_links(path, skill.resolve())
    return skill_fingerprints(skill)

def validate(root, write_manifest=False):
    root = root.resolve()
    skill = root / "skills" / NAME
    fingerprints = validate_skill(skill)
    require({p.name for p in (root / "skills").iterdir()} == {NAME},
            "do not bundle companion skills")
    require((root / "LICENSE").read_bytes() == (skill / "LICENSE").read_bytes(),
            "license copies differ")
    require("Copyright (c) 2026 Freedom-Wind441" in (root / "LICENSE").read_text(),
            "license attribution")
    version = (root / "VERSION").read_text().strip()
    require(re.fullmatch(r"\d+\.\d+\.\d+", version), "invalid version")
    for suffix in ("", ".zh-CN"):
        readme = (root / f"README{suffix}.md").read_text()
        other = "README.md" if suffix else "README.zh-CN.md"
        require(f"(./{other})" in readme, "missing language switch")
        require(f"version-{version}-" in readme, "README version mismatch")
        require(f"## {version} — " in (root / f"CHANGELOG{suffix}.md").read_text(),
                "changelog version mismatch")
        require((root / f"VALIDATION{suffix}.md").is_file(), "missing validation record")
    manifest_path = root / "docs/skill-manifest.json"
    manifest = {"version": version, "sha256": fingerprints}
    if write_manifest:
        manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    require(json.loads(manifest_path.read_text()) == manifest, "manifest mismatch")
    for path in root.rglob("*.md"):
        if ".git" not in path.parts:
            require(not path.is_symlink(), f"symlink forbidden: {path}")
            check_links(path, root)
    with tempfile.TemporaryDirectory() as temporary:
        destination = Path(temporary) / ".agents/skills" / NAME
        shutil.copytree(skill, destination)
        require(validate_skill(destination) == fingerprints, "installation copy differs")
    print(f"PASS: v{version}; {len(fingerprints)} Skill files; metadata, modules, local links,")
    print("SVG, licenses, versions, scoped privacy patterns, fingerprints and clean layout.")
    print("Static checks only; no UI quality or universal host-compatibility claim.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write-manifest", action="store_true",
                        help="Refresh fingerprints after reviewing intentional Skill changes")
    args = parser.parse_args()
    try:
        validate(args.root, args.write_manifest)
    except (ValueError, OSError, TypeError, KeyError, yaml.YAMLError) as error:
        parser.exit(1, f"FAIL: {error}\n")
