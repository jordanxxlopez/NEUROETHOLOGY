from pathlib import Path
import subprocess,sys
HERE=Path(__file__).resolve().parent
subprocess.run([sys.executable,str(HERE.parents[1]/"tools/build_lecture.py"),str(HERE/"lecture.json")],check=True)
