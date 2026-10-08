# Lecture 23

**Magnetoreception: sea turtle and migratory bird magnetic compasses**

**Monday, October 19, 2026**

Authoritative connected repository default branch refreshed through `4dfc791`; no ZIP or older checkout used. Style references and all available repository lectures were reviewed before writing.

46 slides: title, 44 content slides with three academic paragraphs each, six Key takeaways. Every content slide has an original primary-article figure; 22 image slides pass the repository color test. Arial and previously unused charcoal / brick red. Full verified references, DOI links and teaching transcripts are in speaker notes.

Build from the repository root:

```bash
python lectures/L23/crop_all.py
python lectures/L23/write_spec.py
python tools/build_lecture.py lectures/L23/lecture.json
python lectures/L23/finalize.py
python tools/check_lecture.py lectures/L23/Neuroethology_Lecture23_FA2026.pptx --lecture 23
python lectures/L23/validate.py
soffice --headless --convert-to pdf lectures/L23/Neuroethology_Lecture23_FA2026.pptx
```

The original PDFs belong in ignored `papers/`. Exact crop coordinates, panel identifiers, source DOIs and SHA256 hashes are retained in the manifests and `sources/provenance.json`. Native PowerPoint and its 46-page LibreOffice PDF were rendered and visually checked for layout and caption collisions. A fresh Presenton export supplies HTTPS PPTX/PDF downloads and a viewable preview.

Interpretive limits are taught explicitly: magnetic influence on behavior does not identify a receptor; purified Cry4 photochemistry and localization do not establish downstream neural signaling; particle-based maps remain a candidate mechanism. Published Fig. 2c in Goforth et al. labels Newfoundland/Virginia, whereas the corresponding main-text passage uses Cuba/Massachusetts. The slide describes the second learned signature pair without choosing between those inconsistent geographical labels.
