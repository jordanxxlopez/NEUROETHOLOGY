"""Reproduce unmodified article crops from the ignored, instructor-supplied PDFs."""
from pathlib import Path
import json, subprocess, sys
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
for crop in json.loads((HERE/'crops.json').read_text()):
    pdf=HERE/'papers'/Path(crop['pdf']).name
    output=HERE/'figures'/Path(crop['out']).name
    subprocess.run([sys.executable,str(ROOT/'tools/crop_figure.py'),str(pdf),str(crop['page']),
                    '--dpi','180','--box',*map(str,crop['box']),'-o',str(output)],check=True)
