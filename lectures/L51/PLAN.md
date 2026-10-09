# Lecture 51 build record

Authoritative default-branch revision: 392e085, refreshed for this request.
Exact title: Elephants II: Comparative Cognition, Vocal Learning, and Social Neurobiology
Exact date: Date TBD

46 slides: title, 44 content slides, six-point Key takeaways. Three academic paragraphs per content slide, complete teaching transcripts and DOI references. All 44 content slides carry original article figures drawn from 14 primary papers. Arial throughout; new glacier-blue-paper theme. The color preference remains a warning because many foundational sources are grayscale; published figures were never recolored.

The narrative connects sensory-appropriate cognitive tests, neuronal morphology, vocal imitation, social knowledge and affiliative behavior. Controlled findings are separated from hypotheses. Morphology does not establish empathy circuits; behavioral tasks do not identify elephant-specific transmitters, channels, or causal circuitry.

Build with:
```sh
python lectures/L51/write_spec.py
python tools/build_lecture.py lectures/L51/lecture.json
python lectures/L51/finalize.py
python tools/check_lecture.py lectures/L51/Neuroethology_Lecture51_FA2026.pptx --lecture 51
```

The finalizer sets the exact title as one editable Arial paragraph and adds complete DOI links to notes. Native output passes the repository checker with zero failures and the color preference warning. All 46 rendered slides were inspected for text fit, original labels and caption readability. Sources/validation.json and figure-provenance.json record the checks. Public Presenton delivery uses fresh validated HTML translated from the verified native deck, preserving source image assets and speaker notes.

Environment setup: runtime and onboarding skills applied; network access, Git fetch, Python, source PDF opening, Poppler cropping, LibreOffice rendering, and repository build/check tools verified. No new packages or environment configuration were required.
