# Rebuild Lecture 81

Use the current default branch of jordanxxlopez/NEUROETHOLOGY and its AGENTS.md and neuroethology-lecture skill. Preserve the exact Lecture 81 title and Date TBD from course/schedule.json. Build 46 slides with 44 content slides and six exam-level takeaways using tools/build_lecture.py.

Every paragraph teaches mechanisms, relationships, experimental results, or behavior. Include a limitation only when it changes the scientific conclusion. Never use a fixed method-result-limitation ending or an em dash in visible slide text.

Use only intact original published article panels cropped with the repository tools, or permitted credited real images where needed. Never create, redraw, replot, recolor, generate, or substitute a scientific figure. Preserve panel letters, axes, units, scales, and exact DOI provenance. Stop for any essential inaccessible PDF and request an upload. At least 40 content slides carry images and 34 carry primary-paper figures; prefer color from the original source. Include anatomy for structures discussed.

Distinguish acoustic sensing with neural stimulation from decoding brain signals. Distinguish offline prediction from an operating real-time interface. Teach dopamine error signaling, positive and negative reinforcement, D1/D2 behavioral roles, temporal credit assignment, evaluator/premotor circuit timing, and flexible song sequences using the secured original papers. Do not invent performance metrics or imply a deployed song prosthesis was tested in an offline decoding study.

Use the saved crops.json and figure_sources.json as the authoritative crop manifest. Run prepare_figures.py, write_spec.py, tools/build_lecture.py, and add_article_media.py in that order. Re-embed the two original article recordings after rebuilding. Verify media hashes and relationships, rerun the lecture checker, and render all slides for visual QA. Interactive PowerPoint playback remains untested in this environment.
