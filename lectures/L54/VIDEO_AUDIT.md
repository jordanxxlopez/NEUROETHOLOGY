# Lecture 54 article-video revision

The user-uploaded 46-slide deck is preserved in baseline commit `06cccc7`. All original slide shape XML, text, figures, positions, fonts and original notes are retained. This revision adds six click-to-play movies and short credits to existing slides, with full references, sources, licenses and context appended to notes. It does not rebuild or rewrite the older lecture.

| Slide | Primary article supplement | Teaching use |
|---|---|---|
| 3 | Somppi et al. (2016), S1 Movie | Trained dog and contact-free eye-tracking measurement session |
| 7 | Somppi et al. (2016), S2 Movie | Actual stimulus block and author-supplied gaze paths |
| 10 | Humphrey et al. (2020), Supplementary Information 3 video | Human–cat slow-blink comparison with nonthreatening communication |
| 11 | Humphrey et al. (2020), Supplementary Information 2 video | Human–cat slow-blink demonstration, distinct from purring |
| 13 | Wan et al. (2012), Video S2 | Expert-consensus fearful dog stimulus |
| 14 | Wan et al. (2012), Video S1 | Expert-consensus happy dog stimulus, for comparison |

The Wan and Humphrey clips are from related primary studies, not recordings of the Salonen or Quaranta experiments discussed in those slides. The visible credits and appended notes identify that distinction. The Humphrey videos are publisher-provided demonstrations; they are not measurements of the neural circuits discussed later in the lecture. Wan's clips are article-supplied research stimuli, collected by the study from videographers and dog behavior professionals.

Sources are the original PLOS supplementary downloads and the Springer Nature player embedded in the Scientific Reports article. No YouTube, social-media or generic website videos were used. Stable original article/supplement URLs, exact identifiers, reference metadata, license, conversion details and SHA256 hashes appear in `media_sources.json`. Crossref metadata was checked for Wan and Humphrey; Somppi's bibliographic reference was checked against the original article.

## Other cited studies checked

- Quaranta et al. (2020), DOI 10.3390/ani10071107: accessible full-text supplement list contains a PDF, not a movie.
- Salonen et al. (2020), DOI 10.1038/s41598-020-59837-z: publisher supplement is a PDF, not a movie.
- van der Leij et al. (2019), DOI 10.1371/journal.pone.0223492: article appendices contain no downloadable movie.
- Bhatt et al. (2008), DOI 10.1016/j.bbi.2007.07.011, and Bhatt et al. (2009), DOI 10.1016/j.neuroscience.2009.07.050: Europe PMC records report no supplements.
- Lu et al. (1992), DOI 10.1016/0006-8993(92)90351-9, and Cheu & Siegel (1998), DOI 10.1016/s0006-8993(97)01357-7: no verified original movie was located. No unrelated circuit video was substituted.

## Reproduction and verification

Run `/workspace/lecture-venv/bin/python lectures/L54/embed_video.py` from the repository with baseline commit and media files available. The script verifies 46 slides, byte-equivalent original shape XML, original notes retained, six actual embedded MP4 payloads, hashes and video relationships. All six media files were completely decoded with FFmpeg. The original article figure is the movie poster and remains intact underneath as a static fallback. Click the figure in PowerPoint Slide Show for full-screen playback. Actual PowerPoint GUI playback was unavailable for testing.

This preservation-only edit does not assert that the historical slide prose passes the newer caveat-ending or em-dash rules. A content rewrite would be a separate task.
