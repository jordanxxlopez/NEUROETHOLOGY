# Lecture 62

The exact special-topic title and Date TBD are in course/schedule.json. Follow AGENTS.md and PROMPT.md. Scientific sources are in research/refs.json, verified against Crossref and the papers. PAPERS.md records the resolved Baratta upload.

Rebuild with `python lectures/L62/write_spec.py`, then `python lectures/L62/build.py`. The latter calls tools/build_lecture.py and tools/check_lecture.py, with a local title-positioning adjustment for this unusually long title. No scientific figures are generated.

To recrop, place the original PDFs at the papers/ paths in crops.json and run `python lectures/L62/crop_source_figures.py`. This invokes the repository crop tool with its PyMuPDF fallback, so normalized boxes match the inspected CropBox coordinates. PDF inputs are ignored by Git; all delivered crops are already tracked.

DELIVERY.md has the public PPTX, preview, permanent repository backup, font inventory and verification results. Required Field Experience: Fall Recess material is excluded.
