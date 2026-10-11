"""Scaffold spec for Lecture 31 (Drive deck Neuroethology_Lecture31_FA2026.pptx). Body rewrites are in body_L31.py."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L31 as _body  # noqa: E402


def ins(after, title, paragraphs, citation, notes, refs):
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


inserts = [
    ins(3, "Corridor width measures how consistent a route is", [
        "A **corridor** is the band of ground a bird covers repeatedly when it flies home along the same learned path. Its width describes how tightly a bird's training tracks cluster around one route. A narrow corridor means the bird returns to nearly the same ground on each journey, whereas a wide corridor means its paths vary more from flight to flight.",
        "Biro and colleagues measured corridor widths from each bird's final training tracks, expressed relative to its route length. The average width was 151 m at Weston Wood and 176 m at High Cogges. Because the width is scaled to the route, routes of different lengths can be compared on one scale.",
        "The corridor width therefore captures consistency in the flight path, not the accuracy of arrival at the loft. A pigeon can stay within a narrow corridor and still take an indirect route, so the width summarizes how repeatable the path is. The GPS records supply this measure directly from the tracks.",
    ], "Biro et al. (2004)", [
        "Corridor width is a property of the flight tracks themselves.",
        ["Definition.", "A corridor is the band of ground covered on repeated flights along one learned path.", "A narrow band means the tracks cluster tightly."],
        ["Measurement.", "Widths came from each bird's final training tracks.", "The widths were scaled to route length so that routes could be compared."],
        ["Values.", "Mean widths were 151 m at Weston Wood and 176 m at High Cogges.", "Both values come from repeated training flights."],
        ["Consistency and accuracy.", "A consistent route can still be indirect.", "The width measures repeatability, while arrival is a separate outcome."],
        ["Data source.", "The GPS records supply the positions used for the widths.", "The measure follows directly from the recorded tracks."],
        ["Meaning.", "Narrow corridors show that each bird keeps to its own route.", "The width gives a compact summary of that route."],
    ], ["Biro 2004"]),
    ins(5, "Convergence reveals a pull toward a learned corridor", [
        "**Convergence** is the movement of a displaced bird back toward a route it has flown before. In an off-route release, the bird begins far from its usual corridor, so any turn toward the old track shows what draws it. Biro and colleagues recorded the complete homing track of each pigeon to see whether it headed straight for the loft or first rejoined the familiar route.",
        "Many off-route tracks merged with the previously used corridor before continuing toward home. The published maps show the training tracks alongside the test tracks at a scale of about 2 km, so each displacement can be read against the surrounding terrain. The merge happened far from the release point, which indicates that the route exerts its pull over a broad area.",
        "The merging supports attraction toward familiar visual landmarks more than a fresh calculation of the shortest course. The pigeon reaches features it recognizes first and follows the route toward the loft afterward. Other navigational systems remained available during the same flights, so the convergence reflects a combination of guidance rather than one signal.",
    ], "Biro et al. (2004)", [
        "Displacement tests show what a bird goes back to.",
        ["Off-route release.", "Each pigeon was released outside its preferred corridor.", "Its complete track shows the route it followed."],
        ["Merging.", "Many tracks rejoined the previously used corridor.", "The rejoining happened well away from the release point."],
        ["Scale.", "The maps use a scale of about 2 km.", "Each displacement can be compared with the surrounding landscape."],
        ["Interpretation.", "The merge fits attraction toward recognized landmarks.", "A fresh shortest-path calculation does not explain the pattern."],
        ["Other systems.", "Other navigational systems stayed available during the flights.", "The pull of the route is one part of the guidance."],
        ["Route memory.", "The learned corridor shapes where the bird goes after displacement.", "The effect depends on the familiar features along the route."],
    ], ["Biro 2004"]),
    ins(8, "Time-compensated sun compass uses the sun and clock", [
        "A **time-compensated sun compass** combines the sun's position with the bird's internal sense of time to estimate a direction. The sun moves across the sky at a steady rate, so the same solar position corresponds to a different compass direction at a different hour. Keeping the internal clock matched to local time keeps the sun compass accurate.",
        "Biro and colleagues shifted the birds' clock by delaying artificial sunrise and sunset by 4 h for 5–7 days. The shift predicted a solar-compass error of about 90° on the release dates. The tracks after treatment were compared with each bird's earlier flights, so every pigeon's own route served as the baseline.",
        "The clock shift sets the sun compass against the landmarks that the bird recognizes. A bird that follows its familiar route ignores part of the compass error, whereas a bird that trusts the compass moves away from the route. The contrast shows that the sun is one source among several that the pigeon combines.",
    ], "Biro et al. (2007)", [
        "The sun compass depends on time as well as on the sun.",
        ["Principle.", "The sun's position changes steadily through the day.", "A bird must know the time to read the sun correctly."],
        ["Manipulation.", "Artificial sunrise and sunset were delayed by 4 h.", "The delay lasted 5–7 days."],
        ["Prediction.", "The shift predicted a solar-compass error of about 90°.", "The predicted error is the size of the directional conflict."],
        ["Controls.", "Each pigeon was compared with its own earlier flights.", "This keeps individual routes as the reference."],
        ["Conflict.", "The familiar route and the compass point in different directions.", "The bird's track shows which one it follows."],
        ["Combination.", "The sun is one of several cues that the bird weighs.", "Landmarks and other cues remain available."],
    ], ["Biro 2007"]),
    ins(11, "Parallel offsets keep shape while shifting position", [
        "A **parallel offset** is a flight that keeps the shape of an earlier route while sitting consistently to one side of it. The bird does not abandon its route for a new straight line. It maintains the sequence of turns and the overall form, and only the position changes.",
        "After the clock shift, some highly familiar pigeons flew parallel to their former tracks on the anticlockwise side. Route-relative vectors measured the lateral offset in metres, with reference rings at 100, 300 and 500 m that make each displacement easy to compare. The offsets were consistent across the birds that showed them.",
        "Parallel offsets indicate that landmark attraction and compass influence act together during the journey. The bird keeps its learned route shape while the compass shifts the whole route sideways. A flight of this kind combines recognition of features with a directional correction.",
    ], "Biro et al. (2007)", [
        "A parallel offset separates the shape of a route from its position.",
        ["Definition.", "The bird keeps the shape of its earlier route.", "The whole route is moved to one side."],
        ["Measurement.", "Vectors were calculated relative to the route.", "Rings at 100, 300 and 500 m mark the size of the offset."],
        ["Direction.", "Some pigeons shifted anticlockwise of their former tracks.", "The bias was retained in the route-relative vectors."],
        ["Two sources.", "Landmark attraction keeps the shape.", "Compass influence moves the position."],
        ["Contrast.", "A straight compass flight would abandon the route shape.", "The offsets do not do that."],
        ["Meaning.", "Route memory and the compass operate together.", "Each flight shows the balance between them."],
    ], ["Biro 2007"]),
    ins(15, "Olfactory map versus activation hypothesis", [
        "An **olfactory map** uses learned odor information to estimate position relative to home, so the smell of a place carries location. An **olfactory activation hypothesis** proposes that the mere experience of unfamiliar odors helps navigation, even when the odors carry no location information. The two accounts predict different results when the odor history is changed.",
        "Gagliardo and colleagues transported pigeons in containers supplied with natural air, charcoal-filtered air or filtered air with artificial plant odors. Artificial odor puffs were supplied about every 20 min during transport and while the birds waited at the release site. Each group therefore carried a different odor history into the release.",
        "The activation account predicts that artificial odors should help as much as natural air. The map account predicts that only the natural mixture helps, because only natural air carries the geographical odor signature. The later tracks decide between these predictions.",
    ], "Gagliardo et al. (2011)", [
        "The two odor accounts make different predictions.",
        ["Map account.", "Odors carry location through their mixture.", "Only natural air holds the geographical signature."],
        ["Activation account.", "Any unfamiliar odor stimulates the sense of smell.", "Stimulation alone may help navigation."],
        ["Transport.", "Birds were carried in containers with different air supplies.", "Artificial odors were added in puffs about every 20 min."],
        ["Waiting period.", "The same air conditions applied while birds waited at the release site.", "The odor history continued up to release."],
        ["Comparison.", "The later tracks show which prediction holds.", "The groups differ only in the air they received."],
        ["Outcome.", "The result depends on whether location information was present.", "Sensory stimulation alone was tested as a separate condition."],
    ], ["Gagliardo 2011"]),
    ins(18, "Nasal anesthesia applies the same block to all groups", [
        "A **nasal block** removes the sense of smell for a short time by anesthetizing the olfactory mucosa. Gagliardo and colleagues applied Xylocaine immediately before release, so every pigeon lost new odor input during early flight. Because the block was the same across groups, any difference between the groups must come from the odors they experienced before release.",
        "The birds had already been exposed to natural air, filtered air or artificial odors during transport and before takeoff. Releases occurred at sites 53 km and 61 km from home. The shared block limited new odor sampling while the earlier exposure differences stayed in place.",
        "This design isolates the effect of prior odor history on navigation. The anesthesia wears off, so the later part of the flight reflects smell returning, and the timing of that recovery is part of the measured flight.",
    ], "Gagliardo et al. (2011)", [
        "The nasal block holds new odor input constant across groups.",
        ["Anesthetic.", "Xylocaine was applied to the olfactory mucosa.", "The block was applied immediately before release."],
        ["Common condition.", "All three air-exposure groups received the same block.", "New odor input was reduced equally."],
        ["Prior exposure.", "Birds had experienced their assigned air before release.", "The earlier exposure was the variable under test."],
        ["Release sites.", "Releases occurred at 53 km and 61 km from home.", "Two sites allowed the result to be checked."],
        ["Recovery.", "The block wears off during the flight.", "The later flight includes returning smell."],
        ["Interpretation.", "Differences between groups reflect earlier odor history.", "Early navigation is the main outcome."],
    ], ["Gagliardo 2011"]),
    ins(22, "Bearings and tracks describe different flight phases", [
        "A **bearing** is the compass direction in which a released bird disappears from view. It records the first moments of the flight. A complete GPS track instead records the whole journey, including circling, stops, course correction and progress toward home.",
        "Gagliardo and colleagues found that bearings from the early part of each track did not reflect all the differences that appeared over the first hour. At the 53 km release, artificial-odor birds could leave in a set direction and then make little homeward progress. The full track revealed a deficit that the departure alone did not show.",
        "The two measures therefore describe different stages of the same flight. A bird can leave in a reasonable direction and correct later, or leave poorly and recover, so the full track is needed to judge how well it navigated.",
    ], "Gagliardo et al. (2011)", [
        "A departure bearing is only the first part of a flight.",
        ["Bearing.", "The bearing is the direction at which the bird is last seen.", "It describes the start of the flight."],
        ["Full track.", "The complete GPS track records the whole route.", "It includes circling, stops and course correction."],
        ["Early results.", "Early bearings missed some differences.", "The differences appeared over the first hour."],
        ["Release site.", "At 53 km, artificial-odor birds departed and then progressed little.", "The departure alone looked normal."],
        ["Two stages.", "Departure and later progress are separate measures.", "Each one reports a different phase."],
        ["Judgment.", "Navigation quality is judged from the full track.", "A single early direction is not enough."],
    ], ["Gagliardo 2011"]),
    ins(25, "c-Fos maps regional activity, not single neurons", [
        "**c-Fos** is an activity-related protein whose presence marks cells that recently fired. Antibody labeling reveals the labeled nuclei, and their density in a region shows how strongly that region was engaged over the hours before sampling. The measure summarizes activity across a region instead of recording the spikes of single cells.",
        "Jorge and colleagues sampled brains 1–2 h after each odor treatment and counted labeled nuclei per square millimetre in the hippocampal formation, olfactory bulb and piriform cortex. Each condition was compared against controls processed the same way. The counts show which regions responded to each treatment.",
        "A regional count shows where activity accumulated across the sampled tissue. The dorsolateral hippocampal area stands out because its labeling tracked the odor treatments most closely, which tells the reader where the response was strongest.",
    ], "Jorge et al. (2014)", [
        "c-Fos is a regional index of recent activity.",
        ["Marker.", "c-Fos marks cells that recently fired.", "Labeled nuclei are detected with an antibody."],
        ["Density.", "Labeled nuclei were counted per square millimetre.", "The density gives a regional value."],
        ["Timing.", "Brains were sampled 1–2 h after each treatment.", "The label reflects activity over that window."],
        ["Regions.", "The hippocampal formation, olfactory bulb and piriform cortex were sampled.", "Each region gives its own count."],
        ["Controls.", "Each condition was compared against matched controls.", "Differences reflect the treatment."],
        ["Result.", "The dorsolateral hippocampal area responded most to the odors.", "The regional pattern shows where the activity was strongest."],
    ], ["Jorge 2014"]),
    ins(28, "Magnetic stimulation labels trigeminal nuclei", [
        "The **trigeminal nerve** carries sensory information from the head to brainstem nuclei. Its ophthalmic branch, V1, sends fibers to the principal and spinal trigeminal nuclei. Lefeldt and colleagues used ZENK labeling to ask whether changing magnetic fields activated these nuclei in pigeons.",
        "Pigeons were exposed for 3 h to a constantly changing magnetic field, to a compensated zero field, or to the changing field after bilateral V1 section. ZENK was detected in the principal and spinal trigeminal nuclei after each exposure. The pattern of labeling across the three groups shows where the changing field had its effect.",
        "Labeling rose when the field changed and V1 was intact, and it fell when the field was removed or the nerve was cut. The result links the magnetic stimulus to the peripheral sensory pathway that runs through V1.",
    ], "Lefeldt et al. (2014)", [
        "Trigeminal labeling depends on both the field and the nerve.",
        ["Nerve.", "V1 is the ophthalmic branch of the trigeminal nerve.", "It carries sensory input from the head."],
        ["Nuclei.", "The principal and spinal trigeminal nuclei receive V1 input.", "ZENK marks them after exposure."],
        ["Exposure.", "Birds spent 3 h in one of three magnetic conditions.", "The conditions were changing, zero, and changing with V1 section."],
        ["Pattern.", "Labeling was highest with an intact nerve and a changing field.", "Removing either reduced it."],
        ["Controls.", "The zero-field condition removes the changing stimulus.", "V1 section removes the nerve input."],
        ["Link.", "The result connects magnetic stimulation to a peripheral pathway.", "The pathway runs through V1."],
    ], ["Lefeldt 2014"]),
    ins(31, "Tracing shows a route from V1 to labeled nuclei", [
        "**Neuronal tracing** follows the anatomical pathways that leave an injection site. Lefeldt and colleagues injected cholera toxin B into V1 to label its central projections. The labeled fibers were then compared with the regions that showed ZENK after magnetic stimulation.",
        "V1 fibers terminated in the principal and spinal trigeminal nuclei, which are the same nuclei that contained ZENK-positive cells. The overlays keep the position of each traced fiber relative to the activation, with scales of 100 µm and 200 µm. Acetylcholinesterase staining marked the nuclear boundaries, so the subdivisions could be located precisely.",
        "The overlap places the magnetic response along a known route from the nerve to the brainstem. Acetylcholinesterase acts here as a marker of boundaries, which keeps the labeled tissue tied to the known anatomy.",
    ], "Lefeldt et al. (2014)", [
        "Tracing links the nerve to the labeled brainstem.",
        ["Injection.", "Cholera toxin B was injected into V1.", "It labels the central projections of V1."],
        ["Overlap.", "The labeled fibers overlapped the ZENK-positive nuclei.", "The same nuclei received V1 input."],
        ["Scale.", "The overlays carry 100 µm and 200 µm scale bars.", "Positions can be compared across sections."],
        ["Boundaries.", "Acetylcholinesterase outlines the nuclei.", "Subdivisions are located from the stain."],
        ["Route.", "The fibers link the nerve to the brainstem.", "The route runs from the periphery to the labeled tissue."],
        ["Anatomy.", "The tracing keeps the response within known regions.", "Each step follows an anatomical pathway."],
    ], ["Lefeldt 2014"]),
    ins(34, "Stains locate iron, not the cell that holds it", [
        "**Prussian blue** is a stain that reveals ferric iron in tissue. A stained spot shows where iron accumulates, and a second line of evidence is needed to name the cell that holds it, since iron also appears in metabolic storage and immune cells.",
        "Treiber and colleagues stained pigeon upper beaks with Prussian blue and mapped the labeled cells through serial sections. The stained cells lay in respiratory epithelium, subepidermal tissue and feather follicles. The position of each labeled cell is therefore recorded alongside its tissue.",
        "The stained positions give a map of where iron occurs, which is the first step toward identifying a magnetic receptor. Further markers and ultrastructure then decide whether the stained cells are sensory or storage cells.",
    ], "Treiber et al. (2012)", [
        "Staining locates iron, and a cell is identified by more markers.",
        ["Stain.", "Prussian blue detects ferric iron.", "A blue spot marks iron, not a cell type."],
        ["Sections.", "Labeled cells were mapped through serial sections.", "Each cell has a recorded position."],
        ["Tissues.", "Labeled cells lay in three tissue types.", "These tissues are distinct in the beak."],
        ["Iron sources.", "Iron also appears in storage and immune cells.", "A stain alone cannot name the cell."],
        ["Next step.", "Additional markers and ultrastructure identify the cell.", "Those tests decide the cell's role."],
        ["Meaning.", "The stain gives the first map of iron positions.", "Identification follows from further tests."],
    ], ["Treiber 2012"]),
    ins(37, "Immune markers test cell identity in beak tissue", [
        "**Macrophages** are immune cells that engulf material and take part in tissue defense. MHC II is a cell-surface marker of antigen presentation that several immune cell types express. Treiber and colleagues combined this marker with iron staining to check whether the beak cells were immune cells.",
        "MHC II labeling colocalized with the iron-positive cells in respiratory epithelium, subepidermal tissue and feather follicles. The ultrastructure and the lack of convincing neuronal-marker labeling supported macrophages over magnetosensitive neurons. The micrographs carry a 10 µm scale bar.",
        "Cell identity determines whether iron in a cell can carry magnetic information. An iron-laden macrophage is a storage cell, and that identity rests on several markers taken together across the tissues.",
    ], "Treiber et al. (2012)", [
        "Immune markers identify the iron-containing cells.",
        ["Macrophage.", "Macrophages engulf material in tissue.", "They are part of the immune system."],
        ["Marker.", "MHC II marks antigen presentation.", "Several immune cell types express it."],
        ["Colocalization.", "MHC II labeling overlapped the iron-positive cells.", "The overlap occurred in all three tissues."],
        ["Neuronal markers.", "Convincing neuronal-marker labeling was absent.", "The absence weakens the neuron identity."],
        ["Scale.", "The micrographs carry a 10 µm scale bar.", "The cell size can be checked."],
        ["Meaning.", "The cells are best identified as macrophages.", "Iron in these cells is a storage product."],
    ], ["Treiber 2012"]),
    ins(39, "Local field potentials sum population activity", [
        "A **local field potential** is an extracellular voltage that reflects coordinated activity in a population of neurons around the electrode. It differs from the spike of one identified neuron, because it sums the currents of many cells at once.",
        "Yang and colleagues recorded hippocampal LFPs and the bird's position at the same time during outdoor homing flights. The electrodes sampled the left hippocampal formation, and the release sites lay more than 0.8 km from the loft. Trials were run in clear weather with low wind.",
        "Recording the population signal during flight allows the neural state to be read against the bird's position and heading. The shared time base is what links a population rhythm to a particular stage of the trip.",
    ], "Yang et al. (2025)", [
        "The LFP is a population signal recorded during flight.",
        ["Definition.", "An LFP is an extracellular voltage from many cells.", "It differs from a single neuron's spike."],
        ["Recording.", "LFPs were recorded with the bird's position.", "Both signals share one time base."],
        ["Site.", "Electrodes sampled the left hippocampal formation.", "The side of the recording is fixed."],
        ["Flights.", "Release sites were more than 0.8 km from the loft.", "Trials were run in clear weather with low wind."],
        ["Analysis.", "The population signal is compared across flight stages.", "The position data identify each stage."],
        ["Meaning.", "Population activity tracks the bird's trip.", "The LFP summarizes many cells together."],
    ], ["Yang 2025"]),
    ins(42, "Band power changes between navigation stages", [
        "**Spectral power** measures how much of a recorded voltage falls within a chosen frequency range. Yang and colleagues assigned theta to 4–12 Hz, beta to 12–30 Hz, low gamma to 30–60 Hz and high gamma to 60–120 Hz, so each band has a fixed range.",
        "Theta and beta power ratios were higher in the initial decision-making stage than during en route flight. The high-gamma ratio rose en route, while low gamma showed no consistent difference between stages. The comparisons used paired stages from the same homing flights.",
        "The stages therefore differ in how power is distributed across the bands, rather than in a single overall increase. Each band reflects a separate pattern of population activity, and the stage contrast depends on the band selected.",
    ], "Yang et al. (2025)", [
        "Each frequency band reflects a different pattern of activity.",
        ["Bands.", "Theta is 4–12 Hz and beta is 12–30 Hz.", "Low gamma is 30–60 Hz and high gamma is 60–120 Hz."],
        ["Stages.", "Initial decision-making is the early circling stage.", "En route flight is the stable homeward stage."],
        ["Theta and beta.", "Both ratios were higher during decision-making.", "The ratios fell during the en route stage."],
        ["High gamma.", "High gamma rose during the en route stage.", "Low gamma showed no consistent change."],
        ["Pairing.", "The comparisons used stages from the same flights.", "Individual birds served as their own controls."],
        ["Meaning.", "The stage difference is in the distribution across bands.", "No single band captures the change."],
    ], ["Yang 2025"]),
]

EXTRA_NOTES = [
    ["Source values.", "The published tracks and the measured values come from the original paper.", "Each value is reported with the scale used in the source."],
    ["Why the measure matters.", "The result separates the bird's measured behavior from the mechanism that produces it.", "The comparison stays within the same birds or sites."],
]
APPEND_P3 = {
    18: " The comparison therefore keeps the nasal block constant while the earlier odor history changes.",
    22: " Each measure is kept separate in the analysis so that the early and late parts of the flight are not confused.",
    28: " The labeling pattern therefore identifies which nuclei the changing field reached.",
    31: " The labeled fibers and the activated nuclei are compared in the same sections, which keeps the spatial relation intact.",
    34: " Each stained location is then examined for the cell type that carries it.",
    37: " Together, the markers and the ultrastructure give a consistent identity for the cells, and the immune identity is what the pigeon-beak data show.",
    39: " The population signal therefore reflects the activity of many cells recorded at one electrode.",
}
for _ins in inserts:
    _ins["notes"] = [_ins["notes"][0]] + _ins["notes"][1:] + EXTRA_NOTES
    if _ins["after"] == 37:
        _ins["notes"].append(["Context.", "Macrophages are normal residents of many tissues.", "Their iron load comes from the material they clear."])
    if _ins["after"] in APPEND_P3:
        _ins["paragraphs"][2] = _ins["paragraphs"][2] + APPEND_P3[_ins["after"]]
spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(_body.body)} body slides rewritten, {len(inserts)} scaffold slides")
