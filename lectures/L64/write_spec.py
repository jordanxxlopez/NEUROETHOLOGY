"""Lecture 64: verified source-based teaching prose and original PDF crops."""
import json,re
from pathlib import Path
B=Path(__file__).resolve().parent
R=json.loads((B/'research.json').read_text());F=json.loads((B/'figure_sources.json').read_text());S=[]
def ref(k):return R[k]['reference']
def short(k):return ('Wilson & Alger' if k=='maternal' else R[k]['first_author']+' et al.')+' ('+str(R[k]['year'])+')'
def figure(n):
 x=F[n];k=x['paper'];return {'path':'figures/'+n+'.png','kind':'article','caption':short(k)+', Fig. '+x['figure']+'. '+x['description'],'source_url':'https://doi.org/'+R[k]['doi']}
def add(title,k,imgs,text,note):
 body=[p.strip() for p in text.strip().split('\n\n')];assert len(body)==3,title
 keys=list(dict.fromkeys([k]+[F[n]['paper'] for n in imgs]));sd={'title':title,'body':body,'transcript':[re.sub(r'\*\*|(?<!\w)_(?=\w)|(?<=\w)_(?!\w)','',p) for p in body]+[note],'refs':[ref(x) for x in keys],'cite':'; '.join(short(x) for x in keys),'figure_width':5.8}
 if len(imgs)==1:sd.update(layout='figure-right',figure=figure(imgs[0]))
 else:sd.update(layout='figures-right',figures=[figure(n) for n in imgs],primary_figure_height=2.05)
 if len(imgs)==2 and imgs[1] in ['cook_anatomy','eeg_histology']:sd.update(figure_arrangement='side-by-side',primary_figure_width=3.5)
 S.append(sd)

add('Cold-stunning disrupts endocrine and behavioral recovery','cold',['cold_hormones'],'''
**Cold-stunning** is a life-threatening loss of normal function during prolonged exposure to cold water. Juvenile Kemp’s ridley turtles stranded on Cape Cod entered rehabilitation with disturbed hormone concentrations and, in some cases, persistent deficits in feeding and growth.

**Corticosterone** is a glucocorticoid, a steroid hormone involved in the physiological response to stress. **Thyroxine** is a hormone associated with metabolic regulation. Hunt and colleagues repeatedly measured both in blood during rehabilitation, linking their trajectories to feeding, activity, body mass, and survival.

Corticosterone generally declined while thyroxine increased during recovery. In most turtles, concentrations approached the recovered range by about day 18. A smaller group retained high corticosterone and low thyroxine, separating rapid endocrine recovery from a prolonged physiological disturbance within the same rehabilitation setting.
''','Cold exposure was the presenting condition, and the study followed animals prospectively through care. The hormonal trajectories were compared with clinical and behavioral outcomes rather than assumed to be equivalent to recovery. A decline in a stress-associated hormone and restoration of a metabolic hormone occurred together in most surviving animals.')
add('Persistent stress hormones predict later mortality','cold',['cold_survival'],'''
The physiological state of a turtle several weeks after admission was more informative than the initial emergency response alone. Elevated corticosterone on day 18 was associated with subsequent mortality, after the first phase of rehabilitation had already passed.

The fitted relationship placed the highest survival probability below approximately 9.2 ng/mL of corticosterone. Above that concentration, predicted survival declined sharply. This value describes the relationship in the studied cold-stunned turtles, rather than a universal release threshold for reptiles.

Persistently elevated corticosterone accompanied low thyroxine in the poorly recovering group. The combination links continued stress physiology with an impaired metabolic recovery trajectory. Serial sampling distinguishes a transient response to stranding from sustained disturbance during care, even when animals have survived their first days in rehabilitation.
''','The fitted curve uses day-18 concentrations to predict later survival. The concentration is expressed in nanograms per milliliter of plasma. The study’s relationship is specific to the species, presenting condition, and rehabilitation population; release decisions still require clinical and behavioral assessment.')
add('Endocrine recovery accompanies feeding and mass gain','cold',['cold_growth_hormones'],'''
Turtles with higher corticosterone on day 18 subsequently gained less body mass. Higher thyroxine was associated with greater mass gain between days 7 and 60, connecting the endocrine trajectory to a sustained biological outcome rather than to one day’s appearance.

Food intake also differed with hormone state. Turtles that had not eaten during the preceding week had markedly higher corticosterone than turtles that ate daily. Higher thyroxine was associated with more consistent feeding, linking metabolic recovery with the behavior supplying energy for growth.

Growth changes the condition in which a juvenile returns to the sea. The authors proposed that reduced growth could increase vulnerability after release because smaller turtles may face greater predation risk. The directly measured outcomes were hormone concentrations, feeding, and mass gain during rehabilitation.
''','The predation link is the authors’ hypothesis about a later ecological consequence, not a post-release outcome measured in this endocrine study. The measured feeding history covered the week before the day-18 sample. Body-mass gain integrates food intake and physiological recovery over a longer interval.')
add('Individual growth trajectories reveal delayed recovery','cold',['cold_growth'],'''
**Growth trajectory** means the pattern of body-mass change through time. The study included a turtle that gained mass steadily, another that initially failed to gain mass for about two months before recovering, and a third that remained near its admission mass before dying.

These patterns separate immediate progress, delayed progress, and persistent failure to recover. A single mass measurement could place turtles with very different histories at a similar value. Repeated measurements identify whether condition is improving, stable, or deteriorating during treatment.

The delayed-growing survivor eventually increased its mass, whereas the persistently impaired animal never developed a sustained growth trajectory. Hormone measurements and longitudinal growth therefore describe different aspects of the same recovery process: current physiological state and the accumulated consequences for body condition.
''','Mass was expressed relative to each turtle’s own admission mass, allowing individual trajectories to be compared despite different starting sizes. The examples are individual clinical histories, not separate experimental treatments. The endocrine associations were evaluated across the broader cohort.')
add('Fecal hormone assays require species-specific validation','possum',['possum_assays','possum_challenge'],'''
**Fecal glucocorticoid metabolites** are breakdown products of glucocorticoid hormones excreted in feces. They provide a way to monitor physiological stress without repeatedly capturing an animal for blood sampling. Cope and colleagues tested this approach in common brushtail possums undergoing rehabilitation.

An **enzyme immunoassay** uses antibody binding to quantify compounds in an extracted sample. Different assays recognize different hormones or metabolite groups. The investigators compared several assays after an **ACTH challenge**, administration of adrenocorticotrophin hormone to stimulate glucocorticoid secretion.

The 72a assay produced the greatest change following the challenge and was selected for rehabilitation monitoring. Assay choice determined how clearly the induced response was detected, because an antibody’s recognition of possum metabolites differed from recognition of the original circulating hormone.
''','ACTH stimulation supplies a biological validation: an assay should detect the expected increase after hormone secretion is deliberately stimulated. Fecal material contains metabolized compounds, so an assay that performs well with a blood hormone is not automatically suitable for fecal samples. The challenge comparison preceded monitoring of animals in rehabilitation.')
add('Fecal signals lag behind the event that triggers them','possum',['possum_challenge'],'''
Hormone secretion and fecal excretion occur at different times. A stress-associated signal must pass through metabolism and intestinal transit before it appears in a collected fecal sample. The ACTH challenge allowed the investigators to measure that delay in brushtail possums.

Across assays and individuals, the first rise above baseline appeared about 7–55.5 hours after administration. The selected assay’s response also varied among individuals, so collection time and the time of the triggering event were not interchangeable.

A fecal peak can therefore correspond to an earlier episode of handling, relocation, or treatment. Event logs and repeated samples place the signal within its biological time course. Sampling over several days captures a response that an immediately collected fecal sample may precede entirely.
''','The 7–55.5 hour interval is the reported range for the first rise across the validation assays, not a fixed lag for every sample measured with 72a. Metabolic processing and gut passage contribute to the separation between secretion and excretion. Peak timing also depends on which metabolites an assay recognizes.')
add('Possums differ in baseline and response during care','possum',['possum_events'],'''
Rehabilitating possums differed substantially in their baseline fecal hormone concentrations. **Baseline** refers to the individual’s reference level used to distinguish ordinary variation from an elevated episode. Comparing each animal with its own pattern avoids treating a naturally high value as an identical state across all animals.

Rehabilitators recorded events such as handling, a new cage, medication, separation, and the arrival of another possum. Hormone peaks sometimes followed these events, but event category did not reliably predict whether a peak occurred. A peak within five days followed roughly half of the recorded events.

The repeated trajectories combine individual physiology with the timing of care. They support monitoring changes within an animal while also recording behavioral and clinical context. A quiet animal and an animal with elevated metabolites can require different interpretation depending on their previous pattern and recent treatment history.
''','The study measured responses during rehabilitation and did not validate a fecal concentration as a post-release survival threshold. Baselines varied with individual histories and circumstances. The event records supplied context, but a recorded event was not a reliable one-to-one explanation for every hormonal peak.')
add('Transport adds a new stress response before release','pool',['pool_cort'],'''
Rehabilitated Kemp’s ridley turtles were transported by road from Massachusetts to Georgia for release into suitable water temperatures. Even after treatment had restored good clinical condition, the out-of-water journey increased corticosterone, producing a new physiological challenge immediately before release.

Blood was collected before transport, immediately afterward, and after either 6 or 24 hours in unfamiliar saltwater pools. The repeated measurements compared each turtle’s post-journey state with its own pre-transport state and its subsequent recovery in water.

Corticosterone declined toward baseline during pool recovery, although it remained elevated relative to the initial sample. A brief period in water therefore changed the physiological state in which turtles entered the sea. Rehabilitation recovery and transport recovery occurred at different stages of the release process.
''','The turtles were clinically suitable for transport, so the measured response concerned the journey rather than their initial stranding emergency. All animals experienced transport and then pool recovery; the study lacked a transport group released immediately without a pool. The repeated samples nevertheless directly document a partial hormonal recovery over time.')
add('Metabolic and ionic measures recover at different rates','pool',['pool_glucose','pool_potassium'],'''
**Glucose** is a circulating fuel used by tissues, and **potassium** is an ion whose concentration contributes to physiological function. Transport increased blood glucose and slightly reduced potassium in the rehabilitated turtles. Both measures returned to their pre-transport levels after pool recovery.

Recovery after at least 6 hours was sufficient for these changes. Extending the pool period to 24 hours did not produce a marked additional improvement across the measured physiological profile. The results distinguish the time needed for observed recovery from the assumption that a longer holding period always adds benefit.

Corticosterone was still only partly recovered while glucose and potassium had normalized. Different measurements therefore captured different recovery time courses. Returning one blood variable to baseline did not mean that every component of the transport response had resolved at the same moment.
''','Potassium here is a measured circulating ion, not a direct recording of neuronal ion-channel activity. The two recovery intervals were approximately six and twenty-four hours. The physiological results concern recovery before release; the study did not compare later survival of the two groups.')
add('Immune changes outlast the transport response','pool',['pool_immune'],'''
**White blood cells**, or leukocytes, participate in immune responses. A **heterophil-to-lymphocyte ratio** compares two leukocyte types and can change with physiological stress. Hunt and colleagues measured both alongside corticosterone and glucose during transport and pool recovery.

Total white-cell counts and the heterophil-to-lymphocyte ratio increased during the journey. These immune measures remained elevated after pool recovery, even as glucose returned to baseline and corticosterone declined. The response thus extended beyond a single stress-hormone measurement.

Release preparation involves a physiological transition with several time scales. The pool period restored some variables more rapidly than others, leaving an altered immune-cell profile in otherwise clinically stable turtles. Parallel measurement of hormonal, metabolic, and immune variables describes this transition more completely than any one variable alone.
''','A ratio can increase through changes in either cell population, so it is interpreted as a combined leukocyte profile. The study did not establish that the residual immune changes caused poor release outcomes. The measured fact is their persistence after the recovery period used before release.')
add('Paired orphan seal pups retain early social behavior','maternal',['seal_pair','seal_contacts'],'''
Newborn harbor seal pups normally spend their first weeks near their mothers. Wilson and Alger maintained orphan pups in pairs with access to water and dry resting areas, then recorded behavior during rehabilitation and compared it with wild mother–pup behavior.

An **ethogram** is a defined set of behaviors used to classify observations consistently. The study recorded resting, body contact, following, nosing, play, and suckling. Paired pups remained within 1 m of one another almost continuously across dry, edge, and aquatic zones.

Body contact was especially frequent on land, while close following and interaction occurred in water. The pups directed species-typical early social behavior toward their companions, providing reciprocal contact after maternal loss. Social opportunity was therefore part of the environment in which development continued during care.
''','The paired pups were compared with previously recorded wild mother–pup pairs, rather than randomly allocated to paired and isolated rehabilitation treatments. The direct finding is that paired orphans expressed the defined early social repertoire toward each other. Partner contact was maintained across several physical zones.')
add('Water use increases as orphan pups develop','maternal',['seal_water','seal_follow'],'''
The paired seal pups entered water every day, including during their first weeks in rehabilitation. Time in water increased after about 2.5 weeks of age, while resting periods on land continued between aquatic sessions. Free access allowed the pups to choose between these environments.

During the first 16 days, water use occupied up to about 15% of the day; later it reached about 43%. Early sessions were usually relatively short, whereas older pups could remain in water for several hours. The change followed development rather than a single imposed swimming schedule.

Partners often oriented toward and followed one another when entering or leaving the water. The shared environment linked social behavior with aquatic experience, while the haul-out area preserved a dry resting option. Both opportunities were available as the pups’ daily activity pattern changed.
''','Haul-out means leaving water to rest on a dry surface. The daily percentages summarize the observed early and later rehabilitation periods. The study provided choice of water access, rather than forcing pups to remain immersed for a fixed duration.')
add('Nosing and aquatic play replace lost contact opportunities','maternal',['seal_play','seal_behaviors'],'''
**Nosing** is contact directed with the nose toward a partner’s face or body. Orphan pups exchanged these contacts on land, at the water’s edge, and underwater. The body locations contacted differed across zones, linking contact behavior to resting, following, and aquatic interaction.

Play was concentrated in water and often involved paired circling, somersaulting, and changes in body orientation. Bouts commonly lasted about five minutes. When deeper baths were available alongside shallower pools, paired play occupied substantially more time in the baths.

The physical environment changed the movements available during interaction. Deeper water permitted three-dimensional maneuvering, whereas shallow pools constrained it. Partner availability and enclosure geometry jointly shaped the repertoire expressed during rehabilitation, extending social care beyond the mere presence of another animal.
''','The authors classified play from the observed exaggerated and interactive movements. Depth affected the form of maneuvering available, not simply whether a second pup was present. The behavioral observations concern opportunities during care; they were not linked to post-release survival in this study.')
add('Growth and social recovery provide different measures','maternal',['seal_growth','seal_comparison'],'''
The paired orphan pups gained body mass steadily through rehabilitation, at about 0.285 kg per day. Their growth pattern was similar to that of previously rehabilitated pups, while the behavioral recordings documented close contact and a developing aquatic repertoire.

Compared with wild pups interacting with mothers, the orphan pairs spent relatively more time in body contact, nosing, and aquatic play. The substitute relationship therefore expressed the same broad behavior classes with a different distribution of activity across environments.

Body growth describes nutritional and physical progress, while social interaction describes opportunities for species-typical development. These outcomes coexist during rehabilitation. A satisfactory growth trajectory can be assessed alongside contact, following, and play, rather than used as a complete description of an orphan pup’s recovery.
''','The historical growth comparison and the wild behavioral comparison addressed different outcomes. Maternal absence changes the social relationship, so paired orphans are not assumed to reproduce every feature of maternal care. The direct observations show continued growth and expression of early social behaviors in the paired setting.')
add('A predictive feeding cue recruits anticipatory behavior','anticipate',['enrichment_exposure'],'''
**Anticipatory behavior** occurs before an expected rewarding event. Chudeau and colleagues studied it in rehabilitating harbor seal pups that could independently retrieve fish. A one-minute water-spray cue preceded feeding, separating the predicted reward from other routine staff activity.

Feeding occurred at scheduled times, while cameras recorded behavior before and after fish delivery. The investigators identified behaviors associated with the pre-feeding period, then measured their occurrence and duration during rehabilitation. The cue created a repeatable relationship between a sensory event and food availability.

Individual pups expressed anticipation differently, including repeated behaviors in some animals and longer bouts in others. Learned prediction therefore changed behavior before the reward arrived. Counting events and measuring time captured distinct features of this response within an environment containing frequent human care activity.
''','The spray was used as an unambiguous cue because staff also entered enclosures for cleaning and treatment. Free-feeding pups were assessed after they could retrieve dispersed fish independently. Anticipation was quantified from defined behaviors rather than inferred from any movement occurring near feeding time.')
add('Structural and cognitive enrichment offer different tasks','anticipate',['structural','cognitive'],'''
**Environmental enrichment** provides opportunities for behavior beyond basic feeding and shelter. Structural enrichment changes the objects or physical features available, while cognitive enrichment adds a problem that must be solved to obtain a reward. The seal study offered both during daily sessions.

Structural devices included floating objects, artificial kelp, and resting structures. Cognitive devices placed fish inside containers or behind barriers, requiring the seal to manipulate or investigate the device before accessing food. Both types were designed for repeated use in rehabilitation enclosures.

The distinction concerns what the animal does, rather than whether an object is present. A structure can support exploration or resting; a food puzzle introduces an action–reward contingency. Comparing these opportunities separates physical complexity from a task that changes how a seal obtains a valued resource.
''','An action–reward contingency means that access to a reward depends on a particular behavior. These devices were published figures in the study, and their visual appearance is retained without reconstruction. The paper describes both animal safety and cleaning as constraints on enrichment used in a clinical rehabilitation setting.')
add('Enrichment engagement differs from reward anticipation','anticipate',['enrichment_interaction','anticipatory_count'],'''
The pups interacted with both enrichment types for similar proportions of recorded time. The amount of interaction did not reliably predict either the rate of anticipatory events or the average duration of anticipatory bouts. Engagement with a device and anticipation of feeding were separate measured behaviors.

**Count rate** describes how often a defined behavior occurs during observation. A pup making frequent brief movements can have a high count rate without spending much total time in anticipation. Another pup can produce fewer events that last longer.

Enrichment exposure also varied across individuals during rehabilitation. Recording both exposure and actual interaction distinguished what was offered from what each animal used. Behavioral assessment therefore followed the animal’s response to an opportunity rather than equating device provision with a uniform experience.
''','The study measured exposure, interaction, count rate, and duration as separate variables. Similar interaction with structural and cognitive devices did not mean that the devices required identical behavior. Individual differences in the form of anticipation contributed to differences between the frequency and duration measures.')
add('Cognitive enrichment may shorten anticipatory bouts','anticipate',['anticipatory_duration'],'''
Pups exposed predominantly to cognitive enrichment tended to have shorter anticipatory bouts than pups exposed predominantly to structural enrichment. The relationship was a tentative trend in this study, so it supports a hypothesis about welfare rather than a settled treatment effect.

The proposed explanation is that additional opportunities to obtain rewards reduce dependence on a narrow set of predictable feeding events. Under this hypothesis, anticipation becomes less prolonged when rewarding activity is available through problem-solving as well as scheduled meals.

Anticipatory event frequency did not follow the same pattern as bout duration. The measured behavioral change concerned how long anticipation persisted, not a general suppression of activity. Repeated assessment of both dimensions can distinguish altered reward expectation from a simple reduction in movement during care.
''','The study’s enrichment-dose result was tentative and sensitive to the model specification, which limits a causal welfare claim. The explanation involving additional rewarding opportunities is explicitly a hypothesis. These pups were not followed after release to test whether a shorter anticipatory bout predicted survival.')
add('Tactile enrichment changes a rescued turtle’s activity','enrich',['turtle_sensory'],'''
An olive ridley turtle undergoing rehabilitation received tactile and structural enrichment in a case described by Escobedo-Bonilla and colleagues. Scratchers, a shelter, and a waterfall supplied different opportunities for contact, refuge use, and movement within the tank.

**Tactile stimulation** is sensory input produced through physical contact. The scratchers allowed the turtle to contact surfaces without staff handling, while the shelter supplied an alternative location within the enclosure. Each device was offered for several days and the turtle’s interaction was recorded.

The program was associated with increased swimming and reduced resting relative to the earlier behavior record. These observations describe a change in activity during care. The turtle had not yet been released when the case was reported, so the measured outcome was captive behavioral engagement rather than survival in the wild.
''','This source is a review that includes an original illustrative rehabilitation case, rather than a controlled primary enrichment trial. The deck treats the case descriptively. The article’s reported behavior changes concern one turtle’s care program and are not presented as a general effect size for sea turtle rehabilitation.')
add('Food-access enrichment recruits foraging movements','enrich',['turtle_feeding'],'''
**Foraging** includes searching for and obtaining food, rather than consuming a readily available ration alone. The olive ridley case used a vegetable feeder, a food-containing jar, and an ice block with food to make access depend on manipulation or investigation.

The ice block required the turtle to interact with the food-containing material before obtaining the ration. Other feeders changed the location and accessibility of food. The devices therefore altered the actions preceding ingestion while continuing to provide nutritional resources during rehabilitation.

Interaction differed among devices, with strong engagement reported for the food-containing ice block. Swimming increased and resting decreased across the broader enrichment program. These observations connect food delivery to an expanded behavioral repertoire, while retaining the distinction between behavior recorded in a tank and competence measured after release.
''','The case used several enrichment types together, so the overall activity changes cannot be attributed exclusively to one feeder. The paper reports interaction categories as well as changes in the activity record. No graph has been recreated from those reported values; the images are the original published device photographs.')
add('Hippocampal injury predicts spatial-memory deficits','cook',['cook_anatomy','eeg_histology'],'''
**Domoic acid** is an algal neurotoxin associated with seizures and brain injury in California sea lions. The **hippocampus** is a brain structure involved in spatial memory, the retention of information about locations. Cook and colleagues studied stranded animals during veterinary care and rehabilitation.

Magnetic resonance imaging, or **MRI**, measured hippocampal anatomy in living animals. Investigators traced the structure and expressed its volume relative to total brain volume. They compared left and right sides and the dorsal and ventral portions along its length.

Smaller right hippocampal volumes were associated with poorer performance in spatial-memory tasks. The association connected a measurable neural injury with behavior needed to revisit food locations. Structural assessment therefore addressed a functional problem that could persist after an animal’s immediate clinical condition improved.
''','The histology comes from Williams and colleagues and provides the sea lion tissue comparison; Cook and colleagues supplied the behavioral and imaging association. MRI measures living anatomy, whereas histology examines tissue after death. The hippocampal tracing preserved the anatomical boundaries used to quantify volume.')
add('A seven-second delay exposes impaired spatial alternation','cook',['cook_memory','cook_anatomy'],'''
**Delayed alternation** requires choosing the opposite location from the preceding choice after a waiting period. The sea lions first learned to alternate between left and right routes in a two-choice maze. Investigators then introduced a 7 s delay before the next choice.

No-delay trials provided a comparison for performance without the added retention interval. Animals with smaller right hippocampal volumes made more errors during delayed trials, even when no-delay performance was considered. The dorsal right portion was especially associated with successful delayed alternation.

The task required retention of a recent navigational episode rather than simply approaching visible food. Separating delay from no-delay performance reduced the influence of general task proficiency on the memory comparison. The behavioral deficit therefore appeared when the previous choice had to guide a later action.
''','The animals were trained to a common free-running alternation criterion before delayed testing. The source apparatus is documented in the supplement, and the graph associates memory performance with structural measurements. The image of hippocampal anatomy identifies the region discussed on this slide.')
add('Remembering recent searches reduces repeated errors','cook',['cook_foraging','cook_anatomy'],'''
The spatial foraging task presented four identical opaque buckets once every 24 hours. A fixed location contained fish for each animal, while the other locations did not. Opaque containers prevented direct visual inspection of their contents from guiding the initial search.

A **within-session error** was a return to a location already visited during that search. Animals with smaller right hippocampal volumes made more of these repeated visits. Remembering which locations had just been inspected reduced redundant search behavior within an episode.

The task combined a stable rewarded location with the need to track recent choices. Its within-session measure addressed immediate search memory, while changes across days addressed learning of the persistent food location. These two time scales separated remembering a current search from retaining a location between foraging opportunities.
''','All buckets were identical and one location remained rewarded for a given animal. The figure is the paper’s published apparatus depiction, cropped from its supplement. The deck has not drawn a new diagram. Repeated-location errors were recorded separately from the latency to find the reward.')
add('Learning a fixed food location involves regional differences','cook',['cook_learning','cook_anatomy'],'''
**Acquisition rate** describes how quickly performance improves while an animal learns a task. Sea lions generally found the rewarded bucket faster across repeated testing days. The decrease in latency measured learning of a location that remained consistent between daily sessions.

Whole-hippocampus volume did not predict this learning rate. Separating the right hippocampus into dorsal and ventral portions revealed opposite associations: larger dorsal volume was associated with faster acquisition, while larger ventral volume was associated with slower acquisition in the regional analysis.

The regional result differs from the simpler relationship between whole right hippocampal volume and repeated-search errors. A brain structure can contribute differently to distinct behavioral measures, and combining its subdivisions can obscure those relationships. The daily task therefore separated immediate search accuracy from acquisition over repeated days.
''','The opposite regional associations are correlations in a clinical population, not the result of experimentally removing either subdivision. The reported learning curve summarizes performance across days, and the regional insets relate individual acquisition rates to anatomy. The inference concerns the importance of retaining regional and behavioral specificity.')
add('Hippocampal injury disrupts the memory network','cook',['cook_network','cook_thalamus'],'''
The **thalamus** is a group of deep brain nuclei involved in communication among brain systems. Cook and colleagues examined its relationship with the hippocampus using **functional connectivity**, similarity in the time courses of brain signals measured during functional MRI.

Animals with hippocampal lesions had reduced hippocampal–thalamic connectivity compared with animals lacking evident neurological abnormalities. The reductions involved both sides of the network, even though behavioral associations with hippocampal volume were strongest on the right.

Local tissue injury was therefore accompanied by an altered relationship between brain regions. The authors proposed that impaired memory and network function could interfere with flexible foraging and navigation after release. The measured neural outcomes were anatomical damage and altered connectivity; the proposed ecological consequence concerned finding food in the wild.
''','Functional connectivity is a relationship between recorded signal time courses, not a direct measure of axonal connections or synaptic strength. The control animals were assessed clinically and radiologically. The anatomical thalamic tracing and the original network figure both come from the same study and supplement.')
add('Scalp recordings detect neural abnormalities','eeg',['eeg_electrodes'],'''
**Electroencephalography**, or EEG, records voltage differences from electrodes placed on the scalp. Williams and colleagues used it in stranded California sea lions with suspected domoic acid toxicosis and in animals presenting for other clinical problems.

A **montage** is the arrangement of electrode pairs used to display voltage differences. The investigators adapted electrode placement to sea lion head anatomy and compared recordings across the resulting channels. Sedation facilitated placement and recording, while the drug state was documented for interpretation.

Normal recordings contained background rhythms and state-dependent transient events. Establishing these patterns allowed abnormal activity to be distinguished from ordinary variation during sedation and recovery. The recording preparation supplied a measure of current neural activity alongside the anatomical assessment used in rehabilitation.
''','EEG channels represent voltage differences between electrode sites rather than independent recordings from specific deep brain nuclei. Sedatives and anesthetics affect background activity, so the normal comparison must retain the recording state. The electrode figure documents the actual clinical preparation used in the study.')
add('Electrical seizures can occur without convulsions','eeg',['eeg_seizure','eeg_histology'],'''
Domoic acid preferentially binds **kainate receptors**, a subtype of receptor for **glutamate**, an excitatory neurotransmitter. Binding at sites before and after a synaptic junction raises calcium concentrations inside cells. Excessive excitation can cause **excitotoxicity**, neuronal injury associated with cell loss and altered hippocampal tissue.

An **epileptiform discharge** is an abnormal electrical event with features associated with seizure disorders. The sea lion recordings contained spikes, sharp waves, and complexes combining faster events with slower waves. Abnormal events could be widespread or concentrated over one side.

Some animals had **electrographic seizures**, sustained seizure-like electrical activity detected in EEG, without an observed clinical seizure during recording. An absence of overt convulsions therefore did not mean normal neural activity. Electrical recordings and hippocampal tissue measurements address current activity and persistent injury, respectively.
''','The paper discusses domoic acid acting through glutamate receptors as the context for excessive excitation; it did not record individual receptor currents. The histological panel preserves the scale bars and original tissue comparison. The direct clinical observation is that abnormal EEG activity may occur without visible seizure behavior during the recording.')
add('Repeated EEG records changing neural function','eeg',['eeg_recovery','eeg_histology'],'''
A repeated EEG can track whether an animal’s neural activity changes during rehabilitation. The study included recordings from the same sea lion at different times, with substantial changes in abnormal discharges. Electrical state was therefore evaluated longitudinally rather than assigned from one observation.

Some animals had normal or improved recordings despite abnormal earlier activity. Medication and recording state also affected EEG patterns, so these factors were retained in the clinical history. The time of assessment influenced the measured relationship between neurological signs and electrical activity.

A changing EEG and a persistent anatomical lesion describe different components of recovery. Electrical abnormalities can fluctuate while tissue loss remains. Combining behavioral assessment, imaging, and repeated recording distinguishes current neural state from structural damage relevant to learning and navigation outside the rehabilitation enclosure.
''','The source figure presents improvement in one individual between recordings. This is a clinical longitudinal example, not a randomized treatment comparison. Structural histology is supplied as a separate anatomical comparison and is not presented as tissue from that same repeatedly recorded animal.')
add('Boldness predicts survival in released ringtail possums','bold',['bold_personality'],'''
**Boldness** describes an individual’s tendency to approach or engage with unfamiliar conditions rather than withdraw. Corsetti and colleagues assessed behavior in captive-raised western ringtail possums and then monitored the animals after release using radio collars.

After three months, reported survival was higher for bold than for shy individuals, approximately 53% versus 41%. A trait measured before release was therefore associated with an ecological outcome after the animals encountered a natural environment.

The authors proposed that bold animals could explore resources more effectively under these release conditions. That explanation is a hypothesis about how personality influences adaptation. The observed association makes behavioral variation relevant to rehabilitation, because animals in similar physical condition can differ in how they respond to unfamiliar surroundings.
''','The study evaluated personality before release and followed survival afterward, rather than inferring wild success from behavior in care alone. Boldness was derived from the behavioral assessment, not from a subjective impression of friendliness. The proposed resource-exploration mechanism was not experimentally isolated.')
add('Behavioral assessment distinguishes several responses','bold',['bold_personality','bold_release'],'''
Before release, possums underwent a behavioral assessment in an unfamiliar testing environment. The investigators recorded several responses and combined their variation into a personality measure. Bold and shy categories therefore reflected patterns of behavior rather than one isolated movement.

The same animals were later monitored with radio collars, linking pre-release observations to subsequent survival. Tracking located living animals and helped determine causes of mortality. The behavior–outcome comparison was made across the release period rather than within the testing enclosure.

The release environment contained introduced foxes, and fox predation accounted for much of the mortality. Personality was therefore expressed within a particular risk landscape. The observed advantage of boldness belongs to those conditions, where successful adjustment involved both finding resources and surviving predator encounters.
''','The assessment and the release stage measured different outcomes. The study tested additional management variables across releases, so release history is part of the context for the personality result. A behavioral score is not treated as a species-independent certificate of release readiness.')
add('Sex and predator management also influence survival','bold',['bold_sex','bold_release'],'''
Survival after release differed with sex as well as personality. Females had higher survival than males in the study, while variation among release events also reflected different management conditions. The outcome was shaped by several animal and environmental characteristics together.

Introduced red foxes caused most of the identified deaths. Fox control by shooting was associated with better possum survival than baiting under the studied conditions. Managing the threat around the release site therefore changed the environment in which behavioral competence had to operate.

A pre-release behavior measure and a release-site intervention address different parts of the survival problem. One concerns how an individual responds; the other concerns the frequency or severity of the external threat. The study connected both to tracked outcomes in the same conservation program.
''','The management comparison occurred across releases and was not a randomized head-to-head fox-control trial. The study’s survival pattern supports predator management as part of reintroduction planning. Sex-related differences were reported without establishing one specific physiological or behavioral mechanism.')
add('Release conditions determine the meaning of a trait','bold',['bold_release','bold_personality'],'''
The ringtail possum study compared personality with survival across release events that differed in management history. Some releases also incorporated predator-awareness training. The same broad behavioral category was therefore evaluated within changing ecological and husbandry conditions.

Boldness can influence approach to unfamiliar surroundings, while predator exposure determines the consequences of that approach. The authors linked the observed survival advantage to the possibility that exploratory animals adapted more effectively to available resources. This remains a hypothesis about the observed association.

Readiness for release includes a relationship between an animal and its destination. The tracked survival data connect pre-release behavior with a setting containing fox predation, habitat differences, and management interventions. Behavioral assessment gains ecological meaning when its outcomes are followed in the environment where the animal must live.
''','The observational association is not a recommendation to select only bold animals across taxa. The study’s destination and predator landscape are integral to interpreting the result. The plotted release comparison includes management differences, so it is not presented as a pure effect of personality alone.')
add('Predator training pairs fox cues with an aversive event','predator',['predator_map'],'''
**Predator-awareness training** exposes an animal to cues associated with danger before it encounters a living predator. Corsetti and colleagues trained captive-raised western ringtail possums using a taxidermic fox, fox urine, and loud noises intended to frighten the possum.

The training paired visual and odor cues with an aversive event across three sessions. In the third session, the fox was moved on wheels, adding movement to the cue combination. Possums without training formed the comparison group before release at the same national park.

**Associative learning** changes responses when events occur together predictably. The training hypothesis was that fox-associated cues would later recruit protective behavior in the wild. The protocol therefore connected sensory recognition with a consequence before testing the animals’ survival after release.
''','The protocol used a taxidermic predator rather than exposing possums to an uncontrolled live attack. Training combined several cues, so it did not isolate vision, odor, or sound as the sole learned signal. The direct post-release comparison concerned trained and untrained groups.')
add('Training is tested by survival outside the enclosure','predator',['predator_survival'],'''
Trained and untrained possums were released into Yalgorup National Park and followed by radio tracking for three months. Monitoring after release tested whether the pre-release intervention was associated with survival under natural exposure to threats and resources.

Approximately 77% of trained possums remained alive after three months, compared with 25% of untrained possums. Confirmed fox predation occurred in the untrained group. The survival difference connected the rehabilitation intervention to an outcome beyond recognition or avoidance inside the training enclosure.

The result supports predator-awareness training as a contributor to this release program. The proposed behavioral pathway is learned avoidance of fox-associated danger. Radio tracking supplied the ecological endpoint, while the training design specified the cue–consequence relationship that could alter behavior before a dangerous encounter.
''','The reported percentages correspond to the analyzed animals after exclusions described in the paper. The study directly followed survival, but it did not record every predator encounter or identify the exact protective movement used. The deck distinguishes the survival finding from the proposed learned-avoidance mechanism.')
add('The early release period carries substantial risk','predator',['predator_hazard'],'''
**Hazard** refers to the risk of an event among individuals still surviving at a given time. The paper also plotted cumulative hazard, which accumulates this risk across the release period. Untrained possums experienced a steeper accumulation than trained animals.

The divergence developed during the three-month tracking period, when newly released animals were adapting to a wild environment. The survival and hazard presentations describe the same underlying outcome from different perspectives: how many animals remain alive and how risk accumulates over time.

Training was completed before that early exposure period. Its practical role was to change behavior before threats could cause irreversible mortality. The timing links sensory learning during care with the phase in which unfamiliar predators and habitat demands immediately affect released animals.
''','Cumulative hazard is a published analytical representation of the observed survival data, not a new graph drawn for this lecture. Its values are not an independent physiological measure. The plotted difference concerns the timing of mortality in the tracked trained and untrained groups.')
add('Learning and predator control address different risks','predator',['predator_survival','bold_release'],'''
Predator-awareness training changes the released animal’s prior experience of threat cues. Predator control changes the abundance or activity of the threat around the release site. The ringtail possum studies evaluated these approaches through post-release survival rather than treating them as interchangeable interventions.

The training study found higher survival in animals exposed to fox cues before release. The broader reintroduction study also associated fox-control strategy with survival. Behavioral preparation and environmental management therefore addressed different components of the same predation problem.

A learned response can influence an encounter, while reduced predator pressure changes how often dangerous encounters occur. The studies support combining information about the animal with information about the release landscape. Readiness concerns both the behavior available to an individual and the conditions in which that behavior must succeed.
''','The studies came from the same research program but did not use a factorial design crossing every training and predator-control condition. Their results therefore support complementary management considerations without supplying an experimentally measured interaction between the two interventions.')
add('Experienced companions change post-release foraging','monkey',['monkey_diet'],'''
**Conspecifics** are individuals of the same species. Gómez-Muñoz and colleagues followed reintroduced woolly monkeys in Colombia across successive releases. The first group lacked previously released companions, while later groups encountered survivors already familiar with the site.

Observers recorded diet, proximity, movement, and forest height after release. The later groups differed in diet composition during the initial two months, with more rapid use of wild foods. The presence of experienced individuals supplied a social environment containing animals that already knew local resources.

The authors proposed **social learning**, acquisition of information through others, as a mechanism for faster adaptation. Encountering experienced companions could direct attention toward usable foods and foraging locations. The measured findings concerned diet and space use in naturally interacting groups, rather than a controlled imitation experiment.
''','The experienced individuals were survivors of earlier releases, not a separately introduced population of demonstrators. Release cohorts differed in year and composition, so the proposed social-learning mechanism was not isolated experimentally. The focal observations nevertheless documented the social context and behavioral adjustment after release.')
add('Diet diversity expands with access to local experience','monkey',['monkey_richness'],'''
**Dietary richness** is the number of distinct food species consumed. Across monitoring, the first woolly monkey group consumed fruits from 25 plant species, compared with 31 and 53 species in the later groups. The later groups had access to previously released, experienced companions.

Fruit identification was based on collected plant material and recorded feeding bouts. This distinguished use of wild fruit species from feeding at supplemental platforms. A broader wild diet represents access to more natural resources than a narrow dependence on provided food.

The authors proposed that experienced companions help newly released monkeys locate and recognize suitable fruits. This hypothesis links social proximity with resource knowledge. Differences in diet became less pronounced over the longer monitoring period, consistent with continued adjustment as initially inexperienced animals gained their own experience.
''','Diet richness counts food species rather than animal sample size. The study separately recorded food categories and identified fruits botanically. The richer later diets were observed alongside experienced companions, but other cohort and temporal differences remain part of the interpretation.')
add('Home-range expansion measures adjustment to the forest','monkey',['monkey_range'],'''
A **home range** is the area an animal uses during ordinary activity. Researchers mapped woolly monkey locations after release and compared spatial use during the first two months with use across six months. The first group initially remained close to feeding areas.

Its estimated broad home range increased from about 0.34 ha at two months to about 108 ha at six months. The later groups, released with experienced companions present, established larger early ranges of about 3 and 22 ha. These differences described how rapidly groups began using the surrounding forest.

Expansion of space use changes access to dispersed fruit resources. The later groups’ earlier movement away from the feeding area coincided with differences in diet. Spatial and dietary adjustment therefore developed together, connecting navigation through the release habitat with the resources available for independent foraging.
''','A hectare is an area of ten thousand square meters. The reported ranges are the paper’s broad utilization estimates, not the smaller core areas used most intensively. The first group’s large later range does not erase its very restricted early use, which is the relevant timing difference.')
add('Forest height and survival vary among released monkeys','monkey',['monkey_height','monkey_survival'],'''
**Vertical strata** are height layers within a forest. The woolly monkey study recorded the height of each focal animal, linking release adjustment to movement above the ground as well as movement across the site. The groups initially occupied different height distributions.

The third group used higher strata during the early period, while the second used lower strata. Differences became less pronounced over six months. Experienced companions therefore accompanied faster adjustment in some behaviors, but the groups did not follow one identical spatial pattern.

Individual survival also varied within and among groups. The study linked access to experienced animals with diet diversity and spatial adaptation, while retaining the differences among individual outcomes. Recovery of species-typical foraging requires several coordinated behaviors: locating resources, traveling through the forest, and using its vertical structure.
''','The study was observational across successive releases. The survival figure documents individual outcomes rather than a randomized effect of companion presence. Early differences in height use and later convergence reinforce that behavioral adjustment has a time course and several dimensions.')
add('Satellite tracks test reintegration after rehabilitation','logger',['turtle_core'],'''
**Satellite telemetry** uses an attached transmitter to relay an animal’s location or other measurements through satellites. Robinson and colleagues used it to follow rehabilitated green sea turtles released from the United Arab Emirates after injuries and prolonged periods in care.

Some turtles had spent months to years in rehabilitation before release. Their tracks documented return to shallow coastal areas used by wild green turtles. The majority established local ranges between Dubai and Abu Dhabi, near areas where they had originally stranded.

Movement records supplied evidence of reintegration after physical recovery. Returning to suitable habitat and maintaining a coherent range are behavioral outcomes beyond discharge from a clinic. The original maps preserve the relationship between release, movement, and repeated use of coastal areas associated with feeding habitat.
''','The study reported rehabilitation durations from 96 to 1,353 days. Duration in care alone did not prevent the documented movements after release. Satellite telemetry supplies location evidence; direct feeding behavior was inferred from habitat use rather than continuously observed underwater.')
add('Local residency can be a successful post-release pattern','logger',['turtle_ranges'],'''
**Residency** means repeated use of a relatively restricted area rather than continual long-distance travel. Several rehabilitated green turtles established shallow-water home ranges along the United Arab Emirates coast, with overlapping areas of use after release.

**Core habitat** is the portion of a range used most intensively. The turtles’ core areas were predominantly coastal and associated with known seagrass areas, generally in water shallower than 10 m. Repeated use linked movement to habitat capable of supplying food resources.

Long travel is therefore not the only behavioral outcome associated with successful reintegration. A resident turtle can remain active within a suitable feeding landscape. The tracked animals expressed both resident and transient patterns, so post-release evaluation followed habitat use and persistence rather than ranking success by distance traveled alone.
''','The original maps distinguish broad ranges from more intensively used core areas. Seagrass association supports a foraging interpretation for green turtles, but satellite locations are not direct observations of each feeding event. The study documented both local residency and movement beyond the Gulf.')
add('A rehabilitated turtle resumes ocean-scale movement','logger',['turtle_longtrack'],'''
One green turtle, Dibba, was released near the area where she had been found after rehabilitation. Her subsequent satellite track covered 8,283 km from the United Arab Emirates toward the Andaman Sea, passing through several regional marine environments.

The route extended through Omani waters, across the Arabian Sea toward the Maldives, then past Sri Lanka and into the Bay of Bengal. Transmissions were intermittent, and the mapped track connected recorded positions across the journey rather than continuously observing every movement.

The long-distance record documented sustained travel after prolonged care and serious injury. Cross-border movement also placed the animal within several jurisdictions after release. Rehabilitation outcomes therefore depended on marine conditions and threats extending far beyond the clinic and the coastline where release occurred.
''','Dibba’s track was the longest published for a green turtle at the time of the study. Intermittent transmission means the mapped distance describes the recorded track rather than an exact continuous path. The study combines this exceptional journey with resident turtles rather than treating it as the required pattern for all releases.')
add('Post-release monitoring reveals function and new threats','logger',['turtle_temperature'],'''
Temperature records documented the environments encountered by green turtles after release. Their tracks and temperature histories placed behavior within seasonal marine conditions, rather than treating a functioning transmitter as the entire rehabilitation outcome.

The turtles used shallow coastal habitat and experienced the local seasonal temperature range. Most persisted after release, while one was killed by an injury thought to result from a spear gun. A new human-caused threat could therefore interrupt an otherwise successful return to the wild.

Release readiness concerns the capacities regained during care; post-release monitoring concerns how those capacities operate in the destination environment. The tracking study connected movement, habitat use, and later mortality to that environment. Continued survival depended on both recovered function and exposure to hazards after the animal left rehabilitation.
''','The suspected spear-gun death was a post-release injury, not evidence that the turtle had failed to recover its earlier problem. Some tags stop transmitting because of equipment or attachment failure, so transmission cessation alone must be distinguished from confirmed mortality. The study used the available track and clinical evidence to interpret individual outcomes.')

assert len(S)==44,len(S)
spec={'lecture':64,'content_slides':44,'theme':'ash-blue-porcelain','title_height':2.6,'title_image':figure('seal_social'),'title_refs':[ref('maternal')],'slides':S,'takeaways':{'items':[
 {'lead':'Recovery has several time scales','text':'Hormones, feeding, growth, immune measures, and neural activity can recover at different rates; serial measurements preserve those differences.'},
 {'lead':'Behavioral opportunity matters','text':'Social contact, water access, and food-access tasks allow species-typical behavior during care; their value must be assessed through the animal’s response.'},
 {'lead':'Neural injury can persist','text':'Sea lion hippocampal damage is associated with spatial-memory deficits and reduced hippocampal–thalamic connectivity relevant to foraging.'},
 {'lead':'Learning can improve release outcomes','text':'Fox-awareness training increased tracked survival in western ringtail possums; experienced companions were associated with faster dietary and spatial adjustment in woolly monkeys.'},
 {'lead':'Readiness depends on the destination','text':'Personality, predator pressure, habitat resources, and transport-induced stress influence the conditions faced immediately after release.'},
 {'lead':'Monitoring tests reintegration','text':'Post-release tracking distinguishes local residency, long-distance movement, and new threats, connecting recovery during care to life in the wild.'}], 'cite':'; '.join(short(k) for k in ['cold','cook','predator','monkey','logger']),'refs':[ref(k) for k in R]}}
(B/'lecture.json').write_text(json.dumps(spec,indent=2,ensure_ascii=False))
print('Written',len(S),'content slides; words',min(len(' '.join(s['body']).split()) for s in S),max(len(' '.join(s['body']).split()) for s in S))
