# Lecture 72: original recordings added

The supplied Biocomputing II PPTX identifies itself as Lecture 72. The refreshed current repository default branch has no Lecture 72 deck or schedule entry. This revision preserves the supplied deck exactly and stores it here; no schedule, theme, title, date, body text, figure, existing shape position, or slide count was changed.

Four original article recordings were embedded: Kagan Video S2 on slide 7, Kagan Video S1 on slide 12, Cai Supplementary Video 2 on slide 36, and Cai Supplementary Video 1 on slide 37. The recordings and unedited original-frame posters occupy unused figure-column space. Existing credited article figures remain visible. Exact identifiers, sources, authors, licenses, DOI links, hashes, compatibility conversion, and source-specific teaching notes are saved in media_sources.json and appended speaker notes.

The package-preserving wrapper verifies that every original slide element and existing note paragraph has unchanged XML, and all untouched original package parts are byte-identical. Each embedded media hash and video/media relationship was verified. Every full clip decoded without errors, and all 46 rendered slides were visually reviewed. Interactive PowerPoint Slide Show playback was unavailable in this Linux environment.

The current repository checker cannot directly look up Lecture 72 because the authoritative schedule lacks it. A scratch copy of the unchanged checker was run with the exact uploaded title and Date TBD as temporary metadata. Both the supplied original and revised decks passed with zero failures and warnings. Repository schedule remains untouched. See media_qa.json.

To reproduce the revision from the instructor’s original uploaded deck, run from the repository root:

```bash
python lectures/L71/add_article_media.py ORIGINAL_BIOCOMPUTING_II.pptx lectures/L72/media_sources.json lectures/L72/Neuroethology_Lecture72_FA2026.pptx
```

The shared Kagan recordings and posters are stored under lectures/L71/media/; Cai recordings are under this lecture’s media/.
