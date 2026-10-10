# Lecture 81: completed

Built with the current repository lecture builder and exact schedule title and Date TBD. The supplied PDFs and three additional secured primary papers support the deck. Bibliographic references and DOI sources are recorded in research.json and speaker notes.

The final PPTX has 46 slides, 44 content slides with original primary-article figures, 43 content slides with original color figures, six exam-level takeaways, and two original article-provided recordings. No figures were generated, redrawn, replotted, or recolored. The title animal photograph is an original article panel.

The repository checker passed with zero failures and zero warnings. All 46 slides were rendered with LibreOffice and Poppler and visually reviewed for text fit, readable figures, panel boundaries, captions, and footers. Two static unedited recording frames retain visible video fallbacks in PDF exports. Both complete clips decoded without errors; embedded media hashes and relationships were verified. Interactive PowerPoint Slide Show playback could not be tested in this environment.

The new muted carmine / paper white theme is recorded as used for Lecture 81. PLAN.md, PROMPT.md, crops.json, figure_sources.json, figure_inventory.json, and media_sources.json preserve the content plan, strict image rules, and source provenance. Full source PDFs remain uncommitted under papers/.

Rebuild from the repository root:

```bash
python lectures/L81/prepare_figures.py
python lectures/L81/write_spec.py
python tools/build_lecture.py lectures/L81/lecture.json
python lectures/L81/add_article_media.py
```

Rebuilding requires the secured source PDFs at the locations recorded in crops.json. The media wrapper must run after every builder invocation to restore the original recordings.
