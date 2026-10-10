"""Lecture 63: primary-source teaching prose and original article figures."""
import json,re
from pathlib import Path
D=Path(__file__).resolve().parent;R=D.parents[1];refs=json.loads((D/'references.json').read_text());slides=[]
authors={'noise':'Sørensen et al. (2023)','auditory':'Wong et al. (2022)','cooperation_pmc':'Jaakkola et al. (2018)','reward':'Schultz et al. (1993)','fishlearning':'Pereira et al. (2020)','anticipation':'Clegg et al. (2018)','nofood':'Platto & Serres (2023)','innovate':'Yeater et al. (2024)','enrichment':'Clegg et al. (2023)'}
def fig(k,name,num,description):return {'path':'figures/'+name+'.png','caption':authors[k]+', Fig. '+num+'. '+description,'kind':'article','source_url':'https://doi.org/'+refs[k]['doi']}
F={}
def f(name,k,num,desc):F[name]=fig(k,name,num,desc)
f('dolphin','noise','1(detail)','A bottlenose dolphin wearing an acoustic tag.')
f('noise_setup','noise','1','Lagoon, paired buttons and animal-borne recording tags.')
f('noise_success','noise','2A–B','Cooperation declines as noise exposure increases.')
f('noise_spectrum','noise','2A–B','Frequency composition of the noise treatments.')
f('noise_amplitude','noise','2C–F','Whistle amplitude changes with received noise.')
f('noise_duration','noise','2C–F','Whistle duration changes with received noise.')
f('aep','auditory','2A–B','Auditory responses and their peak latencies.')
f('threshold','auditory','3A–B','Hearing thresholds and noise-induced shifts.')
f('hair_cells','auditory','4A–C','Saccular anatomy, stained hair cells and Ribeye b puncta.')
f('tank_stress','auditory','5A–D','Novel-tank behavior after noise exposure.')
f('partner_setup','cooperation_pmc','1','Paired underwater buttons in the experimental lagoon.')
f('partner_success','cooperation_pmc','2A–B','Task success across partner-release delays.')
f('partner_strategy','cooperation_pmc','3A–C','Swimming time, first presses and interpress timing.')
f('reward_rasters','reward','3A–C','Dopamine spikes during learning and established performance.')
f('reward_omission','reward','4','Reward delivery and omitted-reward responses.')
f('reward_population','reward','5','Population reward responses across learning stages.')
f('midbrain','reward','6A–B','Histological reconstruction of dopamine recording sites.')
f('reward_groups','reward','7','Reward responsiveness in midbrain cell groups.')
f('reward_cue','reward','8(detail)','Responses to instruction, trigger and reward events.')
f('cue_independence','reward','10','Cue responses with different movement requirements.')
f('fish_housing','fishlearning','1A–D','Enriched and impoverished aquarium environments.')
f('fish_maze','fishlearning','2','Visual landmarks in the plus-maze learning task.')
f('fish_brain','fishlearning','3A–D','Tambaqui and dorsal, ventral and lateral brain views.')
f('fish_histology','fishlearning','4A–P','Nissl-stained tectal and telencephalic sections.')
f('fish_learning','fishlearning','5A–C','Growth and acquisition of the spatial task.')
f('fish_cells','fishlearning','6A–B','Cell counts in telencephalon and optic tectum.')
f('cue_sounds','anticipation','1a–c','Sound cues for control, toys and human interaction.')
f('anticipation','anticipation','2','Anticipatory behavior before the three contexts.')
f('participation','anticipation','3a–c','Anticipation and subsequent event participation.')
f('nonfood_participation','nofood','3','Participation in interactions without food reward.')
f('nonfood_responses','nofood','4','Positive and negative responses to trainer presence.')
f('nonfood_latency','nofood','5','Response latency across trainers and seasons.')
f('nonfood_training','nofood','6','Frequency of training activities across seasons.')
f('nonfood_petting','nofood','7','Petting activities across trainers and seasons.')
f('nonfood_play','nofood','8','Play activities across trainers and seasons.')
f('nonfood_wait','nofood','10','Waiting behavior during trainer interactions.')
f('nonfood_playtime','nofood','11','Play duration across trainers and seasons.')
f('innovation_fluency','innovate','1','Correct nonrepeated responses during innovation sessions.')
f('innovation_repetition','innovate','2','Different responses before repetition.')
f('innovation_energy','innovate','3','Energy levels of responses to the innovate cue.')
f('innovation_types','innovate','4','Motor categories used during innovation.')
f('innovation_originality','innovate','5','Original behaviors produced by individual dolphins.')
f('innovation_elaboration','innovate','6','Elaborated responses during innovation sessions.')
f('enrichment_devices','enrichment','1(detail)','Published photographs and descriptions of enrichment devices.')
f('enrichment_engagement','enrichment','4','Engagement scores under both enrichment treatments.')
f('enrichment_training','enrichment','5','Willingness to participate in training.')
f('enrichment_interaction','enrichment','6A–B','Individual and group engagement with devices.')
f('enrichment_welfare','enrichment','7A–G','Behavioral measures across enrichment treatments.')
def add(title,k,images,body,extra):
 paras=body.split('\n\n');assert len(paras)==3,(title,len(paras));words=len(re.sub(r'[*_]','',body).split());assert 90<=words<=170,(title,words)
 keys=[k]
 for name in images:
  for kk in refs:
   if F[name]['source_url'].endswith(refs[kk]['doi']) and kk not in keys:keys.append(kk)
 sd={'title':title,'layout':'figure-right' if len(images)==1 else 'figures-right','body':paras,'cite':'; '.join(authors[kk] for kk in keys),'refs':[refs[kk]['reference'] for kk in keys],'transcript':[re.sub(r'[*_]','',p) for p in paras]+[extra]}
 if len(images)==1:sd['figure']=F[images[0]]
 else:sd['figures']=[F[x] for x in images];sd['primary_figure_height']=2.7
 slides.append(sd)
add('Noise reduces the precision of cooperative action','noise',['noise_success','noise_setup'],'''**Bottlenose dolphins** coordinate their movements and vocal signals during joint activities. Sørensen and colleagues tested this coordination in a lagoon where each animal pressed a separate underwater button. Both presses had to occur within 1 s to produce a shared reward.

Ambient sound provided the control condition. Increasing playback noise and a pressure washer used for lagoon cleaning created louder treatments. Cooperative success fell from 85% under ambient conditions to 62.5% during the highest noise exposure.

**Acoustic masking** occurs when competing sound reduces detection or perception of a signal. The loss of precise coordination links a changed sensory environment to the success of a social task.''','A hydrophone records underwater sound, while the tags record the sound and movement experienced by each dolphin. The experiment therefore pairs an environmental manipulation with a functional behavioral outcome.')
add('Received sound depends on the animal’s position','noise',['noise_spectrum','noise_setup'],'''The sound reaching an animal is its **received noise level**, which can differ from the level measured beside a loudspeaker. Dolphins move through the lagoon, so their exposure changes with their location and orientation during the cooperative task.

Animal-borne acoustic tags recorded the noise experienced just before whistles. The researchers also measured noise beside the buttons over the 1–20 kHz band. Mean levels ranged from about 115 dB re 1 µPa during ambient trials to 150 dB re 1 µPa during pressure-washer trials.

The pressure reference of 1 µPa specifies the underwater measurement scale. Exposure measurements tied to the animal capture the immediate acoustic conditions in which communication occurs.''','Decibels express sound levels relative to a specified reference pressure. The article reports the underwater reference, and its noise spectrum identifies how much sound occupies different frequency bands.')
add('Dolphins raise whistle amplitude in louder noise','noise',['noise_amplitude','noise_setup'],'''A **Lombard response** is an increase in vocal amplitude as background noise rises. Both dolphins increased whistle amplitude when their tags recorded greater noise immediately before vocalization. This response adjusts communication to current acoustic conditions rather than relying on a fixed output.

The adjustment was partial: Reese increased whistle output by about 0.08 dB and Delta by about 0.14 dB for each 1 dB increase in noise. Their signals therefore gained less amplitude than the competing sound gained.

Signature whistles carry individual identity in their frequency contours. Reese’s signature occupied 4–18 kHz and Delta’s 6–20 kHz, placing these communication signals within the frequency range of the experimental noise.''','The output estimate is an apparent output level obtained from the tag recording. Partial amplitude compensation helps explain why louder calling can accompany poorer communication and coordination.')
add('Longer whistles accompany reduced task success','noise',['noise_duration','noise_success'],'''**Whistle duration** is the time over which a dolphin produces a continuous communication signal. During the highest noise exposure, Reese’s whistles averaged 1.85 times their ambient duration and Delta’s averaged 1.66 times their ambient duration.

Delta’s duration increased consistently with received noise, whereas Reese’s responses were more variable. Longer signals provide a temporal adjustment to a noisy environment, alongside the amplitude adjustment measured in both animals.

Cooperative success still declined at the highest exposure. Vocal compensation therefore left a measurable behavioral cost: the animals altered their communication while becoming less successful at aligning their button presses within the required 1 s interval.''','The article measures compensation and joint performance in the same task. An increase in calling effort can be a response to sensory difficulty, so call production and task success provide different information about the animal’s condition.')
add('Noise timing changes hearing sensitivity in fish','auditory',['threshold','hair_cells'],'''**Zebrafish** provide a preparation for measuring how aquarium noise changes hearing. Wong and colleagues exposed adults to white noise at 150 dB re 1 µPa for 24 h, then compared their hearing with fish maintained under control conditions.

Treatments included continuous noise, 1 s noise pulses separated by 1 s silence, and 1 s pulses separated by 4 s silence. Continuous exposure and the faster intermittent treatment produced the largest average threshold shifts, about 13 dB.

An **auditory threshold** is the lowest sound level producing a repeatable response at a tested frequency. A higher threshold means that a stronger sound is required for detection, connecting acoustic exposure to reduced sensory sensitivity.''','The experiment also included irregular intervals. Regularity had less influence than the overall duration of exposure, so the amount of time filled by noise carries a biological effect in this preparation.')
add('Auditory responses become slower after exposure','auditory',['aep','hair_cells'],'''An **auditory evoked potential** is an electrical response recorded after a sound stimulus. Repeated tone presentations allow investigators to measure the response waveform and identify its peak latency, the interval from sound onset to that peak.

After 24 h of noise, zebrafish auditory responses had longer peak latencies than controls. Continuous exposure produced a delay of about 0.5 ms in the study’s comparison. The same treatment also elevated hearing thresholds.

The saccule is an inner-ear sensory organ containing hair cells that receive mechanical stimulation. Slower evoked responses and higher thresholds describe changes in the pathway from sensory stimulation to population electrical activity, complementing the examination of the saccular tissue.''','The stimulus tones lasted 20 ms. Threshold and latency measure distinct properties: one concerns the sound level required to evoke a response, and the other concerns how soon that response develops.')
add('Sensory ribbons change without major hair-cell loss','auditory',['hair_cells'],'''**Hair cells** are sensory cells whose bundles respond to mechanical displacement. In the zebrafish saccule, fluorescent staining identified the bundles and the presynaptic protein Ribeye b. A presynaptic ribbon is a structure associated with neurotransmitter release from a hair cell to its neural target.

Continuous noise reduced the number of Ribeye b puncta, the discrete stained protein clusters, particularly in middle and posterior saccular regions. Counts of hair cells did not differ clearly between exposure groups and controls.

The combination changes the biological interpretation of hearing loss. Sensory transmission can be impaired at the release apparatus even when the sensory cells remain present, linking microscopic synaptic changes with elevated auditory thresholds.''','Phalloidin labels the hair-cell bundles, while an antibody labels Ribeye b. These markers separate the persistence of sensory cells from changes in their presynaptic structures.')
add('Noise exposure increases bottom dwelling','auditory',['tank_stress','hair_cells'],'''**Bottom dwelling** is a zebrafish response to placement in a novel tank. Fish initially remain low in the water column and then explore upper regions as they habituate, meaning that their response diminishes with continued exposure to the unfamiliar setting.

During the first minute, noise-exposed fish spent more than 98% of their time in the bottom zone, compared with about 82% for controls. Their first entry into the upper zone was also delayed, particularly after intermittent noise treatments.

The behavioral effect accompanied altered hearing and presynaptic staining. Noise exposure therefore affected both sensory performance and exploration, two different functions relevant to the conditions experienced by fish in managed aquatic environments.''','The assay measures behavior after exposure rather than sound detection during playback. The vertical trajectories capture how fish distribute their activity within a new environment.')
add('Quiet intervals alter the acoustic exposure dose','auditory',['threshold','hair_cells'],'''The **time regime** of noise describes the pattern of sound and silence across an exposure period. In the zebrafish experiment, a 1 s pulse followed by 4 s of silence imposed less total sound exposure than a 1 s pulse followed by 1 s of silence.

Fast intermittent noise produced hearing shifts closer to continuous noise than to the slower intermittent treatment. Random timing produced fewer frequency-specific threshold changes than the highest-duty treatments, despite also using repeated pulses.

The sensory tissue comparison identified reduced Ribeye b after continuous exposure. Together, the timing and tissue results connect the duration of acoustic stimulation with changes in auditory performance and its presynaptic apparatus.''','All noise treatments lasted 24 h and used the same playback level. Varying the silent intervals changed the pattern of exposure while holding these two features constant.')
add('A partner’s arrival governs cooperative timing','cooperation_pmc',['partner_success','partner_setup'],'''**Cooperation** requires the contribution of more than one individual to a joint outcome. Jaakkola and colleagues trained bottlenose dolphin pairs to press separate underwater buttons within 1 s. A single early press failed to earn the shared reward.

The researchers released partners together or introduced delays of 1–20 s. Dolphins succeeded even when one animal had to wait for the other, connecting its own action to the partner’s opportunity to act.

Random release delays disrupted a fixed rhythm between the trainer’s signal and the button press. Successful timing therefore depended on information about the partner rather than simply repeating a movement sequence at a constant speed.''','The narrow time window made loose overlap between independent actions insufficient. The task required alignment at the buttons after the dolphins crossed the lagoon.')
add('Waiting replaces a rush to catch up','cooperation_pmc',['partner_strategy','partner_setup'],'''Early in the cooperative task, the delayed dolphin swam faster to catch up with its partner. Later, delayed animals swam more slowly while the timing between partners’ button presses became more precise.

The investigators measured swimming time, which animal pressed first, and the interval between presses. As experience accumulated, the animal released first was less likely to be the first to press its button, connecting its response to the delayed partner’s progress.

**Behavioral flexibility** means adjusting an action strategy to current conditions. The dolphins changed from rapid catching up toward coordinated waiting, preserving the shared 1 s response window through improved control of their joint action.''','The strategy measures divide the behavior into travel and action phases. Coordination can be achieved by changing either phase, and individual dolphins used these opportunities differently.')
add('Practice refines subsecond coordination','cooperation_pmc',['partner_strategy','partner_setup'],'''The interval between the dolphins’ button presses became shorter over the study. In the later trials, the average interval was 370 ms, substantially smaller than the 1 s maximum interval permitted for a reward.

This precision emerged in a task where partners sometimes started 1–20 s apart. The first animal had to maintain the opportunity for a joint response while the delayed partner crossed the lagoon.

**Synchrony** is close alignment of actions in time. The animals refined synchrony beyond the task’s minimum requirement, connecting repeated cooperative experience with improved control of the final shared action. Travel adjustments and waiting behavior contributed to maintaining that alignment.''','A 370 ms interpress interval concerns the coordination of two individuals, rather than a single animal’s reaction time. The improvement followed experience with the cooperative contingency.')
add('Social timing depends on the sensory environment','noise',['noise_success','partner_setup'],'''The cooperative button task combines two requirements: each dolphin must perform its own action, and both actions must occur close enough together to satisfy the shared timing rule. Partner-delay experiments established that dolphins can adjust their behavior to this rule.

The noise experiment used the same 1 s window but changed the acoustic environment. Cooperation fell from 85% under ambient conditions to 62.5% under the highest noise exposure, even as whistle amplitude and duration increased.

The behavioral cost connects social coordination with access to communication signals. A task learned successfully in quiet conditions can become harder when competing sound interferes with the information exchanged during its execution.''','Jaakkola and colleagues tested partner roles, while Sørensen and colleagues tested acoustic disturbance. These experiments manipulate different components of a shared cooperative task.')
add('Dopamine neurons respond differently during learning','reward',['reward_rasters','midbrain'],'''**Dopamine** is a neurotransmitter released by specific midbrain neurons. Schultz and colleagues recorded individual neurons in monkeys learning tasks that paired visual instructions and correct movements with liquid reward. Each recorded spike represented an action potential from one neuron.

A **phasic response** is a brief change in firing around an event. Reward delivery activated a larger fraction of dopamine neurons during learning than during established performance, about 25% compared with 9%.

The same reward therefore evoked different neural activity as task relationships became familiar. Reward-related firing depended on the animal’s stage of learning, connecting a cellular signal with the acquisition of predictable behavioral contingencies.''','A contingency is a reliable relationship between an event or action and its outcome. These are monkey single-neuron recordings, which provide the neural preparation for the reward-learning mechanisms discussed here.')
add('Predictive cues recruit dopamine responses','reward',['reward_cue','midbrain'],'''A **conditioned stimulus** acquires significance through its association with another event. In the monkey tasks, an instruction cue identified the movement target and a later trigger cue indicated when the animal could make the rewarded response.

Dopamine neurons responded to these visual cues during established performance. The earliest reward-relevant instruction frequently evoked stronger responses than the later trigger, while reward delivery itself activated fewer neurons than it had during learning.

Neural responsiveness therefore became organized around events that supplied information about the upcoming reward. The sensory cue preceded the action and outcome, allowing reward-related activity to occur before consumption rather than only after liquid reached the animal.''','The instruction and trigger served different functions within the task. Their separation allows the sensory prediction of a reward to be distinguished from the permission to execute the movement.')
add('Reward omission suppresses expected-time firing','reward',['reward_omission','midbrain'],'''When a monkey made an incorrect response, the expected liquid reward was omitted. Dopamine neurons that responded to reward in successful trials showed a depression of activity near the time when reward would normally arrive.

The comparison separated the action from the outcome: touching a lever was not sufficient to evoke the reward response. Activity depended on whether liquid was delivered after the task event and on the expectation established by previous trials.

An **omission response** is a neural change when a predicted event fails to occur. The timed decrease in firing connects learned expectation with a negative outcome, rather than treating dopamine activity as a simple response to movement.''','The reward apparatus and solenoid events were examined separately in the recording comparison. Depression during unrewarded error trials occurred around the expected outcome time.')
add('Midbrain populations differ in reward responsiveness','reward',['reward_groups','midbrain'],'''The recorded dopamine neurons occupied several midbrain cell groups, designated A8, A9 and A10. Histological reconstruction located recording sites in relation to the substantia nigra and neighboring structures after the behavioral experiments.

**Histology** is the microscopic examination of tissue structure. Mapping responsive and nonresponsive neurons back onto tissue sections associated their activity with specific anatomical locations. During learning, reward responsiveness was greater in A10 than in the other recorded groups.

The population comparison links anatomical organization with event-related neuronal activity. Dopamine neurons share a transmitter identity, yet their responses vary across locations and across learning stages, providing differentiated signals during reward-guided behavior.''','The coronal sections include a 2 mm scale bar and named landmarks. A cell’s anatomical location and its event response are distinct measurements combined by reconstruction of the recording sites.')
add('Cue responses are not a copy of the movement','reward',['cue_independence','midbrain'],'''The monkey tasks varied which movement followed a visual event. Schultz and colleagues compared dopamine activity across conditions with different movement requirements, including task events followed by reaching and events without the same motor response.

The neurons’ cue responses were associated with the learned significance of the stimulus rather than a simple one-to-one copy of a particular movement. The instruction could recruit a brief response even though the animal still had to wait before acting.

**Sensorimotor control** converts sensory information into organized movement. These dopamine recordings separated a reward-relevant sensory event from the motor execution that followed, connecting neuronal activity to the information supplied by the cue.''','The study also varied movement laterality and timing. Cue-related activation and subsequent motor behavior were therefore compared across more than one action pattern.')
add('Brief dopamine signals differ from holding a memory','reward',['reward_cue','midbrain'],'''In the delayed-response task, a monkey received an instruction and then waited before making its response. The delay separated information about the target from the opportunity to reach and obtain the liquid reward.

Dopamine neurons produced brief responses around task events rather than sustained increases throughout the waiting period. **Sustained activity** persists over an interval; phasic activity is concentrated around a particular change or event.

The temporal pattern assigns dopamine activity a different role from continuously holding the target location in memory. Cue and outcome responses marked reward-relevant events while behavior required the target information to remain available across the delay.''','The lack of persistent delay firing is a specific result that changes the interpretation of the recorded neurons. Their brief signals should not be equated with the maintained spatial representation required for the later response.')
add('Aquarium complexity changes opportunities for learning','fishlearning',['fish_housing','fish_brain'],'''**Environmental enrichment** adds opportunities for species-relevant activity beyond basic housing. Pereira and colleagues maintained juvenile tambaqui, _Colossoma macropomum_, for 192 days in enriched or impoverished aquaria before testing learning.

The enriched aquarium contained natural plants, a shelter object and a water stream operating for 12 h each day. The comparison aquarium lacked these additions, while both environments provided filtration, food and a regular light-dark cycle.

Plants and shelter changed the spatial setting, while running water offered voluntary exercise. Fish from the enriched environment subsequently learned the experimental task faster, linking prolonged differences in daily sensory and motor experience with later performance in a new learning apparatus.''','The enriched treatment combined several opportunities rather than manipulating one isolated feature. The experiment measured the response to that housing package, including growth, behavior and brain tissue.')
add('Enriched fish acquire landmark-guided choices faster','fishlearning',['fish_learning','fish_maze'],'''An **allocentric cue** identifies a location through features of the environment rather than through the animal’s current body orientation. In the tambaqui plus maze, visual squares and circles marked different arms, allowing fish to learn a relationship between landmarks and food.

Fish raised in enriched aquaria acquired the task faster than fish from impoverished housing. After 30 training sessions, more than half of the enriched fish reached the learning criterion, compared with fewer than 30% of the comparison fish.

The landmarks supplied information for choosing an arm. Repeated rewarded choices connected that sensory information to movement through the maze, converting environmental experience into a stable behavioral preference.''','The test took place in a third aquarium, distinct from either housing environment. The performance difference therefore concerned learning in the test apparatus following prolonged exposure to contrasting homes.')
add('Telencephalic cell counts track housing experience','fishlearning',['fish_cells','fish_brain'],'''The **telencephalon** is the anterior division of the brain, consisting of paired hemispheres in these fish. Pereira and colleagues compared its total cell number with that of the optic tectum, a dorsal midbrain structure involved in visuomotor processing.

**Stereology** estimates tissue quantities by systematically sampling sections. The enriched fish had more telencephalic cells than the impoverished fish, whereas total cell counts in the optic tectum did not differ clearly between treatments.

The region-specific result connects prolonged environmental experience with brain organization. The counting method included neurons and glia, so the increase describes total cellular population rather than identifying a particular neuronal class as the source of the difference.''','The tissue sections were stained with Nissl methods that make cell bodies visible. The paper’s anatomical views identify the two sampled regions before their cell counts are compared.')
add('Learning and cellular plasticity develop together','fishlearning',['fish_histology','fish_brain'],'''**Plasticity** is a lasting change in biological organization or function associated with experience. In the tambaqui experiment, 192 days of enrichment preceded faster maze learning, greater body growth and a larger telencephalic cellular population.

Nissl-stained sections identified cell bodies in the telencephalon and optic tectum. The regional contrast was selective: higher total cell counts occurred in the telencephalon while tectal counts remained similar across housing treatments.

Whole-brain RNA measurements also identified differentially expressed transcripts, meaning that some gene products were represented at different levels between treatments. Behavioral performance, tissue organization and gene expression supplied complementary measurements of the response to a prolonged change in the environment.''','The cell-count method combines neurons and glia, and the RNA analysis used whole brain. These measures describe different levels of plasticity without assigning the behavioral effect to one newly generated cell type.')
add('Sound cues acquire event-specific significance','anticipation',['cue_sounds','dolphin'],'''**Classical conditioning** links a sensory cue with an event that follows it. Clegg and colleagues used different underwater sounds to announce toys, interaction with a familiar trainer, or a control context for bottlenose dolphins.

Each event began after a 5 min delay and remained available for 10 min. Supplementary visual cards accompanied the sounds. The delay allowed observers to measure behavior before the event itself could attract the dolphins.

Animals performed more anticipatory behavior before toys and human interaction than before the control context. The association gave each cue information about a particular future opportunity, producing an observable response in the interval between prediction and access.''','The sounds were presented at 130 dB re 1 µPa and had been checked for audibility across the pools. The animal photograph is from Sørensen’s separate dolphin study; the cue data come from Clegg’s conditioning experiment.')
add('Surface looking is directed toward expected events','anticipation',['anticipation'],'''**Anticipatory behavior** occurs before an expected event and prepares an animal to engage with it. In the dolphin study, surface looking and spy hopping were measured during the 5 min after a cue and before access to the announced context.

Surface looking oriented the animal toward the area where the event would appear. Spy hopping raised the head above the water. These behaviors were more frequent before toys and familiar-trainer interactions than before the control context.

The event-specific difference separates anticipation from general activity elicited by any sound. The dolphins directed behavior toward a predicted opportunity while the opportunity itself was still absent, connecting learned cues to prospective motivation.''','The control had its own cue and delay. This comparison retained the announcement procedure while changing whether a rewarding interaction or set of objects would follow.')
add('Familiar human interaction elicits strong anticipation','anticipation',['anticipation','dolphin'],'''A **human-animal interaction** in the experiment involved a familiar trainer approaching the pool and playing with dolphins. The event provided social contact without using food as the immediate reward within that context.

Dolphins showed greater anticipation before this interaction than before toy provision. Both contexts elicited more anticipation than the control, but the human event recruited the stronger pre-event response during the 5 min waiting interval.

The comparison identifies differentiated motivation among opportunities available in managed care. Social interaction and object play were both attractive, while their relative anticipatory responses varied. The animals’ behavior therefore supplied information about which event they expected and how strongly they approached that opportunity.''','The trainers were familiar caretakers rather than unfamiliar visitors. The result concerns established trainer relationships in this setting, and the study separately measured participation once the trainer arrived.')
add('Anticipation predicts engagement with toys and people','anticipation',['participation'],'''The researchers compared behavior before each event with participation during the following 10 min. Participation included time spent attending to, investigating or contacting the toy or familiar human, rather than only counting physical touches.

Higher anticipatory behavior predicted greater subsequent engagement with both toys and people. The pre-event response was therefore connected to the animal’s later use of the announced opportunity.

**Motivation** organizes behavior toward an available outcome. The relationship between waiting behavior and later engagement places anticipation within that behavioral sequence: a cue identifies an opportunity, the animal orients toward it, and then spends time interacting after access begins. Both phases contributed evidence about event-specific interest.''','The observation definition included focused attention near the person or object, with contact optional. This prevents active investigation from being excluded simply because the animal did not touch the target.')
add('Leaving a feeding session measures participation','anticipation',['participation'],'''Dolphins could swim away during food-reinforced training sessions without punishment. The investigators counted these voluntary breaks as a participation measure and related them to anticipation during the 5 min before the session began.

A break involved moving more than 2 m from the trainer and remaining away for more than 5 s. Higher anticipation was associated with fewer breaks per minute, connecting a stronger pre-session response with greater persistence once feeding began.

Participation reflected a choice among available activities. Toys, other dolphins and other pool locations remained possible alternatives, so continued proximity to the trainer described how behavior was allocated during a rewarding event rather than merely whether the dolphin performed a trained action.''','The study normalized breaks by session duration. Food-session anticipation was based on the dolphins’ established daily schedule and associated cues, rather than the novel cue-conditioning protocol used for toys and human interaction.')
add('Dolphins approach trainers without food reward','nofood',['nonfood_participation','dolphin'],'''At Dolphin Reef in Eilat, trainer interactions were separated from food delivery. Platto and Serres observed dolphins approaching caretakers on platforms or in the water during activities that could include play, petting and training without food rewards.

Dolphins participated in 94.5% of the recorded interaction sessions. Their responses were usually rapid, and animals often arrived at the interaction site before or as a trainer appeared.

The **nonfood context** separates immediate feeding from the social opportunity. Participation in this setting connects caretakers’ presence with interaction itself, supplying a behavioral measure of attraction that can be examined alongside studies where food and human attention arrive together.''','This was an observational study of established relationships. The separation of food and trainer interactions was part of the facility’s routines, allowing approach behavior to be measured without immediate food reinforcement.')
add('Arrival latency captures spontaneous engagement','nofood',['nonfood_latency','dolphin'],'''**Response latency** is the interval between an event and the animal’s response. In the nonfood trainer-interaction study, it measured how quickly dolphins arrived after caretakers appeared or signaled from a platform or the water.

Responses were usually shorter than 1 min, and dolphins often arrived before a formal call. Both called and uncalled interactions therefore attracted animals within the same general setting.

Arrival before a signal connects participation to the broader context surrounding the caretakers, including their visible approach and the ongoing routine. Measuring latency adds a temporal dimension to participation: an animal may attend an interaction frequently, approach promptly, or vary these two features independently.''','The figures divide responses by trainer and season. This retains individual relationship and context information rather than reducing every interaction to one facility-wide response rate.')
add('Play materials change trainer-interaction participation','nofood',['nonfood_play','nonfood_playtime'],'''Play opportunities formed part of the nonfood interactions at Dolphin Reef. The presence of toys was associated with more frequent participation by dolphins, connecting the material offered during a session with the animals’ decision to approach.

Observers distinguished playing from petting, trained activities and waiting. They also measured play duration, preserving the difference between joining an interaction and continuing to engage once it began.

**Object play** involves interaction with a material that is not immediately used to obtain food. In this setting, toys altered the opportunities available during human contact. Participation and duration therefore described different aspects of the same social and exploratory activity, without requiring immediate food delivery.''','The study classified several types of trainer-dolphin activity. Keeping those categories separate allows a change in play to be distinguished from a change in all interactions combined.')
add('Trainer relationships differ among individuals','nofood',['nonfood_responses','nonfood_petting'],'''Different caretakers elicited different participation patterns during the nonfood sessions. Some dolphins approached particular trainers more often, while interaction categories such as petting and play also varied across trainer relationships.

The study recorded **individual differences**, persistent or repeated differences among animals observed within a shared environment. These differences affected how much each dolphin used available human contact and how promptly it approached an interaction.

A group-level participation rate therefore combines several distinct relationships. The same opportunity can be used differently by different animals, connecting the social environment to individual behavioral choices. Monitoring named dolphins and named caretakers preserves that relationship information during routine welfare assessment.''','The observations also considered potential health and personality influences on individual participation. A change relative to an animal’s own usual pattern can be more informative than its rank compared with every other dolphin.')
add('Participation changes across daily and seasonal contexts','nofood',['nonfood_training','nonfood_wait'],'''Dolphin participation in nonfood trainer interactions varied with time of day and reproductive context. More animals participated during morning sessions and during the neutral season, when mating activities and births were absent.

These observations connect human interaction with the animals’ broader activity schedule. Reproductive and social activities supply competing opportunities, so a dolphin’s allocation of time can change even when familiar caretakers remain available.

**Diel variation** is variation across the daily cycle. Diel and seasonal patterns identify recurring contexts for engagement, allowing a participation record to be interpreted against when the interaction occurred and what other activities were occurring in the same environment.''','Neutral season is the article’s term for the interval without mating and birth activity. The study did not use a low participation score as a diagnosis by itself; it compared patterns across the recorded contexts.')
add('An innovate cue rewards nonrepeated behavior','innovate',['innovation_fluency'],'''Yeater and colleagues studied an **innovate cue**, a trainer gesture that requested a behavior different from those already produced in the current session. The dolphin chose the response rather than receiving an instruction for a specific movement.

Food reinforcement followed acceptable nonrepeated responses. Repeating an earlier response counted as an error, making the relationship between the animal’s recent actions and its current choice part of the task.

**Fluency** describes the production of acceptable different responses. The rule encouraged dolphins to select from their behavioral repertoire while tracking what they had already performed. Reward was therefore contingent on variation, connecting a training procedure with flexible selection rather than repetition of one specified act.''','The investigators evaluated fluency, flexibility, originality and elaboration separately. Each measure captured a different feature of the response sequence under the same innovate instruction.')
add('Different motor categories contribute to flexibility','innovate',['innovation_types','innovation_energy'],'''**Flexibility** concerns the range of categories used in a response sequence. In the dolphin innovation study, behaviors were classified by motor form and energy level, allowing variation across kinds of movement to be distinguished from repeated use of one category.

A dolphin could produce several acceptable different acts while remaining within a narrow category, or distribute responses across more kinds of action. The recorded profiles varied among individuals, even though they received the same innovate instruction.

Motor-category and energy classifications describe how animals organize their choices. They connect the behavioral repertoire to the demands of the training contingency, separating the number of different acts from the breadth of the actions selected.''','The article’s categories are operational definitions used to score observable responses. They describe variation in performance rather than assigning an unmeasured neural process to a particular movement.')
add('Originality and elaboration are distinct outcomes','innovate',['innovation_originality','innovation_elaboration'],'''**Originality** measures the production of responses classified as novel, while **elaboration** concerns responses that extend or combine behavioral components. These dimensions distinguish creating a new response from modifying the complexity of an existing one.

Some dolphins produced original behaviors during the innovate sessions, and the amount of elaboration varied among individuals. Animals could therefore differ in more than their rate of correct nonrepeated responses.

The task permitted the animal to choose how to satisfy a reward contingency. Comparing originality with elaboration connects that choice to the organization of the response itself, preserving distinct kinds of behavioral variation rather than collapsing every different act into a single creativity score.''','The researchers developed scoring definitions before comparing individuals. Novelty, complexity and correct variation were measured as separate constructs, so high performance on one dimension did not automatically imply high performance on every dimension.')
add('Response diversity depends on the current contingency','innovate',['innovation_repetition','innovation_energy'],'''An **operant contingency** links the consequence of an action to the action performed. In innovation training, reinforcement depended on producing a response that had not already occurred in the session, making the recent behavioral sequence relevant to reward.

The number of different responses before a repetition varied among dolphins and across sessions. Response-energy categories also differed, separating diversity of choice from the physical intensity of the actions selected.

This training arrangement offers a contrast with rewarding a fixed behavior every time. The dolphin must vary its output while retaining the shared rule, connecting reinforcement with flexible behavioral production and the use of an individual repertoire.''','The experiment reported variation in the length and composition of response sequences. Diversity therefore describes the pattern generated under this contingency rather than a requirement that every response be a newly invented movement.')
add('Cognitive foraging changes how food is acquired','enrichment',['enrichment_devices'],'''**Cognitive foraging enrichment** requires an animal to solve a problem to obtain food. Clegg and colleagues compared devices containing hidden fish with simpler enrichment items that provided fish without the same problem-solving requirement.

The treatments alternated weekly over 8 weeks. Both received comparable food quantities, including 0.1–0.2 kg of fish per animal per day during enrichment. Animals were familiar with the devices before the experiment, reducing novelty as the central difference.

The comparison changed the route to a reward while maintaining its food value. Finding and extracting hidden fish supplied opportunities for investigation and goal-directed action, connecting enrichment design with how dolphins controlled the acquisition of a resource.''','The daily schedule included approximately 1 h of morning enrichment and 2 h in the afternoon. Devices were rotated, and several copies were often available to reduce competition.')
add('Problem-solving devices sustain greater engagement','enrichment',['enrichment_engagement','enrichment_devices'],'''Caretakers scored each dolphin’s engagement with enrichment devices, while independent observations measured interaction during the treatment weeks. Dolphins engaged more with cognitive foraging devices than with the simpler non-cognitive items.

**Engagement** included sustained involvement with the opportunity, rather than merely whether an item was present in the pool. Hidden food required the animal to investigate and act on the device before obtaining the reward.

The food-matched comparison connects stronger engagement with the structure of the activity. Comparable fish provision accompanied different behavioral use of the devices, indicating that the process of acquiring food contributed to how dolphins allocated their time during enrichment.''','The study combined caretaker ratings with direct behavioral sampling. These methods addressed the same treatment comparison through different observation procedures, preserving both overall engagement and recorded interaction behavior.')
add('Enrichment also changes later training motivation','enrichment',['enrichment_training'],'''**Willingness to participate** was a caretaker rating of each dolphin’s motivation during training sessions. These sessions were measured separately from enrichment, allowing the researchers to examine whether treatment differences extended beyond contact with the devices themselves.

During cognitive enrichment weeks, dolphins received higher training-participation scores than during non-cognitive weeks. The positive change occurred alongside increased engagement with the problem-solving devices.

The response therefore involved more than occupying an animal during an enrichment session. The weekly pattern connected cognitive foraging opportunities with motivation in another activity, while comparable food provision across treatments helped separate the activity design from the amount of enrichment food supplied.''','Training and enrichment ratings were collected in distinct events. A caretaker who scored training was not simultaneously scoring the enrichment interaction in that same session.')
add('Lower anticipation can accompany stronger motivation','enrichment',['enrichment_welfare','enrichment_training'],'''During cognitive enrichment weeks, dolphins displayed less anticipatory behavior but greater willingness to participate in training. These changes occurred together, despite anticipation predicting participation within specific events in the earlier conditioning study.

The comparisons address different scales. One measured how strongly a dolphin anticipated a particular announced event; the other altered opportunities across a week and measured behavior among those activities.

The authors’ **reward-sensitivity hypothesis** proposes that limited rewarding opportunities can amplify anticipation of the available events. Providing additional cognitive opportunities can therefore reduce disproportionate waiting behavior while maintaining or increasing motivation when training occurs, connecting anticipation to the wider distribution of rewarding experiences.''','The hypothesis concerns the relationship between reward availability and anticipation, rather than a claim that every anticipatory response indicates poor welfare. Event-specific prediction and the weekly activity environment have to be considered together.')
add('Cognitive enrichment reduces repetitive behavior','enrichment',['enrichment_welfare','enrichment_interaction'],'''A **stereotypy** is a repetitive, relatively invariant behavior with no obvious immediate function. Dolphins expressed less stereotypic behavior during cognitive enrichment weeks than during the food-matched non-cognitive weeks in the study.

The researchers also recorded play, social behavior, pattern swimming and anticipation. These measures did not all change in the same way, preserving a behavioral profile rather than treating any increase in activity as equivalent to improved welfare.

Reduced stereotypy accompanied greater enrichment interaction and higher training motivation. This combination connects problem-solving opportunities with several components of behavior, giving stronger grounds for evaluating an intervention than a change in one response considered alone.''','The overall stereotypy frequencies were low in this group. Pattern swimming was tracked separately from stereotypy, and the intervention did not produce an identical effect across every behavior category.')
add('Participation and sensory access require separate measures','noise',['noise_success','enrichment_training'],'''A dolphin’s success in a trained activity depends on access to the information needed for that activity as well as on its motivation to participate. In the cooperation experiment, noise reduced successful coordination despite changes in whistle production.

Cognitive enrichment increased willingness to participate in separate training sessions. This result concerns engagement, whereas the noise result concerns the sensory conditions supporting precise joint performance.

**Neuroethical evaluation** considers how management practices affect animals’ sensory, cognitive and behavioral lives. The two experiments support evaluating both access to communication and opportunities for motivated activity: a participation measure and a task-success measure identify different effects of the managed environment.''','The ethical inference here concerns which measured functions should be included in an evaluation. It does not require equating successful task performance with the animal’s entire welfare state.')
add('Choice-rich care is evaluated through behavioral profiles','enrichment',['enrichment_welfare','nonfood_participation'],'''The enrichment and nonfood-interaction studies measured how dolphins used opportunities for foraging, play and human contact. Cognitive devices increased engagement and training motivation while reducing stereotypy; nonfood sessions attracted participation even without immediate feeding.

**Agency** refers to an animal’s opportunity to influence its own actions and access to outcomes. Choosing a response, approaching a familiar caretaker, or investigating a foraging device involves different forms of behavioral control within managed care.

The empirical changes support evaluating the range and quality of these opportunities alongside repetitive behavior and social engagement. Ethical judgments about training and performance can then use a behavioral profile that includes voluntary approach, sustained activity and the sensory conditions necessary for communication.''','The studies provide measured outcomes for specific management practices. Agency is the evaluative concept used here to organize those opportunities, while the behavioral results remain tied to the original interventions and observation settings.')
assert len(slides)==44,len(slides)
items=[('Acoustic access','Noise reduced dolphin cooperation even when animals increased whistle amplitude and duration.'),('Sensory transmission','Zebrafish hearing changed with exposure timing and presynaptic Ribeye b, without clear major hair-cell loss.'),('Reward learning','Monkey dopamine responses depended on learning stage, predictive cues and expected-reward omission.'),('Motivation in context','Anticipation predicted participation in specific events, while additional cognitive opportunities reduced anticipation across weeks.'),('Behavioral choice','Nonfood social contact and innovation contingencies recruited participation and varied responses.'),('Evidence for management','Food-matched cognitive enrichment increased engagement and training motivation while reducing stereotypy; several measures are needed to evaluate its effects.')]
spec={'lecture':63,'theme':'graphite-mist-paper','content_slides':44,'title_height':4.65,'title_image':F['dolphin'],'title_refs':[refs['noise']['reference']],'slides':slides,'takeaways':{'items':[{'lead':l,'text':t} for l,t in items],'cite':'Sørensen et al. (2023); Wong et al. (2022); Schultz et al. (1993); Clegg et al. (2018, 2023); Yeater et al. (2024); Platto & Serres (2023)','refs':[v['reference'] for v in refs.values()]}}
(D/'lecture.json').write_text(json.dumps(spec,indent=2,ensure_ascii=False)+'\n')
p=R/'course/themes.json';themes=json.loads(p.read_text());themes['palettes']['graphite-mist-paper']={'label':'graphite / mist white','title_bg':'45515C','title_text':'FFFFFF','title_muted':'DEE3E8','bg':'FFFFFF','heading':'2F3942','text':'000000','muted':'000000','tint':'F1F3F5','accent':'45515C','rule':'CDD4DA'};p.write_text(json.dumps(themes,indent=2,ensure_ascii=False)+'\n')
print('Wrote 44 teaching slides')
