# Lecture 91

Sea lions: rhythmic entrainment, auditory–motor coordination, and experimental tests of beat synchronization

46-slide sea-lion-only media revision. One original sea-lion experiment recording is embedded on slide 20. All other-animal video additions were removed; original lecture teaching text and scientific figures remain unchanged. The separate MP4 is in media/. The PDF is a static preview. See MEDIA.md for credits, viewer limitations, and the original sea-lion recordings needed to meet the 10–12-video target.

Rebuild:

```sh
python lectures/L91/write_spec.py
python tools/build_lecture.py lectures/L91/lecture.json
python lectures/L91/embed_videos.py
python tools/check_lecture.py lectures/L91/Neuroethology_Lecture91_FA2026.pptx --lecture 91
```

Source PDFs remain ignored in papers/. Crop manifest: crops.json. The original 2025 study-video links on slides 17 and 39 are links, not embedded recordings.
