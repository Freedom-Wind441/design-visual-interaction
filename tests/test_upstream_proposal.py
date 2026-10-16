"""Exercise the guarded proposal on synthetic text, without bundling upstream."""
import hashlib
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "proposal", ROOT / "docs/upstream-contributions/apply-interface-target-size.py")
proposal = importlib.util.module_from_spec(spec)
spec.loader.exec_module(proposal)


class UpstreamProposalTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.target = self.root / proposal.TARGET
        self.target.parent.mkdir(parents=True)
        self.original = f"# Synthetic fixture\n- {proposal.OLD} Preserve this example.\nNext rule.\n".encode()
        self.target.write_bytes(self.original)
        self.expected = proposal.EXPECTED_BLOB
        self.addCleanup(setattr, proposal, "EXPECTED_BLOB", self.expected)
        proposal.EXPECTED_BLOB = hashlib.sha1(
            b"blob " + str(len(self.original)).encode() + b"\0" + self.original).hexdigest()

    def test_intended_edit_preserves_other_content(self):
        proposal.apply(self.root)
        changed = self.target.read_text()
        self.assertIn("# Synthetic fixture\n", changed)
        self.assertIn(proposal.NEW + " Preserve this example.", changed)
        self.assertIn(proposal.NOTE + "\nNext rule.\n", changed)
        self.assertNotIn(proposal.OLD, changed)

    def test_drift_rejected_without_write(self):
        altered = self.original + b"changed upstream\n"
        self.target.write_bytes(altered)
        with self.assertRaisesRegex(ValueError, "Upstream changed"):
            proposal.apply(self.root)
        self.assertEqual(self.target.read_bytes(), altered)

    def test_second_application_rejected_without_write(self):
        proposal.apply(self.root)
        once = self.target.read_bytes()
        with self.assertRaisesRegex(ValueError, "Upstream changed"):
            proposal.apply(self.root)
        self.assertEqual(self.target.read_bytes(), once)


if __name__ == "__main__":
    unittest.main()
