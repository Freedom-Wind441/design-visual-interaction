"""Negative release-contract tests; never mutate the source Skill."""
import importlib.util
import tempfile
import unittest
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validator", ROOT / "scripts/validate.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)

class ReleaseContractTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.skill = Path(self.temporary.name) / validator.NAME
        shutil.copytree(ROOT / "skills" / validator.NAME, self.skill)

    def test_valid_standalone_copy(self):
        self.assertEqual(len(validator.validate_skill(self.skill)), 18)

    def test_duplicate_metadata_rejected(self):
        path = self.skill / "SKILL.md"
        path.write_text(path.read_text().replace(
            "name: design-visual-interaction",
            "name: design-visual-interaction\nname: duplicate"))
        with self.assertRaisesRegex(ValueError, "duplicate YAML key"):
            validator.validate_skill(self.skill)

    def test_missing_module_rejected(self):
        (self.skill / "references/buttons.md").unlink()
        with self.assertRaisesRegex(ValueError, "unexpected/missing"):
            validator.validate_skill(self.skill)

    def test_escaping_reference_rejected(self):
        path = self.skill / "SKILL.md"
        path.write_text(path.read_text() + "\n[escape](../outside.md)\n")
        with self.assertRaisesRegex(ValueError, "escapes boundary"):
            validator.validate_skill(self.skill)

    def test_machine_path_rejected(self):
        path = self.skill / "references/buttons.md"
        path.write_text(path.read_text() + "\n/root/private-project\n")
        with self.assertRaisesRegex(ValueError, "machine path"):
            validator.validate_skill(self.skill)

    def test_symlink_rejected(self):
        path = self.skill / "references/buttons.md"
        path.unlink()
        path.symlink_to(self.skill / "references/project-baseline.md")
        with self.assertRaisesRegex(ValueError, "symlink forbidden"):
            validator.validate_skill(self.skill)

    def test_manifest_drift_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            copy = Path(temporary) / "repo"
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            path = copy / "skills" / validator.NAME / "references/buttons.md"
            path.write_text(path.read_text() + "\nAn intentional but unfingerprinted change.\n")
            with self.assertRaisesRegex(ValueError, "manifest mismatch"):
                validator.validate(copy)

if __name__ == "__main__":
    unittest.main()
