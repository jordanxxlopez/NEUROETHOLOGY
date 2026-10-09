# Lecture 40 — completed build

Exact title: Frontiers: optogenetics, wireless-recording tools in emerging neuroethology systems, and casual tests of neural circuits underlying natural behavior

Exact date: Friday, December 4, 2026

The instructor’s new title, including the literal wording `casual tests`, is preserved in the authoritative schedule and delivered files. The scientific material distinguishes causal interventions from observational recording.

The connected repository’s current default branch (`claude/neuroethology-fa2026-schedule-2lgmmr`) was fetched and verified against `9da8853a42489ca33b314611e264fcc3eb06a226` and refreshed against `9cd700618873a75325dd8af5f5c144ea58814cf1` before publication. The new optional-lecture rules for lectures 41+ were retained; they do not change Lecture 40 requirements. Earlier lectures are unchanged. No ZIP or outdated branch was used.

## Evidence and presentation

- 46 slides: one title, 44 content slides, and six exam-level points on one Key takeaways slide.
- Three explanatory paragraphs on every content slide, with complete teaching-transcript notes and verified DOI references.
- All 44 content slides carry original primary-paper figures; 38 have native published color.
- 50 original PDF crops from 13 primary papers; no web photographs, generated illustrations, redrawn graphs or recolored panels.
- The title carries an original image of the annelid Platynereis. Published structural images accompany discussion of neural cells, regions and effectors.
- Unused muted rosewood / paper white theme, Arial throughout including notes, black body/caption/footer text, and darker rosewood headings and bold terms.
- The exact long title uses the repository builder’s optional `title_height` setting. Its default is unchanged for other lectures.

## Reproduction

Place the original PDFs listed in `PAPERS.md` under `papers/`, then run:

```bash
python tools/crop_panels.py lectures/L40/crops.json
python lectures/L40/build.py
soffice --headless --convert-to pdf --outdir lectures/L40 lectures/L40/Neuroethology_Lecture40_FA2026.pptx
```

`build.py` calls `tools/build_lecture.py`, formats the notes, and runs the repository checker. `plan.json` records final slide titles, source allocation and panel assignments; `research.json` preserves literature searches and citation/access verification. `validation.json` and `validation.txt` record the completed checks. `export.json` records verified public downloads after publication.

## Instructor-requested blue styling revision

The instructor requested a theme matching the blue optical light in a mouse photograph: dark-blue titles and bold terms, with black body/caption/footer text. The deck now uses `optical-blue-paper` (title panel #284FA6; headings/bold #1E3B7B). All slide wording, notes, scientific image bytes and element positions were compared with the previous deck and are unchanged. The rebuilt PPTX and 46-page PDF pass the repository checker with no failures or warnings.

The requested title-photo replacement remains pending: the inline mouse image was visible in chat but had no downloadable identifier or local image attachment. Its original URL was requested. The existing title figure remains until the exact source image can be inserted; no substitute or generated image was used.
