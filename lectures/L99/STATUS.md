# Current delivery: corrected 21-video package

The embedded MP4 part with invalid trailing-period filename has been renamed to `.mp4`; its relationships and content-type reference are corrected. All 46 slide XML files, notes, layouts, images and 21 videos remain byte-for-byte unchanged. The corrected package passes strict internal part-name and relationship checks. See `additional_videos/repair_fix_validation.json` and the current browser download in DOWNLOAD.md. Desktop PowerPoint opening cannot be tested in this cloud environment.

# Previous delivery record

# Completed 21-video Lecture 99 revision

46 slides, a single final Key takeaways slide, 21 embedded recordings. Seven additional academic videos and three uploaded MBARI excerpts have been added without changing existing text, figures, theme, titles, layout or the original eleven videos. All uploads are resolved. Native source frames and audio are preserved; the MBARI excerpts are 1920 × 1080. Final OpenXML validation has zero errors; the repository checker has zero failures and warnings. Movie count, internal relationships, ZIP integrity, source-frame identity and existing-media preservation pass. Final source records and validation reports are in `additional_videos/`. Native desktop PowerPoint playback is untested.

# Original delivered-deck record

# Lecture 99 complete

46 slides: one title, 44 content, one final Key takeaways. All 44 content slides carry original published figures. Eleven distinct article-linked videos are embedded, with credited static fallbacks.

All 132 body paragraphs have five complete sentences and at least six rendered lines. No routine limitation endings or scaffolding were detected. Figure crops, references, teaching transcripts and media metadata are recorded in this folder. The title-animal source passed the earlier-lecture source audit and comparison with 5,479 available earlier images.

Theme: abyssal blue / white paper, newly added to the palette pool because the existing palettes were used, and recorded for Lecture 99. Arial throughout; ordinary text black, titles and bold terms in the required darker theme shade.

Source files are retained at /workspace/l99-research. PDFs and original movies are not committed as ordinary Git objects. The final download uses Git LFS so all embedded recordings stay inside a self-contained PPTX. Native desktop PowerPoint playback is untested; validation reports distinguish structural validation, media decoding and static rendering.
