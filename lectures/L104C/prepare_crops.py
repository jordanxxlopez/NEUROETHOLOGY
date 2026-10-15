from pathlib import Path
import fitz,json
R=Path('/workspace/NEUROETHOLOGY/lectures/L104C');P=Path('/workspace/scratch/L104C/downloads')
sel={'OctopusMDMA2':('10.1016/j.cub.2018.07.061',{15:1,16:2,17:3,18:4}),'AntCaffeine':('10.1016/j.isci.2024.109935',{3:1,4:2,5:3,6:4,7:5}),'BumblebeeNicotine':('10.1038/s41598-017-01980-1',{2:1,3:2,4:3,5:4}),'BeeCaffeine2':('10.1126/science.1228806',{5:1,6:2,7:3,8:4}),'FishNicotine':('10.1073/pnas.0908247106',{2:1,4:3,5:4})}
crops={};papers={};provenance=[]
for key,(doi,pages) in sel.items():
 papers[key]='papers/'+key+'.pdf';d=fitz.open(P/(key+'.pdf'))
 for page,num in pages.items():
  p=d[page-1];im=[x for x in p.get_image_info() if x['width']>=200 and x['height']>=200 and (x['bbox'][2]-x['bbox'][0])>100];assert im,(key,page)
  im=max(im,key=lambda x:(x['bbox'][2]-x['bbox'][0])*(x['bbox'][3]-x['bbox'][1]));b=im['bbox'];rect=[max(0,(b[0]-2)/p.rect.width),max(0,(b[1]-2)/p.rect.height),min(1,(b[2]+2)/p.rect.width),min(1,(b[3]+2)/p.rect.height)];name=key+'_Fig'+str(num);crops[name]=[key,page,rect];provenance.append({'path':'figures/'+name+'.png','article_doi':doi,'figure':num,'source_pdf':papers[key],'page':page,'crop_box':rect,'status':'Original article figure; visual crop review pending'})
papers['Frog']='papers/Frog.pdf'
for num,page in [(3,5),(4,6)]:
 name='Frog_Fig'+str(num);crops[name]=['Frog',page,[.08,.05,.50,.315]];provenance.append({'path':'figures/'+name+'.png','article_doi':'10.1159/000314901','figure':num,'source_pdf':papers['Frog'],'page':page,'status':'Vector figure crop; visual review pending'})
R.joinpath('crops.json').write_text(json.dumps({'papers':papers,'dpi':200,'crops':crops},indent=2)+'\n');R.joinpath('figure_sources.json').write_text(json.dumps(provenance,indent=2)+'\n');print(len(crops),'source figure crops queued')
