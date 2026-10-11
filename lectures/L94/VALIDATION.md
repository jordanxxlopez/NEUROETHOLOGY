# Lecture 94 slide-specific EVE excerpt validation

- 46 slides; 44 image slides, all 44 with primary article figures, 34 with source color. Repository checker: zero failures and warnings.
- Seventeen embedded MP4s: ten existing complete original recordings plus seven instructor-authorized EVE excerpts on slides 9–15. Every embedded SHA-256 matches the credited input. Original ten MP4 hashes remain identical.
- All original movie shape XML and positions, original title/body/footer/recording-credit text XML, and original source figure image bytes remain unchanged. Only article-figure geometry/caption sizing on the seven affected slides was adjusted. The lecture spec and theme were not changed.
- Seven excerpts decoded fully with ffmpeg. Original 854 × 480 scene, 30000/1001 frame rate and normal playback speed retained; original AAC audio packets retained. Source interval, encoding and provenance recorded per excerpt.
- Full source inspected across 53 timestamped frames at five-second intervals; each selected excerpt inspected at start, midpoint and near end against its author-provided phase label and the primary paper. Six training phases and the separate feeder condition were identified. No generated graphics, recoloring, spatial crop or inserted audio.
- All 46 slides rendered with LibreOffice and visually reviewed across six contact sheets. Existing figures remain present, new credits/posters have no visible overlap with text or footers, and the existing comparative videos on slides 12 and 14 retain their original positions.
- Interactive Microsoft PowerPoint playback remains untested in this Linux environment. Embedded movie relationships and timing entries were verified. Static PDF/browser previews cannot play the recordings.
- Full original EVE remains embedded on slide 2. Excerpts were added for teaching context under explicit instructor authorization, not to pad the distinct-source recording count.

PPTX size: 103,321,774 bytes, below GitHub’s 100 MiB file limit.
PPTX SHA-256: f5fb040bb99b08fc7d380a326ddba292d82099e205184be3969fb099c290d1c7
