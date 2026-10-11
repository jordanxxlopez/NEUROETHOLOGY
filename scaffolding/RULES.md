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
