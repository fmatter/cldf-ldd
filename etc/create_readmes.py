import json
from pycldf.terms import Terms
from csvw.metadata import Table
from pathlib import Path
from cldfspec.commands.component_readmes import colrow
import yaml
from importlib_resources import files  # pragma: no cover

cldf_path = files("cldf_ldd") / "components"

keys = yaml.load(open(cldf_path / "keys.yaml", "r"), Loader=yaml.SafeLoader)
key_dict = {}
for source, col1, target, col2 in keys:
    key_dict.setdefault(source, {})
    key_dict[source][col1] = target

def table2markdown(table, name):
    res = []
    res.append(
        "## {}: `{}`\n".format(
            name,
            table.url.string,
        )
    )
    if table.common_props.get("dc:description"):
        res.append(table.common_props["dc:description"] + "\n")
    res.append("Name/Property | Datatype | Cardinality | Description")
    res.append(" --- | --- | --- | --- ")
    terms = Terms(Path("../cldf/cldf") / "terms.rdf")
    table_url = str(table.url)
    for col in table.tableSchema.columns:
        row = colrow(col, table.tableSchema.primaryKey, terms)
        if table_url in key_dict and str(col) in key_dict[table_url]:
            target = key_dict[table_url][str(col)]
            row += f"\nReferences {target}."
        res.append(row)
    return "\n".join(res)


for p in Path("src/cldf_ldd/components").glob("*/*.json"):
    readme = ""
    desc_path = p.parent.joinpath("description.md")
    if desc_path.is_file():
        readme = desc_path.read_text(encoding="utf8")
    else:
        readme = ""
    cols = table2markdown(
        Table.fromvalue(json.loads(p.read_text(encoding="utf8"))),
        p.stem.replace("-metadata", ""),
    )
    p.parent.joinpath("README.md").write_text(readme + "\n\n" + cols, encoding="utf8")
