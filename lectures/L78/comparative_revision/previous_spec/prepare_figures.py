"""Reproduce original article crops and retrieve the unchanged atlas image."""
from pathlib import Path
import subprocess,sys,json,urllib.request,hashlib
b=Path(__file__).resolve().parent
subprocess.run([sys.executable,str(b.parents[1]/"tools/crop_panels.py"),str(b/"crops.json")],check=True)
m=json.loads((b/"web_images.json").read_text())["accumbens_atlas"]
p=b/"figures/accumbens_atlas.jpg"
if not p.exists():
 data=urllib.request.urlopen(m["image_url"],timeout=30).read()
 if hashlib.sha256(data).hexdigest()!=m["sha256"]:raise RuntimeError("Atlas image changed; inspect and verify the source before using it")
 p.write_bytes(data)
