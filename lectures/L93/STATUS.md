# Lecture 93 complete

46 slides: exact registered title, 44 content slides, and six exam-level key takeaways. Date TBD matches course/schedule.json. All 44 content slides carry published primary-paper figures, and 36 carry source color after embedding. Arial and a new smoke blue / chalk white palette are used throughout.

Fifteen distinct original study videos are embedded. Slides 5, 8, 10, 13 and 14 each contain two independently playable comparison clips; slides 18, 20, 22, 29 and 31 each contain one clip. Five additional recordings were added at the instructor's request. The ten ape recordings cover communicative entry, absent entry, grooming and play exits, absent exit, and unilateral versus mutual exit. These are distinct source recordings, not duplicated footage. Three larynx movies and two added ape recordings have no audio tracks; other source tracks include quiet or effectively silent recordings. All original audio is retained. Video credit, source URLs, DOI, licenses, durations, audio checks and hashes are recorded in media_sources.json and notes.

The title photograph is a newly used chimpanzee facial image cropped from Oña et al. (2019), Fig. 1. Its source and comparison with 50 earlier decks and 2169 distinct images are in title_source_uniqueness.json. Content figures may recur under the instructor’s first-slide-only rule.

The repository checker reports zero failures and warnings. Every slide and all used source crops were visually reviewed initially; the five revised paired-video slides were rendered and visually reviewed again. All fifteen complete clips decoded, and the embedded files, media relationships, timing nodes and display proportions were verified. Desktop PowerPoint interactive playback was unavailable; PDF rendering is static. Click each embedded recording in PowerPoint Slide Show.

Rebuild: run write_spec.py, tools/crop_panels.py with crops.json, tools/build_lecture.py with lecture.json, and then embed_media.py. Rebuild the baseline before embedding again. PDFs are excluded from version control; media files and published crops are included.
