"""Lecture 59. Paragraphs teach the cited sources; figures are original PDF crops."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parent
R={
'B':'Bosch OJ, Nair HP, Ahern TH, Neumann ID, Young LJ (2009). The CRF system mediates increased passive stress-coping behavior following the loss of a bonded partner in a monogamous rodent. Neuropsychopharmacology 34: 1406–1415. https://doi.org/10.1038/npp.2008.154',
'O':'Bosch OJ, Dabrowska J, Modi ME, Johnson ZV, Keebaugh AC, Barrett CE, Ahern TH, Guo J, Grinevich V, Rainnie DG, Neumann ID, Young LJ (2016). Oxytocin in the nucleus accumbens shell reverses CRFR2-evoked passive stress-coping after partner loss in monogamous male prairie voles. Psychoneuroendocrinology 64: 66–78. https://doi.org/10.1016/j.psyneuen.2015.11.011',
'D':'Pierce AF, Protter DSW, Watanabe YL, Chapel GD, Cameron RT, Donaldson ZR (2024). Nucleus accumbens dopamine release reflects the selective nature of pair bonds. Current Biology 34: 519–530.e5. https://doi.org/10.1016/j.cub.2023.12.041',
'T':'Sadino JM, Bradeen XG, Kelly CJ, Brusman LE, Walker DM, Donaldson ZR (2023). Prolonged partner separation erodes nucleus accumbens transcriptional signatures of pair bonding in male prairie voles. eLife 12: e80517. https://doi.org/10.7554/eLife.80517'
}
C={'B':'Bosch et al. (2009)','O':'Bosch et al. (2016)','D':'Pierce et al. (2024)','T':'Sadino et al. (2023)'}
S=[]
def fig(key,k,panel,meaning):
 return {'path':'figures/'+key+'.png','kind':'article','caption':C[k]+', Fig. '+panel+'. '+meaning,'source_url':R[k].split('https://')[1].join(['https://',''])}
def add(title,k,key,panel,meaning,body,anatomy=None):
 paras=body.strip().split('\n\n');assert len(paras)==3
 f=fig(key,k,panel,meaning)
 s={'title':title,'layout':'figure-right','body':paras,'cite':C[k],'refs':[R[k]],'transcript':[re.sub(r'\*\*|(?<!\w)_(?=\w)|(?<=\w)_(?!\w)','',p) for p in paras],'figure':f}
 if anatomy:
  s.pop('figure');s['layout']='figures-right';s['figures']=[f,fig('p24_3b','D','3B','Histological localization in the accumbens shell.')];s['cite']+='; '+C['D'];s['refs'].append(R['D'])
 S.append(s)

add('Losing a bonded partner changes stress coping','B','b09_2ab','2a–b','Passive coping after partner or sibling separation.', '''Prairie voles, _Microtus ochrogaster_, form selective social attachments. Bosch and colleagues housed males with a female partner or male sibling for 5 days, then either maintained the pair or separated the animals. This comparison distinguishes the consequences of losing a bonded mate from those of losing another familiar cage-mate.

After several days apart, males separated from the female spent more time floating during forced swimming and more time immobile during tail suspension. **Passive coping** means reduced active movement during these inescapable challenges, rather than a measurement of the animal's subjective grief.

Males separated from a sibling retained coping behavior resembling paired controls. Relationship history therefore changes the response to social removal: the same housing manipulation has different behavioral consequences when it interrupts a mating partnership.''')
add('Floating and immobility measure passive coping','B','b09_2ab','2a–b','Floating and immobility measured in seconds.', '''The **forced swim test** places a vole in water and measures active swimming, struggling, and floating. Floating conserves movement while keeping the animal above water. The **tail suspension test** instead measures periods without active escape movements while the animal is suspended, providing a second physical challenge.

Bosch and colleagues measured these behaviors after 4–5 days of separation. The original plots express floating and immobility in seconds. Female-partner separation increased both measures, whereas sibling separation did not produce the same shift.

Convergence across water exposure and suspension links partner loss to coping strategy across different challenges. The shared result concerns allocation of active versus passive behavior, so interpreting the tasks as a direct diagnosis of human depression would change the biological meaning of the measurement.''')
add('Separation affects different defensive measures differently','B','b09_2cd','2c–d','Open-arm exploration after social separation.', '''An **elevated plus-maze** has exposed open arms and enclosed arms. A vole can explore either, allowing investigators to measure avoidance of exposed space separately from floating or immobility. Open-arm time and the proportion of arm entries sample related but distinct features of exploration.

In the Bosch study, separation left the proportion of time in the open arms unchanged. Open-arm entry patterns showed a broader separation-related tendency rather than the clear female-partner specificity observed during forced swimming and tail suspension. Closed-arm entry counts were similar across the groups.

Social removal therefore modifies some behavioral responses more strongly than others. The passive-coping effect tracks loss of the female partner, while exposed-space exploration provides a different response profile. A single behavioral score would collapse these distinct consequences of separation.''')
add('Partner loss elevates basal corticosterone','B','b09_3','3a–b','Circulating corticosterone and ACTH after separation.', '''The **hypothalamo–pituitary–adrenal axis** coordinates endocrine responses to challenge. Corticotropin-releasing factor, or **CRF**, stimulates pituitary secretion of adrenocorticotropic hormone, or **ACTH**, which stimulates the adrenal cortex to produce glucocorticoids. In these rodents, corticosterone is the measured circulating glucocorticoid.

Bosch and colleagues sampled males that had remained undisturbed rather than exposing them to the behavioral tests first. After 5 days apart, males separated from a female had higher basal corticosterone than males still housed with that female. Sibling separation produced a different endocrine profile.

The corticosterone result connects social relationship disruption to a persistent physiological state outside the test apparatus. ACTH measurements were more variable and lacked a clear group difference, so the two sampled hormones should not be taught as showing identical separation effects.''')
add('Pairing raises CRF transcription in the medial BNST','B','b09_4','4a–b','CRF transcript labeling in the medial BNST.', '''The **bed nucleus of the stria terminalis**, or **BNST**, is a forebrain structure involved in sustained responses to social and stress-related conditions. Bosch and colleagues examined CRF messenger RNA in its medial division. **Messenger RNA** carries gene-derived information used to synthesize a protein or peptide.

In situ hybridization labels a target RNA within tissue. Counts of labeled grains were higher in males with female-pairing experience than in sibling-housed males, whether the female was still present or had been removed. The tissue preparation links the signal to the medial BNST rather than to the entire brain.

The transcriptional difference therefore follows pairing history, while passive coping emerges especially after separation. The authors proposed that a bonding-associated CRF system can contribute to aversive responses when contact with the partner is interrupted.''')
add('CRF receptor blockade reduces separation-induced coping','B','b09_5','5a–c','CRF blockade and coping after partner separation.', '''A **receptor antagonist** occupies or interferes with a receptor so that its usual ligand produces less signaling. Bosch and colleagues delivered the nonselective CRF receptor antagonist d-phe-CRF into the lateral ventricle, allowing central exposure during the separation period rather than giving a single dose immediately before testing.

The infusion began when the partner was removed after 5 days of cohabitation. Separated vehicle-treated males showed increased floating and immobility. Antagonist-treated separated males had lower passive-coping scores, whereas males whose partner remained present changed little with treatment.

The behavioral effect depends on both receptor signaling and relationship condition. Reducing central CRF signaling primarily altered the coping response associated with separation, linking an experimentally manipulated peptide system to how the animal behaves during subsequent challenge.''')
add('CRF blockade preserves an established partner preference','B','b09_5','5a–c','Coping and partner contact under CRF blockade.', '''A **partner preference test** gives a vole access to its familiar partner and an unfamiliar animal. Time spent huddling with each measures selective affiliation. Huddling is sustained close physical contact, so a preference compares allocation of social contact rather than the effort needed to obtain it.

Males in the CRF-antagonist experiment continued to huddle more with the original female than with a stranger. This preference survived both several days of separation and antagonist treatment. At the same time, the antagonist reduced separation-associated floating and immobility.

Selective affiliation and passive coping can therefore move independently. The drug altered the stress response while preserving an already established social preference, allowing students to distinguish the mechanism expressing distress from the behavioral expression of partner recognition and attachment.''')
add('Both central CRF receptor types influence passive coping','B','b09_6','6a–b','Selective CRFR1 and CRFR2 blockade after separation.', '''CRF acts through two receptor classes, **CRFR1** and **CRFR2**. To separate their contributions, Bosch and colleagues used CP-154526 to antagonize CRFR1 and astressin-2B to antagonize CRFR2. Binding experiments checked that these compounds had the intended receptor selectivity in prairie vole tissue.

During separation, either selective antagonist reduced floating in the forced swim test and immobility during tail suspension. The corresponding treatments had little effect in males that remained with their female partner. The effect therefore extends beyond a single nonselective drug.

Because the compounds were delivered centrally, the result identifies receptor involvement across the exposed brain rather than assigning both receptors to one nucleus. Later local manipulations of the accumbens shell isolate a more specific CRFR2 contribution to separation-related behavior.''')
add('Accumbens CRFR2 blockade reduces passive coping','O','b16_1','1','Local CRFR2 manipulations change floating.', '''The **nucleus accumbens** is a ventral striatal region involved in motivated behavior, with core and shell subdivisions. Bosch and colleagues targeted the shell with bilateral drug infusions after males had cohabited with a female for 5 days. Animals were then tested after 3 days with the female present or removed.

Astressin-2B blocked CRFR2 locally and reduced the increased floating observed after partner separation. Vehicle-infused separated males retained greater passive coping. Infusions outside the intended accumbens target lacked the corresponding behavioral effect.

This local comparison narrows the central CRFR2 result to an accumbens-shell mechanism. The shell receives oxytocin-containing fibers, providing an anatomical substrate through which stress-related peptide signaling can alter an attachment-related neuromodulatory system.''',anatomy=True)
add('CRFR2 activation shifts coping with the partner present','O','b16_1','1','CRFR2 activation and blockade have opposing effects.', '''An **agonist** activates a receptor and can reproduce part of its normal ligand's effect. Stresscopin was used to activate CRFR2 in the accumbens shell while paired and separated male voles were compared. The drug and vehicle infusions continued through the experimental period.

Stresscopin increased floating in males that still lived with their female partner. The antagonist produced the complementary reduction in floating after separation. Outside-target infusions supplied an anatomical comparison for the local effects.

These opposing manipulations connect accumbens CRFR2 activity to the balance of active and passive coping. Partner presence is ordinarily associated with lower floating, but experimentally increasing receptor activation can shift behavior even while that social condition remains intact.''',anatomy=True)
add('Oxytocin receptor binding changes after partner loss','O','b16_2top','2(top)','Oxytocin transcripts and receptor binding.', '''**Oxytocin** is a peptide made by hypothalamic neurons and released at sites involved in social behavior. Its receptor, **OTR**, permits target cells to respond to the peptide. Bosch and colleagues measured oxytocin transcripts in the paraventricular nucleus and receptor binding in the accumbens after partner separation.

The accumbens shell showed lower OTR binding after 3 days apart from the female partner. Binding in the accumbens core lacked the same difference. Female-partner and male-sibling conditions helped distinguish relationship-related changes from removal of any cage-mate.

The hypothalamic transcript decrease was weaker and depended on a planned comparison, so it should be treated as tentative. The regional receptor-binding result motivates testing whether changing oxytocin signaling within the shell directly changes the coping response.''',anatomy=True)
add('Local oxytocin reverses separation-associated floating','O','b16_2mid','2(middle)','Oxytocin delivery and receptor blockade alter coping.', '''Bosch and colleagues supplied synthetic oxytocin directly to the accumbens shell during partner separation. This manipulation increases peptide availability near local receptors instead of changing the amount of contact with the missing partner. Vehicle-treated males provided the comparison under the same separation condition.

Oxytocin infusion eliminated the increase in floating after separation. Conversely, blocking OTR increased floating in males that remained with their partner. The behavioral directions match an oxytocin contribution that favors more active coping in this preparation.

The local manipulations connect peptide availability, receptor activation, and behavior. Partner contact is one route associated with the oxytocin system, while experimentally restoring local signaling can modify a separation response even without restoring the social relationship during the treatment period.''',anatomy=True)
add('Reducing accumbens OTR increases passive coping','O','b16_2bottom','2(bottom)','Receptor knockdown and floating behavior.', '''**RNA interference** reduces expression of a selected gene by targeting its messenger RNA. Bosch and colleagues used a viral vector carrying a short hairpin RNA directed against the prairie vole oxytocin receptor. A scrambled sequence provided a control with the same delivery procedure but a different RNA target.

The treatment reduced receptor binding in the accumbens shell and immediate surroundings by about 63%. Binding in the caudate putamen and prefrontal cortex was preserved. Males with reduced accumbens OTR showed increased floating even during cohabitation with a female.

The genetic manipulation converges with local receptor blockade: lowering the capacity to respond to oxytocin changes coping while the partner remains available. Receptor abundance therefore participates in the local pathway linking the social environment to behavioral responses under challenge.''',anatomy=True)
add('Hypothalamic oxytocin neurons also label for CRFR2','O','b16_3abc','3A–C','Oxytocin and CRFR2 labeling in the PVN.', '''The **paraventricular nucleus**, or **PVN**, lies in the hypothalamus beside the third ventricle. Oxytocin-producing neurons have cell bodies and dendrites there. **Immunofluorescence** uses fluorescently labeled antibodies to locate a target molecule in fixed tissue, making the positions of two labels directly comparable.

Bosch and colleagues labeled oxytocin and CRFR2 in prairie vole PVN tissue. The labels overlapped in many oxytocin-positive cells, with receptor and peptide signals occupying related but nonidentical locations. The published panels preserve the cell distribution and a 20 µm scale bar.

The co-labeling supplies an anatomical basis for interactions between stress signaling and the oxytocin system. Receptor presence within this neuronal population motivated physiological recordings to determine how receptor activation changes its electrical inputs.''')
add('Accumbens oxytocin fibers carry CRFR2 labeling','O','b16_3def','3D–F','Co-labeled oxytocin fibers in the accumbens shell.', '''An **axon** carries signals from a neuronal cell body toward its targets, and axonal branches distribute transmitter or peptide release across a target region. Sparse large-caliber oxytocin-positive fibers course through the prairie vole accumbens shell, bringing a hypothalamic peptide system into a motivated-behavior circuit.

The original tissue panels contain oxytocin and CRFR2 labeling along these fibers, including overlapping puncta. Their 20 µm scale bars place the labeled structures at the level of neuronal processes rather than whole brain subdivisions.

This arrangement supports the hypothesis that CRFR2 signaling can regulate oxytocin locally along its axonal pathway. The behavioral shell infusions and fiber labeling address the same region through complementary approaches: one manipulates signaling during coping, while the other identifies a candidate anatomical substrate.''')
add('A reporter identifies oxytocin neurons and their fibers','O','b16_3ghi','3G–I','Oxytocin and Venus labeling in the PVN.', '''A **fluorescent reporter** marks cells expressing a chosen genetic construct. Bosch and colleagues introduced a construct that expresses Venus in oxytocin neurons of the PVN. Labeling for both the reporter and oxytocin checks that the experimental marker identifies the intended neuronal population.

In the hypothalamus, Venus and oxytocin overlapped within a plume of labeled neurons. In the accumbens shell, reporter-positive fibers also overlapped with oxytocin labeling. The source panels use a 200 µm scale bar for the broader hypothalamic distribution and smaller scales for axonal labeling.

Reporter targeting connects identifiable cell bodies to fibers carrying the same peptide marker. It also makes living candidate oxytocin neurons visible during slice experiments, where investigators can record membrane currents from selected cells rather than from an unidentified mixture of hypothalamic neurons.''')
add('Oxytocin reporter fibers reach the accumbens shell','O','b16_3jkl','3J–L','Reporter and oxytocin co-labeling in accumbens fibers.', '''The hypothalamic reporter experiment also examined the accumbens shell, a target outside the injection site. Fibers labeled for Venus overlapped with oxytocin staining there. The 20 µm scale bars distinguish the sparse processes from the much larger PVN field examined in the same study.

This shared labeling links the hypothalamic targeting procedure to an oxytocin-containing projection field in the accumbens. It places the cells used for electrophysiology within the peptide system implicated by the local coping experiments.

The authors' hypothesis combines two possible regulatory sites: CRFR2 can influence the oxytocin population's excitatory drive in the PVN, and receptor labeling along accumbens fibers offers a second possible site for regulating local peptide availability. Both involve the same distributed neuronal system.''')
add('Microdialysis measures local oxytocin availability','O','b16_4','4','Accumbens oxytocin measurements after CRFR2 drugs.', '''**Microdialysis** samples extracellular molecules through a small probe membrane, allowing peptide concentrations to be measured near living brain tissue. Bosch and colleagues placed the probe in the accumbens shell and collected 30-minute samples before and after a central CRFR2 drug infusion.

Oxytocin in each sample was measured by radioimmunoassay, a binding-based method for detecting peptide concentration. Two pre-infusion samples defined the baseline, and later samples covered 90 minutes after infusion. The published graph expresses subsequent measurements relative to that baseline.

This temporal sampling connects receptor manipulation to local peptide availability. The signal averages release, movement, and removal over many minutes, so it represents extracellular oxytocin dynamics across a sampling interval rather than the firing of an individual oxytocin neuron.''',anatomy=True)
add('CRFR2 drugs shift sampled oxytocin in opposing directions','O','b16_4','4','Opposing oxytocin changes after receptor manipulation.', '''In the microdialysis experiment, CRFR2 agonist treatment was associated with lower accumbens oxytocin relative to the preceding sample. The reported immediate decrease was about 24%, followed by a decrease of about 20% in the next interval. Vehicle infusion lacked a comparable directional change.

CRFR2 antagonist treatment was associated with an approximately 48% increase after a 30-minute delay. These estimates arose from planned within-group comparisons; the overall treatment-by-time analysis was inconclusive. The directional effect therefore remains tentative rather than a settled measurement of a complete release mechanism.

The authors proposed that increased CRFR2 signaling reduces the local oxytocin support for active coping. This hypothesis connects the sampled peptide changes to the opposing behavioral effects of receptor activation and blockade in the accumbens shell.''',anatomy=True)
add('Selective labeling enables oxytocin-cell recordings','O','b16_5a','5A','Venus labeling distinguishes oxytocin from vasopressin cells.', '''A **brain slice** preserves local tissue and synaptic connections for electrical recording outside the animal. To target oxytocin neurons, Bosch and colleagues used Venus fluorescence in the PVN. Antibody labeling confirmed that reporter-positive neurons overlapped with oxytocin rather than with neighboring vasopressin-positive cells.

**Patch-clamp recording** creates an electrical connection through a fine pipette at the neuronal membrane. In voltage clamp, the experimenter controls membrane voltage and records the currents required to hold it there, allowing small incoming synaptic events to be measured.

Cell identification is essential because nearby peptide-producing neurons can have different functions. The reporter makes the physiological response attributable to the selected oxytocin population, connecting receptor pharmacology to a defined cell type in the hypothalamic source of the accumbens peptide pathway.''')
add('CRFR2 activation reduces excitatory input frequency','O','b16_5bc','5B–C','Excitatory synaptic events during stresscopin exposure.', '''A **spontaneous excitatory postsynaptic current**, or **sEPSC**, is an inward synaptic current recorded without deliberately stimulating an incoming axon. Its frequency describes how often detectable excitatory events arrive, while its amplitude describes the size of each event at the recorded membrane voltage.

Applying 200 nM stresscopin for 10 minutes reduced the mean sEPSC frequency in identified oxytocin neurons from about 6.64 to 4.76 Hz. Following washout, frequency recovered partly to about 5.83 Hz. Event amplitudes retained a similar distribution during treatment.

The frequency change means the cells received fewer excitatory events during receptor activation. The authors interpreted the combination of reduced frequency and stable amplitude as consistent with presynaptic regulation of excitatory drive, linking CRFR2 signaling to input onto the oxytocin-producing population.''')
add('Synaptic input changes without a broad membrane shift','O','b16_5bc','5B–C','Event intervals and amplitudes under CRFR2 activation.', '''**Intrinsic membrane properties** describe how a neuron responds electrically apart from changes in its incoming synaptic activity. The Bosch study examined input resistance, membrane charging, action-potential threshold, and spike kinetics in reporter-positive PVN neurons during stresscopin exposure.

These intrinsic measures were broadly preserved at the tested 200 nM concentration. In contrast, excitatory events became less frequent and the distribution of intervals between events shifted toward longer gaps. Event amplitude was preserved, separating the timing of incoming excitation from its individual size.

The physiological response therefore centers on synaptic drive rather than a broad suppression of membrane excitability. The authors' proposed pathway links reduced excitation of oxytocin neurons with altered peptide support for active coping, alongside possible regulation at their accumbens fibers.''')
add('Established preference survives dopamine antagonism','D','p24_1','1A–H','Partner preference under D1- and D2-class antagonism.', '''**Dopamine** is a neuromodulator involved in motivation and reward-related behavior. Pierce and colleagues tested established prairie vole bonds using antagonists of D1-class and D2-class dopamine receptors. The partner preference test offered low-effort access to a partner and an unfamiliar animal.

Systemic SCH-23390 at 0.5 mg/kg blocked D1-class receptors, while eticlopride at 2 mg/kg targeted D2-class receptors. Neither treatment eliminated the established partner preference during the first test hour. D2 antagonism increased the proportion of partner huddling while also reducing locomotion.

The retained preference separates expression of an established social choice from dopamine-dependent processes engaged during bond formation or active seeking. Once access is freely available, selective contact can persist while receptor pharmacology changes other aspects of behavior.''')
add('D1 blockade reduces effortful social seeking','D','p24_2fgh','2F–H','Lever pressing and response latencies under D1 blockade.', '''An **operant task** makes an outcome depend on an animal's action. In the Pierce study, female voles learned to press a lever to gain access to a partner or novel vole. Lever pressing measures willingness to perform an action for social access rather than preference when both animals are freely available.

After learning, systemic D1-class antagonism reduced pressing for both partner and novel access and increased the latency to press. Latency to enter the social chamber after opening was preserved. The drug therefore affected initiation of the access-seeking action more than subsequent entry.

This behavioral separation connects dopamine signaling to the appetitive phase of social interaction. **Appetitive behavior** obtains a desired outcome, whereas **consummatory behavior** occurs once it is available; lever pressing and freely available huddling engage different requirements.''')
add('D2 blockade preserves pressing for social access','D','p24_2ijk','2I–K','Social operant behavior under D2 blockade.', '''Pierce and colleagues compared D2-class antagonism with the D1-class manipulation using the learned social access task. The animal could earn encounters with either its partner or an unfamiliar vole, allowing receptor effects to be compared across two social outcomes under the same response requirement.

D2 blockade preserved lever pressing, latency to press, and latency to enter the social chamber. This contrasts with the reduction in pressing caused by D1 antagonism. D2 treatment nevertheless reduced locomotion in the separate partner preference test.

The receptor comparison distinguishes social seeking from a simple measure of overall movement. Reduced free locomotion under D2 treatment coexisted with retained operant responding, whereas D1 treatment reduced effortful social actions without broadly suppressing movement in the preference apparatus.''')
add('Barrier climbing also depends on D1-class signaling','D','p24_2lmn','2L–N','Voles climb toward a partner under receptor treatments.', '''Prairie voles will climb a mesh barrier to obtain access to a bonded partner. This response uses an immediate obstacle rather than a learned lever-action rule. Pierce and colleagues measured climbing attempts under vehicle, D1-class antagonist, and D2-class antagonist conditions.

D1 antagonism reduced attempts to climb, while D2 antagonism preserved them. The animals had an independently confirmed partner preference. Real photographs in the source document the climbing behavior, linking the access-seeking measure to the animal's physical actions.

The shared effect across climbing and lever pressing connects D1-class signaling to effortful social pursuit under different task demands. Both behaviors obtain contact, whereas huddling after unrestricted access can retain partner selectivity under the same broad receptor manipulation.''')
add('A fluorescent sensor tracks accumbens dopamine','D','p24_3b','3B','Sensor expression and recording track in the accumbens.', '''**GRABDA** is a genetically encoded fluorescent sensor that changes its signal in response to dopamine. Pierce and colleagues expressed it in the accumbens shell and used an implanted optical fiber to collect fluorescence during social behavior. This **fiber photometry** measurement tracks a local population-level optical signal over time.

Histology verified sensor expression and the recording track within the intended region. A second fluorescent marker aided localization. The published micrographs preserve the accumbens tissue and 500 µm scale bars, connecting the recorded signal to the actual brain preparation.

The sensor allowed dopamine-related responses to be aligned to lever presentation, pressing, door opening, and chamber entry with subsecond timing. Event-resolved measurements separate motivation before access from the subsequent encounter with a partner or novel animal.''')
add('Learning increases dopamine responses to access cues','D','p24_3jk','3J–K','Event-aligned dopamine signals during task learning.', '''In the social operant task, voles encountered a sequence of events: a lever appeared, a press earned access, a door opened, and the animal entered the social chamber. These events were time-stamped so dopamine-sensor fluorescence could be compared at equivalent moments on early and late training days.

By day 6, dopamine responses were greater around lever presentation, pressing, and chamber opening than on day 1. Chamber-entry responses were more stable across learning. The authors summarized event-associated fluorescence over the 2 seconds following each event.

The temporal redistribution links dopamine dynamics to learning that particular actions and cues predict social access. The signal changes before contact becomes available, connecting the access-seeking phase with anticipation of a social outcome.''',anatomy=True)
add('Partner seeking evokes larger dopamine responses','D','p24_4fg','4F–G','Dopamine during partner and novel access events.', '''Pierce and colleagues alternated blocks in which pressing earned access to the bonded partner or to a novel vole. Pressing rates and response latencies were similar for the two social targets once the task was learned, making it possible to compare neural signals during matched actions.

Partner-directed pressing and door opening elicited greater accumbens dopamine responses than the same events during novel trials. Differences were less evident at lever presentation and immediately after chamber entry. The effect therefore depended on the specific event within the access sequence.

The authors proposed that dopamine responses reflect the motivational value assigned to the bonded partner. Target identity changed the signal even when overt access-seeking performance was similar, providing a neural distinction that a simple count of lever presses would miss.''',anatomy=True)
add('Four weeks apart reduces partner-associated dopamine','D','p24_4kl','4K–L','Partner-event dopamine before and after separation.', '''After confirming the bond and recording stable operant performance, Pierce and colleagues separated pairs for 4 weeks. The same animals then completed a probe session with the familiar partner and a novel animal. This design compares the social signals of an individual before and after prolonged loss of contact.

Partner-associated dopamine responses decreased at lever presentation, door opening, and chamber entry. Pressing still occurred, although total presses fell and entry became slower. The relative dopamine advantage for partner over novel access was reduced.

The within-animal comparison connects prolonged separation to remodeling of partner-related reward signals. A previously distinctive social target elicited a smaller response at several access events, even though the vole could still execute the learned action sequence.''',anatomy=True)
add('Novel-target responses remain comparatively stable','D','p24_4mn','4M–N','Novel-event dopamine before and after separation.', '''The post-separation session retained novel-vole trials as well as trials with the former partner. These novel trials provided a comparison for the same recording preparation, task events, and time interval. The contrast tests whether prolonged separation changes every social dopamine response in the same direction.

Dopamine responses during novel-target lever presentation, pressing, chamber opening, and entry were comparatively stable across the separation interval. The reduction was concentrated in partner-associated responses rather than a uniform decrease across all recorded social events.

This target-specific pattern supports the authors' hypothesis of reduced partner-related motivational value. Continued sensor responses to novel access and continued task performance distinguish changes in social selectivity from a general loss of detectable fluorescence or complete disappearance of the learned task.''',anatomy=True)
add('Partner contact loses its dopamine advantage','D','p24_5de','5D–E','Dopamine during direct social contact before and after loss.', '''**Direct contact investigation** includes sniffing the other animal's head, body, and anogenital region. Pierce and colleagues scored these encounters after social chamber entry while recording dopamine-sensor fluorescence. Partner and novel investigations can thus be compared during similar types of physical contact.

Before separation, direct contact with the partner produced greater dopamine responses than comparable contact with a novel vole. After 4 weeks apart, that difference was absent. Contact investigation itself continued and its overall duration increased following separation.

The neural adaptation therefore accompanies a change in the relative signal attached to contact rather than elimination of social investigation. The same broad behavior can persist while its partner-specific dopamine association weakens, separating overt social engagement from selective reward signaling.''',anatomy=True)
add('Partner huddling persists as dopamine selectivity weakens','D','p24_5hi','5H–I','Huddling-related dopamine before and after separation.', '''Huddling is sustained affiliative contact, distinct from brief sniffing or approach. Pierce and colleagues measured both huddling bouts and the dopamine response associated with huddle onset. Before separation, partner huddling produced a greater dopamine response than huddling with a novel vole.

After 4 weeks apart, the partner-specific neural difference disappeared. Nevertheless, animals retained a greater cumulative number of huddling bouts with the partner. Total huddle duration changed little, so bout counts and summed contact time described different aspects of social allocation.

Partner familiarity and some selective affiliation therefore persist while dopamine responses become less differentiated. The result teaches loss adaptation as a change in multiple components of a relationship, with neural reward selectivity and behavioral recognition following partially different trajectories.''',anatomy=True)
add('Investigation without contact follows a different pattern','D','p24_5jk','5J–K','Non-contact investigation before and after separation.', '''**Non-contact investigation** occurs when a vole orients and sniffs toward another animal without direct physical contact. This distinguishes remote sampling from body investigation and huddling. Pierce and colleagues scored each behavior separately instead of combining all social activity into one total.

Before separation, non-contact investigation occurred more often toward novel animals, unlike the partner bias in direct contact and huddling. After separation, non-contact investigation became shorter and the difference in bout accumulation between targets was reduced.

Different social acts therefore organize around different features of an encounter. Novelty favors remote investigation, while familiarity favors close affiliative contact. Separation changes this behavioral allocation alongside the weakening of partner-associated dopamine responses measured during seeking and contact.''')
add('Partner preference can outlast prolonged separation','T','s23_1b','1B','Partner preference across pairing and separation.', '''Sadino and colleagues paired male prairie voles with an opposite-sex partner or a same-sex sibling for 2 weeks. Partner preference was measured before separation and again after 48 hours or 4 weeks apart. Removed partners were housed in another room, eliminating ongoing contact through sight, smell, or sound.

Both opposite-sex and same-sex pairs retained greater huddling with the familiar animal than with a novel one after prolonged separation. The baseline affiliation was therefore more persistent than the authors had initially hypothesized.

This behavioral persistence provides a reference for interpreting molecular adaptation to loss. Changes in accumbens gene expression can occur while a familiar partner still attracts selective contact, so separation-related neural remodeling need not wait until the preference test becomes indifferent.''')
add('Continued cohabitation strengthens partner contact','T','s23_1c','1C','Partner and novel huddling during continued pairing.', '''Sadino and colleagues followed animals that remained together over the same interval used for the separation groups. This comparison distinguishes changes caused by prolonged separation from the ongoing maturation of a relationship during continued cohabitation.

Partner huddle duration increased over time in the remain-paired animals, while novel huddling changed little. Males separated from the partner lacked the same overall strengthening of partner-directed contact. Initial preference could persist even as its normal growth was interrupted.

Relationship maintenance therefore includes continued behavioral change rather than preservation of a single fixed score. Repeated cohabitation can increase selective contact, and partner removal can halt this trajectory while leaving the earlier familiar-partner preference measurable.''')
add('Accumbens transcription remains stable during pairing','T','s23_2d','2D','Gene-expression differences at two pairing durations.', '''**Transcription** produces RNA from a gene, and **RNA sequencing** measures the representation of many transcripts in a tissue sample. Sadino and colleagues sampled the nucleus accumbens after 2 or 6 weeks of cohabitation, comparing opposite-sex pairs with same-sex pairs to identify expression differences associated with mating partnerships.

Patterns of relative transcript expression were similar at the two pairing durations. Genes elevated in opposite-sex pairs tended to remain elevated, while genes reduced relative to same-sex pairs retained that direction. The published heatmap summarizes these relationships across transcripts.

This consistent **transcriptional signature** provides a molecular reference for the intact bond. Subsequent separation-related changes can be evaluated against a pattern that normally persists during continued cohabitation rather than against an arbitrary single-timepoint sample.''',anatomy=True)
add('Bond-associated transcripts include glial processes','T','s23_2h','2H','Biological processes associated with bond-related genes.', '''**Glia** are non-neuronal brain cells that support, regulate, and interact with neurons. Tissue-level RNA sequencing includes glial transcripts as well as neuronal ones. Sadino and colleagues analyzed which biological processes were associated with the genes differing between opposite-sex and same-sex paired males.

Elevated transcripts in opposite-sex pairs were associated with glial differentiation and related developmental processes. Other transcript groups implicated synaptic organization and vesicle docking, the positioning of transmitter-containing vesicles for release at synapses.

The expression profile therefore distributes across several cellular functions rather than a single peptide receptor. The authors proposed a glial contribution to bond-associated accumbens adaptation, motivating a second analysis that isolates neuronal transcripts from the mixed-cell tissue measurement.''',anatomy=True)
add('Short separation preserves much of the bond signature','T','s23_3e','3E','Transcriptional concordance after short and long separation.', '''Sadino and colleagues compared the intact-bond expression pattern with accumbens samples collected after 48 hours or 4 weeks of separation. Both separation groups began with the same 2-week pairing period, allowing the duration without the partner to define the later comparison.

After 48 hours, many transcripts retained directions of change consistent with the intact bond. The same pattern was much less concordant after 4 weeks. **Concordance** here means that genes tending to be elevated or reduced in the bond also tend to change in the same direction in the comparison condition.

The molecular adaptation develops across time rather than appearing as an immediate complete erasure. A short absence preserves much of the coordinated expression pattern, while prolonged absence reorganizes it despite continued behavioral preference for the familiar partner.''',anatomy=True)
add('Prolonged loss erodes coordinated expression patterns','T','s23_3hi','3H–I','Eroded gene groups across bonding and separation.', '''**Transcriptional erosion** in the Sadino study means weakening or reversal of the expression pattern associated with an intact pair bond. It describes coordinated differences across RNA measurements, rather than a literal loss of brain tissue or disappearance of every transcript.

Some genes elevated during pairing and short separation became reduced after prolonged separation. A complementary group that was reduced during the intact bond shifted in the opposite direction. The published heatmaps retain the source's expression scales and display the two trajectories separately.

The adaptation therefore involves bidirectional reorganization of the accumbens molecular state. Both previously elevated and previously reduced transcript groups change over time, linking social loss to a broad remodeling process instead of a single uniform decrease in gene activity.''',anatomy=True)
add('Loss alters glial and synaptic expression programs','T','s23_3jk','3J–K','Processes associated with eroded bond-related transcripts.', '''Sadino and colleagues identified biological processes associated with transcript groups whose bond-related pattern eroded after separation. This analysis groups genes by known functional annotations, allowing a coordinated expression change to be related to candidate cellular functions rather than to isolated gene names.

The eroded groups included glial-associated processes, synapse organization, and vesicle docking. Proposed upstream regulators included factors involved in developmental signaling and cellular regulation. These are associations within the expression analysis, not direct measurements of synapse number or transmitter release.

The authors' hypothesis is that the accumbens gradually reorganizes functions supporting the intact bond as the animal adapts to prolonged absence. Separating annotated functions from directly measured physiology keeps the cellular interpretation tied to what RNA sequencing actually samples.''',anatomy=True)
add('Neuron-enriched transcripts separate mixed-cell signals','T','s23_4e','4E','Cell-type expression of neuron-enriched transcripts.', '''**Translating ribosome affinity purification**, adapted for voles as **vTRAP**, isolates messenger RNAs attached to genetically tagged ribosomes in selected cells. Ribosomes are the cellular structures that build proteins from RNA instructions. A neuron-selective construct allowed Sadino and colleagues to enrich transcripts being translated in neurons.

The enriched transcript set included dopamine-receptor and other neuronal genes, while reducing the contribution of glial-associated transcripts. Comparison with a rat accumbens single-nucleus dataset placed the selected genes predominantly in neuronal cell classes, including **medium spiny neurons**, striatal projection cells with spine-bearing dendrites.

This cellular separation complements tissue-level sequencing. Mixed accumbens tissue reveals the overall social-loss signature, while neuron-enriched analysis resolves expression programs that might otherwise be obscured by the strong glial component of the bond-associated pattern.''',anatomy=True)
add('Neuronal gene programs follow different loss timescales','T','s23_4g','4G','Functional annotations of three neuronal gene clusters.', '''A **gene-expression cluster** groups transcripts with related trajectories across experimental conditions. Sadino and colleagues identified three neuronal clusters with distinct changes across intact pairing, short separation, and long separation. The trajectories distinguish early responses to loss from later molecular adaptation.

One cluster rose during bonding and short separation but declined after prolonged loss. Another increased rapidly after separation and included dopamine-related genes such as Drd1a and Drd2. A third increased mainly after long separation and was associated with mitochondrial and other metabolic processes.

The neuronal response therefore contains both signaling-related and cellular-energy components. The authors proposed that these temporally distinct programs participate in loss adaptation and readiness for future bonding, rather than treating every transcript change as the same acute stress response.''',anatomy=True)
add('Social loss separates coping, reward, and affiliation','T','s23_1de','1D–E','Partner and novel huddling following separation.', '''Prairie vole partner separation engages several experimentally distinguishable responses. Within days, male coping behavior changes with CRF and oxytocin manipulations. Over weeks, accumbens dopamine responses to a partner weaken and bond-associated transcript patterns reorganize. These findings describe different physiological measurements and social tasks.

The Sadino study nevertheless found continued familiar-partner preference after 4 weeks apart. Pierce and colleagues also observed retained partner-biased contact bouts despite reduced partner-specific dopamine responses. Selective affiliation therefore persists alongside changes in reward signaling and molecular state.

Loss adaptation is a coordinated but uneven process across the attachment system. Stress-related coping, motivation to obtain contact, recognition of a familiar animal, and accumbens cellular programs each supply a distinct part of the biological account of separation.''')
S[-1]['cite']='Bosch et al. (2009, 2016); Pierce et al. (2024); Sadino et al. (2023)'
S[-1]['refs']=list(R.values())
items=[
('Relationship specificity','Female-partner separation increases passive coping more clearly than sibling separation in the male vole preparation.'),
('CRF and oxytocin','Accumbens-shell CRFR2 activation favors passive coping, while local oxytocin signaling supports more active coping.'),
('Defined neuronal inputs','CRFR2 activation reduces excitatory-event frequency in identified hypothalamic oxytocin neurons while broadly preserving intrinsic membrane properties.'),
('Seeking versus contact','D1-class signaling supports effortful social seeking, while an established low-effort partner preference can survive receptor antagonism.'),
('Partner-related dopamine','Prolonged separation reduces the dopamine advantage associated with partner seeking and contact, alongside continued social engagement.'),
('Time-dependent remodeling','Accumbens bond-related transcription erodes across prolonged separation; neuronal signaling and metabolic programs follow different trajectories while familiar-partner preference can persist.')]
photo={'path':'photos/prairie_vole.png','kind':'web','caption':'Photo: Prairie vole (Microtus ochrogaster).','credit':'Nastacia Goodwin','license':'CC BY-SA 4.0','source_url':'https://commons.wikimedia.org/wiki/File:Prairie_Vole_Nastacia_Goodwin_CC_BY-SA.png'}
assert len(S)==44,len(S)
spec={'lecture':59,'theme':'muted-rose-paper','content_slides':44,'title_height':3.1,'title_image':photo,'title_refs':list(R.values()),'slides':S,'takeaways':{'items':[{'lead':a,'text':b} for a,b in items],'cite':'Bosch et al. (2009, 2016); Pierce et al. (2024); Sadino et al. (2023)','refs':list(R.values())}}
(ROOT/'lecture.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2))
(ROOT/'REFERENCES.md').write_text('# Verified primary references\n\n'+'\n\n'.join(R.values())+'\n')
(ROOT/'PLAN.md').write_text('# Lecture 59: slide claims\n\n'+'\n'.join(f'{i+2}. {s["title"]} ({s["cite"]})' for i,s in enumerate(S))+'\n')
