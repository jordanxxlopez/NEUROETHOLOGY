"""Paragraph overrides for Lecture 35 (scaffolding/RULES.md). Applied by L35.py."""

# third paragraph of original slides, keyed by slide number
BODY_P3 = {
    24: "Recordings from each animal span the whole pairing period, so the time course is traced in individual animals.",
    30: "The product is measured in the cells that express the receptor, so the readout reflects that receptor's signaling alone.",
    32: "The cGMP analogue was tested at 100 µM, so its failure to slow habituation was measured at a concentration above the cAMP analogue's.",
    33: "The inhibitor was applied in every preparation before the drug, so the same order was used throughout.",
    42: "Each neuron's response is shown with its own voltage calibration, so the sizes of the changes can be read directly.",
    43: "Each animal's maze behavior comes from its own test session, so the boundary retreats belong to the individual animal.",
    5: "Dominant animals kept attacking and approaching throughout the 30 min, while the subordinates' retreats accumulated across the same periods. Counts taken in 5 min periods show the rise in retreat as it happens, rather than as a total at the end of the encounter.",
    6: "The effect was measured within each pair, so the treated subordinate's own saline period sets the baseline. Estimated serotonin near 10 µM was reached during the infusion, and the fights that followed were longer and more intense than the saline fights.",
    10: "Thresholds rose in subordinates during contests and fell again after the encounter ended, which shows that the change depends on the interaction. Dominants showed a smaller change, so the size of the threshold shift tracks rank. Electrode placement and stimulus recruitment were held constant across the periods.",
    14: "Rectifying contacts transmit more strongly in one direction, so the membrane voltage of the receiving cell changes how much of an input is passed on. A depolarized LG therefore passes a smaller share of each sensory signal than a hyperpolarized one.",
    16: "Serotonin reduced LG responses to repeated stimuli delivered every 15 s, and the later stimuli failed to fire LG at all. Washout restored firing in the same preparation, so the inhibition is reversible and tied to the drug's presence. The source recordings keep mV and ms calibration.",
    17: "Octopamine enhanced the later β component more than the early α component, so the change falls mainly on the later part of the excitation. Stimuli that were subthreshold before octopamine could trigger spikes during perfusion, and the facilitation of the later component is separable from the early response.",
    18: "Serotonin concentration, onset rate and exposure duration each change the outcome, so the sign of the effect follows from the whole schedule rather than the dose alone. Juvenile bath concentrations and adult arterial concentrations also differed, and that difference alone changes the dose that reaches the nerve.",
    19: "Slow onset over 20–30 min favored facilitation even at the high concentration, while rapid onset produced inhibition. The timing of exposure is therefore part of the drug's dose, and the same concentration can produce either sign depending on how quickly it arrives.",
    21: "Stimulus-response curves show the threshold for firing at each shock strength. In isolates and dominants the curve moved toward lower thresholds, while in established subordinates it moved toward higher thresholds. The same stimulus strengths were used in every animal.",
    22: "Higher input resistance allows a given current produce a larger voltage change, so the increase in isolates and dominants makes the same synaptic input more effective. The reduced resistance in subordinates has the opposite effect on the same input.",
    23: "New subordinates kept serotonergic facilitation for the first week, then became inhibitory in the second. Renewed isolation for eight days restored facilitation, so the subordinate response reverses once social conditions change.",
    24: "The newly dominant animal's response followed its new role over about two weeks. The inhibitory response from its earlier subordination persisted during that time, so the change came gradually rather than as a single switch.",
    27: "Preabsorption of the antibody with its target peptide reduced the specific labeling, which identifies the staining pattern as antibody-specific. The labeling was then examined across the abdominal ganglia, and the pattern followed the segmental organization of each ganglion.",
    30: "Serotonin is the most potent ligand among those tested. Receptor-expressing cells respond to it at the concentration reported above, which makes inositol-phosphate production a specific readout of this receptor.",
    32: "The cAMP analogue slowed habituation, while the cGMP analogue did not, so the effect follows cAMP rather than cyclic nucleotides in general. The control curve declined faster than the cAMP-treated curve in each preparation.",
    33: "Cyclase inhibition shifted the median back toward control values, so the block removed a large share of the facilitation. The inhibitor alone left the initial shock threshold unchanged.",
    34: "The analogue, delivered inside the cell, produced a clear increase in both early and late EPSPs. The carrier-only electrode did not produce the change, so the increase is attributed to the analogue itself.",
    35: "Facilitation came mostly from the synaptic responses, not from a shift in the resting voltage of LG. Cyclase inhibition removed most of both increases, so the enhancement runs through cAMP synthesis, and washout partly restored the original response.",
    36: "The brief exposure gave an inhibition that reversed quickly, while the 45 min exposure gave facilitation that remained after the drug was gone. The time the drug is present therefore determines which sign the response shows afterward.",
    38: "Tactile input to the anterior abdomen produced turning in isolates and dominants and pushing backward in subordinates, so the same touch drives different motor programs. Depressor activity over the first 0.6 s followed the behavior in the same animal.",
    39: "The status pattern survives removal of the anterior centers, so it is generated by the local ganglionic circuit. Electrical stimulation of an abdominal sensory nerve produced the pattern without any descending input, and each isolated ganglion carries its animal's social history.",
    40: "Serotonergic cells in isolates and dominants responded differently to ipsilateral and contralateral touch, and subordinate cells responded more symmetrically. The shift toward symmetric responses matches the change in walking-leg organization, so one cell type carries the status effect.",
    41: "A single serotonin neuron can therefore excite some motor units while inhibiting others within one nerve. Averaged nerve recordings would miss this split, so the motor units were followed individually and each was measured against its own baseline.",
    42: "The depressor neurons' resistance changed in the same direction as their EPSPs, so the synaptic and membrane changes reinforce each other. The sensory input was delivered by a controlled movement of the proprioceptor.",
    43: "The winner and loser effects were measured on the day after a single contest, which tests recent experience against a long-term change in fighting ability. Each win rate is set beside the naive control group that matches its size class.",
    7: "Treated subordinates kept fighting for longer than controls, and most of the extra time came from persistence rather than from a change in who started the encounter. The original opponent usually still won the contest, so the drug lengthened fights without reversing rank.",
    29: "Forskolin raises cAMP by activating adenylyl cyclase, so a receptor that reduces forskolin-stimulated cAMP acts on that pathway from the inhibitory side. The cloned receptor therefore lowers cAMP when it is activated, which places it on the opposite side of the cAMP route from the facilitation described earlier.",
    34: "The analogue raised EPSP amplitude while the carrier-only electrode did not, so the enhancement comes from the analogue rather than from the injection current. The analogue also depolarized LG by about 5.4 mV, a separate effect that the same neuron shows during injection.",
    37: "The labeled terminals lie around the septate junction, where successive segmental giant axons meet, so the contact sits at a defined point along the LG axon. Similar labeling appears near the proximal parts of the terminal-ganglion LG neurons.",
    44: "Fluoxetine blocks serotonin uptake, so a drug that raises serotonin can strengthen or weaken the same social effect depending on when it is given. Acute treatment in one protocol and treatment after dominance in the other produced opposite changes in winning.",
    45: "Losers that endured more attacks avoided light more strongly, so the number of attacks predicted avoidance better than fight duration did. Methysergide increased time in the light arms in subsequent losers and reduced their boundary retreats, so serotonin signaling contributes to the avoidance.",
}

# third paragraph of insert slides, keyed by the original slide each insert follows
INSERT_P3 = {
    6: "Estimated circulating serotonin approached 10 µM during the infusion. The saline baseline and the infusion period belong to the same pairs, so every fight is measured against its own pair. Fight duration and intensity rose during the 60 min infusion.",
    18: "The antagonist cinanserin reduced connective-induced facilitation while leaving repeated-stimulation depression intact. This pattern points to a serotonergic route to facilitation that runs alongside the depression. Facilitation and depression therefore have separable causes.",
    21: "The stimulus strength needed to fire LG is set by the animal's social history. Isolates and dominants fired at lower shock strengths after serotonin, while established subordinates needed stronger shocks, so the same drug moves the threshold in opposite directions.",
    27: "Puncta around the cell bodies mark where the receptor protein sits in the cytoplasm of each labeled cell. Nuclear counterstain marks where each cell body lies, and serotonin labeling in the same sections marks the source of the transmitter.",
    30: "Matched non-transfected cells gave no receptor-associated response, so the inositol-phosphate signal depends on the expressed receptor. Other monoamines needed much higher concentrations or had little activity, which places serotonin at the top of the potency order.",
    36: "Longer exposure produced persistent facilitation, which remained above baseline during the 30 min wash and could persist for hours. Brief exposure reversed quickly, so the two exposure lengths give distinct washout profiles.",
    24: "The shift toward facilitation took about two weeks, which places the change on the timescale of the new social role. Former subordinates carried their inhibitory serotonin response into the new rank before the facilitatory response replaced it. Dominants made from isolates had facilitation from the start, so the earlier history set the starting point.",
    33: "Adenylyl cyclase is the enzyme that makes cAMP, so blocking it removes the substrate that cAMP-dependent facilitation needs. In these preparations, the block removed most of the extra resistance to habituation that serotonin produces, and the remaining resistance was small.",
    42: "Changes in the average nerve activity can conceal these opposing effects, so each motor unit has to be followed on its own. The units were recorded individually in each preparation, which keeps the excited and inhibited responses distinct within one nerve.",
}

# second paragraph of insert slides
INSERT_P2 = {
    24: "These former subordinates were set against new dominants generated from isolates. Isolates began with a facilitatory response, so the two groups start from different points before the promotion takes effect.",
    33: "With serotonin alone, the median stimulus number before habituation was 12.5, whereas controls had a median of 3. With cyclase inhibition and serotonin together, the median fell to 6, and later response loss approached the control pattern.",
}

# sentences appended to paragraphs that were still short: (original slide or insert-after, paragraph)
APPEND_BODY = {
    (24, 3): " The rank change set the timing, and the inhibitory response was still present when the new role began.",
    (30, 3): " Two receptor types can be compared on the same readout, so the cAMP and inositol-phosphate pathways are kept apart.",
    (32, 3): " The cGMP result is judged against the cAMP-treated curve from the same preparation.",
    (33, 3): " The median values are reported for each group, so the size of the effect is visible without the individual traces.",
    (42, 3): " The proprioceptor input is kept constant, so the EPSP change can be attributed to the motor neuron's own state.",
    (43, 3): " Win and loss rates are reported for the same number of contests in each group.",
}
APPEND_INS = {
    (24, 2): " The promotion results and the naive-animal results are recorded in the same way.",
    (36, 3): " The two exposure lengths therefore predict different outcomes at the next day's test.",
    (18, 1): " Each drug is applied under the same protocol, so each effect is measured under identical conditions.",
    (30, 1): " The receptor sequence and the expression system are identified before any signaling is measured.",
}
