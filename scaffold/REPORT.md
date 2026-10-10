# Scaffold report

One section per scaffolded deck (rules: scaffold/GUIDELINE.md; checker: tools/check_scaffold.py).

Closing-paragraph revision: under the rule that every paragraph teaches and no slide closes on a caveat, the last body paragraph of 28 scaffold slides in the seven decks below was rewritten as teaching content (L1 16a; L2 8a, 28a, 35a, 37a, 41a, 44a; L3 13a, 26a, 34a, 40a; L4 31a, 38a, 41a, 43a; Managed Environments I 13a, 16a, 41a, 43a; II 8a, 17a, 23a, 26a, 43a; III 04a, 32a, 35a, 39a). Titles, the other paragraphs, figures, footers and speaker notes are unchanged; caveats that matter remain in the notes. The checker now fails any scaffold slide whose last paragraph is a caveat, and the tables show the rebuilt scores.

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
| 16a | The panorama is necessary; vision alone is sufficient locally | 16 | 15: Cormons & Zeil (2023), Fig. 6(A–B). Search distributions when local nonvisual cues were masked. | 8, 13, 14, 15, 16 | 10.1371/journal.pone.0282144, 10.1111/j.1439-0310.1963.tb01161.x | distinction, method_logic, integration, consequence | 5 | 0.23 | 0.19 |
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
| 8a | Sign stimuli add together to set the strength of a response | 8 | 7: Tinbergen (1948), Fig. 3. Head-down threat posture and ventral-spine display at a mirror. | 3, 5, 7, 8 | 10.5281/zenodo.16185673 | mechanism, method_logic, integration, consequence | 4 | 0.20 | 0.16 |
| 10a | Each action is released by its own small set of features | 10 | 10: Tinbergen (1948), Fig. 5(A–C). A non-stickleback fish model, a normal-abdomen fish, and a swollen-abdomen dummy. | 3, 9, 10 | 10.5281/zenodo.16185673 | distinction, foundation, integration, consequence | 3 | 0.29 | 0.12 |
| 15a | Egg retrieval is a chain of steps released by different cues | 15 | 14: Lorenz & Tinbergen (1938), Fig. 1(a–b). Visual orientation followed by a bill-contact test. | 13, 14, 15, 16 | 10.1111/j.1439-0310.1939.tb01558.x, 10.5281/zenodo.16185673 | mechanism, integration, consequence, foundation | 3 | 0.28 | 0.29 |
| 20a | Three manipulations separate a fixed core from feedback | 20 | 18: Lorenz & Tinbergen (1938), Fig. 4(c–d). Escape of an oversized object followed by continued empty movement. | 17, 18, 19, 20, 22 | 10.1111/j.1439-0310.1939.tb01558.x | method_logic, distinction, integration, mechanism | 4 | 0.43 | 0.12 |
| 24a | A preset movement trades flexibility for speed and reliability | 24 | 24: Lorenz & Tinbergen (1938), Fig. 1(c–d). Inward rolling toward the nest and lifting of the transported egg. | 17, 20, 21, 23, 24 | 10.1111/j.1439-0310.1939.tb01558.x | mechanism, consequence, integration, foundation | 5 | 0.21 | 0.13 |
| 26a | Retrieval fatigue is not sensory adaptation or muscle fatigue | 26 | 25: Lorenz & Tinbergen (1938), Fig. 6(a–c). Orientation and an alternative nest-material movement after repeated retrieval. | 13, 25, 26 | 10.1111/j.1439-0310.1939.tb01558.x, 10.5281/zenodo.16185673 | distinction, method_logic, integration, mechanism | 4 | 0.33 | 0.16 |
| 28a | Innate release and later tuning answer different questions | 28 | 27: Lorenz & Tinbergen (1938), Fig. 6(d–e). Avoidance of an artificial egg after changes in response readiness. | 11, 25, 27, 28 | 10.1111/j.1439-0310.1939.tb01558.x, 10.5281/zenodo.16185673 | distinction, method_logic, integration, consequence | 4 | 0.22 | 0.18 |
| 29a | The diencephalon links social signals to hormonal output | 29 | 29: James & Bell (2021), Fig. 2(A–C). Brain visibility through the skull and dissected dorsal brain anatomy. | 29, 30, 33, 40, 42 | 10.1371/journal.pone.0251653, 10.1371/journal.pgen.1006840 | foundation, integration, method_logic | 4 | 0.33 | 0.14 |
| 32a | A disabled virus delivers a gene into adult brain cells | 32 | 31: James & Bell (2021), Fig. 3(A–B). Restricted expression after one injection and broader expression after delivery at multiple depths. | 30, 31, 32, 35 | 10.1371/journal.pone.0251653 | foundation, method_logic, distinction, mechanism | 5 | 0.33 | 0.16 |
| 35a | Acute and sustained vasotocin pushed charging in opposite ways | 35 | 35: James & Bell (2021), Fig. 8. Paired baseline and post-transfection charge counts for EYFP, AVP, and MAOA.; 35: James & Bell (2021), Fig. 2(C). Dorsal brain anatomy; original scale bar 2 mm. | 33, 34, 35, 39 | 10.1371/journal.pone.0251653 | integration, mechanism, distinction, consequence | 3 | 0.25 | 0.12 |
| 37a | Lower respiration confirms the enzyme worked as expected | 37 | 37: James & Bell (2021), Fig. 9. Paired respiration measurements in opercular beats per 20 seconds. | 34, 36, 37 | 10.1371/journal.pone.0251653 | mechanism, method_logic, integration, consequence | 3 | 0.33 | 0.20 |
| 41a | Early regulators drive later genes, producing expression waves | 41 | 41: Bukhari et al. (2017), Fig. 2(B,D). Temporal expression patterns and functional associations of telencephalic gene clusters. | 40, 41, 43, 45 | 10.1371/journal.pgen.1006840 | mechanism, foundation, integration, consequence | 5 | 0.35 | 0.21 |
| 43a | Expression data nominate genes; perturbation tests them | 43 | 43: Bukhari et al. (2017), Fig. 3. The published inferred network of transcription factors and gene clusters. | 35, 37, 41, 43 | 10.1371/journal.pgen.1006840, 10.1371/journal.pone.0251653 | distinction, method_logic, integration, consequence | 5 | 0.20 | 0.20 |
| 44a | Acetylation loosens histone grip so genes can be transcribed | 44 | 44: Bukhari et al. (2017), Fig. 4(D). Published chromatin-mark tracks near the Pparg locus. | 41, 44, 45 | 10.1371/journal.pgen.1006840 | foundation, mechanism, consequence, integration | 3 | 0.29 | 0.17 |

### For the instructor's attention

- The uploaded file was named `Neuroethology_Lecture2_FA2026_V2_2.pptx`; it was saved as `scaffold/input/Neuroethology_Lecture2_FA2026_V2.pptx`.
- Body text size follows the cloned slide: 15 pt on most scaffold slides (the deck's stickleback, goose and early James & Bell slides), 14.5 pt on 41a and 44a, 14 pt on 43a. The 16.5 pt James & Bell layout and the 11.5/12.5 pt Bukhari layouts were not used as templates (too little room, or below 13 pt).
- 35a also carries the dorsal brain anatomy panel (James & Bell 2021, Fig. 2(C)) that the deck's own slides 33–39 place beside their main figure.
- 35a reports a result the deck does not mention: in James & Bell (2021), a single vasotocin injection decreased charging at the highest dose, opposite to the increase after viral AVP expression; the slide gives the authors' timing explanation and marks it as untested.
- Numbers taken from the cited papers rather than the deck: 76 intrusions per hour in natural stickleback populations (41a, Bukhari et al. 2017).

## Neuroethology_Lecture3_FA2026_V2.pptx

- Output: Neuroethology_Lecture3_FA2026_V2_SCAFFOLDED.pptx / .pdf — 60 slides, PDF 60 pages
- Integrity: all 46 original slides identical to the input (slide XML, relationships, media, notes)
- Checker: PASS; every scaffold slide inspected in the rendered PDF.

| # | Title | After | Reused figure (slide: caption) | Integrates | Cited papers used | Moves | Run | Sim | Overlap |
|---|---|---|---|---|---|---|---|---|---|
| 06a | Air pushed ahead of a predator reaches the cerci first | 6 | 6: Camhi et al. (1978), Fig. 3(B). Wind trace near the behavioral response threshold. | 2, 6, 11, 33 | 10.1007/BF00656853, 10.1016/j.jinsphys.2014.07.002, 10.1016/j.jinsphys.2014.05.017 | foundation, mechanism, integration, consequence | 7 | 0.31 | 0.12 |
| 10a | Each hair moves in one plane, giving it a preferred wind axis | 10 | 10: Camhi & Tom (1978), Fig. 10. Turning after clockwise cercal rotation. | 8, 9, 10, 17 | 10.1007/BF00656852, 10.1038/s41598-021-85341-z | foundation, mechanism, integration, consequence | 5 | 0.26 | 0.14 |
| 13a | Synchronous input spikes sum more effectively downstream | 13 | 13: Olsen & Triblehorn (2014), Fig. 4(A–C). Species differences in wind-response timing. | 11, 13, 14, 15 | 10.1016/j.jinsphys.2014.07.002, 10.1016/j.jinsphys.2014.05.017 | foundation, mechanism, integration, consequence | 4 | 0.29 | 0.12 |
| 14a | Detecting wind and measuring its speed are different jobs | 14 | 12: Olsen & Triblehorn (2014), Fig. 5(A–D). Early and later afferent stimulus–response curves. | 12, 14, 33, 34 | 10.1016/j.jinsphys.2014.07.002, 10.1016/j.jinsphys.2014.05.017 | distinction, foundation, consequence, integration | 4 | 0.26 | 0.13 |
| 16a | Wide axons carry the warning to the thorax faster | 16 | 15: Booth et al. (2009), Fig. 1(A,B). Second-instar animal and its cercal sensory circuit. | 6, 15, 16, 33 | 10.1523/JNEUROSCI.1374-09.2009, 10.1016/j.jinsphys.2014.05.017 | foundation, mechanism, consequence, integration | 4 | 0.20 | 0.17 |
| 18a | A single GI's firing is ambiguous about wind direction | 18 | 17: Levi & Camhi (2000b), Fig. 1(A). Adult GI directional profiles used as model inputs. | 17, 18, 27, 30 | 10.1523/JNEUROSCI.20-10-03822.2000 | foundation, distinction, mechanism, integration | 4 | 0.20 | 0.18 |
| 26a | Winner-take-all requires strong mutual inhibition | 26 | 26: Levi & Camhi (2000a), Fig. 8(A,B). Turning changes after adding left-side GI spikes. | 23, 25, 26 | 10.1523/JNEUROSCI.20-10-03814.2000 | mechanism, distinction, integration, consequence | 6 | 0.29 | 0.16 |
| 32a | Adding, removing and replacing activity test different claims | 32 | 32: Levi & Camhi (2000b), Fig. 7(A,B). Natural GI2 firing and partial behavioral rescue. | 5, 9, 23, 26, 29, 31 | 10.1007/BF00656852, 10.1523/JNEUROSCI.20-10-03814.2000, 10.1523/JNEUROSCI.20-10-03822.2000 | distinction, method_logic, integration, consequence | 5 | 0.27 | 0.14 |
| 34a | Keeping a sensor does not mean using it for escape | 34 | 33: McGorry et al. (2014), Fig. 4. Ascending wind responses in four cockroach species. | 14, 33, 34 | 10.1016/j.jinsphys.2014.07.002, 10.1016/j.jinsphys.2014.05.017 | distinction, consequence, integration | 4 | 0.40 | 0.23 |
| 36a | Several preferred trajectories keep escape unpredictable | 36 | 35: Booth et al. (2009), Fig. 5(C–H). Juvenile trajectories by wind direction and En treatment. | 3, 4, 35, 36, 40 | 10.1523/JNEUROSCI.1374-09.2009 | consequence, integration, mechanism | 4 | 0.26 | 0.14 |
| 37a | Engrailed tells a sensory neuron which giants to contact | 37 | 37: Booth et al. (2009), Fig. 2(A,B). Second-instar En staining before and after RNAi. | 8, 10, 17, 37, 38 | 10.1523/JNEUROSCI.1374-09.2009 | mechanism, foundation, consequence, integration | 3 | 0.21 | 0.28 |
| 40a | Knock-down animals act as if rear wind came from the front | 40 | 41: Booth et al. (2009), Fig. 6(A–F). Third-instar trajectories after En reduction. | 35, 36, 37, 40, 41 | 10.1523/JNEUROSCI.1374-09.2009 | distinction, method_logic, integration, consequence | 7 | 0.42 | 0.21 |
| 43a | Deprived giants may strengthen the surviving cercal input | 43 | 43: Jankowska et al. (2021), Fig. 2(a,b). Left-cercal nerve responses over three weeks after injury. | 42, 43, 44 | 10.1038/s41598-021-85341-z | mechanism, foundation, integration, method_logic | 4 | 0.22 | 0.19 |
| 45a | Left-right decisions rely on comparing the two cerci | 45 | 44: Jankowska et al. (2021), Fig. 3(a–d). Peripheral and central responses with field exposure. | 10, 26, 43, 45 | 10.1007/BF00656852, 10.1523/JNEUROSCI.20-10-03814.2000, 10.1038/s41598-021-85341-z | mechanism, consequence, integration | 5 | 0.25 | 0.23 |

### For the instructor's attention

- Uploaded as `Neuroethology_Lecture3_FA2026_V2.pptx`; saved under the same name in `scaffold/input/`.
- Full text read: Olsen & Triblehorn 2014, McGorry et al. 2014, Jankowska et al. 2021. Camhi & Tom 1978, Camhi et al. 1978, Levi & Camhi 2000a,b and Booth et al. 2009 were not retrievable in full text (publisher pages blocked; PMC had abstracts only); slides drawing on them use the deck, the abstracts and textbook principles.
- This deck keeps all body paragraphs in one text box and zero-pads slide numbers, so scaffold numbers are written 06a, 10a, etc.; notes use the deck's typed •/– bullets.
- Bold key terms use the deck's dark-red bold style; slides cloned from templates without bold text borrow only that color.
- 37a summarizes the earlier Engrailed wiring result as Booth et al. (2009) describe it; it is not a separate citation.

## Neuroethology_Lecture4_FA2026_V2.pptx

- Output: Neuroethology_Lecture4_FA2026_V2_SCAFFOLDED.pptx / .pdf — 60 slides, PDF 60 pages
- Integrity: all 46 original slides identical to the input (slide XML, relationships, media, notes)
- Checker: PASS; every scaffold slide inspected in the rendered PDF.

| # | Title | After | Reused figure (slide: caption) | Integrates | Cited papers used | Moves | Run | Sim | Overlap |
|---|---|---|---|---|---|---|---|---|---|
| 3a | A single LG spike is enough to command a tail flip | 3 | 3: Wine & Krasne (1972), Fig. 2. Simultaneous connective and abdominal recordings of giant-fiber activity. | 3, 12, 16, 31 | 10.1242/jeb.56.1.1, 10.1523/JNEUROSCI.22-20-09078.2002, 10.1523/JNEUROSCI.11-01-00059.1991 | foundation, mechanism, integration, distinction | 4 | 0.29 | 0.12 |
| 5a | Giant circuits trade sensory guidance for speed | 5 | 5: Wine & Krasne (1972), Fig. 3(A,B). Giant-mediated initial responses followed by nongiant swimming. | 2, 4, 5, 6, 26 | 10.1242/jeb.56.1.1, 10.1523/JNEUROSCI.17-22-08867.1997 | distinction, integration, consequence, mechanism | 5 | 0.37 | 0.15 |
| 11a | Gap junctions pass both current and small molecules | 11 | 11: Herberholz et al. (2002), Fig. 2(A). LG and dye-coupled neurons in the terminal ganglion. | 9, 11, 13, 14, 20 | 10.1523/JNEUROSCI.22-20-09078.2002, 10.1523/JNEUROSCI.11-07-02117.1991 | foundation, mechanism, method_logic, integration | 6 | 0.25 | 0.20 |
| 18a | Lateral excitation makes LG recruitment self-reinforcing | 18 | 15: Herberholz et al. (2002), Fig. 4(A,B). Increasing nerve shocks recruit sensory EPSPs and afferent spikes. | 13, 14, 15, 16, 17, 18 | 10.1523/JNEUROSCI.22-20-09078.2002 | mechanism, consequence, integration, foundation | 4 | 0.22 | 0.18 |
| 21a | Rectifying junctions weaken inputs after LG depolarizes | 21 | 20: Edwards et al. (1991), Fig. 3(A–D). Interneuron A transmission and voltage-dependent LG responses. | 20, 21, 22, 25 | 10.1523/JNEUROSCI.11-07-02117.1991 | foundation, mechanism, consequence, integration | 4 | 0.29 | 0.12 |
| 28a | Shunting inhibition opens a leak that excitation must fill | 28 | 29: Vu et al. (1997), Fig. 6(A,B). Reduced attenuation of injected-current responses during picrotoxin. | 27, 28, 29, 30 | 10.1523/JNEUROSCI.17-22-08867.1997 | foundation, mechanism, integration, consequence | 4 | 0.21 | 0.21 |
| 30a | Three timing filters let only abrupt stimuli fire LG | 30 | 22: Edwards et al. (1998), Fig. 3(B). LG EPSP amplitude as a function of sensory-input delay. | 4, 15, 22, 25, 26, 28 | 10.1242/jeb.56.1.1, 10.1073/pnas.95.12.7145, 10.1523/JNEUROSCI.17-22-08867.1997, 10.1523/JNEUROSCI.22-20-09078.2002 | integration, mechanism, consequence | 3 | 0.20 | 0.18 |
| 31a | Light and a dye fill silence only the filled neuron | 31 | 31: Fraser & Heitler (1991), Fig. 1(A–C). Recordings before and during dye-mediated segmental-giant inactivation. | 7, 31, 32, 33 | 10.1523/JNEUROSCI.11-01-00059.1991 | foundation, mechanism, method_logic, integration | 4 | 0.22 | 0.18 |
| 33a | Removing a dominant pathway can unmask a hidden one | 33 | 33: Fraser & Heitler (1991), Fig. 4(A,B). Comparisons of LG and MG input after SG removal. | 31, 32, 33, 34 | 10.1523/JNEUROSCI.11-01-00059.1991 | method_logic, integration, consequence | 4 | 0.32 | 0.29 |
| 35a | Chemical synapses slow more on cooling than electrical ones | 35 | 35: Fraser & Heitler (1991), Fig. 10(A–C). Residual motor EPSPs at 20°C, 7°C, and with cadmium. | 34, 35 | 10.1523/JNEUROSCI.11-01-00059.1991 | foundation, mechanism, method_logic, integration | 3 | 0.23 | 0.20 |
| 36a | MG integrates several inputs before it commits to escape | 36 | 36: Swierzbinski & Herberholz (2018), Fig. 1(B). Antenna II-evoked connective activity and intracellular MG potentials.; 36: Swierzbinski & Herberholz (2018), Fig. 1(A). Published anatomical arrangement of antenna II input and the MG neuron. | 2, 8, 36 | 10.3389/fphys.2018.00448, 10.1242/jeb.56.1.1 | integration, mechanism, consequence, distinction | 3 | 0.25 | 0.12 |
| 38a | Early ethanol effects disinhibit escape before sedation | 38 | 38: Swierzbinski & Herberholz (2018), Fig. 3. MG potential amplitudes before, during, and after ethanol exposure. | 36, 37, 38, 39 | 10.3389/fphys.2018.00448 | integration, consequence, foundation, mechanism | 3 | 0.25 | 0.21 |
| 41a | Pretreatment tests whether two drugs share a target | 41 | 41: Swierzbinski & Herberholz (2018), Fig. 5. MG responses to muscimol followed by ethanol. | 38, 39, 40, 41 | 10.3389/fphys.2018.00448 | method_logic, foundation, integration, distinction | 4 | 0.33 | 0.13 |
| 43a | Manganese brightens images where calcium channels opened | 43 | 42: Herberholz et al. (2011), Fig. 3(A,B). Axial brain sections after antenna II stimulation and manganese injection. | 10, 42, 43, 44 | 10.3389/fnbeh.2011.00016 | foundation, mechanism, integration, consequence | 4 | 0.35 | 0.30 |

### For the instructor's attention

- Uploaded as `Neuroethology_Lecture4_FA2026_V2.pptx`; saved under the same name in `scaffold/input/`.
- Full text read: Swierzbinski & Herberholz 2018, Herberholz et al. 2011. Wine & Krasne 1972, Herberholz et al. 2002, Edwards et al. 1991 and 1998, Vu et al. 1997 and Fraser & Heitler 1991 were available as abstracts only; slides drawing on them use the deck, those abstracts and textbook principles.
- Number from a cited paper rather than the deck: about 17 mM for the US legal driving limit (38a, Swierzbinski & Herberholz 2018).
- 36a also carries the MG anatomy panel (Swierzbinski & Herberholz 2018, Fig. 1(A)) that the deck's slides 36–41 place beside their main figure.

## Animal_Behavior_in_Managed_Enviornments_I.pptx

- Output: Animal_Behavior_in_Managed_Enviornments_I_SCAFFOLDED.pptx / .pdf — 60 slides, PDF 60 pages
- Integrity: all 46 original slides identical to the input (slide XML, relationships, media, notes)
- Checker: PASS; every scaffold slide inspected in the rendered PDF.

| # | Title | After | Reused figure (slide: caption) | Integrates | Cited papers used | Moves | Run | Sim | Overlap |
|---|---|---|---|---|---|---|---|---|---|
| 5a | Pacing can arise when searching never reaches its goal | 5 | 5: Clubb & Mason (2003), Fig. 1(a–b). Natural home range, infant mortality and pacing across carnivores. | 3, 5, 26, 42, 43 | 10.1038/425473a, 10.1371/journal.pone.0144276, 10.3390/ani11092566 | mechanism, foundation, distinction, integration | 3 | 0.17 | 0.09 |
| 8a | A looming visitor resembles an attacking predator | 8 | 8: Chiew et al. (2019), Fig. 4(a–d). Penguins and the habitat areas sampled by the cameras. | 7, 8, 9, 11 | 10.3390/ani9060285, 10.3390/ani10071224 | mechanism, consequence, foundation, integration | 4 | 0.19 | 0.08 |
| 10a | Fecal hormones lag behavior by hours and average many events | 10 | 7: Chiew et al. (2019), Fig. 2. The physical barrier that increased visitor viewing distance. | 7, 10, 12, 28 | 10.3390/ani9060285, 10.3390/ani10071224 | foundation, mechanism, method_logic, distinction | 4 | 0.19 | 0.13 |
| 13a | Covering a window removed sound and vibration as well as sight | 13 | 11: Chiew et al. (2020), Fig. 2(a–b). Glass viewing windows and the visitor pathway.; 11: Chiew et al. (2020), Fig. 3. The opaque barrier used in the window-covering experiment. | 9, 11, 12, 13 | 10.3390/ani10071224 | method_logic, distinction, mechanism, integration | 3 | 0.22 | 0.15 |
| 16a | Double labeling ties activity to a defined pathway | 16 | 16: Baratta et al. (2009), Fig. 2(A–C). Prefrontal activation following controllable or uncontrollable stress.; 16: Baratta et al. (2009), Fig. 1(A–B). Dorsal raphe tracer deposit and labeled prefrontal neurons. | 14, 15, 16, 17 | 10.1111/j.1460-9568.2009.06867.x | foundation, method_logic, distinction, mechanism | 3 | 0.36 | 0.13 |
| 17a | Uncontrollable stress sensitizes serotonin neurons for days | 17 | 18: Baratta et al. (2009), Fig. 3(A–C). Prefrontal activation after prior experience with stressor control. | 14, 16, 17, 18 | 10.1111/j.1460-9568.2009.06867.x | mechanism, consequence, method_logic, integration | 5 | 0.32 | 0.12 |
| 18a | Retreats and partner choice give zoo animals a form of control | 18 | 12: Chiew et al. (2020), Fig. 1. The penguin encounter habitat and viewing areas.; 12: Chiew et al. (2020), Fig. 6(a–b). Penguin visibility across habitat areas with the window uncovered and covered. | 12, 14, 18, 31, 32 | 10.1111/j.1460-9568.2009.06867.x, 10.3390/ani10071224, 10.3390/ani11092566 | integration, distinction, consequence | 3 | 0.45 | 0.18 |
| 22a | Kinship stabilizes elephant groups by keeping ranks settled | 22 | 21: Harvey et al. (2018), Fig. 5(a–b). Directed affiliative relationships among individual elephants. | 19, 21, 22, 23 | 10.3390/ani8080132 | foundation, mechanism, distinction, consequence | 4 | 0.33 | 0.12 |
| 27a | GPS distance must be cleaned to measure purposeful travel | 27 | 27: Glaeser et al. (2021), Fig. 4(c–d). An elephant’s GPS locations in warm and cool seasons. | 3, 5, 25, 27, 35 | 10.3390/ani11092566, 10.1371/journal.pone.0150331 | method_logic, integration, distinction | 4 | 0.29 | 0.16 |
| 29a | A temporary hormone rise can signal healthy coping | 29 | 29: Glaeser et al. (2021), Fig. 5(a–d). Individual glucocorticoid metabolite concentrations across habitat phases. | 10, 28, 29, 31, 33 | 10.3390/ani11092566 | foundation, distinction, consequence, integration | 6 | 0.25 | 0.15 |
| 34a | Food that must be found turns walking into foraging | 34 | 34: Glaeser et al. (2021), Fig. 10. Interactions with food resources, enrichment objects and habitat features. | 5, 25, 26, 34, 35 | 10.3390/ani11092566, 10.1371/journal.pone.0150331 | mechanism, integration, consequence, distinction | 5 | 0.28 | 0.16 |
| 37a | Deep water serves a drive that food does not satisfy | 37 | 37: Fuller et al. (2023), Fig. 4. Time spent in different water-depth categories.; 37: Fuller et al. (2023), Fig. 2. A king penguin wearing a flipper-mounted time–depth recorder. | 36, 37, 38, 39, 41 | 10.3390/ani13142312 | foundation, consequence, integration, mechanism | 4 | 0.19 | 0.11 |
| 41a | Crowding raises aggression where penguins compete for space | 41 | 41: Fuller et al. (2023), Fig. 5. Behavioral time budgets in the two habitats.; 41: Fuller et al. (2023), Fig. 7. Rates of social and maintenance behaviors. | 22, 33, 40, 41 | 10.3390/ani13142312 | mechanism, method_logic, integration, consequence | 6 | 0.29 | 0.13 |
| 43a | Population risk factors point to causes but cannot prove them | 43 | 30: Glaeser et al. (2021), Fig. 6(a–f). Individual and combined elephant activity budgets. | 23, 30, 35, 42, 43 | 10.1371/journal.pone.0144276, 10.3390/ani8080132, 10.1371/journal.pone.0150331 | method_logic, distinction, integration | 4 | 0.30 | 0.10 |

### For the instructor's attention

- Full text read: Chiew et al. 2019 and 2020, Baratta et al. 2009, Harvey et al. 2018, Glaeser et al. 2021, Holdgate et al. 2016, Fuller et al. 2023, Greco et al. 2016. Clubb & Mason 2003 (Nature brief communication) was available as an abstract only; 5a draws on it, the deck, Greco et al. 2016 and Glaeser et al. 2021.
- Numbers from cited papers rather than the deck: a 7 h median excretion lag and a 10.8 h average peak (10a, Chiew et al. 2019); 32/17 and 10/28 affiliative/agonistic acts in spring and autumn (22a, Harvey et al. 2018); 7.3 to 14.7 km per day after removing repetitive behavior (27a), food-delivery engagement rising from 3.8% to 24.5% and total foraging at 36.6% vs 39.9% (34a, Glaeser et al. 2021); wild foraging depths of 120–150 m, a 2 m old pool and 8 m new pool, the 2–4 m and 6 m depth bands (37a, Fuller et al. 2023); 89 elephants at 39 zoos (43a, Greco et al. 2016).
- 17a uses the slide 18 layout with only the Baratta et al. (2009) Fig. 3 panel, because Fig. 1 is already used on 16a; the lower figure area is empty.
- 18a links the rat controllability circuit to penguin retreats and elephant partner choice and states explicitly that the parallel is a hypothesis, not a finding in those species.
- Several slides carry two of the deck's figures, the way the cloned slide does: 13a, 16a, 18a, 37a and 41a.

## Animal_Behavior_in_Managed_Enviornments_II.pptx

- Output: Animal_Behavior_in_Managed_Enviornments_II_SCAFFOLDED.pptx / .pdf — 60 slides, PDF 60 pages
- Integrity: all 46 original slides identical to the input (slide XML, relationships, media, notes)
- Checker: PASS; every scaffold slide inspected in the rendered PDF.

| # | Title | After | Reused figure (slide: caption) | Integrates | Cited papers used | Moves | Run | Sim | Overlap |
|---|---|---|---|---|---|---|---|---|---|
| 5a | Partial Lombard gains leave whistles more masked in noise | 5 | 4: Sørensen et al. (2023), Fig. 2C–F. Whistle amplitude changes with received noise. | 2, 3, 4, 5 | 10.1016/j.cub.2022.12.063 | foundation, mechanism, integration, consequence | 4 | 0.18 | 0.12 |
| 7a | Evoked potentials sum synchronous firing in auditory pathways | 7 | 7: Wong et al. (2022), Fig. 2A–B. Auditory responses and their peak latencies. | 6, 7, 8 | 10.1038/s41598-022-19573-y | foundation, method_logic, mechanism, integration | 3 | 0.25 | 0.22 |
| 8a | Fewer ribbons can raise thresholds while hair cells survive | 8 | 8: Wong et al. (2022), Fig. 4A–C. Saccular anatomy, stained hair cells and Ribeye b puncta. | 6, 7, 8, 10 | 10.1038/s41598-022-19573-y | foundation, mechanism, integration, distinction | 5 | 0.33 | 0.12 |
| 10a | Hearing tracked noise dose but anxiety-like diving did not | 10 | 9: Wong et al. (2022), Fig. 5A–D. Novel-tank behavior after noise exposure. | 6, 9, 10 | 10.1038/s41598-022-19573-y | method_logic, distinction, integration, consequence | 7 | 0.29 | 0.20 |
| 13a | Tight timing rules out following the partner as a strategy | 13 | 13: Jaakkola et al. (2018), Fig. 3A–C. Swimming time, first presses and interpress timing. | 11, 12, 13 | 10.1098/rspb.2018.0948 | method_logic, distinction, integration, foundation | 5 | 0.19 | 0.18 |
| 17a | Dopamine responses follow the error in reward prediction | 17 | 17: Schultz et al. (1993), Fig. 4. Reward delivery and omitted-reward responses. | 15, 16, 17 | 10.1523/JNEUROSCI.13-03-00900.1993 | foundation, integration, mechanism, consequence | 4 | 0.29 | 0.12 |
| 20a | Dopamine cell groups send brief signals to distinct targets | 20 | 18: Schultz et al. (1993), Fig. 7. Reward responsiveness in midbrain cell groups. | 18, 19, 20 | 10.1523/JNEUROSCI.13-03-00900.1993 | foundation, integration, distinction, consequence | 4 | 0.27 | 0.20 |
| 23a | An unchanged tectum argues against body-size growth alone | 23 | 23: Pereira et al. (2020), Fig. 6A–B. Cell counts in telencephalon and optic tectum. | 21, 22, 23, 24 | 10.3389/fphar.2020.00840 | foundation, method_logic, integration, distinction | 4 | 0.28 | 0.17 |
| 26a | Anticipation reveals that a cue now predicts a valued event | 26 | 26: Clegg et al. (2018), Fig. 2. Anticipatory behavior before the three contexts. | 16, 25, 26, 27 | 10.1016/j.applanim.2018.01.015, 10.1523/JNEUROSCI.13-03-00900.1993 | integration, foundation, method_logic, distinction | 5 | 0.29 | 0.19 |
| 31a | Arrival before any call points to a learned daily schedule | 31 | 31: Platto & Serres (2023), Fig. 5. Response latency across trainers and seasons. | 26, 30, 31 | 10.3390/ani13101651 | method_logic, distinction, integration, consequence | 4 | 0.25 | 0.19 |
| 33a | Fewer alternatives can raise the value of human contact | 33 | 33: Platto & Serres (2023), Fig. 4. Positive and negative responses to trainer presence. | 29, 33, 34, 42 | 10.3390/ani13101651, 10.3390/ani13020238 | integration, mechanism, distinction, consequence | 3 | 0.43 | 0.14 |
| 36a | Innovating requires memory for the dolphin's own recent acts | 36 | 35: Yeater et al. (2024), Fig. 1. Correct nonrepeated responses during innovation sessions. | 35, 36, 37, 38 | 10.3390/ani14060896 | foundation, method_logic, consequence, integration | 3 | 0.20 | 0.14 |
| 40a | Dolphins engage more when food must be worked for | 40 | 40: Clegg et al. (2023), Fig. 4. Engagement scores under both enrichment treatments. | 39, 40, 41 | 10.3390/ani13020238 | foundation, consequence, method_logic, integration | 4 | 0.20 | 0.10 |
| 43a | Construction noise was modeled as a rival cause of behavior | 43 | 43: Clegg et al. (2023), Fig. 7A–G. Behavioral measures across enrichment treatments. | 2, 6, 9, 40, 43 | 10.3390/ani13020238 | method_logic, integration, consequence, distinction | 4 | 0.45 | 0.20 |

### For the instructor's attention

- Full text read: Wong et al. 2022, Jaakkola et al. 2018, Pereira et al. 2020, Platto & Serres 2023, Yeater et al. 2024, Clegg et al. 2023. Sørensen et al. 2023 and Schultz et al. 1993 were available as abstracts only; Clegg et al. 2018 (Applied Animal Behaviour Science) was not available, so 26a uses only what the deck says about that study plus a general conditioning principle.
- Numbers from cited papers rather than the deck: each tone presented at least 1000 times (7a, Wong et al. 2022); the call used in 76% of sessions, approach in 96% of sessions without a call and after 66% of calls (31a, Platto & Serres 2023); wild dolphins foraging for 60–70% of their activity budget (40a), drilling noise during 18% of daytime hours and stereotypy at 0.01% of time, the latter in notes only (43a, Clegg et al. 2023).
- Interpretations that go beyond the cited papers are labeled as such on the slides: 17a presents the reward-prediction-error account as a later reading of the 1993 data, not the authors' framing; 20a uses textbook projection anatomy of the A8, A9 and A10 groups; 26a states that the parallel between monkey dopamine cue responses and dolphin anticipation is a hypothesis.
- Please check original slide 22: it describes the fish learning a relationship "between landmarks and food", but Pereira et al. (2020) describe a maze in which a correct choice ended the trial and returned the fish to its home aquarium, and a wrong choice led to a 1-minute confinement in a net; the paper does not describe a food reward. No scaffold slide contradicts or repeats the original.
- Most figures on this deck's two-picture slides pair a main figure with a small secondary panel that recurs on many original slides; since a figure may appear on only one scaffold slide, the scaffold slides carry the main figure only and the lower-right area of 5a, 7a, 10a, 13a, 17a, 20a, 23a, 31a, 33a, 40a and 43a is blank.

## Animal_Behavior_in_Managed_Enviornmens_III.pptx

- Output: Animal_Behavior_in_Managed_Enviornmens_III_SCAFFOLDED.pptx / .pdf — 60 slides, PDF 60 pages
- Integrity: all 46 original slides identical to the input (slide XML, relationships, media, notes)
- Checker: PASS; every scaffold slide inspected in the rendered PDF.

| # | Title | After | Reused figure (slide: caption) | Integrates | Cited papers used | Moves | Run | Sim | Overlap |
|---|---|---|---|---|---|---|---|---|---|
| 04a | Brief stress surges help; lingering ones stall growth | 4 | 4: Hunt et al. (2025), Fig. 4. Day-18 hormones and later mass gain. | 2, 3, 4, 5 | 10.1371/journal.pone.0325265 | mechanism, distinction, integration, method_logic | 3 | 0.21 | 0.11 |
| 06a | ACTH challenges test whether an assay sees secretion | 6 | 7: Cope et al. (2022), Fig. 2. Fecal hormone responses following an ACTH challenge. | 6, 7, 8 | 10.3390/ani12131627 | foundation, method_logic, mechanism, integration | 4 | 0.20 | 0.12 |
| 08a | A missing hormone peak does not mean no stress | 8 | 8: Cope et al. (2022), Fig. 4. Fecal hormone trajectories and recorded care events. | 6, 7, 8 | 10.3390/ani12131627 | method_logic, distinction, mechanism, integration, consequence | 5 | 0.27 | 0.14 |
| 11a | Stress effects recover on separate clocks after transport | 11 | 11: Hunt et al. (2019), Fig. 1C–D. White blood cells and heterophil-to-lymphocyte ratio. | 9, 10, 11 | 10.1093/conphys/coy065 | mechanism, integration, consequence, distinction | 5 | 0.33 | 0.17 |
| 14a | Wet skin may make partner contact more rewarding | 14 | 14: Wilson & Alger (2024), Fig. 3(e–j). Nosing, underwater contact, and play in paired orphan pups. | 12, 13, 14, 15 | 10.3390/ani14223264 | mechanism, foundation, consequence, integration | 3 | 0.21 | 0.17 |
| 19a | Anticipation gauges how much a pup values a meal | 19 | 19: Chudeau et al. (2025), Fig. 6(b). Anticipatory behavior duration and enrichment dose. | 16, 17, 18, 19 | 10.3390/ani15223237 | foundation, mechanism, method_logic, integration | 3 | 0.21 | 0.15 |
| 22a | Kainate receptor density makes the hippocampus vulnerable | 22 | 22: Cook et al. (2015), Fig. S1(A–I). MRI tracing of the sea lion hippocampus. | 22, 23, 28, 29 | 10.1126/science.aac5675, 10.3389/fvets.2023.1040125 | mechanism, foundation, consequence, integration | 4 | 0.35 | 0.15 |
| 26a | Coupled signal fluctuations define functional connectivity | 26 | 26: Cook et al. (2015), Fig. 3. Hippocampal–thalamic connectivity with and without lesions. | 22, 23, 24, 26 | 10.1126/science.aac5675, 10.3389/fvets.2023.1040125 | foundation, mechanism, integration, consequence | 4 | 0.28 | 0.16 |
| 29a | Sleep exposes discharges that wakefulness can hide | 29 | 29: Williams et al. (2023), Fig. 10(A–B). An abnormal recording and the same animal’s later recording. | 27, 28, 29 | 10.3389/fvets.2023.1040125 | method_logic, distinction, foundation, integration | 3 | 0.30 | 0.19 |
| 32a | Mortality-sensing collars separate death from lost contact | 32 | 30: Corsetti et al. (2024), Fig. 1(a). Post-release survival of bold and shy possums. | 30, 31, 32, 35, 45 | 10.1038/s41598-024-67726-y, 10.1038/s41598-025-22596-w, 10.1371/journal.pone.0184286 | method_logic, integration, distinction, foundation | 4 | 0.17 | 0.13 |
| 35a | Fox cues gain meaning by predicting a frightening event | 35 | 35: Corsetti et al. (2025), Fig. 2. Post-release survival after fox-awareness training. | 32, 34, 35, 36, 37 | 10.1038/s41598-025-22596-w | foundation, mechanism, method_logic, distinction, integration | 3 | 0.22 | 0.13 |
| 39a | Following experienced monkeys reveals food trees | 39 | 39: Gómez-Muñoz et al. (2025), Fig. 2. Fruit-species richness across months after release. | 38, 39, 40, 41 | 10.1007/s10329-024-01156-2 | mechanism, integration, method_logic, consequence | 6 | 0.21 | 0.23 |
| 43a | Argos fixes are approximate, so home ranges are estimates | 43 | 43: Robinson et al. (2017), Fig. 3. Overlap of post-release green turtle home ranges. | 42, 43, 44, 45 | 10.1371/journal.pone.0184286 | foundation, method_logic, consequence, integration | 3 | 0.14 | 0.09 |
| 44a | Long journeys may resume interrupted migrations | 44 | 44: Robinson et al. (2017), Fig. 2. Dibba’s 8,283 km post-release track. | 42, 43, 44, 45 | 10.1371/journal.pone.0184286 | distinction, consequence, integration, method_logic | 4 | 0.15 | 0.15 |

### For the instructor's attention

- The file name is kept as uploaded (`Enviornmens_III`), so outputs are `Animal_Behavior_in_Managed_Enviornmens_III_SCAFFOLDED.*`. The deck uses zero-padded slide numbers, so scaffold footers read 04a, 06a and so on.
- Full text read: Hunt et al. 2025 and 2019, Cope et al. 2022, Wilson & Alger 2024, Chudeau et al. 2025, Escobedo-Bonilla et al. 2022, Williams et al. 2023, Corsetti et al. 2024 and 2025, Gómez-Muñoz et al. 2025, Robinson et al. 2017. Cook et al. 2015 (Science) was available as an abstract only; 22a and 26a draw on the deck, Williams et al. 2023 and textbook principles (BOLD signal, fornix–thalamus memory circuit).
- Numbers from cited papers rather than the deck: the presumed-normal corticosterone level below 5 ng/mL, in notes only (04a, Hunt et al. 2025); the collar mortality signal after 4 h without movement (32a, Corsetti et al.); the 5 m proximity radius and 8% vs about a quarter of early samples near experienced companions (39a, Gómez-Muñoz et al. 2025); the 95% and 50% kernel contours (43a, Robinson et al. 2017).
- Please check original slide 29: it describes Williams et al. (2023) Fig. 10(A–B) as an abnormal recording and the same animal's later recording, but the paper describes the panels as a change of state near the end of one recording, from slow-wave sleep to wakefulness. 29a teaches the paper's account.
- Robinson et al. (2017) is internally inconsistent on sub-adults (the Discussion calls all sub-adults transient while Table 1 lists three sub-adult residents); 44a makes no claim about sub-adults.
- 26a reuses Cook et al. (2015) Fig. 3 at the small size and position it has on slide 26, so the area below it is empty.

## Neuroethology_Lecture5_FA2026_4.pptx

- Output: Neuroethology_Lecture5_FA2026_4_SCAFFOLDED.pptx / .pdf — 58 slides (the input has 44, so 14 were added), PDF 58 pages
- Integrity: all 44 original slides identical to the input (slide XML, relationships, media, notes)
- Checker: PASS; every scaffold slide inspected in the rendered PDF.

| # | Title | After | Reused figure (slide: caption) | Integrates | Cited papers used | Moves | Run | Sim | Overlap |
|---|---|---|---|---|---|---|---|---|---|
| 4a | A thick myelinated axon delivers one spike to the whole trunk | 4 | none (text-only clone, icon kept) | 4, 6, 23, 24 | 10.1073/pnas.1918578117, 10.1016/S0301-0082(00)00047-2 | foundation, mechanism, consequence, integration | 6 | 0.21 | 0.13 |
| 7a | Two groups of brainstem neurons time the bend and the thrust | 7 | none (text-only clone, icon kept) | 7, 24, 28, 34 | 10.1242/jeb.66.1.65, 10.1016/0006-8993(90)91012-6 | mechanism, distinction, consequence, integration | 5 | 0.39 | 0.17 |
| 8a | Dense otoliths lag behind the body to signal sound | 8 | none (text-only clone, icon kept) | 8, 12, 15, 35 | 10.1016/j.cub.2015.04.025 | foundation, mechanism, integration, consequence | 4 | 0.19 | 0.14 |
| 10a | Chemical release at club endings grows during afferent bursts | 10 | none (text-only clone, icon kept) | 9, 10, 11, 39 | 10.1523/JNEUROSCI.08-04-01313.1988 | mechanism, foundation, consequence, integration | 6 | 0.24 | 0.15 |
| 14a | Spike-to-muscle timing and side make Mauthner firing causal | 14 | none (text-only clone, icon kept) | 5, 14, 15, 20 | 10.1242/jeb.66.1.243 | method_logic, integration, consequence, distinction | 5 | 0.26 | 0.17 |
| 16a | Low input resistance demands large, synchronous excitation | 16 | none (text-only clone, icon kept) | 10, 12, 16, 25 | 10.1016/j.cub.2015.04.025, 10.1016/j.neuron.2005.05.019 | foundation, mechanism, consequence, integration | 5 | 0.32 | 0.23 |
| 17a | Shunting inhibition divides excitation rather than subtracting | 17 | none (text-only clone, icon kept) | 10, 16, 17, 22 | Faber & Korn (1978), book chapter, 10.1016/j.neuron.2005.05.019 | foundation, mechanism, consequence, integration | 5 | 0.23 | 0.20 |
| 25a | Spiral fibers add delayed excitation where the spike starts | 25 | none (text-only clone, icon kept) | 13, 16, 19, 25 | 10.1016/j.cub.2015.04.025 | mechanism, integration, consequence, foundation | 4 | 0.27 | 0.13 |
| 28a | Ablation tests necessity; stimulation tests sufficiency | 28 | none (text-only clone, icon kept) | 26, 27, 28, 29 | 10.1016/0006-8993(90)91012-6, 10.1073/pnas.1918578117 | distinction, method_logic, integration, consequence | 5 | 0.27 | 0.16 |
| 29a | The axon initial segment, not the soma, sets escape speed | 29 | none (text-only clone, icon kept) | 13, 25, 27, 29, 30 | 10.1073/pnas.1918578117 | foundation, mechanism, integration, distinction | 4 | 0.19 | 0.12 |
| 31a | Mixed predator trials isolate the survival cost of one neuron | 31 | none (text-only clone, icon kept) | 15, 27, 30, 31 | 10.1073/pnas.1918578117 | method_logic, consequence, integration | 5 | 0.17 | 0.06 |
| 33a | Serial copies of the Mauthner cell give a slower backup | 33 | none (text-only clone, icon kept) | 27, 30, 32, 33 | 10.1016/j.cub.2015.04.025, Kimmel et al. (1980), 10.1073/pnas.1918578117 | foundation, mechanism, integration, consequence | 5 | 0.19 | 0.13 |
| 39a | Habituation differs from fatigue and from sensory adaptation | 39 | none (text-only clone, icon kept) | 10, 16, 17, 39 | 10.1016/j.neuron.2005.05.019, 10.1523/JNEUROSCI.08-04-01313.1988 | distinction, method_logic, foundation, integration | 4 | 0.21 | 0.11 |
| 40a | Co-active brainstem neurons shape what a Mauthner spike does | 40 | none (text-only clone, icon kept) | 7, 28, 33, 40 | Canfield & Rose (1993), 10.1016/0006-8993(90)91012-6, 10.1016/S0301-0082(00)00047-2 | mechanism, integration, consequence | 5 | 0.30 | 0.23 |

### For the instructor's attention

- Uploaded as `Neuroethology_Lecture5_FA2026_4.pptx`; the name is kept, so outputs are `Neuroethology_Lecture5_FA2026_4_SCAFFOLDED.*`.
- Older format (44 slides, icon plus text, references printed under the title, no speaker notes, no figure captions). Scaffold slides clone that layout: each keeps its template's icon, carries a reference line copied exactly from the deck, keeps the deck's "NEUROETHOLOGY · LECTURE 5" footer label, and has no figure, like its neighbours. The deck sets no bold key terms in body text, so none are used.
- Speaker notes are new on the scaffold slides only and end with references copied exactly from the deck's reference lines.
- Full text read: Hecker et al. 2020, Lacoste et al. 2015. Abstracts only: Lin & Faber 1988, Zottoli 1977, Eaton et al. 1977, Nissanov et al. 1990, Eaton et al. 1991 and 2001, Korn & Faber 2005; Faber & Korn 1978 (book chapter), Kimmel et al. 1980 and Canfield & Rose 1993 were not available, so slides citing them rely on the deck and textbook principles.
- Numbers from cited papers rather than the deck are listed per slide under `paper_numbers` in the spec (for example the 22% and 47% reductions after single-cell stimulation, 28a; the 4.4-fold optogenetic enhancement, 25a; Zottoli's 34, 39 and 52 trials, 14a).
- Slide 31a describes the predator in Hecker et al. (2020) without naming its species, since the deck does not name it.

## Neuroethology_Lecture6_FA2026_2.pptx

- Output: Neuroethology_Lecture6_FA2026_2_SCAFFOLDED.pptx / .pdf — 58 slides (the input has 44, so 14 were added), PDF 58 pages
- Integrity: all 44 original slides identical to the input (slide XML, relationships, media, notes)
- Checker: PASS; every scaffold slide inspected in the rendered PDF.

| # | Title | After | Reused figure (slide: caption) | Integrates | Cited papers used | Moves | Run | Sim | Overlap |
|---|---|---|---|---|---|---|---|---|---|
| 4a | A rearward body wave pushes water back and the leech forward | 4 | none (text-only clone, icon kept) | 4, 14, 15, 16 | 10.1186/2042-1001-1-13, 10.1126/science.663615 | mechanism, foundation, consequence, integration | 3 | 0.18 | 0.16 |
| 8a | Resetting the rhythm separates oscillator cells from followers | 8 | none (text-only clone, icon kept) | 8, 9, 10, 16 | 10.1242/jeb.75.1.25, 10.1186/2042-1001-1-13 | method_logic, distinction, mechanism, integration | 5 | 0.31 | 0.16 |
| 11a | Leech oscillator cells are not pacemakers; the network is | 11 | none (text-only clone, icon kept) | 9, 11, 12, 13 | 10.1016/0149-7634(94)90010-8, 10.1186/2042-1001-1-13 | distinction, foundation, mechanism, integration | 4 | 0.18 | 0.14 |
| 12a | Inhibition passed around a three-group ring sets phase order | 12 | none (text-only clone, icon kept) | 10, 11, 12, 16 | 10.1242/jeb.75.1.25, 10.1186/2042-1001-1-13, 10.1126/science.663615 | mechanism, foundation, integration, consequence | 5 | 0.25 | 0.22 |
| 15a | Asymmetric coupling and feedback set the intersegmental lag | 15 | none (text-only clone, icon kept) | 9, 13, 14, 15, 17 | 10.1186/2042-1001-1-13, 10.1242/jeb.75.1.25, 10.1016/j.conb.2008.01.006 | mechanism, consequence, integration, foundation | 4 | 0.25 | 0.20 |
| 17a | Stretch feedback entrains the swim rhythm to the moving body | 17 | none (text-only clone, icon kept) | 9, 15, 17, 18 | Blackshaw & Kristan (1990), 10.1186/2042-1001-1-13 | foundation, mechanism, integration, consequence | 4 | 0.22 | 0.17 |
| 22a | Serotonin turns cell 204 into a lasting source of drive | 22 | none (text-only clone, icon kept) | 20, 22, 23 | 10.1007/BF00189399, 10.1152/jn.1986.55.5.977 | mechanism, foundation, consequence, integration | 4 | 0.19 | 0.11 |
| 23a | Bypassing the sensory path locates where habituation happens | 23 | none (text-only clone, icon kept) | 19, 20, 23 | 10.1152/jn.1986.55.5.977 | method_logic, integration, consequence, mechanism | 5 | 0.16 | 0.14 |
| 28a | Crawl steps travel as excitation waves, not locked oscillators | 28 | none (text-only clone, icon kept) | 12, 14, 25, 28, 29 | 10.1523/JNEUROSCI.20-04-01643.2000, 10.1186/2042-1001-1-13 | distinction, mechanism, integration, consequence | 4 | 0.22 | 0.29 |
| 31a | Voltage-sensitive dyes report inhibition as well as excitation | 31 | none (text-only clone, icon kept) | 11, 31, 32, 41 | 10.1523/JNEUROSCI.3265-06.2006, 10.1002/dneu.20551 | foundation, method_logic, integration, consequence | 5 | 0.24 | 0.16 |
| 35a | Early discriminators decide; cell 204 carries out the swim | 35 | none (text-only clone, icon kept) | 20, 33, 35, 36 | 10.1126/science.1103736, 10.1186/2042-1001-1-13 | integration, mechanism, consequence, distinction | 4 | 0.19 | 0.16 |
| 36a | Combining neurons reveals a decision no single cell shows | 36 | none (text-only clone, icon kept) | 33, 35, 36, 37 | 10.1126/science.1103736 | foundation, method_logic, mechanism, integration | 5 | 0.23 | 0.15 |
| 38a | A fluid-filled body turns muscle tension into shape changes | 38 | none (text-only clone, icon kept) | 25, 27, 32, 38 | 10.1186/2042-1001-1-13, 10.1016/j.conb.2008.01.006 | foundation, mechanism, integration, consequence | 6 | 0.31 | 0.11 |
| 40a | Inhibition that grows with input changes the circuit's gain | 40 | none (text-only clone, icon kept) | 11, 31, 40 | 10.1016/j.neuron.2007.11.028 | foundation, method_logic, mechanism, consequence | 5 | 0.26 | 0.19 |

### For the instructor's attention

- Uploaded as `Neuroethology_Lecture6_FA2026_2.pptx`; the name is kept, so outputs are `Neuroethology_Lecture6_FA2026_2_SCAFFOLDED.*`.
- Older format, handled as for Lecture 5: text-only clones with the template icon, a reference line copied from the deck, the deck's footer label, no bold key terms, new speaker notes ending with references copied from the deck.
- Full text read: Lamb & Calabrese 2011. Abstracts only: Briggman et al. 2005, Briggman & Kristan 2006, Cacciatore et al. 2000, Eisenhart et al. 2000, Baca et al. 2008, Friesen & Kristan 2007, Friesen 1994, Stent et al. 1978, Friesen et al. 1978, Debski & Friesen 1986, O'Gara & Friesen 1995, Nusbaum et al. 1987, Marin-Burgin et al. 2008; Blackshaw & Kristan 1990 was not found in Europe PMC.
- Numbers from cited papers are listed under `paper_numbers` (for example swim periods of 0.3 to 1.0 s and phase lags of 0.044 to 0.1 per segment, 15a; the 290 ms earlier discrimination, 35a; 72 trials of direct cell 204 stimulation, 23a).
- Lamb & Calabrese (2011) state that few swim oscillator cells are reciprocally connected and that they are not intrinsic bursters; 11a teaches this, which refines the half-center framing on original slide 11 without contradicting it.
