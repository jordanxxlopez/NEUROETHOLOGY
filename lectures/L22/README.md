# NEUR 411 Lecture 22

**Electroreception III: the jamming avoidance response (Heiligenberg)**  
**Friday, October 16, 2026**

The connected repository’s default branch was refreshed and merged through commit `c368aec`. No ZIP was used. Lecture 21 and repository reference decks were reviewed; this lecture concentrates on the JAR’s amplitude/phase cues, time-comparison pathway, sign-sensitive neurons, separate motor pathways, receptor pharmacology and competing amplitude-only explanations.

The deck has 46 slides: one title, 44 content and six exam-level key takeaways on one final slide. Every content slide has three academic paragraphs, an original published figure, and a teaching transcript with complete DOI references. The native PowerPoint has editable text, Arial throughout and the unused ink/cherry palette. Forty-nine original figure crops are embedded, including the title animal and supporting anatomy. See PAPERS.md and sources/provenance.json for sources and classification.

## Rebuild

Install the repository requirements, PyMuPDF, poppler and LibreOffice. Restore the original PDFs in the ignored `papers/` directory using the verified sources and hashes. Then run from the repository root:

```bash
python lectures/L22/crop_all.py
python lectures/L22/write_spec.py
python tools/build_lecture.py lectures/L22/lecture.json
python lectures/L22/finalize.py
python tools/check_lecture.py lectures/L22/Neuroethology_Lecture22_FA2026.pptx --lecture 22
python lectures/L22/validate.py
soffice --headless --convert-to pdf lectures/L22/Neuroethology_Lecture22_FA2026.pptx
```

`crop_all.py` invokes the required repository crop tool. Its only subsequent operation is lossless reorientation of two figures printed sideways in the original paper; it never draws or modifies scientific data. `finalize.py` preserves the character-exact scheduled title, applies Arial to notes and adds clickable DOI links. Visual review covered all 46 rendered slides and the source crops; wrapped content headings were shortened to prevent collisions. The exact lecture title was preserved.

The delivery service exports fresh PPTX and PDF downloads and a shareable preview from the same final Arial design and source images. Temporary export HTML is deleted after delivery.
