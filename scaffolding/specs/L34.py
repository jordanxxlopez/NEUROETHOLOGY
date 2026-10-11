"""Scaffold spec for Lecture 34 (Drive deck Neuroethology_Lecture34_FA2026.pptx). Body rewrites are in body_L34.py."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L34 as _body  # noqa: E402
import L34_text as _txt  # noqa: E402


def ins(after, title, paragraphs, citation, notes, refs):
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


inserts = [
    ins(3, "Movement and sound share one timeline", [
        "Video tracking and acoustic recording capture different sides of the same courtship. Song is identified from the microphone record, and each male's movement is identified from its trajectory. Both streams are kept on one clock, so every sound can be placed at the exact moment of each fly's movement.",
        "Pulse and sine bouts occur at irregular times during the approximately 25 min of courtship. The shared timeline allows the analysis to check whether a change in movement comes before or after a change in song mode. Each bout is therefore read against the movement that precedes it.",
        "Simultaneous traces also separate the male's own motion from the female's motion and from the sound source. This separation prevents movement-associated noise from being counted as song, and it keeps the measures for each partner distinct.",
    ], "Coen et al. (2014)", [
        "Tracking and sound are recorded on one timeline.",
        ["Recording.", "Sound and trajectories share one clock.", "Each sound is matched to fly positions."],
        ["Timing.", "Song changes can be compared with prior movement.", "Each bout is read against its preceding movement."],
        ["Separation.", "Male, female and sound are traced separately.", "Noise is not counted as song."],
        ["Meaning.", "The shared timeline supports short-timescale comparisons.", "Each partner is measured on its own."],
    ], ["Coen 2014"]),
    ins(6, "Distance alters the balance between song modes", [
        "Distance between the two flies changes how much visual information each partner receives. In this experiment, the proportion of pulse song rose as the flies moved farther apart. The effect was measured across several distance bands so that each band could be compared against the others.",
        "Darkness changed the mix of song modes, with males tested in the dark producing more pulse song. Both lighting conditions still produced song, so the change lies in the composition of the song rather than in the presence of singing. Each condition is compared with its own illuminated control.",
        "Visual information therefore takes part in choosing between pulse and sine. Distance and light act on the same song output, which allows the two cues to be compared in one framework and linked to the sensory conditions.",
    ], "Coen et al. (2014)", [
        "Distance changes the proportion of pulse song.",
        ["Distance.", "Pulse proportion rises as the flies separate.", "Bands are compared against each other."],
        ["Darkness.", "Dark-tested males produced more pulse song.", "Singing itself continued in both conditions."],
        ["Controls.", "Each condition is compared with its illuminated control.", "The lighting is the only change."],
        ["Meaning.", "Visual cues contribute to choosing a song mode.", "Distance and light act on the same output."],
    ], ["Coen 2014"]),
    ins(9, "Splice alleles isolate the P1 decision", [
        "A splice allele changes the sequence that controls one step in RNA processing. Demir and Dickson designed alleles that alter only the sex-specific P1 splice decision, so each allele affects one choice while leaving other fruitless functions intact. This design isolates the P1 decision from the rest of the gene.",
        "The alleles were verified at the transcript level and at the level of FruM protein in adult brains. A forced female-type allele and a forced male-type allele were compared against each other. The verification ensures that each behavioral result can be linked to a known molecular change.",
        "Because each allele changes one decision, its phenotype can be attributed to that decision. The comparison between the two forced patterns then shows which courtship features follow from the male-type splice, and which follow from the female-type splice.",
    ], "Demir & Dickson (2005)", [
        "Alleles that change only the P1 splice decision.",
        ["Design.", "Each allele changes the P1 splice decision.", "Other fruitless functions are preserved."],
        ["Verification.", "Transcripts and protein were checked in adult brains.", "The molecular change is confirmed."],
        ["Comparison.", "Female-type and male-type alleles are contrasted.", "Each phenotype is traced to its allele."],
        ["Meaning.", "Behavioral results can be linked to one splice decision.", "The gene effect is isolated."],
    ], ["Demir 2005"]),
    ins(12, "Forced male splicing suppresses female egg laying", [
        "Receptivity is the willingness of a female to accept mating, and egg laying is a separate reproductive output. Demir and Dickson measured both in females carrying male-spliced alleles, so each female was scored for mating, fertility and egg production together.",
        "Most control females mated within an hour, while fewer than one female in six carrying the male-spliced alleles mated during that time. After mating, control females laid many eggs over three days, whereas the engineered females laid very few. The reduction in egg laying is large and consistent across the females tested.",
        "Genital anatomy does not supply the full account of this phenotype, so the reproductive effect is interpreted as a change in behavior. The mating and egg-laying results agree, which makes the suppression of female reproductive behavior a coherent outcome of the male splice.",
    ], "Demir & Dickson (2005)", [
        "Male splicing in females suppresses mating and egg laying.",
        ["Receptivity.", "Mating within 60 min was scored in each female.", "Controls mated far more often."],
        ["Egg laying.", "Control females laid many eggs after mating.", "Engineered females laid very few."],
        ["Anatomy.", "Genital structure is not the full explanation.", "The effect is read as behavioral."],
        ["Meaning.", "Mating and egg laying are both suppressed.", "The outcome is a single reproductive phenotype."],
    ], ["Demir 2005"]),
    ins(15, "Isoform mutants lose song modes differently", [
        "An isoform mutant removes one protein product of the fruitless gene while leaving the others in place. von Philipsborn and colleagues paired each mutant male with a virgin female and recorded pulse song, sine song and copulation, so each mutant is compared on the same measures.",
        "FruC mutants lost sine song and showed the strongest mating impairment among the isoform mutants. Sine song has a carrier frequency of about 120–170 Hz, so its loss removes an entire song mode. FruA and FruB perturbations produced different, milder combinations of defects.",
        "The distinct profiles of the isoform mutants indicate that each isoform contributes a different part of the courtship network. The mutants show that a single gene can influence several outputs through separate protein products.",
    ], "von Philipsborn et al. (2014)", [
        "Each isoform removes a different part of the song.",
        ["Mutants.", "Each isoform mutant removes one protein product.", "Pulse, sine and copulation are scored."],
        ["FruC.", "FruC mutants lost sine song.", "Mating was impaired more than in other mutants."],
        ["FruA and FruB.", "These mutants showed milder, different defects.", "The profiles differ from FruC."],
        ["Meaning.", "Isoforms contribute distinct parts of the network.", "One gene drives several outputs."],
    ], ["von Philipsborn 2014"]),
    ins(18, "Dark courtship depends on FruC in defined classes", [
        "Cell-specific knockdown reduces a gene product only in selected neurons. von Philipsborn and colleagues depleted FruC in defined courtship-related classes and compared pulse production under illumination and in darkness, so each class can be assessed separately.",
        "Knockdown in aSP4 or vAB3 feminized characteristic arbors and impaired courtship in the dark. Comparing pulse amounts in light and in darkness separates the visual from the nonvisual contribution. The dark measure isolates the part of the behavior that does not depend on sight.",
        "P1 neuron presence depended on the sex-determination gene doublesex as well as on fruitless. Each neuronal class is assessed for its dependence on both genes, and the combined effects are read from the same courtship measures.",
    ], "von Philipsborn et al. (2014)", [
        "Knockdown in specific classes reduces dark courtship.",
        ["Knockdown.", "FruC is reduced in defined neuron classes.", "Other cells keep their expression."],
        ["Light and dark.", "Pulse amounts are compared under both conditions.", "The dark measure isolates nonvisual input."],
        ["Arbors.", "Knockdown in aSP4 or vAB3 changed characteristic arbors.", "Dark courtship was impaired."],
        ["Doublesex.", "P1 presence depended on doublesex.", "The two genes are assessed together."],
    ], ["von Philipsborn 2014"]),
    ins(21, "Wing choice is separate from P1 initiation", [
        "A population that starts singing and a population that selects a wing can be separate circuits. von Philipsborn and colleagues compared unilateral and bilateral P1 activation using stochastic expression, so each male's wing choice could be scored against the side of activation.",
        "Unilateral activation did not impose a consistent wing choice on the animals. Males chose either wing across repeated bouts and normally avoided extending both wings at once. The wing record is therefore independent of the side of the activated neurons.",
        "The dissociation places wing selection downstream of, or parallel to, the initiation function. Each bout is scored for its wing, and the activation record and the wing record are compared in the same animals.",
    ], "von Philipsborn et al. (2011)", [
        "Wing choice and song initiation are dissociated.",
        ["Initiation.", "P1 activation can start pulse song.", "Song initiation is one function."],
        ["Wing choice.", "The chosen wing varied across bouts.", "The side of activation did not set it."],
        ["Comparison.", "Unilateral and bilateral activation were compared.", "Stochastic labeling supplied the variation."],
        ["Meaning.", "Wing selection is a separate motor step.", "Each bout is scored for its wing."],
    ], ["von Philipsborn 2011"]),
    ins(24, "vPR6 shortens interpulse intervals with temperature", [
        "Interpulse interval is the time between successive pulses in a pulse train. von Philipsborn and colleagues tested whether activation of vPR6 changed this interval, rather than producing an undifferentiated wing movement.",
        "Across five genetic patterns, the interval shortened by about 5.4–7.0 ms for each degree of temperature increase. Wild-type intervals changed by about 1.0 ms per degree, so the vPR6 effect is several times larger than the ordinary temperature dependence of song.",
        "The effect was associated with patterns containing vPR6 rather than with every song-promoting pattern. Each pattern is compared with the same wild-type baseline on the same scale, which links vPR6 activity to the timing of the pulses.",
    ], "von Philipsborn et al. (2011)", [
        "vPR6 activity shortens the interval between pulses.",
        ["Interval.", "The interpulse interval is the time between pulses.", "It was measured in each pattern."],
        ["Rate.", "The interval shortened about 5.4–7.0 ms per degree.", "The wild type changed about 1.0 ms per degree."],
        ["Patterns.", "Five genetic patterns were compared.", "vPR6 was present in the strongest effect."],
        ["Meaning.", "vPR6 couples to pulse timing.", "The effect is specific to this class."],
    ], ["von Philipsborn 2011"]),
    ins(27, "GABA knockdown produces bilateral wing extension", [
        "Normal courtship usually uses one extended wing at a time. Amin and colleagues knocked down GAD1 or Rdl in fruitless-positive neurons and scored the wing posture of each male. Genetic controls matched the expression system, so the posture change is attributed to the knockdown.",
        "Many knockdown males extended both wings, whereas control males predominantly extended one. The posture defect was scored separately from the timing and waveform of the sound, which kept the motor and acoustic measures distinct.",
        "The result supports an inhibitory contribution to coordinating competing wing movements. Bilateral extension is the defect that inhibition normally prevents, and each male's posture is compared with its matched control.",
    ], "Amin et al. (2023)", [
        "GABA knockdown removes control of wing posture.",
        ["Posture.", "Control males usually extended one wing.", "Knockdown males extended both."],
        ["Controls.", "Genetic controls matched the expression system.", "The knockdown is the variable."],
        ["Measures.", "Posture is scored apart from sound.", "Waveform and timing are measured separately."],
        ["Meaning.", "Inhibition helps coordinate competing wings.", "Bilateral extension is the defect."],
    ], ["Amin 2023"]),
    ins(30, "Brain and nerve-cord GABA affect different outputs", [
        "Regional restriction separates a perturbation in the brain from a perturbation in the nerve cord. Amin and colleagues confirmed each expression pattern anatomically before scoring behavior, so the region of each effect is known.",
        "Nerve-cord knockdown reproduced bilateral wing extension and abnormal song. Brain-restricted knockdown did not reproduce those motor defects, and instead impaired courtship conditioning after exposure to an unreceptive mated female.",
        "The regional dissociation assigns different inhibitory roles to motor control and to learned changes in courtship. Each role is tied to the region where it was measured, so the two outputs are compared with the same knockdown groups.",
    ], "Amin et al. (2023)", [
        "Brain and nerve-cord GABA support different outputs.",
        ["Regions.", "Expression was restricted to the brain or nerve cord.", "Each region was confirmed anatomically."],
        ["Nerve cord.", "Nerve-cord knockdown caused bilateral extension.", "Abnormal song followed."],
        ["Brain.", "Brain knockdown impaired courtship conditioning.", "Motor defects were not reproduced."],
        ["Meaning.", "Motor control and conditioning are separate outputs.", "Each is tied to its region."],
    ], ["Amin 2023"]),
    ins(33, "Complex bouts follow frontal female positions", [
        "Relative bearing describes where the female stands with respect to the male's body axis. Roemschied and colleagues compared bearing, inter-fly distance and bout duration for simple pulse, simple sine and complex bouts, so the geometry of each bout is recorded.",
        "Complex bouts occurred more often when the female was closer and more directly in front of the male. Their duration was longer than that of simple bouts, with distributions spanning about 0 to 3 s.",
        "Close frontal positions also increase opportunities for contact and change visual motion. The geometry is therefore read together with those factors, and each bout is described by the female's position at the time it occurred.",
    ], "Roemschied et al. (2023)", [
        "Complex bouts are associated with frontal female positions.",
        ["Bearing.", "Relative bearing is the female's position on the male's axis.", "It is recorded for each bout."],
        ["Complex bouts.", "They occurred more often in close, frontal positions.", "Their duration was longer."],
        ["Duration.", "Distributions spanned about 0 to 3 s.", "Simple bouts were shorter."],
        ["Meaning.", "Geometry is linked to song sequencing.", "Contact and visual motion are also involved."],
    ], ["Roemschied 2023"]),
    ins(36, "TN1 neurons show opposing calcium dynamics", [
        "Calcium imaging reports changes in intracellular calcium through fluorescence. Roemschied and colleagues combined pIP10 optogenetic stimulation with two-photon imaging in TN1 neurons, so each cell's response is recorded during the same stimulation.",
        "Some TN1 calcium signals tracked the stimulus. Others were anticorrelated and peaked after the stimulus was removed. The recordings kept response timing over several seconds and anatomical positions at a 20 µm scale.",
        "The opposing dynamics support a functional subdivision within TN1. Each subgroup is defined by its response timing, which places the two groups in different roles in the wing circuit.",
    ], "Roemschied et al. (2023)", [
        "TN1 neurons respond with opposing dynamics.",
        ["Imaging.", "Calcium signals are read through fluorescence.", "Each cell is recorded individually."],
        ["Tracking.", "Some signals followed the stimulus.", "Others peaked after it ended."],
        ["Scale.", "Timing was kept over seconds.", "The 20 µm scale locates each response."],
        ["Meaning.", "TN1 contains functionally distinct subgroups.", "Timing defines each group."],
    ], ["Roemschied 2023"]),
    ins(39, "Nested populations share nerve-cord circuitry", [
        "A nested activation pattern means that one active population includes another as a subset. Shiozaki and colleagues imaged identified nerve-cord neurons while flies alternated pulse and sine, with wing vibration preserved by attaching parts of the legs.",
        "dPR1 signals preferred pulse, whereas TN1A-2 signals remained active during both modes and were stronger during sine. The responses were aligned around transitions on a 0.5 s timescale, so the timing of each change is visible.",
        "The observations support shared circuit participation with an additional pulse-related population. The pulse and sine populations overlap in a defined way, which is the basis of the nested model.",
    ], "Shiozaki et al. (2024)", [
        "Pulse and sine populations overlap in the nerve cord.",
        ["Nesting.", "One population includes another as a subset.", "The overlap is defined by activity."],
        ["dPR1.", "dPR1 preferred pulse and declined during sine.", "It is a pulse-associated population."],
        ["TN1A-2.", "TN1A-2 stayed active in both modes.", "It was stronger during sine."],
        ["Alignment.", "Responses were aligned to transitions.", "The timescale is 0.5 s."],
        ["Meaning.", "Shared participation links the two modes.", "The nested model follows."],
    ], ["Shiozaki 2024"]),
    ins(42, "pMP2 and pIP10 carry different song dynamics", [
        "pMP2 is a descending neuron class that connects the brain and nerve cord. Shiozaki and colleagues recorded its calcium activity alongside pIP10 while flies alternated pulse and sine, so both pathways are compared on one timeline.",
        "pIP10 remained active during both song modes. pMP2 was pulse-selective, increasing at sine-to-pulse transitions and declining at pulse-to-sine transitions. Each transition is measured in both pathways on the same 0.5 s scale.",
        "The two pathways provide differential input to the thoracic network. Each descending pathway contributes according to its own dynamics, and the labeled anatomy identifies which pathway carries each pattern.",
    ], "Shiozaki et al. (2024)", [
        "Two descending pathways carry different song dynamics.",
        ["Pathways.", "pMP2 and pIP10 both connect brain and nerve cord.", "They were recorded together."],
        ["pIP10.", "pIP10 stayed active during both modes.", "It did not change with the transitions."],
        ["pMP2.", "pMP2 was pulse-selective.", "It rose at sine-to-pulse transitions."],
        ["Timing.", "Transitions were aligned on a 0.5 s scale.", "Both pathways share the scale."],
        ["Meaning.", "Descending input differs by pathway.", "No single command drives every mode."],
    ], ["Shiozaki 2024"]),
]

EXTRA_NOTES = [
    ["Source values.", "The published recordings and measurements come from the original paper.", "Each result is reported with the condition used in the source."],
    ["Why the measure matters.", "The result separates the measured property from the mechanism that produces it.", "The comparison stays within the same flies, cells or recordings."],
    ["Interpretation.", "Each result is read within the genetic background and condition that produced it.", "The claim is restricted to the measured animals and conditions."],
    ["Context.", "The parent figure shows the measurement that the paragraphs describe.", "Each claim is tied to the recordings of the original study."],
    ["Method.", "The measurements follow the methods described in the original paper.", "Each value is kept with the condition under which it was measured."],
]
for _ins in inserts:
    _ins["notes"] = [_ins["notes"][0]] + _ins["notes"][1:] + EXTRA_NOTES
for _k, _ps in _txt.BODY.items():
    for _p, _t in _ps.items():
        _body.body[_k][_p - 1] = _t
for _ins in inserts:
    for _p, _t in _txt.INSERT.get(_ins["after"], {}).items():
        _ins["paragraphs"][_p - 1] = _t

spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(_body.body)} body slides rewritten, {len(inserts)} scaffold slides")
