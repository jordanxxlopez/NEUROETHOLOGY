"""Lecture 80, written against the four supplied primary articles."""
import json,re
from pathlib import Path
D=Path(__file__).resolve().parent;R=D.parents[1]
refs={
'spines':'Roberts TF, Tschida KA, Klein ME, Mooney R (2010). Rapid spine stabilization and synaptic enhancement at the onset of behavioural learning. Nature 463:948–952. https://doi.org/10.1038/nature08759',
'motor':'Roberts TF, Gobes SMH, Murugan M, Ölveczky BP, Mooney R (2012). Motor circuits are required to encode a sensory model for imitative learning. Nature Neuroscience 15:1454–1459. https://doi.org/10.1038/nn.3206',
'dopamine':'Tanaka M, Sun F, Li Y, Mooney R (2018). A mesocortical dopamine circuit enables the cultural transmission of vocal behaviour. Nature 563:117–120. https://doi.org/10.1038/s41586-018-0636-7',
'inception':'Zhao W, Garcia-Oscos F, Dinh D, Roberts TF (2019). Inception of memories that guide vocal learning in the songbird. Science 366:83–89. https://doi.org/10.1126/science.aaw4226'}
short={'spines':'Roberts et al. (2010)','motor':'Roberts et al. (2012)','dopamine':'Tanaka et al. (2018)','inception':'Zhao et al. (2019)'}
dois={k:v.split('https://doi.org/')[1] for k,v in refs.items()}
figinfo={
'motor_2ab':('2(a–b)','Viral expression and HVC histology.'),'motor_2ef':('2(e–f)','Adult songs after HVC disruption during tutoring.'),
'inception_1':('1(A–C)','Song development and auditory–motor pathways.'),'inception_2ac':('2(A–C)','Labeled NIf terminals and glutamatergic currents in HVC.'),'inception_2df':('2(D–F)','Excitatory and suppressive responses to terminal stimulation.'),'inception_2hl':('2(G–L)','Projection specificity and absence of antidromic recruitment.'),'inception_3':('3(A–G)','Optical pulse duration and adult song-element duration.'),'inception_3ad':('3(A–D)','Short-pulse tutoring and short adult song elements.'),'inception_3eg':('3(E–G)','Long-pulse tutoring and long adult song elements.'),'inception_4':('4(A–B)','Developmental trajectories after short and long optical tutoring.'),'inception_4a':('4(A)','Short-element song develops after 50-ms tutoring.'),'inception_4b':('4(B)','Long-element song develops after 300-ms tutoring.'),'inception_5':('5(A–E)','Optical tutoring competes with natural tutor experience.'),'inception_6':('6(A–C)','Pathway lesions before and after tutor-song acquisition.'),
'motor_1':('1(a–c)','Sensory learning and the song circuit.'),'motor_1b':('1(b)','Auditory inputs and vocal premotor circuitry.'),'motor_2':('2(a–f)','Tutor-contingent HVC disruption impairs imitation.'),'motor_3':('3(a–c)','Syllable-contingent HVC stimulation selectively impairs copying.'),'motor_4':('4(a–e)','NMDA blockade, spine size, and song imitation.'),'motor_4b':('4(b)','A stable HVC spine before and after NMDA blockade during tutoring.'),'motor_4de':('4(d–e)','NMDA blockade during tutoring impairs adult copying.'),'motor_5':('5(a–g)','NIf lesions, reversible blockade, and timed stimulation.'),
'spines_1':('1(a–d)','HVC localization and repeated dendritic-spine imaging.'),'spines_1a':('1(a)','HVC anatomy, labeled neurons, and imaging schedule.'),'spines_1bc':('1(b–d)','Stable dendritic branches and individual spine turnover.'),'spines_2':('2(a–b)','Age, spine turnover, and subsequent song imitation.'),'spines_3':('3(a–e)','Spine stabilization, accumulation, and early vocal changes.'),'spines_3ab':('3(a–b)','Spine turnover falls after the tutor begins singing.'),'spines_3cd':('3(c–e)','New persistent spines, density, and early vocal change.'),'spines_4':('4(a–c)','Stable-spine enlargement after tutoring.'),'spines_4a':('4(a)','The same stable spines before and after tutoring.'),'spines_5':('5(a–b)','Intracellular depolarizing synaptic activity after tutoring.'),
'dopamine_1':('1(a–k)','PAG anatomy and responses during live tutoring.'),'dopamine_1abc':('1(a–c)','Dopaminergic PAG neurons project to HVC.'),'dopamine_1dk':('1(d–k)','PAG activity depends on the live singing tutor.'),'dopamine_2':('2(a–i)','Dopamine-sensor fluorescence during tutoring and controls.'),'dopamine_3':('3(a–j)','Dopamine lesions, receptor blockade, and optical rescue.'),'dopamine_3ad':('3(a–f)','Dopamine fibers and age-dependent effects of lesions.'),'dopamine_3gh':('3(g–h)','Receptor blockade during and after tutoring.'),'dopamine_3ij':('3(i–j)','PAG-terminal stimulation paired with song playback.'),'dopamine_4':('4(a–i)','Rapid neural and vocal changes after social tutoring.')}
def fig(name):
 k=name.split('_')[0];n,t=figinfo[name];return {'path':f'figures/{name}.png','kind':'article','caption':f'{short[k].replace(" et al.","")}, Fig. {n}. {t}','source_url':'https://doi.org/'+dois[k]}
slides=[]
def add(title,key,image,paras,anatomy=None,extra=None):
 body=paras.strip().split('\n\n');assert len(body)==3;assert '—' not in title+paras
 image={'spines_3ab':'spines_3','spines_3cd':'spines_3'}.get(image,image)
 if image=='motor_2':image='motor_2ef';anatomy='motor_2ab'
 fs=[fig(image)];keys=[key]
 if anatomy and anatomy!=image:fs.append(fig(anatomy));keys.append(anatomy.split('_')[0])
 x={'title':title,'layout':'figure-right' if len(fs)==1 else 'figures-right','body':body,'cite':'; '.join(short[k] for k in dict.fromkeys(keys)),'refs':[refs[k] for k in dict.fromkeys(keys)],'transcript':[re.sub(r'\*\*|(?<!\w)_(?=\w)|(?<=\w)_(?!\w)','',p) for p in body]}
 if extra:x['transcript'].append(extra)
 if len(fs)==1:x['figure']=fs[0]
 else:x['figures']=fs;x['primary_figure_height']=3.35
 slides.append(x)
add('Optical tutoring specifies a vocal duration goal','inception','inception_3', '''**Optogenetics** uses introduced light-sensitive proteins to control neuronal activity. A young male zebra finch can acquire a target for song-element duration without hearing an adult sing. A **behavioral-goal memory** is a retained representation of a desired performance that guides later practice. Zhao and colleagues supplied timed neural activity instead of an acoustic model.

Juveniles received either 50-ms or 300-ms light pulses at inputs to the vocal premotor nucleus **HVC**, a brain region identified by that proper name. The resulting adult songs contained shorter or longer elements, respectively, after weeks of vocal development.

The manipulation supplied temporal information. **Spectral features**, such as pitch and frequency composition, were not systematically specified by these pulses. An artificial duration goal is one component of song learning, rather than an implanted recording of a complete song.''', 'motor_1b')
add('Memorization and vocal practice overlap in development','motor','motor_1', '''Male zebra finches learn an adult tutor's song during a developmental **sensitive period**, an interval when experience has an unusually strong influence on learning. Sensory learning includes hearing and retaining the model; sensorimotor learning includes practicing vocalizations using their auditory consequences.

Roberts and colleagues described sensory learning at approximately 30–60 days after hatching and vocal copying at approximately 45–90 days. These intervals overlap, so a juvenile may listen, memorize, and practice during the same developmental stage.

A **motif** is the recurring sequence of song syllables. Mature pupils reproduce recognizable temporal and acoustic features of the tutor's motif. Experiments restricted to moments of listening distinguish acquisition of the model from the neural activity associated with the pupil's own singing.''')
add('HVC links auditory input to vocal motor pathways','motor','motor_1b', '''HVC is a **premotor nucleus**, a population of neurons involved in organizing activity before the final motor commands reach muscles. Auditory information reaches HVC through forebrain pathways, placing sensory input within circuitry that also controls learned song.

HVC projects to **RA**, the robust nucleus of the arcopallium, which communicates with brainstem vocal motor circuitry. It also projects to **Area X**, a striatal component of the song system involved in learning. These routes couple a developing song representation to motor production and modification.

The auditory and motor organization permits tutor experience to alter circuitry later used for performance. Disrupting HVC specifically during listening tests this encoding role, while leaving later rehearsal outside the stimulation period.''')
add('NIf provides an auditory entry into HVC','inception','inception_2ac', '''The **nucleus interfacialis of the nidopallium**, abbreviated NIf, supplies a major auditory input to HVC. A projection is the set of axons connecting one neuronal population to another. NIf neurons deliver signals to HVC through synapses at their axon terminals.

Zhao and colleagues introduced an axon-targeted light-sensitive protein into NIf neurons and illuminated their terminals in HVC. The labeled tissue identifies the input being manipulated, while recordings establish that this input excites HVC neurons.

NIf activity during singing can mark the beginnings and endings of song elements. The hypothesis motivating optical tutoring was that imposed activity in this pathway could specify a duration target for later vocal learning. Terminal stimulation tests that hypothesis at an identified sensory–motor connection.''')
add('Repeated imaging follows the same HVC spines','spines','spines_1', '''A **dendritic spine** is a small protrusion on a neuron's dendrite and a major site of excitatory synaptic input. Roberts and colleagues labeled HVC neurons with **green fluorescent protein**, a fluorescent marker, and repeatedly imaged their dendrites through a cranial window.

**Two-photon microscopy** permits optical measurements within living tissue. Images were collected during the birds' subjective night to reduce interference with daytime behavior. Retrograde tracers, labels transported from projection targets back to cell bodies, helped identify HVC and its projection neurons.

The same dendritic branches persisted across nights, while individual spines appeared or disappeared over shorter intervals. Repeated observations therefore separated stable neuronal architecture from local changes at potential synaptic contacts during the onset of tutoring.''')
add('Spine dynamics change with age and experience','spines','spines_2', '''**Spine turnover** describes the appearance and disappearance of dendritic spines between observations. In HVC, turnover measured across a 2-h interval was elevated in untutored 45-day-old juveniles compared with birds of the same age that had heard a tutor.

Untutored birds at 60 days varied widely, with some retaining dynamic spines and others resembling already tutored birds. At 90 days, untutored birds had lower turnover resembling age-matched controls. Development can therefore reduce spine dynamics even without a new adult model.

Tutoring experience and maturation jointly shape the available synaptic substrate. The hypothesis is that more dynamic HVC contacts permit greater modification by a newly encountered tutor song, whereas stabilization accompanies commitment to an established vocal pattern.''', 'spines_1a')
add('Dynamic spines predict later tutor-song copying','spines','spines_2', '''Previously untutored juveniles first encountered a song model at 60 days, near an age when normally tutored zebra finches resist learning a new model. Some of these delayed pupils copied new song elements, while others changed very little.

Spine turnover measured the night before tutoring was positively related to the subsequent increase in song similarity. **Song similarity** compares acoustic features of a pupil's vocalizations with those of the tutor, rather than measuring how much the pupil sings.

This relationship connects a local property of HVC dendrites to the capacity for later behavioral change. Dynamic spines provide a candidate substrate for accepting new experience; the association motivated direct imaging of the same contacts immediately before and after the first tutoring session.''', 'spines_1a')
add('First tutoring rapidly stabilizes dynamic spines','spines','spines_3ab', '''High-turnover juveniles rapidly reduced HVC spine turnover after their first exposure to tutor song. The change was evident by the next night, placing structural modification within approximately 24 h of the initial instructive experience.

Birds with initially low turnover showed little corresponding change. Thus the same experience acted differently depending on the prior state of the dendritic population. Both live tutoring and operant access to recorded tutor song could produce stabilization in responsive juveniles.

In one bird followed through the remaining month of sensorimotor learning, much of the eventual turnover reduction occurred during the first 48 h after hearing the tutor. Early listening reorganized a synaptic substrate before the gradual completion of adult song imitation.''', 'spines_1a')
add('A silent tutor does not trigger spine stabilization','spines','spines_3ab', '''A tutor housed with one high-turnover juvenile remained silent for the first two days. HVC spine turnover stayed high during this period and declined only after the adult began singing. Social presence alone was insufficient to produce the observed structural change.

The timing distinguishes contact with an adult bird from access to the acoustic song model. Operant tutoring also induced stabilization, so a live social encounter was not obligatory for this particular structural response under the study's conditions.

Auditory experience can therefore initiate rapid modification of HVC contacts. Social factors still influence how effectively pupils learn songs in other preparations; the delayed-singing observation identifies the event linked to stabilization in this juvenile rather than replacing the broader role of social tutoring.''', 'spines_1a')
add('Tutoring adds persistent contacts to HVC dendrites','spines','spines_3cd', '''Following initial tutoring, high-turnover juveniles accumulated additional HVC dendritic spines. **Spine density** is the number of spines along a defined extent of dendrite. Its increase accompanied reduced turnover, combining formation of new contacts with greater persistence.

Repeated images distinguished newly formed spines from pre-existing stable spines. Some contacts that appeared during the first tutoring day remained present during the following imaging session, increasing the population available for excitatory synaptic transmission.

Low-turnover juveniles showed little comparable density increase. The responsive state therefore involved coordinated changes in contact number and stability. During the same early period, their vocalizations began acquiring acoustic variation associated with imitation, linking structural plasticity to the onset of behavioral development.''', 'spines_1a')
add('Stable spines enlarge after instructive experience','spines','spines_4', '''Tutoring also altered contacts that were already present. In high-turnover birds, stable HVC spines increased in size by the first night after tutoring. Integrated fluorescence provided a measure related to spine volume, allowing the same contacts to be compared across sessions.

The reported enlargement was approximately 28%. Before tutoring, stable spines in the high-turnover group were smaller than those in low-turnover birds; that size difference disappeared after the first instructive session. Low-turnover birds showed little enlargement.

Spine enlargement is a structural correlate of stronger excitatory synaptic connections. Together with stabilization and accumulation, it suggests that initial tutor experience modifies both existing contacts and the set of contacts retained on HVC neurons.''', 'spines_1a')
add('Tutoring enhances depolarizing synaptic activity','spines','spines_5', '''An **excitatory postsynaptic potential** is a synaptically produced change that moves a neuron's membrane voltage toward firing. Intracellular recordings from HVC projection neurons compared spontaneous depolarizing activity before and after a juvenile's first day with a tutor.

After tutoring, depolarizing synaptic events became larger and prolonged bursts lasting approximately 1 s emerged. Resting membrane voltage and action-potential firing rate did not undergo matching changes, separating the enhanced synaptic activity from a simple increase in overall output firing.

Enhancement occurred even in a juvenile that did not sing during its first tutoring session. Hearing the tutor could therefore alter HVC physiology before vocal rehearsal supplied feedback. The hypothesis is that strengthened synaptic input helps establish the representation subsequently used during imitation.''', 'spines_1a')
add('Closed-loop stimulation targets the listening episode','motor','motor_2', '''A **closed-loop intervention** uses a detected event to trigger a manipulation. Roberts and colleagues detected recognizable features of the adult tutor's song and immediately delivered light to the pupil's HVC, concentrating disruption within the listening episode.

Previously untutored juveniles met the tutor for 2 h per day on five consecutive days. Light pulses lasted 200 or 500 ms, and birds were subsequently raised without further tutoring until their adult song was measured after 90 days.

The supplementary recording captures the tutor on the right and the connected juvenile during its first tutoring experience. The cable delivers the optical intervention when tutor song is detected. The experimental contingency links an auditory event outside the pupil to a precise manipulation inside its vocal premotor circuitry.''')
add('Channelrhodopsin changes activity in the HVC network','motor','motor_2', '''**Channelrhodopsin-2**, abbreviated ChR2, is a light-sensitive cation channel, which conducts positively charged ions introduced into neurons using a viral vector. Illumination can change membrane voltage and evoke activity, permitting rapid perturbation of the juvenile HVC network.

In the 2012 study, 473-nm light produced excitation at some recording sites, suppression at others, and mixed responses at others. Network inhibition can suppress neurons even when the introduced channel is excitatory. The intervention therefore disrupted normal population dynamics rather than uniformly silencing HVC.

Responses were confined mainly to superficial HVC, and recordings found no corresponding antidromic activation in the tested upstream auditory regions. **Antidromic activation** means an action potential traveling back toward a cell body along an axon. These controls localized the manipulated activity.''')
add('Disruption during listening impairs adult imitation','motor','motor_2', '''Juveniles receiving tutor-song-contingent optical disruption in HVC developed adult songs with little resemblance to their tutor's song. Controls exposed to the same tutor copied recognizable acoustic structure, linking the later deficit to the timing and location of the neural intervention.

Delivering the same temporal pattern of stimulation after the tutor was removed preserved copying. Light delivered without ChR2 also preserved learning. The physical illumination and connection to the apparatus were therefore insufficient to explain the impaired imitation.

The pupil's premotor activity during observation contributes to acquiring the model. Activity outside that observation period has a different experimental consequence, so sensory acquisition can be separated from later rehearsal rather than inferred from a lasting lesion affecting both phases.''')
add('Timed disruption selectively damages one syllable copy','motor','motor_3', '''Electrical microstimulation provided finer temporal control over HVC than the optical perturbation used in the initial experiment. A detector triggered stimulation during one designated syllable of the tutor's motif, while preceding and following syllables remained outside the targeted interval.

Stimulation used 20-µA biphasic pulses at 170 Hz for 200 ms. Adult pupils copied the targeted syllable poorly but reproduced surrounding syllables more accurately. The disruption therefore affected a temporally restricted component of the observed model.

This result connects the timing of HVC activity during listening to the identity of the material acquired. A song memory is not merely a global decision to sing; encoding preserves information about specific elements encountered at specific times.''', 'motor_1b')
add('NMDA receptors are needed for tutor-evoked enlargement','motor','motor_4', '''**NMDA receptors** are glutamate-activated ion channels associated with excitatory transmission and synaptic plasticity. The antagonist **D-AP5** blocks their activation. Roberts and colleagues applied this drug to HVC before tutoring while imaging the same stable dendritic spines across nights.

A brief tutoring session normally enlarged stable spines in responsive juveniles. When preceded by D-AP5, tutoring failed to produce the enlargement. The intervention links an identified receptor class to the structural response induced by the acoustic model.

The result supports an NMDA-dependent plasticity mechanism at the sensory–motor interface. Spine enlargement is the measured structural change; its relationship to learning becomes stronger when the same receptor manipulation is timed to tutoring and adult song copying is examined afterward.''')
add('NMDA blockade during tutoring prevents copying','motor','motor_4', '''Juveniles with bilateral HVC microdialysis probes received D-AP5 while listening to the tutor. **Microdialysis** exchanges dissolved substances through a small membrane, allowing a drug to be delivered locally during an experimental session and subsequently removed.

Blocking NMDA receptors during tutoring impaired the adult copy of the tutor song. Reversing the treatment schedule, so that blockade occurred during a later period of vocal practice rather than tutor exposure, preserved substantially better imitation.

The timing links NMDA-dependent HVC activity to acquiring the instructive song experience. In the imaging experiment, the same receptor class supported stable-spine enlargement. Together the behavioral and cellular interventions connect receptor activation, structural modification, and the model that guides subsequent vocal development.''')
add('Sodium-channel blockade in NIf disrupts acquisition','motor','motor_5', '''**Tetrodotoxin**, abbreviated TTX, blocks voltage-gated sodium channels required for action-potential propagation. Local TTX application reversibly suppressed NIf activity while previously untutored juveniles heard a live adult song model.

Birds received bilateral NIf treatment before each daily 1.5-h tutoring session and saline later in the day. They subsequently copied the tutor poorly. Birds receiving saline during tutoring and TTX afterward developed more accurate copies, tying the impairment to NIf activity during observation.

NIf conveys auditory information toward HVC, so transiently blocking its spikes interrupts an input needed for sensory acquisition. The reversible schedule complements permanent lesions by allowing activity to recover for later practice and distinguishing the listening interval from other stages of song development.''', 'motor_1b')
add('NIf disruption differs from nearby auditory stimulation','motor','motor_5', '''Tutor-song-triggered electrical stimulation in NIf impaired later copying, while stimulation in the neighboring auditory region Field L1 permitted much better imitation. **Field L** is a primary auditory forebrain region, and Field L1 names a subdivision within it.

The anatomical comparison asks whether any nearby electrical intervention would have the same effect. Together with reversible NIf inactivation, the location-specific result identifies the NIf pathway as a particularly important contributor during acquisition of the model.

Permanent NIf lesions also produced poorer copying when more of NIf was removed. Converging interventions therefore connect the extent, location, and timing of disrupted activity to subsequent imitation. The sensory input reaching HVC is organized through defined pathways rather than an interchangeable mass of auditory tissue.''', 'motor_1b')
add('PAG dopamine neurons provide a social tutoring signal','dopamine','dopamine_1abc', '''The **periaqueductal gray**, abbreviated PAG, is a midbrain region containing dopamine-producing neurons that project to HVC. **Dopamine** is a neurotransmitter that modulates target-cell signaling rather than providing the acoustic pattern of the tutor's syllables.

Tanaka and colleagues injected a retrograde tracer into HVC and labeled **tyrosine hydroxylase**, an enzyme involved in catecholamine synthesis. Neurons containing both labels identified a major dopaminergic source of the projection to HVC in the PAG.

This pathway differs from dopamine projections associated with the basal ganglia song-learning circuit. Its position allows social information about a singing tutor to converge with auditory input within vocal premotor circuitry, potentially facilitating acquisition of a suitable model.''')
add('PAG neurons respond selectively to a singing tutor','dopamine','dopamine_1', '''PAG neurons in previously untutored juvenile males increased firing during encounters with a live singing tutor. **Tetrodes**, groups of four recording wires, allowed extracellular action potentials from individual neurons to be tracked during these social encounters.

Playback of adult song through a speaker produced little comparable increase. Encounters with a non-singing adult male or a female also failed to generate the response associated with live tutoring. The signal depended on the combined social and vocal situation.

PAG activity was not precisely locked to each syllable and could remain elevated after song stopped. Its temporal profile is consistent with a contextual tutoring signal rather than a millisecond-by-millisecond acoustic copy. Auditory pathways can carry song structure while PAG activity indicates the instructive encounter.''')
add('A fluorescent sensor detects dopamine in HVC','dopamine','dopamine_2', '''The **GRAB dopamine sensor** is a modified dopamine receptor coupled to a fluorescent readout. In this study, a modified D2 receptor increased fluorescence when dopamine bound to it, allowing dopamine transients in HVC to be measured with two-photon microscopy.

Awake, head-fixed juvenile males exhibited increased sensor fluorescence while a live tutor sang. Song playback, a non-singing adult male, and a female produced little comparable response. Dopamine release thus paralleled the socially selective activity recorded in PAG.

The sensor identifies transmitter availability, rather than directly measuring postsynaptic spiking or permanent synaptic change. Its response places the modulatory signal inside HVC during the event that supplies the acoustic model, linking social context to a potential gate for song-memory formation.''')
add('Lesioning PAG dopamine neurons removes HVC transients','dopamine','dopamine_2', '''The catecholaminergic neurotoxin **6-hydroxydopamine**, abbreviated 6-OHDA, was used to ablate dopamine neurons in the PAG. After this treatment, live tutor song no longer evoked the usual dopamine-sensor transients in the juvenile's HVC.

This manipulation identifies the source of the measured release. The anatomical tracer establishes a PAG-to-HVC projection, PAG recordings establish tutor-related activity, and loss of the HVC fluorescence response after PAG treatment connects the projection to the transmitter signal.

The combined observations place social detection upstream of local dopamine release during tutoring. A singing adult engages PAG activity, and the resulting dopaminergic projection can influence the HVC circuitry that receives auditory information and later organizes learned song.''', 'dopamine_1abc')
add('Early dopamine-fiber lesions prevent song copying','dopamine','dopamine_3ad', '''Dopaminergic fibers within HVC were lesioned with 6-OHDA at two developmental stages. Removing the fibers near 30 days of age, at the beginning of tutor-song memorization, prevented accurate copying despite continued exposure to adult tutors.

The resulting adult syllables were unusually long and acoustically simple, resembling songs of untutored birds. Overall singing rate was preserved, separating failure to acquire the tutor's structure from a general failure to produce vocal behavior.

The same type of lesion near 45 days, after sufficient tutor experience, spared copying. Dopamine input was therefore especially consequential before the model had been acquired. The age comparison motivated reversible receptor blockade confined to actual tutoring sessions.''')
add('D1-type receptors contribute during tutor exposure','dopamine','dopamine_3gh', '''**D1-type dopamine receptors** are a receptor family through which dopamine modulates neuronal signaling. Reversibly blocking these receptors in HVC during live tutoring impaired subsequent song imitation, linking the transmitter's effect to an identified postsynaptic receptor class.

Pupils met a tutor for 1.5 h on five consecutive days. Broader dopamine-receptor blockade during those sessions also impaired copying, whereas delivery immediately after the session spared learning. The model was acquired when local dopamine signaling coincided with tutor exposure.

The vehicle condition preserved receptor signaling and normal learning. The corresponding supplementary recording captures a pupil interacting with its tutor under that control condition. The acoustic model and social encounter are available while HVC receives its normal modulatory input.''', 'dopamine_1abc')
add('HVC dopamine blockade spares observable attention','dopamine','dopamine_3gh', '''Juveniles receiving dopamine-receptor blockers in HVC continued orienting toward their tutors during the tutoring sessions. Tutors also continued singing at normal rates. These behaviors preserved access to the model even though the pupils later copied it poorly.

The supplementary recording permits comparison with the vehicle condition. The pupil can attend to the adult without intact local dopamine signaling in HVC, separating an observable attentional response from the neural processes that encode the song experience.

Dopamine's contribution therefore includes modulation within the memory-related circuit, beyond maintaining gross orientation toward the tutor. Blocking receptors during exposure disrupts later imitation while leaving the immediate social behavior that supplies the model substantially available.''', 'dopamine_1abc')
add('PAG inactivation changes orientation and learning','dopamine','dopamine_1', '''**Muscimol** is an agonist at inhibitory GABA-A receptors and can suppress activity in a locally treated brain region. Tanaka and colleagues applied it to the pupil's PAG during daily tutoring to test whether the upstream social signal was necessary.

PAG inactivation impaired subsequent copying and reduced the pupil's orientation toward the tutor, even though the adult continued singing. The supplementary recording captures this altered social response, which differs from the preserved orientation during dopamine blockade confined to HVC.

The anatomical level of intervention therefore matters. PAG activity contributes to attending to the singing model as well as supplying dopamine to HVC; local HVC receptor blockade isolates a downstream encoding effect while leaving more of the immediate attentional behavior intact.''')
add('Dopamine-terminal stimulation enables playback learning','dopamine','dopamine_3ij', '''Passive song playback normally produced little copying in the tutoring preparation used by Tanaka and colleagues. To replace a missing social signal, the researchers expressed ChR2 in PAG neurons and illuminated their axon terminals within HVC while the recorded song played.

Pairing terminal activation with playback enabled pupils to copy the acoustic model more effectively. Playback alone and illumination without ChR2 were less effective, linking the benefit to activity in the identified projection rather than to the light or speaker.

Dopamine-receptor blockade in HVC removed the benefit of the pairing. The acoustic recording supplied song content, while the stimulated pathway supplied a modulatory condition that allowed that content to be acquired. This differs from directly specifying duration with NIf input pulses.''')
add('Live tutoring rapidly increases HVC burst activity','dopamine','dopamine_4', '''A **burst** is a brief cluster of closely spaced action potentials. Within approximately 1 h after initial live tutoring, spontaneous HVC activity included more bursts exceeding 100 Hz, even though mean firing rate did not increase correspondingly.

The change concerns the temporal organization of spiking rather than simply the total amount of activity. Such bursts can accompany concentrated synaptic input, connecting the new instructive experience to altered dynamics in premotor circuitry.

Dopamine disruption prevented the increase in bursting. The hypothesis is that tutor-evoked dopamine facilitates rapid enhancement of auditory inputs to HVC. The initial physiological change can occur before vocal practice, since the recorded pupils did not sing during or immediately after the tutoring session.''', 'dopamine_1abc')
add('Tutor responses become more temporally reproducible','dopamine','dopamine_4', '''Before initial live tutoring, HVC responses to the tutor's recorded song were relatively inconsistent across presentations. After the juvenile encountered the singing adult, responses to playback became more reproducible at particular times within the motif.

Mean response firing rate was largely unchanged. Reduced variability across trials therefore reflected tighter temporal organization, rather than a simple increase in the average number of spikes produced by the recorded neurons. Dopamine disruption prevented the normal change.

A representation that responds reliably to particular song features can provide more structured input to the circuits used for imitation. The hypothesis is that coincident auditory experience and dopamine signaling reorganize HVC responses so that the observed model acquires a reproducible temporal representation.''', 'dopamine_1abc')
add('Early vocal changes follow dopamine-dependent tutoring','dopamine','dopamine_4', '''Initial tutoring rapidly changed the acoustic organization of juvenile vocalizations. Long, relatively unstructured vocal sounds became more varied, and within-syllable entropy variance increased. **Entropy** describes spectral disorder; its variation captures changes in acoustic structure across a vocal element.

These changes were evident within the early hours after tutoring, well before mature imitation was complete. Dopamine blockade in HVC prevented both the early vocal changes and the normal neural changes associated with the tutor encounter.

The behavioral trajectory therefore begins with a rapid response to the acquired model and continues through extended sensorimotor practice. Modulation during observation can alter the initial conditions for later learning without producing an immediate finished adult song.''', 'dopamine_1abc')
add('Axon-targeted ChR2 isolates NIf input to HVC','inception','inception_2ac', '''Zhao and colleagues introduced **axon-targeted ChR2** into NIf neurons using a self-complementary adeno-associated viral vector. Targeting the protein toward axons permitted light delivered over HVC to activate the terminals of a defined input population.

Labeled tissue identified the projection in both NIf and HVC. Brain-slice recordings then measured light-evoked excitatory postsynaptic currents in HVC neurons, verifying that illumination could recruit synaptic transmission through the selected pathway.

The preparation separates manipulating an input from directly exciting all cells in a premotor nucleus. This distinction changes the teaching signal: the earlier HVC perturbation disrupted encoding, whereas timed NIf-terminal activation was used to supply information capable of guiding subsequent song-element duration learning.''')
add('Glutamate receptors mediate light-evoked excitation','inception','inception_2ac', '''**Glutamate** is the excitatory transmitter mediating the tested NIf input to HVC. The postsynaptic ionotropic **AMPA** and NMDA receptor classes permit synaptic currents when activated; the study used receptor antagonists to identify their contribution to light-evoked transmission.

HVC neurons were recorded at a holding potential of −80 mV while NIf terminals received 20-ms pulses at 1 Hz. Applying DNQX and DL-AP5 blocked the evoked excitatory currents, and birds lacking ChR2 lacked the corresponding light-driven response.

Thus optical tutoring engages a glutamatergic synaptic connection rather than delivering an acoustic stimulus to the ears. The electrophysiological control establishes how introduced light sensitivity is translated into input received by neurons in the vocal premotor circuit.''')
add('Projection controls distinguish direct and indirect routes','inception','inception_2hl', '''NIf also projects to **Avalanche**, abbreviated Av, another sensorimotor region with connections to HVC. Tracer injections distinguished NIf neurons targeting HVC, neurons targeting Av, and the small population projecting to both regions.

Most labeled NIf projection neurons targeted one destination rather than both. Terminal illumination in HVC produced local responses without the tested antidromic activation of NIf. Effective optical recruitment was also confined near the brain surface, away from the deeper Av terminals.

These controls support selective manipulation of the NIf-to-HVC connection. In living birds, HVC responses included excitation and suppression, so the imposed input propagated through a network containing multiple interacting cell types. Input duration, rather than uniform output firing in every neuron, was the manipulated variable.''')
add('Brief pulse trains supply a temporally defined tutor','inception','inception_3ad', '''Untutored juveniles received optical tutoring late in their sensory-learning period. NIf viral injections occurred around 45 days after hatching, with stimulation beginning after expression developed. No adult song model was supplied during the optical sessions.

The short-pulse condition used four 50-ms pulses separated by 100-ms intervals, repeated in 300 trials across approximately 1.5 h per day for five days. Timing was chosen to resemble repeated brief elements encountered during natural tutoring patterns.

Adult song was analyzed at 90–120 days rather than during stimulation itself. The experimental separation between juvenile input and mature output tests whether a transient instructive experience leaves a target that can influence the prolonged developmental learning process.''', 'inception_2ac')
add('Short optical tutoring yields short adult elements','inception','inception_3ad', '''Adult birds exposed to 50-ms optical tutoring as juveniles produced song elements clustered near that duration. Their median element duration was 62.3 ms, compared with 106 ms for normally tutored birds and 171 ms for untutored birds in this study.

The researchers segmented recorded vocalizations using thresholds of amplitude, the intensity of the sound, and measured each element's duration. Short-pulse birds often produced relatively simple songs containing a few repeated element types, including rapidly repeated or trilled elements.

The duration difference links the temporal pattern supplied to the input pathway with the later acoustic output. The acquired target shaped one measurable feature of courtship song while the juvenile still developed the ability to produce and organize vocalizations through practice.''', 'inception_2ac')
add('Long optical tutoring yields longer song elements','inception','inception_3eg', '''Changing the optical input from 50-ms pulses to 300-ms pulses shifted adult song elements toward longer durations. The long-pulse group had a median duration of approximately 323 ms, substantially longer than the elements of the short-pulse group.

Both conditions stimulated the same NIf-to-HVC connection and used repeated juvenile tutoring sessions. The contrasting outcome therefore identifies pulse duration as an instructive parameter, rather than treating optical activation as a generic trigger for song development.

Long-pulse birds also produced simple songs with a few element types. The behavioral target was temporal: increasing the duration of pathway activation altered the time scale of elements that emerged after extended practice, without supplying the spectral detail of an adult tutor recording.''', 'inception_2ac')
add('Short-element songs emerge through gradual practice','inception','inception_4a', '''After short optical tutoring, juvenile vocalizations did not instantly become a mature sequence of 50-ms elements. Initial changes appeared within 2–3 days, followed by further modification over the month of sensorimotor learning.

Long, noisy precursor elements increasingly developed amplitude modulation, meaning rises and falls in sound intensity across time. Distinct gaps and rapidly repeated short elements emerged as the vocal pattern became organized. The developmental recordings followed the same bird across successive ages.

This trajectory resembles learning toward a retained goal rather than immediate execution of an imposed motor sequence. The temporal target persisted after optical sessions ended, while the vocal system gradually produced elements and separations that approached the instructed time scale.''', 'inception_2ac')
add('Long-element songs consolidate through another trajectory','inception','inception_4b', '''Juveniles given 300-ms optical tutoring gradually reduced amplitude modulation within vocal elements. Longer and more harmonic sounds emerged over subsequent practice, following a developmental trajectory different from the increasing segmentation of short-pulse birds.

Before approximately 80 days, durations and acoustic features remained variable. Around 85–90 days, songs began **crystallizing**, becoming increasingly stable and stereotyped. Long-pulse and short-pulse birds therefore shared a prolonged developmental learning phase despite approaching different duration goals.

The light pattern set the direction of temporal development while the motor pattern matured afterward. A persistent goal can influence how successive vocal precursors are modified, rather than requiring the adult form to be available during the initial instructive experience.''', 'inception_2ac')
add('Artificially tutored song retains its courtship use','inception','inception_4', '''**Directed singing** is song produced toward a female during courtship, as distinguished from undirected singing when the male is alone. Optically tutored adults used their short or long learned elements during directed singing when females were presented.

These birds also practiced alone and produced other call types typical of zebra finches. The altered temporal pattern was therefore incorporated into socially appropriate vocal behavior rather than appearing only as an isolated laboratory response.

The behavioral organization separates what was modified from how song was deployed. Optical tutoring changed element duration, while the birds retained courtship use and a broader vocal repertoire. The acquired temporal target could be expressed within the animal's existing social communication behavior.''')
add('Optical duration goals can override a live tutor','inception','inception_5', '''Juveniles could receive two potential sources of instruction at once: a live adult song and tutor-song-contingent 300-ms activation of NIf terminals in HVC. Their eventual vocalizations followed the long-duration optical condition rather than accurately copying the adult's song.

The combined group resembled birds receiving optical tutoring alone in element duration. Representative control pupils copied their tutor's motif closely, whereas pupils receiving simultaneous optical input developed markedly different song elements despite access to the natural model.

Competition between the two inputs places the manipulated connection within acquisition of the behavior-guiding representation. The imposed temporal signal can dominate the target used for later practice when delivered during the same encounter that normally supplies auditory and social instruction.''', 'inception_2ac')
add('Pathway lesions before tutoring block model acquisition','inception','inception_6', '''An **intersectional viral strategy** selects cells using two linked targeting conditions. Zhao and colleagues used this approach to express **caspase-3**, an enzyme that triggers cell death, specifically in NIf neurons projecting to HVC.

When this pathway was lesioned at approximately 35–40 days before the birds first encountered a tutor at 55–60 days, adult pupils copied poorly. Selective removal of the projection therefore disrupted acquisition even though other auditory pathways remained available.

The intervention identifies the population carrying an essential contribution to the newly acquired model. Its effect complements artificial tutoring: activity supplied at NIf-to-HVC terminals can guide duration learning, and loss of those projecting neurons before observation prevents normal imitation of the social tutor.''', 'inception_2ac')
add('Acquisition and later imitation use different dependencies','inception','inception_6', '''Removing NIf-to-HVC neurons after juveniles had already experienced a tutor spared their later imitation. These pupils continued developing accurate adult copies despite losing the projection that was essential when removed before initial tutoring.

The timing distinguishes the pathway needed to establish a behavior-guiding memory from the circuitry that subsequently uses it during practice. A lasting memory can continue influencing development after the original acquisition route has been removed.

The hypothesis is that the acquired representation is retained downstream of NIf-to-HVC synapses, potentially across a distributed network. Artificial tutoring, timed disruption, dopamine modulation, and spine plasticity identify complementary parts of the transformation from observed song to a persistent goal for vocal behavior.''', 'inception_2ac')
assert len(slides)==44,len(slides)
# Complete read-aloud paragraphs are retained as transcript bullets; additional detail
# belongs to the specific study rather than a generic method/result/limitation template.
media=json.loads((D/'media_sources.json').read_text())
assign={'tutor_disruption':13,'vehicle':26,'dopamine_block':27,'pag_inactivation':28}
for m in media:
 key=Path(m['path']).stem;i=assign[key];x=slides[i-1];m['content_slide']=i;m['pptx_slide']=i+1
 number='1' if key in ['tutor_disruption','vehicle'] else '2' if key=='dopamine_block' else '3'
 m['caption']=f'{m["credit"]}, Supplementary Video {number}. '+{'tutor_disruption':'Tutor-song-triggered optical disruption during first tutoring.','vehicle':'Pupil–tutor interaction with vehicle in HVC.','dopamine_block':'Pupil–tutor interaction with dopamine blockers in HVC.','pag_inactivation':'Pupil–tutor interaction with muscimol in PAG.'}[key]
 x['media_source']=m
(D/'media_sources.json').write_text(json.dumps(media,indent=2))
# An original frame of the article-provided recording is a photograph of the study animals.
title={'path':'figures/tutor_disruption_poster.png','kind':'web','caption':'Photo: Juvenile zebra finch and adult tutor during experimental tutoring.','credit':'Roberts et al. (2012), original Supplementary Video 1 frame','license':'Publisher-supplied supplementary recording; copyright remains with the authors/publisher','source_url':next(m['url'] for m in media if 'tutor_disruption' in m['path'])}
items=[('Behavioral-goal memory','A retained target guides gradual vocal development; 50-ms and 300-ms NIf-input tutoring produce different adult element durations.'),('Premotor encoding','HVC activity during tutor listening contributes to acquiring the song model, including temporally specific syllable information.'),('Synaptic plasticity','Initial tutoring stabilizes and enlarges HVC spines; NMDA-receptor blockade during tutoring prevents enlargement and impairs imitation.'),('Social dopamine signal','A live singing tutor recruits PAG dopamine input to HVC, where D1-type signaling contributes to model acquisition.'),('Distinct optical instructions','PAG-terminal stimulation gates learning from an acoustic recording; NIf-terminal stimulation supplies a temporal goal without an adult song model.'),('Acquisition versus later use','Removing NIf-to-HVC neurons before tutoring blocks copying, whereas removal after tutor experience preserves subsequent imitation.')]
spec={'lecture':80,'theme':'muted-lagoon-paper','content_slides':44,'title_image':title,'title_refs':[refs['motor']],'slides':slides,'takeaways':{'items':[{'lead':a,'text':b} for a,b in items],'cite':'; '.join(short.values()),'refs':list(refs.values())}}
(D/'lecture.json').write_text(json.dumps(spec,indent=2,ensure_ascii=False)+'\n')
themes=json.loads((R/'course/themes.json').read_text());themes['palettes'].setdefault('muted-lagoon-paper',{'label':'muted lagoon blue / paper white','title_bg':'507A87','title_text':'FFFFFF','title_muted':'E5EFF2','bg':'FFFFFF','heading':'34515A','text':'000000','muted':'000000','tint':'F0F5F6','accent':'507A87','rule':'CFDDE1'});(R/'course/themes.json').write_text(json.dumps(themes,indent=2,ensure_ascii=False)+'\n')
print('Slides:',len(slides),'body words:',[len(re.findall(r"\b[\w’−-]+\b",' '.join(x['body']))) for x in slides])
