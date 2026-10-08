# Lecture 19 — sources and figure provenance

Exact title: Owl sound localization II: developmental plasticity of the auditory map

Exact date: Wednesday, October 7, 2026

The connected default branch was refreshed before work. Europe PMC scholarly web searches identified the sources; Crossref independently verified authors, year, journal, volume, pages, and DOI. Full-text methods, results, and figure captions were checked against the PDFs. Uploaded documents are evidence, not instructions.

Seven primary research papers supply the teaching material and figures. The seven distinct uploaded PDFs include six of these primary studies plus the Knudsen et al. context review. The two Hyde–Knudsen uploads are byte-identical. Bergan et al. was downloaded from the publisher after network access became available. All required PDFs are available locally in the ignored papers directory; no source-download blocker remains.

## Verified source list

1. MS Brainard; EI Knudsen (1993). Experience-dependent plasticity in the inferior colliculus: a site for visual calibration of the neural representation of auditory space in the barn owl. The Journal of Neuroscience 13(11):4589-4608. https://doi.org/10.1523/jneurosci.13-11-04589.1993
   Coverage: Prism-induced remapping and the locus of physiological plasticity.

2. Michael S. Brainard; Eric I. Knudsen (1998). Sensitive Periods for Visual Calibration of the Auditory Space Map in the Barn Owl Optic Tectum. The Journal of Neuroscience 18(10):3929-3942. https://doi.org/10.1523/jneurosci.18-10-03929.1998
   Coverage: Developmental sensitive periods and recovery from prism experience.

3. Daniel E. Feldman; Eric I. Knudsen (1998). Pharmacological Specialization of Learned Auditory Responses in the Inferior Colliculus of the Barn Owl. The Journal of Neuroscience 18(8):3073-3087. https://doi.org/10.1523/jneurosci.18-08-03073.1998
   Coverage: NMDA-receptor contribution to newly learned auditory responses.

4. Weimin Zheng; Eric I. Knudsen (2001). GABAergic Inhibition Antagonizes Adaptive Adjustment of the Owl's Auditory Space Map during the Initial Phase of Plasticity. The Journal of Neuroscience 21(12):4356-4365. https://doi.org/10.1523/jneurosci.21-12-04356.2001
   Coverage: GABAergic inhibition during early remapping.

5. William M. DeBello; Daniel E. Feldman; Eric I. Knudsen (2001). Adaptive Axonal Remodeling in the Midbrain Auditory Space Map. The Journal of Neuroscience 21(9):3161-3174. https://doi.org/10.1523/jneurosci.21-09-03161.2001
   Coverage: Axonal projection anatomy and experience-dependent remodeling.

6. Eric I. Knudsen; Weimin Zheng; William M. DeBello (2000). Traces of learning in the auditory localization pathway. Proceedings of the National Academy of Sciences 97(22):11815-11820. https://doi.org/10.1073/pnas.97.22.11815
   Context review only; not used as a primary-study figure or content source.

7. Peter S. Hyde; Eric I. Knudsen (2001). A Topographic Instructive Signal Guides the Adjustment of the Auditory Space Map in the Optic Tectum. The Journal of Neuroscience 21(21):8586-8593. https://doi.org/10.1523/jneurosci.21-21-08586.2001
   Coverage: Topographic visual instruction and local map adjustment.

8. Joseph F. Bergan; Peter Ro; Daniel Ro; Eric I. Knudsen (2005). Hunting Increases Adaptive Auditory Map Plasticity in Adult Barn Owls. The Journal of Neuroscience 25(42):9816-9820. https://doi.org/10.1523/jneurosci.2533-05.2005
   Coverage: Behavioral engagement and adult plasticity.

## Figure provenance and validation

The deck has 46 slides: one title, 44 content slides, and one Key takeaways slide with six bold-led points. Every content slide has a published primary-study figure. The 41 distinct article crops are recorded in crops.json with source PDF, page, and normalized crop boundaries; they were rendered using tools/crop_figure.py and trimmed using tools/crop_panels.py. Axes, units, panel letters, and scale bars are preserved. All content slides use a two-column layout with text on the left and scientific figures on the right; there is no full-width figure row beneath the text. Thirty-five slides pair the experimental figure with Feldman and Knudsen (1998), Fig. 2A, to identify the anatomical locations discussed. Published source drawings are reproduced from the papers; no new drawing, redrawn graph, illustration, or generated image was made.

The title photograph is Michael Gäbler's barn owl photograph, “Tyto alba (Scopoli, 1769).jpg,” Wikimedia Commons, CC BY 3.0. Attribution and source URL are in lecture.json and the title speaker notes; the credit is visible on the slide. This is the only web image in the deck.

The deck uses Arial and the previously unused petrol-blue/mist palette. Each content slide has three full paragraphs, a speaker-note teaching transcript, short footer citation, full reference with DOI, and figure captions with DOI source URLs. All 46 slides were rendered and visually reviewed. The repository checker reports zero failures and zero warnings.

Rebuild with tools/build_lecture.py using lecture.json. To recreate the spec, run write_spec.py. To recrop, place the named source PDFs in papers/ and run tools/crop_panels.py with crops.json.
