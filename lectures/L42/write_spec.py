"""Author Lecture 42 from verified primary literature and original PDF crops."""
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parent
REF={
'B':('Berns et al. (2015)','10.1098/rspb.2015.1203','Berns GS, Cook PF, Foxley S, Jbabdi S, Miller KL, Marino L (2015). Diffusion tensor imaging of dolphin brains reveals direct auditory pathway to temporal lobe. Proceedings of the Royal Society B 282: 20151203.'),
'J':('Janik et al. (2006)','10.1073/pnas.0509918103','Janik VM, Sayigh LS, Wells RS (2006). Signature whistle shape conveys identity information to bottlenose dolphins. Proceedings of the National Academy of Sciences USA 103: 8293–8297.'),
'K':('King & Janik (2013)','10.1073/pnas.1304459110','King SL, Janik VM (2013). Bottlenose dolphins can use learned vocal labels to address each other. Proceedings of the National Academy of Sciences USA 110: 13216–13221.'),
'M':('Bruck (2013)','10.1098/rspb.2013.1726','Bruck JN (2013). Decades-long social memory in bottlenose dolphins. Proceedings of the Royal Society B 280: 20131726.'),
'C':('King et al. (2013)','10.1098/rspb.2013.0053','King SL, Sayigh LS, Wells RS, Fellner W, Janik VM (2013). Vocal copying of individually distinctive signature whistles in bottlenose dolphins. Proceedings of the Royal Society B 280: 20130053.'),
'R':('Richards et al. (1984)','10.1037/0735-7036.98.1.10','Richards DG, Wolz JP, Herman LM (1984). Vocal mimicry of computer-generated sounds and vocal labeling of objects by a bottlenosed dolphin, Tursiops truncatus. Journal of Comparative Psychology 98: 10–28.'),
'S':('Sayigh et al. (2023)','10.1073/pnas.2300262120','Sayigh LS, El Haddad N, Tyack PL, Janik VM, Wells RS, Jensen FH (2023). Bottlenose dolphin mothers modify signature whistles in the presence of their own calves. Proceedings of the National Academy of Sciences USA 120: e2300262120.')
}
CAP={
'B1':('B','1','Probabilistic auditory tracts through inferior colliculus, thalamus and cortex.'),
'B2':('B','2','Cortical-region connectivity parcellates the common dolphin thalamus.'),
'B3':('B','3','Temporal cortex tracts connect with dorsal auditory cortex.'),
'B4':('B','4','Orbital cortical connectivity parcellates the basal ganglia.'),
'C1a':('C','1(a)','A calf copies its mother’s whistle contour; its own whistle differs.'),
'C1b':('C','1(b)','A mother copies her calf’s whistle contour; her own whistle differs.'),
'C1c':('C','1(c)','An adult male copies another male’s whistle contour.'),
'C2':('C','2','Association coefficients are higher among signature-whistle-copying pairs.'),
'C3':('C','3','Acoustic measurements separate copies from original and copier whistles.'),
'J1a':('J','1 (top pair)','Original and synthetic whistles preserve the same frequency contour.'),
'J1b':('J','1 (middle pair)','A kin whistle contour is reproduced without its original voice features.'),
'J1c':('J','1 (bottom pair)','An unrelated familiar whistle is synthesized for the control playback.'),
'J2':('J','2','Head turns toward the speaker differ between nonkin and kin playbacks.'),
'K1':('K','1','Matching replies resemble the playback contour more than controls do.'),
'K2':('K','2','Own-signature-copy playbacks elicit more matching replies than controls.'),
'K3':('K','3','Playback whistles and matching group replies appear in spectrograms.'),
'K4':('K','4','Individual whistle contours occur before and after copy playbacks.'),
'M1':('M','1','Familiar-whistle responses persist across separation-duration categories.'),
'M2':('M','2','Response scores differ across calf, juvenile and adult life stages.'),
'R1':('R','1','Baseline whistles differ between Akeakamai and Phoenix.'),
'R2':('R','2','The dolphin reproduces several trained frequency-modulation patterns.'),
'R3':('R','3','Successive attempts change toward a novel acoustic model.'),
'R4':('R','4','Repeated responses preserve learned acoustic patterns.'),
'R5':('R','5','Five visual objects elicit distinct learned whistle responses.'),
'S1a':('S','1(A)','Dolphins carry suction-cup hydrophones during health assessments.'),
'S1bc':('S','1(B–C)','One mother’s whistle extends to higher frequencies with her calf.'),
'S1d':('S','1(D)','Paired maternal recordings show higher maximum frequencies with calves.'),
'S2':('S','2','Calf presence changes frequency measures without shortening whistle loops.')
}
def fig(name):
 k,n,desc=CAP[name];return {'path':f'figures/{name}.png','caption':f'{REF[k][0]}, Fig. {n}. {desc}','source_url':'https://doi.org/'+REF[k][1],'kind':'article'}
slides=[]
def add(title, keys, images, paragraphs, extra):
 body=paragraphs.strip().split('\n\n')
 assert len(body)==3,(title,len(body))
 assert len(title)<=62,title
 words=sum(len(x.split()) for x in body)
 assert 90<=words<=170,(title,words)
 fs=[fig(i) for i in images.split()]
 keys=keys.split()
 s={'layout':'figure-right' if len(fs)==1 else 'figures-right','title':title,'body':body,'cite':'; '.join(REF[k][0] for k in keys),'refs':[REF[k][2]+' https://doi.org/'+REF[k][1] for k in keys],'transcript':body+[extra]}
 if len(fs)==1:s['figure']=fs[0]
 else:s['figures']=fs
 slides.append(s)
add('Whistle patterns support social recognition','S M','S1a',"""
Bottlenose dolphins, _Tursiops truncatus_, maintain relationships while companions separate and reunite. A **signature whistle** is an individually distinctive, learned frequency pattern that can identify its customary producer. It provides a candidate acoustic cue when visual contact is limited.

Sayigh and colleagues recorded identified mothers with and without their calves using suction-cup underwater microphones. The same mother retained her recognizable whistle contour while changing its frequency range; maximum frequency increased by an average of 2.4 kHz with her calf.

Bruck tested playback responses to former companions after documented separation. Recognition persisted for as long as 20.5 years. Together, these studies link flexible vocal production to durable social information, without demonstrating a particular neural memory mechanism.
""","The photograph documents the recording preparation rather than an undisturbed social encounter. Later playback experiments distinguish acoustic recognition from simple resemblance or generalized arousal. Long separation intervals refer to documented former cohabitation, not an experimentally imposed deprivation period.")
add('A contour specifies how frequency changes through time','C','C1a',"""
A **frequency contour** tracks the dominant sound frequency through time, measured in kilohertz and seconds. Frequency modulation means that frequency changes within a call. A **spectrogram** displays time horizontally, frequency vertically, and acoustic energy through the published color scale.

King and colleagues recorded mother–calf pairs and compared the mother’s signature, the calf’s copy, and the calf’s own signature. The calf reproduced the mother’s characteristic modulation pattern rather than merely emitting its usual whistle during a social exchange.

The original spectrograms show similarities alongside consistent differences. Copying therefore concerns the organization of a learned pattern, rather than exact reproduction of every acoustic feature. The figure’s color represents the paper’s acoustic display, not measured neuronal activity.
""","Read the three rows as owner, copy, and copier’s own signature. Preserve the distinction between a frequency contour and the complete acoustic signal, which also contains amplitude and spectral detail. The article used individual recording channels to establish who produced each whistle.")
add('Identity can survive removal of original voice features','J','J1a',"""
A learned contour and a producer’s **voice features** are different potential identity cues. Voice features include acoustic properties arising from how a particular animal generates a sound. Janik and colleagues tested whether dolphins recognize a familiar individual when those original features are removed.

They synthesized tonal whistles from measured frequency contours and played them through an underwater speaker. The model retained changes in frequency over roughly second-long calls while replacing the original waveform and its fine spectral structure.

Dolphins distinguished synthetic contours of familiar relatives from familiar unrelated animals. This manipulation establishes that contour information can be sufficient for identity-sensitive behavior. It does not show that natural voice features are useless, or that every dolphin uses only a single cue.
""","The paired plots show original recordings on the left and synthetic playback signals on the right. Compare frequency trajectories rather than absolute waveform amplitude. Synthesizing a stimulus was part of the published experiment; the slide itself uses the original article figure without reconstructing it.")
add('Postmortem imaging maps candidate auditory routes','B','B1',"""
Berns and colleagues examined preserved brains from a common dolphin, _Delphinus delphis_, and a pantropical spotted dolphin, _Stenella attenuata_. These are comparative anatomical preparations, not brain recordings from bottlenose dolphins producing or recognizing signature whistles.

**Diffusion imaging** measures how water displacement depends on direction within tissue. The study used 1.3-mm isotropic diffusion measurements to estimate preferential directions through white matter, where bundles of neuronal axons carry signals between regions.

**Tractography** follows those directional estimates to propose anatomical routes. Pathways connected an auditory midbrain seed with thalamic and temporal regions. This evidence supports a candidate sensory infrastructure, but cannot identify which cells respond to a known individual or establish the direction of synaptic transmission.
""","An axon is a neuronal process that carries electrical signals to other cells. In fixed tissue, diffusion is a structural measurement: no neuron is firing during the scan. Species differences and preservation limit direct translation from these brains to bottlenose dolphin behavior.")
add('Preserved brains require specialized diffusion methods','B','B1',"""
The common dolphin brain had been stored in formalin, a chemical fixative that preserves tissue while changing its magnetic properties. Its fresh mass was 981 g. Berns and colleagues therefore used an imaging method designed for the weak diffusion signal of preserved material.

Diffusion-weighted steady-state free precession samples directional water motion while accounting for altered tissue relaxation. Anatomical images, acquired at 0.6 × 0.6 × 0.5 mm resolution, helped place the estimated pathways within recognizable structures.

Using structural landmarks alongside diffusion estimates reduces anatomical ambiguity, but fixation remains a limitation. Agreement across differently preserved specimens is more informative than a visually impressive tract image alone. Neither brain mass nor image resolution measures cognitive ability or the number of functional connections.
""","Magnetic relaxation describes how magnetization returns toward equilibrium after excitation. The fine structural scan and the coarser diffusion scan answer different questions. Preservation-dependent signal loss can change tract sensitivity, so absent streamlines cannot simply be equated with absent axons.")
add('The inferior colliculus links brainstem and forebrain','B','B1',"""
The **inferior colliculus** is an auditory midbrain structure receiving ascending input from brainstem pathways. Berns and colleagues placed tractography seeds in the left and right inferior colliculi and estimated routes extending toward both lower brainstem structures and the forebrain.

Descending portions of the structural reconstruction joined the lateral lemniscus, an auditory fiber bundle, near pathways associated with the superior olive and cochlear nuclei. Ascending portions reached the ventrocaudal thalamus and temporal cortex.

The figure displays only voxels crossed by at least 20% of the relevant estimated streamlines. That visualization threshold is not a percentage of auditory neurons. Because diffusion lacks axonal polarity, these tracks do not establish whether any particular connection carries ascending or descending signals.
""","The cochlear nuclei are early central auditory relays; the superior olive participates in brainstem auditory processing. Their anatomical association does not demonstrate a signature-whistle computation. The names ascending and descending refer to the known comparative pathway framework, not a direction measured by diffusion.")
add('Thalamic connectivity reaches temporal cortex','B','B2',"""
The **thalamus** is a forebrain collection of nuclei that relays and transforms information between subcortical structures and cortex. Berns and colleagues found that the inferior-colliculus route passed through a ventrocaudal thalamic region before reaching deep temporal cortex near the Sylvian fissure.

They compared connectivity to predefined cortical regions: a presumed visual region, a traditional dorsal auditory region, and a temporal region. Their color-coded thalamic map assigned voxels according to the strongest estimated connection to those targets.

Temporal connectivity occupied a different thalamic territory from much of the traditional dorsal auditory target. The inferred auditory relay was anatomically compatible with the medial geniculate nucleus, but tractography did not establish its cellular identity through histology or auditory response recordings.
""","A cortical region is a surface territory; a thalamic nucleus is a deeper neuronal grouping. Connectivity-based parcellation is a classification of estimated paths, not a measurement of neurotransmission. The paper’s target labels are hypotheses informed by comparative anatomy and earlier physiology.")
add('Temporal and dorsal auditory territories are connected','B','B3',"""
The **cortex** is the layered outer gray matter of the cerebral hemispheres. A **sulcus** is a cortical groove; a fissure is a particularly prominent groove. Berns and colleagues identified an auditory candidate near the Sylvian fissure within the temporal lobe.

Starting tractography from temporal regions also revealed pathways toward the suprasylvian territory, a dorsal region traditionally associated with dolphin auditory responses. The published image shows these routes across several anatomical views, with colors identifying the seed side.

Connectivity between the two territories makes a distributed auditory organization plausible. It does not prove that one area decodes whistle identity while the other controls vocal output. Such a division would require functional recordings or carefully designed causal interventions.
""","The anatomical views place the temporal target relative to the Sylvian fissure and neighboring sulci. Multiple views of one reconstruction improve spatial interpretation but do not constitute independent experimental replications. Avoid assigning language-like functions to a region solely because of its anatomical location.")
add('Orbital connectivity provides a comparative check','B','B4',"""
The **basal ganglia** are interconnected subcortical structures receiving cortical input and participating in action-related processing across mammals. Berns and colleagues used orbital cortical connectivity to test whether their dolphin reconstruction recovered a broadly recognizable organization outside the auditory pathway.

They divided the orbital surface into five cortical targets and classified connected basal-ganglia voxels. The resulting map followed a rostrocaudal gradient: more anterior cortical targets tended to connect with more ventral basal-ganglia territories.

This comparative pattern supports anatomical plausibility of the tractography method. The targets were defined operationally, however, and were not functionally mapped motor or executive areas. Recovering an expected gradient cannot validate every auditory streamline or localize the decision to copy another dolphin’s whistle.
""","Rostral means toward the front of the brain; caudal means toward the rear. The colors identify different orbital targets and associated territories. The comparison is a methodological plausibility check, not a behavioral experiment on action selection in dolphins.")
add('Replication supports the route but preserves uncertainty','B','B1',"""
Berns and colleagues repeated the auditory analysis in a pantropical spotted dolphin brain after studying the common dolphin. The second specimen supported the same broad route from inferior colliculus through ventrocaudal thalamus toward temporal cortex.

The two archival brains differed in preservation and imaging sensitivity. In the second specimen, pathways required a lower display threshold, making exact comparisons of visible tract extent inappropriate. Broad agreement is therefore stronger evidence than apparent differences in tract thickness.

The illustrated common-dolphin reconstruction shows the principal anatomical proposal. Across both specimens, streamlines remain estimates that can miss fibers or follow spurious routes. Replication increases confidence in the candidate pathway without establishing synapses, axon counts, or a dedicated social-recognition circuit.
""","The image is explicitly the common-dolphin result; it is not presented as the spotted-dolphin replication image. A lower threshold can reveal weak estimates but also increase false positives. Anatomical agreement should be interpreted at the scale actually supported by the measurements.")
add('Structure does not identify the recognition computation','B J','B3',"""
An anatomical auditory route and an identity-sensitive behavioral response answer different questions. Berns and colleagues traced candidate connections in preserved brains; Janik and colleagues manipulated whistle contours and measured living dolphins’ head turns toward an underwater speaker.

The structural images specify possible routes for information reaching cortex. The playback manipulation shows that familiar contours can influence behavior after original voice features are removed. Combining the findings motivates functional hypotheses, but does not directly link the observed response to a particular tract.

Neither study measured transmitter release, receptor activity, ion-channel currents, or single-neuron recognition responses. Assigning those mechanisms to dolphin identity processing would exceed the evidence. Electrical and synaptic implementation remains a distinct experimental question.
""","Do not substitute a mammalian textbook circuit for a demonstrated dolphin mechanism. The gap is specific: behavior identifies information used by the animal, whereas postmortem imaging identifies anatomical candidates. Neural recordings, molecular localization, or selective interventions would be needed to bridge those levels.")
add('Synthetic playback isolates the identity-bearing contour','J','J1b',"""
Janik and colleagues converted recorded signature whistles into synthetic tonal signals following the same frequency-modulation trajectory. The synthetic waveform replaced original voice features while retaining the characteristic contour over the call’s duration.

The crucial comparison used a familiar relative’s contour and a familiar unrelated dolphin’s contour. The unrelated comparison animal was matched in age and sex, reducing the possibility that broad demographic differences explained the response.

Dolphins turned toward the speaker more often for the relative’s synthetic contour. Because no original voice waveform was played, the response could not require that waveform. The experiment demonstrates usable identity information in a learned contour, while leaving the contribution of additional cues in natural communication open.
""","The kin-versus-nonkin comparison is meaningful because both were familiar individuals. It was not a familiar-versus-novel sound test. Matching age and sex controls some demographic variables, but cannot equalize every aspect of relationship history or motivation.")
add('Matched familiarity controls a simple novelty explanation','J','J1c',"""
An unfamiliar sound can attract attention simply because it is novel. Janik and colleagues avoided that explanation by selecting both playback contours from dolphins known to the recipient: a close relative and a familiar unrelated individual matched in age and sex.

The published synthetic examples preserve frequency trajectories in kilohertz over time in seconds. Original amplitude patterns and detailed voice spectra were not retained as identity cues in the experimental playback signals.

Different head-turn responses therefore depended on more than whether a sound had ever been encountered. Relationship-specific experience is consistent with the result, although familiarity matching does not make social histories identical. The experiment tests contour-based individual information rather than a general preference for all familiar sounds.
""","The bottom original–synthetic pair depicts the unrelated familiar control. Discuss what each control removes and what it leaves unresolved. Similar exposure categories do not imply equal emotional significance, frequency of contact, or current motivation to respond.")
add('Turning and calling measure different response channels','J','J2',"""
Janik and colleagues scored head turns toward and away from the underwater speaker and recorded vocal responses. A head turn toward a source is an orienting behavior, indicating that the stimulus has altered attention or approach-related engagement.

Recipients turned toward related individuals’ synthetic whistles more often than toward matched familiar nonkin whistles. Head turns away from the speaker and overall whistle rates did not show the same difference between stimulus classes.

The plotted counts therefore support an identity-sensitive orienting response, rather than a universal increase in all behavior. A dolphin can recognize a signal without producing more whistles. Conversely, a high whistle rate alone would not establish that the caller was identified.
""","The paired lines connect two conditions for the same recipient. They show individual variation as well as the overall tendency. Counts of head turns are not a direct measure of subjective certainty or the strength of a stored identity representation.")
add('Self-similarity does not explain the kin preference','J','J1a J1c',"""
One alternative explanation is that dolphins prefer contours resembling their own signature whistle, rather than recognize particular companions. Janik and colleagues compared spectrogram similarity between each recipient’s whistle and the two synthetic playback contours.

They found no consistent tendency for the relative’s contour to resemble the recipient’s own whistle more closely. Response preferences also did not follow whether a playback contour was more or less similar to the recipient’s signature.

The illustrated example makes the logic visible: the recipient’s contour resembles the unrelated stimulus more closely, yet its response favored the relative. This control weakens a simple acoustic-self-matching account. It does not establish the detailed neural representation of a familiar individual.
""","The two displayed original–synthetic pairs show the recipient and unrelated familiar individual. The full published figure also includes the kin stimulus. The behavioral preference is the result reported in the paper. Similarity analysis constrains a specific alternative rather than proving every feature of recognition.")
add('Recognition requires a link to prior experience','J','J2',"""
**Discrimination** is detecting a difference between stimuli; **recognition** links a current stimulus to something previously encountered. Janik and colleagues used familiar animals’ signature contours to ask whether contour discrimination had socially meaningful consequences.

Recipients oriented differently toward synthetic contours of relatives and unrelated familiar animals. Acoustic comparisons did not support a simple preference for kin-like contour features or resemblance to the recipient’s own whistle.

The authors therefore interpreted the response as individual recognition based on prior experience. That conclusion goes beyond mere detection of two different sounds, but it does not show a verbal name concept or a human-like autobiographical memory. The behavior reveals access to identity-related information under the tested conditions.
""","A recognition interpretation is strongest when responses depend on learned relationships and alternative acoustic biases are controlled. The term does not require a claim about conscious naming. The paper’s distinction between discrimination and recognition is conceptual, not a separate brain measurement.")
add('Recognition is expressed with individual variability','J','J2',"""
The head-turn data in Janik and colleagues’ study did not show identical behavior from every dolphin. Some recipients strongly favored related contours; others showed little preference or oriented more toward the unrelated familiar individual.

Both stimulus classes carried recognizable frequency patterns, and overall vocal rates did not distinguish them. Variation in the orienting response is therefore compatible with recognition being influenced by relationship history, motivation, or the immediate recording context.

A behavioral difference supports contour-based identity information at the tested level. Absence of a strong preference in one recipient cannot automatically be read as inability to recognize the whistle. Equally, motivational explanations remain hypotheses unless their predicted effects are tested independently.
""","Avoid turning a group-level result into a claim that every dolphin always responds to kin in the same way. Playback gives a controlled input, but the expressed output is shaped by more than perceptual ability. Individual response differences are visible in the original paired plot.")
add('Vocal learning can change the produced sound itself','R','R1',"""
**Vocal production learning** changes the acoustic form of a call through experience, rather than merely changing when an existing call is used. Richards and colleagues trained the female bottlenose dolphin Akeakamai to reproduce computer-generated tonal models.

Before training, baseline recordings documented a limited set of stereotyped whistle patterns. Her common whistle was centered near 9 kHz with rapid modulation around 10 Hz, visibly different from several later training models.

Comparison with baseline is essential: an apparent imitation could otherwise be selection of an already existing call. After training, new frequency patterns appeared that tracked model sounds. The result demonstrates learned acoustic modification in this individual, not a species-wide estimate of spontaneous imitation frequency.
""","The original baseline figure also includes Phoenix, the other dolphin housed with Akeakamai. The relevant comparison is Akeakamai’s own pretraining repertoire versus her later responses. Frequency in kilohertz describes pitch-related acoustic structure; modulation rate in hertz describes how often that structure cycles.")
add('Reinforcement shaped matching to an acoustic model','R','R2',"""
Richards and colleagues presented computer-generated model sounds and reinforced whistle responses judged to resemble them. **Reinforcement** is a consequence that increases the probability of a behavior; here, successful matching was followed by a conditioned signal and food reward.

The models varied tonal frequency through time, including slow modulation at 1–2 Hz and faster modulation at 3–11 Hz. Published spectrograms compare model patterns with the dolphin’s subsequent whistles, rather than comparing only whether she vocalized.

Repeated training produced accurate reproduction of several distinct modulation forms. The procedure establishes controllable production learning under intensive training conditions. It does not show that each pattern would emerge without reinforcement or that the same learning process explains every natural signature whistle.
""","Distinguish an acoustic frequency, such as 9 kHz, from a modulation rate, such as 10 Hz. The paired examples test pattern structure rather than a nonspecific increase in calling. Reward contingencies are part of the preparation and should not be omitted when interpreting the result.")
add('Novel models reveal transfer beyond trained exemplars','R','R3',"""
A learned response may be tied to a specific training stimulus or may generalize to a new one. Richards and colleagues tested unfamiliar acoustic models after Akeakamai had acquired matching responses to several previously trained patterns.

The published sequence shows successive attempts at reproducing a novel model. Responses changed toward the target across the sequence; other novel sounds could be reproduced promptly. Model durations were approximately 0.5–1.5 s during the training procedure.

Transfer to new models supports a generalized auditory-to-vocal matching ability, rather than memorization of only a fixed set of rewarded whistles. It does not mean every new sound was copied perfectly on the first attempt. The figure specifically illustrates progressive adjustment during learning.
""","The first trace is the model and subsequent traces are dolphin responses. Preserve the distinction between immediate transfer in some tests and progressive improvement in this example. The result concerns learned vocal imitation, not imitation of arbitrary human speech or every possible acoustic signal.")
add('Trained and natural copies share flexible modulation','R C','R2 C1c',"""
Richards and colleagues trained Akeakamai to reproduce tonal patterns with smooth modulation, rapid transitions, and nearly constant frequencies. Some responses also tracked amplitude variations that had not been explicitly reinforced, indicating transfer beyond the specific rewarded feature.

King and colleagues later recorded untrained social copying between dolphins. Their original colored spectrograms compare an adult male’s signature, another male’s copies, and the copier’s own signature over time in seconds and frequency in kilohertz.

The two studies connect production flexibility with a natural social behavior, while using different preparations. Trained model imitation demonstrates acoustic capacity; naturally recorded copying shows its social expression. Neither finding alone explains how juvenile dolphins construct their own signature whistles during development.
""","The two source figures are intentionally separate: the grayscale panel is the trained imitation experiment, and the colored panel is natural social copying. Do not treat natural signature copies as responses to the computer models. Similar behavioral capacity does not prove identical learning histories.")
add('Repeated matching is more than an isolated resemblance','R','R4',"""
A single similar-looking whistle could occur by chance. Richards and colleagues repeatedly presented familiar model sounds and compared sequences of Akeakamai’s responses, testing whether distinct acoustic patterns could be reproduced reliably.

The original figure includes a moderately modulated sound, a constant-frequency sound, a widely swept pattern, and a square-wave-like transition pattern. Successive whistles retain the relevant organization rather than reverting to one common baseline form.

Repeated production supports stable learned control of acoustic structure over multiple trials. The result concerns reproducibility within this trained individual, not unrestricted imitation accuracy across all dolphins. Performance also varied by model: stable transfer to some patterns should not be treated as evidence that all acoustic transformations were equally easy.
""","Read each row as repeated responses to one model class. The comparison controls the possibility that the dolphin produced the same favored whistle regardless of the sound presented. The experiment remains a heavily trained single-animal preparation, which is strong for capability but limited for population prevalence.")
add('Visual objects can acquire distinct vocal responses','R C','R5 C1a',"""
Richards and colleagues transferred control of learned whistles from an acoustic model to a visible object. **Stimulus control** means that a particular cue reliably selects a response. The dolphin eventually produced different trained sounds for a ball, pipe, hoop, person, and frisbee.

Objects were displayed in air so their presentation did not supply the original underwater model sound. The original figure shows the resulting whistle patterns; the separate colored figure shows natural mother–calf copying for comparison.

Object-controlled production demonstrates an acquired association between a visual cue and a vocal output. Natural copying establishes a different social use of learned contours. Together they show flexibility, but they do not establish that wild dolphins routinely attach arbitrary whistle labels to nonsocial objects.
""","The original object-label figure includes model sounds alongside examples of the responses elicited by objects alone. Separate artificial visual-cue training from the natural copying evidence. The word label describes the learned cue–response association without assuming human semantic structure.")
add('Blind scoring verifies learned object–sound associations','R C','R5 C1b',"""
Richards and colleagues tested object labeling with an observer who could hear and inspect the dolphin’s response but could not see the object or the tankside presentation. Objects appeared in balanced random order without playback of their associated acoustic models.

Akeakamai gave the correct learned whistle on 91% of the tested presentations. Most errors confused the sounds associated with person and frisbee, whose acoustic forms resembled each other. The published traces allow comparison of those responses.

Blind scoring reduces the possibility that an observer inferred the answer from seeing the object. The result supports reliable learned object–sound associations under training. The separate natural-copying panel illustrates social vocal flexibility, not an additional object-labeling trial or evidence of grammatical language.
""","The object labels were assigned by the training procedure and evaluated from vocal output. Control of observer information is essential when judging animal communication. Error structure matters conceptually because similar acoustic responses can be confused even when the presented objects differ.")
add('Natural copying preserves another animal’s contour','C','C1a',"""
King and colleagues analyzed individually identified whistles during health assessments and recordings of managed dolphins. They compared each possible copy with both the apparent owner’s signature and the copier’s own signature, using blind similarity judgments and acoustic measurements.

A calf could reproduce its mother’s contour while retaining a separate signature of its own. The original spectrograms show frequency in kilohertz and time in seconds across owner, copy, and copier rows.

These comparisons support copying of another animal’s distinctive pattern rather than misclassification of the copier’s usual whistle. Copies retained systematic acoustic differences, so the evidence does not support perfect impersonation. Individual source identification is crucial because similar calls alone cannot reveal who copied whom.
""","A hydrophone is an underwater microphone. Source assignment depends on the recording preparation, not on recognizing the contour by eye. A copied signature must resemble the model owner more than the copier’s ordinary signature; otherwise normal production could be mistaken for imitation.")
add('Copying can occur in either direction within a pair','C','C1b',"""
Natural signature-whistle copying is not restricted to calves copying mothers. King and colleagues documented mother–calf pairs in which a mother reproduced the calf’s contour, and some pairs showed copying in both directions.

The published example separates the calf’s signature, the mother’s copied versions, and the mother’s own signature. Contours were extracted with 5-ms time resolution, permitting comparison of frequency changes throughout a whistle rather than only its average pitch.

Bidirectional capacity weakens an interpretation of every copy as simple immature practice of maternal sounds. It is compatible with interactive social signaling, but the recordings do not show what a copied contour means to its recipient. Function requires response-based evidence beyond production similarity.
""","The figure reverses the copying direction shown previously: the calf is the model owner and the mother is the copier. Measurement resolution specifies temporal sampling of the extracted contour; it does not establish the timing resolution of the animal’s auditory system.")
add('Copying is concentrated among closely associated animals','C','C2 C1c',"""
King and colleagues quantified association using a **coefficient of association**, ranging from 0 for little recorded association to 1 for frequent co-occurrence. This measure describes observed social contact, not an experimentally manipulated bond.

Pairs producing signature-whistle copies had a mean coefficient near 0.8, compared with approximately 0.4 among noncopying pairs. Copies occurred particularly in mother–calf and male–male relationships. The separate colored example shows one male copying another’s distinctive contour.

Association with close relationships is consistent with an affiliative role. It does not show that copying causes bonding or that every strongly associated pair copies. Some closely bonded males did not copy, so social affiliation appears to permit this behavior without making it obligatory.
""","The histogram compares distributions of association coefficients; it should not be read as a randomized social manipulation. The male spectrogram illustrates the kind of interaction represented by the copying category. Strong association and vocal copying may both arise from relationship history.")
add('A copied contour can retain a distinguishable producer','C','C3 C1c',"""
King and colleagues measured whistle duration, frequency range, start and end frequencies, and repeated modulation segments. A **loop** is a recurring contour pattern within one whistle, sometimes separated from another loop by a brief gap.

Although copies preserved the owner’s broad contour, they often differed consistently in detailed acoustic parameters. Frequency and duration measurements placed copies between or apart from the original and the copier’s ordinary signature in the published multidimensional comparison.

This combination suggests that a copied whistle can refer to another individual without concealing that a different dolphin produced it. Deliberate deception was not demonstrated. The display summarizes acoustic similarity, rather than recording how a recipient’s neurons represent either identity.
""","The multidimensional display combines several measured acoustic properties; its axes are abstract coordinates rather than kilohertz or seconds. Use it only to discuss separation and similarity among measured calls. The colored spectrogram retains the actual time and frequency axes for the corresponding behavioral comparison.")
add('Copying follows the owner’s call rapidly','C','C1a',"""
King and colleagues examined the interval between an owner’s signature whistle and another dolphin’s copy. **Vocal matching** is a response that changes a call toward the acoustic pattern of a preceding signal, rather than simply increasing call rate.

During managed-dolphin exchanges, copies occurred within 1 s of the original owner’s signature. A comparison with intervals involving the copier’s own signature helped test whether timing reflected a general tendency to call frequently.

Rapid, contour-specific responses are consistent with interactive matching. Natural recordings still cannot establish the recipient’s interpretation, and high call rates make timing alone insufficient. The strongest inference combines identified producers, contour resemblance, and temporal organization rather than treating any short interval as evidence of addressing.
""","In the wild health-assessment recordings, call rates were high, which made a purely sequential interpretation difficult. The particularly short managed-dolphin intervals provided cleaner temporal evidence. Natural temporal association is not the same as an experimental manipulation of a copied label.")
add('Observed copying was not accompanied by aggression','C','C1c',"""
King and colleagues combined acoustic recordings with observations of managed adult males. One pair engaged in repeated exchanges of the same signature contour while also showing substantial synchronized behavior, an indicator of close social association in this setting.

Copying was not accompanied by observed aggression. Signature copies were rare in the health-assessment records: approximately 0.18 copies per minute per individual in recording sets that contained copying, despite much higher overall whistle rates.

The evidence favors an affiliative interpretation over an aggressive one for these observed exchanges. It does not prove that copying can never occur during conflict elsewhere. A rare behavior can be socially selective, so low copy rates should not be equated with an absence of vocal-learning capacity.
""","The rate applies to recording sets in which copying occurred, not to all free-ranging dolphins at all times. The behavioral observations constrain context but do not reveal intentions. Synchronized swimming and copying may both be consequences of a close relationship.")
add('Playback asks whether a copy functions as an address','K','K3',"""
King and Janik tested whether hearing a copy of an animal’s own signature triggers a matching reply. **Addressing** means directing a communication act toward a particular recipient, rather than merely broadcasting the producer’s own identity.

They recorded signature whistles from free-swimming groups in Scotland, synthesized their contours, and played copies through an underwater speaker. A typical playback contained two whistles separated by 3 s; responses were analyzed before and after playback.

Groups produced matching contours preferentially after own-signature copies. The published spectrograms distinguish the playback from replies. This manipulation links copied identity information to a selective response, but the study could not acoustically localize every reply to a particular dolphin within the group.
""","The key advance over natural recording is manipulation of the incoming contour. The image is a published representation of the actual playback and response sequence. Inability to localize the caller is a material limitation when interpreting the selective reply as the signature owner answering.")
add('Signature identification depends on delivery patterns','K','K4',"""
King and Janik identified candidate signature whistles from their repeated delivery pattern in recordings of free-swimming groups. This method uses the tendency for signature contours to recur in characteristic bouts, rather than requiring physical capture to identify each signal.

They then created contour copies for playback and monitored whistles during the minute before and the minute after the stimulus. The timeline displays different contour identities across that 120-s observation window.

Repeated matching contours appeared especially after own-signature-copy playback. The identification method makes a field experiment possible, but misclassifying a nonsignature contour would weaken the addressing test. The authors therefore checked how contour classification affected interpretation and used control playback conditions rather than relying on repetition alone.
""","The signature identification method is called SIGID in the source paper. Letters in the timeline distinguish contour types, not confirmed individual positions. The temporal window is anchored to playback at zero seconds; the plot does not measure a neuron’s firing rate.")
add('Familiar and unfamiliar controls test different alternatives','K','K2',"""
King and Janik compared own-signature-copy playbacks with familiar control whistles from the same population and unfamiliar synthetic signatures from other populations. Familiar controls test a response to a known local signal; unfamiliar controls test novelty and general responsiveness.

The response measure was whether subsequent whistles matched the playback contour. Own-signature-copy stimuli elicited matching replies more often, whereas unfamiliar controls did not elicit matching and familiar controls rarely did.

The control classes were not acoustically identical: some familiar controls retained natural voice information while copy stimuli were synthesized. The selective matching result nevertheless argues against a simple novelty response or indiscriminate copying of any whistle. It supports identity-linked addressing under the field conditions tested.
""","A good control targets a particular alternative. Novelty and local familiarity are separate explanations, so both comparisons matter. The paper also analyzed familiar-control classification issues; do not describe all control signals as experimentally identical except for social identity.")
add('Reply similarity distinguishes matching from extra calling','K','K1',"""
King and Janik asked independent observers to compare reply contours with the playback pattern. A matching reply should resemble the incoming contour more closely than unrelated whistles produced in the same response period.

Replies after own-signature-copy playback had high contour similarity. Other whistles after those playbacks, familiar-control responses, and unfamiliar-control responses generally resembled their stimuli less closely. The published plot summarizes these different acoustic response classes.

The distinction matters because an animal might call more after any audible event without answering the particular signal. Here the key effect involved which contour was produced, rather than a general rise in whistle rate. Similarity supports selective matching while leaving the identity of every responding group member unresolved.
""","Similarity scores summarize human assessments of contour resemblance; they are not a direct readout of dolphin perception. The noncopy-response category is a useful within-treatment comparison. A matching whistle and a high overall call rate are different forms of evidence.")
add('Matching replies appear within a few seconds','K','K3',"""
King and Janik measured the delay between playback and subsequent whistles. The average first-whistle latency was approximately 2 s after own-signature-copy playback, compared with approximately 14 s after familiar control playback.

For specifically matching replies, the average latency after copy playback was 3.8 s. Matching control responses were much less common and later. These timing measurements complement the contour comparisons by showing a rapid response to the manipulated signal.

A short latency strengthens the interpretation of a directed vocal exchange, especially when the response contour is selective. It does not identify the responding animal or prove that the whistle was understood as a human-style name. Both timing and identity-related acoustic information are needed for that functional inference.
""","First-whistle latency and first-matching-reply latency are different measures; do not combine them into one response time. The spectrogram examples show the acoustic sequence, whereas the numerical averages come from the article’s results. The mean is not a claim that every reply occurred at exactly that delay.")
add('Selective replies support addressing with bounded claims','K','K4',"""
King and Janik found selective matching after playback of an animal’s signature contour, without a corresponding general increase in calling or a clear treatment-specific movement toward the speaker. Addressing can therefore be expressed through call identity rather than approach.

Natural copying was rare enough that a matching reply from an unrelated third party was considered unlikely. However, the recording could not directly assign all replies to the signature owner, so this alternative was constrained rather than eliminated.

The result supports learned vocal labels functioning in directed social communication. It does not demonstrate grammar, conversation about absent individuals, or an arbitrary vocabulary comparable with human language. Those questions require different experimental contrasts and direct source identification.
""","The timeline shows which contours occurred around playback, not who occupied each location. Functional language analogies can organize questions, but should not replace the measured result: a selective contour-matching reply to a manipulated signature stimulus.")
add('Former companions remain recognizable after separation','M','M1',"""
Bruck used records from managed dolphin facilities to identify former companions with documented periods of cohabitation and separation. **Social memory** here means a persistent behavioral distinction between a former associate’s whistle and an unfamiliar dolphin’s whistle.

Recipients heard recorded signature whistles after separation periods ranging from months to 20.5 years. Familiar and unfamiliar signals were matched for the caller’s age and sex, and response order was counterbalanced.

Responses remained stronger for familiar whistles even after very long separation. The published plot groups intervals into several duration categories. This finding establishes long-lasting acoustic social recognition in the tested setting, not a lifetime memory guarantee or a neural measurement of how an identity is stored.
""","Documented transfer histories make the long separation intervals interpretable. The longest successful comparison was 20.5 years, which is the observed duration rather than an extrapolated upper bound. Managed-facility histories differ from uncontrolled contact possibilities in the wild.")
add('Habituation controls general responses to whistles','M','M1',"""
Bruck first played unfamiliar signature whistles until recipients stopped showing a response. **Habituation** is a reduction in responding to repeated or similar stimulation. This step reduced the chance that any subsequent whistle would evoke strong attention merely because playback had begun.

The test then compared familiar and unfamiliar whistles, with a 5-min interval between playback events and counterbalanced order. Playbacks were triggered when the recipient was within 1 m of the speaker and separated from other animals.

Stronger familiar-whistle responses after habituation support discrimination based on social history, rather than persistent arousal to every sound. Habituation cannot erase all differences in motivation or prior experience. Its role is to control generalized responsiveness before testing a specific familiar signal.
""","Habituation was to unfamiliar whistles, not repeated presentation of the familiar test signal. Counterbalancing helps separate stimulus class from order effects. Self-separation and a standardized starting distance reduce social facilitation and position differences, but do not create a completely context-free memory assay.")
add('Behavioral scores operationalize recognition strength','M','M2',"""
Bruck classified responses by behavior: head turning, approach to within 1 m, sustained proximity beyond 2 s, and stronger physical or swimming engagement. An **ordinal score** ranks categories without assuming that equal numerical steps represent equal biological changes.

Familiar playbacks produced higher response scores than unfamiliar playbacks. Calves were also more responsive to unfamiliar signals than adults or juveniles, showing that developmental stage affects background responsiveness as well as recognition behavior.

The score makes a complex behavioral response comparable across tests. It does not measure memory strength in physical units or establish that a response of twice the score means twice the recognition. Familiar–unfamiliar comparisons and age-related responsiveness must therefore be interpreted together.
""","The original figure separates response categories by life stage and familiarity. A two-second proximity boundary defines a scoring category, not a neural memory time constant. Strong motor engagement is evidence of response intensity, while recognition is inferred from its relationship to familiarity.")
add('Long persistence does not prove that memory never decays','M','M1',"""
Bruck found no clear reduction in familiar-whistle recognition across the tested separation categories, including the longest intervals. The familiar–unfamiliar difference persisted after more than 15 years, with recognition documented up to 20.5 years.

Recorded kinship, sex, and previous cohabitation duration did not clearly account for the response pattern. Those negative comparisons narrow simple explanations, but they do not establish that relationship quality or experience can never influence recognition.

The observed persistence is consistent with memory serving relationships in societies where groups separate and reunite. That adaptive interpretation is a hypothesis: the experiment did not measure survival or reproductive benefits. Nor does a lack of detected decline prove absolutely unchanged memory throughout the separation period.
""","Distinguish a measured absence of a trend from proof that no decay exists. Behavioral sensitivity and uneven histories can conceal smaller changes. The proposed ecological benefit follows from the social setting, but fitness consequences were not tested in this playback study.")
add('Calf presence changes a mother’s frequency range','S','S1bc',"""
Sayigh and colleagues compared the same mothers’ signature whistles with and without their dependent calves during Sarasota health assessments. A **within-individual comparison** controls each mother’s characteristic contour, making contextual modification easier to distinguish from differences among animals.

One mother’s maximum contour frequency rose from about 14.4 to 15.8 kHz with her calf. Across mothers, the mean increase was 2.4 kHz, while the recognizable overall signature pattern was retained.

The measured change is compatible with calf-directed vocal modification. Because calf presence was not randomly assigned, the comparison cannot fully separate audience effects from every change in arousal or capture context. It establishes contextual acoustic plasticity, not improved calf learning or a neural mechanism for that adjustment.
""","The plotted examples are from the same female, FB55, not two different mothers. The numerical example is illustrative, whereas the 2.4-kHz result summarizes the paired comparison. The published colors are preserved and do not imply recoloring by the slide author.")
add('Mothers consistently raise maximum whistle frequency','S','S1d',"""
Sayigh and colleagues aligned each mother’s recordings with and without her calf, rather than averaging unrelated females into two groups. Individual signature patterns differ widely, so paired comparisons are essential for detecting an audience-associated change.

Mothers increased maximum contour frequency in the calf-present condition. The average difference was 2.4 kHz, and the effect remained when analyses addressed age-related differences between recording occasions. The published paired display preserves each maternal identity.

Consistency across identities strengthens the interpretation that the change is contextual rather than an accidental difference in which mothers were recorded. It still does not turn the observational condition into a randomized intervention. Other factors correlated with calf presence, including the social and handling context, remain possible contributors.
""","The article’s original panel uses standardized changes to compare mothers with different baseline contours. The kilohertz result comes from the reported unstandardized frequency comparison. Do not treat the standardized vertical axis as absolute acoustic frequency.")
add('Wider frequency ranges do not require shorter loops','S','S2',"""
Sayigh and colleagues measured several acoustic properties rather than treating all calf-associated changes as one effect. Maximum frequency increased and minimum frequency decreased, producing a wider frequency range in mothers’ whistles with calves.

**Bandwidth** is the span of frequencies in a signal; the study’s contour measure summarized the central frequency range. Temporal measures included loop duration, the interval between repeated loops, and the number of loops within a whistle.

Loop duration did not reliably shorten, and median frequency did not show the same clear change as maximum frequency. The result therefore concerns selective modification of spectral structure, not a wholesale acceleration of calling. Similarity to human child-directed speech is a functional comparison, not evidence that every acoustic feature changes in the same way.
""","The original metric plot includes statistical annotations because it is preserved exactly as published; the teaching text emphasizes the biological effects. Frequency range and duration describe different signal dimensions. Keeping the null temporal result prevents an overgeneralized claim about simplified or shortened calf-directed calls.")
add('Calf-directed modification leaves its function unresolved','S','S1bc',"""
Sayigh and colleagues interpreted the wider maternal frequency range as a form of calf-directed communication, comparable in some respects with human child-directed speech. The same mother’s signature contour remained recognizable while its acoustic range changed.

The study measured adult vocal output during health assessments. It did not directly test whether calves paid more attention, learned a contour faster, formed stronger bonds, or recognized their mothers more accurately when hearing the modified whistles.

Attention, learning, and bonding are therefore proposed functions rather than measured outcomes. Earlier evidence for contour recognition and long social memory makes those proposals biologically plausible, but does not validate them. The experiment establishes flexible audience-associated production; testing benefit requires controlled receiver-response or developmental experiments.
""","A receiver experiment could manipulate the relevant acoustic range while retaining identity contour and then measure calf attention or learning. That proposal is an experimental inference, not a figure or result claimed from this paper. The existing study does not specify the receptors or ion channels generating the vocal change.")
assert len(slides)==44,len(slides)
take=[
('Anatomical routes','Diffusion imaging supports a candidate auditory route through inferior colliculus, thalamus and temporal cortex; it does not identify a recognition circuit or synaptic mechanism.'),
('Contour-based identity','Synthetic whistles retain identity-sensitive information after original voice features are removed. Familiarity and self-similarity controls distinguish recognition from simple acoustic preference.'),
('Production learning','Trained dolphins can imitate new tonal patterns and acquire object-controlled whistles. These capabilities do not establish natural object naming or human language.'),
('Copying and addressing','Natural copies are selective and distinguishable from owners’ whistles; controlled copy playbacks elicit contour-matching replies. Group-level source uncertainty limits who-answering-whom claims.'),
('Durable social memory','Familiar signature whistles remain recognizable after separation up to 20.5 years. Persistence does not prove memory never decays or reveal its neural storage.'),
('Contextual vocal plasticity','Mothers widen signature-whistle frequency range with calves. Attention, developmental learning and bonding benefits remain proposed functions, not outcomes measured by that study.')
]
spec={'lecture':42,'theme':'quartz-steel','content_slides':44,'title_image':fig('S1a'),'slides':slides,'takeaways':{'cite':'Berns et al. (2015); Janik et al. (2006); Richards et al. (1984); King et al. (2013); King & Janik (2013); Bruck (2013); Sayigh et al. (2023)','refs':[r[2]+' https://doi.org/'+r[1] for r in REF.values()],'items':[{'lead':a,'text':b} for a,b in take]}}
(ROOT/'lecture.json').write_text(json.dumps(spec,indent=2,ensure_ascii=False)+'\n')
themes_path=ROOT.parents[1]/'course/themes.json'
themes=json.loads(themes_path.read_text())
themes['palettes']['quartz-steel']={'label':'quartz gray / steel white','title_bg':'70767B','title_text':'FFFFFF','title_muted':'E0E4E7','bg':'FFFFFF','heading':'43474A','text':'000000','muted':'000000','tint':'F1F2F3','accent':'70767B','rule':'D5D8DA'}
themes['used']['42']='quartz gray / steel white'
themes_path.write_text(json.dumps(themes,indent=2)+'\n')
(ROOT/'PAPERS.md').write_text('# Lecture 42 / S2 — primary sources\n\nAll seven requested PDFs were supplied by the instructor and inspected. No inaccessible article is required for this deck. Figures are unaltered crops from the supplied PDFs; axes, units and panel lettering are retained. No created images or web images are used.\n\n'+'\n'.join(f'{i}. {r[2]} https://doi.org/{r[1]}' for i,r in enumerate(REF.values(),1))+'\n')
(ROOT/'source_manifest.json').write_text(json.dumps({k:{'doi':r[1],'pdf_sha256':hashlib.sha256((ROOT/f'papers/{k}.pdf').read_bytes()).hexdigest(),'source':'instructor-supplied published article PDF','crop_manifest':'crops.json'} for k,r in REF.items()},indent=2)+'\n')
print('Written',len(slides),'content slides; words',min(sum(len(p.split()) for p in s['body']) for s in slides),max(sum(len(p.split()) for p in s['body']) for s in slides))
