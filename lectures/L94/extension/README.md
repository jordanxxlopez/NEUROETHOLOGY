# Lecture 94 extension

Adds 24 research-based content slides and one final Key takeaways, without rewriting the existing 46 slides. The exact original title/date/theme are preserved.

Rebuild from the repository root with the installed presentation dependencies:

```sh
mkdir -p /workspace/l94-expansion
python lectures/L94/extension/write_extension.py
python tools/build_lecture.py lectures/L94/extension/extension.json /workspace/l94-expansion/Extension_Base.pptx
python lectures/L94/extension/append_extension.py
python tools/check_lecture.py lectures/L94/deliverables/Neuroethology_Lecture94_FA2026_Expanded71_Compatible.pptx --lecture 94 --content-slides 69
```

The preserved Rio-revised master must exist in `lectures/L94/deliverables/`. It can be rebuilt with the previous revision scripts or obtained from the pinned download in that directory's README. The earlier original source videos and all four new uploaded source videos are required. `media_manifest.json` verifies sources, dimensions, durations and SHA-256. `package_validation.json` records the byte-level preservation check.

Scientific source metadata was verified using the supplied PDFs and Crossref. `verified_references.json` is the reusable citation input. `crops.json` records PDF pages, crop bounds and source DOI links. Source PDFs are locally stored in the ignored papers directory. The duplicate chapter-17 attachment was used once.

The LED training movie is on 66 and baseline movies on 67; the movie captions retain their original filenames. Both baseline configurations are familiar, while the text also teaches novel-configuration tests. Luca's exact article provenance is unverified and labeled accordingly.

The append operation reuses byte-identical existing master, layout and theme parts. It rejects multiple notes-master relationships and duplicated layout IDs. This prevents the package error found in the previous 71-slide delivery. Microsoft Open XML SDK validation is recorded in `openxml_validation.json`; all 71 slide renders were compared pixel-for-pixel.

## One final summary revision

After rebuilding the compatible 71-slide master, run `python lectures/L94/extension/make_single_summary.py` to remove the earlier Key takeaways slide, renumber the remaining footers and consolidate duplicate identical media. Output: `Neuroethology_Lecture94_FA2026_70slides_SingleSummary.pptx`, 70 slides, one summary, 38 movie placements. No media encoding or resolution change occurs. The instructor explicitly accepted roughly 457 MB to preserve all embedded videos unchanged. Checks are recorded in `single_summary_validation.json` and `single_summary_download_validation.json`.
