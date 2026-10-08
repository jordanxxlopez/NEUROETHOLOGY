import json
from pathlib import Path
H=Path(__file__).resolve().parent
C={};F={}
def crop(n,k,p,b,number,desc,color=False):
 C[n]=[k,p,b];d=json.loads((H/'sources'/f'{k}-crossref.json').read_text());a=d['author'];who=a[0]['family']+(' & '+a[1]['family']if len(a)==2 else ' et al.'if len(a)>2 else '');yr=d['published']['date-parts'][0][0]
 F[n]={'paper':k,'pdf':f'papers/{k}.pdf','page':p,'box':b,'out':f'figures/{n}.png','caption':f'{who} ({yr}), Fig. {number}. {desc}.','source_url':'https://doi.org/'+d['DOI'],'original_color':color}
crop('animal','flow13',3,[.5,.235,.82,.4],'1C','Caribbean spiny lobster with its lateral antennule labeled',True)
crop('arena','search91',4,[.18,.115,.76,.415],'1A–B','Flume, odor delivery and reference grid')
crop('paths','search91',11,[.205,.125,.79,.46],'5A–C','Repeated recorded source-search paths of individual lobsters')
crop('angles','search91',10,[.14,.12,.83,.72],'4A–B','Heading and turning-angle distributions')
crop('approach','search91',11,[.18,.6,.82,.85],'6','Walking speed and heading versus distance from the source')
crop('aesthetasc','search04',2,[.32,.32,.68,.535],'1B','Scanning electron micrograph of aesthetasc and guard hairs')
crop('sensorybody','search04',2,[.055,.095,.69,.535],'1A–F','Body and antennular sensory structures')
crop('flume04','search04',5,[.14,.12,.85,.435],'2','Shrimp-odor source, flow chamber and lobster release position')
crop('success','search04',6,[.055,.69,.46,.865],'3','Source-finding success after selective antennular lesions')
crop('performance','search04',7,[.05,.115,.76,.45],'4A–D','Arrival time, path straightness, walking speed and heading')
crop('antennafix','search04',8,[.055,.565,.6,.95],'5A–E','Search performance with second antennae immobilized')
crop('plumes','sampling11',6,[.055,.115,.86,.31],'3A–C','Measured dye plumes under three flow conditions',True)
crop('sampler','sampling11',8,[.09,.115,.48,.33],'5A–B','Colored plume filaments and concentration along a sampling transect',True)
crop('samplingtraces','sampling11',8,[.08,.655,.54,.95],'6A–E','Concentrations encountered at different heights and sampling schedules')
crop('doseposition','sampling11',10,[.13,.115,.845,.32],'8A–D','Encountered concentrations versus source distance')
crop('gaps','sampling11',11,[.07,.115,.66,.28],'10A–B','Odor-free gap durations for flicking antennules and continuous sampling')
crop('edges','sampling11',12,[.20,.115,.81,.28],'12A–B','Odor encounters at plume centers and edges')
crop('sniffphoto','sniff01',2,[.058,.094,.94,.239],'1A–D','Original video frames of dye capture and retention during flicking',True)
crop('sniffmap','sniff01',2,[.37,.38,.925,.55],'2','Measured spatial dye pattern retained between successive flicks',True)
crop('hairanatomy','flick08',3,[.085,.088,.47,.594],'1A–C','Spiny lobster photograph and antennular scanning electron micrographs')
crop('hairmodel','flick08',5,[.54,.12,.94,.536],'3A–B','Photographed biological hair array and dynamically scaled physical model')
crop('downflow','flick08',7,[.09,.115,.47,.54],'5A–B','Measured particle-image-velocimetry flow during the downstroke',True)
crop('orientation','flick08',7,[.60,.66,.94,.865],'6','Measured flow through a zigzag array in its observed orientation',True)
crop('guards','flick08',8,[.085,.115,.48,.398],'7A–C','Hair-array photographs and measured velocity with guard hairs present or removed')
crop('returnflow','flick08',9,[.085,.088,.48,.54],'9A–B','Measured slow-return flow field and velocity profile',True)
crop('irlocal','ir13',4,[.14,.09,.85,.71],'2','Receptor RNA localization with antisense and sense-probe controls',True)
crop('dendrites','ir13',6,[.2,.636,.824,.78],'4B, upper row','IR25a immunofluorescence in aesthetasc dendrites with control labels intact',True)
crop('somata','ir13',6,[.295,.09,.83,.26],'4C, upper row','IR25a staining in sensory-cell somata and inner dendrites',True)
crop('ligands','ir13',8,[.09,.09,.86,.405],'6A–D','Calcium imaging reveals heterogeneous odor-response profiles',True)
crop('singlecell','single20',3,[.17,.582,.46,.765],'2d','Fluorescent sensory-cell cluster and collection pipette',True)
crop('irheat','single20',6,[.275,.092,.784,.72],'3','Single-cell expression of common and variable ionotropic receptors',True)
crop('cellgenes','single20',7,[.095,.595,.91,.884],'4','Authors’ summary of genes expressed in olfactory sensory neurons',True)
crop('stimulus','diversity12',3,[.085,.1,.925,.477],'1A–C','Simultaneous dye calibration, calcium responses and firing-rate controls',True)
crop('currents','diversity12',5,[.09,.09,.715,.605],'2A–D','Excitatory, inhibitory and intrinsically generated sensory activity',True)
crop('calcium','diversity12',6,[.09,.1,.875,.69],'3A–C','Simultaneous spikes and calcium responses across neuronal response classes',True)
crop('oscillations','diversity12',7,[.09,.1,.77,.925],'4A–B','Simultaneous bursting and slower calcium oscillations',True)
crop('neighbors','diversity12',8,[.08,.247,.70,.80],'5A–C','Colored sensory-cell images, calcium records and pairwise correlations',True)
crop('cyclic','cyclic92',3,[.50,.09,.94,.295],'3','Proline, phosphodiesterase inhibition and cyclic-GMP analog evoke outward currents')
crop('forskolin','cyclic92',4,[.52,.09,.94,.24],'5','Forskolin mimics an odor-evoked outward current')
crop('secondtime','dual94',2,[.50,.09,.94,.485],'1','Odor evokes rapid cAMP and IP3 accumulation in dendritic membranes')
crop('secondligands','dual94',3,[.09,.50,.93,.87],'3A–B','Taurine and proline differ in second-messenger recruitment')
crop('burstperiod','burst14',3,[.055,.088,.475,.84],'1a–d','Recorded spontaneous bursts and distribution of intrinsic periods',True)
crop('burstphase','burst14',4,[.05,.085,.94,.566],'2a–d','Stimulus timing changes burst probability and sensory responses',True)
crop('burstdecode','burst14',8,[.05,.08,.94,.545],'6a–c','Authors’ synthetic-population decoder estimates stimulus intervals',True)
crop('brain','inhibit99',3,[.092,.225,.46,.435],'1A–C, lower inset','Original published lobster olfactory-lobe anatomy and recording positions')
crop('paired','inhibit99',3,[.058,.085,.46,.435],'1A–C','Paired-shock responses in the olfactory lobe and antennular nerve')
crop('drugs','inhibit99',4,[.054,.11,.484,.49],'2A–B','Histamine and GABA suppress lobster afferent voltage signals')
crop('separate','inhibit99',4,[.525,.115,.932,.49],'3','Histamine inhibition persists after GABA-receptor blockade')
crop('antagonists','inhibit99',5,[.055,.115,.468,.305],'4','Receptor antagonists distinguish histamine and GABA actions')
crop('measuredflow','flow13',9,[.14,.74,.91,.875],'4A–C','Measured particle velocities and dye concentration in a flume',True)
crop('flux','flow13',14,[.23,.23,.78,.388],'11C','Authors’ modeled transverse odor flux on opposite sides of a plume',True)
crop('plumevalidate','plume20',5,[.15,.087,.765,.417],'2','Measured fluorescence and velocity vectors used for plume-model validation',True)
crop('intermittency','plume20',7,[.055,.285,.94,.492],'6','Authors’ modeled intermittency profiles across the plume',True)
crop('samplefreq','plume20',8,[.14,.085,.94,.257],'7','Authors’ model compares intermittency estimates at different sampling frequencies',True)
# Bounds verified against original pages; remove text outside each figure.
updates={
'animal':[.50,.226,.775,.378], 'arena':[.18,.115,.77,.40], 'paths':[.205,.11,.805,.405], 'angles':[.14,.11,.85,.72], 'approach':[.18,.60,.825,.83],
'aesthetasc':[.07,.367,.381,.533], 'sensorybody':[.07,.09,.625,.536], 'flume04':[.14,.105,.85,.415], 'success':[.065,.65,.483,.859], 'performance':[.16,.09,.865,.38],
'plumes':[.06,.08,.89,.267], 'sampler':[.085,.08,.50,.322], 'doseposition':[.15,.09,.86,.317],
'sniffphoto':[.075,.093,.932,.23], 'sniffmap':[.365,.378,.932,.54],
'hairanatomy':[.095,.087,.462,.669], 'hairmodel':[.537,.087,.905,.516], 'downflow':[.10,.087,.46,.464], 'orientation':[.557,.661,.875,.856], 'guards':[.085,.085,.482,.432], 'returnflow':[.085,.085,.48,.501],
'irlocal':[.093,.077,.747,.70], 'dendrites':[.093,.58,.826,.765], 'somata':[.321,.076,.827,.27], 'ligands':[.09,.08,.90,.406], 'irheat':[.18,.113,.8,.761],
'stimulus':[.09,.08,.90,.458], 'currents':[.09,.077,.615,.681], 'calcium':[.09,.08,.875,.619], 'oscillations':[.09,.08,.77,.925], 'neighbors':[.08,.208,.70,.806],
'cyclic':[.518,.084,.95,.25], 'forskolin':[.516,.085,.95,.228], 'secondtime':[.516,.084,.95,.487], 'secondligands':[.053,.483,.95,.913],
'burstperiod':[.073,.075,.647,.835], 'burstphase':[.135,.075,.862,.598], 'burstdecode':[.073,.08,.94,.491],
'brain':[.211,.196,.481,.378], 'paired':[.068,.074,.484,.378], 'drugs':[.068,.085,.486,.41], 'separate':[.516,.085,.934,.438],
'flux':[.272,.383,.75,.48], 'intermittency':[.26,.268,.94,.465], 'samplefreq':[.26,.085,.94,.267]
}
for n,b in updates.items():C[n][2]=b;F[n]['box']=b
C['gaps']=['sampling11',9,[.07,.085,.635,.585]];F['gaps'].update(page=9,box=C['gaps'][2],caption='Reidenbach & Koehl (2011), Fig. 7A–F. Odor-free gap categories for flicking and continuous sampling.')
F['hairmodel']['caption']='Reidenbach et al. (2008), Fig. 3A–B. Ventral and side photographs of the dynamically scaled physical hair-array model.'
F['cyclic']['caption']=F['cyclic']['caption'].replace('Fig. 3.','Fig. 4.')
F['forskolin']['caption']=F['forskolin']['caption'].replace('Fig. 5.','Fig. 6.')
F['dendrites']['caption']=F['dendrites']['caption'].replace('4B, upper row','4B, fluorescent row and original labels')
F['somata']['caption']=F['somata']['caption'].replace('4C, upper row','4C, fluorescent row and original labels')
F['intermittency']['caption']='Michaelis et al. (2020), Fig. 6. Authors’ modeled concentration-spike counts across the plume at different sampling frequencies.'
F['samplefreq']['caption']='Michaelis et al. (2020), Fig. 7. Authors’ model compares detected concentration-spike counts at different sampling frequencies.'
C['forskolin']=['cyclic92',3,[.06,.084,.495,.297]];F['forskolin'].update(page=3,box=C['forskolin'][2],caption='Michel & Ache (1992), Fig. 2. Forskolin and IBMX evoke an outward current in a proline-inhibited neuron.')
# Final label-preserving refinements.
for n,b in {'paths':[.205,.11,.805,.42],'angles':[.14,.11,.85,.70],'sampler':[.075,.08,.50,.335],'plumes':[.11,.08,.9,.272],'flume04':[.14,.093,.85,.409],'orientation':[.557,.661,.90,.866],'drugs':[.068,.067,.486,.41],'separate':[.516,.067,.934,.438],'intermittency':[.165,.25,.935,.463],'samplefreq':[.165,.054,.935,.26]}.items():C[n][2]=b;F[n]['box']=b
C['brain']=C['paired'].copy();F['brain'].update(page=3,box=C['brain'][2],caption='Wachowiak & Cohen (1999), Fig. 1A–C. Olfactory-lobe anatomy and original recording locations.')
F['currents']['caption']=F['currents']['caption'].replace('intrinsically generated','intrinsic')
for n in ['antennafix','samplingtraces','edges','antagonists','measuredflow','plumevalidate']:C.pop(n,None);F.pop(n,None)
F['somata']['caption']='Corey et al. (2013), Fig. 4C, fluorescent row. IR25a in somata and inner dendrites; control shown.'
F['singlecell']['caption']='Kozma et al. (2020), Fig. 2d. Sensory-cell cluster and collection pipette.'
(H/'crops.json').write_text(json.dumps({'papers':{k:f'papers/{k}.pdf'for k in {v[0]for v in C.values()}},'dpi':300,'crops':C},indent=2)+'\n');(H/'figure-sources.json').write_text(json.dumps(F,indent=2,ensure_ascii=False)+'\n')
