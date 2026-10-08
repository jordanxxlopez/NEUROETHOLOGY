# Lecture 30 — final slide plan

Exact title: Navigation III: monarch butterfly migration and the circadian sun compass

Exact date: Wednesday, November 4, 2026

Final format: 1 title + 44 content + 1 Key takeaways = 46 slides. Every content slide has a primary-paper figure, three academic paragraphs and a teaching transcript with complete DOI references.

| Slide | Topic | Original figure sources |
| --- | --- | --- |
| 2 | Autumn migrants maintain a southwest flight bearing | Mouritsen & Frost (2002), Fig. 2(A) |
| 3 | A vertical tether preserves turning without translation | Mouritsen & Frost (2002), Fig. 1(B–D) |
| 4 | Rotating the apparatus does not rotate the compass | Mouritsen & Frost (2002), Fig. 1(B–D) |
| 5 | Advancing the clock rotates flight toward the southeast | Mouritsen & Frost (2002), Fig. 2(A–C) |
| 6 | Delaying the clock produces the opposite heading change | Mouritsen & Frost (2002), Fig. 2(A–C) |
| 7 | Constant light leaves orientation tied to the visible sun | Froy et al. (2003), Fig |
| 8 | Blocking ultraviolet light disrupts sustained flight | Froy et al. (2003), Fig; Sauman et al. (2005), Fig |
| 9 | Visible light can entrain the emergence rhythm | Froy et al. (2003), Fig |
| 10 | Retinal cells express distinct visual-pigment proteins | Sauman et al. (2005), Fig |
| 11 | The dorsal rim area is specialized for ultraviolet input | Sauman et al. (2005), Fig |
| 12 | Polarizer rotation changes flight in a restricted assay | Sauman et al. (2005), Fig; Sauman et al. (2005), Fig |
| 13 | Polarized-light behavior requires brightness controls | Stalleicken et al. (2005), Fig |
| 14 | Dorsal-rim masking leaves sun-based orientation intact | Stalleicken et al. (2005), Fig |
| 15 | Emergence persists without a daily light signal | Froy et al. (2003), Fig |
| 16 | The per transcript changes with circadian phase | Froy et al. (2003), Fig |
| 17 | PER marks candidate clock cells in the lateral brain | Sauman et al. (2005), Fig |
| 18 | CRY1 links light exposure to clock-protein depletion | Zhu et al. (2008), Fig; Sauman et al. (2005), Fig |
| 19 | Brain TIMELESS responds to circadian phase and light | Zhu et al. (2008), Fig |
| 20 | CRY2 represses clock-controlled transcription | Zhu et al. (2008), Fig; Zhu et al. (2008), Fig |
| 21 | Reducing CRY2 removes normal transcriptional repression | Zhu et al. (2008), Fig; Zhu et al. (2008), Fig |
| 22 | Clock proteins form complexes that support CRY2 stability | Zhu et al. (2008), Fig; Zhu et al. (2008), Fig |
| 23 | Nuclear CRY2 varies with clock phase | Zhu et al. (2008), Fig |
| 24 | Rhythmic CRY2 occurs in central-body fibers | Zhu et al. (2008), Fig; Heinze & Reppert (2011), Fig. 2(A–J) |
| 25 | Removing antennae disrupts the group compass bearing | Merlin et al. (2009), Fig |
| 26 | Antenna-less butterflies remain capable of free flight | Merlin et al. (2009), Fig |
| 27 | Antennal clock-gene RNA remains rhythmic in darkness | Merlin et al. (2009), Fig |
| 28 | Isolated antennae retain a locally entrainable rhythm | Merlin et al. (2009), Fig |
| 29 | Black paint blocks the antennal light response | Merlin et al. (2009), Fig |
| 30 | Optically blocking antennae changes the selected heading | Merlin et al. (2009), Fig |
| 31 | One functioning antenna is sufficient for compensation | Guerra et al. (2012), Fig |
| 32 | Conflicting antennal timing disrupts the shared bearing | Guerra et al. (2012), Fig |
| 33 | Removing the conflicting antenna restores orientation | Guerra et al. (2012), Fig |
| 34 | Central-complex neuropils define a compass substrate | Heinze & Reppert (2011), Fig. 2(A–J) |
| 35 | Dye-filled neurons connect visual input to compass regions | Heinze & Reppert (2011), Fig. 3(A); Heinze & Reppert (2011), Fig. 3(B) |
| 36 | Compass neurons respond to the polarization axis | Heinze & Reppert (2011), Fig. 4(A–D); Heinze & Reppert (2011), Fig. 3(A) |
| 37 | The same compass circuit represents solar azimuth | Heinze & Reppert (2011), Fig. 5(A–F); Heinze & Reppert (2011), Fig. 3(A) |
| 38 | Dorsal masking separates two converging visual inputs | Heinze & Reppert (2011), Fig. 6(A–F); Sauman et al. (2005), Fig |
| 39 | Migratory butterflies have narrower green-light tuning | Nguyen et al. (2021), Fig; Heinze & Reppert (2011), Fig. 3(A) |
| 40 | Migratory tuning concentrates sensitivity near the front | Nguyen et al. (2021), Fig; Heinze & Reppert (2011), Fig. 3(A) |
| 41 | Spring remigrants reverse direction but retain compensation | Guerra & Reppert (2013), Fig. 1(A–C) |
| 42 | Cold exposure triggers northward orientation | Guerra & Reppert (2013), Fig. 3(B–C) |
| 43 | Age and calendar date do not replace the cold trigger | Guerra & Reppert (2013), Fig. 4(A–B) |
| 44 | Loss of CRY1 weakens behavioral and molecular rhythms | Iiams et al. (2024), Fig; Iiams et al. (2024), Fig |
| 45 | Goal coding differs from coding the current heading | Beetz et al. (2023), Fig; Heinze & Reppert (2011), Fig. 2(A–J) |

Theme: flint / soft blue; Arial. Native article color is retained on 26 content slides. Original source panels retain calibration, axes and panel labels. Anatomy accompanies the named eye, antennal, clock-cell and central-complex structures.

Evidence boundaries retained: artificial polarizer behavior versus migratory cue necessity; head/brain rhythms versus antennal timing; reporter feedback versus autonomous cultured oscillation; migratory cohort associations versus causal seasonal tuning; arbitrary laboratory goal neurons versus natural seasonal goals. The complete timing-to-steering synaptic and molecular chain remains unresolved.

Build: `python tools/build_lecture.py lectures/L30/lecture.json`, then `python lectures/L30/finalize_notes.py` for Arial/plain speaker notes. `python lectures/L30/build.py` runs both steps. Panel generation invokes `tools/crop_panels.py` through `crop_originals.py`, selecting the repository’s PyMuPDF backend for PDFs whose CropBox differs from MediaBox. No scientific content is redrawn.

Reusable prompt: `prompts/make_lecture_30.md`; persistent image policy: `AGENTS.md` and `.claude/skills/neuroethology-lecture/SKILL.md`.
