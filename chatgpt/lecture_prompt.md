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
   diagrams, charts or any other image. Nearly every slide gets a figure (40+ of 44, 34+ from articles); the study animal on the title slide; an anatomy image wherever a slide discusses a specific structure; prefer colorful figures over grayscale ones (color only as published, never recolored); at most 10 credited web images, only where needed.
4. Write lectures/L[N]/lecture.json with slide paragraphs, a teaching transcript for the speaker notes,
   citations and figures, then run: python tools/build_lecture.py lectures/L[N]/lecture.json
   and fix everything until it reports 0 failures.
5. For both new lectures and updates, check the cited articles and supplements for useful original videos.
   Follow AGENTS.md rule 11: only article-provided media or author/lab repositories explicitly linked
   or cited by the article; never YouTube. Embed when supported, preserve the recording, credit its
   identifier/filename, DOI and original URL, verify media/playback when possible, and retain a static
   fallback. If unavailable, tell me briefly, provide the original link/file where accessible and
   continue. Aim for 8–10 useful embedded original article recordings per lecture (10 preferred, 8 acceptable); explain any shortfall and never pad with repeated or unhelpful clips. No generated footage or changes to titles, slide counts or figure requirements.
6. Reread every slide and transcript against the writing rules (no framing, no "this shows", no
   statistics clutter, natural teaching voice), then give me the .pptx and the updated themes.json.
```


- **First-slide images must be unique.** Every image on slide 1 must show the animal studied in that lecture. Use an original experimental image or a credited real photograph chosen for appearance, subject to the existing source and license rules. Never reuse an image already used anywhere in an earlier lecture; another crop, resize, or encoding of the same image does not make it new. Before choosing it, compare the candidate with images in previous lecture decks and record its source and the uniqueness check. This no-repeat requirement applies only to slide 1; content-slide figures may recur when scientifically appropriate.

## Scoped demonstration exception: Lectures 104A–C

For 104A, 104B, and 104C only, follow `course/demonstration_104_rules.md` in addition to these rules. It takes precedence for access failures, 20–30 embedded research-linked videos, no news/Shorts/TikTok, and approximately 25–35 additional credited subject-related images (animals, neurons, brain regions, or other slide-related structures). Continue with accessible alternatives except when a discussed article has a blocked relevant recording: request that original recording before final delivery. Retain 46 slides, primary research figures, teaching content, scientific provenance, and native video proportions. Other lectures are unaffected.


## Scoped demonstration exception: Lectures 105A–B

For 105A and 105B only, follow `course/demonstration_105_rules.md`. Each is a separate 50-slide PPTX (title + 48 content + Key takeaways), with 35–40 native embedded research-linked videos and approximately 25–35 additional credited subject-related images. Every content slide has a relevant image; retain at least 38 primary-figure content slides. Research-linked web/YouTube footage is allowed; news, Shorts and TikTok-style clips are excluded. Continue with accessible alternatives for ordinary source failures, but request the original recording when a selected article has a relevant blocked video before final delivery. Preserve the exact titles, scientific provenance, teaching requirements and native media proportions. Other lectures are unaffected.
