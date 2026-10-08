# Prompt: make a NEUR 411 lecture

Copy everything in the box below into Claude Code or Codex, opened on this repository. Change only the lecture number in the first line.

```text
Make Lecture [N] for NEUR 411 Neuroethology (Fall 2026) as a downloadable .pptx.

Use the exact title and date for Lecture [N] from course/schedule.json, character for
character. Follow the neuroethology-lecture rules in this repo (AGENTS.md /
.claude/skills/neuroethology-lecture/SKILL.md) and build with tools/build_lecture.py.

Format
- 46 slides: 1 title slide, 44 content slides, 1 "Key takeaways" slide (5–6 exam-level
  points, each with a bold lead phrase).
- No outline, agenda, learning objectives, "up next"/next-lecture slides, "Part 1 of 4"
  or "(continued)" splits, and no lecture metacommentary ("In this lecture we will…").
  Start with the topic and go straight into the material.
- A new color theme from course/themes.json that has not been used (never yellow, orange
  or gold; purple and green are retired). Arial throughout. Record the theme as used.

Content
- Do web searches and use the primary academic literature. Every content slide is built on
  real studies: preparation, methods, controls, measured results with numbers and units,
  and what the result does and does not show.
- 3–5 full paragraphs per slide in academic register. Define each technical term when it
  first appears. Explain circuits, transmitters, receptors and ion channels step by step and
  connect them to neuronal activity and behavior. Keep established findings separate from
  proposed explanations.
- Verify every citation (authors, year, journal, volume, pages, DOI). Short citation in the
  slide footer; full reference with DOI in the speaker notes.

Figures — strict
- Figures must come ONLY from published academic articles: panels cropped from the papers'
  PDFs (tools/crop_figure.py), with axes, units, scale bars and panel letters intact.
- Caption every figure "Author (year), Fig. N(panel). What it shows." and give the
  article's DOI as source_url.
- Do NOT create any figure: no schematics, diagrams, flowcharts, re-plotted or redrawn
  graphs, charts made from reported numbers, model/template curves, illustrations, icons,
  stock photos or clip art — not even labeled as such.
- If a paper's PDF cannot be downloaded, do not substitute anything. Stop and give me a
  numbered list of the papers you need with DOI links so I can upload the PDFs. Slides
  without an article figure are text slides (a table of reported values is fine).
- At least 15 content slides must carry an article figure.

Finish
- Run the builder and checker until there are 0 failures, render every slide and fix any
  text overflow or bad crops, then commit, push, and give me the .pptx.
```
