from pathlib import Path
import fitz,json,subprocess,re,xml.etree.ElementTree as E
B=Path(__file__).resolve().parent;(B/'figures').mkdir(exist_ok=True)
S={'fish':('science.aav4632.pdf','Musilova et al. (2019)','10.1126/science.aav4632'),'dragon':('11079412.pdf','Douglas et al. (2000)','10.1098/rstb.2000.0681'),'eyes':('rstb.2016.0069.pdf','Thomas et al. (2017)','10.1098/rstb.2016.0069'),'humboldt':(next((B/'papers').glob('burford*.pdf')).name,'Burford & Robison (2020)','10.1073/pnas.1920875117'),'vampire':('rspb20121357.pdf','Hoving & Robison (2012)','10.1098/rspb.2012.1357'),'vent':('PMC12221356.pdf','Nagata et al. (2025)','10.1016/j.jbc.2025.110291'),'pelagic':('PMC11814407.pdf','DeLeo & Bracken-Grissom (2025)','10.1038/s42003-025-07450-z'),'worm':('PMC11730519.pdf','Yan et al. (2025)','10.1186/s12915-025-02112-2'),'octopus':('PMC10291714.pdf','Golikov et al. (2023)','10.1098/rspb.2023.0640'),'stars':('PMC10295343.pdf','Stuckless et al. (2023)','10.3390/biology12060774'),'signals':('PMC3996283.pdf','Davis et al. (2014)','10.1007/s00227-014-2406-x')}
assets={};crops=[]
def crop(key,fn,page,box,num):
 d=fitz.open(B/'papers'/fn);r=d[page-1].rect;frac=[box[0]/r.width,box[1]/r.height,box[2]/r.width,box[3]/r.height];out=B/'figures'/(key+'.png')
 subprocess.run(['python','tools/crop_figure.py',str(B/'papers'/fn),str(page),'--box',*map(str,frac),'-o',str(out)],cwd=B.parents[1],check=True,stdout=subprocess.DEVNULL)
 crops.append({'pdf':fn,'page':page,'box':frac,'out':str(out.relative_to(B)),'figure':num});return str(out.relative_to(B))
for k,(fn,author,doi)in S.items():
 d=fitz.open(B/'papers'/fn);rows=[]
 if k=='fish':boxes=[(2,(30,50,550,655),1),(3,(34,43,525,382),2),(4,(36,44,545,650),3)]
 elif k=='dragon':boxes=[(3,(42,48,280,519),2)]
 else:
  boxes=[];n=0
  for i,p in enumerate(d):
   ims=[fitz.Rect(x['bbox'])for x in p.get_image_info()if x['bbox'][2]-x['bbox'][0]>90 and x['bbox'][3]-x['bbox'][1]>55]
   if not ims:continue
   r=ims[0]
   for x in ims[1:]:r|=x
   if k=='worm' and i+1 in [5,7,8]:continue
   n+=1
   matches=re.findall(r'(?:Figure|Fig\.)\s*(\d+)[\.:]',p.get_text())
   num=int(matches[-1])if matches else n
   boxes.append((i+1,tuple(r),num))
 for i,(page,box,num)in enumerate(boxes):rows.append({'path':crop(k+'_'+str(i+1),fn,page,box,num),'caption':f'{author}, Fig. {num}. Published evidence from the original study.','source_url':'https://doi.org/'+doi,'kind':'article'})
 assets[k]=rows
assets['title']={'path':crop('title_vampire',S['vampire'][0],3,(62.3,189.2,290.7,318.3),'1b'),'caption':'Hoving & Robison (2012), Fig. 1(b). Vampire squid with a retrieved feeding filament.','source_url':'https://doi.org/10.1098/rspb.2012.1357','kind':'article'}
(B/'assets.json').write_text(json.dumps(assets,indent=2));(B/'crops.json').write_text(json.dumps(crops,indent=2));print({k:len(v)for k,v in assets.items()if isinstance(v,list)})
