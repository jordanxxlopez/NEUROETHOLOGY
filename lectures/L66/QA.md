# Lecture 66 validation

- Native build: `python tools/build_lecture.py lectures/L66/lecture.json`. 46 slides, 44 image slides, 44 article-figure slides, 22 in color, zero failures, zero warnings.
- Native presentation rendered through LibreOffice; all 46 slides inspected. PDF text-bound check: no words outside the slide.
- Matching Presenton document validated at 1280 × 720: all images loaded, 46 slide sections and speaker notes, Arial throughout, no text/image overflow. All 46 screenshots inspected before export.
- All figure crops were taken directly from the original PDFs with the repository tools, preserving panel labels, units, scale bars and scientific content. Color comes exclusively from the original source figures. The title photograph is an article panel.
- Exact schedule title and Date TBD retained. Three teaching paragraphs per content slide, six takeaway statements, no em dashes, no routine caveat-ending template, no prohibited framing or statistics in authored slide prose.
- Seven citations verified against source texts and DOI metadata. Lindburg et al. is dated 2001 by its journal record. The mate-choice cub-production comparison retains the successful-mating denominator. Genomic receptor classifications, microbial associations and hormonal timing are explained at the level measured by their respective studies.

Machine-readable results are in qa.json. Original source-access history and successful uploads are in source_access.json. Original PDF files remain locally available in the ignored papers directory.
