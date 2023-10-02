# cldf-ldd

cldf-ldd is a collection of [CLDF](https://cldf.clld.org/) components for modeling typical corpora resulting from descriptive fieldwork.

## Installation

```shell
pip install cldf_ldd
```


## Usage

Adding [components](components) to a CLDF dataset:

```python
from cldf_ldd.components import StemTable
...
args.writer.cldf.add_component(StemTable)
...
args.writer.objects[StemTable["url"]].append({...})
```

Adding [foreign keys](foreignkeys.md):

```python
from cldf_ldd import add_keys
...
add_keys(args.writer.cldf)
```

Adding [additional columns](columns.md) to native tables:
```python
from cldf_ldd import add_columns
...
add_columns(args.writer.cldf)
```
