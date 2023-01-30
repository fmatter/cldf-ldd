import json
from pycldf.terms import Terms
from csvw.metadata import Table
from pathlib import Path
from cldfspec.commands.component_readmes import colrow
from pycldf.terms import Terms


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
    TERMS = Terms(Path("../cldf/cldf") / "terms.rdf")
    for col in table.tableSchema.columns:
        res.append(colrow(col, table.tableSchema.primaryKey, TERMS))
    return "\n".join(res)


for p in Path("src/cldf_ldd/components").glob("*/*.json"):
    print(p)
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
