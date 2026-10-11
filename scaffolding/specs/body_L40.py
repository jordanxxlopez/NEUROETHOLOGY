"""Body-text rewrites for Lecture 40 (scaffolding/RULES.md). Figures, captions and videos are untouched."""

body = {
    2: [
        "**Optogenetics** gives control over cell activity by making selected cells express a light-sensitive protein. A **descending neuron** relays signals from the brain to the ventral nerve cord, a longitudinal structure with motor networks that organize movement. Cande and colleagues placed the light-gated channel CsChrimson into identified descending neurons of adult flies.",
        "Flies received 15 s pulses of red light separated by 45 s recovery periods. Flies fed retinal, the light-absorbing cofactor the channel needs, raised how often they occupied particular grooming or locomotor behaviors. Genetically matched flies without the cofactor served as the control for the light itself.",
        "**Sufficiency** means that activating the tested cells can produce a response under the assay conditions. A proposed circuit arrangement by Inagaki and colleagues places the courtship interneuron P1 upstream of the descending population pIP10, which links optical input to a defined motor output in that proposed pathway.",
    ],
    3: [
        "**Channelrhodopsin-2**, or ChR2, is a membrane protein from the green alga Chlamydomonas reinhardtii that contains retinal. Its ion channel forms a pathway for charged particles to cross the membrane. Nagel and colleagues expressed ChR2 in frog oocytes and mammalian cells to learn what the protein does when light reaches it.",
        "Illumination near 450 nm produced currents that were missing from uninjected oocytes. Voltage clamp holds the membrane at a chosen voltage while an amplifier measures the current. Changing the held voltage changed the size and direction of the current, a pattern that fits a **passive conductance** rather than an ion pump.",
        "A truncated construct containing the first 315 amino acids kept its channel function. The light-gated conductance therefore sits within the membrane-spanning portion of the protein, which forms the pathway for charged particles. The protein carries the current itself rather than relaying it through another molecule.",
    ],
    4: [
        "**Ion selectivity** sets which charged species a channel admits. Nagel and colleagues replaced the external salts around ChR2-expressing oocytes while measuring the response to the same blue light. Cations carry positive charge, and anions carry negative charge.",
        "Photocurrents depended on the cation available in the solution. Replacing external chloride with aspartate left the current and its **reversal voltage** almost unchanged. The reversal voltage is the membrane voltage at which the net current changes direction. Calcium passed through ChR2, while magnesium permeated the channel to a negligible degree.",
        "At pH 9, a small current remained in a solution containing the bulky cation N-methyl-D-glucamine, and that remnant disappeared. Its loss identified a proton contribution at lower pH. Together these substitution controls support cation conduction through the channel.",
    ],
    5: [
        "A light-evoked current could come from the expressed protein itself or from a signaling pathway that opens a different channel. Nagel and colleagues recorded ChR2 in **excised membrane patches**, membrane fragments removed from the cell so that the internal solution could be controlled.",
        "Photocurrents persisted after the soluble contents of the cell were replaced. A 10 ns laser flash opened the channel with a rise time of about 200 µs or faster. Closing was much slower and depended on intracellular pH, taking roughly 10 to 400 ms across the conditions tested.",
        "Rapid opening and persistent current support **direct gating**, in which light opens the channel without a diffusible messenger inside the cell. The slower closing means that the electrical response can outlast the light pulse, because the closing rate depends on intracellular pH.",
    ],
    6: [
        "Boyden and colleagues delivered a ChR2 fusion with yellow fluorescent protein into cultured rat neurons, using a lentiviral vector, a modified virus that carries the expression construct. The fluorescent tag marked the expressing cells and the membrane-associated processes that extend from them.",
        "Blue light between 450 and 490 nm generated an average peak **inward current** near 496 pA, followed by a smaller sustained current near 193 pA. Neurons carrying the fluorescent tag alone gave no light-evoked response, so the electrical effect came from the channel rather than from fluorescence or illumination.",
        "Inward current depolarizes the neuron, making its internal voltage less negative. When that voltage reaches firing threshold, the neuron produces an **action potential**, a rapid regenerative change in membrane voltage. Light therefore drives spikes in an expressing cell without requiring knowledge of its natural synaptic targets.",
    ],
    7: [
        "An **action potential** is a brief regenerative shift in membrane voltage that conveys a neuron's signal. Boyden and colleagues recorded neurons during repeated 10 to 15 ms light pulses, comparing the timing of evoked spikes across repeated stimulation sequences.",
        "The same pulse sequence gave highly repeatable spike patterns, yet some individual pulses failed to evoke a spike. In two irregular protocols about 76% and 85% of pulses drove spikes successfully. Spike reliability fell at higher stimulation rates in the 5 to 30 Hz range.",
        "Continuous illumination produced a precisely timed first spike followed by less precisely timed activity. A pulse train therefore sets a controlled input, while the spike output varies from one neuron to another. Each experiment must check the spikes that the light actually produces in its own neurons.",
    ],
    8: [
        "Govorunova and colleagues put light-sensitive proteins from the cryptophyte alga Guillardia theta into mammalian cells. The two proteins, GtACR1 and GtACR2, act as **anion channelrhodopsins**, light-gated channels that carry negatively charged ions instead of the positive ions carried by ChR2.",
        "Changing external sodium, potassium or calcium left the photocurrent reversal in place. Replacing chloride with a nonpermeant anion shifted the reversal, which identified chloride as the carried ion. Membrane voltage was stepped in 20 mV increments while the ion substitutions supplied the selectivity controls.",
        "GtACRs produced an inward current in a high-chloride recording solution. The voltage effect of that current depends on the neuron's chloride gradient and its starting membrane voltage. The same channel can therefore excite one neuron and suppress another.",
    ],
    9: [
        "A **chloride equilibrium potential** is the voltage at which the electrical and concentration forces acting on chloride balance. When an anion channel opens, the membrane voltage moves toward this value, so the effect depends on the ionic conditions of the cell rather than being fixed.",
        "In cultured rat neurons, GtACR2 photocurrent reversed near −88 mV. Illumination suppressed current-evoked spikes in trains up to at least 25 Hz. In a ramp protocol, full suppression occurred at a light intensity of 0.005 mW/mm². The ramp tested a graded range of light intensities.",
        "Expressing neurons kept their dark-state electrical properties and morphology, so the expression left the cells intact. Silencing was validated under the measured recording conditions, and each new cell type or species needs its own check of the chloride gradient before inhibition is assumed.",
    ],
    10: [
        "The adult fly's cuticle, its external covering, reduces the light that reaches internal neurons. Inagaki and colleagues measured light transmission and compared several opsins, the retinal-binding light-sensitive proteins, in peripheral and central neurons of intact _Drosophila melanogaster_.",
        "The red-shifted channelrhodopsin ReaChR responded to 627 nm light. In gustatory receptor neurons, which detect chemical taste cues, 100 ms pulses at 1 Hz produced timed spiking and **proboscis extension**, the outward movement of the feeding appendage.",
        "ReaChR also drove responses from central neurons under conditions where several blue-sensitive variants had no effect. Cuticle penetration, protein expression and membrane trafficking all contributed to how well the light worked. Red illumination also reduced a concern about visual stimulation.",
    ],
    11: [
        "Light can change behavior through the animal's normal sensory pathways as well as through an introduced opsin. Intact flies carrying different opsins were set against no-opsin controls by Inagaki and colleagues, with identical light and scoring conditions.",
        "ReaChR activation evoked responses that depended on the targeted population, including wing extension and side walking, and no-opsin controls showed none of these responses. With 5 ms red-light pulses aimed at courtship-related P1 neurons, response probability rose with pulse frequency and reached a fitted midpoint near 38.3 Hz.",
        "A dose-response relationship links stimulation strength to response probability, so the curve describes how an induced action scales with input. At high intensities some populations produced **paralysis** in place of the lower-intensity behavior, so control genotypes and intensity jointly set which neuronal contribution can be inferred.",
    ],
    12: [
        "Courtship control involves P1 neurons, a male-specific set of brain interneurons. An interneuron links processing stages rather than serving directly as a muscle's motor output. After 7 days of single or group housing, Inagaki and colleagues measured how readily ReaChR activation produced wing extension. Wing extension served as the measured readout of that circuit.",
        "Males housed alone reacted to weaker red light than males housed in groups. Activating the descending courtship neurons pIP10 instead produced no housing-dependent shift in sensitivity. Both experiments used matched stimulation methods while the social experience of the animals changed.",
        "Experience therefore changes how strongly activation at P1, or at a downstream stage before the pIP10 output, drives wing extension. Social history thus modifies the behavioral consequence of activation while the light stimulus stays the same.",
    ],
    13: [
        "The **split-GAL4** system restricts expression by combining two separately expressed parts of a transcriptional activator, a protein that switches on gene expression. Gene activation occurs where the two expression patterns overlap strongly. The intersectional strategy was the one Cande and colleagues applied to reach sparse descending-neuron groups.",
        "The actuator CsChrimson converted 617 nm illumination into a timed depolarizing stimulus. Experimental and control flies carried the same genetic construct, and experimental flies alone received supplemental retinal. Repeated 15 s activation epochs tested the behavioral effects of the targeted population.",
        "A sparse expression pattern sharpens anatomical specificity. When several cells express the actuator, a behavioral phenotype can still arise from more than one cell, so the expression pattern of each screened line must be verified. Restricted access and physiological efficacy are separate requirements that each line has to meet.",
    ],
    14: [
        "Behavior can shift while walking speed stays nearly constant. Cande and colleagues recorded freely moving flies at 100 frames per second, aligned their body images and represented postures over time in a low-dimensional behavior space, a map that groups similar movement patterns together.",
        "Different regions of the map contained anterior grooming, wing and abdomen movements, slow postures and locomotion. **Occupancy** measured how often a fly performed the movements assigned to each region. Occupancy during red-light activation, set against matched controls, distinguished action-specific effects from a general rise in activity.",
        "The map is an empirical description of movements sampled in this arena rather than a map of neural anatomy. Sampling at 100 frames per second sets the time scale of the movements the map captures, and the flat chamber sets which behaviors can appear. A quantitative classifier gives reproducible measurements within those bounds.",
    ],
    15: [
        "A **motor module** is a coordinated part of behavior that can be recruited on its own, without triggering a complete behavioral sequence. Cande and colleagues asked whether activating descending neurons concentrated movement into particular regions of the behavior space they had measured.",
        "During 15 s red-light epochs, many experimental flies showed reduced **behavioral entropy**, a measure of how broadly their activity spread across available actions. Matched controls without retinal showed no such population-level reduction. Most effective lines favored one behavioral region.",
        "Modular recruitment, under these arena and stimulation conditions, means that a single descending population can bias behavior toward one class of actions. Selective tests of normal activity, necessity and context offer the way to determine how many distinct actions each targeted neuron commands.",
    ],
    16: [
        "Light-driven activation engages a circuit that is already active during behavior. Cande and colleagues related each fly's movement in the 1.5 s before stimulation to its movement during the first 1.5 s of red-light activation. Its output therefore depends on what the animal is already doing.",
        "For some descending-neuron lines, the action after activation depended strongly on the action that came before it. **Mutual information** measures how much knowing the earlier behavioral state predicts the later one, and for many lines this dependence exceeded that in matched no-retinal controls.",
        "The result supports **state-dependent recruitment**, in which the same activation produces different actions depending on the current behavior. Sensory input, the activity of other neurons and the state of local motor networks can each contribute to this context effect.",
    ],
    17: [
        "Cilia, which are microscopic moving projections on specialized cells, propel the marine annelid _Platynereis dumerilii_. At about 72 h after fertilization, locomotor cilia form a main band called the prototroch, along with additional bands distributed along the larval trunk.",
        "Verasztó and colleagues brought together scanning electron microscopy, fast video and calcium imaging. The different locomotor bands stopped beating together and resumed together, and each arrest coincided with a coordinated rise in calcium-indicator fluorescence across the ciliated fields.",
        "A **calcium indicator** changes fluorescence as intracellular calcium rises and falls, giving an indirect readout of cell activation. The synchrony links a distributed set of effectors to one shared event, and identifying the neurons that trigger that event takes separate experiments.",
    ],
    18: [
        "A **connectome** maps the identified neural connections inside a reconstructed nervous system. Using serial transmission electron microscopy on a 3-day-old Platynereis larva, Verasztó and colleagues followed neurons and their synaptic contacts, matching them to where ciliated cells sit across the body.",
        "The large MC neuron and the paired Loop neurons formed extensive contacts with the locomotor ciliary bands. Molecular labeling and cell morphology supported a cholinergic identity, meaning that these cells use acetylcholine as their transmitter. Axons reached several positions along the body.",
        "According to this reconstruction, a small set of neurons can coordinate effectors that lie far apart. A synaptic contact by itself sets neither the timing nor the sign of the functional response, so calcium recordings and selective interventions are needed to show which reconstructed neurons take part in arrests.",
    ],
    19: [
        "Verasztó and colleagues imaged identified ciliomotor neurons and the prototroch with GCaMP6s, a genetically encoded calcium-sensitive fluorescent protein. In 2-day-old larvae, cell position and reconstructed morphology linked each recorded cell to the anatomical circuit.",
        "Fluorescence in cMNvl and cMNd, two catecholaminergic ciliomotor cells, rose in step with the ciliary band. The cMNATO cell tended to vary in the opposite direction. Catecholaminergic identity marks a transmitter-related molecular class, while the functional sign of each cell comes from its activity pattern.",
        "These phase relationships place the neurons in populations with different timing within the coordinated rhythm. Calcium fluorescence integrates activity over time, so opposite phases show **differentiated circuit participation** rather than the millisecond timing of individual spikes.",
    ],
    20: [
        "**Ablation** destroys a chosen cell so that its contribution can be tested. Verasztó and colleagues used a pulsed laser to ablate the identified MC neuron, then compared prototroch calcium activity and ciliary arrests before and after the procedure. Calcium activity and arrests were the two readouts of the rhythm.",
        "Removing MC abolished the prominent rhythmic prototroch activity and sharply cut the number of arrests. In intact imaged preparations the MC calcium cycle had a median period of about 71 s. Blocking **nicotinic acetylcholine receptors** with α-bungarotoxin uncoupled the ciliary response, while the MC neuron kept cycling.",
        "The two interventions distinguish the source of rhythmic neuronal activity from the cholinergic transmission that drives the effector. The MC neuron therefore contributes both to the rhythm and to its receptor-dependent output, and the reconstructed network contains additional cholinergic neurons that also feed into arrests.",
    ],
    21: [
        "A **hydrodynamic stimulus** moves water locally and can deform sensory structures. Bezares-Calderón and colleagues tested Platynereis larvae with a vibrating tungsten filament and observed ciliary arrest, body contraction and elevation of paired appendages called parapodia.",
        "High-speed recordings at 230 to 350 frames per second resolved the response. Faster filaments pushed the appendages into a wider elevation, and a filament placed farther from the head had to move more forcefully to trigger it. Wide elevation was consistently recruited above about 28 µm/ms under the arrangement tested.",
        "The controlled stimulus ties local water movement to a coordinated defensive action. The dependence on distance supports **near-field sensing**, in which receptors respond to water movement close to the body. Filament speed is the mechanical parameter the experimenter sets, so it provides an input that can be varied and measured.",
    ],
    22: [
        "Each **collar-receptor** neuron bears a sensory cilium ringed by microvilli, which are small projections that form a collar. Bezares-Calderón and colleagues combined electron microscopy with calcium imaging to find these sensory cells in the head of Platynereis larvae.",
        "One collar contained ten thick microvilli linked to the projecting cilium by fine fibers. A vibrating filament placed about 50 µm in front of the head increased calcium-indicator fluorescence in identified head collar receptors. A nearby sensory neuron with a different morphology served as a comparison in the same recording.",
        "The anatomy and the stimulus-evoked activity together support mechanosensory input through these cells. Calcium imaging identifies which sensory population becomes active, while molecular expression and genetic disruption show which proteins the behavioral response requires.",
    ],
    23: [
        "**Polycystins** are a protein family with candidate components for mechanosensory signaling. Bezares-Calderón and colleagues detected PKD1-1 and PKD2-1 expression in larval collar-receptor neurons, then generated inherited loss-of-function mutations with targeted genome editing.",
        "Larvae homozygous for either mutation produced abnormal startle responses to the vibrating filament instead of the normal coordinated response. Sensory-cell morphology was preserved, which argues against a simple loss of the entire receptor cell. Predatory copepods, which are small planktonic crustaceans, caught PKD2-1 mutants more easily in predator tests.",
        "The genetic result shows that PKD1-1 and PKD2-1 are required in the pathway that carries the filament stimulus from sensory cell to behavior. Recordings of mechanically activated current are the measurement that would show how force reaches these proteins.",
    ],
    24: [
        "Larval zebrafish hunt small moving prey with a coordinated sequence of eye and body movements. Eye convergence rotates both eyes toward a common frontal region. A **saccade** is a rapid eye movement, and convergent saccades provide a measurable marker of hunting initiation.",
        "Antinucci and colleagues studied larvae 6 to 7 days after fertilization. In a partly restrained visual assay, small dark moving spots preferentially recruited convergence together with lateral tail movement. About 92% of convergent saccades coincided with tail motion, and the eye-to-tail delay averaged near 12 ms.",
        "**Two-photon calcium imaging** recorded brain activity while the eyes and tail stayed mobile, which ties controlled visual input to the movements of the hunt. Free-swimming activation and ablation experiments then supplied complementary behavioral tests in fully mobile larvae.",
    ],
    25: [
        "Lying close to the retinal input sites and the optic tectum, the **pretectum** is a visual brain region. Retinal ganglion cells carry signals from the eye into the brain, and their axons end in regions called arborization fields. Activity was mapped around the AF7 input region by Antinucci and colleagues.",
        "Calcium responses were measured for prey-like stimuli that evoked convergence and for those that failed to evoke it. Prey-responsive cells followed the visual input, whereas other clusters were more strongly tied to the start of hunting. Their distributions overlapped near AF7 and diverged across the surrounding brain.",
        "This split distinguishes a response to the sensory event from a response tied to the animal's own action. A neuron active near movement onset may contribute to initiation, may receive a related command, or may respond to the movement that follows, and targeted interventions decide among these options.",
    ],
    26: [
        "CoChR, a light-gated cation channel, was expressed by Antinucci and colleagues in single genetically accessible pretectal neurons. Cell morphology identified each targeted neuron, and high-speed video quantified free-swimming responses during repeated 7 s blue-light periods.",
        "Illumination at 470 nm and 0.44 mW/mm² led some single-cell preparations to produce eye convergence, lateralized swim bouts and sustained hunting-like routines without prey. Responsive preparations had a median response probability near 18% during illumination, while light-off trials produced zero such events.",
        "Opsin-negative controls showed no hunting under blue light alone, so the response depends on the opsin. The activated routine includes eye convergence followed by lateralized swimming, which means that a single identified cell can recruit a coordinated motor program.",
    ],
    27: [
        "**Necessity** asks whether normal performance requires the tested component. At 6 days after fertilization, Antinucci and colleagues destroyed fluorescently labeled pretectal cells and then scored free-swimming behavior both before the procedure and the next day.",
        "About 90% of the labeled population was removed. Prey consumption, hunting initiation and the duration of hunting sequences declined. Average swimming speed, escape responses to looming stimuli and the optomotor response, which is swimming driven by moving visual patterns, were retained. Sham ablations removed nearby thalamic cells instead.",
        "The preserved behaviors show that the loss reflects a specific deficit in hunting rather than a general decline in movement or visual responsiveness. The pretectal population therefore contributes to the initiation and maintenance of normal hunting.",
    ],
    28: [
        "The **optic tectum** is a midbrain region that takes part in visual and motor processing. Antinucci and colleagues stimulated a ChR2-expressing anterior-ventral tectal region and compared sighted larvae with mutants that lack retinal ganglion cells because of disrupted atoh7 function.",
        "Blind larvae kept tectal ChR2 expression even though they lacked retinal input. Light stimulation evoked hunting-like behavior more easily in these mutants than in sighted siblings. Evoked routines kept eye convergence and lateralized tail movements, although response probability and duration differed between the groups.",
        "Removing retinal input tests whether ordinary light-driven vision is required for the optically induced action, and the result shows that the action can be recruited through central circuitry. Retinal activation can therefore interfere with the assay itself.",
    ],
    29: [
        "Flyception2, an optical tracking system for brain fluorescence in freely moving adult flies, was developed by Grover and colleagues. The animal is untethered, meaning that no cable links it to the microscope, and external optics follow its head as it moves.",
        "Three glass beads that reflect light, about 30 µm across, outlined a window over the brain. Mirror position was refreshed 1,000 times per second by a tracking loop. **Retroreflection** sends incoming light back toward its source, so the head stays identifiable when two flies' body outlines overlap.",
        "Focus tracked the change in head height that occurred during courtship and copulation. The method keeps social contact in the measurement, which outline-based tracking had disrupted. The approach still uses a surgically prepared imaging window and a bounded imaging arena.",
    ],
    30: [
        "A fluorescence change in a moving animal can come from activity, from altered focus or from a changing tissue orientation. Flyception2 measured calcium-dependent green GCaMP fluorescence together with calcium-independent red tdTomato fluorescence in the same targeted cells.",
        "Both channels were recorded simultaneously at 50 Hz, with excitation at 473 and 561 nm. Taking the ratio reduced fluctuations shared by both channels. Frames were also screened for visible tracking beads, sharpness and excessive motion, and about 75% of frames in 100 s recordings passed these criteria.",
        "These controls strengthen the attribution of fluorescence changes to cellular calcium. Rapid movements or occlusion can remove precisely timed parts of an interaction, so the analysis applies to the behavioral periods that pass the screen.",
    ],
    31: [
        "P1 neurons were imaged by Grover and colleagues as a male moved toward, touched and mated with a female. Neural fluorescence was synchronized with the distance and angle between the two flies, which links activity to the ongoing social interaction.",
        "P1 activity rose during courtship and fell during copulation, even though physical contact continued. After mating, P1 activity returned when the male again approached the female. In a separate targeted population, mAL neurons, which use **GABA** as their transmitter, stayed active across courtship and copulation.",
        "GABA is a transmitter that can reduce the excitation of target cells. The contrasting activity patterns show that circuit recruitment depends on behavioral state, and recordings of this kind complement experiments that activate or remove particular neurons directly.",
    ],
    32: [
        "**Neural telemetry** transmits recorded electrical signals remotely. Szuts and colleagues built a rat-borne system that combines implanted electrodes, a head-mounted amplifier and a radio transmitter carried in a back harness. A short connection links the animal's own boards, and no cable runs to the recording computer.",
        "The electronics processed up to 64 channels, each sampled at 20 kHz, and sent the combined signal to a receiver. Continuous operation lasted about 6 h with the larger battery configuration. The arrangement made recordings possible during outdoor movement and during travel through tunnels.",
        "Wireless access expands the movements and environments available to an experiment, while implant surgery and the carried mass are part of the preparation. The validation covered rats carrying this particular payload and the larger battery.",
    ],
    33: [
        "**Sampling rate** specifies how often a signal is measured, whereas **bandwidth** specifies the range of frequencies the system retains. In the configuration of Szuts and colleagues, electrode voltages passed through a filter between 80 and 2,300 Hz, and each channel was sampled 20,000 times per second.",
        "A simultaneous sample-and-hold stage captured the channel voltages before time-division multiplexing placed successive channels onto a shared output. Synchronization markers identified each channel scan, so the original signals could be rebuilt after radio transmission.",
        "Frequency components removed by the filter stay absent however fast the sampling is. The configuration suited extracellular spike analysis, so hardware settings determine which neural events a behavioral experiment can relate to movement, sensation or task timing.",
    ],
    34: [
        "Wireless recordings need validation of signal fidelity as well as transmission range. Szuts and colleagues compared the same extracellular waveform before and after radio transmission, then tested whether the reconstructed recordings kept distinguishable spike shapes.",
        "The system added less than 4 µV of electrode-referred noise. In line-of-sight tests, recordings at distances up to 60 m kept their spike waveforms and separable waveform clusters. Antenna orientation and a known test signal characterized how signal quality changed with distance.",
        "A **sorted unit** is a putative neuron recognized as one group of similar extracellular waveforms. Retained clustering supports the reliability of this recording chain, so a sorted unit can be linked to a stable waveform cluster even after the signal has traveled by radio.",
    ],
    35: [
        "While Egyptian fruit bats flew between reward sites, Snyder and colleagues recorded from the hippocampus, a region that participates in spatial representation. A light implanted microdrive placed electrodes in dorsal CA1, a hippocampal subregion that histology confirmed after recording.",
        "Bats spontaneously followed reproducible three-dimensional paths to human experimenters who offered fruit. The humans exchanged reward locations every 5 min while keeping their hands on fixed platforms. Wireless recording retained the bats' flights between sites without an external recording tether.",
        "Repeated paths let neural activity be compared during similar movement toward different experimenters. That control removes one source of behavioral variability while the bats still choose their own flights. The flights were self-initiated, so each bat chose when to travel between sites.",
    ],
    36: [
        "A shared time reference is needed before a recorded spike can be matched to an external event. Both bats and human experimenters carried tags, and a real-time location system estimated those positions from fixed room anchors, as Snyder and colleagues describe.",
        "An external timing signal kept the position samples, taken at 100 Hz, aligned with the neural data. Repeated trajectories were aligned to landing or take-off, so neuronal discharge could be compared at matching stages of flights toward different reward providers.",
        "A landing-aligned firing change can be distinguished from firing linked to a different location or route when the spatial and temporal measurements are precise enough. Synchronization fixes which measured position corresponds to each recorded spike.",
    ],
    37: [
        "Hippocampal firing was compared by Snyder and colleagues across flights on closely matched paths toward two human experimenters. Exchanging the reward locations decoupled the identity of the reward provider from any one fixed reward site, and stable flight trajectories kept self-motion differences small.",
        "About 48% of the analyzable neurons differed in discharge according to the experimenter at the landing site. A subset of cells showed both spatial selectivity and modulation tied to the experimenter. The effect often appeared at one particular take-off or landing location rather than uniformly across every site.",
        "The result supports a **neural representation** that combines the animal's position with features associated with an external individual. Hippocampal responses therefore carry information about another individual in addition to the animal's own location.",
    ],
    38: [
        "An experimenter-related response could arise indirectly from changes in the animal's movement, its reward or a nearby animal. Analyses were confined to comparable trajectories, and flights with another member of the same species at take-off or landing were removed.",
        "Experimenter-dependent firing persisted in more than 40% of the analyzable units after that exclusion. In separate trials, a resting bat stayed at a stable position while humans repeated fixed paths, and about 20% of analyzable units carried information about human position.",
        "These comparisons argue against explanations based solely on the bat's own movement or on a nearby bat. They keep the external participant's influence in the measurement, and they tie that influence to observed **neural coding** under controlled behavioral comparisons.",
    ],
    39: [
        "A **neural ensemble** is a group of neurons whose joint activity can carry information. Wireless Neuropixels recordings from the dorsal hippocampus were made by Forli and colleagues in freely flying Egyptian fruit bats that foraged for rewards at their own pace.",
        "The system recorded single-unit activity together with local field potentials, which reflect nearby population currents. Flights alternated spontaneously with rest. Of the flight-active neurons, about 71% satisfied the study's test for spatial selectivity along the sampled routes.",
        "Population recording reveals activity sequences that one electrode or one cell would miss. Freely chosen flights combined with repeated routes keep natural variability while still allowing consistent measurement. Sequences can be compared across repeated flights.",
    ],
    40: [
        "**Replay** means that an ordered neuronal sequence tied to an earlier path is reactivated. Forli and colleagues compared hippocampal **place-cell** activity during flight with brief population events that occurred while the bats rested. Place cells are neurons whose discharge depends on position. Their firing marks where the animal is along a route.",
        "Detected replay events had a median duration near 358 ms and could preserve either the forward or the reverse order of flight-related activity. They coincided with sharp-wave ripples, brief coordinated field-potential events, and often represented paths remote from the bat's current resting location. Each event reflects an organized sequence.",
        "Sequence comparisons and position decoding show structured reactivation rather than indiscriminate population firing. Because the reactivated paths can lie far from the resting spot, the rest-time events carry route information about places other than where the bat currently sits.",
    ],
    41: [
        "Forli and colleagues tracked how hippocampal population representations shifted during ongoing flight. The recordings contained no sustained locomotor theta oscillations, the rhythmic field-potential pattern classically linked to rodent spatial processing.",
        "Accelerometers, by contrast, picked up a prominent wing-beat rhythm near 8 Hz. Many place cells fired preferentially at particular wing-beat phases, and the decoded position swept ahead of the animal's current position in a cyclical manner. These representational sweeps occurred even though the measured field potential lacked continuous theta.",
        "This **coupling** links a species-specific motor rhythm, the wing beat, to the timing of population coding in the hippocampus. The observation therefore connects the animal's own movement to the structure of its spatial representation during flight.",
    ],
    42: [
        "For mice, Montgomery and colleagues designed light-delivery implants that sit fully inside the body. A **micro-LED** is a miniature light-emitting diode that converts electrical power into light near the targeted tissue. A receiving coil and local electronics drew power from an external radio-frequency apparatus.",
        "The lightest implant weighed roughly 20 mg and filled about 10 mm³. An aluminum resonant cavity operating near 1.5 GHz concentrated electromagnetic energy in the mouse, powering a blue LED with no external fiber or battery attached to the animal.",
        "Miniaturization allowed implantation beneath the skin and access to central or peripheral targets. The radio-frequency geometry was optimized for mice in the tested arena, so the power transfer was matched to that body size and that setup. The implant then needs no external fiber to deliver light.",
    ],
    43: [
        "A wireless implant must deliver enough light while keeping unwanted heating low. Montgomery and colleagues calibrated the LED's emitted power, pulse fidelity and position-dependent power delivery, using controlled electrical tests and measurements in a mouse-sized saline preparation.",
        "Pulses as brief as 100 µs were produced by the device. At a fixed cavity input, the estimated light power density across the tested surface ranged from about 9.2 to 25.8 mW/mm². With 20 mW/mm² illumination, brain-adjacent tissue warmed by less than 1 °C at duty cycles up to 20%.",
        "**Duty cycle** measures the share of time during which stimulation is switched on. Higher duty cycles increased heating, with rises above 1 °C near the 40% condition tested. Calibration therefore sets both the light dose and the thermal load for a given implant design. Stimulation settings thus trade light dose against heating.",
    ],
    44: [
        "Montgomery and colleagues implanted a wireless LED near the right premotor cortex, a cortical region that takes part in movement control. ChR2-expressing mice and implanted wild-type controls were tested in the same powered arena while video quantified their movement.",
        "During 20 s stimulation epochs, 5 ms pulses at 20 Hz increased circling from about 0.40 to 2.5 turns per minute in the ChR2 group. Mean normalized locomotor speed rose by about 40%. Wild-type controls showed none of the light-dependent movement changes.",
        "The genotype comparison links wireless stimulation to an **opsin-dependent behavioral effect**. Persistent circling after stimulation shows that the activated population can drive a turning behavior when light is delivered through an untethered implant.",
    ],
    45: [
        "A causal neural test links a specified intervention to a specified behavioral effect, and it controls for competing explanations. Montgomery and colleagues placed wireless LEDs near paw sensory endings that express ChR2 in nociceptors, neurons that detect potentially damaging stimulation.",
        "With 10 ms pulses at 10 Hz, mice spent less time in the powered compartment during a 30 min stimulation period. Controls with the fluorescent tag alone showed no such reduction. In a complementary necessity test, Antinucci and colleagues reduced hunting after pretectal ablation, while swimming, visual escape and optomotor responses were preserved.",
        "Activation produces an opsin-dependent aversive consequence under these conditions, and selective ablation shows a contribution to normal hunting. A behavioral claim is strongest when perturbation efficacy, anatomical targeting and preserved comparison behaviors are confirmed together.",
    ],
}
