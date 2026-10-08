# NEUR 411 Neuroethology — lecture builder (instructions for coding agents)

This repo builds the course's lecture PowerPoints. When asked to "make lecture N" (or given a topic from `course/schedule.json`), follow every rule and step below. Claude Code reads the same rules from `.claude/skills/neuroethology-lecture/SKILL.md`; keep the two files in sync.

Lectures 8, 9 and 10 are the approved model. Lectures 1-7 used an older format; do not copy them.
Every rule below comes from the instructor. Follow all of them every time, without being asked again.

## Fixed rules

1. **Title is sacred.** Take the title and date from `course/schedule.json` exactly, character for character. Never reword, shorten, or split it into "Topic / subtitle" with different words. (The builder reads it from the schedule for you.)
2. **Slide count:** 1 title slide + **44 content slides** + 1 **Key takeaways** slide = **46 slides**. If the instructor gives a different number for a specific lecture, set `"content_slides"` in the spec to match what they said and tell them the total.
3. **Never include:** an outline/agenda, learning objectives, "Up next" / "Next lecture" / previews, "Part 1 of 4" or "(continued)" splits, or lecture metacommentary ("In this lecture we will…", "Let's look at…", "This is important because…" repeated). Open with the topic and go straight into the material.
4. **Research-based.** Do web searches and use the primary literature. Every content slide is built around real studies: the preparation, the method, the controls, the measured **results with numbers and units**, and what the result does and does not establish. Verify each citation (authors, year, journal, volume, pages, DOI) against the source before using it. No invented data, no simulated curves presented as measurements.
5. **Real figures, not decoration.** Use selected panels from the original papers (axes, units, scale bars and panel letters intact) and explain what the panel shows. No stock photos or clip art. At least 15 content slides carry a research figure; Lectures 8-10 had 20+.
6. **More words per slide, academic register.** Each content slide has 3-5 full explanatory paragraphs (about 90-170 words of text). Define every technical term the first time it appears. Explain circuits, neurotransmitters, receptors and ion channels step by step and connect them to neuronal activity and to behavior. Distinguish established findings from proposed explanations ("supports", "is consistent with", "has not been shown").
7. **New color theme every lecture.** Pick a palette from `course/themes.json` that is not in `used`. Never yellow, orange, gold or other loud colors; purple and green are already used. Font is always **Arial**. After the deck is final, add the lecture to `used`.
8. **Citations:** short citation in the slide footer (e.g. `Maisak et al. (2013)`), full reference with DOI in the speaker notes, figure caption names the exact figure and panel (`Author (year), Fig. 3B. …`).
9. **Key takeaways are for the exam**, not a summary of the slide titles: 5-6 statements of what a student must know, each with a bold lead phrase.
10. Deliver a downloadable **.pptx**.

## Workflow

1. Look up the lecture in `course/schedule.json` (number, exact title, date). Read the previous lecture's spec in `lectures/` if one exists so content does not repeat.
2. **Research** (use web search; open papers in the browser or download PDFs): find the classic papers named in the title and the key modern work (anatomy, physiology, molecular/ion-channel mechanism, behavior). Prefer open-access PDFs (PMC, journal OA, author pages) so figures can be cropped. Record full references with DOIs.
3. **Plan 44 content slides** that progress: behavior → anatomy → neuronal activity → cellular/synaptic/channel mechanism → modulation/plasticity/state → comparative and current work. One idea per slide; title is a short claim (≤ 62 characters, no final period).
4. **Figures:** download the PDF into its own scratch folder outside `lectures/`, then
   `python tools/crop_figure.py paper.pdf <page> --preview p.png` → look at it →
   `python tools/crop_figure.py paper.pdf <page> --box L T R B -o lectures/L<N>/figures/<name>.png`.
   Check each crop visually: no clipped labels, no fragments of neighboring panels.
   **If the session's network blocks journal/PMC downloads** (check once with `curl -sI https://pmc.ncbi.nlm.nih.gov`), do not invent figures: re-plot only the numbers the papers report (write a `lectures/L<N>/make_figures.py`, matplotlib, theme colors, draw at ~0.72 scale so labels stay legible) and draw labeled schematics of methods/circuits. Every caption must say "re-plotted from values reported in …" or "schematic drawn from …". Tell the instructor that original panels can be swapped in if they upload the PDFs.
5. **Write the spec** (for long lectures, generate it from a `write_spec.py` that defines each reference once): copy `lectures/_template/` to `lectures/L<N>/` and fill `lecture.json` (layouts: `text`, `figure-right`, `figure-left`, `figure-below`, `two-figures`, `table`; `**bold**` for key terms, `_italic_` for species names). Vary layouts; most slides should carry a figure or a results table. Prefer `figure-right` for most figure slides — it keeps body text largest.
6. **Build:** `python tools/build_lecture.py lectures/L<N>/lecture.json` → writes `lectures/L<N>/Neuroethology_Lecture<N>_FA2026.pptx` and runs `tools/check_lecture.py`. The builder refuses text that will not fit at 13 pt; cut words or move a paragraph rather than shrinking further. Fix every FAIL.
7. **Visual QA:** `soffice --headless --convert-to pdf <deck>.pptx` then `pdftoppm -jpeg -r 60 <deck>.pdf slide`, and look at every slide image (text overflow, figure crops, caption collisions with the footer). Fix and rebuild.
8. Add the theme to `used` in `course/themes.json`, commit the spec, figures and deck, and give the instructor the .pptx.

## Checks you can run on any deck

`python tools/check_lecture.py deck.pptx --lecture <N>` — slide count, exact title and date, banned slide types/phrases, minimum words per slide, figures, references in notes. Lecture 10 passes it cleanly.

## Setup

```bash
pip install -r requirements.txt      # python-pptx, Pillow, matplotlib
# also needed: poppler (pdftoppm) and LibreOffice (soffice) for figure crops and visual QA
#   macOS:  brew install poppler && brew install --cask libreoffice
#   Ubuntu: sudo apt install poppler-utils libreoffice
```

## Repo map

- `course/schedule.json` — all 40 lecture numbers, dates and exact titles.
- `course/themes.json` — used themes and available palettes.
- `tools/build_lecture.py` — spec (`lecture.json`) → .pptx, then runs the checker.
- `tools/check_lecture.py` — rule checker for any deck.
- `tools/crop_figure.py` — cut figure panels from paper PDFs.
- `lectures/_template/` — starter spec showing every layout.
- `lectures/L12/` — a complete worked example (spec generator, figure script, finished deck).
- `reference/` — approved Lectures 8–11 decks.

