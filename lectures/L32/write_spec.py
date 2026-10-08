import json,re
from pathlib import Path
H=Path(__file__).resolve().parent;ROOT=H.parents[1]
R={}
for p in (H/'sources').glob('*-crossref.json'):
 k=p.name.removesuffix('-crossref.json');j=json.loads(p.read_text());year=str(j['published']['date-parts'][0][0])+('a' if k=='dopamine10' else 'b' if k=='anatomy09' else '');authors=j['author'];a=', '.join(x['family']+' '+''.join(s[0] for s in re.findall(r'\w+',x.get('given',''))) for x in authors);title=re.sub('<[^>]+>','',j['title'][0]);journal=j['container-title'][0];volume=j.get('volume','');issue='('+j['issue']+')' if j.get('issue')else'';pages=j.get('page',j.get('article-number',''))
 R[k]={'ref':f'{a} ({year}). {title}. {journal} {volume}{issue}:{pages}. https://doi.org/{j["DOI"]}','doi':'https://doi.org/'+j['DOI'],'cite':authors[0]['family']+(' et al.' if len(authors)>2 else ' & '+authors[1]['family']if len(authors)==2 else '')+f' ({year})'}
F={}
def fig(name,k,num,description):F[name]={'path':f'figures/{name}.png','caption':f'{R[k]["cite"]}, Fig. {num}. {description}','source_url':R[k]['doi'],'kind':'article','paper_key':k}
for name,n,desc in [('m1','1(a–f)','Targeted labeling and single-cell filling in HVC.'),('m2','2(a–f)','Identified RA- and X-projecting HVC neurons.'),('m3','3','Dendritic arbors grouped by projection target.'),('m4','4(a–d)','Spatial distribution and size of HVC dendrites.'),('m5','5(a–d)','Axonal boutons and their spatial density.'),('m6','6','Local axons of RA-projecting HVC neurons.'),('m7','7','Local axons of X-projecting HVC neurons.'),('m8','8','Two dual-projecting HVC neurons.'),('m9','9(a–c)','Processes extending from HVC into the shelf.'),('m10','10(a–d)','Local axonal distributions within HVC.'),('m11','11(a–d)','Local and broadcast axonal territories.')]:fig(name,'morphology18',n,desc)
for name,n,desc in [('z1','1(a–k)','RA motor anatomy and temperature-dependent spikes.'),('z1a','1(a)','RA and descending vocal motor pathways.'),('z2','2(a–j)','RA sodium-subunit expression and resurgent current.'),('z3','3(a–l)','Developmental sodium-subunit expression in RA.'),('z4','4(a–f)','Developmental increase of resurgent current.'),('z5','5(a–i)','Axonal and voltage-clamp recording controls.'),('z6','6(a–j)','Developmental spike and firing properties.'),('z7','7(a–l)','Native and scrambled Navβ4 peptide interventions.'),('z8','8(a–h)','Current records and dynamic-clamp interventions.'),('z9','9(a–g)','Female RA expression and sodium-current measurements.')]:fig(name,'sodium21',n,desc)
fig('zbrain','sodium21','1(a, upper)','RA and brainstem targets in the vocal motor pathway.')
fig('sy1','syrinx21','1(a–b)','Syrinx muscles and the medial vibratory mass.')
for name,n,desc in [('v1','1(A–D)','Song development and convergent forebrain pathways.'),('v1c','1(C)','HVC, LMAN, and RA in the published pathway map.'),('v2','2(A–E)','Pathway stimulation and currents recorded in RA.'),('v3','3(A–G)','HVC input strengthening and refinement.'),('v4','4(A–H)','LMAN current strength and receptor contributions.'),('v5','5(A–F)','RA firing responses across developmental stages.')]:fig(name,'variability14',n,desc)
for name,n,desc in [('g1','1(A–C)','Anatomy of forebrain-to-midbrain routes.'),('g1a','1(A)','Area X, DLM, LMAN, and midbrain connections.'),('g2','2(A–C)','Auditory responses across three circuit regions.'),('g3','3(A–F)','Self-song selectivity across the recorded populations.'),('g4','4(A–F)','Recorded cell labeling and transmitter-marker staining.'),('g5','5(A–B)','Response dynamics and latencies across regions.'),('g6','6(A–D)','Responses to electrical stimulation of HVC.'),('g7','7(A–D)','Area X receptor blockade and vehicle controls.'),('g8','8(A–H)','Area X drug injections alter midbrain firing.')]:fig(name,'dopamine10',n,desc)
for name,n,desc in [('d1','1(A–D)','Reversible dopamine effects on RA firing and voltage.'),('d2','2(A–D)','Depolarization with and without sodium-channel blockade.'),('d3','3(A–D)','D1-like agonist effects on RA neurons.'),('d4','4(A–D)','D1-like antagonist limits dopamine excitation.'),('d5','5(A–D)','D2-like agonist measurements in RA neurons.')]:fig(name,'dopamine13',n,desc)
for name,n,desc in [('s1','1(A–F)','SK blockade changes evoked firing and spike recovery.'),('s2','2(A–E)','Spontaneous spike timing before and after apamin.'),('s3','3(A–C)','Evoked threshold changes during SK blockade.'),('s4','4(A–E)','Apamin effects after glutamate-receptor blockade.')]:fig(name,'sk12',n,desc)
for name,n,desc in [('n7','7(a–d)','Degeneration staining in the canary song pathway.'),('n11','11','Lesion locations associated with song disruption.'),('n13','13','Canary song before and after a forebrain lesion.')]:fig(name,'nottebohm76',n,desc)
for name,n,desc in [('f1','1','Published anatomical map of the forebrain loop.'),('f2','2(a–b)','Tracer-filled HVC and RA neurons.'),('f3','3(a–e)','Tracer labeling linking LMAN, Area X, and RA.'),('f4','4(a–f)','Injection sites and retrogradely labeled LMAN cells.'),('f5','5(a–b)','Two retrograde labels in LMAN neurons.')]:fig(name,'feedback95',n,desc)
for name,n,desc in [('q2','2(a–c)','LMAN responses to self-song and comparison songs.'),('q4','4(a)','Relative responses to different song stimuli.'),('q5','5(a–d)','Normal, reversed, and isolated-syllable playback.'),('q6','6(a–d)','Responses depend on song and syllable order.'),('q7','7(a–g)','Responses to combinations of song syllables.'),('q9','9(a–d)','Song-selective auditory responses in Area X.')]:fig(name,'doupe97',n,desc)
slides=[]
for i,chunk in enumerate((H/'content.txt').read_text().strip().split('\n---\n'),1):
 lines=chunk.splitlines();title,keys,im=lines[0].split('|');body=lines[1:];ks=keys.split('+');assert len(body)==3
 anatomy=None
 if im.startswith(('z','s','d','v')) and im not in ['z1a','v1c']:anatomy='zbrain' if im.startswith(('z','s','d'))else'v1c'
 if im.startswith('q')or im in ['g4','g8']:anatomy='g1a'
 if im=='n13':anatomy='n11'
 if im=='n7':anatomy='m2'
 if im=='z1a':anatomy='sy1'
 if im in ['z1','z2','z3','z5','z9','v2']:anatomy=None
 if im=='f5':anatomy='f4'
 if anatomy:
  fs=[F[im],F[anatomy]];ks+= [f['paper_key']for f in fs];sl={'layout':'figures-right'if i%2 else'figures-left','figures':fs,'primary_figure_height':3.2}
 else:sl={'layout':'figure-right'if i%2 else'figure-left','figure':F[im]};ks+=[F[im]['paper_key']]
 ks=list(dict.fromkeys(ks));sl.update(title=title,body=body,cite='; '.join(R[k]['cite']for k in ks),refs=[R[k]['ref']for k in ks],transcript=[re.sub(r'\*\*|(?<!\w)_(?!\w)','',x)for x in body]);slides.append(sl)
assert len(slides)==44
for f in F.values():f.pop('paper_key',None)
spec={'lecture':32,'theme':'porcelain-steel','content_slides':44,'title_image':{'path':'figures/zebra-finch.jpg','kind':'web','caption':'Photo: Male and female zebra finches.','credit':'Michael Hains','license':'CC BY-NC 4.0','source_url':'https://www.inaturalist.org/photos/147702462'},'title_refs':[R[k]['ref']for k in ['nottebohm76','bottjer84','morphology18','doupe97']],'slides':slides,'takeaways':{'title':'Key takeaways','cite':'Nottebohm et al. (1976); Bottjer et al. (1984); Doupe (1997)','items':[
 {'lead':'Separate projection pathways','text':'HVC reaches RA directly for vocal motor control and reaches Area X through a distinct output population; DLM and LMAN form the anterior forebrain route back to RA.'},
 {'lead':'Anatomical connections constrain mechanisms','text':'Lesions establish regional necessity, tracers establish projection direction, and single-cell reconstructions reveal local collaterals; none alone specifies the information transmitted at a synapse.'},
 {'lead':'RA integrates different excitatory inputs','text':'HVC and LMAN converge on RA, but their developmental connectivity and receptor contributions differ; stronger, refined HVC input can coexist with persistent LMAN input.'},
 {'lead':'Motor physiology has multiple controls','text':'Resurgent sodium current supports rapid RA firing, while SK channels regulate spike recovery and timing in interaction with synaptic input; dopamine modulates RA excitability through D1-like signaling.'},
 {'lead':'LMAN contributes differently across ages','text':'Early lesions disrupt vocal development, whereas established adult song can persist after lesions; this difference does not imply that adult LMAN becomes anatomically disconnected or functionless.'},
 {'lead':'Auditory selectivity is not an error signal by itself','text':'LMAN, Area X, and dopaminergic circuitry respond selectively to self-song, but anesthetized playback responses do not establish the complete teaching signal or learning rule used during singing.'}],
 'refs':[R[k]['ref']for k in ['nottebohm76','bottjer84','morphology18','variability14','sodium21','sk12','dopamine13','doupe97','dopamine10']]}}
(H/'lecture.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n')
p=ROOT/'course/themes.json';themes=json.loads(p.read_text());themes['palettes']['porcelain-steel']={'label':'porcelain / steel blue','title_bg':'E6EBEF','title_text':'2D4355','title_muted':'52697B','bg':'FFFFFF','heading':'405D72','text':'252E36','muted':'64717D','tint':'F2F5F7','accent':'698498','rule':'CDD8DF'};p.write_text(json.dumps(themes,indent=2)+'\n')
print('44 three-paragraph slides with source figures and full reference notes.')
