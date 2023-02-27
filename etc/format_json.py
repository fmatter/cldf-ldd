from pathlib import Path
import json

files = list(Path("src/cldf_ldd/components").glob("*/*.json"))

files.extend(list(Path("src/cldf_ldd/components").glob("*.json")))

for p in files:
    t = json.loads(p.read_text(encoding="utf8"))
    with open(p, "w") as f:
        json.dump(t, f, indent=4)
