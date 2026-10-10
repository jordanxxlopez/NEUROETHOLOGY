# Lecture 71 status

Completed as `Neuroethology_Lecture71_FA2026.pptx` using the current connected repository default branch and `tools/build_lecture.py`.

- Exact scheduled title and `Date TBD` preserved. The em dash in the sacred scheduled title is retained; content slides and takeaways contain none.
- 46 slides: title, 44 content slides, and six exam-level key takeaways with bold lead phrases. Each content slide contains three teaching paragraphs, with a complete teaching transcript and full DOI references in speaker notes.
- All 44 content slides carry original primary-paper figures. No images, diagrams, or plots were created, redrawn, recolored, or generated. Published panels that contain diagrams remain the authors’ original figures.
- Nine primary papers include the original DishBrain study and three additional Cortical Labs-associated studies on criticality, drug response, and neural organoid plasticity. Claims distinguish planar DishBrain cultures from organoids and performance from consciousness.
- Scholarly and web searches, source metadata, PDF provenance, and exact panel crops are saved. All requested source PDFs have been received.
- New iron blue / chalk white theme, Arial throughout. Title uses a 21 pt lower fit bound to keep its full long wording and the instructor attribution inside the slide. The builder’s new optional `title_min_pt` leaves existing decks’ default at 22 pt.
- Automated validation and visual review results are recorded in `qa.json`.

Rebuild: `python lectures/L71/write_spec.py` then `python tools/build_lecture.py lectures/L71/lecture.json`. With source PDFs available, regenerate original panels using `python lectures/L71/prepare_figures.py` and `python tools/crop_panels.py lectures/L71/crops.json`.

## Original recordings added, October 10, 2026

The instructor-uploaded Biocomputing I deck matches the repository Lecture 71 slide text. Its existing slide shape XML, formatting, figure bytes, geometry, and note paragraphs are preserved. Three original article recordings are embedded: Lancaster Supplementary Video 2 on slide 18, Kagan Video S1 on slide 28, and Kagan Video S2 on slide 31. The existing credited figure on slide 18 is its click-to-play poster; the other clips have unedited original-frame posters in unused space. No slides or existing text were changed.

media_sources.json records exact source identifiers, DOI links, publisher and archive URLs, credits, supplied licenses, original and delivered hashes, compatibility conversions, and teaching notes. media_qa.json records the revised deck hash, exact preservation checks, complete media decode, relationships, and visual review of all 46 rendered slides. The repository checker passes with zero failures and warnings. Interactive PowerPoint playback was unavailable in this environment.

After a fresh repository rebuild, restore the videos with:

```bash
python lectures/L71/add_article_media.py lectures/L71/Neuroethology_Lecture71_FA2026.pptx lectures/L71/media_sources.json lectures/L71/Neuroethology_Lecture71_FA2026.pptx
```

Use this only on a fresh deck without recordings; applying it to an already revised deck would duplicate the additions. The original qa.json describes the earlier content build; media_qa.json is the validation record for this video revision.
