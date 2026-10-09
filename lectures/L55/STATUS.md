# Lecture 55: complete

Built from the current default branch of jordanxxlopez/NEUROETHOLOGY, including the October 9 teaching-focused writing update. The exact schedule title and `Date TBD` are preserved.

- 46 slides: title, 44 content slides and six exam-level key takeaways.
- All 44 content slides contain original primary-article figures; 37 include source color.
- Twelve source papers, verified citations and DOI references in speaker notes.
- Three teaching paragraphs per content slide, natural teaching transcripts and varied paragraph order.
- No em dashes in slide text and zero caveat-ending content slides.
- No created, reconstructed or recolored images; no web or stock photographs.
- New stone brown / porcelain palette, recorded for Lecture 55; Arial throughout.
- Repository builder/checker: zero failures and zero warnings.
- All 46 rendered slides and all 57 source crops inspected; corrected panel boundaries and enlarged dense figure layouts rechecked.

## Rebuild

```bash
python lectures/L55/write_spec.py
python tools/build_lecture.py lectures/L55/lecture.json
python tools/check_lecture.py lectures/L55/Neuroethology_Lecture55_FA2026.pptx --lecture 55
```

The reusable request is in `PROMPT.md`. Scholarly web searches are recorded in `research_queries.json`. Figure provenance, PDF pages and crop coordinates are in `figure_sources.json` and `crops.json`. For recropping, obtain the PDFs listed in `source_downloads.json`, verify the hashes in `research.json`, and update the scratch paths in `crops.json`. Source PDFs remain outside the committed lecture folder.
