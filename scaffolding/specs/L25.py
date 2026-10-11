"""Scaffold spec for Lecture 25 (Drive deck Neuroethology_Lecture25_FA2026.pptx). Body rewrites are in body_L25.py."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import body_L25 as _body  # noqa: E402


def ins(after, title, paragraphs, citation, refs):
    notes = [title + "."] + [
        [f"Explanation {i + 1}.", *(p.split(". ", 1))] for i, p in enumerate(paragraphs)
    ]
    notes.append(["Source.", f"The figure and measurements come from {citation}."])
    return dict(after=after, title=title, bold=[], paragraphs=paragraphs, citation=citation, notes=notes, refs_from=refs)


inserts = [
    ins(3, "Mussel extract was delivered at a set rate", [
        "Mussel extract was delivered at 0.5 g/L and 50 mL/min from a source 9 cm above the bottom of the arena. Control trials kept the same delivery conditions but replaced the extract with raw seawater, which sets the baseline for every extract condition. The control differs from its extract trial in chemical content alone.",
        "A reference grid and overhead video allowed position and heading to be measured in each walk. The rostrum, the animal's anterior projection, served as the positional landmark. Its position was digitized once per second, giving a common spatial and temporal reference for all trials. Heading was measured from the same digitized positions. All walks were scored on the same grid.",
        "Turbulent dilution and the animal's own movement mean the concentration at a receptor is not read directly from the source solution. The source concentration differs from the fluctuating concentration reaching the animal downstream. Odor arrives as intermittent pulses rather than as a steady field, so walking animals meet a fluctuating signal. Walking animals sample a fluctuating signal rather than a steady gradient.",
    ], "Moore et al. (1991)", ["Moore 1991"]),
    ins(6, "Raking events per 5 s by distance band", [
        "Raking averaged 3.4 events per 5 s within 7 cm of the source and 2.6 events per 5 s at 7 to 15 cm. Those two distance bands contained the highest raking rates in the recorded approaches. The 7-cm band marks the closest distance at which raking was scored. Raking was counted in each band separately.",
        "Between 15 and 22 cm, the average fell to 1.15 events per 5 s, a value that sits between the nearer bands and the far one. Beyond 22 cm it averaged 0.1 per 5 s, a rate near zero relative to the source zone. Rates are averages of counts taken within each distance band.",
        "The distance bands were 0 to 7 cm, 7 to 15 cm, 15 to 22 cm and beyond 22 cm. The figure omits raking frequency, so its trajectories alone are not a direct readout of leg-receptor activity. The bands are fixed ranges from the source rather than single lobster positions. These bands are the same for every recorded approach.",
    ], "Moore et al. (1991)", ["Moore 1991"]),
    ins(9, "Success rates by odor and sensory treatment", [
        "Intact lobsters reached the high-odor source in 68% of trials, versus 45% for the weaker odor. No intact animal located a seawater source, which fixes the reference point for the experiment. These intact values serve as the reference for every lesion condition in the flume. Intact animals reached the high-odor source more often than the low-odor source.",
        "After aesthetasc removal, success was 77% for high odor and 69% for low odor, both above the intact values. Removing non-aesthetasc sensilla gave 64% for high odor, four points below the intact animals, and 45% for low odor, matching the intact result. Those percentages come from the same flume trials. Those values are proportions of trials.",
        "Preserved success after one pathway is removed argues against that pathway's unique necessity for the task. Odor concentration changed success in every treatment, with high odor giving the higher percentage. Both pathways carried useful information for the weak odor. Non-aesthetasc removal left the low-odor result equal to the intact value. Low-odor trials were the more demanding test in each treatment.",
    ], "Horner et al. (2004)", ["Horner 2004"]),
    ins(12, "Virtual sampler flicks and plume geometry", [
        "The lobster sampler flicked at 2 Hz and moved at 6 cm/s during the downstroke, so two downstrokes occurred every second. The crab sampler flicked at 3 Hz, which made its flicks occur more often than the lobster's. Both geometries were compared at the same 8-cm height above the bed. Lobster geometry was the larger of the two sampling structures.",
        "A virtual sampler is an analysis of physical measurements, not a recording of a receptor neuron. Its purpose is to isolate which aspects of the input depend on appendage size and motion. Flick rate and sampler speed are fixed inputs in each calculation, and both samplers used the same plume records. Flick counts per second differ by one.",
        "The calculated output is an estimate of odor encounters per flick. That estimate follows from the measured plume images and the sampling assumptions specified in the analysis. Its values describe the physical input to a sampler of that shape, not a neuron's response. The estimate is an analysis output, not a measured animal response.",
    ], "Reidenbach & Koehl (2011)", ["Reidenbach 2011"]),
    ins(15, "Aesthetasc dimensions set the array scale", [
        "Representative aesthetasc diameter was 22 µm, length about 720 µm and spacing about 60 µm. These dimensions were measured on the lateral flagellum of Panulirus before any physical model was built. The model reproduces these scales at a larger size in mineral oil, which keeps the scale of each hair in proportion. Those dimensions define the scale of the array.",
        "An outer dendrite is the distal sensory portion of a neuron extending into the hair. Membrane receptors sit on those dendrites and respond to molecules that reach them. The hair's cuticle and fluid environment lie on the path between transported chemicals and the neuronal membrane. Odor molecules must reach that membrane before any receptor can respond.",
        "Microscopy establishes dimensions and arrangement, not channel opening or neural firing. The 60 µm spacing is the gap width that water passes through in the model. The 22 µm diameter sets the width of each hair in the same model, which keeps the proportions of the living array. The hair width sets the scale for the water flow analyzed in the model.",
    ], "Reidenbach et al. (2008)", ["Reidenbach 2008"]),
    ins(18, "Diffusion spans about 32 µm in 0.5 s", [
        "Diffusion is random molecular motion that redistributes solute down local concentration differences. Retaining water increases the contact time available for molecules to reach the membrane, but not every retained molecule reaches it. That contact time is set by the slow return rather than by the downstroke. Diffusion acts within the retained water near each hair.",
        "The authors estimated that diffusion over 0.5 s could span about 32 µm. That figure is a length scale for the retained sample at the aesthetasc surfaces during the return, not the distance traveled by any particular molecule. The calculation uses a simple diffusion estimate over that time window. The estimate covers the return interval alone.",
        "The estimate is a physical calculation, not a measured uptake of ligand by neurons. Transport in the retained sample is one stage in a sequence, and receptor binding is the stage that follows it. The sequence begins with a physical stage before the molecular stage. Receptor binding follows once solute reaches the membrane. Its timing follows the flick.",
    ], "Reidenbach et al. (2008)", ["Reidenbach 2008"]),
    ins(21, "Dye parcels were about 1 mm thick", [
        "Each dye parcel was about 1 mm thick when it crossed the array. In the same preparation, the benthic dye source sat 1 m upstream of the antennule. A horizontal streak in the published map means concentration at one position remained similar over time. Parcel size and source distance were both taken from the video frames.",
        "Tracking the same dye feature across frames distinguishes exchange with the plume from simple movement of the appendage. The image sequence contains successive frames from the original recording rather than a drawn diagram. Each frame sequence captures one flick cycle from start to finish. Those video frames were recorded during successive flicks of the antennule.",
        "The original high-speed frames record each stage of a flick, from the rapid downstroke through the slower return. The parcels leave the array during the next downstroke. A sustained spike train or a labeled sensory axon is not what this map shows. Those parcels can be followed from frame to frame in each sequence. Parcels were captured in one downstroke each.",
    ], "Koehl et al. (2001)", ["Koehl 2001"]),
    ins(24, "Deorphanization links a ligand to a receptor", [
        "Deorphanization means identifying the ligand that activates a receptor without an identified ligand. Calcium imaging supplies a candidate list one cell at a time, and that list is then tested with the receptor protein itself. Responses were scored cell by cell across the stimulus panel. The dye turns calcium changes into fluorescence intensity. Calcium responses differed between cells that sat side by side.",
        "IR25a appeared in cell somata and inner dendrites in the fluorescent row of the published immunolabeling figure. The protein occurs in both the cell body and the inner dendrites, which places it in the cells whose responses were imaged. A control image accompanied the labeled row. The control labeling marks background staining. Labeling in that row shows bright somata and dendritic profiles.",
        "A response to arginine in an intact cell identifies a candidate responder rather than the receptor protein. Expression and localization together narrow the candidates before any functional test, and ligand binding, ion selectivity and subunit composition each need their own measurement. Sequence data alone identify candidates only. Functional tests are run in defined cell types.",
    ], "Corey et al. (2013)", ["Corey 2013"]),
    ins(27, "G proteins couple receptors to enzymes", [
        "A G protein links some activated receptors to intracellular enzymes or channels. That coupling is a second-messenger route, which differs from ligand-gated channels that open directly when a ligand binds. Enzymes activated this way change messenger levels before any ionic current flows. The intracellular cascade sets the timing of the response. Its second messengers are inside the cell.",
        "Ligand-gated channels are described by their ion permeation rather than by second-messenger steps. Ionic current through the channel is the readout of activation, so the identity of the ions carried matters for the response. Current direction depends on the ions carried through that channel. GPCRs can regulate intracellular signaling, so they act through a different route.",
        "Molecular presence indicates that a pathway could exist, but causal function must be tested rather than assigned from a protein-family name. Expression data identify candidate genes, which functional tests then assign to odor responses. A transcript for a GPCR or TRP channel needs a functional test before it is linked to odor. Each candidate receptor then needs its own ligand test.",
    ], "Kozma et al. (2020)", ["Kozma 2020"]),
    ins(30, "Calcium follows spikes with a delay", [
        "Calcium can enter a neuron through voltage-dependent channels, and it can also be released from intracellular stores. The fluorescence reflects calcium from either source, so a single optical trace combines both contributions. Calcium-sensitive dye reports these changes through its fluorescence intensity. The calcium signal is slower than the electrical event that causes it. The calcium rise follows the stimulus with a delay.",
        "A broad calcium peak has its own duration, which differs from both the odor pulse and the spike burst that produced it. Dye kinetics stretch the signal in time, so the peak lasts longer than the electrical event it follows. Peak timing comes from that neuron's optical trace. Those effects were measured in identified neurons.",
        "Excitation increased firing and then accumulated a calcium signal, while an inhibitory optical response accompanied reduced firing. Bobkov and colleagues recorded both signals together, so the two time courses come from the same cells. The optical peak occurs after the spike burst that drives it. Spike timing and fluorescence answer different questions. Spikes alone resolve the timing of individual events.",
    ], "Bobkov et al. (2012)", ["Bobkov 2012"]),
    ins(33, "cGMP analog mimics proline's outward current", [
        "Phosphodiesterases normally break down cyclic nucleotides. Blocking them raises intracellular levels of these messengers, so the inhibitor works as a pathway probe rather than an odor-specific receptor ligand. Opening a potassium conductance can shift voltage toward the potassium equilibrium potential. The behavioral meaning of that shift depends on which sensory neuron is inhibited in each case.",
        "The cyclic-GMP analog produced an outward current matching the one proline evoked in this cell class. The same outward response appeared with phosphodiesterase inhibition, so three distinct manipulations converged on one current. IBMX raised cyclic-nucleotide levels by blocking their breakdown. The response class was defined by proline inhibition. Responses were recorded as outward currents.",
        "Drug actions and analog selectivity need a check against cells that lack the proline-inhibitory phenotype. Cells that respond to food extract but lack proline-driven inhibition form the contrasting group. Analog selectivity is tested by comparing these cells with the proline-excited class. Those cells test whether the outward current is specific to the inhibited class. The proline-excited class supplies that comparison.",
    ], "Michel & Ache (1992)", ["Michel 1992"]),
    ins(36, "Messenger levels at 100 µM", [
        "At 100 µM, taurine produced a peak IP3 near 630 pmol/mg and a cAMP peak near 280 pmol/mg. Those values were measured in the same isolated dendritic membranes as the low-dose traces, so the two concentrations can be read side by side. The higher-dose values come from a separate figure, not an extrapolation. The low-dose traces show preference rather than total messenger output.",
        "Proline produced a cAMP peak near 720 pmol/mg and an IP3 peak near 220 pmol/mg at the same concentration. Its cAMP response was larger than its IP3 response, which reverses the ordering seen for taurine at this dose. The two ligands kept their preferences at this dose as well. Both messengers were measured for each ligand.",
        "Picomoles per milligram normalize the measured messenger quantity to membrane protein rather than to one neuron. The pooled measurement describes membrane material rather than any single cell type. Membrane protein is the normalization unit used in these measurements. The values describe group-level messenger levels. Values are group-level, summarizing the whole preparation in each sample.",
    ], "Boekhoff et al. (1994)", ["Boekhoff 1994"]),
    ins(39, "2,000 synthetic neurons estimate intervals", [
        "The synthetic population contained 2,000 neurons, which the authors combined to estimate event timing. The estimate used population output rather than the activity of any single neuron. Each synthetic cell carried its own intrinsic period. The population was then decoded as one signal. Each cell's period was set in the oscillator model. Those periods differed across the population.",
        "The estimated intervals included inputs at 10, 12, 35, 40 and 43 s, spanning both brief and long gaps between events. Combining cells whose intrinsic periods differ improved the estimate for each interval in the sequence. Each interval estimate used the same decoder, applied across the whole population. The estimates were checked against the true input intervals.",
        "A computationally available signal is not automatically read out by the animal. The model motivates a behavioral prediction, and its idealized decoder sets the scope of that prediction. The 2,000 neurons were synthetic, not simultaneously recorded from real animals. A behavioral test would be needed to link this code to searching. Its predictions can be tested in live animals.",
    ], "Park et al. (2014)", ["Park 2014"]),
    ins(42, "Picrotoxin and cimetidine dissociate actions", [
        "Picrotoxin at 100 µM blocked the GABA effect, whereas histamine inhibition persisted. The GABA-receptor blocker left the histamine response in place in the same nerve preparation. Histamine inhibition remained after GABA receptor blockade. Responses were measured from afferent voltage signals. Picrotoxin left histamine inhibition intact in the same nerve. The effect was read from voltage signals in afferents.",
        "Cimetidine at 5 mM reduced the histamine effect without producing the same blockade of GABA. The two drugs separated the inhibitory actions by receptor type. The cimetidine result complements the picrotoxin result. Together the two drugs show that GABA and histamine act through separate receptor types. Its effect was measured against control responses in the same nerve.",
        "Histamine used as a central transmitter must be distinguished from histamine delivered as an odorant to sensory dendrites. The site of application determines which role is being tested, and the recorded response identifies the pathway. The two roles are distinct experimental questions. Odorant histamine reaches sensory dendrites, whereas transmitter histamine acts within the nerve. The two roles are separate experimental questions.",
    ], "Wachowiak & Cohen (1999)", ["Wachowiak 1999"]),
]

spec = {"third_paragraph": {}, "inserts": inserts, "body": _body.body}

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{out}: {len(_body.body)} body slides rewritten, {len(inserts)} scaffold slides")
