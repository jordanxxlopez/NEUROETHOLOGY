"""Validate the authored Lecture 31 JSON; build.py builds the PowerPoint."""
import json
from pathlib import Path
spec=json.loads(Path(__file__).with_name('lecture.json').read_text())
assert spec['lecture']==31 and len(spec['slides'])==44
print('Lecture 31 authored source: 44 content slides')
