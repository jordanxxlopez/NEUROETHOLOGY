"""Use the repository cropper's PyMuPDF fallback for PDFs with CropBoxes."""
import runpy,shutil,sys
from pathlib import Path
D=Path(__file__).resolve().parent;root=D.parents[1]
original=shutil.which
shutil.which=lambda name,*a,**k: None if name=='pdftoppm' else original(name,*a,**k)
sys.argv=[str(root/'tools/crop_panels.py'),str(D/'crops.json')]
runpy.run_path(str(root/'tools/crop_panels.py'),run_name='__main__')
