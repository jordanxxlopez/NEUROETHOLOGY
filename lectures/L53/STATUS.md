# Lecture 53 — complete

Built from the connected repository default branch (base 392e085f06abdb1981b58002a46bed3fb6e0e925) using tools/build_lecture.py. The exact instructor title is registered under special_topics in course/schedule.json with Date TBD; existing titles were preserved.

The PPTX contains 46 slides: one title, 44 content and six exam-level key takeaways on the final slide. All 44 content slides carry original article figures; 28 carry color figures. No generated, redrawn or recolored images and no web photos were used. Arial and the new faded bordeaux / paper white theme are used; theme 53 is recorded in course/themes.json.

Web searches, Europe PMC literature searches and Crossref citation verification identified 12 primary articles. Eight PDFs were downloaded and four were supplied by the instructor. Their verified metadata, DOI references and PDF SHA-256 digests are in research.json. All 55 source crops were visually inspected against article pages; clipped labels and stray neighboring text were corrected. Source PDF pages and crop coordinates are recorded in crops.json and figure_sources.json. PDFs are intentionally ignored by Git.

The repository checker reports zero failures and zero warnings. LibreOffice exported 46 PDF pages. Every rendered slide was visually inspected for text overflow, crop integrity and caption/footer separation. Full DOI references and teaching transcripts are in the speaker notes. PROMPT.md records the reusable instructions; AGENTS.md and the lecture skill now retain the instructor's strict inaccessible-PDF rule for special topics as well.

Rebuild: python lectures/L53/write_spec.py && python tools/build_lecture.py lectures/L53/lecture.json
Recrop, with source PDFs present: python tools/crop_panels.py lectures/L53/crops.json
