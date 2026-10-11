"""Scaffold spec for Lecture 29 (Drive deck Neuroethology_Lecture29_FA2026.pptx).

Body rewrites are in body_L29.py, lengthened by L29_extend.py. Insert slides clone the figure of the
slide they follow; their paragraphs teach the facts behind that figure.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L29 as _body  # noqa: E402
import L29_extend as _ext  # noqa: E402


def ins(after, title, paragraphs, citation, refs):
    notes = [title + "."] + [
        [f"Explanation {i + 1}.", *(p.split(". ", 1))] for i, p in enumerate(paragraphs)
    ]
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


inserts = [
    ins(3, "Waggle angles vary across repeated runs", [
        "The absolute flight bearing also depends on the sun's current position, not on the comb angle alone. Because the sun moves across the day, a fixed food source can call for different waggle-run angles at different times. A dance therefore reflects the sun's position at the moment it is performed, so one site can be advertised with several angles.",
        "Each waggle run is followed by a return loop that brings the dancer back to the start of the next run. The loop itself is not a second advertised destination, so the straight runs carry the directional information. A follower that tracks the sequence therefore attends to the runs, while the loops only organize the repetition of those runs.",
        "Divergence among repeated runs measures variation around the advertised angle. A systematic bias in the average bearing is a different error, and the two have different consequences for a follower. An average bearing can be correct while individual runs vary widely, so the spread of runs and their mean angle answer separate questions. The mean angle gives the bearing, and the spread shows reliability.",
    ], "Dong et al. (2023)", ["Dong 2023"]),
    ins(6, "Displaced recruits keep the flight vector", [
        "The harmonic radar transponder marks where the bee is, not a neural signal, so each track is a record of position over time. Reading a recruit's flight therefore means reading its path through the landscape. Each track also begins at the point where the recruit was released, so the starting site is part of the record.",
        "Search counts as a genuine part of recruitment rather than an error-free continuation of the initial vector. Its later phase therefore belongs to the navigation itself, not to noise in the endpoint data. Recruits that search follow a different routine from those flying straight, and both phases belong to the same recruitment event. Counting that phase keeps the full recruitment event in view.",
        "Ground velocity combines the bee's movement through the air with air movement over the ground. Air drift can push the heading away from the destination direction, so heading and destination are different quantities. Measuring both allows the two to be told apart, and the difference between them is what the recruit corrects for. Both must be kept separate to read a track.",
    ], "Riley et al. (2005)", ["Riley 2005"]),
    ins(9, "Tunnel texture drives the visual odometer", [
        "Waggle duration is the measured motor output of the dance. The texture contrast addresses distance estimation rather than reward quality, so a change in dance type reflects the visual input. Followers decode the dance, so the difference reaches them as a change in the message they receive. Reward quality was not the variable under test.",
        "A tunnel flight is interpreted through the outdoor relation without being equated with an ordinary outdoor flight. The tunnel result is therefore a reading of the signal, not a claim about how far the bee flew outdoors. The dance itself is the only evidence that the reading uses, so the inference stays tied to the signal.",
        "Stripes and random texture impose different visual motion while the target location stays the same. The dance type therefore reflects the visual input received along the route, with the physical destination held fixed. The texture comparison isolates visual input from reward and location within a single design. Sensory input is the only variable that changes.",
    ], "Srinivasan et al. (2000)", ["Srinivasan 2000"]),
    ins(12, "Short tunnel journeys signal long distances", [
        "The tunnel results establish a visual dependence of the signal without requiring any claim that the bee perceived meters. The duration itself is a measured motor output, and the outdoor relation gives that output its distance reading. The signal therefore carries information about the visual route, not about the bee's sense of length. This keeps the interpretation on the signal side.",
        "This relation is applied to the tunnel passages without treating them as ordinary outdoor flights. The reading therefore describes what the dance signals about the route, not a measured outdoor journey. The calibration itself was measured on outdoor feeders, so the tunnel values are set against an independent outdoor scale. Both arrangements sit on the same scale.",
        "Two arrangements with different outdoor approach lengths produced readings that both exceed the physical journey. Their shared pattern points to the visual surroundings as the source of the inflated signal, consistent with the close textured walls both passages shared. Neither reading depends on the length actually flown outdoors, because both values come from the same calibration.",
    ], "Srinivasan et al. (2000)", ["Srinivasan 2000"]),
    ins(15, "Closing the tunnel stops recruitment", [
        "The dancer and the follower can share a visual interpretation because both navigate comparable terrain along the route. That shared terrain links the advertised tunnel distance to the search that follows. The tunnel distance is therefore decoded in visual terms rather than in meters. The link depends on the terrain both bees experience. Both bees use that terrain for orientation.",
        "Bees arriving at the control stations were captured, so their own return dances could not add recruitment to a station. The search pattern therefore tests how followers decode a dance, independently of the dancer's physical flight length. Station arrivals measure the decoding alone, since the stations offered no reward. Recruitment therefore reflects the dance information alone.",
        "The physical feeder distance and the searched distance are experimentally distinct quantities. Recruit searches measure the followers' interpretation of the dance, not the feeder's physical position. Each search site is therefore a readout of a visual calibration. The experiment reports searched distances in meters from the hive. Searches are reported as distances from the hive.",
    ], "Esch et al. (2001)", ["Esch 2001"]),
    ins(18, "Land scenes carry more image contrast", [
        "Low contrast can weaken motion signals even when the animal keeps moving. The water segments therefore reduce the effective image motion the odometer receives, even though the bee continues flying across them. The odometer's rate of accumulation is set by that input, so a slower rise in duration over water follows from the image structure.",
        "The photographs document the actual terrain rather than a reconstructed visual stimulus. Their measurement windows therefore reflect the scene a bee flew over, which gives the contrast values a direct link to real foraging routes. Each photograph was taken along the route a recruit actually flew. Those windows were applied to every scene in the same way.",
        "A correlation across route segments also tracks flight height, viewing direction and surface texture. Those factors vary together along a route, so contrast is one of several linked variables. The controlled tunnel-texture experiments supply a separate intervention on visual motion, which isolates one variable at a time. The tunnel manipulation alone changes texture while holding the rest of the route fixed.",
    ], "Tautz et al. (2004)", ["Tautz 2004"]),
    ins(21, "Tracing links the dorsal rim to the MEDRA", [
        "Covering the extradorsal region left the candidate polarization-sensitive area available, a stronger test of localization than covering the whole eye. Bees in that group retained the trained discrimination while much of the eye stayed occluded. The control therefore asks whether the effect follows the specialized region or simply the amount of eye covered. The rim is the candidate region under test.",
        "The result therefore points to the rim's specific role under these conditions rather than to the total amount of light reaching the eye. The rim lies at the top of the eye, so a localized occlusion tests that area directly. Covering it removed the rim input whose downstream pathway is traced in the next experiment.",
        "Zeller's tracing shows that rim input reaches a dorsal-medulla compartment, while Sakura's occlusion shows that the rim is needed for the learned response. Each experiment addresses a separate level of the same pathway. In both experiments the dorsal rim is the variable that changes, while the rest of the eye is held as a control.",
    ], "Sakura et al. (2012); Zeller et al. (2015)", ["Sakura 2012", "Zeller 2015"]),
    ins(24, "Polarization axis sets the dance axis", [
        "The polarizer orientation changed while the tunnel direction stayed fixed, so the two groups differed only in the polarization pattern. Any difference between their dances therefore came from that pattern. Both groups flew the same textured tunnel, and their dances were measured on the comb after training. The diffuser was used in both groups, which holds the sky cue constant for both groups.",
        "The original article provides the preparation images and the measured dance distributions. The direction plots in this deck were not reconstructed from raw data, so the reported axes are the authors' own values. The mean axes were measured separately for the transverse and axial groups. The authors' numbers are reported directly in the source. Both values come from that source.",
        "The signal therefore carries an orientation on the comb, and the sign of the direction is missing. Each group's waggle runs came from the same comb and were measured the same way, so the two axes are directly comparable. Such a signal narrows the possible headings to one line on the comb. The axis carries the information the bees conveyed.",
    ], "Evangelista et al. (2014)", ["Evangelista 2014"]),
    ins(27, "Cloud cover removes direct sun sight", [
        "The actual daily course of the sun was known independently from astronomical position. The bees' dances can therefore be judged by a reference calculated from astronomy. The two groups' dance orientations can then be checked against that reference across the test, which makes the astronomical course an independent standard. The astronomical course is the reference for the dances.",
        "Direction in this experiment was inferred from dances relative to a known food route. No electrode recorded a sun representation in the bees, so the solar estimate comes from the dance orientation alone. The inference therefore rests on what the dancers communicated, not on neural recordings. Dance orientation is the only measured quantity in this comparison.",
        "Shared cloud cover controlled the immediate celestial cues available to both groups. The remaining difference between the two dance patterns therefore reflects the bees' training history under matched sky conditions. Both groups were tested on the same cloudy day. The bees' flight histories were the factor that differed. Sky conditions were identical for both groups.",
    ], "Dyer & Dickinson (1994)", ["Dyer 1994"]),
    ins(30, "Anesthesia delays the hive's activity rhythm", [
        "Cryptochrome and period expression were sampled across the daily cycle rather than at a single time after treatment. A sampling schedule of this kind shows the whole rhythm, not a snapshot of one moment in the day. Sampling across the day sets the timing of each measurement, so a phase shift can be seen directly.",
        "A phase shift changes when the rhythm peaks, not simply whether a gene is expressed. A delay in the rhythm therefore appears as a change in timing, and expression levels can remain similar while their peaks move. Shifts in timing are the quantity that matters here, not the on-off state of each gene. Peak timing is what a phase shift moves.",
        "Both the anesthetic target and the cells supplying timing to the compass pathway are left unidentified here. Averaging over whole brains hides which cells those are, so the mechanism stays open. This study measured the hive, not individual cells, and identifying the cells is required before the timing signal can be traced. The cells are the open question here.",
    ], "Cheeseman et al. (2012)", ["Cheeseman 2012"]),
    ins(33, "PDF fibers lie beside transmedulla neurons", [
        "Immunoreactivity means that an antibody recognizes its target in the preparation. Staining establishes that the labeled substance is present in a region. A specific connection needs separate evidence, since a labeled structure is a location and not yet a connection. Its function needs a separate test, and staining alone gives that test no answer. The labels are therefore evidence of presence only.",
        "Close proximity is a candidate contact. Peptide release, a postsynaptic PDF receptor and a functional synapse would each need separate evidence before any of them could be assumed to operate in this pathway. The two labels were also examined at higher magnification to measure that proximity. The two labels were combined in a single preparation.",
        "A nearby labeled bouton marks a possible site of contact. Its role in circadian compass correction is a proposal drawn from how the two labels sit in the medulla. The contact therefore stays a candidate until other methods test it in this preparation. Its strength depends on the staining conditions used in that preparation. The labels were examined in one layer.",
    ], "Zeller et al. (2015)", ["Zeller 2015"]),
    ins(36, "Separated complexes lie in both bulbs", [
        "Synapsin and actin are markers rather than transmitter identities. Their different distributions help identify terminal compartments before the finer synaptic membrane structure is examined. Each marker therefore shows where a structure lies, not what signal a given terminal carries. Both stains were applied to honeybee bulb tissue. The markers help set up the anatomy before finer imaging.",
        "Traced TuLAL1 terminals occupied the presynaptic cores, and processes from TL neurons contacted them from the postsynaptic side. The arrangement is stained in both the lateral and medial bulbs, so the same organization appears in each bulb. Each TL process therefore touches a terminal that TuLAL1 has already occupied, which places the two cells in one complex.",
        "Confocal imaging shows where profiles lie close together. Electron microscopy resolves those contacts, and the authors used it to examine the complexes at membrane resolution. The confocal stage gives the arrangement, and the electron stage gives its membrane detail. Each stage answers a different question about the complexes. The membrane detail confirms the contacts that the stains suggested.",
    ], "Held et al. (2016)", ["Held 2016"]),
    ins(39, "Learned field cues persist for 24 h", [
        "Treatments applied after conditioning distinguish sensory access at test from the initial acquisition of the association. Bees were first trained with their antennae intact, which sets the association before any manipulation. Learning is therefore held constant while the sensory access alone changes. Treatments at test then probe what the bees currently use. The timing of the treatment is the variable under study.",
        "Coating the surfaces and restricting the joints are different manipulations, and they produced different reductions in the learned response. Each treatment targets a distinct route of mechanical input from the antenna. A coating that leaves the joints mobile is therefore a weaker manipulation of joint input than restriction. The two treatments are compared on the same learned response.",
        "The conditioned response to electric cues was retained for 24 h after conditioning. Learning therefore persisted across a full day, which places the field cue within a memory that outlasts a single training session. The retention test was run on the same bees that had learned the cue, so the memory belongs to those individuals.",
    ], "Greggers et al. (2013)", ["Greggers 2013"]),
    ins(42, "Mature foragers differ from young workers", [
        "Young bees had been kept in cages, while the foragers had natural behavioral experience before recording. The two groups therefore differ in more than age, and the group contrast reflects the conditions each group lived in. Those living conditions are part of what the cell measurements capture. Both groups were tested with the same recording preparation.",
        "Reconstructions and response distributions document the change at two levels of analysis. The arborizations describe the cell's anatomy, and the response distributions describe its activity during stimulation. Each level captures a different aspect of the same neuron, so the two levels complement each other. The recordings were made from the same identified neuron type. The two levels were reported together.",
        "Foragers also showed branch density differences in selected regions, while the overall arbor extent stayed similar. Those regional branch changes provide a structural correlate for the response difference seen in the recordings. The branch differences are therefore a candidate anatomical basis for the response change. Both changes are reported for the same cell type. Both changes accompany the age difference.",
    ], "Kumaraswamy et al. (2019)", ["Kumaraswamy 2019"]),
]

for _k, _ps in _ext.EXTEND.items():
    for _p, _t in _ps.items():
        _body.body[_k][_p - 1] = _body.body[_k][_p - 1] + _t
# sentences dropped so that the body fits the free column at 14 pt (slides with figures on the right)
for _k, _ps in _ext.TRIM.items():
    for _p, _t in _ps.items():
        assert _t in _body.body[_k][_p - 1], (_k, _p, _t)
        _body.body[_k][_p - 1] = _body.body[_k][_p - 1].replace(_t, "")
# full rewrites for slides with one free column (see L29_extend.OVERRIDE)
for _k, _paras in _ext.OVERRIDE.items():
    _body.body[_k] = list(_paras)
for _ins in inserts:
    if _ins["after"] in _ext.INSERT_OVERRIDE:
        _ins["paragraphs"] = list(_ext.INSERT_OVERRIDE[_ins["after"]])
for _ins in inserts:
    for _p, _t in _ext.INSERT_EXTEND.get(_ins["after"], {}).items():
        _ins["paragraphs"][_p - 1] = _ins["paragraphs"][_p - 1] + _t
    _ins["notes"] = [_ins["title"] + "."] + [
        [f"Explanation {i + 1}.", *(q.split(". ", 1))] for i, q in enumerate(_ins["paragraphs"])
    ] + [["Source.", f"The figure and the measurements come from {_ins['citation']}.", "Each statement is tied to the recordings or observations of that study."]]

spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(_body.body)} body slides rewritten, {len(inserts)} scaffold slides")
