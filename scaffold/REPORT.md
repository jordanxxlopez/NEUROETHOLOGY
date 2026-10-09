# Scaffold report

One section per scaffolded deck (rules: scaffold/GUIDELINE.md; checker: tools/check_scaffold.py).

## Neuroethology_Lecture1_FA2026_V2.pptx

- Output: Neuroethology_Lecture1_FA2026_V2_SCAFFOLDED.pptx / .pdf — 60 slides, PDF 60 pages
- Integrity: all 46 original slides identical to the input (slide XML, relationships, media, notes)
- Checker: PASS (count, integrity, non-redundancy, moves, sources, language, format); every scaffold slide inspected in the rendered PDF.
- Cited papers read in full for added explanation: Cormons & Zeil 2023, Hodgkin & Huxley 1952, Fehér et al. 2009, Haesler et al. 2007, Poláček et al. 2013, Barber et al. 2022.

| # | Title | After | Reused figure (slide: caption) | Integrates | Cited papers used | Moves | Run | Sim | Overlap |
|---|---|---|---|---|---|---|---|---|---|
| 7a | Moth ears answer bats now but arose for another use | 7 | 43: Barber et al. (2022), Fig. 2(A–D). A moth, tegular structures, modified scales, and emitted ultrasound. | 6, 7, 43, 45 | 10.1073/pnas.2117485119, 10.1111/j.1439-0310.1963.tb01161.x | distinction, mechanism, consequence, integration | 4 | 0.38 | 0.15 |
| 12a | Wasps search where the current view best matches a stored view | 12 | 12: Cormons & Zeil (2023), Fig. 4(A). Sequential training, landmark shifts, and digging attempts. | 2, 4, 12, 13 | 10.1371/journal.pone.0282144 | mechanism, foundation, integration, consequence | 4 | 0.25 | 0.14 |
| 14a | Panorama and local landmarks are used at the same time | 14 | 13: Cormons & Zeil (2023), Fig. 5(A–B). Barrier geometry and the sequence of landmark manipulations. | 12, 13, 14 | 10.1371/journal.pone.0282144 | distinction, method_logic, integration, consequence | 3 | 0.23 | 0.14 |
| 16a | The panorama is necessary; vision alone is sufficient locally | 16 | 15: Cormons & Zeil (2023), Fig. 6(A–B). Search distributions when local nonvisual cues were masked. | 8, 13, 14, 15, 16 | 10.1371/journal.pone.0282144, 10.1111/j.1439-0310.1963.tb01161.x | distinction, method_logic, integration, consequence | 5 | 0.23 | 0.20 |
| 19a | Clamping voltage breaks the loop between current and voltage | 19 | 18: Hodgkin & Huxley (1952), Fig. 1. The authors’ equivalent circuit for membrane currents. | 18, 19, 20, 22 | 10.1113/jphysiol.1952.sp004764 | foundation, method_logic, mechanism, integration | 4 | 0.33 | 0.19 |
| 20a | Ion gradients make sodium current inward and potassium outward | 20 | 20: Hodgkin & Huxley (1952), Fig. 2(a–b). Potassium conductance during depolarization and repolarization. | 18, 20, 22, 23 | 10.1113/jphysiol.1952.sp004764 | foundation, mechanism, method_logic, integration | 3 | 0.27 | 0.21 |
| 23a | Threshold is where sodium inflow outruns outward current | 23 | 22: Hodgkin & Huxley (1952), Fig. 6(A–L). Transient sodium conductance across depolarization levels. | 20, 21, 22, 23, 25 | 10.1113/jphysiol.1952.sp004764 | mechanism, foundation, integration, consequence | 4 | 0.25 | 0.14 |
| 25a | Refractoriness keeps a propagating impulse moving forward | 25 | 24: Hodgkin & Huxley (1952), Fig. 15(a–d). Predicted and recorded propagated action potentials. | 22, 23, 24, 25 | 10.1113/jphysiol.1952.sp004764 | mechanism, integration, consequence, foundation | 4 | 0.20 | 0.08 |
| 29a | Copying bias, not copying error, pulls song toward wild type | 29 | 28: Fehér et al. (2009), Fig. 2(g–j). Tutor–pupil spectrograms and the relationship of syllable durations. | 27, 28, 29, 30 | 10.1038/nature07994 | distinction, mechanism, integration, consequence | 6 | 0.20 | 0.10 |
| 31a | Genes set the learning bias; generations build the song | 31 | 31: Fehér et al. (2009), Fig. 4(a–e). Relationships and song change in the isolated colony. | 5, 26, 30, 31 | 10.1038/nature07994, 10.1111/j.1439-0310.1963.tb01161.x | distinction, consequence, integration, foundation | 7 | 0.24 | 0.20 |
| 34a | Each control rules out a different nonspecific explanation | 34 | 34: Haesler et al. (2007), Fig. 1(G). FoxP2 and reporter labeling in control and knockdown tissue. | 32, 33, 34, 35 | 10.1371/journal.pbio.0050321 | method_logic, distinction, integration, consequence | 3 | 0.22 | 0.19 |
| 38a | Song learning varies output, then keeps the better matches | 38 | 38: Haesler et al. (2007), Fig. 5(A–B). Imitation accuracy and variability across pupil age.; 38: Haesler et al. (2007), Fig. 1(A). Area X in a sagittal brain section; original scale bar 1 mm. | 35, 37, 38 | 10.1371/journal.pbio.0050321 | foundation, mechanism, distinction, integration | 3 | 0.33 | 0.17 |
| 42a | Failure to eject can reflect ability, not recognition | 42 | 39: Poláček et al. (2013), Fig. 1. Flat objects differing in size, color, and shape. | 39, 40, 41, 42 | 10.1371/journal.pone.0078771 | distinction, method_logic, consequence, integration | 4 | 0.33 | 0.15 |
| 44a | Palatability tests separate honest warnings from bluffs | 44 | 44: Barber et al. (2022), Fig. 3. Clusters of moth signals, taxa, and palatability categories. | 6, 9, 44 | 10.1073/pnas.2117485119 | distinction, method_logic, integration, consequence | 4 | 0.27 | 0.20 |

Run = longest word run shared with any original slide or its notes (fail at 8); Sim = highest content-word Jaccard similarity with any original sentence (fail at 0.6); Overlap = share of the slide's content words found on the most similar original slide, technical terms excluded (fail above 0.40).

### For the instructor's attention

- The uploaded file was named `Neuroethology_Lecture1_FA2026_V2_2.pptx`; it was saved as `scaffold/input/Neuroethology_Lecture1_FA2026_V2.pptx`, so outputs are named `Neuroethology_Lecture1_FA2026_V2_SCAFFOLDED.*`.
- Body text size follows the cloned slide (14 pt; 14.5 pt on the FoxP2 slides 34a and 38a), since the deck itself varies between 13 and 15 pt.
- Slide 38a also carries the Area X anatomy panel that the deck's own FoxP2 slides (33–38) place beside their main figure; 34a carries only its main figure.
- The deck's own text colors (titles #16181D, body #202329, footer #5E636D) were kept as cloned; theme_colors.py was not run, per the guideline.
- Some numbers come from the cited papers rather than the deck (each listed under `paper_numbers` in the spec): 85% of Macroheterocera with ears (7a), the 67–180 ms wild-type duration range (29a), day 25 sensory-phase onset (38a), real-egg ejection in 2 of 19 nests, 81.7% flat-object removal and 21/22 vs 4/11 removal by sex (42a).

## Neuroethology_Lecture2_FA2026_V2.pptx

- Output: Neuroethology_Lecture2_FA2026_V2_SCAFFOLDED.pptx / .pdf — 60 slides, PDF 60 pages
- Integrity: all 46 original slides identical to the input (slide XML, relationships, media, notes)
- Checker: PASS (count, integrity, non-redundancy, moves, sources, language, format); every scaffold slide inspected in the rendered PDF.
- Cited papers read in full for added explanation: Tinbergen 1948 (Zenodo PDF), James & Bell 2021, Bukhari et al. 2017. Lorenz & Tinbergen 1938 (German) was not available in full text; the goose slides draw on the deck, Tinbergen 1948 and textbook principles.

| # | Title | After | Reused figure (slide: caption) | Integrates | Cited papers used | Moves | Run | Sim | Overlap |
|---|---|---|---|---|---|---|---|---|---|
| 8a | Sign stimuli add together to set the strength of a response | 8 | 7: Tinbergen (1948), Fig. 3. Head-down threat posture and ventral-spine display at a mirror. | 3, 5, 7, 8 | 10.5281/zenodo.16185673 | mechanism, method_logic, integration, consequence | 4 | 0.20 | 0.14 |
| 10a | Each action is released by its own small set of features | 10 | 10: Tinbergen (1948), Fig. 5(A–C). A non-stickleback fish model, a normal-abdomen fish, and a swollen-abdomen dummy. | 3, 9, 10 | 10.5281/zenodo.16185673 | distinction, foundation, integration, consequence | 3 | 0.29 | 0.12 |
| 15a | Egg retrieval is a chain of steps released by different cues | 15 | 14: Lorenz & Tinbergen (1938), Fig. 1(a–b). Visual orientation followed by a bill-contact test. | 13, 14, 15, 16 | 10.1111/j.1439-0310.1939.tb01558.x, 10.5281/zenodo.16185673 | mechanism, integration, consequence, foundation | 3 | 0.28 | 0.29 |
| 20a | Three manipulations separate a fixed core from feedback | 20 | 18: Lorenz & Tinbergen (1938), Fig. 4(c–d). Escape of an oversized object followed by continued empty movement. | 17, 18, 19, 20, 22 | 10.1111/j.1439-0310.1939.tb01558.x | method_logic, distinction, integration, mechanism | 4 | 0.43 | 0.12 |
| 24a | A preset movement trades flexibility for speed and reliability | 24 | 24: Lorenz & Tinbergen (1938), Fig. 1(c–d). Inward rolling toward the nest and lifting of the transported egg. | 17, 20, 21, 23, 24 | 10.1111/j.1439-0310.1939.tb01558.x | mechanism, consequence, integration, foundation | 5 | 0.21 | 0.13 |
| 26a | Retrieval fatigue is not sensory adaptation or muscle fatigue | 26 | 25: Lorenz & Tinbergen (1938), Fig. 6(a–c). Orientation and an alternative nest-material movement after repeated retrieval. | 13, 25, 26 | 10.1111/j.1439-0310.1939.tb01558.x, 10.5281/zenodo.16185673 | distinction, method_logic, integration, mechanism | 4 | 0.33 | 0.16 |
| 28a | Innate release and later tuning answer different questions | 28 | 27: Lorenz & Tinbergen (1938), Fig. 6(d–e). Avoidance of an artificial egg after changes in response readiness. | 11, 25, 27, 28 | 10.1111/j.1439-0310.1939.tb01558.x, 10.5281/zenodo.16185673 | distinction, method_logic, integration, consequence | 4 | 0.22 | 0.20 |
| 29a | The diencephalon links social signals to hormonal output | 29 | 29: James & Bell (2021), Fig. 2(A–C). Brain visibility through the skull and dissected dorsal brain anatomy. | 29, 30, 33, 40, 42 | 10.1371/journal.pone.0251653, 10.1371/journal.pgen.1006840 | foundation, integration, method_logic | 4 | 0.33 | 0.14 |
| 32a | A disabled virus delivers a gene into adult brain cells | 32 | 31: James & Bell (2021), Fig. 3(A–B). Restricted expression after one injection and broader expression after delivery at multiple depths. | 30, 31, 32, 35 | 10.1371/journal.pone.0251653 | foundation, method_logic, distinction, mechanism | 5 | 0.33 | 0.16 |
| 35a | Acute and sustained vasotocin pushed charging in opposite ways | 35 | 35: James & Bell (2021), Fig. 8. Paired baseline and post-transfection charge counts for EYFP, AVP, and MAOA.; 35: James & Bell (2021), Fig. 2(C). Dorsal brain anatomy; original scale bar 2 mm. | 33, 34, 35, 39 | 10.1371/journal.pone.0251653 | integration, mechanism, distinction, consequence | 3 | 0.25 | 0.11 |
| 37a | Lower respiration confirms the enzyme worked as expected | 37 | 37: James & Bell (2021), Fig. 9. Paired respiration measurements in opercular beats per 20 seconds. | 34, 36, 37 | 10.1371/journal.pone.0251653 | mechanism, method_logic, integration, consequence | 3 | 0.33 | 0.21 |
| 41a | Early regulators drive later genes, producing expression waves | 41 | 41: Bukhari et al. (2017), Fig. 2(B,D). Temporal expression patterns and functional associations of telencephalic gene clusters. | 40, 41, 43, 45 | 10.1371/journal.pgen.1006840 | mechanism, foundation, integration, consequence | 5 | 0.35 | 0.22 |
| 43a | Expression data nominate genes; perturbation tests them | 43 | 43: Bukhari et al. (2017), Fig. 3. The published inferred network of transcription factors and gene clusters. | 35, 37, 41, 43 | 10.1371/journal.pgen.1006840, 10.1371/journal.pone.0251653 | distinction, method_logic, integration, consequence | 5 | 0.20 | 0.20 |
| 44a | Acetylation loosens histone grip so genes can be transcribed | 44 | 44: Bukhari et al. (2017), Fig. 4(D). Published chromatin-mark tracks near the Pparg locus. | 41, 44, 45 | 10.1371/journal.pgen.1006840 | foundation, mechanism, consequence, integration | 3 | 0.29 | 0.18 |

### For the instructor's attention

- The uploaded file was named `Neuroethology_Lecture2_FA2026_V2_2.pptx`; it was saved as `scaffold/input/Neuroethology_Lecture2_FA2026_V2.pptx`.
- Body text size follows the cloned slide: 15 pt on most scaffold slides (the deck's stickleback, goose and early James & Bell slides), 14.5 pt on 41a and 44a, 14 pt on 43a. The 16.5 pt James & Bell layout and the 11.5/12.5 pt Bukhari layouts were not used as templates (too little room, or below 13 pt).
- 35a also carries the dorsal brain anatomy panel (James & Bell 2021, Fig. 2(C)) that the deck's own slides 33–39 place beside their main figure.
- 35a reports a result the deck does not mention: in James & Bell (2021), a single vasotocin injection decreased charging at the highest dose, opposite to the increase after viral AVP expression; the slide gives the authors' timing explanation and marks it as untested.
- Numbers taken from the cited papers rather than the deck: 76 intrusions per hour in natural stickleback populations (41a, Bukhari et al. 2017).
