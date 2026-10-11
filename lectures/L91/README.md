# Lecture 91

**Sea lions: brain/neuro anatomy/organization, rhythmic entrainment, auditory–motor coordination, learned commands, and tests of beat synchronization**

50 slides, using the previously authorized four extra Ronan slides. The updated teaching material covers somatosensory anatomy, state-dependent EEG, task-specific whisker control, ball balancing, coordinated flipper movements, Lo’s task commands, Hama’s demonstrated and delayed actions, and the Ronan rhythm experiments. Slides 41–43 remain unchanged.

Ten videos are embedded on slides 10, 12, 13, 14, 15, 17, 20, 41, 42, and 43. There are nine qualifying study recordings plus the separately excluded Ronan feature. This is one short of the requested ten-study-video minimum. The brief ball-balancing source lasts 0.74 s at its original 300 fps; its speed is unchanged.

`Neuroethology_Lecture91_FA2026.pptx` is the complete editable deck with native media. The PDF preview is static and contains posters. Open the PPTX in desktop PowerPoint and click a movie to play it. Native display ratios are retained, and the media/figure layouts keep the two distinct. Actual desktop playback and Google Slides import remain untested. Google Slides may require separate MP4 insertion from Google Drive after importing.

Original-source URLs, study identifiers, credits, licenses, and hashes are in `media_sources.json`. All source video frames, dimensions, presentation timing, and audio were preserved during compatibility/delivery conversion; evidence is in `media_conversion_audit.json`. The instructor’s compressed Ronan MP4 is embedded byte-for-byte. Original PDF crops are specified in `crops.json`; PDFs are ignored by Git.

Rebuild from the repository root:

```bash
python lectures/L91/write_spec.py
python tools/build_lecture.py lectures/L91/lecture.json
python lectures/L91/embed_videos.py
python tools/check_lecture.py lectures/L91/Neuroethology_Lecture91_FA2026.pptx --lecture 91 --content-slides 48
```

The builder supplies the exact title/date from the updated schedule, Arial typography, and the retained smoked-steel theme. Embedding must follow a fresh build to prevent duplicate videos. The supplemental embedding script checks that source figures and visible text survive its layout changes.
