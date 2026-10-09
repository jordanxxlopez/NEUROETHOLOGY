import json,re
from pathlib import Path
H=Path(__file__).resolve().parent;ROOT=H.parents[1]
research=json.loads((H/'research.json').read_text());R={}
for s in research['sources']:
 k=s['id'];a=s['authors'];year=str(s['year'])+('a'if k=='varicosities88'else'b'if k=='contacts88'else'');surname=a[0].split()[0];label=surname+(' et al.'if len(a)>2 else' & '+a[1].split()[0]if len(a)==2 else'')+' ('+year+')';ref=s['reference'].replace('('+str(s['year'])+')','('+year+')');R[k]={'ref':ref,'cite':label,'doi':'https://doi.org/'+s['doi']}
F={}
def fig(name,k,n,d):F[name]={'path':'figures/'+name+'.png','kind':'article','source_url':R[k]['doi'],'caption':R[k]['cite']+', Fig. '+n+'. '+d,'paper_key':k}
for name,n,d in [('p1','1(A–C)','Gill, siphon, recording preparation, and stimulus-intensity responses.'),('p2','2(A–B)','Withdrawal habituation, dishabituation, and recovery after rest.'),('p3','3(A–B)','Repeated-stimulation decrement and recovery of gill withdrawal.')]:fig(name,'pinsker70',n,d)
for name,n,d in [('c1','1(A–B)','Receptive skin, isolated ganglion, and motor-cell potentials.'),('c2','2(A–D)','Elementary EPSP decrement, recovery, and connective-induced facilitation.')]:fig(name,'castellucci70',n,d)
for name,n,d in [('a1','1(A–B)','Siphon, ganglia, and behavioral training protocols.'),('a4','4(A–B)','Motor-cell firing compared with siphon withdrawal.'),('a6','6(A–C)','Withdrawal, motor activity, and sensory activity during training.')]:fig(name,'behavior99',n,d)
fig('q2','quantal74','2','Small successful EPSPs and failures during depression.');fig('q3','quantal74','3(E1–2)','Averaged successful EPSPs retain similar waveforms during depression.')
fig('s2','silencing02','2(A–D)','Empirical depression and paired-pulse responses at strong and weak connections.');fig('s10','silencing02','13(A–B)','Persistence of depression after 40 min or 100 s of rest.')
fig('h1','carew72','1(A–C)','Training and retention of withdrawal habituation over three weeks.');fig('h2','carew72','2(A–B)','Matched trial totals with spaced versus massed training.')
fig('b2','varicosities88','2','Reconstructed sensory-neuron arbors in sensitized animals and controls.');fig('contact','contacts88','1(A–C)','Electron micrographs of labeled contacts onto gill motor-cell processes.');fig('f2','frost85','2(A–B)','Sensory–motor EPSPs after long-term sensitization training.')
fig('br1','brunelli76','1(A–B)','Serotonin facilitates EPSPs; cinanserin reduces connective-induced facilitation.');fig('br2','brunelli76','2(B)','Intracellular cAMP enhances transmission relative to injection controls.')
for name,n,d in [('k1','1(A–C)','PKA anchoring disruption and short- versus long-term facilitation.'),('k5','5(A–D)','RII protein levels in terminal fractions and sensory neurons.'),('k7','7(A–D)','RII antisense impairs expression and long-term facilitation.')]:fig(name,'pka04',n,d)
fig('g2','glutamate93','2(A–C)','Voltage-dependent currents evoked by sensory spikes and applied glutamate.')
for name,n,d in [('l1','1(A–B)','Postsynaptic calcium buffering reduces serotonin facilitation.'),('l2','2(A–B)','Postsynaptic IP3-receptor intervention and EPSPs.'),('l5','5(A–B)','Postsynaptic botulinum toxin affects persistent EPSP enhancement.'),('l9','9(A–D)','Reduced withdrawal preparation and motor-cell intervention during dishabituation.')]:fig(name,'postsynaptic05',n,d)
for name,n,d in [('mo1','1(A–C)','Repeated serotonin and macromolecular-synthesis interventions.'),('mo2','2(A–C)','Short-term facilitation persists during synthesis inhibition.'),('mo4','4(A–C)','Timing of synthesis inhibition relative to long-term facilitation.')]:fig(name,'montarolo86',n,d)
for name,n,d in [('t2','2(A–B)','Synapsin immunostaining in sensory-neuron varicosities.'),('t4','4(A–B)','Serotonin increases synapsin-promoter-driven reporter expression.'),('t5','5(A–B)','CREB binding and histone-related assays at the synapsin promoter.'),('t7','7(A–B)','Synapsin siRNA impairs the 24 h facilitation response.')]:fig(name,'synapsin11',n,d)
for name,n,d in [('u2','2(a–c)','Local reporter responses in sensory-neuron processes.'),('u4','4(a–d)','ApCPEB4 knockdown and overexpression alter facilitation.'),('u5','5(a–c)','Phosphorylation assays and mutated ApCPEB4 intervention.')]:fig(name,'cpeb16',n,d)
fig('nt4','neurotrophin13','4(A–E)','ApNT isoform processing and localization in cultured neurons.');fig('nt6','neurotrophin13','6(A–D)','ApNT-dependent enhancement and growth of neuronal varicosities.');fig('ntcell','neurotrophin13','4(E)','Published fluorescence images of ApNT-tagged neuronal cells and processes.')
fig('z1','creb15','1(A–B)','Recorded EPSPs after CREB1 knockdown or control RNA.');fig('z6','creb15','6(A–B)','Empirical EPSPs after rescue training and rolipram intervention.')
fig('r3','reinstatement14','3(A–C)','Repeated imaging of sensory–motor cocultures and changing varicosities.');fig('r8','reinstatement14','8(A–B)','Withdrawal sensitization after disruption and abbreviated retraining.');fig('e7','epigenetic17','7(A–B)','Consolidated sensitization and delayed methyltransferase inhibition.')
fig('r3a','reinstatement14','3(A)','Fluorescent sensory–motor coculture at 0, 24, and 48 hr; original 20 µm scale bar retained.')
slides=[]
for i,chunk in enumerate((H/'content.txt').read_text().strip().split('\n---\n'),1):
 lines=chunk.splitlines();title,keys,im=lines[0].split('|');body=lines[1:];ks=keys.split('+');assert len(body)==3 and len(title)<=62
 anatomy='p1'if i in [2,3,4,13,14,43,44] else'r3a'if i in [5,6,7,8,9,10,11,12,16,17,18,19,22,23,24,25,26,27,28,29,34,40,41] else None
 if i in [7,8,26]:anatomy='a1'
 fs=[dict(F[im])]+([dict(F[anatomy])]if anatomy else[]);ks=list(dict.fromkeys(ks+[x.pop('paper_key')for x in fs]));sl={'layout':('figures-right'if i%2 else'figures-left')if anatomy else('figure-right'if i%2 else'figure-left'),'title':title,'body':body,'cite':'; '.join(R[k]['cite']for k in ks),'refs':[R[k]['ref']for k in ks],'transcript':[re.sub(r'\*\*|_', '',x)for x in body]}
 if anatomy:sl.update(figures=fs,primary_figure_height=3.3)
 else:sl['figure']=fs[0]
 slides.append(sl)
assert len(slides)==44
spec={'lecture':36,'theme':'pearl-bordeaux','content_slides':44,'title_image':{'path':'figures/aplysia.jpg','kind':'web','caption':'Photo: Aplysia californica, the California sea hare.','credit':'Jeff Young','license':'CC BY 4.0','source_url':'https://www.inaturalist.org/photos/746343526'},'title_refs':[R[k]['ref']for k in ['pinsker70','castellucci70','brunelli76','montarolo86']],'slides':slides,'takeaways':{'title':'Key takeaways','cite':'Castellucci & Kandel (1974); Brunelli et al. (1976); Montarolo et al. (1986)','items':[
 {'lead':'Behavioral distinctions','text':'Habituation decreases repeated-stimulus responsiveness; sensitization increases responsiveness after strong stimulation; dishabituation restores a habituated response without proving that all depression has reversed.'},
 {'lead':'Presynaptic depression','text':'Short-term habituation reduces transmitter quanta released per sensory impulse; an unchanged unitary postsynaptic response argues against receptor desensitization in the tested preparation.'},
 {'lead':'Modulatory signaling','text':'Serotonin, cAMP, and localized PKA signaling facilitate sensory–motor transmission; release enhancement and postsynaptic calcium-dependent regulation can contribute together.'},
 {'lead':'Persistence requires additional mechanisms','text':'Repeated stimulation recruits lasting facilitation with a restricted requirement for transcription and translation; spacing and synthesis timing affect retention independently of immediate response strength.'},
 {'lead':'Functional and structural plasticity','text':'Long-term training changes sensory-neuron varicosities and contacts; CREB, synapsin, local translation, and neurotrophin signaling contribute under defined protocols without any one accounting for the entire memory.'},
 {'lead':'Expression is not storage by itself','text':'Lost withdrawal enhancement or synaptic growth does not prove complete memory erasure; retraining, cellular interventions, and appropriate controls distinguish latent experience from current performance.'}],'refs':[R[k]['ref']for k in ['pinsker70','quantal74','silencing02','brunelli76','pka04','postsynaptic05','montarolo86','carew72','synapsin11','reinstatement14','epigenetic17']]}}
(H/'lecture.json').write_text(json.dumps(spec,indent=2,ensure_ascii=False)+'\n')
p=ROOT/'course/themes.json';themes=json.loads(p.read_text());themes['palettes']['pearl-bordeaux']={'label':'pearl / muted deep red','title_bg':'EDE5E6','title_text':'60353B','title_muted':'77575D','bg':'FFFFFF','heading':'60353B','text':'000000','muted':'000000','tint':'F7F1F2','accent':'95656C','rule':'DFCFD2'};p.write_text(json.dumps(themes,indent=2)+'\n')
print('Lecture 36: 44 source-based content slides; three full paragraphs each.')
