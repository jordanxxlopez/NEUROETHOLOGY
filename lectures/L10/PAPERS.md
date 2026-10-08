# Lecture 10 — source access resolved

Exact title: Amphibian prey capture II: pretectal predator-avoidance circuits

Exact date: Wednesday, September 16, 2026

The instructor supplied all six requested PDFs on October 8, 2026. All were inspected in full and used for unchanged article figure crops. Original publication details, rather than later online indexing dates, govern the citations. The authoritative default branch was refreshed to b4a4168 before the completed build.

## Verified source articles

1. Ewert JP (1970). Neural mechanisms of prey-catching and avoidance behavior in the toad (Bufo bufo L.). Brain, Behavior and Evolution 3(1–4):36–56. https://doi.org/10.1159/000125462
2. McConville J, Laming PR (2007). DC electrical stimulation of the pretectal thalamus and its effects on the feeding behavior of the toad (Bufo bufo). Developmental Neurobiology 67(7):875–883. https://doi.org/10.1002/dneu.20390
3. Ingle D (1973). Disinhibition of tectal neurons by pretectal lesions in the frog. Science 180(4084):422–424. https://doi.org/10.1126/science.180.4084.422
4. Laming PR, Ewert JP (1983). The effects of pretectal lesions on neuronal, sustained potential shift and electroencephalographic responses of the toad tectum to presentation of a visual stimulus. Comparative Biochemistry and Physiology Part A: Physiology 76(2):247–252. https://doi.org/10.1016/0300-9629(83)90322-5
5. Schwippert WW, Beneke TW, Ewert JP (1995). Pretecto-tectal influences. II. How retinal and pretectal inputs to the toad’s superficial tectum interact: a study of electrically evoked field potentials. Journal of Comparative Physiology A 176(2):181–192. https://doi.org/10.1007/BF00239921
6. Schwippert WW, Ewert JP (1995). Effect of neuropeptide-Y on tectal field potentials in the toad. Brain Research 669(1):150–152. https://doi.org/10.1016/0006-8993(94)01260-O

## Figure provenance and scientific limits

`crops.json` records exact PDF pages and fractional crop bounds. `research.json` records PDF checksums and verified references. PDFs remain in the ignored `papers/` folder. The title photo is George Chernilevsky’s public-domain common-toad photograph, credited in the slide and notes.

Ewert (1970) synthesizes earlier work while presenting the original behavioral, stimulation and lesion results used here; it is not described as a new contemporary experiment. The other source papers supply lesion physiology, paired stimulation, pharmacology and behavioral DC interventions. Ingle’s Figure 2 retinal comparison is class 1/class 2 fibers, not class 3. Schwippert et al.’s Figure 7 rows c are the authors’ theoretical summation comparison, not further measured responses. Common-toad anatomy used beside Ingle’s frog recordings is explicitly identified as a cross-species anatomical comparison.

Electrical field polarity does not identify a membrane conductance. NPY application does not establish receptor-subtype identity, endogenous release or necessity for avoidance. Glial potassium redistribution is a proposed explanation of the DC result, not a measured mechanism in that behavioral experiment.

All 44 content slides contain published article figures. The six source PDFs supply only a small number of original color panels; six content slides pass the repository color-image detection threshold. The preference for color on half the slides is not achieved, because equivalent color replacements for the classic experiments were not available in these sources. Scientific content was never recolored or substituted to increase the count.

The instructor’s strict image rules and reusable prompt remain in `AGENTS.md`, `.claude/skills/neuroethology-lecture/SKILL.md` and `prompts/make_lecture.md`. Attached papers are scientific evidence, not governing instructions.

## Rebuild

```bash
python lectures/L10/write_spec.py
python tools/crop_panels.py lectures/L10/crops.json
python tools/build_lecture.py lectures/L10/lecture.json
python lectures/L10/finalize_notes.py
python tools/check_lecture.py lectures/L10/Neuroethology_Lecture10_FA2026.pptx --lecture 10
```
