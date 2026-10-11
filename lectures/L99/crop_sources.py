from pathlib import Path
import json,subprocess,sys
R=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
D=Path('/workspace/l99-research/papers')
# Fractions are measured from inspected original PDF pages. No scientific pixels are edited.
rows=[
('animal','moroz',2,[.066,.076,.272,.310],'1(a)','Pleurobrachia bachei with tentacles and comb rows'),
('p_tentacle','moroz',9,[.19,.28,.445,.45],'Extended Data 1(b,e)','Tentacle sheaths and tentilla'),
('p_cilia','moroz',2,[.266,.313,.489,.45],'1(d)','Scanning electron microscopy of ciliary combs'),
('p_colloblast','moroz',2,[.49,.313,.703,.45],'1(e)','Adhesive colloblasts on a tentacle'),
('p_net','moroz',9,[.46,.454,.823,.81],'Extended Data 1(h)','Neural plexus surrounding the mouth'),
('p_anatomy','moroz',9,[.19,.071,.823,.453],'Extended Data 1(a–e)','Body, tentacles, comb rows and aboral organ'),
('p_glutamate','moroz',5,[.075,.078,.466,.299],'5(a)','Neural processes and muscle-associated tissues'),
('p_response','moroz',5,[.057,.313,.535,.552],'5(b)','Concentration dependence of muscle contraction'),
('p_phylo','moroz',2,[.079,.539,.856,.921],'2','Relationships among sampled ctenophore lineages'),
('p_genes','moroz',4,[.168,.074,.823,.278],'4(a,b)','Developmental stages and expression profiles'),
('p_receptors','moroz',4,[.508,.299,.825,.459],'4(d)','Glutamate-receptor expression during development'),
('k_local','jokura2022',4,[.505,.124,.90,.394],'1(C–E)','Distinct localization of CTENO64 and CTENO189'),
('k_whole','jokura2022',4,[.096,.228,.49,.418],'1(B)','Comb-specific CTENO189 labeling in Bolinopsis'),
('k_em','jokura2022',4,[.096,.43,.495,.56],'1(F)','Proximal and distal ciliary ultrastructure'),
('k_growth','jokura2022',4,[.504,.401,.905,.573],'1(G)','Lengths of proximal and distal compartments'),
('k_knock','jokura2022',5,[.091,.122,.451,.282],'2(A)','Control and CTENO189-depleted cydippids'),
('k_loss','jokura2022',5,[.459,.124,.90,.259],'2(C)','Distal comb-plate ultrastructure after knockdown'),
('k_spacing','jokura2022',6,[.157,.126,.881,.312],'3(A,B)','Ciliary positions and neighboring distances'),
('k_wave','jokura2022',7,[.146,.122,.855,.37],'4(A)','Control and knockdown beat waveforms under load'),
('k_phase','jokura2022',7,[.449,.379,.848,.54],'4(D,E)','Adjacent comb-plate phase relationships'),
('j_organ','statocyst',4,[.075,.249,.925,.442],'1(D,E)','Statolith and balancer anatomy in two planes'),
('j_volume','statocyst',4,[.073,.447,.921,.607],'1(F,G)','Reconstructed aboral-organ cell organization'),
('j_cells','statocyst',8,[.074,.210,.452,.327],'3(B)','Balancer-cell anatomy across quadrants'),
('j_bridge','statocyst',8,[.073,.328,.449,.433],'3(C)','Bridge-cell processes spanning the statocyst'),
('j_ann','statocyst',6,[.074,.073,.924,.201],'2(A,B)','Aboral syncytial neurons in orthogonal views'),
('j_synapse','statocyst',6,[.074,.36,.476,.473],'2(E)','Original ultrastructure of aboral synapses'),
('j_targets','statocyst',8,[.464,.078,.923,.212],'3(E)','Aboral nerve-net contacts on balancer cells'),
('j_recip','statocyst',8,[.465,.213,.924,.326],'3(F)','Reciprocal bridge and nerve-net contacts'),
('j_arrest','statocyst',11,[.075,.273,.91,.516],'4(C,D)','Kymographs and timing of arrest and renewed beating'),
('j_time','statocyst',11,[.589,.275,.884,.497],'4(D)','Timing differences across balancer pairs'),
('j_freq','statocyst',11,[.076,.531,.549,.708],'4(E)','Balancer beat frequency through time'),
('b_net','burkhardt',3,[.264,.066,.675,.350],'2(A)','Continuous subepithelial nerve-net reconstruction'),
('b_bodies','burkhardt',3,[.676,.066,.938,.261],'2(B)','Reconstructed neuronal somata and vesicles'),
('b_vesicles','burkhardt',3,[.264,.355,.604,.433],'2(D)','Vesicles inside expanded neurite segments'),
('b_peptide','burkhardt',3,[.605,.355,.938,.433],'2(E)','Peptide labeling in tubulin-positive neurites'),
('b_neurite','burkhardt',3,[.264,.432,.713,.546],'2(F)','Vesicles in a beaded neurite reconstruction'),
('b_meso','burkhardt',4,[.228,.066,.666,.357],'3(A)','Mesogleal neurons alongside the surface nerve net'),
('b_sensory','burkhardt',4,[.265,.432,.939,.816],'4(A–D)','Sensory cells and their observed cellular contacts'),
('s_precursor','sachkova',3,[.298,.568,.87,.883],'1(F)','Ctenophore peptide-precursor sequence alignments'),
('s_net','sachkova',5,[.11,.405,.884,.555],'2(E–H)','Peptide immunolabeling around nerve net and combs'),
('s_ao','sachkova',6,[.108,.127,.901,.391],'3(A–I)','Neuropeptide expression in aboral and pharyngeal cells'),
('s_pharynx','sachkova',6,[.108,.394,.901,.535],'3(J–M)','Peptide labeling in sensory and pharyngeal cells'),
('s_behavior','sachkova',7,[.211,.141,.467,.242],'4(B)','Five-minute swimming paths before peptide comparisons'),
('s_speeds','sachkova',7,[.096,.248,.898,.484],'4(D)','Normalized swimming speeds following peptide exposure'),
('s_transcript','sachkova',8,[.489,.129,.847,.314],'5(B)','Molecular annotation of a subepithelial neuron'),
('s_calcium','sachkova',8,[.49,.317,.85,.401],'5(C)','Calcium-sensor domain organization'),
('s_em','sachkova',10,[.104,.13,.898,.382],'6(A–C)','Nerve net, comb cells and neuronal vesicles'),
('s_triads','sachkova',10,[.535,.386,.895,.56],'6(H–K)','Neuronal organelles and synaptic triad ultrastructure'),
]
refs={'moroz':('Moroz',2014,'10.1038/nature13400'),'jokura2022':('Jokura',2022,'10.1016/j.cub.2022.09.061'),'statocyst':('Jokura',2026,'10.7554/eLife.108420'),'burkhardt':('Burkhardt',2023,'10.1126/science.ade5645'),'sachkova':('Sachkova',2021,'10.1016/j.cub.2021.09.005')}
manifest=[];assets={}
for key,paper,page,box,panel,description in rows:
 f=O/'figures'/f'{key}.png'
 if len(sys.argv)==1 or key in sys.argv[1:]:subprocess.run([sys.executable,str(R/'tools/crop_figure.py'),str(D/(paper+'.pdf')),str(page),'--box',*map(str,box),'-o',str(f)],check=True,stdout=subprocess.DEVNULL)
 author,year,doi=refs[paper];caption=f'{author} ({year}), Fig. {panel}. {description}.'
 # Extended-data panels retain the exact published identifier.
 if panel.startswith('Extended Data '):caption=f'{author} ({year}), Fig. {panel.replace("Extended Data ","")} (Extended Data). {description}.'
 assets[key]={'kind':'article','path':'figures/'+key+'.png','caption':caption,'source_url':'https://doi.org/'+doi,'paper':paper,'source_color':key not in ['p_cilia','p_colloblast','k_em','k_loss','b_vesicles','j_synapse']}
 manifest.append({'key':key,'pdf':str(D/(paper+'.pdf')),'page':page,'box':box,'output':str(f),'panel':panel})
(O/'crops.json').write_text(json.dumps(manifest,indent=2)+'\n');(O/'figure_sources.json').write_text(json.dumps(assets,indent=2)+'\n')
