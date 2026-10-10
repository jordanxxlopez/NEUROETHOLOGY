"""Reproduce the current comparative deck from unchanged published PDF panels."""
from pathlib import Path
import subprocess,sys,json,tempfile
b=Path(__file__).resolve().parent
s=json.loads((b/"lecture.json").read_text());c=json.loads((b/"crops.json").read_text())
used={Path(f["path"]).stem for z in s["slides"] for f in z.get("figures",[z.get("figure")])}
used.add(Path(s["title_image"]["path"]).stem)
c["crops"]={n:v for n,v in c["crops"].items() if n in used};c.pop("combos",None)
p=b/"crops_build.json"
try:
 p.write_text(json.dumps(c,indent=2)+"\n")
 subprocess.run([sys.executable,str(b.parents[1]/"tools/crop_panels.py"),str(p)],check=True)
finally:
 p.unlink(missing_ok=True)
