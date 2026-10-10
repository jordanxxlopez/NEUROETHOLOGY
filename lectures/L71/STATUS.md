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
