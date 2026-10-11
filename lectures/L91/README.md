# Lecture 91

Sea lions: rhythmic entrainment, auditory–motor coordination, and experimental tests of beat synchronization

46-slide PPTX with ten non-Ronan article-supplement recordings plus one Ronan research movie. Original titles, body text, and scientific figure pixels are unchanged. Only the video-slide right columns were rearranged. The PDF is a static preview. Separate MP4s are in media/; source credits, licenses, citations, and compatibility notes are in MEDIA.md and media_sources.json. The supplied YouTube feature still needs an original-file upload.

Rebuild:

```sh
python lectures/L91/write_spec.py
python tools/build_lecture.py lectures/L91/lecture.json
python lectures/L91/embed_videos.py
python tools/check_lecture.py lectures/L91/Neuroethology_Lecture91_FA2026.pptx --lecture 91
```

Source PDFs remain ignored in papers/. Crop manifest: crops.json. Additional video teaching and references: additional_videos.json. Native timing/frame-count audit: media_conversion_audit.json.
