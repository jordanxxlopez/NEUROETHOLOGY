"""Run the authoritative repository builder, then format Lecture 35 speaker notes."""
from pathlib import Path
import subprocess,sys
b=Path(__file__).resolve().parent
subprocess.run([sys.executable,str(b.parents[1]/'tools/build_lecture.py'),str(b/'lecture.json')],check=True)
subprocess.run([sys.executable,str(b/'finalize_notes.py')],check=True)
