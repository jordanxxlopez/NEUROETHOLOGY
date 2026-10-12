"""Scaffold spec for Lecture 16 (Drive deck Neuroethology_Lecture16_FA2026_NEW.pptx). Body rewrites are in body_L16.py."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L16 as _body  # noqa: E402


def ins(after, title, paragraphs, citation, refs):
    notes = [title + "."] + [
        [f"Explanation {i + 1}.", *(p.split(". ", 1))] for i, p in enumerate(paragraphs)
    ] + [["Source.", f"The figure and the measurements come from {citation}.", "Each statement is tied to the recordings or observations of that study."]]
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


inserts = [
    ins(3, "CF and FM name parts of one call", [
        "The recordings came from two settings. In one, a bat called while it stayed in place. In the other, the bat flew toward a landing grid, and its calls were recorded through that approach. The two settings give calls from the same species under different conditions. Comparing them shows how calls change when the bat approaches a landing target.",
        "During the final approach, the sustained CF part remained present. Over the same stretch, the calls became shorter and the higher harmonics became weaker. The steady tone stayed in place while the rest of the call changed around it. Its frequency stayed within a narrow range throughout the approach. The shrinking calls still carried that same carrier.",
        "The CF and FM labels name acoustic components of one call, not two separate calls. Each call holds both parts. The steady tone near 65 to 66 kHz lies above the range of human hearing, so people hear none of it. The brief sweep at the end takes up a small share of the call.",
    ], "Schoeppler et al. (2018)", ["Schoeppler 2018"]),
    ins(6, "Playback and flight shifts can act differently", [
        "A natural Doppler shift and an electronic shift can affect a call in different ways. The difference is most visible in the frequency-modulated parts of the call, where the frequency is changing. Flight adds its own Doppler change on top of any echo shift. A playback may not reproduce every feature of a flight echo.",
        "The lowering built up over a short run of calls. The emitted frequency settled at a new level after several calls, rather than jumping in one step. A single prerecorded tone did not produce that pattern. The response unfolded call by call, as each new echo arrived. The bat's later calls moved to a new level as the sequence went on.",
        "Schuller's test kept the bat in one place, so its calls changed without any flight motion. The playback supplied the whole frequency change by itself. That design isolates the effect of the echo from the effect of movement. Movement was held constant across the whole test. In flight, the echo frequency is set by the bat's approach speed.",
    ], "Schuller et al. (1974)", ["Schuller 1974"]),
    ins(9, "The threshold curve came from earlier audiograms", [
        "The threshold curve comes from earlier work. Long and Schnitzler measured behavioral audiograms in the greater horseshoe bat, Rhinolophus ferrumequinum, in 1975. The playback study used that curve as its threshold context, so the audiogram is a reference rather than a new measurement. The study itself measured the response to playback, not the threshold. The threshold curve is an input to the playback design.",
        "A behavioral audiogram is built from the sounds that an animal responds to. Each frequency gets its own threshold. So the curve covers the whole range of playback frequencies that the team tested. Frequencies far from the sensitive band need more sound to reach the same audibility. Hearing sensitivity at a frequency sets how loud a sound must be to be detected.",
        "Playback levels were set relative to each frequency's threshold. A lower-frequency sound needed more intensity to be heard as well as a higher one. Matched levels allow the team to compare shifts on both sides of the resting frequency on fair terms. That gave a fair test of the direction of the shift. That made the sound level a controlled quantity.",
    ], "Metzner et al. (2002); Long & Schnitzler (1975)", ["Metzner 2002", "Long 1975"]),
    ins(12, "Positive steps also recover faster with louder feedback", [
        "The time constant was measured from the vocal trajectory. It tracks progress toward the adjusted call frequency. It describes the whole feedback loop, not the conduction delay of a single neuron. The loop includes the strength of the returning acoustic signal, so loudness enters the measure. The measurements came from each bat's own calls during playback.",
        "For positive steps, the constant dropped from about 1.64 seconds to 0.75 seconds as feedback grew stronger. Positive steps recover faster than negative steps at both reported feedback levels. The shorter values at zero attenuation show the same ordering. Both sets of values come from the same recordings. A negative step moves the echo to a lower frequency than before.",
        "Both directions show faster recovery with stronger echoes. The sign of the step and the loudness of the echo both set the speed of the response. A rule based on direction alone misses the loudness effect. The recovery speed tracks how loud the returning echo is. The bat's control loop, not one neuron, sets that speed.",
    ], "Metzner et al. (2002)", ["Metzner 2002"]),
    ins(15, "Two bat species share one cochlear atlas", [
        "The atlas compares a CF bat with an FM bat. The horseshoe bat is Rhinolophus ferrumequinum, and the FM bat is Myotis pilosus. Both species were studied with the same combined method of sequencing and tissue staining. The shared method makes the two atlases directly comparable. The atlas was built from two bats with different echolocation modes.",
        "Hair cells provide the sensory interface of the cochlea. Supporting cells sit alongside them in the same sensory epithelium. The atlas treats this sensory epithelium as its own group, separate from the spiral ganglion neurons. Each compartment receives its own cell types in the analysis. The FM bat's atlas had 13 types, one fewer than the horseshoe bat.",
        "The stained sections show the layout of the cochlea in both species. Neural tissue and sensory tissue appear as separate regions. Each region can then be matched with its molecular cell types. That step pairs the anatomy with the RNA data from the same tissue. Those cell types were then named by their gene expression.",
    ], "Wang et al. (2025)", ["Wang 2025"]),
    ins(18, "Sensory cells are separated from neurons and wall cells", [
        "Wang and colleagues separated the sensory epithelial populations from the spiral ganglion neurons. They also separated them from the cochlear lateral-wall cells. Each group forms its own population in the atlas. The separate groups make it possible to ask which tissue holds each marker. The sensory group and the neural group carry different marker genes.",
        "The horseshoe-bat atlas has 14 categories in total. Placing a channel marker in that framework shows which tissue expresses it. That places the marker in a tissue context. A tissue context is a different thing from a measured channel, and the atlas supplies just that first step. Each category is a tissue-level grouping of cells, not a single cell.",
        "Gene expression tells the team where a gene is active in the tissue. The channel's gating and its current need separate experiments. Blocking the channel in tissue would be one such experiment. The atlas supplies the tissue location for the candidate, and nothing more. Those are three separate steps, and each needs its own data.",
    ], "Wang et al. (2025)", ["Wang 2025"]),
    ins(21, "One comparison space for two species", [
        "The joint atlas gives a common comparison space for both species. It avoids comparing two unrelated marker lists, one for each species. Both species are measured against the same set of genes. That shared set makes differences in cell types easier to spot. Cells from both species can be placed on one shared map. This makes the atlas a single resource.",
        "The joint map keeps two things in view. One is shared cellular organization. The other is species-specific expression differences. The map shows both without merging them into one pattern. Some clusters hold cells from both species, and others hold cells from a single species. The cluster identities came from expression profiles, not from species labels.",
        "The shared gene list makes the species easier to compare. Call type is one trait among several that separate these two bats. Other traits can add to the expression differences that the joint map shows. The joint map offers a starting list of candidate genes for later tests. The expression comparison is one line of evidence among several.",
    ], "Wang et al. (2025)", ["Wang 2025"]),
    ins(24, "Glia are inferred from molecular matches", [
        "Ligand-receptor inference rests on molecular compatibility. It is not direct observation of signal transmission. The analysis found matching molecules, not a signal that was passed between cells. Matching molecules are a hint, and the hint needs testing. The analysis of expression data produces a candidate list, not a demonstrated pathway. Matches are predicted from the gene lists of the two cell classes.",
        "The study did not stimulate the glia. It also did not measure a resulting response in the SGN membrane. The proposed adhesion and growth signals remain a hypothesis about cell communication. That hypothesis rests on gene expression alone. The proposed signals are candidates that a stimulation experiment could confirm or reject. The study named these signals as a possibility.",
        "A test would stimulate the glia and record the SGNs at the same time. Only that experiment could show whether the proposed signal changes neuron firing. Such a test would need stimulation and recording tools placed in the cochlea. Until then, the glia remain candidates in the atlas. The test would also show the size of any response.",
    ], "Wang et al. (2025)", ["Wang 2025"]),
    ins(27, "A late response may come from the cochlea", [
        "The acoustic envelope sets when the sound is delivered. The cochlear envelope sets how the peripheral response develops. Near resonance, the two envelopes differed from each other. That difference can make a late neural response appear after the sound has stopped. The rise time of a sound is one part of its envelope. Near resonance, the cochlear build-up is slow.",
        "A neural response after a tone can begin without any central rebound. The loudspeaker goes silent, but the cochlea keeps ringing. A late response can come from the cochlea itself. The ringing is a peripheral event that starts before the brain gets involved. A rebound would require a second source of excitation after the loudspeaker stops.",
        "Evidence for a central rebound would need its own recordings from central neurons. The silent loudspeaker alone supplies none of that evidence. Suga's cochlear recordings offer a peripheral explanation that comes first in the chain. The cochlear ringing gives a testable alternative that an experiment can check directly. The rise-time test isolated the effect of the rise itself.",
    ], "Suga et al. (1975)", ["Suga 1975"]),
    ins(30, "Resonance estimates belong to individual bats", [
        "The measurements give each bat its own values rather than one species-wide CF frequency. The resting emission and the resonance estimate come from the same animals. Their gap was measured in each bat, not assumed. Each bat's pair of values is a separate data point. The two values come from one animal, measured at one time.",
        "Neural tuning was judged against each bat's own acoustic and peripheral specialization. Not every midbrain cell near that band feeds the vocal feedback path. Candidate cells can be identified this way, one animal at a time. Macías and colleagues examined sharply tuned neurons near the specialized band. Each bat's neural and acoustic data form one matched set.",
        "The midbrain recordings came from the same bats as the acoustic data. So each neuron's tuning can be set against its owner's resting and resonance values. That pairing gives the team individual-level evidence. Each bat's neural data sit beside its own acoustic data, so the match is within animal. Matched sets make the individual values easier to interpret.",
    ], "Macías et al. (2016)", ["Macías 2016"]),
    ins(33, "Holding the neuron fixed isolates frequency", [
        "Each neuron served as its own control in this design. The team changed the tone frequency and nothing else between the two conditions. Cell identity stayed constant across them. That design removes differences between neurons from the picture. The resting frequency lies just below the resonant band, so the change was small. Changing one value at a time keeps the design clean.",
        "The change in duration tuning must come from the tone frequency, not from a difference between neurons. The same cell gave a sharp duration preference at one frequency and a broad response at another. Cell identity alone fails to explain that contrast. That sharp preference was not present at the lower tone, so the pattern is frequency-specific.",
        "The result shows that tone frequency and central timing processing work together. Identifying the synapses behind this interaction needs other experiments. The recordings already show the effect in single neurons, which makes it concrete. Central processing can filter timing in a frequency-dependent way. The effect depends on the carrier and not on any single fixed duration.",
    ], "Macías et al. (2016)", ["Macías 2016"]),
    ins(36, "The CF area also responds to other signals", [
        "Suga noted that the CF area also responds to signals other than orientation calls and their echoes. The area's specialization describes the typical neuron there. That specialization is not a rule for every neuron in the area. Other neurons respond to a broader set of sounds. The cortex there is organized by frequency, and this area is a large part of it.",
        "Suga's mapping also recorded where along the cortex each neuron sat. Those positions tell the team which frequencies and levels sit next to each other. Neurons at neighboring sites can differ in level preference. The mapping showed how these properties change across the cortical surface. The map ties each site to a best frequency and a best amplitude.",
        "The mapping was done in one species, the mustached bat. Its area of about 2.3 mm2 sets the scale of the map. A later study would need the same kind of mapping in other bats to test whether the pattern holds. The mapping is a single study in one species, so its pattern is a starting point rather than a general rule.",
    ], "Suga (1977)", ["Suga 1977"]),
    ins(39, "Frequency and amplitude maps share one surface", [
        "Tonotopy orders neurons by frequency, and amplitopy orders them by preferred level. Both orderings are spatial, so they can be drawn on the same cortical surface. Suga drew them together for the CF area. The two maps can run in different directions. The amplitude map adds a second organizing principle to the same surface.",
        "The mapping measured neural preference at each cortical site. It was a neural measure, separate from any sampling of the echoes that bats hear in nature. The two kinds of data answer different questions. One measures the neurons, and the other measures the sound. The team recorded at many sites across the area to build the map.",
        "A frequency map and an amplitude map of one area can guide later tests of how the cortex encodes frequency and level together. Those tests would track how one neuron responds across both frequency and level. The map gives them a starting point. That pattern describes the map, not the echoes themselves. Neurons at each site were tested with several sound levels.",
    ], "Suga (1977)", ["Suga 1977"]),
    ins(42, "A precise control system can track a moving band", [
        "The resting frequency was measured just before each flight. The reference frequency was calculated from the echoes of that flight. The two values come from the same time window. Pairing them in time keeps the offset estimate honest. Each flight gives its own pair of values. Both measurements come from the same flight record.",
        "A precise control system can track a preferred state that changes over time. The offset between reference and resting frequency stayed about 80 Hz on average. That stable average shows the offset holds even as both values move. The average offset of about 80 Hz held across the flights studied. Both values moved together across the flights.",
        "Two values measured at one time give a cleaner offset than values from different days. Using a resting value from an earlier session would mix a band shift into the offset. A same-time baseline removes that mix. The same-time baseline is the only fair reference for the offset. The reference offset is then measured in the same session.",
    ], "Schoeppler et al. (2018)", ["Schoeppler 2018"]),
]

spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(_body.body)} body slides rewritten, {len(inserts)} scaffold slides")
