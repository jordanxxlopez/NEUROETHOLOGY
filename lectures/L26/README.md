# Lecture 26

Built from the refreshed authoritative default branch (6e34a38), with the exact schedule title and Monday, October 26, 2026 date. No ZIP was used. Seven uploaded example presentations were inspected (example-review.json). All three previously missing primary papers were received from the user.

The editable deck has 46 slides: title, 44 content slides, and six exam-level key takeaways. All 44 content slides contain authentic published article panels; 33 satisfy the repository color-figure check. Arial is used throughout, with the new aluminum / Atlantic blue theme recorded in course/themes.json. Full references and teaching transcripts are in speaker notes. No visuals were generated, redrawn, replotted, or recolored.

figure-sources.json records original paper, PDF page, point bounds, figure/panel caption, DOI, original color, and source/crop hashes. crops.json is the reproducible repository crop manifest; source PDFs are retained locally in ignored papers/. Crossref records and validation results are under sources/.

Rebuild with the environment Python: run make_crops.py, write_spec.py, ../../tools/build_lecture.py lecture.json, finalize.py, and validate.py from this directory. Run the repository check_lecture.py with --lecture 26. The final deck passed those checks and all 46 rendered slides were visually inspected.
