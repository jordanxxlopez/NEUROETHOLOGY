# Lecture 83 delivery validation

- Repository builder and final checker: 46 slides, 44 image slides, 44 primary-article figure slides, 36 color-image slides; zero failures and zero warnings.
- Exact schedule title and Date TBD, Arial typography, muted-indigo-paper theme, teaching paragraphs and transcripts, original-figure captions and DOI references were checked.
- All 46 rendered slides were visually inspected. Corrected crops preserve panel letters, axes, units and scale bars; the final five video-bearing slides were inspected again after integration. No text overflow or caption/footer collisions remain.
- Each embedded recording fully decodes with ffmpeg without errors. Five saved MP4 hashes match media_sources.json; all corresponding slides contain video/media relationships and timing elements. The PPTX contains 46 slides after embedding.
- H.264 recordings from Stowers are retained byte-for-byte. Compatibility conversions retain original dimensions, scene, sound where present, and timing within one-frame/container rounding. Posters are unedited frames from these recordings, with duplicate static frame fallbacks below the movie objects for PDF export.
- Static PDF rendering retains the original credited figure and unedited recording-frame fallback. Interactive Microsoft PowerPoint playback was unavailable; click-to-play is configured through python-pptx movie objects. Some browser/Google Slides viewers may omit embedded playback.
- Optional mantis supplementary video sources returned decoding errors. No damaged or truncated conversion is embedded; original DOI and recording URL are supplied in slide 18 notes and media metadata.
- Final PPTX SHA-256: `574f20ad3d88504577f555b08d3438159213528177731ccb7777a63647430714`.

Rebuild with `python lectures/L83/write_spec.py`, `python tools/build_lecture.py lectures/L83/lecture.json`, then `python lectures/L83/embed_media.py`. Rerun `python tools/check_lecture.py lectures/L83/Neuroethology_Lecture83_FA2026.pptx --lecture 83`. PDF inputs remain in ignored papers/.
