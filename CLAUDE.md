# NEUR 411 Neuroethology — Fall 2026

This repo builds the course's lecture PowerPoints.

- **To make any lecture, use the `neuroethology-lecture` skill** (`.claude/skills/neuroethology-lecture/SKILL.md`). It holds every format rule; follow it without waiting to be reminded.
- Lectures 8, 9 and 10 are the approved model (46 slides: title + 44 content + key takeaways). Lectures 1-7 are an older format — do not copy them.
- Lecture titles and dates live in `course/schedule.json`. Never change a title.
- Color themes: `course/themes.json` — never reuse one, no yellow/orange, no purple/green.
- Tools: `tools/build_lecture.py` (spec → .pptx, then checks), `tools/check_lecture.py` (rule checker for any deck), `tools/crop_figure.py` (cut figure panels from paper PDFs).
- Python deps: `pip install -r requirements.txt` (python-pptx, Pillow) and poppler (`pdftoppm`).
