# Scaffold slides: add 14 teaching slides to every lecture deck (46 → 60)

This file is the single source of truth for the scaffold task. AGENTS.md (Codex),
CLAUDE.md, and the neuroethology-scaffold skill (Claude Code) point here. When asked to
scaffold a lecture, add the 14 slides, make the 60-slide version, or work with
Lectures-Part1_2.zip / Lectures-Part2_2.zip, follow every rule in this file, every time,
without being asked again.

## 1. What a scaffold slide is

The finished decks are accurate but dense: most slides present one experiment, and students
struggle to connect them. For every deck, add exactly 14 scaffold slides so the deck has 60
slides.

A scaffold slide is a regular teaching slide that teaches something the original slides do
not already say. It explains the mechanism behind a finding, the reasoning behind a method
or control, the consequence of a result, or how findings on separate slides fit together
into one explanation. It looks exactly like the deck's own content slides, and its title
states what it teaches.

THE TEST: if a student could learn everything on a scaffold slide by reading the original
slides around it, the scaffold slide has failed and must be rewritten. A scaffold slide that
restates, paraphrases, condenses or merges original slides is not a scaffold slide.

## 2. Inputs, outputs and the repository

- Inputs: the instructor's final decks in Lectures-Part1_2.zip and Lectures-Part2_2.zip,
  unzipped into scaffold/input/. Process every .pptx they contain (45 files).
- For this task the zip decks are the authoritative decks. The repository rule "do not use
  a ZIP" refers to the repository's code, rules and specs, which still come from the
  current default branch. Never substitute decks from lectures/ or reference/; they may be
  older.
- Lectures 15, 16, 17, 19 and 40 have two versions each. Scaffold each file separately.
  Never merge, choose between, rename or delete versions.
- Outputs: scaffold/output/<OriginalName>_SCAFFOLDED.pptx and
  scaffold/output/<OriginalName>_SCAFFOLDED.pdf.
- Per-deck spec (committed): scaffold/specs/<OriginalName>.json, in the format of
  scaffold/specs/_template.json.
- Report (committed): scaffold/REPORT.md.
- scaffold/input/ and scaffold/output/ are git-ignored. Deliver decks and PDFs as
  downloads; commit specs, report and tools.
- Always build from the original input deck. Never build on top of an earlier
  _SCAFFOLDED output. Never modify the input files.

## 3. The original 46 slides never change

- Do not edit, rewrite, reformat, resize, recolor, move, delete or reorder any original
  slide, or any of its text, images, captions, citations, footer, slide number, speaker
  notes, fonts, colors, shapes or layout.
- The only change to a deck is inserting 14 new slides: add them, then rearrange
  <p:sldIdLst> in ppt/presentation.xml. Original slides keep their relative order.
- Never run tools/theme_colors.py, tools/build_lecture.py or any whole-deck rewriting tool
  on these decks.
- If anything would require changing an original slide, stop and report it.

## 4. Where the 14 slides go

There is no fixed position, order or set of slide types. Read the entire deck first (slide
text, captions, figures, speaker notes), then place each scaffold slide where students need
an explanation the deck does not give. Spread the 14 slides through the deck. Never put one
before the title slide or after Key takeaways. Avoid two scaffold slides in a row unless the
content requires it.

Typical places:
- before the first slide that depends on a principle, structure or method the deck uses
  without explaining it;
- after a run of slides on one study or one set of experiments, where no slide explains
  what the findings mean together;
- where a mechanism is spread across several slides and no slide explains the causal chain
  from start to finish;
- where two cell types, pathways, species, preparations or conditions are taught separately
  and the reason they differ is never explained;
- where two ideas are easy to confuse;
- after a dense figure whose meaning for the animal or the neuron is never stated.

## 5. THE CORE RULE: add teaching, never repeat it

### 5.1 What each scaffold slide must do

Each scaffold slide makes at least THREE of these six teaching moves. None of them may
already be stated on an original slide.

1. MECHANISM: explains why a finding happens, step by step, in sentences: what moves,
   opens, flows or changes, and what each step causes.
2. CONSEQUENCE: states what a finding means for the neuron, the circuit or the animal's
   behavior.
3. INTEGRATION: combines findings from two or more original slides (not only the
   neighboring one) into one explanation that no single slide states, naming the specific
   results it combines.
4. METHOD LOGIC: explains what alternative explanation a method or control removes, and
   what would have been wrongly concluded without it.
5. DISTINCTION: separates two ideas students commonly confuse (activation vs.
   inactivation, knockdown vs. knockout, necessity vs. sufficiency, behavioral vs. cellular
   threshold, function vs. ancestry, proximate vs. ultimate) and explains how the deck's
   results separate them.
6. FOUNDATION: gives background a dense slide assumes but never explains (what a
   conductance change does to membrane voltage, what a loading control measures, what a
   sensitive period is) and applies it directly to the deck's experiment.

### 5.2 What is never allowed

- Paraphrasing, rewording or condensing an original slide. Swapping synonyms, changing word
  order, shortening sentences or merging two slides' sentences is still repetition.
- Copying any sentence or clause from an original slide or its notes.
- Re-describing an experiment (preparation, manipulation, result) that an original slide
  already describes. Name the result in a few words, then explain beyond it.
- A slide built as "definition, then the result restated", or "the previous slide, shorter".

### 5.3 Definitions

A formal definition may be stated when the explanation needs it: one sentence per term,
never copied from an original slide. A definition alone never counts as one of the six
teaching moves unless it is FOUNDATION applied to the experiment.

### 5.4 Allowed sources (this replaces the earlier "deck content only" rule)

- Everything in the deck, including findings from slides far from the insertion point.
- The full text of the papers the deck already cites (introduction, methods, results,
  discussion, figure legends), found through the DOIs in the original speaker notes. Use
  them to explain what the slides compress.
- Foundational neuroscience principles at textbook level, stated as general principles, when
  they are needed to explain the deck's content.
- Not allowed: new studies, new species, new data, or any citation the deck does not
  already contain. Every number on a scaffold slide comes from the deck or its cited papers.
- Teach concepts, not statistics: no p-values, test names, ± errors, SD/SEM, confidence
  intervals or sample-size bookkeeping.
- Visible math only: no equations, formulas or calculations unless one is visibly shown in
  the deck. Explain relationships in words.
- No reference to any other lecture in the course. Each deck stands alone.
- Keep established findings separate from proposed explanations ("supports", "is consistent
  with", "has not been shown").

### 5.5 Example of the difference (the pattern applies to every deck)

From one deck, after a slide on sodium inactivation:

NOT ACCEPTABLE (repeats the original slide):
"Inactivation is a decline in a conductance despite continued conditions that first
activated it. Sodium conductance rose rapidly and then declined during a maintained
depolarization, unlike the sustained rise of potassium conductance."

ACCEPTABLE (mechanism + integration + consequence):
"Sodium and potassium conductances act on different timescales, and the action potential
follows from that timing. A small depolarization raises sodium conductance, sodium ions flow
inward, and the inflow depolarizes the membrane further, which raises sodium conductance
again. This positive feedback produces the rapid rising phase of the spike. Two slower
processes end it: sodium conductance inactivates while the membrane stays depolarized, and
the delayed rise in potassium conductance lets potassium flow outward and returns the
membrane toward rest. Until sodium inactivation recovers, a second stimulus cannot drive the
same regenerative rise, so recovery after a spike is a measurable change in the membrane's
state."

The acceptable version joins four original slides (potassium delay, sodium inactivation,
spike generation, recovery) into one causal explanation that none of them states, and adds
the principle of positive feedback. It adds no new study and no new number.

## 6. What a scaffold slide looks like

Clone the layout of an existing content slide in the SAME deck (title box, text boxes,
figure position, caption box, footer rule, citation box, slide-number box) and replace the
text. The clone is a new slide; the source slide is never touched. Read every position,
font, size, color and spacing value from that slide's XML. Never assume values or copy them
from another deck.

- TITLE: a claim sentence stating what the slide teaches, at most 62 characters, no final
  period, formatted exactly like the deck's content titles.
- BODY: 3–5 full explanatory paragraphs, about 90–170 words, never below 13 pt, with the
  deck's own font, size, color, paragraph spacing, bold key terms and italic species names.
- FIGURE (required): every scaffold slide carries a figure, because nearly every slide in
  these decks carries one. Copy a figure that is already in the deck and carries the
  evidence the slide explains, with its original caption character for character, placed
  and sized the way the deck places figures (text and figure side by side). Never move,
  crop, recolor or alter it. Never reuse a decorative photo. Do not use the same figure on
  two scaffold slides.
- FOOTER: the deck's own rule line and styles. Left: the short citation(s) of the studies
  the slide explains, written the way the deck writes them. Right, in the original
  slide-number position and format: the number of the original slide it follows plus a
  letter (24a, 24b), so original numbering stays correct.
- COLORS: only colors the deck's own content slides use, read from the deck.
- SPEAKER NOTES: required on every scaffold slide (section 9).

## 7. Forbidden

- Created images of any kind: schematics, diagrams, flowcharts, roadmaps, pathway boxes,
  arrows, icons, charts, tables built from reported numbers, illustrations, AI images.
  The only images on scaffold slides are figures already in the deck.
- Checkpoints, check-ins, quizzes, questions to students, think-pair-share or any classroom
  activity.
- Figure-reading guides ("How to read it", "Reading the figure", step lists for a panel).
- Agenda, outline, overview, section-divider, transition, recap or summary slides.
- Titles such as "Putting it together", "Summary", "Recap", "Review", "Checkpoint",
  "Overview", "Key concepts", "Where this leads", "How to read …", "Introduction to …" or
  "Part 1 of 4". A slide that combines findings is titled with the combined finding.
- New shapes, text boxes, cards or decorations beyond what the cloned original slide contains.

## 8. Writing rules (scaffold slide text AND notes)

The repository writing rules in AGENTS.md apply in full and are enforced by
tools/style_rules.py:
- No non-instructional framing: every sentence teaches content or clarifies a concept. No
  roadmap, transition, figure-reading or takeaway framing, evaluative filler, or
  explanation of why a topic is introduced ("before getting to", "the next step is", "this
  helps us understand", "reading the figure shows", "the key point is", "this sets up",
  "from here", "this becomes important later").
- No structural or presentation commentary. If deleting a sentence removes no concept,
  mechanism, finding, definition, experimental detail, relationship or evidence, delete it.
- No illustrative framing ("this illustrates/demonstrates/shows that…", "a graph is shown
  that…"); state the content directly, with the numbers and labels as evidence.
- No attention-directing language ("we now turn to", "moving on to", "let's turn to").
- No narration of the writing itself; the subject of every sentence is the science.
- Never describe how an image looks; teach the content it carries.
- No reference-sheet style: connected, complete sentences a professor could say aloud,
  stating the reasoning between ideas.
- Define each technical term where it first appears on the slide. Plain, precise,
  advanced-undergraduate language. No hedging, filler, enthusiasm, poetic or motivational
  language, or phrases about "understanding", "appreciating" or "seeing why something
  matters".
- Never start a sentence with "Because".

## 9. Speaker notes

- A natural teaching transcript in bullets and sub-bullets of complete, flowing sentences
  the instructor can read aloud. Main bullets 2–5 sentences, sub-bullets 1–3.
- The notes go further than the slide: they walk through the reasoning in more detail and
  name the original slides the explanation draws on.
- Never copy the slide text into the notes. No notes sentence may repeat a sentence from the
  slide body.
- Do not start with a label such as "Teaching transcript:". Start with the content.
- No teaching-process narration ("now let's look at", "next we have", "as you can see",
  "remember that", "this is important to understand").
- End with "References:" followed by the full references with DOIs, copied exactly from the
  original slides' notes.

## 10. Verification (required for every deck; tools/check_scaffold.py)

1. COUNT: exactly 60 slides. If an input does not have 46, still add exactly 14 and report
   the total.
2. INTEGRITY: match original slides by order (part names may change on save) and compare
   each original's slide XML, relationships, media bytes and notes with the input. All must
   be identical.
3. NON-REDUNDANCY: for each scaffold slide, compare its body and notes with the text and
   notes of all 46 original slides, ignoring case and punctuation:
   - FAIL if any run of 8 or more consecutive words matches an original slide's text or notes;
   - FAIL if any scaffold sentence has content-word Jaccard similarity ≥ 0.6 with any single
     original sentence (stopwords removed);
   - FAIL if more than 40% of the slide's content words also appear in the single most
     similar original slide (stopwords and the lecture's unavoidable technical terms
     removed);
   - FAIL if any notes sentence has similarity ≥ 0.6 with a sentence of the same slide's body.
4. TEACHING MOVES: the spec lists the teaching moves (section 5.1) each slide makes, with
   the original slides it integrates. FAIL if fewer than three. Then reread every scaffold
   slide and confirm the moves are real and not already stated on an original slide.
5. SOURCE: every number appears in the deck or its cited papers; no citation the deck lacks;
   no equation unless visible in the deck; no statistics clutter.
6. LANGUAGE: tools/style_rules.py (framing_problems, stats_problems) on all scaffold text and
   notes, plus a search for "illustrates", "demonstrates", "shows that", "turn to", "next",
   "key point", "as you can see", "remember", "note that", "putting it together",
   "checkpoint", "summary", "recap", "Teaching transcript", any "Lecture <number>"
   reference, and sentences beginning with "Because". Rewrite every hit.
7. FORMAT: every scaffold slide has a reused figure with its original caption, a footer
   number in the "24a" form, and the cloned slide's formatting.
8. VISUAL: render with soffice --headless --convert-to pdf and pdftoppm; inspect every
   scaffold slide for overflow, overlap, caption-footer collisions, unreadable figures and
   any mismatch with neighboring original slides. Fix only scaffold slides.
9. PDF: 60 pages.

## 11. Report

scaffold/REPORT.md, one section per deck: file name, slide count, integrity result, and a
table of the 14 scaffold slides with footer number, title, original slide it follows,
reused figure (original slide and caption), original slides integrated, cited papers used
for added explanation, teaching moves made, and non-redundancy scores (longest shared word
run, maximum sentence similarity, content-word overlap). List any problems needing the
instructor's attention.
