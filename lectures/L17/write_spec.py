"""Validate the authored Lecture 17 JSON; build.py builds the PowerPoint."""
import json
from pathlib import Path
spec=json.loads(Path(__file__).with_name('lecture.json').read_text())
assert spec['lecture']==17 and len(spec['slides'])==44
print('Lecture 17 authored source: 44 content slides')
