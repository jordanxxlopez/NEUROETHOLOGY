# NEUR 411 Neuroethology — Fall 2026

This repo builds the course's lecture PowerPoints.

- **To make any lecture, use the `neuroethology-lecture` skill** (`.claude/skills/neuroethology-lecture/SKILL.md`). It holds every format rule; follow it without waiting to be reminded.
- Lectures 8, 9 and 10 are the approved model (46 slides: title + 44 content + key takeaways). Lectures 1-7 are an older format — do not copy them.
- **Never create images.** Figures come from published articles (cropped panels, `Author (year), Fig. N`, DOI) — these get priority. Nearly every slide carries an image: at least 40 of 44 content slides, at least 34 with primary-article figures. The title slide shows the study animal (paper figure or credited web photo). Any slide about a specific structure (brain region, neuron, sense organ) carries an anatomy image of it. Credited web images (`Photo: …`, credit, license; neuroscience-related is fine) only where needed, max 6. No schematics, diagrams, re-plotted charts, illustrations or AI images. If a PDF can't be obtained, ask the instructor to upload it; otherwise use a text slide.
- **Writing:** every sentence teaches source content — no roadmap/transition/figure-reading/takeaway framing, no 'this shows/illustrates', no attention-directing phrases, no filler; speaker notes are a natural teaching transcript; concepts over statistics (no p-values, test names, ± errors); no math the sources don't show. Full rules in the skill; enforced by `tools/style_rules.py`.
- Lecture titles and dates live in `course/schedule.json`. Never change a title.
- Color themes: `course/themes.json` — never reuse one, no yellow/orange, no purple/green.
- Tools: `tools/build_lecture.py` (spec → .pptx, then checks), `tools/check_lecture.py` (rule checker for any deck), `tools/crop_figure.py` (cut figure panels from paper PDFs).
- Python deps: `pip install -r requirements.txt` (python-pptx, Pillow) and poppler (`pdftoppm`).
- `AGENTS.md` holds the same rules for Codex; keep it in sync with the skill.
