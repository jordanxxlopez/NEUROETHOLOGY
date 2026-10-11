"""Scaffold spec for Lecture 24 (Drive deck Neuroethology_Lecture24_FA2026.pptx). Body rewrites are in body_L24.py."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L24 as _body  # noqa: E402


def ins(after, title, paragraphs, citation, refs):
    notes = [title + "."] + [
        [f"Explanation {i + 1}.", *(p.split(". ", 1))] for i, p in enumerate(paragraphs)
    ] + [["Source.", f"The figure and the measurements come from {citation}.", "Each statement is tied to the recordings or observations of that study."]]
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


inserts = [
    ins(3, 'Ion tracers measure plume arrival', [
        'Signal was present about 20% of the time at the downwind detectors in both the field and the forest. Murlis, Willis and Cardé released negatively charged air ions as the tracer, which made the arrival of air from the source measurable at each detector. Intermittent tracer signals appeared at several field and forest distances, so the alternation between signal and gap held across both sites.',
        'Sampling extended 20 m downwind in the open field and 10 m downwind in the forest, so the tracer covered a range of distances in both environments. Ionized air approximates plume transport, but it is not chemically identical to pheromone. The tracer shows when air carrying odor arrives, rather than the chemistry of the signal a moth detects.',
        'In this framework, a filament is a strand of odor-bearing air, and a gap is an interval without detectable signal. The two states alternate along the wind, so a fixed detector switches between encounter and clean air as the strands pass. Strands are brief, and the clean-air gaps between them set the spacing of encounters.',
    ], 'Murlis et al. (2000)', ['Murlis 2000']),
    ins(6, 'Filament contact triggers a brief surge', [
        'The average upwind surge covered 13.4 cm and lasted 0.38 s. Its onset followed odor contact by about 0.30 s, so the motor response began shortly after the strand had reached the male. Surge length and onset time are two separate measures of one brief response, and both describe the same flight event. The surge was short and came soon after contact.',
        'The authors combined their observations into a proposed phasic-tonic account. Individual recorded tracks remained distinct from the calculated template that the account produced, so the template summarized the responses without matching each track exactly. The account describes a pattern of responses rather than a single flight trajectory. The template was calculated from the recorded trajectories.',
        'Casting means repeated crosswind turns after odor contact is lost. The surge and the casting form two phases of one response, with the first moving the male upwind and the second searching sideways across the wind. Together the two phases produce the flight track that the recordings display. The sequence fits a short sensory trigger followed by a longer motor response.',
    ], 'Vickers & Baker (1994)', ['Vickers 1994']),
    ins(9, 'Virtual search succeeds within a 10-mm radius', [
        'A search counted as successful when the virtual position entered a 10-mm radius around the source within 300 s. Odor ports stimulated the two antennae independently, so the left and right sensory inputs could differ within the same trial. Wind arrived from four directions, which allowed wind direction to be set apart from odor. Every trial had a defined end point.',
        "Closed-loop stimulation means the sensory inputs depend on the animal's measured movement. Movement and input influence one another instead of following an entirely predetermined replay, which makes the virtual search interactive rather than scripted. Each step the animal takes changes what its antennae and eyes receive next. The loop links the animal's walking to what it smells next.",
        'Optic flow is the movement of a visual scene associated with self-motion. Visual stimulation supplied this optic flow, which gave the animal feedback about its own motion through the virtual field. That feedback sits alongside the odor and wind inputs in the same closed loop during each trial. Each cue can be reversed without changing the others.',
    ], 'Yamada et al. (2021)', ['Yamada 2021']),
    ins(12, 'Spike size identifies the bombykol neuron', [
        "Sakurai and colleagues distinguished the large-amplitude spikes of the bombykol neuron from the smaller spikes of the bombykal neuron. Those amplitude differences allowed the two units to be followed separately during each stimulus, even within one hair. Spike amplitude served as a practical identity marker for each unit during the recordings. Spike size is a measurement of each unit's activity.",
        'PxOR1 is a receptor from Plutella xylostella, a different species of moth from Bombyx mori. Its gene was introduced into the bombykol-responsive neurons, which already expressed their native receptor. The transgenic neurons carried two receptors, and the native one was retained. Those two receptors were present together in one cell type. The second receptor did not replace the first.',
        'Bombykal is the aldehyde corresponding to bombykol, while bombykol is the alcohol. The neighboring neuron responds to a chemically related molecule rather than to the same compound. That difference in functional group is one reason the two channels can be told apart by their ligand preference. Ligand preference, not position in the hair, marks each channel.',
    ], 'Sakurai et al. (2011)', ['Sakurai 2011']),
    ins(15, 'Glomeruli set the central target', [
        'A glomerulus is a region of concentrated sensory terminals and the central neurons that interact with them. Sensory axons from one receptor class converge on a restricted target, so each glomerulus carries one kind of input. A glomerulus holds a defined place in the central map of olfactory input. The map links each receptor class to a defined place.',
        'The toroid is a central target, whereas the receptor itself resides in the peripheral neuron. Preserving the target distinguishes a change in ligand recognition from a wholesale remapping of sensory axons. A remapping would move the axons into a different glomerulus, and the axons did not move. Axon endings alone were used to judge the target.',
        "A shift to the neighboring cumulus would have moved the new ligand's information into a different glomerulus. The toroid result tests where that information lands in the brain after the receptor change. Because the target stayed the same, the altered receptor drove the existing toroid channel. That placement makes the toroid a useful test of channel rerouting.",
    ], 'Sakurai et al. (2011)', ['Sakurai 2011']),
    ins(18, 'Residue substitutions shift potassium permeability', [
        'BmOR1 D299N and E356Q reduced relative potassium permeability, while Orco Y464A increased it. Those three substitutions moved permeability in opposite directions across the two subunits. Because permeability sets the reversal potential, these shifts changed the ion balance of the complex in opposite ways. Each change alters one residue in one of the two subunits.',
        'The notation names the original residue, its position and the replacement. E356Q replaces glutamate at position 356 with glutamine, and the substitution keeps the receptor intact rather than deleting it. A residue name encodes the change at one position without removing the protein. The residue numbers refer to positions within each protein. The name thus pinpoints where the change was made.',
        'Each test changed one subunit while the other stayed in its normal form, so each shift could be assigned to a single protein. The reported changes identify which subunit carries each specific effect. Both subunits contribute to the ion preference of the complex, so neither can be treated as inert. Their effects are interpreted together.',
    ], 'Nakagawa et al. (2012)', ['Nakagawa 2012']),
    ins(21, 'Matched loads compensate for lower sensitivity', [
        'Shiota and colleagues used 100 ng of bombykol for the normal group and 10,000 ng for the knockout group. The larger knockout load was chosen to compensate for the lower knockout sensitivity. Matching the response amplitudes in this way kept the timing comparison from being driven by size. The matching was done on response size, not on stimulus timing.',
        'Pulses were delivered at 0.17 Hz and at 2 Hz in these trains. At 2 Hz, several knockout preparations never returned to baseline throughout the train, whereas normal antennae recovered rapidly. The knockout trace carried residual voltage from one pulse into the next. The difference between the two groups appeared at the faster rate.',
        'The remaining voltage between responses was larger in the knockout. That residual voltage is the trace of earlier stimuli that had not yet decayed when the next pulse arrived. Each successive pulse started from a higher baseline in the knockout trains. Those trains were analyzed for the voltage left between pulses. That measure reflects the slowed termination.',
    ], 'Shiota et al. (2021)', ['Shiota 2021']),
    ins(24, 'Arrival delay reveals a timing deficit', [
        'Normal moths received 1-100 ng bombykol source loads, while knockouts received 100-10,000 ng to compensate for lower sensitivity. The two dose ranges overlap at 100 ng, and the knockout range reached loads 100-fold higher. Those loads were matched to the reduced sensitivity rather than to the stimulus timing. The knockout loads were set well above the normal range.',
        'A sensory system can keep the ability to reach a source while losing the timing precision needed for rapid progress. Arrival time was the measure that revealed the knockout deficit. Success alone would have hidden the delay, because both groups eventually located the source. Success was a weaker measure of the defect than arrival time.',
        'Source-finding success and time were measured separately, so a delay could be identified even when the males found the source. The knockout males showed briefer forward bouts and extra turning along the route. These differences appeared in the same wind tunnel trials that produced the success results. The delay was an arrival effect, not an inability to find the source.',
    ], 'Shiota et al. (2021)', ['Shiota 2021']),
    ins(27, 'Light pulse duration sets weak and strong input', [
        'Tabuchi and colleagues used a 3-ms pulse, which sat near behavioral threshold, and a 10-ms pulse, which produced strong behavioral responsiveness. These two durations defined weak and strong input for this optogenetic preparation. The 3-ms duration was then used for the paired-pulse tests. The contrast between these two durations was the basis of the test.',
        "Parental genetic controls lacked the light response, which ties the response to the introduced channel. Increasing the pulse duration raised the spike output of the targeted unit, so the input could be graded. Light intensity had the same effect, so both parameters set how strongly the sensory neuron fired. The sensory neuron's output was the quantity being controlled.",
        "Peripheral recordings also constrain claims that later amplification originates entirely in the sensory neuron. The measured spikes set the limit on what the central pathway receives. Recording the receptor neuron directly gives the transmitted input itself. Spike counts from one unit are a direct readout of its input. The readout is the unit's spikes, not the light itself.",
    ], 'Tabuchi et al. (2013)', ['Tabuchi 2013']),
    ins(30, 'GABA blockade exposes strong-input integration', [
        'After blockade, strong inputs separated by about 40-100 ms could produce supralinear integration in the projection neurons. Before blockade, the same strong inputs did not integrate in this way. The integration window opened once inhibition was removed. The window was absent in normal PNs with inhibition intact. The contrast between normal and blocked preparations is the central result.',
        'GABA-A receptors are associated with ion-channel inhibition, whereas GABA-B receptors signal through G proteins. Those signaling mechanisms differ, and the combined blockade treats both receptor classes together. The pharmacology identifies GABA signaling as a whole rather than one subtype. The combined treatment tested the whole GABA system. The blockers were applied during the PN recordings.',
        'Spontaneous and light-evoked firing also increased after blockade, consistent with removal of inhibition. The rise in baseline firing is a second effect of the same treatment, separate from the change in how strong inputs combine. The increase persisted during the recordings. Strong inputs had a larger effect after blockade. Their rise was visible in the same cells.',
    ], 'Tabuchi et al. (2013)', ['Tabuchi 2013']),
    ins(33, 'Dye labels both fiber directions', [
        'Fluorescent dye introduced through the neck connectives labeled both descending and ascending fibers. Backfill labeling includes fibers that carry signals toward the brain as well as away from it. The staining map thus covers both directions of travel along the connectives. The dye was introduced through the neck connectives, so the labels reflect fibers that run along that route.',
        'Confocal imaging showed dense labeling in the posterior slope, a posterior-ventral neuropil. Dense labeling in one neuropil shows where fibers from the dye concentrate, and the cell types in those fibers need separate identification. The labeling was imaged with confocal microscopy, a method that produces optical sections. Optical sections separate the labeled fibers from one another in depth.',
        'The staining included ascending fibers in the same preparation, so the map covers the full set of labeled routes rather than the outgoing neurons alone. Each labeled route is a candidate pathway for pheromone information, and its identity is defined by its anatomy. Physiological recordings are needed to test each route. The mapping is an anatomical first step.',
    ], 'Namiki et al. (2018)', ['Namiki 2018']),
    ins(36, 'FF and ff name opposite and synchronized classes', [
        "The authors named the antiphasic class FF and the synchronized class ff. These labels appear throughout the paper's recordings and identify the two response classes. The paper treats these classes as response patterns, not as receptor types. Their names mark two distinct patterns across the recorded signals. Neither label implies a particular receptor or molecular cause.",
        'Bilateral connective recordings revealed opposite states across the two sides. A small-bundle recording separated large and small impulses with opposite switching patterns. The two impulse sizes carried opposite switching behavior within one bundle, a result that the bilateral data alone would miss. Those states describe two sides of the same descending system. The pattern was visible on both connectives.',
        "Antiphasic activity means one signal is high while the other is low. The relationship requires no regular oscillation and no direct connection between the two signals. Synchronized state changes instead move both signals in the same direction at the same time. Synchronized changes are the second pattern in the paper's classification. Both patterns are relationships between signals, not single responses.",
    ], 'Kanzaki et al. (1994)', ['Kanzaki 1994']),
    ins(39, 'Serotonin raises the response fraction', [
        'For 5 ng bombykol, the response fraction rose from 18% in the control condition to 30% during serotonin treatment. That increase shows the same dose producing more behavioral responses. The curve shifted toward higher sensitivity at a fixed pheromone dose. Responses were scored as a fraction of tested males. The rise was measured against a saline-treated baseline.',
        'Sensitivity drifted back toward baseline 24 h after application. The curve moved back toward its original control position, and the recovery indicates that the effect was partly temporary. The change in responsiveness was partly reversible. A full dose-response curve was recorded at each time point. Sensitivity recovered toward its earlier level over the following day.',
        'Brain exposure and pharmacological application can affect several elements at once. The cellular target is inferred from the behavioral curve rather than measured directly. Identifying that target would need a more selective manipulation. The application site was the exposed brain, which is a broad target. Several cell types in that region could respond. Modulation is a change in gain, not in the stimulus.',
    ], 'Gatellier et al. (2004)', ['Gatellier 2004']),
    ins(42, 'Serotonin content tracks daily sensitivity', [
        'Serotonin content peaked around noon at about 0.72 pmol per brain and declined to about 0.41 pmol per brain two hours after darkness began. Measurements were taken every 4 h across the 24-h cycle. Serotonin content changed by a large margin across a single day. The measurements covered a full light-dark cycle. The daily peak was found near midday.',
        'For 1 ng bombykol, behavioral responsiveness rose from 32% at 06:00 to 63% around noon, then declined to 16% at 22:00. The sensitivity curve followed the serotonin rhythm across the day. The lowest responsiveness came in the late night. Responsiveness was measured at several times across the day. Responsiveness followed the same daily order as serotonin content.',
        "Both measures were taken at matching times of day. The shared timing links the brain's serotonin state to the strength of the search response. The pattern is a correlation across the day rather than a direct test of cause. The peak sensitivity and the peak serotonin content occurred in the same part of the day.",
    ], 'Gatellier et al. (2004)', ['Gatellier 2004']),
]

spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(_body.body)} body slides rewritten, {len(inserts)} scaffold slides")
