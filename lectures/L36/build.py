from pathlib import Path
import subprocess,sys
H=Path(__file__).resolve().parent;ROOT=H.parents[1]
for script,args in [(H/'write_spec.py',[]),(ROOT/'tools/build_lecture.py',[str(H/'lecture.json')]),(H/'finalize.py',[]),(ROOT/'tools/check_lecture.py',[str(H/'Neuroethology_Lecture36_FA2026.pptx'),'--lecture','36'])]:subprocess.run([sys.executable,str(script),*args],cwd=ROOT,check=True)
