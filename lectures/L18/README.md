# Lecture 18

**Owl sound localization I: ITD/ILD maps in the inferior colliculus (Konishi & Knudsen)**

**Monday, October 5, 2026**

Built from the current default branch through `32bc0f77b9a4eb06778a1efd5fcaaa57d0679a2d`, with the stricter instructor image requirements retained. Reference presentations include the uploaded Lecture 16 and Lectures 12–15. Steel / sky is a new theme; all text is Arial.

The deck has 46 slides: a title slide, 44 content slides carrying authentic article figures and three explanatory paragraphs each, and six exam-level takeaways. Content notes contain teaching transcripts, full references, and figure DOI provenance. The figure set uses 15 primary papers, including both instructor-supplied Science PDFs.

## Rebuild

```bash
python lectures/L18/write_spec.py
python tools/build_lecture.py lectures/L18/lecture.json
python lectures/L18/finalize.py
python tools/check_lecture.py lectures/L18/Neuroethology_Lecture18_FA2026.pptx --lecture 18
```

`finalize.py` preserves the scheduled title as one exact paragraph and adds complete takeaway notes; it creates no images. The course builder supplies the title/date and all slide layouts. Figure crops remain unchanged; `crops.json` and `sources/provenance.json` document their original PDF origins. To recrop an entry, use its PDF, one-based page, and fractional `box` with `tools/crop_figure.py`.

Validation includes the repository checker, exact title/date comparison, paragraph counts, Arial run inventory, complete notes/reference checks, image-blob comparison against recorded PDF crops, and visual inspection of all 46 rendered slides. Final checks are recorded in `validation.json`.
