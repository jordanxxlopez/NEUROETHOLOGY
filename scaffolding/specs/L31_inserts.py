"""Insert-slide paragraphs for Lecture 31 (scaffolding/RULES.md). Keyed by the original slide each insert follows."""

INSERT_PARAS = {
    3: [
        "A **corridor** is the band of ground that a bird covers repeatedly when it flies home along the same learned path. Its width describes how tightly a bird's training tracks cluster around one route. A narrow corridor means the bird returns to nearly the same ground on each journey, while a wide corridor means its paths vary more from flight to flight.",
        "Biro and colleagues measured corridor widths from each bird's final training tracks and expressed them relative to route length. The average width was 151 m at Weston Wood and 176 m at High Cogges. Scaling by route length places routes of different lengths on one scale, so the widths can be compared directly.",
        "A consistent route can still be indirect, so the width measures repeatability of the path rather than accuracy of arrival at the loft. The GPS records supply the positions used to calculate each width.",
    ],
    5: [
        "**Convergence** is the movement of a displaced bird back toward a route it has flown before. In an off-route release, the bird begins far from its usual corridor, so any turn toward the old track shows what draws it. Biro and colleagues recorded the complete homing track of each pigeon to see whether it headed straight for the loft or first rejoined the familiar route.",
        "Many off-route tracks merged with the previously used corridor before continuing toward home. The published maps show training and test tracks at a scale of about 2 km, so each displacement can be read against the surrounding terrain. The merge happened far from the release point, which places the pull of the route over a broad area.",
        "The merging points to attraction toward familiar visual landmarks, with the bird reaching recognized features before it turns toward the loft. Other navigational systems remained available during the same flights.",
    ],
    8: [
        "A **time-compensated sun compass** combines the sun's position with the bird's internal sense of time to estimate a direction. The sun moves across the sky at a steady rate, so the same solar position corresponds to a different compass direction at a different hour. Keeping the internal clock matched to local time keeps the sun compass accurate.",
        "Biro and colleagues shifted the birds' clock by delaying artificial sunrise and sunset by 4 h for 5–7 days. The shift predicted a solar-compass error of about 90° on the release dates. Tracks after treatment were set against each bird's earlier flights, so every pigeon's own route served as its baseline.",
        "A bird that follows its familiar route ignores part of the compass error, whereas a bird that trusts the compass moves away from the route. Each track shows which of these two cues the bird weights more heavily.",
    ],
    11: [
        "A **parallel offset** is a flight that keeps the shape of an earlier route while sitting consistently to one side of it. The bird maintains the sequence of turns and the overall form of the route, and only its position changes sideways. The displacement is measured from that bird's own former track, so each offset starts from its own route.",
        "After the clock shift, some highly familiar pigeons flew parallel to their former tracks on the anticlockwise side. Route-relative vectors measured the lateral offset in metres, with reference rings at 100, 300 and 500 m. The offsets were consistent across the birds that showed them.",
        "A parallel offset combines recognition of the route with a directional correction from the compass. The shape of the familiar route is kept while the whole route is moved to one side.",
    ],
    15: [
        "An **olfactory map** uses learned odor information to estimate position relative to home, so the smell of a place carries location. An **olfactory activation hypothesis** proposes that the experience of unfamiliar odors helps navigation even when the odors carry no location information. The two accounts predict different results when the odor history is changed.",
        "Gagliardo and colleagues transported pigeons in containers supplied with natural air, charcoal-filtered air or filtered air with artificial plant odors. Artificial odor puffs were supplied about every 20 min during transport and while the birds waited at the release site. Each group carried a different odor history into the release.",
        "The activation account predicts that artificial odors should help as much as natural air. The map account predicts that only natural air helps, because only natural air carries the geographical odor signature. The later tracks decide between these predictions.",
    ],
    18: [
        "A **nasal block** removes the sense of smell for a short time by anesthetizing the olfactory mucosa. Gagliardo and colleagues applied Xylocaine immediately before release, so every pigeon lost new odor input during early flight. The earlier odor histories of the groups stay in place.",
        "The birds had already been exposed to natural air, filtered air or artificial odors during transport and before takeoff. Releases occurred at sites 53 km and 61 km from home. The nasal block therefore limited new odor sampling for every group, while the earlier exposure differences remained.",
        "The anesthetic wears off during the flight, so the later part of each track reflects the return of smell. The timing of that recovery is part of each measured flight.",
    ],
    22: [
        "A **vanishing bearing** is the compass direction in which a released bird disappears from view. It records the first moments of the flight. A complete GPS track instead records the whole journey, including circling, stops, course correction and progress toward home.",
        "Bearings from the early part of each track did not reflect all the differences that appeared over the first hour. At the 53 km release, artificial-odor birds could leave in a set direction and then make little homeward progress. The full track revealed a deficit that the departure alone did not show.",
        "A bird can leave in a reasonable direction and then correct later, or leave poorly and recover. The full track is what shows how well the bird navigated.",
    ],
    25: [
        "The **dorsolateral hippocampal area** is one subdivision of the pigeon hippocampal formation, distinct from its dorsomedial and triangular subdivisions. Jorge and colleagues measured c-Fos labeling separately in each region, so the forebrain response is not treated as uniform across the hippocampus.",
        "Natural odors during displacement and unfamiliar artificial odors increased dorsolateral activation relative to filtered air. Artificial odor exposure at the home loft produced activation comparable to the displacement groups. The dorsolateral subdivision responded most strongly to the odor treatments.",
        "The same region responds to odor even when the bird has not been moved. Odor exposure alone is therefore enough to activate this part of the hippocampus.",
    ],
    28: [
        "The **trigeminal nerve** carries sensory information from the head, and its ophthalmic branch, V1, projects to brainstem trigeminal nuclei. Lefeldt and colleagues used ZENK labeling to ask whether changing magnetic fields activated these nuclei in pigeons.",
        "Pigeons were exposed for 3 h to a constantly changing magnetic field, to a compensated zero field, or to the changing field after bilateral V1 section. ZENK was detected in the principal and spinal trigeminal nuclei after each exposure, and the pattern across the three groups shows where the changing field had its effect.",
        "Labeling rose when the field changed and V1 was intact, and it fell when the field was removed or the nerve was cut. The response therefore runs through the peripheral sensory pathway that passes through V1.",
    ],
    31: [
        "**Neuronal tracing** follows the anatomical pathways that leave an injection site. Lefeldt and colleagues injected cholera toxin B into V1 to label its central projections. The labeled fibers were then matched to the regions that showed ZENK after magnetic stimulation.",
        "V1 fibers terminated in the principal and spinal trigeminal nuclei, the same nuclei that contained ZENK-positive cells. The overlays keep the position of each traced fiber relative to the activated cells, with scales of 100 µm and 200 µm. Acetylcholinesterase staining marked the nuclear boundaries, so each subdivision could be located precisely.",
        "The overlap places the magnetic response along a known route from the nerve to the brainstem. Acetylcholinesterase keeps the labeled tissue tied to the known anatomy of each nucleus.",
    ],
    34: [
        "**Prussian blue** is a stain that reveals ferric iron in tissue. A stained spot shows where iron accumulates, but identifying the cell that holds it needs a second line of evidence, because iron also appears in metabolic storage and immune cells.",
        "Treiber and colleagues stained pigeon upper beaks with Prussian blue and mapped the labeled cells through serial sections. The stained cells lay in the respiratory epithelium, the subepidermal tissue and the feather follicles. The position of each labeled cell is recorded together with its tissue.",
        "The stained positions give a map of where iron occurs, which is the first step toward identifying a magnetic receptor. Additional markers and ultrastructure then identify the stained cells.",
    ],
    37: [
        "**Macrophages** are immune cells that engulf material and take part in tissue defense. **MHC II** is a cell-surface marker of antigen presentation that several immune cell types express. Treiber and colleagues combined this marker with iron staining to identify the beak cells.",
        "MHC II labeling colocalized with the iron-positive cells in the respiratory epithelium, the subepidermal tissue and the feather follicles. Together with the ultrastructure and the absence of convincing neuronal-marker labeling, this result identifies the cells as macrophages. The micrographs carry a 10 µm scale bar.",
        "Macrophages carry iron as a storage product, so the iron in these cells is stored rather than sensed. The identity of the cells rests on several markers taken together across the tissues.",
    ],
    39: [
        "A **local field potential**, or LFP, is an extracellular voltage that reflects coordinated activity in a population of neurons around the electrode. It differs from the spike of one identified neuron, because it sums the currents of many cells at once.",
        "Yang and colleagues recorded hippocampal LFPs and the bird's position at the same time during outdoor homing flights. The electrodes sampled the left hippocampal formation, and the release sites lay more than 0.8 km from the loft. Trials were run in clear weather with low wind.",
        "Recording the population signal during flight links a neural state to a particular stage of the trip. The shared time base allows each stage to be matched to a moment in the recording.",
    ],
    42: [
        "**Spectral power** measures how much of a recorded voltage falls within a chosen frequency range. Yang and colleagues assigned theta to 4–12 Hz, beta to 12–30 Hz, low gamma to 30–60 Hz and high gamma to 60–120 Hz, so each band has a fixed range.",
        "Theta and beta power ratios were higher in the initial decision-making stage than during en route flight. The high-gamma ratio rose en route, while low gamma showed no consistent difference between the stages. The comparisons used paired stages from the same homing flights.",
        "The stages therefore differ in how power is distributed across the bands rather than in a single overall increase. Each band reflects its own pattern of population activity.",
    ],
}
