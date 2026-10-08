"""Rebuild Lecture 17 from verified source crops and the repository builder."""
import subprocess,sys
from pathlib import Path
base=Path(__file__).resolve().parent;root=base.parents[1]
for cmd in [[sys.executable,str(base/'write_spec.py')],[sys.executable,str(root/'tools/build_lecture.py'),str(base/'lecture.json')],[sys.executable,str(base/'finalize_notes.py')],[sys.executable,str(root/'tools/check_lecture.py'),str(base/'Neuroethology_Lecture17_FA2026.pptx'),'--lecture','17']]:subprocess.run(cmd,cwd=root,check=True)
