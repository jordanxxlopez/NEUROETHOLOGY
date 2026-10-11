"""Lecture 29 body-text rewrites (scaffolding/RULES.md): three developed paragraphs per content slide."""

body = {
    2: [
        "**Waggle dances** are repeated movements on the vertical comb that tell nestmates where a food source lies. Each dance contains a straight abdominal-wagging run and alternating return loops. A **vector** specifies a direction and a distance from an origin, and for a forager's dance that origin is the hive.",
        "Dong and colleagues recorded marked foragers that visited a feeder 150 m from the hive. On the vertical comb, the angle of the waggle run encoded the food's direction relative to the sun, and the run's duration encoded its distance. Followers stayed close to the dancer and attended to every run.",
        "The signal describes a place outside the hive rather than the dancer's immediate position. Video recordings measure the spatial and temporal structure of the message. Successful communication also requires that followers pick up the signal and then choose an appropriate flight.",
    ],
    3: [
        "A dancer on a vertical comb treats upward as the sun's direction. The waggle-run angle measured from vertical stands for the resource's direction relative to the sun outside, so **gravity** substitutes for the sun in a dark hive. The message carries a direction even where no sunlight reaches the dancer.",
        "Dong and colleagues recorded dance angles on the crowded, uneven comb surface. Repeated waggle runs spread around a mean angle, so the team measured that **divergence** rather than assuming each run conveyed an identical angle. Bees without experienced dancers produced the largest spread in their first dances.",
        "Encoding direction involves a reference system and motor precision in executing the angle. A follower must convert the comb-relative angle into a flight direction using celestial information. The dancer's output supplies the first half of that conversion, which is why the recordings measure precision as well as direction.",
    ],
    4: [
        "Von Frisch and Lindauer trained marked foragers to a feeder 180 m away, in a direction 30° north of west from the hive. The bees learned this route during the afternoon. The team then moved the hive into an unfamiliar landscape to test the learned bearing.",
        "The following morning, equally familiar scented food dishes were offered in four directions in the new landscape. Arriving bees were captured at once, so successful visitors could not return and recruit nestmates. Searches favored the trained **compass direction** despite the changed surroundings.",
        "The result points to compensation for the sun's movement between afternoon training and morning flight. In related tests, cloudy skies prevented correct orientation when neither direct sunlight nor polarized skylight was available. Landmarks and celestial cues can compete with each other during orientation.",
    ],
    5: [
        "Riley and colleagues tracked bees that had followed dances advertising an unscented feeder 200 m east of the hive. A harmonic radar detects a small transponder carried by each bee, so the trajectory can be recorded outside the observation hive. Positions were sampled every 3 s.",
        "Recruits released at the hive generally flew an initially straight eastward route. Their straight sections averaged 206 m before searching began. Radar positions allowed **directed travel** to be told apart from more tortuous search behavior.",
        "The recruits had never visited the advertised feeder, and the unscented food and wind direction reduced direct odor guidance from the destination. The flight therefore reflects a **flight vector** acquired from the dance. Radar records the flight itself, while the sensory cues a follower used during the dance remain unmeasured.",
    ],
    6: [
        "Riley and colleagues captured dance followers at the hive and released them 200–250 m southwest of it. This manipulation kept the dance's instruction unchanged while moving the starting point. From the release site, the feeder lay in a new direction and at a new distance.",
        "Rather than redirecting toward the feeder from the release point, displaced bees began with an eastward straight flight that averaged 188 m before search. The **flight instruction** kept its direction and approximate distance after displacement, which shows that the decoded movement is separate from a world location.",
        "A vector from one origin therefore leads to a different endpoint when executed elsewhere. Familiar landmarks can guide later search, particularly in landscapes rich in recognizable features. Those landmarks become useful after the initial vector flight has already been flown.",
    ],
    7: [
        "Hive-released recruits ended their straight flights near the advertised feeder on average, although individual endpoints differed by tens of meters. Riley and colleagues then tracked **looping searches**, some lasting up to 20 min and reaching 200 m from the feeding site.",
        "Two of the tracked recruits found the unscented feeder. An average endpoint near the food location therefore fails to predict arrival by every bee. Directional variation rose near the end of the vector flight as directed travel gave way to search.",
        "Dance information supplies an approximate search area. Local visual or odor cues can be needed to pin down the final destination. Spatial scatter and terminal failure set successful long-range information transfer apart from precise source recognition.",
    ],
    8: [
        "Riley and colleagues measured flight tracks together with wind velocity, which distinguishes movement over the ground from movement through the air. A bee in a crosswind must angle its body partly into the wind to hold the advertised **ground track**.",
        "In one recorded flight, ground speed was 6.8 m/s while a 3.3 m/s wind blew from another direction. The reconstructed air velocity was 5.2 m/s. The bee's air heading diverged from its ground-track direction by about 28°, counteracting the wind drift.",
        "The displacement followed the eastward instruction instead of the uncorrected, wind-driven heading, which shows **active compensation** during recruitment flight. The wind and radar data document the correction in this flight, while the visual feedback behind it was beyond these measurements.",
    ],
    9: [
        "**Optic flow** is the movement of environmental images across the retina during self-motion. Nearby surfaces produce larger angular image displacement than distant surfaces for the same travel. A narrow textured tunnel therefore boosts optic flow without requiring a long physical flight.",
        "Srinivasan and colleagues trained honeybees through a tunnel 6.4 m long, 11 cm wide and 20 cm high. Random black-and-white texture covered the walls and floor, a mesh ceiling let the bees see the sky, and the feeder sat 6 m into the tunnel.",
        "Returning bees produced waggle dances after this brief passage, although a similar outdoor journey normally elicits round dances. The preparation distinguishes physical distance from the visual motion experienced en route. It supports a **visual odometer**, a mechanism that estimates distance traveled, over an energy-based distance measure.",
    ],
    10: [
        "Srinivasan and colleagues kept the feeder at the same physical location and replaced the random texture with stripes parallel to flight. Axial stripes change little along the flight axis, so they generate much less visual motion during forward travel.",
        "A 35 m outdoor journey followed by 6 m through random texture produced waggle dances in 90% of recorded dances. With axial stripes over the same total of 41 m, 86.7% of dances were round dances. Outdoors, a feeder at 35 m elicited mostly round dances.",
        "The two 41 m preparations share the same physical journey length, which therefore fails to account for the difference. The texture control identifies **optic flow** as the relevant variable under these conditions. Visual pattern, not the distance walked, sets how far the dance reports.",
    ],
    11: [
        "Srinivasan and colleagues moved outdoor feeders between 60 and 350 m and timed each waggle phase on the bee's return to the hive. Over this range, mean **waggle duration** rose roughly linearly with feeder distance.",
        "The calibration increased by 1.88 ms of waggle duration per meter of outdoor travel. It served as a reference for interpreting the unusually long dances produced after textured-tunnel flights. The calibration was obtained independently of the tunnel manipulation.",
        "A calibration links a measured signal to a known quantity under specified conditions. Its value holds for the tested routes and distances, and it is a relation rather than a universal conversion for every landscape or colony.",
    ],
    12: [
        "Srinivasan and colleagues applied the outdoor calibration to dances that followed textured-tunnel passages. A 41 m journey with 6 m inside the tunnel produced a mean waggle duration of 528.8 ms, which corresponds to about 230 m outdoors.",
        "A second arrangement placed the tunnel nearer the hive, producing 12 m of total travel. Its mean duration was 441.2 ms, corresponding to about 184 m outdoors. Both preparations generated a disproportionately large **distance signal** despite their different outdoor approach lengths.",
        "Close textured surfaces amplified the visually measured journey. Waggle duration therefore reflects visual surroundings as well as physical meters. These outdoor distances are values read from the authors' calibration rather than records of what a bee experiences.",
    ],
    13: [
        "Esch and colleagues trained dancers to fly 3 m outdoors and then 8 m through a textured tunnel toward the south. The actual feeder lay 11 m from the hive, yet returning bees produced waggle runs averaging 358 ms.",
        "The local outdoor calibration linked that duration to about 72 m. Newly recruited bees searched mostly at a **control station** 70 m south of the hive instead of at the tunnel feeder. The stations offered neither food reward nor added scent.",
        "For the first 30 min, the closed tunnel kept dancers from advertising the tunnel journey, and no recruits arrived at the stations. Opening the tunnel started dancing and recruitment. The visually inflated distance signal therefore drives **followers' search**, not just the dancer's movements.",
    ],
    14: [
        "Esch and colleagues measured outdoor dance durations separately for southern and northwestern routes. A given waggle duration corresponded to different physical distances on the two routes, even though both involved ordinary outdoor flight.",
        "For example, 270 ms corresponded to about 52 m with the southern relation but about 157 m with the northwestern relation. The northwestern landscape produced less distance signal per physical meter. A single route-independent conversion would therefore misread the dance.",
        "The relevant quantity is the **accumulated visual motion** shaped by the route. Terrain and viewing geometry change how optic flow relates to physical distance, so a conversion has to reflect the route being flown.",
    ],
    15: [
        "Esch and colleagues repeated the tunnel recruitment test with a northwestern approach, flying 3 m outdoors and then 6 m through the tunnel. The actual feeder lay 9 m from the hive, and returning dancers produced waggle runs averaging 270 ms.",
        "Recruit searches peaked near 140 m along the northwestern route. The northwestern calibration predicted about 157 m, while the southern calibration would have predicted about 52 m. Recruits searched where a **route-appropriate visual distance** placed the destination.",
        "Unrewarded stations and a tunnel closed before each trial prevented the relevant dances and recruitment. The result links dance decoding with followers' own visual navigation. The duration-to-distance conversion is set by the visual conditions the navigating bees encounter.",
    ],
    16: [
        "Tautz and colleagues moved feeders along two routes, each 580 m long. One route crossed land, then water, then an island, and the other stayed over land. Marked foragers were trained to follow the moving food source, including a feeder carried by boat.",
        "At each position, returning dances were filmed and their **waggle-run durations** measured. The experiment tested whether the tunnel-defined visual odometer also depends on natural terrain. Both routes increased physical distance without the artificial closeness of tunnel walls.",
        "Water-crossing bees kept signaling increasing distance, but the rate of increase varied across route segments. Recruits were scarce while the feeder was over water and reappeared on the island. Recruitment success and distance encoding are related yet distinct outcomes, and habitat change can affect both.",
    ],
    17: [
        "On the land–water–island route, Tautz and colleagues measured waggle-duration increases of 1.970 ms/m over the first land segment, 0.546 ms/m over water and 2.243 ms/m over the island. Equal physical travel therefore added unequal amounts to the dance signal.",
        "Segment-specific relations tracked the change more closely than one constant slope across the whole route. An all-land comparison route lacked the water-associated flattening, which identifies a specific **terrain transition** rather than a general dependence on feeder distance.",
        "A visual odometer can keep working over water while accumulating less effective image motion there. These behavioral measurements constrain how the distance signal depends on its input, with low **image contrast** offering one explanation for the water effect.",
    ],
    18: [
        "**Visual contrast** measures the difference in image intensity that makes spatial structure detectable. Tautz and colleagues photographed land and water scenes along the experimental routes and analyzed intensity variation within defined image windows.",
        "Mean contrast was greater over land than over water. The low-contrast water segment coincided with slower accumulation of waggle duration, while the terrestrial segments supported larger increases. The original photographs keep the investigators' measurement windows.",
        "Contrast offers a plausible link between natural image structure and effective optic flow. Controlled tunnel-texture experiments manipulate visual motion directly, while field measurements show the dependence under ordinary foraging conditions.",
    ],
    19: [
        "Polarized light has a preferred orientation of its electric-field oscillation, called the **e-vector**. Sakura and colleagues tested whether restrained honeybees could discriminate two e-vector directions presented from above, without requiring a navigational journey.",
        "One direction was paired with sucrose, while the perpendicular direction went unrewarded. The **proboscis extension response**, the extension of the feeding mouthparts, served as a behavioral readout of association. Responses increased to the rewarded direction during ultraviolet conditioning and stayed low to the other.",
        "The test shows learned discrimination of polarization orientation, independent of free-flight steering. Head-fixed bees also learned, which points to detection without repeated active head scanning. The step from this sensory discrimination to the direction advertised in a dance lies beyond the test.",
    ],
    20: [
        "Sakura and colleagues repeated polarization conditioning with ultraviolet light near 350 nm, blue light near 442 nm and green light near 546 nm. Each preparation used a rewarded e-vector and a perpendicular unrewarded e-vector.",
        "Bees acquired the discrimination under ultraviolet stimulation but failed to acquire it under the blue or green conditions. The wavelength comparison held the **associative task** constant while changing the spectral input. Responsiveness to sucrose was assessed in a separate control.",
        "The learning therefore depends on ultraviolet input, so the task is not solved at every wavelength. The result fits **ultraviolet-sensitive polarization input** as the channel that carries the e-vector information used in learning.",
    ],
    21: [
        "The dorsal rim area is a specialized region near the upper edge of the compound eye, associated with skylight polarization detection. Sakura and colleagues painted either this region or the rest of the eye before ultraviolet polarization conditioning.",
        "Bees with the dorsal rim covered failed to learn the rewarded e-vector. Bees with the extradorsal region covered kept their discrimination even with much of the eye occluded. This complementary control ties the behavioral effect to the specialized region rather than to reduced exposed area.",
        "The result supports a necessary **dorsal-rim contribution** under these conditions. Zeller and colleagues traced input from this region into a specialized dorsal-medulla compartment, so the occlusion and tracing results converge on one sensory pathway.",
    ],
    22: [
        "Kraft and colleagues trained bees in a four-tunnel maze with one entrance and three possible exits. Each tunnel measured 125 cm long, 11 cm wide and 18 cm high. Polarizing filters above the tunnels set the illumination parallel or perpendicular to the flight axis.",
        "The rewarded exit carried the same relative polarization orientation as the entrance, while incorrect exits offered no reward. During tests, choices were recorded without reward. A diffuser blocked direct sight of the sun and obscured overhead landmarks.",
        "The design asks whether a bee can associate a route with a fixed relationship between its body axis and the **e-vector**. Moving the illumination among exits then tests polarization against a learned preference for turning or going straight.",
    ],
    23: [
        "In Kraft and colleagues' straight-ahead training condition, bees chose the rewarded tunnel on 67% of tests with the original illumination. Moving the rewarded polarization to the left exit raised left choices from 15% to 28%, while straight-ahead choices held at 51%.",
        "In the right-turn training condition, bees chose the rewarded right exit on 74% of tests. After its polarization moved to the straight-ahead exit, straight-ahead choices reached 56%. A random choice among three exits would yield about 33%.",
        "The cue relocation changed behavior, yet its effect varied with training. **Polarization** and **motor-route memory** can both shape choice. The results show learned use of relative e-vector information, which contributes to route decisions alongside turning habits.",
    ],
    24: [
        "Evangelista and colleagues trained bees through a 12 m textured tunnel covered by ultraviolet-transmitting polarizers and a diffuser. The diffuser removed direct sight of the sun and overhead landmarks, so the artificial polarization pattern served as the celestial cue.",
        "With transverse polarization, waggle runs clustered along a vertical axis on the comb. With axial polarization, they clustered along a horizontal axis. The mean axes were about 91.7° and 1.3° relative to horizontal, respectively.",
        "A single e-vector has a **180° ambiguity**, so the same axis represents opposite travel directions. Bees advertised both alternatives instead of a unique direction. The experiment links polarized flight input to the communicated direction, while showing that an axis of possible headings differs from a fully sun-referenced bearing.",
    ],
    25: [
        "Evangelista and colleagues also changed the polarization axis halfway along the tunnel. The first 6 m and the second 6 m carried perpendicular e-vector orientations, although the tunnel itself stayed straight.",
        "After the two-segment journey, bees advertised diagonal directions consistent with interpreting a turn between the segments. Their mean waggle duration was shorter than after a tunnel with one uniform polarization axis. The authors linked this reduced **distance signal** to an inferred two-leg displacement.",
        "The intervention alters the sensory compass instruction without inserting an actual corner. It supports combining directional input with a distance estimate when the dance is generated. The inferred trajectory relies on ambiguity in the artificial sky cue, and the neural accumulation of vector information remains unmeasured.",
    ],
    26: [
        "**Solar azimuth** is the sun's horizontal bearing, and an ephemeris describes how that position changes over the day. Dyer and Dickinson reared bees in an incubator and restricted their outdoor flights to late afternoon.",
        "On a cloudy test day, these bees flew for the first time during morning and early afternoon. Their dances indicated a morning solar estimate about 180° from the evening azimuth they had experienced. Around local noon, they switched toward the familiar evening direction.",
        "The bees supplied an approximate morning reference without having directly experienced that part of the sun's course. The step-like pattern reflects a general expectation of daily solar movement, refined by experience. It differs from exact memorization of every hourly sun position.",
    ],
    27: [
        "Dyer and Dickinson compared experience-restricted bees with bees that had flown throughout the day earlier. Both groups were tested under cloudy skies, when direct sight of the sun was unavailable, so current visual access to the sun could not explain their different dance orientations.",
        "Fully experienced bees' solar estimates followed the continuously changing local sun course closely. Bees with afternoon-only experience instead used the coarse morning-afternoon pattern. The contrast shows a broad expectation about solar movement refined into a precise **local calibration**.",
        "The sun's horizontal bearing changes at a variable rate with time, latitude and season, so a universal constant angular-rate correction is inadequate. Experience improves the **temporal reference** used for navigation, which makes the calibration learned rather than fixed.",
    ],
    28: [
        "A **circadian clock** is an internal timing system with an approximately daily cycle. Cheeseman and colleagues used 2% isoflurane anesthesia to perturb this timing system and then tested sun-compass homing.",
        "In the Southern Hemisphere, bees trained to a feeder 100 m from the hive were transported 6 km into unfamiliar terrain. Six hours of anesthesia shifted the vanishing bearing about 87° anticlockwise relative to a 30 min anesthetic control. A vanishing bearing is the direction in which a departing bee leaves the observer's view.",
        "A time error predicts a directional error, because solar bearing depends on the time of day. The shifted orientation supports this relationship, although extended anesthesia can also affect general performance. A short-anesthetic control and independent clock measurements help tell a timing disturbance apart from nonspecific drug effects.",
    ],
    29: [
        "Cheeseman and colleagues repeated the navigation test in the Northern Hemisphere using harmonic radar. Bees trained to a feeder 300 m from the hive were displaced 500 m before release, allowing the initial homeward vector flight to be distinguished from later correction.",
        "Six hours of anesthesia shifted the initial vector about 58° clockwise relative to the 30 min control. Unanesthetized catch-and-release bees provided another handling comparison. The **error direction** ran opposite to the Southern Hemisphere result, as expected from the different solar course.",
        "The hemisphere pattern ties the behavioral error to **sun-compass timing** instead of a fixed tendency to turn left or right after treatment. Individual variation and possible secondary cues exist. The trajectory shows an altered initial compass instruction, while its neural basis lies outside these tracks.",
    ],
    30: [
        "Cheeseman and colleagues measured hive activity under constant dim light, which removes ordinary day-night transitions as the immediate cause of a shifted rhythm. Six hours of daytime anesthesia delayed daily activity and altered rhythmic gene expression in the sampled bee brains.",
        "The reported phase delays were 4.9 h for mammalian-type cryptochrome **messenger RNA** and 4.3 h for period messenger RNA. Messenger RNA is the transcript used to produce a gene's protein. The sampled hive's activity phase shifted by 5.3 h, while clock gene expression stayed broadly constant.",
        "Six hours of anesthesia during subjective night produced no comparable delay. This time-dependent effect points to disturbance of the circadian oscillator rather than a literal six-hour pause in all behavior. Whole-brain expression averages over many cells, which hides the cells that deliver time information to a compass pathway.",
    ],
    31: [
        "Zeller and colleagues injected fluorescent tracers into the dorsal rim of the honeybee eye and labeled the surrounding **neuropil**. Neuropil is tissue containing interwoven neuronal branches and synapses. The medulla is a visual-processing region within the optic lobe.",
        "Dorsal-rim input reached a distinct dorsal-medulla compartment called the **MEDRA**. Complementary injections into other pathway regions and synapsin labeling set this compartment apart from neighboring medulla. The published micrographs keep anatomical orientation and micrometer scale bars.",
        "This tracing identifies an entry pathway for polarization-associated visual input. Anatomical localization measures connectivity, whereas Sakura's regional-occlusion experiment addresses a different link between sensory specialization and behavior.",
    ],
    32: [
        "Zeller and colleagues traced **transmedulla neurons**, cells whose branches cross the medulla from the dorsal-rim-associated input compartment toward more medial brain regions. Dye injections at different sites gave complementary views of their branching pattern.",
        "These neurons arborized in the MEDRA and extended through a defined medulla layer. Their medial projections reached the lower unit complex of the anterior optic tubercle, a visual-processing center outside the optic lobe. Fine terminal morphology distinguished the plausible input and output parts of the pathway.",
        "The ordered projection offers an anatomical route from specialized eye input toward central compass circuitry. Morphology supports this direction of information flow, while transmission is measured through physiology. The **direction of flow** is therefore set by the arrangement of branches.",
    ],
    33: [
        "**Pigment-dispersing factor**, or PDF, is a neuropeptide associated with circadian signaling in insects. Zeller and colleagues combined PDF immunostaining with tracer labeling of transmedulla neurons to locate where potential timing input could meet the honeybee sky-compass pathway.",
        "PDF-positive fibers occupied the same medulla layer as parts of the traced neurons. At higher magnification, labeled puncta lay in close proximity along their passage through the medulla. The two labels did not colocalize, and PDF labeling was absent from within the MEDRA itself.",
        "The result identifies neighboring neuronal populations and a candidate site for modulation. Close proximity marks a candidate contact region, and circadian compass correction is the proposed role of that contact.",
    ],
    34: [
        "Zeller and colleagues combined transmedulla tracer labeling with antibodies against **serotonin**, a monoamine signaling molecule, and **GABA**, gamma-aminobutyric acid. GABA commonly contributes inhibitory signaling, and its action at a given connection depends on receptor and physiological evidence.",
        "Serotonin-positive puncta overlapped the dorsal portion of the relevant medulla layer but not the MEDRA. GABA-positive fibers lay near transmedulla branches throughout their length, including within the MEDRA. In both preparations, tracer and transmitter labels marked different populations rather than the same cells.",
        "These spatial relationships suggest candidate modulatory and local processing interactions. Each one points to a possible role, and the receptor identity and synaptic direction determine its functional meaning.",
    ],
    35: [
        "Held and colleagues traced the honeybee sky-compass network using dye injections, neuropil labeling and single-cell preparations. **TuLAL1 neurons** project from the anterior optic tubercle toward paired synaptic regions called the lateral and medial bulbs.",
        "A second class, **TL neurons**, connects these bulbs with the lower division of the central body, part of the central complex. The labeled branches establish two parallel anatomical routes from tubercle outputs toward central-brain circuitry associated with directional processing.",
        "The bulbs form a defined interface rather than an undifferentiated relay. The labeled projections describe anatomy, and physiological recordings would be the route to a honeybee heading code.",
    ],
    36: [
        "A **microglomerulus** is a compact synaptic complex in which a large presynaptic terminal contacts several smaller postsynaptic processes. Held and colleagues stained honeybee bulb tissue for synapsin, associated with presynaptic machinery, and for filamentous actin, prominent in postsynaptic regions.",
        "Confocal images revealed separated microglomerular complexes in the lateral and medial bulbs. Traced TuLAL1 terminals occupied the presynaptic cores, and postsynaptic processes from TL neurons contacted them. Complementary labeling linked each cell's projection to the local terminal organization.",
        "These stains describe an anatomical arrangement for distributing tubercle signals among downstream neurons. Confocal images alone leave finer membrane contacts unseen, so the authors added electron microscopy to the analysis.",
    ],
    37: [
        "Held and colleagues used transmission electron microscopy to examine honeybee bulb complexes at **membrane resolution**. Large TuLAL1 terminals contained vesicles and multiple presynaptic specializations facing smaller profiles. Vesicles are membrane-bound structures that store releasable signaling molecules.",
        "The authors identified **dyadic and tetradic contacts**, in which one presynaptic specialization faced two or four postsynaptic profiles. GABA immunostaining associated downstream TL neurons with an inhibitory transmitter phenotype. These observations constrain connectivity more directly than light-microscopy overlap.",
        "Synaptic morphology establishes physical contacts, and transmitter staining points to a candidate sign of downstream signaling. Receptor identity and activity-dependent effects complete the picture for the navigation computation.",
    ],
    38: [
        "Greggers and colleagues recorded electric fields around dancing bees and measured antennal movements during controlled electrical stimulation. Charged bodies exert forces on nearby charged structures, so a force can move an antenna without any dedicated electric-field receptor.",
        "An isolated wing oscillating at 40 Hz, 2 mm from the head, evoked larger flagellar movements when charge was preserved rather than discharged. Laser Doppler measurements quantified these movements. **Johnston's organ**, a mechanosensory organ in the antennal pedicel, responded to field-induced movement. The flagellum is the distal antennal segment, and the pedicel is its supporting joint region.",
        "The sequence runs from electric force to antennal displacement and then to activation of movement-sensitive sensory neurons. This supports a **mechanical route** for field detection. The mechanotransduction channel that converts movement into receptor current completes the chain.",
    ],
    39: [
        "Greggers and colleagues paired an electric-field stimulus with sucrose and tested the conditioned proboscis extension response. Uncharged material or an inactive stimulus source served as the unrewarded comparison. Bees learned both constant fields and modulated stimulation at 60 Hz.",
        "After learning, removing the antennae eliminated the learned field response. Wax treatments that restricted the antennal joints strongly reduced it, while coating the surfaces and keeping the joints mobile produced a smaller reduction. Learned responses to electric cues were still present after 24 h.",
        "The intervention pattern supports a contribution from **antennal mechanoreception**, including receptors linked to both joints. Johnston's organ is one of several possible sensors, alongside the antennal surface hairs. The conditioning demonstrates a usable cue under controlled conditions.",
    ],
    40: [
        "Ai and colleagues recorded intracellularly from identified honeybee interneurons while a mechanical stimulator vibrated the antennal flagellum. **DL-Int-1** branches in the dorsal lobe and related mechanosensory tissue. Dye filling and anti-GABA staining associated this cell type with a GABAergic phenotype.",
        "The stimulus carrier was 265 Hz, within the wing-vibration range relevant to waggle dancing. Pulse trains with durations up to 16 ms and intervals up to 33 ms suppressed DL-Int-1 firing below its spontaneous level. Longer 100 ms intervals allowed intermittent spikes during the train.",
        "This response distinguishes closely spaced vibration pulses from more widely spaced events. Antibody controls supported label specificity, and GABA staining links the cell to **inhibitory signaling**. Responses reveal **temporal filtering** of the vibration signal.",
    ],
    41: [
        "Ai and colleagues found a different response in **DL-Int-2**, another identified interneuron in the primary mechanosensory processing region. Its soma lacked the anti-GABA labeling seen in DL-Int-1, so its transmitter identity rests on other markers.",
        "At a 265 Hz carrier, trains with 16 ms pulses and 33 ms intervals evoked an initial excitation followed by maintained excitation. DL-Int-1, by contrast, was suppressed during comparable short-interval stimulation. **Tonic activity** is sustained activity during a stimulus, whereas **phasic activity** concentrates near a change such as onset.",
        "The contrasting responses could allow pulse-train duration to shape downstream signaling. A proposed inhibitory relationship between the two cell types rests on modeling and morphology rather than direct synaptic measurement, which places the recorded excitation within a proposed circuit for decoding advertised distance.",
    ],
    42: [
        "Kumaraswamy and colleagues compared DL-Int-1 in newly emerged workers aged 1–3 days with foragers older than 10 days. The preparation combined intracellular recording with dye-filled morphology, which kept cell identity constant across the age comparison.",
        "Gross arborization extent was similar between groups, but branch density differed in selected regions. Foragers' responses showed a stronger contrast between spontaneous activity and vibration-evoked inhibition, giving the stimulus a sharper **temporal signature**. Reconstructions and response distributions document these changes at two levels of analysis.",
        "Maturation can alter signal processing without replacing a neuron's overall projection pattern. Age and experience covary in this design, so the differences reflect development linked with foraging rather than a single cause.",
    ],
    43: [
        "Dong and colleagues created colonies of newly emerged workers without experienced dancers and compared them with mixed-age colonies. Individually marked bees first danced for a feeder 150 m away, and the same bees were tested again 20 days later.",
        "Bees that could not follow experienced dancers before their first dance produced larger **waggle-angle divergence** and more disordered movements. Their directional precision improved by the later test. First dances in mixed-age colonies were already more precise, which shows that early social exposure matters apart from simply performing a dance.",
        "The result supports social contributions to dance development alongside an inherited behavioral pattern. Later improvement could reflect age, flight practice, following experience or a combination. Colony composition changes several experiences together, so one teaching interaction is hard to single out.",
    ],
    44: [
        "In Dong and colleagues' 150 m feeder preparation, naive first dancers produced longer waggle runs and more waggles per run than first dancers from mixed-age colonies. The altered timing advertised a **greater distance**, even though the food location was the same.",
        "Twenty days later, the previously naive bees still produced the elevated distance signal. Their return-flight times had improved and their directional precision had recovered, yet the distance difference persisted. The persistence distinguishes distance calibration from changes that become more typical with later foraging experience.",
        "Social experience therefore influences different components of the dance in different ways. The lasting effect holds across the adult interval that was measured. The sensory and neural mechanisms that store this early calibration lie beyond these measurements.",
    ],
    45: [
        "Wang and colleagues tracked dance followers released either at the hive or at displaced sites within an explored landscape. The recruits had never visited the advertised food source. Harmonic radar sampled flight positions every 3 s.",
        "Both groups first flew approximately the communicated vector. During later search, displaced recruits directed more behavior toward the real feeder location than toward the virtual endpoint obtained by executing that vector from the wrong origin. Search could therefore draw on **landscape knowledge** acquired before the recruitment event.",
        "The authors interpreted this as inference of source location from map-like spatial knowledge. The contrast with Riley and colleagues' sparse-terrain experiment shows that initial vector flight and subsequent search make separate contributions.",
    ],
}
