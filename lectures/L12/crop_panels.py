#!/usr/bin/env python3
"""Crop original figure panels for Lecture 12 from page renders of the source PDFs.

Render pages first (220 dpi):  pdftoppm -png -r 220 <paper>.pdf <pages_dir>/<paper>
    python lectures/L12/crop_panels.py <pages_dir>
Boxes are fractions of the page: (left, top, right, bottom).
"""
import sys
from pathlib import Path
from PIL import Image, ImageChops

OUT = Path(__file__).resolve().parent / "figures"
CROPS = {
    "p_land69a_fig1": ("land69a-04", (0.10, 0.19, 0.78, 0.545)),
    "p_land69a_fig2": ("land69a-04", (0.08, 0.605, 0.92, 0.795)),
    "p_land69a_fig3": ("land69a-06", (0.12, 0.25, 0.88, 0.695)),
    "p_land69a_fig5": ("land69a-08", (0.08, 0.215, 0.96, 0.69)),
    "p_land69a_fig10": ("land69a-15", (0.06, 0.205, 0.94, 0.70)),
    "p_land69a_fig12": ("land69a-19", (0.06, 0.135, 0.94, 0.385)),
    "p_land69a_fig13": ("land69a-19", (0.06, 0.505, 0.94, 0.745)),
    "p_land69b_fig1": ("land69b-02", (0.04, 0.42, 0.96, 0.765)),
    "p_land69b_fig2": ("land69b-05", (0.06, 0.095, 0.94, 0.54)),
    "p_land69b_fig4": ("land69b-06", (0.1, 0.17, 0.94, 0.71)),
    "p_land69b_fig7": ("land69b-12", (0.04, 0.34, 0.96, 0.585)),
    "p_land69b_fig8": ("land69b-14", (0.04, 0.175, 0.96, 0.515)),
    "p_land69b_fig9": ("land69b-15", (0.12, 0.225, 0.90, 0.72)),
    "p_land69b_fig11": ("land69b-17", (0.10, 0.285, 0.96, 0.86)),
    "p_land69b_fig12": ("land69b-20", (0.04, 0.275, 0.96, 0.45)),
    "p_land69b_fig13": ("land69b-21", (0.06, 0.305, 0.94, 0.48)),
    "p_land69b_plate": ("land69b-23", (0.04, 0.07, 0.96, 0.93)),
    "p_jakob18_fig1": ("jakob18-2", (0.03, 0.10, 0.60, 0.335)),
    "p_zurek10_fig2": ("zurek10-4", (0.02, 0.03, 0.51, 0.37)),
    "p_zurek10_fig3": ("zurek10-4", (0.50, 0.085, 0.98, 0.26)),
    "p_zurek10_fig4": ("zurek10-5", (0.02, 0.075, 0.50, 0.77)),
    "p_menda14_fig1": ("menda14-2", (0.02, 0.055, 0.48, 0.72)),
    "p_menda14_fig2": ("menda14-3", (0.02, 0.06, 0.98, 0.385)),
    "p_menda14_fig3": ("menda14-4", (0.02, 0.055, 0.98, 0.44)),
    "p_menda14_fig4": ("menda14-5", (0.02, 0.07, 0.63, 0.635)),
}


def trim(im, pad=12):
    """Remove surrounding white margin, keep a small pad."""
    bg = Image.new(im.mode, im.size, (255, 255, 255))
    box = ImageChops.difference(im, bg).convert("L").point(lambda v: 255 if v > 25 else 0).getbbox()
    if not box:
        return im
    l, t, r, b = box
    return im.crop((max(0, l - pad), max(0, t - pad), min(im.width, r + pad), min(im.height, b + pad)))


def main(pages):
    OUT.mkdir(exist_ok=True)
    for name, (page, (l, t, r, b)) in CROPS.items():
        im = Image.open(Path(pages) / f"{page}.png").convert("RGB")
        w, h = im.size
        trim(im.crop((int(l * w), int(t * h), int(r * w), int(b * h)))).save(OUT / f"{name}.png")
        print(name)


if __name__ == "__main__":
    main(sys.argv[1])


COMBOS = {  # name: (direction, [panels])
    "c_land69a_fig12_13": ("v", ["p_land69a_fig12", "p_land69a_fig13"]),
    "c_land69b_fig2_4": ("h", ["p_land69b_fig2", "p_land69b_fig4"]),
    "c_land69b_fig1_plate": ("h", ["p_land69b_fig1", "p_land69b_plate"]),
    "c_zurek10_fig3_4": ("h", ["p_zurek10_fig3", "p_zurek10_fig4"]),
}


def combine():
    """Join panel pairs into one image (scaled to a common height or width)."""
    for name, (d, parts) in COMBOS.items():
        ims = [Image.open(OUT / f"{p}.png").convert("RGB") for p in parts]
        gap = 40
        if d == "h":
            h = max(i.height for i in ims)
            ims = [i.resize((int(i.width * h / i.height), h)) for i in ims]
            out = Image.new("RGB", (sum(i.width for i in ims) + gap, h), "white")
            out.paste(ims[0], (0, 0)); out.paste(ims[1], (ims[0].width + gap, 0))
        else:
            w = max(i.width for i in ims)
            ims = [i.resize((w, int(i.height * w / i.width))) for i in ims]
            out = Image.new("RGB", (w, sum(i.height for i in ims) + gap), "white")
            out.paste(ims[0], (0, 0)); out.paste(ims[1], (0, ims[0].height + gap))
        out.save(OUT / f"{name}.png")
        print(name)


if __name__ == "__main__":
    combine()
