"""Paragraph overrides for Lecture 34 (scaffolding/RULES.md): 5-7 lines, no filler. Applied by L34.py.

BODY[original slide][paragraph] and INSERT[slide the insert follows][paragraph].
"""

BODY = {
    2: {
        1: "Courtship song is an acoustic signal that a male Drosophila melanogaster produces by vibrating an extended wing while following a female. Pulse song consists of separated sound pulses, whereas sine song is a relatively continuous, approximately sinusoidal vibration. Both modes come from the same male during one courtship, and each has its own acoustic signature that identifies it in a recording.",
    },
    4: {
        3: "The outcomes support a contribution of song reception and production to successful courtship. Each surgical manipulation removes one sense or one structure, so a change in courtship success can be linked to that input. Males and females are both tested, which shows which half of the acoustic exchange contributes to success.",
    },
    5: {
        1: "Sensory history is the sequence of information available before a behavioral event. Coen and colleagues tested whether recent movement predicted song starts and pulse-to-sine transitions, using histories no longer than 600 ms. The short window places the analysis at each song event.",
        2: "A generalized linear model relates movement features to the probability of a song event. Male forward velocity and lateral speed predicted pulse starts. Forward velocity and inter-fly distance separated pulse from sine starts, so each predictor is weighed alongside the others in the same model.",
    },
    6: {
        3: "The finding is consistent with visual signals contributing to the choice between song modes. Darkness changes the interaction in several ways, and the distance records show how partners were positioned in each condition. Visual information therefore counts among the cues that shape song composition, and each lighting condition is paired with its own illuminated control.",
    },
    7: {
        2: "Song-related slowing was measured in 1 min windows. Female speed decreased before copulation, and the link between song amount and female speed changed with the paired species and sensory condition. Both D. melanogaster and D. simulans pairs were measured with identical windows, so the species share one time scale.",
    },
    9: {
        3: "Male-spliced alleles produced FruM labeling in females as well as males. The female-spliced allele removed that labeling in males. The verification links each behavioral result to a defined molecular change, so later phenotypes can be traced back to the splice pattern that produced them. Every phenotype is tied to its verified allele, which gives each behavioral result a known molecular cause.",
    },
    10: {
        1: "Necessity means that removing a factor disrupts an outcome under specified conditions. Demir and Dickson paired males carrying engineered fruitless splice alleles with wild-type virgin females. They measured the proportion of observation time devoted to courtship, using the same pairing and timing for every genotype so that every genotype is measured under identical conditions with the same control.",
        2: "Males forced into female-type splicing showed very little female-directed courtship, with courtship indices near 80% in control and male-spliced genotypes. Competitive mating assays also separated the female-spliced genotype from males that retained male-type splicing. Both assays point to the same P1 requirement, and each measure gives a separate readout of the same splice change.",
    },
    11: {
        3: "The result supports developmental sufficiency for many male-typical courtship actions in this genetic background. The set of actions is broad, while copulation is missing, which places the final step outside what the splice change produced. Each action was scored on its own, so the list shows exactly which parts of courtship the splice change can produce.",
    },
    12: {
        1: "Receptivity is a female's willingness to accept mating. Courtship production and reproductive receptivity are separable behavioral outcomes. Demir and Dickson tested whether forcing male fruitless splicing in females changed mating, fertility and egg laying, in addition to the newly expressed courtship actions. The reproductive measures were scored in the same females, so each female contributes to every readout.",
        3: "Behavior, not gross genital anatomy, carries the reproductive phenotype. The findings associate FruM with suppression of female reproductive behaviors. The receptivity and egg-laying results agree, so the phenotype appears as one outcome spanning several measures that reinforce one another.",
    },
    14: {
        3: "Isoform mutants differed in their production of pulse song, whose usual interpulse interval is about 35 ms. Coexpression therefore allows distinct functions within the same neurons. Each isoform contributes its own effect in those neurons, and the mutants reveal functions that the overlap would otherwise hide. The same song measures are recorded for every mutant.",
    },
    15: {
        1: "Isoform-specific mutations distinguish a general requirement for fruitless from a requirement for one of its protein endings. von Philipsborn and colleagues paired mutant males with virgin females and recorded pulse song, sine song and copulation. Each measure was taken in every mutant, using the same pairing protocol for all genotypes, so every mutant's results can be set against its own control.",
    },
    16: {
        3: "The dependence on illumination is consistent with altered access to nonvisual courtship information. The result links light availability with the FruC phenotype. The dark result carries the sharpest signal, because it removes visual cues from courtship.",
    },
    17: {
        2: "FruC was required for male-typical arborization in classes including aSP4 and vAB3. Mutants lacking this isoform also showed reduced pulse song without visual cues. Normal pulse spacing is about 35 ms, and the anatomy and the behavior measure the phenotype at different levels, so each mutant is described at both the cellular and the song scale.",
        3: "The results link a specific transcription-factor isoform with sex-dependent neuronal morphology. Arbor shape can constrain possible connectivity, which makes the anatomy a candidate basis for the song phenotype. Each arbor is recorded in its registered form for every genotype, so the shape differences can be identified as a sex-specific feature of the circuit.",
    },
    18: {
        1: "Cell-specific knockdown reduces a gene product in selected neurons while preserving it elsewhere. von Philipsborn and colleagues depleted FruC in defined courtship-related classes and compared pulse production under illumination and in darkness. The knockdown is confined to the targeted cells, so each class is tested under the same light conditions and its role is isolated.",
        3: "P1 neuron presence depended on the sex-determination gene doublesex rather than on fruitless alone. FruM can enable broad courtship behavior without specifying every courtship element on its own. Each neuronal class is therefore assessed for its dependence on both genes, and the combined effects are recorded with the same measures.",
    },
    20: {
        1: "Synaptic silencing blocks communication from a neuron rather than removing its anatomy. The 2011 study expressed tetanus-toxin light chain in a P1-containing fruitless-positive population. This protein cleaves a component required for synaptic vesicle release, so the toxin silences transmission while the cells remain present, and each population is paired with its own control.",
        3: "The contrast supports a requirement for transmission from these neurons under the tested conditions. Driver expression also labeled additional cells, so the silencing result is interpreted alongside the activation results. The two directions of manipulation reinforce each other, and both point to the same P1-containing population.",
    },
    23: {
        3: "Silenced males could still extend their wings while producing less pulse song. Wing posture and acoustic patterning therefore vary independently, so the wing movement and the song are scored for each male. The activation supports a thoracic contribution to song production that is distinct from the brain-driven pattern, and both the posture and the pulse output are tracked.",
    },
    24: {
        1: "vPR6 identifies a thoracic neuronal class with processes in wing neuropil. von Philipsborn and colleagues used several genetic patterns containing the vPR6-containing neurons. They tested whether activation changed pulse timing rather than merely triggering an undifferentiated wing movement, and pulse timing is the measure that tells these possibilities apart.",
        3: "The excess shortening was associated with patterns containing vPR6 rather than with every song-promoting pattern. The result supports coupling between vPR6 activity and the interval between pulses. Every pattern is plotted against the wild-type baseline on the same scale, so the effect can be assigned to vPR6-containing neurons and not to simple song initiation.",
    },
    25: {
        3: "Silencing the broader pattern also increased the fraction of pulses containing more than two oscillatory cycles to about 59%, up from fewer than 3% in controls. Other labeled cells could contribute to this change. Each pulse was scored for its cycles, so the waveform change is measured directly, and it adds a second readout beside the wing posture result.",
    },
    26: {
        3: "Reducing synthesis limits the available transmitter, while reducing the receptor changes the postsynaptic response to GABA. Both perturbations disrupted courtship motor coordination, so the two manipulations share one motor outcome. The same motor measures score each perturbation, and they are used throughout the following slides.",
    },
    27: {
        3: "The result supports an inhibitory contribution to the coordination of competing wing movements. Bilateral extension is the defect that inhibition normally prevents. Each male's posture is recorded against its matched control, so the defect appears against a clear baseline, and the contrast between bilateral and unilateral posture is the key measure in both genotypes.",
    },
    28: {
        3: "The defects concern both the organization of successive pulses and the structure of individual pulses. They support a role for inhibition in shaping the motor pattern. Each measure is taken at both the pulse level and the song level, which places the effect at two scales that are described together.",
    },
    30: {
        1: "Regional restriction distinguishes gene perturbation in the brain from perturbation in the nerve cord. Amin and colleagues used genetic repression and brain-specific recombination, verifying the resulting expression patterns anatomically before interpreting behavior. Each expression pattern is confirmed before its behavior is scored, so the anatomical check comes first in every experiment.",
        3: "Courtship conditioning is a subsequent reduction in courtship after rejection experience. The regional dissociation assigns different inhibitory contributions to motor control and to learned changes in courtship. Each contribution is tied to the region where it was measured, so motor control and conditioning are studied as two outputs, each measured against the same knockdown groups.",
    },
    31: {
        3: "The positive control establishes that the playback could compensate for missing wing-generated sound. Failure in the knockdown males therefore implicates additional courtship motor defects beyond the missing song. Each male's copulation is scored within the playback group it belongs to, and the knockdown result is set against the rescued control.",
    },
    33: {
        3: "The relationship connects the organization of song with the geometry of the interaction. Close frontal positioning also increases opportunities for contact and changes visual motion, so the geometry is interpreted alongside those factors. Each bout is described by where the female stands, and position and song are linked in the same records.",
    },
    38: {
        1: "pC2 neurons integrate visual and auditory signals, while P1a is a courtship-related subset of P1 neurons. Roemschied and colleagues activated these populations separately and together with descending pIP10 to examine how brain input changes song sequencing. Each population is tested alone and in combination, and the combined activation is measured against each single population.",
    },
    39: {
        2: "dPR1 calcium signals preferred pulse and declined during sine. TN1A-2 signals remained active during both modes, with stronger activity during sine. Response changes were aligned around transitions on a 0.5 s timescale, which reveals the timing of each change, and each neuron is aligned to the same transition.",
    },
    41: {
        1: "A heterogeneous neuronal class can contain subpopulations with different activity preferences. Shiozaki and colleagues imaged broader TN1 populations during alternating song, tracking calcium signals aligned to the transitions between pulse and sine. Each neuron is aligned to the same transition, which allows subpopulations with different preferences to be identified.",
    },
    43: {
        3: "These neurons were classified as cholinergic and are therefore likely excitatory. Acetylcholine is the transmitter indicated by that classification. Each connection is treated as an excitatory input, which is consistent with the pulse-related activity, and the same transmitter classification is applied to each neuron.",
    },
    44: {
        3: "Engineered D. virilis females produced male-typical song in a subset of pairings, and at much lower total amounts than males. A conserved transcription factor therefore has a species-specific output. Each pairing is scored for its song, which makes the species difference measurable, and the female totals are expressed in the same units as the male totals.",
    },
    45: {
        3: "These outcomes differ from the strong suppression of egg laying in engineered D. melanogaster females. The contrast shows that fruitless effects vary by species, so a single binary-switch model of the gene is too simple. Effects on male song, female receptivity and fertility each vary by species and dose, and each outcome is interpreted within its own genetic background.",
    },
}

INSERT = {
    3: {
        2: "Pulse and sine bouts occur at irregular times during the approximately 25 min of courtship. The shared timeline allows the analysis to ask whether a change in movement comes before or after a change in song mode. Each bout is therefore paired with the movement recorded just before it, so the sequence of events can be read in order.",
        3: "Simultaneous traces also distinguish the male's own motion from the female's motion and from the sound source. Movement-associated noise is therefore kept out of the song measures, and each partner's trajectory is held on its own track throughout the analysis.",
    },
    6: {
        1: "Distance between the two flies changes how much visual information each partner receives. In this experiment, the proportion of pulse song rose as the flies moved farther apart. The effect was measured across several distance bands, which were defined on the same scale for every pair, so each band reflects the same spacing for all pairs.",
        2: "Darkness changed the mix of song modes, with males tested in the dark producing more pulse song. Both lighting conditions still produced song, so the change lies in the composition of the song rather than in its presence. Both conditions covered the same range of distances, so the lighting change is the main difference between them, and each condition is paired with its own illuminated control.",
    },
    9: {
        1: "A splice allele changes the sequence that controls one step in RNA processing. Demir and Dickson designed alleles that change the sex-specific P1 splice decision, while other fruitless functions stay intact. Each allele therefore tests one choice in the gene. The wild-type control was run under the same conditions as each allele.",
        2: "The alleles were verified at the transcript level and at the level of FruM protein in adult brains. A forced female-type allele and a forced male-type allele were checked in the same tissue, so their molecular outputs can be read side by side. Each behavioral result can be linked to a known molecular change in this way.",
        3: "Because each allele changes one decision, a phenotype can be attributed to that decision. The contrast between the two forced patterns shows which courtship features follow from the male-type splice and which follow from the female-type splice. Each phenotype is therefore traced to a single molecular switch.",
    },
    12: {
        3: "Behavior, not genital anatomy, carries this reproductive effect, so it is interpreted as a change in what females do. The mating and egg-laying results agree, which makes suppression of female reproductive behavior a coherent outcome of the male splice. The three readouts together describe one reproductive phenotype.",
    },
    15: {
        3: "The distinct profiles of the isoform mutants indicate that each isoform contributes a different part of the courtship network. The mutants show that a single gene can influence several outputs through separate protein products. Each isoform's profile is recorded against the same set of measures, so the profiles line up across mutants.",
    },
    18: {
        2: "Knockdown in aSP4 or vAB3 feminized characteristic arbors and impaired courtship in the dark. Pulse amounts measured in light and in darkness divide the visual from the nonvisual contribution. The dark measure isolates the part of courtship that runs without sight. Both light conditions use the same pairing and the same measures.",
        3: "P1 neuron presence depended on the sex-determination gene doublesex as well as on fruitless. Each neuronal class is assessed for its dependence on both genes, and the combined effects are recorded with the same courtship measures. Those combined results apply across all of the tested classes.",
    },
    24: {
        2: "Across five genetic patterns, the interval shortened by about 5.4–7.0 ms for each degree of temperature increase. Wild-type intervals changed by about 1.0 ms per degree, so the vPR6 effect is several times larger than the ordinary temperature dependence of song. Each temperature step is plotted on the same baseline.",
        3: "The effect was associated with patterns containing vPR6 rather than with every song-promoting pattern. Every pattern is plotted on the same scale as the wild-type baseline, which links vPR6 activity to the timing of the pulses. The timing result therefore reflects the vPR6 neurons, not song in general.",
    },
    27: {
        3: "The result supports an inhibitory contribution to coordinating competing wing movements. Bilateral extension is the defect that inhibition normally prevents, and each male's posture is recorded against its matched control. Bilateral and unilateral posture are contrasted within each genotype.",
    },
    30: {
        1: "Regional restriction distinguishes a perturbation in the brain from one in the nerve cord. Amin and colleagues confirmed each expression pattern anatomically before scoring behavior, so the region of each effect is known. Each expression pattern is checked before its behavior is measured.",
        2: "Nerve-cord knockdown reproduced bilateral wing extension and abnormal song. Brain-restricted knockdown did not reproduce those motor defects, and instead impaired courtship conditioning after exposure to an unreceptive mated female. The regional results are all measured against the same conditioning test.",
        3: "The regional dissociation assigns different inhibitory roles to motor control and to learned changes in courtship. Each role is tied to the region where it was measured, so the two outputs are scored in the same knockdown groups. Each region's output is reported on its own.",
    },
    33: {
        3: "Close frontal positions also increase opportunities for contact and change visual motion. The geometry is interpreted alongside those factors, and each bout is described by the female's position at the time it occurred. Each bout's geometry is recorded together with its song.",
    },
    36: {
        3: "The opposing dynamics support a functional subdivision within TN1. Each subgroup is defined by its response timing, which places the two groups in different roles in the wing circuit. The subgroups are recorded side by side in the same preparations, so their timing can be lined up directly.",
    },
    39: {
        1: "A nested activation pattern means that one active population includes another as a subset. Shiozaki and colleagues imaged identified nerve-cord neurons while flies alternated pulse and sine, with wing vibration preserved by attaching parts of the legs. Each neuron is recorded alongside the other recorded classes.",
    },
}

# Paragraphs that were 4 lines or that carried the source wording "compared" (scaffolding/RULES.md).
BODY[16][3] = "The dependence on illumination is consistent with altered access to nonvisual courtship information. The result links light availability with the FruC phenotype. The dark result carries the sharpest signal, because it removes visual cues from courtship, so the behavior that remains in darkness reflects nonvisual input."

INSERT[6][3] = "Visual information therefore takes part in choosing between pulse and sine. Distance and light act on the same song output, so the two cues can be placed in one framework. The framework links each change in song mode to the sensory conditions present at the time it occurred."
INSERT[21] = {
    1: "A population that starts singing and a population that selects a wing can be separate circuits. von Philipsborn and colleagues used stochastic expression to activate P1 neurons on one side or on both sides. Each male's wing choice was recorded against the side of activation, which tests whether the two functions share neurons.",
    2: "Unilateral activation did not impose a consistent wing choice on the animals. Males chose either wing across repeated bouts and normally avoided extending both wings at once. The wing record therefore stands apart from the side of the activated neurons.",
    3: "The dissociation places wing selection downstream of, or parallel to, the initiation function. Each bout is scored for its wing, and the activation record and the wing record are kept in the same animals, so the two can be lined up for each male.",
}
INSERT[24][1] = "Interpulse interval is the time between successive pulses in a pulse train. von Philipsborn and colleagues tested whether activation of vPR6 changed this interval, rather than producing an undifferentiated wing movement. Pulse timing is the readout that distinguishes these two outcomes. The interval is measured for each pulse in the train."
INSERT[33][2] = "Complex bouts occurred more often when the female was closer and more directly in front of the male. Their duration was longer than that of simple bouts, with distributions spanning about 0 to 3 s. Complex bouts therefore pair a close frontal position with a longer song episode, so position and song duration sit in one record."
INSERT[36][2] = "Some TN1 calcium signals tracked the stimulus. Others were anticorrelated and peaked after the stimulus was removed. The recordings kept response timing over several seconds and anatomical positions at a 20 µm scale. Each cell's timing is therefore tied to its position and to the stimulus period."
INSERT[39][2] = "dPR1 signals preferred pulse, whereas TN1A-2 signals remained active during both modes and were stronger during sine. The responses were aligned around transitions on a 0.5 s timescale, so the timing of each change is visible. Each signal's rise and fall is therefore located relative to the moment the song mode switched."
INSERT[39][3] = "The observations support shared circuit participation with an additional pulse-related population. The pulse and sine populations overlap in a defined way, which is the basis of the nested model. The overlap means that the pulse-related population is contained within the broader population active during song."
INSERT[42] = {
    1: "pMP2 is a descending neuron class that connects the brain and nerve cord. Shiozaki and colleagues recorded its calcium activity alongside pIP10 while flies alternated pulse and sine. Both pathways were imaged on one timeline, so their activity can be placed at the same moment in each song transition.",
    2: "pIP10 remained active during both song modes. pMP2 was pulse-selective, increasing at sine-to-pulse transitions and declining at pulse-to-sine transitions. Each transition is measured in both pathways on the same 0.5 s scale, which allows the two dynamics to be set side by side.",
    3: "The two pathways provide differential input to the thoracic network. Each descending pathway contributes according to its own dynamics, and the labeled anatomy identifies which pathway carries each pattern. The pulse-selective pattern therefore comes from a different source than the pattern active in both modes.",
}
