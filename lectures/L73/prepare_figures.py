"""Reproduce original article crops from the local source PDFs."""
from pathlib import Path
import subprocess
import sys
base = Path(__file__).resolve().parent
subprocess.run([sys.executable, str(base.parents[1] / "tools/crop_panels.py"), str(base / "crops.json")], check=True)
