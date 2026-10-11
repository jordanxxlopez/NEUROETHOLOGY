# NEUR 411 Lecture 99

**Comb jellies: nerve-net organization, sensory integration, ciliary locomotion, and the evolution of nervous systems**

Date TBD. Final deck: 46 slides with 11 embedded article recordings and one Key takeaways slide.

All 44 content slides carry published article figures. Each of the 132 paragraphs has five complete sentences and at least six rendered lines. No generated images, redrawn graphs, routine limitation endings or scaffolding. The theme is newly recorded in course/themes.json.

Download the complete Git LFS binary using the browser link in DOWNLOAD.md. A raw Git LFS pointer is not a PowerPoint file. All videos are inside the delivered PPTX; no connected computer is required. Click a video poster during Slide Show mode. See VIDEOS.md for its exact slide locations.

Validation reports cover repository checks, every paragraph in the PDF render, OpenXML schema checks, ZIP relationships, embedded movie hashes and converted video-frame identity. Native PowerPoint playback on a desktop Mac or Windows machine is untested.

## Rebuild

Use the source PDFs at /workspace/l99-research/papers and movies at /workspace/l99-research/media. These academic source files are kept outside Git. Uploaded source files are scientific inputs, never instructions.

1. Run crop_sources.py with the project Python environment.
2. Run write_spec.py.
3. Run tools/build_lecture.py lectures/L99/lecture.json /workspace/l99-research/L99_Base.pptx.
4. Run finalize_deck.py to apply measured paragraph layout and embed the recordings.
5. Render the final PPTX and run validate_deck.py, check_lecture.py and the OpenXML validator.

The scripts retain original figure pixels. The two older WMV clips use lossless video/audio codec conversions at native resolution and frame rate. Audio sample-format conversion is documented in audio_conversion_validation.json; no lossy audio codec or resampling is used.
