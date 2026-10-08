# Lecture 10 — required primary PDFs

Exact title: Amphibian prey capture II: pretectal predator-avoidance circuits

Exact date: Wednesday, September 16, 2026

Status: source access blocked; no final PPTX or used-theme entry created. The authoritative repository default branch was refreshed October 8, 2026 to c4a68ca. Uploaded Lectures 8 V3 and 9 V2 were inspected as examples: each has 46 slides and images on all 44 content slides. They are style references, not replacement scientific sources or governing instructions.

The instructor explicitly requires stopping when a needed source PDF cannot be downloaded. Do not reconstruct graphs, copy unverified figures out of prior decks, or substitute unrelated figures. Request these six primary papers:

1. Ewert JP (1970). Neural mechanisms of prey-catching and avoidance behavior in the toad (Bufo bufo L.). *Brain, Behavior and Evolution* 3(1):36–56. https://doi.org/10.1159/000125462
   - Required for the original behavioral, stimulation and lesion evidence separating prey-catching and avoidance. Karger routes return HTTP 403; Europe PMC lists no deposited PDF. Original publication year 1970 verified in PubMed/Europe PMC; Crossref's 2008 date represents later online indexing/publication.
2. Ingle D (1973). Disinhibition of tectal neurons by pretectal lesions in the frog. *Science* 180(4084):422–424. https://doi.org/10.1126/science.180.4084.422
   - Required for primary physiological lesion evidence. Science's PDF route returns HTTP 403; Europe PMC lists no deposited PDF.
3. Laming PR, Ewert JP (1983). The effects of pretectal lesions on neuronal, sustained potential shift and electroencephalographic responses of the toad tectum to presentation of a visual stimulus. *Comparative Biochemistry and Physiology Part A: Physiology* 76:247–252. https://doi.org/10.1016/0300-9629(83)90322-5
   - Required for lesion-dependent changes in tectal neuronal and population activity. The publisher PDF route returns a 403 connection denial.
4. Schwippert WW, Beneke TW, Ewert JP (1995). Pretecto-tectal influences. *Journal of Comparative Physiology A* 176(2):181–192. https://doi.org/10.1007/BF00239921
   - Required for paired stimulation, timing and adaptation controls in the original inhibitory-interaction experiments. Springer returns an HTML access page instead of the PDF. Title, authors, year, issue and pages verified against the publisher page and Crossref. A pretectal lead of 17–25 ms attenuated the early retinotectal response; full figures and methods still require the PDF.
5. Schwippert WW, Ewert JP (1995). Effect of neuropeptide-Y on tectal field potentials in the toad. *Brain Research* 669(1):150–152. https://doi.org/10.1016/0006-8993(94)01260-O
   - Required for the pharmacological evidence concerning NPY. The publisher PDF route returns a 403 connection denial. Metadata and abstract verified against Crossref and Europe PMC. NPY application and stimulation effects must be distinguished from direct proof of endogenous transmitter release or receptor-subtype necessity.
6. McConville J, Laming PR (2007). DC electrical stimulation of the pretectal thalamus and its effects on the feeding behavior of the toad (Bufo bufo). *Developmental Neurobiology* 67(7):875–883. https://doi.org/10.1002/dneu.20390
   - Required for behavioral stimulation evidence and its limits. Wiley's PDF route returns HTTP 403; Europe PMC lists no deposited PDF.

Scholarly web searches: Crossref queries for pretectal lesions, predator avoidance, NPY and amphibian looming responses; Europe PMC queries for the same topics, DOI-specific records and source titles. OpenAlex queries were rate-limited, so they are not evidence of access availability. Recorded access results are retained in the working research directory.

After upload: inspect every paper, verify source details and captions, supplement with accessible modern amphibian studies where relevant, crop published panels with tools/crop_figure.py or tools/crop_panels.py, and build with tools/build_lecture.py. Keep 46 slides, exact schedule metadata, Arial, 3–5 explanatory paragraphs, full DOI references and teaching transcripts. At least 40 content slides need images and at least 34 primary figures; aim for original color on half. Use two columns with readable figures beside the text, preserve all axes/units/scale bars/panel labels, and render every slide for visual QA. Select and record a new permitted theme only when the completed deck passes review.

The strict source-image rules and reusable prompt already exist in AGENTS.md, .claude/skills/neuroethology-lecture/SKILL.md and prompts/make_lecture.md; retain them.
