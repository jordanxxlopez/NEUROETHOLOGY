# Lecture 91

**Sea lions: brain/neuro anatomy/organization, rhythmic entrainment, auditory–motor coordination, learned commands, and tests of beat synchronization**

Standard 46-slide deck: title, 44 content slides, and Key takeaways. The four additional ending slides have been removed at the instructor's request. Three repetitive model slides were replaced with the instructor-uploaded sign-sequence, visual identity, and functional-class experiments. Slides 41–43, including all their text, notes, figures, movie bytes and placement, remain unchanged.

18 native embedded clips use 10 distinct sea-lion study recordings. Separate excerpts from a single recording count once toward the study-recording requirement. The Ronan UCSC feature and the longer Bimbo zoo demonstration are additional recordings, excluded from the target. The three expressly retained rat/human comparison movies are also outside the sea-lion count.

| Slide | Recording |
| --- | --- |
| 10 | Lo, task-specific exploration |
| 12 | Bimbo balancing on land and in water, 44 s observational demonstration |
| 13 | Leahy Movie 3, banking turn |
| 14 | Leahy Movie 1, captive porpoising |
| 15 | Leahy Movie 2, wild porpoising |
| 17 | Instructor-supplied UCSC Ronan feature, unchanged |
| 21 | Rouse Video 1, persistent interval change |
| 23 | Rouse Video 1, phase disturbance |
| 25 | Rouse Video 1, larger interval change and extra nod |
| 28 | Rocky, ordered signs and object transport |
| 29 | Rio, identity matching |
| 30 | Rio, stimulus-class matching |
| 32 | Hama, previously learned vocal and hand commands |
| 35 | Cook ESM 2, Ronan at 112 bpm |
| 38 | Cook ESM 2, human and sea-lion movement comparison |
| 41–43 | Preserved Ito rat/human comparison recordings |

`Neuroethology_Lecture91_FA2026.pptx` contains the actual videos; the preview PDF is static. Native proportions, scientific labels, temporal order, sound and playback speed are retained. Timing-relevant frame rates are unchanged. Delivery copies use H264/AAC compression; large video frames are proportionally resized to at most 1280 px wide. Posters are source frames, proportionally reduced for delivery. Ronan's solo 2025 excerpt removes only its black side margins. All temporal selections and this spatial crop are recorded in `segment_audit.json`.

The Rocky and Rio movies come from the original publisher's supplements to Cook, Reichmuth and Hanke's *The Mind of a Sea Lion* chapter, DOI 10.1007/978-3-030-59184-7_17. They record the trained procedures but are not identified as the particular trials measured in the earlier articles. Numerical findings and original figure crops cite the uploaded 1992, 1994 and 2001 papers. Hama's clip records familiar command responses, not delayed-Go imitation. Bimbo's clip is a zoo demonstration, not a participant in the adjacent ball-balancing experiment. The uploaded Science adi8081 movie package depicts mice and is excluded.

`media_sources.json` lists citations, original media URLs, credits, hashes, clip slides and source-count rules. `delivery_verification.json` records complete decoding, saved PPTX relationships, native display ratio checks and preservation of slides 41–43. Desktop PowerPoint GUI playback and Google Slides import remain untested. Google Slides may require uploading MP4 files to Drive and inserting them separately after import.

Rebuild from the repository root:

```bash
python lectures/L91/write_spec.py
python tools/build_lecture.py lectures/L91/lecture.json
python lectures/L91/embed_videos.py
python tools/check_lecture.py lectures/L91/Neuroethology_Lecture91_FA2026.pptx --lecture 91
```

The builder uses the exact schedule title/date, retained smoked-steel theme, Arial and the current teaching rules. A fresh build is required before embedding to prevent duplicate movies. `verify_delivery.py` optionally compares against the previous delivery saved at its documented scratch path; media decoding and embedding verification are otherwise reproducible from the supplied assets. New figure crop boxes are in `revision_crops.json` and metadata verification is in `uploaded_reference_verification.json`.
