"""Restore the full PowerPoint from lossless parts kept below GitHub's file limit."""
from pathlib import Path
import hashlib,json
B=Path(__file__).resolve().parent
m=json.loads((B/'manifest.json').read_text());out=B/m['filename'];tmp=out.with_suffix('.tmp');h=hashlib.sha256()
with tmp.open('wb')as f:
 for part in m['parts']:
  blob=(B/part['filename']).read_bytes()
  assert hashlib.sha256(blob).hexdigest()==part['sha256']
  f.write(blob);h.update(blob)
assert h.hexdigest()==m['sha256']
assert tmp.stat().st_size==m['size_bytes']
tmp.replace(out)
print(out)
