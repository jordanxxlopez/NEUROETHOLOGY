---
name: neuroethology-scaffold
description: Add exactly 14 scaffold teaching slides to a finished NEUR 411 Neuroethology lecture deck (46 → 60) without changing any original slide. Scaffold slides teach what the deck does not already say — mechanisms, consequences, integration across slides, method logic, distinctions, foundations — and never paraphrase or repeat the original slides. They clone the deck's own layout, reuse only figures already in the deck, never create diagrams or images, and contain no checkpoints, quizzes, roadmaps, figure-reading guides, summaries or cross-lecture links. Use whenever the user asks to scaffold a lecture, add the 14 slides, make the 60-slide version, or works with Lectures-Part1_2.zip / Lectures-Part2_2.zip.
---

# NEUR 411 scaffold slides

Read scaffold/GUIDELINE.md completely before starting and follow every rule in it. The essentials:

1. Input: the instructor's final decks from Lectures-Part1_2.zip and Lectures-Part2_2.zip in scaffold/input/ (45 files,
   both versions of Lectures 15, 16, 17, 19, 40). Always build from the original input, never from an earlier output.
2. The 46 original slides never change. Insert 14 slides and reorder <p:sldIdLst> only. Never run theme_colors.py or
   build_lecture.py on these decks.
3. A scaffold slide teaches what the original slides do not say. Each makes at least three teaching moves (mechanism,
   consequence, integration, method logic, distinction, foundation). Never paraphrase, condense, merge or copy original
   slides. Test: if a student could learn it from the neighboring slides, rewrite it.
4. Sources: the deck, the full text of papers the deck already cites, and textbook-level principles. No new studies,
   species, data, citations or numbers; no statistics clutter; no math unless visible in the deck; no other lectures.
5. Looks like the deck: clone a content slide of the same deck; claim-sentence title ≤ 62 characters; 3–5 paragraphs
   (90–170 words); a reused figure with its original caption on every scaffold slide; footer number like "24a".
6. Never: created images or diagrams, checkpoints, questions to students, roadmaps, figure-reading guides, summaries,
   "putting it together" titles.
7. Notes: teaching transcript that goes further than the slide, never copies it, no "Teaching transcript:" label, ends
   with References: copied from the original notes.
8. Verify with tools/check_scaffold.py (count, integrity, non-redundancy, teaching moves, source, language, format,
   visual, 60-page PDF) and update scaffold/REPORT.md.
