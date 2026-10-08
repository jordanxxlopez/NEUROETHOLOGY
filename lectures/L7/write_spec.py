"""Build the source-verified Lecture 7 spec; images are original article crops."""
import json
from pathlib import Path
D = Path(__file__).resolve().parent
S = json.loads((D / 'sources.json').read_text())
# Normalize bibliographic typography without changing article titles.
for v in S.values():
    v['reference'] = v['reference'].replace('<i>', '').replace('</i>', '')
CITE = {'M76':'Marder (1976)', 'M82':'Miller & Selverston (1982)', 'E82':'Eisen & Marder (1982)', 'H87':'Hooper & Marder (1987)', 'S10':'Tang et al. (2010)', 'M19':'Martinez et al. (2019)', 'D18':'Rosenbaum & Marder (2018)', 'S21':'Powell et al. (2021)', 'S15':'Städele et al. (2015)', 'G15':'Garcia et al. (2015)', 'R22':'Schneider et al. (2022)', 'H23':'More-Potdar & Golowasch (2023)', 'G22':'Gorur-Shandilya et al. (2022)'}
FIG={}
def f(name, panel, text):
    k=name.split('_')[0]
    FIG[name]={'path':f'figures/{name}.png','kind':'article','caption':f'{CITE[k]}, Fig. {panel}. {text}', 'source_url':'https://doi.org/'+S[k]['doi']}
f('M82_1','1','Dissected lobster nerves and motor activity with and without input')
f('M82_2','2(A–B)','AB retains slow bursting after other inputs are removed')
f('M82_3','3(A–D)','Isolated PD is tonic; nerve stimulation recruits bursting')
f('M82_4','4(A–C)','Nerve stimulation recruits conditional membrane oscillations')
f('M82_5','5(A–B)','Brief nerve stimulation recruits a reduced pyloric network')
f('E82_2','2(A–B)','Synchronous AB–PD bursts and LP-evoked inhibitory potentials')
f('E82_4','4','Selective deletion separates AB and PD synaptic outputs')
f('E82_5','5','Chloride loading changes the isolated AB-to-LP response')
f('E82_6','6','External potassium shifts the isolated PD-to-LP reversal')
f('E82_9','9','LP-evoked potentials reverse together during PD polarization')
f('M76_2','2(A–B)','Hexamethonium reversibly reduces nerve and ACh responses')
f('M76_7','7','Nerve-evoked and ACh responses reverse at similar voltages')
f('M76_8','8(A–C)','Dilator muscles contract in acetylcholine rather than glutamate')
f('M76_9','9(A–B)','Other pyloric muscles respond to glutamate; nerve stimulation is a control')
f('H87_1','1','Lobster STG anatomy, identified recordings and pyloric connections')
f('H87_net','1(right)','Published lobster pyloric circuit and identified neuron classes')
f('H87_4','4','Proctolin changes AB oscillations and the activity of follower cells')
f('H87_6','6','Proctolin excites the isolated AB neuron in a concentration-dependent manner')
f('H87_7','7','Isolated PD neurons retain tonic activity in proctolin')
f('H87_9','9','The isolated LP response depends on membrane voltage')
f('D18_1A','1(A–B, recordings)','Crab pyloric recordings before and after input removal')
f('D18_net','1(C)','Published crab pyloric pacemaker and inhibitory connections')
f('D18_6B','6(B)','Presynaptic depolarization evokes graded inhibition without spikes')
f('D18_2B','2(B)','Oxotremorine sustains slow oscillations after spike blockade')
f('D18_3','3(A–C)','Proctolin, FLRFamide and CCAP rhythms stop in TTX')
f('D18_8','8(A–B)','Isolated AB–PD oscillations persist in TTX with selected modulators')
f('S10_1AB','1(A–B)','Pyloric motor bursts at 7°C and 19°C')
f('S10_1C','1(C)','Pyloric frequency increases with temperature')
f('S10_1D','1(D)','Burst phases remain nearly constant from 7°C to 23°C')
f('S10_net','2(B)','Published crab pacemaker and follower-neuron connections')
f('S10_2C','2(C)','Voltage trajectories align when scaled to cycle duration')
f('S10_4A','4(A)','Transient potassium-current recordings at five temperatures')
f('S10_5A','5(A)','Hyperpolarization-activated current recordings across temperature')
f('M19_1BC','1(B–C)','Recorded PD waveforms entrain LP latency and activity phase')
f('M19_2AB','2(A–B)','Blocking glutamatergic input disrupts LP bursting')
f('M19_3BC','3(B–C)','Measured synaptic waveforms and dynamic-clamp-driven LP bursts')
f('M19_4','4(A–B)','LP phase depends on the timing reference and inhibitory duty cycle')
f('M19_6C','6(C1–C2)','Later inhibitory peaks delay LP activity in dynamic clamp')
f('G15_3A','3(A)','Crab foregut and the locations of nervous-system structures')
f('G15_4','4','CCAP receptor transcript abundance differs across identified neurons')
f('G15_7','7(A–F)','CCAP current amplitude and concentration dependence differ between LP and IC')
f('G15_5','5(A–D)','CCAP increases the graded VD-to-LG synaptic response')
f('R22_3AC','3(A–C)','Proctolin and CCAP change LP excitability and output variability')
f('R22_4ABC','4(A–C)','Modulators alter LP rebound latency and subsequent firing')
f('S21_1b','1(b)','Simultaneous slow gastric and fast pyloric motor output')
f('S21_net','1(c)','Published crab gastric, pyloric and descending-input connections')
f('S21_1d','1(d)','AB activity interrupts Int1 inhibition near LG burst onset')
f('S21_5ab','5(a–b)','LG cycle periods remain close to integer multiples of PD periods')
f('S21_6abc','6(a–c)','LG burst starts and spikes retain a preferred pyloric phase')
f('S15_net','1(A)','Published gastric half-center and descending MCN1 input')
f('S15_2A','2(A)','Fixed 6 Hz MCN1 drive fails at 13°C and recovers after cooling')
f('S15_3EF','3(E–F)','LG current responses and resistance differ between 10°C and 13°C')
f('S15_4AB','4(A–B)','Added leak stops bursting; leak subtraction rescues it')
f('S15_5A','5(A)','Gastric and pyloric activity persist in an intact crab at 13°C')
f('S15_6','6(A–E)','MCN1 activity increases with warming and stronger stimulation rescues LG')
f('S15_7A','7(A)','CabTRP Ia with continuing MCN1 drive restores LG bursts at 13°C')
f('H23_net','1(B)','Published crab pyloric network and descending modulatory input')
f('H23_2AB','2(A–B)','Frequency and phase recover over hours after decentralization')
f('H23_6','6','Pyloric phase relationships recover across temperature after 24 hours')
f('G22_1a','1(a)','Identified motor nerves resolve the regular crab pyloric rhythm')
slides=[]
def add(title, figures, body, extra, anatomy=None):
    assert len(body)==3
    fs=[figures] if isinstance(figures,str) else figures
    if anatomy: fs=fs+[anatomy]
    assert len(fs)<=2
    refs=list(dict.fromkeys(x.split('_')[0] for x in fs))
    # Complete connected explanatory sentences become the spoken bullet heads;
    # individually authored sub-bullets expand source-supported mechanisms and limits.
    notes=[[p.replace('**','').replace('_',''),[e]] for p,e in zip(body,extra)]
    sd={'title':title,'body':body,'transcript':notes,'cite':'; '.join(CITE[k] for k in refs),'refs':[S[k]['reference'] for k in refs],'figure_width':6.0}
    if len(fs)==1:sd.update(layout='figure-right',figure=FIG[fs[0]])
    else:
        sd.update(layout='figures-right',figures=[FIG[x] for x in fs],primary_figure_height=3.35)
        if anatomy:
            sd.update(figure_arrangement='side-by-side',primary_figure_width=4.3)
    slides.append(sd)

add('Two motor rhythms control processing in the foregut','S21_1b',[
'The **stomatogastric ganglion (STG)** is a compact collection of neurons that controls movements of the crustacean foregut. In the Jonah crab, _Cancer borealis_, the gastric mill moves teeth used for chewing, whereas the pyloric system controls filtering. The two motor patterns operate on different timescales within the same ganglion.',
'Powell and colleagues recorded identified motor nerves simultaneously in an isolated nervous system. The pyloric rhythm was approximately 1 Hz, while the slower gastric mill rhythm was approximately 0.1 Hz. A **burst** is a group of action potentials separated from the next group by a quieter interval.',
'The preparation retains central circuitry but removes normal food movement and most peripheral feedback. Its recordings identify coordinated motor commands; they do not measure tooth forces, particle transport or the amount of food swallowed.'
],[
'The gastric mill and pyloric systems are motor systems inside the foregut, rather than two names for the same set of muscles.',
'An action potential is a brief regenerative voltage change that travels along an axon; a nerve recording detects the spikes sent toward muscles.',
'A central pattern generator produces rhythmic neural output without requiring a separate sensory trigger for every cycle.'
],anatomy='G15_3A')
add('Input removal changes an isolated pyloric rhythm','M82_1',[
'Miller and Selverston isolated the stomatogastric nervous system of the spiny lobster, _Panulirus interruptus_. The STG remained connected to anterior ganglia through the **stomatogastric nerve (stn)**. Electrodes on outgoing nerves detected the activity of motor neurons supplying the pyloric muscles.',
'An isotonic sucrose solution around a short segment of the stn reversibly blocked impulse conduction. Comparing the same preparation before and during the block separated the local circuit from ongoing input supplied by other ganglia. The published control and blocked records use a 0.5 s timescale.',
'Input blockade changed the pyloric motor pattern even though the local neurons and their connections remained present. Central rhythm generation therefore depends on circuit state as well as connectivity. A disconnected preparation cannot be treated as an unchanged copy of the intact animal.'
],[
'Isotonic means that the solution has an osmotic concentration suitable for the tissue; the local sucrose pool blocks conduction through the input nerve.',
'The control is the same nervous system before its descending input is blocked, so differences are not comparisons between different animals.',
'The experiment tests the contribution of input to the ganglion, without requiring the experimenter to remove each descending neuron individually.'
])
add('Identified motor neurons connect spikes to muscle output','H87_1',[
'Stomatogastric neurons can be identified by the muscles their axons innervate and by the nerves carrying those axons. The lobster ganglion contains about 30 neurons. The **pyloric dilator (PD)** neurons, **lateral pyloric (LP)** neuron and **pyloric (PY)** neurons form recognizable classes within its pyloric motor system.',
'Hooper and Marder combined intracellular recordings from neuron cell bodies with extracellular recordings from the lateral and median ventricular nerves. **Intracellular recording** measures membrane voltage through an electrode inside a cell; **extracellular recording** detects spikes outside cells, including spikes traveling along axons.',
'Matching a cell-body spike to a nerve spike establishes the recorded neuron’s output pathway. Its name identifies a motor role, but does not specify its intrinsic rhythm-generating ability, transmitter or response to a modulator. Those properties require separate physiological experiments.'
],[
'A motor neuron sends its axon toward muscle; an interneuron communicates primarily with other neurons rather than directly innervating a muscle.',
'The nerve records distinguish motor units by their characteristic spike patterns and correspondence with an intracellular recording.',
'The count is species-dependent: the crab preparations studied by Rosenbaum and Marder contain 26–27 STG neurons, rather than the lobster count.'
])
# Include the crab count source in the spoken comparison.
slides[-1]['refs'].append(S['D18']['reference']);slides[-1]['cite']+='; '+CITE['D18']
add('Crab pyloric output repeats in three ordered phases','G22_1a',[
'The crab pyloric rhythm is **triphasic**: three neuron groups burst in a repeating sequence. PD activity is followed by LP activity and then PY activity. These motor commands activate different foregut muscles, organizing filtering movements rather than a synchronous contraction of the entire pyloric region.',
'Gorur-Shandilya and colleagues recorded separate PD, LP and PY motor nerves together with the mixed lateral ventricular nerve. The dedicated nerves separated units that overlapped in the mixed recording. Under baseline conditions at 11°C, the three groups retained their characteristic order on a 1 s timescale.',
'A mixed nerve signal can contain several identifiable neurons, but overlapping spikes become difficult to assign during irregular activity. Separate nerve recordings provide a control on unit identification. A regular sequence describes circuit output; it does not establish which neuron generates the rhythm.'
],[
'The anterior burster, abbreviated AB, is an interneuron electrically coupled to the two PD motor neurons.',
'An electrical synapse allows current to pass between coupled cells; a chemical synapse uses transmitter released by one cell to affect another.',
'The dedicated pyloric dilator, lateral pyloric and pyloric nerves provide independent recordings of the motor groups.'
])
add('Electrical coupling synchronizes AB and PD activity','E82_2',[
'Eisen and Marder recorded the lobster **anterior burster (AB)** interneuron, a PD motor neuron and the LP motor neuron simultaneously. AB and PD underwent synchronous slow voltage oscillations, with spikes concentrated during their depolarized portions. Electrical coupling permits voltage changes in one cell to influence the other.',
'LP spikes were followed by inhibitory voltage changes in both PD and AB. An **inhibitory postsynaptic potential (IPSP)** is a synaptically produced voltage response that reduces the likelihood of firing under the tested conditions. In AB, these responses were smaller and slower than those recorded in PD.',
'The detailed recordings used calibrations of 4 mV and 0.5 s. A spike-associated response in a coupled cell can arrive indirectly through another neuron. Temporal association alone therefore does not establish a direct chemical synapse from LP to AB.'
],[
'The slow voltage wave is distinct from the individual action potentials riding on its depolarized portion.',
'Electrical current spreading from PD could account for an inhibitory response in AB even if LP releases no transmitter directly onto AB.',
'Selective deletion and independent current injection are needed to distinguish those alternative pathways.'
],anatomy='H87_net')
add('An isolated AB neuron retains endogenous bursting','M82_2',[
'Miller and Selverston tested whether a neuron could oscillate after its known synaptic inputs were removed. **Photoinactivation** used an intracellularly injected dye and illumination to disable selected cells. A sucrose block simultaneously removed impulse-mediated input through the stomatogastric nerve.',
'After PD, LP and ventricular dilator neurons were disabled, AB retained spontaneous slow oscillations. In the published before-and-after recordings, outgoing spikes from the deleted neurons disappeared while the intracellular AB oscillation remained. The voltage and time calibrations were 20 mV and 1 s.',
'An **endogenous burster** generates recurring depolarizations without the synaptic inputs tested in this isolation procedure. AB met that operational criterion. The experiment identifies a cell-level source of rhythmicity, while leaving the specific ionic mechanism of its oscillation unresolved.'
],[
'The dye was lucifer yellow; illumination made the filled cells inactive while recordings tracked the remaining network.',
'The absence of the other cells’ output spikes and synaptic potentials checked whether the isolation was effective.',
'Endogenous bursting is a physiological property under specified conditions, rather than a conclusion drawn from a cell’s name or its circuit position.'
],anatomy='H87_net')
add('PD neurons become bursters when input recruits them','M82_3',[
'The two electrically coupled PD neurons did not behave like isolated AB. After AB and other relevant inputs were removed and the stn was blocked, PD fired **tonically**, meaning that spikes continued without the regularly separated slow depolarizing waves that define bursting.',
'Injecting depolarizing current increased tonic firing, but stimulation of the remaining input nerve recruited slow membrane oscillations. The published example used a 20 Hz stimulus train lasting 0.3 s. Oscillations outlasted the stimulus; across experiments they could continue for up to about a minute.',
'PD is therefore a **conditional burster**: an appropriate input state permits rhythm-generating properties that are absent in the isolated baseline state. The stimulation activated a collection of inputs, so the result does not identify one transmitter, receptor or channel as its sole cause.'
],[
'The surviving PD cells were recorded after the cells supplying their normal phasic input had been disabled.',
'A brief stimulation episode could change neuronal state for longer than the duration of the imposed spikes.',
'Tonic current injection and nerve stimulation are different interventions; similar depolarization does not guarantee the same cellular response.'
],anatomy='H87_net')
add('Input can recruit oscillations in follower neurons','M82_4',[
'Conditional oscillation was not confined to PD. Miller and Selverston examined a reduced lobster network after disabling AB and the ventricular dilator neuron. PD, LP and a late-firing pyloric neuron remained available for intracellular recording and controlled membrane polarization.',
'A 20 Hz input-nerve train lasting 0.5 s recruited voltage oscillations in the remaining neurons. Current injection suppressed selected cells to test whether an observed response required another cell’s activity. LP could express slow oscillations even when activity in the recorded PD and other pyloric cells was reduced.',
'The **ventricular dilator (VD)** neuron is a pyloric motor neuron with conditional bursting in the study’s other isolation experiments. Oscillatory capacity thus belongs to several circuit members under appropriate input conditions; AB was distinctive in bursting spontaneously after the complete tested isolation.'
],[
'Hyperpolarization makes a membrane voltage more negative, and can suppress a neuron’s spike generation or bursting.',
'The surviving neurons were not assumed to be independent merely because they were recorded separately; imposed polarization tested the contribution of their interactions.',
'The isolation results separate spontaneous endogenous bursting from input-dependent expression of oscillatory properties.'
],anatomy='H87_net')
add('A brief input can recruit a reduced motor network','M82_5',[
'After removal of the spontaneously bursting AB neuron and several other cells, a reduced PD–LP–VD network could remain nonrhythmic when descending input was blocked. Its retained neurons had inhibitory interactions, but those connections alone did not produce continuous coordinated bursting in that state.',
'A 50 Hz stimulus train lasting 1.4 s in the stomatogastric nerve initiated an episode of coordinated activity. Intracellular recordings at both fast and slow time bases distinguished individual membrane waves from the longer duration of the recruited episode.',
'A circuit can contain the connections needed for coordinated output while lacking the active cellular state that expresses it. The recruited episode supports a contribution of conditional membrane oscillations to motor-pattern stability. It does not imply that this reduced network reproduces every muscle command of the intact pyloric system.'
],[
'The experiment removed AB, the neuron that had passed the spontaneous isolation test, before assessing the remaining network.',
'The slow recording resolves persistence after the stimulus; the fast recording resolves the relationships among individual voltage waves.',
'A synaptic connection constrains interactions, but the activity generated by those interactions also depends on the membrane properties of the connected cells.'
],anatomy='H87_net')
add('Selective deletion separates two inhibitory outputs','E82_4',[
'Synchronous activity of AB and PD produces a compound IPSP in LP. Eisen and Marder separated the contributing pathways by photoinactivating either AB or both PD neurons. The comparison preserved recordings from LP and from the surviving member of the coupled pacemaker group.',
'With PD removed, AB bursts still inhibited LP. With AB removed, PD depolarizations also inhibited LP, but their responses had a different time course. The intact response therefore combined two chemical inhibitory outputs that were normally activated together by the electrically coupled cells.',
'LP-evoked IPSPs disappeared from AB when PD was removed. The same manipulation separated a direct AB-to-LP synapse from an indirect LP influence on AB through PD. Functional connectivity must distinguish transmitter release at a synapse from voltage propagation through an electrical connection.'
],[
'The pacemaker group consists of AB and its coupled PD neurons; their synchronous activity does not make their synapses identical.',
'Deletion assigns a component of a compound response to the cell that actually supplies it.',
'The loss of the LP response in AB after PD deletion is more discriminating than observing LP and AB activity at the same time.'
],anatomy='H87_net')
add('AB inhibition of LP depends strongly on chloride','E82_5',[
'After PD deletion, AB-to-LP inhibition could be tested without the overlapping PD output. Eisen and Marder varied LP membrane voltage and altered ionic conditions while evoking AB activity. The isolated response reversed near −64 mV in the published control experiment.',
'The **reversal potential** is the voltage at which a synaptic response changes sign. Doubling extracellular potassium did not shift the AB-evoked reversal appreciably. Increasing intracellular chloride shifted the response toward more positive voltages, implicating a substantial chloride contribution to its synaptic conductance.',
'A **conductance** describes how readily a membrane pathway carries electrical current. Chloride-dependent inhibition can oppose firing even when its voltage effect becomes small near reversal. These ionic manipulations constrain the mechanism of the synapse; they do not identify a molecular receptor subunit.'
],[
'Changing the postsynaptic holding voltage separates the response’s driving force from the amount of transmitter released.',
'Increasing chloride inside LP changes the ionic gradient across its membrane, so a chloride-carrying response should reverse at a different voltage.',
'The isolated AB response differed from the potassium-sensitive inhibition supplied by PD, despite the normal synchrony of the two presynaptic neurons.'
],anatomy='H87_net')
add('PD inhibition of LP is sensitive to potassium','E82_6',[
'Eisen and Marder isolated PD-to-LP transmission by disabling AB and VD, then depolarized PD with current pulses. LP was recorded at several membrane voltages to determine where the isolated inhibitory response changed sign. The control reversal in the published experiment was −86 mV.',
'Doubling extracellular potassium shifted that reversal to approximately −65 mV. Chloride loading did not produce the corresponding shift found for AB-to-LP inhibition. The PD response therefore depended strongly on potassium permeability, whereas the synchronized AB response had a different ionic basis.',
'An ion’s concentration gradient and the postsynaptic voltage determine the direction of its contribution to synaptic current. Two inputs can both inhibit LP at its normal operating voltage while differing in reversal, kinetics and pharmacology. Their combined effect cannot be represented as two physiologically identical synapses.'
],[
'The current pulse reproduced presynaptic depolarization while allowing the experimenter to control when the PD response was evoked.',
'External potassium was an experimental manipulation of driving force, rather than a test of the number of potassium channels in the neuron.',
'The measured ionic selectivity does not establish the identity of every channel protein involved in the synaptic response.'
],anatomy='H87_net')
add('Electrical coupling can carry an indirect IPSP','E82_9',[
'An LP spike can produce a response in AB although chemical feedback directly targets PD. Eisen and Marder hyperpolarized AB or PD while recording all three cells. They tested whether the AB response followed AB voltage or the response generated in PD.',
'Hyperpolarizing AB to approximately −72 mV did not reverse its LP-associated IPSP. Hyperpolarizing PD instead reversed the response in PD and the voltage response appearing in AB. The AB response therefore tracked a PD synaptic event carried through electrical coupling.',
'**Electrotonic spread** is passive propagation of a voltage change through a connected electrical pathway. A neuron may receive such a propagated response without possessing the corresponding chemical synapse. A connection map based only on spike-correlated voltage changes can consequently assign the wrong presynaptic target.'
],[
'The manipulation compared the two cells at similar negative voltages, but changed which cell was directly polarized.',
'If LP released transmitter directly onto AB, changing AB’s own membrane voltage should govern the local synaptic reversal.',
'The results require a chemical LP-to-PD connection plus electrical propagation from PD into AB.'
],anatomy='H87_net')
add('Acetylcholine excites the lobster dorsal dilator','M76_2',[
'Marder tested transmitter identity at the lobster PD-to-muscle junction. **Acetylcholine (ACh)** is a small-molecule neurotransmitter; applying it locally to the dorsal dilator produced a depolarizing response. Stimulating the PD motor nerve produced an **excitatory junctional potential**, the muscle voltage response to neural transmitter release.',
'Hexamethonium reversibly reduced both the nerve-evoked response and the response to applied ACh. Washout restored them toward their control amplitudes. Local ACh delivery and motor-nerve stimulation therefore interrogated a pharmacologically similar postsynaptic pathway in the same muscle system.',
'A transmitter candidate is stronger when it reproduces the nerve response and shares its antagonist sensitivity. Drug sensitivity alone is insufficient because a compound may affect more than one receptor class. These experiments support cholinergic transmission without assigning a modern molecular receptor subtype.'
],[
'Iontophoresis delivers a charged substance from a pipette with electrical current, allowing a localized test of the muscle’s response.',
'The comparison included normal saline, antagonist exposure and saline wash, separating a reversible drug action from irreversible tissue failure.',
'Excitation at the muscle does not mean that the same transmitter excites every neuron onto which PD releases it.'
],anatomy='G15_3A')
add('Nerve and ACh responses reverse at similar voltages','M76_7',[
'Marder compared the voltage dependence of applied ACh responses with the dorsal dilator’s nerve-evoked junctional responses. The muscle membrane was polarized to different voltages, and response amplitude was measured using intracellular and focal extracellular recording approaches.',
'The ACh response extrapolated to a reversal near −18 mV in the recorded experiment. Nerve-evoked responses reversed in a similar negative voltage range. A **depolarization** makes the membrane less negative; its amplitude declines as the muscle voltage approaches the response’s reversal potential.',
'Similar reversal behavior supports a shared postsynaptic ionic mechanism for the applied transmitter and the neural response. Receptor desensitization and large response amplitudes could distort the extrapolation, so Marder used small responses and controlled application timing. The agreement strengthens transmitter identification without directly observing individual molecules released from PD.'
],[
'Focal extracellular recording placed the electrode near an active junction, while intracellular recording measured the muscle fiber’s membrane voltage.',
'The reversal estimate summarizes an electrical property of the response; it is not the muscle’s resting voltage.',
'Desensitization is a reduction in responsiveness during repeated or sustained agonist exposure, and can make successive application tests misleading.'
],anatomy='G15_3A')
add('Motor-neuron classes differ in transmitter evidence','M76_8',[
'Marder screened muscles innervated by identified lobster motor-neuron classes with ACh and L-glutamate. **Glutamate** is another small-molecule transmitter. PD-innervated dilators and the VD-innervated muscle contracted in ACh, whereas the LP/PY region and inferior cardiac muscle responded to glutamate.',
'An unresponsive bath application was checked against nerve-evoked contraction. In the LP/PY preparation, stimulation at 10 pulses/s for 2 s confirmed that the muscles were still viable. Choline acetyltransferase assays provided separate evidence for ACh synthesis in identified neuronal cell bodies.',
'The combined evidence assigned ACh or glutamate as transmitter candidates for different motor classes. The strongest detailed physiological identification concerned PD; several other assignments remained putative. A candidate inferred from muscle sensitivity and synthesis should be distinguished from complete proof of its release and action at every central synapse.'
],[
'Choline acetyltransferase is the enzyme that synthesizes acetylcholine, so its presence supplies biochemical evidence distinct from a muscle’s drug response.',
'The inferior cardiac neuron is abbreviated IC; the name refers to a foregut motor neuron, rather than a neuron controlling the heart.',
'A peripheral muscle can be excited by a transmitter that mediates inhibition at another target, because postsynaptic receptor and ionic mechanisms differ.'
],anatomy='G15_3A')
add('Slow presynaptic depolarization can release transmitter','D18_6B',[
'In crab pyloric neurons, chemical transmission has both spike-mediated and **graded** components. Graded transmission varies with the presynaptic membrane potential and does not require a full action potential. Rosenbaum and Marder tested it while tetrodotoxin, or **TTX**, blocked the voltage-gated sodium channels needed for spiking.',
'LP was depolarized from −60 mV to −20 mV for 500 ms while PD was held near −50 mV. PD developed an inhibitory response despite the absence of presynaptic spikes. Holding the postsynaptic voltage constant reduced differences in response amplitude caused merely by changing driving force.',
'The LP-to-PD pathway can therefore transmit a slow voltage signal through transmitter release. A motor circuit’s synaptic communication cannot be inferred exclusively from spike counts. This result concerns central synaptic potentials; it does not imply that a spike-free isolated circuit produces normal muscle contractions.'
],[
'Voltage-gated channels change their probability of opening when the membrane voltage changes; TTX selectively blocks a major sodium-dependent spike mechanism.',
'The presynaptic voltage step and the postsynaptic voltage control separate transmitter-release conditions from the voltage at which the response is measured.',
'An inhibitory graded response provides feedback to the pacemaker even when spikes have been experimentally removed.'
],anatomy='D18_net')
add('Muscarinic activation can sustain a spike-free rhythm','D18_2B',[
'Rosenbaum and Marder first blocked descending input to the crab STG, then applied a modulator and finally added TTX. **Oxotremorine** is an agonist that activates muscarinic acetylcholine receptors. These receptors alter cellular state rather than supplying the brief muscle-junction response tested in the lobster experiments.',
'Oxotremorine at 10 μM increased the pyloric activity of the decentralized preparation. Addition of 0.1 μM TTX removed action potentials while PD and LP retained alternating slow membrane oscillations. Intracellular voltage records were essential because extracellular motor nerves no longer contained the usual spikes.',
'Slow voltage dynamics and graded inhibition can sustain central rhythmicity in this modulatory state. Persistence after sodium-channel blockade does not mean that spikes never contribute to the intact rhythm. Nor does it establish normal behavioral output, which requires commands to reach the muscles.'
],[
'An agonist is a substance that activates a receptor; muscarinic receptors are a class of acetylcholine receptor associated with slower modulation.',
'Decentralization removes descending modulatory input, making the bath-applied compound the controlled source of the tested modulatory drive.',
'The before-modulator, after-modulator and after-TTX sequence distinguishes restoration of a rhythm from its dependence on spiking.'
],anatomy='D18_net')
add('Similar activating peptides differ in spike dependence','D18_3',[
'**Neuropeptides** are short chains of amino acids released as chemical signals that can alter neuronal activity. Rosenbaum and Marder compared several peptides that activate the same modulator-activated inward current, **I_MI**, a voltage-dependent current carried by nonspecific cation channels, in different subsets of crab pyloric neurons.',
'Proctolin, TNRNFLRFamide and crustacean cardioactive peptide, or **CCAP**, each at 1 μM, activated robust pyloric rhythms after decentralization. Adding TTX stopped the rhythms in the published examples. By contrast, oxotremorine and the tachykinin-related peptide CabTRP1a supported slow oscillations without spikes.',
'Activation of a common inward current is not sufficient to predict whether a network can oscillate after spike blockade. Target-cell distributions, synaptic actions and other currents can differ among modulators. The experiment establishes state-dependent reliance on spikes, rather than one universal mechanism for all peptide-activated rhythms.'
],[
'An inward current carries net positive charge into the cell and can promote depolarization. Extracellular calcium blocks I_MI at strongly negative membrane voltages; relief of that block during depolarization can amplify slow voltage waves.',
'CabTRP1a means Cancer borealis tachykinin-related peptide Ia; its name identifies the peptide rather than a distinct neuron.',
'Each compound was tested as a controlled bath application, so the comparison does not imply equal natural release patterns in the animal.'
],anatomy='D18_net')
add('The pacemaker can oscillate without follower feedback','D18_8',[
'The AB–PD ensemble can be examined after feedback from glutamatergic follower neurons is blocked. **Picrotoxin (PTX)** blocks the relevant glutamatergic inhibitory synapses in this preparation. Rosenbaum and Marder combined PTX with TTX to separate pacemaker oscillation from spikes and major follower feedback.',
'In oxotremorine or CabTRP1a, PD retained slow oscillations after both drugs were added. LP activity was greatly reduced, yet the remaining pacemaker wave continued. The intracellular records used 20 mV voltage calibration and 1–2 s time calibration.',
'The result localizes a rhythm-generating capability to the electrically coupled AB–PD group under these modulatory conditions. PTX is a pharmacological isolation procedure, not physical removal of every neuron. Persistence of the pacemaker does not specify which coupled member or which individual channel is sufficient on its own.'
],[
'AB and PD remain electrically connected when follower chemical synapses are blocked, so the retained oscillator is an ensemble.',
'TTX prevents the usual sodium-dependent spikes, while PTX removes a different component: the inhibitory feedback carried by glutamatergic synapses.',
'The combination tests the dependence of the central voltage rhythm on two mechanisms without measuring the behavior of the whole crab.'
],anatomy='D18_net')
add('LP latency and phase change differently with period','M19_1BC',[
'**Cycle period** is the interval between successive starts of a rhythm. **Latency** is the time from a reference event to a response, whereas **phase** expresses that delay as a fraction of the cycle. A fixed latency therefore does not automatically preserve phase when the cycle changes.',
'Martinez and colleagues voltage-clamped a crab PD neuron with a recorded waveform repeated at different periods. **Voltage clamp** holds a membrane to a commanded voltage by injecting the required current. LP followed the imposed rhythm, but its onset latency and normalized onset phase changed differently.',
'The measured LP phase declined as period increased, rather than remaining perfectly constant. Imposed pacemaker waveforms separated the timing of inhibition from the free-running network’s normal adjustments. This preparation tests mechanisms of phase control, not a claim that natural pyloric phase is always invariant.'
],[
'The published conceptual alternatives distinguish constant delay from constant relative timing; the physiological records and measurements test where LP falls between those alternatives.',
'The voltage command used a waveform recorded from PD, so the experiment preserved a realistic presynaptic voltage shape while changing its repetition rate.',
'The period range in the plotted experiment spans fractions of a second to around two seconds, with latency measured in seconds and phase expressed without units.'
],anatomy='S10_net')
add('Glutamatergic input is required for normal LP bursts','M19_2AB',[
'Martinez and colleagues recorded LP intracellularly while monitoring the crab lateral ventricular nerve. LP normally received alternating inhibition from the pacemaker and other pyloric neurons. Its recurring bursts depended on those inputs interacting with its own membrane properties.',
'Bath application of 10 μM picrotoxin blocked glutamatergic inhibition from AB and PY. LP’s organized slow bursting disappeared while activity from other pyloric neurons remained visible on the nerve. The published comparison used a 500 ms time calibration and a 10 mV intracellular voltage calibration.',
'Loss of LP rhythmicity after removal of particular inputs distinguishes a follower neuron from an autonomous oscillator in this condition. The remaining cholinergic PD synapse means that pharmacological isolation was incomplete. The experiment assigns a requirement to the blocked pathways, rather than proving that all synaptic inputs are interchangeable.'
],[
'A follower neuron can generate spikes and rebound responses without generating a self-sustaining rhythm when its coordinating inhibition is removed.',
'Picrotoxin blocks the relevant glutamatergic inhibitory pathways here; it should not be treated as a universal blocker of every chemical synapse.',
'The surviving nerve units help distinguish selective disruption of LP’s timing from a preparation-wide failure of neuronal activity.'
],anatomy='S10_net')
add('Dynamic clamp tests the timing effect of inhibition','M19_3BC',[
'**Dynamic clamp** injects an electrical current calculated from the recorded membrane voltage and a specified conductance. Martinez and colleagues used it to replace blocked input to a living LP neuron. The neuron’s own channels remained active while the experimenter controlled the inhibitory waveform.',
'The physiological synaptic waveform was measured in voltage-clamped LP and aligned to pacemaker burst onset. Replaying a conductance based on that waveform recruited LP bursts. Increasing imposed conductance delayed LP onset, whereas lengthening the repetition period tended to move onset to an earlier fraction of the cycle.',
'Opposing timing effects allow synaptic properties to compensate for changes in rhythm speed. The intervention tests the effect of a specified electrical input on a real neuron. It does not establish that the intact network naturally changes every waveform parameter in exactly the imposed manner.'
],[
'A conductance-based input changes current as the postsynaptic voltage changes, preserving a property that a fixed current pulse does not capture.',
'The publication includes measured synaptic currents, replayed responses and phase measurements; these are distinct parts of the causal test.',
'The amplitude of the synaptic conductance was measured in microsiemens, and the repetition period was measured in seconds.'
],anatomy='S10_net')
add('Inhibitory duty cycle contributes to phase control','M19_4',[
'**Duty cycle** is the fraction of a complete cycle occupied by an event. The duration of inhibition can remain a similar fraction of the pyloric cycle even as the absolute period changes. That relationship alters when an LP neuron is released from inhibition.',
'Martinez and colleagues compared LP onset phase measured from the start of the imposed pacemaker burst with onset measured from its end. The same bursts produced different phase-versus-period relationships under the two reference definitions. Their dynamic-clamp experiments also varied inhibitory duration independently of other waveform features.',
'Maintaining inhibitory duration proportional to period promoted phase maintenance more effectively than keeping duration fixed in milliseconds. The result concerns the timing of a controlled synaptic input. A stable motor phase can therefore emerge from coordinated input timing without requiring each neuron to retain a fixed absolute rebound latency.'
],[
'The reference event must be stated whenever a phase is reported, because onset-relative and offset-relative phases describe different delays.',
'The authors compared a fixed-duration condition of 300 ms with a fixed-duty-cycle condition occupying 0.3 of each cycle in their systematic waveform experiments.',
'Coordinating synaptic duration with period changes the time available for recovery from inhibition and for subsequent depolarization.'
],anatomy='S10_net')
add('Later inhibitory peaks delay a follower’s activity','M19_6C',[
'Martinez and colleagues varied the position of the peak within an imposed inhibitory conductance while keeping its period and amplitude controlled. A **peak phase** specifies when the conductance reaches its maximum within the active inhibitory interval. The waveform was delivered by dynamic clamp to a living LP neuron.',
'Moving the peak later shifted the onset of LP firing to a later pyloric phase. The published recording examples used a 500 ms period and compared several peak positions. They separated a change in inhibitory timing from a change in the neuron’s identity or its natural synaptic wiring.',
'Amplitude, duration and peak position can jointly influence release from inhibition. The authors’ mathematical analysis proposes how short-term synaptic depression could coordinate these features as period changes. The imposed-waveform recordings directly establish timing sensitivity; the proposed natural coordination requires a separate mechanistic inference.'
],[
'Short-term synaptic depression is a transient reduction of a synapse’s efficacy during repeated activation, followed by recovery when activation is reduced.',
'The input shapes are experimental conductances specified by the authors, and the voltage responses are recordings from the biological LP neuron.',
'The published inference about depression should be distinguished from an experiment that selectively blocks the molecular mechanism of depression in the intact circuit.'
],anatomy='S10_net')
add('Proctolin changes the lobster pacemaker’s oscillation',['H87_4','H87_6'],[
'**Proctolin** is a five-amino-acid neuropeptide that modulates the lobster pyloric circuit. Hooper and Marder applied it to the isolated stomatogastric preparation after descending input was blocked. Intracellular recordings separated slow membrane oscillations from the spikes generated during each depolarized phase.',
'At 1 μM proctolin, AB oscillation amplitude increased and follower-neuron activity changed. In isolated AB, progressively higher peptide concentrations recruited stronger activity. Saline wash between applications returned the neuron toward its baseline, providing a control for reversibility and persistent peptide effects.',
'The network response combined direct peptide actions on selected neurons with consequences propagated through their existing connections. Increased activity in a motor neuron did not by itself establish a direct receptor-mediated action on that cell. Isolation was required to distinguish a peptide target from a synaptic follower of another target.'
],[
'A peptide can alter a circuit without replacing its established synaptic connections or supplying a new rhythmic command on every cycle.',
'The isolated AB series included 0.1 nM, 10 nM and 1 μM applications, with at least 45 minutes of saline wash between tests.',
'The concentration-dependent response identifies a physiological action of proctolin; these recordings alone do not identify its receptor’s molecular sequence.'
])
add('Direct peptide targets differ from affected motor cells',['H87_7','H87_9'],[
'Hooper and Marder isolated lobster PD neurons from their major synaptic inputs, then applied 1 μM proctolin. The PD cells continued tonic firing without the direct peptide response found in isolated AB. In the intact circuit, however, PD activity changed because PD remained electrically coupled to the peptide-responsive AB neuron.',
'An isolated LP neuron responded differently depending on its membrane voltage. At approximately −58 mV, proctolin caused depolarization and spiking. At approximately −62 mV in the same neuron, that response was absent. Voltage-dependent expression of modulation can therefore obscure a response during a single baseline test.',
'A modulator’s circuit effect depends on target-cell properties and the connections transmitting their effects. Failure to respond in one voltage state does not prove that a neuron lacks a relevant receptor. Conversely, changed activity in the connected circuit does not prove that the modulator acts directly on that motor neuron.'
],[
'Electrical coupling provides a route by which an AB change affects PD even when isolated PD is insensitive to the tested proctolin application.',
'Two electrodes allowed the experimenter to record LP voltage while using injected current to set its starting membrane potential.',
'The observed voltage dependence motivates tests over several membrane states; it does not establish a particular channel’s gating mechanism from these traces alone.'
])
add('CCAP receptor transcripts differ among neuron classes','G15_4',[
'Garcia and colleagues identified a candidate **CCAP receptor** transcript in the crab nervous system. A **transcript** is an RNA copy of a gene used in protein production. The candidate sequence resembled known peptide receptors and predicted a receptor with seven membrane-spanning segments.',
'**Single-cell quantitative PCR** measured receptor RNA from individually identified neurons. PCR amplifies a selected nucleic-acid sequence so its abundance can be estimated. LP generally contained more receptor transcript than IC, while expression was low or undetectable in several other STG classes.',
'Transcript distribution broadly matched the cells in which CCAP activates I_MI. VD was an exception: receptor RNA was present without a detected current response. RNA abundance does not measure membrane receptor protein or identify every downstream effect of activation.'
],[
'The seven-segment topology and sequence similarity support a G-protein-coupled receptor candidate, rather than identifying a ligand-gated ion channel.',
'A G protein participates in intracellular signaling after receptor activation; those signaling steps can alter a different membrane protein that carries current.',
'The transcript and physiological measurements are complementary, but the study did not equate each RNA molecule with one functional membrane receptor.'
],anatomy='S21_net')
add('The same peptide produces different current responses','G15_7',[
'Garcia and colleagues voltage-clamped identified crab neurons while applying CCAP at controlled concentrations. They measured **I_MI**, a voltage-dependent modulator-activated inward current, by subtracting control currents from currents measured in peptide. LP and IC differed in both response magnitude and concentration dependence.',
'LP generated larger inward currents and responded more strongly at low concentrations than IC. Current measurements at −20 mV distinguished a cell’s concentration-response relationship from its spontaneous firing pattern. Increasing CCAP could saturate the response, so added peptide eventually produced little additional current.',
'Both cells possessed the capacity for peptide-activated inward current, yet the same bath concentration did not produce equivalent activation. Receptor abundance and access to downstream channel mechanisms are possible contributors. The physiological comparison does not establish a one-to-one conversion between receptor transcript count and current amplitude.'
],[
'Saturation means that increasing the ligand no longer increases the measured response substantially under the tested conditions.',
'The current–voltage measurements retained the voltage dependence of the inward current, while the concentration series tested sensitivity to the ligand.',
'The source’s receptor RNA comparison and current comparison support cell-specific modulation without defining the complete molecular composition of the I_MI channel.'
],anatomy='S21_net')
add('CCAP can modulate a synapse without activating I_MI','G15_5',[
'The crab VD neuron expressed candidate CCAP receptor RNA but lacked a detected CCAP-induced I_MI response. Garcia and colleagues tested a different physiological endpoint: the graded inhibitory synapse from VD to the lateral gastric neuron, **LG**, a motor neuron participating in the gastric mill rhythm.',
'VD voltage steps evoked postsynaptic current in voltage-clamped LG. Application of 100 nM CCAP strengthened this response, and washout returned it toward control. The comparison measured the same synapse under controlled presynaptic and postsynaptic voltages, rather than inferring synaptic strength from uncontrolled spike counts.',
'A peptide receptor can influence synaptic transmission even when one particular intrinsic current is absent. The VD result resolves an apparent mismatch between transcript expression and I_MI response. It does not establish that receptor activation follows identical intracellular signaling steps in VD, LP and IC.'
],[
'The lateral gastric motor neuron is associated with the protraction component of the gastric mill rhythm, and receives input from neurons shared with other motor patterns.',
'The publication measured graded synaptic current across presynaptic voltage steps and during an imposed waveform, separating voltage-dependent release from natural circuit firing.',
'A negative result for one current assay should not be treated as a negative result for every form of modulation in that cell.'
])
add('Modulators change excitability and reduce output variation','R22_3AC',[
'**Excitability** describes how readily a neuron generates action potentials in response to input. Schneider and colleagues isolated the crab LP neuron pharmacologically, then injected progressively larger depolarizing currents. The resulting firing-rate relationship was measured in control saline, proctolin, proctolin plus CCAP and wash.',
'Proctolin shifted the relationship so LP began firing at lower injected current. Adding CCAP further altered its output. Comparisons across animals found that neuronal firing responses became more similar in modulators, even though the underlying measured intrinsic and synaptic currents remained variable.',
'**Interindividual variability** means differences among animals of the same species. Neuromodulation can constrain that variability at the level of output without making every cellular parameter identical. The result concerns responses of isolated LP to controlled current, rather than all dimensions of the intact pyloric motor pattern.'
],[
'The firing-rate–current relationship measures spikes per second at a specified current in nanoamperes, making input and output explicit.',
'The test included 1 μM proctolin and 1 μM CCAP, with wash recordings used to assess the reversibility of modulation.',
'Similar activity can arise in neurons with different current magnitudes because output depends on the interaction of currents over the neuron’s operating voltage range.'
],anatomy='S10_net')
add('Peptide state changes rebound after inhibition','R22_4ABC',[
'**Postinhibitory rebound** is renewed depolarization or firing after an inhibitory episode ends. Schneider and colleagues tested it in isolated crab LP neurons with a 5 s hyperpolarizing current pulse of −5 nA. Recording continued after release to measure the first spike and subsequent firing.',
'Proctolin and proctolin plus CCAP shortened rebound latency and increased spike output relative to control saline. The recordings compared identical imposed inhibitory pulses across modulatory conditions. Across animals, several rebound-output differences became smaller in the peptide states.',
'The same neuron can therefore resume firing differently after the same inhibition when its modulatory state changes. Rebound is an interaction between prior voltage history and active membrane currents, rather than a fixed delay assigned to a cell type. The experiments do not isolate one current as the sole source of rebound.'
],[
'The neuron’s voltage during inhibition changes the availability of voltage-dependent channels before the pulse ends.',
'Rebound latency was measured from the end of the imposed inhibitory current to the first detected action potential, not from the beginning of the pulse.',
'The wash condition checked the persistence of the altered response after peptide removal.'
],anatomy='S10_net')
add('Gastric mill activity alternates protraction and retraction','S21_1d',[
'The crab **gastric mill rhythm** organizes chewing movements through alternating phases. LG participates in **protraction**, movement of the gastric teeth toward the chewing configuration, whereas other gastric motor neurons are associated with **retraction**, their return movement. The slower gastric rhythm interacts with the fast pyloric rhythm.',
'Powell and colleagues recorded activity from identified gastric and pyloric motor nerves. Gastric activity included alternating LG and dorsal gastric, or **DG**, bursts, while PD continued its faster rhythm. Intracellular recordings linked LG activity to the inhibitory gastric interneuron **Int1**, meaning interneuron 1.',
'LG and Int1 participate in a **half-center**, a reciprocally inhibitory arrangement in which activity in each member inhibits the other. That arrangement helps organize alternation but does not, by itself, establish sustained rhythm generation in every input state. Descending modulation supplies additional conditions for gastric activity.'
],[
'LG and DG are gastric motor neurons, whereas Int1 is an interneuron within the central gastric circuit.',
'Reciprocal inhibition means that each partner supplies inhibition to the other; the active partner suppresses its antagonist during its burst.',
'The slow rhythm operates near 0.1 Hz in the preparations discussed by Powell and colleagues, while the pyloric rhythm operates near 1 Hz.'
],anatomy='S21_net')
add('Descending MCN1 input recruits the gastric half-center','S15_2A',[
'**Modulatory commissural neuron 1 (MCN1)** is a descending projection neuron whose cell body lies in a commissural ganglion. Its axon reaches the crab STG through the input nerves. Städele and colleagues controlled this input by stimulating the identified pathway after disconnecting other anterior influences.',
'MCN1 releases the peptide CabTRP Ia, which activates an inward current in LG, and also supplies electrical and other synaptic influences within the gastric circuit. LG and Int1 inhibit one another. Rhythmic alternation therefore depends on a combination of imposed modulatory drive, intrinsic membrane properties and reciprocal inhibition.',
'At 10°C, continuous MCN1 stimulation at 6 Hz recruited recurring LG bursts in the published example. The stimulus itself was tonic, rather than patterned to match every LG burst. Slow gastric rhythmicity was thus generated by the responding circuit under sustained descending activation.'
],[
'A projection neuron sends an axon from one ganglion into another and can provide a modulatory state rather than a precisely timed command for every contraction.',
'LG inhibits MCN1 terminals during its active phase, so a constant axonal stimulus does not guarantee constant effective peptide influence throughout the gastric cycle.',
'The controlled stimulation establishes a defined gastric-rhythm state; naturally recruited gastric rhythms can receive additional descending and sensory inputs.'
],anatomy='S15_net')
add('Warming speeds the pyloric rhythm about fourfold','S10_1C',[
'Tang and colleagues tested the crab pyloric circuit over a temperature range relevant to an ectothermic animal. An **ectotherm** relies substantially on environmental conditions to determine body temperature. The isolated stomatogastric preparation was warmed gradually while outgoing motor activity was recorded.',
'Between 7°C and 23°C, pyloric rhythm frequency increased about fourfold. PD, LP and PY retained the characteristic burst sequence while completing cycles more quickly. Comparisons during warming and cooling checked whether the relationship depended on the direction of temperature change.',
'The reported frequency temperature coefficient, **Q10**, was approximately 2.3; Q10 describes the fold change associated with a 10°C increase. Temperature compensation need not mean a constant frequency. Different output properties can remain coordinated even when the entire motor pattern accelerates.'
],[
'The nerve recordings measure central motor commands in a preparation with its normal anterior modulatory connections retained.',
'The recorded sequence persisted even though the absolute intervals separating successive bursts became shorter.',
'The observed frequency increase should be distinguished from a mechanism that holds a circadian period constant across temperature.'
],anatomy='S10_net')
add('Relative burst timing remains stable during warming','S10_1D',[
'Tang and colleagues measured each motor burst relative to the start of the PD burst. The **onset phase** specifies when a burst begins within a cycle, and the **offset phase** specifies when it ends. These fractions distinguish relative coordination from absolute delays measured in seconds.',
'Across 7°C to 23°C, PD, LP and PY onset and offset phases remained nearly constant despite the increase in frequency. When intracellular voltage trajectories were scaled to cycle duration, their characteristic temporal relationships also remained similar across the tested temperatures.',
'The pyloric circuit therefore compensated the coordination of its motor output more closely than its speed. Stability of phase does not imply that every underlying conductance was temperature-invariant. The neuron’s membrane currents and synaptic input could change while their combined effect preserved the sequence.'
],[
'The phase reference was the beginning of the PD burst, which is assigned the start of the pyloric cycle.',
'A shorter delay in seconds can occupy the same fraction of a shorter cycle, so unchanged phase and increased frequency are compatible observations.',
'The intracellular trajectories were normalized by cycle duration; their alignment tests whether relative voltage timing persists as the cycles become faster.'
],anatomy='S10_net')
add('A transient potassium current opposes depolarization','S10_4A',[
'The LP neuron contains the **A-type potassium current, I_A**, which activates during depolarization and then declines. Activation increases channel opening; **inactivation** reduces channel availability despite continuing depolarization. This transient outward current can oppose the return to firing after inhibition.',
'Tang and colleagues isolated I_A with voltage-clamp protocols that separated it from other potassium currents. Depolarizing test steps from −40 mV to +30 mV elicited transient currents at temperatures from 7°C to 23°C. The published families of currents use 100 nA and 400 ms calibrations.',
'Warming increased current magnitude and accelerated its activation and inactivation. A change in amplitude alone therefore does not predict its effect on burst delay; a stronger transient current may also disappear sooner. The measurements identify temperature-sensitive current behavior without proving that I_A alone maintains LP phase.'
],[
'Potassium current is outward over the tested depolarized range, carrying a voltage influence that opposes excitation.',
'Voltage clamp allows the current to be measured at controlled membrane voltages instead of inferring it from a changing burst waveform.',
'The time course matters because the inhibition preceding LP firing changes which channels are available when excitation resumes.'
],anatomy='S10_net')
add('Hyperpolarization recruits an opposing inward current','S10_5A',[
'The **hyperpolarization-activated inward current, I_h**, turns on as the membrane becomes more negative. It carries a depolarizing influence during and after inhibition, opposing the voltage effect of sustained inhibitory input. Its activation can therefore interact with the outward I_A current in determining LP rebound.',
'Tang and colleagues applied hyperpolarizing voltage steps from a holding potential near −50 mV, with test potentials extending to −120 mV. The slowly developing inward current was recorded at several temperatures. The published recordings have a 15 nA current calibration and a 2 s time calibration.',
'Warming increased I_h conductance and accelerated its activation. Its temperature sensitivity differed from that of I_A and synaptic inhibition. The observed phase stability must therefore arise from combined processes; it cannot be attributed to every current changing by the same amount or remaining unchanged.'
],[
'An inward current need not create an action potential immediately; it can alter how quickly a neuron approaches the voltage range where spikes begin.',
'The current grows during a sustained hyperpolarizing step, unlike the transient decline of I_A during a depolarizing step.',
'The experiment measures an electrical current and its temperature dependence, rather than directly counting the channel proteins in the membrane.'
],anatomy='S10_net')
add('A weakly driven gastric rhythm fails after modest warming','S15_2A',[
'Städele and colleagues held MCN1 stimulation constant near the minimum frequency that recruited a gastric mill rhythm at 10°C. They then warmed the crab STG to 13°C while recording LG. This isolated preparation lacked the anterior circuits that could naturally increase descending drive.',
'LG’s regular bursts disappeared at 13°C with the same MCN1 stimulation. Cooling back to 10°C restored them. The published example used a 6 Hz stimulus throughout, separating temperature-dependent circuit failure from an intentional reduction of input frequency.',
'The failure was conditional on the weak, fixed drive and the isolated preparation. It does not establish that a living crab loses chewing after every 3°C temperature increase. A different input strength or naturally changing descending activity can preserve the slow motor rhythm at the same temperature.'
],[
'The within-preparation return to 10°C is a recovery control, reducing the likelihood that the lost bursting simply reflected irreversible damage.',
'The term failure here refers to the absence of rhythmic LG bursting, even when some spikes or membrane activity remained.',
'Input state must accompany any temperature threshold: the authors could raise the permissive temperature range by increasing MCN1 stimulation.'
],anatomy='S15_net')
add('Leak conductance can stop or restore gastric bursting','S15_4AB',[
'A **leak conductance** is a membrane pathway that contributes current without the rapid voltage gating characteristic of spike-generating channels. Städele and colleagues found that warming reduced LG input resistance, so a given input current produced a smaller membrane-voltage change.',
'Dynamic clamp added an effective leak to LG at 10°C during 7 Hz MCN1 stimulation, and bursting stopped. At 13°C, subtracting an effective leak restored recurring LG bursts while the MCN1 stimulus remained unchanged. Opposite interventions tested whether the conductance change was sufficient to alter circuit output.',
'Leak subtraction is an imposed electrical compensation, rather than direct removal of a channel protein. The causal result connects LG membrane responsiveness to gastric rhythmicity in this preparation. It does not establish that the animal compensates warming by physically closing exactly the channels represented in the clamp.'
],[
'Input resistance describes the voltage response to an injected current; a larger effective membrane conductance makes that response smaller.',
'The dynamic clamp used the measured voltage to calculate an added or subtracted current continuously, while the biological circuit remained active.',
'The addition and subtraction tests are stronger evidence than observing a resistance change and a rhythm change at the same time.'
],anatomy='S15_net')
add('Stronger descending drive restores gastric output','S15_6',[
'The crab gastric mill rhythm persisted at 13°C in intact-animal recordings, despite failure of the isolated weakly driven preparation. Städele and colleagues tested whether descending MCN1 activity could supply compensatory input. They recorded MCN1 axonal activity from the commissural ganglion pathway during warming.',
'MCN1 firing increased with temperature. In the published example it rose from 2.31 Hz at 10°C to 3.63 Hz at 13°C. In a separate controlled stimulation test, increasing imposed MCN1 activity from 7 Hz to 9 Hz at 13°C restored LG bursting; returning to 7 Hz removed that rescue.',
'Descending drive can compensate a temperature-sensitive local circuit. The intact-animal comparison supports a role for naturally changing input but does not isolate MCN1 as the only compensatory pathway in vivo. Circuit robustness depends on the nervous-system components retained by the experimental preparation.'
],[
'The MCN1 recordings were made from the remaining nerve connected to its cell-body ganglion, so the measured firing was not inferred from LG output.',
'The controlled rescue changed stimulation frequency while holding the elevated STG temperature fixed.',
'The intact recordings and isolated stimulation experiments answer complementary questions: whether the rhythm survives in the animal, and whether stronger MCN1 drive can restore it in a defined circuit state.'
],anatomy='S15_net')
add('CabTRP Ia can rescue the rhythm with continuing input','S15_7A',[
'Städele and colleagues applied 1 μM CabTRP Ia to the warmed crab STG. CabTRP Ia is a peptide cotransmitter of MCN1: **cotransmission** means that one neuron supplies more than one chemical signal. The peptide can strengthen the modulatory influence received by LG without increasing the imposed axonal stimulus frequency.',
'At 13°C, 7 Hz MCN1 stimulation alone failed to sustain LG bursts in the published example. CabTRP Ia together with continuing stimulation restored rhythmic bursting. Peptide application without the accompanying stimulation did not fully recreate that recovered rhythm, and washout removed the rescue.',
'The peptide and remaining MCN1 actions jointly maintained the effective drive needed for oscillation. Activation of I_MI can counteract the temperature-associated loss of membrane responsiveness; the authors’ conductance model supports that explanation. The rescue recording itself does not identify every intervening signaling molecule or exclude additional MCN1 mechanisms.'
],[
'The same neuron can release signals whose actions differ in time course and target, so bath application of one cotransmitter need not reproduce complete neuron stimulation.',
'The experiment included peptide alone, peptide with continued MCN1 stimulation and peptide washout while the elevated temperature was maintained.',
'The mechanistic proposal is that additional inward current offsets the increased effective leak; molecular steps linking the peptide receptor to the channel were not resolved by this rescue experiment.'
],anatomy='S15_net')
add('Fast and slow rhythms retain integer coupling','S21_5ab',[
'**Integer coupling** means that a slow rhythm’s cycle duration lies close to a whole-number multiple of a faster rhythm’s period. Powell and colleagues tested this relationship between crab gastric LG bursts and pyloric PD bursts while changing temperature from 7°C to 23°C.',
'Both rhythms accelerated, yet LG cycles remained close to integer numbers of PD cycles. In the published example, an LG cycle lasted 9.17 s with a mean PD period of 0.911 s at 7°C; at 23°C, the corresponding values were 3.44 s and 0.313 s. The integer number itself could change.',
'Coordination therefore persisted without holding either oscillator’s frequency constant. LG burst starts retained a preferred pyloric phase, whereas DG coupling was weaker. These are empirical timing relationships; they do not establish that every gastric rhythm produced by every descending input follows the same coupling rule.'
],[
'The cycle ratios in the published example are approximately ten and eleven, so integer coupling does not mean an invariant ten-to-one ratio.',
'AB inhibition of Int1 can create a brief reduction in inhibition of LG, contributing a pyloric-timed opportunity for LG burst initiation.',
'The strong contrast with the weakly driven 2015 preparation is consistent with different circuit and input states, rather than a universal temperature threshold for gastric rhythms.'
],anatomy='S21_net')
add('Circuit activity can recover after input removal','H23_2AB',[
'More-Potdar and Golowasch followed crab pyloric preparations for many hours after **decentralization**, removal of descending modulatory input. They recorded the outgoing motor rhythm over time and tested its phase relationships at different temperatures. Immediate slowing was therefore distinguished from the later state of the same circuit.',
'In the published time course, the study reported frequency recovery to approximately 75% of control and phases to within about 10% of control after approximately 24 h. Temperature tests found recovery of several phase relationships across the tested range, with incomplete recovery for some measures over the broadest range.',
'Long-term recovery supports regulation of functional output after loss of modulation. The authors propose homeostatic changes in intrinsic and synaptic properties; the experiment does not identify one uniquely responsible channel change. Near-normal baseline rhythmicity and resilience to temperature are distinct properties that require separate measurements.'
],[
'Homeostatic regulation is compensatory adjustment that tends to restore a functional property after perturbation; recovery of output does not imply restoration of the original parameter values.',
'The study compared time-matched connected and decentralized preparations, reducing confusion between recovery and the ordinary passage of time in an isolated preparation.',
'Recovery of motor-nerve output does not establish normal feeding behavior in a crab after removal of its descending inputs.'
],anatomy='H23_net')

# Balance the two experimental figures without shrinking the second recording.
slides[26]['primary_figure_height']=2.35
slides[25]['primary_figure_height']=2.35
# The complete source figure already contains the gastric anatomy.
slides[32]['figure']=slides[32].pop('figures')[0];slides[32]['layout']='figure-right'
slides[32].pop('figure_arrangement',None);slides[32].pop('primary_figure_width',None)

# These source regions include complete published panel groups to preserve labels.
FIG['M19_1BC']['caption']=f"{CITE['M19']}, Fig. 1(A–C). Published timing alternatives and recorded PD–LP latency and phase"
FIG['M19_3BC']['caption']=f"{CITE['M19']}, Fig. 3(A–F). Measured input, conductance replay and LP phase responses"
FIG['S10_1C']['caption']=f"{CITE['S10']}, Fig. 1(A–D). Frequency increases while pyloric phase remains stable"
FIG['S10_1D']['caption']=FIG['S10_1C']['caption']
FIG['S21_1b']['caption']=f"{CITE['S21']}, Fig. 1(a–d). STG anatomy, gastric and pyloric recordings and circuit connections"
FIG['G15_5']['caption']=f"{CITE['G15']}, Fig. 5(A–F). CCAP strengthens graded transmission and changes short-term synaptic dynamics"
FIG['R22_3AC']['caption']=f"{CITE['R22']}, Fig. 3(A–F). Proctolin and CCAP change LP excitability and output variability"
FIG['S21_5ab']['caption']=f"{CITE['S21']}, Fig. 5(a–c). Gastric periods remain near integer multiples of pyloric periods"
FIG['S21_1d']['caption']=f"{CITE['S21']}, Fig. 1(a–d). Gastric and pyloric circuits and their recorded interaction"
for key,panel,label in [('H87_net','1(right)','Lobster pyloric circuit'),('S10_net','2(B)','Crab pyloric circuit'),('S15_net','1(A)','Gastric circuit'),('S21_net','1(c)','Crab STG circuit'),('H23_net','1(B)','Pyloric circuit'),('G15_3A','3(A)','Crab foregut anatomy'),('D18_net','1(C)','Pyloric circuit')]:
    FIG[key]['caption']=f"{CITE[key.split('_')[0]]}, Fig. {panel}. {label}"
# Rebind caption objects after the source-region descriptions are finalized.
for sd in slides:
    for fig in ([sd['figure']] if 'figure' in sd else sd['figures']):
        fig.update(FIG[Path(fig['path']).stem])
# The complete first published figure supplies both anatomy and recordings.
slides[0].pop('figures');slides[0].pop('figure_arrangement');slides[0].pop('primary_figure_width');slides[0]['layout']='figure-right';slides[0]['figure']=FIG['S21_1b']
# Explicit anatomy accompanies classic muscle-response work as a foregut comparison.
slides[13]['transcript'][0][1].append('The anatomical localization in Garcia and colleagues is from the crab; the transmitter and muscle experiments discussed here are from the spiny lobster.')
assert len(slides)==44, len(slides)
allrefs=list(dict.fromkeys(r for sd in slides for r in sd['refs']))
spec={'lecture':7,'theme':'slate-dusty-rose','content_slides':44,'title_image':{'path':'figures/jonah-crab-noaa.jpg','kind':'web','caption':'Photo: Jonah crab (Cancer borealis). Courtesy NOAA Fisheries.','credit':'National Oceanic and Atmospheric Administration, NOAA Fisheries','license':'U.S. government photograph; NOAA Fisheries permits reuse of NOAA-created photos with credit (https://www.fisheries.noaa.gov/disclaimer).','source_url':'https://www.fisheries.noaa.gov/species/jonah-crab'},'slides':slides,
 'takeaways':{'cite':'Marder (1976); Miller & Selverston (1982); Eisen & Marder (1982); Tang et al. (2010); Städele et al. (2015); Rosenbaum & Marder (2018); Powell et al. (2021)', 'refs':['References:']+allrefs, 'items':[
 {'lead':'Pacemaker and conditional bursters.','text':'Isolated AB retains spontaneous bursting; PD and several followers can express oscillations when appropriate input recruits them.'},
 {'lead':'Electrical and chemical pathways.','text':'AB and PD synchronize electrically but have different chemical outputs. An IPSP in a coupled cell can arrive indirectly through its partner.'},
 {'lead':'Transmitter and target determine action.','text':'ACh excites the lobster PD-innervated dilator muscle. Central inhibition depends on the postsynaptic ionic mechanism, not on transmitter identity alone.'},
 {'lead':'Phase depends on active synaptic timing.','text':'Inhibition, its duration and peak timing, and the neuron’s membrane currents jointly determine follower burst onset. Graded release can function without spikes.'},
 {'lead':'Modulation changes the operative mechanism.','text':'Modulators differ in target neurons and synaptic actions. Activating the same inward current does not guarantee the same spike dependence or network output.'},
 {'lead':'Robustness depends on state and timescale.','text':'Pyloric phase and gastric–pyloric coupling can survive warming. Descending drive can rescue weak gastric rhythms, and prolonged input loss can be followed by recovery.'}
 ]}}
(D/'lecture.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n')
print(f'Wrote {len(slides)} content slides, {len(allrefs)} primary references')
