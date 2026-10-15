from pathlib import Path
import json
R=Path('/workspace/NEUROETHOLOGY/lectures/L104C')
items=[
('MDMA increases social approach in octopuses','Octopus bimaculoides','10.1016/j.cub.2018.07.061',4),
('Social contact includes a change in exploratory touch','Octopus bimaculoides','10.1016/j.cub.2018.07.061',3),
('The octopus serotonin transporter retains a drug target','Octopus bimaculoides','10.1016/j.cub.2018.07.061',2),
('Caffeine strengthens honeybee odor memory','Apis mellifera','10.1126/science.1228806',2),
('Kenyon-cell responses link caffeine to learned value','Apis mellifera','10.1126/science.1228806',3),
('High caffeine concentrations trigger rejection','Apis mellifera','10.1126/science.1228806',4),
('Repeated cocaine changes honeybee responsiveness','Apis mellifera','10.1371/journal.pone.0064920',1),
('Nicotine alters bumblebee choices between flowers','Bombus terrestris','10.1038/s41598-017-01980-1',1),
('Nicotine changes acquisition of floral associations','Bombus terrestris','10.1038/s41598-017-01980-1',2),
('A learned flower preference persists after reversal','Bombus terrestris','10.1038/s41598-017-01980-1',3),
('Ant foraging separates learning from running speed','Linepithema humile','10.1016/j.isci.2024.109935',1),
('Caffeine concentration changes foodward routes','Linepithema humile','10.1016/j.isci.2024.109935',2),
('Repeated journeys change reward-finding time','Linepithema humile','10.1016/j.isci.2024.109935',3),
('Nestward and foodward journeys respond differently','Linepithema humile','10.1016/j.isci.2024.109935',4),
('Oriental hornets tolerate unusually strong ethanol','Vespa orientalis','10.1073/pnas.2410874121',1),
('Ethanol tolerance includes rapid metabolic handling','Vespa orientalis','10.1073/pnas.2410874121',2),
('Tree frogs learn associations with amphetamine','Hyla cinerea','10.1159/000314901',3),
('Place conditioning measures a learned context choice','Hyla cinerea','10.1159/000314901',2),
('Locomotor effects and conditioned preference differ','Hyla cinerea','10.1159/000314901',4),
('Ethanol sensitivity depends on dopamine signaling','Caenorhabditis elegans','10.1371/journal.pgen.1009346',1),
('DOP-2 loss changes the movement response to ethanol','Caenorhabditis elegans','10.1371/journal.pgen.1009346',2),
('PDE neurons contribute to ethanol-dependent sedation','Caenorhabditis elegans','10.1371/journal.pgen.1009346',3),
('Dopamine and ethanol interact within a motor circuit','Caenorhabditis elegans','10.1371/journal.pgen.1009346',4),
('Neuropeptide signaling changes motor output','Caenorhabditis elegans','10.1371/journal.pgen.1009346',6),
('Dopamine neurons recruit ethanol-stimulated walking','Drosophila melanogaster','10.1371/journal.pone.0009954',1),
('DopR function links a brain target to intoxication','Drosophila melanogaster','10.1371/journal.pone.0009954',4),
('Repeated ethanol exposure changes fly courtship','Drosophila melanogaster','10.1371/journal.pone.0001391',2),
('Genetic background modifies ethanol disinhibition','Drosophila melanogaster','10.1371/journal.pone.0001391',4),
('A first ethanol experience leaves a neural memory','Drosophila melanogaster','10.1371/journal.pgen.1011582',1),
('GABA circuits distinguish forms of ethanol tolerance','Drosophila melanogaster','10.1371/journal.pgen.1011582',4),
('Zebrafish can obtain an opioid through their actions','Danio rerio','10.1172/jci143990',1),
('Drug seeking can change without suppressing all behavior','Danio rerio','10.1172/jci143990',2),
('Nicotine produces a concentration-dependent response','Danio rerio','10.1073/pnas.0908247106',1),
('Repeated nicotine exposure changes later responsiveness','Danio rerio','10.1073/pnas.0908247106',1),
('A genetic screen separates nicotine-response pathways','Danio rerio','10.1073/pnas.0908247106',3),
('GABA-B signaling contributes to nicotine responses','Danio rerio','10.1073/pnas.0908247106',4),
('A partner’s drinking changes the vole social context','Microtus ochrogaster','10.3389/fpsyt.2017.00226',1),
('Discordant alcohol intake alters partner preference','Microtus ochrogaster','10.3389/fpsyt.2017.00226',2),
('Alcohol affects different social behaviors differently','Microtus ochrogaster','10.3389/fpsyt.2017.00226',3),
('Social rank influences reinstatement in macaques','Macaca fascicularis','10.3389/fnbeh.2026.1770940',2),
('Nicotine changes cocaine-related responding by sex','Macaca fascicularis','10.3389/fnbeh.2026.1770940',4),
('A single intoxication changes neuronal organization','Mus musculus','10.1073/pnas.2122477119',2),
('Ethanol increases mitochondrial mobility in axons','Mus musculus','10.1073/pnas.2122477119',4),
('Vesicle transport provides a distinct cellular comparison','Mus musculus','10.1073/pnas.2122477119',4),
]
assert len(items)==44
rows=[{'slide':i+2,'title':t,'animal':a,'doi':d,'provisional_figure':f,'status':'Source reading and exact panel selection required before final slide text'} for i,(t,a,d,f) in enumerate(items)]
plan={'lecture':'104C','total_slides':46,'title':'Animals on drugs: psychoactive substances, altered perception, drug-seeking and self-administration, and how social environments influence reward and addiction.','date':'Date TBD','animals':sorted(set(a for t,a,d,f in items)),'content_slides':rows,'video_target':20,'additional_credited_image_target':30,'status':'Preparation only. Not a completed lecture or validated PPTX.'}
R.joinpath('slide_plan.json').write_text(json.dumps(plan,indent=2,ensure_ascii=False)+'\n')
lines=['# Lecture 104C: comparative slide map','',f"{len(plan['animals'])} species across 44 content slides. One title slide and one Key takeaways slide bring the planned total to 46.",'','Status: source preparation; not a finished deck. Exact panel choices and all teaching text require source and layout validation.','']
for r in rows:lines.append(f"{r['slide']}. **{r['title']}** · _{r['animal']}_ · https://doi.org/{r['doi']}")
R.joinpath('SLIDE_PLAN.md').write_text('\n'.join(lines)+'\n')
# Retain only the selected references in the compact verification manifest.
cand=json.loads(R.joinpath('reference_verification.json').read_text());selected={d:cand[d] for d in {x[2] for x in items} if d in cand}
P=Path('/workspace/scratch/L104C');m=json.loads((P/'Monkey2026.json').read_text())['resultList']['result'][0];selected[m['doi'].lower()]=m
R.joinpath('reference_verification.json').write_text(json.dumps(selected,indent=2,ensure_ascii=False)+'\n')
print(len(rows),'content slides;',len(plan['animals']),'species;',len(selected),'indexed references')
