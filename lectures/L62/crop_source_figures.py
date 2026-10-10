"""Repository batch crops, using its PyMuPDF fallback for CropBox coordinates."""
from pathlib import Path
import runpy,sys,shutil
R=Path(__file__).resolve().parents[2]
original=shutil.which
shutil.which=lambda name,*a,**kw:None if name=='pdftoppm' else original(name,*a,**kw)
sys.argv=['crop_panels.py',str(Path(__file__).with_name('crops.json'))]
runpy.run_path(str(R/'tools/crop_panels.py'),run_name='__main__')
