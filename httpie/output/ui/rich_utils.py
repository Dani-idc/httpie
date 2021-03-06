import os

from typing import Iterator
from contextlib import contextmanager

from rich.console import Console, RenderableType
from rich.highlighter import Highlighter


def render_as_string(renderable: RenderableType) -> str:
    """Render any `rich` object in a fake console and
    return a *style-less* version of it as a string."""

    with open(os.devnull, "w") as null_stream:
        fake_console = Console(
            file=null_stream,
            record=True
        )
        fake_console.print(renderable)
        return fake_console.export_text()


@contextmanager
def enable_highlighter(
    console: Console,
    highlighter: Highlighter,
) -> Iterator[Console]:
    """Enable a higlighter temporarily."""

    original_highlighter = console.highlighter
    try:
        console.highlighter = highlighter
        yield console
    finally:
        console.highlighter = original_highlighter
