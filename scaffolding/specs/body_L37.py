"""Body-text rewrites for Lecture 37 (scaffolding/RULES.md). Figures, captions and videos are untouched."""

body = {
    2: [
        "A **place cell** is a hippocampal neuron whose activity depends on the animal's location. O'Keefe and Dostrovsky recorded hippocampal units while rats moved on a 24 × 36 cm platform, testing whether neural firing could supply a spatial reference for behavior.",
        "The clearest CA1 example also required a particular facing direction and a restraining tactile stimulus. Location was therefore one part of a combined response that included orientation and touch, and each element had to be present for the unit to fire strongly.",
        "The proposed **cognitive map** interpreted these responses as an internal representation of spatial relationships. The recordings established spatial coding in the hippocampus, which made a spatial reference for behavior a plausible function of the cells.",
    ],
    3: [
        "An **extracellular recording** measures voltage changes outside neurons when they fire action potentials. A lightweight skull-mounted microdrive let electrodes advance through the dorsal hippocampus while the recovered rat walked, groomed, ate or remained still, so the spikes were recorded during natural behavior.",
        "Adjacent recording and reference electrodes fed a differential amplifier, which reduced shared muscle and movement artifacts. Because the recovered animal was not anesthetized, the preparation kept the behavior that anesthesia would remove, while the recording apparatus stayed attached to the animal.",
        "The authors also tested sounds, moving visual stimuli, odors and touch. These tests separated spatially dependent responses from simple sensory responsiveness, so a unit's spatial tuning could be identified apart from its response to any single stimulus.",
    ],
    4: [
        "The recorded CA1 unit fired when the rat was restrained at positions A and B. A hand over the back supplied the tactile stimulus while the experimenter moved the animal around the platform and repeated the same manipulation at other positions, so position and touch were varied together.",
        "At position D, the same restraint produced a much weaker response than at A. At A, remaining still without restraint also failed to produce firing. Both the spatial configuration and the tactile input were therefore needed to evoke the strong response under these conditions.",
        "A **conjunctive response** depends on a combination of variables. This cell's response was conjunctive, so it combined touch with the animal's position on the platform. Touch alone or position alone was insufficient to drive the strong response.",
    ],
    5: [
        "O'Keefe and Dostrovsky translated the rat to position H while keeping an orientation related to the preferred orientation. The response became much smaller, so the unit's activity depended on more than facing direction.",
        "The procedure compared restraint at multiple positions and orientations, with intervals of immobility before and after restraint. These intervals isolated the sensory manipulation from the animal's movement between testing positions, which kept the sensory test separate from locomotion.",
        "A neuron's **spatial field** is the set of locations associated with elevated firing under specified conditions. In this early experiment, the effective field included position, orientation and touch, so a firing field is defined together with the behavioral conditions used to measure it.",
    ],
    6: [
        "Switching off the lights abolished the response of the featured CA1 unit. The spatially restricted tactile response therefore depended on visual information, even though the immediate stimulus that evoked firing was touch on the animal's back.",
        "The authors moved striped cards past the animal and identified no restricted visual **receptive field** that explained the response. A receptive field is the region of sensory space within which a suitable stimulus alters a neuron's activity, and this response spread across the surrounding view.",
        "The rat rotated between effective orientations, so a fixed retinal image was an unlikely explanation. These observations favored dependence on the surrounding visual configuration, which provided the positional information that drove the unit.",
    ],
    7: [
        "A neighboring hippocampal unit responded to moving visual stimuli when the rat occupied a preferred orientation between G and A. At moderate arousal, stimulation elsewhere evoked no comparable response.",
        "At higher arousal, weak responses became possible outside the preferred orientation, while the preferred response grew stronger. **Arousal** here refers to the animal's behavioral activation state, which changed how readily sensory input produced spikes.",
        "The same sensory stimulus therefore produced different responses depending on spatial configuration and behavioral state. State dependence shapes which stimuli a spatially tuned unit can drive, and the response changes with the animal's activation level.",
    ],
    8: [
        "The investigators rotated the platform to test explanations based on local odors or tactile markings. They also removed prominent sound sources and darkened or occluded parts of the visual environment while monitoring spatially restricted responses.",
        "Removing a single cue often left the orientation preferences intact. More radical changes, including removing the surrounding curtain, disrupted some responses and induced sustained exploration, so a familiar environment behaved like a new one.",
        "The authors proposed that several cues provide interchangeable spatial information. One cue can compensate for another, so the spatial code survives the loss of any single landmark.",
    ],
    9: [
        "O'Keefe and Dostrovsky proposed that activation of spatially selective cells, combined with signals related to movement, could recruit cells representing subsequent orientations. In this model, neural activity anticipates the sensory input associated with movement.",
        "The 1971 recordings established location-dependent responses. Prediction, route selection and explanations of lesion-induced behavioral deficits were theoretical extensions that the authors built on those responses.",
        "A **neural representation** is a reliable relationship between activity and a variable, while a **navigational mechanism** also requires transformations that guide behavior. The initial evidence supplied the first, and circuit manipulations during spatial choice tasks are the means of testing the second.",
    ],
    10: [
        "A **grid cell** fires in multiple spatial fields arranged with approximately regular spacing. Hafting and colleagues recorded neurons in superficial dorsocaudal medial entorhinal cortex while rats explored a circular arena 2 m in diameter.",
        "The larger arena exposed repeated fields that were difficult to recognize in smaller enclosures. Individual cells fired when the rat crossed separated locations distributed across the recording surface, rather than one confined region.",
        "A **firing-rate map** relates activity to position after accounting for time spent at each location. The repeated fields establish a periodic spatial code, and the regular repetition is the property that defines the grid pattern across the arena.",
    ],
    11: [
        "**Histology** identifies tissue structure in thin stained brain sections. The recording location in Hafting and colleagues' example was in layer II of medial entorhinal cortex, near its border with postrhinal cortex.",
        "A **Nissl stain** highlights neuronal cell bodies and reveals cortical layers and regional boundaries. Electrode positions were reconstructed from their tracks and the recorded progression of the microdrive, linking physiological measurements to anatomical location.",
        "This reconstruction identifies an entorhinal recording rather than a hippocampal one. A spatial firing phenotype and an anatomical layer are measurable properties, and together they tie the grid pattern to a defined cortical layer.",
    ],
    12: [
        "Rats spend uneven time at different points in an arena. A **firing rate**, measured in spikes per second or hertz, relates spike counts to the time available for spikes at each location.",
        "Hafting and colleagues compared the animal's trajectory with spike locations and the corresponding rate map. Repeated regions of elevated rate remained after the spatial distribution of occupancy was incorporated into the analysis.",
        "Occupancy correction keeps a frequently visited region from counting as a high-response field. Adequate exploration supplies the samples on which each location's rate depends, and a color-coded rate map shows measured activity across the arena.",
    ],
    13: [
        "**Spatial autocorrelation** compares a rate map with shifted versions of itself. Similarity rises when the displacement aligns one set of firing fields with another, which exposes repetition that a single trajectory may hide.",
        "The central autocorrelation peak represents alignment without displacement. Six nearby peaks surrounded it, with directions separated by about 60°, an arrangement consistent with firing locations at the vertices of an equilateral triangular lattice.",
        "A **temporal autocorrelation** is a different measure: it compares the timing of spikes at different lags. The spatial measure reveals the regularity of the spatial pattern and identifies the lattice geometry, while leaving the circuit that produces the pattern to other experiments.",
    ],
    14: [
        "**Grid spacing** is the distance between neighboring repeated firing locations. Hafting and colleagues estimated spacing from the distances between the central autocorrelation peak and its nearest surrounding peaks.",
        "Across the reported cells, spacing ranged from 39 to 73 cm. Within a cell, similar distances in several directions and an angular separation of about 60° supported a regular triangular pattern across the arena.",
        "Spacing describes the spatial scale of a neuron's code, and cells with different spacing can represent the same room at different scales. The original observations also raised whether those scales vary continuously or fall into discrete functional modules.",
    ],
    15: [
        "Hafting and colleagues recorded cells as animals moved between a large and a smaller circular enclosure and returned to the large enclosure. The repeated triangular organization remained recognizable across the changes in available surface.",
        "The expanded arena contained more activity nodes, while their density remained similar. The pattern was therefore not a small fixed collection of fields stretched to match the enclosing walls.",
        "The result supports a spatially repeated code that extends across recording areas. The authors discussed grids of potentially unlimited extent, and each arena size sets how much of the pattern a recording can sample.",
    ],
    16: [
        "Simultaneously recorded grid cells near the same electrode location had similar spacing and orientation. **Orientation** is the angle of the lattice relative to a reference direction in the recording environment.",
        "Their rate maps contained repeated fields with a common geometry, even when the locations of individual fields differed. A **tetrode**, a bundle of four recording wires, helps separate neurons by comparing spike amplitudes across channels.",
        "Shared metric properties point to coordination among nearby cells. Common input and local interactions are both candidate explanations for the coordinated geometry, and the recordings capture that shared geometry directly.",
    ],
    17: [
        "**Dorsal** and **ventral** describe positions along the anatomical axis used to compare recording sites. In one rat, a site near the dorsal entorhinal border had denser grid spacing than a site 560 µm deeper.",
        "Reported spacing was 39.1–43.0 cm at the dorsal location and 48.1–52.2 cm at the more ventral location. Comparing sites within one animal kept explanations based on differences between animals or environments from driving the result.",
        "The finding links anatomical position to the spatial scale of firing. The recordings sampled different cells at different positions, which revealed an organized relationship across the tissue that holds across the sampled depth.",
    ],
    18: [
        "A **firing field** is a region where a cell's rate exceeds the surrounding background under the tested conditions. Hafting and colleagues measured field size from the central peak of the spatial autocorrelation.",
        "More ventral recording positions were associated with both greater spacing and larger individual fields. Spacing concerns the separation between fields, whereas field size concerns the extent of each field.",
        "Their joint increase produces a coarser spatial pattern, not merely a shift of unchanged fields farther apart. Field size depends on the analysis threshold, so it measures an activity region rather than an anatomical boundary visible in the tissue.",
    ],
    19: [
        "The angle of a grid can differ between recording locations even when nearby cells at each location share similar orientation. Hafting and colleagues defined that angle relative to a camera-based reference direction.",
        "Spacing and field size increased toward ventral locations, but orientation followed no such dorsal-to-ventral pattern. Spatial scale and directional alignment are therefore separate properties of the code.",
        "A change in angle rotates a lattice while leaving the distance between its fields intact. A change in spacing alters the metric scale, and separating these variables keeps a shift in directional reference from being mistaken for a change in spatial resolution.",
    ],
    20: [
        "**Spatial phase** describes where the vertices of a grid lie relative to a reference location. Nearby neurons can share spacing and orientation while placing their elevated firing fields at different positions.",
        "Hafting and colleagues compared simultaneously recorded rate maps and found displaced versions of similar lattices. Superimposing the patterns after a spatial shift brought their vertices into closer alignment.",
        "Different phases let neighboring cells become active at different positions, so together they cover more of the environment than one cell could. Phase here is a spatial displacement, a different measurement from the timing of a spike relative to an oscillation.",
    ],
    21: [
        "**Spatial cross-correlation** compares the rate maps of two different neurons as one map is shifted relative to the other. Peaks indicate displacements that bring their firing patterns into alignment.",
        "For neighboring grid cells, the cross-correlation kept a repeated arrangement but usually placed its nearest peak away from the origin. That offset quantifies a difference in spatial phase despite shared spacing and orientation.",
        "Cells at different recording locations can have different scales and orientations, which produces less sharply aligned cross-correlations. The measure captures the similarity of two spatial codes, and a correlated pattern can arise from common inputs without a direct synapse between the recorded cells.",
    ],
    22: [
        "A grid cell's periodic firing leaves locations where that particular cell is relatively inactive. Neighboring cells with different spatial phases place their fields in other regions while retaining similar metric properties.",
        "The recorded population covered the arena collectively, because field locations differed across cells. The observed phase differences spread across the available range rather than clustering around a single common alignment.",
        "Population coverage supports a code for location built from combinations of active neurons. Because periodic activity repeats, additional scales, starting-position information or other inputs can resolve the ambiguity that repetition creates.",
    ],
    23: [
        "An **external landmark** is an environmental feature that can supply a stable spatial reference. Hafting and colleagues rotated a cue card by 90° and compared the grid before, during and after the manipulation.",
        "Grid orientation changed with the cue, while the periodic organization was retained. Returning the card toward its original position restored the corresponding alignment, which shows that a visible feature controls the grid's directional reference.",
        "The result distinguishes the existence of periodic firing from its alignment to a particular room. The same lattice keeps its geometry while external cues determine how it is oriented in the environment, so vision sets orientation rather than periodicity.",
    ],
    24: [
        "Hafting and colleagues recorded a grid cell during 10 min of light, 10 min of darkness and a return to light. The animal remained in the recording environment throughout these changes.",
        "The grid pattern persisted in darkness, although fields could become somewhat dispersed or displaced. **Self-motion** information comprises signals related to the animal's own movement, which remain available when visual landmarks are absent.",
        "Persistence without vision is consistent with movement-based updating of location. Odors, touch and environmental boundaries remain available in darkness, so the result supports a contribution from self-motion alongside other cues.",
    ],
    25: [
        "**Path integration** updates an estimate of location from movement since a reference position. A spatial code that persists in darkness fits this computation, because movement information can continue to update the estimate.",
        "Hafting and colleagues found no major change in grid spacing during visual deprivation. The preserved metric pattern contrasted with the ability of visible landmarks to change the grid's directional alignment.",
        "The combination distinguishes internally maintained geometry from external calibration. Path integration is a supported explanation of grid function, with movement signals maintaining the metric pattern while landmarks set its alignment.",
    ],
    26: [
        "The animals were tested in a familiar room, a novel room and the familiar room again. Repeated firing fields were already present early in the novel environment, rather than appearing after prolonged experience with that room.",
        "Hafting and colleagues divided the novel-room trial into short blocks. Activity during the first 2 min already related to the spatial pattern measured near the end of the trial, while the pattern became more stable with exposure.",
        "Rapid expression supports transfer of a spatial organizing process across environments. Landmark associations are still forming during the trial, while the available grid geometry is expressed from the start of exposure.",
    ],
    27: [
        "The novel-room rate maps became more consistent during continued exploration. Stability was measured by comparing firing at corresponding locations during earlier portions of a trial and its final portion.",
        "The grid's orientation also differed between the familiar and novel rooms, while repeated familiar-room tests showed much smaller changes. The same spatial organizing principle was therefore expressed with room-specific alignment.",
        "The authors proposed that learning builds associations between landmarks and the grid's phase and orientation. This account explains the gradual stabilization of alignment, and the study measured the changes in spatial activity that such associations would produce.",
    ],
    28: [
        "Giocomo and colleagues tested whether an ion-channel protein, **HCN1**, contributes to spatial scale. They recorded grid cells in mice with forebrain-restricted HCN1 knockout, a deletion that removes functional expression of the gene in the affected tissue.",
        "Littermate controls provided a comparison for the genetic manipulation, and experimenters were unaware of group identity during collection and preliminary analysis. Recordings sampled superficial medial entorhinal cortex while mice explored open fields.",
        "The intervention moved beyond observing a scale gradient to altering a candidate molecular contributor. Because the deletion covered the forebrain rather than the recorded grid cells alone, the effect reflects the circuit in which those cells sit.",
    ],
    29: [
        "**HCN** denotes hyperpolarization-activated cyclic nucleotide-gated channels. These channels conduct the inward cation current called I_h, and they shape membrane responses and the time window over which inputs interact.",
        "Prior cellular evidence showed that reducing HCN1 slows resonance and temporal integration in entorhinal layer II cells. Giocomo and colleagues used that evidence as the rationale for recording spatial activity after forebrain deletion, and temporal integration is the combination of inputs arriving at different times.",
        "The knockout grid maps connect the channel intervention to altered spatial firing. The link between membrane integration and the transformation of movement into spatial position is a mechanistic interpretation supported by the observed changes in scale.",
    ],
    30: [
        "Mice explored a 100 × 100 cm box and, in additional sessions, a 50 × 50 cm box. The larger environment provided enough extent to recognize repeated fields across the sampled dorsal-to-ventral recording range.",
        "The smaller box supported measurements of boundary-related and head-direction activity, but it did not reveal every grid's full periodicity. The principal grid-cell comparison therefore came from recordings in the larger environment.",
        "Arena dimensions determine how much of a spatial pattern can be sampled. A lattice that is missing from a small box can still be present, and this control matters most when a manipulation enlarges spacing and reduces the number of visible fields.",
    ],
    31: [
        "Grid cells remained present after forebrain HCN1 deletion. Their rate maps and spatial autocorrelations kept repeated, approximately hexagonal organization, so HCN1 was not required for every expression of the grid pattern.",
        "Giocomo and colleagues compared the observed spatial patterns with patterns obtained by shifting spike timing relative to the animal's path. This shuffle control keeps the spike sequence while breaking its original association with position.",
        "Preserved periodicity distinguishes the generation of grid-like structure from the regulation of its scale. Other HCN subunits, other intrinsic currents and circuit interactions can all contribute to network activity after HCN1 is removed.",
    ],
    32: [
        "Grid spacing was greater in knockout mice than in controls across the sampled anatomical positions. Giocomo and colleagues plotted spacing against distance from the dorsal border of medial entorhinal cortex.",
        "Comparing cells at similar anatomical levels reduced confusion between a genetic effect and the normal dorsal-to-ventral scale difference. The knockout relationship sat at larger spacing values while still increasing toward ventral positions.",
        "HCN1 expression therefore contributes to the normal range of spatial scale. The measured outcome is a change in the distance between activity fields, which shows that the channel tunes spacing while spatial coding remains intact.",
    ],
    33: [
        "HCN1 knockout enlarged both grid spacing and the size of individual fields. These two measurements distinguish the distance between repeated peaks from the extent of each elevated firing region.",
        "The reported spacing-to-field-size ratios were about 3.26 in controls and 3.32 after knockout. Their similarity supports coordinated expansion of the pattern, rather than selective broadening of fields without a corresponding spacing change.",
        "A proportionately enlarged grid represents a coarser metric pattern. The experiment quantified spatial firing during exploration, a measure that is separate from navigational accuracy or memory.",
    ],
    34: [
        "Giocomo and colleagues presented grid maps together with stained sections that located their recording sites. At similar distances from the dorsal entorhinal border, knockout examples had wider spacing than control examples.",
        "The anatomical reconstruction used sagittal sections and cortical staining patterns to identify medial entorhinal cortex and its layers. **Cytoarchitecture** is the arrangement and appearance of cells used to distinguish tissue regions.",
        "Matching anatomical locations shows that the scale difference is not explained by recording deeper in the knockout group. Histology confirms where the electrodes sampled activity in each genotype.",
    ],
    35: [
        "Within a single knockout animal, grid spacing still increased as recording locations moved away from the dorsal border. Giocomo and colleagues used this within-animal series to test whether HCN1 deletion abolished the anatomical organization of scale.",
        "The persistence of the gradient distinguishes a general expansion of the scale range from the loss of topographic organization. **Topography** is the systematic relationship between anatomical position and a measured functional property.",
        "HCN1 therefore contributes to scale without being the sole determinant of the dorsal-to-ventral relationship. Other cellular properties and circuit mechanisms are possible contributors, and the surviving gradient points toward them.",
    ],
    36: [
        "**Theta modulation** is a recurring change in neuronal firing associated with a low-frequency rhythm. Giocomo and colleagues compared spike-time autocorrelations of grid cells in control and knockout mice.",
        "The typical interval between theta-related peaks was longer after knockout: 108.1 ms in controls and 114.4 ms in knockout grid cells. The enlarged spatial pattern therefore accompanied a slower recurring timescale of firing.",
        "A **temporal autocorrelation** measures how often spikes recur at different time lags, not the physical spacing of fields. The shared shift in timing and spacing constrains the mechanisms that could produce the knockout phenotype.",
    ],
    37: [
        "Movement speed can influence theta-related activity, so Giocomo and colleagues compared groups across speed ranges. At 20–30 cm/s, the reported theta-related spike intervals were 101.4 ms in controls and 112.4 ms after HCN1 knockout.",
        "The difference persisted at comparable speeds, which makes an explanation based on the knockout animals' faster average movement less likely. The speed comparison separated a behavioral covariate from the genetic change in neuronal timing.",
        "The result is consistent with altered coupling between movement and the spatial code. HCN1 shapes neuronal integration, whereas the origin and routing of velocity-related inputs are a separate question for circuit measurements.",
    ],
    38: [
        "A **local field potential** is the extracellular voltage produced by coordinated activity in nearby tissue. Its theta frequency differs from the frequency inferred from repeated spikes of one neuron.",
        "Giocomo and colleagues reported average entorhinal field-theta frequencies of 8.63 Hz in controls and 8.25 Hz after knockout. The increase of field-theta frequency with running speed was also weaker in knockout mice.",
        "These observations connect the channel intervention to population-level timing as well as to grid-cell scale. Individual discharge timing and the surrounding field rhythm are measured separately, so a proposed phase relationship can be tested against both.",
    ],
    39: [
        "An **interneuron** is a neuron whose principal connections remain within a local circuit. Giocomo and colleagues compared theta-modulated entorhinal interneurons with the principal cells that carry the grid-cell spatial pattern.",
        "The knockout-related increase in theta timing was present in grid cells and was not comparably detected in the simultaneously recorded interneuron population. The change therefore concerns grid cells specifically, rather than every recorded neuron.",
        "Cell-class differences constrain how a molecular intervention affects network dynamics. The selective physiological effect points to specific cell classes, which makes a targeted change in those classes the likely explanation.",
    ],
    40: [
        "A **border cell** fires most strongly near one or more environmental boundaries. Giocomo and colleagues recorded boundary-related activity in the same entorhinal region used to study grid cells.",
        "The maps concentrated activity along walls rather than at the repeated interior locations characteristic of a grid. Border-related firing remained identifiable after HCN1 deletion, providing a clear contrast with the enlarged grid pattern.",
        "A boundary code supplies information different from grid spacing, because it relates activity to environmental edges. Its persistence shows that the knockout left other forms of spatial tuning in place.",
    ],
    41: [
        "A **head-direction cell** fires preferentially when the animal's head points toward a particular direction. Giocomo and colleagues used two tracking lights to estimate heading and compared firing across angles.",
        "Directional tuning was present in control and knockout mice. A directional response is distinct from a grid field: an animal can face the preferred direction at several locations, whereas a grid cell's rate is organized by repeated spatial positions.",
        "The continued directional signal shows that heading information persists after the knockout. Heading and speed are the inputs that a grid network transforms into location, so measuring them in these circuits connects the directional signal to the grid pattern.",
    ],
    42: [
        "**Spatial stability** describes the consistency of a neuron's firing pattern across repeated portions of a recording. Giocomo and colleagues compared maps from the first and second halves of each trial.",
        "Grid and border patterns were more stable in knockout mice, while directional stability changed much less. The analysis also considered grid spacing, because broader patterns can appear more stable than narrower patterns under the same displacement.",
        "Greater consistency of activity is distinct from greater spatial precision. A broader field can remain stable while distinguishing positions less sharply, so the stability difference describes the consistency of firing rather than navigational precision.",
    ],
    43: [
        "An **oscillatory interference model** proposes that relationships between oscillations contribute to spatially periodic firing. Giocomo and colleagues examined their knockout results against proposed links between intrinsic timing and grid scale.",
        "HCN1 deletion enlarged spacing but preserved the dorsal-to-ventral gradient. The authors contrasted that result with earlier cellular observations that HCN1 deletion strongly alters the anatomical gradient of resonance.",
        "The mismatch challenges explanations in which the HCN1-dependent resonance gradient alone determines the scale gradient. Different versions of the model make different predictions, and the forebrain intervention leaves other intrinsic currents and network interactions free to shape activity.",
    ],
    44: [
        "The three studies establish different levels of evidence: spatially dependent hippocampal responses, periodic entorhinal firing, and a genetic contribution to the spatial scale of that periodic activity. Each level answers a different question about the spatial code.",
        "HCN1 knockout perturbs a candidate cellular mechanism, while grid recordings in darkness and under landmark rotation test conditions affecting an intact spatial code. Each manipulation constrains a different explanation of the measured firing.",
        "A causal account of navigation additionally requires linking the altered representation to behavior under a defined spatial demand, with controls for movement, sensory information and the broader effects of the intervention. Those tests would connect the neural code to behavior.",
    ],
    45: [
        "**Gain** describes how strongly a system's output changes in response to its input. Giocomo and colleagues proposed that HCN1-dependent integration contributes to the gain linking movement signals with changes in the spatial firing pattern.",
        "After HCN1 deletion, wider field spacing accompanied weaker modulation of theta frequency by running speed. These outcomes fit an altered movement-to-space relationship, while the preserved anatomical scale gradient points to additional determinants.",
        "The study recorded spatial firing alongside speed-dependent theta timing, and gain regulation is the proposed explanation connecting the molecular intervention to these measurements. It links the channel to spatial activity through a transformation of velocity signals.",
    ],
}
