# Lecture 104B

**Social transmission of pain in animals: sensory cues, neural circuits, and how social interactions alter pain sensitivity across species.**

46 slides: title, 44 content slides, and six exam-level Key takeaways. Date: Date TBD. Arial, arctic slate theme. The repository's current default branch was refreshed before work. The demonstration exception for 104A–C remains authoritative.

## Scientific scope

Nine primary papers supply new material relative to 104A: Li 2018, Smith 2016, Nakamura 2024, Kasai 2025, Han 2024, Zhang 2025, Rein 2024, Zhang 2024, and Geng 2026. The direct pain-transfer and care evidence concerns rats and mice. Freezing, withdrawal thresholds, partner care, and endocrine responses are distinguished. The deck does not label defensive freezing as a direct pain-threshold measurement or imply uniform evidence across every animal taxon.

Every content slide has primary research imagery. There are 35 additional credited image placements; these are not 35 unique photographs. The companion images are original animal and anatomical panels, reused only where related to the slide. No figures, diagrams, data plots, images, or recordings were created or recolored. Figures for Zhang 2024 were obtained as the publisher's intact published figure PNGs because an accessible PDF was not available; its original manuscript and recordings were accessible.

## Embedded videos

20 clips on slides **3–7, 22–23, 26, 28, 30–31, and 36–44**, sourced from **15 distinct original experimental recordings**. Four excerpts separate Li's bee venom, formalin, CFA, and nerve-injury conditions. Separate excerpts of Geng's Video 5 distinguish neutral and injured partners; Video 6 separates the fluorescent control from GtACR2 inhibition. These are distinct experimental conditions, not duplicate clips. The remaining source recordings are retained in full.

Clips preserve native display proportions, scene order, original timing/speed, audio where present, and original labels. H.264/AAC conversion supports playback compatibility. A movie is embedded separately from its scientific figure and unaltered-frame static fallback. Metadata records source identifiers, URLs, DOI, authors, licenses, hashes, and excerpt boundaries. No YouTube, news, entertainment, narrated reports, or generated recordings were used.

Desktop PowerPoint GUI playback and Google Slides import were not tested. Google Slides may require uploading the videos to Drive and reinserting them. The PDF preview is static and does not play the videos.

## Reproduction

Use the tested `/workspace/lecture-venv/bin/python` environment. Run `write_spec.py`, the repository's `tools/build_lecture.py`, `embed_videos.py`, `verify_delivery.py`, and `tools/check_lecture.py --lecture 104B`, in that order. Embedding requires a fresh build. Original PDF sources are kept outside version control; `crops.json` and `source_access.json` record provenance. `prepare_media.py` records the source conversions and excerpts.

The named presentation skills were consulted; the instructor's explicit repository-builder requirement takes precedence over generic remote export and deck-length guidance. No Presenton-hosted export is represented as the embedded-media deliverable.
