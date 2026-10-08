# Lecture 12 — validation

The revised deck contains **46 slides**: one title, 44 content slides and six exam-level key takeaways on the final slide. The schedule title and date are unchanged. The new **pewter / pale blue** palette is recorded in `course/themes.json`; Arial is used in slides and speaker notes.

- All **44 content slides** contain original figures from the eleven verified primary articles; **28** contain native color. There are **60 article-image occurrences**, using **37 distinct content crops**, plus the published animal photograph on the title slide. No web photos or created scientific images are used.
- Each content slide has three explanatory paragraphs, **113–137 words**, and a complete-sentence teaching transcript. Full references with DOI appear after `References:`; each figure has its own exact article/figure caption and DOI source.
- The repository builder and checker report **0 failures and 0 warnings**. Source PNG bytes are preserved exactly in the PPTX. No figure was recolored, reconstructed or redrawn.
- The PDF contains **46 pages**. Every slide was visually reviewed; corrected crops and enlarged layouts were rendered and reviewed again. Exported text remains inside the slide boundaries.
- Layer comparisons in depth estimation, contour-analysis accounts, predicted filtered spectral channels, anatomical convergence and candidate transmitter labeling are distinguished from direct neural evidence. Findings from different spider genera are identified explicitly. Unmeasured postsynaptic receptors and ion channels are not invented.

Rebuild from the source PDFs listed in `PAPERS.md`:

```bash
python tools/crop_panels.py lectures/L12/crops.json
python lectures/L12/build.py
soffice --headless --convert-to pdf --outdir lectures/L12 lectures/L12/Neuroethology_Lecture12_FA2026.pptx
```

`build.py` calls the authoritative repository builder, adds the title-photograph credit and final-slide teaching notes, applies Arial to speaker notes and reruns the checker. PDF inputs remain ignored by Git. Crops are reproducible from `crops.json`; source hashes and retrieval provenance are in `research.json`. Final artifact sizes, hashes and verification counts are in `validation.json`.

The cloud workflow was verified using the existing Python environment, LibreOffice, Poppler and native Git access. No additional environment configuration is needed.
