from pathlib import Path
import sys
import pymupdf
from PIL import Image
R=Path(__file__).resolve().parents[2]
D=Path(__file__).resolve().parent
p=D/"crops.json"
sys.path.insert(0,str(R/'tools'));import crop_panels
def render(path,page,dpi):
 d=pymupdf.open(path);pm=d[page-1].get_pixmap(matrix=pymupdf.Matrix(dpi/72,dpi/72));return Image.frombytes('RGB',[pm.width,pm.height],pm.samples)
crop_panels.render=render;crop_panels.main(p)
