# Lecture 87 complete

The instructor’s exact title is registered as special topic 87 with Date TBD. Existing schedule titles are preserved. Current default-branch guidelines, templates, crop tools and tools/build_lecture.py were used. The new granite-blue-paper palette is recorded as used.

The lecture contains 46 slides: one title, 44 content, and six exam-level key takeaways. Every content slide has three academic paragraphs, a teaching transcript and full DOI references. All 44 content slides carry primary-article figures; 32 have color article figures before video posters, and 39 have color images in the finished deck. No scientific image was created, redrawn, recolored or reconstructed.

Fresh scholarly web searches used Europe PMC. Original article PDFs and full-text XML were downloaded and inspected; all PDFs required for the deck were available. PAPERS.md, research.json, web_search_log.json, crops.json and figure_sources.json record citations and provenance. Original PDFs are retained in the ignored papers directory.

Ten distinct original article-provided recordings are embedded on slides 30, 31, 32, 35, 36, 37, 38, 43, 44 and 45. Each has a DOI, original source URL, credit, license, teaching purpose, unedited source-frame poster and published static figure. The two tactile-contact scenes were visually checked against the article’s protocol: Supplementary Video 1 is free form (slide 45); Supplementary Video 2 is imposed contact (slide 44). No online video player is required.

Compatibility conversion uses H.264 and AAC where present, preserving full scenes, original frame dimensions, timing and audio content. Larger recordings were compressed for delivery without cropping or resizing. Publisher checksums, complete media decode, saved-file hashes, embedded relationships and playback timing nodes were checked. Interactive Microsoft PowerPoint playback is unavailable in this environment. In desktop PowerPoint, enter Slide Show and click the recording. The PDF preview is static and cannot play the embedded videos.

The repository builder and final checker report zero failures and zero warnings. All 46 final rendered slides were visually reviewed for overflow, intact figures, caption placement and video posters. The PPTX uses Arial; the local LibreOffice preview substitutes an available compatible font.

Rebuild:

    python lectures/L87/write_spec.py
    python tools/build_lecture.py lectures/L87/lecture.json
    python lectures/L87/embed_media.py
    python tools/check_lecture.py lectures/L87/Neuroethology_Lecture87_FA2026.pptx --lecture 87

Repository guidelines and reusable prompts now explicitly preserve the target of 8–10 original study recordings per lecture, with 10 preferred and 8 acceptable. PROMPT.md stores the Lecture 87 prompt.
