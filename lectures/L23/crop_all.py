"""Reproduce only original PDF crops with the course crop tool."""
import json, subprocess, sys
from pathlib import Path
H=Path(__file__).resolve().parent
for manifest in ['crops.json','extra-crops.json']:
 for x in json.loads((H/manifest).read_text()):
  subprocess.run([sys.executable,str(H.parents[1]/'tools/crop_figure.py'),str(H/x['pdf']),str(x['page']),'--dpi',str(x['dpi']),'--box',*map(str,x['box']),'-o',str(H/x['out'])],check=True)
