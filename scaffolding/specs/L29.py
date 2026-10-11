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
        "The waggle-run angle is measured relative to vertical on the comb, and vertical stands in for the sun inside the dark hive. Dong and colleagues recorded these angles on the crowded, uneven comb surface. A single dance contains repeated waggle runs, and each run carries its own angle, so the dance produces a distribution of angles rather than one value.",
        "Repeated runs spread around a mean angle, and the spread is the divergence the team measured. Bees without experienced dancers to follow produced the largest divergence in their first dances. Precision therefore depends on experience, not only on the direction the dancer is signaling. Later tests of the same bees showed improved directional precision.",
        "A follower must convert the comb-relative angle into a flight direction, and that conversion draws on celestial information outside the hive. The dancer supplies the angle, while the follower supplies the sun's bearing. Both steps together turn a comb angle into a flight route toward the resource. Motor precision limits how exactly the angle is produced in the first place.",
    ], "Dong et al. (2023)", ["Dong 2023"]),
    ins(6, "Displaced recruits keep the flight vector", [
        "Riley and colleagues released dance followers at sites 200–250 m southwest of the hive, after they had attended dances advertising a feeder 200 m east of the hive. The flight instruction had been decoded at the hive, so the release point was the sole change. Their dances had described the same direction and distance from the hive.",
        "Displaced bees began with a straight eastward flight, averaging 188 m before search. Their initial heading matched the advertised feeder, not the release point. The bees did not calculate a new bearing from the release site toward the real feeder. Straight flights of this kind were measured in the hive-released recruits as well, averaging 206 m.",
        "The dance therefore carries a flight instruction that is tied to the hive's position. A vector from one origin leads to a different endpoint when executed elsewhere. Familiar landmarks can refine the search later, particularly in landscapes with many recognizable features. Riley's landscape was sparse, so the recruit's search depended on the flight vector.",
    ], "Riley et al. (2005)", ["Riley 2005"]),
    ins(9, "Tunnel texture drives the visual odometer", [
        "Srinivasan and colleagues compared outdoor dances with dances after brief tunnel flights. The tunnel was 6.4 m long, 11 cm wide and 20 cm high, so the walls were close to the flying bee. Random black-and-white texture covered the walls and floor, and a mesh ceiling allowed the sky to be seen. The feeder sat 6 m into the tunnel.",
        "Returning bees produced waggle dances after this short passage, even though an equally short outdoor journey normally produces round dances. Dance type therefore depends on the visual experience gathered along the route, not only on physical length.",
        "A visual odometer estimates distance from optic flow, the image motion produced by self-motion. Its readout is the duration of the waggle phase. Dance duration therefore encodes the visually experienced distance, which can differ from the physical distance flown. The striped-tunnel control keeps the feeder location fixed while changing the texture.",
    ], "Srinivasan et al. (2000)", ["Srinivasan 2000"]),
    ins(12, "Short tunnel journeys signal long distances", [
        "Srinivasan and colleagues used the outdoor calibration to read dances that followed tunnel passages. The first arrangement had 41 m of total travel, with 6 m inside the tunnel. Its mean waggle duration of 528.8 ms corresponded to about 230 m outdoors, far beyond the physical route.",
        "The second arrangement moved the tunnel nearer the hive and covered 12 m in total. Its mean duration of 441.2 ms corresponded to about 184 m. Both passages therefore produced an outdoor-equivalent distance many times the journey actually flown.",
        "The tunnel's close textured surfaces amplify the visual motion that the bee experiences. Waggle duration therefore records visual surroundings as well as physical meters. The 184 m and 230 m values are outputs of the authors' calibration, rather than records of what a bee experiences.",
    ], "Srinivasan et al. (2000)", ["Srinivasan 2000"]),
    ins(15, "Closing the tunnel stops recruitment", [
        "For the first 30 min, the closed tunnel kept dancers from advertising the tunnel journey. Recruits did not arrive at the control stations during this period. Opening the tunnel started dancing and recruitment at the stations. The stations offered neither food reward nor added scent, so arrivals reflect the dance alone.",
        "The northwestern test used the same logic: a closed tunnel before each trial prevented the relevant dances and recruitment. Each trial therefore links a specific dance to the search it triggers. Recruits searched at distances consistent with the route-specific visual calibration. The result connects dance decoding with the followers' own visual navigation.",
        "The search site is thus a measure of how followers decode the dance. The decoding depends on the visual conditions that each route provides, so no single distance dictionary applies. The northwestern peak near 140 m matched that route's calibration of about 157 m. The southern calibration would have predicted about 52 m.",
    ], "Esch et al. (2001)", ["Esch 2001"]),
    ins(18, "Land scenes carry more image contrast", [
        "Tautz and colleagues photographed land and water scenes along the experimental routes. Contrast was calculated from intensity variation inside defined image windows, rather than estimated by eye. Each scene therefore produced a numeric value that could be compared across habitats. The original photographs keep the investigators' measurement windows.",
        "Mean contrast was higher over land than over water. The low-contrast water segment coincided with slower accumulation of waggle duration, while terrestrial segments supported larger increases. Contrast offers a plausible link between natural image structure and effective optic flow.",
        "Controlled tunnel-texture experiments change visual motion directly. Field measurements instead show the dependence under ordinary foraging conditions. The two approaches therefore test the same odometer from opposite directions. Both lines of evidence point to the same conclusion about optic flow.",
    ], "Tautz et al. (2004)", ["Tautz 2004"]),
    ins(21, "Tracing links the dorsal rim to the MEDRA", [
        "Zeller and colleagues injected fluorescent tracers into the dorsal rim of the honeybee eye. The labeled input reached a distinct dorsal-medulla compartment called the MEDRA. Neighboring medulla regions were distinguished by complementary injections and synapsin labeling. The published micrographs keep anatomical orientation and micrometer scale bars.",
        "Sakura's occlusion experiment tested the same region from a behavioral angle. Covering the dorsal rim eliminated e-vector learning, whereas covering the rest of the eye left it intact. Anatomy and behavior therefore support the same pathway from opposite ends.",
        "Input from the dorsal rim therefore enters the visual system through a specialized compartment. Such an entry pathway identifies where polarization-associated signals first arrive in the optic lobe. Tracing reveals this connection, while the sky-compass response is tested separately.",
    ], "Sakura et al. (2012); Zeller et al. (2015)", ["Sakura 2012", "Zeller 2015"]),
    ins(24, "Polarization axis sets the dance axis", [
        "Evangelista and colleagues trained bees through a 12 m textured tunnel with ultraviolet-transmitting polarizers overhead. A diffuser removed direct sight of the sun and overhead landmarks. The artificial polarization pattern therefore served as the sole celestial cue. Transverse and axial polarizations were presented in separate groups of bees. Each group's waggle runs were then measured on the comb.",
        "Transverse polarization shifted the waggle runs to a vertical axis on the comb, and axial polarization shifted them to a horizontal axis. The mean axes were about 91.7° and 1.3° relative to horizontal. The dance direction is therefore set by the polarization orientation. The axis constrains the direction without specifying one heading.",
        "A single e-vector carries a 180° ambiguity, so the same axis represents opposite travel directions. The bees' dances advertised both alternatives. The result links polarized flight input to the communicated direction, while showing that an axis of headings differs from a fully sun-referenced bearing.",
    ], "Evangelista et al. (2014)", ["Evangelista 2014"]),
    ins(27, "Cloud cover removes direct sun sight", [
        "Dyer and Dickinson tested both groups under a cloudy sky. Under those conditions the sun was not visible, so visual access to it could not explain the difference between groups. Their dances therefore reflected learned information about the sun's course. Experience-restricted bees oriented to a morning-afternoon pattern, while full-day bees tracked the local course.",
        "Fully experienced bees' solar estimates followed the continuously changing local sun course. Bees with afternoon-only experience instead used a coarse pattern of the sun's movement. The difference is a refinement of a broad expectation rather than an exact memory of each hourly position. Experience thus sharpens the temporal reference that bees use for sun-compass orientation.",
        "The sun's horizontal bearing changes at a variable rate with time, latitude and season. A universal constant angular-rate correction is therefore inadequate. Experience improves the temporal reference used for navigation, making the calibration learned rather than fixed. Bees therefore calibrate the reference to the local sun course over time.",
    ], "Dyer & Dickinson (1994)", ["Dyer 1994"]),
    ins(30, "Anesthesia delays the hive's activity rhythm", [
        "Cheeseman and colleagues measured hive activity under constant dim light. Under constant dim light, the ordinary day-night cycle is removed as the immediate cause of the shifted rhythm. Six hours of daytime anesthesia delayed daily activity and altered rhythmic gene expression in sampled brains. The hive's activity phase shifted by 5.3 h.",
        "Messenger RNA is the transcript used to produce a gene's protein. The reported delays were 4.9 h for mammalian-type cryptochrome messenger RNA and 4.3 h for period messenger RNA. Clock gene expression remained broadly constitutive. The delays fit a phase shift of the whole daily rhythm, not a pause in every process.",
        "Six hours of anesthesia during subjective night produced no comparable delay. The time-dependent effect points to disturbance of the circadian oscillator. Whole-brain expression averages over many cells, which hides the cells that deliver time information to a compass pathway. Timing of the anesthesia therefore matters for the phase of the rhythm.",
    ], "Cheeseman et al. (2012)", ["Cheeseman 2012"]),
    ins(33, "PDF fibers lie beside transmedulla neurons", [
        "Pigment-dispersing factor, or PDF, is a neuropeptide associated with circadian signaling in insects. Zeller and colleagues combined PDF immunostaining with tracer labeling of transmedulla neurons. The combined labels revealed where potential timing input could meet the sky-compass pathway. Both labels were examined at higher magnification in the medulla.",
        "PDF-positive fibers occupied the same medulla layer as parts of the traced neurons. Labeled puncta lay in close proximity along the cells' passage through the medulla. The two labels did not colocalize, and PDF labeling was absent from within the MEDRA. This pattern places PDF fibers next to the cells without overlapping them.",
        "The result identifies neighboring neuronal populations and a candidate site for modulation. PDF is a neuropeptide, so the contact is a plausible route for timing signals. Circadian compass correction is the proposed role of that contact. Tracer labeling defined the traced neurons in these preparations.",
    ], "Zeller et al. (2015)", ["Zeller 2015"]),
    ins(36, "Separated complexes lie in both bulbs", [
        "Synapsin is associated with presynaptic machinery, and filamentous actin is prominent in postsynaptic regions. Held and colleagues used both stains on honeybee bulb tissue. Their combined pattern marks the sites where terminals and processes meet. Each complex contains one large presynaptic core and several smaller postsynaptic profiles.",
        "Confocal images revealed separated complexes in the lateral and medial bulbs. Traced TuLAL1 terminals formed the presynaptic cores, and TL neuron processes contacted them. Complementary labeling connected each cell's projection to the local terminal organization. The arrangement distributes tubercle signals to several downstream cells in parallel.",
        "The bulbs use these complexes to distribute the tubercle outputs among several downstream neurons. Confocal images alone leave finer membrane contacts unseen. Electron microscopy, used next in the study, resolves the contacts in detail. Membrane-level detail shows which cells make each contact.",
    ], "Held et al. (2016)", ["Held 2016"]),
    ins(39, "Learned field cues persist for 24 h", [
        "Greggers and colleagues paired an electric-field stimulus with sucrose during conditioning. An uncharged material or an inactive stimulus source served as the unrewarded comparison. Bees learned constant fields as well as fields modulated at 60 Hz. The conditioned proboscis extension response served as the readout. Both stimulus types produced clear learning.",
        "Removing the antennae eliminated the learned field response. Wax coating that restricted the antennal joints strongly reduced it, while coating the surfaces and keeping the joints mobile produced a smaller reduction. Responses to electric cues were still present after 24 h. The retained response shows that the memory outlasted the conditioning session.",
        "The intervention pattern supports a contribution from antennal mechanoreception, including receptors linked to both joints. Johnston's organ is one of several possible sensors, alongside the antennal surface hairs. Antennal removal eliminates the whole antenna, which is a stronger manipulation than coating the surfaces. Conditioning under these controlled conditions demonstrates a usable electric cue.",
    ], "Greggers et al. (2013)", ["Greggers 2013"]),
    ins(42, "Mature foragers differ from young workers", [
        "Kumaraswamy and colleagues compared DL-Int-1 in newly emerged workers aged 1–3 days with foragers older than 10 days. Both groups were recorded intracellularly and filled with dye for morphology. Cell identity was preserved across the age comparison, so the same neuron type could be followed. Gross arborization extent was similar in the two groups.",
        "Branch density differed in selected regions, while the overall arbor extent matched between the groups. Foragers' responses showed a stronger contrast between spontaneous activity and vibration-evoked inhibition. That contrast gives the stimulus a sharper temporal signature in older bees. Reconstructions and response distributions document these changes at two levels of analysis.",
        "Maturation can change signal processing without replacing a neuron's overall projection pattern. Age and experience covary in this design, so the differences reflect development linked with foraging. The response distribution shows what changes, and the reconstructions show that the cell's wiring is retained. Foraging experience is one candidate driver of these changes.",
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
