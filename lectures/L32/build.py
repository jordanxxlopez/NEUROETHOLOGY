"""Build with repository tools, then preserve exact title and Arial notes."""
import subprocess,sys
from pathlib import Path
H=Path(__file__).resolve().parent;ROOT=H.parents[1]
for args in [[str(H/"write_spec.py")],[str(ROOT/"tools/build_lecture.py"),str(H/"lecture.json")],[str(H/"finalize.py")],[str(ROOT/"tools/check_lecture.py"),str(H/"Neuroethology_Lecture32_FA2026.pptx"),"--lecture","32"]]:
 subprocess.run([sys.executable,*args],check=True,cwd=ROOT)
