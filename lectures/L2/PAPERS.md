# Lecture 2 — sources and figure provenance

Authoritative repository: current default branch `claude/neuroethology-fa2026-schedule-2lgmmr`, refreshed initially from `9dcd4e143b89436356a61b2d911ec7ca88513166`, then rebased onto `e4e16b0` to incorporate the new original-color preference.

Exact title: Fixed action patterns & sign stimuli — Lorenz and Tinbergen's stickleback and graylag goose work

Exact date: Wednesday, August 26, 2026

## Verified references

N. Tinbergen (1948). Social Releasers and the Experimental Method Required for Their Study. The Wilson Bulletin 60(1):6–51. Digitized article; repository DOI. https://doi.org/10.5281/zenodo.16185673

K. Lorenz; N. Tinbergen (1938). Taxis und Instinkthandlung in der Eirollbewegung der Graugans. I. Zeitschrift für Tierpsychologie 2(1):1–29. Archive edition identifies 1938; Crossref indexes this DOI under 1939. https://doi.org/10.1111/j.1439-0310.1939.tb01558.x

N. James; A. Bell (2021). Minimally invasive brain injections for viral-mediated transgenesis: New tools for behavioral genetics in sticklebacks. PLOS ONE 16(5):e0251653. https://doi.org/10.1371/journal.pone.0251653

S.A. Bukhari; M.C. Saul; C.H. Seward; H. Zhang; M. Bensky; N. James; S.D. Zhao; S. Chandrasekaran; L. Stubbs; A.M. Bell (2017). Temporal dynamics of neurogenomic plasticity in response to social interactions in male threespined sticklebacks. PLOS Genetics 13(7):e1006840. https://doi.org/10.1371/journal.pgen.1006840

## Source editions

The instructor supplied Lorenz and Tinbergen's goose paper. Its Konrad Lorenz Haus archive edition contains reformatted/OCR text, printed page breaks, and the original photographic panels. Its cover and running headers identify 1938; DOI/Crossref metadata index 1939. The slides cite the archived article year (1938) and retain this discrepancy in the notes. These crops are original article photographs, not a claim that the uploaded edition is an unmodified original-page facsimile.

Tinbergen (1948) was downloaded from Zenodo's BHL-derived record. Its repository DOI identifies the digitized original, not an original 1948 journal DOI. Author, title, volume, issue, pages and printed March 1948 date were checked against the PDF. Its MD5 matches the repository value `95593509e4a05485b1998e0cc1805bf0`. This synthesis includes author-reported classic experiments and figures credited to earlier studies. Its ten content slides are not counted toward the requirement of 34 unambiguous primary-study figure slides.

James and Bell (2021) and Bukhari et al. (2017) were downloaded as the publishers' open-access PDFs. Metadata were checked against article front matter and Europe PMC records. Web literature searches used Europe PMC and OpenAlex to locate and verify these primary sources. PDFs remain in ignored `papers/`; `crops.json` records every crop and can reproduce it with the repository's crop tools.

The supplied Burkhardt (2014) historical review, *Tribute to Tinbergen: Putting Niko Tinbergen’s ‘Four Questions’ in Historical Context*, Ethology 120:215–223, DOI https://doi.org/10.1111/eth.12200, was consulted for historical context. It supplies no scientific figure or primary experimental result in this deck.

## Final validation

All needed source PDFs are available; the earlier missing-PDF blocker is resolved. There are 46 slides, including 44 content slides with article images: ten Tinbergen synthesis slides, seventeen original goose-study slides, eleven James/Bell primary-study slides, and six Bukhari primary-study slides. Thus 34 content slides use figures from unambiguous primary experimental studies. The deck uses 31 unique original article crops and zero web or generated images. Repeated panels support distinct claims rather than fabricated replacement figures.

All content uses text-left/figures-right columns; paired figures remain within the right column. The title carries the original goose photograph. Original axes, panel letters, units and scale bars are preserved. The paper's film frames have no reported frame rate, so no invented millisecond durations are assigned. Modern gene, receptor and muscle interpretations are distinguished from directly measured effects; no neural or transmitter recordings are invented for the classic studies.

The refreshed repository added a preference for original color figures while this deck was being completed. After incorporating that update, the checker reports zero failures and one color-preference warning: 16 of the 44 image slides have color figures. The classic Tinbergen and goose experiments have no equivalent original color panels; their grayscale evidence is retained under the explicit exception, without recoloring or unrelated decoration. All 46 slides were inspected in the LibreOffice-rendered PDF; enlarged paired figures were reviewed again after final layout edits. Structured checks confirm Arial throughout and all objects inside slide bounds. The unused denim/ivory palette is recorded for Lecture 2 in `course/themes.json`.

The existing `AGENTS.md`, lecture skill, and `prompts/make_lecture.md` already preserve the instructor's no-created-images and two-column requirements. No replacement guideline file or ZIP was used. The managed build environment was verified with the repository tools; no setup configuration change was necessary.
