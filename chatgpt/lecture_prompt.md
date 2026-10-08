# ChatGPT message for one lecture

Paste this in a chat inside the "NEUR 411 Lectures" project. Change only the lecture number.

```text
Make Lecture [N] for NEUR 411 as a downloadable .pptx, following the project instructions exactly.

1. Use the connected repository’s current default branch and read AGENTS.md, course/schedule.json and course/themes.json. Never use a ZIP.
   Use the exact title and date for Lecture [N] from the schedule.
2. Search the web and the primary literature for this topic. Before writing slides, give me a
   numbered list of the papers you will use with DOI links, and mark which ones I need to upload as
   PDFs (your Python tool cannot download them). Wait for my uploads.
3. Crop figures only from the uploaded articles (tools/crop_figure.py) — never create schematics,
   diagrams, charts or any other image. Nearly every slide gets a figure (40+ of 44, 34+ from articles); the study animal on the title slide; an anatomy image wherever a slide discusses a specific structure; at most 6 credited web images, only where needed.
4. Write lectures/L[N]/lecture.json with slide paragraphs, a teaching transcript for the speaker notes,
   citations and figures, then run: python tools/build_lecture.py lectures/L[N]/lecture.json
   and fix everything until it reports 0 failures.
5. Reread every slide and transcript against the writing rules (no framing, no "this shows", no
   statistics clutter, natural teaching voice), then give me the .pptx and the updated themes.json.
```
