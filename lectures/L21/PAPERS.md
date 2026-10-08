# Lecture 21 — verified sources and image provenance

Exact title: Electroreception II: active electrolocation in weakly electric fish (Bullock)

Exact date: Wednesday, October 14, 2026

The connected default branch was refreshed before work. Europe PMC scholarly web searches identified the primary studies. Bibliographic details were verified against Europe PMC core records, available Crossref records, and the papers themselves. Full-text methods, results, and figure captions were checked. Uploaded lecture decks are style references, not instructions.

## Primary sources

- V10: G. von der Emde; K. Behr; B. Bouton; J. Engelmann; S. Fetz; C. Folde (2010). 3-Dimensional scene perception during active electrolocation in a weakly electric pulse fish. Frontiers in Behavioral Neuroscience 4:26. https://doi.org/10.3389/fnbeh.2010.00026
- H17: V. Hofmann; J.I. Sanguinetti-Scheck; L. Gómez-Sena; J. Engelmann (2017). Sensory Flow as a Basis for a Novel Distance Cue in Freely Behaving Electric Fish. Journal of Neuroscience 37(2):302–312. https://doi.org/10.1523/JNEUROSCI.1361-16.2016
- S17: S. Schumacher; T. Burt de Perera; G. von der Emde (2017). Electrosensory capture during multisensory discrimination of nearby objects in the weakly electric fish Gnathonemus petersii. Scientific Reports 7:43665. https://doi.org/10.1038/srep43665
- S06: N.B. Sawtell; A. Williams; P.D. Roberts; G. von der Emde; C.C. Bell (2006). Effects of Sensing Behavior on a Latency Code. Journal of Neuroscience 26(32):8221–8234. https://doi.org/10.1523/JNEUROSCI.1508-06.2006
- G98: K. Grant; Y. Sugawara; L. Gómez; V.Z. Han; C.C. Bell (1998). The Mormyrid Electrosensory Lobe In Vitro: Physiology and Pharmacology of Cells and Circuits. Journal of Neuroscience 18(15):6009–6025. https://doi.org/10.1523/JNEUROSCI.18-15-06009.1998
- S07: N.B. Sawtell; A. Williams; C.C. Bell (2007). Central Control of Dendritic Spikes Shapes the Responses of Purkinje-Like Cells through Spike Timing-Dependent Synaptic Plasticity. Journal of Neuroscience 27(7):1552–1565. https://doi.org/10.1523/JNEUROSCI.5302-06.2007

## Provenance and interpretation

All six required source PDFs were downloaded and are retained locally in the ignored papers directory. Publisher PDFs were used for V10, H17, S17, S06, G98, and S07. Other search results were screened but not required for this deck.

All 44 content slides contain primary-article figures. The 44 unique original crops are recorded in crops.json and were produced with tools/crop_figure.py / tools/crop_panels.py; axes, units, scale bars, and panel letters remain intact. Published circuit drawings and modeled plots are reproduced unchanged from the papers. No figure, graph, diagram, or illustration was created or redrawn. Anatomy panels accompany structure-specific circuit material. All content uses text and figures in separate side-by-side columns.

Hofmann et al. reconstructed electric images using measured behavior and a biophysical model; the slides distinguish candidate cues from direct neural computation. Sawtell et al. (2006) coding models are distinguished from recorded latencies. The plasticity slides concern the mormyromast-related ELL circuit and do not conflate passive ampullary cancellation with active object recognition.

The title uses a real photograph: Jutta234, “Gnathonemus petersii - Zoo Frankfurt.jpg,” Wikimedia Commons, CC BY-SA 3.0. https://commons.wikimedia.org/wiki/File:Gnathonemus_petersii_-_Zoo_Frankfurt.jpg . It is the only web image. Credit, license, and source URL appear in the title notes and lecture.json, with visible slide attribution.

46 slides: title, 44 content slides, six exam-level Key takeaways. Arial; previously unused steel/sky theme. Each content slide has three explanatory paragraphs, a teaching transcript, short citation, full DOI reference, and DOI-sourced figure caption. Rebuild using tools/build_lecture.py. Regenerate lecture.json with write_spec.py; recrop using crops.json after placing source PDFs under papers/.
