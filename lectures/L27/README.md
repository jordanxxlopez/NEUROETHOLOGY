# Lecture 27

**Archerfish: predictive aiming and ballistic prey capture** — **Wednesday, October 28, 2026**.

The connected repository default branch was refreshed and merged through commit 8c7bafd before preparation was completed. No ZIP was used. Current AGENTS.md, neuroethology-lecture skill, schedule, themes, template, and build tools were followed. Uploaded Lectures 8, 9, 22, 23, and 24 were inspected as format examples (example-review.json).

46 slides: title, 44 three-paragraph content slides, and six exam takeaways. Every content slide has primary article figures; 35 include original color. Full teaching notes and linked DOI references appear on all slides. No generated, redrawn, reconstructed, recolored, stock, or decorative scientific visual is present. Theme: rosewater / harbor blue; font: Arial.

Eleven original primary PDFs support the deck. The instructor supplied five previously inaccessible papers; access is resolved. Figures were cropped with tools/crop_panels.py, which calls tools/crop_figure.py. Cropping provenance, hashes, research searches and Crossref metadata are preserved. PDFs remain ignored in papers/. Bibliographic years follow the selected eLife reviewed-preprint PDF volume-year lines (2023;12:RP92909 and 2024;13:RP99634), rather than later indexing dates. Species/preparation differences and causal limits are explicit.

Rebuild with the repository Python environment:

```sh
python lectures/L27/make_crops.py
python lectures/L27/write_spec.py
python tools/build_lecture.py lectures/L27/lecture.json
python lectures/L27/finalize.py
python lectures/L27/validate.py
```

The native deck passed tools/check_lecture.py; all 46 rendered slides and source crops were reviewed for labels, axes, units, clipping, text fit and caption placement. Validation details: sources/validation.json. The reusable strict-figure prompt is prompts/make_lecture_27.md.
