# NEUR 411 Neuroethology — Fall 2026 lecture builder

Builds lecture PowerPoints in the approved Lecture 8–10 format: title slide + 44 content slides + key takeaways (46 total), research-based, exact schedule titles, new color theme each lecture.

## Use with an AI coding agent

- **ChatGPT:** see `chatgpt/SETUP.md` (Project instructions in `chatgpt/INSTRUCTIONS.md`, per-lecture message in `chatgpt/lecture_prompt.md`).

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

## Rules in short

- Images are never created: figures come from published articles (priority); a few credited web photos only where needed.
- Every sentence teaches source content: no roadmap, transition, figure-reading or takeaway framing; concepts over statistics.
- Speaker notes are a teaching transcript you can read aloud.
- Full rules: `AGENTS.md` (Codex) / `.claude/skills/neuroethology-lecture/SKILL.md` (Claude). Enforced by `tools/style_rules.py`.

## Prompt

`prompts/make_lecture.md` has the copy-paste request for Claude Code or Codex.
