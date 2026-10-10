# Lecture 73 completed

The 46-slide PowerPoint is `Neuroethology_Lecture73_FA2026.pptx`. It preserves the exact title and date from the current default-branch schedule.

All 44 content slides carry original published article figures; 35 carry source-color figures. Twelve primary papers support the content, including the two user-uploaded PDFs. Every content slide has three teaching paragraphs and a teaching transcript with full DOI references in its notes. The final slide has six exam-level takeaways.

The repository checker reports zero failures and zero warnings. All 46 final slides were rendered through LibreOffice and visually reviewed. No text, caption, or footer collisions remain. The new pewter / paper white theme is recorded for Lecture 73.

Rebuild with `python lectures/L73/write_spec.py` and `python tools/build_lecture.py lectures/L73/lecture.json`. To reproduce the original figure crops, restore the source PDFs listed in `research.json` under the ignored `papers/` directory and run `python lectures/L73/prepare_figures.py`. The canonical crop manifest is `crops.json`. No image is generated, redrawn, recolored, or substituted.

`PROMPT.md` preserves the reusable original-image and teaching-content requirements. `search_log.json`, `research.json`, `figure_sources.json`, and `qa.json` record the research and verification.
