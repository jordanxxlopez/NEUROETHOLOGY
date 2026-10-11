"""Scaffold spec for Lecture 35 (Drive deck Neuroethology_Lecture35_FA2026.pptx). Body rewrites are in body_L35.py."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L35 as _body  # noqa: E402
import L35_text as _txt  # noqa: E402


def ins(after, title, paragraphs, citation, notes, refs):
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


inserts = [
    ins(3, "Field recordings place events on a shared clock", [
        "A bath electrode records the voltage changes that a moving crayfish produces in the surrounding water. Because the animal is free to move, its activity can be recorded during natural behavior rather than in a restrained preparation. Each recording is kept on a clock shared with the video.",
        "High-speed video sampled movement every 5 ms, which resolves the fast abdominal movements of escape and grappling. Matching each frame to the electrical record places every event on the same timeline. Each escape or grappling bout is then read in terms of both its movement and its neural activity.",
        "Comparing the bath signal with implanted electrodes in the same animal confirmed that the two signals reflect the same activity. This check gives the bath recording a known basis, so its events can be interpreted with confidence in later analyses.",
    ], "Herberholz et al. (2001)", [
        "Bath recordings and video share one clock.",
        ["Recording.", "Field potentials are measured in the water.", "The animal moves freely during recording."],
        ["Video.", "Movement is sampled every 5 ms.", "Each frame is matched to the electrical record."],
        ["Check.", "Implanted electrodes confirmed the bath signal.", "Both reflect the same activity."],
        ["Meaning.", "Events can be read as movement and neural activity together.", "The timeline is shared across all bouts."],
    ], ["Herberholz 2001"]),
    ins(6, "Serotonin's effect depends on a timed infusion", [
        "Infusion timing matters when a drug is delivered to a freely moving animal. Huber and colleagues began each infusion after rank had formed, so the effect of serotonin is measured in animals whose social status is already established. The schedule is the same for every pair.",
        "Each pair served as its own control, with 30 min of saline before 60 min of serotonin delivery. Estimated circulating serotonin approached 10 µM during the infusion. Fight duration and intensity increased while the drug was delivered, and the increase is measured against the saline period.",
        "The infusion design isolates serotonin's effect on an established subordinate. The saline baseline and the drug period belong to the same animals, so each pair's change can be attributed to the drug. Each fight is compared with that pair's own preinfusion level.",
    ], "Huber et al. (1997)", [
        "A timed infusion isolates the effect of serotonin.",
        ["Schedule.", "Infusion began after rank formation.", "The schedule was the same for each pair."],
        ["Control.", "Each pair served as its own control.", "Saline came before serotonin."],
        ["Concentration.", "Estimated serotonin approached 10 µM.", "Fight duration increased during delivery."],
        ["Meaning.", "The drug effect is measured within each pair.", "The baseline belongs to the same animals."],
    ], ["Huber 1997"]),
    ins(9, "Nongiant escape dominates social encounters", [
        "Nongiant escape uses interneurons and motor neurons without firing the giant command pathways. Its movements are more variable than giant escapes, and it also drives repeated swimming tail flips after an initial escape. This pathway makes up most of the defensive movements in encounters.",
        "Across 30 min of juvenile encounters, the new subordinate produced extensive nongiant escape and swimming. The giant interneuron LG fired only once across the paired encounters, when an opponent struck the abdomen directly. Such strikes are rare during the rest of the contest.",
        "Frequent defensive escape therefore depends mainly on nongiant circuitry. Each escape is classified by the pathway it used, and the classification follows the recorded activity of the giant and nongiant neurons. Each classification is checked against the timing of the recorded giant-neuron activity.",
    ], "Herberholz et al. (2001)", [
        "Most social escapes use nongiant circuitry.",
        ["Nongiant escape.", "It uses interneurons and motor neurons.", "It produces variable movements."],
        ["Swimming.", "Repeated swimming tail flips follow the escape.", "The nongiant pathway drives them."],
        ["LG activity.", "LG fired once across the encounters.", "The strike was the only trigger."],
        ["Meaning.", "Defensive escape relies on nongiant neurons.", "Each escape is classified by its pathway."],
    ], ["Herberholz 2001"]),
    ins(12, "Two synapses link sensory input to LG", [
        "A monosynaptic pathway passes its signal through one synapse, whereas a disynaptic pathway passes through two. The number of synapses sets the delay and the shape of the response in LG. Each pathway is identified by how many synapses separate the sensory input from the giant neuron.",
        "Edwards and colleagues combined identified-cell recordings with stained-neuron reconstructions in adult crayfish. Interneuron A overlaps the LG dendritic region and contributes to the sensory excitation. Nerve shocks produce an early α depolarization and a later β component.",
        "The early and late components of the response show which pathway is active at each latency. The α component follows the direct input, while the β component follows the recruitment of interneurons. Each EPSP is attributed to its pathway by its timing.",
    ], "Edwards et al. (1991)", [
        "Two pathways supply sensory input to LG.",
        ["Synapses.", "A synapse transfers a signal between neurons.", "Monosynaptic means one synapse, disynaptic two."],
        ["Reconstruction.", "Identified cells were recorded and stained.", "Interneuron A overlaps the LG dendrites."],
        ["Components.", "The α component is early and the β component is late.", "Each follows a different pathway."],
        ["Meaning.", "Latency reveals which pathway is active.", "Each EPSP is assigned to its pathway."],
    ], ["Edwards 1991"]),
    ins(15, "Descending input suppresses the sensory response", [
        "Tonic inhibition is a sustained suppression of a circuit, distinct from the brief inhibition that accompanies one response. A descending input travels from more anterior nervous-system regions toward abdominal circuits, and it can hold the escape pathway in check during rest.",
        "Vu and colleagues interrupted transmission through a thoracic-abdominal connective with sucrose and then severed it. Sensory-evoked LG EPSPs increased during the reversible block. After severing, another sucrose application produced little additional increase, so the descending influence had already been removed.",
        "The increase in EPSPs during the block shows that descending input suppresses the sensory pathway to LG. Voltage responses were compared within the same preparation at each stage, which identifies a selective route by which escape is restrained from above.",
    ], "Vu et al. (1993)", [
        "Descending input holds back the sensory response.",
        ["Tonic inhibition.", "Sustained suppression is distinct from a brief response.", "The input travels from anterior regions."],
        ["Interruption.", "Sucrose blocked the connective reversibly.", "Severing removed the descending input."],
        ["EPSPs.", "Sensory EPSPs increased during the block.", "Severing added little further increase."],
        ["Meaning.", "Escape is restrained from above.", "The route is selective."],
    ], ["Vu 1993"]),
    ins(18, "Concentration and onset set the sign of serotonin", [
        "Serotonin concentration, onset rate and exposure duration can each be changed separately. Teshiba and colleagues varied all three in crayfish isolated for at least two weeks, so the contribution of each factor can be measured on its own.",
        "Rapid high-concentration exposure inhibited sensory EPSPs, whereas lower concentrations facilitated them. Juvenile bath concentrations were 5 µM for the low condition and 100 µM for the high condition. Adult arterial concentrations differed because the delivery route differed.",
        "The measured sign depends on the preparation and on the exposure schedule. Concentration, onset and duration interact, so the same drug can inhibit or facilitate the same synapse. Each result is read together with its delivery schedule.",
    ], "Teshiba et al. (2001)", [
        "Concentration, onset and duration set the sign of the effect.",
        ["Factors.", "Three factors were varied separately.", "Each contribution can be compared."],
        ["Concentration.", "High rapid exposure inhibited EPSPs.", "Lower concentrations facilitated them."],
        ["Routes.", "Bath and arterial concentrations differed.", "Delivery shapes the dose at the nerve."],
        ["Meaning.", "The same drug can inhibit or facilitate.", "Each result is read with its schedule."],
    ], ["Teshiba 2001"]),
    ins(21, "Serotonin's sign depends on social history", [
        "A **subthreshold input** evokes a response without a spike, whereas a **suprathreshold input** is sufficient to initiate firing. Yeh and colleagues tested a range of sensory shock strengths on identified LG neurons, so each animal's firing threshold can be located on a curve.",
        "After 45 min of 50 µM serotonin, LG EPSPs increased across stimulus levels in isolates and dominants and decreased in established subordinates. Representative stimulus-response relations changed by about +117%, +39% and −37%, respectively. These values come from individual preparations.",
        "The stimulus needed to fire LG is shifted in opposite directions by serotonin, depending on social history. The same drug can lower the firing threshold in one animal and raise it in another, so each stimulus-response relation is compared with its own baseline.",
    ], "Yeh et al. (1997)", [
        "The same serotonin dose shifts LG in opposite directions.",
        ["Inputs.", "Subthreshold input does not fire LG.", "Suprathreshold input does."],
        ["Exposure.", "Serotonin was applied at 50 µM for 45 min.", "Stimulus strengths were tested across a range."],
        ["Changes.", "Isolates and dominants increased, subordinates decreased.", "The values come from individual preparations."],
        ["Meaning.", "The firing threshold moves in opposite directions.", "Social history sets the direction."],
    ], ["Yeh 1997"]),
    ins(24, "Promotion gradually reverses a subordinate response", [
        "Yeh and colleagues paired former subordinates with one another, which allowed one member to acquire dominant status. This manipulation tests whether a retained inhibitory serotonin response changes after a new social relationship develops, and each animal's rank is recorded at the same time points.",
        "The newly dominant animal's LG response shifted gradually from serotonin-induced inhibition toward facilitation over about two weeks. The comparison set these animals against new dominants generated from isolates, which began with a facilitatory response from the outset.",
        "Promotion therefore changes an experienced subordinate's cellular modulation over time. The change follows the new social role, and each response is compared with the response of new dominants generated from isolates.",
    ], "Yeh et al. (1997)", [
        "Promotion gradually reverses the inhibitory response.",
        ["Pairing.", "Former subordinates were paired together.", "One member became dominant."],
        ["Time course.", "The LG response shifted over about two weeks.", "Inhibition gave way to facilitation."],
        ["Comparison.", "New dominants from isolates were the reference.", "They began with facilitation."],
        ["Meaning.", "Social role can change cellular modulation.", "The change follows the new role."],
    ], ["Yeh 1997"]),
    ins(27, "A receptor map shows candidate cellular sites", [
        "Immunocytochemistry uses antibodies to locate a target molecule in cells. Spitzer and colleagues mapped a putative crustacean type-1 serotonin receptor, designated 5-HT1crust, with fluorescence microscopy, and they compared the receptor labeling with serotonin labeling.",
        "Receptor-associated puncta occurred around neuronal cell bodies and within their cytoplasm. In cluster 10 brain cells, optical sections separated the labeled material from nuclear staining. Antibody preabsorption controls reduced the specific labeling pattern, which confirms that the antibody detects its target.",
        "The map identifies candidate locations where the receptor could act on serotonergic signals. Each labeled region is compared with the nuclear counterstain and with the control sections, which points to the cells most likely to carry the receptor.",
    ], "Spitzer et al. (2005)", [
        "A receptor map points to candidate cells.",
        ["Method.", "Antibodies locate the receptor in tissue.", "Serotonin labeling is compared with it."],
        ["Labeling.", "Puncta surround cell bodies and fill cytoplasm.", "Nuclear staining is separated optically."],
        ["Controls.", "Preabsorption reduced the specific labeling.", "The antibody detects its target."],
        ["Meaning.", "Candidate cells are identified by the map.", "Controls keep the reading specific."],
    ], ["Spitzer 2005"]),
    ins(30, "Cloned type-2 receptors activate inositol signaling", [
        "Spitzer and colleagues expressed the crayfish 5-HT2β receptor in HEK cells, a mammalian cell line used to test an introduced protein. They measured inositol phosphates, intracellular products generated when phospholipase C cleaves membrane phosphoinositides.",
        "Serotonin increased inositol-phosphate accumulation in receptor-expressing cells, with a half-maximal effective concentration near 270 nM. Matched non-transfected cells produced no comparable response. Other tested monoamines required much higher concentrations or had little activity.",
        "The assay links the type-2 receptor to a messenger pathway that is distinct from cAMP. Serotonin is the most potent ligand among those tested, and each response is compared with the matched control cells. The receptor signal is read as its own pathway, separate from the cAMP route.",
    ], "Spitzer et al. (2008)", [
        "The type-2 receptor activates a distinct messenger.",
        ["Expression.", "The receptor was expressed in HEK cells.", "HEK cells are a mammalian test line."],
        ["Readout.", "Inositol phosphates were measured.", "They come from phospholipase C."],
        ["Potency.", "Serotonin was the most potent ligand.", "Its half-maximal concentration was near 270 nM."],
        ["Meaning.", "Signaling differs from the type-1 cAMP route.", "Controls keep the effect specific."],
    ], ["Spitzer 2008"]),
    ins(33, "A cyclase block removes serotonin's facilitation", [
        "**Adenylyl cyclase** produces cAMP, so inhibiting this enzyme tests whether serotonin's facilitation requires cyclic-nucleotide synthesis. Araki and colleagues pretreated isolated abdominal preparations with 100 µM SQ22536 before adding 10 µM serotonin, applying the inhibitor before the drug in every preparation.",
        "With serotonin alone, the median stimulus number before habituation was 12.5, compared with 3 in controls. With cyclase inhibition and serotonin together, the median was 6, and later response loss approached the control pattern. The inhibitor alone did not change the initial shock threshold.",
        "This interaction supports a serotonin action that runs through cAMP synthesis. Blocking the enzyme removes most of the extra resistance to habituation that serotonin produces, and each preparation is compared with its own control.",
    ], "Araki et al. (2005)", [
        "The cyclase block removes serotonin's effect on habituation.",
        ["Inhibitor.", "SQ22536 blocks adenylyl cyclase.", "It was applied before serotonin."],
        ["Serotonin alone.", "The median stimulus number was 12.5.", "Controls had a median of 3."],
        ["With block.", "The median fell to 6 with inhibition.", "Response loss approached the control pattern."],
        ["Meaning.", "Serotonin's effect requires cAMP synthesis.", "Each preparation is compared with its control."],
    ], ["Araki 2005"]),
    ins(36, "Long exposure leaves facilitation after washout", [
        "Exposure duration changes how long serotonergic modulation persists. Teshiba and colleagues compared brief application, of approximately 10 min, with longer exposures near 45 min. They then followed sensory EPSPs during a saline washout, so each exposure length is tracked through recovery.",
        "Brief high exposure produced inhibition that reversed relatively rapidly. Longer exposure was followed by persistent facilitation, even after an inhibitory phase during rapid high delivery. Facilitated responses remained above baseline during the 30 min wash comparison and could persist for hours.",
        "The result separates the immediate sign of the response during drug presence from its sign after the drug is removed. Each recording is compared with the baseline of its own preparation, so duration and washout are read as separate features.",
    ], "Teshiba et al. (2001)", [
        "Long exposure leaves facilitation after washout.",
        ["Duration.", "Brief exposure lasted about 10 min.", "Longer exposure lasted near 45 min."],
        ["Brief exposure.", "Inhibition reversed relatively rapidly.", "Recovery was fast."],
        ["Long exposure.", "Facilitation persisted after the inhibitory phase.", "It remained above baseline."],
        ["Meaning.", "Sign during presence differs from sign after removal.", "Each preparation is its own baseline."],
    ], ["Teshiba 2001"]),
    ins(39, "Status persists in isolated ganglia", [
        "An **isolated ganglion** is a local concentration of neuronal cell bodies and their connections, removed from the anterior centers. Issa and colleagues isolated thoracic and abdominal ganglia with walking-leg nerves, so the local circuit can be tested without descending input.",
        "Electrical stimulation of an abdominal sensory nerve retained the status-related pattern. Preparations from isolates and dominants favored ipsilateral depressor activity, whereas subordinate preparations produced more symmetric responses. Each preparation is compared before and after circuit isolation.",
        "The status-related organization therefore persists in local circuits after the anterior centers are removed. Each isolated ganglion carries the pattern of its animal's social history, which identifies the local circuit as one site of the status effect.",
    ], "Issa et al. (2012)", [
        "The status pattern persists in isolated ganglia.",
        ["Isolation.", "Ganglia were removed with their walking-leg nerves.", "Descending input was excluded."],
        ["Stimulation.", "Abdominal sensory nerve stimulation retained the pattern.", "Status shaped the depressor response."],
        ["Symmetry.", "Subordinates produced more symmetric responses.", "Isolates and dominants favored one side."],
        ["Meaning.", "Local circuits carry the status effect.", "Each ganglion keeps its animal's history."],
    ], ["Issa 2012"]),
    ins(42, "Serotonin cells split motor units in opposite directions", [
        "Bacqué-Cazenave and colleagues stimulated one identified serotonin neuron in the first abdominal ganglion of isolated adult crayfish. Current pulses inside the cell drove it, and the team recorded individual walking-leg motor units and motor-neuron voltage at the same time.",
        "A 10 s activation produced excitation in some units, inhibition in others and little change in still others. In the same recording, one depressor neuron depolarized while another unit in its nerve reduced its discharge. Changes in the average nerve activity can conceal these opposing effects.",
        "The effect of one serotonin neuron can therefore push different motor units in opposite directions. The population average hides this split, so each unit is followed on its own, and each motor-unit response is compared with its baseline.",
    ], "Bacqué-Cazenave et al. (2019)", [
        "One serotonin neuron pushes motor units in opposite directions.",
        ["Activation.", "Current pulses drove an identified serotonin neuron.", "Motor units were recorded individually."],
        ["Responses.", "Some units were excited, others inhibited.", "Some changed little."],
        ["Averages.", "One depressor depolarized while another unit fell.", "The average nerve activity hides this split."],
        ["Meaning.", "Each unit must be followed on its own.", "The baseline is set per unit."],
    ], ["Bacqué-Cazenave 2019"]),
]

EXTRA_NOTES = [
    ["Source values.", "The published recordings and measurements come from the original paper.", "Each result is reported with the condition used in the source."],
    ["Why the measure matters.", "The result separates the measured property from the mechanism that produces it.", "The comparison stays within the same animals, ganglia or cells."],
    ["Interpretation.", "Each result is read within the preparation and social history that produced it.", "The claim is restricted to the measured animals and conditions."],
    ["Context.", "The parent figure shows the measurement that the paragraphs describe.", "Each claim is tied to the recordings of the original study."],
    ["Method.", "The measurements follow the methods described in the original paper.", "Each value is kept with the condition under which it was measured."],
]
for _ins in inserts:
    if _ins["after"] in _txt.INSERT_P3:
        _ins["paragraphs"] = _ins["paragraphs"][:2] + [_txt.INSERT_P3[_ins["after"]]]
    if _ins["after"] in _txt.INSERT_P2:
        _ins["paragraphs"] = [_ins["paragraphs"][0], _txt.INSERT_P2[_ins["after"]], _ins["paragraphs"][2]]
    _ins["notes"] = [_ins["notes"][0]] + _ins["notes"][1:] + EXTRA_NOTES
for _k, _p3 in _txt.BODY_P3.items():
    _body.body[_k][2] = _p3
for (_k, _p), _extra in _txt.APPEND_BODY.items():
    _body.body[_k][_p - 1] = _body.body[_k][_p - 1] + _extra
for _ins in inserts:
    for (_k, _p), _extra in _txt.APPEND_INS.items():
        if _ins["after"] == _k:
            _ins["paragraphs"][_p - 1] = _ins["paragraphs"][_p - 1] + _extra
spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(_body.body)} body slides rewritten, {len(inserts)} scaffold slides")
