# Expanded Lecture 94 PowerPoint

The expanded deck has 46 slides and 25 embedded videos, including the eight additional excerpts requested by the instructor. The complete PPTX exceeds GitHub’s 100 MiB per-file limit, so its exact bytes are preserved in two parts. Run `python lectures/L94/deliverables/assemble_pptx.py` from the repository root to restore `lectures/L94/deliverables/Neuroethology_Lecture94_FA2026.pptx`. The script verifies every part and the final SHA-256. No codec conversion or media change occurs during assembly.

The older, tracked PPTX one directory above remains the preserved 17-video baseline. To rebuild the expanded version from source, run the repository builder, then `embed_media.py`, `add_eve_excerpts.py`, and `add_uploaded_excerpts.py` in that order. Only the final script writes the expanded PPTX here. The already checked-in excerpts suffice; regenerating excerpts additionally requires the original uploaded videos.
