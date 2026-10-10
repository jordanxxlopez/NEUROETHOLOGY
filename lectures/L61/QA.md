# Lecture 61 validation

The authoritative base was the freshly fetched default branch, commit 2159c81. Lecture 61 was registered with the exact instructor title and special-topic date Date TBD. The deck uses a new muted clay / paper white palette and Arial.

Repository build and checker: 46 slides, 44 content slides with primary article figures, 30 content slides with source-color images, zero failures and zero warnings. Each content slide contains three paragraphs (110–128 words) and a complete teaching transcript. Full DOI references appear in notes. Slide text contains no em dashes. Routine caveat endings were not copied from older decks.

All 46 native slides were rendered with LibreOffice and visually inspected. All 46 public-delivery HTML slides were browser-rendered and visually inspected. Browser QA confirmed loaded images, correct slide count and zero overflowing elements. Relevant electrical-property panels were enlarged without recoloring or reconstruction; source axes, scale bars and panel identifiers were preserved.

Published schematics and network simulations are original panels cropped from the cited articles, not drawings produced for this lecture. The authors’ network simulation is explicitly taught as their proposed explanation. Close anatomical appositions are described as putative synaptic contacts. The gephyrin method identifies combined inhibitory output, not a distinct GABA-versus-glycine assignment.

## Rebuild

```sh
python lectures/L61/write_spec.py
python tools/build_lecture.py lectures/L61/lecture.json
python tools/check_lecture.py lectures/L61/Neuroethology_Lecture61_FA2026.pptx --lecture 61
```

To regenerate original crops, restore PDFs to papers/ and run python lectures/L61/crop.py. This invokes the repository crop_panels.py and its supported PyMuPDF fallback. The fallback respects the PDFs’ CropBoxes; Poppler’s larger media-page rendering shifted otherwise identical fractional crop regions.
