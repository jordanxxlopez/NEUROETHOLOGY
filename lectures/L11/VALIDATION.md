# Lecture 11 — validation

- Built with `tools/build_lecture.py`; `tools/check_lecture.py` reports 0 failures and 0 warnings.
- 46 slides: title, 44 content slides and six-item Key takeaways. Schedule title/date preserved exactly.
- Original article figures on all 44 content slides; native published color on 41. One credited, licensed web photograph on the title.
- All visible text uses Arial. Each content slide contains three full paragraphs and a teaching transcript followed by full DOI references.
- All scientific image hashes embedded in the PPTX match their source crop files byte for byte. No scientific images were created, recolored, re-plotted or redrawn.
- Reviewed every source crop against its original article and all 46 LibreOffice-rendered slides for clipping, text overflow and caption/footer collisions. Rendered text bounds fit within their columns.
- PDF preview contains 46 pages. Final counts are in `validation.json`; original PDF retrieval and upload provenance are in `research.json`.

Rebuild with the repository requirements installed, obtain the source PDFs listed in `PAPERS.md`, run `tools/crop_panels.py lectures/L11/crops.json`, then run `lectures/L11/write_spec.py` and `tools/build_lecture.py lectures/L11/lecture.json`.
