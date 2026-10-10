import json,re,sys,hashlib
from pathlib import Path
D=Path(__file__).resolve().parent;R=D.parents[1];Q=D
refs={
'shahaf':'Shahaf G; Marom S (2001). Learning in networks of cortical neurons. Journal of Neuroscience 21(22):8782–8788. https://doi.org/10.1523/JNEUROSCI.21-22-08782.2001',
'pong':'Kagan BJ; Kitchen AC; Tran NT; Habibollahi F; Khajehnejad M; Parker BJ; Bhat A; Rollo B; Razi A; Friston KJ (2022). In vitro neurons learn and exhibit sentience when embodied in a simulated game-world. Neuron 110(23):3952–3969.e8. https://doi.org/10.1016/j.neuron.2022.09.001',
'drug':'Watmuff B; Habibollahi F; Desouza C; Khajehnejad M; Loeffler A; Baranes K; Poulin N; Kotter M; Kagan BJ (2025). Drug treatment alters performance in a neural microphysiological system of information processing. Communications Biology 8:916. https://doi.org/10.1038/s42003-025-08194-6',
'efficiency':'Khajehnejad M; Habibollahi F; Loeffler A; Paul A; Razi A; Kagan BJ (2025). Dynamic Network Plasticity and Sample Efficiency in Biological Neural Cultures: A Comparative Study with Deep Reinforcement Learning. Cyborg and Bionic Systems 6:0336. https://doi.org/10.34133/cbsystems.0336',
'brainoware':'Cai H; Ao Z; Tian C; Wu Z; Liu H; Tchieu J; Gu M; Mackie K; Guo F (2023). Brain organoid reservoir computing for artificial intelligence. Nature Electronics 6(12):1032–1039. https://doi.org/10.1038/s41928-023-01069-w',
'ethics':'Milford SR; Shaw D; Starke G (2023). Playing Brains: The Ethical Challenges Posed by Silicon Sentience and Hybrid Intelligence in DishBrain. Science and Engineering Ethics 29(6):38. https://doi.org/10.1007/s11948-023-00457-x',
'framework':'Sellar EP; Rouleau N (2026). A cybernetic framework for synthetic biological intelligence in the era of neural tissue engineering. npj Unconventional Computing 3:31. https://doi.org/10.1038/s44335-026-00077-1'}
short={'shahaf':'Shahaf & Marom (2001)','pong':'Kagan et al. (2022)','drug':'Watmuff et al. (2025)','efficiency':'Khajehnejad et al. (2025)','brainoware':'Cai et al. (2023)','ethics':'Milford et al. (2023)','framework':'Sellar & Rouleau (2026)'}
c=json.loads((D/'crops.json').read_text());slides=[]
def fig(name,panel,cap):
 k=c['crops'][name][0];return {'kind':'article','path':f'figures/{name}.png','caption':short[k]+f', Fig. {panel}. {cap}.','source_url':refs[k].split()[-1]}
for block in (Q/'content.txt').read_text().strip().split('\n\n'):
 lines=block.splitlines();head=lines[0].split('|');title,keys,name,panel,cap=head[:5];keys=keys.split(',');body=lines[1:];assert len(body)==3
 x={'layout':'text' if name=='text' else 'figure-right','title':title,'body':body,'transcript':[re.sub(r'\*\*','',p) for p in body],'cite':'; '.join(short[k] for k in keys),'refs':[refs[k] for k in keys]}
 if name!='text':x['figure']=fig(name,panel,cap)
 if len(head)>5:
  x['layout']='figures-right';x['figures']=[x.pop('figure'),fig(head[5],'3D' if head[5]=='b3d' else '1A–B','Classification accuracy across training epochs' if head[5]=='b3d' else 'Differentiation and neuronal tissue markers')];x['primary_figure_height']=2.45 if head[5]=='d1b' else 2.7;x['figure_width']=5.8
 slides.append(x)
assert len(slides)==44
for i,x in enumerate(slides,2):
 if len(x['title'])>62:print('Long title',i,len(x['title']),x['title'])
items=[('Contingent feedback','Stopping stimulation after a selected response can increase that response, and Pong learning depends on how action changes subsequent input.'),('Sensory and action codes','Electrode location and pulse rate encode ball information; opposing output activity controls paddle movement through an electronic decoder.'),('Network state','Adaptive output involves population coordination, and high-dose carbamazepine improves gameplay in the tested hyperactive NGN2 preparation.'),('Reservoir computation','Brainoware combines nonlinear, fading neural responses with trained electronic readouts for speech classification and time-series prediction.'),('Comparative performance','Sample efficiency depends on the experience budget, input representation, action mapping, and algorithm used in the comparison.'),('Sentience and welfare','Adaptive performance and subjective experience require different evidence; welfare proposals state their assumptions about experience and suffering.')]
spec={'lecture':72,'theme':'slate-indigo-paper','content_slides':44,'title_height':2.7,'title_image':fig('p2b','2B','Human cortical neurons used in DishBrain'),'title_refs':[refs['pong']],'slides':slides,'takeaways':{'items':[{'lead':a,'text':b} for a,b in items],'cite':'Kagan et al. (2022); Cai et al. (2023); Watmuff et al. (2025); Milford et al. (2023)','refs':list(refs.values())}}
(D/'lecture.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n');(D/'REFERENCES.md').write_text('# Lecture 72 sources\n\n'+'\n\n'.join(refs.values())+'\n\nThe first five sources report primary experiments. Milford et al. is an ethical analysis; Sellar and Rouleau is a perspective. The latter mentions Doom without supplying a primary Doom protocol or performance dataset. All seven full PDFs were obtained and checked before writing and cropping.\n')
p=R/'course/themes.json';themes=json.loads(p.read_text());themes['palettes']['slate-indigo-paper']={'label':'slate indigo / paper white','title_bg':'58677E','title_text':'FFFFFF','title_muted':'E0E5EC','bg':'FFFFFF','heading':'394352','text':'000000','muted':'000000','tint':'F1F3F6','accent':'58677E','rule':'CCD3DD'};p.write_text(json.dumps(themes,ensure_ascii=False,indent=2)+'\n')
print('Content word counts',min(len(' '.join(x['body']).split()) for x in slides),max(len(' '.join(x['body']).split()) for x in slides))
