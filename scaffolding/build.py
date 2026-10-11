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
from style_rules import body_problems, line_problems, tongue_twister_flags, EM_DASH, MAX_LIMITATION_SHARE, ends_with_limitation, framing_problems, stats_problems  # noqa: E402

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
    subprocess.run([sys.executable, str(ROOT / "tools/scaffold_deck.py"), str(deck), str(spec_json), str(out)] + (["--single-box"] if n >= 21 else []), check=True)

    problems = []
    src = Presentation(str(deck))
    # rewritten third paragraphs: only slides whose third paragraph really changed, no caveat left
    for num, value in m.spec["third_paragraph"].items():
        if int(num) in m.spec.get("body", {}):             # the full body rewrite replaces this paragraph
            continue
        old = [p.text for _, p in sd.body_paragraphs(src.slides[int(num) - 1])][2]
        text = sd.resolve_third(old, value)
        if "--show" in sys.argv:
            print(f"-- slide {num}\n   OLD: {old}\n   NEW: {text}")
        if old == text:
            problems.append(f"slide {num}: replacement equals the original third paragraph")
        problems += text_problems(f"slide {num} third paragraph", text)
        if ends_with_limitation([text]):
            problems.append(f"slide {num}: replacement still ends on a caveat")
        if n >= 21:
            problems += [f"slide {num} third paragraph: {w}" for w in body_problems([text])]
    # full body rewrites (scaffolding/RULES.md): three developed paragraphs, 60-130 words each
    for num, paras in m.spec.get("body", {}).items():
        where = f"body of slide {num}"
        if len(paras) != 3:
            problems.append(f"{where}: needs exactly 3 paragraphs, has {len(paras)}")
        for k, t in enumerate(paras, 1):
            if n < 31 and not 50 <= words(t) <= 115:
                problems.append(f"{where} paragraph {k}: {words(t)} words (expected 50-115, about 5-7 lines)")
            problems += text_problems(where, t)
        problems += [f"{where}: {w}" for w in body_problems(paras)]
        for t in paras:
            for phrase, why in tongue_twister_flags(t):
                print(f"  REVIEW {where}: {why}: {phrase!r}")
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
        if n >= 21:
            problems += [f"{where}: {w}" for w in body_problems(body)]
        for t in body + [ins["title"], notes]:
            problems += text_problems(where, t)
    # the built deck: body paragraphs fill 5-7 lines from Lecture 31 on (scaffolding/RULES.md)
    if n >= 31:
        built_check = Presentation(str(out))
        for k, sl in enumerate(built_check.slides, 1):
            if k in (1, len(built_check.slides)):
                continue
            counts = sd.body_line_counts(sl)
            if counts:
                problems += [f"built slide {k}: {w}" for w in line_problems(counts)]
            problems += [f"built slide {k}: {w}" for w in sd.body_format_problems(sl)]
    # the built deck
    built = Presentation(str(out))
    # body layout (scaffolding/RULES.md): exactly three body paragraphs per content slide, and no
    # paragraph of the original deck left on a slide
    original = {p.text.strip() for sl in src.slides for sh in sl.shapes if sh.has_text_frame
                for p in sh.text_frame.paragraphs if p.text.strip()}
    for k, sl in enumerate(built.slides, 1):
        if k in (1, len(built.slides)):
            continue
        c = sd.classify(sl)
        if c["title"] is not None and c["title"].text_frame.text.strip().lower().startswith("key takeaways"):
            continue
        for text in sd.overlap_problems(sl):
            problems.append(f"built slide {k}: text overlaps a figure: {text}")
        n_body = sum(1 for bx in c["body"] for q in bx.text_frame.paragraphs if q.text.strip())
        if n_body != 3:
            problems.append(f"built slide {k}: {n_body} body paragraphs (expected 3)")
        for bx in c["body"] + c["caption"]:
            for q in bx.text_frame.paragraphs:
                if q.text.strip() in original and "Fig." not in q.text:
                    problems.append(f"built slide {k}: original paragraph left on the slide: {q.text.strip()[:50]}")
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
