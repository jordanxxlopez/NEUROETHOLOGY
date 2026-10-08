# Lecture 20 — Fall 2026

Exact title: **Electroreception I: passive sensing in sharks and rays (ampullae of Lorenzini)**

Exact date: **Monday, October 12, 2026**

Built from the connected repository’s refreshed default branch (authoritative upstream commit `5115d7e6233da147b06766e05ac240af031e1f4b`). The uploaded prior lectures were style examples; no ZIP was used.

46 slides: title, 44 content slides, and six exam-level key takeaways. Every content slide has an original published article figure; the deck contains 49 distinct PDF crops and 68 content image instances across ten primary articles. Arial and the unused deep-sea blue/cyan palette follow the course rules. The title animal is an original little-skate photograph published in Bellono et al. (2017).

Scientific visuals are only crops from original article PDFs. Original published diagrams are retained where appropriate; no diagrams, graphs, photos, illustrations or data were generated, reconstructed or replotted. Crop coordinates, original figure/panel numbers, source DOI, and PDF/image hashes are recorded in `crops.json`, `extra-crops.json`, and `sources/provenance.json`. PDFs reside in the ignored `papers/` folder.

Every content slide has three academic paragraphs and a complete teaching transcript. Full verified references and DOI links are in speaker notes, including supplementary anatomy images. All slide and note text uses Arial. Established physiology is distinguished from proposed ecological explanations, and the cited release experiments are not used to invent transmitter identities.

## Rebuild and check

Use Python with python-pptx, Pillow, PyMuPDF and requests; pdftoppm and LibreOffice are available for cropping and visual review. Original PDFs must be present at the paths in the crop manifests.

```bash
python write_spec.py
python ../../tools/build_lecture.py lecture.json
python finalize.py
python ../../tools/check_lecture.py Neuroethology_Lecture20_FA2026.pptx --lecture 20
python validate.py
```

The course builder runs first; finalization preserves the title as one exact paragraph and makes DOI links clickable in notes. `validation.json` records count, fonts, notes, crop integrity, and final visual review. All 46 slides were rendered and inspected; the course checker reports zero failures and zero warnings.

Reusable instructor prompt and strict image rules: `../../prompts/make_lecture.md`, `../../AGENTS.md`, and `../../.claude/skills/neuroethology-lecture/SKILL.md`.
