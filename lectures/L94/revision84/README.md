# Lecture 94: fourteen-slide expansion and writing revision

The instructor authorized rewriting the existing teaching paragraphs while preserving
their findings, figures and videos. The resulting deck has 84 slides: the preserved
title, 82 content slides, and one final **Key takeaways** slide. New content occupies
slides 70–83. All 38 existing movie placements remain.

## Writing requirements for this revision

- Three teaching paragraphs on each content slide, each with 5–7 complete sentences
  and at least five rendered lines. This version uses five sentences per paragraph.
- Teach the scientific content directly. Define terms where first introduced and
  explain the source's own methods, actions, results and relationships.
- No roadmaps, lecture narration, figure-reading instructions, routine caveats or
  cautionary closing paragraphs. Paragraph 3 adds scientific content.
- State an indispensable qualification as a scientific fact only when required for
  accurate interpretation. Do not insert limitations to fill a paragraph position.
- Use natural wording suitable for speaking aloud. Avoid cumbersome strings of
  abstract nouns and redundant closing clauses.
- Preserve the previous findings, all existing figures, native video bytes and audio,
  title, date, theme and the single final summary. No lossy media processing.

The current default-branch `AGENTS.md` and
`.claude/skills/neuroethology-lecture/SKILL.md` supply the remaining requirements.
The instructor's sentence and rendered-line requirements override the older default
word-count guidance for this specific revision.

## Sources and build

`revised_paragraphs.json` contains the 68 rewritten existing content slides.
`additions.json` contains the 14 added slides and their teaching transcripts, figure
credits and full references. Original published panels are cropped with the repository
tool according to `crops.json`. `academic_search.json` records Europe PMC searches;
`verified_crossref.json` records citation metadata checked against the actual papers.

The preserved 70-slide baseline is
`../deliverables/Neuroethology_Lecture94_FA2026_70slides_SingleSummary.pptx`, SHA-256
`37b42982e516a3b33c47285fe18211579261ad828add63fef3d519a23145a5c6`.
Its archived browser-download URL is:

https://media.githubusercontent.com/media/jordanxxlopez/NEUROETHOLOGY/308be4fc2dfd05ba034a967b4650ad65dfb1fb47/lectures/L94/Neuroethology_Lecture94_FA2026_Download.pptx

From the repository root:

```bash
python tools/build_lecture.py lectures/L94/revision84/additions.json lectures/L94/revision84/Added14_Base.pptx
python lectures/L94/revision84/build_revision.py
python tools/check_lecture.py lectures/L94/deliverables/Neuroethology_Lecture94_FA2026_84slides_Revised.pptx --lecture 94 --content-slides 82
```

The assembly replaces only the teaching body and its corresponding note transcript
on existing content slides. All other existing shapes are preserved. It imports only
the donor's 14 content slides before the original final summary, reusing identical
slide layouts, slide masters, notes master and theme parts. It never adds a second
notes master or resaves existing media through a presentation library.

Text uses Arial, with fixed line spacing checked in the rendered PDF. Bold terms
retain the darker shade derived from the existing title color. Package validation,
rendered-line checks, original-shape comparisons and Microsoft Open XML SDK
validation are recorded alongside the specification. Interactive playback in desktop
PowerPoint is not tested in this Linux environment.

## Reusable revision prompt

Revise Lecture 94 and add only the authorized content slides. Read the connected
repository's current default-branch rules first. Preserve the findings, original
figures, all embedded videos and audio, exact title and date, existing theme and one
final Key takeaways slide. Each content slide must contain three full teaching
paragraphs, with 5–7 complete sentences and at least five rendered lines in each.
Use clear wording that reads naturally aloud. Teach the cited sources directly,
without scaffolding narration or routine limitation endings in any paragraph.
Paragraph 3 must add a result, mechanism, behavioral relationship or substantive
comparison. Use only original published figures or permitted credited photographs;
never generate or redraw images. Build additions with the repository tools, preserve
media bytes during assembly, inspect every rendered slide, validate the final package
with Microsoft Open XML SDK, and provide a normal downloadable PPTX.
