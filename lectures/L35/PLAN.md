# Lecture 35 — completed

Exact title: Social behavior: crayfish dominance and serotonergic modulation of escape

Exact date: Wednesday, November 18, 2026

Authoritative repository: `jordanxxlopez/NEUROETHOLOGY`, current default branch `claude/neuroethology-fa2026-schedule-2lgmmr`; starting revision `6f7bedf791dfe8e2b9de85bf2292817eef0e178b`.

## Build and source decisions

- 46 slides: one title, 44 content slides, six bold-led exam takeaways on the final slide.
- All 44 content slides carry primary-paper figures. Original color panels occur on 36 content slides.
- Arial; a new muted `dove-oyster` palette; black body text and captions. All pre-existing palettes were used, so the new palette was added to `course/themes.json`.
- Three full explanatory paragraphs per content slide, with teaching-transcript notes and verified full DOI references.
- Sources progress from hierarchy and fighting through escape circuitry, social-history plasticity, receptor signaling, cAMP experiments, walking circuits and post-defeat avoidance.
- Original article panels were cropped with repository tools. No scientific image was drawn, generated, recolored or replotted. Published anatomical drawings remain unchanged.
- Figure crop coordinates use the PDF CropBox inspected with PyMuPDF; the renderer is selected through `crop_originals.py`.
- The title animal photograph is the original Herberholz et al. (2011), Fig. 1(B).
- LG and MG anatomy on slide 8 comes from the published Herberholz et al. (2001), Fig. 1(B); other LG slides use original Yeh et al. (1997) microscopy.

## Rebuild

```bash
python lectures/L35/write_spec.py
python lectures/L35/crop_originals.py  # requires the original source PDFs
python lectures/L35/build.py
python tools/check_lecture.py lectures/L35/Neuroethology_Lecture35_FA2026.pptx --lecture 35
soffice --headless --convert-to pdf --outdir lectures/L35 lectures/L35/Neuroethology_Lecture35_FA2026.pptx
```

## Validation

Repository checker: 46 slides, 44 article-figure content slides, 36 native-color content slides, zero failures and zero warnings. Every source crop and all 46 rendered pages were inspected. Final edits enlarge tall recordings and paired motor-neuron panels, and correct the Momohara dose unit against the journal HTML. PowerPoint and PDF download hashes are recorded in `export.json`.
