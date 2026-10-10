"""Reproduce original-paper crops using the inspected PDF CropBoxes.

Run with the six instructor-uploaded PDFs and two retrieved papers in papers/.
No scientific image is drawn, reconstructed or recolored.
"""
from pathlib import Path
import sys
import pymupdf as fitz
from PIL import Image
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
import crop_panels

def render(pdf, page, dpi):
    pix = fitz.open(pdf)[page - 1].get_pixmap(dpi=dpi)
    return Image.frombytes('RGB', (pix.width, pix.height), pix.samples)

crop_panels.render = render
crop_panels.main(Path(__file__).with_name('crops.json'))
