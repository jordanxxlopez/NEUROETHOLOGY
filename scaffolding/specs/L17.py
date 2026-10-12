"""Scaffold spec for Lecture 17 (Drive deck Neuroethology_Lecture17_FA2026_NEW.pptx). Body rewrites are in body_L17.py."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L17 as _body  # noqa: E402
import L17_insert_extend as _ext  # noqa: E402


def ins(after, title, paragraphs, citation, refs):
    notes = [title + "."] + [
        [f"Explanation {i + 1}.", *(p.split(". ", 1))] for i, p in enumerate(paragraphs)
    ] + [["Source.", f"The figure and the measurements come from {citation}.", "Each statement comes from that study's recordings or observations."]]
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


inserts = [
    ins(3, "Recordings isolate target echoes", [
        "Simmons recorded the outgoing call and the returning echo from a target at 30 cm. The echo arrived after the call, not at the same moment as the sound leaving the bat. Sound from the apparatus also appeared in the recording. The investigator separated target echoes from that other returning sound before measuring the delay.",
        "In the experimental conditions, the echo from that target returned about 1.7 ms after the call. Electronic delay channels could change this interval directly. The loudspeakers kept fixed physical positions while the timing changed. Direct control over echo timing gave the experimenter a clean test of the ranging cue, with no physical movement required.",
        "Simmons recorded outgoing sounds and echoes while bats discriminated target distance. Each echo in the recording can be matched to the call that produced it. The recordings thus show the timing that bats had available during the task.",
    ], "Simmons (1973)", ["Simmons 1973"]),
    ins(6, "Choices and prediction are separate curves", [
        "The measured curve shows the bats' actual choices at each difference between two targets. The other curve is a prediction that Simmons published from the recorded signal. The other curve comes from calculation, not from behavior. Each point on the measured curve counts correct choices at one difference. Both curves appear on one set of axes.",
        "A matched receiver is a proposed interpretation of that agreement. It is not a demonstrated neural mechanism. Its role is to predict the curves, not to name neurons. Neurons that perform the matching were not identified in this study. Simmons described the receiver as a functional hypothesis.",
        "Simmons plotted both curves at 30 cm, the same distance used for the measured choices. The prediction used a signal that the bats had produced. The result sets a behavioral measure beside a signal-based prediction, not a single cell's response.",
    ], "Simmons (1973)", ["Simmons 1973"]),
    ins(9, "Arrival-time differences of about 1 cm", [
        "The electronic-delay experiment could discriminate arrival-time differences corresponding to about 1 cm of range. Simmons set the simulated range at 30 cm as the reference distance for that comparison. Both conditions used the same bats and a comparable choice task. The result is reported as a difference in arrival time, not in position.",
        "The plot keeps both the physical distance scale and the electronic delay scale. Spectral, directional and intensity cues were controlled, so timing was the remaining cue under test. Those controlled variables matter in natural scenes, which carry all of the cues together. The experiment isolated one cue on purpose.",
        "Physical-range and electronic-delay discrimination were both measured at a 30 cm reference range. The electronic curve matched the physical one closely. The mode of delivery was the one difference between the two conditions.",
    ], "Simmons (1973)", ["Simmons 1973"]),
    ins(12, "Echo spacing in the cascade", [
        "After the first echo, the later echo intervals were 2.1, 3.5 and 6.8 ms. The first echo moved in 1-ms steps across a span of about 6 ms. Each waveform in the series keeps this fixed cascade pattern. The stimuli were built by the experimenters, not captured from a flying bat.",
        "The broadcast lasted 2.5 ms in every stimulus. Its FM1 part swept from 50 to 20 kHz, and its FM2 part from 100 to 40 kHz. The four echoes shared that spectral content. The echo amplitudes were set separately for each of the four echoes.",
        "Each plotted waveform begins with a broadcast and then contains four echoes. The series is a controlled acoustic approximation of approaching a set of targets. The waveforms show the stimulus, not an animal's behavior. Each waveform's first echo arrives at a different delay in the series.",
    ], "Simmons et al. (2024)", ["Simmons 2024"]),
    ins(15, "Jitter rises as the broadcast weakens", [
        "The cochlear-nucleus broadcast peak had mean jitter values of 32, 44 and 67 μs at −30, −40 and −50 dB attenuation. The three settings differ in how loud the stimulus was. Greater attenuation makes the stimulus weaker. Timing was least precise at the quietest setting.",
        "A response can arrive several milliseconds after a sound and still repeat within tens of microseconds. Mean delay and repeatability are separate measures of the same response. Latency and jitter answer different questions about one event. The broadcast peak was late, but its repeats were tight.",
        "Across the delays, the jitter changed only slightly. That stability held within each sound level. Sound level, not echo delay, set the size of the jitter. The seven delays covered the full cascade used in the study.",
    ], "Simmons et al. (2024)", ["Simmons 2024"]),
    ins(18, "Later responses can stay precise", [
        "The midbrain broadcast latencies were 6.7, 7.0 and 7.5 ms across the three settings. Those latencies are longer than the cochlear-nucleus latencies at the same settings. The added latency is the time needed before a midbrain response occurs. Midbrain responses arrive later, after more processing has occurred.",
        "The consistency of the waveform across repetitions is a separate property. Extra processing time by itself says little about precision. This property was measured separately from the latency. Early midbrain peaks stayed closely aligned from one repetition to the next.",
        "The midbrain data came from the same animals as the cochlear-nucleus data. Identical stimuli and timing measures were applied at both sites. This design isolates the midbrain step from differences in animals or stimuli. Each site produced its own latency and its own jitter values.",
    ], "Simmons et al. (2024)", ["Simmons 2024"]),
    ins(21, "The decoder remains untested", [
        "The recordings were digitized at 20 kHz. That rate places important constraints on very small timing estimates. Sampling at that rate sets how precisely a latency can be measured. Restricted recording sites add a second limit on interpretation.",
        "The behavioral and neural values come from different tasks and preparations. The brainstem data explain only part of one-microsecond perception, because its variability stayed larger. The behavioral value comes from specialized tasks. The neural value comes from anesthetized recordings.",
        "The authors identified precisely timed population signals as candidate inputs to a range readout. The experiment never directly identified such a decoder. Precisely timed population signals are one proposed input to that computation.",
    ], "Simmons et al. (2024)", ["Simmons 2024"]),
    ins(24, "Two-tone timing reveals inhibitory arrival", [
        "The two-tone experiment reveals suppression that recordings of isolated tones alone would miss. A sideband can suppress a response without producing a visible response when presented by itself. That is why the paired-tone test is needed. The inhibitory tone outlasted the excitatory one in these pairs.",
        "The method infers when inhibition becomes effective at the recorded neuron. Experiments that vary acoustic timing reveal the functional timing of inhibition. The measured quantity is functional timing, not a direct recording of synaptic current. Each tone interval in the series gave one data point.",
        "The 5-ms excitatory tone was shorter than the 20-ms inhibitory tone. Its onset could fall before, during or after the excitatory tone as the interval varied. Each interval produced its own level of suppression. The response was measured as the drop in excitatory firing.",
    ], "Williams & Fuzessery (2011)", ["Williams 2011"]),
    ins(27, "Two blockers, one neuron", [
        "The three conditions were obtained from the same neuron. Differences between the two blockers could not be explained by sampling different neurons. Baseline, gabazine and strychnine conditions were all measured in that one cell. The design kept neuron identity constant across conditions, which makes the drug effects directly comparable.",
        "A direction preference that remains after one drug shows that the blocked pathway is not essential by itself. Other inputs or inherited tuning can keep the preference in place. Gabazine and strychnine were applied separately to the same neuron. The result describes one pathway at a time.",
        "A receptor class by itself is not enough to fix that outcome. Each neuron's arrangement of inputs sets its own outcome. Two neurons with the same receptor class can respond differently to the same sweep. Each drug condition used the same sweeps, and the outcome was read from those responses.",
    ], "Williams & Fuzessery (2011)", ["Williams 2011"]),
    ins(30, "A 3.5-ms shift flips the preference", [
        "Negative and positive arrival values in the two-tone test give the relative order of two inputs. In the published example, the inhibitory input shifted by 3.5 ms in that order. Before the shift, inhibition arrived first. Those values came from the two-tone measurements of the same neuron.",
        "Measurable suppression still existed after the shift. The timing of that suppression had changed, though its size had not. Late inhibition could not stop an early excitatory response. The neuron responded to upward sweeps that earlier inhibition had blocked.",
        "Selectivity in this example depended on the order of inputs more than on their size. Changing when the suppression arrives changed the preference. Its strength was measurable at the end of the shift.",
    ], "Williams & Fuzessery (2011)", ["Williams 2011"]),
    ins(33, "Glycine and sideband suppression agree", [
        "The pharmacological result agrees with the earlier spectral-removal test. Two manipulations gave matching results on rate tuning. Removing high frequencies from the stimulus and blocking glycine receptors both produced a similar change. Each manipulation tested the same sideband from a different side.",
        "The other manipulation removes a local receptor role in the suppression. Together, the two results implicate the same sideband. Each test isolated a different step of the suppression. Agreement between separate methods strengthens the case for a sideband effect.",
        "The gabazine examples kept their high-frequency suppression and fast-pass preference. Gabazine left this sideband intact. In the strychnine example, the sideband was eliminated, so the rate tuning changed with it. The same pattern held for the rate tuning, which fell with the sideband.",
    ], "Williams & Fuzessery (2011)", ["Williams 2011"]),
    ins(36, "Two glints and a Y-shaped platform", [
        "The bat sat on the Y platform and chose between two targets. Microphones captured its calls, which electronic delay channels then returned from loudspeakers. The bat was rewarded for choosing the two-glint target. Its probe timing spanned the region around both rewarded delays.",
        "The probe contained one glint, so it carried less structure than the target. Electronic filters allowed the two harmonics to be manipulated independently. Each manipulation left the rest of the procedure the same. The probe was unrewarded, so choosing it counted as an error. Harmonic balance was the factor under test.",
        "Electronic construction allowed the experimenters to set glint delays exactly. No natural insect echo was used in the study. Choices were counted for each probe delay. The rewarded target kept the same two glints throughout, with a 300-μs spacing.",
    ], "Bates et al. (2011)", ["Bates 2011"]),
    ins(39, "Advance and recovery differ by glint", [
        "The advance was applied to FM2, the harmonic that had been weakened. Its size was checked against the timing shift predicted for a 1.5-dB reduction. The predicted shift came from the proposed amplitude-latency trading.",
        "The timing measurements used to infer these responses were recorded earlier. The behavioral test changed the harmonic balance of one probe. Masking returned when the advance was applied. Masking was measured as incorrect choices.",
        "This experiment recorded choices, not the neural responses that the timing shift describes. Neural timing was inferred from earlier data, while this study measured choices. The result shows how harmonic timing bears on the trade-off between delay precision and clutter resistance. Each prediction in this series came from timing data, not from neural recordings. The advance tested that prediction on the choices of the bats.",
    ], "Bates et al. (2011)", ["Bates 2011"]),
    ins(42, "Hits, captures and attempts differ", [
        "The behavioral categories separate a failure to attempt from an attempted approach that missed or was aborted. Each category marks a different step of the interception. Counting them apart shows where clutter had its effect. Hits and captures are one outcome, while attempts are another.",
        "A decline in the combined measure may not come from failed detection alone. An attempt can fail after detection has occurred. Some approaches end in a miss or an abort instead of a capture. Each of those outcomes is counted in a separate category. Attempts and captures respond to clutter in different ways.",
        "The open-room condition gave the baseline for these categories. Near the vegetation, echoes from the plant arrived alongside the echo from the insect. The categories show whether the bat failed to try or failed after trying.",
    ], "Moss et al. (2006)", ["Moss 2006"]),
]

for _ins in inserts:
    for _p, _t in _ext.INSERT_EXTEND.get(_ins["after"], {}).items():
        _ins["paragraphs"][_p - 1] = _ins["paragraphs"][_p - 1] + _t

for _ins in inserts:
    _ins["notes"] = [_ins["title"] + "."] + [
        [f"Explanation {i + 1}.", *(q.split(". ", 1))] for i, q in enumerate(_ins["paragraphs"])
    ] + [["Source.", f"The figure and the measurements come from {_ins['citation']}.", "Each statement comes from that study's recordings or observations."]]

spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(_body.body)} body slides rewritten, {len(inserts)} scaffold slides")
