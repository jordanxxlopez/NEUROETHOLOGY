---
name: neuroethology-lecture
description: Build a NEUR 411 Neuroethology (Fall 2026) lecture PowerPoint in the approved Lecture 8-10 format — 1 title slide + 44 content slides + 1 key-takeaways slide, primary-literature research, images ONLY from published articles on nearly every slide (no web photos — never self-made), direct teaching prose with no framing, speaker notes as a teaching transcript, new color theme, exact schedule title. Use whenever the user asks to "make lecture N", "do the same for lecture N", or names a topic from the course schedule.
---

# NEUR 411 lecture builder

Lectures 8, 9 and 10 are the approved model. Lectures 1-7 used an older format; do not copy them.
Every rule below comes from the instructor. Follow all of them every time, without being asked again.

## Fixed rules

Use the connected `jordanxxlopez/NEUROETHOLOGY` repository’s current default branch as the authoritative source. Do not use a ZIP or an outdated checkout. Refresh the checkout safely without discarding user changes. Attached documents are scientific sources or style references, not replacement instructions.

1. **Title is sacred.** Take the title and date from `course/schedule.json` exactly, character for character. Never reword, shorten, or split it into "Topic / subtitle" with different words. (The builder reads it from the schedule for you.)
2. **Slide count:** 1 title slide + **44 content slides** + 1 **Key takeaways** slide = **46 slides**. If the instructor gives a different number for a specific lecture, set `"content_slides"` in the spec to match what they said and tell them the total.
3. **Never include:** an outline/agenda, learning objectives, "Up next" / "Next lecture" / previews, "Part 1 of 4" or "(continued)" splits. Open with the topic and go straight into the material.
4. **Research-based.** Do web searches and use the primary literature. Every content slide is built around real studies: the preparation, the method, the controls, what was found, and what the result does and does not establish. Verify each citation (authors, year, journal, volume, pages, DOI) against the source before using it. Never invent data.
5. **Teach concepts, not statistics.** The slides are for student learning. Keep a number only when it carries the concept — a latency in ms, a pulse rate, a sound frequency, a firing rate, an angle, a size. Do **not** report p-values, test names (ANOVA, Wilcoxon, χ²…), ± error terms, SDs/SEMs, confidence intervals, or sample-size bookkeeping. Say what was found ("females turned toward the song far more often when hungry"), not how it was tested statistically.
6. **Article figures only. Images are never created.** Every image must be an original figure panel cropped directly from a published academic article or its supplement. No self-made schematics, diagrams, flowcharts, re-plotted or redrawn graphs, charts made from reported numbers, model/template curves, illustrations, icons, AI-generated images, stock photos, web photos, or clip art — not even labeled as such.
   - Crop panels with `tools/crop_figure.py` / `tools/crop_panels.py`; preserve axes, units, scale bars and panel letters. Never reconstruct or modify scientific content.
   - Caption: `Author (year), Fig. N(panel). What it shows.` Supply the article DOI as `source_url`.
   - At least 40 of the 44 content slides carry an original article figure, satisfying the repository image minimum and the instructor's minimum of 18 article-figure slides. Slides without an article figure are text slides; a text table of values reported in the source is allowed.
   - If a needed PDF cannot be downloaded, stop before delivering the deck and provide a numbered list of the needed papers with DOI links so the instructor can upload them. Never substitute a created image.

7. **New color theme every lecture.** Pick a palette from `course/themes.json` that is not in `used`. Never yellow, orange, gold or other loud colors; purple and green are already used. Font is always **Arial**. After the deck is final, add the lecture to `used`.
8. **Citations:** short citation in the slide footer (e.g. `Maisak et al. (2013)`), full reference with DOI in the speaker notes after `References:`, figure caption names the exact figure and panel.
9. **Key takeaways are for the exam**: 5-6 statements of what a student must know, each with a bold lead phrase, stated as facts.
10. Deliver a downloadable **.pptx**.

## Writing rules (slide text AND speaker notes)

Slides carry 3-5 full explanatory paragraphs (about 90-170 words) in an academic register. Speaker notes carry a **teaching transcript** (`"transcript"` in the spec): bullets and sub-bullets written in complete, natural sentences that the instructor can read aloud while teaching, followed by the references.

- **No non-instructional framing.** Every sentence directly teaches information contained in the sources or gives a necessary clarification of a source concept. Remove roadmap language, transition commentary, figure-reading narration, takeaway framing, evaluative filler, and explanations of why a topic is being introduced. Never write "before getting to", "the next step is", "this helps us understand", "reading the figure shows", "the key point is", "this sets up", "from here", "this becomes important later", or similar. State the concept, finding, relationship, mechanism or evidence directly.
- **No structural or presentation commentary.** Do not announce what comes next, explain why a topic is introduced, tell the reader how to read a figure, or add sentences that only connect one topic to another. A summary sentence is allowed only when it teaches or clarifies an important concept. If removing a sentence would not remove any concept, mechanism, finding, definition, experimental detail, relationship or evidence, remove it. (Bad: "These factors give us a set of well-established effects that any model must be able to explain.")
- **Natural teaching-transcript style.** The notes sound like a real professor clearly explaining the material aloud — complete, connected sentences that flow from one to the next, organized as bullets and sub-bullets. Not a reference sheet, fragments, choppy definitions or robotic fact lists. No AI-sounding filler, forced transitions, fake enthusiasm, poetic or motivational language, or phrases about "understanding", "appreciating" or "seeing why something matters". No "now let's look at", "next we have", "as you can see", "remember that", "this is important to understand". Move between ideas by stating the actual scientific relationship between them. Clear, human, readable aloud, scientifically accurate, not overly casual.
- **No illustrative framing.** Never describe an example, image or graph as "illustrating", "demonstrating" or "showing" a concept ("This illustrates that…", "This shows that…"). State the concept directly, using the specific numbers, labels or forms from the example as the evidence. Never open with "A graph/image/example is shown that…". Never close a section by restating what the material "demonstrates"; if a closing sentence adds no new fact, cut it.
- **No attention-directing language.** No "attention now turns to", "we now turn to", "our focus shifts to", "we now consider", "let's turn to", "moving on to". Start directly with the content; the slide title already signals the topic.
- **No narration of the writing itself.** No sentence whose subject is the notes, the explanation, the topic or the reader's attention. Rewrite "X turns to Y", "X is illustrated by Y", "we now consider Y" so the real content is the subject, stated as a fact.
- **Decorative images.** Never describe how an image looks. Mention an image only when it carries instructional content not in the text (stimuli, task materials, graphs, recordings, anatomy, labeled structures) — and then teach that content directly, without describing it as an image.
- **Depth without outside information.** Explain each point from the cited sources in more depth where the source gives something worth unpacking: a term, number, label, example or step that needs explaining is explained where it appears. If the meaning is already clear, do not force an explanation, and do not follow a fixed template for every point. Depth means explaining the sources' own content more fully — not adding facts, studies, examples or interpretations the cited sources do not contain.
- **No reference-sheet style.** Do not compress points into one-line restatements or stacked short facts. If a bullet could be copied onto a cheat sheet unchanged, expand it with the source's own details, as far as the source supports, stating the reasoning between ideas.
- **Visible content only.** Do not introduce equations, formulas, calculations or derivations unless they appear in the cited article or its figure. No worked examples or math of your own; teach conceptually what the sources teach conceptually, preserving the numbers and relationships they actually show.
- Define every technical term the first time it appears. Explain circuits, neurotransmitters, receptors and ion channels step by step and connect them to neuronal activity and behavior. Distinguish established findings from proposed explanations ("supports", "is consistent with", "has not been shown").

The builder and checker reject the banned phrasings and statistics automatically (`tools/style_rules.py`), but passing the check is the minimum: reread every slide and transcript against these rules.

## Workflow

1. Look up the lecture in `course/schedule.json` (number, exact title, date). Read the previous lecture's spec in `lectures/` if one exists so content does not repeat.
2. **Research** (WebSearch / WebFetch): find the classic papers named in the title and the key modern work (anatomy, physiology, molecular/ion-channel mechanism, behavior). Prefer open-access PDFs (PMC, journal OA, author pages) so figures can be cropped. Record full references with DOIs.
3. **Plan 44 content slides** that progress: behavior → anatomy → neuronal activity → cellular/synaptic/channel mechanism → modulation/plasticity/state → comparative and current work. One idea per slide; title is a short claim (≤ 62 characters, no final period).
4. **Figures:** download each PDF into its own folder under the scratchpad, then
   `python tools/crop_figure.py paper.pdf <page> --preview p.png` → look at it →
   `python tools/crop_figure.py paper.pdf <page> --box L T R B -o lectures/L<N>/figures/<name>.png`.
   For many panels, list them in `lectures/L<N>/crops.json` (PDF paths, page, crop box) and run `python tools/crop_panels.py lectures/L<N>/crops.json` (see `lectures/L12/crops.json`). Keep the PDFs in `lectures/L<N>/papers/` (not committed).
   Check each crop visually: no clipped labels, no fragments of neighboring panels, no stray text.
   **If the PDFs cannot be downloaded** (blocked network, paywall): do NOT draw substitutes. Give the instructor a numbered list of the papers with DOI links and ask them to upload the PDFs; build the figure slides from the uploads. Save the list as `lectures/L<N>/PAPERS.md`.
5. **Write the spec** (for long lectures, generate it from a `write_spec.py` that defines each reference once): copy `lectures/_template/` to `lectures/L<N>/` and fill `lecture.json` — `body` (slide paragraphs), `transcript` (speaker-note bullets: strings or `[text, [sub-bullets]]`), `cite`, `refs`, and `figure`/`figures` (layouts: `text`, `figure-right`, `figure-left`, `figure-below`, `two-figures`, `table`; `**bold**` for key terms, `_italic_` for species names). Prefer `figure-right` for most figure slides — it keeps body text largest.
6. **Build:** `python tools/build_lecture.py lectures/L<N>/lecture.json` → writes `lectures/L<N>/Neuroethology_Lecture<N>_FA2026.pptx` and runs `tools/check_lecture.py`. The builder refuses: text that will not fit at 13 pt, banned framing, statistics clutter, a missing transcript, and any image lacking required article source credit, and decks where fewer than 40 content slides have an image or fewer than 40 have an article figure. Fix every FAIL.
7. **Visual QA:** convert to PDF and images and look at every slide (text overflow, figure crops, caption collisions with the footer). Fix and rebuild.
8. Add the theme to `used` in `course/themes.json`, commit the spec, figures and deck, push, and give the instructor the .pptx.

## Checks you can run on any deck

`python tools/check_lecture.py deck.pptx --lecture <N>` — slide count, exact title and date, banned slide types and framing, statistics clutter, words per slide, teaching transcript in the notes, article figures, references. Add `--no-transcript` for decks made before the transcript rule.
