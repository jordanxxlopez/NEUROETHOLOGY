# Prompt: make a NEUR 411 lecture

Copy everything in the box below into Claude Code or Codex, opened on this repository. Change only the lecture number in the first line.

```text
Make Lecture [N] for NEUR 411 Neuroethology (Fall 2026) as a downloadable .pptx.

Use the connected jordanxxlopez/NEUROETHOLOGY repository, current default branch, as
the authority. Do not use a ZIP or an outdated checkout.

Use the exact title and date for Lecture [N] from course/schedule.json, character for
character. Follow the neuroethology-lecture rules in this repo (AGENTS.md /
.claude/skills/neuroethology-lecture/SKILL.md) and build with tools/build_lecture.py.

FORMAT
- 46 slides: 1 title slide, 44 content slides, 1 "Key takeaways" slide (5–6 exam-level
  points, each with a bold lead phrase, stated as facts).
- No outline, agenda, learning objectives, "up next"/next-lecture slides, "Part 1 of 4"
  or "(continued)" splits. Start with the topic and go straight into the material.
- A new color theme from course/themes.json that has not been used (never yellow, orange
  or gold; purple and green are retired). Arial throughout. Record the theme as used.

CONTENT
- Do web searches and use the primary academic literature. Every content slide is built on
  real studies: preparation, methods, controls, what was found, and how it works (mechanism,
  circuit, link to behavior). Verify every citation (authors, year, journal, volume, pages, DOI). Short
  citation in the slide footer; full reference with DOI in the speaker notes.
- Teach concepts, not statistics. Keep numbers only when they carry the concept (latencies
  in ms, pulse rates, sound frequencies, firing rates, angles, sizes). No p-values, test
  names, ± errors, SD/SEM, confidence intervals or sample-size bookkeeping.
- Slides: 3–5 full paragraphs in academic register. Speaker notes: a teaching transcript —
  bullets and sub-bullets in complete, natural sentences I can read aloud while teaching —
  followed by the references.
- Define each technical term when it first appears. Explain circuits, transmitters,
  receptors and ion channels step by step and connect them to neuronal activity and
  behavior. A limitation gets a sentence only when it changes
  what students should conclude; not on every slide. No fixed paragraph structure; no em dashes
  in slide text.

WRITING (slides and notes)
- NO NON-INSTRUCTIONAL FRAMING: every sentence directly teaches information from the sources
  or clarifies a source concept. No roadmap language, transition commentary, figure-reading
  narration, takeaway framing, evaluative filler, or explanations of why a topic is
  introduced ("before getting to", "the next step is", "this helps us understand", "reading
  the figure shows", "the key point is", "this sets up", "from here", "this becomes
  important later"). State the concept, finding, relationship, mechanism or evidence directly.
- NO STRUCTURAL OR PRESENTATION COMMENTARY: do not announce what comes next, explain why a
  topic is introduced, tell the reader how to read a figure, or add sentences that only
  connect topics. If removing a sentence would not remove any concept, mechanism, finding,
  definition, experimental detail, relationship or evidence, remove it.
- NATURAL TEACHING TRANSCRIPT STYLE: sounds like a real professor explaining aloud; complete
  connected sentences, still in bullets and sub-bullets; not a reference sheet, fragments or
  robotic fact lists. No AI filler, forced transitions, fake enthusiasm, poetic or
  motivational language, no "understanding/appreciating/seeing why it matters", no "now
  let's look at", "next we have", "as you can see", "remember that", "this is important to
  understand". Move between ideas by stating the scientific relationship between them.
- NO ILLUSTRATIVE FRAMING: never "this illustrates/demonstrates/shows that…", never "a
  graph/image/example is shown that…", never a closing sentence restating what the material
  "shows". State the concept directly, using the example's numbers or labels as evidence.
- NO ATTENTION-DIRECTING LANGUAGE: no "attention now turns to", "we now turn to", "our focus
  shifts to", "we now consider", "let's turn to", "moving on to".
- NO NARRATION OF THE WRITING ITSELF: the subject of every sentence is the science, never the
  notes, the explanation, the topic or the reader's attention.
- DECORATIVE IMAGES: never describe how an image looks. Mention an image only when it carries
  instructional content not in the text, and then teach that content directly.
- DEPTH WITHOUT OUTSIDE INFORMATION: unpack terms, numbers, labels and steps from the cited
  sources where they need it; do not force explanations or follow a fixed template; do not
  add facts, studies or interpretations the sources do not contain.
- NO REFERENCE-SHEET STYLE: no one-line restatements or stacked short facts; expand with the
  source's own details and reasoning.
- VISIBLE CONTENT ONLY: no equations, formulas or calculations unless they appear in the
  cited article or figure; no worked examples or math of your own.

IMAGES — ON NEARLY EVERY SLIDE
- Never create images: no schematics, diagrams, flowcharts, re-plotted or redrawn graphs,
  charts from reported numbers, model/template curves, illustrations, icons, AI-generated
  images or clip art — not even labeled as such.
- Almost every slide has a figure, not just a minimum number; ignore any "at least 15/18
  figures" requirement. At least 40 of the 44 content slides carry an image, and at least 34
  carry a figure cropped from a primary paper (tools/crop_figure.py) with axes, units, scale
  bars and panel letters intact; caption "Author (year), Fig. N(panel). What it shows." and
  the DOI as source_url.
- The title slide shows the study animal so students see what the lecture is about: a
  figure of the animal from a primary paper or a credited web photo.
- When a slide discusses a specific brain region, neuron, sense organ or other structure,
  include an anatomy image of it (an article figure first, otherwise a credited web image).
- Prefer color figures: grayscale-only decks tire students. Among a paper's panels, or
  between papers showing the same finding, pick colorful ones (fluorescence and stained
  micrographs, color-coded maps, heat maps, color traces and plots, color photos of the
  animal); aim for color on at least half of the image slides. The color must come from the
  source: never recolor, tint or edit a figure, and never make one. Backgrounds stay as they are.
- Credited web images (Wikimedia Commons, museum, lab or atlas pages; caption "Photo: …"
  with credit, license and source_url) are fine where they help, including
  neuroscience-related ones; at most 10 per deck; never generic decoration.
- If a paper's PDF cannot be downloaded, do not substitute anything. Stop and give me a
  numbered list of the papers you need with DOI links so I can upload the PDFs.

LAYOUT
- Use two columns: text on one side and scientific figures on the other. Keep figures
  large, readable, and aligned with the corresponding text. Avoid figures at the bottom
  beneath the text.

FINISH
- Run the builder and checker until there are 0 failures, reread every slide and transcript
  against the writing rules, render every slide and fix any text overflow or bad crops,
  then commit, push, and give me the .pptx.
```

## Lecture 72 particulars

Use Lecture 72, its exact registered title, and Date TBD. Preserve the instructor-supplied em dash only in the sacred course title; use no em dashes in other slide text. Every paragraph teaches; include a caveat only when it changes the scientific conclusion. Crop original published figures only. Require at least 40 image content slides, including 34 primary article figure slides. No Required Field Experience material. Treat the 2026 Doom mention as a reported extension unless primary technical results are obtained. Do not infer subjective experience from adaptive gameplay. The published Brainoware PDF has been supplied and verified. Use its original panels.
