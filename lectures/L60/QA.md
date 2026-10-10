# Lecture 60 validation

Built with tools/build_lecture.py through the lecture-local build.py wrapper. The wrapper only positions the unusually long exact title and title-slide metadata; it reruns tools/check_lecture.py after saving.

Validation: 46 slides; all 44 content slides have original primary-paper figures; 34 content slides have source-color images; zero checker failures and zero warnings. All content slides contain three teaching paragraphs. References and teaching transcripts are in speaker notes. No em dashes occur in slide text.

The native PPTX was rendered with LibreOffice and all 46 slides inspected. A fresh 1280 x 720 HTML version was generated from the scientific spec for public delivery; all images loaded and the browser reported zero overflowing elements. All 46 HTML slides were visually reviewed, with changed slides reviewed again after final edits.

Figure fidelity corrections included complete hydrodynamic axes, the full Kiss2 puberty graph and histology panel, and removal of adjacent panel fragments. Senarat et al. Figure 35 is identified by its actual spinal-cord anatomy rather than the inconsistent source caption. Original panel identifiers remain intact.

Rebuild from the repository root:

```sh
python lectures/L60/write_spec.py
python lectures/L60/build.py
```

Original PDFs are ignored by git. To regenerate crops, restore the seven source PDFs to papers/ and run tools/crop_panels.py on crops.json.
