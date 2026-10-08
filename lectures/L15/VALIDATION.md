# Lecture 15 — validation

- Built with `tools/build_lecture.py`; repository checker reports **46 slides, 44 image slides, 44 article-figure slides, 26 native-color slides, zero failures and zero warnings**.
- Exact schedule title and date retained. Arial specified in every PowerPoint text run. Three explanatory paragraphs on each content slide; 100–142 words per slide. Expanded teaching transcripts and verified DOI references are included in speaker notes. Six exam-level takeaways have bold lead phrases.
- All 48 used source crops inspected against their PDF pages. Axes, units, panel letters and scale bars retained; crop bounds recorded in `crops.json`. Original author model and reanalysis panels are distinguished from measured data. No new figures, plots, recoloring or generated images.
- LibreOffice export contains 46 PDF pages. Every rendered slide inspected, including revised slides after correcting the crowded calibration paragraph and enlarging dense recordings. No off-page text or body/footer collisions in the final PDF.
- PPTX ZIP integrity verified. Theme iron / cloud blue recorded as used only after final validation.

Source PDFs stay in the ignored `papers/` directory. `research.json` records sources, searches, PDF origins and checksums.

Public immutable GitHub downloads tested without authentication: PPTX and PDF return HTTP 200 and exactly match the validated local files. Downloaded PPTX opens as a valid 46-slide ZIP, downloaded PDF has 46 pages, and the GitHub PDF preview returns HTTP 200. Links and checksums are recorded in `export.json`.
