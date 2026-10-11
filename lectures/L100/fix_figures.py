from pathlib import Path
import json,subprocess
B=Path('lectures/L100');a=json.load(open(B/'assets.json'));s=json.load(open(B/'lecture.json'))
def crop(fn,page,box,name):
 out=B/'figures'/name;subprocess.run(['python','tools/crop_figure.py',str(B/'papers'/fn),str(page),'--box',*map(str,box),'-o',str(out)],check=True,stdout=subprocess.DEVNULL);return str(out.relative_to(B))
# Figure 3 is the filament histology, rather than Figure 4's ingested material.
f={'path':crop('rspb20121357.pdf',4,[.496,.067,.879,.680],'vampire_filament_fig3.png'),'kind':'article','source_url':'https://doi.org/10.1098/rspb.2012.1357','caption':'Hoving & Robison (2012), Fig. 3. Filament hairs and sensory-cell morphology.'};s['slides'][22]['figure']=f
f={'path':crop('rstb.2016.0069.pdf',7,[.235,.047,.763,.678],'eyes_optics_fig5.png'),'kind':'article','source_url':'https://doi.org/10.1098/rstb.2016.0069','caption':'Thomas et al. (2017), Fig. 5. Sighting distance depends on aperture, depth and target type.'};s['slides'][14]['figure']=f
f={'path':crop('PMC11730519.pdf',5,[.103,.100,.902,.515],'worm_visual_fig2.png'),'kind':'article','source_url':'https://doi.org/10.1186/s12915-025-02112-2','caption':'Yan et al. (2025), Fig. 2. Anterior anatomy and loss of vision-associated genes.'};s['slides'][31]['figure']=f
f=dict(a['worm'][2]);f['caption']='Yan et al. (2025), Fig. 6. Chemosensory ionotropic receptor IR25a conservation.';s['slides'][32]['figure']=f
# Published physiological results receive matching captions, not generic image descriptions.
s['slides'][26]['figure']['caption']='Nagata et al. (2025), Fig. 4. Absorption spectra of four shrimp opsins.'
s['slides'][28]['figure']['caption']='Nagata et al. (2025), Fig. 2. Light-dependent calcium and cyclic AMP responses.'
for q in s['slides']:q['transcript']=[x.replace('**','').replace('_','')for x in q['body']]
(B/'lecture.json').write_text(json.dumps(s,indent=2,ensure_ascii=False)+'\n');(B/'fix_figures.py').write_text(Path(__file__).read_text())

# Use the animal photograph, not the sampling map, for octopod posture.
import json
from pathlib import Path
p=Path("lectures/L100/lecture.json");s=json.loads(p.read_text());s["slides"][33]["figure"]={"path":"figures/octopus_2.png","caption":"Golikov et al. (2023), Fig. 2. Cirroteuthis muelleri posture and bottom interactions.","source_url":"https://doi.org/10.1098/rspb.2023.0640","kind":"article"};p.write_text(json.dumps(s,indent=2,ensure_ascii=False)+"\n")

p=Path("lectures/L100/lecture.json");s=json.loads(p.read_text());s["slides"][43]["figure"]["caption"]="Golikov et al. (2023), Fig. 1. Locations of Arctic octopod observations.";s["slides"][36]["figure"]["caption"]="Golikov et al. (2023), Fig. 4. Seafloor traces of octopod bottom activity.";p.write_text(json.dumps(s,indent=2,ensure_ascii=False)+"\n")
