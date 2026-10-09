"""Lecture 55: source-based teaching paragraphs and original article crops."""
import json,re,html
from pathlib import Path
B=Path(__file__).resolve().parent
R=json.loads((B/'research.json').read_text());F=json.loads((B/'figure_sources.json').read_text());S=[]
def ref(k):return html.unescape(re.sub('<[^>]*>','',R[k]['reference']))
def figure(n):
 x=F[n];k=x['paper'];a=R[k]['authors'][0]['family']
 return {'path':'figures/'+n+'.png','kind':'article','caption':f"{a} et al. ({R[k]['year']}), Fig. {x['figure']}. {x['description']}",'source_url':'https://doi.org/'+R[k]['doi']}
def add(title,k,imgs,text,note):
 body=[p.strip() for p in text.strip().split('\n\n')];assert len(body)==3,title
 keys=list(dict.fromkeys([k]+[F[n]['paper'] for n in imgs]));sd={'title':title,'body':body,'transcript':[re.sub(r'\*\*|(?<!\w)_(?=\w)|(?<=\w)_(?!\w)','',p) for p in body]+[note],'refs':[ref(x) for x in keys],'cite':'; '.join(f"{R[x]['authors'][0]['family']} et al. ({R[x]['year']})" for x in keys),'figure_width':5.8}
 if len(imgs)==1:sd.update(layout='figure-right',figure=figure(imgs[0]))
 else:sd.update(layout='figures-right',figures=[figure(n) for n in imgs],primary_figure_height=2.7)
 S.append(sd)

add('Visitor distance changes penguin use of the pool','penguin_proximity',['penguin_barrier'],'''
Little penguins at Melbourne Zoo changed their behavior when visitors could approach the enclosure edge. **Vigilance** is sustained monitoring of the surroundings; **huddling** is close aggregation with other birds. Both increased as conditions changed from a closed exhibit to ordinary visitor access.

With unregulated visitor behavior, huddling increased from about 25% in the closed exhibit to 69% at normal viewing distance. Surface swimming decreased from 39% to 9%. The birds redistributed their activity from exposed pool use toward aggregation and monitoring.

A barrier placed visitors 2 m from the enclosure while preserving their view. Increased distance reduced the opportunity to loom over birds and reach the pool. Physical separation therefore changed the sensory encounters available to penguins as well as the locations visitors could occupy.
''','The experiment manipulated viewing distance and visitor-behavior regulation separately. The percentages describe the visible birds sampled during observations, rather than the probability that any particular individual experienced fear.')
add('A physical barrier changes visitor actions','penguin_proximity',['penguin_barrier','penguin_layout'],'''
The enclosure had visitor access along several edges, allowing people to approach swimming birds closely. Chiew and colleagues compared normal access with a 2 m setback, and also tested signs and uniformed personnel intended to regulate visitor behavior.

The setback reduced touching of enclosure features by about 90% and sudden visitor movements by about 99%. Contact with the water fell to zero. Ambient sound remained around 61–62 dB across the open-exhibit conditions, so reduced close encounters occurred without a corresponding reduction in overall noise.

**Looming** means approaching or extending the body over another animal, producing a nearby changing visual stimulus. The barrier constrained this action directly. Altering visitor access can change the frequency and geometry of animal encounters even when the visitors still observe the animals and the general sound environment persists.
''','The sound measurements were made in air at the exhibit and use the sound meter’s reference, not the underwater reference used in the dolphin and fish studies. Sound-level numbers from those environments should not be compared directly.')
add('Close visitors shift swimming toward withdrawal','penguin_proximity',['penguin_cameras'],'''
Penguins can respond to a nearby visitor by moving away, aggregating, or maintaining visual surveillance. Cameras sampled different land and pool regions, allowing the investigators to relate these responses to the visitor-facing boundaries rather than counting only total activity.

As unregulated visitors approached more closely, the proportion of birds within 1 m of the viewing edges fell sharply. Near one edge it decreased from about 28% with the exhibit closed to 1% at normal access. Retreating events were rare with the exhibit closed or viewing distance increased.

The same enclosure supported different activity distributions under different visitor conditions. More surface swimming with distant or absent visitors accompanied greater use of exposed areas. Withdrawal therefore has both a behavioral component, such as retreat, and a spatial component, such as reduced occupancy near a viewing edge.
''','Allopreening is one bird preening another bird. The study separated these brief behavioral events from sustained behavioral states such as huddling, which were scored as proportions of the visible group.')
add('Changing access is more reliable than a sign alone','penguin_proximity',['penguin_sign','penguin_cameras'],'''
Signs and uniformed personnel asked visitors to remain quiet, move slowly, and avoid physically interacting with the birds. **Behavioral regulation** here means this attempt to modify human conduct, whereas increased viewing distance physically restricted where visitors could stand.

The regulation treatment did not produce a clear change in the measured frequencies of visitor actions. It reduced penguin huddling by about 20% when the exhibit was open, while the setback changed several visitor actions directly. With both regulation and increased distance, huddling was similar to the closed-exhibit level.

Penguin behavior changed even though fecal glucocorticoid metabolite concentrations showed no detected treatment effect. These metabolites are excreted products of adrenal hormones. Immediate withdrawal and a delayed endocrine measure operate over different timescales, so the behavioral response remains relevant when the fecal comparison is unchanged.
''','The unchanged fecal measure is a consequential result because it prevents hormone concentration from being used as the sole criterion for whether the visitor intervention mattered. It does not negate the measured spatial and behavioral changes.')
add('A covered window changes local visual exposure','penguin_window',['window_cover'],'''
At Taronga Zoo, little penguins occupied a pool bordered by four viewing windows and a corner hidden from visitors. A visual screen covered the main window on treatment days, creating a local change in exposure while other viewing positions remained available.

The proportion of visitors at the main window fell by about 85%, with many moving to a second window. Touching and direct interaction at the covered window were eliminated. Mean ambient noise stayed near 59–60 dB, and overall visitor numbers did not change clearly.

The intervention separated close contact at one boundary from the wider presence of visitors. It altered the visual and tactile encounters at a particular part of the pool rather than removing people from the entire exhibit. Penguin location could consequently be evaluated against a specific change in sensory access.
''','Treatments were applied on different days, and behavior was scored in defined viewing-window and corner areas. The screen also changed visitor behavior, so its effect includes altered human actions as well as blocked visual access.')
add('Visual shielding supports preening near the window','penguin_window',['window_views','window_cover'],'''
**Preening** is the use of the beak to maintain feathers. Near the main viewing window, penguins performed more preening in the water when a visual screen blocked visitor contact. Vigilance in that same area decreased by about 70%.

Water preening near the main window increased by about 180%, from a low starting frequency. These are relative changes in behavior within the sampled area. The intervention altered the allocation of activity between monitoring the surroundings and feather maintenance.

Covering the window also increased the proportion of penguins present nearby. Visual shielding thus made a visitor-facing region more usable while reducing surveillance there. A pool boundary can support swimming and maintenance behavior differently depending on the encounters permitted through the glass above it.
''','A large relative increase can begin from a small baseline: water-preening observations increased from about 0.33% to 0.92% near this window. The effect is local and should not be described as a comparable change in the entire flock’s daily activity.')
add('Exhibit geometry redistributes animals and visitors','penguin_window',['window_locations','window_views'],'''
**Space use** describes where animals spend their time within an enclosure. In the Taronga experiment, covering one viewing window redirected visitors toward another and increased penguin occupancy near the screened boundary. People and birds therefore responded to the same local modification.

The corner remained the region with the greatest penguin presence, with daily visible proportions commonly between 30% and 60%. The main-window region typically contained about 10–20%. These unequal distributions reveal that nominal pool area and behaviorally usable area are different quantities.

When the main window was covered, surface swimming in the hidden corner decreased while maintenance behavior increased near the screened window. The activity pattern involved redistribution across regions. Enclosure evaluation can distinguish total visibility from occupancy and behavior at individual sensory boundaries.
''','The observation system recorded only birds visible in each camera view. Overall visibility did not change clearly between treatments, which makes the local redistribution informative rather than simply a consequence of all birds becoming easier to see.')

add('Dolphins coordinate a learned task through sound','dolphin_noise',['noise_setup'],'''
Bottlenose dolphins at Dolphin Research Center learned to swim to separate underwater buttons and press them within 1 s of each other. A successful response required coordination between partners, including trials when one animal was released after a randomized delay.

Animal-borne **DTAGs**, instruments recording sound and movement, captured the signals reaching each dolphin. Investigators added broadband noise spanning 1–20 kHz or used a pressure washer employed in lagoon maintenance, comparing these conditions with ambient noise.

The buttons established a measurable link between communication and joint action. The pair succeeded in 85% of ambient-noise trials but in 62.5% under the highest-noise treatment. A learned cooperative response therefore depended on the acoustic environment in which the partners attempted to coordinate.
''','This experiment involved one trained male dyad. Its strength is the within-pair change under controlled noise treatments, with the same learned task and partners, rather than a population estimate for all dolphins.')
add('Noise overlaps the dolphins’ communication signals','dolphin_noise',['noise_spectra'],'''
**Acoustic masking** occurs when background sound reduces the detectability of a relevant signal. The noise playback occupied 1–20 kHz, overlapping the dolphins’ whistle frequencies. Reese’s signature whistle spanned approximately 4–18 kHz, and Delta’s spanned 6–20 kHz.

A **signature whistle** is an individually distinctive identity signal. Sound recorded near the buttons ranged from about 115 dB in the ambient condition to 150 dB during pressure-washer exposure, referenced to 1 µPa. These underwater pressure levels describe the stimulus at the measurement position.

Cooperative success declined as noise increased. Because the animals had to align button presses within 1 s, interference with detecting a partner’s signal could disrupt the timing of their actions. The same acoustic disturbance can therefore affect a social task through its sensory demands rather than through a change in the task’s rules.
''','The authors interpret masking as a principal mechanism, while the behavioral experiment measures task performance and compensatory signaling. Measurements at the buttons and animal-borne measurements have different positions and should retain their original labels.')
add('Dolphins increase whistle output in louder noise','dolphin_noise',['noise_amplitude'],'''
**Apparent output level** is the whistle amplitude estimated from the animal-borne acoustic recording. Both dolphins increased whistle output as the noise measured before a call increased. Increasing signal amplitude is a vocal compensation for a more difficult listening environment.

The response occurred in each member of the dyad, even though their absolute whistle levels differed. Animal-borne recording linked each call to the noise experienced by its producer, instead of assigning every call the same sound level measured elsewhere in the lagoon.

The dolphins also oriented toward their partner more often and approached the partner’s half of the lagoon during louder treatments. The authors’ hypothesis is that directional listening and reduced separation helped detect the partner’s signal. Vocal output, body orientation and movement formed coordinated responses to the sensory disturbance.
''','Directional listening is a proposed interpretation of the orientation response, not a measurement of auditory neurons in this study. The increase in amplitude and the movement changes were measured directly in the same noise experiment.')
add('Longer whistles still leave coordination impaired','dolphin_noise',['noise_duration','noise_spectra'],'''
Dolphins can lengthen a communication signal by stretching its contour or repeating whistle elements. Under the highest noise, both animals nearly doubled their average whistle duration. Reese’s mean duration rose from about 0.62 to 1.15 s, and Delta’s from 0.50 to 0.83 s.

A longer signal supplies more acoustic material during which a listener may detect the call. The pair also increased amplitude and changed orientation, yet cooperative success remained lower under stronger noise. These measured compensations were therefore incomplete for this time-sensitive joint task.

Lagoon cleaning noise reached the frequency range used for social communication while the dolphins were actively cooperating. Sensory management includes the timing and operation of maintenance equipment as well as the sound produced during a public session. The relevant outcome is successful communication-linked behavior under those conditions.
''','Longer whistles should not be equated with restored performance: duration and task success were measured separately. The pressure washer was a realistic maintenance source, while the other noise treatments were experimentally controlled playbacks.')

add('Noise exposure changes the timing of auditory responses','fish_noise',['fish_aep','fish_hair'],'''
**Auditory evoked potentials** are electrical responses recorded after sound stimulation, reflecting synchronized activity in the auditory pathway. Wong and colleagues exposed adult zebrafish to noise for 24 h and then compared these responses with those of unexposed controls.

At a 1000 Hz test stimulus, peak response latency increased from about 2.17 ms in controls to 2.66 ms after continuous noise. Latency is the interval between the stimulus and the measured response. Noise exposure therefore changed the timing of the neural signal as well as auditory sensitivity.

The experiment compared continuous noise with several intermittent regimes at approximately 150 dB re 1 µPa. All noise-treated groups had delayed responses. The temporal structure of exposure influenced the size and frequency range of impairment, while a delay in auditory processing was shared across the treatments.
''','The auditory response combines electrical activity across the auditory pathway. Saccular hair cells and their presynaptic ribbons were examined in the same exposure experiment, connecting sensory tissue measurements with changes in response timing.')
add('Quiet intervals alter the auditory exposure dose','fish_noise',['fish_threshold','fish_regimes'],'''
An **auditory threshold** is the lowest sound level producing a detectable auditory response. After 24 h of exposure, zebrafish required stronger test sounds across parts of their hearing range. The shift from control sensitivity was reported in dB.

Continuous noise and a fast pattern of 1 s noise followed by 1 s silence produced average shifts of about 13 dB. A slower pattern with 4 s silent intervals and an irregular pattern produced shifts nearer 10 dB. Intermittent sound therefore retained substantial effects despite its silent intervals.

**Duty cycle** is the proportion of exposure time occupied by noise. Changing the intervals changes cumulative acoustic exposure while preserving the level during each noise segment. The findings favor overall exposure amount over regularity alone as a determinant of auditory impairment in this preparation.
''','Differences among the noise-treatment average threshold shifts were not clearly separated in the formal comparison. The approximately 13 and 10 dB values describe the measured pattern, while the source’s central interpretation emphasizes dose and duty cycle rather than a precise safe interval.')
add('Auditory impairment involves the hair-cell synapse','fish_noise',['fish_hair'],'''
The **saccule** is an inner-ear organ containing sensory hair cells. Their stereocilia are projections involved in detecting mechanical stimulation. Hair cells communicate with afferent neurons, which carry sensory information toward the brain, through specialized presynaptic structures called ribbon synapses.

**Ribeye b** is a protein associated with those presynaptic ribbons. Fluorescent labeling identified hair-cell bundles and Ribeye b puncta separately. Continuous noise reduced the measured Ribeye b puncta particularly in middle and posterior saccular regions, while hair-cell bundle counts showed no clear overall group difference.

The authors’ hypothesis is that reduced ribbon-associated protein compromises transmitter release and weakens afferent stimulation. This synaptic explanation links the tissue measurement to higher hearing thresholds and slower evoked responses. Counting sensory cells alone would miss the measured change at their communication sites.
''','Ribeye b staining is a structural presynaptic marker. The study did not directly record transmitter release, so the release mechanism remains the authors’ explicitly named hypothesis rather than an additional experimental measurement.')
add('Prior noise shifts exploration of a new tank','fish_noise',['fish_diving'],'''
The **novel tank diving test** measures how zebrafish explore an unfamiliar tank. Fish initially favor the bottom and then increasingly enter upper water. Following noise exposure, investigators recorded this time-dependent distribution during a 6 min test.

During the first minute, controls spent about 82% of their time at the bottom, compared with approximately 98–99% in noise-exposed groups. The differences were prominent early in the test and no longer clear during minutes 3–6. Previous acoustic conditions therefore affected the initial response to a new environment.

Irregular-noise exposure also delayed the first entry into the top zone. Average swimming velocity over the test did not change clearly across groups, so altered vertical exploration was not explained by a general slowing of movement. Sensory exposure can modify where and when an animal explores even after the sound treatment has ended.
''','Bottom dwelling is the behavior measured; the assay is commonly used as an anxiety-related measure. The distinction from unchanged swimming speed matters because it separates spatial avoidance from a simple motor deficit.')

add('Aquarium complexity changes the opportunities for learning','fish_learning',['learning_tanks','learning_maze'],'''
Juvenile tambaqui, _Colossoma macropomum_, lived for 192 days in enriched or impoverished aquaria. The enriched environment included plants, shelter and running water; the impoverished environment lacked these features. **Environmental enrichment** changes the opportunities for activity and sensory experience within housing.

Fish then entered a plus-maze aquarium with different visual cues on its arms. Squares marked a correct choice and circles a wrong choice. Correct choices ended the trial, while wrong choices produced a 1 min restriction of swimming space before the fish returned to its home aquarium.

Across 30 possible trials, more than half of enriched fish met the learning criterion, compared with fewer than 30% of impoverished fish. A long-term difference in aquarium experience accompanied a later difference in acquiring a visually guided choice, linking everyday sensory and motor opportunities to task performance.
''','The enriched treatment combined several changes, including flow-driven activity and visual complexity. The maze used an aversive consequence after incorrect choices, so it should not be described as food-reward conditioning.')
add('Enriched fish acquire the visual-choice task faster','fish_learning',['learning_performance','learning_maze'],'''
**Learning acquisition** is the development of a reliable response through experience. In the tambaqui experiment, repeated maze trials linked visual cues to different consequences: immediate return to the home aquarium after a correct choice, or brief confinement after an incorrect choice.

Enriched fish reached the task criterion more often over the three testing days. They were also larger, averaging about 10.0 cm and 20.2 g, compared with 8.9 cm and 14.9 g in impoverished housing. Growth and learning were separate measured outcomes of the same housing comparison.

Plants and shelters supplied spatial features, while water flow supplied repeated motor activity. The authors’ hypothesis is that this combination of visuospatial stimulation and exercise contributed to improved learning. The daily environment supplied repeated experience before formal testing began, rather than changing only the appearance of the test aquarium.
''','Fish met the acquisition criterion after three consecutive correct choices or seven correct choices within ten consecutive trials. They performed up to ten trials on each of three consecutive days. The enriched housing combined visual complexity and opportunities for exercise, rather than isolating these components in separate treatments.')
add('Telencephalic cell counts change with enriched housing','fish_learning',['learning_cells','learning_brain'],'''
The **telencephalon** is the anterior part of the fish forebrain, associated with learning and spatial behavior. The **optic tectum** is a midbrain region involved in sensory and motor processing. Pereira and colleagues counted cells in both regions after the housing and maze procedures.

Estimated total telencephalic cell counts averaged about 1.42 million in enriched fish and 1.15 million in impoverished fish. The tectal count did not exhibit the same clear housing difference. Enriched experience therefore accompanied a region-specific structural response rather than a uniform increase throughout the sampled brain.

**Stereology** estimates cell totals using systematically sampled tissue sections. The counts included cells visible with the staining method rather than a defined neuronal subtype. The regional comparison connects housing, brain structure and learning while identifying the telencephalon as the region with the measured increase.
''','The staining identified total cells rather than selectively labeling neurons. Neurons and glia can both contribute to the estimate, and a larger regional total does not by itself identify the cellular process that produced the difference.')
add('Brain transcripts link experience to protein regulation','fish_learning',['learning_genes','learning_histology'],'''
A **transcript** is an RNA molecule produced from genetic information. Brain RNA sequencing identified 64 transcripts whose abundance differed between enriched and impoverished tambaqui. Samples grouped according to housing condition, connecting the long-term environment to molecular expression.

One enriched-housing-associated transcript was **PPP2R1B**, encoding part of a protein phosphatase complex. A phosphatase removes phosphate groups from proteins. Phosphorylation and dephosphorylation change protein regulation at presynaptic and postsynaptic sites, providing a molecular route through which experience could affect signaling.

The authors’ hypothesis connects altered phosphatase-related expression with synaptic plasticity, persistent changes in communication between neurons. This molecular response accompanied better maze acquisition and higher telencephalic cell counts. The measurements span gene expression, regional structure and learned behavior within the same contrasting housing conditions.
''','RNA abundance is a molecular measurement, not a recording of firing or a measurement of enzyme activity. The paper calls for additional validation of the transcriptomic findings; the proposed phosphatase connection should be taught as a hypothesis.')

add('Foraging puzzles change how dolphins obtain food','dolphin_enrich',['enrich_devices','dolphin_photo'],'''
**Cognitive foraging enrichment** makes food acquisition depend on searching or manipulating a device. At Kolmårdens Djurpark, bottlenose dolphins received alternating weeks of cognitive devices and simpler objects during an 8-week study. The same animals experienced both treatments.

Fish were hidden inside sandboxes, barrels, kelp-like structures or containers during cognitive weeks. During non-cognitive weeks, similar food quantities were placed on or beside simpler objects. Each dolphin received about 0.1–0.2 kg of fish daily through enrichment, controlling the reward quantity while changing the actions required to obtain it.

The comparison separated possessing an object from solving a food-access problem. Dolphins could search, move a component, release fish and consume the reward through a sequence of actions. Food distribution therefore supplied opportunities for learned manipulation and foraging between their scheduled feeding and training sessions.
''','Both treatments included fish rewards. The cognitive devices required finding or extracting that fish, while the simple devices received food on or nearby. Several copies were generally provided to reduce competition within the dolphin group.')
add('Dolphins engage more with problem-solving devices','dolphin_enrich',['enrich_devices','enrich_engagement'],'''
Dolphin caretakers scored enrichment engagement on a five-level scale after observing each animal for 5–15 min. The scale ranged from no interest to sustained high engagement. The cognitive condition produced more highly engaged scores and fewer no-interest scores than the simpler-object condition.

The devices were familiar to the dolphins for at least three months before the study. They were placed at varying pool locations and not repeated during the next three days. Engagement therefore occurred with familiar task types whose immediate presentation and location varied.

A hidden-food device repeatedly connects manipulation with access to fish. This creates a functional reason to search or act on the object, while an equally familiar simple item mainly supports contact, pushing or rubbing. The observed difference concerns what the animals do with the resources, rather than the presence of objects alone.
''','Caretakers practiced the engagement scoring before the study. The scores are ordinal categories of involvement; they should not be interpreted as a direct continuous measurement of pleasure.')
add('Cognitive enrichment increases solitary and shared use','dolphin_enrich',['enrich_interaction','dolphin_photo'],'''
Independent focal observations recorded dolphin behavior in 5 min periods. During cognitive weeks, dolphins interacted with enrichment more often both alone and with other dolphins. Individual and social interaction were recorded separately as proportions of visible observations.

Multiple copies of devices were usually supplied to reduce competition, and dolphins remained together as one group. Access to the resource therefore combined individual manipulation with opportunities for shared activity. The observed social use involved the devices rather than a general increase in every social behavior.

Synchronous swimming and social play did not differ clearly between the two treatments. The behavioral effect was concentrated on enrichment interaction, anticipatory behavior and stereotypy. Cognitive resources changed particular components of the activity budget, providing a more precise account than a claim that all activity increased.
''','The plotted interaction proportions are observations within the focal sampling protocol. They are not percentages of an entire twenty-four-hour day, and device interaction alone is only one part of the welfare assessment.')
add('Foraging opportunities reduce repetitive dolphin behavior','dolphin_enrich',['enrich_behavior','dolphin_photo'],'''
**Stereotypy** is repetitive, relatively invariant behavior without an obvious immediate function. **Anticipatory behavior** occurs before a predictable event, such as a feeding or training session. Clegg and colleagues recorded both outside the enrichment provision itself.

Dolphins displayed less anticipatory and stereotypic behavior during cognitive weeks than during non-cognitive weeks. Pattern swimming, scored as a separate category, did not exhibit the same clear treatment difference. Classification matters because different recurring movement patterns need not respond identically to a change in foraging opportunities.

The food puzzles expanded behavior between scheduled sessions while the amount of enrichment food remained similar. The authors’ hypothesis is that more opportunities for independent problem solving reduced reliance on upcoming caretaker events as salient sources of stimulation. The measured improvement extended beyond immediate contact with the devices.
''','Anticipation is not automatically an abnormal behavior. Its frequency and context help interpret the result: the study measured a reduction alongside stereotypy and greater engagement, rather than treating every anticipatory response as pathology.')
add('Cognitive weeks support participation in training','dolphin_enrich',['enrich_training','dolphin_photo'],'''
Caretakers assessed **willingness to participate**, the dolphin’s readiness and motivation to engage during a training session. Scores ranged from no contact to excellent participation. Dolphins had higher participation scores during weeks when cognitive foraging enrichment was supplied.

The park conducted six to ten feeding sessions daily using positive reinforcement. A **reinforcer** is a consequence that increases the future likelihood of a response; here food rewards followed requested tasks. The participation measure consequently described engagement in an established human–animal learning routine.

Enrichment occurred outside that routine, yet its treatment was associated with the dolphins’ subsequent interaction with trainers. Providing opportunities for independent foraging and maintaining trained cooperative behavior were compatible in this experiment. Their effects were evaluated through both unscheduled activity and scheduled sessions at the park.
''','The study recorded construction work and access to different pools because these environmental factors also influenced behavior. The participation scale describes observable involvement with trainers rather than an estimate of a particular neurotransmitter concentration.')

add('Movement tags separate speed from body activity','dolphin_activity',['dolphin_gait','dolphin_photo'],'''
**Biologging** records an animal’s behavior using an attached instrument. Suction-cup movement tags on dolphins combined acceleration, orientation, depth and a speed sensor. Investigators measured activity outside formal training sessions at accredited zoos and aquariums.

**Overall dynamic body acceleration**, abbreviated ODBA, summarizes movement-related acceleration after gravitational components are removed. Speed measures travel through water instead. A gliding animal can maintain travel while changing acceleration relatively little, whereas repeated body movements produce a different acceleration pattern.

Dolphins in the analyzed dataset traveled an average of about 2.32 km per hour outside training. The synchronized records connected depth changes, surfacing, swimming speed and body pitch over seconds. Housing effects can therefore be evaluated against distinct motor outcomes rather than a single visual impression of how active a dolphin appears.
''','The study reported group ODBA values in m/s², while its representative frequency histogram labels acceleration in g. Each original axis must retain its unit; the slide uses the source’s reported distance rate without converting its data.')
add('Access and novelty relate to dolphin activity','dolphin_activity',['dolphin_speed','dolphin_photo'],'''
Lauderdale and colleagues compared movement records with habitat and management information. **Spatial experience** combined the water volume available to a dolphin with the time spent in different habitats. Greater daytime spatial experience was associated with higher dynamic body acceleration.

Dolphins receiving new enrichment weekly or monthly also had higher acceleration than animals receiving new types only yearly or less often. Activity differed with age and sex, with older dolphins exhibiting lower values. These associations place resource access and management frequency alongside individual biological characteristics.

Distance traveled and acceleration had different relationships with the measured predictors. A habitat can support different movement patterns even when total travel is similar. The observations consequently distinguish availability of space, frequency of new resources and the motor behavior actually expressed within that environment.
''','Facilities were not randomly assigned to their management routines. These results are associations across institutions, and should not be taught as a controlled demonstration that changing one schedule will necessarily reproduce the group-level difference.')
add('Training schedules relate to travel outside sessions','dolphin_activity',['dolphin_tag','dolphin_gait'],'''
The dolphin movement study categorized training schedules as predictable or semi-predictable. **Predictability** describes how consistently an event occurs at the same times. Semi-predictable routines retained regular care while allowing variation in the timing of sessions.

Dolphins with semi-predictable training schedules traveled farther per hour outside sessions than those with predictable schedules. The association concerned their unscheduled movement, because formal sessions were excluded from the analyzed tag records. New-enrichment frequency was also related to distance traveled.

The two motor measures responded differently to management categories: acceleration and distance were not interchangeable indicators. Examining behavior between sessions connects a training routine to the animal’s wider activity budget. Public presentation time is only one interval within a day of swimming, exploration and social interaction.
''','The movement analyses excluded sessions using recorded management information. The schedule result therefore applies to between-session travel in this observational dataset, rather than the amount of swimming performed on command during a show.')

add('A tactile puzzle recruits gorilla manipulation','gorilla',['gorilla_modules','gorilla_photo'],'''
Zoo-housed gorillas manipulated a modular food puzzle with connected compartments. **Cognitive enrichment** supplied a physical problem: move nuts through the compartments toward reward slots. Twelve modules arranged in three rows and four columns created different routes and access points.

The faceplates included 30 mm holes for fingers and 15 mm holes for sticks. Reward slots were larger, allowing food removal after the nut reached an accessible location. The geometry separated an action used to move the food from the location where the reward could be retrieved.

Gorillas usually sat at the device, using one hand for the puzzle and the other for postural support. Poking with fingers or sticks was more common than mouth use or shaking. Enrichment recruited coordinated posture, tactile investigation and object manipulation within a food-directed sequence of behavior.
''','The device contained protected sensing and camera technology, but gorillas interacted with the physical modules rather than a touchscreen. Its operation was independent of the computer backend during this study.')
add('Tool use changes access to puzzle rewards','gorilla',['gorilla_photo','gorilla_frame'],'''
A **tool** is an external object used to alter another object or obtain a goal. In the gorilla puzzle, stick tools extended access through small holes and helped move nuts along the modules. Food rewards were removed through the larger reward slots.

The three tool-using gorillas were the individuals that successfully extracted nuts. Across the trials, they retrieved 22, 50 and 20 nuts respectively. Tool use differed substantially among individuals, linking a specific manipulation strategy to successful access rather than merely to proximity to the device.

Most nuts were eaten immediately, but one gorilla accumulated five before consuming them together after a prolonged bout of use. The puzzle supported extended sequences of manipulation, retrieval and consumption. A useful task can therefore supply sustained behavior even when food extraction occurs intermittently rather than after every contact.
''','The study recorded naturally chosen strategies during voluntary access. It did not assign some animals to use sticks and others to use fingers, so strategy and success remain linked observations rather than randomized training conditions.')
add('Gorillas retain interest across repeated puzzle trials','gorilla',['gorilla_trials','gorilla_photo'],'''
The modular puzzle was offered in six hour-long trials. Engagement included physical contact and close observation. Device-use duration did not decline clearly across successive presentations, and time spent using it did not track reward extraction frequency in a simple one-to-one pattern.

Two females accumulated about 2 h of use each, approximately one-third of the total available presentation time. Other individuals used the device much less. The silverback observed it nearby but did not physically manipulate it, while infants also played around the structure.

Repeated availability supported different forms of engagement within the same group. Manipulation, observation and play can occupy different animals and developmental stages. The persistence of use across trials indicates that the device continued to recruit behavior after its first appearance, with individual response profiles remaining central to its evaluation.
''','The internal and external cameras allowed observation and physical use to be distinguished. A device located in a social enclosure should not be evaluated only by averaging the behavior of its most active users.')
add('Social access determines who uses the gorilla puzzle','gorilla',['gorilla_turns','gorilla_use'],'''
Gorillas generally took turns using the puzzle alone. The order differed among trials, and the youngest infant often remained with her mother during the mother’s device use. The time series recorded contact every 20 s within each hour-long presentation.

The study observed one device-related aggressive event, when a frequent user pushed an infant away during the first trial. Other use was largely compatible with sequential access. Individual differences in use reflected the social setting as well as the actions needed to retrieve food.

Multiple behavioral pathways contributed to the resource’s value: successful tool users manipulated the puzzle, the silverback observed, and infants played nearby. Enrichment access can be assessed by identifying who engages, how they engage, and whether another animal’s use blocks their opportunities. Group-level resource provision does not distribute participation uniformly.
''','There was no consistent overall change in the wider behavior measures after exposure. The device nevertheless supported distinct patterns of manipulation, observation and sequential access within the group.')

add('An expanded habitat changes elephant movement','elephant_habitat',['elephant_walk','elephant_map'],'''
Asian elephants at Oregon Zoo moved from an older enclosure to a larger, more complex habitat with distributed resources. GPS bracelets measured daily walking distances, while observations separately recorded route tracing and other activity. The design included previous, construction and new-habitat phases.

One adult female increased average daily walking from 7.6 to 15.4 km. Another walked about 17.3 km before and 17.6 km afterward. Removing estimated repetitive-route movement from the distances preserved the large increase for the first female.

The new habitat distributed feeders, pools, vegetation and other features across several areas. Movement could connect different resources rather than repeatedly follow one restricted path. The individuals’ contrasting responses distinguish the opportunities supplied by habitat design from the particular way each elephant uses them.
''','The before-and-after habitat comparison also included changes in management and herd dynamics. The GPS result measures distance directly and should retain the individual differences instead of describing a universal doubling for the herd.')
add('Elephants choose routes through dispersed resources','elephant_habitat',['elephant_tracks','elephant_map'],'''
**GPS tracking** records successive positions to reconstruct movement through an enclosure. In the new elephant habitat, recorded paths reached pools, dirt mounds, feeders and other outdoor areas. Location records connected movement to the distribution of resources.

Elephants had outdoor access for more than 20 h per day in every month except January. Individuals chose to spend roughly 6–20 h outdoors. Previous management constraints sometimes required one group to remain inside while another used the outdoor areas.

Access duration and actual occupancy are distinct. The expanded arrangement allowed different individuals to choose among indoor and outdoor locations for longer periods, while their routes varied with season and resources. Space functions as a network of reachable opportunities, and its use depends on where those opportunities are placed and when access is available.
''','Bracelet damage limited some juvenile recordings. The adult comparisons provide the most complete daily distance records, whereas juvenile tracking covered fewer observation periods.')
add('Food delivery recruits active elephant foraging','elephant_habitat',['elephant_budget','elephant_resources'],'''
An **activity budget** is the allocation of observed time among behaviors. In the new habitat, elephant interaction with food-delivery resources increased from about 3.8% to 24.5% of observations. Feeding without manipulating a delivery resource decreased from 32.7% to 15.3%.

Timed feeders and overhead hay nets changed how food became accessible. The elephants searched for or manipulated these resources rather than relying entirely on directly available food. Sharing food resources also increased, contributing additional feeding time scored within social behavior.

Foraging and feeding together, including shared food use, increased from about 42.4% to 53.9%. The principal change was therefore both temporal and functional: more observed activity involved obtaining food through environmental resources. Enclosure complexity changed the sequence of actions leading to feeding, not simply the number of objects present.
''','The activity budgets were sampled during staffed daytime hours. Their percentages should not be interpreted as the same measurement window as the twenty-four-hour elephant study discussed at the end of the deck.')
add('Construction and relocation have different endocrine effects','elephant_habitat',['elephant_hormone'],'''
**Glucocorticoids** are adrenal hormones involved in physiological regulation and responses to challenge. Their fecal metabolites are products measured after processing and excretion. In the elephant habitat study, concentrations and variability were compared across previous, construction and new-habitat phases.

The construction phase produced the highest median concentrations across the analyzed individuals. For one adult female, the phase medians were approximately 142, 194 and 146 ng/g respectively. Most individuals had lower values after construction, while one female retained higher concentrations in the new habitat.

Development of a habitat and its later use were biologically different periods. Construction combined disruption and environmental change; the finished habitat supplied more distributed resources and access. Individual endocrine trajectories help distinguish a temporary challenge during the transition from the pattern associated with living in the completed environment.
''','Fecal metabolites reflect delayed hormone secretion and varied among individuals. In particular, the adult female with continued elevation prevents describing the new habitat as uniformly reducing every elephant’s glucocorticoid concentration.')
add('Greater social choice changes elephant partner patterns','elephant_habitat',['elephant_social','elephant_types'],'''
**Affiliative behavior** maintains or expresses social association, whereas **agonistic behavior** includes conflict and dominance-related interactions. Elephants’ affiliative interactions formed most of the recorded social behavior in both habitats, ranging from about 72% to 91% across individuals.

The new habitat changed which herdmates spent time together. A female calf increased the share of her interactions involving adult females other than her mother from about 6% to 35%. The juvenile male spent less observed time near herdmates, while other animals showed different proximity patterns.

Reduced proximity can coexist with greater opportunity for social choice. The functional outcome depends on the identities of partners and the behaviors performed together, including shared feeding and affiliative contact. More space changed the organization of the herd’s interactions rather than producing one uniform increase in all social contact.
''','Proximity was defined within two body lengths and did not automatically mean active interaction. Adult-bull access also differed between phases, so partner composition should remain part of the interpretation of the social comparison.')

add('Positive reinforcement links cooperation to reward','elephant_training',['training_cort'],'''
**Positive reinforcement training** makes a desired response followed by a rewarding consequence. Elephants voluntarily cooperated with familiar husbandry tasks during routine training, while a separate treatment presented novel objects. Saliva was sampled before and over 60 min after each treatment.

Salivary **cortisol** is a glucocorticoid measure associated with the circulating hormone response. Mean cortisol decreased after familiar training, reaching a value about 23% below the initial level at 15 min. After novel-object exposure it initially increased, with its highest average level around 30 min.

Learned cooperation and unfamiliar enrichment supplied different challenges. Familiar response–reward contingencies allowed animals to act predictably within the training interaction. Novel objects instead recruited exploration of something not previously encountered, producing a different short-term endocrine trajectory despite both treatments being management activities.
''','These were routine familiar training sessions rather than the acquisition of a novel trained response. The time course is an observed salivary response; the article discusses choice and controllability as interpretations of the familiar training context.')
add('Novelty recruits both approach and avoidance','elephant_training',['training_individual','training_cort'],'''
**Neophilia** is the tendency to approach novelty, and **neophobia** is avoidance of unfamiliar stimuli. Presenting a new object can recruit both motivations. The elephant experiment compared the resulting short-term salivary cortisol response with familiar positive reinforcement sessions.

Novel-object exposure increased the average cortisol concentration by about 10% in the first study period and 20% in the second at its peak. Individual responses varied substantially, and the overall cortisol level was lower in the second period. The time course rose initially and then declined.

Novelty can therefore produce a transient physiological challenge while supplying opportunities to investigate. The response depends on the animal as well as the stimulus category. Enrichment evaluation can track approach, interaction and the temporal endocrine response instead of assuming that every unfamiliar object has the same effect on every individual.
''','The treatment compared different study periods and individual biological characteristics. The difference between periods should not be described as a pure experimentally isolated habituation effect.')
add('Individual context shapes the elephant cortisol response','elephant_training',['training_handling','training_individual'],'''
Elephants in the training study lived at three zoos and experienced different handling arrangements. **Protected contact** places a barrier between caretaker and elephant; **free contact** allows them in the same space. The investigators analyzed these conditions alongside individual biological characteristics.

Cortisol concentrations varied with sex, age, reproductive condition, institution and handling context in different analyses. Novel-object responses and routine training responses also followed distinct time courses. A single post-event sample would therefore combine several sources of variation while missing the trajectory.

The repeated sampling schedule distinguished an initial response from later recovery over 60 min. Individual context and time since the event are both part of the endocrine measurement. Training and enrichment assessment can retain that temporal and biological information rather than assign one hormone value to an entire species or management category.
''','Handling arrangements covaried with zoo and individual histories; they were not randomly assigned. The article’s broad conclusion is to interpret cortisol within individual and procedural context rather than infer a universal causal advantage from one handling category.')

add('Pinnipeds respond differently to enrichment devices','seal',['seal_devices','seal_preferences'],'''
Rehabilitating California sea lions and northern elephant seals received artificial kelp and two rubber enrichment devices during 30 min presentations. **Pinnipeds** are the group containing seals, sea lions and walruses. Their shared aquatic environment did not produce identical object use.

Elephant seals made more interactions with the devices on average, while use varied substantially among individuals. The heat map captured these patterns separately for each animal and object. Some animals never contacted a particular device despite using other available resources.

A device’s effectiveness depends on the behaviors it affords and the animal’s response to those opportunities. Sea-lion pups engaged more than yearlings in this study. Species, age and individual use patterns therefore contributed to enrichment performance, even when the same objects and presentation duration were supplied.
''','These were recovering young animals at a rehabilitation center with pools and whole-fish feeding, not a public performance program. Their results provide a comparative test of device function during temporary managed housing.')
add('Some devices reduce sea-lion stereotypic behavior','seal',['seal_stereotypy','seal_devices'],'''
California sea lions expressed repetitive pacing, pattern swimming or inappropriate suckling during rehabilitation. The investigators compared behavior during device presentation with no-enrichment observations. Animals were medically stable and had access to pools before entering this enrichment comparison.

Artificial kelp and the larger rubber device were associated with reduced stereotypic behavior. The smaller device recruited interaction but did not produce the same clear reduction. Engagement with an object and reduction of a target behavior were therefore separate outcomes.

The effective resources supplied alternative manipulation and activity during the presentation. This comparison identifies function at the level of a particular device and behavior, rather than assigning all enrichment an identical effect. Monitoring the repetitive behavior alongside interaction time distinguishes an attractive resource from one associated with the intended behavioral change.
''','Only the sea lions with recorded stereotypy contributed to the target-behavior model. Device contact and changes in stereotypy were separate measurements, which explains why an object could recruit use without producing the same effect on repetitive behavior.')
add('Enrichment redirects attention from people to resources','seal',['seal_people','seal_preferences'],'''
The pinniped study scored attention toward people and staff areas separately from swimming, inactivity and device contact. Without enrichment, looking toward these areas occupied about 13% of observed sea-lion behavior and 24% of elephant-seal behavior on average.

Artificial kelp and the smaller rubber device reduced looking toward people and staff areas. The larger device did not produce the same clear effect on this behavior. Device function therefore depended on the behavioral outcome being measured, alongside differences in use among individuals.

Managed aquatic environments contain both human-associated cues and opportunities for animal-directed activity. The measured shift in attention parallels the dolphin study’s reduction in anticipatory behavior during cognitive weeks. Resources can change how behavior is distributed between caretaker-related locations and activities available independently of a scheduled session.
''','The dolphin and pinniped studies used different ethograms and observation protocols. Their comparison concerns the direction of behavior toward available resources, not equivalence of percentages or a shared measured neural circuit.')

add('Dispersed feeding extends elephant foraging time','elephant_long',['long_feeding','elephant_resources'],'''
At Whipsnade Zoo, hay was supplied in elevated nets and browse was hung on winches or distributed at ground level. Food at opposite ends of the exhibit encouraged elephants to use more of the enclosure, while summer grass paddocks supported grazing.

The adult male spent about 81% of daytime observations feeding, and adult females about 70%. These values exceeded the historical comparison used in the paper. The resources extended the actions involved in obtaining and processing food throughout the observed daytime period.

The Oregon study similarly recorded more interaction with food-delivery resources after habitat expansion. Across these institutions, food presentation changed both locations and sequences of behavior. Foraging opportunity includes searching, reaching and manipulation as well as consuming the same nutritional resource, linking enclosure design to the time available for those actions.
''','The Whipsnade study used a historical published comparison rather than a simultaneous randomized control herd. Its direct measurements establish this herd’s activity budget, while the Oregon before-and-after study supplies a separate comparison of resource use.')
add('Resting and foraging require different habitat resources','elephant_long',['long_rest','elephant_budget'],'''
The Whipsnade elephants had access to deep sand during the study. All observed individuals spent more than half of their resting time lying down, with the youngest animals showing particularly high proportions of lying rest. Resting posture was scored separately from feeding and other activity.

Adult females averaged approximately 244–297 min of rest per night, while younger individuals rested longer. These night observations measured a different behavioral interval from daytime feeding. A habitat must support recovery periods as well as opportunities for movement and foraging.

Activity budgets connect those requirements across a day. Penguin shielding changed surveillance and maintenance behavior, dolphin puzzles changed foraging and anticipation, and elephant resources supported feeding and rest. The functional question is which behaviors the environment permits and how the animal distributes its activity among them.
''','Resting time combines standing and lying rest. The percentage of lying rest uses total resting time as its denominator, so it describes posture during recovery rather than the proportion of the entire night spent resting.')

for title, extras in [('Enrichment redirects attention from people to resources',['dolphin_enrich']),('Resting and foraging require different habitat resources',['penguin_window','dolphin_enrich'])]:
 sd=next(x for x in S if x['title']==title)
 sd['refs'].extend(ref(k) for k in extras)
 sd['cite']+='; '+'; '.join(f"{R[k]['authors'][0]['family']} et al. ({R[k]['year']})" for k in extras)
# Give dense and tall source panels the full figure column.
for title, name in [
 ('Exhibit geometry redistributes animals and visitors','window_locations'),
 ('Foraging puzzles change how dolphins obtain food','enrich_devices'),
 ('Dolphins engage more with problem-solving devices','enrich_engagement'),
 ('Foraging opportunities reduce repetitive dolphin behavior','enrich_behavior'),
 ('Movement tags separate speed from body activity','dolphin_gait'),
 ('Access and novelty relate to dolphin activity','dolphin_speed')]:
 sd=next(x for x in S if x['title']==title)
 sd.pop('figures',None);sd.pop('primary_figure_height',None)
 sd.update(layout='figure-right',figure=figure(name))
for title in ['Brain transcripts link experience to protein regulation','Pinnipeds respond differently to enrichment devices']:
 sd=next(x for x in S if x['title']==title)
 sd.update(figure_arrangement='side-by-side',primary_figure_width=3.6)

assert len(S)==44,len(S)
refs=[ref(k) for k in R]
spec={'lecture':55,'content_slides':44,'title_height':2.8,'title_refs':[ref('dolphin_activity')],'theme':'stone-brown-porcelain','title_image':figure('dolphin_photo'),'slides':S,'takeaways':{'items':[
 {'lead':'Sensory access changes behavior.','text':'Visitor distance and visual shielding alter penguin vigilance, maintenance behavior and use of exposed pool areas.'},
 {'lead':'Noise affects social coordination.','text':'Dolphins increase whistle amplitude and duration under noise, while success in a time-sensitive cooperative task still decreases.'},
 {'lead':'Auditory function depends on synapses.','text':'Noise changes zebrafish hearing thresholds and response latency alongside reduced presynaptic Ribeye b labeling.'},
 {'lead':'Learning opportunities have lasting effects.','text':'Complex fish housing accompanies better maze acquisition and regional brain changes; cognitive dolphin devices increase engagement and reduce stereotypy.'},
 {'lead':'Enrichment function varies among animals.','text':'Food puzzles, social access and device properties recruit different behaviors across individuals, ages and species.'},
 {'lead':'Habitat and training shape activity.','text':'Resource distribution alters elephant movement and feeding; familiar reinforcement and novelty produce different cortisol time courses.'}
 ],'cite':'Chiew et al. (2019); Sørensen et al. (2023); Wong et al. (2022); Clegg et al. (2023); Glaeser et al. (2021)','refs':refs}}
(B/'lecture.json').write_text(json.dumps(spec,indent=2,ensure_ascii=False)+'\n')
(B/'spine.md').write_text('# Lecture 55 teaching spine\n\n'+'\n'.join(f'{i}. {x["title"]}' for i,x in enumerate(S,1))+'\n')
for i,x in enumerate(S,2):
 words=len(re.sub(r'[*_]','', ' '.join(x['body'])).split())
 if not 90<=words<=170:print('WORD COUNT',i,words)
 if len(x['title'])>62:print('TITLE LENGTH',i,len(x['title']),x['title'])
print('Wrote',len(S),'content slides')
