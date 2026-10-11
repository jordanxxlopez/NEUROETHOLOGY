"""Paragraph overrides for Lecture 36 (scaffolding/RULES.md): 5-7 lines, no filler. Applied by L36.py.

BODY[original slide] is the third body paragraph (5-7 lines).
INSERT[slide the insert follows] lists the three insert paragraphs; None keeps the source paragraph.
"""

BODY = {
    2: "Stimulus intensity and response amplitude can be measured separately in this preparation. Because the jet strength sets the size of the contraction, the same animal can be tested across a range of intensities. Each intensity is paired with the response it evokes, so the stimulus-response relation can be drawn for one animal.",
    3: "A smaller contraction can arise from sensory adaptation, weaker central transmission, altered motor-neuron firing or muscle fatigue. Intracellular recordings in the same preparation identify which of these sites changed. The sites lie at different points along the reflex pathway, so each candidate can be tested in turn.",
    4: "The animal keeps the capacity to contract its gill throughout habituation. Recovery of this kind points to a reversible change rather than to injury or to failure of the muscles. The decrement therefore lies in the control of the response, which can return once the stimulus is withheld.",
    6: "The isolated ganglion contains a defined sensory–motor pathway, so the connection can be recorded directly at each stimulus. Intact preparations extend the same recordings to the behavior of the whole animal, so the neural change can be linked to what the animal does.",
    8: "Activating the motor cell directly skips sensory processing, so downstream changes can be isolated from changes at the sensory input. The motor cell's firing then sets the siphon response. The one-third estimate describes how far siphon flaring changes in this preparation, so the output of that cell is measured against the same baseline.",
    12: "Depression follows its own time course, independent of the initial strength of a connection. Activity appears to silence functional release sites in a stimulus-dependent way. The measured kinetics are the evidence for that account, because they track how fast transmission falls during repeated stimulation.",
    14: "Retention lasting weeks indicates that a simple withdrawal system supports enduring nonassociative learning. The retained change could rest on persistent synaptic efficacy, on altered connectivity or on changes elsewhere in the circuit. Each candidate predicts a different pattern of change at the synapse, so the sites can be tested in turn.",
    15: "The measured outcome is withdrawal behavior, which records how much of the change lasts across days. Spacing effects of this kind lead to later experiments that test the molecular events under different temporal patterns. Those experiments ask which steps must occur during each spaced interval for retention to last.",
    16: "The counts describe labeled structures in the arbor, and each swelling is identified by its position along the arbor. A changed varicosity count accompanies the remembered response. The individual swellings that carry the change are identified separately, so each one can be followed across the training.",
    17: "The ganglion preparation keeps the enhanced synapse in place after the behavioral context is removed. Interneurons, other motor cells and peripheral targets could carry further parts of the sensitization. Each of these routes can be traced by recording from its own cell in the same ganglion.",
    19: "Spike propagation and calcium entry at distant terminals could also change with cAMP. Recordings at the terminals themselves identify the compartment where cAMP acts. Those measurements set the location of the change, so the terminal can be tested alongside the cell body.",
    20: "Kinase activity must be available near the right targets, so the location of PKA is part of the mechanism. The Ht31 result shows that localized PKA signaling is needed for facilitation in this sensorimotor preparation. Blocking the anchoring site therefore changes the outcome of the same serotonin exposure.",
    24: "Facilitation therefore needs a postsynaptic calcium signal in this preparation. The quantal and cAMP results from the sensory side remain valid, and a single connection can change on both sides at once. Together, the two sides show that facilitation is shared across the synapse, not confined to the sensory terminal.",
    25: "Several independent interventions converge on the same calcium-store pathway, with each one timed to the same serotonin exposure. The postsynaptic route from serotonin to enhanced transmission runs through these stores. Each intervention reaches the same endpoint, so the stores can be treated as one shared step.",
    26: "Calcium-dependent insertion or regulation of postsynaptic AMPA receptors fits these results. Presynaptic release enhancement and postsynaptic receptor regulation can work together, and they differ in onset and persistence. The two mechanisms can be ordered in time by measuring each one at successive intervals after serotonin.",
    31: "A labeled contact is a structural measure, and its release probability is measured physiologically in the same preparation. The contact addition is linked to the sensitization of the behavior at an identified output cell. Structure and function are therefore recorded in one preparation, so each added contact can be assessed for its release.",
    32: "Synapsin is a candidate effector that links serotonin-dependent gene regulation to persistent changes in synaptic function. Its requirement is tested by knocking it down in the same cultures. Knockdown shows whether synapsin is needed for the enhancement that serotonin produces.",
    33: "Serotonin-dependent signaling reaches synapsin production through CREB1 binding at this promoter. Other transcriptional responses of long-term facilitation are assigned to their own target genes. Each target is linked to its own binding site, so the promoter results sit among the other responses.",
    34: "The chromatin changes appear alongside the CREB1 binding in the same region of the promoter. Timing experiments identify the first modification in this sequence. The later changes can then be ordered relative to that first step, so the sequence of events is traced in time.",
    35: "Synapsin is required for facilitation under this protocol, and it is one component of persistent enhancement. Vesicle organization, receptor signaling, transcription and synaptic structure interact with it. Each of these processes can be followed alongside synapsin, so its place in the chain is traced directly.",
    36: "Isolated processes hold a local pool of RNA that responds to modulatory signaling without the nucleus. Local translation therefore adds a control point for facilitation alongside transcription. Both control points act on the same synapse, so their contributions can be measured within one preparation.",
    37: "ApCPEB4 lacks the prion-like domain of ApCPEB and binds different RNA targets. Its role in starting persistent change is distinct from the maintenance role of ApCPEB. The two proteins therefore divide the work of persistent change between them, with each one assigned to its own phase.",
    38: "The mutant protein changes more than its phosphorylation site, so it is tested against the wild-type protein in the same cultures. The PKA-to-ApCPEB4 link is shown in the cultured connection. Keeping the mutant and wild-type proteins in one culture holds every other factor fixed.",
    39: "The ApNT isoform with the stronger secretion profile reaches the ApTrk receptor on distant neurites. Receptor activation in those neurites is tested with functional assays. Each isoform's reach is therefore linked to its secretion profile at the distant site.",
    41: "A transcription factor is therefore needed for persistent synaptic enhancement under this protocol. CREB1 works alongside other regulators, and partial loss of it weakens an otherwise effective training pattern. The regulators act in the same neurons, so their contributions can be measured within one training protocol.",
    42: "Rescue was partial, and its size depends on the preparation. Raising cAMP signaling compensates for part of a molecular deficit, and the same recordings identify the neurons in which it occurs. Those recordings place the compensation in the neurons that carry the enhancement.",
    44: "Recovery after retraining points to a retained trace of the original training. The retraining response shows that sensitization can be expressed again after the change has been reduced. Full elimination of the training-dependent change would leave no such response, so the retained trace is the basis of recovery.",
    45: "Different memory phases depend on different molecular steps. Cellular release, postsynaptic regulation, structural growth and gene regulation each contribute at a different level of this learning system. Each step is tied to its phase, so the phases can be assigned to their molecular causes.",
}

INSERT = {
    3: [
        None,
        "Shorter intervals produced a faster decline in contraction, while longer intervals slowed it. Responses commonly fell toward about 25% of the initial amplitude across the range of intervals tested. The decline therefore depends on the interval between stimuli, with the stimulus strength held constant.",
        "Stimuli delivered at closer intervals leave less time for the response to recover between trials. Recovery between trials is therefore part of what determines how far responsiveness falls across a series. The final level of responsiveness reflects the balance between each stimulus and the recovery that follows it.",
    ],
    6: [
        "An identified gill motor neuron receives a direct excitatory input from the skin of the siphon. Brief stimuli to that skin depolarize the motor cell, and this depolarization is the first measurable link between touch and contraction. The link runs from one defined synapse to one identified cell.",
        "Castellucci and colleagues recorded the response in the same cell on repeated trials. Repeated stimulation reduced the response, and the reduction accumulated from one trial to the next across each session. Because the same cell is recorded throughout, each trial's change is measured against the trials before it.",
        "Each EPSP in the identified cell can be traced to one defined synapse. The cell's large size makes it possible to record that synapse repeatedly over the whole session. Repeated recordings from one synapse show how its strength changes as the session proceeds, which ties the behavioral decrement to a single connection.",
    ],
    9: [
        None,
        "Facilitation appeared in sensory neurons whose receptive fields covered the test site and in sensory neurons activated from elsewhere on the body. The modulatory action of shock therefore reaches more inputs than the one that was tapped during habituation. This spread explains why shock changes responses to touches at sites that were not tapped during habituation.",
        "The change is spread across many connections, so its synaptic basis appears at several sites. Motor-cell firing, complex postsynaptic potentials and monosynaptic potentials each follow this spread. Each measure tracks the same change, so the spread is seen at more than one level of the circuit.",
    ],
    12: [
        "Gover and colleagues evoked sensory action potentials at 15 s intervals in strong and weak sensory–motor connections. The two kinds of connection differed in their initial transmission and in their paired-pulse behavior, yet they depressed at similar rates. Both kinds were tested under the same stimulation schedule, so the rates can be set side by side.",
        "Applying 4-aminopyridine broadened sensory spikes and increased calcium-dependent release. This change raised initial transmission while depression stayed the same speed, which runs opposite to what a simple depletion account would predict. A depletion account would have predicted faster depression with the larger initial response.",
        "The depression kinetics point to silencing of functional release sites in a stimulus-dependent way. Activity itself drives the silencing rather than the strength of the initial connection. Because the silencing follows the stimulation, the sites that are silenced are the ones that were recently active.",
    ],
    15: [
        "Carew and colleagues gave forty habituation trials in one day to one group, and the same total spread over four days to another. The massed schedule concentrated the experience in one session, and the spaced schedule distributed it across days. Both groups received the same number of trials.",
        "Both schedules produced substantial decrement during training. Spaced training yielded stronger retention after 24 h and after one week than massed training. The session-level decline looked similar, but the lasting change did not, so retention marks the difference between the two schedules.",
        "Retention was measured as withdrawal behavior, and it could be tested in a restrained preparation as well. Spacing effects of this kind set up the later experiments that examine the molecular events under different temporal patterns. Those experiments then ask which steps must occur during each spaced interval.",
    ],
    18: [
        "Brunelli and colleagues compared serotonin, dopamine and octopamine at the sensory-neuron connection onto a gill motor neuron. Serotonin changes how an existing pathway responds, so the same connection can be measured before and after each neuromodulator. Each modulator is applied to the same identified connection.",
        "Sensory neurons were first depressed by repeated stimulation. Serotonin applied during a 2.5 min rest increased the subsequent synaptic responses. Rest periods without serotonin produced no such enhancement, so the drug accounts for the increase. The enhancement therefore follows the drug, not the rest itself.",
        "The antagonist cinanserin reversibly reduced the facilitation evoked by connective stimulation, while the repeated-stimulation depression stayed intact. This pattern identifies a serotonergic route to facilitation that runs alongside the depression. The two processes act through separate routes, so each can be blocked on its own.",
    ],
    21: [
        None,
        None,
        "Each synaptosome preparation contains many terminals, so the measured increase is an average across them. Nuclear type 1 PKA and synaptic type 2 PKA carry complementary roles in this account. Each role is assigned by the subcellular location in which each subunit is found.",
    ],
    24: [
        None,
        None,
        "Facilitation therefore needs a postsynaptic calcium signal in this preparation. A single connection can change on both sides at once, so the presynaptic and postsynaptic results combine into one account of facilitation that spans the synapse.",
    ],
    27: [
        None,
        "Control preparations increased siphon withdrawal after shock, whereas postsynaptic toxin blocked this dishabituation. Motor activity recorded alongside the movement linked the cell-targeted treatment to a measured behavioral change. The toxin therefore removes the behavioral increase that shock otherwise produces.",
        "Postsynaptic exocytosis in the siphon motor cells contributes to the behavior. The same requirement carries over to other gill responses and to sensitization protocols, which share the same motor cells. Each protocol can therefore be tested for the same postsynaptic requirement, using the same toxin.",
    ],
    30: [
        None,
        None,
        "A critical window fits the production of proteins that start or stabilize persistent change. Identifying those proteins, and how quickly they turn over, would show which products the window protects. Their locations in the cell would then place each product at its site of action.",
    ],
    33: [
        None,
        None,
        "Serotonin-dependent signaling reaches synapsin production through CREB1 binding at this promoter. Other transcriptional responses of long-term facilitation are assigned to their own target genes. Each target is linked to its own binding site, so the promoter results sit among the other responses.",
    ],
    36: [
        None,
        "Severed neurites allowed local responses to be recorded apart from delivery by the cell body. Serotonin increased reporter expression in these isolated processes. Translation-related controls showed that the increase is independent of new transcription, which places the response in the processes themselves.",
        "Isolated processes hold a local pool of RNA that responds to modulatory signaling without the nucleus. Local translation therefore adds a control point for facilitation alongside transcription. Both control points act on the same synapse, so their contributions can be measured within one preparation.",
    ],
    39: [
        None,
        None,
        "The ApNT isoform with the stronger secretion profile reaches the ApTrk receptor on distant neurites. Receptor activation in those neurites is tested with functional assays. Those assays show whether the secreted isoform reaches the receptor and activates it at the distant site.",
    ],
    42: [
        None,
        "Control siRNA and vehicle groups ran in parallel with the CREB1 knockdown. CREB1 knockdown impaired long-term facilitation. Control-RNA synapses reached about 184% of their pretest amplitude, whereas CREB1-siRNA synapses reached about 121%. The gap between the two groups is the measure of the knockdown's effect.",
        "A transcription factor is therefore needed for persistent synaptic enhancement under this protocol. Partial loss of CREB1 weakens an otherwise effective training pattern while the neurons remain responsive. The continued responsiveness of those neurons places the deficit in the persistence of the change.",
    ],
}
