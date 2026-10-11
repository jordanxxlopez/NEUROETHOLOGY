"""Scaffold spec for Lecture 40 (Drive deck Neuroethology_Lecture40_FA2026.pptx). Body rewrites are in body_L40.py."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L40 as _body  # noqa: E402


def ins(after, title, paragraphs, citation, notes, refs):
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


def plain(text):
    return re.sub(r"\*\*|(?<![A-Za-z0-9])_|_(?![A-Za-z0-9])", "", text)


inserts = [
    ins(3, "ChR2 conducts light-driven current directly", [
        "**Channelrhodopsin-2** is a retinal-containing protein from the green alga Chlamydomonas reinhardtii. When blue light near 450 nm reached ChR2-expressing frog oocytes, it produced a current that uninjected oocytes lacked, which showed that the protein itself carries the response to light.",
        "Voltage clamp holds the membrane at a chosen voltage while the amplifier records the current that flows. Changing the held voltage altered the size and direction of the light-evoked current, a pattern that fits a passive conductance rather than an ion pump. Current direction therefore depends on the voltage at which the membrane is held.",
        "A truncated protein containing the first 315 amino acids kept its channel function. The light-gated conductance therefore lies within the membrane-spanning portion of the protein, the part that forms the pathway for charged particles. That region alone is sufficient to carry the light-gated current.",
    ], "Nagel et al. (2003)", [
        "ChR2 conducts light-driven current directly.",
        ["Expression.", "Blue light near 450 nm produced a current in ChR2-expressing oocytes.", "Uninjected oocytes showed no such current.", "The protein carries the response itself."],
        ["Clamp.", "Voltage clamp held the membrane at chosen voltages.", "The current changed size and direction with the held voltage.", "That pattern fits a passive conductance."],
        ["Truncation.", "The first 315 amino acids kept channel function.", "The light-gated conductance lies in the membrane-spanning region."],
        ["Field setting.", "The experiments used expression systems, not intact animals.", "They identify a cellular mechanism."],
    ], ["Nagel 2003"]),
    ins(6, "Membrane expression enables optical spiking", [
        "Boyden and colleagues delivered a ChR2 fusion with yellow fluorescent protein into cultured rat neurons using a lentiviral vector. The fluorescent tag marked the expressing cells and the membrane-associated processes that extend from them. The lentiviral vector is a modified virus that carries the expression construct into the cells.",
        "Blue light between 450 and 490 nm generated an average peak **inward current** near 496 pA, followed by a smaller sustained current near 193 pA. Neurons carrying the fluorescent tag alone gave no light-evoked response, so the electrical effect came from the channel rather than from fluorescence or illumination.",
        "Inward current depolarizes the neuron, and when the voltage reaches firing threshold, the neuron produces an **action potential**. Light therefore drives spikes in an expressing cell without requiring knowledge of its natural synaptic targets. The current is an inward flow that makes the internal voltage less negative.",
    ], "Boyden et al. (2005)", [
        "Membrane expression enables optical spiking.",
        ["Expression.", "A ChR2 fusion with yellow fluorescent protein was delivered into cultured rat neurons.", "The fluorescent tag marked the expressing cells."],
        ["Current.", "Blue light produced an average peak inward current near 496 pA.", "A smaller sustained current near 193 pA followed."],
        ["Control.", "Neurons with the tag alone gave no light-evoked response.", "The effect therefore came from the channel itself."],
        ["Spikes.", "Inward current made the internal voltage less negative.", "Threshold triggered an action potential."],
        ["Field setting.", "The neurons were cultured, not in an intact animal.", "The result concerns expression in a dish."],
    ], ["Boyden 2005"]),
    ins(9, "Chloride gradients set the silencing effect", [
        "Govorunova and colleagues used GtACR2 in cultured rat neurons to test whether light can silence cells. The photocurrent reversed near −88 mV, a voltage that depends on the chloride gradient across the membrane. The reversal voltage is the point where the measured current changes sign.",
        "Illumination suppressed current-evoked spikes in trains up to at least 25 Hz. In a ramp protocol, full suppression occurred at a light intensity of 0.005 mW/mm², and the ramp tested a graded range of light intensities. Expressing neurons kept their dark-state electrical properties and morphology.",
        "Opening an anion channel moves the membrane toward the chloride equilibrium potential, so the same light can hyperpolarize one cell and depolarize another. The starting voltage and the chloride gradient of each cell determine which outcome occurs. Silencing was validated under the measured recording conditions, so each new cell type needs its own chloride measurement.",
    ], "Govorunova et al. (2015)", [
        "Chloride gradients set the silencing effect.",
        ["Reversal.", "The photocurrent reversed near −88 mV in cultured rat neurons.", "That voltage depends on the chloride gradient."],
        ["Suppression.", "Illumination suppressed spikes in trains up to at least 25 Hz.", "A ramp protocol reached full suppression at 0.005 mW/mm²."],
        ["Mechanism.", "An anion channel moves the membrane toward the chloride equilibrium potential.", "The same light can hyperpolarize one cell and depolarize another."],
        ["Context.", "Dark-state properties of the expressing neurons were retained.", "The silencing was validated under the measured recording conditions."],
    ], ["Govorunova 2015"]),
    ins(12, "Housing changes wing-extension sensitivity", [
        "Inagaki and colleagues housed males alone or in groups for 7 days before testing them with red light. Wing extension was the measured readout of the courtship circuit, and each male was stimulated across a range of light intensities with the same method.",
        "Males housed alone responded to weaker red light than males housed in groups. Activating the descending courtship neurons pIP10 produced no comparable shift, even though the stimulation method matched across the two groups. Housing-dependent sensitivity therefore appeared for P1 activation but not for pIP10 activation.",
        "The housing effect acts at P1 or at a downstream stage before pIP10, so social experience changes how strongly the same light input drives wing extension. The light stimulus stays constant while the behavioral response changes with housing history. Social history thus modifies the behavioral consequence of an identical input.",
    ], "Inagaki et al. (2014)", [
        "Housing changes wing-extension sensitivity.",
        ["Design.", "Males were housed alone or in groups for 7 days.", "Red-light intensities were then varied during testing."],
        ["Result.", "Single-housed males responded at lower intensities.", "The pIP10 activation showed no comparable shift."],
        ["Locus.", "The housing effect acts at P1 or upstream of pIP10.", "The light input stays the same across groups."],
        ["Context.", "The stimulation method matched across the two groups.", "The social experience was the difference between them."],
    ], ["Inagaki 2014"]),
    ins(15, "Single neurons bias behavior toward one action", [
        "Cande and colleagues measured behavior in a low-dimensional map that groups similar movements, then asked whether activating a descending population moved behavior toward one region of that map. Occupancy counted how often each fly performed the movements assigned to a region.",
        "Many experimental flies showed reduced behavioral entropy during 15 s red-light epochs, which means their activity spread across fewer actions. Matched controls without retinal showed no such population-level reduction. Most effective lines favored one behavioral region. Entropy is a measure of how broadly activity is distributed across the available actions.",
        "The pattern points to modular control, in which a descending population recruits a coherent part of the movement repertoire. Selective tests of normal activity, necessity and context would show whether each neuron serves one command or several. Each tested line therefore recruits a defined region of the behavior space.",
    ], "Cande et al. (2018)", [
        "Single neurons bias behavior toward one action.",
        ["Map.", "Behavior was described in a low-dimensional map of similar movements.", "Occupancy was tracked for each red-light activation."],
        ["Entropy.", "Many experimental flies showed reduced behavioral entropy.", "Matched controls showed no such reduction."],
        ["Modularity.", "Most effective lines favored one behavioral region.", "A descending population can recruit a coherent part of the repertoire."],
        ["Context.", "The effect was measured in an arena with stimulation at 15 s epochs.", "Entropy measures how broadly activity spreads across actions."],
    ], ["Cande 2018"]),
    ins(18, "Serial reconstruction maps ciliomotor wiring", [
        "Serial transmission electron microscopy of a 3-day-old Platynereis larva allowed Verasztó and colleagues to trace neurons and their synaptic contacts. The reconstruction was related to the whole-body distribution of ciliated cells. The map therefore links specific neurons to specific sites of ciliary control.",
        "The large MC neuron and the paired Loop neurons made extensive contacts with the locomotor ciliary bands. Molecular labeling and cell morphology supported a cholinergic identity, meaning that these cells use acetylcholine as their transmitter. Axons reached several positions along the body.",
        "A structural synapse sets neither the timing nor the sign of the functional response. Calcium recordings and selective interventions are therefore needed to show which reconstructed neurons take part in ciliary arrests. Reconstructed contacts show where a neuron could act, and calcium recordings show when it acts.",
    ], "Verasztó et al. (2017)", [
        "Serial reconstruction maps ciliomotor wiring.",
        ["Method.", "Serial transmission electron microscopy imaged a 3-day-old larva.", "Neurons and their synaptic contacts were traced."],
        ["Contacts.", "The MC neuron and the paired Loop neurons contacted the ciliary bands.", "Axons reached several positions along the body."],
        ["Identity.", "Molecular labeling supported a cholinergic identity.", "These cells use acetylcholine as their transmitter."],
        ["Meaning.", "The wiring shows how a few neurons reach distant effectors.", "Function is tested separately with calcium recordings."],
    ], ["Verasztó 2017"]),
    ins(21, "Filament speed sets the startle response", [
        "Bezares-Calderón and colleagues moved a vibrating tungsten filament past Platynereis larvae and recorded the movements at 230 to 350 frames per second. The startle included ciliary arrest, body contraction and elevation of the parapodia. Several of these movements occurred together in each response.",
        "Increasing filament speed favored wider appendage elevation. Placing the filament farther from the head required stronger stimulation, which indicates sensing at short range. Wide elevation was consistently recruited above about 28 µm/ms, and that speed marks the recruitment threshold.",
        "The arrangement therefore links a defined water movement to a coordinated defensive action. The filament speed is the mechanical parameter the experimenter controls, so it provides an input that can be varied and measured across trials. Varying that input changes which appendage movements the larva produces.",
    ], "Bezares-Calderón et al. (2018)", [
        "Filament speed sets the startle response.",
        ["Stimulus.", "A vibrating tungsten filament moved water around the larva.", "Responses were recorded at 230 to 350 frames per second."],
        ["Speed.", "Faster filaments favored wider parapodia elevation.", "Wide elevation was recruited above about 28 µm/ms."],
        ["Distance.", "Filaments placed farther from the head needed stronger stimulation.", "The result indicates sensing at short range."],
        ["Meaning.", "A defined water movement drives a coordinated defensive action.", "Filament speed is the controlled input."],
    ], ["Bezares-Calderón 2018"]),
    ins(24, "Eye convergence marks the start of hunting", [
        "Larval zebrafish that spot small moving prey converge their eyes toward a common frontal region. In the study by Antinucci and colleagues, convergent saccades served as the measurable marker that hunting had begun. A saccade is a rapid eye movement, so each convergent saccade can be counted as the start of a hunt.",
        "Larvae 6 to 7 days after fertilization produced convergence together with lateral tail movement in response to small dark moving spots. About 92% of convergent saccades coincided with tail motion, and the eye-to-tail delay averaged near 12 ms. Small dark spots were the stimulus that most reliably recruited the combined movement.",
        "Two-photon calcium imaging recorded brain activity during these movements in the restrained preparation. Pretectal neurons were then tested for their role in hunting through activation and ablation in larvae that moved freely. Those experiments used free-swimming larvae to test the behavior under fewer constraints.",
    ], "Antinucci et al. (2019)", [
        "Eye convergence marks the start of hunting.",
        ["Behavior.", "Larval zebrafish converge their eyes toward a frontal region when prey appears.", "Convergent saccades mark the start of hunting."],
        ["Timing.", "About 92% of convergent saccades coincided with tail motion.", "The eye-to-tail delay averaged near 12 ms."],
        ["Imaging.", "Two-photon calcium imaging recorded activity in the restrained preparation.", "Eyes and tails stayed mobile during recording."],
        ["Follow-up.", "Activation and ablation tests were run in free-swimming larvae.", "They addressed the role of pretectal neurons."],
    ], ["Antinucci 2019"]),
    ins(27, "Pretectal loss spares swimming and escape", [
        "Antinucci and colleagues ablated about 90% of a fluorescently labeled pretectal population at 6 days after fertilization. Free-swimming larvae were tested before the procedure and again on the following day. Fluorescent labeling identified which cells were removed.",
        "Prey consumption, hunting initiation and the duration of hunting sequences declined after the ablation. Average swimming speed, escape responses to looming stimuli and the optomotor response were retained. The optomotor response is swimming driven by moving visual patterns. Sham ablations of nearby thalamic cells were run as the control instead.",
        "The spared behaviors indicate that the deficit is specific to hunting rather than a general loss of movement or visual responsiveness. The pretectal population contributes to the start and continuation of prey capture, and its loss leaves swimming and escape working normally.",
    ], "Antinucci et al. (2019)", [
        "Pretectal loss spares swimming and escape.",
        ["Ablation.", "About 90% of the labeled pretectal population was removed.", "Larvae were tested before and after the procedure."],
        ["Deficit.", "Prey consumption and hunting initiation declined.", "Hunting-sequence duration also declined."],
        ["Controls.", "Swimming speed and escape responses were retained.", "The optomotor response was also retained."],
        ["Sham.", "Sham ablations removed nearby thalamic cells.", "That comparison isolates the pretectal population."],
    ], ["Antinucci 2019"]),
    ins(30, "Head tracking follows flies during copulation", [
        "Flyception2 tracks the head rather than the outline of the body, so the head stays identifiable when two flies overlap. Grover and colleagues built the system to record brain fluorescence in freely moving adult flies. The animal is untethered, with no cable running to the microscope.",
        "Three glass retroreflective beads, each about 30 µm across, marked the imaging window. A tracking loop updated mirror position at 1,000 Hz, and focus followed changes in head height during courtship and copulation. Retroreflection returns incoming light toward its source, which makes the beads easy to track.",
        "P1 fluorescence during the same social interaction was recorded in freely moving flies. The method keeps social contact in the measurement, which outline-based tracking had disrupted, and it still uses a surgically prepared window in a bounded arena. Recordings were made from the same targeted cells during courtship and mating.",
    ], "Grover et al. (2020)", [
        "Head tracking follows flies during copulation.",
        ["Tracking.", "The system tracks the head instead of the body outline.", "The head stays identifiable when flies overlap."],
        ["Hardware.", "Three glass beads, each about 30 µm across, marked the window.", "A tracking loop updated mirror position at 1,000 Hz."],
        ["Focus.", "Focus followed changes in head height.", "Courtship and copulation were both tracked."],
        ["Preparation.", "A surgically prepared window and a bounded arena were used.", "Social contact was preserved in the recording."],
    ], ["Grover 2020"]),
    ins(33, "Filters set which spikes can be measured", [
        "In the Szuts design, electrode voltages passed a filter between 80 and 2,300 Hz, and each channel was sampled 20,000 times per second. Sampling rate states how often a signal is measured, while bandwidth states which frequency range the filter keeps. Both settings determine what the recording can show.",
        "A simultaneous sample-and-hold stage captured the channel voltages before time-division multiplexing placed successive channels onto one shared output. Synchronization markers identified each channel scan, so the original signals could be rebuilt after radio transmission. Multiplexing therefore sends the channels in turn through one radio link.",
        "Frequency components removed by the filter stay absent however fast the sampling is. The configuration suited extracellular spike analysis, so hardware settings decide which neural events a behavioral experiment can relate to movement, sensation or task timing.",
    ], "Szuts et al. (2011)", [
        "Filters set which spikes can be measured.",
        ["Settings.", "Electrode voltages were filtered from 80 to 2,300 Hz.", "Each channel was sampled at 20 kHz."],
        ["Multiplexing.", "A sample-and-hold stage captured the channel voltages.", "Successive channels were placed onto one shared output."],
        ["Markers.", "Synchronization markers identified each channel scan.", "The original signals could be rebuilt after radio transmission."],
        ["Meaning.", "Hardware settings define which events are measurable.", "Spike analysis was the configuration's main purpose."],
    ], ["Szuts 2011"]),
    ins(36, "Synchronized clocks link spikes to landings", [
        "Snyder and colleagues tracked bats and human experimenters with a real-time location system that estimates tag positions from fixed room anchors. Relating a spike to a landing requires that the positional and neural clocks share one reference.",
        "Positions were sampled at 100 Hz and synchronized to the neural data through an external timing signal. Repeated trajectories were aligned to landing or take-off, so discharge could be compared at matching flight stages toward different reward providers. Each aligned trajectory therefore lines up with the same event in every flight.",
        "A landing-aligned change in firing can be distinguished from firing linked to a different location or route when the spatial and temporal measurements are precise enough. Synchronization fixes which measured position corresponds to each recorded spike. Matched timing keeps each flight's events aligned across trials.",
    ], "Snyder et al. (2024)", [
        "Synchronized clocks link spikes to landings.",
        ["Tracking.", "A real-time location system estimated tag positions from room anchors.", "Bats and human experimenters were both tracked."],
        ["Sampling.", "Positions were sampled at 100 Hz.", "An external timing signal synchronized them with the neural data."],
        ["Alignment.", "Repeated trajectories were aligned to landing or take-off.", "Discharge was compared across matching flight stages."],
        ["Precision.", "The spatial and temporal measurements set the resolution.", "Synchronization matches each spike to a measured position."],
    ], ["Snyder 2024"]),
    ins(39, "Ensembles record freely flying foraging bats", [
        "A **neural ensemble** is a group of neurons whose joint activity can carry information. Wireless Neuropixels recordings from the dorsal hippocampus were made by Forli and colleagues in freely flying Egyptian fruit bats. The bats chose when to fly and foraged for rewards at their own pace.",
        "The system recorded single-unit activity together with local field potentials, which reflect nearby population currents. Flights alternated spontaneously with rest, and about 71% of flight-active neurons showed spatial selectivity across the sampled trajectories. Both single units and population signals were therefore available for each flight.",
        "Population recording reveals activity sequences that one electrode or one cell would miss. Freely chosen flights combined with repeated routes keep natural variability while still allowing consistent measurement. Sequences can be compared across repeated flights, which is the value of the design.",
    ], "Forli et al. (2025)", [
        "Ensembles record freely flying foraging bats.",
        ["Preparation.", "Wireless Neuropixels recorded the dorsal hippocampus.", "The bats flew freely and foraged at a self-paced rate."],
        ["Signals.", "Single-unit activity and local field potentials were recorded together.", "Field potentials reflect nearby population currents."],
        ["Selectivity.", "About 71% of flight-active neurons showed spatial selectivity.", "The trajectories were sampled across the flights."],
        ["Meaning.", "Population recordings expose sequences that single cells cannot show.", "Repeated routes keep variability while enabling consistent measurement."],
    ], ["Forli 2025"]),
    ins(42, "Miniature LEDs receive power wirelessly", [
        "Montgomery and colleagues built light-delivery implants for mice that sit entirely inside the body. A receiving coil and local electronics drew power from an external radio-frequency apparatus, and a micro-LED converted that power into light near the target tissue. The implant is fully internal, so no fiber leaves the skin.",
        "The lightest implant weighed roughly 20 mg and filled about 10 mm³. An aluminum resonant cavity operating near 1.5 GHz concentrated electromagnetic energy in the mouse, which powered a blue LED with no external fiber or battery. The cavity delivered power to the implant from outside the animal.",
        "Miniaturization allowed implantation beneath the skin and access to central or peripheral targets. The radio-frequency geometry was optimized for mice in the tested arena, so the power transfer was matched to that body size and that setup. Access to peripheral targets is therefore possible without a tether.",
    ], "Montgomery et al. (2015)", [
        "Miniature LEDs receive power wirelessly.",
        ["Implant.", "The light-delivery implant sits entirely inside the mouse.", "A receiving coil and electronics take power from outside."],
        ["Output.", "A micro-LED converts electrical power into light near the tissue.", "The lightest implant weighed roughly 20 mg."],
        ["Cavity.", "An aluminum resonant cavity operated near 1.5 GHz.", "It concentrated energy in the mouse."],
        ["Access.", "Miniaturization allowed implantation beneath the skin.", "Central and peripheral targets could be reached."],
    ], ["Montgomery 2015"]),
]

# speaker notes: title sentence, one group per paragraph (scaffolding/RULES.md transcript), 150-420 words in all
for _ins in inserts:
    _ins["notes"] = [_ins["notes"][0]] + [
        [f"Explanation {_i + 1}.", *(plain(p_).split(". ", 1))] for _i, p_ in enumerate(_ins["paragraphs"])
    ] + _ins["notes"][1:]

spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(_body.body)} body slides rewritten, {len(inserts)} scaffold slides")
