"""Top-level package for cldf-ldd."""
import logging
import colorlog

handler = colorlog.StreamHandler(None)
handler.setFormatter(
    colorlog.ColoredFormatter("%(log_color)s%(levelname)-7s%(reset)s %(message)s")
)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.propagate = True
log.addHandler(handler)

__author__ = "Florian Matter"
__email__ = "fmatter@mailbox.org"
__version__ = "0.0.1.dev"


def run_method(one, two, *args, **kwargs):
    """A docstring."""
    print(f"{one}, {two}, and then some.")
    return 5
