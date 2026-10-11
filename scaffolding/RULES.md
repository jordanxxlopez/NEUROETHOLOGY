# Lecture body-text rules (Lectures 21–40 and later)

These rules apply to the three body paragraphs of every content slide and to every scaffolded
("a") slide. They override any older habit of closing a paragraph with a caveat.

## Content
- Write exactly three developed paragraphs per slide, in one editable text box, separated by paragraph breaks.
- Each paragraph adds one distinct idea: the concept or task, the mechanism or result, and what the result means for the animal.
- Never include limitations, caveats, methodological disclaimers, or statements about what an experiment did not establish.
  Words and phrases such as "does not establish", "cannot", "remains unresolved", "limits", "not proof", "requires further
  evidence", "a limitation", "it does not", "unknown" are banned in the body text.
- Replace any removed limitation with the substantive scientific explanation of the result, scoped to what the study measured.
- No metacommentary: no advice to researchers, no instructions about how to interpret or evaluate a study, no commentary on
  the lecture or course.
- No first-person narration ("I", "we", "our", "let's"), and no talk about the slide itself ("this slide", "this figure", "the panel").
- Teach what the results show and why they matter, not a walkthrough of axes, panels or plotted values.
- Numbers only when they clarify an important finding. No standard deviations, p-values, test names or strings of values.

## Tense
- Simple present for concepts, established theories, mechanisms, and how experimental tasks work.
- Simple past only for specific historical events, researchers' completed actions, and findings from particular studies.
  Do not turn a study-specific finding into a universal claim.
- Never present continuous ("is looking", "are examining") and never simple future ("will", "is going to").

## Structure and bolding
- Use bold for key terms, mechanisms, task features, and central findings: short phrases, not whole sentences.
- Keep the existing title, layout, figures, citations, and structure; only the body text box changes.
- Aim for about 5–7 full lines per paragraph at the existing text box width and font size.
- No repetition across paragraphs and no filler.

## Enforcement
`tools/style_rules.py` (BODY_LIMITATION, BODY_FRAMING, BODY_TENSE) and `tools/check_lecture.py` report violations.

## Paragraph format (updated)
- Three paragraphs per slide body, all in one text box. Press Enter once between paragraphs; never leave an empty paragraph or blank line.
- Create the visual gap with Paragraph Spacing → After (`spcAft`, about 12 pt), not with extra Enter presses.
- Each paragraph fills about 5–7 lines at the existing text box width and font size. Measure lines, not sentences. Use
  complete sentences and let the sentence count vary naturally within that length.
- Revise the existing paragraphs too, preserving the findings, the figure references and the videos; only the wording changes.
- Limitations are banned in all three paragraphs. A caveat may appear only when it is absolutely necessary for the scientific
  claim, and then as one clause that states the finding, not as a closing sentence.

## Awkward phrasing when read aloud (review flags)
These are review flags, not automatic failures. Necessary scientific terms may be long without being awkward.
- Stacked modifiers: "reward-dependent cursor-target acquisition performance" → "how accurately the animal moved the cursor to earn a reward."
- Long noun strings: "auditory stimulus response selection mechanisms" → "how the animal selects a response to a sound."
- Repeated sounds or near-identical words that make a sentence easy to stumble over.
- Complicated sentence structure: several embedded clauses, unclear pronouns, or a long delay before the main verb.
`tools/style_rules.py` `tongue_twister_flags()` returns each suspicious phrase with the reason. A language review decides the revision.
Reading the revised paragraph aloud is the final check.

## Font size and paragraph spacing (updated)
- Body text is 14–15 pt. Choose the size from the space available on each slide, and use the same size for all three paragraphs on that slide.
- Apply Line and Paragraph Spacing → Space After to every paragraph in the body text box, including the last one.
- Separate paragraphs with paragraph spacing only. Never insert blank lines between paragraphs.

## Body layout (guideline, every content slide)

- Each content slide has exactly three body paragraphs, and nothing else in body text. No original paragraph may remain on the slide, in any box, column or position.
- The three paragraphs sit in one text box. Put them in the left column, where most figure-left slides keep their text. Use the right column only where the original slide's text sat there, and never place text over a figure or a caption.
- A stacked right-column layout is allowed only when the source layout already uses it. It must still contain exactly three paragraphs in total, and no paragraph may repeat across boxes.
- Before publishing, check the built slide: the count of body paragraphs is three, every body paragraph is new text, and no text overlaps a figure or caption (`scaffolding/build.py` reports these).
- `python tools/check_paragraphs.py` checks every scaffolded deck: each slide except the first and last must have exactly three body paragraphs. Figure captions, figure labels and photo credits do not count.
- Every body paragraph is 5-7 full rendered lines at the slide's font size. Count lines, not sentences. `tools/check_paragraphs.py` checks this together with the three-paragraph rule.
