# Handoff: NEUR 411 lecture scaffolding

Read this first in a new session. Branch: `claude/festive-keller-lewmhk`. Do not open a PR unless asked. Do not commit or push unless asked (the user has asked for commits after each finished lecture). Do not put model names in commits, PRs or code.

Commit trailers used for every lecture commit:

```
Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Ed32PAQHh91bsZ3XG1vCPp
```

## Source file rule (set by the user)

For lecture N, use `drive_updated/Neuroethology_Lecture{N}_FA2026.pptx`, unless a `_V2`, `_V3` or `_NEW` file exists for that lecture. In that case use the suffixed file.

| Lectures | Source file |
|---|---|
| 1–7, 9–11, 13, 14 | `_V2` |
| 8, 12 | `_V3` |
| 15, 16, 17 | **Undecided.** Both `_NEW` and `_V2` exist, and their text differs. Ask the user which to use before building. |
| 18 | plain |
| 19 | `_V2` |
| 20–30 | plain |
| 31–39 | plain (done) |
| 40 | `_V2` (done, commit `24d8a71`) |

## Status

- Done and committed: 31, 32, 33, 34, 35, 36, 37, 38, 39, 40.
- Next: **29 and 30** (plain files). The user asked for these next, with the guidelines unchanged.
- Then: 1–14 (V2/V3), 15–17 (after the user decides), 18–28.
- Lectures 1–30 are the older backfill. They must be brought to the same rules as 31–40.

## How a lecture is built (the working pipeline)

1. Dump the source text per slide with python-pptx. Skip Fig./Photo/Credit captions when rewriting. Get the reference keys with `sd.reference_index(Presentation(path))` from `tools/scaffold_deck.py`.
2. Write `scaffolding/specs/body_L{N}.py`:
   `body = {slide: [para1, para2, para3], ...}` for every content slide 2..45. Slide 1 and the last slide are not rewritten.
3. Write `scaffolding/specs/L{N}.py`. It has `ins(after, title, paragraphs, citation, refs)` for 14 inserts after slides 3, 6, 9, … 42. Each insert gets notes built from its paragraphs (see L39.py). End with `spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}`.
4. If the lengthening sentences are kept separate, put them in `L{N}_extend.py` (body) and `L{N}_insert_extend.py` (inserts), and hook them in before `spec = ...`. Lectures 37 and 39 do this.
5. Build: `python3 scaffolding/build.py N drive_updated/<source file>`. It must exit 0 with no PROBLEM or WARNING lines.
6. Check: `python3 tools/check_paragraphs.py scaffolded/Neuroethology_Lecture{N}_FA2026_SCAFFOLDED.pptx`, `python3 scaffolding/render_check.py <same file>`, and `python3 scaffolding/specs/flagged_text.py N` (must print nothing).
7. Verify media: count `ppt/media` files and pictures in the source and the scaffolded deck. Media files must match. Pictures should equal source pictures plus the clones made for the inserts.
8. Commit only that lecture's files and push.

## Rules to keep (from scaffolding/RULES.md, plus what was learned)

- Exactly three body paragraphs per content slide, in one text box.
- Body paragraphs need 5–7 rendered lines. In practice this is about 52–62 words for body text. Build measurements at 14 pt show about 8–9 words per line, so 4-line paragraphs fail. Lectures 40's agent measured about 8 words per line and used 44–50 words, which passed.
- Insert paragraphs: 3 paragraphs totaling 110–200 words. About 55–65 words each.
- Notes for each insert: 150–420 words. The L39 builder derives them from the paragraphs (title sentence, then "Explanation n." lines, then a "Source." line).
- Total body text must fit the column. At 14 pt about 20 rendered lines total fit; if placement fails the build prints `WARNING: no column free of figures`, and the original text stays. Shorten the longest paragraph when this happens.
- Banned wording in body and inserts (checked by the build and check_paragraphs):
  - Limitations/caveats: "does not", "do not", "cannot", "not necessarily", "limited to", "remains unresolved", "without establishing", "not establish", "should not", "only (the|a|one|an)", "not proof".
  - Filler: "the comparison", "compared with/against", "read together", "read alongside", "are read", "is read", "separates", "keeps ... distinct", "is tested next", "next step", "next question(s)".
  - Narration: "lets", "let's", "this slide", "this figure", "I", "we", "our", em dashes.
  - Use "distinguishes", "measured against", "allows", "tied to", "kept separate" instead.
- Paragraph 3 teaches one new fact from the source. It is not a summary.
- Only facts from the source deck text may be used. Rewrite source sentences in new words.
- Keep figures, captions, photos, videos and the title/takeaway slides untouched.

## Shared tool change

`scaffolding/build.py` (commit `a52b4ea`) no longer counts `Photo:` and `Credit:` lines as left-over original paragraphs. This matches `tools/check_paragraphs.py`.

## Known warning

The build prints a `DeprecationWarning` for a positional `maxsplit` at `tools/scaffold_deck.py:474`. It was already there and does not affect the output. Not fixed.

## Useful files

- `scaffolding/specs/L39.py` and `body_L39.py`: the most recent complete pattern (inserts with derived notes, body text).
- `scaffolding/specs/L37.py` with `L37_extend.py` and `L37_insert_extend.py`: the lengthening-sentence pattern.
- `scaffolding/specs/L40.py` and `body_L40.py`: built by a subagent; the notes builder is in L40.py.
- `scaffolding/specs/map_built.py N built_slide ...`: maps a built slide number to its source key (`('body', n)` or `('insert', after)`).
- `scaffolding/specs/flagged_text.py N`: prints filler-flagged paragraphs.

## Starter prompt for the new chat

"Continue the NEUR 411 scaffolding work. Read `scaffolding/HANDOFF.md` first and follow it. Build Lectures 29 and 30 from their plain drive files, keeping the rules in that file. Commit and push each lecture when its checks pass."
