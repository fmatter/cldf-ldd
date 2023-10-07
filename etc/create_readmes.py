import json
from pycldf.terms import Terms
from csvw.metadata import Table
from pathlib import Path
import yaml
from importlib_resources import files  # pragma: no cover
from clldutils.misc import slug


cldf_path = files("cldf_ldd") / "components"

keys = yaml.load(open(cldf_path / "keys.yaml", "r"), Loader=yaml.SafeLoader)
key_dict = {}
for source, col1, target, col2 in keys:
    key_dict.setdefault(source, {})
    key_dict[source][col1] = target


def to_camel_case(snake_str):
    return "".join(x.capitalize() for x in snake_str.lower().split("_"))


def to_lower_camel_case(snake_str):
    # We capitalize the first letter of each component except the first one
    # with the 'capitalize' method and join them together.
    camel_string = to_camel_case(snake_str)
    return snake_str[0].lower() + camel_string[1:]

def colrow(col, fks, pk, terms):
    dt = '`{}`'.format(col.datatype.base if col.datatype else 'string')
    if col.separator:
        dt = 'list of {} (separated by `{}`)'.format(dt, col.separator)
    desc = col.common_props.get('dc:description', '').replace('\n', ' ')
    if not desc:
        term = terms.get(to_lower_camel_case(col.name))
        if term:
            desc = term.comment().replace("\n", " ")
    if col.name in pk:
        desc = (desc + '<br>') if desc else desc
        desc += 'Primary key'
    # else:
    #     input(col)
    #     input(fks)
    # elif col.propertyUrl \
    #         and col.propertyUrl.uri == "http://cldf.clld.org/v1.0/terms.rdf#source" \
    #         and 'dc:source' in ds.properties:
    #     desc = (desc + '<br>') if desc else desc
    #     desc += 'References [{}::BibTeX-key]({}{})'.format(
    #         ds.properties['dc:source'], rel_path, ds.properties['dc:source'])

    return ' | '.join([
        '[{}]({})'.format(col.name, col.propertyUrl)
        if col.propertyUrl else '`{}`'.format(col.name),
        dt,
        desc,
    ])


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
        row = colrow(col, key_dict.get(str(table.url), {}), ["ID"], terms)
        if table_url in key_dict and str(col) in key_dict[table_url]:
            target = key_dict[table_url][str(col)]
            if target.lower() == target:
                row += f"<br>References {target}."
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
