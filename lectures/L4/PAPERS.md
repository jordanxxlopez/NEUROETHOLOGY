# Lecture 4 — source and validation record

Authority: connected repository default branch `claude/neuroethology-fa2026-schedule-2lgmmr`, refreshed at `4dfc791188f69e259678a057df70169acd684502`. No ZIP or older checkout was used.

Exact title: Crayfish tail-flip: lateral and medial giant fiber circuits (Wine & Krasne)

Exact date: Monday, August 31, 2026

## Primary sources

- J. J. Wine; F. B. Krasne (1972). The Organization of Escape Behaviour in the Crayfish. Journal of Experimental Biology 56(1):1–18. https://doi.org/10.1242/jeb.56.1.1
- M. E. Swierzbinski; J. Herberholz (2018). Effects of ethanol on sensory inputs to the medial giant interneurons of crayfish. Frontiers in Physiology 9:448. https://doi.org/10.3389/fphys.2018.00448
- J. Herberholz; B. L. Antonsen; D. H. Edwards (2002). A lateral excitatory network in the escape circuit of crayfish. Journal of Neuroscience 22(20):9078–9085. https://doi.org/10.1523/JNEUROSCI.22-20-09078.2002
- J. Herberholz; S. H. Mishra; D. Uma; M. W. Germann; D. H. Edwards; K. Potter (2011). Non-invasive imaging of neuroanatomical structures and neural activation with high-resolution MRI. Frontiers in Behavioral Neuroscience 5:16. https://doi.org/10.3389/fnbeh.2011.00016
- D. H. Edwards; W. J. Heitler; E. M. Leise; R. A. Fricke (1991). Postsynaptic modulation of rectifying electrical synaptic inputs to the LG escape command neuron in crayfish. Journal of Neuroscience 11(7):2117–2129. https://doi.org/10.1523/JNEUROSCI.11-07-02117.1991
- D. H. Edwards; S.-R. Yeh; F. B. Krasne (1998). Neuronal coincidence detection by voltage-sensitive electrical synapses. Proceedings of the National Academy of Sciences USA 95(12):7145–7150. https://doi.org/10.1073/pnas.95.12.7145
- E. T. Vu; A. Berkowitz; F. B. Krasne (1997). Postexcitatory inhibition of the crayfish lateral giant neuron: a mechanism for sensory temporal filtering. Journal of Neuroscience 17(22):8867–8879. https://doi.org/10.1523/JNEUROSCI.17-22-08867.1997
- K. Fraser; W. J. Heitler (1991). Photoinactivation of the crayfish segmental giant neuron reveals a direct giant-fiber to fast-flexor connection with a chemical component. Journal of Neuroscience 11(1):59–71. https://doi.org/10.1523/JNEUROSCI.11-01-00059.1991

## Acquisition and verification

Wine and Krasne (1972) and Edwards, Yeh and Krasne (1998) were supplied by the instructor after publisher access failures. Both uploaded PDFs were inspected, and their original published panels were used. The other six primary papers were downloaded from Journal of Neuroscience or Frontiers publisher PDF endpoints and verified as real PDFs. Metadata was cross-checked with Crossref, Europe PMC, OpenAlex and the papers’ front matter. Literature web searches and access diagnostics are retained in `/workspace/research-L4/`. Source PDFs are retained in ignored `papers/`.

Eight primary studies support the deck. Herberholz (2022), DOI 10.3389/fphys.2022.1052354, provided bibliographic context only. Historical circuit illustrations reproduced by Wine and Krasne are accompanied by newer primary anatomy when the slide requires a structural image. Schematics present inside an original article panel remain untouched published material; none were created for this lecture.

## Figures and layout

46 slides: title, 44 content, and six bold-lead exam takeaways. All 44 content slides carry primary-article imagery; 28 include color already present in the published figure. There are 41 unique PDF crops, extracted at 220 dpi with `tools/crop_panels.py` and `tools/crop_figure.py`. `crops.json` records paper, page and normalized crop box. No image was generated, redrawn, recolored or replaced with stock material; no web photos were needed. Captions identify author, year, figure and panel, and DOI source URLs are in the spec and notes.

Text is on the left and scientific figures are on the right. Paired anatomy and experimental panels remain inside the figure column. The unused deep-sea blue/cyan palette and Arial follow the course theme rules. Every content slide has three full paragraphs and a complete teaching transcript with full references in its notes. The current repository prompt and guidelines retain the strict original-image, two-column and image-density requirements.

## Validation

Built with `tools/build_lecture.py`: 46 slides, 44 image content slides, 44 article-figure slides, 28 with original color, zero failures and zero warnings. All 41 crops were visually checked against source panels, including axes, units, panel letters and scale bars. All 46 rendered slides were visually reviewed for text fit and figure placement; the MG anatomy panels were enlarged during that review. Citations, source labels and experimental claims were checked against the original text. Numerical coincidence timing uses microseconds where PDF OCR incorrectly substitutes milliseconds. Models and pharmacological interpretations are identified separately from measured effects.
