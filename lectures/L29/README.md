# Lecture 29

**Navigation II: honeybee waggle dance and sun-compass navigation (von Frisch)**

**Monday, November 2, 2026**

Authoritative connected default branch was refreshed at task start and merged again at `02dd657`, including completed Lecture 28. Work is on `codex/lecture29-primary-sources`. No ZIP or older checkout was used. Current AGENTS.md, lecture skill, schedule, template, themes and the preceding lecture were reviewed. All seven supplied example decks were inspected for slide content, images, notes and typography; their review is recorded in `example-review.json`.

The completed deck has 46 slides: a title, 44 content slides and six exam-level key takeaways. All 44 content slides carry authentic primary-paper figure crops, with three explanatory paragraphs each (115–140 words), natural teaching transcripts and full references with linked DOIs. The repository checker detects color on 29 content slides, above the half-deck target. No generated, redrawn, recolored or re-plotted scientific visuals, stock decoration, or web photos were used. Specific anatomical structures are accompanied by published anatomy. All editable text and notes are Arial. The new palette is oyster gray / muted carmine.

Academic web searches covered dance communication, visual odometry, sun-compass learning and timing, polarization, compass anatomy, antennal mechanoreception and social learning. Seventeen primary articles were verified and analyzed. Twelve PDFs were downloaded; five were uploaded by the instructor. `references.json` contains verified full citations; `PAPERS.md` lists them; `available-papers.json` records original PDF hashes. `needed-papers.json` is empty. Source metadata, access records and searches are in `sources/`. Rejected unverified or unrelated DOI candidates were excluded.

`figure-sources.json` records each source paper, figure/panel, DOI, PDF page and crop box. `crops.json` is the complete repository crop manifest; `make_crops.py` reproduces it. Scientific content remains unchanged, including axes, labels, units, scale bars and panel letters. The title uses the complete original panel containing the photographed animal.

## Rebuild

```bash
python lectures/L29/make_crops.py
python lectures/L29/write_spec.py
python tools/build_lecture.py lectures/L29/lecture.json
python lectures/L29/finalize.py
python tools/check_lecture.py lectures/L29/Neuroethology_Lecture29_FA2026.pptx --lecture 29
```

`finalize.py` preserves the exact schedule title in one editable run and applies Arial and DOI links to notes. `validate.py` additionally checks exact title/date, counts, paragraphs, references, editable fonts, original-crop byte hashes and all rendered PDF titles. PDF rendering and all 46 slides were visually reviewed; used crops were checked against their source pages. `validation.json` records results.

The build initially misidentified the legitimate author surname Ai as an AI-image label. `tools/style_rules.py` now excludes only that exact capitalization from the abbreviation match; generated/redrawn/simulated image rejection remains active. Two focused tests verify both authentic-author acceptance and generated-image rejection.

Fresh Presenton PPTX/PDF download links and a browser preview are generated from the final native slide geometry, editable text, unchanged source images and full teaching notes. URLs expire after 24 hours. The native repository PPTX remains available for later rebuilding/export. The strict figure policy already persists in the current guidelines and `prompts/make_lecture_29.md`.

The configured Python environment, LibreOffice and Poppler support the full build and rendering workflow. No onboarding configuration changes were required.
