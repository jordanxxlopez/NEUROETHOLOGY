# Lecture 51 preparation

Authoritative default-branch revision: 392e085 (refreshed from origin for this request).
Exact title: Elephants II: Comparative Cognition, Vocal Learning, and Social Neurobiology
Exact date: Date TBD

Status: research paused at the instructor's missing-PDF gate. Do not export a partial deck.

## Content allocation to develop after source analysis

44 content slides: comparative cognition and sensory/task controls (12); cortical organization, neuron morphology, and limits of anatomical inference (8); vocal production learning and imitation controls (8); social recognition, leadership, disruption, and reassurance (12); comparative interpretation and unresolved neural mechanisms (4). One title slide and one six-point Key takeaways slide bring the total to 46.

This allocation is provisional, not a final slide outline or a completed scientific analysis. Claims and figure selections must be checked in the source PDFs before writing slides. Do not infer an elephant-specific transmitter, receptor, ion channel, or causal social circuit from a behavioral result or a neuronal shape.

## Remaining work

1. Receive the five source PDFs listed in PAPERS.md and verify their complete bibliographic details against the papers.
2. Analyze all original papers, including preparation, controls, measured findings, and limits. Compare against earlier elephant content to avoid repetition.
3. Select and visually inspect original PDF crops using tools/crop_figure.py or tools/crop_panels.py. Preserve source colors, panel letters, axes, units, and scale bars. Provide anatomy images whenever anatomy is discussed.
4. Choose a new allowed palette and record it in course/themes.json only after final validation. Do not reuse prior Atlantic ink / pearl or rosewood themes.
5. Write the 44-slide spec with 3–5 paragraphs, teaching transcripts, DOI references, and source-caption provenance. At least 40 content slides need images, at least 34 primary-paper figures, and color is sought on at least half.
6. Build with tools/build_lecture.py, run tools/check_lecture.py, and render and inspect every slide. Audit exact title/date, slide count, Arial, notes, source provenance, and figure readability.
7. Export once through Presenton, obtain a fresh public PPTX URL and browser preview, and verify both links before delivery.

## Setup evidence

Git fetch and default-branch refresh succeeded without discarding user changes. Existing Python virtual environment can open all nine downloaded PDFs. The repository's crop_figure.py rendered a source PDF successfully through pdftoppm. No extra package installation or environment configuration was needed for this preparation. No final lecture build, full slide QA, or public export has run.
