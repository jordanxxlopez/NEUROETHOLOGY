"""Scaffold spec for Lecture 15 (Drive deck Neuroethology_Lecture15_FA2026_NEW.pptx). Body rewrites are in body_L15.py."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L15 as _body  # noqa: E402


def ins(after, title, paragraphs, citation, refs):
    notes = [title + "."] + [
        [f"Explanation {i + 1}.", *(p.split(". ", 1))] for i, p in enumerate(paragraphs)
    ] + [["Source.", f"The figure and the measurements come from {citation}.", "Each statement above comes from that paper's text, its figure legend or the speaker notes."]]
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


inserts = [
    ins(3, "Direction is judged from the moth's path", [
        "A downward movement can count as directional when it carries the moth away from a source above it. A dive can carry a moth away from an overhead speaker, so the path, not the dive, marks direction. Roeder's photographs made each insect's path visible for that judgment. Roeder applied that path-based definition throughout the trials.",
        "Roeder enclosed the camera, which reduced the unwanted ultrasound produced by its shutter. The enclosure removed an artifact that the camera itself introduced. Stationary-flight preparations can restrict turning and may disturb the animal before a test. Roeder instead watched insects that entered the sound field during their own flights. Each trial was judged by the moth's path after onset.",
        "Pooling different maneuvers into one rigid reflex would discard the variation recorded in free flight. Roeder's records keep turning, diving and climbing as separate responses to the same sound. Each response is a different motor solution to the acoustic threat. The records cover responses from weaker and stronger sources. Those responses were measured in natural flight.",
    ], "Roeder (1962)", ["Roeder 1962"]),
    ins(6, "Evasion was scored from the flight itself", [
        "Evasion was scored from the flight itself. A moth could be evasive and still be captured. Keeping movement and outcome apart prevents a circular definition of escape behavior. Surviving the encounter tells nothing about the maneuver itself. The authors recorded capture or escape for every encounter. The authors used infrared video to record each sequence.",
        "Moth species, body form and flight performance also differed between the evasive and non-evasive groups. Those traits could also affect capture, alongside the maneuvers themselves. Successful evasion needs analysis of the maneuver itself, not just the sensory signal behind it. Flight performance was measured from the same reconstructed paths.",
        "The study covered real pursuit and evasion in one outdoor enclosure. The moth assemblage in that enclosure limits how far the results extend to other habitats and predator species. A different set of moths would test that boundary. Each encounter was scored from the recorded path and its outcome. The results apply to this enclosure.",
    ], "Corcoran & Conner (2016)", ["Corcoran 2016"]),
    ins(9, "Sound-driven spikes mark peripheral input", [
        "The nerve had been separated from the central ganglion in the original preparation. Sound-evoked activity arose in the periphery, not from a feedback command sent by the brain. That separation kept central input out of the recording. The sensory side alone was sampled. The preparation kept the nerve's sensory output intact.",
        "The non-acoustic discharge commonly occurred at 5 to 20 spikes per second. Separating that activity from sound-evoked spikes keeps every nerve event from counting as hearing. The regular firing of that unit gave a clear baseline for the sound-driven trains. Only two acoustic units followed the sound in these recordings.",
        "Two acoustic units responded to sound, and the regular unit did not. Their thresholds separated the two responding units in the same nerve. The recorded thresholds identify the cells, not the spike forms. Roeder and Treat recorded both kinds of unit in the same preparation. Their thresholds were distinct even where spike sizes overlapped.",
    ], "Roeder & Treat (1957)", ["Roeder 1957"]),
    ins(12, "Stronger sound reveals dissection effects", [
        "Ter Hofstede and colleagues alternated the order of the two intact orientations between animals. That design reduced an order effect. The inverted preparation placed the moth in a different orientation from flight. Removing muscles and inserting an electrode may have little consistent influence near threshold. Dissection was set against the intact conditions.",
        "The control validates the tested frequency and level range only. Suprathreshold responses and frequency-modulated bat calls were not tested in the same way, so the control leaves those responses untested. Validation applies to the measured range rather than to every stimulus the preparation could receive. The pure-tone conditions set the boundary of that validation.",
        "The same moth served in every condition. Nerve electrodes went into the third condition alone. Each condition was set against the others within one animal. Individual differences stay out of the analysis. Velocity and displacement were both measured at each condition. The conditions for each moth were run in sequence.",
    ], "ter Hofstede et al. (2011)", ["ter Hofstede 2011"]),
    ins(15, "Membrane motion peaks at the attachment", [
        "The female displacement maximum occurred around 90 to 95 kHz. That band lies within the reported male calling range of this species, so the membrane's tuning overlaps the calls it may hear. That tuning peak is a membrane property measured optically. Sound pressure of 90 dB SPL set the level for the membrane readings.",
        "The paper found no reliable sex difference in mechanical tuning. Mechanical sensitivity and neural sensitivity must remain distinct because each describes a different stage of the ear's response. Sensitivity and tuning are separate questions in this experiment. Each stage of the response needs its own measurement.",
        "The membrane measurements were made at 90 dB SPL, so the displacement values describe that sound level. The optical method tracked the membrane surface across the full 50 to 300 kHz range. Displacement was the quantity recorded at each frequency. Each tested frequency gave its own displacement value.",
    ], "Moir et al. (2013)", ["Moir 2013"]),
    ins(18, "Frequency sensitivity without pitch identity", [
        "Gordon and ter Hofstede compared the two cells across frequency using extracellular nerve recordings. Each cell's threshold curve was measured separately, so the two curves can be read side by side. The erebid moths added a second noctuoid family to the data. Both cells were measured at the same frequencies.",
        "Threshold separation between A1 and A2 assigns no distinct behavior to either neuron. The curves describe nerve input rather than an animal's response. Each cell adds its own threshold to the range of sound levels the nerve can signal. Gordon and ter Hofstede separated the cells by their threshold curves. A threshold gap is a property of the recording, not a behavior.",
        "Frequency-dependent sensitivity can exist without an output that identifies sound frequency. That is a property of the nerve's response, not of a pitch judgment made by the moth. Discriminating pitch would need a separate measure from the animal. The result describes the nerve's sensitivity profile in these moths. Gordon and ter Hofstede measured this profile for both cells.",
    ], "Gordon & ter Hofstede (2018)", ["Gordon 2018"]),
    ins(21, "Latency shortens as sound grows stronger", [
        "Roeder measured tympanic responses to brief pulses presented in succession. He stepped the amplitude up in calibrated increments against each preparation's threshold. Responses near threshold were measured at 1 dB increments, which gave fine resolution at the lowest levels. Timing and spike count were measured at each step.",
        "The external onset marker permits this latency measurement. Timing was more variable near threshold, which is when the stimulus is weakest. Some of that delay is axonal conduction from the receptor to the recording site. The delay is reported after that correction. The delay was measured in the same preparations at each level.",
        "Roeder and Treat's section shows the attachment that drives this receptor, a structure in the ear rather than in the brain. A flying moth lacks an external marker and must obtain timing from its own sensory signals. Roeder's latency values came from a single preparation. The section is a published reconstruction, not a live recording.",
    ], "Roeder (1964)", ["Roeder 1964"]),
    ins(24, "Summation and steering are separate questions", [
        "Roeder's matched pulses kept intensity constant across the three ear conditions. The recording coordinates place the units within the thoracic ganglia, where flight control circuits sit. Simultaneous stimulation of both ears was included. Each ear received the same stimulus pattern. The units sat near the midline of the ganglion.",
        "The summating unit responded to both sides rather than to one. A unit's response to both ears leaves the stronger side unidentified. Steering needs side-specific information, and this unit lacks it. Roeder kept the summating response apart from the steering question. The unit's firing was measured in the same recordings.",
        "The proposed steering mechanisms were not resolved by this summating response. Roeder distinguished this summation from the steering mechanism he had hypothesized, and the two ideas answer different questions about the same ganglion. Convergence of auditory inputs is one result, and a directional difference detector is a further one.",
    ], "Roeder (1966)", ["Roeder 1966"]),
    ins(27, "Duration sets the threshold of each cell", [
        "Threshold changes with pulse duration in both cells. In moths the change fits temporal integration, a process that adds up sound energy across the pulse. Pulse duration was the only variable in the tested set. Gordon and ter Hofstede reported threshold differences in decibels. The contrast between the two cells adds the duration effect to that picture.",
        "A1 showed the steeper change of the two cells. A2 thresholds fell more gradually across the durations. A1 is the more sensitive of the two cells at every duration. Heliothis virescens is one of the species in which this pattern was measured. Those thresholds are reported in dB SPL.",
        "Bat calls differ in two cues, duration and level, that the ear must combine. A comparison of bat calls must account for their duration as well as their level at the ear. Duration and level together set which calls a moth can detect. The duration effect is measured at the nerve, not at the moth's behavior. The same measurements covered two moth families.",
    ], "Gordon & ter Hofstede (2018)", ["Gordon 2018"]),
    ins(30, "Interval timing is a second intensity code", [
        "The experiment tested two claims about timing. One asked whether spikes form a burst. The other asked whether spacing inside the burst encodes extra intensity differences. The question was whether timing carries intensity information once spike count saturates. Gordon and ter Hofstede examined both claims in A1 recordings. The two claims were tested in the same recordings.",
        "A reliable short interval can add to central excitation, even when it changes little across the plateau. Those intervals came from the short-pulse condition, where spike count saturated. Roeder's earlier recordings showed that tight bursts differ from isolated spikes. That range is where spike count stayed flat across levels. The plateau is the setting for these interval measures.",
        "Pooled curves can look smoother than any single animal's response. One individual's plateau can occur at a different relative amplitude from another's. Spacing carries timing information that the spike count omits. Each moth's receptor output sets its own plateau. The meaningful event here is the burst itself. Burst spacing and spike count are separate readouts.",
    ], "Gordon & ter Hofstede (2018)", ["Gordon 2018"]),
    ins(33, "Tiger-moth clicks respond to call timing", [
        "The clicking thresholds came from a laboratory playback of pulses with set intervals. Each interval represented a stage of bat echolocation. Playback intensity rose across the tested range. The thresholds came from the same playback design across intervals, with silent gaps between presentations. The first click is the measured endpoint of each playback.",
        "This definition ties the threshold to the defensive output rather than to the sensory response alone. The threshold measures an action, not a receptor. Each click response was checked against the interval it followed. Clicks were scored as the moth's defensive output, not as its hearing. The sensory cells were never tested in isolation.",
        "Rapid terminal timing required sound at higher levels than late approach timing did. Late approach calls at 20 to 30 ms triggered clicking at the lowest sound levels. The clicks themselves are the output that the threshold tracks. Hearing a pulse and emitting a defensive click are different measured events.",
    ], "Corcoran et al. (2013)", ["Corcoran 2013"]),
    ins(36, "Bats raise intensity before a moth clicks", [
        "Corcoran and colleagues measured the bat's call levels over the 250 ms before clicking began. Those levels increased before the click. The claim concerns changes that come before a measured behavioral event. Both changes preceded the defensive output in the recorded encounters. Received level was measured at the moth in each encounter.",
        "The bat's pulse intervals shortened slightly during the same interval. Shorter intervals and rising received intensity together marked the approach that preceded the moth's defense. The timing change was small next to the level change. Both measurements came from the same calls. Received level and interval are measured against the same clicking onset.",
        "The authors proposed that selection favored efficient timing of the bat's calls. Field records alone leave that evolutionary history untested. The first click was the behavioral event used to time these changes. The proposal is a hypothesis about evolution, not a measured result. The proposal explains the timing pattern as a product of selection.",
    ], "Corcoran et al. (2013)", ["Corcoran 2013"]),
    ins(39, "Escape angle and radial acceleration predict outcomes", [
        "The escape angle is different from the moth's initial direction of travel before the evasive turn. The angle was measured after the initial turn, not at the start of the chase. A moth's escape angle is measured relative to the bat's approach direction. The angle is measured in three dimensions along the reconstructed path.",
        "High radial acceleration allows rapid redirection, while the angle sets where that redirection places the moth relative to interception. Radial acceleration is a rate of change of direction. Both values came from one set of reconstructed paths. Successful maneuvers were set against failed ones on this measure. Larger angles marked the captured prey.",
        "The sensory and motor mechanisms that choose the trajectory were not identified. The measured flight paths show which geometries worked. Trajectory choice was not measured directly in these encounters. Escape angle and radial acceleration remain the measured variables of this study. The angle and acceleration describe the maneuver, not the sensory input.",
    ], "Corcoran & Conner (2016)", ["Corcoran 2016"]),
    ins(42, "Tymbal removal raises bat contact rates", [
        "The same moth species was tested with and without the ability to click. That design helped separate sound production from differences among prey species. Each moth type was presented to the same bats. Silent palatable moths were the controls in these trials. The moths in the flight room were the same species used throughout.",
        "Contact was the measured endpoint, which is distinct from consumption or long-term survival. Tethering restricts evasive flight, and organ removal is a physical manipulation. Ablation removed the tymbals from the clicking moths. Contact rates were recorded for each moth type. Each contact was recorded during the attack sequence. Tethered moths were the subjects in the same room.",
        "The experiment shows that sound production matters in this preparation, not every ecological benefit of the species. The bats' contact rates changed with the tymbal, the one variable tested. Tymbal removal altered the contact outcome for the same bats. The intervention is stronger evidence than observing clicks near a missed capture alone.",
    ], "Corcoran et al. (2009)", ["Corcoran 2009"]),
]

for _ins in inserts:
    _ins["notes"] = [_ins["title"] + "."] + [
        [f"Explanation {i + 1}.", *(q.split(". ", 1))] for i, q in enumerate(_ins["paragraphs"])
    ] + [["Source.", f"The figure and the measurements come from {_ins['citation']}.", "Each statement above comes from that paper's text, its figure legend or the speaker notes."]]

spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(_body.body)} body slides rewritten, {len(inserts)} scaffold slides")
