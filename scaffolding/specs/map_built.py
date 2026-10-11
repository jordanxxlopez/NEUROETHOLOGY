"""Map built slide numbers to the spec key they came from: ('body', original slide) or ('insert', after).

    python scaffolding/specs/map_built.py 35 9 32 38
"""
import importlib.util
import sys
from pathlib import Path

n = int(sys.argv[1])
built = [int(x) for x in sys.argv[2:]]
spec = importlib.util.spec_from_file_location(f"L{n}", Path(__file__).parent / f"L{n}.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
after = sorted(i["after"] for i in m.inserts)
table = {}
b = 1
for orig in range(2, 47):
    b += 1
    table[b] = ("body", orig)
    if orig in after:
        b += 1
        table[b] = ("insert", orig)
for k in built:
    print(k, table.get(k))
