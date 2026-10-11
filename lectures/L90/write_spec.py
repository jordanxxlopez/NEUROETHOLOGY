"""Source-grounded Lecture 90; rebuild with repository tools, then embed_media.py."""
import json
from pathlib import Path
B=Path(__file__).resolve().parent
R=json.loads((B/'research.json').read_text())
slides=[]
def fig(k,n,desc):
 return {'kind':'article','path':f'figures/{k}_{n}.png','caption':f"{R[k]['short']}, Fig. {n}. {desc}",'source_url':'https://doi.org/'+R[k]['doi']}
def add(k,n,title,text,desc,extra=None):
 body=text.strip().split('\n\n');assert len(body)==3,(title,len(body));assert len(title)<=62,title
 s={'title':title,'layout':'figure-right','body':body,'figure':fig(k,n,desc),'cite':R[k]['short'],'refs':[R[k]['reference']],'transcript':body.copy()}
 if extra:s['layout']='figures-right';s['figures']=[s.pop('figure'),fig(*extra)]
 slides.append(s)
add('elephant',2,'Mirror use is defined by behavior directed at the body', '''**Mirror self-recognition** is the use of a reflection as information about one's own body. A mark test places a visible change on a body surface that the animal cannot inspect directly. A positive response is directed toward the actual body rather than toward the reflected animal.

An Asian elephant named Happy received a white X on one side of her head and an invisible sham X on the other. The sham mark matched handling and application while withholding the visible change. Her trunk contacted the visible-mark side after mirror inspection.

Body inspection, repeated movements and social displays are separate behavioral categories. They can precede a mark response, but only the mark response tests whether information at the reflective surface guides action toward the corresponding body location.''','Happy bearing a visible mark and touching her head')
add('elephant',1,'A large accessible mirror permits elephant inspection','''The elephant experiment used a mirror approximately **2.5 m tall**, installed in the animals' yard and available for close investigation. Accessibility permitted trunk contact and inspection of surfaces that a distant or small mirror would not expose clearly.

The same installation was tested with its reflective surface covered. Happy spent 19.4% of observation time near the open mirror, compared with 0.2% near the covered mirror. Maxine and Patty also spent much more time near the open surface.

A covered mirror preserves the position and much of the apparatus while removing the reflected body. The open-versus-covered comparison therefore separates attraction to reflected visual information from interest in a novel wall fixture or its location.''','Published layout of the accessible mirror and elephant yard')
add('elephant',2,'Elephants inspect otherwise inaccessible body surfaces','''Before marking, the elephants made unusual movements while facing the open mirror. They opened their mouths and moved their trunks around the mouth and ears. These actions exposed body surfaces that ordinary forward vision cannot inspect.

**Contingency checking** means testing the relationship between one's movements and changes in the reflected image. Repetitive movements in front of the mirror differed from routine feeding and from social interaction with another elephant. Self-investigation emerged after several days of access.

Happy met the authors' behavioral readiness criterion within 3 days; Maxine and Patty did so within 4 days. Mirror exploration and body inspection occurred in animals that later differed in their mark-test performance. Familiarization and successful mark responding are therefore distinct outcomes.''','The marked elephant and mirror-directed trunk movement')
add('elephant',3,'Happy touched the visible mark after mirror exposure','''During or within **90 s** after proximity to the mirror, Happy made 12 touches that contacted or approached the visible mark. None contacted or approached the sham mark on the opposite side. Touches within 20 cm of the mark were included in the location criterion.

The visible and sham applications controlled for handling and nonvisual sensations. Happy's usual head touching in baseline and covered-mirror conditions lacked the strong bias toward the subsequently marked side. Her response depended on a newly visible body feature.

Maxine and Patty did not produce equivalent mark-directed responses despite their earlier mirror exploration. The positive result identifies mirror-guided action in Happy under these conditions; the individual differences remain part of the biological result rather than evidence for uniform performance by elephants.''','Head-touching rates in mark, open, covered and baseline conditions')
add('dolphin',2,'Dolphins expose marked body regions to reflective surfaces','''Bottlenose dolphins lack grasping hands and cannot use the manual mark-removal response typical of an ape. Reiss and Marino instead scored body orientations that exposed a marked region to a reflective surface. Marks were temporary, nontoxic and placed outside direct view.

A dolphin marked near a pectoral fin could orient the corresponding side toward the reflection. Ventral marking could elicit an upward stretch that exposed the underside. The scored response therefore changed with the location of the body alteration.

Sham marking reproduced contact without leaving a visible mark. Exploratory movements that exposed a different region were scored separately from mark-directed postures. This distinction prevents all swimming near a reflective wall from being counted as body recognition.''','Mark locations and a dolphin with an experimental mark')
add('dolphin',3,'Early sham marking elicited little dolphin inspection','''In early sham trials, before genuine marking, a dolphin spent only **0.3%** of observation time in sham-directed behavior at reflective surfaces. With visible marks, mark-directed behavior occupied 6.1% of observation time. The measured variable was body inspection rather than generic mirror proximity.

An early sham bout lasted 8 s during the initial control sessions. The low response before visible marking weakens a simple explanation in which skin contact alone causes the animal to present that body region to a reflection.

Later sham trials elicited more checking than early sham trials. Experience with visible marks altered the significance of subsequent handling. The order of exposure matters because a control applied after learning can carry a different expectation from an identical control applied beforehand.''','Inspection time and latency under marking and sham conditions')
add('dolphin',4,'Dolphin postures track the site of an expected mark','''A dolphin performed **12 dorsal-to-lateral-to-ventral flips over 32 s** while exposing the sham-treated underside and tip of its right pectoral fin. The sequence followed prior experience with real marks and was directed toward the best available reflective surface.

The experiment also compared a real mirror with an opaque covering at the same location. Marked dolphins spent more time at an uncovered mirror than at the covered installation. This comparison separated the reflected image from the physical mirror location.

The body-region specificity links the posture to information about the dolphin's own body. The authors also scored social threats and invitations to interaction separately; those categories did not account for the observed mark-directed inspection.''','Region-specific inspection at the best reflective surface')
add('chimptract',1,'Chimpanzee frontoparietal tracts link body-related cortex','''The **superior longitudinal fasciculus**, or SLF, is a system of white-matter pathways connecting frontal and parietal cortex. Hecht and colleagues reconstructed its second and third branches in chimpanzees using diffusion magnetic resonance imaging, which estimates tissue organization from water diffusion.

Anatomical target regions included inferior parietal cortex and frontal regions involved in action production and perception. SLF III extended toward ventrolateral prefrontal cortex, including the chimpanzee homologue of Broca's area. A homologue is a region related by common ancestry.

Probabilistic tractography estimates likely pathways from diffusion patterns. It measures structural organization rather than neurons firing during mirror inspection. Anatomical variation was compared with independently scored mark-directed behavior, preserving the distinction between connectivity estimates and behavioral performance.''','Frontal and parietal regions used to quantify tract terminations',('chimptract',2,'Diffusion-based reconstructions of SLF II and III'))
add('chimptract',5,'Rightward SLF asymmetry relates to recognition','''Chimpanzees with compelling mark-test performance had greater **rightward asymmetry** in SLF II and SLF III white matter. Rightward asymmetry means that the measured feature was larger on the right than on the left, rather than that the left pathway was absent.

SLF III terminations in the Broca's-area homologue also differed across negative, ambiguous and compelling performance categories. The right prefrontal extension became more pronounced in the category with the clearest mirror-directed mark behavior.

The structural relationship is a correlation between anatomy and performance. A proposed explanation is that frontoparietal body and action representations support matching reflected movements to the animal's body. The study did not manipulate the tract or establish its necessity for the behavior.''','SLF III terminations across mirror-recognition categories',('chimptract',3,'Hemispheric asymmetry of the measured pathways'))
add('chimpthickness',2,'Recognition relates to regional cortical thickness','''**Cortical thickness** is the distance between the gray-matter boundaries reconstructed from magnetic resonance images. Hopkins and colleagues compared this measure across chimpanzees classified by repeat mark-test performance. Their analysis examined both individual surface locations and predefined anatomical regions.

Consistently positive animals had thicker anterior cingulate cortex in parts of both hemispheres. They had thinner cortex in portions of the precentral and postcentral gyri, especially on the left. The relationship therefore differed across regions rather than reflecting universally thicker cortex.

Sex also modified several regional associations. These are anatomical associations with behavioral classification, not recordings of a self-specific neural signal. The cingulate and sensorimotor pattern supports regional hypotheses about body-related processing while preserving the opposite directions of the reported thickness effects.''','Surface maps of thickness differences between recognition groups')
add('bonobo',3,'Mirror experience alters bonobo responses to self footage','''Bonobos initially looked briefly at live contingent self-video and mirror reflections, but longer at prerecorded self footage. **Noncontingent** footage does not change immediately with the viewer's current movements. Each test stimulus was presented for 30 s.

After 3 months of freely available mirror access, median looking time to prerecorded self footage fell from 22.1 s to 7.4 s. Looking at unfamiliar individuals remained similar, at 18.1 s before exposure and 18.5 s afterward. Retesting occurred almost 2 years after the initial trials.

The identity-dependent change is preliminary evidence consistent with greater familiarity with the self-image. Looking time measures visual interest, not mark removal. The embedded Movie S1 is an example of the bonobo footage used as a stimulus, rather than a video of a subject recognizing itself.''','Looking time before and after prolonged mirror access')
add('monkeyimplant',1,'Rhesus monkeys use mirrors to groom around implants','''Rhesus macaques in Rajala and colleagues' study used small mirrors to inspect parts of their bodies. Some animals groomed around a surgically implanted head device while watching its reflection. The device provided an unusually salient visual and tactile body feature.

In Movie S1, a monkey wakes, reaches for the mirror and positions it before grooming near the implant. A green cheek mark remains visible. That animal failed the conventional colored-mark test, despite the mirror-guided grooming behavior.

Mirror-assisted body inspection and success in a standard mark test can dissociate within one animal. The implant context changes experience and motivation, so the result concerns the observed inspection behavior rather than an interchangeable replication of spontaneous colored-mark recognition in an unimplanted monkey.''','Mirror-guided inspection of the body and implant')
add('monkeyimplant',4,'Body inspection persisted after implant removal','''After the head implant was removed, a rhesus macaque continued using a small mirror to inspect its lower body and genitals. The animal adjusted the mirror and its posture to obtain a view of body surfaces that were otherwise difficult to inspect.

Movie S3 records the monkey looking over its shoulder and moving a hand between its legs. It pushes the genital region into view near the end of the recording. This coordinated adjustment links mirror position, body posture and access to a particular body surface.

The recording separates continued body inspection from the immediate presence of the implant. It does not erase the animal's earlier experience. Mirror use following that history differs from a claim that an experimentally naive macaque would produce the same inspection without familiarization.''','Mirror-assisted body inspection without the head implant')
add('monkeytrain',1,'Precise training changes mirror-guided reaching','''**Proprioception** is information about the position and movement of the body. Chang and colleagues trained rhesus macaques to reach toward a light location seen through a mirror. The task connected a reflected visual location to a real reaching movement.

Initial training with a ball reached 100% accuracy, but even 2 additional weeks at this stage did not produce successful facial mark responding. A subsequent board task varied target positions and demanded more precise correspondence between the reflection and the reach.

After several days of the more precise training, reaching accuracy again reached 100%. The animals received another 2 weeks of stabilization. The transition from coarse targeting to precise spatial matching identifies the learned association that preceded transfer to reflected body locations.''','Training apparatus, target positions and reaching performance')
add('monkeytrain',2,'Trained monkeys transfer mirror guidance to their bodies','''After precise reaching training, facial laser tests elicited **92–100%** correct touching. The monkeys also touched colored dye marks on the face and ear while using a mirror. The mark tests omitted the food reward used during training.

Different colors and body locations tested transfer beyond one repeatedly rewarded light position. Monkeys with comparable mirror exposure but without the precise visual-proprioceptive training did not produce the same mark-directed behavior. Mere duration of exposure was therefore insufficient under the study's conditions.

The authors called the later expression spontaneous because it occurred without a mark-test reward. Its developmental history was nevertheless experimentally trained. The result supports learned transfer from mirror-guided spatial action to mirror-guided body action, with the acquisition experience retained in the explanation.''','Mirror-guided touching after training and control comparisons')
add('macaqueSII',2,'SII recordings sample a multisensory body region','''The **secondary somatosensory cortex**, or SII, lies in the parietal opercular region near the lateral sulcus. Somatosensory signals concern touch and bodily sensation. Bretas and colleagues recorded individual neurons in this region in a Japanese macaque after mirror familiarization.

For approximately 2 weeks, the animal experienced its limbs being touched or moved while looking in a mirror. Reflected visual information was paired with bodily stimulation. The recording sites were localized with magnetic resonance images rather than inferred from behavior alone.

Individual cells were tested with tactile stimulation, directly visible approaching stimuli and stimuli visible through the mirror. The preparation allowed comparisons between visual access and bodily contact while sampling neural firing in an anatomically identified region.''','MRI localization and recording sites in SII')
add('macaqueSII',4,'SII cells respond to near-body events seen in a mirror','''A **receptive field** is the set of stimulus locations or conditions that change a neuron's firing. Some SII neurons responded when a hand approached the macaque's body, whether the approach was directly visible or seen in the mirror.

An opaque plate blocked peripheral vision during a critical control. The approaching hand could then be seen only through the mirror, yet the illustrated neuron retained its response. The firing-rate trace was aligned to the moment of closest approach and expressed in spikes per second.

Other neurons responded to a hand approaching the projected face in the mirror. The authors distinguished these mirror-image responses from ordinary near-body visual receptive fields. Reflected events can therefore access body-related neural responses without direct visual access to the stimulated location.''','A–B: responses to directly visible and reflected approaches',('macaqueSII',2,'MRI localization of the recorded SII region'))
add('macaqueSII',4,'Self-touch responses distinguish contact from movement','''A recorded SII neuron increased firing when the macaque's hand contacted its own mouth. The experimenter moved the arm passively, so arm movement and touch could be compared without requiring the animal to initiate a trained reaching action.

When an object was placed between the hand and mouth, the same movement did not elicit the illustrated self-touch response. Touching the mouth with an external object or the experimenter's hand also failed to reproduce it. The response therefore depended on the particular self-body contact configuration.

The published firing traces use a millisecond time axis aligned to touch onset. Their timing connects bodily contact to the cell's activity. Contact-selective firing is a physiological distinction between stimulus conditions, rather than direct evidence for the animal's subjective experience.''','C–D: firing aligned to self-touch and non-self touch',('macaqueSII',2,'Anatomical localization of the sampled cells'))
add('macaqueSII',5,'SII also represents touch involving another body','''Other SII neurons responded when the macaque touched an external body rather than its own. One example responded when the monkey's hand contacted the experimenter's hand, but not during a comparable movement toward its own forearm or opposite hand.

A separate illustrated neuron responded while the macaque watched the experimenter touch their own cheek. Its firing increased around the observed touch onset on the millisecond time axis. This response concerned a non-self event rather than contact with the macaque's body.

Self-touch, external touch and observed touch recruit different response profiles within a multisensory region. The recordings came from one animal, so their presence establishes possible neural response types without defining a species-wide distribution or a uniquely self-recognition-specific circuit.''','Firing during observed touch of the experimenter’s cheek',('macaqueSII',2,'SII recording-site anatomy'))
add('magpie',2,'Magpies test the contingency of their reflections','''Eurasian magpies explored mirrors with repeated head and body movements. The researchers separated aggressive social displays from inspection and **contingency testing**, in which movements probe the immediate correspondence between action and the reflected image.

Gerti and Schatzi moved back and forth or sideways while watching the reflection. In Video S3, Gerti slowly leans left at approximately 20 s and inspects the reflected body. The authors did not observe comparable movement sequences during ordinary interactions between two magpies.

Different birds varied in mirror preference and behavior. Social responses were transient in some individuals, whereas others avoided the mirror. Contingency testing identifies a response to matched visual movement; it remains behaviorally separate from directing a foot or beak toward an unseen mark on the body.''','Published examples of mark-directed and other body actions')
add('magpie',3,'Visible throat marks elicit magpie removal attempts','''The magpie mark test used a colored sticker on black throat plumage and a black control sticker. Both applications involved a sticker, but only the colored one created a conspicuous visual change. The throat location was unavailable to direct visual inspection.

Gerti and Goldie directed more behavior toward the mark region when a visible mark and mirror were jointly available. Removing the mark ended the mark-directed activity. Video S5 records Gerti attempting to reach with her beak and then removing the sticker with her foot.

The action was directed toward the bird's actual throat rather than toward the reflection. Comparing visible and black stickers with mirror and no-mirror conditions tested whether visual access to the mark changed body-directed behavior. The result was concentrated in particular individuals rather than uniformly present across the tested birds.''','Mark-directed behavior under visible and control sticker conditions')
add('jackdaw',2,'Jackdaw stickers can trigger touching without a mirror','''Jackdaws were tested with colored and black throat stickers, using mirror and cardboard conditions. The sticker altered feather contact as well as appearance. **Tactile confounding** occurs when a nonvisual sensation can explain the action attributed to seeing a mark.

Mark-directed attempts occurred even without the mirror, and birds attempted to reach control stickers as well as conspicuous ones. Video S8 records beak attempts toward a sticker. The movement itself is recognizable as mark-directed, but its sensory cause requires the control conditions.

Sticker contact can disturb the plumage of a small bird even when its color blends with surrounding feathers. A black sticker is therefore not automatically an effective nonvisual control. The jackdaw results caution against interpreting a removal attempt as mirror recognition solely because the animal is marked.''','Experimental stickers on the jackdaw throat')
add('corvid',2,'Corvid species differ in exploration and social response','''Common ravens, azure-winged magpies and carrion crows were compared using a common mirror-test procedure. A mirror, wood and silver foil separated a structured reflection from a nonreflective surface and from brightness without a clear body image.

The species differed in approach, exploration and social behavior during mirror exposure. Supplementary file 1 records social behaviors by azure-winged magpies and common ravens. Such interactions provide a behavioral category for comparison with subsequent contingency and self-directed movements.

The tested birds did not produce convincing mark-test success under this protocol. Exploration and social responses therefore varied despite a shared negative mark outcome. Standardized controls reduce the risk of treating differences in apparatus or handling across studies as differences in recognition capacity.''','Experimental mark positions in the compared corvids')
add('rooster',3,'Roosters call more for a live audience than a reflection','''Roosters give alarm calls to warn other birds about an aerial threat. Hillemacher and colleagues projected a moving predator shadow and compared a live visible companion, an empty compartment, a mirror and a companion hidden behind a mirror.

With up to 3 predator presentations per condition, mean alarm calls were 1.33 with a visible companion, 0.43 with the mirror and 0.29 when alone. The hidden-companion comparison tested whether hearing or other nonvisual social cues accounted for the response.

A reflection did not function like a visible social audience in this task. That distinction concerns the social meaning assigned to the reflected bird. Recognizing that a reflection is not an ordinary companion is different from using it to locate a novel mark on one's body.''','Published audience conditions and alarm-call outcomes')
add('rooster',2,'Roosters failed the conventional visible-mark test','''Roosters also received a conspicuous pink mark between the wattles below the beak. The **wattles** are the paired fleshy structures hanging beneath the beak. A sham application controlled the handling and application procedure without the same visible change.

Marked roosters did not selectively preen the marked region in the mirror condition. This negative outcome contrasts with their reduced alarm calling toward a reflection relative to a visible live companion. The same animal can distinguish social conditions without producing mark-directed body behavior.

The experiments measure different operations: an audience effect on vocal output and visual guidance of body-directed action. Treating either operation as the entire meaning of self-recognition would erase the dissociation between them. Both outcomes belong in the cross-species comparison.''','Rooster preparation and the marked body region')
add('horse',1,'Horses examine an open mirror more than a covered one','''Domestic horses entered an arena containing a **1.8 m wide mirror** and were tested with the surface covered or open. Attention, apparatus exploration and unusual repetitive movements were recorded separately. The covered condition retained the installation without a body reflection.

Mean selective attention lasted 420.0 s with the open mirror and 135.6 s with the covered mirror. Horses performed head movements and peek-a-boo behavior, moving outside and back into the reflected field. These actions changed access to the reflected body.

Some horses remained fearful or aggressive and were excluded from the subsequent reported comparison. The analyzed result therefore concerns animals that progressed beyond persistent social or avoidance responses. Familiarization history and selection criteria affect what the later group-level mark response represents.''','Arena geometry and mirror-access zones')
add('horse',1,'Visible cheek marks increase horse face scratching','''Horses received transparent sham marks and colored marks on their cheeks using matched application shapes. A horse cannot grasp its cheek with fingers, so the experiment scored face rubbing against a limb, the ground or environmental supports.

With the mirror available, mean face scratching lasted **6.21 s** with colored marks and **1.29 s** with transparent marks. Ordinary body scratching did not show the same increase. The response was associated with the marked region rather than a generalized elevation of scratching.

Supplementary file 10 records Shaif rubbing the marked face against a wooden pole. The control application and separation of face from body scratching support the visual-mark interpretation. Motor anatomy determines the measurable removal action and prevents an ape-like hand response from being a universal criterion.''','Experimental arena used for cheek-mark and sham comparisons')
add('fish2022',1,'Cleaner-wrasse marks resemble parasites','''Cleaner wrasses remove external parasites from other fish. Kohda and colleagues placed small colored marks beneath the wrasse's throat, where the focal animal could inspect them through a mirror but not directly. The response was throat scraping against the substrate.

Brown marks resembled the coloration of relevant parasites. The published figure compares the experimental marks with a real parasite, including a **1 mm scale bar**. Blue and green marks created visible changes without the same ecological resemblance.

The choice of mark is a biological manipulation of salience, meaning the likelihood that a stimulus attracts attention and action. A conspicuous unfamiliar color and a parasite-like body feature need not evoke the same motivation. Sensory visibility and behavioral significance are therefore separate requirements for a useful mark test.''','Experimental mark colors and a parasite with scale bar')
add('fish2022',2,'Fish throat scraping depends on a mark and mirror','''Cleaner wrasses scraped their throats when a brown mark was present and the mirror exposed. Sham marking and brown marking without visual mirror access did not elicit the same response. The comparison separated the physical treatment from seeing its reflected location.

Scraping directed the marked throat toward the tank substrate. The study measured scraping frequency during standardized observation windows and distinguished throat scraping from other body actions. Its interpretation depends on the location specificity of the response.

A mark applied beneath transparent tissue can supply bodily stimulation even when it is visually hidden. The mirror-absent and sham conditions therefore remain necessary alongside a positive scraping result. The conjunction of a salient mark, visual access and location-specific action defines the measured behavioral pattern.''','Throat-scraping comparisons across mark and mirror conditions')
add('fish2022',3,'Mark color changes the cleaner fish response','''The cleaner-wrasse study compared brown, blue and green throat marks. Brown marks elicited scraping in mirror-experienced fish, whereas the conspicuous alternative colors did not produce comparable mark-directed responses. The colors were an experimental variable rather than decoration.

The brown treatment linked an unseen body feature to an action normally useful for removing an irritant or parasite. Blue and green created a visual mismatch without the same apparent ecological meaning. A failure to scrape those colors therefore differs from a failure to detect any reflected body alteration.

The authors proposed that ecologically relevant marks facilitate expression of the capacity being tested. This proposal connects motivation to behavioral readout. It also explains why matching mark location alone is insufficient when comparing studies that use different colors, textures or naturally meaningful features.''','Responses to brown, blue and green marks')
add('fish2023',2,'Cleaner fish transfer mirror experience to photographs','''After passing a mirror mark test, cleaner wrasses were presented with photographs of themselves or unfamiliar fish. A photograph is **noncontingent**: its posture does not update with the focal animal's current movement. The experiment therefore removed moment-to-moment movement matching.

Before mirror experience, fish attacked self and unfamiliar photographs. Afterward, they showed much less aggression toward self photographs while continuing to attack unfamiliar individuals. Observations were scored over 5 min, using rushing, bumping and biting as aggressive categories.

The transfer extended beyond a currently moving reflection. The authors proposed a stored representation of self appearance acquired during mirror experience. Comparing photographs of different identities tested visual recognition after learning while leaving the representational mechanism as an explanation rather than a directly recorded neural process.''','Self, unfamiliar and composite photographic stimuli')
add('fish2023',3,'The face carries cleaner-fish identity information','''Composite photographs exchanged the face and body between self and unfamiliar cleaner wrasses. Fish with prior mirror recognition showed little aggression toward a self face on an unfamiliar body. They attacked an unfamiliar face even when it was attached to their own body.

The measured aggression frequency over **5 min** therefore followed face identity more strongly than body identity. The controls held photographic presentation constant while changing which visual region belonged to the focal fish. The procedure identifies the part of the appearance carrying the relevant information.

The authors also compared self and familiar-neighbor photographs to address a simple familiarity account. Self photographs continued to evoke less aggression under those comparisons. Face-based discrimination is an experimentally supported behavior; the form of an internal self-image remains a proposed explanation of it.''','Aggression toward self, unfamiliar and exchanged-face images')
add('fish2023',2,'A marked self photograph triggers throat scraping','''A cleaner wrasse with prior mirror-test experience viewed a self photograph bearing a brown throat mark. Its actual earlier body mark had faded, and the mirror was removed before recording. The new apparent mark existed on the photograph rather than on the fish's skin.

In Movie S1, the fish scraped its throat **10 times in 30 s** after inspecting the marked self photograph. It alternated viewing with scraping against a small sandy block. The authors described repeated bouts of 3, 4 and 3 scrapes within that interval.

Marked unfamiliar photographs and unmarked self photographs did not produce comparable responses in the experiment. Transfer to a static marked self-image connects appearance identity with body-directed action even when physical irritation from a new actual mark is absent.''','The photographic models used to test self-face identity')
add('octopus',1,'Octopus mirror responses include body-pattern displays','''Common octopuses were compared with a mirror, a nonreflective panel and a live conspecific. **Agonistic behavior** is behavior involved in threat, conflict or avoidance. Mirror trials elicited some agonistic responses, whereas a nonreflective panel did not evoke the same category.

The animals also contacted the surface and sometimes investigated behind it. A **passing-cloud display** is a moving pattern across the body surface. Supplementary Video S1 records this display in a mirror trial; the study also observed it in interactions with another octopus.

The occurrence of a body pattern in both mirror and social conditions prevents the display from serving as a uniquely self-directed criterion. Exploratory, social and body-pattern responses were scored separately from attempts to remove an experimental mark.''','Octopus contact, exploration and social responses')
add('octopus',3,'Octopus mark touching often occurs without a mirror','''The octopus mark test used visible and sham marks and compared mirror-present with control trials. Octopuses could investigate marked areas with their arms and suckers. This motor access permitted removal attempts while also making tactile cues especially relevant.

Of 42 recorded mark-directed events, **30 occurred in control trials without the mirror**. Sham-marked animals also groomed the treated region. Mark-directed touching was therefore not contingent on seeing a reflected mark under these conditions.

The social comparison recorded attacks, avoidance, grooming and body patterns in front of a mirror or a conspecific. Similar response categories across conditions describe how a reflection can be treated as a social stimulus. They do not rescue a mark criterion that is already satisfied in mirror-absent controls.''','Mirror and live-conspecific behavioral comparisons')
add('zebra',1,'Zebrafish mirror aggression varies across generations','''Zebrafish can respond to their reflection with repeated aggressive displays. Reichmann and colleagues measured time engaged in mirror aggression during a **5 min observation period**. The starting population ranged from no aggression to about 178 s of aggressive activity.

Selective breeding produced high- and low-mirror-aggression lines. Adult high-aggression fish remained more aggressive across successive generations, although the distributions overlapped. Juvenile differences were not identical in every generation, so the breeding result was not a perfectly discrete behavioral switch.

During a prolonged 1 h exposure, the high-aggression line also remained more aggressive without a corresponding difference in locomotor activity. The mirror provided a standardized social stimulus for quantifying aggression; attacking a reflection is not a mark-directed self-recognition response.''','Tracked activity and aggression across selectively bred generations')
add('zebra',4,'Aggression-related transcripts differ by sex and line','''**Transcriptomics** measures the RNA molecules expressed in tissue. The zebrafish study compared whole-brain RNA from high- and low-mirror-aggression lines, analyzing males and females separately. Gene-expression patterns were related to the inherited behavioral differences.

The differentially expressed genes and enriched biological functions varied with sex. Shared and sex-dependent patterns linked aggressive phenotype to molecular state rather than to one uniformly altered gene program. The published heat maps retain the source's original color-coded expression scale.

Expression differences are associations, not receptor manipulations or measurements of synaptic current. A whole-brain transcript can change because of cell composition, state or regulation within cells. The molecular comparison complements the 5 min behavioral assay without identifying a self-recognition mechanism or a single causal aggression pathway.''','Sex-dependent differential gene expression')
add('mouse',1,'Mouse grooming requires visual and tactile cues','''Black-furred mice received ink on the top of the head and were tested in 30 min sessions. **Visuotactile integration** means combining visual and touch-related information. White ink provided visual contrast, while mark size and amount altered the bodily stimulation associated with application.

A standard 0.2 cm² white mark did not produce the same mirror-dependent head grooming as larger ink loads. The experiment compared white ink without a mirror, white ink in darkness, black ink with a mirror and white ink with a visible mirror.

Head grooming increased with a sufficiently strong white mark and visible reflection. The color and visibility controls separated a general reaction to ink from a response involving the reflected body. Whisker, body and tail grooming were analyzed separately from the marked head region.''','Mark conditions, original grooming measurements and experimental preparation')
add('mouse',3,'Mirror habituation changes the mouse mark response','''**Habituation** is a reduction in response during repeated exposure to a stimulus. Mice initially explored and investigated the mirror, including its rear surface. Repeated access reduced this exploratory pattern while allowing experience with the reflected body.

After 4 days of mirror exposure, mice continued substantial rear-mirror investigation and did not express the same mark-related head grooming. After 7 days, rear investigation was lower and the positive grooming pattern emerged. The duration of prior mirror experience therefore changed performance.

The mark sessions remained comparisons of visible contrast, mirror access and bodily application. Habituation did not itself count as a successful mark response. Its effect was expressed in later visual guidance of head-directed grooming, linking prior exposure to the behavioral readout.''','Habituation time course and subsequent mark-directed grooming')
add('mouse',4,'Social experience supports mirror-directed grooming','''Yokose and colleagues varied the mice's social experience before mirror testing. Mice isolated after weaning continued investigating the back of the mirror and failed to express the usual mark-related head grooming. Isolation altered the acquisition conditions for mirror familiarity.

Black-furred mice raised with white-furred mice also showed persistent rear-mirror investigation and failed the grooming criterion. This manipulation changed the appearance of the social bodies encountered during development. It separated ordinary social exposure from exposure to a visually similar body type.

The authors proposed that prior visual experience with similar bodies contributes to recognizing reflected appearance. The mark controls remained necessary because social experience can affect exploration, anxiety and grooming as well as visual familiarity. The observed developmental effect connects early experience with later use of reflected body information.''','Isolation, cross-fostering and subsequent behavioral responses')
add('mouse',5,'Chemogenetic inhibition reduces vCA1 excitability','''The **hippocampus** contains anatomically distinct subfields, including CA1. Its ventral CA1 region, or vCA1, was targeted with a viral construct expressing hM4Di, an engineered inhibitory receptor. A red fluorescent reporter identified the cells carrying the construct.

hM4Di is a **Gi-coupled receptor**, meaning that receptor activation engages an inhibitory G-protein signaling pathway. The ligand clozapine-N-oxide was administered 30 min before testing. Recordings confirmed hyperpolarization, a shift to a more negative membrane voltage, and a greater current requirement for firing.

Reduced excitability links the receptor manipulation to neuronal output. The same intervention reduced mark-related grooming, while ordinary grooming without the mirror-mark condition remained intact. This connects verified inhibition of a defined hippocampal population to a specific behavioral comparison.''','vCA1 histology, voltage recordings and chemogenetic behavioral effects')
add('mouse',6,'CA1 inhibition affects mirror-related grooming selectively','''The study compared inhibition across hippocampal subfields. Inhibiting dorsal CA1 or ventral CA1 reduced the mirror-induced head-grooming response. Equivalent tests of dorsal CA2, dorsal CA3 and ventral CA3 did not produce the same suppression.

The anatomical labels distinguish different hippocampal populations rather than successive stages directly proven by the experiment. Fluorescent histology documented the injection sites. Vehicle-treated and inhibitory-receptor conditions allowed the effect of the receptor manipulation to be assessed against the same mark protocol.

Dorsal CA1 inhibition also reduced the activity-associated signal measured in ventral CA1. This physiological relationship is consistent with interaction along the hippocampal longitudinal axis. It supplies a functional link while leaving the exact synaptic route between the manipulated and measured populations unresolved.''','Injection-site histology and subfield-specific inhibition comparisons')
add('mouse',7,'Activity tagging identifies recurring mirror responses','''An **activity-tagged ensemble** is a population labeled because its neurons were active during a defined experience. The researchers used a regulated viral system to tag hippocampal neurons during mirror exposure, then measured reactivation during a later exposure.

In ventral CA1, mirror re-exposure recruited more overlap with the tagged population than the comparison conditions. The tag and subsequent activity marker were visualized with different fluorescent signals. Overlap measured the recurrence of activity in the same cells rather than the total activity of the whole region.

Some tagged cells were also reactivated by a stranger of the same black-furred strain, but less by a different white-furred strain. Their tuning therefore includes appearance shared with similar animals. Calling them exclusively self-identity neurons would omit the study's explicit same-strain response.''','Fluorescent activity tags and reactivation in vCA1 ensembles')
add('mouse',8,'Tagged-ensemble inhibition reduces grooming','''The authors combined activity tagging with the inhibitory receptor to target neurons recruited during mirror experience. Later inhibition of that tagged ventral CA1 ensemble reduced mirror-related head grooming. This manipulation narrowed the intervention beyond inhibiting the entire region.

Ensembles tagged during exposure to similar black-furred animals also contributed to the grooming response. Inhibition of populations tagged during exposure to white-furred animals or an open field did not produce the same effect. An **open field** is an arena used here as a different tagging experience.

The targeted comparison supports a causal contribution of experience-selected hippocampal cells to the behavioral response. Their shared recruitment by mirror and same-strain social experience connects visual similarity, acquired representation and body-directed action without making mark grooming a complete measure of subjective self-awareness.''','Tagged-cell histology and ensemble-specific inhibition effects')
assert len(slides)==44,len(slides)
title=fig('elephant',2,'Happy with a visible experimental mark')
title['path']='figures/title_elephant.png';title['caption']='Plotnik et al. (2006), Fig. 2A. Happy with an experimental head mark.'
take=[('Visual guidance','A positive mark response is directed toward the animal’s actual body and depends on seeing an otherwise unseen mark.'),('Sensory controls','Sham marks, mirror-absent conditions and matched handling separate visual guidance from tactile irritation and ordinary grooming.'),('Distinct operations','Social discrimination, contingency checking, body inspection and mark-directed action are different measured behaviors.'),('Experience matters','Mirror habituation, precise visual-proprioceptive training and developmental social experience can change performance.'),('Species-specific actions','Trunk touching, dolphin positioning, bird removal, horse rubbing and fish scraping reflect different motor access to body locations.'),('Neural evidence','Chimpanzee anatomy and macaque firing provide associations; verified inhibition of mouse CA1 and tagged ensembles supplies causal evidence for the grooming task.')]
keys=['elephant','dolphin','magpie','jackdaw','monkeytrain','mouse','chimptract','macaqueSII']
spec={'lecture':90,'theme':'steel-blue-porcelain','content_slides':44,'title_image':title,'title_refs':[R['elephant']['reference']],'slides':slides,'takeaways':{'items':[{'lead':a+'.','text':b}for a,b in take],'cite':'; '.join(R[k]['short']for k in ['elephant','monkeytrain','mouse']),'refs':[R[k]['reference']for k in keys],'transcript':[a+'. '+b for a,b in take]}}
(B/'lecture.json').write_text(json.dumps(spec,indent=2,ensure_ascii=False)+'\n')
(B/'PLAN.md').write_text('# Lecture 90\n\n'+ '\n'.join(f'{i+2}. {s["title"]}'for i,s in enumerate(slides))+'\n\nEmbed 10 original article clips on slides 12, 13, 14, 21, 22, 23, 24, 28, 34 and 35. Consecutive video slides are permitted; placement follows the relevant experiments.\n')
print('Written',len(slides),'content slides')
