"""Top-level package for cldf-ldd."""
from cldf_ldd.cldf import *
import functools
import re

try:
    from importlib.resources import files  # pragma: no cover
except ImportError:  # pragma: no cover
    from importlib_resources import files  # pragma: no cover

__author__ = "Florian Matter"
__email__ = "fmatter@mailbox.org"
__version__ = "0.0.1.dev"


__all__ = ["MorphTable", "POSTable"]


def valid_parts(name, dataset, table, column, row):
    value = row[column.name]
    if value and None in value:
        raise ValueError(f"None in {value} in column {column}")


validators = [
    (
        None,
        "http://cldf.clld.org/v1.0/terms.rdf#segments",
        functools.partial(valid_parts, "Segments"),
    ),
]


def validate(ds):
    ds.validate(validators=validators)
