from pathlib import Path
import json,re
root=Path(__file__).resolve().parent
R=json.loads((root/'references.json').read_text())
C={'G':'Greco et al. (2016)','F':'Boyle et al. (2015)','N':'Herculano-Houzel et al. (2014)','S':'Vilela et al. (2025)','T':'Bansiddhi et al. (2019)','W':'Finch et al. (2020)','R':'Pretorius et al. (2023)'}
F={}
for key,k,num,desc in [('g1','G','1','Daytime and nighttime activity budgets'),('g5','G','5','Individual daytime stereotypy rates'),('g6','G','6','Individual nighttime stereotypy rates'),('g7','G','7','Modeled association with separate housing'),('g8','G','8','Modeled association with juvenile contact'),('g9','G','9','Modeled association with managed activities'),('g10','G','10','Modeled association with transfers'),('g11','G','11','Modeled association with social experience'),('g12','G','12','Modeled association with indoor–outdoor choice'),('g13','G','13','Nighttime transfer association'),('f1','F','1','Published exhibit map and recording locations'),('f2','F','2(A–C)','Daytime activity before, during, and after renovation'),('f3','F','3(A–C)','Nighttime activity before and after renovation'),('f4','F','4(A–C)','Timing and duration of recumbent rest'),('f5','F','5(A–C)','Rest-event frequency and duration'),('f6','F','6','Serum cortisol profiles across renovation'),('n1','N','1(A–C)','Regional mass and cell-count scaling'),('n2','N','2(A–B)','Cortical folding and surface area comparisons'),('n3','N','3(A–D)','Anterior–posterior cortical cell distributions'),('n4','N','4','Original cortical sections and density map'),('n5','N','5','Cerebellar and cortical neuron-number comparison'),('s1','S','1(A–B)','Baseline and post-conflict self-directed behavior'),('s2','S','2(A–B)','Behavior-specific post-conflict comparisons'),('s3','S','3','Trunk orientation and self-directed behavior'),('s4','S','4(A–B)','Individual responses across social conditions'),('w2','W','2','Daytime feeding and historical comparison'),('w3','W','3','Individual stereotypy and historical comparison'),('w5','W','5','Proportion of rest spent lying'),('r1','R','1(a–c)','Captivity and post-release physiological and behavioral measures'),('r2','R','2(a–c)','Reintegration-phase physiology and behavior'),('r3','R','3(a–c)','Responses to environmental disturbance')]:
 F[key]={'path':'figures/'+key+'.png','kind':'article','caption':C[k].replace(' et al.','')+', Fig. '+num+'. '+desc+'.','source_url':R[k].split()[-1]}
P=json.loads((root/'photos.json').read_text());S=[]
def add(title,key,k,text,anatomy=False):
 body=text.strip().split('\n\n');refs=[R[k]];f=P['asian'] if key=='photo' else F[key]
 s={'title':title,'layout':'figure-right','body':body,'cite':C[k],'refs':refs,'transcript':[re.sub(r'\*\*|_', '',p) for p in body],'figure':f}
 if anatomy:
  s.pop('figure');s['layout']='figures-right';s['figures']=[f,F['n4']]
 S.append(s)
add('Stereotypy is defined by a repetitive behavioral pattern','g5','G','''A **stereotypy** is a repetitive, relatively invariant behavior without an evident immediate goal. Greco and colleagues recorded stereotypic activity in zoo-housed African elephants, _Loxodonta africana_, and Asian elephants, _Elephas maximus_, rather than classifying every repeated movement as abnormal.

Observers used a behavioral coding system and repeated daytime and nighttime observations. Performance was expressed relative to active observation time, allowing feeding, locomotion, and repetitive movements to be distinguished within each animal’s activity budget.

Stereotypy can indicate a welfare problem, but its presence is not a direct measurement of neuronal injury or a psychiatric diagnosis. Repeated walking toward food differs from invariant pacing without an apparent immediate goal; context and the operational definition determine which behavior enters the measure.''')
add('Active-time percentages differ from whole-day exposure','g1','G','''An **activity budget** partitions observed time among defined behaviors. Greco and colleagues distinguished active periods from rest before calculating the proportion of active observations allocated to feeding, locomotion, stereotypy, and other categories.

Elephants were active during approximately eighty percent of daytime observations and sixty percent of nighttime observations. Feeding and stereotypic behavior were prominent active categories in both periods, while locomotion and self-maintenance were more frequent during the day.

A percentage of active time must not be interpreted as the same percentage of all twenty-four hours. Excluding rest changes the denominator. Comparison across studies requires matching behavioral definitions, observation periods, and denominators before differences are attributed to environmental conditions or individual welfare.''')
add('Individuals differ substantially in daytime stereotypy','g5','G','''Greco and colleagues quantified the rate of stereotypic behavior separately for each observed elephant. Among animals performing stereotypy, daytime rates ranged from approximately one half of one percent to sixty-eight percent of active observation time.

The individual distribution includes low and high performers rather than one uniform zoo-elephant phenotype. Repeated observations and standardized coding allowed researchers to relate this variation to documented housing conditions, management practices, species, and life histories.

A group average conceals animals that rarely performed the behavior and animals for which it occupied much of active time. The measured heterogeneity supports individual monitoring; it does not identify whether a high-performing animal has a particular neural lesion, whether its current enclosure caused the behavior, or whether the behavior began before arrival.''')
add('Night observations detect substantial repetitive activity','g6','G','''Nighttime behavioral recording samples a period that routine visitor-hour observation can miss. Greco and colleagues measured stereotypy during active nighttime observations using the same broad behavioral categories employed during daytime recording.

Among stereotypy-performing animals, nighttime rates ranged from approximately one to seventy-four percent of active observation time, with a mean near twenty-five percent. Daytime and nighttime measurements were associated, but the night record provided additional information about the animal’s daily environment.

A nocturnal rate is not equivalent to a sleep measurement, and activity does not establish insomnia without appropriate physiological evidence. Night surveillance can identify repetitive activity during indoor confinement while remaining distinct from electroencephalography, which measures electrical brain activity and was not used in this study.''')
add('Separate housing is associated with more stereotypy','g7','G','''**Epidemiology** examines how measured outcomes vary with exposures across a population. Greco and colleagues combined behavioral observations with management records to examine separate housing while accounting for other recorded characteristics.

More daytime spent housed separately was associated with higher stereotypy risk. In the published model, each ten-percentage-point increase in separate housing corresponded to approximately a nine-percent increase in the risk measure, with other modeled exposures held constant.

Separate housing was not randomly assigned, and animals may have been separated because of health, compatibility, or management concerns. The association therefore supports scrutiny of social restriction without proving that isolation alone caused every repetitive behavior. Ethical decisions about separation must also consider aggression risk and the welfare of prospective social partners.''')
add('Juvenile contact is associated with lower daytime risk','g8','G','''Greco and colleagues measured the proportion of time adults spent with juvenile elephants. Greater juvenile contact was associated with lower modeled daytime stereotypy risk after consideration of the other recorded management and demographic variables.

A ten-percentage-point increase in juvenile contact corresponded to approximately a fifteen-percent reduction in the model’s risk measure. Juvenile exposure was recorded as a management variable; the study did not experimentally isolate play, caregiving, learning, or another particular interaction.

The result is consistent with benefits of socially varied environments, but it does not establish a universal prescription to introduce a calf to every group. Compatibility and the juvenile’s own welfare remain separate considerations. The behavioral association cannot be assigned to oxytocin release or a specific social circuit because neither was measured.''')
add('Managed activity has a conditional behavioral association','g9','G','''Managed activity included structured interactions within the recorded zoo-management system. Greco and colleagues related the proportion of time in these activities to stereotypy while also considering housing separation, juvenile exposure, transfer history, and species.

More managed activity was associated with lower daytime stereotypy risk. The published model linked an additional ten percentage points of managed time to an approximately twelve-percent reduction in its risk measure under the recorded conditions.

This category does not establish that every training method, work demand, or human interaction improves welfare. Duration and broad category are not measurements of voluntariness or experience. An observed association supports evaluation of the particular practices studied; it cannot justify coercive activity or replace assessment of physical health, social contact, and behavioral choice.''')
add('Transfer history is associated with repetitive behavior','g10','G','''A **transfer** moves an elephant between institutions and can coincide with changes in familiar partners, keepers, routines, and surroundings. Greco and colleagues used recorded lifetime transfer histories rather than inferring them from the animal’s current behavior.

More transfers were associated with greater daytime stereotypy risk; the model estimated approximately an eighteen-percent increase in its risk measure per additional transfer. A related association also appeared in the nighttime model, supporting consideration of life history in current welfare assessment.

The analysis does not isolate separation distress from transport, age, selection for transfer, or earlier environments. It also does not establish that every transfer worsens welfare: relocation can provide improved conditions. The evidence identifies a risk association that should inform prospective planning and monitoring, without diagnosing trauma from transfer count alone.''')
add('Social experience predicts nighttime behavior','g11','G','''Greco and colleagues constructed a **social experience** score from time spent with different numbers of conspecific companions. A conspecific is another member of the same species; the score therefore describes opportunities for elephant social contact rather than human interaction.

Higher nighttime social experience was associated with lower modeled stereotypy risk. Each additional unit of the score corresponded to approximately a twenty-five-percent reduction in the model’s risk measure, with the other retained exposures held constant.

A numerical exposure score cannot establish the quality of every relationship. Affiliation, aggression, kinship, and the ability to withdraw may differ among groups with similar scores. The finding supports attention to nighttime social conditions while leaving relationship quality and the mechanism linking contact to repetitive behavior unresolved.''')
add('Indoor–outdoor choice has a distinct nighttime association','g12','G','''**Choice** in this study meant access to indoor and outdoor areas rather than being assigned exclusively to one location. Greco and colleagues recorded the proportion of nighttime during which elephants could move between these environments.

Greater indoor–outdoor choice was associated with lower nighttime stereotypy risk. An additional ten percentage points of choice time corresponded to approximately a thirteen-percent reduction in the published model’s risk measure, after considering social experience and transfer history.

This is an association with an operational opportunity, not a direct measurement of perceived control. Climate, space, resources, and management may differ alongside access. The result supports evaluating available options as part of welfare assessment while avoiding the unsupported claim that access alone repairs a particular neural pathway or guarantees good welfare.''')
add('Day and night models retain different environmental terms','g13','G','''The daytime and nighttime analyses did not retain identical combinations of exposures. Daytime associations included separate housing, juvenile contact, and managed activity, while nighttime associations included social experience and indoor–outdoor choice.

Transfer history was associated with stereotypy in both periods. The nighttime model estimated approximately a twelve-percent increase in its risk measure per additional transfer, compared with the somewhat larger daytime estimate.

These models describe outcomes under different observed conditions rather than identifying two separate disease mechanisms. Housing schedules and opportunities for contact differ across the day. A management change should therefore be evaluated throughout the full daily cycle, with the understanding that correlated environmental variables and unmeasured history limit causal interpretation.''')
add('Population associations do not diagnose an individual','g5','G','''Greco and colleagues documented a broad range of individual stereotypy rates while estimating associations across the studied population. A population association identifies a tendency under measured conditions; it does not determine the cause of one elephant’s behavior.

Management decisions can use that evidence to identify exposures worth assessing, including separation and transfer history. Repeated observation of the same individual can determine whether a proposed change is followed by altered activity, social contact, or repetitive behavior.

**Neuroethics** concerns ethical questions involving nervous systems, behavior, and mental experience. The empirical finding supplies evidence about a potential harm; deciding what restrictions are justified also requires an explicit ethical judgment. A risk model cannot by itself establish a psychiatric diagnosis, a moral ranking of animals, or the acceptability of every captive environment.''')
add('Brain mass and neuron number are separate measurements','n1','N','''Herculano-Houzel and colleagues measured the cellular composition of an African elephant brain. A **neuron** is a specialized cell that receives and transmits neural signals; total brain mass includes neurons, other cells, fibers, and extracellular components.

The sampled brain weighed approximately 4.6 kilograms and contained about 257 billion neurons. The investigators compared regional cell counts with previously measured mammalian species, rather than equating a larger mass directly with a larger cerebral-cortex neuron population.

The preparation was anatomical tissue, not a comparison of captive and wild elephants before and after an intervention. Its counts establish structural composition under the study’s methods. They do not measure the animal’s subjective experience, determine cognitive ability from mass alone, or establish that captivity altered its neuronal population.''',anatomy=True)
add('Cerebellar neurons dominate the sampled elephant brain','n5','N','''The **cerebellum** is a major brain division involved in coordinating neural processing, including sensorimotor functions. Herculano-Houzel and colleagues found approximately 251 billion neurons in the sampled elephant cerebellum, accounting for about ninety-eight percent of total brain neurons.

The cerebellar-to-cortical neuron ratio was approximately an order of magnitude greater than the relationship reported across the comparison mammals. This unusual regional distribution distinguishes total neuron number from the number located in cerebral cortex.

The authors proposed a possible relationship with elephant sensorimotor specialization, but did not record activity during trunk behavior or manipulate cerebellar circuits. The proposal remains separate from the measured cell counts. Neither a high cerebellar count nor the comparative ratio establishes a neural explanation for stereotypy or captivity-related distress.''',anatomy=True)
add('Cortical folding does not directly count neurons','n2','N','''The **cerebral cortex** is the folded outer gray-matter sheet of the cerebral hemispheres. Herculano-Houzel and colleagues measured cortical surface area, folding, and cellular composition, permitting these anatomical quantities to be compared independently.

The sampled cortex had approximately 5.6 billion neurons despite a cortical mass exceeding that of the human comparison. Its folding index was approximately 4.2, and neurons were distributed over a comparatively large cortical surface.

More folding therefore did not imply more cortical neurons than the human reference. This comparison does not rank the moral significance of species or measure an elephant’s social experience. Structural organization can constrain a biological account, while claims about captivity-induced cortical change require an exposure comparison that this study did not provide.''',anatomy=True)
add('Cortical tissue contains regional density differences','n3','N','''**Neuronal density** is the number of neurons within a specified amount of tissue. Herculano-Houzel and colleagues sampled cortical sections along the anterior–posterior axis, from the front toward the back of the hemisphere.

Anterior cortical sections had lower neuronal densities than much of the remaining cortex. The number of neurons beneath a unit of cortical surface also varied, so a uniform density assumption would not adequately describe the entire sampled hemisphere.

The investigators measured tissue composition rather than electrical activity or behavior during captivity. A regional difference can reflect normal anatomical organization; it is not evidence of a lesion. Assigning the distribution to stress, deprivation, or a particular behavioral pathology would require additional histological and exposure-controlled evidence.''',anatomy=True)
add('Density maps preserve anatomical measurement boundaries','n4','N','''Herculano-Houzel and colleagues reconstructed cortical sections and mapped their measured neuronal densities. The original sections provide anatomical context for the cell-count results, while the displayed density scale reports the quantity measured in the study.

An **isotropic fractionator** estimates cell numbers after tissue is dissociated into a suspension of nuclei. Neuron-associated labeling distinguishes neuronal nuclei from the total nuclear population; repeated sampling is used to estimate the proportion identified as neuronal.

Dissociation supports quantitative counting but removes the intact connections among the original cells. Consequently, this preparation cannot establish synaptic strength, transmitter release, receptor function, or which neurons were active during repetitive behavior. The anatomical map and counting method should not be mistaken for a functional scan of the elephant’s mental state.''')
add('Anatomical counts cannot establish captivity-induced injury','n1','N','''The elephant cell-count study provides regional anatomy and comparisons with other mammals. It does not include a matched captive-versus-wild exposure experiment or a longitudinal neural measurement before and after changes in housing.

A claim of **captivity-induced neural injury** requires evidence that an exposure changed neural tissue or function, with alternatives such as age, disease, and individual history addressed. Differences among species in cortical and cerebellar neuron counts answer a different question.

The lack of such an experiment does not establish that captivity has no neural effects. It limits the mechanism that can be asserted from these particular data. Ethical concern can be supported by behavioral or physiological evidence without presenting unmeasured neuron loss, receptor changes, or a human psychiatric diagnosis as an established elephant finding.''',anatomy=True)
add('Self-directed behavior increases after social conflict','s1','S','''**Self-directed behaviors** are actions directed toward the animal’s own body, including mouth touching and head shaking. Vilela and colleagues compared these behaviors in captive Asian elephants during baseline observation and after recipients experienced aggression.

Focal recording continued for ten minutes after a conflict. Expected counts of self-directed behaviors were approximately forty percent greater in the post-conflict context than in the corresponding baseline, with the comparison matched to the relevant social condition.

The result supports a context-sensitive behavioral indicator of social stress. It does not mean that every dust bath or head shake expresses anxiety; the inference comes from the change following a recorded event. No receptor assay or brain recording was used to identify the neural mechanism underlying that change.''')
add('Different self-directed actions have different responses','s2','S','''Vilela and colleagues distinguished brief self-directed events from behaviors measured as durations. Events were counted relative to observation time, whereas sustained postures were expressed as the proportion of time occupied by the behavior.

Mouth touching, head shaking, and dust bathing showed prominent post-conflict changes among the recorded events. Holding the trunk curled inward also changed after aggression, while several other scored actions did not display the same response.

Pooling all movements without these definitions would conceal differences among actions and measurement scales. The findings concern changes within the observed social context, not a diagnostic checklist that can classify every elephant from one gesture. Environmental conditions and the individual baseline remain necessary for interpreting the recorded behavior.''')
add('Trunk orientation can compete with self-directed activity','s3','S','''After aggression, Vilela and colleagues also measured how long the victim oriented its trunk toward the aggressor. This measure described attention to the other animal’s location without assuming that trunk orientation revealed a particular thought or intention.

Higher rates of self-directed events were associated with a lower proportion of time directing the trunk toward the aggressor. The relationship was recorded during post-conflict observation rather than established by experimentally changing one behavior.

The actions can reflect different responses to the same event or compete for available time. The association does not prove that self-directed behavior reduces vigilance or relieves distress. It also does not establish a specific attentional circuit, because neuronal activity and transmitter-dependent signaling were not measured in these elephants.''')
add('Social stress indicators do not equal stereotypy','s4','S','''Vilela and colleagues followed changes in social composition and aggression across different observation conditions. Baseline self-directed behavior varied among individuals, and the animal not observed receiving aggression had particularly low self-directed levels.

The measured relationship between baseline self-directed behavior and stereotypy was not a consistent correlation across the observed conditions. Stereotypy and post-conflict self-directed events therefore could not be treated as interchangeable measurements of the same behavioral state.

An acute response to aggression differs from a persistent repetitive pattern. Monitoring both can provide complementary information, while neither establishes an elephant diagnosis of post-traumatic stress disorder. That human clinical category cannot be inferred from repetitive movement or an aggression history without an independently validated species-appropriate diagnostic framework.''')
add('Fecal metabolites reflect delayed adrenal output','photo','T','''**Glucocorticoids** are adrenal hormones associated with metabolic regulation and responses to challenge. Bansiddhi and colleagues measured fecal glucocorticoid metabolites in Asian tourist-camp elephants, providing a noninvasive measure after circulating hormones had been metabolized and excreted.

The overall reported mean was approximately fifty-three nanograms per gram of fecal material. This concentration differs in units and biological time course from serum cortisol measured in nanograms per milliliter of blood.

Excretion creates a delay between an event and the sampled fecal signal. A single concentration cannot identify the animal’s instantaneous mental state or the particular neural input responsible for secretion. The study therefore evaluated management, health, and behavior alongside hormone measurements rather than treating the hormone alone as a welfare diagnosis.''')
add('Adrenal activity and stereotypy need not move together','photo','T','''Bansiddhi and colleagues scored stereotypic behavior alongside fecal glucocorticoid metabolites in tourist-camp elephants. Animals without recorded stereotypy had higher adjusted metabolite concentrations than animals that performed stereotypy under the studied conditions.

This direction differs from a simple expectation that more repetitive behavior must accompany higher hormone output. The authors discussed a coping explanation, in which performing repetitive activity might relate to altered arousal, but did not experimentally test whether the activity reduced distress.

The observation establishes a dissociation between two proposed welfare indicators. It does not prove that stereotypy is beneficial or that low glucocorticoid concentrations guarantee good welfare. Neural mechanisms involving particular neurotransmitters, receptors, or feedback circuits remain proposed explanations rather than direct elephant measurements in this study.''')
add('Physical health changes the interpretation of hormone data','photo','T','''Bansiddhi and colleagues assessed body condition, foot health, and wounds alongside fecal hormone metabolites. **Body condition** is a structured estimate of an animal’s tissue reserves, while foot and wound scores describe visible physical health features.

Most recorded elephants had relatively high body-condition scores, and wounds of several documented origins occurred. Animals with wounds attributed to multiple causes had the highest reported metabolite concentrations among the wound-origin comparisons, approximately seventy-four nanograms per gram.

Hormone differences can therefore accompany physical condition and injury rather than a single social exposure. An association does not isolate pain intensity or establish a neural lesion, but it requires health assessment when interpreting the endocrine measure. Low behavioral activity should likewise not be assumed to reflect calmness without considering mobility limitations.''')
add('A management category is not a complete welfare measure','photo','T','''The tourist-camp analysis considered work type, duration of activity, walking, rest, and health rather than relying on one tourism label. Different camps combined these practices in different ways, creating correlated exposures within the observational data.

The authors concluded that behavioral and physiological measures can provide different information and should be assessed together. Walking opportunity, physical condition, and wounds supply additional context for a glucocorticoid result or the absence of observed stereotypy.

A broad label such as riding or non-riding does not establish the conditions experienced throughout an elephant’s day. Ethical evaluation requires the actual restrictions, health risks, social conditions, and opportunities to withdraw to be specified. These value judgments should be distinguished from a claim that the study measured a particular conscious experience or neural injury.''')
add('Flooring renovation provides a within-animal comparison','f1','F','''Boyle and colleagues studied female African elephants before, during, and after replacement of indoor flooring with a rubberized surface. The preparation combined daytime outdoor observations, nighttime indoor recordings, and repeated serum cortisol sampling.

The original exhibit map identifies the renovated area and the locations used for behavioral recording. Comparing each elephant with its own prior observations reduces some effects of stable individual differences, such as long-standing behavioral tendencies.

The renovation also included a construction period and temporary changes in indoor access. It was not a randomized flooring experiment with an unchanged parallel control group. Observed changes can therefore inform management evaluation while remaining potentially influenced by season, pregnancy, disruption, and other conditions that varied over the study.''')
add('Daytime walking increases after indoor renovation','f2','F','''Boyle and colleagues used repeated scan sampling to construct daytime outdoor activity budgets. **Scan sampling** records the behavior occurring at scheduled observation points rather than continuously counting every movement throughout the day.

After renovation, all studied females spent more daytime observations walking and fewer eating. Outdoor recording occurred approximately between nine in the morning and four in the afternoon, while the flooring itself had been changed inside the elephant house.

The daytime response extends beyond direct contact with the new surface, but it does not isolate a sensory or neural cause. Construction history, routine, and the opportunity to use different spaces can influence activity. Less daytime eating also should not be interpreted as a nutritional improvement without information about intake and body condition.''')
add('Nighttime rest differs among individual elephants','f3','F','''Night recordings in the flooring study sampled indoor behavior from the evening until morning husbandry. Lying rest and standing rest were scored separately, allowing rest posture to be distinguished from total inactivity.

The oldest elephant showed the least lying rest before renovation, occupying approximately thirteen percent of nightly scans, compared with roughly thirty-five and fifty-seven percent in the younger females. These percentages describe sampled behavior, not electrical sleep stages.

Age, health, and individual history can contribute to posture differences. A low lying-rest percentage cannot identify one cause without further assessment, and standing rest is not equivalent to an absence of sleep. The comparison supports individual evaluation rather than a universal nighttime posture threshold applied regardless of physical condition.''')
add('Recumbent rest has a measurable temporal pattern','f4','F','''**Recumbent rest** means resting while lying down. Boyle and colleagues recorded the timing and duration of these episodes during the thirteen nights before and thirteen nights after the flooring change.

The episode record preserves differences among individuals and shows when lying occurred across the night. An activity-budget percentage alone would not distinguish a few long episodes from many brief episodes producing a similar total.

Event structure can inform assessment of comfortable rest opportunities, but an observed lying episode does not establish a particular sleep stage. The study did not use brain electrical recordings to separate rapid-eye-movement sleep from other states. Claims about restored sleep circuitry would therefore exceed the behavioral and endocrine measurements actually collected.''')
add('Flooring responses are not uniform across the group','f5','F','''Boyle and colleagues compared the frequency of lying-rest events, their duration, and the interval spanning the first and last episode of the night. Those outcomes address different aspects of nighttime behavior.

Following renovation, one female increased lying rest, while another increased standing rest. Responses therefore were not identical even though the animals experienced the same broad flooring intervention and were observed with the same measurement framework.

An intervention can change behavior for some individuals without producing a universal group response. That heterogeneity should not be dismissed as proof that the surface has no effect, nor converted into a claim that every animal benefited equally. Repeated individual measurements are needed to evaluate the actual outcome and competing explanations.''')
add('Serum cortisol is reported in blood concentration units','f6','F','''**Cortisol** is a glucocorticoid measured here in serum, the fluid remaining after blood clotting. Boyle and colleagues collected blood repeatedly and used an enzyme immunoassay to quantify cortisol across the flooring-renovation period.

Baseline concentrations for the studied females were approximately three, four and a half, and five nanograms per milliliter. Two females remained near baseline across the intervention, while the pregnant female had elevated concentrations during construction and afterward.

The hormonal response therefore did not match a uniform stress reaction in every animal. Pregnancy and the construction disruption complicate a flooring-specific interpretation. Serum concentration is a physiological measure at collection, not a direct neural recording or an independent determination of whether the elephant experienced the renovation positively or negatively.''')
add('Unchanged cortisol does not erase a behavioral response','f3','F','''In the flooring study, changes in activity and rest occurred alongside cortisol concentrations that remained near baseline in two females. Behavioral and endocrine outcomes therefore provided overlapping but nonidentical information about the intervention.

A surface change might alter comfort, posture, or activity without producing a large sustained change in the sampled blood hormone. Conversely, altered cortisol during pregnancy or disruption need not be caused only by contact with the new floor.

The data do not identify a specific nociceptive pathway or establish that pain was reduced. **Nociception** is neural processing of potentially damaging stimuli, which requires evidence distinct from a rest-posture change. Practical assessment can combine behavior and health records while retaining this distinction between a plausible mechanism and a measured outcome.''')
add('Construction and the final environment differ','f6','F','''The flooring intervention included a transient renovation phase and a later period of access to the new surface. Boyle and colleagues separated these phases when describing hormone profiles and changes in behavior.

During construction the animals did not have normal indoor access, and one female’s cortisol increased. Later behavioral changes occurred after the renovated space became available, so an immediate construction response and a sustained housing response should not be conflated.

The study supports measuring both implementation costs and later outcomes of a proposed welfare improvement. It does not establish a fully controlled causal estimate for the floor material. Ethical decisions about renovation should consider disruption and individual vulnerability while using the observed post-intervention behavior to evaluate the result.''')
add('Foraging time can expand under altered husbandry','w2','W','''Finch and colleagues assessed Asian elephants at ZSL Whipsnade Zoo using repeated behavioral observations and nighttime recordings. Hay nets, dispersed browse, and grass paddocks provided opportunities to obtain food across the enclosure rather than at a single feeding point.

The adult male spent approximately eighty-one percent of daytime feeding, and adult females approximately seventy percent. These values exceeded the historical forty-five-percent comparison cited in the study, although that reference was not a simultaneously observed control group.

Longer feeding time can reflect extended foraging opportunity, but duration alone does not establish appropriate energy intake or freedom from hunger. The study’s historical comparison combines different observation periods and husbandry conditions; it cannot isolate one enrichment device as the cause of the difference.''')
add('Improved conditions can accompany low stereotypy','w3','W','''The Whipsnade study recorded relatively low stereotypy compared with the cited historical population. Several individuals were not observed performing stereotypic behavior, and pacing accounted for approximately seventy-seven percent of the stereotypy that was recorded.

Observation across daytime and nighttime periods supplied more information than visitor-hour recording alone. Individual results were retained rather than assuming every member of the group responded alike to the institution’s housing and management conditions.

The comparison supports the possibility of improved behavioral outcomes within human care, but does not establish that every aspect of welfare was optimal. Historical differences, selection, life history, and measurement limits remain relevant. Absence of observed stereotypy is not proof of unrestricted agency or an absence of negative experience.''')
add('Rest posture complements other behavioral measures','w5','W','''Finch and colleagues quantified the proportion of total resting time spent lying rather than standing. All observed subjects engaged in nightly lying rest, and each spent more than half of its recorded resting time recumbent.

The youngest individuals had the greatest lying-rest proportions. The facility provided deep sand and social groupings, but these features were not independently randomized, so their separate effects could not be estimated from the case study.

The denominator is resting time, not the entire night or a physiological measure of sleep duration. Rest posture, feeding, social association, and stereotypy describe different dimensions of the animal’s daily behavior. Their combination supports a more complete assessment while leaving direct claims about brain state or subjective satisfaction untested.''')
add('Reintegration is followed through multiple phases','r2','R','''Pretorius and colleagues followed African elephants transitioning from captivity into a free-ranging setting. They measured fecal glucocorticoid metabolites, temporal gland secretion, and defined behavioral responses across successive management and release phases.

A **temporal gland** is an elephant gland located beside the eye; the extent of visible secretion was scored as a physiological indicator. Measures were retained separately because hormone excretion, visible secretion, and immediate behavior have different biological time courses.

The release was a real management transition rather than a randomized laboratory manipulation. Group history, environment, and time changed together. The longitudinal record nevertheless permits the immediate release period to be distinguished from later adaptation, without assuming that a single post-release measurement represents the entire transition.''')
add('Stereotypy was not observed after release','r1','R','''Pretorius and colleagues recorded stereotypic behavior during the earlier captive phases but did not observe it after the elephants were released. Behavioral frequency was expressed as occurrences per minute of group observation.

The captivity-to-release comparison followed the same group, retaining information about its earlier experience. Elimination from the observed record indicates a substantial behavioral change under the new conditions, rather than requiring that repetitive patterns persist irreversibly.

Non-observation during the study is not proof that no episode ever occurred outside sampling. The result also does not establish repair of a particular brain lesion or reversal of every consequence of captivity. It provides direct behavioral evidence of change while the neural mechanism and broader individual welfare outcomes remain separate questions.''')
add('Release indicators do not change in a single direction','r1','R','''In the immediate captivity-versus-release comparison, visible temporal gland secretion increased after release, whereas fecal glucocorticoid metabolites did not show a clear difference between the compared periods. Observed stereotypy disappeared from the post-release record.

These outcomes are not contradictory measurements of one identical quantity. Visible secretion can change over a different timescale from excreted hormone metabolites, and a repetitive behavior can stop while an animal responds actively to a novel environment.

The findings prevent the claim that release must immediately lower every proposed stress measure. They also prevent treating increased secretion as proof that captivity was preferable. A transition can remove restrictions while imposing short-term challenges; the empirical assessment must specify which outcome and interval are being evaluated.''')
add('Longer follow-up changes the endocrine interpretation','r2','R','''Pretorius and colleagues separated the first, second, and third years after release. Fecal glucocorticoid metabolite concentrations were higher during the first year than in the preceding phases, indicating that short post-release comparisons did not capture the full endocrine trajectory.

Later concentrations declined descriptively, but the corrected comparison did not establish a reliable first-versus-third-year difference. The published phase record should therefore not be summarized as a conclusively proven complete physiological recovery by year three.

A prolonged adjustment period is compatible with changing environmental and social demands, but the study does not isolate the cause of each phase difference. Long follow-up is necessary to distinguish a transient response from a lasting outcome, while preserving the uncertainty in individual and group comparisons.''')
add('Disturbances change secretion and behavior differently','r3','R','''The reintegration study distinguished extreme infrequent disturbances from common immediate disturbances. This classification separated unusual events from the routine presence of environmental stimuli that elephants could encounter repeatedly.

Temporal gland secretion was greater on days with extreme disturbance events, but the frequency of the scored disturbance-related behaviors did not show the same clear difference. For common immediate disturbances, some group behavioral frequencies were lower when the disturbances were present.

A physiological indicator and a behavioral category therefore need not register every event identically. The observations cannot establish a single stress threshold that applies to all stimuli and elephants. Interpretation depends on event type, familiarity, behavioral opportunity, observation scale, and the interval between an event and the collected measure.''')
add('Behavioral improvement does not prove neural repair','r1','R','''The reintegration study supplies direct evidence that observed stereotypy can disappear following a transition to free-ranging conditions. It does not include neural imaging, receptor binding, electrophysiology, or histological comparisons before and after release.

A **mechanistic explanation** identifies the biological processes connecting an exposure to an outcome. Candidate explanations for behavioral change can involve altered opportunities, social experience, or arousal, but none of those possibilities establishes a measured change in a particular elephant circuit.

The appropriate inference is behavioral plasticity under changed conditions, with the causal contribution of individual environmental features unresolved. Ethical concern about the original repetitive behavior does not require inventing a neural lesion. Conversely, behavioral improvement alone cannot establish that every prior physical or psychological harm has been reversed.''')
add('Ethical judgments require values and evidence','r1','R','''The disappearance of observed stereotypy after release is an empirical outcome, while deciding whether an earlier restriction was justified is a normative judgment. **Normative** claims specify what ought to be done, rather than only describing what was measured.

Pretorius and colleagues also documented short-term physiological challenges during the transition, so assessment must distinguish immediate adjustment from later behavioral outcomes. A policy that considers only one indicator or one time point can omit relevant consequences for the individual.

Evidence about health, social opportunity, choice, and behavior can inform duties to prevent harm and evaluate alternatives. It cannot alone assign a numerical moral value to neuronal count or identify an elephant’s subjective experience. Neuroethical reasoning should state its values explicitly and preserve the limits of the biological evidence on which it relies.''')
# Source-colored animal context complements the original grayscale evidence.
for i in [0,5,7,9,20]:
 slide=S[i];f=slide.pop('figure');slide['layout']='figures-right';slide['figures']=[f,P['asian'] if i==20 else P['african']]
# Immediate and longer-term release comparisons use different measures.
for i in [37,40]:
 slide=S[i];f=slide.pop('figure');slide['layout']='figures-right';slide['figures']=[f,F['r1']]
assert len(S)==44,len(S)
items=[('Stereotypy:','Repetitive behavior is a contextual welfare indicator, not a diagnosis of neural injury or human psychiatric disease.'),('Social conditions and choice:','Separation, social experience, transfers, and indoor–outdoor access have observational associations with stereotypy.'),('Complementary indicators:','Glucocorticoids, self-directed behavior, repetitive activity, health, and rest measure different processes.'),('Individual outcomes:','Flooring and husbandry responses vary among elephants; evaluate behavior and physiology over time.'),('Neural evidence:','Anatomical cell counts establish brain composition, not captivity-induced neuronal damage or subjective experience.'),('Neuroethical inference:','Behavioral improvement after release can coexist with adjustment stress; ethical conclusions require explicit values and careful causal claims.')]
spec={'lecture':52,'theme':'iron-blue-paper','content_slides':44,'title_image':P['african'],'title_refs':[R['G']],'title_height':3.3,'slides':S,'takeaways':{'items':[{'lead':a,'text':b} for a,b in items],'cite':'Greco et al. (2016); Herculano-Houzel et al. (2014); Vilela et al. (2025); Pretorius et al. (2023)','refs':list(R.values())}}
(root/'lecture.json').write_text(json.dumps(spec,indent=2,ensure_ascii=False)+'\n');(root/'references.json').write_text(json.dumps(R,indent=2,ensure_ascii=False)+'\n')
