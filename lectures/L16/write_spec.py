"""Validate the authored Lecture 16 JSON; build.py performs the PowerPoint build."""
import json
from pathlib import Path
spec=json.loads(Path(__file__).with_name('lecture.json').read_text())
assert spec['lecture']==16 and len(spec['slides'])==44
print('Lecture 16 authored source: 44 content slides')
