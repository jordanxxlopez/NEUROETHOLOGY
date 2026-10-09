"""Build Lecture 40 with repository tools and format its teaching notes."""
from pathlib import Path
import subprocess
import sys

base = Path(__file__).resolve().parent
root = base.parents[1]
for command in (
    [sys.executable, str(base / "write_spec.py")],
    [sys.executable, str(root / "tools/build_lecture.py"), str(base / "lecture.json")],
    [sys.executable, str(base / "finalize_notes.py")],
    [sys.executable, str(root / "tools/check_lecture.py"),
     str(base / "Neuroethology_Lecture40_FA2026.pptx"), "--lecture", "40"],
):
    subprocess.run(command, check=True)
