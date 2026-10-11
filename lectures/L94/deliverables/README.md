# Expanded Lecture 94 PowerPoint

The expanded deck has 46 slides and 25 embedded videos, including the eight additional excerpts requested by the instructor. The complete PPTX exceeds GitHub’s 100 MiB per-file limit, so its exact bytes are preserved in two parts. Run `python lectures/L94/deliverables/assemble_pptx.py` from the repository root to restore `lectures/L94/deliverables/Neuroethology_Lecture94_FA2026.pptx`. The script verifies every part and the final SHA-256. No codec conversion or media change occurs during assembly.

The older, tracked PPTX one directory above remains the preserved 17-video baseline. To rebuild the expanded version from source, run the repository builder, then `embed_media.py`, `add_eve_excerpts.py`, and `add_uploaded_excerpts.py` in that order. Only the final script writes the expanded PPTX here. The already checked-in excerpts suffice; regenerating excerpts additionally requires the original uploaded videos.

## Single-file browser download

[Download the unchanged expanded PPTX](https://media.githubusercontent.com/media/jordanxxlopez/NEUROETHOLOGY/aa70cd9a4f5d25ea50cecb9285e6aa6a913022be/lectures/L94/Neuroethology_Lecture94_FA2026_Download.pptx). The complete file is 119,072,985 bytes and contains all 25 embedded videos. No additional video compression, resolution reduction or content change was applied. This normal browser download avoids the connected-computer file viewer and its 40 MB preview limit. After download, embedded videos can play offline in PowerPoint. The GitHub LFS download was verified against the existing expanded PPTX SHA-256.
