"""Source-based Lecture 61. Original figures and verified references only."""
import json,re
from pathlib import Path
D=Path(__file__).resolve().parent;R=D.parents[1]
m=json.loads((D/'reference_metadata.json').read_text())
refs={}
for k,x in m.items():
 authors=', '.join(a.get('given','')+' '+a['family'] for a in x['author']);year=x['published']['date-parts'][0][0]
 refs[k]=f"{authors} ({year}). {x['title'][0]}. {x['container-title'][0]} {x.get('volume','')}: {x.get('page',x.get('article-number',''))}. https://doi.org/{x['DOI']}"
cites={'spatial':'López et al. (2003a)','reversal':'López et al. (2003b)','pyramidal':'Crockett et al. (2015)','scratch':'Morris et al. (2024)','contacts':'Bannatyne et al. (2020)'}
F={}
def fig(key,paper,num,what):F[key]={'path':'figures/'+key+'.png','kind':'article','caption':cites[paper]+', Fig. '+num+'. '+what,'source_url':'https://doi.org/'+m[paper]['DOI']}
fig('spatial_training','spatial','1','Place learning before and after medial-cortex lesions.')
fig('mc','spatial','2','Medial cortex and reconstructed lesion extent.')
fig('histology','spatial','3A–C','Medial-cortex anatomy and lesion histology.')
fig('probes','spatial','4','Place-task performance when landmarks or starts change.')
fig('paths','spatial','5','Original search paths from novel starting positions.')
fig('cue','spatial','6','Cue learning before and after medial-cortex lesions.')
fig('cueprobes','spatial','7','Cue-guided choices during landmark and beacon tests.')
fig('reversal','reversal','1A–B','Spatial and cue acquisition followed by reversal.')
fig('cortex','pyramidal','1A–B','Published comparison of six-layer and three-layer cortex.')
fig('microcircuit','pyramidal','1B','Published anatomy of three-layer dorsal cortex.')
fig('recording','pyramidal','2','Published whole-cell recording preparation.')
fig('ap','pyramidal','3A–B','Definitions of action-potential and afterpotential measurements.')
fig('types','pyramidal','6','Physiological properties of the two pyramidal-neuron types.')
fig('spikes','pyramidal','7A','Current-evoked firing and physiological cell types.')
fig('visual','pyramidal','8A–C','Eye-attached preparation and light-evoked cortical responses.')
fig('network','pyramidal','9A–C','The authors’ network simulation and connection-dependent responses.')
fig('multifunction','scratch','1A–D','One neuron active during swimming and pocket scratching.')
fig('specialized','scratch','2A–D','Scratch-specialized activity and swimming inhibition.')
fig('phase','scratch','5A–D','A neuron changes its hip-flexor phase preference between behaviors.')
fig('flexion','scratch','6A–E','Flexion-reflex activity and inhibition during rhythmic patterns.')
fig('swim','scratch','9A–E','Swim-specialized responses and inhibition during scratching.')
fig('cpganatomy','contacts','1','Spinal locations of recorded interneuron types.')
fig('excitatory','contacts','2A–E','Reconstructed excitatory multifunctional interneurons.')
fig('inhibitory','contacts','3A–H','Reconstructed inhibitory multifunctional interneurons.')
fig('transmitters','contacts','4A–G','Recorded neurons, axon reconstructions and transmitter-associated labeling.')
fig('motoneuron','contacts','5A–C','Putative inhibitory interneuron contacts on motoneurons.')
fig('scratchcontacts','contacts','7A–E','Scratch-specialized neurons and excitatory terminal labeling.')
fig('reflexcontacts','contacts','8A–C','Scratch-specialized terminals near motoneuron somata.')
fig('traits','pyramidal','7A–B','Current responses and the combined physiological profiles.')
fig('resistance','pyramidal','6','Original input-resistance distributions for the two cell types.')
fig('resting','pyramidal','6','Original resting-voltage distributions for the two cell types.')
fig('timeconstant','pyramidal','6','Original membrane-time-constant distributions for the two cell types.')
slides=[]
def add(title,keys,papers,text):
 body=text.strip().split('\n\n');assert len(body)==3,title
 transcript=[]
 for p in body:
  sentences=re.split(r'(?<=[.!?])\s+',re.sub(r'\*\*|_', '',p));transcript.append([sentences[0],sentences[1:]])
 fs=[F[k] for k in keys];s={'layout':'figures-right' if len(fs)>1 else 'figure-right','title':title,'body':body,'transcript':transcript,'cite':'; '.join(cites[p] for p in papers),'refs':[refs[p] for p in papers]}
 if len(fs)==1:s['figure']=fs[0]
 else:s['figures']=fs;s['primary_figure_height']=2.25
 slides.append(s)
add('Turtles learn the location of hidden food',['spatial_training'],['spatial'],'''
Red-eared slider turtles learned to locate food in a 2 m by 2 m aquatic arena. Four raised feeders occupied different positions, but only one contained food. **Place learning** means learning a goal’s location from information about the surrounding environment rather than following a marker attached to the goal.

The rewarded position stayed constant relative to the experimental room. The arena was rotated between sessions, preventing an animal from solving the problem by following a fixed mark on its wall. Room landmarks therefore supplied stable information while local apparatus features changed orientation.

With training, turtles made fewer incorrect feeder choices and reached food sooner. Animals rewarded at randomly changing locations retained poorer performance. A stable relationship between environmental information and reward supported efficient search.
''')
add('Random reward locations prevent efficient place search',['spatial_training'],['spatial'],'''
A turtle approaching a feeder could potentially use food odor instead of remembering its position. López and colleagues tested this possibility with a control procedure in which the baited feeder occupied a randomly selected location. Food remained available, but yesterday’s rewarded place no longer predicted today’s reward.

These controls continued making more errors and taking longer to locate food than animals trained with a fixed rewarded location. The procedure preserved the food itself while removing a consistent spatial relationship between the room and the goal.

The difference links improved search to learned environmental information. The fixed-location animals progressively approached the correct feeder with fewer detours, whereas random-location animals had to keep searching among alternatives. Reward consistency changed the organization of their behavior.
''')
add('The medial cortex occupies the pallial forebrain',['mc','histology'],['spatial'],'''
The **medial cortex** is a cortical region along the medial side of the turtle forebrain. The **pallium** is the forebrain territory containing cortical structures; medial cortex belongs to this territory. In the lesion study, anatomical sections distinguished medial cortex from dorsal cortex and the dorsal ventricular ridge.

Coronal sections, which cut across the brain from side to side, located the damaged tissue at successive forebrain levels. The reconstructed lesions removed between 51% and 90% of medial cortex in the place-learning experiment. Anatomical verification linked each animal’s behavioral outcome to its actual tissue damage.

The normal and lesioned sections retained recognizable neighboring landmarks. Comparing these sections localized the intervention within a forebrain containing several distinct cortical and subcortical territories, rather than treating the turtle brain as one undifferentiated structure.
''')
add('Medial-cortex damage disrupts a learned place',['spatial_training','histology'],['spatial'],'''
Turtles first learned the rewarded location, then received medial-cortex lesions or **sham operations**, surgical controls that preserved the target tissue. This sequence tested retention of an already learned place rather than simply comparing animals with different amounts of training.

After surgery, lesioned turtles made more errors and took longer to find food than they had before surgery. Sham-operated turtles maintained their earlier performance. Both groups returned to the same task, with the same room cues and rewarded feeder position.

Additional training improved the lesioned animals’ performance until it approached the sham group’s level. Recovery of accurate choices created a second question: whether the animals had recovered their former navigational strategy or learned a different way to reach the same goal.
''')
add('Relearning can restore accuracy with a changed strategy',['probes','histology'],['spatial'],'''
A correct feeder choice can arise through different learning strategies. A turtle may recognize relationships among several landmarks or simply approach a particular visible landmark near food. The place-learning study tested these alternatives after lesioned animals had regained accurate performance.

**Probe trials** are tests that alter information used during training to reveal what controls a learned response. The investigators hid room cues, moved cues, or changed starting positions. Feeders were unbaited during probes, keeping newly available food from directing the animal’s choice.

Sham and lesioned turtles responded differently to partial landmark removal and novel starts despite comparable retrained accuracy. Their behavior therefore depended on different environmental information. Relearning the same rewarded choice had changed the organization of spatial control.
''')
add('Removing all landmarks disrupts both groups',['probes'],['spatial'],'''
In the all-room concealed test, gray curtains surrounded the arena and blocked the distal visual cues used during training. **Distal cues** are landmarks outside the immediate goal apparatus, such as features distributed around the room. The physical feeders and water arena remained available.

Both sham-operated and medial-cortex-lesioned turtles made more errors when the entire room was concealed. Even animals that had relearned the task after a lesion depended on visual information outside the feeders. Removing that information degraded goal recognition in both groups.

This shared dependence explains why recovered accuracy did not amount to random searching or exclusive reliance on food-related cues. The groups both used the visual environment, but subsequent partial-concealment tests separated their ways of using that environment.
''')
add('Intact turtles use landmarks beyond the goal vicinity',['probes','histology'],['spatial'],'''
The half-room concealed test hid the room landmarks near the rewarded location while leaving landmarks on the opposite side visible. Sham-operated turtles continued reaching the trained goal accurately. They could use information distributed beyond the immediate neighborhood of the feeder.

Medial-cortex-lesioned turtles made more errors under this manipulation. When the opposite half of the room was concealed instead, leaving goal-side landmarks visible, both groups searched accurately. The direction of concealment mattered because it changed which learned landmarks remained accessible.

These complementary tests connect medial cortex to flexible use of distributed spatial information. The intact animals could reach a location from a partial set of room cues, whereas lesioned animals depended more strongly on cues close to the goal.
''')
add('A novel start exposes inflexible navigation',['paths','histology'],['spatial'],'''
During ordinary training, turtles began at the center of the arena. In the novel-start tests, they began from its corners. This change altered the direction and route needed to reach the same rewarded place while preserving the room’s visual landmarks.

Sham-operated turtles followed efficient paths toward the trained goal from the new positions. Medial-cortex-lesioned turtles made additional errors and searched less directly. The published tracks retain the actual paths, start markers and rewarded location recorded during these tests.

A fixed movement sequence from the familiar start would become inappropriate from a corner. Successful transfer required selecting a route suited to the new position. The lesion effect therefore links medial cortex to navigation that adjusts when the animal’s starting relationship to its surroundings changes.
''')
add('Moving room cues changes place-task choices',['probes'],['spatial'],'''
Cue transposition moved relevant room landmarks while the physical arena remained in place. **Transposition** means changing the arrangement of cues that previously predicted a goal. This test disrupted learned relationships between the visual environment and the rewarded position rather than concealing the room altogether.

Both sham-operated and medial-cortex-lesioned turtles made more errors during cue-transposition probes. Their trained choices depended on the room information in its learned arrangement. Altering that arrangement disturbed the guidance available to both groups.

Together with curtain tests, transposition distinguishes a visual spatial task from simply detecting an accessible feeder. The room supplied behaviorally effective information, and changing its organization changed search. Partial-cue and novel-start tests then identified the additional flexibility supported by intact medial cortex.
''')
add('A goal beacon supports preserved cue learning',['cue','histology'],['spatial'],'''
**Cue learning** associates reward with a directly identifiable stimulus rather than with a fixed place. In the second experiment, a visible intramaze cue identified the rewarded feeder, while the feeder’s location changed. **Intramaze** means inside the experimental apparatus, close to the available choices.

Turtles learned to approach the marked feeder, reducing errors and search time during training. After medial-cortex lesions or sham operations, both groups continued finding the cued feeder effectively. The spatial-learning impairment from the first experiment therefore occurred alongside preserved performance in this cue-guided task.

The beacon remained useful despite changing goal locations. Approaching it required learning a cue–reward relationship that could be applied wherever the marker appeared, providing a different behavioral solution from remembering a position in the room.
''')
add('Cue-guided turtles tolerate hidden room landmarks',['cueprobes'],['spatial'],'''
Turtles trained with a goal beacon were tested while all room landmarks or selected halves of the room were concealed. Unlike the place task, their relevant training information stayed beside the feeder. Curtains changed the surroundings while preserving the directly rewarded cue.

Both sham-operated and medial-cortex-lesioned animals continued choosing the cued feeder under these concealment conditions. Their choices relied on the intramaze stimulus rather than requiring the distal landmark arrangement used by place-trained animals.

When the goal-associated cue itself was deleted, performance deteriorated in both groups. The two manipulations identify the effective information: hiding the room preserved cue-guided behavior, whereas removing the learned beacon removed the stimulus controlling that behavior. Spatial and cue tasks recruited different learned relationships.
''')
add('Reversal changes which previously learned choice pays',['reversal'],['reversal'],'''
**Reversal learning** changes the reward rule after an animal has mastered the original rule. López and colleagues trained turtles in a four-arm maze using two accessible goal arms. Depending on the starting arm, reaching the rewarded location required a left or right turn.

In the place procedure, the rewarded arm occupied a stable position relative to room landmarks. In the cue procedure, a red panel identified food and moved between possible goal arms. Both lesioned and sham-operated turtles acquired their initial tasks accurately.

Reversal moved the rewarded place to the opposite arm or made the formerly rewarded panel identify the empty arm. Animals now had to replace an established choice rule. The initial drop in accuracy reflected persistence of the old learned relationship when reward contingencies changed.
''')
add('Medial cortex supports flexible spatial reversal',['reversal','histology'],['reversal','spatial'],'''
After the rewarded place switched, sham-operated turtles learned to approach its new location. Medial-cortex-lesioned turtles continued making **perseverative errors**, repeated choices that follow a formerly correct rule after that rule has become inappropriate. Their behavior remained biased toward the previously rewarded place.

The lesion group improved with training but failed to reach the acquisition criterion during 30 reversal sessions. Initial acquisition had been successful, so the impairment emerged when an established spatial relationship had to be reorganized rather than when animals first learned to choose an arm.

The same experimental framework preserved cue reversal after medial-cortex damage. Spatial flexibility and cue-based adjustment therefore separated within the turtle’s behavioral repertoire, linking the medial cortical contribution specifically to updating place-guided choices.
''')
add('Multiple memory systems guide turtle choices',['cue','histology'],['spatial','reversal'],'''
Turtles can solve a food-search problem by locating a place within a landmark configuration or approaching a rewarded cue. The place and cue experiments demonstrate these alternatives using distinct reward rules, followed by lesions and targeted changes to available information.

Medial-cortex damage disrupted place retention, transfer from novel starts, and spatial reversal. Cue-guided learning and cue reversal remained effective. These outcomes separate a memory system supporting flexible spatial relationships from learning that directly associates a stimulus with reward.

The authors propose functional correspondence between turtle medial cortex and the hippocampal formation of mammals and birds. This is a hypothesis about conserved spatial-learning functions, grounded in the behavioral dissociation. The turtle experiments measured goal choices and search paths rather than hippocampal-style place-cell firing.
''')
add('Turtle dorsal cortex has three organized layers',['microcircuit'],['pyramidal'],'''
The **dorsal cortex** is a visual cortical region of the turtle pallium. Its three-layer organization contains a densely packed middle layer of neuronal cell bodies between two layers rich in processes. **Neuropil** is tissue dominated by dendrites, axons and their connections rather than densely packed somata.

The middle layer contains **pyramidal neurons**, principal neurons with branching dendrites that receive synaptic inputs. **Dendrites** are the receiving processes of a neuron, and the **soma** is its cell body. The surrounding layers provide space for inputs and interactions among cortical cells.

Crockett and colleagues studied this organized tissue rather than isolated cells detached from their cortical surroundings. Their recordings connect intrinsic electrical properties with responses generated while neurons remain embedded in the three-layer circuit.
''')
add('Three layers retain a differentiated visual circuit',['cortex'],['pyramidal'],'''
The published anatomical comparison places six-layer mammalian neocortex beside three-layer turtle dorsal cortex. **Neocortex** is the six-layer cortical organization characteristic of mammals; the turtle visual cortex concentrates principal-cell somata within one main cellular layer instead of distributing them across several layers.

Turtle layers above and below that cellular layer contain extensive dendrites and axons. **Interneurons**, neurons participating in local circuit interactions, occur among these processes as well as elsewhere in the circuit. A smaller number of layers still supports differentiated inputs and cellular interactions.

The comparison focuses attention on circuit organization rather than counting layers as a measure of behavioral capacity. Turtle visual responses arise from principal cells receiving external inputs and recurrent cortical inputs within an anatomically simpler laminar arrangement.
''')
add('Thalamic input meets recurrent cortical connections',['microcircuit'],['pyramidal'],'''
The turtle dorsal cortex receives visual input from the **lateral geniculate nucleus**, a thalamic relay in the visual pathway. The **thalamus** is a forebrain region that relays sensory information to cortical targets. Geniculate fibers contact the distal portions of pyramidal-neuron apical dendrites.

**Apical dendrites** extend from the soma toward the outer cortical layer; basal dendrites branch closer to the cell body. A pyramidal neuron also receives extensive contacts from other cortical pyramidal neurons and interneurons. These recurrent connections return activity through the local network.

A visually driven cortical response therefore combines input arriving through the sensory pathway with activity circulating among cortical neurons. This anatomical convergence motivated testing whether a neuron’s intrinsic electrical type predicts its response to the same brief retinal stimulus.
''')
add('Whole-cell recordings measure cortical voltage',['recording'],['pyramidal'],'''
**Whole-cell recording** places an electrode in electrical continuity with the interior of a neuron, allowing measurement of its membrane potential. **Membrane potential** is the voltage difference across the cell membrane. Crockett and colleagues recorded cells from the densely packed cellular layer of turtle dorsal cortex.

The preparation exposed the ventricular surface of the cortex, allowing visually guided placement of a recording pipette at a cell body. **Current clamp** means injecting a controlled electrical current while recording how the neuron’s voltage responds rather than holding voltage at a chosen value.

The measured voltage traces reveal resting potential, action potentials and slower voltage changes. Because the neuron remains in cortical tissue, the experiment can compare its response to injected current with the activity it receives from the surrounding circuit.
''')
add('Injected current separates intrinsic response properties',['spikes','microcircuit'],['pyramidal'],'''
A controlled current pulse tests how a neuron transforms electrical input into voltage changes and spikes. The investigators applied 1-second pulses, separated by at least 2 seconds, and characterized the resulting responses. **Intrinsic properties** are features of the cell’s own electrical responsiveness, measured here with somatic current injection.

**Depolarization** makes membrane voltage less negative, bringing the cell toward spike initiation. **Hyperpolarization** makes it more negative. Both types of current pulses contributed measurements, separating voltage responsiveness below spike threshold from the firing patterns produced above it.

The recorded cells differed in these responses despite occupying the same densely packed cortical layer. Visible anatomical position alone therefore concealed physiological diversity that became apparent when neurons received the same controlled kind of electrical input.
''')
add('Rheobase identifies the current needed for a spike',['ap','microcircuit'],['pyramidal'],'''
An **action potential** is a brief regenerative electrical event used by neurons to transmit activity. In the cortical recordings, **rheobase** was the lowest injected current that elicited an action potential in three consecutive trials. It measures excitability under a specified stimulation protocol.

The investigators began with hyperpolarizing pulses and increased injected current in 10 pA steps. A **picoampere**, abbreviated pA, is a unit of electrical current. Crossing from subthreshold voltage responses to a spike identified the current level required to activate that cell under these conditions.

Cells with different resting voltages and input resistances can require different injected currents to reach firing. Rheobase consequently complements measurements of voltage and firing pattern when comparing physiological cell types within the same cortical tissue.
''')
add('Input resistance describes voltage responsiveness',['resistance','microcircuit'],['pyramidal'],'''
**Input resistance** describes how strongly a neuron’s membrane voltage changes in response to injected current. Crockett and colleagues measured it from voltage drops during 1-second hyperpolarizing pulses. A larger resistance means a given current produces a larger voltage response under the recording conditions.

The two identified pyramidal-cell types differed in this property. Their reported mean input resistances were approximately 423 MΩ for type A and 271 MΩ for type B. **Megaohms**, abbreviated MΩ, are the resistance units used for these neuronal measurements.

This difference changes the electrical impact of a current delivered to the soma. Combined with resting potential and adaptation, input resistance contributed to distinguishing cells that appeared similar within the cortical layer but transformed injected electrical input differently.
''')
add('Resting voltage contributes to cell-type differences',['resting','microcircuit'],['pyramidal'],'''
**Resting membrane potential** is the membrane voltage measured without an imposed depolarizing stimulus. In these cortical recordings, type A neurons had a reported mean near −53 mV, whereas type B neurons rested near −66 mV. A **millivolt**, abbreviated mV, measures the small voltage differences involved in neuronal activity.

The more negative resting voltage of type B changed its starting position relative to spike threshold. The authors measured this resting value alongside resistance and firing adaptation rather than classifying neurons from one voltage measurement alone.

The distinction places cellular diversity within a shared anatomical layer. Two cells receiving the same injected current can begin at different voltages and undergo different voltage changes, making their spike patterns differ even before differences in incoming circuit activity are considered.
''')
add('Membrane time course shapes responses to current',['timeconstant','microcircuit'],['pyramidal'],'''
The **membrane time constant** describes how rapidly voltage approaches its changed level during a sustained current input. Crockett and colleagues measured the voltage time course during hyperpolarizing pulses, adding a temporal property to the resistance and resting-voltage measurements.

Their reported mean time constants were approximately 198 ms for type A and 121 ms for type B. **Milliseconds**, abbreviated ms, measure the speed of these cellular responses. The types therefore differed both in the size of voltage changes and in how those changes developed over time.

A neuron’s response to an input has an amplitude and a duration, not merely a decision to spike or remain silent. The measured time constants contribute to the physiological profiles distinguishing the two cortical cell types.
''')
add('Spike-frequency adaptation changes sustained firing',['spikes','microcircuit'],['pyramidal'],'''
**Spike-frequency adaptation** is a change in firing frequency during a sustained input, typically a slowing of the spike train. Crockett and colleagues compared the first interspike interval with later intervals during a depolarizing pulse. An **interspike interval** is the time separating consecutive action potentials.

Type A cells generally maintained more regular firing, whereas type B cells showed stronger adaptation. The published traces preserve the timing of successive spikes during current injection, relating cell type to the transformation of a sustained stimulus into a changing output pattern.

This difference accompanies distinct resting voltages and input resistances. The physiological profile therefore concerns both initial excitability and the ongoing response after activity has begun, separating neurons with sustained firing from neurons whose firing decreases over the same pulse.
''')
add('An afterhyperpolarization follows the action potential',['ap','microcircuit'],['pyramidal'],'''
An **afterhyperpolarization** is the voltage decrease following an action potential, when membrane potential becomes more negative after the spike. The study measured the interval from the spike’s descending threshold crossing to the deepest point of this afterpotential.

The original measurement panel also distinguishes spike height, spike width and the falling phase of the action potential. These features describe different portions of the same electrical event rather than interchangeable measures of whether a cell fired.

Timing after a spike contributes to the cell’s physiological profile alongside repeated firing during a current pulse. Recording both rapid spikes and slower afterpotentials captures electrical diversity that would be missed by counting action potentials alone, helping distinguish the two types within the cortical layer.
''')
add('Physiological diversity includes spike shape',['ap','types'],['pyramidal'],'''
The two pyramidal-neuron types differed in several features of their action potentials. Mean spike widths measured halfway between threshold and peak were approximately 2.2 ms for type A and 3.1 ms for type B. **Spike width** therefore captures the duration of an electrical event at a specified measurement level.

The authors measured spike amplitude from threshold to peak and also measured the steepness of the falling phase. These measures characterized the waveform rather than assuming that all action potentials in the layer shared one shape.

Differences in waveform accompanied stronger differences in resting voltage, resistance and adaptation. The cell types represent combinations of electrical properties; the same anatomical compartment contains neurons with distinct ways of producing and recovering from spikes.
''')
add('Two cell types emerge from combined electrical traits',['traits','microcircuit'],['pyramidal'],'''
Crockett and colleagues grouped neurons using their combined electrical profiles rather than deciding their type from one trace. Resting voltage, input resistance and adaptation provided especially clear separation. The original color-coded recordings preserve representative type A and type B firing responses.

An individual property can overlap between groups even when several properties considered together distinguish them. The combined profile therefore separated cells that could look similar under the microscope and could overlap on a single electrophysiological measurement.

These types classify responses to somatic electrical stimulation. Retinal stimulation tested whether these electrically defined types also differed in sensory responsiveness. The comparison retained active cortical connections and used the same sensory stimulus across the physiological types.
''')
add('An eye-attached preparation preserves visual input',['visual'],['pyramidal'],'''
The **eye-attached whole-brain preparation** retains the retina and its connections to the brain while allowing cortical recording. The **retina** is the neural tissue that receives light in the eye. In this preparation, the investigators exposed an eye cup and presented controlled flashes directly to the retinal surface.

The geniculocortical input pathway remained available while the dorsal cortex was unfolded to expose its recording surface. **Geniculocortical** refers to the projection linking the visual thalamic relay with cortex. This arrangement allowed a light stimulus to activate neurons through the preserved sensory pathway.

The researchers first measured each recorded cell’s current-evoked properties and then measured its light-evoked response. Cellular classification and sensory responsiveness could consequently be compared within the same neuron rather than inferred from separate preparations.
''')
add('A brief retinal flash evokes prolonged cortical activity',['visual'],['pyramidal'],'''
A 10 ms flash of 640 nm light stimulated the exposed retina. **Nanometers**, abbreviated nm, express light wavelength; 640 nm is in the red portion of the spectrum. The investigators waited 30 seconds between flashes while recording cortical membrane voltage.

Visual responses began approximately 100 ms after the flash and typically persisted for more than 1,000 ms. The cortical response therefore outlasted the sensory stimulus by a large interval. A brief retinal event recruited sustained activity in the preserved brain and cortical circuit.

The recorded responses contained broad depolarization with substantial fluctuations. Their temporal extent links sensory stimulation to continuing network activity, rather than treating cortical voltage as an instantaneous copy of the light pulse delivered to the retina.
''')
add('Excitation and inhibition combine in visual responses',['visual','microcircuit'],['pyramidal'],'''
A **postsynaptic potential** is a membrane-voltage change produced by input at a synapse, the contact through which neurons communicate. The light-evoked cortical responses contained overlapping excitatory and inhibitory postsynaptic potentials rather than a single smooth event.

**Excitatory** input tends to promote activation, whereas **inhibitory** input restrains or reshapes it. Many such inputs combined into a broad depolarization following the retinal flash. The response varied substantially across repeated presentations of the same stimulus.

The circuit’s recurrent connections provide a route for activity to continue after the initial sensory input. A recorded pyramidal neuron therefore reflects the interaction of incoming sensory drive with activity from other cortical neurons, linking its voltage trajectory to the state of the surrounding network.
''')
add('Visual input reduces the distinction between cell types',['visual','spikes'],['pyramidal'],'''
Type A and type B neurons differed clearly during controlled current injection, but their light-evoked responses were largely indistinguishable. Both types developed prolonged depolarization and large voltage fluctuations following the same brief retinal flash in the eye-attached preparation.

Response variability across trials was comparable in amplitude to the average response. A physiological classification based on resting voltage, resistance and adaptation therefore did not divide these neurons into correspondingly distinct visual-response groups under this stimulation condition.

The result connects intrinsic properties to circuit context. Cell-specific electrical traits remain measurable, while strong sensory-driven network activity produces similar response trajectories across types. The authors proposed that recurrent cortical interactions can reduce the expression of intrinsic cellular differences during sensory processing.
''')
add('The authors’ network model tests recurrent mixing',['network'],['pyramidal'],'''
Crockett and colleagues constructed a network simulation containing two excitatory neuron types and an inhibitory population. **Simulation** means a computational implementation used to test a proposed mechanism. The published model figure is reproduced directly from the paper, with its original connections and response plots.

The model delivered external input only to excitatory type A neurons, then varied connections within and between populations. Increasing interactions between groups made their population responses more similar despite differences in cellular properties and initial sensory access.

This is the authors’ hypothesis for how recurrent activity can reduce cell-type distinctions during sensory responses. The experimental observations establish similar light-evoked voltage responses; the simulation identifies a connection-dependent mechanism capable of generating that similarity in the modeled circuit.
''')
add('Spinal circuits coordinate several motor behaviors',['cpganatomy','multifunction'],['contacts','scratch'],'''
Turtles generate coordinated hindlimb activity for swimming, scratching and withdrawal. A **central pattern generator** is a neural circuit capable of organizing rhythmic motor output. The spinal experiments recorded motor nerves and individual interneurons to examine how several behaviors share spinal circuitry.

Investigators separated the spinal cord from descending brain input by transecting it between dorsal segments D2 and D3. **Transection** means cutting across the cord. Rhythmic motor patterns could still be evoked in this preparation through stimulation of appropriate pathways or skin regions.

The retained spinal cord organized patterned activity in nerves controlling hip and knee movements. Brain input is therefore not required for every cycle of these experimentally evoked patterns; spinal interactions provide substantial organization of their timing and muscle-related output.
''')
add('Skin location selects an appropriate scratch pattern',['specialized','cpganatomy'],['scratch','contacts'],'''
Mechanical stimulation of different skin regions evokes different forms of turtle scratching. A **receptive field** is the region where stimulation affects a particular sensory or motor response. The investigators used a smooth glass probe within the receptive field for each scratch form.

Motor nerve recordings distinguished hip flexion, hip extension and knee extension as the response developed. **Flexion** bends a joint, whereas **extension** straightens it or moves the limb in the opposite direction. Their relative timing organized the different scratch outputs.

The preparation was immobilized, so the recorded patterns were **fictive motor patterns**, neural output without the corresponding overt limb movement. Recording the nerves preserved the timing information needed to compare how sensory stimulation recruits different spinal motor programs.
''')
add('Multifunctional neurons participate in two rhythms',['multifunction','cpganatomy'],['scratch','contacts'],'''
A **multifunctional interneuron** increases its firing during both swimming and scratching. Morris and colleagues recorded its membrane voltage together with motor nerve activity, allowing the neuron’s spikes to be aligned with the ongoing hip and knee motor pattern.

The published example exhibits clear rhythmic voltage changes and spiking during forward swimming and pocket scratching. Activity is organized relative to successive nerve bursts rather than consisting of a simple continuous increase in firing throughout stimulation.

Participation in both behaviors connects one neuron to more than one motor pattern. The same spinal circuit can recruit overlapping neuronal populations while generating behavior-specific combinations of motor output, providing a cellular basis for shared control across the turtle’s movement repertoire.
''')
add('Scratch-specialized neurons are suppressed in swimming',['specialized','cpganatomy'],['scratch','contacts'],'''
A **scratch-specialized interneuron** increases its firing during scratching but not during swimming. In the published example, pocket scratching produced depolarization and spikes, whereas swimming drove the membrane below its prestimulation baseline.

The swimming response is **hyperpolarization**, a more negative membrane voltage. The neuron still received behavior-related input during swimming, but that input suppressed rather than recruited its firing. Behavioral specialization therefore involved selective inhibition as well as selective activation.

The contrast connects sensory and motor state to cell recruitment. A neuron can belong to an active spinal network yet contribute different outputs across behaviors because the balance of input changes. Specialized cells operate alongside multifunctional neurons rather than forming entirely isolated motor systems.
''')
add('Shared neurons can change their preferred motor phase',['phase','cpganatomy'],['scratch','contacts'],'''
**Motor phase** describes a point within the repeating cycle of a motor pattern. Morris and colleagues aligned interneuron activity to hip-flexor nerve bursts, separating the interval when the hip flexor was active from the interval between its bursts.

One multifunctional neuron fired primarily between hip-flexor bursts during forward swimming, but mainly during hip-flexor bursts in caudal scratching. The same cell therefore shifted its timing relationship to the hip pattern when the behavior changed.

Its firing tended to occur when the knee extensors were inactive in both behaviors. A shared cell’s relationship to one motor output can remain similar while its relationship to another changes. Behavioral coordination depends on the combination of phase relationships across the participating nerves.
''')
add('Flexion-reflex neurons withdraw the limb selectively',['flexion','cpganatomy'],['scratch','contacts'],'''
The **flexion reflex** withdraws a limb following an appropriate sensory stimulus. Investigators evoked it with a tap or electrical stimulation of the dorsal foot while recording spinal neurons and motor nerves. Flexion-reflex-selective neurons increased firing during this response.

The published example fired following the withdrawal stimulus but was hyperpolarized during swimming and scratching. Its membrane trajectory distinguished the reflex-associated activation from the inhibition received during rhythmic motor behaviors.

Selective recruitment preserves a different behavioral output within the same spinal cord. Sensory stimulation can trigger withdrawal without requiring that every neuron involved in rhythmic swimming or scratching adopt the same activity pattern. Shared circuitry includes cells preferentially recruited for particular responses.
''')
add('Swim-specialized activity includes fast sensory responses',['swim','cpganatomy'],['scratch','contacts'],'''
The 2024 study recorded a **swim-specialized neuron**, a neuron activated during swimming rather than scratching. Its swimming response included tonic activation, meaning activity sustained without a strong rhythmic voltage oscillation across the motor cycle.

Individual stimuli used to evoke swimming triggered a postsynaptic potential and usually a spike at a latency of approximately 20 ms. **Latency** is the elapsed time from a stimulus to its response. This fast response connected activation of the stimulating pathway to excitation of the recorded cell.

Rostral scratching strongly inhibited the neuron. Some subsequent spikes followed release from inhibition, termed **postinhibitory rebound**. The example separates sustained recruitment for swimming from the voltage suppression and rebound that can occur when another motor behavior occupies the circuit.
''')
add('Recorded behavior can be linked to axon anatomy',['transmitters'],['contacts'],'''
Bannatyne and colleagues combined intracellular recordings with neuronal labeling and anatomical reconstruction. **Axons** are neuronal processes that carry output toward other cells, and **axon terminals** are the endings where that output is delivered. Labeling connected a recorded response with the same cell’s anatomical projections.

Reconstructed multifunctional interneurons projected within the spinal cord, sometimes into the opposite side. **Contralateral** means opposite to the recorded soma; **ipsilateral** means on the same side. These projections provide anatomical routes through which one interneuron can influence local and bilateral circuitry.

The investigators then examined terminal-associated proteins to classify likely transmitter function. Electrophysiology, reconstruction and molecular labeling linked what the cell did during motor behavior with where its output traveled and what kind of synaptic action it was associated with.
''')
add('Glutamatergic terminals support excitatory output',['transmitters'],['contacts'],'''
**Glutamate** is a neurotransmitter associated with excitatory synaptic transmission. A **neurotransmitter** is a chemical signal released by neurons to affect other cells. Bannatyne and colleagues used labeling associated with glutamatergic terminals to identify excitatory spinal interneurons.

**VGLUT2**, vesicular glutamate transporter 2, packages glutamate into synaptic vesicles. **Homer** is a postsynaptic protein used in the study as a marker associated with excitatory synapses. Labeled interneuron terminals were compared with these markers in thin optical sections.

Some multifunctional cells carried excitatory terminal-associated labeling and projected toward motor regions. Shared participation in swimming and scratching therefore includes excitatory output pathways, linking the activity of behaviorally shared neurons to anatomical connections capable of promoting downstream activation.
''')
add('Gephyrin-associated contacts identify inhibitory output',['transmitters','inhibitory'],['contacts'],'''
**GABA**, gamma-aminobutyric acid, and **glycine** are neurotransmitters associated with inhibition in these spinal circuits. Bannatyne and colleagues identified inhibitory contacts using terminal relationships with **gephyrin**, a postsynaptic scaffolding protein associated with GABAergic and glycinergic synapses.

The original fluorescent panels retain labeled axon terminals and neighboring synaptic-protein signals. Close association of a terminal with gephyrin supported classification of that cell’s output as inhibitory. This labeling distinguished inhibitory multifunctional interneurons from glutamatergic multifunctional interneurons.

The gephyrin method grouped GABAergic and glycinergic output together rather than assigning a specific one of those transmitters to every cell. The broader inhibitory identity still connects the recorded neuron’s behavioral participation with a pathway capable of restraining activity in its postsynaptic targets.
''')
add('Shared interneurons can contact motoneurons directly',['motoneuron'],['contacts'],'''
A **motoneuron** is a neuron whose axon carries output to muscle. Bannatyne and colleagues identified motoneurons with labeling for **ChAT**, choline acetyltransferase, the enzyme synthesizing acetylcholine. **Acetylcholine** is the transmitter associated with motoneuron output to skeletal muscle.

Labeled boutons from a multifunctional interneuron lay closely against motoneuron somata or dendrites. A **bouton** is a small terminal swelling along an axon. Associated gephyrin labeling supported inhibitory identity for the reconstructed interneuron contacts in the published example.

These putative contacts provide a direct anatomical route from behaviorally shared interneuron activity to motor output. The anatomical evidence is close apposition with synaptic markers; it identifies likely connectivity while preserving the distinction between reconstructed contact and a directly recorded synaptic effect.
''')
add('Specialized and shared pathways act within one cord',['scratchcontacts','reflexcontacts'],['contacts','scratch'],'''
Scratch-specialized interneurons included excitatory and inhibitory cells, just as multifunctional interneurons did. Some specialized axons projected toward motor regions, while others extended through spinal territories containing additional interneurons. Behavioral specialization therefore did not determine a single transmitter identity or projection pattern.

The original labeled examples connect scratch-associated firing with reconstructed axons and terminal-associated proteins. Other experiments recorded inhibition of specialized neurons when swimming occupied the circuit. Both anatomical connectivity and behavior-dependent input contribute to deciding which cells are active.

Shared rhythmic organization and specialized recruitment coexist in the turtle spinal cord. Sensory conditions can favor scratching, swimming or withdrawal by changing which neurons fire and when they fire, while overlapping neuronal populations maintain substantial participation across motor behaviors.
''')
for sl in slides:
 if sl.get('figures') and sl['figures'][0]['path'] in ['figures/ap.png','figures/traits.png']:
  sl['primary_figure_height']=3.3
assert len(slides)==44,len(slides)
photo={'path':'figures/animal.jpg','kind':'web','caption':'Photo: Red-eared slider, the experimental turtle.','credit':'Kat B via iNaturalist','license':'CC BY 4.0','source_url':'https://www.inaturalist.org/observations/407129368'}
items=[('Spatial information','Turtles use room landmarks to locate food; hiding, moving or selectively removing landmarks changes their search.'),('Medial cortex','Medial-cortex damage impairs flexible place navigation and spatial reversal while preserving cue-guided learning.'),('Cortical organization','Three-layer dorsal cortex combines thalamic visual input with extensive recurrent cortical connections.'),('Cell and circuit','Pyramidal-neuron types differ during current injection but have largely similar prolonged responses to brief retinal flashes.'),('Motor selection','Spinal circuits recruit multifunctional and specialized neurons differently during swimming, scratching and withdrawal.'),('Output pathways','Shared and specialized interneurons include excitatory and inhibitory outputs, with putative direct contacts on motoneurons.')]
s={'lecture':61,'theme':'muted-clay-paper','content_slides':44,'title_height':2.5,'title_image':photo,'title_refs':[refs['spatial']],'slides':slides,'takeaways':{'items':[{'lead':a,'text':b} for a,b in items],'cite':'López et al. (2003a,b); Crockett et al. (2015); Bannatyne et al. (2020); Morris et al. (2024)','refs':list(refs.values())}}
(D/'lecture.json').write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
(D/'REFERENCES.md').write_text('# Lecture 61 verified references\n\n'+'\n\n'.join(refs.values())+'\n')
(D/'PLAN.md').write_text('# Lecture 61 content plan\n\n'+'\n'.join(f'{n}. {x["title"]}' for n,x in enumerate(slides,2))+'\n\n46. Key takeaways\n')
for n,x in enumerate(slides,2):print(n,len(re.findall(r'\b\S+\b',' '.join(x['body']))),x['title'])
