"""Lecture 54: source-grounded text and original article panels only."""
import json,re
from pathlib import Path
root=Path(__file__).resolve().parent
scratch=Path('/workspace/scratch/L54')
years={'D':2016,'C':2020,'P':2020,'H':2019,'N':1992,'G':1998,'S':2008,'I':2009}
cites={'D':'Somppi et al. (2016)','C':'Quaranta et al. (2020)','P':'Salonen et al. (2020)','H':'van der Leij et al. (2019)','N':'Lu et al. (1992)','G':'Cheu & Siegel (1998)','S':'Bhatt et al. (2008)','I':'Bhatt et al. (2009)'}
refs={};dois={}
for key in years:
 m=json.loads((scratch/f'{key}_metadata.json').read_text());m=m.get('message',m)
 authors=', '.join(a['family']+' '+''.join(x[0] for x in re.findall(r'[A-Za-zÀ-ž]+',a.get('given',''))) for a in m['author'])
 refs[key]=f"{authors} ({years[key]}). {m['title'][0]}. {m['container-title'][0]} {m['volume']}({m.get('issue','')}): {m.get('page',m.get('article-number',''))}. https://doi.org/{m['DOI']}"
 dois[key]='https://doi.org/'+m['DOI']
figinfo={
'd1dog':('D','1 (dog rows)','Dog facial stimuli and the published gaze distributions'),
'd1':('D','1','Dog and human facial stimuli with published gaze distributions'),
'd2':('D','2A,B','Expression-dependent fixation scores and first fixations'),
'd3':('D','3','Fixation scores for eyes, midface, and mouth'),
'd4':('D','4','Original first-fixation targets and scanning paths; circle key is 500 ms'),
'c1cat':('C','1 (cat rows)','Hiss and purr faces with corresponding waveforms and sonograms'),
'c1human':('C','1 (human rows)','Happiness and anger stimuli with corresponding vocalizations'),
'c3':('C','3','Congruence scores for matching facial and vocal emotional cues'),
'c4':('C','4','Stress-related behavior during emotional stimulus presentations'),
'p1':('P','1a,b','Reported prevalence of canine anxiety traits and subtraits'),
'p2a':('P','2a','Co-occurrence of reported behavioral traits'),
'p2b':('P','2b','Relative risks of co-occurring reported traits'),
'p3':('P','3a–d','Age and sex distributions of reported behavioral traits'),
'n1':('N','1A,B','PAG and medial hypothalamic stimulation sites'),
'n2':('N','2','Kynurenic acid reverses hypothalamic facilitation of the PAG response'),
'n3':('N','3','AP7 dose and recovery time compared with CNQX'),
'n4':('N','4','NMDA microinjection decreases hissing latency'),
'n5':('N','5A,B','PAG tracer sites and hypothalamic amino-acid labeling'),
'n6ab':('N','6A–C','PAG tracer site, aspartate-positive fibers, and hypothalamic cells'),
'n6def':('N','6D–F','Retrogradely labeled hypothalamic cells and double-labeled neuron'),
'g1':('G','1','Medial defensive sites and lateral suppressive sites'),
'g2':('G','2','Single and dual stimulation differ in hiss latency'),
'g3':('G','3','Bicuculline blocks lateral hypothalamic suppression'),
'g4':('G','4','Bicuculline does not change single-stimulation latency'),
'g5':('G','5','Muscimol increases the current threshold for defensive rage'),
'g6':('G','6','Bicuculline pretreatment blocks muscimol suppression'),
'g7':('G','7','Baclofen leaves hissing latency unchanged'),
'g8':('G','8','Lateral hypothalamic muscimol leaves latency unchanged'),
'g9':('G','9','Original medial hypothalamic tracer injection histology and localization'),
'g11':('G','11A–F','GABA and tracer labeling in lateral hypothalamic neurons'),
's1':('S','1','Hypothalamic and PAG sites with original anatomical sections'),
's2':('S','2','Concurrent stimulation facilitates the hissing response'),
's3':('S','3','PAG IL-1β dose and time dependence of hissing facilitation'),
's4a':('S','4a','IL-1 receptor antibody blocks cytokine facilitation'),
's4b':('S','4b','Isotype antibody does not block cytokine facilitation'),
's5a':('S','5a','Serotonin receptor blockade prevents IL-1β facilitation'),
's5bc':('S','5b,c','NK-1 and CCKb blockade leave cytokine facilitation intact'),
's6':('S','6A–E','Original PAG receptor labeling and antibody validation'),
's6abcd':('S','6A–E','Original PAG receptor labeling and antibody validation'),
's6a':('S','6A,D','PAG tissue surrounding the aqueduct and receptor labeling; 100 μm bar'),
'i1':('I','1A,B','PAG and hypothalamic sites with original anatomical sections'),
'i2':('I','2A–C','Peripheral LPS, fever, and local LPS have different effects'),
'i3':('I','3A–D','Peripheral TNF neutralization blocks LPS effects'),
'i4':('I','4A–C','Hypothalamic prostaglandin and serotonin blockade oppose LPS effects'),
'i4b':('I','4B','Hypothalamic prostaglandin blockade opposes LPS suppression'),
'i4c_full':('I','4C','Hypothalamic serotonin blockade opposes LPS suppression'),
'i5':('I','5','LPS suppresses hissing but spares elicited head turning'),
'h1':('H','1','Individual Cat-Stress-Score trajectories with and without hiding boxes'),
'h2':('H','2','Individual body-weight changes during shelter quarantine'),
}
def figure(name):
 k,panel,desc=figinfo[name]
 author={'D':'Somppi et al.','C':'Quaranta et al.','P':'Salonen et al.','H':'van der Leij et al.','N':'Lu et al.','G':'Cheu & Siegel','S':'Bhatt et al.','I':'Bhatt et al.'}[k]
 return {'path':f'figures/{name}.png','kind':'article','caption':f'{author} ({years[k]}), Fig. {panel}. {desc}.','source_url':dois[k]}
slides=[]
def add(title,k,names,text,note):
 body=text.strip().split('\n\n');assert len(body)==3,(title,len(body))
 wordcount=len(re.findall(r'\S+',text));assert 90<=wordcount<=170,(title,wordcount)
 keys=list(dict.fromkeys([k]+[figinfo[n][0] for n in names]))
 sd={'title':title,'body':body,'cite':'; '.join(cites[x] for x in keys),'refs':[refs[x] for x in keys], 'transcript':[[body[0],[note]],body[1],body[2]]}
 if len(names)==1:sd.update(layout='figure-right',figure=figure(names[0]),figure_width=5.6)
 else:sd.update(layout='figures-right',figures=[figure(n) for n in names],figure_width=5.6,primary_figure_height=2.7)
 slides.append(sd)

add('Dogs allocate gaze according to the source of threat','D',['d2','d1dog'],'''
**Threat recognition** is discrimination of cues associated with possible harm. Somppi and colleagues measured dogs’ spontaneous gaze toward photographs of dog and human faces bearing threatening, pleasant, or neutral expressions. Each photograph appeared for 1500 ms.

Dogs devoted more viewing time to the inner faces of threatening dogs than to pleasant or neutral dog faces. Their response to threatening human faces differed: initial fixations were less likely to land within the inner face than for pleasant or neutral humans.

The experiment controlled presentation duration and compared expressions within each depicted species. The result establishes expression-dependent visual attention, rather than a direct measurement of fear, attack probability, or subjective emotional experience.
''','The inner face comprises the eyes, midface, and mouth; looking time describes visual sampling rather than the animal’s entire defensive response.')
add('Brief presentations isolate spontaneous visual sampling','D',['d1dog'],'''
Dogs watched facial photographs while resting their heads voluntarily on a chin support. An infrared **eye tracker**, an instrument estimating gaze position, recorded where each dog looked without requiring a trained choice between emotional categories.

Images appeared for 1500 ms, separated by 500 ms intervals. Stimulus order and block length were randomized, while owners and experimenters waited behind an opaque barrier. These procedures reduced predictable sequences and immediate social guidance during viewing.

Calibration related measured eye position to known screen locations. The measured outcome was spontaneous fixation allocation, not successful completion of a rewarded emotion-labeling task. Because the stimuli were still photographs, the study did not test moving bodies, approaching animals, or the coordination of escape with gaze.
''','Training accustomed dogs to the apparatus; it did not train an emotional classification response to the test photographs.')
add('Dogs prioritize eyes over exposed teeth','D',['d3','d1dog'],'''
A **fixation** is a period during which gaze remains within a restricted area. Facial regions were classified as eyes, midface, and mouth, allowing Somppi and colleagues to compare visual sampling of different components of an expression.

Across dog and human faces, dogs looked longer at eyes than at mouths. Average entry times were about 503 ms for eyes, 501 ms for midface, and 584 ms for mouths. Thus, exposed teeth were not the only visual information sampled during threatening expressions.

Fixation scores accounted for facial-region size and total face-viewing time. The comparison supports structured sampling of facial information. It does not identify the neural detector for threat or establish that a single facial feature determines a defensive reaction.
''','Entry time is the interval from image onset to the first fixation in a defined region; it is distinct from the duration spent looking there.')
add('Threatening human faces alter initial orienting','D',['d2','d4'],'''
**Initial orienting** describes where attention is directed at the beginning of stimulus inspection. The probability of a first fixation landing on the inner face was lower for threatening human expressions than for pleasant or neutral human expressions.

The same dogs viewed conspecific faces, meaning faces of their own species. Threatening dog faces received more inner-face viewing than other dog expressions. Consequently, the visual response depended jointly on expression and the species producing the signal.

The first-fixation analysis adjusted for the relative size of the target region. Reduced initial gaze toward human threat is compatible with avoidance, but gaze alone cannot establish the animal’s motivation. No neural recording or circuit intervention accompanied these 1500 ms presentations.
''','The comparison separates an early orienting measure from sustained fixation; these measures need not vary in parallel.')
add('Gaze heat maps locate attention without measuring fear','D',['d1'],'''
A **gaze heat map** represents the distribution of recorded fixations across a stimulus. The published maps from Somppi and colleagues place dogs’ gaze on eyes, muzzle, and mouth during presentations lasting 1500 ms.

The analysis compared threatening, pleasant, and neutral faces of both humans and dogs. It normalized looking duration for facial-region size, reducing the possibility that a larger mouth or eye region automatically receives a larger score simply because it occupies more space.

These maps describe visual attention rather than neuronal activation. They cannot locate an amygdala response or distinguish arousal from avoidance without additional measurements. Expression-dependent gaze is evidence that the visual system discriminates social cues; the downstream defensive state remains a separate experimental question.
''','The colors are the authors’ original fixation distributions, not a reconstructed brain map or an added interpretation of the dog’s emotional state.')
add('Facial scanning reflects several competing cues','D',['d4'],'''
Dogs’ first fixations and subsequent scanning paths sampled multiple parts of a face. Somppi and colleagues recorded these paths during 1500 ms presentations, with fixation duration and entry time providing different descriptions of visual attention.

Threatening dog faces received greater sustained sampling than pleasant or neutral dog faces, while threatening human faces were less likely to receive an initial inner-face fixation. The distinction prevents a simple rule that every threatening expression should produce longer looking.

The authors compared expressions within species and considered image properties when analyzing gaze. Nonetheless, a photograph does not provide the motion, distance, vocalization, or opportunity to withdraw present in a real encounter. Visual discrimination and defensive behavior therefore require different measured outcomes.
''','Long looking can reflect vigilance, whereas reduced looking can reflect disengagement; this experiment does not assign either interpretation solely from fixation duration.')

add('Cats match hissing sounds to threatening faces','C',['c3','c1cat'],'''
**Cross-modal recognition** is matching information carried by different senses. Quaranta and colleagues presented cats with two facial expressions of the same individual while playing a vocalization matching only one expression. A presentation lasted 5 s.

Cats looked longer at the congruent face when hearing a conspecific hiss. They also matched human anger and happiness vocalizations to the corresponding human expressions. **Congruent** means that the expression and sound belonged to the same emotional condition.

Neutral Brownian sound provided a control without the emotional vocal cue. Preferential matching supports integration of visual and auditory social information. It does not prove that cats experience the displayed emotion or identify the neurons performing this integration.
''','The face matching the hiss competes with a different expression of the same cat, limiting a simple explanation based on individual identity alone.')
add('Matched sound intensity controls one source of arousal','C',['c1cat'],'''
The cat recognition study used hissing and purring recorded during different social conditions. Hiss recordings came from a threatening encounter involving an approaching dog; purr recordings came from relaxed interactions with owners.

Recordings were adjusted to 69 dB at the tested cat’s position. Facial photographs were converted to grayscale in the published experiment. These controls reduced sound-intensity and image-color differences as explanations for matching an expression to a vocalization.

Each audiovisual presentation lasted 5 s, allowing spontaneous gaze to either face. The published waveform and sonogram preserve time and frequency information from the actual stimuli. Matching cannot be reduced to loudness alone, but acoustic and facial features still differ between emotional conditions and contribute to their discrimination.
''','A sonogram depicts how acoustic frequency content varies through time; frequency is measured in kilohertz and elapsed time in seconds in the source figure.')
add('Human anger increases cats’ stress-related behavior','C',['c4','c1human'],'''
Quaranta and colleagues scored cats’ behavior during audiovisual presentations of human anger, human happiness, cat hissing, and cat purring. **Stress-related behavior** was operationalized as the observed frequency of specified behavioral signs, rather than inferred directly from facial matching.

Cats expressed more stress-related behavior during human anger and cat hiss presentations than during human happiness or cat purr presentations. Sounds were standardized to 69 dB, and the same 5 s presentation procedure was used across conditions.

The behavioral score complements the gaze measure by assessing the recipient’s response. It does not measure circulating stress hormones or record brain activity. A threatening communication signal can alter behavior even when the recipient does not attack the sender.
''','Operationalization states exactly what was counted; it does not make the observed score identical to an unobserved subjective feeling.')
add('Purring does not produce the same matching result','C',['c3','c1cat'],'''
Cats did not display reliable preferential matching for the purr condition in the Quaranta study, although they matched cat hissing and both tested human emotional conditions. This asymmetry limits a claim that every affective vocalization is linked equally strongly to a distinctive facial expression.

The **congruence index** describes relative looking toward the matching face. A value of 1 indicates exclusive matching-face looking, a value of −1 indicates exclusive nonmatching-face looking, and zero indicates balanced looking.

Presentations lasted 5 s and compared expressions of the same individual. The absence of reliable purr matching may reflect the tested cues, task, or their salience. It does not establish that cats cannot perceive purring or recognize relaxed social contexts.
''','A null matching result concerns the experimental contrast, not the animal’s general ability to hear or interpret the vocalization.')
add('Matching is tested against a neutral auditory control','C',['c3','c1human'],'''
The cat recognition experiment paired emotional faces with a neutral Brownian sound as a control condition. **Brownian sound** is a nonvocal noise stimulus; here it supplied auditory stimulation without a human or cat emotional vocalization.

Cats did not reliably prefer either emotional face in these control presentations. In contrast, human anger and happiness vocalizations supported preferential looking toward the matching expression during 5 s trials. Owners were instructed to avoid interacting with their cats during the presentations.

The neutral condition weakens an explanation based solely on a fixed preference for one facial photograph. Because no sensory pathway was disrupted, the experiment establishes behavioral audiovisual matching rather than causal dependence on a specific brain region or receptor.
''','The design controls for a baseline picture preference while preserving an auditory event in the control condition.')

add('Canine fears vary with the provoking stimulus','P',['p1'],'''
**Fear** refers to a defensive response associated with a threat, while anxiety-related traits describe broader recurring patterns of apprehensive behavior. Salonen and colleagues used owner reports to assess noise sensitivity, social fear, surface-related fear, and several other behavioral traits.

Highly noise-sensitive behavior was reported in 32% of the surveyed dogs, and fear in 29%. Fireworks were the most commonly reported noise trigger. Fear of other dogs was the most common social-fear subtrait in this sample.

These percentages describe the recruited survey population and the study’s operational thresholds. They do not establish population-wide prevalence or identify a neurotransmitter deficiency. Distinguishing triggers preserves information about sensory context that would be lost by treating all fearful behavior as one uniform phenotype.
''','An owner questionnaire samples recurring behavior in the home environment; it does not expose each dog to an identical calibrated threat.')
add('Fear and aggression overlap without being identical','P',['p2b'],'''
**Comorbidity** is the occurrence of more than one classified condition in the same individual. In Salonen and colleagues’ owner-reported survey, dogs classified as aggressive were 3.2 times more often classified as fearful than dogs without that aggression classification.

The study separately scored fear and aggression, rather than defining aggression as proof of fear. Fear also overlapped with noise sensitivity and separation-related behavior. These associations connect several behavioral dimensions while preserving their separate definitions.

A cross-sectional survey measures co-occurrence at the time of reporting. It cannot establish that fear caused aggression, that aggression caused fear, or that both depend on the same neural mechanism. Shared environments, inherited predispositions, and reporting patterns remain possible contributors to the association.
''','A relative risk compares the frequency of a trait between groups; it is not a direct measurement of a synaptic interaction.')
add('Age and sex associations do not identify mechanisms','P',['p3'],'''
Salonen and colleagues compared reported anxiety-related traits across ages and sexes. Noise sensitivity, particularly fear of thunder, increased with age in their survey, while female dogs were more often classified as fearful and male dogs more often classified as aggressive.

The dogs ranged from young puppies to older adults, extending the observations across much of the canine lifespan. The questionnaire distinguished fear of other dogs, strangers, and novel situations from aggression toward people and other behavioral categories.

These associations describe variation rather than an experimental effect of aging or sex hormones. Cohort differences, prior experiences, health, and owner interpretation were not eliminated by assigning dogs randomly to these characteristics. The survey provides behavioral context, but receptor-level explanations require a different experimental design.
''','An age association within a survey is distinct from repeatedly following the same animal as its behavior changes over time.')

add('Cat defensive rage recruits coordinated responses','N',['n1','s6a'],'''
**Defensive rage** is the historical name for a coordinated feline defensive response elicited experimentally, including hissing, ear retraction, piloerection, back arching, and strikes with the paws. **Piloerection** means raising the hairs rather than a separate act of attack.

Lu and colleagues elicited the response from the medial hypothalamus and the dorsal **periaqueductal gray**, or PAG, the midbrain gray matter surrounding the cerebral aqueduct. They measured the time from stimulation onset to hissing, with stimulation limited to 15 s.

Electrical stimulation tests whether activity at a site can recruit a behavioral pattern. It does not reproduce recognition of a particular natural threat or measure subjective fear. The elicited response includes vocal, postural, and autonomic components rather than a single isolated movement.
''','The hypothalamus lies in the forebrain, whereas the PAG lies in the midbrain; their interaction links distributed structures rather than one compact fear center.')
add('Two-site stimulation tests descending facilitation','N',['n2','n1'],'''
Lu and colleagues stimulated a PAG site that elicited hissing and paired it with medial hypothalamic stimulation below the level required to elicit behavior by itself. **Facilitation** means that the combined input made the PAG-elicited response occur sooner.

At matched PAG stimulation parameters, concurrent hypothalamic stimulation shortened hissing latency. Before the highest kynurenic-acid dose, the dual-stimulation response was about 37% faster than the PAG-only response. Alternating single and dual trials provided a comparison within the same preparation.

This procedure establishes a functional interaction between the selected sites. Electrical current can excite several elements, including passing fibers, so the result alone does not identify a monosynaptic connection or the transmitter responsible for facilitation.
''','A subthreshold input need not produce visible behavior alone to alter the response to activity elsewhere in the circuit.')
add('PAG amino-acid blockade removes facilitation','N',['n2','n1'],'''
**Excitatory amino acids** are amino-acid neurotransmitters capable of increasing neuronal excitation. Lu and colleagues injected kynurenic acid, an antagonist blocking several excitatory amino-acid receptor classes, into the PAG site used for eliciting defensive rage.

A 2.0 nmol injection reversed medial hypothalamic facilitation. At 15 min, dual-stimulation hissing latency rose above the PAG-only reference instead of remaining shorter. Lower doses produced smaller or shorter-lasting effects, and the response recovered over time.

The drug was delivered locally while electrical stimulation parameters remained unchanged. This supports excitatory amino-acid receptor participation at the PAG target region. Because kynurenic acid is not selective for one receptor class, this experiment cannot by itself assign the effect specifically to NMDA receptors.
''','An antagonist interferes with receptor activation; local delivery narrows the tested site but does not restrict the intervention to a genetically defined cell population.')
add('Selective NMDA blockade reverses hypothalamic gain','N',['n3','n1'],'''
**NMDA receptors** are excitatory amino-acid receptors named for the agonist N-methyl-D-aspartate. An **agonist** activates a receptor, whereas an antagonist reduces its activation. Lu and colleagues tested the selective NMDA antagonist AP7 inside the PAG.

A 2 nmol AP7 injection changed dual-stimulation latency from about 17% below the PAG-only reference to about 42% above it during the early post-injection period. The effect weakened with recovery; 0.1 nmol AP7 did not produce a comparable blockade.

The combination of receptor selectivity, dose dependence, and recovery supports NMDA participation in hypothalamic facilitation. Hissing latency is the measured output. The study did not record membrane current or identify which PAG neurons express the behaviorally relevant receptors.
''','NMDA receptors link transmitter binding to excitatory ion-channel signaling; the behavioral intervention tests receptor participation rather than the detailed current through the channel.')
add('Local NMDA activation makes hissing occur sooner','N',['n4','s6a'],'''
Lu and colleagues directly injected NMDA into PAG defensive sites without concurrent stimulation of the hypothalamus. This tested whether local receptor activation could reproduce the facilitation associated with the upstream input while the PAG stimulation procedure remained in place.

A 1.0 nmol NMDA injection shortened hissing latency by about 48% during the first 5–15 min. A 0.5 nmol dose produced a smaller, approximately 27% reduction. Latencies returned toward baseline within the subsequent observation periods.

Local activation therefore supplied a facilitatory influence on an electrically elicited response. It did not establish that NMDA alone generates a complete natural defensive episode. The transient dose-dependent result supports modulation of PAG excitability rather than permanent alteration of the circuit.
''','The colored anatomical tissue is the published PAG section from Bhatt and colleagues; it locates the region rather than measuring the NMDA experiment’s neuronal activity.')
add('Receptor controls narrow the excitatory explanation','N',['n3','n1'],'''
Lu and colleagues compared NMDA blockade with other receptor interventions at the same PAG sites. CNQX, which blocks non-NMDA excitatory amino-acid receptors, produced only small changes at 4 nmol. Atropine, a muscarinic acetylcholine receptor antagonist, had little effect at 4.4 nmol.

These local injections were compared with the larger reversal produced by AP7. The contrast narrows the explanation for medial hypothalamic facilitation toward NMDA receptor participation rather than indiscriminate disruption by fluid delivery or any receptor antagonist.

A negative result is limited to the dose, site, and response tested. It does not exclude non-NMDA or muscarinic signaling elsewhere in the brain, during sensory recognition, or under natural threat conditions. The intervention addresses one experimentally activated circuit link.
''','Receptor-class controls address pharmacological specificity, but they do not establish that every possible alternative transmitter has been excluded.')
add('Tracing identifies hypothalamic neurons reaching the PAG','N',['n5','n6def'],'''
**Retrograde tracing** labels neurons by transporting a marker from their axonal terminal region back to their cell bodies. Lu and colleagues injected Fluoro-Gold into behaviorally identified PAG sites and examined hypothalamic labeling after 5–6 days.

Labeled neurons extended through the medial hypothalamus, with concentrations in dorsomedial and perifornical regions. Immunocytochemistry, the use of antibodies to detect tissue components, identified aspartate- or glutamate-positive cells, including cells also carrying the retrograde marker.

Double labeling supports an anatomical projection containing excitatory amino-acid-associated neurons. It does not directly measure transmitter release during hissing or verify that every labeled cell participates in defense. Projection anatomy and the receptor-blockade results supply different kinds of evidence for the same proposed pathway.
''','Perifornical means near the fornix; labeling location specifies where candidate projecting neurons occur without claiming a uniform function for every cell in that region.')
add('Amino-acid labeling supports a candidate synaptic link','N',['n6ab','s6a'],'''
The Lu study detected aspartate-positive fibers and preterminal profiles in the dorsal PAG. **Preterminal** refers to an axonal segment approaching a terminal region. Aspartate-positive cells and retrogradely labeled cells also occurred in the medial hypothalamus.

A neuron could carry both Fluoro-Gold from the PAG projection target and amino-acid immunoreactivity. The published tissue panels preserve 100 μm and 25 μm scale bars, distinguishing regional localization from individual cellular labeling.

These observations are compatible with an excitatory descending connection acting through PAG NMDA receptors. Amino-acid immunoreactivity alone does not prove synaptic release, and the study did not record identified synapses. The stronger interpretation depends on agreement between anatomical labeling and local pharmacological manipulation of hissing latency.
''','A scale bar indicates the physical extent represented in tissue; antibody labeling detects molecular presence rather than electrical signaling during behavior.')

add('Lateral hypothalamic input can inhibit defense','G',['g2','g1'],'''
Cheu and Siegel paired stimulation of a medial hypothalamic defensive site with stimulation of the lateral hypothalamus. **Inhibition** here means a reduction in expression of the elicited defensive response, operationalized as a longer latency to hissing.

With medial stimulation alone, mean latency was 7.21 s; during dual medial and lateral stimulation it was 12.28 s. These differences persisted during the saline-control observation period, rather than appearing only after a drug injection.

The result contrasts with the facilitatory medial-hypothalamic–PAG relationship. A region can influence defense by suppressing another site’s output, not only by driving a response directly. Electrical interaction establishes functional suppression but does not, by itself, identify the inhibitory transmitter or the contributing cells.
''','Medial and lateral describe positions relative to the brain’s midline; they distinguish the stimulated territories rather than two names for the same site.')
add('GABA blockade weakens lateral suppression','G',['g3','g9'],'''
**GABA**, gamma-aminobutyric acid, is an inhibitory neurotransmitter. Cheu and Siegel injected bicuculline, a GABA-A receptor antagonist, into the medial hypothalamic site while testing lateral hypothalamic suppression of defensive rage.

At 60 pmol, bicuculline reduced the suppressive effect from about 73% before injection to about 15% in the early observation period. The suppression returned toward baseline by 180–200 min. A 10 pmol dose and saline did not produce the same blockade.

This local, reversible effect supports a GABA-A-dependent component of the inhibitory influence reaching the medial hypothalamus. It does not establish the pattern of GABA release during spontaneous fear. The study measured behavior after circuit stimulation rather than identified-cell firing in a natural encounter.
''','GABA-A receptors are ion-channel receptors whose activation generally reduces neuronal excitation; the experiment tests their behavioral contribution without recording chloride currents.')
add('Muscimol increases the threshold for defensive output','G',['g5','g9'],'''
Cheu and Siegel activated medial hypothalamic GABA-A receptors with **muscimol**, a receptor agonist, instead of stimulating the lateral inhibitory site. The question was whether local receptor activation could suppress defensive output from the target region.

A 30 pmol muscimol injection increased the stimulation-current threshold by about 155 μA early after delivery. **Threshold** means the electrical current required to elicit the response. Lower doses lacked the same pronounced effect, and the increase weakened over time.

The threshold measurement differs from hissing latency at a fixed current. A stronger input was required to recruit behavior after local inhibition. This supports receptor-dependent suppression, but it does not establish a clinical treatment for fearful cats or determine how natural threat recognition recruits the circuit.
''','The source plot reports a change in current threshold in microamperes; a higher threshold means the same stimulation becomes less effective at eliciting the defensive response.')
add('An antagonist reverses the agonist’s suppressive effect','G',['g6','g9'],'''
Cheu and Siegel pretreated the medial hypothalamic site with bicuculline before injecting muscimol. **Pretreatment** means applying one intervention before another to test whether the second effect depends on the blocked receptor class.

A 60 pmol bicuculline pretreatment opposed suppression caused by 30 pmol muscimol. The early stimulation-threshold increase was reduced by about 143 μA relative to the muscimol-plus-saline condition. A lower bicuculline dose produced a smaller reversal.

The agonist–antagonist comparison supports GABA-A receptor participation more specifically than an agonist effect alone. It reduces the likelihood that the response reflects only injected volume or an unrelated muscimol action. It does not determine which individual cells were inhibited within the injection territory.
''','The two drugs act in opposing directions at the same receptor class; their interaction provides a receptor-level control on the behavioral interpretation.')
add('GABA receptor classes produce different outcomes','G',['g7','g9'],'''
GABA-A and **GABA-B** are different receptor classes. GABA-A receptors directly gate ion-channel signaling, whereas GABA-B receptors act through intracellular signaling proteins. Cheu and Siegel compared a GABA-B agonist with the GABA-A agonist used in their medial hypothalamic experiments.

Baclofen at 120 pmol did not alter the latency or current threshold for defensive rage from the tested site. This dose was four times the highest muscimol dose used in the study, which had increased the response threshold.

The contrast supports receptor-class selectivity under these experimental conditions. Equal amounts of different drugs do not imply equal receptor occupancy, so the finding does not prove that GABA-B receptors are absent or irrelevant throughout feline defensive circuitry.
''','The preparation measures a behavioral consequence of receptor activation, not the number of receptors present or their affinity for the two drugs.')
add('The suppressive drug effect depends on injection site','G',['g8','g9'],'''
Local injection narrows a pharmacological intervention to a region, but diffusion can complicate localization. Cheu and Siegel tested whether muscimol’s suppressive effect extended from the medial hypothalamus into adjoining lateral hypothalamic tissue.

A 60 pmol muscimol injection into the lateral hypothalamus did not change the latency or threshold for defense elicited from the medial site. This dose was twice the medial dose producing pronounced suppression. Tracer injections were also checked for their anatomical extent.

The neighboring-site comparison supports regional specificity of the suppressive effect. It does not prove that all drug remained within one microscopic nucleus or that the lateral hypothalamus lacks a role in defense. Its electrical stimulation had already supplied a distinct inhibitory influence on the medial response.
''','An injection-site control tests whether a drug has the same consequence nearby; it does not equate pharmacological silencing with electrical stimulation of a region.')
add('Lateral GABA-positive neurons project medially','G',['g11','g9'],'''
Cheu and Siegel injected Fluoro-Gold into the medial hypothalamic defensive territory and then examined retrograde labeling in the lateral hypothalamus. They combined tracing with antibody detection of GABA to identify candidate inhibitory projection neurons.

Some lateral neurons contained both the tracer and GABA immunoreactivity. The injection focus was approximately 0.5–0.7 mm in diameter and did not visibly extend into the lateral hypothalamus. This localization reduced the possibility that lateral labeling simply reflected contamination by the injection itself.

The anatomical result supports a lateral-to-medial GABA-associated projection. Double labeling does not measure release at a functioning synapse. Together with bicuculline blockade and muscimol suppression, it supports a candidate inhibitory pathway while leaving its activity during naturally occurring threats unresolved.
''','The paired tissue views compare labeling in the same cellular territory; projection labeling and transmitter immunoreactivity answer different questions about the candidate neurons.')
add('Baseline defense need not depend on tonic inhibition','G',['g4','g9'],'''
**Tonic inhibition** is continuously maintained inhibitory influence, while episodic inhibition appears when a particular input is engaged. Cheu and Siegel tested bicuculline during medial hypothalamic stimulation alone, without concurrent lateral hypothalamic stimulation.

A 60 pmol injection left baseline hissing latency essentially unchanged: about 6.62 s before injection and 6.65 s in the early post-injection period. The same intervention blocked suppression when the lateral input was activated during dual stimulation.

The contrast is consistent with an inhibitory influence recruited by the lateral stimulation rather than strong continuous inhibition in this preparation. It does not exclude spontaneous GABA signaling or establish its temporal pattern in behaving animals outside the stimulation experiment. The conclusion concerns the tested conditions and the measured response.
''','Failure to change baseline behavior differs from failure to block an experimentally recruited input; the same receptor can matter strongly only under the second condition.')

add('A cytokine can increase defensive circuit responsiveness','S',['s3','s6'],'''
A **cytokine** is a signaling protein involved in immune and cellular communication. Bhatt and colleagues injected interleukin-1β, or IL-1β, into PAG sites while eliciting defensive hissing through the experimentally identified hypothalamic–PAG circuit.

A 5 ng injection produced maximal facilitation at about 60 min, corresponding to roughly a 42% reduction in hissing latency. The effect declined over subsequent observations but remained detectable at 180 min. Saline and the lowest tested dose lacked comparable facilitation.

The result establishes that local cytokine delivery can modulate a defensive response. It does not establish that infection invariably increases aggression or that the administered amount equals endogenous release during natural fear. The intervention tests one molecule at one identified circuit site.
''','The direction and duration of the behavioral change are measured directly; the endogenous source and release pattern of the cytokine remain separate questions.')
add('IL-1 receptor blockade prevents cytokine facilitation','S',['s4a','s6'],'''
Bhatt and colleagues pretreated a PAG defensive site with an antibody against the type-I IL-1 receptor before injecting IL-1β. A **receptor antibody** can interfere with the interaction between a signaling molecule and its receptor.

Pretreatment 5 min before cytokine delivery blocked the facilitatory reduction in hissing latency. The receptor antibody alone did not appreciably change the baseline response. Thus, preventing the cytokine effect did not require eliminating electrically elicited hissing altogether.

The comparison supports involvement of the targeted IL-1 receptor in the administered cytokine’s action. It does not identify whether the behavioral effect arises directly in the recorded defensive neurons, indirectly through neighboring cells, or through a specific intracellular cascade. No identified-neuron recording was performed in this experiment.
''','Receptor dependence concerns the cytokine-evoked modulation; the baseline defensive response and the additional facilitation are distinct outcomes.')
add('An isotype control tests nonspecific antibody effects','S',['s4b','s6'],'''
An **isotype control** is an antibody of a comparable class that does not target the experimental receptor. Bhatt and colleagues used IgG2a to test whether antibody delivery alone nonspecifically prevented IL-1β from facilitating defensive rage.

The control antibody did not block facilitation after 5 ng IL-1β, and it did not appreciably alter baseline hissing when administered alone. The same 30–180 min observation windows were used to follow the cytokine effect across the treatment conditions.

This result strengthens the receptor-specific interpretation of the blocking antibody experiment. It does not establish absolute specificity for every molecular interaction, nor does it replace a direct measurement of receptor signaling. A comparison between targeting and control antibodies addresses a different confound from comparing cytokine with saline.
''','A molecule can have effects because it is an antibody preparation or because it binds a particular target; the control distinguishes these possibilities experimentally.')
add('Serotonin receptor blockade prevents IL-1 facilitation','S',['s5a','s6'],'''
**Serotonin**, also called 5-HT, is a neuromodulator with multiple receptor classes. Bhatt and colleagues pretreated the PAG site with LY53857, a 5-HT2 receptor antagonist, before administering IL-1β during defensive-hissing experiments.

The antagonist prevented the latency reduction normally produced by 5 ng IL-1β. Antagonist delivery alone did not appreciably alter baseline hissing. The comparison supports serotonin-receptor participation in the cytokine-dependent increase in circuit responsiveness.

The tissue study labeled 5-HT2C receptors, but the behavioral pharmacology does not isolate every receptor subtype or the precise cellular interaction. A **neuromodulator** changes how a circuit responds to other inputs; the experiment supports such an interaction without directly measuring serotonin release, intracellular signaling, or the activity of identified PAG neurons.
''','The authors’ receptor staining and antagonist experiment are complementary; receptor presence alone would not establish its contribution to the behavioral modulation.')
add('Other facilitatory receptor blockers do not match 5-HT2','S',['s5bc','s6a'],'''
Bhatt and colleagues compared 5-HT2 blockade with blockade of NK-1 and CCKb receptors at the PAG site. **NK-1** is a receptor for substance P, and **CCKb** is a cholecystokinin receptor; both were candidate modulatory receptor classes in this preparation.

GR82334 and CR2945 did not prevent the facilitation caused by 5 ng IL-1β during the tested observation period. These compounds also lacked an appreciable effect on baseline hissing when administered alone, unlike the selective loss of cytokine facilitation after 5-HT2 blockade.

The comparison narrows the candidate receptor interaction rather than proving that the other signaling systems never influence defense. Their contribution could depend on other inputs or conditions. The result concerns IL-1β-mediated facilitation at the tested PAG sites and doses.
''','A receptor may be capable of influencing the behavior yet unnecessary for the effect of one specific modulator; these are different causal claims.')
add('Receptor staining localizes candidates within the PAG','S',['s6'],'''
Bhatt and colleagues used **immunocytochemistry**, antibody-based molecular labeling, to examine IL-1 and serotonin receptors in PAG tissue. IL-1 receptor labeling was stronger in dorsal PAG than in ventral PAG, while 5-HT2C labeling was distributed through the examined PAG region.

The published fluorescence panels preserve the original green and red labels and a 100 μm scale bar. Western blotting, which separates proteins before antibody detection, identified bands near 88 kDa for IL-1R1 and 47 kDa for 5-HT2C.

Anatomical presence is compatible with the pharmacological effects on hissing latency. It does not establish that the two receptors occur on the same behaviorally active cell or that one directly controls the other. Colocalization and functional coupling require additional cell-specific evidence.
''','A kilodalton is a unit of molecular mass; the blot supports antibody recognition of proteins near expected masses without measuring signaling during a defensive episode.')

add('Peripheral immune challenge can suppress hissing','I',['i2','i1'],'''
**Lipopolysaccharide**, or LPS, is a bacterial cell-wall component used experimentally to provoke an immune response. Bhatt and colleagues administered peripheral LPS at 50 μg/kg and measured PAG-elicited defensive hissing over subsequent hours.

Hissing latency increased beginning about 60 min after injection. Body temperature rose more strongly later, reaching about 105 °F at 120 min. Local medial hypothalamic delivery of 5 ng LPS did not reproduce the peripheral effect.

The contrast supports an indirect influence of peripheral immune activation rather than the same effect of local LPS delivery at the tested site. The timing weakens a simple explanation based only on peak fever, but it does not establish an absence of all sickness-related changes or subjective discomfort.
''','The source reports temperature in degrees Fahrenheit; the temporal comparison concerns when defensive suppression and the largest temperature increase appeared.')
add('Peripheral TNF neutralization blocks LPS effects','I',['i3','s6a'],'''
**Tumor necrosis factor**, or TNF, is a cytokine involved in immune signaling. Bhatt and colleagues tested whether peripheral cytokine neutralization could prevent the change in PAG-elicited defensive hissing following LPS challenge.

An anti-TNF antibody given 5 min before LPS blocked both the increase in hissing latency and the temperature rise. In contrast, the tested anti-IL-1 intervention did not prevent either effect. Antibody-alone conditions provided baseline comparisons over the same observation schedule.

The result supports a peripheral TNF-dependent component of the LPS effect. It does not establish the entire route by which peripheral signaling reaches the brain or identify all participating cells. Cytokine actions differ with administration site and biological context; local PAG IL-1β facilitation is not equivalent to systemic immune challenge.
''','Neutralizing a peripheral mediator and blocking a central receptor intervene at different points; the behavioral effects should not be assigned to one undifferentiated immune pathway.')
add('Prostaglandin blockade opposes immune suppression','I',['i4b','i1'],'''
**Prostaglandin E2**, or PGE2, is a lipid signaling molecule associated with inflammatory responses. Bhatt and colleagues injected the antagonist SC19220 into medial hypothalamic defensive sites before administering peripheral LPS.

The pretreatment opposed the LPS-induced increase in hissing latency for about 180 min, with weakening blockade later. Local anti-TNF treatment did not produce the same protection, despite the effectiveness of peripheral TNF neutralization in a separate experiment.

These interventions support different peripheral and central steps in immune-dependent defensive modulation. The article uses inconsistent prostaglandin-receptor subtype terminology, so the subtype assignment remains uncertain. The data support involvement of prostaglandin-sensitive signaling under the tested conditions, without resolving a complete molecular pathway from immune activation to neuronal inhibition.
''','The source’s methods, results, and discussion do not consistently name the same EP subtype; assigning one subtype as an established mechanism would exceed the evidence.')
add('Hypothalamic 5-HT1A blockade opposes the LPS effect','I',['i4c_full','i1'],'''
**5-HT1A** is a serotonin receptor class distinct from the 5-HT2 receptors implicated in local PAG cytokine facilitation. Bhatt and colleagues injected the 5-HT1A antagonist p-MPPI into medial hypothalamic defensive sites before peripheral LPS challenge.

A 12 nmol injection in 0.5 μl prevented the prolonged increase in hissing latency produced by LPS. Antagonist-alone treatment did not appreciably alter the baseline response. This contrasts with 5-HT2-dependent facilitation after direct IL-1β administration in the PAG.

The findings support context-dependent serotonin modulation at different sites and receptor classes. They do not establish that serotonin uniformly promotes or uniformly suppresses fear. The LPS experiment measured an evoked defensive response without recording receptor-bearing neurons or the serotonin concentration reaching them.
''','Site, receptor class, and biological state all differ between the two experiments; the opposite behavioral directions do not contradict each other.')
add('Preserved head turning limits motor explanations','I',['i5','s6a'],'''
Bhatt and colleagues compared LPS effects on defensive hissing with effects on head turning elicited by midbrain stimulation. **Motor control** here means a comparison response used to test whether the animal simply lost the capacity to move or respond to stimulation.

Across the 300 min observation period, LPS prolonged defensive-response latency but did not appreciably change head-turning latency. The tested motor response therefore remained available while defensive output was suppressed under the same immune challenge.

This comparison weakens a nonspecific paralysis or broad motor-failure explanation. It does not exclude changes in motivation, other movements, sensory processing, or sickness state. A preserved comparison behavior narrows interpretation of the affected response without proving that the manipulation acts exclusively on a single defensive circuit.
''','One spared motor behavior cannot establish that every other behavior is unaffected; it supplies a specific control against a general loss of movement.')

add('Access to concealment accelerates behavioral recovery','H',['h1'],'''
**Concealment** allows an animal to remain visually sheltered from its surroundings. Van der Leij and colleagues randomly assigned shelter cats to quarantine cages with or without cardboard hiding boxes measuring 44 × 31 × 26 cm.

Cats with boxes reached a relatively stable behavioral stress score by Day 2, compared with Day 9 in the control group. Both groups experienced the shelter quarantine environment and comparable daily care, allowing the available hiding space to be tested as an environmental intervention.

The result supports faster recovery of observable stress-related behavior when concealment is available. It does not identify the neural mechanism or establish that the cats experienced no fear. Environmental changes can alter defensive expression without requiring pharmacological manipulation of a receptor.
''','Random assignment tests the effect of providing a box; it is stronger causal evidence for that environmental intervention than an association between hiding and stress alone.')
add('Behavioral stress scores change over several days','H',['h1'],'''
The shelter study used the **Cat-Stress-Score**, a standardized assessment of posture and behavior. Cats were video-recorded for 20 min on observation days, with repeated samples contributing to each daily score during the 12-day quarantine period.

The hiding-box group had lower stress scores after the first observation day and reached stability sooner. Scoring retained each animal’s trajectory, rather than assuming identical recovery for every cat. Individual differences persisted within both housing conditions.

A behavioral score operationalizes visible responses; it is not a direct assay of a stress hormone or neuronal activity. Concealment also changes observation conditions, and some features can become harder to see. The reported benefit therefore concerns the measured behavioral adaptation under the study’s housing and scoring procedures.
''','Repeated observations distinguish a change through time from a single calm-looking moment; the scoring procedure still depends on which behaviors remain observable.')
add('Calmer behavior does not guarantee physical recovery','H',['h2'],'''
Van der Leij and colleagues measured body weight at intake and during quarantine as an outcome separate from the behavioral stress score. A hiding box accelerated behavioral recovery, but it did not reliably prevent weight loss over the 12-day study.

Control cats lost about 7.7% of initial body weight, while cats with boxes lost about 6.3%. The difference between housing groups was not reliably established. Food was provided under a standardized regime, but individual daily food intake was not monitored.

The divergence limits an inference that calmer behavior means every aspect of welfare has recovered. Body weight can reflect feeding and health as well as stress. Neither weight change nor posture alone identifies a specific neural circuit or establishes the animal’s complete internal state.
''','Behavior and physical condition are distinct outcomes; an intervention can improve one while leaving another unresolved.')

assert len(slides)==44,len(slides)
# Explicit source verification notes are retained outside the student-facing text.
spec={'lecture':54,'theme':'ash-blue-paper','content_slides':44,'title_height':2.4,'title_image':figure('d1dog'),'title_refs':[refs['D']],'slides':slides,'takeaways':{'cite':'Somppi et al. (2016); Quaranta et al. (2020); Lu et al. (1992); Cheu & Siegel (1998); Bhatt et al. (2008, 2009); van der Leij et al. (2019)','refs':list(refs.values()),'items':[
{'lead':'Recognition differs from defensive expression.','text':'Gaze and audiovisual matching establish cue discrimination; stimulation and intervention test recruitment of behavioral output.'},
{'lead':'Social threat depends on context.','text':'Dogs sample threatening dog and human faces differently, and cats match hissing and human emotional signals across vision and hearing.'},
{'lead':'Excitatory input facilitates feline defense.','text':'Medial hypothalamic facilitation of PAG-elicited hissing depends on local NMDA receptor signaling in the tested preparation.'},
{'lead':'Inhibition is site and receptor dependent.','text':'Lateral hypothalamic suppression involves medial hypothalamic GABA-A receptors; activating these receptors raises the defensive-response threshold.'},
{'lead':'Immune state changes circuit responsiveness.','text':'Local PAG IL-1β can facilitate defense through serotonin-sensitive signaling, whereas peripheral LPS can suppress the evoked response.'},
{'lead':'Inference must match the measurement.','text':'Cat circuit experiments do not establish canine mechanisms. Concealment improves observed cat stress without guaranteeing recovery of body weight.'}
]}}
(root/'lecture.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n')
(root/'REFERENCES.md').write_text('# Lecture 54 verified primary references\n\n'+'\n\n'.join(refs.values())+'\n\nAll eight PDFs were read and checked against Crossref metadata. Figures are original PDF crops. The Bhatt 2009 paper has inconsistent EP-receptor subtype naming; the lecture explicitly retains that uncertainty.\n')
(root/'PLAN.md').write_text('# Lecture 54 slide claims\n\n'+'\n'.join(f'{i}. {x["title"]} — {x["cite"]}' for i,x in enumerate(slides,2))+'\n')
print('Wrote',len(slides),'content slides')
