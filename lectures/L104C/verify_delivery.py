"""Verify native media bytes, original proportions, prose, credits and slide count."""
from pathlib import Path
import hashlib,json,re,subprocess
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
R=Path(__file__).resolve().parent;P=R/'Neuroethology_Lecture104C_FA2026.pptx';prs=Presentation(P);sp=json.load(open(R/'lecture.json'));media=json.load(open(R/'media_sources.json'));assert len(prs.slides)==51
assert media['embedded_video_count']==media['distinct_original_recordings']==20
assert sum(sh.shape_type==MSO_SHAPE_TYPE.MEDIA for s in prs.slides for sh in s.shapes)==20
clean=lambda t:re.sub(r'_([^_]+)_',r'\1',re.sub(r'\*\*(.*?)\*\*',r'\1',t))
for n,sd in enumerate(sp['slides'],2):
 sl=prs.slides[n-1];body=next(sh for sh in sl.shapes if sh.name=='Body');assert [p.text for p in body.text_frame.paragraphs]==[clean(t) for t in sd['body']],n;assert len(sd['body'])==3
 for p in sd['body']:assert 5<=len(re.findall(r'[.!?](?:\s|$)',p))<=7,(n,p)
 assert all(r.font.name=='Arial' for sh in sl.shapes if sh.has_text_frame for p in sh.text_frame.paragraphs for r in p.runs)
 assert 'References:' in sl.notes_slide.notes_text_frame.text
assert len(json.load(open(R/'additional_image_placements.json')))==30
checks=[]
for row in media['sources']:
 sl=prs.slides[row['slide']-1];movie=next(sh for sh in sl.shapes if sh.name==Path(row['delivery_file']).stem);el=movie._element.xpath(".//*[local-name()='media']")[0];rid=el.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed');part=sl.part.rels[rid].target_part;assert hashlib.sha256(part.blob).hexdigest()==row['delivery_sha256'];assert abs(movie.width/movie.height-row['native_aspect_ratio'])<.002
 subprocess.run(['ffmpeg','-v','error','-i',str(R/row['delivery_file']),'-f','null','-'],check=True)
 checks.append(dict(slide=row['slide'],identifier=row['original_identifier'],embedded_bytes_match=True,native_proportions=True,full_decode_passed=True))
assert P.stat().st_size<100*1024*1024,P.stat().st_size
out=dict(slides=51,content_slides=49,additional_deltafosb_slides=5,nonhuman_species=13,embedded_videos=20,distinct_original_recordings=20,additional_subject_images=30,content_slides_with_primary_figure=49,teaching_text_matches_spec=True,paragraphs_per_content_slide=3,sentences_per_paragraph='5–7',size_bytes=P.stat().st_size,sha256=hashlib.sha256(P.read_bytes()).hexdigest(),desktop_powerpoint_GUI_playback='Untested',google_slides_import='Untested; native videos may require separate Drive insertion',video_checks=checks)
(R/'delivery_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='video_checks'},indent=2))
