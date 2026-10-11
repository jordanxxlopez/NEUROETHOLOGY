"""Scaffold spec for Lecture 32 (Drive deck Neuroethology_Lecture32_FA2026.pptx). Body rewrites are in body_L32.py."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L32 as _body  # noqa: E402


def ins(after, title, paragraphs, citation, notes, refs):
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


inserts = [
    ins(4, "Fink–Heimer staining marks downstream terminals", [
        "**Fink–Heimer staining** reveals degenerating fibers and terminals after a neuron is damaged. Because the stain marks only the processes that lost their cell body, it shows where a lesioned population sends its axons. Nottebohm and colleagues used this stain to follow the output of song nuclei in adult canaries.",
        "After lesions of the region historically called HVc, degenerating fibers were found in RA. Degeneration in RA then pointed toward descending pathways that reach vocal motor structures in the brainstem. Each labeled tract starts at a known lesion and ends at a known target.",
        "The anatomy therefore supplies a direction for the song pathway, independent of any change in the song itself. A lesion that disrupts song and a lesion that produces degeneration in RA point to the same chain of nuclei, which makes the pathway easier to trace.",
    ], "Nottebohm et al. (1976)", [
        "Degeneration staining follows the output of a lesioned region.",
        ["Stain.", "Fink–Heimer staining reveals degenerating fibers and terminals.", "Only processes that lost their cell body are labeled."],
        ["Lesion.", "The lesions targeted the region historically called HVc.", "Each lesion has a known starting point."],
        ["Target.", "Degeneration appeared in RA.", "RA receives the output of HVc."],
        ["Descending output.", "RA connects to descending pathways.", "These pathways reach the vocal motor structures."],
        ["Combined evidence.", "Lesion location and degeneration pattern agree.", "Both point to the same chain of nuclei."],
        ["Meaning.", "Anatomy gives the direction of the pathway.", "The direction is independent of the song changes."],
    ], ["Nottebohm 1976"]),
    ins(6, "Single-cell filling reveals complete local arbors", [
        "**Single-cell filling** labels one neuron completely so that its dendrites and axons can be traced in full. Benezra and colleagues filled identified HVC neurons after labeling them through their output targets. A filled cell therefore carries both its anatomy and the target that defines it.",
        "Two-photon imaging resolved the fine branches of these cells inside living tissue. The reconstructions were then built from serial sections, so each arbor could be followed across the boundaries of the slices. The complete branching pattern is visible only when a single cell is isolated from its neighbors.",
        "A single reconstructed neuron can therefore be compared with the population of neurons that share its target. The filled cell links a projection identity to a measurable shape. Its branches tell the reader where that neuron's information can travel within HVC.",
    ], "Benezra et al. (2018)", [
        "Single-cell filling connects projection identity to structure.",
        ["Filling.", "One neuron is labeled completely.", "Its dendrites and axons are then traced."],
        ["Targeting.", "Cells were labeled through their output targets.", "The label identifies the projection."],
        ["Imaging.", "Two-photon imaging resolved fine branches.", "The fine branches are often hidden in dense labeling."],
        ["Reconstruction.", "Serial sections allow tracing across slices.", "Each arbor is followed from start to end."],
        ["Isolation.", "A single cell is separated from its neighbors.", "Its branching pattern can be read clearly."],
        ["Meaning.", "Each reconstruction gives one neuron's full shape.", "The shape can be compared across the population."],
    ], ["Benezra 2018"]),
    ins(10, "Local axons vary within the RA-projecting population", [
        "A **local axon collateral** is a branch that stays within the same nucleus as its parent cell. Benezra and colleagues measured these branches in HVC(RA) neurons, which send their long axons to RA. The branches show how much each cell contacts the tissue around it.",
        "Some HVC(RA) neurons kept most of their local branches close to the cell body. Others spread their branches across a larger part of HVC. Both patterns appeared among cells that share the same long-range target, so the target alone does not fix the local arbor.",
        "Local branches therefore give each RA-projecting cell its own position in the HVC network. A neuron with broad local branches can influence more of the surrounding tissue before its signal reaches RA.",
    ], "Benezra et al. (2018)", [
        "Local collaterals differ among cells with the same target.",
        ["Definition.", "A local collateral stays within HVC.", "It is a branch of the same cell's axon."],
        ["Target.", "HVC(RA) neurons send their long axons to RA.", "Those long axons define the projection."],
        ["Local arbor.", "Some cells keep branches near the cell body.", "Others spread branches across HVC."],
        ["Variation.", "The variation appears within one projection class.", "The target alone does not set the arbor."],
        ["Network position.", "Local branches place each cell in the HVC network.", "Each cell contacts a different amount of tissue."],
        ["Meaning.", "Local output is a property of each cell.", "It adds to the long-range projection."],
    ], ["Benezra 2018"]),
    ins(16, "Temperature sets the width and rate of RA spikes", [
        "**Spike half-width** is the duration of an action potential measured at half its peak height. Zemel and colleagues measured this value in identified RA projection neurons at about 40 °C, close to the body temperature of the bird. The spikes were very brief, with a half-width near 0.18 ms.",
        "The same neurons fired about fourfold faster at this temperature than at room temperature. Depolarizing current evoked sustained trains of rapid spikes, so the neurons had the capacity to fire quickly when driven. The comparison across temperatures is what makes the spike width meaningful.",
        "Temperature therefore changes the speed of the motor neuron's output. Spike width and firing rate both depend on conditions, so the same cell can have a different timing profile in a warm slice and in a cool one.",
    ], "Zemel et al. (2021)", [
        "Temperature changes both spike width and firing rate.",
        ["Half-width.", "Spike half-width is the duration at half the peak height.", "The spikes measured here were very brief."],
        ["Temperature.", "The recordings were made at about 40 °C.", "This is close to the bird's body temperature."],
        ["Value.", "The half-width was about 0.18 ms.", "This is a fast spike."],
        ["Rate.", "Spontaneous firing was about fourfold faster than at room temperature.", "The difference is large."],
        ["Trains.", "Depolarizing current evoked sustained rapid spikes.", "The neurons could fire quickly when driven."],
        ["Meaning.", "Temperature changes the timing profile of the same cell.", "Spike timing depends on conditions."],
    ], ["Zemel 2021"]),
    ins(19, "Resurgent current rises with age in males", [
        "A **resurgent sodium current** is a current that reappears as the membrane repolarizes after a strong depolarization. Zemel and colleagues measured it alongside the transient sodium current in the same RA neurons. Comparing the two currents within one sweep separates the resurgent component from the overall sodium current.",
        "The recordings covered birds at 20, 35 and 50 days after hatching and adult males. Resurgent current increased with age, including after normalization to the transient current. The result shows that the increase is specific to the resurgent component rather than a general rise in all sodium current.",
        "The developmental change therefore follows the maturation of the neuron's sodium channels. Because the current grows over the same period as song development, it is a candidate contributor to the faster firing of mature motor neurons.",
    ], "Zemel et al. (2021)", [
        "Resurgent current grows with age in male RA neurons.",
        ["Current.", "Resurgent current appears as the membrane repolarizes.", "It is distinct from the transient current."],
        ["Comparison.", "Both currents were measured in the same sweep.", "The comparison isolates the resurgent component."],
        ["Ages.", "Birds were recorded at 20, 35 and 50 days and in adulthood.", "The same voltage protocol was used at each age."],
        ["Normalization.", "The increase persisted after normalizing to the transient current.", "The change is specific to the resurgent component."],
        ["Development.", "The increase follows the maturation of the sodium channels.", "The current grows across the song-learning period."],
        ["Meaning.", "Resurgent current is a candidate for faster firing.", "It may help mature neurons fire quickly."],
    ], ["Zemel 2021"]),
    ins(22, "Dynamic clamp moves resurgent current into real neurons", [
        "**Dynamic clamp** is a recording method that calculates a current from the membrane voltage in real time and injects it into a neuron. Zemel and colleagues used it to add a resurgent-current component to juvenile RA neurons. The same method subtracted a corresponding component from adult neurons.",
        "Adding the component increased the firing frequency of juvenile neurons. Subtracting it reduced the firing of adult neurons. Because the same cell was tested with the intervention off and on, the immediate effect of the current could be separated from differences between cells of different ages.",
        "This manipulation tests whether resurgent current contributes to firing, rather than only correlating with it. The injected conductance was calibrated against the measured sodium-current kinetics, so the added current matches the one recorded in the cells.",
    ], "Zemel et al. (2021)", [
        "Dynamic clamp tests the effect of a current directly.",
        ["Method.", "Dynamic clamp computes a current from the voltage in real time.", "The current is injected into a real neuron."],
        ["Juvenile.", "A resurgent-current component was added to juvenile neurons.", "Firing frequency increased."],
        ["Adult.", "The component was subtracted from adult neurons.", "Firing decreased."],
        ["Within-cell design.", "The same cell was tested with the intervention off and on.", "This isolates the immediate effect."],
        ["Calibration.", "The conductance was matched to the measured kinetics.", "The added current resembles the recorded current."],
        ["Meaning.", "The current contributes to firing rather than only correlating with it.", "The experiment is a causal test."],
    ], ["Zemel 2021"]),
    ins(25, "Apamin changes spike timing without changing mean rate", [
        "**Apamin** is a toxin that blocks SK channels, which are calcium-activated potassium channels. Hou and colleagues applied it to RA projection neurons and recorded their spontaneous spikes before and after the drug. The same cells were compared in both conditions.",
        "The interval between successive spikes became more variable after apamin. The average firing rate changed little, so the regularity of the spike train changed independently of its speed. A neuron can therefore fire at the same rate with more or less reproducible timing.",
        "SK channels help set the timing of spikes by shaping the return toward threshold after each action potential. Blocking them makes the spike train less regular, which shows that timing precision is a separate property from firing rate.",
    ], "Hou et al. (2012)", [
        "Apamin separates spike timing from firing rate.",
        ["Drug.", "Apamin blocks SK channels.", "SK channels are calcium-activated potassium channels."],
        ["Design.", "The same RA neurons were recorded before and after the drug.", "Spontaneous spike trains were compared."],
        ["Interval.", "Intervals between spikes became more variable.", "The variation was the main effect."],
        ["Rate.", "The average firing rate changed little.", "Rate and regularity are separate properties."],
        ["Threshold.", "SK channels shape the return toward threshold.", "This shapes the timing of the next spike."],
        ["Meaning.", "Regularity and rate can be changed independently.", "Each property needs its own measure."],
    ], ["Hou 2012"]),
    ins(28, "Dopamine raises RA neuronal firing reversibly", [
        "**Dopamine** is a neuromodulator that changes the excitability of neurons through receptor signaling. Liao and colleagues applied dopamine to adult RA projection neurons while controlling the injected current. The same cell was recorded before, during and after the drug.",
        "Firing rose during the dopamine application and returned toward baseline after the wash. The membrane potential also shifted toward a less negative value. The reversal within each cell shows that the effect came from the drug rather than from a difference between neurons.",
        "The depolarization makes RA neurons closer to firing for the same input. This change in excitability is a candidate mechanism for how dopamine alters the output of the motor nucleus during song-related activity.",
    ], "Liao et al. (2013)", [
        "Dopamine increases the excitability of RA neurons.",
        ["Preparation.", "Adult male RA projection neurons were recorded.", "The injected current was controlled."],
        ["Application.", "Dopamine was applied at 50 µM.", "The drug was applied to the bath."],
        ["Firing.", "Firing rose during the application.", "The rise was about 1.38 times baseline."],
        ["Voltage.", "The membrane potential became less negative.", "The neuron moved closer to threshold."],
        ["Reversal.", "The effect reversed after washout.", "The same cell returned toward baseline."],
        ["Meaning.", "Dopamine makes RA neurons more likely to fire.", "The effect is a candidate for song-related modulation."],
    ], ["Liao 2013"]),
    ins(31, "D1-like and D2-like agonists act differently on RA", [
        "A **D1-like receptor** and a **D2-like receptor** are two classes of dopamine receptor that act through different signaling pathways. Liao and colleagues compared the effect of a D1-like agonist with that of a D2-like agonist on RA neurons. The two drugs were tested on the same kind of cell.",
        "The D2-like agonist quinpirole did not reproduce the strong increase in excitability produced by dopamine. The D1-like agonist did produce a comparable increase. The two agonists therefore produced different effects in the same preparation.",
        "The receptor class determines whether dopamine excites RA neurons. The result constrains how dopamine acts on the motor nucleus, because a single transmitter can produce different responses through different receptors.",
    ], "Liao et al. (2013)", [
        "Receptor class determines how dopamine acts on RA.",
        ["Receptor classes.", "D1-like and D2-like receptors signal through different pathways.", "They are pharmacologically distinct."],
        ["Agonists.", "Each class was tested with its own agonist.", "The agonists were applied to RA neurons."],
        ["D2-like result.", "Quinpirole did not produce the strong increase.", "The effect was weaker than that of dopamine."],
        ["D1-like result.", "The D1-like agonist produced a comparable increase.", "This matches the effect of dopamine."],
        ["Comparison.", "The two classes differ in their effect.", "The difference is what the experiment tests."],
        ["Meaning.", "One transmitter can act through several receptor types.", "The receptor type controls the response."],
    ], ["Liao 2013"]),
    ins(33, "Stronger HVC synapses increase during development", [
        "A **single-fiber response** is a current evoked by activating one input fiber at a time. Garst-Orozco and colleagues used weak stimulation to isolate these responses on RA neurons. Stronger stimulation was used to recruit the full population of inputs, so the two measures can be compared.",
        "Median single-fiber HVC currents rose from about 23 pA in subsong birds to about 60 pA in adults. The estimated number of recruited inputs first increased and then declined. The synapses therefore grew stronger while the number of active inputs was refined.",
        "This pattern describes refinement rather than a uniform increase in every aspect of connectivity. The strengthening of individual HVC inputs can change how RA converts HVC activity into motor output over the course of development.",
    ], "Garst-Orozco et al. (2014)", [
        "HVC inputs strengthen and are then refined.",
        ["Stimulation.", "Weak stimulation isolates single-fiber responses.", "Stronger stimulation recruits the whole input population."],
        ["Single fiber.", "A single fiber produces a consistent current.", "This is the basic unit of the measurement."],
        ["Strength.", "Median currents rose from about 23 pA to 60 pA.", "Subsong and adult birds were compared."],
        ["Number.", "The number of recruited inputs first increased.", "Later in development the number declined."],
        ["Refinement.", "Connectivity was refined rather than uniformly increased.", "Some inputs were strengthened and others reduced."],
        ["Meaning.", "Strengthening changes how HVC drives RA.", "Development shapes which inputs are active."],
    ], ["Garst-Orozco 2014"]),
    ins(36, "Stage comparisons separate intrinsic and synaptic change", [
        "**Input-to-firing gain** is the change in output firing for a given increase in input current. Garst-Orozco and colleagues measured this gain in RA neurons across subsong, plastic-song and adult stages. The gain and spike-frequency adaptation were broadly similar across these groups.",
        "Zemel and colleagues instead tested younger 20-day birds and isolated sodium-current components. They reported a pronounced maturation of resurgent current and spike properties over the same developmental period. The two studies used different ages and different measurements, so their results address different questions.",
        "Firing responses that look stable across one age range do not contradict an earlier change in a specific ion current. Intrinsic change can be visible in one measure and absent in another, so the developmental account depends on which property is measured.",
    ], "Garst-Orozco et al. (2014)", [
        "Different measures can reveal different developmental changes.",
        ["Gain.", "Input-to-firing gain relates input current to firing rate.", "It is one measure of excitability."],
        ["Stages.", "Subsong, plastic-song and adult stages were compared.", "The same stimulus was used across stages."],
        ["Adaptation.", "Spike-frequency adaptation was similar across the stages.", "This is a second firing property."],
        ["Zemel comparison.", "Younger 20-day birds were included.", "Sodium-current components were isolated."],
        ["Maturation.", "Resurgent current and spike properties changed strongly.", "The change followed the developmental window."],
        ["Meaning.", "Different properties change at different times.", "The developmental account depends on the property measured."],
    ], ["Garst-Orozco 2014", "Zemel 2021"]),
    ins(39, "Tracers show LMAN output to Area X and RA", [
        "A **retrograde tracer** labels neurons that project toward an injection site, whereas an **anterograde tracer** labels the axons and terminals that leave a site. Vates and Nottebohm used both kinds of tracer to map connections between song nuclei. The two directions together show which cells send a projection and where it ends.",
        "Injections associated with Area X and RA labeled neurons and terminal fields in LMAN. These findings supported an output route from LMAN to both the basal ganglia region and the motor nucleus. The circuit therefore extends beyond the one-way chain from HVC to the vocal organ.",
        "Projections in both directions make the song circuit more interconnected than a single chain. A forebrain nucleus can send information to the motor pathway as well as to the basal ganglia, which shapes how the song system can be studied as a network.",
    ], "Vates & Nottebohm (1995)", [
        "Two tracer directions reveal the connections in both directions.",
        ["Retrograde.", "A retrograde tracer labels neurons projecting to the injection site.", "It identifies the cells that send the projection."],
        ["Anterograde.", "An anterograde tracer labels the axons and terminals downstream.", "It shows where the projection ends."],
        ["Injections.", "Injections were placed in Area X and RA.", "Labeled neurons and terminals appeared in LMAN."],
        ["Output route.", "LMAN projects to the basal ganglia region and the motor nucleus.", "This route is in addition to the HVC chain."],
        ["Combined directions.", "Each direction checks the other.", "The circuit map is less ambiguous."],
        ["Meaning.", "The song system is a network with several routes.", "LMAN is part of the output side of the circuit."],
    ], ["Vates 1995"]),
    ins(41, "Playback trials compare self-song with control sounds", [
        "A **playback** experiment presents a recorded sound to an animal while its neural responses are recorded. Doupe played the bird's own song and comparison sounds while recording LMAN spikes in anesthetized adult zebra finches. The responses to each stimulus were compared trial by trial.",
        "Many neurons responded strongly to the bird's own song but weakly to other conspecific songs and simple sounds. Amplitude-modulated noise and tones served as controls that match the sound energy of the songs. A response that was only a generic reaction to loudness would appear with these controls as well.",
        "The selective response therefore links an anterior forebrain nucleus to the acoustic structure of the bird's own learned song. The effect was measured under anesthesia during playback, so it describes the sensory response of the neurons rather than their behavior during singing.",
    ], "Doupe (1997)", [
        "Playback responses separate song-specific activity from generic sound energy.",
        ["Playback.", "A recorded sound is played while spikes are recorded.", "The response to each sound is compared."],
        ["Stimuli.", "The bird's own song was compared with other songs.", "Simple sounds served as additional comparisons."],
        ["Selectivity.", "Many neurons responded strongly to self-song.", "The response to other songs was weaker."],
        ["Controls.", "Amplitude-modulated noise and tones match the sound energy.", "These controls test for a generic response."],
        ["Anesthesia.", "The recordings were made in anesthetized adult birds.", "The condition limits the interpretation."],
        ["Meaning.", "LMAN responds to the acoustic structure of learned song.", "The response is measured during playback."],
    ], ["Doupe 1997", "Gale 2010a"]),
    ins(44, "Recorded midbrain cells are identified by their labeling", [
        "A **juxtacellular label** is a dye delivered to a single recorded neuron after its spikes have been measured. Gale and Perkel combined this label with immunostaining for tyrosine hydroxylase, an enzyme involved in catecholamine synthesis. Marker-positive cells provide a check on the identity assigned from firing properties.",
        "The recordings were made in the substantia nigra pars compacta and the ventral tegmental area, SNc/VTA. Cells that were classified by their spike waveform were then checked against the marker. The fluorescent micrographs carry 20 µm scale bars, so the recorded cell and its tissue can be located together.",
        "A waveform classification gives a provisional identity, and the labeled cell confirms or revises it. The combination of recording and staining links a cell's firing pattern to its neurochemical identity, which gives a stronger identification than the waveform alone.",
    ], "Gale & Perkel (2010a)", [
        "Juxtacellular labeling confirms the identity of a recorded cell.",
        ["Label.", "A dye is delivered to the recorded neuron.", "The cell is identified after its spikes are measured."],
        ["Marker.", "Tyrosine hydroxylase marks catecholamine-synthesizing cells.", "Immunostaining reveals the marker."],
        ["Regions.", "The recordings came from SNc and VTA.", "These regions supply dopaminergic input to Area X."],
        ["Waveform.", "Cells were first classified by spike waveform.", "The waveform gives a provisional identity."],
        ["Check.", "Marker-positive cells were compared with the classification.", "The check confirms or revises the identity."],
        ["Meaning.", "Firing pattern is linked to neurochemical identity.", "Both measures are needed for the identification."],
    ], ["Gale 2010a"]),
]

EXTRA_NOTES = [
    ["Source values.", "The published values and recording conditions come from the original paper.", "Each value is reported with the scale or condition used in the source."],
    ["Why the measure matters.", "The result separates the measured property from the mechanism that produces it.", "The comparison stays within the same cells or the same birds."],
    ["Interpretation.", "Each result is read within the preparation and the age group that produced it.", "The claim is restricted to the measured cells and conditions."],
]
APPEND_P1 = {
    16: " The temperature of the recording is part of the measurement, so the value applies to warm slices.",
    31: " Each agonist was tested under the same recording conditions.",
}
APPEND_P3 = {
    10: " The branching pattern of each cell is therefore recorded as an individual property.",
    16: " Each recording therefore reflects the temperature at which it was made.",
    25: " Each spike train is compared with itself before and after the drug.",
    28: " The effect is therefore a property of the cells in this preparation.",
    31: " The receptor comparison uses the D1-like result as its reference.",
    4: " Each stained tract can be followed back to a lesioned population.",
    19: " The developmental result is therefore a measurement of the current itself.",
    22: " Each manipulation is tested on the same cell before and after the intervention.",
    33: " Each measurement is kept separate so that connection strength is not confused with input number.",
    36: " The comparison across studies depends on which property each study measured.",
    41: " The selective response is a property of the neurons, not of the playback sound alone.",
}
for _ins in inserts:
    _ins["notes"] = [_ins["notes"][0]] + _ins["notes"][1:] + EXTRA_NOTES
    if _ins["after"] in APPEND_P1:
        _ins["paragraphs"][0] = _ins["paragraphs"][0] + APPEND_P1[_ins["after"]]
    if _ins["after"] in APPEND_P3:
        _ins["paragraphs"][2] = _ins["paragraphs"][2] + APPEND_P3[_ins["after"]]
spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(_body.body)} body slides rewritten, {len(inserts)} scaffold slides")
