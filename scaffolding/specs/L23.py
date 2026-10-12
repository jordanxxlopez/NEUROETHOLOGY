"""Scaffold spec for Lecture 23 (Drive deck Neuroethology_Lecture23_FA2026.pptx). Body rewrites are in body_L23.py."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L23 as _body  # noqa: E402


def ins(after, title, paragraphs, citation, refs):
    notes = [title + "."] + [
        [f"Explanation {i + 1}.", *(p.split(". ", 1))] for i, p in enumerate(paragraphs)
    ] + [["Source.", f"The figure and the measurements come from {citation}.", "Its recordings and observations support each statement above."]]
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


inserts = [
    ins(3, 'Arena dimensions fix the magnetic setting', [
        "Lohmann's orientation arena was a 1.02-m-diameter inverted satellite dish, surrounded by a 130-cm magnetic coil. The coil set the field around the turtle throughout each trial, while the animal stayed inside the water-filled preparation. Changing the coil output changed the field without moving the animal from the arena.",
        "The harness and tracking system give a behavioral readout. That record shows which direction the turtle chose, but it reveals neither receptor activity nor the tissue that supplies the magnetic information. The eyes, the head or another tissue could each supply that information, and the record leaves those sources undetermined.",
        "Direction selection in this arena supports magnetic influence within the arena. Free-ranging turtles combine several cues that the arena removes. Direction selection in an arena leaves open how multiple cues guide free-ranging turtles at sea.",
    ], 'Lohmann (1991)', ['Lohmann 1991']),
    ins(6, 'Dark recording follows a short adjustment', [
        "After the eastern light was extinguished, investigators changed the inclination and allowed 3 min for adjustment. Swimming was then recorded for 5 min in darkness, so each heading reflects the field rather than visible cues. The same sequence was used for every inclination tested.",
        "A detectable field can fail to trigger a shared heading, especially when it lacks the ecological meaning of a field encountered near a route boundary. The absence of a shared heading at 75°, 45° and 15° leaves open whether those fields are detected.",
        "Headings can differ across angles without each angle being tied to a geographical coordinate. Discrimination between nearby inclinations is the measured result, while a geographical reading is an interpretation added afterward. That interpretation needs a separate test of position.",
    ], 'Lohmann & Lohmann (1994)', ['Lohmann 1994']),
    ins(9, 'A map gives position, a compass gives heading', [
        "A map sense determines information about position, whereas a compass sets a heading. The regional-field assay requires a location-dependent change in compass direction, a demand that differs from holding one bearing. A compass measures direction, while a map supplies the location-based correction.",
        "The assay leaves open how the brain represents the field and how it chooses the resulting action. The heading record links a field to a direction without describing the circuit between them. Neural recordings from that circuit would be needed to resolve the representation.",
        "A map can select the appropriate course while a compass maintains it. Other senses can influence both decisions, so the two functions can be separate without each sense operating alone. Sensory input from other systems can enter either decision.",
    ], 'Lohmann et al. (2001)', ['Lohmann 2001']),
    ins(12, 'Acquisition followed controlled reinforcement', [
        "Acquisition of these pairs took place under controlled reinforcement, so the learned responses reflect training rather than chance exposure. The evidence concerns learning under those conditions, not behavior during natural travel. A laboratory capacity to learn several signatures is compatible with natural return to different feeding areas.",
        "The behavioral experiment records learning rather than a documented journey to a feeding area. The natural return itself was never observed in these tests. Several learned fields could coexist within one animal's behavioral repertoire, and each new pairing followed the earlier training period.",
        "Those cues are candidates that the experiment supports for natural travel. Acquisition and natural return are separate questions in this assay. The learned association was measured, while natural travel was outside the test. The stored signatures are tied to the trained fields.",
    ], 'Goforth et al. (2025)', ['Goforth 2025']),
    ins(15, 'Mismatch responses resemble unrewarded fields', [
        "The response criterion in this experiment is learned recognition. Field measurements define the physical stimuli, while the duration of dancing reports whether a stimulus has acquired reward-related meaning. Neither measure records the neural computation that connects them. Both measures are needed to describe the result.",
        "Animals can still detect either parameter individually. One familiar component was insufficient to identify the rewarded compound under these conditions. The mismatch test isolates which combination the animal learned, and each mismatch keeps one learned value while replacing the other.",
        "Mismatch conditions reveal which parameter pairs an animal has learned to recognize. The stimuli were defined from the trained fields, so the test uses real field values. Behavior in each of the four test fields was scored as food-anticipatory dancing.",
    ], 'Goforth et al. (2025)', ['Goforth 2025']),
    ins(18, 'Pulse order was fixed after the controls', [
        "The pulse condition followed the controls in a fixed position, so treatment and sequence were not fully independent. Sequence effects remain entangled with the pulse itself. The baseline was measured before any pulse, which set the reference for every later test.",
        "A sham control reproduces the nonmagnetic components of an intervention. It leaves open every other conceivable effect of the pulse, but it tests whether placement and handling alone account for the change. The initial conditioning result provides the learned response against which the perturbation is judged.",
        "Magnetic pulses act on the receptor candidate itself, not on the sensory nerve. The pulse was designed to alter magnetization in iron-based candidate receptors, which makes the perturbation a test of a specific class of mechanism.",
    ], 'Mackiewicz et al. (2025)', ['Mackiewicz 2025']),
    ins(21, 'Perch activation measures a directional tendency', [
        "Perch activation provides an orientation measure, not a record of retinal activity. The cage counts describe the bird's directional tendency, while the sensory tissue that produced it stays unobserved. Migratory restlessness is the directional behavior that appears when migration is due.",
        "The seasonal preference was measured in a controlled field configuration rather than across the whole natural migration. A response in this setup shows what the bird does under those conditions, which is a narrower claim than migration as a whole.",
        "The migratory program supplies context for the heading, and a single sensory system can serve several seasonal headings. The historical report gives the field conditions for the record, and one configuration defines the outcome of that test.",
    ], 'Wiltschko & Wiltschko (1972)', ['Wiltschko 1972']),
    ins(24, 'Cluster N is a dorsal forebrain region', [
        "The authors collected brains after birds had been relatively still and awake. That condition limited movement-related expression, so the marker reflects the sensory condition rather than locomotion. The result is an activity pattern in tissue, not a recording from the living bird.",
        "The anatomical preparation linked a defined group of forebrain regions to a controlled visual condition. Dim light was chosen to approximate moonlight, and daytime room light was the control condition in the same species. The analysis used the same brain region in every bird.",
        "The marker identifies a region that responds to dim light in migrants. A candidate region is a starting point for functional tests, and expression alone leaves the magnetic role of that region open. Its magnetic role needs a separate test that manipulates the region.",
    ], 'Mouritsen et al. (2005)', ['Mouritsen 2005']),
    ins(27, 'Lesions test whether a region is needed', [
        "Expression data had shown an association between Cluster N and night vision, while a lesion can test whether the region is needed. Showing necessity requires a manipulation rather than an observed correlation. The behavioral loss localizes a necessary processing stage more strongly than gene expression alone.",
        "The lesion agent was injected locally, so the damage was confined to the region around the injection site. The result leaves the magnetic computation within the region unassigned to any single cell type or synapse. The injection site lies within the dorsal region identified by the earlier expression study.",
        "Sham-operated birds received the surgical steps but no active injection. The lesion removed coherent compass orientation while the other orientation responses stayed available, which points to a specific deficit. The sham result is the reference group for the lesion effect.",
    ], 'Zapka et al. (2009)', ['Zapka 2009']),
    ins(30, 'Virtual displacement changes the magnetic cues', [
        "Virtual displacement changes the local magnetic parameters without moving the bird from its capture site. The non-magnetic cues stay at the original site, so the magnetic signal alone conflicts with the displaced position. The conflict is set entirely by the magnetic parameters that were changed.",
        "The displacement changed intensity, inclination and declination together. The replicated field set the target location for the test, and the response was measured against the capture-site course. Those values define the places being simulated, not the bird's location.",
        "The coil changed several geographical field properties together, so the response reflects the combined magnetic signature. A simple compass rotation would change only direction, while the displacement changes the location-related signal. A heading response shows what the bird's map contributes.",
    ], 'Pakhomov et al. (2018)', ['Pakhomov 2018']),
    ins(33, 'Grounding decides the shielding effect', [
        "Grounding connects the conductive screening to an electrical reference, so its effect on noise differs from an isolated metal enclosure. The screens reduced electromagnetic noise only when they were electrically grounded, and the same screens produced different outcomes in the two electrical conditions.",
        "The behavioral comparison is tied to measured exposure conditions, not to the nominal construction of the huts. Observers scoring orientation did not know which hut was grounded, and the electromagnetic noise was measured in each hut.",
        "The grounded screens recovered the seasonal direction in the same birds, which is the pattern expected for a causal electromagnetic effect. A metal-screened hut without grounding fails to reproduce the effect. Electromagnetic noise, rather than metal alone, accounts for the two outcomes.",
    ], 'Engels et al. (2014)', ['Engels 2014']),
    ins(36, 'Staining locates Cry4 in photoreceptor outer segments', [
        "Cry4 was concentrated in the outer segments of photoreceptors, the light-sensitive compartments of the retina. The distribution spanned both peripheral and central retina, and the staining was seen in robins, the migratory species. A localization result identifies where a protein is, not what it does.",
        "Monoclonal antibodies recognize a selected antigenic target, whereas polyclonal preparations include several antibody populations. Immunohistochemistry was applied to robin and chicken retina with both classes of antibody. Each reagent class carries its own specificity, so agreement between them is informative.",
        "Agreement between independent reagents helps constrain a localization claim, provided that their specificity is tested rather than assumed. Fluorescence reports the location of the antibody's target, while a magnetoreceptor's signal output is a separate target for tests.",
    ], 'Günther et al. (2018)', ['Günther 2018']),
    ins(39, 'FAD is bound to the purified Cry4 protein', [
        "Spectroscopy and mass spectrometry measured the purified protein without cellular material. More than 97% of the wild-type protein carried FAD, which is the cofactor needed for the radical-pair reaction. Those measurements characterize the purified protein as a standalone molecule.",
        "The supplementary spectrum resolved FAD-bound peaks from weaker peaks attributed to protein without the cofactor. Those assignments distinguish the bound protein from a cofactor-free fraction in the same preparation. The spectrum is evidence about the bound state, not about neural activity.",
        "Mass spectra identify the FAD-bound form of cryptochrome 4 in the supplementary figure. The same purified preparation supplies the molecular system used for the photochemistry measurements. Spectroscopy and mass measurements supply the experimental evidence, whereas the structural image is a proposed arrangement.",
    ], 'Xu et al. (2021)', ['Xu 2021']),
    ins(42, 'Cry4 recycling depends on oxygen and reagents', [
        "The optical spectra were recorded as photoreduced Cry4 reoxidized in contact with air. No added redox reagents were present, so the reoxidation reflects the protein's own chemistry with ambient oxygen. The starting oxidation state set the reference for the recovery spectra.",
        "A receptor cycle includes activation and recovery. Resetting differs from showing that a neuron reads the changing state, and the downstream signaling partner and membrane mechanism are still being established. Each spectrum captured a different point in the oxidation sequence.",
        "Living cells contain oxygen, reducing agents and protein partners that a cuvette lacks. The rates measured in vitro set a reference for the cell, and they may differ in a living retina. Measured recovery times apply to the tested cuvette conditions.",
    ], 'Xu et al. (2021)', ['Xu 2021']),
]

spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(_body.body)} body slides rewritten, {len(inserts)} scaffold slides")
