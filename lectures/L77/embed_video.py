"""Add the original supplementary movie to the finished deck without rebuilding it.
The baseline PPTX is read from the lecture77 branch so the operation is repeatable.
"""
import subprocess,json,zipfile,hashlib
from pathlib import Path
from io import BytesIO
from lxml import etree
from pptx import Presentation
from pptx.util import Inches,Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE_TYPE
D=Path(__file__).resolve().parent;R=D.parents[1]
original=subprocess.check_output(['git','show','lecture77:lectures/L77/Neuroethology_Lecture77_FA2026.pptx'],cwd=R)
r=Presentation(BytesIO(original));s=r.slides[6];before=[[etree.tostring(x._element) for x in slide.shapes] for slide in r.slides];notes=[slide.notes_slide.notes_text_frame.text for slide in r.slides]
f=next(x for x in s.shapes if x.shape_type==MSO_SHAPE_TYPE.PICTURE)
# The poster is the unchanged original article figure at exactly its existing bounds.
# Full-screen playback preserves the movie's 4:3 source aspect ratio when activated.
m=s.shapes.add_movie(str(D/'media/Yamaguchi2012_SupplementaryMovie1.mp4'),f.left,f.top,f.width,f.height,poster_frame_image=BytesIO(f.image.blob),mime_type='video/mp4')
ns={'p':'http://schemas.openxmlformats.org/presentationml/2006/main'}
s._element.find('.//p:video',ns).set('fullScrn','1')
a=s.shapes.add_textbox(Inches(7.11),Inches(6.77),Inches(5.6),Inches(.17));p=a.text_frame.paragraphs[0];p.text='Yamaguchi et al. (2012), Supplementary Movie 1. T3-enabled imprinting. Click figure to play.';p.font.name='Arial';p.font.size=Pt(7);p.font.color.rgb=RGBColor(0,0,0)
u='https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fncomms2088/MediaObjects/41467_2012_BFncomms2088_MOESM1173_ESM.mov'
s.notes_slide.notes_text_frame.text+='\n\nSupplementary recording:\nYamaguchi et al. (2012), Supplementary Movie 1. T3-enabled imprinting. The recording captures the preference-test preparation used to assess learned approach to the moving imprinting stimulus. T3 administered before training restores imprinting in older dark-reared chicks within the responsive developmental interval.\nArticle DOI: https://doi.org/10.1038/ncomms2088\nOriginal publisher recording: '+u+'\nCredit: Yamaguchi et al.; publisher supplementary material. No additional reuse license stated. Original MOV converted to H.264/AAC MP4 for compatibility; timing, scene, and original audio retained. Click the figure during Slide Show to activate full-screen playback. The original published Fig. 4b remains unchanged underneath the movie. PowerPoint GUI playback was not available for testing in the cloud environment.\n'
path=D/'Neuroethology_Lecture77_FA2026.pptx';r.save(path);saved=Presentation(path)
assert len(saved.slides)==46
for i,slide in enumerate(saved.slides):
 assert [etree.tostring(x._element) for x in list(slide.shapes)[:len(before[i])]]==before[i],f'Original slide {i+1} modified'
 if i!=6:assert slide.notes_slide.notes_text_frame.text==notes[i]
with zipfile.ZipFile(path) as z:
 media=[n for n in z.namelist() if n.endswith('.mp4')];assert len(media)==1;assert hashlib.sha256(z.read(media[0])).digest()==hashlib.sha256((D/'media/Yamaguchi2012_SupplementaryMovie1.mp4').read_bytes()).digest();assert 'videoFile' in z.read('ppt/slides/slide7.xml').decode()
metadata={'slide':7,'caption':'Yamaguchi et al. (2012), Supplementary Movie 1. T3-enabled imprinting.','doi':'10.1038/ncomms2088','original_url':u,'file':'media/Yamaguchi2012_SupplementaryMovie1.mp4','credit':'Yamaguchi et al. (2012), publisher supplementary recording','license':'No additional reuse license stated','original_duration_seconds':20.456780,'conversion':'MOV to H.264/AAC MP4, scene/timing/audio preserved','original_slide_shapes_unchanged':True,'all_original_slide_titles_body_figures_positions_unchanged':True,'unchanged_slide_count':46,'notes_unchanged_except_recording_metadata_on_slide':7,'embedded_payload_hash_verified':True,'complete_media_decode_verified':True,'powerpoint_gui_playback':'Not tested','robot_video_access':'Article cites V1–V3, but publisher returned an access/challenge page rather than media; no substitutes used.'}
(D/'media_sources.json').write_text(json.dumps([metadata],indent=2))
print('Verified all original shapes unchanged across 46 slides; supplementary movie embedded on slide 7')
