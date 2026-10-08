"""Reproduce original PDF crops; only rotate the two sideways source figures."""
import json, subprocess, sys
from pathlib import Path
from PIL import Image
here = Path(__file__).resolve().parent
root = here.parents[1]
for manifest in ['crops.json', 'extra-crops.json']:
    for row in json.loads((here/manifest).read_text()):
        output = here/row['out']
        subprocess.run([sys.executable, str(root/'tools/crop_figure.py'), str(here/row['pdf']), str(row['page']), '--dpi', '300', '--box', *map(str, row['box']), '-o', str(output)], check=True)
        rotation = row.get('rotation_degrees', 0)
        if rotation:
            assert rotation == 270
            with Image.open(output) as original:
                original.transpose(Image.Transpose.ROTATE_270).save(output)
