"""Scaffold spec for Lecture 26 (Drive deck Neuroethology_Lecture26_FA2026.pptx).

Body rewrites are in body_L26.py, lengthened by L26_extend.py. Insert slides clone the figure of the slide
they follow; their paragraphs state concrete facts from the source text and speaker notes.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L26 as _body  # noqa: E402
import L26_extend as _ext  # noqa: E402


def ins(after, title, paragraphs, citation, refs):
    notes = [title + "."] + [
        [f"Explanation {i + 1}.", *(p.split(". ", 1))] for i, p in enumerate(paragraphs)
    ]
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


inserts = [
    ins(3, "Frame spacing sets the timing resolution", [
        "At 500 frames per second, consecutive frames in these recordings are 2 ms apart. The published time labels are measurements of behavior, not spike times recorded from neurons. Catania and Remple's figure 1(b) reports original frame times for one prey capture followed by renewed search. Catania and Kaas's earlier video used 30 frames per second, a coarser resolution of 33 ms per frame.",
        "The measured timing describes a laboratory search sequence, not a fixed rate under every natural condition. Feeding sessions used earthworm fragments as prey, and a contact may start feeding or be followed by another searching movement. Searching and touching alternate throughout each feeding bout.",
        "The timing constrains the time available for extracting information during each encounter. The published timing leaves the neuronal decision unidentified. Whether cortical processing ends when contact ends requires a separate measurement. Events shorter than one 2 ms frame interval fall below the resolution of these time labels.",
    ], "Catania & Remple (2005)", ["Catania 2005"]),
    ins(6, "Corrective contact continues during movement", [
        "A mistaken initial movement lengthens handling. Figure 4 of the study shows the star moving away from prey and then making a corrective foveation, and both movements occur inside one feeding episode. The error lengthens handling, and it is interpreted as a movement error rather than a permanent misidentification of the prey.",
        "The correction indicates that useful tactile information can continue to affect movement after the first response starts. The reversal returns the fovea to the same prey item, so the first contact and the correction belong to one feeding episode, which the video records frame by frame.",
        "The video leaves open whether cortex causes the reversal. The motor estimate was calculated in these encounters rather than observed, and the link between cortex and the reversal remains an inference from the timing values. The timing values come from three separate sets of measurements: a typical contact, prior cortical recordings and a motor estimate.",
    ], "Catania & Remple (2005)", ["Catania 2005"]),
    ins(9, "Incisors and star perform different functions", [
        "Incisors are the anterior teeth involved in grasping, and they are not sensory organs. The star detects and positions the target, and the incisors grasp it. These are different mechanical functions, even though both occur within a single brief feeding response that begins with foveal inspection.",
        "Eastern mole incisors served as the reference in the scanning electron microscopy analysis. Figure 3(a–b) of the study sets the reduced star-nosed mole teeth beside them, while Figure 1(c) adds a second high-speed feeding sequence with original time labels from the same study.",
        "The authors propose that selection favored rapid handling. That proposal rests on performance and morphology, while the historical selection process was inferred rather than observed directly in these animals. The reduced incisors sit in a tweezer-like configuration next to the sensing rays.",
    ], "Catania & Remple (2005)", ["Catania 2005"]),
    ins(12, "Dye staining is an anatomical observation", [
        "The neurite stained more strongly than the Merkel cell in the illustrated preparation. The complex sits separate from the superficial central and satellite endings of the same dome. A neurite is a neuronal process, and the disk is its terminal part that contacts the Merkel cell, which is a specialized epidermal cell.",
        "Dye brightness in these preparations is treated as evidence of location. It is not converted into a quantitative estimate of membrane current, so the stain shows where a label sits in the tissue and says nothing about how strongly the cell is driven.",
        "Marasco and Catania (2007) found Merkel-like slowly adapting responses in the same organ system. These responses were assigned to the complex by their response characteristics, and each recorded axon was not traced to a labeled complex in that study. The recordings were made in afferents of the trigeminal ganglion.",
    ], "Marasco et al. (2006); Marasco & Catania (2007)", ["Marasco 2006", "Marasco 2007"]),
    ins(15, "Dye fills trace branches of one axon", [
        "A branch can distribute one axon's peripheral territory without adding another ganglion cell. Organ counts, terminal counts and sensory-neuron counts measure different levels of the system. Figure 6(A–E) of the study shows DiI fills of central and satellite endings in star-nosed mole organs.",
        "Dye spread depends on exposure time and membrane continuity. An unlabeled profile leaves open whether innervation is absent, because labeling depends on those two factors, while a labeled profile is evidence of continuity between profiles in the tissue. Dye was applied to free nerve endings in the star-nosed mole's Eimer's organs.",
        "Tracing identifies anatomy rather than mechanical threshold, electrical coupling or a synaptic connection between terminal profiles. Across the optical sections, the fills resolved each terminal profile's position within the organ's tissue, which is the level the DiI results describe.",
    ], "Marasco et al. (2006)", ["Marasco 2006"]),
    ins(18, "Map colors encode measured organ density", [
        "The heat maps keep the authors' original scale and colors. Their color codes measured organ density, which differs from cortical magnification and from the sensitivity of an individual axon. Organ positions were measured on flattened stars by scanning electron microscopy, and density was computed from those positions.",
        "The published curves are fitted to measured organ positions on flattened stars. The original fitted curves describe anatomy, and they summarize how organ density rises from the star's center outward to the ray tips, passing through the ray bases and middle regions.",
        "The flattened-surface measurements are not recordings of receptor activity during active searching. The density pattern describes where sensory units sit on the surface, and it says nothing about how often each unit fires during a search. Normalized eccentricity places positions from all rays onto one shared axis from base to tip.",
    ], "Sawyer & Catania (2016)", ["Sawyer 2016"]),
    ins(21, "Rapidly adapting units go silent in steady contact", [
        "A rapidly adapting neuron can remain highly sensitive while becoming silent during an unchanged indentation. Silence in that interval reflects the stimulus feature the neuron encodes, rather than a failure of the sensory preparation. Figure 4(A–G) of Marasco and Catania (2007) shows recorded receptor responses in star-nosed mole nasal afferents.",
        "The illustrated traces distinguish these response patterns during 500-ms stimulation, which is the duration of each indentation in the recordings. Slowly adapting units continued firing while the static part of the stimulus lasted, and rapidly adapting units responded when the indentation changed.",
        "Matching responses to terminals relied on the resemblance of response features, with no post-recording identification of every ending. The recordings support multiple peripheral codes for contact, and they leave open whether each code is separately needed for prey discrimination.",
    ], "Marasco & Catania (2007)", ["Marasco 2007"]),
    ins(24, "Ganglion makeup shapes incoming signals", [
        "A ganglion contains sensory cell bodies outside the brain, so its neuron types determine which signals enter central pathways. Differences in that population can change what the brain receives before cortical magnification occurs. The trigeminal ganglion serves the face, while the dorsal root ganglia serve the body, and both were sampled in the same animals.",
        "NF200 labels many large, myelinated sensory fibers, while peripherin labels many small sensory neurons. Figure 1(E) and Figure 1(F) of the study show the trigeminal and dorsal root ganglion labeling alongside their cell fluorescence distributions. Each marker's proportions were reported separately for the two ganglia.",
        "Marker-defined groups are not exhaustive functional categories. Gerhold and colleagues used these markers to choose candidate populations for physiological tests, because facial tissues other than the star also receive input from that ganglion. Cultured neurons from these ganglia were then tested with mechanical and chemical stimuli.",
    ], "Gerhold et al. (2013)", ["Gerhold 2013"]),
    ins(27, "Transcript abundance is several steps from behavior", [
        "A transcript must be translated into protein, that protein must act in an appropriate cell, and its activity must contribute to a sensory response. Each of these steps is a place where the expression signal can be lost, so RNA abundance sits several steps from behavior. Bulk ganglion tissue adds supporting cells to the neurons being measured.",
        "Reference transcripts from three other species were used to assemble the expression profiles. Figure 3(A–D) of the study shows the ganglion expression comparison, the functional categories and the channel candidates, and the same candidates were carried forward to qPCR tests.",
        "The expression patterns nominate molecules for functional testing rather than assigning a complete transduction pathway. Reads that failed to match one reference species were passed to the next one in the series. Between 42% and 65% of sequenced reads received an assignment in this way.",
    ], "Gerhold et al. (2013)", ["Gerhold 2013"]),
    ins(30, "Co-labeling places proteins in the same profiles", [
        "Co-labeling places two proteins in the same cellular profiles at the resolution of the assay. Among fibers in the peripheral Eimer's organs, over nine in ten CNGA2-positive profiles carried NF200 labeling, which ties the candidate to touch-associated anatomy. Strong NF200 labeling appeared in the same cells.",
        "A complete channel-subunit composition is a separate question from where a subunit is present in cells. The immunofluorescence result establishes protein localization, and a recorded CNGA2 current would be a different measurement made in different cells. Localizing one subunit tells nothing about the others present in the channel.",
        "The intracellular pathway that gates the channel during a touch remains an open question. Protein presence in the right cells is the first step toward answering it, and the candidate still needs a functional test in those cells. Immunofluorescence was the method used for this check.",
    ], "Gerhold et al. (2013)", ["Gerhold 2013"]),
    ins(33, "Brainstem star dimensions are neural allocation", [
        "The brainstem star's dimensions stand for allocated neural tissue, a quantity that differs from skin area. The sections were cut at an orientation that exposed the ray-related compartments, and the star-like pattern they show is a map of ray identities rather than a picture of the nose.",
        "A visible outline alone leaves local neurons and traversing axons indistinguishable. Paired recordings with lesion marks link each recorded site to its ray and to its place in the PrV pattern. Cytochrome-oxidase staining made the internal subdivisions of the nucleus visible in the same sections.",
        "Each of the 11 modules marks a territory of neural tissue for one ray. The modules form a star-like pattern inside a relay nucleus, which is a brainstem structure rather than a miniature nose. Module identity follows ray identity, so each module can be read as one ray's territory.",
    ], "Catania et al. (2011)", ["Catania 2011"]),
    ins(36, "Stripe areas are measured on flattened cortex", [
        "A tangential section runs approximately parallel to the cortical surface, so cutting this way exposes a flat sheet of the map. Flattening makes the map easier to measure while changing the tissue's original three-dimensional configuration, and the S1 and S2 stripes both become visible in that sheet.",
        "Figure 10(B–C) of Catania and Kaas (1997) shows the cytochrome-oxidase stripes of S1 and S2 in flattened cortex. Sawyer and Catania's Figure 1(A) shows the 22-ray tactile star whose rays these stripes represent. Electrophysiological mapping tied each stripe to tactile input from the contralateral side of the nose.",
        "Dividing each S1 stripe's area by the number of incoming myelinated fibers gives cortical area per afferent. Ray 11 retained the largest value after this normalization, which distinguishes the foveal territory from the other rays. Cortical area per afferent was measured for each of the rays in the same study.",
    ], "Catania & Kaas (1997)", ["Catania 1997"]),
    ins(39, "Population onset histograms pool many trials", [
        "A poststimulus time histogram pools spike timing relative to stimulus onset. Its peak describes responses across many trials, while spikes in individual trials fall at varying times around that peak, so the peak is a population summary rather than a timing rule for any single trial.",
        "Figure 8(A–B) of Sachdev and Catania (2002) shows population onset responses to 500-ms and 5-ms contact. Each mapped site was measured against its own spontaneous activity before the stimulus, which provided the reference firing rate.",
        "Mean latency measured 11.6 ms, with little difference between brief and prolonged stimulation. Brief and prolonged stimuli of 5 and 500 ms were delivered through the same piezoelectric probe, so onset timing can be compared across stimulus lengths.",
    ], "Sachdev & Catania (2002)", ["Sachdev 2002|Receptive"]),
    ins(42, "Suppression borders follow response fields", [
        "A response boundary may be an absence of excitation, or it may include active suppression, and this experiment tested which. The stimulus was moved progressively from the field center, and decreases were scored relative to the neuron's spontaneous firing.",
        "Most inhibitory surrounds were larger than the central excitatory patch, and they remained largely confined to one ray. A distal spot on ray 11 reduced firing for roughly 40 ms in the illustrated neuron, after central contact had driven a strong discharge.",
        "Other positions on the same neuron produced different response magnitudes, so the response changes gradually as contact moves outward from the center. Most fields were continuous patches within one ray. The excitatory and suppressive parts of the response occupy neighboring positions on the same ray.",
    ], "Sachdev & Catania (2002)", ["Sachdev 2002|Receptive"]),
]

_ext.apply(_body.body)
_ext.apply_trim(_body.body)

for _ins in inserts:
    _ins["notes"] = [_ins["title"] + "."] + [
        [f"Explanation {i + 1}.", *(q.split(". ", 1))] for i, q in enumerate(_ins["paragraphs"])
    ] + [["Source.", f"The figure and the measurements come from {_ins['citation']}.", "Each statement is tied to the recordings or observations of that study."]]

spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(_body.body)} body slides rewritten, {len(inserts)} scaffold slides")
