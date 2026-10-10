"""Lecture 73, source-verified teaching paragraphs and original article panels."""
from pathlib import Path
import json,re
B=Path(__file__).resolve().parent
R=json.loads((B/'research.json').read_text());F=json.loads((B/'figure_sources.json').read_text());S=[]
AUTH={'corwin':'Corwin & Cotanche','ryals':'Ryals & Rubel','hearing':'Sato et al.','fish_direct':'Beaulieu et al.','fish_genes':'Jiang et al.','posture':'Dickman & Lim','afferent':'Boyle et al.','reflex':'Carey et al.','fish_growth':'Sun et al.','physiology':'Hardy et al.','bird_cascade':'Benkafadar et al.','enhancers':'Shi et al.'}
YEAR={'corwin':1988,'ryals':1988,'hearing':2024,'fish_direct':2024,'fish_genes':2014,'posture':2004,'afferent':2002,'reflex':1996,'fish_growth':2011,'physiology':2021,'bird_cascade':2024,'enhancers':2024}
def short(k):return AUTH[k]+' ('+str(YEAR[k])+')'
def fig(n):
 x=F[n];return {'path':'figures/'+n+'.png','kind':'article','caption':short(x['paper'])+', Fig. '+x['figure']+'. '+x['description'],'source_url':'https://doi.org/'+R[x['paper']]['doi']}
def add(title,k,imgs,text,note):
 body=text.strip().split('\n\n');assert len(body)==3;assert len(title)<=62,title
 keys=list(dict.fromkeys([k]+[F[n]['paper'] for n in imgs]));z={'title':title,'body':body,'transcript':[re.sub(r'\*\*','',p) for p in body]+[note],'cite':'; '.join(short(x) for x in keys),'refs':[R[x]['reference'] for x in keys],'figure_width':5.8}
 if len(imgs)==1:z.update(layout='figure-right',figure=fig(imgs[0]))
 else:z.update(layout='figures-right',figures=[fig(n) for n in imgs],primary_figure_height=2.5)
 S.append(z)
add('Regenerated avian hair cells restore auditory sensitivity','hearing',['hearing_recovery','bird_anatomy'],'''
A **hair cell** is a sensory receptor that converts mechanical displacement into an electrical response. In birds, auditory hair cells occupy the **basilar papilla**, the elongated sensory epithelium of the inner ear. Loss of these receptors interrupts the input that normally carries sound information to auditory neurons.

Sato and colleagues infused sisomicin, a hair-cell-toxic aminoglycoside antibiotic, into the chicken inner ear. Hearing was initially undetectable, but regenerated receptors and renewed neural contacts subsequently accompanied recovery. **Auditory brainstem responses**, or ABRs, are sound-evoked electrical responses recorded from the auditory pathway.

The first consistent threshold improvement appeared 9–11 days after treatment. A **threshold** is the lowest sound level producing the measured response. Over five weeks, thresholds approached pre-injury levels, linking replacement of peripheral receptors with renewed sensitivity in the auditory system.
''','Threshold recovery was variable across animals and frequencies. Some birds retained a threshold shift at five weeks. The investigators removed the opposite basilar papilla to prevent the untreated ear from contributing auditory responses while preserving its vestibular organs.')
add('Hair cells convert water motion into afferent firing','physiology',['phys_calcium'],'''
Zebrafish also possess hair cells in the **lateral line**, a sensory system that detects water motion along the body surface. Its receptors form clusters called **neuromasts**, each containing hair cells surrounded by supporting cells. This surface organ provides access for live imaging and controlled mechanical stimulation.

A **hair bundle** consists of projecting stereocilia, the mechanically sensitive extensions of a hair cell. Their displacement opens mechanoelectrical transducer channels, membrane pores whose gating depends on mechanical force. The resulting electrical response promotes calcium signaling and neurotransmitter release at the cell’s basal pole.

An **afferent neuron** carries sensory information toward the central nervous system. Hardy and colleagues displaced neuromast bundles with a fluid jet and measured calcium responses in hair cells and afferent terminals. These measurements connect water displacement with communication from the receptor to its innervating neuron.
''','The lateral line is a water-motion system rather than the zebrafish hearing organ. Hair cell polarity specifies the excitatory direction of displacement, and afferents connect to hair cells sharing that polarity. Fluid-jet stimulation permits calcium responses to be compared across bundle orientations.')
add('Receptor position organizes avian auditory input','hearing',['bird_anatomy','bird_innervation'],'''
**Tonotopy** is the ordered representation of sound frequency across an auditory structure. The chicken basilar papilla has a frequency gradient along its length, while its width separates medial tall hair cells from lateral short hair cells. Medial and lateral are also called neural and abneural in this tissue.

Sisomicin removed hair cells across the sensory epithelium. Surviving **supporting cells**, the neighboring nonsensory cells that maintain the epithelium and can produce replacement receptors, remained between the sites formerly occupied by hair cells. Auditory nerve processes withdrew toward the underlying basement membrane.

New hair cells formed basal projections and were contacted by regrowing afferents. Sato and colleagues hypothesize that local reconnection helps preserve frequency-specific relationships. Regenerated contacts extended along the tonotopic axis, making spatial organization part of auditory repair as well as receptor replacement.
''','The hypothesis concerns preservation of relationships along the frequency gradient. The study measured anatomical reconnection and ABR thresholds rather than following the tuning of each individual afferent before and after injury. Tall and short hair cells have different positions within the avian sensory epithelium.')
add('Vestibular receptors support compensatory eye movement','reflex',['reflex_trace','reflex_anatomy'],'''
The **vestibular system** detects head motion and contributes to balance and gaze stabilization. Its sensory hair cells occupy the rotation-sensitive semicircular canal cristae and the gravity- and acceleration-sensitive otolith organs. Carey and colleagues examined the **vestibuloocular reflex**, or VOR, the compensatory eye movement generated during head motion.

During sinusoidal head rotation, the eyes normally move in the opposite direction. **Gain** describes the ratio of eye velocity to head velocity, while **phase** describes their relative timing. Reduced gain means that eye movement compensates less effectively for head movement.

Streptomycin treatment depleted vestibular hair cells in chicks and nearly eliminated the reflex during the first recovery week. Hair cell density and reflex responses subsequently increased over several weeks. Repair of vestibular receptors therefore reestablishes a sensory input needed for stabilizing the visual scene during movement.
''','The preparation received streptomycin injections for five days. The source compares reflex measurements with hair cell density in the horizontal canal and utricle. The neural pathway includes peripheral afferents and central circuitry, so the reflex measures integrated function rather than receptor count alone.')
add('Acoustic injury reactivates division in avian epithelia','corwin',['classic_division','classic_surface'],'''
**Mitosis** is the division that produces daughter cells after DNA replication. Corwin and Cotanche exposed young chickens to a 1.5 kHz tone for 48 hours and examined the damaged auditory epithelium during recovery. The exposure removed hair bundles and produced a localized sensory lesion.

The investigators administered **tritiated thymidine**, a radioactive DNA precursor incorporated during replication. **Autoradiography** detects this incorporation as silver grains over labeled nuclei. After injury, labeled nuclei occurred in both hair cells and supporting cells within the recovering region.

Uninjured controls and undamaged regions of exposed ears lacked comparable labeling in these epithelial cell types. The normally quiescent tissue therefore activated a proliferative response after acoustic trauma. Surviving supporting cells retained the capacity to contribute new sensory cells after developmental hair cell production had ended.
''','The acoustic exposure was 115–120 dB sound pressure level. The published experiment combines thymidine incorporation with epithelial anatomy. It supports production of new cells after injury rather than merely regrowth of bundles on every surviving hair cell.')
add('New hair bundles mature within the recovering lesion','corwin',['classic_surface'],'''
The apical surface of the chicken auditory epithelium contains hair bundles separated by narrow supporting-cell surfaces. A **lesion** is an area of tissue injury. Corwin and Cotanche examined the same approximate epithelial location immediately after acoustic trauma and during the following ten days.

At the injury site, normal bundles disappeared and extruded hair cell bodies accumulated. By six days, small bundles were present among enlarged supporting-cell surfaces. Their short stereocilia and surrounding microvilli resembled features normally associated with immature hair cells.

The epithelial surface approached its normal appearance by ten days. Bundle growth therefore followed a sequence of receptor maturation inside the injured region. Combined with DNA labeling, this recovery linked production of replacement cells with construction of the mechanically sensitive surface that receives acoustic stimulation.
''','Microvilli are small membrane projections, distinct from the specialized mechanosensitive stereocilia bundle. The original electron micrographs contain their scale bars. Surface recovery was an anatomical endpoint; the later chicken study separately measured auditory thresholds.')
add('Adult quail regenerate receptors after acoustic trauma','ryals',['quail_counts','quail_birth'],'''
Hair cell regeneration also occurs in mature birds. Ryals and Rubel exposed adult Coturnix quail to a 115 dB tone for 12 hours and counted auditory hair cells along the basilar membrane at successive recovery times. Adult animals separated the injury response from ordinary early postembryonic development.

The middle region initially lost a large fraction of its hair cells. Counts at 30 and 60 days increased toward the normal complement, with recovery to within 5% of the original number. The damaged region regained cells without a corresponding depletion in undamaged regions.

Total receptor number increased across the organ, making redistribution of existing hair cells an inadequate explanation for recovery. The adult sensory epithelium retained a source of replacement cells, extending regenerative capacity beyond the juvenile chicken preparation used in the parallel acoustic-trauma study.
''','The quantitative profiles are counts at locations spaced along the organ. The paper reports an initial local loss approaching 70%, followed by substantial recovery. Counts concern receptor restoration and are distinct from an assessment of hearing thresholds.')
add('DNA labeling identifies newly produced adult hair cells','ryals',['quail_birth'],'''
Ryals and Rubel tested whether adult quail recovery included production of new cells by administering tritiated thymidine after acoustic trauma. Tissue was collected ten days later for autoradiography. A nucleus retaining this label had synthesized DNA during the post-injury labeling period.

Labeled hair cells and supporting cells occurred within the region of initial receptor loss. Both tall and short hair cells were labeled, with short hair cells more frequently labeled in this preparation. Unexposed birds receiving the same injections lacked comparable labeling in these epithelial cell types.

Receptor birth therefore followed injury after developmental production had ceased. The paired anatomical and labeling experiments distinguish new-cell production from receptor migration or simple enlargement of surviving cells. Adult quail maintain a regenerative cellular reserve within the auditory epithelium that can be activated by sensory damage.
''','Silver grains locate radioactive label over nuclei in the original tissue sections. The experiment did not provide a modern lineage-specific genetic trace of every precursor. Its conclusion rests on post-injury DNA incorporation into identified sensory and supporting cells.')
add('Supporting cells change gene expression within one hour','fish_genes',['genes_early','fish_animal'],'''
**Gene expression** is the production of RNA from DNA and, for protein-coding genes, the subsequent production of protein. Jiang and colleagues examined the early regenerative response in zebrafish neuromasts after neomycin, an aminoglycoside antibiotic, killed hair cells.

Fluorescent supporting and mantle cells were isolated by **fluorescence-activated cell sorting**, which separates cells according to fluorescent signals. Mantle cells form the outer neuromast ring; inner supporting cells surround the central receptors. Hair cells lacked the sorting label and were excluded from the enriched population.

**RNA sequencing** measured transcripts at 1, 3, and 5 hours after injury. In situ hybridization, a method that localizes selected RNA molecules in tissue, confirmed early expression changes within neuromasts. The cellular response began before substantial receptor replacement, placing rapid transcriptional regulation at the start of regeneration.
''','The analysis enriched a mixed mantle and inner-supporting-cell population rather than sequencing purified hair cells. Sox2 labeling and lateral-line marker expression verified cell enrichment. In situ hybridization preserved the anatomical localization of selected transcript changes.')
add('Cell-cycle responses precede Wnt pathway activation','fish_genes',['genes_cycle'],'''
The **cell cycle** is the sequence through which a cell grows, replicates DNA, and divides. Jiang and colleagues found that cell-cycle regulators changed early after neuromast injury. Their expression pattern indicated release from the regulatory state that normally restrains supporting-cell proliferation.

**Wnt signaling** is a pathway in which extracellular Wnt proteins regulate intracellular effectors, including β-catenin, that influence gene expression. In this regeneration time course, Wnt pathway activation appeared later than the earliest cell-cycle response. Wnt-associated activity rose around 12 hours after neomycin treatment.

The authors’ hypothesis is that Wnt regulates later regenerative proliferation rather than initiating the first division response. The order of events separates activation of a proliferative program from subsequent control of its extent, so early cell-cycle changes should not be assigned automatically to the later Wnt signal.
''','Cyclin-dependent kinases are enzymes involved in advancing the cell cycle, and their inhibitors restrain progression. The study followed transcripts and a Wnt-responsive reporter. Timing constrains the proposed initiating mechanism but does not identify every upstream injury signal.')
add('Transient Notch reduction changes the regenerative state','fish_genes',['genes_notch'],'''
**Notch signaling** is communication between neighboring cells through membrane-bound ligands and Notch receptors. Its downstream transcriptional regulators influence whether a sensory epithelial cell adopts a hair cell identity. Jiang and colleagues measured pathway-associated genes during early zebrafish lateral-line regeneration.

Several Notch targets decreased shortly after neomycin injury and subsequently recovered. The hair-cell-associated regulator **atoh1a** changed in the same regenerative interval. Atoh1a encodes a transcription factor, a DNA-binding protein that regulates expression of other genes involved in receptor differentiation.

The transient response permits a changing balance between replacement-cell production and maintenance of nonsensory supporting cells. Notch-associated regulation resumes as the tissue rebuilds, helping constrain the final cellular composition. Regeneration therefore involves timed changes in neighboring-cell communication rather than a permanent removal of every inhibitory signal.
''','The original transcript profiles distinguish early Notch reduction from later recovery. A pathway expression change is different from a receptor-level perturbation. Shi and colleagues subsequently tested Notch inhibition directly in the inner-ear enhancer experiments.')
add('A transgenic ion channel enables crista hair cell ablation','fish_direct',['fish_ablation','fish_ear'],'''
A **crista** is the sensory patch in a semicircular canal that contains motion-sensitive hair cells. Beaulieu and colleagues engineered zebrafish crista hair cells to express mammalian **TRPV1**, a membrane channel that opens in response to capsaicin, the pungent compound in chili peppers.

Endogenous zebrafish Trpv1 is insensitive to capsaicin, allowing the introduced mammalian channel to target the labeled receptors. A 1 hour exposure to 10 µM capsaicin produced cation influx and rapid hair cell death. Supporting-cell numbers were largely preserved, and debris cleared within several hours.

Sibling controls lacking the effective transgene retained their receptors during capsaicin exposure. This genetic ablation, the experimentally induced removal of selected cells, made protected inner-ear sensory patches accessible to regeneration studies. Receptor replacement could then be compared with normal growth in the same larval organ.
''','The method worked consistently in the cristae but not in every macular or lateral-line organ in this transgenic line. Larval cristae are present before they become fully functional, so cell regeneration at these ages is not equivalent to measured recovery of balance behavior.')
add('Regenerated cristae recover regional hair cell identities','fish_direct',['fish_pattern'],'''
Crista hair cells differ according to their position within the sensory patch. Beaulieu and colleagues distinguished peripheral cells expressing **cabp1b** from central cells lacking that marker. Hybridization chain reaction amplified the RNA signal so that subtype identity could be localized in individual cells.

At two days after ablation, regenerated cristae contained a greater proportion of new central-type cells than growing control cristae. The complementary central marker **scn5lab** supported this shift. Recovery therefore initially favored one receptor identity instead of replacing every subtype in its original proportion immediately.

By fourteen days, overall hair cell numbers and the central-to-peripheral spatial pattern approached control organization. The recovered tissue reestablished both cell abundance and regional identity. Organ repair thus includes restoration of the arrangement of receptor subtypes, with an early transient imbalance followed by later pattern recovery.
''','The markers identify regional molecular phenotypes. The study did not measure distinct physiological responses of the regenerated subtypes. Central identity was supported by reciprocal markers rather than inferred only from cell position.')
add('Supporting-cell division briefly expands the precursor pool','fish_direct',['fish_division'],'''
**EdU** is a thymidine analog incorporated into newly synthesized DNA during S phase, the DNA-replication stage of the cell cycle. Beaulieu and colleagues administered 24 hour EdU pulses at successive times after zebrafish crista hair cell ablation.

Supporting cells incorporated substantially more EdU during the first day after injury than in control cristae. Pulses at days 3–4 and 6–7 no longer revealed the same excess. The injury therefore elicited an early wave of supporting-cell proliferation rather than a sustained increase throughout receptor replacement.

Most newly added hair cells lacked EdU during each pulse interval. Supporting-cell division expanded the pool available for repair, while receptor production proceeded largely without immediate DNA replication in the differentiating cell. The tissue’s proliferative response and its production of new hair cells were temporally separable processes.
''','Supporting cells near the sensory patch expressed the supporting-cell marker zpld1a. The rare EdU-positive hair cells were sometimes paired with a labeled supporting cell, compatible with occasional asymmetric divisions. The predominant regenerative mechanism differed from the proliferative zebrafish lateral line.')
add('Crista cell conversion is uncoupled from recent division','fish_direct',['fish_conversion'],'''
**Transdifferentiation** is conversion from one differentiated cell identity to another. Beaulieu and colleagues combined EdU pulse-chase labeling with photoconversion to determine when crista supporting cells divided and when their descendants became hair cells.

**Photoconversion** changes an existing fluorescent protein to another color with light, marking the hair cells already present. Newly formed hair cells retain the unconverted signal. After an EdU pulse during the first day of regeneration, labeled hair cells became more common several days later.

The fraction of new hair cells carrying EdU was similar in injured and control cristae. Injury-induced division therefore increased the precursor pool without making each recently divided cell more likely to differentiate. Most receptor addition arose through direct conversion, while a smaller population converted after an earlier division separated in time from differentiation.
''','The comparison was based on the fraction of newly added cells carrying EdU, not only their absolute number. Absolute numbers increased with the larger regenerative response. This distinction supports temporal uncoupling of pool expansion and cell-fate conversion.')
add('Long-range enhancers permit Atoh1 expression','enhancers',['enhancer_activity'],'''
An **enhancer** is a regulatory DNA sequence that influences gene expression, sometimes from a position far from the gene’s promoter. Shi and colleagues identified long-range enhancers associated with **Atoh1**, the transcription factor that helps specify hair cell identity.

Fluorescent reporter constructs linked selected enhancer sequences to detectable expression in zebrafish inner-ear cells. Different regulatory elements were active in supporting cells and hair cells, separating elements associated with initiating the hair cell program from those associated with maintaining it after differentiation.

Supporting-cell-active elements provide a regulatory route through which a nonsensory cell can activate Atoh1 after injury. Their activity preceded the hair-cell-associated autoregulatory state, in which Atoh1 supports its own expression. The onset and maintenance of receptor identity therefore depend on distinguishable classes of regulatory DNA.
''','The source calls these initiation-associated elements class 2 enhancers and distinguishes them from class 1 hair-cell-associated elements. Reporter activity was evaluated in the inner ear. Each class has its own developmental accessibility pattern.')
add('Adult regenerative supporting cells retain open chromatin','enhancers',['enhancer_chromatin'],'''
**Chromatin** is DNA together with its associated proteins. **Chromatin accessibility** describes how exposed a DNA region is to regulatory proteins and experimental probing. Shi and colleagues compared accessible regions near Atoh1 in zebrafish, anole lizards, and mice.

Long-range enhancers retained accessibility in adult supporting cells of regenerative fish and lizards. Corresponding regions became less accessible during development of the nonregenerative mouse cochlea. The comparison separated supporting-cell regulatory competence from gene expression in already differentiated hair cells.

Accessible regulatory DNA can remain available even when Atoh1 expression is suppressed. The authors’ hypothesis is that retention of this developmental regulatory state contributes to adult regenerative competence. Injury can then recruit an existing accessible program rather than requiring every regulatory element to reopen from a closed state.
''','Single-nucleus ATAC sequencing assays chromatin accessibility, while RNA sequencing measures expression. Accessibility alone is not proof that a gene is currently transcribed. The study also used enhancer reporters and deletion experiments to test regulatory function.')
add('Notch repression restrains an accessible hair cell program','enhancers',['enhancer_activity'],'''
Supporting cells can retain accessible Atoh1 regulatory elements while remaining nonsensory. Shi and colleagues tested whether **Notch-dependent repression** restrains expression from these elements in the zebrafish inner ear. Repression is regulation that reduces gene transcription.

The investigators blocked Notch activation with a γ-secretase inhibitor. γ-secretase is the protease involved in releasing the signaling portion of activated Notch. Inhibition increased enhancer-associated reporter expression in supporting cells of the crista and utricle within 48 hours.

An accessible enhancer therefore supplies competence, while signaling from neighboring cells helps control whether that competence is used. Injury and Notch reduction can change the transcriptional state without requiring complete reconstruction of the regulatory landscape. Maintenance of supporting-cell identity depends on active repression as well as on the availability of hair-cell-promoting DNA elements.
''','The study used 10 µM DBZ in the reporter experiment. It compared regulatory activity with and without Notch inhibition and after injury. Open chromatin and active transcription are distinct states that can be experimentally separated.')
add('Enhancer deletion separates two sensory organs','enhancers',['enhancer_deletion'],'''
A **deletion experiment** removes a selected DNA region and measures the consequences. Shi and colleagues deleted groups of long-range atoh1a enhancers from zebrafish, testing their function in the inner ear and in lateral-line neuromasts.

Deletion reduced atoh1a expression and hair cell numbers in inner-ear sensory organs. It also impaired supporting-cell conversion during inner-ear regeneration. Lateral-line hair cell production was comparatively preserved, even though both organs use Atoh1a and contain mechanically sensitive receptors.

The two sensory systems therefore have different regulatory requirements for activating the same cell-identity factor. A gene shared across organs can be controlled by different enhancers in each tissue. This organ specificity connects regulatory DNA with the contrasting regenerative routes of inner-ear conversion and lateral-line proliferative replacement.
''','The displayed developmental panels compare cristae, utricles, and neuromasts in wild-type and enhancer-deletion animals. The regeneration experiments in the same paper extend the deletion result to injury. The inference is organ specificity, not loss of regenerative capacity in every zebrafish sensory tissue.')
add('Dying avian hair cells evoke an early supporting-cell state','bird_cascade',['cascade_response'],'''
Benkafadar and colleagues followed chicken supporting cells after sisomicin-induced hair cell death. **Single-cell RNA sequencing** measures transcript abundance in individual cells, allowing changing cellular states to be distinguished within a mixed tissue.

An early responding supporting-cell population appeared 12–20 hours after treatment. Its transcripts included **HBEGF**, a growth-factor ligand, and **F2RL1**, a protease-activated membrane receptor. Hair cells underwent apoptosis, a regulated cell-death process, before extrusion from the sensory epithelium.

RNA localization placed the early-response genes in supporting cells adjacent to dying receptors. These molecular changes preceded S-phase entry around 36 hours. The sequence links local sensory-cell loss with a distinct supporting-cell signaling state before proliferation begins, placing injury detection upstream of replacement-cell production.
''','The experiment sampled baseline and 12, 16, 20, and 38 hour states in seven-day-old chickens. Hybridization chain reaction confirmed the spatial distribution of selected transcripts. Early signaling and later DNA replication were measured at different points in the same response.')
add('Protease-activated F2RL1 contributes to injury signaling','bird_cascade',['cascade_perturb','cascade_response'],'''
A **protease** is an enzyme that cleaves proteins. F2RL1 is a **G-protein-coupled receptor**, a membrane receptor that transmits extracellular signals through intracellular G proteins. Proteolytic activation can connect extracellular tissue changes with the supporting cell’s internal signaling state.

Benkafadar and colleagues inhibited F2RL1 before sisomicin injury. Supporting cells subsequently incorporated less EdU at 48 hours, connecting receptor activity with entry into DNA replication. The same study localized increased F2RL1 transcripts to the early responding sensory epithelium.

Activating F2RL1 without hair cell injury failed to induce supporting-cell S phase. F2RL1 activity therefore contributes to the response within an injured tissue, but receptor stimulation alone is insufficient. The regenerative program requires a coordinated injury context rather than a single isolated receptor signal.
''','The F2RL1 antagonist was FSLLRY-NH2. The authors propose that extracellular proteases activate the receptor after hair cell demise. The agonist result changes the mechanistic conclusion by separating contribution to the response from sufficiency to initiate it.')
add('EGFR activity recruits ERK phosphorylation during repair','bird_cascade',['cascade_erk','cascade_response'],'''
**EGFR**, the epidermal growth factor receptor, is a membrane receptor with protein-tyrosine kinase activity. A **kinase** transfers phosphate groups to proteins, changing their signaling state. HBEGF can activate EGFR after release from its membrane-associated precursor.

The authors’ hypothesis is that **matrix metalloproteases**, enzymes that cleave extracellular or membrane-associated proteins, release HBEGF and recruit EGFR signaling after F2RL1 activation. Inhibiting F2RL1, metalloproteases, or EGFR reduced downstream ERK1/2 phosphorylation after hair cell injury.

**ERK1/2** are signaling kinases that link receptor activation with cellular responses. Phosphorylated ERK increased about tenfold at 24 hours after sisomicin. The perturbations place these upstream components before ERK activation, connecting an extracellular injury response with an intracellular pathway associated with supporting-cell proliferation.
''','Phosphorylation was measured by immunoblotting. The precise HBEGF-shedding order is the authors’ proposed model, while inhibitor-dependent reduction of ERK phosphorylation is the measured result. The body labels the proposed ordering as a hypothesis rather than treating every step as directly visualized.')
add('Pathway blockade suppresses proliferation and repair','bird_cascade',['cascade_perturb','cascade_newcells'],'''
Benkafadar and colleagues inhibited components of the proposed regenerative cascade before inducing hair cell loss. EdU incorporation measured supporting-cell entry into S phase at 48 hours. Later MYO7A labeling identified regenerated hair cells, linking an early proliferation assay with a differentiated-cell endpoint.

Inhibiting metalloproteases, EGFR, or ERK1/2 strongly suppressed the DNA-replication response. Repeated inhibitor exposure also reduced the production of new hair cells and mature hair bundles by day nine. Brief and repeated treatments distinguished delayed regeneration from longer-lasting pathway suppression.

Supporting-cell apoptosis was not increased at the early assay time under these conditions, so reduced EdU labeling was not explained simply by elimination of the precursor population. The pathway interventions impaired progression through a regenerative program that normally connects supporting-cell activation with production of new sensory receptors.
''','MYO7A is a hair-cell-associated motor protein used for immunolabeling. SOX2 identified supporting cells. TUNEL assessed apoptotic DNA fragmentation. Inhibitor effects differed among pathway components, and the source reports some surrounding-cell toxicity with specific treatments.')
add('ERK-linked transcription precedes receptor differentiation','bird_cascade',['cascade_tf','cascade_response'],'''
**Transcription factors** connect signaling activity with changes in gene expression by regulating target DNA regions. Benkafadar and colleagues identified a transient supporting-cell response involving ATF3, FOSL2, and CREM before the production of regenerated hair cells.

Inhibition of F2RL1, metalloproteases, EGFR, or ERK reduced induction of these factors. Other responsive factors, including KLF6 and TCF24, followed a different dependence pattern. The injury response therefore contained distinguishable regulatory branches rather than a single uniform transcriptional output.

**STAT3** is a signaling protein that can act as a transcriptional regulator after phosphorylation. Its inhibition partially reduced supporting-cell S-phase entry without preventing ERK phosphorylation. ERK-dependent and STAT3-associated signaling thus contribute differently to the transition from early injury response to proliferation and subsequent sensory-cell differentiation.
''','The source quantified selected transcripts by real-time PCR and phosphorylation by immunoblotting. ATF3, FOSL2, and CREM increased transiently and declined by 38 hours. A transient transcriptional state precedes the later mature receptor phenotype.')
add('Acoustic injury damages zebrafish saccular bundles','fish_growth',['growth_celltypes','growth_bundles'],'''
The **saccule** is an inner-ear sensory organ containing hair cells involved in fish hearing. Sun and colleagues exposed adult zebrafish to a 150 Hz underwater tone for 40 hours and examined the saccular epithelium after exposure.

**Phalloidin** binds filamentous actin and labels the stereocilia that form hair bundles. The investigators distinguished normal bundles, damaged bundles, thin bundles, and bundleless cells. Buffer-treated fish had lower bundle density in the central and caudal saccule than unexposed baseline animals.

The spatial injury pattern concentrated receptor damage within particular parts of the sensory organ. Counting bundles at matched positions separated local damage from a change in the organ’s overall size. Reconstructing this mechanically sensitive surface was an anatomical endpoint for testing interventions that alter the response to acoustic trauma.
''','The source level was 179 dB referenced to 1 µPa root mean square underwater pressure; this reference differs from airborne sound pressure conventions. The printed PDF renders the micro symbol inconsistently in text extraction. The experiment used a controlled exposure chamber, not ordinary aquarium sound.')
add('Growth hormone improves post-injury bundle density','fish_growth',['growth_bundles'],'''
**Growth hormone**, or GH, is a peptide signal that regulates growth and can also act locally in tissues. Sun and colleagues injected recombinant carp GH after zebrafish acoustic exposure and compared the resulting saccular hair bundles with buffer-injected and unexposed animals.

At two days after sound exposure, GH-treated fish had bundle densities close to baseline across the sampled saccular positions. Buffer-treated fish retained lower densities, especially toward the caudal region. The effect therefore concerned the injured sensory epithelium rather than only whole-animal growth.

Because treatment began immediately after exposure, the preserved density could include both accelerated replacement and reduced continuing cell loss. The accompanying proliferation and apoptosis assays measured these candidate processes separately. GH modified the post-injury balance between receptor loss and restoration within a short recovery interval.
''','The paper does not measure hearing thresholds in this experiment. Density recovery is therefore an anatomical endpoint. Growth hormone could protect damaged cells as well as accelerate replacement, a distinction supported by the separate cell-death measurements.')
add('Growth hormone changes proliferation and cell survival','fish_growth',['growth_proliferation','growth_survival'],'''
Sun and colleagues measured two cellular processes after acoustic injury: DNA replication and apoptosis. **BrdU**, a thymidine analog, labeled newly synthesized DNA, while **TUNEL** detected DNA fragmentation associated with apoptotic cell death.

GH treatment increased BrdU-labeled cells one day after exposure and reduced TUNEL-labeled cells relative to buffer controls. The response therefore altered both addition to the proliferating population and loss from the injured tissue. These processes can contribute together to the later increase in bundle density.

Blocking endogenous GH signaling reduced post-injury proliferation in inner-ear sensory organs. The intervention connects the tissue’s own GH-associated activity with its regenerative response. Enhanced proliferation and improved survival are complementary routes by which a modulatory signal changes the number of cells available to rebuild the sensory epithelium.
''','Endogenous GH transcripts were also localized around erythrocyte nuclei in vessels near sensory tissue. This localization suggests a potential local source but does not by itself establish the complete signaling route. BrdU-positive cells were counted in sensory organs, not assumed all to be newly differentiated hair cells.')
add('Copper injury spares afferents at a selected concentration','physiology',['phys_damage','phys_support'],'''
**Ototoxicity** is toxicity that damages the ear or related sensory receptors. Hardy and colleagues exposed larval zebrafish to copper sulfate to remove lateral-line hair cells and follow their functional regeneration. The concentration controlled which parts of the sensory system were affected.

A 2 hour treatment with 10 µM copper removed about 95% of hair cells while preserving most afferent terminals. Higher concentrations also damaged afferent fibers and supporting cells. The lower dose separated receptor loss from more extensive disruption of the neuromast’s cellular environment.

Hair cell numbers increased toward control levels within 48 hours in early larvae. Preserved supporting cells and neural terminals provided a local framework for rebuilding receptors and reconnecting their output. Dose-dependent injury therefore supplied distinct experimental conditions for testing receptor replacement and the contributions of surrounding cells.
''','The displayed supporting-cell contacts are from the related regeneration experiment in the same study. Copper sensitivity differed among hair cells, afferent terminals, and supporting cells. The principal low-dose protocol was applied at three days after fertilization.')
add('Bundle displacement recruits calcium in repaired receptors','physiology',['phys_calcium'],'''
Hardy and colleagues used **R-GECO**, a fluorescent calcium indicator expressed in hair cells, to detect responses to mechanical stimulation. A fluid jet displaced the neuromast cupula, the gelatinous structure coupling water motion to the hair bundles.

Excitatory displacement opens mechanoelectrical transducer channels and changes the receptor’s electrical state. Calcium-dependent signaling accompanies activation at the basal synaptic pole. **GCaMP3**, a calcium indicator expressed in afferent neurons, reported activity in the contacting neural terminals.

After copper injury, fewer regenerated cells and contacts initially responded to stimulation. By 48 hours in early larvae, the fractions responding approached control values. Repair therefore restored the connection between mechanical input and cellular activation on both sides of the receptor-afferent interface, while individual contacts retained different response properties.
''','Fluorescence changes report calcium signals rather than direct recordings of every membrane channel. The study compared presynaptic hair cell responses with postsynaptic afferent responses. Not every anatomically present terminal produced a detectable calcium response during the stimulus.')
add('Glutamate release and afferent spikes return rapidly','physiology',['phys_baseline'],'''
**Glutamate** is the neurotransmitter released by these hair cells to communicate with afferent neurons. A neurotransmitter is a chemical messenger released at a synapse, the specialized junction between communicating cells. Hardy and colleagues monitored release with **iGluSnFR**, a fluorescent glutamate sensor.

Copper injury nearly eliminated spontaneous afferent action potentials, the rapidly propagating electrical impulses of neurons. Firing became comparable to control recordings toward the end of the first recovery day. Regenerating hair cells also displayed spontaneous glutamate-release signals during the following day.

The recovered output connects the newly formed receptor population with renewed neural activity. Hair cells at different maturation stages coexisted, so some cells released transmitter while others remained less active. Restoration of average afferent firing can therefore precede completion of receptor addition and refinement of every individual synaptic contact.
''','The electrophysiological recordings were made from posterior lateral-line ganglion neuron cell bodies. The glutamate reporter labeled only some hair cells in each neuromast. Detection of spontaneous transmission and recovery of mechanically evoked responses are separate functional measurements.')
add('Fluid-jet stimulation restores stimulus-evoked firing','physiology',['phys_evoked','phys_calcium'],'''
Spontaneous firing establishes that an afferent is active, whereas **stimulus-evoked firing** measures its response to sensory input. Hardy and colleagues displaced hair bundles with a controlled fluid jet and recorded action potentials from posterior lateral-line ganglion neurons.

At 48 hours after copper treatment, mechanical stimulation produced a rapid increase in firing from baseline, similar to age-matched controls. The peak response and **first-spike latency**, the delay between stimulus onset and the first recorded impulse, approached control behavior.

The repaired receptor-afferent connection therefore conveyed the onset of water displacement as well as spontaneous activity. This timing relationship is part of sensory recovery because the central nervous system receives information through the pattern of impulses, including when they begin and how strongly they increase during stimulation.
''','Action potentials are brief electrical impulses that carry sensory information along afferent axons. Mechanically evoked firing requires receptor activity to reach the afferent through synaptic transmission. The study measured induced activity directly rather than inferring it from cell counts.')
add('Ribbon contacts are rebuilt and subsequently refined','physiology',['phys_ribbons'],'''
A **ribbon synapse** contains a presynaptic specialization associated with transmitter release by a hair cell. Hardy and colleagues labeled CtBP proteins, markers of synaptic ribbons, together with hair cells and afferent terminals during lateral-line regeneration.

Ribbon-marker puncta reappeared rapidly after copper treatment and contacted afferent processes. By 24 hours, counts were comparable to untreated tissue, but substantial variability remained during the following day. **Puncta** are small localized spots of immunolabeling used here to identify synaptic specializations.

Afferent terminals also occupied regenerating neuromasts before visible hair cells had returned. New receptor production therefore occurred within a partly preserved or regrowing neural framework. Continued addition of hair cells and refinement of ribbon contacts extended beyond the earliest return of spontaneous firing, producing a more complete neuromast by about two days.
''','CtBP labeling identifies presynaptic structures and was interpreted alongside physiological measurements. The fluorescent reporter detects nascent hair cells early, reducing the possibility that all apparently empty contacts simply belonged to unlabeled mature receptors. Anatomy and function were assessed with complementary assays.')
add('Older zebrafish larvae recover on a slower time scale','physiology',['phys_older'],'''
Hardy and colleagues compared early larvae with fish injured at twelve days after fertilization. **Days post-fertilization**, abbreviated dpf, measures developmental age, while hours post-treatment measures time elapsed after the injury protocol. Developmental state changed the trajectory of repair.

Older larvae regenerated hair cells and resumed afferent firing more slowly. Active regenerated receptors could drive neural responses within approximately 48 hours, but full recovery required more than 120 hours. Age-matched controls normally contained more high-frequency spontaneous-firing afferents than very young larvae.

Similar eventual receptor numbers therefore concealed different rates of rebuilding a mature sensory interface. Regeneration must restore the functional properties appropriate to the animal’s developmental stage, including its characteristic firing distribution and synaptic organization. The rapid one-day response of early larvae is not a universal recovery interval for all zebrafish ages.
''','The older groups were followed through approximately seventeen days after fertilization. The measurements concern the lateral line, not adult hearing recovery. The source distinguished return of detectable receptor activity from full restoration of age-matched neural output.')
add('Afferent survival contributes to rapid neuromast repair','physiology',['phys_ganglion','phys_support'],'''
A **ganglion** is a collection of peripheral neuron cell bodies. Hardy and colleagues used targeted laser ablation to remove the posterior lateral-line ganglion and compared this intervention with severing its afferent nerve. The two procedures differed in whether neural regrowth could occur.

Severed nerves regenerated rapidly and produced little sustained delay in hair cell recovery. Complete ganglion ablation prevented afferent reinnervation and strongly impaired supporting-cell and hair cell regeneration over the observed interval. Neural presence therefore contributed to the usual rapid regenerative response.

During recovery, afferent terminals contacted supporting cells before many new hair cells appeared. The sensory neuron population participated in rebuilding its receptor environment rather than serving only as a passive recipient of completed receptors. Maintaining the local neural framework supported both tissue renewal and later sensory transmission.
''','The observation establishes a role for the afferent system in timely regeneration but does not identify a particular trophic molecule. Laser ganglion removal is more persistent than nerve transection because the latter leaves neuronal cell bodies available for axonal regrowth.')
add('New avian hair cells extend long basal projections','hearing',['bird_neurites','bird_otoferlin'],'''
Regenerated chicken hair cells initially differ in shape from mature receptors. Sato and colleagues found long **basal projections**, extensions from the side of the cell facing the underlying tissue, reaching toward the basement membrane during early regeneration.

MYO7A and **otoferlin**, a hair-cell-associated protein involved in synaptic release, labeled these projections. Their identity was distinguished from nearby neurites by combining hair cell markers with neurofilament labeling of afferent processes. Different markers were necessary because immature hair cells also expressed neuronal-associated tubulin.

The projections brought the nascent receptors close to withdrawn nerve endings. Afferent contacts formed near their tips before shortening shifted the synaptic region toward the cell body. Receptor repair therefore included a changing geometry that connected distant cell bodies and nerve terminals during the earliest stage of reinnervation.
''','The anatomy was resolved with several immunolabels rather than assigning every tubulin-positive extension to a neuron. Projections were prominent from approximately day five onward. Their contraction accompanied later cytomorphological maturation.')
add('Returning afferents contact projection tips','hearing',['bird_innervation'],'''
**Reinnervation** is the restoration of neural contacts with a tissue after their loss. Sato and colleagues followed neurofilament-labeled auditory afferents as they returned to the regenerated chicken basilar papilla. Nerve endings initially remained near the basement membrane after receptor loss.

Contacts with hair cell projections appeared during the first regeneration week, followed by larger cup-like neural thickenings around days 9–14. By four weeks, the contacts had become smaller and more similar to those in undamaged tissue. Otoferlin labeling identified the receptor side of the emerging interface.

Projection-tip contact allowed neural communication to develop before the receptor acquired its mature compact shape. Continued afferent growth and projection contraction changed the distance between the synapse and the hair cell nucleus. Reinnervation therefore progressed through a temporary elongated arrangement before returning toward the mature epithelial organization.
''','The source used NF200 to distinguish afferent neurites from tubulin-positive nascent hair cell projections. It found innervation across the length of the sensory organ. Contact geometry and overall receptor morphology matured on overlapping but distinct schedules.')
add('Presynaptic and postsynaptic specializations reunite','hearing',['bird_ribbons'],'''
A synapse has a **presynaptic** sending side and a **postsynaptic** receiving side. Sato and colleagues labeled presynaptic CTBP2 ribbon puncta in hair cells and **PSD95**, a postsynaptic scaffolding protein, in auditory nerve endings during regeneration.

PSD95 organizes proteins near the receiving membrane and is associated with AMPA-type glutamate receptors. These receptors respond to glutamate and mediate excitatory transmission. From approximately day six, PSD95-positive neural endings associated with CTBP2-positive puncta at basal projection tips.

As the projections contracted, synaptic specializations moved closer to the hair cell bodies. Ribbon counts also approached those of controls by about two weeks. Receptor maturation thus rebuilt complementary sending and receiving structures while progressively restoring their normal position within the sensory epithelium.
''','The association is an anatomical measurement; ABR recovery separately assessed physiological output. The paper reports approximately 4.7 CTBP2 puncta per PSD95-associated structure in controls and 4.5 by day fourteen. Those counts were not used to invent a new graph.')
add('Auditory recovery continues after early synapses form','hearing',['hearing_recovery','bird_ribbons'],'''
The earliest return of auditory activity preceded complete anatomical maturation in regenerated chickens. Sato and colleagues detected no auditory brainstem thresholds during the first week after sisomicin, followed by initial responses around days 9–11.

During this interval, new hair bundles and synaptic contacts were already developing, but basal projections were still contracting. Hearing sensitivity continued improving after these early contacts formed. **Decibels**, abbreviated dB, express sound level on a logarithmic scale; a higher threshold requires a stronger sound to evoke the response.

By five weeks, thresholds approached pre-injury values, although some animals retained shifts as large as about 20 dB. The extended recovery joined progressive bundle maturation, afferent reconnection, and synaptic refinement. Detectable hearing returned before every animal recovered its original sensitivity, separating onset of function from completion of sensory repair.
''','Average residual shifts varied with frequency, and the paper reports a 6.3–18.5 dB range across the tested conditions. The experiment controlled input from the opposite ear. Thresholds were measured independently of the anatomical labeling time course.')
add('Early vestibular afferents can remain electrically silent','afferent',['canal_early','canal_terminals'],'''
Boyle and colleagues recorded **primary vestibular afferents**, the neurons directly innervating vestibular hair cells, after streptomycin injury in chicks. They mechanically indented the anterior semicircular canal to produce a controlled input resembling canal stimulation during rotation.

At 14–18 days after treatment, many fibers were silent or had low spontaneous firing. Some anatomically labeled fibers entered the sensory epithelium while the receptor population remained incomplete. Responsive fibers often produced only weak changes during mechanical stimulation.

Neural endings provided a framework for reconnection before normal sensory coding returned. Functional receptors and effective synaptic communication were required for strong motion responses. Their firing properties recovered later than the anatomical appearance of nerve processes.
''','The recording and intracellular labeling experiments assessed both discharge and terminal morphology. The animals received streptomycin over five days. Silent fibers and weakly responsive fibers were distinct observations within the early recovery period.')
add('Resting firing and motion sensitivity recover differently','afferent',['canal_late','canal_terminals'],'''
A vestibular afferent’s **resting discharge** is its firing without imposed motion, whereas **motion sensitivity** is the change in firing produced by sensory stimulation. Boyle and colleagues compared these properties during successive stages of avian vestibular regeneration.

By 28–34 days, more fibers were spontaneously active and mechanical responses had increased. At later intervals, many afferents produced substantial motion-driven discharge, although their resting rates and response properties remained different from controls. Recovery did not restore every neural measurement simultaneously.

The authors hypothesize that spontaneous receptor output can return before mature mechanical transduction is fully restored. Reconnection and receptor maturation therefore affect different aspects of sensory coding at different times. A neuron that fires at rest may still transmit a weak or altered response when the animal moves its head.
''','The source followed late recovery through roughly 38–58 days after treatment. It measured canal indentation responses in impulses per micrometer, rather than assuming that resting activity represented normal sensitivity. The spontaneous-before-transduction explanation is explicitly a hypothesis.')
add('Vestibuloocular gain returns over several recovery weeks','reflex',['reflex_gains','reflex_anatomy'],'''
Carey and colleagues measured the vestibuloocular reflex repeatedly after streptomycin treatment in chicks. Reflex gain was nearly zero during the first week, when vestibular hair cell density was greatly reduced. Eye movement therefore provided an integrated functional endpoint beyond histological cell counts.

Gain and phase improved during subsequent weeks as the hair cell population recovered. By approximately 8–9 weeks, the reflex measurements approached normal values while receptor subtype recovery remained incomplete. The recovery interval was longer than the earliest appearance of replacement hair bundles.

**Type I hair cells** have a flask-like form and receive enclosing calyx endings; **type II hair cells** receive smaller bouton contacts. Reflex recovery correlated more closely with restoration of type I cells than type II cells, connecting receptor subtype composition with the return of coordinated eye movement during head motion.
''','A calyx is an expanded neural ending surrounding the hair cell, whereas boutons are localized terminals. The paper measured the horizontal VOR and vestibular cell populations. Correlation with type I density is not an independent selective manipulation of that receptor subtype.')
add('Bundle appearance alone does not predict reflex recovery','reflex',['reflex_early','reflex_anatomy'],'''
New hair bundles can appear before a vestibular system regains normal functional output. Carey and colleagues compared scanning electron microscopy with eye-movement measurements in regenerating chicks. Receptor density and bundle morphology were evaluated alongside VOR gain and phase.

At early recovery times, animals with similar-looking bundles could retain different reflex responses. The mechanically sensitive surface was therefore only one component of the repaired interface. Effective output also depended on the receptor’s synaptic contacts and the neural pathway carrying signals to eye-movement circuitry.

Rebuilding the vestibular epithelium produced progressively better gaze compensation over weeks. Anatomical replacement and integrated reflex function followed related but nonidentical trajectories. The difference makes receptor abundance, bundle maturation, and evoked behavioral output complementary measurements of recovery rather than interchangeable definitions of a restored vestibular system.
''','This limitation changes the conclusion and is retained explicitly in the teaching material. The study measured reflex function directly rather than treating normal-looking bundles as sufficient. Central compensation may contribute, but the source does not isolate it as the sole recovery mechanism.')
add('Head stabilization returns before accurate navigation','posture',['posture_behavior','posture_histology'],'''
Dickman and Lim followed adult pigeons after extensive vestibular hair cell loss. **Head stabilization** is control of head position during movement, while **orientation** includes maintaining an appropriate direction of travel. Before injury, birds were trained to traverse a straight chamber and obtain a reward.

After treatment, the pigeons developed tremors, circling, staggering, and disrupted head movement. During recovery, head shaking declined and normal head-bobbing patterns returned before accurate directed walking had fully recovered. Different components of movement control therefore improved at different stages.

By about four weeks, birds could take directed steps but remained inaccurate. The sequence linked renewed vestibular input with restoration of postural control before complete navigational performance. Repair of the sensory periphery supported a gradual reconstruction of coordinated behavior rather than an immediate return of every movement function.
''','Head bobbing contains phases of relative head stability during walking and phases of movement to a new position. The original study assessed successful trials, steps, lane changes, saccades, bobs, and shakes. Tissue recovery and behavioral recovery were complementary endpoints.')
add('Behavioral recovery extends beyond early receptor return','posture',['posture_behavior','posture_histology'],'''
Vestibular regeneration in adult pigeons unfolded over many weeks. Dickman and Lim found severe behavioral dysfunction at day seven after injury and persistent abnormalities through the first month. Sensory repair was therefore accompanied by a prolonged period of impaired movement.

Most walking trials were successful by approximately day 49, while performance approached baseline around day 70. **Latency**, the time required to complete the task, decreased as coordinated locomotion recovered. Steps and lane changes also moved toward the pre-injury pattern.

Successful release from a lesion’s behavioral consequences required more than the first appearance of new receptors. Head stability, orientation, and locomotor accuracy recovered along different trajectories as the sensory interface and its use in movement matured. Hearing thresholds, afferent responses, reflexes, and whole-animal behavior each locate a different stage of functional restoration.
''','Walking accuracy measures coordinated locomotion, whereas head stability measures control of posture during movement. These endpoints recovered on different time courses after vestibular injury. Baseline training supplied a within-animal behavioral reference.')
assert len(S)==44,len(S)
items=[{'lead':'Sensory transduction','text':'Hair bundle displacement activates receptors, transmitter release drives afferents, and restored output must be measured functionally.'},{'lead':'Supporting-cell plasticity','text':'Lateral-line proliferation and crista transdifferentiation are distinct routes; precursor-pool expansion can precede conversion.'},{'lead':'Regulatory competence','text':'Accessible Atoh1 enhancers permit a hair cell program that neighboring-cell signals can still repress.'},{'lead':'Avian injury signaling','text':'F2RL1, metalloprotease, EGFR, and ERK activity contribute to the proliferative response and production of replacement receptors.'},{'lead':'Synaptic reintegration','text':'Replacement receptors rebuild ribbon contacts and afferent communication while their geometry and physiological responses mature.'},{'lead':'Recovery criteria','text':'Cell counts, afferent firing, hearing thresholds, vestibular reflexes, and coordinated behavior recover on different time courses.'}]
for z in S:
 if z['layout']=='figures-right':z.update(figure_arrangement='side-by-side',primary_figure_width=3.9)
spec={'lecture':73,'content_slides':44,'theme':'pewter-paper','title_height':2.7,'title_min_pt':22,'title_image':fig('fish_animal'),'title_refs':[R['fish_genes']['reference']],'slides':S,'takeaways':{'items':items,'cite':'; '.join(short(k) for k in ['hearing','fish_direct','enhancers','posture']),'refs':[v['reference'] for v in R.values()]}}
(B/'lecture.json').write_text(json.dumps(spec,indent=2,ensure_ascii=False)+'\n')
print('Slides:',len(S),'words:',min(len(' '.join(z['body']).split()) for z in S),max(len(' '.join(z['body']).split()) for z in S))
