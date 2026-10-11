# Lecture 89

**Unihemispheric Sleep in Animals: Comparative brain/neuro anatomy & organization, hemispheric specialization, predator vigilance, and the neural boundaries of consciousness**

Date TBD. 46 slides.

- [Download editable PowerPoint](Neuroethology_Lecture89_FA2026.pptx)
- [Static PDF preview](Neuroethology_Lecture89_FA2026_preview.pdf)

Eight original article-provided recordings are embedded on seven slides:

- Slide 3: Pophale et al. (2023), Supplementary Videos 1 and 2, matched octopus active-sleep and waking recordings.
- Slide 14: Lyamin et al. (2005), Supplementary Video, orca mother and calf four weeks postpartum.
- Slides 34 and 35: Rattenborg et al. (2016), Supplementary Movies 2 and 3, authors’ published visualizations of recorded flight trajectories.
- Slide 37: Rattenborg et al. (2016), Supplementary Movie 4, awake preening in a magnificent frigatebird, not EEG-confirmed REM.
- Slide 40: Ungurean et al. (2023), Supplementary Movie 1, pigeon NREM–REM–NREM transition during fMRI.
- Slide 45: Pophale et al. (2023), Supplementary Video 4, paired skin patterns during waking and active sleep.

The octopus clips are comparative controls for behavioral state classification and consciousness claims, not evidence of unihemispheric sleep. Only slides 3, 14 and 45 received targeted body-text changes; all titles, original figures, the theme and the 46-slide sequence were retained. Inaccessible jackdaw/elephant-seal supplements and defective frigatebird Movie 1 remain documented in `media_sources.json`; no clips were duplicated to reach the count.

Click each recording in PowerPoint Slide Show. The PDF is a static preview. Full video decode and PPTX media relationships were checked; interactive PowerPoint playback was unavailable. The high-resolution octopus recordings were encoded at 720p with full timing and audio retained so the entire PPTX stays below 40 MB. Posters are unedited frames from the original files.

Rebuild with `python lectures/L89/write_spec.py`, `python tools/build_lecture.py lectures/L89/lecture.json`, then `python lectures/L89/embed_media.py`. The compatible recordings are committed. Crop originals are documented in `crops.json`; source PDFs remain in ignored `papers/`. `RESUME_PROMPT.md` preserves the instructor’s strict no-created-images requirement and current teaching rules.

To redownload/re-encode recordings, run `python lectures/L89/prepare_media.py` and `python lectures/L89/prepare_extra_media.py` before rebuilding and embedding.
