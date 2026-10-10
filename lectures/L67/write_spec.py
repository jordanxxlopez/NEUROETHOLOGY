"""Lecture 67: flamingo primary literature and unmodified source crops."""
import json,re
from pathlib import Path
B=Path(__file__).resolve().parent
R=json.loads((B/'research.json').read_text());F=json.loads((B/'figure_sources.json').read_text());S=[]
AUTH={'balance':'Chang & Ting','orexin':'Mazengenya et al.','vascular':'Holliday et al.','retina':'Lisney et al.','fields':'Martin et al.','filter':'Zweers et al.','jenkin':'Jenkin','vortices':'Ortega-Jimenez et al.','feeding':'Deville et al.','acoustic':'Mathevon','display':'Perrot et al.','friends':'Rose & Croft','juvenile':'Loader & Rose','cosmetics':'Chiale et al.'}
YEARS={'balance':2017,'orexin':2026,'vascular':2006,'retina':2020,'fields':2005,'filter':1995,'jenkin':1957,'vortices':2025,'feeding':2013,'acoustic':1997,'display':2016,'friends':2020,'juvenile':2023,'cosmetics':2021}
def short(k):return AUTH[k]+' ('+str(YEARS[k])+')'
def fig(n):
 x=F[n];return {'path':'figures/'+n+'.png','kind':'article','caption':short(x['paper'])+', Fig. '+x['figure']+'. '+x['description'],'source_url':'https://doi.org/'+R[x['paper']]['doi']}
def add(title,k,imgs,text,note):
 body=text.strip().split('\n\n');assert len(body)==3;assert len(title)<=62,title
 keys=list(dict.fromkeys([k]+[F[n]['paper'] for n in imgs]));z={'title':title,'body':body,'transcript':[re.sub(r'\*\*','',p) for p in body]+[note],'refs':[R[x]['reference'] for x in keys],'cite':'; '.join(short(x) for x in keys),'figure_width':5.8}
 if len(imgs)==1:z.update(layout='figure-right',figure=fig(imgs[0]))
 else:z.update(layout='figures-right',figures=[fig(n) for n in imgs],primary_figure_height=2.05)
 if imgs==['balance_limb','balance_setup']:z.update(figure_arrangement='side-by-side',primary_figure_width=3.8)
 if imgs==['balance_sway','balance_limb']:z.update(figure_arrangement='side-by-side',primary_figure_width=3.2)
 widths={('orexin_histology','orexin_map'):3.1,('retina_map','retina_histology'):3.3,('retina_eye','retina_map'):2.5,('bill_tongue','bill_motion'):2.6,('bill_motion','bill_tongue'):3.2,('bill_cavity','bill_buds'):3.1}
 if tuple(imgs) in widths:z.update(figure_arrangement='side-by-side',primary_figure_width=widths[tuple(imgs)])
 S.append(z)
add('A relaxed flamingo can support itself on one leg','balance',['balance_sway'],'''
Flamingos often rest with one foot on the ground and the other leg folded against the body. The standing limb must support body weight while keeping the body balanced over a relatively small contact area.

Chang and Ting combined force-platform recordings of living Chilean flamingos with manipulation of Caribbean flamingo cadavers. A **force platform** measures the forces exerted against the ground, allowing the researchers to follow how the point of support moved beneath the foot.

Quiet birds with closed eyes exhibited especially small movements of that support point. Resting on one leg therefore combines a conspicuous posture with low measured sway. The cadaver experiments identified a passive mechanical contribution that helps explain how this posture can persist without continuous large corrective movements.
''','Weight support and balance are distinct mechanical tasks. The cadaver tests address passive weight support, while the live-bird recordings characterize movement during standing. The two preparations were different flamingo species, and the living birds were juveniles.')
add('Quiet standing localizes pressure beneath the foot','balance',['balance_sway'],'''
The **center of pressure** is the point at which the resultant ground force acts under the foot. It shifts when the bird changes how its weight is distributed across the toes and the rest of the contact surface.

During quiet one-legged standing, this point remained near the joint connecting the long foot segment to the toes. In the representative quiet trial, peak movement speed was 31 mm/s. When the same bird was alert but still, the peak reached 133 mm/s.

Grooming and body shaking produced still larger excursions, with a representative peak of 362 mm/s. Activity therefore changes the mechanical demand placed on the supporting foot. Locating the ground force beneath the distal joint reduces the turning effect of that force compared with a more displaced point of application.
''','Pressure movement is expressed in millimeters per second. These three speeds belong to the representative trials in Figure 2. The location of the force matters because a force acting away from a joint has a larger turning effect.')
add('A cadaver retains a stable one-leg joint posture','balance',['balance_limb','balance_setup'],'''
A **cadaver** is a dead specimen in which muscles cannot generate active contractile force. Fully thawed Caribbean flamingo specimens were supported by clamps near the lower end of the leg, reproducing the support supplied by one standing limb.

Body weight brought the proximal joints, the joints nearest the body, into a stable configuration resembling the posture of living resting birds. Tilting the supported specimen forward and backward through approximately 119° produced relatively little change in the hip and knee angles.

The limb therefore contains a passive route for resisting the load imposed by gravity. Stability in a preparation without active contraction distinguishes this mechanical support from a continuously commanded muscular hold. The observed joint configuration depended on how the body and the supporting leg were positioned.
''','The hip connects the thigh to the body, and the knee joins the thigh and lower leg. The passive support did not require a living nervous system. Its dependence on posture means that a stable configuration can be lost when the geometry changes.')
add('Medial foot placement engages passive support','balance',['balance_limb','balance_setup'],'''
A flamingo’s one-leg stance places the supporting foot beneath the body rather than directly below the hip on the same side. **Adduction** is movement toward the body’s midline; the standing limb is adducted to achieve this medial placement.

In the cadaver experiments, a stable configuration persisted when the lower leg was inclined approximately 20° inward from vertical. Positioning the leg vertically, closer to the geometry of two-legged standing, made the proximal joints unstable under the same body load.

The support mechanism depends on alignment in more than one plane. Forward and backward tilting could be tolerated over a wide range, while sideways alignment was more restricted. Bringing the foot inward engages joint constraints that keep the body supported, linking the characteristic stance directly to functional limb geometry.
''','The sagittal plane separates left and right and contains forward-backward movement. The frontal plane contains sideways movement. The experiments found broad tolerance in the first plane and a narrower set of stable arrangements in the second.')
add('Gravity loads the hip and knee against joint constraints','balance',['balance_limb','balance_setup'],'''
The body’s **center of mass** is the effective location of its distributed mass for describing gravitational loading. In the supported flamingo posture, it lies forward of the knee, so body weight tends to extend the knee and flex the hip.

**Joint torque** is the turning effect of a force about a joint. The researchers found that anatomical limits of movement opposed the gravity-induced torques. The knee resisted extension more strongly than flexion when manipulated, giving the support a directional mechanical character.

This combination is a **gravitational stay**, a posture in which gravity itself loads a passive stabilizing arrangement. The same weight that must be supported helps engage the restraint. Moving the body’s load behind the knee changes the direction of loading and can release the stable configuration.
''','Extension straightens a joint, whereas flexion bends it. A stay apparatus is a passive support arrangement. The study established its functional behavior without identifying one single tissue as the complete mechanism.')
add('Load direction determines upright stability','balance',['balance_limb','balance_setup'],'''
The location of an applied force determines how it rotates the body around the supported joints. Chang and Ting tested this relationship by applying downward forces at different locations on cadavers already held in a one-leg stance.

A downward force applied forward of the knee produced less than 10° of additional joint movement in the reported tests. Loading the body nearer the tail instead caused backward pitching. The passive restraint therefore supported one direction of loading more effectively than the opposite direction.

This directional response explains why stable standing requires an appropriate body posture as well as correct foot placement. A limb can resist gravity in one configuration and move freely after that configuration changes. Passive support emerges from the arrangement of the body, joints, and ground contact acting together.
''','The test moved the point at which downward force acted, rather than asking a living bird to correct its posture. Backward pitching exposed the direction in which the restraint did not hold. The one-leg configuration is a mechanically specific arrangement.')
add('Two-leg geometry can release the gravitational stay','balance',['balance_limb'],'''
Adding a second supporting leg does not automatically reproduce the stable configuration found in one-legged standing. In the cadaver preparation, positioning the limbs as in a two-leg pose failed to retain the same stable proximal joint arrangement.

When the foot was no longer placed medially enough beneath the body, the hip and knee could move rather than remain constrained. The limb then behaved as linked segments with several available directions of movement, instead of as a passively supported configuration.

The comparison separates the number of ground contacts from the geometry of support. One contact can be mechanically favorable when it engages passive constraints; two contacts can require a different pattern of stabilization. The authors’ hypothesis is that one-legged posture can reduce the muscular energy needed for prolonged standing.
''','The hypothesis concerns energetic expenditure, which was not measured directly in these experiments. The demonstrated result is the contrast in passive stability between limb arrangements. The authors also distinguished this proposal from explanations centered on heat loss or muscle fatigue.')
add('Quiet balance differs from passive weight support','balance',['balance_sway','balance_limb'],'''
Passive support at the proximal joints addresses the load of the body, while balance also depends on keeping the body above the supporting foot. These mechanical demands occur together but were examined with different preparations in the study.

Living flamingos displayed tightly localized pressure trajectories when quiet. Their more active movements displaced the ground-force application point and increased its speed. The relationship connects behavioral state with the torque required at the foot and the challenge of maintaining upright posture.

The cadaver results establish that active contraction is unnecessary for the demonstrated proximal support configuration. The living recordings measured forces rather than muscle activation. Together, the findings support a hypothesis in which passive geometry reduces the muscular demands of resting, while active movement changes the stabilization required from the supporting limb.
''','Electromyography would measure muscle electrical activity directly, but it was not part of this study. Small pressure motion is compatible with low muscular demand rather than proof that every muscle is silent. This distinction changes how the force recordings should be interpreted.')
add('CT reconstruction locates flamingo head vessels','vascular',['vascular_head'],'''
**Computed tomography**, or CT, reconstructs internal anatomy from X-ray measurements collected through a specimen. Holliday and colleagues injected arteries and veins with contrasting materials, allowing the two vascular systems to be separated in scans of a Caribbean flamingo head.

**Arteries** carry blood away from the heart, while **veins** return it. Differences in the injected contrast made their paths distinguishable during digital segmentation, the process of selecting structures from the scan according to their location and image properties.

The reconstructed vessels could then be related to the brain, eye sockets, jaw, and oral cavity in three dimensions. This method preserves their spatial relationships more clearly than an isolated vessel removed by dissection. It identifies the anatomical supply routes surrounding the neural and sensory structures involved in flamingo behavior.
''','The study used differential vascular injection to distinguish vessel types. Segmentation made the vascular paths visible within the intact spatial organization of the head.')
add('Flamingo brain vessels retain a conservative avian pattern','vascular',['vascular_head'],'''
The flamingo’s specialized feeding apparatus is supplied by vessels that largely retain the general organization described in other birds. The CT study traced vascular routes through the temporal, orbital, pharyngeal, and brain regions rather than treating the bill as an isolated structure.

**Orbital** refers to the region surrounding the eye; **encephalic** refers to the brain. Differentiating arteries and veins allowed the investigators to locate vessels relative to these structures and to identify connections between neighboring vascular territories.

A distinctive feature was a paired vascular space beside the tongue, the **paralingual sinus**, associated with depressions on the inner jaw surface. The authors’ hypothesis is that this specialization has a mechanical role during tongue pumping. The anatomical combination joins a broadly conserved head circulation to a localized feeding-related specialization.
''','A sinus is an expanded vascular space. Paralingual means beside the tongue. Its proposed mechanical function is a hypothesis arising from anatomy, whereas its location and associated bony depressions were directly documented.')
add('Orexin-positive cells form two hypothalamic clusters','orexin',['orexin_histology','orexin_map'],'''
**Orexin**, also called hypocretin, is a neuropeptide associated with arousal and food intake. A neuropeptide is a small protein used in signaling between cells. Mazengenya and colleagues mapped cells containing orexin-A in six bird species, including a Caribbean flamingo.

The **hypothalamus** is a brain region involved in regulating internal state. Antibody staining identified orexin-A-positive cells in a relatively dense cluster near its midline and a more dispersed cluster extending toward its lateral and ventral boundaries.

The medial group was centered on the **paraventricular hypothalamic nucleus**, while the lateral group occupied the **lateral hypothalamus**. These two clusters provide an anatomical organization for a state-regulating signaling system. The same broad arrangement occurred across the studied birds despite differences in brain size and life history.
''','Immunohistochemistry uses an antibody to detect a molecular target in tissue sections. The sections locate peptide-positive cells rather than measuring their firing during feeding or standing. The source reports the orexin-2 receptor as the avian receptor subtype, but it did not map that receptor in flamingos.')
add('Orexin-cell shape varies with hypothalamic location','orexin',['orexin_histology','orexin_map'],'''
The orexin-positive neurons in the flamingo were frequently **bipolar**, meaning that their visible processes extended in two principal directions. A **dendrite** is a neuronal process that receives signals and contributes to how a cell integrates input.

In the paraventricular cluster, the dendrites tended to run dorsoventrally, from the upper toward the lower part of the section. In the lateral cluster, they more often extended mediolaterally, from the midline toward the side of the brain.

Serial sections placed these different orientations within the same hypothalamic organization. The dense medial cluster and the more dispersed lateral cells are therefore distinguishable by both location and morphology. Their processes occupy different anatomical directions within tissue, adding cellular organization to the map of the peptide-positive population.
''','Dorsal means toward the upper aspect in these published section images, and ventral means toward the lower aspect. Medial means toward the brain midline and lateral means away from it. The staining resolves visible morphology rather than the functional strength of particular inputs.')
add('Additional staining occurs in the medial eminence','orexin',['orexin_eminence'],'''
The **medial eminence**, the term used in this paper, is a hypothalamic region linking neural regulation with endocrine signaling. The flamingo specimen contained orexin-A-positive bipolar cells there in addition to the two main hypothalamic clusters.

Most of these labeled cells occupied the internal layer, with occasional cells in the external layer. Their dendrites were predominantly radial, extending across the local tissue organization. This location differed from the pattern observed in the other birds examined in the same study.

The authors classified these as potential orexinergic neurons because antibody labeling can reflect cross-reactivity or uptake of peptide made elsewhere. Testing for **prepro-orexin messenger RNA**, the transcript used to produce the orexin precursor, would distinguish local production from those alternatives. A feeding and salt-balance role was proposed as a hypothesis.
''','The labeled cells were concentrated in the internal layer of the eminence. The tentative identity of these cells is a meaningful qualification because staining alone does not establish peptide synthesis. The source suggests examining precursor messenger RNA to resolve that question.')
add('Orexin-cell abundance scales with avian brain mass','orexin',['orexin_scaling','orexin_histology'],'''
**Stereology** estimates the number of cells in a three-dimensional tissue volume using systematically sampled sections. The study applied this method to the orexin-positive populations in the main hypothalamic clusters rather than counting only cells visible in one section.

The Caribbean flamingo brain weighed 11.1 g and contained an estimated 4,300 hypothalamic orexinergic neurons. The domestic goose brain weighed 12 g and contained an estimated 4,838, whereas the 2.8 g Inca tern brain contained an estimated 1,764.

Across the combined avian data, larger brains generally contained more orexinergic neurons. This **allometric relationship**, a relationship between biological size and another anatomical quantity, coexisted with a conserved two-cluster arrangement. Differences in cell abundance therefore occurred within a broadly similar organization rather than requiring an entirely different cluster layout.
''','These counts describe the main hypothalamic populations, not an experimentally measured increase in arousal or appetite. The flamingo specimen was one adult male, so the result is an anatomical estimate for that preparation. The relationship compares species rather than changes within an individual bird.')
add('A visual streak organizes the flamingo retina','retina',['retina_map','retina_histology'],'''
The **retina** is the neural tissue at the back of the eye that receives light and begins visual processing. Lisney and colleagues flattened and stained retinal preparations from Caribbean and Chilean flamingos to map neurons across the retinal surface.

Both species had a **visual streak**, an elongated region of elevated neuron density. It extended across the retinal meridian, just above the **pecten**, a vascular structure projecting into the avian eye. A small central region within the streak had particularly high density.

Peak densities were approximately 13,000–16,000 cells/mm². The concentration of neurons along a band provides an anatomical basis for sampling a broad sector of the visual environment with finer spatial resolution. The authors’ hypothesis links this organization to the open, relatively flat habitats in which flamingos commonly forage.
''','The maps count Nissl-stained neurons in the ganglion-cell layer, which can include displaced amacrine cells as well as retinal ganglion cells. The visual streak describes spatial distribution, not a strip that is the only region capable of vision. The pecten supplied a landmark for orienting each flattened retina.')
add('Dense retinal regions contain smaller neuronal somata','retina',['retina_histology'],'''
A neuronal **soma** is the cell body containing the nucleus and much of the cell’s metabolic machinery. In the flamingo retinal preparations, stained somata differed in size and appearance between low-density and high-density regions.

The investigators compared neurons from regions below 5,000 cells/mm², intermediate regions, and regions with at least 10,000 cells/mm². Neurons in the densest areas were generally smaller and more uniform than those in regions with fewer cells.

This relationship links the visual streak’s density to the cellular organization that produces it. Small cell bodies can occupy closely packed regions, while more heterogeneous populations occur elsewhere. The similar pattern in Caribbean and Chilean flamingos connects their shared retinal specialization with comparable local changes in neuronal packing.
''','The stained cell body is the structure measured here, rather than a complete neuron with all of its processes. Density is the number of labeled cells per square millimeter. Small neuronal somata accompanied high local cell density in both species.')
add('Optical scans identify a thickened retinal band','retina',['retina_oct'],'''
**Optical coherence tomography**, or OCT, uses reflected light to resolve tissue structure. Lisney and colleagues examined living Caribbean flamingo eyes with this method, complementing the flattened retinal preparations used for cell-density mapping.

Images looking toward the back of the eye contained a narrow dark band running across the retina above the pecten. Cross-sectional scans through this region identified retinal thickening compared with neighboring tissue. Its position matched the visual streak found in the neuron-density maps.

The two preparations therefore locate the same specialization through different measurements. Stained tissue maps where neurons are concentrated, while optical scans resolve tissue thickness in the living eye. Together they connect surface topography with the depth organization of the retina, without requiring the eye to be removed for the optical examination.
''','An OCT cross-section is a depth-resolved view through the retina. The agreement is anatomical: the band in the living eye aligns with the density streak in tissue preparations. The study compared these observations rather than treating image darkness as a direct measurement of neuron number.')
add('Flamingo spatial resolution lacks a central fovea','retina',['retina_eye','retina_map'],'''
A **fovea** is a localized retinal specialization that commonly includes a central depression and concentrated visual sampling. Neither retinal whole mounts nor optical scans identified a central fovea in the flamingos examined by Lisney and colleagues.

Instead, high-density regions within the visual streak supplied the basis for estimating **spatial resolving power**, the ability to distinguish fine spatial detail. Estimates near the central region were approximately 10–11 cycles/degree, where a cycle is one repeated dark-and-light pattern.

This estimate was calculated from anatomy rather than measured with a behavioral discrimination task. The eye morphology was similar in the two flamingo species, and their peak neuron densities were also comparable. Fine sampling can therefore arise within an extended retinal band without requiring a central foveal depression.
''','Cycles per degree expresses how many repeated light-dark patterns fit within one degree of visual angle. The study estimated this quantity from retinal density and optical dimensions. A behavioral threshold would also depend on downstream visual processing and the conditions of the task.')
add('Head inversion changes which directions are visible','fields',['fields_full'],'''
A **visual field** is the set of directions from which an eye can receive visual information. Martin and colleagues measured the field margins of lesser flamingos using an ophthalmoscopic reflex technique, which locates the directions visible through the eye’s optical system.

The birds had a frontal **binocular field**, the region visible to both eyes, that was narrow but vertically extended. Its maximum width was approximately 10°, and its vertical extent was about 90°. A blind sector above and behind the upright head reached approximately 28° in width.

Inverting the head during filter feeding reorients those sectors relative to the body. A feeding flamingo can walk forward into a direction falling within its blind area. Head orientation therefore changes sensory access even when the eyes and their field boundaries remain anatomically unchanged.
''','The field is described relative to the head, not permanently relative to the direction of walking. Inverting the head rotates the blind sector into a different part of the surrounding world. The authors proposed that sweeping the feeding head can permit scanning of these directions.')
add('Chick provisioning requires accurate bill alignment','fields',['fields_full'],'''
Lesser flamingos retain a frontal visual field that includes the bill, even though their own filter feeding does not require the precision of capturing an individual prey item. Martin and colleagues examined parental feeding as an explanation for this arrangement.

Parents deliver **crop milk**, a nutrient-rich secretion, into the open bill of a chick. The adult’s bill tip must align with that small target. The young bird develops the specialized filtering apparatus gradually and begins self-feeding at approximately 10–12 weeks.

The authors’ hypothesis is that chick provisioning helps shape the adult visual field. A second hypothesis involves accurate bill placement while constructing a mud nest. These behaviors impose positioning requirements distinct from adult filtration, connecting sensory organization to several uses of the same feeding structure across the life cycle.
''','The proposed selective explanation is a hypothesis, whereas the measured field geometry is the direct result. The study argues that adult feeding ecology alone is insufficient to explain the field. Precise alignment during provisioning uses the bill in a different way from drawing water through a filter.')
add('Lamellae divide the bill into particle-filtering spaces','jenkin',['lamella_types'],'''
**Lamellae** are repeated thin structures lining the flamingo bill. Jenkin examined their arrangement and dimensions alongside food and mineral particles recovered from digestive contents to investigate how these structures contribute to filtration.

The bill contains several forms of lamellae rather than one uniform mesh. Their spacing and orientation determine the openings through which water and particles can pass. Differences between shallow-keeled and deep-keeled bills accompany differences in the particle sizes processed by different flamingos.

Filtration therefore depends on the geometry of biological surfaces, not simply on opening the bill underwater. Structures that admit water can retain particular particles while excluding or releasing others. Comparing the filter with actual food contents links morphological dimensions to the kinds of material collected during natural feeding.
''','A keel is a ridge-like projection; the depth of the bill’s lower component changes the space available to the filtering apparatus. Jenkin distinguished filter and excluder functions. The spaces among the lamellae determine which particle sizes can pass through the apparatus.')
add('Fine bill platelets match a different feeding niche','jenkin',['fine_filter'],'''
Greater and lesser flamingos can use the same lake while processing different food. Jenkin compared the coarser apparatus of greater flamingos with the finer filter of lesser flamingos, which consume small algae and diatoms.

**Diatoms** are microscopic algae with mineralized outer walls. Their remains in stomach contents supplied a size reference for the fine lamellar platelets. Greater flamingos commonly processed larger material such as insect larvae and seeds, alongside mineral grit associated with that food.

Matching particle dimensions with filter structure explains how related birds can exploit different resources in one environment. The relevant specialization is the geometry of the bill surfaces and openings through which water is moved. The feeding apparatus partitions the available particles, reducing direct overlap between the materials retained by the two forms.
''','The comparison concerns the species and food records examined in the historical study. It connects anatomical dimensions to ingested particles rather than assigning every flamingo an identical diet. Diatom walls can remain recognizable after the soft cell contents have been processed.')
add('Tongue movements coordinate collection and transport','filter',['bill_tongue','bill_motion'],'''
The flamingo tongue occupies the trough of the lower bill and follows its curvature. Zweers and colleagues combined dissection, scanning electron microscopy, radiography, and movement analysis to examine how this apparatus collects food and then transports it toward the throat.

**Protraction** moves the tongue forward; **retraction** draws it backward. Tongue motion changes the space inside the mouth as the jaws move. Recurved spines on its posterior surface are oriented toward the throat and participate in directing retained material backward.

Collecting and transporting are different movement modes. Their coordination changes how water passes through the bill while food is retained and repositioned. The feeding system therefore combines a particle-selecting surface with a moving pump and a mechanism for transferring selected material away from the filtering region.
''','Radiography records internal movement through X-ray images, so tongue motion can be related to visible bill motion. The article analyzed separate collecting and transporting sequences. Its tongue anatomy and motion traces supply complementary evidence for the coordinated apparatus.')
add('Oral structure provides touch and taste information','filter',['bill_cavity','bill_buds'],'''
The filtering apparatus also contains surfaces involved in selecting food. Zweers and colleagues examined the oral lining and identified openings associated with **taste buds**, sensory structures involved in chemical detection, using scanning electron microscopy.

The study combined this anatomy with feeding experiments using seeds differing in size and taste. Selection changed when several foods were offered together, and the birds sometimes washed material out of the bill rather than retaining everything entering the mouth.

The authors attributed discrimination to both touch and taste. Mechanical properties inform the bird about particles interacting with the filtering surfaces, while chemical information can alter acceptance. These forms of sensory guidance operate alongside the physical mesh, making collection an actively regulated behavior rather than a purely fixed sieve acting on every particle identically.
''','The micrographs identify taste-bud openings rather than a complete map of the sensory nerves. The article’s feeding experiments support a role for both particle properties and taste. The study connects oral structure and food discrimination without identifying the receptor proteins responsible.')
add('Collection and transport use different motions','filter',['bill_motion','bill_tongue'],'''
Filtering food and moving retained food toward the throat require different relationships among the jaws, tongue, and head. Zweers and colleagues tracked anatomical landmarks during feeding to compare these coordinated motions.

During collection, repeated jaw and tongue movements maintained the filtering cycle. Transporting sequences altered their timing and displacement as material was moved away from the collecting region. **Kinematics** is the description of movement, including the position and motion of these anatomical landmarks through time.

The motion records connect visible bill opening with movements inside the mouth. A small external change can accompany a larger rearrangement of the tongue and oral space. Switching between movement modes allows the same apparatus to draw in particle-bearing water, retain selected food, and transfer that food toward ingestion.
''','The article separates collection from transport using measured movement patterns. Its traces describe the preparation rather than a proposed neural controller. The large curved tongue and caudally oriented spines provide the anatomical setting for these changing movements.')
add('Rapid head retraction generates prey-moving vortices','vortices',['vortex_head'],'''
A **vortex** is a region of rotating fluid. Ortega-Jimenez and colleagues used high-speed recordings and flow measurements to examine water motion generated by feeding Chilean flamingos and by physical models of their feeding structures.

Rapid head retraction reached approximately 40 cm/s and occurred over roughly 400 ms. It generated vortices that stirred material near the substrate and moved particles upward. The researchers followed visible particles in water to relate the animal’s movement to the resulting flow.

The bill therefore encounters a food distribution partly created by the bird’s own behavior. Retraction concentrates and redistributes material before it enters the filtering apparatus. This mechanism joins body movement with fluid dynamics, changing where prey and sediment are available rather than merely sampling an undisturbed water column.
''','The source includes both living-bird measurements and model experiments. A vortex rotates surrounding water and can carry suspended material along its motion. The retraction brings material from near the bottom toward the surface.')
add('Asymmetric bill chattering produces directional flow','vortices',['vortex_chatter'],'''
**Chattering** is rapid repeated opening and closing of the bill during feeding. The Chilean flamingos examined by Ortega-Jimenez and colleagues moved their mandibles at approximately 12 Hz, meaning about twelve oscillations per second.

The motion produced a directed water flow reaching approximately 7 cm/s. The upper and lower components contributed unequally, so the cycle was not equivalent to two symmetric plates simply moving apart and together. Flow measurements linked that asymmetry to water movement around the bill.

Particles and live brine shrimp were drawn along the resulting flow toward the feeding region. The opening cycle thus modifies the supply of material available to the internal filter. A repeatedly moving bill acts on its external fluid environment as well as changing the opening through which food-bearing water enters.
''','The directional flow was measured around living birds and examined with mechanical mandibles. A frequency of twelve hertz refers to motion cycles, not the pitch of a vocal sound. Asymmetric mandible movement directed flow upward toward the feeding region.')
add('Morphing feet generate prey-trapping eddies','vortices',['vortex_foot'],'''
Flamingos spread and fold the webbing of their feet during stepping and stomping. Ortega-Jimenez and colleagues recorded this motion and tested its fluid effects using a mechanical foot that reproduced changes in the exposed surface.

During downward motion, the expanded foot pushes a larger volume of water. During upward motion, folding reduces its exposed area. This asymmetry generates rotating flows that can lift sediment and hold small organisms near the feeding region rather than moving water equally in both directions.

The mechanical-foot experiments produced flows capable of trapping live prey. The foot therefore participates in acquiring food before the bill filters it. A locomotor structure changes the local fluid environment through its shape and movement, coupling stepping behavior with the concentration and transport of particles and organisms.
''','Morphing here means changing shape during movement. The mechanical preparation isolates the contribution of foot motion to water flow. The paper also includes numerical flow analysis, so different panels should be interpreted according to their experimental or computational preparation.')
add('Bent-bill skimming creates recirculating prey traps','vortices',['vortex_skim','vortex_capture'],'''
**Skimming** places the bill near the water surface while the bird and surrounding flow move relative to one another. The bent shape of the flamingo bill affects how water separates and circulates around it.

Experiments with the bill-shaped preparation identified alternating vortices and recirculating regions that trapped particles and live brine shrimp. In a separate capture experiment, the researchers compared a suction pump alone with the same pump plus moving mechanical mandibles.

Adding chattering increased shrimp capture from about 1.6 to 11.6 shrimp/s in the reported preparation. The comparison separates suction from the additional contribution of bill motion. External recirculation and repeated movement can increase the food reaching an intake system, linking local hydrodynamics to a measured change in capture performance.
''','The numerical capture rates belong to the mechanical apparatus, not a directly measured intake rate for a freely feeding flamingo. The pump approximated internal suction while mandible motion added external fluid effects. The control retained pumping while removing chattering.')
add('Food density changes the rate of ingestion','feeding',['intake_shrimp'],'''
A **functional response** is the relationship between food density and the rate at which an animal consumes that food. Deville and colleagues offered greater flamingos food trays containing different densities of live brine shrimp, insect larvae, and rice seeds.

The order of food densities was randomized, and video recordings measured the time spent with the bill underwater. Remaining food was counted after each short trial, linking the decrease in available items to the duration of feeding rather than to total observation time.

Intake generally changed nonlinearly with food density. At high densities, the increase slowed as the feeding apparatus approached processing limits. At low densities, reduced encounters also limited ingestion. The resulting relationship explains why declining wetland food abundance can reduce feeding returns even in a bird capable of continuously filtering water.
''','The intake estimate was expressed as items consumed per second of feeding. Some trials involved several birds, and the authors combined their underwater feeding times to estimate the shared rate. The density manipulation measures a feeding response rather than a neural decision threshold.')
add('Contact calls contain combinations of identity cues','acoustic',['call_features'],'''
A **contact call** is a vocal signal associated with maintaining social contact. Mathevon recorded greater flamingos in a captive flock and compared repeated calls from identified adults to determine which acoustic properties differed consistently between individuals.

Calls contained broad frequency structure and large fluctuations in amplitude. **Amplitude** describes the magnitude of a sound signal; **frequency** describes the number of oscillations per second. The analysis separated how these properties changed through time from how energy was distributed across frequencies.

Combining temporal and spectral information distinguished individuals more effectively than one parameter alone. A caller’s acoustic identity therefore resided in a pattern of features rather than a single uniquely diagnostic pitch. The measured differences provide information that a receiver could use when locating a familiar bird within a crowded social environment.
''','The paper compared acoustic recordings, not neural responses or a playback recognition test. Its findings identify available identity cues. Repeated calls from an individual contained consistent temporal and frequency properties.')
add('The amplitude envelope carries temporal identity','acoustic',['call_time','call_features'],'''
The **amplitude envelope** describes the slower rise and fall of sound magnitude over a call. Mathevon compared envelopes from equal-duration segments so that differences in their shapes could be evaluated independently of total call length.

The first 0.145 s of each call supplied the common interval. Temporal patterns separated several individuals clearly, while two callers retained overlapping patterns. Repeated calls from one bird were generally more similar than calls from different birds.

These results connect acoustic identity with the timing of energy within the signal. Two birds can have similar temporal envelopes, so timing alone need not specify the caller. Differences in spectral structure can complement this overlap, providing additional cues when the sequence of amplitude changes is similar between individuals.
''','The common interval was determined by the shortest analyzed call. Equalizing the comparison window avoided treating unequal recording length as the only difference. The patterns were compared analytically, so the separation describes acoustic information rather than a demonstrated perceptual boundary.')
add('Spectral and temporal call features complement each other','acoustic',['call_features'],'''
A **spectrum** describes how a signal’s energy is distributed across frequencies. Mathevon examined the flamingo call over approximately 0.5–5.5 kHz, including its lowest components, strongest frequencies, and broader distribution of energy.

**Harmonics** are components related to a fundamental frequency by whole-number multiples. The calls contained two harmonic series, producing a two-voice structure. Differences between callers occurred in the placement of spectral energy as well as in the time course of amplitude changes.

Some individuals with overlapping amplitude envelopes separated more clearly by their spectra. Considering both forms of information distinguished all analyzed callers. Acoustic identity is consequently distributed across complementary properties, allowing one domain to supply differences that are weak or overlapping in the other.
''','Kilohertz means thousands of oscillations per second. The two harmonic series are properties of the recorded call, not evidence for two identified neural generators. The combined analysis supports a multiparameter description of the available acoustic identity information.')
add('Colony noise favors redundant acoustic information','acoustic',['call_features'],'''
Flamingo colonies contain many simultaneous vocalizations, making individual signals compete with background sound. Mathevon compared the measured call features with the constraints that dense colonial environments impose on reliable information transmission.

Call duration, slow amplitude modulation, spectral bandwidth, and the distribution of energy among harmonics all contained differences between individuals. **Bandwidth** is the frequency range occupied by a signal. No single measured feature fully separated every caller in the analysis.

The authors’ hypothesis is that combining temporal and frequency cues improves identification under these conditions. Repeated contact calls also provide repeated opportunities to receive the same information. Multiparameter structure and repetition connect the physical form of the vocal signal to the problem of maintaining social contact within persistent background noise.
''','The proposed advantage in noise was an interpretation of call structure and comparative acoustic work. The study did not manipulate colony noise during a recognition task. Its measured result is that several distinct acoustic properties carried individual differences.')
add('Courtship assembles a repertoire of group displays','display',['display_animals'],'''
Greater flamingo courtship involves coordinated actions performed within groups. Perrot and colleagues recorded individually identified wild birds in the Camargue and scored the actions and transitions appearing in their display sequences.

A **behavioral repertoire** is the set of distinct actions available within a context. Flamingo displays included head flagging, wing salutes, inverted wing salutes, and marching. **Versatility** described changes among the actions rather than simply how long the bird remained active.

Combining repertoire size with versatility yielded a measure of display complexity. This distinguishes a bird repeating one action from a bird assembling many actions into changing sequences. The social signal therefore contains information in its organization through time as well as in the posture or movement expressed at any one moment.
''','Head flagging involves repeated movements of the raised head. Wing salutes expose the wings during display, and marching coordinates directional movement within the group. The investigators recorded these behaviors during the group courtship period preceding breeding.')
add('Display complexity rises and then declines with age','display',['display_age','display_animals'],'''
Marked flamingos allowed Perrot and colleagues to connect courtship behavior with known age. The recorded birds ranged from approximately 4 to 37 years, permitting comparison across much of the adult life span.

Display complexity, repertoire size, and versatility each changed nonlinearly with age. Their fitted relationships rose through younger adulthood, reached their highest region around 20 years, and declined among older birds. The pattern was not a simple increase in performance throughout life.

The authors interpreted the later decline as consistent with reproductive senescence, age-related reduction in reproductive performance. A hypothesis in the discussion links display effort with physiological costs and oxidative stress. The directly observed relationship joins age with the complexity of the behavioral sequences used during group courtship.
''','Age was known from individual marking records rather than estimated from plumage. Senescence names an age-related decline, but its cellular cause was not measured by these videos. The source’s interpretation is therefore stated as a hypothesis alongside the observed behavioral trajectory.')
add('More complex displays predict breeding status','display',['display_breed','display_animals'],'''
Courtship performance was related to later reproductive status in the Camargue study. Perrot and colleagues compared the display complexity of birds subsequently confirmed at the breeding colony with those not confirmed there during the same breeding season.

Confirmed breeders had more complex display sequences. This relationship connects the repertoire and switching among actions to a reproductive outcome rather than treating complexity only as a descriptive property of movement.

The association is compatible with a role for display performance during pair formation. It also places the age-related trajectory within breeding behavior: changes in display complexity can accompany changes in access to reproduction. The authors discussed how selection during pairing could shape which older individuals later appear among breeding birds.
''','Breeding status was determined by subsequent observation at the colony. The comparison is observational, so it does not isolate whether greater complexity itself caused pair formation. It nevertheless connects the measured display organization with a later reproductive classification.')
add('Selective social bonds persist across several years','friends',['friends_network'],'''
An **association** is an observed occurrence of individuals together under a defined proximity rule. Rose and Croft repeatedly recorded individually marked flamingos in four captive flocks from 2012 to 2016, allowing the persistence of preferred companions to be examined.

The study represented birds as **nodes** and associations as **edges** in a social network. Edge strength summarized how often a particular pair occurred together. Selected strong connections remained apparent across observation periods rather than being replaced by indiscriminate mixing.

Stable relationships involved pairs, trios, and small groups. These associations show that a large flock can contain structured preferences within its collective activity. Keeping the flock together therefore preserves more than the number of birds: it also preserves opportunities for particular individuals to maintain long-term social relationships.
''','A dyad is a pair of individuals. The comparison included more than one flamingo species and repeated seasonal observations. Network edges represent observed association frequencies rather than an assumed emotional state.')
add('A flock contains preferred and avoided companions','friends',['friends_caribbean'],'''
Social organization includes variation in which birds associate, even when they share one enclosure. Rose and Croft compared observed pairwise associations with expectations for groups of the same size to identify preferred and avoided companions.

An **association index** expresses how consistently a pair is observed together, with higher values indicating stronger co-occurrence. Smaller flocks tended to have larger mean pairwise associations, while larger flocks offered more possible social combinations.

The networks retained strongly connected subsets within the broader flock. Some relationships occurred between birds of the same sex and persisted over time, so every strong association cannot be treated as a breeding pair. Flock membership, reproductive pairing, and preferred social companionship describe related but distinct parts of flamingo social organization.
''','Avoided association means less co-occurrence than expected under the study’s comparison, not necessarily an observed aggressive interaction. A strong edge can connect breeding partners or nonbreeding companions. Sex information and repeated observations help distinguish these possibilities.')
add('Season changes the density of realized social ties','friends',['friends_network'],'''
**Network density** describes how many of the possible connections among individuals are actually observed. Rose and Croft compared flamingo flock networks between spring and summer observations and the autumn and winter period.

Lesser, Caribbean, and Andean flamingos showed denser realized networks during spring and summer in the study. The Chilean flamingo flock did not show the same seasonal pattern. Social structure therefore changed with time in ways that differed among the observed flocks.

Seasonal changes can alter collective association without eliminating persistent preferred partners. A bird can retain familiar companions while also participating in a broader set of social connections during another part of the year. The result connects enduring individual relationships with changing opportunities for interaction across a flock’s annual activity cycle.
''','Density summarizes the network as a whole, whereas a persistent edge describes one relationship. These measures can change independently. The observed species differences also occurred in separate captive flocks, so enclosure and group context accompany the taxonomic comparison.')
add('Young flamingos change position within the flock','juvenile',['juvenile_positions','juvenile_age'],'''
Loader and Rose photographed greater and Caribbean flamingo flocks to record where young birds stood and which age classes occurred nearby. Age categories were identified using developmental appearance and known flock records.

Greater flamingos in the younger age classes occurred disproportionately around the periphery of the flock. The relationship changed as birds matured beyond the early juvenile stages. Caribbean flamingos showed a different spatial pattern, with young birds commonly located toward the center of their observed flock.

**Ontogeny** is development across an individual’s life. The contrasting trajectories connect ontogeny with spatial social organization, rather than assuming that a chick immediately occupies the same social position as an adult. Where a young bird stands changes the set of companions and social interactions available at that location.
''','Periphery means the edge of the flock, while center means a position with birds surrounding the focal individual. The study compared captive groups in their own enclosures. Species differences should therefore be interpreted with those group and enclosure contexts attached.')
add('Nearest companions change as juveniles develop','juvenile',['juvenile_neighbours','juvenile_age'],'''
A **nearest neighbor** is the closest individual to a focal bird under the study’s proximity definition. Loader and Rose used repeated photographs to classify the age of the birds nearest to juvenile flamingos.

In greater flamingos, birds in the youngest category most often occurred nearest other young birds. The dominant age class among nearest companions shifted as juveniles developed. Older birds increasingly associated with members of later developmental stages and with adults.

These changes connect social assortment with maturation. **Assortment** means nonrandom grouping according to a characteristic such as age. Juvenile proximity patterns therefore do more than describe where the flock stands: they identify which developmental categories are encountered together, potentially changing access to social information and the context in which young birds acquire adult behavior.
''','The measured result is proximity by age class rather than direct observation of learning. Access to social information is a proposed consequence of encountering different companions. The study’s age categories distinguish young juveniles, older juveniles, subadults, and adults.')
add('Cosmetic pigments contribute to plumage color','cosmetics',['cosmetic_animal'],'''
Flamingo feather color includes pigments deposited within growing feathers and pigments applied externally during plumage maintenance. Chiale and colleagues separated these locations in neck feathers and compared their pigment content with redness.

**Carotenoids** are pigments contributing yellow-to-red coloration in biological tissues. **Canthaxanthin** is a carotenoid abundant in greater flamingo plumage and in the secretions used for cosmetic application. The study extracted pigments separately from feather surfaces and from material within the feathers.

Surface carotenoid concentration was associated with feather redness. The visible signal therefore combines feather structure with a behaviorally maintained external contribution. Changes in cosmetic application can alter the appearance presented to other birds, connecting an action performed during maintenance with the coloration available during social interactions.
''','Separate extraction distinguishes pigments already within feathers from pigments on their surface. The study examined coloration and its maintenance rather than directly measuring mate choice.')
add('Sunlight fades color without cosmetic renewal','cosmetics',['cosmetic_fading','cosmetic_animal'],'''
Chiale and colleagues tested how feather color changed when cosmetic maintenance stopped. Neck feathers were exposed to outdoor conditions for 40 days, with one group receiving direct sunlight and a comparison group shielded from solar radiation.

Feathers exposed to sunlight lost redness, while the shaded comparison did not show the same decline. The study used the **redness coordinate**, the a-star measure along the green-to-red axis, to quantify changes in scanned feathers before and after exposure.

The result links signal appearance with both environment and maintenance. Pigment on the feather surface can degrade after application, so preserving intense color requires renewed input rather than one permanent deposit. A flamingo’s social appearance can consequently reflect a continuing behavioral investment as well as the pigments incorporated when its feathers grew.
''','The experiment used removed feathers, which could receive no fresh cosmetic secretions. Both groups experienced outdoor conditions, while their orientation controlled direct solar exposure. Redness reflects the pigments remaining after environmental exposure.')
assert len(S)==44,len(S)
items=[{'lead':'Passive posture','text':'One-leg support depends on medial foot placement and gravity loading proximal joint constraints.'},{'lead':'State and balance','text':'Quiet flamingos localize the ground-force application point; activity increases its excursions and speed.'},{'lead':'Neural organization','text':'Flamingo orexin-positive cells form medial and lateral hypothalamic clusters, with tentative additional staining in the medial eminence.'},{'lead':'Sensory guidance','text':'A retinal visual streak supports spatial sampling, while head orientation and chick provisioning impose distinct visual demands.'},{'lead':'Feeding mechanics','text':'Bill filtering, tongue motion, and behavior-generated vortices jointly determine particle and prey capture.'},{'lead':'Social signals','text':'Calls combine temporal and spectral identity cues; displays, preferred companions, and maintained plumage organize social behavior.'}]
spec={'lecture':67,'content_slides':44,'theme':'carbon-paper','title_height':2.6,'title_image':fig('display_animals'),'title_refs':[R['display']['reference']],'slides':S,'takeaways':{'items':items,'cite':'; '.join(short(k) for k in ['balance','orexin','retina','vortices','acoustic']),'refs':[R[k]['reference'] for k in R]}}
(B/'lecture.json').write_text(json.dumps(spec,indent=2)+'\n')
print('Slides',len(S),'words',min(len(' '.join(s['body']).split()) for s in S),max(len(' '.join(s['body']).split()) for s in S))
