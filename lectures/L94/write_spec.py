"""Verified source-grounded Lecture 94. Build with tools/build_lecture.py."""
from pathlib import Path
import json
B=Path(__file__).resolve().parent;R=json.loads((B/'research.json').read_text());slides=[]
def figure(k,n,desc):return {'kind':'article','path':f'figures/{k}_{n}.png','caption':f"{R[k]['short']}, Fig. {n}. {desc}",'source_url':'https://doi.org/'+R[k]['doi']}
def add(k,n,title,text,desc,extra=None):
 body=text.strip().split('\n\n');assert len(body)==3,(title,len(body))
 s={'title':title,'layout':'figure-right','body':body,'figure':figure(k,n,desc),'cite':R[k]['short'],'refs':[R[k]['reference']],'transcript':body.copy()}
 if extra:s['layout']='figures-right';s['figures']=[s.pop('figure'),figure(*extra)];s['refs']=list(dict.fromkeys(s['refs']+[R[extra[0]]['reference']]))
 slides.append(s)
add('intro',7,'Sea lions learn to control a computer cursor','''**Cognitive enrichment** provides opportunities to use perception, learning and decision making within an animal's managed environment. Winship and colleagues introduced Enclosure Video Enrichment, abbreviated **EVE**, to California sea lions housed in outdoor sea pens. The animals controlled a visible cursor rather than watching a prerecorded sequence.

Pressing directional buttons moved a blue circle toward a black target. Contact with the target produced an acoustic signal and reinforcement. This arrangement linked the animal's action to an observable consequence on the display and subsequently to a reward.

The sea lions progressed through successive training phases and acquired enough cursor control to enter additional games. Their movements therefore affected the ongoing task. Watching a screen, contacting a controller and directing a cursor are separate behavioral achievements.''','Sea lion operating the cursor task')
add('intro',1,'A display and a touchscreen are different interfaces','''A **touchscreen** registers contact at a location on its display. EVE instead separated the display from the input device: a monitor presented visual targets, while four buttons controlled cursor movement. The sea lion selected movements rather than directly touching the target's displayed position.

This separation matters for task demands. A direct-contact response identifies a location, whereas cursor control requires a relationship between button direction, duration of contact and movement elsewhere in the visual field. The researchers trained that relationship explicitly rather than assuming it was already understood.

The apparatus accommodated marine mammals without requiring fingers or hands to manipulate a conventional computer input device. The published EVE experiments concern a controller-based interface; their performance measures must be interpreted within that particular arrangement.''','Separate monitor and directional controller')
add('intro',1,'Controller geometry changes the response options','''The EVE controller contained four arcade buttons positioned in compass directions on a **6 × 6 inch** box. Each button corresponded to a direction of cursor travel. The controller was mounted to support comfortable access while the animal monitored the display.

An earlier, larger box provided extra space around the buttons. Sea lions sometimes contacted that space rather than activating a button. Replacing it with the smaller controller reduced the amount of irrelevant surface encountered during a response and supported subsequent training.

Simultaneous contact with two buttons could produce diagonal movement. A response was therefore not always a single isolated direction. Controller geometry and the program's treatment of combined inputs determined which movements an animal could produce during a trial.''','Controller size and button arrangement')
add('intro',7,'Protective coverings can interfere with control','''The initial controller included a plastic covering intended to protect its buttons from moisture and animal contact. The researchers reported that the covering interfered with finding and depressing individual buttons. Removing it was followed by more rapid progress in training.

The covering could also place tension across neighboring buttons, making simultaneous presses more likely. A hardware feature intended for protection therefore changed the relationship between a contact and the registered input. Such a change affects the action that the game actually records.

The authors proposed that reduced tactile access contributed to the difficulty. That explanation was not established by a separate sensory experiment. The observed improvement concerns an interface modification during acquisition, with the animal's behavior and the functioning of the controller evaluated together.''','Animal contacting the uncovered controller')
add('intro',2,'Cursor contact determines the trial consequence','''A **contingency** is a relationship between an event and the consequence that follows it. In the Cursor Training Game, cursor contact with a target produced a success tone and reinforcement. The animal's button presses controlled when that contact occurred.

The cursor was a bright blue circle against a white background, and the targets were black rectangles. Target location and cursor size changed across training phases. These changes altered the movements required for success while retaining the basic response–consequence relationship.

Game software recorded directional presses, their durations and response times. A successful response could therefore be evaluated from the cursor's contact with the target and from the sequence of inputs that produced it, rather than being scored only from a trainer's impression.''','Successive cursor-training task displays')
add('intro',7,'Screen attention is trained separately from movement','''At initial exposure, the sea lions were accustomed to monitoring their trainers and did not consistently attend to the display. The researchers reinforced visual monitoring while manually advancing trials so that target and wall positions changed every **2–3 s**.

These changes made the display relevant before the animals had mastered directional control. During this stage, the blue circle was not moved independently of the sea lion's own actions. Manual progression changed the trial layout rather than supplying a moving cursor that might be mistaken for an animal-produced movement.

The distinction separated attention to the screen from control of a moving object on it. An animal could notice a changing display without yet understanding how its contact with the controller changed the position of the circle.''','Sea lion orienting toward the task display')
add('intro',1,'A success tone becomes a conditioned reinforcer','''A **conditioned reinforcer** is a signal that acquires reinforcing value through its association with other consequences. The EVE success tone was paired with reinforcement during training. The animals subsequently responded to it in a manner resembling their familiar verbal success cue.

The tone could be delivered manually while the relationship between the apparatus and reward was established. Later, software generated it when the cursor contacted a target. The same signal therefore connected early training to the consequences of independent gameplay.

Food, ice and trainer encouragement were used as reinforcements. The tone marked the relevant event, while the additional consequence followed it. This temporal organization reduced reliance on a trainer's visible movement to identify which cursor action had been successful.''','Apparatus used for tone-conditioned gameplay')
add('intro',2,'Early targets reinforce brief button contact','''**Shaping** builds a behavior through successive approximations to the desired response. In the first Cursor Training Game phase, targets were placed near the cursor so that brief button contact could produce success. The initial task emphasized producing an effective input rather than fine positional control.

Trials distributed targets across directions, requiring different buttons over the course of the phase. Some arrangements required contacting several targets before the trial advanced. This design reduced the usefulness of repeatedly pressing only one favored button.

The researchers modified early layouts when unrestricted movement allowed animals to continue along empty parts of the display. Added walls constrained that movement and increased opportunities for successful direction changes. Acquisition depended on both the animal's experience and the evolving task layout.''','Training phases with nearby targets and walls')
add('intro',2,'Walls isolate the direction that earns reinforcement','''In the second training phase, a target lay in one rewarded direction and walls restricted movement in incorrect directions. A **response bias** is a tendency to select an action independently of the current problem; the investigators observed early preferences for particular buttons.

Target arrangements were changed to require neglected directions. The trainers sometimes used an additional disconnected button as a prompt during early acquisition. The relevant response gradually became pressing a functional directional button rather than contacting any convenient part of the box.

Walls made some errors ineffective while allowing the appropriate movement to produce a tone. Their role was to support acquisition of directional relationships. Performance in this constrained environment must be distinguished from selecting the correct direction when all movements remain possible.''','Directionally constrained training displays')
add('intro',2,'Sustained contact produces a longer movement','''The third phase permitted cursor movement in all four directions. Success required sustained contact with the appropriate button rather than only a brief touch. The animal had to relate the duration of its action to continued travel on the display.

**Motor precision** in this preparation concerns when to begin, continue and stop an input. Holding a button could bring the cursor closer to a target, but continuing after passing its relevant position could make a subsequent movement more difficult.

The task therefore added a temporal component to the directional relationship learned earlier. The same button retained its direction, while the useful duration depended on the target's position. Training advanced from producing an effective movement to regulating how far that movement continued.''','Task layouts requiring directional cursor travel')
add('intro',2,'Interior targets require stopping before a wall','''In later training, targets were positioned away from the display boundaries. Earlier wall-guided behavior allowed an animal to hold a button until the cursor stopped at an edge. Interior targets required interrupting movement before such an external stop occurred.

The investigators described this change as a substantial challenge for some sea lions. Trainers sometimes used an established wait cue to interrupt a press and provide an opportunity to switch directions. This assistance differed from identifying the target or moving the circle for the animal.

Controlling an interior position required combining visual feedback with release of the current button. The task no longer rewarded a rule based only on reaching a boundary. Its geometry changed the point at which the animal needed to alter its action.''','Interior targets in later training phases')
add('intro',2,'Opposing targets require switching directions','''The fifth training phase placed fewer targets on opposing parts of the screen. A trial could require movements in different directions before it ended. The appropriate button sequence depended on the locations still requiring contact rather than on one fixed directional response.

A **response sequence** is an ordered series of actions. Here, releasing one button and selecting another changed the trajectory of the same cursor. The animal had to maintain the overall target-contact goal while changing its immediate movement.

The investigators varied display arrangements to discourage learning a single repeated sequence. Successful gameplay consequently required continued use of the visual layout. A memorized order that worked for one arrangement would not necessarily reach the remaining targets in a different trial.''','Opposing targets requiring direction changes')
add('intro',2,'One small target demands precise cursor placement','''The final training phase presented one small target at varying screen positions. The cursor began in a common location, but the required movements differed across trials. Success required bringing the controlled circle into contact with that target without relying on multiple nearby alternatives.

**Feedback control** uses the consequences of an action to adjust subsequent behavior. Sea lions were observed switching buttons when the cursor reached a wall or traveled in an inappropriate direction. These adjustments linked visible movement to the next selected input.

Later games retained the acquired cursor-driving skill while changing the decision to be made. The training phase thus supplied an input-control foundation. It did not by itself establish that the animal understood the matching rule or planning demands introduced in another game.''','Final single-target cursor training')
add('failure',1,'An automated feeder follows programmed success','''An automated feeder linked the game's success signal to delivery of fish or ice. Software communicated with a microcontroller, which operated a valve. The resulting pressure change moved water and a piston through a tube, pushing reinforcement toward the animal.

**Automated reinforcement** connects a recorded event to a consequence without requiring the trainer to make every delivery. In the EVE studies, automated feeding and trainer-delivered reinforcement were both used, with different exposure histories across animals and training periods.

The feeder therefore changed part of the social context of a session as well as the delivery mechanism. Its introduction did not remove every human influence: staff still managed sessions and the apparatus. The published records distinguish feeder use from the animal's underlying cursor-control performance.''','Sea lion using EVE with the automated feeder')
add('welfare',1,'Voluntary participation varies with the session','''EVE sessions depended on animal interest, performance, staffing and the reinforcement available from the daily ration. Participation was voluntary, and sessions ended when disengagement or frustration was observed. The duration was therefore not imposed as one identical exposure for every animal.

In the apparatus study, one sea lion continued some sessions for more than **30 min** when ice and encouragement were the available reinforcements. This observation broadened the recorded consequences beyond delivery of fish alone, while retaining the animal's established training context.

Session length and willingness to interact are behavioral outcomes that require interpretation alongside the task and reward history. Long participation is different from accurate performance, and neither measure alone captures all aspects of welfare or motivation.''','Sea lion participating in a supervised game session')
add('intro',4,'Target-contact latency declines during training','''**Latency** is the time between a defined starting event and a response. EVE latency to success was measured from the first button contact to cursor contact with the target. This definition excludes the time before the animal initiated that trial's movement.

Across the final training sessions, latency to target contact declined for each sea lion. The result concerns improvement within a common single-target phase, after the earlier steps had established how to operate the directional controller.

Faster target contact can result from more direct routes, appropriately timed releases or reduced periods without effective input. The latency measure combines these possibilities. Recorded button sequences provide additional information about how the same final contact was achieved and how performance changed across sessions.''','Latency across final training sessions',('intro',2,'Single-target task underlying the latency measure'))
add('intro',5,'Button efficiency changes differently across animals','''**Response efficiency** concerns how much action is used to obtain a specified outcome. During final cursor training, the number of button presses per trial declined for ANK and SLD, whereas REX's count remained comparatively stable. Faster performance and fewer presses were therefore not identical outcomes.

Each press marked a change or continuation in the animal's interaction with the controller. More presses could represent unnecessary movements, but could also reflect shorter corrective adjustments. The count must be interpreted together with press duration and the resulting route.

Individual differences persisted within the same nominal task. Training history, session availability and early apparatus modifications differed among the sea lions. These records support describing distinct acquisition trajectories rather than assigning one uniform cursor-learning pattern to the species.''','Button presses across training sessions',('intro',7,'Animal performing the cursor task'))
add('intro',6,'Acquisition criteria combine speed and input count','''A **criterion** specifies the performance required before training advances. For the Cursor Training Game, progression required consecutive sessions with an average latency below **6 s** and an average input count below seven presses per trial. Both features had to be considered.

These thresholds were grounded in the movement demands of the final phase. Many trials could be solved with two appropriately directed presses, while a route along a horizontal and then vertical boundary took approximately **3 s**. The criterion permitted variation around an efficient solution.

Additional sessions were provided when earlier qualifying performance was variable. Passing the criterion therefore reflected sustained control across sessions rather than one unusually rapid trial. All of the focal sea lions ultimately progressed to games with additional cognitive demands.''','Individual input counts and target-contact latencies',('intro',2,'Training display used for acquisition'))
add('failure',3,'An incorrect choice can end a trial without reward','''**Failure** in the gameplay study meant an incorrect decision ended the current opportunity for reinforcement. The earlier cursor-training task allowed continued attempts until the target was reached. The advanced tasks therefore changed the consequences of an error, not simply the appearance of the display.

After an incorrect outcome, the display froze for **3 s** before the next trial loaded. Button presses during that interval did not rescue the previous trial. The animal encountered a boundary between continued exploration within a trial and the termination of that opportunity.

The investigators subsequently returned the animals to the familiar cursor task. Comparing performance before and after advancement addressed whether exposure to unsuccessful outcomes was followed by reduced engagement or changes in the already acquired control skill.''','Advanced maze and matching displays')
add('failure',3,'Maze choices determine where the cursor falls','''The MAZE game restricted cursor movement to left and right choices. The cursor traveled along platforms and could fall toward a target below them. A correct choice of direction and drop location allowed target contact; an incorrect route could send it off the display.

**Planning** concerns selecting actions in relation to a later outcome. The maze imposed such an opportunity by making the consequence of a horizontal choice depend on the platform below. Introductory trials simplified this relationship before more complex arrangements were presented.

REX encountered the maze, whereas the other focal animals entered matching tasks. Their advancement conditions therefore differed. Subsequent comparisons in the common cursor task concern their experience of changed consequences, rather than equivalent exposure to one identical advanced problem.''','Maze training arrangement and matching alternatives')
add('failure',3,'Matching requires selecting the sampled shape','''**Matching-to-sample** presents a sample and then alternatives, one of which shares the relevant property of that sample. In the EVE matching task, the sea lion first moved the cursor into a displayed shape. The program then presented that shape and a different alternative.

The rewarded choice was the shape matching the sample. Unlike the maze, movement was not restricted to left and right. Cursor-control skill was necessary to reach an alternative, but the matching relation determined which contact produced reinforcement.

An incorrect selection froze the screen and ended the opportunity to retry that trial. The same motor interface therefore supported a new cognitive requirement. Successful navigation to a visible object was distinguishable from choosing the object that satisfied the sampled relation.''','Sample presentation and two matching alternatives')
add('failure',4,'Targeting and staircasing are different movement strategies','''A **strategy** is an operationally defined pattern of behavior used during the task. The gameplay researchers coded movements such as targeting and staircasing rather than treating every successful route as equivalent. The definitions linked observed button presses to the cursor's trajectory.

Targeting involved directing movement toward the target, whereas staircasing alternated directions to create a stepped route. Both could result in contact, but they differed in the sequence used to approach the goal. Video coding supplemented the automatically recorded input data.

Targeting was frequent in the recorded behavior, and staircasing remained prominent after advancement. The coded categories describe recurring movements under the experimental rules. They are not direct measurements of the animal's internal representation of the target or its conscious intention.''','Strategy frequencies before and after advancement',('failure',2,'Cursor task used for strategy coding'))
add('intro',7,'Wall-guided movement can persist into later tasks','''**Wall surfing** uses the boundary of the display as part of the movement route. An animal can hold a direction until the cursor contacts an edge, then change direction along that boundary. Early training made this approach useful because walls constrained movement.

Interior targets created a different demand. Continuing to the edge could carry the cursor away from the target's useful position, making subsequent correction necessary. The apparatus investigators observed this persistence and sometimes interrupted presses with a familiar wait cue.

The strategy study separately coded circling, diagonal movements and other recurring routes. These categories made it possible to distinguish reaching the target from how it was reached. Transfer to a harder layout required adjustments to movements previously reinforced in simpler conditions.''','Animal controlling a cursor toward an interior target')
add('failure',5,'Shorter strategy episodes can contain more presses','''After advanced gameplay, the animals spent less time in an average coded strategy episode while making more button presses within an episode. The aggregate duration changed from approximately **2.10 s** to **1.24 s**. These outcomes describe temporal organization as well as movement frequency.

The combined mean press count per strategy increased from approximately 2.12 to 2.67. Shorter contact periods with more distinct inputs are compatible with finer adjustments rather than prolonged holding of one button. The recorded movement and duration measures specify the behavioral change.

An increased number of presses is therefore not automatically a sign of poorer control. Its meaning depends on the temporal scale being measured. Counting inputs within an episode differs from counting all inputs required to complete an entire trial.''','Duration and input count for coded strategies')
add('failure',7,'Time without input differs from time spent pressing','''The game recorded total latency to target contact and the cumulative time spent contacting buttons. **Latency without contact** was the remaining interval during which the trial was progressing but no directional input was being produced. The measures address different components of performance.

Time without input can reflect observation, hesitation or disengagement, and the recorded interval does not distinguish these states by itself. Interpreting it as interest requires the animal's behavior and the surrounding conditions rather than assuming every pause has one cause.

After advancement, the recorded noncontact interval declined for ANK and SLD, while REX had remained relatively low across conditions. The result supports a comparison of participation within the familiar task, alongside route efficiency and the time spent actively manipulating the controller.''','Noncontact latency across animals and conditions',('failure',2,'Controller-based cursor task'))
add('failure',6,'Familiar-task performance improves after advancement','''The investigators compared final cursor training with cursor-task sessions offered after the animals entered games containing failure. Combined mean trial latency declined from **9.80 s** to **3.42 s**, and total time contacting buttons declined from **6.87 s** to **1.80 s**.

These changes were measured in the familiar task rather than by comparing unlike maze and matching outcomes. Returning to that common preparation provided a consistent response requirement across the two periods. Individual starting latencies differed, but post-advancement latencies were more similar.

The before-and-after sequence also included continued practice, so failure exposure was not isolated from every other learning experience. The behavioral finding is sustained engagement and improved familiar-task performance following advancement, rather than a randomized demonstration that failure alone produced the improvement.''','Trial latency before and after advanced gameplay',('failure',3,'Advanced tasks that introduced failure'))
add('matching',1,'Physical-object matching separates sample and choices','''Pack and colleagues trained a California sea lion with three-dimensional objects rather than a computer controller. A sample object was presented, followed by comparison objects from which the animal selected the matching item. **Identity matching** requires choosing the same object type as the sample.

The apparatus arranged the sample and alternatives in distinct positions. Reinforcement depended on the selected relation, not on operating a directional cursor. This preparation supplies a comparison between a cognitive rule and the particular motor interface used to report it.

The sea lion acquired the trained matching problem and was subsequently tested with new objects. That separation allowed the investigators to ask whether performance reflected only particular rewarded objects or a relation that could extend beyond the initial training materials.''','Published drawing of the physical matching apparatus')
add('matching',3,'Novel objects test generalization of matching','''**Generalization** is extension of learned performance to stimuli or situations outside the initial training set. The sea lion's transfer tests introduced objects that had not been used in the original matching training. Some tests retained one familiar object, whereas others used novel objects throughout.

Across successive transfers, acquisition of the matching problems generally required fewer errors. Later tests approached the animal's well-established baseline matching performance. This progression was more informative than accuracy on the original trained pair alone.

The animal sometimes reacted cautiously to unfamiliar objects, complicating interpretation of its very first encounters. Novelty can affect willingness to select an object independently of knowledge about the matching relation. The investigators consequently considered performance over transfer trials as well as immediate responses.''','Matching accuracy across novel-object transfer sets')
add('matching',5,'Sample removal turns matching into a memory task','''In **delayed matching-to-sample**, the sample is removed before the comparison choices are presented. The intervening **retention interval** separates seeing the sample from reporting the matching choice. The sea lion therefore had to retain information about an object no longer available to inspect.

Matching performance remained at **78% correct or better** through delays of **45 s**. At the longest tested delay, **58 s**, performance declined to **69% correct**. The temporal manipulation connected the choice outcome to the duration for which sample information had to be maintained.

The response was still a physical-object selection, so motor control requirements were retained while the memory demand changed. Matching accuracy at a particular delay concerns memory under this trained procedure, rather than a general estimate of every form of sea-lion memory.''','Matching accuracy across retention intervals')
add('matching',6,'Practice and retention interval influence performance','''Repeated exposure to delayed matching provided additional experience with the requirement to choose after the sample disappeared. The investigators tracked performance as a function of practice as well as delay, distinguishing improvement in the procedure from the effect of waiting longer.

The sea lion's accuracy changed across delayed-matching sessions while remaining sensitive to the retention interval. A long wait and an unfamiliar task can both reduce successful choices, but they are different experimental demands. Session records help separate their contributions to the observed trajectory.

The preparation also retained the previously acquired identity relation. Delay was introduced after matching could already be performed with the available sample. This ordering made the later outcome interpretable as delayed use of a learned relation rather than initial acquisition of both matching and memory requirements together.''','Delayed-matching performance across practice')
add('transfer',3,'Multiple exemplars support an identity relation','''Kastak and Schusterman trained sea lions across numerous identity-matching problems before introducing novel transfer problems. An **exemplar** is a particular instance of the relation being learned. Varying exemplars changes which objects carry the same rewarded relation.

The researchers distinguished learning separate conditional associations from acquiring a more general identity rule. The same physical stimulus can appear as a sample or comparison in different trials, so a successful selection must depend on the current relation rather than one object's permanent reward status.

Novel transfer performance improved after extensive exemplar training. The animals did not reach the strongest generalization criteria at the same point, emphasizing that the relation emerged through different learning histories. Performance on unfamiliar problems supplied evidence beyond repetition of previously reinforced choices.''','Transfer performance following exemplar training')
add('transfer',4,'First-trial choices provide a strict transfer test','''A **transfer test** assesses a learned relation under a changed stimulus set. The identity-matching study evaluated the first choice on novel problems as well as performance over several trials. A correct first response cannot result from reinforcement delivered later within that particular problem.

The investigators also compared test trials with established baseline trials and evaluated short problem blocks. These complementary measures distinguished immediate use of the identity relation from rapid learning after initial errors. The animals eventually satisfied the study's combined criteria for generalization.

The procedure preserved the same matching requirement while changing its specific materials. Successful transfer therefore linked earlier exemplar training to new choices. It did not require that every novel stimulus be equally attractive or that the animals display identical learning rates across successive tests.''','First-trial and short-block transfer criteria')
add('transfer',7,'A prior stimulus history can compete with identity','''The second experiment used stimuli previously learned in another context. A **learning history** includes the relationships through which an animal has encountered a stimulus and its consequences. An object can therefore carry associations that differ from the identity relation currently required.

The sea lions were asked to apply identity matching to these previously experienced materials. The test addressed whether the generalized matching relation extended beyond wholly unfamiliar objects to items with other learned significance. Earlier experience was a relevant feature of the new problem rather than background information to ignore.

The study reported successful transfer under its evaluation criteria. Together with novel-stimulus tests, the result supports a relation usable across different stimulus histories. Cognitive testing thus benefits from specifying both the current reward rule and the associations acquired before the present experiment.''','Identity matching with previously experienced stimuli')
add('reversal',1,'Reversal changes which stimulus earns reinforcement','''**Reversal learning** changes the rewarded alternative after an animal has acquired a discrimination. Erdsack and colleagues trained harbor seals to select one of two visual patterns, then exchanged the reward assignments. The formerly correct response became incorrect without changing the response apparatus.

The seals indicated choices by contacting a response target below the selected pattern. This was a physical visual-testing apparatus, not a touchscreen or EVE cursor game. A correct selection was followed by an acoustic signal and food reinforcement.

The comparison isolates a change in the learned contingency from initial recognition of the alternatives. Continuing to choose the formerly rewarded pattern produces errors after reversal. Successful adjustment requires behavior to become sensitive to the new consequences despite the previous selection history.''','Harbor-seal visual discrimination apparatus')
add('reversal',3,'Repeated reversals reveal individual flexibility','''**Behavioral flexibility** is adjustment of behavior when the conditions determining success change. Serial reversal learning repeatedly exchanges which stimulus is rewarded after the current discrimination has been acquired. The harbor-seal study tracked errors across these successive changes.

One seal completed **37 reversals** and progressively improved, reaching a minimum of six errors in the thirty-third reversal. Other individuals showed much more limited progress. The findings therefore identify a demonstrated capacity within a variable set of individual outcomes.

A faster later reversal suggests that previous changes affected how the animal approached another change in consequences. It is different from simply recognizing the same visual patterns more quickly. The repeated-contingency procedure evaluates adaptation to reward reassignment using a consistent sensory and response preparation.''','Errors across successive reversals in one seal')
add('reversal',6,'Side preference can conceal the rewarded relation','''A **side preference** is a tendency to choose a position rather than the currently rewarded stimulus. In a two-choice apparatus, a strong positional tendency can reduce accuracy even when the animal can perceive the patterns. The reversal study tracked side choices alongside discrimination performance.

Stimulus position and stimulus identity were therefore distinct variables. Changing which pattern was rewarded did not necessarily remove a tendency to respond repeatedly on one side. Records of those choices supplied information about how an animal approached the task.

The distinction also applies to designing computerized tests: a task should prevent one fixed location from consistently identifying success. In the EVE training study, variation in target position served this purpose. Physical and computerized interfaces can address comparable control problems through different response arrangements.''','Side preferences during serial reversal learning',('intro',2,'Variable target positions in computerized training'))
add('personality',3,'Personality ratings describe recurring behavioral traits','''**Personality** refers to recurring differences in behavior among individuals across observations. Ramos and Winship used ratings of sea-lion traits and related them to recorded computerized gameplay. The ratings described tendencies such as perceptiveness, affability, persistence and reactivity.

The analysis grouped related ratings into broader trait clusters. These clusters summarized the recorded behavioral descriptions rather than identifying discrete kinds of animal. An individual could receive different scores across several clusters, producing a profile instead of one exclusive category.

The resulting profiles were compared with task latency and button-use measures. This combination linked observations outside a particular cursor trial to behavior within the computerized preparation. The study addressed individual variation, with trait labels remaining operational summaries of rated behavior.''','Published grouping of rated personality traits')
add('personality',5,'Individuals combine traits in different profiles','''The personality study found distinct combinations of rated traits across sea lions. Some animals received high cognitive and diligent ratings with low insecurity ratings, while others had different balances across the same dimensions. **A personality profile** describes that combination of scores.

The authors retained multiple dimensions rather than placing every animal into one mutually exclusive cluster. The same overall task therefore involved participants with different patterns of behavioral tendencies. Such patterns can influence how animals approach unfamiliar stimuli, trainers and repeated opportunities to respond.

The ratings were considered alongside prior task experience and the measured gameplay variables. A profile is not a direct record of how a particular trial was solved. Its relevance comes from associations with the animal's responses, evaluated against the defined task and its conditions.''','Individual profiles across personality dimensions')
add('personality',5,'Rated perceptiveness is associated with faster responses','''The investigators related personality-cluster ratings to latency during computerized gameplay. Higher perceptiveness ratings were associated with faster responses in initial sessions and remained associated with quicker responding later. Higher dominance ratings also accompanied faster initial responses and fewer initial button presses.

These outcomes distinguish time to success from the amount of controller input. A sea lion can differ on either measure, and the personality associations were not identical across all measures or training periods. The comparison concerns recorded behavior within the EVE task.

Because the traits were rated rather than experimentally assigned, their associations do not establish that changing a trait would change performance. The findings support considering individual tendencies when interpreting response trajectories and selecting an appropriate level of task challenge.''','Trait profiles related to response measures',('personality',1,'Computerized task used for response measurements'))
add('personality',5,'Affability is associated with improvement over sessions','''Higher affability ratings were associated with a greater reduction in gameplay latency over training. **Improvement** here means a change in the recorded response time across sessions, not simply high accuracy or fast performance in the first session.

The distinction separates an initial behavioral tendency from the trajectory of learning. The same preparation can reveal differences in starting performance and in subsequent change. These measurements give different information about how an animal interacts with the task over repeated opportunities.

The study's associations provide a basis for testing individualized enrichment, but the reported analysis did not experimentally compare alternative personalized programs. A proposed design implication is to adjust difficulty and engagement opportunities while continuing to record the animal's actual response, rather than relying on its trait label alone.''','Personality profiles considered with learning trajectories',('personality',2,'Different games available through the same interface'))
add('welfare',1,'Food consumption is a separate welfare-related outcome','''The welfare study examined daily food records before and after EVE was introduced. **Incomplete consumption of the offered diet** meant the animal did not consume its planned daily ration. The measure extended beyond response speed or success within a single computerized trial.

The investigators focused on sea lions with histories of incomplete consumption and compared their records with other animals. Food provided during EVE sessions formed part of the existing daily diet rather than an unrestricted addition to it. Veterinary and husbandry records supplied the broader context.

Consumption was treated as a proxy for participation and health-related interest. The animals' sea pens also contained natural fauna, so offered-diet consumption was not an exhaustive measure of everything ingested. The experimental interpretation depends on that particular managed-feeding context.''','Sea lion participating in a reward-based EVE session')
add('welfare',2,'Incomplete-consumption days decline after EVE begins','''The study compared two-year periods before and after the introduction of computerized enrichment. Incomplete-consumption days declined from **61 to 18 days** for REX and from **40 to 15 days** for SLD. The control animals did not exhibit the same pattern of improvement.

The comparison retained individual histories instead of reporting only the combined population. Both focal animals had been selected because their earlier feeding records suggested a potential benefit from additional cognitive engagement. This selection matters when considering which animals the findings directly describe.

The control records help distinguish the focal change from an improvement shared by the entire managed population. The design was a longitudinal husbandry comparison rather than a randomized assignment of enrichment. Its evidence concerns changes associated with introducing EVE within the animals' existing care.''','Incomplete-diet-consumption days across two periods',('welfare',1,'EVE session context for the feeding records'))
add('welfare',3,'The offered-consumed difference also becomes smaller','''The authors separately measured the difference between the amount of diet offered and the amount consumed. This **diet difference** describes the size of the unconsumed portion, whereas an incomplete-consumption day records whether any such difference occurred at all.

For REX, the mean difference declined from approximately **0.44 lb to 0.11 lb**; for SLD, it declined from approximately **0.38 lb to 0.08 lb**. The control animals did not show a comparable decline across the same periods.

These measures provide complementary descriptions of the feeding outcome. Fewer incomplete days and smaller unconsumed portions indicate a different pattern of participation in offered feeding opportunities. The study linked that pattern to the broader enrichment and care history rather than substituting gameplay success for a direct feeding record.''','Mean offered-consumed diet difference',('welfare',1,'Animal using the reward-based enrichment interface'))
add('welfare',2,'Clinical records help interpret apparent welfare changes','''The welfare analysis excluded acutely ill days from the primary food-consumption comparison because illness and treatment can change appetite. The investigators also examined clinical records separately, retaining a distinction between the feeding measure and veterinary assessment.

Clinically ill days declined for the focal animals across the two periods, while a control animal experienced illness in the later period. These records added health context to the enrichment-associated feeding changes. They were not generated by the game's latency or button-count logs.

Assessing enrichment therefore requires several outcomes: performance under the task's contingencies, voluntary participation, feeding records and health history. The published study combined these observations within managed care. A design that retains those distinctions can evaluate an animal-controlled interface without treating every successful cursor contact as evidence of improved welfare.''','Feeding outcomes interpreted alongside clinical records',('welfare',1,'Sea lion interacting with computerized enrichment'))
assert len(slides)==44,len(slides)
takeaways=[
'**Interface demands:** EVE separates a visual display from four directional buttons; cursor control differs from direct touchscreen selection.',
'**Reward contingencies:** Shaping, success tones and reinforcement establish effective actions before the animal enters more demanding games.',
'**Distinct cognitive tasks:** Cursor navigation, identity matching, delayed matching and reversal learning test different requirements.',
'**Failure and adaptation:** The published advancement study retained engagement and improved familiar-task performance after games introduced unrewarded errors.',
'**Individual variation:** Response trajectories and rated personality profiles differ among sea lions and must be considered alongside task history.',
'**Welfare evidence:** Gameplay metrics, offered-diet consumption and clinical records describe different outcomes and require separate interpretation.']
spec={'lecture':94,'theme':'marine-steel-paper','content_slides':44,'title_image':figure('intro',7,'Sea lion operating the computerized cursor interface'),'slides':slides,'takeaways':{'items':[{'lead':t.split('**')[1], 'text':t.split('**')[2].strip()} for t in takeaways], 'cite':'Winship et al. (2023, 2024); Roberts et al. (2023); Ramos & Winship (2025)','transcript':[t.replace('**','')for t in takeaways],'refs':[R[k]['reference']for k in R]}}
(B/'lecture.json').write_text(json.dumps(spec,indent=2,ensure_ascii=False)+'\n')
(B/'PLAN.md').write_text('# Lecture 94 slide plan\n\n'+'\n'.join(f'{i+2}. {s["title"]}'for i,s in enumerate(slides))+'\n')
print(len(slides),'content slides')
