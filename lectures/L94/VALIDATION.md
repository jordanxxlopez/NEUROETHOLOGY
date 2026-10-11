# Expanded Lecture 94 validation

- 46 slides; 44 image slides, all 44 with original primary article figures, 34 with source color. Repository checker: zero failures and warnings.
- 25 embedded MP4 files with hashes matching the source manifest: ten complete original recordings, seven earlier EVE excerpts and eight new excerpts. All original embedded media bytes, including all original figure/poster image bytes and all 17 prior MP4 files, match the preserved baseline exactly.
- Original 17 movie shape XML/positions and all original title/body/footer/video-credit text retained. Lecture JSON and theme unchanged. Only article figure/caption geometry on new-video slides adjusted to fit additions.
- All eight new excerpts decoded fully with ffmpeg. Source audio remains present; no audio added or intentionally removed. Full scene and display orientation preserved, resized to compatible 854 × 480 H.264/AAC with normal playback speed.
- All three complete uploads inspected via timestamped source contact sheets. Source strategy transition boundaries additionally inspected at 0.5-second intervals to exclude preceding strategy footage. New clips inspected at beginning, middle and end.
- Roberts Video S1 title verified directly from the uploaded primary PDF (DOI 10.3390/jzbg4010021). Other two uploaded sources explicitly credited as instructor-supplied context with unverified publication/producer provenance, not falsely labeled academic supplements.
- All 46 slides rendered with LibreOffice and visually reviewed. No visible text/footer/credit collisions; existing movies retain their original placements. Source figure fallbacks remain available.
- Embedded video/media relationships and timing entries verified. Interactive Microsoft PowerPoint playback remains untested in Linux. PDF/browser exports are static.
- Expanded PPTX bytes preserved in two parts because the complete file exceeds GitHub’s 100 MiB limit. Assembly verifies every part hash and the complete output hash; no compression or media edits occur during assembly.

Expanded PPTX size: 119,072,985 bytes.
Expanded PPTX SHA-256: 3a54cbe2736c0e1f30077f82a9da0058fb7f7278729048b57ed97c2d1cf531de

## Latest 32-video revision

- 46 slides; all 44 content slides retain their primary article figures. Repository checker: 0 failures and 0 warnings.
- Seven additional original article recordings on slides 28, 29, 30, 31, 33, 37 and 44; the 25 existing video shape XML/positions and all original media bytes are preserved. All earlier title/body/footer/credit text is unchanged.
- New source hashes match the extracted PPTX media hashes and downloaded original hashes exactly. Three native MPG/MOV recordings were embedded using their correct video MIME type without conversion. No trimming, spatial cropping, compression or resolution reduction was applied to these seven additions.
- All seven recordings decoded to completion with exit status 0. The slide 28 original emits recoverable H.264 slice warnings; the slide 44 original emits duplicate timestamp warnings in the default null-output check. Other five sources produce no decoder messages. These original artifacts were not silently repaired. Interactive Microsoft PowerPoint playback and installation codec support remain untested.
- All 46 slides rendered in LibreOffice and visually reviewed on six contact sheets; seven changed slides were also rendered at full-size resolution. Original article figures, video posters, captions and footers remain visible with no collisions.
- Each new recording’s exact article identifier, source URL, complete citation, license and appropriate comparative task distinction are included in notes and metadata. No movie is misrepresented as footage of an older sea-lion experiment.

Latest PPTX size: 335676221 bytes.
Latest SHA-256: e0dd2ef75aca38871c91ec022e63dc52ad52977d1fec1826bcea60bc52b015e8

The pinned single-file browser download returned HTTP 200 and its complete 335,676,221-byte response matched the final PPTX SHA-256.

## Paragraph 3 revision

- Only paragraph 3 on slides 3, 5, 10, 14, 15, 16, 18, 21, 23, 27, 29, 30, 33, 38, 39, 40, 41, 42, 43 and 45 was replaced with affirmative source-supported teaching content. Matching transcript passages were updated; other speaker notes are unchanged.
- The PPTX package differs only in those 20 slide XML parts and 20 corresponding notes XML parts. Structural XML is unchanged when the replaced text nodes are restored. All other parts, including media, movie relationships, timing, themes, layout and every image/video byte, are identical. Paragraphs 1 and 2 and all other slide text remain unchanged.
- Repository checker: 46 slides, 44 primary-figure content slides, 0 failures and 0 warnings. All 46 rendered slides visually reviewed; slide 23 text shortened to preserve spacing above the existing footer.
- Complete size: 335675627 bytes. SHA-256: f9ec3ebde39368d6c29ae55ad1f33f7babfc0e4831b96de4b5f7d786abaa0f5f.
- Reproducible patch: `python lectures/L94/revise_paragraph3.py` against the preserved pre-edit 32-video deck. Exact old/new paragraphs are saved in `paragraph3_revision_audit.json`.

Revised single-file browser download returned HTTP 200; its full response matched the final PPTX SHA-256.

## Rio recording replacement/addition

- 46 slides and 33 movie placements. Rio appears exactly twice, on slides 32 and 35. The Joly media hash is absent from the saved PPTX; the uploaded Rio hash is present unchanged.
- Every original title, body paragraph, citation, slide number and takeaway is unchanged, including the corrected paragraph 3 passages. All other movie XML/geometry and media bytes are unchanged. Only slide 32 figure/caption geometry was adjusted to accommodate its video; slide 35 video geometry was changed to the Rio source aspect ratio.
- The Rio upload fully decoded with ffmpeg, exit 0 and no errors. All 41 one-second source frames were inspected. The original title card and publisher supplementary description verified its identity, credit and task.
- Correct citation and exact Supplementary Video 17.2 identifier are included in the notes and captions. Slide 35 distinguishes identity matching from its reversal-learning evidence.
- Native resolution, original audio and original video bytes preserved, without any editing or encoding. Interactive Microsoft PowerPoint playback remains untested.
- Repository checker and rendered-slide visual review completed for the revised deck. Final size 337375852 bytes; SHA-256 14c54f80b92f4adf2f6e17f1299d86cf691a734ef9da8d7aaf58110739cf8b94.

Latest Rio-revised direct browser download returned HTTP 200, and its complete 337375852-byte response matched the deck SHA-256.

## Latest 71-slide expansion

The current deck is `deliverables/Neuroethology_Lecture94_FA2026_Expanded71.pptx`: 71 slides, with 25 appended slides (24 content slides plus a final Key takeaways). Original slides 1–46 remain in their original positions, including their Key takeaways slide. All original slide XML, notes, relationships, figures, posters and video bytes are identical to the Rio-revised master; only package indexes and the slide-count property change.

The deck contains 38 embedded movie placements. The five supplied recordings are added on slides 47 (Rio), 57 (Luca), 66 (Moe training), and 67 (both LED baseline trials). Rio appears exactly three times in the whole deck: 32, 35 and 47. Native uploaded media bytes, resolution, timing and audio are preserved without re-encoding.

- Package preservation: 313 original parts unchanged byte-for-byte.
- All five supplied source hashes match embedded video parts. All four newly accessible MP4 files decode completely with ffmpeg. Rio was decoded and verified in its earlier revision.
- Repository checker: 71 slides, 68 image slides, 68 article-figure slides, 51 color image slides; 0 failures, 0 warnings.
- Source PDF figures cropped with the repository crop tool; all 24 new content slides include an original published figure. No images were generated, redrawn or recolored.
- The standalone donor has an additional title used only by the build tool; that donor title is excluded from the append operation. Original title and theme are unchanged.
- Interactive Microsoft PowerPoint playback remains untested in Linux.
- Exact PPTX bytes: 459,026,231. SHA-256: `04f8c93d31a5ad0d4ea2b6ba6ac23cfac0fe06ece3978a1a3182b1993b8bd2a1`.

All 71 slides rendered in LibreOffice, and all 25 appended slides visually reviewed. The final two corrected figure crops were re-rendered and checked separately. There were no visible text, caption or footer collisions. The original 46 slide parts remain byte-identical, including slide notes and media.

Direct browser delivery verified: HTTP 200; full 459,026,231-byte PPTX SHA-256 matches the local expanded master. See `extension/download_validation.json`.

## PowerPoint compatibility correction

The first 71-slide delivery is superseded. Microsoft Open XML SDK 3.3.0 identified `Pkg_OnlyOnePartAllowed`: two notes-master relationships were present, while the presentation format permits one. Appending also duplicated slide-layout IDs. The correction shares the original, byte-identical master/layout/theme parts. No slide, note, image or movie content was edited or removed.

The corrected file is `deliverables/Neuroethology_Lecture94_FA2026_Expanded71_Compatible.pptx`. Microsoft Open XML validation for Office 2019 returns **zero errors**; repository checks return zero failures/warnings. All 71 slide renders match the earlier full deck pixel-for-pixel. All 38 video placements remain, and every slide XML, note text and media blob is byte-identical. All internal relationship targets resolve and layout IDs are unique. Native Mac PowerPoint opening remains untested in this Linux environment.

See `extension/openxml_validation.json`, `extension/compatibility_validation.json`, and `extension/ValidateOpenXml.cs`. SHA-256: `fb34c848d1a663416c8b8e8f23b9361ecf1feab0205e61f16a64b33fd0f1301c`; exact size 459,001,230 bytes.

[Download the corrected 71-slide PPTX](https://media.githubusercontent.com/media/jordanxxlopez/NEUROETHOLOGY/97bdec026ea1330f55ad9188dbf8727e2377ec7b/lectures/L94/Neuroethology_Lecture94_FA2026_Download.pptx). Verified HTTP 200 full response, 459,001,230 bytes, matching SHA-256. Opening in native Mac PowerPoint is untested; Microsoft Open XML structural validation, complete relationship checks, byte-preservation checks and all-slide render comparisons passed.
