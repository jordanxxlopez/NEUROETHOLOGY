#!/usr/bin/env python3
"""Cut a figure panel out of a paper's PDF page.

    # 1. render a page to look at it
    python tools/crop_figure.py paper.pdf 4 --preview lectures/L11/figures/p4.png
    # 2. crop a panel by fractions of the page (left top right bottom, 0-1)
    python tools/crop_figure.py paper.pdf 4 --box 0.08 0.12 0.52 0.48 -o lectures/L11/figures/fig2a.png

Keep axes, units, scale bars and panel letters inside the crop.
Needs pdftoppm (poppler) and Pillow.
"""
import argparse
import subprocess
import tempfile
from pathlib import Path

from PIL import Image


def render(pdf, page, dpi):
    tmp = Path(tempfile.mkdtemp())
    subprocess.run(["pdftoppm", "-png", "-r", str(dpi), "-f", str(page), "-l", str(page),
                    "-singlefile", str(pdf), str(tmp / "page")], check=True)
    return Image.open(tmp / "page.png")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("page", type=int)
    ap.add_argument("--dpi", type=int, default=250)
    ap.add_argument("--preview")
    ap.add_argument("--box", type=float, nargs=4, metavar=("L", "T", "R", "B"))
    ap.add_argument("-o", "--out")
    a = ap.parse_args()
    im = render(a.pdf, a.page, a.dpi)
    if a.preview:
        im.save(a.preview)
        print(f"page {a.page}: {im.size[0]}x{im.size[1]} px -> {a.preview}")
    if a.box:
        w, h = im.size
        l, t, r, b = a.box
        crop = im.crop((int(l * w), int(t * h), int(r * w), int(b * h)))
        crop.save(a.out)
        print(f"cropped {crop.size[0]}x{crop.size[1]} px -> {a.out}")


if __name__ == "__main__":
    main()
