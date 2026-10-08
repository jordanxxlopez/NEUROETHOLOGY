# Lecture 3 — build and verification

The authoritative repository default branch was refreshed before finalization. The deck uses the exact schedule title and date, the unused crimson/slate theme, and the repository builder.

## Rebuild

From the repository root, with `requirements.txt` installed:

```bash
python tools/build_lecture.py lectures/L3/lecture.json
```

To reproduce source crops, place the eight PDFs at the paths listed in `crops.json` and run:

```bash
python tools/crop_panels.py lectures/L3/crops.json
```

PDFs are ignored by Git. The committed PNGs already permit a deck rebuild without the PDFs. All images are original article crops. The same published anatomy is reused where it identifies the structure being discussed.

The builder accepts optional `title_refs` so the title animal has a complete source reference in its notes. For tall recordings, `figures-right` supports `figure_arrangement: "side-by-side"` and `primary_figure_width`; the source panels are placed separately, without changing their pixels. Other two-figure slides retain the established stacked layout. The outer layout remains teaching text beside scientific figures.

## Verification

- 46 slides: title, 44 content slides, six-item key takeaways.
- Exact title: Cockroach escape: the cercal system and giant interneurons (Camhi).
- Exact date: Friday, August 28, 2026.
- Three explanatory paragraphs and a teaching transcript on every content slide.
- Article images on all 44 content slides; original source color on 37.
- 39 distinct article crops and 83 image placements across the content slides.
- Eight verified primary papers, with complete DOI references in speaker notes.
- Arial throughout editable slide text; body type is 15–16 pt.
- Repository builder/checker: zero failures and zero warnings.
- LibreOffice PDF conversion: 46 pages. All pages and all retained source crops were visually reviewed, including the enlarged recordings and final terminology edits.

The managed environment has Python 3.12, a virtual environment at `/workspace/.neuroethology/venv`, Poppler and LibreOffice. The PPTX specifies Arial; the Linux PDF preview uses the installed Liberation Sans substitute. No generated QA montage is embedded in the presentation.

Scientific limits and source provenance are recorded in `PAPERS.md`. The reusable instructor prompt is `prompts/make_lecture_3.md`; the permanent image restrictions remain in the repository's AGENTS.md, lecture skill and general prompt.
