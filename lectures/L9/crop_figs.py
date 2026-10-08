#!/usr/bin/env python3
"""Crop Lecture 9 figure panels from original article figures (nothing is redrawn).

Sources in lectures/L9/papers/ (not committed): instructor-uploaded PDFs (Ewert 1978, 1979,
1997, 2001; Schürg-Pfeiffer & Ewert 1981) rendered with pdftoppm, PMC open-access figure files,
and eLife full-resolution figures (papers/hi/). Boxes are fractions (left, top, right, bottom).
"""
import subprocess, sys, tempfile
from pathlib import Path
from PIL import Image, ImageChops

HERE = Path(__file__).resolve().parent
P, OUT = HERE / "papers", HERE / "figures"
E01, T97, E79, E78, SP = (P / f for f in ("Ewert2001_CBP.pdf", "Ewert1997_TINS.pdf", "Ewert1979_BBE.pdf",
                                         "Ewert1978.pdf", "SchurgPfeiffer1981.pdf"))
CROPS = {
    "e01_f2a": ((E01, 3), (0.08, 0.14, 0.42, 0.395)),
    "e01_f2bc": ((E01, 3), (0.08, 0.40, 0.42, 0.680)),
    "e01_f2d": ((E01, 3), (0.08, 0.680, 0.42, 0.835)),
    "e01_f3": ((E01, 5), (0.18, 0.23, 0.83, 0.795)),
    "e01_f4": ((E01, 8), (0.13, 0.11, 0.48, 0.585)),
    "e01_f5": ((E01, 9), (0.18, 0.17, 0.86, 0.64)),
    "e01_f6": ((E01, 10), (0.555, 0.065, 0.93, 0.28)),
    "e01_f7": ((E01, 11), (0.565, 0.06, 0.80, 0.785)),
    "e01_f9": ((E01, 15), (0.505, 0.07, 0.87, 0.265)),
    "e01_f10": ((E01, 16), (0.13, 0.14, 0.48, 0.835)),
    "e01_f12": ((E01, 18), (0.18, 0.18, 0.47, 0.82)),
    "e01_f13": ((E01, 19), (0.09, 0.06, 0.48, 0.54)),
    "e01_f14": ((E01, 19), (0.52, 0.06, 0.88, 0.385)),
    "e01_f16": ((E01, 22), (0.53, 0.08, 0.90, 0.48)),
    "e01_f18": ((E01, 26), (0.18, 0.55, 0.84, 0.785)),
    "e01_f22": ((E01, 33), (0.50, 0.07, 0.865, 0.445)),
    "t97_tab1": ((T97, 2), (0.455, 0.21, 0.81, 0.66)),
    "t97_f1a": ((T97, 3), (0.17, 0.20, 0.54, 0.318)),
    "t97_f1bc": ((T97, 3), (0.17, 0.322, 0.54, 0.53)),
    "t97_f1b": ((T97, 3), (0.17, 0.322, 0.54, 0.432)),
    "t97_f1c": ((T97, 3), (0.17, 0.432, 0.54, 0.53)),
    "t97_f2a": ((T97, 4), (0.45, 0.20, 0.82, 0.335)),
    "t97_f2ab": ((T97, 4), (0.45, 0.20, 0.82, 0.512)),
    "t97_f2b": ((T97, 4), (0.45, 0.34, 0.82, 0.512)),
    "t97_f3": ((T97, 5), (0.18, 0.20, 0.54, 0.545)),
    "t97_f4": ((T97, 6), (0.18, 0.20, 0.447, 0.565)),
    "t97_f5": ((T97, 6), (0.45, 0.20, 0.815, 0.335)),
    "e79_f1": ((E79, 3), (0.10, 0.10, 0.93, 0.68)),
    "e79_f2": ((E79, 5), (0.18, 0.08, 0.58, 0.47)),
    "e79_f3": ((E79, 7), (0.18, 0.08, 0.62, 0.625)),
    "e79_f4": ((E79, 9), (0.12, 0.088, 0.62, 0.545)),
    "e79_f6": ((E79, 11), (0.08, 0.075, 0.92, 0.38)),
    "e78_f1": ((E78, 3), (0.08, 0.10, 0.49, 0.445)),
    "e78_f2": ((E78, 3), (0.52, 0.10, 0.95, 0.445)),
    "sp_f8": ((SP, 8), (0.08, 0.08, 0.48, 0.51)),
    "sp_f11": ((SP, 11), (0.08, 0.08, 0.92, 0.345)),
    "sp_f12": ((SP, 11), (0.08, 0.385, 0.33, 0.555)),
    "xromm_f8": ("XROMM2022/obac045fig8.jpg", (0, 0, 1, 1)),
    "yov_f2": ("Yovanovich2017/rstb20160066-g2.jpg", (0, 0, 1, 1)),
    "flaive_f8": ("FlaiveRyczko2022/CNE-530-2518-g008.jpg", (0, 0, 1, 1)),
    "flaive_f7": ("FlaiveRyczko2022/CNE-530-2518-g007.jpg", (0, 0, 1, 1)),
    "bianco11_f2": ("Bianco2011/fnsys-05-00101-g002.jpg", (0, 0, 1, 0.74)),
    "forster_f3c": ("hi/Forster_fig3.jpg", (0.555, 0.505, 1, 1)),
    "semm_f1": ("hi/Semmelhack_fig1.jpg", (0, 0, 1, 0.22)),
    "semm_f2": ("hi/Semmelhack_fig2.jpg", (0, 0, 1, 1)),
    "semm_f3": ("hi/Semmelhack_fig3.jpg", (0, 0, 1, 0.72)),
    "semm_f6": ("hi/Semmelhack_fig6.jpg", (0, 0, 1, 1)),
    "be15_f1": ("BiancoEngert2015/gr1.jpg", (0, 0, 1, 1)),
    "be15_f5": ("BiancoEngert2015/gr5.jpg", (0, 0, 0.66, 0.23)),
    "antin_f2": ("hi/Antinucci_fig2.jpg", (0, 0, 1, 0.33)),
    "antin_f5": ("hi/Antinucci_fig5.jpg", (0, 0, 1, 0.33)),
    "forster_f6": ("hi/Forster_fig6.jpg", (0, 0, 1, 1)),
    "muto_f2": ("Muto2017/ncomms15029-f2.jpg", (0, 0, 1, 0.5)),
    "henriques_f2": ("Henriques2019/gr2.jpg", (0, 0, 1, 1)),
}

def render(pdf, n, cache={}):
    if (pdf, n) not in cache:
        tmp = Path(tempfile.mkdtemp())
        subprocess.run(["pdftoppm", "-png", "-r", "300", "-f", str(n), "-l", str(n), "-singlefile", str(pdf), str(tmp / "p")], check=True)
        cache[(pdf, n)] = tmp / "p.png"
    return cache[(pdf, n)]

def trim(im, pad=8):
    diff = ImageChops.difference(im, Image.new("RGB", im.size, (255, 255, 255))).convert("L").point(lambda v: 255 if v > 30 else 0)
    b = diff.getbbox()
    if not b:
        return im
    return im.crop((max(b[0] - pad, 0), max(b[1] - pad, 0), min(b[2] + pad, im.width), min(b[3] + pad, im.height)))

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for name, (src, (l, t, r, b)) in CROPS.items():
        if sys.argv[1:] and name not in sys.argv[1:]:
            continue
        im = Image.open(render(*src) if isinstance(src, tuple) else P / src).convert("RGB")
        W, H = im.size
        c = trim(im.crop((round(l * W), round(t * H), round(r * W), round(b * H))))
        c.save(OUT / f"{name}.png")
        print(f"{name}: {c.size[0]}x{c.size[1]}")
