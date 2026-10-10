# Using the lecture builder in ChatGPT

ChatGPT does not read `AGENTS.md` or the Claude skill on its own. Set it up once as a **ChatGPT Project** (or a custom GPT); after that each lecture is one short message.

## One-time setup (ChatGPT Project — recommended)

1. In ChatGPT, click **Projects → New project**, name it "NEUR 411 Lectures".
2. Open the project's **Instructions** (or "Customize project") and paste the whole of `chatgpt/INSTRUCTIONS.md`.
3. Add **project files**: upload `NEUR411-lecture-builder.zip` (the whole builder). Optionally also upload `AGENTS.md` and `course/schedule.json` on their own so ChatGPT can read them without unzipping.
4. Use a model that can search the web and run Python (the default GPT models in a paid plan can).

### Alternative: a custom GPT
**Explore GPTs → Create → Configure**: paste `chatgpt/INSTRUCTIONS.md` into **Instructions**, upload the zip under **Knowledge**, and turn on **Web Search** and **Code Interpreter & Data Analysis**.

## Each lecture

Start a chat inside the project and paste `chatgpt/lecture_prompt.md` with the lecture number filled in. When ChatGPT lists papers it cannot open, download those PDFs (USC library access works in your own browser) and upload them in the same chat.

## Things to know

- **Upload the papers.** ChatGPT's Python tool has no internet, so it cannot download PDFs; upload the PDFs it asks for. Web search still finds the papers and their DOIs.
- **Themes and finished lectures** live in the uploaded zip. After each lecture, ChatGPT gives you the deck and the updated `course/themes.json`; replace that file in the project (or re-upload a fresh zip from GitHub) so the next lecture does not reuse a color theme.
- **Same rules everywhere.** The builder inside the zip enforces the image, writing and statistics rules in ChatGPT exactly as it does in Claude and Codex.
- **Visual check.** ChatGPT usually cannot render slides to images; open the .pptx yourself and look at each slide.

## Article-provided videos

For new lectures and revisions, check cited papers and supplementary materials for useful original recordings. Follow AGENTS.md rule 11: no YouTube or unrelated web videos. Embed useful article-provided recordings when supported, credit the study and original media URL, and verify the saved media. A static hosted preview is separate from a PPTX with embedded video. If original media cannot be obtained or embedded, report this briefly and continue with published figures; provide the original article link or recording when accessible.
