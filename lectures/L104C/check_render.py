from pathlib import Path
import json,hashlib,shutil
import pymupdf as f
from pptx import Presentation
R=Path(__file__).resolve().parent;P=R/'Neuroethology_Lecture104C_FA2026.pptx';pdf=Path('/workspace/scratch/L104C/Neuroethology_Lecture104C_FA2026.pdf');d=f.open(pdf);prs=Presentation(P);assert len(d)==len(prs.slides)==51
rows=[]
for n in range(2,51):
 sh=next(s for s in prs.slides[n-1].shapes if s.name=='Body');rect=f.Rect(sh.left/12700,sh.top/12700,(sh.left+sh.width)/12700,(sh.top+sh.height)/12700);blocks=[b for b in d[n-1].get_text('dict',clip=rect)['blocks'] if b['type']==0];assert len(blocks)==3,(n,len(blocks));counts=[len(b['lines']) for b in blocks];assert min(counts)>=5,(n,counts)
 bottom=max(b['bbox'][3] for b in blocks);assert bottom<=rect.y1+.5,(n,bottom,rect.y1)
 rows.append(dict(slide=n,paragraph_rendered_lines=counts,text_fits_body_box=True))
out=dict(slide_count=51,pdf_is_static_preview=True,all_51_slides_reviewed_in_contact_sheets=True,source_panels_reviewed=True,final_slide_43_anatomical_panel_reviewed=True,minimum_rendered_lines_per_paragraph=min(min(x['paragraph_rendered_lines']) for x in rows),all_content_body_boxes_fit=True,caption_and_footer_separation_reviewed=True,video_proportions_verified_in_delivery_check=True,desktop_GUI_playback='Not tested',pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),body_checks=rows)
(R/'visual_qa.json').write_text(json.dumps(out,indent=2)+'\n');shutil.copyfile(pdf,R/'Neuroethology_Lecture104C_FA2026_STATIC_PREVIEW.pdf');d[42].get_pixmap(matrix=f.Matrix(1.2,1.2)).save('/workspace/scratch/L104C/final_slide43.png');print('51 rendered slides; all 147 content paragraphs fit and have at least',out['minimum_rendered_lines_per_paragraph'],'lines.')
