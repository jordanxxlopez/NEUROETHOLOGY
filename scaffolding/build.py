#!/usr/bin/env python3
"""Check a scaffold spec against the house rules, build the scaffolded deck and verify it.

    python scaffolding/build.py 11 drive_updated/Neuroethology_Lecture11_FA2026_V2.pptx

Reads scaffolding/specs/L<N>.py (written by hand), writes scaffolding/specs/L<N>.json and
scaffolded/<deck name>_SCAFFOLDED.pptx. Exits 1 when any rule fails.
"""
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from pptx import Presentation  # noqa: E402

import scaffold_deck as sd  # noqa: E402
from style_rules import EM_DASH, MAX_LIMITATION_SHARE, ends_with_limitation, framing_problems, stats_problems  # noqa: E402

A_BODY_WORDS = (110, 200)       # approved scaffolded slides run 115-191 words of body text
A_NOTE_WORDS = (150, 420)       # and 178-373 words of speaker notes


def words(text):
    return len(text.split())


def flatten(items):
    out = []
    for it in items:
        out += [it] if isinstance(it, str) else list(it)
    return out


BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
TITLE_PT, TITLE_WIDTH_EMU = 22.5, 11296650 * 0.93   # approved slide titles run on one line


def title_wraps(title):
    from PIL import ImageFont
    return ImageFont.truetype(BOLD, int(TITLE_PT * 10)).getlength(title) / 10 * 12700 > TITLE_WIDTH_EMU


def text_problems(where, text):
    bad = []
    if EM_DASH in text:
        bad.append(f"{where}: em dash")
    bad += [f"{where}: {why} ({m!r})" for why, m in framing_problems(text)]
    bad += [f"{where}: statistics clutter ({m!r})" for m in stats_problems(text)]
    return bad


def main():
    n, deck = int(sys.argv[1]), Path(sys.argv[2])
    spec_py = ROOT / "scaffolding/specs" / f"L{n}.py"
    mod = importlib.util.spec_from_file_location(f"L{n}", spec_py)
    m = importlib.util.module_from_spec(mod)
    mod.loader.exec_module(m)
    spec_json = spec_py.with_suffix(".json")
    subprocess.run([sys.executable, str(spec_py)], check=True)
    out = ROOT / "scaffolded" / (deck.stem + "_SCAFFOLDED.pptx")
    out.parent.mkdir(exist_ok=True)
    subprocess.run([sys.executable, str(ROOT / "tools/scaffold_deck.py"), str(deck), str(spec_json), str(out)], check=True)

    problems = []
    src = Presentation(str(deck))
    # rewritten third paragraphs: only slides whose third paragraph really changed, no caveat left
    for num, text in m.spec["third_paragraph"].items():
        old = [p.text for _, p in sd.body_paragraphs(src.slides[int(num) - 1])][2]
        if old == text:
            problems.append(f"slide {num}: replacement equals the original third paragraph")
        problems += text_problems(f"slide {num} third paragraph", text)
        if ends_with_limitation([text]):
            problems.append(f"slide {num}: replacement still ends on a caveat")
    # new slides
    for ins in m.spec["inserts"]:
        where = f"scaffold after slide {ins['after']}"
        body = ins["paragraphs"]
        notes = " ".join(flatten(ins["notes"]))
        n_body = words(" ".join(body))
        if not A_BODY_WORDS[0] <= n_body <= A_BODY_WORDS[1]:
            problems.append(f"{where}: body has {n_body} words (expected {A_BODY_WORDS[0]}-{A_BODY_WORDS[1]})")
        if not A_NOTE_WORDS[0] <= words(notes) <= A_NOTE_WORDS[1]:
            problems.append(f"{where}: notes have {words(notes)} words (expected {A_NOTE_WORDS[0]}-{A_NOTE_WORDS[1]})")
        if title_wraps(ins["title"]):
            problems.append(f"{where}: title wraps onto a second line ({len(ins['title'])} chars): {ins['title']!r}")
        if ends_with_limitation(body):
            problems.append(f"{where}: closes on a caveat")
        for t in body + [ins["title"], notes]:
            problems += text_problems(where, t)
    # the built deck
    built = Presentation(str(out))
    want = len(src.slides) + len(m.spec["inserts"])
    if len(built.slides) != want:
        problems.append(f"deck has {len(built.slides)} slides, expected {want}")
    labels = [sd.classify(s)["number"].text_frame.text.strip() for s in built.slides if sd.classify(s)["number"]]
    if sum(1 for l in labels if l.endswith("a")) != len(m.spec["inserts"]):
        problems.append("slide-number labels do not match the number of scaffold slides")
    caveat = 0
    for s in list(built.slides)[1:-1]:
        paras = [p.text for _, p in sd.body_paragraphs(s)]
        if paras and ends_with_limitation(paras):
            caveat += 1
    body_slides = len(built.slides) - 2
    if caveat > MAX_LIMITATION_SHARE * body_slides:
        problems.append(f"{caveat} slides still end on a caveat (limit {int(MAX_LIMITATION_SHARE * body_slides)})")
    print(f"built {out.name}: {len(built.slides)} slides, {caveat} end on a caveat")
    for p in problems:
        print("  PROBLEM:", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
