# Lecture 91: expanded Sea Lions I revision

The instructor requested all five Ito et al. (2022) slides be restored after the later brain/hearing revision, without replacing that revision. The deck now contains 51 slides: title, 49 content slides, and final Key takeaways. It retains the original title, date, Arial typography, and smoked-steel-paper theme.

Slides 1–45 are byte-identical to the latest Lecture 91 deck at commit `6c0ae35adcda4f0ff2e1bb5de7cb9009d2e92094`. Slides 46–50 restore the five dedicated Ito slides from commit `bc97bb7af733ffd501e9bd24f1b5b61152187d89`, formerly numbered 41–45. Their original article figures are preserved. All 17 existing videos and the three restored Ito movies retain their original embedded bytes. Takeaways are last, on slide 51; the final point now covers comparative rhythm and neural adaptation.

The restored rat/human slide and notes correct an overgeneralization about prediction: rat movement peaks were more reactive than human peaks, although rising jerk preceded some beats. Movie S2 notes distinguish the freely moving standing-rat/pop-music preparation from the Mozart head-accelerometer experiment. Source: Ito et al. (2022), Science Advances 8:eabo7019, https://doi.org/10.1126/sciadv.abo7019.

## Reproduce and verify

`python lectures/L91/expand_ito.py` downloads the two pinned source decks into ignored research scratch space and preserves their native slide and media relationships. This revision uses a package merge rather than rebuilding the unchanged slides, preserving the released formatting and videos exactly. `lecture_expanded.json` records the combined source specification and the explicit content-count exception; the 43 referenced source images are included. Embedded media provenance is in `media_sources_expanded.json`.

`python tools/check_lecture.py lectures/L91/Neuroethology_Lecture91_FA2026_Expanded_51Slides.pptx --lecture 91 --content-slides 49`

Verified: 51 slides; 49 content slides with original article figures; 39 with color figures; 20 embedded MP4 files; all internal package relationships resolve; original slides 1–45 and existing video bytes are unchanged. Actual playback in Microsoft PowerPoint has not been tested in this environment. The PDF preview is static and does not play videos.
