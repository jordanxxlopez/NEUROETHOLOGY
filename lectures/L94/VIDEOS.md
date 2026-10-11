# Lecture 94 embedded video locations

Open the PPTX in PowerPoint Slide Show and click the video poster labeled “Click to play.” The recordings are embedded in the file; internet access is not required to play them. A static PDF or browser preview cannot play these recordings.

| Slide | Original recording | Duration | Audio stream |
|---|---|---:|---|
| 2 | Winship et al. (2023), article-provided video: Winship-etal-EVE_Supplemental Video [784572439].mp4. Cursor control. | 263.7 s | Yes |
| 3 | Stowers et al. (2017), Supplementary Video 7. Zebrafish responses to real and virtual posts. | 48.5 s | No, original is silent |
| 8 | Rouse et al. (2016), article-provided video: Video1.MP4. Sea-lion rhythmic responding. | 114.8 s | Yes |
| 12 | Portugues & Engert (2011), Movie S1. Tail movements and closed-loop gratings. | 9.8 s | No, original is silent |
| 14 | Stowers et al. (2017), Supplementary Video 13. Zebrafish portals and virtual swarms. | 359.0 s | No, original is silent |
| 20 | Zebunke et al. (2018), Supplementary Video 3. Switching from waiting to the immediate reward. | 14.6 s | No, original is silent |
| 22 | Calapai et al. (2017), ESM 2. Rhesus macaque using a cognitive-testing interface. | 120.0 s | Yes |
| 26 | Zebunke et al. (2018), Supplementary Video 1. Waiting for the delayed reward. | 22.2 s | No, original is silent |
| 35 | Joly et al. (2014), Movie S1. Mouse-lemur touchscreen discrimination. | 59.0 s | No, original is silent |
| 42 | Zebunke et al. (2018), Supplementary Video 2. Choosing the immediate reward. | 6.8 s | No, original is silent |

Ten distinct original recordings are embedded. The instructor authorized relevant comparative experiments while retaining sea lions as the lecture’s focus. All 44 original content-slide titles and body paragraphs are retained; added notes explicitly distinguish the comparative preparations from sea-lion evidence. There are two sea-lion recordings (EVE apparatus/acquisition and trained rhythmic responding), two comparative primate interfaces, three original reward-choice conditions in pigs, and three zebrafish visual-feedback/interface recordings. No recording was duplicated or divided to reach the count.

The original EVE recording supplied by the instructor is 263.68 s and contains AAC audio. It is retained byte-for-byte in the instructor’s compressed compatible form. The mouse-lemur WMV was converted to H.264 MP4 for compatibility, preserving the complete recording and its original silence. Interactive Microsoft PowerPoint playback could not be tested in this Linux environment; each clip decoded fully and the saved PPTX media, relationships and timing entries were verified.

## Instructor-requested EVE excerpts

The complete original ten recordings above remain embedded and unchanged. Seven additional, slide-specific excerpts from only the instructor-supplied EVE recording are embedded. There are 17 playable videos, drawn from ten original recordings; these excerpts are not additional distinct studies. This addition follows the instructor’s explicit request to extract relevant segments and retain all existing recordings.

| Slide | Source interval | Topic | Clip length |
|---|---|---|---:|
| 9 | 0:00–0:13 | (2023), EVE excerpt 0:00–0:13. Brief button contact. | 13.01 s |
| 10 | 0:15–0:30 | (2023), EVE excerpt 0:15–0:30. Restricted directional movement. | 15.02 s |
| 11 | 0:45–1:05 | (2023), EVE excerpt 0:45–1:05. Sustained directional contact. | 20.02 s |
| 12 | 1:14–1:35 | (2023), EVE excerpt 1:14–1:35. Stopping at interior targets. | 21.02 s |
| 13 | 2:00–2:25 | (2023), EVE excerpt 2:00–2:25. Switching directions. | 25.02 s |
| 14 | 2:40–3:00 | (2023), EVE excerpt 2:40–3:00. Precise target placement. | 20.02 s |
| 15 | 3:20–3:40 | (2023), EVE excerpt 3:20–3:40. Phase 6 with feeder. | 20.02 s |

The newly uploaded full-size original exceeds the 32 MiB attachment transfer limit. Excerpts therefore use the instructor’s previously supplied complete compressed copy of this same recording (263.68 s, all six phases). Only temporal trimming and compatible H.264 encoding were applied. The full scene is retained so the animal, directional buttons, screen, trainer and feeder context remain visible. Original AAC audio packets are retained; no narration, music or sound effects were added. Audio-stream presence does not guarantee audible sound throughout an excerpt. Source intervals and hashes are recorded in `media_sources.json`.

Original movie positions, captions and all original lecture text remain unchanged. Only article-figure placement/size on slides 9–15 was adjusted to accommodate the new clips. On slides 12 and 14, the new EVE excerpt is above the existing comparative recording, alongside the article figure.

Rebuild: run `tools/build_lecture.py lectures/L94/lecture.json`, then `lectures/L94/embed_media.py`, then `lectures/L94/add_eve_excerpts.py`. The checked-in excerpts can be regenerated with `lectures/L94/extract_eve_excerpts.py`. Use the repository Python environment. Do not apply the embedding scripts twice to an already embedded deck.

## Additional instructor-uploaded excerpts

The expanded deliverable is `deliverables/Neuroethology_Lecture94_FA2026.pptx`, with 25 embedded videos. All 17 earlier videos remain byte-for-byte unchanged. The older PPTX one directory above is the preserved 17-video baseline. The expanded PPTX is also stored as two lossless parts to meet GitHub’s per-file limit; see `deliverables/README.md` for verified assembly.

| Slide | Uploaded source | Exact source interval | Excerpt |
|---|---|---|---|
| 4 | Navy_Sea_Lions_HD.mp4 | 6–18 s | Controller contact. |
| 6 | Meet_EVE_HD (1).mp4 | 84–101 s | Response and trainer reward. |
| 21 | Meet_EVE_HD (1).mp4 | 53–59 s | Maze gameplay. |
| 22 | Meet_EVE_HD (1).mp4 | 70–84 s | Sample and choice display. |
| 23 | Examples_of_Defined_Strategies_HD (1).mp4 | 11–14.5 s | (2023), Video S1, 11–14.5 s. Staircase strategy. |
| 23 | Examples_of_Defined_Strategies_HD (1).mp4 | 20.5–25.5 s | (2023), Video S1, 20.5–25.5 s. Targeting strategy. |
| 24 | Examples_of_Defined_Strategies_HD (1).mp4 | 26.5–31.5 s | (2023), Video S1, 26.5–31.5 s. Wall surfing strategy. |
| 25 | Examples_of_Defined_Strategies_HD (1).mp4 | 6–10.5 s | (2023), Video S1, 6–10.5 s. Diagonal strategy. |

The uploaded Roberts paper explicitly identifies Video S1 as “Examples of Defined Strategies”; its source title is verified. `Meet_EVE_HD (1).mp4` and `Navy_Sea_Lions_HD.mp4` are instructor-authorized contextual recordings, and their publication linkage/producer was not independently verified. They are credited by exact uploaded filenames, not presented as independently verified article supplements. Their clips provide visible apparatus/task/reward context, while the cited primary studies support scientific claims. The beginning of Meet EVE concerning dolphins and general naval work was excluded.

New excerpts preserve original scene orientation, normal speed, source labels and audio. Only temporal selection, resolution reduction to 854 × 480, and H.264/AAC compatibility encoding were applied. No added drawings, subtitles, music or generated frames. All eight new MP4 files decoded fully. Open the expanded PPTX in PowerPoint Slide Show and click the recording poster. Static exports cannot play videos; interactive Microsoft PowerPoint playback remains untested in this Linux environment.

## Single-file browser download

[Download the unchanged expanded PPTX](https://media.githubusercontent.com/media/jordanxxlopez/NEUROETHOLOGY/aa70cd9a4f5d25ea50cecb9285e6aa6a913022be/lectures/L94/Neuroethology_Lecture94_FA2026_Download.pptx). The complete file is 119,072,985 bytes and contains all 25 embedded videos. No additional video compression, resolution reduction or content change was applied. This normal browser download avoids the connected-computer file viewer and its 40 MB preview limit. After download, embedded videos can play offline in PowerPoint. The GitHub LFS download was verified against the existing expanded PPTX SHA-256.
