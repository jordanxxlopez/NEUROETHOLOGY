"""Broad comparative Lecture 78; original published figures and verified sources."""
from pathlib import Path
import json,re
B=Path(__file__).resolve().parent
R=json.loads((B/'research.json').read_text());F=json.loads((B/'figure_sources.json').read_text());S=[]
AUTH={'classic':'Panksepp and Burgdorf','somatosensory':'Ishiyama and Brecht','pag':'Gloveli et al.','apes':'Davila Ross et al.','mice_hamsters':'Dagher et al.','bonobo_tickling':'Demuru et al.','bonobo_optimism':'Winkler et al.','dogs':'Palagi et al.','wolves':'Byosiere et al.','dog_horse':'Maglieri et al.','dolphins':'Maglieri et al.','elephants':'Cordoni et al.','kea':'Schwing et al.'}
YEAR={'classic':2000,'somatosensory':2016,'pag':2023,'apes':2009,'mice_hamsters':2026,'bonobo_tickling':2025,'bonobo_optimism':2025,'dogs':2015,'wolves':2016,'dog_horse':2020,'dolphins':2024,'elephants':2025,'kea':2017}
def short(k):return AUTH[k]+' ('+str(YEAR[k])+')'
def fig(n):
 x=F[n];return {'path':'figures/'+n+'.png','kind':'article','caption':short(x['paper'])+', Fig. '+x['figure']+'. '+x['description']+'.','source_url':'https://doi.org/'+R[x['paper']]['doi']}
def add(title,keys,imgs,text,note):
 body=text.strip().split('\n\n');assert len(body)==3;assert len(title)<=62,title
 keys=list(dict.fromkeys(keys+[F[n]['paper'] for n in imgs]));z={'title':title,'body':body,'transcript':[re.sub(r'\*\*','',p) for p in body]+[note],'cite':'; '.join(short(k) for k in keys),'refs':[R[k]['reference'] for k in keys],'figure_width':5.8,'taxa':[]}
 if len(imgs)==1:z.update(layout='figure-right',figure=fig(imgs[0]))
 else:
  z.update(layout='figures-right',figures=[fig(n) for n in imgs],primary_figure_height=2.2)
  if imgs[0] in ('s_neural','p_block'):z.update(figure_arrangement='side-by-side',primary_figure_width=3.5)
  if imgs[0]=='cmp_bonobo_direction':z.update(figure_arrangement='side-by-side',primary_figure_width=2.8)
 S.append(z)
add('Tickling responses differ across animals',['mice_hamsters','apes'],['cmp_bonobo_photo','cmp_mouse_response'],'''
**Tickling** is repeated tactile stimulation delivered by another individual. In humans and great apes, vigorous playful contact can evoke laughter-like vocalizations. Comparative experiments also examine calling, approach, and voluntary pursuit in rodents, because a vocal response alone provides an incomplete description of the interaction.

Dagher and colleagues compared selectively tame mice, unselected mice, and golden hamsters. Tame mice emitted more ultrasonic calls during tickling and pursued the experimenter’s hand. Hamsters showed little hand-directed play while engaging actively with other hamsters.

**Conspecific** interactions involve members of the same species; **heterospecific** interactions involve different species. A response to human touch therefore depends on both the animal and its relationship with the partner. Strong conspecific play can coexist with weak human-directed tickling responses.
''','The final 2026 publication distinguishes minimal hamster human-directed play from robust hamster–hamster interaction. The same manual procedure is not a universal assay of positive affect across species.')
add('Play signals provide different evidence from tickling',['dogs','dolphins','kea'],['cmp_dolphin_display','cmp_kea_calls'],'''
A **play signal** is a behavior exchanged during playful interaction that can influence a partner’s response. Dogs exchange relaxed open-mouth displays and bows; dolphins exchange open-mouth displays; kea produce a characteristic warble during play. These studies measure communication rather than responses to experimental tickling.

**Behavioral contagion** occurs when observing or hearing another animal increases a related behavior in the receiver. Kea started new play during warble playback. Dolphins more often matched an open-mouth display when they could see its sender.

**Positive affect** refers to a favorable emotional state. Investigators infer it from converging behavioral or cognitive measures. Play contagion, rapid matching, and direct tickling are related comparisons, but they measure different processes. Calling each animal ticklish would collapse these distinct findings into an unsupported claim.
''','Emotional contagion is the hypothesis that a receiver shares an affective state, whereas behavioral contagion is the observable change in behavior. The dog, dolphin and kea studies do not apply a standardized tickling stimulus.')
add('Rats voluntarily seek playful tactile contact',['classic'],['classic_approach'],'''
Young rats emit **ultrasonic vocalizations**, sounds above the human hearing range, during playful manual tickling. Panksepp and Burgdorf studied calls near **50 kHz**, or 50,000 cycles per second, together with movements toward or away from the experimenter.

Rats could leave a protected chamber to receive tickling and return to stop contact. Individually housed animals approached sooner and avoided contact less during reinforced testing than socially housed animals. Before reinforcement began, the groups had similar emergence latencies during habituation.

A **reinforcer** is a consequence that increases the behavior producing it. During extinction, when approach no longer produced tickling, previously reinforced animals retained differences in contact seeking. Learned approach and escape choices connect the tactile interaction with motivation beyond the immediate production of a call.
''','The bell-jar opening allowed animals to end the interaction. Vocal production, approach and avoidance were separate measurements. Greater calling after isolation should not be treated as proof that isolated housing improves welfare.')
add('Rat trunk cortex links touch with vocal activity',['somatosensory'],['s_neural','s_anatomy'],'''
The **somatosensory cortex** processes bodily sensory input; its trunk region represents the torso. Ishiyama and Brecht recorded extracellular spikes, brief electrical events associated with neuronal action potentials, while rats received gentle touch, vigorous tickling, and opportunities to pursue a hand.

Many neurons increased their **firing rate**, the number of spikes per second, during tickling. Some responses persisted after contact stopped, and activity during hand chasing covaried with tickling responses. Trunk cortical activity therefore tracked both contact and playful engagement.

Electrical stimulation of deeper cortical sites could evoke ultrasonic calls, including after 50–100 ms stimulation trains. Stimulation supplies causal evidence that recruiting this tissue can drive vocal output. Anxiety-provoking bright, elevated conditions reduced both tickling-related calling and cortical responses, linking tactile processing with behavioral state.
''','Deep-layer stimulation was more effective than superficial stimulation. Natural responses were recorded during behavior, and the published stained section localizes the trunk cortex; stimulation establishes sufficiency rather than a complete vocal-production pathway.')
add('Rat midbrain inhibition reduces playful engagement',['pag'],['p_block','p_anatomy'],'''
The **periaqueductal gray**, or PAG, is midbrain tissue surrounding the cerebral aqueduct, a fluid-filled passage. Gloveli and colleagues tested its role by injecting muscimol and comparing behavior with saline treatment during tickling and pursuit of the experimenter’s hand.

Muscimol activates **GABA-A receptors**, receptor-controlled ion channels responsive to the inhibitory transmitter gamma-aminobutyric acid. These channels primarily conduct chloride ions, increasing inhibitory conductance and reducing the likelihood of action potentials. PAG inhibition reduced ultrasonic calling and hand chasing, affecting tactile interaction and active pursuit together.

PAG neurons had diverse responses to touch and play, with strongly excited play-responsive cells concentrated laterally. Selective light-driven inhibition of lateral play-responsive tissue also reduced conspecific rough-and-tumble play. The midbrain contribution extends beyond contact with a human hand to interaction with another rat.
''','The selective manipulation used ArchT, a light-activated outward proton pump that reduces neuronal excitability, with GFP controls. Some ventral-tickling calls remained after muscimol, so PAG inhibition reduced rather than eliminated the entire repertoire.')
add('Selection for tameness changes mouse tickling responses',['mice_hamsters'],['cmp_mouse_response'],'''
**Active tameness** is a tendency to approach a human hand rather than avoid it. Dagher and colleagues compared mice selectively bred for this trait with unselected controls from the same wild-derived stock. Juvenile males received the same daily interaction sequence.

Each session separated dorsal tickling, gentle dorsal touch, and no-contact hand pursuit. Interaction phases lasted 15 s, with breaks between them. Tame mice increased ultrasonic calling around tickling onset, while unselected mice showed little corresponding ultrasonic response.

Audible calls increased at contact onset in both groups, and the group difference was especially prominent for ultrasound during tickling. Selection therefore changed a particular behavioral and acoustic response rather than every consequence of handling. Gentle touch and hand pursuit supplied distinct comparisons for the tactile effect.
''','These animals belonged to generation 34 of selection for active tameness. The result concerns this selected stock, not an assertion that every mouse strain responds similarly. The animals could move in the arena between contacts.')
add('Mouse call patterns separate contact from pursuit',['mice_hamsters'],['cmp_mouse_calls','cmp_mouse_context'],'''
A **spectrogram** represents sound frequency over time, with intensity encoded by brightness or color. Mouse recordings contained a high-frequency ultrasonic band and lower-frequency audible calls. Separating these outputs allowed the investigators to compare distinct acoustic responses to the same interaction.

Tame mice produced more ultrasonic calls than controls during dorsal tickling. The groups showed no comparable difference during gentle dorsal touch or the no-contact pursuit phase. Audible call rates also lacked the same consistent difference between selected and unselected animals.

Calling and movement therefore varied independently across conditions. Tame mice pursued the hand without the elevated ultrasound characteristic of physical tickling. Rats can call during both tickling and pursuit, whereas the selected mouse response was more closely tied to tactile contact.
''','The original figure retains frequency in kHz and a 50 ms scale. The paper distinguishes audible calls from ultrasound rather than assigning every sound to a positive emotional state. The mouse–rat comparison is explicitly discussed by the authors.')
add('Tame mice pursue the hand without being touched',['mice_hamsters'],['cmp_mouse_chase'],'''
During the no-contact phase, the experimenter moved a hand through the arena without touching the animal. **Hand pursuit** measured voluntary movement toward that social stimulus, providing a behavioral comparison with calling during imposed tactile contact.

Tame mice spent approximately half of the available pursuit time following the hand, compared with approximately one-third for unselected controls. The hand was present in both conditions, and both groups could approach or disengage. The difference concerned sustained engagement with the moving stimulus.

Selected mice also had a lower overall stereotyped jump rate. Approach, jumping, and calling were separately recorded components of the response. Increased pursuit together with tickling-associated ultrasound supports the authors’ interpretation of enhanced human-directed playfulness, with different components expressed during different interaction phases.
''','The figure reports chasing time as a percentage. One sentence in the article labels the accompanying numerical values in Hz, but the axis, methods and discussion consistently describe the measure as time percentage; the slide uses the correct time-based interpretation.')
add('Tame mouse play extends to conspecific partners',['mice_hamsters'],['cmp_mouse_contact','cmp_mouse_social_calls'],'''
Selection for human approach also changed mouse–mouse interactions. The investigators paired animals from the same breeding group in freely moving sessions, introducing a new partner across tests. Tame pairs spent more time in reciprocal bodily and facial contact than unselected pairs.

**Reciprocity** means that both partners contribute to the interaction. Sudden, exaggerated movements and repeated non-aggressive contacts accompanied tame-mouse encounters. Unselected pairs had fewer such exchanges and more agonistic behavior, meaning behavior associated with conflict.

Ultrasonic calling increased during several partner-contact categories in tame pairs. Audible calling did not follow the same consistent pattern. The behavioral and acoustic differences extended across human and conspecific contexts, while call slope and duration differed between those contexts even when principal ultrasonic frequency was similar.
''','Individual callers could not be identified in paired sessions, so calling is described at the pair or group level. Mounting did not differ clearly between groups; the contact-related differences were not uniform across every social behavior.')
add('Golden hamsters show little hand-directed play',['mice_hamsters'],['cmp_hamster_contact'],'''
Golden hamsters received the same categories of interaction used for mice: dorsal tickling, gentle dorsal touch, and an opportunity to follow the hand without contact. The animals were tested repeatedly across ten days rather than classified from one encounter.

Hamsters spent less than 10% of the pursuit phase following the hand on average. Calls occurred throughout the session, but they lacked a strong onset-linked response specific to tickling. Calling during tickling was similar to calling during intervening breaks.

Gentle touch produced fewer calls than breaks, while introduction periods had low call rates. Different tactile and social circumstances therefore affected behavior without producing the selected-mouse pattern. Minimal hand-directed engagement is a result about this interaction, not evidence that hamsters lack play with appropriate partners.
''','The repeated-session comparison used juvenile male golden hamsters. Low pursuit and weak tactile modulation distinguish their response from that of tame mice. Their calls during human sessions are not labeled laughter or assigned a proven emotional valence.')
add('Hamsters actively play with other hamsters',['mice_hamsters'],['cmp_hamster_social'],'''
A hamster’s weak response to human tickling contrasts with its activity toward another hamster. In freely moving conspecific sessions, animals engaged in reciprocal boxing, mounting, chasing, and pinning rather than simply remaining separate from the partner.

**Pinning** places one partner underneath the other during bodily interaction; **boxing** involves opposed upright contact. The ethogram, a defined catalogue of behaviors, separated these actions from breaks without physical contact. Calls were more frequent during most interaction categories than during breaks.

Overall call rates were higher in conspecific sessions than in human-contact sessions. The partner relationship therefore changed both behavior and acoustic output. A manual tickling assay can underestimate social playfulness in an animal that engages strongly with members of its own species.
''','Facial contact was an exception to the general increase in calls over break periods. The paper identifies reciprocal boxing and pinning as play-related interactions; not every behavior in a mixed social session is itself proof of positive affect.')
add('Hamster sounds change with the interaction partner',['mice_hamsters'],['cmp_hamster_spectra'],'''
Hamster calls were acoustically more uniform during conspecific encounters than during sessions involving a human hand. Conspecific calls often had long duration and relatively flat frequency trajectories, while human-session calls included short, descending, and inverted-U-shaped forms.

**Harmonics** are frequency components occurring at multiples of a fundamental frequency. They appear as approximately parallel bands in some hamster recordings. **Frequency slope** describes the direction and rate of frequency change within a call, distinguishing flat calls from sharply descending calls.

The boundary between audible and ultrasonic hamster calls was less clear than in mice. The investigators therefore grouped calls using their full spectrogram patterns. Differences in duration, frequency trajectory, and acoustic complexity describe context-sensitive vocal output rather than a single species-wide laughter sound.
''','The original spectrograms preserve the 20 kHz reference and 50 ms scale. Calls in a human-contact session could occur during breaks as well as actual contact, so session-associated calls are not all treated as tickle-evoked calls.')
add('Hamster vocal repertoires vary within human sessions',['mice_hamsters'],['cmp_hamster_clusters','cmp_hamster_features'],'''
The investigators compared whole spectrograms to group similar hamster sounds. A **call cluster** is a collection of calls with related acoustic structure. Calls during conspecific sessions formed a relatively uniform distribution, while human-session recordings contained several distinguishable groups.

Some groups contained high-frequency descending calls; others contained shorter calls or inverted-U trajectories. **Call duration** measures how long an acoustic event persists, while principal frequency describes its characteristic frequency. These properties differed between conspecific calls and human-session groups.

Group proportions also varied across introduction, breaks, tickling, and gentle touch. A dominant descending-call group changed across repeated sessions. Acoustic repertoire and rate therefore supply complementary information: two encounters can produce calls yet recruit different forms and different relationships to actual contact.
''','Clustering was based on spectrogram-image features and then checked against measured acoustic properties. The published plots are unchanged; the deck does not create a new call classification or infer that a particular hamster cluster is established positive-affect laughter.')
add('Orangutans vocalize during caregiver tickling',['apes'],['ape_spectra'],'''
Davila Ross and colleagues recorded young orangutans, gorillas, chimpanzees, bonobos, and humans during caregiver tickling. Familiar partners stimulated regions including palms, feet, neck, and armpits, generating vocal behavior in a comparable social setting across these species.

Orangutan calls were comparatively long and occurred in shorter sequences than the faster repeated calls typical of the Pan species. **Pan** is the genus containing chimpanzees and bonobos. Temporal structure distinguished vocal responses even though all were collected during playful tactile interaction.

Orangutan recordings included both inward- and outward-airflow vocalizations and an example of sustained outward-airflow sound lasting 4.2 s. Tickling-related vocal capacity is therefore broader than a single alternating pant pattern. Related species can share a behavioral response while differing in how their vocal sequences are organized.
''','The source analyzes acoustic characters rather than direct respiratory measurements. The spectrogram shown includes other species for comparison; the orangutan-specific statements come from the reported species comparisons and the documented 4.2 s example.')
add('Gorilla tickling calls include prolonged exhalation',['apes'],['ape_airflow'],'''
Gorillas vocalized during tickling with familiar caregivers. Their calls tended to be longer and less densely repeated within a sequence than chimpanzee and bonobo calls, giving the response a different temporal organization within the same social context.

**Egressive** sound accompanies outward airflow; **ingressive** sound accompanies inward airflow. Gorilla recordings contained both categories. Some sequences remained egressive for several seconds, including a reported example lasting 13.2 s.

That example establishes a production capacity expressed by an individual, rather than a universal maximum for gorillas. Ape laughter is not obligatorily limited to alternating one inhalation with one exhalation. Human laughter’s strong outward-airflow bias modifies a capacity that other great apes can also express during tactile play.
''','Airflow categories were assigned from acoustic and perceptual characteristics, not a simultaneous respiratory sensor. The duration is an observed example. Gorilla and human vocal behavior can differ in typical usage while sharing the capacity for prolonged egressive sound.')
add('Chimpanzees produce repeated tickling vocalizations',['apes'],['ape_timing'],'''
Chimpanzees responded to familiar caregivers’ tickling with repeated vocal events. Compared with orangutans and gorillas, chimpanzees and bonobos tended to produce shorter calls and more calls within a sequence, separating call duration from overall bout duration.

An **intercall interval** is the time between successive vocal events. Measuring event timing and the number of calls in a sequence captures organization that cannot be described by whether an animal vocalizes at all. The Pan pattern is temporally closer to the densely repeated organization of human laughter.

Chimpanzee sequences included both airflow directions, as well as a sustained egressive example lasting 3.3 s. Temporal similarity therefore coexists with production differences. Comparative analysis treats call duration, sequence length, voicing, and airflow as separate characters of tickling-induced vocal behavior.
''','The comparison concerns recorded juvenile tickling responses. It does not imply that acoustic resemblance alone measures the animal’s subjective experience. Familiar caregivers and repeated calls establish the behavioral context of the analyzed recordings.')
add('Bonobos tickle one another during natural social play',['bonobo_tickling'],['cmp_bonobo_photo'],'''
Bonobo tickling occurs between animals, as well as during human–ape interaction. Demuru and colleagues observed play in a socially housed group and identified repeated grasping pressure on regions such as the neck, belly, feet, and armpits.

Hands, feet, or the mouth could deliver the stimulation. The published sequence records an adult male using its mouth to tickle an infant female, then inspecting her face. This is bodily play directed toward a partner rather than an experimenter imposing a standard tactile stimulus.

Tickling occurred in approximately 13% of the analyzed dyadic play sessions. **Dyadic** means involving two individuals. Tickling was therefore one particular component of the broader repertoire, not synonymous with all bonobo play. Actor identity, receiver identity, age, and relationship characterized its social distribution.
''','A bout began at contact and ended when contact stopped. Closely separated bouts were grouped into a tickling session. Observations included sessions recorded from beginning to end; the analysis did not experimentally assign partners or vary tickling pressure.')
add('Bonobo tickling depends on age and social bonds',['bonobo_tickling'],['cmp_bonobo_direction','cmp_bonobo_bond'],'''
Bonobo tickling was socially asymmetric. Older animals spent a greater proportion of their play time tickling others, while younger animals spent more time receiving tickling. Older-to-younger interactions contained more tickling than same-age or younger-to-older interactions.

An **affiliative bond** is a social relationship expressed through friendly interaction. The researchers used grooming to distinguish strongly and weakly bonded pairs. Strongly bonded pairs devoted more of their play to tickling, with mother–infant relationships particularly prominent.

The individual that initiated play also tended to perform more tickling. Age, initiation, and relationship therefore organized the contact sequence together. These findings support the hypothesis that tickling contributes to coordinated, partner-sensitive play, rather than functioning as an identical skin-triggered response regardless of who delivers contact.
''','Developmental change concerns the roles of actor and receiver, not an experimentally measured age-specific sensory threshold. The observations support partner-sensitive interaction; the proposed contribution to intersubjectivity is a hypothesis rather than a directly measured mental state.')
add('Bonobo laughter may influence reward expectations',['bonobo_optimism'],['cmp_bonobo_optimism','cmp_bonobo_task'],'''
A **judgment-bias task** measures responses to ambiguous cues after animals learn rewarded and unrewarded alternatives. Winkler and colleagues trained bonobos to approach a black box containing food and skip a white box that was empty.

After hearing either bonobo laughter or wind noise, animals encountered unfamiliar gray boxes between those learned colors. They tended to approach ambiguous boxes more often after laughter. The effect was suggestive rather than decisive, so it supports a hypothesis of altered positive expectation rather than a confirmed mood shift.

The task measures a consequence beyond immediately joining another animal’s play. Learned color–reward relationships supplied the basis for interpreting the choice. Comparing laughter with a control sound asks whether a social vocal signal can influence expectations about a later, separate opportunity for reward.
''','Playback lasted 7 min 28 s. The paper describes a small trained sample and a marginal condition effect; the slide intentionally calls the result suggestive. The approach-or-skip task tests decision bias, not direct ticklishness or an animal’s verbal report of emotion.')
add('Human tickling laughter emphasizes regular voicing',['apes'],['ape_voicing'],'''
Human children produced tickling-induced laughter with more regular voicing than the nonhuman great apes in the comparative recordings. **Voicing** is sound generated through regular vibration in the vocal source, producing a periodic acoustic structure.

Many nonhuman ape calls were predominantly irregular or breathy, although some recordings contained voiced components. A bonobo produced particularly clear voicing. The difference was therefore one of distribution and emphasis rather than a perfectly exclusive human capacity.

Voicing is independent of the social trigger: a familiar caregiver’s tickling elicited sounds in every comparison group. Acoustic organization can change during evolution while the triggering behavior remains shared. Describing voiced versus irregular sound identifies a production character without equating a human-like sound with a uniquely human emotional state.
''','The study compared recorded calls across hominid species and used a siamang outgroup. The human result concerns the acoustic regularity of tickling laughter, not an assertion that every human laugh in every setting is voiced.')
add('Human laughter favors outward-airflow sequences',['apes'],['ape_airflow'],'''
Human tickling laughter in the study was consistently egressive, meaning associated with outward airflow. Nonhuman great apes produced both egressive and ingressive vocalizations, often combining these within a longer sequence of tactile play.

Breathing direction and call repetition describe different levels of organization. A sequence can contain repeated short events during an outward-airflow period, or alternate between inward and outward components. Human production placed stronger emphasis on the outward-airflow pattern.

Gorilla and bonobo recordings nevertheless included prolonged egressive examples lasting 13.2 s and 10.5 s. Human laughter’s respiratory bias therefore does not require that sustained outward vocalization originated only in humans. An inherited capacity can become more consistently expressed along one evolutionary lineage.
''','These are acoustic airflow assignments and observed durations, not measured limits of lung function. The source gives individual examples to distinguish a capacity from a species’ typical distribution of airflow patterns.')
add('Acoustic ancestry links human and great-ape laughter',['apes'],['ape_tree'],'''
A **homologous trait** is related across species through shared evolutionary ancestry. Davila Ross and colleagues reconstructed relationships using measured characters of tickling vocalizations, including acoustic regularity, temporal organization, and airflow pattern.

The acoustic grouping resembled established great-ape relationships: humans were closest to chimpanzees and bonobos, followed by gorillas and orangutans. This correspondence supports an ancestral origin for tickling-induced laughter within the great-ape and human group.

Shared ancestry and similar current function answer different questions. Dog play faces, dolphin displays, and kea warbles may help coordinate playful interaction, but their resemblance in function is not the acoustic evidence used to reconstruct hominid laughter. The phylogenetic claim applies to the taxa and characters actually analyzed.
''','A siamang served as the outgroup for the reconstruction. The published evolutionary timeline is the authors’ inference from acoustic characters and known relationships. Similar playful function in distant groups does not independently establish vocal homology.')
add('Dogs rapidly match open-mouth faces and play bows',['dogs'],['cmp_dog_mimic'],'''
A **relaxed open mouth** is a play-related facial display distinct from an attempt to bite. A **play bow** lowers the front of the body while the hindquarters remain raised. Palagi and colleagues recorded both during spontaneous dog–dog play.

**Rapid mimicry** is replication of a partner’s displayed movement within 1 s. Dogs more often returned a bow after observing a bow than after observing a jump. They also more often returned an open-mouth display after the same display than after a bite-like movement.

The comparison separates matching a social signal from simply responding to any nearby movement. Bowing and facial opening recruit different visible actions, yet both had a rapid matching pattern. These are measures of canine play communication, not experiments establishing a laughter response to tickling.
''','The observations were collected in a dog park without experimental manipulation of contact. The same motor form had to be replicated within the one-second window, with visual orientation toward the signaler and no corresponding response already underway.')
add('Dog signal matching exceeds movement coincidence',['dogs'],['cmp_dog_frequency','cmp_dog_mimic'],'''
Frequent actions can produce apparent matches by coincidence. The dog study compared play bows with jumps and relaxed open mouths with bite-like actions, pairing each signal with a movement that had overlapping components but a different social role.

Jumps occurred more frequently than bows, and bite-like movements more frequently than relaxed open mouths. Despite this, bows and open-mouth signals produced the clearer matching responses. The effect therefore was not explained simply by those signals being the most common actions.

Returning a partner’s signal within 1 s provides a temporal relationship between perception and action. The authors propose that this coupling supports sharing a playful state. That affective interpretation is a hypothesis; the directly recorded result is selective, rapidly timed replication of particular social displays.
''','Responses were normalized to the stimuli actually perceived by the receiver. A frequent movement and an effective social signal are different quantities. The comparison preserves the observed motor controls rather than interpreting every simultaneous action as mimicry.')
add('Familiar dogs match play signals more frequently',['dogs'],['cmp_dog_bond'],'''
The dog study categorized partners as friends, acquaintances, or strangers using their history of interaction. Friends had more sustained relationships, while strangers lacked prior familiarity. These categories described the social context of the same visible play signals.

Body and facial mimicry occurred most frequently between friends, less between acquaintances, and least between strangers. The relationship effect remained after accounting for the play signals perceived. Merely having more opportunities to see a signal did not explain the complete pattern.

Familiarity can therefore shape rapid perception–action coupling during play. A hypothesis is that recognizing a trusted partner increases readiness to match its playful behavior. Like the social distribution of bonobo tickling, the canine result links observable interaction with who the partner is, rather than treating the motor response as socially invariant.
''','The friends category reflected frequent prior interaction, rather than a newly assigned experimental relationship. Bond quality predicted mimicry frequency in the observational model. The study did not manipulate oxytocin or directly record neurons in dogs.')
add('Dog signal mimicry accompanies longer play',['dogs'],['cmp_dog_duration'],'''
Dog play sessions containing at least one rapid matching event lasted longer than sessions containing a play signal without matching. Both conditions included visible bows or relaxed open mouths, so the comparison concerned the partner’s response rather than simply signal presence.

Session duration measures the persistence of the shared activity. Longer interaction provides more opportunity for reciprocal movement and continued exchange. Rapid matching and sustained play were associated features of these recorded encounters.

The authors’ hypothesis is that signal matching helps partners coordinate and maintain playful motivation. The observational result establishes association rather than proving that mimicry alone lengthened the session. Partner familiarity also influenced matching, connecting communication and social relationship within the same behavioral setting.
''','The original figure reports duration in seconds. The direction of influence between engagement and mimicry was not experimentally separated, so a causal claim that matching necessarily prolongs play would exceed the evidence.')
add('Wolf puppies direct play bows toward visible partners',['wolves'],['cmp_wolf_wolf'],'''
Wolf puppies used the canid play bow during freely moving social play. Byosiere and colleagues examined what each partner did immediately before and after the posture, distinguishing the animal that bowed from the partner receiving the signal.

Every recorded wolf bow occurred when the two animals could see one another. Dog puppies likewise had mutual visibility for almost all bows; the exceptional dog case included barking, an attention-getting action. Visual availability was therefore closely associated with this bodily signal.

The posture appeared within an exchange of offensive, vulnerable, paused, and other play-related actions. **Offensive play** refers to partner-directed actions such as chasing or playful bites, not necessarily serious aggression. Coding the surrounding sequence connects a visible gesture with the ongoing interaction rather than assigning meaning from posture alone.
''','The study compared dog puppies aged 2–5 months with wolf puppies aged 2.7–7.8 months. Its operational categories describe immediate behavior around each bow; their presence does not establish tactile ticklishness in either species.')
add('Play bows restart dog and wolf play differently',['wolves'],['cmp_wolf_dog','cmp_wolf_wolf'],'''
A familiar-looking signal can have different effects in closely related animals. Dog puppies often bowed after a pause, and both partners were less likely to remain paused after the bow. This sequence was consistent with restarting an interrupted play exchange.

Wolf puppies did not show the same before–after reduction in pauses. Their bows occurred during social play, but the posture was not associated with the same clear reinitiation pattern. The meaning of a signal therefore depends on its observed position and consequences within the behavioral sequence.

The comparison used the same categories for both species and separately scored the bower and partner. Comparable measurement makes the functional difference visible. A shared canid posture need not recruit an identical partner response across developmental stages and species.
''','A pause was a defined category in the ethogram, not a subjective judgment that the animal had lost interest. The findings compare these puppy groups and should not be generalized to every adult dog or wolf interaction.')
add('Canid play bows relate to complementary movements',['wolves'],['cmp_wolf_wolf','cmp_wolf_dog'],'''
After a play bow, both dog and wolf bowers were more likely than their partners to perform vulnerable or escape-related actions. Such actions can create opportunities for the other animal to pursue or counterattack within a playful exchange.

The hypothesis that bows simply announce easily misinterpreted offensive behavior was not consistently supported. Dog partners increased offensive actions after bows, while bite-related actions in wolf puppies were more common before than after the posture. The same signal participated in different action sequences.

Nor did bows increase identical, synchronous actions in both animals. **Complementary behavior** involves different but coordinated roles, such as pursuit and escape, rather than both partners making the same movement. Play communication can organize reciprocity without producing direct motor mimicry.
''','The absence of increased synchronous behavior changes the interpretation of the posture: the study supports sequence-dependent interaction rather than a universal synchronization command. These substantive contrasting outcomes are part of the teaching content, not routine caveat endings.')
add('Dogs and horses balance their playful actions',['dog_horse'],['cmp_horse_balance','cmp_horse_photo'],'''
Dogs and horses can play together despite differences in body size and movement repertoire. Maglieri and colleagues analyzed recorded interactions in which both partners were free to move and humans did not intervene in the exchange.

**Play variability** describes diversity among an animal’s actions during a session. Dog and horse partners had similar variability in their playful movements. The repertoire included running, contact, and species-specific actions rather than a sequence in which only one animal contributed.

Coordinated interaction can therefore span a species boundary. Comparable variability does not require identical anatomy or identical movements; each partner contributes a range of actions appropriate to its body. These observations concern interspecies play and communication, providing a comparison with human–rodent tactile interaction rather than direct evidence of horse ticklishness.
''','The study used publicly available videos selected for sustained, unconstrained play. It does not estimate how common dog–horse play is in the general population. Comparable action diversity describes the recorded dyads.')
add('Dogs and horses adopt self-handicapping positions',['dog_horse'],['cmp_horse_handicap','cmp_horse_photo'],'''
**Self-handicapping** occurs when an animal adopts a vulnerable position or limits its advantage during play. In the dog–horse recordings, partners rolled, shook their heads, crouched, or used other actions that could permit the partner to counterattack.

Dog and horse players showed similar proportions of self-handicapping actions within their respective repertoires. This reciprocity accompanied comparable play variability, even though the two species differ greatly in typical size and the movements available to them.

A vulnerable position changes the possibilities for the next exchange. A dog lying or crouching and a horse lowering its forequarters can modify who approaches, escapes, or directs contact. The authors propose that balanced tactics help maintain play across mismatched bodies without requiring both partners to use the same action.
''','The paper’s ethograms distinguish shared and species-specific self-handicapping patterns. The interpretation concerns coordination in the observed exchanges, rather than claiming that the animals consciously calculate fairness or intentionally suppress a measured amount of force.')
add('Dog–horse facial matching occurs within one second',['dog_horse'],['cmp_horse_mimic','cmp_horse_photo'],'''
Dogs and horses displayed relaxed open mouths during their shared play. More than 90% of these displays were not followed by a bite or attempt to bite by the same animal, separating the visible signal from completion of a biting sequence.

Receivers more often returned an open-mouth display within 1 s after seeing the partner’s open mouth than after seeing a bite attempt. The difference was concentrated in the first second rather than persisting clearly into the later response windows.

Matching occurred in both directions across the dog–horse boundary. A rapidly timed response can therefore be triggered by a partner with a different face and behavioral repertoire. The shared visual display supplies one means of coordinating social play without requiring a shared species-specific vocalization.
''','The receiver had to be looking at the sender and not already displaying an open mouth. Bite attempts provided a motor control resembling the display. The published photograph and plot are unchanged original panels from the article.')
add('Dolphin open-mouth displays accompany social play',['dolphins'],['cmp_dolphin_display'],'''
Bottlenose dolphins emitted open-mouth displays mainly during social rather than solitary play. Maglieri and colleagues recorded spontaneous activity outside feeding and training sessions, distinguishing dolphin–dolphin interaction from human–dolphin and solitary activity.

The mouth opening was a behavioral event, not the animal’s permanent apparent smile. Most recorded displays occurred during dolphin–dolphin play. The open mouth was not accompanied by the violent vertical head motions that characterized observed aggressive encounters.

Play included reciprocal chasing, escape, gentle bites, and tail actions, with opportunities for both partners to respond. The open-mouth display occurred within this exchange as a candidate visual play signal. The study tests its communication role rather than whether dolphins laugh or respond positively to human tickling.
''','Intraspecific play accounted for 92.3% of the open-mouth cases. Only one display occurred during solitary play. The source figure is an original published display-and-visibility comparison, with drawings credited to the article’s illustrator.')
add('Dolphins display open mouths within a partner’s view',['dolphins'],['cmp_dolphin_visual','cmp_dolphin_display'],'''
A **visual field** is the portion of the environment available to an animal’s sight. The dolphin study classified displays according to the sender’s position relative to the potential receiver, separating events within and outside the receiver’s field of view.

Approximately 89% of open-mouth displays occurred within the partner’s visual field. Rostrum touches and attempts to play bite did not have the same strong visibility bias. These comparison actions also involve the mouth region, so head orientation alone was not an adequate description of the difference.

The position of a social signal affects whether a partner can detect it. The authors hypothesize that dolphins adjust display use to the receiver’s attention. Underwater play can involve visual exchanges at close range, even in a taxon with extensive acoustic communication.
''','Visibility was inferred from relative body orientation rather than measured by eye tracking. The published geometric diagram preserves the authors’ field-of-view definition. Rostrum means the elongated snout, represented in the original source panels.')
add('Visible dolphin displays recruit rapid matching',['dolphins'],['cmp_dolphin_mimic'],'''
Dolphins sometimes returned an open-mouth display within 1 s of a partner’s display. The study compared events in which the receiver could detect the sender with events in which the sender was outside its visual field.

Matching followed about one-third of detected displays, compared with approximately 4% of displays outside the receiver’s view. Receiver visibility therefore predicted the rapid response rather than both animals simply opening their mouths during the same activity.

The timing and detection comparison connect an observed signal with a subsequent action. **Visual mimicry** describes that behavioral relationship; sharing a playful emotional state is the authors’ proposed interpretation. The directly recorded response concerns visible mouth opening, not a recorded laughter-like acoustic event.
''','The study did not collect synchronized ultrasound or vocal recordings. The slide reports observed response percentages rather than treating the paper’s adjusted model coefficient as a probability multiplier.')
add('Dolphin play displays differ from bite attempts',['dolphins'],['cmp_dolphin_display'],'''
An open-mouth display and a bite attempt share mouth opening but differ in action sequence. A bite attempt includes rapid opening and closing while lunging toward a partner; a rostrum touch places the snout against a body or object.

Open-mouth displays had a stronger orientation toward a visible receiver than these comparison actions. When a visible display was not reciprocated, the sender did not simply complete the sequence by biting the partner. Display and completed contact were therefore behaviorally separable.

**Ritualization** is the evolutionary hypothesis that an action can acquire a signaling function after modification of its original form or context. The authors propose a relationship between bite-related movements and play displays. The observed separation of display from biting supplies evidence relevant to that hypothesis without making the display a tickling response.
''','The study compares signal-like behavior with motorically similar actions. The source itself contains the illustrative dolphin drawings; they were cropped without being recreated, recolored or modified. The proposed evolutionary origin remains a hypothesis.')
add('Elephants rapidly match playful trunk movements',['elephants'],['cmp_elephant_control','cmp_elephant_actions'],'''
African savanna elephants performed distinctive trunk and head movements during play. Cordoni and colleagues tracked movements such as raising the trunk, swinging it forward, placing it over the head, and moving the head from side to side.

An elephant was more likely to perform the same target movement within 1 s after a partner’s movement than during a matched control period without the preceding movement. **Motor mimicry** therefore concerned specific rapidly repeated actions, rather than any increase in nearby activity.

These movements occur within social play, with the body and trunk providing visible signals. The comparison extends perception–action matching beyond mouth displays in dogs and dolphins. It is evidence of elephant play coordination, not a demonstration that trunk movement is laughter or that the elephant was experimentally tickled.
''','The original photographs retain the published yellow arrows identifying target movements; no arrows were added by the deck author. The matched-control comparison separated response after a triggering movement from a period without that trigger.')
add('Elephant matching accompanies competitive play',['elephants'],['cmp_elephant_actions'],'''
Elephant play included sparring, chasing, standing tall, and spinning. **Sparring** is a partner-directed competitive exchange performed in the play context. The researchers compared surrounding actions when a target movement was rapidly matched and when it was not.

Matched movements were associated with sparring before and after the response, and were often preceded by play chase. Unmatched target movements also occurred around sparring, but their preceding sequence included more neutral standing-tall and spinning patterns.

Matching was therefore related to the organization of a challenging exchange rather than simply to longer play sessions. Unlike the association reported in dogs, elephant mimicry did not predict longer sessions. The authors hypothesize a role in coordinating competitive play, with function shaped by the surrounding repertoire.
''','Competitive or offensive patterns in the ethogram are not equated with serious aggression. The different relationship to session duration is a meaningful cross-species contrast. The photograph identifies the same trunk and head movements used in the sequence analysis.')
add('Elephant mimicry and play contagion covary',['elephants'],['cmp_elephant_contagion','cmp_elephant_actions'],'''
Rapidly matching a current partner and starting play after watching others are distinct behaviors. The elephant study compared each animal’s involvement in a network of movement matching with its involvement in a network of play contagion.

Animals more prominent as receivers of matching interactions were also more prominent as animals that began playing after others. The relationship connected coordination within an ongoing exchange with recruitment into new playful activity elsewhere in the group.

A **social network** describes individuals and their observed relationships. Greater involvement in one network corresponded to greater involvement in the other, while age, sex, and measured affiliation did not explain the rapid-matching effect. The authors propose a connection with affect sharing, but the measured result is covariation between two behavioral processes.
''','The plot retains the original network measures on its axes. Mimicry happens within a current dyad; play contagion involves an animal that was not already engaged. Neither measure is a direct self-report of an emotional state.')
add('Kea warble calls trigger new playful behavior',['kea'],['cmp_kea_calls'],'''
Kea are parrots with social, object-directed, and aerial play. Schwing and colleagues tested a characteristic play **warble**, a modulated vocalization associated with playful behavior, using acoustic playback to wild birds rather than physical tickling.

Each trial included 5 min before playback, 5 min of playback, and 5 min afterward. Warble playback increased both the number of play bouts and their duration. Behavior returned toward the pre-playback pattern afterward, giving the response a close relationship to the acoustic stimulus.

Birds could initiate new exchanges, manipulate objects, or perform aerial acrobatics. A social sound therefore changed activity without the experimenter contacting the bird’s skin. The result broadens the comparison from tactile elicitation of play-related sounds to behavioral responses caused by hearing such sounds.
''','The published figure reports play bouts per bird and play duration in seconds per bird. The experiment supplies a playback intervention, contrasting with observational mimicry studies and with direct tickling assays in rodents and hominids.')
add('Control sounds isolate the kea play-call effect',['kea'],['cmp_kea_calls'],'''
Sound playback can attract attention without specifically promoting play. The kea experiment therefore compared the play warble with two non-play kea calls, a South Island robin call, and a standardized **2 kHz** tone.

The warble was the only tested sound that increased both play frequency and play-bout duration during playback. Other calls and the tone did not produce the same pattern across the before, during, and after periods.

These controls distinguish a play-associated acoustic signal from general noise, a conspecific call, or a familiar bird sound. The authors’ hypothesis is positive emotional contagion: the warble induces a playful state in receivers. The recorded outcome is the selective increase in playful behavior during the experimental sound period.
''','The robin call was a familiar environmental comparison, and two other kea call categories separated the effect from conspecific identity alone. No physical touch occurred, so the result is not evidence that kea experience mammalian-style tactile tickling.')
add('Kea calls recruit social and solitary play',['kea'],['cmp_kea_calls'],'''
After hearing the warble, kea often began new play rather than merely joining an exchange already underway. Some interacted with previously non-playing birds, while others manipulated objects or performed aerial acrobatics alone.

Both juveniles and adults participated, including adult males and females. The effect therefore extended across age and sex categories rather than being confined to juvenile rough-and-tumble contact. Solitary activity also changed, despite lacking an immediate partner whose actions could be copied.

This breadth favors the authors’ hypothesis that the call induces playfulness rather than serving only as an invitation to one ongoing interaction. Behavioral recruitment can occur through sound without direct motor matching. Kea provide an avian comparison with mammalian laughter-like play vocalizations while retaining a distinct experimental evidence base.
''','The paper contrasts brief emotional responses with persistent moods because play did not remain elevated in the post-playback period. Individual birds were difficult to track during rapid aerial activity, so the deck avoids assigning exact age-specific effect sizes.')
add('Partner identity shapes responses to playful contact',['mice_hamsters','bonobo_tickling','dogs'],['cmp_hamster_social','cmp_bonobo_photo'],'''
Responses to playful contact vary with both species and partner. Tame mice pursued human hands and vocalized during tickling, while golden hamsters showed much greater engagement with conspecifics than with the same classes of human interaction.

Within bonobos, tickling was more prominent between strongly bonded partners and commonly directed from older toward younger animals. In dogs, familiar partners more frequently matched one another’s play signals. Relationship and developmental role therefore altered observable interaction within a species.

These results separate social receptiveness from a fixed property of skin stimulation. Human-directed approach, partner-directed bodily play, and rapidly matched signals measure different components of engagement. A comparative account preserves each animal’s behavioral repertoire and the experimental or observational context in which its responses were measured.
''','The evidence supports context-sensitive responses across species without implying a common measured receptor mechanism in every animal. Tameness selection, natural bonobo relationships and dog familiarity were investigated with different designs.')
add('Animals coordinate play through different sensory signals',['apes','mice_hamsters','dolphins','elephants','kea'],['cmp_dolphin_mimic','cmp_kea_calls'],'''
Playful interaction recruits different sensory routes across animals. Direct tickling combines touch with social contact in hominids and responsive rodents. Mouse and hamster calls additionally vary with whether the partner is human or conspecific.

Dolphins use rapidly reciprocated visual mouth displays, elephants match trunk and head movements, and kea respond to heard play warbles. The measured relationships include immediate matching, initiation of new play, learned approach, and suggestive changes in reward expectation.

Shared social function and shared evolutionary origin are separate claims. Acoustic phylogeny supports ancestral continuity of tickling laughter among great apes and humans; comparable play coordination in distant taxa does not by itself establish the same ancestry. Across-species comparison links behavior to the specific sensory evidence available for each animal.
''','Direct tickling, play-signal matching and play-call playback remain explicitly separate evidence categories. The deck’s broad scope does not claim that dogs, wolves, horses, dolphins, elephants and kea have experimentally established gargalesis.')
assert len(S)==44,len(S)
items=[{'lead':'Species and partner','text':'Tame mice engage with human hands, while golden hamsters show weak human-directed play and strong conspecific play; contact responses are context dependent.'},{'lead':'Direct tactile evidence','text':'Rats voluntarily seek tickling, and trunk cortex and PAG manipulations link touch and play with vocal output; those neural findings come from rats.'},{'lead':'Hominid continuity','text':'Orangutans, gorillas, chimpanzees, bonobos and humans vocalize during tickling; acoustic relationships support shared ancestry within this group.'},{'lead':'Social coordination','text':'Dogs, dog–horse partners and dolphins rapidly match play displays, while elephants match trunk and head movements; canid play-bow functions differ across species.'},{'lead':'Acoustic recruitment','text':'Kea warble playback selectively increases social and solitary play; bonobo laughter provides suggestive evidence of altered reward expectations.'},{'lead':'Evidence boundaries','text':'Direct tickling, play contagion and motor mimicry measure different processes; similar playful function alone proves neither ticklishness nor shared vocal ancestry.'}]
spec={'lecture':78,'content_slides':44,'theme':'umber-stone-paper','title_height':2.5,'title_min_pt':25,'title_image':fig('cmp_bonobo_photo'),'title_refs':[R['bonobo_tickling']['reference']],'slides':S,'takeaways':{'items':items,'cite':'; '.join(short(k) for k in AUTH),'refs':[R[k]['reference'] for k in AUTH]}}
if (B/'media_sources.json').exists():
 media=json.loads((B/'media_sources.json').read_text())
 for z in S:
  for v in media['unavailable_useful_recordings']:
   if R[v['paper']]['reference'] in z['refs']:z['transcript'].append('Original article recording: '+v['identifier']+'. '+v['original_article_media_link']+'. Download unavailable; the published figure is retained.')
(B/'lecture.json').write_text(json.dumps(spec,indent=2,ensure_ascii=False)+'\n')
wc=[len(re.sub(r'\*\*','', ' '.join(z['body'])).split()) for z in S];print('Slides',len(S),'words',min(wc),max(wc));print([(i+2,n) for i,n in enumerate(wc) if not 90<=n<=170])
