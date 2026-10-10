"""Render PDF CropBox coordinates and crop original article panels."""
from pathlib import Path
import sys
import pymupdf
from PIL import Image
D=Path(__file__).resolve().parent;sys.path.insert(0,str(D.parents[1]/'tools'))
import crop_panels

def render(pdf,page,dpi):
 with pymupdf.open(pdf) as doc:
  p=doc[page-1].get_pixmap(matrix=pymupdf.Matrix(dpi/72,dpi/72),alpha=False)
  return Image.frombytes('RGB',(p.width,p.height),p.samples)
crop_panels.render=render
crop_panels.main(str(D/'crops.json'))
