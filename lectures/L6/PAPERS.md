# Lecture 6 — source access and required PDFs

Authority: connected repository default branch `claude/neuroethology-fa2026-schedule-2lgmmr`, refreshed at 4900215f403a41f516fd0e5db2e1148524d3a1a9. No ZIP or old checkout was used.

Exact title: Central pattern generators I: leech swimming and crawling (Kristan)

Exact date: Friday, September 4, 2026

## Required uploads

1. Kristan, W. B., Jr., & Calabrese, R. L. (1976). Rhythmic swimming activity in neurones of the isolated nerve cord of the leech. Journal of Experimental Biology, 65(3), 643–668. https://doi.org/10.1242/jeb.65.3.643
2. Crisp, K. M., Gallagher, B. R., & Mesce, K. A. (2012). Mechanisms contributing to the dopamine induction of crawl-like bursting in leech motoneurons. Journal of Experimental Biology, 215(17), 3028–3036. https://doi.org/10.1242/jeb.069245

Both citations were verified against Europe PMC and OpenAlex metadata. Current publisher pages and legacy PDF routes returned HTTP 403. OpenAlex listed no downloadable open-access copy for either paper. Author-copy web searches did not locate a usable PDF. Access diagnostics and literature searches are retained in `/workspace/research-L6/`. No HTML challenge page was accepted as a PDF.

The first paper supplies original isolated-cord evidence for a swimming central pattern generator. The second addresses the cellular mechanisms underlying dopamine-induced crawl-like bursting; molecular mechanisms must not be inferred from behavioral drug effects alone.

## Available primary PDFs

Verified PDFs and extracted text are retained in the scratch directory; copies are in ignored `papers/`:

- Briggman & Kristan (2006), Imaging dedicated and multifunctional neural circuits generating distinct behaviors. Journal of Neuroscience 26(42):10925–10933. DOI 10.1523/JNEUROSCI.3265-06.2006.
- Cacciatore, Rozenshteyn & Kristan (2000), Kinematics and modeling of leech crawling: evidence for an oscillatory behavior produced by propagating waves of excitation. Journal of Neuroscience 20(4):1643–1655. DOI 10.1523/JNEUROSCI.20-04-01643.2000.
- Puhl & Mesce (2008), Dopamine activates the motor pattern for crawling in the medicinal leech. Journal of Neuroscience 28(16):4192–4200. DOI 10.1523/JNEUROSCI.0136-08.2008.
- Willard (1981), Effects of serotonin on the generation of the motor program for swimming by the medicinal leech. Journal of Neuroscience 1(9):936–944. DOI 10.1523/JNEUROSCI.01-09-00936.1981.
- Yu, Nguyen & Friesen (1999), Sensory feedback can coordinate the swimming activity of the leech. Journal of Neuroscience 19(11):4634–4643. DOI 10.1523/JNEUROSCI.19-11-04634.1999.
- Puhl, Masino & Mesce (2012), Necessary, sufficient and permissive: a single locomotor command neuron important for intersegmental coordination. Journal of Neuroscience 32(49):17646–17657. DOI 10.1523/JNEUROSCI.2249-12.2012.
- Ashaber et al. (2021), Anatomy and activity patterns in a multifunctional motor neuron and its surrounding circuits. eLife 10:e61881. DOI 10.7554/eLife.61881. CDN v1 is a manuscript-layout PDF; obtain and inspect the final published version before cropping.
- Pipkin et al. (2018), Verifying, challenging, and discovering new synapses among fully EM-reconstructed neurons in the leech ganglion. Frontiers in Neuroanatomy 12:95. DOI 10.3389/fnana.2018.00095.
- Kearney et al. (2022), Intersegmental interactions give rise to a global network. Frontiers in Neural Circuits 16:843731. DOI 10.3389/fncir.2022.843731.
- Radice et al. (2026), Phase-specific premotor inhibition modulates leech rhythmic motor output. eLife 14:RP104921. DOI 10.7554/eLife.104921.

The additional Mesce & Pierce-Shimomura (2010) review, DOI 10.3389/fnbeh.2010.00049, supplies context only. Its figures do not replace primary evidence. Bibliographic details of available papers will be verified against front matter before inclusion.

## Retained build requirements and status

Build paused under the instructor’s explicit missing-PDF rule. No deck or placeholder scientific image has been created; no theme has been marked used. On resumption: 46 slides, exact schedule wording, three to five full paragraphs per content slide, teaching transcripts and full DOI references, Arial, unused permitted theme, two-column text/figure layout, at least 40 image content slides and 34 primary-article figure slides, and an aim of original color on at least half the image slides. Never create or recolor images. Use original PDF panels, preserve scientific labels, build with `tools/build_lecture.py`, visually review all slides, commit and push, and export a Presenton PPTX with a browser preview. Existing `AGENTS.md`, `.claude/skills/neuroethology-lecture/SKILL.md`, and `prompts/make_lecture.md` already retain these rules.

The source progression is behavior and kinematics → ganglion and identified-neuron anatomy → isolated-cord CPG evidence → swim phase and intersegmental coordination → sensory feedback → crawling rhythms and shared neurons → dopamine/serotonin and cellular mechanism → command signals and modern anatomical/functional tests.

Existing Python/PPTX/Pillow and Poppler tools are available; the previous lecture builder and render workflow remain usable. No cloud configuration change is needed for setup. The remaining blocker is access to the two primary PDFs above.
