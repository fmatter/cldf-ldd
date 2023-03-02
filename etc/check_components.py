import yaml
import json
from pathlib import Path

PKG = "cldf_ldd"

comp_path = Path("src/cldf_ldd/components")


filenames = yaml.load(open("etc/filenames.yaml"), Loader=yaml.SafeLoader)
for handle, name in filenames.items():
    handle_path = comp_path / handle
    if not handle_path.is_dir():
        print("creating folder", handle_path)
        handle_path.mkdir()
    md_path = handle_path / f"{name}-metadata.json"
    desc_path = handle_path / "description.md"
    if not md_path.is_file():
        print("does not exist:", md_path)
    if not desc_path.is_file():
        print("Creating", desc_path)
        with open(desc_path, "w") as f:
            f.write(f"# {handle.capitalize()}\n")
