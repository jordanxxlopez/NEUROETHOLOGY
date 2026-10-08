"""Validate the authored Lecture 34 JSON; build.py builds the PowerPoint."""
import json
from pathlib import Path
spec=json.loads(Path(__file__).with_name('lecture.json').read_text())
assert spec['lecture']==34 and len(spec['slides'])==44
print('Lecture 34 authored source: 44 content slides')
