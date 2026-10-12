"""Lengthening sentences for the Lecture 21 inserts (L21.py). INSERT_EXTEND[after][paragraph] is appended after a space."""

INSERT_EXTEND = {
    3: {3: "The frames follow the successive discharges emitted during the approach."},
    6: {
        1: "The rewarded size was the stable reference across trials.",
        2: "Image intensity and image width were the two candidate cues for size.",
        3: "The learned preference still held when each cube's distance changed relative to the gates.",
    },
    9: {
        1: "This ratio is the quantity that changes during each approach.",
        2: "The recorded discharge timing supplied the sampling record for every approach.",
        3: "The approach geometry was measured as well as the electric samples.",
    },
    12: {1: "The ratio thus discounts the overall scale of the signal.", 2: "Each cube size yielded its own sampling profile.", 3: "Relative gradients give the same distance information across the cube sizes tested. The absolute amplitude, by contrast, carries size information that tracks object size rather than distance."},
    15: {
        1: "The paper defined that criterion for the reconstructed cues.",
        2: "Both cues were judged over the same range of simulated distances.",
        3: "The two ranges were measured in different experiments, so the two numbers answer different questions.",
    },
    18: {1: "Accuracy stayed at or above 84% in each group despite the different sensory inputs.", 2: "The electric route alone supported accurate choices at close range.", 3: "Placement at the gates was identical across the three groups and in every test session."},
    21: {
        1: "The latency is measured from stimulus onset, so it reflects the timing of a single neuron's response. Each recording reflects one afferent's timing.",
        2: "The pulses were controlled, so the same stimulus could be repeated for each amplitude and interval.",
        3: "Latency adds a second dimension to the afferent response, beyond how many spikes were fired.",
    },
    24: {
        1: "The replay kept the sequence of natural pulses intact across each trial. Fixed-rate pulses lack the variability of that sequence.",
        2: "The amplitude input was constant across the replayed intervals, which isolated the interval effect. Latency was read on every replayed pulse.",
        3: "Sampling history is a property of the animal's own sensing, since the animal generates the intervals. Every sequence was run through the same afferents.",
    },
    27: {
        1: "The added term changes gain with the previous intervals, not with the present amplitude alone.",
        2: "Prediction failures were examined separately for each interval pattern. The fits were checked against the recorded latencies.",
        3: "Such models summarize the afferent's input-output relation in a form that can be tested on new sequences.",
    },
    30: {
        1: "Their contributions were separated by drug application. The NMDA and AMPA receptors are distinguished by their antagonists, which were applied in separate tests.",
        2: "The reversibility argument rests on recovery after washout in the same tissue. Recovery confirmed the reversibility of that effect.",
        3: "The field response combines these contributions and gives no count of receptors per synapse. Their pharmacology identifies the contributing receptors.",
    },
    33: {
        1: "Facilitation was tested across that whole range. Pulse spacing was the variable that changed across the pairs.",
        2: "Facilitation depends on which fibers are recruited as well as on the interval. The two cases differ in which fibers respond to the second pulse.",
        3: "Its time course follows the spacing of the paired stimuli, which is why the interval is the key variable.",
    },
    36: {
        1: "Their current-evoked firing was recorded for each cell type. Those recordings sampled cells of different types within one slice.",
        2: "The balance was tested for each pathway and cell in these recordings. The stimulated pathway determined which influence dominated.",
        3: "Circuit position determines whether a local signal reaches the output neurons. Behavior-level interpretation requires intact animal experiments.",
    },
    39: {
        1: "Their timing relative to the command can be compared on a shared reference. Both event classes were examined in each recording.",
        2: "Their relative timing was tracked across cycles. Their relation to the command cycle was examined phase by phase.",
        3: "The narrow spike carries the immediate output, and the broad spike feeds back on synaptic strength. Both events remain distinguishable in the same recording.",
    },
    42: {
        1: "The recordings examined the cycles that followed each stimulation episode. Command-linked recordings were analyzed in the cycles immediately after stimulation ended.",
        2: "Switching off the stimulus changed the timing of B spikes within the early cycles. This change in early timing is what the transient increase consists of.",
        3: "The circuit state built during stimulation provides one explanation for the rise. Each candidate mechanism predicts a different time course for the transient.",
    },
}
