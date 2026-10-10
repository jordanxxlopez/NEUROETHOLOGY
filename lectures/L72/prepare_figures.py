"""Crop the original, unmodified article panels using inspected PDF coordinates."""
import sys
from pathlib import Path
D=Path(__file__).resolve().parent
sys.path.insert(0,str(D.parents[1]/'tools'))
import crop_panels,crop_figure
# Use the PDF CropBox, matching the inspected source renders.
crop_figure.shutil.which=lambda _:None
crop_panels.main(D/'crops.json')
