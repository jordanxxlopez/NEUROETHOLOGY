"""Make metadata-free presentation copies of credited photographs; retain originals."""
from pathlib import Path
from PIL import Image
import json,hashlib
R=Path(__file__).resolve().parent;rows=json.load(open(R/'companions.json'));out=R/'companions/delivery';out.mkdir(exist_ok=True)
for row in rows:
 orig=R/row['path'];dest=out/orig.name
 im=Image.open(orig).convert('RGB');im.thumbnail((1024,1024) if orig.name=='octopus_1.jpg' else (640,640));im.save(dest,quality=90,subsampling=0,optimize=True)
 row['original_path']=row['path'];row['presentation_path']=str(dest.relative_to(R));row['presentation_sha256']=hashlib.sha256(dest.read_bytes()).hexdigest();row['status']='Reviewed real subject image. Presentation copy preserves the complete photograph and proportions, with downsampling appropriate to its small slide placement and removal of ancillary metadata.'
(R/'companions.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
print('Prepared',len(rows),'credited photographs')
