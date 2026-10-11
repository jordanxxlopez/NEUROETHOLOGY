"""Scaffold spec for Lecture 27 (Drive deck Neuroethology_Lecture27_FA2026.pptx). Body rewrites are in body_L27.py, lengthening in L27_extend.py."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L27 as _body  # noqa: E402
import L27_extend as _ext  # noqa: E402


def ins(after, title, paragraphs, citation, refs):
    notes = [title + "."] + [
        [f"Explanation {i + 1}.", *(p.split(". ", 1))] for i, p in enumerate(paragraphs)
    ] + [["Source.", f"The figure and the measurements come from {citation}.", "Each statement is tied to the recordings or observations of that study."]]
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


inserts = [
    ins(3, "Perspective correction fixes the error reference", [
        "Overhead video shows a falling prey at positions that shift with its height, because camera perspective changes as the object descends. Rossel and colleagues corrected that perspective for the prey's changing height before any error was scored. The correction treated the water surface as the reference plane, so each landing estimate was read in one physical frame.",
        "Without that correction, the image position of a falling prey would drift as the object fell, and errors would be scored against a moving reference. Destinations for the 20 and 40 cm release heights were therefore placed on the same error scale, which makes the two heights directly comparable.",
        "Overhead video sampled prey and fish positions at 20-ms intervals. Temporal resolution sets the precision assigned to each individual response latency, so every latency value is an estimate tied to that frame interval. Latencies are therefore reported as estimates at the resolution of that frame interval.",
    ], "Rossel et al. (2002)", ["Rossel 2002"]),
    ins(6, "Within-trial errors isolate the early aim", [
        "Both error measures came from the same responses within each trial. Because one group of fish and one stimulus history supplied both measures, the contrast between the two errors is free of differences between animal groups or stimulus histories. The within-trial design keeps the aim measure tied to a single set of turns.",
        "Prediction could operate through an explicit internal trajectory or through a learned relation between sensory variables and the destination. Measured errors identify where the fish aimed, whereas the internal computation behind that aim is a separate question. The data therefore constrain the output of the computation without naming its form.",
        "Eventual catches alone would be weaker evidence, because the initial heading exists before later corrections take effect. Subsequent swimming corrections change the path after the fact, so the early heading is the record that reflects the fish's estimate before the outcome is known.",
    ], "Rossel et al. (2002)", ["Rossel 2002"]),
    ins(9, "Kinematics describe the movement, not its commands", [
        "The silhouette sequence is the authors' published high-speed record, with stage colors and measured center-of-mass markers that follow the body through both stages. Predictive starts were filmed from above, so the silhouettes show the turn in the horizontal plane. Each silhouette is an original frame from the recording rather than a drawing.",
        "A kinematic record specifies the form and timing of a start. Identifying the descending neurons that initiate the maneuver calls for separate measurements, because the movement itself carries no label for its source. Experiments that record or stimulate the command pathway provide evidence that the body record alone lacks.",
        "The two-stage sequence repeats across starts, so the bending stage serves as a consistent marker of when the turn is being set. Each start was resolved frame by frame at 2-ms intervals, which keeps the stage boundaries explicit in the analysis.",
    ], "Wöhl & Schuster (2007)", ["Wöhl 2007"]),
    ins(12, "Bending predicts turns, not commands", [
        "The original relation compares the required turn angle with the extent of body bending, so each start contributes a paired measurement of the two. Those pairs spanned the whole range of turns in the recordings. Each pair links one observed start to the turn it needed to complete.",
        "Correlations among body measurements show which features vary together, while the order in which the nervous system specifies those features is a separate question. A correlation can rank features by how tightly they track each other without revealing which one is set first. Establishing that order requires experiments that manipulate the features directly.",
        "A kinematic predictor is useful because it links a measurable body shape to the turn the fish is about to complete. That link gives experimenters a quantity they can measure in every start before the turn is finished. Measuring the bending stage therefore offers an early readout of the turn's final angle.",
    ], "Wöhl & Schuster (2007)", ["Wöhl 2007"]),
    ins(15, "Rare misses expose the jet beyond its target", [
        "Missed short-range targets supplied the uninterrupted jets needed for this comparison. The shaft comparison therefore used jets that reached the common 30-cm path without being interrupted by a target. Each jet was examined at the same travel distance, which made the shaft shape directly comparable across intended ranges.",
        "Because every shaft was examined after the same travel distance, differences in shaft shape reflect the intended range rather than a difference in path length. The design therefore reads the same measurement across all three target heights. Shaft modulation is a property of the emitted water itself, observed after release.",
        "Each shot contributes one shaft image tied to one intended range, which gives a direct record of the jet's coherence at that range. Those records were gathered for the same set of shooting heights used in the focusing images.",
    ], "Gerullis & Schuster (2014)", ["Gerullis 2014"]),
    ins(18, "Measured fluid properties match control water", [
        "Shot viscosity was 0.867 mPa·s, against 0.869 mPa·s for control water. Surface tension was 70.37 mN/m for the shot water and 70.49 mN/m for the control, so the two fluids were nearly identical in both measures. The shot water was collected directly from the fish's own shots, so the values describe the fluid the fish actually emitted.",
        "The fluid properties were measured for shots aimed at several target heights. Neither viscosity nor surface tension changed systematically with the intended range, which fits a fixed fluid composition across the shots. Chemical tuning of the jet would have required one of these properties to vary with range.",
        "Mouth-tip drift and body rotation were measured during the same emission period, and neither changed systematically with target height. Those movements were small enough that the water release itself carried the range difference. The jet's range was therefore set inside the mouth rather than by the fish's body position.",
    ], "Gerullis & Schuster (2014)", ["Gerullis 2014"]),
    ins(21, "Receptor curves keep their original scales", [
        "The regional spectra are drawn from curves that keep their original axes and relative sensitivity scales. Each curve shows how absorption changes with wavelength in one selected photoreceptor, so the shapes can be compared across retinal locations. The published figure keeps every curve in its original form.",
        "The retina's two regions view different parts of the environment, and the spectral curves show how each region samples light from them. The aquatic and aerial views therefore carry different light conditions into the eye, and each region's spectrum reflects the light it receives.",
        "Spectral coverage is a property of the receptors themselves, so it sets which wavelengths are available for detecting a target against the sky. Spectral and spatial measures are therefore reported separately for each retinal region, so each region's capabilities can be read on its own terms.",
    ], "Temple et al. (2010)", ["Temple 2010"]),
    ins(24, "Relative timing references the population, not the motor act", [
        "Relative latencies are referenced to the onset of the recorded population response, not to the animal's motor response. The reference therefore belongs to the retinal recording itself, which is distinct from when the fish decides to move. This reference makes the timing measure depend on the recorded responses alone.",
        "The four decoding analyses were the authors' own original analysis of the same recorded responses. Each ranking of decoders is therefore a comparison made on one dataset rather than on separate experiments. A shared dataset makes the difference between decoders a difference in method rather than in the animals sampled.",
        "A spike-count estimate integrates activity over a longer period, so a short first-spike window can carry information that a count over a longer window would average out. The first-spike analysis uses that early timing directly. Its advantage lies in using the earliest spikes that the cell produces after onset.",
    ], "Kretschmer et al. (2012)", ["Kretschmer 2012"]),
    ins(27, "Analytical filters describe the response model", [
        "The published eigenvectors belong to an analytical response model, which describes how the neuron responds to light history. They are not a reconstructed anatomical circuit, so each filter stands for a computation rather than a wiring diagram. Each eigenvector is a weighting over the preceding light levels, read off the fitted model.",
        "Reichenthal and colleagues used full-field flashes, so every filter describes responses to a whole-field light history rather than to a spatial pattern. The temporal analysis therefore complements the earlier receptive-field maps. Spatial and temporal structure were measured with separate stimulus sets, so each dimension could be analyzed separately.",
        "The filters are estimated from the stimuli presented and the amount of recorded activity, so their precision follows the data collected. Larger recordings would give the same analysis more samples to estimate each filter. Filter estimates therefore improve as the recorded activity grows.",
    ], "Reichenthal et al. (2018)", ["Reichenthal 2018"]),
    ins(30, "The axon cap shapes the field signal", [
        "The focused extracellular signal depends on the geometry of the axon cap around the cell, which shapes where the field is strongest. That geometry means the signal reports the cell's local field rather than an average over the hindbrain. Field recordings near the cell therefore identify a particular neuron's signal.",
        "Antidromic stimulation travels backward from axon toward cell body, so it activates the cell by way of its axon. That route is distinct from the forward flow of sensory input through the dendrites. Stimulation of this kind is an experimental probe rather than a description of natural input.",
        "Antidromic activation shows that the cell can be driven from its axon, a property separate from its firing during a natural prey-directed turn. Experimental access to that axon is what makes the cell testable in the first place. The identified cell then serves as a platform for the sensory tests that follow.",
    ], "Machnik et al. (2018a)", ["Machnik 2018a"]),
    ins(33, "The distant reference carries the spike field", [
        "The distant reference can itself carry the local spike-associated field, which is why the external potential has to be corrected before the membrane voltage is determined. The correction turns a reference reading into an estimate of the cell's own voltage. Without it, the spike seen at a distant electrode would mix the cell's voltage with the surrounding field.",
        "Each intracellular spike was checked against the field recorded around the cell, so the reported spike amplitude belongs to the cell rather than to its surroundings. This isolates the cell's own voltage change from the surrounding potential. The distinction matters for every amplitude value reported for these neurons.",
        "Stable recordings allowed the same cell to be tested with repeated stimulation over the course of an experiment. Because the excitability measures come from one identified neuron, each response can be judged within that cell. Repeated tests in one cell make paired comparisons possible.",
    ], "Machnik et al. (2018b)", ["Machnik 2018b"]),
    ins(36, "Two dendritic sites bracket the lateral dendrite", [
        "Recordings were made about 50 and 150 µm lateral to the axon hillock, giving a proximal and a distal site on the same lateral dendrite. The two positions bracket the region where the sensory inputs were compared. Passive spread is the common basis for interpreting both positions.",
        "The gradient interpretation relies on passive decay measured independently, so the spread of each input is set by the cell's own passive properties. That independent measurement anchors the reading of the two gradients. A reading of that kind depends on knowing the passive decay before the inputs are interpreted.",
        "Anatomical tracing of each presynaptic axon is a separate task from measuring these gradients. Gradient measurements locate the likely entry region of an input, while tracing identifies the axon that carries it. The two approaches answer different questions about the same synapse.",
    ], "Machnik et al. (2018b)", ["Machnik 2018b"]),
    ins(39, "Airflow acts on the aerial stream, not the target", [
        "Airflow acted on the aerial water stream, while the target location remained under experimental control. The airflow therefore changed the jet's path without changing where the visible target sat. Errors came from the stream itself, which is why the setup isolates the deflection of the jet.",
        "The published setup includes a photographed water jet, which documents the stream that the airflow deflects. That image anchors the stream geometry that the blower acted on. The photographed jet is the physical object whose deflection the fish corrected across the session.",
        "Adjustment was tested in both directions, so the correction could be checked for whether it worked for either direction of deflection. Each direction was run as its own condition in the same session. Those conditions show whether the fish's adjustment worked on one side or on both.",
    ], "Volotsky et al. (2023)", ["Volotsky 2023"]),
    ins(42, "Virtual prey separate the rule from the feeder", [
        "The virtual task keeps an objective predicted landing point while letting the investigators change the motion-to-reward relation. That arrangement allows the reward to follow a rule that a physical falling prey could not supply.",
        "Latency and accuracy were reported together across the training sequence, so the speed of the predictive start and its correctness both show how the learned rule developed. The two measures tracked each other as training progressed. Together they show the rule emerging without a change in the response's speed.",
        "Rapid decisions persisted while the learned rule changed, which places the plasticity inside the speed constraint of the start. The change therefore affects which destination is chosen without slowing the response into a deliberate approach. The learned rule thus operates within the same fast motor program.",
    ], "Krause et al. (2024)", ["Krause 2024"]),
]

# insert paragraphs: lengthening sentences (kept with the inserts they belong to)
INS_EXT = {
    3: {2: " Each landing estimate kept its meaning at either height.", 3: " The sampling rate therefore sets how precisely any turn onset can be dated."},
    6: {1: " Each trial supplied both values.", 2: " Each interpretation predicts a different pattern across trials.", 3: " A fish with a learned relation would show the same early aim across repeated trials of one stimulus."},
    9: {1: " Those markers track each stage in order.", 2: " Such experiments can separate the two possibilities directly.", 3: " Stage boundaries defined this way give every start a shared timing reference for analysis."},
    12: {1: " The relation therefore tracks turn size against bending extent.", 2: " Such a ranking is descriptive.", 3: " Its value is in timing."},
    15: {1: " This design kept travel distance constant across the jets.", 2: " Shaft shape therefore carries the range information.", 3: " The shaft records therefore complement the focusing images collected for the same heights, giving two views of one shot."},
    18: {2: " The fish's emission was sampled at each height.", 3: " Mouth measures are therefore central to the range question."},
    21: {1: " Each spectrum therefore has its own scale and baseline.", 2: " The curves therefore reflect the light each region receives. Each region's sensitivity is measured directly.", 3: " A region with broad coverage can respond to more contrasts than a narrow one."},
    24: {1: " That choice keeps the analysis focused on the responses themselves.", 2: " The shared dataset keeps every ranking on equal footing.", 3: " That choice favors the earliest information in each response."},
    27: {1: " The fitted model defines each weighting directly.", 2: " Each dimension therefore has its own measurement basis.", 3: " Estimates from short recordings carry more variability than those from long ones."},
    30: {1: " The cell's geometry therefore shapes each recording.", 2: " Its route bypasses the dendritic inputs that carry natural sensory signals.", 3: " That identification makes the cell a usable target."},
    33: {2: " Each spike amplitude was therefore corrected before analysis.", 3: " Each recording therefore yields several measures from a single neuron. That reuse is a practical advantage of the preparation."},
    36: {1: " Both sites sit on the same dendrite, so they share one geometry.", 2: " Passive decay sets how far a voltage change spreads along the dendrite.", 3: " Tracing would name the carrying axon directly, something gradient measures alone never supply."},
    39: {1: " The stream itself was the object of the deflection in every trial.", 2: " The photograph therefore links the apparatus to the jet that the fish aimed, which helps interpret the errors.", 3: " Both airflow directions were therefore run in every session."},
    42: {1: " The prediction stays fixed while the reward moves, which isolates the learning from the physical scene. This setup gives the experimenter direct control of reward timing and location.", 2: " Both measures are summarized across the same trials.", 3: " The speed of the response was preserved throughout training."},
}
for _k, _ps in INS_EXT.items():
    for _ins in inserts:
        if _ins["after"] == _k:
            for _p, _t in _ps.items():
                _ins["paragraphs"][_p - 1] = _ins["paragraphs"][_p - 1] + _t
            _ins["notes"] = [_ins["title"] + "."] + [
                [f"Explanation {i + 1}.", *(q.split(". ", 1))] for i, q in enumerate(_ins["paragraphs"])
            ] + [["Source.", f"The figure and the measurements come from {_ins['citation']}.", "Each statement is tied to the recordings or observations of that study."]]

for _k, _ps in _ext.EXTEND.items():
    for _p, _t in _ps.items():
        if _t:
            _body.body[_k][_p - 1] = _body.body[_k][_p - 1] + _t

spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(_body.body)} body slides rewritten, {len(inserts)} scaffold slides")
