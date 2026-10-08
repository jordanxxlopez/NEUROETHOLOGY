#!/usr/bin/env python3
"""Crop Lecture 5 figure panels from the original article figures.

Sources live in lectures/L5/papers/ (not committed): PMC open-access figure files,
publisher full-resolution figure files (papers/hi/), images embedded in the article
PDFs (papers/<paper>/emb/), or PDF pages rendered with pdftoppm. Boxes are
fractions of the source image (left, top, right, bottom). Nothing is redrawn.
"""
import subprocess, tempfile
from pathlib import Path
from PIL import Image, ImageChops

HERE = Path(__file__).resolve().parent
P = HERE / "papers"
OUT = HERE / "figures"

def page(pdf, n, dpi=400):
    tmp = Path(tempfile.mkdtemp())
    subprocess.run(["pdftoppm", "-png", "-r", str(dpi), "-f", str(n), "-l", str(n), "-singlefile", str(pdf), str(tmp / "p")], check=True)
    return tmp / "p.png"

HECKER = P / "Hecker2020/PMC7022180.1.pdf"
CROPS = {
    "f01a_schuster_f2a": ("Schuster2023/359_2023_1658_Fig2_HTML.jpg", (0, 0, 1, 0.165)),
    "f01b_burgess_f1b": ("Burgess2007/zns0180732290001.jpg", (0, 0.47, 1, 1)),
    "f02_burgess_f1a": ("Burgess2007/zns0180732290001.jpg", (0, 0, 1, 0.455)),
    "f03_preuss_f1a": ("Preuss2006/zns0120615280001.jpg", (0, 0, 0.42, 0.53)),
    "f04_koyama_f9a": ("hi/Koyama2016_fig9.jpg", (0, 0, 1, 0.275)),
    "f05_koyama_f10ab": ("hi/Koyama2016_fig10.jpg", (0, 0, 1, 0.37)),
    "f06_marquart_f1b": ("Marquart2019/emb/i-003.jpg", (0.548, 0, 1, 0.56)),
    "f07a_marquart_f1cd": ("Marquart2019/emb/i-003.jpg", (0, 0.562, 1, 1)),
    "f07b_burgess_f3a": ("Burgess2007/zns0180732290003.jpg", (0, 0, 0.468, 0.445)),
    "f08_burgess_f4": ("Burgess2007/zns0180732290004.jpg", (0, 0, 0.6, 1)),
    "f09_koyama_f1b": ("hi/Koyama2016_fig1.jpg", (0, 0.185, 0.5, 0.52)),
    "f10a_schuster_f6b": ("Schuster2023/359_2023_1658_Fig6_HTML.jpg", (0, 0.365, 1, 0.615)),
    "f10b_preuss_f8a": ("Preuss2006/zns0120615280008.jpg", (0, 0, 0.47, 0.31)),
    "f11_miller_f4ab": ("hi/Miller2017_fig4.jpg", (0, 0, 0.69, 0.33)),
    "f12_watanabe_f3b": ("hi/Watanabe_F3.jpg", (0, 0.635, 1, 1)),
    "f13_echeverry_f1": ("hi/Echeverry_F1.jpg", (0, 0, 1, 0.55)),
    "f14_echeverry_f4": ("hi/Echeverry_F4.jpg", (0, 0, 0.455, 1)),
    "f15_echeverry_f6": ("hi/Echeverry_F6.jpg", (0, 0, 1, 0.47)),
    "f16_echeverry_f5": ("hi/Echeverry_F5.jpg", (0, 0, 1, 1)),
    "f17_miller_f6": ("hi/Miller2017_fig6.jpg", (0, 0, 0.48, 0.72)),
    "f18_lasseigne_f1": ("hi/Lasseigne2021_fig1.jpg", (0, 0.28, 1, 0.62)),
    "f19_lasseigne_f3": ("hi/Lasseigne2021_fig3.jpg", (0, 0, 1, 0.68)),
    "f20_lasseigne_f5": ("hi/Lasseigne2021_fig5.jpg", (0, 0, 1, 0.503)),
    "f21_marsden_f4": ("Marsden2018/emb/i-005.jpg", (0, 0, 1, 0.37)),
    "f22_batora_f2": ("Batora2021/emb/i-001.png", (0, 0, 1, 0.54)),
    "f23_hecker_f2": (("page", HECKER, 2), (0.49, 0.31, 0.925, 0.745)),
    "f24_weissfaber_f3": ("WeissFaber2010/fncir-04-00015-g003.jpg", (0, 0, 1, 1)),
    "f25_otero_f3a": ("hi/OteroCoronel2024_fig3.jpg", (0, 0, 1, 0.3)),
    "f26_koyama_f1c": ("hi/Koyama2016_fig1.jpg", (0.5, 0.185, 1, 1)),
    "f27_schuster_f3": ("Schuster2023/359_2023_1658_Fig3_HTML.jpg", (0, 0, 1, 1)),
    "f28_koyama_f10c": ("hi/Koyama2016_fig10.jpg", (0, 0.37, 1, 1)),
    "f29_miller_f3ac": ("hi/Miller2017_fig3.jpg", (0, 0, 0.73, 0.33)),
    "f30_watanabe_f1": ("hi/Watanabe_F1.jpg", (0, 0, 1, 1)),
    "f31_watanabe_f2": ("hi/Watanabe_F2.jpg", (0, 0, 1, 1)),
    "f32_watanabe_f4": ("hi/Watanabe_F4.jpg", (0, 0, 1, 0.5)),
    "f33_hecker_f1": (("page", HECKER, 2), (0.06, 0.06, 0.48, 0.503)),
    "f34_hecker_f3": (("page", HECKER, 3), (0.22, 0.535, 0.82, 0.815)),
    "f35_hecker_f4": (("page", HECKER, 4), (0.49, 0.06, 0.94, 0.455)),
    "f36_preuss_f5": ("Preuss2006/zns0120615280005.jpg", (0, 0, 1, 1)),
    "f37_martorell_f4": ("hi/Martorell_Fig4.png", (0, 0, 1, 0.255)),
    "f38_otero_f2": ("hi/OteroCoronel2024_fig2.jpg", (0, 0, 1, 0.18)),
    "f39_marquart_f2": ("Marquart2019/emb/i-005.jpg", (0, 0.62, 1, 1)),
    "f40_marquart_f7": ("Marquart2019/emb/i-015.jpg", (0, 0, 1, 1)),
    "f41_marsden_f5": ("Marsden2018/emb/i-006.jpg", (0, 0, 1, 0.6)),
    "f42_batora_f4": ("Batora2021/emb/i-003.png", (0.5, 0, 1, 0.555)),
    "f43_burgess_f5": ("Burgess2007/zns0180732290005.jpg", (0, 0, 0.285, 0.302)),
    "f44_bronson_f3": ("BronsonPreuss2017/emb/i-002.jpg", (0, 0, 1, 0.48)),
}

def trim(im, pad=6):
    bg = Image.new("RGB", im.size, (255, 255, 255))
    diff = ImageChops.difference(im, bg).convert("L").point(lambda v: 255 if v > 18 else 0)
    box = diff.getbbox()
    if not box:
        return im
    l, t, r, b = box
    return im.crop((max(l - pad, 0), max(t - pad, 0), min(r + pad, im.width), min(b + pad, im.height)))

def main(names=None):
    OUT.mkdir(exist_ok=True)
    cache = {}
    for name, (src, (l, t, r, b)) in CROPS.items():
        if names and name not in names:
            continue
        if isinstance(src, tuple):
            key = src[1:]
            if key not in cache:
                cache[key] = page(src[1], src[2])
            path = cache[key]
        else:
            path = P / src
        im = Image.open(path).convert("RGB")
        W, H = im.size
        c = trim(im.crop((round(l * W), round(t * H), round(r * W), round(b * H))))
        c.save(OUT / f"{name}.png")
        print(f"{name}: {c.size[0]}x{c.size[1]}")

if __name__ == "__main__":
    import sys
    main(sys.argv[1:] or None)
