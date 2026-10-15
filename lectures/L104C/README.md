# Lecture 104C: Animals on drugs

The instructor-authorized expansion contains **51 slides**: title, 49 content slides, and Key takeaways. Slides 46–50 add ΔFosB, emphasizing rodent experiments and a limited human postmortem comparison. The exact schedule title and Date TBD are retained.

The comparative material spans 13 nonhuman species: California two-spot octopus, honeybee, bumblebee, Argentine ant, Oriental hornet, green tree frog, C. elegans, fruit fly, zebrafish, prairie vole, cynomolgus macaque, mouse and rat. Primary-source figures appear on all 49 content slides. Thirty additional credited animal photographs accompany the evidence; the title has a separately credited unique octopus photograph.

**20 original research videos are embedded natively**, on slides 12–15, 21–26, 28–29, 34–37 and 43–45. Slide 24 has two recordings. Fullscreen playback is enabled where supported. Every movie retains its proportions. Figures, photographs and native movies remain separate objects. Full source metadata and credits are in speaker notes, `media_sources.json` and `additional_image_placements.json`.

Build with the repository Python environment:

```bash
python lectures/L104C/write_spec.py
python tools/build_lecture.py lectures/L104C/lecture.json
python lectures/L104C/embed_videos.py
python tools/check_lecture.py lectures/L104C/Neuroethology_Lecture104C_FA2026.pptx --lecture 104C --content-slides 49
python lectures/L104C/verify_delivery.py
```

`teaching.md` contains the original comparative teaching text; `deltafosb_slides.json` contains the five additional slides. `crops.json` and `figure_sources.json` record original PDF crops. The additional honeybee anatomy panel is a previously verified content-slide crop from Geng et al. (2022), DOI 10.1038/s42003-022-03075-8. Source PDFs and original archives remain local. Presentation photo copies preserve the complete image and proportions, downsampled for their small slide placements; original files and source hashes remain available.

`delivery_verification.json` checks native media bytes and proportions, complete video decoding, slide count, font, teaching text and credits. `visual_qa.json` records PDF layout checks. The PDF is a **static preview**; videos play from the PPTX. Desktop PowerPoint GUI playback has not been tested. Google Slides import has not been tested and may require separate Drive video insertion.
