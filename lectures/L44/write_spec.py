"""Source-grounded Lecture 44; all scientific images are original PDF crops."""
from pathlib import Path
import json,re
ROOT=Path(__file__).parent
R={
'S':"Sur, M., Garraghty, P. E., & Roe, A. W. (1988). Experimentally Induced Visual Projections into Auditory Thalamus and Cortex. Science, 242(4884), 1437–1441. https://doi.org/10.1126/science.2462279",
'R':"Roe, A. W., Pallas, S. L., Kwon, Y. H., & Sur, M. (1992). Visual projections routed to the auditory pathway in ferrets: receptive fields of visual neurons in primary auditory cortex. Journal of Neuroscience, 12(9), 3651–3664. https://doi.org/10.1523/JNEUROSCI.12-09-03651.1992",
'A':"Angelucci, A., Clascá, F., Bricolo, E., Cramer, K. S., & Sur, M. (1997). Experimentally Induced Retinal Projections to the Ferret Auditory Thalamus: Development of Clustered Eye-Specific Patterns in a Novel Target. Journal of Neuroscience, 17(6), 2040–2055. https://doi.org/10.1523/JNEUROSCI.17-06-02040.1997",
'H':"Sharma, J., Angelucci, A., & Sur, M. (2000). Induction of visual orientation modules in auditory cortex. Nature, 404, 841–847. https://doi.org/10.1038/35009043",
'M':"von Melchner, L., Pallas, S. L., & Sur, M. (2000). Visual behaviour mediated by retinal projections directed to the auditory pathway. Nature, 404, 871–876. https://doi.org/10.1038/35009102",
'C':"Chapman, B., & Stryker, M. P. (1993). Development of orientation selectivity in ferret visual cortex and effects of deprivation. Journal of Neuroscience, 13(12), 5251–5262. https://doi.org/10.1523/JNEUROSCI.13-12-05251.1993"}
short={'S':'Sur et al. (1988)','R':'Roe et al. (1992)','A':'Angelucci et al. (1997)','H':'Sharma et al. (2000)','M':'von Melchner et al. (2000)','C':'Chapman & Stryker (1993)'}
F={}
def fig(k,src,num,desc):F[k]={'path':'figures/'+k+'.png','kind':'article','caption':f'{short[src].replace(" et al.", "").replace(" & Stryker", " & Stryker")}, Fig. {num}. {desc}','source_url':R[src].split()[-1]}
fig('sur1','S','1','Normal and neonatally rewired sensory pathways.')
fig('sur2','S','2','Retinal terminals and cortical tracer labeling in auditory thalamus.')
fig('sur3','S','3(A–D)','Optic-chiasm latencies and retinal ganglion-cell sizes.')
fig('sur4','S','4(A–B)','Visual receptive fields in normal visual and rewired auditory cortex.')
fig('s1main','H','1(A–L)','Orientation domains, preference maps and spatial periodicity.')
fig('s1bottom','H','1(M–O)','Tuning strength, domain area and map periodicity.')
fig('brain_locations','H','1(A,G)','Locations of imaged auditory and visual cortex.')
fig('s1maps','H','1(C–D,I–J)','Orientation preferences and tuning magnitude in A1 and V1.')
fig('s2ab','H','2(a–b)','Auditory cortical anatomy, orientation maps and single-cell tuning.')
fig('s2a','H','2(a)','Primary auditory cortex and anterior auditory field.')
fig('s2cd','H','2(c–d)','Orientation and direction selectivity distributions.')
fig('s3','H','3(a–g)','Horizontal connection fields in normal V1, normal A1 and rewired A1.')
fig('s4','H','4(a–b)','Tracer-labeled cells aligned with matching orientation domains.')
fig('s5','H','5(a–d)','Periodicity of horizontal connection fields.')
fig('m1','M','1(a–b)','Rewired pathway and modality-choice apparatus.')
fig('m2','M','2(a–d)','Modality choices before and after thalamic and cortical lesions.')
fig('m3','M','3(a–d)','Grating-detection task, contrast sensitivity and spatial resolution.')
fig('a1','A','1(A–F)','Retinal terminal clusters within subdivisions of auditory thalamus.')
fig('a6','A','6(A–B)','Adjacent, partly segregated terminals from the two eyes.')
fig('a8','A','8(A–E)','Postnatal refinement of retinal projections in auditory thalamus.')
fig('a10','A','10(A–D)','Eye-specific segregation between postnatal days 6 and 27.')
fig('a11color','A','11(A–B)','Original optical-density maps at P8 and adulthood.')
fig('a12','A','12(A–C)','Published summary of afferent patterns and target organization.')
fig('c2','C','2','Development of visual cortical orientation selectivity.')
fig('c6','C','6','Activity blockade and binocular deprivation compared with normal development.')
fig('r2','R','2(A–C)','Receptive-field diameters and positions in A1 and V1.')
fig('r4','R','4','Ocular dominance in rewired A1 and normal V1.')
fig('r5','R','5','Simple, complex and nonoriented receptive-field classes.')
fig('r8','R','8(A–B)','Orientation selectivity and tuning-width distributions.')
fig('r9','R','9','Direction selectivity in rewired A1 and normal V1.')
fig('r10upper','R','10(A, examples 1–3)','Responses to moving bars at different velocities.')
PHOTO={'path':'photos/ferret_walk.jpg','kind':'web','caption':'Photo: Domestic ferret walking.','credit':'Kyte / Wikimedia Commons','license':'CC0 1.0','source_url':'https://commons.wikimedia.org/wiki/File:Mustela_putorius_furo_walk.jpg'}
for k in ['r4','r5','r8','c6','s5']:F[k]['path']='figures/'+k+'_final.png'
F['r2']['path']='figures/r2_ab.png'
F['r2']['caption']=F['r2']['caption'].replace('(A–C)','(A–B)')
F['c6']['path']='figures/c6_complete.png'
slides=[]
def add(title,src,images,body,extra):
 paras=body.strip().split('\n\n'); refs=[R[x] for x in src];cite='; '.join(short[x] for x in src)
 s={'title':title,'body':paras,'cite':cite,'refs':refs,'transcript':[paras[0],[paras[1],[extra]],paras[2]],'figure_width':6.0}
 fs=[PHOTO if k=='photo' else F[k] for k in images]
 for f in fs:
  for ref in R.values():
   if ref.endswith(f['source_url']) and ref not in s['refs']:s['refs'].append(ref)
 if len(fs)==1:s.update(layout='figure-right',figure=fs[0])
 else:s.update(layout='figures-right',figures=fs,primary_figure_height=3.15)
 slides.append(s)
add('Neonatal inputs can change cortical sensory function','SM',['photo'],'''
Domestic ferrets, _Mustela putorius furo_, are born with immature retinal projections. **Developmental plasticity** is the capacity of growing neural connections to change their targets or organization. Sur and colleagues redirected retinal input shortly after birth, then examined the animals after they matured.

The intervention combined removal of normal visual targets with removal of ascending input to an auditory target. Retinal axons consequently entered a pathway that ordinarily carries sound, rather than being surgically attached directly to cortex.

Later behavioral experiments used 300-ms light presentations and separate rewards for light and sound. Rewired ferrets treated light reaching the altered pathway as visual. The finding concerns development after neonatal surgery; it does not establish comparable rewiring in an intact adult brain.
''','The retina-to-auditory projection developed over time after lesions; the experiment did not transplant visual cortex or connect a cable between two mature brain areas.')
add('Normal visual and auditory routes use different relays','S',['sur1'],'''
A **sensory relay** is a neuronal station that receives input and sends it onward. Retinal ganglion cells, the output neurons of the retina, normally project to the lateral geniculate nucleus, or **LGN**, and to the superior colliculus, a midbrain visual target.

The **medial geniculate nucleus**, or MGN, is the auditory thalamic relay. It normally receives ascending auditory input from the inferior colliculus and projects to primary auditory cortex, **A1**. Primary visual cortex, **V1**, normally receives its major thalamic visual input from the LGN.

Sur and colleagues compared normal pathways with pathways altered at birth and examined physiological responses in adulthood. Retinal labeling occupied up to one-third of the MGN in operated animals. An anatomical projection identifies a possible route; recordings are required to establish whether that route transmits visual signals.
''','The published pathway diagram is a crop from the original Science paper. The normal MGN-to-A1 link remained available to relay the new retinal input.')
add('Early lesions create access to an auditory target','SA',['sur1','a11color'],'''
**Deafferentation** means removing incoming axons from a target. In newborn ferrets, the researchers reduced normal retinal target space and deafferented auditory thalamus. Cutting the brachium of the inferior colliculus interrupted ascending auditory fibers; superior-colliculus ablation reduced a major retinal target.

In the original preparation, removal of visual cortical areas also caused severe LGN shrinkage through retrograde degeneration, the loss of neurons after their downstream target is removed. Sur and colleagues recorded adult animals whose novel retinal terminals could occupy up to one-third of the MGN.

The later developmental study traced the new projection from postnatal day 4 onward. Retinal invasion followed the lesion, rather than merely preserving a substantial normal retinal projection to MGN. These experiments alter target availability and input competition together; they do not isolate a single molecular guidance signal.
''','Surgery changes several features of the developing pathway simultaneously. A proposed trophic attraction is compatible with the anatomy but was not directly measured in these studies.')
add('Tracing connects retinal terminals to the cortical relay','S',['sur2'],'''
An **anterograde tracer** labels axons from their origin toward their terminals. Intraocular tracer injections in operated ferrets labeled retinal projections within auditory thalamus as well as surviving visual targets. The ectopic projection occupied patches in dorsal and ventral MGN subdivisions.

A **retrograde tracer** travels from terminals toward neuronal cell bodies. Restricted injections into A1 labeled MGN neurons, including neurons in regions overlapped by retinal terminals. The original anatomical panels retain 0.5-mm and 2-mm scale bars, linking thalamic sections to the cortical injection location.

Combining these directions of tracing supports a retina–MGN–A1 route. It does not establish that every labeled retinal terminal makes a functional synapse onto every labeled relay neuron. Electrical stimulation and visually evoked recordings supply the complementary physiological evidence for transmission through the altered pathway.
''','The retinal label and cortical retrograde label answer different anatomical questions: where retinal axons end and which thalamic neurons project to A1.')
add('Auditory thalamic neurons become visually responsive','S',['sur3','sur2'],'''
Sur and colleagues recorded individual neurons in the MGN of adult operated ferrets. Electrical stimulation at the **optic chiasm**, where retinal axons cross between the eyes and brain, tested whether retinal output could evoke spikes in this normally auditory relay.

MGN neurons responded to large flashing or moving spots of light. Their receptive fields, the regions of visual space capable of changing a neuron's firing, were generally circular and could respond to light onset, offset, or both. Orientation selectivity was uncommon at this thalamic stage.

Optic-chiasm responses occurred with a mean latency of 4.8 ms in operated MGN. Normal LGN responses averaged 2.0 ms in the comparison population. The light responses establish functional visual input, while the latency difference also indicates that the new route does not reproduce all properties of the normal visual relay.
''',"A receptive field is defined by the relationship between stimulus location and firing, rather than by the physical location of the neuron's cell body.")
add('The rerouted retinal input conducts more slowly','S',['sur3','sur2'],'''
**Conduction latency** is the delay between stimulation of an input and the recorded neuronal response. Sur and colleagues stimulated the optic chiasm and compared responses from normal LGN, operated LGN, and the newly innervated MGN under the same general recording approach.

The MGN responses in operated animals ranged from 2.8 to 11.0 ms, with a mean of 4.8 ms. Normal LGN responses ranged from 1.5 to 3.0 ms. Retrograde labeling also associated the novel projection mainly with small retinal ganglion-cell bodies.

The latency and anatomy are consistent with recruitment of a slower retinal pathway, commonly associated with W-type ganglion cells. W cells are a heterogeneous retinal class, rather than a single universal morphological category. The authors explicitly left open whether some novel-projecting neurons were other classes affected by development; conduction delay alone cannot identify a cell type conclusively.
''','Small ganglion-cell bodies and long latencies converge on a W-like interpretation, but the original paper did not use a modern molecular marker to identify the recruited neurons.')
add('Visual input acquires cortical receptive-field structure','S',['sur4','sur2'],'''
In operated ferrets, visually driven neurons were recorded in A1, downstream of the altered MGN. Responses were strongest in middle cortical layers, at recording depths of approximately 600–900 µm. Cortex therefore transformed input that had entered through an auditory thalamic relay.

Some A1 neurons responded preferentially to a bar with a particular orientation. Others preferred motion in one direction. In the original recordings, oriented receptive fields had overlapping light-on and light-off responses, a feature associated with **complex cells** in normal visual cortex.

The visual receptive fields could be much larger than those of normal V1 neurons, with scales of several degrees of visual angle. Visual selectivity and receptive-field size therefore changed differently: a nonvisual cortical target could develop visual feature selectivity without becoming an exact physiological copy of V1.
''','Light-on and light-off responses refer to firing after increases or decreases in local luminance. Their spatial arrangement distinguishes different cortical receptive-field organizations.')
add('Rewired cortical fields cover more visual space','R',['r2','brain_locations'],'''
Roe and colleagues mapped visual receptive fields in adult rewired A1 and compared them with fields in normal V1. Receptive-field diameter was defined from the average of field width and height, expressed in degrees of visual angle rather than millimeters of cortex.

The reported mean diameter was 10.9° in A1 and 3.9° in V1. A1 recordings also included more peripheral visual-field locations. **Eccentricity** is distance from the center of gaze; peripheral neurons often have larger fields, making it an important comparison variable.

Larger fields persisted when the authors restricted comparisons to overlapping eccentricities. The difference therefore could not be explained simply by sampling farther from central vision. Field size places a constraint on spatial precision, although a neuronal receptive-field measurement is not itself a behavioral acuity threshold.
''','The eccentricity control prevents a sampling difference from being mistaken for an intrinsic difference between A1 and V1.')
add('Simple and complex visual cells arise in auditory cortex','R',['r5','brain_locations'],'''
Roe and colleagues classified responsive cortical neurons by the spatial organization of their visual receptive fields. **Simple cells** contain separated subregions responding to light onset or offset. **Complex cells** respond to the appropriate orientation across overlapping onset and offset regions.

The researchers used flashed and moving bars, varying position and contrast, to distinguish these classes in rewired A1 and normal V1. The characterized populations in both areas contained roughly half complex cells, one-quarter simple cells, and one-quarter nonoriented cells.

Rewired A1 responses were generally weaker and less consistent, so only sufficiently responsive neurons could be fully classified. The similarity among characterized cells supports shared cortical transformations of visual input. It does not establish that every neuron in the two cortical areas belongs to the same functional population or that the sampling captured their complete cell-class composition.
''','Nonoriented cells respond without a clear preferred bar angle. The paper treated the classification proportions as properties of the characterized sample, not an unbiased census of all cortical neurons.')
add('Orientation tuning can emerge outside visual cortex','R',['r8','brain_locations'],'''
**Orientation selectivity** is preferential firing for a stimulus angle, such as a horizontal rather than vertical bar. Roe and colleagues moved bars through each receptive field at several orientations and compared the resulting tuning in rewired A1 with normal V1.

The distributions included strongly tuned, weakly tuned, and nonoriented cells in both regions. Mean tuning widths were approximately 65.3° in A1 and 72.3° in V1. A tuning width describes how broadly a neuron responds around its preferred angle; it differs from receptive-field diameter.

The measured distributions did not reveal a clear separation between the two areas in orientation tuning. This supports the ability of auditory cortex to develop a visual feature preference. It does not prove that the same synaptic wiring, inhibitory mechanisms, or developmental sequence generated the preference in both regions.
''','Roe used a response-ratio selectivity measure, whereas Sharma later used vector-based indices. Their numerical scales should not be treated as interchangeable.')
add('Motion direction is distinct from bar orientation','R',['r9','brain_locations'],'''
**Direction selectivity** means that a neuron responds differently when the same stimulus moves in opposite directions. A cell can prefer a horizontal bar yet respond equally to upward and downward movement, separating its orientation preference from its motion-direction preference.

Roe and colleagues swept optimally oriented bars in opposite directions and compared response ratios in rewired A1 and normal V1. Their direction-selectivity distributions overlapped, with mean indices of approximately 0.45 in A1 and 0.36 in V1 on the study's response-ratio scale.

These responses add a second emergent visual property to orientation tuning. The altered thalamic input could support cortical sensitivity to the order in which a moving stimulus activates space. The recordings did not selectively block a direction-generating circuit and therefore did not identify which feedforward or intracortical connections caused the preference.
''','The stimulus angle remains fixed when testing opposite motion directions. Changing both angle and direction would confound two distinct tuning properties.')
add('Eye preference survives the change in cortical target','R',['r4','brain_locations'],'''
**Ocular dominance** is the relative influence of the two eyes on a cortical neuron's response. Roe and colleagues stimulated each eye separately and used binocular stimulation to classify cells in rewired A1 and normal V1 on a seven-category scale.

In A1, approximately 66% of characterized visual cells were driven only by the contralateral eye, the eye opposite the recorded hemisphere. Approximately 30% had binocular contributions. The overall distribution resembled the contralateral bias found in normal ferret V1 under the same comparison.

The novel auditory route therefore preserved information about eye of origin while reaching a different cortical target. Similar ocular-dominance distributions do not imply that MGN developed the eye-specific cellular layers of LGN. Eye preference measured in cortex and laminar anatomy measured in thalamus are separate levels of organization.
''','A binocular contribution means that either eye can influence the cell; it does not establish stereoscopic depth perception in the animal.')
add('New retinal projections refine over postnatal weeks','A',['a8'],'''
Angelucci and colleagues traced retinal projections at successive postnatal ages to distinguish initial invasion from later refinement. **Axon arbors** are terminal branch systems through which an axon distributes contacts within a target. In rewired MGN, early axons were widespread and only sparsely branched.

The projection remained diffuse during the first postnatal week. A tendency to cluster appeared around P8, meaning postnatal day 8. By P22–P27, retinal terminals were largely concentrated in restricted regions, and the overall pattern approached that found in adults.

Normal controls lacked a comparable retinal terminal projection within MGN. The new organization consequently developed after surgery rather than reflecting maintenance of an abundant normal pathway. This age series records structural change across animals; it does not follow a single labeled axon continuously throughout all four weeks.
''','The developmental sampling provides an ordered anatomical sequence, but it is not time-lapse microscopy of the same arbor.')
add('Inputs from the two eyes segregate in a novel relay','A',['a10'],'''
**Eye-specific segregation** is the spatial separation of terminal fields from the two eyes. Angelucci and colleagues labeled each eye with a different tracer and reconstructed the retinal terminations in rewired MGN at several postnatal ages.

At P6, projections from the two eyes overlapped extensively. Overlap remained at P14 even as clustering began. By P22–P27, adjacent terminal regions were increasingly segregated according to eye of origin, despite the target being auditory rather than visual thalamus.

The timing broadly resembled refinement in the normal retinal pathway and supports an influence carried by the incoming afferents, the axons entering a target. It does not isolate activity as the only cause: this experiment did not independently suppress retinal correlations while preserving growth, guidance cues, and target physiology.
''','Tracer color identifies the eye of origin in the published reconstruction. The separation of those labels is an anatomical observation, not a direct recording of synchronized activity.')
add('Growing thalamus and growing retinal territory differ','A',['a11color'],'''
Angelucci and colleagues quantified the area of MGN and the territory occupied by retinal terminals. The published optical-density maps encode tracer intensity, a measure of labeling, rather than directly measuring firing rate or synaptic strength in the relay.

Mean MGN area increased approximately 7.7-fold between P4 and adulthood. Retinal projection area increased approximately 3.5-fold over the same interval. After the third postnatal week, the nucleus continued growing while the labeled retinal territory changed much less.

The fraction of MGN occupied by retinal input consequently decreased even though the novel projection persisted. Clustering increased approximately sevenfold by the end of the third week. Development thus involved both target growth and redistribution of terminals; a smaller relative projection fraction need not mean proportional loss of all functional retinal connections.
''',"The source's color maps are unmodified PDF panels. Their color scale is normalized optical density and must not be interpreted as a calcium-activity map.")
add('Target structure constrains the new retinal pattern','A',['a12','a11color'],'''
The ventral MGN contains **fibrodendritic laminae**, aligned arrangements of fibers and relay-cell dendrites. Angelucci and colleagues found that retinal terminal clusters in the new auditory target were oriented within its existing cellular organization rather than creating the eye-specific layers typical of LGN.

In the coronal plane, ventral-MGN clusters averaged approximately 61 µm along the mediolateral axis and 151 µm along the dorsoventral axis. Their elongation matched the target's organized dendritic fields. Normal and rewired MGN remained comparable in overall cellular architecture.

The incoming axons contributed eye-specific segregation, while the target constrained cluster geometry. This combination supports neither a fully predetermined cortical system nor an unconstrained blank slate. The relationship between arbor shape and dendrites is anatomical evidence; it does not prove that a particular dendritic molecule instructed each terminal's position.
''',"The published Figure 12 is the authors' summary drawing, cropped directly from the paper. The supporting measured terminal sizes and histological observations come from their anatomical results.")
add('Eye-specific clusters do not create a visual thalamus','A',['a6','a11color'],'''
Angelucci and colleagues compared terminal patterning with the cellular organization of the new target. Retinal inputs in adult rewired MGN formed clusters from the two eyes that were often adjacent but partly separated, rather than the continuous eye-specific layers of normal LGN.

Coronal reconstructions retained distinct MGN subdivisions and spatially restricted terminal patches. The published sections and reconstructions use scale bars of hundreds of micrometers, allowing the terminal arrangement to be related to the size and subdivisions of the auditory relay.

This distinction separates afferent identity from target identity. Retinal axons can preserve properties associated with their source while adapting their final distribution to a different target. The authors did not find that the MGN transformed wholesale into LGN, even though the novel route was capable of delivering visual signals to cortex.
''','Cellular architecture and input distribution are different measurements. Eye-specific input segregation can coexist with an auditory-type arrangement of relay neurons.')
add('Rewired A1 develops an orientation preference map','H',['s1main'],'''
An **orientation map** is the spatial arrangement of preferred stimulus angles across cortex. Sharma and colleagues imaged adult ferrets after retinal inputs had been redirected neonatally, comparing rewired A1 with normal V1 under binocular grating stimulation.

Gratings are repeated light and dark bars. The principal stimulus had a spatial frequency of 0.375 cycle per degree and drifted at 1.0 Hz. Different grating orientations activated different cortical domains, groups of neighboring neurons with a shared stimulus preference.

Rewired A1 contained organized orientation domains and locations where preferences changed around a common center. Normal A1 controls produced no comparable visually driven intrinsic signal over the tested stimulus range. An orientation map therefore emerged in the altered cortical target, although its spatial arrangement was less regular than the map in V1.
''','A spatial frequency of 0.375 cycle per degree describes visual pattern spacing; the drift frequency of 1.0 Hz describes how frequently the pattern advances through one full cycle.')
add('Optical imaging measures local population responses','H',['s1main'],'''
**Intrinsic-signal imaging** detects stimulus-related changes in light reflected from cortical tissue. These signals reflect local activity-related physiological changes and pool responses over a region; they are not direct measurements of every action potential in an individual neuron.

Sharma and colleagues presented gratings at four or eight orientations and compared responses across cortical locations. Darker regions in each single-orientation panel correspond to stronger responses to that stimulus. The 0.5-mm scale bars locate these response domains within the exposed cortical surface.

Combining the orientation conditions yielded a map of preference rather than a map of general visual responsiveness alone. Because imaging can be influenced by vascular anatomy, the researchers also recorded individual neurons. Agreement between the two methods supported a neural interpretation of the spatially organized orientation responses.
''','Single-unit recordings test whether local cells share the preference inferred from the population signal, reducing reliance on a hemodynamic or optical measurement alone.')
add('Map color encodes preferred angle rather than firing rate','H',['s1main'],'''
Sharma and colleagues combined responses to several grating orientations using vector averaging. A **preference map** assigns a preferred angle to each cortical location. In the published color panels, the accompanying orientation key links each color to a stimulus angle.

A separate vector-magnitude map measures how strongly the location prefers one orientation over others. A region can have a defined preferred angle while its selectivity is weak. The source therefore separates the identity of the preferred stimulus from the strength of its tuning.

Both rewired A1 and normal V1 contained regions sharing a common preference. Their maps were obtained with the same 0.375-cycle-per-degree gratings, limiting stimulus differences in the comparison. Color boundaries alone cannot establish that cells on either side are connected, and anatomical tracing was required to investigate that relationship.
''','A preference map and a tuning-strength map answer different questions. The source color key remains intact; no map colors have been reassigned.')
add('Pinwheel centers are less dense in rewired A1','H',['s1main'],'''
A **pinwheel** is a cortical location around which preferred orientation changes progressively through the available stimulus angles. Sharma and colleagues identified these singularities in both normal V1 and rewired A1 from the composite preference maps.

The mean density was approximately 1.1 pinwheel centers per mm² in rewired A1 and 4.5 per mm² in normal V1. Orientation-vector magnitude was often lower near pinwheel centers, where neighboring responses represent multiple orientations within a small cortical area.

The appearance of pinwheels outside visual cortex supports substantial input-dependent organization. Their lower density also marks a limit: the same broad type of map can have different spatial geometry. Pinwheel density is a property of cortical organization and cannot by itself specify visual acuity or the strength of an individual neuron's orientation tuning.
''','The physical unit is pinwheel centers per square millimeter of cortex, rather than per degree of visual space.')
add('Orientation domains are larger in rewired cortex','H',['s1main','s1bottom'],'''
Sharma and colleagues measured the area of cortical domains responding to a single orientation. The two cortical targets were stimulated with matched gratings, and their activity maps were analyzed with the same general procedures to compare spatial organization.

Domains in rewired A1 occupied more cortical area than those in V1. In the same study, normal V1 had quasi-periodic orientation-domain spacing of about 750 µm, while the arrangement in rewired A1 was less periodic. Domain area and domain spacing describe related but distinct properties.

Larger domains do not imply sharper tuning. The preferred angle may be shared over a larger region even when individual neurons have comparable orientation selectivity. The comparison separates the organization of a population across cortical space from the width or strength of tuning measured at one location.
''','The domain-area comparison uses square millimeters of cortical surface, whereas spacing uses micrometers. Neither is the receptive-field size measured in degrees of visual angle.')
add('Map periodicity differs despite visual selectivity','H',['s1main'],'''
**Autocorrelation** measures how strongly a spatial pattern resembles itself after different displacements. Sharma and colleagues applied this analysis to orientation maps, then examined the published power spectra to compare repeating spatial structure in rewired A1 and normal V1.

Normal V1 contained a prominent spatial frequency near 1.3 cycles per mm, corresponding to its roughly 750-µm domain spacing. Rewired A1 had weaker organization away from the central, zero-displacement component, consistent with less regularly spaced orientation domains.

The source plots quantify an observed cortical pattern rather than a model curve generated for teaching. These data separate the presence of orientation selectivity from the regularity of its map. A less periodic cortical arrangement can still contain sharply tuned neurons, so orderly spacing is not a prerequisite for every form of visual feature selectivity.
''','A power spectrum here concerns variation across millimeters of cortex. It is different from the stimulus spatial frequency, which is expressed in cycles per degree of visual angle.')
add('Single neurons match their local orientation domains','H',['s2ab'],'''
After optical imaging, Sharma and colleagues recorded individual neurons in the superficial layers of rewired auditory cortex. Recording sites were registered to the cortical map so that the preferred angle of a neuron could be compared with its local population preference.

Preferred orientations generally matched the imaged domain within 22.5°. The published polar response plots preserve the relationship between stimulus angle and firing at individual recording sites. A polar plot arranges stimulus directions around a circle, rather than treating angle as a linear axis.

This correspondence links population imaging to neuronal selectivity. A colored domain is therefore supported by local spike recordings rather than only by an optical signal. Agreement does not mean every neuron in a domain has identical tuning, and the superficial recordings do not directly measure all layers or every synaptic input to the mapped region.
''','Registration used the cortical vasculature and marked recording locations. The orientation comparison depends on matching the physiological site to the correct map location.')
add('Visual firing rates overlap those in normal V1','H',['s2ab'],'''
Sharma and colleagues compared visually evoked single-neuron firing in rewired A1, the anterior auditory field, and normal V1. The **anterior auditory field**, or AF, is an adjacent cortical auditory region receiving thalamic and cortical auditory-system connections.

Under the study's grating conditions, mean response levels were approximately 13.7 spikes/s in rewired A1, 13.9 spikes/s in rewired AF, and 14.2 spikes/s in normal V1. These overlapping firing levels complement the comparison of orientation preference rather than replacing it.

A neuron can fire at a similar rate yet differ in receptive-field size, latency, or input pathway. Comparable response rates therefore do not establish that rewired auditory cortex and normal visual cortex are functionally interchangeable. They establish that the altered pathway can generate substantial visually driven cortical spiking in multiple auditory cortical regions.
''','The earlier Roe study used moving bars and reported generally weaker responses in A1. The later grating study measured different neurons and stimuli, so its rates should not erase the earlier result.')
add('Orientation selectivity strength can be comparable','H',['s2cd','s2ab'],'''
Sharma and colleagues used an **orientation selectivity index**, or OSI, to quantify the concentration of responses around a preferred angle. Their vector-based measure ranges from 0 to 1, with larger values indicating a more strongly concentrated orientation preference.

They compared the full distributions of single-cell OSI in rewired A1, rewired AF, and normal V1. The distributions overlapped substantially. A parallel analysis of imaged orientation-vector magnitude gave a similar comparison between A1 and V1 population tuning.

Agreement across single-cell and imaging measures supports comparable tuning strength under the tested conditions. It does not imply equal domain size or map periodicity: normal V1 still had more regularly arranged domains. The distinction prevents a population's spatial arrangement from being treated as the same variable as a neuron's stimulus selectivity.
''',"Sharma's 0–1 vector measure is defined differently from the response-ratio measure in Roe. Similar scientific questions can be addressed with distinct numerical indices.")
add('Direction tuning also emerges in neighboring cortex','H',['s2cd','s2ab'],'''
Sharma and colleagues measured a **direction selectivity index**, or DSI, from responses to gratings moving in opposite directions. Their index ranges from 0 to 1 and distinguishes the direction of motion from the orientation of the grating's bars.

The DSI distributions in rewired A1 and AF overlapped those in normal V1. Thus, visual responses in both altered auditory areas included preferences for motion direction, as well as the orientation preferences encoded by their cortical maps.

Orientation and direction tuning are emergent response properties, but their measurement alone does not identify the underlying circuit. This experiment combined imaging with spike recordings; it did not selectively manipulate inhibition, recurrent excitation, or individual thalamic inputs. Equivalent index distributions therefore support similar response selectivity without establishing an identical mechanism across all three cortical regions.
''','A vertical grating can move left or right. Direction tests compare those opposite movements while holding the bar orientation constant.')
add('Visual maps extend into the anterior auditory field','H',['s2ab'],'''
Sharma and colleagues imaged a cortical region spanning A1 and AF, then recorded neurons in both fields. AF normally belongs to the auditory cortical system; the experiment tested whether the visual input's influence was restricted to primary auditory cortex.

Both fields contained orientation domains and visually responsive neurons. Their mean visual response levels were near 14 spikes/s under the grating conditions. A dense vascular band at the approximate A1–AF boundary disrupted the optical signal, so the map's visible discontinuity could not be interpreted simply as a functional absence.

The findings establish visual processing across more than one auditory cortical area after early rerouting. Existing thalamocortical and corticocortical pathways could contribute to that distribution. The study did not isolate the relative contribution of direct visual input through auditory thalamus versus input relayed between A1 and AF.
''','The vascular boundary is a measurement limitation in intrinsic-signal imaging. Single-neuron recordings helped establish visual selectivity within each cortical field.')
add('Tracing tests the organization of horizontal connections','H',['s3','brain_locations'],'''
**Horizontal connections** link neurons across the cortical surface within an area. Sharma and colleagues made focal injections of cholera toxin subunit B, **CTB**, into superficial cortex to identify neurons whose axons reached the injection site.

The tracer was injected approximately 250–300 µm below the cortical surface. After transport, tangential tissue sections were used to reconstruct the spatial distribution of labeled neurons in normal V1, normal A1, and rewired A1. Published color maps represent labeled cell density in cells per mm².

This approach measures connection-field organization rather than stimulus preference directly. It permits a comparison between the functional map and a structural network capable of linking separated domains. Retrograde labeling does not reveal the strength of each synapse, its neurotransmitter, or whether the labeled connection is necessary for a particular visual response.
''','CTB identifies the neurons projecting toward the injection site. The dense local injection halo was excluded from quantitative analyses of long-range organization.')
add('Normal auditory connections form an elongated band','H',['s3','brain_locations'],'''
In normal A1, Sharma and colleagues found that labeled horizontal connections formed a broad, anisotropic band. **Anisotropy** means that a pattern extends farther along one axis than another, rather than spreading equally in all directions.

The dominant connection axis followed the anteroposterior direction associated with the isofrequency organization of auditory cortex. **Isofrequency** regions contain neurons tuned to similar sound frequencies. The normal-A1 labeled field had an average long-axis extent of approximately 3.2 mm.

This normal auditory pattern served as a control for assessing the influence of retinal input. It differed from the numerous discrete patches in normal V1. Consequently, a patchy connection field in rewired A1 could be evaluated against its usual auditory organization, rather than being assumed to be a generic consequence of injecting a tracer into any cortical area.
''',"Anteroposterior means front to back on the cortical surface. It describes the connection field's axis, not the direction in which a visual stimulus moved.")
add('Visual cortex contains multiple connection patches','H',['s3','brain_locations'],'''
In normal V1, focal CTB injections labeled multiple separated patches of neurons around the injection site. Sharma and colleagues compared these fields with normal and rewired auditory cortex using the same tracing and reconstruction procedures.

The V1 field extended primarily along the mediolateral axis, meaning toward and away from the midline, with a mean long-axis extent of approximately 4.8 mm. Labeled cells were clustered into numerous patches rather than the broad anteroposterior band typical of normal A1.

This comparison defines a visual-cortical structural pattern against which the altered auditory cortex can be assessed. A longer connection field is not inherently a better network, and patchiness alone does not identify stimulus preference. The later combination of optical maps and targeted injections tested whether separated patches preferentially linked domains with matching orientation tuning.
''','The normal V1 and normal A1 conditions distinguish area-specific organization from a common tracer artifact. The anatomical patterns were reconstructed from tangential cortical sections.')
add('Rewired A1 develops a more patchy connection field','H',['s3','brain_locations'],'''
After neonatal visual rerouting, A1 horizontal connections formed multiple labeled patches separated by more sparsely labeled cortex. Sharma and colleagues compared the altered area with both normal A1 and normal V1, separating original target organization from visual-like remodeling.

The average connection-field long axis in rewired A1 was approximately 4.0 mm, between the normal-A1 and normal-V1 values. The field was elongated mediolaterally, resembling the dominant axis in V1 rather than the anteroposterior band in normal A1.

Patch number and arrangement also shifted toward the visual pattern, but patch sizes and periodicity remained different from V1. The anatomical result therefore supports partial restructuring of the intracortical network. It does not establish a complete conversion of auditory cortex into visual cortex, and tracer distributions cannot by themselves determine how information flows during behavior.
''','The transformation affects the arrangement of cortical connections while the auditory thalamocortical route remains the input pathway. These are distinct levels of wiring.')
add('Connection patches retain an intermediate geometry','H',['s3','brain_locations'],'''
Sharma and colleagues quantified the organization of labeled horizontal connection fields after comparable focal injections. Their analyses considered patch number, patch area, aggregation, and the direction of the field's elongation rather than classifying the entire cortex with a single label.

Rewired A1 and normal V1 each produced approximately 12 patches per injection on average, whereas normal A1 produced approximately four. Rewired-A1 patches were smaller than those in normal A1 but tended to be larger than those in V1.

This combination separates several components of circuit organization. Retinal input strongly influenced patch formation and field orientation, while other features remained intermediate. The data support developmental constraints acting alongside input-dependent change; they do not identify whether each remaining difference comes from target properties, the recruited retinal population, or the history of visual experience.
''','Similar patch counts do not establish identical connectivity. Patch size, separation, field geometry and physiological selectivity remain separate measurements.')
add('Horizontal connections favor matching orientations','H',['s4','brain_locations'],'''
Sharma and colleagues placed focal tracer injections within orientation domains identified by optical imaging. After histological reconstruction, the positions of labeled neurons were aligned with the earlier maps to compare structural connections with stimulus preference.

In both V1 and rewired A1, labeled cell patches preferentially occupied regions responsive to the injection site's orientation. The published examples use 45° stimulation in V1 and 135° stimulation in rewired A1, with 0.5-mm scale bars preserving the cortical spatial scale.

The correspondence supports selective linkage between similarly tuned regions after novel visual input reaches auditory cortex. It is stronger evidence than observing patchiness alone. Nevertheless, anatomical preference does not establish that those horizontal connections generate orientation selectivity, and the experiment did not remove the patches to test their necessity for the tuning of individual neurons.
''','The map and tracer distribution were obtained with separate techniques and aligned using anatomical landmarks. Their correspondence relates cortical function to a measured connection pattern.')
add('Horizontal connection periodicity changes only partly','H',['s5','brain_locations'],'''
Sharma and colleagues applied autocorrelation and power-spectrum analyses to the anatomical connection fields. These source analyses assess repeated spacing among labeled patches across millimeters of cortex, rather than the timing of neuronal spikes.

Normal V1 showed periodic organization along the mediolateral axis with a cycle of approximately 500–750 µm. Normal A1 had little comparable periodicity. Rewired A1 had more periodic organization than normal A1, yet less than normal V1.

The ordering of these anatomical conditions parallels the differences in functional orientation maps. Both sets of measurements support substantial but incomplete reorganization under novel visual input. Their agreement remains correlational: it does not establish that changing horizontal patch spacing alone would change the orientation map, or that map geometry determines the animal's visual percept.
''','Functional maps and anatomical connection fields were analyzed separately. Their shared intermediate organization is evidence for constrained remodeling, rather than proof of a one-way causal relationship.')
add('Normal orientation tuning matures after early responses','C',['c2','brain_locations'],'''
Chapman and Stryker recorded single neurons in normal ferret V1 at different postnatal ages. They varied moving-bar orientation to measure whether cortical firing was selectively concentrated around a preferred angle, rather than merely testing whether light could evoke any response.

Visual responses were first recorded at P23. Through postnatal week 5, only about 25% of neurons were clearly orientation selective. By week 7, approximately 75% had clear orientation tuning, approaching the adult distribution under the study's criteria.

The developmental change was not simply an increase in overall responsiveness: firing strength and selectivity were not correlated within the examined groups. The first visual response therefore precedes mature feature tuning. This normal-development comparison provides a temporal context for neonatal rewiring without establishing that rewired A1 follows precisely the same schedule.
''',"Chapman's index scale and selectivity criterion differ from Sharma's vector-based OSI. The percentages describe their study's classification and should be taught with that definition.")
add('Sodium-channel blockade prevents tuning maturation','C',['c6','brain_locations'],'''
Chapman and Stryker infused **tetrodotoxin**, or TTX, into V1 to suppress cortical activity. TTX blocks voltage-gated sodium channels, the membrane proteins whose activation permits the rapid inward sodium current underlying an action potential's rising phase.

Suppressing sodium-dependent spikes interrupts the neuronal activity available for developmental refinement. Infusion beginning in postnatal week 4 and continuing through week 7 left orientation tuning near the immature distribution. Untreated contralateral cortex and saline-treated cortex developed substantially more mature tuning.

Recordings after treatment withdrawal allowed the authors to examine persistent developmental consequences rather than merely the immediate absence of spikes under TTX. The result establishes an activity requirement during this interval. It does not identify a particular synapse, excitatory transmitter receptor, or calcium-dependent learning rule responsible for the arrested refinement.
''','The measured manipulation was broad cortical activity blockade. Specific NMDA-receptor or inhibitory-synapse mechanisms were not isolated by this TTX experiment.')
add('Visual deprivation differs from silencing the cortex','C',['c6','brain_locations'],'''
Chapman and Stryker deprived developing ferrets of normal vision by suturing both eyelids before natural eye opening. **Binocular deprivation** removes normal patterned visual experience while leaving the eyes and much spontaneous neural activity present.

By postnatal week 8 or later, deprived cortex had less mature orientation tuning than normally reared cortex. Approximately half of the recorded neurons were poorly selective, compared with approximately one-quarter in normal adults. Some deprived cells nevertheless developed strong orientation selectivity.

TTX blockade was more disruptive than lid suture, maintaining a distribution resembling much younger cortex. The comparison separates the need for neuronal activity from the need for normal visual experience. It does not establish that lid suture eliminates every visual or retinal signal, nor that spontaneous activity alone is sufficient for all aspects of cortical map development.
''','Lid closure is not equivalent to pharmacologically blocking spikes. The two preparations leave different forms of input and intrinsic activity available during development.')
add('A modality-choice task distinguishes light from sound','M',['m1'],'''
Von Melchner and colleagues trained adult ferrets to make different responses to light and sound. **Stimulus modality** is the sensory category of an input. A right reward spout was associated with light, and a left spout with auditory stimuli.

The animal initiated a trial by maintaining its muzzle in a monitored start position. Lights and sounds were presented for 300 ms. Visual training initially used only the left monocular field, the region seen through the nonrewired right hemisphere, leaving the novel projection untrained on the task.

The researchers subsequently tested light in the right visual field, which entered the rewired left hemisphere. During these probe trials, either spout was rewarded to avoid selectively teaching a particular response. This design tests generalization of a learned sensory distinction, rather than direct training of the rewired pathway's response.
''','The side of the visual stimulus and the side of the rewarded movement are different variables. Light in the left field was trained to elicit movement to the right spout.')
add('The novel pathway supports a visual choice after lesions','M',['m2','m1'],'''
Von Melchner and colleagues removed the remaining LGN and lateral posterior visual thalamic routes in the rewired hemisphere after initial behavioral training. The **lateral posterior nucleus**, or LP, is another thalamic recipient of visual input and a potential alternative route.

Following recovery, light presented in the right monocular field still elicited the response previously associated with vision. Rewired ferrets chose the visual reward spout despite the surviving route passing through MGN and auditory cortex. Responses to sound and light in other fields provided internal controls.

This preserved choice after conventional visual-thalamic lesions supports functional use of the novel pathway. Histological verification checked the lesion locations. The behavioral classification is consistent with a visual or visual-like percept; it cannot report the animal's exact subjective experience or establish that the new percept matches normal vision in every respect.
''','The late LGN/LP lesions isolated the novel route after the ferrets had matured. Neonatal rewiring and adult pathway-isolation lesions served different purposes.')
add('Auditory-cortex ablation removes the rerouted visual choice','M',['m2','m1'],'''
After isolating the rewired route, von Melchner and colleagues ablated A1 and adjacent auditory cortex in the altered hemisphere. An **ablation** removes tissue; comparing behavior before and after it tests whether that tissue is necessary under the experimental conditions.

Choices of the visual reward spout for right-field light fell toward chance after the cortical lesion. In this two-choice protocol, chance is approximately 50%. Responses to other stimuli changed much less, including light reaching the intact visual hemisphere.

The loss of the isolated visual response establishes a necessary contribution of the ablated auditory cortical territory. It is more informative than visual activation of A1 alone. Because the lesion included adjacent cortex and its connections, the experiment does not assign necessity to one cell class or distinguish local computations from pathways passing through the damaged territory.
''','Preserved responding to other stimuli reduces the likelihood that the effect was a general inability to initiate trials, move to a spout or obtain the reward.')
add('Controls separate sensory category from stimulus location','M',['m2','m1'],'''
A spatial shortcut could mimic sensory classification if a ferret always associated one stimulus location with one reward. Von Melchner and colleagues moved the unseen speaker into the right monocular field to test whether sound location changed the learned response.

The animals maintained more than 90% accuracy for these displaced sounds. A separately trained, light-only rewired animal responded at the visual spout with more than 95% accuracy for right-field light after visual-thalamic lesions. A sound-only animal turned toward right-field light without using the trained auditory spout.

Together, these controls support a distinction between the novel light input and sound, rather than simple location-based responding. Some control conditions involved individual animals, limiting broad population claims. They also do not identify how downstream motor pathways learned to interpret the developing auditory-cortical visual signal.
''',"The sound-only animal's orienting response indicates detection without the trained sound-category response. That behavior separates detection from the particular classification rule.")
add('Rewired vision detects gratings at lower spatial resolution','M',['m3'],'''
Von Melchner and colleagues measured **grating acuity**, the finest repeating light–dark pattern an animal can detect. Adult rewired ferrets compared gratings with equally bright, unpatterned screens after the remaining visual-thalamic route had been lesioned.

In animal R6, a 0.25-cycle-per-degree grating in the intact left field produced approximately 50% correct responses at 0.06 contrast. The same spatial frequency in the rewired right field was not detected even at 0.22 contrast; a coarser 0.18-cycle-per-degree pattern elicited responses.

At 0.15 contrast, monocular spatial resolution was approximately 0.5 cycle per degree in intact fields and approximately 0.15 in rewired fields. **Contrast** describes luminance modulation relative to mean luminance. The equiluminant control limits explanations based on brightness alone, while the field comparison establishes a substantial loss of spatial precision despite usable vision.
''',"Behavioral acuity depends on the full sensory and decision pathway. It cannot be read directly from a single neuron's receptive-field diameter or orientation index.")
add('Developmental reorganization preserves measurable limits','MH',['m3','s2ab'],'''
The ferret studies establish a chain from new retinal input to altered cortical organization and visually guided behavior. Rewired auditory cortex develops orientation-selective spiking and cortical domains, yet its visual acuity and map geometry differ from those of the normal visual pathway.

In a central-field task reported by von Melchner and colleagues, normal vision detected 1 cycle per degree at 0.15 contrast, whereas the rewired side detected only 0.25 cycle per degree. Sharma and colleagues likewise found orientation maps with larger domains and less regular spacing than normal V1.

The experiments support a substantial instructive influence of early sensory input within a constrained developing system. They do not establish that cortex has no intrinsic specialization, that adult cortex can undergo the same transformation, or that the exact conscious quality of rewired vision is known from reward choices.
''','Circuit plasticity is established at anatomical, physiological and behavioral levels, but each level retains limits. The behavioral experiment cannot resolve the subjective quality of the visual-like sensation.')
assert len(slides)==44,len(slides)
items=[
('Early input redirects function:','Neonatal lesions allow retinal axons to enter auditory thalamus and provide functional visual input to auditory cortex.'),
('Source and target both matter:','Eye-specific retinal clusters develop within the retained organization of MGN; the novel relay does not become an LGN.'),
('Tuning and map order differ:','Rewired A1 develops orientation and direction selectivity, while domains and horizontal connections remain less periodic than in V1.'),
('Activity supports refinement:','Cortical TTX blockade arrests orientation-tuning maturation; binocular deprivation impairs it without producing the same complete arrest.'),
('Behavior tests circuit necessity:','Visual choices survive isolation of the rerouted pathway and decline after auditory cortical ablation.'),
('Plasticity has limits:','Rewired vision has lower spatial resolution, and neonatal results do not establish equivalent adult rewiring or identical subjective perception.')]
spec={'lecture':44,'theme':'rosewood-paper','content_slides':44,'title_height':2.8,'title_image':PHOTO,'title_refs':[R['S'],R['M']],'slides':slides,'takeaways':{'items':[{'lead':a,'text':b} for a,b in items],'cite':'; '.join(short.values()),'refs':list(R.values())}}
for i,s in enumerate(slides,2):
 words=len(re.findall(r"\b[\w’'-]+\b",' '.join(s['body'])));print(i,words,s['title'])
 assert len(s['body'])==3
 assert 90<=words<=170,(i,words)
(ROOT/'lecture.json').write_text(json.dumps(spec,indent=2,ensure_ascii=False)+'\n')
(ROOT/'references.json').write_text(json.dumps(R,indent=2,ensure_ascii=False)+'\n')
