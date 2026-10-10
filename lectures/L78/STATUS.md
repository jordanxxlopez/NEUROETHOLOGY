# Lecture 78 complete

The connected repository default branch was fetched and used as the authoritative version. The exact schedule title and Date TBD are preserved. Updated teaching-paragraph rules, meaningful caveats only, no em dashes in slide text, teaching transcripts, and original-source image rules govern this lecture.

All seven primary papers are available and verified, including the three uploaded papers. The deck contains 46 slides: one title, 44 content slides, and six exam-level points on the final Key takeaways slide. Each content slide has three teaching paragraphs, a teaching transcript, and full DOI references in its notes. Original article figures appear on all 44 content slides; 32 carry color images. Forty-eight unique article crops preserve source panel letters, axes, and scale bars. One unchanged, credited Allen Mouse Brain Atlas plate provides clearly identified comparative anatomy on five dopamine slides. No figure was generated, redrawn, or recolored.

The smoke rose / paper white theme is recorded as used in course/themes.json. Arial is used throughout. The repository checker reports zero failures and zero warnings. All 46 slides were rendered and visually reviewed, with revised crops and captions rechecked. Source records, figure inventory, provenance, the reusable prompt, build specification, and validation record are saved alongside the PPTX. No PDFs remain outstanding.

Rebuild and check from the repository root:

```bash
python lectures/L78/prepare_figures.py
python lectures/L78/write_spec.py
python tools/build_lecture.py lectures/L78/lecture.json
python tools/check_lecture.py lectures/L78/Neuroethology_Lecture78_FA2026.pptx --lecture 78
```

The seven source PDFs belong in lectures/L78/papers and are excluded from Git. Source identities and acquisition records are in research.json and PAPERS.md. Figure reproduction uses the repository crop tool. The validated cloud environment includes the required Python libraries, Poppler, and LibreOffice; no configuration or credential changes were needed.
