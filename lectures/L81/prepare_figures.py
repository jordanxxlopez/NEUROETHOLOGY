"""Reproduce intact article crops from the reviewed, saved crop manifest."""
from pathlib import Path
import subprocess
B=Path(__file__).resolve().parent
subprocess.run(['python','tools/crop_panels.py',str(B/'crops.json')],check=True,cwd=B.parents[1])
