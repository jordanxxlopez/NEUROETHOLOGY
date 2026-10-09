from pathlib import Path
import json,re
R=Path(__file__).parent
refs={
'P':"Lehrman DS (1955). The physiological basis of parental feeding behavior in the ring dove (Streptopelia risoria). Behaviour 7:241–286. https://doi.org/10.1163/156853955X00094",
'A':"Martinez-Vargas MC, Erickson CJ (1973). Some social and hormonal determinants of nest-building behaviour in the ring dove (Streptopelia risoria). Behaviour 45:12–36. https://doi.org/10.1163/156853974X00570",
'C':"Cheng MF, Silver R (1975). Estrogen-progesterone regulation of nest-building and incubation behavior in ovariectomized ring doves (Streptopelia risoria). Journal of Comparative and Physiological Psychology 88:256–263. https://doi.org/10.1037/h0076181",
'F':"Cheng MF (1986). Female cooing promotes ovarian development in ring doves. Physiology & Behavior 37:371–374. https://doi.org/10.1016/0031-9384(86)90248-9",
'L':"Liley NR (1976). The role of estrogen and progesterone in the regulation of reproductive behaviour in female ring doves (Streptopelia risoria) under long vs. short photoperiods. Canadian Journal of Zoology 54:1409–1422. https://doi.org/10.1139/z76-164",
'N':"Nottebohm F (1981). A brain for all seasons: Cyclical anatomical changes in song control nuclei of the canary brain. Science 214:1368–1370. https://doi.org/10.1126/science.7313697",
'T':"Tramontin AD, Hartman VN, Brenowitz EA (2000). Breeding conditions induce rapid and sequential growth in adult avian song control circuits: A model of seasonal plasticity in the brain. Journal of Neuroscience 20:854–861. https://doi.org/10.1523/JNEUROSCI.20-02-00854.2000",
'Y':"Marlin BJ, Mitre M, D’amour JA, Chao MV, Froemke RC (2015). Oxytocin enables maternal behaviour by balancing cortical inhibition. Nature 520:499–504. https://doi.org/10.1038/nature14402",
'G':"Gillespie MJ, Haring VR, McColl KA, Monaghan P, Donald JA, Nicholas KR, Moore RJ, Crowley TM (2011). Histological and global gene expression analysis of the ‘lactating’ pigeon crop. BMC Genomics 12:452. https://doi.org/10.1186/1471-2164-12-452"}
cites={'P':'Lehrman (1955)','A':'Martinez-Vargas & Erickson (1973)','C':'Cheng & Silver (1975)','F':'Cheng (1986)','L':'Liley (1976)','N':'Nottebohm (1981)','T':'Tramontin et al. (2000)','Y':'Marlin et al. (2015)','G':'Gillespie et al. (2011)'}
fg={}
def f(key,ref,num,caption):
 fg[key]={'path':f'figures/{key}.png','kind':'article','caption':cites[ref]+f', Fig. {num}. '+caption,'source_url':refs[ref].split()[-1]}
for key,ref,num,cap in [
('g1','G','1(A–C)','Non-lactating and milk-producing pigeon crops; ruler in cm.'),
('g2','G','2(A–H)','Pigeon crop epithelium, vasculature and lipid staining.'),
('g2ab','G','2(A,B)','Pigeon crop epithelial proliferation and connective tissue.'),
('g2gh','G','2(G,H)','Lipid droplets in pigeon crop epithelial cells.'),
('a1','A','1','Breeding cages used for paired ring-dove observations.'),
('a3','A','3','Male nest attendance, wing-flipping and nest-cooing.'),
('a7','A','7','Bow-cooing frequency relative to the first egg.'),
('a8','A','8','Female nest-cooing relative to egg laying.'),
('a13','A','13','Nest soliciting after female hormone or oil treatment.'),
('a14','A','14','Reed and pine-needle transport on successive days.'),
('c1','C','1','Daily nest building by treated females and untreated males.'),
('c2','C','2','Daily incubation time in each female hormone condition.'),
('f1','F','1(a,b)','Female and male ring-dove nest-coo sonograms.'),
('l1','L','1','Female soliciting under an 8-hour photoperiod.'),
('l2','L','2','Female soliciting under a 16-hour photoperiod.'),
('l3','L','3','Nest-material accumulation under short days.'),
('l4','L','4','Nest-material accumulation under long days.'),
('t1','T','1','Published song pathways and steroid-receptor distribution.'),
('t2','T','2','White-crowned sparrow song; 2 kHz and 0.5 s bars.'),
('t3','T','3','Sequential growth of HVC, RA and Area X over 20 days.'),
('t4','T','4','Soma size, neuron density and neuron number in HVC and RA.'),
('y1','Y','1(a–e)','Mouse pup retrieval with oxytocin and maternal experience.'),
('y2','Y','2(a–h)','Oxytocin receptors in mouse auditory cortex.'),
('y2bc','Y','2(b,c)','Receptor staining and knockout control; bars 150 µm.'),
('y2de','Y','2(d,e)','Receptor-positive cortical cells and interneurons; bars 50 µm.'),
('y2gh','Y','2(g,h)','Left–right cortical receptor expression; bars 100 µm.'),
('y3','Y','3(a–d)','Cortical inactivation, oxytocin and receptor antagonists.'),
('y4','Y','4(a–e)','Pup-call responses and spike timing in auditory cortex.'),
('y5','Y','5(a–d)','Call-evoked excitation and inhibition in cortical neurons.'),
('y6','Y','6(a–f)','Oxytocin pairing and subsequent synaptic and spike plasticity.'),
('yED1','Y','Extended Data 1(a,b)','Oxytocin-neuron targeting in mouse PVN; bars 100 µm.')]:f(key,ref,num,cap)
DATA="""
Parental feeding depends on physiology and experience|g1|P,G
**Ring doves** are domesticated columbids in which both parents incubate eggs and feed their young. Lehrman described a clutch of two eggs, approximately 14 days of incubation, and parental regurgitation of crop contents into the squab, the newly hatched young bird.
The **crop** is a bilobed expansion of the esophagus. Its epithelial lining proliferates during incubation and supplies the cellular material called crop milk. Modern pigeon dissections distinguish a thin non-lactating wall from enlarged, milk-producing lateral lobes.
The anatomical comparison concerns pigeons, whereas Lehrman’s behavioral experiments concern ring doves. Milk-producing tissue supplies nourishment, but its presence alone does not establish that a parent will recognize or feed a squab.

Prolactin-induced feeding requires prior brood experience|g2ab|P,G
**Prolactin** is a pituitary hormone that promotes crop development in columbids. Lehrman administered a total of 450 international units over 7 days and then presented a squab, comparing hormonally treated birds with controls and distinguishing birds with different reproductive histories.
Previously experienced parents generally began feeding after prolactin treatment. Birds without prior brood experience failed to feed under the same artificial sequence, despite physiological responses to treatment. Prior experience therefore changed the behavioral consequence of a hormone.
Pigeon histology identifies proliferating crop epithelium, the peripheral tissue affected during milk production. The behavioral comparison does not identify a central prolactin receptor or establish that prolactin acts only outside the nervous system.

Crop sensation contributes to parental feeding|g2|P,G
Lehrman reduced sensation near the crop using 0.5 cubic centimeters of the local anesthetic Efocaine, administered 2 days before a squab was presented. A comparison group received anesthetic elsewhere, controlling for consequences of receiving the drug rather than its location.
Local treatment near the crop reduced parental feeding. **Peripheral feedback** means sensory information returning from the body to the nervous system; crop distension and contact with a squab were candidate sources of such information.
The crop tissue displayed here is from pigeons, not the anesthetized ring doves. The location-dependent behavioral effect supports a sensory contribution, but drug spread and other local effects prevent identifying one sensory receptor or excluding central hormone actions.

Partners perform complementary nest-building actions|a3|A
Ring-dove nest building involves a division of labor: males usually gather and transport material, while females remain at the nest site and **tuck** material into the developing nest. Martinez-Vargas and Erickson recorded these actions separately during the days before the first egg.
Established pairs received space, nest sites and alternative materials. Repeated observations related the male’s gathering to the female’s attendance and construction rather than treating total nest size as the only behavioral measurement.
Transport increased when females were established at the nest. Coordinated behavior can therefore arise through signals exchanged between partners; simultaneous increases in both birds’ activity do not by themselves establish simultaneous increases in a shared circulating hormone.

Courtship components change at different rates|a7|A
**Bow-cooing** is a male courtship vocalization accompanied by a bowing display. Martinez-Vargas and Erickson recorded its frequency across days aligned to the first egg, permitting comparison with nest-material transport and female nest attendance in the same reproductive period.
Bow-cooing declined as nesting progressed, while material gathering followed a different time course. Behavioral components therefore changed together within a breeding cycle without having identical trajectories or an interchangeable function.
Alignment to egg laying supplies a common reference event, not a manipulation of the underlying endocrine system. The records establish temporal relationships among observable actions but cannot determine whether a decline in vocalization directly causes the increase in construction.

Female nest-cooing is a changing social signal|f1|A,F
**Nest-cooing** is a vocal display given at the nest site. Females join males in this behavior and may continue alone after the male leaves to gather material. Daily observation distinguished female cooing from male bow-cooing and from physical nest construction.
Martinez-Vargas and Erickson distinguished nest attendance from active nest soliciting. Cheng described an abrupt cessation of female cooing after the second egg, linking the vocal phase to the transition toward incubation rather than to a constant readiness to reproduce.
A vocalization can influence a partner and provide sensory feedback to its producer. These observational records establish when cooing occurs; separate playback and hormone manipulations are needed to test its physiological and social consequences.

Female hormone treatment changes male gathering|a13|A
Martinez-Vargas and Erickson compared females treated with estrogen and progesterone with oil-treated females before pairing them with males. **Hormone replacement** supplies an experimental endocrine signal, while the oil comparison controls for injection and the vehicle carrying the hormones.
On the first pairing day, treated females performed more nest soliciting, including wing-flipping and nest-cooing. Their untreated male partners also participated differently in gathering material, and female nest attendance was closely associated with male transport.
Only the female received the experimental hormones. A change in male behavior therefore need not reflect direct drug action on the male; altered signals from his partner are a plausible route, although this experiment did not isolate every exchanged signal.

Sequential steroid treatment restores nest building|c1|C
Cheng and Silver used reproductively experienced females after **ovariectomy**, surgical removal of the ovaries, to reduce endogenous ovarian hormone contributions. They compared estradiol benzoate, progesterone, both steroids in a timed regimen, and sesame oil, with untreated males as partners.
Estradiol benzoate was administered on courtship days 4–10. Progesterone was added on days 8 and 10 in the combined condition, after estrogen exposure had begun. The administered doses were 50 micrograms of estradiol benzoate and 100 micrograms of progesterone.
The combined regimen produced the strongest nest-building response. Its timing supports a role for endocrine sequence, but the study did not compare every possible order and therefore cannot establish that this particular schedule is uniquely required.

Picking up material differs from completing a nest|c1|C
Cheng and Silver separated picking up and dropping nest material, carrying it to a site, and tucking it into the nest bowl. These measurements distinguish interaction with an available object from the coordinated construction required for a functional nest.
Females given the combined estrogen–progesterone regimen more reliably performed the later construction actions than females given either hormone alone or oil. Daily records also included untreated males, allowing each partner’s contribution to be distinguished.
At egg introduction on days 8 and 10, pairs lacking completed nests received an experimenter-built nest. Subsequent tucking can therefore include rearrangement of an existing nest; it should not automatically be interpreted as construction of an entirely new nest.

Estrogen and progesterone facilitate female incubation|c2|C
**Incubation** is sustained contact with eggs during their development. Cheng and Silver introduced infertile eggs under a controlled schedule and recorded the fraction of observation time spent sitting, comparing the four hormone conditions after ovariectomy.
Combined estrogen and progesterone most effectively restored incubation in females. Estrogen alone, progesterone alone and vehicle produced different, generally weaker early responses, despite access to the same breeding setting and experimental eggs.
Eggs and a nest were parts of the preparation. Hormone replacement altered responsiveness within this sensory and social context; the experiment does not establish an endocrine command that produces normal incubation independently of an appropriate nest, eggs or partner.

Untreated males respond to the female’s endocrine state|c2|C
In Cheng and Silver’s preparation, males were intact and received no experimental steroid treatment. Their mates differed in estrogen and progesterone replacement, enabling a test of whether manipulating one animal’s endocrine state changes another animal’s behavior.
Males paired with females receiving the combined regimen began incubating more readily early in the observation period. The difference concerned the timing and distribution of sitting; overall incubation duration across the full period was not clearly different among male groups.
A partner effect is therefore distinct from a direct pharmacological effect. Male responses may depend on female actions, competition or coordination at the nest, and changing availability of sitting opportunities. The experiment did not measure a specific male endocrine intermediary.

Hormones change readiness within a breeding context|c1,c2|C
**Estradiol** is an estrogenic steroid, and progesterone is another ovarian steroid involved in reproductive state. Their combined replacement restored nest building and incubation more effectively than either steroid alone in experienced ovariectomized ring doves.
The treatment operated in a preparation containing an untreated mate, nesting material, a nest and introduced eggs. Courtship, construction and sitting were measured separately because one hormone condition need not affect every component in the same way.
These systemic injections do not locate the relevant receptors in a particular brain nucleus or separate neural from peripheral actions. They establish a causal endocrine contribution to behavior under defined conditions, while leaving the cellular pathway and the complete normal hormone sequence unresolved.

Muting separates vocal output from social contact|f1|F
Cheng tested whether a female’s own vocal behavior contributes to reproductive development. A reversible peripheral muting procedure prevented normal sound production, permitting females to interact with courting males while experimental playback supplied controlled auditory input.
**Devocalization** means preventing vocal sound production; it does not mean removing the animal’s hearing. Sham-operated females controlled for the procedure, and muted females heard their own coos, male coos, another female’s coos, or no playback.
Pairs interacted for 2 hours daily over 5 days. Keeping male contact present reduced the possibility that poor development simply resulted from social isolation, although altered female output could still change details of the reciprocal interaction.

Self-produced calls provide endocrine feedback|f1|F
**Acoustic feedback** is hearing sound generated by one’s own behavior. Cheng recorded female nest-coos before muting and played those calls back during pairing, allowing auditory input to be restored without restoring normal vocal sound production.
The diameter of the same dominant ovarian follicle was measured before and after the playback period. A follicle is the developing egg and its surrounding tissue; the initial measured diameters were 4–5 millimeters across treatment conditions.
Own-call playback produced substantially more growth than male-call playback. This rescue supports an auditory contribution from the female’s own display, but does not identify the intervening neural circuit or prove that motor and bodily feedback make no contribution during natural cooing.

Own-call playback restores follicular growth|f1|F
Cheng reported a mean follicular diameter increase of 6.8 millimeters in muted females hearing their own coos. The corresponding increase was 2.1 millimeters with male coos and 1.7 millimeters without playback; sham females increased by 6.5 millimeters.
These are reported changes in diameter, rather than final follicular diameters or rates per day. Before and after measurements of the same dominant follicle connected the acoustic treatment to a physical reproductive response during the 5-day pairing procedure.
The own-call condition approached the sham response despite continued muting. Playback therefore supplied a physiologically effective component of the missing display, although the experiment did not measure the complete pituitary hormone sequence connecting sound to follicular growth.

Other female calls can also stimulate development|f1|F
Muted females hearing another female’s nest-coos showed a mean follicular diameter increase of 4.7 millimeters in Cheng’s experiment. Own-call playback produced 6.8 millimeters, whereas male-call playback produced only 2.1 millimeters under the same general pairing procedure.
The result prevents treating the effect as an all-or-none requirement for recognizing one’s unique voice. Female call characteristics can carry an effective stimulus even when the recording comes from a different individual.
The paper considered acoustic differences between female and male nest-coos, but did not isolate each acoustic feature with synthetic stimuli. The original sonograms document the supplied call classes; they do not establish the precise auditory feature or receptor responsible for the reproductive response.

Auditory rescue does not exclude bodily feedback|f1|F
Cheng distinguished hearing a nest-coo from **proprioceptive feedback**, sensory information associated with performing the movements of a vocal display. Playback to muted females restored an auditory stimulus while leaving normal sound production impaired.
The strong own-call response supports an acoustic route, but playback can also provoke attempted vocal movements and associated bodily signals. Consequently, auditory rescue is not equivalent to holding every motor and sensory consequence of calling constant.
The normal reproductive sequence can contain reciprocal links: courtship promotes female behavior, and that behavior supplies further stimulation to the female herself. The measured endpoint was follicular growth; the experiment did not directly record the neurons, synapses or hormone release events mediating each link.

Photoperiod changes responsiveness to progesterone|l1,l2|L
**Photoperiod** is the daily duration of light exposure. Liley housed intact female ring doves under 8-hour or 16-hour light periods, administered saline or steroid treatments for 15 days, and introduced reproductively active males after 7 days of treatment.
Females interacted with males for 4 hours daily across 9 observation days. Progesterone-treated females showed little soliciting under short days but increased activity rapidly under long days, despite receiving the same class of administered hormone.
Control females did not differ clearly in egg laying, courtship or nest building between these light schedules. The photoperiod effect therefore depended on treatment and behavioral context, rather than establishing a universal enhancement of all reproductive behavior whenever daylight is extended.

Long days facilitate hormone-dependent nest activity|l3,l4|L
Liley measured nest-material accumulation as well as female soliciting. Under 16-hour days, progesterone-treated pairs built more actively than the corresponding 8-hour condition; estrogen-containing treatments also supported substantial nest-oriented activity.
Nest material was counted across the 9-day period after male introduction. Because both partners contribute to construction, the accumulated material is a pair-level output, whereas duration of female soliciting identifies a particular animal’s behavior.
Long-day treatment modified responsiveness to the steroid conditions, but did not isolate a single light-sensitive neural pathway. The observed pair-level difference should not be interpreted as a direct measurement of one female motor circuit or as proof that a particular receptor changed abundance.

Steroid treatment does not recreate every reproductive act|l2|L
Liley’s estrogen and combined estrogen–progesterone treatments supported female soliciting and nest-building activity, with greater nest-oriented activity generally occurring under long days. Yet begging and sexual crouching associated with copulation remained infrequent in the hormone-treated birds.
Treatment lasted 15 days and was combined with daily access to an active male. Different reproductive actions were recorded separately, rather than inferred from a single global judgment that a bird was in breeding condition.
Hormonal facilitation is therefore behavior-specific. A treatment can promote nest-directed activity without restoring the complete sequence of mating and egg laying. These findings concern intact females and should not be assumed to match the replacement requirements of ovariectomized females exactly.

Canary song nuclei differ between spring and autumn|t1|N,T
**HVC** is a proper name for a song-control nucleus; a nucleus is an anatomically defined collection of neurons. **RA**, the robust nucleus of the arcopallium, receives motor-pathway input from HVC and projects toward the brainstem circuitry controlling vocal production.
Nottebohm compared adult male canaries in spring and autumn. HVC was approximately 99 percent larger in spring, and RA was roughly three-quarters larger, establishing substantial seasonal differences in adult brain anatomy.
The pathway drawing is the original published sparrow anatomy from Tramontin and colleagues, not a canary reconstruction. Nottebohm’s seasonal groups were different animals examined after death; the comparison supports seasonal plasticity but is not repeated imaging of one animal’s annual cycle.

Seasonal androgens covary with song-system anatomy|t1|N,T
**Androgens** are steroid hormones that include testosterone and influence reproductive physiology. Nottebohm reported spring serum androgen concentrations of 1.65 nanograms per milliliter, compared with 0.13 nanograms per milliliter in the autumn canaries.
The larger spring HVC and RA coincided with the higher circulating hormone concentrations. Comparisons normalized to a reference brain region also retained substantial seasonal differences, reducing the likelihood that uniform enlargement of the entire brain explains the result.
Season and hormone level were not independently assigned in this comparison. Their association cannot alone establish that testosterone caused the anatomical change, and a larger nucleus cannot reveal whether neurons were added, cells enlarged or connections remodeled without additional cellular measurements.

Seasonal volume changes require cellular explanation|t1,t4|N,T
**Neural plasticity** is a change in nervous-system structure or function with state or experience. Nottebohm’s canary measurements established seasonal variation in song-nucleus volume, but volume combines contributions from neurons, their processes and other tissue components.
A seasonal increase therefore cannot automatically be called neuron birth or stronger synaptic transmission. Histological measurements must distinguish cell size, cell density and cell number, while recordings or behavioral assays address consequences for vocal output.
Tramontin and colleagues later measured these attributes in white-crowned sparrows exposed to controlled breeding-like conditions. Their cellular results provide an experimental comparison across species; they do not retrospectively identify every process responsible for the original canary differences.

Breeding-like conditions recruit adult song circuitry|t1|T
Tramontin and colleagues housed adult male Gambel’s white-crowned sparrows under 8-hour days for 12 weeks, allowing the song system to reach a nonbreeding-like condition. They then increased the light period to 20 hours and supplied testosterone through implants.
Implants were placed on day 2 and were designed to produce concentrations within the physiological breeding range of approximately 4–10 nanograms per milliliter. Tissue was examined at baseline and after 7 or 20 days, with morphometry performed without knowledge of treatment group.
The intervention combined daylight and testosterone, so it tested their joint breeding-like effect. It did not separate the independent contributions of these cues or imply that wild birds normally experience the laboratory’s particular 20-hour light schedule.

Published pathways identify distinct song-system targets|t1|T
HVC sends output to RA in the descending vocal motor pathway and to **Area X**, a basal-ganglia component of the anterior forebrain song circuit. RA projects toward **nXIIts**, the tracheosyringeal hypoglossal motor nucleus supplying the vocal organ.
The anterior pathway includes the medial dorsolateral thalamic nucleus and the lateral magnocellular nucleus of the anterior nidopallium, or **LMAN**. The paper uses older anatomical names in its original drawing; the connectivity, rather than those historical regional labels, defines the circuit comparison.
Published receptor symbols distinguish androgen- and estrogen-sensitive locations. Receptor distribution supplies candidate sites for steroid action, but is not itself a functional test of which projection or cell population causes seasonal growth.

HVC reaches breeding size before its targets|t3,t1|T
Tramontin and colleagues measured the volume of HVC, RA and Area X after the combined long-day and testosterone intervention. HVC reached approximately 94 percent of its eventual breeding-like size within 7 days, whereas its targets grew more slowly.
RA and Area X did not reach their larger condition until the 20-day measurement. Because the nuclei were measured within a defined time course, the result establishes an order of anatomical response rather than simply a difference between two seasons.
Early HVC growth is consistent with influences transmitted to downstream targets, but temporal precedence alone is not evidence that HVC caused their growth. Direct manipulation of HVC or its projections would be needed to establish such a transsynaptic mechanism.

HVC growth includes an increase in neuron number|t4,t1|T
The sparrow study estimated **neuron number**, the total neuronal population within a nucleus, separately from **neuron density**, the population per unit tissue volume. These quantities distinguish growth caused by more neurons from expansion around an unchanged population.
Within 7 days of long-day and testosterone exposure, HVC gained approximately 50,000 neurons. Its density remained relatively stable while its volume increased, making a change in total neuronal population a substantial component of the structural response.
An increased population does not by itself identify the source or birth date of every added cell. The study counted neurons in terminal tissue samples; it did not track individual cells longitudinally or label their complete developmental histories.

Soma enlargement begins before all nuclei expand|t4,t1|T
A neuronal **soma** is the cell body, distinguished from axons and dendrites. Tramontin and colleagues measured cross-sectional soma area in tissue sections to test whether cellular enlargement contributed to the volume changes in HVC and RA.
HVC soma area increased within 7 days and remained enlarged at day 20. RA somata also enlarged by day 7, even though the major increase in RA volume occurred later, separating a cellular response from the timing of whole-nucleus expansion.
Cross-sectional area is an anatomical measure, not a direct measurement of membrane conductance or firing rate. Enlarged somata may accompany altered physiology, but this study did not record ion-channel activity from the cells whose sizes were measured.

RA expands without a comparable neuron increase|t4,t1|T
RA grew more slowly than HVC after breeding-like stimulation. Its neurons enlarged early, while the later increase in nucleus volume was accompanied by a reduction in neuron density rather than a clear increase in total neuron number.
By day 20, the same general neuronal population occupied a larger amount of tissue. This pattern differs from HVC, where substantial population growth contributed to enlargement within the first 7 days.
Lower density can be consistent with greater space occupied by neuronal processes or other tissue components, but it does not directly measure dendritic length, synapse number or glial proliferation. The study establishes different cellular signatures of seasonal growth in connected song nuclei.

Not every song nucleus follows the same growth schedule|t1,t3|T
The anterior forebrain song circuit contains Area X and LMAN, connected through the thalamic relay. Tramontin and colleagues measured these regions alongside the descending motor nuclei rather than assuming that every component responded uniformly to reproductive cues.
Area X enlarged more slowly than HVC, reaching its expanded condition at the 20-day time point. LMAN changed little over the same interval, despite occupying a circuit linked anatomically to the growing nuclei.
Regional selectivity argues against uniform swelling of the entire song system. It also limits a simple explanation in which circulating testosterone produces identical structural effects wherever a song-related neuron is present; receptor distribution, connectivity and cellular composition remain possible contributors.

Peripheral and brainstem responses have distinct timing|t1|T
The **syrinx** is the avian vocal organ, supplied by motor neurons in nXIIts. Tramontin and colleagues measured syringeal mass and the brainstem motor nucleus to compare peripheral vocal machinery with forebrain changes under breeding-like stimulation.
Syringeal mass increased within 7 days of long-day and testosterone exposure. The volume of nXIIts did not clearly enlarge over the 20-day observation period, even though this nucleus can vary over longer seasonal intervals.
A peripheral target can therefore respond while a connected brainstem structure has not yet changed detectably in volume. The study does not establish that the syrinx drives forebrain growth, and lack of measured volume change does not mean the motor neurons were physiologically unchanged.

Song measurements separate duration from consistency|t2|T
A **spectrogram** displays sound frequency over time, permitting individual song components to be measured. Tramontin and colleagues separated the white-crowned sparrow song into whistle, warble and buzz portions, using the published 2-kilohertz and 0.5-second calibration bars.
Mean whole-song duration was 1.80 seconds after 7 days of breeding-like stimulation and 1.84 seconds after 20 days. Whistle duration was similarly stable, approximately 0.51 and 0.52 seconds at the two time points.
Stable average duration does not mean identical renditions. Measurements of variation across repeated songs address consistency, while average durations describe the central timing of the vocal pattern. The study did not record comparable songs from the short-day birds because they did not sing.

Song becomes more stereotyped as circuits mature|t2,t1|T
**Stereotypy** means consistency across repeated performances. The sparrows’ temporal and spectral song features were more consistent after 20 days of breeding-like stimulation than after 7 days, even though mean song duration changed little.
Song rates were similar at the two time points, approximately three songs per minute during recording. Increased consistency therefore cannot be equated with simply singing more frequently, and it accompanied the slower growth of RA and Area X.
The study linked behavioral and anatomical time courses, but did not independently manipulate nucleus size while holding hormonal state constant. Circuit maturation and song stabilization covaried; the exact cellular change responsible for the improved consistency remains unresolved by these measurements.

Sequential growth supports a trophic hypothesis|t3,t1|T
A **trophic influence** is an effect that supports growth or maintenance of another cell or tissue. HVC grew before RA and Area X, creating the possibility that signals from HVC contribute to the subsequent enlargement of its connected targets.
The long-day and testosterone experiment established temporal sequence and distinct cellular responses: rapid HVC population growth, early soma enlargement, and later expansion of downstream nuclei. These findings constrain explanations of seasonal plasticity more precisely than volume comparisons alone.
The proposed trophic relationship was not directly tested by blocking a growth factor or an HVC projection. Direct steroid sensitivity, activity changes and other local mechanisms can also contribute, so sequential growth should remain evidence supporting a hypothesis rather than proof of one pathway.

Oxytocin accelerates experience-dependent pup retrieval|y1,yED1|Y
**Oxytocin** is a neuropeptide synthesized by hypothalamic neurons, including those in the **paraventricular nucleus**, or PVN. Marlin and colleagues tested its central behavioral effects in female mice, a mammalian comparison rather than a mechanism established for ring doves.
Initially inexperienced virgin females were housed with a mother and pups. Systemic oxytocin or optical stimulation of genetically targeted PVN oxytocin neurons accelerated retrieval of isolated pups, with many females beginning within 12 hours of co-housing.
Saline-treated females generally required longer experience. The manipulation changed the speed of acquiring a response in a social setting; it did not establish that oxytocin makes every inexperienced female perform maternal behavior independently of experience or pup-derived signals.

Maternal experience can substitute for pregnancy history|y1|Y
Marlin and colleagues compared mothers, inexperienced virgin females, and virgin females that acquired pup-retrieval behavior through experience. **Retrieval** is carrying an isolated pup back toward the nest, measured separately as successful responses and the time needed to perform them.
Experienced virgins retrieved with rates and speeds comparable to mothers. Oxytocin accelerated acquisition, while isolated virgins given oxytocin acquired retrieval more slowly than co-housed virgins receiving both hormonal modulation and social experience.
Pregnancy and parturition were therefore not necessary for successful performance in this experimental setting. The finding does not imply that maternal endocrine history is irrelevant; it establishes an alternative experiential route to the measured behavior in female mice.

Knockout controls verify cortical receptor labeling|y2bc|Y
An **oxytocin receptor** is a membrane protein coupled to intracellular signaling through G proteins, rather than a pore directly carrying synaptic current. Marlin and colleagues developed an antibody and tested its labeling against receptor-deficient mice, whose auditory cortex lacked the staining detected in normal animals.
They also compared staining with a genetic reporter linked to oxytocin-receptor expression. Agreement between independent labeling methods strengthened the interpretation that the marked cells express the receptor rather than an unrelated protein recognized by the antibody.
The **auditory cortex** is cortical tissue involved in sound processing. Receptor staining locates candidate sites of hormonal modulation, but does not measure receptor activation, downstream signaling strength or behavioral necessity. Those questions require physiological and intervention experiments in addition to anatomy.

Cortical inhibition contains oxytocin-sensitive cells|y2de|Y
**Interneurons** are local neurons that influence neighboring cells within a circuit. Marlin and colleagues identified oxytocin receptors on inhibitory cortical interneurons marked by parvalbumin or somatostatin, proteins used to distinguish important inhibitory cell populations.
Approximately 30–40 percent of the labeled parvalbumin-positive and somatostatin-positive populations expressed oxytocin receptors. Thus, hormone sensitivity included cells positioned to regulate local inhibition rather than being restricted to excitatory output neurons.
This colocalization supports a candidate route from oxytocin to inhibitory control, but the staining does not establish identical physiological effects in every receptor-positive cell. Subsequent synaptic recordings were required to determine how inhibition changed during hormone exposure and learning-related stimulation.

Receptor expression favors the left auditory cortex|y2gh|Y
Marlin and colleagues compared the left and right auditory cortex within female mice. Oxytocin-receptor labeling was more abundant on the left in both mothers and inexperienced virgins, indicating that the asymmetry was not limited to animals already performing retrieval.
In virgin females, approximately 19.5 percent of cells were receptor-positive on the left, compared with 14.3 percent on the right. Hypothalamic axonal projections did not have an equally obvious asymmetry, suggesting that receptor distribution contributes to local sensitivity.
An anatomical asymmetry does not by itself establish behavioral specialization. It identifies a candidate difference between hemispheres that can be tested by separately manipulating activity or oxytocin signaling in the left and right sound-processing regions.

Left auditory-cortex activity contributes to retrieval|y3,y2gh|Y
Marlin and colleagues infused **muscimol**, an agonist of inhibitory GABA_A receptors, into one auditory cortex at a time. GABA is an inhibitory neurotransmitter; GABA_A receptors are ion channels whose conductance constrains excitation. The intervention temporarily reduced local activity before retrieval testing.
Inactivation of the left cortex impaired retrieval in experienced females, whereas the corresponding right-side manipulation did not produce the same impairment. Before-treatment and after-treatment measurements helped distinguish the transient intervention effect from a permanent inability to perform the task.
The result establishes a contribution from left cortical activity under these conditions, not that this region alone generates the entire motor behavior. Hearing a relevant call and carrying a pup depend on additional sensory, motivational and motor components outside the infused region.

Oxytocin facilitates acquisition more than performance|y3,y2bc|Y
Local oxytocin delivery to the left auditory cortex accelerated retrieval in inexperienced female mice. Optical stimulation of oxytocin axons there produced a similar acceleration, connecting a localized neuromodulatory input to acquisition in the presence of pups and social experience.
In contrast, oxytocin-receptor antagonists infused into the left auditory cortex did not clearly impair retrieval after the behavior was established. An **antagonist** blocks receptor activation, allowing ongoing signaling to be tested separately from the effects of earlier exposure.
Acquisition and performance therefore have different experimental dependencies. The result is consistent with lasting circuit changes after oxytocin-assisted experience, but antagonist failure does not prove that oxytocin is unnecessary at every other site or during every maternal behavior.

Experience improves call-evoked spike reliability|y4,y2bc|Y
An **action potential** is a brief electrical event used by neurons to transmit output. Marlin and colleagues recorded single-cell responses to pup calls in mothers, inexperienced virgins and experienced virgins, using electrodes in the auditory cortex of anesthetized animals.
Calls evoked stronger and more precisely timed spiking in the left cortex of experienced females. Responses to pure tones were broadly comparable across groups, providing a control against interpreting the change as a uniform increase in responsiveness to all sounds.
Experience therefore modified responses to behaviorally relevant vocal signals. Recordings under anesthesia characterize cortical responses to controlled playback; they do not directly measure the neuron’s contribution during an awake retrieval episode or identify the entire downstream motor pathway.

Matched excitation and inhibition sharpen call responses|y5,y2de|Y
An **excitatory postsynaptic current** promotes neuronal activation, whereas an **inhibitory postsynaptic current** opposes or constrains it. Voltage-clamp recordings hold membrane voltage at selected levels so these call-evoked inputs can be examined separately in auditory cortical neurons.
Mothers and experienced virgins had better matched timing and call selectivity of excitation and inhibition than inexperienced virgins. The amplitudes of synaptic responses were broadly comparable, arguing against a simple explanation based only on stronger excitatory input.
**Excitation–inhibition balance** here means coordinated patterns across time and calls, not cancellation of every current at every instant. Measurements from separate recording conditions support this relationship, but do not capture both currents simultaneously within the same individual trial.

Oxytocin opens a window for lasting synaptic change|y6,y2de|Y
Marlin and colleagues paired pup calls with oxytocin application or stimulation of oxytocin axons. Inhibition decreased rapidly, within approximately 40–60 seconds, permitting a temporary change in the balance of inputs during exposure to the vocal signal.
Over subsequent minutes to hours, excitation and inhibition became better matched to the paired calls, and spiking became stronger and more temporally reliable. Inhibitory responses recovered while the improved coordination persisted, separating an early permissive change from the later learned circuit state.
The evidence supports neuromodulation of plasticity rather than permanent removal of inhibition. These are mouse auditory-cortex experiments; the comparable general principle that hormonal state changes sensory responsiveness does not establish the same receptor or synaptic mechanism in ring doves or seasonal songbirds.
"""
slides=[]
for block in DATA.strip().split('\n\n'):
 lines=block.splitlines();title,images,rs=lines[0].split('|');body=lines[1:];ks=rs.split(',');fs=[fg[x] for x in images.split(',')]
 s={'title':title,'body':body,'transcript':[re.sub(r'\*\*|_', '',p) for p in body],'cite':'; '.join(cites[k] for k in ks),'refs':[refs[k] for k in ks]}
 if len(fs)==1:s.update(layout='figure-right',figure=fs[0],figure_width=5.6)
 else:s.update(layout='figures-right',figures=fs,figure_width=6.0,figure_arrangement='side-by-side',primary_figure_width=4.0)
 slides.append(s)
assert len(slides)==44,len(slides)
spec={'lecture':39,'theme':'dust-blue-charcoal','content_slides':44,'title_image':{'path':'figures/dove.jpg','kind':'web','caption':'Photo: Domestic ring dove.','credit':'Frits Schouten / iNaturalist','license':'CC BY-NC 4.0','source_url':'https://www.inaturalist.org/photos/7178728'},'slides':slides,'takeaways':{'cite':'Lehrman (1955); Cheng & Silver (1975); Cheng (1986); Nottebohm (1981); Tramontin et al. (2000); Marlin et al. (2015)','refs':[refs[k] for k in ['P','C','F','N','T','Y']],'items':[
{'lead':'Hormones and experience interact.','text':'Prolactin-induced feeding depends on reproductive history and sensory conditions; a physiological response is not a complete behavioral program.'},
{'lead':'Reproductive coordination is reciprocal.','text':'Estrogen–progesterone treatment facilitates female nesting and incubation and changes behavior in untreated male partners.'},
{'lead':'Vocal behavior feeds back on physiology.','text':'Own-coo playback rescues follicular growth in muted females, supporting an acoustic contribution without excluding bodily feedback.'},
{'lead':'Seasonal plasticity is region-specific.','text':'Breeding-like conditions rapidly increase HVC neuron number; RA and Area X expand later, with different cellular signatures.'},
{'lead':'Anatomical sequence is not causal proof.','text':'Song consistency increases as circuitry develops, but sequential growth alone does not establish a particular trophic mechanism.'},
{'lead':'Hormones can facilitate sensory learning.','text':'In mice, oxytocin transiently reduces cortical inhibition and promotes lasting call-response coordination; acquisition and established performance have different dependencies.'}]}}
(R/'lecture.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n')
print('Wrote',len(slides),'content slides; word range',min(len(' '.join(s['body']).split()) for s in slides),max(len(' '.join(s['body']).split()) for s in slides))
