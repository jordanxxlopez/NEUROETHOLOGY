"""Use the repository cropper with PDF CropBox coordinates (PyMuPDF)."""
import runpy,shutil,sys
from pathlib import Path
D=Path(__file__).resolve().parent;R=D.parents[1]
which=shutil.which
shutil.which=lambda n,*a,**kw: None if n=='pdftoppm' else which(n,*a,**kw)
sys.argv=['crop_panels.py',str(D/'crops.json')]
runpy.run_path(str(R/'tools/crop_panels.py'),run_name='__main__')
