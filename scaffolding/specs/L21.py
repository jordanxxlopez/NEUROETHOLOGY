"""Scaffold spec for Lecture 21 (Drive deck Neuroethology_Lecture21_FA2026.pptx). Body rewrites are in body_L21.py
Inserts follow the L39 pattern: notes are derived from the paragraphs."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L21 as _body  # noqa: E402
import L21_insert_extend as _iext  # noqa: E402


def ins(after, title, paragraphs, citation, refs):
    notes = [title + "."] + [
        [f"Explanation {i + 1}.", *(p.split(". ", 1))] for i, p in enumerate(paragraphs)
    ] + [["Source.", f"The figure and the measurements come from {citation}.", "Each statement is tied to the recordings or observations of that study."]]
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


inserts = [
    ins(3, "Matched simulations isolate the object's contribution", [
        "Conductivity describes how readily a material carries electric current, and an object's conductivity sets how strongly it distorts the field around it. Simulated scenes with and without the object were otherwise matched, so the difference between them reflects the object itself rather than other scene differences. The reconstruction keeps that difference as the signal of interest for each frame.",
        "The pattern also depends on where the fish sits relative to the object. Each receptor samples a different part of the perturbation as the fish moves, so the same metal cube can generate different electric images at different positions. Each frame records the object's influence at every receptor location, and position is encoded alongside the object.",
        "Because the reconstruction was built from real approaches, each image in the series corresponds to one moment in one fish's inspection. The estimates inherit the timing of the fish's own movement. Each reconstructed frame is a model output, not a snapshot taken by a camera.",
    ], "Hofmann et al. (2017)", ["Hofmann 2017"]),
    ins(6, "Image intensity and diameter both shift with distance", [
        "A rule based on image intensity fails here because intensity falls as an object moves away, while the rewarded physical size stays the same. The distance manipulation separated intensity from the real cube size in each trial, so a fixed intensity criterion could not match the reward across every combination of distances.",
        "Image diameter behaved in the same way, and its measured width grew with each increase in distance, so the image changed while the reward did not. Width fails as a stand-in for size, and the fish's choices followed the physical cube instead of the image it produced.",
        "Darkness controls showed that the size discrimination survived without visual input, which suggests an electrosensory route for the learned choice. Cubes were moved to new distances in separate tests, while each cube's rewarded size stayed fixed across them.",
    ], "von der Emde et al. (2010)", ["von der Emde 2010"]),
    ins(9, "Discharge timing shapes each approach sample", [
        "Spatial sampling density is the number of electric discharges per distance traveled. It depends jointly on emission timing and swimming speed, so a fish that swims faster collects fewer discharges per centimeter unless it also raises its discharge rate. Density reflects two behaviors at once, the emission pattern and the movement.",
        "Each electric sample reaches the skin while the object's image is changing, so each discharge carries a different spatial context. Hofmann and colleagues paired the discharge record with the approach trajectory, which let each sample be matched to the fish's position at that moment.",
        "Thrust and discharge activity moved in opposite directions across the approach, and the sampling density rose as the fish closed in. Straighter postures and more direct alignment with the object accompanied that rise in density, so the geometry of inspection and the sample sequence changed together.",
    ], "Hofmann et al. (2017)", ["Hofmann 2017"]),
    ins(12, "Normalization removes the amplitude scale", [
        "A relative gradient divides the rate of amplitude change by the current amplitude, so its output depends on the shape of the change rather than on absolute size. For that reason the relative-gradient curves overlapped across cube sizes that produced very different absolute amplitudes, which is the central result of this comparison.",
        "Adapted emission and movement produced more samples near each cube than unadapted patterns did, so the cue depends on the animal's own sampling pattern in every trial. Adapted emission changes how many measurements feed the gradient at each distance, and that change is built into the reconstruction.",
        "The gradient cue was built from reconstructed frames and tested inside the modeled input. The reconstruction supplies the candidate signal, while the neurons that would use that signal were not part of the model.",
    ], "Hofmann et al. (2017)", ["Hofmann 2017"]),
    ins(15, "Dynamic cues reach threshold farther away", [
        "The detection criterion defines when an object's information first rises above the variability of the reference condition. Under that criterion, the dynamic cue crossed threshold at about 6 cm, while the static image measure crossed it at about 3 cm, so the dynamic cue carried information to a greater distance.",
        "The dynamic measure also resolved distance more finely at longer distances in the modeled data. That resolution describes what the reconstructed cue can separate, which is an analysis result rather than a value recorded from the fish, and it is computed from the same reconstructed approaches.",
        "The roughly 4 cm recognition range in the choice tasks is a separate measure of identification. Shape discrimination and distance estimation require different kinds of information, so the two thresholds can differ in value even when both come from the same object.",
    ], "Hofmann et al. (2017)", ["Hofmann 2017"]),
    ins(18, "Electrolocation alone reached high accuracy", [
        "Each group was defined by the senses it could use during testing, and each group was tested under its own condition. Every group reached at least 84% correct, so electrolocation by itself supported a high level of discrimination in this near-field task.",
        "The gain from combining the senses was measured with the objects placed close to the gates, at about 1 cm, where electric information is strongest for these fish. Both sensory channels were available together in the combined condition, so the difference reflects the information each channel supplied.",
        "The rewarded-object choice stayed identical across those conditions, so accuracy differences reflect the sensory information available to each group. Final accuracy and the number of training days are separate outcomes, one describing the stable endpoint and the other the speed of learning.",
    ], "Schumacher et al. (2017)", ["Schumacher 2017"]),
    ins(21, "Latency adds timing to amplitude information", [
        "The first spike of a mormyromast afferent appears at a latency measured from the electric stimulus. A larger amplitude shortens that latency, so the spike's timing carries amplitude information that a spike count alone lacks.",
        "The brief pulses were chosen to resemble an EOD, which allowed amplitude to vary while the sampling interval was held apart from it. Each recorded response was tied to a controlled pulse, and its latency could be read directly from the recording.",
        "Timing information is available within a single spike, before the count of a whole burst is known. The latency code is one way the afferent represents local electric contrast, and it operates at the level of a single fiber rather than a population.",
    ], "Sawtell et al. (2006)", ["Sawtell 2006"]),
    ins(24, "Natural interval sequences change latency", [
        "The replay used natural EOD interval sequences, so each pulse in the sequence carried its own preceding interval. Latency changed from pulse to pulse as those intervals varied, a pattern that a fixed-rate stimulus lacks entirely.",
        "Amplitude modulation was delivered as a controlled comparison input, so the replayed intervals and the amplitude changes were recorded in the same afferents. This arrangement isolated how the interval sequence shifted the response while the amplitude input was held constant.",
        "The same local amplitude gave a different latency depending on the sequence that preceded it, which places sampling history inside the afferent code. The afferent carries information about the timing of active sampling itself, alongside the electric contrast.",
    ], "Sawtell et al. (2006)", ["Sawtell 2006"]),
    ins(27, "Interval-dependent gain improves latency fits", [
        "Interval-dependent sensitivity was added as a term that changes the amplitude gain according to previous intervals. The model with this term predicted measured latencies better than a model that ignored interval history, which is the main result of the fitting exercise.",
        "The fit used the same recorded afferent responses, so the improvement came from representing stimulus history rather than from new data. Prediction failures were most visible when natural intervals were combined with slowly correlated amplitudes, which is the condition the model had to reproduce.",
        "The fitted model names the variables that govern the history dependence of the latency code. A model of this kind can make predictions for responses to interval sequences that were not part of the original fit, so it extends beyond the recorded examples.",
    ], "Sawtell et al. (2006)", ["Sawtell 2006"]),
    ins(30, "Excitation in the ELL uses two glutamate receptors", [
        "Glutamate-gated ion channels of the AMPA and NMDA types carry the excitatory current evoked by parallel-fiber input. Their pharmacology was examined separately in the same slice preparation, so each receptor type could be tested on its own.",
        "Removing magnesium increased the NMDA component of the response, which shows that magnesium blocks the NMDA channel at normal resting voltage. Washing out the antagonists restored the response, so the drug effect was reversible rather than a sign of tissue damage.",
        "The two receptor types respond to the same transmitter, so their relative contributions depend on the state of the postsynaptic membrane at the moment of input. The slice results name the receptor types that contribute in this preparation.",
    ], "Grant et al. (1998)", ["Grant 1998"]),
    ins(33, "Facilitation depends on the spacing of two pulses", [
        "Paired-pulse facilitation was measured as the ratio of the second EPSP to the first, using pulse pairs spaced across tens to hundreds of milliseconds. Facilitation was strongest at the shortest spacings tested, which means the effect fades as the gap between pulses lengthens.",
        "Independent stimulation sites separated repeated stimulation of one fiber population from activation of a different population. Each site produced its own pair of responses, which made the source of facilitation identifiable in the recordings.",
        "Short-term facilitation enlarges the response of a synapse that was used moments earlier, so the next input has a larger effect on the cell. Long-lasting changes need repeated spike pairings, a separate process from the short-term change measured in these recordings.",
    ], "Grant et al. (1998)", ["Grant 1998"]),
    ins(36, "Efferent cells respond to both input layers", [
        "Output neurons of two kinds, large ganglion cells and fusiform cells, were recorded in these slices alongside the medium ganglion interneurons. Their firing to current injection was set against that of the interneurons, which provides a second cell type for comparison.",
        "Excitatory and inhibitory influences reached these output cells, and the balance between them depended on the stimulated pathway. A fusiform cell has an elongated cell body, which distinguishes its morphology from that of the Purkinje-like interneuron in the same structure.",
        "The output cells form a separate route out of the ELL, while the medium ganglion interneuron contributes to the local circuit. Local responses are one stage of the processing that precedes the output neurons in each slice.",
    ], "Grant et al. (1998)", ["Grant 1998"]),
    ins(39, "B spikes and N spikes are separate events", [
        "Broad dendritic events, called B spikes, are tied to plasticity at parallel-fiber synapses. Both event classes arise in one medium ganglion cell, which allows their timing to be compared directly within a single recording.",
        "B-spike timing shifted across the phases of the electric-organ command cycle, and specific N-spike patterns were found near each B spike. These associations were made within the same cell during the same recording sessions, so the two event types were observed together.",
        "Keeping the two event types apart matters because they reach different targets within one cell. A broad spike regulates later synaptic change, while a narrow spike carries the cell's immediate signal outward to the rest of the circuit.",
    ], "Sawtell et al. (2007)", ["Sawtell 2007"]),
    ins(42, "A transient rise follows stimulus removal", [
        "The recordings captured the state that the circuit entered during repeated electrosensory stimulation, and they tracked that state into the command cycles that followed. Switching the stimulus off produced a transient increase in early B-spike activity.",
        "That rise appeared although the command signal served as the timing reference throughout. Stimulus history shaped when and how often these events occurred, not merely whether they occurred in a given cycle.",
        "The transient response is a candidate learned prediction, and additional inhibition and pairing experiments are needed to identify the mechanism behind it. The observed firing pattern is the measured result, while the mechanism is an interpretation of that result.",
    ], "Sawtell et al. (2007)", ["Sawtell 2007"]),
]

for _ins in inserts:
    for _p, _t in _iext.INSERT_EXTEND.get(_ins["after"], {}).items():
        _ins["paragraphs"][_p - 1] = _ins["paragraphs"][_p - 1] + " " + _t
    _ins["notes"] = [_ins["title"] + "."] + [
        [f"Explanation {i + 1}.", *(q.split(". ", 1))] for i, q in enumerate(_ins["paragraphs"])
    ] + [["Source.", f"The figure and the measurements come from {_ins['citation']}.", "Each statement is tied to the recordings or observations of that study."]]


body_slides = _body.body

spec = {"third_paragraph": {}, "inserts": inserts, "body": body_slides}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(body_slides)} body slides rewritten, {len(inserts)} scaffold slides")
