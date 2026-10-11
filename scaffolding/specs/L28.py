"""Scaffold spec for Lecture 28 (Drive deck Neuroethology_Lecture28_FA2026.pptx).

Body rewrites are in body_L28.py. Inserts follow slides 3, 6, 9, ... 42 and teach a source fact
(a method, a measurement or a control) that the body text of the same lecture does not restate.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L28 as _body  # noqa: E402


def ins(after, title, paragraphs, citation, refs):
    notes = [title + "."] + [
        [f"Explanation {i + 1}.", *(p.split(". ", 1))] for i, p in enumerate(paragraphs)
    ]
    notes += [["Source.", f"The figure and the measurements come from {citation}.",
               "Each statement is tied to the recordings or observations of that study."]]
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


inserts = [
    ins(3, 'Displaced foragers reveal a stored outward vector', [
        "Müller and Wehner captured food-carrying ants at the feeding location and released each one in open terrain. Each ant's later course was followed on a 10 m spatial scale. That course was measured against the true geographical direction of the nest and against the course predicted from the ant's recorded outbound trajectory. Its outward walk had been recorded before the ant was captured.",
        'In the two-leg experiments, both legs varied over lengths of 5–10 m and turning angles spanning 0–180°. The plotted experiment used a first leg of 10 m and a second leg of 5 m. Release occurred within one minute of capture, which shortened the time before the directional test. The experiments produced a homing direction for each combination of lengths and angles.',
        'Under natural conditions, landmark guidance and systematic searching remain available as additional mechanisms for locating the nest. Each of these can operate alongside a stored home vector, and neither one replaces the other. Landmark guidance and systematic searching are listed as separate mechanisms, each one an addition to the path integrator.',
    ], 'Müller & Wehner (1988)', ['Müller 1988']),
    ins(6, 'Screening and painting remove two compass inputs', [
        "Screening the sun removed direct solar information from the compass. Ants on this route still erred under the screening. The same two-leg geometry had produced homing errors of about 20° at turning angles near 150° in the earlier test. Screening removed the direct sun's information but left the polarized pattern in place. The polarized skylight pattern was still available to the screened ants.",
        'Painting the dorsal rim of the compound eyes removed access to the specialized polarization-sensitive eye region. Ants with painted eyes also erred on the 10 m and 5 m route, which uses the same two-leg geometry as the screened test. Direct sunlight stayed available to these ants, so the sun cue was not removed.',
        'Restricted sky windows can themselves distort polarization estimates. The authors treated this as a separate source of compass error when they interpreted their homing results, which kept the two sources apart. A narrow channel limits the visible part of the sky, which is one way a sky window becomes restricted.',
    ], 'Müller & Wehner (1988)', ['Müller 1988']),
    ins(9, 'Stilts and stumps alter the distance per stride', [
        'Wittlinger and colleagues trained Cataglyphis fortis to a feeder 10 m from the nest. At the feeder, attached pig bristles lengthened the legs to produce stilts, and shortened legs produced stumps. Food-carrying ants were then tested in a separate channel, after their outward distance had already been learned on normal legs.',
        "The first study of this manipulation appeared in Science in 2006 under the title The Ant Odometer: Stepping on Stilts and Stumps. The later follow-up, published in 2007, added a second level of leg shortening. The 2006 paper's figures show normal legs, stilts and stumps side by side.",
        'The 2007 follow-up tested stumps that differed in which leg region was removed. Its normal-legged group served as the reference for each lengthened and shortened condition. Its figures present the four leg conditions as color-coded search distributions.',
    ], 'Wittlinger et al. (2006)', ['Wittlinger 2006']),
    ins(12, 'Graded shortening tests different leg reductions', [
        'Stumps I lacked the distal tarsal segments, whereas stumps II had the distal half of the tibia removed. The stilt group was lengthened with bristles, and normal-legged ants provided the reference for every group. Those leg changes were made at the feeder, after the outward distance had been learned.',
        'All groups had acquired the same 10 m outbound feeder distance before the first test. The expanded experiment placed the normal-legged group at 10.20 m, the stumps-I group at 6.95 m and the stumps-II group at 5.75 m. The stilted group reached 15.30 m.',
        'The video was recorded at 250 frames per second before and after each manipulation. The recorded strides were used to measure stride length and walking speed. Workers of larger size carry longer legs. The recorded strides supplied the stride frequency used in the analysis.',
    ], 'Wittlinger et al. (2007)', ['Wittlinger 2007']),
    ins(15, 'Search width tracks the stride-determined spread', [
        'The test channel was divided into 10 cm bins before the search data were analyzed. In the first test, the full width at half maximum was 8.3 m for stilts, 6.0 m for normal legs, 5.2 m for stumps I and 4.1 m for stumps II. The search distributions were then plotted for each leg condition.',
        'Stilts had the widest distribution of the four conditions, and stumps II had the narrowest. The four widths follow the same order as the leg treatments that produced them. Search centers for the same conditions were 15.30 m for stilts and 10.20 m for normal legs. The stump-II searches covered the least ground of the four conditions.',
        'Searches in the first test were measured before any matched training, so these widths describe the initial mismatch. Repeated outbound training changed the distributions in the second test. Those widths are full widths at half maximum, reported in meters.',
    ], 'Wittlinger et al. (2007)', ['Wittlinger 2007']),
    ins(18, 'Stride frequency and length measured at 20 Hz', [
        'Stride frequency and stride length are measured separately in the analysis, and either one can change walking speed. Comparing animals at 20 Hz reduced the effect of unequal movement speeds on the predicted homing distances. The analysis used straight runs without abrupt stops. The analysis compared the leg conditions at 20 Hz, which is 20 cycles per second.',
        'Stride length was expressed relative to the alitrunk, a body-size reference. The high-speed records then linked those relative strides with frequency, including the 20 Hz analysis. The curves for stilts, stumps and normal legs were read at matching frequencies.',
        "The stride-length relationship was established independently of the turning-point measures used to locate each ant's nest search. Stilt ants showed longer strides at matched speeds, and stump ants showed shorter ones. Those measures came from freely walking animals. Each leg condition produced its own frequency-length curve.",
    ], 'Wittlinger et al. (2007)', ['Wittlinger 2007']),
    ins(21, 'Accumulated movement signals fit a stride integrator', [
        "The 2007 experiment combined a 10 m navigational task with leg-length manipulations. In that experiment the leg conditions were stilts, stumps and normal legs. The 2007 paper's title describes a stride integrator that accounts for both stride length and walking speed.",
        'Stilted animals searched at 15.30 m after a 10 m outbound journey, while shortened-leg animals searched at 5.75 m. The search centers came from the middle value of the initial six turning points. Both values came from searches after the same 10 m outbound run.',
        'After one more outbound walk, the searches for all four leg conditions converged on the correct 10 m distance. Stride length was plotted against walking speed in millimeters per second, and the kinematic analysis measured both for each animal.',
    ], 'Wittlinger et al. (2007)', ['Wittlinger 2007']),
    ins(24, 'Lateral-complex synapses respond to light exposure', [
        'The whole-brain image in the published figure has a 200 µm scale bar, and the synaptic insets have 10 µm bars. Giant-synapse numbers in the lateral complex rose after three days of exposure to full-spectrum light, with no learning walks required. Both scales appear in the same figure panel.',
        'Removing ultraviolet light lowered that rise. Ants given full-spectrum light without learning walks still showed the increase. Dark controls provided the reference level for each light treatment. The experiment ran for three days before the brains were analyzed.',
        'Central-complex volume did not follow this light-driven pattern. The light treatments were natural skylight, a filter that removed ultraviolet, and a fixed polarization pattern. Lateral-complex synapses sit along the sky-compass pathway in these ants. The lateral complex is a region of the visual pathway that the study counted synapses in.',
    ], 'Grob et al. (2022)', ['Grob 2022']),
    ins(27, 'Learning-walk setup defines the treatment groups', [
        'A table installed 30 cm above the nest entrance held the polarization filter over a 60 × 60 cm learning-walk area. Novices tested around natural nests in Greece experienced their defined skylight condition over three days. Novices performed learning walks around the nest.',
        "A time-compensated compass has to follow the sun's position, which changes through the day. Initial learning can establish the link between those celestial changes and stable surroundings. Each treatment set how often the polarization direction changed.",
        'Across the learning-walk schedules, volume changed in the central complex and in the mushroom-body collar, while giant-synapse counts stayed broadly similar. The continuous rotation condition changed filter orientation at 15° per hour. The natural skylight condition was one of those schedules.',
    ], 'Grob et al. (2022)', ['Grob 2022']),
    ins(30, 'Rotation schedules shape collar and lateral responses', [
        'Each of the three rotating schedules raised collar volume and the microglomerular count. A stationary pattern produced no such growth, and polarized light alone did not produce that growth either. The stationary pattern was the reference condition for the rotating schedules.',
        'Lateral-complex giant synapses changed little across those schedules. Continuous rotation advanced the filter orientation by 15° per hour, a slower step than the hourly 45° turns, and the schedules differed in how fast the pattern rotated over three days.',
        'Learning walks take the ant on short trips around the nest as it moves from indoor work to outdoor foraging. The sky-compass pathway runs through the lateral complex, one of the visual integration centers. Mushroom-body volume responded to the same schedules.',
    ], 'Grob et al. (2022)', ['Grob 2022']),
    ins(33, 'Natural field components set the magnetic conditions', [
        'The coil system was three-dimensional. The natural field measured 46.1 µT in total, and 26.6 µT of that was horizontal. Helmholtz coils set the horizontal and vertical components separately in each condition. The coils set the field in a volume around the learning platform.',
        'With horizontal elimination, the downward vertical field measured about 37.5 µT. The published angular distributions of nest-directed gazes were binned at 10°. The coils surrounded a 60 × 60 cm platform joined to the nest, and novices learned on it for three days. The retained field pointed downward, not horizontally.',
        "Central-complex volume rose in the natural field and in several elimination or disarray conditions over three days. Nest-directed gazes were scored from the longest pirouette pauses in each walk. Under natural conditions, those pauses point toward the nest. Those pauses were scored within each ant's own walk.",
    ], 'Grob et al. (2024)', ['Grob 2024']),
    ins(36, 'Magnetic conditions set collar and microglomerular growth', [
        "The magnetic-plus-solar condition adjusted the horizontal vector every 10 seconds to follow the sun's azimuth across the day. Individual learning walks lasted seconds to minutes, and the reference only had to hold during each walk. During each walk, the sun's azimuth set the direction of the vector. The same magnetic-plus-solar condition kept the look-back behavior intact.",
        'Under total elimination, the residual field was about 0.1 µT, far below the natural value. Complete removal differs from a remaining downward vertical field. The natural field was measured at the same site as the coil platform. The altered conditions were set relative to the natural field measured at this site.',
        'The coils controlled the horizontal and vertical field components separately, while the natural panorama stayed in view. Both collar volume and microglomerular number were corrected for body size. Nest-directed pirouette pauses were the orientation measure in each condition. These two endpoints were measured after the same three-day learning period. Both measures were taken from the same brains.',
    ], 'Grob et al. (2024)', ['Grob 2024']),
    ins(39, 'Ten training journeys set up two feeders', [
        'Ants completed ten training journeys: four to feeder A, four to B and two final journeys to A. Feeder B lay 45° to the left or right of A as viewed from the nest. Each feeder had its own channel leading from the nest during training. The nest-to-feeder channels were separated from the connecting channel.',
        'The subsequent test removed food and opened the connecting test channel at A. At any moment, a single nest-channel entrance was open. Its distances from the nest were 4.5 m to A and 5.7 m to B. The connecting channel was new to the ants. The test then measured where the searches concentrated.',
        "Feeder B was placed on either side of A in separate test arrangements. A shortcut links familiar destinations through a route that the ant never used during training. Feeder B's test arrangements placed it left or right of A in balanced fashion. The left and right placements were both tested.",
    ], 'Voegeli et al. (2025)', ['Voegeli 2025']),
    ins(42, 'Symmetric controls set the baseline for the bias', [
        'Control ants visited feeder A alone before the test. Once food was removed, their searches centered on the old feeder and spread roughly evenly to both sides. Their distribution served as the baseline for the two-feeder searches. Without a second food source in memory, one-feeder controls show the expected search pattern.',
        'About two-thirds of two-feeder ants turned first toward the side where the second feeder sat. The effect appeared whichever side feeder B occupied. Stored goals persist across journeys, while the current vector updates during travel.',
        'Searches were scored as distances in metres from the start along the connecting channel. The first U-turn is an early movement, separate from the later back-and-forth searching. The searches were recorded as density distributions over the channel.',
    ], 'Voegeli et al. (2025)', ['Voegeli 2025']),
]

spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(_body.body)} body slides rewritten, {len(inserts)} scaffold slides")
