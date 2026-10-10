# Lecture 79 complete

Exact title and Date TBD registered from the instructor’s request, using the latest default branch. Built with tools/build_lecture.py, then embedded the author-provided vehicle recording on slide 2.

46 slides; 44 illustrated content slides: 44 with primary article figures; slide 2 also embeds the original author video over its intact static figure fallback. 38 article slides carry color. Arial; new muted carmine / chalk white theme. Updated teaching-first writing and no em dashes. Checker: zero failures and warnings. All native and HTML slides reviewed, with no text beyond slide boundaries. Full verified references and teaching transcripts are in the notes.

The native PPTX embeds an approximately 13-second H.264 recording from the lab repository cited by Givon (2022), not YouTube. The hosted Presenton PPTX and preview are static, with the original setup figure in place of video. Native playback requires desktop PowerPoint Slide Show; package and decoder validation passed, but this workspace cannot test the PowerPoint UI.

Rebuild: python write_spec.py; python ../../tools/build_lecture.py lecture.json; python embed_video.py. PDFs are local uncommitted sources. Run rebuild_figures.py from this directory to reproduce crops.
