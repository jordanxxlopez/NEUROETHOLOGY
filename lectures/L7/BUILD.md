# Lecture 7 build and review

Completed October 8, 2026 against the connected repository’s current default branch.

- Exact title and date loaded by tools/build_lecture.py from course/schedule.json.
- 46 slides: title, 44 content slides, six exam-level key takeaways.
- Three explanatory paragraphs per content slide (120–146 words), plus complete teaching transcripts and DOI references in notes.
- All 44 content slides carry primary-paper figures; 24 carry source color figures.
- 52 distinct original article crops from 13 verified primary papers; one credited NOAA study-animal photo on the title.
- No images, schematics, graphs or data were generated, redrawn or recolored.
- New slate / dusty rose palette recorded; previous Lecture 7 and current Lecture 8 theme records preserved.
- Built with tools/build_lecture.py; repository checker: zero failures, zero warnings.
- All source pages, retained crops and 46 rendered slides visually reviewed. Two crowded text slides and two undersized secondary recordings corrected and reviewed again.
- LibreOffice PDF export verified at 46 pages; content text remains above the footer in every page.
- PPTX and PDF preview retained together for download and viewing.

## Reproduce

Install requirements.txt and Poppler/LibreOffice. Supply the 13 PDFs listed in sources.json under papers/ (ignored by Git). Run:

```bash
python tools/crop_panels.py lectures/L7/crops.json
python lectures/L7/write_spec.py
python tools/build_lecture.py lectures/L7/lecture.json
python tools/check_lecture.py lectures/L7/Neuroethology_Lecture7_FA2026.pptx --lecture 7
```

The reusable instructor prompt is prompts/make_lecture_7.md. The strict image rules are retained in AGENTS.md and the matching neuroethology-lecture skill.

PPTX SHA-256: `5eaf96cd4c01d6027002ec4357e10ddd81a8bca112a39379214e7b19a71b66b7`
