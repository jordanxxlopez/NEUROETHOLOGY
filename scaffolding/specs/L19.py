"""Scaffold spec for Lecture 19 (source deck drive_updated/Neuroethology_Lecture19_FA2026_V2.pptx).

Body rewrites are in body_L19.py. Insert facts come from the
speaker-note glosses and from the same paper's other slides (see the report in the commit notes).
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L19 as _body  # noqa: E402


def ins(after, title, paragraphs, citation, refs):
    notes = [title + "."] + [
        [f"Explanation {i + 1}.", *(p.split(". ", 1))] for i, p in enumerate(paragraphs)
    ] + [["Source.", f"The figure and its data come from {citation}.", "The full references are listed below."]]
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


inserts = [
    ins(3, "Occlusion and displacement differ in input", [
        "A visual receptive field, or VRF, is the region of visual space whose stimulation drives a neuron. Auditory tuning recorded at the same site can be read against that VRF, which shows where a given timing preference points in space. Each site thus links a timing value to a point in the visual field, and the prismatic displacement changes that visual reference.",
        "Occluding part of the visual field removes regional visual information, leaving that region without any input. An optical displacement works differently, because visible objects remain present while their apparent positions move. The two manipulations probe different aspects of the visual input and can yield different auditory outcomes.",
        "In one owl, the visual field beyond 15° was occluded while the central field stayed normal. That arrangement kept normal vision at the center of gaze and left the periphery without visual input. Regions with different visual status within one animal give an internal control for the calibration.",
    ], "Hyde & Knudsen (2001)", ["Hyde 2001"]),
    ins(6, "Electrode lesions anchor timing to tissue", [
        "Ear-leading labels state which ear receives the waveform first, so each timing value carries a sign as well as a magnitude. Leftward and rightward displacements produce timing values that differ in sign. Reading the sign of each measured value is what allows the direction of an adaptive shift to be identified.",
        "Electrode-site lesions linked each measured response to a specific anatomical location. Histology identifies tissue structures in thin stained sections, so a response could be assigned to tissue rather than judged from the shape of its tuning curve alone. Lesions marked at recording sites provided the anatomical reference for that assignment.",
        "Topographic projections preserve an ordered relationship between source and target locations. Such projections connect the ICX spatial representation with the tectal map. An ordered location in ICX can be followed to a corresponding position in the optic tectum. Ordered projections preserve neighboring relations, so neighboring ICX locations project to neighboring tectal locations.",
    ], "Brainard & Knudsen (1993)", ["Brainard 1993"]),
    ins(9, "Shift size is set by the visual reference", [
        "A complete adaptive shift is a reference predicted from the visual displacement. It is an expectation for the animal's map, not an assumption that every animal must reach the same endpoint. Owls differ in how far their maps move, so the predicted shift works as a benchmark rather than a fixed outcome.",
        "The outcome in this work is how far the auditory preference sits from the normal visual reference. The count of days spent in prisms is a distinct measure and is not a substitute for displacement. Displacement relative to that reference expresses the adaptation of each owl.",
        "Chronic recording means returning to the same preparation across time. Repeated measurements of this kind establish the temporal course of functional adaptation, which one session alone would not reveal. Each animal's time course can then be set against the predicted endpoint. Stable and changing maps can be told apart by repeated sessions.",
    ], "Brainard & Knudsen (1998)", ["Brainard 1998"]),
    ins(12, "Orienting error measures behavior, not tuning", [
        "Auditory orienting error is the difference between the direction of a sound source and the owl's head orientation. It is a behavioral quantity distinct from the neuronal best ITD, and both were assessed in the cage and aviary experiments. Each measure reports a different aspect of the adjustment.",
        "The strength of adaptation to a novel displacement is one question, and the ability to recover a normal mapping after prism removal is another. Those two abilities place their own requirements on the circuit, so the two measures should be kept apart. Neural recovery and behavioral recovery were tested as distinct outcomes.",
        "An auditory threshold is the minimum sound level that reliably evokes a response. Changes in threshold must be distinguished from changes in the preferred timing cue. Impaired sound sensitivity can alter a measured response, so the threshold measure guards the timing result. Its change is measured separately from the timing shift.",
    ], "Brainard & Knudsen (1998)", ["Brainard 1998"]),
    ins(15, "Housing order distinguishes input from its use", [
        "Prior calibration provides a different starting circuit state from the state of an adult encountering an unfamiliar optical displacement. The owls here had already regained normal vision when the housing changed. Normal visual input was in place before the aviary transfer. Housing was changed once the visual input had already returned.",
        "Sensory calibration in these owls was reversed by restoring normal vision, and the animals were moved afterward. Reversal of the imposed displacement changes which ITDs are adaptive. The measured response must be judged against the new optical condition. The starting state of each animal shapes what the transfer can reveal.",
        "The housing change followed the visual manipulation rather than preceding it, so the two factors were applied in sequence. The mechanism behind the aviary effect is still to be identified. The aviary period changed the expression of an existing capacity rather than creating one.",
    ], "Brainard & Knudsen (1998)", ["Brainard 1998"]),
    ins(18, "A paired regional comparison controls history", [
        "Center-of-gaze and peripheral manipulations create different visual conditions within one animal, which gives an internal comparison between regions of the map. Both regions share the animal's age, housing, and prism history. Their difference reflects the visual condition alone. Every region was measured within the same owl, so no values were averaged across individuals.",
        "A location-specific difference within the same brain is especially informative when age, general housing conditions, and prismatic history are shared. That is the situation these paired regions provide. Regional contrasts within one owl are the variable of interest, because the other conditions are fixed. Local signals and global signals predict different spatial patterns of change.",
        "The study distinguishes the spatial pattern of instruction from the cellular implementation of learning. A topographic outcome leaves the learning algorithm unspecified. The regional measurements identify where change occurs, not which cellular rule produces it.",
    ], "Hyde & Knudsen (2001)", ["Hyde 2001"]),
    ins(21, "Drugs act through local ejection", [
        "Iontophoresis uses electrical current to eject charged drug molecules from a recording pipette. The drug acts locally, and its concentration at any single synapse goes unmeasured. The effect is tied to the neurons near the pipette. The ejection level in each trial sets the drug dose delivered. Recovery measurements confirmed that the drug effect was reversible.",
        "A drug effect that is equal across two response components can arise from a change in one of them. Equal blockade alone leaves open which component changed. Two components can contribute to one spike response at once. Spike output reflects both components together, so drug effects are judged at the level of the response.",
        "An adaptive flank is the side of a tuning curve toward the ITD values instructed by the prism displacement. The definition depends on the animal's experimental condition, not on the drug applied. Adaptive and nonadaptive flanks were measured on the same tuning curve. Learned responses in this study are identified by their ITD position.",
    ], "Feldman & Knudsen (1998)", ["Feldman 1998"]),
    ins(24, "Learned responses change their drug sensitivity", [
        "Expression is the ability of an established input to evoke a response during measurement. Induction is the process that originally changed the circuit. The two are different causal questions, and the drug result in this study addresses the first. The drug result reflects expression during the recording.",
        "The adaptive direction reverses with prism direction. Selectivity that follows the reversal carries more weight than selectivity seen for a single stimulus range. Opposite prism directions give a test of the adaptive side. Owls adapted in opposite directions show the same reversal of selectivity.",
        "Disinhibition is removal or reduction of inhibition. A weighted-average ITD summarizes the distribution of responses across timing values rather than identifying the strongest point alone. A distribution with a learned peak shifts the weighted value toward that peak. The weighted value reflects both peaks together.",
    ], "Feldman & Knudsen (1998)", ["Feldman 1998"]),
    ins(27, "Pharmacology tracks age and exposure together", [
        "Voltage dependence is one reason antagonist sensitivity fails to reveal receptor abundance directly. Mechanistic alternatives remain distinct from the measured drug effect. The drug effect is a measured quantity, while the mechanism behind it is an inference. Mechanisms such as AMPA or NMDA changes are candidate explanations.",
        "Spikes are the measured endpoint here, and interactions among excitatory currents can shift that endpoint away from the effect of a single blocker. Blocking one receptor class has consequences that extend beyond that class. The response measured in these recordings is the spike, not the receptor. Interactions in the cell determine how these currents combine.",
        "What matters for map expression is the relation between inhibitory tuning and the competing excitatory inputs. That relation is the quantity the drug experiments track. Inhibitory tuning can differ from excitatory tuning at the same site. Competing inputs set the weighting, and weighting sets the expressed timing preference.",
    ], "Feldman & Knudsen (1998)", ["Feldman 1998"]),
    ins(30, "Expressed responses depend on competing inputs", [
        "Normal and learned components are defined by stimulus timing and the anatomical reference. Their inhibitory and excitatory pharmacology may develop at different rates. The stimulus timing sets which values count as learned. The anatomical reference marks the normal timing that the learned values depart from.",
        "The asymmetric effect concerns which timing inputs are suppressed. It is not simply how much total firing increases when an inhibitory receptor is blocked. A functional bias can reverse without inhibition becoming globally stronger or weaker. Inhibition is a distinct input from the excitatory timing values it modifies.",
        "A tuning curve records neuronal response across stimulus values. Its preferred value and its width describe different properties of the response. A broad curve and a narrow curve can share the same preferred value. The curve's shape is informative beyond its peak. Shape and peak together describe the expressed response.",
    ], "Zheng & Knudsen (2001)", ["Zheng 2001"]),
    ins(33, "Inhibition shapes the expressed weighting", [
        "Sequential blockade measures excitation and inhibition within one local preparation. A surviving effect argues against a mechanism that depends on the blocked receptor. That logic was applied to the NMDA receptor in these recordings. A blocker of one receptor type is applied first, and the second blocker follows.",
        "Inhibitory bias at one site can exist with or without a matching NMDA bias. The bias is measured in expressed timing values, not in total firing. A site can show uniform AP-5 effects and still display an adaptive increase when inhibition is removed. At such a site, the disinhibition effect appears in the expressed timing values.",
        "The recordings follow no single inhibitory synapse across stages. Each stage is a sample of the circuit at one moment, not a tracked synapse. The bias changes as the map is reorganized, and the stages sample that change at a few points. Expressed weighting is a property of the whole inhibitory and excitatory balance.",
    ], "Zheng & Knudsen (2001)", ["Zheng 2001"]),
    ins(36, "Light microscopy shows presence, not strength", [
        "A bouton is a localized swelling along or at the end of an axon, commonly associated with a presynaptic release site. Its appearance is anatomical evidence rather than a measure of release efficacy. The swelling is a candidate site for transmitter release. Light microscopy identifies boutons by their shape along labeled axons.",
        "Spatially selective loss can sharpen a projection without moving every surviving axon. A cross-sectional comparison counts surviving axons at one moment rather than tracking each elimination event. Individual elimination events are not visible in a cross-sectional count. The count gives the net anatomical difference at each age.",
        "Anatomical comparisons need to distinguish rostralward and caudalward shifts instead of pooling them. Pooled data would hide the direction of the change. The direction of each shift determines which side of the projection gains labeling. Two directions of shift need two distinct comparisons. The regional pattern is the quantity these measures summarize.",
    ], "DeBello et al. (2001)", ["DeBello 2001"]),
    ins(39, "Bouton frequency differs from total boutons", [
        "Bouton frequency is the number of boutons per measured axonal length. It differs from the total number of boutons contributed by an entire projection field. A projection can gain contacts through longer axons or denser boutons. The two routes give different patterns of bouton labeling.",
        "Preservation predicts an adult retaining approximately the earlier anatomical amount. An increase beyond the juvenile reference requires an additional net contribution to the projection. The adaptive projection is measured against both references. Preservation and elaboration give different predictions for the same measurement.",
        "A presynaptic structure belongs to the transmitting side of a synapse. The receiving dendrite and its receptor currents require additional methods to characterize. Presynaptic labeling alone shows one side of the contact. The postsynaptic side of each contact is measured separately.",
    ], "DeBello et al. (2001)", ["DeBello 2001"]),
    ins(42, "Raster displays show response organization", [
        "A raster display marks individual spike times across repeated stimulus presentations, with each row representing one presentation. Population tuning combines the timing preferences of multiple recording sites. The display shows variability across trials as well as the typical timing.",
        "The predicted full shift for the 17-degree displacement was approximately 42.5 microseconds. The adult hunting response was substantial but remained incomplete. The predicted value is the benchmark against which the hunting shifts are judged. The predicted value is a reference, not a measured endpoint.",
        "Correlation between map change and strike performance constrains the functional interpretation, though a selective causal manipulation would still be needed. The strike performance is a behavioral outcome, not a neural measure. Its link to the map is a correlation across sessions.",
    ], "Bergan et al. (2005)", ["Bergan 2005"]),
]

spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(_body.body)} body slides rewritten, {len(inserts)} scaffold slides")
