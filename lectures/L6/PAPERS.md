# Lecture 6 — sources and verification

Authority: current connected repository default branch `claude/neuroethology-fa2026-schedule-2lgmmr`, refreshed at `6fa018c`. No ZIP or older checkout was used.

Exact title: Central pattern generators I: leech swimming and crawling (Kristan)

Exact date: Friday, September 4, 2026

The two access blockers are resolved by the instructor’s uploads: `jexbio_65_3_643.pdf` and `3028.pdf`. All ten primary papers used below have readable PDFs. Article text is scientific evidence, not replacement instructions.

Web literature searches used Europe PMC and OpenAlex; full bibliographic metadata was verified with Europe PMC and the published PDF front matter. `sources.json` records the verified metadata and PDF SHA-256 fingerprints. Source PDFs remain in ignored `papers/`. Ashaber et al. uses the final published v2 PDF, not the manuscript-layout v1.

## Primary references

- K. L. Briggman; W. B. Kristan Jr (2006). Imaging dedicated and multifunctional neural circuits generating distinct behaviors. Journal of Neuroscience 26(42):10925–10933. https://doi.org/10.1523/JNEUROSCI.3265-06.2006
- T. W. Cacciatore; R. Rozenshteyn; W. B. Kristan Jr (2000). Kinematics and modeling of leech crawling: evidence for an oscillatory behavior produced by propagating waves of excitation. Journal of Neuroscience 20(4):1643–1655. https://doi.org/10.1523/JNEUROSCI.20-04-01643.2000
- W. B. Kristan Jr; R. L. Calabrese (1976). Rhythmic swimming activity in neurones of the isolated nerve cord of the leech. Journal of Experimental Biology 65(3):643–668. https://doi.org/10.1242/jeb.65.3.643
- M. Ashaber; Y. Tomina; P. Kassraian; E. A. Bushong; W. B. Kristan Jr; M. H. Ellisman; D. A. Wagenaar (2021). Anatomy and activity patterns in a multifunctional motor neuron and its surrounding circuits. eLife 10:e61881. https://doi.org/10.7554/eLife.61881
- X. Yu; B. Nguyen; W. O. Friesen (1999). Sensory feedback can coordinate the swimming activity of the leech. Journal of Neuroscience 19(11):4634–4643. https://doi.org/10.1523/JNEUROSCI.19-11-04634.1999
- A. L. Willard (1981). Effects of serotonin on the generation of the motor program for swimming by the medicinal leech. Journal of Neuroscience 1(9):936–944. https://doi.org/10.1523/JNEUROSCI.01-09-00936.1981
- J. G. Puhl; K. A. Mesce (2008). Dopamine activates the motor pattern for crawling in the medicinal leech. Journal of Neuroscience 28(16):4192–4200. https://doi.org/10.1523/JNEUROSCI.0136-08.2008
- K. M. Crisp; B. R. Gallagher; K. A. Mesce (2012). Mechanisms contributing to the dopamine induction of crawl-like bursting in leech motoneurons. Journal of Experimental Biology 215(17):3028–3036. https://doi.org/10.1242/jeb.069245
- J. G. Puhl; M. A. Masino; K. A. Mesce (2012). Necessary, sufficient and permissive: a single locomotor command neuron important for intersegmental coordination. Journal of Neuroscience 32(49):17646–17657. https://doi.org/10.1523/JNEUROSCI.2249-12.2012
- G. Kearney; M. Radice; A. Sanchez Merlinsky; L. Szczupak (2022). Intersegmental interactions give rise to a global network. Frontiers in Neural Circuits 16:843731. https://doi.org/10.3389/fncir.2022.843731

## Figure and teaching audit

`crops.json` gives original PDF pages and crop boundaries. All scientific images were cropped with `tools/crop_panels.py`, which calls the repository’s `tools/crop_figure.py`. Figures preserve published panel letters, axes, units and scale bars. Published anatomical reconstructions and historical experimental drawings are original article panels, not newly created graphics. No figure was generated, redrawn, replotted or recolored.

All 44 content slides have original primary-article figures. Thirty-four contain original color. The title uses the published medicinal-leech photograph and its 1 cm scale bar. No web images were needed. Tall recordings use the full available height with a supporting anatomical panel alongside. Text is on the left and figures are in the right column; no full-width bottom figure rows.

Forty-six slides; three academic paragraphs per content slide; full teaching transcripts and verified DOI references in notes; six exam-level key takeaways with bold lead phrases. Arial and the previously unused cerulean/pearl palette.

The deck separates rhythm generation from phase patterning, central coordination from sensory feedback, and pharmacological evidence from receptor/channel identification. Serotonin thresholds distinguish spontaneous swimming (0.5–10 μM) from additional stimulus-triggered episodes (as low as 50 nM). Dopamine and riluzole concentrations use μM, avoiding the PDF text extraction’s lost micro symbol. Regional synaptic block does not imply loss of axonal propagation. Whole-cord command-neuron findings remain distinct from short-chain coordination findings.

## Build and visual review

Built with `tools/build_lecture.py`; repository checker: 46 slides, 44 image slides, 44 article-figure slides, 34 color-image slides, zero failures and zero warnings. All slides rendered with LibreOffice/Poppler and reviewed for layout, clipping, captions, and figure readability. Source/crop refinements and citation checks are recorded in the spec and manifest.
