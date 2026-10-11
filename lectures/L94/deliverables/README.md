# Expanded Lecture 94 PowerPoint

The expanded deck has 46 slides and 25 embedded videos, including the eight additional excerpts requested by the instructor. The complete PPTX exceeds GitHub’s 100 MiB per-file limit, so its exact bytes are preserved in two parts. Run `python lectures/L94/deliverables/assemble_pptx.py` from the repository root to restore `lectures/L94/deliverables/Neuroethology_Lecture94_FA2026.pptx`. The script verifies every part and the final SHA-256. No codec conversion or media change occurs during assembly.

The older, tracked PPTX one directory above remains the preserved 17-video baseline. To rebuild the expanded version from source, run the repository builder, then `embed_media.py`, `add_eve_excerpts.py`, and `add_uploaded_excerpts.py` in that order. Only the final script writes the expanded PPTX here. The already checked-in excerpts suffice; regenerating excerpts additionally requires the original uploaded videos.

## Single-file browser download

[Download the unchanged expanded PPTX](https://media.githubusercontent.com/media/jordanxxlopez/NEUROETHOLOGY/aa70cd9a4f5d25ea50cecb9285e6aa6a913022be/lectures/L94/Neuroethology_Lecture94_FA2026_Download.pptx). The complete file is 119,072,985 bytes and contains all 25 embedded videos. No additional video compression, resolution reduction or content change was applied. This normal browser download avoids the connected-computer file viewer and its 40 MB preview limit. After download, embedded videos can play offline in PowerPoint. The GitHub LFS download was verified against the existing expanded PPTX SHA-256.

## Latest 32-video revision

[Download the complete 32-video PPTX](https://media.githubusercontent.com/media/jordanxxlopez/NEUROETHOLOGY/1fdcbd5ca961b61b5bab272c20d001247cce6bb9/lectures/L94/Neuroethology_Lecture94_FA2026_Download.pptx). This is a normal single-file browser download, 335676221 bytes. Its source videos are embedded; no connected-computer viewer or split-file assembly is required. All 25 existing recordings remain intact, and seven complete article-provided comparative videos are added on slides 28, 29, 30, 31, 33, 37 and 44. New videos retain their original quality and bytes.

Local output: `Neuroethology_Lecture94_FA2026_32videos.pptx`. After rebuilding/assembling the preserved 25-video master, run `python lectures/L94/add_late_recordings.py`. The GitHub LFS pointer at `../Neuroethology_Lecture94_FA2026_Download.pptx` resolves to the latest complete file. The older 25-video parts remain unchanged.

## Paragraph 3 text revision

Latest output: `Neuroethology_Lecture94_FA2026_Paragraph3_Revised.pptx`. Only paragraph 3 and its matching transcript on 20 flagged slides differ from the preserved 32-video deck. Recreate with `python lectures/L94/revise_paragraph3.py`; all media and layout remain unchanged. The root LFS download pointer resolves to this latest revision.

[Download the paragraph-3 revised PPTX](https://media.githubusercontent.com/media/jordanxxlopez/NEUROETHOLOGY/578a5eb5fc67a3832ec19fb6195ee40f4f539ebe/lectures/L94/Neuroethology_Lecture94_FA2026_Download.pptx). Full response and SHA-256 verified.

## Latest Rio revision

Latest output: `Neuroethology_Lecture94_FA2026_Rio_Revised.pptx`, with 33 embedded video placements. Reproduce from the preserved paragraph-3 revision with `python lectures/L94/add_rio_identity.py`. Rio replaces Joly on slide 35 and is also embedded on slide 32. The uploaded file is preserved without trimming, cropping, compression or resolution changes. The root GitHub LFS download points to this latest revision.

[Download the verified Rio-revised PPTX](https://media.githubusercontent.com/media/jordanxxlopez/NEUROETHOLOGY/b5e12a2c61c4246ec691cc713c5dd7f7d55d762d/lectures/L94/Neuroethology_Lecture94_FA2026_Download.pptx). Complete browser response and SHA-256 verified.
