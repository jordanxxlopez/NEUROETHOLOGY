#!/usr/bin/env python3
"""Check a finished NEUR 411 deck against the house rules.

    python tools/check_lecture.py deck.pptx --lecture 11 [--content-slides 44]

Works on any .pptx, including decks not made by build_lecture.py.
Exit code 1 if any rule fails.
"""
import argparse
import json
import re
import sys
from pathlib import Path

from pptx import Presentation

ROOT = Path(__file__).resolve().parent.parent

BANNED = [
    (r"\bup next\b|\bnext (time|lecture|class)\b|\bcoming up\b|\bpreview of\b", "no 'up next' / next-lecture slides or lines"),
    (r"\bpart \d+ of \d+\b|\(\d+\s*/\s*\d+\)|\bpart [ivx]+\b", "no 'Part 1 of 4' style splitting"),
    (r"^\s*(lecture )?(outline|agenda|overview|roadmap)\s*$", "no outline/agenda slide"),
    (r"\blearning (objectives|goals|outcomes)\b|^\s*objectives\s*$", "no objectives slide"),
    (r"\bin this lecture\b|\btoday we will\b|\bwe will (now )?(discuss|cover|explore)\b|\blet'?s (look|turn|explore)\b",
     "no lecture metacommentary"),
    (r"\b(continued|cont\.)\s*$", "no 'continued' slide splits"),
    (r"lorem|ipsum|\bTODO\b|\bTBD\b|\[insert", "placeholder text left in"),
]
MIN_WORDS = 70         # per content slide, text only
MIN_FIGURE_SLIDES = 15 # content slides carrying at least one research figure


def slide_text(slide):
    out = []
    for sh in slide.shapes:
        if sh.has_text_frame:
            out.append(sh.text_frame.text)
        if sh.has_table:
            for row in sh.table.rows:
                for c in row.cells:
                    out.append(c.text)
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("--lecture", type=int, required=True)
    ap.add_argument("--content-slides", type=int, default=44)
    a = ap.parse_args()

    sched = json.loads((ROOT / "course/schedule.json").read_text())
    meta = next(l for l in sched["lectures"] if l["n"] == a.lecture)
    prs = Presentation(a.deck)
    slides = list(prs.slides)
    errs, warns = [], []

    want = a.content_slides + 2
    if len(slides) != want:
        errs.append(f"deck has {len(slides)} slides; need {want} (1 title + {a.content_slides} content + 1 key takeaways)")

    first = re.sub(r"\s+", " ", slide_text(slides[0]))
    if re.sub(r"\s+", " ", meta["title"]) not in first:
        errs.append(f"title slide does not contain the exact schedule title: {meta['title']!r}")
    month_day = meta["date"].split(", ")[1]  # e.g. "September 18"
    if month_day not in first:
        errs.append(f"title slide missing date {meta['date']!r}")

    if "key takeaways" not in slide_text(slides[-1]).lower():
        errs.append("last slide must be 'Key takeaways'")

    fig_slides = 0
    for i, s in enumerate(slides, 1):
        txt = slide_text(s)
        for line in txt.splitlines():
            for pat, why in BANNED:
                if re.search(pat, line, re.I):
                    errs.append(f"slide {i}: {why}: {line.strip()[:80]!r}")
        if i in (1, len(slides)):
            continue
        words = len(txt.split())
        if words < MIN_WORDS:
            errs.append(f"slide {i}: only {words} words; content slides need >= {MIN_WORDS}")
        pics = [sh for sh in s.shapes if sh.shape_type == 13 and sh.height > 914400 * 0.6]
        if pics:
            fig_slides += 1
        notes = s.notes_slide.notes_text_frame.text if s.has_notes_slide else ""
        if not re.search(r"\((19|20)\d{2}[a-z]?\)|\b(19|20)\d{2}[a-z]?\b", notes):
            errs.append(f"slide {i}: speaker notes need the full reference(s) with year")
        if "doi" not in notes.lower() and "http" not in notes.lower():
            warns.append(f"slide {i}: no DOI/URL in notes")
        if not re.search(r"(19|20)\d{2}", txt.splitlines()[-2] if len(txt.splitlines()) > 1 else ""):
            if not re.search(r"\((19|20)\d{2}[a-z]?\)", txt):
                warns.append(f"slide {i}: no short citation visible on slide")

    if fig_slides < MIN_FIGURE_SLIDES:
        errs.append(f"only {fig_slides} content slides have research figures; need >= {MIN_FIGURE_SLIDES}")

    for w in warns:
        print("WARN ", w)
    for e in errs:
        print("FAIL ", e)
    print(f"{len(slides)} slides, {fig_slides} figure slides, {len(errs)} failures, {len(warns)} warnings")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
