# Lecture 85 complete

The exact title supplied at the beginning of the instructor’s request is registered as special topic 85 in course/schedule.json, with Date TBD. Existing lecture titles are preserved. A new mineral-blue-paper palette is recorded for Lecture 85.

This lecture adapts the cross-species primary-paper synthesis in current default-branch Lecture 83, rather than introducing unsupported new studies. Fruit flies, honey bees, praying mantises, cockroaches, blowflies, zebrafish, mice and rats are covered. The 44 content slides retain the same scientific teaching content and speaker transcripts, under the instructor’s newly requested lecture number and title.

All article crops remain unchanged. Original study recordings have provenance checks; compatibility conversions preserve dimensions, scene and timing. No scientific images were created, redrawn, recolored or reconstructed. Nine useful article-provided videos are embedded with source URLs, credits, licenses, full scene/timing preservation, and credited static fallbacks. The optional damaged mantis recording remains excluded with the original source URL in the notes.

The repository builder and checker passed with 46 slides, 44 article-figure slides, 36 color-image slides, zero failures and zero warnings. All 46 initial rendered slides were reviewed; the four slides changed by this revision were rendered and reviewed again. Embedded-media hashes and relationships were verified. The recorded original media already passed complete decode checks in this task before copying to Lecture 85; the compact-copy exporter also verifies every converted stream with ffmpeg.

During the initial build, fresh web search, publisher access and Presenton were blocked by network policy (HTTP 403); the repository’s documented sources and figure assets were used. During this video revision, Europe PMC full-text XML and original article supplements became accessible. Four additional source recordings were downloaded, checked against publisher MD5 metadata, decoded fully, and embedded. The ignored original PDFs are not restored in this machine. No new source-PDF cropping was attempted or required for this adaptation.

Interactive Microsoft PowerPoint playback is unavailable. Use PowerPoint Slide Show and click recordings on slides 2, 3, 5, 6, 23, 24, 27, 38 and 39. The PDF is a static preview and does not play video. Arial remains in the PPTX; LibreOffice’s local preview substitutes Liberation Sans.

Rebuild with:

    python tools/build_lecture.py lectures/L85/lecture.json
    python lectures/L85/embed_media.py
    python tools/check_lecture.py lectures/L85/Neuroethology_Lecture85_FA2026.pptx --lecture 85
    python lectures/L85/export_compact.py

PROMPT.md preserves the current instructor rules. PAPERS.md, research.json, figure_sources.json and media_sources.json preserve the source record. The compact copy compresses videos for delivery while preserving all scientific figure/slide parts; video details can appear softer than in the full-size copy.

Video revision: nine recordings meet the usual 8–10 target. The compact delivery copy is about 43 MB; its filename no longer claims it is under 40 MB. All nine compressed streams passed full decoding, and all slide, figure, theme and relationship parts match the full copy. The 8–10 target is saved in repository guidelines and reusable prompts.
