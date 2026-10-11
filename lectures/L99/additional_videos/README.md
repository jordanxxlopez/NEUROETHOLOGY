# PowerPoint repair-prompt fix

The previous package contained `ppt/media/media18.`, an embedded MP4 part with a trailing period and no extension. It came from the extensionless research download filename `finalprobe2`. `fix_package_names.py` renames it to `media18.mp4` and updates the two slide-4 relationship targets and the content-type entry. All other package parts, including every slide XML, notes, layout, poster and movie bytes, are unchanged. The academic preparation script now supplies a `.mp4` input filename to prevent recurrence. Validation includes part-name syntax, duplicate ZIP members, relationship targets, shape/timing IDs, video extensions, byte preservation, repository rules and OpenXML schema. Desktop PowerPoint opening is not available here, so repair-free opening on a Mac cannot be directly confirmed.

# Prior 21-video revision

# Completed 21-video revision

`complete_videos.py` adds the final uploaded MBARI excerpt to slide 45. The three credited aesthetic/general-science clips are on slides 11, 40 and 45. Seven academic additions remain on slides 4, 9, 25, 28, 32, 33 and 34. Original text, figures, titles, theme and eleven movies are preserved. Final source metadata is in `FINAL_VIDEOS.json`; final frame, package, preservation, layout, repository and OpenXML validation reports are beside it. Native desktop PowerPoint playback is not tested in this cloud environment.

# Earlier preparation records

# Lecture 99 additional-video revision

Requested change: add seven academic and three aesthetic video clips, preserving existing text, figures, theme, slide count, and all eleven embedded recordings. The three aesthetic clips are an explicit lecture-specific exception authorized by the instructor; the general research-source rule remains in force.

`prepare_academic.py` adds the seven downloaded academic recordings in existing whitespace, without repositioning or changing old shapes. It checks canonical XML equality for all old shapes and byte equality for all existing media. The working binary is in the ignored `../deliverables/` folder. Research downloads and video analysis remain in `/workspace/l99-extra-videos/` outside Git. `ACADEMIC.json` records the prepared source URLs, DOI, credits, processing, hashes and placements. See `UPLOADS.md` for the three blocked files needed before final delivery.

Uploaded-source revision: `prepare_uploaded.py` trims and fits two uploaded MBARI recordings on slides 11 and 40, using native H.264/AAC stream copy. `UPLOADED.json` records original and extracted hashes, intervals, credits, movie geometry and probes. All old shapes and 75 existing media parts are unchanged. The third upload exceeds 32 MiB and is pending a short native-quality excerpt; see the current header in `UPLOADS.md`. No final 21-video PPTX has been published.
