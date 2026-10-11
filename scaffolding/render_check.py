#!/usr/bin/env python3
"""Render a deck with LibreOffice and flag pages where text collides, overflows or crosses the footer rule.

    python scaffolding/render_check.py scaffolded/Neuroethology_Lecture11_FA2026_V2_SCAFFOLDED.pptx [--png 5,8]

Prints one line per problem page. Exit code 1 when any page is flagged. --png saves those pages
as scratch images next to the PDF for a quick look.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

PAGE_W, PAGE_H = 960.0, 540.0
RULE_Y = 6382512 / 12700            # footer rule, in points
WORD = re.compile(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>')


def overlap(a, b):
    w = min(a[2], b[2]) - max(a[0], b[0])
    h = min(a[3], b[3]) - max(a[1], b[1])
    if w <= 1 or h <= 1:
        return 0.0
    small = min((a[2] - a[0]) * (a[3] - a[1]), (b[2] - b[0]) * (b[3] - b[1]))
    return w * h / small if small else 0.0


def main():
    deck = Path(sys.argv[1]).resolve()
    keep = [int(x) for x in sys.argv[sys.argv.index("--png") + 1].split(",")] if "--png" in sys.argv else []
    work = Path(tempfile.mkdtemp(prefix="render_check_"))
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(work), str(deck)],
                   check=True, capture_output=True, timeout=600)
    pdf = work / (deck.stem + ".pdf")
    html = subprocess.run(["pdftotext", "-bbox", str(pdf), "-"], check=True, capture_output=True, text=True).stdout
    bad = 0
    for page_no, page in enumerate(html.split("<page ")[1:], 1):
        words = [(float(a), float(b), float(c), float(d), t) for a, b, c, d, t in WORD.findall(page)]
        issues = []
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if overlap(words[i][:4], words[j][:4]) > 0.12:
                    issues.append(f"text collides: {words[i][4]!r} / {words[j][4]!r}")
                    break
            if len(issues) >= 2:
                break
        body = [w for w in words if w[1] < RULE_Y - 4]
        if any(w[3] > RULE_Y + 1 for w in body):
            issues.append("body text runs past the footer rule")
        if any(w[3] > PAGE_H - 4 for w in words):
            issues.append("text runs off the slide")
        if issues:
            bad += 1
            print(f"page {page_no}: " + "; ".join(issues[:3]))
    print(f"{deck.name}: {bad} problem page(s)")
    if keep:
        for p in keep:
            subprocess.run(["pdftoppm", "-r", "60", "-f", str(p), "-l", str(p), "-png", str(pdf), str(work / "pg")], check=True)
        print("images in", work)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
