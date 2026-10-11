"""Scaffold spec for Lecture 37 (Drive deck Neuroethology_Lecture37_FA2026.pptx). Body rewrites are in body_L37.py."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L37 as _body  # noqa: E402
import L37_extend as _ext  # noqa: E402
import L37_insert_extend as _insx  # noqa: E402


def ins(after, title, paragraphs, citation, notes, refs):
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


OKEEFE = "O'Keefe & Dostrovsky (1971)"
HAFTING = "Hafting et al. (2005)"
GIOCOMO = "Giocomo et al. (2011)"

inserts = [
    ins(3, "Moving electrodes capture spikes during behavior", [
        "A microdrive moves the electrode in small steps, so a single unit can be followed as the rat changes behavior. Walking, grooming, eating and resting were all observed during the same recording session, so each spike train is paired with the behavior it accompanies.",
        "Differential recording subtracts the signal shared by two nearby electrodes. That subtraction reduced artifacts from muscle and movement, which let the spikes of the hippocampal unit stand out during free movement.",
        "The authors also presented sounds, moving visual stimuli, odors and touch to the same units. Responses to these stimuli separated spatially dependent firing from ordinary sensory responsiveness.",
    ], OKEEFE, [
        "Movable electrodes capture spikes during behavior.",
        ["Recording.", "The electrode advanced through the hippocampus.", "The rat moved and rested freely."],
        ["Artifacts.", "Shared muscle signals were subtracted.", "Spikes stood out during movement."],
        ["Stimuli.", "Sounds, visual, odor and touch stimuli were tested.", "Spatial responses were separated from sensory ones."],
        ["Meaning.", "Behavior and spikes are recorded together.", "Spatial tuning is identified in free movement."],
    ], ["O'Keefe 1971"]),
    ins(6, "Light removal abolishes a touch-evoked response", [
        "Turning off the lights removed the response of the featured CA1 unit. The restricted tactile response therefore depended on visual information, even though touch on the animal's back was the stimulus that evoked the firing.",
        "Moving striped cards produced no response that a small visual receptive field could explain. A receptive field is the region of sensory space in which a suitable stimulus changes a neuron's activity, and the result pointed to the wider surrounding view.",
        "The rat turned through several effective orientations, so a fixed retinal image is an unlikely explanation. The observations favored dependence on the surrounding visual configuration over any single landmark.",
    ], OKEEFE, [
        "Light removal abolishes a touch-evoked response.",
        ["Darkness.", "Lights were switched off.", "The tactile response disappeared."],
        ["Receptive field.", "No small visual field explained the response.", "The surrounding view was implicated."],
        ["Orientation.", "The rat rotated through effective orientations.", "A fixed retinal image was unlikely."],
        ["Meaning.", "Visual configuration shapes the response.", "Touch alone was not sufficient."],
    ], ["O'Keefe 1971"]),
    ins(9, "The cognitive map links firing to predicted input", [
        "O'Keefe and Dostrovsky proposed that spatially selective cells, together with movement signals, could recruit cells representing subsequent orientations. In this model the network anticipates the sensory input that movement brings.",
        "The 1971 recordings established location-dependent firing. Prediction, route selection and the explanation of lesion-induced deficits were extensions that the authors built on those recordings.",
        "A neural representation is a reliable link between activity and a variable. A navigational mechanism adds transformations that guide behavior, and testing that mechanism calls for circuit manipulations during tasks that require spatial choices.",
    ], OKEEFE, [
        "The cognitive map links firing to predicted input.",
        ["Proposal.", "Selective cells recruit subsequent orientations.", "Movement signals drive the recruitment."],
        ["Evidence.", "Location-dependent firing was recorded.", "Prediction was an extension of that firing."],
        ["Representation.", "A representation links activity to a variable.", "A mechanism adds behavior-guiding transformations."],
        ["Meaning.", "The map is a testable circuit hypothesis.", "Manipulations during spatial choice tasks test it."],
    ], ["O'Keefe 1971"]),
    ins(12, "Occupancy correction sets the firing-rate scale", [
        "Hafting and colleagues recorded spikes while rats explored a circular arena, and the animals spent unequal time at each location. The firing rate at each location relates the spike count to the time the animal spent there.",
        "Repeated regions of elevated rate remained after occupancy was built into the analysis. The repeated pattern therefore reflects where the cell fires, not where the rat lingers.",
        "Locations sampled poorly give little information about firing, so the reliability of each rate value depends on how thoroughly the arena was explored. A color map of these rates displays measured activity across the whole arena.",
    ], HAFTING, [
        "Occupancy correction sets the firing-rate scale.",
        ["Occupancy.", "Rats spent unequal time at locations.", "Rates were scaled by the time available."],
        ["Result.", "Repeated elevated regions remained.", "The pattern reflects firing, not lingering."],
        ["Sampling.", "Poorly sampled locations are uncertain.", "Exploration sets reliability."],
        ["Meaning.", "Rate maps show measured activity.", "The map is a record of spiking."],
    ], ["Hafting 2005"]),
    ins(15, "Repeated fields survive a change of arena size", [
        "Hafting and colleagues moved animals between a large and a smaller circular enclosure and then back to the large one. The triangular organization stayed recognizable across the change in available surface.",
        "The larger arena contained more activity nodes at a similar density. The pattern was therefore a repeated code, not a small set of fields stretched to fit the walls.",
        "The authors discussed grids of potentially unlimited extent, and each arena size sets how much of the pattern a recording can sample. The periodic code is a property of the cell rather than of the enclosure that holds it.",
    ], HAFTING, [
        "Repeated fields survive a change of arena size.",
        ["Arenas.", "Animals moved between two circular enclosures.", "The large enclosure was revisited."],
        ["Pattern.", "The triangular organization stayed recognizable.", "Node density stayed similar."],
        ["Extent.", "Grids could extend beyond one arena.", "Arena size sets how much is sampled."],
        ["Meaning.", "The periodic code belongs to the cell.", "Enclosures only reveal part of it."],
    ], ["Hafting 2005"]),
    ins(18, "Field size grows with the spatial scale", [
        "A firing field is a region where a cell's rate exceeds its surrounding background under the tested conditions. Hafting and colleagues measured field size from the central peak of the spatial autocorrelation.",
        "Ventral positions showed greater spacing and larger fields together. The two properties are related but separate: spacing describes the gap between fields, and field size describes the extent of each one.",
        "Joint growth of spacing and field size produces a coarser pattern, not a set of unchanged fields moved farther apart. Field size depends on the analysis threshold, so it measures an activity region rather than a visible anatomical boundary.",
    ], HAFTING, [
        "Field size grows with the spatial scale.",
        ["Field.", "A firing field exceeds background rate.", "Field size came from the autocorrelation peak."],
        ["Pattern.", "Ventral sites had larger spacing and fields.", "The two properties are related."],
        ["Growth.", "Spacing and field size increase together.", "The pattern becomes coarser."],
        ["Meaning.", "Field size is an operational measure.", "It depends on the threshold."],
    ], ["Hafting 2005"]),
    ins(21, "Cross-correlation reveals a phase offset", [
        "Spatial cross-correlation compares two neurons' rate maps as one map slides across the other. A peak away from the origin marks the displacement that aligns the two firing patterns.",
        "Neighboring grid cells shared spacing and orientation, yet their nearest peaks were offset from the origin. That offset measures the difference in spatial phase between the two cells.",
        "Cells at different recording sites have different scales and orientations, so their cross-correlations are less sharply aligned. Shared inputs can produce a correlated pattern without any direct synapse between the recorded cells.",
    ], HAFTING, [
        "Cross-correlation reveals a phase offset.",
        ["Method.", "One rate map slides across another.", "Peaks mark aligning displacements."],
        ["Offset.", "Neighbors share spacing and orientation.", "Their peaks are displaced from the origin."],
        ["Sites.", "Distant cells differ in scale.", "Alignment is sharper for nearby cells."],
        ["Meaning.", "Phase is measured as an offset.", "Shared inputs can produce correlation."],
    ], ["Hafting 2005"]),
    ins(24, "Grid firing remains in the dark", [
        "Hafting and colleagues recorded a grid cell across 10 min of light, 10 min of darkness and a return to light. The animal stayed in the same environment throughout the session.",
        "The grid pattern persisted in darkness, although its fields became somewhat dispersed or displaced. Self-motion signals, which come from the animal's own movement, stay available when visual landmarks are removed.",
        "Persistence without vision fits movement-based updating of location. Odors, touch and boundaries remain available, so self-motion is one of several inputs that can drive the pattern in darkness.",
    ], HAFTING, [
        "Grid firing remains in the dark.",
        ["Protocol.", "Light, darkness and light were alternated.", "The animal stayed in the same room."],
        ["Result.", "The grid pattern persisted in darkness.", "Fields became somewhat dispersed."],
        ["Self-motion.", "Movement signals remain without vision.", "They update the estimate of location."],
        ["Meaning.", "Movement contributes to the grid.", "Other cues also remain available."],
    ], ["Hafting 2005"]),
    ins(27, "Landmark experience aligns the grid to a new room", [
        "Hafting and colleagues compared a familiar room with a novel room and tested the familiar room again. Rate maps in the novel room became more consistent during continued exploration.",
        "The grid's orientation differed between the familiar and novel rooms, while repeated familiar-room tests changed much less. The same organizing principle was therefore expressed with room-specific alignment.",
        "The authors proposed that learning builds associations between landmarks and the grid's phase and orientation. This account explains the gradual stabilization of alignment that appeared over continued exploration.",
    ], HAFTING, [
        "Landmark experience aligns the grid to a new room.",
        ["Rooms.", "A familiar room, a novel room and a return were tested.", "Exploration continued in each."],
        ["Alignment.", "The novel-room orientation differed.", "Familiar-room tests changed less."],
        ["Stability.", "Novel-room maps became more consistent.", "Stability grew with exploration."],
        ["Meaning.", "Landmark associations shape the alignment.", "The learned alignment is room-specific."],
    ], ["Hafting 2005"]),
    ins(30, "The larger box reveals the knockout grid pattern", [
        "The 100 × 100 cm box provided enough extent to recognize repeated fields across the dorsal-to-ventral range. Mice explored this larger box in the main sessions of the HCN1 experiment.",
        "The 50 × 50 cm box supported measurements of boundary-related and head-direction activity. Its size did not reveal every grid's full periodicity, so the principal grid comparison used the larger box.",
        "Arena dimensions set how much of a spatial pattern can be sampled. A lattice missing from a small box can still be present, which makes the larger box important when spacing is enlarged.",
    ], GIOCOMO, [
        "The larger box reveals the knockout grid pattern.",
        ["Main box.", "Mice explored a 100 × 100 cm box.", "The extent showed repeated fields."],
        ["Small box.", "A 50 × 50 cm box was used in extra sessions.", "It supported boundary and head-direction measures."],
        ["Control.", "Arena size sets how much pattern is sampled.", "Enlarged spacing needs a large box."],
        ["Meaning.", "The grid comparison rests on the larger box.", "Periodicity is visible when enough fields are sampled."],
    ], ["Giocomo 2011"]),
    ins(33, "HCN1 knockout scales the whole grid", [
        "HCN1 knockout enlarged both grid spacing and the size of individual fields. These measurements distinguish the distance between repeated peaks from the extent of each elevated firing region.",
        "The spacing-to-field-size ratio was about 3.26 in controls and 3.32 after knockout. The near-identical ratios show that the whole pattern expanded together.",
        "A proportionately enlarged grid is a coarser metric pattern. The experiment measured spatial firing during exploration, a quantity that is separate from navigational accuracy or memory.",
    ], GIOCOMO, [
        "HCN1 knockout scales the whole grid.",
        ["Measures.", "Spacing and field size were both measured.", "Peak distance differs from field extent."],
        ["Ratio.", "The spacing-to-field-size ratio was about 3.3.", "It matched across genotypes."],
        ["Scale.", "The whole pattern expanded together.", "The grid became coarser."],
        ["Meaning.", "The measure is spatial firing during exploration.", "Navigation requires its own test."],
    ], ["Giocomo 2011"]),
    ins(36, "Theta timing and spacing move together", [
        "Giocomo and colleagues compared spike-time autocorrelations of grid cells in control and knockout mice. Theta-related peaks mark the recurring timing of firing in each cell.",
        "The typical interval between peaks was 108.1 ms in controls and 114.4 ms in knockout grid cells. Wider spatial spacing therefore came with a slower recurring timescale of firing.",
        "A temporal autocorrelation measures how spikes recur at different lags, which is different from the physical spacing of fields. The shared shift in timing and spacing narrows the set of mechanisms that could explain the knockout.",
    ], GIOCOMO, [
        "Theta timing and spacing move together.",
        ["Method.", "Spike-time autocorrelations were compared.", "Control and knockout mice were used."],
        ["Interval.", "Peaks were spaced 108.1 ms in controls.", "They were 114.4 ms in knockouts."],
        ["Link.", "Wider spacing accompanied slower timing.", "The two shifts occurred together."],
        ["Meaning.", "Timing and spacing constrain mechanisms.", "Both shift in the same cells."],
    ], ["Giocomo 2011"]),
    ins(39, "Interneurons keep their timing", [
        "An interneuron is a neuron whose principal connections stay within a local circuit. Giocomo and colleagues compared theta-modulated entorhinal interneurons with the principal grid cells.",
        "The increase in theta timing was present in grid cells but was not comparably detected in simultaneously recorded interneurons. The change therefore concerns grid cells specifically, rather than every recorded neuron.",
        "Cell-class differences constrain how a molecular intervention reshapes network dynamics. The selective effect points to specific cell classes, which makes a targeted physiological change in those classes the likely explanation.",
    ], GIOCOMO, [
        "Interneurons keep their timing.",
        ["Cells.", "Interneurons were compared with grid cells.", "Both were theta-modulated."],
        ["Timing.", "The increase appeared in grid cells.", "It was not detected in interneurons."],
        ["Selectivity.", "The effect is specific to a cell class.", "Every neuron was not slowed."],
        ["Meaning.", "The intervention reshapes specific networks.", "Cell classes respond differently."],
    ], ["Giocomo 2011"]),
    ins(42, "Knockout raises within-trial stability", [
        "Spatial stability describes how consistently a neuron fires across repeated portions of a recording. Giocomo and colleagues compared maps from the first and second halves of each trial.",
        "Grid and border patterns were more stable in knockout mice, while directional stability changed much less. Grid spacing was also considered, because broader patterns can look more stable under the same displacement.",
        "A broader field can stay stable while distinguishing positions less sharply. The stability difference therefore describes the consistency of firing, which is a separate property from spatial precision.",
    ], GIOCOMO, [
        "Knockout raises within-trial stability.",
        ["Stability.", "Maps from trial halves were compared.", "Consistency defines stability."],
        ["Result.", "Grid and border maps were more stable.", "Directional stability changed less."],
        ["Spacing.", "Broader patterns look more stable.", "Spacing was accounted for."],
        ["Meaning.", "Consistency differs from precision.", "The result is about firing, not navigation."],
    ], ["Giocomo 2011"]),
]

for _k, _ps in _ext.EXTEND.items():
    for _p, _t in _ps.items():
        _body.body[_k][_p - 1] = _body.body[_k][_p - 1] + _t
for _ins in inserts:
    for _p, _t in _insx.INSERT_EXTEND.get(_ins["after"], {}).items():
        _ins["paragraphs"][_p - 1] = _ins["paragraphs"][_p - 1] + _t
for _ins in inserts:
    _ins["notes"] = _ins["notes"] + [
        [f"Explanation {_i + 1}.", *(p_.split(". ", 1))] for _i, p_ in enumerate(_ins["paragraphs"])
    ]

spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(_body.body)} body slides rewritten, {len(inserts)} scaffold slides")
