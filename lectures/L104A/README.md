# Lecture 104A

**Pain across species: nociception, neural pathways, behavioral responses, evolution of pain processing, social transmission of pain sensitivity, social buffering of pain, and experimental evidence for empathy-like behavior.**

Date TBD. Forty-six slides, Arial, palladium / blue mist. The scoped instructor rules in course/demonstration_104_rules.md apply only to 104A–C.

The PPTX contains 20 embedded original article recordings and 35 additional credited source animal/anatomical images. All 44 content slides have images; 40 have published research figures. The video list includes 17 experimental recordings and three original Carrillo Figure360 explanations of the paper's findings. These are expressly identified rather than labeled as experimental trials.

| Slide | Original recording |
| --- | --- |
| 3 | Arenas, video 1: planarian thermal avoidance |
| 4 | Arenas, video 2: planarian chemical avoidance |
| 6 | Khuong, Movie S1: adult thermal escape |
| 7 | Khuong, Movie S2: injury-associated allodynia |
| 10 | Oikawa, Video 1: Goro control |
| 11 | Oikawa, Video 2: CCKLR-17D1 mutant |
| 12 | Oikawa, Videos 3–4: control and cell-targeted RNAi |
| 13 | Oikawa, Videos 5–6: control and CCKLR-17D3 mutant |
| 15 | Florman and Alkema, S3 Video: wild-type touch response |
| 16 | Florman and Alkema, S4 Video: altered escape after overexpression |
| 17 | Florman and Alkema, S1–S2 Videos: two overexpression strategies |
| 30 | Carrillo, Video S1: experimental conditions |
| 31–33 | Carrillo, Figure360 presentations of Figures 2, 3, and 4 |
| 42 | Ben-Ami Bartal, Movie S1: trapped-cagemate exploration |
| 43 | Ben-Ami Bartal, Movie S2: release sequence |

Native proportions, original timing, audio presence, and scientific labels are retained. Compatibility encoding uses H264/AAC and proportional resizing at most 1280 px wide. Recordings are complete, not speed-altered. A native full-screen playback preference is set. Posters are source frames; metadata records their time. Static figures remain distinct from movie objects. A static PDF cannot play videos. Google Slides may require reinserting the supplied MP4 files through Drive after import.

Source figures are original paper crops or intact published article image files. The 2025 corrected bee graph is used. No generated diagrams, illustrations, reconstructed graphs, or recolored figures are included. See crops.json, original_figure_files.json, reference_verification.json, media_sources.json, and delivery_verification.json for the audit trail. Title-image uniqueness was checked against the previous local lecture specs.

Rebuild from the repository root:

```bash
python lectures/L104A/write_spec.py
python tools/build_lecture.py lectures/L104A/lecture.json
python lectures/L104A/embed_videos.py
python tools/check_lecture.py lectures/L104A/Neuroethology_Lecture104A_FA2026.pptx --lecture 104A
python lectures/L104A/verify_delivery.py
```

A fresh build is required before embedding to avoid duplicate media. Native desktop GUI playback and Google Slides import remain untested. The source-video preparation audit retains original hashes and compatibility conversion details.
