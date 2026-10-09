# Lecture 40 preparation

Exact new title: Frontiers: optogenetics, wireless-recording tools in emerging neuroethology systems, and casual tests of neural circuits underlying natural behavior

Exact date: Friday, December 4, 2026

Status: awaiting the four original PDFs in `PAPERS.md`. No slide spec, PowerPoint or figure crop has been created. No theme has been marked used.

The current default branch and eleven authoritative repository files were verified against current commit `9da8853a42489ca33b314611e264fcc3eb06a226`. The checkout matches that commit; no ZIP or older checkout is used. The environment already has python-pptx, Pillow, PyMuPDF, Poppler and LibreOffice. Git authentication currently fails; the public default-branch page and pinned file reads work.

The new title is the instructor’s explicit replacement for the old genetic-tools title. The wording `casual tests` is retained exactly unless the instructor answers the optional spelling clarification. Scientific content will distinguish causal intervention from observational recordings.

## Preliminary 44-slide source allocation

Topics are provisional until all original methods, controls, results and figures are inspected. This plan is not a drafted lecture.

1. Optical activation links descending input to behavior — cande18.
2. Channelrhodopsin converts illumination into ionic current — nagel03.
3. Cation selectivity determines the effect of illumination — nagel03.
4. Light pulses control the timing of membrane excitation — nagel03 boyden05.
5. Genetic targeting confines optical drive to selected cells — boyden05.
6. Millisecond pulses can evoke and time action potentials — boyden05.
7. Anion channels require a different electrical interpretation — govorunova15.
8. The chloride gradient constrains optical inhibition — govorunova15.
9. Red-shifted activation permits tests in intact flies — inagaki14.
10. Light-only and expression controls constrain interpretation — inagaki14.
11. Experience changes the consequence of neuronal activation — inagaki14.
12. Descending-neuron targeting separates behavioral pathways — cande18.
13. Behavioral measurements resolve more than locomotor speed — cande18.
14. Anatomy distinguishes parallel descending pathways — cande18.
15. Activation depends on the animal’s behavioral state — cande18.
16. Ciliary coordination controls larval locomotion — veraszto17.
17. Serial reconstruction defines the ciliomotor network — veraszto17.
18. Calcium activity relates network recruitment to movement — veraszto17.
19. Cell-targeted activation tests ciliomotor function — veraszto17.
20. A hydrodynamic stimulus recruits a startle response — bezares18.
21. Polycystin-bearing sensory cells define a candidate input — bezares18.
22. Genetic disruption tests sensory-channel dependence — bezares18.
23. Larval hunting includes a coordinated orienting sequence — antinucci19.
24. Identified pretectal cells participate in prey responses — antinucci19.
25. Optical activation tests initiation of hunting behavior — antinucci19.
26. Cell ablation tests contribution to natural hunting — antinucci19.
27. Connectivity constrains the interpretation of activation — antinucci19.
28. Untethered imaging retains interaction between animals — grover20.
29. Motion correction separates movement from fluorescence — grover20.
30. Activity during social behavior remains correlational — grover20.
31. Wireless amplification removes the recording tether — szuts11.
32. Bandwidth and sampling constrain the recorded signal — szuts11.
33. Recording quality must be tested during movement — szuts11.
34. Wireless logging allows behavior during free flight — zhang24.
35. Synchronized trajectories relate spikes to external events — zhang24.
36. Experimenter identity can influence neural recordings — zhang24.
37. Cue controls constrain an interpretation of social coding — zhang24.
38. Repeated flights permit comparisons across natural episodes — forli25.
39. Activity after flight can retain structured temporal patterns — forli25.
40. Representation stability differs from a causal intervention — forli25.
41. Wireless power supplies an implanted light source — montgomery15.
42. Power delivery depends on position and device geometry — montgomery15.
43. Implanted stimulation must retain behavioral controls — montgomery15.
44. Causal claims require matched perturbation and behavior — cande18 antinucci19 montgomery15.

## Build constraints

- One title slide, 44 content slides and one six-item Key takeaways slide.
- At least 40 image-bearing content slides and 34 primary-figure slides; aim for native color on at least half of image slides.
- Original published PDF panels only, plus at most ten real credited web photographs where useful; no created or modified scientific imagery.
- An unused muted palette will be selected only when building. All current palettes are recorded as used; add a distinct compliant palette rather than reusing one.
- Arial, black body/caption/footer text, 3–5 paragraphs per content slide and teaching-transcript notes with verified DOI references.
- Build through `tools/build_lecture.py`, run the repository checker, render and inspect all slides, and verify the delivered files.
- Preserve the previously delivered lectures unchanged.
