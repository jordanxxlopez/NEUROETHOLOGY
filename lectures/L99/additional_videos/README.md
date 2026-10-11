# Lecture 99 additional-video revision

Requested change: add seven academic and three aesthetic video clips, preserving existing text, figures, theme, slide count, and all eleven embedded recordings. The three aesthetic clips are an explicit lecture-specific exception authorized by the instructor; the general research-source rule remains in force.

`prepare_academic.py` adds the seven downloaded academic recordings in existing whitespace, without repositioning or changing old shapes. It checks canonical XML equality for all old shapes and byte equality for all existing media. The working binary is in the ignored `../deliverables/` folder. Research downloads and video analysis remain in `/workspace/l99-extra-videos/` outside Git. `ACADEMIC.json` records the prepared source URLs, DOI, credits, processing, hashes and placements. See `UPLOADS.md` for the three blocked files needed before final delivery.

Uploaded-source revision: `prepare_uploaded.py` trims and fits two uploaded MBARI recordings on slides 11 and 40, using native H.264/AAC stream copy. `UPLOADED.json` records original and extracted hashes, intervals, credits, movie geometry and probes. All old shapes and 75 existing media parts are unchanged. The third upload exceeds 32 MiB and is pending a short native-quality excerpt; see the current header in `UPLOADS.md`. No final 21-video PPTX has been published.
