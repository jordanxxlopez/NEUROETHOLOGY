# Lecture 74 complete

Built from the authoritative connected repository default branch with the exact schedule title and `Date TBD`. The 46-slide PowerPoint contains 44 content slides and six exam-level takeaways. Every content slide has three teaching paragraphs, an original primary-article figure, a speaker-note teaching transcript, and full DOI references.

Seven primary sources cover fish-operated vehicle navigation, visual odometry, comparative pallial lesions, freely swimming spatial neurons, boundary-vector coding, geometric navigation, and whole-body motor adaptation. The instructor’s uploaded Vargas et al. (2011) PDF supplies the previously missing geometric-navigation source. Web searches and citation checks are recorded in `search_log.json` and `research.json`.

The repository builder and checker pass with zero failures and zero warnings. All 46 rendered slides and all 40 original figure crops were inspected. Thirty content slides have original source color. Figures retain their published labels and measurements; no images were created, reconstructed or recolored. Slide text contains no em dashes, and final paragraphs teach rather than repeat routine caveats.

The new blue steel / paper white theme is recorded for Lecture 74. `qa.json` contains the final PPTX checksum and checks. `PROMPT.md` preserves the reusable updated lecture prompt. Rebuild with `python lectures/L74/write_spec.py` then `python tools/build_lecture.py lectures/L74/lecture.json`. If recropping is necessary, supply the seven original PDFs at the local paths in `crops.json` and run `python lectures/L74/prepare_figures.py`.
