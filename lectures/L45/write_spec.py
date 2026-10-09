import json,re,pathlib
D=pathlib.Path(__file__).parent
source=json.loads((D/'sources/available-pdfs.json').read_text())
R={x['key']:x['full_reference'] for x in source}
U={x['key']:'https://doi.org/'+x['doi'] for x in source}
A={'ford91':'Ford (1991)','deecke00':'Deecke et al. (2000)','marino04':'Marino et al. (2004)','szymanski99':'Szymanski et al. (1999)','whistles21':'Souhaut & Shields (2021)','biphonic20':'Filatova (2020)','imitation18':'Abramson et al. (2018)','innovate22':'Hill et al. (2022)','social21':'Weiss et al. (2021)','network24':'Jourdain et al. (2024)','repertoire20':'Wellard et al. (2020)','pitman12':'Pitman & Durban (2012)','hunting24':'McInnes et al. (2024)','pilot26':'Selbmann et al. (2026)','astro25':'Venkatesh et al. (2025)'}
F={}
def f(name,key,fig,description):
 F[name]={'path':'figures/'+name+'.png','kind':'article','caption':f'{A[key]}, Fig. {fig}. {description}','source_url':U[key]}
f('mri1','marino04','1','Labeled rostral coronal brain section')
f('mri3','marino04','3','Amygdala and adjacent forebrain anatomy')
f('mri4','marino04','4','Insula, operculum and cortical fields')
f('mri7','marino04','7','Cerebellar hemispheres, vermis and brainstem')
f('mri13','marino04','13','Superior and inferior colliculi in an axial section')
f('mri16','marino04','16','Corpus callosum, internal capsule and basal ganglia')
f('mri17','marino04','17','Dorsal hemispheric folds and cortical organization')
f('hearing1','szymanski99','1','Whale position, acoustic projectors and recording electrodes')
f('hearing3a','szymanski99','3(a)','Auditory brainstem waveforms at three sound levels')
f('hearing3b','szymanski99','3(b)','Evoked-potential threshold relative to background activity')
f('hearing4','szymanski99','4','Brainstem response amplitude as a function of stimulus level')
f('hearing5','szymanski99','5(a–c)','Behavioral and brainstem audiograms of the same whales')
f('hearing5b','szymanski99','5(b)','Vigga’s behavioral and brainstem hearing thresholds')
f('hearing5c','szymanski99','5(c)','Mean frequency-dependent hearing thresholds')
f('ford2','ford91','2','Acoustic relationships among resident pods and clans')
f('ford3','ford91','3','Related but distinguishable discrete call variants')
f('ford18','ford91','18','Historical and later repertoires of southern resident pod J')
f('ford12','ford91','12','Calls of pod C and the captive whale Namu')
f('whistle1','whistles21','1','Historical and recent stereotyped whistle forms')
f('whistle2','whistles21','2','Newly identified stereotyped whistle contours')
f('biphonic1','biphonic20','1','Amplitude measurement locations on biphonic call components')
f('biphonic2','biphonic20','2','Independent acoustic distances of the two call components')
f('biphonic3','biphonic20','3','Received and hearing-adjusted component amplitudes')
f('deecke1','deecke00','1','Parameters used to quantify the structure of call N4')
f('deecke2','deecke00','2(a–c)','Within-matriline change and between-matriline divergence of N4')
f('deecke4','deecke00','4(a–d)','Longitudinal pulse-rate and duration measurements')
f('imitate1','imitation18','1(a–c)','Original experimental arrangement for vocal copying')
f('imitate2a','imitation18','2(a,b)','Human “hello” model and killer-whale copy')
f('imitate2b','imitation18','2(c,d)','Novel conspecific breathy-raspberry model and killer-whale copy')
f('imitate3ab','imitation18','3(a,b)','Alignment of familiar conspecific sound features')
f('imitate3cd','imitation18','3(c,d)','Alignment of novel human and conspecific sounds')
f('imitate4','imitation18','4','Dissimilarity of model–copy and mismatched sound pairs')
f('innovate2','innovate22','2','Trials before behavior repetition across animals and sessions')
f('social1cd','social21','1(c,d)','Aerial observations of surfacing synchrony and body contact')
f('social2','social21','2(a–f)','Different networks for association, synchrony and contact')
f('network3','network24','3','Mixed-diet whales within a connected social network')
f('typeC4','repertoire20','4','Type C killer whale encountered during acoustic fieldwork')
f('typeC5','repertoire20','5(a–d)','Published color spectrograms of Type C call categories')
f('typeC7','repertoire20','7(a–f)','Biphonic Type C calls with distinct spectral components')
f('wave2','pitman12','2','A coordinated wave dislodges a Weddell seal')
f('wave3','pitman12','3','Whales approach an ice floe during wave washing')
f('hunt2','hunting24','2(A–D)','Canyon habitat, whale locations and prey encounter locations')
f('hunt6','hunting24','6(A–D)','Tracks of groups searching and feeding around canyon contours')
f('hunt6a','hunting24','6(A)','An offshore search track along canyon habitat')
f('hunt6d','hunting24','6(D)','A focal-follow track linking search and feeding')
f('hunt8','hunting24','8(A–D)','Predation on different marine-mammal prey')
f('hunt8a','hunting24','8(A)','Coordinated attack on a California sea lion')
f('hunt8bc','hunting24','8(B,C)','Northern-elephant-seal and Pacific-white-sided-dolphin predation')
f('hunt9','hunting24','9(A–D)','Attack sequence and feeding on a grey-whale calf')
f('hunt9a','hunting24','9(A)','A grey-whale mother and calf under attack')
f('hunt9d','hunting24','9(D)','Killer whales feeding on a grey-whale calf')
f('hunt4','hunting24','4(A,B)','Seasonal encounters, group size and prey availability')
f('hunt5','hunting24','5','Seasonal occurrence of transient whales and grey-whale calves')
f('pilot1','pilot26','1','Tagged movement and acoustic activity across controlled playbacks')
f('pilot3','pilot26','3','Horizontal movement responses to playback categories')
f('pilot5','pilot26','5(a–e)','Group cohesion and movement changes during playbacks')
f('astro4a','astro25','4(a)','GFAP-labeled layer 1 in killer-whale motor cortex')
f('astro5a','astro25','5(a)','Nissl-stained layers of killer-whale motor cortex')
f('astro3','astro25','3','White-matter astrocyte cell-body diameters across species')
slides=[]
def S(title,text,fig,keys,extra='',secondary=None):
 body=[x.strip() for x in text.strip().split('\n\n')];assert len(body)==3,(title,len(body))
 notes=[re.sub(r'\*\*|_','',x) for x in body]
 if extra:notes.append(extra)
 sd={'title':title,'layout':'figure-right' if len(slides)%2==0 else 'figure-left','figure_width':5.7,'body':body,'transcript':notes,'cite':'; '.join(A[x] for x in keys),'refs':[R[x] for x in keys],'figure':F[fig]}
 if secondary:
  sd.pop('figure');sd['figures']=[F[fig],F[secondary]];sd['layout']='figures-right';sd['primary_figure_height']=2.65
 slides.append(sd)

S('Ecotypes differ in prey and social behavior', '''A killer-whale **ecotype** is a population-associated form distinguished by ecological and behavioral characteristics. In the northeastern Pacific, resident whales specialize on fish, whereas transient whales hunt marine mammals. These feeding differences coexist with distinctive social and acoustic patterns; they are not merely differences in the prey encountered during one trip.

McInnes and colleagues followed identifiable transient groups around Monterey Canyon and documented coordinated attacks on sea lions, seals and cetaceans. Natural dorsal-fin shapes and scars allowed researchers to recognize individuals across encounters. Focal follows linked group movements with searching, pursuit and feeding rather than treating every sighting as a successful hunt.

Ford’s resident-whale recordings instead linked stable social groups with shared call repertoires. Ecological specialization and vocal tradition must be attributed to the population studied. Neither dataset establishes that every killer-whale population organizes hunting or communication in the same way.''', 'hunt8a',['hunting24','ford91'])
S('Postmortem MRI resolves brain organization', '''**Magnetic resonance imaging**, or MRI, distinguishes tissues using their responses in a magnetic field. Marino and colleagues scanned an adult male killer-whale brain obtained after death from natural causes and preserved in buffered formalin. This preparation preserved gross internal relationships without requiring the brain to be sliced physically for every anatomical view.

A 1.5-T scanner acquired contiguous coronal and axial sections, representing frontal and horizontal viewing planes. The images had 2-mm section thickness and approximately 0.63-mm resolution within each plane. Researchers identified structures by comparison with published odontocete photographs, illustrations and MRI atlases.

The resulting labels establish the positions and visible proportions of brain regions in this specimen. They do not measure neuronal firing during communication, synaptic connections or learning-related activity. Fixation and examination of one postmortem brain also limit conclusions about living tissue properties and variation among individuals.''', 'mri1',['marino04'])
S('Antibody labeling resolves cortical astrocytes', '''**Astrocytes** are glial cells that support the cellular environment of neurons. Venkatesh and colleagues examined formalin-fixed cortical tissue from several cetaceans, including killer-whale motor and auditory cortex. Paraffin sections were 6 μm thick, permitting cellular measurements that complement the larger-scale regional relationships resolved by MRI.

Antibodies labeled **glial fibrillary acidic protein**, or GFAP, an intermediate-filament protein used to identify astrocytes. A fluorescent secondary antibody detected the bound primary antibody, while DAPI counterstaining labeled nuclei. Sections processed without primary antibody controlled for nonspecific fluorescence. Tissue identity was concealed during image thresholding, reducing expectations about species or cortical region.

The killer-whale motor cortex contained prominent GFAP-positive labeling in superficial layer 1. This establishes the distribution of the detected marker, rather than measuring astrocyte activity during hearing or learning. GFAP does not identify every astrocyte, and fixed tissue cannot reveal moment-to-moment neurotransmitter handling. Marker distribution therefore requires interpretation alongside the preparation and its controls.''', 'astro4a',['astro25'])
S('The insula lies within an elaborate operculum', '''The **insula** is cortex situated within the lateral cerebral region. An **operculum** is an overlying cortical fold that covers a deeper region. Marino and colleagues identified marked elaboration of the insular cortex and surrounding temporal operculum in coronal sections of the killer-whale brain, using established anatomical comparisons to assign labels.

The MRI sections distinguish insular tissue, surrounding cortex and nearby internal structures. The authors proposed that this elaboration might relate to cetacean sensory or communicative specialization. They also emphasized that the arrangement of cortical functional maps differs across mammalian lineages, so a human regional function cannot simply be transferred to a whale.

No auditory stimulation, vocal production task or lesion experiment was performed in this preparation. Consequently, assigning a specific call-learning role to the operculum remains a hypothesis. The observed anatomical elaboration is established; its contribution to recognizing group calls or controlling vocal imitation is unresolved.''', 'mri4',['marino04'])
S('Cortical layers differ in glial labeling', '''A **cortical layer** is a depth-defined subdivision of cortex with characteristic cellular organization. Venkatesh and colleagues identified layer 1, combined layers 2/3, layer 5 and underlying white matter using GFAP labeling, Nissl staining and myelin staining. **Nissl staining** marks cellular material rich in ribosomal RNA and provides landmarks for identifying neuron-containing tissue.

Motor-cortex comparisons found greater GFAP-positive area in layer 1 and white matter than in layers 2/3 and 5. Across the sampled species, the corresponding mean labeled fractions were approximately 4.17%, 4.06%, 1.66% and 0.87%. These are percentages of measured tissue area occupied by the marker, not percentages of all cells that are astrocytes.

Killer-whale tissue retained the contrasting superficial and deeper labeling pattern. Layer 1 had relatively sparse Nissl staining alongside greater GFAP labeling. Tissue from one animal per species limits population-level generalization, and stain intensity does not measure synaptic strength. The result establishes a laminar cellular organization without identifying a circuit for vocal tradition.''', 'astro5a',['astro25'],secondary='astro4a')
S('Cerebellar hemispheres flank a narrow vermis', '''The **cerebellum** is a hindbrain structure whose hemispheres flank a central region called the **vermis**. Marino and colleagues identified large cerebellar hemispheres and a comparatively narrow vermis in the killer-whale brain. Coronal MRI sections also retained the relationship between the cerebellum, brainstem and cerebral tissue above it.

The authors compared these proportions with other odontocete descriptions and found the arrangement consistent with that lineage. Their labeled sections identify cerebellar peduncles, the bundles that connect cerebellar tissue with the brainstem. These gross features provide a structural description rather than a measurement of a hunting-specific motor computation.

Coordinated swimming and precise prey attacks require controlled movement, but this MRI preparation did not measure those behaviors or perturb cerebellar activity. The anatomical result therefore supports comparison of hindbrain organization across species. It does not establish that the observed vermis proportions explain wave washing or coordinated attack timing.''', 'mri7',['marino04'])
S('The inferior colliculi occupy a distinct midbrain', '''The **tectum** is the dorsal midbrain region containing the superior and inferior colliculi. Marino and colleagues identified well-developed inferior colliculi in the killer-whale specimen, with a spatial arrangement resembling other odontocetes. Axial sections retained the positions of both collicular pairs relative to the cerebellum and nearby brainstem tissue.

The **inferior colliculus** is associated with auditory processing in mammalian neuroanatomy. Its identification provides an anatomical candidate within the hearing pathway, but the MRI signal does not reveal frequency tuning, response timing or the identity of active neurons. Labels were assigned through comparison with established anatomical material rather than functional stimulation.

The study also described an unusual lateral position of the cerebral peduncle, a major fiber-bundle region. Neither regional position nor gross size identifies how group-specific calls are encoded. Establishing those mechanisms would require direct physiological or connectivity evidence beyond this postmortem anatomical preparation.''', 'mri13',['marino04'])
S('Astrocyte size is a cellular measurement', '''Venkatesh and colleagues measured **fibrous astrocytes**, the relatively sparsely branched astrocytes associated with white matter. Cells were selected for consistent GFAP labeling, an in-plane cell body and expected morphology. The **soma**, or cell body, was measured along its longest visible axis, rather than treating the extent of branching processes as cell-body diameter.

The mean measured killer-whale soma diameter was approximately 11.54 μm, compared with 7.53 μm in the pygmy sperm whale and 12.50 μm in the false killer whale. The rodent comparison was approximately 10.34 μm and did not differ detectably from the sampled cetaceans. Brain regions were pooled when one region lacked enough suitable cells for measurement.

Different cell-body sizes are established morphological observations. They do not directly quantify neurotransmitter clearance, ion regulation or learning ability. Formalin-fixed sections and limited tissue availability constrain the comparison, while GFAP-negative cells are not represented equally. Proposed relationships between astrocyte morphology and complex behavior therefore require functional experiments beyond the measurements in this study.''', 'astro3',['astro25'],secondary='astro4a')
S('Conditioned responses measure hearing thresholds', '''An **audiogram** records the lowest sound level detected at each tested frequency. Szymanski and colleagues trained adult killer whales to respond to tones at an underwater station; physiological recordings used a separate surface station. A **go/no-go task** requires an action when the signal is present and withholding that action when it is absent.

During behavioral testing, a 2-s tone occurred after a variable delay, and the whale had 4 s to respond. Sound level decreased after detections and increased after misses. Threshold required repeated detections at one level and failures at the next lower level, linking the estimate to a reproducible behavioral criterion.

Silent trials, disconnected equipment and frequencies the projector could not produce tested responses without a valid acoustic signal. An observer unaware of signal timing judged behavior, and personnel were varied to reduce inadvertent cues. These controls distinguish hearing from responses to trainers, although motivation and the response criterion still influence threshold estimates.''', 'hearing1',['szymanski99'])
S('Hearing sensitivity varies with sound frequency', '''Szymanski and colleagues measured both conditioned detection and auditory brainstem responses in the same killer whales. Their **frequency-dependent threshold** curves were approximately U-shaped: low and very high frequencies required greater sound levels than the most sensitive middle range. Sound frequency is expressed in kilohertz, with 1 kHz corresponding to 1,000 cycles per second.

The combined mean audiogram had its minimum near 20 kHz, at approximately 36 dB referenced to 1 µPa. This reference expresses underwater sound-pressure level; it is not directly interchangeable with an airborne sound level. The most sensitive band, defined within 10 dB of the minimum, extended approximately from 18 to 42 kHz.

These measurements establish a broad region of effective hearing under the tested conditions. They do not imply that calls outside that band are inaudible. Detectability also depends on signal level, duration and background noise, which were controlled differently in the behavioral and physiological procedures.''', 'hearing5c',['szymanski99'])
S('Brainstem responses track synchronized activity', '''An **auditory brainstem response**, or ABR, is an electrical potential recorded after sound stimulation. It reflects synchronized population activity rather than a recording from one identified neuron. Szymanski and colleagues placed suction-cup electrodes on the head and body while trained whales maintained a stationary position near an underwater sound projector.

Short tone bursts were delivered at 30 per second, and responses were averaged to distinguish stimulus-linked activity from ongoing electrical noise. The principal waveform peaks occurred within 10 ms of tone onset. At 32 kHz, recorded responses became smaller as the acoustic stimulus was reduced, and later peaks persisted after smaller early components disappeared into background activity.

The authors used the largest late peak-to-trough component for threshold estimation. Averaging and artifact rejection improved detection of reproducible responses, but the scalp potential does not identify a cortical call-recognition circuit. Its amplitude depends on synchrony, electrode placement and stimulus conditions as well as auditory sensitivity.''', 'hearing3a',['szymanski99'])
S('Physiological and behavioral thresholds differ', '''Szymanski and colleagues compared brainstem and behavioral audiograms from the same individuals, reducing uncertainty caused by comparing different animals. The **physiological threshold** was the minimum level producing a repeatable response above averaged electrical background. The behavioral threshold depended on the trained detection response to a much longer tone.

Across tested frequencies, the brainstem audiogram was on average approximately 12 dB less sensitive than the behavioral audiogram. Agreement was closest in the 18–42-kHz sensitive band, where the difference was approximately 5 dB. At 60–100 kHz, disagreement reached approximately 22 dB rather than remaining a fixed offset across the hearing range.

Brief tone bursts and 2-s behavioral tones differ in the time available for auditory integration. The authors discussed this difference as one contribution to the discrepancy. A brainstem threshold can therefore estimate hearing while still exceeding the behavioral detection threshold; the two measures are not interchangeable readings of identical stimulus processing.''', 'hearing5c',['szymanski99'])
S('High-frequency detection extends beyond 32 kHz', '''Both killer whales in Szymanski and colleagues’ study responded behaviorally to tones at 100 kHz, and one also responded at 120 kHz. These direct detections extended beyond the approximately 32-kHz upper limit reported in an earlier individual. A **hearing limit** is consequently an empirical boundary for a tested animal and procedure, not a universal species constant.

The authors monitored the stimulus near the lower jaw, where the whale’s receiving region was positioned, and checked spectral content and level. Silent and disconnected-equipment trials helped exclude responses to nonacoustic cues. Calibrating the underwater projector was essential because a nominal high-frequency setting alone does not establish the sound actually reaching the animal.

High-frequency thresholds were substantially elevated relative to the sensitive middle band, and physiological thresholds exceeded behavioral thresholds. The result establishes ultrasonic detection in the tested whales. It does not establish identical sensitivity across ages, individuals or natural noise conditions, nor a sharp frequency boundary shared by all killer whales.''', 'hearing5b',['szymanski99'])
S('Calls, whistles and clicks differ acoustically', '''Killer-whale recordings contain **clicks**, brief broadband signals associated with echolocation; **whistles**, tonal signals with a frequency contour; and **pulsed calls**, repeated pulses whose timing contributes to their audible character. Ford classified resident communication using recurring call structure, whereas later studies separately examined whistle repertoires and Antarctic call categories.

A **spectrogram** represents sound energy across frequency and time. Wellard and colleagues recorded Type C whales in McMurdo Sound and segmented calls according to changing acoustic components. Their published color recordings retain the original frequency and time axes, allowing particular call categories to be distinguished by their temporal and spectral organization.

These categories describe recorded signals rather than proving a message’s meaning. A call type can remain recognizable while varying among groups or renditions. Type C recordings also concern a different population from northeastern-Pacific residents, so the same broad signal class does not imply a shared dialect or identical behavioral use.''', 'typeC5',['repertoire20','ford91','whistles21'])
S('Discrete repertoires contain persistent call types', '''A **discrete call type** is a recurring acoustic pattern that can be distinguished from other patterns within a repertoire. Ford recorded resident killer-whale pods during repeated encounters and identified the groups using natural individual markings. This connected acoustic samples to known social units rather than assigning every recording to an unidentified population.

Pods produced repertoires of approximately 7–17 discrete call types. Related versions of a call retained recognizable structure while differing in features such as frequency modulation or the arrangement of call segments. Classification therefore separated a shared call category from the more detailed variants associated with particular pods.

Repeated sampling across encounters helped establish that a repertoire was persistent rather than an incidental collection from one recording session. The study nevertheless inferred learning from patterns of stability and group-specific variation. It did not experimentally demonstrate how a calf copied each type or identify the neural machinery that stored the repertoire.''', 'ford3',['ford91'])
S('Shared call types define acoustic clans', '''An **acoustic clan** is a set of pods sharing a vocal tradition, distinguished from other clans by their call repertoires. Ford compared resident pods in coastal British Columbia and recognized four such associations. Pods within a clan shared several discrete call types, whereas the clans in the study did not share those repertoire elements.

Shared calls could still contain pod-specific structural variants. Consequently, **dialect** refers to a patterned group difference within a broader vocal tradition, rather than requiring every signal to be unique to one pod. Acoustic relationships were evaluated alongside known pod identities and repeated recordings.

Pods from different clans sometimes traveled together, and observed association patterns did not always match acoustic similarity. The author proposed descent from ancestral groups and gradual dialect divergence through learning-related change. Those historical mechanisms were interpretations of the observed repertoire organization, not direct records of the founding events or controlled tests of call acquisition.''', 'ford2',['ford91'])
S('Historical recordings retain repertoire continuity', '''Ford compared contemporary resident-whale repertoires with older recordings whose group identities could be assessed. Historical material associated with southern resident pod J from 1958–1961 contained 14 of the 17 call types used by that group in 1979–1983. The recurring repertoire therefore persisted across a period exceeding two decades.

Comparisons distinguished the presence of recognizable call types from their relative frequency of production. Recordings made during foraging and traveling need not contain the same proportions even when the group retains the same repertoire. Behavioral context and recording opportunity were relevant controls when interpreting differences between old and recent samples.

Long-term continuity is consistent with a vocal tradition maintained across generations. It does not establish that every rendition is acoustically unchanged, and it cannot by itself separate inherited predispositions from social learning. The stable group repertoire and later demonstrations of vocal copying provide different forms of evidence rather than duplicating the same experimental test.''', 'ford18',['ford91'])
S('Whistle forms persist across more than 35 years', '''Souhaut and Shields examined southern resident whistles recorded in 2006–2007 and 2015–2017 and compared them with stereotyped forms described from 1979–1982. A **stereotyped whistle** is a recurring tonal contour distinguishable from the more variable whistle forms also present in recordings. Boat and shore recording opportunities supplied acoustic material from the population.

Approximately 53.5% of the analyzed whistles belonged to stereotyped categories. Three of four previously recognized types were still detected, extending the documented persistence of particular contours beyond 35 years. Additional stereotyped forms were identified, so continuity did not require an entirely unchanging catalog.

The failure to detect an older category does not establish that it disappeared, because whistles occur less frequently than pulsed calls and sampling differs across periods. These comparisons establish persistence of recorded forms. They support whistle traditions but do not directly reveal which social partners transmitted a contour or whether a new type originated by imitation.''', 'whistle1',['whistles21'])
S('Biphonic calls contain separately modulated contours', '''A **biphonic call** contains two frequency components that can vary independently. Filatova analyzed lower- and higher-frequency contours in resident-type calls, treating their acoustic information separately rather than assuming that the upper component simply repeated the lower one at a harmonic multiple. A **harmonic** is a component at an integer multiple of a fundamental frequency.

Amplitude measurements were taken from defined locations within each component. Separating contour shape from received amplitude allowed the study to compare acoustic differences among family groups and evaluate how the components might remain detectable. Independent modulation supplies additional potential distinctions between calls that otherwise sound similar in one component.

Wellard and colleagues also documented biphonic forms in Type C whales using color spectrograms. This comparative evidence establishes the signal structure across particular recordings, not one universal family code. Neither study directly recorded the sound-producing tissues during the sampled calls or experimentally mapped the brain regions that distinguish their components.''', 'typeC7',['biphonic20','repertoire20'],secondary='biphonic1')
S('Combining contours improves family classification', '''Filatova quantified differences between the lower- and higher-frequency contours of resident-type biphonic calls. **Dynamic time warping** compares the shapes of sequences while allowing local adjustments in their temporal alignment. This analytical method avoids treating small timing differences as if they necessarily changed the identity of the overall acoustic pattern.

Distances between family groups calculated from the lower component were largely unrelated to distances calculated from the higher component. Classifying calls using both contours assigned them to their family more accurately than relying on either contour alone. Two acoustic dimensions can therefore contain complementary group information rather than redundant copies of the same distinction.

This result concerns acoustic classification performed by the analysis. It supports the proposed availability of family cues to a listener, but it does not demonstrate that whales use the same algorithm or distinguish families from these recordings in a playback task. Behavioral recognition remains a separate experimental question.''', 'biphonic2',['biphonic20'])
S('Hearing sensitivity changes effective call contrast', '''Filatova compared received amplitudes of the two biphonic call components and adjusted them using killer-whale hearing sensitivity across frequencies. **Sensation level** expresses how far a received signal lies above the hearing threshold at its frequency. Equal measured sound pressure need not provide equal perceptual accessibility if thresholds differ.

The higher-frequency component had a greater hearing-adjusted sensation level than the lower component in the analyzed recordings. This contrasts with an interpretation based only on raw amplitude. The authors proposed that the higher component could preserve family information when low-frequency environmental noise masks the lower component.

**Masking** occurs when background sound makes another signal harder to detect. The proposed benefit depends on the actual noise spectrum, propagation and hearing conditions. The study did not experimentally expose whales to masked calls and test recognition, so hearing adjustment supports a plausible sensory explanation rather than establishing successful family recognition under natural noise.''', 'biphonic3',['biphonic20','szymanski99'])
S('Longitudinal recordings quantify call modification', '''Deecke, Ford and Spong compared calls N4 and N9 from the A12 and A30 resident matrilines across 12–13 years. A **matriline** contains individuals connected through maternal ancestry. Repeated recordings from known groups allowed the analysis to distinguish change within a social lineage from acoustic differences between the lineages.

The investigators extracted pulse-repetition-rate contours at evenly spaced positions along each call and included call duration separately. A trained artificial neural network supplied an acoustic similarity index. This was a computer classification tool; it was not a recording of biological neurons or a model established as the whale’s recognition mechanism.

N4 changed detectably within both matrilines, whereas N9 did not show comparable modification during the observation period. Using two call types constrained the idea that all recordings shifted in the same way. The result establishes selective temporal change in a repertoire, rather than uniform replacement of the entire dialect.''', 'deecke1',['deecke00'])
S('Call change need not produce group divergence', '''Deecke and colleagues compared modification of N4 within each matriline with divergence of N4 between matrilines. **Modification** is change in a group’s call over time; **divergence** is an increasing difference between groups. These processes can occur at different rates even when both groups continue producing a recognizable call type.

The acoustic similarity of N4 recordings decreased as the years separating samples increased within each matriline. Between-group differences changed less than the calls changed within either group. Thus, the two lineages modified their calls in sufficiently similar ways that within-group temporal change did not become equally large separation between lineages.

The authors considered horizontal transmission, meaning transfer between social lineages rather than exclusively from mother to offspring. Correlated call change supports that possibility, but it does not directly document an individual listening and copying. Parallel maturational change remained an alternative explanation that the longitudinal observations could not eliminate.''', 'deecke2',['deecke00'])
S('Maturation remains an alternative to cultural drift', '''**Cultural drift** is change in socially transmitted behavior that can accumulate without a consistent directional advantage. Deecke and colleagues examined structural features of N4, including plateau pulse rate, maximum pulse rate, duration and the timing of the maximum. These measurements tested whether call change followed a clear directional trajectory.

The structural changes lacked strong overall directionality. The authors discussed drift combined with horizontal transmission as one explanation for similar modification in two matrilines. However, maturational changes in vocal production could also generate parallel changes if individuals in the groups experienced related age-dependent effects.

The recordings did not assign each call to a known individual or experimentally manipulate exposure to another lineage’s calls. Consequently, the study does not isolate learning from maturation as the sole cause. Its strongest result is that a call can change over years while maintaining relatively stable between-group relationships, with the transmission mechanism remaining partly unresolved.''', 'deecke4',['deecke00'])
S('A copying cue tests vocal production learning', '''**Vocal production learning** means acquiring or modifying a sound through auditory experience, rather than merely learning when to produce an existing signal. Abramson and colleagues tested a trained female killer whale using a previously learned gesture requesting imitation. Familiar actions and sounds established that the subject understood the copying procedure.

Novel conspecific and human models were then presented in live or recorded conditions. During tests of novel sounds, the subject received no reward or corrective feedback for matching the model. Familiar control trials were reinforced, and familiar actions without a copying request helped separate the experimental response from an unrestricted stream of vocalizations.

Recognizable copies of the tested novel sounds support a capacity to match auditory models. This direct experimental result is stronger evidence for imitation than dialect similarity alone. Nevertheless, performance by a trained subject in air does not establish how calves acquire underwater dialects in the wild or identify the neuronal changes underlying a copied sound.''', 'imitate2b',['imitation18'],secondary='imitate1')
S('Novel sound models test rapid acoustic matching', '''Abramson and colleagues selected novel sounds that were absent from the subject’s known trained repertoire and checked spontaneous in-air recordings before testing. The model could be another killer whale or a loudspeaker recording. **Novelty** was therefore evaluated relative to the subject’s prior production, not assumed simply because a signal had an unfamiliar human label.

The whale produced recognizable versions of novel conspecific sounds, often within the first ten trials. Some were copied on the first attempt. Familiar conspecific signals supplied comparison examples in the acoustic analysis, including signals labeled “blow” and “birdy,” whose feature sequences could be aligned with the subject’s copies.

A rapid match without reward on the novel test trial supports production learning rather than gradual trial-by-trial shaping of that sound. The prior imitation training still matters: the study tested a learned copying context. It did not show that every untrained whale spontaneously copies every unfamiliar signal after one exposure.''', 'imitate3ab',['imitation18'])
S('Human models test mimicry without language claims', '''**Vocal mimicry** is imitation of an acoustic model produced by another species. Abramson and colleagues asked the killer whale to copy human sounds, including the word-like model “hello.” Model and response recordings were compared using waveform, spectrogram and acoustic-feature analyses rather than relying exclusively on a listener’s impression.

The whale produced recognizable versions of the tested human models. Copies were imperfect: matching a coarse sequence of acoustic features did not require identical timbre or every spectral detail. “Hello” was among the novel sounds copied on an early attempt, supporting flexibility of production beyond the existing conspecific repertoire.

These results concern sound matching, not the meaning of human words. The subject was not tested on the semantic interpretation of “hello” or human syntax. Moreover, the signals were produced in air during a trained task. The experiment establishes vocal flexibility under those conditions while leaving underwater natural-language-like interpretation and population-wide performance untested.''', 'imitate2a',['imitation18'])
S('Acoustic comparisons constrain imitation judgments', '''Abramson and colleagues supplemented human judgments with comparisons of acoustic feature sequences. The analysis estimated how dissimilar a model and its proposed copy were after dynamic time alignment. **Dissimilarity** here measures differences in the extracted sound features, not a directly measured perceptual distance inside a whale’s nervous system.

Model–copy comparisons were assessed alongside mismatched sounds and repeated models. The copied sounds generally resembled their intended models more closely than unrelated sounds. Human judges who were unaware of the model’s identity also evaluated pairings, reducing dependence on the expectations of the trainers conducting the copying trials.

Some copies retained less detail than others, and the method’s result depends on the features selected for comparison. Agreement between acoustic analysis and independent judgments supports recognizable copying. It does not establish that the copies convey the same social information as the model or that the animal comprehends the meaning of a human utterance.''', 'imitate4',['imitation18'])
S('An innovation cue rewards behavioral novelty', '''Hill and colleagues trained killer whales to respond to an **innovation cue**, a signal requesting a behavior different from those already performed in that session. Familiar trained behaviors could be recombined or replaced by other responses. Reinforcement depended on avoiding repetition, so the preparation tested flexible selection rather than acquisition of a single new movement.

The investigators evaluated the number of responses before repetition, variation in behavioral categories and whether actions were combined in sequences or simultaneously. Whales produced diverse responses under the cue, with individual differences in fluency and complexity. Repeated sessions allowed performance to be evaluated beyond one isolated unusual action.

The result establishes flexibility within a trained and reinforced context. It is not a direct test of a whale inventing a novel wild hunting tactic or teaching it to companions. Age, prior experience and physical capacity also constrain available responses, so individual performance cannot be interpreted as a simple ranking of general intelligence.''', 'innovate2',['innovate22'])
S('Social contacts differ from simple association', '''**Association** means that individuals occur together with an opportunity to interact. **Interaction** requires a particular behavior between them. Weiss and colleagues used unoccupied aerial aircraft to observe southern resident whales, distinguishing simultaneous presence, synchronous surfacing and physical contact. Recognizable markings connected those actions to identified individuals.

The contact and surfacing networks differed from the association network. Age and sex shaped interaction patterns even when those characteristics did not detectably structure simple association. Females and younger individuals were more central in the contact network, meaning that they occupied more connected positions under that specific definition of a social relationship.

A broad measure of traveling together can therefore miss selective social behavior within an associated group. Aerial views improved access to contact that is difficult to observe from boats, but visibility and the selection of focal subgroups still limited sampling. These data establish patterned interactions; they do not identify the neural representation of social partners.''', 'social2',['social21'])
S('Diet boundaries need not isolate social networks', '''Jourdain and colleagues combined photo-identification, dietary information and genetic data from killer whales in Norway. **Genetic relatedness** estimates shared inherited variation, whereas an association index records how frequently identified animals occur together. Keeping these measures separate allowed diet-based categories to be evaluated alongside kinship and social connectivity.

Whales observed eating both fish and mammals were embedded in a larger network that included exclusive fish-eaters. Relatedness was an important correlate of social ties, and dietary difference did not produce complete social or genetic segregation. Flexible contact across groups therefore coexisted with individual variation in prey use.

The authors proposed that cultural diffusion could contribute to ecological breadth within this connected population. Network overlap supplies opportunities for information transfer, but it does not directly demonstrate the copying of a hunting tactic. These Norwegian results also cannot be assumed to describe the stronger ecotype boundaries documented in every northeastern-Pacific population.''', 'network3',['network24'])
S('Antarctic call repertoires vary with population context', '''Wellard and colleagues recorded Type C killer whales in McMurdo Sound and identified recurring call categories from their spectral and temporal organization. **Type C** designates an Antarctic form whose ecology differs from the seal-specialist pack-ice whales used in the wave-washing study. Population identity is therefore part of the experimental context, not an interchangeable label.

The acoustic study used hydrophone recordings and accompanying encounters with whales to classify calls, including multi-component and biphonic forms. The analysis linked particular sound categories with identifiable recording sessions rather than treating every Antarctic vocalization as one undifferentiated repertoire.

The observed category diversity establishes a repertoire for the sampled Type C recordings. Similar broad acoustic structures across ecotypes do not demonstrate shared call meaning or a common hunting tradition. Comparing populations requires attention to recorder characteristics, encounter conditions and categorization methods, as well as genuine differences in the animals’ sound production and behavioral use.''', 'typeC4',['repertoire20'])
S('Pack-ice hunters select particular seal prey', '''Pitman and Durban directly followed pack-ice killer whales hunting off the Antarctic Peninsula and compared observed seal kills with the seals available on ice floes. **Prey selectivity** means that consumption differs from availability; an abundant potential prey species need not be the species most often attacked successfully.

Weddell seals accounted for approximately 93% of identified seal kills despite comprising only approximately 15% of seals identified on floes. Crabeater seals were much more abundant in the observations but were not taken. Identifying both prey availability and the prey consumed constrained the explanation that the hunters simply encountered mostly Weddell seals.

This observational contrast establishes marked selectivity during the study. It does not experimentally separate prey handling difficulty, energetic reward and learned preferences as causes. The photographed approach to a floe documents a hunting encounter, while the population-specific prey pattern remains distinct from the broader marine-mammal diet of Monterey transient whales.''', 'wave3',['pitman12'])
S('Aligned swimmers generate coordinated waves', '''During **wave washing**, multiple killer whales swim in coordinated formation toward an ice floe, producing a wave that can wash over the surface and dislodge a seal. Pitman and Durban followed attack sequences directly, recording the animals’ approaches, the waves produced and the fate of the prey rather than inferring hunting from proximity to ice.

Whales sometimes submerged together beneath a floe and generated a wave as they approached or passed it. The photographed wave-producing event retained the relationship between the swimmers, water movement and seal position. The behavior couples collective movement with a physical disturbance of the prey’s refuge.

The observations establish spatially and temporally coordinated action with a common hunting outcome. They do not identify whether particular calls issued a command, whether every participant represented a shared plan or which neural pathway synchronized the swimming. Acoustic control of the formation remains a separate question from the directly observed movement coordination.''', 'wave2',['pitman12'])
S('Repeated waves can dislodge seals from ice', '''An ice floe protects a resting seal by separating it from underwater predators. Wave washing changes that physical relationship: water sweeping across the floe can move the seal into the sea. Pitman and Durban recorded repeated waves during attacks rather than treating the first wave as the complete hunting sequence.

The hunters produced approximately 4.1 waves per successful attack on average, with successful sequences ranging from one to ten waves. Repetition could be accompanied by changes in approach and prey position. Some seals regained the ice or avoided immediate capture, so dislodgment and final consumption were distinct observable events.

Successful hunting therefore depended on more than generating a wave once. The observed sequences are compatible with flexible adjustments to prey behavior and floe conditions, but the study did not experimentally manipulate those variables. It establishes repeated coordinated attacks; it does not prove that every adjustment was socially learned or communicated through a particular vocal signal.''', 'wave3',['pitman12'])
S('Attack duration constrains hunting interpretations', '''Pitman and Durban recorded both unsuccessful and successful attempts to remove Weddell seals from ice. Approximately 75% of the Weddell seals attacked during the observations were taken. **Capture success** refers to the final prey outcome, whereas a successful wave or temporary dislodgment can occur without an immediate kill.

Successful attacks lasted approximately 30.4 min on average and ranged from 15 to 62 min. These durations include repeated approaches and interactions with an active prey animal. The hunters’ coordinated behavior therefore operated across extended sequences, rather than being limited to one brief synchronized movement.

The observations constrain descriptions of the tactic as uniformly instantaneous or guaranteed. However, the study did not compare experimentally trained and untrained hunters or control prey motivation and floe geometry. Duration and success quantify natural attack outcomes while leaving the contributions of individual experience, group composition and specific communication signals incompletely resolved.''', 'wave2',['pitman12'])
S('Prey processing continues after capture', '''Pitman and Durban examined seal remains associated with a kill and described careful postmortem processing, including removal of selected tissue rather than indiscriminate swallowing of an intact carcass. **Prey handling** includes the actions after capture that make food accessible, as well as the movements used to seize the animal.

The evidence came from directly observed hunting and recovered remains, not an experimentally supplied carcass. It therefore connects natural wave-washing encounters with subsequent consumption. The anatomical condition of the remains supported the description of meticulous processing, while observation opportunities limited how completely the sequence could be reconstructed.

Coordinated capture and selective processing need not have identical learning mechanisms. The paper discussed the possibility of experience and social transmission, but observing adults handle prey does not establish deliberate teaching of younger whales. Demonstrating teaching would require evidence that a tutor changes behavior in a way that facilitates another animal’s acquisition of the skill.''', 'wave3',['pitman12'])
S('Canyon contours accompany prey-search routes', '''McInnes and colleagues followed transient killer-whale groups around Monterey Canyon and mapped their movements against bathymetry. **Bathymetry** describes the depth and shape of the seafloor. The continental shelf break and upper canyon slope supplied a spatial context for distinguishing searching, traveling and feeding during focal follows.

Groups often followed canyon contours while searching in open water. Recorded tracks connected routes with locations where prey were encountered or feeding occurred, rather than classifying every segment as an attack. Whales spent approximately 26% of observed time searching along the shelf break and upper slope and approximately 25% searching elsewhere in open water.

These tracks establish repeated use of particular habitat features during foraging. They do not determine whether whales followed remembered routes, detected current acoustic cues or used several sensory sources together. The study measured natural movement and behavioral context, leaving the underlying spatial-memory and sensory computations unrecorded.''', 'hunt6',['hunting24'])
S('Search occupies more time than prey pursuit', '''McInnes and colleagues classified activity during focal follows using observable behavioral criteria. **Searching** described movement while seeking prey; **pursuit** began when the whales actively chased an encountered animal; **feeding** followed successful prey capture. Separating these states prevented all time spent in a foraging area from being counted as direct predation.

Searching occupied approximately 51% of the observed activity, compared with approximately 10% pursuing prey and 23% feeding. The remaining time included traveling, socializing and resting. Search routes and feeding locations were retained in the spatial record, linking the time budget to particular encounters and habitat features.

A hunt therefore includes substantial information acquisition before attack and consumption. These proportions are observations from the sampled groups and conditions, not fixed species-wide constants. They also do not reveal which sensory channel supplied each prey detection, because the investigators did not experimentally remove hearing or vision during natural searches.''', 'hunt6d',['hunting24'])
S('Large prey recruit extended coordinated attacks', '''McInnes and colleagues documented transient killer whales attacking grey-whale calves accompanied by their mothers. A calf is not an isolated stationary target: maternal defense, prey movement and the surrounding group influence the attack. The recorded sequence retained identifiable interactions between hunters, mother and calf through pursuit and feeding.

Hunters coordinated approaches and physical contacts while attempting to separate or restrain the calf. Feeding followed successful attacks, but the presence of multiple whales near a mother–calf pair alone was not sufficient to classify an encounter as a kill. Sequential observations distinguished attack actions from the final outcome.

These natural records establish coordination against large, defended prey. They do not prove that participants held explicit complementary roles from the start or that a particular call directed each action. The observable tactic differs from ice-floe wave washing, even though both combine individual movements into a group hunting outcome.''', 'hunt9',['hunting24'])
S('Seasonal prey opportunities accompany whale occurrence', '''McInnes and colleagues compared seasonal transient-whale encounters with the availability of different marine-mammal prey around Monterey Canyon. **Phenology** describes the seasonal timing of biological events. Grey whales moving northward from breeding areas create a changing spring opportunity to encounter mothers and calves rather than a constant year-round prey distribution.

Transient-whale encounters increased during spring, and observations linked some attacks with the migrating grey-whale calves. The study also documented other prey, including sea lions, elephant seals and small cetaceans. Seasonal presence therefore reflected a broader predatory context rather than exclusive dependence on one prey species.

The temporal association supports the interpretation that prey opportunities contribute to predator occurrence. It does not establish prey availability as the only driver, because sighting effort, environmental conditions and movements outside the study area also matter. Observed seasonal patterns constrain ecological interpretations without identifying a single neural calendar or learned migration rule.''', 'hunt5',['hunting24'])
S('Observed coordination does not establish shared intent', '''McInnes and colleagues recorded different attack sequences against sea lions, harbor seals and small cetaceans. **Coordination** describes a relationship among observable actions in space and time; **shared intent** would require a stronger claim about what participants represent internally. Successful group predation does not make those terms equivalent.

Photographs and focal observations retained attacks on particular prey rather than combining all marine-mammal encounters into a generic cooperative tactic. The methods could establish who was present, how movements related to the prey and whether feeding occurred. They could not directly establish the internal goals or expectations of every participant.

Repeated group behavior provides opportunities for younger animals to observe experienced hunters, making social learning a plausible explanation for persistent tactics. The recorded hunts nevertheless lacked a controlled manipulation of learning opportunities. Cooperation, ecological specialization and cultural transmission are related hypotheses whose strongest evidence comes from different observations or experimental preparations.''', 'hunt8',['hunting24','pitman12'])
S('Playback links acoustic input with group movement', '''A **playback experiment** presents a controlled recording to test whether sound changes behavior. Selbmann and colleagues exposed tagged killer whales near an Icelandic herring spawning ground to long-finned pilot-whale sounds and control stimuli. **Multi-sensor tags** recorded movement, diving and acoustic activity, linking the stimulus interval with the whale’s subsequent actions.

Pilot-whale playback commonly elicited faster, more directed movement away from the sound source, accompanied by changes in group cohesion and alignment. Calling often increased initially and then decreased. Comparing these responses with noise controls constrained the explanation that any broadcast sound would produce the same movement.

The experiment establishes that acoustic information can alter individual and group behavior without a live pilot whale approaching. It does not identify the brain circuitry producing avoidance or prove that the listeners experienced a particular emotion. Interpretation as anticipated harassment or threat is supported by ecological context but remains distinct from the measured movement response.''', 'pilot1',['pilot26'])
S('Controls constrain acoustic-response explanations', '''Selbmann and colleagues evaluated horizontal movement, acoustic output and group organization before, during and after playback. Noise control recordings and a 1–2-kHz upsweep stimulus provided comparisons with pilot-whale sounds. **Group cohesion** concerns how closely individuals remain together, whereas **alignment** concerns similarity in their movement direction.

Responses to pilot-whale sounds included movement away from the source and more coordinated group organization. The upsweep control was used too sparingly for the same inferential treatment as the better-sampled noise comparison, so the authors distinguished descriptive observations from their principal analysis. Stimulus identity and available controls therefore shaped the strength of each conclusion.

Acoustically triggered alignment supplies direct evidence linking hearing with a group action, but it is an avoidance response rather than a hunt. It cannot establish that the same control mechanism organizes cooperative prey capture. The causal sensory manipulation and the observational hunting studies answer complementary questions about sound-guided social behavior.''', 'pilot5',['pilot26'])
assert len(slides)==44
key=['ford91','marino04','astro25','szymanski99','deecke00','imitation18','pitman12','hunting24','pilot26']
spec={'lecture':45,'theme':'rosewood-paper','content_slides':44,'title_height':3.2,'title_image':F['typeC4'],'title_refs':[R['repertoire20']],'slides':slides,'takeaways':{'cite':'; '.join(A[x] for x in key),'refs':[R[x] for x in key],'items':[
{'lead':'Anatomy and function differ.','text':'Killer-whale MRI establishes regional organization; it does not identify the synaptic circuit for dialect learning or hunting coordination.'},
{'lead':'Hearing is frequency dependent.','text':'Behavioral and brainstem audiograms reveal ultrasonic detection, but physiological thresholds exceed behavioral thresholds and depend on stimulus conditions.'},
{'lead':'Dialects are group traditions.','text':'Shared discrete calls define acoustic clans, while historical recordings establish repertoire persistence without directly isolating the learning mechanism.'},
{'lead':'Learning evidence has levels.','text':'Longitudinal call change permits maturation as an alternative; controlled copying of novel sounds directly supports vocal production learning.'},
{'lead':'Hunting involves coordinated action.','text':'Wave washing and large-prey attacks link group movements with capture outcomes, without proving deliberate teaching, shared intent or a specific call command.'},
{'lead':'Playback tests acoustic causation.','text':'Pilot-whale recordings alter movement and group organization; this avoidance result does not establish the mechanism coordinating prey capture.'}]}}
(D/'lecture.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n')
for i,x in enumerate(slides,2):
 words=len(re.sub(r'\*\*|_','', ' '.join(x['body'])).split());print(i,words,x['title'])
