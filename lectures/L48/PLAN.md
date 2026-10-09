# Lecture 48 — completed build

The current repository default branch at bbf3b0d504476212995aea9107e7853b214d8a02 supplied the rules, templates, schedule and build tools. The instructor’s new special topic was added verbatim with Date TBD. No ZIP or older checkout was used.

The finished deck contains 46 slides, three academic paragraphs on each of 44 content slides, original published figures on every content slide, and six exam-level takeaways. Twelve full-text primary sources cover comparative brain organization, candidate trigeminal and facial maps, auditory psychophysics, foot mechanoreceptors, bone-conduction mechanics, controlled seismic behavior and field localization. The eLife source is identified accurately as a peer-reviewed reviewed preprint. Behavioral effects, anatomical assignments and proposed mechanisms are kept distinct.

Figures are rectangular crops of original PDFs; axes, labels, units, scale bars and panel letters are preserved. No scientific visuals were generated, reconstructed or recolored. Web photos were not needed. Figure provenance includes page coordinates and PDF/image hashes. The title animal photograph comes from the original Kaufmann article.

Build and verification:

```sh
python tools/crop_panels.py lectures/L48/crops.json
python lectures/L48/write_spec.py
python tools/build_lecture.py lectures/L48/lecture.json
python lectures/L48/finalize.py
python tools/check_lecture.py lectures/L48/Neuroethology_Lecture48_FA2026.pptx --lecture 48
python lectures/L48/audit.py
```

`finalize.py` preserves the exact long title in one text paragraph, positions the date and instructor, formats all speaker-note text in Arial, and adds clickable DOI hyperlinks. The builder itself remains unchanged. The native PPTX was rendered to 46 PDF pages and every slide reviewed visually. Presenton generates fresh public download and browser-preview links from matching editable slide text and the exact source-image assets.
