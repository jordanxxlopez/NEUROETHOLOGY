"""Body-text rewrites for Lecture 27 (scaffolding/RULES.md)."""

body = {
    4: [
        "For the released flies, horizontal landing distance increased with initial horizontal velocity. Rossel and colleagues compared measured distances at 20- and 40-cm release heights with the ballistic predictions. The measured distances matched those predictions under these conditions, which means air resistance and initial vertical velocity contributed little to the trajectory.",
        "The same horizontal speed produces a more distant landing point when the release height is greater, because the object stays airborne longer. A fish must therefore combine motion information with height information to locate the destination across both heights.",
        "The ballistic relation links the landing point to release height and initial horizontal velocity, the two variables that a fish needs to combine. Predicting the landing point from these two inputs lets the fish start its response before the prey reaches the water.",
    ],
    6: [
        "Rossel and colleagues measured where the fish's final heading intersected the prey's projected horizontal path. Errors relative to the future water-entry point were centered near zero at both tested heights, across the naturally occurring range of horizontal take-off speeds, so the turns aimed at the point where the prey would enter the water.",
        "Errors relative to the prey's position at turn completion showed a systematic offset instead. The fish had already aimed ahead of that position, so the response anticipates the landing point. This within-trial comparison used the same responses for both measures, so the offset reflects the aim itself.",
        "The result supports prediction of the landing destination before impact. The initial heading is set before later swimming corrections occur, so the initial aim itself carries the prediction. Aiming at the future water-entry point, and not at the current prey position, is the defining feature of a **predictive start**.",
    ],
    8: [
        "Rossel and colleagues placed prey on a transparent horizontal glass screen at 20 or 40 cm height. Air from a blast pipe moved the object horizontally at speeds within the natural take-off range. The target therefore moved without descending toward the water, so the fish saw horizontal motion with no fall.",
        "Fish nevertheless turned toward the **virtual landing point**, the destination at which prey with that initial height and horizontal velocity would have entered the water if allowed to fall. Errors relative to this virtual point were centered near zero at both heights.",
        "The fish's turn therefore depends on a computed relation among initial height, speed and direction, rather than on the visible horizontal path alone. The horizontal screen supplies the speed and direction inputs without the fall, and the fish still outputs the landing point.",
    ],
    28: [
        "Reichenthal and colleagues fitted models that combined the recovered temporal filters through **nonlinear response functions**. A nonlinearity means that the response combines the filter outputs non-additively, so the joint values of the filters can change how strongly the neuron fires.",
        "The original examples included one-, two- and three-filter descriptions with different response surfaces. Two-filter models reproduced response structure that an average-based single filter missed. The authors compared model output with recorded firing rates, so each model is tested against the measured responses.",
        "These are phenomenological models, compact descriptions of measured input–output relationships. The diverse combinations provide candidate transformations of visual timing before a motor decision, and each combination specifies a distinct response surface.",
    ],
    33: [
        "Machnik and colleagues obtained intracellular recordings from identified archerfish **Mauthner cells**. Mean resting voltage was −79.5 mV, antidromic spike onset latency was 0.265 ms, and the somatically recorded spike had a half-maximal duration of 0.54 ms.",
        "The apparently small somatic spike, about 36.7 mV, must be read together with the extracellular field around the cell. Subtracting the nearby external potential reconstructs the actual membrane-voltage change, so the corrected signal reflects the cell's own voltage.",
        "These recordings remained stable for approximately 2–3 hours, permitting repeated sensory and inhibitory tests within one cell. A spike onset latency of 0.265 ms and a half-maximal duration of 0.54 ms mark a **rapidly conducting output neuron** that signals fast.",
    ],
    39: [
        "Volotsky and colleagues trained Toxotes chatareus to shoot at an aerial target and introduced horizontal airflow above the water. The air deflected the jet while the fish remained in the water, creating an aiming error without moving the visible target itself.",
        "The experiment compared baseline shots, a perturbation period and shots after the airflow was removed. Errors initially increased when the airflow began and then declined over successive shots. Trials in both airflow directions showed that the adjustment applies to either direction of physical deflection.",
        "**Motor adaptation** is the adjustment of a movement in response to systematic errors caused by changed conditions. The measured correction shows flexible calibration of the shooting action, and the declining errors over successive shots show that the fish recalibrates each shot using the outcome of earlier shots.",
    ],
}
insert_body = {
    5: [
        "**Heading** is the direction in which the body axis points at a given moment. A bystander's initial heading can differ greatly from the direction in which a dislodged fly moves, so the angle of the required turn changes from trial to trial.",
        "Rossel and colleagues sampled this angular relation at both 20- and 40-cm prey heights, including orientations that required large turns before acceleration toward the destination. The fish occupied different positions and orientations in the tank, so the same destination was reached from many starting headings.",
        "The turn needed to reach the destination depends on the heading at the moment of the response. A fixed turn angle would succeed from only one starting orientation, so the responder converts prey-motion information into a turn measured from its own body axis.",
    ],
}
