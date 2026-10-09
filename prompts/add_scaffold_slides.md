# Prompt: add the 14 scaffold slides

Paste the text below into Claude Code or Codex, opened on this repository, with Lectures-Part1_2.zip and
Lectures-Part2_2.zip in scaffold/input/. To do one deck, replace "every deck" with its file name.

Add 14 scaffold slides to every deck in scaffold/input/ so each has 60 slides. Follow scaffold/GUIDELINE.md
completely (Claude Code: the neuroethology-scaffold skill). Build from the original input decks only. Never change
any of the 46 original slides. Every scaffold slide must teach something the original slides do not already say,
making at least three teaching moves, and must never paraphrase or repeat an original slide. Place the slides
wherever students need them. Each slide clones the deck's own layout, reuses a figure already in the deck, and is
numbered after the slide it follows (24a). Never create diagrams or images. No checkpoints, questions to students,
roadmaps, figure-reading guides, summaries or references to other lectures. Run tools/check_scaffold.py until every
deck passes, render and inspect every scaffold slide, update scaffold/REPORT.md, commit, push, and give me each
<OriginalName>_SCAFFOLDED.pptx and .pdf.
