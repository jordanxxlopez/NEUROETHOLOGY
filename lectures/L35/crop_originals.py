"""Run the repository crop tool using its PyMuPDF backend (PDF CropBox coordinates)."""
import runpy,sys,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
# PDF CropBox must match the pages inspected before selecting normalized bounds.
# Poppler's default MediaBox includes publisher margins in some uploaded PDFs.
original_which=shutil.which
shutil.which=lambda name: None if name=='pdftoppm' else original_which(name)
sys.argv=[str(ROOT/'tools/crop_panels.py'),str(Path(__file__).with_name('crops.json'))]
runpy.run_path(str(ROOT/'tools/crop_panels.py'),run_name='__main__')
