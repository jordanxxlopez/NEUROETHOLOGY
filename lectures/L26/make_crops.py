"""Extract the recorded, unmodified published panels using the repository tool."""
from pathlib import Path
import subprocess,sys
here=Path(__file__).resolve().parent
subprocess.run([sys.executable,str(here.parents[1]/"tools/crop_panels.py"),str(here/"crops.json")],check=True)
