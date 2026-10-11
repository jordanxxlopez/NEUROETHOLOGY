"""Scaffold spec for Lecture 39 (Drive deck Neuroethology_Lecture39_FA2026.pptx). Body rewrites are in body_L39.py."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L39 as _body  # noqa: E402
import L39_extend as _ext  # noqa: E402


def ins(after, title, paragraphs, citation, refs):
    notes = [title + "."] + [
        [f"Explanation {i + 1}.", *(p.split(". ", 1))] for i, p in enumerate(paragraphs)
    ]
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


inserts = [
    ins(3, "Prolactin feeding depends on brood experience", [
        "Lehrman's prolactin protocol delivered 450 international units over 7 days, after which a squab was presented to each bird. The design compared treated birds with controls and grouped the birds by whether they had reared young before. Each parent's feeding was recorded against its own history.",
        "Experienced parents usually began feeding once prolactin had been given. Inexperienced birds failed to feed under the same sequence, although they responded physiologically to the hormone. The behavioral outcome therefore depended on the bird's history as well as the hormone.",
        "The crop's proliferating epithelium is the tissue that supplies milk, and it responds in the periphery. A physiological change in the crop therefore accompanies the hormone treatment, while the feeding decision depends on the bird's experience.",
    ], "Lehrman (1955)", ["Lehrman 1955"]),
    ins(6, "Female nest-cooing marks the nesting phase", [
        "Female nest-cooing is a vocal display given at the nest site. Females join males in this display and may continue alone after the male leaves to gather material. Daily observations separated these vocalizations from bow-cooing and from physical construction.",
        "Cheng described an abrupt end to female cooing after the second egg. That change marks the transition from nest building toward incubation, so the vocal record tracks the reproductive stage of the pair.",
        "Records of when cooing happens establish the timing of the signal. Playback and hormone manipulations then test the physiological and social effects of cooing within the same pairs.",
    ], "Martinez-Vargas & Erickson (1973)", ["Martinez-Vargas 1973"]),
    ins(9, "Estrogen and progesterone restore nest building", [
        "Cheng and Silver used reproductively experienced females after ovariectomy to reduce endogenous ovarian hormone input. They compared estradiol benzoate, progesterone, both steroids in a timed regimen, and sesame oil, with untreated males as partners.",
        "Estradiol benzoate was given on courtship days 4–10, and progesterone was added on days 8 and 10 in the combined condition. The doses were 50 micrograms of estradiol benzoate and 100 micrograms of progesterone, timed to follow estrogen exposure.",
        "The combined regimen produced the strongest nest-building response. Its timing shows that the order of the two signals matters for construction, and the schedule defines that order.",
    ], "Cheng & Silver (1975)", ["Cheng 1975"]),
    ins(12, "Construction requires more than picking up material", [
        "Cheng and Silver separated picking up and dropping nest material, carrying it to a site, and tucking it into the nest bowl. These measures distinguish interaction with an available object from the coordinated construction needed for a functional nest.",
        "Females given the combined regimen more reliably performed the later construction actions than females given either hormone alone or oil. Records of untreated males allowed each partner's contribution to be measured separately.",
        "On days 8 and 10, pairs lacking completed nests received an experimenter-built nest. Tucking material into that nest therefore involved rearranging an existing structure rather than constructing a new one.",
    ], "Cheng & Silver (1975)", ["Cheng 1975"]),
    ins(15, "Acoustic feedback restores follicular growth", [
        "Cheng recorded female nest-coos before muting and played those calls back during pairing. Auditory input was restored while normal vocal sound production stayed impaired, which isolates hearing from vocal output.",
        "The diameter of the same dominant ovarian follicle was measured before and after the playback period. The initial diameters were 4–5 millimeters across treatment conditions, so each change is measured from a common starting point.",
        "Own-call playback produced substantially more growth than male-call playback. The rescue supports an auditory contribution from the female's own display, and the neural circuit carrying that signal is the link still to be identified.",
    ], "Cheng (1986)", ["Cheng 1986"]),
    ins(18, "Hearing and bodily feedback are distinct inputs", [
        "Cheng distinguished hearing a nest-coo from proprioceptive feedback, which is sensory information from performing the movements of a vocal display. Playback restored the auditory stimulus while the muted females' sound production stayed impaired.",
        "Playback can also provoke attempted vocal movements and their bodily signals. Auditory rescue therefore engages one route, and the motor and sensory consequences of calling form a separate route.",
        "Courtship promotes female behavior, and that behavior stimulates the female herself. This reciprocal link makes the reproductive sequence a loop, with follicular growth as the measured endpoint.",
    ], "Cheng (1986)", ["Cheng 1986"]),
    ins(21, "Hormones promote nest activity while copulation stays rare", [
        "Liley's estrogen and combined estrogen–progesterone treatments supported female soliciting and nest-building activity. Nest-oriented activity was greatest under long days, while begging and sexual crouching stayed infrequent in the hormone-treated birds.",
        "The treatment lasted 15 days and was combined with daily access to an active male. Each reproductive action was recorded separately, so the results describe specific behaviors rather than a single judgment of breeding condition.",
        "Hormonal facilitation is behavior-specific. A treatment can promote nest-directed activity while the full sequence of mating and egg laying remains infrequent, and this pattern was observed in intact females.",
    ], "Liley (1976)", ["Liley 1976"]),
    ins(24, "Volume changes call for cellular measures", [
        "Neural plasticity is a change in nervous-system structure or function with state or experience. Nottebohm's measurements established seasonal variation in song-nucleus volume, and that volume combines neurons, their processes and other tissue components.",
        "A seasonal increase can reflect cell size, cell density or cell number. Histology distinguishes these measures, and recordings or behavioral assays address the consequences for vocal output.",
        "Tramontin and colleagues measured these cellular attributes in white-crowned sparrows exposed to controlled breeding-like conditions. Their results supply the cellular detail that the canary volume data lacked.",
    ], "Nottebohm (1981); Tramontin et al. (2000)", ["Nottebohm 1981", "Tramontin 2000"]),
    ins(27, "HVC expands before its targets", [
        "Tramontin and colleagues measured the volume of HVC, RA and Area X after the combined long-day and testosterone intervention. HVC reached about 94 percent of its eventual breeding-like size within 7 days, while its targets grew more slowly.",
        "RA and Area X reached their larger condition at the 20-day measurement, after HVC had already expanded. The order of these changes is the first evidence for a sequence of anatomical responses.",
        "The nuclei were measured across one defined time course, so the order of growth is a result of the treatment. Manipulating HVC or its projections would test whether this transsynaptic sequence operates.",
    ], "Tramontin et al. (2000)", ["Tramontin 2000"]),
    ins(30, "RA grows through larger tissue volume", [
        "RA grew more slowly than HVC after breeding-like stimulation. Its neurons enlarged early, and the later increase in nucleus volume came with a drop in neuron density rather than a rise in total neuron number.",
        "By day 20, the same general neuronal population occupied a larger volume of tissue. HVC differed, because substantial population growth contributed to its enlargement within the first 7 days.",
        "A lower density fits more space taken up by neuronal processes or other tissue components. The result identifies different cellular signatures of seasonal growth in two connected song nuclei.",
    ], "Tramontin et al. (2000)", ["Tramontin 2000"]),
    ins(33, "Song duration and consistency are separate measures", [
        "A spectrogram displays sound frequency over time, so individual song components can be measured. Tramontin and colleagues divided the white-crowned sparrow song into whistle, warble and buzz portions, using the published 2 kHz and 0.5 s calibration bars.",
        "Mean song duration was 1.80 seconds after 7 days of breeding-like stimulation and 1.84 seconds after 20 days. Whistle duration stayed close to 0.51 and 0.52 seconds across the two time points.",
        "Average duration and repeat-to-repeat consistency describe different properties of the vocal pattern. The average gives the central timing, while variation across repeated songs gives the consistency.",
    ], "Tramontin et al. (2000)", ["Tramontin 2000"]),
    ins(36, "Oxytocin accelerates pup retrieval in females", [
        "Marlin and colleagues tested oxytocin's central behavioral effects in female mice, a mammalian system that clarifies how the hormone acts. Oxytocin is a neuropeptide made by hypothalamic neurons, including those in the paraventricular nucleus, or PVN.",
        "Initially inexperienced virgin females were housed with a mother and her pups. Systemic oxytocin, or optical stimulation of PVN oxytocin neurons, sped retrieval of isolated pups, and many females began within 12 hours of co-housing.",
        "Saline-treated females needed longer experience before retrieving. Oxytocin therefore changed how quickly a social setting produced the response, which makes it a regulator of when experience becomes behavior.",
    ], "Marlin et al. (2015)", ["Marlin 2015"]),
    ins(39, "Oxytocin receptors sit on inhibitory interneurons", [
        "Interneurons are local neurons that influence neighboring cells within a circuit. Marlin and colleagues identified oxytocin receptors on inhibitory cortical interneurons marked by parvalbumin or somatostatin.",
        "About 30–40 percent of the labeled parvalbumin-positive and somatostatin-positive populations expressed oxytocin receptors. Hormone sensitivity therefore reached cells positioned to regulate local inhibition, not only excitatory output neurons.",
        "Oxytocin's effect on inhibition is a candidate route to control of local circuits. Synaptic recordings show how inhibition changed during hormone exposure and learning-related stimulation.",
    ], "Marlin et al. (2015)", ["Marlin 2015"]),
    ins(42, "Oxytocin acts most strongly on acquisition", [
        "Local oxytocin delivery to the left auditory cortex accelerated retrieval in inexperienced females. Optical stimulation of oxytocin axons in the same region produced a similar acceleration, which links a localized input to acquisition.",
        "Oxytocin-receptor antagonists infused into the left cortex left retrieval largely intact once the behavior was established. An antagonist blocks receptor activation, so it tests ongoing signaling apart from earlier exposure.",
        "Acquisition and performance therefore have different experimental dependencies. The result fits lasting circuit changes after oxytocin-assisted experience, which the established behavior shows when receptor signaling is blocked.",
    ], "Marlin et al. (2015)", ["Marlin 2015"]),
]

for _k, _ps in _ext.EXTEND.items():
    for _p, _t in _ps.items():
        _body.body[_k][_p - 1] = _body.body[_k][_p - 1] + _t
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
