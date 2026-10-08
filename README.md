# NEUR 411 Neuroethology — Fall 2026 lecture builder

Builds lecture PowerPoints in the approved Lecture 8–10 format: title slide + 44 content slides + key takeaways (46 total), research-based, exact schedule titles, new color theme each lecture.

## Use with an AI coding agent

- **Codex:** open this folder and ask, e.g., "make lecture 13". Codex reads `AGENTS.md`.
- **Claude Code:** same request. Claude reads `CLAUDE.md` and the skill in `.claude/skills/neuroethology-lecture/`.

## Use by hand

```bash
pip install -r requirements.txt
cp -r lectures/_template lectures/L13          # then fill lectures/L13/lecture.json
python tools/build_lecture.py lectures/L13/lecture.json
python tools/check_lecture.py lectures/L13/Neuroethology_Lecture13_FA2026.pptx --lecture 13
```

Also install poppler (`pdftoppm`) and LibreOffice (`soffice`) for figure cropping and slide previews.

## Prompt

`prompts/make_lecture.md` has a copy-paste request for Claude Code or Codex. Figures must come only from published articles; the builder rejects anything else.
