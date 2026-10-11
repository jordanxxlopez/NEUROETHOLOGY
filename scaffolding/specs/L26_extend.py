"""Lengthening sentences for the Lecture 26 body rewrites (body_L26.py), so each paragraph runs 52-62 words."""

# (slide, paragraph) -> sentence appended to that paragraph
EXTEND = {
    2: {2: " The scored contacts form the basis of the ray-use record."},
    3: {3: " Each brief touch is therefore a sampling event."},
    4: {2: " Each later contact moves the item closer to those rays.",
        3: " Its function therefore resembles fixation."},
    5: {2: " Every trial uses the same endpoints.",
        3: " The sequence ends when the star resumes searching."},
    6: {3: " The timing values come from separate sets of measurements."},
    7: {1: " The curves are shown as the authors modeled them.",
        3: " A small fragment can therefore be worth handling."},
    8: {1: " Coverage is distinct from receptor density.",
        3: " Eastern moles therefore set the baseline for this analysis."},
    9: {1: " Dental anatomy was therefore examined in the same study as the sensory surface.",
        3: " Both appear in the same high-speed sequences, which ties sensing to grasping."},
    10: {2: " Their repeated arrangement makes the star's surface a measurable sheet of sensory units."},
    11: {1: " Each organ therefore shows its own spatial arrangement.",
         3: " The arrangement shows structure, not function."},
    12: {2: " These sections were paired with the dye labeling.",
         3: " Positions and shapes of the complex are reported in the same figures."},
    13: {1: " Its layers are visible under dye labeling.",
         2: " One corpuscle per organ was the illustrated case.",
         3: " These deeper components sit beneath the epidermis of each organ."},
    14: {3: " The two labeling patterns therefore point to different candidate functions."},
    15: {1: " Organs were traced individually.",
         3: " Counting these profiles requires knowing which fiber each belongs to. Dye tracing supplies that information."},
    16: {1: " Thin sections make each bundle visible.",
         3: " Each count is therefore a measure of afferent allocation for its ray."},
    17: {1: " The measure is expressed per organ.",
         3: " Dome counts and fiber counts therefore answer different questions."},
    18: {1: " Each recorded position is therefore a point on the surface, not a depth.",
         3: " Distal sampling is finer than basal sampling."},
    19: {1: " This control makes the ray-by-ray measure fair.",
         3: " Each one can be measured on its own."},
    20: {1: " Its value is an area, not a count.",
         2: " Smaller organs therefore dominate the distal tips.",
         3: " The map gives the force-filtering idea a testable form."},
    21: {1: " Each unit's firing is therefore judged against a fixed stimulus.",
         2: " All three patterns were recorded in the same trigeminal preparation.",
         3: " Holding and changing contact are coded separately."},
    22: {1: " Frequency and amplitude were varied together.",
         3: " The classes differ in their preferred inputs, not in their presence."},
    23: {1: " Ramp stimuli reach the same displacement at every speed.",
         2: " Both slow and fast ramps were included in the series.",
         3: " Each unit's preferred velocity is part of its response profile."},
    24: {1: " Peripherin labels a population of small neurons.",
         2: " The two markers reveal different proportions in each ganglion.",
         3: " The ganglion differences are population-level findings, so each one needs a cell-level test. Each population could be tested in turn."},
    25: {1: " Cells from each tissue were tested under identical conditions.",
         2: " The DRG fraction is therefore less than half the TG fraction.",
         3: " Cell-level calcium responses are a functional readout."},
    26: {1: " Every agonist was tested on the same cell cultures.",
         2: " These responses show which stimuli each ganglion favors.",
         3: " The facial ganglion therefore leans toward mechanical responses."},
    27: {1: " Many transcripts were measured in each ganglion.",
         2: " Reads that failed one reference went on to the next.",
         3: " Shared differences can be set aside before the mole-specific ones are examined."},
    28: {2: " The enrichment pattern is therefore uneven across the candidate list.",
         3: " Each candidate needs a test in its own cell type."},
    29: {1: " The qPCR step is an independent check of the screen.",
         3: " Expression evidence and functional evidence are therefore reported separately."},
    30: {1: " The next check was whether the protein itself appears in mole ganglia. This check moves the evidence from RNA to protein.",
         3: " Protein localization is one level of the system, and the RNA screen is another."},
    31: {1: " Detection in mouse tissue is a practical route to later tests.",
         3: " Gene presence alone leaves function to be tested. Species differences therefore need to be measured."},
    32: {1: " The two species differ in nasal receptor surfaces, which makes the pairing informative.",
         2: " The expanded nucleus is therefore a feature of the star's anatomy.",
         3: " The central expansion is measured at the first brainstem relay. Its subdivisions are visible in the same stained material."},
    33: {1: " A map of this kind organizes the nucleus by ray identity. Each module's position reflects its ray.",
         2: " The nose's arrangement is mirrored in the relay.",
         3: " Electrophysiology therefore gives the map its functional meaning. Each module is tested with stimulation of its ray."},
    34: {2: " The paired record therefore links each recorded site to a ray.",
         3: " Each recording site was therefore assigned by both methods. The lesion marks and the sections together fix each site."},
    35: {1: " The measurements cover each stage of the pathway. Each stage contributes a different proportion of the star.",
         3: " Ray 11 is the reference point for each stage."},
    36: {1: " Flattened cortex therefore gives a single map of the rays.",
         3: " Its area can be read against the innervation counts for that ray."},
    37: {1: " The denominator is the count of myelinated fibers.",
         3: " The excess also varies with the stage at which it is measured. Cortical magnification is therefore stage-dependent."},
    38: {1: " Each field is therefore a measured boundary, not an anatomical one.",
         3: " Field size therefore reflects both anatomy and the recording criteria."},
    39: {2: " Stimuli were applied to the same mapped unit. Each response was measured against baseline spontaneous activity.",
         3: " The measurement ties the response to the stimulus onset."},
    40: {3: " The response code therefore carries timing information."},
    41: {3: " Center–surround organization therefore operates within a single cortical map. The organization is a spatial code, not a transmitter code."},
    42: {1: " The approach reveals the shape of the boundary.",
         2: " Its center and surround therefore both belong to one neuron. A single neuron can carry both effects.",
         3: " Spatial structure is measured in each field separately. Each field's shape can be defined separately."},
    43: {1: " The response classes are defined by their timing.",
         3: " Such duration coding is measured from the same receptive fields. The same fields therefore carry both transient and sustained signals."},
    44: {2: " Each stage is defined by the crest pattern visible at that length.",
         3: " The ordering is developmental rather than chronological. Embryo length serves as the stage marker."},
    45: {1: " The DiI labeling records where each nerve runs.",
         3: " The receptor surface and its nerves therefore develop together."},
}


# second tier: paragraphs that were still short or at the lower edge after the first tier
EXTEND2 = {
    10: {1: " The map is continuous across the front surface."},
    17: {3: " Both counts are needed."},
    19: {1: " Matching positions remove the effect of position along the ray.",
         3: " These factors are separate in the analysis."},
    21: {2: " The three types are distinct."},
    22: {2: " Both ranges were measured at several amplitudes."},
    23: {2: " Speeds below that value were also tested."},
    28: {1: " These proteins are ion channels or their regulators."},
    29: {2: " Each value is normalized to the same reference."},
    30: {2: " Both observations come from the same tissue sections."},
    31: {2: " Both tissues were examined for each candidate."},
    35: {3: " Each ratio is a share of its own total."},
    36: {2: " These pinwheel sets are visible in one cortical sheet.",
         3: " Stripe boundaries are defined by staining rather than by cell type."},
    38: {2: " The fields are reported as areas in square millimeters."},
    39: {1: " Each stimulus duration was delivered through that probe."},
    40: {1: " Both responses are timed relative to the stimulus transition."},
    41: {1: " Simultaneous recordings place both units in the same stimulus sequence.",
         2: " Each example involves one excited and one suppressed neuron.",
         3: " The spatial pattern is a cortical property."},
    42: {1: " Each step is defined by a measured position."},
    43: {1: " Each class is defined by its firing across the stimulus.",
         2: " Transient and sustained neurons are distinguished by their response pattern."},
    44: {1: " The rays first appear as epidermal structures."},
    45: {2: " The nerve arrangement changes with each growth stage.",
         3: " The early nerve pattern precedes the free appendage."},
}


def apply(body):
    for table in (EXTEND, EXTEND2):
        for slide, paras in table.items():
            for para, text in paras.items():
                body[slide][para - 1] = body[slide][para - 1] + text
    return body


# third tier: shorter wording where a slide's text had to fit a column with a figure beside it
TRIM = [
    (8, 2, "The two factors multiply, so a large contact area and a high rate both raise the chance of meeting prey.", "Both factors together raise the chance of meeting prey in one encounter."),
    (8, 3, "Eastern moles therefore set the baseline for this analysis.", "Eastern moles set the baseline."),
    (14, 2, "The two studies agree that the outer ring differs from the central cluster.", "The two studies agree on the outer ring."),
    (14, 3, "The two labeling patterns therefore point to different candidate functions.", "The two patterns point to different candidate functions."),
    (21, 1, "Each unit's firing is therefore judged against a fixed stimulus.", "Firing is judged against a fixed stimulus."),
    (21, 2, "All three patterns were recorded in the same trigeminal preparation.", "All three patterns came from one preparation."),
    (22, 2, "Each class therefore has its own tuning range.", "Each class has its own range."),
    (28, 1, "These proteins are ion channels or their regulators.", "They are channels or regulators."),
    (31, 3, "Species differences therefore need to be measured.", "Species differences need measuring."),
    (32, 1, "The two species differ in nasal receptor surfaces, which makes the pairing informative.", "The species differ in nasal receptor surfaces."),
    (32, 3, "Its subdivisions are visible in the same stained material.", "Its subdivisions are visible in these sections."),
    (41, 1, "Simultaneous recordings place both units in the same stimulus sequence.", "Both units were recorded in one sequence."),
    (43, 1, " The response classes are defined by their timing.", ""),
    (43, 3, "The same fields therefore carry both transient and sustained signals.", "The same fields carry both signal types."),
]


def apply_trim(body):
    for slide, para, old, new in TRIM:
        text = body[slide][para - 1]
        assert text.count(old) == 1, (slide, para, old[:40])
        body[slide][para - 1] = text.replace(old, new)
    return body


# fourth tier: one sentence removed from a paragraph so the slide fits its column at 14 pt (six lines)
TRIM += [
    (41, 1, " Both units were recorded in one sequence.", ""),
]

# fifth tier: one paragraph per slide shortened to six lines (the column holds about twenty lines)
TRIM += [
    (21, 1, "each recorded unit under the same mechanical event.", "each unit under the same event."),
    (22, 3, "The classes differ in their preferred inputs, not in their presence.", "The classes differ in their preferred inputs."),
    (32, 3, "The central expansion is measured at the first brainstem relay.", "This relay is the first stage."),
]
