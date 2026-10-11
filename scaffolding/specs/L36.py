"""Scaffold spec for Lecture 36 (Drive deck Neuroethology_Lecture36_FA2026.pptx). Body rewrites are in body_L36.py."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L36 as _body  # noqa: E402
import L36_text as _txt  # noqa: E402


def ins(after, title, paragraphs, citation, notes, refs):
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


inserts = [
    ins(3, "Stimulus spacing sets the size of the decrement", [
        "The decrement in gill withdrawal depends on how the repeated siphon stimuli are spaced in time. Pinsker and colleagues held the seawater-jet stimulus constant and varied the interval between stimuli, so the spacing alone sets the pattern of repetition in each series.",
        "Shorter intervals produced a faster decline in contraction, while longer intervals slowed it. Responses commonly fell toward about 25% of the initial amplitude across the range of intervals tested. Each series begins from the same first response in the same animal.",
        "Stimuli delivered at closer intervals leave less time for the response to recover between trials. Recovery between trials is therefore part of what determines how far responsiveness falls across a series.",
    ], "Pinsker et al. (1970)", [
        "Stimulus spacing sets the size of the decrement.",
        ["Spacing.", "The interval between siphon stimuli was varied.", "The stimulus strength was held constant."],
        ["Decrement.", "Shorter intervals produced a faster decline.", "Longer intervals slowed it."],
        ["Baseline.", "Each series starts from the same first response.", "The reference is the same animal."],
        ["Meaning.", "Temporal history shapes the decrement.", "The pattern of repetition is recorded."],
    ], ["Pinsker 1970"]),
    ins(6, "Skin stimuli evoke EPSPs in an identified motor neuron", [
        "An identified gill motor neuron receives a direct excitatory input from the skin of the siphon. Brief stimuli to that skin depolarize the motor cell, and this depolarization is the first measurable link between touch and contraction.",
        "Castellucci and colleagues recorded the response in the same cell on repeated trials. Repeated stimulation reduced the response, and the reduction accumulated from one trial to the next across each session.",
        "Each EPSP in the identified cell can be traced to one defined synapse. The cell's large size makes it possible to record that synapse repeatedly over the whole session.",
    ], "Castellucci et al. (1970)", [
        "An identified motor neuron receives skin input.",
        ["Input.", "Skin stimuli produce a depolarization.", "The response links touch to contraction."],
        ["Recording.", "The same identified cell is recorded repeatedly.", "Each trial follows the one before."],
        ["Decrement.", "Repeated stimulation reduced the response.", "The reduction accumulated across the session."],
        ["Meaning.", "One defined synapse is measured directly.", "Its size allows repeated recordings."],
    ], ["Castellucci 1970"]),
    ins(9, "Shock acts on sensory inputs beyond the tapped one", [
        "Antonov and colleagues recorded behavior and neural activity together through a set of training protocols. Habituation used repeated siphon taps, dishabituation added tail shock after habituation, and sensitization used shock alone.",
        "Facilitation appeared in sensory neurons whose receptive fields covered the test site and in sensory neurons activated from elsewhere on the body. The modulatory action of shock therefore reaches more inputs than the one that was tapped during habituation.",
        "The change is spread across many connections, so its synaptic basis appears at several sites. Motor-cell firing, complex postsynaptic potentials and monosynaptic potentials each track this spread.",
    ], "Antonov et al. (1999)", [
        "Shock spreads its effect across sensory inputs.",
        ["Protocols.", "Habituation, dishabituation and sensitization were recorded.", "Shock was added at different points."],
        ["Facilitation.", "Sensory neurons from other locations were facilitated.", "Shock acted beyond the tapped input."],
        ["Spread.", "The change is distributed across several connections.", "Each site shows its own change."],
        ["Meaning.", "Several synapses carry the modulatory action.", "Motor and sensory measures track the spread."],
    ], ["Antonov 1999"]),
    ins(12, "Strong and weak connections depress at similar rates", [
        "Gover and colleagues evoked sensory action potentials at 15 s intervals in strong and weak sensory–motor connections. The two kinds of connection differed in their initial transmission and in their paired-pulse behavior, yet they depressed at similar rates.",
        "Applying 4-aminopyridine broadened sensory spikes and increased calcium-dependent release. This change raised initial transmission while depression stayed the same speed, which is the opposite of what a simple depletion account would predict.",
        "The observed depression kinetics therefore point to silencing of functional release sites in a stimulus-dependent way. Activity itself drives the silencing rather than the strength of the initial connection.",
    ], "Gover et al. (2002)", [
        "Depression rate is similar across connection strengths.",
        ["Connections.", "Strong and weak connections were recorded.", "Initial transmission differed between them."],
        ["Paired pulses.", "Paired-pulse behavior differed between the groups.", "Depression rates were similar."],
        ["Manipulation.", "4-aminopyridine broadened sensory spikes.", "Calcium-dependent release increased."],
        ["Meaning.", "Activity drives release-site silencing.", "Initial strength does not set the rate."],
    ], ["Gover 2002"]),
    ins(15, "Spaced training retains more than massed training", [
        "Carew and colleagues gave forty habituation trials in one day to one group, and the same total spread over four days to another. The **massed** schedule concentrated the experience in one session, and the **spaced** schedule distributed it across days.",
        "Both schedules produced substantial decrement during training. Spaced training yielded stronger retention after 24 h and after one week than massed training. The response within a single session predicts little about how much of the change lasts across days.",
        "Retention was measured as withdrawal behavior, and it could be tested in a restrained preparation as well. Spacing effects of this kind set up the later experiments that examine the molecular events under different temporal patterns.",
    ], "Carew et al. (1972)", [
        "Spacing trials across days improves retention.",
        ["Schedules.", "Massed training occurred in one day.", "Spaced training spanned four days."],
        ["Training.", "Both schedules produced large decrements.", "The within-session response is a weak guide."],
        ["Retention.", "Spaced training retained more after 24 h and one week.", "The difference persisted."],
        ["Meaning.", "Temporal distribution shapes what is retained.", "Molecular events are examined next."],
    ], ["Carew 1972"]),
    ins(18, "Serotonin enhances EPSPs after depression", [
        "Brunelli and colleagues compared serotonin, dopamine and octopamine at the sensory-neuron connection onto a gill motor neuron. Serotonin changes how an existing pathway responds, so the same connection can be measured before and after each neuromodulator.",
        "Sensory neurons were first depressed by repeated stimulation. Serotonin applied during a 2.5 min rest increased the subsequent synaptic responses. Rest periods without serotonin produced no such enhancement, so the drug accounts for the increase.",
        "The antagonist cinanserin reversibly reduced the facilitation evoked by connective stimulation, while the repeated-stimulation depression stayed intact. This pattern identifies a serotonergic route to facilitation that runs alongside the depression.",
    ], "Brunelli et al. (1976)", [
        "Serotonin facilitates a depressed connection.",
        ["Drugs.", "Serotonin, dopamine and octopamine were tested.", "Each acts on the same connection."],
        ["Depression.", "Repeated stimulation depressed the EPSPs.", "Serotonin was applied during a rest period."],
        ["Facilitation.", "Serotonin increased the subsequent responses.", "Rest without serotonin did not."],
        ["Antagonist.", "Cinanserin reduced connective-induced facilitation.", "Depression stayed intact."],
    ], ["Brunelli 1976"]),
    ins(21, "Type 2 PKA concentrates near nerve endings", [
        "Liu and colleagues measured PKA regulatory subunits in cell bodies, neurites and synaptosomes, which are terminal-enriched particles isolated from nervous tissue. Type 1 PKA was mostly soluble, whereas type 2 PKA was enriched in neuronal processes and tied to anchoring proteins near nerve endings.",
        "Repeated serotonin treatment increased RII protein in synaptosome preparations at 24 h. Immunostaining also detected more RII in sensory neurons. Prolonged facilitation is therefore linked to a change in the amount and location of a signaling protein, not only to a brief rise in cAMP.",
        "Each synaptosome preparation contains many terminals, so the measured increase is an average across them. Nuclear type 1 PKA and synaptic type 2 PKA carry complementary roles in this account.",
    ], "Liu et al. (2004)", [
        "Type 2 PKA sits near nerve endings.",
        ["Subunits.", "Type 1 and type 2 PKA differ in location.", "Type 2 is enriched in processes."],
        ["RII.", "Repeated serotonin raised RII protein at 24 h.", "Sensory neurons showed more RII."],
        ["Fraction.", "Synaptosomes are terminal-enriched particles.", "They report averages across terminals."],
        ["Meaning.", "Protein amount and place both change.", "Nuclear and synaptic pools have distinct roles."],
    ], ["Liu 2004"]),
    ins(24, "Postsynaptic calcium contributes to facilitation", [
        "Li and colleagues introduced BAPTA, a fast calcium buffer, into the motor neuron of cultured sensory–motor synapses. Intracellular calcium regulates signaling inside a cell without being the extracellular transmitter. The buffer therefore tests whether facilitation needs a change beyond the sensory terminal.",
        "A ten-minute application of 10 μM serotonin enhanced control EPSPs. Buffering postsynaptic calcium reduced the facilitation, most clearly after serotonin was removed. Motor-cell injections without the buffer showed that the effect comes from the calcium buffer itself.",
        "Facilitation therefore needs a postsynaptic calcium signal in this preparation. A single connection can change on both sides at once, so the presynaptic and postsynaptic results combine into one account.",
    ], "Li et al. (2005)", [
        "Postsynaptic calcium is needed for facilitation.",
        ["Buffer.", "BAPTA was introduced into the motor neuron.", "The sensory terminal was left intact."],
        ["Serotonin.", "A ten-minute application enhanced EPSPs.", "Buffering reduced the enhancement."],
        ["Controls.", "Motor-cell injections without the buffer were run.", "The effect was assigned to the buffer."],
        ["Meaning.", "Facilitation requires a postsynaptic change.", "Presynaptic and postsynaptic results combine."],
    ], ["Li 2005"]),
    ins(27, "Motor-cell toxin blocks dishabituation", [
        "Li and colleagues moved the postsynaptic toxin experiment from culture into a reduced siphon-withdrawal preparation. Identified motor neurons were injected with botulinum toxin B before a sequence of siphon taps, tail shock and further siphon tests.",
        "Control preparations increased siphon withdrawal after shock, whereas postsynaptic toxin blocked this dishabituation. Motor activity recorded alongside the movement linked the cell-targeted treatment to a measured behavioral change.",
        "Postsynaptic exocytosis in the siphon motor cells contributes to the behavior. The same requirement carries over to other gill responses and to sensitization protocols, which share the same motor cells.",
    ], "Li et al. (2005)", [
        "A motor-cell toxin blocks dishabituation.",
        ["Toxin.", "Botulinum toxin B was injected into motor neurons.", "Injection preceded the behavioral sequence."],
        ["Sequence.", "Taps, shock and further tests were applied.", "The sequence was the same for all groups."],
        ["Controls.", "Control preparations increased withdrawal after shock.", "Toxin blocked that increase."],
        ["Meaning.", "Postsynaptic exocytosis contributes to behavior.", "The same cells serve other responses."],
    ], ["Li 2005"]),
    ins(30, "Synthesis is needed during a restricted window", [
        "Montarolo and colleagues varied when anisomycin was present relative to repeated serotonin. A three-hour exposure during and immediately after induction blocked long-term facilitation. Inhibition that began much earlier, or several hours later, left the 24 h enhancement intact.",
        "Biochemical measurements showed strong suppression of protein synthesis during drug exposure and recovery after washout. The timing of the drug therefore lines up with its effect on the cell. Long-term facilitation depends on new synthesis during a restricted induction period.",
        "A critical window fits the production of proteins that start or stabilize persistent change. The identities, turnover rates and locations of these proteins are the next questions.",
    ], "Montarolo et al. (1986)", [
        "Protein synthesis is required within a restricted window.",
        ["Timing.", "Anisomycin was applied at different times.", "Only induction exposure blocked persistence."],
        ["Biochemistry.", "Protein synthesis was strongly suppressed.", "Recovery followed washout."],
        ["Window.", "Long-term facilitation depends on a restricted period.", "Synthesis is needed during induction."],
        ["Meaning.", "Persistent change needs newly made proteins.", "Their identities come next."],
    ], ["Montarolo 1986"]),
    ins(33, "CREB1 binds the synapsin promoter", [
        "**CREB1** is a transcription factor that regulates gene expression by binding DNA. A **promoter** is a DNA region that controls transcription of a gene. Hart and colleagues identified a cAMP response element in the _Aplysia_ synapsin promoter, which is a site that CREB1 can bind.",
        "A promoter-driven fluorescent reporter increased expression after serotonin treatment. Chromatin immunoprecipitation, which pulls down DNA bound to a chosen protein, found more CREB1 bound to the synapsin promoter. These measurements link the regulatory sequence, transcription-factor binding and expression level.",
        "Serotonin-dependent signaling reaches synapsin production through CREB1 binding at this promoter. Other transcriptional responses of long-term facilitation are assigned to their own target genes.",
    ], "Hart et al. (2011)", [
        "CREB1 binds the synapsin promoter after serotonin.",
        ["CREB1.", "CREB1 regulates gene expression by binding DNA.", "A promoter controls transcription of a gene."],
        ["Reporter.", "A fluorescent reporter rose after serotonin.", "The promoter drives the reporter."],
        ["Binding.", "Chromatin immunoprecipitation found more CREB1.", "The synapsin promoter was bound more."],
        ["Meaning.", "A route links serotonin to synapsin production.", "Other target genes have their own routes."],
    ], ["Hart 2011"]),
    ins(36, "Local translation responds to serotonin", [
        "Lee and colleagues examined **ApCPEB4**, an RNA-binding translation regulator in _Aplysia kurodai_, a related sea-hare species. They attached fluorescent reporters to its 3′ untranslated region, an RNA segment that controls expression without encoding protein sequence.",
        "Severed neurites allowed local responses to be recorded apart from delivery by the cell body. Serotonin increased reporter expression in these isolated processes. Translation-related controls showed that this increase does not require new transcription.",
        "Isolated processes hold a local pool of RNA that responds to modulatory signaling without the nucleus. Local translation therefore adds a control point for facilitation alongside transcription.",
    ], "Lee et al. (2016)", [
        "Isolated neurites translate reporter RNA in response to serotonin.",
        ["Reporter.", "ApCPEB4 3′ untranslated region was linked to a reporter.", "Expression was tracked in neurites."],
        ["Severing.", "Severed neurites were recorded apart from the cell body.", "Local responses were measured."],
        ["Controls.", "Translation-related controls were used.", "Transcription was ruled out."],
        ["Meaning.", "Local translation responds to serotonin.", "It adds a control point for facilitation."],
    ], ["Lee 2016"]),
    ins(39, "Neurotrophin isoforms reach different compartments", [
        "Kassabov and colleagues identified **ApNT**, an Aplysia neurotrophin, and **ApTrk**, its receptor tyrosine kinase. A **neurotrophin** is a secreted signaling protein that regulates neuronal growth or function. Alternative RNA processing produced ApNT isoforms with different processing and secretion properties.",
        "Tagged isoforms were expressed in sensory–motor cultures and examined with biochemical assays and fluorescence microscopy. Their distributions differed between cell bodies, neurites and secretion-related compartments. The labeling ties each isoform's processing to where it sits in the cell.",
        "The ApNT isoform with the stronger secretion profile reaches the ApTrk receptor on distant neurites. Receptor activation in those neurites is measured with functional assays.",
    ], "Kassabov et al. (2013)", [
        "ApNT isoforms reach different compartments.",
        ["Neurotrophin.", "ApNT is a secreted signaling protein.", "ApTrk is its receptor."],
        ["Isoforms.", "Alternative RNA processing generates the isoforms.", "They differ in processing and secretion."],
        ["Localization.", "Distributions differ across compartments.", "Labeling ties processing to location."],
        ["Meaning.", "Each isoform reaches its own targets.", "Receptor activation is measured directly."],
    ], ["Kassabov 2013"]),
    ins(42, "CREB1 knockdown weakens day-long enhancement", [
        "Zhou and colleagues injected CREB1-targeting siRNA into sensory neurons and waited 72 h before applying repeated serotonin. The standard protocol used five 5 min pulses of 50 μM serotonin, and EPSPs were recorded before treatment and at 24 h afterward.",
        "Control siRNA and vehicle groups ran in parallel with the CREB1 knockdown. CREB1 knockdown impaired long-term facilitation. Control-RNA synapses reached about 184% of their pretest amplitude, whereas CREB1-siRNA synapses reached about 121%.",
        "A transcription factor is therefore needed for persistent synaptic enhancement under this protocol. Partial loss of CREB1 weakens an otherwise effective training pattern while the neurons remain responsive.",
    ], "Zhou et al. (2015)", [
        "CREB1 knockdown weakens day-long enhancement.",
        ["Injection.", "CREB1 siRNA was injected into sensory neurons.", "Repeated serotonin followed 72 h later."],
        ["Protocol.", "Five 5 min pulses of 50 μM serotonin were applied.", "EPSPs were recorded at 24 h."],
        ["Controls.", "Control siRNA and vehicle groups ran in parallel.", "Injection effects were controlled."],
        ["Meaning.", "A transcription factor supports persistent enhancement.", "Partial loss weakens the effect."],
    ], ["Zhou 2015"]),
]

EXTRA_NOTES = [
    ["Source values.", "The published recordings and measurements come from the original paper.", "Each result is reported with the condition used in the source."],
    ["Why the measure matters.", "The result separates the measured property from the mechanism that produces it.", "The measurement stays with the same animals, ganglia or cells."],
    ["Interpretation.", "Each result is read within the preparation and protocol that produced it.", "The claim covers the measured animals and conditions."],
    ["Context.", "The parent figure shows the measurement that the paragraphs describe.", "Each claim is tied to the recordings of the original study."],
    ["Method.", "The measurements follow the methods described in the original paper.", "Each value is kept with the condition under which it was measured."],
]
for _ins in inserts:
    _ins["notes"] = [_ins["notes"][0]] + _ins["notes"][1:] + EXTRA_NOTES
for _k, _t in _txt.BODY.items():
    _body.body[_k][2] = _t
for _ins in inserts:
    for _i, _t in enumerate(_txt.INSERT.get(_ins["after"], [None, None, None])):
        if _t is not None:
            _ins["paragraphs"][_i] = _t

spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(_body.body)} body slides rewritten, {len(inserts)} scaffold slides")
