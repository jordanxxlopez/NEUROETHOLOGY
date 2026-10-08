# NEUR 411 Neuroethology — lecture builder (instructions for coding agents)

This repo builds the course's lecture PowerPoints. When asked to "make lecture N" (or given a topic from `course/schedule.json`), follow every rule and step below. Claude Code reads the same rules from `.claude/skills/neuroethology-lecture/SKILL.md`; keep the two files in sync. A copy-paste prompt is in `prompts/make_lecture.md`.

Lectures 8, 9 and 10 are the approved model. Lectures 1-7 used an older format; do not copy them.
Every rule below comes from the instructor. Follow all of them every time, without being asked again.

## Fixed rules

1. **Title is sacred.** Take the title and date from `course/schedule.json` exactly, character for character. Never reword, shorten, or split it into "Topic / subtitle" with different words. (The builder reads it from the schedule for you.)
2. **Slide count:** 1 title slide + **44 content slides** + 1 **Key takeaways** slide = **46 slides**. If the instructor gives a different number for a specific lecture, set `"content_slides"` in the spec to match what they said and tell them the total.
3. **Never include:** an outline/agenda, learning objectives, "Up next" / "Next lecture" / previews, "Part 1 of 4" or "(continued)" splits. Open with the topic and go straight into the material.
4. **Research-based.** Do web searches and use the primary literature. Every content slide is built around real studies: the preparation, the method, the controls, what was found, and what the result does and does not establish. Verify each citation (authors, year, journal, volume, pages, DOI) against the source before using it. Never invent data.
5. **Teach concepts, not statistics.** The slides are for student learning. Keep a number only when it carries the concept — a latency in ms, a pulse rate, a sound frequency, a firing rate, an angle, a size. Do **not** report p-values, test names (ANOVA, Wilcoxon, χ²…), ± error terms, SDs/SEMs, confidence intervals, or sample-size bookkeeping. Say what was found ("females turned toward the song far more often when hungry"), not how it was tested statistically.
6. **Images are never created.** No schematics, diagrams, flowcharts, re-plotted or redrawn graphs, charts made from reported numbers, model/template curves, illustrations, icons, AI-generated images, clip art — not even labeled as such. Two kinds of image are allowed, and only these:
   - **Article figures (the priority).** Panels cropped from peer-reviewed articles (or their supplements) found through web search / the academic literature, with axes, units, scale bars and panel letters intact. Caption: `Author (year), Fig. N(panel). What it shows.` plus the article DOI as `source_url`. At least 18 content slides carry an article figure; Lectures 8-10 had 20+.
   - **Web photos, only where needed.** A real photograph from a credited web source (Wikimedia Commons, a museum, a lab or university page) for general orientation — e.g. the animal on the title slide or the first slide, its habitat, a specimen. Caption `Photo: <what it is>.` with `credit`, `license` and `source_url`. At most 4 per deck. Do not add images just for decoration.
   If no article figure is available for a slide, make it a text slide (a table of values reported in the paper is allowed as text).
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
2. **Research** (use web search; open papers in the browser or download PDFs): find the classic papers named in the title and the key modern work (anatomy, physiology, molecular/ion-channel mechanism, behavior). Prefer open-access PDFs (PMC, journal OA, author pages) so figures can be cropped. Record full references with DOIs.
3. **Plan 44 content slides** that progress: behavior → anatomy → neuronal activity → cellular/synaptic/channel mechanism → modulation/plasticity/state → comparative and current work. One idea per slide; title is a short claim (≤ 62 characters, no final period).
4. **Figures:** download each PDF into its own scratch folder outside `lectures/`, then
   `python tools/crop_figure.py paper.pdf <page> --preview p.png` → look at it →
   `python tools/crop_figure.py paper.pdf <page> --box L T R B -o lectures/L<N>/figures/<name>.png`.
   Check each crop visually: no clipped labels, no fragments of neighboring panels, no stray text.
   **If the PDFs cannot be downloaded** (blocked network, paywall): do NOT draw substitutes. Give the instructor a numbered list of the papers with DOI links and ask them to upload the PDFs; build the figure slides from the uploads. Save the list as `lectures/L<N>/PAPERS.md`.
   **Web photos:** download only real photographs with a clear license (e.g. Wikimedia Commons file page); record credit, license and page URL.
5. **Write the spec** (for long lectures, generate it from a `write_spec.py` that defines each reference once): copy `lectures/_template/` to `lectures/L<N>/` and fill `lecture.json` — `body` (slide paragraphs), `transcript` (speaker-note bullets: strings or `[text, [sub-bullets]]`), `cite`, `refs`, and `figure`/`figures` (layouts: `text`, `figure-right`, `figure-left`, `figure-below`, `two-figures`, `table`; `**bold**` for key terms, `_italic_` for species names). Prefer `figure-right` for most figure slides — it keeps body text largest.
6. **Build:** `python tools/build_lecture.py lectures/L<N>/lecture.json` → writes `lectures/L<N>/Neuroethology_Lecture<N>_FA2026.pptx` and runs `tools/check_lecture.py`. The builder refuses: text that will not fit at 13 pt, banned framing, statistics clutter, a missing transcript, and any image that is not a credited article figure or credited web photo. Fix every FAIL.
7. **Visual QA:** `soffice --headless --convert-to pdf <deck>.pptx` then `pdftoppm -jpeg -r 60 <deck>.pdf slide`, and look at every slide image (text overflow, figure crops, caption collisions with the footer). Fix and rebuild.
8. Add the theme to `used` in `course/themes.json`, commit the spec, figures and deck, push, and give the instructor the .pptx.

## Checks you can run on any deck

`python tools/check_lecture.py deck.pptx --lecture <N>` — slide count, exact title and date, banned slide types and framing, statistics clutter, words per slide, teaching transcript in the notes, article figures, references. Add `--no-transcript` for decks made before the transcript rule.

## Setup

```bash
pip install -r requirements.txt      # python-pptx, Pillow
# also needed: poppler (pdftoppm) and LibreOffice (soffice) for figure crops and visual QA
#   macOS:  brew install poppler && brew install --cask libreoffice
#   Ubuntu: sudo apt install poppler-utils libreoffice
```

## Repo map

- `course/schedule.json` — all 40 lecture numbers, dates and exact titles.
- `course/themes.json` — used themes and available palettes.
- `tools/build_lecture.py` — spec (`lecture.json`) → .pptx, then runs the checker. Enforces the image, writing and statistics rules.
- `tools/check_lecture.py` — rule checker for any deck.
- `tools/style_rules.py` — banned framing phrases, statistics patterns and image-caption rules shared by both tools.
- `tools/crop_figure.py` — cut figure panels from paper PDFs.
- `lectures/_template/` — starter spec showing every layout, a transcript and a web photo.
- `lectures/L12/` — worked example of article panels (`crop_panels.py`); built before the transcript rule.
- `lectures/L14/PAPERS.md` — papers to upload for Lecture 14.
- `reference/` — approved Lectures 8–11 decks.
- `prompts/make_lecture.md` — the request prompt to paste into Claude or Codex.
- `chatgpt/` — setup guide, Project instructions and per-lecture message for ChatGPT.

