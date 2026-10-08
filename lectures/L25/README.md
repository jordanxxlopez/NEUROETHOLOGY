# Lecture 25

**Chemoreception II: lobster olfactory search behavior**

**Friday, October 23, 2026**

46 slides: title, 44 content, six-point Key takeaways. All content slides contain original primary-paper figures; 28 use source-color panels (26 meet the automated color detector). Arial; unused powder blue / oxblood theme, now recorded in course/themes.json.

The instructor’s two uploads resolved the behavioral source gaps. Fifteen verified primary papers support behavioral experiments, sampling hydrodynamics, receptor expression, sensory physiology, intracellular signaling, central modulation and explicitly identified computational hypotheses. No scientific visual was created, reconstructed, replotted or recolored.

Rebuild from repository root:

```bash
python lectures/L25/make_crops.py
python tools/crop_panels.py lectures/L25/crops.json
python lectures/L25/write_spec.py
python tools/build_lecture.py lectures/L25/lecture.json
python lectures/L25/finalize.py
python lectures/L25/validate.py
python tools/check_lecture.py lectures/L25/Neuroethology_Lecture25_FA2026.pptx --lecture 25
```

Ignored original PDFs must be present in papers/ for cropping. figure-sources.json records original PDF page, fractional crop coordinates, DOI, original color and file hashes. The renderer uses the unaltered original crops as image objects; slide text remains editable. Complete DOI-linked references and natural teaching transcripts are in speaker notes.

The PPTX was rendered with LibreOffice to a 46-page PDF. All slides and original figure crops were visually reviewed for missing labels, overflow, layout and caption placement; automated checks passed with no failures or warnings. The exact title and date were validated against course/schedule.json. Presentation and PDF exports are delivered through fresh Presenton HTTPS links and a viewable preview.
