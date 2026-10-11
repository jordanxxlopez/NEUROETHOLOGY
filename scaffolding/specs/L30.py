"""Scaffold spec for Lecture 30 (Drive deck Neuroethology_Lecture30_FA2026.pptx). Body rewrites are in body_L30.py."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L30 as _body  # noqa: E402
import L30_extend as _ext  # noqa: E402
import L30_extend2 as _ext2  # noqa: E402


def ins(after, title, paragraphs, citation, refs):
    notes = [title + "."] + [
        [f"Explanation {i + 1}.", *(p.split(". ", 1))] for i, p in enumerate(paragraphs)
    ]
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


inserts = [
    ins(3, "Tethered headings reveal sustained orientation", [
        "A fine wire attached to the dorsal thorax held each monarch in place while it rotated freely. A cylinder roughly 59 cm wide and 64 cm high limited its view to the sky overhead, so the sky was the visual reference available to the insect. Vertical airflow lifted the butterfly without supplying a horizontal wind direction.",
        "The system sampled heading every 200 ms, which recorded both sustained orientation and course changes within a single trial. Virtual trajectories were built from those headings by assuming a flight speed, so the distances shown are calculated rather than measured.",
        "Excluding landscape landmarks allowed solar orientation to be tested under controlled visual access, which isolates the sky as the reference. Because the record is continuous, each trial keeps changes in course as they occur.",
    ], "Mouritsen & Frost (2002)", ["Mouritsen 2002"]),
    ins(6, "Opposite clock shifts rotate headings oppositely", [
        "Mouritsen and Frost delayed the entraining 12-h light:12-h dark cycle by 6 h, creating the reverse of the advance tested earlier. The delayed group was tested in the same simulator as the autumn migrants, so the apparatus stayed constant while the light schedule changed.",
        "Delayed butterflies oriented near 335°, toward the northwest, a change of about 110° clockwise from the local-time mean of 225°. The advance had produced a counterclockwise change, so the two manipulations moved the heading in opposite directions.",
        "Unequal magnitudes between the two shifts reflect the observed solar geometry and the experimental conditions. Opposite shifts from opposite clock manipulations indicate a signed link between clock phase and compass direction.",
    ], "Mouritsen & Frost (2002)", ["Mouritsen 2002"]),
    ins(9, "UV-blocked light still sets emergence timing", [
        "Froy and colleagues reared monarch pupae under light–dark cycles with a filter that blocked UV, then recorded eclosion, the emergence of adults from the pupal case. Advancing the filtered schedule by 6 h moved the emergence peaks approximately 5.5 h, which shows that the schedule carried the timing signal.",
        "Emergence remained concentrated at one phase of the daily cycle in these pupae. The timing response occurred without ultraviolet illumination, so visible wavelengths were sufficient to set the daily emergence phase.",
        "The flight disruption caused by the UV filter in adults is a separate observation from the emergence result. Visible wavelengths can carry daily timing information in this preparation, so the wavelength that disrupts flight and the wavelength that sets the clock can differ.",
    ], "Froy et al. (2003)", ["Froy 2003"]),
    ins(12, "Polarizer rotation tested under restricted skylight", [
        "Sauman and colleagues fixed monarchs to a tether beneath a linear polarizing filter, which limited the skylight to an 80° field and excluded sight of the sun. Rotating the filter by 90° changed the electric-field orientation of the light available to the animal.",
        "Each trial used sequential 5-min records taken before rotation, after rotation, during UV interference below 397 nm, and after the UV filter was removed. Interference frequently produced circling and cut virtual progress by at least 70%.",
        "Removing the UV filter restored sustained directional flight, so the effect reversed with the treatment. Spectral interference also altered flight continuity, which mixes the loss of direction with changes in flight behavior.",
    ], "Sauman et al. (2005)", ["Sauman 2005"]),
    ins(15, "Emergence rhythm free-runs in constant darkness", [
        "Froy and colleagues entrained monarch pupae to a light–dark schedule and then exposed them to three conditions: continued cycling light, constant darkness and constant light. Adult emergence time was recorded in each condition.",
        "Eclosion clustered early in the light phase and remained rhythmic in constant darkness, which shows that the rhythm persisted once daily lights were removed. A 6-h shift in the prior light schedule altered the emergence phase.",
        "Continuous light disrupted the timing that darkness preserved, so light exposure changes the emergence pattern. Free-running rhythms proceed without daily entrainment, and emergence therefore measures an endogenous timing output.",
    ], "Froy et al. (2003)", ["Froy 2003"]),
    ins(18, "CRY1 knockdown blocks light-driven TIM decline", [
        "Zhu and colleagues used cultured monarch DpN1 cells and RNA interference to lower CRY1 expression. Control cells received interference directed against green fluorescent protein, which served as the reference treatment.",
        "Under the control treatment, TIM decreased during the light-exposure time course before PER and CRY2 decreased. The cry1 interference prevented this normal light-dependent decline of TIM, the TIMELESS clock protein.",
        "These protein measurements support CRY1-dependent light input to clock regulation. Brain labeling places CRY1 alongside PER in candidate clock cells, which connects the cell-culture result to the brain.",
    ], "Zhu et al. (2008)", ["Zhu 2008"]),
    ins(21, "CRY2 knockdown raises reporter activity", [
        "Zhu and colleagues reduced endogenous CRY2 in DpN1 cells with RNA interference and set the results against a control sequence. Protein measurements confirmed that the targeted regulator was depleted.",
        "CRY2 reduction increased reporter activity about threefold. Across a 24-h light–dark cycle, per RNA remained near its peak values after cry2 interference, instead of following the rise and fall seen in controls.",
        "The loss-of-function result matches the gain-of-function assay, in which added CRY2 reduced transcription. Together, the two tests show negative feedback, with clock-associated proteins restraining the transcription that produces them.",
    ], "Zhu et al. (2008)", ["Zhu 2008"]),
    ins(24, "CRY2 fibers in the central body vary daily", [
        "The central body is part of the insect central complex, a set of brain neuropils linked to orientation. Neuropils are regions dense with neuronal processes and synaptic connections, so they can carry signals between cell groups. Zhu and colleagues found CRY2-containing fibers in this region.",
        "The maximum CRY2 staining occurred near CT15, and the minimum occurred near CT9, both measured in constant darkness. Heinze and Reppert's synapsin labeling identifies the central-complex anatomy in which these fibers sit.",
        "A rhythmic protein signal in an orientation-associated region suggests a possible route from clock state to compass processing. Establishing that route depends on identifying the connected cells and manipulating their signal during compass recording.",
    ], "Zhu et al. (2008); Heinze & Reppert (2011)", ["Zhu 2008", "Heinze 2011"]),
    ins(27, "Antennal clock RNA rhythms persist in darkness", [
        "Merlin and colleagues measured clock-associated RNA in isolated monarch antennae across a light–dark cycle. The transcripts were per, tim and cry2, and cry1 was assessed alongside them. Quantitative PCR converts RNA to DNA so that abundance can be estimated for each sequence.",
        "Antennal per, tim and cry2 RNA varied across the cycle and continued to vary after transfer to constant darkness. Levels were lower near ZT6 than near ZT18, while cry1 RNA showed no such phase difference.",
        "A molecular clock program is present in the appendages needed for normal orientation. Rhythms that continue in darkness point to endogenous timing rather than a direct response to light onset, and they come from the antenna itself.",
    ], "Merlin et al. (2009)", ["Merlin 2009"]),
    ins(30, "Black antennal paint shifts the selected heading", [
        "Merlin and colleagues coated the antennae with black or clear enamel. Black paint blocked transmission across the tested 300–800 nm range, while clear paint kept transmission high and served as the control for the painting procedure. Both coatings left the appendage physically present.",
        "Black-painted butterflies chose an abnormal northward bearing near 344° on the normal schedule. Delayed black-painted animals lost group organization, with directions disorganized across the group rather than sharing one heading.",
        "Clear-painted animals kept a consistent heading and moved it after a 6-h delay, shifting from about 162° to 269°. The paint result connects antennal light access to time-compensated orientation.",
    ], "Merlin et al. (2009)", ["Merlin 2009"]),
    ins(33, "Removing a conflicting antenna restores bearing", [
        "Guerra and colleagues first flew migrants with one black-painted and one clear-painted antenna, which produced disorganized group headings. The black-painted appendage was then removed, and flight was tested again in the same animals.",
        "The previously disorganized animals regained a southwest group heading near 214°. Combining repeated-flight controls with first-flight removal controls gave a mean near 216°, which reduces the chance that simulator experience explains the recovery.",
        "Removing a conflicting timing source restored a consistent bearing, which supports coordinated input from both antennae. The effect depends on which source is removed, and the clear antenna stayed available throughout the intervention.",
    ], "Guerra et al. (2012)", ["Guerra 2012"]),
    ins(36, "Compass neurons prefer specific E-vector angles", [
        "Heinze and Reppert recorded identified compass neurons while presenting polarized 365-nm UV light from above. The E-vector rotated through 360° at 30° or 60° per second, so every polarization angle was presented during the recording.",
        "Action potentials, brief electrical spikes, occurred at different rates for different E-vector angles. The preferred and suppressed axes sat about 90° apart, and the response repeated after 180°, matching the axial symmetry of linear polarization.",
        "Neurons in this circuit are sensitive to the polarization axis under controlled stimulation. Behavioral masking addresses a different question, because it tests whether the input drives orientation during flight.",
    ], "Heinze & Reppert (2011)", ["Heinze 2011"]),
    ins(39, "Migrants show narrower green-light tuning", [
        "Nguyen and colleagues recorded tangential neurons from autumn migrants and from non-migratory monarchs. A green 530-nm light spot rotated around the animal at 30° elevation, and the angular range producing elevated spike rates was measured.",
        "Full width at half maximum gives the width of a tuning curve at half its peak response. Migrants averaged about 83°, and non-migrants averaged about 118°. Peak firing rates were broadly similar, so migrants differed mainly in how narrowly they selected direction.",
        "The narrower tuning is associated with migratory condition in these recordings. Wild migrants and commercially sourced non-migrants differed in origin and rearing, so the link between tuning and migration is an association between two groups.",
    ], "Nguyen et al. (2021); Heinze & Reppert (2011)", ["Nguyen 2021", "Heinze 2011"]),
    ins(42, "Cold exposure produces northward headings", [
        "Guerra and Reppert exposed fall migrants to 24 days of conditions resembling the overwintering environment, at 11°C during the light phase and 4°C during darkness. Both treatments included cold, but one gradually increased day length while the other kept a constant 12-h light:12-h dark cycle.",
        "Both cold-treated groups oriented near 358° after warming enough to fly. Warm-housed animals retained a southwest direction near 227°. The northward orientation appeared with or without the changing photoperiod.",
        "The 24-day treatment provides an effective exposure for inducing the reversal in these experiments. Cold therefore acts as an environmental trigger, while time-compensated sun orientation remains available after the switch.",
    ], "Guerra & Reppert (2013)", ["Guerra 2013"]),
]

for _k, _ps in _ext.EXTEND.items():
    for _p, _t in _ps.items():
        _body.body[_k][_p - 1] = _body.body[_k][_p - 1] + _t
for _ins in inserts:
    for _p, _t in _ext.INSERT_EXTEND.get(_ins["after"], {}).items():
        _ins["paragraphs"][_p - 1] = _ins["paragraphs"][_p - 1] + _t

for _k, _ps in _ext2.EXTRA.items():
    for _p, _t in _ps.items():
        _body.body[_k][_p - 1] = _body.body[_k][_p - 1] + _t
for _ins in inserts:
    for _p, _t in _ext2.INSERT_EXTRA.get(_ins["after"], {}).items():
        _ins["paragraphs"][_p - 1] = _ins["paragraphs"][_p - 1] + _t

for _ins in inserts:
    _ins["notes"] = [_ins["title"] + "."] + [
        [f"Explanation {i + 1}.", *(q.split(". ", 1))] for i, q in enumerate(_ins["paragraphs"])
    ] + [["Source.", f"The figure and the measurements come from {_ins['citation']}.", "Each statement is tied to the recordings or observations of that study."]]

spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(_body.body)} body slides rewritten, {len(inserts)} scaffold slides")
